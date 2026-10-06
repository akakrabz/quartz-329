#!/usr/bin/env python3
"""Verification of every number, sign and direction on
content-src/practice/17-magnetization-and-maxwell-in-matter.md  (Lecture 17 practice page).

Rules followed (SPEC section 1): numpy/scipy only.
  * every direction comes from an explicit np.cross (moments, torques, forces, sheet fields
    1/2 Js x n, magnetization surface currents M x n with n the OUTWARD normal of the body,
    interface currents n x (M1 - M2) with n from medium 2 into medium 1);
  * curls and divergences are centred finite differences of the Cartesian fields as written;
  * totals are quad integrals; fields of graded or cylindrical bound sources are checked by
    brute-force superposition (layers as current sheets; 2-D line charges / line currents with
    the angular integral done numerically; Biot-Savart summation over the side of a magnet);
  * the gapped toroid is solved with brentq from Ampere's law + continuity of B_n.
Output: L17.out (run: python3 L17.py > L17.out).
"""
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
import warnings
from scipy.integrate import IntegrationWarning
# ring_G's angular integrand is sharply peaked when rp ~ r; quad may warn about round-off there.
# The outer results are compared with the closed forms to 1e-5 below, so the warning is silenced.
warnings.filterwarnings('ignore', category=IntegrationWarning)

eps0 = 8.8541878128e-12
mu0 = 4e-7 * np.pi
e = 1.602176634e-19
me = 9.1093837e-31
XH, YH, ZH = np.eye(3)
NCHK = 0
FAILS = []


def fmt(v):
    v = np.atleast_1d(np.asarray(v, float)).ravel()
    return "(" + ", ".join(f"{x:.6g}" for x in v) + ")" if v.size > 1 else f"{v[0]:.6g}"


def check(label, got, want, rel=1e-6, ab=1e-12):
    global NCHK
    NCHK += 1
    ok = np.allclose(np.asarray(got, float), np.asarray(want, float), rtol=rel, atol=ab)
    print(f"   [{'ok' if ok else 'FAIL'}] {label}: {fmt(got)}  vs  {fmt(want)}")
    if not ok:
        FAILS.append(label)


def head(s):
    print("\n" + "=" * 96 + "\n" + s + "\n" + "=" * 96)


def curl(F, p, h=1e-7):
    p = np.asarray(p, float)
    Jm = np.zeros((3, 3))
    for j in range(3):
        dp = np.zeros(3); dp[j] = h
        Jm[:, j] = (F(p + dp) - F(p - dp)) / (2 * h)
    return np.array([Jm[2, 1] - Jm[1, 2], Jm[0, 2] - Jm[2, 0], Jm[1, 0] - Jm[0, 1]])


def div(F, p, h=1e-7):
    p = np.asarray(p, float)
    s = 0.0
    for j in range(3):
        dp = np.zeros(3); dp[j] = h
        s += (F(p + dp)[j] - F(p - dp)[j]) / (2 * h)
    return s


def sheets_H(zp, sheets):
    """H (or B/mu0) of infinite sheets [(z0, K)], 1/2 K x n with n from sheet to field point."""
    H = np.zeros(3)
    for z0, K in sheets:
        n = ZH if zp > z0 else -ZH
        H += 0.5 * np.cross(np.asarray(K, float), n)
    return H


def ring_G(r, rp):
    """int_0^2pi (r - rp cos f)/(r^2 + rp^2 - 2 r rp cos f) df, numerically (brute force)."""
    if rp == 0:
        return 2 * np.pi / r
    f = lambda t: (r - rp * np.cos(t)) / (r * r + rp * rp - 2 * r * rp * np.cos(t))
    return 2 * quad(f, 0, np.pi, points=[0.0], limit=400, epsabs=1e-13, epsrel=1e-11)[0]


# =============================================================================================
head("17.1  Moment and torque on a loop")
I1 = 2.0
C = np.array([[0, 0, 0], [0.04, 0, 0], [0.04, 0.05, 0], [0, 0.05, 0]], float)
m_poly = 0.5 * I1 * sum(np.cross(C[i], C[(i + 1) % 4]) for i in range(4))  # m = (I/2) sum r x dl
print("   current path (0,0)->(4,0)->(4,5)->(0,5) cm: counter-clockwise seen from +z")
check("m = I A z  [A m^2]", m_poly, [0, 0, 2 * 0.04 * 0.05])
B1 = np.array([0.3, 0, 0.4])
T1 = np.cross(m_poly, B1)
check("T = m x B  [N m]", T1, [0, 1.2e-3, 0])
sinth = np.linalg.norm(np.cross(ZH, B1)) / np.linalg.norm(B1)
check("sin(angle m,B) = 0.6, |T| = m B sin", [sinth, np.linalg.norm(m_poly) * 0.5 * sinth], [0.6, 1.2e-3])
F = []
ctr = C.mean(axis=0)
Tsum = np.zeros(3)
for i in range(4):
    dl = C[(i + 1) % 4] - C[i]
    Fi = I1 * np.cross(dl, B1)
    F.append(Fi)
    Tsum += np.cross(0.5 * (C[i] + C[(i + 1) % 4]) - ctr, Fi)
    print(f"   edge {C[i]*100} -> {C[(i+1)%4]*100} cm: F = {fmt(Fi)} N")
