#!/usr/bin/env python3
"""R07 -- independent re-solution of content-src/practice/07-poisson-and-laplace.md.

Each section re-solves one problem from its stated data only:
  * FD Laplacian of every V(x) / V(r) / V(r,theta) the page claims,
  * a numerical BVP/IVP solve (solve_bvp / solve_ivp / sparse FD) from the boundary data,
  * a brute-force second route where one exists (Coulomb quadrature, smeared sheet,
    Lagrangian electron shooting, 2-D (r,theta) Laplace solve, sheet superposition).
Page values are transcribed literally and compared with PASS/FAIL.
chk_sf passes iff the computed value rounds to the page's printed digits.
numpy/scipy only.
"""
import numpy as np
from scipy.integrate import solve_bvp, solve_ivp, quad
from scipy.optimize import brentq
import scipy.sparse as sp
import scipy.sparse.linalg as spla

eps0 = 8.8541878128e-12
e = 1.602e-19
me = 9.109e-31
RES = []


def report(label, ok, detail):
    RES.append(bool(ok))
    print(f"{'PASS' if ok else 'FAIL'}  {label}: {detail}")


def chk(label, stated, computed, rtol=1e-6, atol=0.0):
    ok = abs(computed - stated) <= max(atol, rtol * abs(stated))
    report(label, ok, f"page {stated:.6g}, computed {computed:.8g}")


def chk_sf(label, stated_str, computed, scale=1.0):
    s = stated_str.lower()
    mant, ex = (s.split('e') + ['0'])[:2]
    dec = len(mant.split('.')[1]) if '.' in mant else 0
    stated = float(s) * scale
    half = 0.5 * 10.0 ** (-dec) * 10.0 ** int(ex) * scale
    ok = abs(computed - stated) <= half * (1 + 1e-9) + 1e-12 * abs(stated)
    report(label, ok, f"page {stated_str} (x{scale:g}), computed {computed / scale:.6g}")


def lap1d(Vf, r, h, g):
    """(1/r^g) d/dr (r^g dV/dr), flux form, g = 0 planar, 1 cylindrical, 2 spherical."""
    rp, rm = r + h / 2, r - h / 2
    return (rp ** g * (Vf(r + h) - Vf(r)) - rm ** g * (Vf(r) - Vf(r - h))) / (r ** g * h * h)


def lap3(Vf, p, h):
    x, y, z = p
    return (Vf(x + h, y, z) + Vf(x - h, y, z) + Vf(x, y + h, z) + Vf(x, y - h, z)
            + Vf(x, y, z + h) + Vf(x, y, z - h) - 6 * Vf(x, y, z)) / h ** 2


def fdcheck(label, Vf, pts, h, g, expected, scale):
    err = max(abs(lap1d(Vf, r, h, g) - expected(r)) for r in pts)
    report(label, err <= 1e-4 * scale, f"max |FD Laplacian - expected| = {err:.2e} (scale {scale:.2e})")


# ===================================================================== 7.1
print("=== 7.1 Two plates, two potentials ===")
d = 3e-3
sol = solve_bvp(lambda x, y: np.vstack([y[1], 0 * x]), lambda ya, yb: np.array([ya[0] - 9, yb[0]]),
                np.linspace(0, d, 11), np.zeros((2, 11)), tol=1e-10)
V = lambda x: sol.sol(x)[0]
Ex = lambda x: -sol.sol(x)[1]
chk("V(1 mm) [V]", 6.0, V(1e-3))
chk("A = dV/dx [V/m]", -3000.0, -Ex(1e-3))
chk("E_x in gap [V/m] (+x: 9 V plate -> grounded plate)", 3000.0, Ex(2e-3))
fdcheck("page V = 9 - 3000x satisfies V'' = 0", lambda x: 9 - 3000 * x, np.linspace(2e-4, 2.8e-3, 9), 1e-5, 0,
        lambda r: 0.0, 9 / d ** 2)
rs0, rsd = eps0 * Ex(0.0) * (+1), eps0 * Ex(d) * (-1)       # n = +x at x=0, -x at x=d
chk_sf("rho_s(0) [C/m^2]", "2.66e-8", rs0)
chk_sf("rho_s(0) [nC/m^2]", "26.6", rs0, 1e-9)
chk_sf("rho_s(d) [nC/m^2]", "-26.6", rsd, 1e-9)
chk("check: rho_s/eps0 [V/m]", 3000.0, rs0 / eps0)

# ===================================================================== 7.2
print("\n=== 7.2 Which potential needs charge ===")
opts = {'a': (lambda x, y, z: 3 * x ** 2 - 2 * y ** 2 - z ** 2, 'all'),
        'b': (lambda x, y, z: 5 * x * y * z, 'all'),
        'c': (lambda x, y, z: x ** 2 + y ** 2 - z ** 2, 'all'),
        'd': (lambda x, y, z: 4 * np.log(np.hypot(x, y)), 'cyl'),
        'e': (lambda x, y, z: 2 / np.sqrt(x * x + y * y + z * z), 'sph')}
rng = np.random.default_rng(7)


def sample(reg, n=25):
    pts = []
    while len(pts) < n:
        p = rng.uniform(-2.5, 2.5, 3)
        rc, rsph = np.hypot(p[0], p[1]), np.linalg.norm(p)
        if reg == 'all' or (reg == 'cyl' and 1.05 < rc < 1.95) or (reg == 'sph' and rsph > 1.05):
            pts.append(p)
    return pts


nonzero = []
for k, (Vf, reg) in opts.items():
    L = np.array([lap3(Vf, p, 1e-3) for p in sample(reg)])
    print(f"      ({k}) FD Laplacian over 25 random points in its region: mean {L.mean():+.6f}, spread {np.ptp(L):.1e} V/m^2")
    if abs(L.mean()) > 1e-3:
        nonzero.append((k, L.mean()))
report("exactly one option needs charge, and it is (c)", len(nonzero) == 1 and nonzero[0][0] == 'c',
       f"nonzero Laplacian in {[k for k, _ in nonzero]}")
chk("(c) Laplacian [V/m^2]", 2.0, nonzero[0][1], rtol=1e-4)
chk_sf("(c) rho = -eps0*lap [C/m^3]", "-1.77e-11", -eps0 * nonzero[0][1])
h = 1e-3
Va2 = opts['a'][0]
p0 = (0.3, -0.7, 1.1)
for lab, dvec, val in (("d2V/dx2", (h, 0, 0), 6), ("d2V/dy2", (0, h, 0), -4), ("d2V/dz2", (0, 0, h), -2)):
    fd = (Va2(*np.add(p0, dvec)) - 2 * Va2(*p0) + Va2(*np.subtract(p0, dvec))) / h ** 2
    chk(f"(a) {lab}", val, fd, rtol=1e-5)
Vb2 = opts['b'][0]
mixed = (Vb2(0.3 + h, -0.7 + h, 1.1) - Vb2(0.3 + h, -0.7 - h, 1.1) - Vb2(0.3 - h, -0.7 + h, 1.1)
         + Vb2(0.3 - h, -0.7 - h, 1.1)) / (4 * h * h)
