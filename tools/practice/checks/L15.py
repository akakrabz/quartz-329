#!/usr/bin/env python3
"""Verification script for practice/15-inductance-and-magnetic-energy.md (Lecture 15).

numpy/scipy only. Every flux and energy integral is computed numerically (quad/dblquad),
L is obtained both from flux and from energy wherever both apply, ODEs are integrated with
solve_ivp, fields from potentials use central finite differences, gauge invariance is tested
on an arbitrary test lambda, directions use explicit np.cross, and the toroid field is checked
against a brute-force Biot-Savart sum over 1000 discrete rectangular turns.
"""
import numpy as np
from scipy import integrate, optimize

eps0 = 8.8541878128e-12
mu0 = 4 * np.pi * 1e-7
c0 = 2.99792458e8
FAILS = []


def head(s):
    print("\n" + "=" * 78 + "\n" + s + "\n" + "=" * 78)


def show(label, val, unit=""):
    if isinstance(val, (list, tuple, np.ndarray)):
        print(f"  {label} = {np.array2string(np.asarray(val, dtype=float), precision=6)} {unit}")
    else:
        print(f"  {label} = {val:.6g} {unit}")


def check(label, a, b, rtol=1e-6, atol=1e-12):
    a = np.asarray(a, dtype=float)
    b = np.asarray(b, dtype=float)
    ok = np.allclose(a, b, rtol=rtol, atol=atol)
    sa = np.array2string(a, precision=7) if a.ndim else f"{float(a):.7g}"
    sb = np.array2string(b, precision=7) if b.ndim else f"{float(b):.7g}"
    print(f"  [{'OK' if ok else 'FAIL'}] {label}: {sa}  vs  {sb}")
    if not ok:
        FAILS.append(label)


def area_vector(pts):
    """Right-hand-rule area vector of a closed polygon (vertices in traversal order)."""
    pts = np.asarray(pts, dtype=float)
    s = np.zeros(3)
    for i in range(len(pts)):
        s += np.cross(pts[i], pts[(i + 1) % len(pts)])
    return 0.5 * s


# ----------------------------------------------------------------- finite-difference vector calculus
HFD = 1e-4


def grad(f, x, y, z, t, h=HFD):
    return np.array([(f(x + h, y, z, t) - f(x - h, y, z, t)) / (2 * h),
                     (f(x, y + h, z, t) - f(x, y - h, z, t)) / (2 * h),
                     (f(x, y, z + h, t) - f(x, y, z - h, t)) / (2 * h)])


def ddt(F, x, y, z, t, h=HFD):
    return (np.asarray(F(x, y, z, t + h)) - np.asarray(F(x, y, z, t - h))) / (2 * h)


def curl(F, x, y, z, t, h=HFD):
    dx = (np.asarray(F(x + h, y, z, t)) - np.asarray(F(x - h, y, z, t))) / (2 * h)
    dy = (np.asarray(F(x, y + h, z, t)) - np.asarray(F(x, y - h, z, t))) / (2 * h)
    dz = (np.asarray(F(x, y, z + h, t)) - np.asarray(F(x, y, z - h, t))) / (2 * h)
    return np.array([dy[2] - dz[1], dz[0] - dx[2], dx[1] - dy[0]])


def fields(Phi, A, x, y, z, t):
    E = -grad(Phi, x, y, z, t) - ddt(A, x, y, z, t)
    B = curl(A, x, y, z, t)
    return E, B


rng = np.random.default_rng(15)
PTS = [tuple(rng.uniform(-2, 2, 3)) + (rng.uniform(0, 3),) for _ in range(5)]

# =============================================================================
head("15.1  Long solenoid: L, N^2 scaling, energy two ways")
N, ell, a, I = 500, 0.25, 0.01, 2.0
A = np.pi * a**2
n = N / ell
show("n = N/l", n, "turns/m")
B_in = mu0 * n * I
show("B inside at I = 2 A", B_in, "T")
# flux per turn by numerical integration of B over the cross-section (B uniform inside, 0 outside)
Psi_turn = integrate.quad(lambda r: (mu0 * n * 1.0) * 2 * np.pi * r, 0, a)[0]   # per ampere
L_flux = N * Psi_turn
L_form = mu0 * N**2 * A / ell
check("L from flux = mu0 N^2 A / l", L_flux, L_form)
check("L = 4 pi^2 x 1e-5 H", L_form, 4 * np.pi**2 * 1e-5)
show("L (a)", L_form * 1e3, "mH  -> 0.395 mH")
L_b = mu0 * 1000**2 * A / ell
show("L with 1000 turns over 25 cm (b)", L_b * 1e3, "mH  -> 1.58 mH")
check("(b) factor 4", L_b / L_form, 4.0)
L_c = mu0 * 500**2 * A / 0.5
show("L with 500 turns over 50 cm (c)", L_c * 1e3, "mH  -> 0.197 mH")
check("(c) factor 1/2", L_c / L_form, 0.5)
W_circ = 0.5 * L_form * I**2
H = n * I
w = 0.5 * mu0 * H**2
vol = A * ell
W_field = integrate.quad(lambda r: 0.5 * mu0 * H**2 * 2 * np.pi * r * ell, 0, a)[0]
show("H = nI", H, "A/m")
show("w = 1/2 mu0 H^2", w, "J/m^3  (= 3.2 pi)")
check("w = 3.2 pi", w, 3.2 * np.pi)
show("volume pi a^2 l", vol, "m^3")
show("W = 1/2 L I^2", W_circ * 1e3, "mJ  (= 8 pi^2 x 1e-5 J)")
check("W = 8 pi^2 x 1e-5", W_circ, 8 * np.pi**2 * 1e-5)
check("W from int 1/2 mu0 H^2 dV = 1/2 L I^2", W_field, W_circ)
# info only: end effect of a finite solenoid at its centre
print("  info: B_centre/B_inf for l/a = 25:", (ell / 2) / np.sqrt((ell / 2)**2 + a**2))

# =============================================================================
head("15.2  RL decay of a shorted coil")
L, R, I0 = 40e-3, 8.0, 2.0
tau = L / R
show("tau = L/R", tau * 1e3, "ms")
show("1/tau", 1 / tau, "1/s  -> I(t) = 2 exp(-200 t) A")
show("energy time constant tau/2", tau / 2 * 1e3, "ms")
sol = integrate.solve_ivp(lambda t, y: [-R * y[0] / L], [0, 0.03], [I0], rtol=1e-11, atol=1e-14,
                          dense_output=True)