check("edge x = 4 cm (current +y): F = (0.04, 0, -0.03) N  -> sinks", F[1], [0.04, 0, -0.03])
check("edge x = 0 (current -y): F = (-0.04, 0, +0.03) N  -> rises", F[3], [-0.04, 0, 0.03])
check("net force = 0", sum(F), [0, 0, 0])
check("torque from edge forces about the centre", Tsum, T1)
# rotation produced by T (about +y) tilts m from +z towards +x (towards B)
dm = np.cross(T1 / np.linalg.norm(T1), m_poly / np.linalg.norm(m_poly))
print(f"   T_hat x m_hat = {fmt(dm)}  -> m tilts toward +x (toward B)")
ang_eq = np.degrees(np.arccos(B1[2] / np.linalg.norm(B1)))
check("stable orientation: normal along B = (0.6,0,0.8), tilt from z [deg]", ang_eq, 36.8699, rel=1e-5)
Ry = lambda th: np.array([[np.cos(th), 0, np.sin(th)], [0, 1, 0], [-np.sin(th), 0, np.cos(th)]])
R = Ry(np.radians(ang_eq))
check("rotating about +y by 36.87 deg takes z to B_hat", R @ ZH, B1 / np.linalg.norm(B1))
print(f"   ...and takes the x = 4 cm edge direction +x to {fmt(R @ XH)} (it is lowered)")
# electron circling counter-clockwise seen from +z: m = (q/2) r x v with q = -e
r_e, v_e = np.array([1.0, 0, 0]), np.array([0, 1.0, 0])
m_e = 0.5 * (-e) * np.cross(r_e, v_e)
print(f"   electron (ccw seen from +z): m direction = {fmt(m_e / np.linalg.norm(m_e))}  (-z)")
mh = m_e / np.linalg.norm(m_e)
Te = np.cross(mh, B1)
print(f"   torque per unit m on it: m_hat x B = {fmt(Te)} N m per A m^2 (along -y)")
ang0 = np.degrees(np.arccos(mh @ B1 / 0.5))
mh2 = mh + 1e-3 * np.cross(Te / np.linalg.norm(Te), mh)
ang1 = np.degrees(np.arccos(mh2 @ B1 / np.linalg.norm(mh2) / 0.5))
print(f"   angle(m_e, B) = {ang0:.2f} deg; after a small turn about T: {ang1:.3f} deg (decreases -> toward B)")
check("electron: angle(m,B) = 143.13 deg", ang0, 143.1301, rel=1e-5)
NCHK += 1
if not ang1 < ang0:
    FAILS.append("17.1 electron turns toward B")

# =============================================================================================
head("17.2  Four rods in a solenoid (multiple choice)")
H2 = 400.0
Ms = {"P": -3.76e-3, "Q": 8.4e-3, "R": 0.32, "S": 2.0e5}
chi = {k: v / H2 for k, v in Ms.items()}
for k in Ms:
    cls = "dia" if chi[k] < 0 else ("para" if chi[k] < 1 else "ferro")
    print(f"   {k}: M = {Ms[k]:.4g} A/m  chi_m = M/H = {chi[k]:.4g}  mu_r = {1+chi[k]:.8g}  -> {cls}")
check("chi_m P, Q, R, S", list(chi.values()), [-9.4e-6, 2.1e-5, 8.0e-4, 500])
check("mu_r P, Q, R, S", [1 + c for c in chi.values()], [0.9999906, 1.000021, 1.0008, 501])
BS = mu0 * (H2 + Ms["S"])
check("B in S = mu0(H+M) [T]", BS, 0.251830, rel=1e-5)
print(f"   B in S = {BS:.4f} T ;  empty solenoid mu0 H = {mu0*H2*1e3:.4f} mT = {mu0*H2*1e6:.1f} uT")
check("B in P - B empty = mu0 M_P [T]", mu0 * Ms["P"], -4.7250e-9, rel=1e-4)
print(f"   B_S/B_empty = {BS/(mu0*H2):.1f} ; wrong chi = M/(mu0 H) would be 1/mu0 = {1/mu0:.4g} times too big")
print(f"   ratio of chi_m(S) to the largest para value: {chi['S']/chi['R']:.3g} ; to Q: {chi['S']/chi['Q']:.3g}")

# =============================================================================================
head("17.3  Ferrite between two sheets (find the error)")
free3 = [(0.0, [0.5, 0, 0]), (0.04, [-0.5, 0, 0])]
for zp in (-0.01, 0.005, 0.02, 0.035, 0.05):
    print(f"   z = {zp*100:5.1f} cm: H(free sheets) = {fmt(sheets_H(zp, free3))} A/m")
check("H between the sheets", sheets_H(0.02, free3), [0, -0.5, 0])
check("H outside (z<0, z>4 cm)", [sheets_H(-0.01, free3), sheets_H(0.05, free3)], np.zeros((2, 3)))
mur3 = 500.0
print("   student's numbers:")
check("  B_air = mu0*0.5 [T] (0.628 uT)", mu0 * 0.5, 6.2832e-7, rel=1e-4)
check("  H_slab(student) = B_air/mu = 1.0e-3 A/m", mu0 * 0.5 / (mur3 * mu0), 1.0e-3)
check("  M(student) = 499 * 1e-3 = 0.499 A/m", (mur3 - 1) * 1e-3, 0.499)
Hs3 = sheets_H(0.02, free3)
Bs3 = mur3 * mu0 * Hs3
Ms3 = (mur3 - 1) * Hs3
check("correct B_slab = 500 mu0 (-0.5 y) [T]", Bs3, [0, -3.14159e-4, 0], rel=1e-5)
check("correct M_slab = 499 (-0.5 y) [A/m]", Ms3, [0, -249.5, 0])
top = np.cross(Ms3, ZH)       # face z = 3 cm, outward +z
bot = np.cross(Ms3, -ZH)      # face z = 1 cm, outward -z
check("J_sM on z = 3 cm face (M x z)", top, [-249.5, 0, 0])
check("J_sM on z = 1 cm face (M x -z)", bot, [249.5, 0, 0])
allc = free3 + [(0.01, bot), (0.03, top)]
check("vacuum check, free+bound: B in slab", mu0 * sheets_H(0.02, allc), Bs3)
check("vacuum check: B in gap z = 0.5 cm and 3.5 cm", [mu0 * sheets_H(0.005, allc), mu0 * sheets_H(0.035, allc)],
      [[0, -mu0 * 0.5, 0]] * 2)
