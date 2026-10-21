#!/usr/bin/env python3
"""Two independent time-steppers for a lossless line with resistive ends (used by verify_L29.py).

Neither uses reflection or injection coefficients or bounce diagrams: the ends are solved from KVL/Ohm's law.
Units: microseconds, metres, volts, ohms, amperes; v in m/us.

moc():  method of characteristics on the "magic" grid v dt = dz. The invariants A = V + Z0 I and B = V - Z0 I
        move one cell per step to the right and to the left (d'Alembert); at z = 0 the source equation
        V = f_i - R_g I and at z = l the load equation V = R_L I close the system. Exact at the grid points.
fdtd(): Yee leapfrog of the telegrapher's equations dV/dz = -L' dI/dt, dI/dz = -C' dV/dt at Courant number S < 1,
        with C. R. Paul's half-cell lumped terminations. Second-order accurate; small ringing behind sharp edges.
"""
import numpy as np


def moc(Z0, v, l, Rg, RL, fi, tmax, N, t0=0.0):
    """Return (z, t, V[t, z], I[t, z]) on the grid z_k = k l/N, t_n = t0 + n dz/v. Line at rest at t0."""
    dz = l / N
    dt = dz / v
    nst = int(round((tmax - t0) / dt))
    z = np.arange(N + 1) * dz
    t = t0 + np.arange(nst + 1) * dt
    A = np.zeros(N + 1)
    B = np.zeros(N + 1)
    VV = np.zeros((nst + 1, N + 1))
    II = np.zeros((nst + 1, N + 1))
    for n in range(nst + 1):
        if n > 0:
            A[1:] = A[:-1].copy()
            B[:-1] = B[1:].copy()
        # z = 0: V - Z0 I = B0 (arriving), V = f_i - Rg I
        I0 = (fi(t[n]) - B[0]) / (Rg + Z0)
        V0 = B[0] + Z0 * I0
        A[0] = V0 + Z0 * I0
        # z = l: V + Z0 I = A_N (arriving), V = RL I
        if RL == np.inf:
            IN = 0.0
            VN = A[N]
        else:
            IN = A[N] / (RL + Z0)
            VN = RL * IN
        B[N] = VN - Z0 * IN
        VV[n] = 0.5 * (A + B)
        II[n] = 0.5 * (A - B) / Z0
    return z, t, VV, II


def fdtd(Z0, v, l, Rg, RL, fi, tmax, N, S=0.5, snaps=(), probes=(), t0=0.0):
    """Leapfrog FDTD. Returns {'snap': {t: (z, V, I)}, 't': times, 'V': {z: series}, 'I': {z: series}}.
    I is averaged to the V nodes and to integer time steps."""
    dz = l / N
    dt = S * dz / v
    Lp, Cp = Z0 / v, 1.0 / (Z0 * v)
    cv, ci = dt / (Cp * dz), dt / (Lp * dz)
    a = Cp * dz / (2 * dt)
    gL = 0.0 if RL == np.inf else 1.0 / RL
    V = np.zeros(N + 1)
    I = np.zeros(N)
    nst = int(round((tmax - t0) / dt))
    snap_n = {int(round((ts - t0) / dt)): ts for ts in snaps}
    pk = {p: int(round(p / dz)) for p in probes}
    ts_out = t0 + np.arange(nst) * dt
    oV = {p: np.zeros(nst) for p in probes}
    oI = {p: np.zeros(nst) for p in probes}
    shots = {}
    for n in range(nst):
        Iold = I.copy()                      # I^{n-1/2}
        I = I - ci * (V[1:] - V[:-1])        # I^{n+1/2} from V^n
        # record time n: V^n and the average of I^{n-1/2}, I^{n+1/2}
        Im = 0.5 * (Iold + I)
        In = np.empty(N + 1)
        In[1:N] = 0.5 * (Im[:-1] + Im[1:])
        In[0], In[N] = Im[0], Im[-1]
        for p, k in pk.items():
            oV[p][n] = V[k]
            oI[p][n] = In[k]
        if n in snap_n:
            shots[snap_n[n]] = (np.arange(N + 1) * dz, V.copy(), In.copy())
        Vn = V.copy()
        V[1:N] = Vn[1:N] - cv * (I[1:] - I[:-1])
        th = t0 + (n + 0.5) * dt
        if Rg == 0:
            V[0] = fi(t0 + (n + 1) * dt)
        else:
            gR = 1.0 / Rg
            V[0] = (Vn[0] * (a - gR / 2) + gR * fi(th) - I[0]) / (a + gR / 2)
        V[N] = (Vn[N] * (a - gL / 2) + I[N - 1]) / (a + gL / 2)
    return {"t": ts_out, "V": oV, "I": oI, "snap": shots, "dt": dt, "dz": dz}


if __name__ == "__main__":
    z, t, VV, II = moc(50, 300, 900, 50, 50, lambda s: 1.0 * (s >= 0), 6, 900)
    print(VV[300, ::100], II[300, ::100] * 50)
