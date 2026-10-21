#!/usr/bin/env python3
"""Checks for practice/29-bounce-diagram-examples.md (Lecture 29, bounce-diagram examples).

Units: times in us (29.6 in ns), lengths in m, V, ohm, A; v in m/us (m/ns in 29.6).
Three independent routes for every number:
  bk()   -- the pages' bookkeeping: weighted, delayed copies of f_i (tau_g, Gamma_g, Gamma_L).
  MoC    -- method-of-characteristics time-stepper of the telegrapher's equations: invariants
            V +- Z0 I move one cell per step; ends closed by KVL / Ohm's law only (no Gammas).
            Exact on its grid.
  FDTD   -- Yee leapfrog of -dV/dz = L dI/dt, -dI/dz = C dV/dt with lumped half-cell ends
            (Courant 0.5; second order, small ringing behind sharp edges).
"""
import numpy as np

INF = np.inf
ALL = []


def hdr(s):
    print("\n" + "=" * 100 + "\n" + s + "\n" + "=" * 100)


def close(label, a, b, rtol=1e-6, atol=1e-9):
    a, b = np.atleast_1d(np.asarray(a, float)), np.atleast_1d(np.asarray(b, float))
    ok = bool(np.allclose(a, b, rtol=rtol, atol=atol))
    ALL.append(ok)
    print(f"  [{'OK ' if ok else 'BAD'}] {label}: {np.round(a, 6).tolist()} vs {np.round(b, 6).tolist()}")
    return ok


def check(label, cond):
    ALL.append(bool(cond))
    print(f"  [{'OK ' if cond else 'BAD'}] {label}")


def coeffs(Z0, Rg, RL):
    tg = Z0 / (Rg + Z0)
    Gg = (Rg - Z0) / (Rg + Z0)
    GL = 1.0 if RL == INF else (RL - Z0) / (RL + Z0)
    return tg, Gg, GL


def bk(Z0, Rg, RL, v, l, fi, z, t, nmax=80):
    """Bookkeeping V, I (vectorised in z or t)."""
    tg, Gg, GL = coeffs(Z0, Rg, RL)
    T = l / v
    z, t = np.asarray(z, float), np.asarray(t, float)
    V = np.zeros(np.broadcast(z, t).shape)
    I = np.zeros_like(V)
    for n in range(nmax):
        w = tg * (GL * Gg) ** n
        if abs(w) < 1e-16:
            break
        a = w * fi(t - z / v - 2 * n * T)
        b = w * GL * fi(t + z / v - 2 * (n + 1) * T)
        V = V + a + b
        I = I + (a - b) / Z0
    return V, I


def moc(Z0, Rg, RL, v, l, fi, tmax, N, probes=(), snaps=()):
    """Characteristics stepper. Returns t, {z: (V, I)}, {t: (z, V, I)}."""
    dz = l / N
    dt = dz / v
    nst = int(round(tmax / dt))
    A = np.zeros(N + 1)  # V + Z0 I, moves +z
    B = np.zeros(N + 1)  # V - Z0 I, moves -z
    pk = {p: int(round(p / dz)) for p in probes}
    for p, k in pk.items():
        assert abs(k * dz - p) < 1e-9 * max(1, l), (p, dz)
    sn = {}
    for ts in snaps:
        n = int(round(ts / dt))
        assert abs(n * dt - ts) < 1e-9, (ts, dt)
        sn[n] = ts
    rec = {p: (np.zeros(nst + 1), np.zeros(nst + 1)) for p in probes}
    shots = {}
    zs = np.arange(N + 1) * dz
    for n in range(nst + 1):
        t = n * dt
        if n > 0:
            A[1:] = A[:-1].copy()
            B[:-1] = B[1:].copy()
        # z = 0: arriving B; V = fi - Rg I and V - Z0 I = B
        I0 = (fi(t) - B[0]) / (Rg + Z0)
        V0 = B[0] + Z0 * I0
        A[0] = V0 + Z0 * I0
        # z = l: arriving A; V = RL I and V + Z0 I = A
        if RL == INF:
            IN, VN = 0.0, A[N]
        elif RL == 0:
            VN, IN = 0.0, A[N] / Z0
        else:
            IN = A[N] / (RL + Z0)
            VN = RL * IN
        B[N] = VN - Z0 * IN
        V = 0.5 * (A + B)
        I = 0.5 * (A - B) / Z0
        for p, k in pk.items():
            rec[p][0][n] = V[k]
            rec[p][1][n] = I[k]
        if n in sn:
            shots[sn[n]] = (zs.copy(), V.copy(), I.copy())
    return np.arange(nst + 1) * dt, rec, shots


def fdtd(Z0, Rg, RL, v, l, fi, tmax, N, probes=(), S=0.5):
    """Yee leapfrog; returns t, {z: (V, I)} with I averaged to V nodes and integer steps."""
    dz = l / N
    dt = S * dz / v
    Lp, Cp = Z0 / v, 1.0 / (Z0 * v)
    cv, ci = dt / (Cp * dz), dt / (Lp * dz)
    a = Cp * dz / (2 * dt)
    gL = 0.0 if RL == INF else (None if RL == 0 else 1.0 / RL)
    V = np.zeros(N + 1)
    I = np.zeros(N)
    nst = int(round(tmax / dt))
    pk = {p: int(round(p / dz)) for p in probes}
    rec = {p: (np.zeros(nst), np.zeros(nst)) for p in probes}
    for n in range(nst):
        Iold = I.copy()
        I = I - ci * (V[1:] - V[:-1])
        Im = 0.5 * (Iold + I)
        for p, k in pk.items():
            rec[p][0][n] = V[k]
            if k == 0:
                rec[p][1][n] = Im[0]
            elif k == N:
                rec[p][1][n] = Im[-1]
            else:
                rec[p][1][n] = 0.5 * (Im[k - 1] + Im[k])
        Vn = V.copy()
        V[1:N] = Vn[1:N] - cv * (I[1:] - I[:-1])
        th = (n + 0.5) * dt
        if Rg == 0:
            V[0] = fi((n + 1) * dt)
        else:
            gR = 1.0 / Rg
            V[0] = (Vn[0] * (a - gR / 2) + gR * fi(th) - I[0]) / (a + gR / 2)
        if gL is None:
            V[N] = 0.0
        else:
            V[N] = (Vn[N] * (a - gL / 2) + I[N - 1]) / (a + gL / 2)
    return np.arange(nst) * dt, rec


