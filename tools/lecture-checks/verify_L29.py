#!/usr/bin/env python3
"""Verification of every number, sign and time on the Lecture 29 pages of the ECE 329 study site.

Pages checked:
  content-src/4-transmission-lines/29-bounce-diagram-examples.md      (sections A-F)
  content-src/problems/a-ramp-pulse-meets-its-echo.md                 (section G)
  figs_l29.py: the series behind every figure                          (sections C, D, F, G use it)
Method: every bounce-diagram result is compared with two independent time-steppings of the line
(tlsim29.moc: method of characteristics on the magic grid, exact at grid points; tlsim29.fdtd: Yee leapfrog of the
telegrapher's equations at Courant 0.5 with lumped terminations). Neither stepper uses Gamma, tau or the diagram:
the ends are solved from KVL / Ohm's law. numpy only. Units: us, m, V, ohm, A.
"""
import sys
from fractions import Fraction as Fr
import numpy as np

sys.path.insert(0, "/home/claude/work")
sys.path.insert(0, "/home/claude/work/digest10")
import figs_l29 as F          # noqa: E402  (the figures' series = the page's formulas)
from tlsim29 import moc, fdtd  # noqa: E402

ok_count = 0


def ok(cond, msg):
    global ok_count
    assert cond, "FAILED: " + msg
    ok_count += 1
    print("ok  ", msg)


def close(a, b, msg, atol=1e-9):
    a_, b_ = np.asarray(a, dtype=float), np.asarray(b, dtype=float)
    d = np.max(np.abs(a_ - b_)) if a_.size else 0.0
    ok(np.allclose(a_, b_, rtol=0, atol=atol), f"{msg}: max |diff| {d:.1e} over {a_.size} values (tol {atol:g})")


def coeffs(Z0, Rg, RL):
    Z0, Rg = Fr(Z0), Fr(Rg)
    tg = Z0 / (Rg + Z0)
    Gg = (Rg - Z0) / (Rg + Z0)
    GL = Fr(1) if RL == np.inf else (Fr(RL) - Z0) / (Fr(RL) + Z0)
    return tg, Gg, GL


def away(x, edges, gap):
    """mask: x farther than gap from every edge"""
    m = np.ones_like(x, dtype=bool)
    for e in edges:
        m &= np.abs(x - e) > gap
    return m


W_S = 0.3   # us: width of the raised-cosine edge used for the FDTD runs


def S_(t, w=W_S):
    """unit step convolved with the unit-area raised cosine (1 - cos 2 pi tau/w)/w on (0, w): exact, continuous"""
    t = np.asarray(t, dtype=float); x = np.clip(t / w, 0, 1)
    return x - np.sin(2 * np.pi * x) / (2 * np.pi)


def R_(t, w=W_S):
    """ramp t u(t) convolved with the same kernel (the integral of S_)"""
    t = np.asarray(t, dtype=float); x = np.clip(t, 0, w)
    inner = x ** 2 / (2 * w) + (np.cos(2 * np.pi * x / w) - 1) * w / (4 * np.pi ** 2)
    return np.where(t > w, t - w / 2, inner)


# smoothed versions of the notes' and the problem's inputs (FDTD runs; the series uses the same functions, by linearity)
fs_step = lambda t: S_(t)
fs_ex3 = lambda t: (S_(np.asarray(t) + 0.5) - S_(np.asarray(t) - 0.5)) + 2 * (S_(np.asarray(t) - 0.5) - S_(np.asarray(t) - 1.5))
fs_ramp = lambda t: 3 * (R_(t) - R_(np.asarray(t) - 1)) - 3 * S_(np.asarray(t) - 1)


C = 300.0

print("=== A. coefficients and times")
tg, Gg, GL = coeffs(50, 50, 100)                       # Example 1 with Z0 = 50 (any Z0: R_g = Z0, R_L = 2 Z0)
ok((tg, Gg, GL) == (Fr(1, 2), Fr(0), Fr(1, 3)), "Ex 1: tau_g = 1/2, Gamma_g = 0, Gamma_L = (2-1)/(2+1) = 1/3")
for Z0 in (1, 37.5, 75, 300):
    ok(coeffs(Z0, Z0, 2 * Z0) == (Fr(1, 2), Fr(0), Fr(1, 3)), f"Ex 1 coefficients independent of Z0 (Z0 = {Z0})")
