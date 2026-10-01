#!/usr/bin/env python3
"""V2-electrostatics: independent re-solve of practice problems 4.9, 7.9, 8.11, 9.10, 10.9.

Routes are chosen to differ from the page's own algebra where possible:
  4.9  finite-difference curl/div of the 3-D field, quad line integrals on the actual
       polygonal paths, dblquad flux of the numerical curl, brentq for x0
  7.9  E from superposition of infinite charge sheets (no boundary condition used),
       V by cumulative integration; silicon diode on a micron grid
  8.11 brute-force 2-D superposition of ~400k line charges (field and log-potential),
       Gauss with *total* (free + bound) charge, brentq for the null
  9.10 E-first self-consistent linear solve for induced/bound shell charges, V by
       superposing charged spherical shells and by quad from infinity
  10.9 1-D conservative finite-difference Laplace solve, flux/current by quadrature over
       the lossy hemisphere, dissipation by a volume integral, discharge by solve_ivp
Prints PASS/FAIL per quantity: a computed value is compared with the number printed on the
page (rounded to the page's significant figures where the page rounds).
"""
import numpy as np
from scipy import integrate, optimize
from scipy.sparse import diags
from scipy.sparse.linalg import spsolve

eps0 = 8.8541878128e-12
pi = np.pi
NP = NF = 0


def rnd(x, sig):
    return float(f"{x:.{sig}g}")


def check(name, got, page, sig=None, rtol=1e-6, atol=1e-9):
    """sig=k: computed value rounded to k significant figures must equal the page's number."""
    global NP, NF
    got = float(got)
    if sig is None:
        ok = bool(np.isclose(got, page, rtol=rtol, atol=atol))
    else:
        ok = bool(np.isclose(rnd(got, sig), page, rtol=1e-9, atol=0.0))
    NP += ok
    NF += (not ok)
    print(f"{'PASS' if ok else 'FAIL'}  {name:<62s} computed {got: .6g}   page {page: .6g}")


def head(s):
    print("\n======== " + s + " ========")


# =====================================================================================
head("4.9 Electrostatic or not")


def F1(p):
    return np.array([0.0, 3 * np.cos(pi * p[1] / 2), 0.0])


def F2(p):
    return np.array([0.0, 2 * np.cos(pi * p[0] / 2), 0.0])


def FE(p):
    return F1(p) + F2(p)


def jac(F, p, h=1e-5):
    p = np.asarray(p, float)
    J = np.zeros((3, 3))
    for j in range(3):
        d = np.zeros(3)
        d[j] = h
        J[:, j] = (F(p + d) - F(p - d)) / (2 * h)
    return J


def curl(F, p):
    J = jac(F, p)
    return np.array([J[2, 1] - J[1, 2], J[0, 2] - J[2, 0], J[1, 0] - J[0, 1]])


def div(F, p):
    return np.trace(jac(F, p))


rng = np.random.default_rng(1)
pts = rng.uniform(-3, 3, size=(300, 3))
check("(a) max |curl E1| over 300 random points [V/m^2]", max(np.abs(curl(F1, p)).max() for p in pts), 0.0, atol=1e-6)
check("(a) max |curl E2 - (-pi sin(pi x/2)) z_hat|",
      max(np.abs(curl(F2, p) - np.array([0, 0, -pi * np.sin(pi * p[0] / 2)])).max() for p in pts), 0.0, atol=1e-6)
check("(b) max |div E2| (E2 carries no charge)", max(abs(div(F2, p)) for p in pts), 0.0, atol=1e-6)
check("(b) max |rho - (-(3pi/2) eps0 sin(pi y/2))| [C/m^3]",
      max(abs(eps0 * div(FE, p) + 1.5 * pi * eps0 * np.sin(pi * p[1] / 2)) for p in pts), 0.0, atol=1e-19)