print(f"      note (b): mixed derivative d2V/dxdy of 5xyz at z=1.1 is {mixed:.4f} (= 5z), only the pure ones vanish")
for rr in (1.2, 1.5, 1.9):
    Vd = lambda r: 4 * np.log(r)
    Ve = lambda r: 2 / r
    chk(f"(d) d2V/dr2 at r={rr} vs -4/r^2", -4 / rr ** 2, (Vd(rr + h) - 2 * Vd(rr) + Vd(rr - h)) / h ** 2, rtol=1e-5)
    chk(f"(e) d2V/dr2 at r={rr} vs +4/r^3", 4 / rr ** 3, (Ve(rr + h) - 2 * Ve(rr) + Ve(rr - h)) / h ** 2, rtol=1e-5)
fdcheck("(d) cylindrical Laplacian of 4 ln r = 0", lambda r: 4 * np.log(r), np.linspace(1.1, 1.9, 9), 1e-4, 1,
        lambda r: 0.0, 4.0)
fdcheck("(e) spherical Laplacian of 2/r = 0", lambda r: 2 / r, np.linspace(1.1, 5, 9), 1e-4, 2, lambda r: 0.0, 2.0)

# ===================================================================== 7.3
print("\n=== 7.3 Concentric spheres, find the error ===")
a, b = 0.01, 0.02
rr = np.linspace(a, b, 21)
sol = solve_bvp(lambda r, y: np.vstack([y[1], -2 * y[1] / r]), lambda ya, yb: np.array([ya[0] - 100, yb[0]]),
                rr, np.vstack([100 * (b - rr) / (b - a), -1e4 * np.ones_like(rr)]), tol=1e-10)
V = lambda r: sol.sol(r)[0]
Er = lambda r: -sol.sol(r)[1]
chk_sf("V(1.5 cm) [V]", "33.3", V(0.015))
chk("E(a) [V/m] (outward)", 20e3, Er(a))
chk("E(b) [V/m] (outward)", 5e3, Er(b))
Avals = [r * r * Er(r) for r in np.linspace(a, b, 7)]
chk("A = r^2 E_r, constant across gap [V m]", 2.0, np.mean(Avals))
report("r^2 E_r constant", np.ptp(Avals) < 1e-6, f"spread {np.ptp(Avals):.1e}")
chk("B = V - A/r [V]", -100.0, V(0.013) - 2 / 0.013)
fdcheck("page V = 2/r - 100 satisfies spherical Laplace", lambda r: 2 / r - 100, np.linspace(0.011, 0.019, 9), 1e-6,
        2, lambda r: 0.0, 100 / a ** 2)
Vs = lambda r: 100 * (b - r) / (b - a)               # student's potential
chk("student's own arithmetic: E = -dV/dr [V/m]", 1e4, -(Vs(0.015 + 1e-6) - Vs(0.015 - 1e-6)) / 2e-6)
chk("student's own arithmetic: V(1.5 cm) [V]", 50.0, Vs(0.015))
chk("average field (V(a)-V(b))/(b-a) [V/m]", 1e4, (100 - 0) / (b - a))
chk("spherical Laplacian of student V at 1.5 cm [V/m^2]", -1.33e6, lap1d(Vs, 0.015, 1e-6, 2), rtol=3e-3)
chk("... equals -2e4/r", -2e4 / 0.015, lap1d(Vs, 0.015, 1e-6, 2), rtol=1e-5)

# ===================================================================== 7.4
print("\n=== 7.4 Wedge between two plates ===")
sol = solve_bvp(lambda p, y: np.vstack([y[1], 0 * p]), lambda ya, yb: np.array([ya[0], yb[0] - 100]),
                np.linspace(0, np.pi / 2, 11), np.zeros((2, 11)), tol=1e-10)
chk("A = dV/dphi [V/rad] = 200/pi", 200 / np.pi, sol.sol(0.3)[1])
chk("V on bisector [V]", 50.0, sol.sol(np.pi / 4)[0])
Vw = lambda x, y, z=0.0: (200 / np.pi) * np.arctan2(y, x)
L = [lap3(Vw, (0.1 * np.cos(f) * s, 0.1 * np.sin(f) * s, 0.0), 1e-5)
     for f, s in zip(rng.uniform(0.1, 1.4, 10), rng.uniform(0.5, 3, 10))]
report("page V = (200/pi) phi harmonic (3-D Cartesian FD, 10 pts)", max(map(abs, L)) < 1e-2,
       f"max |lap| = {max(map(abs, L)):.1e} V/m^2 (scale ~ 1e4)")
P, hh = 0.1 * np.array([np.cos(np.pi / 4), np.sin(np.pi / 4)]), 1e-7
Exw = -(Vw(P[0] + hh, P[1]) - Vw(P[0] - hh, P[1])) / (2 * hh)
Eyw = -(Vw(P[0], P[1] + hh) - Vw(P[0], P[1] - hh)) / (2 * hh)
chk_sf("|E| at r=10 cm [V/m]", "637", np.hypot(Exw, Eyw))
chk_sf("E_x on bisector [V/m]", "450", Exw)
chk_sf("E_y on bisector [V/m]", "-450", Eyw)
phihat = np.array([-np.sin(np.pi / 4), np.cos(np.pi / 4)])
chk("E_phi = -200/(pi r) [V/m]", -200 / (np.pi * 0.1), Exw * phihat[0] + Eyw * phihat[1], rtol=1e-6)
report("E clockwise seen from +z: (r x E)_z < 0", P[0] * Eyw - P[1] * Exw < 0, f"(r x E)_z = {P[0] * Eyw - P[1] * Exw:.3g}")
Ey_plate0 = -(Vw(0.1, hh) - Vw(0.1, -hh)) / (2 * hh)        # plate phi=0 at x=0.1, n = +y
Ex_plate90 = -(Vw(hh, 0.1) - Vw(-hh, 0.1)) / (2 * hh)       # plate phi=pi/2 at y=0.1, n = +x
chk_sf("rho_s grounded plate (phi=0) [nC/m^2]", "-5.64", eps0 * Ey_plate0, 1e-9)
chk_sf("rho_s 100 V plate (phi=pi/2) [nC/m^2]", "5.64", eps0 * Ex_plate90, 1e-9)
arc = quad(lambda f: (200 / (np.pi * 0.1)) * 0.1, 0, np.pi / 2)[0]  # |E_phi| r dphi along the arc
Ephi_num = lambda f: (-(Vw(0.1 * np.cos(f) + hh, 0.1 * np.sin(f)) - Vw(0.1 * np.cos(f) - hh, 0.1 * np.sin(f))) / (2 * hh)
                      * (-np.sin(f)) + -(Vw(0.1 * np.cos(f), 0.1 * np.sin(f) + hh)
                                         - Vw(0.1 * np.cos(f), 0.1 * np.sin(f) - hh)) / (2 * hh) * np.cos(f))
chk("check: V(pi/2) - V(0) = -int E.dl along arc, phi 0 -> pi/2 [V]", 100.0,
    -quad(lambda f: Ephi_num(f) * 0.1, 0, np.pi / 2)[0], rtol=1e-6)
W = lambda x, y, z=0.0: Vw(x, y) + 7.0 * x * y
print(f"      uniqueness note: V + 7xy is also harmonic (FD lap {lap3(W, (0.05, 0.08, 0), 1e-5):.1e}) and equals "
      f"0 on phi=0 ({W(0.3, 0.0):.1f}) and 100 on phi=pi/2 ({W(0.0, 0.3):.1f}); only boundedness at large r excludes it")

