#!/usr/bin/env python3
"""Numerical verification of every answer on practice/06-circulation-and-boundary-conditions.md.

numpy/scipy only. Every boundary condition is checked with explicit np.dot / np.cross,
every circulation with scipy.integrate.quad along parameterized straight legs,
curls with central finite differences, Stokes with dblquad, Gauss with a numerical flux.
Convention: n points FROM medium 2 INTO medium 1:
    n.(D1-D2) = rho_s,  n x (E1-E2) = 0,  n.(B1-B2) = 0,  n x (H1-H2) = Js.
"""
import numpy as np
from scipy.integrate import quad, dblquad

EPS0 = 8.8541878128e-12
MU0 = 4e-7 * np.pi

np.set_printoptions(precision=6, suppress=True)


def unit(v):
    v = np.asarray(v, float)
    return v / np.linalg.norm(v)


def split(v, n):
    """normal scalar component and tangential vector part of v w.r.t. unit normal n"""
    vn = float(np.dot(v, n))
    return vn, np.asarray(v, float) - vn * n


def leg(field, P, Q, points=None):
    """straight-line integral of field . dl from P to Q (r = P + t(Q-P), dl = (Q-P) dt)"""
    P, Q = np.asarray(P, float), np.asarray(Q, float)
    d = Q - P
    val, err = quad(lambda t: float(np.dot(field(P + t * d), d)), 0.0, 1.0,
                    points=points, limit=200, epsabs=1e-12, epsrel=1e-12)
    return val


def loop(field, corners, points_per_leg=None):
    vals = []
    for i in range(len(corners)):
        P, Q = corners[i], corners[(i + 1) % len(corners)]
        pts = None if points_per_leg is None else points_per_leg[i]
        vals.append(leg(field, P, Q, pts))
    return vals


def curl_fd(F, r, h=1e-5):
    r = np.asarray(r, float)
    J = np.zeros((3, 3))  # J[i,j] = dF_i/dx_j
    for j in range(3):
        e = np.zeros(3); e[j] = h
        J[:, j] = (np.asarray(F(r + e)) - np.asarray(F(r - e))) / (2 * h)
    return np.array([J[2, 1] - J[1, 2], J[0, 2] - J[2, 0], J[1, 0] - J[0, 1]])


def check(label, cond):
    print(f"   [{'OK' if cond else 'FAIL'}] {label}")
    if not cond:
        raise SystemExit(f"CHECK FAILED: {label}")


def hdr(s):
    print("\n" + "=" * 78 + "\n" + s + "\n" + "=" * 78)


print(f"eps0 = {EPS0:.10e} F/m, mu0 = {MU0:.10e} H/m")

# ---------------------------------------------------------------------------------
hdr("6.1  What is always continuous (MC)")
# Interface with eps1 = 2 eps0, eps2 = 5 eps0, rho_s != 0. Test with an arbitrary field.
e1r, e2r = 2.0, 5.0
n = np.array([0.0, 0.0, 1.0])
E2 = np.array([1.3, -0.7, 2.1])        # arbitrary field in medium 2 (V/m)
rho_s = 4.0 * EPS0                      # arbitrary nonzero free charge
E2n, E2t = split(E2, n)
E1t = E2t                               # tangential E continuous (thin loop)
D1n = e2r * EPS0 * E2n + rho_s          # pillbox
E1 = E1t + (D1n / (e1r * EPS0)) * n
D1, D2 = e1r * EPS0 * E1, e2r * EPS0 * E2
print("   E1 =", E1, " E2 =", E2)
check("(c) n x (E1-E2) = 0 (tangential E continuous)", np.allclose(np.cross(n, E1 - E2), 0))
print(f"   (a) E1n - E2n = {np.dot(n, E1 - E2):.6f} V/m  (nonzero -> E_n jumps)")
print(f"   (b) n.(D1-D2)/eps0 = {np.dot(n, D1 - D2) / EPS0:.6f}  (= rho_s/eps0 = 4, nonzero)")
D1t, D2t = D1 - np.dot(D1, n) * n, D2 - np.dot(D2, n) * n
print(f"   (d) D1t/D2t = {D1t[0] / D2t[0]:.6f} = eps1/eps2 = {e1r / e2r:.6f} = 2/5")
print(f"   (e) |E1| = {np.linalg.norm(E1):.6f}, |E2| = {np.linalg.norm(E2):.6f} (differ)")
# follow-up: rho_s = 0
D1n0 = e2r * EPS0 * E2n
E1_0 = E1t + (D1n0 / (e1r * EPS0)) * n
check("follow-up: rho_s=0 -> D_n continuous", np.isclose(e1r * E1_0[2], e2r * E2[2]))
print(f"   follow-up: E1n/E2n = {E1_0[2] / E2[2]:.6f} = eps2/eps1 = 2.5 (E_n still jumps)")

# ---------------------------------------------------------------------------------
hdr("6.2  Kirchhoff around a triangle (uniform E)")
E = lambda r: np.array([3.0, 4.0, -2.0])
P1, P2, P3 = (0, 0, 0), (2, 0, 0), (2, 3, 0)
legs = loop(E, [P1, P2, P3])
print(f"   legs P1->P2, P2->P3, P3->P1: {legs[0]:.6f}, {legs[1]:.6f}, {legs[2]:.6f} V")
print(f"   circulation = {sum(legs):.3e} V")
check("legs = 6, 12, -18", np.allclose(legs, [6, 12, -18]))
check("circulation 0", abs(sum(legs)) < 1e-12)
dV = -(legs[0] + legs[1])
dV_alt = -(-legs[2])  # along the slant side traversed P1->P3
print(f"   V(P3)-V(P1) = {dV:.6f} V (via P2), {dV_alt:.6f} V (via slant side)")
check("V(P3)-V(P1) = -18 V", np.isclose(dV, -18) and np.isclose(dV_alt, -18))
# slant-leg parameterization in the solution: dl = (-2,-3,0) dt, E.dl = -18 dt
print(f"   slant leg integrand E.(-2,-3,0) = {np.dot(E(0), [-2, -3, 0]):.1f} per unit t")