ys = np.linspace(-4, 4, 8001)
rho_y = np.array([eps0 * div(FE, (0.37, y, 0.2)) for y in ys])
check("(b) max |rho| on grid y in [-4,4] [C/m^3]", np.abs(rho_y).max(), 4.17e-11, sig=3)
ar = np.abs(rho_y)
pk = ys[1:-1][(ar[1:-1] >= ar[:-2]) & (ar[1:-1] >= ar[2:])]
print("      |rho| local maxima at y =", np.round(pk, 3))
for y, s in [(1, -1), (-1, 1), (3, 1)]:
    check(f"(b) sign of rho on y = {y} m", np.sign(eps0 * div(FE, (0.0, y, 0.0))), s)
xs = np.linspace(-4, 4, 8001)
cz = np.array([np.linalg.norm(curl(FE, (x, 0.4, -0.1))) for x in xs])
check("(c) max |curl E| on grid x in [-4,4] [V/m^2]", cz.max(), 3.14, sig=3)
pkx = xs[1:-1][(cz[1:-1] >= cz[:-2]) & (cz[1:-1] >= cz[2:])]
print("      |curl E| local maxima at x =", np.round(pkx, 3))


def line_int(F, verts):
    tot = 0.0
    for A, B in zip(verts[:-1], verts[1:]):
        A = np.asarray(A, float)
        d = np.asarray(B, float) - A
        tot += integrate.quad(lambda t: F(A + t * d) @ d, 0, 1, epsabs=1e-13, epsrel=1e-12)[0]
    return tot


O, P = (0, 0, 0), (2, 1, 0)
rA, rB = [O, (2, 0, 0), P], [O, (0, 1, 0), P]
IA, IB = line_int(F2, rA), line_int(F2, rB)
check("(d) route A  int E2.dl [V]", IA, -2.0)
check("(d) route B  int E2.dl [V]", IB, 2.0)
flux = integrate.dblquad(lambda y, x: curl(F2, (x, y, 0.0))[2], 0, 2, 0, 1)[0]
check("(d) flux of numerical curl E2 over rectangle, dS = +z dxdy [V]", flux, -4.0, rtol=1e-6)
loop = line_int(F2, [O, (2, 0, 0), (2, 1, 0), (0, 1, 0), O])
check("(d) closed loop (A then B reversed) [V]", loop, -4.0)
poly = np.array([[0, 0], [2, 0], [2, 1], [0, 1]], float)
sa = 0.5 * np.sum(poly[:, 0] * np.roll(poly[:, 1], -1) - np.roll(poly[:, 0], -1) * poly[:, 1])
check("(d) that loop is CCW seen from +z (signed area sign)", np.sign(sa), 1.0)
check("(e) straight segment O->P  int E2.dl [V]", line_int(F2, [O, P]), 0.0, atol=1e-10)
s_ = np.linspace(0, 1, 11)
check("(e) E2y odd about x = 1: max|E2y(1+s)+E2y(1-s)|",
      max(abs(F2((1 + s, 0, 0))[1] + F2((1 - s, 0, 0))[1]) for s in s_), 0.0, atol=1e-12)


def stair(x0):
    return line_int(F2, [O, (x0, 0, 0), (x0, 1, 0), P])


x0 = optimize.brentq(lambda x: stair(x) + 1.0, 0.0, 2.0, xtol=1e-13)
check("(e) staircase climb x0 giving -1 V [m]", x0, 4 / 3)
vals = np.array([stair(x) for x in np.linspace(0, 2, 201)])
check("(e) staircase values: minimum over x0 in [0,2] [V]", vals.min(), -2.0)
check("(e) staircase values: maximum over x0 in [0,2] [V]", vals.max(), 2.0)
sg = np.sign(vals + 1)
check("(e) number of x0 in [0,2] giving -1 V", np.sum(sg[:-1] != sg[1:]), 1)
check("(e) int E1.dl route A [V] (6/pi)", line_int(F1, rA), 6 / pi)
check("(e) int E1.dl route B [V] (~1.91)", line_int(F1, rB), 1.91, sig=3)
check("(e) int E1.dl straight O->P equals route A (curl-free)", line_int(F1, [O, P]), 6 / pi)

# =====================================================================================
head("7.9 Junction with an intrinsic layer")


