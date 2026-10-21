#!/usr/bin/env python3
"""Independent review checks for the Lecture 29 page set (bounce-diagram examples).

Two independent time-steppings of a lossless line driven by a Thevenin source (fi behind Rg) at z = 0
and terminated by RL at z = l; neither uses a reflection coefficient, only circuit laws at the ends:
  * MoC: forward/backward characteristic amplitudes shifted one cell per step (dz = v dt, exact on grid);
         ends solved from KVL f_i = Rg I + V and Ohm's law V = RL I.
  * FDTD: Yee leapfrog of the telegrapher's equations with half-cell lumped-element ends.
Units: us, m, V, ohm (currents in A unless stated).
"""
import sys
import numpy as np

OUT = []
NFAIL = 0


def rep(name, ok, info=""):
    global NFAIL
    s = f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  [{info}]" if info else "")
    OUT.append(s); print(s)
    if not ok:
        NFAIL += 1


def close(a, b, tol=1e-9):
    return np.allclose(a, b, atol=tol, rtol=0)


# ------------------------------------------------------------------------------------------------ steppers
def moc(Z0, v, ell, Rg, RL, fi, t0, t1, dz, snap_t=(), probe_z=()):
    """method of characteristics; returns snapshots {t: (z, V, I)} and probes {z: (t, V, I)}"""
    N = int(round(ell / dz)); dt = dz / v
    z = np.arange(N + 1) * dz
    a = np.zeros(N + 1); b = np.zeros(N + 1)      # forward / backward voltage amplitudes
    nsteps = int(round((t1 - t0) / dt))
    snap_n = {int(round((ts - t0) / dt)): ts for ts in snap_t}
    pk = [int(round(zp / dz)) for zp in probe_z]
    tp = np.empty(nsteps + 1); Vp = np.empty((len(pk), nsteps + 1)); Ip = np.empty_like(Vp)
    snaps = {}
    rg = Rg / Z0; rl = RL / Z0
    for n in range(nsteps + 1):
        t = t0 + n * dt
        if n > 0:
            a[1:] = a[:-1].copy(); b[:-1] = b[1:].copy()
            # load: V = RL I with V = a+b, I = (a-b)/Z0
            b[N] = a[N] * (rl - 1) / (rl + 1)
        # generator: fi = Rg (a-b)/Z0 + a + b
        a[0] = (fi(np.array([t]))[0] - b[0] * (1 - rg)) / (1 + rg)
        V = a + b; I = (a - b) / Z0
        tp[n] = t
        for j, k in enumerate(pk):
            Vp[j, n] = V[k]; Ip[j, n] = I[k]
        if n in snap_n:
            snaps[snap_n[n]] = (z.copy(), V.copy(), I.copy())
    probes = {zp: (tp, Vp[j], Ip[j]) for j, zp in enumerate(probe_z)}
    return snaps, probes


def fdtd(Z0, v, ell, Rg, RL, fi, t0, t1, dz, S=1.0, snap_t=(), probe_z=()):
    """Yee FDTD of dV/dz = -L dI/dt, dI/dz = -C dV/dt; lumped half cells at the ends"""
    Lp = Z0 / v; Cp = 1 / (Z0 * v)
    N = int(round(ell / dz)); dt = S * dz / v
    z = np.arange(N + 1) * dz
    V = np.zeros(N + 1); I = np.zeros(N)            # I at k+1/2, time n+1/2
    nsteps = int(round((t1 - t0) / dt))
    snap_n = {int(round((ts - t0) / dt)): ts for ts in snap_t}
    pk = [int(round(zp / dz)) for zp in probe_z]
    tp = np.empty(nsteps + 1); Vp = np.empty((len(pk), nsteps + 1)); Ip = np.empty_like(Vp)
    snaps = {}
    h = Cp * dz / (2 * dt)

    def node_I(V, I, t):
        In = np.empty(N + 1)
        In[1:N] = 0.5 * (I[:-1] + I[1:])
        In[0] = (fi(np.array([t]))[0] - V[0]) / Rg if Rg > 0 else I[0]
        In[N] = V[N] / RL
        return In
    for n in range(nsteps + 1):
        t = t0 + n * dt
        if n > 0:
            tm = t - dt                               # V known at tm; I at tm + dt/2
            I -= dt / (Lp * dz) * (V[1:] - V[:-1])
            Vn = V.copy()
            Vn[1:N] = V[1:N] - dt / (Cp * dz) * (I[1:] - I[:-1])
            if Rg == 0:
                Vn[0] = fi(np.array([t]))[0]
            else:
                fh = fi(np.array([tm + dt / 2]))[0]
                Vn[0] = (V[0] * (h - 1 / (2 * Rg)) + fh / Rg - I[0]) / (h + 1 / (2 * Rg))
            Vn[N] = (V[N] * (h - 1 / (2 * RL)) + I[N - 1]) / (h + 1 / (2 * RL))
            V = Vn
        In = node_I(V, I, t)
        tp[n] = t
        for j, k in enumerate(pk):
            Vp[j, n] = V[k]; Ip[j, n] = In[k]
        if n in snap_n:
            snaps[snap_n[n]] = (z.copy(), V.copy(), In.copy())
    probes = {zp: (tp, Vp[j], Ip[j]) for j, zp in enumerate(probe_z)}
    return snaps, probes


