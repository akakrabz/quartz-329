#!/usr/bin/env python3
"""Numerical verification for content-src/practice/04-divergence-and-curl.md (Lecture 4).

numpy/scipy only.  Divergences and curls are checked by central finite differences of
Cartesian components (curvilinear fields are converted to Cartesian first and the result
is projected back onto the local unit vectors); every flux, volume and line integral is
recomputed with scipy.integrate.  Every number that appears on the page is printed here.
"""
import numpy as np
from scipy import integrate

EPS0 = 8.8541878128e-12
MU0 = 4e-7 * np.pi
rng = np.random.default_rng(329)
FAIL = []


def ok(label, got, want, rtol=1e-6, atol=1e-9):
    got = np.asarray(got, float)
    want = np.asarray(want, float)
    good = np.allclose(got, want, rtol=rtol, atol=atol)
    if not good:
        FAIL.append(label)
    g = np.array2string(got, precision=6) if got.ndim else f"{float(got):.6g}"
    w = np.array2string(want, precision=6) if want.ndim else f"{float(want):.6g}"
    print(f"  [{'OK' if good else 'FAIL'}] {label}: numeric {g}  vs  closed form {w}")


# ---------------------------------------------------------------- finite-difference operators
def jac(F, p, h):
    p = np.asarray(p, float)
    J = np.zeros((3, 3))
    for j in range(3):
        e = np.zeros(3)
        e[j] = h
        J[:, j] = (np.asarray(F(p + e), float) - np.asarray(F(p - e), float)) / (2 * h)
    return J


def div(F, p, h=1e-6):
    return np.trace(jac(F, p, h))


def curl(F, p, h=1e-6):
    J = jac(F, p, h)
    return np.array([J[2, 1] - J[1, 2], J[0, 2] - J[2, 0], J[1, 0] - J[0, 1]])


def cyl_basis(p):
    x, y, _ = p
    r = np.hypot(x, y)
    return r, np.array([x / r, y / r, 0.0]), np.array([-y / r, x / r, 0.0]), np.array([0.0, 0.0, 1.0])


def sph_basis(p):
    x, y, z = p
    r = np.linalg.norm(p)
    th = np.arccos(z / r)
    ph = np.arctan2(y, x)
    rh = np.asarray(p, float) / r
    thh = np.array([np.cos(th) * np.cos(ph), np.cos(th) * np.sin(ph), -np.sin(th)])
    phh = np.array([-np.sin(ph), np.cos(ph), 0.0])
    return r, th, ph, rh, thh, phh


def line_int(F, A, B):
    A = np.asarray(A, float)
    B = np.asarray(B, float)
    d = B - A
    return integrate.quad(lambda t: np.dot(F(A + t * d), d), 0, 1, epsabs=1e-13, epsrel=1e-12)[0]


def path_int(F, pts):
    return sum(line_int(F, pts[i], pts[i + 1]) for i in range(len(pts) - 1))


def sample_points(n, lo, hi):
    return rng.uniform(lo, hi, (n, 3))


# ============================================================== 4.1
print("=== 4.1 Faucet or whirlpool")
E1 = lambda p: np.array([3 * p[0], -p[1], 2 * p[2]])
E2 = lambda p: np.array([2 * p[1], -3 * p[0], 0.0])
for p in sample_points(3, -2, 2):
    ok(f"div E1 at {np.round(p, 2)}", div(E1, p), 4.0)
    ok(f"curl E1 at {np.round(p, 2)}", curl(E1, p), [0, 0, 0])
    ok(f"div E2 at {np.round(p, 2)}", div(E2, p), 0.0)
    ok(f"curl E2 at {np.round(p, 2)}", curl(E2, p), [0, 0, -5])
print(f"  rho for E1 = 4 eps0 = {4 * EPS0:.4e} C/m^3  (page: 3.54e-11)")
print("  E2 at (0,1,0) =", E2(np.array([0, 1, 0.0])), " (page: +2 x-hat);  E2 at (1,0,0) =", E2(np.array([1, 0, 0.0])), " (page: -3 y-hat)")
R = 1e-3
circ = integrate.quad(lambda t: np.dot(E2(np.array([R * np.cos(t), R * np.sin(t), 0])),
                                       np.array([-R * np.sin(t), R * np.cos(t), 0])), 0, 2 * np.pi)[0]
ok("E2 circulation per unit area around a small CCW (from +z) circle", circ / (np.pi * R ** 2), -5.0)
print("  -> negative circulation for CCW travel: the wheel turns CLOCKWISE seen from +z")

# ============================================================== 4.2
print("\n=== 4.2 Curl-free but not charge-free (MC)")
E = lambda p: np.array([p[2] ** 2 + 2 * p[1], 2 * p[0] - 3, 2 * p[0] * p[2]])
for p in sample_points(4, -3, 3):
    ok(f"curl E at {np.round(p, 2)}", curl(E, p), [0, 0, 0], atol=1e-7)
    ok(f"div E at {np.round(p, 2)} (=2x)", div(E, p), 2 * p[0], atol=1e-7)
