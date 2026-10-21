#!/usr/bin/env python3
"""Verification of every number, sign and direction on the Lecture 28 pages of the ECE 329 study site.

Pages checked:
  content-src/4-transmission-lines/28-distributed-circuits-and-bounce-diagrams.md   (sections A-F)
  content-src/concepts/bounce-diagram.md                                            (section H)
  content-src/problems/reading-a-line-from-two-pulses.md                            (section G)
  figs_l28.py: figure numbers and labels                                            (section I)

Three independent routes, numpy only:
  1. the bounce-diagram series (the page's formulas): weights tau_g (G_L G_g)^n, tau_g G_L (G_L G_g)^n;
  2. FDTD of the telegrapher's equations (Yee leapfrog, Courant number 1) with the generator's KVL and the load's
     Ohm's law discretized on half cells at the two ends -- no reflection coefficient appears anywhere in it;
  3. the Laplace-domain line solution from the ABCD (cosh/sinh) matrix with a Thevenin source and a resistive load,
     compared with the Laplace transform of the series at complex s, and its s -> 0 limit (DC).
Conventions (as on the page): z = 0 generator, z = l load; V of the upper wire relative to the lower; I along +z on
the upper wire; forward wave I = +V/Z0, backward I = -V/Z0; T = l/v.
"""
import numpy as np

ok_count = 0


def ok(cond, msg):
    global ok_count
    assert cond, "FAILED: " + msg
    ok_count += 1
    print("ok  ", msg)


def close(a, b, msg, rtol=1e-9, atol=1e-12):
    a_, b_ = np.asarray(a), np.asarray(b)
    shown = f"max |diff| {np.max(np.abs(a_ - b_)):.1e} over {a_.size} values" if a_.size > 6 else f"{np.round(a, 6)} vs {np.round(b, 6)}"
    ok(np.allclose(a, b, rtol=rtol, atol=atol), f"{msg}: {shown}")


# ---------------------------------------------------------------------------------------------- the page's formulas
def coefs(Z0, Rg, RL):
    tg = Z0 / (Rg + Z0)
    Gg = 1.0 if np.isinf(Rg) else (Rg - Z0) / (Rg + Z0)
    GL = 1.0 if np.isinf(RL) else (RL - Z0) / (RL + Z0)
    return tg, Gg, GL


def bounce_events(Z0, Rg, RL, zp, T, l, tmax, amp=1.0):
    """list of (arrival time at zp, voltage weight, direction +1/-1) from the bounce diagram"""
    tg, Gg, GL = coefs(Z0, Rg, RL)
    v = l / T
    ev = []
    n = 0
    while True:
        tf = zp / v + 2 * n * T
        tb = (2 * l - zp) / v + 2 * n * T
        if tf > tmax and tb > tmax:
            break
        if tf <= tmax:
            ev.append((tf, amp * tg * (GL * Gg) ** n, +1))
        if tb <= tmax:
            ev.append((tb, amp * tg * GL * (GL * Gg) ** n, -1))
        n += 1
    return sorted(ev)


def bounce_step(Z0, Rg, RL, zp, T, l, t, V0=1.0):
    """V(zp,t), I(zp,t) for f_i = V0 u(t): running sums of the crossed weights"""
    ev = bounce_events(Z0, Rg, RL, zp, T, l, np.max(t) + 1e-12, V0)
    t = np.asarray(t, float)
    V = np.zeros_like(t); I = np.zeros_like(t)
    for tk, w, d in ev:
        V += w * (t > tk)
        I += d * w / Z0 * (t > tk)
    return V, I