ok(2 * 900 / C == 6.0, "Ex 1: 2l/v = 2*900 m / 300 m/us = 6 us")
ok(C / 1.0 == 300.0 and 900 / 300.0 == 3, "Ex 1: lambda = v/f = 300 m at 1 MHz; line = 3 lambda")
ok(np.isclose(2 * np.pi * 1.0 * 6.0, 12 * np.pi), "Ex 1: omega * 6 us = 12 pi")
tg, Gg, GL = coeffs(50, 0, 100)
ok((tg, Gg, GL) == (Fr(1), Fr(-1), Fr(1, 3)), "Ex 2: tau_g = 1, Gamma_g = -1, Gamma_L = 1/3")
ok(2400 / C == 8.0 and 1200 / C == 4.0, "Ex 2: l/v = 2400 m / 300 m/us = 8 us; z = 1200 m reached at 4 us")
ok(GL * Gg == Fr(-1, 3) and 2 * 2400 / C == 16, "Ex 3 (Ex 2's circuit): Gamma_L Gamma_g = -1/3, 2l/c = 16 us")
tg, Gg, GL = coeffs(50, 25, 150)
ok((tg, Gg, GL) == (Fr(2, 3), Fr(-1, 3), Fr(1, 2)), "problem: tau_g = 50/75 = 2/3, Gamma_g = -25/75 = -1/3, Gamma_L = 100/200 = 1/2")
ok(600 / 200.0 == 3.0 and 200.0 * 1.0 == 200.0, "problem: l/v = 3 us; pulse length vT = 200 m")
ok((tg * GL, tg * GL * Gg) == (Fr(1, 3), Fr(-1, 9)), "problem: leg weights 2/3, 1/3, -1/9 (times f_i)")
# leg-weight generator used by the figures
lg = F.legs(1.0, 1 / 3, -1.0, 8.0, 56.0)
close([w for *_, w in lg], [1, 1 / 3, -1 / 3, -1 / 9, 1 / 9, 1 / 27, -1 / 27], "Ex 2 figure legs: weights 1, 1/3, -1/3, -1/9, 1/9, 1/27, -1/27")
lg = F.legs(0.5, 1 / 3, 0.0, 3.0, 7.0)
close([w for *_, w in lg], [0.5, 1 / 6], "Ex 1 figure legs: 1/2, 1/6, then nothing (Gamma_g = 0)")

tt_ = np.linspace(-1, 3, 40001)
close(fs_step(tt_)[tt_ > W_S], 1.0, "smoothed step = 1 after w = 0.3 us", atol=1e-12)
close(np.gradient(R_(tt_), tt_), S_(tt_), "smoothed ramp is the integral of the smoothed step", atol=1e-3)
ok(np.max(np.abs(fs_ex3(tt_) - F.f_ex3(tt_))[F.f_ex3(tt_) == F.f_ex3(tt_ - W_S - 0.01)]) < 1e-12, "smoothed Ex 3 pulse = pulse once w has passed after each edge")
ok(np.max(np.abs(fs_ramp(tt_) - F.f_ramp(tt_ - W_S / 2))[((tt_ > W_S) & (tt_ < 1)) | (tt_ > 1 + W_S)]) < 1e-12, "smoothed ramp = ramp delayed by w/2 away from the edges")

print("=== B. the two steppers agree with each other (step into an open line, R_g = Z0)")
fs = fs_step
z, t, VV, II = moc(50, 300, 900, 50, np.inf, fs, 10, 900)
errs = {}
for N in (1800, 3600):
    r = fdtd(50, 300, 900, 50, np.inf, fs, 10, N, snaps=(1.5, 4.5, 7.5))
    for ts in (1.5, 4.5, 7.5):
        zf, Vf, If = r["snap"][ts]
        n = int(round(ts / (t[1] - t[0])))
        errs[N, ts] = np.max(np.abs(Vf - np.interp(zf, z, VV[n])))
        if N == 1800:
            close(Vf, np.interp(zf, z, VV[n]), f"open line, t = {ts} us: FDTD vs MoC, V(z)", atol=0.01)
            close(If, np.interp(zf, z, II[n]), f"open line, t = {ts} us: FDTD vs MoC, I(z)", atol=0.01 / 50)