I_tau = sol.sol(tau)[0]
check("I(tau) ODE vs 2/e", I_tau, 2 / np.e)
show("I(tau)", I_tau, "A")
dIdt = (sol.sol(tau + 1e-7)[0] - sol.sol(tau - 1e-7)[0]) / 2e-7
VL = L * dIdt
check("V_L = L dI/dt at tau (finite diff) vs -R I", VL, -R * 2 / np.e, rtol=1e-6)
show("V_L(tau)", VL, "V  -> -5.89 V")
show("rise -L dI/dt = drop R I", -VL, "V")
W0 = 0.5 * L * I0**2
Wtau = 0.5 * L * I_tau**2
show("W0", W0 * 1e3, "mJ")
show("W(tau)", Wtau * 1e3, "mJ  -> 10.8 mJ")
check("W(tau) = W0 e^-2", Wtau, W0 * np.exp(-2))
show("W(tau)/W0 = e^-2", Wtau / W0, " -> 0.135")
t_halfW = optimize.brentq(lambda t: 0.5 * L * sol.sol(t)[0]**2 - W0 / 2, 1e-6, 0.02, xtol=1e-14)
show("time at which W = W0/2", t_halfW * 1e3, "ms  -> 1.73 ms")
check("t_halfW = (tau/2) ln 2", t_halfW, tau / 2 * np.log(2))
show("I at that time", sol.sol(t_halfW)[0], "A  (= 2/sqrt2 = 1.41 A)")
heat = integrate.quad(lambda t: R * (I0 * np.exp(-t / tau))**2, 0, np.inf)[0]
check("heat int I^2 R dt = W0", heat, W0)

# =============================================================================
head("15.3  Fields from Phi = 2y^2, A = -4yt y + 3x z (SP18 MC(v) style)")
Phi3 = lambda x, y, z, t: 2 * y**2
A3 = lambda x, y, z, t: np.array([0.0, -4 * y * t, 3 * x])
for p in PTS:
    E, B = fields(Phi3, A3, *p)
    check(f"E = 0 at {np.round(p, 2)}", E, [0, 0, 0], atol=1e-6)
    check(f"B = -3 y at {np.round(p, 2)}", B, [0, -3, 0], atol=1e-6)
    # Faraday consistency: curl E = -dB/dt
    curlE = curl(lambda x, y, z, t: fields(Phi3, A3, x, y, z, t)[0], *p, h=1e-3)
    dBdt = ddt(lambda x, y, z, t: fields(Phi3, A3, x, y, z, t)[1], *p, h=1e-3)
    check("  curl E = -dB/dt", curlE, -dBdt, atol=1e-4)
x, y, z, t = PTS[0]
show("slip: -grad Phi only (E without -dA/dt)", -grad(Phi3, x, y, z, t), f"V/m at y = {y:.3f} (= -4y yhat)")
check("slip value -4y", -grad(Phi3, x, y, z, t)[1], -4 * y, rtol=1e-6)
# MC distractors, evaluated at two points
for p in PTS[:2]:
    E_flip = -grad(Phi3, *p) + ddt(A3, *p)          # sign of dA/dt flipped
    check(f"distractor (d): -grad Phi + dA/dt = -8y yhat at y={p[1]:.3f}", E_flip, [0, -8 * p[1], 0], atol=1e-6)
    h = HFD
    dAz_dx = (A3(p[0] + h, *p[1:])[2] - A3(p[0] - h, *p[1:])[2]) / (2 * h)
    dAx_dz = (A3(p[0], p[1], p[2] + h, p[3])[0] - A3(p[0], p[1], p[2] - h, p[3])[0]) / (2 * h)
    check("distractor (c): y-component with the order reversed, dAz/dx - dAx/dz = +3", dAz_dx - dAx_dz, 3.0, atol=1e-6)
print("  -> answer (a): E = 0, B = -3 yhat T; (b) = -4y yhat, (c) B = +3 yhat, (d) E = -8y yhat are the slips")
# gauge relation: (Phi3, A3) = gauge transform of (0, 3x z) with lambda = -2 y^2 t
lam = lambda x, y, z, t: -2 * y**2 * t
for p in PTS[:2]:
    gl = grad(lam, *p)
    dl = (lam(p[0], p[1], p[2], p[3] + HFD) - lam(p[0], p[1], p[2], p[3] - HFD)) / (2 * HFD)
    check("A3 = 3x z + grad(-2y^2 t)", np.array([0, 0, 3 * p[0]]) + gl, A3(*p), atol=1e-6)
    check("Phi3 = 0 - d(-2y^2 t)/dt", 0 - dl, Phi3(*p), atol=1e-6)

# =============================================================================
head("15.4  Gauge T/F: reference Phi = 0, A = B0 x y  (E = 0, B = B0 z)")
for B0 in (1.7, -0.6):     # B0 symbolic on the page: check two values
    print(f"  -- B0 = {B0}")
    ref_E, ref_B = np.zeros(3), np.array([0, 0, B0])
    pairs = {
        "(a) Phi'=0, A'=-B0 y x": (lambda x, y, z, t: 0.0, lambda x, y, z, t: np.array([-B0 * y, 0, 0])),
        "(b) Phi'=0, A'=B0 x y + 2t z": (lambda x, y, z, t: 0.0, lambda x, y, z, t: np.array([0, B0 * x, 2 * t])),
        "(c) Phi'=-2z, A'=B0 x y + 2t z": (lambda x, y, z, t: -2 * z, lambda x, y, z, t: np.array([0, B0 * x, 2 * t])),
        "(d) Phi'=0, A'=B0 y x": (lambda x, y, z, t: 0.0, lambda x, y, z, t: np.array([B0 * y, 0, 0])),
    }
    expect = {"(a)": True, "(b)": False, "(c)": True, "(d)": False}
    for name, (Ph, Av) in pairs.items():
        same = True
        for p in PTS:
            E, B = fields(Ph, Av, *p)
            same &= np.allclose(E, ref_E, atol=1e-6) and np.allclose(B, ref_B, atol=1e-6)
        E, B = fields(Ph, Av, *PTS[0])
        print(f"  {name}: E' = {np.round(E, 6)}, B' = {np.round(B, 6)}  -> same fields: {same}")
        if same != expect[name[:3]]:
            FAILS.append("15.4 " + name)
    # (d): A' - A = B0 y x - B0 x y has curl -2 B0 z, so it is not a gradient
    check("(d) curl(A' - A) = -2 B0 z", curl(lambda x, y, z, t: np.array([B0 * y, -B0 * x, 0.0]), *PTS[2]),
          [0, 0, -2 * B0], atol=1e-6)
    # gauge functions for the true items
    for lamf, Phi_new, A_new, nm in [
            (lambda x, y, z, t: -B0 * x * y, pairs["(a) Phi'=0, A'=-B0 y x"][0], pairs["(a) Phi'=0, A'=-B0 y x"][1], "(a) lambda=-B0 x y"),
            (lambda x, y, z, t: 2 * z * t, pairs["(c) Phi'=-2z, A'=B0 x y + 2t z"][0], pairs["(c) Phi'=-2z, A'=B0 x y + 2t z"][1], "(c) lambda=2zt")]:
        p = PTS[1]
        gl = grad(lamf, *p)
        dl = (lamf(p[0], p[1], p[2], p[3] + HFD) - lamf(p[0], p[1], p[2], p[3] - HFD)) / (2 * HFD)
        check(f"{nm}: A + grad lambda = A'", np.array([0, B0 * p[0], 0]) + gl, A_new(*p), atol=1e-6)
        check(f"{nm}: 0 - dlambda/dt = Phi'", 0 - dl, Phi_new(*p), atol=1e-6)
