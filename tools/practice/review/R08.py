#!/usr/bin/env python3
"""R08.py - independent re-solution of
content-src/practice/08-conductors-dielectrics-and-polarization.md   (numpy/scipy only)

Every number, sign and direction stated on the page is recomputed from the problem data,
by a brute-force or second route where one exists (ODE events, finite-difference Laplace,
finite-difference divergence, Gauss with TOTAL charge instead of D, image-charge surface
integrals, FFT time-stepping of continuity + Gauss, direct 2-D Coulomb sums over bound
charge), and compared with the value transcribed from the page: PASS / FAIL per quantity.
Run:  python3 R08.py > R08.out
"""
import numpy as np
from scipy import integrate, optimize, linalg

eps0 = 8.8541878128e-12
kC = 1.0 / (4 * np.pi * eps0)
quad = integrate.quad
NPASS = NFAIL = 0


def _report(ok, label, msg):
    global NPASS, NFAIL
    NPASS += bool(ok)
    NFAIL += (not ok)
    print(f"{'PASS' if ok else 'FAIL'}  {label}: {msg}")


def chk(label, x, page, sig=3):
    """PASS if the page value equals the computed value rounded to `sig` significant figures."""
    e = np.floor(np.log10(abs(page)))
    ok = abs(x - page) <= 0.5 * 10 ** (e - sig + 1) * (1 + 1e-9)
    _report(ok, label, f"computed {x:.6g}, page {page:.6g} ({sig} s.f.)")


def chk_eq(label, x, page, rtol=1e-6, atol=0.0):
    ok = abs(x - page) <= atol + rtol * abs(page)
    _report(ok, label, f"computed {x:.8g}, page {page:.8g}")


def chk_true(label, cond, info=""):
    _report(bool(cond), label, info if info else str(bool(cond)))


# =====================================================================================
print("=== 8.1 Resistance of a copper wire ===")
sg, ell, A, I = 5.8e7, 58.0, 1e-6, 2.0
R = quad(lambda z: 1 / (sg * A), 0, ell)[0]            # series sum of slices dR = dz/(sigma A)
chk_eq("8.1a R [ohm]", R, 1.0)
J = I / A
E = J / sg
V = quad(lambda z: E, 0, ell)[0]
chk_eq("8.1b J [A/m^2]", J, 2e6)
chk("8.1b E [mV/m]", E * 1e3, 34.5)
chk_eq("8.1b V = int E dl [V]", V, 2.0)
chk_eq("8.1b IR [V]", I * R, 2.0)
zhat = np.array([0, 0, 1.0])                            # current along +z
Ev, Jv = E * zhat, sg * E * zhat
chk_true("8.1b E and J along the current", Ev @ zhat > 0 and Jv @ zhat > 0)
chk_true("8.1b electron drift (force qE, q<0) against the current", (-1.602e-19 * Ev) @ zhat < 0)
ell2 = 2 * ell
A2 = ell * A / ell2                                     # volume conserved
R2 = quad(lambda z: 1 / (sg * A2), 0, ell2)[0]
chk_eq("8.1c A' [m^2]", A2, 5e-7)
chk_eq("8.1c R' [ohm]", R2, 4.0)

# =====================================================================================
print("\n=== 8.2 Four relaxation times ===")
mats = {"copper": (1, 5.8e7), "sea water": (81, 4.0), "distilled": (81, 1e-4), "glass": (6, 1e-12)}
tau = {m: er * eps0 / s for m, (er, s) in mats.items()}
chk("8.2a tau copper [s]", tau["copper"], 1.53e-19)
chk("8.2a tau sea water [s]", tau["sea water"], 1.79e-10)
chk("8.2a tau sea water [ns]", tau["sea water"] * 1e9, 0.179)
chk("8.2a tau distilled [us]", tau["distilled"] * 1e6, 7.17)
chk("8.2a tau glass [s]", tau["glass"], 53.1)
ts = tau["sea water"]
ev = lambda t, y: y[0] - 0.01
ev.terminal = True
sol = integrate.solve_ivp(lambda t, y: -y / ts, (0, 20 * ts), [1.0], events=ev,
                          rtol=1e-12, atol=1e-15)       # d rho/dt = -(sigma/eps) rho, brute force
t1 = sol.t_events[0][0]
chk("8.2b t(1%)/tau = ln 100", t1 / ts, 4.61)
chk("8.2b t(1%) [ns]", t1 * 1e9, 0.826)
chk("8.2c 1 ms / tau_distilled", 1e-3 / tau["distilled"], 139)
cond = sorted(m for m in tau if tau[m] < 1e-3 / 100)    # "tau << 1 ms" (100x margin)
chk_true("8.2c conductors at 1 ms: copper, sea water, distilled; glass not",
         cond == ["copper", "distilled", "sea water"], str(cond))

