#!/usr/bin/env python3
"""Numbers, signs and formulas on the Lecture 31-33 pages and the three concept pages
(line-resonances, stub-input-impedance, quarter-wave-transformer).
Closed forms are checked against brute force: finite differences of the telegrapher's equations,
a characteristics (bouncing-wave) simulation, and tlsim.py (Kirchhoff at the nodes, no Gamma)."""
import os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tlsim import simulate
pi = np.pi; c = 3e8; n = dict(p=0, f=0)
def chk(label, mine, want, tol=1e-6, atol=1e-9):
    ok = np.allclose(np.asarray(mine, complex), np.asarray(want, complex), rtol=tol, atol=atol)
    n["p" if ok else "f"] += 1
    a = np.asarray(mine); a = a.astype(complex) if np.iscomplexobj(a) else a.astype(float)
    print(("PASS " if ok else "FAIL ") + f"{label}: {np.round(a, 5)}")
def phasor(t, y, w, periods=3):
    T = 2 * pi / w; m = t > t[-1] - periods * T; dt = t[1] - t[0]
    return 2 * np.sum(y[m] * np.exp(-1j * w * t[m])) * dt / (periods * T)

print("== Lecture 31: modes satisfy the telegrapher's equations and the end conditions")
Z0, v, l = 50.0, 2e8, 30.0; L_ = Z0 / v; C_ = 1 / (Z0 * v)
def resid(V, I, z, t, hz=1e-5, ht=1e-13):
    r1 = (V(z + hz, t) - V(z - hz, t)) / (2 * hz) + L_ * (I(z, t + ht) - I(z, t - ht)) / (2 * ht)
    r2 = (I(z + hz, t) - I(z - hz, t)) / (2 * hz) + C_ * (V(z, t + ht) - V(z, t - ht)) / (2 * ht)
    return r1, r2
F, th = 1.7, 0.6
for k in (1, 2, 3):
    w = k * pi * v / l; b = w / v
    V = lambda z, t: 2 * F * np.cos(w * t + th) * np.cos(b * z); I = lambda z, t: 2 * F / Z0 * np.sin(w * t + th) * np.sin(b * z)
    r1, r2 = resid(V, I, 11.3, 4.2e-8)
    chk(f" open-open n={k}: residuals (scaled), I(0), I(l); f = n v/2l [MHz]", [r1 / (b * F), r2 / (b * F / Z0), I(0, 1e-8), I(l, 1e-8), w / (2 * pi) / 1e6], [0, 0, 0, 0, k * v / (2 * l) / 1e6], tol=1e-5, atol=1e-6)
    V = lambda z, t: 2 * F * np.sin(w * t + th) * np.sin(b * z); I = lambda z, t: 2 * F / Z0 * np.cos(w * t + th) * np.cos(b * z)
    r1, r2 = resid(V, I, 11.3, 4.2e-8)
    chk(f" short-short n={k}: residuals (scaled), V(0), V(l)", [r1 / (b * F), r2 / (b * F / Z0), V(0, 1e-8), V(l, 1e-8)], [0, 0, 0, 0], tol=1e-5, atol=1e-6)
for k in (0, 1, 2):
    w = (2 * k + 1) * pi * v / (2 * l); b = w / v
    V = lambda z, t: Z0 * np.cos(b * z) * np.cos(w * t); I = lambda z, t: np.sin(b * z) * np.sin(w * t)
    r1, r2 = resid(V, I, 11.3, 4.2e-8)
    chk(f" open(z=0)-short(z=l) n={k}: residuals, I(0), V(l); w/(pi v/l)", [r1 / (b * Z0), r2 / b, I(0, 1e-8), V(l, 1e-8), w / (pi * v / l)], [0, 0, 0, 0, k + 0.5], tol=1e-5, atol=1e-6)
