#!/usr/bin/env python3
"""R13 -- independent re-solution of practice/13-current-sheets-solenoids-and-vector-potential.md
numpy/scipy only.  Brute-force routes: sheets and slabs as continua of infinite wires (np.cross for
every direction), Ampere with signed enclosed current, numerical Biot-Savart over rings (trapezoid in
phi') and over straight segments (exact segment formula), finite-difference div/curl/grad/Laplacian,
Coulomb integrals for A, quad/brentq.  Prints PASS/FAIL for each quantity stated on the page."""
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy import integrate, optimize

mu0 = 4e-7*np.pi
X, Y, Z = np.eye(3)
NP = NF = 0


def chk(label, page, val, rtol=1e-3, atol=1e-12):
    global NP, NF
    p = np.atleast_1d(np.asarray(page, float)); v = np.atleast_1d(np.asarray(val, float))
    ok = p.shape == v.shape and np.allclose(v, p, rtol=rtol, atol=atol)
    NP += ok; NF += (not ok)
    f = lambda a: ("[" + ", ".join(f"{x:.7g}" for x in a) + "]") if a.size > 1 else f"{a[0]:.7g}"
    print(f"{'PASS' if ok else 'FAIL'}  {label}: page {f(p)} | computed {f(v)}")


def info(label, val):
    v = np.atleast_1d(np.asarray(val, float))
    print(f"INFO  {label}: " + ", ".join(f"{x:.7g}" for x in v))


# ---------------------------------------------------------------- brute-force field builders
TH, WTH = leggauss(80); TH = 0.25*np.pi*(TH + 1); WTH = 0.25*np.pi*WTH   # theta in (0, pi/2)
TT, JAC = np.tan(TH), 1/np.cos(TH)**2
XG, WG = leggauss(40)


def H_wires(I, p0, u, P):
    """infinite straight wires through points p0 (n,3) along unit u, current I along u: H at P."""
    d = P - p0
    rho = d - np.outer(d @ u, u)
    return np.asarray(I, float)[..., None]/(2*np.pi)*np.cross(u, rho)/np.sum(rho*rho, axis=1)[:, None]


def H_layer(K, xi, u, nrm, P):
    """plane r.nrm = xi carrying K (A/m) along u, built as a continuum of infinite wires along u;
    transverse coordinate s = s_P +- |d| tan(theta) covers (-inf, inf) in symmetric pairs."""
    u = np.asarray(u, float)/np.linalg.norm(u); nrm = np.asarray(nrm, float); w = np.cross(nrm, u)
    d = P @ nrm - xi; sc = abs(d); base = xi*nrm + (P @ u)*u
    plus = base + (P @ w + sc*TT)[:, None]*w
    minus = base + (P @ w - sc*TT)[:, None]*w
    return np.sum((H_wires(K, plus, u, P) + H_wires(K, minus, u, P))*(sc*JAC*WTH)[:, None], axis=0)


def H_slab(Jf, lo, hi, u, nrm, P):
    """slab lo < r.nrm < hi with current density Jf(xi) (A/m^2) along u: layers of wires, GL in xi."""
    xP = P @ np.asarray(nrm, float)
    bps = [lo] + ([xP] if lo < xP < hi else []) + [hi]
    H = np.zeros(3)
    for a, b in zip(bps[:-1], bps[1:]):
        for x, wt in zip(0.5*(b - a)*XG + 0.5*(a + b), 0.5*(b - a)*WG):
            H += wt*H_layer(Jf(x), x, u, nrm, P)
    return H


def B_rings(a, zc, I, P, M=720):
    """numerical Biot-Savart for coaxial rings (radius a, heights zc), current I counter-clockwise
    seen from +z; trapezoid rule in phi' (spectrally accurate for a closed loop)."""
    ph = 2*np.pi*np.arange(M)/M
    src = np.stack([a*np.cos(ph), a*np.sin(ph), 0*ph], 1)
    dl = np.stack([-a*np.sin(ph), a*np.cos(ph), 0*ph], 1)*(2*np.pi/M)
    zc = np.atleast_1d(np.asarray(zc, float)); B = np.zeros(3)
    for k in range(0, len(zc), 300):
        R = P[None, None, :] - (src[None, :, :] + zc[k:k + 300, None, None]*Z)
        Rn = np.linalg.norm(R, axis=2)
        B += np.sum(np.cross(np.broadcast_to(dl, R.shape), R)/Rn[..., None]**3, axis=(0, 1))
    return mu0*I/(4*np.pi)*B


def B_segments(A, Bp, I, P):
    """exact Biot-Savart of straight segments A->Bp (n,3) carrying I (well-conditioned form:
    mu0 I/(4 pi) (u x rho)/rho^2 [cos(angle at A) - cos(angle at B)])."""
    u = (Bp - A)/np.linalg.norm(Bp - A, axis=1)[:, None]
    R1, R2 = P - A, P - Bp
    rho = R1 - np.sum(R1*u, axis=1)[:, None]*u
    br = np.sum(R1*u, axis=1)/np.linalg.norm(R1, axis=1) - np.sum(R2*u, axis=1)/np.linalg.norm(R2, axis=1)
    return mu0*I/(4*np.pi)*np.sum(np.cross(u, rho)/np.sum(rho*rho, axis=1)[:, None]*br[:, None], axis=0)


def jac(Af, P, h):
    Jm = np.zeros((3, 3))
    for j in range(3):
        e = np.zeros(3); e[j] = h
        Jm[:, j] = (Af(P + e) - Af(P - e))/(2*h)
    return Jm


def curl(Af, P, h=1e-6):
    J = jac(Af, P, h); return np.array([J[2, 1] - J[1, 2], J[0, 2] - J[2, 0], J[1, 0] - J[0, 1]])


