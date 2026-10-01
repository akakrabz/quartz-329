#!/usr/bin/env python3
"""Verification script for practice/07-poisson-and-laplace.md (Lecture 7).

numpy/scipy only. For every potential on the page we check, numerically,
  * the ODE/PDE it must satisfy (Laplacian by central finite differences),
  * every boundary / matching value,
and every number, sign and direction quoted in an answer is printed here.
Where possible an independent route is used as well (solve_bvp / solve_ivp,
quad / dblquad superposition integrals, a finite-difference Poisson solve,
superposition of sheet fields).
"""
import numpy as np
from scipy.integrate import quad, dblquad, solve_bvp, solve_ivp
from scipy.optimize import minimize_scalar

eps0 = 8.8541878128e-12
e = 1.602176634e-19
me = 9.1093837e-31

NFAIL = 0
print(f"constants used: eps0 = {eps0:.4e} F/m, e = {e:.4e} C, me = {me:.4e} kg")


def check(label, got, want, rtol=1e-6, atol=0.0):
    global NFAIL
    ok = np.allclose(got, want, rtol=rtol, atol=atol)
    if not ok:
        NFAIL += 1
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}: got {np.array2string(np.asarray(got), precision=6)}"
          f"  want {np.array2string(np.asarray(want), precision=6)}")
    return ok


def show(label, val, unit=""):
    print(f"  {label} = {val:.6g} {unit}".rstrip())


# ---------- finite-difference helpers ----------
def d1(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)


def d2(f, x, h):
    return (f(x + h) - 2 * f(x) + f(x - h)) / h**2


def lap_cart(F, p, h):
    p = np.asarray(p, float)
    s = 0.0
    for i in range(3):
        dp = np.zeros(3); dp[i] = h
        s += (F(*(p + dp)) - 2 * F(*p) + F(*(p - dp))) / h**2
    return s


def grad_cart(F, p, h):
    p = np.asarray(p, float)
    g = np.zeros(3)
    for i in range(3):
        dp = np.zeros(3); dp[i] = h
        g[i] = (F(*(p + dp)) - F(*(p - dp))) / (2 * h)
    return g


def lap_sph_radial(V, r, h):
    """(1/r^2) d/dr (r^2 dV/dr) by nested central differences."""
    g = lambda s: s**2 * d1(V, s, h)
    return d1(g, r, h) / r**2


def lap_cyl_radial(V, r, h):
    g = lambda s: s * d1(V, s, h)
    return d1(g, r, h) / r


print("=" * 78)
print("7.1  Two plates, two potentials")
print("=" * 78)
V1 = lambda x: 9 - 3000 * x
d = 3e-3
check("V(0) [V]", V1(0), 9)
check("V(3 mm) [V]", V1(d), 0, atol=1e-12)
check("V(1 mm) [V]", V1(1e-3), 6)
for x in [0.5e-3, 1.7e-3, 2.9e-3]:
    check(f"V'' at x={x*1e3:.1f} mm (Laplace)", d2(V1, x, 1e-5), 0, atol=1e-6)
Ex = -d1(V1, 1e-3, 1e-6)
check("E_x [V/m] (= +3000, points +x: from 9 V plate to grounded plate)", Ex, 3000)
rs0 = +1 * eps0 * Ex      # n = +x at x = 0
rsd = -1 * eps0 * Ex      # n = -x at x = d
check("rho_s(x=0) [C/m^2]", rs0, 2.65626e-8, rtol=1e-5)
check("rho_s(x=3mm) [C/m^2]", rsd, -2.65626e-8, rtol=1e-5)
show("rho_s(x=0) in nC/m^2", rs0 * 1e9)
# independent: solve_bvp
sol = solve_bvp(lambda x, y: np.vstack([y[1], 0 * y[0]]),
                lambda ya, yb: np.array([ya[0] - 9, yb[0]]),
                np.linspace(0, d, 11), np.zeros((2, 11)))
check("solve_bvp V(1 mm)", sol.sol(1e-3)[0], 6, rtol=1e-6)
check("check: field of two sheets rho_s/eps0 [V/m]", rs0 / eps0, 3000)

print()
print("=" * 78)
print("7.2  Which potential needs charge (MC)")
print("=" * 78)
cands = {
    "(a) 3x^2-2y^2-z^2": lambda x, y, z: 3 * x**2 - 2 * y**2 - z**2,
    "(b) 5xyz": lambda x, y, z: 5 * x * y * z,
    "(c) x^2+y^2-z^2": lambda x, y, z: x**2 + y**2 - z**2,
    "(d) 4 ln r (cyl)": lambda x, y, z: 4 * np.log(np.sqrt(x**2 + y**2)),
    "(e) 2/r (sph)": lambda x, y, z: 2 / np.sqrt(x**2 + y**2 + z**2),
}
rng = np.random.default_rng(7)
pts_cyl = []
while len(pts_cyl) < 4:          # points with 1 < r_cyl < 2
    p = rng.uniform(-2, 2, 3)
    if 1.1 < np.hypot(p[0], p[1]) < 1.9:
        pts_cyl.append(p)
pts_sph = []
while len(pts_sph) < 4:          # points with r > 1
    p = rng.uniform(-3, 3, 3)
    if np.linalg.norm(p) > 1.2:
        pts_sph.append(p)
for name, F in cands.items():
    pts = pts_cyl if "cyl" in name else pts_sph
    laps = [lap_cart(F, p, 1e-3) for p in pts]
    print(f"  {name}: Laplacian at 4 points = {np.round(laps, 6)}")
check("(a) Laplacian", 6 - 4 - 2, 0)
check("(c) Laplacian [V/m^2]", lap_cart(cands["(c) x^2+y^2-z^2"], [0.3, -0.7, 1.1], 1e-3), 2, rtol=1e-6)
for k in ["(a) 3x^2-2y^2-z^2", "(b) 5xyz"]:
    check(f"{k} harmonic", lap_cart(cands[k], [0.4, 1.3, -0.8], 1e-3), 0, atol=1e-5)