def sheets_E(z, rho):
    """eps*E_z from superposing infinite sheets: E = (1/2eps)[Q(left of z) - Q(right of z)] (returns eps*E)."""
    Ql = integrate.cumulative_trapezoid(rho, z, initial=0.0)
    return 0.5 * (Ql - (Ql[-1] - Ql))


z = np.linspace(-4.0, 3.0, 700001)
rho = np.where((z > -3) & (z < -1), -3.0, 0.0) + np.where((z > 1) & (z < 2), 6.0, 0.0)
check("(a) net charge per unit area [C/m^2]", integrate.trapezoid(rho, z), 0.0, atol=1e-4)
e0E = sheets_E(z, rho)
page_e0E = np.select([(z > -3) & (z < -1), (z >= -1) & (z <= 1), (z > 1) & (z < 2)],
                     [-3 * (z + 3), -6.0 + 0 * z, 6 * (z - 2)], 0.0)
check("(a) max |eps0 Ez(sheets) - page piecewise| [C/m^2]", np.abs(e0E - page_e0E).max(), 0.0, atol=2e-4)
check("(a) max |eps0 Ez| for z < -3 (sheet sum, no BC imposed)", np.abs(e0E[z < -3.0001]).max(), 0.0, atol=2e-4)
check("(a) max |eps0 Ez| for z > 2", np.abs(e0E[z > 2.0001]).max(), 0.0, atol=2e-4)
check("(a) sign of Ez inside (field along -z)", np.sign(np.interp(0.3, z, e0E)), -1)
e0V = -integrate.cumulative_trapezoid(e0E, z, initial=0.0)
e0V -= np.interp(-3.0, z, e0V)
for zz, val in [(-1, 6), (0, 12), (1, 18), (2, 21)]:
    check(f"(b) eps0 V({zz})  [V*eps0]", np.interp(zz, z, e0V), val, atol=2e-4)
zt = np.linspace(-3, 3, 601)
page_e0V = np.select([zt <= -1, zt <= 1, zt <= 2], [1.5 * (zt + 3) ** 2, 6 * (zt + 2), 21 - 3 * (zt - 2) ** 2], 21.0)
check("(b) max |eps0 V - page piecewise| on [-3,3]", np.abs(np.interp(zt, z, e0V) - page_e0V).max(), 0.0, atol=2e-4)
for zz, s in [(-2, 1), (0, 0), (1.5, -1)]:
    i = np.searchsorted(z, zz)
    d2 = (e0V[i + 50] - 2 * e0V[i] + e0V[i - 50]) / (50 * (z[1] - z[0])) ** 2
    check(f"(b) sign of V'' at z = {zz} (bowl/line/dome)", np.sign(np.round(d2, 3)), s)
check("(b) V(0) [V]", np.interp(0, z, e0V) / eps0, 1.36e12, sig=3)
check("(c) V(2)-V(-3) [V]", (np.interp(2, z, e0V) - np.interp(-3, z, e0V)) / eps0, 2.37e12, sig=3)
check("(c) max |Ez| [V/m]", np.abs(e0E).max() / eps0, 6.78e11, sig=3)
inI = (z > -0.999) & (z < 0.999)
check("(c) |Ez| constant across intrinsic layer (spread) [eps0 units]", np.ptp(e0E[inI]), 0.0, atol=2e-4)
rho0 = np.where((z > -3) & (z < -1), -3.0, 0.0) + np.where((z > -1) & (z < 0), 6.0, 0.0)
e0E0 = sheets_E(z, rho0)
dV0 = integrate.trapezoid(-e0E0, z)
check("(c) no-layer junction V(right)-V(left) [eps0 units]", dV0, 9.0, atol=2e-4)
check("(c) no-layer junction [V]", dV0 / eps0, 1.02e12, sig=3)
check("(c) no-layer peak field unchanged [eps0 units]", np.abs(e0E0).max(), 6.0, atol=2e-4)
check("(c) lecture formula rho2 W2 (W1+W2)/2", 6 * 1 * 3 / 2, 9.0)
check("(c) difference 21-9 = Emax*g", 21 - dV0, 6 * 2, atol=2e-4)
# (d) silicon p-i-n, positions in m
e, eps = 1.602e-19, 11.7 * eps0
NA, ND, W1, g, W2 = 1e22, 2e22, 0.2e-6, 0.2e-6, 0.1e-6
zs = np.linspace(-0.3e-6, 0.6e-6, 900001)
rs = np.where((zs > -W1) & (zs < 0), -e * NA, 0.0) + np.where((zs > g) & (zs < g + W2), e * ND, 0.0)
Es = sheets_E(zs, rs) / eps
check("(d) e N_A [C/m^3]", e * NA, 1.60e3, sig=3)
check("(d) e N_D [C/m^3]", e * ND, 3.20e3, sig=3)
check("(d) N_A W1 [m^-2]", NA * W1, 2e15)
check("(d) N_D W2 [m^-2]", ND * W2, 2e15)
check("(d) E_max [V/m]", np.abs(Es).max(), 3.09e6, sig=3)
Vbi = integrate.trapezoid(-Es, zs)
check("(d) built-in potential V(n side) - V(p side) [V]", Vbi, 1.08, sig=3)
check("(d) area rule 6(1+2+0.5) for part (c)", 6 * (1 + 2 + 0.5), 21.0)

