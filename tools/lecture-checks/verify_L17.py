#!/usr/bin/env python3
"""Verification of every number, sign and direction used in the Lecture 17 pages
(3-maxwell-and-waves/17-..., concepts/magnetization, concepts/permeability,
problems/fields-across-a-magnetic-interface, the small additions to other concept pages)
and in the figures of figs_l17.py.

Every vector direction is fixed with an explicit np.cross.  Frames:
  page frame   : the coordinates named in the text (x, y, z as the problem states them)
  screen frame : x right, y up, z out of the screen (used for the figures)
Run:  python3 verify_L17.py > verify_L17.out
"""
import math
import numpy as np

RESULTS = []


def check(name, ok, detail=""):
    RESULTS.append((name, bool(ok)))
    print(("PASS " if ok else "FAIL ") + name + (("  —  " + detail) if detail else ""))


def close(a, b, rel=1e-9, abs_=1e-12):
    a = np.asarray(a, float); b = np.asarray(b, float)
    return np.allclose(a, b, rtol=rel, atol=abs_)


X, Y, Z = np.eye(3)
mu0 = 4e-7 * math.pi
eps0 = 8.8541878128e-12
e = 1.602176634e-19
me = 9.1093837015e-31
hbar = 1.054571817e-34
alpha = 7.2973525693e-3
c = 299792458.0
a0 = 5.29177210903e-11
kB = 1.380649e-23
NA = 6.02214076e23
muB = e * hbar / (2 * me)

print("=" * 78)
print("A. Atomic dipoles: m = IA, torque, M = N m")
print("=" * 78)
# A1 Bohr orbit: I and m
v = alpha * c
I_orb = e * v / (2 * math.pi * a0)
m_orb = I_orb * math.pi * a0 ** 2
print(f"   Bohr orbit: v = {v:.4e} m/s, I = e v/(2 pi a0) = {I_orb:.4e} A, m = I pi a0^2 = {m_orb:.4e} A m^2, muB = {muB:.4e}")
check("A1 Bohr-orbit current is about 1.05 mA", abs(I_orb - 1.054e-3) < 0.005e-3, f"{I_orb*1e3:.3f} mA")
check("A1 Bohr-orbit moment equals the Bohr magneton e*hbar/2m_e = 9.27e-24 A m^2", abs(m_orb / muB - 1) < 1e-6, f"{m_orb:.5e} vs {muB:.5e}")
check("A1 m = e v a/2 = I pi a^2", close(e * v * a0 / 2, m_orb))

# A2 orbit direction (page frame of the figure's left panel: x right, z up, viewer at -y;
# the near side of the orbit is y = -a).  Electron at r = -a y moving -x.
a = 1.0; vv = 1.0
r = -a * Y; vel = -vv * X
I_dir = -vel / np.linalg.norm(vel)               # conventional current opposite to the electron
# right-hand rule: for a loop around n, current direction at r is n x r_hat
n_up = Z
check("A2 near-side current +x with the loop normal +z (counter-clockwise seen from +z): z x (-y) = +x",
      close(np.cross(n_up, r / np.linalg.norm(r)), I_dir))
m_vec = (-e / 2) * np.cross(r, vel)              # m = (q/2) r x v with q = -e
L_vec = me * np.cross(r, vel)                    # orbital angular momentum
check("A2 m = (q/2) r x v points along +z (up)", m_vec[2] > 0 and abs(m_vec[0]) < 1e-30 and abs(m_vec[1]) < 1e-30)
check("A2 electron's m is antiparallel to its angular momentum L", np.dot(m_vec, L_vec) < 0 and close(np.cross(m_vec, L_vec), 0, abs_=1e-60))
check("A2 m = -(e/2m_e) L", close(m_vec, -(e / (2 * me)) * L_vec, rel=1e-12, abs_=1e-60))

# A3 torque on a tilted square loop in a uniform B (page frame), exact segment integration
def loop_forces(theta, ell=1.0, I=1.0, B=Z * 1.0):
    mhat = np.array([0.0, math.sin(theta), math.cos(theta)])
    u = np.array([0.0, math.cos(theta), -math.sin(theta)])       # in-plane, perpendicular to x
    assert close(np.cross(X, u), mhat)                             # x then u circulates around +mhat
    corners = [(-X - u) * ell / 2, (X - u) * ell / 2, (X + u) * ell / 2, (-X + u) * ell / 2]
    Ftot = np.zeros(3); Ttot = np.zeros(3)
    for k in range(4):
        p, q = corners[k], corners[(k + 1) % 4]
        dl = q - p
        F = I * np.cross(dl, B)                                    # uniform B: F = I L x B on a straight side
        mid = (p + q) / 2
        Ftot += F; Ttot += np.cross(mid, F)
    return mhat, Ftot, Ttot

for th_deg in (20, 35, 60, 120):
    th = math.radians(th_deg)
    mhat, F, T = loop_forces(th)
    m = 1.0 * 1.0 ** 2 * mhat
    check(f"A3 tilted loop theta={th_deg} deg: net force zero, torque = m x B", close(F, 0, abs_=1e-12) and close(T, np.cross(m, Z)),
          f"T = {np.round(T, 4)}, m x B = {np.round(np.cross(m, Z), 4)}")
    # rotation about T moves m toward B: d m/dt ∝ T x m has positive component along B
    check(f"A3 theta={th_deg} deg: the torque turns m toward B (d(m.B) > 0)", np.dot(np.cross(T, mhat), Z) > 0)

