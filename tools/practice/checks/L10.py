#!/usr/bin/env python3
"""Verification script for practice/10-capacitance-and-conductance.md (Lecture 10).

numpy/scipy only. Every number, sign and direction quoted on the page is printed here.
Symbolic results are checked against brute-force numerics (solve_bvp Laplace solutions,
quad/dblquad integrals of E, J and 1/2 eps E^2, finite-difference derivatives,
solve_ivp time integrations) at the page's parameters AND at a second parameter set.
"""
import numpy as np
from scipy.integrate import quad, dblquad, solve_bvp, solve_ivp
from scipy.optimize import brentq

eps0 = 8.8541878128e-12
mu0 = 4e-7 * np.pi
e = 1.602176634e-19

FAILS = []


def check(name, a, b, rtol=1e-6, atol=0.0):
    ok = np.isclose(a, b, rtol=rtol, atol=atol)
    print(f"   [{'OK ' if ok else 'BAD'}] {name}: {a:.6g} vs {b:.6g}")
    if not ok:
        FAILS.append(name)


def p(label, val, unit="", scale=1.0, sf=3):
    v = val / scale
    print(f"   {label} = {v:.{sf}g} {unit}   (raw {val:.6e})")


def head(s):
    print("\n" + "=" * 78 + "\n" + s + "\n" + "=" * 78)


# ---------------------------------------------------------------- brute-force helpers
def laplace_radial_C(kind, a, b, eps, V0=1.0, L=1.0):
    """Given-V route: solve Laplace numerically (solve_bvp) between r=a (V0) and r=b (0),
    take rho_s = eps*E_r(a) on the inner conductor, Q = rho_s * area, C = Q/V0."""
    m = 1 if kind == "coax" else 2           # (1/r^m) d/dr (r^m dV/dr) = 0
    def f(r, y):
        return np.vstack([y[1], -m * y[1] / r])
    def bc(ya, yb):
        return np.array([ya[0] - V0, yb[0]])
    r = np.geomspace(a, b, 400)
    y0 = np.vstack([V0 * (b - r) / (b - a), -V0 / (b - a) * np.ones_like(r)])
    sol = solve_bvp(f, bc, r, y0, tol=1e-10, max_nodes=200000)
    Ea = -sol.sol(a)[1]
    rho_s = eps * Ea
    area = 2 * np.pi * a * L if kind == "coax" else 4 * np.pi * a**2
    return rho_s * area / V0


def gauss_route_C(kind, a, b, eps, Q=1e-9, L=1.0):
    """Given-Q route: Gauss gives E_r, integrate the drop numerically, C = Q/V."""
    if kind == "coax":
        Er = lambda r: Q / (2 * np.pi * eps * r * L)
    else:
        Er = lambda r: Q / (4 * np.pi * eps * r**2)
    V = quad(Er, a, b, limit=200)[0]
    return Q / V


# =============================================================================
head("10.1  Four capacitances by formula")
# (a) plates 10 cm x 10 cm, d = 0.5 mm, eps_r = 4
A, d, er = 0.10 * 0.10, 0.5e-3, 4.0
Ca = er * eps0 * A / d
p("(a) C = 80 eps0", Ca, "pF", 1e-12)
check("(a) 80 eps0", Ca, 80 * eps0)
# brute force for plates: solve V''=0 by solve_bvp, rho_s = eps*|dV/dx|
sol = solve_bvp(lambda x, y: np.vstack([y[1], 0 * y[1]]),
                lambda ya, yb: np.array([ya[0] - 1.0, yb[0]]),
                np.linspace(0, d, 50), np.zeros((2, 50)), tol=1e-12)
check("(a) plates given-V route", er * eps0 * (-sol.sol(0)[1]) * A / 1.0, Ca)
print("   (a) without eps_r (watch-out):", f"{eps0*A/d/1e-12:.3g} pF")
# (b) coax a = 0.375 mm, b = 1.5 mm, eps_r = 2.25, per unit length
a, b, er = 0.375e-3, 1.5e-3, 2.25
Cb = 2 * np.pi * er * eps0 / np.log(b / a)
print(f"   ln(b/a) = ln 4 = {np.log(b/a):.4f}")
p("(b) script C per metre", Cb, "pF/m", 1e-12)
check("(b) coax Laplace (solve_bvp) route", laplace_radial_C("coax", a, b, er * eps0), Cb, rtol=1e-6)
check("(b) coax Gauss route", gauss_route_C("coax", a, b, er * eps0), Cb, rtol=1e-8)
print(f"   (b) with log10 instead of ln (watch-out): {2*np.pi*er*eps0/np.log10(b/a)/1e-12:.3g} pF/m")
# (c) spheres 4 cm and 5 cm
a, b = 0.04, 0.05
Cc = 4 * np.pi * eps0 * a * b / (b - a)
print(f"   (c) ab/(b-a) = {a*b/(b-a):.3g} m")
p("(c) C spheres", Cc, "pF", 1e-12)
check("(c) spheres Laplace route", laplace_radial_C("sphere", a, b, eps0), Cc, rtol=1e-6)
check("(c) spheres Gauss route", gauss_route_C("sphere", a, b, eps0), Cc, rtol=1e-8)
# (d) isolated sphere a = 9 cm
a = 0.09
Cd = 4 * np.pi * eps0 * a
p("(d) C isolated sphere", Cd, "pF", 1e-12)
print(f"   (d) with 1/(4 pi eps0) = 9e9: C = {a/9e9/1e-12:.4g} pF")
Vinf = quad(lambda r: 1e-9 / (4 * np.pi * eps0 * r**2), a, np.inf)[0]
check("(d) isolated sphere, integrate E to infinity", 1e-9 / Vinf, Cd, rtol=1e-8)
# Earth
p("Earth (a = 6.37e6 m) C", 4 * np.pi * eps0 * 6.37e6, "uF", 1e-6)
# scaling: double every length
k = 2.0
print("   scaling x2: plates C ratio",
      (er * eps0 * (k * k * 0.01) / (k * d)) / (er * eps0 * 0.01 / d),
      "; spheres ratio", (4*np.pi*eps0*(k*0.04)*(k*0.05)/(k*0.01)) / Cc,
      "; coax script-C ratio", (2*np.pi*eps0/np.log(k*1.5e-3/(k*0.375e-3))) / (2*np.pi*eps0/np.log(4)))

