#!/usr/bin/env python3
"""L28 practice checks: distributed circuits and bounce diagrams (numpy only).

Every number on practice/28-bounce-diagrams.md is printed here, found twice:
  (1) wave bookkeeping: the L28 page's series, forward segment n of weight
      tau_g (GL Gg)^n passing z at z/v + 2nT, backward segment n of weight
      tau_g GL (GL Gg)^n passing at 2T - z/v + 2nT; V = sum w f_i(t - t_k),
      I = sum (+-) w f_i(t - t_k) / Z0;
  (2) an independent FDTD simulation of the telegrapher's equations
      (Yee grid at Courant number 1, half-cell capacitors at the two ends,
      resistive source and load terminations by KVL/KCL, implicit in time, open/short/ideal
      source as limits). Impulses are simulated as narrow unit-area pulses
      and their weights recovered by integrating over a window.
Plateau values are sampled mid-interval; DC limits from long runs.
Units: metres, microseconds (or ns where stated), volts, ohms, amperes.
"""
import numpy as np

ALL = []
INF = np.inf


def hdr(s):
    print("\n" + "=" * 78 + "\n" + s + "\n" + "=" * 78)


def close(label, a, b, rtol=1e-6, atol=1e-9):
    a = np.asarray(a, float)
    b = np.asarray(b, float)
    ok = np.allclose(a, b, rtol=rtol, atol=atol)
    print(f"  [{label}] {np.round(a, 6).tolist()} vs {np.round(b, 6).tolist()} -> {'OK' if ok else 'FAIL'}")
    ALL.append(bool(ok))


def check(label, cond):
    print(f"  [{label}] {'OK' if cond else 'FAIL'}")
    ALL.append(bool(cond))


# ---------------------------------------------------------------- coefficients
def coeffs(Z0, Rg, RL):
    tg = Z0 / (Rg + Z0)
    Gg = (Rg - Z0) / (Rg + Z0)
    GL = 1.0 if RL == INF else (RL - Z0) / (RL + Z0)
    return tg, Gg, GL


# ---------------------------------------------------------------- bookkeeping
def segments(Z0, Rg, RL, T, zf, tmax):
    """Crossings of the vertical line z = zf*ell: list of (time, V weight, dir)."""
    tg, Gg, GL = coeffs(Z0, Rg, RL)
    out = []
    n = 0
    while True:
        tf = zf * T + 2 * n * T
        tb = 2 * T - zf * T + 2 * n * T
        if tf > tmax and tb > tmax:
            break
        wf = tg * (GL * Gg) ** n
        wb = tg * GL * (GL * Gg) ** n
        if tf <= tmax:
            out.append((tf, wf, +1))
        if tb <= tmax:
            out.append((tb, wb, -1))
        n += 1
    out.sort(key=lambda s: (s[0], -s[2]))
    return out


def bk(Z0, Rg, RL, T, zf, fi, t):
    """V and I at z = zf*ell, time t, for source f_i (vectorised callable)."""
    segs = segments(Z0, Rg, RL, T, zf, t + 1e-12)
    V = sum(w * fi(t - tk) for tk, w, d in segs)
    I = sum(d * w * fi(t - tk) for tk, w, d in segs) / Z0
    return float(V), float(I)


def step(t):
    return np.where(np.asarray(t) > 0, 1.0, 0.0)


def pulse(width):
    return lambda t: np.where((np.asarray(t) > 0) & (np.asarray(t) < width), 1.0, 0.0)