print(f"  rho = 2 eps0 x; e.g. at x = 1 m: {2 * EPS0:.4e} C/m^3; zero only on x = 0  -> (d) FALSE")
straight = line_int(E, [0, 0, 0], [1, 2, 3])
stair = path_int(E, [[0, 0, 0], [1, 0, 0], [1, 2, 0], [1, 2, 3]])
stair2 = path_int(E, [[0, 0, 0], [0, 0, 3], [0, 2, 3], [1, 2, 3]])
ok("line integral (0,0,0)->(1,2,3), straight line", straight, 7.0)
ok("line integral, staircase x then y then z", stair, 7.0)
ok("line integral, staircase z then y then x", stair2, 7.0)
ok("  staircase legs (x, then y, then z)", [line_int(E, [0, 0, 0], [1, 0, 0]), line_int(E, [1, 0, 0], [1, 2, 0]),
                                          line_int(E, [1, 2, 0], [1, 2, 3])], [0.0, -2.0, 9.0])
# a scalar f with E = -grad f (covers the identity curl grad f = 0)
f42 = lambda p: -(p[0] * p[2] ** 2 + 2 * p[0] * p[1] - 3 * p[1])


def grad(f, p, h=1e-6):
    p = np.asarray(p, float)
    return np.array([(f(p + h * e) - f(p - h * e)) / (2 * h) for e in np.eye(3)])


for p in sample_points(3, -3, 3):
    ok(f"-grad f = E at {np.round(p, 2)}, f = -(x z^2 + 2xy - 3y)", -grad(f42, p), E(p), atol=1e-7)
    ok("  curl(grad f) = 0 (nested finite differences)", curl(lambda q: grad(f42, q, 1e-4), p, 1e-4), [0, 0, 0], atol=1e-5)
print(f"  f(1,2,3) = {f42([1, 2, 3]):.6g}")
ok("f(O) - f(P) = line integral O->P", f42([0, 0, 0]) - f42([1, 2, 3]), 7.0)

# ============================================================== 4.3
print("\n=== 4.3 Along or across the flow (T/F)")
E0, a = 2.0, 0.5
Fa = lambda p: np.array([E0 * np.exp(-p[1] / a), 0.0, 0.0])
for p in sample_points(3, -1, 1):
    ok(f"(a) div at {np.round(p, 2)}", div(Fa, p), 0.0)
    ok(f"(b) curl at {np.round(p, 2)}", curl(Fa, p), [0, 0, E0 / a * np.exp(-p[1] / a)])
print("  (b) curl_z > 0 -> paddlewheel turns counter-clockwise seen from +z")
coul = lambda p: np.asarray(p) / np.linalg.norm(p) ** 3            # Q/(4 pi eps0) = 1
for p in sample_points(3, 0.3, 2):
    ok(f"(c) Coulomb div at r = {np.linalg.norm(p):.3f}", div(coul, p, 1e-6), 0.0, atol=1e-6)
k = 1.7
vort = lambda p: k * np.array([-p[1], p[0], 0.0]) / (p[0] ** 2 + p[1] ** 2)
for p in sample_points(3, 0.3, 2):
    ok(f"(d) free-vortex curl at {np.round(p, 2)}", curl(vort, p), [0, 0, 0], atol=1e-6)
Rc = 0.8
circv = integrate.quad(lambda t: np.dot(vort(np.array([Rc * np.cos(t), Rc * np.sin(t), 0])),
                                        np.array([-Rc * np.sin(t), Rc * np.cos(t), 0])), 0, 2 * np.pi)[0]
ok("(d) circulation around a circle enclosing the axis = 2 pi k", circv, 2 * np.pi * k)

# ============================================================== 4.4
print("\n=== 4.4 The missing metric factor (find the error)")
D0, a = 6e-6, 0.03
Dcyl = lambda p: D0 * np.hypot(p[0], p[1]) * np.array([p[0], p[1], 0.0]) / a ** 2   # D0 (r/a)^2 r-hat
for rr in [a / 2, 0.8 * a]:
    p = np.array([rr * np.cos(0.7), rr * np.sin(0.7), 0.3])
    ok(f"div D at r = {rr:.4f} m equals 3 D0 r / a^2", div(Dcyl, p, 1e-8), 3 * D0 * rr / a ** 2)
