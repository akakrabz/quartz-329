#!/usr/bin/env python3
"""R05 -- independent re-solution of content-src/practice/05-electrostatic-potential.md.

numpy/scipy only. Every number on the page is recomputed from the problem data, by a
brute-force route where possible (numerical line integrals along explicit paths,
finite-difference curl/grad, numerical Coulomb sums over the charge distribution,
superposition of sheets/filaments, an ODE for the electron, all 24 assembly orders),
then compared with the value transcribed from the page (PASS/FAIL per quantity).
"""
import itertools
import warnings

import numpy as np
from scipy import integrate, optimize

warnings.simplefilter("ignore", integrate.IntegrationWarning)

EPS0 = 8.8541878128e-12
K_EX = 1 / (4 * np.pi * EPS0)  # exact Coulomb constant
K9 = 9e9                        # the page's rounded constant
QE = 1.602176634e-19
ME = 9.11e-31                   # electron mass as used on the page

NFAIL = 0
NCHECK = 0


def check(label, got, page, rtol=5e-3, atol=0.0):
    """Compare a computed value (scalar or vector) with the value stated on the page."""
    global NFAIL, NCHECK
    g = np.atleast_1d(np.asarray(got, float))
    p = np.atleast_1d(np.asarray(page, float))
    ok = bool(np.allclose(g, p, rtol=rtol, atol=atol))
    NCHECK += 1
    NFAIL += not ok
    fmt = lambda v: (np.array2string(v, precision=6, separator=", ") if v.size > 1 else f"{v[0]:.6g}")
    print(f"  {'PASS' if ok else 'FAIL'}  {label}: computed {fmt(g)} | page {fmt(p)}")


def section(title):
    print(f"\n=== {title}")


# ---------------------------------------------------------------- generic tools
def polyline(Efun, pts):
    """Line integral of E along straight segments through the points, in order."""
    tot = 0.0
    for p, q in zip(pts[:-1], pts[1:]):
        p, q = np.asarray(p, float), np.asarray(q, float)
        tot += integrate.quad(lambda t: float(np.dot(Efun(p + t * (q - p)), q - p)), 0, 1,
                              limit=200, epsabs=1e-13, epsrel=1e-12)[0]
    return tot


def path_integral(Efun, path, h=1e-6):
    """Line integral of E along a parametrised path r(t), t in [0, 1] (numerical r'(t))."""
    def f(t):
        dr = (np.asarray(path(t + h)) - np.asarray(path(t - h))) / (2 * h)
        return float(np.dot(Efun(np.asarray(path(t))), dr))
    return integrate.quad(f, 0, 1, limit=400, epsabs=1e-12, epsrel=1e-11)[0]


def curl_fd(Efun, r, h=1e-5):
    r = np.asarray(r, float)
    J = np.zeros((3, 3))  # J[i, j] = dE_i / dx_j
    for j in range(3):
        dr = np.zeros(3)
        dr[j] = h
        J[:, j] = (np.asarray(Efun(r + dr)) - np.asarray(Efun(r - dr))) / (2 * h)
    return np.array([J[2, 1] - J[1, 2], J[0, 2] - J[2, 0], J[1, 0] - J[0, 1]])


def grad_fd(Vfun, r, h=1e-6):
    r = np.asarray(r, float)
    g = np.zeros(3)
    for j in range(3):
        dr = np.zeros(3)
        dr[j] = h
        g[j] = (Vfun(r + dr) - Vfun(r - dr)) / (2 * h)
    return g


def coulomb_E(charges, r, k=K9):
    r = np.asarray(r, float)
    E = np.zeros(3)
    for q, p in charges:
        R = r - np.asarray(p, float)
        E += k * q * R / np.linalg.norm(R) ** 3
    return E


def coulomb_V(charges, r, k=K9):
    r = np.asarray(r, float)
    return sum(k * q / np.linalg.norm(r - np.asarray(p, float)) for q, p in charges)


def V_from_inf(charges, P, u, k=K9):
    """V(P) = -int_inf^P E.dl along the straight ray P + s*u, s from inf down to 0."""
    u = np.asarray(u, float) / np.linalg.norm(u)
    return integrate.quad(lambda s: float(np.dot(coulomb_E(charges, P + s * u, k), u)),
                          0, np.inf, limit=400)[0]


# =============================================================================
section("5.1  uniform E = 50 x V/m, a = (1,2,0), b = (4,-2,0)")
E51 = lambda r: np.array([50.0, 0.0, 0.0])
a51, b51 = np.array([1.0, 2, 0]), np.array([4.0, -2, 0])
wig = lambda t: a51 + t * (b51 - a51) + np.array([0.7 * np.sin(3 * np.pi * t),
                                                  0.5 * np.sin(2 * np.pi * t),
                                                  0.4 * np.sin(np.pi * t)])
