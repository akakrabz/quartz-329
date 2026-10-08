#!/usr/bin/env python3
"""Verification of every number, sign and direction on the Lecture 19 pages of the ECE 329 study site.

Pages checked:
  content-src/3-maxwell-and-waves/19-dalembert-solutions-and-radiation-from-current-sheets.md
  content-src/concepts/current-sheet-radiation.md, content-src/concepts/poynting-vector.md
  content-src/problems/a-current-sheet-launches-two-waves.md
  figs_l19.py (arrow directions, screen frame X right, Y up, Z out of the screen)
numpy only; derivatives by central finite differences; every vector direction by an explicit np.cross.
"""
import numpy as np

mu0 = 1.25663706212e-6
eps0 = 8.8541878128e-12
c = 1 / np.sqrt(mu0 * eps0)
eta0 = np.sqrt(mu0 / eps0)
X, Y, Z = np.eye(3)
cr = np.cross
ok_count = 0

def ok(cond, msg):
    global ok_count
    assert cond, "FAILED: " + msg
    ok_count += 1
    print("ok  ", msg)

def close(a, b, msg, rtol=1e-6, atol=1e-12):
    ok(np.allclose(a, b, rtol=rtol, atol=atol), f"{msg}: {np.round(a, 6)} vs {np.round(b, 6)}")

print("=== A. constants")
close(c, 2.99792458e8, "c")
close(eta0, 376.730313, "eta0 [ohm]")
close(120 * np.pi, 376.991118, "120 pi")
close(abs(120 * np.pi - eta0) / eta0, 6.92e-4, "120pi relative error", rtol=1e-2)
close(eta0 / 2, 188.365, "eta0/2", rtol=1e-5)
close(mu0 / eta0, 1 / c, "mu0/eta0 = 1/c")

print("=== B. Notes Example 1: E = x tri((t - y/c)/tau), H and B")
tri = lambda u: np.clip(1 - 2 * np.abs(u), 0, None)     # unit-duration triangle, support |u| < 1/2
tau = 1e-6
Ex = lambda y, t: tri((t - y / c) / tau)
Bz = lambda y, t: -tri((t - y / c) / tau) / c          # page: B = -z tri / c
y0, t0, h = 40.0, 0.05e-6, 1e-12
dBdt = (Bz(y0, t0 + h) - Bz(y0, t0 - h)) / (2 * h)
dEdy = (Ex(y0 + 1e-3, t0) - Ex(y0 - 1e-3, t0)) / 2e-3
close(dBdt, dEdy, "Faraday z-component: dBz/dt = +dEx/dy (= -(curl E)_z)", rtol=1e-4)
close(cr(X, -Z), Y, "E x H = x cross (-z) = +y (travel +y)")
close(cr(Y, X), -Z, "H = u x E / eta: y cross x = -z")

print("=== C. Notes Example 2: magnetic/electric force ratio = v_perp/c")
for v in (1e6 * X, 1e6 * Y, 1e6 * Z, 2e8 * X):
    Evec = X * 1.0; Bvec = -Z / c
    ratio = np.linalg.norm(cr(v, Bvec)) / np.linalg.norm(Evec)
    vperp = np.linalg.norm(v - np.dot(v, Z) * Z)
    close(ratio, vperp / c, f"v = {v}: |v x B|/|E| = {ratio:.4g}")
close(1e6 / c, 3.336e-3, "1e6 m/s: ratio 3.34e-3", rtol=1e-3)
close(2e8 / c, 0.667, "2e8 m/s: ratio 0.667", rtol=1e-3)

print("=== D. Notes Example 3: ramp pulse, c = 300 m/us")
cc = 300.0       # m/us
f3 = lambda t: np.where(np.abs(t) < 0.5, 2 * t, 0.0)      # V/m, t in us
E3 = lambda z, t: f3(t - z / cc)
close(600 / cc, 2.0, "z/c = 2 us at 600 m")
close([E3(0, -0.4999), E3(0, 0.4999)], [-1, 1], "E(0,t): -1 -> +1 over |t| < 0.5 us", rtol=1e-3)
close([E3(600, 1.5001), E3(600, 2.0), E3(600, 2.4999)], [-1, 0, 1], "E(600 m,t): -1 at 1.5, 0 at 2, +1 at 2.5 us", rtol=1e-3, atol=1e-3)
close([E3(-149.99, 0), E3(149.99, 0)], [1, -1], "E(z,0): +1 at -150 m, -1 at +150 m", rtol=1e-3)
close([E3(450.01, 2), E3(600, 2), E3(749.99, 2)], [1, 0, -1], "E(z,2us): +1 at 450, 0 at 600, -1 at 750", rtol=1e-3, atol=1e-3)
close(1 / eta0, 2.654e-3, "H peak 1/eta0 = 2.65 mA/m", rtol=1e-3)
close(cr(X, Y), Z, "x cross y = z (travel +z)")