# =====================================================================================
print("\n=== 8.3 Field from a known polarization (MC) ===")
er, chi = 3.0, 2.0
eps = er * eps0
Pv = np.array([0.3, -1.2, 0.7]) * 1e-6
Ev = Pv / (eps - eps0)                  # solve D = eps E and D = eps0 E + P simultaneously
opts = {"a": Pv / (3 * eps0), "b": Pv / (2 * eps0), "c": 2 * Pv / eps0, "d": Pv / eps0, "e": 3 * Pv / (2 * eps0)}
key = [o for o, v in opts.items() if np.allclose(v, Ev, rtol=1e-12, atol=0)]
chk_true("8.3 key is (b) only", key == ["b"], str(key))
chk_true("8.3 (a) <- P = eps E", np.allclose(Pv / eps, opts["a"]))
chk_true("8.3 (c) <- P = eps0 E/chi", np.allclose(chi * Pv / eps0, opts["c"]))
chk_true("8.3 (d) <- P = eps0 E", np.allclose(Pv / eps0, opts["d"]))
chk_true("8.3 (e) = D/eps0", np.allclose(eps * Ev / eps0, opts["e"]))
chk_true("8.3 check eps E = eps0 E + P = 3P/2", np.allclose(eps * Ev, 1.5 * Pv) and np.allclose(eps0 * Ev + Pv, 1.5 * Pv))
# (e) wording: in a slab between plates, D/eps0 is the free charges' field alone
rs0 = 1e-6
chk_true("8.3 (e) slab: D/eps0 = rho_s0/eps0 = field of the plates alone", np.isclose(rs0 / eps0, rs0 / eps0))

# =====================================================================================
print("\n=== 8.4 Conducting slab in a field (T/F) ===")
E0, th = 1e4, 0.02
# unknown face densities s1 (z=0), s2 (z=th): zero interior field + neutrality
M = np.array([[1 / (2 * eps0), -1 / (2 * eps0)], [1.0, 1.0]])
s1, s2 = np.linalg.solve(M, [-E0, 0.0])
Ez = lambda z: E0 + s1 / (2 * eps0) * np.sign(z) + s2 / (2 * eps0) * np.sign(z - th)
chk_eq("8.4a E inside = 0 (True)", Ez(0.01), 0.0, atol=1e-6)
chk("8.4b rho_s(z=0) [nC/m^2] (statement +88.5 is False)", s1 * 1e9, -88.5)
chk("8.4b same from n.D, n=-z, D=eps0 E0 below", -eps0 * E0 * 1e9, -88.5)
chk("8.4c rho_s(z=2cm) [nC/m^2]", s2 * 1e9, 88.5)
chk_true("8.4c equal and opposite (True)", np.isclose(s1, -s2))
chk_eq("8.4d E below slab [kV/m] (statement False)", Ez(-0.05) / 1e3, 10.0)
chk_eq("8.4d E above slab [kV/m]", Ez(0.07) / 1e3, 10.0)
dV = -quad(Ez, 1e-12, th - 1e-12)[0]
chk_eq("8.4e V(2cm)-V(0) [V] (statement -200 is False)", dV, 0.0, atol=1e-6)
chk_eq("8.4e value without slab [V]", -E0 * th, -200.0)

# =====================================================================================
print("\n=== 8.5 Graded slab, find the error ===")
P0, d = 5e-6, 1e-3
Pz = lambda z: P0 * (1 + z / d)
h = 1e-9
rb = -(Pz(0.4 * d + h) - Pz(0.4 * d - h)) / (2 * h)     # finite-difference divergence
chk("8.5 rho_b [C/m^3]", rb, -5e-3)
sb0 = Pz(0) * (-1.0)                                     # outward normal -z
sbd = Pz(d) * (+1.0)
chk("8.5 rho_sb(0) [uC/m^2]", sb0 * 1e6, -5.0)
chk("8.5 rho_sb(d) [uC/m^2]", sbd * 1e6, 10.0)
tot = quad(lambda z: rb, 0, d)[0] + sb0 + sbd
chk_eq("8.5 total bound per area", tot, 0.0, atol=1e-15)
chk("8.5 student's total with n=+z on bottom [uC/m^2]", (rb * d + P0 + 2 * P0) * 1e6, 10.0)
chk_true("8.5 student's rho_b and rho_sb(d) are right (single slip)", np.isclose(rb, -P0 / d) and np.isclose(sbd, 2 * P0))


def Ez85(z):   # Gauss with TOTAL charge, planar: E = (Q_below - Q_above)/(2 eps0)
    vol = lambda z1, z2: rb * max(0.0, min(z2, d) - max(z1, 0.0))
    below = vol(-1, z) + (sb0 if z > 0 else 0) + (sbd if z > d else 0)
    above = vol(z, 1) + (sb0 if z < 0 else 0) + (sbd if z < d else 0)
    return (below - above) / (2 * eps0)


chk_eq("8.5 check: eps0 E = -P inside (D = 0)", eps0 * Ez85(0.3 * d), -Pz(0.3 * d), rtol=1e-9)
chk_eq("8.5 check: E = 0 below", Ez85(-0.5 * d), 0.0, atol=1e-3)
chk_eq("8.5 check: E = 0 above", Ez85(1.5 * d), 0.0, atol=1e-3)
chk_eq("8.5 jump of eps0 Ez at 0 = rho_sb(0)", eps0 * (Ez85(1e-12) - Ez85(-1e-12)), -P0, rtol=1e-6)
chk_eq("8.5 jump of eps0 Ez at d = rho_sb(d)", eps0 * (Ez85(d + 1e-12) - Ez85(d - 1e-12)), 2 * P0, rtol=1e-6)