check("vacuum check: B outside", [mu0 * sheets_H(-0.01, allc), mu0 * sheets_H(0.05, allc)], np.zeros((2, 3)))
print(f"   free + bound per side = {0.5+249.5} A/m ; B_slab/B_air = {Bs3[1]/(-mu0*0.5):.0f}")

# =============================================================================================
head("17.4  Reading a hysteresis loop (true or false)")
Br = 0.4 * np.pi
Hc = 8.0e5
print(f"   B_r = 0.4 pi = {Br:.4f} T")
check("(a) M at remanence = B_r/mu0 [A/m]", Br / mu0 - 0, 1.0e6)
check("(b) M at coercive point = 0/mu0 - (-Hc) [A/m] (not zero)", 0 / mu0 - (-Hc), 8.0e5)
check("(c) saturated: dB = mu0 dH for dH = 1e5 A/m [T]", mu0 * 1e5, 0.125664, rel=1e-5)

# =============================================================================================
head("17.5  A nickel rod as a solenoid")
N5, nmu, muB = 9.14e28, 0.60, 9.27e-24
M5 = N5 * nmu * muB
check("M = N m [A/m]", M5, 5.08367e5, rel=1e-5)
check("mu0 M [T]", mu0 * M5, 0.638832, rel=1e-5)
check("J_sM at phi = 0 (n = x): M z x x = M y = M phi_hat", np.cross(M5 * ZH, XH), [0, M5, 0])
check("end faces: M z x (+-z) = 0", [np.cross(ZH, ZH), np.cross(ZH, -ZH)], np.zeros((2, 3)))
check("equivalent current I = M/n, n = 1000/m [A]", M5 / 1000, 508.367, rel=1e-5)
a5, L5 = 5e-3, 2.0
Bc5 = quad(lambda zp: mu0 * M5 * a5**2 / (2 * (a5**2 + zp**2)**1.5), -L5 / 2, L5 / 2, epsabs=1e-14, epsrel=1e-12)[0]
check("brute force: 2-m rod, centre B by summing loops ~ mu0 M", Bc5, mu0 * M5, rel=2e-5)
print(f"   (2-m rod: B_centre/mu0M = {Bc5/(mu0*M5):.7f}; H = B/mu0 - M = {Bc5/mu0 - M5:.3g} A/m ~ 0)")

# =============================================================================================
head("17.6  Graded magnetization in a slab")
M06, d6 = 3.0e4, 0.02
Mf6 = lambda p: (M06 * (p[2] / d6)**2 * XH) if 0 < p[2] < d6 else np.zeros(3)
for zp in (0.005, 0.01, 0.015, 0.0199):
    Jfd = curl(Mf6, [0.3, -0.2, zp], h=1e-7)
    check(f"curl M at z = {zp*100:.2f} cm = (2 M0 z/d^2) y", Jfd, [0, 2 * M06 * zp / d6**2, 0], rel=1e-6, ab=1e-3)
print(f"   2 M0/d^2 = {2*M06/d6**2:.4g} A/m^3 ; J_M(1 cm) = {2*M06*0.01/d6**2:.4g} A/m^2 ; J_M(top) = {2*M06/d6:.4g} A/m^2")
JsTop = np.cross(M06 * XH, ZH)
check("top face: M(d) x z = -M0 y [A/m]", JsTop, [0, -3.0e4, 0])
check("bottom face: M(0) x (-z) = 0", np.cross(np.zeros(3), -ZH), [0, 0, 0])
vol6 = quad(lambda zp: 2 * M06 * zp / d6**2, 0, d6)[0]
check("volume current per metre of x = M0", vol6, M06)
check("net bound current through y = 0 (per m of x)", vol6 + JsTop[1], 0.0, ab=1e-9)
check("B(1 cm) = mu0 M0/4 [T]", mu0 * M06 / 4, 9.42478e-3, rel=1e-5)
check("B just below top = mu0 M0 [T]", mu0 * M06, 3.76991e-2, rel=1e-5)


def B6(zp):  # superposition of layers dz' (sheets K = J dz' y) + top sheet
    below = quad(lambda s: 2 * M06 * s / d6**2, 0, min(max(zp, 0), d6))[0] if zp > 0 else 0.0
    above = quad(lambda s: 2 * M06 * s / d6**2, min(max(zp, 0), d6), d6)[0] if zp < d6 else 0.0
    Bx = mu0 / 2 * (below - above)            # sheet K y: +mu0 K/2 x above it, -mu0 K/2 x below it
    Bx += mu0 / 2 * (1 if zp > d6 else -1) * JsTop[1]   # top sheet K = -M0 at z = d (below it: -mu0 K/2)
    return Bx


check("superposition B_x(1 cm) = mu0 M0/4", B6(0.01), mu0 * M06 / 4)
print(f"   pieces at z = 1 cm (units mu0 M0/2): below {0.25}, above {-0.75}, top sheet {+1.0}")
check("superposition B_x(0.5 cm), B_x(1.9 cm) = mu0 M (z/d)^2", [B6(0.005), B6(0.019)],
      [mu0 * M06 * 0.0625, mu0 * M06 * 0.9025])