print(f"  student's rho(a/2) = 2 D0 (a/2)/a^2 = D0/a = {D0 / a * 1e6:.1f} uC/m^3 (page: 200)")
print(f"  correct   rho(a/2) = 3 D0/(2a)          = {3 * D0 / (2 * a) * 1e6:.1f} uC/m^3 (page: 300)")
rr, L = 0.6 * a, 1.0
flux = (D0 * rr ** 2 / a ** 2) * 2 * np.pi * rr * L
qc = integrate.quad(lambda s: 3 * D0 * s / a ** 2 * 2 * np.pi * s * L, 0, rr)[0]
qs = integrate.quad(lambda s: 2 * D0 * s / a ** 2 * 2 * np.pi * s * L, 0, rr)[0]
ok("Gauss: flux 2 pi L D0 r^3/a^2 = charge from 3 D0 r/a^2", qc, flux)
ok("student's rho encloses (4 pi/3) L D0 r^3/a^2 = 2/3 of the flux", qs / flux, 2 / 3)

# ============================================================== 4.5
print("\n=== 4.5 Draining a cube (continuity)")
J = lambda p: np.array([4 * p[0], 2 * p[1], -p[2]])
for p in sample_points(2, -1, 1):
    ok(f"div J at {np.round(p, 2)} -> d rho/dt = -5", -div(J, p), -5.0)
s = 0.5
vol = integrate.tplquad(lambda z, y, x: -div(J, [x, y, z]), 0, s, 0, s, 0, s)[0]
ok("dQ/dt = integral of d rho/dt over the cube [A]", vol, -0.625)
faces = {}
faces["x=0.5 (+x)"] = integrate.dblquad(lambda z, y: J([s, y, z])[0], 0, s, 0, s)[0]
faces["x=0 (-x)"] = integrate.dblquad(lambda z, y: -J([0, y, z])[0], 0, s, 0, s)[0]
faces["y=0.5 (+y)"] = integrate.dblquad(lambda z, x: J([x, s, z])[1], 0, s, 0, s)[0]
faces["y=0 (-y)"] = integrate.dblquad(lambda z, x: -J([x, 0, z])[1], 0, s, 0, s)[0]
faces["z=0.5 (+z)"] = integrate.dblquad(lambda y, x: J([x, y, s])[2], 0, s, 0, s)[0]
faces["z=0 (-z)"] = integrate.dblquad(lambda y, x: -J([x, y, 0])[2], 0, s, 0, s)[0]
for kf, v in faces.items():
    print(f"  outward current through face {kf}: {v:+.4f} A")
print("  J_x(0.5)=", J([s, 0, 0])[0], " J_y(0.5)=", J([0, s, 0])[1], " J_z(0.5)=", J([0, 0, s])[2], " A/m^2; face area", s * s, "m^2; volume", s ** 3, "m^3")
ok("net outward current = -dQ/dt", sum(faces.values()), 0.625)

# ============================================================== 4.6
print("\n=== 4.6 Three fields in curved coordinates")
E0, a = 5.0, 0.1


def E1c(p):
    r, rh, phh, zh = cyl_basis(p)
    return E0 * r / a * phh


def E2s(p):
    r, th, ph, rh, thh, phh = sph_basis(p)
    return E0 * a ** 2 / r ** 2 * np.cos(th) * rh


def E3s(p):
    r, th, ph, rh, thh, phh = sph_basis(p)
    return E0 * (a ** 3 / r ** 3 * (2 * np.cos(th) * rh + np.sin(th) * thh) + r / a * rh)


def E3cart(p):          # same field written as dipole (3 z r/r^5 - z-hat/r^3) + ball (r/a)
    p = np.asarray(p, float)
    r = np.linalg.norm(p)
    return E0 * (a ** 3 * (3 * p[2] * p / r ** 5 - np.array([0, 0, 1.0]) / r ** 3) + p / a)


for p in [np.array([0.03, -0.05, 0.04]), np.array([-0.02, 0.06, -0.01])]:
    ok(f"(a) curl E1 at {p}", curl(E1c, p, 1e-7), [0, 0, 2 * E0 / a], atol=1e-5)
    ok(f"(a) div E1 at {p}", div(E1c, p, 1e-7), 0.0, atol=1e-5)
    r, th, ph, rh, thh, phh = sph_basis(p)
    c2 = curl(E2s, p, 1e-8)
    ok(f"(b) div E2 at r={r:.3f}", div(E2s, p, 1e-8), 0.0, atol=1e-4)
    ok(f"(b) curl E2 . phi-hat = E0 a^2 sin(th)/r^3", np.dot(c2, phh), E0 * a ** 2 * np.sin(th) / r ** 3, rtol=1e-5)
    ok("(b) curl E2 has no r, theta parts", [np.dot(c2, rh), np.dot(c2, thh)], [0, 0], atol=1e-3)
    ok("(c) E3 spherical form = Cartesian dipole + ball form", E3s(p), E3cart(p))
    ok(f"(c) curl E3 at r={r:.3f}", curl(E3s, p, 1e-8), [0, 0, 0], atol=1e-3)
    ok(f"(c) div E3 at r={r:.3f} = 3 E0/a", div(E3s, p, 1e-8), 3 * E0 / a, rtol=1e-5)