# A4 screen frame of figure mag-moment-torque, middle panel: B0 up (+y), m tilted right by theta
th = math.radians(35)
m_s = np.array([math.sin(th), math.cos(th), 0.0]); B_s = Y
P_R = 0.5 * np.array([math.cos(th), -math.sin(th), 0.0])      # lower-right end of the edge-on loop
P_L = -P_R                                                      # upper-left end
cur_R = np.cross(m_s, P_R / np.linalg.norm(P_R)); cur_L = np.cross(m_s, P_L / np.linalg.norm(P_L))
check("A4 [fig mag-moment-torque] lower-right end carries current INTO the screen (otimes): m x r_R = -z", close(cur_R, -Z))
check("A4 [fig mag-moment-torque] upper-left end carries current OUT of the screen (odot): m x r_L = +z", close(cur_L, Z))
F_R = np.cross(cur_R, B_s); F_L = np.cross(cur_L, B_s)
check("A4 [fig] force on the lower-right end points RIGHT: (-z) x (+y) = +x", close(F_R, X))
check("A4 [fig] force on the upper-left end points LEFT: (+z) x (+y) = -x", close(F_L, -X))
T_s = np.cross(P_R, F_R) + np.cross(P_L, F_L)
check("A4 [fig] couple's torque is out of the screen (counter-clockwise) and equals m x B0",
      close(T_s / np.linalg.norm(T_s), Z) and close(T_s, np.cross(m_s, B_s) * 1.0))
check("A4 [fig] counter-clockwise rotation moves the right-tilted m toward B0 (vertical)", np.dot(np.cross(Z, m_s), B_s) > 0)

# A5 iron at saturation: M = N m
rho_Fe = 7874.0; M_Fe = 55.845e-3
N_Fe = rho_Fe / M_Fe * NA
M_sat = N_Fe * 2.2 * muB
print(f"   iron: N = {N_Fe:.4e} /m^3, M_sat (2.2 muB/atom) = {M_sat:.4e} A/m, mu0 M = {mu0*M_sat:.4f} T")
check("A5 iron atom density about 8.5e28 per m^3", abs(N_Fe / 8.49e28 - 1) < 0.005)
check("A5 iron M_sat ≈ 1.7e6 A/m and mu0 M_sat ≈ 2.2 T", abs(M_sat / 1.73e6 - 1) < 0.01 and abs(mu0 * M_sat - 2.18) < 0.02)

# A6 paramagnet: alignment energy vs thermal energy
ratio = kB * 300 / (muB * 1.0)
check("A6 kT(300 K) / (muB x 1 T) ≈ 450", 440 < ratio < 455, f"ratio = {ratio:.1f}; kT = {kB*300:.3e} J, muB*1T = {muB:.3e} J")

# A6b how many bound charges: copper has 29 electrons per atom, 8.49e28 atoms per m^3
n_Cu = 8960.0 / 63.546e-3 * NA
check("A6b electrons per m^3 in copper ≈ 2.5e30 ('about 10^30')", abs(29 * n_Cu / 2.46e30 - 1) < 0.01, f"atoms {n_Cu:.3e}/m^3, electrons {29*n_Cu:.3e}/m^3")
# A7 units of M: [N][m] = m^-3 * A m^2 = A m^-1, same as H (A/m) and J_s (A/m)
dimN = np.array([-3, 0]); dimm = np.array([2, 1])      # (metre exponent, ampere exponent)
check("A7 units: (1/m^3)(A m^2) = A/m", close(dimN + dimm, [-1, 1]))
# magnet-as-solenoid number used on concepts/magnetization
check("A8 mu0 x 1.0e6 A/m = 1.26 T (a permanent magnet ≈ 1000 turns/m x 1000 A)", abs(mu0 * 1e6 - 1.2566) < 1e-3 and 1000 * 1000 == 1e6)

print("=" * 78)
print("B. Bound-charge continuity and the macroscopic decomposition (finite differences)")
print("=" * 78)
h = 1e-4
def Pf(x, y, z, t):
    return np.array([np.sin(x + 2 * y) * np.cos(t), x * z * np.sin(2 * t), np.exp(-y * y) * np.cos(z + t)])
def Mf(x, y, z, t):
    return np.array([y * np.cos(z) + t * x, np.sin(x * z) * (1 + t), x * x * y - np.cos(y * t)])
def div(F, p, t):
    x, y, z = p
    return ((F(x + h, y, z, t)[0] - F(x - h, y, z, t)[0]) + (F(x, y + h, z, t)[1] - F(x, y - h, z, t)[1]) +
            (F(x, y, z + h, t)[2] - F(x, y, z - h, t)[2])) / (2 * h)
def curl(F, p, t):
    x, y, z = p
    d = lambda i, j: (F(*(p + h * np.eye(3)[j]), t)[i] - F(*(p - h * np.eye(3)[j]), t)[i]) / (2 * h)
    return np.array([d(2, 1) - d(1, 2), d(0, 2) - d(2, 0), d(1, 0) - d(0, 1)])
def ddt(F, p, t):
    return (F(*p, t + h) - F(*p, t - h)) / (2 * h)
rng = np.random.default_rng(17)
worst_cont, worst_divcurl = 0.0, 0.0
for _ in range(6):
    p = rng.uniform(-1, 1, 3); t = rng.uniform(0, 2)
    rho_b = lambda tt: -div(Pf, p, tt)
    J_b = lambda pp, tt: ((Pf(*pp, tt + h) - Pf(*pp, tt - h)) / (2 * h) + curl(Mf, pp, tt))
    drho_dt = (rho_b(t + h) - rho_b(t - h)) / (2 * h)
    divJ = sum((J_b(p + h * np.eye(3)[k], t)[k] - J_b(p - h * np.eye(3)[k], t)[k]) / (2 * h) for k in range(3))
    worst_cont = max(worst_cont, abs(drho_dt + divJ))
    dc = sum((curl(Mf, p + h * np.eye(3)[k], t)[k] - curl(Mf, p - h * np.eye(3)[k], t)[k]) / (2 * h) for k in range(3))
    worst_divcurl = max(worst_divcurl, abs(dc))