print("=== E. The radiating sheet (notes' orientation J_s = x f(t), z = 0), general medium")
for epsr, mur in ((1, 1), (4, 1), (2, 3)):
    eps, mu = epsr * eps0, mur * mu0
    v, eta = 1 / np.sqrt(mu * eps), np.sqrt(mu / eps)
    fJ = lambda t: np.exp(-((t - 3e-9) / 1e-9) ** 2) * np.cos(2e9 * t)      # A/m, arbitrary
    def Ex_(z, t): return -eta / 2 * fJ(t - np.abs(z) / v)
    def Hy_(z, t): return -np.sign(z) * fJ(t - np.abs(z) / v) / 2
    for z0 in (0.37, -0.52):
        t0 = 4.1e-9; dz = 1e-5; dt = dz / v
        dEdz = (Ex_(z0 + dz, t0) - Ex_(z0 - dz, t0)) / (2 * dz)
        dHdt = (Hy_(z0, t0 + dt) - Hy_(z0, t0 - dt)) / (2 * dt)
        dHdz = (Hy_(z0 + dz, t0) - Hy_(z0 - dz, t0)) / (2 * dz)
        dEdt = (Ex_(z0, t0 + dt) - Ex_(z0, t0 - dt)) / (2 * dt)
        sc = abs(dEdz) + abs(mu * dHdt) + 1e-30
        ok(abs(dEdz + mu * dHdt) / sc < 1e-5, f"epsr={epsr}, mur={mur}, z={z0}: Faraday dEx/dz = -mu dHy/dt")
        sc = abs(dHdz) + abs(eps * dEdt) + 1e-30
        ok(abs(-dHdz - eps * dEdt) / sc < 1e-5, f"epsr={epsr}, mur={mur}, z={z0}: Ampere -dHy/dz = eps dEx/dt")
    t0 = 3.3e-9; zp, zm = 1e-12, -1e-12
    close(Ex_(zp, t0), Ex_(zm, t0), "E_x continuous at the sheet")
    Hp, Hm = Hy_(zp, t0) * Y, Hy_(zm, t0) * Y
    close(cr(Z, Hp - Hm), fJ(t0) * X, "z cross (H1 - H2) = J_s (n from 2 = z<0 into 1 = z>0)")
    close(Ex_(zp, t0) / fJ(t0), -eta / 2, "E_x / J_x = -eta/2 at the sheet")
# directions
close(cr(-X, -Y), Z, "z>0: E x H = (-x) cross (-y) = +z")
close(cr(-X, Y), -Z, "z<0: E x H = (-x) cross (+y) = -z")
close(0.5 * cr(X, Z), -0.5 * Y, "static sheet 1/2 J x n, z>0: -y/2")
close(0.5 * cr(X, -Z), 0.5 * Y, "static sheet 1/2 J x n, z<0: +y/2")
ok(np.dot(X, -eta0 / 2 * X) < 0, "J_s . E = -eta/2 |J_s|^2 < 0 (sheet is a source)")