# ---------------------------------------------------------------- FDTD
class Line:
    """Lossless line, Courant number 1: V at nodes k*dz, I at (k+1/2)dz."""

    def __init__(self, Z0, T, Rg, RL, fi, N=1200):
        self.Z0, self.T, self.Rg, self.RL, self.fi, self.N = Z0, T, Rg, RL, fi, N
        self.dt = T / N                       # = dz / v

    def run(self, tmax, probes=(), snaps=()):
        Z0, N, dt, Rg, RL = self.Z0, self.N, self.dt, self.Rg, self.RL
        V = np.zeros(N + 1)
        I = np.zeros(N)
        a = 1 / (2 * Z0)                      # C dz / (2 dt)
        steps = int(round(tmax / dt))
        kp = [int(round(zf * N)) for zf in probes]
        tV = np.arange(steps + 1) * dt
        rec_V = np.zeros((len(kp), steps + 1))
        rec_I = np.zeros((len(kp), steps + 1))   # I at node, time n dt
        Ihalf_prev = I.copy()
        snap_steps = {int(round(ts / dt)): ts for ts in snaps}
        out_snaps = {}

        def node_I(Iold, Inew, Vn, n):
            # current at nodes at time n*dt: average of half-node values in space and time
            Ia = 0.5 * (Iold + Inew)
            In = np.empty(N + 1)
            In[1:N] = 0.5 * (Ia[:-1] + Ia[1:])
            if Rg == 0:
                In[0] = Ia[0]
            else:
                In[0] = (self.fi(n * dt) - Vn[0]) / Rg
            if RL == INF:
                In[N] = 0.0
            elif RL == 0:
                In[N] = Ia[-1]
            else:
                In[N] = Vn[N] / RL
            return In

        for n in range(steps):
            Inew = I - (V[1:] - V[:-1]) / Z0
            if n > 0:
                In = node_I(I_old_for_avg, I, V, n)
                for j, k in enumerate(kp):
                    rec_V[j, n] = V[k]
                    rec_I[j, n] = In[k]
                if n in snap_steps:
                    out_snaps[snap_steps[n]] = (V.copy(), In.copy())
            I_old_for_avg = I
            I = Inew
            Vn = V.copy()
            Vn[1:N] = V[1:N] - Z0 * (I[1:] - I[:-1])
            # source end
            if Rg == 0:
                Vn[0] = self.fi((n + 1) * dt)
            else:
                # implicit (backward-Euler) resistor current: damps the
                # Nyquist mode a Courant-1 half-cell boundary otherwise excites
                Vn[0] = (a * V[0] + self.fi((n + 1) * dt) / Rg - I[0]) / (a + 1 / Rg)
            # load end
            if RL == 0:
                Vn[N] = 0.0
            else:
                gL = 0.0 if RL == INF else 1 / RL
                Vn[N] = (a * V[N] + I[-1]) / (a + gL)
            V = Vn
        self.t = tV
        self.rec_V, self.rec_I, self.snaps = rec_V, rec_I, out_snaps
        return self

    def at(self, j, t):
        n = int(round(t / self.dt))
        return self.rec_V[j, n], self.rec_I[j, n]

    def weight(self, j, t0, half=None):
        """Integral of V and I over [t0 - half, t0 + half] (impulse weights),
        divided by the discrete area of the source samples (unit-area pulse)."""
        half = half or 0.2 * self.T
        m = (self.t > t0 - half) & (self.t < t0 + half)
        n = np.arange(len(self.t)) + 1
        area = np.sum(self.fi(n * self.dt)) * self.dt / self.amp
        return self.rec_V[j, m].sum() * self.dt / area, self.rec_I[j, m].sum() * self.dt / area


def narrow(width):
    """Unit-area rectangle of the given width (stands in for delta(t))."""
    return lambda t: np.where((np.asarray(t) > 0) & (np.asarray(t) < width), 1.0 / width, 0.0)


def scaled(f, A):
    return lambda t: A * f(t)


# ============================================================================
hdr("FDTD self-test against bookkeeping (five terminations, step source, four probes)")
for (Rg, RL) in [(150, 50 / 3), (25, 150), (0, 300), (50, INF), (30, 0)]:
    Z0, T = 50.0, 1.0
    sim = Line(Z0, T, Rg, RL, step).run(9.0, probes=(0, 0.25, 0.5, 1))
    errs = []
    for j, zf in enumerate((0, 0.25, 0.5, 1)):
        for t in np.arange(0.13, 8.9, 0.37):
            Vb, Ib = bk(Z0, Rg, RL, T, zf, step, t)
            Vs, Is = sim.at(j, t)
            # skip samples within one cell of a discontinuity
            near = any(abs(t - tk) < 0.05 * T for tk, _, _ in segments(Z0, Rg, RL, T, zf, 9))
            if not near:
                errs.append(max(abs(Vb - Vs), Z0 * abs(Ib - Is)))
    print(f"  Rg={Rg}, RL={RL}: max |V_bk - V_fdtd| (and Z0*dI) over {len(errs)} samples = {max(errs):.2e}")
    check(f"self-test Rg={Rg} RL={RL}", max(errs) < 1e-6)


# ============================================================================
hdr("28.1 Three coefficients: Z0 = 60, Rg = 20, RL = 180, 16 V step")
Z0, Rg, RL = 60.0, 20.0, 180.0
tg, Gg, GL = coeffs(Z0, Rg, RL)
print(f"  tau_g = {tg}, Gamma_g = {Gg}, Gamma_L = {GL}; current coefficients: load {-GL}, generator {-Gg}")
close("tau_g, Gg, GL", [tg, Gg, GL], [0.75, -0.5, 0.5])
close("tau_g = (1 - Gg)/2", tg, (1 - Gg) / 2)
print(f"  first wave: V+ = {16 * tg} V, I+ = {16 * tg / Z0} A, drop across Rg = {16 - 16 * tg} V = I+ Rg = {16 * tg / Z0 * Rg}")
close("V+, I+, Rg drop", [16 * tg, 16 * tg / Z0, 16 - 16 * tg], [12, 0.2, 4])
sim = Line(Z0, 1.0, Rg, RL, scaled(step, 16)).run(4.0, probes=(0, 0.5, 1))
close("FDTD V(0), I(0) at t = 1.0T (first epoch)", sim.at(0, 1.0), [12, 0.2])
close("FDTD V(l/2), I(l/2) at t = 0.8T", sim.at(1, 0.8), [12, 0.2])
# reflected current at the load: I(l) = (1 - GL) I+  => reflected/incident current = -GL
VL, IL = sim.at(2, 1.5)
print(f"  FDTD at load, t = 1.5T: V = {VL:.6f} = (1+GL)12, I = {IL:.6f} = (1-GL)0.2; reflected I / incident I = {(IL - 0.2) / 0.2:.6f}")
close("current reflection ratio = -GL", (IL - 0.2) / 0.2, -GL)
close("V/I at load = RL", VL / IL, RL)


