#!/usr/bin/env python3
"""R31 -- independent re-solution of practice/31-resonances-of-line-segments.md.
No lambda/2 or lambda/4 rule is used: resonant frequencies and mode shapes are the eigenvalues and
eigenvectors of the discretized telegrapher's equations (V'' = -(w/v)^2 V with V = 0 at a short and
dV/dz = 0 at an open end); time-domain parts use a leapfrog (FDTD) integration at Courant number 1."""
import numpy as np
pi = np.pi; NF = [0, 0]
def chk(name, got, want, tol=2e-3, atol=1e-6):
    ok = np.allclose(np.asarray(got, float), np.asarray(want, float), rtol=tol, atol=atol); NF[0 if ok else 1] += 1
    print(("PASS " if ok else "FAIL ") + f"{name}: computed {np.round(np.asarray(got, float), 4)}, page {want}")
def modes(l, v, left, right, k=4, N=900):
    """lowest k non-zero resonances [Hz] and voltage mode shapes; left/right in {'open','short'}"""
    h = l / N; A = np.zeros((N + 1, N + 1))
    for i in range(N + 1):
        A[i, i] = 2
        if i > 0: A[i, i - 1] = -1
        if i < N: A[i, i + 1] = -1
    if left == "open": A[0, 1] = -2              # mirror node: dV/dz = 0
    if right == "open": A[N, N - 1] = -2
    idx = list(range(N + 1))
    if left == "short": idx.remove(0)
    if right == "short": idx.remove(N)
    w2, vec = np.linalg.eig(A[np.ix_(idx, idx)] / h ** 2)
    w2 = np.real(w2); order = np.argsort(w2); w2 = w2[order]; vec = np.real(vec[:, order])
    keep = w2 > 1e-8 * w2[-1]            # drops only the DC solution of an open-open line
    f = v * np.sqrt(w2[keep][:k]) / (2 * pi)
    shapes = []
    for m in np.where(keep)[0][:k]:
        full = np.zeros(N + 1); full[idx] = vec[:, m]; shapes.append(full / np.abs(full).max())
    return f, shapes, np.linspace(0, l, N + 1)
def nulls(y, z):
    s = np.where(np.sign(y[:-1]) * np.sign(y[1:]) < 0)[0]
    out = [z[i] - y[i] * (z[i + 1] - z[i]) / (y[i + 1] - y[i]) for i in s]
    if abs(y[0]) < 1e-9: out = [z[0]] + out
    if abs(y[-1]) < 1e-9: out = out + [z[-1]]
    return out
print("== 31.1"); f, _, _ = modes(45, 1.8e8, "open", "open", 3); chk("open-open [MHz]", f / 1e6, [2, 4, 6])
f, _, _ = modes(45, 1.8e8, "short", "short", 3); chk("short-short [MHz]", f / 1e6, [2, 4, 6])
f, _, _ = modes(45, 1.8e8, "open", "short", 3); chk("open-short [MHz]", f / 1e6, [1, 3, 5])
print("== 31.2"); f, sh, z = modes(10, 1e8, "open", "open", 2); chk("(b) |V| at the midpoint for n = 1, 2", [abs(sh[0][450]), abs(sh[1][450])], [0, 1])
print("== 31.3"); f, _, _ = modes(12, 2.4e8, "short", "open", 3); chk("short-open 12 m [MHz]", f / 1e6, [5, 15, 25])
print("== 31.4"); f, sh, z = modes(90, 3e8, "open", "open", 3); chk("f3 [MHz]", f[2] / 1e6, 5); chk("voltage nulls [m]", nulls(sh[2], z), [15, 45, 75])
dV = np.gradient(sh[2], z); chk("current nulls [m] (zeros of dV/dz, interior) plus the two open ends", [0] + [x for x in nulls(dV, z) if 1 < x < 89] + [90], [0, 30, 60, 90])
chk("peak current [A] = peak |dV/dz| v/(w Z0) with 12 V peak", 12 * np.abs(dV).max() * 3e8 / (2 * pi * f[2]) / 75, 0.16)
print("== 31.5"); f, sh, z = modes(150, 3e8, "short", "open", 3); chk("f_n [MHz]", f / 1e6, [0.5, 1.5, 2.5])
# leapfrog from V(z,0) = 20 sin(pi z/100), I(z, -dt/2) ~ 0 (I is odd in t): short at z=0, open at z=l
N = 3000; l = 150.0; v = 3e8; Z0 = 100.0; dz = l / N; dt = dz / v
zk = np.arange(N + 1) * dz; zh = (np.arange(N) + 0.5) * dz
V = 20 * np.sin(pi * zk / 100); w = 3 * pi * 1e6
I = -0.2 * np.cos(pi * zh / 100) * np.sin(w * (-dt / 2)) * 0 + (-(1 / Z0) * (V[1:] - V[:-1])) * 0.5   # half step from I(0) = 0
tgt = 0.2e-6; steps = int(round(tgt / dt))
for m in range(steps):
    if m > 0: I = I - (1 / Z0) * (V[1:] - V[:-1])
    V[1:-1] = V[1:-1] - Z0 * (I[1:] - I[:-1]); V[0] = 0.0; V[-1] = V[-1] + 2 * Z0 * I[-1]