check("(d) harmonic", lap_cart(cands["(d) 4 ln r (cyl)"], pts_cyl[0], 1e-3), 0, atol=1e-5)
check("(e) harmonic", lap_cart(cands["(e) 2/r (sph)"], pts_sph[0], 1e-3), 0, atol=1e-5)
rho_c = -eps0 * 2
check("(c) rho = -eps0*lap V [C/m^3]", rho_c, -1.77084e-11, rtol=1e-5)
check("cyl formula for (d): (1/r)(r V')' ", lap_cyl_radial(lambda r: 4 * np.log(r), 1.5, 1e-4), 0, atol=1e-6)
check("sph formula for (e): (1/r^2)(r^2 V')' ", lap_sph_radial(lambda r: 2 / r, 1.5, 1e-4), 0, atol=1e-6)
# individual second partials quoted in the solution
p0 = np.array([0.4, 1.3, -0.8])
for k in ["(a) 3x^2-2y^2-z^2", "(c) x^2+y^2-z^2"]:
    F = cands[k]
    parts = []
    for i in range(3):
        dp = np.zeros(3); dp[i] = 1e-3
        parts.append((F(*(p0 + dp)) - 2 * F(*p0) + F(*(p0 - dp))) / 1e-6)
    want = [6, -4, -2] if k.startswith("(a)") else [2, 2, -2]
    check(f"{k}: d2V/dx2, d2V/dy2, d2V/dz2", parts, want, rtol=1e-6)
# the trap: plain d2V/dr2 is NOT the Laplacian in cylindrical/spherical coordinates
for r in [1.2, 1.7]:
    check(f"(d) d2V/dr2 = -4/r^2 (nonzero, but not the Laplacian) at r={r}", d2(lambda s: 4 * np.log(s), r, 1e-4), -4 / r**2, rtol=1e-6)
    check(f"(e) d2V/dr2 = +4/r^3 (nonzero, but not the Laplacian) at r={r}", d2(lambda s: 2 / s, r, 1e-4), 4 / r**3, rtol=1e-6)

print()
print("=" * 78)
print("7.3  Find the error: concentric spheres")
print("=" * 78)
a, b, V0 = 0.01, 0.02, 100.0
A = V0 / (1 / a - 1 / b)
B = -A / b
check("A [V m]", A, 2.0)
check("B [V]", B, -100.0)
Vs = lambda r: A / r + B
check("V(a) [V]", Vs(a), 100)
check("V(b) [V]", Vs(b), 0, atol=1e-10)
for r in [0.012, 0.015, 0.019]:
    # FD Laplacian compared with the size of its individual terms, V'' = 2A/r^3
    # (an absolute tolerance is meaningless here: the terms are ~1e6 V/m^2)
    scale = 2 * A / r**3
    check(f"spherical Laplacian / (2A/r^3) at r={r}", lap_sph_radial(Vs, r, 1e-6) / scale, 0, atol=1e-6)
    F = lambda x, y, z: Vs(np.sqrt(x * x + y * y + z * z))
    check(f"3-D Cartesian Laplacian / (2A/r^3) at |r|={r}", lap_cart(F, [r / np.sqrt(3)] * 3, 1e-5) / scale, 0, atol=1e-5)
Er = lambda r: -d1(Vs, r, 1e-7)
check("E_r(a) [V/m] (outward)", Er(a), 20000, rtol=1e-6)
check("E_r(b) [V/m] (outward)", Er(b), 5000, rtol=1e-6)
check("r^2 E_r constant = A [V m]", [a**2 * Er(a), b**2 * Er(b), 0.015**2 * Er(0.015)], [2, 2, 2], rtol=1e-6)
check("student's uniform field = average (V(a)-V(b))/(b-a) [V/m]", (Vs(a) - Vs(b)) / (b - a), 10000)
check("true V(1.5 cm) [V]", Vs(0.015), 100 / 3, rtol=1e-9)
show("student's V(1.5 cm)", V0 * (b - 0.015) / (b - a), "V")
check("linear V fails spherical Laplace (nonzero): (1/r^2)(r^2 V')' at 1.5 cm",
      abs(lap_sph_radial(lambda r: V0 * (b - r) / (b - a), 0.015, 1e-6)) > 1e5, True)
show("  value of that Laplacian", lap_sph_radial(lambda r: V0 * (b - r) / (b - a), 0.015, 1e-6), "V/m^2")

print()
print("=" * 78)
print("7.4  Wedge between two plates")
print("=" * 78)
Vw = lambda x, y, z: (200 / np.pi) * np.arctan2(y, x)
check("V on phi=0 plate [V]", Vw(0.3, 0.0, 0), 0, atol=1e-12)
check("V on phi=pi/2 plate [V]", Vw(0.0, 0.3, 0), 100)
check("V at phi=pi/4 [V]", Vw(1, 1, 0), 50)
for p in [[0.05, 0.02, 0.1], [0.1, 0.1, -0.3], [0.02, 0.2, 0.0]]:
    check(f"Laplacian at {p}", lap_cart(Vw, p, 1e-5), 0, atol=1e-2)
r0, ph = 0.1, np.pi / 4
P = [r0 * np.cos(ph), r0 * np.sin(ph), 0]
E = -grad_cart(Vw, P, 1e-7)
check("|E| at r=10 cm [V/m] = 2000/pi", np.linalg.norm(E), 2000 / np.pi)
show("2000/pi", 2000 / np.pi, "V/m")
phihat = np.array([-np.sin(ph), np.cos(ph), 0])
check("E along -phi_hat (E.phihat/|E|)", E @ phihat / np.linalg.norm(E), -1)
check("E components (x,y) [V/m] = 450.16*(1,-1)", E[:2], [450.158, -450.158], rtol=1e-5)
# surface charge on phi=0 plate (n = +y) at r = 0.1 m, field just above the plate
Eplate0 = -grad_cart(Vw, [0.1, 1e-6, 0], 1e-8)
rs_w0 = eps0 * Eplate0[1]
check("rho_s on grounded plate at r=10 cm [C/m^2] = -200 eps0/(pi r)", rs_w0, -200 * eps0 / (np.pi * 0.1), rtol=1e-4)
show("  in nC/m^2", rs_w0 * 1e9)
Eplate1 = -grad_cart(Vw, [1e-6, 0.1, 0], 1e-8)
rs_w1 = eps0 * Eplate1[0]      # n = +x on the phi = pi/2 plate (gap is x>0)
check("rho_s on 100 V plate at r=10 cm [C/m^2] (positive)", rs_w1, 200 * eps0 / (np.pi * 0.1), rtol=1e-4)
check("arc check |E| * (pi r/2) = 100 V", np.linalg.norm(E) * np.pi * r0 / 2, 100)