def at(zarr, arr, zq):
    return np.interp(zq, zarr, arr)


def coeffs(Z0, Rg, RL):
    return Z0 / (Rg + Z0), (Rg - Z0) / (Rg + Z0), (RL - Z0) / (RL + Z0)


def page_series(z_over_v, t, fi, tg, GL, Gg, T, nmax=60):
    """the page's horizontal-cut / impulse-response series (Lecture 28 key box)"""
    V = 0 * (z_over_v + t); ZI = 0 * (z_over_v + t)
    for n in range(nmax):
        F = tg * (GL * Gg) ** n * fi(t - z_over_v - 2 * n * T)
        B = tg * GL * (GL * Gg) ** n * fi(t + z_over_v - 2 * (n + 1) * T)
        V = V + F + B; ZI = ZI + F - B
    return V, ZI


# ------------------------------------------------------------------------------------------------ sources
W1 = 2 * np.pi * 1.0                                   # rad/us, 1 MHz


def f_sin(t):
    t = np.asarray(t, float); return np.sin(W1 * t) * (t >= 0)


def f_step(t):
    return 1.0 * (np.asarray(t, float) >= 0)


def f_ex3(t):
    t = np.asarray(t, float)
    return 1.0 * ((t > -0.5) & (t < 0.5)) + 2.0 * ((t >= 0.5) & (t < 1.5))


def f_ramp(t):
    t = np.asarray(t, float); return 3.0 * t * ((t > 0) & (t < 1))


print("Lecture 29 independent review"); print("=" * 60)

# ================================================================================================ A. Example 1
print("\nA. Example 1: l = 900 m, v = c = 300 m/us, Rg = Z0, RL = 2 Z0, sin(wt)u(t), 1 MHz")
for Z0 in (50.0, 75.0, 300.0):
    tg, Gg, GL = coeffs(Z0, Z0, 2 * Z0)
    rep(f"A1 tau_g = 1/2, Gamma_g = 0, Gamma_L = 1/3 (Z0 = {Z0:g})", close([tg, Gg, GL], [0.5, 0, 1 / 3]))
c = 300.0; ell1 = 900.0; T1 = ell1 / c
rep("A1 2T = 6 us", close(2 * T1, 6.0))
lam = c / 1.0
rep("A2 lambda = 300 m, l = 3 lambda", close([lam, ell1 / lam], [300, 3]))
Z0 = 50.0
snapt = (1.0, 2.0, 4.5, 6.0, 7.0, 10.0, 10.25)
s1, p1 = moc(Z0, c, ell1, Z0, 2 * Z0, f_sin, 0.0, 14.0, 0.25, snap_t=snapt, probe_z=(0.0, 450.0, 900.0))
errV = errI = 0
for ts in snapt:
    z, V, I = s1[ts]
    Vp_, ZIp = page_series(z / c, ts, f_sin, 0.5, 1 / 3, 0.0, T1)
    # page closed form (only two terms)
    Vc = 0.5 * f_sin(ts - z / c) + (1 / 6) * f_sin(ts + z / c - 6)
    ZIc = 0.5 * f_sin(ts - z / c) - (1 / 6) * f_sin(ts + z / c - 6)
    errV = max(errV, np.max(abs(V - Vc)), np.max(abs(V - Vp_))); errI = max(errI, np.max(abs(Z0 * I - ZIc)))