print("=== F. Slides' route: J_s = -J_s(t) x, region 1 = z>0, a_n = z")
Js = 0.8
Af = eta0 / 2 * Js
close(Af, 150.692, "A f(t) = eta0/2 J_s for J_s = 0.8 A/m", rtol=1e-5)
H1, H2 = Af / eta0 * Y, -Af / eta0 * Y
close(cr(Z, H1 - H2), -Js * X, "a_z x (H1 - H2) = -J_s x = vec J_s")
close(cr(X, Y), Z, "slides z>0: x cross y = +z"); close(cr(X, -Y), -Z, "slides z<0: x cross (-y) = -z")
ok(np.dot(Af * X, -Js * X) < 0, "slides: E . J_s < 0")
# compact rule E = -(eta/2) J_s, H = 1/2 J_s x n, for random orientations: E x H along +n
rng = np.random.default_rng(1)
for _ in range(5):
    n = rng.normal(size=3); n /= np.linalg.norm(n)
    J = rng.normal(size=3); J -= np.dot(J, n) * n
    E = -eta0 / 2 * J; H = 0.5 * cr(J, n)
    S = cr(E, H)
    close(S / np.linalg.norm(S), n, "random sheet: E x H along n (away from sheet)")
    close(np.linalg.norm(E) / np.linalg.norm(H), eta0, "random sheet: |E|/|H| = eta")
    close(cr(n, H - 0.5 * cr(J, -n)), J, "random sheet: n x (H1 - H2) = J_s")

print("=== G. Notes Example 4: ramp sheet current, t = 2 us, c = 300 m/us, eta = 120 pi")
fJ4 = lambda t: np.where(np.abs(t) < 0.5, 2 * t, 0.0)      # A/m, t in us
H4 = lambda z, t: -np.sign(z) * fJ4(t - np.abs(z) / cc) / 2
E4 = lambda z, t: -120 * np.pi / 2 * fJ4(t - np.abs(z) / cc)
for z, Hexp, Eexp in ((-749.99, -0.5, 60 * np.pi), (-600, 0, 0), (-450.01, 0.5, -60 * np.pi),
                      (450.01, -0.5, -60 * np.pi), (600, 0, 0), (749.99, 0.5, 60 * np.pi)):
    close([H4(z, 2.0), E4(z, 2.0)], [Hexp, Eexp], f"Ex.4 z = {z:.0f} m: H_y, E_x", rtol=1e-3, atol=1e-3)
close(60 * np.pi, 188.5, "60 pi = 188.5 V/m", rtol=1e-3)
close(E4(500, 2.0), E4(-500, 2.0), "E_x even in z"); close(H4(500, 2.0), -H4(-500, 2.0), "H_y odd in z")

print("=== H. Slide 17 (sheet on y = 0, current along -z)")
close(0.5 * cr(-Z, Y), 0.5 * X, "y>0: H = 1/2(-z) x y = +x/2"); close(0.5 * cr(-Z, -Y), -0.5 * X, "y<0: -x/2")
close(-eta0 / 2 * (-Z), eta0 / 2 * Z, "E = -(eta/2) J_s = +z eta/2 J_s")
close(cr(Z, X), Y, "y>0: E x H = z cross x = +y"); close(cr(Z, -X), -Y, "y<0: z cross (-x) = -y")
close(eta0 * 1.0, 376.73, "|E| = eta0 H0", rtol=1e-5)

print("=== I. Slide 11: transforming time and space, v = +100 m/s")
zp_ = np.array([-100, 0, 100, 300, 400.]); Fp = np.array([0, 1, -1, 0, 0.])
F = lambda z: np.interp(z, zp_, Fp, left=0, right=0)
E11 = lambda z, t: F(z - 100 * t)
close([E11(z, 1) for z in (0, 100, 200, 400, 500)], [0, 1, -1, 0, 0], "(a) E(z,1s) at 0,100,200,400,500")
close([E11(50, 0), E11(150, 1)], [0, 0], "(a) zero crossing moves 50 -> 150 m")
close([E11(0, t) for t in (1, 0, -1, -3, -4)], [0, 1, -1, 0, 0], "(b) E(0,t) at t = 1,0,-1,-3,-4 s")
close(E11(0, -0.5), 0, "(b) zero crossing at t = -0.5 s")
close([E11(200, t) for t in (3, 2, 1.5, 1, 0, -1, -2)], [0, 1, 0, -1, -0.5, 0, 0], "(c) E(200 m,t) at 3,2,1.5,1,0,-1,-2 s")
ts = np.linspace(-6, 6, 241)
close(E11(200, ts), E11(0, ts - 2), "(c) E(200,t) = E(0, t - 2 s)")