def at(tarr, rec, z, t):
    i = int(round(t / (tarr[1] - tarr[0])))
    return rec[z][0][i], rec[z][1][i]


def plateau(tarr, rec, z, a, b):
    """mean of V over the middle half of (a, b): averages out FDTD ringing behind sharp edges."""
    m = (tarr > a + (b - a) / 4) & (tarr < b - (b - a) / 4)
    return rec[z][0][m].mean()


def smooth(fun, x, eps=1e-6, jump=1e-3):
    """mask of points where fun has no jump within +-eps."""
    return np.abs(fun(x + eps) - fun(x - eps)) < jump


def cmp_record(label, tarr, Vs, Is, fV, fI, tol=1e-8, tmin=None, tmax=None, skip=None):
    m = smooth(fV, tarr) & smooth(fI, tarr)
    if tmin is not None:
        m &= tarr > tmin
    if tmax is not None:
        m &= tarr < tmax
    if skip is not None:
        m &= skip(tarr)
    dv = np.max(np.abs(Vs[m] - fV(tarr[m])))
    di = np.max(np.abs(Is[m] - fI(tarr[m])))
    ok = dv < tol and di < tol / 10
    ALL.append(bool(ok))
    print(f"  [{'OK ' if ok else 'BAD'}] {label}: max|dV| = {dv:.2e}, max|dI| = {di:.2e} over {m.sum()} samples")


def cmp_snap(label, zs, Vs, Is, fV, fI, tol=1e-8):
    m = smooth(fV, zs) & smooth(fI, zs)
    dv = np.max(np.abs(Vs[m] - fV(zs[m])))
    di = np.max(np.abs(Is[m] - fI(zs[m])))
    ok = dv < tol and di < tol / 10
    ALL.append(bool(ok))
    print(f"  [{'OK ' if ok else 'BAD'}] {label}: max|dV| = {dv:.2e}, max|dI| = {di:.2e} over {m.sum()} nodes")


def piece(x, edges, funcs):
    """piecewise function: funcs[i] on [edges[i], edges[i+1]), 0 elsewhere."""
    x = np.asarray(x, float)
    out = np.zeros_like(x)
    for i, f in enumerate(funcs):
        m = (x >= edges[i]) & (x < edges[i + 1])
        out = np.where(m, f(x) if callable(f) else f, out)
    return out


def rect(a, b, A=1.0):
    return lambda t: A * ((np.asarray(t) >= a) & (np.asarray(t) < b))


# ============================================================================
hdr("29.1 Which way round: Z0 = Rg = 50, RL = 100, l = 1000 m, v = 200 m/us; f_i = 2 V (0,1), 6 V (1,2); t = 3 us")
Z0, Rg, RL, v, l = 50.0, 50.0, 100.0, 200.0, 1000.0
fi = lambda t: rect(0, 1, 2)(t) + rect(1, 2, 6)(t)
tg, Gg, GL = coeffs(Z0, Rg, RL)
print(f"  T = l/v = {l / v} us (front reaches the load after the snapshot)")
print(f"  tau_g = {tg}; front at v*3 = {v * 3} m, tail (sent at 2 us) at v*(3-2) = {v * 1} m; the 2 V part (sent first) -> {tg * 2} V on 400-600 m")
fV = lambda z: piece(z, [200, 400, 600], [3.0, 1.0])
fI = lambda z: fV(z) / 50
zs = np.array([250, 350, 450, 550, 650, 150])
Vb, Ib = bk(Z0, Rg, RL, v, l, fi, zs, 3.0)
close("bk V at z = 250,350,450,550,650,150", Vb, [3, 3, 1, 1, 0, 0])
close("bk I (mA)", Ib * 1e3, [60, 60, 20, 20, 0, 0])
t_, rec, sh = moc(Z0, Rg, RL, v, l, fi, 3.0, 1000, snaps=(3.0,))
z_, V_, I_ = sh[3.0]
cmp_snap("MoC snapshot t = 3 vs answer (a)", z_, V_, I_, fV, fI)
print("  distractors: (b) reversed = 1 V on 200-400, 3 V on 400-600; (c) no tau_g = 6 V / 2 V;"
      " (d) tail placed at vt = 600: 3 V on 400-600, 1 V on 600-800")

# ============================================================================
hdr("29.2 True or false")
# (a) a switched-on sine never settles: Z0 50, Rg 25, RL 100, l 300, v 300, 5 sin(2 pi t)
w = 2 * np.pi
t_, rec, _ = moc(50, 25, 100, 300, 300, lambda t: 5 * np.sin(w * t) * (t >= 0), 60.0, 300, probes=(300.0,))
VL = rec[300.0][0]
late = (t_ > 50) & (t_ < 60)
print(f"  (a) V(l,t) for 50 < t < 60 us: max {VL[late].max():.4f} V, min {VL[late].min():.4f} V (keeps oscillating)")
check("(a) false: no constant limit", VL[late].max() - VL[late].min() > 1.0)
# (b) Rg = Z0: a burst of duration D leaves the line at rest after 2T + D
Z0, l, v, D = 50.0, 600.0, 200.0, 2.0
T = l / v
fi = lambda t: 4 * np.sin(w * t) * ((t >= 0) & (t < D))
t_, rec, sh = moc(Z0, 50, 150, v, l, fi, 12.0, 600, snaps=(8.0 + 0.5, 11.0))
mx = max(np.max(np.abs(sh[k][1])) for k in sh)
print(f"  (b) 2T + D = {2 * T + D} us; max |V| on the whole line at t = 8.5 and 11 us: {mx:.2e}")
check("(b) true: line at rest after 2T + D", mx < 1e-12)
t_, rec, sh = moc(Z0, 50, 150, v, l, fi, 7.9, 600, snaps=(7.5,))
print(f"  (b) but at t = 7.5 us (< 2T + D) max |V| = {np.max(np.abs(sh[7.5][1])):.4f} V")
# (c) DC limit independent of Z0 and length: 10 V step, Rg 25, RL 100
for Z0_, l_ in [(50, 300), (50, 900), (75, 300)]:
    t_, rec, _ = moc(Z0_, 25, 100, 200, l_, lambda t: 10.0 * (t >= 0), 400.0, 150, probes=(l_ / 2,))
    print(f"  (c) Z0 = {Z0_}, l = {l_} m: V(l/2, 400 us) = {rec[l_ / 2][0][-1]:.6f} V (divider 10*100/125 = {10 * 100 / 125})")
    close(f"(c) DC independent of Z0, l ({Z0_},{l_})", rec[l_ / 2][0][-1], 8.0, rtol=1e-6)
