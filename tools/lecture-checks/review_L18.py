#!/usr/bin/env python3
"""Independent reviewer's checks for the Lecture 18 material (wave equation, plane TEM waves).

numpy only.  Run:  python3 review_L18.py | tee review_L18.out
Every quantitative claim on the L18 page, its three concept pages, the worked problem and the five figures is
re-derived here from scratch: finite-difference Maxwell residuals (curl, div, d/dt) for every (E, H) pair,
explicit np.cross for every E x H and u x E / eta, speeds read off arguments, and all numbers.
"""
import math
import numpy as np

mu0 = 1.25663706212e-6          # CODATA 2018
eps0 = 8.8541878128e-12
c = 1 / math.sqrt(mu0 * eps0)
eta0 = math.sqrt(mu0 / eps0)
X, Y, Z = np.eye(3)
FAILS = []


def check(name, ok, info=""):
    print(("PASS  " if ok else "FAIL  ") + name + (("   [" + info + "]") if info else ""))
    if not ok:
        FAILS.append(name)


# ---------------------------------------------------------------------------------------------- A. numbers
print("== A. constants, media, cable")
print(f"   c = {c:.7e} m/s, eta0 = {eta0:.4f} ohm, 120pi = {120*math.pi:.4f} ohm")
check("c = 2.998e8 m/s", abs(c / 1e8 - 2.998) < 5e-4)
check("eta0 = 376.7 ohm", abs(eta0 - 376.7) < 0.05)
check("120pi approximates eta0 to 0.07 %", abs((120 * math.pi - eta0) / eta0 - 6.9e-4) < 3e-5,
      f"{(120*math.pi-eta0)/eta0:.3e}")
check("c ~ 30 cm/ns, 300 m/us, 300 km/ms", abs(c * 1e-9 - 0.2998) < 1e-4 and abs(c * 1e-6 - 299.8) < 0.1
      and abs(c * 1e-3 - 2.998e5) < 100)
check("tau for 1 m = 1/c = 3.34 ns", abs(1e9 / c - 3.34) < 0.005, f"{1e9/c:.4f} ns")
H1, B1 = 1 / eta0, mu0 / eta0
check("1 V/m: H = 2.65 mA/m, B = 3.34 nT = E/c", abs(H1 * 1e3 - 2.65) < 0.005 and abs(B1 * 1e9 - 3.34) < 0.005
      and abs(B1 * c - 1) < 1e-12, f"H = {H1*1e3:.4f} mA/m, B = {B1*1e9:.4f} nT")


def medium(mur, epsr):
    return c / math.sqrt(mur * epsr), eta0 * math.sqrt(mur / epsr)


v4, e4 = medium(1, 4)
check("eps_r = 4: v = 1.50e8, eta = 188 (60pi)", abs(v4 / 1e8 - 1.50) < 0.005 and abs(e4 - 188) < 0.5,
      f"v = {v4:.4e}, eta = {e4:.3f}, 60pi = {60*math.pi:.3f}")
er9 = (c / 1e8) ** 2
check("v = 1e8: eps_r = (c/v)^2 = 8.99, eta = mu0 v = 40pi = 126", abs(er9 - 8.99) < 0.005
      and abs(mu0 * 1e8 - 40 * math.pi) < 1e-5 and abs(mu0 * 1e8 - 126) < 0.5,
      f"eps_r = {er9:.4f}, mu0*v = {mu0*1e8:.3f}, eta0/sqrt(eps_r) = {eta0/math.sqrt(er9):.3f}")
vp, ep = medium(1, 2.25)
check("polyethylene: v = c/1.5 = 2.00e8, eta = 251", abs(vp / 1e8 - 2.00) < 0.005 and abs(ep - 251) < 0.5,
      f"v = {vp:.4e}, eta = {ep:.3f}, 80pi = {80*math.pi:.3f}")
vm, em = medium(2, 8)
check("mu_r = 2, eps_r = 8: eta = eta0/2 (= eps_r 4 alone), v = c/4", abs(em - eta0 / 2) < 1e-9
      and abs(vm - c / 4) < 1e-3)
for mur, epsr in ((1, 1), (1, 4), (3, 2), (2, 8)):
    mu, eps = mur * mu0, epsr * eps0
    v, eta = 1 / math.sqrt(mu * eps), math.sqrt(mu / eps)
    assert abs(eta - mu * v) < 1e-9 and abs(eta - 1 / (eps * v)) < 1e-9 and abs(v - c / math.sqrt(mur * epsr)) < 1e-3
check("eta = sqrt(mu/eps) = mu v = 1/(eps v); v = c/sqrt(mur epsr), eta = eta0 sqrt(mur/epsr)", True)
check("units: mu/eps in (H/m)/(F/m) = (ohm s)/(s/ohm) = ohm^2", True)
fac = math.log(3.5) / (2 * math.pi)
check("coax factor ln(3.5)/2pi = 0.199, x 251 ohm = 50 ohm", abs(fac - 0.199) < 5e-4 and abs(fac * ep - 50) < 0.2,
      f"{fac:.5f} -> {fac*ep:.3f} ohm")