print("=== J. Sinusoidal sheet, Poynting vector, wave parameters")
f = 100e6; w = 2 * np.pi * f; beta = w / c; lam = 2 * np.pi / beta
close([beta, lam, lam * f], [2.0958, 2.9979, c], "100 MHz: beta, lambda, lambda f = c", rtol=1e-4)
JS0 = 1.0
for z in (0.4, -0.4):
    s = np.sign(z); tt = 1.3e-9
    ph = w * tt - s * beta * z
    E = eta0 * JS0 / 2 * np.cos(ph) * X
    H = s * JS0 / 2 * np.cos(ph) * Y
    S = cr(E, H)
    close(S, s * eta0 * JS0 ** 2 / 4 * np.cos(ph) ** 2 * Z, f"S = E x H = +/- eta0 J^2/4 cos^2 z^ at z = {z}")
    # phase derivatives
    dphdt = w; dphdz = -s * beta
    close(abs(dphdz), beta, "beta = |d phi/dz|"); close(-s * dphdz, beta, "beta = -/+ d phi / dz (upper z>0)")
close(eta0 / 4, 94.18, "peak S per side, J_S0 = 1 A/m: eta0/4 = 94.2 W/m^2", rtol=1e-3)
close(eta0 * 0.1 ** 2 / 4, 0.9418, "J_S0 = 0.1 A/m: peak 0.94 W/m^2", rtol=1e-3)
# energy check of the page's statement: per side peak S = eta0/4 J^2, both sides = eta0/2 J^2 = -J.E at the sheet
ok(np.isclose(2 * eta0 / 4 * JS0 ** 2, -np.dot(-JS0 * X, eta0 / 2 * JS0 * X)), "2 x (eta/4 J^2) = -J_s . E = eta/2 J^2 at the sheet")
# S = |E|^2/eta = eta |H|^2
E0 = eta0 * JS0 / 2; H0 = JS0 / 2
close([E0 ** 2 / eta0, eta0 * H0 ** 2], [eta0 / 4, eta0 / 4], "S = E^2/eta = eta H^2")
# SP18 Exam 2 #1(vii)
w7 = 3 * np.pi / 10e-6; f7 = w7 / (2 * np.pi); lam7 = 3e8 / f7
close([w7, f7, lam7], [3 * np.pi * 1e5, 1.5e5, 2000.0], "SP18 E2 #1(vii): omega, f, lambda")
# 1 MHz in free space check for the concept page
close(c / 1e6, 299.79, "lambda at 1 MHz = 300 m", rtol=1e-4)

print("=== K. Slides 18-21 (x = 0 sheet), plot scale (peak 2 A/m) and printed-formula scale (x100)")
cu = 300.0     # m/us, as the stem implies free space
for scale, lab in ((0.02, "plot scale"), (2.0, "formula scale")):
    Fk = lambda xi: np.where((xi > 0) & (xi < 100), scale * xi, 0.0)
    Hk = lambda x, t: np.where(x > 0, Fk(x - cu * (t - 1)), -Fk(-x - cu * (t - 1)))
    pk = scale * 100
    close(float(Hk(400, 2.0001)), scale * (400 - 300 * 1.0001), f"[{lab}] (a) H_y(400 m, 2.0001 us) just below peak")
    close([float(Hk(400, 2.3)), float(Hk(400, 7 / 3 + 1e-6)), float(Hk(400, 1.999))], [pk * 0.1, 0, 0], f"[{lab}] (a) 2.3 us: 10% of peak; 0 after 7/3 us and before 2 us", atol=1e-3 * pk)
    close([float(Hk(x, 4)) for x in (999.999, 950, 900, -999.999, -950, -900, 1100, 0)],
          [pk, pk / 2, 0, -pk, -pk / 2, 0, 0, 0], f"[{lab}] (b) H_y(x, 4 us)", atol=1e-3 * pk)
    Ek = lambda x, t: -eta0 * Fk(np.abs(x) - cu * (t - 1))       # E_z, even in x
    close([float(Ek(x, 2)) for x in (399.9999, 350, 300, -399.9999, -350, 0)],
          [-eta0 * pk, -eta0 * pk / 2, 0, -eta0 * pk, -eta0 * pk / 2, 0], f"[{lab}] (c) E_z(x, 2 us)", rtol=1e-5, atol=1e-6)
    Jk = lambda t: 2 * Fk(cu * (1 - t))                           # J_s,z(t)
    close([float(Jk(2 / 3 + 1e-9)), float(Jk(0.8)), float(Jk(1.0)), float(Jk(0.5))],
          [2 * pk, 2 * pk * 0.6, 0, 0], f"[{lab}] (d) J_s,z at 2/3+, 0.8, 1.0, 0.5 us", rtol=1e-6, atol=1e-6)
    close(2 * scale * 300, {0.02: 12, 2.0: 1200}[scale], f"[{lab}] (d) J_s = {2*scale*300:.0f}(1 - t/us) z^")