# ---------------------------------------------------------------------------------
hdr("6.3  A field at a metal surface (MC)")
n = unit([3, 4, 0])   # out of the metal (metal where 3x+4y<12)
print("   n =", n)
opts = {"a": [4, 3, 0], "b": [-6, -8, 0], "c": [3, 4, 5], "d": [8, -6, 0]}
for k, v in opts.items():
    v = np.array(v, float)
    c = np.cross(n, v)
    print(f"   ({k}) E = {v}:  n x E = {c},  n.E = {np.dot(n, v):.6f}  -> "
          f"{'allowed' if np.allclose(c, 0) else 'tangential part, NOT allowed'}")
check("(a) n x E = -7/5 z", np.allclose(np.cross(n, opts['a']), [0, 0, -1.4]))
check("(b) only allowed option", np.allclose(np.cross(n, opts['b']), 0))
check("(b) E = -10 n", np.allclose(np.array(opts['b']), -10 * n))
check("(c) z-hat is tangential: n.z = 0", np.dot(n, [0, 0, 1]) == 0)
check("(d) purely tangential: n.E = 0", abs(np.dot(n, opts['d'])) < 1e-12)
rho = np.dot(n, EPS0 * np.array(opts['b'], float))
print(f"   rho_s = n.D = {rho / EPS0:.6f} eps0 = {rho:.4e} C/m^2")
check("rho_s = -10 eps0 = -8.85e-11", np.isclose(rho / EPS0, -10) and np.isclose(rho, -8.854e-11, rtol=1e-3))

# ---------------------------------------------------------------------------------
hdr("6.4  Crossing a current sheet (x = 0, Js = 4 z)")
n = np.array([1.0, 0, 0])            # from medium 2 (x<0) into medium 1 (x>0)
Js = np.array([0, 0, 4.0])
H2 = np.array([3.0, -2.0, 0])
H2n, H2t = split(H2, n)
H1 = H2n * n + H2t + np.cross(Js, n)  # Bn continuous (free space); Ht jump = Js x n
print("   Js x n =", np.cross(Js, n), " H1 =", H1, "A/m")
check("H1 = 3x + 2y", np.allclose(H1, [3, 2, 0]))
check("n x (H1-H2) = Js", np.allclose(np.cross(n, H1 - H2), Js))
B1, B2 = MU0 * H1, MU0 * H2
check("n.(B1-B2) = 0", abs(np.dot(n, B1 - B2)) < 1e-18)
print(f"   B1 = {B1 * 1e6} uT,  B2 = {B2 * 1e6} uT")
check("B1 ~ (3.77, 2.51, 0) uT", np.allclose(np.round(B1 * 1e6, 2), [3.77, 2.51, 0]))
check("B2 ~ (3.77, -2.51, 0) uT", np.allclose(np.round(B2 * 1e6, 2), [3.77, -2.51, 0]))
# hint route: x x (a y + b z) = a z - b y
a, b = 4.0, 0.0
check("x x (a y + b z) = a z - b y with a=4, b=0 gives Js", np.allclose(np.cross(n, [0, a, b]), Js))
# brute-force Ampere: thin loop in the xy-plane, ccw from +z (dS = +z), long sides along y
h, L = 1e-3, 2.0
Hfield = lambda r: H1 if r[0] > 0 else H2
corners = [(h, 0, 0), (h, L, 0), (-h, L, 0), (-h, 0, 0)]
pts = [None, [0.5], None, [0.5]]
circ = sum(loop(Hfield, corners, pts))
print(f"   Ampere loop: circulation = {circ:.6f} A, enclosed J_s L = {Js[2] * L:.6f} A")
check("Ampere thin loop", np.isclose(circ, Js[2] * L))

# ---------------------------------------------------------------------------------
hdr("6.5  The flipped normal (find the error)")
Dbelow = np.array([2.0, 0, 6.0])   # nC/m^2
Dabove = np.array([2.0, 0, 1.0])
student = np.dot([0, 0, 1], Dbelow - Dabove)
fix1 = np.dot([0, 0, -1], Dbelow - Dabove)   # medium 1 below, n = -z
fix2 = np.dot([0, 0, 1], Dabove - Dbelow)    # medium 1 above, n = +z
print(f"   student: {student:+.1f} nC/m^2;  corrected: {fix1:+.1f} (n=-z), {fix2:+.1f} (relabelled)")
check("correct rho_s = -5 nC/m^2", fix1 == -5 and fix2 == -5 and student == 5)
check("tangential D_x equal (2 = 2)", Dbelow[0] == Dabove[0] == 2)

