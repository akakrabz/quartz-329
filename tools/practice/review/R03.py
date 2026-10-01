#!/usr/bin/env python3
"""R03.py -- independent re-solve of content-src/practice/03-gauss-law-at-work.md.

Every number on the page is recomputed from the problem data by a route that does not reuse
the page's derivation: direct Coulomb integrals (rings, rays cast from the field point, stacks
of thin sheets, 2-D line-element sums), numerical surface integrals, np.cross for normals,
root finding / optimisation for special points.  The page's stated values are transcribed and
compared, normally within half a unit of the last digit the page prints.
numpy + scipy only.

Ray formula used for volume charge (3-D):  E(P) = -(1/4 pi eps0) Int dOmega s_hat Int_0^inf rho(P + s s_hat) ds
(2-D, infinite in z):                      E(P) = -(1/2 pi eps0) Int dphi   s_hat Int_0^inf rho(P + s s_hat) ds
Both follow from Coulomb's law with dV' = s^2 ds dOmega (dA' = s ds dphi); the 1/R^2 (1/R) singularity cancels.
"""
import numpy as np
from scipy import integrate, optimize, special

eps0 = 8.8541878128e-12
PI = np.pi
NP = [0, 0]  # [pass, fail]


def check(label, computed, page, tol):
    """PASS if every component of `computed` lies within `tol` of the page's value."""
    c = np.atleast_1d(np.asarray(computed, dtype=float))
    p = np.atleast_1d(np.asarray(page, dtype=float))
    ok = bool(c.shape == p.shape or p.size == 1) and bool(np.all(np.abs(c - p) <= tol))
    NP[0 if ok else 1] += 1
    fmt = lambda a: ("(" + ", ".join(f"{v:.6g}" for v in a) + ")") if a.size > 1 else f"{a[0]:.6g}"
    print(f"  {'PASS' if ok else 'FAIL'}  {label:<62s} computed {fmt(c):<32s} page {fmt(p)}")
    return ok


def section(title):
    print(f"\n=== {title} ===")


GLx, GLw = np.polynomial.legendre.leggauss(64)


def chord_gl(lo, hi, f):
    """Gauss-Legendre integral of f(S) over [lo, hi], vectorised over an array of intervals."""
    S = 0.5 * (hi - lo)[..., None] * GLx + 0.5 * (hi + lo)[..., None]
    W = 0.5 * (hi - lo)[..., None] * GLw
    return np.sum(W * f(S), axis=-1)


# =============================================================== 3.1
section("3.1 Two sheets of charge")


def Ez_sheet(rho_s, z0, z):
    """E_z of an infinite sheet on z = z0 by direct Coulomb integration over rings of radius s."""
    h = z - z0
    f = lambda s: rho_s / (4 * PI * eps0) * h * 2 * PI * s / (s * s + h * h) ** 1.5
    return integrate.quad(f, 0, np.inf, limit=400)[0]


def Ez31(z):
    return Ez_sheet(4e-9, 0.0, z) + Ez_sheet(-1e-9, 2.0, z)


for zs, page, name in [((-0.5, -6.0), -169, "z<0"), ((0.3, 1.7), 282, "0<z<2"), ((2.5, 9.0), 169, "z>2")]:
    for z in zs:
        check(f"E_z at z = {z:+} m ({name}) [V/m]", Ez31(z), page, 0.5)
check("Check: eps0 * jump of E_z at z = 0 [nC/m^2] (= rho_s1)", eps0 * (Ez31(0.5) - Ez31(-0.5)) * 1e9, 4, 1e-6)
check("Check: eps0 * jump of E_z at z = 2 [nC/m^2] (= rho_s2)", eps0 * (Ez31(2.5) - Ez31(1.5)) * 1e9, -1, 1e-6)

# =============================================================== 3.2
section("3.2 Flux through a tilted window")
C0, C1, C2, C3 = (np.array(c, float) for c in [(0, 0, 0), (0, 2, 0), (3, 2, 4), (3, 0, 4)])
u, v = C1 - C0, C3 - C0
check("corners close: C0 + u + v = C2", C0 + u + v, C2, 1e-12)
check("u . v (edges perpendicular)", u @ v, 0, 1e-12)
N32 = np.cross(u, v)
check("u x v [m^2]", N32, [8, 0, -6], 1e-12)
A32 = np.linalg.norm(N32)
check("area |u x v| [m^2]", A32, 10, 1e-12)
check("|u| x |v| (2 m x 5 m rectangle)", np.linalg.norm(u) * np.linalg.norm(v), 10, 1e-12)
n32 = N32 / A32
n32 = n32 if n32[2] > 0 else -n32
check("n_hat with positive z component", n32, [-0.8, 0, 0.6], 1e-12)
m = 300
sg = (np.arange(m) + 0.5) / m
S_, T_ = np.meshgrid(sg, sg, indexing="ij")
pts = S_[..., None] * u + T_[..., None] * v  # points of the window (for a general field)