# ===================================================================== 7.5
print("\n=== 7.5 Laplace's equation, true or false ===")
V1 = lambda x, y, z: x ** 2 - y ** 2
V2 = lambda x, y, z: x * y * z
comb = lambda x, y, z: 3 * V1(x, y, z) - 2 * V2(x, y, z) + 7
L = [lap3(comb, p, 1e-3) for p in rng.uniform(-2, 2, (10, 3))]
report("(a) TRUE: lap(3V1 - 2V2 + 7) = 0", max(map(abs, L)) < 1e-4, f"max |lap| = {max(map(abs, L)):.1e}")
chk("(b) FALSE: lap(x^2) with V = x harmonic", 2.0, lap3(lambda x, y, z: x * x, (0.4, 0.2, -0.3), 1e-3), rtol=1e-6)
pt = (0.7, -0.4, 0.2)
gV = np.array([2 * pt[0], -2 * pt[1], 0])
chk("(b) lap(V^2) = 2|grad V|^2 for V = x^2-y^2", 2 * gV @ gV, lap3(lambda x, y, z: V1(x, y, z) ** 2, pt, 1e-4), rtol=1e-5)
gx, gw = np.polynomial.legendre.leggauss(24)
phis = np.linspace(0, 2 * np.pi, 48, endpoint=False)


def sphere_avg(f, c, R):
    tot = 0.0
    for u, w in zip(gx, gw):
        st = np.sqrt(1 - u * u)
        tot += w * np.mean([f(c[0] + R * st * np.cos(p), c[1] + R * st * np.sin(p), c[2] + R * u) for p in phis])
    return tot / 2


H = lambda x, y, z: x ** 2 - y ** 2 + 3 * x * z + y * z - 2 * x
c0, Rr = (0.3, 0.5, -0.2), 0.25
report("(c) FALSE: harmonic V equals its sphere average (no pits)", abs(sphere_avg(H, c0, Rr) - H(*c0)) < 1e-12,
       f"avg - centre = {sphere_avg(H, c0, Rr) - H(*c0):.1e}")
Wq = lambda x, y, z: x * x + y * y + z * z
chk("(c) lap is PROPORTIONAL to (avg - centre): (avg-centre)/lap = R^2/6", Rr ** 2 / 6,
    (sphere_avg(Wq, c0, Rr) - Wq(*c0)) / 6.0, rtol=1e-9)
n = 40
xs = np.linspace(0, 1, n + 2)
bvals = {}
Ls = sp.lil_matrix((n * n, n * n))
rhs = np.zeros(n * n)
bfun = lambda x, y: np.sin(3 * x) * np.cos(5 * y) + x * y        # arbitrary boundary data
for i in range(n):
    for j in range(n):
        k = i * n + j
        Ls[k, k] = -4
        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ii, jj = i + di, j + dj
            if 0 <= ii < n and 0 <= jj < n:
                Ls[k, ii * n + jj] = 1
            else:
                rhs[k] -= bfun(xs[ii + 1], xs[jj + 1])
Vin = spla.spsolve(Ls.tocsr(), rhs)
bd = [bfun(x, y) for x in xs for y in (0, 1)] + [bfun(x, y) for y in xs for x in (0, 1)]
report("(c)/(d) max principle: interior within boundary [min,max]", min(bd) <= Vin.min() and Vin.max() <= max(bd),
       f"interior [{Vin.min():.3f},{Vin.max():.3f}] boundary [{min(bd):.3f},{max(bd):.3f}]")
Vz = spla.spsolve(Ls.tocsr(), np.zeros(n * n))
report("(d) TRUE: zero boundary data -> V = 0 inside", np.max(np.abs(Vz)) == 0, f"max |V| = {np.max(np.abs(Vz))}")

# ===================================================================== 7.6
print("\n=== 7.6 Coaxial cable by Laplace ===")
a, b = 1e-3, 4e-3
rr = np.linspace(a, b, 31)
sol = solve_bvp(lambda r, y: np.vstack([y[1], -y[1] / r]), lambda ya, yb: np.array([ya[0] - 100, yb[0]]),
                rr, np.vstack([100 * (b - rr) / (b - a), -100 / (b - a) * np.ones_like(rr)]), tol=1e-10)
V = lambda r: sol.sol(r)[0]
Er = lambda r: -sol.sol(r)[1]
C = np.mean([r * Er(r) for r in rr])
chk_sf("C = r E_r [V]", "72.1", C)
chk("C = 100/ln 4", 100 / np.log(4), C)
chk_sf("E(a) [kV/m]", "72.1", Er(a), 1e3)
chk_sf("E(b) [kV/m]", "18.0", Er(b), 1e3)
r50 = brentq(lambda r: V(r) - 50, a, b, xtol=1e-14)
chk("r where V = 50 V [m] = sqrt(ab)", 2e-3, r50)
chk_sf("V(2.5 mm) [V]", "33.9", V(2.5e-3))
rsa, rsb = eps0 * Er(a), -eps0 * Er(b)
chk_sf("rho_s(a) [nC/m^2]", "639", rsa, 1e-9)
chk_sf("rho_s(b) [nC/m^2]", "-160", rsb, 1e-9)
chk_sf("rho_l inner = 2 pi a rho_s(a) [nC/m]", "4.01", 2 * np.pi * a * rsa, 1e-9)
chk_sf("rho_l inner = 2 pi eps0 100/ln4 [nC/m]", "4.01", 2 * np.pi * eps0 * 100 / np.log(4), 1e-9)
chk_sf("rho_l outer = 2 pi b rho_s(b) [nC/m]", "-4.01", 2 * np.pi * b * rsb, 1e-9)
chk_sf("Gauss check E(3 mm) = rho_l/(2 pi eps0 r) [kV/m]", "24.0", 2 * np.pi * a * rsa / (2 * np.pi * eps0 * 3e-3), 1e3)
chk_sf("BVP E(3 mm) [kV/m]", "24.0", Er(3e-3), 1e3)
fdcheck("page V = (100/ln4) ln(b/r) satisfies cylindrical Laplace", lambda r: 100 / np.log(4) * np.log(b / r),
        np.linspace(1.2e-3, 3.8e-3, 9), 1e-7, 1, lambda r: 0.0, 100 / a ** 2)

# ===================================================================== 7.7
print("\n=== 7.7 Space charge between grounded plates ===")
d, rho0 = 0.03, 1e-6
chk_sf("rho0/eps0 [V/m^2]", "1.13e5", rho0 / eps0)


def poisson(rhof):
    x = np.linspace(0, d, 101)
    s = solve_bvp(lambda x, y: np.vstack([y[1], -rhof(x) / eps0]), lambda ya, yb: np.array([ya[0], yb[0]]),
                  x, np.zeros((2, x.size)), tol=1e-10, max_nodes=100000)
    return (lambda x: s.sol(x)[0]), (lambda x: -s.sol(x)[1])