dV51 = -polyline(E51, [a51, b51])
check("V(b)-V(a), straight path [V]", dV51, -150)
check("V(b)-V(a), staircase via (1,-2,0) [V]", -polyline(E51, [a51, [1, -2, 0], b51]), -150)
check("V(b)-V(a), wiggly 3-D path [V]", -path_integral(E51, wig), -150)
check("staircase first leg (along -y) contributes [V]", -polyline(E51, [a51, [1, -2, 0]]), 0, atol=1e-12)
check("int_a^b E.dl = drop V(a)-V(b), distractor (a) [V]", -dV51, 150)
check("|r_b - r_a| [m]", np.linalg.norm(b51 - a51), 5)
check("-E|r_b - r_a|, distractor (c) [V]", -50 * np.linalg.norm(b51 - a51), -250)
print("  keyed answer (b) -150 V is the computed value; V(b) < V(a) since b is 3 m further along E")

# =============================================================================
section("5.2  Q1 = 2 nC at O, Q2 = -4 nC at (0.6,0,0), Q3 = 3 nC at (0,0.8,0); P = (0.6,0.8,0)")
ch52 = [(2e-9, (0, 0, 0)), (-4e-9, (0.6, 0, 0)), (3e-9, (0, 0.8, 0))]
P52 = np.array([0.6, 0.8, 0])
check("R1, R2, R3 [m]", [np.linalg.norm(P52 - np.array(p)) for _, p in ch52], [1, 0.8, 0.6])
V52 = coulomb_V(ch52, P52)
check("(a) V(P), k = 9e9 [V]", V52, 18)
check("(a) V(P), exact k [V]", coulomb_V(ch52, P52, K_EX), 17.98, rtol=3e-4)
for u in ([0.6, 0.8, 0], [0, 0, 1], [1, -1, 0.5]):
    check(f"(a) V(P) = -int E.dl in from infinity along ray {u} [V]", V_from_inf(ch52, P52, u), 18, rtol=1e-7)
W52 = -1 * (V52 - 0)  # q = -e, in eV
check("(b) agent work q[V(P)-V(inf)] [eV]", W52, -18)
check("(b) agent work [J]", W52 * QE, -2.88e-18, rtol=2e-3)
s = np.concatenate(([0.0], np.logspace(-4, 4, 4000)))
Vray = np.array([coulomb_V(ch52, P52 + si * np.array([0.6, 0.8, 0])) for si in s])
print(f"  claim 'agent holds it back the whole way': on the radial ray V is monotonic: {bool(np.all(np.diff(Vray) < 0))}")
Vnear = coulomb_V(ch52, [0.7, 0.05, 0])
print(f"  but V(0.7,0.05,0) = {Vnear:.1f} V < 0: a route past Q2 raises U = -eV to {-Vnear:.0f} eV, so there the agent"
      " must PUSH -> 'the whole way' is path-dependent (only the total -18 eV is not)")

# =============================================================================
section("5.3  true / false")
ch53 = [(1e-9, (-0.1, 0, 0)), (-1e-9, (0.1, 0, 0))]
check("(b) V at origin of the +-1 nC pair [V]", coulomb_V(ch53, [0, 0, 0], K_EX), 0, atol=1e-12)
check("(b) E at origin (vector) [V/m]", coulomb_E(ch53, [0, 0, 0], K_EX), [1798, 0, 0], rtol=3e-4, atol=1e-9)
check("(b) 2kq/d^2 with q = 1 nC, d = 0.1 m [V/m]", 2 * K_EX * 1e-9 / 0.1 ** 2, 1798, rtol=3e-4)
Q53, a53 = 1e-9, 0.2
sig53 = Q53 / (4 * np.pi * a53 ** 2)


def V_shell(zp):
    f = lambda th: K_EX * sig53 * 2 * np.pi * a53 ** 2 * np.sin(th) / np.sqrt(a53 ** 2 + zp ** 2 - 2 * a53 * zp * np.cos(th))
    return integrate.quad(f, 0, np.pi, limit=200)[0]


for zp in (0.0, 0.07, 0.15, 0.19):
    check(f"(c) V inside shell, {zp} m from centre (ring sum) [V]", V_shell(zp), 44.94, rtol=2e-4)
E53d = lambda r: np.array([np.sin(r[1]), np.cos(r[0]), 0.0])
c53 = curl_fd(E53d, [0.3, 0.7, 0])
check("(d) curl_z at (0.3,0.7,0), finite difference [V/m^2]", c53[2], -1.06, rtol=5e-3)
check("(d) page formula -sin x - cos y vs FD", -np.sin(0.3) - np.cos(0.7), c53[2], rtol=1e-6)
hl = 1e-3
sq = [[0.3, 0.7, 0], [0.3 + hl, 0.7, 0], [0.3 + hl, 0.7 + hl, 0], [0.3, 0.7 + hl, 0], [0.3, 0.7, 0]]
check("(d) circulation / area of a 1 mm CCW square [V/m^2]", polyline(E53d, sq) / hl ** 2, -1.06, rtol=5e-3)
dV_p, dV_e = -10.0 * 1e-3, -10.0 * (-1e-3)
check("(e) dV, proton 1 mm along +x [V]", dV_p, -0.01)
check("(e) dV, electron 1 mm along -x [V]", dV_e, 0.01)
check("(e) dU proton = e dV [J]", QE * dV_p, -1.6e-21, rtol=2e-3)
check("(e) dU electron = -e dV [J]", -QE * dV_e, -1.6e-21, rtol=2e-3)
print("  verdicts recomputed: (a) T, (b) F, (c) F, (d) F, (e) T -> two true, as the hint says")