def flux32(Efun):
    E = Efun(pts)
    return np.sum(E @ n32) * A32 / m ** 2


fa = flux32(lambda p: np.broadcast_to([0, 0, 500.0], p.shape))
fb = flux32(lambda p: np.broadcast_to([300.0, 0, 400.0], p.shape))
check("(a) E.n_hat [V/m]", np.array([0, 0, 500.0]) @ n32, 300, 1e-9)
check("(a) flux of E [V m]", fa, 3000, 1e-6)
check("(a) psi_E = eps0 * flux [nC]", eps0 * fa * 1e9, 26.56, 0.005)
check("(b) |E| [V/m] (same strength)", np.linalg.norm([300, 0, 400]), 500, 1e-12)
check("(b) flux of E [V m]", fb, 0, 1e-9)
check("(b) E x v = 0 (E parallel to edge v)", np.cross([300.0, 0, 400.0], v), [0, 0, 0], 1e-12)
check("Check: shadow on xy plane = |(u x v)_z| [m^2]", abs(N32[2]), 6, 1e-12)

# =============================================================== 3.3
section("3.3 Finite line in a closed cylinder (MC, key b)")
rl3 = 3e-9


def D_seg(r, z):
    """(D_r, D_z) of the segment -1<z'<1 by direct Coulomb integration."""
    fr = lambda zp: rl3 / (4 * PI) * r / (r * r + (z - zp) ** 2) ** 1.5
    fz = lambda zp: rl3 / (4 * PI) * (z - zp) / (r * r + (z - zp) ** 2) ** 1.5
    return integrate.quad(fr, -1, 1, epsabs=1e-22)[0], integrate.quad(fz, -1, 1, epsabs=1e-22)[0]


side3 = integrate.quad(lambda z: D_seg(1.0, z)[0] * 2 * PI * 1.0, -2, 2, limit=200, epsabs=0)[0]
top3 = integrate.quad(lambda r: D_seg(r, 2.0)[1] * 2 * PI * r, 0, 1, limit=200, epsabs=0)[0]
bot3 = integrate.quad(lambda r: -D_seg(r, -2.0)[1] * 2 * PI * r, 0, 1, limit=200, epsabs=0)[0]
check("curved-side flux [nC]", side3 * 1e9, 5.244, 5e-4)
check("curved-side flux = rho_l (sqrt10 - sqrt2) [nC]", side3 * 1e9, 3 * (np.sqrt(10) - np.sqrt(2)), 1e-6)
check("top-cap flux [nC]", top3 * 1e9, 0.378, 5e-4)
check("bottom-cap flux [nC]", bot3 * 1e9, 0.378, 5e-4)
check("both caps [nC]", (top3 + bot3) * 1e9, 0.756, 5e-4)
check("total outward flux [nC] (key b)", (side3 + top3 + bot3) * 1e9, 6, 1e-6)
check("distractor (d): rho_l x 4 m [nC]", rl3 * 4 * 1e9, 12, 1e-9)

# =============================================================== 3.4
section("3.4 Charges written with delta functions (deltas as Gaussians, sigma = 0.1 mm)")
sig = 1e-4


def box1d(x0, lo=-2.0, hi=2.0):
    """Integral over [lo, hi] of a unit-area Gaussian centred at x0 (a smeared delta)."""
    return 0.5 * (special.erf((hi - x0) / (np.sqrt(2) * sig)) - special.erf((lo - x0) / (np.sqrt(2) * sig)))


Lc = 4.0  # integral of 1 over [-2, 2]
terms = [("point 4 nC at (1,-1,0)", 4 * box1d(1) * box1d(-1) * box1d(0), 4),
         ("line -2 nC/m along z through (-1,0)", -2 * box1d(-1) * box1d(0) * Lc, -8),
         ("sheet 0.5 nC/m^2 on z = 1", 0.5 * Lc * Lc * box1d(1), 8),
         ("point 2 nC at (0,3,0)", 2 * box1d(0) * box1d(3) * box1d(0), 0)]