check("B1 bound charge rho_b = -div P and bound current J_b = dP/dt + curl M obey continuity", worst_cont < 1e-5, f"max residual {worst_cont:.1e}")
check("B2 div(curl M) = 0: the magnetization current never piles up charge", worst_divcurl < 1e-5, f"max {worst_divcurl:.1e}")
# B3 microscopic Ampere with all currents <=> macroscopic with free current only (sign bookkeeping)
def Ef(x, y, z, t): return np.array([np.cos(x * t), y * z, np.sin(x + y + z + t)])
def Bf(x, y, z, t): return np.array([z * np.sin(t), np.cos(x - y) * t, x * y * z])
worst = 0.0
for _ in range(4):
    p = rng.uniform(-1, 1, 3); t = rng.uniform(0, 2)
    # J_f that makes microscopic Ampere hold: curl(B/mu0) = J_f + dP/dt + curl M + eps0 dE/dt
    Jf = curl(lambda *a: Bf(*a) / mu0, p, t) - ddt(Pf, p, t) - curl(Mf, p, t) - eps0 * ddt(Ef, p, t)
    Hf = lambda *a: Bf(*a) / mu0 - Mf(*a)
    Df = lambda *a: eps0 * Ef(*a) + Pf(*a)
    resid = curl(Hf, p, t) - Jf - ddt(Df, p, t)
    worst = max(worst, np.max(np.abs(resid)) / np.max(np.abs(Jf)))
check("B3 with H = B/mu0 - M and D = eps0 E + P, curl H = J_free + dD/dt (same J_free)", worst < 1e-6, f"rel. residual {worst:.1e}")
# B4 same for Gauss: div(eps0 E) = rho_f - div P  <=>  div D = rho_f
worst = 0.0
for _ in range(4):
    p = rng.uniform(-1, 1, 3); t = rng.uniform(0, 2)
    rhof = div(lambda *a: eps0 * Ef(*a), p, t) + div(Pf, p, t)
    resid = div(lambda *a: eps0 * Ef(*a) + Pf(*a), p, t) - rhof
    worst = max(worst, abs(resid))
check("B4 div(eps0 E) = rho_f - div P  <=>  div D = rho_f", worst < 1e-8)

print("=" * 78)
print("C. Atomic loops -> magnetization current (volume curl M and surface M x n)")
print("=" * 78)
def edge_currents(Igrid):
    """Cells (i,j): i = column (x), j = row (y), each a counter-clockwise loop (seen from +z) of current I[i,j].
    Return net current on vertical edges (along +y) and horizontal edges (along +x)."""
    nx, ny = Igrid.shape
    V = np.zeros((nx + 1, ny)); H_ = np.zeros((nx, ny + 1))
    for i in range(nx):
        for j in range(ny):
            I = Igrid[i, j]
            V[i + 1, j] += I     # right edge goes up (+y)
            V[i, j] -= I         # left edge goes down
            H_[i, j] += I        # bottom edge goes right (+x)
            H_[i, j + 1] -= I    # top edge goes left
    return V, H_
nx, ny, I0 = 4, 3, 1.0
V, Hh = edge_currents(np.full((nx, ny), I0))
check("C1 uniform loops: every interior edge carries zero net current", np.all(V[1:-1, :] == 0) and np.all(Hh[:, 1:-1] == 0))
check("C1 uniform loops: right boundary +I (up), left -I (down), bottom +I (right), top -I (left)",
      np.all(V[-1, :] == I0) and np.all(V[0, :] == -I0) and np.all(Hh[:, 0] == I0) and np.all(Hh[:, -1] == -I0))
# compare with M x n (M = +z): right n=+x -> +y ; top n=+y -> -x ; left -> -y ; bottom -> +x
for nvec, expect, lab in ((X, Y, "right"), (Y, -X, "top"), (-X, -Y, "left"), (-Y, X, "bottom")):
    check(f"C1 boundary current direction on the {lab} edge equals M x n (M out of the page)", close(np.cross(Z, nvec), expect))
# magnitude: cell side s, loop current I -> m = I s^2, M = m/s^3 = I/s; boundary: one edge (current I) per length s -> I/s = M
s = 0.3; Icell = 2.0
check("C1 surface current per unit length I/s equals M = I s^2/s^3", close(Icell / s, Icell * s ** 2 / s ** 3))
# C2 non-uniform M_z(x): net current on a shared vertical edge -> J_y = -dM_z/dx
s = 0.01
xs = np.arange(0, 1, s)
Mz = 3.0 + 2.0 * xs + 0.5 * xs ** 2
Igrid = np.tile((Mz * s)[:, None], (1, 5))     # I = M s
V, _ = edge_currents(Igrid)
Jy_edges = V[1:-1, 2] / s ** 2                 # current per area s x s (layers stacked with spacing s in z)
x_edges = xs[:-1] + s / 2                      # cells are centred at xs; the shared edge is half-way
dMdx = 2.0 + 1.0 * x_edges
check("C2 non-uniform M: the uncancelled edge current density equals -dMz/dx = (curl M)_y", close(Jy_edges, -dMdx, rel=1e-6, abs_=1e-6),
      f"edge J_y at x={x_edges[50]:.2f}: {Jy_edges[50]:.4f} vs {-dMdx[50]:.4f}")
# example on concepts/magnetization: M = M0 (x/d) z in a slab -> curl M = -(M0/d) y
M0, d = 5.0, 0.2
cm = curl(lambda x, y, z, t: np.array([0, 0, M0 * x / d]), np.array([0.05, 0.1, 0.0]), 0.0)
check("C2 M = M0 (x/d) z gives curl M = -(M0/d) y (uniform)", close(cm, [0, -M0 / d, 0], rel=1e-6, abs_=1e-6))
# C3 uniformly magnetized rod: side n = r_hat -> M x r_hat = M phi_hat ; ends -> 0
Mrod = 7.0 * Z
ok = True
for ph in np.linspace(0, 2 * math.pi, 9):
    rh = np.array([math.cos(ph), math.sin(ph), 0]); phh = np.array([-math.sin(ph), math.cos(ph), 0])
    ok &= close(np.cross(Mrod, rh), 7.0 * phh)
