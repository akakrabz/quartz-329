#!/usr/bin/env python3
"""R06.py -- independent re-solve of practice page 06 (circulation and boundary conditions).

Method (independent of the page's own algebra):
  * every n-hat is a finite-difference gradient of the interface function, normalised and then
    ORIENTED by testing which side of the interface a small step lands in (medium 1 or 2);
  * every boundary condition is solved as an over-determined linear system
        n x (F1 - F2) = tangential source,   n . (k1 F1 - k2 F2) = normal source
    with np.linalg.lstsq (residual asserted to be zero), never by "copy the tangential part";
  * line integrals: scipy quad along each straight side (crossings of charged planes found by brentq);
    surface integrals: dblquad; curls: central finite differences;
  * sheet fields: brute-force superposition of infinite straight wires; 1-D Poisson by finite differences.
The page's stated answers are transcribed and compared: PASS / FAIL per quantity.
Units: in electrostatics, charges/D are carried in units of eps0 unless converted explicitly.
"""
import numpy as np
from scipy import integrate, optimize, linalg

EPS0 = 8.8541878128e-12
MU0 = 4e-7 * np.pi
N_PASS = 0
N_FAIL = 0


def fmt(a):
    a = np.atleast_1d(np.asarray(a, dtype=float))
    if a.size == 1:
        return f"{a[0]:.6g}"
    return "[" + ", ".join(f"{v:.6g}" for v in a) + "]"


def chk(tag, name, computed, page, atol=1e-9, rtol=0.0):
    global N_PASS, N_FAIL
    c = np.atleast_1d(np.asarray(computed, dtype=float))
    p = np.atleast_1d(np.asarray(page, dtype=float))
    ok = (c.shape == p.shape) and bool(np.allclose(c, p, atol=atol, rtol=rtol))
    N_PASS += ok
    N_FAIL += (not ok)
    print(f"[{tag}] {name:<48s} computed={fmt(c):<36s} page={fmt(p):<28s} {'PASS' if ok else 'FAIL'}")
    return ok


def chk_eq(tag, name, computed, page):
    global N_PASS, N_FAIL
    ok = computed == page
    N_PASS += ok
    N_FAIL += (not ok)
    print(f"[{tag}] {name:<48s} computed={str(computed):<36s} page={str(page):<28s} {'PASS' if ok else 'FAIL'}")
    return ok


def note(tag, text):
    print(f"[{tag}] note: {text}")


def grad(f, p, h=1e-20):
    """Complex-step derivative: Im f(p + i h e)/h, exact to rounding for analytic f."""
    p = np.asarray(p, dtype=complex)
    return np.array([f(p + 1j * h * e).imag / h for e in np.eye(3)])


def normal_2_to_1(f, p, in1):
    """Unit normal of the level surface of f through p, oriented to point INTO medium 1."""
    g = grad(f, p)
    n = g / np.linalg.norm(g)
    if not in1(p + 1e-4 * n):
        n = -n
    assert in1(p + 1e-4 * n) and not in1(p - 1e-4 * n), "orientation test failed"
    return n


def split(v, n):
    v = np.asarray(v, float)
    vn = float(np.dot(v, n))
    return vn, vn * n, v - vn * n


def X(n):
    """Matrix with X(n) @ v == np.cross(n, v)."""
    return np.array([[0.0, -n[2], n[1]], [n[2], 0.0, -n[0]], [-n[1], n[0], 0.0]])


def solve_side1(n, F2, k1, k2, tan_src, nrm_src):
    """F1 from n x (F1-F2) = tan_src and n.(k1 F1 - k2 F2) = nrm_src (least squares, exact)."""
    A = np.vstack([X(n), k1 * n[None, :]])
    b = np.concatenate([X(n) @ F2 + tan_src, [nrm_src + k2 * np.dot(n, F2)]])
    F1 = np.linalg.lstsq(A, b, rcond=None)[0]
    assert np.allclose(A @ F1, b, atol=1e-9), "inconsistent BC system"
    return F1


def solve_side2(n, F1, k1, k2, tan_src, nrm_src):
    """F2 from the same two conditions with F1 known."""
    A = np.vstack([X(n), k2 * n[None, :]])
    b = np.concatenate([X(n) @ F1 - tan_src, [k1 * np.dot(n, F1) - nrm_src]])
    F2 = np.linalg.lstsq(A, b, rcond=None)[0]
    assert np.allclose(A @ F2, b, atol=1e-9), "inconsistent BC system"
    return F2


def line_int(E, P, Q, f=None, levels=()):
    """int_P^Q E . dl along the straight segment P->Q (quad, split where f crosses a level)."""
    P = np.asarray(P, float)
    Q = np.asarray(Q, float)
    d = Q - P
    pts = []
    if f is not None:
        for L in levels:
            g = lambda t, L=L: f(P + t * d) - L
            if g(0.0) * g(1.0) < 0:
                pts.append(optimize.brentq(g, 0.0, 1.0, xtol=1e-14))
    val = integrate.quad(lambda t: float(np.dot(E(P + t * d), d)), 0.0, 1.0,
                         points=pts if pts else None, limit=500, epsabs=1e-12, epsrel=1e-12)[0]
    return val, [P + t * d for t in pts]


def loop_normal(corners):
    c = [np.asarray(v, float) for v in corners]
    A = 0.5 * sum(np.cross(c[i], c[(i + 1) % len(c)]) for i in range(len(c)))
    return A / np.linalg.norm(A)