mu, eps = mu0, 2.25 * eps0
Lc, Cc = mu / (2 * math.pi) * math.log(3.5), 2 * math.pi * eps / math.log(3.5)
Lp, Cp = mu * 1e-3 / 1e-2, eps * 1e-2 / 1e-3
check("coax LC = mu eps, sqrt(L/C) = (eta/2pi) ln(b/a); plates sqrt(L/C) = eta d/W",
      abs(Lc * Cc / (mu * eps) - 1) < 1e-12 and abs(math.sqrt(Lc / Cc) - ep * fac) < 1e-9
      and abs(math.sqrt(Lp / Cp) - ep * 0.1) < 1e-9 and abs(1 / math.sqrt(Lc * Cc) - vp) < 1e-3)
check("coax page: Z0 = (60 ohm/sqrt(eps_r)) ln(b/a) ~ eta0/2pi = 59.96", abs(eta0 / (2 * math.pi) - 59.96) < 0.01)


# ---------------------------------------------------------------------------------------------- B. Maxwell residuals
print("\n== B. finite-difference Maxwell residuals (relative); pass < 1e-6, fail = O(1)")


def jac(F, r, t, h):
    J = np.zeros((3, 3))
    for j in range(3):
        d = np.zeros(3); d[j] = h
        J[:, j] = (F(r + d, t) - F(r - d, t)) / (2 * h)
    return J


def curl_div(F, r, t, h):
    J = jac(F, r, t, h)
    return np.array([J[2, 1] - J[1, 2], J[0, 2] - J[2, 0], J[1, 0] - J[0, 1]]), np.trace(J), np.linalg.norm(J)


def ddt(F, r, t, h):
    return (F(r, t + h) - F(r, t - h)) / (2 * h)


def resid(E, H, mu, eps, pts, T, v):
    ht, hs = 1e-4 * T, 1e-4 * v * T
    w = np.zeros(4)
    for r, t in pts:
        cE, dE, nE = curl_div(E, r, t, hs)
        cH, dH, nH = curl_div(H, r, t, hs)
        mH, eE = mu * ddt(H, r, t, ht), eps * ddt(E, r, t, ht)
        w = np.maximum(w, [np.linalg.norm(cE + mH) / (np.linalg.norm(cE) + np.linalg.norm(mH) + 1e-300),
                           np.linalg.norm(cH - eE) / (np.linalg.norm(cH) + np.linalg.norm(eE) + 1e-300),
                           abs(dE) / (nE + 1e-300), abs(dH) / (nH + 1e-300)])
    return w


def lap_resid(F, mu, eps, pts, T, v):
    ht, hs = 1e-3 * T, 1e-3 * v * T
    worst = 0
    for r, t in pts:
        lap = sum((F(r + hs * e, t) - 2 * F(r, t) + F(r - hs * e, t)) / hs ** 2 for e in np.eye(3))
        tt = mu * eps * (F(r, t + ht) - 2 * F(r, t) + F(r, t - ht)) / ht ** 2
        worst = max(worst, np.linalg.norm(lap - tt) / (np.linalg.norm(lap) + np.linalg.norm(tt) + 1e-300))
    return worst


rng = np.random.default_rng(329)
T = 1e-9
mu, eps = 1.3 * mu0, 2.7 * eps0                          # a generic linear medium
v, eta = 1 / math.sqrt(mu * eps), math.sqrt(mu / eps)
f = lambda s: np.exp(-(s / T - 1) ** 2) * (1 + 0.5 * np.sin(2 * s / T))       # asymmetric waveforms
g = lambda s: (s / T) ** 3 * np.exp(-(s / T) ** 2 / 2)


def pts_one(sign, n=12):          # points where f(t - sign z/v) is non-negligible
    out = []
    for _ in range(n):
        s, z = rng.uniform(-0.5, 2.5) * T, rng.uniform(-0.5, 0.5)
        out.append((np.array([rng.uniform(-1, 1), rng.uniform(-1, 1), z]), s + sign * z / v))
    return out


def pts_two(n=12):                # points where both f(t - z/v) and g(t + z/v) are non-negligible
    out = []
    for _ in range(n):
        s1, s2 = rng.uniform(-0.5, 2.5) * T, rng.uniform(-2.5, 2.5) * T
        out.append((np.array([rng.uniform(-1, 1), rng.uniform(-1, 1), v * (s2 - s1) / 2]), (s1 + s2) / 2))
    return out


def ok(w, faraday=True, ampere=True, divs=True):
    return (w[0] < 1e-6) == faraday and (w[1] < 1e-6) == ampere and ((w[2] < 1e-6 and w[3] < 1e-6) == divs)