check("C3 rod: M x r_hat = M phi_hat on the side (a solenoid winding, counter-clockwise seen from +z)", ok)
check("C3 rod: no magnetization current on the end faces (M x (+-z) = 0)", close(np.cross(Mrod, Z), 0) and close(np.cross(Mrod, -Z), 0))
# screen frame of figure mag-loops-surface-current right panel: rod with M up (+y_s): right side n=+x -> into screen; left -> out
check("C3 [fig mag-loops-surface-current] rod with M up: right side current INTO the screen (y x x = -z)", close(np.cross(Y, X), -Z))
check("C3 [fig] rod with M up: left side current OUT of the screen (y x -x = +z)", close(np.cross(Y, -X), Z))
# that winding (odot left, otimes right) must make B up inside, as in fig solenoid-ampere:
# explicit Biot-Savart sense at the centre from two antiparallel line currents at x=-R (+z) and x=+R (-z)
R = 1.0
B_centre = np.cross(Z, (np.zeros(3) - (-R * X))) / R ** 2 + np.cross(-Z, (np.zeros(3) - R * X)) / R ** 2
check("C3 [fig] explicit dl x R_hat: the two wires give B along +y (up) at the centre", B_centre[1] > 0 and abs(B_centre[0]) < 1e-12)
# C4 thin-layer limit: M_z drops from M0 to 0 across x in (0, delta) -> integral of (curl M)_y = M0 -> J_sM = M0 y = M x n
M0, delta = 4.0, 1e-3
xg = np.linspace(-delta, 2 * delta, 30001)
Mz = M0 * np.clip(1 - xg / delta, 0, 1)
Jy = -np.gradient(Mz, xg)
Js_layer = np.trapezoid(Jy, xg) if hasattr(np, "trapezoid") else np.trapz(Jy, xg)
check("C4 thin layer: integral of curl M across the surface = M x n (n = +x)", abs(Js_layer - M0) < 1e-6 and close(np.cross(M0 * Z, X), M0 * Y))
# C5 interface form: J_sM = n x (M1 - M2) = M2 x n_out2 + M1 x n_out1
for _ in range(5):
    M1 = rng.normal(size=3); M2 = rng.normal(size=3); n = Z
    lhs = np.cross(n, M1 - M2); rhs = np.cross(M2, n) + np.cross(M1, -n)
    ok = close(lhs, rhs)
check("C5 interface magnetization current n x (M1 - M2) = (face of 2: M2 x n) + (face of 1: M1 x (-n))", ok)
# C6 twin: surface bound charge rho_sb = -n.(P1 - P2) = P2.n + P1.(-n)
for _ in range(5):
    P1 = rng.normal(size=3); P2 = rng.normal(size=3); n = Z
    ok = close(-np.dot(n, P1 - P2), np.dot(P2, n) + np.dot(P1, -n))
check("C6 twin: rho_sb = -n.(P1 - P2) = P2.n + P1.(-n)", ok)

print("=" * 78)
print("D. H, chi_m, mu; the solenoid with a core; inductance; demagnetization")
print("=" * 78)
for chi in (-9.4e-6, 2.1e-5, 99.0, 4999.0):
    Hv = np.array([0.3, -1.2, 2.0])
    Mv = chi * Hv; Bv = mu0 * (Hv + Mv)
    mu = mu0 * (1 + chi)
    ok = close(Bv, mu * Hv) and close(Hv, Bv / mu0 - Mv)
    ok &= close(Bv * (mu - mu0) / (mu * mu0), Mv)        # slide-17 concept-map form
    check(f"D1 chi_m={chi:g}: B = mu0(H + M) = mu H, H = B/mu0 - M, M = B(mu-mu0)/(mu mu0) = chi_m H", ok)
# D2 solenoid with core
n_t, I0, chi = 1000.0, 2.0, 99.0
H0 = n_t * I0; B0 = mu0 * n_t * I0; Mc = chi * H0; Bc = mu0 * (1 + chi) * H0
print(f"   solenoid: H = {H0:.0f} A/m, B0 = {B0*1e3:.4f} mT, M = {Mc:.4e} A/m, mu0 M = {mu0*Mc:.5f} T, B_core = {Bc:.5f} T")
check("D2 solenoid n=1000/m, I=2 A: H = 2000 A/m in and out of the core", H0 == 2000)
check("D2 B0 = mu0 n I = 2.51 mT outside the core", abs(B0 - 2.5133e-3) < 1e-6)
check("D2 M = 99 x 2000 = 1.98e5 A/m, mu0 M = 0.249 T", abs(Mc - 1.98e5) < 1e-6 and abs(mu0 * Mc - 0.24881) < 1e-5)
check("D2 B_core = B0 + mu0 M = mu0 (1 + chi) H = 0.251 T = 100 B0", abs(Bc - 0.25133) < 1e-5 and close(Bc, B0 + mu0 * Mc) and close(Bc / B0, 100))
check("D2 H = B/mu0 - M equals n I inside the core too", close(Bc / mu0 - Mc, H0))
B_iron_linear = mu0 * 5000 * H0
check("D2 iron mu_r = 5000 in the same coil: linear formula gives 12.6 T, far above iron's ≈2.2 T saturation", abs(B_iron_linear - 12.566) < 0.01 and B_iron_linear > 5 * 2.2)
# Ampere check: rectangle with one leg (length l) inside the core along z, the other outside the coil -> H l = n l I
lseg = 0.37
check("D2 Ampere on a rectangle through the core: H*l = (n l) I, independent of the core", close(H0 * lseg, n_t * lseg * I0))
# D3 the notes' atomic-stack average
for _ in range(3):
    Al, Il, dx, dy, dz = rng.uniform(0.1, 2, 5)
    Na = 1 / (dx * dy * dz)
    ok = close(Al / (dx * dy) * mu0 * Il / dz, mu0 * Na * Il * Al)
