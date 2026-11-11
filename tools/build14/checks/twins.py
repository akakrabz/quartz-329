#!/usr/bin/env python3
"""Build 14, author's check: every number in the new worked twins (content/exams/e3-steady-state-lines.md
S1-S5, content/exams/e3-summer-hour-exams.md T6) and the numbers quoted on the Midterm 3 summary."""
import numpy as np
pi = np.pi; c = 3e8; mu0 = 4e-7 * pi; eps0 = 1e-9 / (36 * pi); eta0 = 120 * pi
X, Y, Z = np.eye(3); n = dict(p=0, f=0)
def chk(label, mine, want, tol=1e-6):
    ok = np.allclose(np.asarray(mine, complex), np.asarray(want, complex), rtol=tol, atol=1e-9)
    n["p" if ok else "f"] += 1; print(("PASS " if ok else "FAIL ") + f"{label}: {np.round(np.asarray(mine), 5)}")
def zline(Z0, ZL, bd):
    if np.isinf(ZL): return -1j * Z0 / np.tan(bd)
    return Z0 * (ZL + 1j * Z0 * np.tan(bd)) / (Z0 + 1j * ZL * np.tan(bd))
print("== S1 open stub in series with R: Z0 = 75, v = 2.4e8, f = 60 MHz, R = 150, F = 6 V")
v = 2.4e8; f = 60e6; lam = v / f; b = 2 * pi / lam
chk("lambda [m]", lam, 4); chk("1/Z(l) at l = lambda/2 (open stub) -> 0", 1 / zline(75, np.inf, b * 2 + 1e-9), 0, tol=1e-6)
chk("lengths with I_R = 0: n lambda/2 [m]", [k * lam / 2 for k in (1, 2, 3)], [2, 4, 6])
Vp = -6 / 2            # V(l) = 2 V+ cos(beta l) = 6 with beta l = pi
chk("open-end voltage V(0) = 2V+ [V]; voltage null at d [m]; max |I| [mA]", [2 * Vp, lam / 4, abs(2 * Vp) / 75 * 1e3], [-6, 1, 80])
b30 = 2 * pi * 30e6 / v; Zin = zline(75, np.inf, b30 * 2)
chk("at 30 MHz: Z(l) [ohm], I_R [mA]", [Zin, 6 / (150 + Zin) * 1e3], [0, 40], tol=1e-6)
print("== S2 quarter-wave section: Z0 = 60, ZL = 20, Vg = 12 V, Rg = 60")
Zin = zline(60, 20, pi / 2 - 1e-12); Vin = 12 * Zin / (Zin + 60); Iin = 12 / (Zin + 60)
IL = -1j * Vin / 60; VL = IL * 20
chk("Z_in, V_in, I_in [A], I_L [A], V_L [V]", [Zin, Vin, Iin, IL, VL], [180, 9, 0.05, -0.15j, -3j], tol=1e-6)
chk("V_L = -j Z0 I_in; P_in, P_L [W]", [-1j * 60 * Iin, 0.5 * np.real(Vin * np.conj(Iin)), 0.5 * abs(IL) ** 2 * 20], [-3j, 0.225, 0.225], tol=1e-6)
Zh = zline(60, 20, pi); Vh = 12 * Zh / (Zh + 60)
chk("half-wave instead: Z_in, V_in, V_L, P [W]; matched maximum [W]", [Zh, Vh, -Vh, 0.5 * abs(Vh) ** 2 / 20, 144 / (8 * 60)], [20, 3, -3, 0.225, 0.3], tol=1e-6)
print("== S3 resonances: l = 60 m, v = 1.5e8")
l = 60.0; v = 1.5e8
chk("open-open f_n [MHz]", [k * v / (2 * l) / 1e6 for k in (1, 2, 3)], [1.25, 2.5, 3.75]); chk("short-open f_n [MHz]", [(2 * k - 1) * v / (4 * l) / 1e6 for k in (1, 2, 3)], [0.625, 1.875, 3.125])
lam2 = v / 2.5e6; chk("second open-open resonance: lambda [m], voltage nulls [m], current nulls [m]", [lam2, lam2 / 4, 3 * lam2 / 4, 0, lam2 / 2, lam2], [60, 15, 45, 0, 30, 60])
chk("Z(d) of the open-ended line at d = lambda/4 -> 0", zline(50, np.inf, pi / 2), 0)
print("== S4 open stub, lowest series resonance at w0 (beta l = pi/2 there)")
for r, want in ((0.5, -1j), (1.5, 1j), (3.0, 0)):
    chk(f"Z_in/Z0 at {r} w0", zline(1, np.inf, pi / 2 * r), want, tol=1e-6)