# ---------------------------------------------------------------------------------
hdr("6.6  Circulation of two fields (triangle O-A-B)")
E1f = lambda r: np.array([2 * r[0] + r[1], r[0], 0.0])
E2f = lambda r: np.array([0.0, r[0] * r[1], 0.0])
O, A, B = (0, 0, 0), (2, 0, 0), (2, 2, 0)
l1 = loop(E1f, [O, A, B]); l2 = loop(E2f, [O, A, B])
print(f"   E1 legs OA, AB, BO: {l1[0]:.6f}, {l1[1]:.6f}, {l1[2]:.6f}; circulation {sum(l1):.2e} V")
print(f"   E2 legs OA, AB, BO: {l2[0]:.6f}, {l2[1]:.6f}, {l2[2]:.6f}; circulation {sum(l2):.6f} V (4/3 = {4/3:.6f})")
check("E1 legs 4, 4, -8; circ 0", np.allclose(l1, [4, 4, -8]) and abs(sum(l1)) < 1e-12)
check("E2 legs 0, 4, -8/3; circ 4/3", np.allclose(l2, [0, 4, -8 / 3]) and np.isclose(sum(l2), 4 / 3))
rng = np.random.default_rng(6)
for r in rng.uniform(-3, 3, size=(3, 3)):
    c1, c2 = curl_fd(E1f, r), curl_fd(E2f, r)
    print(f"   at r={r}: curl E1 = {c1}, curl E2 = {c2} (expect (0,0,y)=(0,0,{r[1]:.4f}))")
    check("curl E1 = 0", np.allclose(c1, 0, atol=1e-6))
    check("curl E2 = y z", np.allclose(c2, [0, 0, r[1]], atol=1e-6))
stokes, _ = dblquad(lambda y, x: y, 0, 2, lambda x: 0.0, lambda x: x)  # (curl E2).z over triangle, dS=+z
print(f"   Stokes: flux of curl E2 through triangle (dS = +z) = {stokes:.6f} V")
check("Stokes 4/3", np.isclose(stokes, 4 / 3))
# potential of E1: V = -(x^2 + x y)
V = lambda r: -(r[0] ** 2 + r[0] * r[1])
for r in rng.uniform(-3, 3, size=(2, 3)):
    gradV = np.array([(V(r + e) - V(r - e)) / 2e-6 for e in np.eye(3) * 1e-6])
    check(f"-grad V = E1 at {np.round(r, 3)}", np.allclose(-gradV, E1f(r), atol=1e-6))
dVB = V(np.array(B, float)) - V(np.array(O, float))
print(f"   V(B)-V(O) = {dVB:.6f} V; -(OA+AB legs) = {-(l1[0] + l1[1]):.6f} V")
check("V(B)-V(O) = -8 V", np.isclose(dVB, -8))
pA = l2[0] + l2[1]; pS = leg(E2f, O, B)
print(f"   E2: O->A->B gives {pA:.6f} V, straight O->B gives {pS:.6f} V, difference {pA - pS:.6f} V")
check("E2 path dependence 4 vs 8/3", np.isclose(pA, 4) and np.isclose(pS, 8 / 3) and np.isclose(pA - pS, 4 / 3))

# ---------------------------------------------------------------------------------
hdr("6.7  A charged tilted interface (x + 2y + 2z = 0)")
n = unit([1, 2, 2])                    # into medium 1 (vacuum, x+2y+2z>0)
print("   n =", n, "(= (1,2,2)/3)")
check("n = (1,2,2)/3", np.allclose(n, np.array([1, 2, 2]) / 3))
eps1, eps2 = 1.0 * EPS0, 2.0 * EPS0
rho_s = 3 * EPS0
E2 = np.array([3.0, 1.0, 2.0])
E2n, E2t = split(E2, n)
print(f"   E2n = {E2n:.6f} V/m, E2n*n = {E2n * n}, E2t = {E2t} V/m, E2t.n = {np.dot(E2t, n):.1e}")
check("E2n = 3, E2t = 2x - y", np.isclose(E2n, 3) and np.allclose(E2t, [2, -1, 0]))
D2n = eps2 * E2n
D1n = D2n + rho_s
E1n = D1n / eps1
E1 = E2t + E1n * n
print(f"   D2n = {D2n / EPS0:.6f} eps0, D1n = {D1n / EPS0:.6f} eps0, E1n = {E1n:.6f} V/m")
print("   E1 =", E1, "V/m")
check("E1 = 5x + 5y + 6z", np.allclose(E1, [5, 5, 6]))
D1, D2 = eps1 * E1, eps2 * E2
print("   D1/eps0 =", D1 / EPS0, " D2/eps0 =", D2 / EPS0)
check("D1 = eps0(5,5,6), D2 = eps0(6,2,4)", np.allclose(D1 / EPS0, [5, 5, 6]) and np.allclose(D2 / EPS0, [6, 2, 4]))
print(f"   n.(D1-D2) = {np.dot(n, D1 - D2) / EPS0:.6f} eps0 (rho_s = 3 eps0); "
      f"(D1-D2)/eps0 = {(D1 - D2) / EPS0} -> (-1 + 2*3 + 2*2)/3")
check("n.(D1-D2) = rho_s", np.isclose(np.dot(n, D1 - D2), rho_s))
print("   n x (E1-E2) =", np.cross(n, E1 - E2), "; E1-E2 =", E1 - E2, "; (1,2,2)x(2,4,4) =",
      np.cross([1, 2, 2], [2, 4, 4]))
check("n x (E1-E2) = 0", np.allclose(np.cross(n, E1 - E2), 0))
tot = np.dot(n, EPS0 * E1 - EPS0 * E2)
rho_sb = tot - rho_s
print(f"   total surface charge = {tot / EPS0:.6f} eps0, rho_sb = {rho_sb / EPS0:.6f} eps0 = {rho_sb:.4e} C/m^2")
check("total 6 eps0, bound 3 eps0 = 2.66e-11", np.isclose(tot / EPS0, 6) and np.isclose(rho_sb / EPS0, 3)
      and np.isclose(rho_sb, 2.656e-11, rtol=1e-3))