check("D3 (A_l/(dx dy)) mu0 I_l/dz = mu0 N_a I_l A_l = mu0 M", ok)
# twin: Lecture 8 dipole lattice average -P/eps0 (opposite to p) vs loop lattice +mu0 M (along m)
q_, dsep, dx, dy, dz = 1.3, 0.1, 1.0, 1.0, 1.0
E1 = -q_ / (eps0 * dx * dy)              # between the sheets of a pair, opposite to p
Ep = E1 * dsep / dz
check("D3 twin: dipole lattice averages to -P/eps0 (against p); loop lattice to +mu0 M (along m)",
      close(Ep, -(q_ * dsep / (dx * dy * dz)) / eps0) and (Al / (dx * dy) * mu0 * Il / dz) > 0)
# D4 sphere in a uniform field (demagnetizing factor 1/3)
for mur in (100.0, 5000.0):
    chi = mur - 1; Happ = 1.0
    Hin = 3 * Happ / (mur + 2)
    Min = chi * Hin
    ok = close(Hin, Happ - Min / 3)
    Bratio = mu0 * (Hin + Min) / (mu0 * Happ)
    check(f"D4 sphere mu_r={mur:g}: H_in = H0 - M/3 = 3H0/(mu_r+2); B_in/(mu0 H0) = 3mu_r/(mu_r+2) = {Bratio:.4f}",
          ok and close(Bratio, 3 * mur / (mur + 2)))
check("D4 an iron sphere multiplies B by less than 3, a long iron rod along H by mu_r", 3 * 5000 / 5002 < 3)
# D5 inductance with a core
n_t, A, ell = 1000.0, 1e-4, 0.1
L_air = n_t ** 2 * mu0 * A * ell
print(f"   solenoid L: air {L_air*1e6:.3f} uH, mu_r=100 core {100*L_air*1e3:.4f} mH")
check("D5 L = n^2 mu0 A l = 12.6 uH (n=1000/m, A=1 cm^2, l=10 cm); filled core mu_r=100 -> 1.26 mH",
      abs(L_air - 12.566e-6) < 1e-8 and abs(100 * L_air - 1.2566e-3) < 1e-6)

print("=" * 78)
print("E. Material tables (slides): chi_m <-> mu_r and classification")
print("=" * 78)
chis = {"Copper": -0.94e-5, "Water": -0.88e-5, "Platinum": 2.90e-5, "Aluminum": 2.10e-5, "Liquid oxygen": 3.50e-5}
for k, v_ in chis.items():
    print(f"   {k:14s} chi_m = {v_:+.2e} -> mu_r = {1+v_:.7f}")
check("E1 copper -0.94e-5 -> mu_r 0.9999906 ≈ table 0.999991", abs((1 - 0.94e-5) - 0.999991) < 1e-6)
check("E1 water -0.88e-5 -> mu_r 0.9999912 ≈ table 0.999991", abs((1 - 0.88e-5) - 0.999991) < 1e-6)
check("E1 aluminum +2.10e-5 -> mu_r 1.000021 ≈ table 1.00002", abs((1 + 2.1e-5) - 1.00002) < 2e-6)
table = {"Bismuth": 0.99983, "Silver": 0.99993, "Copper": 0.999991, "Water": 0.999991, "Aluminum": 1.00002, "Palladium": 1.0008,
         "2-81 Permalloy powder": 130, "Cobalt": 250, "Nickel": 600, "Ferroxcube 3": 1500, "Mild steel": 2000, "Iron (0.2 imp.)": 5000,
         "Silicon iron": 7000, "78 Permalloy": 1e5, "Mumetal": 1e5, "Purified iron": 2e5, "Superalloy": 1e6}
for k, v_ in table.items():
    print(f"   {k:22s} mu_r = {v_:<10g} chi_m = {v_-1:+.3g}")
check("E2 bismuth chi_m = -1.7e-4, silver -7e-5 (diamagnetic: negative)", abs((0.99983 - 1) + 1.7e-4) < 1e-9 and abs((0.99993 - 1) + 7e-5) < 1e-9)
check("E2 palladium chi_m = +8e-4 (paramagnetic: small positive)", abs(1.0008 - 1 - 8e-4) < 1e-12)
check("E2 cobalt chi_m = 249, nickel 599, iron 4999 (ferromagnetic: >> 1)", table["Cobalt"] - 1 == 249 and table["Nickel"] - 1 == 599 and table["Iron (0.2 imp.)"] - 1 == 4999)
check("E2 every diamagnet in the table has mu_r < 1, every paramagnet 1 < mu_r < 1.001, every ferromagnet mu_r >= 130",
      all(table[k] < 1 for k in ("Bismuth", "Silver", "Copper", "Water")) and all(1 < table[k] < 1.001 for k in ("Aluminum", "Palladium"))
      and all(table[k] >= 130 for k in list(table)[6:]))