# =============================================================================
head("10.2  Slide in a slab (fixed Q vs fixed V)")
for (C0, V0, er) in [(1e-9, 10.0, 4.0), (3.3e-10, 250.0, 4.0)]:
    print(f"  parameter set C0={C0}, V0={V0}, eps_r={er}")
    Q0 = C0 * V0
    W0 = 0.5 * C0 * V0**2
    # (i) battery disconnected: Q fixed
    C1 = er * C0
    V1 = Q0 / C1
    W1 = Q0**2 / (2 * C1)
    check("(i) V/V0 = 1/4", V1 / V0, 0.25)
    check("(i) W/W0 = 1/4 (falls, statement (c) false)", W1 / W0, 0.25)
    print(f"   (i) D/D0 = 1 (Q fixed); E/E0 = {V1/V0:.3g}")
    check("(i) mechanical work = (3/8) C0 V0^2", W0 - W1, 0.375 * C0 * V0**2)
    # (ii) battery connected: V fixed
    Q2 = C1 * V0
    W2 = 0.5 * C1 * V0**2
    Wbatt = (Q2 - Q0) * V0
    check("(ii) Q/Q0 = 4", Q2 / Q0, 4.0)
    check("(ii) W/W0 = 4", W2 / W0, 4.0)
    check("(ii) battery work = 3 C0 V0^2", Wbatt, 3 * C0 * V0**2)
    check("(ii) stored increase = 1.5 C0 V0^2", W2 - W0, 1.5 * C0 * V0**2)
    check("(ii) battery work / stored increase = 2", Wbatt / (W2 - W0), 2.0)
    check("(ii) work by field on slab = 1.5 C0 V0^2", Wbatt - (W2 - W0), 1.5 * C0 * V0**2)
    print(f"   Q0 = {Q0/1e-9:.4g} nC, W0 = {W0/1e-9:.4g} nJ; (i) V = {V1:.4g} V, W = {W1/1e-9:.4g} nJ, W0 - W = {(W0-W1)/1e-9:.4g} nJ")
    print(f"   (ii) Q = {Q2/1e-9:.4g} nC, dQ = {(Q2-Q0)/1e-9:.4g} nC, W = {W2/1e-9:.4g} nJ, battery work = {Wbatt/1e-9:.4g} nJ,"
          f" stored increase = {(W2-W0)/1e-9:.4g} nJ, work on slab = {(Wbatt-(W2-W0))/1e-9:.4g} nJ")
    # (iii) force on a partially inserted slab, both cases, finite differences
    # plates of length Lp along x, slab inserted a distance s: C(s) = C0*[er*s + (Lp - s)]/Lp
    Lp = 0.1
    Cs = lambda s: C0 * (er * s + (Lp - s)) / Lp
    h = 1e-7
    for s in [0.02, 0.05, 0.08]:
        FQ = -((Q0**2 / (2 * Cs(s + h))) - (Q0**2 / (2 * Cs(s - h)))) / (2 * h)   # -dW/ds at fixed Q
        FV = (0.5 * Cs(s + h) * V0**2 - 0.5 * Cs(s - h) * V0**2) / (2 * h)        # +dW/ds at fixed V
        print(f"   s={s}: F (fixed Q) = {FQ:.4e} N  (>0: pulled IN) ; F (fixed V) = {FV:.4e} N (>0: pulled IN)")
        assert FQ > 0 and FV > 0
        # same instantaneous charge -> same force
        Qs = Cs(s) * V0
        FQs = -((Qs**2 / (2 * Cs(s + h))) - (Qs**2 / (2 * Cs(s - h)))) / (2 * h)
        check("   same force at same instantaneous charge", FQs, FV, rtol=1e-5)
    # integrated force = mechanical work
    WmQ = quad(lambda s: Q0**2 / (2 * Cs(s)**2) * C0 * (er - 1) / Lp, 0, Lp)[0]
    WmV = quad(lambda s: 0.5 * V0**2 * C0 * (er - 1) / Lp, 0, Lp)[0]
    check("(i) integral of F ds = (3/8) C0 V0^2", WmQ, 0.375 * C0 * V0**2)
    check("(ii) integral of F ds = 1.5 C0 V0^2", WmV, 1.5 * C0 * V0**2)
print("   ANSWERS: (i) false = (c); (ii) false = (d); (iii) FALSE: slab pulled in, both cases")

# =============================================================================
head("10.3  Leakage of a long cable")
Cpm = 100e-12
er, sig = 2.25, 1.0e-14
eps = er * eps0
s_over_e = sig / eps
p("sigma/eps", s_over_e, "1/s", 1.0, 4)
Gpm = s_over_e * Cpm
p("script G = (sigma/eps) script C", Gpm, "S/m", 1.0, 4)
# brute force: b/a from script C, then integrate J around a circle
lnba = 2 * np.pi * eps / Cpm
print(f"   implied ln(b/a) = {lnba:.4f}, b/a = {np.exp(lnba):.4f}")
V = 1.0
for r in [1.1, 2.0, 3.0]:   # in units of a (a = 1 mm)
    a = 1e-3
    rr = r * a
    Jr = sig * V / (rr * lnba)
    I = quad(lambda phi: Jr * rr, 0, 2 * np.pi)[0]
    check(f"J-integral script G at r={r}a", I / V, Gpm, rtol=1e-10)
for ell in [1000.0, 2000.0]:
    G = Gpm * ell
    p(f"G({ell:.0f} m)", G, "S", 1.0, 4)
    p(f"R({ell:.0f} m)", 1 / G, "GOhm", 1e9, 4)
    p(f"C({ell:.0f} m)", Cpm * ell, "nF", 1e-9, 4)
    check(f"R C ({ell:.0f} m) = eps/sigma", (1 / G) * (Cpm * ell), eps / sig)