# =============================================================================
section("5.4  V = 2x^2 y - 3yz + 5, P = (1,2,-1)")
V54 = lambda r: 2 * r[0] ** 2 * r[1] - 3 * r[1] * r[2] + 5
V54v = lambda R: 2 * R[:, 0] ** 2 * R[:, 1] - 3 * R[:, 1] * R[:, 2] + 5
P54 = np.array([1.0, 2, -1])
g54 = grad_fd(V54, P54)
check("grad V(P) [V/m]", g54, [8, 5, -6], atol=1e-6)
check("(a) E(P) = -grad V [V/m]", -g54, [-8, -5, 6], atol=1e-6)
check("(a) |E|^2", g54 @ g54, 125, rtol=1e-8)
check("(a) |E| [V/m]", np.linalg.norm(g54), 11.18, rtol=5e-4)
check("(b) grad V / |grad V|", g54 / np.linalg.norm(g54), [0.716, 0.447, -0.537], atol=6e-4)
U = np.random.default_rng(0).normal(size=(400000, 3))
U /= np.linalg.norm(U, axis=1)[:, None]
dd = (V54v(P54 + 1e-5 * U) - V54v(P54 - 1e-5 * U)) / 2e-5
check("(b) best of 4e5 random directions (brute-force steepest ascent)", U[np.argmax(dd)], [0.716, 0.447, -0.537], atol=6e-3)
check("(b) its rate [V/m]", dd.max(), 11.18, rtol=1e-3)
t54 = np.cross(g54, [0, 0, 1.0])
t54 /= np.linalg.norm(t54)
check("(b) dV along a tangent of the equipotential [V/m]", (V54(P54 + 1e-6 * t54) - V54(P54 - 1e-6 * t54)) / 2e-6, 0, atol=1e-6)
check("check: dV/dz at P [V/m]", g54[2], -6, atol=1e-6)

# =============================================================================
section("5.5  find the error: Q = 1 nC, r = 0.3 m")
Q55, r55 = 1e-9, 0.3
grid = np.geomspace(1e9, r55, 400001)  # an explicit inward walk from far away
mid = 0.5 * (grid[1:] + grid[:-1])
walk = -np.sum(K9 * Q55 / mid ** 2 * np.diff(grid)) + K9 * Q55 / 1e9  # -sum E.dl with dl = actual (negative) steps
check("V(0.3 m), inward walk with dl = actual step [V]", walk, 30, rtol=1e-6)
check("V(0.3 m), -int_inf^r E dr' as int_r^inf [V]", integrate.quad(lambda r: K9 * Q55 / r ** 2, r55, np.inf)[0], 30)
check("V(0.3 m), exact k [V]", K_EX * Q55 / r55, 29.96, rtol=2e-4)
check("student's result (direction counted twice) [V]", -integrate.quad(lambda r: K9 * Q55 / r ** 2, r55, np.inf)[0], -30)
Vr = lambda r: K9 * Q55 / r
check("check: -dV/dr at 0.3 m [V/m]", -(Vr(r55 + 1e-7) - Vr(r55 - 1e-7)) / 2e-7, 100, rtol=1e-6)

# =============================================================================
section("5.6  E+- = 3x^2 y x +- x^3 y, O -> P = (1,2,0)")
Ep = lambda r: np.array([3 * r[0] ** 2 * r[1], r[0] ** 3, 0.0])
Em = lambda r: np.array([3 * r[0] ** 2 * r[1], -r[0] ** 3, 0.0])
O6, P6 = np.zeros(3), np.array([1.0, 2, 0])
C1 = [O6, [1, 0, 0], P6]
C2 = [O6, [0, 2, 0], P6]
C3 = [O6, P6]
for pt in ([0.3, 0.5, 0.2], [1.1, -0.4, 0.7]):
    check(f"(a) curl E+ at {pt}", curl_fd(Ep, pt), [0, 0, 0], atol=1e-6)
    check(f"(a) curl E- at {pt} vs -6x^2 z", curl_fd(Em, pt), [0, 0, -6 * pt[0] ** 2], atol=1e-6)