for name, val, page in terms:
    check(f"(b) {name}: charge inside cube [nC]", val, page, 1e-9)
check("(b) psi_E out of the cube [nC]", sum(t[1] for t in terms), 4, 1e-9)

# =============================================================== 3.5
section("3.5 Magnetic flux through a dome (MC, key b)")
B5, a5 = np.array([0.3, 0, 0.4]), 0.5


def dome_flux(B, a):
    f = lambda th, ph: B @ np.array([np.sin(th) * np.cos(ph), np.sin(th) * np.sin(ph), np.cos(th)]) * a * a * np.sin(th)
    return integrate.dblquad(f, 0, 2 * PI, 0, PI / 2)[0]


psi5 = dome_flux(B5, a5)
check("dome flux by surface integral [Wb] vs 0.1 pi", psi5, 0.1 * PI, 1e-9)
check("dome flux [Wb] (key b, 0.314)", psi5, 0.314, 5e-4)
check("base flux, outward -z [Wb]", B5 @ np.array([0, 0, -1.0]) * PI * a5 ** 2, -0.1 * PI, 1e-12)
check("x component alone through the dome [Wb]", dome_flux(np.array([0.3, 0, 0]), a5), 0, 1e-9)
check("distractor (c) = B_z * 2 pi a^2 [Wb] (0.2 pi)", B5[2] * 2 * PI * a5 ** 2, 0.628, 5e-4)
check("distractor (d) = |B| * 2 pi a^2 [Wb] (0.25 pi)", np.linalg.norm(B5) * 2 * PI * a5 ** 2, 0.785, 5e-4)
check("distractor (e) = |B| * pi a^2 [Wb] (0.125 pi)", np.linalg.norm(B5) * PI * a5 ** 2, 0.393, 5e-4)

# =============================================================== 3.6
section("3.6 Sphere with a graded density (direct Coulomb by rays)")
a6, r06, b6 = 0.09, 2e-6, 0.18
rho6 = lambda r: np.where(r < a6, r06 * (1 - r / a6), 0.0)
MU6, WMU6 = np.polynomial.legendre.leggauss(600)


def Ez_ball(z0, rho, R):
    """E_z at (0,0,z0) of a spherically symmetric rho(r) supported in r<R; phi integral = 2 pi."""
    pd = z0 * MU6
    disc = pd ** 2 - z0 ** 2 + R ** 2
    sq = np.sqrt(np.clip(disc, 0, None))
    s1 = np.where(disc > 0, np.clip(-pd - sq, 0, None), 0.0)
    s2 = np.where(disc > 0, np.clip(-pd + sq, 0, None), 0.0)
    sm = np.clip(-pd, s1, s2)  # closest approach to the centre: split there (kink of |r|)
    mu = MU6[:, None]
    f = lambda S: rho(np.sqrt(np.clip(S * S + 2 * S * z0 * mu + z0 * z0, 0, None)))
    L = chord_gl(s1, sm, f) + chord_gl(sm, s2, f)
    return -(1 / (4 * PI * eps0)) * 2 * PI * np.sum(WMU6 * MU6 * L)


Q6 = integrate.quad(lambda r: rho6(r) * 4 * PI * r * r, 0, a6, epsabs=0)[0]
check("(a) Q = Int rho dV [nC]", Q6 * 1e9, 1.527, 5e-4)
check("(a) Q vs pi rho0 a^3 / 3 [nC]", Q6 * 1e9, PI * r06 * a6 ** 3 / 3 * 1e9, 1e-9)
E6_in = lambda r: r06 / eps0 * (r / 3 - r * r / (4 * a6))
E6_out = lambda r: r06 * a6 ** 3 / (12 * eps0 * r * r)
for r in [0.02, 0.045, 0.075, 0.085]:
    e = Ez_ball(r, rho6, a6)
    check(f"(b) E_r at r = {r * 100:g} cm vs page inside formula [V/m]", e, E6_in(r), 1e-4 * abs(e))
for r in [0.12, 0.30]:
    e = Ez_ball(r, rho6, a6)
    check(f"(b) E_r at r = {r * 100:g} cm vs page outside formula [V/m]", e, E6_out(r), 1e-4 * abs(e))
check("Check: E at the centre [V/m]", Ez_ball(1e-7, rho6, a6), 0, 1e-2)
res6 = optimize.minimize_scalar(lambda r: -Ez_ball(r, rho6, a6), bounds=(0.01, 0.089), method="bounded",
                                options={"xatol": 1e-8})