P2 = D2 - EPS0 * E2
print(f"   cross-check P2 = {P2 / EPS0} eps0, P2.n_out (n_out = +n) = {np.dot(P2, n) / EPS0:.6f} eps0")
check("P2.n = 3 eps0", np.isclose(np.dot(P2, n) / EPS0, 3))
D1t, D2t = D1 - np.dot(D1, n) * n, D2 - np.dot(D2, n) * n
print(f"   tangential D: D2t = {D2t / EPS0} eps0, D1t = {D1t / EPS0} eps0 (halves)")
check("D2t = eps0(4,-2,0), D1t = eps0(2,-1,0)", np.allclose(D2t / EPS0, [4, -2, 0]) and np.allclose(D1t / EPS0, [2, -1, 0]))

# ---------------------------------------------------------------------------------
hdr("6.8  Refraction of field lines (air over glass, y = 0)")
n = np.array([0, 1.0, 0])     # from glass (2) into air (1)
eps1, eps2 = 1.0, 3.0         # relative
th1 = np.radians(30)
E1 = 200 * np.array([np.sin(th1), np.cos(th1), 0])
E1n, E1t = split(E1, n)
E2t = E1t
E2n = eps1 * E1n / eps2
E2 = E2t + E2n * n
th2 = np.degrees(np.arctan2(np.linalg.norm(E2t), E2n))
print("   E1 =", E1, f"(E1t = {np.linalg.norm(E1t):.4f}, E1n = {E1n:.4f} = 100 sqrt3 = {100 * np.sqrt(3):.4f})")
print("   E2 =", E2, f"|E2| = {np.linalg.norm(E2):.4f} (200/sqrt3 = {200 / np.sqrt(3):.4f}), theta2 = {th2:.4f} deg")
check("E2 = 100x + 57.7y, |E2| = 115.5, theta2 = 60", np.allclose(np.round(E2, 1), [100, 57.7, 0])
      and np.isclose(round(np.linalg.norm(E2), 1), 115.5) and np.isclose(th2, 60))
ratio = np.tan(th1) / np.tan(np.radians(th2))
print(f"   tan(th1)/tan(th2) = {ratio:.6f} = eps1/eps2 = {eps1 / eps2:.6f}")
check("refraction law 1/3", np.isclose(ratio, 1 / 3))
D1, D2 = eps1 * EPS0 * E1, eps2 * EPS0 * E2
print(f"   D1/eps0 = {D1 / EPS0}, D2/eps0 = {D2 / EPS0}")
print(f"   D1 = {D1 * 1e9} nC/m^2, D2 = {D2 * 1e9} nC/m^2")
check("D_y continuous, D_x triples", np.isclose(D1[1], D2[1]) and np.isclose(D2[0] / D1[0], 3))
check("D1 ~ (0.885, 1.53), D2 ~ (2.66, 1.53) nC/m^2",
      np.allclose(np.round(D1 * 1e9, 3)[:2], [0.885, 1.534]) and np.allclose(np.round(D2 * 1e9, 2)[:2], [2.66, 1.53]))
check("D2/eps0 = (300, 173.2)", np.allclose(np.round(D2 / EPS0, 1)[:2], [300, 173.2]))
rho_sb = EPS0 * (E1n - E2n)
print(f"   rho_sb = eps0 (E1n - E2n) = {(E1n - E2n):.4f} eps0 = {rho_sb:.4e} C/m^2 (200/sqrt3 eps0)")
check("rho_sb = 1.02e-9 C/m^2", np.isclose(rho_sb, 1.0224e-9, rtol=1e-3) and np.isclose(E1n - E2n, 200 / np.sqrt(3)))
P2 = D2 - EPS0 * E2
check("bound charge = P2.n (outward from glass = +y)", np.isclose(np.dot(P2, n), rho_sb))
th_air = np.degrees(np.arctan(np.tan(np.radians(45)) / 81))
print(f"   water (81) at 45 deg -> air at {th_air:.4f} deg")
check("0.71 deg", np.isclose(round(th_air, 2), 0.71))

# ---------------------------------------------------------------------------------
hdr("6.9  Two tilted charged planes (P: 3x+4z = 0, Q: 3x+4z = 10)")
n = unit([3, 0, 4])
print("   n =", n, " distance between planes =", 10 / np.linalg.norm([3, 0, 4]), "m")
rho_a = 5 * EPS0
DM = EPS0 * np.array([7.0, 2.0, 1.0])
DMn, DMt = split(DM, n)
print(f"   D_Mn = {DMn / EPS0:.6f} eps0, D_Mt = {DMt / EPS0} eps0, D_Mt.n = {np.dot(DMt, n):.1e}")
check("D_Mn = 5 eps0, D_Mt = eps0(4,2,-3)", np.isclose(DMn / EPS0, 5) and np.allclose(DMt / EPS0, [4, 2, -3]))
DLn = DMn - rho_a
DL = DMt + DLn * n
print(f"   D_Ln = {DLn / EPS0:.6f} eps0, D_L = {DL / EPS0} eps0, E_L = {DL / EPS0} V/m")
check("D_L = eps0(4,2,-3)", np.allclose(DL / EPS0, [4, 2, -3]))
# region R: D_R = D_Mt + DRn n, x-component = eps0
DRn = (EPS0 - DMt[0]) / n[0]
DR = DMt + DRn * n
rho_b = np.dot(n, DR - DM)
print(f"   D_Rn = {DRn / EPS0:.6f} eps0, D_R = {DR / EPS0} eps0, rho_sQ = {rho_b / EPS0:.6f} eps0 = {rho_b:.4e} C/m^2")
check("D_Rn = -5 eps0, D_R = eps0(1,2,-7), rho_sQ = -10 eps0", np.isclose(DRn / EPS0, -5)
      and np.allclose(DR / EPS0, [1, 2, -7]) and np.isclose(rho_b / EPS0, -10) and np.isclose(rho_b, -8.854e-11, rtol=1e-3))