def curl(F, p, h=1e-5):
    p = np.asarray(p, float)
    J = np.zeros((3, 3))
    for j, e in enumerate(np.eye(3)):
        J[:, j] = (np.asarray(F(p + h * e), float) - np.asarray(F(p - h * e), float)) / (2 * h)
    return np.array([J[2, 1] - J[1, 2], J[0, 2] - J[2, 0], J[1, 0] - J[0, 1]])


def sheet_H(Js_vec, n, p, W=1e4):
    """H at p from a flat sheet through the origin (normal n, surface current Js_vec) built from
    infinite straight wires along Js: dH = (Js ds) u x R_perp / (2 pi |R_perp|^2)."""
    Js = np.linalg.norm(Js_vec)
    u = Js_vec / Js
    t = np.cross(n, u)

    def integrand(s, c):
        R = p - s * t
        Rp = R - np.dot(R, u) * u
        return Js * np.cross(u, Rp)[c] / (2 * np.pi * np.dot(Rp, Rp))

    H = np.zeros(3)
    for c in range(3):
        H[c] = sum(integrate.quad(integrand, a, b, args=(c,), limit=800, epsabs=1e-13, epsrel=1e-12)[0]
                   for a, b in [(-W, -1.0), (-1.0, 0.0), (0.0, 1.0), (1.0, W)])
    return H


# ====================================================================================== 6.1
T = "6.1"
print(f"\n=== {T} What is always continuous ===")
e1, e2 = 2.0, 5.0
n = normal_2_to_1(lambda r: r[2], np.zeros(3), lambda r: r[2] > 0)
chk(T, "n-hat (2 -> 1) in the worked example", n, [0, 0, 1])
E2 = np.array([1.3, -0.7, 2.1])
E1 = solve_side1(n, E2, e1, e2, np.zeros(3), 4.0)
E1n, _, E1t = split(E1, n)
E2n, _, E2t = split(E2, n)
chk(T, "E1 tangential part [V/m]", E1t, [1.3, -0.7, 0])
chk(T, "E1z [V/m]", E1n, 7.25)
chk(T, "(a) E1z - E2z [V/m]", E1n - E2n, 5.15)
chk(T, "(b) n.(D1-D2) [eps0]", np.dot(n, e1 * E1 - e2 * E2), 4.0)
chk(T, "(d) D1t/D2t", np.linalg.norm(e1 * E1t) / np.linalg.norm(e2 * E2t), 0.4)
chk(T, "(e) |E1| [V/m]", np.linalg.norm(E1), 7.40, atol=0.005)
chk(T, "(e) |E2| [V/m]", np.linalg.norm(E2), 2.57, atol=0.005)
E1_0 = solve_side1(n, E2, e1, e2, np.zeros(3), 0.0)
chk(T, "follow-up rho_s=0: E1n/E2n", np.dot(E1_0, n) / np.dot(E2, n), 2.5)
# brute force: which quantities are equal on both sides for EVERY field (random sampling)?
rng = np.random.default_rng(329)


def always_equal(rho_choice):
    ok = dict.fromkeys("abcde", True)
    for _ in range(3000):
        nn = rng.normal(size=3)
        nn /= np.linalg.norm(nn)
        F2 = 3 * rng.normal(size=3)
        rho = rho_choice()
        F1 = solve_side1(nn, F2, e1, e2, np.zeros(3), rho)
        G1, G2 = e1 * F1, e2 * F2
        tests = {"a": abs(np.dot(nn, F1 - F2)), "b": abs(np.dot(nn, G1 - G2)),
                 "c": np.linalg.norm(split(F1, nn)[2] - split(F2, nn)[2]),
                 "d": np.linalg.norm(split(G1, nn)[2] - split(G2, nn)[2]),
                 "e": abs(np.linalg.norm(F1) - np.linalg.norm(F2))}
        for k, v in tests.items():
            if v > 1e-9:
                ok[k] = False
    return sorted(k for k, v in ok.items() if v)


chk_eq(T, "key (always equal, rho_s != 0)", always_equal(lambda: rng.choice([-1, 1]) * rng.uniform(0.5, 5)), ["c"])
chk_eq(T, "key (always equal, rho_s = 0)", always_equal(lambda: 0.0), ["b", "c"])
# wording audit: special fields for which (a) or (e) happen to hold despite rho_s != 0
E2n_a = 4.0 / (e1 - e2)
E1n_a = (4.0 + e2 * E2n_a) / e1
note(T, f"rho_s=4eps0: E2n={E2n_a:.4f} gives E1n={E1n_a:.4f} -> normal E continuous for this one field "
        "(so 'normal E jumps at ANY charged surface' is an over-statement)")
E1n_e = 4.0 / (e1 + e2)
note(T, f"rho_s=4eps0: E2n={-E1n_e:.4f} gives E1n={E1n_e:.4f} -> |E1|=|E2| for this field "
        "(so 'one component jumps, so the magnitudes differ' is not automatic)")

