#!/usr/bin/env python3
"""Verification of every number, sign and direction on
content-src/practice/16-charge-conservation-and-displacement-current.md  (Lecture 16 practice page).

Rules followed (SPEC section 1): numpy/scipy only.
  * divergences and curls are centred finite differences of the fields as written;
  * charges and fluxes are numerical volume/surface integrals (tplquad / dblquad), and for
    closed surfaces the face-by-face sum is compared with the volume integral of the divergence;
  * electric fluxes of point charges through disks and cups are numerical surface integrals of
    D = q R/(4 pi R^3), compared with the solid-angle formula;
  * MMFs are numerical line integrals of the Biot-Savart field of the wire, compared with the
    Ampere-Maxwell value on two different surfaces;
  * time derivatives are centred finite differences; the leaky-capacitor circuit is integrated
    with solve_ivp;
  * every direction comes from an explicit np.cross or a dot product with the stated normal.
Output: L16.out (run: python3 L16.py > L16.out).
"""
import numpy as np
from scipy.integrate import quad, dblquad, tplquad, solve_ivp
from scipy.optimize import minimize_scalar

eps0 = 8.8541878128e-12
mu0 = 4e-7 * np.pi
XH, YH, ZH = np.eye(3)
TOL = dict(epsabs=1e-15, epsrel=1e-11)
NCHK = 0
FAILS = []


def check(label, got, want, rel=1e-6, ab=1e-15):
    global NCHK
    NCHK += 1
    ok = abs(got - want) <= max(ab, rel * abs(want))
    print(f"   [{'ok' if ok else 'FAIL'}] {label}: computed {got:.10g}  expected {want:.10g}")
    if not ok:
        FAILS.append(label)


def checkv(label, got, want, rel=1e-6, ab=1e-12):
    global NCHK
    NCHK += 1
    got = np.asarray(got, float)
    want = np.asarray(want, float)
    ok = np.linalg.norm(got - want) <= max(ab, rel * np.linalg.norm(want))
    print(f"   [{'ok' if ok else 'FAIL'}] {label}: computed {np.array2string(got, precision=7)}  expected {np.array2string(want, precision=7)}")
    if not ok:
        FAILS.append(label)


def head(s):
    print("=" * 96)
    print(s)
    print("=" * 96)


def fd(f, t, h):
    return (f(t + h) - f(t - h)) / (2 * h)


def div_fd(F, r, h=1e-6):
    return sum((F(r + h * e)[i] - F(r - h * e)[i]) / (2 * h) for i, e in enumerate(np.eye(3)))


def curl_fd(F, r, h=1e-6):
    Jm = np.zeros((3, 3))  # Jm[i, j] = dF_i/dx_j
    for j, e in enumerate(np.eye(3)):
        Jm[:, j] = (F(r + h * e) - F(r - h * e)) / (2 * h)
    return np.array([Jm[2, 1] - Jm[1, 2], Jm[0, 2] - Jm[2, 0], Jm[1, 0] - Jm[0, 1]])


def D_point(q, rq):
    """D field of a point charge q at rq (free space)"""
    def D(r):
        R = r - rq
        return q * R / (4 * np.pi * np.linalg.norm(R) ** 3)
    return D


def flux_hdisk(D, zc, R):
    """flux of D through the horizontal disk z = zc, radius R, normal +z"""
    v, _ = dblquad(lambda rho, ph: D(np.array([rho * np.cos(ph), rho * np.sin(ph), zc]))[2] * rho,
                   0, 2 * np.pi, 0, R, **TOL)
    return v


def circ_hcircle(H, zc, R):
    """circulation of H around the horizontal circle (centre on the z axis), CCW seen from +z"""
    def f(ph):
        r = np.array([R * np.cos(ph), R * np.sin(ph), zc])
        dl = R * np.array([-np.sin(ph), np.cos(ph), 0.0])
        return H(r) @ dl
    v, _ = quad(f, 0, 2 * np.pi, limit=200, **TOL)
    return v


# =====================================================================================
head("16.1 Charge piling up in a cylinder (easy)")
def J1(r):
    x, y, z = r
    rr = np.hypot(x, y)
    return np.array([2 * rr * x, 2 * rr * y, -4 * z])   # 2 r^2 r-hat - 4 z z-hat


for rr, ph, z in [(0.2, np.pi / 6, 1.0), (1.0, 0.3, 0.5), (0.5, 2.0, 1.7)]:
    p = np.array([rr * np.cos(ph), rr * np.sin(ph), z])
    d = div_fd(J1, p)
    check(f"div J at r = {rr} m (finite difference) vs 6r - 4 [A/m^3]", d, 6 * rr - 4)
    print(f"      d(rho)/dt = -div J = {-d:+.6f} A/m^3 at r = {rr} m -> {'GROWING' if -d > 0 else 'SHRINKING'}")
print(f"   d(rho)/dt = 4 - 6r vanishes at r = 2/3 = {2/3:.6f} m")
dQdt, _ = tplquad(lambda r, ph, zz: (4 - 6 * r) * r, 0, 2, 0, 2 * np.pi, 0, 0.5)
check("dQ/dt = int (4-6r) dV over r<0.5, 0<z<2 [A]", dQdt, np.pi)
side, _ = dblquad(lambda zz, ph: J1(np.array([0.5 * np.cos(ph), 0.5 * np.sin(ph), zz])) @ np.array([np.cos(ph), np.sin(ph), 0]) * 0.5,
                  0, 2 * np.pi, 0, 2)
top, _ = dblquad(lambda r, ph: J1(np.array([r * np.cos(ph), r * np.sin(ph), 2.0])) @ ZH * r, 0, 2 * np.pi, 0, 0.5)
bot, _ = dblquad(lambda r, ph: J1(np.array([r * np.cos(ph), r * np.sin(ph), 0.0])) @ (-ZH) * r, 0, 2 * np.pi, 0, 0.5)
check("side face r = 0.5 m: outward current [A] (= pi)", side, np.pi)
check("top face z = 2 m: outward current [A] (= -2 pi, i.e. 2 pi in)", top, -2 * np.pi)
check("bottom face z = 0: outward current [A]", bot, 0.0, ab=1e-12)
print(f"      J_r(0.5) = {2*0.25:.3f} A/m^2 on side area 2 pi (0.5)(2) = {2*np.pi*0.5*2:.6f} m^2 (= 2 pi);"
      f" J_z(2) = {-8:.0f} A/m^2 on top area pi/4 = {np.pi/4:.6f} m^2")
check("net outward current [A] = -dQ/dt", side + top + bot, -np.pi)
print(f"   ANSWER 16.1: d(rho)/dt = 4 - 6r A/m^3: +2.8 A/m^3 (growing) at r = 0.2 m, -2 A/m^3 (shrinking) at r = 1 m;"
      f" dQ/dt = +pi = {np.pi:.4f} A, the cylinder GAINS charge (side pi A out, top 2 pi A in)")

# =====================================================================================
head("16.2 Displacement current through a window (easy)")
E0, w, side_len = 1e4, 2 * np.pi * 1e6, 0.1
A2 = side_len ** 2
uE = np.array([0.6, 0.0, 0.8])