for tag, rhof, pageV, xm_s, Vm_s, E0_s, Ed_s, rs0_v, rsd_v in (
        ("(a) uniform", lambda x: rho0 + 0 * x, lambda x: rho0 * x * (d - x) / (2 * eps0), "1.5", "12.7", "-1.69", "1.69",
         -15e-9, -15e-9),
        ("(b) graded", lambda x: 2 * rho0 * x / d, lambda x: rho0 * x * (d * d - x * x) / (3 * eps0 * d), "1.73", "13.0",
         "-1.13", "2.26", -10e-9, -20e-9)):
    V, Ex = poisson(rhof)
    xm = brentq(Ex, 1e-3, d - 1e-3, xtol=1e-15)
    chk_sf(f"{tag}: x of V_max [cm]", xm_s, xm, 1e-2)
    chk_sf(f"{tag}: V_max [V]", Vm_s, V(xm))
    chk_sf(f"{tag}: E_x(0) [kV/m]", E0_s, Ex(0.0), 1e3)
    chk_sf(f"{tag}: E_x(d) [kV/m]", Ed_s, Ex(d), 1e3)
    chk(f"{tag}: rho_s(0) = eps0 E_x(0) [C/m^2]", rs0_v, eps0 * Ex(0.0))
    chk(f"{tag}: rho_s(d) = -eps0 E_x(d) [C/m^2]", rsd_v, -eps0 * Ex(d))
    xx = np.linspace(0, d, 301)
    report(f"{tag}: page V(x) formula equals BVP solution", np.max(np.abs(pageV(xx) - V(xx))) < 1e-6,
           f"max diff {np.max(np.abs(pageV(xx) - V(xx))):.1e} V")
    fdcheck(f"{tag}: page V satisfies V'' = -rho/eps0", pageV, np.linspace(2e-3, 2.8e-2, 9), 1e-5, 0,
            lambda x: -rhof(x) / eps0, rho0 / eps0)
    Vpp = [(V(x + 1e-5) - 2 * V(x) + V(x - 1e-5)) / 1e-10 for x in np.linspace(1e-4, d - 1e-4, 50)]
    report(f"{tag}: V'' <= 0 in gap (dome)", max(Vpp) <= 1e-3 * rho0 / eps0, f"max V'' = {max(Vpp):.3g}")
    if tag.startswith("(b)"):
        chk("(b) x of V_max = d/sqrt3 [m]", d / np.sqrt(3), xm)
        chk("(b) V_max = 2 rho0 d^2/(9 sqrt3 eps0)", 2 * rho0 * d * d / (9 * np.sqrt(3) * eps0), V(xm))
        Ef = lambda x: -rho0 * (d * d - 3 * x * x) / (3 * eps0 * d)
        report("(b) page E_x formula equals BVP", max(abs(Ef(x) - Ex(x)) for x in xx) < 1e-4,
               f"max diff {max(abs(Ef(x) - Ex(x)) for x in xx):.1e} V/m")
        Qtot = quad(rhof, 0, d)[0]
        chk("(c) space charge per area [C/m^2]", 30e-9, Qtot)
        chk("(c) plates total [C/m^2]", -30e-9, eps0 * Ex(0.0) - eps0 * Ex(d))
        chk("(c) charge between x=0 and E=0 plane [C/m^2]", 10e-9, quad(rhof, 0, xm)[0])
        chk("(c) charge between E=0 plane and x=d [C/m^2]", 20e-9, quad(rhof, xm, d)[0])
    else:
        chk("(a) total space charge rho0 d [C/m^2] (same as (b))", 30e-9, quad(rhof, 0, d)[0])

# ===================================================================== 7.8
print("\n=== 7.8 Plates and a charged sheet ===")
Lz, N = 4.0, 400001
z = np.linspace(0, Lz, N)
hz = z[1] - z[0]
A8 = sp.diags([np.ones(N - 3), -2 * np.ones(N - 2), np.ones(N - 3)], [-1, 0, 1], format='csc') / hz ** 2
lu = spla.splu(A8)


def sheet_fd(rs_e0, zs=3.0, w=2e-3, Vtop=3.0):
    """Brute force: smear the sheet into a slab of width w and solve V'' = -rho/eps0 by FD (no jump condition used)."""
    q = np.where(np.abs(z - zs) < w / 2, 1.0, 0.0)
    q *= rs_e0 / (q.sum() * hz)
    rhs = -q[1:-1].copy()
    rhs[-1] -= Vtop / hz ** 2
    Vv = np.empty(N)
    Vv[0], Vv[-1] = 0.0, Vtop
    Vv[1:-1] = lu.solve(rhs)
    lo = (z > 0.5) & (z < 2.5)
    hi = (z > 3.2) & (z < 3.8)
    pl, ph = np.polyfit(z[lo], Vv[lo], 1), np.polyfit(z[hi], Vv[hi], 1)
    return Vv, pl, ph, np.polyval(pl, zs)


for rs_e0, Vs_s, Eb, Ea, pb, pa in ((9.0, 9.0, -3.0, 6.0, -3.0, -6.0), (13.0, 12.0, -4.0, 9.0, -4.0, -9.0)):
    Vv, pl, ph, Vs_num = sheet_fd(rs_e0)
    tag = f"rho_s = {rs_e0:g} eps0"
    chk(f"{tag}: sheet potential V_s [V] (smeared-sheet FD)", Vs_s, Vs_num, rtol=1e-5)
    chk(f"{tag}: same from region above", Vs_s, np.polyval(ph, 3.0), rtol=1e-5)
    chk(f"{tag}: E_z below [V/m]", Eb, -pl[0], rtol=1e-5)
    chk(f"{tag}: E_z above [V/m]", Ea, -ph[0], rtol=1e-5)
    chk(f"{tag}: plate z=0, rho_s/eps0 = +E_z(0+)", pb, -pl[0], rtol=1e-5)
    chk(f"{tag}: plate z=4, rho_s/eps0 = -E_z(4-)", pa, ph[0], rtol=1e-5)
    chk(f"{tag}: total charge / eps0", 0.0, -pl[0] + ph[0] + rs_e0, atol=1e-4)
    if rs_e0 == 9.0:
        chk("page V = 3z below (slope)", 3.0, pl[0], rtol=1e-5)
        chk("page V = 3z below (intercept)", 0.0, pl[1], atol=1e-6)
        chk("page V = 27 - 6z above (slope)", -6.0, ph[0], rtol=1e-5)
        chk("page V = 27 - 6z above (intercept)", 27.0, ph[1], rtol=1e-5)
        chk_sf("rho_s(0) [C/m^2]", "-2.66e-11", eps0 * (-pl[0]))
        chk_sf("rho_s(4) [C/m^2]", "-5.31e-11", eps0 * ph[0])
        report("sheet is the maximum of V", Vv.max() <= Vs_num + 1e-2 and abs(z[np.argmax(Vv)] - 3) < 2e-3,
               f"max V = {Vv.max():.4f} at z = {z[np.argmax(Vv)]:.4f}")
for rs_e0 in (-5.0, 0.0, 9.0, 13.0, 20.0):
    chk(f"boxed formula V_s = 3/4 (rho_s/eps0 + 3) at rho_s/eps0 = {rs_e0:g}", 0.75 * (rs_e0 + 3),
        sheet_fd(rs_e0)[3], rtol=1e-5, atol=1e-4)   # FD grid h = 1e-5 m