# ====================================================================================== 6.2
T = "6.2"
print(f"\n=== {T} Kirchhoff around a triangle ===")
E = lambda r: np.array([3.0, 4.0, -2.0])
P1, P2, P3 = np.array([0, 0, 0.0]), np.array([2, 0, 0.0]), np.array([2, 3, 0.0])
s12, s23, s31 = line_int(E, P1, P2)[0], line_int(E, P2, P3)[0], line_int(E, P3, P1)[0]
chk(T, "sides P1P2, P2P3, P3P1 [V]", [s12, s23, s31], [6, 12, -18])
chk(T, "circulation [V]", s12 + s23 + s31, 0, atol=1e-9)
chk(T, "V(P3)-V(P1) via P2 [V]", -(s12 + s23), -18)
chk(T, "V(P3)-V(P1) along slanted side [V]", -line_int(E, P1, P3)[0], -18)
V = lambda r: -(3 * r[0] + 4 * r[1] - 2 * r[2])
chk(T, "-grad V == E (finite differences)", -grad(V, [0.3, -1.2, 0.7]), [3, 4, -2], atol=1e-6)
chk(T, "V(P3)-V(P1) from V function [V]", V(P3) - V(P1), -18)

# ====================================================================================== 6.3
T = "6.3"
print(f"\n=== {T} A field at a metal surface ===")
f = lambda r: 3 * r[0] + 4 * r[1]
p0 = np.array([4.0, 0.0, 0.0])                     # 3*4 = 12: on the surface
n = normal_2_to_1(f, p0, lambda r: f(r) > 12)      # medium 1 = free space (outside the metal)
chk(T, "n-hat out of the metal", n, [0.6, 0.8, 0])
opts = {"a": [4, 3, 0], "b": [-6, -8, 0], "c": [3, 4, 5], "d": [8, -6, 0]}
page_nxE = {"a": [0, 0, -1.4], "b": [0, 0, 0], "c": [4, -3, 0], "d": [0, 0, -10]}
page_ndE = {"a": 4.8, "b": -10, "c": 5, "d": 0}
allowed = []
for k, Ev in opts.items():
    Ev = np.array(Ev, float)
    En, _, Et = split(Ev, n)
    chk(T, f"({k}) n x E [V/m]", np.cross(n, Ev), page_nxE[k], atol=1e-9)
    chk(T, f"({k}) n . E [V/m]", En, page_ndE[k], atol=1e-9)
    if np.linalg.norm(Et) < 1e-9:
        allowed.append(k)
chk_eq(T, "key (no tangential E outside metal)", allowed, ["b"])
chk(T, "(b) E = -10 n-hat: coefficient", np.dot(opts["b"], n), -10)
rho = np.dot(n, EPS0 * np.array(opts["b"], float))
chk(T, "rho_s [C/m^2] = -10 eps0", rho, -8.85e-11, atol=0.005e-11)

# ====================================================================================== 6.4
T = "6.4"
print(f"\n=== {T} Crossing a current sheet ===")
n = normal_2_to_1(lambda r: r[0], np.zeros(3), lambda r: r[0] > 0)
chk(T, "n-hat (2 -> 1)", n, [1, 0, 0])
Js = np.array([0, 0, 4.0])
H2 = np.array([3, -2, 0.0])
H1 = solve_side1(n, H2, 1.0, 1.0, Js, 0.0)          # free space both sides
chk(T, "H1x = H2x [A/m]", np.dot(H1, n), 3)
dHt = split(H1 - H2, n)[2]
chk(T, "jump a (y), b (z) [A/m]", [dHt[1], dHt[2]], [4, 0])
chk(T, "H1 [A/m]", H1, [3, 2, 0])
chk(T, "B1 [uT]", MU0 * H1 * 1e6, [3.77, 2.51, 0], atol=0.005)
chk(T, "B2 [uT]", MU0 * H2 * 1e6, [3.77, -2.51, 0], atol=0.005)
# brute force: wire-superposition field of the sheet + a uniform background fixed by H2
d = 1e-4
Hs_p, Hs_m = sheet_H(Js, n, d * n), sheet_H(Js, n, -d * n)
H0 = H2 - Hs_m
chk(T, "H1 by wire superposition [A/m]", H0 + Hs_p, [3, 2, 0], atol=1e-6)
# Ampere on the thin rectangle described in the Check
dd = 1e-6
C = [np.array(v) for v in ([dd, 0, 0], [dd, 2, 0], [-dd, 2, 0], [-dd, 0, 0])]
Hpw = lambda r: H1 if r[0] > 0 else H2
circ = sum(line_int(Hpw, C[i], C[(i + 1) % 4], lambda r: r[0], (0.0,))[0] for i in range(4))
nl = loop_normal(C)
chk(T, "loop normal (ccw seen from +z)", nl, [0, 0, 1], atol=1e-9)
chk(T, "loop circulation [A]", circ, 8, atol=1e-5)
chk(T, "enclosed current Js.n_loop * 2 m [A]", np.dot(Js, nl) * 2, 8)

# ====================================================================================== 6.5
T = "6.5"
print(f"\n=== {T} The flipped normal ===")
D_below, D_above = np.array([2, 0, 6.0]), np.array([2, 0, 1.0])  # nC/m^2
# student's labelling: medium 1 = below, medium 2 = above
n = normal_2_to_1(lambda r: r[2], np.zeros(3), lambda r: r[2] < 0)
chk(T, "correct n-hat (above=2 -> below=1)", n, [0, 0, -1])
chk(T, "student's value z.(D1-D2) [nC/m^2]", np.dot([0, 0, 1], D_below - D_above), 5)
chk(T, "rho_s, medium 1 below, n=-z [nC/m^2]", np.dot(n, D_below - D_above), -5)
n_b = normal_2_to_1(lambda r: r[2], np.zeros(3), lambda r: r[2] > 0)
chk(T, "rho_s, relabelled (1 above), n=+z [nC/m^2]", np.dot(n_b, D_above - D_below), -5)
# brute force: pillbox flux through a 2a x 2a x 2c box straddling z = 0
a, c = 0.5, 0.1
Dpw = lambda x, y, z: D_above if z > 0 else D_below
flux = 0.0
for sgn in (+1, -1):
    flux += integrate.dblquad(lambda y, x: sgn * Dpw(x, y, sgn * c)[2], -a, a, -a, a)[0]
    flux += integrate.dblquad(lambda z, y: sgn * Dpw(sgn * a, y, z)[0], -a, a, -c, c, epsabs=1e-12)[0]
    flux += integrate.dblquad(lambda z, x: sgn * Dpw(x, sgn * a, z)[1], -a, a, -c, c, epsabs=1e-12)[0]