check("(c) location of max |E| [cm]", res6.x * 100, 6, 0.01)
check("(c) E_max [V/m]", -res6.fun, 2259, 0.5)
Ea6 = Ez_ball(a6, rho6, a6)
check("(c) E at the surface r = a [V/m]", Ea6, 1694, 0.5)
check("(c) E(a) / E_max", Ea6 / -res6.fun, 0.75, 1e-4)
rs6 = -Q6 / (4 * PI * b6 ** 2)
check("(d) rho_s = -Q/(4 pi b^2) [nC/m^2]", rs6 * 1e9, -3.75, 5e-4)
check("(d) -rho0 a^3/(12 b^2) [nC/m^2]", -r06 * a6 ** 3 / (12 * b6 ** 2) * 1e9, -3.75, 1e-9)
check("(d) -rho0 a/48 (b = 2a) [nC/m^2]", -r06 * a6 / 48 * 1e9, -3.75, 1e-9)


def Ez_shell(z0, rs, R):
    """E_z at (0,0,z0) of a thin spherical shell, by direct Coulomb integration over rings."""
    f = lambda th: rs * 2 * PI * R * R * np.sin(th) * (z0 - R * np.cos(th)) / (
        4 * PI * eps0 * (z0 * z0 + R * R - 2 * z0 * R * np.cos(th)) ** 1.5)
    return integrate.quad(f, 0, PI, limit=200)[0]


check("(d) ball + shell: E at r = 25 cm [V/m]", Ez_ball(0.25, rho6, a6) + Ez_shell(0.25, rs6, b6), 0, 1e-4 * Ez_ball(0.25, rho6, a6))  # ball alone ~220 V/m
check("(d) shell alone at r = 12 cm (inside it) [V/m]", Ez_shell(0.12, rs6, b6), 0, 1e-3)

# =============================================================== 3.7
section("3.7 Point-charge flux through a disk")
Q7, h7 = 12e-9, 0.04
nz7 = np.array([0, 0, -1.0])


def psi_disk(a):
    """Flux of D through the disk r<a on z = 0 along -z: direct 2-D integral of D.dS."""
    def f(ph, r):
        R = np.array([r * np.cos(ph), r * np.sin(ph), -h7])  # from the charge to the disk point
        return (Q7 * R / (4 * PI * np.linalg.norm(R) ** 3)) @ nz7 * r
    return integrate.dblquad(f, 0, a, 0, 2 * PI, epsabs=1e-17, epsrel=1e-10)[0]


psi_formula = lambda a: Q7 / 2 * (1 - h7 / np.sqrt(h7 ** 2 + a ** 2))
for a in [0.01, 0.03, 0.10]:
    check(f"(a) direct integral vs page formula, a = {a * 100:g} cm [nC]", psi_disk(a) * 1e9, psi_formula(a) * 1e9, 1e-6)
p7 = psi_disk(0.03)
check("(b) psi at a = 3 cm [nC]", p7 * 1e9, 1.2, 5e-3)
check("(b) psi / Q at a = 3 cm", p7 / Q7, 0.1, 1e-6)
aq = optimize.brentq(lambda a: psi_disk(a) - Q7 / 4, 0.005, 0.5, xtol=1e-12)
check("(c) radius that catches Q/4 [cm]", aq * 100, 6.93, 5e-3)
check("(c) a / h", aq / h7, np.sqrt(3), 1e-6)
check("(c) a < 2h", float(aq < 2 * h7), 1, 0)
pinf = 2 * PI * integrate.quad(lambda r: Q7 * h7 * r / (4 * PI * (r * r + h7 * h7) ** 1.5), 0, np.inf, epsabs=0)[0]
check("(d) psi as a -> infinity [nC]", pinf * 1e9, 6, 1e-6)
Rc = np.hypot(h7, 0.03)
alpha = np.arccos(h7 / Rc)
cap7 = integrate.dblquad(lambda th, ph: Q7 / (4 * PI * Rc ** 2) * Rc ** 2 * np.sin(th), 0, 2 * PI, 0, alpha, epsabs=0)[0]
check("second route: spherical-cap flux = disk flux (a = 3 cm) [nC]", cap7 * 1e9, p7 * 1e9, 1e-6)

# =============================================================== 3.8
section("3.8 Find the error, odd slab (stack of thin sheets)")
r08, a8 = 1e-6, 1.0