check("(b) E+ on C1, C2, C3 [V]", [polyline(Ep, C) for C in (C1, C2, C3)], [2, 2, 2], atol=1e-9)
check("(b) E- on C1, C2, C3 [V]", [polyline(Em, C) for C in (C1, C2, C3)], [-2, 2, 1], atol=1e-9)
check("(b) E+ C1 legs [V]", [polyline(Ep, C1[:2]), polyline(Ep, C1[1:])], [0, 2], atol=1e-9)
V6 = lambda r: -r[0] ** 3 * r[1]
check("(c) -grad(-x^3 y) = E+ at (0.7,1.3,0.2)", -grad_fd(V6, [0.7, 1.3, 0.2]), Ep(np.array([0.7, 1.3, 0.2])), atol=1e-6)
check("(c) V(P)-V(O) from page V [V]", V6(P6) - V6(O6), -2)
check("(c) V(P)-V(O) = -int E+ on a curved 3-D path [V]",
      -path_integral(Ep, lambda t: np.array([t, 2 * t ** 3, 0.3 * np.sin(np.pi * t)])), -2, atol=1e-7)
area = lambda pts: 0.5 * sum(np.cross(p, q)[2] for p, q in zip(pts, pts[1:] + pts[:1]))
print(f"  signed area O->(1,0)->P: {area([np.zeros(3), np.array([1.0, 0, 0]), P6]):+.1f} (>0: CCW seen from +z)")
check("(d) closed loop C1 out, C3 back [V]", polyline(Em, [O6, [1, 0, 0], P6, O6]), -3, atol=1e-9)
check("(d) flux of curl E- through lower triangle, +z [V]",
      integrate.dblquad(lambda y, x: curl_fd(Em, [x, y, 0])[2], 0, 1, lambda x: 0, lambda x: 2 * x)[0], -3, rtol=1e-6)
print(f"  signed area O->(0,2)->P: {area([np.zeros(3), np.array([0.0, 2, 0]), P6]):+.1f} (<0: clockwise)")
check("check: loop C2 out, C3 back [V]", polyline(Em, [O6, [0, 2, 0], P6, O6]), 1, atol=1e-9)
fu = integrate.dblquad(lambda y, x: curl_fd(Em, [x, y, 0])[2], 0, 1, lambda x: 2 * x, lambda x: 2)[0]
check("check: curl flux through upper triangle with +z [V]", fu, -1, rtol=1e-6)
check("check: ... with -z [V]", -fu, 1, rtol=1e-6)

# =============================================================================
section("5.7  uniform ball, a = 9 cm, Q = 1 nC")
a57, Q57 = 0.09, 1e-9
rho57 = Q57 / (4 / 3 * np.pi * a57 ** 3)


def V_ball(r, k=K9):
    """Brute-force Coulomb sum over the ball (rings in r', theta'), field point at distance r."""
    f = lambda th, rp: k * rho57 * 2 * np.pi * rp ** 2 * np.sin(th) / np.sqrt(
        max(r ** 2 + rp ** 2 - 2 * r * rp * np.cos(th), 1e-300))
    return integrate.dblquad(f, 0, a57, lambda rp: 0, lambda rp: np.pi, epsabs=1e-12, epsrel=1e-11)[0]


check("(c) V(a) [V]", V_ball(a57), 100, rtol=1e-6)
check("(c) V(a/2) [V]", V_ball(a57 / 2), 137.5, rtol=1e-6)
check("(c) V(0) [V]", V_ball(0.0), 150, rtol=1e-6)
check("(c) V(a), exact k [V]", V_ball(a57, K_EX), 99.86, rtol=2e-4)
check("(c) V(0), exact k [V]", V_ball(0.0, K_EX), 149.79, rtol=2e-4)
for r in (0.03, 0.06, 0.12, 0.2):
    Efd = -(V_ball(r + 5e-4) - V_ball(r - 5e-4)) / 1e-3  # h large enough to beat quadrature noise
    Epage = K9 * Q57 * r / a57 ** 3 if r <= a57 else K9 * Q57 / r ** 2
    check(f"(a) E_r({r} m): -dV/dr of brute-force V vs page formula [V/m]", Efd, Epage, rtol=1e-4)
for r in (0.0, 0.02, 0.07, 0.15):
    Vpage = K9 * Q57 / (2 * a57) * (3 - r ** 2 / a57 ** 2) if r <= a57 else K9 * Q57 / r
    check(f"(b) page V({r} m) vs brute force [V]", Vpage, V_ball(r), rtol=1e-6)
check("(d) proton work e[V(0)-0] [eV]", V_ball(0.0), 150, rtol=1e-6)
check("(d) ... [J]", V_ball(0.0) * QE, 2.40e-17, rtol=2e-3)

# =============================================================================
section("5.8  uniform cylinder, a = 2 cm, rho_l = 200 pi eps0")
a58 = 0.02
rhol58 = 200 * np.pi * EPS0
rho58 = rhol58 / (np.pi * a58 ** 2)
check("rho_l [nC/m]", rhol58 * 1e9, 5.56, rtol=1e-3)
check("rho_l/(2 pi eps0) [V]", rhol58 / (2 * np.pi * EPS0), 100, rtol=1e-12)