# general gauge invariance on an arbitrary test pair and test lambda
print("  -- general test: arbitrary (Phi, A) and lambda = x^2 y t^2 + sin(z t) + exp(0.3x) y z")
PhiT = lambda x, y, z, t: x * y * np.sin(t) + z**2
AT = lambda x, y, z, t: np.array([y * z * t, x**2 * t**2, np.sin(x) * np.cos(y) * t])
lamT = lambda x, y, z, t: x**2 * y * t**2 + np.sin(z * t) + np.exp(0.3 * x) * y * z
grad_lamT = lambda x, y, z, t: np.array([2 * x * y * t**2 + 0.3 * np.exp(0.3 * x) * y * z,
                                         x**2 * t**2 + np.exp(0.3 * x) * z,
                                         t * np.cos(z * t) + np.exp(0.3 * x) * y])
dt_lamT = lambda x, y, z, t: 2 * x**2 * y * t + z * np.cos(z * t)
for p in PTS[:3]:
    check("  analytic grad(lambda) vs finite difference", grad_lamT(*p), grad(lamT, *p), rtol=1e-6, atol=1e-7)
    check("  analytic dlambda/dt vs finite difference", dt_lamT(*p),
          (lamT(p[0], p[1], p[2], p[3] + HFD) - lamT(p[0], p[1], p[2], p[3] - HFD)) / (2 * HFD), rtol=1e-6, atol=1e-7)
    PhiP = lambda x, y, z, t: PhiT(x, y, z, t) - dt_lamT(x, y, z, t)
    AP = lambda x, y, z, t: AT(x, y, z, t) + grad_lamT(x, y, z, t)
    PhiW = lambda x, y, z, t: PhiT(x, y, z, t) + dt_lamT(x, y, z, t)    # wrong sign
    E1, B1 = fields(PhiT, AT, *p)
    E2, B2 = fields(PhiP, AP, *p)
    E3, _ = fields(PhiW, AP, *p)
    check("  E unchanged under A+grad(l), Phi-dl/dt", E2, E1, atol=1e-6)
    check("  B unchanged", B2, B1, atol=1e-6)
    print(f"    (wrong sign Phi + dl/dt changes E by {np.round(E3 - E1, 4)})")

# =============================================================================
head("15.5  Two-wire line (find the error)")
a5, D5 = 1e-3, 1e-2
# wire 1 at x=0 carries +I (+z), wire 2 at x=D carries -I. B_y on the segment between them:
def By_two_wires(x, I=1.0):
    B1 = mu0 * I / (2 * np.pi * x)            # from wire 1: phi-hat at (x,0) is +y
    B2 = mu0 * I / (2 * np.pi * (D5 - x))     # from wire 2 (current -z) at its left: +y as well
    return B1 + B2
# directions by explicit cross products (Biot-Savart dl x R)
p = np.array([0.004, 0, 0])
d1 = np.cross([0, 0, 1], p - np.array([0, 0, 0]))
d2 = np.cross([0, 0, -1], p - np.array([D5, 0, 0]))
print("  direction of B1, B2 between the wires:", np.sign(d1), np.sign(d2), "(both +y)")
Psi_one = integrate.quad(lambda x: mu0 / (2 * np.pi * x), a5, D5 - a5)[0]
Psi_two = integrate.quad(By_two_wires, a5, D5 - a5)[0]
show("student's L' (one wire)", Psi_one * 1e6, "uH/m -> 0.44 uH/m")
show("correct L' (both wires)", Psi_two * 1e6, "uH/m -> 0.879 uH/m")
check("L' = (mu0/pi) ln 9", Psi_two, mu0 / np.pi * np.log(9))
show("ln 9", np.log(9))
C5 = np.pi * eps0 / np.log((D5 - a5) / a5)
# verify C' from line-charge potentials: V(+surface) - V(-surface)
rho = 1.0
Vline = lambda r_plus, r_minus: rho / (2 * np.pi * eps0) * (-np.log(r_plus) + np.log(r_minus))
dV = Vline(a5, D5 - a5) - Vline(D5 - a5, a5)
check("C' from line-charge potentials = pi eps0 / ln 9", rho / dV, C5)
show("C'", C5 * 1e12, "pF/m -> 12.7 pF/m")
show("L'C' (correct)", Psi_two * C5, "s^2/m^2")
check("L'C' = mu0 eps0", Psi_two * C5, mu0 * eps0)
show("mu0 eps0", mu0 * eps0, "s^2/m^2 -> 1.11e-17")
show("student L'C' / (mu0 eps0)", Psi_one * C5 / (mu0 * eps0))
show("student 1/sqrt(L'C')", 1 / np.sqrt(Psi_one * C5), "m/s -> 4.24e8 = sqrt2 c")
check("student speed = sqrt(2) c", 1 / np.sqrt(Psi_one * C5), np.sqrt(2) * c0, rtol=1e-6)

# =============================================================================
head("15.6  Switching on an RL circuit")
V0, L6, R6 = 12.0, 0.2, 10.0
tau6 = L6 / R6
show("tau", tau6 * 1e3, "ms")
show("1/tau", 1 / tau6, "1/s  -> I(t) = 1.2 (1 - exp(-50 t)) A")
show("I_inf", V0 / R6, "A")
sol6 = integrate.solve_ivp(lambda t, y: [(V0 - R6 * y[0]) / L6], [0, 0.2], [0.0], rtol=1e-11, atol=1e-14,
                           dense_output=True)