rep("A3 page V(z,t) (two terms) = MoC at t = 1, 2, 4.5, 6, 7, 10, 10.25 us", errV < 1e-9, f"max err {errV:.1e}")
rep("A3 page Z0 I(z,t) (same with -1/6) = MoC", errI < 1e-9, f"max err {errI:.1e}")
# A4 front positions and wavelengths in the snapshots
for ts, front in ((1.0, 300.0), (2.0, 600.0)):
    z, V, I = s1[ts]
    beyond = np.max(abs(V[z > front + 1e-9])); amp = np.max(abs(V[z < front]))
    zc = z[(z < front)]; Vc_ = V[(z < front)]
    ncross = np.sum(np.sign(Vc_[1:-1]) * np.sign(Vc_[2:]) < 0) if len(Vc_) > 2 else 0
    nwav = front / lam
    rep(f"A4 t = {ts:g} us: front at {front:g} m, amplitude 1/2 behind it, {nwav:g} wavelength(s)",
        beyond < 1e-12 and abs(amp - 0.5) < 1e-6 and close(nwav, ts), f"max|V| beyond {beyond:.0e}, amp {amp:.4f}")
z, V, I = s1[1.0]
rep("A4b notes' margin plot: V(75 m, 1 us) = -1/2 (negative next to z = 0), V(225 m, 1 us) = +1/2",
    close([at(z, V, 75), at(z, V, 225)], [-0.5, 0.5], 1e-9))
# A5 load voltage
tp, VL, IL = p1[900.0]
m = (tp > 3.0) & (tp < 14.0)
rep("A5 V(l,t) = (2/3) sin w(t-3) for t > 3 us", close(VL[m], (2 / 3) * np.sin(W1 * (tp[m] - 3)), 1e-9))
rep("A5 V(l,t) = 0 for t < 3 us", np.max(abs(VL[tp < 3.0])) < 1e-12)
rep("A5 V(l)/I(l) = RL = 100 ohm where I != 0", np.allclose(VL[m][abs(IL[m]) > 1e-4], 100 * IL[m][abs(IL[m]) > 1e-4]))
# A6 echo front at 4.5 us
z, V, I = s1[4.5]
inc = 0.5 * f_sin(4.5 - z / c)
d = V - inc
rep("A6 t = 4.5 us: echo front at z = 450 m (V = incident alone for z < 450, echo added for z > 450)",
    np.max(abs(d[z < 450])) < 1e-12 and np.max(abs(d[z > 451])) > 0.1)
# A7 steady state t > 6 us
tt = np.linspace(6.0, 14.0, 4001); zz = np.linspace(0, 900, 3601)
TT, ZZ = np.meshgrid(tt, zz)
beta = W1 / c
Vss = 0.5 * np.sin(W1 * TT - beta * ZZ) + (1 / 6) * np.sin(W1 * TT + beta * ZZ)
Vpg = 0.5 * f_sin(TT - ZZ / c) + (1 / 6) * f_sin(TT + ZZ / c - 6)
rep("A7 for t >= 6 us the line holds 1/2 sin(wt - bz) + 1/6 sin(wt + bz) (w 6 us = 12 pi)",
    close(Vss, Vpg, 1e-9) and close(W1 * 6.0, 12 * np.pi))
envph = abs(0.5 * np.exp(-1j * beta * zz) + (1 / 6) * np.exp(1j * beta * zz))
zmax = zz[np.r_[False, (envph[1:-1] > envph[:-2]) & (envph[1:-1] >= envph[2:]), False]]
rep("A7 envelope between 1/3 and 2/3", close([envph.min(), envph.max()], [1 / 3, 2 / 3], 1e-6))
rep("A7 maxima every 150 m incl. the load (z = 0,150,...,900)",
    close(envph[np.isin(zz, np.arange(0, 901, 150))], 2 / 3, 1e-9) and close(np.diff(zmax), 150, 1e-6),
    f"interior maxima at {zmax}")
# envelope from the MoC time series at probe points 450 m and 900 m over 10-14 us
tp, V450, _ = p1[450.0]
rep("A7 MoC amplitude at z = 450 m (a maximum, 1.5 lambda) = 2/3 and at load = 2/3",
    abs(np.max(abs(V450[tp > 8])) - 2 / 3) < 1e-3 and abs(np.max(abs(p1[900.0][1][tp > 8])) - 2 / 3) < 1e-3)