def dV_cyl(rP, rQ):
    """V(rP) - V(rQ) by superposing infinite line-charge filaments over the cross-section."""
    f = lambda ph, s: s * np.log(np.hypot(rP - s * np.cos(ph), s * np.sin(ph)) /
                                 np.hypot(rQ - s * np.cos(ph), s * np.sin(ph)))
    I = integrate.dblquad(f, 0, a58, lambda s: 0, lambda s: 2 * np.pi, epsabs=1e-15, epsrel=1e-10)[0]
    return -rho58 / (2 * np.pi * EPS0) * I


check("(c) V(0), ref V(a) = 0 [V]", dV_cyl(0, a58), 50, rtol=1e-5)
check("(c) V(2a), ref V(a) = 0 [V]", dV_cyl(2 * a58, a58), -69.31, rtol=1e-4)
check("(c) V(0) - V(2a) [V]", dV_cyl(0, 2 * a58), 119.31, rtol=1e-4)
for R, pg in ((1e3, -1082), (1e6, -1773), (1e9, -2464)):
    check(f"(d) V({R:g} m) - V(a) [V]", dV_cyl(R, a58), pg, rtol=4e-4)
check("(d) V(a), ref V(0) = 0 [V]", dV_cyl(a58, 0), -50, rtol=1e-5)
check("(d) V(2a), ref V(0) = 0 [V]", dV_cyl(2 * a58, 0), -119.31, rtol=1e-4)
for r in (0.005, 0.013, 0.03):
    Vpage = 50 * (1 - r ** 2 / a58 ** 2) if r <= a58 else -100 * np.log(r / a58)
    check(f"(b) page V({r} m) vs filament sum [V]", Vpage, dV_cyl(r, a58), rtol=1e-5)
for r in (0.01, 0.05):
    Efd = -(dV_cyl(r + 1e-6, a58) - dV_cyl(r - 1e-6, a58)) / 2e-6
    check(f"(a) E_r({r} m): -dV/dr of filament sum vs page [V/m]", Efd, 100 * r / a58 ** 2 if r < a58 else 100 / r, rtol=1e-4)

# =============================================================================
section("5.9  rectangle -1<=x<=2, 0<=y<=2; loop a -> c1 -> b -> c2 -> a")
A9, Cc1, B9, Cc2 = (np.array(v, float) for v in ([2, 2, 0], [2, 0, 0], [-1, 0, 0], [-1, 2, 0]))
loop9 = [A9, Cc1, B9, Cc2, A9]
vecA = 0.5 * sum(np.cross(p, q) for p, q in zip(loop9[:-1], loop9[1:]))
check("oriented vector area [m^2] (clockwise from +z -> dS = -z dA)", vecA, [0, 0, -6], atol=1e-12)
Ea9 = lambda r: np.array([3.0, 4, -2])
legs = [polyline(Ea9, [p, q]) for p, q in zip(loop9[:-1], loop9[1:])]
check("(a) legs a->c1, c1->b, b->c2, c2->a [V]", legs, [-8, -9, 8, 9], atol=1e-9)
check("(a) circulation [V]", sum(legs), 0, atol=1e-9)
check("(a) V(b)-V(a) via C_R and via C_L [V]", [-polyline(Ea9, [A9, Cc1, B9]), -polyline(Ea9, [A9, Cc2, B9])], [17, 17])
cvec = np.array([2.0, -3, 5])
check("(b) curl . oriented vector area [V]", cvec @ vecA, -30)
Ec9 = lambda r: np.array([-(2.5 * r[1] + 1.5 * r[2]), 2.5 * r[0] - r[2], 1.5 * r[0] + r[1]])
for pt in ([0.3, -0.7, 1.1], [2.0, 1.0, -0.5]):
    check(f"(c) FD curl E at {pt} [V/m^2]", curl_fd(Ec9, pt), cvec, atol=1e-6)
    check(f"check: E = (1/2) c x r at {pt}", Ec9(np.array(pt)), 0.5 * np.cross(cvec, pt), atol=1e-12)
check("(b) flux of FD curl through rectangle, dS = -z dA [V]",
      integrate.dblquad(lambda y, x: -curl_fd(Ec9, [x, y, 0])[2], -1, 2, lambda x: 0, lambda x: 2)[0], -30, rtol=1e-6)
