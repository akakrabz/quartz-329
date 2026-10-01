#!/usr/bin/env python3
"""Numerical verification of every number on practice/05-electrostatic-potential.md.

numpy/scipy only. Line integrals are done numerically along the stated paths,
gradients and curls by central finite differences, and V / E of continuous
charge by direct superposition integrals (independent of the closed forms).
"""
import numpy as np
from scipy import integrate

eps0 = 8.8541878128e-12
e = 1.602176634e-19
me = 9.1093837e-31
kx = 1 / (4 * np.pi * eps0)      # exact Coulomb constant
k9 = 9e9                          # course approximation

np.set_printoptions(precision=6, suppress=True)
ok_all = []


def check(label, got, want, rtol=1e-6, atol=1e-9):
    got = np.asarray(got, float)
    want = np.asarray(want, float)
    ok = np.allclose(got, want, rtol=rtol, atol=atol)
    ok_all.append(ok)
    print(f"  [{'OK' if ok else 'FAIL'}] {label}: computed {got}  expected {want}")
    return ok


# ---------------------------------------------------------------- helpers
def seg_integral(E, p0, p1):
    """int E . dl along the straight segment p0 -> p1 (numerical)."""
    p0 = np.asarray(p0, float)
    p1 = np.asarray(p1, float)
    d = p1 - p0
    f = lambda t: float(np.dot(np.asarray(E(*(p0 + t * d)), float), d))
    return integrate.quad(f, 0.0, 1.0, limit=200, epsabs=1e-12, epsrel=1e-12)[0]


def poly_integral(E, pts):
    return sum(seg_integral(E, a, b) for a, b in zip(pts[:-1], pts[1:]))


def param_integral(E, r, dr, t0, t1):
    f = lambda t: float(np.dot(np.asarray(E(*r(t)), float), dr(t)))
    return integrate.quad(f, t0, t1, limit=400, epsabs=1e-12, epsrel=1e-12)[0]


def grad_fd(V, p, h=1e-6):
    p = np.asarray(p, float)
    g = np.zeros(3)
    for i in range(3):
        dp = np.zeros(3)
        dp[i] = h
        g[i] = (V(*(p + dp)) - V(*(p - dp))) / (2 * h)
    return g


def curl_fd(E, p, h=1e-5):
    p = np.asarray(p, float)
    J = np.zeros((3, 3))
    for j in range(3):
        dp = np.zeros(3)
        dp[j] = h
        J[:, j] = (np.asarray(E(*(p + dp)), float) - np.asarray(E(*(p - dp)), float)) / (2 * h)
    return np.array([J[2, 1] - J[1, 2], J[0, 2] - J[2, 0], J[1, 0] - J[0, 1]])


def div_fd(E, p, h=1e-5):
    p = np.asarray(p, float)
    s = 0.0
    for j in range(3):
        dp = np.zeros(3)
        dp[j] = h
        s += (np.asarray(E(*(p + dp)), float)[j] - np.asarray(E(*(p - dp)), float)[j]) / (2 * h)
    return s


# =====================================================================
print("=" * 70)
print("5.1  Uniform field E = 50 x V/m, a = (1,2,0), b = (4,-2,0)")
E51 = lambda x, y, z: (50.0, 0.0, 0.0)
a51, b51 = (1, 2, 0), (4, -2, 0)
I_straight = seg_integral(E51, a51, b51)
I_stair = poly_integral(E51, [a51, (1, -2, 0), b51])
# a wiggly path: straight line plus a sine bump in y and z
r = lambda t: np.array([1 + 3 * t, 2 - 4 * t + 0.7 * np.sin(np.pi * t), 0.5 * np.sin(2 * np.pi * t)])
dr = lambda t: np.array([3.0, -4 + 0.7 * np.pi * np.cos(np.pi * t), np.pi * np.cos(2 * np.pi * t)])
I_wiggle = param_integral(E51, r, dr, 0, 1)
print(f"  int_a^b E.dl: straight {I_straight:.6f}, staircase {I_stair:.6f}, wiggly {I_wiggle:.6f} V")
check("V(b)-V(a) = -int (all paths)", [-I_straight, -I_stair, -I_wiggle], [-150, -150, -150])
dist = np.linalg.norm(np.subtract(b51, a51))
print(f"  distractor: |b-a| = {dist} m, 50*|b-a| = {50*dist} V  (option c = -250 V)")
check("curl of uniform field", curl_fd(E51, (0.3, 0.2, 0.1)), [0, 0, 0], atol=1e-6)
print(f"  [page] displacement b-a = {np.subtract(b51, a51)} m; staircase via (1,-2,0): legs "
      f"{seg_integral(E51, a51, (1, -2, 0)):.6f} V and {seg_integral(E51, (1, -2, 0), b51):.6f} V")

# =====================================================================
print("=" * 70)
print("5.2  Point charges, V(P) and work on an electron")
Q = np.array([2e-9, -4e-9, 3e-9])
pos = np.array([[0, 0, 0], [0.6, 0, 0], [0, 0.8, 0]], float)
P = np.array([0.6, 0.8, 0])
dists = np.linalg.norm(P - pos, axis=1)
print(f"  distances to P: {dists} m")
V9 = k9 * np.sum(Q / dists)
Vx = kx * np.sum(Q / dists)
print(f"  V(P) with 9e9: {V9:.6f} V ; with exact 1/(4 pi eps0): {Vx:.6f} V")
print(f"  [page] Q_i/R_i = {Q / dists * 1e9} nC/m, sum = {np.sum(Q / dists) * 1e9:.6f} nC/m; e = {e} C")
check("V(P) (9e9)", V9, 18.0)
# brute force: V(P) = -int_inf^P E.dl along a straight line from far away
def E_pts(x, y, z, Q=Q, pos=pos, k=k9):
    rr = np.array([x, y, z])
    out = np.zeros(3)
    for q, p in zip(Q, pos):
        d = rr - p
        out += k * q * d / np.linalg.norm(d) ** 3
    return out