# ============================================================================
hdr("28.2 True or false")
# (a) V/I = Z0 fails once an echo is present: example Z0 = 50, Rg = 50, RL = 150, at l/2 after echo
Z0 = 50.0
sim = Line(Z0, 1.0, 50, 150, step).run(3.0, probes=(0.5,))
V, I = sim.at(0, 1.8)
print(f"  (a) Z0 = 50, Rg = 50, RL = 150, 1 V step, z = l/2, t = 1.8T: V/I = {V / I:.4f} ohm (not 50)")
check("(a) false: V/I != Z0 after an echo", abs(V / I - Z0) > 1)
# (b) backward wave V/I = -Z0: isolate it as the change at t = 1.5T
V1, I1 = sim.at(0, 1.2)
dV, dI = V - V1, I - I1
print(f"  (b) backward wave alone: dV = {dV:.6f} V, dI = {dI:.6f} A, dV/dI = {dV / dI:.4f}")
close("(b) true: backward V/I = -Z0", dV / dI, -Z0)
# (c) Gamma_g independent of source amplitude: same Gg from 1 V and 7 V
for A in (1.0, 7.0):
    s = Line(Z0, 1.0, 150, 0, scaled(step, A)).run(3.0, probes=(0.5,))
    # forward A/4, backward -A/4, then Gg*(-A/4) forward at 2.5T
    w1 = s.at(0, 1.2)[0] - s.at(0, 0.8)[0] * 1
    w_back = s.at(0, 1.8)[0] - s.at(0, 1.2)[0]
    print(f"  (c) A = {A}: launched {s.at(0, 1.2)[0]:.6f}, backward {s.at(0, 1.6)[0] - s.at(0, 1.2)[0]:.6f}, "
          f"re-reflected {s.at(0, 2.8)[0] - s.at(0, 2.2)[0]:.6f}, Gg = {(s.at(0, 2.8)[0] - s.at(0, 2.2)[0]) / (s.at(0, 1.6)[0] - s.at(0, 1.2)[0]):.6f}")
    close(f"(c) Gg = 0.5 for Rg = 150 at A = {A}", (s.at(0, 2.8)[0] - s.at(0, 2.2)[0]) / (s.at(0, 1.6)[0] - s.at(0, 1.2)[0]), 0.5)
# (d) Rg = 0: V(0,t) = f_i(t) for any load
s = Line(Z0, 1.0, 0, 20, pulse(0.7)).run(6.0, probes=(0,))
ts = np.arange(0.05, 5.9, 0.1)
dev = max(abs(s.at(0, t)[0] - pulse(0.7)(t)) for t in ts if min(abs(t - 0.7), abs(t)) > 0.02)
print(f"  (d) Rg = 0, RL = 20, 0.7T pulse: max |V(0,t) - f_i(t)| = {dev:.2e}")
check("(d) true", dev < 1e-9)
# (e) tau_g vs 1 + Gg
for Rg in (0, 25, 50, 150, 1e6):
    tg, Gg, _ = coeffs(50, Rg, 50)
    print(f"  (e) Rg = {Rg}: tau_g = {tg:.4f}, (1-Gg)/2 = {(1 - Gg) / 2:.4f}, 1+Gg = {1 + Gg:.4f}")
tg, Gg, _ = coeffs(50, 150, 50)
check("(e) false: tau_g != 1 + Gg (Rg = 150: 0.25 vs 1.5)", abs(tg - 0.25) < 1e-12 and abs(1 + Gg - 1.5) < 1e-12)