p("tau = eps/sigma (length independent)", eps / sig, "s", 1.0, 4)
p("tau in minutes", eps / sig / 60, "min", 1.0, 3)

# =============================================================================
head("10.4  Energy density in a dielectric (find the error)")
A, d, er, V = 0.04, 1e-3, 5.0, 50.0
E = V / d
p("E = V/d", E, "V/m")
p("volume A d", A * d, "m^3")
w_student = 0.5 * eps0 * E**2
w_right = 0.5 * er * eps0 * E**2
p("student w = 1/2 eps0 E^2", w_student, "J/m^3")
p("student W", w_student * A * d, "uJ", 1e-6)
p("correct w = 1/2 eps E^2", w_right, "J/m^3")
p("correct W", w_right * A * d, "uJ", 1e-6)
C = er * eps0 * A / d
print(f"   C = {er*A/d:.0f} eps0 = {C/1e-9:.4g} nF")
p("1/2 C V^2", 0.5 * C * V**2, "uJ", 1e-6)
# brute force: integrate 1/2 eps E^2 over the gap volume (x in 0..0.2, y in 0..0.2, z in 0..d)
Wnum = dblquad(lambda z, x: 0.5 * er * eps0 * E**2 * 0.2, 0, 0.2, 0, d)[0]
check("numerical volume integral of 1/2 eps E^2 = 1/2 C V^2", Wnum, 0.5 * C * V**2, rtol=1e-8)
check("student / correct = 1/eps_r", (w_student * A * d) / (0.5 * C * V**2), 1 / er)

# =============================================================================
head("10.5  Which capacitor leaks first")
eps, sig = 2 * eps0, 1.0e-13
tau = eps / sig
p("tau = eps/sigma", tau, "s", 1.0, 4)
p("t_half = tau ln2", tau * np.log(2), "s", 1.0, 4)
# (1) plates, C = 1 nF: geometry A/d = C/eps
C1 = 1e-9
Aod = C1 / eps
R1 = 1 / (sig * Aod)            # R = d/(sigma A)
p("(1) plates R", R1, "Ohm", 1.0, 4)
# (2) coax 100 m, script C = 100 pF/m
ell, Cpm = 100.0, 100e-12
lnba = 2 * np.pi * eps / Cpm
C2 = Cpm * ell
# R by integrating dr/(sigma 2 pi r ell) from a to b (a=1 mm)
a = 1e-3
R2 = quad(lambda r: 1 / (sig * 2 * np.pi * r * ell), a, a * np.exp(lnba))[0]
p("(2) coax C", C2, "nF", 1e-9, 4)
p("(2) coax R (shell integral)", R2, "Ohm", 1.0, 4)
# (3) sphere radius 1 m in infinite medium
a = 1.0
C3 = 4 * np.pi * eps * a
R3 = quad(lambda r: 1 / (sig * 4 * np.pi * r**2), a, np.inf)[0]
G3 = 1 / R3
p("(3) sphere C = 8 pi eps0", C3, "pF", 1e-12, 4)
p("(3) sphere G = 4 pi sigma a", G3, "S", 1.0, 4)
p("(3) sphere R", R3, "Ohm", 1.0, 4)
for nm, C, R in [("plates", C1, R1), ("coax", C2, R2), ("sphere", C3, R3)]:
    check(f"RC {nm} = eps/sigma", R * C, tau, rtol=1e-8)
    # time integration of C dV/dt = -V/R with event at half charge
    ev = lambda t, y: y[0] - 50.0
    ev.terminal = True
    sol = solve_ivp(lambda t, y: -y / (R * C), [0, 1000], [100.0], events=ev, rtol=1e-10, atol=1e-12)
    check(f"half-time from ODE ({nm})", sol.t_events[0][0], tau * np.log(2), rtol=1e-6)
print("   ANSWER (d): all three at the same moment")