def V_ray(Pt, E, u=(0.3, 0.5, 0.81)):
    """V(P) = -int_inf^P E.dl = +int_P^inf E.dl along an outward ray P + s*u_hat (s from 0 to inf)."""
    Pt = np.asarray(Pt, float)
    uh = np.asarray(u, float) / np.linalg.norm(u)
    f = lambda s: float(np.dot(E(*(Pt + s * uh)), uh))
    return integrate.quad(f, 0, np.inf, limit=400, epsabs=1e-12, epsrel=1e-12)[0]
V_brute = V_ray(P, E_pts)
print(f"  brute-force V(P) = -int_inf^P E.dl along a ray (9e9) = {V_brute:.6f} V")
check("V(P) brute force", V_brute, 18.0, rtol=1e-8)
W_eV = -1 * V9           # electron: q = -e, W = q V(P) -> in eV numerically -V
W_J = -e * V9
print(f"  work on electron: {W_eV:.4f} eV = {W_J:.6e} J (exact-k value {-e*Vx:.6e} J)")
check("W (J)", W_J, -2.88e-18, rtol=2e-3)

# =====================================================================
print("=" * 70)
print("5.3  True/false support computations")
# (b) +q at x=-d, -q at x=+d: V(0)=0 but E != 0
q, d = 1e-9, 0.1
V_mid = kx * q / d - kx * q / d
E_mid = kx * q / d**2 + kx * q / d**2       # both point +x (from + toward -)
print(f"  (b) V(mid) = {V_mid} V, E(mid) = {E_mid:.3f} V/m along +x (= 2q/(4 pi eps0 d^2))")
check("(b) E_mid formula", E_mid, 2 * kx * q / d**2)
Etot = E_pts(0, 0, 0, Q=np.array([q, -q]), pos=np.array([[-d, 0, 0], [d, 0, 0]]), k=kx)
check("(b) E_mid by vector sum", Etot, [E_mid, 0, 0])
# (c) uniformly charged shell: V inside is constant = Q/(4 pi eps0 a)  (brute-force surface integral)
Qs, a_s = 1e-9, 0.2
rho_s = Qs / (4 * np.pi * a_s**2)
def V_shell(z):
    f = lambda th: rho_s * 2 * np.pi * a_s**2 * np.sin(th) / np.sqrt(a_s**2 + z**2 - 2 * a_s * z * np.cos(th))
    return kx * integrate.quad(f, 0, np.pi, limit=200)[0]
vals = [V_shell(z) for z in (0.0, 0.05, 0.1, 0.15)]
print(f"  (c) V inside shell at z=0,0.05,0.1,0.15 m: {np.array(vals)} V; Q/(4 pi eps0 a) = {kx*Qs/a_s:.6f} V")
check("(c) V constant inside shell", vals, [kx * Qs / a_s] * 4, rtol=1e-6)
# (d) curl of sin(y) x + cos(x) y
E53 = lambda x, y, z: (np.sin(y), np.cos(x), 0.0)
for p in [(0.3, 0.7, 0), (1.2, -0.4, 2.0), (2.0, 1.0, 0)]:
    check(f"(d) curl at {p} = -(sin x + cos y) z", curl_fd(E53, p), [0, 0, -(np.sin(p[0]) + np.cos(p[1]))], atol=1e-7)
# (e) proton/electron in a sample field E = 10 x: force direction and sign of dU along the motion
Ef = np.array([10.0, 0, 0])
print(f"  [page] inputs: (b) q = {q} C, d = {d} m; (c) Q = {Qs} C, a = {a_s} m; (e) E = {Ef} V/m, step 1e-3 m along F")
for name, qq in (("proton", e), ("electron", -e)):
    F = qq * Ef
    step = 1e-3 * F / np.linalg.norm(F)     # move along the force
    dV = -np.dot(Ef, step)                  # dV = -E.dl
    dU = qq * dV
    print(f"  (e) {name}: moves along {np.sign(F[0]):+.0f} x, dV = {dV:+.4f} V (toward {'lower' if dV<0 else 'higher'} V), dU = {dU:+.3e} J (<0)")

# =====================================================================
print("=" * 70)
print("5.4  E = -grad V for V = 2x^2 y - 3yz + 5 at P = (1,2,-1)")
V54 = lambda x, y, z: 2 * x**2 * y - 3 * y * z + 5
P54 = (1, 2, -1)
g = grad_fd(V54, P54)
check("grad V at P", g, [8, 5, -6], atol=1e-6)
E54 = -g
print(f"  E(P) = {E54} V/m, |E| = {np.linalg.norm(E54):.6f} V/m (sqrt(125) = {np.sqrt(125):.6f})")
print(f"  [page] squares of components: {np.round(E54**2, 6)}, sum = {np.sum(E54**2):.6f}")
check("|E|", np.linalg.norm(E54), np.sqrt(125))
print(f"  dV/dz at P = {g[2]:.6f} V/m (V decreases 6 V/m along +z; E_z = {E54[2]:+.3f})")
print(f"  steepest ascent direction grad/|grad| = {g/np.linalg.norm(g)}, rate {np.linalg.norm(g):.4f} V/m")
# second point to test the closed form gradient (4xy, 2x^2-3z, -3y)
P2 = (-0.7, 1.3, 2.2)
check("grad V closed form at a second point", grad_fd(V54, P2),
      [4 * P2[0] * P2[1], 2 * P2[0]**2 - 3 * P2[2], -3 * P2[1]], atol=1e-6)

