#!/usr/bin/env python3
"""R17.py - independent re-solution of practice page 17 (magnetization, Maxwell in matter).

Every number is recomputed from the problem statement, by a brute-force route where one exists
(discretized loops and Biot-Savart sums, finite-difference div/curl, ring superposition of line
charges/currents, sheet superposition, root finding), and compared with the value the page states.
Directions are always computed with np.cross.  Lines tagged PRE-FIX record a value the page stated
before this review, which was wrong and has been corrected (they are expected to FAIL and are not
counted).
"""
import warnings
import numpy as np
from scipy import integrate, optimize

warnings.filterwarnings("ignore", category=integrate.IntegrationWarning)
mu0 = 4e-7 * np.pi
eps0 = 8.8541878128e-12
X = np.array([1.0, 0, 0]); Y = np.array([0, 1.0, 0]); Z = np.array([0, 0, 1.0])
NFAIL = 0


def chk(name, got, stated, rtol=5e-3, atol=0.0):
    global NFAIL
    g = np.atleast_1d(np.asarray(got, float)); s = np.atleast_1d(np.asarray(stated, float))
    ok = g.shape == s.shape and np.allclose(g, s, rtol=rtol, atol=atol)
    NFAIL += (not ok)
    print(f"{'PASS' if ok else 'FAIL'}  {name}: computed {np.array2string(g, precision=5)}  page {np.array2string(s, precision=5)}")


def prefix(name, got, stated, rtol=5e-3, atol=0.0):
    g = np.atleast_1d(np.asarray(got, float)); s = np.atleast_1d(np.asarray(stated, float))
    ok = g.shape == s.shape and np.allclose(g, s, rtol=rtol, atol=atol)
    print(f"{'PASS' if ok else 'FAIL'}  PRE-FIX (now corrected) {name}: computed {np.array2string(g, precision=5)}  old page {np.array2string(s, precision=5)}")


def rot(v, axis, ang):  # Rodrigues rotation of v about axis by ang (right-hand rule)
    k = axis / np.linalg.norm(axis)
    return v * np.cos(ang) + np.cross(k, v) * np.sin(ang) + k * np.dot(k, v) * (1 - np.cos(ang))


def H_sheets(z, sheets):  # superposition of infinite sheets on planes z = z0: H = 1/2 Js x n (n toward field point)
    H = np.zeros(3)
    for z0, Js in sheets:
        H += 0.5 * np.cross(Js, Z if z > z0 else -Z)
    return H


# ---------------------------------------------------------------- 17.1
print("=== 17.1 moment and torque on a loop ===")
I1 = 2.0; B1v = np.array([0.3, 0, 0.4])
V = np.array([[0, 0, 0], [0.04, 0, 0], [0.04, 0.05, 0], [0, 0.05, 0], [0, 0, 0]])
pts, dls = [], []
for k in range(4):
    n = 4000; t = (np.arange(n) + 0.5) / n
    pts.append(V[k] + np.outer(t, V[k + 1] - V[k])); dls.append(np.tile((V[k + 1] - V[k]) / n, (n, 1)))
pts = np.vstack(pts); dls = np.vstack(dls)
m1 = 0.5 * I1 * np.cross(pts, dls).sum(axis=0)             # m = (I/2) oint r x dl
chk("17.1(a) m [A m^2]", m1, [0, 0, 4.0e-3], atol=1e-12)
dF = I1 * np.cross(dls, B1v)
chk("17.1(b) net force [N]", dF.sum(axis=0), [0, 0, 0], atol=1e-12)
ctr = np.array([0.02, 0.025, 0])
chk("17.1(b) torque, brute-force sum r x dF [N m]", np.cross(pts - ctr, dF).sum(axis=0), [0, 1.2e-3, 0], atol=1e-9)
chk("17.1(b) torque m x B [N m]", np.cross(m1, B1v), [0, 1.2e-3, 0], atol=1e-12)
chk("17.1(b) sin(angle m,B)", np.linalg.norm(np.cross(Z, B1v)) / np.linalg.norm(B1v), 0.6)
chk("17.1(c) force on x=4cm edge [N]", I1 * np.cross(0.05 * Y, B1v), [0.04, 0, -0.03], atol=1e-12)
chk("17.1(c) force on x=0 edge [N]", I1 * np.cross(-0.05 * Y, B1v), [-0.04, 0, 0.03], atol=1e-12)
chk("17.1(c) forces on y=0 and y=5cm edges [N]", np.r_[I1 * np.cross(0.04 * X, B1v), I1 * np.cross(-0.04 * X, B1v)],
    [0, -0.032, 0, 0, 0.032, 0], atol=1e-12)