# two-region solve_bvp with the jump condition (n from below = medium 2 into above = medium 1)
f8 = lambda t, y: np.vstack([3 * y[1], 0 * t, y[3], 0 * t])
bc8 = lambda ya, yb: np.array([ya[0], yb[2] - 3, yb[0] - ya[2], -ya[3] + yb[1] - 9.0])
s8 = solve_bvp(f8, bc8, np.linspace(0, 1, 5), np.zeros((4, 5)), tol=1e-10)
chk("two-region solve_bvp V_s [V]", 9.0, s8.sol(1.0)[0])
Vs_rev = 0.75 * (-9.0 + 3)  # jump taken as below - above  <=> rho_s -> -rho_s
chk("wrong-order jump gives V_s [V]", -4.5, Vs_rev)
report("wrong-order V_s is a minimum (below both plates' 0 V and 3 V)", Vs_rev < 0 < 3, f"V_s = {Vs_rev}")
sheets = ((0.0, -3.0), (3.0, 9.0), (4.0, -6.0))
for zz, Ez_page in ((-1.0, 0.0), (1.5, -3.0), (3.5, 6.0), (5.0, 0.0)):
    Ez = sum(0.5 * q * np.sign(zz - zq) for zq, q in sheets)
    chk(f"3-sheet superposition E_z at z={zz} [V/m]", Ez_page, Ez, atol=1e-12)

# ===================================================================== 7.9
print("\n=== 7.9 Junction with an intrinsic layer ===")


def profile(breaks, rhos, eps):
    segs, y = [], np.array([0.0, 0.0])        # (V, E) start at zero
    for za, zb, rho in zip(breaks[:-1], breaks[1:], rhos):
        s = solve_ivp(lambda zz, yy: [-yy[1], rho / eps], (za, zb), y, rtol=1e-12, atol=1e-14 * (1 + abs(y).max()),
                      dense_output=True)
        segs.append((za, zb, s))
        y = s.y[:, -1]
    def ev(zz):
        for za, zb, s in segs:
            if za <= zz <= zb:
                return s.sol(zz)
        raise ValueError
    return ev


print("-- 7.9 (a)-(c) re-parameterized (CITATIONS-WAVE1): rho = -3 / 0 / +6 C/m^3 on (-3,-1) / (-1,1) / (1,2) m")
br, rh = [-3, -1, 1, 2, 3], [-3, 0, 6, 0]
ev = profile(br, rh, 1.0)                      # eps0 = 1  ->  outputs are eps0*V and eps0*E
chk("(a) net charge per area [C/m^2]", 0.0, sum(r * (zb - za) for za, zb, r in zip(br[:-1], br[1:], rh)), atol=1e-15)
pageE = lambda zz: -3 * (zz + 3) if zz < -1 else (-6.0 if zz < 1 else (6 * (zz - 2) if zz < 2 else 0.0))
pageV = lambda zz: 1.5 * (zz + 3) ** 2 if zz < -1 else (6 * (zz + 2) if zz < 1 else (21 - 3 * (zz - 2) ** 2 if zz < 2 else 21.0))
zs = np.concatenate([np.linspace(-2.95, -1.05, 7), np.linspace(-0.95, 0.95, 7), np.linspace(1.05, 1.95, 7), [2.5, 2.9]])
report("(a) eps0 E_z: page piecewise formula == IVP", max(abs(pageE(q) - ev(q)[1]) for q in zs) < 1e-9,
       f"max diff {max(abs(pageE(q) - ev(q)[1]) for q in zs):.1e}")
chk("(a) eps0 E_z for z > 2 (field zero)", 0.0, ev(2.5)[1], atol=1e-9)
report("(b) eps0 V: page piecewise formula == IVP", max(abs(pageV(q) - ev(q)[0]) for q in zs) < 1e-9,
       f"max diff {max(abs(pageV(q) - ev(q)[0]) for q in zs):.1e}")
for zz, val in ((-1, 6), (0, 12), (1, 18), (2, 21)):
    chk(f"(b) eps0 V({zz})", val, ev(float(zz))[0], rtol=1e-9)
for lab, zz, g in (("p slab", -2.0, 3.0), ("i layer", 0.0, 0.0), ("n slab", 1.5, -6.0)):
    hh = 1e-3
    chk(f"(b) FD curvature of page eps0 V in {lab} = -rho", g, (pageV(zz + hh) - 2 * pageV(zz) + pageV(zz - hh)) / hh ** 2,
        rtol=1e-6, atol=1e-6)
chk_sf("(b) V(0) = 12/eps0 [V]", "1.36e12", ev(0.0)[0] / eps0)
chk_sf("(c) V(2) - V(-3) = 21/eps0 [V]", "2.37e12", (ev(2.0)[0] - ev(-3.0)[0]) / eps0)
Emax = max(abs(ev(q)[1]) for q in np.linspace(-3, 3, 601))
chk("(c) largest eps0 |E_z|", 6.0, Emax, rtol=1e-9)
chk_sf("(c) largest field 6/eps0 [V/m]", "6.78e11", Emax / eps0)
report("(c) field in i layer points along -z", ev(0.0)[1] < 0, f"eps0 E_z(0) = {ev(0.0)[1]:.3f}")
ev2 = profile([-3, -1, 0, 1], [-3, 6, 0], 1.0)
chk("(c) no i layer: eps0 (V2 - V1)", 9.0, ev2(0.0)[0] - ev2(-3.0)[0], rtol=1e-9)
chk("(c) lecture formula rho2 W2 (W1+W2)/2", 9.0, 6 * 1 * 3 / 2)
chk_sf("(c) no i layer: 9/eps0 [V]", "1.02e12", (ev2(0.0)[0] - ev2(-3.0)[0]) / eps0)
chk("(c) no i layer: peak eps0|E| unchanged", 6.0, max(abs(ev2(q)[1]) for q in np.linspace(-3, 1, 401)), rtol=1e-9)
chk("(c) difference = E_max g", 12.0, (ev(2.0)[0] - ev(-3.0)[0]) - 9.0, rtol=1e-9)
chk("(c) area rule 6 (1 + 2 + 0.5)", 21.0, 6 * (1 + 2 + 0.5))
for name, rr in (("Summer 2019 HE1 #1a", [0, 4, 0, -4, 0]), ("Summer 2019 HE1 (conflict) #1a", [0, -4, 0, 4, 0])):
    evx = profile([-3, -2, -1, 1, 2, 3], rr, 1.0)
    kv = [float(evx(q)[1]) for q in (-1.5, 0.0, 1.5)]
    nv = [float(ev(q)[1]) for q in (-1.5, 0.0, 1.5)]
    report(f"(a) no carry-over: eps0 E_z at z = -1.5, 0, 1.5 m differs from the {name} key",
           min(abs(a - b) for a, b in zip(kv, nv)) > 0.5, f"key {np.round(kv, 3).tolist()}, page {np.round(nv, 3).tolist()}")