ok(all(errs[3600, ts] < 0.6 * errs[1800, ts] for ts in (1.5, 4.5, 7.5)),
   "halving dz shrinks the FDTD-MoC difference (2-4x): " + ", ".join(f"{errs[1800, ts]:.1e} -> {errs[3600, ts]:.1e}" for ts in (1.5, 4.5, 7.5)))
ok(abs(VV[-1, 450] - 1.0) < 1e-12, "open line, matched source: V -> 1 V after the echo is absorbed (lumped open circuit)")

print("=== C. Example 1 (sine burst, matched generator)")
z, t, VV, II = moc(50, C, 900, 50, 100, F.f_ex1, 9.0, 900)
Zg, Tg = np.meshgrid(z, t)
Vs, ZIs = F.series(Zg / C, Tg, F.f_ex1, **F.EX1)
close(Vs, VV, "series (figure/page formula) = MoC for V(z,t) on the whole grid, 0-9 us", atol=1e-9)
close(ZIs, 50 * II, "series = MoC for Z0 I(z,t)", atol=1e-9)
w = 2 * np.pi
Vnotes = 0.5 * np.sin(w * (Tg - Zg / C)) * (Tg - Zg / C >= 0) + (1 / 6) * np.sin(w * (Tg + Zg / C - 6)) * (Tg + Zg / C - 6 >= 0)
close(Vnotes, VV, "notes' closed form V = 1/2 sin w(t - z/v)u(.) + 1/6 sin w(t + z/v - 6)u(.)", atol=1e-9)
ZInotes = 0.5 * np.sin(w * (Tg - Zg / C)) * (Tg - Zg / C >= 0) - (1 / 6) * np.sin(w * (Tg + Zg / C - 6)) * (Tg + Zg / C - 6 >= 0)
close(ZInotes, 50 * II, "page: Z0 I = same with -1/6", atol=1e-9)
for ts, front in ((1.0, 300), (2.0, 600)):
    n = int(round(ts * C)); row = VV[n]
    ok(np.all(np.abs(row[z > front + 1]) < 1e-12) and np.max(np.abs(row[z < front])) > 0.49, f"t = {ts} us: front at {front} m, amplitude 1/2 behind it")
    ok(abs(np.max(row) - 0.5) < 1e-3 and abs(np.min(row) + 0.5) < 1e-3, f"t = {ts} us: max/min +-1/2")
    ok(row[10] < 0, f"t = {ts} us: V just right of z = 0 is negative (sin w(t - z/v) with integer t), as in the notes' plots")