I6 = lambda t: sol6.sol(t)[0]
check("I(t) ODE vs 1.2(1-e^-t/tau) at t=7 ms", I6(0.007), 1.2 * (1 - np.exp(-0.007 / tau6)))
It = I6(tau6)
dI6 = (I6(tau6 + 1e-7) - I6(tau6 - 1e-7)) / 2e-7
VL6 = L6 * dI6
show("I(tau)", It, "A -> 0.759 A")
show("V_L(tau)", VL6, "V -> 4.41 V")
check("V_L(tau) = 12/e", VL6, 12 / np.e, rtol=1e-6)
show("V_R(tau)", R6 * It, "V -> 7.59 V")
check("V_L + V_R = V0", VL6 + R6 * It, V0, rtol=1e-6)
W6 = 0.5 * L6 * It**2
show("W(tau)", W6 * 1e3, "mJ -> 57.5 mJ")
Pb, PR, PL = V0 * It, It**2 * R6, VL6 * It
show("P_battery", Pb, "W -> 9.10 W")
show("P_R", PR, "W -> 5.75 W")
show("P_L = V_L I", PL, "W -> 3.35 W")
check("P_b = P_R + P_L", Pb, PR + PL, rtol=1e-6)
dWdt = (0.5 * L6 * I6(tau6 + 1e-7)**2 - 0.5 * L6 * I6(tau6 - 1e-7)**2) / 2e-7
check("P_L = dW/dt (finite difference)", PL, dWdt, rtol=1e-6)
Winf = 0.5 * L6 * (V0 / R6)**2
show("W_inf", Winf * 1e3, "mJ")
t_half6 = optimize.brentq(lambda t: 0.5 * L6 * I6(t)**2 - Winf / 2, 1e-4, 0.15, xtol=1e-14)
show("t when W = W_inf/2", t_half6 * 1e3, "ms -> 24.6 ms")
check("= tau ln(1/(1-1/sqrt2))", t_half6, tau6 * np.log(1 / (1 - 1 / np.sqrt(2))))
show("ln(1/(1-1/sqrt2))", np.log(1 / (1 - 1 / np.sqrt(2))))
t_halfI6 = optimize.brentq(lambda t: I6(t) - 0.6, 1e-4, 0.15, xtol=1e-14)
show("t when I = I_inf/2 (for comparison)", t_halfI6 * 1e3, "ms -> 13.9 ms = tau ln 2")
check("= tau ln 2", t_halfI6, tau6 * np.log(2))
show("V_L(0+) = L dI/dt at t = 0", L6 * (V0 - R6 * I6(0.0)) / L6, "V")

# =============================================================================
head("15.7  Internal inductance of a round wire")
for a7 in (0.5e-3, 1e-3, 3e-3):
    I7 = 1.0
    Hin = lambda r: I7 * r / (2 * np.pi * a7**2)
    # Ampere check: H 2 pi r = I r^2/a^2
    check(f"a={a7*1e3:.1f} mm: H(r) 2 pi r = I r^2/a^2 at r=a/2", Hin(a7 / 2) * 2 * np.pi * a7 / 2, I7 / 4)
    Wp = integrate.quad(lambda r: 0.5 * mu0 * Hin(r)**2 * 2 * np.pi * r, 0, a7)[0]
    check("  W' = mu0 I^2/(16 pi)", Wp, mu0 * I7**2 / (16 * np.pi))
    Lint = 2 * Wp / I7**2
    check("  L'_int = mu0/(8 pi) from energy", Lint, mu0 / (8 * np.pi))
    strip = integrate.quad(lambda r: mu0 * Hin(r), 0, a7)[0] / I7
    check("  naive strip flux / I = mu0/(4 pi)", strip, mu0 / (4 * np.pi))
    weighted = integrate.quad(lambda r: (r / a7)**2 * mu0 * Hin(r), 0, a7)[0] / I7
    check("  linkage-weighted flux / I = mu0/(8 pi)", weighted, mu0 / (8 * np.pi))
show("mu0/(8 pi)", mu0 / (8 * np.pi) * 1e9, "nH/m -> 50 nH/m")
Lext5 = mu0 / np.pi * np.log(9)
tot = Lext5 + 2 * mu0 / (8 * np.pi)
show("two-wire external", Lext5 * 1e6, "uH/m")
show("two-wire total (low f)", tot * 1e6, "uH/m -> 0.979 uH/m")
show("increase", (tot / Lext5 - 1) * 100, "% -> 11%")

# =============================================================================
head("15.8  Coaxial solenoids: L1, L2, M both ways, emf, series connection")
a8, b8, n1, n2, l8 = 0.01, 0.02, 2000.0, 1000.0, 0.5
N1, N2 = n1 * l8, n2 * l8
# flux per turn by numerical integration over each turn's disk
B1 = lambda r: mu0 * n1 * 1.0 * (r < a8)      # inner coil field per ampere
B2 = lambda r: mu0 * n2 * 1.0 * (r < b8)      # outer coil field per ampere
flux = lambda Bf, R: integrate.quad(lambda r: Bf(r) * 2 * np.pi * r, 0, R, points=[a8] if R > a8 else None, limit=200)[0]
L1 = N1 * flux(B1, a8)
L2 = N2 * flux(B2, b8)
M21 = N2 * flux(B1, b8)       # inner field through outer turns (radius b)
M12 = N1 * flux(B2, a8)       # outer field through inner turns (radius a)
show("N1, N2", [N1, N2])
show("L1", L1 * 1e3, "mH -> 0.790 mH")
show("L2", L2 * 1e3, "mH -> 0.790 mH")
check("L1 = 0.8 pi^2 1e-4", L1, 0.8 * np.pi**2 * 1e-4)
check("L2 = L1", L2, L1)
show("M21", M21 * 1e3, "mH -> 0.395 mH")
show("M12", M12 * 1e3, "mH")
check("M12 = M21 = mu0 n1 n2 pi a^2 l", [M12, M21], [mu0 * n1 * n2 * np.pi * a8**2 * l8] * 2)
check("M = 0.4 pi^2 1e-4 H", M21, 0.4 * np.pi**2 * 1e-4)
show("emf in outer coil for dI1/dt = 100 A/s", M21 * 100 * 1e3, "mV -> 39.5 mV")
k = M21 / np.sqrt(L1 * L2)
check("coupling k = a/b", k, a8 / b8)
for sgn, nm, expect_L in [(+1, "aiding", L1 + L2 + 2 * M21), (-1, "opposing", L1 + L2 - 2 * M21)]:
    H_in = lambda r: (n1 * sgn + n2) * (r < a8) + n2 * ((r >= a8) & (r < b8))   # per ampere
    Wser = integrate.quad(lambda r: 0.5 * mu0 * H_in(r)**2 * 2 * np.pi * r * l8, 0, b8, points=[a8], limit=200)[0]
    Lser = 2 * Wser
    show(f"series {nm}: L from energy", Lser * 1e3, "mH")
    check(f"  = L1 + L2 {'+' if sgn > 0 else '-'} 2M", Lser, expect_L)