# (d) order on a snapshot: see 29.4 (sent-first 4 V part is at 300-600 m, nearer the generator)
print("  (d) true: see 29.4 -- the first-sent 4 V part of the echo lies on 300-600 m, the later 2 V part on 600-900 m")

# ============================================================================
hdr("29.3 Sine: Z0 = Rg = 75, RL = 225, l = 450, v = 300, f = 2 MHz, f_i = 8 sin(wt) u(t)")
Z0, Rg, RL, v, l = 75.0, 75.0, 225.0, 300.0, 450.0
w = 4 * np.pi  # rad/us
fi = lambda t: 8 * np.sin(w * t) * (np.asarray(t) >= 0)
tg, Gg, GL = coeffs(Z0, Rg, RL)
T = l / v
print(f"  tau_g = {tg}, Gg = {Gg}, GL = {GL}, T = {T} us, lambda = v/f = {v / 2} m, front at t = 1: {v * 1} m = {v / (v / 2)} wavelengths")
close("coeffs", [tg, Gg, GL, T, v / 2.0], [0.5, 0, 0.5, 1.5, 150])
fV = lambda z: piece(z, [0, 300], [lambda z: -4 * np.sin(np.pi * z / 75)])
fI = lambda z: fV(z) / 75
zs = np.array([18.75, 56.25, 100, 299])
print("  bk V(z,1) at", zs.tolist(), "=", np.round(bk(Z0, Rg, RL, v, l, fi, zs, 1.0)[0], 6).tolist(),
      "; formula -4 sin(pi z/75):", np.round(-4 * np.sin(np.pi * zs / 75), 6).tolist())
close("bk = formula (a)", bk(Z0, Rg, RL, v, l, fi, zs, 1.0)[0], -4 * np.sin(np.pi * zs / 75))
print(f"  amplitudes: V 4 V, I 4/75 = {4 / 75 * 1e3:.3f} mA")
t_, rec, sh = moc(Z0, Rg, RL, v, l, fi, 12.0, 900, probes=(l,), snaps=(1.0,))
cmp_snap("MoC snapshot t = 1 vs -4 sin(pi z/75)", *sh[1.0], fV, fI)
print(f"  (1 + GL) tau_g 8 = {(1 + GL) * tg * 8} V; w*T = {w * T / np.pi} pi -> sin w(t-1.5) = sin wt")
fVL = lambda t: np.where(t > 1.5, 6 * np.sin(w * t), 0.0)
fIL = lambda t: fVL(t) / 225
cmp_record("MoC V(l,t), I(l,t) vs 6 sin wt, 26.7 sin wt mA (0 < t < 12)", t_, *rec[l], fVL, fIL)
print(f"  I amplitude: 6/225 = {6 / 225 * 1e3:.4f} mA = (1 - GL) tau_g 8/Z0 = {(1 - GL) * tg * 8 / Z0 * 1e3:.4f} mA")

# ============================================================================
hdr("29.4 Find the error: Z0 = Rg = 60, RL = 20, l = 900, v = 300; f_i = 4 V (0,1), 2 V (1,2); t = 5 us")
Z0, Rg, RL, v, l = 60.0, 60.0, 20.0, 300.0, 900.0
fi = lambda t: rect(0, 1, 4)(t) + rect(1, 2, 2)(t)
tg, Gg, GL = coeffs(Z0, Rg, RL)
print(f"  tau_g = {tg}, GL = {GL}, echo weight tau_g GL = {tg * GL}; echo levels {tg * GL * 4} V, {tg * GL * 2} V")
zs = np.array([150, 450, 750])
Vb, Ib = bk(Z0, Rg, RL, v, l, fi, zs, 5.0)
close("bk V at 150, 450, 750", Vb, [0, -1, -0.5])
close("bk I (mA) at 150, 450, 750", Ib * 1e3, [0, 1000 / 60, 500 / 60])
print(f"  correct I = -V/Z0: {1 / 60 * 1e3:.3f} mA, {0.5 / 60 * 1e3:.3f} mA; student's: {-1 / 60 * 1e3:.3f}, {-0.5 / 60 * 1e3:.3f} mA")
print(f"  forward current was 2/60 = {2 / 60 * 1e3:.3f} mA; times -GL = {-GL} -> {2 / 60 * (-GL) * 1e3:.3f} mA")
t_, rec, sh = moc(Z0, Rg, RL, v, l, fi, 5.0, 900, snaps=(5.0,))
fV = lambda z: piece(z, [300, 600, 900], [-1.0, -0.5])
cmp_snap("MoC snapshot t = 5", *sh[5.0], fV, lambda z: -fV(z) / 60)

# ============================================================================
hdr("29.5 Inputs that settle: Z0 = 50, Rg = 25, RL = 100, l = 300 m, v = 200 m/us")
Z0, Rg, RL, v, l = 50.0, 25.0, 100.0, 200.0, 300.0
tg, Gg, GL = coeffs(Z0, Rg, RL)
print(f"  Gg = {Gg:.6f}, GL = {GL:.6f}, GL*Gg = {GL * Gg:.6f}")
cases = {
    "(a) 12u(t-2)": (lambda t: 12.0 * (t >= 2), 12.0),
    "(b) 9u(t)-6u(t-1)": (lambda t: 9.0 * (t >= 0) - 6.0 * (t >= 1), 3.0),
    "(c) 6 sin(2 pi t)u(t)": (lambda t: 6 * np.sin(2 * np.pi * t) * (t >= 0), None),
    "(d) 10[u(t)-u(t-3)]": (lambda t: 10.0 * ((t >= 0) & (t < 3)), 0.0),
}
for k, (f, F) in cases.items():
    t_, rec, _ = moc(Z0, Rg, RL, v, l, f, 80.0, 150, probes=(0.0, 150.0, 300.0))
    m = (t_ > 70)
    Vs = [rec[p][0][m] for p in (0.0, 150.0, 300.0)]
    Is = [rec[p][1][m] for p in (0.0, 150.0, 300.0)]
    if F is None:
        print(f"  {k}: V(l/2) for 70-80 us ranges {Vs[1].min():.4f} .. {Vs[1].max():.4f} V -> no DC limit")
        check(f"{k} keeps oscillating", Vs[1].max() - Vs[1].min() > 1)
    else:
        Vd, Id = F * RL / (Rg + RL), F / (Rg + RL)
        print(f"  {k}: settles to F = {F} V -> V = {Vd:.4f} V, I = {Id * 1e3:.4f} mA; MoC at 80 us (z = 0, l/2, l):"
              f" V = {[round(x[-1], 6) for x in Vs]}, I = {[round(x[-1] * 1e3, 6) for x in Is]} mA")
        close(f"{k} MoC DC", [x[-1] for x in Vs] + [x[-1] for x in Is], [Vd] * 3 + [Id] * 3, rtol=1e-6, atol=1e-9)