print()
print("=" * 78)
print("7.5  Laplace's equation, true or false")
print("=" * 78)
# (The earlier draft of 7.5, a graded-epsilon multiple choice, duplicated practice 9.3 and was replaced.)
H1 = lambda x, y, z: 3 * x**2 - 2 * y**2 - z**2       # harmonic
H2 = lambda x, y, z: 5 * x * y * z                     # harmonic
pts5 = [[0.3, -0.2, 0.7], [1.1, 0.4, -0.5], [-0.6, 0.9, 0.2]]
# (a) TRUE: linear combination plus a constant is harmonic
Hc = lambda x, y, z: 3 * H1(x, y, z) - 2 * H2(x, y, z) + 7
for p in pts5:
    check(f"(a) lap(3V1 - 2V2 + 7) = 0 at {p}  -> TRUE", lap_cart(Hc, p, 1e-3), 0, atol=1e-5)
# (b) FALSE: lap(V^2) = 2 V lap V + 2|grad V|^2 = 2|E|^2, nonzero wherever E != 0
HH = lambda x, y, z: H1(x, y, z)**2
for p in pts5:
    g = grad_cart(H1, p, 1e-6)
    check(f"(b) lap(V1^2) = 2|grad V1|^2 = {2 * g @ g:.4f} (nonzero) at {p}  -> FALSE", lap_cart(HH, p, 1e-3), 2 * g @ g, rtol=1e-5)
check("(b) simplest counterexample: V = x is harmonic, lap(x^2) = 2 [V/m^2]", lap_cart(lambda x, y, z: x**2, [0.3, 0.1, 0.2], 1e-3), 2, rtol=1e-6)
# (c) FALSE: mean-value property -- the average of a harmonic V over any sphere equals the centre value,
#     so no interior point can lie below all its neighbours. With charge, average - centre = R^2 lap(V)/6
#     (the lecture's 'intuition' box: lap V measures average minus centre).


def sphere_avg(F, c, R):
    f = lambda th, ph: F(c[0] + R * np.sin(th) * np.cos(ph), c[1] + R * np.sin(th) * np.sin(ph),
                         c[2] + R * np.cos(th)) * np.sin(th)
    return dblquad(f, 0, 2 * np.pi, 0, np.pi, epsabs=0, epsrel=1e-11)[0] / (4 * np.pi)


Hsum = lambda x, y, z: H1(x, y, z) + H2(x, y, z) + 2 * x - y + 4
Pq = lambda x, y, z: x**2 + y**2 - z**2               # lap = 2: needs charge
for c, R in [([0.3, -0.2, 0.7], 0.5), ([1.1, 0.4, -0.5], 0.2)]:
    check(f"(c) harmonic: sphere average = centre value (c={c}, R={R})", sphere_avg(Hsum, c, R), Hsum(*c), rtol=1e-9)
    check(f"(c) with charge: average - centre = R^2 lap V / 6 (c={c}, R={R})", sphere_avg(Pq, c, R) - Pq(*c), R**2 * 2 / 6, rtol=1e-7)
# (c)/(d) maximum-minimum principle on the unit ball for random harmonic combinations:
#     extremes over the inner ball r <= 0.9 lie strictly inside the range of boundary values
rng5 = np.random.default_rng(329)
basis = [lambda x, y, z: x, lambda x, y, z: y, lambda x, y, z: z, lambda x, y, z: x * y, lambda x, y, z: y * z,
         lambda x, y, z: x**2 - y**2, H1, H2, lambda x, y, z: x**3 - 3 * x * y**2]
for trial in range(3):
    w = rng5.normal(size=len(basis))
    F = lambda x, y, z, w=w: sum(wi * b(x, y, z) for wi, b in zip(w, basis))
    check(f"(c)/(d) trial {trial}: random combination is harmonic", lap_cart(F, [0.2, -0.3, 0.1], 1e-3), 0, atol=1e-5)
    u = rng5.normal(size=(3, 50000)); u /= np.linalg.norm(u, axis=0)
    inner = F(*(u * 0.9 * rng5.uniform(0, 1, 50000)**(1 / 3)))
    bnd = F(*u)
    check(f"(c)/(d) trial {trial}: max inside < max on boundary, min inside > min on boundary",
          [inner.max() < bnd.max(), inner.min() > bnd.min()], [True, True])
# (d) TRUE: uniqueness. Discrete check: Jacobi relaxation of Laplace's equation on a cube with V = 0 on all
#     faces, started from a random interior guess, decays to the unique solution V = 0.
n5 = 12
Vgrid = np.zeros((n5, n5, n5))
Vgrid[1:-1, 1:-1, 1:-1] = rng5.uniform(-50, 50, (n5 - 2, n5 - 2, n5 - 2))
start_max = np.abs(Vgrid).max()
for _ in range(3000):
    Vgrid[1:-1, 1:-1, 1:-1] = (Vgrid[2:, 1:-1, 1:-1] + Vgrid[:-2, 1:-1, 1:-1] + Vgrid[1:-1, 2:, 1:-1]
                               + Vgrid[1:-1, :-2, 1:-1] + Vgrid[1:-1, 1:-1, 2:] + Vgrid[1:-1, 1:-1, :-2]) / 6
check(f"(d) relaxation from random start (max |V| = {start_max:.1f} V) ends at V = 0", np.abs(Vgrid).max(), 0, atol=1e-8)
print("  => (a) true, (b) false, (c) false, (d) true")

print()
print("=" * 78)
print("7.6  Coaxial cable by Laplace")
print("=" * 78)
a, b, V0 = 1e-3, 4e-3, 100.0
L = np.log(b / a)
show("ln 4", L)
Vc = lambda r: V0 * np.log(b / r) / L
check("V(a) [V]", Vc(a), 100)
check("V(b) [V]", Vc(b), 0, atol=1e-12)
for r in [1.5e-3, 2.5e-3, 3.5e-3]:
    check(f"cyl Laplacian at r={r*1e3} mm", lap_cyl_radial(Vc, r, 1e-7), 0, atol=1.0)
    F = lambda x, y, z: Vc(np.hypot(x, y))
    check(f"3-D Cartesian Laplacian at r={r*1e3} mm", lap_cart(F, [r / np.sqrt(2), r / np.sqrt(2), 0.3], 1e-6), 0, atol=50.0)