print(f"  (d) rho = 3 eps0 E0/a = {3 * E0 / a:.0f} eps0 = {3 * EPS0 * E0 / a:.4e} C/m^3 (page: 150 eps0 ~ 1.33 nC/m^3)")
qflux = integrate.quad(lambda th: EPS0 * (E0 * a ** 3 / (0.07) ** 3 * 2 * np.cos(th) + E0 * 0.07 / a) * 2 * np.pi * 0.07 ** 2 * np.sin(th), 0, np.pi)[0]
ok("(c) check: eps0 * flux of E3 through r=0.07 m = rho * (4/3) pi r^3", qflux, 3 * EPS0 * E0 / a * 4 / 3 * np.pi * 0.07 ** 3)

# ============================================================== 4.7
print("\n=== 4.7 Divergence theorem on a hemisphere")
D0, a = 6e-6, 0.5
Dh = lambda p: D0 * np.array([p[0] / a, 0.0, 1.0])
ok("div D = D0/a [C/m^3]", div(Dh, [0.1, 0.2, 0.3]), D0 / a)
print(f"  D0/a = {D0 / a * 1e6:.1f} uC/m^3; hemisphere volume 2 pi a^3/3 = {2 * np.pi * a ** 3 / 3:.4f} m^3")
volint = integrate.tplquad(lambda r, th, ph: div(Dh, [r * np.sin(th) * np.cos(ph), r * np.sin(th) * np.sin(ph), r * np.cos(th)]) * r ** 2 * np.sin(th),
                           0, 2 * np.pi, 0, np.pi / 2, 0, a)[0]
ok("volume integral of div D = 2 pi a^2 D0/3", volint, 2 * np.pi * a ** 2 * D0 / 3, rtol=1e-6, atol=1e-14)


def dome_integrand(th, ph, part):
    rh = np.array([np.sin(th) * np.cos(ph), np.sin(th) * np.sin(ph), np.cos(th)])
    p = a * rh
    Dv = {"all": Dh(p), "x": np.array([D0 * p[0] / a, 0, 0]), "z": np.array([0, 0, D0])}[part]
    return np.dot(Dv, rh) * a ** 2 * np.sin(th)


dome = integrate.dblquad(lambda th, ph: dome_integrand(th, ph, "all"), 0, 2 * np.pi, 0, np.pi / 2)[0]
dome_x = integrate.dblquad(lambda th, ph: dome_integrand(th, ph, "x"), 0, 2 * np.pi, 0, np.pi / 2)[0]
dome_z = integrate.dblquad(lambda th, ph: dome_integrand(th, ph, "z"), 0, 2 * np.pi, 0, np.pi / 2)[0]
base = integrate.dblquad(lambda r, ph: np.dot(Dh([r * np.cos(ph), r * np.sin(ph), 0]), [0, 0, -1]) * r, 0, 2 * np.pi, 0, a)[0]
ok("dome flux = (2 pi/3 + pi) a^2 D0 = 5 pi a^2 D0/3", dome, 5 * np.pi * a ** 2 * D0 / 3, atol=1e-14)
ok("  x-part through dome = 2 pi a^2 D0/3", dome_x, 2 * np.pi * a ** 2 * D0 / 3, atol=1e-14)
ok("  uniform z-part through dome = pi a^2 D0", dome_z, np.pi * a ** 2 * D0, atol=1e-14)
ok("base flux = -pi a^2 D0", base, -np.pi * a ** 2 * D0, atol=1e-14)
ok("closed-surface flux = volume integral", dome + base, volint, atol=1e-14)
print(f"  dome {dome * 1e6:.3f} uC, base {base * 1e6:.3f} uC, total Q {(dome + base) * 1e6:.4f} uC = pi uC = {np.pi:.4f} uC")
print(f"  rho * volume = {D0 / a * 2 * np.pi * a ** 3 / 3 * 1e6:.4f} uC")

# ============================================================== 4.8
print("\n=== 4.8 Circulation from a given curl (SP18 Exam 1 #2 style; vector changed from the exam's (2,-3,5) to (3,2,-4))")
P1, P2, P3, P4 = [0, 0, 0], [0, 0, 2], [0, 3, 2], [0, 3, 0]
Om = np.array([3.0, 2.0, -4.0])
Eu = lambda p: Om
ok("(a) uniform E: loop integral", path_int(Eu, [P1, P2, P3, P4, P1]), 0.0)
ok("(a) leg P1->P2", line_int(Eu, P1, P2), -8.0)
ok("(a) leg P2->P3", line_int(Eu, P2, P3), 6.0)
ok("(a) P1->P2->P3 total = E.(P3-P1)", path_int(Eu, [P1, P2, P3]), np.dot(Om, np.subtract(P3, P1)))
ok("(a) P1->P2->P3 total = -2 V", path_int(Eu, [P1, P2, P3]), -2.0)
ok("(a) P1->P4->P3 total = -2 V", path_int(Eu, [P1, P4, P3]), -2.0)
n = np.cross(np.subtract(P2, P1), np.subtract(P3, P2))
n = n / np.linalg.norm(n)
print("  normal from right-hand rule (leg1 x leg2):", n, " (page: -x-hat);  area =", 3 * 2, "m^2")
ok("(b) circulation = (curl . n) A", np.dot(Om, n) * 6, -18.0)
print("  (b) dB/dt = -curl E =", -Om, "T/s")
Ed = lambda p: np.array([2 * p[2], -4 * p[0], 3 * p[1]])      # (W_y z, W_z x, W_x y)
for p in sample_points(2, -2, 2):
    ok(f"(d) curl of 2z x - 4x y + 3y z at {np.round(p, 2)}", curl(Ed, p), Om)
