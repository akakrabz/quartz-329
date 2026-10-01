#!/usr/bin/env python3
"""R09.py - independent verification of practice page 09 (Lecture 9: static fields in dielectric media).

numpy/scipy only. One section per problem. Every final number, sign and direction is recomputed from
the problem's given data, where possible by a route independent of the page's own solution:
finite-volume solves of d/dz(eps dV/dz) = -rho (1-D and 2-D), self-consistent bound-charge solves
with direct 2-D Coulomb integrals over cylindrical sheets, shell superposition for potentials,
a field-line ODE, numerical flux integrals. The page's stated answers are transcribed and compared.
9.10 is checked with its NEW parameters (core +5 C, inner eps = 5 eps0, shell -6 C, coating 2 eps0),
and the exam-cited problems are checked against the catalogue keys for non-coincidence.
"""
import re
import warnings
import numpy as np
from scipy import integrate, optimize, sparse
from scipy.sparse.linalg import spsolve

e0 = 8.8541878128e-12
pi = np.pi
R3 = 5e-3            # tolerance for values quoted to 3 significant figures
results = []
PAGE = "/home/claude/work/content-src/practice/09-static-fields-in-dielectric-media.md"


def chk(name, got, want, rtol=1e-9, atol=0.0):
    got = np.atleast_1d(np.asarray(got, dtype=float))
    want = np.atleast_1d(np.asarray(want, dtype=float))
    ok = bool(got.shape == want.shape and np.allclose(got, want, rtol=rtol, atol=atol))
    results.append(ok)
    g = ", ".join(f"{v:.6g}" for v in got)
    w = ", ".join(f"{v:.6g}" for v in want)
    print(f"{'PASS' if ok else 'FAIL'}  {name}: computed [{g}]  page [{w}]")
    return ok


def chk_true(name, cond):
    cond = bool(cond)
    results.append(cond)
    print(f"{'PASS' if cond else 'FAIL'}  {name}")
    return cond


def fd1d(L, N, epsr_half, Vl, Vr, sheets=()):
    """Finite-volume solve of d/dz(eps dV/dz) = -rho_s(sheets)/1 on [0, L], uniform nodes.
    eps given (in units of eps0) at the half points; sheets = [(z_s, sigma/eps0)] lumped on nodes.
    Dirichlet V(0) = Vl, V(L) = Vr. Returns z, zh, e(zh), V(z)."""
    z = np.linspace(0.0, L, N + 1)
    h = L / N
    zh = 0.5 * (z[:-1] + z[1:])
    e = epsr_half(zh)
    main = np.empty(N + 1)
    main[1:-1] = -(e[:-1] + e[1:])
    main[0] = main[-1] = 1.0
    lower = np.zeros(N)
    upper = np.zeros(N)
    lower[:-1] = e[:-1]
    upper[1:] = e[1:]
    rhs = np.zeros(N + 1)
    rhs[0], rhs[-1] = Vl, Vr
    for zs, sig in sheets:
        rhs[int(round(zs / h))] -= sig * h
    A = sparse.diags([lower, main, upper], [-1, 0, 1], format="csc")
    return z, zh, e, spsolve(A, rhs)


def ring_Er(r, R, lam):
    """Radial E at distance r from the axis due to a uniform cylindrical sheet of radius R holding
    lam C/m, by direct 2-D Coulomb integration over its line charges (R = 0: a line on the axis)."""
    if R == 0.0:
        return lam / (2 * pi * e0 * r)
    f = lambda ph: (r - R * np.cos(ph)) / (r * r + R * R - 2 * r * R * np.cos(ph))
    w = abs(r - R) / np.sqrt(r * R)                      # angular width of the near-field peak at phi = 0
    pts = [p for p in (w, 3 * w, 10 * w, 30 * w, 100 * w, 300 * w) if p < pi]
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", integrate.IntegrationWarning)
        val = 2 * integrate.quad(f, 0.0, pi, points=pts or None, limit=1000, epsabs=1e-10 / R, epsrel=1e-11)[0]
    return lam / (2 * pi) * val / (2 * pi * e0)


# ---------------------------------------------------------------------------------------------
print("== 9.1 three layers between charged plates: FD solve of d/dz(eps dV/dz) = 0 ==")
er91 = lambda zh: np.where(zh < 1, 1.0, np.where(zh < 2, 2.0, 3.0))
z, zh, e, Vu = fd1d(3.0, 3000, er91, 0.0, 1.0)          # unit top voltage, then scale
h = z[1] - z[0]
Dz_unit = -e0 * e[0] * (Vu[1] - Vu[0]) / h              # D_z at the bottom plate per volt
s = (-6 * e0) / Dz_unit                                  # bottom rho_s = z.D = -6 eps0
V = s * Vu
Ez = -np.diff(V) / h
Dz = e0 * e * Ez
Pz = Dz - e0 * Ez
mid = [np.argmin(abs(zh - zz)) for zz in (0.5, 1.5, 2.5)]
chk("9.1 D_z in the three layers [C/m^2]", Dz[mid], [-6 * e0] * 3)
chk("9.1 D_z numeric ~ -5.31e-11 C/m^2", Dz[mid[0]], -5.31e-11, rtol=R3)
chk("9.1 E_z in the three layers [V/m]", Ez[mid], [-6, -3, -2])
chk("9.1 P_z / eps0 in the three layers", Pz[mid] / e0, [0, -3, -4], atol=1e-9)
iz = [np.argmin(abs(z - zz)) for zz in (1, 2, 3)]
chk("9.1 V(1), V(2), V(3) [V]", V[iz], [6, 9, 11])
chk("9.1 top plate rho_s = -z.D(3-) [eps0 C/m^2]", -Dz[-1] / e0, 6)
# Summer 2020 HE2 #1a key (catalogue setup: -2/+2 C/m^2, eps0 then 2 eps0, gap 2 m), same solver
z2, zh2, e2, Vu2 = fd1d(2.0, 2000, lambda q: np.where(q < 1, 1.0, 2.0), 0.0, 1.0)
s2 = -2.0 / (-e0 * e2[0] * (Vu2[1] - Vu2[0]) / (z2[1] - z2[0]))
Ve = s2 * Vu2
Ee = -np.diff(Ve) / (z2[1] - z2[0])
exam91 = {"D": -2.0, "E1": Ee[500], "E2": Ee[1500], "P2": e0 * 2 * Ee[1500] - e0 * Ee[1500], "V1": Ve[1000], "V2": Ve[2000]}
prac91 = {"D": Dz[mid[0]], "E1": Ez[mid[0]], "E2": Ez[mid[1]], "P2": Pz[mid[1]], "V1": V[iz[0]], "V2": V[iz[1]]}
common = [f for f in exam91 if np.isclose(prac91[f], exam91[f], rtol=1e-6)]
print("      S20 HE2 #1a key: " + ", ".join(f"{f}={v:.4g}" for f, v in exam91.items()))
chk_true(f"9.1 no answer (same quantity) carries over from Summer 2020 HE2 #1a (common: {common or 'none'})", not common)