nL = t > 3.0 + 1e-9
close(VV[nL, -1], (2 / 3) * np.sin(w * (t[nL] - 3)), "load voltage (1 + 1/3)(1/2) sin w(t - 3 us) = 2/3 sin w(t - 3) for t > 3 us", atol=1e-9)
close(VV[t < 3 - 1e-9, -1], 0, "load voltage zero before 3 us")
n45 = int(round(4.5 * C)); row = VV[n45]
inc = 0.5 * np.sin(w * (4.5 - z / C))
close(row[z < 449], inc[z < 449], "t = 4.5 us: left of 450 m only the burst", atol=1e-9)
ok(np.max(np.abs(row[z > 451] - inc[z > 451])) > 0.15, "t = 4.5 us: right of 450 m the echo adds (difference up to 1/6)")
close(4.5 - 6 + 450 / C, 0, "echo front at t + z/v - 6 = 0 -> z = 450 m at 4.5 us")
# steady state: amplitude over one period for t in [7, 8]
m = (t >= 7) & (t < 8)
amp = 0.5 * (VV[m].max(axis=0) - VV[m].min(axis=0))
close(amp.max(), 2 / 3, "t > 6 us: amplitude max 2/3", atol=2e-4)
close(amp.min(), 1 / 3, "t > 6 us: amplitude min 1/3", atol=2e-4)
ap = np.concatenate(([-1], amp, [-1])); am = np.concatenate(([9], amp, [9]))
imax = [i for i in range(len(amp)) if ap[i + 1] >= ap[i] and ap[i + 1] >= ap[i + 2] and amp[i] > 0.6]
imin = [i for i in range(len(amp)) if am[i + 1] <= am[i] and am[i + 1] <= am[i + 2] and amp[i] < 0.4]
ok([int(z[i]) for i in imax] == [0, 150, 300, 450, 600, 750, 900], f"amplitude maxima at {[int(z[i]) for i in imax]} m: every 150 m, one at the load")
ok([int(z[i]) for i in imin] == [75, 225, 375, 525, 675, 825], f"amplitude minima at {[int(z[i]) for i in imin]} m")
Vss = 0.5 * np.sin(w * Tg - w / C * Zg) + (1 / 6) * np.sin(w * Tg + w / C * Zg)
close(Vss[t > 6], VV[t > 6], "t > 6 us: V = 1/2 sin(wt - beta z) + 1/6 sin(wt + beta z), beta = w/v", atol=1e-9)
r = fdtd(50, C, 900, 50, 100, F.f_ex1, 9.0, 1800, snaps=(1.0, 2.0, 4.5, 8.0))
for ts in (1.0, 2.0, 4.5, 8.0):
    zf, Vf, If = r["snap"][ts]
    Vser, ZIser = F.series(zf / C, ts, F.f_ex1, **F.EX1)
    close(Vf, Vser, f"FDTD (Courant 0.5) vs series, t = {ts} us, V", atol=0.01)
    close(50 * If, ZIser, f"FDTD vs series, t = {ts} us, Z0 I", atol=0.01)

