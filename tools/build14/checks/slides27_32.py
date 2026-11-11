#!/usr/bin/env python3
"""Numbers added to the site from the slide decks synced on Nov 10-11: Lecture 30 (multi-line circuits, annotated),
the annotated Lecture 27 and 29 decks, and Lectures 31-32 (stubs, resonators).
Bounce-diagram results are checked with tlsim.py (Kirchhoff at the nodes, no reflection coefficients)."""
import os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tlsim import simulate
pi = np.pi; n = dict(p=0, f=0)
def chk(label, mine, want, tol=1e-6, atol=1e-9):
    ok = np.allclose(np.asarray(mine, complex), np.asarray(want, complex), rtol=tol, atol=atol)
    n["p" if ok else "f"] += 1
    a = np.asarray(mine); a = a.astype(complex) if np.iscomplexobj(a) else a.astype(float)
    print(("PASS " if ok else "FAIL ") + f"{label}: {np.round(a, 5)}")
def val(r, node, t): return r["Vnode"][node][int(round(t / (r["t"][1] - r["t"][0])))]
print("== L30 slides 3-6: coefficients and power, Z01 = 50, Z02 = 100")
Z1, Z2 = 50.0, 100.0; G = (Z2 - Z1) / (Z2 + Z1)
A = np.array([[1, -1], [1 / Z1, 1 / Z2]]); Vm, Vpp = np.linalg.solve(A, [-1, 1 / Z1])     # V+ = 1: V+ + V- = V++, (V+ - V-)/Z1 = V++/Z2
chk("Gamma, tau from the two boundary equations vs (Z02-Z01)/(Z02+Z01), 1+Gamma", [Vm, Vpp], [G, 1 + G])
chk("current: Gamma_c = -Gamma, tau_c = 1 - Gamma (I++/I+)", [-Vm, (Vpp / Z2) / (1 / Z1)], [-G, 1 - G])
chk("power: reflected/incident = Gamma^2, transmitted/incident = 1 - Gamma^2", [Vm ** 2, Vpp ** 2 / Z2 * Z1], [G ** 2, 1 - G ** 2])
print("== L30 slide 8: one line into two equal lines")
Z0 = 50.0; Zeq = Z0 / 2; Gs = (Zeq - Z0) / (Zeq + Z0)
chk("Gamma, reflected fraction, total transmitted, per line", [Gs, Gs ** 2, 1 - Gs ** 2, (1 + Gs) ** 2], [-1 / 3, 1 / 9, 8 / 9, 4 / 9])
print("== L30 slides 9-16: Example 1, impulse through 50 / 100 / 50 ohm lines, 2 us each, 50 ohm ends")
dt = 1e-7
r = simulate([(50.0, 2e-6), (100.0, 2e-6), (50.0, 2e-6)], 50.0, 50.0, lambda t: 1.0 if t < dt / 2 else 0.0, 16e-6, dt)
chk("load (z = end): weights at 6, 10, 14 us", [val(r, 3, 6e-6), val(r, 3, 10e-6), val(r, 3, 14e-6)], [4 / 9, 4 / 81, 4 / 729])
chk("generator end: 0, 4, 8, 12 us", [val(r, 0, 0), val(r, 0, 4e-6), val(r, 0, 8e-6), val(r, 0, 12e-6)], [0.5, 1 / 6, -4 / 27, -4 / 243])
# waves on line 2 just after 2, 4, 6, 8 us: use node 1 and node 2 voltages (sum of arriving and departing waves there)
chk("junction 1 at 2 us (= tau 0.5 = 2/3), junction 2 at 4 us (= 4/9), junction 1 at 6 us (= -2/9 + 2/27 = -4/27), junction 2 at 8 us (= 4/81)",
    [val(r, 1, 2e-6), val(r, 2, 4e-6), val(r, 1, 6e-6), val(r, 2, 8e-6)], [2 / 3, 4 / 9, -4 / 27, 4 / 81])