chk(T, "pillbox flux / area [nC/m^2]", flux / (2 * a) ** 2, -5, atol=1e-6)
chk(T, "tangential D_x both sides [nC/m^2]", [D_below[0], D_above[0]], [2, 2])

# ====================================================================================== 6.6
T = "6.6"
print(f"\n=== {T} Circulation of two fields ===")
Ea = lambda r: np.array([2 * r[0] + r[1], r[0], 0.0])
Eb = lambda r: np.array([0.0, r[0] * r[1], 0.0])
O, A, B = np.array([0, 0, 0.0]), np.array([2, 0, 0.0]), np.array([2, 2, 0.0])
chk(T, "triangle O,A,B normal (ccw from +z)", loop_normal([O, A, B]), [0, 0, 1])
sa = [line_int(Ea, O, A)[0], line_int(Ea, A, B)[0], line_int(Ea, B, O)[0]]
sb = [line_int(Eb, O, A)[0], line_int(Eb, A, B)[0], line_int(Eb, B, O)[0]]
chk(T, "E_a sides OA, AB, BO [V]", sa, [4, 4, -8], atol=1e-9)
chk(T, "E_a circulation [V]", sum(sa), 0, atol=1e-9)
chk(T, "E_b sides OA, AB, BO [V]", sb, [0, 4, -8 / 3], atol=1e-9)
chk(T, "E_b circulation [V]", sum(sb), 4 / 3, atol=1e-9)
pts = np.random.default_rng(6).uniform(-3, 3, size=(5, 3))
chk(T, "curl E_a at 5 random points", max(np.abs(curl(Ea, p)).max() for p in pts), 0, atol=1e-7)
chk(T, "curl E_b - y z-hat at 5 random points",
    max(np.abs(curl(Eb, p) - np.array([0, 0, p[1]])).max() for p in pts), 0, atol=1e-7)
stokes = integrate.dblquad(lambda y, x: curl(Eb, [x, y, 0])[2], 0, 2, lambda x: 0, lambda x: x)[0]
chk(T, "Stokes: flux of curl E_b through triangle [V]", stokes, 4 / 3, atol=1e-7)
chk(T, "V(B)-V(O) along O->A->B [V]", -(sa[0] + sa[1]), -8)
chk(T, "V(B)-V(O) along straight O->B [V]", -line_int(Ea, O, B)[0], -8)
Vp = lambda r: -(r[0] ** 2 + r[0] * r[1])
chk(T, "-grad V == E_a at a point", -grad(Vp, [0.7, -1.1, 0]) - Ea([0.7, -1.1, 0]), [0, 0, 0], atol=1e-6)
chk(T, "V(B)-V(O) from V=-(x^2+xy) [V]", Vp(B) - Vp(O), -8)
chk(T, "E_b: O->A->B, straight O->B [V]", [sb[0] + sb[1], line_int(Eb, O, B)[0]], [4, 8 / 3], atol=1e-9)

# ====================================================================================== 6.7
T = "6.7"
print(f"\n=== {T} A charged tilted interface ===")
f = lambda r: r[0] + 2 * r[1] + 2 * r[2]
n = normal_2_to_1(f, np.zeros(3), lambda r: f(r) > 0)     # medium 1 = vacuum side
chk(T, "n-hat (dielectric -> vacuum)", n, np.array([1, 2, 2]) / 3)
E2 = np.array([3, 1, 2.0])
E2n, E2nv, E2t = split(E2, n)
chk(T, "E2n [V/m]", E2n, 3)
chk(T, "E2 normal part [V/m]", E2nv, [1, 2, 2])
chk(T, "E2t [V/m]", E2t, [2, -1, 0])
chk(T, "E2t . n", np.dot(E2t, n), 0, atol=1e-12)
E1 = solve_side1(n, E2, 1.0, 2.0, np.zeros(3), 3.0)      # eps1 = eps0, eps2 = 2 eps0, rho_s = 3 eps0
D1, D2 = 1.0 * E1, 2.0 * E2
chk(T, "D2n, D1n [eps0]", [np.dot(D2, n), np.dot(D1, n)], [6, 9])
chk(T, "E1n [V/m]", np.dot(E1, n), 9)
chk(T, "E1 [V/m]", E1, [5, 5, 6])
chk(T, "D1 [eps0 C/m^2]", D1, [5, 5, 6])
chk(T, "D2 [eps0 C/m^2]", D2, [6, 2, 4])
chk(T, "D1 - D2 [eps0]", D1 - D2, [-1, 3, 2])
chk(T, "n.(D1-D2) [eps0]", np.dot(n, D1 - D2), 3)
chk(T, "E1 - E2 [V/m]", E1 - E2, [2, 4, 4])
chk(T, "n x (E1-E2)", np.cross(n, E1 - E2), [0, 0, 0], atol=1e-12)
tot = np.dot(n, E1 - E2)
chk(T, "total surface charge [eps0]", tot, 6)
chk(T, "bound rho_sb [eps0]", tot - 3, 3)
chk(T, "bound rho_sb [C/m^2]", (tot - 3) * EPS0, 2.66e-11, atol=0.005e-11)
P2 = D2 - E2
chk(T, "P2 [eps0]", P2, [3, 1, 2])
chk(T, "P2 . n (n = outward from dielectric) [eps0]", np.dot(P2, n), 3)
chk(T, "D2t, D1t [eps0]", np.concatenate([split(D2, n)[2], split(D1, n)[2]]), [4, -2, 0, 2, -1, 0])