T1 = np.cross(m1, B1v)
print("      x=4cm edge: z after a small turn about T =", rot(np.array([0.02, 0, 0]), T1, 1e-3)[2], "(<0: sinks)")
print("      x=0  edge: z after a small turn about T =", rot(np.array([-0.02, 0, 0]), T1, 1e-3)[2], "(>0: rises)")
print("      m tilts toward", np.round((rot(m1, T1, 1e-3) - m1) / 1e-3 / np.linalg.norm(m1), 6))
al = np.linspace(-np.pi, np.pi, 720001)
U = -np.linalg.norm(m1) * (np.sin(al) * B1v[0] + np.cos(al) * B1v[2])   # m(al) = rot(z, y, al)
amin = al[np.argmin(U)]
chk("17.1(c) stable tilt about +y [deg]", np.degrees(amin), 36.9, rtol=2e-3)
chk("17.1(c) stable normal", rot(Z, Y, amin), [0.6, 0, 0.8], atol=1e-4)
print("      x=4cm edge z at the stable tilt:", rot(np.array([0.02, 0, 0]), Y, amin)[2], "(<0: lowered)")
chk("17.1 check: torque of the vertical forces [N m]", np.cross(0.02 * X, -0.03 * Z) + np.cross(-0.02 * X, 0.03 * Z),
    [0, 1.2e-3, 0], atol=1e-12)
q = -1.602e-19; me = 0.5 * q * np.cross(1e-10 * X, 1e6 * Y)  # electron at +x moving +y: CCW seen from +z
chk("17.1(d) electron moment direction", me / np.linalg.norm(me), [0, 0, -1], atol=1e-12)
tq = np.cross(-Z, B1v)
chk("17.1(d) torque per unit moment [T]", tq, [0, -0.3, 0], atol=1e-12)
print("      electron moment tilts toward", np.round((rot(-Z, tq, 1e-3) + Z) / 1e-3, 6))
chk("17.1(d) angle between -z and B [deg]", np.degrees(np.arccos(-B1v[2] / np.linalg.norm(B1v))), 143.1, rtol=1e-3)

# ---------------------------------------------------------------- 17.2
print("\n=== 17.2 four rods ===")
H2 = 400.0; Mr = {'P': -3.76e-3, 'Q': 8.4e-3, 'R': 0.32, 'S': 2.0e5}
chi = {k: v / H2 for k, v in Mr.items()}
chk("17.2 chi_m P,Q,R,S", [chi[k] for k in 'PQRS'], [-9.4e-6, 2.1e-5, 8.0e-4, 500])
chk("17.2 mu_r P,Q,R,S", [1 + chi[k] for k in 'PQRS'], [0.9999906, 1.000021, 1.0008, 501], rtol=1e-7)
cls = lambda c: 'dia' if c < 0 else ('ferro' if c > 1 else 'para')
print("      classes:", {k: cls(chi[k]) for k in 'PQRS'}, "-> option (a)")
chk("17.2 chi_S / chi_R", chi['S'] / chi['R'], 6.25e5)
chk("17.2 B empty coil [mT]", mu0 * H2 * 1e3, 0.503)
chk("17.2 B inside S [T]", mu0 * (H2 + Mr['S']), 0.252)
chk("17.2 B_S / B_empty", (H2 + Mr['S']) / H2, 501)
chk("17.2 B_P - B_empty [nT]", mu0 * Mr['P'] * 1e9, -4.7, rtol=0.01)
chk("17.2 1/mu0 (page: ~8e5)", 1 / mu0, 8e5, rtol=0.01)

# ---------------------------------------------------------------- 17.3
print("\n=== 17.3 ferrite between sheets ===")
sh3 = [(0.0, 0.5 * X), (0.04, -0.5 * X)]
H3 = H_sheets(0.02, sh3)
chk("17.3 H between sheets [A/m]", H3, [0, -0.5, 0], atol=1e-12)
chk("17.3 H outside", np.r_[H_sheets(-0.01, sh3), H_sheets(0.05, sh3)], np.zeros(6), atol=1e-12)
chk("17.3 student's B [uT]", mu0 * H3[1] * 1e6, -0.628)
chk("17.3 student's H_slab [A/m]", mu0 * H3[1] / (500 * mu0), -1.0e-3)
chk("17.3 student's M [A/m]", 499 * mu0 * H3[1] / (500 * mu0), -0.499)
B3 = 500 * mu0 * H3; M3 = B3 / mu0 - H3
chk("17.3 B slab [T]", B3, [0, -3.14e-4, 0], atol=1e-7)
chk("17.3 M slab [A/m]", M3, [0, -249.5, 0], atol=1e-9)
Jt3, Jb3 = np.cross(M3, Z), np.cross(M3, -Z)
chk("17.3 J_sM top z=3cm [A/m]", Jt3, [-249.5, 0, 0], atol=1e-9)
chk("17.3 J_sM bottom z=1cm [A/m]", Jb3, [249.5, 0, 0], atol=1e-9)
all3 = sh3 + [(0.03, Jt3), (0.01, Jb3)]
chk("17.3 vacuum B from free+bound, in slab [T]", mu0 * H_sheets(0.02, all3), [0, -3.14e-4, 0], atol=1e-7)
chk("17.3 vacuum B in gaps z=0.5, 3.5 cm [uT]", np.r_[mu0 * H_sheets(0.005, all3), mu0 * H_sheets(0.035, all3)] * 1e6,
    [0, -0.628, 0, 0, -0.628, 0], atol=1e-3)