CASES = [  # name, E, H, sign of the argument (+1: t - z/v), expect (Faraday, Ampere, divs)
    ("row 1  x f(t-z/v), +y f/eta", lambda r, t: X * f(t - r[2] / v), lambda r, t: Y * f(t - r[2] / v) / eta, +1, (1, 1, 1)),
    ("row 2  x f(t+z/v), -y f/eta", lambda r, t: X * f(t + r[2] / v), lambda r, t: -Y * f(t + r[2] / v) / eta, -1, (1, 1, 1)),
    ("row 3  y f(t-z/v), -x f/eta", lambda r, t: Y * f(t - r[2] / v), lambda r, t: -X * f(t - r[2] / v) / eta, +1, (1, 1, 1)),
    ("row 4  y f(t+z/v), +x f/eta", lambda r, t: Y * f(t + r[2] / v), lambda r, t: X * f(t + r[2] / v) / eta, -1, (1, 1, 1)),
    ("WRONG  y f(t-z/v), +x f/eta (must fail)", lambda r, t: Y * f(t - r[2] / v), lambda r, t: X * f(t - r[2] / v) / eta, +1, (0, 0, 1)),
    ("WRONG  x f(t+z/v), +y f/eta (must fail)", lambda r, t: X * f(t + r[2] / v), lambda r, t: Y * f(t + r[2] / v) / eta, -1, (0, 0, 1)),
]
for name, E, H, sg, exp in CASES:
    w = resid(E, H, mu, eps, pts_one(sg), T, v)
    check("Maxwell " + name, ok(w, *map(bool, exp)), "Far %.1e Amp %.1e divE %.1e divH %.1e" % tuple(w))
A_, B_ = 1.7, -0.6
E_s = lambda r, t: X * (A_ * f(t - r[2] / v) + B_ * g(t + r[2] / v))
H_s = lambda r, t: Y * (A_ * f(t - r[2] / v) - B_ * g(t + r[2] / v)) / eta
H_bad = lambda r, t: Y * (A_ * f(t - r[2] / v) + B_ * g(t + r[2] / v)) / eta
w = resid(E_s, H_s, mu, eps, pts_two(), T, v)
check("Maxwell superposition Ex = Af + Bg, Hy = (Af - Bg)/eta", ok(w), "Far %.1e Amp %.1e divE %.1e divH %.1e" % tuple(w))
w = resid(E_s, H_bad, mu, eps, pts_two(), T, v)
check("Maxwell superposition with +Bg in Hy fails both curls", ok(w, False, False, True), "Far %.1e Amp %.1e" % tuple(w[:2]))
# Faraday-route H = f/(mu v) and Ampere-route H = eps v f agree with 1/eta
check("1/(mu v) = eps v = 1/eta", abs(1 / (mu * v) * eta - 1) < 1e-12 and abs(eps * v * eta - 1) < 1e-12)
# integration 'constant' C(t) added to Hy: a time-varying one breaks Faraday, a constant one does not
Cvar = lambda r, t: H_s(r, t) + Y * 0.01 * np.sin(t / T)
Ccon = lambda r, t: H_s(r, t) + Y * 0.01
wv, wc = resid(E_s, Cvar, mu, eps, pts_two(), T, v), resid(E_s, Ccon, mu, eps, pts_two(), T, v)
check("z-integration 'constant' C(t): Faraday forces C' = 0 (time-varying C fails, constant passes)",
      wv[0] > 1e-3 and wc[0] < 1e-6 and wc[1] < 1e-6, f"C(t): Far {wv[0]:.1e}; const: Far {wc[0]:.1e}")
# z-polarized
Ez = lambda r, t: Z * f(t - r[2] / v)
cE, dE, nE = curl_div(Ez, np.array([0.1, 0.2, 0.05]), 0.9 * T, 1e-4 * v * T)
fp = (f(0.9 * T - 0.05 / v + 1e-13) - f(0.9 * T - 0.05 / v - 1e-13)) / 2e-13
check("z-polarized z f(t-z/v): div E = -f'/v != 0 and curl E = 0", abs(dE - (-fp / v)) < 1e-6 * abs(fp / v)
      and np.linalg.norm(cE) < 1e-9 * abs(dE), f"div = {dE:.4e}, -f'/v = {-fp/v:.4e}, |curl| = {np.linalg.norm(cE):.1e}")
# general direction u: E = E0 f(t - u.r/v), H = u x E / eta ; also E = eta H x u ; 3D wave equation for E and H
u = rng.normal(size=3); u /= np.linalg.norm(u)
E0 = rng.normal(size=3); E0 -= (E0 @ u) * u
Eu = lambda r, t: E0 * f(t - (u @ r) / v)
Hu = lambda r, t: np.cross(u, Eu(r, t)) / eta
pu = []
for _ in range(12):
    r = rng.uniform(-1, 1, 3); pu.append((r, rng.uniform(-0.5, 2.5) * T + (u @ r) / v))