# ---------------------------------------------------------------------------------------------
print("== 9.2 side-by-side dielectrics: 2-D finite-volume Laplace, no-flux side walls ==")
d, V0 = 2e-3, 10.0
nx, nz, Lx = 40, 20, 4e-3
hx, hz = 2 * Lx / nx, d / nz
xc = -Lx + (np.arange(nx) + 0.5) * hx                     # x = 0 is a cell face
er = np.where(xc < 0, 2.0, 5.0)
idx = lambda i, k: i * (nz + 1) + k
rows, cols, vals = [], [], []
rhs = np.zeros(nx * (nz + 1))
for i in range(nx):
    for k in range(nz + 1):
        p = idx(i, k)
        if k in (0, nz):
            rows.append(p); cols.append(p); vals.append(1.0)
            rhs[p] = 0.0 if k == 0 else V0
            continue
        diag = 0.0
        for kk in (k - 1, k + 1):
            c = er[i] / hz**2
            rows.append(p); cols.append(idx(i, kk)); vals.append(c); diag -= c
        for ii in (i - 1, i + 1):
            if 0 <= ii < nx:
                c = (2 * er[i] * er[ii] / (er[i] + er[ii])) / hx**2
                rows.append(p); cols.append(idx(ii, k)); vals.append(c); diag -= c
        rows.append(p); cols.append(p); vals.append(diag)