def Ex8(x):
    """Each layer rho dx' adds sgn(x - x') rho dx' / (2 eps0)."""
    f = lambda xp: r08 * xp / a8 * np.sign(x - xp) / (2 * eps0)
    return integrate.quad(f, -a8, a8, points=[x] if -a8 < x < a8 else None, limit=200)[0]


page8 = lambda x: -r08 * (a8 ** 2 - x ** 2) / (2 * eps0 * a8) if abs(x) < a8 else 0.0
for x in [-1.6, -0.75, -0.2, 0.0, 0.2, 0.75, 1.6]:
    check(f"(b) E_x at x = {x:+} m vs page formula [V/m]", Ex8(x), page8(x), 1e-3)
check("(a) E_x is even: E_x(0.6) - E_x(-0.6) [V/m]", Ex8(0.6) - Ex8(-0.6), 0, 1e-3)
check("(a) student's symmetric pillbox: cap fluxes E_x(x) - E_x(-x) = 0 for any E", Ex8(0.6) - Ex8(-0.6), 0, 1e-3)
check("(a) yet E_x(0.6) is not zero: value [V/m] vs page formula", Ex8(0.6), page8(0.6), 1e-3)
E80 = Ex8(0.0)
check("(c) |E(0)| [V/m]", abs(E80), 5.65e4, 50)
check("(c) sign of E_x(0) (page: along -x)", np.sign(E80), -1, 0)
check("(c) eps0 |E(0)| = charge/area of the positive half [uC/m^2]", eps0 * abs(E80) * 1e6,
      integrate.quad(lambda x: r08 * x / a8, 0, a8)[0] * 1e6, 1e-9)
check("Check: slope dE_x/dx at x = 0.4 = rho/eps0 [V/m^2]", (Ex8(0.4001) - Ex8(0.3999)) / 2e-4, r08 * 0.4 / a8 / eps0, 1.0)

# =============================================================== 3.9
section("3.9 Two slabs and a sheet (densities / eps0, E in V/m; stack of thin sheets)")


def Ez9(z, sheet):
    e = 0.0
    for lo, hi, k in [(-3, -1, 3.0), (0, 3, -2.0)]:
        e += integrate.quad(lambda zp: k * np.sign(z - zp) / 2, lo, hi, points=[z] if lo < z < hi else None)[0]
    return e + (4.0 * np.sign(z + 1) / 2 if sheet else 0.0)


pageb = lambda z: 0 if z < -3 else 3 * z + 9 if z < -1 else 6 if z < 0 else 6 - 2 * z if z < 3 else 0
pagec = lambda z: -2 if z < -3 else 3 * z + 7 if z < -1 else 8 if z < 0 else 8 - 2 * z if z < 3 else 2
check("(a) slab 1 charge per area / eps0 [V/m]", integrate.quad(lambda z: 3.0, -3, -1)[0], 6, 1e-12)
check("(a) slab 2 charge per area / eps0 [V/m]", integrate.quad(lambda z: -2.0, 0, 3)[0], -6, 1e-12)
zs9 = [-5, -2.5, -1.5, -0.5, 0.5, 2.0, 2.9, 5]
for z in zs9:
    check(f"(b) E_z at z = {z:+} m [V/m]", Ez9(z, False), pageb(z), 1e-9)
for z in zs9:
    check(f"(c) E_z at z = {z:+} m [V/m]", Ez9(z, True), pagec(z), 1e-9)
zg = np.linspace(-8, 8, 1601)
eg = np.array([Ez9(z, True) for z in zg])
roots9 = [optimize.brentq(lambda z: Ez9(z, True), zg[i], zg[i + 1], xtol=1e-13)
          for i in range(len(zg) - 1) if eg[i] * eg[i + 1] < 0]
check("(d) number of planes with E = 0 (scan -8..8 m)", len(roots9), 1, 0)
check("(d) location of E = 0 [m]", roots9[0] if roots9 else np.nan, -7 / 3, 1e-9)
check("(d) E_z just below the sheet [V/m]", Ez9(-1 - 1e-9, True), 4, 1e-6)
check("(d) E_z just above the sheet [V/m]", Ez9(-1 + 1e-9, True), 8, 1e-6)
for zf in [-3, 0, 3]:
    check(f"Check: E_z continuous at z = {zf} (case c) [V/m]", Ez9(zf + 1e-9, True) - Ez9(zf - 1e-9, True), 0, 1e-6)