close("DC answers", [12 * 100 / 125, 12 / 125 * 1e3, 3 * 100 / 125, 3 / 125 * 1e3], [9.6, 96, 2.4, 24])

# ============================================================================
hdr("29.6 Records at both ends (ns): Z0 = 50, Rg = 75, RL = 150, l = 0.1 m, v = 0.2 m/ns; 10 V pulse 0-1.5 ns")
Z0, Rg, RL, v, l = 50.0, 75.0, 150.0, 0.2, 0.1
fi = rect(0, 1.5, 10)
tg, Gg, GL = coeffs(Z0, Rg, RL)
T = l / v
print(f"  tau_g = {tg}, Gg = {Gg}, GL = {GL}, T = {T} ns; forward weights x10: {[10 * tg * (GL * Gg) ** n for n in range(3)]},"
      f" backward: {[10 * tg * GL * (GL * Gg) ** n for n in range(3)]}")
close("coeffs", [tg, Gg, GL, T], [0.4, 0.2, 0.5, 0.5])
print(f"  at z = 0 the echoes arrive as (1+Gg) x backward: {[(1 + Gg) * 10 * tg * GL * (GL * Gg) ** n for n in range(3)]} V;"
      f" at the load (1+GL) x forward: {[(1 + GL) * 10 * tg * (GL * Gg) ** n for n in range(3)]} V")
print(f"  Z0 I at z = 0: echo b contributes -(1 - Gg) b = {[-(1 - Gg) * 10 * tg * GL * (GL * Gg) ** n for n in range(2)]} V")
mids0 = [0.5, 1.25, 1.75, 2.25, 2.75]
V0 = [bk(Z0, Rg, RL, v, l, fi, 0.0, t)[0] for t in mids0]
I0 = [bk(Z0, Rg, RL, v, l, fi, 0.0, t)[1] for t in mids0]
print("  V(0,t) on (0,1),(1,1.5),(1.5,2),(2,2.5),(2.5,3):", np.round(V0, 6).tolist(), " I(0,t) mA:", np.round(np.array(I0) * 1e3, 6).tolist())
close("V(0,t) levels", V0, [4, 6.4, 2.4, 2.64, 0.24])
close("I(0,t) levels (mA)", np.array(I0) * 1e3, [80, 48, -32, -35.2, -3.2])
midsL = [0.25, 1.0, 1.75, 2.25, 2.75]
VLv = [bk(Z0, Rg, RL, v, l, fi, l, t)[0] for t in midsL]
ILv = [bk(Z0, Rg, RL, v, l, fi, l, t)[1] for t in midsL]
print("  V(l,t) on (0,.5),(.5,1.5),(1.5,2),(2,2.5),(2.5,3):", np.round(VLv, 6).tolist(), " I(l,t) mA:", np.round(np.array(ILv) * 1e3, 6).tolist())
close("V(l,t) levels", VLv, [0, 6, 6.6, 0.6, 0.66])
close("I(l,t) levels (mA)", np.array(ILv) * 1e3, [0, 40, 44, 4, 4.4])
print(f"  KVL at z = 0: (1,1.5): 10 - 75*0.048 = {10 - 75 * 0.048}; (1.5,2): -75*(-0.032) = {75 * 0.032}; (2,2.5): {75 * 0.0352}")
t_, rec, _ = moc(Z0, Rg, RL, v, l, fi, 3.0, 400, probes=(0.0, l))
fV0 = lambda t: piece(t, [0, 1, 1.5, 2, 2.5, 3], [4, 6.4, 2.4, 2.64, 0.24])
fI0 = lambda t: piece(t, [0, 1, 1.5, 2, 2.5, 3], [0.08, 0.048, -0.032, -0.0352, -0.0032])
fVL = lambda t: piece(t, [0.5, 1.5, 2, 2.5, 3], [6, 6.6, 0.6, 0.66])
cmp_record("MoC V(0,t), I(0,t), 0-3 ns", t_, *rec[0.0], fV0, fI0, tmax=2.99)
cmp_record("MoC V(l,t), I(l,t), 0-3 ns", t_, *rec[l], fVL, lambda t: fVL(t) / 150, tmax=2.99)
tf, rf = fdtd(Z0, Rg, RL, v, l, fi, 3.0, 2000, probes=(0.0, l))
p0 = [plateau(tf, rf, 0.0, a, b) for a, b in [(0, 1), (1, 1.5), (1.5, 2), (2, 2.5), (2.5, 3)]]
pL = [plateau(tf, rf, l, a, b) for a, b in [(0, .5), (.5, 1.5), (1.5, 2), (2, 2.5), (2.5, 3)]]
print("    FDTD plateau means V(0):", np.round(p0, 4).tolist(), " V(l):", np.round(pL, 4).tolist())
close("FDTD V(0) plateaus", p0, [4, 6.4, 2.4, 2.64, 0.24], rtol=0, atol=0.02)
close("FDTD V(l) plateaus", pL, [0, 6, 6.6, 0.6, 0.66], rtol=0, atol=0.02)