legs = [line_int(Ed, P1, P2), line_int(Ed, P2, P3), line_int(Ed, P3, P4), line_int(Ed, P4, P1)]
ok("(d) the four legs P1P2, P2P3, P3P4, P4P1", legs, [0, 0, -18, 0])
via2 = path_int(Ed, [P1, P2, P3])
via4 = path_int(Ed, [P1, P4, P3])
ok("(d) route via P2", via2, 0.0)
ok("(d) route via P4", via4, 18.0)
ok("(c),(d) via P2 minus via P4 = loop integral", via2 - via4, -18.0)
surf = integrate.dblquad(lambda z, y: np.dot(curl(Ed, [0, y, z]), n), 0, 3, 0, 2)[0]
ok("(d) Stokes: flux of curl Ed through the rectangle (normal -x-hat)", surf, -18.0)

# ============================================================== 4.9
print("\n=== 4.9 Electrostatic or not (Summer HE1 #2 style)")
E1 = lambda p: np.array([0.0, 3 * np.cos(np.pi * p[1] / 2), 0.0])
E2 = lambda p: np.array([0.0, 2 * np.cos(np.pi * p[0] / 2), 0.0])
Et = lambda p: E1(p) + E2(p)
for p in sample_points(3, -2, 2):
    ok(f"(a) curl E1 at {np.round(p, 2)}", curl(E1, p), [0, 0, 0])
    ok(f"(a) curl E2 at {np.round(p, 2)}", curl(E2, p), [0, 0, -np.pi * np.sin(np.pi * p[0] / 2)])
    ok(f"(b) div E at {np.round(p, 2)}", div(Et, p), -1.5 * np.pi * np.sin(np.pi * p[1] / 2))
ys = np.linspace(-4, 4, 80001)
xs = ys
dmax = np.max(np.abs(-1.5 * np.pi * np.sin(np.pi * ys / 2)))
cmax = np.max(np.abs(np.pi * np.sin(np.pi * xs / 2)))
ok("(b) max |div E| = 3 pi/2 [V/m^2]", dmax, 1.5 * np.pi)
print(f"  (b) 3 pi/2 = {1.5 * np.pi:.4f} V/m^2;  max |rho| = (3 pi/2) eps0 = {1.5 * np.pi * EPS0:.4e} C/m^3; attained at y =", ys[np.argmax(np.abs(np.sin(np.pi * ys / 2)))], "(odd integers)")
for yy in [1.0, 3.0, -1.0]:
    print(f"  (b) rho on the plane y = {yy:+.0f} m: {EPS0 * div(Et, [0.2, yy, 0.0]):+.4e} C/m^3")
ok("(c) max |curl E| = pi [V/m^2]", cmax, np.pi)
print(f"  (c) pi = {np.pi:.4f} V/m^2 at x = odd integers; check |curl| at x=1:", abs(curl(Et, [1, 0.3, 0])[2]))
O, P = [0, 0, 0], [1, 1, 0]
rA = path_int(E2, [O, [1, 0, 0], P])
rB = path_int(E2, [O, [0, 1, 0], P])
ok("(d) route A for E2", rA, 0.0)
ok("(d) route B for E2", rB, 2.0)
stokes = integrate.dblquad(lambda y, x: curl(E2, [x, y, 0])[2], 0, 1, 0, 1)[0]
ok("(d) flux of curl E2 through unit square (+z) = A - B", stokes, rA - rB)
ok("(d) closed form -pi * 2/pi = -2", stokes, -2.0, rtol=1e-6)
x0 = 2 / 3
ok("(e) staircase climbing at x0 = 2/3 m gives 1 V", path_int(E2, [O, [x0, 0, 0], [x0, 1, 0], P]), 1.0)
ok("(e) straight diagonal gives 4/pi", line_int(E2, O, P), 4 / np.pi)
print(f"  4/pi = {4 / np.pi:.4f} V")
ok("(e) E1 along route A = 6/pi", path_int(E1, [O, [1, 0, 0], P]), 6 / np.pi)
ok("(e) E1 along route B = 6/pi", path_int(E1, [O, [0, 1, 0], P]), 6 / np.pi)
print(f"  6/pi = {6 / np.pi:.4f} V")