# ============================================================================
hdr("28.3 A step meets four loads: incident 6 V on Z0 = 50 (12 V step, Rg = Z0)")
Z0 = 50.0
for RL, (Vexp, Iexp, Vr) in [(INF, (12, 0, 6)), (0, (0, 0.24, -6)), (50, (6, 0.12, 0)), (25, (4, 0.16, -2))]:
    _, _, GL = coeffs(Z0, Z0, RL)
    Vb, Ib = (1 + GL) * 6, (1 - GL) * 6 / Z0
    s = Line(Z0, 1.0, Z0, RL, scaled(step, 12)).run(3.0, probes=(1,))
    Vs, Is = s.at(0, 1.5)
    print(f"  RL = {RL}: GL = {GL:+.4f}, reflected {GL * 6:+.3f} V; V_L = {Vb:.4f} V, I_L = {Ib:.4f} A; FDTD {Vs:.6f} V, {Is:.6f} A")
    close(f"RL={RL} bookkeeping", [Vb, Ib, GL * 6], [Vexp, Iexp, Vr])
    close(f"RL={RL} FDTD", [Vs, Is], [Vexp, Iexp])


# ============================================================================
hdr("28.4 Arrival times at z = 100 m: l = 300 m, v = 200 m/us (T = 1.5 us), Rg = 25, RL = 150")
Z0, T = 50.0, 1.5
segs = segments(Z0, 25, 150, T, 100 / 300, 6.0)
times = [round(s[0], 6) for s in segs][:4]
print("  bookkeeping crossings:", [(round(s[0], 4), round(s[1], 4), 'fwd' if s[2] > 0 else 'bwd') for s in segs])
close("first four times", times, [0.5, 2.5, 3.5, 5.5])
s = Line(Z0, T, 25, 150, narrow(0.01)).run(6.2, probes=(1 / 3,))
v = s.rec_V[0]
pk = [s.t[i] for i in range(1, len(v) - 1) if abs(v[i]) > 1.0 and abs(v[i]) >= abs(v[i - 1]) and abs(v[i]) > abs(v[i + 1])]
# merge peaks within 0.05 us
merged = []
for p in pk:
    if not merged or p - merged[-1] > 0.05:
        merged.append(p)
print("  FDTD pulse arrivals (us):", [round(p, 3) for p in merged])
close("FDTD arrival times (pulse centre = start + 0.005)", np.array(merged[:4]) - 0.005, [0.5, 2.5, 3.5, 5.5], atol=0.01)
print("  distractors: (b) spacing T:", [0.5 + n * T for n in range(4)], " (c) forward only:", [0.5 + 2 * n * T for n in range(4)],
      " (d) backward at 2T + 2nT:", sorted([0.5, 3.5, 2 * T, 4 * T]))
close("distractors", [0.5 + n * T for n in range(4)] + [0.5 + 2 * n * T for n in range(4)] + sorted([0.5, 3.5, 2 * T, 4 * T]),
      [0.5, 2.0, 3.5, 5.0, 0.5, 3.5, 6.5, 9.5, 0.5, 3.0, 3.5, 6.0])


# ============================================================================
hdr("28.5 Find the error: Z0 = 50, Rg = 75, RL = 200, 10 V step")
Z0 = 50.0
tg, Gg, GL = coeffs(Z0, 75, 200)
print(f"  Gg = {Gg}, student tau = 1 + Gg = {1 + Gg}, student first wave {10 * (1 + Gg)} V, student V_L = {(1 + GL) * 10 * (1 + Gg)} V")
close("student numbers", [Gg, 1 + Gg, 10 * (1 + Gg), GL, (1 + GL) * 10 * (1 + Gg)], [0.2, 1.2, 12, 0.6, 19.2])
print(f"  correct tau_g = {tg}, first wave {10 * tg} V, V_L on (T,3T) = {(1 + GL) * 10 * tg} V, DC = {10 * 200 / 275:.4f} V")
close("correct", [tg, 10 * tg, (1 + GL) * 10 * tg], [0.4, 4, 6.4])
s = Line(Z0, 1.0, 75, 200, scaled(step, 10)).run(40.0, probes=(0, 1))
close("FDTD V(0) first epoch, V(l) on (T,3T)", [s.at(0, 1.0)[0], s.at(1, 2.0)[0]], [4, 6.4])
close("FDTD DC V(l)", s.at(1, 39.0)[0], 10 * 200 / 275, rtol=1e-4)
print(f"  student's 12 V exceeds the 10 V source; 1 + Gg vs (1 - Gg)/2 = {(1 - Gg) / 2}")