print("=== D. Example 2 (unit step, z = 1200 m)")
z, t, VV, II = moc(50, C, 2400, 0, 100, F.f_step, 60.0, 240)
k = int(np.argmin(np.abs(z - 1200)))
Vs, ZIs = F.series(1200 / C, t, F.f_step, **F.EX2)
mk = away(t, [4, 12, 20, 28, 36, 44, 52, 60], 0.05)
close(Vs[mk], VV[mk, k], "series (figure) = MoC: V(1200, t), 0-60 us", atol=1e-9)
close(ZIs[mk], 50 * II[mk, k], "series = MoC: Z0 I(1200, t)", atol=1e-9)
Vnotes = sum(a * (t >= tt) for a, tt in ((1, 4), (1 / 3, 12), (-1 / 3, 20), (-1 / 9, 28), (1 / 9, 36), (1 / 27, 44), (-1 / 27, 52)))
close(Vnotes[mk], VV[mk, k], "notes: V(1200,t) = u(t-4) + 1/3 u(t-12) - 1/3 u(t-20) - 1/9 u(t-28) + 1/9 u(t-36) + 1/27 u(t-44) - 1/27 u(t-52)", atol=1e-9)
levels = [VV[int(round(tm * 30)), k] for tm in (8, 16, 24, 32, 40, 48, 56)]
close(levels, [1, 4 / 3, 1, 8 / 9, 1, 28 / 27, 1], "levels 1, 4/3, 1, 8/9, 1, 28/27, 1 V (and the notes' margin plot)", atol=1e-9)
ok(VV[int(round(2 * 30)), k] == 0, "V(1200, t) = 0 before 4 us")
ilev = [1000 * II[int(round(tm * 30)), k] for tm in (8, 16, 24, 32, 40, 48, 56)]
close(ilev, [20, 40 / 3, 20 / 3, 80 / 9, 100 / 9, 280 / 27, 260 / 27], "I(1200,t) levels 20, 13.3, 6.7, 8.9, 11.1, 10.4, 9.6 mA", atol=1e-9)
close(np.round(ilev, 1), [20.0, 13.3, 6.7, 8.9, 11.1, 10.4, 9.6], "  (as printed, one decimal)", atol=1e-9)
dev = np.array(levels) - 1
close(dev[1::2][1:] / dev[1::2][:-1], [-1 / 3, -1 / 3], "trap: deviation from 1 V shrinks threefold per round trip, alternating in sign (1/3, -1/9, 1/27)", atol=1e-9)
close([levels[1] / 50 * 1000, ilev[1]], [80 / 3, 40 / 3], "trap: on 12-20 us V/Z0 = 26.7 mA but I = 13.3 mA", atol=1e-9)
ZInotes = sum(a * (t >= tt) for a, tt in ((1, 4), (-1 / 3, 12), (-1 / 3, 20), (1 / 9, 28), (1 / 9, 36), (-1 / 27, 44), (-1 / 27, 52)))
close(ZInotes[mk], 50 * II[mk, k], "page: Z0 I(1200,t) = u(t-4) - 1/3 u(t-12) - 1/3 u(t-20) + 1/9 u(t-28) + 1/9 u(t-36) - ...", atol=1e-9)
# Gamma_g = -1: a backward leg and the forward leg it launches cancel at every z after both pass
lg = F.legs(1.0, 1 / 3, -1.0, 8.0, 200.0)
ok(all(np.isclose(lg[i][4], -lg[i + 1][4]) for i in range(1, len(lg) - 1, 2)), "Gamma_g = -1: each forward leg (n >= 1) = minus the backward leg before it")
# impulse response weights at z = 1200 from a narrow unit-area pulse
wdt = 0.2
tri = lambda s: np.clip(1 - np.abs(np.asarray(s, float) - wdt) / wdt, 0, None) / wdt
z2, t2, V2, I2 = moc(50, C, 2400, 0, 100, tri, 60.0, 2400)
k2 = int(np.argmin(np.abs(z2 - 1200))); dt2 = t2[1] - t2[0]
areas = [np.sum(V2[(t2 > T - 1) & (t2 < T + 1.5), k2]) * dt2 for T in (4, 12, 20, 28, 36, 44, 52)]
close(areas, [1, 1 / 3, -1 / 3, -1 / 9, 1 / 9, 1 / 27, -1 / 27], "impulse response h_1200(t): areas of the arrivals at 4, 12, 20, ... us", atol=1e-6)
cur_areas = [50 * np.sum(I2[(t2 > T - 1) & (t2 < T + 1.5), k2]) * dt2 for T in (4, 12, 20, 28)]
close(cur_areas, [1, -1 / 3, -1 / 3, 1 / 9], "current impulse response: left-moving legs flip sign", atol=1e-6)
# DC limit by a long run
z3, t3, V3, I3 = moc(50, C, 2400, 0, 100, F.f_step, 600.0, 24)
close(V3[-1, 12], 1.0, "t -> infinity: V(1200) -> 1 V", atol=1e-9)
close(1000 * I3[-1, 12], 10.0, "t -> infinity: I(1200) -> 10 mA = 1 V / 100 ohm", atol=1e-9)
close(V3[-1], 1.0, "t -> infinity: V = 1 V at every z (pair of wires)", atol=1e-9)
fs = fs_step
r = fdtd(50, C, 2400, 0, 100, fs, 60.0, 4800, probes=(1200,))
tf = r["t"]
Vser, ZIser = F.series(1200 / C, tf, fs, **F.EX2)
close(r["V"][1200], Vser, "FDTD (smoothed step) vs series: V(1200,t), 0-60 us", atol=0.01)
close(50 * r["I"][1200], ZIser, "FDTD (smoothed step) vs series: Z0 I(1200,t)", atol=0.01)

print("=== E. DC limit in general (folded derivation on the page)")
rng = np.random.default_rng(29)
for _ in range(2000):
    Z0, Rg, RL = rng.uniform(1, 300), rng.uniform(0, 500), rng.uniform(0.1, 1000)
    tg, Gg, GL = Z0 / (Rg + Z0), (Rg - Z0) / (Rg + Z0), (RL - Z0) / (RL + Z0)
    assert np.isclose(tg * (1 + GL) / (1 - GL * Gg), RL / (Rg + RL), rtol=1e-12)
    assert np.isclose(tg * (1 - GL) / (1 - GL * Gg), Z0 / (Rg + RL), rtol=1e-12)
    assert abs(GL * Gg) < 1