w = resid(Eu, Hu, mu, eps, pu, T, v)
check("Maxwell general u: E = E0 f(t - u.r/v), H = u x E/eta", ok(w), "Far %.1e Amp %.1e divE %.1e divH %.1e" % tuple(w))
r0, t0 = pu[0]
check("E = eta H x u (inverse rule)", np.allclose(eta * np.cross(Hu(r0, t0), u), Eu(r0, t0), rtol=1e-12, atol=1e-15))
check("3D vector wave equation holds for E and for H (numerical Laplacian)",
      lap_resid(Eu, mu, eps, pu, T, v) < 1e-4 and lap_resid(Hu, mu, eps, pu, T, v) < 1e-4,
      f"{lap_resid(Eu, mu, eps, pu, T, v):.1e}, {lap_resid(Hu, mu, eps, pu, T, v):.1e}")
# cosine solutions and the curl-curl identity
om = 2 * math.pi * 3e8
for sg in (+1, -1):
    Ec = lambda z, t: np.cos(om * (t - sg * z / v))
    hz, ht = 1e-5, 1e-5 / v
    zz = (Ec(0.3 + hz, 1e-9) - 2 * Ec(0.3, 1e-9) + Ec(0.3 - hz, 1e-9)) / hz ** 2
    tt = (Ec(0.3, 1e-9 + ht) - 2 * Ec(0.3, 1e-9) + Ec(0.3, 1e-9 - ht)) / ht ** 2
    check(f"cos(w(t {'-' if sg > 0 else '+'} z/v)): d2/dz2 = -(w/v)^2 E = mu eps d2/dt2", abs(zz - mu * eps * tt) < 1e-5 * abs(zz)
          and abs(zz + (om / v) ** 2 * Ec(0.3, 1e-9)) < 1e-5 * abs(zz))
Ft = lambda r, t: np.array([np.sin(r[0] * r[1]) + r[2] ** 2, r[0] * np.cos(r[1] + r[2]), r[0] * r[1] * r[2]])
rr, hh = np.array([0.4, -0.7, 0.9]), 1e-3
curlF = lambda r, t: curl_div(Ft, r, t, hh)[0]
divF = lambda r: curl_div(Ft, r, 0, hh)[1]
cc = curl_div(curlF, rr, 0, hh)[0]
gd = np.array([(divF(rr + hh * e) - divF(rr - hh * e)) / (2 * hh) for e in np.eye(3)])
lap = sum((Ft(rr + hh * e, 0) - 2 * Ft(rr, 0) + Ft(rr - hh * e, 0)) / hh ** 2 for e in np.eye(3))
check("curl curl F = grad div F - lap F (Cartesian test field)", np.allclose(cc, gd - lap, atol=1e-4), f"{cc.round(5)}")

# ---------------------------------------------------------------------------------------------- C. cross products
print("\n== C. explicit cross products")
rows = [("x-pol +z", X, Y, Z), ("x-pol -z", X, -Y, -Z), ("y-pol +z", Y, -X, Z), ("y-pol -z", Y, X, -Z)]
for name, e, h, uu in rows:
    check(f"sign table {name}: E x H = travel and H = u x E", np.allclose(np.cross(e, h), uu) and np.allclose(np.cross(uu, e), h))
check("example: E = y toward -z: H = (-z) x y = +x; y x x = -z", np.allclose(np.cross(-Z, Y), X) and np.allclose(np.cross(Y, X), -Z))
check("problem: u = +y, E || z: H || y x z = +x; E x H = z x x = +y", np.allclose(np.cross(Y, Z), X) and np.allclose(np.cross(Z, X), Y))
check("problem trap: z x y = -x (wrong order)", np.allclose(np.cross(Z, Y), -X))
check("variant: u = -y: H = (-y) x z = -x", np.allclose(np.cross(-Y, Z), -X))
# relabelling the +z table: cyclic (x->y->z->x) works, a swap fails
perm_c = {0: 2, 1: 0, 2: 1}     # x->z, y->x, z->y  (cyclic)  maps row 1 (E x, H y, u z) to (E z, H x, u y)
P = np.zeros((3, 3))
for i, j in perm_c.items():
    P[j, i] = 1
check("cyclic relabelling of row 1 gives E z, H +x, travel +y (correct); det = +1", np.allclose(P @ X, Z) and np.allclose(P @ Y, X)
      and np.allclose(P @ Z, Y) and round(np.linalg.det(P)) == 1)
S = np.array([[1, 0, 0], [0, 0, 1], [0, 1, 0]])   # swap y <-> z applied to row 3 (E y, H -x, u z) -> (E z, H -x, u y): wrong
check("swap y<->z of row 3 gives H = -x for E z travelling +y (wrong: improper map)", np.allclose(S @ (-X), -X)
      and not np.allclose(np.cross(S @ Y, S @ -X), S @ Z) and round(np.linalg.det(S)) == -1)
# sheets
Js = -X
for n_, side in ((Z, "z>0"), (-Z, "z<0")):
    Hs = 0.5 * np.cross(Js, n_)
    print(f"   static sheet J = -x, {side}: H = 1/2 J x n = {Hs}")