show("bracket (n1+n2)^2 a^2 + n2^2 (b^2 - a^2)", (n1 + n2)**2 * a8**2 + n2**2 * (b8**2 - a8**2), "(900 + 300)")
show("  pieces", [(n1 + n2)**2 * a8**2, n2**2 * (b8**2 - a8**2)])
show("bracket opposing (n1-n2)^2 a^2 + n2^2 (b^2 - a^2)", (n1 - n2)**2 * a8**2 + n2**2 * (b8**2 - a8**2), "(100 + 300)")
show("  pieces", [(n1 - n2)**2 * a8**2, n2**2 * (b8**2 - a8**2)])
check("mu0 pi l x 1200 = L aiding", mu0 * np.pi * l8 * 1200, L1 + L2 + 2 * M21)
check("mu0 pi l x 400 = L opposing", mu0 * np.pi * l8 * 400, L1 + L2 - 2 * M21)
check("n1^2 a^2 = n2^2 b^2 (why L1 = L2)", n1**2 * a8**2, n2**2 * b8**2)

# =============================================================================
head("15.9  Toroid with a two-layer core (SP18 Exam 2 #2 re-parameterized)")
N9, a9, b9, h9, mur9 = 1000, 0.05, 0.10, 0.02, 9.0
I9, dIdt9 = 2.0, 50.0
mu_z = lambda z: mur9 * mu0 if z < h9 / 2 else mu0

# --- brute-force Biot-Savart over N rectangular turns (vacuum) to confirm H = N I / (2 pi r)
def seg_B(P1, P2, pts, I=1.0):
    u = P2 - P1
    Lseg = np.linalg.norm(u)
    uh = u / Lseg
    w = pts - P1
    s = w @ uh
    rho = w - np.outer(s, uh)
    d = np.linalg.norm(rho, axis=1)
    fac = mu0 * I / (4 * np.pi * d) * ((Lseg - s) / np.sqrt((Lseg - s)**2 + d**2) + s / np.sqrt(s**2 + d**2))
    dirn = np.cross(uh, rho / d[:, None])
    return fac[:, None] * dirn


def toroid_B(pts, N=N9, I=1.0):
    B = np.zeros_like(pts)
    for k in range(N):
        ph = 2 * np.pi * (k + 0.5) / N
        cph, sph = np.cos(ph), np.sin(ph)
        P = [np.array([a9 * cph, a9 * sph, 0.0]), np.array([a9 * cph, a9 * sph, h9]),
             np.array([b9 * cph, b9 * sph, h9]), np.array([b9 * cph, b9 * sph, 0.0])]
        for i in range(4):
            B += seg_B(P[i], P[(i + 1) % 4], pts, I)
    return B


test = np.array([[0.07, 0.0, 0.005], [0.06 * np.cos(1.0), 0.06 * np.sin(1.0), 0.015],
                 [0.09 * np.cos(2.5), 0.09 * np.sin(2.5), 0.01],
                 [0.03, 0.0, 0.01], [0.13, 0.0, 0.01], [0.07, 0.0, 0.04]])
Bbs = toroid_B(test)
for pnt, Bv in zip(test, Bbs):
    r = np.hypot(pnt[0], pnt[1])
    phihat = np.array([-pnt[1], pnt[0], 0]) / r
    inside = (a9 < r < b9) and (0 < pnt[2] < h9)
    Hexp = N9 * 1.0 / (2 * np.pi * r) if inside else 0.0
    print(f"  Biot-Savart at r={r:.3f}, z={pnt[2]:.3f}: H_phi = {Bv @ phihat / mu0:9.4f} A/m (per A), "
          f"|H_other| = {np.linalg.norm(Bv - (Bv @ phihat) * phihat) / mu0:.2e}; expected {Hexp:9.4f}")
    if inside:
        check("    H_phi = N I/(2 pi r)", Bv @ phihat / mu0, Hexp, rtol=2e-3)
    else:
        check("    H ~ 0 outside the core", np.linalg.norm(Bv) / mu0, 0.0, atol=0.05)
show("H(r=a) at I=2 A", N9 * I9 / (2 * np.pi * a9), "A/m")
show("H(r=b) at I=2 A", N9 * I9 / (2 * np.pi * b9), "A/m")
# orientation: area vector of one turn in the phi = 0 half-plane vs phi-hat = y-hat
turn = [[a9, 0, 0], [a9, 0, h9], [b9, 0, h9], [b9, 0, 0]]
av = area_vector(turn)
show("area vector of the turn (up inner, out top, down outer, in bottom)", av / np.linalg.norm(av))
check("normal = +phi-hat (= +y at phi=0)", av / np.linalg.norm(av), [0, 1, 0])
check("up x out = phi-hat (z x x = y)", np.cross([0, 0, 1], [1, 0, 0]), [0, 1, 0])
# flux per turn, numerically
Psi1 = integrate.dblquad(lambda z, r: mu_z(z) * N9 * 1.0 / (2 * np.pi * r), a9, b9, 0, h9,
                         epsabs=1e-16, epsrel=1e-12)[0]   # per ampere
Psi1_split = (integrate.dblquad(lambda z, r: mur9 * mu0 * N9 / (2 * np.pi * r), a9, b9, 0, h9 / 2)[0]
              + integrate.dblquad(lambda z, r: mu0 * N9 / (2 * np.pi * r), a9, b9, h9 / 2, h9)[0])
