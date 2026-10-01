#!/usr/bin/env python3
"""R04.py -- independent re-solve of content-src/practice/04-divergence-and-curl.md
(ECE 329, Lecture 4: divergence and curl).  numpy/scipy only.

Every quantity is recomputed from the problem data by a brute-force route:
finite-difference div/curl on Cartesian components (curvilinear fields are built in
Cartesian form first, so no curvilinear formula is reused), numerical line / surface /
volume integrals, np.cross for every orientation, ODE tracking of ions and root finding.
Each result is compared with the value printed on the page: PASS / FAIL.
"""
import numpy as np
from scipy import integrate, optimize

EPS0 = 8.8541878128e-12
PI = np.pi
NPASS = 0
NFAIL = 0


def chk(label, c, s, rtol=1e-6, atol=0.0, sig=None):
    """PASS if |c - s| <= max(atol, rtol*|s|); with sig, if c rounded to sig figures equals s."""
    global NPASS, NFAIL
    c, s = float(c), float(s)
    if sig is not None:
        ok = float(f"{c:.{sig}g}") == float(f"{s:.{sig}g}")
    else:
        ok = abs(c - s) <= max(atol, rtol * abs(s))
    NPASS += ok
    NFAIL += not ok
    print(f"  {'PASS' if ok else 'FAIL'}  {label}: computed {c:.10g} | page {s:.10g}")


def flag(label, ok, detail=""):
    global NPASS, NFAIL
    NPASS += bool(ok)
    NFAIL += not ok
    print(f"  {'PASS' if ok else 'FAIL'}  {label} {detail}")


# ---------- finite-difference operators on Cartesian vector fields F(p) -> array(3) ----------
def jac(F, p, h):
    p = np.asarray(p, float)
    m = np.zeros((3, 3))
    for j in range(3):
        e = np.zeros(3)
        e[j] = h
        m[:, j] = (np.asarray(F(p + e), float) - np.asarray(F(p - e), float)) / (2 * h)
    return m


def div(F, p, h=1e-5):
    return np.trace(jac(F, p, h))


def curl(F, p, h=1e-5):
    m = jac(F, p, h)
    return np.array([m[2, 1] - m[1, 2], m[0, 2] - m[2, 0], m[1, 0] - m[0, 1]])


def seg(F, A, B):
    """line integral of F along the straight segment A -> B"""
    A, B = np.asarray(A, float), np.asarray(B, float)
    d = B - A
    return integrate.quad(lambda t: np.dot(F(A + t * d), d), 0, 1,
                          epsabs=1e-14, epsrel=1e-12, limit=200)[0]


def poly(F, pts):
    return sum(seg(F, pts[i], pts[i + 1]) for i in range(len(pts) - 1))


def curve(F, r, dr, t0, t1):
    return integrate.quad(lambda t: np.dot(F(r(t)), dr(t)), t0, t1,
                          epsabs=1e-14, epsrel=1e-12, limit=200)[0]


def circle(F, R, z=0.0, t0=0.0, t1=2 * PI):
    return curve(F, lambda t: np.array([R * np.cos(t), R * np.sin(t), z]),
                 lambda t: np.array([-R * np.sin(t), R * np.cos(t), 0.0]), t0, t1)


def cylv(p):
    """cylindrical r (distance from z axis), r-hat, phi-hat at Cartesian point p"""
    x, y = p[0], p[1]
    r = np.hypot(x, y)
    return r, np.array([x / r, y / r, 0.0]), np.array([-y / r, x / r, 0.0])


def sphv(p):
    """spherical r, theta, r-hat, theta-hat, phi-hat at Cartesian point p"""
    x, y, z = p
    r = np.sqrt(x * x + y * y + z * z)
    th, ph = np.arccos(z / r), np.arctan2(y, x)
    rh = np.array([np.sin(th) * np.cos(ph), np.sin(th) * np.sin(ph), np.cos(th)])
    thh = np.array([np.cos(th) * np.cos(ph), np.cos(th) * np.sin(ph), -np.sin(th)])
    phh = np.array([-np.sin(ph), np.cos(ph), 0.0])
    return r, th, rh, thh, phh


def rhat(th, ph):
    return np.array([np.sin(th) * np.cos(ph), np.sin(th) * np.sin(ph), np.cos(th)])


def sphere_flux(F, R):
    return integrate.dblquad(lambda th, ph: np.dot(F(R * rhat(th, ph)), rhat(th, ph)) * R**2 * np.sin(th),
                             0, 2 * PI, 0, PI, epsabs=1e-13, epsrel=1e-10)[0]


def spin(F, p0, s=1e-3, n=720):
    """sum over a small ring around p0 (axle along z) of (rho x v)_z, with np.cross:
    > 0 -> counter-clockwise seen from +z, < 0 -> clockwise"""
    p0 = np.asarray(p0, float)
    tot = 0.0
    for ph in np.linspace(0, 2 * PI, n, endpoint=False):
        rv = s * np.array([np.cos(ph), np.sin(ph), 0.0])
        tot += np.cross(rv, F(p0 + rv))[2]
    return tot


rng = np.random.default_rng(329)