# ---------------------------------------------------------------------------------------------- FDTD (independent)
def fdtd(Z0, Rg, RL, l, v, fi, tmax, N=1200, probes=()):
    """Leapfrog telegrapher's equations, dt = dz/v. Returns t_nodes, V at probe nodes (dict), I at probe half-nodes
    (dict, sampled at the half-step times, given at t_half), and V at both ends.
    Lperm = Z0/v, Cperm = 1/(Z0 v). Ends: generator KVL f_i = Rg I_s + V(0), load V(l) = RL I_L, each on a half cell."""
    dz = l / N; dt = dz / v
    nsteps = int(np.ceil(tmax / dt))
    V = np.zeros(N + 1); I = np.zeros(N)
    pk = {zp: int(round(zp / dz)) for zp in probes}
    Vp = {zp: np.zeros(nsteps + 1) for zp in probes}
    Ip = {zp: np.zeros(nsteps) for zp in probes}
    V0h = np.zeros(nsteps + 1); VNh = np.zeros(nsteps + 1)
    ideal = (Rg == 0)
    if ideal:
        V[0] = fi(0.0)
    for zp, k in pk.items():
        Vp[zp][0] = V[k]
    V0h[0] = V[0]; VNh[0] = V[N]
    for n in range(nsteps):
        # I at (n+1/2) dt
        I -= (V[1:] - V[:-1]) / Z0                  # dt/(L dz) = 1/Z0
        for zp, k in pk.items():
            kk = min(k, N - 1)
            Ip[zp][n] = I[kk] if k < N else I[N - 1]
        Vn = V.copy()
        # interior nodes
        V[1:-1] = Vn[1:-1] - Z0 * (I[1:] - I[:-1])   # dt/(C dz) = Z0
        # generator node: (C dz/2) dV0/dt = (f_i - V0)/Rg - I_1/2, trapezoidal V0 in the source current
        th = (n + 0.5) * dt
        if ideal:
            V[0] = fi((n + 1) * dt)
        else:
            V[0] = (Vn[0] * (Rg - Z0) + 2 * Z0 * fi(th) - 2 * Z0 * Rg * I[0]) / (Rg + Z0)
        # load node: (C dz/2) dVN/dt = I_{N-1/2} - VN/RL
        if np.isinf(RL):
            V[N] = Vn[N] + 2 * Z0 * I[N - 1]
        else:
            V[N] = (Vn[N] * (RL - Z0) + 2 * Z0 * RL * I[N - 1]) / (RL + Z0)
        for zp, k in pk.items():
            Vp[zp][n + 1] = V[k]
        V0h[n + 1] = V[0]; VNh[n + 1] = V[N]
    t = np.arange(nsteps + 1) * dt
    th = (np.arange(nsteps) + 0.5) * dt
    return t, th, Vp, Ip, V0h, VNh, dz


def plateau(t, x, a, b):
    """mean of x over the middle 60 % of (a, b)"""
    m = (t > a + 0.2 * (b - a)) & (t < b - 0.2 * (b - a))
    return x[m].mean()


def pulse_areas(t, x, times, half_window):
    out = []
    dt = t[1] - t[0]
    for tk in times:
        m = np.abs(t - tk) < half_window
        out.append(x[m].sum() * dt)
    return np.array(out)


def smooth_step(V0, tr):
    """V0 u(t) with a raised-cosine rise of length tr (a hard step excites the grid's odd-even mode at Courant 1)"""
    return lambda t: V0 * np.where(t <= 0, 0.0, np.where(t >= tr, 1.0, 0.5 - 0.5 * np.cos(np.pi * np.clip(t, 0, tr) / tr)))


def gauss(t0, sig, area):
    return lambda t: area * np.exp(-0.5 * ((t - t0) / sig) ** 2) / (sig * np.sqrt(2 * np.pi))


# ---------------------------------------------------------------------------------------------- Laplace (independent)
def laplace_V(Z0, Rg, RL, l, v, z, s):
    """V(z,s)/F(s) from the ABCD matrix of the lossless line (gamma = s/v), Thevenin source, resistive load"""
    def abcd(L):
        g = s * L / v
        return np.array([[np.cosh(g), Z0 * np.sinh(g)], [np.sinh(g) / Z0, np.cosh(g)]])
    M = abcd(l)                                 # [V0; I0] = M [VL; IL], VL = RL IL
    col = M @ np.array([RL, 1.0])               # [V0; I0] per unit IL
    IL = 1.0 / (col[0] + Rg * col[1])           # F = V0 + Rg I0 = 1
    Mz = abcd(l - z)
    Vz, Iz = Mz @ np.array([RL * IL, IL])
    return Vz, Iz


