#!/usr/bin/env python3
"""Author's checks for practice/32-stubs-and-input-impedance.md: every number in the answers."""
import numpy as np
pi = np.pi; n = dict(p=0, f=0)
def chk(label, mine, want, tol=1e-6, atol=1e-9):
    ok = np.allclose(np.asarray(mine, complex), np.asarray(want, complex), rtol=tol, atol=atol)
    n["p" if ok else "f"] += 1
    a = np.asarray(mine); a = a.astype(complex) if np.iscomplexobj(a) else a.astype(float)
    print(("PASS " if ok else "FAIL ") + f"{label}: {np.round(a, 5)}")
zs = lambda Z0, bl: 1j * Z0 * np.tan(bl); zo = lambda Z0, bl: -1j * Z0 / np.tan(bl)
print("== 32.1"); chk("five stubs [ohm]", [zs(50, pi / 4), zs(50, 3 * pi / 4), zo(50, pi / 4), zo(50, pi / 3), zs(50, pi)], [50j, -50j, -50j, -28.8675j, 0], tol=1e-5, atol=1e-9)
print("== 32.2"); chk("(e) current a quarter wave from the input of a lambda/4 shorted stub, per V+ (Z0 = 1): 2 cos(0)", 2 * np.cos(0.0), 2)
print("== 32.3"); v, f = 2e8, 150e6; lam = v / f
chk("lambda [m], quarter wave [m], beta l of the 0.5 m stub / pi, its Z [ohm]", [lam, lam / 4, 2 * 0.5 / lam, zs(75, 2 * pi * 0.5 / lam)], [1.33333, 0.33333, 0.75, -75j], tol=1e-5)
print("== 32.4"); Z0, v, f, L = 100.0, 2e8, 100e6, 50e-9
X = 2 * pi * f * L; bl = np.arctan(X / Z0); beta = 2 * pi * f / v
chk("X [ohm], tan, beta l [rad], beta/pi, l [cm], L per metre [uH/m], estimate [cm], ratio", [X, X / Z0, bl, beta / pi, bl / beta * 100, Z0 / v * 1e6, L / (Z0 / v) * 100, (L / (Z0 / v)) / (bl / beta)],
    [31.416, 0.31416, 0.3044, 1, 9.69, 0.5, 10, 1.032], tol=1e-3)
print("== 32.5"); Z0, l, v = 50.0, 1.5, 2e8
H = lambda f: (lambda Zp: Zp / (50 + Zp))(1 / (1 / 50 + 1 / zs(Z0, 2 * pi * f * l / v)))
for f in (20e6, 50e6, 90e6):
    bl = 2 * pi * f * l / v; chk(f" H at {f/1e6:.0f} MHz vs 1/(2 - j cot); |H| vs 1/sqrt(4+cot^2)", [H(f), abs(H(f))], [1 / (2 - 1j / np.tan(bl)), 1 / np.sqrt(4 + 1 / np.tan(bl) ** 2)])
chk("nulls n v/2l [MHz]; peaks (2n+1) v/4l [MHz]; |H| at a peak; |H| at 50 MHz", [v / (2 * l) / 1e6, 2 * v / (2 * l) / 1e6, v / (4 * l) / 1e6, 3 * v / (4 * l) / 1e6, 5 * v / (4 * l) / 1e6, abs(H(v / (4 * l) * (1 + 1e-12))), abs(H(50e6))],
    [66.6667, 133.3333, 33.3333, 100, 166.6667, 0.5, 1 / np.sqrt(5)], tol=1e-5)
chk(" |H| at 66.67 MHz -> 0; 1/sqrt5", [abs(H(v / (2 * l) * (1 + 1e-10))), 1 / np.sqrt(5)], [0, 0.44721], tol=1e-4, atol=1e-6)
print("== 32.6"); Z0 = 50.0; bl = 1.5 * pi; Vp = 10 / (2j * np.sin(bl))
Vd = lambda bd: 2j * Vp * np.sin(bd); Id = lambda bd: 2 * Vp / Z0 * np.cos(bd)
chk("V+, V(l), I(l), I(0), V at lambda/4, lambda/2, power at input", [Vp, Vd(bl), Id(bl), Id(0), Vd(pi / 2), Vd(pi), 0.5 * np.real(Vd(bl) * np.conj(Id(bl)))], [5j, 10, 0, 0.2j, -10, 0, 0], atol=1e-9)
chk(" V(d) = -10 sin(bd), I(d) = j0.2 cos(bd) at bd = 0.7", [Vd(0.7), Id(0.7)], [-10 * np.sin(0.7), 0.2j * np.cos(0.7)])
print("== 32.7"); Z0, v, R, F = 50.0, 2.5e8, 75.0, 9.0; lam = v / 125e6
chk("lambda [m]; lengths [m]", [lam] + [(2 * k + 1) * lam / 4 for k in range(3)], [2, 0.5, 1.5, 2.5])
Vp = F / (2j * np.sin(pi / 2)); chk("V+, I through the short [A], V(d) at bd = 0.4 vs 9 sin", [Vp, 2 * Vp / Z0, 2j * Vp * np.sin(0.4)], [-4.5j, -0.18j, 9 * np.sin(0.4)])
bl = 1.5 * pi; chk("(d) l = 3 lambda/4 = 1.5 m: cos(beta l/3) = 0 and 1/tan(beta l) = 0; null at d [m]; next length [m]", [np.cos(bl / 3), 1 / np.tan(bl), 1.5 / 3, 4.5 * pi / (2 * pi) * lam], [0, 0, 0.5, 4.5], atol=1e-9)
others = [np.cos((2 * k + 1) * pi / 2 / 3) for k in (0, 2, 3)]; chk("    lengths lambda/4, 5 lambda/4, 7 lambda/4 do not work (|cos| > 0)", [abs(o) > 0.1 for o in others], [1, 1, 1])
lam2 = v / 250e6; Zin = zs(Z0, 2 * pi * 0.5 / lam2); chk("(e) lambda at 250 MHz [m], Z(l), I_R [A]", [lam2, Zin, F / (R + Zin)], [1, 0, 0.12], atol=1e-9)
print("== 32.8"); Z0, l, v = 50.0, 0.6, 3e8
chk("(a) v/2l, v/4l [MHz]", [v / (2 * l) / 1e6, v / (4 * l) / 1e6], [250, 125])
f1 = 62.5e6; bl = 2 * pi * f1 * l / v; C = 1 / (2 * pi * f1 * Z0 * np.tan(bl))
chk("(b) beta l/pi, stub X [ohm], C [pF]", [bl / pi, Z0 * np.tan(bl), C * 1e12], [0.25, 50, 50.93], tol=1e-3)
H = lambda f: 50 / (50 + 1 / (1j * 2 * pi * f * C) + zs(Z0, 2 * pi * f * l / v))
f2 = 31.25e6; Xs = Z0 * np.tan(2 * pi * f2 * l / v); Xc = -1 / (2 * pi * f2 * C)
chk("(c) |H| at 62.5 MHz (=1), 125 MHz, 1 Hz; (d) stub X, cap X, net, |H| at 31.25 MHz", [abs(H(f1)), abs(H(125e6 * (1 + 1e-10))), abs(H(1.0)), Xs, Xc, Xs + Xc, abs(H(f2))], [1, 0, 0, 20.71, -100, -79.29, 0.5334], tol=1e-3, atol=1e-6)
print(f"\nSUMMARY: {n['p']} PASS, {n['f']} FAIL")