# =====================================================================================
print("== 4.1 Faucet or whirlpool")
E1 = lambda p: np.array([3 * p[0], -p[1], 2 * p[2]])
E2 = lambda p: np.array([2 * p[1], -3 * p[0], 0.0])
P = rng.uniform(-3, 3, (6, 3))
d1 = np.array([div(E1, q) for q in P])
c1 = np.array([curl(E1, q) for q in P])
d2 = np.array([div(E2, q) for q in P])
c2 = np.array([curl(E2, q) for q in P])
chk("(a) div E1 [V/m^2] (mean of 6 random points)", d1.mean(), 4)
chk("(a) spread of div E1 over the points", np.ptp(d1), 0, atol=1e-8)
chk("(a) max |curl E1|", np.abs(c1).max(), 0, atol=1e-8)
chk("(a) max |div E2|", np.abs(d2).max(), 0, atol=1e-8)
chk("(a) curl E2 . z-hat [V/m^2]", c2[:, 2].mean(), -5)
chk("(a) max |x,y components of curl E2|", np.abs(c2[:, :2]).max(), 0, atol=1e-8)
chk("(b) rho = eps0 div E1 [C/m^3]", EPS0 * d1.mean(), 3.54e-11, sig=3)
w = spin(E2, [0, 0, 0])
flag("(c) paddlewheel in E2 turns clockwise seen from +z", w < 0, f"(ring sum {w:.3e} < 0)")
flag("(c) E2(0,1,0) = +2 x-hat, E2(1,0,0) = -3 y-hat",
     np.allclose(E2([0, 1, 0]), [2, 0, 0]) and np.allclose(E2([1, 0, 0]), [0, -3, 0]))
m = jac(E2, [0.3, -0.2, 0.1], 1e-5)
chk("watch-out: reversed order dEx/dy - dEy/dx", m[0, 1] - m[1, 0], 5)

# =====================================================================================
print("== 4.2 Curl-free but not charge-free")
E = lambda p: np.array([p[2]**2 + 2 * p[1], 2 * p[0] - 3, 2 * p[0] * p[2]])
P = rng.uniform(-3, 3, (8, 3))
mc = max(np.abs(curl(E, q)).max() for q in P)
md = max(abs(div(E, q) - 2 * q[0]) for q in P)
chk("max |curl E| over 8 random points", mc, 0, atol=1e-7)
chk("max |div E - 2x| over 8 random points", md, 0, atol=1e-7)
chk("(c) rho at x = 1 m [C/m^3]", EPS0 * div(E, [1, 0.4, -0.7]), 1.77e-11, sig=3)
loops = [poly(E, [A, B, C, A]) for A, B, C in rng.uniform(-2, 2, (6, 3, 3))]
chk("(b) max |circulation| over 6 random triangles [V]", np.abs(loops).max(), 0, atol=1e-9)
O, T = np.zeros(3), np.array([1.0, 2.0, 3.0])
routes = {
    "straight": poly(E, [O, T]),
    "staircase x,y,z": poly(E, [O, [1, 0, 0], [1, 2, 0], T]),
    "staircase z,y,x": poly(E, [O, [0, 0, 3], [0, 2, 3], T]),
    "curve (t, 2t^2, 3 sin(pi t/2))": curve(E, lambda t: np.array([t, 2 * t * t, 3 * np.sin(PI * t / 2)]),
                                             lambda t: np.array([1, 4 * t, 1.5 * PI * np.cos(PI * t / 2)]), 0, 1),
}
for k, v in routes.items():
    chk(f"(e) integral (0,0,0)->(1,2,3) along {k} [V]", v, 7)
chk("(e) staircase leg 1 [V]", seg(E, O, [1, 0, 0]), 0, atol=1e-12)
chk("(e) staircase leg 2 [V]", seg(E, [1, 0, 0], [1, 2, 0]), -2)
chk("(e) staircase leg 3 [V]", seg(E, [1, 2, 0], T), 9)
f = lambda p: -(p[0] * p[2]**2 + 2 * p[0] * p[1] - 3 * p[1])
gdev = max(np.abs(-np.array([(f(q + e) - f(q - e)) / 2e-5 for e in np.eye(3) * 1e-5]) - E(q)).max() for q in P)
chk("check: max |-grad f - E|", gdev, 0, atol=1e-5)
chk("check: f(0,0,0) - f(1,2,3) [V]", f(O) - f(T), 7)
truth = {"a": mc < 1e-6, "b": np.abs(loops).max() < 1e-8, "c": md < 1e-6 and EPS0 * 2 * 1 > 0 > EPS0 * 2 * (-1),
         "d": all(abs(div(E, q)) < 1e-6 for q in P), "e": all(abs(v - 7) < 1e-8 for v in routes.values())}
false_set = [k for k, v in truth.items() if not v]
flag("keyed answer: the only false statement is (d)", false_set == ["d"], f"(false set = {false_set})")

# =====================================================================================
print("== 4.3 Along or across the flow  (arbitrary positive E0, a, k, Q)")
E0, a, k, Kq = 1.7, 0.6, 0.9, 2.3          # Kq = Q/(4 pi eps0)
F = lambda p: np.array([E0 * np.exp(-p[1] / a), 0.0, 0.0])
P = [np.array(q) for q in ([0.3, -0.4, 0.2], [-1.1, 0.7, 0.5], [0.8, 1.3, -0.9], [-0.5, -1.2, 1.4])]
dF = max(abs(div(F, q)) for q in P)
chk("(a) max |div F|  -> (a) True", dF, 0, atol=1e-8)
cz = max(abs(curl(F, q)[2] - E0 / a * np.exp(-q[1] / a)) for q in P)
chk("(b) max |curl_z F - (E0/a) e^(-y/a)|", cz, 0, atol=1e-7)
w = spin(F, [0.2, -0.3, 0])
flag("(b) True: paddlewheel turns counter-clockwise seen from +z", w > 0, f"(ring sum {w:.3e} > 0)")
Ec = lambda p: Kq * np.asarray(p) / np.linalg.norm(p)**3
dC = max(abs(div(Ec, q, 1e-6)) for q in P)
chk("(c) max |div E_Coulomb| at r > 0  -> (c) False", dC, 0, atol=1e-6)
vv = lambda p: k * cylv(p)[2] / cylv(p)[0]
cv = max(np.abs(curl(vv, q, 1e-6)).max() for q in P)
chk("(d) max |curl (k/r) phi-hat| at r > 0  -> (d) False", cv, 0, atol=1e-6)
for R in (0.1, 1.0, 5.0):
    chk(f"(d) circulation on circle r = {R}  vs 2 pi k", circle(vv, R, 0.3), 2 * PI * k)