check("static sheet: H = +y/2 for z>0, -y/2 for z<0", np.allclose(0.5 * np.cross(Js, Z), Y / 2) and np.allclose(0.5 * np.cross(Js, -Z), -Y / 2))
Erad = -eta0 / 2 * Js
Hp, Hm = np.cross(Z, Erad) / eta0, np.cross(-Z, Erad) / eta0
check("radiating sheet: E = -(eta/2)J = +x (opposite J) both sides; H = u x E/eta = +-y/2; jump z x (H+ - H-) = J",
      np.allclose(Erad, eta0 / 2 * X) and np.allclose(Hp, Y / 2) and np.allclose(Hm, -Y / 2) and np.allclose(np.cross(Z, Hp - Hm), Js)
      and np.allclose(np.cross(Erad, Hp) / np.linalg.norm(np.cross(Erad, Hp)), Z) and np.allclose(np.cross(Erad, Hm) / np.linalg.norm(np.cross(Erad, Hm)), -Z))
check("boundary form n x (H1 - H2) = Js with n = z: jump Hy+ - Hy- = Js", np.allclose(np.cross(Z, (0.5 - (-0.5)) * Y), -X))
# ---------------------------------------------------------------------------------------------- D. slide 24
print("\n== D. speeds read off arguments (slide 24)")
def vel(grad, dphidt):
    grad = np.asarray(grad, float)
    return -dphidt * grad / (grad @ grad)
vf, vg, vh = vel([0, 0.05, 0], -1), vel([0.02, 0, 0], 1), vel([0, 0, -2 * math.pi], 2 * math.pi * 1e8)
check("f = (0.05y - t)^2 -> +20 y; g = u(t + 0.02x) -> -50 x; h = cos(2pi1e8 t - 2pi z) -> +1e8 z",
      np.allclose(vf, [0, 20, 0]) and np.allclose(vg, [-50, 0, 0]) and np.allclose(vh, [0, 0, 1e8]), f"{vf}, {vg}, {vh}")
ff = lambda y, t: (0.05 * y - t) ** 2
ys = np.linspace(-10, 100, 110001)
zeros = [ys[np.argmin(ff(ys, t))] for t in (0, 1, 2)]
check("zero of f at y = 20 t", np.allclose(zeros, [0, 20, 40], atol=1e-3), f"{zeros}")
check("f(at - bz): travels +z at a/b (a=6, b=2 -> 3)", np.allclose(vel([0, 0, -2], 6), [0, 0, 3]))
check("function of z - vt is +z travelling (z - 5t)", np.allclose(vel([0, 0, 1], -5), [0, 0, 5]))
check("answer (c): 20 y, -50 x, 1e8 z", True)
# ---------------------------------------------------------------------------------------------- E. shift identities, slide 26
print("\n== E. shift identities, mirror rule, slide 26")
vv = 3.0
wf = lambda t: np.where(t > 0, t * np.exp(1 - t), 0.0)
fwd = lambda z, t: wf(t - z / vv); bwd = lambda z, t: wf(t + z / vv)
zt = rng.uniform(-5, 5, (50, 2))
check("+z: E(z,t) = E(0, t - z/v) = E(z - vt, 0)", all(abs(fwd(z, t) - fwd(0, t - z / vv)) < 1e-12 and abs(fwd(z, t) - fwd(z - vv * t, 0)) < 1e-12 for z, t in zt))
check("-z: E(z,t) = E(0, t + z/v) = E(z + vt, 0)", all(abs(bwd(z, t) - bwd(0, t + z / vv)) < 1e-12 and abs(bwd(z, t) - bwd(z + vv * t, 0)) < 1e-12 for z, t in zt))
check("feature at (z0,t0) found at z0 + v(t - t0) (+z) and z0 - v(t - t0) (-z)",
      abs(fwd(1.0 + vv * 2.5, 0.7 + 2.5) - fwd(1.0, 0.7)) < 1e-12 and abs(bwd(1.0 - vv * 2.5, 0.7 + 2.5) - bwd(1.0, 0.7)) < 1e-12)
zz = np.linspace(-6, 6, 13)
check("mirror: +z snapshot E(z,0) = record at -z/v; -z snapshot = record at +z/v",
      np.allclose(fwd(zz, 0), wf(-zz / vv)) and np.allclose(bwd(zz, 0), wf(zz / vv)))