chk("identities: cos(a-b)-cos(a+b) = 2 sin a sin b; cos(a-b)+cos(a+b) = 2 cos a cos b", [np.cos(0.3) - np.cos(1.7), np.cos(0.3) + np.cos(1.7)], [2 * np.sin(1.0) * np.sin(0.7), 2 * np.cos(1.0) * np.cos(0.7)])
print("== Lecture 31 Example 1: 600 m, open at z=0, short at z=l, v = c, Z0 = 50")
l = 600.0
chk("f_n [MHz], n = 0,1,2", [(2 * k + 1) * c / (4 * l) / 1e6 for k in range(3)], [0.125, 0.375, 0.625])
chk("omega_n [rad/us] / pi, beta_n [rad/m] * 1200/pi for n = 1", [2 * pi * 0.375 / pi, 2 * pi * 0.375e6 / c * 1200 / pi], [3 / 4, 3])
chk("voltage amplitude per ampere = v L = Z0 [V]; '300 L' with L in uH/m", [c * (50 / c), 300 * (50 / c) * 1e6], [50, 50])
chk("same line, both ends open: n c/2l [MHz]", [k * c / (2 * l) / 1e6 for k in (1, 2, 3)], [0.25, 0.5, 0.75])
print("== Lecture 31 battery: 3 V on a 600 m line (v = c) for 1 us, then both ends open (characteristics)")
N = 600; dz = 1.0; dt = dz / c
f = np.zeros(N); b = np.zeros(N)          # forward / backward wave samples, cell k at z = (k+0.5) m
f[:300] = 3.0                              # state at t = 1 us: forward pulse on 0 < z < 300 m
rec = []; snaps = {}
steps = int(round(9e-6 / dt))
for m in range(steps + 1):
    t = 1e-6 + m * dt
    Vz = f + b; Iz = (f - b) / 50.0
    rec.append((t, Vz[449], Vz.mean(), Vz[-1], Iz[-1]))
    for ts in (1e-6, 2.5e-6, 5e-6):
        if abs(t - ts) < dt / 2: snaps[ts] = Vz.copy()
    fo, bo = f[-1], b[0]                   # arriving at z = l and z = 0
    f = np.concatenate(([bo], f[:-1]))     # open end: reflected wave = arriving wave (I = 0)
    b = np.concatenate((b[1:], [fo]))
rec = np.array(rec)
chk("mean voltage along the line stays 1.5 V (min, max over time)", [rec[:, 2].min(), rec[:, 2].max()], [1.5, 1.5])
chk("snapshot at 5 us equals the snapshot at 1 us (period 4 us): max difference", np.abs(snaps[5e-6] - snaps[1e-6]).max(), 0)
chk("at t = 2.5 us near z = l: V = 6 V and I = 0 (pulse folding on the open end)", [rec[np.argmin(abs(rec[:, 0] - 2.5e-6)), 3], rec[np.argmin(abs(rec[:, 0] - 2.5e-6)), 4]], [6, 0])
r450 = rec[:, 1]; k4 = int(round(4e-6 / dt))
chk("record at z = 450 m repeats after 4 us: max |V(t+4us) - V(t)|", np.abs(r450[k4:] - r450[:-k4]).max(), 0)
print("== Lecture 32: stub impedance from the phasor waves")
Z0 = 50.0
for bl in (0.3, 1.1, 2.0, 2.9):
    Vs = 1j * 2 * np.sin(bl); Is = 2 / Z0 * np.cos(bl); Vo = 2 * np.cos(bl); Io = 2j / Z0 * np.sin(bl)
    e = np.exp(1j * bl)
    chk(f" beta l = {bl}: short (V, I from e^(+-jbl)), Z; open (V, I), Z", [(e - 1 / e), (e + 1 / e) / Z0, Vs / Is, (e + 1 / e), (e - 1 / e) / Z0, Vo / Io],
        [Vs, Is, 1j * Z0 * np.tan(bl), Vo, Io, -1j * Z0 / np.tan(bl)])