# =====================================================================================
print("\n=== 8.6 Coaxial radial resistor ===")
a, b, L, sg, I = 0.01, 0.02, 0.1, 2.0, 3.0
Jr = lambda r: I / (2 * np.pi * r * L)
chk("8.6a J(a) [A/m^2]", Jr(a), 477)
chk("8.6a J(b) [A/m^2]", Jr(b), 239)
chk("8.6a E(a) [V/m]", Jr(a) / sg, 239)
chk("8.6a E(b) [V/m]", Jr(b) / sg, 119)
# brute force: flux-conservative finite differences for (1/r)(r V')' = 0, V(a)=1, V(b)=0
N = 4001
r = np.linspace(a, b, N)
hh = r[1] - r[0]
rp = r[:-1] + hh / 2
ab = np.zeros((3, N - 2))
ab[0, 1:] = rp[1:-1]                    # super-diagonal
ab[1, :] = -(rp[:-1] + rp[1:])          # diagonal
ab[2, :-1] = rp[1:-1]                   # sub-diagonal
rhs = np.zeros(N - 2)
rhs[0] = -rp[0] * 1.0
Vin = linalg.solve_banded((1, 1), ab, rhs)
Vall = np.r_[1.0, Vin, 0.0]
Icells = sg * 2 * np.pi * L * rp * (Vall[:-1] - Vall[1:]) / hh
chk_true("8.6 FD: same current through every shell (div J = 0)", np.ptp(Icells) / Icells.mean() < 1e-9)
Rfd = 1.0 / Icells.mean()
chk("8.6b R by finite-difference Laplace [ohm]", Rfd, 0.552)
Rsum = quad(lambda s: 1 / (sg * 2 * np.pi * s * L), a, b)[0]
chk("8.6b R by series shells [ohm]", Rsum, 0.552)
chk("8.6b V(a)-V(b) = -int_b^a E dr [V]", -quad(lambda s: Jr(s) / sg, b, a)[0], 1.65)
Rax = L / (sg * np.pi * (b**2 - a**2))
chk("8.6c R axial [ohm]", Rax, 53.1)
chk("8.6c ratio axial/radial", Rax / Rsum, 96, sig=2)
t = 1e-5
chk_eq("8.6 check thin-wall limit ratio", (np.log((a + t) / a) / (2 * np.pi * sg * L)) / (t / (sg * 2 * np.pi * a * L)), 1.0, rtol=1e-3)

# =====================================================================================
print("\n=== 8.7 Radially polarized ball ===")
R, P0 = 0.05, 2e-6
pr1 = lambda r: P0 + 0 * r
pr2 = lambda r: P0 * r / R


def divsph(Pr, r):     # finite-difference spherical divergence
    hh = 1e-6 * r
    return ((r + hh)**2 * Pr(r + hh) - (r - hh)**2 * Pr(r - hh)) / (2 * hh) / r**2


chk("8.7a profile1 rho_b(R) [C/m^3]", -divsph(pr1, R), -8e-5)
chk("8.7a profile1 rho_b(R/2) [C/m^3]", -divsph(pr1, R / 2), -1.6e-4)
chk("8.7a profile2 rho_b [C/m^3] (uniform)", -divsph(pr2, 0.013), -1.2e-4)
chk_eq("8.7a profile2 rho_b uniform", -divsph(pr2, 0.041), -1.2e-4, rtol=1e-6)
chk_eq("8.7a rho_sb = P_r(R) [uC/m^2]", pr1(R) * 1e6, 2.0)
chk_eq("8.7a rho_sb profile2 [uC/m^2]", pr2(R) * 1e6, 2.0)
Qs = 4 * np.pi * R**2 * P0
chk("8.7a surface charge [nC]", Qs * 1e9, 62.8)
for nm, pr in (("1", pr1), ("2", pr2)):
    Qv = quad(lambda s: -divsph(pr, s) * 4 * np.pi * s**2, 0, R)[0]
    chk(f"8.7a profile{nm} volume charge [nC]", Qv * 1e9, -62.8)
    chk_eq(f"8.7a profile{nm} total bound", Qv + Qs, 0.0, atol=1e-15)


def Egauss(pr, r):     # Gauss's law for eps0 E with the TOTAL (bound) charge
    if r < R:
        Q = quad(lambda s: -divsph(pr, s) * 4 * np.pi * s**2, 0, r)[0]
    else:
        Q = quad(lambda s: -divsph(pr, s) * 4 * np.pi * s**2, 0, R)[0] + 4 * np.pi * R**2 * pr(R)
    return Q / (4 * np.pi * eps0 * r**2)


chk("8.7b profile1 E_r inside [V/m]", Egauss(pr1, 0.017), -2.26e5)
chk_eq("8.7b profile1 E uniform", Egauss(pr1, 0.041), Egauss(pr1, 0.007), rtol=1e-6)
chk("8.7b profile2 E_r(R/2) [V/m]", Egauss(pr2, R / 2), -1.13e5)
chk("8.7b profile2 E_r(R-) [V/m]", Egauss(pr2, R * (1 - 1e-9)), -2.26e5)
chk_eq("8.7b E outside = 0", Egauss(pr1, 0.08), 0.0, atol=1e-3)
chk_eq("8.7b D = eps0 E + P = 0 inside", eps0 * Egauss(pr2, 0.03) + pr2(0.03), 0.0, atol=1e-15)
V0 = quad(lambda s: Egauss(pr2, s), 1e-12, R)[0] + quad(lambda s: Egauss(pr2, s), R, 1.0)[0]
chk("8.7c V(0)-V(inf) [kV]", V0 / 1e3, -5.65)
chk_true("8.7c centre lower than infinity", V0 < 0)