chk("17.3 vacuum B outside", mu0 * H_sheets(0.05, all3), np.zeros(3), atol=1e-15)

# ---------------------------------------------------------------- 17.4
print("\n=== 17.4 hysteresis ===")
Br, Hc = 0.4 * np.pi, 8.0e5
chk("17.4 B_r [T]", Br, 1.26)
chk("17.4(a) M at remanence [A/m] (True)", Br / mu0 - 0, 1.0e6)
chk("17.4(b) M at coercive point [A/m] (nonzero -> False)", 0 / mu0 - (-Hc), 8.0e5)
chk("17.4(c) dB for dH = 1e5 A/m at saturation [T] (True)", mu0 * 1e5, 0.126)

# ---------------------------------------------------------------- 17.5
print("\n=== 17.5 nickel rod ===")
M5 = 9.14e28 * 0.60 * 9.27e-24
chk("17.5(a) M [A/m]", M5, 5.08e5)
ph = 0.7; rh = np.array([np.cos(ph), np.sin(ph), 0]); fh = np.array([-np.sin(ph), np.cos(ph), 0])
chk("17.5(b) J_sM side = M z x r", np.cross(M5 * Z, rh), M5 * fh, rtol=1e-12)
chk("17.5(b) J_sM ends", np.r_[np.cross(Z, Z), np.cross(Z, -Z)], np.zeros(6), atol=1e-15)
a5, L5 = 5e-3, 4.0
Bc5, _ = integrate.quad(lambda zp: mu0 * M5 * a5**2 / (2 * (a5**2 + zp**2)**1.5), -L5 / 2, L5 / 2, points=[0], limit=400)
chk("17.5(c) B at centre of a 4 m rod, loop sum [T]", Bc5, 0.639)
chk("17.5(c) H = B/mu0 - M [A/m]", Bc5 / mu0 - M5, 0.0, atol=1e-4 * M5)
chk("17.5(d) I for n = 1000/m [A]", M5 / 1000, 508)

# ---------------------------------------------------------------- 17.6
print("\n=== 17.6 graded slab ===")
d6, M06 = 0.02, 3.0e4
xs = np.linspace(-0.01, 0.01, 5); zs = np.linspace(0, d6, 2001)
XX, YY, ZZ = np.meshgrid(xs, xs, zs, indexing='ij')
Mx, My, Mz = M06 * (ZZ / d6)**2, 0 * ZZ, 0 * ZZ
dx, dz = xs[1] - xs[0], zs[1] - zs[0]
cx = np.gradient(Mz, dx, axis=1) - np.gradient(My, dz, axis=2)
cy = np.gradient(Mx, dz, axis=2) - np.gradient(Mz, dx, axis=0)
cz = np.gradient(My, dx, axis=0) - np.gradient(Mx, dx, axis=1)
i1 = np.argmin(abs(zs - 0.01))
chk("17.6(a) curl M at z=1cm (FD) [A/m^2]", [cx[2, 2, i1], cy[2, 2, i1], cz[2, 2, i1]], [0, 1.5e6, 0], atol=1.0)
chk("17.6(a) curl M at z=d (FD, one-sided)", cy[2, 2, -1], 3.0e6, rtol=2e-3)
chk("17.6(a) coefficient 2 M0/d^2 [A/m^3]", 2 * M06 / d6**2, 1.5e8)
chk("17.6(a) J_sM top (n=+z) [A/m]", np.cross(M06 * X, Z), [0, -3.0e4, 0], atol=1e-9)
chk("17.6(a) J_sM bottom (M=0)", np.cross(0 * X, -Z), [0, 0, 0], atol=1e-12)
Iv6, _ = integrate.quad(lambda z: 2 * M06 * z / d6**2, 0, d6)
chk("17.6(b) volume current per m along x [A]", Iv6, 3.0e4)
chk("17.6(b) net (volume + top face)", Iv6 - M06, 0.0, atol=1e-6)


def Bx6(z):  # superposition of the sheets J_M dz' (y) and the top face sheet, vacuum formula
    f = lambda zp: 0.5 * mu0 * (2 * M06 * zp / d6**2) * np.sign(z - zp)
    v, _ = integrate.quad(f, 0, d6, points=[z] if 0 < z < d6 else None, limit=200)
    return v + 0.5 * mu0 * np.cross(-M06 * Y, Z if z > d6 else -Z)[0]