close(eta0 * 2, 753.5, "plot scale (c) peak |E_z| = 2 eta0 = 753 V/m (754 with 120 pi)", rtol=1e-3)
close(cr(X, Y), Z, "(d) x cross (H(0+) - H(0-)) along +z for H along +y")
close(0.5 * cr(Z, X), 0.5 * Y, "(d) consistency: 1/2 J_s x n with J along z, n = +x gives +y")
close(cr(-Z, Y), X, "(c) E along -z, H along +y: E x H = +x (travel +x)")

print("=== L. Worked problem: sheet on x = 0, J_s = +J_s(t) y, eps_r = 4, mu_r = 1")
epsr = 4.0
v = c / np.sqrt(epsr); eta = eta0 / np.sqrt(epsr)
close([v, eta], [1.49896e8, 188.365], "v = c/2, eta = eta0/2", rtol=1e-5)
close(60 * np.pi, 188.50, "60 pi approx", rtol=1e-4)
vns = 0.15     # m/ns (rounded c/2, as the problem states)
def Jw(t):     # A/m, t in ns: ramp 0 -> 6 over 0..2 ns, then -2 for 2..4 ns, then 0
    t = np.asarray(t, float)
    return np.where((t > 0) & (t < 2), 3 * t, np.where((t >= 2) & (t < 4), -2.0, 0.0))
close(0.5 * cr(Y, X), -0.5 * Z, "(a) x>0: H = 1/2 y cross x = -z/2")
close(0.5 * cr(Y, -X), 0.5 * Z, "(a) x<0: H = 1/2 y cross (-x) = +z/2")
close(cr(-Y, -Z), X, "(b) x>0: E x H = (-y) cross (-z) = +x"); close(cr(-Y, Z), -X, "(b) x<0: (-y) cross z = -x")
Hz = lambda x, t: np.where(x > 0, -0.5 * Jw(t - x / vns), 0.5 * Jw(t + x / vns))
Ey = lambda x, t: -eta / 2 * Jw(t - np.abs(x) / vns)
close([vns * 2, vns * 4, vns * 6], [0.3, 0.6, 0.9], "distances 0.3, 0.6, 0.9 m for 2, 4, 6 ns")
xs = [0.1, 0.299, 0.301, 0.45, 0.599, 0.601, 0.75, 0.899, 0.95]
exp = [0, 0, 1, 1, 1, -3, -1.5, 0, 0]
close([float(Hz(x, 6)) for x in xs], exp, "(c) H_z(x, 6 ns), x > 0", atol=0.02)
close([float(Hz(-x, 6)) for x in xs], [-e for e in exp], "(c) H_z odd in x", atol=0.02)
close([float(Ey(x, 6)) for x in (0.45, 0.601, 0.75, -0.45, -0.601)],
      [eta, -3 * eta, -1.5 * eta, eta, -3 * eta], "(c) E_y(x, 6 ns) = +eta, -3 eta, -1.5 eta (even)", rtol=1e-2)
close([eta, 3 * eta, 1.5 * eta], [188.4, 565.1, 282.5], "E_y levels 188, 565, 283 V/m", rtol=1e-3)
# (d) Poynting vector at x = 0.75 m, t = 6 ns
E = float(Ey(0.75, 6)) * Y; H = float(Hz(0.75, 6)) * Z
S = cr(E, H)
close(S, eta * 9 / 4 * X, "(d) S(0.75 m, 6 ns) = eta J^2/4 x^ with J = 3 A/m")
close(eta * 9 / 4, 423.8, "(d) 424 W/m^2", rtol=1e-3)
E = float(Ey(-0.75, 6)) * Y; H = float(Hz(-0.75, 6)) * Z
close(cr(E, H), -eta * 9 / 4 * X, "(d) S(-0.75 m, 6 ns) = -424 x^")
# largest S in the snapshot: just beyond 0.6 m where |J| = 6 A/m
close(eta * 36 / 4, 1695.3, "(d) peak S at x = 0.6+ m: eta 36/4 = 1.70 kW/m^2", rtol=1e-3)
# (e) probe at x = -0.45 m records H_z(t)
close([float(Hz(-0.45, t)) for t in (2.9, 3.5, 4.9, 5.1, 6.9, 7.1)], [0, 0.75, 2.85, -1, -1, 0], "(e) probe at -0.45 m: H_z(t)", atol=1e-6)
close(0.45 / vns, 3.0, "(e) delay 0.45/0.15 = 3 ns")
# variant: free space, same current: amplitudes x2 for E, same H
close(eta0 / eta, 2.0, "variant: in vacuum E doubles, H unchanged")