# explicit BCs at both planes (vacuum: E = D/eps0)
EL, EM, ER = DL / EPS0, DM / EPS0, DR / EPS0
check("plane P: n.(D_M-D_L) = rho_sP", np.isclose(np.dot(n, DM - DL), rho_a))
check("plane P: n x (E_M-E_L) = 0", np.allclose(np.cross(n, EM - EL), 0))
check("plane Q: n.(D_R-D_M) = rho_sQ", np.isclose(np.dot(n, DR - DM), rho_b))
check("plane Q: n x (E_R-E_M) = 0", np.allclose(np.cross(n, ER - EM), 0))
print("   E_M - E_L =", EM - EL, "= 5 n ->", 5 * n)
# independent route: superposition of two sheets + one uniform background D0
D0 = DM - (rho_a - rho_b) / 2 * n
DL_sup = D0 - (rho_a + rho_b) / 2 * n
DR_sup = D0 + (rho_a + rho_b) / 2 * n
print("   superposition: background D0 =", D0 / EPS0, "eps0; D_L =", DL_sup / EPS0, "; D_R =", DR_sup / EPS0)
check("superposition reproduces D_L and D_R", np.allclose(DL_sup, DL) and np.allclose(DR_sup, DR))
print(f"   combined jump D_Rn - D_Ln = {(np.dot(DR, n) - np.dot(DL, n)) / EPS0:.6f} eps0 = rho_sP + rho_sQ = {(rho_a + rho_b) / EPS0:.6f} eps0")


def Efield9(r):
    s = 3 * r[0] + 4 * r[2]
    return EL if s < 0 else (EM if s < 10 else ER)


Ap, Bp, Cp, Bprime = np.array([0, 0, 0.]), np.array([2, 0, 1.]), np.array([2, 0, -2.]), 2 * n
print("   B on plane Q (3x+4z):", 3 * Bp[0] + 4 * Bp[2], "; B' =", Bprime, "on plane Q:", 3 * Bprime[0] + 4 * Bprime[2],
      "; C side:", 3 * Cp[0] + 4 * Cp[2])
VBA = -leg(Efield9, Ap, Bp)
VBpA = -leg(Efield9, Ap, Bprime)
print(f"   V(B)-V(A) = {VBA:.6f} V, V(B')-V(A) = {VBpA:.6f} V, V(B)-V(B') = {VBA - VBpA:.6f} V "
      f"(= -E_Mt.(B-B') = {-np.dot(DMt / EPS0, Bp - Bprime):.6f})")
check("V(B)-V(A) = -15, V(B')-V(A) = -10, V(B)-V(B') = -5", np.isclose(VBA, -15) and np.isclose(VBpA, -10)
      and np.isclose(VBA - VBpA, -5))
# circulation A -> B -> C -> A, crossing plane a at z = -1.5 on side B->C (t = 2.5/3)
tcross = 2.5 / 3
print(f"   side B->C (x=2, y=0) meets plane P where 3*2 + 4z = 0: z = {-6/4:.2f} m (t = {tcross:.6f})")
lAB = leg(Efield9, Ap, Bp)
lBC = leg(Efield9, Bp, Cp, points=[tcross])
lCA = leg(Efield9, Cp, Ap)
lBC_M = leg(Efield9, Bp, np.array([2, 0, -1.5]))
lBC_L = leg(Efield9, np.array([2, 0, -1.5]), Cp)
print(f"   A->B {lAB:.6f}, B->C {lBC:.6f} (M part {lBC_M:.6f}, L part {lBC_L:.6f}), C->A {lCA:.6f}; "
      f"circulation {lAB + lBC + lCA:.2e} V")
check("legs 15, -1 (-2.5 + 1.5), -14; circulation 0", np.isclose(lAB, 15) and np.isclose(lBC, -1)
      and np.isclose(lBC_M, -2.5) and np.isclose(lBC_L, 1.5) and np.isclose(lCA, -14) and abs(lAB + lBC + lCA) < 1e-9)
# counter-test: if E_t were NOT continuous (say E_L had +1 extra along y), circulation of a straddling loop != 0
EL_bad = EL + np.array([0, 1.0, 0])
Ebad = lambda r: EL_bad if 3 * r[0] + 4 * r[2] < 0 else EM
t_hat = unit([4, 0, -3])
h = 1e-4
cor = [-h * n, -h * n + 2 * np.array([0, 1.0, 0]), h * n + 2 * np.array([0, 1.0, 0]), h * n]
print(f"   counter-test (tangential jump of 1 V/m along y): straddling-loop circulation = "
      f"{sum(loop(Ebad, cor, [None, [0.5], None, [0.5]])):.6f} V (nonzero)")