def E2f(r, t):
    return E0 * np.cos(w * t) * uE


amp = eps0 * w * E0
print(f"   eps0 omega E0 = {amp:.6f} A/m^2  (amplitude of dD/dt); components 0.6 and 0.8 -> x: {0.6*amp:.6f}, z: {0.8*amp:.6f} A/m^2")
for t in [0.1e-6, 0.37e-6]:
    dDdt = fd(lambda tt: eps0 * E2f(np.zeros(3), tt), t, 1e-12)
    checkv(f"dD/dt at t = {t*1e6:.2f} us vs -eps0 w E0 sin(wt)(0.6,0,0.8)", dDdt, -amp * np.sin(w * t) * uE, rel=1e-5)


def psiE(t):
    v, _ = dblquad(lambda y, x: eps0 * E2f(np.array([x, y, 0.0]), t) @ ZH, 0, side_len, 0, side_len)
    return v


print(f"   psi_E amplitude = 0.8 eps0 E0 A = {0.8*eps0*E0*A2:.6e} C")
for t in [0.25e-6, 0.1e-6, 0.75e-6]:
    Id = fd(psiE, t, 1e-11)
    check(f"I_d(t = {t*1e6:.2f} us) = d psi_E/dt (numeric) vs -0.8 eps0 w E0 A sin(wt) [A]", Id, -0.8 * amp * A2 * np.sin(w * t), rel=1e-5)
Iamp = 0.8 * amp * A2
print(f"   eps0 = {eps0:.4e} F/m;  psi_E amplitude = {0.8*eps0*E0*A2*1e10:.3f} x 10^-10 C")
check("exact form: eps0 omega E0 = 2 pi 1e10 eps0 [A/m^2]", 2*np.pi*1e10*eps0, amp)
check("exact form: I_d amplitude = 1.6 pi 1e8 eps0 [A]", 1.6*np.pi*1e8*eps0, 0.8*amp*A2)
print(f"   amplitude of I_d = {Iamp*1e3:.4f} mA; period = {2*np.pi/w*1e6:.3f} us")
for t in [0.25e-6, 0.75e-6, 1.25e-6]:
    print(f"      t = {t*1e6:.2f} us: sin(wt) = {np.sin(w*t):+.6f}, I_d = {-Iamp*np.sin(w*t)*1e3:+.4f} mA "
          f"({'-z' if -np.sin(w*t) < 0 else '+z'} through the window), E = {np.array2string(E2f(0, t), precision=6)} V/m (zero)")
print(f"   (wrong) using |E| instead of E_z: amplitude {amp*A2*1e3:.4f} mA (25% too high)")
print(f"   ANSWER 16.2: dD/dt = -{amp:.4f} sin(wt)(0.6 x + 0.8 z) A/m^2; I_d = -{Iamp*1e3:.3f} sin(wt) mA; amplitude {Iamp*1e3:.2f} mA;"
      f" largest at t = 0.25, 0.75, ... us, when E = 0; at t = 0.25 us it is 4.45 mA along -z")

# =====================================================================================
head("16.3 The missing displacement current (easy, find the error)")
A3, d3, er3, I3 = 20e-4, 0.5e-3, 4.0, 3e-3
eps3 = er3 * eps0
C3 = eps3 * A3 / d3
dVdt = I3 / C3
dEdt = dVdt / d3
print(f"   C = eps A/d = {C3*1e12:.3f} pF; dV/dt = I/C = {dVdt:.5e} V/s; dE/dt = I/(eps A) = {dEdt:.5e} V/(m s)")
check("dD/dt = eps dE/dt [A/m^2] = I/A", eps3 * dEdt, I3 / A3)
check("correct I_d = A dD/dt [A]", A3 * eps3 * dEdt, 3e-3)
check("student's I_d = eps0 A dE/dt [A]", A3 * eps0 * dEdt, 0.75e-3)
check("polarization current A dP/dt = (eps-eps0) A dE/dt [A]", A3 * (eps3 - eps0) * dEdt, 2.25e-3)
# Gauss route: D in the gap = rho_s = Q/A (independent of eps)
Qf = lambda t: I3 * t
check("Gauss route: A d(Q/A)/dt [A]", A3 * fd(lambda t: Qf(t) / A3, 1e-3, 1e-6), 3e-3)
print("   ANSWER 16.3: slip = eps0 used for D (dropped dP/dt); I_d = 3 mA = I; 0.75 mA vacuum part + 2.25 mA polarization current; MMF equal")

# =====================================================================================
head("16.4 What changes when fields vary (easy, true or false) -- numerical illustrations")
# (a) charging capacitor: conduction flux through a disk pierced by the lead vs a bag through the gap
Ia = 1.0
print(f"   (a) capacitor charged by I = {Ia} A: conduction current through flat disk = {Ia} A, through bag in the gap = 0 A;"
      f" displacement through the bag = dQ/dt = {Ia} A -> conduction alone is surface dependent: FALSE")
# (c) div of a curl vanishes identically (numerical, random smooth field)
rng = np.random.default_rng(1)
Fr = lambda r: np.array([np.sin(r[1] * r[2]) + r[0] ** 2 * r[1], np.cos(r[0]) * r[2] ** 3, np.exp(0.3 * r[0]) * r[1]])
for k in range(2):
    p = rng.uniform(-1, 1, 3)
    dc = div_fd(lambda r: curl_fd(Fr, r, 1e-4), p, 1e-4)
    check(f"(c) div(curl F) at random point {k+1}", dc, 0.0, ab=1e-6)
print("   (c) 0 = div J + d(div D)/dt = div J + d rho/dt: TRUE")
# (d) static B with nonzero divergence passes Faraday's divergence test
B0d = 1.0
Bd = lambda r: B0d * r
print(f"   (d) B = B0 (x,y,z) static: div B = {div_fd(Bd, np.array([0.3,-0.2,0.5])):.6f} B0 (nonzero, constant in time);"
      " d(div B)/dt = 0 is satisfied with E = 0, yet div B != 0 -> Faraday alone does not force div B = 0: FALSE")
# (e) displacement flux through a thin rectangle scales with its width w
dDdt_t = 7.0  # any finite tangential dD/dt [A/m^2]
for wid in [1e-2, 1e-4, 1e-6]:
    print(f"   (e) rectangle 1 m long, w = {wid:.0e} m: displacement current through it = {dDdt_t*wid:.1e} A -> 0 as w -> 0: FALSE")
print("   (b) eps0 dE/dt is nonzero in vacuum whenever E changes: TRUE")
print("   ANSWER 16.4: (a) F, (b) T, (c) T, (d) F, (e) F")

# =====================================================================================
head("16.5 Fields just outside a metal ball (easy, multiple choice)")
P5 = np.array([0.0, 0.6, 0.8])
n5 = P5 / np.linalg.norm(P5)
checkv("n-hat at P = position / radius", n5, [0, 0.6, 0.8])
print(f"   angle between n-hat and z-hat = {np.degrees(np.arccos(n5 @ ZH)):.3f} deg")
vecs = {1: np.array([0, 3.0, 4.0]), 2: np.array([5.0, 0, 0]), 3: np.array([0, 4.0, -3.0]), 4: np.array([0, 0, 5.0])}
for k, v in vecs.items():
    nd = n5 @ v
    nx = np.cross(n5, v)
    canE = np.linalg.norm(nx) < 1e-12
    canH = abs(nd) < 1e-12
    tang = v - nd * n5
    print(f"   ({k}) {v}: n.v = {nd:+.4f}, |n x v| = {np.linalg.norm(nx):.4f}, tangential part {np.array2string(tang, precision=4)} (|.| = {np.linalg.norm(tang):.4f})"
          f" -> can be E: {canE}, can be H: {canH}")