def div(Af, P, h=1e-6):
    return np.trace(jac(Af, P, h))


def grad(f, P, h=1e-6):
    return np.array([(f(P + h*e) - f(P - h*e))/(2*h) for e in np.eye(3)])


def lap(Af, P, h=1e-4):
    return (sum(Af(P + h*e) + Af(P - h*e) for e in np.eye(3)) - 6*Af(P))/h**2


# sanity of the segment formula: long z-directed segment, point on +x  ->  +y, mu0 I/(2 pi d)
_b = B_segments(np.array([[0, 0, -1e4]]), np.array([[0, 0, 1e4]]), 1.0, np.array([0.1, 0, 0]))
chk("self-test segment B-S (long wire, I=1, d=0.1): (Bx,By,Bz)", [0, mu0/(2*np.pi*0.1), 0], _b, 1e-6, 1e-15)

# ===================================================================== 13.1
print("\n== 13.1 one sheet, two points")
Hp1 = H_layer(8, 0, Y, Z, np.array([0, 0, 0.5])); Hp2 = H_layer(8, 0, Y, Z, np.array([3, -2, -40.]))
chk("H(P1) A/m", [4, 0, 0], Hp1, 1e-9, 1e-9)
chk("H(P2) A/m", [-4, 0, 0], Hp2, 1e-9, 1e-9)
chk("|B| = 4 mu0 (uT)", 5.027, mu0*np.linalg.norm(Hp1)*1e6, 1e-4)
Js = np.array([6, 8, 0.])
Ha = H_layer(np.linalg.norm(Js), 0, Js, Z, np.array([1.3, 2.1, 0.3]))
Hb = H_layer(np.linalg.norm(Js), 0, Js, Z, np.array([-2, 5, -7.]))
chk("(b) H above", [4, -3, 0], Ha, 1e-9, 1e-9)
chk("(b) H below", [-4, 3, 0], Hb, 1e-9, 1e-9)
chk("(b) |H| = |Js|/2 = 5", [5, 5], [np.linalg.norm(Ha), np.linalg.norm(Js)/2], 1e-9)
chk("(b) H.Js", 0, Ha @ Js, 0, 1e-9)
chk("jump z x (Ha-Hb) = Js", Js, np.cross(Z, Ha - Hb), 1e-9, 1e-9)

# ===================================================================== 13.2
print("\n== 13.2 crossing a sheet (MC)")
HL = np.array([2, -1, 0.]); PL = np.array([-0.01, 0.3, 0.2]); PR = np.array([0.01, 0.3, 0.2])
hsL = H_layer(3, 0, Z, X, PL); hsR = H_layer(3, 0, Z, X, PR)
chk("sheet's own field left / right (y comps)", [-1.5, 1.5], [hsL[1], hsR[1]], 1e-9)
Hext = HL - hsL; HR = Hext + hsR
chk("distant-source field (2, 0.5)", [2, 0.5, 0], Hext, 1e-9, 1e-9)
chk("key (b): H right = 2x+2y", [2, 2, 0], HR, 1e-9, 1e-9)
opts = {'a': [2, -4, 0], 'b': [2, 2, 0], 'c': [5, -1, 0], 'd': [2, -1, 3], 'e': [2, 0.5, 0], 'f': [-2, 2, 0]}
good = [k for k, v in opts.items() if np.allclose(np.cross(X, np.array(v) - HL), [0, 0, 3]) and v[0] == HL[0]]
chk("only option satisfying both BCs is (b) (1=yes)", 1, float(good == ['b']))
chk("(a) n x Js = -3y ; x x (H1-H2) = -3z", [0, -3, 0, 0, 0, -3],
    np.r_[np.cross(X, [0, 0, 3]), np.cross(X, np.array(opts['a']) - HL)], 1e-12, 1e-12)
chk("(c) x x (H1-H2) = 0", [0, 0, 0], np.cross(X, np.array(opts['c']) - HL), 0, 1e-12)
chk("(d) x x 3z = -3y", [0, -3, 0], np.cross(X, [0, 0, 3]), 0, 1e-12)
chk("(e) x x (H1-H2) = 1.5z ; (e) = average of sides", [0, 0, 1.5, 2, 0.5, 0],
    np.r_[np.cross(X, np.array(opts['e']) - HL), 0.5*(HL + HR)], 1e-12, 1e-12)
chk("(f) x x (-4x+3y) = 3z, but Hx flips", [0, 0, 3], np.cross(X, np.array(opts['f']) - HL), 0, 1e-12)

# ===================================================================== 13.3
print("\n== 13.3 solenoid inside a solenoid")
a1, n1, I1, a2, n2 = 0.02, 2000, 0.5, 0.01, 400
chk("(a) H = n1 I1 (A/m)", 1000, n1*I1)
chk("(a) B (mT)", 1.257, mu0*n1*I1*1e3, 5e-4)
Psi_a = integrate.quad(lambda r: mu0*n1*I1*2*np.pi*r, 0, a1)[0]
chk("(a) Psi = 16 pi^2 e-8 Wb ; ~1.58 uWb", [16*np.pi**2*1e-8, 1.58e-6], [Psi_a, Psi_a], 3e-3)
I2 = optimize.brentq(lambda i: n1*I1 + n2*i, -100, 100)
chk("(b) I2 (A), negative = clockwise seen from +z", -2.5, I2, 1e-12)
Psi_c = integrate.quad(lambda r: mu0*n1*I1*2*np.pi*r, a2, a1)[0]
chk("(c) Psi annulus = 12 pi^2 e-8 ; ~1.18 uWb", [12*np.pi**2*1e-8, 1.18e-6], [Psi_c, Psi_c], 4e-3)
ph = 0.7; rh = np.array([np.cos(ph), np.sin(ph), 0]); phh = np.array([-np.sin(ph), np.cos(ph), 0])
chk("BC at r=a2: r x (1000z - 0) = n2 I2 phi (phi comp)", n2*I2, np.cross(rh, 1000*Z) @ phh, 1e-12)
chk("BC at r=a1: r x (0 - 1000z) = n1 I1 phi (phi comp)", n1*I1, np.cross(rh, -1000*Z) @ phh, 1e-12)
zo = -1 + (np.arange(2*n1) + 0.5)/n1; zi = -1 + (np.arange(2*n2) + 0.5)/n2   # two 2-m coils
Pann = np.array([0.015, 0, 0]); Pcore = np.array([0.005, 0, 0])
Hann = (B_rings(a1, zo, I1, Pann) + B_rings(a2, zi, I2, Pann))/mu0
Hcore = (B_rings(a1, zo, I1, Pcore) + B_rings(a2, zi, I2, Pcore))/mu0
chk("B-S two 2-m coils: Hz in annulus (r=1.5 cm)", 999.8, Hann[2], 1e-4)
info("B-S two 2-m coils: Hz at r=0.5 cm (ideal 0; finite-length residue)", Hcore[2])