# =============================================================================
head("10.6  Two layers between charged plates (Sum20 HE2 #1a re-parameterized)")
rho_s = 4e4 * eps0
d1, d2 = 1e-3, 2e-3
e1, e2 = 4 * eps0, eps0
p("rho_s = 4e4 eps0", rho_s, "uC/m^2", 1e-6, 3)
D = rho_s
E1, E2 = D / e1, D / e2
p("D (both layers, +z)", D, "C/m^2")
p("E1 (dielectric, +z)", E1, "V/m")
p("E2 (air, +z)", E2, "V/m")
P1, P2 = D - eps0 * E1, D - eps0 * E2
p("P1 = 3e4 eps0 (+z)", P1, "uC/m^2", 1e-6, 3)
print(f"   P1/eps0 = {P1/eps0:.6g} ; P2 = {P2:.3g}")
# potentials with V(3 mm) = 0, brute force with quad of -E along z
Ez = lambda z: E1 if z < d1 else E2
V_at = lambda z: quad(lambda zz: Ez(zz), z, d1 + d2, points=[d1], limit=200)[0]   # V(z)-V(3mm) = int_z^3mm E dz
p("V(1 mm)", V_at(d1), "V", 1.0, 4)
p("V(0)", V_at(0.0), "V", 1.0, 4)
CA = rho_s / V_at(0.0)
CA_series = 1 / (d1 / e1 + d2 / e2)
print(f"   d1/eps1 + d2/eps2 = ({d1/e1*eps0*1e3:.4g} + {d2/e2*eps0*1e3:.4g}) mm/eps0 = {(d1/e1 + d2/e2)*eps0:.4g} m/eps0")
print(f"   drop across dielectric V(0)-V(1mm) = {V_at(0.0)-V_at(d1):.4g} V ; across air = {V_at(d1):.4g} V")
p("C/A from Q/V", CA, "nF/m^2", 1e-9, 4)
print(f"   C/A in eps0 units = {CA/eps0:.6g}  (4000/9 = {4000/9:.6g})")
check("C/A series formula", CA_series, CA)
WA_circ = 0.5 * CA * V_at(0.0)**2
WA_field = quad(lambda z: 0.5 * (e1 if z < d1 else e2) * Ez(z)**2, 0, d1 + d2, points=[d1], limit=200)[0]
p("W/A = 1/2 (C/A) V^2", WA_circ, "uJ/m^2", 1e-6, 4)
print(f"   W/A in eps0 units = {WA_circ/eps0:.6g}")
check("W/A field integral", WA_field, WA_circ, rtol=1e-9)
Wd = 0.5 * e1 * E1**2 * d1
Wa = 0.5 * e2 * E2**2 * d2
print(f"   dielectric layer: {Wd/eps0:.6g} eps0 = {Wd/1e-6:.4g} uJ/m^2 ; air layer: {Wa/eps0:.6g} eps0 = {Wa/1e-6:.4g} uJ/m^2")
p("fraction in air", Wa / (Wa + Wd), "", 1.0, 4)
check("fraction in air = 8/9", Wa / (Wa + Wd), 8 / 9)
# checks: top plate charge, bound charges
print(f"   top plate rho_s = (-z).D = {-D:.4e} C/m^2 (= -rho_s)")
print(f"   bound: bottom face of dielectric P.(-z) = {-P1/eps0:.4g} eps0 ; top face P.(+z) = {P1/eps0:.4g} eps0")
check("eps0*(E2-E1) at interface = bound sheet", eps0 * (E2 - E1), P1)
# second parameter set for the series formula & energy two ways
for (rs, dd1, dd2, ee1, ee2) in [(2.0, 0.7e-3, 1.9e-3, 2.5 * eps0, 1.3 * eps0)]:
    EE1, EE2 = rs / ee1, rs / ee2
    Vt = EE1 * dd1 + EE2 * dd2
    check("2nd set: C/A series", rs / Vt, 1 / (dd1 / ee1 + dd2 / ee2))
    Wf = quad(lambda z: 0.5 * rs**2 / (ee1 if z < dd1 else ee2), 0, dd1 + dd2, points=[dd1])[0]
    check("2nd set: energy two ways", Wf, 0.5 * (rs / Vt) * Vt**2, rtol=1e-9)

# =============================================================================
head("10.7  One slab, two placements")
A, d, er, V = 0.01, 2e-3, 3.0, 100.0
C0 = eps0 * A / d
CS = 1 / ((d / 2) / (er * eps0 * A) + (d / 2) / (eps0 * A))
CP = er * eps0 * (A / 2) / d + eps0 * (A / 2) / d
p("C0 = 5 eps0", C0, "pF", 1e-12, 4)
p("C_S (stacked, series)", CS, "pF", 1e-12, 4)
p("C_P (side by side, parallel)", CP, "pF", 1e-12, 4)
check("C_S = 1.5 C0", CS / C0, 1.5)
check("C_P = 2 C0", CP / C0, 2.0)
for er_t in [1.0, 1.5, 3.0, 10.0, 81.0]:
    am, hm = (1 + er_t) / 2, 2 * er_t / (1 + er_t)
    check(f"   eps_r={er_t}: C_P - C_S = C0 (er-1)^2/(2(1+er))", am - hm, (er_t - 1)**2 / (2 * (1 + er_t)), atol=1e-14)
    # brute force: C from Q/V with D common (S) and E common (P)
    Dd = 1.0
    VS = Dd / (er_t * eps0) * d / 2 + Dd / eps0 * d / 2
    check(f"   eps_r={er_t}: series C via D-common", Dd * A / VS / C0, hm)
    EP = 1.0 / d
    QP = er_t * eps0 * EP * A / 2 + eps0 * EP * A / 2
    check(f"   eps_r={er_t}: parallel C via E-common", QP / 1.0 / C0, am)
# (c) fields at V = 100 V
QS = CS * V
DS = QS / A
p("S: Q", QS, "nC", 1e-9, 3)
p("S: D", DS, "C/m^2", 1.0, 4)
p("S: E in dielectric", DS / (er * eps0), "kV/m", 1e3, 4)
p("S: E in air", DS / eps0, "kV/m", 1e3, 4)
check("S: drops add to V", DS / (er * eps0) * d / 2 + DS / eps0 * d / 2, V)
print(f"   S: drop across dielectric = {DS/(er*eps0)*d/2:.4g} V, across air = {DS/eps0*d/2:.4g} V")
p("P: E both halves", V / d, "kV/m", 1e3, 4)
p("P: rho_s under dielectric", er * eps0 * V / d, "uC/m^2", 1e-6, 3)
p("P: rho_s under air", eps0 * V / d, "uC/m^2", 1e-6, 3)
p("empty capacitor E", V / d, "kV/m", 1e3, 3)
# (d) coax half by angle: integrate rho_s(phi) on inner conductor numerically
for (a, b, e1, e2, V0) in [(1e-3, 4e-3, 3 * eps0, eps0, 1.0), (0.7e-3, 5.3e-3, 2.2 * eps0, 4.1 * eps0, 3.0)]:
    lnba = np.log(b / a)
    # numerical Laplace (radial) in each half -> E_r(a); same in both halves
    Ca_num = laplace_radial_C("coax", a, b, 1.0, V0=V0)   # = 2 pi * 1 * ... per unit eps
    Er_a = Ca_num * V0 / (2 * np.pi * a)                 # E_r(a) from the numerical solution
    rho = lambda phi: (e1 if phi < np.pi else e2) * Er_a
    lam = quad(lambda phi: rho(phi) * a, 0, 2 * np.pi, points=[np.pi])[0]
    check(f"coax half-angle C (a={a},b={b})", lam / V0, np.pi * (e1 + e2) / lnba, rtol=1e-6)
    check("   = average of the two single-filled cables", np.pi * (e1 + e2) / lnba,
          0.5 * (2 * np.pi * e1 / lnba + 2 * np.pi * e2 / lnba))
a, b = 1e-3, 4e-3
p("coax half-angle C (3 eps0 | eps0, b/a = 4) = 4 pi eps0/ln4", np.pi * 4 * eps0 / np.log(4), "pF/m", 1e-12, 3)
print("   rho_s ratio on inner conductor (dielectric half : air half) = 3 : 1")