print("   -> (1) only E, (2) and (3) only H, (4) neither = option (a)")
print(f"   arithmetic: n.(3) = 0.6*4 + 0.8*(-3) = {0.6*4:.1f} - {0.8*3:.1f}; n x (3) x-comp = 0.6*(-3) - 0.8*4 = {0.6*-3:.1f} - {0.8*4:.1f} = {0.6*-3-0.8*4:.1f}")
rho5 = eps0 * (n5 @ (1e3 * vecs[1]))
check("rho_s = n.D for (1) as E in kV/m [C/m^2]", rho5, 5000 * eps0)
print(f"      rho_s = 5000 eps0 = {rho5*1e9:.3f} nC/m^2 (positive: E leaves the surface)")
Js5 = np.cross(n5, vecs[3])
checkv("J_s = n x H for (3) as H in A/m", Js5, [-5, 0, 0])
checkv("check: J_s x n = H_t (= vector (3))", np.cross(Js5, n5), vecs[3])
print(f"   ANSWER 16.5: (a); rho_s = {rho5*1e9:.1f} nC/m^2; J_s = {np.array2string(Js5, precision=3)} A/m = -5 x-hat A/m")

# =====================================================================================
head("16.6 Conduction versus displacement in soil (medium)")
sig6, er6, E06 = 0.01, 9.0, 20.0
eps6 = er6 * eps0
tau6 = eps6 / sig6
wc = sig6 / eps6
fc = wc / (2 * np.pi)
print(f"   eps = 9 eps0 = {eps6:.6e} F/m; relaxation time eps/sigma = {tau6*1e9:.4f} ns; omega_c = sigma/eps = {wc:.6e} rad/s; f_c = {fc/1e6:.4f} MHz")
check("1/(2 pi f_c) = eps/sigma [s]", 1 / (2 * np.pi * fc), tau6)
print(f"   conduction amplitude sigma E0 = {sig6*E06:.4f} A/m^2")
for f in [1e6, 2e9]:
    om = 2 * np.pi * f
    Jc = lambda t: sig6 * E06 * np.cos(om * t)
    Jd = lambda t: fd(lambda tt: eps6 * E06 * np.cos(om * tt), t, 1e-4 / om)
    ts = np.linspace(0, 2 * np.pi / om, 4001)
    ampd = max(abs(Jd(t)) for t in ts[::20])
    check(f"f = {f:.0e} Hz: displacement amplitude (numeric) vs omega eps E0 [A/m^2]", ampd, om * eps6 * E06, rel=2e-4)
    r = om * eps6 / sig6
    print(f"      ratio |dD/dt|/|J| = omega eps/sigma = f/f_c = {r:.5f};  conduction/displacement = {1/r:.4f}")
# phase: displacement peaks a quarter period before the field
om = 2 * np.pi * 1e6
res = minimize_scalar(lambda t: -(-eps6 * E06 * om * np.sin(om * t)), bounds=(-0.5 / 1e6, 0.5 / 1e6), method="bounded",
                      options=dict(xatol=1e-16))
print(f"   1 MHz: dD/dt has its maximum at t = {res.x*1e9:.3f} ns = {res.x*1e6:.4f} periods (field max at t = 0): leads by a quarter period")
check("time of dD/dt maximum [periods]", res.x * 1e6, -0.25, rel=1e-5)
# (d) at f_c
Jt = lambda t: sig6 * E06 * np.cos(wc * t) - wc * eps6 * E06 * np.sin(wc * t)
ts = np.linspace(0, 2 * np.pi / wc, 200001)
vals = Jt(ts)
k = np.argmax(vals)
check("f = f_c: max of J + dD/dt over a period [A/m^2] vs sqrt2 sigma E0", vals[k], np.sqrt(2) * sig6 * E06, rel=1e-8)
check("f = f_c: phase of the maximum, omega t mod 2pi vs 7pi/4", wc * ts[k], 7 * np.pi / 4, rel=1e-4)
for t in [0.0, 1.3e-9, 4.1e-9]:
    check(f"J + dD/dt = sqrt2 sigma E0 cos(wt + pi/4) at t = {t*1e9:.1f} ns", Jt(t), np.sqrt(2) * sig6 * E06 * np.cos(wc * t + np.pi / 4))
print(f"   (wrong) adding the two amplitudes would give {2*sig6*E06:.2f} A/m^2")
for f in [1e6, 2e9]:
    om = 2 * np.pi * f
    ts = np.linspace(0, 2 * np.pi / om, 400001)
    tot = sig6 * E06 * np.cos(om * ts) - om * eps6 * E06 * np.sin(om * ts)
    check(f"general amplitude of J + dD/dt at f = {f:.0e} Hz vs E0 sqrt(sigma^2 + omega^2 eps^2)", tot.max(),
          E06 * np.sqrt(sig6 ** 2 + (om * eps6) ** 2), rel=1e-8)
print(f"   ANSWER 16.6: J = 0.2 cos(wt) x A/m^2, dD/dt = -omega eps E0 sin(wt) x (leads by 90 deg); ratio omega eps/sigma; f_c = {fc/1e6:.2f} MHz,"
      f" 1/(2 pi f_c) = eps/sigma = {tau6*1e9:.2f} ns; 1 MHz: conduction {fc/1e6:.1f}x; 2 GHz: displacement {2e9/fc:.0f}x;"
      f" at f_c: {np.sqrt(2)*sig6*E06:.3f} cos(wt + pi/4) x A/m^2")

# =====================================================================================
head("16.7 Charging plates with a dielectric core (medium)")
a7, d7, I7 = 0.04, 2e-3, 0.5
A7 = np.pi * a7 ** 2
print(f"   plate area pi a^2 = {A7:.6e} m^2; C(air) = {eps0*A7/d7*1e12:.3f} pF")
jd = I7 / A7
print(f"   (a) dD/dt = I/(pi a^2) = {jd:.4f} A/m^2 along +z (the direction of the lead current)")
check("exact form: dD/dt = 312.5/pi [A/m^2]", 312.5 / np.pi, jd)
check("exact form: H(a/2) = I/(4 pi a) = 3.125/pi [A/m]", 3.125 / np.pi, I7 / (4 * np.pi * a7))
check("exact form: H(a) = I/(2 pi a) = 6.25/pi [A/m]", 6.25 / np.pi, I7 / (2 * np.pi * a7))


def Henc_air(r):
    """Ampere-Maxwell: displacement current through the disk of radius r (numerical) / (2 pi r)"""
    R = min(r, a7)
    Id, _ = quad(lambda s: jd * 2 * np.pi * s, 0, R, **TOL)
    return Id / (2 * np.pi * r)