# ===================================================================== 13.4
print("\n== 13.4 toroid")
N4, I4, a4, b4, h4 = 600, 2.0, 0.04, 0.06, 0.02
pk = 2*np.pi*np.arange(N4)/N4
cyl = lambda r, p, z: np.stack([r*np.cos(p), r*np.sin(p), z + 0*p], 1)
C1, C2, C3, C4 = cyl(a4, pk, -h4/2), cyl(a4, pk, h4/2), cyl(b4, pk, h4/2), cyl(b4, pk, -h4/2)
SA, SB = np.vstack([C1, C2, C3, C4]), np.vstack([C2, C3, C4, C1])   # +z on inner wall, -z on outer
Hphi = {}
for r in (0.03, 0.05, 0.07):
    vals = []
    for pt in (np.pi/N4, 0.123):
        P = np.array([r*np.cos(pt), r*np.sin(pt), 0.0])
        vals.append(B_segments(SA, SB, I4, P) @ np.array([-np.sin(pt), np.cos(pt), 0])/mu0)
    Hphi[r] = vals
chk("B-S 600 rectangular turns: H_phi(5 cm), two azimuths", [3820, 3820], Hphi[0.05], 1e-4)
info("B-S H_phi at r=3 cm (two azimuths)", Hphi[0.03]); info("B-S H_phi at r=7 cm", Hphi[0.07])
chk("B-S: max |H_phi| at r=3 and 7 cm below 1e-11 A/m (page after fix) (1=yes)", 1,
    float(max(abs(np.r_[Hphi[0.03], Hphi[0.07]])) < 1e-11))
info("B-S |H| above the core (r=5 cm, z=1.5 cm)",
     np.linalg.norm(B_segments(SA, SB, I4, np.array([0.05, 0, 0.015])))/mu0)
Hamp = lambda r: N4*I4/(2*np.pi*r)
chk("H (A/m) at 4, 5, 6 cm", [4775, 3820, 3183], [Hamp(.04), Hamp(.05), Hamp(.06)], 2e-4)
chk("B (mT) at 4, 5, 6 cm", [6, 4.8, 4], [mu0*Hamp(r)*1e3 for r in (.04, .05, .06)], 1e-9)
chk("mu0 N I/(2 pi) (T m)", 2.4e-4, mu0*N4*I4/(2*np.pi), 1e-9)
chk("B(a)/B(b)", 1.5, Hamp(.04)/Hamp(.06), 1e-12)

# ===================================================================== 13.5
print("\n== 13.5 true/false")
H1m = H_layer(6, 0, Y, Z, np.array([0.2, -1, 1.])); H2m = H_layer(6, 0, Y, Z, np.array([0.2, -1, 2.]))
chk("(i) |H| at z = 1 m and 2 m (3.000000)", [3, 3], [np.linalg.norm(H1m), np.linalg.norm(H2m)], 1e-7)
z4 = -2 + (np.arange(4000) + 0.5)/1000
Bc = [B_rings(a, z4, 1.0, np.zeros(3))[2] for a in (0.01, 0.02)]
chk("(ii) B centre of 4-m coil, a=1,2 cm (mT)", [1.2566, 1.2566], np.array(Bc)*1e3, 5e-5)
chk("(ii) Psi = B pi a^2 (uWb): 0.395, 1.58", [0.395, 1.58], [Bc[0]*np.pi*1e-4*1e6, Bc[1]*np.pi*4e-4*1e6], 2e-3)
Hgen = H_layer(5, 0.4, np.array([1, -2, 0.]), Z, np.array([3, 1, -2.]))
chk("(iii) sheet field has no normal component (Hz)", 0, Hgen[2], 0, 1e-10)
B0 = 0.7
A1 = lambda P: 0.5*B0*np.array([-P[1], P[0], 0]); A2 = lambda P: B0*np.array([0, P[0], 0])
for P in (np.array([0.3, -1.2, 0.8]), np.array([-2.0, 0.7, 5.0])):
    chk(f"(iv) curl A1, curl A2 at {P}", [0, 0, .7, 0, 0, .7], np.r_[curl(A1, P), curl(A2, P)], 1e-8, 1e-9)
    chk("(iv) A2 - A1 = grad(B0 x y/2); div A1, div A2", np.r_[A2(P) - A1(P), 0, 0],
        np.r_[grad(lambda Q: 0.5*B0*Q[0]*Q[1], P), div(A1, P), div(A2, P)], 1e-8, 1e-9)