# ---------------------------------------------------------------------------------
hdr("6.10  Plates around a charged sheet (x = 0, 2, 3 m)")
V0, V2, V3 = 0.0, -2.0, 6.0
EA = -(V2 - V0) / 2.0
EB = -(V3 - V2) / 1.0
print(f"   E_A = {EA:+.6f} V/m (x-hat), E_B = {EB:+.6f} V/m (x-hat)")
check("E_A = +1, E_B = -8", np.isclose(EA, 1) and np.isclose(EB, -8))
rs0 = np.dot([1, 0, 0], EPS0 * np.array([EA, 0, 0]) - 0)        # n out of metal at x=0: +x; D in metal = 0
rs3 = np.dot([-1, 0, 0], EPS0 * np.array([EB, 0, 0]) - 0)       # n out of metal at x=3: -x
rs2 = np.dot([1, 0, 0], EPS0 * np.array([EB, 0, 0]) - EPS0 * np.array([EA, 0, 0]))
print(f"   rho_s0 = {rs0 / EPS0:+.6f} eps0 = {rs0:.4e}; rho_s3 = {rs3 / EPS0:+.6f} eps0 = {rs3:.4e}; "
      f"rho_s2 = {rs2 / EPS0:+.6f} eps0 = {rs2:.4e} C/m^2; total = {(rs0 + rs2 + rs3) / EPS0:.2e} eps0")
check("rho_s0 = eps0 = 8.85e-12", np.isclose(rs0 / EPS0, 1) and np.isclose(rs0, 8.854e-12, rtol=1e-3))
check("rho_s3 = 8 eps0 = 7.08e-11", np.isclose(rs3 / EPS0, 8) and np.isclose(rs3, 7.083e-11, rtol=1e-3))
check("rho_s2 = -9 eps0 = -7.97e-11", np.isclose(rs2 / EPS0, -9) and np.isclose(rs2, -7.969e-11, rtol=1e-3))
check("total zero", abs(rs0 + rs2 + rs3) < 1e-25)
rs3_wrong = np.dot([1, 0, 0], EPS0 * np.array([EB, 0, 0]))     # slip: n = +x at x = 3 (into the metal)
print(f"   watch-out: wrong normal +x at x=3 gives {rs3_wrong / EPS0:+.6f} eps0; total would be "
      f"{(rs0 + rs2 + rs3_wrong) / EPS0:+.6f} eps0 (nonzero)")
check("wrong normal gives -8 eps0 and a nonzero total", np.isclose(rs3_wrong / EPS0, -8)
      and not np.isclose((rs0 + rs2 + rs3_wrong) / EPS0, 0))


def sheets_field(charges, x):
    """E_x at x from infinite sheets {position: rho_s} by superposition"""
    return sum(rho / (2 * EPS0) * np.sign(x - xi) for xi, rho in charges.items())


ch = {0.0: rs0, 2.0: rs2, 3.0: rs3}
for x in [-1.0, 1.0, 2.5, 4.0]:
    print(f"   brute force: E_x({x:+.1f}) = {sheets_field(ch, x):+.6f} V/m")
check("superposition: 0 in metal, 1 and -8 in gaps",
      np.allclose([sheets_field(ch, x) for x in [-1, 1, 2.5, 4]], [0, 1, -8, 0]))
Vnum = lambda x: -quad(lambda s: sheets_field(ch, s), 0, x, points=[2.0] if x > 2 else None)[0]
print(f"   brute force V(2) = {Vnum(2.0):+.6f} V, V(3) = {Vnum(3.0):+.6f} V")
check("V(2) = -2, V(3) = 6", np.isclose(Vnum(2.0), -2) and np.isclose(Vnum(3.0), 6))
print(f"   KVL: -(E_A*2 + E_B*1) = {-(EA * 2 + EB * 1):.6f} V = V(3)-V(0)")
# (d) plates joined: E_A' a + E_B' (d - a) = 0 ; eps0 (E_B' - E_A') = rho_s2
a_, d_ = 2.0, 3.0
M = np.array([[a_, d_ - a_], [-1.0, 1.0]])
EAp, EBp = np.linalg.solve(M, [0.0, rs2 / EPS0])
rs0p, rs3p = EPS0 * EAp, -EPS0 * EBp
V2p = -EAp * a_
print(f"   (d) E_A' = {EAp:+.6f}, E_B' = {EBp:+.6f} V/m; rho_s0' = {rs0p / EPS0:+.6f} eps0 = {rs0p:.4e}, "
      f"rho_s3' = {rs3p / EPS0:+.6f} eps0 = {rs3p:.4e} C/m^2; V(2) = {V2p:+.6f} V; plates total {(rs0p + rs3p) / EPS0:.4f} eps0")
check("(d) 3, -6 V/m; 3 eps0, 6 eps0; V(2) = -6 V", np.isclose(EAp, 3) and np.isclose(EBp, -6)
      and np.isclose(rs0p / EPS0, 3) and np.isclose(rs3p / EPS0, 6) and np.isclose(V2p, -6)
      and np.isclose(rs0p, 2.656e-11, rtol=1e-3) and np.isclose(rs3p, 5.313e-11, rtol=1e-3))
ch2 = {0.0: rs0p, 2.0: rs2, 3.0: rs3p}
check("(d) brute force: zero field in metal; V(3)=V(0)",
      np.isclose(sheets_field(ch2, -1), 0) and np.isclose(sheets_field(ch2, 4), 0)
      and np.isclose(quad(lambda s: sheets_field(ch2, s), 0, 3, points=[2.0])[0], 0, atol=1e-12))