for r in [0.02, 0.04, 0.08, 0.013]:
    want = I7 * r / (2 * np.pi * a7 ** 2) if r <= a7 else I7 / (2 * np.pi * r)
    check(f"(a) H_phi(r = {r*100:.1f} cm) numeric vs formula [A/m]", Henc_air(r), want)
print(f"      H(2 cm) = {Henc_air(0.02):.4f} A/m, H(8 cm) = {Henc_air(0.08):.4f} A/m (= I/(4 pi a) = {I7/(4*np.pi*a7):.4f}), H(a) = {Henc_air(a7):.4f} A/m (max)")
# differential check: (1/r) d(r H)/dr = dD_z/dt inside
for r in [0.01, 0.03]:
    g = lambda s: s * I7 * s / (2 * np.pi * a7 ** 2)
    check(f"(a) (1/r) d(r H)/dr at r = {r} m vs dD/dt", fd(g, r, 1e-7) / r, jd)
print(f"   lead field at 8 cm: I/(2 pi r) = {I7/(2*np.pi*0.08):.4f} A/m (same as in the gap at 8 cm)")
# (b) core eps = 3 eps0 for r < a/2: E common, D differs
ec = 3.0
dEdt7 = I7 / (eps0 * (ec * np.pi * (a7 / 2) ** 2 + np.pi * (a7 ** 2 - (a7 / 2) ** 2)))
print(f"   (b) dE/dt = {dEdt7:.6e} V/(m s); I = dE/dt * eps0 pi a^2 (3/4 + 3/4) -> check: {dEdt7*eps0*A7*1.5:.6f} A")
jcore, jair = ec * eps0 * dEdt7, eps0 * dEdt7
Icore = jcore * np.pi * (a7 / 2) ** 2
check("(b) displacement current through the core / I", Icore / I7, 0.5)
print(f"      dD/dt in core = {jcore:.4f} A/m^2, in air = {jair:.4f} A/m^2 (ratio {jcore/jair:.1f})")


def Henc_core(r):
    f = lambda s: (jcore if s < a7 / 2 else jair) * 2 * np.pi * s
    R = min(r, a7)
    pts = [a7 / 2] if R > a7 / 2 else None
    Id, _ = quad(f, 0, R, points=pts, limit=200, **TOL)
    return Id / (2 * np.pi * r)


def H_core_formula(r):
    if r <= a7 / 2:
        return I7 * r / (np.pi * a7 ** 2)
    if r <= a7:
        return I7 / (6 * np.pi * r) * (1 + 2 * r ** 2 / a7 ** 2)
    return I7 / (2 * np.pi * r)


for r in [0.01, 0.02, 0.03, 0.04, 0.08]:
    check(f"(b) H_phi(r = {r*100:.0f} cm) numeric vs piecewise formula [A/m]", Henc_core(r), H_core_formula(r))
check("(b) H(2 cm) with core = I/(2 pi a) [A/m]", Henc_core(0.02), I7 / (2 * np.pi * a7))
print(f"      with core: H(2 cm) = {Henc_core(0.02):.4f} A/m (x{Henc_core(0.02)/Henc_air(0.02):.3f} of air value), H(8 cm) = {Henc_core(0.08):.4f} A/m (unchanged)")
print(f"      continuity at r = a/2: {I7*(a7/2)/(np.pi*a7**2):.6f} vs {I7/(6*np.pi*(a7/2))*(1+0.5):.6f}; at r = a: {I7/(6*np.pi*a7)*3:.6f} vs {I7/(2*np.pi*a7):.6f}")
print(f"   ANSWER 16.7: (a) dD/dt = {jd:.1f} z A/m^2; H = I r/(2 pi a^2) phi (r<a), I/(2 pi r) phi (r>a); {Henc_air(0.02):.3f} A/m at 2 cm and at 8 cm"
      f" (CCW seen from +z); (b) one half; H(2 cm) = {Henc_core(0.02):.2f} A/m (doubled), H(8 cm) = {Henc_core(0.08):.3f} A/m")

# =====================================================================================
head("16.8 Charges and currents on a coax (medium)")
a8, b8 = 2e-3, 6e-3
P8, Q8 = np.array([1.2e-3, 1.6e-3, 0]), np.array([-3.6e-3, -4.8e-3, 0])
print(f"   |P| = {np.linalg.norm(P8)*1e3:.4f} mm (= a), |Q| = {np.linalg.norm(Q8)*1e3:.4f} mm (= b)")
EP, HP = np.array([18e3, 24e3, 0]), np.array([-24.0, 18.0, 0])
EQ, HQ = np.array([-6e3, -8e3, 0]), np.array([8.0, -6.0, 0])
nP = P8 / np.linalg.norm(P8)          # out of the inner conductor = +r-hat
nQ = -Q8 / np.linalg.norm(Q8)         # out of the outer conductor = toward the axis = -r-hat
checkv("n-hat at P (out of inner conductor)", nP, [0.6, 0.8, 0])
checkv("n-hat at Q (out of outer conductor, toward axis)", nQ, [0.6, 0.8, 0])
for lab, n, E, H in [("P", nP, EP, HP), ("Q", nQ, EQ, HQ)]:
    print(f"   {lab}: |n x E| = {np.linalg.norm(np.cross(n, E)):.3e} (E normal), n.H = {n @ H:.3e} (H tangential), n.E = {n@E:+.1f} V/m")
print(f"   arithmetic: n_P.H_P = {0.6*-24:.1f} + {0.8*18:.1f}; n_Q.H_Q = {0.6*8:.1f} - {0.8*6:.1f};"
      f" (n_P x H_P)_z = 0.6*18 - 0.8*(-24) = {0.6*18:.1f} + {0.8*24:.1f} = {0.6*18+0.8*24:.1f};"
      f" (n_Q x H_Q)_z = 0.6*(-6) - 0.8*8 = {0.6*-6:.1f} - {0.8*8:.1f} = {0.6*-6-0.8*8:.1f}")