Bz3 = [B_rings(1.0, [0.0], 1.0, np.array([0, 0, z]))[2]*z**3 for z in (2, 4, 8, 16)]
chk("(v) Bz z^3 at z=2,4,8,16 (1e-7 T m^3)", [4.496, 5.737, 6.139, 6.247], np.array(Bz3)*1e7, 2e-4)
chk("(v) limit mu0/2 (1e-7)", 6.283, mu0/2*1e7, 1e-4)
Bz2 = [B_rings(1.0, [0.0], 1.0, np.array([0, 0, z]))[2]*z**2 for z in (2, 4, 8, 16)]
chk("(v) Bz z^2 keeps falling (1=yes)", 1, float(np.all(np.diff(Bz2) < 0)))

# ===================================================================== 13.6
print("\n== 13.6 parallel-plate line (find the error)")
w6, d6, I6 = 0.04, 0.002, 8.0; K6 = I6/w6
chk("K = I/w (A/m)", 200, K6)
Hfield6 = lambda P, Kv=K6, dd=d6: H_layer(Kv, dd, X, Y, P) + H_layer(-Kv, 0, X, Y, P)
chk("H between plates", [0, 0, -200], Hfield6(np.array([0.1, 0.001, 0])), 1e-9, 1e-9)
chk("H above / below", [0, 0, 0, 0, 0, 0], np.r_[Hfield6(np.array([0, 0.005, 0])), Hfield6(np.array([0, -0.3, 0]))], 0, 1e-9)
chk("B between (T), 251.3 uT", [2.5133e-4, 251.3], [mu0*200, mu0*200*1e6], 2e-4)
stud = 0.5*np.cross(K6*X, Y) + 0.5*np.cross(-K6*X, Y)
chk("student's sum (n=+y for both) = field above the line", Hfield6(np.array([0, 0.005, 0])), stud, 0, 1e-9)
chk("student's top/bottom terms 100z, -100z", [100, -100], [0.5*np.cross(K6*X, Y)[2], 0.5*np.cross(-K6*X, Y)[2]], 1e-12)
chk("BC at top: y x (H_above - H_gap) = 200x", [200, 0, 0],
    np.cross(Y, Hfield6(np.array([0, .005, 0])) - Hfield6(np.array([0, .001, 0]))), 1e-9, 1e-9)
Hc = Hfield6(np.array([0, 0.002, 0]), K6/2, 2*d6)
chk("(c) factor (2d, I/2)", 0.5, Hc[2]/(-200), 1e-9)
Pm = np.array([0, d6/2, 0])
Hstrip = np.array([integrate.quad(lambda zp, k=k: (H_wires(K6, np.array([[0, d6, zp]]), X, Pm)
                   + H_wires(-K6, np.array([[0, 0, zp]]), X, Pm))[0, k], -w6/2, w6/2, points=[0], limit=200)[0]
                   for k in range(3)])
chk("finite strips mid-gap B (T)", 2.4333e-4, mu0*abs(Hstrip[2]), 1e-4)
chk("ratio to mu0 K ; (2/pi) arctan(w/d)", [0.9682, 0.9682], [abs(Hstrip[2])/K6, 2/np.pi*np.arctan(w6/d6)], 1e-4)
chk("sheet model high by % (relative to exact) [page after fix: 3.3]", 3.3, (K6/abs(Hstrip[2]) - 1)*100, 1.5e-2)
info("exact below sheet model by %", (1 - abs(Hstrip[2])/K6)*100)

# ===================================================================== 13.7
print("\n== 13.7 graded slab")
J0, d7 = 400.0, 0.05
J7 = lambda x: J0*x/d7
K7 = integrate.quad(J7, 0, d7)[0]
chk("(a) K (A/m)", 10, K7, 1e-12)
Hy7 = lambda x: H_slab(J7, 0, d7, Z, X, np.array([x, 0.3, -0.2]))
Hamp7 = lambda x: -K7/2 + integrate.quad(J7, 0, min(max(x, 0), d7))[0]       # Ampere, H(-inf) = -K/2
form7 = lambda x: -5 if x < 0 else (5 if x > d7 else 4000*x**2 - 5)
for x in (-0.02, 0.0125, 0.025, 0.04, 0.07):
    h = Hy7(x)
    chk(f"(b,d) H at x={x} (wires | Ampere | page formula)", [form7(x)]*2 + [0, 0], [h[1], Hamp7(x), h[0], h[2]], 1e-9, 1e-9)
x0 = optimize.brentq(lambda x: Hy7(x)[1], 1e-4, d7 - 1e-4)
chk("(c) zero x0 (cm) = d/sqrt2", 3.5355, x0*100, 2e-5)
chk("(c) current left/right of x0", [5, 5], [integrate.quad(J7, 0, x0)[0], integrate.quad(J7, x0, d7)[0]], 1e-6)
chk("(d) H at 1.25, 2.5, 4 cm", [-4.375, -2.5, 1.4], [Hy7(x)[1] for x in (0.0125, 0.025, 0.04)], 1e-9)
fd7 = [(Hy7(x + 1e-5)[1] - Hy7(x - 1e-5)[1])/2e-5 for x in (0.01, 0.03, 0.045)]
chk("curl: dHy/dx at 1, 3, 4.5 cm (A/m^2)", [80, 240, 360], fd7, 1e-6)