ok(True, "2000 random circuits: tau_g(1 + G_L)/(1 - G_L G_g) = R_L/(R_g + R_L); tau_g(1 - G_L)/(1 - G_L G_g) = Z0/(R_g + R_L); |G_L G_g| < 1")
for Rg, RL in ((25, 150), (0, 100), (100, 25), (60, 1e-9)):
    zz, tt, Vd, Id = moc(50, 200, 600, Rg, RL, F.f_step, 3000.0, 6)
    close([Vd[-1, 3], Id[-1, 3]], [RL / (Rg + RL), 1 / (Rg + RL)], f"MoC long run R_g = {Rg}, R_L = {RL:g}: V, I -> lumped DC values", atol=1e-6)

print("=== F. Example 3 (two-level pulse on Example 2's circuit)")
z, t, VV, II = moc(50, C, 2400, 0, 100, F.f_ex3, 14.0, 480, t0=-1.0)
Zg, Tg = np.meshgrid(z, t)
Vs, ZIs = F.series(Zg / C, Tg, F.f_ex3, **F.EX2)
fx = lambda s: F.f_ex3(s)
Vn = sum((-1 / 3) ** n * (fx(Tg - Zg / C - 16 * n) + (1 / 3) * fx(Tg + Zg / C - 16 * (n + 1))) for n in range(4))
In = sum((-1 / 3) ** n * (fx(Tg - Zg / C - 16 * n) - (1 / 3) * fx(Tg + Zg / C - 16 * (n + 1))) for n in range(4)) / 50
edges_t = lambda zz_: [-0.5 + zz_ / C, 0.5 + zz_ / C, 1.5 + zz_ / C]
mask = np.ones_like(Tg, dtype=bool)
for e in (-0.5, 0.5, 1.5):
    for sgn, off in ((1, 0), (-1, 16)):
        mask &= np.abs((Tg - sgn * Zg / C - off) - e) > 0.03
close(Vs[mask], VV[mask], "series (figure) = MoC on the grid, -1..14 us, away from the jumps", atol=1e-9)
close(Vn[mask], VV[mask], "notes' V(z,t) = sum (-1/3)^n [f(t - z/c - 16n) + 1/3 f(t + z/c - 16(n+1))]", atol=1e-9)
close(In[mask], II[mask], "notes' I(z,t) = (1/50)[first sum - (1/3) second sum]", atol=1e-9)
zz = np.linspace(0, 2400, 4801)


def snap(ts):
    return F.series(zz / C, ts, F.f_ex3, **F.EX2)


def piece(ts, pieces, label):
    V, ZI = snap(ts)
    edges = [p[0] for p in pieces] + [p[1] for p in pieces]
    m = away(zz, edges, 2)
    target_V = np.zeros_like(zz); target_I = np.zeros_like(zz)
    for a, b, v, i in pieces:
        sel = (zz > a) & (zz < b)
        target_V[sel] = v; target_I[sel] = i
    close(V[m], target_V[m], f"{label}: V pieces {[(a, b, round(v, 4)) for a, b, v, _ in pieces]}", atol=1e-12)
    close((ZI / 50 * 1000)[m], target_I[m], f"{label}: I pieces (mA) {[round(i, 2) for *_, i in pieces]}", atol=1e-9)
    n = int(round((ts + 1.0) * C / 5.0))
    Vm = np.interp(zz, z, VV[n]); Im = np.interp(zz, z, II[n]) * 1000
    m2 = away(zz, edges, 12)
    close(Vm[m2], target_V[m2], f"{label}: MoC snapshot agrees", atol=1e-9)
    close(Im[m2], target_I[m2], f"{label}: MoC current snapshot agrees", atol=1e-9)