# FDTD cross-check, Example 1
sF, pF = fdtd(Z0, c, ell1, Z0, 2 * Z0, f_sin, 0.0, 10.0, 0.5, S=1.0, snap_t=(2.0, 4.5, 10.0))
e = max(np.max(abs(sF[ts][1] - (0.5 * f_sin(ts - sF[ts][0] / c) + f_sin(ts + sF[ts][0] / c - 6) / 6))) for ts in sF)
rep("A8 FDTD (Yee, S = 1, dz = 0.5 m) agrees with the page's V(z,t)", e < 2e-2, f"max err {e:.1e}")

# ================================================================================================ B. Example 2
print("\nB. Example 2: Z0 = 50, l = 2400 m, Rg = 0, RL = 100, u(t), z = 1200 m")
tg, Gg, GL = coeffs(50.0, 0.0, 100.0)
rep("B1 tau_g = 1, Gamma_g = -1, Gamma_L = 1/3, T = 8 us", close([tg, Gg, GL, 2400 / 300], [1, -1, 1 / 3, 8]))
s2, p2 = moc(50.0, c, 2400.0, 0.0, 100.0, f_step, 0.0, 400.0, 2.0, probe_z=(1200.0,))
tp, V12, I12 = p2[1200.0]
mids = np.array([8, 16, 24, 32, 40, 48, 56, 64])
Vlev = np.interp(mids, tp, V12); Ilev = np.interp(mids, tp, I12) * 1e3
rep("B2 levels 1, 4/3, 1, 8/9, 1, 28/27, 1 V", close(Vlev[:7], [1, 4 / 3, 1, 8 / 9, 1, 28 / 27, 1], 1e-9), f"{np.round(Vlev, 4)}")
rep("B3 I levels 20, 13.3, 6.7, 8.9, 11.1, 10.4, 9.6 mA",
    close(np.round(Ilev[:7], 1), [20, 13.3, 6.7, 8.9, 11.1, 10.4, 9.6], 1e-9), f"{np.round(Ilev, 2)}")
rep("B3 V = 0 and I = 0 before 4 us", np.max(abs(V12[tp < 3.99])) == 0 and np.max(abs(I12[tp < 3.99])) == 0)
# crossings: step sizes at 4, 12, 20, ...
ct = np.arange(4, 60, 8.0)
dV = np.interp(ct + 1, tp, V12) - np.interp(ct - 1, tp, V12)
dZI = 50 * (np.interp(ct + 1, tp, I12) - np.interp(ct - 1, tp, I12))
rep("B4 h_1200 weights 1, 1/3, -1/3, -1/9, 1/9, 1/27, -1/27 at t = 4, 12, ..., 52 us",
    close(dV, [1, 1 / 3, -1 / 3, -1 / 9, 1 / 9, 1 / 27, -1 / 27], 1e-9))
rep("B5 page Z0 I: +1, -1/3, -1/3, +1/9, +1/9, -1/27, ... (backward steps flipped)",
    close(dZI, [1, -1 / 3, -1 / 3, 1 / 9, 1 / 9, -1 / 27, -1 / 27], 1e-9))
rep("B6 DC limit: V(1200, 400 us) = 1 V, I = 10 mA",
    abs(V12[-1] - 1) < 1e-9 and abs(I12[-1] - 0.010) < 1e-9, f"V {V12[-1]:.6f}, I {I12[-1] * 1e3:.6f} mA")
rep("B7 lumped divider V0 RL/(Rg+RL) = 1 V, V0/(Rg+RL) = 10 mA", close([100 / 100, 1 / 100], [1, 0.01]))
errs = Vlev[[1, 3, 5]] - 1
rep("B8 error ratio per round trip = Gamma_L Gamma_g = -1/3", close(errs[1:] / errs[:-1], -1 / 3, 1e-9))
rep("B9 on 12-20 us V = 4/3 V, I = 13.3 mA, V/Z0 = 26.7 mA",
    close([Vlev[1], round(Ilev[1], 1), round(Vlev[1] / 50 * 1e3, 1)], [4 / 3, 13.3, 26.7], 1e-9))