# ====================================================================================== 6.8
T = "6.8"
print(f"\n=== {T} Refraction of field lines ===")
n = normal_2_to_1(lambda r: r[1], np.zeros(3), lambda r: r[1] > 0)
chk(T, "n-hat (glass -> air)", n, [0, 1, 0])
th1 = np.radians(30)
E1 = 200 * np.array([np.sin(th1), np.cos(th1), 0])
chk(T, "E1 [V/m]", E1, [100, 173.2, 0], atol=0.05)
E2 = solve_side2(n, E1, 1.0, 3.0, np.zeros(3), 0.0)
E2n, _, E2t = split(E2, n)
chk(T, "E2 [V/m]", E2, [100, 57.7, 0], atol=0.05)
chk(T, "|E2| [V/m] (=200/sqrt3)", np.linalg.norm(E2), [115.5], atol=0.05)
chk(T, "|E2| exact", np.linalg.norm(E2), 200 / np.sqrt(3))
th2 = np.degrees(np.arctan2(np.linalg.norm(E2t), E2n))
chk(T, "theta2 [deg]", th2, 60)
chk(T, "tan th1 / tan th2 (= eps1/eps2)", np.tan(th1) / np.tan(np.radians(th2)), 1 / 3)
chk(T, "D1 [nC/m^2]", EPS0 * E1[:2] * 1e9, [0.885, 1.53], atol=[0.0005, 0.005])
chk(T, "D2 [nC/m^2]", EPS0 * 3 * E2[:2] * 1e9, [2.66, 1.53], atol=0.005)
rsb = np.dot(n, E1 - E2)
chk(T, "rho_sb [eps0] (=200/sqrt3)", rsb, 200 / np.sqrt(3))
chk(T, "rho_sb [C/m^2]", rsb * EPS0, 1.02e-9, atol=0.005e-9)
chk(T, "P2 . n (glass outward normal +y) [eps0]", np.dot(3 * E2 - E2, n), 115.5, atol=0.05)
# (e) water (medium 2, eps_r 81) below air (medium 1), no free charge
Ew = np.array([np.sin(np.radians(45)), np.cos(np.radians(45)), 0])
Ea_ = solve_side1(n, Ew, 1.0, 81.0, np.zeros(3), 0.0)
th_air = np.degrees(np.arctan2(np.linalg.norm(split(Ea_, n)[2]), np.dot(Ea_, n)))
chk(T, "(e) angle in air [deg]", th_air, 0.71, atol=0.005)

# ====================================================================================== 6.9
T = "6.9"
print(f"\n=== {T} Two tilted charged planes ===")
f9 = lambda r: 3 * r[0] + 4 * r[2]
Apt, Bpt, Cpt = np.array([0, 0, 0.0]), np.array([2, 0, 1.0]), np.array([2, 0, -2.0])
inM = lambda r: 0 < f9(r) < 10
inR = lambda r: f9(r) > 10
nP = normal_2_to_1(f9, Apt, inM)          # at P: medium 1 = M, medium 2 = L
nQ = normal_2_to_1(f9, Bpt, inR)          # at Q: medium 1 = R, medium 2 = M
chk(T, "n-hat at P (L -> M)", nP, [0.6, 0, 0.8])
chk(T, "n-hat at Q (M -> R)", nQ, [0.6, 0, 0.8])
tQ = optimize.brentq(lambda t: f9(Apt + t * nP) - 10, 0, 100, xtol=1e-14)
chk(T, "distance between planes [m]", tQ, 2)
D_M = np.array([7, 2, 1.0])
DMn, _, DMt = split(D_M, nP)
chk(T, "D_Mn [eps0]", DMn, 5)
chk(T, "D_Mt [eps0]", DMt, [4, 2, -3])
D_L = solve_side2(nP, D_M, 1.0, 1.0, np.zeros(3), 5.0)   # vacuum: E = D/eps0 on both sides
chk(T, "D_Ln [eps0]", np.dot(D_L, nP), 0, atol=1e-12)
chk(T, "D_L [eps0] (= E_L in V/m)", D_L, [4, 2, -3])
Asys = np.vstack([X(nQ), [1, 0, 0]])
bsys = np.concatenate([X(nQ) @ D_M, [1.0]])
D_R = np.linalg.lstsq(Asys, bsys, rcond=None)[0]
assert np.allclose(Asys @ D_R, bsys)
chk(T, "D_Rn [eps0]", np.dot(D_R, nQ), -5)
chk(T, "D_R [eps0]", D_R, [1, 2, -7])
rhoQ = np.dot(nQ, D_R - D_M)
chk(T, "rho_sQ [eps0]", rhoQ, -10)
chk(T, "rho_sQ [C/m^2]", rhoQ * EPS0, -8.85e-11, atol=0.005e-11)


