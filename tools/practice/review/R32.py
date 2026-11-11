#!/usr/bin/env python3
"""R32 -- independent re-solution of practice/32-stubs-and-input-impedance.md.
No tan/cot stub formula is used. A stub is (1) a lumped LC ladder of 20000 symmetric sections whose ABCD
matrix is multiplied out, and (2) for resistive circuits, the time-domain simulator tools/build14/checks/tlsim.py
(Kirchhoff at the nodes, no reflection coefficients), read out as phasors once the transient has died."""
import os, sys
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "build14", "checks"))
from tlsim import simulate
pi = np.pi; NF = [0, 0]
def chk(name, got, want, tol=2e-3, atol=1e-6):
    ok = np.allclose(np.asarray(got, complex), np.asarray(want, complex), rtol=tol, atol=atol); NF[0 if ok else 1] += 1
    g = np.asarray(got); g = g.astype(complex) if np.iscomplexobj(g) else g.astype(float)
    print(("PASS " if ok else "FAIL ") + f"{name}: computed {np.round(g, 4)}, page {want}")
def abcd(Z0, v, length, w, N=20000):
    dz = length / N; Z = 1j * w * (Z0 / v) * dz; Y = 1j * w / (Z0 * v) * dz
    M = np.array([[1 + Z * Y / 2, Z * (1 + Z * Y / 4)], [Y, 1 + Z * Y / 2]], complex)
    return np.linalg.matrix_power(M, N)
def zstub(Z0, v, length, w, end):
    A, B, C, D = abcd(Z0, v, length, w).ravel()
    return B / D if end == "short" else A / C            # V_L = 0, or I_L = 0
def phasor(t, y, w, periods=3):
    T = 2 * pi / w; m = t > t[-1] - periods * T; dt = t[1] - t[0]
    return 2 * np.sum(y[m] * np.exp(-1j * w * t[m])) * dt / (periods * T)
v = 2e8; w = 2 * pi * 1e8; lam = v / 1e8
print("== 32.1 (50 ohm line, lengths in wavelengths at 100 MHz, v = 2e8)")
chk("five stubs [ohm]", [zstub(50, v, lam / 8, w, "short"), zstub(50, v, 3 * lam / 8, w, "short"), zstub(50, v, lam / 8, w, "open"), zstub(50, v, lam / 6, w, "open"), zstub(50, v, lam / 2, w, "short")],
    [50j, -50j, -50j, -28.87j, 0], atol=1e-3)
print("== 32.2"); chk("(c) quarter-wave open stub -> 0; (d) adding lambda/2: Z(0.1 lam) vs Z(0.6 lam), shorted", [zstub(50, v, lam / 4, w, "open"), zstub(50, v, 0.6 * lam, w, "short")], [0, zstub(50, v, 0.1 * lam, w, "short")], atol=1e-3)
print("== 32.3"); w3 = 2 * pi * 150e6
chk("Y of a 0.3333 m shorted stub at 150 MHz (-> 0), Z of the 0.5 m stub [ohm]", [1 / zstub(75, 2e8, 1 / 3, w3, "short"), zstub(75, 2e8, 0.5, w3, "short")], [0, -75j], atol=2e-5)
print("== 32.4"); chk("reactance of a 9.69 cm shorted stub (100 ohm, 2e8) at 100 MHz vs w L of 50 nH [ohm]; of a 10 cm stub (3 % more L)",
                      [zstub(100, 2e8, 0.0969, w, "short").imag, zstub(100, 2e8, 0.10, w, "short").imag / 31.416], [31.416, 1.035], tol=3e-3)
print("== 32.5 (stub across the load: node equation with the ladder's admittance)")
def H5(f):
    Ys = 1 / zstub(50, 2e8, 1.5, 2 * pi * f, "short"); return (1 / 50) / (1 / 50 + 1 / 50 + Ys)   # V_L/F from KCL at the load node