s2F, p2F = fdtd(50.0, c, 2400.0, 0.0, 100.0, f_step, 0.0, 70.0, 2.0, S=1.0, probe_z=(1200.0,))
tpF, VF, IF = p2F[1200.0]
eF = np.max(abs(np.interp(mids[:7], tpF, VF) - Vlev[:7]))
eI = np.max(abs(np.interp(mids[:7], tpF, IF) * 1e3 - Ilev[:7]))
rep("B10 FDTD agrees with the levels (V and I)", eF < 1e-2 and eI < 0.2, f"V err {eF:.1e}, I err {eI:.2f} mA")

# ================================================================================================ C. Example 3
print("\nC. Example 3: Example 2's circuit, f_i = rect(t) + 2 rect(t-1)")
rep("C1 f_i: 1 V on (-0.5, 0.5), 2 V on (0.5, 1.5), 0 outside",
    close(f_ex3(np.array([-0.6, -0.4, 0.4, 0.6, 1.4, 1.6])), [0, 1, 1, 2, 2, 0]))
st3 = (3.0, 9.0, 11.0, 20.0, 27.0, 30.0)
s3, p3 = moc(50.0, c, 2400.0, 0.0, 100.0, f_ex3, -1.0, 32.0, 1.0, snap_t=st3)
emax = 0
for ts in st3:
    z, V, I = s3[ts]
    Vpg, ZIpg = page_series(z / c, ts, f_ex3, 1.0, 1 / 3, -1.0, 8.0)
    # exclude points within 3 m of a discontinuity of any term
    ok = np.ones_like(z, bool)
    for n in range(4):
        for edge in (-0.5, 0.5, 1.5):
            ok &= abs((ts - z / c - 16 * n) - edge) > 0.011
            ok &= abs((ts + z / c - 16 * (n + 1)) - edge) > 0.011
    emax = max(emax, np.max(abs(V - Vpg)[ok]), np.max(abs(50 * I - ZIpg)[ok]))
rep("C2 page series V and 50 I vs MoC at t = 3, 9, 11, 20, 27, 30 us", emax < 1e-12, f"max err {emax:.1e}")


def plateau(ts, zq):
    z, V, I = s3[ts]
    return at(z, V, zq), at(z, I, zq) * 1e3


Vq, Iq = plateau(3.0, np.array([300, 600, 900, 1200]))
rep("C3 t = 3: 2 V on 450-750 m, 1 V on 750-1050 m, 0 elsewhere; I = 40, 20 mA",
    close(Vq, [0, 2, 1, 0]) and close(Iq, [0, 40, 20, 0], 1e-9))
Vq, Iq = plateau(11.0, np.array([1200, 1500, 1800, 2100]))
rep("C4 t = 11: 1/3 V on 1350-1650, 2/3 V on 1650-1950, I = -V/50",
    close(Vq, [0, 1 / 3, 2 / 3, 0]) and close(Iq, [0, -1 / 3 / 50e-3, -2 / 3 / 50e-3, 0], 1e-9))
Vq, Iq = plateau(9.0, np.array([1800, 2100, 2350]))
rep("C5 t = 9: 0 below 1950; 1/3 V, -6.7 mA on 1950-2250; 8/3 V, 26.7 mA on 2250-2400",
    close(Vq, [0, 1 / 3, 8 / 3]) and close(np.round(Iq, 1), [0, -6.7, 26.7]))
rep("C5 V/I = 100 ohm = RL on 2250-2400 m at 9 us", close(Vq[2] / (Iq[2] * 1e-3), 100, 1e-9))
# edges at the quoted positions
for ts, edges in ((3.0, (450, 750, 1050)), (11.0, (1350, 1650, 1950)), (9.0, (1950, 2250))):
    z, V, I = s3[ts]
    jumps = [abs(at(z, V, e + 2) - at(z, V, e - 2)) > 0.3 for e in edges]
    rep(f"C6 t = {ts:g}: jumps at {edges} m", all(jumps))
z, V, I = s3[3.0]
rep("C7 pulse length = v x 2 us = 600 m (450-1050)", close(1050 - 450, 300 * 2.0))
# only the first forward / first echo terms
z, V, I = s3[11.0]
rep("C8 t = 11: only the first echo (1/3) f_i(z/c - 5)", np.max(abs(V - f_ex3(z / c - 5) / 3)) < 1e-12)
# order: 1 V part leads
rep("C9 t = 3: 1 V part (sent first) at larger z; t = 11: 1 V part at smaller z (1/3 V on the left)",
    plateau(3.0, 900)[0] == 1 and plateau(3.0, 600)[0] == 2 and close(plateau(11.0, 1500)[0], 1 / 3))