# general formula rho0' = -rho (d-a)/d, rho_d' = -rho a/d, against brute-force solve at several parameter sets
for (aa, dd, rr) in [(2.0, 3.0, -9.0), (0.7, 2.5, 4.0), (1.3, 1.6, -2.2), (5.0, 8.0, 1.0)]:
    EAg, EBg = np.linalg.solve(np.array([[aa, dd - aa], [-1.0, 1.0]]), [0.0, rr])
    r0, rd = EAg, -EBg                      # in units of eps0
    f0, fd = -rr * (dd - aa) / dd, -rr * aa / dd
    print(f"   general: a={aa}, d={dd}, rho={rr} eps0 -> rho0'={r0:+.6f} (formula {f0:+.6f}), "
          f"rho_d'={rd:+.6f} (formula {fd:+.6f}) [eps0]")
    check("general split formula", np.isclose(r0, f0) and np.isclose(rd, fd))
print(f"   share of the induced charge on the nearer plate (x=3 m): {rs3p / (rs0p + rs3p):.6f} = 2/3")

# ---------------------------------------------------------------------------------
hdr("6.11  Charged shell in a dielectric (r = 2 m)")
a = 2.0
er1, er2 = 4.0, 1.0           # medium 1: dielectric r>2; medium 2: vacuum core r<2
# work in a local frame at phi = 0: r-hat = x, phi-hat = y, z-hat = z
nr = np.array([1.0, 0, 0])
E2 = np.array([6.0, 0, 3.0])  # core side
E2n, E2t = split(E2, nr)
E1 = E2t + 1.0 * nr           # given E_r(2+) = 1, tangential copied
D1, D2 = er1 * EPS0 * E1, er2 * EPS0 * E2
print("   E1 =", E1, "V/m (r, phi, z);  D1/eps0 =", D1 / EPS0)
check("E1 = r + 3z, D1 = eps0(4r + 12z)", np.allclose(E1, [1, 0, 3]) and np.allclose(D1 / EPS0, [4, 0, 12]))
check("n x (E1-E2) = 0", np.allclose(np.cross(nr, E1 - E2), 0))
rs = np.dot(nr, D1 - D2)
print(f"   rho_s = {rs / EPS0:+.6f} eps0 = {rs:.4e} C/m^2")
check("rho_s = -2 eps0 = -1.77e-11", np.isclose(rs / EPS0, -2) and np.isclose(rs, -1.771e-11, rtol=1e-3))
tot = np.dot(nr, EPS0 * (E1 - E2))
rsb = tot - rs
print(f"   total = {tot / EPS0:+.6f} eps0, rho_sb = {rsb / EPS0:+.6f} eps0 = {rsb:.4e} C/m^2")
check("total -5 eps0, rho_sb = -3 eps0 = -2.66e-11", np.isclose(tot / EPS0, -5) and np.isclose(rsb / EPS0, -3)
      and np.isclose(rsb, -2.656e-11, rtol=1e-3))
P1 = D1 - EPS0 * E1
print("   P1/eps0 =", P1 / EPS0, "(r, phi, z)")
check("cross-check: bound charge on dielectric inner face = P1.(-r) = -3 eps0", np.isclose(np.dot(P1, -nr) / EPS0, -3))
# (d) rho_l from Gauss in the core: numerical flux of eps0*E through a closed cylinder of radius r0 -> 2-, length 1
rho_l = 2 * np.pi * a * E2[0] * EPS0
print(f"   rho_l = 2 pi (2)(6) eps0 = {rho_l / (np.pi * EPS0):.6f} pi eps0 = {rho_l:.4e} C/m")
Ecore = lambda x, y, z: np.array([rho_l / (2 * np.pi * EPS0) * x / (x * x + y * y),
                                  rho_l / (2 * np.pi * EPS0) * y / (x * x + y * y), 3.0])
r0, Lc = 2.0 - 1e-9, 1.0
side, _ = dblquad(lambda z, ph: float(np.dot(Ecore(r0 * np.cos(ph), r0 * np.sin(ph), z),
                                             [np.cos(ph), np.sin(ph), 0])) * r0, 0, 2 * np.pi, 0, Lc)
top, _ = dblquad(lambda rr, ph: float(Ecore(rr * np.cos(ph), rr * np.sin(ph), Lc)[2]) * rr, 0, 2 * np.pi, 1e-9, r0)
bot, _ = dblquad(lambda rr, ph: -float(Ecore(rr * np.cos(ph), rr * np.sin(ph), 0)[2]) * rr, 0, 2 * np.pi, 1e-9, r0)
Qenc = EPS0 * (side + top + bot)
print(f"   numerical Gauss: side {side:.6f}, caps {top:+.6f} {bot:+.6f} -> Q_enc/L = {Qenc:.4e} C/m")
check("numerical Gauss gives rho_l = 24 pi eps0 = 6.68e-10", np.isclose(Qenc, rho_l, rtol=1e-6)
      and np.isclose(rho_l, 6.676e-10, rtol=1e-3) and np.isclose(rho_l / (np.pi * EPS0), 24))
check("field from rho_l at 2-: E_r = 6", np.isclose(Ecore(2.0, 0, 0)[0], 6))
th2 = np.degrees(np.arctan2(3, 6)); th1 = np.degrees(np.arctan2(3, 1))
print(f"   theta2 (core) = {th2:.4f} deg, theta1 (dielectric) = {th1:.4f} deg, tan ratio = {3 / (3 / 6):.4f}, "
      f"eps1/eps2 = {er1 / er2:.1f}")