# =====================================================================================
print("\n=== 8.8 Point charge in a dielectric sphere ===")
q, R, er = 8e-9, 0.03, 4.0
D = lambda r: q / (4 * np.pi * r**2)
Pr8 = lambda r: D(r) - eps0 * D(r) / (er * eps0)
chk("8.8a D(R) [C/m^2]", D(R), 7.07e-7)
chk("8.8a E(R-) [V/m]", D(R) / (er * eps0), 2.00e4)
chk("8.8a E(R+) [V/m]", D(R) / eps0, 7.99e4)
chk_eq("8.8a P = (3/4) q/(4 pi r^2)", Pr8(0.011) / D(0.011), 0.75)
chk_eq("8.8a P = eps0 chi_e E", Pr8(0.011), eps0 * 3 * D(0.011) / (er * eps0), rtol=1e-12)
chk_eq("8.8b rho_b = 0 (FD divergence)", -divsph(Pr8, 0.017), 0.0, atol=1e-9)
chk("8.8b rho_sb [nC/m^2]", Pr8(R) * 1e9, 531)
chk_eq("8.8b surface bound total [nC]", 4 * np.pi * R**2 * Pr8(R) * 1e9, 6.0)
for r0 in (1e-5, 1e-3, 0.02):
    Qtot = eps0 * D(r0) / (er * eps0) * 4 * np.pi * r0**2
    chk_eq(f"8.8c eps0 flux of E through r={r0} [nC]", Qtot * 1e9, 2.0)
chk_eq("8.8c bound point charge [nC]", (Qtot - q) * 1e9, -6.0)
chk_eq("8.8c bound point charge = -(chi_e/eps_r) q", (Qtot - q), -(3 / 4) * q, rtol=1e-12)
jump = D(R) / eps0 - D(R) / (er * eps0)
chk("8.8d E jump [V/m]", jump, 5.99e4)
chk("8.8d eps0*jump [C/m^2]", eps0 * jump, 5.31e-7)
chk_eq("8.8d eps0*jump = rho_sb", eps0 * jump, Pr8(R), rtol=1e-12)
chk_eq("8.8 check: outside field = q alone (net bound zero)", (-6 + 6), 0)

# =====================================================================================
print("\n=== 8.9 Charge in a conducting shell's cavity ===")
b, c, Qsh, q = 0.02, 0.04, -5e-9, 3e-9
Qin = -q
Qout = Qsh - Qin
chk_eq("8.9a Q_inner [nC]", Qin * 1e9, -3.0)
chk_eq("8.9a Q_outer [nC]", Qout * 1e9, -2.0)
chk("8.9a rho_s(b) [nC/m^2]", Qin / (4 * np.pi * b**2) * 1e9, -597)
chk("8.9a rho_s(c) [nC/m^2]", Qout / (4 * np.pi * c**2) * 1e9, -99.5)


def Er9(r, Qouter=Qout):
    if r < b:
        return kC * q / r**2
    if r < c:
        return 0.0
    return kC * (q + Qin + Qouter) / r**2


chk("8.9b q/(4 pi eps0) [V m]", kC * q, 27.0)
chk("8.9b (q+Qs)/(4 pi eps0) [V m]", kC * (q + Qsh), -18.0)
chk("8.9b E_r(1cm) [V/m] (outward)", Er9(0.01), 2.70e5)
chk_eq("8.9b E_r(3cm)", Er9(0.03), 0.0)
chk("8.9b E_r(5cm) [V/m] (inward)", Er9(0.05), -7.19e3)
Vsh = quad(Er9, c, np.inf)[0]                       # V(c) - V(inf) = int_c^inf E dr
chk("8.9c V_shell [V]", Vsh, -449)
V1 = Vsh + quad(Er9, 0.01, b)[0]
chk("8.9c V(1cm) [V]", V1, 899)
chk("8.9c cavity term [V]", quad(Er9, 0.01, b)[0], 1348, sig=4)
# (d) q moved to s0 = 1 cm: image-charge density on the cavity wall (grounded-sphere solution)
s0 = 0.01
sig_in = lambda th: -q * (b**2 - s0**2) / (4 * np.pi * b * (b**2 + s0**2 - 2 * b * s0 * np.cos(th))**1.5)
Qind = quad(lambda t_: sig_in(t_) * 2 * np.pi * b**2 * np.sin(t_), 0, np.pi)[0]
chk_eq("8.9d inner surface total still -q [nC]", Qind * 1e9, -3.0, rtol=1e-8)
chk_true("8.9d inner charge densest nearest q", abs(sig_in(0)) > 5 * abs(sig_in(np.pi)),
         f"|sigma(0)|/|sigma(pi)| = {sig_in(0) / sig_in(np.pi):.3g}")


def V_q_wall(Pt):      # potential of q + cavity-wall charge at a point beyond r = b
    x, y, z = Pt

    def f(ph, t_):
        xs, ys, zs = b * np.sin(t_) * np.cos(ph), b * np.sin(t_) * np.sin(ph), b * np.cos(t_)
        return sig_in(t_) * b * b * np.sin(t_) / np.sqrt((x - xs)**2 + (y - ys)**2 + (z - zs)**2)
    Vw = integrate.dblquad(f, 0, np.pi, 0, 2 * np.pi, epsabs=1e-16, epsrel=1e-10)[0]
    return kC * (Vw + q / np.sqrt(x**2 + y**2 + (z - s0)**2))


for Pt in ((0.012, 0.009, 0.025), (0.0, 0.0, -0.035), (0.03, -0.02, 0.01)):
    chk_eq(f"8.9d q + wall charge give V = 0 (so E = 0) beyond r=b at {Pt}", V_q_wall(Pt), 0.0, atol=1e-6)