print("=" * 78)
print("F. Hysteresis model used in figure mag-hysteresis")
print("=" * 78)
Bs, Hc, w = 1.0, 0.9, 0.8
Bd = lambda H: Bs * np.tanh((H + Hc) / w)     # descending branch
Ba = lambda H: Bs * np.tanh((H - Hc) / w)     # ascending branch
Bv = lambda H: Bs * np.tanh((H / w) ** 2 / (1 + H / w))   # virgin curve for H >= 0
Hgrid = np.linspace(0, 3, 601)
check("F1 descending branch crosses B = 0 at H = -Hc; ascending at +Hc", abs(Bd(-Hc)) < 1e-15 and abs(Ba(Hc)) < 1e-15)
check("F1 remanence B_r = B(H=0) on the descending branch is positive (permanent magnet)", Bd(0) > 0, f"B_r/B_s = {Bd(0):.3f}")
check("F1 virgin curve starts at the origin and stays inside the loop", Bv(0) == 0 and np.all(Bv(Hgrid) <= Bd(Hgrid) + 1e-12) and np.all(Bv(Hgrid) >= Ba(Hgrid) - 1e-12))
check("F1 loop is traversed counter-clockwise in the (H, B) plane (positive area = energy lost per cycle)",
      (np.trapezoid(Bd(Hgrid) - Ba(Hgrid), Hgrid) if hasattr(np, 'trapezoid') else np.trapz(Bd(Hgrid) - Ba(Hgrid), Hgrid)) > 0)

print("=" * 78)
print("G. Slide-16 example: magnetic slab (mu_r = 100) between two opposite current sheets")
print("=" * 78)
# page frame: x right, z up, y INTO the page.  top sheet at z=+b carries -0.1 y, bottom at z=-b carries +0.1 y.
Js = 0.1
sheets_free = [(+1.0, -Js * Y), (-1.0, +Js * Y)]           # (z position, J_s)
def H_sheets(zp, sheets):
    Ht = np.zeros(3)
    for zs, J in sheets:
        nhat = Z if zp > zs else -Z                        # from the sheet toward the field point
        Ht += 0.5 * np.cross(J, nhat)
    return Ht
check("G1 top sheet (-0.1 y) gives +0.05 x below it: (1/2)(-0.1 y) x (-z) = +0.05 x", close(0.5 * np.cross(-Js * Y, -Z), 0.05 * X))
check("G1 bottom sheet (+0.1 y) gives +0.05 x above it: (1/2)(0.1 y) x z = +0.05 x", close(0.5 * np.cross(Js * Y, Z), 0.05 * X))
check("G1 between the sheets H = 0.1 x A/m (= J_s x)", close(H_sheets(0.0, sheets_free), 0.1 * X))
check("G1 above and below the pair H = 0", close(H_sheets(2.0, sheets_free), 0) and close(H_sheets(-2.0, sheets_free), 0))
check("G1 slide hint: an out-of-page sheet (J = -y, y into page) has H = -(J/2) x above, +(J/2) x below",
      close(0.5 * np.cross(-Y, Z), -0.5 * X) and close(0.5 * np.cross(-Y, -Z), 0.5 * X))
mur = 100.0; chi = mur - 1
Hslab = 0.1 * X
Bslab = mu0 * mur * Hslab; Mslab = chi * Hslab
print(f"   slab: H = {Hslab[0]} x A/m, B = {Bslab[0]:.5e} x T, M = {Mslab[0]:.2f} x A/m; mu_r=1: B = {mu0*0.1:.5e} T")
check("G2 B in the slab = 100 mu0 (0.1) x = 1.2566e-5 x T (12.6 uT)", abs(Bslab[0] - 1.25664e-5) < 1e-9)
check("G2 M in the slab = 99 x 0.1 = 9.9 x A/m", close(Mslab, 9.9 * X))
check("G2 non-magnetic slab: same H, B = mu0 (0.1) = 1.2566e-7 T, M = 0; ratio 100", abs(mu0 * 0.1 - 1.25664e-7) < 1e-11 and close(Bslab[0] / (mu0 * 0.1), 100))
check("G2 B = mu0 (H + M) consistency", close(Bslab, mu0 * (Hslab + Mslab)))
# surface magnetization currents on the slab faces (slab |z| < 0.5, sheets at |z| = 1)
K_top = np.cross(Mslab, Z); K_bot = np.cross(Mslab, -Z)
check("G3 slab top face: M x n = 9.9 x times z = -9.9 y A/m (same sense as the top free sheet)", close(K_top, -9.9 * Y))
check("G3 slab bottom face: M x (-z) = +9.9 y A/m (same sense as the bottom free sheet)", close(K_bot, 9.9 * Y))
cM_in = curl(lambda x, y, z, t: np.array([9.9, 0.0, 0.0]), np.array([0.1, -0.2, 0.05]), 0.0)
check("G3 inside the uniform slab curl M = 0: all of the magnetization current is on the faces", close(cM_in, 0, abs_=1e-9))
check("G3 free + bound on the top face: -0.1 - 9.9 = -10 y A/m", close(-Js * Y + K_top, -10.0 * Y))
all_sheets = sheets_free + [(+0.5, K_top), (-0.5, K_bot)]
for zp, region, expect in ((1.5, "above all", 0 * X), (0.75, "air gap above the slab", mu0 * 0.1 * X), (0.0, "inside the slab", mu0 * 10 * X),
                           (-0.75, "air gap below the slab", mu0 * 0.1 * X), (-1.5, "below all", 0 * X)):
    Bvac = mu0 * H_sheets(zp, all_sheets)                     # vacuum sheet formula with ALL currents
    check(f"G4 vacuum formula with free + magnetization sheets reproduces B {region}: {Bvac[0]:.4e} T", close(Bvac, expect, abs_=1e-15))