# =====================================================================================
head("8.11 Electret rod in a grounded tube")
a, b = 0.02, 0.05
P0 = 1e5 * eps0
check("P0 [uC/m^2]", P0 * 1e6, 0.885, sig=3)


def Pr(r):
    return P0 * r / a if r < a else 0.0


h = 1e-7
rbfd = np.array([-(1 / r) * ((r + h) * Pr(r + h) - (r - h) * Pr(r - h)) / (2 * h) for r in (0.003, 0.01, 0.017)])
check("(a) rho_b by FD of -(1/r)d(rP)/dr [units of eps0]", rbfd.mean() / eps0, -1e7, rtol=1e-6)
check("(a) rho_b uniform (spread of FD values) [C/m^3]", np.ptp(rbfd), 0.0, atol=1e-12)
check("(a) rho_b [uC/m^3]", rbfd.mean() * 1e6, -88.5, sig=3)
rho_b = -2 * P0 / a
lam_v = integrate.quad(lambda r: rho_b * 2 * pi * r, 0, a)[0]
lam_s = 2 * pi * a * Pr(a * (1 - 1e-15))
check("(a) rho_sb = P.n at r = a [units of eps0]", Pr(a * (1 - 1e-15)) / eps0, 1e5)
check("(a) volume bound charge per length [units of pi eps0]", lam_v / (pi * eps0), -4000)
check("(a) volume bound charge per length [nC/m]", lam_v * 1e9, -111, sig=3)
check("(a) surface bound charge per length [nC/m]", lam_s * 1e9, 111, sig=3)
check("(a) total bound charge per length [C/m]", lam_v + lam_s, 0.0, atol=1e-20)

# brute force: cross-section as ~400k line charges (volume cells + ring of surface charge)
Nr, Nph, Ns = 400, 1000, 4000
rc = (np.arange(Nr) + 0.5) * a / Nr
ph = (np.arange(Nph) + 0.5) * 2 * pi / Nph
R_, PH_ = np.meshgrid(rc, ph, indexing="ij")
phs = (np.arange(Ns) + 0.5) * 2 * pi / Ns
X = np.concatenate([(R_ * np.cos(PH_)).ravel(), a * np.cos(phs)])
Y = np.concatenate([(R_ * np.sin(PH_)).ravel(), a * np.sin(phs)])
L = np.concatenate([(rho_b * R_ * (a / Nr) * (2 * pi / Nph)).ravel(), np.full(Ns, lam_s / Ns)])


def E2d(x, y):
    dx, dy = x - X, y - Y
    r2 = dx * dx + dy * dy
    return np.array([np.sum(L * dx / r2), np.sum(L * dy / r2)]) / (2 * pi * eps0)


def V2d(x, y):
    return np.sum(-L * np.log(np.hypot(x - X, y - Y))) / (2 * pi * eps0)