check("Check: slope inside slab 1 [V/m^2]", (Ez9(-1.999, True) - Ez9(-2.001, True)) / 2e-3, 3, 1e-6)
check("Check: slope inside slab 2 [V/m^2]", (Ez9(1.501, True) - Ez9(1.499, True)) / 2e-3, -2, 1e-6)

# =============================================================== 3.10
section("3.10 Sphere with an off-centre cavity (direct Coulomb by rays, no superposition of fields)")
a10, b10, d10, k10 = 1.0, 0.4, np.array([0.5, 0, 0]), 30.0  # k10 = rho/eps0
mu10, wmu10 = np.polynomial.legendre.leggauss(800)
ph10 = (np.arange(800) + 0.5) * 2 * PI / 800
MU_, PH_ = np.meshgrid(mu10, ph10, indexing="ij")
ST_ = np.sqrt(1 - MU_ ** 2)
SH = np.stack([ST_ * np.cos(PH_), ST_ * np.sin(PH_), MU_], axis=-1)
WW = wmu10[:, None] * np.full(800, 2 * PI / 800)[None, :]


def chord3(P, C, R):
    """Length of the ray P + s s_hat (s>0) inside the sphere |r - C| < R, for every direction."""
    p = P - C
    pd = SH @ p
    disc = pd ** 2 - p @ p + R * R
    sq = np.sqrt(np.clip(disc, 0, None))
    return np.where(disc > 0, np.clip(-pd + sq, 0, None) - np.clip(-pd - sq, 0, None), 0.0)


def E10(P, cavity=True):
    L = chord3(P, np.zeros(3), a10) - (chord3(P, d10, b10) if cavity else 0.0)  # length inside the material
    return -(k10 / (4 * PI)) * np.einsum("ij,ijk->k", WW * L, SH)


Pa = np.array([0.3, 0.2, -0.4])
check("(a) full ball, Coulomb at (0.3,0.2,-0.4) vs rho r/(3 eps0) [V/m]", E10(Pa, False), 10 * Pa, 5e-4)
for Pc in [(0.5, 0, 0), (0.3, 0.1, -0.1), (0.7, -0.2, 0.15)]:
    check(f"(b) cavity field at {Pc} [V/m]", E10(np.array(Pc, float)), [5, 0, 0], 5e-3)
P10 = np.array([0.5, 0.5, 0])
check("(c) |r_P| [m]", np.linalg.norm(P10), 0.707, 5e-4)
check("(c) |r_P - d| [m] (> b: in the material)", np.linalg.norm(P10 - d10), 0.5, 1e-12)
EP = E10(P10)
check("(c) E(P) [V/m]", EP, [5, 2.44, 0], 5e-3)
check("(c) |E(P)| [V/m]", np.linalg.norm(EP), 5.56, 5e-3)
S10 = np.array([2.5, 0, 0])
check("(d) E(S) [V/m]", E10(S10), [1.44, 0, 0], 5e-3)
check("(d) E(S) with the cavity filled [V/m]", E10(S10, False), [1.6, 0, 0], 5e-3)
check("Check: E at the cavity-wall point (0.5,0.4,0) [V/m]", E10(np.array([0.5, 0.4, 0])), [5, 0, 0], 5e-3)

# =============================================================== 3.11
section("3.11 Coaxial cable with a graded core (2-D Coulomb sum of line elements, by rays)")
r011, a11, b11, c11 = 3e-6, 0.01, 0.02, 0.03
core = integrate.quad(lambda r: r011 * r / a11 * 2 * PI * r, 0, a11, epsabs=0)[0]
rho1 = core / (PI * (c11 ** 2 - b11 ** 2))
check("(a) core charge per length [nC/m]", core * 1e9, 0.628, 5e-4)
check("(a) rho_1 for neutrality [uC/m^3]", rho1 * 1e6, 0.4, 1e-9)
nph = 20000
phi = (np.arange(nph) + 0.5) * 2 * PI / nph
SH2 = np.stack([np.cos(phi), np.sin(phi)], axis=-1)


def chord2(P, R):
    pd = SH2 @ P
    disc = pd ** 2 - P @ P + R * R
    sq = np.sqrt(np.clip(disc, 0, None))
    ok = disc > 0
    return np.where(ok, np.clip(-pd - sq, 0, None), 0.0), np.where(ok, np.clip(-pd + sq, 0, None), 0.0)