# ===================================================================== 13.8
print("\n== 13.8 three sheets")
sh1 = lambda P: H_layer(4, 0, X, Z, P); sh2 = lambda P: H_layer(6, 1, Y, Z, P)
Pab = np.array([0.3, -0.7, 2.6]); Pbe = np.array([0.3, -0.7, -0.4])
Mx, My = H_layer(1, 2, X, Z, Pab), H_layer(1, 2, Y, Z, Pab)          # unit sheets on z = 2, field above
Js3 = np.linalg.lstsq(np.stack([Mx, My], 1), -(sh1(Pab) + sh2(Pab)), rcond=None)[0]
chk("(a) Js3 (A/m)", [-4, -6], Js3, 1e-9)
sh3 = lambda P: H_layer(Js3[0], 2, X, Z, P) + H_layer(Js3[1], 2, Y, Z, P)
Htot8 = lambda z: sh1(np.array([0.3, -0.7, z])) + sh2(np.array([0.3, -0.7, z])) + sh3(np.array([0.3, -0.7, z]))
chk("(a) H = 0 above and below", np.zeros(6), np.r_[Htot8(2.6), Htot8(-0.4)], 0, 1e-9)
chk("(b) sheet terms in 0<z<1: -2y, -3x, 3x-2y", [0, -2, 0, -3, 0, 0, 3, -2, 0],
    np.r_[sh1(np.array([0, 0, .5])), sh2(np.array([0, 0, .5])), sh3(np.array([0, 0, .5]))], 1e-9, 1e-9)
chk("(b) H in 0<z<1", [0, -4, 0], Htot8(0.5), 1e-9, 1e-9)
chk("(b) H in 1<z<2", [6, -4, 0], Htot8(1.5), 1e-9, 1e-9)
chk("(b) |B| (uT) 5.027, |H| 7.2111, |B| 9.062", [5.027, 7.2111, 9.062],
    [mu0*4e6, np.linalg.norm(Htot8(1.5)), mu0*np.linalg.norm(Htot8(1.5))*1e6], 1e-4)
chk("(c) jumps z x dH at z=0,1,2", [4, 0, 0, 0, 6, 0, -4, -6, 0],
    np.r_[np.cross(Z, Htot8(.5) - Htot8(-.4)), np.cross(Z, Htot8(1.5) - Htot8(.5)), np.cross(Z, Htot8(2.6) - Htot8(1.5))], 1e-9, 1e-9)

# ===================================================================== 13.9
print("\n== 13.9 two slabs and a sheet  (NEW parameters: slab 2 = -1.5 A/m^2 on 0<z<4, sheet -3y on z=1)")


def Hx9(z, Jb, zb, Ks=0.0, Ja=3.0, za=(-3, -1), zs=1.0):
    P = np.array([0.4, -0.9, z])
    H = H_slab(lambda _: Ja, za[0], za[1], Y, Z, P) + H_slab(lambda _: Jb, zb[0], zb[1], Y, Z, P)
    if Ks: H = H + H_layer(Ks, zs, Y, Z, P)
    return H


def Hx9_amp(z, Jb, zb, Ks=0.0, Ja=3.0, za=(-3, -1), zs=1.0):     # Ampere: H(-inf) = -K_tot/2, dHx/dz = Jy
    tot = Ja*(za[1] - za[0]) + Jb*(zb[1] - zb[0]) + Ks
    clip = lambda lo, hi: max(0.0, min(z, hi) - lo)
    return -tot/2 + Ja*clip(*za) + Jb*clip(*zb) + (Ks if z > zs else 0.0)


new = dict(Jb=-1.5, zb=(0, 4))
fa = lambda z: 0 if z < -3 else 3*z + 9 if z < -1 else 6 if z < 0 else 6 - 1.5*z if z < 4 else 0
fb = lambda z: 1.5 if z < -3 else 3*z + 10.5 if z < -1 else 7.5 if z < 0 else 7.5 - 1.5*z if z < 1 else 4.5 - 1.5*z if z < 4 else -1.5
for z in (-4, -2, -0.5, 0.5, 2, 3.5, 5):
    h = Hx9(z, **new)
    chk(f"(a) Hx at z={z} (wires | Ampere | page); Hy, Hz", [fa(z)]*2 + [0, 0], [h[0], Hx9_amp(z, **new), h[1], h[2]], 1e-9, 1e-9)
for z in (-4, -2, -0.5, 0.5, 2, 3, 3.5, 5):
    h = Hx9(z, Ks=-3, **new)
    chk(f"(b) Hx at z={z} (wires | Ampere | page)", [fb(z)]*2, [h[0], Hx9_amp(z, Ks=-3, **new)], 1e-9, 1e-9)
chk("(a) building blocks: slab1 below/above, slab2 below/above",
    [-3, 3, 3, -3], [H_slab(lambda _: 3, -3, -1, Y, Z, np.array([0, 0, -5.]))[0], H_slab(lambda _: 3, -3, -1, Y, Z, np.array([0, 0, 0.]))[0],
                     H_slab(lambda _: -1.5, 0, 4, Y, Z, np.array([0, 0, -1.]))[0], H_slab(lambda _: -1.5, 0, 4, Y, Z, np.array([0, 0, 5.]))[0]], 1e-9)
chk("(a) Hx at z=-1 and z=4 from wires: 6 (reaching 6 at z=-1), 0 (back to 0 at z=4)", [6, 0],
    [Hx9(-1.0, **new)[0], Hx9(4.0, **new)[0]], 1e-9, 1e-9)
chk("(a) slab-2 ramp 3-1.5z alone at z=1, 3", [1.5, -1.5],
    [H_slab(lambda _: -1.5, 0, 4, Y, Z, np.array([0, 0, z]))[0] for z in (1, 3)], 1e-9)
chk("(b) sheet's own field below/above", [1.5, -1.5],
    [H_layer(-3, 1, Y, Z, np.array([0, 0, z]))[0] for z in (0.2, 1.7)], 1e-9)