chk("slide decimals: 1/6, 2/3, -2/9, 4/9, -4/27, 2/27, -2/81, 4/81", [1 / 6, 2 / 3, -2 / 9, 4 / 9, -4 / 27, 2 / 27, -2 / 81, 4 / 81], [0.17, 0.67, -0.22, 0.444, -0.15, 0.074, -0.025, 0.049], tol=3e-2)
chk("sum of the load weights = DC divider 1/2; I+ = 0.5/50 [A]", [(4 / 9) / (1 - 1 / 9), 0.5 / 50], [0.5, 0.01])
print("== L30 slides 17-19: Example 2 with this site's numbers Z01 = Z02 = 50, R1 = 100 (shunt), R2 = 50 (series)")
Z01 = Z02 = 50.0; R1, R2 = 100.0, 50.0
Req = R1 * (R2 + Z02) / (R1 + R2 + Z02); G2 = (Req - Z01) / (Req + Z01); Vt = (1 + G2) * Z02 / (R2 + Z02)
# direct nodal solve: node voltage Vn; incident wave 1 V as a Thevenin source 2 V behind Z01
Vn = (2 / Z01) / (1 / Z01 + 1 / R1 + 1 / (R2 + Z02)); Vline2 = Vn * Z02 / (R2 + Z02)
chk("R_eq, Gamma, V_trans/V+ (formulas) vs nodal solve (Vn - 1, V on line 2); power into line 2", [Req, G2, Vt, Vn - 1, Vline2, Vline2 ** 2], [50, 0, 0.5, 0, 0.5, 0.25])
print("== L30 slides 20-23: Example 3, reflectometry")
dt = 1e-11
r = simulate([(50.0, 1e-9), (150.0, 1.5e-9)], 50.0, 0.0, lambda t: 1.0 if t < dt / 2 else 0.0, 9e-9, dt)
chk("record at z = 0: t = 0, 2 ns, 5 ns, 8 ns [V]", [val(r, 0, 0), val(r, 0, 2e-9), val(r, 0, 5e-9), val(r, 0, 8e-9)], [0.5, 0.25, -0.375, -0.1875])
chk("Z02 from Gamma = 1/2; tau12, tau21; far-end Gamma; T02 [ns]; line-2 length and fault position [m]", [50 * 1.5 / 0.5, 1.5, 0.5, (-0.375 / 0.5) / 0.75, (4 - 1) / 2, 1.5e-9 * 1e8, 0.1 + 0.15], [150, 1.5, 0.5, -1, 1.5, 0.15, 0.25])
print("== L29 slide 14 as corrected in class: f_i = u(t) - u(t - 4 us); Z0 = 50, Rg = 0, RL = 100, l = 2400 m, v = c")
dt = 1e-7
r = simulate([(50.0, 4e-6), (50.0, 4e-6)], 0.0, 100.0, lambda t: 1.0 if t < 4e-6 - dt / 2 else 0.0, 42e-6, dt)
mid = lambda t: val(r, 1, t)
chk("V(1200 m, t) at 6, 10, 14, 18, 22, 26, 30, 34, 38 us", [mid(t * 1e-6) for t in (6, 10, 14, 18, 22, 26, 30, 34, 38)], [1, 0, 1 / 3, 0, -1 / 3, 0, -1 / 9, 0, 1 / 9])
chk("L29 slide 5 challenge: I(L, inf) = 30/(20+30) [A]; slide 12: steady V and I for u(t) with Rg = 0, RL = 100", [30 / 50, 1.0, 1 / 100], [0.6, 1, 0.01])
print("== L27 slide 9 (ink): d = 1 cm, w = 20 cm, eps_r = 2.25")
eta = 120 * pi / 1.5; Z0 = eta * 0.01 / 0.2
chk("eta/pi, Z0/pi; (a) H, P/pi; (b) E/pi, P/pi; (c) I, P/pi; (d) V/pi, P/pi", [eta / pi, Z0 / pi, 300 * pi / eta, 300 * pi * (300 * pi / eta) * 0.002 / pi, 7.5 * eta / pi, 7.5 * eta * 7.5 * 0.002 / pi, 4 * pi / Z0, 4 * pi * (4 * pi / Z0) / pi, 0.5 * Z0 / pi, 0.5 ** 2 * Z0 / pi],
    [80, 4, 3.75, 2.25, 600, 9, 1, 4, 2, 1])