check("superposition: B = 0 at z = -1 cm and z = 3 cm", [B6(-0.01), B6(0.03)], [0, 0], ab=1e-15)
check("jump at top: z x (0 - mu0 M0 x)/mu0 = J_sM", np.cross(ZH, -M06 * XH), JsTop)

# =============================================================================================
head("17.7  A wire of magnetic steel")
a7, I7, mur7 = 1e-3, 5.0, 200.0
chi7 = mur7 - 1
Ha = I7 / (2 * np.pi * a7)
check("H(a) = I/(2 pi a) [A/m]", Ha, 795.775, rel=1e-5)
check("B just inside = mu H(a) [T]", mur7 * mu0 * Ha, 0.2)
check("B just outside = mu0 H(a) [T]", mu0 * Ha, 1.0e-3)
Hin7 = lambda p: I7 / (2 * np.pi * a7**2) * np.array([-p[1], p[0], 0.0])
Mf7 = lambda p: chi7 * Hin7(p)
check("M(a) = 199 H(a) [A/m]", chi7 * Ha, 1.58359e5, rel=1e-5)
Jf7 = I7 / (np.pi * a7**2)
JM7 = curl(Mf7, [0.3e-3, 0.4e-3, 0.0], h=1e-9)
check("J_f = I/(pi a^2) [A/m^2]", Jf7, 1.59155e6, rel=1e-5)
check("curl M (FD at r = 0.5 mm) = chi_m J_f z", JM7, [0, 0, chi7 * Jf7], rel=1e-6)
print(f"   J_M = {chi7*Jf7:.4g} A/m^2 along +z")
check("curl H = J_f (FD)", curl(Hin7, [0.3e-3, 0.4e-3, 0.0], h=1e-9), [0, 0, Jf7], rel=1e-6)
JsM7 = np.cross(Mf7(np.array([a7, 0, 0])), XH)     # at phi = 0, n = x
check("J_sM = M(a) x r_hat [A/m]", JsM7, [0, 0, -chi7 * Ha], rel=1e-9)
Ivol = quad(lambda r: chi7 * Jf7 * 2 * np.pi * r, 0, a7)[0]
Isur = JsM7[2] * 2 * np.pi * a7
check("total volume magnetization current = chi I [A]", Ivol, 995.0)
check("total surface magnetization current = -chi I [A]", Isur, -995.0)
check("net bound current", Ivol + Isur, 0.0, ab=1e-9)
r7 = 0.5e-3
Itot = (I7 + chi7 * I7) * r7**2 / a7**2
check("vacuum Ampere inside (r=0.5 mm): mu0 I_tot/(2 pi r) = mu H", mu0 * Itot / (2 * np.pi * r7),
      mur7 * mu0 * I7 * r7 / (2 * np.pi * a7**2))
check("outside: enclosed I + 995 - 995 = I", I7 + Ivol + Isur, I7)
print(f"   B_out - B_in at r = a: {mu0*Ha - mur7*mu0*Ha:.4g} T")
check("jump at r=a: r_hat x (B_out - B_in)/mu0 = J_sM", np.cross(XH, (mu0 * Ha - mur7 * mu0 * Ha) * YH) / mu0, JsM7)
W7 = quad(lambda r: 0.5 * mur7 * mu0 * (I7 * r / (2 * np.pi * a7**2))**2 * 2 * np.pi * r, 0, a7)[0]
check("W' = mu I^2/(16 pi) [J/m]", W7, mur7 * mu0 * I7**2 / (16 * np.pi))
check("W' = 1.25e-4 J/m", W7, 1.25e-4)
check("L'_int = 2W'/I^2 = mu/(8 pi) = 1e-5 H/m", 2 * W7 / I7**2, 1.0e-5)
check("copper: mu0/(8 pi) = 5e-8 H/m", mu0 / (8 * np.pi), 5.0e-8)

# =============================================================================================
head("17.8  Field lines leaving iron")
mur8 = 2000.0
B2 = np.array([0.8, 0.01, -0.6])
n8 = YH                      # from medium 2 (iron, y<0) into medium 1 (air, y>0)
H2v = B2 / (mur8 * mu0)
check("H_iron = B/mu [A/m]", H2v, [318.310, 3.97887, -238.732], rel=1e-5)
H2n = (H2v @ n8) * n8
H2t = H2v - H2n
B1n = (B2 @ n8) * n8
H1 = H2t + B1n / mu0
B1 = mu0 * H1
check("B_air [T]", B1, [4e-4, 0.01, -3e-4])
check("H_air [A/m]", H1, [318.310, 7957.75, -238.732], rel=1e-5)
check("BC: n.(B1-B2) = 0, n x (H1-H2) = 0", np.r_[n8 @ (B1 - B2), np.cross(n8, H1 - H2v)], np.zeros(4), ab=1e-12)
tB2t = np.linalg.norm(B2 - (B2 @ n8) * n8) / abs(B2 @ n8)
tB1t = np.linalg.norm(B1 - (B1 @ n8) * n8) / abs(B1 @ n8)
print(f"   |B2t| = {np.linalg.norm(B2-(B2@n8)*n8):.4g} T, B2n = {B2@n8} T ; |B1t| = {np.linalg.norm(B1-(B1@n8)*n8)*1e3:.4g} mT, B1n = {B1@n8*1e3:.4g} mT")
check("tan(theta_iron) = 100, tan(theta_air) = 0.05", [tB2t, tB1t], [100, 0.05])
th2, th1 = np.degrees(np.arctan(tB2t)), np.degrees(np.arctan(tB1t))
check("theta_iron, theta_air [deg]", [th2, th1], [89.4271, 2.86241], rel=1e-5)
check("tan ratio = mu1/mu2 = 1/2000", tB1t / tB2t, 1 / 2000)
M2v = B2 / mu0 - H2v
check("M_iron = B/mu0 - H = 1999 H [A/m]", M2v, (mur8 - 1) * H2v)
check("M_iron values", M2v, [6.36302e5, 7953.77, -4.77226e5], rel=1e-5)
JsM8 = np.cross(n8, np.zeros(3) - M2v)
check("J_sM = n x (M1 - M2) [A/m]", JsM8, [4.77226e5, 0, 6.36302e5], rel=1e-5)
check("same from the iron's own face: M2 x n_out (n_out = +y)", np.cross(M2v, YH), JsM8)
check("|J_sM| = 0.9995 * 1.0 T/mu0", np.linalg.norm(JsM8), 0.9995 * 1.0 / mu0)
print(f"   |J_sM| = {np.linalg.norm(JsM8):.4g} A/m")
check("check: n x (B1 - B2)/mu0 = J_sM", np.cross(n8, B1 - B2) / mu0, JsM8)
print(f"   B1 - B2 = {fmt(B1 - B2)} T")
check("H_y jump air - iron = M2y (normal M shows up in H_n)", H1[1] - H2v[1], M2v[1])
print(f"   chi_m H_iron check (17.11 style): 1999 x H = {fmt(1999*H2v)}")