check("V0/ln(b/a) [V]", V0 / L, 72.1348, rtol=1e-5)
Erc = lambda r: -d1(Vc, r, 1e-9)
check("E_r(a) [V/m] outward", Erc(a), 72134.75, rtol=1e-5)
check("E_r(b) [V/m] outward", Erc(b), 18033.69, rtol=1e-5)
rh = np.sqrt(a * b)
check("radius where V = 50 V [m] = sqrt(ab)", rh, 2e-3)
check("V(sqrt(ab)) [V]", Vc(rh), 50)
show("V at arithmetic mean 2.5 mm", Vc(2.5e-3), "V")
rsa = eps0 * Erc(a)
rsb = -eps0 * Erc(b)
check("rho_s(a) [C/m^2]", rsa, 6.38698e-7, rtol=1e-5)
check("rho_s(b) [C/m^2]", rsb, -1.59675e-7, rtol=1e-5)
show("rho_s(a) nC/m^2", rsa * 1e9); show("rho_s(b) nC/m^2", rsb * 1e9)
rla = 2 * np.pi * a * rsa
rlb = 2 * np.pi * b * rsb
check("rho_l inner [C/m] = 2 pi eps0 V0/ln(b/a)", rla, 2 * np.pi * eps0 * V0 / L, rtol=1e-6)
show("rho_l inner nC/m", rla * 1e9); show("rho_l outer nC/m", rlb * 1e9)
check("(rho_l inner + outer)/rho_l inner = 0", (rla + rlb) / rla, 0, atol=1e-6)
check("Gauss check: E(r) = rho_l/(2 pi eps0 r) at 3 mm", rla / (2 * np.pi * eps0 * 3e-3), Erc(3e-3), rtol=1e-6)
solc = solve_bvp(lambda r, y: np.vstack([y[1], -y[1] / r]),
                 lambda ya, yb: np.array([ya[0] - V0, yb[0]]),
                 np.linspace(a, b, 21), np.vstack([np.linspace(V0, 0, 21), -V0 / (b - a) * np.ones(21)]), tol=1e-8)
check("solve_bvp V(2 mm) [V]", solc.sol(2e-3)[0], 50, rtol=1e-5)
check("solve_bvp E(a) [V/m]", -solc.sol(a)[1], 72134.75, rtol=1e-4)

print()
print("=" * 78)
print("7.7  Space charge between grounded plates")
print("=" * 78)
d, rho0 = 0.03, 1e-6
# (a) uniform
Va_ = lambda x: rho0 * x * (d - x) / (2 * eps0)
check("(a) V(0)", Va_(0), 0); check("(a) V(d)", Va_(d), 0, atol=1e-12)
for x in [0.005, 0.015, 0.025]:
    check(f"(a) V'' = -rho0/eps0 at x={x}", d2(Va_, x, 1e-5), -rho0 / eps0, rtol=1e-6)
check("rho0/eps0 [V/m^2]", rho0 / eps0, 112940.9, rtol=1e-6)
check("(a) V_max at d/2 [V] = rho0 d^2/(8 eps0)", Va_(d / 2), rho0 * d**2 / (8 * eps0), rtol=1e-12)
check("(a) V_max hand value [V]", Va_(d / 2), 12.70585, rtol=1e-6)
res = minimize_scalar(lambda x: -Va_(x), bounds=(0, d), method="bounded", options={"xatol": 1e-12})
check("(a) numerical argmax [m]", res.x, d / 2, rtol=1e-6)
Ea0, Ead = -d1(Va_, 0.0, 1e-7), -d1(Va_, d, 1e-7)
check("(a) E_x(0) [V/m] = -rho0 d/(2 eps0) (points -x, into plate)", Ea0, -rho0 * d / (2 * eps0), rtol=1e-6)
check("(a) E_x(d) [V/m] = +rho0 d/(2 eps0) (points +x, into plate)", Ead, rho0 * d / (2 * eps0), rtol=1e-6)
check("(a) |E| at plates hand value [V/m]", Ead, 1694.114, rtol=1e-6)
check("(a) rho_s(0) [C/m^2] = -rho0 d/2", eps0 * Ea0, -1.5e-8, rtol=1e-6)
check("(a) rho_s(d) [C/m^2] = -rho0 d/2", -eps0 * Ead, -1.5e-8, rtol=1e-6)
# (b) graded rho = 2 rho0 x/d
rhob = lambda x: 2 * rho0 * x / d
Vb_ = lambda x: rho0 * x * (d**2 - x**2) / (3 * eps0 * d)
check("(b) V(0)", Vb_(0), 0); check("(b) V(d)", Vb_(d), 0, atol=1e-12)
for x in [0.005, 0.015, 0.025]:
    check(f"(b) V'' = -rho/eps0 at x={x}", d2(Vb_, x, 1e-5), -rhob(x) / eps0, rtol=1e-6)
check("(b) total charge per area [C/m^2] = rho0 d", quad(rhob, 0, d, epsabs=0, epsrel=1e-12)[0], 3e-8, rtol=1e-9)
xm = d / np.sqrt(3)
res = minimize_scalar(lambda x: -Vb_(x), bounds=(0, d), method="bounded", options={"xatol": 1e-12})
check("(b) argmax [m] = d/sqrt3", res.x, xm, rtol=1e-6)
show("(b) x_max in cm", xm * 100)
check("(b) V_max [V] = 2 rho0 d^2/(9 sqrt3 eps0)", Vb_(xm), 2 * rho0 * d**2 / (9 * np.sqrt(3) * eps0), rtol=1e-12)
show("(b) V_max", Vb_(xm), "V")
Eb0, Ebd = -d1(Vb_, 0.0, 1e-7), -d1(Vb_, d, 1e-7)
check("(b) E_x(0) [V/m] = -rho0 d/(3 eps0)", Eb0, -rho0 * d / (3 * eps0), rtol=1e-6)
check("(b) E_x(d) [V/m] = +2 rho0 d/(3 eps0)", Ebd, 2 * rho0 * d / (3 * eps0), rtol=1e-6)
check("(b) E_x(0), E_x(d) hand values [V/m]", [Eb0, Ebd], [-1129.409, 2258.818], rtol=1e-6)
rsb0, rsbd = eps0 * Eb0, -eps0 * Ebd
check("(b)/(c) rho_s(0) [C/m^2] = -rho0 d/3", rsb0, -1e-8, rtol=1e-6)
check("(b)/(c) rho_s(d) [C/m^2] = -2 rho0 d/3", rsbd, -2e-8, rtol=1e-6)
check("(c) total induced = -total space charge", rsb0 + rsbd, -3e-8, rtol=1e-6)
check("(c) charge between plate 0 and zero-field plane = |rho_s(0)|", quad(rhob, 0, xm, epsabs=0, epsrel=1e-12)[0], 1e-8, rtol=1e-9)
check("(c) charge between zero-field plane and plate d = |rho_s(d)|", quad(rhob, xm, d, epsabs=0, epsrel=1e-12)[0], 2e-8, rtol=1e-9)
check("(b) E_x = 0 at x = d/sqrt3", -d1(Vb_, xm, 1e-7), 0, atol=1e-6)
for lab, rhof, Vf in [("(a)", lambda x: rho0 + 0 * x, Va_), ("(b)", rhob, Vb_)]:
    s = solve_bvp(lambda x, y, rhof=rhof: np.vstack([y[1], -rhof(x) / eps0]),
                  lambda ya, yb: np.array([ya[0], yb[0]]),
                  np.linspace(0, d, 31), np.zeros((2, 31)), tol=1e-10)
    xs = np.linspace(0, d, 7)
    check(f"{lab} solve_bvp V(x) agrees", s.sol(xs)[0], Vf(xs), rtol=1e-6, atol=1e-9)