# ============================================================================
hdr("29.7 Triangle into a short: Z0 = Rg = 50, RL = 0, l = 400, v = 200; f_i triangle 0 -> 12 V at 0.5 -> 0 at 1 us")
Z0, Rg, RL, v, l = 50.0, 50.0, 0.0, 200.0, 400.0
fi = lambda t: np.where((t > 0) & (t < 0.5), 24 * t, np.where((t >= 0.5) & (t < 1), 24 * (1 - t), 0.0))
tg, Gg, GL = coeffs(Z0, Rg, RL)
print(f"  tau_g = {tg}, GL = {GL}, T = {l / v}, pulse length v*1 us = {v} m, forward peak {tg * 12} V, {tg * 12 / Z0 * 1e3} mA")
snaps = {
    2.0: (lambda z: piece(z, [200, 300, 400], [lambda z: 0.06 * (z - 200), lambda z: 0.06 * (400 - z)]),
          lambda z: piece(z, [200, 300, 400], [lambda z: 0.06 * (z - 200) / 50, lambda z: 0.06 * (400 - z) / 50])),
    2.5: (lambda z: 0 * z, lambda z: piece(z, [300, 400], [lambda z: 0.0024 * (z - 300)])),
    3.0: (lambda z: piece(z, [200, 300, 400], [lambda z: -0.06 * (z - 200), lambda z: -0.06 * (400 - z)]),
          lambda z: piece(z, [200, 300, 400], [lambda z: 0.06 * (z - 200) / 50, lambda z: 0.06 * (400 - z) / 50])),
}
zs = np.array([250, 300, 350, 399.9])
for ts in snaps:
    Vb, Ib = bk(Z0, Rg, RL, v, l, fi, zs, ts)
    print(f"  t = {ts}: bk V at {zs.tolist()} = {np.round(Vb, 5).tolist()} V; I = {np.round(Ib * 1e3, 4).tolist()} mA")
    close(f"bk vs answer t = {ts}", np.r_[Vb, Ib], np.r_[snaps[ts][0](zs), snaps[ts][1](zs)])
t_, rec, sh = moc(Z0, Rg, RL, v, l, fi, 3.0, 800, snaps=tuple(snaps))
for ts in snaps:
    cmp_snap(f"MoC snapshot t = {ts}", *sh[ts], *snaps[ts])
Cp, Lp = 1 / (Z0 * v * 1e6), Z0 / (v * 1e6)
for ts in snaps:
    z_, V_, I_ = sh[ts]
    dz = z_[1] - z_[0]
    We = 0.5 * Cp * np.trapezoid(V_ ** 2, z_)
    Wm = 0.5 * Lp * np.trapezoid(I_ ** 2, z_)
    print(f"  t = {ts}: electric {We * 1e6:.5f} uJ, magnetic {Wm * 1e6:.5f} uJ, total {(We + Wm) * 1e6:.5f} uJ")
    close(f"energy t = {ts} (uJ)", (We + Wm) * 1e6, 0.24, rtol=1e-3)
print(f"  int V^2 dz at t = 2: {2 * 0.0036 * 100 ** 3 / 3:.1f} V^2 m; int I^2 dz at t = 2.5: {0.0024 ** 2 * 100 ** 3 / 3:.4f} A^2 m;"
      f" I(400, 2.5) = {bk(Z0, Rg, RL, v, l, fi, 399.999999, 2.5)[1] * 1e3:.4f} mA")
print(f"  C' = {Cp * 1e12:.1f} pF/m, L' = {Lp * 1e6:.3f} uH/m; exact: t=2: C' int V^2 = {Cp * 2400 * 1e6:.4f} uJ;"
      f" t=2.5: L'/2 int I^2 = {0.5 * Lp * 0.0024 ** 2 * 100 ** 3 / 3 * 1e6:.4f} uJ; launched int (f/2)^2/Z0 dt = {2 * 144 * 0.125 / 3 / 50:.4f} uJ")

# ============================================================================
hdr("29.8 One pulse, nothing else: Z0 = 60, l = 300 m; 20 V pulse 0-1 us; probe z = 100 m sees 15 V on 0.5-1.5 us only")
Z0, l = 60.0, 300.0
v = 100 / 0.5
tg = 15 / 20
Rg = Z0 * (1 - tg) / tg
print(f"  v = 100/0.5 = {v} m/us, T = {l / v} us; tau_g = {tg}, Rg = Z0(1/tau_g - 1) = {Rg} ohm; RL = Z0 = {Z0}")
close("v, Rg", [v, Rg], [200, 20])
fi = rect(0, 1, 20)
t_, rec, _ = moc(Z0, Rg, Z0, v, l, fi, 30.0, 600, probes=(100.0,))
Vr = rec[100.0][0]
print(f"  MoC with RL = 60, Rg = 20: V(100,1) = {at(t_, rec, 100.0, 1.0)[0]:.6f} V; max |V(100,t)| for t > 1.6 us: {np.max(np.abs(Vr[t_ > 1.6])):.2e}")
check("only one pulse at z = 100 m", np.max(np.abs(Vr[t_ > 1.6])) < 1e-12 and abs(at(t_, rec, 100.0, 1.0)[0] - 15) < 1e-12)
for RLx in (50.0, 75.0):
    t2, r2, _ = moc(Z0, Rg, RLx, v, l, fi, 30.0, 600, probes=(100.0,))
    print(f"    (RL = {RLx}: an echo of {np.max(np.abs(r2[100.0][0][t2 > 1.6])):.4f} V would appear)")
tg, Gg, GL = coeffs(Z0, Rg, INF)
print(f"  open load: GL = {GL}, Gg = {Gg}; crossings at z/v = 0.5: forward 0.5 + 3n, backward 2.5 + 3n")
mids = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 7.75]
Vb = [bk(Z0, Rg, INF, v, l, fi, 100.0, t)[0] for t in mids]
Ib = [bk(Z0, Rg, INF, v, l, fi, 100.0, t)[1] for t in mids]
print("  record at t =", mids, ": V =", np.round(Vb, 6).tolist(), " I (A) =", np.round(Ib, 6).tolist())
close("open-load record V", Vb, [15, 0, 15, -7.5, 0, -7.5, 3.75, 0])
close("open-load record I", Ib, [0.25, 0, -0.25, -0.125, 0, 0.125, 0.0625, 0])
t_, rec, _ = moc(Z0, Rg, INF, v, l, fi, 8.0, 600, probes=(100.0,))
fV = lambda t: piece(t, [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5], [15, 0, 15, -7.5, 0, -7.5, 3.75])
fI = lambda t: piece(t, [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5], [0.25, 0, -0.25, -0.125, 0, 0.125, 0.0625])
cmp_record("MoC open-load record 0-8 us", t_, *rec[100.0], fV, fI, tmax=7.99)