# notes' "circuit of Example 1" would give tau_g = 1/2, Gamma_g = 0, 2T = 6 us: the notes' 16 us needs l = 2400 m
rep("C10 notes' Example 3 numbers (tau_g = 1, Gamma_g = -1, 2l/c = 16 us) are Example 2's, not Example 1's",
    close([2 * 2400 / 300, 2 * 900 / 300], [16, 6]))

# ================================================================================================ D. general horizontal-cut rule
print("\nD. Horizontal-cut series for a generic circuit; which segments a snapshot needs")
rng = np.random.default_rng(29)
Z0d, vd, elld = 75.0, 200.0, 1000.0
Rgd, RLd = 30.0, 400.0
tgd, Ggd, GLd = coeffs(Z0d, Rgd, RLd)
Td = elld / vd


def f_tri(t):
    t = np.asarray(t, float); return np.where((t > 0) & (t < 2.0), 1 - abs(t - 1), 0.0)


tsd = (3.0, 6.0, 11.5, 17.0)
sD, _ = moc(Z0d, vd, elld, Rgd, RLd, f_tri, 0.0, 18.0, 0.5, snap_t=tsd)
eD = 0
for ts in tsd:
    z, V, I = sD[ts]
    Vpg, ZIpg = page_series(z / vd, ts, f_tri, tgd, GLd, Ggd, Td)
    eD = max(eD, np.max(abs(V - Vpg)), np.max(abs(Z0d * I - ZIpg)))
rep("D1 page series (forward w f_i(t-z/v-2nT), backward w f_i(t+z/v-2(n+1)T)) = MoC, generic circuit", eD < 1e-9,
    f"Z0 {Z0d}, Rg {Rgd}, RL {RLd}, err {eD:.1e}")
# A segment the cut does not cross can still contribute (pulse tail in flight): Example 3 at 9 us
# The horizontal cut at 9 us crosses only backward segment 0 (8-16 us); forward segment 0 (0-8 us) still contributes.
z, V, I = s3[9.0]
fwd0 = f_ex3(9.0 - z / c)
rep("D2 Example 3, t = 9 us: forward segment 0 (ended at 8 us, not crossed by the cut) still contributes 2 V near the load",
    np.max(fwd0) == 2.0 and close(at(z, V, 2350), 8 / 3))
# Example 1 at 4.5 us: the cut crosses only the backward segment, yet the forward burst fills the line
z, V, I = s1[4.5]
rep("D3 Example 1, t = 4.5 us: forward segment 0 (0-3 us) not crossed but V != 0 for z < 450 m",
    np.max(abs(V[z < 440])) > 0.4)

# ================================================================================================ E. worked problem
print("\nE. Worked problem: Z0 = 50, v = 200 m/us, l = 600 m, Rg = 25, RL = 150, f_i = 3t on (0,1)")
tg, Gg, GL = coeffs(50.0, 25.0, 150.0)
rep("E1 tau_g = 2/3, Gamma_g = -1/3, Gamma_L = 1/2, T = 3 us, pulse 200 m",
    close([tg, Gg, GL, 600 / 200, 200 * 1.0], [2 / 3, -1 / 3, 1 / 2, 3, 200]))
