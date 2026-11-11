#!/usr/bin/env python3
"""R33 -- independent re-solution of practice/33-half-and-quarter-wave-transformers.md.
No transformer rule is used. Lines are (1) lumped LC ladders of 20000 symmetric sections (ABCD product), with
the source and load solved as an ordinary two-port circuit, and (2) for resistive cases the time-domain
simulator tools/build14/checks/tlsim.py, read out as phasors after the transient."""
import os, sys
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "build14", "checks"))
from tlsim import simulate
pi = np.pi; NF = [0, 0]
def chk(name, got, want, tol=2e-3, atol=1e-6):
    ok = np.allclose(np.asarray(got, complex), np.asarray(want, complex), rtol=tol, atol=atol); NF[0 if ok else 1] += 1
    g = np.asarray(got); g = g.astype(complex) if np.iscomplexobj(g) else g.astype(float)
    print(("PASS " if ok else "FAIL ") + f"{name}: computed {np.round(g, 4)}, page {want}")
def abcd(Z0, frac, N=20000):                             # line of length frac wavelengths; only beta*l and Z0 matter
    th = 2 * pi * frac / N; Z = 1j * Z0 * th; Y = 1j * th / Z0
    return np.linalg.matrix_power(np.array([[1 + Z * Y / 2, Z * (1 + Z * Y / 4)], [Y, 1 + Z * Y / 2]], complex), N)
def solve(Z0, frac, ZL, Vg=None, Zg=0.0, Vin=None):
    """returns Z_in, V_in, I_in, V_L, I_L"""
    A, B, C, D = abcd(Z0, frac).ravel(); Zin = (A * ZL + B) / (C * ZL + D)
    if Vin is None: Vin = Vg * Zin / (Zg + Zin)
    Iin = Vin / Zin; IL = Vin / (A * ZL + B); return Zin, Vin, Iin, ZL * IL, IL
def phasor(t, y, w, periods=3):
    T = 2 * pi / w; m = t > t[-1] - periods * T; dt = t[1] - t[0]
    return 2 * np.sum(y[m] * np.exp(-1j * w * t[m])) * dt / (periods * T)
print("== 33.1"); chk("five inputs [ohm]", [solve(75, .25, 25, Vin=1)[0], solve(75, .5, 25, Vin=1)[0], solve(75, .25, 75j, Vin=1)[0], solve(75, .75, 150, Vin=1)[0], solve(75, .25, 75 + 75j, Vin=1)[0]], [225, 25, -75j, 37.5, 37.5 - 37.5j])
print("== 33.2"); r = solve(50, .5, 20 - 30j, Vin=1); chk("(e) half wave |V_L/V_in|", abs(r[3]), 1); r = solve(50, .25, 50, Vin=1); chk("(f) matched quarter wave |V_L/V_in|", abs(r[3]), 1)
a = solve(50, .25, 10, Vin=1)[4]; b = solve(50, .25, 400 - 90j, Vin=1)[4]; chk("(d) quarter wave: I_L for two very different loads, same V_in", [a, b], [-1j / 50, -1j / 50])
chk("(b) quarter wave of -j40 on 50 ohm; (c) 100 ohm at lambda/8 on 50 ohm is not 25", [solve(50, .25, -40j, Vin=1)[0], abs(solve(50, .125, 100, Vin=1)[0] - 25) > 1], [62.5j, 1])
print("== 33.3"); Zin, Vin, Iin, VL, IL = solve(50, .25, 100, Vg=12, Zg=50)
chk("Z_in, V_in, I_L, V_L, P_L", [Zin, Vin, IL, VL, 0.5 * np.real(VL * np.conj(IL))], [25, 4, -0.08j, -8j, 0.32])
f0 = 100e6; T = 0.25 / f0; r = simulate([(50.0, T)], 50.0, 100.0, lambda t: 12 * np.cos(2 * pi * f0 * t), 40 / f0, T / 250)
chk(" tlsim: V_in, V_L [V]", [phasor(r["t"], r["Vnode"][0], 2 * pi * f0), phasor(r["t"], r["Vnode"][1], 2 * pi * f0)], [4, -8j], atol=5e-3)
print("== 33.4"); chk("75 ohm quarter wave in front of 112.5 ohm [ohm]; reflected fraction without it", [solve(75, .25, 112.5, Vin=1)[0], ((112.5 - 50) / (112.5 + 50)) ** 2], [50, 0.148], tol=3e-3)
r = simulate([(50.0, 1e-8)], 50.0, 112.5, lambda t: 1.0, 1e-7, 1e-10)       # a step: the first echo is Gamma times the launched wave
chk(" tlsim: Gamma from a step (source end after the echo, per launched volt, minus 1)", r["Vnode"][0, -1] / 0.5 - 1, 0.3846, tol=2e-3)
print("== 33.5"); Zin, Vin, Iin, VL, IL = solve(50, 1.25, 30 + 40j, Vg=60, Zg=30 + 40j)
chk("Z_in, V_in, I_in, I_L, V_L, P_L, P_in", [Zin, Vin, Iin, IL, VL, 0.5 * np.real(VL * np.conj(IL)), 0.5 * np.real(Vin * np.conj(Iin))], [30 - 40j, 30 - 40j, 1, -0.8 - 0.6j, -50j, 15, 15])
best = max(0.5 * abs(60 / (30 + 40j + (R + 1j * X))) ** 2 * R for R in np.linspace(1, 100, 100) for X in np.linspace(-100, 100, 201))
chk(" largest power this source gives any load (grid search) [W]", best, 15)
print("== 33.6"); a = solve(50, .25, 25, Vin=10); b = solve(100, .25, 200, Vin=10)
chk("I_L1, V_L1, I_L2, V_L2, P1, P2, I_in total, P_in", [a[4], a[3], b[4], b[3], 0.5 * np.real(a[3] * np.conj(a[4])), 0.5 * np.real(b[3] * np.conj(b[4])), a[2] + b[2], 0.5 * np.real(10 * np.conj(a[2] + b[2]))],
    [-0.2j, -5j, -0.1j, -20j, 0.5, 1, 0.3, 1.5])