t = steps * dt; k = 1000                                  # z = 50 m
chk("(b) V(50 m, 0.2 us) [V] vs 20 sin(pi/2) cos(0.6 pi)", V[k], 20 * np.cos(0.6 * pi), tol=5e-3)
Ihalf = I[k]; tI = t - dt / 2
chk("    I(50.025 m, t - dt/2) [A] vs -0.2 cos(pi z/100) sin(3 pi t): sign and size", Ihalf, -0.2 * np.cos(pi * zh[k] / 100) * np.sin(w * tI), tol=5e-3)
chk("    I at 10 m [A] (cos = 0.951): negative at 0.2 us", I[200], -0.2 * np.cos(pi * zh[200] / 100) * np.sin(w * tI), tol=5e-3)
print("== 31.6"); f, _, _ = modes(20, 2e8, "open", "short", 2); chk("with v = 2e8: unlike ends give [MHz]", f / 1e6, [2.5, 7.5])
f, _, _ = modes(20, 2e8, "short", "short", 3); chk("like ends [MHz]", f / 1e6, [5, 10, 15]); chk("eps_r", (3e8 / 2e8) ** 2, 2.25)
print("== 31.7 (z from the input: short at z=0, open at z=l; d = l - z)")
f, sh, z = modes(50, 2.5e8, "short", "open", 3); chk("omega / (pi 1e6) [rad/s]", 2 * f / 1e6, [2.5, 7.5, 12.5])
d_v = sorted(50 - np.array(nulls(sh[1], z))); chk("second mode: voltage nulls d [m]", d_v, [16.667, 50])
dV = np.gradient(sh[1], z); d_i = sorted([50 - x for x in nulls(dV, z) if 0.5 < x < 49.5] + [0.0]); chk("second mode: current nulls d [m] (load included)", d_i, [0, 33.333])
f, _, _ = modes(50, 2.5e8, "short", "short", 1); chk("(e) both ends shorted, lowest [MHz]", f / 1e6, [2.5])
print("== 31.8 leapfrog: open at z = 0, short at z = 900 m, pulse 5 V / 0.1 A on 0..600 m at t = 2 us")
N = 900; Z0 = 50.0; c = 3e8; dz = 1.0; dt = dz / c
V = np.zeros(N + 1); I = np.zeros(N); V[1:601] = 5.0; I[1:601] = 0.1   # state (V^n, I^{n+1/2}) of a forward pulse; the open end node is already at 0
rec = {}
for m in range(int(round(12.2e-6 / dt)) + 1):
    t = 2e-6 + m * dt
    rec[round(t * 1e6, 4)] = (V[450], 0.5 * (I[449] + I[450]), V.copy(), I.copy())
    V[1:-1] = V[1:-1] - Z0 * (I[1:] - I[:-1]); V[0] = V[0] - 2 * Z0 * I[0]; V[-1] = 0.0
    I = I - (1 / Z0) * (V[1:] - V[:-1])
g = lambda t: rec[round(t, 4)]
vals = np.array([g(t)[:2] for t in (3, 4, 5.5, 7, 8.5, 10, 11.5, 13, 13.8)]).ravel()
chk("(c) (V, I) at 450 m at t = 3, 4, 5.5, 7, 8.5, 10, 11.5, 13, 13.8 us", vals, [5, .1, 0, 0, -5, .1, 0, 0, -5, -.1, 0, 0, 5, -.1, 0, 0, 5, .1], atol=2e-3)
V4, I4 = g(4.0)[2], g(4.0)[3]; L_ = Z0 / c; C_ = 1 / (Z0 * c)
chk("(d) at 4 us: electric, magnetic energy [uJ]; V, I at z = 750 m", [0.5 * C_ * np.sum(V4 ** 2) * 1e6, 0.5 * L_ * np.sum(I4 ** 2) * 1e6, V4[750], I4[750]], [0, 1, 0, 0.2], tol=5e-3, atol=5e-3)
chk("    period: state at 14 us equals state at 2 us (max |dV|)", np.abs(g(14.0)[2] - g(2.0)[2]).max(), 0, atol=1e-6)
print(f"\nSUMMARY: {NF[0]} PASS, {NF[1]} FAIL")