# ============================================================================
hdr("29.9 One sine cycle: Z0 = 50, Rg = 150, RL = 25, l = 500, v = 200; f_i = 12 sin(2 pi t), 0 < t < 1 us")
Z0, Rg, RL, v, l = 50.0, 150.0, 25.0, 200.0, 500.0
fi = lambda t: 12 * np.sin(2 * np.pi * t) * ((t >= 0) & (t < 1))
tg, Gg, GL = coeffs(Z0, Rg, RL)
T = l / v
wts = [12 * tg, 12 * tg * GL, 12 * tg * GL * Gg, 12 * tg * GL * GL * Gg]
print(f"  tau_g = {tg}, Gg = {Gg}, GL = {GL:.6f}, T = {T} us, pulse length {v * 1} m; amplitudes F0, B0, F1, B1 = {np.round(wts, 6).tolist()}")
close("coeffs", [tg, Gg, GL, T], [0.25, 0.5, -1 / 3, 2.5])
close("amplitudes", wts, [3, -1, -0.5, 1 / 6])
k = np.pi / 100
ans = {
    2.0: (lambda z: piece(z, [200, 400], [lambda z: -3 * np.sin(k * z)]),
          lambda z: piece(z, [200, 400], [lambda z: -3 * np.sin(k * z) / 50])),
    2.75: (lambda z: piece(z, [350, 450, 500], [lambda z: -3 * np.cos(k * z), lambda z: -2 * np.cos(k * z)]),
           lambda z: piece(z, [350, 450, 500], [lambda z: -3 * np.cos(k * z) / 50, lambda z: -4 * np.cos(k * z) / 50])),
    6.0: (lambda z: piece(z, [0, 200], [lambda z: 0.5 * np.sin(k * z)]),
          lambda z: piece(z, [0, 200], [lambda z: 0.5 * np.sin(k * z) / 50])),
}
zs = {2.0: [250, 300, 350], 2.75: [400, 450, 475, 499.999], 6.0: [50, 150]}
for ts in ans:
    Vb, Ib = bk(Z0, Rg, RL, v, l, fi, np.array(zs[ts]), ts)
    print(f"  t = {ts}: bk V at {zs[ts]} = {np.round(Vb, 5).tolist()} V, I = {np.round(Ib * 1e3, 4).tolist()} mA")
    close(f"bk = answer t = {ts}", np.r_[Vb, Ib], np.r_[ans[ts][0](np.array(zs[ts])), ans[ts][1](np.array(zs[ts]))])
t_, rec, sh = moc(Z0, Rg, RL, v, l, fi, 6.0, 1000, snaps=tuple(ans), probes=(l,))
for ts in ans:
    cmp_snap(f"MoC snapshot t = {ts}", *sh[ts], *ans[ts])
VL, IL = at(t_, rec, l, 2.75)
print(f"  load at t = 2.75: V = {VL:.6f} V, I = {IL * 1e3:.4f} mA, V/I = {VL / IL:.4f} ohm")
close("load check t = 2.75", [VL, IL * 1e3, VL / IL], [2, 80, 25])
print(f"  (aside) on 450-500 m at t = 2.75 both copies are prop. to cos kz, so V/I = {ans[2.75][0](475.0) / ans[2.75][1](475.0):.3f} ohm there; on 350-450 V/I = Z0 = {ans[2.75][0](400.0) / ans[2.75][1](400.0):.3f}")
tf, rf = fdtd(Z0, Rg, RL, v, l, fi, 6.5, 2000, probes=(450.0, 500.0, 100.0))
print(f"  FDTD: V(500, 2.75) = {at(tf, rf, 500.0, 2.75)[0]:.4f}, I = {at(tf, rf, 500.0, 2.75)[1] * 1e3:.3f} mA;"
      f" V(100, 6) = {at(tf, rf, 100.0, 6.0)[0]:.4f} (exp 0)  V(450,2) = {at(tf, rf, 450.0, 2.0)[0]:.4f} (exp 0)")
close("FDTD load 2.75", [at(tf, rf, 500.0, 2.75)[0], at(tf, rf, 500.0, 2.75)[1] * 1e3], [2, 80], rtol=0, atol=0.02)

# ============================================================================
hdr("29.10 Ramp into an open line: Z0 = Rg = 50, open, l = 300, v = 200; f_i = 20 t V on 0 < t < 6 us")
Z0, Rg, RL, v, l = 50.0, 50.0, INF, 200.0, 300.0
fi = lambda t: np.where((t > 0) & (t < 6), 20 * t, 0.0)
tg, Gg, GL = coeffs(Z0, Rg, RL)
T = l / v
print(f"  tau_g = {tg}, Gg = {Gg}, GL = {GL}, T = {T}, 2T = {2 * T}")
fV0 = lambda t: piece(t, [0, 3, 6, 9], [lambda t: 10 * t, lambda t: 20 * t - 30, lambda t: 10 * (t - 3)])
fI0 = lambda t: piece(t, [0, 3, 6, 9], [lambda t: 0.2 * t, 0.6, lambda t: -0.2 * (t - 3)])
ts = np.array([1.5, 3, 4.5, 6 - 1e-9, 6 + 1e-9, 7, 9 - 1e-9, 9.5])
Vb, Ib = bk(Z0, Rg, RL, v, l, fi, 0.0, ts)
print("  V(0,t) at", np.round(ts, 3).tolist(), "=", np.round(Vb, 4).tolist(), "; I =", np.round(Ib, 4).tolist())
close("bk = answer V(0,t), I(0,t)", np.r_[Vb, Ib], np.r_[fV0(ts), fI0(ts)], atol=1e-6)
fVL = lambda t: piece(t, [1.5, 7.5], [lambda t: 20 * (t - 1.5)])
print(f"  V(l,t) = 20(t - 1.5) on 1.5 < t < 7.5: peak -> {20 * 6} V; I(l) = 0")
t_, rec, sh = moc(Z0, Rg, RL, v, l, fi, 10.0, 600, probes=(0.0, l), snaps=(4.5, 7.0))
cmp_record("MoC V(0,t), I(0,t)", t_, *rec[0.0], fV0, fI0, tol=1e-7)
cmp_record("MoC V(l,t), I(l,t)", t_, *rec[l], fVL, lambda t: 0 * t, tol=1e-7)
s45 = (lambda z: 60 + 0 * z, lambda z: 0.6 * (1 - z / 300))
s7 = (lambda z: piece(z, [0, 200, 300], [lambda z: 40 + z / 20, 110.0]),
      lambda z: piece(z, [0, 200, 300], [lambda z: -(0.8 + z / 1000), lambda z: 0.6 - z / 500]))