chk("(d) with Z02 = 50: I_L2", solve(50, .25, 200, Vin=10)[4], -0.2j)
print("== 33.7")
for k, want in ((1, [50, 5, -0.05j, -10j, 0.25]), (2, [200, 8, -0.04, -8, 0.16]), (3, [50, 5, 0.05j, 10j, 0.25])):
    Zin, Vin, Iin, VL, IL = solve(100, 0.25 * k, 200, Vg=10, Zg=50)
    chk(f" {k} f0 (ladder): Z_in, V_in, I_L, V_L, P_L", [Zin, Vin, IL, VL, 0.5 * np.real(VL * np.conj(IL))], want)
    f = k * 100e6; T = 0.25 / 100e6; r = simulate([(100.0, T)], 50.0, 200.0, lambda t: 10 * np.cos(2 * pi * f * t), 30 / 100e6, T / 300)
    chk(f" {k} f0 (tlsim): V_in, V_L [V]", [phasor(r["t"], r["Vnode"][0], 2 * pi * f), phasor(r["t"], r["Vnode"][1], 2 * pi * f)], [want[1], want[3]], atol=5e-3)
chk(" direct connection: V_L [V], P_L [W]", [10 * 200 / 250, 0.5 * (10 * 200 / 250) ** 2 / 200], [8, 0.16])
print("== 33.8 (stub: its own ladder, shorted; then the quarter-wave ladder)")
A, B, C, D = abcd(50, .125).ravel(); Zs = B / D; YL = 1 / 100 + 1 / Zs
Zin, Vin, Iin, VL, IL = solve(50, .25, 1 / YL, Vg=10, Zg=25)
chk("stub Z, Y_L, Z_in, I_in, V_in, V_L, P in the 100 ohm, P_in", [Zs, YL, Zin, Iin, Vin, VL, 0.5 * abs(VL) ** 2 / 100, 0.5 * np.real(Vin * np.conj(Iin))], [50j, 0.01 - 0.02j, 25 - 50j, 0.1 + 0.1j, 7.5 - 2.5j, 5 - 5j, 0.25, 0.25])
print(f"\nSUMMARY: {NF[0]} PASS, {NF[1]} FAIL")