chk("sign of X: shorted inductive below pi/2, capacitive above; open the reverse", [np.tan(1.0) > 0, np.tan(2.0) < 0, -1 / np.tan(1.0) < 0, -1 / np.tan(2.0) > 0], [1, 1, 1, 1])
v = 2e8; L_ = Z0 / v; C_ = 1 / (Z0 * v); w = 2 * pi * 1e6; ls = 0.5
chk("short stubs (beta l = 0.0157): shorted ~ j w L l, open ~ 1/(j w C l) (ratio)", [1j * Z0 * np.tan(w / v * ls) / (1j * w * L_ * ls), -1j * Z0 / np.tan(w / v * ls) * (1j * w * C_ * ls)], [1, 1], tol=1e-3)
chk("lambda/8 stub on 50 ohm: shorted, open [ohm]", [1j * 50 * np.tan(pi / 4), -1j * 50 / np.tan(pi / 4)], [50j, -50j])
print("== Lecture 32 Example 1: 3 m shorted air stub, Z0 = 50, in series with 50 ohm")
l = 3.0; H1 = lambda f: 50 / (50 + 1j * 50 * np.tan(2 * pi * f * l / c))
fs = np.array([7e6, 33e6, 61e6, 140e6])
chk("|H| = |cos(w l/c)| at 7, 33, 61, 140 MHz", np.abs(H1(fs)), np.abs(np.cos(2 * pi * fs * l / c)))
chk("series resonances n c/2l [MHz]; parallel (2n+1) c/4l [MHz]", [k * c / (2 * l) / 1e6 for k in (0, 1, 2)] + [(2 * k + 1) * c / (4 * l) / 1e6 for k in (0, 1, 2)], [0, 50, 100, 25, 75, 125])
chk("|H| at 50, 100 MHz (=1) and at 25, 75 MHz (-> 0)", [abs(H1(50e6)), abs(H1(100e6)), abs(H1(25e6 * (1 + 1e-9))), abs(H1(75e6 * (1 + 1e-9)))], [1, 1, 0, 0], atol=1e-6)
for f0 in (10e6, 40e6):                     # independent: time-domain line simulation, source matched (Rg = 50), stub shorted
    T = l / c; dt = T / 30; r = simulate([(50.0, T)], 50.0, 0.0, lambda t: np.cos(2 * pi * f0 * t), 60 / f0 if f0 > 2e7 else 12 / f0, dt)
    IR = phasor(r["t"], r["Inode"][0], 2 * pi * f0)
    chk(f" tlsim at {f0/1e6:.0f} MHz: |V_R/F| = 50 |I|", abs(50 * IR), abs(np.cos(2 * pi * f0 * l / c)), tol=5e-3)
print("== Lecture 32 Example 3: add C = 10 pF in series")
C = 10e-12; H3 = lambda f: 50 / (50 + 1 / (1j * 2 * pi * f * C) + 1j * 50 * np.tan(2 * pi * f * l / c))
g = lambda f: 50 * np.tan(2 * pi * f * l / c) - 1 / (2 * pi * f * C)
roots = []
for k in range(3):
    a, b_ = k * 50e6 + 1e3, (k * 50 + 25) * 1e6 - 1e3
    for _ in range(200):
        m = (a + b_) / 2
        if g(a) * g(m) <= 0: b_ = m
        else: a = m
    roots.append(m)
chk("shifted series resonances [MHz] (page: 23.8, 71.5, 119.3)", np.array(roots) / 1e6, [23.8, 71.5, 119.3], tol=1e-3)
chk("|H| there = 1; nulls still at 25, 75 MHz; |H| -> 0 at DC", [abs(H3(roots[0])), abs(H3(roots[1])), abs(H3(25e6 * (1 + 1e-9))), abs(H3(75e6 * (1 + 1e-9))), abs(H3(1.0))], [1, 1, 0, 0, 0], atol=1e-5)
print("== Lecture 32 Example 2: inductor with a stub, series and parallel")
Lx = 40e-9; Zs = lambda f: 1j * 2 * pi * f * Lx + 1j * 50 * np.tan(2 * pi * f * l / c); Yp = lambda f: 1 / (1j * 2 * pi * f * Lx) + 1 / (1j * 50 * np.tan(2 * pi * f * l / c))
a, b_ = 25e6 + 1e3, 50e6 - 1e3
for _ in range(200):
    m = (a + b_) / 2
    if np.imag(Zs(a)) * np.imag(Zs(m)) <= 0: b_ = m
    else: a = m