# =====================================================================
print("=" * 70)
print("5.5  Point-charge potential, Q = 1 nC at r = 0.3 m")
Q55, r55 = 1e-9, 0.3
# numerical V(r) = -int_inf^r E_r dr' with dl = r_hat dr' ; substitute r' = r/s, s in (0,1]
Er = lambda rp, k: k * Q55 / rp**2
def V_point(r, k):
    # -int_{inf}^{r} E dr' = int_r^inf E dr' ; with r' = r/u, dr' = -r/u^2 du, u: 1 -> 0
    f = lambda u: Er(r / u, k) * r / u**2
    return integrate.quad(f, 0, 1, limit=200)[0]
Vc9 = V_point(r55, k9)
Vcx = V_point(r55, kx)
print(f"  correct V(r) numeric: {Vc9:.6f} V (9e9), {Vcx:.6f} V (exact k); closed form kQ/r = {k9*Q55/r55:.6f}")
check("correct V(0.3 m)", Vc9, 30.0)
# student's version: dl = -r_hat dr' AND limits inf -> r  => integrand sign flipped twice
V_student = -Vc9
print(f"  student's (double-counted direction): {V_student:.6f} V")
check("student's value", V_student, -30.0)
# slope check: -dV/dr of correct V is +E_r (outward); of student's is inward
Vfun = lambda rr: k9 * Q55 / rr
h = 1e-6
print(f"  -dV/dr (correct) at r: {-(Vfun(r55+h)-Vfun(r55-h))/(2*h):.4f} V/m, E_r = {k9*Q55/r55**2:.4f} V/m")

# =====================================================================
print("=" * 70)
print("5.6  E = 3x^2 y x +/- x^3 y from O=(0,0,0) to P=(1,2,0)")
Ep = lambda x, y, z: (3 * x**2 * y, x**3, 0.0)
Em = lambda x, y, z: (3 * x**2 * y, -x**3, 0.0)
for p in [(0.4, 1.1, 0), (0.9, -0.3, 0.5), (1.5, 2.0, -1.0)]:
    check(f"curl E+ at {p}", curl_fd(Ep, p), [0, 0, 0], atol=1e-6)
    check(f"curl E- at {p} = -6x^2 z", curl_fd(Em, p), [0, 0, -6 * p[0]**2], atol=1e-6)
O, P6 = (0, 0, 0), (1, 2, 0)
C1 = [O, (1, 0, 0), P6]
C2 = [O, (0, 2, 0), P6]
res = {}
for name, E in (("E+", Ep), ("E-", Em)):
    i1 = poly_integral(E, C1)
    i2 = poly_integral(E, C2)
    i3 = seg_integral(E, O, P6)    # straight line y = 2x
    res[name] = (i1, i2, i3)
    print(f"  {name}: C1 = {i1:.6f}, C2 = {i2:.6f}, C3 (straight) = {i3:.6f} V")
    print(f"  [page] {name} legs: C1 [{seg_integral(E, O, (1, 0, 0)):.6f}, {seg_integral(E, (1, 0, 0), P6):.6f}], "
          f"C2 [{seg_integral(E, O, (0, 2, 0)):.6f}, {seg_integral(E, (0, 2, 0), P6):.6f}]; "
          f"C3 integrand (6 {'+' if name == 'E+' else '-'} 2) x^3 dx = {6 + 2 if name == 'E+' else 6 - 2} x^3 dx -> {(6 + 2 if name == 'E+' else 6 - 2) / 4}")
check("E+ integrals", res["E+"], [2, 2, 2])
check("E- integrals", res["E-"], [-2, 2, 1])
# potential V = -x^3 y for E+
V56 = lambda x, y, z: -x**3 * y
for p in [(0.4, 1.1, 0), (1.3, -0.6, 0.2)]:
    check(f"-grad(-x^3 y) = E+ at {p}", -grad_fd(V56, p), Ep(*p), atol=1e-6)
print(f"  V(P)-V(O) = {V56(*P6) - V56(*O)} V")
# Stokes: lower triangle 0<x<1, 0<y<2x, CCW (dS = +z): flux of curl_z = -6x^2
flux_low = integrate.dblquad(lambda y, x: -6 * x**2, 0, 1, lambda x: 0, lambda x: 2 * x)[0]
flux_up = integrate.dblquad(lambda y, x: -6 * x**2, 0, 1, lambda x: 2 * x, lambda x: 2)[0]
print(f"  flux of curl through lower triangle (+z normal) = {flux_low:.6f}; C1 - C3 = {res['E-'][0]-res['E-'][2]:.6f}")
print(f"  [page] inner y-integral gives -12 x^3: int_0^1 -12 x^3 dx = {integrate.quad(lambda x: -12 * x**3, 0, 1)[0]:.6f}")
check("Stokes lower triangle", res["E-"][0] - res["E-"][2], flux_low)
print(f"  flux through upper triangle (+z normal) = {flux_up:.6f}; C2 - C3 = {res['E-'][1]-res['E-'][2]:.6f} (= -flux_up: loop is clockwise)")
check("Stokes upper triangle", res["E-"][1] - res["E-"][2], -flux_up)