print("== L31 slides: power on a shorted line; the resonance example")
bd, wt, th, Y0, Vp = 0.83, 1.9, 0.4, 1 / 50, 3.0
V = -2 * Vp * np.sin(bd) * np.sin(wt + th); I = 2 * Y0 * Vp * np.cos(bd) * np.cos(wt + th)
chk("P(d,t) = V I = -Y0 |V+|^2 sin(2 beta d) sin(2(wt + theta))", V * I, -Y0 * Vp ** 2 * np.sin(2 * bd) * np.sin(2 * (wt + th)))
chk("V(d,t) = Re{2j V+ sin(bd) e^{j(wt+th)}} = -2|V+| sin(bd) sin(wt+th)", np.real(2j * Vp * np.sin(bd) * np.exp(1j * (wt + th))), V)
l = 1.0; vp = 2e8
chk("open-short stub: lambda_n = 4l/(2n+1), f_n = (2n+1) v/4l for n = 0, 1, 2 [m, MHz]", [4 * l / (2 * k + 1) for k in range(3)] + [(2 * k + 1) * vp / (4 * l) / 1e6 for k in range(3)], [4, 4 / 3, 0.8, 50, 150, 250])
print("== L32 slides: Examples 1 and 4, and the fault-finding example")
c = 3e8
chk("Ex 1a: shorted load, v = c, l = 3 m: parallel resonances [MHz]", [(2 * k + 1) * c / 12 / 1e6 for k in range(3)], [25, 75, 125])
chk("Ex 1b: 10 m, open-open, v = 2c/3: n v/2l [MHz]", [k * (2 * c / 3) / 20 / 1e6 for k in (1, 2, 3)], [10, 20, 30])
v = 1e8; w = pi * 1e8; lam = v / (w / (2 * pi)); beta = 2 * pi / lam; Z0 = 50.0
def stub(l):                                   # open stub of length l across 50 ohm and a 2 A source: returns I_R, V+ (V(d) = 2V+ cos(beta d))
    Zin = -1j * Z0 / np.tan(beta * l) if abs(np.sin(beta * l)) > 1e-12 else np.inf
    Vl = 2 / (1 / 50 + (0 if np.isinf(Zin) else 1 / Zin)); return Vl / 50, Vl / (2 * np.cos(beta * l)) if abs(np.cos(beta * l)) > 1e-12 else None
IR, Vp = stub(lam / 2)
chk("Ex 4: lambda [m]; l = lambda/2 = 1 m: I_R [A], V(l) [V], V(l/2) [V], I(l/2) [A]", [lam, IR, 2 * Vp * np.cos(beta * lam / 2), 2 * Vp * np.cos(beta * lam / 4), 2j * Vp / Z0 * np.sin(beta * lam / 4)], [2, 2, 100, 0, -2j], atol=1e-9)
IR, Vp = stub(lam); chk(" l = lambda = 2 m: I_R [A], I(l/2) [A]", [IR, 2j * Vp / Z0 * np.sin(beta * lam / 2)], [2, 0], atol=1e-9)
Zq = -1j * Z0 / np.tan(beta * lam / 4); chk(" l = lambda/4 = 0.5 m: Z(l) -> 0, so I_R = 0", [abs(Zq), 2 * abs(Zq) / (50 + abs(Zq))], [0, 0], atol=1e-9)
lf = 37.5; vf = 2e8; f1 = vf / (4 * lf)
chk("fault finding: shorted line 37.5 m, v = 2e8: lowest zero-current frequency [MHz], spacing of the zeros [MHz], l recovered [m]", [f1 / 1e6, vf / (2 * lf) / 1e6, vf / (4 * f1)], [4 / 3, 8 / 3, 37.5])
print(f"\nSUMMARY: {n['p']} PASS, {n['f']} FAIL")