chk("1/Z_in at 2 w0 -> 0 (parallel resonance)", 1 / zline(1, np.inf, pi - 1e-13), 0, tol=1e-6)
bd = 0.7; chk("open load: V(d)/V+ = 2cos(bd), I(d) Z0/V+ = 2j sin(bd)", [np.exp(1j * bd) + np.exp(-1j * bd), np.exp(1j * bd) - np.exp(-1j * bd)], [2 * np.cos(bd), 2j * np.sin(bd)])
print("== S5 generalized reflection coefficient: Z0 = 50, ZL = 150")
GL = (150 - 50) / (150 + 50); G = lambda d_over_lam: GL * np.exp(-2j * 2 * pi * d_over_lam)
chk("Gamma_L, Gamma(lambda/8), Gamma(lambda/4), Gamma(lambda/2)", [GL, G(1 / 8), G(1 / 4), G(1 / 2)], [0.5, -0.5j, -0.5, 0.5])
chk("Z(lambda/4) = Z0 (1+G)/(1-G) = Z0^2/ZL [ohm]; VSWR", [50 * (1 + G(0.25)) / (1 - G(0.25)), (1 + GL) / (1 - GL)], [2500 / 150, 3])
print("== T6 sheet on x = 0, Js = -z 3 u(t) sin(2 pi f t), f = 1.5 MHz, eps_r = 4")
v = c / 2; eta = eta0 / 2; f = 1.5e6
chk("v [m/us], eta/pi, T [us], lambda [m], E amplitude/pi [V/m], H amplitude [A/m]", [v / 1e6, eta / pi, 1e6 / f, v / f, eta / 2 * 3 / pi, 1.5], [150, 60, 2 / 3, 100, 90, 1.5])
chk("E = -(eta/2) Js is along +z; H(x>0) along Js x x_hat = -y; H(x<0) along +y; E x H (x>0) along +x", [*(-(-Z)), *np.cross(-Z, X), *np.cross(-Z, -X), *np.cross(Z, -Y)], [0, 0, 1, 0, -1, 0, 0, 1, 0, 1, 0, 0])
chk("arrival at 300 m [us]; front at 3 us [m]; wavelengths behind the front", [300 / 150, 150 * 3, 450 / 100], [2, 450, 4.5])
xs = np.array([25.0, 75.0, 440.0]); chk("H_y(x, 3 us) = -1.5 sin(2 pi x/100): samples at 25, 75, 440 m", -1.5 * np.sin(2 * pi * f * (3e-6 - xs / v)), -1.5 * np.sin(2 * pi * xs / 100))
chk("E_z(300 m, t) just after arrival is positive: sample at 2.1 us [V/m]", 90 * pi * np.sin(2 * pi * f * (2.1e-6 - 2e-6)), 90 * pi * np.sin(0.3 * pi))
chk("<S> per side [W/m^2] = 67.5 pi; <Js.E> [W/m^2] = -135 pi", [eta * 9 / 8, -eta * 9 / 4], [67.5 * pi, -135 * pi])
print(f"      E amplitude = {90 * pi:.1f} V/m, <S> = {67.5 * pi:.1f} W/m^2, <Js.E> = {-135 * pi:.1f} W/m^2")
print("== numbers quoted on the Midterm 3 summary")
chk("dB per neper (field) 20 log10(e)", 20 * np.log10(np.e), 8.686, tol=1e-4); chk("power after one delta e^-2", np.exp(-2), 0.1353, tol=1e-3)
chk("seawater crossover sigma/(2 pi eps) [MHz], sigma = 4, eps_r = 81", 4 / (2 * pi * 81 * eps0) / 1e6, 888.9, tol=1e-3)
chk("copper delta at 60 Hz [mm], sigma = 5.8e7", 1e3 / np.sqrt(pi * 60 * mu0 * 5.8e7), 8.53, tol=2e-3)
chk("glass eps_r = 4 from air: Gamma, tau, reflected and transmitted power fractions", [(60 - 120) / 180, 1 - 1 / 3, 1 / 9, 8 / 9], [-1 / 3, 2 / 3, (1 / 3) ** 2, (2 / 3) ** 2 * 120 / 60])
chk("radiation pressure of 1 kW/m^2 on a perfect mirror [uPa] = 2<S>/c", 2 * 1e3 / c * 1e6, 6.667, tol=1e-3)
chk("bounce example Z0 = 50, Rg = 25, RL = 100, 9 V step: tau_g, Gamma_L, Gamma_g, V1+, steady V [V]", [50 / 75, 50 / 150, -25 / 75, 6, 9 * 100 / 125], [2 / 3, 1 / 3, -1 / 3, 6, 7.2])
print(f"\nSUMMARY: {n['p']} PASS, {n['f']} FAIL")