# =============================================================================
head("10.8  Diode junction capacitance")
eps = 11.7 * eps0
A = 1e-6
NA, ND = 1e23, 1e22
r1, r2 = e * NA, e * ND
p("rho1 = e N_A", r1, "C/m^3", 1.0, 4)
p("rho2 = e N_D", r2, "C/m^3", 1.0, 4)
p("1/rho1 + 1/rho2", 1 / r1 + 1 / r2, "m^3/C", 1.0, 3)
p("eps = 11.7 eps0", eps, "F/m", 1.0, 4)
print(f"   W1/W2 = rho2/rho1 = {r2/r1:.3g} ; fraction of width on n side = W2/(W1+W2) = {r1/(r1+r2):.4f} = 10/11")


def W_formula(V):
    return np.sqrt(2 * eps * V * (r1 + r2) / (r1 * r2))


def V_bruteforce(W2):
    """Total drop V(W2) - V(-W1) for given W2 by integrating the Poisson field numerically."""
    W1 = r2 * W2 / r1
    Ex = lambda x: (-r1 * (x + W1) / eps) if x < 0 else (r2 * (x - W2) / eps)
    return -quad(Ex, -W1, W2, points=[0.0], limit=200)[0]


def Q_bruteforce(V):
    W2 = brentq(lambda w: V_bruteforce(w) - V, 1e-12, 1e-4, xtol=1e-22, rtol=1e-14)
    return r2 * W2 * A, W2


for V in [1.0, 4.0]:
    W = W_formula(V)
    W1, W2 = W * r2 / (r1 + r2), W * r1 / (r1 + r2)
    Q = r2 * W2 * A
    C = eps * A / W
    print(f"  V = {V} V:")
    p("   W1+W2", W, "um", 1e-6, 4)
    p("   W1", W1, "um", 1e-6, 3)
    p("   W2", W2, "um", 1e-6, 3)
    p("   Q", Q, "nC", 1e-9, 3)
    p("   C = eps A/(W1+W2)", C, "pF", 1e-12, 4)
    Qb, W2b = Q_bruteforce(V)
    check("   Q from Poisson brute force", Qb, Q, rtol=1e-8)
    h = 1e-4 * V
    Cfd = (Q_bruteforce(V + h)[0] - Q_bruteforce(V - h)[0]) / (2 * h)
    check("   C = dQ/dV (finite difference of brute-force Q)", Cfd, C, rtol=1e-6)
    Clec = A * np.sqrt(eps * r1 * r2 / (2 * V * (r1 + r2)))
    check("   Lecture-10 formula A sqrt(eps r1 r2/(2V(r1+r2)))", Clec, C)
    p("   secant Q/V", Q / V, "pF", 1e-12, 4)
    check("   secant/slope = 2", (Q / V) / C, 2.0)
check("C(1V)/C(4V) = 2", (eps * A / W_formula(1.0)) / (eps * A / W_formula(4.0)), 2.0)

# =============================================================================
head("10.9  Leaky spheres, one lossy half (SP18 Exam 1 #5 re-parameterized)")


def spheres(a, b, V0, eps, sig, verbose):
    C = 4 * np.pi * eps * a * b / (b - a)
    Q = C * V0                      # on the OUTER shell (+); inner sphere carries -Q
    Er = lambda r: -Q / (4 * np.pi * eps * r**2)
    # V(r) consistent with V(a) = 0, V(b) = V0 (Laplace solution)
    Vr = lambda r: V0 * (1 / a - 1 / r) / (1 / a - 1 / b)
    # finite-difference checks: E = -dV/dr, Laplace (1/r^2)(r^2 V')' = 0
    for r in np.linspace(1.1 * a, 0.9 * b, 4):
        h = 1e-3 * a
        dV = (Vr(r + h) - Vr(r - h)) / (2 * h)
        d2V = (Vr(r + h) - 2 * Vr(r) + Vr(r - h)) / h**2
        lap = d2V + 2 * dV / r                      # spherical Laplacian of V(r)
        assert np.isclose(-dV, Er(r), rtol=1e-5), "E != -grad V"
        assert abs(lap) < 1e-5 * abs(2 * dV / r), "Laplace violated"
    print("   [OK ] finite differences: E = -dV/dr and (1/r^2)(r^2 V')' = 0 at 4 radii")
    # V(b)-V(a) = -int_a^b E_r dr
    dV = -quad(Er, a, b)[0]
    check("V(b)-V(a) from -int E dr = V0", dV, V0, rtol=1e-10)
    # Gauss: flux of eps E through sphere r = enclosed charge = -Q (inner sphere)
    r0 = 0.5 * (a + b)
    flux = dblquad(lambda th, ph: eps * Er(r0) * r0**2 * np.sin(th), 0, 2 * np.pi, 0, np.pi)[0]
    check("Gauss flux = -Q (inner sphere negative)", flux, -Q, rtol=1e-8)
    # current through lower hemisphere (theta from pi/2 to pi), outward, at two radii
    Is = []
    for rr in [1.2 * a, 0.5 * (a + b), 0.95 * b]:
        I = dblquad(lambda th, ph: sig * Er(rr) * rr**2 * np.sin(th), 0, 2 * np.pi, np.pi / 2, np.pi)[0]
        Is.append(I)
    for I in Is:
        check("outward current through lower hemisphere = -sigma Q/(2 eps)", I, -sig * Q / (2 * eps), rtol=1e-8)
    G = abs(Is[0]) / V0
    check("G = 2 pi sigma ab/(b-a)", G, 2 * np.pi * sig * a * b / (b - a), rtol=1e-8)
    check("G = (1/2)(sigma/eps) C", G, 0.5 * sig / eps * C, rtol=1e-8)
    tau = C / G
    check("tau = 2 eps/sigma", tau, 2 * eps / sig, rtol=1e-8)
    # discharge by ODE: dQ/dt = -(G/C) Q, half-time
    ev = lambda t, y: y[0] - 0.5 * Q
    ev.terminal = True
    sol = solve_ivp(lambda t, y: -G / C * y, [0, 100 * tau], [Q], events=ev, rtol=1e-11, atol=1e-30)
    check("half-time from ODE = tau ln 2", sol.t_events[0][0], tau * np.log(2), rtol=1e-6)
    if verbose:
        print(f"   ab/(b-a) = {a*b/(b-a):.4g} m ; V(r) = {V0/a/(1/a-1/b):.4g} - {V0/(1/a-1/b):.4g}/r V (r in m)")
        check("V(r) formula at a and b", Vr(a) + Vr(b), 0.0 + V0)
        p("C", C, "pF", 1e-12, 4)
        p("Q (outer shell +, inner -)", Q, "pC", 1e-12, 4)
        print(f"   E_r = -V0 ab/((b-a) r^2) = -({V0*a*b/(b-a):.4g}/r^2) V/m  -> inward (-r_hat)")
        p("E_r(a)", Er(a), "V/m", 1.0, 3)
        p("E_r(b)", Er(b), "V/m", 1.0, 3)
        p("I outward (any r0)", Is[0], "nA", 1e-9, 4)
        p("G", G, "nS", 1e-9, 4)
        p("R", 1 / G, "MOhm", 1e6, 4)
        p("(sigma/eps) C", sig / eps * C, "nS", 1e-9, 4)
        p("tau = 2 eps/sigma", tau, "ms", 1e-3, 4)
        p("t_half", tau * np.log(2), "ms", 1e-3, 4)
        p("power G V0^2", G * V0**2, "uW", 1e-6, 4)
        p("for comparison eps/sigma", eps / sig, "ms", 1e-3, 4)