# =============================================================================================
head("17.9  Electret and magnet twins")
a9, P0, M09, dP0 = 0.01, 2.0e-6, 5.0e4, 0.4e-6
Pf = lambda p: (P0 / a9**2) * np.hypot(p[0], p[1]) * np.array([p[0], p[1], 0.0])     # P0 (r/a)^2 r_hat
Mf9 = lambda p: (M09 / a9**2) * np.hypot(p[0], p[1]) * np.array([-p[1], p[0], 0.0])  # M0 (r/a)^2 phi_hat
for rr in (0.005, 0.008):
    pt = rr * np.array([np.cos(0.7), np.sin(0.7), 0.0])
    check(f"rho_b = -div P at r = {rr*100} cm = -3 P0 r/a^2", -div(Pf, pt, h=1e-8), -3 * P0 * rr / a9**2, rel=1e-6)
    check(f"curl M at r = {rr*100} cm = 3 M0 r/a^2 z", curl(Mf9, pt, h=1e-8), [0, 0, 3 * M09 * rr / a9**2], rel=1e-6, ab=1e-2)
print(f"   rho_b(a/2) = {-3*P0*0.005/a9**2:.4g} C/m^3 ; J_M(a/2) = {3*M09*0.005/a9**2:.4g} A/m^2")
pa = np.array([a9, 0, 0])
check("rho_sb = P(a).r_hat = P0 [C/m^2]", Pf(pa) @ XH, P0)
check("J_sM = M(a) x r_hat = -M0 z [A/m]", np.cross(Mf9(pa), XH), [0, 0, -M09])
Qv = quad(lambda r: -3 * P0 * r / a9**2 * 2 * np.pi * r, 0, a9)[0]
check("volume bound charge per m = -2 pi a P0 [C/m]", Qv, -2 * np.pi * a9 * P0)
check("surface bound charge per m = +2 pi a P0 = 1.2566e-7 C/m", P0 * 2 * np.pi * a9, 1.25664e-7, rel=1e-5)
check("total bound charge", Qv + P0 * 2 * np.pi * a9, 0, ab=1e-20)
Iv9 = quad(lambda r: 3 * M09 * r / a9**2 * 2 * np.pi * r, 0, a9)[0]
check("volume magnetization current = 2 pi a M0 = 3141.6 A", Iv9, 3141.59, rel=1e-5)
check("total magnetization current", Iv9 - M09 * 2 * np.pi * a9, 0, ab=1e-8)


def E9(r):   # brute force: 2-D superposition of line charges (angular integral numerical)
    vol = quad(lambda rp: (-3 * P0 * rp / a9**2) * ring_G(r, rp) * rp, 0, a9, points=[r] if r < a9 else None,
               limit=200, epsabs=1e-16, epsrel=1e-10)[0]
    return (vol + P0 * a9 * ring_G(r, a9)) / (2 * np.pi * eps0)


def B9(r):   # brute force: 2-D superposition of infinite line currents along z
    vol = quad(lambda rp: (3 * M09 * rp / a9**2) * ring_G(r, rp) * rp, 0, a9, points=[r] if r < a9 else None,
               limit=200, epsabs=1e-14, epsrel=1e-10)[0]
    return mu0 * (vol + (-M09) * a9 * ring_G(r, a9)) / (2 * np.pi)


for rr in (0.005, 0.0099):
    check(f"E_r({rr*100} cm) brute force = -P/eps0", E9(rr), -P0 * (rr / a9)**2 / eps0, rel=1e-5)
    check(f"B_phi({rr*100} cm) brute force = mu0 M", B9(rr), mu0 * M09 * (rr / a9)**2, rel=1e-5)