def E9(r):
    s = f9(r)
    return D_L if s < 0 else (D_M if s < 10 else D_R)


chk(T, "A on P, B on Q, C in L: f(A), f(B), f(C)", [f9(Apt), f9(Bpt), f9(Cpt)], [0, 10, -2])
IAB = line_int(E9, Apt, Bpt, f9, (0.0, 10.0))[0]
chk(T, "V(B)-V(A) [V]", -IAB, -15)
IBC, cross = line_int(E9, Bpt, Cpt, f9, (0.0, 10.0))
ICA = line_int(E9, Cpt, Apt, f9, (0.0, 10.0))[0]
chk(T, "B->C crossing point of P [m]", cross[0], [2, 0, -1.5], atol=1e-9)
chk(T, "B->C pieces in M, in L [V]",
    [line_int(E9, Bpt, cross[0])[0], line_int(E9, cross[0], Cpt)[0]], [-2.5, 1.5], atol=1e-9)
chk(T, "sides AB, BC, CA [V]", [IAB, IBC, ICA], [15, -1, -14], atol=1e-9)
chk(T, "circulation [V]", IAB + IBC + ICA, 0, atol=1e-9)
chk(T, "Check 1: D_Rn - D_Ln vs rho_P + rho_Q [eps0]", [np.dot(D_R - D_L, nP), 5 + rhoQ], [-5, -5])
Bp = Apt + tQ * nP
chk(T, "Check 2: B' [m]", Bp, [1.2, 0, 1.6], atol=1e-9)
chk(T, "Check 2: V(B')-V(A), V(B)-V(B') [V]",
    [-line_int(E9, Apt, Bp)[0], -line_int(E9, Bp, Bpt)[0]], [-10, -5], atol=1e-9)
chk(T, "Watch out: 1 V/m jump x 2 m [V]", 1 * 2, 2)

# ====================================================================================== 6.10
T = "6.10"
print(f"\n=== {T} Plates around a charged sheet ===")
xs = np.array([0.0, 2.0, 3.0])                     # metal face, sheet, metal face
Ex_planes = lambda x, q: float(np.sum(np.asarray(q) / 2 * np.sign(x - xs)))   # eps0 units
dV = lambda a_, b_, q: -integrate.quad(lambda x: Ex_planes(x, q), a_, b_, points=[2.0] if a_ < 2 < b_ else None)[0]
# unknown plane charges (eps0 units) from: zero field in both metals, V(2)-V(0) = -2, V(3)-V(0) = 6
rows, rhs = [], []
cols = np.eye(3)
rows.append([Ex_planes(-1, q) for q in cols]); rhs.append(0.0)
rows.append([Ex_planes(4, q) for q in cols]); rhs.append(0.0)
rows.append([dV(0, 2, q) for q in cols]); rhs.append(-2.0)
rows.append([dV(0, 3, q) for q in cols]); rhs.append(6.0)
q = np.linalg.lstsq(np.array(rows), np.array(rhs), rcond=None)[0]
assert np.allclose(np.array(rows) @ q, rhs)
EA, EB = Ex_planes(1.0, q), Ex_planes(2.5, q)
chk(T, "(a) E_A, E_B [V/m] (superposition solve)", [EA, EB], [1, -8])
# (b) boundary conditions with n-hat from medium 2 into medium 1
n0 = normal_2_to_1(lambda r: r[0], np.zeros(3), lambda r: 0 < r[0] < 2)          # metal(2) -> gap A(1)
n3 = normal_2_to_1(lambda r: r[0], np.array([3.0, 0, 0]), lambda r: 2 < r[0] < 3)  # metal(2) -> gap B(1)
n2 = normal_2_to_1(lambda r: r[0], np.array([2.0, 0, 0]), lambda r: 2 < r[0] < 3)  # gap A(2) -> gap B(1)
chk(T, "n-hats at x=0, x=3, sheet", np.concatenate([n0, n3, n2]), [1, 0, 0, -1, 0, 0, 1, 0, 0])
EvA, EvB, Ezero = np.array([EA, 0, 0]), np.array([EB, 0, 0]), np.zeros(3)
r0, r3, r2 = np.dot(n0, EvA - Ezero), np.dot(n3, EvB - Ezero), np.dot(n2, EvB - EvA)
chk(T, "(b) rho_s0, rho_s3, rho_s2 [eps0]", [r0, r3, r2], [1, 8, -9])
chk(T, "(b) same from superposition solve [eps0]", q, [1, -9, 8], atol=1e-9)
chk(T, "(b) in C/m^2", np.array([r0, r3, r2]) * EPS0, [8.85e-12, 7.08e-11, -7.97e-11],
    atol=[0.005e-12, 0.005e-11, 0.005e-11])
chk(T, "(c) sum [eps0]", r0 + r3 + r2, 0, atol=1e-12)
chk(T, "(c) superposed E: x<0, gapA, gapB, x>3",
    [Ex_planes(-0.5, q), Ex_planes(1, q), Ex_planes(2.5, q), Ex_planes(3.5, q)], [0, 1, -8, 0])
chk(T, "(c) KVL V(3)-V(0) [V]", -(EA * 2 + EB * 1), 6)
# (d) wire: V(0) = V(3) = 0, sheet charge -9 eps0 fixed. Brute force: finite-difference Poisson.