piece(3.0, [(450, 750, 2, 40), (750, 1050, 1, 20)], "t = 3 us")
piece(11.0, [(1350, 1650, 1 / 3, -20 / 3), (1650, 1950, 2 / 3, -40 / 3)], "t = 11 us")
piece(9.0, [(1950, 2250, 1 / 3, -20 / 3), (2250, 2400, 8 / 3, 80 / 3)], "t = 9 us (site example)")
ok(np.isclose((8 / 3) / (80 / 3 / 1000), 100), "t = 9 us, 2250-2400 m: V/I = (8/3 V)/(26.7 mA) = 100 ohm = R_L")
ok(np.isclose((2 - 2 / 3) / 50 * 1000, 80 / 3), "I = (2 - 2/3)/50 A = 26.7 mA")
fs = fs_ex3
r = fdtd(50, C, 2400, 0, 100, fs, 11.5, 4800, snaps=(3.0, 9.0, 11.0), t0=-1.0)
for ts in (3.0, 9.0, 11.0):
    zf, Vf, If = r["snap"][ts]
    Vser, ZIser = F.series(zf / C, ts, fs, **F.EX2)
    close(Vf, Vser, f"FDTD (smoothed pulse) vs series, t = {ts} us, V(z)", atol=0.01)
    close(50 * If, ZIser, f"FDTD (smoothed pulse) vs series, t = {ts} us, Z0 I(z)", atol=0.01)

print("=== G. worked problem (ramp pulse, Z0 = 50, R_g = 25, R_L = 150, l = 600 m, v = 200 m/us)")
v = 200.0
z, t, VV, II = moc(50, v, 600, 25, 150, F.f_ramp, 13.0, 600)
Zg, Tg = np.meshgrid(z, t)
Vs, ZIs = F.series(Zg / v, Tg, F.f_ramp, **F.PRB)
mask = np.ones_like(Tg, dtype=bool)
for off in range(0, 14, 3):
    mask &= np.abs(np.abs(Tg - off) - Zg / v) > 0.0  # ramp is continuous at 0; jump at 1
for e in (1.0,):
    for n in range(3):
        mask &= np.abs((Tg - Zg / v - 6 * n) - e) > 0.02
        mask &= np.abs((Tg + Zg / v - 6 * (n + 1)) - e) > 0.02
close(Vs[mask], VV[mask], "series (figure) = MoC, V(z,t), 0-13 us", atol=1e-9)
close(ZIs[mask], 50 * II[mask], "series = MoC, Z0 I(z,t)", atol=1e-9)
zz = z                                   # MoC nodes, 1 m apart (no interpolation across the jumps)


def at(ts):
    n = int(round(ts * v))
    return VV[n], II[n] * 1000