# =====================================================================================
print("== 4.4 The missing metric factor")
a, D0 = 0.03, 6e-6
Dv = lambda p: D0 * (cylv(p)[0] / a)**2 * cylv(p)[1]
p_half = np.array([a / 2 * np.cos(0.7), a / 2 * np.sin(0.7), 0.05])
chk("rho(a/2) = div D (Cartesian FD) [uC/m^3]", div(Dv, p_half, 1e-8) * 1e6, 300)
Dr = lambda r: D0 * (r / a)**2
chk("student's dDr/dr at a/2 [uC/m^3]", (Dr(a / 2 + 1e-8) - Dr(a / 2 - 1e-8)) / 2e-8 * 1e6, 200)
for r in (a / 3, a / 2, a):
    flux = Dr(r) * 2 * PI * r                     # per unit length
    Qt = integrate.quad(lambda s: div(Dv, np.array([s * 0.6, s * 0.8, 0.0]), 1e-9) * 2 * PI * s, 0, r)[0]
    Qs = integrate.quad(lambda s: 2 * D0 * s / a**2 * 2 * PI * s, 0, r)[0]
    chk(f"Gauss r = {r * 100:.1f} cm: charge(correct rho)/flux", Qt / flux, 1)
    chk(f"Gauss r = {r * 100:.1f} cm: charge(student rho)/flux", Qs / flux, 2 / 3)

# =====================================================================================
print("== 4.5 Draining a cube")
Jf = lambda p: np.array([4 * p[0], 2 * p[1], -p[2]])
chk("(a) d(rho)/dt = -div J [A/m^3]", -div(Jf, [0.1, 0.2, 0.3]), -5)
L = 0.5
fx = lambda X, s: integrate.dblquad(lambda z, y: s * Jf([X, y, z])[0], 0, L, 0, L)[0]
fy = lambda Y, s: integrate.dblquad(lambda z, x: s * Jf([x, Y, z])[1], 0, L, 0, L)[0]
fz = lambda Z, s: integrate.dblquad(lambda y, x: s * Jf([x, y, Z])[2], 0, L, 0, L)[0]
out = {"x=0.5": fx(L, 1), "x=0": fx(0, -1), "y=0.5": fy(L, 1), "y=0": fy(0, -1), "z=0.5": fz(L, 1), "z=0": fz(0, -1)}
chk("(b) outward current through x = 0.5 [A]", out["x=0.5"], 0.5)
chk("(b) outward current through y = 0.5 [A]", out["y=0.5"], 0.25)
chk("(b) outward current through z = 0.5 [A]", out["z=0.5"], -0.125)
chk("(b) faces x=0, y=0, z=0 together [A]", out["x=0"] + out["y=0"] + out["z=0"], 0, atol=1e-12)
net = sum(out.values())
chk("(b) net outward current [A]", net, 0.625)
vol = integrate.tplquad(lambda z, y, x: -div(Jf, [x, y, z]), 0, L, 0, L, 0, L)[0]
chk("(b) dQ/dt = integral of d(rho)/dt [A]", vol, -0.625)
chk("(b) dQ/dt = -(net outward current) [A]", -net, -0.625)

# =====================================================================================
print("== 4.6 Three fields in curved coordinates")
E0, a = 5.0, 0.1


def G1(p):
    r, _, ph = cylv(p)
    return E0 * r / a * ph


def G2(p):
    r, th, rh, _, _ = sphv(p)
    return E0 * a**2 / r**2 * np.cos(th) * rh


def G3(p):
    r, th, rh, thh, _ = sphv(p)
    return E0 * ((a / r)**3 * (2 * np.cos(th) * rh + np.sin(th) * thh) + r / a * rh)


P = [np.array(q) for q in ([0.05, 0.03, 0.02], [-0.08, 0.11, -0.04], [0.13, -0.02, 0.09], [0.02, -0.07, -0.12])]
h = 1e-6
chk("(a) max |div E1|", max(abs(div(G1, q, h)) for q in P), 0, atol=1e-6)
c = np.array([curl(G1, q, h) for q in P])
chk("(a) curl E1 . z-hat [V/m^2]", c[:, 2].mean(), 100)
chk("(a) max |x,y components of curl E1|", np.abs(c[:, :2]).max(), 0, atol=1e-6)
chk("(b) max |div E2|", max(abs(div(G2, q, h)) for q in P), 0, atol=1e-5)
dev = []
for q in P:
    r, th, _, _, phh = sphv(q)
    ref = E0 * a**2 * np.sin(th) / r**3
    dev.append(np.abs(curl(G2, q, h) - ref * phh).max() / ref)
chk("(b) curl E2 vs phi-hat E0 a^2 sin(theta)/r^3: max rel. dev (all 3 comps)", max(dev), 0, atol=1e-6)
chk("(b) numeric coefficient E0 a^2 [V m]", E0 * a**2, 0.05)
d3 = np.array([div(G3, q, h) for q in P])
chk("(c) div E3 [V/m^2]", d3.mean(), 150)
chk("(c) spread of div E3", np.ptp(d3), 0, atol=1e-5)
chk("(c) max |curl E3|", max(np.abs(curl(G3, q, h)).max() for q in P), 0, atol=1e-5)
chk("(d) rho = eps0 div E3 [C/m^3]", EPS0 * d3.mean(), 1.33e-9, sig=3)
chk("(d) rho / eps0", d3.mean(), 150)
for R in (0.05, 0.2):
    chk(f"check: flux of E3 out of r = {R} m / (3E0/a)(4/3 pi r^3)", sphere_flux(G3, R) / (3 * E0 / a * 4 / 3 * PI * R**3), 1)