def series_laplace(Z0, Rg, RL, l, v, z, s):
    tg, Gg, GL = coefs(Z0, Rg, RL)
    T = l / v
    D = 1 - GL * Gg * np.exp(-2 * s * T)
    Vs = tg * (np.exp(-s * z / v) + GL * np.exp(-s * (2 * T - z / v))) / D
    Is = tg / Z0 * (np.exp(-s * z / v) - GL * np.exp(-s * (2 * T - z / v))) / D
    return Vs, Is


rng = np.random.default_rng(28)

print("=== A. notes' derivation (pp. 2-5), symbolic steps checked with random values")
for _ in range(5):
    Z0, Rg, RL = rng.uniform(10, 200, 3)
    tg, Gg, GL = coefs(Z0, Rg, RL)
    # load: V/I = Z0 (f+g)/(f-g) = RL with g = GL f
    f = rng.normal(); g = GL * f
    close(Z0 * (f + g) / (f - g), RL, f"load: Z0(f+g)/(f-g) = RL with g = Gamma_L f (Z0={Z0:.1f}, RL={RL:.1f})")
    # first epoch: fi = Rg f/Z0 + f  =>  f = tau_g fi
    fi = rng.normal(); fpred = tg * fi
    close(Rg * fpred / Z0 + fpred, fi, "first epoch KVL: fi = Rg f/Z0 + f with f = tau_g fi")
    # second epoch: fi = (1+Rg/Z0) f(t) + (1-Rg/Z0) GL f(t-2T); f(t-2T) = tau_g fi(t-2T)
    fi_now, fi_old = rng.normal(size=2)
    f_old = tg * fi_old
    f_now = tg * fi_now + Gg * GL * f_old
    close((1 + Rg / Z0) * f_now + (1 - Rg / Z0) * GL * f_old, fi_now, "second epoch KVL holds with f = tau_g fi + Gamma_g Gamma_L f(t-2T)")
    close(-(1 - Rg / Z0) / (1 + Rg / Z0), Gg, "-(1 - Rg/Z0)/(1 + Rg/Z0) = Gamma_g")
    close(tg, (1 - Gg) / 2, "tau_g = (1 - Gamma_g)/2")
    close(Rg * (f_now - GL * f_old) / Z0 + (f_now + GL * f_old), fi_now, "the notes' p. 3 KVL form, R_g I(0,t) + V(0,t) = f_i")
for R in (0.0, 1.0, 50.0, 1e3, 1e9):
    ok(-1 <= (R - 50) / (R + 50) <= 1, f"|Gamma| <= 1 for R = {R:g} (passive)")
# p. 8: delta(t - Tz) * fi = fi(t - Tz); backward term delta(t + z/v - 2l/v) has delay Tz = 2l/v - z/v > 0 (errata 1)
l_, v_, z_ = 1.0, 1.0, 0.3
Tz_back = 2 * l_ / v_ - z_ / v_
ok(Tz_back > 0, f"backward-term delay 2l/v - z/v = {Tz_back} > 0 (the notes print z/v - 2l/v, an advance)")