check("E and B outside (r = 2 cm) brute force = 0", [E9(0.02), B9(0.02)], [0, 0], ab=1e-6)
check("E(a/2) = -P0/(4 eps0) [V/m]", -P0 / (4 * eps0), -5.64706e4, rel=1e-5)
check("E(a-) = -P0/eps0 [V/m]", -P0 / eps0, -2.25882e5, rel=1e-5)
check("B(a/2) = mu0 M0/4 [T]", mu0 * M09 / 4, 1.57080e-2, rel=1e-5)
check("B(a-) = mu0 M0 [T]", mu0 * M09, 6.28319e-2, rel=1e-5)
# (d) directions at a point
pt = np.array([0.005, 0, 0])
print(f"   at (a/2,0,0): P_hat = {fmt(Pf(pt)/np.linalg.norm(Pf(pt)))}, E along {fmt(-Pf(pt)/np.linalg.norm(Pf(pt)))} (against P)")
print(f"                 M_hat = {fmt(Mf9(pt)/np.linalg.norm(Mf9(pt)))}, B along M (B = +mu0 M)")
# (e) growing polarization
dPf = lambda p: Pf(p) * dP0 / P0
for rr in (0.005, 0.008):
    ptr = rr * np.array([np.cos(1.1), np.sin(1.1), 0.0])
    drho = -3 * dP0 * rr / a9**2
    check(f"continuity at r = {rr*100} cm: d(rho_b)/dt + div(dP/dt) = 0", drho + div(dPf, ptr, h=1e-8), 0, ab=1e-9)
check("dP/dt at a/2 = (dP0/dt)/4 = 0.1 uA/m^2", np.linalg.norm(dPf(pt)), 1.0e-7)
check("dP/dt arriving at r = a equals d(rho_sb)/dt = dP0/dt", dPf(pa) @ XH, dP0)
check("eps0 dE/dt = -dP/dt at a/2", eps0 * (-dPf(pt) / eps0), -dPf(pt))
check("dD/dt = eps0 dE/dt + dP/dt = 0", eps0 * (-dPf(pt) / eps0) + dPf(pt), [0, 0, 0])

# =============================================================================================
head("17.10  Three sheets and two slabs")
K1, K2, K3 = np.array([0, 4.0, 0]), np.array([3.0, -4.0, 0]), np.array([-3.0, 0, 0])
free10 = [(0.0, K1), (0.02, K2), (0.04, K3)]
check("K1 + K2 + K3 = 0", K1 + K2 + K3, [0, 0, 0])
zs = {"z<0": -0.01, "0<z<2": 0.01, "2<z<4": 0.03, "z>4": 0.05}
Hreg = {k: sheets_H(v, free10) for k, v in zs.items()}
for k, v in Hreg.items():
    print(f"   H({k}) = {fmt(v)} A/m")
check("H regions", list(Hreg.values()), [[0, 0, 0], [4, 0, 0], [0, -3, 0], [0, 0, 0]])
print(f"   contributions in 0<z<2: K1 -> {fmt(0.5*np.cross(K1, ZH))}, K2+K3 -> {fmt(0.5*np.cross(K2+K3, -ZH))}")
print(f"   contributions in 2<z<4: K1+K2 -> {fmt(0.5*np.cross(K1+K2, ZH))}, K3 -> {fmt(0.5*np.cross(K3, -ZH))}")
murL, murU = 25.0, 10.0
BL, BU = murL * mu0 * Hreg["0<z<2"], murU * mu0 * Hreg["2<z<4"]
ML, MU = (murL - 1) * Hreg["0<z<2"], (murU - 1) * Hreg["2<z<4"]
check("B lower = 100 mu0 x [T]", BL, [1.25664e-4, 0, 0], rel=1e-5)
check("B upper = -30 mu0 y [T]", BU, [0, -3.76991e-5, 0], rel=1e-5)
check("M lower, M upper [A/m]", [ML, MU], [[96, 0, 0], [0, -27, 0]])
n10 = ZH   # from lower (medium 2) into upper (medium 1)
check("n x (H1 - H2) = K2", np.cross(n10, Hreg["2<z<4"] - Hreg["0<z<2"]), K2)
check("n . (B1 - B2) = 0", n10 @ (BU - BL), 0.0)
jumpB = np.cross(n10, BU - BL) / mu0
check("n x (B1 - B2)/mu0 = 30 x - 100 y [A/m]", jumpB, [30, -100, 0])
Jb0 = np.cross(ML, -ZH)
Jb2 = np.cross(n10, MU - ML)
Jb4 = np.cross(MU, ZH)
check("J_sM at z = 0 (M_L x -z)", Jb0, [0, 96, 0])
check("J_sM at z = 2 cm (z x (M_U - M_L))", Jb2, [27, -96, 0])
check("J_sM at z = 2 cm also = M_L x (+z) + M_U x (-z)", np.cross(ML, ZH) + np.cross(MU, -ZH), Jb2)
check("J_sM at z = 4 cm (M_U x z)", Jb4, [-27, 0, 0])
check("sum of magnetization currents = 0", Jb0 + Jb2 + Jb4, [0, 0, 0])
check("jump = K2 + J_sM(interface)", K2 + Jb2, jumpB)
tot10 = [(0.0, K1 + Jb0), (0.02, K2 + Jb2), (0.04, K3 + Jb4)]
for z0, Kt in tot10:
    print(f"   total sheet at z = {z0*100:.0f} cm: {fmt(Kt)} A/m")
check("vacuum formula with free+bound: B lower, B upper", [mu0 * sheets_H(0.01, tot10), mu0 * sheets_H(0.03, tot10)], [BL, BU])
check("vacuum formula: B outside = 0", [mu0 * sheets_H(-0.01, tot10), mu0 * sheets_H(0.05, tot10)], np.zeros((2, 3)))
chiBi = -1.7e-4
MBi = chiBi * Hreg["0<z<2"]
JBi = np.cross(MBi, -ZH)
check("bismuth: M = -6.8e-4 x A/m", MBi, [-6.8e-4, 0, 0])
check("bismuth: J_sM at z = 0 = -6.8e-4 y A/m (opposite K1)", JBi, [0, -6.8e-4, 0])
print(f"   J_sM(Bi).K1 = {JBi @ K1:.3g} < 0 -> opposes the free sheet")