# ============================================================================
hdr("28.6 Ideal source: Rg = 0, Z0 = 100, RL = 300, 20 V step, l = 150 m, v = 300 m/us (T = 0.5 us)")
Z0, T = 100.0, 0.5
tg, Gg, GL = coeffs(Z0, 0, 300)
print(f"  tau_g = {tg}, Gg = {Gg}, GL = {GL}, GL*Gg = {GL * Gg}")
s = Line(Z0, T, 0, 300, scaled(step, 20)).run(40.0, probes=(0, 1))
VL_exp = [(0.25, 0), (0.75, 30), (1.25, 30), (1.75, 15), (2.25, 15), (2.75, 22.5), (3.25, 22.5), (3.75, 18.75)]
for t, Ve in VL_exp:
    Vb, Ib = bk(Z0, 0, 300, T, 1.0, scaled(step, 20), t)
    Vs, Is = s.at(1, t)
    print(f"  t = {t} us: V(l) bk {Vb:.4f}, FDTD {Vs:.6f}; I(l) = {Ib:.5f} A (FDTD {Is:.6f})")
    close(f"V(l,{t})", [Vb, Vs], [Ve, Ve])
I0_exp = [(0.5, 0.2), (1.5, 0.0), (2.5, 0.1), (3.5, 0.05), (4.25, 0.075)]
for t, Ie in I0_exp:
    Vb, Ib = bk(Z0, 0, 300, T, 0.0, scaled(step, 20), t)
    Vs, Is = s.at(0, t)
    print(f"  t = {t} us: I(0) bk {Ib:.5f}, FDTD {Is:.6f}; V(0) = {Vs:.6f}")
    close(f"I(0,{t})", [Ib, Is], [Ie, Ie])
    close(f"V(0,{t}) = 20", Vs, 20)
close("DC V(l), I(0) after 40 us", [s.at(1, 39.9)[0], s.at(0, 39.9)[1]], [20, 20 / 300], rtol=1e-4)
print(f"  DC: V = 20 V, I = {20 / 300:.5f} A; I(0) jumps: -2w/Z0 with w = 10, -5, 2.5 -> {[-2 * w / Z0 for w in (10, -5, 2.5)]}")


# ============================================================================
hdr("28.7 Reflectometry: Rg = Z0 = 50, 12 V step, v = 200 m/us; V(0) = 6 V then 8 V at 2.4 us")
Z0 = 50.0
ell = 200 * 2.4 / 2
GL = (8 - 6) / 6
RL = Z0 * (1 + GL) / (1 - GL)
print(f"  l = {ell} m, Gamma_L = {GL:.6f}, R_L = {RL:.6f} ohm, DC check 12*RL/(50+RL) = {12 * RL / (50 + RL):.6f}")
close("l, GL, RL", [ell, GL, RL], [240, 1 / 3, 100])
T = ell / 200
for RLx, after in [(100, 8.0), (25, 4.0), (0, 0.0), (INF, 12.0)]:
    s = Line(Z0, T, Z0, RLx, scaled(step, 12)).run(6.0, probes=(0,))
    print(f"  RL = {RLx}: V(0) at 1.2 us = {s.at(0, 1.2)[0]:.6f}, at 3.6 us = {s.at(0, 3.6)[0]:.6f}, at 5.9 us = {s.at(0, 5.9)[0]:.6f}")
    close(f"RL={RLx} record", [s.at(0, 1.2)[0], s.at(0, 3.6)[0], s.at(0, 5.9)[0]], [6, after, after])
print(f"  25 ohm: GL = {coeffs(50, 50, 25)[2]:.6f}")


# ============================================================================
hdr("28.8 Snapshots: Z0 = 50, Rg = 30, short, 16 V step, l = 400 m, v = 200 m/us (T = 2 us)")
Z0, T = 50.0, 2.0
tg, Gg, GL = coeffs(Z0, 30, 0)
print(f"  tau_g = {tg}, Gg = {Gg}, GL = {GL}; weights {[16 * tg, 16 * tg * GL, 16 * tg * GL * Gg, 16 * tg * GL ** 2 * Gg]}")
close("coefficients", [tg, Gg, GL, 16 * tg], [5 / 8, -0.25, -1, 10])
s = Line(Z0, T, 30, 0, scaled(step, 16), N=1200).run(60.0, snaps=(3.0, 5.0), probes=(0, 1))
for ts, (zlo, zhi) in [(3.0, ((10, 0.2), (0, 0.4))), (5.0, ((2.5, 0.45), (0, 0.4)))]:
    Vz, Iz = s.snaps[ts]
    z = np.linspace(0, 400, 1201)
    lo = (z > 5) & (z < 195)
    hi = (z > 205) & (z < 395)
    print(f"  t = {ts} us: z<200: V in [{Vz[lo].min():.6f},{Vz[lo].max():.6f}], I in [{Iz[lo].min():.6f},{Iz[lo].max():.6f}];"
          f" z>200: V in [{Vz[hi].min():.6f},{Vz[hi].max():.6f}], I in [{Iz[hi].min():.6f},{Iz[hi].max():.6f}]")
    close(f"t={ts} z<200 V,I", [Vz[lo].min(), Vz[lo].max(), Iz[lo].min(), Iz[lo].max()], [zlo[0], zlo[0], zlo[1], zlo[1]])
    close(f"t={ts} z>200 V,I", [Vz[hi].min(), Vz[hi].max(), Iz[hi].min(), Iz[hi].max()], [zhi[0], zhi[0], zhi[1], zhi[1]])
    for zf in (0.25, 0.75):
        print(f"    bookkeeping z = {400 * zf} m: V, I = {bk(Z0, 30, 0, T, zf, scaled(step, 16), ts)}")