# =====================================================================
print("=" * 70)
print("5.7  Uniformly charged ball, V(inf) = 0")
def ball_closed(r, Q, a, k):
    return k * Q / r if r >= a else k * Q / (2 * a) * (3 - r**2 / a**2)
def ball_brute(z, Q, a, k):
    """V at distance z from the centre by direct volume superposition (dblquad over r', theta')."""
    rho = Q / (4 / 3 * np.pi * a**3)
    f = lambda th, rp: rho * 2 * np.pi * rp**2 * np.sin(th) / np.sqrt(rp**2 + z**2 - 2 * rp * z * np.cos(th) + 1e-300)
    pts = [z] if 0 < z < a else None
    if pts:
        v1 = integrate.dblquad(f, 0, z, 0, np.pi, epsabs=1e-13, epsrel=1e-10)[0]
        v2 = integrate.dblquad(f, z, a, 0, np.pi, epsabs=1e-13, epsrel=1e-10)[0]
        v = v1 + v2
    else:
        v = integrate.dblquad(f, 0, a, 0, np.pi, epsabs=1e-13, epsrel=1e-10)[0]
    return k * v
for (Qb, ab) in [(1e-9, 0.09), (2.5e-9, 0.2)]:
    for z in (0.0, 0.3 * ab, 0.5 * ab, ab, 2 * ab):
        check(f"ball Q={Qb}, a={ab}, r={z:.4f}: brute vs closed", ball_brute(z, Qb, ab, kx), ball_closed(z, Qb, ab, kx), rtol=1e-5)
# line-integral route: V(r) = -int_inf^r E dr with Gauss E
def E_ball(r, Q, a, k):
    return k * Q / r**2 if r >= a else k * Q * r / a**3
def V_from_E(r, Q, a, k):
    out = integrate.quad(lambda u: E_ball(a / u, Q, a, k) * a / u**2, 0, 1)[0]  # int_a^inf
    inner = integrate.quad(lambda rp: E_ball(rp, Q, a, k), r, a)[0] if r < a else -integrate.quad(lambda rp: E_ball(rp, Q, a, k), a, r)[0]
    return out + inner
for z in (0.0, 0.045, 0.09, 0.2):
    check(f"V from -int E dr at r={z}", V_from_E(z, 1e-9, 0.09, kx), ball_closed(z, 1e-9, 0.09, kx), rtol=1e-8)
Va9, V09 = ball_closed(0.09, 1e-9, 0.09, k9), ball_closed(0.0, 1e-9, 0.09, k9)
print(f"  stated numbers (9e9): V(a) = {Va9:.6f} V, V(0) = {V09:.6f} V, V(a/2) = {ball_closed(0.045,1e-9,0.09,k9):.4f} V")
print(f"  exact k: V(a) = {ball_closed(0.09,1e-9,0.09,kx):.4f} V, V(0) = {ball_closed(0,1e-9,0.09,kx):.4f} V")
check("V(a), V(0)", [Va9, V09], [100, 150])
print(f"  [page] kQ/(2a) = {k9 * 1e-9 / (2 * 0.09):.6f} V; 3 - 1/4 = {3 - 0.25}; V(a/2) = {k9 * 1e-9 / (2 * 0.09) * 2.75:.4f} V; (3/2) V(a) = {1.5 * Va9:.4f} V")
print(f"  proton to centre: W = 150 eV = {150*e:.6e} J")
# slope check: -dV/dr = E inside
hh = 1e-7
rr = 0.05
check("-dV/dr = E inside at r=5 cm", -(ball_closed(rr + hh, 1e-9, 0.09, kx) - ball_closed(rr - hh, 1e-9, 0.09, kx)) / (2 * hh), E_ball(rr, 1e-9, 0.09, kx), rtol=1e-6)

# =====================================================================
print("=" * 70)
print("5.8  Long uniformly charged cylinder, rho_l = 200 pi eps0 C/m, a = 2 cm, V(a) = 0")
def E_cyl_gauss(r, rl, a):
    return rl / (2 * np.pi * eps0 * r) if r >= a else rl * r / (2 * np.pi * eps0 * a**2)
def E_cyl_brute(r, rl, a):
    """E_r at (r,0) by 2-D superposition of infinite line charges over the cross-section."""
    rho = rl / (np.pi * a**2)
    def inner(rp):
        f = lambda ph: (r - rp * np.cos(ph)) / (r**2 + rp**2 - 2 * r * rp * np.cos(ph))
        # the integrand has a peak of width ~|r-rp|/sqrt(r rp) at ph = 0: give quad breakpoints there
        dlt = abs(r - rp) / np.sqrt(r * rp)
        bps = sorted({0.0} | {s * m * dlt for s in (-1, 1) for m in (1, 10, 100) if m * dlt < 3.0})
        edges = [-np.pi] + bps + [np.pi]
        return sum(integrate.quad(f, lo, hi, limit=200, epsabs=1e-13, epsrel=1e-11)[0] for lo, hi in zip(edges[:-1], edges[1:]))
    if 0 < r < a:
        v = integrate.quad(lambda rp: inner(rp) * rp, 0, r, limit=200)[0] + integrate.quad(lambda rp: inner(rp) * rp, r, a, limit=200)[0]
    else:
        v = integrate.quad(lambda rp: inner(rp) * rp, 0, a, limit=200)[0]
    return rho / (2 * np.pi * eps0) * v