hb_, ha_ = Hx9(1 - 1e-7, Ks=-3, **new), Hx9(1 + 1e-7, Ks=-3, **new)
chk("(b) Hx just below/above z=1: 6 -> 3", [6, 3], [hb_[0], ha_[0]], 1e-6)
chk("(b) z x (H1 - H2) at sheet = -3y", [0, -3, 0], np.cross(Z, ha_ - hb_), 1e-5, 1e-6)
chk("(b) faces z=-3,-1,0,4 continuous: 1.5, 7.5, 7.5, -1.5 (below|above each)",
    [1.5, 1.5, 7.5, 7.5, 7.5, 7.5, -1.5, -1.5],
    [Hx9(zf + s, Ks=-3, **new)[0] for zf in (-3, -1, 0, 4) for s in (-1e-7, 1e-7)], 1e-6, 1e-6)
grid = np.linspace(-2.99, 3.99, 141)
chk("(c) without sheet: min Hx on -3<z<4 is > 0 (1=yes)", 1, float(min(Hx9(z, **new)[0] for z in grid) > 0))
zr = optimize.brentq(lambda z: Hx9(z, Ks=-3, **new)[0], 1.01, 3.99)
chk("(c) with sheet: zero at z (m)", 3.0, zr, 1e-9)
chk("(c) 3z+10.5 root (outside slab 1); 7.5-1.5z >= 6 on (0,1)", [-3.5, 6], [-10.5/3, 7.5 - 1.5*1], 1e-12)
chk("(c) no other zero: sign changes of Hx(b) on a fine grid = 1",
    1, float(np.sum(np.diff(np.sign([Hx9(z, Ks=-3, **new)[0] for z in np.linspace(-6.013, 7.017, 261)])) != 0)))
A9 = lambda P: 1.5*mu0*abs(P[2] - 1)*Y
for P in (np.array([0.2, -0.4, -0.6]), np.array([1.1, 0.5, 2.3])):
    Bc9 = curl(A9, P)
    chk(f"(d) curl A at z={P[2]} (1e-6 T) = mu0 x sheet field (wires)", np.r_[Bc9*1e6],
        mu0*H_layer(-3, 1, Y, Z, P)*1e6, 1e-6, 1e-9)
    chk(f"(d) Bx at z={P[2]} (1e-6 T), div A", [1.885 if P[2] < 1 else -1.885, 0], [Bc9[0]*1e6, div(A9, P)], 3e-4, 1e-12)
dl_, dr_ = (A9(np.array([0, 0, 1.0]))[1] - A9(np.array([0, 0, 1 - 1e-4]))[1])/1e-4, (A9(np.array([0, 0, 1 + 1e-4]))[1] - A9(np.array([0, 0, 1.0]))[1])/1e-4
chk("(d) slope jump of Ay at z=1 = 3 mu0 (Wb/m^2)", 3.7699e-6, dr_ - dl_, 1e-4)
chk("(d) J_s = -(jump)/mu0 (A/m, along y)", -3, -(dr_ - dl_)/mu0, 1e-9)
fdslope = [(Hx9(z + 1e-5, **new)[0] - Hx9(z - 1e-5, **new)[0])/2e-5 for z in (-2.5, -1.5, 0.5, 2.5)]
chk("check: dHx/dz in slabs at 4 points", [3, 3, -1.5, -1.5], fdslope, 1e-6)
chk("check: net current 6-6-3 and outside +-1.5", [-3, 1.5, -1.5], [3*2 - 1.5*4 - 3, Hx9(-8, Ks=-3, **new)[0], Hx9(9, Ks=-3, **new)[0]], 1e-9)
# overlap with the exam (Summer 2019 HE2 #2a-b: 4 A/m^2 on -2<x<-1, -2 A/m^2 on 1<x<3, sheet 2 A/m at x=0)
exam_nums = {4.0, -2.0, 2.0}; page_nums = {3.0, -1.5, -3.0, 1.5}
chk("new current data share no value with the exam's (1=yes)", 1, float(not (exam_nums & page_nums)))
# the OLD version (slab 2 = -2 on 0<z<3, sheet -2y) was itself correct:
old = dict(Jb=-2.0, zb=(0, 3))
chk("old version (b) Hx at z=-2, 0.5, 2, 4 (was 4, 6, 1, -1)", [4, 6, 1, -1], [Hx9(z, Ks=-2, **old)[0] for z in (-2, 0.5, 2, 4)], 1e-9)

# ===================================================================== 13.10
print("\n== 13.10 vector potentials of wire and solenoid")
I10 = 10.0
Aw = lambda P, r0=1.0: mu0*I10/(2*np.pi)*np.log(r0/np.hypot(P[0], P[1]))*Z
P10 = np.array([0.03, 0.04, 0.0])
chk("(a) B at (3,4,0) cm (uT) from curl A, r0=1", [-32, 24, 0], curl(Aw, P10)*1e6, 1e-6, 1e-6)
chk("(a) same with r0=0.37 m", [-32, 24, 0], curl(lambda P: Aw(P, 0.37), P10)*1e6, 1e-6, 1e-6)
Bbs = B_segments(np.array([[0, 0, -300.]]), np.array([[0, 0, 300.]]), I10, P10)
chk("(a) B by Biot-Savart of a long wire (uT); |B|=40", [-32, 24, 0, 40], np.r_[Bbs*1e6, np.linalg.norm(Bbs)*1e6], 1e-6, 1e-6)
for P in (P10, np.array([-0.2, 0.05, 1.3])):
    L = lap(Aw, P)
    chk(f"(a) div A, Laplacian Az / |d2Az/dx2| at {P}", [0, 0], [div(Aw, P), L[2]/abs(mu0*I10/(2*np.pi)/np.hypot(P[0], P[1])**2)], 0, 1e-5)