print(f"   E_P = {np.linalg.norm(EP)/1e3:.0f} kV/m * n_P, E_Q = {-np.linalg.norm(EQ)/1e3:.0f} kV/m * n_Q; |H_P| = {np.linalg.norm(HP):.0f}, |H_Q| = {np.linalg.norm(HQ):.0f} A/m")
rhoP, rhoQ = eps0 * (nP @ EP), eps0 * (nQ @ EQ)
check("rho_s(P) [C/m^2] = 30000 eps0", rhoP, 3e4 * eps0)
check("rho_s(Q) [C/m^2] = -10000 eps0", rhoQ, -1e4 * eps0)
print(f"      rho_s(P) = {rhoP*1e9:+.2f} nC/m^2, rho_s(Q) = {rhoQ*1e9:+.2f} nC/m^2")
JsP, JsQ = np.cross(nP, HP), np.cross(nQ, HQ)
checkv("J_s(P) = n x H [A/m]", JsP, [0, 0, 30])
checkv("J_s(Q) = n x H [A/m]", JsQ, [0, 0, -10])
lam_in, lam_out = 2 * np.pi * a8 * rhoP, 2 * np.pi * b8 * rhoQ
I_in, I_out = 2 * np.pi * a8 * JsP[2], 2 * np.pi * b8 * JsQ[2]
check("exact form: lambda_in = 120 pi eps0 [C/m]", 120 * np.pi * eps0, lam_in)
check("exact form: I_in = 0.12 pi [A]", 0.12 * np.pi, I_in)
print(f"   lambda_in = {lam_in*1e9:+.4f} nC/m, lambda_out = {lam_out*1e9:+.4f} nC/m; I_in = {I_in:+.4f} A (z), I_out = {I_out:+.4f} A (z)")
check("lambda_in + lambda_out = 0", lam_in + lam_out, 0.0, ab=1e-20)
check("I_in + I_out = 0", I_in + I_out, 0.0, ab=1e-14)
check("Gauss: E_r(a) = lambda/(2 pi eps0 a) [V/m]", lam_in / (2 * np.pi * eps0 * a8), 30e3)
check("Gauss: E_r(b) = lambda/(2 pi eps0 b) [V/m]", lam_in / (2 * np.pi * eps0 * b8), 10e3)
check("Ampere: H(a) = I/(2 pi a) [A/m]", I_in / (2 * np.pi * a8), 30.0)
check("Ampere: H(b) = I/(2 pi b) [A/m]", I_in / (2 * np.pi * b8), 10.0)
Vab, _ = quad(lambda r: lam_in / (2 * np.pi * eps0 * r), a8, b8)
check("V(a) - V(b) = int_a^b E dr [V] = 30 kV/m * a ln 3", Vab, 30e3 * a8 * np.log(3))
check("C' = lambda/V [F/m] vs 2 pi eps0/ln(b/a)", lam_in / Vab, 2 * np.pi * eps0 / np.log(3))
print(f"      V = {Vab:.3f} V, C' = {lam_in/Vab*1e12:.3f} pF/m")
print(f"   (wrong) n = +r-hat at Q: rho_s = {eps0*((-nQ)@EQ)*1e9:+.2f} nC/m^2, J_s = {np.array2string(np.cross(-nQ, HQ), precision=3)} A/m (net charge and current: impossible)")
print(f"   ANSWER 16.8: n_P = n_Q = (0.6, 0.8, 0); rho_s(P) = {rhoP*1e9:.1f} nC/m^2, J_s(P) = 30 z A/m; rho_s(Q) = {rhoQ*1e9:.2f} nC/m^2, J_s(Q) = -10 z A/m;"
      f" +-{lam_in*1e9:.2f} nC/m; {I_in:.3f} A along +z on the inner, along -z on the outer")

# =====================================================================================
head("16.9 A leaky capacitor and its leads (hard)")
a9, d9, er9, R9, V09 = 0.05, 1e-3, 4.0, 1e7, 100.0
eps9 = er9 * eps0
sig9 = 2000 * eps0
A9 = np.pi * a9 ** 2
C9 = eps9 * A9 / d9
Rl = d9 / (sig9 * A9)
taud = eps9 / sig9
tau9 = 1 / (1 / (R9 * C9) + 1 / (Rl * C9))
print(f"   sigma = 2000 eps0 = {sig9:.5e} S/m; A = {A9:.6e} m^2")
print(f"   C = {C9*1e12:.3f} pF; R_leak = d/(sigma A) = {Rl/1e6:.4f} MOhm; eps/sigma = {taud*1e3:.4f} ms; R C = {R9*C9*1e3:.4f} ms")
check("R_leak C = eps/sigma [s]", Rl * C9, taud)
check("tau = C R R_l/(R + R_l) [s]", tau9, C9 * R9 * Rl / (R9 + Rl))
print(f"   tau = {tau9*1e3:.4f} ms; 1/tau = 1/(RC) + sigma/eps = {1/(R9*C9):.3f} + {1/taud:.3f} = {1/tau9:.3f} 1/s")
sol = solve_ivp(lambda t, V: -V / (C9 * R9) - V / (C9 * Rl), (0, 5e-3), [V09], rtol=1e-12, atol=1e-12, dense_output=True)
for t in [0.5e-3, 2e-3]:
    check(f"V(t = {t*1e3} ms) from ODE vs V0 exp(-t/tau) [V]", sol.sol(t)[0], V09 * np.exp(-t / tau9), rel=1e-8)
IR0, IL0 = V09 / R9, V09 / Rl
print(f"   t = 0: I_R = {IR0*1e6:.4f} uA (leads, along +z), I_leak = {IL0*1e6:.4f} uA (through the dielectric, along -z),"
      f" -dQ/dt = {(IR0+IL0)*1e6:.4f} uA")
# fields in the gap (top plate +V at z = d): E = -(V/d) z
t0 = 0.0
V = lambda t: sol.sol(t)[0]
Ez = lambda t: -V(t) / d9
Jz = sig9 * Ez(t0)
dDz = fd(lambda t: eps9 * Ez(t), 1e-4, 1e-7)   # check the sign at a small t (dense output)
dDz0 = eps9 * V09 / (tau9 * d9)
check("J_z at t = 0 [A/m^2] = -sigma V0/d", Jz, -sig9 * V09 / d9)
check("dD_z/dt at t = 1e-4 s (finite difference) vs +eps V/(tau d)", dDz, eps9 * V(1e-4) / (tau9 * d9), rel=1e-6)
check("dD_z/dt at t = 0 [A/m^2]", dDz0, (IR0 + IL0) / A9)
check("J_z + dD_z/dt at t = 0 = I_R/A [A/m^2]", Jz + dDz0, IR0 / A9)
print(f"      J = {Jz:.5e} z A/m^2 (down), dD/dt = {dDz0:.5e} z A/m^2 (up), sum = {Jz+dDz0:.5e} z A/m^2 (up) = I_R/A = {IR0/A9:.5e}")
for t in [0.7e-3, 3e-3]:
    s = sig9 * Ez(t) + fd(lambda tt: eps9 * Ez(tt), t, 1e-7)
    check(f"J_z + dD_z/dt at t = {t*1e3} ms vs I_R(t)/A", s, V(t) / R9 / A9, rel=1e-6)
H9 = lambda r, I: I * r / (2 * np.pi * a9 ** 2) if r <= a9 else I / (2 * np.pi * r)
# numeric Ampere-Maxwell: total current through disk of radius r
for r in [0.025, 0.05, 0.1]:
    Itot, _ = quad(lambda s: (Jz + dDz0) * 2 * np.pi * s, 0, min(r, a9), **TOL)
    check(f"H_phi(r = {r*100:.1f} cm, t = 0) numeric vs formula [A/m]", Itot / (2 * np.pi * r), H9(r, IR0))
print(f"      H(2.5 cm, 0) = {H9(0.025, IR0)*1e6:.3f} uA/m, H(a, 0) = {H9(a9, IR0)*1e6:.3f} uA/m; CCW seen from +z (total current along +z)")
# two-surface check around the upper lead, loop radius 7 cm above the capacitor
print(f"   two surfaces, loop r = 7 cm around the upper lead: flat disk -> I_R = {IR0*1e6:.3f} uA;"
      f" bag through the gap -> conduction {-IL0*1e6:+.3f} uA + displacement {+(IR0+IL0)*1e6:+.3f} uA = {IR0*1e6:.3f} uA")