for (rl, a8) in [(200 * np.pi * eps0, 0.02), (3e-9, 0.05)]:
    for r in (0.3 * a8, 0.7 * a8, 1.5 * a8, 3 * a8):
        check(f"cyl E rl={rl:.3e}, a={a8}, r={r:.4f}: brute vs Gauss", E_cyl_brute(r, rl, a8), E_cyl_gauss(r, rl, a8), rtol=2e-5)
rl, a8 = 200 * np.pi * eps0, 0.02
print(f"  rho_l = {rl:.6e} C/m ; rho_l/(2 pi eps0) = {rl/(2*np.pi*eps0):.6f} V")
def V_cyl(r, rl=rl, a=a8):   # V(a) = 0, numerical -int_a^r E dr
    return -integrate.quad(lambda rp: E_cyl_gauss(rp, rl, a), a, r)[0]
V0, V2a = V_cyl(0.0), V_cyl(2 * a8)
print(f"  V(0) = {V0:.6f} V, V(2a) = {V2a:.6f} V, V(0)-V(2a) = {V0 - V2a:.6f} V")
check("V(0), V(2a) with V(a)=0", [V0, V2a], [50, -100 * np.log(2)])
print(f"  reference on axis: V(a) = {-V0:.6f} V, V(2a) = {V2a - V0:.6f} V")
check("re-referenced", [-V0, V2a - V0], [-50, -50 - 100 * np.log(2)])
# closed forms at a second parameter set
rl2, a2 = 3e-9, 0.05
for r in (0.0, 0.02, 0.05, 0.11):
    closed = rl2 / (4 * np.pi * eps0) * (1 - r**2 / a2**2) if r <= a2 else -rl2 / (2 * np.pi * eps0) * np.log(r / a2)
    check(f"V closed form, set 2, r={r}", V_cyl(r, rl2, a2), closed, rtol=1e-8)
print(f"  divergence of the log: V(r)-V(a) at r = 1e3, 1e6, 1e9 m: {[round(V_cyl(R),2) for R in (1e3,1e6,1e9)]} V")

# =====================================================================
print("=" * 70)
print("5.9  Rectangle (-1..2) x (0..2), a=(2,2,0), b=(-1,0,0), clockwise from +z")
a9, c1, b9, c2 = (2, 2, 0), (2, 0, 0), (-1, 0, 0), (-1, 2, 0)
loop = [a9, c1, b9, c2, a9]
Eu = lambda x, y, z: (3.0, 4.0, -2.0)
legs = [seg_integral(Eu, p, q) for p, q in zip(loop[:-1], loop[1:])]
print(f"  (a) uniform field legs: {np.round(legs,6)}, circulation = {sum(legs):.6f} V")
check("(a)(i) circulation", sum(legs), 0.0)
Iab = seg_integral(Eu, a9, b9)
check("(a)(ii) V(b)-V(a) = -int_a^b", -Iab, 17.0)
check("(a)(ii) via C_R", -poly_integral(Eu, [a9, c1, b9]), 17.0)
Ec = lambda x, y, z: (-(2.5 * y + 1.5 * z), 2.5 * x - z, 1.5 * x + y)
for p in [(0.1, 0.2, 0.3), (1.7, -2.0, 0.9)]:
    check(f"(c) curl of given field at {p}", curl_fd(Ec, p), [2, -3, 5], atol=1e-6)
print(f"  [page] b - a = {np.subtract(b9, a9)} m; E.(b-a) = {np.dot([3, 4, -2], np.subtract(b9, a9)):.1f} V")
h9 = 1e-5
Jc = np.array([[(Ec(*(np.array([0.4, -0.3, 0.2]) + h9 * np.eye(3)[j]))[i] - Ec(*(np.array([0.4, -0.3, 0.2]) - h9 * np.eye(3)[j]))[i]) / (2 * h9)
                for j in range(3)] for i in range(3)])
print(f"  [page] partials: dyEz = {Jc[2,1]:.4f}, dzEy = {Jc[1,2]:.4f}, dzEx = {Jc[0,2]:.4f}, dxEz = {Jc[2,0]:.4f}, dxEy = {Jc[1,0]:.4f}, dyEx = {Jc[0,1]:.4f}")
for p in [(0.4, -0.3, 0.2), (-1.2, 2.5, 0.7)]:
    check(f"(c) given field = 1/2 c x r with c = (2,-3,5) at {p}", Ec(*p), 0.5 * np.cross([2, -3, 5], p))
area = 3 * 2
flux = integrate.dblquad(lambda y, x: np.dot(curl_fd(Ec, (x, y, 0)), [0, 0, -1]), -1, 2, lambda x: 0, lambda x: 2)[0]
print(f"  (b) area = {area} m^2, flux of curl with dS = -z dA: {flux:.6f} V")
check("(b)(i) circulation by Stokes", flux, -30.0, rtol=1e-6)
circ_c = poly_integral(Ec, loop)
check("(c) circulation by direct line integral", circ_c, -30.0)
IR = poly_integral(Ec, [a9, c1, b9])
IL = poly_integral(Ec, [a9, c2, b9])
legsR = [seg_integral(Ec, a9, c1), seg_integral(Ec, c1, b9)]
legsL = [seg_integral(Ec, a9, c2), seg_integral(Ec, c2, b9)]
print(f"  (c) C_R legs {np.round(legsR,6)} total {IR:.6f} V ; C_L legs {np.round(legsL,6)} total {IL:.6f} V")
check("(c) C_R, C_L", [IR, IL], [-10, 20])
check("(c) C_R - C_L = circulation", IR - IL, -30)
print(f"  -int_a^b along C_R = {-IR:.4f} V, along C_L = {-IL:.4f} V")
print(f"  [page] integrands on the legs: E_y(x=2) = {Ec(2, 0.7, 0)[1]}, E_x(y=0) = {Ec(0.5, 0, 0)[0]}, "
      f"E_x(y=2) = {Ec(0.5, 2, 0)[0]}, E_y(x=-1) = {Ec(-1, 0.7, 0)[1]} V/m")