def lam_bound_enc(r):
    return rho_b * pi * r ** 2 if r < a else lam_v + lam_s


def Er(r, lam_free=0.0):
    """Gauss's law with the TOTAL (free + bound) charge enclosed."""
    return (lam_free + lam_bound_enc(r)) / (2 * pi * eps0 * r)


check("(b) D_r = free charge enclosed/(2 pi r) for r < b [C/m^2]", 0.0, 0.0)
check("(b) E_r at r = 1 cm (Gauss, total charge) [V/m]", Er(0.01), -5e4)
check("(b) E_r just inside r = a [V/m]", Er(a * (1 - 1e-12)), -1e5)
check("(b) E_r in the gap, r = 3.5 cm [V/m]", Er(0.035), 0.0, atol=1e-6)
check("(b) D_r = eps0 E_r + P_r at 1 cm (should be 0) [C/m^2]", eps0 * Er(0.01) + Pr(0.01), 0.0, atol=1e-20)
Eb = E2d(0.01, 0.0)
check("(b) brute-force sum: E_x at (1 cm, 0) [V/m]", Eb[0], -5e4, rtol=3e-3)
check("(b) brute-force sum: E_y at (1 cm, 0) [V/m]", Eb[1], 0.0, atol=100)
Eb = E2d(0.0, 0.019)
check("(b) brute-force sum: E_y at (0, 1.9 cm) vs -5e6 r [V/m]", Eb[1], -5e6 * 0.019, rtol=3e-3)
Eb = E2d(0.025, 0.02)
check("(b) brute-force sum: |E| in the gap at r = 3.2 cm [V/m]", np.hypot(*Eb), 0.0, atol=100)
dV = integrate.quad(Er, 0, b, points=[a], limit=200)[0]
check("(c) V(0)-V(b) = int_0^b E_r dr [V]", dV, -1000)
check("(c) brute-force log-potential V(0)-V(b) [V]", V2d(0, 0) - V2d(b, 0), -1000, rtol=3e-3)
check("(c) charge on tube inner surface = -(free enclosed) [C/m]", -0.0, 0.0)
lam_l = 1000 * pi * eps0
check("(d) rho_l [nC/m]", lam_l * 1e9, 27.8, sig=3)
check("(d) rho_l/(2 pi) [units of eps0]", lam_l / (2 * pi) / eps0, 500)
r0 = optimize.brentq(lambda r: Er(r, lam_l), 1e-4, a * (1 - 1e-9), xtol=1e-15)
check("(d) radius of E = 0 inside the electret [m]", r0, 0.01)
check("(d) E_r at 0.5 cm is outward (sign)", np.sign(Er(0.005, lam_l)), 1)
check("(d) E_r at 1.5 cm is inward (sign)", np.sign(Er(0.015, lam_l)), -1)
check("(d) E_r just inside a [V/m]", Er(a * (1 - 1e-12), lam_l), -7.5e4)
check("(d) E_r just outside a [V/m]", Er(a * (1 + 1e-12), lam_l), 2.5e4)
check("(d) E_r at the tube [V/m]", Er(b * (1 - 1e-12), lam_l), 1e4)
Eb = E2d(0.015, 0.0) + np.array([lam_l / (2 * pi * eps0 * 0.015), 0.0])
check("(d) brute-force E_x at (1.5 cm, 0) vs 500/r - 5e6 r [V/m]", Eb[0], 500 / 0.015 - 5e6 * 0.015, rtol=3e-3)
Db = lam_l / (2 * pi * b)
check("(d) D_r(b) [units of eps0]", Db / eps0, 1e4)
check("(d) rho_s on tube inner surface = n.D, n = -r_hat [nC/m^2]", -Db * 1e9, -88.5, sig=3)
check("(d) tube inner surface per length [nC/m]", -Db * 2 * pi * b * 1e9, -27.8, sig=3)
check("(d) tube inner surface per length = -rho_l", -Db * 2 * pi * b / lam_l, -1.0)
j_b = (Er(a * (1 + 1e-12)) - Er(a * (1 - 1e-12)))
j_d = (Er(a * (1 + 1e-12), lam_l) - Er(a * (1 - 1e-12), lam_l))
check("check: eps0[E(a+)-E(a-)] in (b) [units of eps0]", j_b, 1e5)
check("check: eps0[E(a+)-E(a-)] in (d) [units of eps0]", j_d, 1e5)
check("check: null from rho_l + rho_b pi r0^2 = 0, r0^2 [m^2]", -lam_l / (rho_b * pi), 1e-4)