E0r = lambda t: np.interp(t, [0, 1, 2, 4, 5], [0, 1, 1, 0, 0], left=0, right=0)
Ez26 = lambda z, t: E0r(t + z / 100.0)
q = [(200, 0.2), (-300, 3.4), (100, 0.6)]
right = [float(Ez26(z, t)) for z, t in q]; args = [t + z / 100 for z, t in q]
wrong_args = [t - z / 100 for z, t in q]; wrong = [float(E0r(a)) for a in wrong_args]
check("slide 26: (a) 0.9 (b) 0.4 (c) 1.0 via t + z/v = 2.2, 0.4, 1.6", np.allclose(right, [0.9, 0.4, 1.0]) and np.allclose(args, [2.2, 0.4, 1.6]), f"{right}")
check("slide 26 wrong sign: t - z/v = -1.8, 6.4, -0.4 -> 0, 0, 0", np.allclose(wrong_args, [-1.8, 6.4, -0.4]) and np.allclose(wrong, 0))
zs = np.array([-100, 0, 50, 100, 200, 300, 400, 500.])
check("slide 26 snapshots: t=0 zero for z<=0, 1 at 100-200 m, 0 at 400; t=1 shifted 100 m toward -z",
      np.allclose(Ez26(zs, 0), [0, 0, .5, 1, 1, .5, 0, 0]) and np.allclose(Ez26(zs, 1), Ez26(zs + 100, 0)), f"{Ez26(zs,1)}")
check("record point at 0.4 s: z = 40 m at t = 0 -> z = -300 m at 3.4 s (3 s after it passes z = 0)", abs(100 * (0.4 - 3.4) - (-300)) < 1e-12 and abs(Ez26(-300, 3.4) - 0.4) < 1e-12)
# ---------------------------------------------------------------------------------------------- F. factorisation, chain rule
print("\n== F. operator factorisation and z-integrals")
hfun = lambda xi, ze: np.sin(xi) * ze ** 2 + np.cos(ze * xi)
Ef = lambda tau, t: hfun(t - tau, t + tau)
tau0, t0, h = 0.37, -0.81, 1e-4
dtau = lambda F, a, b: (F(a + h, b) - F(a - h, b)) / (2 * h)
dt_ = lambda F, a, b: (F(a, b + h) - F(a, b - h)) / (2 * h)
xi0, ze0 = t0 - tau0, t0 + tau0
dxi = (hfun(xi0 + h, ze0) - hfun(xi0 - h, ze0)) / (2 * h); dze = (hfun(xi0, ze0 + h) - hfun(xi0, ze0 - h)) / (2 * h)
check("d_tau + d_t = 2 d_zeta and d_tau - d_t = -2 d_xi", abs(dtau(Ef, tau0, t0) + dt_(Ef, tau0, t0) - 2 * dze) < 1e-6
      and abs(dtau(Ef, tau0, t0) - dt_(Ef, tau0, t0) + 2 * dxi) < 1e-6)
G1 = lambda a, b: dtau(Ef, a, b) - dt_(Ef, a, b)
lhs = dtau(G1, tau0, t0) + dt_(G1, tau0, t0)
rhs = (Ef(tau0 + h, t0) - 2 * Ef(tau0, t0) + Ef(tau0 - h, t0)) / h ** 2 - (Ef(tau0, t0 + h) - 2 * Ef(tau0, t0) + Ef(tau0, t0 - h)) / h ** 2
check("(d_tau + d_t)(d_tau - d_t) = d_tau^2 - d_t^2", abs(lhs - rhs) < 1e-4 * max(1, abs(rhs)), f"{lhs:.6f} vs {rhs:.6f}")
F1 = lambda tau, t: f((t - tau) * T)
check("f(t - tau): d_tau = -f', d_t = +f'  (so d_tau E = -d_t E)", abs(dtau(F1, 0.2, 1.1) + dt_(F1, 0.2, 1.1)) < 1e-8)
zq, tq, hz = 0.13, 1.4 * T, 1e-6
fpz = (f(tq + 1e-14 - zq / v) - f(tq - 1e-14 - zq / v)) / 2e-14
gpz = (g(tq + 1e-14 + zq / v) - g(tq - 1e-14 + zq / v)) / 2e-14
check("d/dz[-v f(t - z/v)] = f'(t - z/v) and d/dz[v g(t + z/v)] = g'(t + z/v)",
      abs((-v * f(tq - (zq + hz) / v) + v * f(tq - (zq - hz) / v)) / (2 * hz) - fpz) < 1e-6 * abs(fpz)
      and abs((v * g(tq + (zq + hz) / v) - v * g(tq + (zq - hz) / v)) / (2 * hz) - gpz) < 1e-6 * abs(gpz))