print(f"  (d) voltmeter + at b, - at a reads int_b^a = -int_a^b: C_R {-IR:.4f} V, C_L {-IL:.4f} V, difference {(-IR)-(-IL):.4f} V")
# general check of the uniform-curl construction E = 1/2 c x r at a second curl vector
cvec = np.array([-1.0, 4.0, 2.5])
Eg = lambda x, y, z: 0.5 * np.cross(cvec, [x, y, z])
check("1/2 c x r has curl c (second c)", curl_fd(Eg, (0.4, -0.2, 1.1)), cvec, atol=1e-6)
check("its circulation on C (clockwise) = -c_z * area", poly_integral(Eg, loop), -cvec[2] * area)

# =====================================================================
print("=" * 70)
print("5.10  Slab 0<x<d (rho0 = 6 eps0) + sheet -rho0 d at x = 0; V(0) = 0")
def E_slab_sheet_brute(x, rho0, d):
    # slab = stack of thin sheets rho0 dx' at x'; each gives rho0 dx'/(2 eps0) sgn(x - x')
    pts = [x] if 0 < x < d else None
    slab = integrate.quad(lambda xp: rho0 / (2 * eps0) * np.sign(x - xp), 0, d, points=pts, limit=200)[0]
    sheet = (-rho0 * d) / (2 * eps0) * np.sign(x)
    return slab + sheet
def E_closed(x, rho0, d):
    if x < 0 or x > d:
        return 0.0
    return rho0 / eps0 * (x - d)
for (rho0, d) in [(6 * eps0, 2.0), (2.5e-9, 0.7)]:
    for x in (-1.0, 0.3 * d, 0.8 * d, 1.5 * d):
        check(f"E brute vs closed, rho0={rho0:.3e}, d={d}, x={x:.3f}", E_slab_sheet_brute(x, rho0, d), E_closed(x, rho0, d), rtol=1e-8, atol=1e-6)
rho0, d10 = 6 * eps0, 2.0
print(f"  rho0 = {rho0:.4e} C/m^3 ({rho0*1e12:.2f} pC/m^3), rho_s = {-rho0*d10:.4e} C/m^2 ({-rho0*d10*1e12:.1f} pC/m^2)")
print(f"  E(0+) = {E_closed(1e-12, rho0, d10):.6f} V/m ; E inside = 6(x-2)")
check("jump eps0[E(0+)-E(0-)] = rho_s", eps0 * (E_slab_sheet_brute(1e-9, rho0, d10) - E_slab_sheet_brute(-1e-9, rho0, d10)), -rho0 * d10, rtol=1e-6)
def V10(x, rho0=rho0, d=d10):
    if x <= 0:
        return -integrate.quad(lambda xp: E_slab_sheet_brute(xp, rho0, d), 0, x)[0] if x < 0 else 0.0
    return -integrate.quad(lambda xp: E_slab_sheet_brute(xp, rho0, d), 0, x, points=[min(x, d)], limit=200)[0]
for x in (-1.5, 0.5, 1.0, 2.0, 3.0):
    closed = 0.0 if x <= 0 else (12 * x - 3 * x**2 if x <= 2 else 12.0)
    check(f"V({x})", V10(x), closed, rtol=1e-8, atol=1e-8)
check("V(d) = rho0 d^2/(2 eps0) (set 2)", V10(0.7, 2.5e-9, 0.7), 2.5e-9 * 0.7**2 / (2 * eps0), rtol=1e-8)
KE_eV = 12.0
v_e = np.sqrt(2 * KE_eV * e / me)
print(f"  electron KE beyond x = d: {KE_eV} eV = {KE_eV*e:.6e} J, speed {v_e:.6e} m/s")
print(f"  force on electron at x = 0+: -e*E = {-e*E_closed(1e-12,rho0,d10):+.3e} N along x (pushes +x)")
# Part 2: trig field
Et = lambda x, y, z: (y * np.cos(x), np.sin(x), -2 * z)
for p in [(0.3, 1.2, -0.4), (2.0, -1.0, 0.7)]:
    check(f"(d) curl trig field at {p}", curl_fd(Et, p), [0, 0, 0], atol=1e-6)
Vt = lambda x, y, z: 5 - y * np.sin(x) + z**2
for p in [(0.3, 1.2, -0.4), (2.0, -1.0, 0.7)]:
    check(f"(d) -grad V = E at {p}", -grad_fd(Vt, p), Et(*p), atol=1e-6)
B = (np.pi / 2, 2, 1)
stair = poly_integral(Et, [(0, 0, 0), (np.pi / 2, 0, 0), (np.pi / 2, 2, 0), B])
straight = seg_integral(Et, (0, 0, 0), B)
print(f"  (d) int_O^B E.dl: staircase {stair:.6f}, straight {straight:.6f} V")
st_pts = [(0, 0, 0), (np.pi / 2, 0, 0), (np.pi / 2, 2, 0), B]
print(f"  [page] staircase legs: {[round(seg_integral(Et, p0, p1), 6) for p0, p1 in zip(st_pts[:-1], st_pts[1:])]} V; m_e = {me} kg; "
      f"field E(0+) = {E_closed(1e-12, rho0, d10):.1f} V/m -> F = -eE = {-E_closed(1e-12, rho0, d10):.1f} e")