circ = integrate.quad(lambda t: grad(lambda Q: Aw(Q)[2], 0.03*np.array([np.cos(t), np.sin(t), 0])) @ np.array([np.cos(t), np.sin(t), 0])*0.03, 0, 2*np.pi)[0]
chk("(a) closed-circle integral of dAz/dr = -mu0 I", -mu0*I10, circ, 1e-6)
a10, b10, L10 = 0.01, 0.04, 1.0
corners = [np.array(c, float) for c in ([a10, 0, 0], [a10, 0, L10], [b10, 0, L10], [b10, 0, 0])]
varea = 0.5*sum(np.cross(corners[i], corners[(i + 1) % 4]) for i in range(4))
chk("(b) vector area of the oriented rectangle (along +y)", [0, L10*(b10 - a10), 0], varea, 1e-12, 1e-15)
for r0 in (1.0, 0.3):
    lint = sum(integrate.quad(lambda t: Aw(corners[i] + t*(corners[(i + 1) % 4] - corners[i]), r0) @ (corners[(i + 1) % 4] - corners[i]), 0, 1)[0] for i in range(4))
    chk(f"(b) loop integral of A (Wb), r0={r0}", 2.772589e-6, lint, 1e-7)
flux = integrate.dblquad(lambda z, x: B_segments(np.array([[0, 0, -300.]]), np.array([[0, 0, 300.]]), I10, np.array([x, 0, z]))[1],
                         a10, b10, 0, L10)[0]
chk("(b) flux of Biot-Savart B through the rectangle (Wb)", 2.772589e-6, flux, 1e-6)
Afin = lambda r, hl: 2*integrate.quad(lambda zp: mu0*I10/(4*np.pi)/np.hypot(r, zp), 0, hl, points=[r, 10*r, 100*r, 1000*r], limit=500)[0]
chk("(b) finite wire Az(1 cm), half-lengths 10 m and 1 km (Wb/m)", [1.5202e-5, 2.4412e-5], [Afin(a10, 10), Afin(a10, 1000)], 1e-4)
chk("(b) finite wire Az(1cm)-Az(4cm), 10 m and 1 km (Wb/m)", [2.772581e-6, 2.772589e-6],
    [Afin(a10, 10) - Afin(b10, 10), Afin(a10, 1000) - Afin(b10, 1000)], 2e-7)
R10, n10, Is10 = 0.01, 1000, 2.0; B010 = mu0*n10*Is10
Aphi = lambda r: 0.5*B010*r if r < R10 else B010*R10**2/(2*r)
Asol = lambda P: Aphi(np.hypot(P[0], P[1]))*np.array([-P[1], P[0], 0])/np.hypot(P[0], P[1])
chk("(c) B0 = mu0 n I (T)", 2.51327e-3, B010, 3e-6)
chk("(c) curl A inside (r=0.5cm) / outside (r=2cm) (T)", [0, 0, B010, 0, 0, 0],
    np.r_[curl(Asol, np.array([0.003, 0.004, 0.2])), curl(Asol, np.array([-0.012, 0.016, -1.0]))], 1e-6, 1e-10)
chk("(c) div A inside / outside", [0, 0], [div(Asol, np.array([0.003, 0.004, 0.2])), div(Asol, np.array([-0.012, 0.016, -1.0]))], 0, 1e-12)
chk("(c) A_phi(R) from both forms (Wb/m)", [1.25664e-5, 1.25664e-5], [0.5*B010*R10, B010*R10**2/(2*R10)], 5e-6)
chk("(d) A_phi(2R) (Wb/m)", 6.28319e-6, Aphi(2*R10), 1e-6)
for r in (0.015, 0.02, 0.05):
    lA = integrate.quad(lambda t: Asol(r*np.array([np.cos(t), np.sin(t), 0])) @ (r*np.array([-np.sin(t), np.cos(t), 0])), 0, 2*np.pi)[0]
    chk(f"(d) loop integral of A on r={r} (Wb)", 7.89568e-7, lA, 1e-6)
Kso = n10*Is10


def A_coul(r, hl=50.0):     # Coulomb integral of the sheet K phi_hat at radius R10, |z'|<hl, field point (r,0,0)
    f = lambda p: np.cos(p)*2*np.arcsinh(hl/np.sqrt(r*r + R10*R10 - 2*r*R10*np.cos(p)))
    return mu0*Kso*R10/(4*np.pi)*2*integrate.quad(f, 0, np.pi, limit=400)[0]


chk("check: Coulomb-integral A_phi at r=0.5,1,2,4 cm (Wb/m)", [6.28319e-6, 1.25664e-5, 6.28319e-6, 3.14159e-6],
    [A_coul(r) for r in (0.005, 0.01, 0.02, 0.04)], 5e-6)