print()
print("=" * 78)
print("7.8  Plates and a charged sheet (z in m, V in V, charges in units of eps0)")
print("=" * 78)
VA = lambda z: 3 * z
VB = lambda z: 27 - 6 * z
check("V(0)", VA(0), 0); check("V(3) from below", VA(3), 9); check("V(3) from above", VB(3), 9); check("V(4)", VB(4), 3)
EA, EB = -d1(VA, 1.5, 1e-4), -d1(VB, 3.5, 1e-4)
check("E_z below [V/m]", EA, -3); check("E_z above [V/m]", EB, 6)
rs_0 = +EA           # n = +z, units eps0
rs_4 = -EB           # n = -z
rs_s = EB - EA       # n = +z from below (2) into above (1)
check("rho_s(z=0)/eps0", rs_0, -3); check("rho_s(z=4)/eps0", rs_4, -6); check("rho_s(sheet)/eps0", rs_s, 9)
check("sum of charges", rs_0 + rs_4 + rs_s, 0)
show("rho_s(0) [C/m^2]", -3 * eps0); show("rho_s(4) [C/m^2]", -6 * eps0); show("rho_s(sheet) [C/m^2]", 9 * eps0)


def sheet_field(z, sheets):
    return sum(0.5 * s * np.sign(z - z0) for z0, s in sheets)   # in units of 1/eps0 -> V/m


sheets = [(0, -3), (3, 9), (4, -6)]
check("superposition E(z<0), E(0<z<3), E(3<z<4), E(z>4)",
      [sheet_field(z, sheets) for z in (-1, 1.5, 3.5, 5)], [0, -3, 6, 0])
# (d): unknown V_s with rho_s = 13 eps0
Vs_d = 3 * (13 + 3) / 4
check("(d) V_s [V]", Vs_d, 12)
EAd, EBd = -Vs_d / 3, (Vs_d - 3) / 1
check("(d) E below, above [V/m]", [EAd, EBd], [-4, 9])
check("(d) jump (E_above - E_below) = 13", EBd - EAd, 13)
check("(d) plate charges /eps0", [EAd, -EBd], [-4, -9])
check("(d) plates + sheet = 0", EAd - EBd + 13, 0)
# 'watch out': subtracting in the wrong order, E_below - E_above = rho_s/eps0  ->  -(4/3) Vs + 3 = 9
Vs_wrong = (3 - 9) * 3 / 4
check("wrong-order jump gives a NEGATIVE V_s (a minimum on a positive sheet) [V]", Vs_wrong, -4.5)
check("  ... which indeed satisfies E_below - E_above = 9 with the wrong order", (-Vs_wrong / 3) - (Vs_wrong - 3), 9)
# independent: finite-difference Poisson solve with a thin sheet layer


def fd_sheet(rs_over_eps0, Vtop=3.0, N=40001):
    z = np.linspace(0, 4, N); h = z[1] - z[0]
    f = np.zeros(N)                      # f = rho/eps0
    k = np.argmin(abs(z - 3.0))
    f[k] = rs_over_eps0 / h               # delta function on the grid
    n = N - 2
    main = -2 * np.ones(n); off = np.ones(n - 1)
    Amat = np.diag(main) + np.diag(off, 1) + np.diag(off, -1)
    rhs = -f[1:-1] * h**2
    rhs[-1] -= Vtop
    return z, k


# use a sparse banded solve to keep it fast
from scipy.linalg import solve_banded


def fd_sheet_solve(rs_over_eps0, Vtop=3.0, N=4001):
    z = np.linspace(0, 4, N); h = z[1] - z[0]
    f = np.zeros(N); k = int(round(3.0 / h)); f[k] = rs_over_eps0 / h
    n = N - 2
    ab = np.zeros((3, n)); ab[0, 1:] = 1; ab[1, :] = -2; ab[2, :-1] = 1
    rhs = -f[1:-1] * h**2; rhs[-1] -= Vtop
    Vin = solve_banded((1, 1), ab, rhs)
    V = np.concatenate([[0.0], Vin, [Vtop]])
    return z, V, k


z, Vfd, k = fd_sheet_solve(9.0)
check("FD Poisson solve: V(3) for rho_s = 9 eps0 [V]", Vfd[k], 9.0, rtol=1e-9)
z, Vfd, k = fd_sheet_solve(13.0)
check("FD Poisson solve: V(3) for rho_s = 13 eps0 [V]", Vfd[k], 12.0, rtol=1e-9)

print()
print("=" * 78)
print("7.9  Junction with an intrinsic layer (exam units: rho in C/m^3, z in m, eps0 kept symbolic)")
print("=" * 78)


def rho_pin(z):
    return np.where((z > -3) & (z < -1), -2.0, np.where((z > 1) & (z < 2), 4.0, 0.0))


def E_formula(z):
    z = np.asarray(z, float)
    return np.select([z < -3, z < -1, z < 1, z < 2], [0 * z, -2 * (z + 3), -4 + 0 * z, 4 * (z - 2)], 0 * z)


def V_formula(z):
    z = np.asarray(z, float)
    return np.select([z <= -3, z <= -1, z <= 1, z <= 2],
                     [0 * z, (z + 3)**2, 4 * (z + 2), 14 - 2 * (z - 2)**2], 14 + 0 * z)