rep("E1 segment weights 2/3, 1/3, -1/9; launched peak 2 V", close([tg, tg * GL, tg * GL * Gg, tg * 3], [2 / 3, 1 / 3, -1 / 9, 2]))
v5 = 200.0
stE = (2.0, 3.5, 5.0)
sE, pE = moc(50.0, v5, 600.0, 25.0, 150.0, f_ramp, 0.0, 13.0, 0.25, snap_t=stE, probe_z=(0.0, 600.0))
z, V, I = sE[2.0]
inn = (z > 200.5) & (z < 399.5); out = (z < 199.5) | (z > 400.5)
rep("E2 t = 2: V = 4 - z/100 on 200-400 m, 0 elsewhere", close(V[inn], 4 - z[inn] / 100) and np.max(abs(V[out])) < 1e-12)
rep("E2 t = 2: I = V/50, 40 mA peak at z -> 200+", close(I[inn], V[inn] / 50) and abs(at(z, I, 200.25) * 1e3 - 40) < 0.1)
z, V, I = sE[5.0]
rep("E3 t = 5: V = z/200 - 1 on 200-400 m, 0 elsewhere", close(V[inn], z[inn] / 200 - 1) and np.max(abs(V[out])) < 1e-12)
rep("E3 t = 5: I = -V/50, down to -20 mA at z -> 400-", close(I[inn], -V[inn] / 50) and abs(at(z, I, 399.75) * 1e3 + 20) < 0.1)
z, V, I = sE[3.5]
inn = (z > 500.5) & (z < 600.0)
rep("E4 t = 3.5: V = 4.5 - z/200 on 500-600 m", close(V[inn], 4.5 - z[inn] / 200))
rep("E4 t = 3.5: I = (9.5 - 0.015 z)/50 A on 500-600 m", close(I[inn], (9.5 - 0.015 * z[inn]) / 50))
rep("E4 zero for z < 500 m", np.max(abs(V[z < 499.5])) < 1e-12)
rep("E4 endpoints: V 2 -> 1.5 V, I 40 -> 10 mA", close([at(z, V, 500.25), V[-1], at(z, I, 500.25) * 1e3, I[-1] * 1e3],
                                                     [2 - 0.25 / 200, 1.5, 40 - 0.015 * 0.25 / 50 * 1e3, 10], 1e-6))
rep("E4 load check V/I = 150 ohm, V+(l) = 1 V", close([V[-1] / I[-1], 7 - 600 / 100], [150, 1], 1e-9))
tp, V0, I0 = pE[0.0]
seg = [(0.05, 0.95, lambda t: 2 * t, lambda t: 40e-3 * t),
       (1.05, 5.95, lambda t: 0 * t, lambda t: 0 * t),
       (6.05, 6.95, lambda t: (2 / 3) * (t - 6), lambda t: -(4 / 3) * (t - 6) / 50),
       (7.05, 11.95, lambda t: 0 * t, lambda t: 0 * t)]
okd = True
for a_, b_, fV, fI in seg:
    m = (tp > a_) & (tp < b_)
    okd &= close(V0[m], fV(tp[m]), 1e-9) and close(I0[m], fI(tp[m]), 1e-9)
rep("E5 V(0,t), I(0,t) on 0-1, 1-6, 6-7, 7-12 us as on the page", okd)
rep("E5 -26.7 mA/us slope: (4/3)/50 = 26.67 mA", close(round(4 / 3 / 50 * 1e3, 1), 26.7))
m = (tp > 12.05) & (tp < 12.95)
rep("E5 next echo returns at 12 us (V(0,t) != 0 just after 12)", np.max(abs(V0[m])) > 0.05,
    f"V(0,12.5) = {np.interp(12.5, tp, V0):.4f} V")
m = (tp > 1.0) & (tp < 12.9)
rep("E6 KVL for t > 1: V(0) = -Rg I(0); at t -> 7-: V -> 0.667 V, I -> -26.7 mA", close(V0[m], -25 * I0[m], 1e-9) and
    abs(np.interp(6.995, tp, V0) - (2 / 3) * 0.995) < 1e-9 and abs(np.interp(6.995, tp, I0) * 1e3 + 26.67 * 0.995) < 0.01)
# trap claims
z, V, I = sE[2.0]
rep("E7 t = 2: forward ramp falls toward +z (0 V start leads)", at(z, V, 250) > at(z, V, 350))
z, V, I = sE[5.0]
rep("E7 t = 5: echo V > 0, I < 0", at(z, V, 300) > 0 and at(z, I, 300) < 0)
# S = 1 with the half-cell source (Rg != 0) supports an odd-even mode after a jump; use S = 0.5
sEF, pEF = fdtd(50.0, v5, 600.0, 25.0, 150.0, f_ramp, 0.0, 8.0, 0.1, S=0.5, snap_t=stE, probe_z=(0.0,))
# dispersive ringing trails the 2 V jump at S < 1, so compare at mid-ramp points and at z = 0
pts = [(2.0, 300, 1.0), (2.0, 250, 1.5), (3.5, 550, 1.75), (3.5, 580, 1.6), (5.0, 300, 0.5), (5.0, 350, 0.75)]
eE = max(abs(at(sEF[ts][0], sEF[ts][1], zq) - val) for ts, zq, val in pts)
tpF, V0F, I0F = pEF[0.0]
eE0 = max(abs(np.interp(q, tpF, V0F) - val) for q, val in ((0.5, 1.0), (3.0, 0.0), (6.5, 1 / 3)))
rep("E8 FDTD (S = 0.5, dz = 0.1 m) agrees at mid-ramp points of (b), (c) and at z = 0 in (d)", eE < 2e-2 and eE0 < 2e-2,
    f"max err {eE:.1e}, {eE0:.1e}")