print("=== M. Lecture 15 connection: current source driving two parallel-plate lines")
d, Wd = 1e-3, 1e-2
Z0 = eta0 * d / Wd
close(Z0 / 2, eta0 * d / (2 * Wd), "two lines Z0 in parallel = Z0/2")
I = Wd * 1.0   # total current for J_s = 1 A/m across width W
V = I * Z0 / 2
close(V / d, eta0 / 2 * 1.0, "E = V/d = eta/2 J_s: same as the sheet")
close(1 / np.sqrt((mu0 * d / Wd) * (eps0 * Wd / d)), c, "1/sqrt(LC) = c for the plate line")

print("=== N. Figure arrow checks (screen frame: X right, Y up, Z out)")
# drawing frame of figs_l19 sheet figures: physics x -> screen up (0,1,0), physics y -> out of screen (0,0,1), physics z -> right (1,0,0)
P = {"x": np.array([0, 1, 0.]), "y": np.array([0, 0, 1.]), "z": np.array([1, 0, 0.])}
# notes' J_s = +x J_x: current arrows UP. E = -x: arrow DOWN on both sides.
# z>0: H = -y -> into the screen (otimes); z<0: H = +y -> out (odot)
close(0.5 * cr(P["x"], P["z"]), -0.5 * P["y"], "fig radiated-fields: z>0 H = 1/2 J x n -> into screen (otimes)")
close(0.5 * cr(P["x"], -P["z"]), 0.5 * P["y"], "fig radiated-fields: z<0 H -> out of screen (odot)")
close(cr(-P["x"], -P["y"]), P["z"], "fig radiated-fields: right side E x H = (down) x (in) = right")
close(cr(-P["x"], P["y"]), -P["z"], "fig radiated-fields: left side E x H = (down) x (out) = left")
# problem figure frame: physics x -> right, physics y -> up, physics z -> out of the screen
Q = {"x": np.array([1, 0, 0.]), "y": np.array([0, 1, 0.]), "z": np.array([0, 0, 1.])}
close(0.5 * cr(Q["y"], Q["x"]), -0.5 * Q["z"], "fig problem: x>0 H for J_s > 0 -> into the screen (otimes)")
close(0.5 * cr(Q["y"], -Q["x"]), 0.5 * Q["z"], "fig problem: x<0 H -> out of the screen (odot)")
close(cr(-Q["y"], -Q["z"]), Q["x"], "fig problem: x>0 E (down) x H (in) = right")
print("=== O. Extra spot checks quoted on the pages")
close([H4(700, 2.0), E4(700, 2.0)], [1/3, 40*np.pi], "Ex.4 spot check z = 700 m: H_y = 1/3 A/m, E_x = 40 pi V/m", rtol=1e-6)
close(cr(X, Y), Z, "Ex.4 spot check: x cross y = +z, away from sheet")
close(eta / 2 * 9, 847.6, "problem (e): sheet gives eta/2 J^2 = 848 W/m^2 at t' = 1 ns", rtol=1e-3)
close(eta / 2 * 9 / 2, eta * 9 / 4, "problem (e): half of it per wave")
close(float(Ey(0.75, 6)), -282.5, "problem (c) spot check E_y(0.75 m, 6 ns) = -283 V/m", rtol=1e-3)
close(0.3 * 6, 1.8, "variant: vacuum front at 1.8 m at 6 ns")
close(eta / 2, 94.18, "eta/2 = 94.2 ohm (eps_r = 4)", rtol=1e-3)
print(f"\nALL {ok_count} CHECKS PASSED")