# ============================================================== 4.10
print("\n=== 4.10 Charge layers from a piecewise D")
D0, a = 2e-6, 0.1


def Dr(r):
    if r < a:
        return D0 * r ** 2 / a ** 2
    if r < 2 * a:
        return -2 * D0 * a ** 2 / r ** 2
    return 0.0


Dv = lambda p: Dr(np.linalg.norm(p)) * np.asarray(p, float) / np.linalg.norm(p)
for rr in [0.5 * a, 0.9 * a]:
    p = rr * np.array([0.48, -0.6, 0.64])
    ok(f"(a) div D at r = {rr / a:.1f} a  = 4 D0 r/a^2", div(Dv, p, 1e-8), 4 * D0 * rr / a ** 2, rtol=1e-5)
    ok(f"     curl D at r = {rr / a:.1f} a", curl(Dv, p, 1e-8), [0, 0, 0], atol=1e-9)
for rr in [1.3 * a, 1.8 * a, 2.5 * a]:
    p = rr * np.array([0.48, -0.6, 0.64])
    ok(f"(a) div D at r = {rr / a:.1f} a  = 0", div(Dv, p, 1e-8), 0.0, atol=1e-9)
    ok(f"     curl D at r = {rr / a:.1f} a", curl(Dv, p, 1e-8), [0, 0, 0], atol=1e-9)
print(f"  rho(a/2) = 2 D0/a = {2 * D0 / a * 1e6:.1f} uC/m^3;  rho(a) = 4 D0/a = {4 * D0 / a * 1e6:.1f} uC/m^3")
for delta in [1e-3, 1e-5]:
    shell_flux = 4 * np.pi * ((a + delta) ** 2 * Dr(a + delta) - (a - delta) ** 2 * Dr(a - delta))
    print(f"  thin-shell flux at r=a, delta={delta}: {shell_flux:.6e} C  -> 4 pi a^2 rho_s with rho_s = {shell_flux / (4 * np.pi * a ** 2) * 1e6:.4f} uC/m^2")
ok("(b) rho_s(a) = D(a+) - D(a-) = -3 D0", Dr(a * (1 + 1e-12)) - Dr(a * (1 - 1e-12)), -3 * D0, rtol=1e-6, atol=1e-15)
ok("(b) rho_s(2a) = D(2a+) - D(2a-) = D0/2", Dr(2 * a * (1 + 1e-12)) - Dr(2 * a * (1 - 1e-12)), D0 / 2, rtol=1e-6, atol=1e-15)
print(f"  rho_s(a) = {-3 * D0 * 1e6:.1f} uC/m^2, rho_s(2a) = {D0 / 2 * 1e6:+.1f} uC/m^2")
Qcore = integrate.quad(lambda r: 4 * D0 * r / a ** 2 * 4 * np.pi * r ** 2, 0, a)[0]
Qa = 4 * np.pi * a ** 2 * (-3 * D0)
Q2a = 4 * np.pi * (2 * a) ** 2 * (D0 / 2)
ok("(c) Q_core = 4 pi a^2 D0", Qcore, 4 * np.pi * a ** 2 * D0, atol=1e-18)
print(f"  4 pi a^2 D0 = {4 * np.pi * a ** 2 * D0:.4e} C = 8 pi x 1e-8 = {8 * np.pi * 1e-8:.4e}")
print(f"  Q_core = {Qcore * 1e6:+.4f} uC, Q_a = {Qa * 1e6:+.4f} uC, Q_2a = {Q2a * 1e6:+.4f} uC, total = {(Qcore + Qa + Q2a) * 1e6:+.2e} uC")
ok("(c) total charge zero", Qcore + Qa + Q2a, 0.0, atol=1e-18)
rs = 1.5 * a
fl = integrate.dblquad(lambda th, ph: np.dot(Dv(rs * np.array([np.sin(th) * np.cos(ph), np.sin(th) * np.sin(ph), np.cos(th)])),
                                             [np.sin(th) * np.cos(ph), np.sin(th) * np.sin(ph), np.cos(th)]) * rs ** 2 * np.sin(th),
                       0, 2 * np.pi, 0, np.pi)[0]
ok("(d) flux through r = 1.5 a = -8 pi a^2 D0", fl, -8 * np.pi * a ** 2 * D0, atol=1e-18)
ok("(d) = enclosed charge Q_core + Q_a", fl, Qcore + Qa, atol=1e-18)
print(f"  flux at 1.5a = {fl * 1e6:.4f} uC")