NA, ND, W1, g9, W2, eps = 1e22, 2e22, 0.2e-6, 0.2e-6, 0.1e-6, 11.7 * eps0
chk_sf("(d) e N_A [C/m^3]", "1.60e3", e * NA)
chk_sf("(d) e N_D [C/m^3]", "3.20e3", e * ND)
chk("(d) N_A W1 [m^-2]", 2e15, NA * W1)
chk("(d) N_D W2 [m^-2]", 2e15, ND * W2)
evd = profile([0, W1, W1 + g9, W1 + g9 + W2], [-e * NA, 0.0, e * ND], eps)
Emd = max(abs(evd(q)[1]) for q in np.linspace(0, W1 + g9 + W2, 2001))
chk_sf("(d) E_max [MV/m]", "3.09", Emd, 1e6)
chk("(d) E_max = e N_D W2 / eps (n side)", e * ND * W2 / eps, Emd, rtol=1e-6)
chk_sf("(d) built-in potential [V]", "1.08", evd(W1 + g9 + W2)[0])
chk("(d) field back to zero at the n edge (relative)", 0.0, evd(W1 + g9 + W2)[1] / Emd, atol=1e-8)

# ===================================================================== 7.10
print("\n=== 7.10 Space-charge-limited vacuum diode ===")
d, Va = 8e-3, 16.0
Vd = lambda x: Va * (np.abs(x) / d) ** (4 / 3)
chk("(a) V(0)", 0.0, Vd(0.0), atol=1e-15)
chk("(a) V(d)", 16.0, Vd(d))
chk("(a) V(1 mm) [V]", 1.0, Vd(1e-3))
hh = 1e-7
rhoFD = lambda x: -eps0 * (Vd(x + hh) - 2 * Vd(x) + Vd(x - hh)) / hh ** 2
EFD = lambda x: -(Vd(x + hh) - Vd(x - hh)) / (2 * hh)
chk_sf("(b) coefficient 4 eps0 Va/(9 d^2) [C/m^3]", "9.84e-7", -rhoFD(d))
chk_sf("(b) rho(1 mm) [uC/m^3]", "-3.94", rhoFD(1e-3), 1e-6)
chk_sf("(b) rho(d) [uC/m^3]", "-0.984", rhoFD(d), 1e-6)
report("(b) rho < 0 and V'' > 0 everywhere", all(rhoFD(x) < 0 for x in np.linspace(1e-4, d, 40)), "sign OK")
rhof = lambda x: -(4 * eps0 * Va / (9 * d * d)) * (d / x) ** (2 / 3)
report("(b) page rho(x) formula == FD of V", max(abs(rhof(x) / rhoFD(x) - 1) for x in np.linspace(5e-4, d, 30)) < 1e-5, "")
chk_sf("(c) E_x(d) [kV/m]", "-2.67", EFD(d), 1e3)
chk("(c) E_x near cathode (x = 1e-12 d) / E_x(d) -> 0", 0.0, (-(4 * Va / (3 * d)) * (1e-12) ** (1 / 3)) / EFD(d), atol=1e-3)
rsd = -eps0 * EFD(d)
chk_sf("(c) rho_s(d) [nC/m^2]", "23.6", rsd, 1e-9)
Qsp = quad(lambda s: rhof(d * s ** 3) * 3 * d * s * s, 0, 1)[0]        # x = d s^3 removes the x^(-2/3) singularity
chk_sf("(c) space charge per area [nC/m^2]", "-23.6", Qsp, 1e-9)
chk("(c) neutrality: rho_s(0) + rho_s(d) + space", 0.0, (0.0 + rsd + Qsp) / rsd, atol=1e-6)
chk_sf("(c) empty diode anode eps0 Va/d [nC/m^2]", "17.7", eps0 * Va / d, 1e-9)
chk("(c) ratio = 4/3", 4 / 3, rsd / (eps0 * Va / d), rtol=1e-6)
vf = lambda x: np.sqrt(2 * e * Vd(x) / me)
chk_sf("(d) v(d) [m/s]", "2.37e6", vf(d))
Js = np.array([rhoFD(x) * vf(x) for x in np.linspace(5e-4, d, 40)])
report("(d) J = rho v independent of x", np.ptp(Js) / abs(Js.mean()) < 1e-5, f"relative spread {np.ptp(Js) / abs(Js.mean()):.1e}")
chk_sf("(d) J_x [A/m^2] (-x)", "-2.33", Js.mean())
chk("(d) page closed form -(4 eps0/9) sqrt(2e/m) Va^1.5/d^2", -(4 * eps0 / 9) * np.sqrt(2 * e / me) * Va ** 1.5 / d ** 2,
    Js.mean(), rtol=1e-5)
T = quad(lambda s: 3 * d * s * s / vf(d * s ** 3), 1e-12, 1)[0]
chk_sf("(d) transit time [ns]", "10.1", T, 1e-9)
chk("(d) check: (charge in transit)/T = |J|", abs(Js.mean()), abs(Qsp) / T, rtol=1e-5)

# --- independent route: Lagrangian shooting (Gauss + Newton + energy), no use of the given V(x) ---
# electron leaving at t=0 from rest; the charge between it and the cathode is |J| t (emitted later),
# so with E(0)=0 (space-charge-limited) Gauss gives |E| = |J| t/eps0 at the electron.
def shoot(J):
    hit = lambda t, y: y[0] - d
    hit.terminal = True
    s = solve_ivp(lambda t, y: [y[1], e * J * t / (eps0 * me)], (0, 1e-6), [0.0, 0.0], events=hit,
                  rtol=1e-11, atol=1e-22, dense_output=True)
    return s, s.t_events[0][0], s.y_events[0][0][1]


Jstar = brentq(lambda J: 0.5 * me * shoot(J)[2] ** 2 / e - Va, 0.1, 20, xtol=1e-14)
sJ, TJ, vJ = shoot(Jstar)
chk_sf("(d) shooting |J| [A/m^2]", "2.33", Jstar)
chk_sf("(d) shooting transit time [ns]", "10.1", TJ, 1e-9)
chk_sf("(d) shooting v(d) [m/s]", "2.37e6", vJ)
t1 = brentq(lambda t: sJ.sol(t)[0] - 1e-3, 0, TJ, xtol=1e-24, rtol=1e-14)
chk("(a) shooting V(1 mm) = m v^2/(2e) [V]", 1.0, 0.5 * me * sJ.sol(t1)[1] ** 2 / e, rtol=1e-6)
chk_sf("(b) shooting rho(1 mm) = -|J|/v [uC/m^3]", "-3.94", -Jstar / sJ.sol(t1)[1], 1e-6)
chk_sf("(c) shooting anode charge |J| T [nC/m^2]", "23.6", Jstar * TJ, 1e-9)
chk_sf("(c) shooting |E(d)| = |J| T/eps0 [kV/m]", "2.67", Jstar * TJ / eps0, 1e3)
tt = np.linspace(TJ / 20, TJ, 30)
VV = [0.5 * me * sJ.sol(t)[1] ** 2 / e for t in tt]
report("statement consistent: trajectory potential == Va (x/d)^(4/3)",
       max(abs(v - Vd(sJ.sol(t)[0])) for v, t in zip(VV, tt)) < 1e-6 * Va, "")