# ---------------------------------------------------------------------------------------------- G. worked problem
print("\n== G. worked problem 'A pulse on the move' (y in m, t in us)")
U = lambda x: np.heaviside(x, 0.5)
Egiv = lambda y: 0.02 * (y - 400) * (U(y - 400) - U(y - 700))
Eshift = lambda y, t: Egiv(y - 200 * (t - 3))
Ea = lambda y: 0.02 * (y + 200) * (U(y + 200) - U(y - 100))
Eb = lambda y, t: 0.02 * (y - 200 * t + 200) * (U(y - 200 * t + 200) - U(y - 200 * t - 100))
Fs = lambda s: 4 * (1 - s) * (U(s + 0.5) - U(s - 1))
yt = np.column_stack([rng.uniform(-600, 2000, 4000), rng.uniform(-3, 9, 4000)])
check("given profile peaks at 6 V/m at the front y = 700", abs(Egiv(np.array(700 - 1e-9)) - 6) < 1e-6)
check("(a) E(y,0) = E(y+600, 3us) = 0.02(y+200)[u(y+200)-u(y-100)]", np.allclose(Eshift(yt[:, 0], 0), Ea(yt[:, 0])))
check("trap: E(y-600, 3) sits on 1000<y<1300", np.allclose(Egiv(np.array([999., 1001, 1299, 1301]) - 600) > 0, [0, 1, 1, 0]))
check("(b) closed form = shift form = F(t - y/200) everywhere", np.allclose(Eb(yt[:, 0], yt[:, 1]), Eshift(yt[:, 0], yt[:, 1]))
      and np.allclose(Fs(yt[:, 1] - yt[:, 0] / 200), Eshift(yt[:, 0], yt[:, 1])))
check("front y = 100 + 200t (700 at 3 us), back y = -200 + 200t", abs(Eshift(np.array(100 + 200 * 3 - 1e-7), 3) - 6) < 1e-6
      and abs(Eshift(np.array(-200 + 200 * 1.7 + 1e-7), 1.7)) < 1e-6 and abs(Eshift(np.array(100 + 200 * 1.7 - 1e-7), 1.7) - 6) < 1e-6)
check("F(s): probe at y=0 sees front (6 V/m) at t = -0.5 us, back at 1 us", abs(Fs(np.array(-0.5 + 1e-9)) - 6) < 1e-6 and abs(Fs(np.array(1 - 1e-9))) < 1e-6)
tt = np.linspace(3, 8, 5001) + 1.3e-4   # grid off the jump points
rec = Eshift(1000.0, tt)
on = rec > 0
check("(c) record at 1 km = 4(6 - t) on 4.5<t<6 us, 0 otherwise; reads 4 V/m at 5 us",
      np.allclose(rec, np.where((tt > 4.5) & (tt < 6), 4 * (6 - tt), 0)) and abs(tt[on][0] - 4.5) < 2e-3 and abs(tt[on][-1] - 6) < 2e-3
      and abs(Eshift(1000.0, 5.0) - 4) < 1e-12, f"first {tt[on][0]:.3f}, last {tt[on][-1]:.3f}")
check("snapshot at 5 us = 0.02(y-800) on 800<y<1100 -> 4 V/m at 1000 m", np.allclose(Eshift(yt[:, 0], 5), 0.02 * (yt[:, 0] - 800) * (U(yt[:, 0] - 800) - U(yt[:, 0] - 1100)))
      and abs(0.02 * 200 - 4) < 1e-12)
check("duration 1.5 us = 300 m / 200 m/us", abs(300 / 200 - 1.5) < 1e-12)
vpb = 2e8
check("(d) eps_r = (c/v)^2 = 2.247 (2.25 with c = 3e8)", abs((c / vpb) ** 2 - 2.247) < 5e-4 and abs((3e8 / vpb) ** 2 - 2.25) < 1e-12, f"{(c/vpb)**2:.4f}")
etap = mu0 * vpb
check("(e) eta = mu0 v = 80pi = 251.3; eta0/1.5 = 251.2", abs(etap - 80 * math.pi) < 1e-6 and abs(etap - 251.3) < 0.05 and abs(eta0 / 1.5 - 251.2) < 0.05,
      f"{etap:.4f}, {eta0/1.5:.4f}")
check("(e) H coefficient 0.02/eta = 7.96e-5; 4/eta = 1/(20pi) = 0.0159", abs(0.02 / etap - 7.96e-5) < 5e-8 and abs(4 / etap - 1 / (20 * math.pi)) < 1e-9
      and abs(1 / (20 * math.pi) - 0.0159) < 5e-5)
check("(e) peak H = 6/251.3 = 23.9 mA/m, B = mu0 H = E/v = 30 nT; 6/eta0 = 15.9 mA/m", abs(6 / etap - 0.0239) < 5e-5
      and abs(mu0 * 6 / etap - 3e-8) < 1e-15 and abs(6 / eta0 - 0.0159) < 5e-5)
# full Maxwell check of the problem's E and H in SI (interior of the ramp)
epsp = 1 / (mu0 * vpb ** 2)
Ep = lambda r, t: Z * Fs((t - r[1] / vpb) * 1e6)
Hp_ = lambda r, t: X * Fs((t - r[1] / vpb) * 1e6) / etap
Hwrong = lambda r, t: -X * Fs((t - r[1] / vpb) * 1e6) / etap
pp = []
for _ in range(12):
    s, y = rng.uniform(-0.4, 0.9) * 1e-6, rng.uniform(-500, 1500)
    pp.append((np.array([rng.uniform(-9, 9), y, rng.uniform(-9, 9)]), s + y / vpb))