check("(c) C_R legs a->c1, c1->b [V]", [polyline(Ec9, [A9, Cc1]), polyline(Ec9, [Cc1, B9])], [-10, 0], atol=1e-9)
check("(c) C_L legs a->c2, c2->b [V]", [polyline(Ec9, [A9, Cc2]), polyline(Ec9, [Cc2, B9])], [15, 5], atol=1e-9)
ICR, ICL = polyline(Ec9, [A9, Cc1, B9]), polyline(Ec9, [A9, Cc2, B9])
check("(c) int_a^b along C_R, along C_L [V]", [ICR, ICL], [-10, 20])
check("(c) C_R - C_L and direct closed loop [V]", [ICR - ICL, polyline(Ec9, loop9)], [-30, -30])
rR, rL = polyline(Ec9, [B9, Cc1, A9]), polyline(Ec9, [B9, Cc2, A9])
check("(d) readings int_b^a along C_R, C_L [V]", [rR, rL], [10, -20])
check("(d) difference = |circulation| [V]", rR - rL, 30)
check("(d) in the field of (a) both meters read [V]", [polyline(Ea9, [B9, Cc1, A9]), polyline(Ea9, [B9, Cc2, A9])], [17, 17])

# =============================================================================
section("5.10  slab 0<x<2 m with rho0 = 6 eps0, sheet rho_s = -rho0 d at x = 0")
d10, rho0 = 2.0, 6 * EPS0
rhos10 = -rho0 * d10
check("rho0 [pC/m^3]", rho0 * 1e12, 53.1, rtol=1e-3)
check("rho_s [pC/m^2]", rhos10 * 1e12, -106, rtol=3e-3)


def E10(x):
    """E_x by superposing infinite sheets: the slab's layers rho0 dx' plus the sheet at x = 0."""
    pts = [x] if 0 < x < d10 else None
    slab = integrate.quad(lambda xp: rho0 / (2 * EPS0) * np.sign(x - xp), 0, d10, points=pts, epsabs=1e-13)[0]
    return slab + rhos10 / (2 * EPS0) * np.sign(x)


def V10(x):  # V(0) = 0, V(x) = -int_0^x E dx'
    if x < 0:
        return integrate.quad(E10, x, 0)[0]
    return -integrate.quad(E10, 0, x, points=[d10] if x > d10 else None, epsabs=1e-12)[0]


check("(a) E_x at x = -3, -0.5, 2.5, 7 m [V/m]", [E10(x) for x in (-3, -0.5, 2.5, 7)], [0, 0, 0, 0], atol=1e-9)
check("(a) E_x(x) at 0.3, 1, 1.7 vs 6(x-2) [V/m]", [E10(x) for x in (0.3, 1, 1.7)], [6 * (x - 2) for x in (0.3, 1, 1.7)], rtol=1e-8)
check("(a) E_x(0+) [V/m]", E10(1e-12), -12, rtol=1e-8)
check("(b) V at 0.5, 1, 2, 3 m [V]", [V10(x) for x in (0.5, 1, 2, 3)], [5.25, 9, 12, 12], rtol=1e-7)
check("(b) V(-1.5 m) [V]", V10(-1.5), 0, atol=1e-9)
check("(b) page 12x - 3x^2 vs numeric at 0.8, 1.6 [V]", [12 * x - 3 * x ** 2 for x in (0.8, 1.6)], [V10(0.8), V10(1.6)], rtol=1e-7)
check("(b) rho0 d^2/(2 eps0) [V]", rho0 * d10 ** 2 / (2 * EPS0), 12, rtol=1e-12)
check("check: pillbox eps0[E(0+)-E(0-)] = rho_s [C/m^2]", EPS0 * (E10(1e-12) - E10(-1e-12)), rhos10, rtol=1e-8)
F0 = -QE * E10(1e-12)
check("(c) force on electron at 0+ (x comp) [N]", F0, 1.92e-18, rtol=2e-3)
Kc = integrate.quad(lambda x: -QE * E10(x), 0, d10)[0]
check("(c) K = int F dx over the slab [eV]", Kc / QE, 12, rtol=1e-8)
check("(c) K [J]", Kc, 1.92e-18, rtol=2e-3)
hit = lambda t, y: y[0] - d10
hit.terminal, hit.direction = True, 1
sol = integrate.solve_ivp(lambda t, y: [y[1], -QE * E10(y[0]) / ME], (0, 1e-4), [1e-12, 0.0],
                          events=hit, rtol=1e-10, atol=[1e-14, 1e-6])
check("(c) speed at x = d from the equation of motion [m/s]", sol.y_events[0][0][1], 2.05e6, rtol=2.5e-3)
print(f"  E_x < 0 on the whole slab interior: {all(E10(x) < 0 for x in np.linspace(0.01, 1.99, 50))} -> pushed along +x all the way")
E10d = lambda r: np.array([r[1] * np.cos(r[0]), np.sin(r[0]), -2 * r[2]])
for pt in ([0.4, -1.3, 0.8], [2.2, 0.5, -1.0]):
    check(f"(d) FD curl at {pt}", curl_fd(E10d, pt), [0, 0, 0], atol=1e-6)