# =============================================================================================
head("17.11  A toroid with an air gap")
R11, A11, g11, mur11, N11, I11 = 0.05, 1e-4, 1e-3, 4000.0, 250, 0.2
NI = N11 * I11
li = 2 * np.pi * R11 - g11
print(f"   NI = {NI} A ; mean length 2 pi R = {2*np.pi*R11:.5f} m ; iron path l_i = {li:.5f} m")
Bsol = brentq(lambda B: B / (mur11 * mu0) * li + B / mu0 * g11 - NI, 1e-9, 5.0, xtol=1e-15)
Bcf = mu0 * NI / (g11 + li / mur11)
check("B (brentq) = mu0 NI/(g + l_i/mu_r) [T]", Bsol, Bcf, rel=1e-10)
check("B = 0.05827 T", Bcf, 0.0582695, rel=1e-5)
Hg, Hi = Bcf / mu0, Bcf / (mur11 * mu0)
check("H_gap, H_iron [A/m]", [Hg, Hi], [4.63698e4, 11.5925], rel=1e-5)
print(f"   H_i l_i = {Hi*li:.3f} A ; H_g g = {Hg*g11:.3f} A ; sum = {Hi*li+Hg*g11:.6f} A ; gap share = {Hg*g11/NI*100:.2f} %")
B0 = mur11 * mu0 * NI / (2 * np.pi * R11)
check("no gap: B0 = mu NI/(2 pi R) [T]", B0, 0.8, rel=1e-9)
print(f"   B0/B = {B0/Bcf:.3f}")
Psi = Bcf * A11
L11 = N11 * Psi / I11
check("Psi = B A [Wb], N Psi [Wb]", [Psi, N11 * Psi], [5.82695e-6, 1.45674e-3], rel=1e-5)
check("L = N Psi/I = mu0 N^2 A/(g + l_i/mu_r) [H]", L11, mu0 * N11**2 * A11 / (g11 + li / mur11))
check("L = 7.284 mH", L11, 7.28368e-3, rel=1e-5)
L0 = mur11 * mu0 * N11**2 * A11 / (2 * np.pi * R11)
check("no gap: N Psi0 = 0.02 Wb, L0 = 0.1 H", [N11 * B0 * A11, L0], [0.02, 0.1], rel=1e-9)
W11 = 0.5 * L11 * I11**2
Wg = 0.5 * Bcf * Hg * A11 * g11
Wi = 0.5 * Bcf * Hi * A11 * li
check("W = L I^2/2 = field energy (gap + iron) [J]", W11, Wg + Wi)
check("W = 1.4567e-4 J", W11, 1.45674e-4, rel=1e-5)
check("gap fraction = H_g g/NI = 92.74 %", Wg / W11, 0.927396, rel=1e-5)
M11 = Bcf / mu0 - Hi
check("M = B/mu0 - H_i = chi_m H_i [A/m]", M11, (mur11 - 1) * Hi)
check("M = 4.6358e4 A/m", M11, 4.63582e4, rel=1e-5)
Kfree = NI / (2 * np.pi * R11)
check("free winding current per metre NI/(2 pi R) [A/m]", Kfree, 159.155, rel=1e-5)
print(f"   bound/free per metre = {M11/Kfree:.1f}")
# Vacuum Ampere around the mean circle counts the free current NI plus the bound sheet M (per metre of
# iron) crossing the disk along the iron length l_i:  (B/mu0)(l_i + g) = H_i l_i + M l_i + H_g g = NI + M l_i.
check("vacuum Ampere: (B/mu0)(2 pi R) = NI + M l_i (exact in this model)", (Bcf / mu0) * (li + g11), NI + M11 * li,
      rel=1e-12)
print(f"   (B/mu0)(2 pi R) = {Bcf/mu0*2*np.pi*R11:.1f} A ; NI = {NI:.0f} A ; M l_i = {M11*li:.1f} A")
print(f"   M l_i = {M11*li:.4g} A ; NI + M l_i = {NI+M11*li:.5g} A")
emf = L11 * 20.0
check("|emf| = L dI/dt at 20 A/s [V]", emf, 0.145674, rel=1e-5)
B8000 = mu0 * NI / (g11 + li / 8000)
print(f"   sensitivity: mu_r 4000 -> 8000 changes L from {L11*1e3:.3f} mH to {N11*B8000*A11/I11*1e3:.3f} mH")

# =============================================================================================
head("17.12  A short bar magnet")
a12, l12, M012 = 0.01, 0.02, 9.0e5
mM = mu0 * M012
check("mu0 M0 [T]", mM, 1.130973, rel=1e-6)


def Bz_axis(z, a=a12, l=l12, M=M012):
    return mu0 * M / 2 * ((l / 2 - z) / np.hypot(l / 2 - z, a) + (l / 2 + z) / np.hypot(l / 2 + z, a))


def Bz_loops(z):
    return quad(lambda zp: mu0 * M012 * a12**2 / (2 * (a12**2 + (z - zp)**2)**1.5), -l12 / 2, l12 / 2,
                epsabs=1e-14, epsrel=1e-12)[0]


def B_biot(p, nphi=1200, nz=1200):
    ph = (np.arange(nphi) + 0.5) * 2 * np.pi / nphi
    zz = -l12 / 2 + (np.arange(nz) + 0.5) * l12 / nz
    PH, ZZ = np.meshgrid(ph, zz, indexing="ij")
    src = np.stack([a12 * np.cos(PH), a12 * np.sin(PH), ZZ], axis=-1)
    K = M012 * np.stack([-np.sin(PH), np.cos(PH), np.zeros_like(PH)], axis=-1)   # M x r_hat = M0 phi_hat
    Rv = np.asarray(p, float) - src
    Rn = np.linalg.norm(Rv, axis=-1)[..., None]
    dA = a12 * (2 * np.pi / nphi) * (l12 / nz)
    return mu0 / (4 * np.pi) * np.sum(np.cross(K, Rv) / Rn**3, axis=(0, 1)) * dA