# leads cut: R -> infinity
Vc = lambda t: V09 * np.exp(-t / taud)
for t in [1e-6, 1e-3]:
    Jcut = sig9 * (-Vc(t) / d9)
    s = Jcut + fd(lambda tt: eps9 * (-Vc(tt) / d9), t, 1e-9)
    print(f"      leads cut, t = {t*1e3} ms: J_z = {Jcut:.5e} A/m^2, dD_z/dt = {s-Jcut:+.5e} A/m^2")
    check(f"leads cut: (J + dD/dt)/|J| at t = {t*1e3} ms", s / abs(Jcut), 0.0, ab=1e-7)
Hc = IL0 * 0.025 / (2 * np.pi * a9 ** 2)
print(f"   leads cut: tau = eps/sigma = {taud*1e3:.1f} ms; conduction alone would give H(2.5 cm) = {Hc*1e6:.2f} uA/m, displacement alone {-Hc*1e6:.2f} uA/m; sum 0")
print(f"   sigma -> 0: J = 0 and dD/dt = I_R/A (the ordinary capacitor)")
print(f"   ANSWER 16.9: C = {C9*1e12:.0f} pF, R_leak = {Rl/1e6:.2f} MOhm, eps/sigma = 2 ms, tau = {tau9*1e3:.2f} ms, V = 100 exp(-t/tau) V;"
      f" I_R = {IR0*1e6:.0f} uA exp(-t/tau) along +z; J = -{-Jz*1e3:.3f} mA/m^2 z, dD/dt = +{dDz0*1e3:.3f} mA/m^2 z at t = 0;"
      f" sum {IR0/A9*1e3:.3f} mA/m^2 = I_R/A; H = I_R r/(2 pi a^2) phi, {H9(0.025, IR0)*1e6:.1f} uA/m at 2.5 cm; H = 0 if leads cut")

# =====================================================================================
head("16.10 MMF around a discharging pair (hard)")
b10, a10, Q0, tau10, h10, L10 = 0.03, 0.04, 10e-9, 5e-6, 0.06, 0.05
I0 = Q0 / tau10
Qt = lambda t: Q0 * np.exp(-t / tau10)
check("I(0) = -dQ/dt at t = 0 [A] (finite difference)", -fd(Qt, 0.0, 1e-9), 2e-3)
print(f"   I(t) = {I0*1e3:.3f} mA exp(-t/tau), flowing from the + sphere (z = +b) down to the - sphere: along -z")
c0 = b10 / np.hypot(a10, b10)
print(f"   cos(theta0) = b/sqrt(a^2+b^2) = {c0:.6f}")


def Dpair(Q):
    Dp, Dm = D_point(Q, np.array([0, 0, b10])), D_point(-Q, np.array([0, 0, -b10]))
    return lambda r: Dp(r) + Dm(r)


psi_disk = flux_hdisk(Dpair(1.0), 0.0, a10)
check("flux of D through the flat disk z = 0 per unit Q (numeric) vs -(1 - cos theta0)", psi_disk, -(1 - c0))
psi_p = flux_hdisk(D_point(1.0, np.array([0, 0, b10])), 0.0, a10)
check("  of which from +Q: -(1 - cos theta0)/2", psi_p, -(1 - c0) / 2)
mmf_disk = -I0 + (-psi_disk) * I0          # conduction -I, displacement d(psi)/dt = psi_disk * dQ/dt = -psi_disk * I
check("MMF via disk at t = 0 [A] = -I cos theta0", mmf_disk, -c0 * I0)
print(f"      disk: conduction {-I0*1e3:+.3f} mA, displacement {(-psi_disk)*I0*1e3:+.3f} mA, MMF = {mmf_disk*1e3:+.3f} mA (clockwise seen from +z)")
# cup: side wall r = a, -L<z<0 with C-oriented normal -r-hat; bottom disk z = -L with normal +z
D1 = Dpair(1.0)
side_c, _ = dblquad(lambda zz, ph: D1(np.array([a10 * np.cos(ph), a10 * np.sin(ph), zz])) @ (-np.array([np.cos(ph), np.sin(ph), 0])) * a10,
                    0, 2 * np.pi, -L10, 0, **TOL)
bot_c = flux_hdisk(D1, -L10, a10)
psi_cup = side_c + bot_c
check("flux through the cup per unit Q (C-oriented, numeric) vs psi_disk + 1", psi_cup, psi_disk + 1)
print(f"      cup: side {side_c:+.6f} Q, bottom {bot_c:+.6f} Q, total {psi_cup:+.6f} Q (= 0.6 Q); no conduction term")
mmf_cup = psi_cup * (-I0)
check("MMF via cup at t = 0 [A]", mmf_cup, -c0 * I0)
# Gauss on disk + cup closed surface (outward normals): psi_disk - psi_cup = Q_enc = -1
check("Gauss: psi_disk(+z) + psi_cup(outward) = Q_enc = -Q (per unit Q)", psi_disk - psi_cup, -1.0)


# Biot-Savart for the segment (current I along -z from z = +b to -b)
def H_seg(I, zlo, zhi):
    def H(r):
        def comp(k):
            f = lambda zp: np.cross(-ZH, r - np.array([0, 0, zp]))[k] / np.linalg.norm(r - np.array([0, 0, zp])) ** 3
            return quad(f, zlo, zhi, limit=200, **TOL)[0]
        return I / (4 * np.pi) * np.array([comp(0), comp(1), comp(2)])
    return H


Hs = H_seg(I0, -b10, b10)
Hp = Hs(np.array([a10, 0, 0]))
print(f"   Biot-Savart at (a,0,0): H = {np.array2string(Hp, precision=6)} A/m (phi-hat there = +y): H_phi = {Hp[1]*1e3:+.4f} mA/m")
check("H_phi on C = -(I/4 pi a)(2 cos theta0) [A/m]", Hp[1], -I0 / (4 * np.pi * a10) * 2 * c0)
check("exact form: H_phi(t = 0) = -15/pi mA/m [A/m]", -15e-3 / np.pi, Hp[1])
mmf_bs = circ_hcircle(Hs, 0.0, a10)
check("MMF by Biot-Savart (numerical line integral) [A]", mmf_bs, -c0 * I0)
# spherically symmetric radial current makes no H: thin shell of radial current about one charge
Pf = np.array([a10, 0.01, 0.02])
for s in [0.02, 0.09]:
    def comp(k):
        g = lambda th, ph: (np.cross(np.array([np.sin(th) * np.cos(ph), np.sin(th) * np.sin(ph), np.cos(th)]),
                                     Pf - s * np.array([np.sin(th) * np.cos(ph), np.sin(th) * np.sin(ph), np.cos(th)]))[k]
                            / np.linalg.norm(Pf - s * np.array([np.sin(th) * np.cos(ph), np.sin(th) * np.sin(ph), np.cos(th)])) ** 3 * np.sin(th))
        return dblquad(g, 0, 2 * np.pi, 0, np.pi, epsabs=1e-10, epsrel=1e-8)[0]
    Hshell = np.array([comp(0), comp(1), comp(2)])
    print(f"   Biot-Savart of a radial shell current (radius {s} m) at {Pf}: {np.array2string(Hshell, precision=3)} (zero: displacement current of each charge makes no H)")
    NCHK += 1
    if np.linalg.norm(Hshell) > 1e-6:
        FAILS.append("radial shell")