Bp = np.array([np.pi / 2, 2, 1])
I10 = polyline(E10d, [np.zeros(3), Bp])
check("(d) int_O^B E.dl, straight line [V]", I10, 1)
st = [np.zeros(3), np.array([np.pi / 2, 0, 0]), np.array([np.pi / 2, 2, 0]), Bp]
check("(d) staircase legs [V]", [polyline(E10d, [p, q]) for p, q in zip(st[:-1], st[1:])], [0, 2, -1], atol=1e-9)
check("(d) V(B) = 5 - int [V]", 5 - I10, 4)
V10d = lambda r: 5 - r[1] * np.sin(r[0]) + r[2] ** 2
check("(d) -grad(page V) = E at (0.4,-1.3,0.8)", -grad_fd(V10d, [0.4, -1.3, 0.8]), E10d(np.array([0.4, -1.3, 0.8])), atol=1e-6)
check("(d) page V(B) [V]", V10d(Bp), 4)
check("(d) agent work q[V(B)-V(O)] [J]", 2e-6 * (-I10), -2e-6)

# =============================================================================
section("5.11  annulus a = 5 cm, b = 9 cm, rho_s = 1000 eps0, on the z axis")
a511, b511 = 0.05, 0.09
rs511 = 1000 * EPS0
check("rho_s [nC/m^2]", rs511 * 1e9, 8.85, rtol=1e-3)
OPT = dict(epsabs=1e-13, epsrel=1e-10)


def V_ann(x, z, a=a511, b=b511):
    """Brute-force 2-D Coulomb sum for V at (x, 0, z)."""
    f = lambda ph, rp: K_EX * rs511 * rp / np.sqrt((x - rp * np.cos(ph)) ** 2 + (rp * np.sin(ph)) ** 2 + z ** 2)
    return integrate.dblquad(f, a, b, lambda rp: 0, lambda rp: 2 * np.pi, **OPT)[0]


def E_ann(z, a=a511, b=b511, comps=(0, 1, 2)):
    """Brute-force Coulomb vector sum for E at (0, 0, z)."""
    out = []
    for c in comps:
        def f(ph, rp, c=c):
            R = np.array([-rp * np.cos(ph), -rp * np.sin(ph), z])
            return K_EX * rs511 * rp * R[c] / np.linalg.norm(R) ** 3
        out.append(integrate.dblquad(f, a, b, lambda rp: 0, lambda rp: 2 * np.pi, **OPT)[0])
    return np.array(out)


check("(b) V(0) [V]", V_ann(0, 0), 20, rtol=1e-7)
check("(b) V(12 cm) [V]", V_ann(0, 0.12), 10, rtol=1e-7)
check("(a) page formula vs brute force at z = 0.07 m [V]",
      500 * (np.hypot(b511, 0.07) - np.hypot(a511, 0.07)), V_ann(0, 0.07), rtol=1e-7)
check("(b) E at z = 12 cm, Coulomb vector sum [V/m]", E_ann(0.12), [0, 0, 61.54], rtol=2e-4, atol=1e-8)
check("(b) -dV/dz at 12 cm from brute-force V [V/m]", -(V_ann(0, 0.12 + 1e-6) - V_ann(0, 0.12 - 1e-6)) / 2e-6, 61.54, rtol=2e-4)
check("(b) E at the centre [V/m]", E_ann(0.0), [0, 0, 0], atol=1e-8)
check("(b) E_x on axis from -dV/dx [V/m]", -(V_ann(1e-6, 0.12) - V_ann(-1e-6, 0.12)) / 2e-6, 0, atol=1e-5)
zmax = optimize.minimize_scalar(lambda z: -V_ann(0, z), bounds=(-0.3, 0.3), method="bounded", options={"xatol": 1e-7})
check("(b,d) V on the axis peaks at z = 0 with V = 20 V", [zmax.x, -zmax.fun], [0, 20], atol=1e-5)
check("(c) full disk at z = 3 cm: Coulomb sum vs page formula [V/m]",
      E_ann(0.03, a=0.0, comps=(2,))[0], 500 * (1 - 0.03 / np.hypot(b511, 0.03)), rtol=1e-6)
check("(c) full disk near the sheet, z = 0.1 mm [V/m]", E_ann(1e-4, a=0.0, comps=(2,))[0], 500, rtol=2e-3)
Qd = np.pi * b511 ** 2 * rs511
check("(c) full disk far away, z = 20 m, vs point charge [V/m]", E_ann(20.0, a=0.0, comps=(2,))[0], K_EX * Qd / 400, rtol=1e-4)
Qa = np.pi * rs511 * (b511 ** 2 - a511 ** 2)
check("(c) annulus charge Q [C]", Qa, 1.56e-10, rtol=2e-3)
check("(c) point-charge estimate at 1 m [V]", K_EX * Qa / 1.0, 1.400, rtol=1e-4)
check("(c) brute-force V at 1 m [V]", V_ann(0, 1.0), 1.396, rtol=3e-4)
check("hint: int r' dr'/sqrt(r'^2+z^2) at z = 0.12",
      integrate.quad(lambda r: r / np.hypot(r, 0.12), a511, b511)[0], np.hypot(b511, 0.12) - np.hypot(a511, 0.12), rtol=1e-10)