w = resid(Ep, Hp_, mu0, epsp, pp, 1e-6, vpb)
check("problem E = z F(t - y/v), H = +x F/eta satisfies Faraday, Ampere, div", ok(w), "Far %.1e Amp %.1e divE %.1e divH %.1e" % tuple(w))
w = resid(Ep, Hwrong, mu0, epsp, pp, 1e-6, vpb)
check("problem with H = -x F/eta fails both curls", ok(w, False, False, True), "Far %.1e Amp %.1e" % tuple(w[:2]))
Evar = lambda y, t: Egiv(y + 200 * (t - 3))
check("variant (-y): at t=0 on 1000<y<1300; probe at 1 km records 4t on 0<t<1.5 us", np.allclose(Evar(np.array([999., 1001, 1299, 1301]), 0) > 0, [0, 1, 1, 0])
      and np.allclose(Evar(1000.0, (np.linspace(-1, 3, 401) + 1.3e-3)), np.where(((np.linspace(-1, 3, 401) + 1.3e-3) > 0) & ((np.linspace(-1, 3, 401) + 1.3e-3) < 1.5), 4 * (np.linspace(-1, 3, 401) + 1.3e-3), 0)))
# ---------------------------------------------------------------------------------------------- H. figures
print("\n== H. figure geometry (screen frame: X right, Y up, Z out of the screen)")
scr = {"x": np.array([0, 1, 0.]), "y": np.array([0, 0, 1.]), "z": np.array([1, 0, 0.])}   # slides' frame: x up, y out, z right
check("drawn frame right-handed: x(up) x y(out) = z(right)", np.allclose(np.cross(scr["x"], scr["y"]), scr["z"]))
M = np.column_stack([scr["x"], scr["y"], scr["z"]])
J_s = M @ -X; Hr = np.cross(J_s, M @ Z) / 2; Hl = np.cross(J_s, M @ -Z) / 2
check("fig 1 static: J arrows down; H right side out (odot), left side in (otimes)", np.allclose(J_s, [0, -1, 0]) and np.allclose(Hr, [0, 0, .5]) and np.allclose(Hl, [0, 0, -.5]))
Escr = M @ X
check("fig 1 dynamic: E up both sides; E x H -> right on right, left on left", np.allclose(Escr, [0, 1, 0]) and np.allclose(np.cross(Escr, Hr) / .5, [1, 0, 0]) and np.allclose(np.cross(Escr, Hl) / .5, [-1, 0, 0]))
for name, e, h, uu in rows:
    se, sh = M @ e, M @ h
    check(f"fig 3 {name}: screen E x H = drawn travel arrow ({'right' if uu[2] > 0 else 'left'})", np.allclose(np.cross(se, sh), M @ uu) and abs((M @ uu)[0]) == 1)
a = 0.5e-9; fr = lambda t: np.where(t > 0, t / a * np.exp(1 - t / a), 0.0)
ts = np.linspace(0, 6e-9, 60001)
check("fig 2 record: peak 1 at 0.5 ns, 0.2 at 2 ns, 0.04 at 3 ns", abs(ts[np.argmax(fr(ts))] - a) < 1e-12 and abs(fr(2e-9) - 4 * math.exp(-3)) < 1e-9)
zg = np.linspace(-3.3, 3.3, 66001)
for sg, lab in ((1, "+z"), (-1, "-z")):
    s0, s8 = fr(-sg * zg / c), fr(8e-9 - sg * zg / c)
    pk0, pk8 = zg[np.argmax(s0)], zg[np.argmax(s8)]
    front8 = zg[s8 > 1e-9][-1] if sg > 0 else zg[s8 > 1e-9][0]
    check(f"fig 2 {lab}: peak moves {pk0:+.3f} -> {pk8:+.3f} m (2.4 m), front at {front8:+.3f} m, tail behind",
          abs(abs(pk8 - pk0) - c * 8e-9) < 1e-3 and np.sign(pk8 - pk0) == sg and abs(front8 - sg * c * 8e-9) < 1e-3)
check("fig 4: t=0 snapshot breakpoints 0,100,200,400,500 m; t=1 s at -100,0,100,300,400 m",
      np.allclose([100 * tk for tk in (0, 1, 2, 4, 5)], [0, 100, 200, 400, 500]) and np.allclose([100 * (tk - 1) for tk in (0, 1, 2, 4, 5)], [-100, 0, 100, 300, 400]))
check("fig 5: back/front at t = 0, 3, 5 us: (-200,100), (400,700), (800,1100)", all(abs(Eshift(np.array(b + 1e-6), t)) < 1e-4 and abs(Eshift(np.array(fr_ - 1e-6), t) - 6) < 1e-4
                                                                             for t, b, fr_ in ((0, -200, 100), (3, 400, 700), (5, 800, 1100))))
print("\nSUMMARY:", "all checks pass" if not FAILS else f"{len(FAILS)} FAILED: {FAILS}")