check("26.6 and 71.6 deg, ratio 6", np.isclose(round(th2, 1), 26.6) and np.isclose(round(th1, 1), 71.6))
E1r_0 = er2 * E2[0] / er1
print(f"   with rho_s = 0: E1r = {E1r_0:.4f} V/m, tan theta1 = {3 / E1r_0:.4f}, ratio = {(3 / E1r_0) / 0.5:.4f}")
check("rho_s=0 -> E1r = 1.5, tan = 2, ratio 4", np.isclose(E1r_0, 1.5) and np.isclose((3 / E1r_0) / 0.5, 4))
free_in = rho_l + 2 * np.pi * a * rs
print(f"   check: free charge per m inside r=2+ = {free_in / (np.pi * EPS0):.4f} pi eps0; "
      f"D1r * 2 pi (2) = {D1[0] * 2 * np.pi * a / (np.pi * EPS0):.4f} pi eps0; shell per m = {2 * np.pi * a * rs / (np.pi * EPS0):.4f} pi eps0")
check("Gauss for D outside: 16 pi eps0", np.isclose(free_in, D1[0] * 2 * np.pi * a)
      and np.isclose(free_in / (np.pi * EPS0), 16))

# ---------------------------------------------------------------------------------
hdr("6.12  A tilted current sheet (3y + 4z = 0, Js = 5x)")
n = unit([0, 3, 4])
Js = np.array([5.0, 0, 0])
H2 = np.array([2.0, 3.0, 4.0])
print("   n =", n, " Js.n =", np.dot(Js, n))
check("Js tangential", np.dot(Js, n) == 0)
H2n, H2t = split(H2, n)
print(f"   H2n = {H2n:.6f} A/m, H2n n = {H2n * n}, H2t = {H2t} A/m")
check("H2n = 5, H2t = 2x", np.isclose(H2n, 5) and np.allclose(H2t, [2, 0, 0]))
jump = np.cross(Js, n)
print("   Js x n =", jump, "(= 3z - 4y)")
check("Js x n = -4y + 3z", np.allclose(jump, [0, -4, 3]))
H1t = H2t + jump
H1 = H1t + H2n * n
B1, B2 = MU0 * H1, MU0 * H2
print("   H1t =", H1t, " H1 =", H1, "A/m;  B1 =", B1 * 1e6, "uT")
check("H1 = 2x - y + 7z", np.allclose(H1, [2, -1, 7]))
check("B1 ~ (2.51, -1.26, 8.80) uT", np.allclose(np.round(B1 * 1e6, 2), [2.51, -1.26, 8.80]))
H1_wrong = H2t + np.cross(n, Js) + H2n * n   # slip: n x Js instead of Js x n
print("   watch-out: n x Js instead of Js x n gives H1 =", H1_wrong, "A/m; n x (H1_wrong - H2) =",
      np.cross(n, H1_wrong - H2))
check("wrong order gives 2x + 7y + z, which violates the H_t condition", np.allclose(H1_wrong, [2, 7, 1])
      and np.allclose(np.cross(n, H1_wrong - H2), -Js))
print(f"   H1-H2 = {H1 - H2};  n.(B1-B2) = {np.dot(n, B1 - B2):.2e};  n x (H1-H2) = {np.cross(n, H1 - H2)}")
check("n.(B1-B2) = 0", abs(np.dot(n, B1 - B2)) < 1e-18)
check("n x (H1-H2) = Js", np.allclose(np.cross(n, H1 - H2), Js))
# (d) current through the segment (0,0,0)->(0,4,-3): I = int Js . (t x n) dl, t = unit tangent of segment
P, Q = np.zeros(3), np.array([0, 4.0, -3.0])
t = unit(Q - P)
m = np.cross(t, n)    # in-plane normal to the segment
I_seg = quad(lambda s: float(np.dot(Js, m)), 0, np.linalg.norm(Q - P))[0]
print(f"   segment length {np.linalg.norm(Q - P):.4f} m, t = {t}, in-plane normal t x n = {m}, I = {I_seg:.6f} A")
check("3*0 + 4*... segment lies in plane", np.isclose(3 * Q[1] + 4 * Q[2], 0))
check("I = 25 A along +x", np.isclose(I_seg, 25) and np.allclose(m, [1, 0, 0]))
# (e) the bogus report
Hbad = np.array([2.0, -1.0, 9.0])
print(f"   report: n.Hbad = {np.dot(n, Hbad):.6f} A/m vs H2n = {H2n:.6f}; B_n jump = {np.dot(n, Hbad) - H2n:.4f} mu0")
check("report has H1n = 6.6 != 5", np.isclose(np.dot(n, Hbad), 6.6))
print(f"   report: (-3 + 36)/5 = {(-3 + 36) / 5:.6f}; jump in B_n would be 1.6 mu0 = {1.6 * MU0:.4e} T")
# Ampere thin loop in the plane x = 0 with dS = +x (long sides along +t on side 2, -t on side 1)
t_hat = unit([0, 4, -3])
print("   t_hat x n =", np.cross(t_hat, n), "(loop normal +x)")
print(f"   H1.t = {np.dot(H1, t_hat):.6f}, H2.t = {np.dot(H2, t_hat):.6f}, H1_x = {H1[0]}, H2_x = {H2[0]} A/m")
check("H.t jumps from 0 to -5; H_x continuous", np.isclose(np.dot(H1, t_hat), -5) and np.isclose(np.dot(H2, t_hat), 0)
      and H1[0] == H2[0] == 2)
Hfield = lambda r: H1 if np.dot(r, n) > 0 else H2
h, L = 1e-3, 3.0
cor = [-h * n, -h * n + L * t_hat, h * n + L * t_hat, h * n]
circ = sum(loop(Hfield, cor, [None, [0.5], None, [0.5]]))
print(f"   Ampere loop: circulation = {circ:.6f} A, enclosed (Js.x) L = {Js[0] * L:.6f} A")
check("Ampere thin loop", np.isclose(circ, Js[0] * L))

print("\nALL CHECKS PASSED")