# =====================================================================================
print("== 4.7 Divergence theorem on a hemisphere  (D0 in uC/m^2 -> charge/flux in uC)")
D0, a = 6.0, 0.5
Dh = lambda p: D0 * np.array([p[0] / a, 0.0, 1.0])
chk("(a) rho = div D [uC/m^3]", div(Dh, [0.1, 0.2, 0.1]), 12)
V = integrate.tplquad(lambda r, th, ph: r**2 * np.sin(th), 0, 2 * PI, 0, PI / 2, 0, a)[0]
chk("(a) hemisphere volume [m^3]", V, 0.2618, sig=4)
Q = integrate.tplquad(lambda r, th, ph: div(Dh, r * rhat(th, ph)) * r**2 * np.sin(th), 0, 2 * PI, 0, PI / 2, 0, a)[0]
chk("(a) Q = integral of rho dV [uC]  vs pi", Q, PI)
chk("(a) Q [uC]", Q, 3.1416, sig=5)
base = integrate.dblquad(lambda s, ph: np.dot(Dh([s * np.cos(ph), s * np.sin(ph), 0]), [0, 0, -1]) * s, 0, 2 * PI, 0, a)[0]
chk("(b) base flux, outward normal -z [uC]", base, -4.712, sig=4)
dome = integrate.dblquad(lambda th, ph: np.dot(Dh(a * rhat(th, ph)), rhat(th, ph)) * a**2 * np.sin(th), 0, 2 * PI, 0, PI / 2)[0]
chk("(b) dome flux [uC]", dome, 7.854, sig=4)
chk("(b) dome flux / (pi a^2 D0)", dome / (PI * a**2 * D0), 5 / 3)
chk("(c) base + dome vs Q [uC]", base + dome, Q)
Dx = lambda p: D0 * np.array([p[0] / a, 0.0, 0.0])
Dz = lambda p: D0 * np.array([0.0, 0.0, 1.0])
domex = integrate.dblquad(lambda th, ph: np.dot(Dx(a * rhat(th, ph)), rhat(th, ph)) * a**2 * np.sin(th), 0, 2 * PI, 0, PI / 2)[0]
domez = integrate.dblquad(lambda th, ph: np.dot(Dz(a * rhat(th, ph)), rhat(th, ph)) * a**2 * np.sin(th), 0, 2 * PI, 0, PI / 2)[0]
chk("check: x-part dome flux = Q [uC]", domex, PI)
chk("check: z-part dome flux = +pi a^2 D0 [uC]", domez, PI * a**2 * D0)
chk("hint: integral sin^3 over [0, pi/2]", integrate.quad(lambda t: np.sin(t)**3, 0, PI / 2)[0], 2 / 3)
chk("hint: integral cos^2 over [0, 2 pi]", integrate.quad(lambda t: np.cos(t)**2, 0, 2 * PI)[0], PI)

# =====================================================================================
print("== 4.8 Circulation from a given curl")
P1, P2, P3, P4 = (np.array(v, float) for v in ([0, 0, 0], [0, 0, 2], [0, 3, 2], [0, 3, 0]))
Ek = lambda p: np.array([3.0, 2.0, -4.0])
chk("(a) P1->P2 [V]", seg(Ek, P1, P2), -8)
chk("(a) P2->P3 [V]", seg(Ek, P2, P3), 6)
chk("(a) P1->P2->P3 [V]", poly(Ek, [P1, P2, P3]), -2)
chk("(a) P1->P4->P3 [V]", poly(Ek, [P1, P4, P3]), -2)
chk("(a) closed loop [V]", poly(Ek, [P1, P2, P3, P4, P1]), 0, atol=1e-12)
pts = [P1, P2, P3, P4]
S = 0.5 * sum(np.cross(pts[i], pts[(i + 1) % 4]) for i in range(4))     # vector area of C
flag("(b) vector area of C = -6 x-hat m^2 (n-hat = -x-hat, area 6)", np.allclose(S, [-6, 0, 0]), f"S = {S}")
nl = np.cross(P2 - P1, P3 - P2)
flag("(b) leg1 x leg2 points along -x-hat", np.allclose(nl / np.linalg.norm(nl), [-1, 0, 0]))
yz = [(p[1], p[2]) for p in pts]                 # viewer at +x: right = +y, up = +z
view_right = np.cross(np.array([-1.0, 0, 0]), np.array([0, 0, 1.0]))
area2d = 0.5 * sum(yz[i][0] * yz[(i + 1) % 4][1] - yz[(i + 1) % 4][0] * yz[i][1] for i in range(4))
flag("(b) C is clockwise seen from +x", np.allclose(view_right, [0, 1, 0]) and area2d < 0, f"(signed area {area2d})")
cE = np.array([3.0, 2.0, -4.0])
chk("(b) circulation = (curl E).S [V]", cE @ S, -18)
flag("(b) dB/dt = -curl E = (-3,-2,4) T/s", np.allclose(-cE, [-3, -2, 4]))
Ed = lambda p: np.array([2 * p[2], -4 * p[0], 3 * p[1]])
cd = curl(Ed, [0.3, -0.5, 0.8])
flag("(d) curl of 2z x - 4x y + 3y z = (3,2,-4)", np.allclose(cd, [3, 2, -4], atol=1e-8), f"{cd}")
sg = [seg(Ed, P1, P2), seg(Ed, P2, P3), seg(Ed, P3, P4), seg(Ed, P4, P1)]
for i, (v, s) in enumerate(zip(sg, [0, 0, -18, 0])):
    chk(f"(d) segment {i + 1} [V]", v, s, atol=1e-11)