check("flux per turn (dblquad, split layers)", Psi1, Psi1_split, rtol=1e-8)
Psi1_form = 5 * mu0 * N9 * h9 * np.log(2) / (2 * np.pi)
check("Psi per turn per A = 5 mu0 N h ln2/(2 pi)", Psi1_split, Psi1_form)
show("Psi per turn per ampere", Psi1_form, "Wb/A -> 1.39e-5")
show("Psi per turn at I = 2 A", Psi1_form * I9, "Wb -> 2.77e-5")
show("N Psi per ampere", N9 * Psi1_form, "Wb/A")
show("N Psi at I = 2 A", N9 * Psi1_form * I9, "Wb -> 2.77e-2")
L9 = N9 * Psi1_split
show("L from flux", L9 * 1e3, "mH -> 13.9 mH")
L9_air = mu0 * N9**2 * h9 * np.log(2) / (2 * np.pi)
show("air-core L (SP18 form)", L9_air * 1e3, "mH -> 2.77 mH")
show("L / L_air = mean mu_r over the cross-section (9 + 1)/2", L9 / L9_air)
check("L / L_air = 5", L9 / L9_air, 5.0)
show("mu0 N h/(2 pi)", mu0 * N9 * h9 / (2 * np.pi), "Wb/A per turn")
emf9 = -L9 * dIdt9
show("self-emf -L dI/dt (relative to current's circulation)", emf9, "V -> -0.693 V: acts DOWN along inner face")
show("terminal drop V = L dI/dt", L9 * dIdt9, "V")
# energy, numerically
W9 = integrate.dblquad(lambda z, r: 0.5 * mu_z(z) * (N9 * I9 / (2 * np.pi * r))**2 * 2 * np.pi * r,
                       a9, b9, 0, h9, epsabs=1e-16, epsrel=1e-12)[0]
W9f = integrate.dblquad(lambda z, r: 0.5 * mur9 * mu0 * (N9 * I9 / (2 * np.pi * r))**2 * 2 * np.pi * r,
                        a9, b9, 0, h9 / 2)[0]
W9a = integrate.dblquad(lambda z, r: 0.5 * mu0 * (N9 * I9 / (2 * np.pi * r))**2 * 2 * np.pi * r,
                        a9, b9, h9 / 2, h9)[0]
check("W total = W ferrite + W air", W9, W9f + W9a, rtol=1e-8)
check("W from field = 1/2 L I^2 (L from flux)", W9f + W9a, 0.5 * L9 * I9**2)
show("W", (W9f + W9a) * 1e3, "mJ -> 27.7 mJ")
show("W ferrite", W9f * 1e3, "mJ")
show("W air", W9a * 1e3, "mJ")
show("ferrite fraction", W9f / (W9f + W9a))
# rewound with 500 turns
N9b = 500
Psi1b = 5 * mu0 * N9b * h9 * np.log(2) / (2 * np.pi)
L9b = N9b * Psi1b
show("factor |B| (prop. to N)", N9b / N9)
show("factor Psi per turn", Psi1b / Psi1_form)
show("factor N Psi", (N9b * Psi1b) / (N9 * Psi1_form))
show("factor L", L9b / L9)
check("N^2 scaling of L", L9b / L9, 0.25)

# =============================================================================
head("15.10  Shorted parallel-plate line (SP18 Exam 2 #3 re-parameterized)")
W10, d10, l10, I10 = 0.05, 2e-3, 1.0, 10.0
Js = I10 / W10
Js_top = np.array([Js, 0, 0])      # at y = d, along +x
Js_bot = np.array([-Js, 0, 0])     # at y = 0, along -x
show("J_s top (y=d)", Js_top, "A/m")
show("J_s bottom (y=0)", Js_bot, "A/m")
yh = np.array([0, 1, 0])
H_sheet = lambda J, n_hat: 0.5 * np.cross(J, n_hat)
H_between = H_sheet(Js_top, -yh) + H_sheet(Js_bot, +yh)
H_above = H_sheet(Js_top, +yh) + H_sheet(Js_bot, +yh)
H_below = H_sheet(Js_top, -yh) + H_sheet(Js_bot, -yh)
show("H between", H_between, "A/m")
show("H above", H_above, "A/m")
show("H below", H_below, "A/m")
show("contribution of top sheet between", H_sheet(Js_top, -yh))
show("contribution of bottom sheet between", H_sheet(Js_bot, +yh))
check("H between = -200 z", H_between, [0, 0, -200])
check("H outside = 0", np.concatenate([H_above, H_below]), np.zeros(6))
B_between = mu0 * H_between
show("B between", B_between, "T -> -2.51e-4 z T")
# boundary condition at top plate: n from medium 2 (between) into medium 1 (above) = +y
check("n x (H1 - H2) = Js_top", np.cross(yh, H_above - H_between), Js_top)
check("n x (H1 - H2) = Js_bot (n=+y from below into between)", np.cross(yh, H_between - H_below), Js_bot)
# current path orientation (plane z = const): (0,d) -> (l,d) -> (l,0) -> (0,0)
path = [[0, d10, 0], [l10, d10, 0], [l10, 0, 0], [0, 0, 0]]
av10 = area_vector(path)
show("area vector of current path", av10 / np.linalg.norm(av10))
check("dS = -z (clockwise seen from +z)", av10 / np.linalg.norm(av10), [0, 0, -1])
Psi10 = integrate.dblquad(lambda yy, xx: B_between @ np.array([0, 0, -1]), 0, l10, 0, d10)[0]
show("Psi", Psi10, "Wb -> 5.03e-7")
L10 = Psi10 / I10
show("L", L10 * 1e9, "nH -> 50.3 nH")
check("L = mu0 d l / W", L10, mu0 * d10 * l10 / W10)
show("L' = mu0 d / W", mu0 * d10 / W10 * 1e9, "nH/m")
W10e = integrate.tplquad(lambda zz, yy, xx: 0.5 * mu0 * (H_between @ H_between), 0, l10, 0, d10, 0, W10)[0]
show("W from field", W10e * 1e6, "uJ -> 2.51 uJ")
check("W field = 1/2 L I^2", W10e, 0.5 * L10 * I10**2)
C10 = eps0 * W10 / d10
show("C'", C10 * 1e12, "pF/m -> 221 pF/m")
check("L'C' = mu0 eps0", (mu0 * d10 / W10) * C10, mu0 * eps0)
show("1/sqrt(L'C')", 1 / np.sqrt((mu0 * d10 / W10) * C10), "m/s")
# scaling: d -> d/2, W -> 2W, I -> 3I
def plate(Wv, dv, Iv):
    Bv = mu0 * Iv / Wv
    return Bv, Bv * dv * l10, mu0 * dv * l10 / Wv, eps0 * Wv / dv
B_o, P_o, L_o, C_o = plate(W10, d10, I10)
B_n, P_n, L_n, C_n = plate(2 * W10, d10 / 2, 3 * I10)
show("factor |B|", B_n / B_o, "-> 1.5")
show("factor Psi", P_n / P_o, "-> 0.75")
show("factor L", L_n / L_o, "-> 0.25")
show("factor C'", C_n / C_o, "-> 4")
check("scaling factors", [B_n / B_o, P_n / P_o, L_n / L_o, C_n / C_o], [1.5, 0.75, 0.25, 4.0])
# info: finite-width correction of H at the centre (not on the page)
print("  info: finite-width strips, H at centre / (I/W) =", 2 / np.pi * np.arctan(W10 / d10))