check("J_sM on side at phi=0: M0 z x x = M0 y", np.cross(M012 * ZH, XH), [0, M012, 0])
for zf, lab in ((0.0, "centre"), (l12 / 2, "end face")):
    bc = Bz_axis(zf)
    check(f"B_z {lab}: formula vs loop integral", Bz_loops(zf), bc, rel=1e-9)
    check(f"B {lab}: formula vs Biot-Savart sum over the side current", B_biot([0, 0, zf]), [0, 0, bc], rel=2e-5, ab=1e-9)
Bc12, Be12 = Bz_axis(0.0), Bz_axis(l12 / 2)
check("B centre = mu0 M0/sqrt2 [T]", Bc12, mM / np.sqrt(2))
check("B centre = 0.7997 T", Bc12, 0.799718, rel=1e-5)
check("B end face = (mu0 M0/2)(2/sqrt5) [T]", Be12, mM / 2 * 2 / np.sqrt(5))
check("B end = 0.5058 T", Be12, 0.505787, rel=1e-5)
Hc12 = Bc12 / mu0 - M012
He_in, He_out = Be12 / mu0 - M012, Be12 / mu0
check("H centre = M0(1/sqrt2 - 1) [A/m]", Hc12, M012 * (1 / np.sqrt(2) - 1))
check("H centre = -2.636e5 A/m (along -z)", Hc12, -2.63604e5, rel=1e-5)
check("H end inside, outside [A/m]", [He_in, He_out], [-4.97508e5, 4.02492e5], rel=1e-5)
check("B continuity across end face (just inside/outside, formula)", Bz_axis(l12 / 2 - 1e-9), Bz_axis(l12 / 2 + 1e-9), rel=1e-6)
check("H_out - H_in = M0 = -(M1n - M2n)", He_out - He_in, -(0 - M012))
for ratio in (100.0, 0.01):
    l = ratio * a12
    bc = Bz_axis(0.0, l=l) / mM
    print(f"   l/a = {ratio:g}: B_centre/(mu0 M0) = {bc:.6f}, H_centre/M0 = {bc-1:.6f}; l/(2a) = {l/(2*a12):.4g}")
le = 200 * a12
check("long rod: end-face B -> mu0 M0/2", Bz_axis(le / 2, l=le) / mM, 0.5, rel=1e-4)

# =============================================================================================
print("\n" + "=" * 96)
print("ANSWER 17.1: m = 4.0e-3 z A m^2; T = 1.2e-3 y N m, F = 0; x=4 cm edge sinks (F_z = -0.03 N), x=0 edge rises; stable at m || B (tilt 36.9 deg about y); electron m along -z, also turned toward B")
print("ANSWER 17.2: (a); chi = -9.4e-6, 2.1e-5, 8.0e-4, 500; mu_r = 0.9999906, 1.000021, 1.0008, 501; B_S = 0.252 T; dB_P = -4.7 nT")
print("ANSWER 17.3: slip = normal-B rule for a tangential field; H = -0.5 y A/m, B = -3.14e-4 y T, M = -249.5 y A/m; J_sM = -249.5 x (z=3 cm), +249.5 x (z=1 cm)")
print("ANSWER 17.4: T F T F F F")
print("ANSWER 17.5: M = 5.08e5 z A/m; J_M = 0, J_sM = 5.08e5 phi A/m; B = 0.639 z T, H = 0; I = 508 A")
print("ANSWER 17.6: J_M = 1.5e8 z y A/m^2; J_sM = -3.0e4 y A/m on z = d; net 0; H = 0; B = mu0 M0 (z/d)^2 x: 9.42 mT, 37.7 mT, 0")
print("ANSWER 17.7: B 0.200 T in / 1.00 mT out; M(a) = 1.58e5 A/m; J_M = 3.17e8 z A/m^2 (995 A); J_sM = -1.58e5 z A/m (-995 A); L'_int = 10 uH/m")
print("ANSWER 17.8: H_Fe = (318.3, 3.98, -238.7) A/m; B_air = (0.4, 10, -0.3) mT; H_air = (318.3, 7958, -238.7) A/m; 89.43 / 2.86 deg; J_sM = (4.772e5, 0, 6.363e5) A/m")
print("ANSWER 17.9: rho_b = -3P0 r/a^2, rho_sb = P0, -+126 nC/m; J_M = 3M0 r/a^2 z, J_sM = -M0 z, +-3.14 kA; E(a/2) = -56.5 kV/m, B(a/2) = 15.7 mT")
print("ANSWER 17.10: H = 0, 4x, -3y, 0; B = 1.26e-4 x T, -3.77e-5 y T; M = 96x, -27y; J_sM = 96y, 27x-96y, -27x; Bi: -6.8e-4 y")
print("ANSWER 17.11: B = 58.3 mT (0.800 T no gap); H_i = 11.6, H_g = 4.64e4 A/m; L = 7.28 mH (100 mH); gap 92.7 %; M = 4.64e4 A/m; emf 0.146 V")
print("ANSWER 17.12: J_sM = 9e5 phi A/m; B = 0.800 T (centre), 0.506 T (end); H = -2.64e5, -4.98e5 in / +4.02e5 out A/m")
print("=" * 96)
print(f"checks run: {NCHK};  failures: {len(FAILS)}")
for f in FAILS:
    print("   FAILED:", f)