chk("(d) loop [V]", sum(sg), -18)
viaP2, viaP4 = poly(Ed, [P1, P2, P3]), poly(Ed, [P1, P4, P3])
chk("(d) route via P2 [V]", viaP2, 0, atol=1e-11)
chk("(d) route via P4 [V]", viaP4, 18)
chk("(c) via P2 minus via P4 [V]", viaP2 - viaP4, -18)
st = integrate.dblquad(lambda z, y: curl(Ed, [0, y, z]) @ np.array([-1.0, 0, 0]), 0, 3, 0, 2)[0]
chk("(b) Stokes by dblquad of (curl Ed).(-x-hat) over the rectangle [V]", st, -18)

# =====================================================================================
print("== 4.9 Electrostatic or not")
F1 = lambda p: np.array([0.0, 3 * np.cos(PI * p[1] / 2), 0.0])
F2 = lambda p: np.array([0.0, 2 * np.cos(PI * p[0] / 2), 0.0])
Ft = lambda p: F1(p) + F2(p)
P = rng.uniform(-3, 3, (6, 3))
chk("(a) max |curl E1|", max(np.abs(curl(F1, q)).max() for q in P), 0, atol=1e-8)
chk("(a) max |curl E2 - (-pi sin(pi x/2)) z-hat|",
    max(np.abs(curl(F2, q) - np.array([0, 0, -PI * np.sin(PI * q[0] / 2)])).max() for q in P), 0, atol=1e-8)
chk("(b) max |div E/1 - (-(3 pi/2) sin(pi y/2))|",
    max(abs(div(Ft, q) + 1.5 * PI * np.sin(PI * q[1] / 2)) for q in P), 0, atol=1e-8)
Ey = lambda x, y: 3 * np.cos(PI * y / 2) + 2 * np.cos(PI * x / 2)
ys = np.linspace(-4, 4, 160001)
rho = EPS0 * (Ey(0.37, ys + 1e-6) - Ey(0.37, ys - 1e-6)) / 2e-6
chk("(b) max |rho| on y in [-4,4] [C/m^3]", np.abs(rho).max(), 4.17e-11, sig=3)
chk("(b) max |rho| / eps0  vs 3 pi/2", np.abs(rho).max() / EPS0, 1.5 * PI, rtol=1e-6)
rho_y = lambda y: EPS0 * (Ey(0.37, y + 1e-6) - Ey(0.37, y - 1e-6)) / 2e-6
pk = [optimize.minimize_scalar(lambda y: -abs(rho_y(y)), bounds=b, method="bounded", options={"xatol": 1e-9}).x
      for b in ((0, 2), (-2, 0), (2, 4), (-4, -2))]
flag("(b) |rho| peaks at y = 1, -1, 3, -3 m", np.allclose(pk, [1, -1, 3, -3], atol=1e-4), f"{np.round(pk, 5)}")
flag("(b) rho < 0 at y = 1, > 0 at y = -1 and y = 3", rho_y(1) < 0 < rho_y(-1) and rho_y(3) > 0)
xs = np.linspace(-4, 4, 160001)
cu = (Ey(xs + 1e-6, 0.21) - Ey(xs - 1e-6, 0.21)) / 2e-6
chk("(c) max |curl E| [V/m^2]  vs pi", np.abs(cu).max(), PI)
chk("(c) max |curl E| [V/m^2]", np.abs(cu).max(), 3.14, sig=3)
cu_x = lambda x: (Ey(x + 1e-6, 0.21) - Ey(x - 1e-6, 0.21)) / 2e-6
pk = [optimize.minimize_scalar(lambda x: -abs(cu_x(x)), bounds=b, method="bounded", options={"xatol": 1e-9}).x
      for b in ((0, 2), (-2, 0), (2, 4), (-4, -2))]
flag("(c) |curl E| peaks at x = 1, -1, 3, -3 m", np.allclose(pk, [1, -1, 3, -3], atol=1e-4), f"{np.round(pk, 5)}")
print("  -- 4.9 (d)-(e) re-parameterized (CITATIONS-WAVE1): P = (2,1,0) m, route A via (2,0,0), staircase target -1 V")
O, Pp = np.zeros(3), np.array([2.0, 1.0, 0.0])
rA = poly(F2, [O, [2, 0, 0], Pp])
rB = poly(F2, [O, [0, 1, 0], Pp])
chk("(d) route A O->(2,0,0)->P, E2 [V]", rA, -2)
chk("(d) route B O->(0,1,0)->P, E2 [V]", rB, 2)
nrm = np.cross([2.0, 0, 0], [0, 1.0, 0])      # route A's legs: loop A + reversed B has this normal
flag("(d) loop A then reversed B is counter-clockwise seen from +z (dS = z-hat)", np.allclose(nrm / np.linalg.norm(nrm), [0, 0, 1]))
stk = integrate.dblquad(lambda y, x: curl(F2, [x, y, 0])[2], 0, 2, 0, 1)[0]
chk("(d) flux of curl E2 through 0<=x<=2, 0<=y<=1 m, dS = z-hat [V]", stk, -4)
chk("(d) route A - route B vs flux of curl", rA - rB, stk)
# seg() asks quad for 1e-14 absolute accuracy, below roundoff for a zero result; 1e-12 is attainable
chk("(e) straight segment O->P [V]", integrate.quad(lambda t: np.dot(F2(O + t * (Pp - O)), Pp - O), 0, 1,
                                                   epsabs=1e-12, limit=200)[0], 0, atol=1e-12)