# =====================================================================================
head("9.10 Sphere, shell and two dielectric layers")
Q1, Qsh, er1, er2 = 5.0, -6.0, 5.0, 2.0
# E-first self-consistent solve.  unknowns: qin(r=2), qout(r=3), b1(r=1), b2(r=2), b3(r=3), b4(r=4)
# face charge of a linear layer: inner face -(er-1)*Qtot_enc(just inside layer), outer face +(er-1)*same
A = np.array([
    [1, 1, 0, 0, 0, 0],                       # qin + qout = Qsh
    [1, 0, 1, 1, 0, 0],                       # E = 0 in shell metal: Q1+b1+b2+qin = 0
    [0, 0, er1, 0, 0, 0],                     # b1 = -(er1-1)(Q1+b1)
    [0, 0, -(er1 - 1), 1, 0, 0],              # b2 = (er1-1)(Q1+b1)
    [er2 - 1, er2 - 1, er2 - 1, er2 - 1, er2, 0],  # b3 = -(er2-1)(Q1+b1+b2+qin+qout+b3)
    [-(er2 - 1), -(er2 - 1), -(er2 - 1), -(er2 - 1), -(er2 - 1), 1]], float)  # b4 = (er2-1)(...+b3)
rhs = np.array([Qsh, -Q1, -(er1 - 1) * Q1, (er1 - 1) * Q1, -(er2 - 1) * Q1, (er2 - 1) * Q1])
qin, qout, b1, b2, b3, b4 = np.linalg.solve(A, rhs)
shells = [(1.0, Q1 + b1), (2.0, qin + b2), (3.0, qout + b3), (4.0, b4)]


def Qtot(r):
    return sum(q for R, q in shells if R < r)


def epsr(r):
    return er1 if 1 < r < 2 else (er2 if 3 < r < 4 else 1.0)


def fields(r):
    if r < 1 or 2 < r < 3:
        return 0.0, 0.0, 0.0
    E = Qtot(r) / (4 * pi * eps0 * r ** 2)
    D = epsr(r) * eps0 * E
    return D, E, D - eps0 * E


for r, (Dp, Ep, Pp) in [(1.5, (5 / (4 * pi * 2.25), 1 / (4 * pi * eps0 * 2.25), 1 / (pi * 2.25))),
                        (3.5, (-1 / (4 * pi * 12.25), -1 / (8 * pi * eps0 * 12.25), -1 / (8 * pi * 12.25))),
                        (5.0, (-1 / (4 * pi * 25), -1 / (4 * pi * eps0 * 25), 0.0))]:
    D_, E_, P_ = fields(r)
    check(f"(a) D_r at r = {r} m [C/m^2]", D_, Dp, atol=1e-15)
    check(f"(a) E_r at r = {r} m [V/m]", E_, Ep, atol=1e-6)
    check(f"(a) P_r at r = {r} m [C/m^2]", P_, Pp, atol=1e-15)
check("(a) metal regions: E at r = 0.5 and 2.5 m", abs(fields(0.5)[1]) + abs(fields(2.5)[1]), 0.0)


def Dr(r):
    return fields(r)[0]


dd = 1e-9
rs_free = [Dr(1 + dd) - Dr(1 - dd), Dr(2 + dd) - Dr(2 - dd), Dr(3 + dd) - Dr(3 - dd), Dr(4 + dd) - Dr(4 - dd)]
for R, val, pg in zip([1, 2, 3, 4], rs_free, [0.398, -0.0995, -0.00884, 0.0]):
    if pg == 0.0:   # D ~ 1/r^2 changes by ~5e-12 across the +-1e-9 m probe: compare with an absolute tolerance
        check(f"(b) free rho_s = r.(D_out - D_in) at r = {R} m [C/m^2]", val, pg, atol=1e-10)
    else:
        check(f"(b) free rho_s = r.(D_out - D_in) at r = {R} m [C/m^2]", val, pg, sig=3)