chk("17.6(c,d) B_x at z=1cm [mT]", Bx6(0.01) * 1e3, 9.42)
chk("17.6(c) B_x just below top [mT]", Bx6(d6 - 1e-9) * 1e3, 37.7)
chk("17.6(c) B_x just above top, below bottom [T]", [Bx6(d6 + 1e-9), Bx6(-1e-3)], [0, 0], atol=1e-9)
zz = np.linspace(0.001, 0.019, 7)
chk("17.6(c) B = mu0 M inside (so H = 0)", [Bx6(z) for z in zz], mu0 * M06 * (zz / d6)**2, rtol=1e-6)
chk("17.6(c) z x (B_above - B_below)/mu0 at top [A/m]", np.cross(Z, (0 - mu0 * M06) * X) / mu0, [0, -3.0e4, 0], atol=1e-6)
lo, _ = integrate.quad(lambda zp: 2 * M06 * zp / d6**2, 0, d6 / 2)
hi, _ = integrate.quad(lambda zp: 2 * M06 * zp / d6**2, d6 / 2, d6)
chk("17.6(d) current below / above z=d/2 (units of M0)", [lo / M06, hi / M06], [0.25, 0.75])
chk("17.6(d) 1/4 - 3/4 + 1 (units of mu0 M0/2)", lo / M06 - hi / M06 + 1, 0.5)

# ---------------------------------------------------------------- 17.7
print("\n=== 17.7 steel wire ===")
a7, I7, mur7 = 1e-3, 5.0, 200.0; chi7 = mur7 - 1
Hin = lambda r: I7 * r / (2 * np.pi * a7**2); Hout = lambda r: I7 / (2 * np.pi * r)
chk("17.7(a) H at r=a [A/m]", Hout(a7), 795.8, rtol=1e-4)
chk("17.7(a) B just inside [T]", mur7 * mu0 * Hin(a7), 0.200)
chk("17.7(a) B just outside [mT]", mu0 * Hout(a7) * 1e3, 1.00)
chk("17.7(b) M(a) [A/m]", chi7 * Hin(a7), 1.58e5)


def M7(x, y):
    r = np.hypot(x, y); Mp = chi7 * Hin(r); return np.array([-Mp * y / r, Mp * x / r])


h = 1e-7; x0, y0 = 0.3e-3, 0.4e-3
JM7 = (M7(x0 + h, y0)[1] - M7(x0 - h, y0)[1]) / (2 * h) - (M7(x0, y0 + h)[0] - M7(x0, y0 - h)[0]) / (2 * h)
chk("17.7(b) J_M (FD curl) [A/m^2]", JM7, 3.17e8)
chk("17.7(b) J_f [A/m^2]", I7 / (np.pi * a7**2), 1.59e6)
chk("17.7(b) volume magnetization current [A]", JM7 * np.pi * a7**2, 995)
ph = 1.1; rh = np.array([np.cos(ph), np.sin(ph), 0]); fh = np.array([-np.sin(ph), np.cos(ph), 0])
Js7 = np.cross(chi7 * Hin(a7) * fh, rh)
chk("17.7(b) J_sM = M x r [A/m]", Js7, [0, 0, -1.58e5], atol=600)
chk("17.7(b) surface magnetization current [A]", Js7[2] * 2 * np.pi * a7, -995)
r = 0.5 * a7
chk("17.7(c) vacuum Ampere inside (r=a/2) vs mu H", mu0 * (I7 * (r / a7)**2 + JM7 * np.pi * r**2) / (2 * np.pi * r),
    mur7 * mu0 * Hin(r), rtol=1e-6)
r = 2 * a7
chk("17.7(c) vacuum Ampere outside (r=2a) vs copper", mu0 * (I7 + JM7 * np.pi * a7**2 + Js7[2] * 2 * np.pi * a7) / (2 * np.pi * r),
    mu0 * I7 / (2 * np.pi * r), rtol=1e-6)
W7, _ = integrate.quad(lambda r: 0.5 * mur7 * mu0 * Hin(r)**2 * 2 * np.pi * r, 0, a7)
chk("17.7(d) W' [J/m]", W7, 1.25e-4)
chk("17.7(d) L_int = 2W'/I^2 [uH/m]", 2 * W7 / I7**2 * 1e6, 10.0)
chk("17.7(d) copper mu0/8pi [uH/m]", mu0 / (8 * np.pi) * 1e6, 0.05)
chk("17.7 check: B_out - B_in at r=a [T]", mu0 * Hout(a7) - mur7 * mu0 * Hin(a7), -0.199)
chk("17.7 check: r x (B_out - B_in)/mu0 [A/m]", np.cross(rh, (mu0 * Hout(a7) - mur7 * mu0 * Hin(a7)) * fh) / mu0,
    [0, 0, -1.58e5], atol=600)

# ---------------------------------------------------------------- 17.8
print("\n=== 17.8 iron surface ===")
B8 = np.array([0.8, 0.01, -0.6]); n8 = Y   # medium 2 iron (y<0), medium 1 air (y>0)
H8i = B8 / (2000 * mu0)
chk("17.8(a) H iron [A/m]", H8i, [318.3, 3.98, -238.7], rtol=2e-3)
H8a = H8i - np.dot(H8i, n8) * n8 + (np.dot(B8, n8) / mu0) * n8
B8a = mu0 * H8a
chk("17.8(a) H air [A/m]", H8a, [318.3, 7958, -238.7], rtol=2e-4)
chk("17.8(a) B air [mT]", B8a * 1e3, [0.4, 10, -0.3], rtol=1e-6)
chk("17.8 BC: n x (H1-H2), n.(B1-B2)", np.r_[np.cross(n8, H8a - H8i), np.dot(n8, B8a - B8)], np.zeros(4), atol=1e-9)