xg = np.linspace(0, 2, 401)
flag("(e) E2y(2 - x) = -E2y(x): odd about x = 1 m, so the straight segment cancels",
     np.allclose([F2([x, 0, 0])[1] + F2([2 - x, 0, 0])[1] for x in xg], 0, atol=1e-12))
stair = lambda x0: poly(F2, [O, [x0, 0, 0], [x0, 1, 0], Pp])
x0 = optimize.brentq(lambda x: stair(x) + 1, 0, 2, xtol=1e-14)
chk("(e) x0 in [0, 2] m giving -1 V  vs 4/3", x0, 4 / 3)
sv = np.array([stair(x) for x in xg])
flag("(e) stair(x0) = -1 V has exactly one root on [0, 2] m", np.count_nonzero(np.diff(np.sign(sv + 1))) == 1)
chk("(e) staircase range ends: x0 = 0 [V]", stair(0.0), 2)
chk("(e) staircase range ends: x0 = 2 [V]", stair(2.0), -2)
flag("(e) staircase values fill [-2, 2] V", abs(sv.min() + 2) < 1e-9 and abs(sv.max() - 2) < 1e-9,
     f"min {sv.min():.6f}, max {sv.max():.6f}")
x0n = optimize.brentq(lambda x: stair(x) + 1, -2, 0, xtol=1e-14)
print(f"  NOTE  without a range, x0 = {x0n:.10f} m (= -4/3) also gives {stair(x0n):.10f} V -> statement needs 0 <= x0 <= 2")
chk("(e) E1 route A [V]  vs 6/pi", poly(F1, [O, [2, 0, 0], Pp]), 6 / PI)
chk("(e) E1 route B [V]  vs 6/pi", poly(F1, [O, [0, 1, 0], Pp]), 6 / PI)
chk("(e) E1 routes [V]", poly(F1, [O, [0, 1, 0], Pp]), 1.91, sig=3)
Fk = lambda p: np.array([np.sin(PI * p[1] / 2), 0.0, 0.0])   # Summer 2018 HE1 #2b field, O -> (1,1,0)
k0, k1 = poly(Fk, [O, [1, 0, 0], [1, 1, 0]]), poly(Fk, [O, [0, 1, 0], [1, 1, 0]])
flag("(d)-(e) no carry-over from the S18 HE1 #2b key (x-first path 0 V, y-first path 1 V, target 1 V)",
     abs(k0) < 1e-12 and abs(k1 - 1) < 1e-12 and abs(rA - k0) > 0.5 and abs(rB - k1) > 0.5 and abs(-1 - k1) > 0.5,
     f"key {k0:.3g} / {k1:.3g} V; page route A {rA:.6g}, route B {rB:.6g}, target -1 V")

# =====================================================================================
print("== 4.10 Charge layers from a piecewise D  (D0 in uC/m^2 -> charge in uC)")
D0, a = 2.0, 0.1


def Drad(r):
    if r < a:
        return D0 * (r / a)**2
    if r < 2 * a:
        return -2 * D0 * (a / r)**2
    return 0.0


Dsp = lambda p: Drad(np.linalg.norm(p)) * np.asarray(p) / np.linalg.norm(p)
u = np.array([0.48, -0.36, 0.8])
u /= np.linalg.norm(u)


def rho10(r):          # Cartesian FD divergence, step kept inside the smooth piece
    hh = min(1e-9, abs(r - a) / 10, abs(r - 2 * a) / 10)
    return div(Dsp, r * u, hh)


chk("(a) rho(a/2) [uC/m^3]", rho10(a / 2), 40)
chk("(a) rho just inside r = a (r = a(1-1e-7)) [uC/m^3]", rho10(a * (1 - 1e-7)), 80, sig=5)
chk("(a) rho in a<r<2a (r = 1.5a)", rho10(1.5 * a), 0, atol=1e-5)
chk("(a) rho for r > 2a (r = 2.5a)", rho10(2.5 * a), 0, atol=1e-12)


def shell(rc, d):      # Gauss on a thin shell straddling rc: (flux out - volume charge)/area
    flux = 4 * PI * ((rc + d)**2 * Drad(rc + d) - (rc - d)**2 * Drad(rc - d))
    vol = (integrate.quad(lambda r: rho10(r) * 4 * PI * r**2, rc - d, rc)[0]
           + integrate.quad(lambda r: rho10(r) * 4 * PI * r**2, rc, rc + d)[0])
    return (flux - vol) / (4 * PI * rc**2)


for d in (1e-3, 1e-5):
    chk(f"(b) rho_s(a) from Gauss shell, delta = {d} m [uC/m^2]", shell(a, d), -6)
    chk(f"(b) rho_s(2a) from Gauss shell, delta = {d} m [uC/m^2]", shell(2 * a, d), 1)
Qc = integrate.quad(lambda r: rho10(r) * 4 * PI * r**2, 0, a)[0]
Qa = 4 * PI * a**2 * shell(a, 1e-4)
Q2a = 4 * PI * (2 * a)**2 * shell(2 * a, 1e-4)
chk("(c) Q_core [uC]", Qc, 0.2513, sig=4)
chk("(c) Q on r = a [uC]", Qa, -0.7540, sig=4)
chk("(c) Q on r = 2a [uC]", Q2a, 0.5027, sig=4)
chk("(c) total [uC]", Qc + Qa + Q2a, 0, atol=1e-9)
f15 = sphere_flux(Dsp, 1.5 * a)
chk("(d) flux of D through r = 1.5a [uC]", f15, -0.5027, sig=4)
chk("(d) flux through r = 1.5a vs Q_core + Q_a", f15, Qc + Qa)
chk("(d) flux through r = 2.5a [uC]", sphere_flux(Dsp, 2.5 * a), 0, atol=1e-12)
chk("check: flux just inside r = a / (4 pi a^2 D0)", sphere_flux(Dsp, a * (1 - 1e-9)) / (4 * PI * a**2 * D0), 1, rtol=1e-6)