chk("|H| at 50 MHz; at 33.33, 100 MHz (peaks 0.5); at 66.67, 133.33 MHz (nulls); at 1 kHz (DC null)",
    [abs(H5(50e6)), abs(H5(100e6 / 3)), abs(H5(100e6)), abs(H5(200e6 / 3)), abs(H5(400e6 / 3)), abs(H5(1e3))], [0.4472, 0.5, 0.5, 0, 0, 0], atol=2e-3)
print("== 32.6 (3 lambda/4 shorted stub, 10 V at the input; ladder from the short back to the input)")
f6 = 75e6; w6 = 2 * pi * f6; lam6 = 2e8 / f6
def at_d(d, Ishort):                                   # V(d), I(d) for a current Ishort through the short
    A, B, C, D = abcd(50, 2e8, d, w6).ravel(); return B * Ishort, D * Ishort
Vin1, Iin1 = at_d(0.75 * lam6, 1.0); Is = 10 / Vin1
chk("current through the short [A]; input current [A]; V at lambda/4 and lambda/2 [V]; input power [W]",
    [Is, Iin1 * Is, at_d(0.25 * lam6, Is)[0], at_d(0.5 * lam6, Is)[0], 0.5 * np.real(10 * np.conj(Iin1 * Is))], [0.2j, 0, -10, 0, 0], atol=2e-3)
print("== 32.7 (tlsim: 9 V source behind 75 ohm, 50 ohm line, shorted; v = 2.5e8)")
for f0, length, wantI, wantS in ((125e6, 0.5, 0, -0.18j), (125e6, 1.5, 0, None), (250e6, 0.5, 0.12, None)):
    T = length / 2.5e8; dt = T / 200
    r = simulate([(50.0, T)], 75.0, 0.0, lambda t: 9 * np.cos(2 * pi * f0 * t), 60 / f0, dt)
    IR = phasor(r["t"], r["Inode"][0], 2 * pi * f0); Ish = phasor(r["t"], r["Inode"][1], 2 * pi * f0); Vin = phasor(r["t"], r["Vnode"][0], 2 * pi * f0)
    chk(f" f = {f0/1e6:.0f} MHz, l = {length} m: resistor current [A]", IR, wantI, atol=2e-3)
    if wantS is not None: chk("   input voltage [V], current through the short [A]", [Vin, Ish], [9, wantS], atol=3e-3)
    if length == 1.5:
        Vm, Im = r["probe"](0, 2 / 3 - 1e-9)             # 2/3 of the way from the source = d = l/3 from the short
        chk("   l = 1.5 m: |I| at d = l/3 (null), |I| through the short [A]", [abs(phasor(r["t"], Im, 2 * pi * f0)), abs(Ish)], [0, 0.18], atol=4e-3)
print("== 32.8 (0.6 m shorted air stub, 50 ohm load, series capacitor 50.9 pF)")
def H8(f, C=None):
    X = zstub(50, 3e8, 0.6, 2 * pi * f, "short") + (0 if C is None else 1 / (1j * 2 * pi * f * C)); return 50 / (50 + X)
chk("no capacitor: |H| at 250 MHz (1) and 125 MHz (0)", [abs(H8(250e6)), abs(H8(125e6))], [1, 0], atol=2e-3)
fs = np.linspace(40e6, 100e6, 601); peak = fs[np.argmax([abs(H8(f, 50.93e-12)) for f in fs])]
chk("with 50.93 pF: frequency of the peak below 125 MHz [MHz]; |H| there; at 125 MHz; at 1 kHz; at 31.25 MHz",
    [peak / 1e6, abs(H8(peak, 50.93e-12)), abs(H8(125e6, 50.93e-12)), abs(H8(1e3, 50.93e-12)), abs(H8(31.25e6, 50.93e-12))], [62.5, 1, 0, 0, 0.5334], atol=2e-3)
print(f"\nSUMMARY: {NF[0]} PASS, {NF[1]} FAIL")