spheres(0.01, 0.02, 100.0, 3 * eps0, 1e-8, True)
print("  second parameter set:")
spheres(0.013, 0.031, 37.0, 5.5 * eps0, 3.3e-7, False)
# Interface conditions at the flat interface z = 0 (theta = pi/2): E is tangential there
print("   at theta=pi/2: E = E_r r_hat is tangential to the plane z=0 -> D_n = J_n = 0 on both sides (no interface charge)")
print("   (a)(i) FALSE: inner sphere carries -Q ; (a)(ii) FALSE: E=0 inside because conductor in equilibrium")

# =============================================================================
head("10.10  Pulling capacitor plates apart")


def plates_pull(A, x1, x2, V0, verbose):
    C = lambda x: eps0 * A / x
    Q = C(x1) * V0
    W1 = 0.5 * C(x1) * V0**2
    # fixed Q
    Wq = lambda x: Q**2 / (2 * C(x))
    V2q = Q / C(x2)
    h = 1e-9
    FQ = -(Wq(x1 + h) - Wq(x1 - h)) / (2 * h)
    # direct route: Q times the field of the bottom plate alone (rho_s = -Q/A): -Q/(2 eps0 A) z_hat
    Fdirect = Q * (-Q / A) / (2 * eps0)
    check("F (fixed Q) = -dW/dx = Q * field of bottom plate", FQ, Fdirect, rtol=1e-6)
    Wyou_q = Wq(x2) - Wq(x1)
    Wint = quad(lambda x: -(-(Wq(x + h) - Wq(x - h)) / (2 * h)), x1, x2)[0]
    check("your work (fixed Q) = int F_you dx", Wint, Wyou_q, rtol=1e-6)
    print(f"   using the full gap field Q/(eps0 A) would give {2*abs(Fdirect):.4g} N (twice)")
    # fixed V
    Wv = lambda x: 0.5 * C(x) * V0**2
    Q2 = C(x2) * V0
    dQ = Q2 - Q
    Wbatt = V0 * dQ
    dW = Wv(x2) - Wv(x1)
    Wyou_v = dW - Wbatt
    FV = (Wv(x1 + h) - Wv(x1 - h)) / (2 * h)       # +dW/dx at fixed V
    check("F (fixed V) = +dW/dx = same as fixed Q at x1", FV, FQ, rtol=1e-6)
    Wint_v = quad(lambda x: eps0 * A * V0**2 / (2 * x**2), x1, x2)[0]
    check("your work (fixed V) = int eps0 A V^2/(2x^2) dx", Wint_v, Wyou_v, rtol=1e-9)
    check("battery absorbs twice the drop in stored energy", -Wbatt, -2 * dW, rtol=1e-12)
    if verbose:
        p("(a) C", C(x1), "pF", 1e-12, 4)
        p("(a) Q", Q, "nC", 1e-9, 4)
        p("(a) W", W1, "uJ", 1e-6, 4)
        print(f"   (a) in eps0 units: C = {C(x1)/eps0:.4g} eps0, Q = {Q/eps0:.4g} eps0, W = {W1/eps0:.4g} eps0")
        p("(b) V at x2", V2q, "V", 1.0, 4)
        p("(b) W at x2", Wq(x2), "uJ", 1e-6, 4)
        p("(b) your work", Wyou_q, "uJ", 1e-6, 4)
        p("(b) F_z (attractive, -z)", FQ, "mN", 1e-3, 4)
        print(f"   (b) F = W/x1 = {W1/x1*1e3:.4g} mN ; F * (x2-x1) = {abs(FQ)*(x2-x1)*1e6:.4g} uJ")
        p("(c) C at x2", C(x2), "pF", 1e-12, 4)
        p("(c) Q2", Q2, "nC", 1e-9, 4)
        p("(c) W2", Wv(x2), "uJ", 1e-6, 4)
        p("(c) dW", dW, "uJ", 1e-6, 4)
        p("(c) dQ", dQ, "nC", 1e-9, 4)
        p("(c) battery work V0 dQ (negative: energy INTO battery)", Wbatt, "uJ", 1e-6, 4)
        p("(c) your work", Wyou_v, "uJ", 1e-6, 4)
        p("(c) force at x2 (fixed V)", -eps0 * A * V0**2 / (2 * x2**2), "mN", 1e-3, 4)
        p("(d) F_z at x1 (fixed V)", FV, "mN", 1e-3, 4)