cmp_snap("MoC snapshot t = 4.5 (V = 60, I = 0.6(1 - z/300))", sh[4.5][0][1:-1], sh[4.5][1][1:-1], sh[4.5][2][1:-1], *s45, tol=1e-7)
cmp_snap("MoC snapshot t = 7", sh[7.0][0][1:-1], sh[7.0][1][1:-1], sh[7.0][2][1:-1], *s7, tol=1e-7)
zz = np.array([0, 100, 199.999, 200.001, 250, 300])
print("  t = 7: V at", zz.tolist(), "=", np.round(bk(Z0, Rg, RL, v, l, fi, zz, 7.0)[0], 4).tolist(),
      " I =", np.round(bk(Z0, Rg, RL, v, l, fi, zz, 7.0)[1], 4).tolist())
print(f"  jump at z = 200 m: dV = {50 - 110} V, dI = {-1.0 - 0.2} A, ratio {(50 - 110) / (-1.2)} ohm = Z0 (a forward step of -60 V)")
Ctot = l / (Z0 * v * 1e6)
print(f"  C'l = {Ctot * 1e9:.1f} nF; C'l dV/dt = {Ctot * 20e6:.3f} A (dV(0)/dt = 20 V/us on 3-6 us)")
close("capacitor check", Ctot * 20e6, 0.6)
print(f"  KVL z=0: t = 4.5: f - Rg I = {20 * 4.5 - 50 * 0.6} = V(0) = {20 * 4.5 - 30}; t = 7: -Rg I = {-50 * (-0.8)} = 10(7-3) = {10 * 4}")
tf, rf = fdtd(Z0, Rg, RL, v, l, fi, 10.0, 1500, probes=(0.0, 150.0, 300.0))
for tt in (1.5, 4.5, 7.0, 8.5):
    print(f"    FDTD z=0, t={tt}: V = {at(tf, rf, 0.0, tt)[0]:.4f} (exp {fV0(np.array(tt)):.4f}), I = {at(tf, rf, 0.0, tt)[1]:.4f} (exp {fI0(np.array(tt)):.4f})")
close("FDTD z=0", [at(tf, rf, 0.0, tt)[0] for tt in (1.5, 4.5, 7.0, 8.5)], [fV0(np.array(tt)) for tt in (1.5, 4.5, 7.0, 8.5)], rtol=0, atol=0.1)
close("FDTD I(150, 4.5) = 0.3 A", at(tf, rf, 150.0, 4.5)[1], 0.3, rtol=0, atol=2e-3)

# ============================================================================
hdr("29.11 Soft step at z = 300 m: Z0 = 50, Rg = 25, RL = 100, l = 400, v = 200; f_i = 27 min(t/2, 1)")
Z0, Rg, RL, v, l = 50.0, 25.0, 100.0, 200.0, 400.0
fi = lambda t: 27 * np.clip(t / 2, 0, 1) * (t > 0)
tg, Gg, GL = coeffs(Z0, Rg, RL)
T = l / v
zp = 300.0
times, wv, wi = [], [], []
for n in range(3):
    for tt, w_, s in [(zp / v + 2 * n * T, tg * (GL * Gg) ** n, 1), (2 * T - zp / v + 2 * n * T, tg * GL * (GL * Gg) ** n, -1)]:
        times.append(tt); wv.append(w_); wi.append(s * w_)
o = np.argsort(times)
times, wv, wi = np.array(times)[o], np.array(wv)[o], np.array(wi)[o]
print(f"  tau_g = {tg:.6f}, Gg = {Gg:.6f}, GL = {GL:.6f}, GL Gg = {GL * Gg:.6f}, T = {T}")
print("  crossings t =", times.tolist(), " V weights =", [f"{x:.6f}" for x in wv], " Z0 I weights =", [f"{x:.6f}" for x in wi])
close("times", times, [1.5, 2.5, 5.5, 6.5, 9.5, 10.5])
close("27 x V weights", 27 * wv, [18, 6, -2, -2 / 3, 2 / 9, 2 / 27])
close("27 x Z0I weights", 27 * wi, [18, -6, -2, 2 / 3, 2 / 9, -2 / 27])
bp = np.array([1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5])
Vb, Ib = bk(Z0, Rg, RL, v, l, fi, zp, bp)
print("  V(300,t) at", bp.tolist(), "=", np.round(Vb, 5).tolist())
print("  Z0 I(300,t) =", np.round(Ib * Z0, 5).tolist(), "; I (mA) =", np.round(Ib * 1e3, 4).tolist())
close("V breakpoints", Vb, [0, 9, 21, 24, 24, 23, 65 / 3, 64 / 3, 64 / 3])
close("Z0 I breakpoints", Ib * Z0, [0, 9, 15, 12, 12, 11, 31 / 3, 32 / 3, 32 / 3])
print(f"  slopes on (2.5,3.5): V {9 + 3} V/us, Z0I {9 - 3}; (6.5,7.5): V {-1 - 1 / 3:.4f}, Z0I {-1 + 1 / 3:.4f}")
print(f"  series: 27 tau_g (1+GL)/(1-GL Gg) = 27*{tg:.4f}*{1 + GL:.4f}/{1 - GL * Gg:.4f} = {27 * tg * (1 + GL) / (1 - GL * Gg):.6f} V")
print(f"  DC: V = 27*100/125 = {27 * 100 / 125} V, I = 27/125 = {27 / 125 * 1e3} mA; peak 24 V overshoot {24 - 21.6:.1f} V")
t_, rec, _ = moc(Z0, Rg, RL, v, l, fi, 100.0, 400, probes=(zp,))
fVr = lambda t: bk(Z0, Rg, RL, v, l, fi, zp, t)[0]
fIr = lambda t: bk(Z0, Rg, RL, v, l, fi, zp, t)[1]
cmp_record("MoC record V(300,t), I(300,t), 0-14 us vs bookkeeping", t_, *rec[zp], fVr, fIr, tmax=14, tol=1e-9)
close("MoC breakpoints", [at(t_, rec, zp, x)[0] for x in bp], [0, 9, 21, 24, 24, 23, 65 / 3, 64 / 3, 64 / 3], rtol=1e-9)
close("MoC flats I (mA) at 5, 9", [at(t_, rec, zp, 5.0)[1] * 1e3, at(t_, rec, zp, 9.0)[1] * 1e3], [240, 640 / 3])
close("MoC DC at 100 us", [rec[zp][0][-1], rec[zp][1][-1] * 1e3], [21.6, 216], rtol=1e-8)
tf, rf = fdtd(Z0, Rg, RL, v, l, fi, 15.0, 1600, probes=(zp,))
close("FDTD breakpoints", [at(tf, rf, zp, x)[0] for x in bp], [0, 9, 21, 24, 24, 23, 65 / 3, 64 / 3, 64 / 3], rtol=0, atol=0.02)