V, I = at(2.0)
sel = (zz > 200) & (zz < 400)
close(V[sel], 4 - zz[sel] / 100, "t = 2 us: V = 4 - z/100 V on 200-400 m", atol=1e-9)
close(I[sel], (4 - zz[sel] / 100) / 50 * 1000, "t = 2 us: I = V/50 (40 mA peak)", atol=1e-9)
close(V[(zz <= 200) | (zz >= 400)], 0, "t = 2 us: zero elsewhere")
close([V[201], V[399]], [1.99, 0.01], "t = 2 us: 2 V at 200 m (sent last), 0 at 400 m (front)", atol=1e-9)
V, I = at(5.0)
sel = (zz > 200) & (zz < 400)
close(V[sel], zz[sel] / 200 - 1, "t = 5 us: V = z/200 - 1 V on 200-400 m (echo only)", atol=1e-9)
close(I[sel], -(zz[sel] / 200 - 1) / 50 * 1000, "t = 5 us: I = -V/50 (-20 mA peak)", atol=1e-9)
close(V[(zz <= 200) | (zz >= 400)], 0, "t = 5 us: zero elsewhere (second forward leg starts at 6 us)")
V, I = at(3.5)
sel = (zz > 500) & (zz <= 600)
close(V[sel], 4.5 - zz[sel] / 200, "t = 3.5 us: V = (7 - z/100) + (z/200 - 2.5) = 4.5 - z/200 on 500-600 m", atol=1e-9)
close(I[sel], (9.5 - 3 * zz[sel] / 200) / 50 * 1000, "t = 3.5 us: I = (9.5 - 0.015 z)/50 A", atol=1e-9)
close([V[501], V[600], I[501], I[600]], [2.0 - 0.005, 1.5, 40 - 0.3, 10.0], "t = 3.5 us: 2 V, 40 mA at 500 m; 1.5 V, 10 mA at 600 m", atol=1e-9)
close(V[zz <= 500], 0, "t = 3.5 us: zero left of 500 m")
close(V[-1] / (I[-1] / 1000), 150, "t = 3.5 us: V/I at the load = 150 ohm = R_L", atol=1e-6)
close(VV[int(round(3.5 * v)), -1], 1.5 * 1.0, "(1 + Gamma_L) V+(l) = 1.5 x 1 V", atol=1e-9)
# generator end
tt = t
V0, I0 = VV[:, 0], II[:, 0] * 1000
m = (tt > 0) & (tt < 1)
close(V0[m], 2 * tt[m], "V(0,t) = 2t V for 0 < t < 1 us", atol=1e-9)
close(I0[m], 40 * tt[m], "I(0,t) = 40t mA for 0 < t < 1 us", atol=1e-9)
m = (tt > 1.01) & (tt < 5.99)
close([np.max(np.abs(V0[m])), np.max(np.abs(I0[m]))], [0, 0], "V(0,t) = I(0,t) = 0 for 1 < t < 6 us")
m = (tt > 6) & (tt < 6.99)
close(V0[m], (2 / 3) * (tt[m] - 6), "V(0,t) = (1 + Gamma_g)(t - 6) = 2/3 (t - 6) V for 6 < t < 7 us", atol=1e-9)
close(I0[m], -(4 / 3) * (tt[m] - 6) / 50 * 1000, "I(0,t) = -(1 - Gamma_g)(t - 6)/50 = -26.7 (t - 6) mA", atol=1e-9)
close(V0[m], -25 * I0[m] / 1000, "KVL at the source with f_i = 0: V(0,t) = -R_g I(0,t)", atol=1e-9)
m = (tt > 7.01) & (tt < 11.99)
close([np.max(np.abs(V0[m])), np.max(np.abs(I0[m]))], [0, 0], "V(0,t) = I(0,t) = 0 for 7 < t < 12 us (next echo back at 12 us)")
Vp, ZIp = F.series(0.0, 7 - 1e-12, F.f_ramp, **F.PRB)
close([Vp, ZIp / 50 * 1000], [2 / 3, -80 / 3], "peaks as t -> 7 us (series, equal to MoC above): 0.667 V, -26.7 mA", atol=1e-9)
# load voltage timeline (used in the pattern / check)
VLm = VV[:, -1]
m = (tt > 3) & (tt < 3.99)
close(VLm[m], 1.5 * 2 * (tt[m] - 3), "V(l,t) = (1 + Gamma_L) 2(t - 3) = 3(t - 3) V for 3 < t < 4 us", atol=1e-9)
fs = fs_ramp
r = fdtd(50, v, 600, 25, 150, fs, 8.0, 2400, snaps=(2.0, 3.5, 5.0), probes=(0.0,))
for ts in (2.0, 3.5, 5.0):
    zf, Vf, If = r["snap"][ts]
    Vser, ZIser = F.series(zf / v, ts, fs, **F.PRB)
    close(Vf, Vser, f"FDTD (smoothed ramp) vs series, t = {ts} us, V(z)", atol=0.01)
    close(50 * If, ZIser, f"FDTD (smoothed ramp) vs series, t = {ts} us, Z0 I(z)", atol=0.01)
Vser, ZIser = F.series(0.0, r["t"], fs, **F.PRB)
close(r["V"][0.0], Vser, "FDTD vs series: V(0,t), 0-8 us", atol=0.01)
close(50 * r["I"][0.0], ZIser, "FDTD vs series: Z0 I(0,t), 0-8 us", atol=0.01)

print(f"\nALL {ok_count} CHECKS PASSED")