def E11(r, shell=True):
    """(E_x, E_y) at (r, 0)."""
    P = np.array([r, 0.0])
    s1, s2 = chord2(P, a11)
    sm = np.clip(-(SH2 @ P), s1, s2)
    f = lambda S: r011 * np.hypot(P[0] + S * SH2[:, 0:1], P[1] + S * SH2[:, 1:2]) / a11
    L = chord_gl(s1, sm, f) + chord_gl(sm, s2, f)
    if shell:
        c1, c2 = chord2(P, c11)
        q1, q2 = chord2(P, b11)
        L = L - rho1 * ((c2 - c1) - (q2 - q1))
    return -(1 / (2 * PI * eps0)) * (2 * PI / nph) * (SH2 * L[:, None]).sum(axis=0)


def page11(r):
    if r < a11:
        return r011 * r * r / (3 * eps0 * a11)
    if r < b11:
        return r011 * a11 ** 2 / (3 * eps0 * r)
    if r < c11:
        return r011 * a11 ** 2 / (3 * eps0 * r) * (c11 ** 2 - r * r) / (c11 ** 2 - b11 ** 2)
    return 0.0


for r in [0.004, 0.008, 0.015, 0.022, 0.028, 0.035]:
    e = E11(r)
    check(f"(b) E_r at r = {r * 100:g} cm vs page formula [V/m]", e[0], page11(r), max(1e-4 * abs(e[0]), 1e-2))  # 1e-2 V/m ~ 3e-5 of the core field there
Ea11, Eb11, E25, E25core = E11(a11)[0], E11(b11)[0], E11(0.025)[0], E11(0.025, shell=False)[0]
check("(c) E(r = a) [V/m]", Ea11, 1129, 0.5)
check("(c) E(r = b) [V/m]", Eb11, 565, 0.5)
check("(c) core alone at 2.5 cm (= 'gap formula') [V/m]", E25core, 451.8, 0.05)
check("(c) shell factor E/E_core at 2.5 cm", E25 / E25core, 0.55, 1e-4)
check("(c) E(r = 2.5 cm) [V/m]", E25, 248.5, 0.05)
check("(c) E_y at 2.5 cm (radial field) [V/m]", E11(0.025)[1], 0, 1e-3)
rg = np.arange(0.001, 0.0296, 0.0005)
eg11 = np.array([E11(r)[0] for r in rg])
check("(c) r of max |E| on a 0.5 mm scan [cm]", rg[np.argmax(np.abs(eg11))] * 100, 1.0, 1e-9)
rs11 = -core / (2 * PI * b11)
check("(d) rho_s on r = b [nC/m^2]", rs11 * 1e9, -5, 1e-9)


def E_cylsheet(r, rs, R):
    """E_x at (r,0) of a cylindrical sheet of radius R: 2-D Coulomb sum over line elements."""
    f = lambda pp: rs * R / (2 * PI * eps0) * (r - R * np.cos(pp)) / ((r - R * np.cos(pp)) ** 2 + (R * np.sin(pp)) ** 2)
    return integrate.quad(f, 0, 2 * PI, limit=200)[0]


check("(d) core + sheet at r = 2.5 cm [V/m]", E25core + E_cylsheet(0.025, rs11, b11), 0, 1e-2)
check("(d) sheet alone at r = 1.5 cm (inside it) [V/m]", E_cylsheet(0.015, rs11, b11), 0, 1e-6)

# =============================================================== 3.12
section("3.12 Flux bookkeeping, line and sheet (D in nC/m^2, flux in nC; midpoint surface integrals)")
rt, zt = 0.7, 1.3
Dl = integrate.quad(lambda zp: 6 / (4 * PI) * rt / (rt ** 2 + zp ** 2) ** 1.5, -np.inf, np.inf)[0]
Ds = integrate.quad(lambda s: 4 / (4 * PI) * zt * 2 * PI * s / (s * s + zt * zt) ** 1.5, 0, np.inf)[0]
check("(a) line, Coulomb: D_r at r = 0.7 m vs 6/(2 pi r) [nC/m^2]", Dl, 6 / (2 * PI * rt), 1e-8)
check("(a) sheet, Coulomb: D_z above the sheet vs +2 [nC/m^2]", Ds, 2, 1e-8)


def D12(p):
    x, y, z = p[..., 0], p[..., 1], p[..., 2]
    r2 = x * x + y * y
    return np.stack([6 * x / (2 * PI * r2), 6 * y / (2 * PI * r2), 2 * np.sign(z)], axis=-1)


M = 400
mid = lambda lo, hi: lo + (np.arange(M) + 0.5) * (hi - lo) / M


def flux12(X, N, dA):
    return float(np.sum(np.sum(D12(X) * N, axis=-1) * dA))