print(f"  KVL at z=0, t=5: 16 - 30*0.45 = {16 - 30 * 0.45}")
close("DC (60 us): V(0), I(l)", [s.at(0, 59.0)[0], s.at(1, 59.0)[1]], [0, 16 / 30], rtol=1e-4, atol=1e-5)
print(f"  DC: V = 0, I = 16/30 = {16 / 30:.5f} A")


# ============================================================================
hdr("28.9 SP18-style: Z0 = 50, Rg = 25, RL = 200, l = 20 cm, v = 0.2 m/ns (T = 1 ns), 12u(t)")
Z0, T = 50.0, 1.0   # time unit ns here
tg, Gg, GL = coeffs(Z0, 25, 200)
print(f"  tau_g = {tg:.6f}, Gg = {Gg:.6f}, GL = {GL}, current coeffs: load {-GL}, gen {-Gg:.6f}, GL*Gg = {GL * Gg:.6f}")
close("coefficients", [tg, Gg, GL, GL * Gg], [2 / 3, -1 / 3, 0.6, -0.2])
w = [12 * tg]
for k in range(5):
    w.append(w[-1] * (GL if k % 2 == 0 else Gg))
print("  voltage weights (V):", [round(x, 6) for x in w])
print("  current weights (A):", [round(x / Z0 * (1 if k % 2 == 0 else -1), 6) for k, x in enumerate(w)])
close("V weights", w[:5], [8, 4.8, -1.6, -0.96, 0.32])
close("I weights", [x / Z0 * (1 if k % 2 == 0 else -1) for k, x in enumerate(w[:5])], [0.16, -0.096, -0.032, 0.0192, 0.0064])
s = Line(Z0, T, 25, 200, scaled(step, 12)).run(40.0, probes=(0, 0.25, 1))
for j, zf, rows in [(0, 0.0, [(1.0, 8, 0.16), (3.0, 11.2, 0.032), (5.0, 10.56, 0.0576)]),
                    (2, 1.0, [(0.5, 0, 0), (2.0, 12.8, 0.064), (4.0, 10.24, 0.0512), (6.0, 10.752, 0.05376)]),
                    (1, 0.25, [(3.5, 11.2, 0.032)])]:
    for t, Ve, Ie in rows:
        Vb, Ib = bk(Z0, 25, 200, T, zf, scaled(step, 12), t)
        Vs, Is = s.at(j, t)
        print(f"  z = {zf}l, t = {t} ns: bk V={Vb:.5f} I={Ib:.6f}; FDTD V={Vs:.6f} I={Is:.6f}")
        close(f"z={zf}l t={t}", [Vb, Ib, Vs, Is], [Ve, Ie, Ve, Ie])
print(f"  DC: V = 12*200/225 = {12 * 200 / 225:.5f} V, I = 12/225 = {12 / 225:.6f} A")
close("FDTD DC V(l), I(0)", [s.at(2, 39.0)[0], s.at(0, 39.0)[1]], [12 * 200 / 225, 12 / 225], rtol=1e-5)
close("series DC", 12 * tg * (1 + GL) / (1 - GL * Gg), 12 * 200 / 225)
print(f"  load current on (1,3) ns: 0.4*0.16 = {0.4 * 0.16}, 12.8/0.064 = {12.8 / 0.064} ohm; series 8*1.6/1.2 = {8 * 1.6 / 1.2:.4f}")


# ============================================================================
hdr("28.10 FA23-style: Rg = Z0 = 50, RL = 150, l = 600 m, v = 200 m/us (T = 3 us)")
Z0, T = 50.0, 3.0
tg, Gg, GL = coeffs(Z0, 50, 150)
print(f"  tau_g = {tg}, Gg = {Gg}, GL = {GL}")
print(f"  (a) step 200 V DC: V(0) = {200 * 150 / 200} V, I(l) = {200 / 200} A")
s = Line(Z0, T, 50, 150, scaled(step, 200)).run(12.0, probes=(0, 1))
close("(a) FDTD DC (reached at 2T for matched source)", [s.at(0, 7.0)[0], s.at(1, 7.0)[1]], [150, 1.0])
fi = scaled(pulse(4.0), 200)
s = Line(Z0, T, 50, 150, fi).run(14.0, probes=(0, 0.5, 1))
rows = {0: [(2, 100, 2), (5, 0, 0), (8, 50, -1), (11, 0, 0)],
        1: [(1, 0, 0), (3, 100, 2), (5, 150, 1), (7, 50, -1), (9, 0, 0)],
        2: [(2, 0, 0), (5, 150, 1), (8, 0, 0)]}