# ============================================================== 4.11
print("\n=== 4.11 An expanding ion cloud (continuity)")
a, rho0, tau = 0.01, 3e-6, 2e-3
rho = lambda t: rho0 * np.exp(-3 * t / tau)
Rt = lambda t: a * np.exp(t / tau)
Jf = lambda p, t: rho(t) * np.asarray(p, float) / tau          # rho v, v = r/tau r-hat (inside the cloud)
for t in [0.3e-3, 1.0e-3]:
    for p in [np.array([0.002, -0.004, 0.003]), np.array([-0.006, 0.001, 0.005])]:
        dJ = div(lambda q: Jf(q, t), p, 1e-7)
        drho = (rho(t + 1e-9) - rho(t - 1e-9)) / 2e-9
        ok(f"(a) continuity div J + d rho/dt = 0 at t={t * 1e3:.1f} ms", dJ + drho, 0.0, atol=1e-9)
        ok("    div J = 3 rho/tau", dJ, 3 * rho(t) / tau)
Q0 = 4 / 3 * np.pi * a ** 3 * rho0
print(f"  Q0 = (4/3) pi a^3 rho0 = {Q0:.4e} C = 4 pi pC = {4 * np.pi:.3f} pC")
for t in [0, 0.5e-3, 3e-3]:
    ok(f"(a) cloud charge rho(t)(4/3)pi R(t)^3 at t={t * 1e3:.1f} ms", rho(t) * 4 / 3 * np.pi * Rt(t) ** 3, Q0, atol=1e-20)
# Monte-Carlo check that the uniform-expansion map keeps the density uniform: push ions r -> r e^{t/tau}
N = 400000
u = rng.normal(size=(N, 3))
u /= np.linalg.norm(u, axis=1)[:, None]
rr0 = a * rng.uniform(0, 1, N) ** (1 / 3)
th = tau * np.log(2) / 3
frac = np.mean(rr0 * np.exp(th / tau) < a)
print(f"  Monte Carlo: fraction of ions inside r=a at t = (tau/3) ln2: {frac:.4f} (expect 0.5)")
if abs(frac - 0.5) > 0.005:
    FAIL.append("MC half")
Qa = lambda t: rho(t) * 4 / 3 * np.pi * a ** 3
I_out = lambda t: integrate.dblquad(lambda th_, ph: np.dot(Jf(a * np.array([np.sin(th_) * np.cos(ph), np.sin(th_) * np.sin(ph), np.cos(th_)]), t),
                                                           [np.sin(th_) * np.cos(ph), np.sin(th_) * np.sin(ph), np.cos(th_)]) * a ** 2 * np.sin(th_),
                                    0, 2 * np.pi, 0, np.pi)[0]
for t in [0.0, 1e-3]:
    dQ = (Qa(t + 1e-9) - Qa(max(t - 1e-9, 0))) / (1e-9 + min(t, 1e-9))
    ok(f"(b) dQ_a/dt (finite diff) = -outward current at t={t * 1e3:.1f} ms", dQ, -I_out(t), rtol=1e-5, atol=1e-20)
    ok("    outward current = 3 Q0/tau e^{-3t/tau}", I_out(t), 3 * Q0 / tau * np.exp(-3 * t / tau), atol=1e-20)
print(f"  I(0+) = 3 Q0/tau = {3 * Q0 / tau:.4e} A = 6 pi nA = {6 * np.pi:.2f} nA")
print(f"  J_r(a, 0+) = rho0 a/tau = {rho0 * a / tau:.3e} A/m^2 (page: 15 uA/m^2)")
thalf = tau / 3 * np.log(2)
ok("(c) Q_a(t_half) = Q0/2", Qa(thalf), Q0 / 2, atol=1e-20)
print(f"  t_half = (tau/3) ln 2 = {thalf * 1e3:.4f} ms;  R(t_half) = a 2^(1/3) = {Rt(thalf) * 100:.4f} cm")
# (d) D inside from Gauss, J + dD/dt = 0
for t in [0.2e-3, 1.5e-3]:
    for rr in [0.3 * a, 0.9 * a]:
        Qenc = integrate.quad(lambda s: rho(t) * 4 * np.pi * s ** 2, 0, rr)[0]
        Dr_g = Qenc / (4 * np.pi * rr ** 2)
        ok(f"(d) Gauss D_r = rho r/3 at r={rr / a:.1f}a, t={t * 1e3:.1f} ms", Dr_g, rho(t) * rr / 3, atol=1e-20)
        dDdt = (rho(t + 1e-9) - rho(t - 1e-9)) / 2e-9 * rr / 3
        ok("    J_r + dD_r/dt = 0", rho(t) * rr / tau + dDdt, 0.0, atol=1e-12)
    rout = 2.5 * Rt(t)
    print(f"  outside the cloud at t={t * 1e3:.1f} ms, r={rout:.4f} m: D_r = Q0/(4 pi r^2) = {Q0 / (4 * np.pi * rout ** 2):.4e}, time-independent, J = 0")

# ============================================================== 4.12
print("\n=== 4.12 Inside a current-carrying rod")
H0, a = 400.0, 0.02