def fd_poisson(V0, V3, rho_sheet, N=3000):
    h = 3.0 / N
    i2 = int(round(2.0 / h))
    M = N - 1
    ab = np.zeros((3, M))
    ab[0, 1:] = 1.0
    ab[1, :] = -2.0
    ab[2, :-1] = 1.0
    b = np.zeros(M)
    b[i2 - 1] = -h * h * (rho_sheet / h)          # V'' = -rho/eps0, rho = rho_s delta(x-2)
    b[0] -= V0
    b[-1] -= V3
    V = np.concatenate([[V0], linalg.solve_banded((1, 1), ab, b), [V3]])
    x = np.linspace(0, 3, N + 1)
    Ep = lambda xx: -np.interp(xx + h, x, V) / (2 * h) + np.interp(xx - h, x, V) / (2 * h)
    return V[i2], Ep(1.0), Ep(2.5)


Vs, EAf, EBf = fd_poisson(0.0, 6.0, -9.0)
chk(T, "(a) FD Poisson with battery: V(2), E_A, E_B", [Vs, EAf, EBf], [-2, 1, -8], atol=1e-6)
Vs2, EA2, EB2 = fd_poisson(0.0, 0.0, -9.0)
chk(T, "(d) FD Poisson: E_A', E_B' [V/m]", [EA2, EB2], [3, -6], atol=1e-6)
chk(T, "(d) FD Poisson: V(2) [V]", Vs2, -6, atol=1e-6)
r0d, r3d = np.dot(n0, [EA2, 0, 0]), np.dot(n3, [EB2, 0, 0])
chk(T, "(d) rho_s0', rho_s3' [eps0]", [r0d, r3d], [3, 6], atol=1e-6)
chk(T, "(d) in C/m^2", np.array([r0d, r3d]) * EPS0, [2.66e-11, 5.31e-11], atol=0.005e-11)
chk(T, "(d) plates total [eps0]", r0d + r3d, 9, atol=1e-6)
chk(T, "(d) fraction on nearer plate (x=3)", r3d / (r0d + r3d), 2 / 3, atol=1e-6)
rs, a_, d_ = -9.0, 2.0, 3.0
chk(T, "(d) general formula -rho(d-a)/d, -rho a/d", [-rs * (d_ - a_) / d_, -rs * a_ / d_], [3, 6])
qd = [r0d, rs, r3d]
chk(T, "(d) Check: superposed E for x<0, x>3", [Ex_planes(-1, qd), Ex_planes(4, qd)], [0, 0], atol=1e-6)
chk(T, "(d) Check: V(3)-V(0) [V]", -(EA2 * 2 + EB2 * 1), 0, atol=1e-6)
chk(T, "Watch out: wrong normal face charge, sum", [np.dot([1, 0, 0], EvB), r0 + r2 + np.dot([1, 0, 0], EvB)], [-8, -16])

# ====================================================================================== 6.11
T = "6.11"
print(f"\n=== {T} Charged shell in a dielectric ===")
ph, z0 = 0.7, 0.3
pnt = np.array([2 * np.cos(ph), 2 * np.sin(ph), z0])
rhat = np.array([np.cos(ph), np.sin(ph), 0])
phat = np.array([-np.sin(ph), np.cos(ph), 0])
zhat = np.array([0, 0, 1.0])
cyl = lambda v: np.array([np.dot(v, rhat), np.dot(v, phat), np.dot(v, zhat)])
fr = lambda r: np.sqrt(r[0] ** 2 + r[1] ** 2)
n = normal_2_to_1(fr, pnt, lambda r: fr(r) > 2)          # core (2) -> dielectric (1)
chk(T, "n-hat == r-hat", n, rhat)
E2 = 6 * rhat + 3 * zhat
Asys = np.vstack([X(n), n])
bsys = np.concatenate([X(n) @ E2, [1.0]])                 # tangential continuity + measured E_r(2+) = 1
E1 = np.linalg.lstsq(Asys, bsys, rcond=None)[0]
assert np.allclose(Asys @ E1, bsys)
chk(T, "(a) E1 (r, phi, z) [V/m]", cyl(E1), [1, 0, 3], atol=1e-12)
D1, D2 = 4 * E1, 1 * E2
chk(T, "(a) D1 (r, phi, z) [eps0]", cyl(D1), [4, 0, 12], atol=1e-12)
rs11 = np.dot(n, D1 - D2)
chk(T, "(b) rho_s [eps0]", rs11, -2)
chk(T, "(b) rho_s [C/m^2]", rs11 * EPS0, -1.77e-11, atol=0.005e-11)
tot = np.dot(n, E1 - E2)
chk(T, "(c) total, bound [eps0]", [tot, tot - rs11], [-5, -3])
chk(T, "(c) bound [C/m^2]", (tot - rs11) * EPS0, -2.66e-11, atol=0.005e-11)
P1 = D1 - E1
chk(T, "(c) P1 (r, phi, z) [eps0]", cyl(P1), [3, 0, 9], atol=1e-12)
chk(T, "(c) P1 . (-r-hat) [eps0]", np.dot(P1, -rhat), -3)
# (d) Gauss: closed cylinder r = 2-, length 1 (side + two caps) with E(2-) = 6 r + 3 z
side = integrate.dblquad(lambda p_, z_: np.dot(6 * np.array([np.cos(p_), np.sin(p_), 0]) + 3 * zhat,
                                                np.array([np.cos(p_), np.sin(p_), 0])) * 2.0,
                         0, 1, 0, 2 * np.pi)[0]