chk("zero of the series impedance is a zero of the parallel admittance (|Y| there), and it moved off 50 MHz", [abs(Yp(m)) < 1e-6, m < 50e6 - 1e5], [1, 1])
chk("poles of the series impedance stay at the stub's parallel resonances: |1/Zs| at 25, 75 MHz", [abs(1 / Zs(25e6 * (1 + 1e-9))), abs(1 / Zs(75e6 * (1 + 1e-9)))], [0, 0], atol=1e-5)
print("== Lecture 32 Example 4: 2 A source, 50 ohm, open-ended line")
Zin = lambda bl: -1j * 50 / np.tan(bl)
IR = lambda bl: 2 * (1 / 50) / (1 / 50 + 1 / Zin(bl))
chk("I_R at l = lambda/2 and lambda (-> 2 A); at lambda/4 and 3 lambda/4 (-> 0)", [IR(pi - 1e-9), IR(2 * pi - 1e-9), IR(pi / 2), IR(3 * pi / 2)], [2, 2, 0, 0], atol=1e-6)
print("== Lecture 33: the two rules from the phasor waves, random load")
ZL = 37 - 64j; Vp = 0.8 + 0.3j; Vm = (ZL - Z0) / (ZL + Z0) * Vp
Vd = lambda bd: Vp * np.exp(1j * bd) + Vm * np.exp(-1j * bd); Id = lambda bd: (Vp * np.exp(1j * bd) - Vm * np.exp(-1j * bd)) / Z0
chk("half wave: V_in/V_L, I_in/I_L, Z_in/Z_L", [Vd(pi) / Vd(0), Id(pi) / Id(0), Vd(pi) / Id(pi) / ZL], [-1, -1, 1])
chk("quarter wave: V_in/(j Z0 I_L), I_in/(j V_L/Z0), Z_in Z_L/Z0^2, I_L/(-j V_in/Z0), V_L/(-j Z0 I_in)",
    [Vd(pi / 2) / (1j * Z0 * Id(0)), Id(pi / 2) / (1j * Vd(0) / Z0), Vd(pi / 2) / Id(pi / 2) * ZL / Z0 ** 2, Id(0) / (-1j * Vd(pi / 2) / Z0), Vd(0) / (-1j * Z0 * Id(pi / 2))], [1, 1, 1, 1, 1])
chk("3 lambda/4 inverts, lambda repeats: Z_in Z_L/Z0^2, Z_in/Z_L; power in = power out",
    [Vd(1.5 * pi) / Id(1.5 * pi) * ZL / Z0 ** 2, Vd(2 * pi) / Id(2 * pi) / ZL, np.real(Vd(pi / 2) * np.conj(Id(pi / 2))) / np.real(Vd(0) * np.conj(Id(0)))], [1, 1, 1])
print("== Lecture 33 examples")
Zin = 50 ** 2 / (50 + 50j); chk("Ex 1: Z_in [ohm]", Zin, 25 - 25j)
IL = -1j * 100 / 50; VL = (50 + 50j) * IL
chk("Ex 2: I_L [A], V_L [V], P_L [W] three ways", [IL, VL, 0.5 * np.real(VL * np.conj(IL)), 0.5 * abs(IL) ** 2 * 50, 0.5 * np.real(100 * np.conj(100 / Zin))], [-2j, 100 - 100j, 100, 100, 100])
Zin = 50 ** 2 / 100; Vin = 10j * Zin / (25 + Zin); Vq = -Vin; IL = -1j * Vq / 50; VL = 100 * IL
chk("Ex 3: Z_in, V_in, V(0.25 lambda), I_L, V_L, P_in, P_L", [Zin, Vin, Vq, IL, VL, 0.5 * np.real(Vin * np.conj(Vin / Zin)), 0.5 * abs(IL) ** 2 * 100], [25, 5j, -5j, -0.1, -10, 0.5, 0.5])
f0 = 100e6; T = 0.75 / f0; dt = T / 300                       # independent: tlsim, source j10 = 10 cos(wt + 90 deg) behind 25 ohm
r = simulate([(50.0, T)], 25.0, 100.0, lambda t: 10 * np.cos(2 * pi * f0 * t + pi / 2), 40 / f0, dt)
VLs = phasor(r["t"], r["Vnode"][1], 2 * pi * f0); Vins = phasor(r["t"], r["Vnode"][0], 2 * pi * f0)
chk(" tlsim: V_in, V_L, I_L = V_L/100", [Vins, VLs, VLs / 100], [5j, -10, -0.1], tol=5e-3, atol=2e-3)
IL1 = IL2 = -1j * 5 / 50
chk("Ex 4: I_L1 = I_L2 [A], V_L1, V_L2 [V], P total [W], also from the two input impedances", [IL1, IL1 * 50, IL2 * 100, 0.5 * 0.1 ** 2 * 50 + 0.5 * 0.1 ** 2 * 100, 0.5 * 25 * (1 / 50 + 1 / 25)], [-0.1j, -5j, -10j, 0.75, 0.75])
chk("matching: Gamma of 200 on 50; Z_q = sqrt(50*200); its input [ohm]", [(200 - 50) / 250, np.sqrt(50 * 200), 100 ** 2 / 200], [0.6, 100, 50])
print(f"\nSUMMARY: {n['p']} PASS, {n['f']} FAIL")