# ============================================================================
hdr("29.12 Partial standing wave: Z0 = Rg = 75, RL = 25, l = 500, v = 200, f = 0.5 MHz, f_i = 12 sin(pi t) u(t)")
Z0, Rg, RL, v, l = 75.0, 75.0, 25.0, 200.0, 500.0
w = np.pi
fi = lambda t: 12 * np.sin(w * t) * (t >= 0)
tg, Gg, GL = coeffs(Z0, Rg, RL)
T = l / v
print(f"  tau_g = {tg}, Gg = {Gg}, GL = {GL}, T = {T} us, lambda = {v / 0.5} m, beta = pi/200 rad/m; forward 6 V, echo {6 * GL} V")
close("coeffs", [tg, Gg, GL, T, v / 0.5], [0.5, 0, -0.5, 2.5, 400])
print(f"  load: (1+GL) 6 = {(1 + GL) * 6} V, w T = {w * T / np.pi} pi -> 3 sin(pi t - 2.5 pi) = -3 cos(pi t); I amplitude 3/25 = {3 / 25 * 1e3} mA = (1-GL) 6/75 = {(1 - GL) * 6 / 75 * 1e3} mA")
t_, rec, sh = moc(Z0, Rg, RL, v, l, fi, 20.0, 1000, probes=(0.0, 100.0, 200.0, 300.0, 400.0, l), snaps=(4.0,))
fVL = lambda t: np.where(t > 2.5, -3 * np.cos(w * t), 0.0)
cmp_record("MoC V(l,t), I(l,t) vs -3 cos(pi t), -120 cos(pi t) mA", t_, *rec[l], fVL, lambda t: fVL(t) / 25)
b = np.pi / 200
s4 = (lambda z: piece(z, [0, 200, 500], [lambda z: -6 * np.sin(b * z), lambda z: -3 * np.sin(b * z)]),
      lambda z: piece(z, [0, 200, 500], [lambda z: -6 * np.sin(b * z) / 75, lambda z: -9 * np.sin(b * z) / 75]))
zs = np.array([100, 300, 400, 499.999])
Vb, Ib = bk(Z0, Rg, RL, v, l, fi, zs, 4.0)
print(f"  t = 4: V at {zs.tolist()} = {np.round(Vb, 5).tolist()}, I (mA) = {np.round(Ib * 1e3, 4).tolist()}; load V/I = {Vb[-1] / Ib[-1]:.4f}")
close("bk = answer t = 4", np.r_[Vb, Ib], np.r_[s4[0](zs), s4[1](zs)])
cmp_snap("MoC snapshot t = 4", sh[4.0][0][1:-1], sh[4.0][1][1:-1], sh[4.0][2][1:-1], *s4)
print("  t > 5 us: V = 6 sin(wt - bz) + 3 sin(wt + bz); |V| = sqrt(45 + 36 cos(pi z/100)), Z0|I| = sqrt(45 - 36 cos(pi z/100))")
late = (t_ > 16) & (t_ < 20)
for zp in (0.0, 100.0, 200.0, 300.0, 400.0, l):
    Va = 0.5 * (rec[zp][0][late].max() - rec[zp][0][late].min())
    Ia = 0.5 * (rec[zp][1][late].max() - rec[zp][1][late].min())
    Vf = np.sqrt(45 + 36 * np.cos(np.pi * zp / 100))
    If = np.sqrt(45 - 36 * np.cos(np.pi * zp / 100)) / 75
    print(f"    z = {zp:5.0f}: MoC amplitude V {Va:.5f} (formula {Vf:.5f}), I {Ia * 1e3:.4f} mA (formula {If * 1e3:.4f})")
    close(f"amplitudes at z = {zp}", [Va, Ia], [Vf, If], rtol=1e-4)
zz = np.linspace(0, 500, 5001)
A = np.sqrt(45 + 36 * np.cos(np.pi * zz / 100))
print(f"  max {A.max():.4f} V at z = {zz[np.isclose(A, A.max())].tolist()}, min {A.min():.4f} V at z = {zz[np.isclose(A, A.min())].tolist()}")
close("max/min V amplitude", [A.max(), A.min()], [9, 3])
print(f"  z = 0: V = 9 sin(pi t), I = 3 sin(pi t)/75 = {3 / 75 * 1e3} mA amplitude; KVL 12 - 75*0.04 = {12 - 75 * 0.04}")
Vt = rec[0.0][0][late]; It = rec[0.0][1][late]; tt_ = t_[late]
close("MoC V(0,t) = 9 sin(pi t), I = 0.04 sin(pi t)", [np.max(np.abs(Vt - 9 * np.sin(w * tt_))), np.max(np.abs(It - 0.04 * np.sin(w * tt_)))], [0, 0], atol=1e-8)
tf, rf = fdtd(Z0, Rg, RL, v, l, fi, 20.0, 2000, probes=(100.0, 200.0))
m = (tf > 16)
for zp, Vf in [(100.0, 3.0), (200.0, 9.0)]:
    Va = 0.5 * (rf[zp][0][m].max() - rf[zp][0][m].min())
    print(f"    FDTD amplitude at z = {zp}: {Va:.4f} V (formula {Vf})")
    close(f"FDTD amplitude z = {zp}", Va, Vf, rtol=0, atol=0.02)

hdr(f"SUMMARY: {sum(ALL)}/{len(ALL)} checks OK")