zfs = {0: 0.0, 1: 0.5, 2: 1.0}
for j in (0, 1, 2):
    for t, Ve, Ie in rows[j]:
        Vb, Ib = bk(Z0, 50, 150, T, zfs[j], fi, t)
        Vs, Is = s.at(j, t)
        print(f"  z = {zfs[j]}l, t = {t} us: bk V={Vb:.4f} I={Ib:.4f}; FDTD V={Vs:.6f} I={Is:.6f}")
        close(f"z={zfs[j]}l t={t}", [Vb, Ib, Vs, Is], [Ve, Ie, Ve, Ie])
print("  midpoint intervals: forward on (1.5, 5.5), backward on (4.5, 8.5)")
# energy (uJ): into the line at z = 0, into the load, from the source, in Rg
P0 = s.rec_V[0] * s.rec_I[0]
PL = s.rec_V[2] * s.rec_I[2]
E0 = P0.sum() * s.dt
EL = PL.sum() * s.dt
Isrc = s.rec_I[0]
Esrc = (fi(s.t) * Isrc).sum() * s.dt
ERg = (50 * Isrc ** 2).sum() * s.dt
print(f"  energy into line at z=0: {E0:.4f} uJ (= 100*2*4 - 50*1*4 = {100 * 2 * 4 - 50 * 1 * 4}); into load {EL:.4f} uJ (= 150*1*4 = 600)")
print(f"  from source {Esrc:.4f} uJ (= 200*2*4 = 1600); in Rg {ERg:.4f} uJ (= 4*50*4 + 1*50*4 = {4 * 50 * 4 + 50 * 4})")
close("energies", [E0, EL, Esrc, ERg], [600, 600, 1600, 1000], rtol=2e-3)


# ============================================================================
hdr("28.11 S20-final-style: Z0 = 60, Rg = 20, RL = 300, l = 300 m, v = 100 m/us (T = 3 us), z = 100 m")
Z0, T = 60.0, 3.0
tg, Gg, GL = coeffs(Z0, 20, 300)
print(f"  tau_g = {tg}, Gg = {Gg}, GL = {GL:.6f}, GL*Gg = {GL * Gg:.6f}; eps_r = (300/100)^2 = {(300 / 100) ** 2}")
close("coefficients", [tg, Gg, GL], [0.75, -0.5, 2 / 3])
segs = segments(Z0, 20, 300, T, 1 / 3, 14.0)
print("  12 delta(t): crossings (t, V weight, I weight):",
      [(round(t, 4), round(12 * wv, 5), round(12 * d * wv / Z0, 6)) for t, wv, d in segs])
close("times", [x[0] for x in segs], [1, 5, 7, 11, 13])
close("V weights (V us)", [12 * x[1] for x in segs], [9, 6, -3, -2, 1])
close("I weights (A us)", [12 * x[1] * x[2] / Z0 for x in segs], [0.15, -0.1, -0.05, 1 / 30, 1 / 60])
s = Line(Z0, T, 20, 300, scaled(narrow(0.06), 12), N=1200)
s.amp = 12.0
s.run(14.5, probes=(1 / 3,))
fw = [s.weight(0, t + 0.03, half=0.5) for t in (1, 5, 7, 11, 13)]
print("  FDTD impulse weights (V us, A us):", [(round(a, 5), round(b, 6)) for a, b in fw])
close("FDTD V weights", [a for a, b in fw], [9, 6, -3, -2, 1], rtol=1e-4)
close("FDTD I weights", [b for a, b in fw], [0.15, -0.1, -0.05, 1 / 30, 1 / 60], rtol=1e-4)
s = Line(Z0, T, 20, 300, scaled(step, 12)).run(80.0, probes=(1 / 3, 1))
stair = [(0.5, 0, 0), (3, 9, 0.15), (6, 15, 0.05), (9, 12, 0.0), (12, 10, 1 / 30), (13.5, 11, 0.05)]
for t, Ve, Ie in stair:
    Vb, Ib = bk(Z0, 20, 300, T, 1 / 3, scaled(step, 12), t)
    Vs, Is = s.at(0, t)
    print(f"  step t = {t}: bk V={Vb:.5f} I={Ib:.6f}; FDTD V={Vs:.6f} I={Is:.6f}")
    close(f"step t={t}", [Vb, Ib, Vs, Is], [Ve, Ie, Ve, Ie])