plates_pull(0.02, 1e-3, 3e-3, 500.0, True)
print("  second parameter set:")
plates_pull(0.0137, 0.4e-3, 2.9e-3, 73.0, False)

# =============================================================================
head("10.11  Two lossy layers in series")


def two_layers(A, d1, d2, e1, e2, s1, s2, V0, verbose):
    # steady state
    J = V0 / (d1 / s1 + d2 / s2)
    E1, E2 = J / s1, J / s2
    I = J * A
    G = I / V0
    D1, D2 = e1 * E1, e2 * E2
    rho_int = D2 - D1        # n_hat = -z (from layer 2 into layer 1): n.(D1 - D2) = D2z - D1z
    rho_bot = D1             # n = +z out of bottom plate
    rho_top = -D2            # n = -z out of top plate
    check("steady state: E1 d1 + E2 d2 = V0", E1 * d1 + E2 * d2, V0)
    check("interface charge = J (e2/s2 - e1/s1)", rho_int, J * (e2 / s2 - e1 / s1))
    check("total free charge (plates + interface) = 0", rho_bot + rho_int + rho_top, 0.0, atol=1e-20)
    # t = 0+: D common
    E1_0 = V0 / (d1 + d2 * e1 / e2)
    E2_0 = E1_0 * e1 / e2
    tau = (e1 / d1 + e2 / d2) / (s1 / d1 + s2 / d2)
    V1inf, V10 = E1 * d1, E1_0 * d1

    # brute force: continuity at interface d(rho)/dt = J1 - J2, with E1, E2 from (rho, V0)
    def fields(rho):
        M = np.array([[d1, d2], [-e1, e2]])
        return np.linalg.solve(M, np.array([V0, rho]))

    def rhs(t, y):
        f1, f2 = fields(y[0])
        return [s1 * f1 - s2 * f2]

    T = np.linspace(0, 6 * tau, 13)
    sol = solve_ivp(rhs, [0, 6 * tau], [0.0], t_eval=T, rtol=1e-11, atol=1e-22)
    for t, rho in zip(sol.t, sol.y[0]):
        V1_num = fields(rho)[0] * d1
        V1_formula = V1inf + (V10 - V1inf) * np.exp(-t / tau)
        if not np.isclose(V1_num, V1_formula, rtol=1e-7, atol=1e-9 * V0):
            FAILS.append("two-layer ODE")
            print("   BAD ODE at t =", t, V1_num, V1_formula)
    print("   [OK ] continuity ODE reproduces V1(t) = V1inf + (V1(0+) - V1inf) exp(-t/tau) at 13 times")
    check("ODE end state interface charge", solve_ivp(rhs, [0, 60 * tau], [0.0], rtol=1e-11, atol=1e-22).y[0][-1], rho_int,
          rtol=1e-6, atol=1e-18)
    # circuit model: C_i || G_i in series (per unit area)
    C1, C2, G1, G2 = e1 / d1, e2 / d2, s1 / d1, s2 / d2
    check("tau = (C1+C2)/(G1+G2)", tau, (C1 + C2) / (G1 + G2))
    check("V1inf = G2 V0/(G1+G2)", V1inf, G2 * V0 / (G1 + G2))
    check("V1(0+) = C2 V0/(C1+C2)", V10, C2 * V0 / (C1 + C2))
    if verbose:
        p("J (+z)", J, "A/m^2", 1.0, 4)
        p("E1 (+z)", E1, "V/m", 1.0, 4)
        p("E2 (+z)", E2, "V/m", 1.0, 4)
        p("V1inf (across layer 1)", V1inf, "V", 1.0, 4)
        p("V2inf (across layer 2)", E2 * d2, "V", 1.0, 4)
        p("I", I, "nA", 1e-9, 4)
        p("G", G, "nS", 1e-9, 4)
        p("R", 1 / G, "GOhm", 1e9, 4)
        p("R1 = d1/(s1 A)", d1 / (s1 * A), "GOhm", 1e9, 4)
        p("R2 = d2/(s2 A)", d2 / (s2 * A), "GOhm", 1e9, 4)
        print(f"   D1 = {D1/eps0:.6g} eps0 = {D1:.4e} C/m^2 ; D2 = {D2/eps0:.6g} eps0 = {D2:.4e} C/m^2 (+z)")
        print(f"   interface rho_s = {rho_int/eps0:.6g} eps0 = {rho_int:.4e} C/m^2")
        print(f"   bottom plate rho_s = {rho_bot/eps0:.6g} eps0 = {rho_bot:.4e} ; top plate = {rho_top/eps0:.6g} eps0 = {rho_top:.4e}")
        p("E1(0+)", E1_0, "V/m", 1.0, 4)
        p("E2(0+)", E2_0, "V/m", 1.0, 4)
        p("V1(0+)", V10, "V", 1.0, 4)
        p("V1(0+) - V1inf", V10 - V1inf, "V", 1.0, 3)
        p("J1(0+) = s1 E1(0+) arriving at interface", s1 * E1_0, "uA/m^2", 1e-6, 4)
        p("J2(0+) = s2 E2(0+) leaving interface", s2 * E2_0, "uA/m^2", 1e-6, 4)
        p("tau", tau, "s", 1.0, 4)
        p("layer relaxation e1/s1", e1 / s1, "ms", 1e-3, 4)
        p("layer relaxation e2/s2", e2 / s2, "ms", 1e-3, 4)
        Ctot = A / (d1 / e1 + d2 / e2)
        p("series C at t=0+ (whole plate)", Ctot, "pF", 1e-12, 4)
        print(f"   (sigma1/eps1) C = {s1/e1*Ctot:.4g} S, (sigma2/eps2) C = {s2/e2*Ctot:.4g} S, actual G = {G:.4g} S")