# G5 screen frame: page x = screen x, page z = screen y, page y (into page) = -screen z
def to_screen(vp): return np.array([vp[0], vp[2], -vp[1]])
check("G5 [fig mag-slab-between-sheets] top free sheet -0.1 y -> screen +z: odot (out)", to_screen(-Js * Y)[2] > 0)
check("G5 [fig] bottom free sheet +0.1 y -> screen -z: otimes (in)", to_screen(Js * Y)[2] < 0)
check("G5 [fig] top-face magnetization current -9.9 y -> odot; bottom-face +9.9 y -> otimes", to_screen(K_top)[2] > 0 and to_screen(K_bot)[2] < 0)
check("G5 [fig] H, M, B along +x -> arrows pointing right", to_screen(Hslab)[0] > 0 and to_screen(Mslab)[0] > 0)
# right-handedness of the page frame (x right, z up, y into page): x cross y = z must hold in screen terms
check("G5 page frame (x right, z up, y into page) is right-handed: x_s x (-z_s) = +y_s", close(np.cross(to_screen(X), to_screen(Y)), to_screen(Z)))

print("=" * 78)
print("H. Boundary conditions in magnetic media; refraction")
print("=" * 78)
for _ in range(5):
    mu1, mu2 = rng.uniform(1, 10, 2) * mu0
    H1 = rng.normal(size=3); n = Z
    H2 = np.array([H1[0], H1[1], mu1 / mu2 * H1[2]])
    B1, B2 = mu1 * H1, mu2 * H2
    t1 = math.hypot(H1[0], H1[1]) / abs(H1[2]); t2 = math.hypot(H2[0], H2[1]) / abs(H2[2])
    ok = close(np.dot(n, B1 - B2), 0, abs_=1e-18) and close(np.cross(n, H1 - H2), 0) and close(t1 / t2, mu1 / mu2)
    tB1 = math.hypot(B1[0], B1[1]) / abs(B1[2]); tB2 = math.hypot(B2[0], B2[1]) / abs(B2[2])
    ok &= close(tB1, t1) and close(tB2, t2)
check("H1 B_n continuous + H_t continuous => mu1 H1n = mu2 H2n and tan(th1)/tan(th2) = mu1/mu2 (B lines bend the same as H)", ok)
for th_iron, th_air_expect in ((85.0, 0.131), (89.0, 0.657), (89.9, 6.54)):
    th_air = math.degrees(math.atan(math.tan(math.radians(th_iron)) / 5000))
    check(f"H2 air over iron (mu_r 5000): theta_iron = {th_iron} deg -> theta_air = {th_air:.3f} deg", abs(th_air - th_air_expect) < 0.005)
ok = True
for _ in range(5):
    mu1, mu2 = rng.uniform(1, 10, 2) * mu0
    H1 = rng.normal(size=3); H2 = np.array([H1[0], H1[1], mu1 / mu2 * H1[2]])
    B1, B2 = mu1 * H1, mu2 * H2
    ok &= close(B1[:2] / mu1, B2[:2] / mu2) and not close(B1[:2], B2[:2])
check("H3 with no free current tangential B still jumps: B1t/mu1 = B2t/mu2, B1t != B2t", ok)