def ang(Bv):
    Bn = abs(np.dot(Bv, n8)); Bt = np.linalg.norm(Bv - np.dot(Bv, n8) * n8)
    return np.degrees(np.arctan2(Bt, Bn)), Bt / Bn


(th2, t2), (th1, t1) = ang(B8), ang(B8a)
chk("17.8(b) angle from normal: iron, air [deg]", [th2, th1], [89.43, 2.86], rtol=1e-3)
chk("17.8(b) tan1/tan2 = mu1/mu2", t1 / t2, 1 / 2000, rtol=1e-9)
M8 = B8 / mu0 - H8i
chk("17.8(c) M iron [A/m]", M8, [6.363e5, 7.95e3, -4.772e5], rtol=1e-3)
Js8 = np.cross(n8, 0 - M8)
chk("17.8(c) J_sM = n x (M1 - M2) [A/m]", Js8, [4.772e5, 0, 6.363e5], rtol=1e-3, atol=1e-6)
chk("17.8(c) same as M2 x n_out (+y)", np.cross(M8, Y), Js8, rtol=1e-12)
chk("17.8(c) |J_sM| [A/m]", np.linalg.norm(Js8), 7.95e5, rtol=1e-3)
chk("17.8(c) B1 - B2 [T]", B8a - B8, [-0.7996, 0, 0.5997], rtol=1e-4, atol=1e-12)
chk("17.8(c) n x (B1-B2)/mu0 = J_sM", np.cross(n8, B8a - B8) / mu0, Js8, rtol=1e-9)
chk("17.8(c) H_y iron, air [A/m]", [H8i[1], H8a[1]], [3.98, 7958], rtol=2e-3)

# ---------------------------------------------------------------- 17.9
print("\n=== 17.9 electret and magnet twins ===")
a9, P0, M09, dP0 = 0.01, 2.0e-6, 5.0e4, 0.4e-6
ph = 0.3; x0, y0 = a9 / 2 * np.cos(ph), a9 / 2 * np.sin(ph)
rh = np.array([np.cos(ph), np.sin(ph), 0]); fh = np.array([-np.sin(ph), np.cos(ph), 0])
Pv = lambda x, y: P0 * (np.hypot(x, y) / a9)**2 * np.array([x, y]) / np.hypot(x, y)
h = 1e-8
divP = (Pv(x0 + h, y0)[0] - Pv(x0 - h, y0)[0]) / (2 * h) + (Pv(x0, y0 + h)[1] - Pv(x0, y0 - h)[1]) / (2 * h)
chk("17.9(a) rho_b at a/2 (FD) [C/m^3]", -divP, -3.0e-4)
chk("17.9(a) rho_sb = P.r at a [uC/m^2]", np.dot(P0 * rh, rh) * 1e6, 2.0)
Qv, _ = integrate.quad(lambda r: -3 * P0 * r / a9**2 * 2 * np.pi * r, 0, a9)
chk("17.9(a) bound charge per m: volume, surface [nC/m]", [Qv * 1e9, P0 * 2 * np.pi * a9 * 1e9], [-126, 126])
chk("17.9(a) total", Qv + P0 * 2 * np.pi * a9, 0, atol=1e-20)
Mv = lambda x, y: M09 * (np.hypot(x, y) / a9)**2 * np.array([-y, x]) / np.hypot(x, y)
curlM = (Mv(x0 + h, y0)[1] - Mv(x0 - h, y0)[1]) / (2 * h) - (Mv(x0, y0 + h)[0] - Mv(x0, y0 - h)[0]) / (2 * h)
chk("17.9(b) J_M at a/2 (FD curl) [A/m^2]", curlM, 7.5e6)
Js9 = np.cross(M09 * fh, rh)
chk("17.9(b) J_sM = M x r [A/m]", Js9, [0, 0, -5.0e4], atol=1e-9)
Iv9, _ = integrate.quad(lambda r: 3 * M09 * r / a9**2 * 2 * np.pi * r, 0, a9)
chk("17.9(b) current: volume, surface [kA]", [Iv9 / 1e3, Js9[2] * 2 * np.pi * a9 / 1e3], [3.14, -3.14])


def Kring(s, r):  # radial field at (r,0) of a ring of 2-D line sources (total strength 1) of radius s, kernel 1/(2 pi rho)
    f = lambda p: (r - s * np.cos(p)) / ((r - s * np.cos(p))**2 + (s * np.sin(p))**2)
    v, _ = integrate.quad(f, -np.pi, np.pi, points=[0.0], limit=400)
    return v / (2 * np.pi) / (2 * np.pi)


