#!/usr/bin/env python3
"""Lossless transmission-line transient simulator (method of characteristics), numpy only.

Independent of the bounce-diagram algebra: no reflection or transmission coefficient is used.
Each section carries a forward and a backward wave sample per cell; at every node the voltage
follows from Kirchhoff's current law with each incoming wave replaced by its Thevenin
equivalent (open-circuit voltage 2*wave behind the line's Z0).  Exact for inputs sampled at dt.

simulate(sections, Rg, RL, vs, t_end, dt, shunt=None)
  sections : list of (Z0 [ohm], one-way delay T [s])      (delays must be multiples of dt)
  Rg, RL   : source and load resistances (0 = ideal source / short, np.inf = open)
  vs       : function t -> source voltage
  shunt    : optional dict {junction index j: R} of resistors across the junction between
             sections j and j+1
returns dict with t, Vnode[k] (node voltages: 0 = generator end, last = load end), Inode[k]
(current toward +z at node k, taken on the line just to the right of the node; for the last
node, just to its left) and a probe(sec, frac) function giving (V(t), I(t)) inside a section.
"""
import numpy as np

def simulate(sections, Rg, RL, vs, t_end, dt, shunt=None):
    shunt = shunt or {}
    n = [int(round(T / dt)) for (_, T) in sections]
    for (Z, T), k in zip(sections, n):
        assert abs(k * dt - T) < 1e-9 * max(T, dt), "delay not a multiple of dt"
    Z = [s[0] for s in sections]
    S = len(sections)
    f = [np.zeros(k) for k in n]
    b = [np.zeros(k) for k in n]
    steps = int(round(t_end / dt))
    t = np.arange(steps) * dt
    Vn = np.zeros((S + 1, steps)); In = np.zeros((S + 1, steps))
    F = [np.zeros((steps, k)) for k in n]; B = [np.zeros((steps, k)) for k in n]
    for m in range(steps):
        a_in = [f[i][-1] for i in range(S)]      # forward waves arriving at right ends
        b_in = [b[i][0] for i in range(S)]       # backward waves arriving at left ends
        v = vs(t[m])
        # generator node
        if Rg == 0:
            V0 = v
        else:
            V0 = (v / Rg + 2 * b_in[0] / Z[0]) / (1 / Rg + 1 / Z[0])
        outf = [0.0] * S; outb = [0.0] * S
        outf[0] = V0 - b_in[0]
        Vn[0, m] = V0; In[0, m] = (outf[0] - b_in[0]) / Z[0]
        # junctions
        for j in range(S - 1):
            g = 1 / Z[j] + 1 / Z[j + 1] + (1 / shunt[j] if j in shunt else 0.0)
            V = (2 * a_in[j] / Z[j] + 2 * b_in[j + 1] / Z[j + 1]) / g
            outb[j] = V - a_in[j]; outf[j + 1] = V - b_in[j + 1]
            Vn[j + 1, m] = V; In[j + 1, m] = (outf[j + 1] - b_in[j + 1]) / Z[j + 1]
        # load node
        a = a_in[-1]
        if RL == 0:
            VL = 0.0
        elif np.isinf(RL):
            VL = 2 * a
        else:
            VL = (2 * a / Z[-1]) / (1 / Z[-1] + 1 / RL)
        outb[-1] = VL - a
        Vn[S, m] = VL; In[S, m] = (a - outb[-1]) / Z[-1]
        for i in range(S):
            F[i][m] = f[i]; B[i][m] = b[i]
            f[i] = np.concatenate(([outf[i]], f[i][:-1]))
            b[i] = np.concatenate((b[i][1:], [outb[i]]))
    def probe(sec, frac):
        k = min(n[sec] - 1, int(frac * n[sec]))
        return F[sec][:, k] + B[sec][:, k], (F[sec][:, k] - B[sec][:, k]) / Z[sec]
    def snapshot(sec, time):
        m = int(round(time / dt))
        zfrac = (np.arange(n[sec]) + 0.5) / n[sec]
        return zfrac, F[sec][m] + B[sec][m], (F[sec][m] - B[sec][m]) / Z[sec]
    return dict(t=t, Vnode=Vn, Inode=In, probe=probe, snapshot=snapshot)

def at(t, y, time):
    """value of the sampled waveform y(t) at 'time' (nearest sample)"""
    return y[int(np.argmin(np.abs(t - time)))]

if __name__ == "__main__":
    # self-test: matched source and load, 1 V step -> 0.5 V everywhere after the front
    r = simulate([(50.0, 1e-6)], 50.0, 50.0, lambda t: 1.0, 5e-6, 1e-8)
    ok = abs(r["Vnode"][0, -1] - 0.5) < 1e-12 and abs(r["Vnode"][1, -1] - 0.5) < 1e-12
    # open line with ideal source: load doubles, never settles
    r = simulate([(50.0, 1e-6)], 25.0, np.inf, lambda t: 1.0, 40e-6, 1e-8)
    ok = ok and abs(r["Vnode"][1, -1] - 1.0) < 1e-3
    print("PASS" if ok else "FAIL", "tlsim self-test")