# =====================================================================================
print("== 4.11 An expanding ion cloud")
a, rho0, tau = 0.01, 3e-6, 2e-3
Rt = lambda t: a * np.exp(t / tau)
rt = lambda t: rho0 * np.exp(-3 * t / tau)


def Jc(p, t):
    p = np.asarray(p, float)
    return rt(t) * p / tau if np.linalg.norm(p) < Rt(t) else np.zeros(3)   # J = rho v, v = r/tau r-hat


for t in (0.3e-3, 1.7e-3):
    q = 0.6 * a * np.array([0.6, 0.0, 0.8])
    dJ = div(lambda p: Jc(p, t), q, 1e-8)
    drdt = (rt(t + 1e-8) - rt(t - 1e-8)) / 2e-8
    chk(f"(a) (div J + d rho/dt)/(d rho/dt) at t = {t * 1e3} ms", (dJ + drdt) / drdt, 0, atol=1e-6)
    chk(f"(a) div J / (3 rho/tau) at t = {t * 1e3} ms", dJ / (3 * rt(t) / tau), 1)
Qs = [integrate.quad(lambda r: rt(t) * 4 * PI * r**2, 0, Rt(t))[0] for t in (0.0, 1e-3, 4e-3)]
for t, Qv in zip((0, 1, 4), Qs):
    chk(f"(a) Q(t = {t} ms) [pC]", Qv * 1e12, 12.566, sig=5)
Q = Qs[0]
chk("(a) Q / (4 pi pC)", Q / (4 * PI * 1e-12), 1)
sol = integrate.solve_ivp(lambda t, r: r / tau, (0, 5e-3), [a], rtol=1e-12, atol=1e-18, dense_output=True)
chk("(a) edge ion (ODE dr/dt = r/tau) at 3 ms vs R(t) = a e^(t/tau)", sol.sol(3e-3)[0], Rt(3e-3))


def Iflux(t):
    return integrate.dblquad(lambda th, ph: np.dot(Jc(a * rhat(th, ph), t), rhat(th, ph)) * a**2 * np.sin(th),
                             0, 2 * PI, 0, PI, epsabs=1e-22, epsrel=1e-11)[0]


t0 = 1e-12
chk("(b) J_r(a) at t = 0+ [uA/m^2]", Jc(a * np.array([0, 0, 1.0]), t0)[2] * 1e6, 15, sig=6)
I0 = Iflux(t0)
chk("(b) I(0+) [nA]", I0 * 1e9, 18.85, sig=4)
chk("(b) I(0+) / (6 pi nA)", I0 * 1e9 / (6 * PI), 1)
Qin = lambda t: integrate.quad(lambda r: rt(t) * 4 * PI * r**2, 0, min(a, Rt(t)))[0]
for t in (0.5e-3, 2e-3):
    It = Iflux(t)
    dQa = (Qin(t + 1e-8) - Qin(t - 1e-8)) / 2e-8
    chk(f"(b) (dQa/dt + I)/I at t = {t * 1e3} ms", (dQa + It) / It, 0, atol=1e-6)
    chk(f"(b) I(t) vs (3Q/tau) e^(-3t/tau) at t = {t * 1e3} ms", It, 3 * Q / tau * np.exp(-3 * t / tau))


def r_at(r0, t):
    return integrate.solve_ivp(lambda s, r: r / tau, (0, t), [r0], rtol=1e-12, atol=1e-18).y[0, -1]


def frac_inside(t):    # ions inside r = a at time t started inside r0*, uniform density -> (r0*/a)^3
    r0s = optimize.brentq(lambda r0: r_at(r0, t) - a, 1e-3 * a, a, xtol=1e-16)
    return (r0s / a)**3


th_ = optimize.brentq(lambda t: frac_inside(t) - 0.5, 1e-5, 5e-3, xtol=1e-13)
chk("(c) t_1/2 by ion tracking [ms]", th_ * 1e3, 0.4621, sig=4)
chk("(c) cloud radius at t_1/2 (edge ion ODE) [cm]", r_at(a, th_) * 100, 1.2599, sig=5)


def Dr11(r, t):        # Gauss: D_r = Q_enc / (4 pi r^2), Q_enc by quadrature
    return integrate.quad(lambda s: rt(t) * 4 * PI * s**2, 0, min(r, Rt(t)), epsabs=0, epsrel=1e-13)[0] / (4 * PI * r**2)


for r, t in ((0.7 * a, 0.4e-3), (1.5 * a, 1.5e-3)):
    chk(f"(d) D_r / (rho r/3) at r = {r / a}a, t = {t * 1e3} ms", Dr11(r, t) / (rt(t) * r / 3), 1)
    dDdt = (Dr11(r, t + 1e-8) - Dr11(r, t - 1e-8)) / 2e-8
    Jr = Jc(r * np.array([0, 0, 1.0]), t)[2]
    chk(f"(d) (dD_r/dt + J_r)/J_r at r = {r / a}a", (dDdt + Jr) / Jr, 0, atol=1e-5)
dDo = (Dr11(3 * a, 0.5e-3 + 1e-8) - Dr11(3 * a, 0.5e-3 - 1e-8)) / 2e-8
chk("(d) outside the cloud (r = 3a, t = 0.5 ms): dD_r/dt / (rho0 a/tau)", dDo / (rho0 * a / tau), 0, atol=1e-5)