def ring_sum(vol_density, surf_total, r):  # sum over rings: volume density (per m^2) and a surface ring at s = a9
    v, _ = integrate.quad(lambda s: vol_density(s) * 2 * np.pi * s * Kring(s, r), 0, a9,
                          points=[r] if r < a9 else None, limit=200)
    return v + surf_total * Kring(a9, r)


Er = lambda r: ring_sum(lambda s: -3 * P0 * s / a9**2, P0 * 2 * np.pi * a9, r) / eps0      # Coulomb superposition
Bp = lambda r: mu0 * ring_sum(lambda s: 3 * M09 * s / a9**2, -M09 * 2 * np.pi * a9, r)    # Biot-Savart of z-currents
Ea, Ee, Eo = Er(a9 / 2), Er(0.9999 * a9), Er(2 * a9)
chk("17.9(c) E_r at a/2, just inside a [V/m] (superposition)", [Ea, Ee], [-5.65e4, -2.26e5])
chk("17.9(c) E outside (r=2a)", Eo, 0.0, atol=1e-6 * abs(Ee))
chk("17.9(c) D = eps0 E + P at a/2", eps0 * Ea + P0 * 0.25, 0.0, atol=1e-4 * P0)
Ba, Be, Bo = Bp(a9 / 2), Bp(0.9999 * a9), Bp(2 * a9)
chk("17.9(c) B_phi at a/2, just inside a [mT] (superposition)", [Ba * 1e3, Be * 1e3], [15.7, 62.8])
chk("17.9(c) B outside (r=2a)", Bo, 0.0, atol=1e-6 * abs(Be))
chk("17.9(c) H = B/mu0 - M at a/2", Ba / mu0 - M09 * 0.25, 0.0, atol=1e-4 * M09)
print("      (d) E.P sign:", np.sign(Ea * P0), " B.M sign:", np.sign(Ba * M09), "(-1: against, +1: along)")
chk("17.9(e) dP/dt at a/2 [uA/m^2]", dP0 * 0.25 * 1e6, 0.1)
rho = lambda r, t: -3 * (P0 + dP0 * t) * r / a9**2
Pr = lambda r, t: (P0 + dP0 * t) * (r / a9)**2
r0, dt, dr = a9 / 2, 1e-3, 1e-7
dPdt = lambda r: (Pr(r, dt) - Pr(r, -dt)) / (2 * dt)
res = (rho(r0, dt) - rho(r0, -dt)) / (2 * dt) + ((r0 + dr) * dPdt(r0 + dr) - (r0 - dr) * dPdt(r0 - dr)) / (2 * dr) / r0
chk("17.9(e) continuity residual [C/m^3/s]", res, 0.0, atol=1e-12)
chk("17.9(e) eps0 dE/dt at a/2 (from superposition E, linear in P0) [uA/m^2]", eps0 * Ea / P0 * dP0 * 1e6, -0.1)
chk("17.9(e) dP/dt + eps0 dE/dt at a/2", dP0 * 0.25 + eps0 * Ea / P0 * dP0, 0.0, atol=1e-12)

# ---------------------------------------------------------------- 17.10
print("\n=== 17.10 three sheets and two slabs ===")
sh = [(0.0, 4 * Y), (0.02, 3 * X - 4 * Y), (0.04, -3 * X)]
chk("17.10 sum of free sheets", sum(s[1] for s in sh), np.zeros(3), atol=1e-15)
Hr = [H_sheets(z, sh) for z in (-0.01, 0.01, 0.03, 0.05)]
chk("17.10(a) H in z<0, 0-2, 2-4, z>4 cm [A/m]", np.r_[tuple(Hr)], [0, 0, 0, 4, 0, 0, 0, -3, 0, 0, 0, 0], atol=1e-12)
Hs = [np.zeros(3)]
for z0, Js in sh:                      # independent route: step up across each sheet, H_above = H_below + Js x z
    Hs.append(Hs[-1] + np.cross(Js, Z))