print(f"  DC: V = 12*300/320 = {12 * 300 / 320} V, I = 12/320 = {12 / 320} A")
close("FDTD DC at z = l/3 and l", [s.at(0, 79.0)[0], s.at(0, 79.0)[1], s.at(1, 79.0)[0]], [11.25, 0.0375, 11.25], rtol=1e-5)
close("series DC", 12 * tg * (1 + GL) / (1 - GL * Gg), 11.25)


# ============================================================================
hdr("28.12 Open line as a capacitor: Z0 = 50, Rg = 450, open, l = 100 m, v = 200 m/us (T = 0.5 us), 10 V")
Z0, T = 50.0, 0.5
tg, Gg, GL = coeffs(Z0, 450, INF)
print(f"  tau_g = {tg}, Gg = {Gg}, GL = {GL}")
close("coefficients", [tg, Gg, GL], [0.1, 0.8, 1.0])
s = Line(Z0, T, 450, INF, scaled(step, 10), N=600).run(30.0, probes=(0, 1))
for n in range(5):
    t = (2 * n + 2) * T
    Vf = 10 * (1 - 0.8 ** (n + 1))
    Vb, _ = bk(Z0, 450, INF, T, 1.0, scaled(step, 10), t)
    print(f"  n = {n}: V(l) on ({2 * n + 1}T,{2 * n + 3}T) formula {Vf:.5f}, bk {Vb:.5f}, FDTD {s.at(1, t)[0]:.6f}")
    close(f"stair n={n}", [Vb, s.at(1, t)[0]], [Vf, Vf])
close("first values", [10 * (1 - 0.8 ** k) for k in (1, 2, 3)], [2, 3.6, 4.88])
nreq = np.log(0.01) / np.log(0.8)
print(f"  0.8^(n+1) <= 0.01 -> n+1 >= {nreq:.4f} -> n+1 = 21, step at (2*20+1)T = {41 * T} us; 0.8^20 = {0.8 ** 20:.5f}, 0.8^21 = {0.8 ** 21:.5f}")
plate = [(n, s.at(1, (2 * n + 2) * T)[0]) for n in range(28)]
nfirst = next(n for n, Vp in plate if Vp >= 9.9)
print(f"  FDTD plateaus: n = 19: {plate[19][1]:.5f} V, n = 20: {plate[20][1]:.5f} V; first plateau >= 9.9 V starts at {(2 * nfirst + 1) * T} us")
close("99% time", [(2 * nfirst + 1) * T], [20.5])
C = 100 / (200e6 * 1e-6 * 50)  # l / (v Z0) with v in m/s -> F
C = 100 / (2e8 * 50)
tau = 450 * C
print(f"  C = l/(v Z0) = {C * 1e9:.4f} nF, Rg C = {tau * 1e6:.4f} us = {tau * 1e6 / T:.2f} T; RC 99% time = {tau * 1e6 * np.log(100):.4f} us")
print(f"  per round trip 2T = 1 us: staircase factor {Gg}, exponential factor e^(-1/4.5) = {np.exp(-1 / 4.5):.5f}")
close("C, RgC, 99% RC", [C * 1e9, tau * 1e6, tau * 1e6 * np.log(100)], [10, 4.5, 20.7233], rtol=1e-4)
x = 50 / 450
print(f"  x = Z0/Rg = {x:.5f}: Gg = (1-x)/(1+x) = {(1 - x) / (1 + x):.6f}; e^(-2x) = {np.exp(-2 * x):.6f}; "
      f"e^(-2(x + x^3/3 + x^5/5)) = {np.exp(-2 * (x + x ** 3 / 3 + x ** 5 / 5)):.6f}; -2 artanh(x) = {-2 * np.arctanh(x):.6f} = ln Gg {np.log(0.8):.6f}")
close("ln Gg = -2 artanh(x)", np.log((1 - x) / (1 + x)), -2 * np.arctanh(x))
close("e^(-2T/RgC) = e^(-2x)", np.exp(-2 * T / 4.5), np.exp(-2 * x))
print(f"  ln100/ln1.25 = {np.log(100) / np.log(1.25):.4f}; final value V0*RL/(Rg+RL) -> 10 V for RL -> inf")
# V(0,t) staircase for completeness
for n in range(3):
    t = (2 * n + 1) * T
    print(f"  V(0) on ({2 * n}T,{2 * n + 2}T): formula 10 - 9*0.8^n = {10 - 9 * 0.8 ** n:.4f}, FDTD {s.at(0, t)[0]:.6f}")
    close(f"V(0) n={n}", s.at(0, t)[0], 10 - 9 * 0.8 ** n)
close("FDTD DC V(l), I(0) at 29.9 us", [s.at(1, 29.9)[0] > 9.9, abs(s.at(0, 29.9)[1]) < 0.0003], [1, 1])

hdr(f"SUMMARY: {sum(ALL)}/{len(ALL)} checks OK")
if not all(ALL):
    raise SystemExit(1)