print("=== B. series (page section 4) = Laplace-domain line solution at complex s (independent algebra)")
for _ in range(6):
    Z0, Rg, RL = rng.uniform(10, 200, 3)
    l, v = rng.uniform(10, 1000), rng.uniform(1e8, 3e8)
    T = l / v
    z = rng.uniform(0, l)
    s = (rng.uniform(0.05, 2) + 1j * rng.uniform(-20, 20)) / T
    Va, Ia = laplace_V(Z0, Rg, RL, l, v, z, s)
    Vb, Ib = series_laplace(Z0, Rg, RL, l, v, z, s)
    close(Va, Vb, f"V(z,s)/F(s): ABCD vs bounce series (z/l = {z/l:.2f})", rtol=1e-8)
    close(Ia, Ib, "I(z,s)/F(s): ABCD vs bounce series (backward weights with minus sign)", rtol=1e-8)
    # DC: s -> 0 gives the divider
    Vdc, Idc = laplace_V(Z0, Rg, RL, l, v, z, 1e-9 / T)
    close(Vdc.real, RL / (Rg + RL), "s -> 0: V = RL/(Rg+RL) at every z", rtol=1e-6)
    close(Idc.real, 1 / (Rg + RL), "s -> 0: I = 1/(Rg+RL)", rtol=1e-6)
    tg, Gg, GL = coefs(Z0, Rg, RL)
    close(tg * (1 + GL) / (1 - GL * Gg), RL / (Rg + RL), "tau_g (1+G_L)/(1 - G_L G_g) = RL/(Rg+RL)")
    close(tg * (1 - GL) / (Z0 * (1 - GL * Gg)), 1 / (Rg + RL), "tau_g (1-G_L)/(Z0 (1 - G_L G_g)) = 1/(Rg+RL)")

print("=== C. impulse weights by FDTD (narrow Gaussian input of unit area), generic circuit")
Z0, Rg, RL = 50.0, 20.0, 300.0
l, v = 100.0, 2e8
T = l / v
zp = 0.3 * l
sig = T / 150
t, th, Vp, Ip, V0h, VNh, dz = fdtd(Z0, Rg, RL, l, v, gauss(5 * sig, sig, 1.0), 7 * T, N=3000, probes=(zp,))
ev = bounce_events(Z0, Rg, RL, zp, T, l, 6.5 * T)
times = np.array([e[0] for e in ev]) + 5 * sig
wV = np.array([e[1] for e in ev]); wI = np.array([e[2] * e[1] / Z0 for e in ev])
aV = pulse_areas(t, Vp[zp], times, 0.1 * T)
aI = pulse_areas(th, Ip[zp], times, 0.1 * T)
close(aV, wV, "V(0.3l, t): FDTD impulse areas = tau_g (G_LG_g)^n, tau_g G_L (G_LG_g)^n at z/v + 2nT, (2l - z)/v + 2nT", rtol=3e-3, atol=3e-5)
close(aI, wI, "I(0.3l, t): FDTD areas = +w/Z0 forward, -w/Z0 backward", rtol=3e-3, atol=3e-7)
tot = Vp[zp].sum() * (t[1] - t[0])
close(tot, wV.sum(), "nothing else arrives at 0.3l (total area = sum of the weights)", rtol=3e-3, atol=3e-5)