chk("17.10(a) same H by stepping the BC up from H=0", np.r_[tuple(Hs[1:])], [4, 0, 0, 0, -3, 0, 0, 0, 0], atol=1e-12)
Bl, Bu = 25 * mu0 * Hr[1], 10 * mu0 * Hr[2]
Ml, Mu = Bl / mu0 - Hr[1], Bu / mu0 - Hr[2]
chk("17.10(b) B lower [T]", Bl, [1.26e-4, 0, 0], atol=1e-7)
chk("17.10(b) B upper [T]", Bu, [0, -3.77e-5, 0], atol=1e-8)
chk("17.10(b) M lower, upper [A/m]", np.r_[Ml, Mu], [96, 0, 0, 0, -27, 0], atol=1e-9)
chk("17.10(c) n x (H1-H2) at z=2cm = Js2", np.cross(Z, Hr[2] - Hr[1]), [3, -4, 0], atol=1e-12)
chk("17.10(c) n.(B1-B2)", np.dot(Z, Bu - Bl), 0.0, atol=1e-20)
chk("17.10(c) jump in tangential B, B1-B2 [T]", Bu - Bl, [-1.26e-4, -3.77e-5, 0], atol=1e-7)
chk("17.10(c) n x (B1-B2)/mu0 [A/m]", np.cross(Z, Bu - Bl) / mu0, [30, -100, 0], atol=1e-9)
chk("17.10(c) |Js2| [A/m]", np.linalg.norm(sh[1][1]), 5.0)
chk("17.10(c) |n x (B1-B2)/mu0| / |Js2|", np.linalg.norm(np.cross(Z, Bu - Bl) / mu0) / np.linalg.norm(sh[1][1]), 20.9)
prefix("17.10 answer line 'tangential B/mu0 jumps by 30x-100y A/m'", (Bu - Bl) / mu0, [30, -100, 0], atol=1e-9)
J0, J2, J4 = np.cross(Ml, -Z), np.cross(Ml, Z) + np.cross(Mu, -Z), np.cross(Mu, Z)
chk("17.10(d) J_sM z=0 [A/m]", J0, [0, 96, 0], atol=1e-9)
chk("17.10(d) J_sM z=2cm (two faces) [A/m]", J2, [27, -96, 0], atol=1e-9)
chk("17.10(d) J_sM z=2cm = n x (M1-M2)", np.cross(Z, Mu - Ml), [27, -96, 0], atol=1e-9)
chk("17.10(d) J_sM z=4cm [A/m]", J4, [-27, 0, 0], atol=1e-9)
chk("17.10(d) sum of J_sM", J0 + J2 + J4, np.zeros(3), atol=1e-9)
tot = [(0.0, sh[0][1] + J0), (0.02, sh[1][1] + J2), (0.04, sh[2][1] + J4)]
chk("17.10(d) total sheets [A/m]", np.r_[tot[0][1], tot[1][1], tot[2][1]], [0, 100, 0, 30, -100, 0, -30, 0, 0], atol=1e-9)
chk("17.10(d) vacuum B lower, upper from total sheets [T]", np.r_[mu0 * H_sheets(0.01, tot), mu0 * H_sheets(0.03, tot)],
    np.r_[Bl, Bu], rtol=1e-9, atol=1e-15)
chk("17.10(d) vacuum B outside", np.r_[mu0 * H_sheets(-0.01, tot), mu0 * H_sheets(0.05, tot)], np.zeros(6), atol=1e-15)
Mbi = -1.7e-4 * Hr[1]
chk("17.10(e) M bismuth [A/m]", Mbi, [-6.8e-4, 0, 0], atol=1e-12)
chk("17.10(e) J_sM on z=0 [A/m]", np.cross(Mbi, -Z), [0, -6.8e-4, 0], atol=1e-12)

# ---------------------------------------------------------------- 17.11
print("\n=== 17.11 gapped toroid ===")
mur, R, A, g, N, I = 4000.0, 0.05, 1e-4, 1e-3, 250, 0.2
li = 2 * np.pi * R - g
chk("17.11 iron path l_i [m]", li, 0.3132, rtol=2e-4)
Bt = optimize.brentq(lambda B: B / (mur * mu0) * li + B / mu0 * g - N * I, 0, 10)
Hg, Hi = Bt / mu0, Bt / (mur * mu0)
chk("17.11(b) B [T]", Bt, 5.83e-2)
chk("17.11(b) H_gap, H_iron [A/m]", [Hg, Hi], [4.64e4, 11.6])
chk("17.11(b) H_iron l_i, H_gap g [A]", [Hi * li, Hg * g], [3.6, 46.4], rtol=0.01)
chk("17.11(b) share of NI on the gap", Hg * g / (N * I), 0.93, rtol=0.01)
B0 = mur * mu0 * N * I / (2 * np.pi * R)
chk("17.11(b) B without gap [T], ratio", [B0, B0 / Bt], [0.800, 13.7])
Psi = Bt * A; L = N * Psi / I
chk("17.11(c) Psi [Wb], N Psi [Wb], L [mH]", [Psi, N * Psi, L * 1e3], [5.83e-6, 1.46e-3, 7.28])
chk("17.11(c) no gap: N Psi [Wb], L0 [mH]", [N * B0 * A, N * B0 * A / I * 1e3], [0.0200, 100])
W = 0.5 * Bt * Hi * A * li + 0.5 * Bt * Hg * A * g
chk("17.11(c) energy: 1/2 L I^2 and sum of 1/2 B H vol [J]", [0.5 * L * I**2, W], [1.46e-4, 1.46e-4])
chk("17.11(c) gap fraction of energy", 0.5 * Bt * Hg * A * g / W, 0.927, rtol=1e-3)
chk("17.11(c) L with mu_r = 8000 [mH]", N * A * mu0 * N / (g + li / 8000) * 1e3, 7.56)
M11 = Bt / mu0 - Hi
chk("17.11(d) M [A/m]", M11, 4.64e4)
chk("17.11(d) M = chi_m H_iron", 3999 * Hi, M11, rtol=1e-12)
chk("17.11(d) winding per metre of ring [A/m], ratio", [N * I / (2 * np.pi * R), M11 / (N * I / (2 * np.pi * R))], [159, 291])
chk("17.11(d) J_sM on a face with n=+y of a bar magnetized along x: circulates like a winding (x cross y)",
    np.cross(M11 * X, Y) / M11, np.cross(X, Y), atol=1e-12)
