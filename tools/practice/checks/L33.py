#!/usr/bin/env python3
"""Author's checks for practice/33-half-and-quarter-wave-transformers.md: every number in the answers."""
import numpy as np
pi = np.pi; n = dict(p=0, f=0)
def chk(label, mine, want, tol=1e-6, atol=1e-9):
    ok = np.allclose(np.asarray(mine, complex), np.asarray(want, complex), rtol=tol, atol=atol)
    n["p" if ok else "f"] += 1
    a = np.asarray(mine); a = a.astype(complex) if np.iscomplexobj(a) else a.astype(float)
    print(("PASS " if ok else "FAIL ") + f"{label}: {np.round(a, 5)}")
def zin(Z0, ZL, bl):                       # general line formula, used as the reference
    return Z0 * (ZL * np.cos(bl) + 1j * Z0 * np.sin(bl)) / (Z0 * np.cos(bl) + 1j * ZL * np.sin(bl))
def load(Z0, ZL, bl, Vin):                 # V_L, I_L from V_in by the phasor waves
    G = (ZL - Z0) / (ZL + Z0); Vp = Vin / (np.exp(1j * bl) + G * np.exp(-1j * bl)); return Vp * (1 + G), Vp * (1 - G) / Z0
print("== 33.1"); chk("five inputs [ohm]", [zin(75, 25, pi / 2), zin(75, 25, pi), zin(75, 75j, pi / 2), zin(75, 150, 1.5 * pi), zin(75, 75 + 75j, pi / 2)], [225, 25, -75j, 37.5, 37.5 - 37.5j])
print("== 33.2"); VL, IL = load(50, 50, pi / 2, 1.0); chk("(f) matched quarter wave: V_L/V_in", VL, -1j); VL, IL = load(50, 20 - 30j, pi, 1.0); chk("(e) half wave: V_L/V_in", VL, -1)
chk("(b) quarter wave of a capacitive load -j40 on 50 ohm", zin(50, -40j, pi / 2), 62.5j); chk("(c) 100 ohm on 50 ohm at l = lambda/8 is not Z0^2/ZL = 25", abs(zin(50, 100, pi / 4) - 25) > 1, 1)
print("== 33.3"); Zi = zin(50, 100, pi / 2); Vin = 12 * Zi / (Zi + 50); VL, IL = load(50, 100, pi / 2, Vin)
chk("Z_in, V_in, I_L, V_L, P_L, P_in; the student's wrong value", [Zi, Vin, IL, VL, 0.5 * abs(IL) ** 2 * 100, 0.5 * np.real(Vin * np.conj(Vin / Zi)), -1j * 12 / 50], [25, 4, -0.08j, -8j, 0.32, 0.32, -0.24j])
print("== 33.4"); G = (112.5 - 50) / (112.5 + 50); chk("Gamma, Gamma^2, Z_q, lambda [m], l [cm], check Z_q^2/R_L", [G, G ** 2, np.sqrt(50 * 112.5), 2e8 / 3e8, 2e8 / 3e8 / 4 * 100, 75 ** 2 / 112.5], [0.38462, 0.14793, 75, 0.66667, 16.6667, 50], tol=1e-4)
print("== 33.5"); ZL = 30 + 40j; Zg = 30 + 40j; bl = 2.5 * pi; Zi = zin(50, ZL, bl); Iin = 60 / (Zg + Zi); Vin = Zi * Iin; VL, IL = load(50, ZL, bl, Vin)
chk("Z_in, I_in, V_in, I_L, V_L, P_L, available power, P_in", [Zi, Iin, Vin, IL, VL, 0.5 * abs(IL) ** 2 * 30, 60 ** 2 / (8 * 30), 0.5 * np.real(Vin * np.conj(Iin))], [30 - 40j, 1, 30 - 40j, -0.8 - 0.6j, -50j, 15, 15, 15])
print("== 33.6"); V1, I1 = load(50, 25, pi / 2, 10.0); V2, I2 = load(100, 200, pi / 2, 10.0)
Iin = 10 / zin(50, 25, pi / 2) + 10 / zin(100, 200, pi / 2)
chk("I_L1, V_L1, I_L2, V_L2, P1, P2, Z_in1, Z_in2, I_in, P_in", [I1, V1, I2, V2, 0.5 * abs(I1) ** 2 * 25, 0.5 * abs(I2) ** 2 * 200, zin(50, 25, pi / 2), zin(100, 200, pi / 2), Iin, 0.5 * np.real(10 * np.conj(Iin))],
    [-0.2j, -5j, -0.1j, -20j, 0.5, 1, 100, 50, 0.3, 1.5])
V2b, I2b = load(50, 200, pi / 2, 10.0); chk("(d) with Z02 = 50: I_L2 = I_L1", I2b, I1)
print("== 33.7")
for k, want in ((1, [50, 5, -0.05j, -10j, 0.25]), (2, [200, 8, -0.04, -8, 0.16]), (3, [50, 5, 0.05j, 10j, 0.25])):
    bl = k * pi / 2; Zi = zin(100, 200, bl); Vin = 10 * Zi / (Zi + 50); VL, IL = load(100, 200, bl, Vin)
    chk(f" at {k} f0: Z_in, V_in, I_L, V_L, P_L", [Zi, Vin, IL, VL, 0.5 * abs(IL) ** 2 * 200], [want[0], want[1], want[2], want[3], want[4]])
chk("available power [W]; direct connection V_L, P_L; gain", [100 / (8 * 50), 10 * 200 / 250, 0.5 * 8 ** 2 / 200, 0.25 / 0.16], [0.25, 8, 0.16, 1.5625])
print("== 33.8"); Zs = 1j * 50 * np.tan(pi / 4); YL = 1 / 100 + 1 / Zs; Zi = zin(50, 1 / YL, pi / 2); Iin = 10 / (25 + Zi); Vin = Zi * Iin; VL, IL = load(50, 1 / YL, pi / 2, Vin)
chk("stub Z, Y_L, Z_in, I_in, V_in, V_L, |V_L|^2, P in the resistor, P_in, total load current two ways",
    [Zs, YL, Zi, Iin, Vin, VL, abs(VL) ** 2, 0.5 * abs(VL) ** 2 / 100, 0.5 * np.real(Vin * np.conj(Iin)), IL, YL * VL],
    [50j, 0.01 - 0.02j, 25 - 50j, 0.1 + 0.1j, 7.5 - 2.5j, 5 - 5j, 50, 0.25, 0.25, -0.05 - 0.15j, -0.05 - 0.15j])
chk(" V_L = -j Z0 I_in", -1j * 50 * Iin, 5 - 5j)
print(f"\nSUMMARY: {n['p']} PASS, {n['f']} FAIL")