# =============================================================================
head("15.11  Wire and rectangular loop: M, emf, A-route, RL response")
d1, d2, h11 = 0.02, 0.08, 0.5
k11 = 1e4
R11, Lloop = 5e-3, 1e-6
# B of wire at (x,0,z): phi-hat = y-hat
check("phi-hat at (x>0, y=0) = z x x-hat = +y", np.cross([0, 0, 1], [1, 0, 0]), [0, 1, 0])
loop = [[d1, 0, 0], [d1, 0, h11], [d2, 0, h11], [d2, 0, 0]]   # up near side, out along top, down far side
av11 = area_vector(loop)
check("reference circulation -> dS = +y", av11 / np.linalg.norm(av11), [0, 1, 0])
Psi11 = integrate.dblquad(lambda zz, xx: mu0 * 1.0 / (2 * np.pi * xx), d1, d2, 0, h11)[0]
M11 = Psi11
check("M = (mu0 h/2 pi) ln(d2/d1)", M11, mu0 * h11 / (2 * np.pi) * np.log(d2 / d1))
show("M", M11 * 1e6, "uH -> 0.139 uH")
show("ln 4", np.log(4))
emf11 = -M11 * k11
show("emf (reference direction)", emf11 * 1e3, "mV -> -1.39 mV (down the near side)")
# force check of Lenz: near-side current antiparallel to wire -> repelled
Iw = np.array([0, 0, 1.0])
i_near = np.array([0, 0, -1.0])
Bnear = np.array([0, 1, 0])
F = np.cross(i_near, Bnear)
show("force direction on near side for current -z in B +y", F, "(+x: pushed away from wire)")
# net force on the whole loop with the induced circulation (down near side, +x along bottom,
# up far side, -x along top), per ampere of wire and loop current: sum of i dl x B over the 4 sides
Bw = lambda xx: mu0 / (2 * np.pi * xx) * np.array([0, 1.0, 0])
F_near = h11 * np.cross([0, 0, -1.0], Bw(d1))
F_far = h11 * np.cross([0, 0, 1.0], Bw(d2))
F_bot = np.array([integrate.quad(lambda xx, k=k: np.cross([1.0, 0, 0], Bw(xx))[k], d1, d2)[0] for k in range(3)])
F_top = np.array([integrate.quad(lambda xx, k=k: np.cross([-1.0, 0, 0], Bw(xx))[k], d1, d2)[0] for k in range(3)])
F_net = F_near + F_far + F_bot + F_top
show("net force on loop per (A wire x A loop)", F_net, "N -> along +x: repelled")
check("top and bottom forces cancel", F_bot + F_top, np.zeros(3), atol=1e-20)
check("net force = mu0 h/(2 pi) (1/d1 - 1/d2) xhat", F_net, [mu0 * h11 / (2 * np.pi) * (1 / d1 - 1 / d2), 0, 0])
# A-route: A_z = -(mu0 I / 2 pi) ln(r/r0)
for r0 in (1.0, 0.003, 7.5):
    Az = lambda r, I=1.0: -mu0 * I / (2 * np.pi) * np.log(r / r0)
    # line integral around loop: near side +z, top +x (A.dl = 0), far side -z, bottom -x (A.dl = 0)
    near = integrate.quad(lambda zz: Az(d1), 0, h11)[0]
    top = integrate.quad(lambda xx: 0.0 * Az(xx), d1, d2)[0]
    far = integrate.quad(lambda zz: -Az(d2), 0, h11)[0]
    bot = 0.0
    circ = near + top + far + bot
    check(f"r0={r0}: oint A.dl = Psi (per A)", circ, Psi11)
# also check B = curl A numerically for the wire's A
Aw = lambda x, y, z, t: np.array([0, 0, -mu0 * 1.0 / (2 * np.pi) * np.log(np.hypot(x, y) / 1.0)])
pp = (0.05, 0.03, 0.2, 0.0)
rr = np.hypot(pp[0], pp[1])
check("curl of wire A = mu0 I/(2 pi r) phi-hat", curl(Aw, *pp, h=1e-6),
      mu0 / (2 * np.pi * rr) * np.array([-pp[1], pp[0], 0]) / rr, rtol=1e-5)
dEz = mu0 / (2 * np.pi) * k11 * np.log(d1 / d2)     # E_z(d1) - E_z(d2), E = -dA/dt
show("E_z(near) - E_z(far)", dEz * 1e3, "mV/m -> -2.77 mV/m")
check("h [E_z(d1) - E_z(d2)] = emf", h11 * dEz, emf11)
# RL response of the closed loop
tau11 = Lloop / R11
show("tau = L_loop/R", tau11 * 1e3, "ms")
sol11 = integrate.solve_ivp(lambda t, y: [(-M11 * k11 - R11 * y[0]) / Lloop], [0, 3e-3], [0.0],
                            rtol=1e-11, atol=1e-14, dense_output=True)
i_inf = -M11 * k11 / R11
show("i_inf = -M k / R", i_inf, "A -> -0.277 A")
check("ODE i(1 ms) vs closed form", sol11.sol(1e-3)[0], i_inf * (1 - np.exp(-1e-3 / tau11)))
t1pc = optimize.brentq(lambda t: sol11.sol(t)[0] / i_inf - 0.99, 1e-6, 2.9e-3, xtol=1e-15)
show("time to reach 99% of emf/R", t1pc * 1e3, "ms -> 0.921 ms")
check("= tau ln 100", t1pc, tau11 * np.log(100))
# reciprocity (extra, not on the page): M from the Neumann double integral
#   M = (mu0/4pi) oint_wire oint_loop dl.dl'/R
# Only the loop's z-directed sides couple to the z-directed wire (closed at infinity); the near side
# (x = d1) is traversed +z, the far side (x = d2) -z, so the kernel is 1/R(d1) - 1/R(d2).
# FIX: the previous version evaluated A_z of each side as ln[(u2+sqrt(u2^2+x^2))/(u1+sqrt(u1^2+x^2))],
# which cancels catastrophically for zf >> h (u < 0) and gave a 3e-4 relative error. The bracket is
# now written without cancellation: 1/s1 - 1/s2 = (d2^2 - d1^2)/(s1 s2 (s1 + s2)).
# By hand: int_{-inf}^{inf} [1/s1 - 1/s2] du = 2 ln(d2/d1) for every z', so M = mu0 h ln(d2/d1)/(2 pi) exactly.
def kern(u):
    s1, s2 = np.hypot(u, d1), np.hypot(u, d2)
    return (d2**2 - d1**2) / (s1 * s2 * (s1 + s2))