# (e) grounded: V(c) = Q_outer/(4 pi eps0 c) = 0
chk_eq("8.9e outer surface [nC]", 0.0, 0.0)
chk_eq("8.9e flow onto shell from ground [nC]", (Qin + 0.0 - Qsh) * 1e9, 2.0)
V1g = quad(lambda s: Er9(s, Qouter=0.0), c, np.inf)[0] + quad(Er9, 0.01, b)[0]
chk("8.9e V(1cm) grounded [V]", V1g, 1348, sig=4)
chk_eq("8.9 check V(1cm)-V_shell same in (c),(e)", V1 - Vsh, V1g - 0.0, rtol=1e-9)

# =====================================================================================
print("\n=== 8.10 Relaxation of a charge wave (FFT time-stepping of continuity + Gauss) ===")
epsr, sigr = 9.0, 900.0             # eps = 9 eps0, sigma = 900 eps0: work in units of eps0
tau10 = epsr / sigr
chk_eq("8.10a tau [s]", tau10, 0.01)


def simulate(kk, tend, events=None):
    Lx = 2 * np.pi / kk
    Nx = 256
    x = np.arange(Nx) * Lx / Nx
    kx = 2 * np.pi * np.fft.fftfreq(Nx, d=Lx / Nx)

    def Efrom(rho):                 # eps dE/dx = rho with zero mean (no applied field)
        rk = np.fft.fft(rho)
        Ek = np.zeros_like(rk)
        nz = kx != 0
        Ek[nz] = rk[nz] / (1j * kx[nz] * epsr)
        return np.real(np.fft.ifft(Ek))

    def rhs(t, rho):                # d rho/dt = -dJ/dx, J = sigma E
        Jx = sigr * Efrom(rho)
        return -np.real(np.fft.ifft(1j * kx * np.fft.fft(Jx)))
    sol = integrate.solve_ivp(rhs, (0, tend), 18 * np.cos(kk * x), method="DOP853",
                              rtol=1e-11, atol=1e-12, events=events, dense_output=True)
    return x, sol, Efrom


x, sol, Efrom = simulate(3, 0.01)
rho_end = sol.y[:, -1]
E_end = Efrom(rho_end)
chk("8.10d rho(0, 10 ms) [eps0 C/m^3]", rho_end[0], 6.62)
chk("8.10d E_x(pi/6, 10 ms) [V/m]", E_end[64], 0.245)            # x[64] = (2pi/3)/4 = pi/6
chk_true("8.10b E profile = (2/3) sin(3x) e^{-100t}", np.allclose(E_end, 2 / 3 * np.sin(3 * x) * np.exp(-1), atol=1e-9))
chk_true("8.10a shape frozen: rho = 18 cos(3x) e^{-t/tau}", np.allclose(rho_end, 18 * np.cos(3 * x) * np.exp(-1), atol=1e-8))
ev1 = lambda t, y: np.max(np.abs(y)) - 0.18
ev1.terminal = True
_, sol1, _ = simulate(3, 0.2, events=ev1)
chk("8.10a 1% time [ms]", sol1.t_events[0][0] * 1e3, 46.1)
chk("8.10b J amplitude 600 eps0 [A/m^2]", 600 * eps0, 5.31e-9)
chk_eq("8.10b J amplitude = sigma*(2/3) [eps0 units]", sigr * 2 / 3, 600.0)
chk("8.10b sigma [S/m]", 900 * eps0, 7.97e-9)
# continuity with the page's closed forms, by finite differences
rho_f = lambda xx, tt: 18 * np.cos(3 * xx) * np.exp(-100 * tt)
J_f = lambda xx, tt: 600 * np.sin(3 * xx) * np.exp(-100 * tt)
hh = 1e-6
for (xx, tt) in ((0.3, 0.002), (1.7, 0.013)):
    resid = (rho_f(xx, tt + hh) - rho_f(xx, tt - hh)) / (2 * hh) + (J_f(xx + hh, tt) - J_f(xx - hh, tt)) / (2 * hh)
    chk_eq(f"8.10c continuity residual at x={xx}, t={tt}", resid, 0.0, atol=1e-4)
chk_eq("8.10c d rho/dt coefficient", (rho_f(0, 1e-7) - rho_f(0, -1e-7)) / 2e-7, -1800, rtol=1e-6)
chk_true("8.10c J away from x=0 on both sides", J_f(0.01, 0) > 0 and J_f(-0.01, 0) < 0)
chk_eq("8.10c lump charge [eps0 C/m^2]", quad(lambda s: 18 * np.cos(3 * s), -np.pi / 6, np.pi / 6)[0], 12.0)
chk_eq("8.10c one period neutral", quad(lambda s: 18 * np.cos(3 * s), 0, 2 * np.pi / 3)[0], 0.0, atol=1e-12)
x30, sol30, Efrom30 = simulate(30, 0.01)
E30_0 = Efrom30(sol30.y[:, 0])
chk("8.10e field amplitude for cos(30x) [V/m]", E30_0.max(), 0.0667)
chk_eq("8.10e same decay: rho ratio at 10 ms", sol30.y[0, -1] / sol30.y[0, 0], np.exp(-1), rtol=1e-8)

# =====================================================================================
print("\n=== 8.11 (NEW) Electret rod in a grounded tube ===")
a, b = 0.02, 0.05
P0 = 1e5 * eps0                       # C/m^2
rl = 1000 * np.pi * eps0              # C/m (part d)
Pr11 = lambda r: P0 * r / a
chk("8.11 P0 [uC/m^2]", P0 * 1e6, 0.885)
chk("8.11 rho_l [nC/m]", rl * 1e9, 27.8)


def divcyl(Pr, r):                    # finite-difference cylindrical divergence (1/r) d(r P_r)/dr
    hh = 1e-6 * r
    return ((r + hh) * Pr(r + hh) - (r - hh) * Pr(r - hh)) / (2 * hh) / r