R_, P_ = np.meshgrid(mid(0, 1), mid(0, 2 * PI), indexing="ij")


def disk12(zc, nsign):
    X = np.stack([R_ * np.cos(P_), R_ * np.sin(P_), np.full_like(R_, zc)], axis=-1)
    N = np.zeros_like(X)
    N[..., 2] = nsign
    return flux12(X, N, R_ * (1 / M) * (2 * PI / M))


top_b, bot_b = disk12(2.0, 1), disk12(-1.0, -1)
Ph_, Z_ = np.meshgrid(mid(0, 2 * PI), mid(-1, 2), indexing="ij")
Xs = np.stack([np.cos(Ph_), np.sin(Ph_), Z_], axis=-1)
Ns = np.stack([np.cos(Ph_), np.sin(Ph_), 0 * Z_], axis=-1)
side_b = flux12(Xs, Ns, np.full_like(Z_, (2 * PI / M) * (3 / M)))
check("(b) top cap [nC] (2 pi)", top_b, 6.28, 5e-3)
check("(b) bottom cap [nC] (2 pi)", bot_b, 6.28, 5e-3)
check("(b) curved side [nC]", side_b, 18, 1e-6)
check("(b) total [nC]", top_b + bot_b + side_b, 30.57, 5e-3)
check("(b) total vs Q_enc = 6*3 + 4*pi*1^2 [nC]", top_b + bot_b + side_b, 18 + 4 * PI, 1e-6)
U_, V_ = np.meshgrid(mid(-1, 1), mid(-1, 1), indexing="ij")
Y_, Zc_ = np.meshgrid(mid(-1, 1), mid(1, 3), indexing="ij")
dA4 = (2 / M) * (2 / M)
one = np.ones_like(U_)
faces = {
    "top z=3": (np.stack([U_, V_, 3 * one], -1), [0, 0, 1], 8),
    "bottom z=1": (np.stack([U_, V_, 1 * one], -1), [0, 0, -1], -8),
    "+x": (np.stack([one, Y_, Zc_], -1), [1, 0, 0], 3),
    "-x": (np.stack([-one, Y_, Zc_], -1), [-1, 0, 0], 3),
    "+y": (np.stack([Y_, one, Zc_], -1), [0, 1, 0], 3),
    "-y": (np.stack([Y_, -one, Zc_], -1), [0, -1, 0], 3),
}
tot_c = 0.0
for name, (X, n, page) in faces.items():
    fl = flux12(X, np.broadcast_to(np.array(n, float), X.shape), dA4)
    tot_c += fl
    check(f"(c) cube face {name} [nC]", fl, page, 1e-4)
check("(c) cube total [nC]", tot_c, 12, 1e-4)
Th_, Pd_ = np.meshgrid(mid(0, PI / 2), mid(0, 2 * PI), indexing="ij")
nd = np.stack([np.sin(Th_) * np.cos(Pd_), np.sin(Th_) * np.sin(Pd_), np.cos(Th_)], axis=-1)
dome12 = flux12(nd + np.array([0, 0, 1.0]), nd, np.sin(Th_) * (PI / 2 / M) * (2 * PI / M))
disk_z1 = disk12(1.0, -1)
check("(d) dome flux, direct surface integral [nC]", dome12, 12.28, 5e-3)
check("(d) dome flux vs 6 + 2 pi [nC]", dome12, 6 + 2 * PI, 1e-4)
check("(d) closing disk z = 1 (outward -z) [nC]", disk_z1, -2 * PI, 1e-6)
check("(d) dome + disk = Q_enc (line, 1 m) [nC]", dome12 + disk_z1, 6, 1e-4)
pt = np.array([[0.3, 0.4, np.sqrt(1 - 0.25) + 1], [0.05, 0.0, np.sqrt(1 - 0.0025) + 1]])
nn = pt - np.array([0, 0, 1.0])
Dline_n = np.sum(np.stack([6 * pt[:, 0] / (2 * PI * (pt[:, 0] ** 2 + pt[:, 1] ** 2)),
                           6 * pt[:, 1] / (2 * PI * (pt[:, 0] ** 2 + pt[:, 1] ** 2)), 0 * pt[:, 0]], -1) * nn, -1)
check("Check: line's D.n on the dome is 6/(2 pi) everywhere [nC/m^2]", Dline_n, 6 / (2 * PI), 1e-12)

print(f"\nSUMMARY: {NP[0]} PASS, {NP[1]} FAIL")