print("=== D. page example (sections 4-5): Z0 = 60, Rg = 180, RL = 20, 12 V (review: re-parameterized from 50/150/50/3)")
Z0, Rg, RL, V0 = 60.0, 180.0, 20.0, 12.0
tg, Gg, GL = coefs(Z0, Rg, RL)
close([tg, Gg, GL], [0.25, 0.5, -0.5], "tau_g = 1/4, Gamma_g = 1/2, Gamma_L = -1/2")
close(GL * Gg, -0.25, "Gamma_L Gamma_g = -1/4")
l, v = 300.0, 3e8                     # T = 1 us (any T works: results scale with t/T)
T = l / v
evL = bounce_events(Z0, Rg, RL, l / 2, T, l, 6 * T, V0)
close([w for _, w, _ in evL], [3, -1.5, -0.75, 0.375, 0.1875, -0.09375], "12 V weights: 3, -1.5, -0.75, 0.375, 0.1875, -0.09375")
# section 4 example, f_i = delta(t): weights 1/4, -1/8, -1/16, 1/32 at T/2, 3T/2, 5T/2, 7T/2; Z0 I flips backward signs
ev1 = bounce_events(Z0, Rg, RL, l / 2, T, l, 3.6 * T, 1.0)
close([e[1] for e in ev1], [1 / 4, -1 / 8, -1 / 16, 1 / 32], "h_{l/2}: 1/4, -1/8, -1/16, +1/32")
close([e[2] * e[1] for e in ev1], [1 / 4, 1 / 8, -1 / 16, -1 / 32], "Z0 I(l/2): +1/4, +1/8, -1/16, -1/32")
close([e[2] for e in ev1], [1, -1, 1, -1], "2nd and 4th impulses at l/2 are backward")
# impulse 12 delta(t): V(l/2,t) and I(l/2,t)
ev_half = bounce_events(Z0, Rg, RL, l / 2, T, l, 3.6 * T, V0)
close([e[0] / T for e in ev_half], [0.5, 1.5, 2.5, 3.5], "crossings of z = l/2 at T/2, 3T/2, 5T/2, 7T/2")
close([e[2] * e[1] / Z0 for e in ev_half], [0.05, 0.025, -0.0125, -0.00625], "I(l/2): 3/60, +1.5/60, -0.75/60, -0.375/60 A (backward weights flip sign)")
t, th, Vp, Ip, V0h, VNh, dz = fdtd(Z0, Rg, RL, l, v, smooth_step(V0, T / 100), 9 * T, N=2000, probes=(l / 2,))
VL_page = [1.5, 1.125, 1.21875, 1.1953125]
for k, val in enumerate(VL_page):
    a, b = (2 * k + 1) * T, (2 * k + 3) * T
    close(plateau(t, VNh, a, b), val, f"FDTD V(l,t) on ({2*k+1}T, {2*k+3}T) = {val} V", rtol=2e-3)
Vhalf_page = [3.0, 1.5, 0.75, 1.125, 1.3125, 1.21875, 1.171875]
for k, val in enumerate(Vhalf_page):
    a, b = (k + 0.5) * T, (k + 1.5) * T
    close(plateau(t, Vp[l / 2], a, b), val, f"FDTD V(l/2,t) on ({k+0.5}T, {k+1.5}T) = {val} V", rtol=2e-3)
Vb, Ib = bounce_step(Z0, Rg, RL, l / 2, T, l, np.array([(k + 1.0) * T for k in range(7)]), V0)
close(Vb, Vhalf_page, "bounce running sums at z = l/2 match the same list")
Ihalf = [0.05, 0.075, 0.0625, 0.05625, 0.059375, 0.0609375, 0.06015625]
close(Ib, Ihalf, "bounce I(l/2,t) running sums: 50, 75, 62.5, 56.25, 59.38, 60.94, 60.16 mA")
for k, val in enumerate(Ihalf):
    a, b = (k + 0.5) * T, (k + 1.5) * T
    close(plateau(th, Ip[l / 2], a, b), val, f"FDTD I(l/2,t) on ({k+0.5}T, {k+1.5}T) = {val*1e3:.4g} mA", rtol=3e-3)