check("(d) V(B) = 5 - int_O^B", [5 - stair, 5 - straight], [4, 4])
check("(d) V(B) closed", Vt(*B), 4.0)
W10 = 2e-6 * (Vt(*B) - Vt(0, 0, 0))
print(f"  (d) work by agent on q = 2 uC: {W10:.6e} J")
check("(d) work", W10, -2e-6)

# =====================================================================
print("=" * 70)
print("5.11  Annulus a=5 cm, b=9 cm, rho_s = 1000 eps0 C/m^2: axis potential")
def V_ann_closed(z, rs, a, b):
    return rs / (2 * eps0) * (np.sqrt(b**2 + z**2) - np.sqrt(a**2 + z**2))
def V_ann_brute(z, rs, a, b):
    f = lambda ph, rp: rs * rp / np.sqrt((rp * np.cos(ph))**2 + (rp * np.sin(ph))**2 + z**2)
    return kx * integrate.dblquad(f, a, b, 0, 2 * np.pi, epsabs=1e-14, epsrel=1e-11)[0]
def Ez_ann_brute(z, rs, a, b):
    f = lambda ph, rp: rs * rp * z / ((rp * np.cos(ph))**2 + (rp * np.sin(ph))**2 + z**2) ** 1.5
    return kx * integrate.dblquad(f, a, b, 0, 2 * np.pi, epsabs=1e-14, epsrel=1e-11)[0]
def Ez_ann_closed(z, rs, a, b):
    return rs / (2 * eps0) * z * (1 / np.sqrt(a**2 + z**2) - 1 / np.sqrt(b**2 + z**2))
for (rs, a, b) in [(1000 * eps0, 0.05, 0.09), (3e-9, 0.02, 0.10)]:
    for z in (0.0, 0.03, 0.12, -0.2, 1.0):
        check(f"V brute vs closed rs={rs:.3e}, z={z}", V_ann_brute(z, rs, a, b), V_ann_closed(z, rs, a, b), rtol=1e-7)
        check(f"E_z brute vs -dV/dz closed, z={z}", Ez_ann_brute(z, rs, a, b), Ez_ann_closed(z, rs, a, b), rtol=1e-6, atol=1e-9)
        hz = 1e-6
        check(f"E_z closed = -dV/dz (FD), z={z}", -(V_ann_closed(z + hz, rs, a, b) - V_ann_closed(z - hz, rs, a, b)) / (2 * hz), Ez_ann_closed(z, rs, a, b), rtol=1e-6, atol=1e-6)
rs, a, b = 1000 * eps0, 0.05, 0.09
print(f"  rho_s = {rs:.6e} C/m^2 ; rho_s/(2 eps0) = {rs/(2*eps0):.3f} V/m")
print(f"  V(0) = {V_ann_closed(0,rs,a,b):.6f} V, V(12 cm) = {V_ann_closed(0.12,rs,a,b):.6f} V, E_z(12 cm) = {Ez_ann_closed(0.12,rs,a,b):.6f} V/m")
print(f"  [page] b - a = {b - a:.2f} m; sqrt(b^2+0.12^2) = {np.sqrt(b**2 + 0.0144):.6f} m, sqrt(a^2+0.12^2) = {np.sqrt(a**2 + 0.0144):.6f} m; "
      f"(rho_s/2eps0)*0.12 = {rs / (2 * eps0) * 0.12:.6f} V")
# disk limits: sheet value near the surface, point-charge value far away (two radii)
for bd in (0.09, 0.2):
    check(f"disk (b={bd}) E_z(z->0+) -> rho_s/(2 eps0)", Ez_ann_closed(1e-9, rs, 0.0, bd), rs / (2 * eps0), rtol=1e-6)
    zf = 300 * bd
    check(f"disk (b={bd}) E_z(z={zf}) -> pi b^2 rho_s/(4 pi eps0 z^2)", Ez_ann_closed(zf, rs, 0.0, bd), kx * np.pi * bd**2 * rs / zf**2, rtol=1e-4)
check("V(0), V(0.12)", [V_ann_closed(0, rs, a, b), V_ann_closed(0.12, rs, a, b)], [20, 10])
check("E_z(0.12)", Ez_ann_closed(0.12, rs, a, b), 60 * (1 / 0.13 - 1 / 0.15))
check("E_z(0) = 0", Ez_ann_brute(0.0, rs, a, b), 0.0, atol=1e-9)
zz = np.linspace(-0.5, 0.5, 2001)
Vz = V_ann_closed(zz, rs, a, b)
print(f"  max of V on axis at z = {zz[np.argmax(Vz)]:.4f} m (monotone decrease with |z|: {np.all(np.diff(Vz[zz>=0])<0)})")
Qa = np.pi * rs * (b**2 - a**2)
print(f"  total charge Q = {Qa:.6e} C ; far field Q/(4 pi eps0 z) at z = 1 m: {kx*Qa:.6f} V vs exact {V_ann_closed(1.0,rs,a,b):.6f} V")
print(f"  coefficient rho_s (b^2-a^2)/(4 eps0) = {rs*(b**2-a**2)/(4*eps0):.6f} V m")
# disk limit (a -> 0) vs Lecture 2 disk field
for z in (0.01, 0.1, 0.5):
    check(f"a->0 gives disk E_z at z={z}", Ez_ann_closed(z, rs, 0.0, b), rs / (2 * eps0) * (1 - z / np.sqrt(b**2 + z**2)))