check("(b) charge on shell inner surface [C]", qin, -5.0)
check("(b) charge on shell outer surface [C]", qout, -1.0)
Pf = lambda r: fields(r)[2]
rsb = [-Pf(1 + dd), Pf(2 - dd), -Pf(3 + dd), Pf(4 - dd)]
for R, val, pg in zip([1, 2, 3, 4], rsb, [-0.318, 0.0796, 0.00442, -0.00249]):
    check(f"(c) bound rho_sb at r = {R} m [C/m^2]", val, pg, sig=3)
for R, q, pg in zip([1, 2, 3, 4], [b1, b2, b3, b4], [-4, 4, 0.5, -0.5]):
    check(f"(c) bound charge total at r = {R} m [C]", q, pg)
check("(c) rho_sb(r=3) exact = 1/(72 pi)", rsb[2], 1 / (72 * pi))
check("(c) rho_sb(r=4) exact = -1/(128 pi)", rsb[3], -1 / (128 * pi))


def Vsup(r):  # superposition of charged spherical shells (free + bound), V(inf) = 0
    return sum(q / (4 * pi * eps0 * max(r, R)) for R, q in shells)


Vsh_int = integrate.quad(lambda r: fields(r)[1], 3 + 1e-12, 4, limit=200)[0] + \
    integrate.quad(lambda r: fields(r)[1], 4, np.inf, limit=200)[0]
check("(d) V_shell by quad from infinity [V]", Vsh_int, -2.62e9, sig=3)
check("(d) V_shell by shell superposition = -7/(96 pi eps0)", Vsup(3.0), -7 / (96 * pi * eps0), rtol=1e-9)
V0_int = Vsh_int + integrate.quad(lambda r: fields(r)[1], 1 + 1e-12, 2 - 1e-12)[0]
check("(d) V(0) by quad [V]", V0_int, 1.87e9, sig=3)
check("(d) V(0) by shell superposition = 5/(96 pi eps0)", Vsup(0.0), 5 / (96 * pi * eps0), rtol=1e-9)
check("(d) V(core) - V(shell) [V]", Vsup(0.0) - Vsup(3.0), 4.49e9, sig=3)
check("(d) V(core) - V(shell) = 1/(8 pi eps0)", Vsup(0.0) - Vsup(3.0), 1 / (8 * pi * eps0), rtol=1e-9)
check("check: eps0[E(4+)-E(4-)] = -1/(128 pi) [C/m^2]", eps0 * (fields(4 + dd)[1] - fields(4 - dd)[1]),
      -1 / (128 * pi), rtol=1e-6)

# =====================================================================================
head("10.9 Leaky spheres, one lossy half")
a, b, V0, eps, sig = 0.01, 0.02, 100.0, 3 * eps0, 1e-8
N = 20001
r = np.linspace(a, b, N)
hh = r[1] - r[0]
rp, rm = (r[1:-1] + hh / 2) ** 2, (r[1:-1] - hh / 2) ** 2
Amat = diags([rm[1:], -(rp + rm), rp[:-1]], [-1, 0, 1], format="csc")
rhs = np.zeros(N - 2)
rhs[-1] = -rp[-1] * (-V0)          # V(b) = -V0 ; V(a) = 0 contributes nothing
V = np.concatenate([[0.0], spsolve(Amat, rhs), [-V0]])
check("(b) max |V_FD - (-200 + 2/r)| [V]", np.abs(V - (-200 + 2 / r)).max(), 0.0, atol=1e-6)
E = -np.gradient(V, r, edge_order=2)
check("(b) E_r(a) [V/m]", E[0], 2e4, rtol=1e-4)
check("(b) E_r(b) [V/m]", E[-1], 5e3, rtol=1e-4)
check("(a)(i) sign of charge on inner sphere: n.D = eps E_r(a), n = +r", np.sign(eps * E[0]), 1)
check("(a)(ii) rho_s on inner sphere, same in both halves [uC/m^2]", eps * E[0] * 1e6, 0.531, sig=3)
check("(a)(ii) rho_s = 6e4 eps0", eps * E[0] / eps0, 6e4, rtol=1e-4)
# interface z = 0: radial E has no z-component at points of the plane
pz = np.array([0.012, -0.007, 0.0])
check("(b) E.z_hat on z = 0 for radial E", (2 / (pz @ pz)) * (pz / np.linalg.norm(pz)) @ np.array([0, 0, 1.0]), 0.0)
k = N // 2
Q = 4 * pi * r[k] ** 2 * eps * E[k]
C = Q / V0
check("(b) C = Q/V0 with Q = flux of D [pF]", C * 1e12, 6.676, sig=4)
check("(b) charge on inner sphere [pC]", Q * 1e12, 667.6, sig=4)