close(plateau(t, V0h, 0, 2 * T), 3.0, "FDTD V(0,t) = tau_g 12 = 3 V for 0 < t < 2T", rtol=2e-3)
close(plateau(t, V0h, 2 * T, 4 * T), 3 + (-1.5) * (1 + Gg), "FDTD V(0,t) = 3 + (-1.5)(1 + Gamma_g) = 0.75 V on (2T, 4T)", rtol=3e-3)
Vdc = V0 * RL / (Rg + RL); Idc = V0 / (Rg + RL)
close([Vdc, Idc], [1.2, 0.06], "DC: V = 12*20/200 = 1.2 V, I = 60 mA")
t2, th2, Vp2, Ip2, V0h2, VNh2, _ = fdtd(Z0, Rg, RL, l, v, smooth_step(V0, T / 5), 40 * T, N=400, probes=(0.37 * l,))
last2 = lambda x: 0.5 * (x[-1] + x[-2])           # average the two sublattices of the Courant-1 grid
close([last2(VNh2), last2(V0h2), last2(Vp2[0.37 * l])], [Vdc] * 3, "FDTD t = 40T: V = 1.2 V at z = 0, 0.37l, l", rtol=1e-4)
close(last2(Ip2[0.37 * l]), Idc, "FDTD t = 40T: I = 60 mA", rtol=1e-4)
close(V0 * tg * (1 + GL) / (1 - GL * Gg), 1.2, "series form: 12 (1/4)(1/2)/(5/4) = 1.2 V")
close([round(1.21875, 3), round(1.1953125, 3)], [1.219, 1.195], "page rounds 1.21875 -> 1.219, 1.1953125 -> 1.195")
close(12 * tg, 3.0, "first wave 12 tau_g = 3 V")
close([(1 + GL) * w for w in (3, -0.75)], [1.5, -0.375], "load jumps (1+G_L) w: +1.5, -0.375 -> 1.5, 1.125")

print("=== E. special terminations (section 6)")
Z0 = 50.0
close(coefs(Z0, 10, Z0)[2], 0.0, "matched load: Gamma_L = 0")
close(coefs(Z0, 10, np.inf)[2], 1.0, "open load: Gamma_L = +1")
close(coefs(Z0, 10, 0.0)[2], -1.0, "short load: Gamma_L = -1")
close(coefs(Z0, Z0, 100)[:2], (0.5, 0.0), "matched generator: tau_g = 1/2, Gamma_g = 0")
close(coefs(Z0, 0.0, 100)[:2], (1.0, -1.0), "ideal source: tau_g = 1, Gamma_g = -1")
l, v = 100.0, 2e8; T = l / v
for RL, name, VLexp, ILexp in ((np.inf, "open", 2 * 0.5, 0.0), (0.0, "short", 0.0, 2 * 0.5 / Z0)):
    t, th, Vp, Ip, V0h, VNh, _ = fdtd(Z0, Z0, RL, l, v, smooth_step(1.0, T / 100), 3 * T, N=1000, probes=(l,))
    close(plateau(t, VNh, T, 3 * T), VLexp, f"{name} load, matched generator, 1 V step: V(l) = (1+Gamma_L)/2 = {VLexp}", rtol=2e-3, atol=2e-3)
    IL_fd = plateau(th, Ip[l], T, 3 * T)                  # current on the last half cell, next to the load
    close(IL_fd, ILexp, f"{name} load: I near the load = (1-Gamma_L)/(2 Z0) = {ILexp*1e3:.0f} mA", rtol=2e-3, atol=2e-5)
    close(plateau(t, V0h, 2 * T, 3 * T), 0.5 * (1 + coefs(Z0, Z0, RL)[2]), f"{name} load: V(0) settles after one echo at 2T (Gamma_g = 0)", rtol=2e-3, atol=2e-3)
t, th, Vp, Ip, V0h, VNh, _ = fdtd(Z0, Z0, Z0, l, v, smooth_step(1.0, T / 100), 3 * T, N=1000)
close(plateau(t, V0h, 0.2 * T, 3 * T), 0.5, "matched both ends: V(0) = 1/2 forever, no echo", rtol=1e-3)
t, th, Vp, Ip, V0h, VNh, _ = fdtd(Z0, 0.0, 100.0, l, v, smooth_step(1.0, T / 100), 5 * T, N=1000)
close([plateau(t, V0h, a * T, (a + 1) * T) for a in range(4)], [1, 1, 1, 1], "ideal source: V(0,t) = f_i(t) at all times")
# lossless both ends: |Gamma_L Gamma_g| = 1, no decay
close(abs(coefs(Z0, 0.0, np.inf)[1] * coefs(Z0, 0.0, np.inf)[2]), 1.0, "Rg = 0 with open load: |Gamma_L Gamma_g| = 1, echoes never decay")