# --- self-consistent BVP: w'' = kappa/sqrt(w), w(0)=0, w(1)=1, w'(0)=0 (E=0 at cathode), kappa unknown ---
# dimensionless w = V/Va, xi = x/d = s^m (m = 6, 9: RHS m s^(m-1) kappa/sqrt(w) -> 0 at the cathode, no 0/0).
# solve_bvp's relative-residual test cannot be met where w ~ 1e-20 (below the collocation's absolute
# rounding), so its status is printed for information; convergence is judged by agreement of kappa
# and w(xi) between the two transformations (independent meshes).
bc10 = lambda ya, yb, p: np.array([ya[0], yb[0] - 1.0, ya[1]])
ss = np.linspace(0, 1, 401)
kaps = []
for m in (6, 9):
    f10 = lambda s, y, p, m=m: np.vstack([m * s ** (m - 1) * y[1], m * s ** (m - 1) * p[0] / np.sqrt(np.abs(y[0]) + 1e-300)])
    s10 = solve_bvp(f10, bc10, ss, np.vstack([ss ** m, np.ones_like(ss)]), p=[0.5], tol=1e-8, max_nodes=200000)
    print(f"      Child-Langmuir solve_bvp, xi = s^{m}: status {s10.status} ({s10.message}), {s10.x.size} nodes")
    kap = s10.p[0]
    kaps.append(kap)
    chk(f"kappa = 4/9 (xi = s^{m})", 4 / 9, kap, rtol=1e-6)
    chk_sf(f"(d) BVP |J| = kappa eps0 Va^1.5 sqrt(2e/m)/d^2 [A/m^2] (xi = s^{m})", "2.33",
           kap * eps0 * Va ** 1.5 * np.sqrt(2 * e / me) / d ** 2)
    chk(f"(a) BVP V(1 mm) [V] (xi = s^{m})", 1.0, Va * s10.sol((1 / 8) ** (1 / m))[0], rtol=1e-6)
    dev = np.max(np.abs(s10.sol(ss)[0] - ss ** (4 * m / 3)))
    report(f"BVP w(xi) == xi^(4/3): statement's V(x) is the SCL solution (xi = s^{m})", dev < 1e-6, f"max diff {dev:.1e}")
report("kappa agrees between the two transformations", abs(kaps[0] - kaps[1]) < 1e-7, f"diff {abs(kaps[0] - kaps[1]):.1e}")

# ===================================================================== 7.11
print("\n=== 7.11 Charged ball, two ways ===")
a, rho0, R = 0.1, 1e-6, 2.0
S = np.zeros((4, 4))
S[1, 1] = -2.0
f11 = lambda t, y: np.vstack([a * y[1], -a * rho0 / eps0 * np.ones_like(t), (R - a) * y[3],
                              (R - a) * (-2 * y[3] / (a + (R - a) * t))])
bc11 = lambda ya, yb: np.array([ya[1], yb[0] - ya[2], yb[1] - ya[3], yb[3] + yb[2] / R])
tt = np.linspace(0, 1, 201)
s11 = solve_bvp(f11, bc11, tt, np.zeros((4, tt.size)), S=S, tol=1e-8, max_nodes=100000)
Vball = lambda r: s11.sol(r / a)[0] if r <= a else s11.sol((r - a) / (R - a))[2]
dVball = lambda r: s11.sol(r / a)[1] if r <= a else s11.sol((r - a) / (R - a))[3]
report("two-region spherical solve_bvp converged", s11.status == 0, s11.message)


def coulomb(r0):
    """Brute force V(r0) = int rho/(4 pi eps0 |r-r'|) d^3r' over the ball (phi' done exactly = 2 pi)."""
    inner = lambda rp: quad(lambda u: 1 / np.sqrt(max(r0 * r0 + rp * rp - 2 * r0 * rp * u, 1e-300)), -1, 1, limit=200)[0]
    pts = [r0] if 0 < r0 < a else None
    return rho0 / (4 * np.pi * eps0) * 2 * np.pi * quad(lambda rp: rp * rp * inner(rp), 0, a, points=pts, limit=200)[0]


pageV11 = lambda r: rho0 * (3 * a * a - r * r) / (6 * eps0) if r <= a else rho0 * a ** 3 / (3 * eps0 * r)
for lab, r0, s_ in (("V(0)", 0.0, "565"), ("V(5 cm)", 0.05, "518"), ("V(a)", 0.1, "376"), ("V(20 cm)", 0.2, "188")):
    chk_sf(f"(c) {lab} [V] solve_bvp", s_, Vball(r0))
    chk_sf(f"(c) {lab} [V] Coulomb quadrature", s_, coulomb(r0))
    chk(f"(c) {lab} page formula == BVP", pageV11(r0), Vball(r0), rtol=1e-7)
chk("(c) V(0)/V(a) = 3/2", 1.5, Vball(0.0) / Vball(a), rtol=1e-7)
chk("(d) shell integral V(0) [V]", rho0 * a * a / (2 * eps0), quad(lambda rp: rho0 * 4 * np.pi * rp * rp / (4 * np.pi * eps0 * rp), 0, a)[0])
chk("(b) C3 = rho0 a^3/(3 eps0) = Q/(4 pi eps0) [V m]", (4 / 3 * np.pi * a ** 3 * rho0) / (4 * np.pi * eps0), Vball(0.3) * 0.3, rtol=1e-7)
chk("(b) C2 = rho0 a^2/(2 eps0) [V]", rho0 * a * a / (2 * eps0), Vball(0.04) + rho0 * 0.04 ** 2 / (6 * eps0), rtol=1e-7)
fdcheck("page V inside satisfies spherical Poisson", pageV11, np.linspace(0.01, 0.09, 9), 1e-5, 2,
        lambda r: -rho0 / eps0, rho0 / eps0)
fdcheck("page V outside satisfies spherical Laplace", pageV11, np.linspace(0.11, 0.5, 9), 1e-5, 2,
        lambda r: 0.0, rho0 / eps0)
chk_sf("check: Q_enc(5 cm) = 4 pi r^2 eps0 E_r [nC]", "0.524", 4 * np.pi * 0.05 ** 2 * eps0 * (-dVball(0.05)), 1e-9)
chk_sf("check: Q = 4 pi r^2 eps0 E_r outside [nC]", "4.19", 4 * np.pi * 0.3 ** 2 * eps0 * (-dVball(0.3)), 1e-9)

# ===================================================================== 7.12
print("\n=== 7.12 Grounded sphere in a uniform field ===")
a, E0 = 0.1, 1000.0
Vc = lambda r, th: -E0 * (r - a ** 3 / r ** 2) * np.cos(th)
Vcart = lambda x, y, z: Vc(np.sqrt(x * x + y * y + z * z), np.arccos(z / np.sqrt(x * x + y * y + z * z)))
pts = []
while len(pts) < 15:
    p = rng.uniform(-0.4, 0.4, 3)
    if np.linalg.norm(p) > 1.1 * a:
        pts.append(p)
L = [abs(lap3(Vcart, p, 1e-5)) for p in pts]
report("(a) candidate harmonic for r > a (3-D Cartesian FD, 15 pts)", max(L) < 1e-3 * E0 / a,
       f"max |lap| = {max(L):.1e} (scale E0/a = {E0 / a:.0e})")