two_layers(0.01, 1e-3, 1e-3, 2 * eps0, 4 * eps0, 4e-10, 1e-10, 10.0, True)
print("  second parameter set (unequal thicknesses):")
two_layers(0.03, 0.6e-3, 1.7e-3, 3.1 * eps0, 1.4 * eps0, 2.2e-11, 7.5e-10, 37.0, False)
# matched ratios: no interface charge, no transient
print("  matched eps/sigma (no interface charge):")
two_layers(0.01, 1e-3, 1e-3, 2 * eps0, 4 * eps0, 2e-10, 4e-10, 10.0, False)

# =============================================================================
head("10.12  Lossy coax driven through a resistor (Sum19 HE2 #1 re-parameterized)")


def lossy_coax(a, b, ell, er, sig, Vs, Rs, Vend, verbose):
    eps = er * eps0
    lnba = np.log(b / a)
    Cpm = 2 * np.pi * eps / lnba
    # brute force script C: Laplace route
    check("script C via solve_bvp Laplace", laplace_radial_C("coax", a, b, eps), Cpm, rtol=1e-6)
    # brute force script G: integrate J over cylinders of two radii
    Vt = 1.0
    for r in [1.3 * a, 0.9 * b]:
        Jr = sig * Vt / (r * lnba)
        I = dblquad(lambda z, ph: Jr * r, 0, 2 * np.pi, 0, 1.0)[0]   # per metre
        check(f"script G via J integral at r={r:.3g}", I / Vt, 2 * np.pi * sig / lnba, rtol=1e-10)
    Gpm = 2 * np.pi * sig / lnba
    C, G = Cpm * ell, Gpm * ell
    R = 1 / G
    check("G/C = sigma/eps", Gpm / Cpm, sig / eps)
    # charging: C dV/dt = (Vs - V)/Rs - G V
    Rpar = R * Rs / (R + Rs)
    tau1 = C * Rpar
    Vinf = Vs * R / (R + Rs)
    ev = lambda t, y: y[0] - Vinf * (1 - np.exp(-1))
    ev.terminal = True
    sol = solve_ivp(lambda t, y: ((Vs - y) / Rs - G * y) / C, [0, 50 * tau1], [0.0], events=ev, rtol=1e-11, atol=1e-14)
    check("charging tau from ODE (63.2% point)", sol.t_events[0][0], tau1, rtol=1e-6)
    solinf = solve_ivp(lambda t, y: ((Vs - y) / Rs - G * y) / C, [0, 60 * tau1], [0.0], rtol=1e-11, atol=1e-14)
    check("steady-state V from ODE", solinf.y[0][-1], Vinf, rtol=1e-8)
    # energy per metre two ways
    Wp_circ = 0.5 * Cpm * Vinf**2
    Wp_field = quad(lambda r: 0.5 * eps * (Vinf / (r * lnba))**2 * 2 * np.pi * r, a, b)[0]
    check("energy per metre: field integral = 1/2 C' V^2", Wp_field, Wp_circ, rtol=1e-10)
    Wc = lambda c: quad(lambda r: 0.5 * eps * (Vinf / (r * lnba))**2 * 2 * np.pi * r, a, c)[0]
    chalf = brentq(lambda c: Wc(c) - 0.5 * Wp_field, a * 1.0000001, b * 0.9999999, xtol=1e-15)
    check("half-energy radius = sqrt(ab)", chalf, np.sqrt(a * b), rtol=1e-8)
    # discharge after disconnect: C dV/dt = -G V
    tau2 = C / G
    ev2 = lambda t, y: y[0] - Vend
    ev2.terminal = True
    sol2 = solve_ivp(lambda t, y: -G / C * y, [0, 100 * tau2], [Vinf], events=ev2, rtol=1e-11, atol=1e-14)
    check("discharge tau = eps/sigma", tau2, eps / sig)
    check("time to Vend from ODE", sol2.t_events[0][0], tau2 * np.log(Vinf / Vend), rtol=1e-6)
    if verbose:
        print(f"   ln(b/a) = {lnba:.4f}")
        p("(a) script C", Cpm, "pF/m", 1e-12, 4)
        p("(a) script G", Gpm, "nS/m", 1e-9, 4)
        p("(a) C", C, "nF", 1e-9, 4)
        p("(a) G", G, "nS", 1e-9, 4)
        p("(a) R", R, "MOhm", 1e6, 4)
        p("(a) sigma/eps", sig / eps, "1/s", 1.0, 4)
        p("(b) R || Rs", Rpar, "MOhm", 1e6, 4)
        p("(b) tau charging", tau1, "ms", 1e-3, 4)
        p("(b) V_inf", Vinf, "V", 1.0, 4)
        p("(b) steady leakage current G V_inf", G * Vinf, "uA", 1e-6, 4)
        check("(b) source current (Vs - Vinf)/Rs = G Vinf", (Vs - Vinf) / Rs, G * Vinf)
        p("(c) W' = 1/2 C' Vinf^2", Wp_circ, "nJ/m", 1e-9, 4)
        p("(c) W total", 0.5 * C * Vinf**2, "nJ", 1e-9, 4)
        p("(c) half-energy radius sqrt(ab)", chalf, "mm", 1e-3, 4)
        print(f"   (c) area fraction of a<r<sqrt(ab): {(chalf**2 - a**2)/(b**2 - a**2):.4g}")
        p("(d) tau discharge = eps/sigma", tau2, "ms", 1e-3, 4)
        p("(d) ln(Vinf/1V)", np.log(Vinf / Vend), "", 1.0, 4)
        p("(d) time to 1 V", sol2.t_events[0][0], "ms", 1e-3, 4)
        p("steady leakage power V^2 G", Vinf**2 * G, "uW", 1e-6, 3)


lossy_coax(1e-3, 4e-3, 10.0, 2.5, 1e-9, 12.0, 10e6, 1.0, True)
print("  second parameter set:")
lossy_coax(0.6e-3, 3.1e-3, 3.7, 3.3, 4.4e-8, 7.0, 2.2e6, 0.5, False)

# =============================================================================
print("\n" + "=" * 78)
print("ALL CHECKS PASSED" if not FAILS else f"FAILURES: {FAILS}")