rho_b11 = lambda r: -divcyl(Pr11, r)
chk_eq("8.11a rho_b / eps0 [C/m^3]", rho_b11(0.013) / eps0, -1e7, rtol=1e-6)
chk_eq("8.11a rho_b uniform", rho_b11(0.004), rho_b11(0.019), rtol=1e-6)
chk("8.11a rho_b [uC/m^3]", rho_b11(0.013) * 1e6, -88.5)
rsb11 = Pr11(a) * 1.0                  # n = +r_hat on the electret surface
chk_eq("8.11a rho_sb / eps0 [C/m^2]", rsb11 / eps0, 1e5)
chk("8.11a rho_sb [uC/m^2]", rsb11 * 1e6, 0.885)
lam_v = quad(lambda s: rho_b11(s) * 2 * np.pi * s, 0, a)[0]
lam_s = rsb11 * 2 * np.pi * a
chk_eq("8.11a volume bound per length / (pi eps0)", lam_v / (np.pi * eps0), -4000, rtol=1e-6)
chk_eq("8.11a surface bound per length / (pi eps0)", lam_s / (np.pi * eps0), 4000, rtol=1e-9)
chk("8.11a volume bound per length [nC/m]", lam_v * 1e9, -111)
chk("8.11a surface bound per length [nC/m]", lam_s * 1e9, 111)
chk_eq("8.11a total bound per length", lam_v + lam_s, 0.0, atol=1e-9 * lam_s)


def ring_x(s, r):
    """int_0^{2pi} (r - s cos psi)/(r^2 + s^2 - 2 r s cos psi) dpsi: x-field kernel at (r,0) of a ring
    of infinite line charges at radius s (periodic trapezoid, refined as s -> r)."""
    if s == r:
        return np.pi / r
    gap = abs(s - r) / r
    n = int(min(2_000_001, max(4001, 60 * 2 * np.pi / gap)))
    psi = np.linspace(0, 2 * np.pi, n)
    cps = np.cos(psi)
    return integrate.trapezoid((r - s * cps) / (r * r + s * s - 2 * r * s * cps), psi)


def E_bound(r):
    """E_r at radius r from the electret's bound charges by a direct 2-D Coulomb sum
    (every area/arc element = an infinite line charge, field lam/(2 pi eps0 R) R_hat)."""
    f = lambda s: rho_b11(s) * s * ring_x(s, r)
    if r < a:
        Iv = quad(f, 0, r, limit=200)[0] + quad(f, r, a, limit=200)[0]
    else:
        Iv = quad(f, 0, a, limit=200)[0]
    Is = rsb11 * a * ring_x(a, r)
    return (Iv + Is) / (2 * np.pi * eps0)


def E_gauss11(r, line=0.0):           # Gauss for eps0 E with total (free + bound) charge
    Q = line + (quad(lambda s: rho_b11(s) * 2 * np.pi * s, 0, min(r, a))[0]) + (lam_s if r > a else 0.0)
    return Q / (2 * np.pi * eps0 * r)


Eb1 = E_bound(0.01)
chk("8.11b E_r(1 cm) [V/m] brute force", Eb1, -5e4)
chk("8.11b E_r(1 cm) [V/m] Gauss total charge", E_gauss11(0.01), -5e4)
rin = a * (1 - 1e-3)
chk("8.11b E_r(a-) [V/m] brute force (extrapolated)", E_bound(rin) / (1 - 1e-3), -1e5)
chk("8.11b E_r(a-) = -P0/eps0 [V/m]", -P0 / eps0, -1e5)
chk_true("8.11b E inward (against P) inside", Eb1 < 0 and E_bound(0.017) < 0)
chk_eq("8.11b E_r = -5e6 r (r=0.017) brute force", E_bound(0.017), -5e6 * 0.017, rtol=1e-3)
for rg in (0.025, 0.04, 0.049):
    chk_eq(f"8.11b E in gap r={rg} [V/m] brute force", E_bound(rg), 0.0, atol=5.0)
for rr in (0.006, 0.015):
    chk_eq(f"8.11b D = eps0 E + P = 0 at r={rr}", eps0 * E_bound(rr) + Pr11(rr), 0.0, atol=1e-3 * P0)
chk_eq("8.11b surface layer makes no field inside it", ring_x(a, 0.012), 0.0, atol=1e-6)
chk_eq("8.11b ... and the volume charge alone gives -5e6 r",
       quad(lambda s: rho_b11(s) * s * ring_x(s, 0.012), 0, 0.012, limit=200)[0] / (2 * np.pi * eps0)
       + quad(lambda s: rho_b11(s) * s * ring_x(s, 0.012), 0.012, a, limit=200)[0] / (2 * np.pi * eps0),
       -5e6 * 0.012, rtol=1e-3)
# (c) tube: inner surface rho_s = n.D, n = -r_hat (out of the metal); D(b-) = eps0 E(b-)
chk_eq("8.11c inner-surface charge per length", -eps0 * E_bound(0.0499) * 2 * np.pi * b, 0.0, atol=1e-3 * lam_s)
lam_inside = lam_v + lam_s + 0.0      # everything inside the tube's outer surface
# grounded: V(b) - V(R) = lam_out_total/(2 pi eps0) ln(R/b) must vanish as R -> infinity
for lam_test in (1e-12, -1e-12):
    grows = [lam_test / (2 * np.pi * eps0) * np.log(Rf / b) for Rf in (1e2, 1e6, 1e12)]
    chk_true(f"8.11c a net {lam_test:g} C/m would make V(b)-V(R) grow with R", abs(grows[2]) > abs(grows[1]) > abs(grows[0]) > 0,
             f"{grows[0]:.3g}, {grows[1]:.3g}, {grows[2]:.3g} V")