# =====================================================================================
print("== 4.12 Inside a current-carrying rod")
a, H0 = 0.02, 400.0


def Hf(p):
    r, _, ph = cylv(p)
    return (H0 * (r / a)**3 if r < a else H0 * a / r) * ph


for t, z in ((0.3, 0.0), (2.0, 0.5)):
    q = np.array([0.012 * np.cos(t), 0.012 * np.sin(t), z])
    cc = curl(Hf, q, 1e-8)
    r = np.hypot(q[0], q[1])
    chk("(a) J_z inside / (4 H0 r^2/a^3)", cc[2] / (4 * H0 * r**2 / a**3), 1)
    chk("(a) |J_x|,|J_y| inside / J_z", np.abs(cc[:2]).max() / cc[2], 0, atol=1e-6)
cc = curl(Hf, np.array([0.03, 0.02, 0.1]), 1e-8)
chk("(a) |J| outside / (4 H0/a)", np.abs(cc).max() / (4 * H0 / a), 0, atol=1e-6)
uu = np.array([np.cos(1.1), np.sin(1.1), 0.0])
chk("(a) J just inside r = a [A/m^2]", curl(Hf, a * (1 - 1e-6) * uu, 1e-10)[2], 8e4, sig=4)
dJ = div(lambda p: curl(Hf, p, 1e-7), np.array([0.008, 0.005, 0.2]), 1e-5)
chk("(a) div J / (J(a)/a)", dJ / (4 * H0 / a / a), 0, atol=1e-4)
I = integrate.dblquad(lambda r, ph: curl(Hf, [r * np.cos(ph), r * np.sin(ph), 0], 1e-9)[2] * r, 0, 2 * PI, 0, a)[0]
chk("(b) I = flux of J through the cross-section [A]", I, 50.27, sig=4)
chk("(b) I / (16 pi)", I / (16 * PI), 1)
flag("(b) J_z > 0 (along +z) and H at (r,0,0) along +y (counter-clockwise seen from +z)",
     curl(Hf, [0.01, 0.001, 0], 1e-8)[2] > 0 and Hf(np.array([0.01, 0, 0]))[1] > 0)
b = a / 2
s1 = seg(Hf, [0, 0, 0], [b, 0, 0])
arc = circle(Hf, b, 0.0, 0, PI / 2)
s3 = seg(Hf, [0, b, 0], [0, 0, 0])
chk("(c) radial legs contribute", abs(s1) + abs(s3), 0, atol=1e-12)
chk("(c) MMF around quarter-disk [A]", s1 + arc + s3, 0.7854, sig=4)
chk("(c) MMF / (pi/4)", (s1 + arc + s3) / (PI / 4), 1)
Iq = integrate.dblquad(lambda r, ph: curl(Hf, [r * np.cos(ph), r * np.sin(ph), 0], 1e-9)[2] * r, 0, PI / 2, 0, b)[0]
chk("(c) current through quarter-disk vs MMF", Iq, s1 + arc + s3)
Iqa = integrate.dblquad(lambda r, ph: curl(Hf, [r * np.cos(ph), r * np.sin(ph), 0], 1e-9)[2] * r, 0, PI / 2, 0, a)[0]
chk("(c) quarter-disk of radius a [A]", Iqa, 12.57, sig=4)
chk("(c) quarter-disk of radius a / (I/4)", Iqa / (I / 4), 1)
m2 = circle(Hf, 2 * a, 0.0)
chk("(d) MMF on r = 2a [A]", m2, 50.27, sig=4)
chk("(d) MMF on r = 2a vs I", m2, I)
for r in (0.005, 0.015):
    Ir = integrate.dblquad(lambda s, ph: curl(Hf, [s * np.cos(ph), s * np.sin(ph), 0], 1e-9)[2] * s, 0, 2 * PI, 0, r)[0]
    chk(f"check: Ampere on r = {r * 100} cm: MMF vs enclosed current", circle(Hf, r), Ir)
chk("check: |H| just inside r = a [A/m]", np.linalg.norm(Hf(a * (1 - 1e-12) * uu)), H0)
chk("check: |H| just outside r = a [A/m]", np.linalg.norm(Hf(a * (1 + 1e-12) * uu)), H0)
Bc = lambda p: 1.0 * cylv(p)[1] / cylv(p)[0]                                   # B_r = C/r, C = 1
Bg = lambda p: np.cos(np.arctan2(p[1], p[0])) * cylv(p)[1] / cylv(p)[0]         # B_r = cos(phi)/r
chk("(e) div of (C/r) r-hat", div(Bc, [0.01, 0.007, 0.0], 1e-8), 0, atol=1e-5)
chk("(e) div of (cos(phi)/r) r-hat", div(Bg, [0.01, 0.007, 0.0], 1e-8), 0, atol=1e-5)
Lc, r0 = 0.3, 0.013
side = integrate.dblquad(lambda z, ph: Bc([r0 * np.cos(ph), r0 * np.sin(ph), z]) @ np.array([np.cos(ph), np.sin(ph), 0]) * r0,
                         0, 2 * PI, 0, Lc)[0]
chk("(e) flux of (C/r) r-hat out of a coaxial cylinder / (2 pi C L)", side / (2 * PI * Lc), 1)
print(f"  NOTE  |cos(phi)/r| at r = 1e-6 a along phi = 0: {np.linalg.norm(Bg([a * 1e-6, 0, 0])):.3e} (diverges on the axis)")

print(f"\nTOTAL: {NPASS} PASS, {NFAIL} FAIL")