def Hf(p):
    r, rh, phh, zh = cyl_basis(p)
    return (H0 * r ** 3 / a ** 3 if r < a else H0 * a / r) * phh


for rr in [0.3 * a, 0.5 * a, 0.9 * a]:
    p = np.array([rr * np.cos(1.1), rr * np.sin(1.1), 0.004])
    ok(f"(a) curl H at r={rr / a:.1f} a = 4 H0 r^2/a^3 z-hat", curl(Hf, p, 1e-8), [0, 0, 4 * H0 * rr ** 2 / a ** 3], rtol=1e-5, atol=1e-2)
for rr in [1.5 * a, 3 * a]:
    p = np.array([rr * np.cos(-0.4), rr * np.sin(-0.4), -0.01])
    ok(f"(a) curl H at r={rr / a:.1f} a = 0", curl(Hf, p, 1e-8), [0, 0, 0], atol=1e-2)
Jnum = lambda p: curl(Hf, p, 1e-7)
for p in [np.array([0.004, 0.006, 0.0]), np.array([-0.009, 0.003, 0.01])]:
    ok(f"(a) div(curl H) at {p} (nested finite differences)", div(Jnum, p, 1e-5), 0.0, atol=5.0)
print(f"  (scale for the last check: J itself ~ {4 * H0 / a:.0f} A/m^2, its r-derivative ~ {8 * H0 / a ** 2:.0f} A/m^3)")
print(f"  J(r=a) = 4 H0/a = {4 * H0 / a:.3e} A/m^2 (page: 8e4)")
Itot = integrate.quad(lambda r: 4 * H0 * r ** 2 / a ** 3 * 2 * np.pi * r, 0, a)[0]
ok("(b) total current = 2 pi a H0 = 16 pi A", Itot, 2 * np.pi * a * H0)
print(f"  I = {Itot:.4f} A = 16 pi = {16 * np.pi:.4f}")
ok("(b) direction: curl_z > 0 at r = a/2 (current along +z)", np.sign(curl(Hf, [a / 2, 0, 0], 1e-8)[2]), 1.0)
Rq = a / 2
circ_q = (line_int(Hf, [1e-12, 0, 0], [Rq, 0, 0])
          + integrate.quad(lambda t: np.dot(Hf(np.array([Rq * np.cos(t), Rq * np.sin(t), 0])), np.array([-Rq * np.sin(t), Rq * np.cos(t), 0])), 0, np.pi / 2)[0]
          + line_int(Hf, [0, Rq, 0], [0, 1e-12, 0]))
fluxJ = integrate.dblquad(lambda r, ph: curl(Hf, [r * np.cos(ph), r * np.sin(ph), 0], 1e-9)[2] * r, 0, np.pi / 2, 1e-9, Rq)[0]
ok("(c) MMF around quarter-disk boundary (R = a/2) = pi H0 a/32", circ_q, np.pi * H0 * a / 32)
ok("(c) flux of J through quarter disk", fluxJ, np.pi * H0 * a / 32, rtol=1e-5)
print(f"  pi H0 a/32 = {np.pi * H0 * a / 32:.4f} A = pi/4 = {np.pi / 4:.4f}")
circ_full = integrate.quad(lambda t: np.dot(Hf(np.array([a * 0.999999999 * np.cos(t), a * 0.999999999 * np.sin(t), 0])),
                                            np.array([-a * np.sin(t), a * np.cos(t), 0])), 0, np.pi / 2)[0]
ok("(c) quarter disk with full radius a: pi H0 a/2 = 4 pi = I/4", circ_full, Itot / 4, rtol=1e-6)
print(f"  4 pi = {4 * np.pi:.4f} A")
R2 = 2 * a
circ2 = integrate.quad(lambda t: np.dot(Hf(np.array([R2 * np.cos(t), R2 * np.sin(t), 0])), np.array([-R2 * np.sin(t), R2 * np.cos(t), 0])), 0, 2 * np.pi)[0]
ok("(d) MMF around circle r = 2a = I", circ2, Itot)
print(f"  MMF(2a) = {circ2:.4f} A")
g = lambda p: (0.7 + 0.2 * np.cos(np.arctan2(p[1], p[0]))) * np.array([p[0], p[1], 0.0]) / (p[0] ** 2 + p[1] ** 2)   # B_r = g(phi)/r
for p in [np.array([0.01, 0.02, 0.0]), np.array([-0.03, 0.005, 0.1])]:
    ok(f"(e) a B_r = g(phi)/r field is divergence-free off the axis at {p}", div(g, p, 1e-8), 0.0, atol=1e-5)
print("  (e) but |B_r| = g/r diverges as r -> 0, so finiteness on the axis forces g = 0, B_r = 0")

print("\n" + ("ALL CHECKS PASSED" if not FAIL else f"FAILED: {FAIL}"))