A2 = sparse.csr_matrix((vals, (rows, cols)), shape=(nx * (nz + 1),) * 2)
V2 = spsolve(A2, rhs).reshape(nx, nz + 1)
Ez2 = -np.diff(V2, axis=1) / hz                          # (nx, nz)
Ex2 = -np.diff(V2, axis=0) / hx
chk("9.2 E_z uniform in both halves (min,max) [V/m]", [Ez2.min(), Ez2.max()], [-5000, -5000], rtol=1e-8)
chk_true("9.2 E_x = 0 everywhere (field parallel to the interface)", np.abs(Ex2).max() < 1e-6)
DL, DR = e0 * 2 * Ez2[nx // 4, -1], e0 * 5 * Ez2[3 * nx // 4, -1]
chk("9.2 D_z x<0, x>0 [eps0 units]", [DL / e0, DR / e0], [-1e4, -2.5e4])
chk("9.2 D_z x<0, x>0 [nC/m^2]", [DL * 1e9, DR * 1e9], [-88.5, -221], rtol=R3)
chk("9.2 top-plate rho_s = -z.D above each half [nC/m^2]", [-DL * 1e9, -DR * 1e9], [88.5, 221], rtol=R3)
PL, PR = DL - e0 * Ez2[nx // 4, -1], DR - e0 * Ez2[3 * nx // 4, -1]
chk("9.2 P_z x<0, x>0 [eps0 units]", [PL / e0, PR / e0], [-5000, -2e4])
chk("9.2 P_z x<0, x>0 [nC/m^2]", [PL * 1e9, PR * 1e9], [-44.3, -177], rtol=R3)
chk("9.2 free+bound at top = eps0|E| in both halves [nC/m^2]", [(-DL + PL) * 1e9, (-DR + PR) * 1e9], [44.3, 44.3], rtol=R3)

# ---------------------------------------------------------------------------------------------
print("== 9.3 MC: graded example eps = 4 eps0/(4-z), D_z = 2 eps0 (finite differences) ==")
zg = np.linspace(0, 2, 4001)
epsg = 4 / (4 - zg)                                      # eps / eps0
Ezg = 2.0 / epsg
Vg = -integrate.cumulative_trapezoid(Ezg, zg, initial=0)
dV = np.gradient(Vg, zg)
lap = np.gradient(dV, zg)
divE = np.gradient(Ezg, zg)
divP = np.gradient(2.0 - Ezg, zg)                        # P_z/eps0 = D_z/eps0 - E_z
divD = np.gradient(epsg * dV, zg)
sl = slice(100, -100)
chk("9.3 (c) div(eps grad V) = 0 [eps0 V/m^2]", np.abs(divD[sl]).max(), 0, atol=1e-6)
chk("9.3 (a) lap V = +1/2 V/m^2 (not 0)", lap[sl].mean(), 0.5, rtol=1e-6)
chk("9.3 (b) div E = -1/2 V/m^2, rho_b = -eps0/2 (eps0 units)", divE[sl].mean(), -0.5, rtol=1e-6)
chk("9.3 (d) div P = +eps0/2 (eps0 units)", divP[sl].mean(), 0.5, rtol=1e-6)
lap_epsV = np.gradient(np.gradient(epsg * Vg, zg), zg)
exam_opts_fail = (np.abs(dV[sl]).min() > 0.1) and (abs(divE[sl].mean()) > 0.1) and \
                 (abs(lap[sl].mean()) > 0.1) and (np.abs(lap_epsV[sl]).max() > 0.1)
chk_true("9.3 SP18 E1 #1(i) options (grad V, div E, lap V, lap(eps V)) all fail -> exam key 'none'; page key is (c), so the exam key does not carry over", exam_opts_fail)

# ---------------------------------------------------------------------------------------------
print("== 9.4 MC: refraction at an air/glass face (eps_r = 4), 45 deg incidence ==")
nhat = np.array([0, 0, 1.0])
E1 = np.array([np.sin(pi / 4), 0, np.cos(pi / 4)])       # E0 = 1, medium 1 = air
E2 = np.array([E1[0], 0, E1[2] / 4])
chk("9.4 n x (E1 - E2) = 0 and n.(D1 - D2) = 0", list(np.cross(nhat, E1 - E2)) + [nhat @ (E1 - 4 * E2)], [0, 0, 0, 0], atol=1e-15)
th2 = np.degrees(np.arctan2(E2[0], E2[2]))
chk("9.4 theta_2 [deg]", th2, 76.0, rtol=R3)
chk("9.4 |E2| / E0", np.linalg.norm(E2), 0.729, rtol=R3)
chk("9.4 |D2| / (eps0 E0)", np.linalg.norm(4 * E2), 2.92, rtol=R3)
chk_true("9.4 key (b): bends away (theta_2 > 45) and |E2| < E0; (c) false; (e) false (|D2| > |D1|)",
         th2 > 45 and np.linalg.norm(E2) < 1 and np.linalg.norm(4 * E2) > 1)
chk_true("9.4 (d) E0/4 violates tangential continuity", abs(E1[0] / 4 - E1[0]) > 0.1)
chk("9.4 tan(th1)/tan(th2) = eps1/eps2", np.tan(pi / 4) / np.tan(np.radians(th2)), 0.25)

# ---------------------------------------------------------------------------------------------
print("== 9.5 coated wire: self-consistent bound charge + direct 2-D Coulomb integrals ==")
a, b, rl, chi = 1e-3, 2e-3, 10e-9, 1.5
dl = 1e-3     # evaluate at r = R(1 -/+ dl) and scale by r/R: every sheet's field is 0 inside and ~1/r outside
k_a = ring_Er(a * (1 + dl), a, 1.0) * (1 + dl)           # field at a+ per C/m on the sheet r = a
# bound at a: beta_a = -2 pi a P(a+) = -2 pi a eps0 chi E(a+), E(a+) from the sheets at a (free + beta_a)
c_a = 2 * pi * a * e0 * chi * k_a
beta_a = -c_a * rl / (1 + c_a)
E_bm_inner = ring_Er(b * (1 - dl), a, rl + beta_a) * (b * (1 - dl) / b)
k_bself = ring_Er(b * (1 - dl), b, 1.0)                  # sheet at b seen from just inside (~0)
c_b = 2 * pi * b * e0 * chi
beta_b = c_b * E_bm_inner / (1 - c_b * k_bself)
E_bm = E_bm_inner + ring_Er(b * (1 - dl), b, beta_b)
E_bp = (ring_Er(b * (1 + dl), a, rl + beta_a) + ring_Er(b * (1 + dl), b, beta_b)) * (1 + dl)
print(f"      self-consistent bound charges: beta_a = {beta_a:.4g} C/m (= -0.6 rho_l), beta_b = {beta_b:.4g} C/m")
chk("9.5 D(b) = rho_l/(2 pi b) [uC/m^2]", (e0 * E_bp) * 1e6, 0.796, rtol=R3)
chk("9.5 E(b-) [kV/m] (also the student's number)", E_bm / 1e3, 36.0, rtol=R3)
chk("9.5 E(b+) [kV/m]", E_bp / 1e3, 89.9, rtol=R3)
chk("9.5 rho_sb(b) [uC/m^2]", beta_b / (2 * pi * b) * 1e6, 0.477, rtol=R3)
chk("9.5 eps0 (E(b+) - E(b-)) = rho_sb(b)", e0 * (E_bp - E_bm), beta_b / (2 * pi * b), rtol=1e-4)
chk_true("9.5 both fields along +r", E_bm > 0 and E_bp > 0)

# ---------------------------------------------------------------------------------------------
print("== 9.6 graded dielectric eps_r = (1+z)^2 at fixed voltage: FD solve ==")
N6 = 20000
z6, zh6, e6, V6 = fd1d(1.0, N6, lambda q: (1 + q) ** 2, 6.0, 0.0)
h6 = z6[1] - z6[0]
D6 = -e6 * np.diff(V6) / h6                              # D_z / eps0 at half points
chk("9.6 D_z constant across the gap (max-min) [eps0]", D6.max() - D6.min(), 0, atol=1e-6)
Dz6 = D6.mean()
chk("9.6 D_z [eps0 C/m^2]", Dz6, 12, rtol=1e-7)
chk("9.6 D_z numeric ~ 1.06e-10 C/m^2", Dz6 * e0, 1.06e-10, rtol=R3)
chk("9.6 plate rho_s bottom (+z.D), top (-z.D) [eps0]", [Dz6, -Dz6], [12, -12], rtol=1e-7)
E6 = lambda q: Dz6 / (1 + q) ** 2
chk("9.6 E_z(0), E_z(1) [V/m]", [E6(0), E6(1)], [12, 3], rtol=1e-7)
chk("9.6 V(0.5) [V]", V6[N6 // 2], 2, rtol=1e-7)
zz = np.array([0.2, 0.7])
chk("9.6 V(z) = 6 - 12z/(1+z) at z = 0.2, 0.7", np.interp(zz, z6, V6), 6 - 12 * zz / (1 + zz), rtol=1e-7)
P6 = lambda q: Dz6 - E6(q)                               # P_z / eps0
zf = np.linspace(0, 1, 10001)
rhob6 = -np.gradient(P6(zf), zf)
chk("9.6 P_z(0), P_z(1) [eps0]", [P6(0), P6(1)], [0, 9], atol=1e-6)
chk("9.6 rho_b(0), rho_b(1) [eps0 C/m^3]", [rhob6[0], rhob6[-1]], [-24, -3], rtol=1e-3)
chk("9.6 rho_b(z) = -24/(1+z)^3 at z = 0.5", np.interp(0.5, zf, rhob6), -24 / 1.5**3, rtol=1e-6)
bulk6 = integrate.trapezoid(rhob6, zf)
chk("9.6 faces top +P(1), bottom -P(0); bulk; total [eps0]", [P6(1), -P6(0), bulk6, P6(1) - P6(0) + bulk6], [9, 0, -9, 0], atol=1e-5)
zq = np.array([0.3, 0.7])
tot_below = Dz6 + 0.0 + np.array([integrate.quad(lambda q: np.interp(q, zf, rhob6), 0, x)[0] for x in zq])
chk("9.6 Gauss with all charge: eps0 E_z(z) = free + bound below z", tot_below, E6(zq), rtol=1e-5)

# ---------------------------------------------------------------------------------------------
print("== 9.7 sheet on a dielectric interface between grounded plates: FD with a sheet source ==")
er97 = lambda q: np.where(q < 1, 2.0, 1.0)
z7, zh7, e7, V7 = fd1d(3.0, 3000, er97, 0.0, 0.0, sheets=[(1.0, 10.0)])
h7 = z7[1] - z7[0]
E7 = -np.diff(V7) / h7
D7 = e7 * E7
chk("9.7 V(1) [V]", V7[1000], 4)
chk("9.7 below: E_z [V/m], D_z [eps0]", [E7[500], D7[500]], [-4, -8])
chk("9.7 above: E_z [V/m], D_z [eps0]", [E7[2000], D7[2000]], [2, 2])
chk("9.7 plate rho_s bottom, top [eps0]", [D7[0], -D7[-1]], [-8, -2])
chk("9.7 bottom plate share of -rho_s", D7[0] / -10, 0.8)
P7 = D7[500] - E7[500]
chk("9.7 P_z in dielectric; rho_sb top face (+z), bottom face (-z) [eps0]", [P7, P7, -P7], [-4, -4, 4])
chk("9.7 jump of eps0 E_z at z=1 = free + bound there [eps0]", [E7[2000] - E7[500], 10 + P7], [6, 6])
def E_above(Vt):
    zz7, _, ee7, VV = fd1d(3.0, 3000, er97, 0.0, Vt, sheets=[(1.0, 10.0)])
    return -(VV[-1] - VV[-2]) / (zz7[1] - zz7[0])
Vt = optimize.brentq(E_above, 0.0, 20.0, xtol=1e-14)
_, _, e7d, V7d = fd1d(3.0, 3000, er97, 0.0, Vt, sheets=[(1.0, 10.0)])
E7d = -np.diff(V7d) / h7
chk("9.7 (d) top-plate potential V(3) [V]", Vt, 5)
chk("9.7 (d) V(1), E_z below [V, V/m]", [V7d[1000], E7d[500]], [5, -5])
chk("9.7 (d) plate charges bottom, top [eps0]", [e7d[0] * E7d[0], -e7d[-1] * E7d[-1]], [-10, 0], atol=1e-9)
chk("9.7 watch-out: eps0-only jump gives V0 = 20/3", optimize.brentq(lambda v: v / 2 + v - 10, 0, 20), 20 / 3)

# ---------------------------------------------------------------------------------------------
print("== 9.8 dielectric rod with charged surface: self-consistent solve with 2-D Coulomb rings ==")
Rr, chi8 = 2.0, 3.0
dl8 = 1e-3    # evaluate at 2(1 -/+ dl8), scale by r/2 (every contribution is 0 or ~1/r on each side)
kin = ring_Er(Rr * (1 - dl8), 0.0, 1.0) * (1 - dl8)      # axis line seen at 2-
kout = ring_Er(Rr * (1 + dl8), 0.0, 1.0) * (1 + dl8)
sin_ = ring_Er(Rr * (1 - dl8), Rr, 1.0) * (1 - dl8)      # surface sheet seen at 2- (~0)
sout = ring_Er(Rr * (1 + dl8), Rr, 1.0) * (1 + dl8)
# unknowns x = [rho_l, rho_s, beta0 (axis bound, C/m), beta2 (surface bound, C/m)]
M = np.array([[kin, 2 * pi * Rr * sin_, kin, sin_],          # E(2-) = 3
              [kout, 2 * pi * Rr * sout, kout, sout],         # E(2+) = 8
              [chi8, 0, 1 + chi8, 0],                         # beta0 = -chi (rho_l + beta0)
              [0, 0, 0, 1]])                                  # beta2 = 2 pi R eps0 chi E(2-)
rhs8 = np.array([3.0, 8.0, 0.0, 2 * pi * Rr * e0 * chi8 * 3.0])
rl8, rs8, b0, b2 = np.linalg.solve(M, rhs8)
chk("9.8 rho_s [eps0 C/m^2], numeric", [rs8 / e0, rs8], [-4, -3.54e-11], rtol=R3)
chk("9.8 rho_s exact", rs8 / e0, -4, rtol=1e-6)
chk("9.8 rho_l [pi eps0 C/m], numeric", [rl8 / (pi * e0), rl8], [48, 1.34e-9], rtol=R3)
chk("9.8 rho_l exact", rl8 / (pi * e0), 48, rtol=1e-6)
chk("9.8 surface bound rho_sb [eps0], per metre [pi eps0]", [b2 / (2 * pi * Rr) / e0, b2 / (pi * e0)], [9, 36], rtol=1e-6)
chk("9.8 axis bound line [pi eps0 C/m], total bound", [b0 / (pi * e0), (b0 + b2) / (pi * e0)], [-36, 0], rtol=1e-6, atol=1e-6)
E8 = lambda r: ring_Er(r, 0.0, rl8 + b0) + ring_Er(r, Rr, 2 * pi * Rr * rs8 + b2)
chk("9.8 E inside = 6/r at r = 1, 1.5", [E8(1.0), E8(1.5)], [6, 4], rtol=1e-6)
chk("9.8 E outside = 16/r at r = 3, 4", [E8(3.0), E8(4.0)], [16 / 3, 4], rtol=1e-6)
chk("9.8 P inside = 18 eps0/r at r = 1", e0 * chi8 * E8(1.0) / e0, 18, rtol=1e-6)
chk("9.8 free + bound at surface = eps0 (8 - 3) [eps0]", (rs8 + b2 / (2 * pi * Rr)) / e0, 5, rtol=1e-6)
gx, gw = np.polynomial.legendre.leggauss(40)
def gl(f, lo, hi):
    xs = 0.5 * (hi - lo) * gx + 0.5 * (hi + lo)
    return 0.5 * (hi - lo) * sum(w * f(x) for x, w in zip(xs, gw))
dV8 = gl(E8, 1.0, 2.0) + gl(E8, 2.0, 4.0)
chk("9.8 V(1) - V(4) [V] = 22 ln 2", [dV8, dV8], [22 * np.log(2), 15.2], rtol=R3)
chk("9.8 V(1) - V(4) exact", dV8, 22 * np.log(2), rtol=1e-6)
chk_true("9.8 differs from SP18 E1 #4 key (rho_s = eps0*4 - 5 eps0*2 = -6 eps0; radius 3 m)", not np.isclose(rs8 / e0, 4 - 10))

# ---------------------------------------------------------------------------------------------
print("== 9.9 glass slab (eps_r = 3, 0 < z < 3 cm) in an oblique field ==")
E0v = np.array([40.0, 0, 30.0])
Ein = np.array([E0v[0], 0, E0v[2] / 3])
Eab = np.array([Ein[0], 0, 3 * Ein[2]])
chk("9.9 BCs at z=0: n x (E_in - E0) = 0, n.(3 E_in - E0) = 0", list(np.cross(nhat, Ein - E0v)) + [nhat @ (3 * Ein - E0v)], [0, 0, 0, 0], atol=1e-12)
chk("9.9 E inside [V/m]", Ein, [40, 0, 10])
chk("9.9 D, P inside [eps0 C/m^2]", list(3 * Ein) + list(2 * Ein), [120, 0, 30, 80, 0, 20])
chk("9.9 D numeric (x, z) [1e-9 C/m^2]", [3 * Ein[0] * e0 * 1e9, 3 * Ein[2] * e0 * 1e9], [1.06, 0.266], rtol=R3)
chk("9.9 P numeric (x, z) [1e-10 C/m^2]", [2 * Ein[0] * e0 * 1e10, 2 * Ein[2] * e0 * 1e10], [7.08, 1.77], rtol=R3)
t1, t2 = np.degrees(np.arctan2(E0v[0], E0v[2])), np.degrees(np.arctan2(Ein[0], Ein[2]))
chk("9.9 angles from normal: air, glass [deg]", [t1, t2], [53.1, 76.0], rtol=R3)
chk("9.9 tan ratio", np.tan(np.radians(t1)) / np.tan(np.radians(t2)), 1 / 3)
chk("9.9 E above the slab = E0 [V/m]", Eab, [40, 0, 30])
P9 = 2 * e0 * Ein
sb_top, sb_bot = P9 @ nhat, P9 @ (-nhat)
chk("9.9 rho_sb top, bottom [eps0]; top numeric", [sb_top / e0, sb_bot / e0, sb_top], [20, -20, 1.77e-10], rtol=R3)
sheetE = lambda zp: sum(sig / (2 * e0) * np.sign(zp - zs) for zs, sig in ((0.03, sb_top), (0.0, sb_bot)))
chk("9.9 field of the two bound sheets at z = -1, 1.5, 4 cm [V/m]", [sheetE(-0.01), sheetE(0.015), sheetE(0.04)], [0, -20, 0], atol=1e-9)
def Efield(p):
    return E0v if p[2] < 0 else (Ein if p[2] < 0.03 else Eab)
ev = lambda t, p: p[2] - 0.03
ev.terminal = True
sol = integrate.solve_ivp(lambda t, p: Efield(p) / np.linalg.norm(Efield(p)), [0, 1], [0, 0, 1e-12],
                          events=ev, rtol=1e-12, atol=1e-14)
B = sol.y_events[0][0]
chk("9.9 exit point B [m]", B, [0.12, 0, 0.03], rtol=1e-6, atol=1e-9)
VBA = -integrate.quad(lambda t: Ein @ (B - 0), 0, 1)[0]
leg1 = -integrate.quad(lambda zq: Ein[2], 0, 0.03)[0]
leg2 = -integrate.quad(lambda xq: Ein[0], 0, B[0])[0]
chk("9.9 V(B)-V(A); path 2 legs; |E| x length [V]", [VBA, leg1, leg2, leg1 + leg2, np.linalg.norm(Ein) * np.linalg.norm(B)],
    [-5.1, -0.3, -4.8, -5.1, 5.1], rtol=1e-9)
chk("9.9 without slab: x at z = 3 cm; sideways drag [cm]", [0.03 * E0v[0] / E0v[2] * 100, (B[0] - 0.03 * E0v[0] / E0v[2]) * 100], [4, 8])

# ---------------------------------------------------------------------------------------------
print("== 9.10 sphere, shell, two layers (NEW: core +5 C, eps_r 5; shell -6 C; coating eps_r 2) ==")
q, k1, Qsh, k2 = 5.0, 5.0, -6.0, 2.0
c1, c2 = k1 - 1, k2 - 1                                  # susceptibilities
# unknowns [b1, b2, s2, b3, b4]: bound at r=1,2,3,4 (C) and free charge on the shell's inner surface
# self-consistent: bound face charge = -/+ 4 pi r^2 eps0 chi E(face), E from all enclosed charge
Mx = np.array([[1 + c1, 0, 0, 0, 0],                     # b1 = -c1 (q + b1)
               [-c1, 1, 0, 0, 0],                        # b2 = +c1 (q + b1)
               [1, 1, 1, 0, 0],                          # E = 0 in the shell metal: q+b1+b2+s2 = 0
               [c2, c2, 0, 1 + c2, 0],                   # b3 = -c2 (q+b1+b2+Qsh+b3)
               [-c2, -c2, 0, -c2, 1]])                   # b4 = +c2 (q+b1+b2+Qsh+b3)
rhsx = np.array([-c1 * q, c1 * q, -q, -c2 * (q + Qsh), c2 * (q + Qsh)])
b1, b2_, s2_, b3, b4 = np.linalg.solve(Mx, rhsx)
s3_ = Qsh - s2_
shells = [(1.0, q + b1), (2.0, b2_ + s2_), (3.0, s3_ + b3), (4.0, b4)]   # total charge per radius
Etot = lambda r: sum(Qi for Ri, Qi in shells if Ri < r) / (4 * pi * e0 * r * r)
Vsup = lambda r: sum(Qi / (4 * pi * e0 * max(r, Ri)) for Ri, Qi in shells)
epsr10 = lambda r: k1 if 1 < r < 2 else (k2 if 3 < r < 4 else 1.0)
metal = lambda r: r < 1 or 2 < r < 3
def fields(r):
    E = 0.0 if metal(r) else Etot(r)
    P = 0.0 if metal(r) else e0 * (epsr10(r) - 1) * E
    return e0 * E + P, E, P
chk_true("9.10 E = 0 inside both metals from the all-charge sum (r = 0.5, 2.5)", abs(Etot(0.5)) < 1e-30 and abs(Etot(2.5)) < 1e-6)
for r, Dc, Ec, Pc in [(1.5, 5 / (4 * pi), 1 / (4 * pi), 1 / pi), (3.5, -1 / (4 * pi), -1 / (8 * pi), -1 / (8 * pi)),
                      (5.0, -1 / (4 * pi), -1 / (4 * pi), 0.0)]:
    D_, E_, P_ = fields(r)
    chk(f"9.10 (a) r={r}: r^2 D, eps0 r^2 E, r^2 P", [D_ * r * r, E_ * e0 * r * r, P_ * r * r], [Dc, Ec, Pc], rtol=1e-12, atol=1e-15)
chk("9.10 (a) D = Q_free_enc/(4 pi r^2) at r = 1.5, 3.5, 5 (Gauss for free charge)",
    [fields(r)[0] for r in (1.5, 3.5, 5.0)], [q / (4 * pi * 2.25), (q + Qsh) / (4 * pi * 12.25), (q + Qsh) / (4 * pi * 25)], rtol=1e-12)
chk("9.10 (b) free charge at r = 1, 2, 3, 4 [C]", [q, s2_, s3_, 0.0], [5, -5, -1, 0], atol=1e-12)
rs_free = [q / (4 * pi), s2_ / (16 * pi), s3_ / (36 * pi), 0.0]
chk("9.10 (b) rho_s exact [C/m^2]", rs_free, [5 / (4 * pi), -5 / (16 * pi), -1 / (36 * pi), 0], rtol=1e-12, atol=1e-15)
chk("9.10 (b) rho_s numeric [C/m^2]", rs_free[:3], [0.398, -0.0995, -0.00884], rtol=R3)
rs_b = [b1 / (4 * pi), b2_ / (16 * pi), b3 / (36 * pi), b4 / (64 * pi)]
chk("9.10 (c) bound totals at r = 1, 2, 3, 4 [C]", [b1, b2_, b3, b4], [-4, 4, 0.5, -0.5], rtol=1e-12)
chk("9.10 (c) rho_sb exact [C/m^2]", rs_b, [-1 / pi, 1 / (4 * pi), 1 / (72 * pi), -1 / (128 * pi)], rtol=1e-12)
chk("9.10 (c) rho_sb numeric [C/m^2]", rs_b, [-0.318, 0.0796, 0.00442, -0.00249], rtol=R3)
chk("9.10 (c) rho_sb from P.n with the table's P: -P(1), +P(2), -P(3), +P(4)",
    [-fields(1 + 1e-12)[2], fields(2 - 1e-12)[2], -fields(3 + 1e-12)[2], fields(4 - 1e-12)[2]], rs_b, rtol=1e-9)
chk("9.10 (c) face totals -/+(1 - 1/eps_r) Q_enc", [b1, b4], [-(1 - 1 / k1) * q, (1 - 1 / k2) * (q + Qsh)], rtol=1e-12)
r_ = np.linspace(1.1, 1.9, 9); r2P = [fields(x)[2] * x * x for x in r_]
chk_true("9.10 (c) r^2 P_r constant in each layer -> rho_b = 0", np.ptp(r2P) < 1e-14 and np.ptp([fields(x)[2] * x * x for x in np.linspace(3.1, 3.9, 9)]) < 1e-14)
Vsh_sup, V0_sup = Vsup(2.5), Vsup(0.0)
Vsh_int = integrate.quad(lambda r: fields(r)[1], 3, 4)[0] + integrate.quad(lambda r: fields(r)[1], 4, np.inf)[0]
V0_int = Vsh_int + integrate.quad(lambda r: fields(r)[1], 1, 2)[0]
chk("9.10 (d) V_shell: shell superposition vs line integral, exact -7/(96 pi eps0)", [Vsh_sup, Vsh_int], [-7 / (96 * pi * e0)] * 2, rtol=1e-9)
chk("9.10 (d) V(0): shell superposition vs line integral, exact 5/(96 pi eps0)", [V0_sup, V0_int], [5 / (96 * pi * e0)] * 2, rtol=1e-9)
chk("9.10 (d) numeric V_shell, V(0), V(0)-V_shell [V]", [Vsh_sup, V0_sup, V0_sup - Vsh_sup], [-2.62e9, 1.87e9, 4.49e9], rtol=R3)
chk("9.10 (d) V(0) - V_shell = 1/(8 pi eps0)", V0_sup - Vsh_sup, 1 / (8 * pi * e0), rtol=1e-12)
chk_true("9.10 (d) the core is at the higher potential", V0_sup > Vsh_sup)
chk("9.10 check: eps0[E(4+) - E(4-)] = rho_sb(4) = -1/(128 pi)", e0 * (fields(4 + 1e-9)[1] - fields(4 - 1e-9)[1]), -1 / (128 * pi), rtol=1e-6)
chk("9.10 check terms: eps0 E(4+) = -1/(64 pi), -eps0 E(4-) = +1/(128 pi)",
    [e0 * fields(4 + 1e-12)[1], -e0 * fields(4 - 1e-12)[1]], [-1 / (64 * pi), 1 / (128 * pi)], rtol=1e-9)
# non-coincidence with the catalogue keys of the #3a family (radii 1, 2, 3 m; free space r > 3 m)
def key(Qc, epsr, Qshell):
    Qo = Qc + Qshell
    return {"inD": Qc / (4 * pi), "inE": Qc / (4 * pi * epsr), "inP": (1 - 1 / epsr) * Qc / (4 * pi),
            "rs1": Qc / (4 * pi), "rs2": -Qc / (16 * pi), "rs3": Qo / (36 * pi), "outD": Qo / (4 * pi), "outE": Qo / (4 * pi)}
exams = {"S18 HE1 #3a": key(4, 2, 0), "S19 HE1 #3a": key(-4, 3, 0), "S19c HE1 #3a": key(2, 4, 2)}
new = {"inD": 5 / (4 * pi), "inE": 1 / (4 * pi), "inP": 1 / pi, "rs1": 5 / (4 * pi), "rs2": -5 / (16 * pi),
       "rs3": -1 / (36 * pi), "outD": -1 / (4 * pi), "outE": -1 / (4 * pi)}          # outE: air r > 4
new_coatE = -1 / (8 * pi)
old = key(2, 4, -6)
for nm, kk in exams.items():
    hits_new = [f for f in new if np.isclose(new[f], kk[f], rtol=1e-9)] + (["coatE"] if np.isclose(new_coatE, kk["outE"]) else [])
    hits_old = [f for f in old if np.isclose(old[f], kk[f], rtol=1e-9)]
    print(f"      {nm}: old 9.10 (+2 C, 4 eps0) coincided in {hits_old or 'nothing'}")
    chk_true(f"9.10 new numbers coincide with no {nm} key value ({hits_new or 'none'})", not hits_new)

# ---------------------------------------------------------------------------------------------
print("== 9.11 graded coax eps = eps_a a/r ==")
def coax(a_, b_, ea, V0_):
    lam = V0_ / integrate.quad(lambda r: 1 / (2 * pi * (ea * a_ / r) * r), a_, b_)[0]
    E = lambda r: lam / (2 * pi * (ea * a_ / r) * r)
    return lam, E
for a_, b_, ea, V0_ in [(1e-3, 3e-3, 6 * e0, 200.0), (2e-3, 7e-3, 3 * e0, 50.0)]:
    lam, E = coax(a_, b_, ea, V0_)
    rr = np.linspace(a_, b_, 7)
    chk(f"9.11 (a) E independent of r and = V0/(b-a) (a={a_}, b={b_})", [E(x) for x in rr], [V0_ / (b_ - a_)] * 7, rtol=1e-9)
a, b = 1e-3, 3e-3
lam, E = coax(a, b, 6 * e0, 200.0)
Ec = E(2e-3)
chk("9.11 (b) E [V/m], rho_l [C/m], rho_l [nC/m]", [Ec, lam, lam * 1e9], [1.0e5, 3.34e-8, 33.4], rtol=R3)
chk("9.11 (b) D(r) r = const [C/m]; D(a), D(b) [uC/m^2]", [lam / (2 * pi), lam / (2 * pi * a) * 1e6, lam / (2 * pi * b) * 1e6], [5.31e-9, 5.31, 1.77], rtol=R3)
Pr = lambda r: lam / (2 * pi * r) - e0 * E(r)
chk("9.11 (c) P(a), P(b) [uC/m^2]", [Pr(a) * 1e6, Pr(b) * 1e6], [4.43, 0.885], rtol=R3)
rg = np.linspace(a, b, 20001)
rhob = -np.gradient(rg * np.array([Pr(x) for x in rg]), rg) / rg
chk("9.11 (c) rho_b(a), rho_b(b) [mC/m^3]", [rhob[0] * 1e3, rhob[-1] * 1e3], [0.885, 0.295], rtol=R3)
chk("9.11 (c) rho_b = eps0 E / r at mid", np.interp(2e-3, rg, rhob), e0 * Ec / 2e-3, rtol=1e-6)
chk("9.11 (c) rho_sb(a) = -P(a), rho_sb(b) = +P(b) [uC/m^2]", [-Pr(a) * 1e6, Pr(b) * 1e6], [-4.43, 0.885], rtol=R3)
inner, outer = -Pr(a) * 2 * pi * a, Pr(b) * 2 * pi * b
bulk = integrate.trapezoid(rhob * 2 * pi * rg, rg)
chk("9.11 (c) per length: inner, outer, bulk [nC/m]", [inner * 1e9, outer * 1e9, bulk * 1e9], [-27.8, 16.7, 11.1], rtol=R3)
chk("9.11 (c) fractions of rho_l and total", [inner / lam, outer / lam, bulk / lam, (inner + outer + bulk) / lam], [-5 / 6, 1 / 2, 1 / 3, 0], rtol=1e-6, atol=1e-9)
lam_h = 200.0 / integrate.quad(lambda r: 1 / (2 * pi * 4 * e0 * r), a, b)[0]
Emax_h = lam_h / (2 * pi * 4 * e0 * a)
chk("9.11 (d) homogeneous E_max [V/m]; ratio to graded (= 2/ln 3)", [Emax_h, Emax_h / Ec, 2 / np.log(3)], [1.82e5, 1.82, 1.82], rtol=R3)
chk("9.11 check: Gauss with all charge at r = 2 mm equals 2 pi eps0 E r", lam + inner + integrate.quad(lambda r: e0 * Ec / r * 2 * pi * r, a, 2e-3)[0],
    2 * pi * e0 * Ec * 2e-3, rtol=1e-9)

# ---------------------------------------------------------------------------------------------
print("== 9.12 sphere half in oil: numerical flux and surface integrals ==")
def sphere_oil(Q, a_, er_):
    epsth = lambda th: e0 if th < pi / 2 else er_ * e0
    flux1 = integrate.dblquad(lambda ph, th: epsth(th) * 1.0 / 0.3**2 * 0.3**2 * np.sin(th), 0, pi, 0, 2 * pi,
                              epsabs=1e-20)[0]
    return Q / flux1                                     # A from Gauss's law for D (flux linear in A)
for er_ in (2.0, 5.0):
    A_ = sphere_oil(30e-9, 0.1, er_)
    chk(f"9.12 (a) A = Q/(2 pi (eps0 + eps)) for eps_r = {er_}", A_, 30e-9 / (2 * pi * (e0 + er_ * e0)), rtol=1e-9)
Q, a = 30e-9, 0.1
A_ = sphere_oil(Q, a, 2.0)
chk("9.12 (a) A [V m], E(a) [V/m]", [A_, A_ / a**2], [180, 1.80e4], rtol=R3)
chk("9.12 (a) A = Q/(6 pi eps0)", A_, Q / (6 * pi * e0), rtol=1e-9)
# boundary conditions on the oil surface z = 0 (r > a): E radial lies in the plane
for ph in (0.3, 2.0):
    p = np.array([0.25 * np.cos(ph), 0.25 * np.sin(ph), 0.0]); Ev = A_ * p / np.linalg.norm(p) ** 3
    chk_true(f"9.12 (a) on z=0 at phi={ph}: E tangential (E_z = 0) so D_z = 0 both sides; E_t equal", abs(Ev[2]) < 1e-15)
up = integrate.dblquad(lambda ph, th: e0 * A_ / a**2 * a**2 * np.sin(th), 0, pi / 2, 0, 2 * pi)[0]
lo = integrate.dblquad(lambda ph, th: 2 * e0 * A_ / a**2 * a**2 * np.sin(th), pi / 2, pi, 0, 2 * pi)[0]
chk("9.12 (b) rho_s upper, lower [nC/m^2]", [e0 * A_ / a**2 * 1e9, 2 * e0 * A_ / a**2 * 1e9], [159, 318], rtol=R3)
chk("9.12 (b) charge upper, lower hemisphere [nC]", [up * 1e9, lo * 1e9], [10, 20], rtol=1e-9)
Pa = e0 * A_ / a**2
chk("9.12 (c) rho_sb at sphere [nC/m^2], total [nC]", [-Pa * 1e9, -Pa * 2 * pi * a**2 * 1e9], [-159, -10], rtol=R3)
chk("9.12 (c) net surface charge lower = upper [nC/m^2]", [(2 * e0 * A_ / a**2 - Pa) * 1e9, e0 * A_ / a**2 * 1e9], [159, 159], rtol=R3)
chk("9.12 (c) uniform 20 nC sphere in vacuum gives A", 20e-9 / (4 * pi * e0), A_, rtol=1e-9)
Va = integrate.quad(lambda r: A_ / r**2, a, np.inf)[0]
Vair = integrate.quad(lambda r: Q / (4 * pi * e0 * r**2), a, np.inf)[0]
Voil = integrate.quad(lambda r: Q / (4 * pi * 2 * e0 * r**2), a, np.inf)[0]
chk("9.12 (d) V(a), all air, all oil [kV]", [Va / 1e3, Vair / 1e3, Voil / 1e3], [1.80, 2.70, 1.35], rtol=R3)
chk("9.12 (d) V(a)/V_air = 2/3", Va / Vair, 2 / 3, rtol=1e-9)

# ---------------------------------------------------------------------------------------------
print("== Sources: Source lines vs the closing 'Sources for this page' paragraph ==")
txt = open(PAGE, encoding="utf-8").read()
srcs = re.findall(r"^### (9\.\d+) .*?\n.*?^> \*Source: (.*?)\*$", txt, flags=re.S | re.M)
para = txt.split("### Sources for this page", 1)[1]
want10 = ("Summer 2019 HE1 (conflict) #3a, re-parameterized (new charges and permittivities, outer dielectric "
          "coating added); same layout as Summer 2018 HE1 #3a and Summer 2019 HE1 #3a; FA26 HW4 #6 is the cylindrical analogue.")
chk_true("9.10 Source line is exactly the requested text", dict(srcs).get("9.10") == want10)
ids = set()
for num, s in srcs:
    for m in re.findall(r"(Summer 20\d\d HE\d(?: \(conflict\))? #\w+|SP18 Exam 1 #[\w()]+|HW\d #\d)", s):
        ids.add(m)
for m in sorted(ids):
    chk_true(f"Sources paragraph mentions '{m}'", m in para)
chk_true("Sources paragraph cites no HW/exam that no Source line cites (HW3 #7)", "HW3 #7" not in para)
orig = [n for n, s in srcs if s.strip().startswith("original")]
chk_true(f"Sources paragraph lists the original problems {orig}", all(n in para for n in orig))

print(f"\n{sum(results)} PASS, {len(results) - sum(results)} FAIL")