# (e) loop at z = h above the upper sphere
c1 = (h10 - b10) / np.hypot(a10, h10 - b10)
c2 = (h10 + b10) / np.hypot(a10, h10 + b10)
print(f"   (e) cos(theta1) = {c1:.6f}, cos(theta2) = 9/sqrt(97) = {c2:.6f}")
psi_e = flux_hdisk(Dpair(1.0), h10, a10)
check("(e) flux through the disk z = 6 cm per unit Q (numeric) vs (1-c1)/2 - (1-c2)/2", psi_e, (1 - c1) / 2 - (1 - c2) / 2)
print(f"      from +Q: {+(1-c1)/2:+.6f} Q (up), from -Q: {-(1-c2)/2:+.6f} Q (down), total {psi_e:+.6f} Q")
mmf_e = psi_e * (-I0)
check("(e) MMF at t = 0 = (I/2)(cos theta1 - cos theta2) [A]", mmf_e, I0 / 2 * (c1 - c2))
check("(e) MMF by Biot-Savart around C' [A]", circ_hcircle(Hs, h10, a10), mmf_e)
print(f"      MMF(C') = {mmf_e/I0:+.6f} I = {mmf_e*1e3:+.4f} mA at t = 0 (static Ampere: 0)")
print(f"   ANSWER 16.10: I = {I0*1e3:.0f} mA exp(-t/tau) along -z; MMF(C) = -I cos theta0 = -0.6 I = {mmf_disk*1e3:+.1f} mA at t = 0 (disk: -I + 0.4 I;"
      f" cup: 0 + d(0.6 Q)/dt); H_phi = {Hp[1]*1e3:+.2f} mA/m; MMF(C') = {mmf_e/I0:+.4f} I = {mmf_e*1e3:+.3f} mA")

# =====================================================================================
head("16.11 A region with no conduction current (hard, SP18 Exam 2 #1(iv) style)")
D0, T = 2e-9, 1e-3
DA = lambda r, t: D0 * (t / T) * np.array([r[0], r[1], 0])
DB = lambda r, t: D0 * np.array([r[0], r[1], t / T])
DC = lambda r, t: D0 * (t / T) * np.array([r[1], r[0], 0])
pts = [np.array([0.3, -0.7, 0.2]), np.array([-0.9, 0.4, 0.8])]
for name, Df, rho_want, drho_want in [("A", DA, lambda t: 2 * D0 * t / T, 2 * D0 / T), ("B", DB, lambda t: 2 * D0, 0.0),
                                      ("C", DC, lambda t: 0.0, 0.0)]:
    for p in pts:
        t = 0.4e-3
        rho = div_fd(lambda r: Df(r, t), p)
        drho = fd(lambda tt: div_fd(lambda r: Df(r, tt), p), t, 1e-5)
        check(f"D_{name}: rho at {p}, t = 0.4 ms [C/m^3]", rho, rho_want(t), ab=1e-17)
        check(f"D_{name}: d rho/dt [A/m^3] (needs div J = -d rho/dt)", drho, drho_want, rel=1e-5, ab=1e-12)
print(f"   D_A: rho = 2 D0 t/T = {2*D0*1e9:.0f} (t/T) nC/m^3, d rho/dt = 2 D0/T = {2*D0/T*1e6:.0f} uA/m^3 -> would need div J = -4 uA/m^3: NOT compatible")
print(f"   D_B: rho = 2 D0 = {2*D0*1e9:.0f} nC/m^3, static -> compatible (charge held in place)")
print("   D_C: rho = 0 -> compatible")
# for D_B: H = (D0/2T)(-y, x, 0)
HB = lambda r: D0 / (2 * T) * np.array([-r[1], r[0], 0])
for p in pts:
    checkv(f"D_B: curl of (D0/2T)(-y, x, 0) at {p} vs dD_B/dt = (D0/T) z", curl_fd(HB, p), fd(lambda tt: DB(p, tt), 0.5e-3, 1e-6), rel=1e-6, ab=1e-14)
# for D_A no H exists: div of dD_A/dt != 0
print(f"   D_A: div(dD_A/dt) = {div_fd(lambda r: fd(lambda tt: DA(r, tt), 0.5e-3, 1e-6), pts[0]):.4e} A/m^3 != 0 -> no H can have this curl")
# (c) H for D_C
HC = lambda r: D0 / (2 * T) * np.array([0, 0, r[1] ** 2 - r[0] ** 2])
for p in pts + [np.array([0.1, 0.95, -0.6])]:
    checkv(f"D_C: curl H at {p} vs dD_C/dt", curl_fd(HC, p), fd(lambda tt: DC(p, tt), 0.5e-3, 1e-6), rel=1e-6, ab=1e-14)
print(f"   D0/(2T) = {D0/(2*T):.3e} A/m;  H(1,0,0) = {HC(np.array([1.0,0,0]))[2]:+.3e} z A/m, H(0,1,0) = {HC(np.array([0,1.0,0]))[2]:+.3e} z A/m, H(0,0,z) = {HC(np.array([0,0,0.7]))[2]:.1e}")
# (d) the four equations
for p in pts:
    for t in [0.2e-3, 0.9e-3]:
        E = lambda r, tt=t: DC(r, tt) / eps0
        B = lambda r: mu0 * HC(r)
        check(f"(d) div D_C at {p}, t = {t*1e3} ms [= rho = 0]", div_fd(lambda r: DC(r, t), p), 0.0, ab=1e-17)
        check(f"(d) div B at {p}", div_fd(B, p), 0.0, ab=1e-18)
        checkv(f"(d) curl E vs -dB/dt (= 0, H static) at {p}, t = {t*1e3} ms", curl_fd(lambda r: E(r), p), np.zeros(3), ab=1e-6)
        checkv(f"(d) curl H vs J + dD/dt at {p}", curl_fd(HC, p), fd(lambda tt: DC(p, tt), t, 1e-6), rel=1e-6, ab=1e-14)