# ===================================================================== 13.11
print("\n== 13.11 Helmholtz coils")
N11, a11, I11 = 50, 0.2, 2.0
Bax1 = lambda z: B_rings(a11, [0.0], N11*I11, np.array([0, 0, z]))[2]
Bpair = lambda z: B_rings(a11, [-a11/2, a11/2], N11*I11, np.array([0, 0, z]))[2]
chk("(a) B (mT) at z=0, 10, 30 cm", [0.314159, 0.2248, 0.05362], [Bax1(z)*1e3 for z in (0, .1, .3)], 2e-4)
chk("(a) centre = pi e-4 T", np.pi*1e-4, Bax1(0), 1e-9)
chk("(b) midpoint B (T); (4/5)^1.5 mu0NI/a", [4.495881e-4, 4.495881e-4], [Bpair(0), 0.8**1.5*mu0*N11*I11/a11], 1e-6)
chk("(b) factors 0.71554 and mu0NI/a = 6.28319e-4", [0.71554, 6.28319e-4], [0.8**1.5, mu0*N11*I11/a11], 1e-5)
hh = 1e-3
d1 = (Bpair(hh) - Bpair(-hh))/(2*hh); d2 = (Bpair(hh) - 2*Bpair(0) + Bpair(-hh))/hh**2
d2s = (Bax1(hh) - 2*Bax1(0) + Bax1(-hh))/hh**2
chk("(c) pair B'(0), B''(0) relative to single-coil B''", [0, 0], [d1, d2/abs(d2s)], 0, 1e-4)
chk("(c) single coil B''(0) (T/m^2)", -2.356e-2, d2s, 2e-4)
drop_pair = (1 - Bpair(0.02)/Bpair(0))*100; drop_one = (1 - Bax1(0.02)/Bax1(0))*100
chk("(c) drop 2 cm away: pair %, single %", [0.0114, 1.481], [drop_pair, drop_one], 5e-3)
info("(c) pair drop % at 2 cm (more digits)", drop_pair)
m11 = 2*N11*I11*np.pi*a11**2
chk("(d) m (A m^2) = 8 pi", [8*np.pi, 25.13], [m11, m11], 2e-4)
dip = lambda z: mu0*m11/(2*np.pi*z**3)
ex2, ex4 = Bpair(2.0), Bpair(4.0)
chk("(d) exact B at 2 m, 4 m (T)", [6.281448e-7, 7.853844e-8], [ex2, ex4], 2e-7)
chk("(d) dipole at 2 m, 4 m (T)", [6.283185e-7, 7.853982e-8], [dip(2.0), dip(4.0)], 2e-7)
chk("(d) ratios 0.999724, 0.999982; B(2)/B(4)", [0.999724, 0.999982, 7.99793], [ex2/dip(2), ex4/dip(4), ex2/ex4], 2e-6)
poly = lambda zc, M=4000: (np.stack([a11*np.cos(2*np.pi*np.arange(M)/M), a11*np.sin(2*np.pi*np.arange(M)/M), zc + 0*np.arange(M)], 1))
segB = lambda P: sum(B_segments(poly(zc), np.roll(poly(zc), -1, axis=0), N11*I11, P) for zc in (-a11/2, a11/2))
chk("check: polygon (4000-gon) Biot-Savart midpoint (mT)", 0.4496, segB(np.zeros(3))[2]*1e3, 1e-4)
chk("check: polygon (4000-gon) Biot-Savart at 2 m (1e-7 T)", 6.281447, segB(np.array([0, 0, 2.0]))[2]*1e7, 1e-6)
chk("check: one coil at z=10a, exact/dipole", 0.98519, Bax1(2.0)/(mu0*N11*I11*np.pi*a11**2/(2*np.pi*8)), 1e-5)
for s_ in (0.5, 1.5):
    zz = 20*a11
    exact = B_rings(a11, [-s_*a11/2, s_*a11/2], N11*I11, np.array([0, 0, zz]))[2]/dip(zz)
    chk(f"check: spacing s={s_}a, z=20a: ratio-1 vs 1.5((s/a)^2-1)(a/z)^2", 1.5*(s_**2 - 1)/400, exact - 1, 2e-2)

# ===================================================================== 13.12
print("\n== 13.12 finite solenoid")
l12, a12, N12, I12 = 0.30, 0.03, 600, 1.5; n12 = N12/l12; Bi = mu0*n12*I12
Bform = lambda z: Bi/2*((l12/2 - z)/np.hypot(a12, l12/2 - z) + (l12/2 + z)/np.hypot(a12, l12/2 + z))
Bquad = lambda z: integrate.quad(lambda zp: mu0*n12*I12*a12**2/(2*(a12**2 + (z - zp)**2)**1.5), -l12/2, l12/2, points=[z] if abs(z) < l12/2 else None)[0]
chk("(b) n, mu0 n I (T)", [2000, 3.76991e-3], [n12, Bi], 1e-6)
chk("(a,b) B(0) formula | z'-quad (T)", [3.69670e-3, 3.69670e-3], [Bform(0), Bquad(0)], 1e-6)
chk("(a,b) B(l/2) formula | z'-quad (T)", [1.87560e-3, 1.87560e-3], [Bform(l12/2), Bquad(l12/2)], 1e-6)
chk("(b) B(0)/mu0nI = 5/sqrt26, B(end)/mu0nI = 5/sqrt101, ratio", [0.980581, 0.497519, 0.50737],
    [Bform(0)/Bi, Bform(l12/2)/Bi, Bform(l12/2)/Bform(0)], 5e-6)
zr12 = -l12/2 + (np.arange(N12) + 0.5)*l12/N12
chk("check: 600 discrete rings B-S, centre and end (T)", [3.696702e-3, 1.875601e-3],
    [B_rings(a12, zr12, I12, np.zeros(3))[2], B_rings(a12, zr12, I12, np.array([0, 0, l12/2]))[2]], 2e-6)
chk("(b) very long coil: end value / mu0nI", 0.5, (lambda L: 0.5*L/np.hypot(a12, L))(1e4), 1e-7)
x12 = optimize.brentq(lambda x: x/np.sqrt(x*x + 1) - 0.99, 0.1, 100)
chk("(c) l/a >= 14.0358", 14.0358, 2*x12, 1e-5)
chk("(c) this coil (l/a=10) is 1.9 % below", 1.9, (1 - Bform(0)/Bi)*100, 3e-2)
m12 = N12*I12*np.pi*a12**2
chk("(d) m = 0.81 pi (A m^2)", [0.81*np.pi, 2.54469], [m12, m12], 1e-6)
for z, ep, dp, rp in ((1.5, 1.53763e-7, 1.50796e-7, 1.01967), (3.0, 1.89413e-8, 1.88496e-8, 1.00487)):
    d_ = mu0*m12/(2*np.pi*z**3)
    chk(f"(d) z={z}: exact (formula | quad), dipole, ratio", [ep, ep, dp, rp], [Bform(z), Bquad(z), d_, Bform(z)/d_], 2e-5)

print(f"\nTOTAL: {NP} PASS, {NF} FAIL")