print("  total charge per area (must be 0):", quad(lambda z: float(rho_pin(z)), -3, 2, points=[-1, 1])[0])
zs = np.array([-3.5, -2.5, -1.5, -0.5, 0.0, 0.7, 1.3, 1.8, 2.5])
Ez_int = np.array([quad(lambda s: float(rho_pin(s)), -4, zz, points=[-3, -1, 1, 2], limit=200)[0] for zz in zs])
check("E_z*eps0 by integrating rho (Gauss) vs formula", Ez_int, E_formula(zs), atol=1e-9)
Vz_int = np.array([-quad(lambda s: float(E_formula(s)), -4, zz, points=[-3, -1, 1, 2], limit=200)[0] for zz in zs])
check("V*eps0 by integrating -E vs formula", Vz_int, V_formula(zs), atol=1e-9)
# Poisson by FD inside each region
for zz, rho_here in [(-2.2, -2), (0.4, 0), (1.6, 4)]:
    check(f"V'' = -rho at z={zz} (eps0=1 units)", d2(lambda s: V_formula(s), zz, 1e-3), -rho_here, rtol=1e-6, atol=1e-6)
check("continuity of V at z=-1,1,2", [V_formula(-1 - 1e-12) - V_formula(-1 + 1e-12), V_formula(1 - 1e-12) - V_formula(1 + 1e-12),
                                       V_formula(2 - 1e-12) - V_formula(2 + 1e-12)], [0, 0, 0], atol=1e-9)
check("V(-1), V(1), V(0), V(2)  [units 1/eps0]", V_formula([-1, 1, 0, 2]), [4, 12, 8, 14])
check("max |E| [units 1/eps0]", np.max(abs(E_formula(np.linspace(-4, 3, 7001)))), 4)
# independent IVP: V'' = -rho, V(-3)=0, V'(-3)=0
iv = solve_ivp(lambda z, y: [y[1], -float(rho_pin(z))], [-3, 2.5], [0, 0], max_step=1e-3, rtol=1e-10, atol=1e-12, dense_output=True)
check("solve_ivp V(2), V(0) [1/eps0]", [iv.sol(2.0)[0], iv.sol(0.0)[0]], [14, 8], rtol=1e-5)
check("solve_ivp E(2) = -V'(2) = 0", -iv.sol(2.0)[1], 0, atol=1e-6)
show("4/eps0 [V/m]", 4 / eps0); show("8/eps0 [V]", 8 / eps0); show("14/eps0 [V]", 14 / eps0); show("6/eps0 [V]", 6 / eps0)
# no gap: slab 1 on (-3,-1) rho=-2, slab 2 on (-1,0) rho=+4
rho_ng = lambda z: -2.0 if -3 < z < -1 else (4.0 if -1 < z < 0 else 0.0)
iv2 = solve_ivp(lambda z, y: [y[1], -rho_ng(z)], [-3, 1], [0, 0], max_step=1e-3, rtol=1e-10, atol=1e-12, dense_output=True)
check("no-gap V2 [1/eps0]", iv2.sol(0.5)[0], 6, rtol=1e-5)
check("lecture formula rho2 W2 (W1+W2)/2 [1/eps0]", 4 * 1 * (2 + 1) / 2, 6)
check("gap adds Emax*g [1/eps0]", 4 * 2, 14 - 6)
# (d) silicon
eps_si = 11.7 * eps0
NA, ND = 1e22, 2e22
W1, g, W2 = 0.2e-6, 0.2e-6, 0.1e-6
check("neutrality NA W1 = ND W2", NA * W1, ND * W2, rtol=1e-12)
Emax = e * NA * W1 / eps_si
check("(d) E_max [V/m]", Emax, 3.09318e6, rtol=1e-5)
dV = Emax * (W1 / 2 + g + W2 / 2)
check("(d) V2 - V1 [V]", dV, 1.08261, rtol=1e-5)
show("(d) e N_A [C/m^3]", e * NA); show("(d) e N_D [C/m^3]", e * ND); show("(d) eps = 11.7 eps0 [F/m]", eps_si)
check("(d) W1/2 + g + W2/2 [m]", W1 / 2 + g + W2 / 2, 0.35e-6, rtol=1e-12)
check("(d) E_max = e N_D W2/eps (same from the n side) [V/m]", e * ND * W2 / eps_si, Emax, rtol=1e-12)
# solve in micrometres so the ODE is well scaled: u = z/1 um, V in volts,
# d2V/du2 = -(rho/eps)*1e-12  [V/um^2]; dV/du in V/um = 1e-6 * (V/m)
rho_si_u = lambda u: (-e * NA if 0 < u < 0.2 else (e * ND if 0.4 < u < 0.5 else 0.0)) / eps_si * 1e-12
iv3 = solve_ivp(lambda u, y: [y[1], -rho_si_u(u)], [0, 0.55], [0, 0], max_step=1e-4, rtol=1e-10, atol=1e-12, dense_output=True)
check("(d) solve_ivp V across structure [V]", iv3.sol(0.54)[0], dV, rtol=1e-4)
check("(d) solve_ivp max field [V/m]", np.max(np.abs(iv3.sol(np.linspace(0, 0.55, 5501))[1])) * 1e6, Emax, rtol=1e-4)
check("(d) solve_ivp field at u=0.54 um (outside) [V/m]", iv3.sol(0.54)[1] * 1e6, 0, atol=1e-4 * Emax)
check("(d) scaling from exam answer: 14/eps0 * (e NA/2) * (1e-7)^2 / 11.7", 14 / eps0 * (e * NA / 2) * 1e-14 / 11.7, dV, rtol=1e-9)

print()
print("=" * 78)
print("7.10  Space-charge-limited vacuum diode")
print("=" * 78)
d, Va = 8e-3, 16.0
Vd = lambda x: Va * (x / d)**(4 / 3)
check("V(0)", Vd(0.0), 0); check("V(d)", Vd(d), 16); check("V(1 mm) [V]", Vd(1e-3), 1.0, rtol=1e-12)
rho_d = lambda x: -(4 * eps0 * Va / (9 * d**2)) * (d / x)**(2 / 3)
for x in [1e-3, 3e-3, 6e-3]:
    check(f"rho = -eps0 V'' at x={x*1e3:.0f} mm", -eps0 * d2(Vd, x, 1e-6), rho_d(x), rtol=1e-5)
coef = 4 * eps0 * Va / (9 * d**2)
check("4 eps0 Va/(9 d^2) [C/m^3]", coef, 9.83799e-7, rtol=1e-5)
check("rho(1 mm) [C/m^3]", rho_d(1e-3), -3.93520e-6, rtol=1e-5)
check("rho(d) [C/m^3]", rho_d(d), -9.83799e-7, rtol=1e-5)
Ed = lambda x: -(4 * Va / (3 * d)) * (x / d)**(1 / 3)
for x in [1e-3, 5e-3]:
    check(f"E = -V' at x={x*1e3:.0f} mm", -d1(Vd, x, 1e-7), Ed(x), rtol=1e-6)