r0, t0, hh = 0.2, 0.7, 1e-5
rad = ((r0 + hh / 2) ** 2 * (Vc(r0 + hh, t0) - Vc(r0, t0)) - (r0 - hh / 2) ** 2 * (Vc(r0, t0) - Vc(r0 - hh, t0))) / (r0 * r0 * hh * hh)
ang = (np.sin(t0 + hh / 2) * (Vc(r0, t0 + hh) - Vc(r0, t0)) - np.sin(t0 - hh / 2) * (Vc(r0, t0) - Vc(r0, t0 - hh))) / (r0 * r0 * np.sin(t0) * hh * hh)
chk("(a) radial part = -2E0 cos(th)(1/r - a^3/r^4)", -2 * E0 * np.cos(t0) * (1 / r0 - a ** 3 / r0 ** 4), rad, rtol=1e-5)
chk("(a) angular part = +2E0 cos(th)(1/r - a^3/r^4)", 2 * E0 * np.cos(t0) * (1 / r0 - a ** 3 / r0 ** 4), ang, rtol=1e-5)
# 2-D FD solve of Laplace in (u = ln r/a, theta) from the data alone, for the induced part Vi = V + E0 z:
# Vi = E0 a cos(th) on r = a (V = 0 there), Vi -> 0 far away (V -> -E0 z); outer edge r = 100a.
# (Solving for Vi, which decays, avoids the O(dth^2) eigenvalue error of the discrete theta operator
#  acting on the growing uniform-field part.)
Rout, Nu, Nt = 100 * a, 460, 180
u = np.linspace(0, np.log(Rout / a), Nu + 1)
du = u[1] - u[0]
rg = a * np.exp(u)
th = (np.arange(Nt) + 0.5) * np.pi / Nt
dth = np.pi / Nt
thf = np.arange(Nt + 1) * np.pi / Nt
sinf = np.sin(thf)
sinf[0] = sinf[-1] = 0.0
idx = lambda i, j: (i - 1) * Nt + j
rows, cols, vals = [], [], []
rhs = np.zeros((Nu - 1) * Nt)
Vin_b = E0 * a * np.cos(th)
for i in range(1, Nu):
    rp, rm = a * np.exp(u[i] + du / 2), a * np.exp(u[i] - du / 2)
    cr = 1.0 / (rg[i] * du * du)
    for j in range(Nt):
        k = idx(i, j)
        ca = 1.0 / (np.sin(th[j]) * dth * dth)
        rows.append(k); cols.append(k); vals.append(-cr * (rp + rm) - ca * (sinf[j + 1] + sinf[j]))
        if i + 1 <= Nu - 1:
            rows.append(k); cols.append(idx(i + 1, j)); vals.append(cr * rp)
        if i - 1 >= 1:
            rows.append(k); cols.append(idx(i - 1, j)); vals.append(cr * rm)
        else:
            rhs[k] -= cr * rm * Vin_b[j]
        if j + 1 < Nt:
            rows.append(k); cols.append(idx(i, j + 1)); vals.append(ca * sinf[j + 1])
        if j - 1 >= 0:
            rows.append(k); cols.append(idx(i, j - 1)); vals.append(ca * sinf[j])
Vi = np.zeros((Nu + 1, Nt))
Vi[0] = Vin_b
Vi[1:Nu] = spla.spsolve(sp.csr_matrix((vals, (rows, cols)), shape=(rhs.size, rhs.size)), rhs).reshape(Nu - 1, Nt)
Vg = Vi - E0 * rg[:, None] * np.cos(th)[None, :]
near = rg <= 5 * a
errV = np.max(np.abs(Vg[near] - Vc(rg[near][:, None], th[None, :])))
report("(b) 2-D FD Laplace solution == candidate for a <= r <= 5a", errV < 1e-3 * E0 * a,
       f"max |diff| = {errV:.2e} V (E0 a = {E0 * a:.0f} V)")
Er_s = -(-3 * Vg[0] + 4 * Vg[1] - Vg[2]) / (2 * du) / a
Cfit = np.sum(Er_s * np.cos(th)) / np.sum(np.cos(th) ** 2)
chk("(c) surface E_r = C cos(th): C = 3 E0 [V/m] (max at poles)", 3000.0, Cfit, rtol=1e-3)
report("(c) surface E_r is C cos(th) (shape)", np.max(np.abs(Er_s - Cfit * np.cos(th))) < 1e-3 * Cfit, "")
chk("(c) page E_r(a, th=0.3) = 3 E0 cos th", 3 * E0 * np.cos(0.3), -(Vc(a + hh, 0.3) - Vc(a - hh, 0.3)) / (2 * hh), rtol=1e-6)
chk("(c) page E_theta(a) = 0", 0.0, -(Vc(a, 0.3 + hh) - Vc(a, 0.3 - hh)) / (2 * hh) / a, atol=1e-6)
Eth_off = -(Vc(1.2 * a, 0.8 + hh) - Vc(1.2 * a, 0.8 - hh)) / (2 * hh) / (1.2 * a)
chk("watch-out: E_theta just off the sphere = -E0(1-a^3/r^3) sin th", -E0 * (1 - 1 / 1.2 ** 3) * np.sin(0.8), Eth_off, rtol=1e-6)
chk("watch-out: E_theta on the z axis (th=0) at r = 1.2a is 0 too", 0.0,
    -(Vc(1.2 * a, hh) - Vc(1.2 * a, -hh)) / (2 * hh) / (1.2 * a), atol=1e-6)
for rr_, tt_ in ((0.15, 0.4), (0.3, 2.0)):
    Er_fd = -(Vc(rr_ + hh, tt_) - Vc(rr_ - hh, tt_)) / (2 * hh)
    chk(f"(c) page E_r formula at r={rr_}, th={tt_}", E0 * (1 + 2 * a ** 3 / rr_ ** 3) * np.cos(tt_), Er_fd, rtol=1e-6)
chk_sf("(d) rho_s north pole = 3 eps0 E0 [nC/m^2]", "26.6", 3 * eps0 * E0, 1e-9)
chk("(d) rho_s north pole, 2-D FD [C/m^2]", 26.6e-9, eps0 * Cfit, rtol=2e-3)
chk("(d) rho_s south pole, 2-D FD [C/m^2]", -26.6e-9, -eps0 * Cfit, rtol=2e-3)
up = th < np.pi / 2
Qup = np.sum(eps0 * Er_s[up] * 2 * np.pi * a * a * np.sin(th[up]) * dth)
chk_sf("(d) 3 pi eps0 E0 a^2 [C]", "8.34e-10", 3 * np.pi * eps0 * E0 * a * a)
chk("(d) upper-hemisphere charge, 2-D FD + quadrature [C] (page 8.34e-10)", 8.34e-10, Qup, rtol=1e-3)
Qall = np.sum(eps0 * Er_s * 2 * np.pi * a * a * np.sin(th) * dth)
chk("(d) total induced charge / Q_up", 0.0, Qall / Qup, atol=1e-6)
i5 = np.argmin(np.abs(rg - 1.5 * a))
pfit = np.sum(Vi[i5] * rg[i5] ** 2 * np.cos(th)) / np.sum(np.cos(th) ** 2)
chk("(b) dipole p/(4 pi eps0) = E0 a^3 from 2-D FD induced potential at r=1.5a [V m^2]", E0 * a ** 3, pfit, rtol=1e-3)
Er_far = -(Vc(100 * a + hh, 0.5) - Vc(100 * a - hh, 0.5)) / (2 * hh)
chk("check: far-field E_r -> E0 cos th", E0 * np.cos(0.5), Er_far, rtol=1e-5)

print(f"\nTOTAL: {sum(RES)} PASS, {len(RES) - sum(RES)} FAIL")