# ================================================================================================ F. figures
print("\nF. Figure data (figs_l29.series and legs) against the MoC")
sys.path.insert(0, "/home/claude/work")
sys.argv = [sys.argv[0], "/tmp/claude-0/-home-claude/770cd07e-d432-56ac-9487-eb6a1bddcb01/scratchpad/figs_tmp"]
import figs_l29 as F  # noqa: E402
eF1 = 0
for ts in (1.0, 2.0, 4.5):
    z, V, I = s1[ts]
    Vs, ZIs = F.series(z / c, ts, F.f_ex1, **F.EX1)
    eF1 = max(eF1, np.max(abs(Vs - V)))
rep("F1 bex-example1 snapshot curves = MoC", eF1 < 1e-9, f"{eF1:.1e}")
tp, V12, I12 = p2[1200.0]
m = tp < 60
Vs, ZIs = F.series(1200 / c, tp[m], F.f_step, **F.EX2)
ok = np.ones(m.sum(), bool)
for ct_ in np.arange(4, 61, 8.0):
    ok &= abs(tp[m] - ct_) > 0.01
rep("F2 bex-example2 V and Z0 I curves = MoC", close(Vs[ok], V12[m][ok]) and close(ZIs[ok], 50 * I12[m][ok]))
rep("F2 right-axis labels: Z0 I = 1 V <-> 20 mA", close(1 / 50 * 1e3, 20))
e3 = 0
for ts in (3.0, 9.0, 11.0):
    z, V, I = s3[ts]
    Vs, ZIs = F.series(z / c, ts, F.f_ex3, **F.EX2)
    ok = np.ones_like(z, bool)
    for edge in (450, 750, 1050, 1350, 1650, 1950, 2250):
        ok &= abs(z - edge) > 1.5
    e3 = max(e3, np.max(abs(Vs - V)[ok]), np.max(abs(ZIs - 50 * I)[ok]))
rep("F3 bex-example3 curves = MoC", e3 < 1e-9, f"{e3:.1e}")
e4 = 0
for ts in stE:
    z, V, I = sE[ts]
    Vs, ZIs = F.series(z / v5, ts, F.f_ramp, **F.PRB)
    ok = np.ones_like(z, bool)
    for edge in (200, 400, 500, 600):
        ok &= abs(z - edge) > 0.6
    e4 = max(e4, np.max(abs(Vs - V)[ok]), np.max(abs(ZIs - 50 * I)[ok]))
rep("F4 bex-ramp-problem curves = MoC", e4 < 1e-9, f"{e4:.1e}")
lw = [round(w, 9) for *_, w in F.legs(**F.EX2, tmax=56.0)]
rep("F5 Example 2 diagram weights 1, 1/3, -1/3, -1/9, 1/9, 1/27, -1/27",
    close(lw, [1, 1 / 3, -1 / 3, -1 / 9, 1 / 9, 1 / 27, -1 / 27]))
lw = [w for *_, w in F.legs(**F.EX1, tmax=7.0)]
rep("F5 Example 1 diagram weights 1/2, 1/6 and nothing after 6 us", close(lw, [0.5, 1 / 6]))
lw = [w for *_, w in F.legs(**F.PRB, tmax=8.0)]
rep("F5 worked-problem diagram weights 2/3, 1/3, -1/9", close(lw, [2 / 3, 1 / 3, -1 / 9]))

print("=" * 60)
print(f"{len(OUT) - NFAIL} PASS, {NFAIL} FAIL")
with open("/home/claude/work/digest10/review_L29.out", "w") as fh:
    fh.write("\n".join(OUT) + f"\n{len(OUT) - NFAIL} PASS, {NFAIL} FAIL\n")