check("(d) proton minimum K = e V(0) [eV]", V_ann(0, 0), 20, rtol=1e-7)
check("(d) ... [J]", V_ann(0, 0) * QE, 3.20e-18, rtol=2e-3)
Ke = QE * integrate.quad(lambda z: E_ann(z, comps=(2,))[0], 0, 0.12, epsabs=1e-10)[0]  # work of F = -eE over z: 0.12 -> 0
check("(d) electron K at the centre from int F.dl of the Coulomb field [eV]", Ke / QE, 10, rtol=1e-6)
check("(d) ... [J]", Ke, 1.60e-18, rtol=2e-3)
check("(d) electron speed [m/s]", np.sqrt(2 * Ke / ME), 1.88e6, rtol=3e-3)

# =============================================================================
section("5.12  four 2 nC charges on a 30 cm square, centred at O")
s12, q12 = 0.3, 2e-9
corners = [np.array([sx * s12 / 2, sy * s12 / 2, 0.0]) for sx, sy in ((1, 1), (-1, 1), (-1, -1), (1, -1))]
ch4 = [(q12, c) for c in corners]


def assemble(order, charges, k=K9):
    W, placed, steps = 0.0, [], []
    for i in order:
        qi, ri = charges[i]
        dW = qi * coulomb_V(placed, ri, k) if placed else 0.0
        steps.append(dW)
        W += dW
        placed.append(charges[i])
    return W, steps


def total_U(charges, k=K9):
    return sum(k * qi * qj / np.linalg.norm(np.asarray(ri) - np.asarray(rj))
               for (qi, ri), (qj, rj) in itertools.combinations(charges, 2))


def force_on(i, charges, k=K9):
    qi, ri = charges[i]
    return sum((k * qi * qj * (ri - rj) / np.linalg.norm(ri - rj) ** 3
                for j, (qj, rj) in enumerate(charges) if j != i), np.zeros(3))


Ws = [assemble(p, ch4)[0] for p in itertools.permutations(range(4))]
check("(a) W4 over all 24 orders, min and max [J]", [min(Ws), max(Ws)], [6.50e-7, 6.50e-7], rtol=1e-3)
kq2s = K9 * q12 ** 2 / s12
check("kq^2/s [J]", kq2s, 1.2e-7, rtol=1e-12)
W4, steps = assemble([0, 1, 2, 3], ch4)
check("(a) step costs going round the square / (kq^2/s)", np.array(steps) / kq2s,
      [0, 1, 1 + 1 / np.sqrt(2), 2 + 1 / np.sqrt(2)], rtol=1e-12, atol=1e-12)
check("(a) W4/(kq^2/s) = 4 + sqrt 2", W4 / kq2s, 5.414, rtol=1e-4)
Vc = coulomb_V(ch4, [0, 0, 0])
check("(b) corner-to-centre distance [m]", np.linalg.norm(corners[0]), 0.2121, rtol=2e-4)
check("(b) V at centre [V]", Vc, 339.4, rtol=2e-4)
Q12 = optimize.brentq(lambda Q: total_U(ch4 + [(Q, np.zeros(3))]), -1e-8, 0, xtol=1e-25, rtol=1e-15)
check("(c) Q giving zero total energy [nC]", Q12 * 1e9, -1.91, rtol=3e-3)
check("(c) Q/q = -(1/sqrt2 + 1/4)", Q12 / q12, -0.957, rtol=5e-4)
ch5 = ch4 + [(Q12, np.zeros(3))]
check("(d) net forces on the 4 corners and Q, max |F| [N]", max(np.linalg.norm(force_on(i, ch5)) for i in range(5)), 0, atol=1e-18)
Fc = force_on(0, ch4)
check("(d) other corners on corner (s/2,s/2): |F| [N]", np.linalg.norm(Fc), 7.66e-7, rtol=1e-3)
check("(d) ... its x, y components [N]", Fc[:2], [5.414e-7, 5.414e-7], rtol=1e-3)
check("(d) ... direction (outward diagonal)", Fc / np.linalg.norm(Fc), [1 / np.sqrt(2), 1 / np.sqrt(2), 0], atol=1e-12)
FQ = K9 * q12 * Q12 * corners[0] / np.linalg.norm(corners[0]) ** 3
check("(d) pull of Q on that corner: |F| [N]", np.linalg.norm(FQ), 7.66e-7, rtol=1e-3)
check("(d) ... x, y components [N]", FQ[:2], [-5.414e-7, -5.414e-7], rtol=1e-3)
check("kq^2/s^2 [N]", K9 * q12 ** 2 / s12 ** 2, 4e-7, rtol=1e-12)
check("(d) scaling: total energy at lambda = 0.5, 2, 3.7 [J]",
      [total_U([(qq, lam * rr) for qq, rr in ch5]) for lam in (0.5, 2.0, 3.7)], [0, 0, 0], atol=1e-18)

print(f"\n{NCHECK} checks, {NFAIL} FAIL")