KEp = 20.0
print(f"  proton minimum KE = {KEp} eV = {KEp*e:.6e} J")
KEe = (V_ann_closed(0, rs, a, b) - V_ann_closed(0.12, rs, a, b))
v_e2 = np.sqrt(2 * KEe * e / me)
print(f"  electron from rest at 12 cm: KE at centre = {KEe:.6f} eV = {KEe*e:.6e} J, speed = {v_e2:.6e} m/s")

# =====================================================================
print("=" * 70)
print("5.12  Square of four q = 2 nC, side 30 cm, plus a centre charge")
q12, s = 2e-9, 0.3
corners = np.array([[s / 2, s / 2, 0], [-s / 2, s / 2, 0], [-s / 2, -s / 2, 0], [s / 2, -s / 2, 0]])
def assembly_energy(charges, positions, k):
    W = 0.0
    n = len(charges)
    for i in range(n):
        for j in range(i + 1, n):
            W += k * charges[i] * charges[j] / np.linalg.norm(positions[i] - positions[j])
    return W
def incremental(charges, positions, order, k):
    W, placed = 0.0, []
    for i in order:
        V = sum(k * charges[j] / np.linalg.norm(positions[i] - positions[j]) for j in placed)
        W += charges[i] * V
        placed.append(i)
    return W
qs = np.array([q12] * 4)
W4_9 = assembly_energy(qs, corners, k9)
W4_x = assembly_energy(qs, corners, kx)
unit9 = k9 * q12**2 / s
print(f"  kq^2/s (9e9) = {unit9:.6e} J ; (4+sqrt2) = {4+np.sqrt(2):.6f}")
print(f"  W4 = {W4_9:.6e} J (9e9) ; exact-k {W4_x:.6e} J")
check("W4 = (4+sqrt2) kq^2/s", W4_9, (4 + np.sqrt(2)) * unit9)
for order in ([0, 1, 2, 3], [2, 0, 3, 1], [3, 2, 1, 0]):
    check(f"incremental qV, order {order}", incremental(qs, corners, order, k9), W4_9)
steps = [incremental(qs, corners, [0, 1, 2, 3][:n + 1], k9) - incremental(qs, corners, [0, 1, 2, 3][:n], k9) for n in range(4)]
print(f"  [page] steps of order [0,1,2,3] in units of kq^2/s: {np.round(np.array(steps) / unit9, 6)} (1 + 1/sqrt2 = {1 + 1/np.sqrt(2):.6f})")
Vc_9 = sum(k9 * q12 / np.linalg.norm(c) for c in corners)
print(f"  V(centre) = {Vc_9:.6f} V (9e9), exact-k {sum(kx*q12/np.linalg.norm(c) for c in corners):.6f} V; s/sqrt2 = {s/np.sqrt(2):.6f} m")
check("V(centre) = 4 sqrt2 kq/s", Vc_9, 4 * np.sqrt(2) * k9 * q12 / s)
Qc = -W4_9 / Vc_9
print(f"  Q for zero total energy = {Qc:.6e} C = {Qc/q12:.6f} q ; -(1/sqrt2 + 1/4) = {-(1/np.sqrt(2)+0.25):.6f}")
check("Q/q", Qc / q12, -(1 / np.sqrt(2) + 0.25))
all_q = np.append(qs, Qc)
all_p = np.vstack([corners, [0, 0, 0]])
check("total 5-charge energy = 0", assembly_energy(all_q, all_p, k9), 0.0, atol=1e-18)
# force on corner 0 with Q at centre
def force_on(i, charges, positions, k):
    F = np.zeros(3)
    for j in range(len(charges)):
        if j != i:
            dvec = positions[i] - positions[j]
            F += k * charges[i] * charges[j] * dvec / np.linalg.norm(dvec) ** 3
    return F
F_corners_only = force_on(0, qs, corners, k9)
F_all = force_on(0, all_q, all_p, k9)
F_centre = force_on(0, np.array([q12, Qc]), np.array([corners[0], [0, 0, 0]]), k9)
fmt = lambda v: "[" + ", ".join(f"{c:+.6e}" for c in v) + "]"
print(f"  kq^2/s^2 = {k9*q12**2/s**2:.6e} N")
print(f"  force on corner (s/2,s/2) from other corners: {fmt(F_corners_only)} N, |F| = {np.linalg.norm(F_corners_only):.6e} N  ((sqrt2 + 1/2) kq^2/s^2 = {(np.sqrt(2)+0.5)*k9*q12**2/s**2:.6e})")
print(f"  force on it from the centre charge: {fmt(F_centre)} N, |F| = {np.linalg.norm(F_centre):.6e} N")
check("net force on a corner = 0", F_all, [0, 0, 0], atol=1e-18)
check("net force on centre = 0", force_on(4, all_q, all_p, k9), [0, 0, 0], atol=1e-18)
# scaling: energy of the configuration scaled by lambda stays zero; with a different Q it scales as 1/lambda
for lam in (0.5, 2.0):
    check(f"scaled square x{lam}: energy still 0", assembly_energy(all_q, all_p * lam, k9), 0.0, atol=1e-18)
Wtest = assembly_energy(np.append(qs, -q12), all_p, k9)
check("with Q=-q, energy scales as 1/lambda", assembly_energy(np.append(qs, -q12), all_p * 2, k9), Wtest / 2)

print("=" * 70)
print(f"ALL CHECKS PASSED: {all(ok_all)}  ({sum(ok_all)}/{len(ok_all)})")