chk("17.11(d) vacuum Ampere: (B/mu0) 2 pi R [A]", Bt / mu0 * 2 * np.pi * R, 1.457e4, rtol=1e-3)
chk("17.11(d) NI + M l_i [A], M l_i [A]", [N * I + M11 * li, M11 * li], [1.457e4, 1.452e4], rtol=1e-3)
chk("17.11(d) J_sM on gap faces (M along n)", np.cross(M11 * X, X), np.zeros(3), atol=1e-12)
lam = lambda i: N * A * optimize.brentq(lambda B: B / (mur * mu0) * li + B / mu0 * g - N * i, 0, 10)
chk("17.11(e) emf = d(N Psi)/dI * dI/dt [V]", (lam(I + 1e-4) - lam(I - 1e-4)) / 2e-4 * 20, 0.146)

# ---------------------------------------------------------------- 17.12
print("\n=== 17.12 short bar magnet ===")
a12, l12, M012 = 0.01, 0.02, 9.0e5


def Bz_formula(z, l=l12, a=a12):
    return mu0 * M012 / 2 * ((l / 2 - z) / np.sqrt((l / 2 - z)**2 + a**2) + (l / 2 + z) / np.sqrt((l / 2 + z)**2 + a**2))


def B_bs(P, nphi=720, nz=1500):  # 3-D Biot-Savart over the side sheet J_sM = M x n on r = a
    p = (np.arange(nphi) + 0.5) * 2 * np.pi / nphi
    zp = -l12 / 2 + (np.arange(nz) + 0.5) * l12 / nz
    PH, ZP = np.meshgrid(p, zp, indexing='ij')
    nh = np.stack([np.cos(PH), np.sin(PH), 0 * PH], axis=-1)
    src = np.stack([a12 * np.cos(PH), a12 * np.sin(PH), ZP], axis=-1)
    K = np.cross(M012 * Z, nh)
    Rv = P - src; Rn = np.linalg.norm(Rv, axis=-1)[..., None]
    return (mu0 / (4 * np.pi) * np.cross(K, Rv) / Rn**3).sum(axis=(0, 1)) * a12 * (2 * np.pi / nphi) * (l12 / nz)


# (a) end faces: M x (+-z) = 0; side: M x r = M phi
chk("17.12(a) J_sM side, ends", np.r_[np.cross(M012 * Z, np.array([np.cos(.4), np.sin(.4), 0])), np.cross(Z, Z)],
    np.r_[M012 * np.array([-np.sin(.4), np.cos(.4), 0]), 0, 0, 0], rtol=1e-12, atol=1e-9)
Bc, Bf = B_bs(np.zeros(3)), B_bs(np.array([0, 0, l12 / 2]))
chk("17.12(b) B centre, end face: Biot-Savart sum [T]", [Bc[2], Bf[2]], [0.800, 0.506])
chk("17.12(b) B centre, end face: on-axis formula [T]", [Bz_formula(0), Bz_formula(l12 / 2)], [0.800, 0.506])
chk("17.12(b) mu0 M0 [T]", mu0 * M012, 1.131, rtol=1e-3)
chk("17.12(c) H centre [A/m]", Bc[2] / mu0 - M012, -2.64e5)
Bin, Bout = B_bs(np.array([0, 0, l12 / 2 - 1e-6])), B_bs(np.array([0, 0, l12 / 2 + 1e-6]))
chk("17.12(c) H just inside / just outside end face [A/m]", [Bin[2] / mu0 - M012, Bout[2] / mu0], [-4.98e5, 4.02e5])
chk("17.12(d) B_z continuous across end face [T]", [Bin[2], Bout[2]], [0.506, 0.506])
chk("17.12(d) jump H_out - H_in = M0 [A/m]", Bout[2] / mu0 - (Bin[2] / mu0 - M012), 9.0e5)
chk("17.12(e) long rod l=100a: H/M0 at centre", Bz_formula(0, l=100 * a12) / (mu0 * M012) - 1, -2e-4, rtol=0.01)
chk("17.12(e) long rod l=1000a: B end face / mu0 M0", Bz_formula(500 * a12, l=1000 * a12) / (mu0 * M012), 0.5, rtol=1e-3)
chk("17.12(e) thin disk l=0.01a: B/mu0M0, H/M0 at centre",
    [Bz_formula(0, l=0.01 * a12) / (mu0 * M012), Bz_formula(0, l=0.01 * a12) / (mu0 * M012) - 1], [0.005, -0.995], rtol=1e-3)

print(f"\nTOTAL FAIL (excluding PRE-FIX lines): {NFAIL}")