print("=== F. arrival-time formulas (section 4 recipe)")
l, v = 120.0, 150.0                       # m, m/us
T = l / v
zp = 30.0
ev = bounce_events(75, 25, 37.5, zp, T, l, 5.0)
close([e[0] for e in ev], [0.2, 1.4, 1.8, 3.0, 3.4, 4.6], "z_p/v + 2nT and (2l - z_p)/v + 2nT at z_p = 30 m, l = 120 m, v = 150 m/us")

print("=== G. worked problem")
c = 300.0                                  # m/us
l, zp, Z0 = 120.0, 30.0, 75.0
v = zp / 0.2
close(v, 150.0, "(a) v = 30 m / 0.2 us = 150 m/us")
close((2 * l - zp) / v, 1.4, "(a) check: (240 - 30)/150 = 1.4 us")
close((c / v) ** 2, 4.0, "(a) eps_r = (c/v)^2 = 4")
GL = -1 / 3
RL = Z0 * (1 + GL) / (1 - GL)
close(RL, 37.5, "(c) R_L = 75 (2/3)/(4/3) = 37.5 ohm")
Rg = Z0
tg, Gg, GL2 = coefs(Z0, Rg, RL)
close([tg, Gg, GL2], [0.5, 0.0, -1 / 3], "(b) Rg = Z0: tau_g = 1/2, Gamma_g = 0; Gamma_L = -1/3")
A = 24 * tg
close(A, 12.0, "(d) A = 24 tau_g = 12")
# FDTD with a narrow pulse of area 24 (t in us): only two pulses at z = 30 m
T = l / v
sig = T / 150
t, th, Vp, Ip, V0h, VNh, _ = fdtd(Z0, Rg, RL, l, v, gauss(5 * sig, sig, 24.0), 4.0, N=2400, probes=(zp,))
aV = pulse_areas(t, Vp[zp], np.array([0.2, 1.4, 1.8, 3.0]) + 5 * sig, 0.08)
close(aV, [12, -4, 0, 0], "FDTD: V(30 m) = 12 delta(t-0.2) - 4 delta(t-1.4), nothing at 1.8 or 3.0 us", rtol=3e-3, atol=2e-2)
aI = pulse_areas(th, Ip[zp], np.array([0.2, 1.4]) + 5 * sig, 0.08)
close(aI, [12 / 75, 4 / 75], "(e) FDTD: I(30 m) = 0.16 delta(t-0.2) + 0.0533 delta(t-1.4) A", rtol=3e-3, atol=1e-4)
close([12 / 75, 4 / 75], [0.16, 0.05333333], "(e) 12/75 = 0.16 A, 4/75 = 53.3 mA", rtol=1e-6)
# (f) Rg = 25
Rg = 25.0
tg, Gg, GL2 = coefs(Z0, Rg, RL)
close([tg, Gg, GL2 * Gg], [0.75, -0.5, 1 / 6], "(f) tau_g = 3/4, Gamma_g = -1/2, Gamma_L Gamma_g = 1/6")
ev = bounce_events(Z0, Rg, RL, zp, T, l, 3.5, 24.0)
close([e[0] for e in ev], [0.2, 1.4, 1.8, 3.0, 3.4], "(f) impulse times 0.2, 1.4, 1.8, 3.0, 3.4 us")
close([e[1] for e in ev], [18, -6, 3, -1, 0.5], "(f) weights 18, -6, 3, -1, 0.5")
t, th, Vp, Ip, V0h, VNh, _ = fdtd(Z0, Rg, RL, l, v, gauss(5 * sig, sig, 24.0), 3.8, N=2400, probes=(zp,))
aV = pulse_areas(t, Vp[zp], np.array([0.2, 1.4, 1.8, 3.0, 3.4]) + 5 * sig, 0.08)
close(aV, [18, -6, 3, -1, 0.5], "(f) FDTD areas at z = 30 m", rtol=3e-3, atol=2e-2)
# (g) step 24 u(t)
tt = np.array([1.0, 1.6, 2.4, 3.2, 4.0])
Vb, Ib = bounce_step(Z0, Rg, RL, zp, T, l, tt, 24.0)
close(Vb, [18, 12, 15, 14, 14.5], "(g) V(30 m, t) staircase: 18, 12, 15, 14, 14.5 V")
t, th, Vp, Ip, V0h, VNh, _ = fdtd(Z0, Rg, RL, l, v, smooth_step(24.0, T / 100), 4.5, N=2400, probes=(zp,))
for (a, b), val in zip(((0.2, 1.4), (1.4, 1.8), (1.8, 3.0), (3.0, 3.4), (3.4, 4.5)), (18, 12, 15, 14, 14.5)):
    close(plateau(t, Vp[zp], a, b), val, f"(g) FDTD V(30 m) on ({a}, {b}) us = {val} V", rtol=2e-3)