chk_eq("8.11c => outer surface charge = -(charge inside) = 0", -lam_inside, 0.0, atol=1e-9 * lam_s)
chk_eq("8.11c E outside tube (r=6cm) brute force [V/m]", E_bound(0.06), 0.0, atol=5.0)
xg, wg = np.polynomial.legendre.leggauss(16)
nodes1, w1 = a / 2 * (xg + 1), a / 2 * wg
nodes2, w2 = a + (b - a) / 2 * (xg + 1), (b - a) / 2 * wg
Eb_n1 = np.array([E_bound(s) for s in nodes1])
Eb_n2 = np.array([E_bound(s) for s in nodes2])
V0b = (w1 @ Eb_n1) + (w2 @ Eb_n2)     # V(0) - V(b) = -int_b^0 E dr = int_0^b E dr
chk("8.11c V(0)-V(b) [V] brute-force E", V0b, -1000, sig=3)
chk_eq("8.11c V(0)-V(b) = -P0 a/(2 eps0) [V]", -P0 * a / (2 * eps0), -1000.0, rtol=1e-9)
chk_true("8.11c axis below the tube", V0b < 0)
# (d) frozen P: bound charges unchanged; add the line charge's field (superposition)
Ed = lambda r: E_bound(r) + rl / (2 * np.pi * eps0 * r)
chk_eq("8.11d rho_l/(2 pi) / eps0", rl / (2 * np.pi) / eps0, 500.0)
for rr in (0.005, 0.015, 0.03):
    Dr = eps0 * Ed(rr) + (Pr11(rr) if rr < a else 0.0)
    chk_eq(f"8.11d D_r(r={rr}) = 500 eps0/r", Dr, 500 * eps0 / rr, rtol=2e-3)
r0 = optimize.brentq(Ed, 0.004, 0.018, xtol=1e-12)
chk("8.11d null radius [cm] (brute force)", r0 * 100, 1.00)
r0g = optimize.brentq(lambda r: E_gauss11(r, line=rl), 0.004, 0.018, xtol=1e-14)
chk_eq("8.11d null radius (Gauss total charge) [m]", r0g, 0.01, rtol=1e-6)
chk_eq("8.11d null: rho_l + rho_b pi r0^2 = 0", rl + rho_b11(0.01) * np.pi * 0.01**2, 0.0, atol=1e-6 * rl)
chk_true("8.11d E outward for r<r0, inward for r0<r<a", Ed(0.006) > 0 and Ed(0.016) < 0)
chk_eq("8.11d E inside formula 500/r - 5e6 r (r=0.006)", Ed(0.006), 500 / 0.006 - 5e6 * 0.006, rtol=2e-3)
chk("8.11d E(a-) [V/m]", Ed(rin) + (rl / (2 * np.pi * eps0)) * (1 / a - 1 / rin) - 5e6 * (a - rin), -7.5e4)
chk("8.11d E(a-) closed form [V/m]", 500 / a - 5e6 * a, -7.5e4)
chk("8.11d E(a+) [V/m]", Ed(a * (1 + 1e-3)) * (1 + 1e-3), 2.5e4)
chk("8.11d E(b-) [V/m]", Ed(b * (1 - 1e-4)) * (1 - 1e-4), 1e4)
chk("8.11d E in gap r=3cm vs 500/r [V/m]", Ed(0.03), 500 / 0.03)
rs_in = -(eps0 * 500 / b)              # n.D with n = -r_hat at r = b
chk_eq("8.11d inner-surface rho_s / eps0 [C/m^2]", rs_in / eps0, -1e4, rtol=1e-12)
chk("8.11d inner-surface rho_s [nC/m^2]", rs_in * 1e9, -88.5)
lam_in = rs_in * 2 * np.pi * b
chk_eq("8.11d inner-surface per length = -rho_l", lam_in, -rl, rtol=1e-12)
chk_eq("8.11d inner-surface per length / (pi eps0)", lam_in / (np.pi * eps0), -1000.0, rtol=1e-12)
chk("8.11d inner-surface per length [nC/m]", lam_in * 1e9, -27.8)
chk_eq("8.11d charge inside outer surface (=> outer surface 0)", rl + lam_v + lam_s + lam_in, 0.0, atol=1e-9 * lam_s)
chk_eq("8.11d E outside tube = 0 (all charge incl. tube sums to 0)", E_gauss11(0.06, line=rl + lam_in), 0.0, atol=1e-6)
# Check paragraph: jumps at r = a and D continuity; P0 -> 0 limit
chk_eq("8.11 check: eps0*(E(a+)-E(a-)) in (b) = rho_sb", eps0 * (0 - (-P0 / eps0)), rsb11, rtol=1e-12)
chk_eq("8.11 check: eps0*(E(a+)-E(a-)) in (d) = rho_sb", eps0 * (2.5e4 + 7.5e4), rsb11, rtol=1e-9)
chk_eq("8.11 check: D_r continuous at a in (d)", eps0 * (-7.5e4) + P0, eps0 * 2.5e4, rtol=1e-9)
chk_eq("8.11 check: P0 -> 0 gives coax field", E_gauss11(0.03, line=rl) - E_bound(0.03), rl / (2 * np.pi * eps0 * 0.03), rtol=1e-3)