check("E_x(d) [V/m] (points -x, toward cathode)", Ed(d), -2666.667, rtol=1e-6)
check("E_x(0) [V/m]", Ed(0.0), 0.0)
rs_cath = +eps0 * Ed(0.0)
rs_an = -eps0 * Ed(d)
check("rho_s cathode [C/m^2]", rs_cath, 0.0)
check("rho_s anode [C/m^2] = 4 eps0 Va/(3d)", rs_an, 2.36112e-8, rtol=1e-5)
# NB: the integral is ~1e-8, below quad's default epsabs (1.49e-8) -> force a relative tolerance
Qsp = quad(rho_d, 0, d, limit=200, epsabs=0, epsrel=1e-10)[0]
check("space charge per area [C/m^2] (quad) = -4 eps0 Va/(3d)", Qsp, -4 * eps0 * Va / (3 * d), rtol=1e-8)
check("space charge per area, hand value [C/m^2]", Qsp, -2.36112e-8, rtol=1e-5)
check("total = 0", rs_cath + rs_an + Qsp, 0, atol=1e-18)
check("empty diode anode charge eps0 Va/d [C/m^2]", eps0 * Va / d, 1.77084e-8, rtol=1e-5)
check("ratio anode charge with/without space charge", rs_an / (eps0 * Va / d), 4 / 3)
v0 = np.sqrt(2 * e * Va / me)
vx = lambda x: np.sqrt(2 * e * Vd(x) / me)
check("v(d) [m/s]", vx(d), 2.37239e6, rtol=1e-5)
check("v(x) = v(d) (x/d)^(2/3) at 1 mm", vx(1e-3), vx(d) / 4, rtol=1e-12)
Js = [rho_d(x) * vx(x) for x in [0.1e-3, 1e-3, 4e-3, 7.9e-3, 8e-3]]
check("J = rho v at 5 positions [A/m^2] (constant, negative => -x)", Js, [-2.33395] * 5, rtol=1e-5)
Jchild = (4 * eps0 / 9) * np.sqrt(2 * e / me) * Va**1.5 / d**2
check("Child-Langmuir |J| [A/m^2]", Jchild, 2.33395, rtol=1e-5)
T = quad(lambda x: 1 / vx(x), 0, d, limit=200, epsabs=0, epsrel=1e-10)[0]
check("transit time T = 3d/v(d) [s]", T, 3 * d / v0, rtol=1e-6)
check("|J| = |space charge| / T", abs(Qsp) / T, Jchild, rtol=1e-6)
check("|Q|/T = 4 eps0 Va v(d)/(9 d^2) = |rho(d)| v(d) = |J|", [abs(Qsp) / T, 4 * eps0 * Va * v0 / (9 * d**2), abs(rho_d(d)) * v0], [Jchild] * 3, rtol=1e-6)
show("transit time", T, "s")
show("transit time in ns", T * 1e9)
# independent: integrate Newton's law m dv/dt = -e E_x = (e/m)(4Va/(3d))(x/d)^(1/3) for one electron.
# Scaled variables xi = x/d, tau = t v0/d turn it into xi'' = (2/3) xi^(1/3) (since e Va/m = v0^2/2).
check("scaling: (e/me)(4Va/(3d)) = (2/3) v0^2/d", (e / me) * (4 * Va / (3 * d)), (2 / 3) * v0**2 / d, rtol=1e-12)
xi_s = 1e-18                                  # start a hair off the cathode (x = 0, v = 0 is a rest point)
hit = lambda t, y: y[0] - 1.0
hit.terminal = True
mo = solve_ivp(lambda t, y: [y[1], (2 / 3) * max(y[0], 0.0)**(1 / 3)], [0, 10], [xi_s, xi_s**(2 / 3)],
               events=hit, rtol=1e-11, atol=1e-24, max_step=1e-3)
check("equation of motion: arrival time [s] (start offset ~3e-6 relative)", mo.t_events[0][0] * d / v0, 3 * d / v0, rtol=1e-5)
check("equation of motion: arrival speed [m/s]", mo.y_events[0][0][1] * v0, v0, rtol=1e-6)
# first integral of Poisson with V(0)=V'(0)=0: (V')^2 = 4 (|J|/eps0) sqrt(me/(2e)) sqrt(V)
lhs = d1(Vd, 5e-3, 1e-7)**2
rhs = 4 * (Jchild / eps0) * np.sqrt(me / (2 * e)) * np.sqrt(Vd(5e-3))
check("energy first integral (V')^2 vs 4K sqrt(V) at 5 mm", lhs, rhs, rtol=1e-6)

print()
print("=" * 78)
print("7.11  Charged ball, two ways")
print("=" * 78)
a, rho0 = 0.1, 1e-6
Vin = lambda r: rho0 * (3 * a**2 - r**2) / (6 * eps0)
Vout = lambda r: rho0 * a**3 / (3 * eps0 * r)
for r in [0.03, 0.07]:
    check(f"inside: (1/r^2)(r^2V')' = -rho0/eps0 at r={r}", lap_sph_radial(Vin, r, 1e-5), -rho0 / eps0, rtol=1e-5)
for r in [0.15, 0.4]:
    check(f"outside: Laplace at r={r}", lap_sph_radial(Vout, r, 1e-5), 0, atol=1e-2 * rho0 / eps0)
check("V continuous at a", Vin(a), Vout(a), rtol=1e-12)
check("V' continuous at a", d1(Vin, a, 1e-7), d1(Vout, a, 1e-7), rtol=1e-6)
check("V(0) [V] = rho0 a^2/(2 eps0)", Vin(0.0), 564.704, rtol=1e-5)
check("V(a) [V] = rho0 a^2/(3 eps0)", Vin(a), 376.469, rtol=1e-5)
check("V(0)/V(a) = 3/2", Vin(0) / Vin(a), 1.5)
Q = 4 / 3 * np.pi * a**3 * rho0
check("outside = Q/(4 pi eps0 r)", Vout(0.25), Q / (4 * np.pi * eps0 * 0.25), rtol=1e-12)
for r in [0.05, 0.2]:
    Er_ = -d1(Vin if r < a else Vout, r, 1e-7)
    Qenc = 4 / 3 * np.pi * min(r, a)**3 * rho0
    check(f"Gauss: 4 pi r^2 eps0 E_r = Q_enc at r={r}", 4 * np.pi * r**2 * eps0 * Er_, Qenc, rtol=1e-6)