# Stokes check: unit square in the plane x = 0, corners (0,0,0),(0,1,0),(0,1,1),(0,0,1), normal +x
flux_sq, _ = dblquad(lambda zz, yy: fd(lambda tt: DC(np.array([0.0, yy, zz]), tt), 0.5e-3, 1e-6)[0], 0, 1, 0, 1)
sq = [np.array([0, 0, 0.0]), np.array([0, 1, 0.0]), np.array([0, 1, 1.0]), np.array([0, 0, 1.0])]
circ_sq = sum(quad(lambda s: HC(sq[i] + s * (sq[(i + 1) % 4] - sq[i])) @ (sq[(i + 1) % 4] - sq[i]), 0, 1)[0] for i in range(4))
print(f"   Stokes check: (y-hat then z-hat edges -> normal {np.cross(YH, ZH)}) displacement current through the square = {flux_sq*1e6:.6f} uA")
check("Stokes check: circulation of H around the unit square in x = 0 [A] = flux of dD_C/dt", circ_sq, flux_sq)
check("Stokes check value [A] = D0/(2T)", flux_sq, D0 / (2 * T))
# (e) divergence of Faraday
B0 = 1e-3
B1 = lambda r, t: B0 * (t / T) * np.array([r[0], r[1], 0])
B2 = lambda r, t: B0 * np.array([r[0], r[1], 0])
p = pts[0]
d1 = fd(lambda tt: div_fd(lambda r: B1(r, tt), p), 0.5e-3, 1e-5)
d2 = fd(lambda tt: div_fd(lambda r: B2(r, tt), p), 0.5e-3, 1e-5)
check("(e) d(div B1)/dt = 2 B0/T (nonzero -> Faraday impossible)", d1, 2 * B0 / T, rel=1e-5)
check("(e) d(div B2)/dt = 0 (Faraday allows it)", d2, 0.0, ab=1e-9)
check("(e) div B2 = 2 B0 (nonzero -> needs magnetic charge)", div_fd(lambda r: B2(r, 0.0), p), 2 * B0)
print("   ANSWER 16.11: (a) only d rho/dt = 0 must hold; (b) D_A impossible (d rho/dt = 4 uA/m^3), D_B allowed (static rho = 4 nC/m^3),"
      " D_C allowed (rho = 0); (c) H = 1e-6 (y^2 - x^2) z A/m: -1 uA/m at (1,0,0), +1 uA/m at (0,1,0); (d) all four hold;"
      " (e) B1 ruled out by Faraday, B2 by div B = 0 (no magnetic charge)")

# =====================================================================================
head("16.12 Four conditions at a tilted interface (hard, SP18 Exam 2 #1(vi) style)")
n12 = np.array([2.0, -1.0, 2.0]) / 3
e1, e2 = 2.0, 5.0
rhos = 3000 * eps0
Js12 = np.array([1.0, 4.0, 1.0])
E2v, H2v = np.array([4e3, 1e3, 1e3]), np.array([3.0, 1.0, 2.0])
print(f"   n-hat = {np.array2string(n12, precision=6)}; n.Js = {n12 @ Js12:.2e} (tangential); P = origin on the plane: 2(0)-0+2(0) = 0")
E2n = n12 @ E2v
H2n = n12 @ H2v
E2t = E2v - E2n * n12
H2t = H2v - H2n * n12
check("E2n [V/m]", E2n, 3e3)
checkv("E2 normal part [V/m]", E2n * n12, [2e3, -1e3, 2e3])
checkv("E2 tangential part [V/m]", E2t, [2e3, 2e3, -1e3])
check("H2n [A/m]", H2n, 3.0)
checkv("H2 normal part [A/m]", H2n * n12, [2, -1, 2])
checkv("H2 tangential part [A/m]", H2t, [1, 2, 0])
# (b)
E1n = (e2 * eps0 * E2n + rhos) / (e1 * eps0)
check("E1n from n.(D1 - D2) = rho_s [V/m]", E1n, 9e3)
E1v = E1n * n12 + E2t
checkv("E1 [V/m]", E1v, [8e3, -1e3, 5e3])
D1v, D2v = e1 * eps0 * E1v, e2 * eps0 * E2v
check("n.(D1 - D2) = rho_s [C/m^2]", n12 @ (D1v - D2v), rhos)
checkv("n x (E1 - E2) = 0", np.cross(n12, E1v - E2v), np.zeros(3), ab=1e-9)
print(f"      D1 = {np.array2string(D1v*1e9, precision=3)} nC/m^2 (= eps0 (16, -2, 10) kV/m), D2 = {np.array2string(D2v*1e9, precision=3)} nC/m^2 (= eps0 (20, 5, 5) kV/m)")
print(f"      |E1| = {np.linalg.norm(E1v):.2f} V/m;  rho_s = 3000 eps0 = {rhos*1e9:.3f} nC/m^2")
# (c)
jump = np.cross(Js12, n12)
print(f"   arithmetic: (1,4,1) x (2,-1,2) = {np.cross(Js12, [2,-1,2])}; n.H1 terms (12 - 1 - 2)/3; n.E2 = (8 - 1 + 2)/3, n.H2 = (6 - 1 + 4)/3")
print(f"   9 n-hat = {np.array2string(9*n12*3/3, precision=4)} kV/m (E1 normal part)")
checkv("J_s x n [A/m]", jump, [3, 0, -3])
H1v = H2n * n12 + H2t + jump
checkv("H1 [A/m]", H1v, [6, 1, -1])
checkv("n x (H1 - H2) = J_s", np.cross(n12, H1v - H2v), Js12)
print(f"      n x (H1 - H2) before dividing by 3: {np.cross([2,-1,2], H1v - H2v)};  n.H1 = {n12 @ H1v:.6f} A/m")
check("n.(B1 - B2) = 0 [T]", n12 @ (mu0 * H1v - mu0 * H2v), 0.0, ab=1e-18)
print(f"      B1 = mu0 H1 = {np.array2string(mu0*H1v*1e6, precision=4)} uT; B2 = {np.array2string(mu0*H2v*1e6, precision=4)} uT; B_n = 3 mu0 = {3*mu0*1e6:.4f} uT both sides")
# (d) bound and total surface charge
P1, P2 = (e1 - 1) * eps0 * E1v, (e2 - 1) * eps0 * E2v
rho_sb = n12 @ P2 - n12 @ P1
check("bound surface charge n.P2 - n.P1 [C/m^2] = 3000 eps0", rho_sb, 3000 * eps0)
print(f"      n.P2 = 4 eps0 (3 kV/m) = {n12@P2/eps0:.0f} eps0, n.P1 = eps0 (9 kV/m) = {n12@P1/eps0:.0f} eps0")
tot = eps0 * (n12 @ (E1v - E2v))
check("total eps0 n.(E1 - E2) = rho_s + rho_sb [C/m^2]", tot, rhos + rho_sb)
print(f"      rho_sb = {rho_sb*1e9:.3f} nC/m^2, total = 6000 eps0 = {tot*1e9:.3f} nC/m^2")
# (e) shrinking-rectangle argument: flux of finite dD/dt and dB/dt through a w x l rectangle -> 0
for wid in [1e-3, 1e-6]:
    print(f"   (e) rectangle l = 1 m, w = {wid:.0e} m: flux of a finite dD/dt (say 1 A/m^2) = {wid:.0e} A -> 0; J_s through it stays |J_s| l")
print(f"   ANSWER 16.12: n = (2,-1,2)/3; E2 = (2,-1,2) + (2,2,-1) kV/m, H2 = (2,-1,2) + (1,2,0) A/m; E1 = (8,-1,5) kV/m,"
      f" D1 = eps0(16,-2,10) kV/m; H1 = (6,1,-1) A/m, B1 = ({mu0*6e6:.2f}, {mu0*1e6:.3f}, {-mu0*1e6:.3f}) uT;"
      f" rho_sb = 3000 eps0 = {rho_sb*1e9:.1f} nC/m^2, total {tot*1e9:.1f} nC/m^2")

# =====================================================================================
print("=" * 96)
print(f"checks run: {NCHK};  failures: {len(FAILS)}")
for f in FAILS:
    print("   FAIL:", f)