caps = sum(integrate.dblquad(lambda p_, r_, s=s: s * 3.0 * r_, 0, 2, 0, 2 * np.pi)[0] for s in (+1, -1))
chk(T, "(d) rho_l = eps0 * flux [eps0 C/m]", side + caps, 24 * np.pi, atol=1e-8)
# independent: Coulomb integral of a long line charge (unit rho_l) -> E_r at r = 2
Er_unit = integrate.quad(lambda zp: 1 / (4 * np.pi * EPS0) * 2.0 / (4 + zp ** 2) ** 1.5, -1e5, 1e5,
                         points=[0.0], limit=500)[0]
chk(T, "(d) rho_l from Coulomb sum [C/m]", 6 / Er_unit, 6.68e-10, atol=0.005e-10)
E1n, _, E1t = split(E1, n)
E2n, _, E2t = split(E2, n)
t2 = np.degrees(np.arctan2(np.linalg.norm(E2t), E2n))
t1 = np.degrees(np.arctan2(np.linalg.norm(E1t), E1n))
chk(T, "(e) theta2, theta1 [deg]", [t2, t1], [26.6, 71.6], atol=0.05)
chk(T, "(e) tan ratio", np.tan(np.radians(t1)) / np.tan(np.radians(t2)), 6)
E1_0 = solve_side1(n, E2, 4.0, 1.0, np.zeros(3), 0.0)
chk(T, "(e) rho_s=0: E_r(2+), tan th1, ratio",
    [np.dot(E1_0, n), np.linalg.norm(split(E1_0, n)[2]) / np.dot(E1_0, n),
     np.linalg.norm(split(E1_0, n)[2]) / np.dot(E1_0, n) / np.tan(np.radians(t2))], [1.5, 2, 4])
chk(T, "Check: free charge per m inside 2+, D_r*2pi*2 [eps0]",
    [24 * np.pi + 2 * np.pi * 2 * rs11, np.dot(D1, n) * 2 * np.pi * 2], [16 * np.pi, 16 * np.pi])

# ====================================================================================== 6.12
T = "6.12"
print(f"\n=== {T} A tilted current sheet ===")
f12 = lambda r: 3 * r[1] + 4 * r[2]
n = normal_2_to_1(f12, np.zeros(3), lambda r: f12(r) > 0)
chk(T, "(a) n-hat (2 -> 1)", n, [0, 0.6, 0.8])
Js = np.array([5.0, 0, 0])
chk(T, "(a) Js . n", np.dot(Js, n), 0, atol=1e-12)
H2 = np.array([2, 3, 4.0])
H2n, H2nv, H2t = split(H2, n)
chk(T, "(b) H2n [A/m]", H2n, 5)
chk(T, "(b) normal part, H2t [A/m]", np.concatenate([H2nv, H2t]), [0, 3, 4, 2, 0, 0])
H1 = solve_side1(n, H2, 1.0, 1.0, Js, 0.0)
dH = H1 - H2
chk(T, "(c) Delta H_t [A/m]", split(dH, n)[2], [0, -4, 3])
chk(T, "(c) H1t [A/m]", split(H1, n)[2], [2, -4, 3])
chk(T, "(c) H1 [A/m]", H1, [2, -1, 7])
chk(T, "(c) B1 [uT]", MU0 * H1 * 1e6, [2.51, -1.26, 8.80], atol=0.005)
chk(T, "(c) n.(H1-H2), n x (H1-H2)", np.concatenate([[np.dot(n, dH)], np.cross(n, dH)]), [0, 5, 0, 0], atol=1e-12)
d = 1e-4
Hs_p, Hs_m = sheet_H(Js, n, d * n), sheet_H(Js, n, -d * n)
chk(T, "(c) H1 by wire superposition [A/m]", (H2 - Hs_m) + Hs_p, [2, -1, 7], atol=1e-6)
seg = np.array([0, 4, -3.0])
chk(T, "(d) segment in sheet: f(end)", f12(seg), 0)
L = np.linalg.norm(seg)
tt = seg / L
m = np.cross(tt, n)
chk(T, "(d) length, t-hat, m-hat", np.concatenate([[L], tt, m]), [5, 0, 0.8, -0.6, 1, 0, 0], atol=1e-12)
I = integrate.quad(lambda s: np.dot(Js, m), 0, L)[0]
chk(T, "(d) current through segment [A] (along +m = +x)", I, 25)
Hp = np.array([2, -1, 9.0])
chk(T, "(e) partner's n.H1 [A/m]", np.dot(n, Hp), 6.6)
chk(T, "(e) B_n jump [T]", MU0 * (np.dot(n, Hp) - H2n), 2.01e-6, atol=0.005e-6)
dd = 1e-6
C = [-dd * n, -dd * n + 3 * tt, dd * n + 3 * tt, dd * n]
Hpw = lambda r: H1 if f12(r) > 0 else H2
circ = sum(line_int(Hpw, C[i], C[(i + 1) % 4], f12, (0.0,))[0] for i in range(4))
nl = loop_normal(C)
chk(T, "Check: loop normal (t x n)", nl, np.cross(tt, n), atol=1e-9)
chk(T, "Check: H2.t, H1.t [A/m]", [np.dot(H2, tt), np.dot(H1, tt)], [0, -5], atol=1e-12)
chk(T, "Check: circulation, enclosed [A]", [circ, np.dot(Js, nl) * 3], [15, 15], atol=1e-5)
chk(T, "Watch out: H1 with n x Js [A/m]", H2 + np.cross(n, Js), [2, 7, 1])

print(f"\nTOTAL: {N_PASS} PASS, {N_FAIL} FAIL")