# Green's function at the centre: 1-D radial integral
Vc_green = quad(lambda rp: rho0 * 4 * np.pi * rp**2 / (4 * np.pi * eps0 * rp), 0, a)[0]
check("Green's integral V(0) [V]", Vc_green, Vin(0.0), rtol=1e-9)
# brute-force Green's function off-centre (2-D integral over r', theta'; phi' gives 2 pi)


def V_green(r):
    f = lambda th, rp: rho0 * rp**2 * np.sin(th) * 2 * np.pi / (4 * np.pi * eps0 * np.sqrt(r * r + rp * rp - 2 * r * rp * np.cos(th) + 1e-300))
    return dblquad(f, 0, a, 0, np.pi, epsabs=1e-10, epsrel=1e-10)[0]


for r in [0.05, 0.2]:
    check(f"brute-force Green's integral V({r}) [V]", V_green(r), Vin(r) if r < a else Vout(r), rtol=1e-6)
# a point charge at the centre: A/r term solves Laplace inside except at 0
check("A/r is harmonic for r>0 (the excluded point-charge term)", lap_sph_radial(lambda r: 1 / r, 0.05, 1e-5), 0, atol=1e-3)
# solve_bvp: regular at small r, exact far value
Rmax = 1.0


def rhs_ball(r, y):
    return np.vstack([y[1], -2 * y[1] / r - np.where(r < a, rho0 / eps0, 0.0)])


rr = np.linspace(1e-6, Rmax, 4001)
sb = solve_bvp(rhs_ball, lambda ya, yb: np.array([ya[1], yb[0] - Q / (4 * np.pi * eps0 * Rmax)]), rr,
               np.vstack([np.zeros_like(rr), np.zeros_like(rr)]), tol=1e-8, max_nodes=200000)
check("solve_bvp V(0+) [V]", sb.sol(1e-6)[0], Vin(0.0), rtol=1e-4)
check("solve_bvp V(a) [V]", sb.sol(a)[0], Vin(a), rtol=1e-4)

print()
print("=" * 78)
print("7.12  Grounded conducting sphere in a uniform field")
print("=" * 78)
E0 = 1000.0
for a in [0.1, 0.37]:
    Vsph = lambda x, y, z, a=a: -E0 * z * (1 - a**3 / (x * x + y * y + z * z)**1.5)
    for p in [[0.2, 0.1, 0.3], [-0.5, 0.4, -0.2], [0.05, -0.6, 0.9]]:
        p = np.array(p) * (a / 0.1)
        if np.linalg.norm(p) > a * 1.05:
            check(f"a={a}: Laplacian at {np.round(p,3)}", lap_cart(Vsph, p, 1e-4 * a), 0, atol=1e-3 * E0 / a)
    # spherical-coordinate Laplacian (radial + theta parts), by FD in (r, theta)
    Vrt = lambda r, th, a=a: -E0 * (r - a**3 / r**2) * np.cos(th)
    r_, th_ = 1.7 * a, 0.9
    hr, ht = 1e-4 * a, 1e-4
    rad = (((r_ + hr)**2 * (Vrt(r_ + 2 * hr, th_) - Vrt(r_, th_)) / (2 * hr)) - ((r_ - hr)**2 * (Vrt(r_, th_) - Vrt(r_ - 2 * hr, th_)) / (2 * hr))) / (2 * hr) / r_**2
    ang = ((np.sin(th_ + ht) * (Vrt(r_, th_ + 2 * ht) - Vrt(r_, th_)) / (2 * ht)) - (np.sin(th_ - ht) * (Vrt(r_, th_) - Vrt(r_, th_ - 2 * ht)) / (2 * ht))) / (2 * ht) / (r_**2 * np.sin(th_))
    check(f"a={a}: radial part = -2E0 cos(th)(1/r - a^3/r^4)", rad, -2 * E0 * np.cos(th_) * (1 / r_ - a**3 / r_**4), rtol=1e-5)
    check(f"a={a}: angular part = +2E0 cos(th)(1/r - a^3/r^4)", ang, 2 * E0 * np.cos(th_) * (1 / r_ - a**3 / r_**4), rtol=1e-5)
    # boundary values
    ths = np.linspace(0.1, 3.0, 7)
    check(f"a={a}: V on the sphere", [Vrt(a, t) for t in ths], np.zeros(7), atol=1e-9)
    R = 1000 * a
    check(f"a={a}: V + E0 z -> 0 far away (relative)", max(abs(Vrt(R, t) + E0 * R * np.cos(t)) for t in ths) / (E0 * R), 0, atol=1e-8)
    # field on the surface
    for t in [0.0, 0.6, np.pi / 2, 2.5, np.pi]:
        rr_ = a * (1 + 1e-7)
        pt = rr_ * np.array([np.sin(t), 0, np.cos(t)])
        Ev = -grad_cart(Vsph, pt, 1e-9 * a)
        rhat = np.array([np.sin(t), 0, np.cos(t)])
        thhat = np.array([np.cos(t), 0, -np.sin(t)])
        check(f"a={a}, th={t:.3f}: E_r = 3E0 cos th, E_th = 0",
              [Ev @ rhat, Ev @ thhat], [3 * E0 * np.cos(t), 0], rtol=1e-4, atol=1e-2)
    Qtop = dblquad(lambda th, ph: 3 * eps0 * E0 * np.cos(th) * a**2 * np.sin(th), 0, 2 * np.pi, 0, np.pi / 2, epsabs=0, epsrel=1e-10)[0]
    Qbot = dblquad(lambda th, ph: 3 * eps0 * E0 * np.cos(th) * a**2 * np.sin(th), 0, 2 * np.pi, np.pi / 2, np.pi, epsabs=0, epsrel=1e-10)[0]
    check(f"a={a}: total induced charge (Qtop + Qbot)/Qtop", (Qtop + Qbot) / Qtop, 0, atol=1e-9)
    check(f"a={a}: charge on upper hemisphere = 3 pi eps0 E0 a^2", Qtop, 3 * np.pi * eps0 * E0 * a**2, rtol=1e-8)
check("max |E| on sphere = 3 E0 [V/m]", 3 * E0, 3000)
check("rho_s at north pole = 3 eps0 E0 [C/m^2]", 3 * eps0 * E0, 2.65626e-8, rtol=1e-5)
check("rho_s at south pole [C/m^2]", 3 * eps0 * E0 * np.cos(np.pi), -2.65626e-8, rtol=1e-5)
check("rho_s zero on equator", 3 * eps0 * E0 * np.cos(np.pi / 2), 0, atol=1e-20)

print()
print("=" * 78)
print(f"TOTAL FAILURES: {NFAIL}")
print("=" * 78)