def I_out(i):
    sig_th = lambda th: sig if th > pi / 2 else 0.0      # z < 0  <=>  theta > pi/2
    return integrate.quad(lambda th: sig_th(th) * E[i] * r[i] ** 2 * np.sin(th) * 2 * pi, 0, pi, points=[pi / 2])[0]


Is = [I_out(i) for i in (1000, k, N - 1000)]
check("(c) current through lower hemisphere at three radii: spread [A]", np.ptp(Is), 0.0, atol=1e-15)
I = Is[1]
check("(c) leakage current, outward [nA]", I * 1e9, 125.7, sig=4)
G = I / V0
check("(c) G [nS]", G * 1e9, 1.257, sig=4)
check("(c) R [MOhm]", 1 / G / 1e6, 795.8, sig=4)
Pdis = integrate.quad(lambda rr: sig * (np.interp(rr, r, E)) ** 2 * 2 * pi * rr ** 2, a, b, limit=200)[0]
check("(c) power = int sigma E^2 dV over the lossy half [uW]", Pdis * 1e6, 12.57, sig=4)
check("(c) (sigma/eps) C [nS]", sig / eps * C * 1e9, 2.513, sig=4)
check("(c) G / ((sigma/eps) C)", G / (sig / eps * C), 0.5, rtol=1e-4)


def rhs_ode(t, y):        # y = V(b); shell charge C*V(b) (inner sphere grounded), dQ/dt = G*(0 - V(b))
    return [-G * y[0] / C]


ev = lambda t, y: y[0] + 50.0
ev.terminal = True
sol = integrate.solve_ivp(rhs_ode, [0, 0.1], [-V0], events=ev, rtol=1e-11, atol=1e-12)
th = sol.t_events[0][0]
check("(d) time for V(b) to reach -50 V [ms]", th * 1e3, 3.682, sig=4)
check("(d) tau = t_half/ln2 [ms]", th / np.log(2) * 1e3, 5.313, sig=4)
check("(d) tau = 2 eps/sigma", th / np.log(2), 2 * eps / sig, rtol=1e-6)
check("(d) eps/sigma [ms]", eps / sig * 1e3, 2.656, sig=4)
check("check: R C [ms]", (1 / G) * C * 1e3, 5.313, sig=4)
# --- the case the original statement left open: shell also facing a distant ground at 0 V
Cext = 4 * pi * eps0 * b
print("      [info] shell-to-infinity capacitance 4 pi eps0 b = %.4g pF; extra charge at -100 V = %.4g pC;"
      " shell total would be %.4g pC" % (Cext * 1e12, -Cext * V0 * 1e12, (-Q - Cext * V0) * 1e12))
check("(d) note: 4 pi eps0 b [pF]", Cext * 1e12, 2.225, sig=4)
check("(d) note: tau with that capacitance added, (C + 4 pi eps0 b)/G [ms]", (C + Cext) / G * 1e3, 7.08, sig=3)

print(f"\nTOTAL: {NP} PASS, {NF} FAIL")