close(24 * RL / (Rg + RL), 14.4, "(g) V_L(inf) = 24 (37.5/62.5) = 14.4 V")
close(24 / (Rg + RL), 0.384, "(g) I_L(inf) = 24/62.5 = 0.384 A")
Vlong, _ = bounce_step(Z0, Rg, RL, zp, T, l, np.array([4.8, 5.2, 40.0]), 24.0)
close(Vlong, [14.5 - 1 / 6, 14.5 - 1 / 6 + 1 / 12, 14.4], "(g) next steps 14.333, 14.417, ... -> 14.4 (closing in from both sides)")
close(0.2 + 2 * T, 1.8, "(b) generator re-reflection would pass 30 m at 0.2 + 2T = 1.8 us")
close(T, 0.8, "(a) T = 120/150 = 0.8 us")
close(24 * tg * (1 + GL2) / (1 - GL2 * Gg), 14.4, "(g) series: 24 (3/4)(2/3)/(5/6) = 14.4 V")
t, th, Vp, Ip, V0h, VNh, _ = fdtd(Z0, Rg, RL, l, v, smooth_step(24.0, T / 5), 30.0, N=300, probes=(zp,))
close(last2(VNh), 14.4, "(g) FDTD t = 30 us: V(l) = 14.4 V", rtol=1e-4)
close(last2(VNh) / RL, 0.384, "(g) FDTD t = 30 us: I_L = 0.384 A", rtol=1e-4)

print("=== H. concept page")
tg, Gg, GL = coefs(60, 180, 20)
close(12 * tg * (1 + GL) / (1 - GL * Gg), 1.2, "concept example: 1.2 V")
close(coefs(75, 25, 37.5)[1:], (-0.5, -1 / 3), "concept example from the worked problem: Gamma_g = -1/2, Gamma_L = -1/3")

print("=== I. figure numbers (figs_l28.py)")
import sys
sys.path.insert(0, "/home/claude/work")
import importlib
import io, contextlib
with contextlib.redirect_stdout(io.StringIO()):
    F = importlib.import_module("figs_l28")
close([F.Z0, F.RG, F.RL, F.V0], [60, 180, 20, 12], "figure circuit = page example")
ws = F.example_weights()
close(ws, [3, -1.5, -0.75, 0.375, 0.1875, -0.09375], "bounce-step labels")
tg, Gg, GL = coefs(60, 180, 20)
tt = np.linspace(0, 8, 801)[1:] - 0.0037          # off the step instants
Vf = F.step_curves(tt)
Vb_l, _ = bounce_step(60, 180, 20, 1.0, 1.0, 1.0, tt, 12)
Vb_h, _ = bounce_step(60, 180, 20, 0.5, 1.0, 1.0, tt, 12)
close(Vf[0], Vb_h, "figure V(l/2,t) curve = bounce running sum")
close(Vf[1], Vb_l, "figure V(l,t) curve = bounce running sum")

print(f"\nALL {ok_count} CHECKS PASSED")