print("=" * 78)
print("I. Worked problem: fields across a magnetic interface (z = 0, n = +z from 2 into 1)")
print("=" * 78)
mur1, mur2 = 2.0, 6.0
chi1, chi2 = mur1 - 1, mur2 - 1
H1 = np.array([4.0, -3.0, -9.0])
n = Z
H1t = H1 - np.dot(H1, n) * n; H1n = np.dot(H1, n)
H2 = H1t + (mur1 / mur2) * H1n * n
check("I-a H2 = 4x - 3y - 3z A/m", close(H2, [4, -3, -3]))
check("I-a tangential H copied (no free current) and mu1 H1n = mu2 H2n: 2(-9) = 6(-3)", close(np.cross(n, H1 - H2), 0) and close(mur1 * H1n, mur2 * H2[2]))
B1 = mur1 * mu0 * H1; B2 = mur2 * mu0 * H2
check("I-b B1 = mu0 (8x - 6y - 18z), B2 = mu0 (24x - 18y - 18z)", close(B1 / mu0, [8, -6, -18]) and close(B2 / mu0, [24, -18, -18]))
check("I-b normal B equal (-18 mu0) on both sides; tangential B jumps by mu2/mu1 = 3", close(B1[2], B2[2]) and close(B2[:2] / B1[:2], 3))
print(f"   B1z = B2z = {B1[2]:.4e} T ; |B1| = {np.linalg.norm(B1):.4e} T ; |B2| = {np.linalg.norm(B2):.4e} T")
check("I-b B_z = -18 mu0 = -2.26e-5 T (-22.6 uT)", abs(B1[2] + 2.2619e-5) < 1e-8)
M1 = chi1 * H1; M2 = chi2 * H2
check("I-c M1 = 4x - 3y - 9z, M2 = 20x - 15y - 15z A/m", close(M1, [4, -3, -9]) and close(M2, [20, -15, -15]))
check("I-c M = B/mu0 - H in each medium", close(M1, B1 / mu0 - H1) and close(M2, B2 / mu0 - H2))
th1 = math.degrees(math.atan2(np.linalg.norm(H1t), abs(H1n))); th2 = math.degrees(math.atan2(np.linalg.norm(H2[:2]), abs(H2[2])))
print(f"   theta1 = {th1:.2f} deg, theta2 = {th2:.2f} deg, tan ratio = {math.tan(math.radians(th1))/math.tan(math.radians(th2)):.4f}")
check("I-d theta1 = atan(5/9) = 29.05 deg, theta2 = atan(5/3) = 59.04 deg", abs(th1 - 29.05) < 0.01 and abs(th2 - 59.04) < 0.01)
check("I-d tan(theta1)/tan(theta2) = 1/3 = mu1/mu2", close(math.tan(math.radians(th1)) / math.tan(math.radians(th2)), 1 / 3))
check("I-d |H1t| = |H2t| = 5 A/m (3-4-5)", close(np.linalg.norm(H1t), 5) and close(np.linalg.norm(H2[:2]), 5))
K2 = np.cross(M2, n)          # top face of medium 2 (outward normal +z)
K1 = np.cross(M1, -n)         # bottom face of medium 1 (outward normal -z)
KM = K1 + K2
check("I-e face of medium 2: M2 x (+z) = -15x - 20y A/m", close(K2, [-15, -20, 0]))
check("I-e face of medium 1: M1 x (-z) = +3x + 4y A/m", close(K1, [3, 4, 0]))
check("I-e interface magnetization current = -12x - 16y A/m (= n x (M1 - M2)), magnitude 20 A/m", close(KM, [-12, -16, 0]) and close(KM, np.cross(n, M1 - M2)) and close(np.linalg.norm(KM), 20))
check("I-e check: n x (B1 - B2)/mu0 = J_s(free = 0) + J_sM", close(np.cross(n, B1 - B2) / mu0, KM))
check("I-e the face currents are antiparallel to each other (opposite faces, same-sense M_t)", np.dot(K1, K2) < 0)
check("I-e J_sM is perpendicular to H_t (it is n x (tangential M jump), (chi1 - chi2) z x H1t)", close(np.dot(KM, H1t), 0) and close(KM, (chi1 - chi2) * np.cross(n, H1t)))
check("I-e normal H jumps by minus the normal-M jump: H1z - H2z = -(M1z - M2z) = 6", close(H1[2] - H2[2], -(M1[2] - M2[2])) and close(H1[2] - H2[2], -6))
# trap numbers
check("I-trap inverted ratio gives H2z = (6/2)(-9) = -27 (wrong)", close((mur2 / mur1) * H1n, -27))
check("I-trap scaling the whole vector by 1/3 gives (4/3, -1, -3) (wrong: H_t is continuous)", close(H1 * mur1 / mur2, [4 / 3, -1, -3]))
check("I-trap M = mu0 chi H would be in tesla (wrong units): 1.0 * mu0 * 4 = 5.0e-6", abs(mu0 * chi1 * 4 - 5.0265e-6) < 1e-9)
# variant: free surface current J_s = 2 y A/m on the interface
Jsv = np.array([0.0, 2.0, 0.0])
H2v_t = H1t - np.cross(Jsv, n)
H2v = H2v_t + (mur1 / mur2) * H1n * n
check("I-var J_s x n = 2y x z = +2x, so H2t = H1t - J_s x n = (2, -3)", close(np.cross(Jsv, n), [2, 0, 0]) and close(H2v_t, [2, -3, 0]))
check("I-var boundary condition n x (H1 - H2) = J_s holds", close(np.cross(n, H1 - H2v), Jsv))
check("I-var H2 = 2x - 3y - 3z (normal part unchanged: B_n still continuous)", close(H2v, [2, -3, -3]))
B2v = mur2 * mu0 * H2v; M2v = chi2 * H2v
check("I-var B2 = mu0 (12x - 18y - 18z), M2 = 10x - 15y - 15z", close(B2v / mu0, [12, -18, -18]) and close(M2v, [10, -15, -15]))
KMv = np.cross(n, M1 - M2v)
check("I-var J_sM = n x (M1 - M2) = -12x - 6y A/m", close(KMv, [-12, -6, 0]))
check("I-var total J_s + J_sM = -12x - 4y = n x (B1 - B2)/mu0", close(Jsv + KMv, [-12, -4, 0]) and close(np.cross(n, B1 - B2v) / mu0, Jsv + KMv))
th2v = math.degrees(math.atan2(np.linalg.norm(H2v[:2]), abs(H2v[2])))
check("I-var theta2 = atan(sqrt(13)/3) = 50.2 deg", abs(th2v - math.degrees(math.atan(math.sqrt(13) / 3))) < 1e-9 and abs(th2v - 50.24) < 0.01, f"{th2v:.2f} deg")
# general pattern, random parameters
ok = True
for _ in range(20):
    m1, m2 = rng.uniform(0.5, 50, 2)
    H1r = rng.normal(size=3); Jr = np.array([*rng.normal(size=2), 0.0])
    H1rt = H1r - H1r[2] * Z
    H2r = H1rt - np.cross(Jr, Z) + (m1 / m2) * H1r[2] * Z
    B1r, B2r = m1 * mu0 * H1r, m2 * mu0 * H2r
    M1r, M2r = (m1 - 1) * H1r, (m2 - 1) * H2r
    ok &= close(np.cross(Z, H1r - H2r), Jr) and close(np.dot(Z, B1r - B2r), 0, abs_=1e-18)
    ok &= close(np.cross(Z, B1r - B2r) / mu0, Jr + np.cross(Z, M1r - M2r))
check("I-pattern general recipe (H2t = H1t - J_s x n, H2n = (mu_r1/mu_r2) H1n) satisfies all conditions and the current check", ok)
# the exam-number guard: the dielectric problem used eps_r 4, 6 and E1 = (3, 2, -6); this one differs
check("I-pattern numbers differ from the dielectric worked problem (4/6, (3,2,-6)) and FA26 (2/5, (4,0,-10))",
      not close(H1, [3, 2, -6]) and not close(H1, [4, 0, -10]) and (mur1, mur2) not in ((4, 6), (2, 5)))
# figure mag-refraction left panel uses the problem's numbers: tangential 5, normal -9 above, -3 below
check("I-fig [fig mag-refraction] left panel: H1 drawn (t, n) = (5, -9), H2 = (5, -3)", close([np.linalg.norm(H1t), H1n], [5, -9]) and close([np.linalg.norm(H2[:2]), H2[2]], [5, -3]))

print("=" * 78)
n_pass = sum(1 for _, ok in RESULTS if ok); n_fail = len(RESULTS) - n_pass
print(f"TOTAL: {len(RESULTS)} checks, {n_pass} PASS, {n_fail} FAIL")