check("int kern du over all u = 2 ln(d2/d1)",
      sum(integrate.quad(kern, lo, hi, epsabs=1e-14, epsrel=1e-12, limit=400)[0]
          for lo, hi in [(-np.inf, -1), (-1, 0), (0, 1), (1, np.inf)]), 2 * np.log(d2 / d1), rtol=1e-9)
inner = lambda zw: integrate.quad(lambda zp: kern(zp - zw), 0, h11, epsabs=1e-14, epsrel=1e-12, limit=200)[0]
M_neu = mu0 / (4 * np.pi) * sum(integrate.quad(inner, lo, hi, epsabs=1e-13, epsrel=1e-11, limit=400)[0]
                                for lo, hi in [(-np.inf, -10), (-10, 0), (0, h11), (h11, 10), (10, np.inf)])
check("reciprocity: Neumann double integral (wire closed at infinity) = M", M_neu, M11, rtol=1e-8)

# =============================================================================
head("15.12  Coax: solid inner conductor, magnetic sleeve, air; energy route and LC")
a12, c12, b12 = 1e-3, 2e-3, 4e-3
mu_s, eps_s = 4 * mu0, 4 * eps0
I12 = 1.0
H12 = lambda r: I12 * r / (2 * np.pi * a12**2) if r < a12 else (I12 / (2 * np.pi * r) if r < b12 else 0.0)
mu12 = lambda r: mu0 if r < a12 else (mu_s if r < c12 else mu0)
# continuity of H_phi at r = a and r = c
check("H_phi continuous at r=a", H12(a12 * (1 - 1e-12)), H12(a12 * (1 + 1e-12)), rtol=1e-9)
show("B jump at r=c (sleeve/air)", mu12(c12 * 0.999999) * H12(c12) / (mu12(c12 * 1.000001) * H12(c12)))
Wreg = []
for lo, hi in [(0, a12), (a12, c12), (c12, b12)]:
    Wreg.append(integrate.quad(lambda r: 0.5 * mu12(r) * H12(r)**2 * 2 * np.pi * r, lo, hi,
                               epsabs=1e-20, epsrel=1e-12)[0])
Lreg = [2 * Wr / I12**2 for Wr in Wreg]
show("W' per region at I = 1 A", Wreg, "J/m")
check("W'1 = mu0 I^2/16 pi", Wreg[0], mu0 / (16 * np.pi))
check("W'2 = (mu0 I^2/pi) ln 2", Wreg[1], mu0 / np.pi * np.log(2))
check("W'3 = (mu0 I^2/4 pi) ln 2", Wreg[2], mu0 / (4 * np.pi) * np.log(2))
show("L' per region (energy)", np.array(Lreg) * 1e9, "nH/m -> 50, 554.5, 138.6")
Ltot = sum(Lreg)
show("L' total", Ltot * 1e9, "nH/m -> 743 nH/m")
show("fractions", np.array(Lreg) / Ltot)
# flux route for a < r < b
Lext_flux = integrate.quad(lambda r: mu12(r) * H12(r), a12, b12, points=[c12], epsabs=1e-20, epsrel=1e-12)[0] / I12
check("external L' by flux = energy (a<r<b)", Lext_flux, Lreg[1] + Lreg[2])
check("external L' = 1e-6 ln 2", Lext_flux, 1e-6 * np.log(2))
show("external L'", Lext_flux * 1e6, "uH/m -> 0.693 uH/m")
# internal: naive flux vs weighted
naive = integrate.quad(lambda r: mu0 * H12(r), 0, a12)[0] / I12
wtd = integrate.quad(lambda r: (r / a12)**2 * mu0 * H12(r), 0, a12)[0] / I12
check("naive internal flux/I = mu0/4pi (twice too big)", naive, mu0 / (4 * np.pi))
check("weighted internal flux/I = mu0/8pi = energy", wtd, Lreg[0])
# capacitance: series layers, from V = int E dr with D = rho_l/(2 pi r)
eps12 = lambda r: eps_s if r < c12 else eps0
rho_l = 1e-9
V12 = integrate.quad(lambda r: rho_l / (2 * np.pi * eps12(r) * r), a12, b12, points=[c12], epsabs=1e-20, epsrel=1e-12)[0]
C12 = rho_l / V12
check("C' = 2 pi eps0/(1.25 ln 2)", C12, 2 * np.pi * eps0 / (1.25 * np.log(2)))
show("C'", C12 * 1e12, "pF/m -> 64.2 pF/m")
LC = Lext_flux * C12
show("L'_ext C'", LC, "s^2/m^2")
show("L'_ext C' / (mu0 eps0)", LC / (mu0 * eps0), "-> 4")
check("L'C' = 4 mu0 eps0", LC, 4 * mu0 * eps0)
show("sleeve mu eps / (mu0 eps0)", mu_s * eps_s / (mu0 * eps0))
show("1/sqrt(L'C')", 1 / np.sqrt(LC), "m/s -> c/2")
show("sleeve speed 1/sqrt(mu eps)", 1 / np.sqrt(mu_s * eps_s), "m/s -> c/4")
show("4 mu0 eps0", 4 * mu0 * eps0)
show("factors: L_ext/((mu0/2pi) ln2) and (2 pi eps0 / C')/ln2", [Lext_flux / (mu0 / (2 * np.pi) * np.log(2)),
                                                              2 * np.pi * eps0 / C12 / np.log(2)], "-> 5, 1.25")
# control: a uniform fill (same mu, eps in both layers) restores LC = mu eps
for mur_u, epr_u in [(1.0, 1.0), (4.0, 4.0)]:
    Lu = integrate.quad(lambda r: mur_u * mu0 / (2 * np.pi * r), a12, b12)[0]
    Cu = rho_l / integrate.quad(lambda r: rho_l / (2 * np.pi * epr_u * eps0 * r), a12, b12)[0]
    check(f"uniform fill mu_r = eps_r = {mur_u:g}: L'C' = mu eps", Lu * Cu, mur_u * epr_u * mu0 * eps0)

# =============================================================================
head("SUMMARY")
if FAILS:
    print("FAILURES:", FAILS)
else:
    print("All checks passed.")