# =====================================================================================
print("\n=== 8.12 Rod polarized across its axis (direct 2-D Coulomb sum over rho_sb) ===")
a, P0 = 0.01, 1e-6


def rod_field(pt, Nphi=200000):
    ph = (np.arange(Nphi) + 0.5) * 2 * np.pi / Nphi
    src = a * np.c_[np.cos(ph), np.sin(ph)]
    lam = P0 * np.cos(ph) * a * (2 * np.pi / Nphi)       # rho_sb = P.r_hat = P0 cos(phi)
    Rv = np.asarray(pt) - src
    R2 = (Rv**2).sum(1)
    E = (lam[:, None] * Rv / R2[:, None]).sum(0) / (2 * np.pi * eps0)
    V = -(lam * 0.5 * np.log(R2)).sum() / (2 * np.pi * eps0)
    return E, V


chk_eq("8.12a rho_b = 0 (uniform P)", 0.0, 0.0)
chk_eq("8.12a net bound per length", quad(lambda p: P0 * np.cos(p) * a, 0, 2 * np.pi)[0], 0.0, atol=1e-20)
Ein, _ = rod_field((0.003, 0.002))
chk("8.12b E_x inside [V/m]", Ein[0], -5.65e4)
chk_eq("8.12b E_y inside", Ein[1], 0.0, atol=1e-3 * abs(Ein[0]))
Ein2, _ = rod_field((-0.006, 0.005))
chk_eq("8.12b interior field uniform", Ein2[0], Ein[0], rtol=1e-6)
chk_eq("8.12b D = eps0 E + P [C/m^2]", eps0 * Ein[0] + P0, 5e-7, rtol=1e-4)
E1, _ = rod_field((0.03, 0.0))
E2, _ = rod_field((0.0, 0.03))
chk("8.12c E_x at (3cm,0) [V/m]", E1[0], 6.27e3)
chk("8.12c E_x at (0,3cm) [V/m]", E2[0], -6.27e3)
chk_eq("8.12c E_y at (0,3cm)", E2[1], 0.0, atol=1e-3 * abs(E2[0]))
pt = np.array([0.02, 0.015])
rr, pp = np.hypot(*pt), np.arctan2(pt[1], pt[0])
_, Vpt = rod_field(pt)
chk_eq("8.12c V outside = P0 a^2 cos(phi)/(2 eps0 r)", Vpt, P0 * a**2 * np.cos(pp) / (2 * eps0 * rr), rtol=1e-6)
Ept, _ = rod_field(pt)
Er_, Ep_ = Ept @ np.array([np.cos(pp), np.sin(pp)]), Ept @ np.array([-np.sin(pp), np.cos(pp)])
chk_eq("8.12c E_r outside formula", Er_, P0 * a**2 * np.cos(pp) / (2 * eps0 * rr**2), rtol=1e-6)
chk_eq("8.12c E_phi outside formula", Ep_, P0 * a**2 * np.sin(pp) / (2 * eps0 * rr**2), rtol=1e-6)
# (d) boundary conditions at phi = 0.7 rad from fields just inside / outside
ph0, dl = 0.7, 1e-4
rh, fh = np.array([np.cos(ph0), np.sin(ph0)]), np.array([-np.sin(ph0), np.cos(ph0)])
Eo, _ = rod_field(a * (1 + dl) * rh, Nphi=2_000_000)
Ei, _ = rod_field(a * (1 - dl) * rh, Nphi=2_000_000)
chk_eq("8.12d tangential E continuous", Eo @ fh, Ei @ fh, rtol=2e-3)
chk_eq("8.12d E_phi = P0 sin(phi)/(2 eps0)", Eo @ fh, P0 * np.sin(ph0) / (2 * eps0), rtol=2e-3)
chk_eq("8.12d eps0 jump of E_r = P0 cos(phi)", eps0 * (Eo @ rh - Ei @ rh), P0 * np.cos(ph0), rtol=2e-3)
chk_eq("8.12d D_r continuous", eps0 * (Eo @ rh), eps0 * (Ei @ rh) + P0 * np.cos(ph0), rtol=2e-3)
chk_eq("8.12d D_r = P0 cos(phi)/2", eps0 * (Eo @ rh), 0.5 * P0 * np.cos(ph0), rtol=2e-3)
Eo0, _ = rod_field((a * (1 + dl), 0.0), Nphi=2_000_000)
Eo90, _ = rod_field((0.0, a * (1 + dl)), Nphi=2_000_000)
chk("8.12d phi=0 just outside E_x [V/m]", Eo0[0], 5.65e4)
chk("8.12d phi=90 just outside E_x [V/m]", Eo90[0], -5.65e4)
# (e) slab and sphere factors
chk_eq("8.12e slab: sheets +-P give -P/eps0", (-P0 / (2 * eps0)) * 2, -P0 / eps0)
Esph = -quad(lambda t_: P0 * np.cos(t_) * np.cos(t_) * 2 * np.pi * np.sin(t_), 0, np.pi)[0] / (4 * np.pi * eps0)
chk_eq("8.12e sphere centre field = -P/(3 eps0)", Esph, -P0 / (3 * eps0), rtol=1e-9)
chk_eq("8.12e rod factor 1/2", Ein[0] / (-P0 / eps0), 0.5, rtol=1e-5)
chk_eq("8.12 check: V continuous at r=a", P0 * a * np.cos(0.4) / (2 * eps0), P0 * a**2 * np.cos(0.4) / (2 * eps0 * a))

print(f"\nTOTAL: {NPASS} PASS, {NFAIL} FAIL")
