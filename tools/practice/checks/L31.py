#!/usr/bin/env python3
"""Author's checks for practice/31-resonances-of-line-segments.md: every number in the answers."""
import numpy as np
pi = np.pi; n = dict(p=0, f=0)
def chk(label, mine, want, tol=1e-6, atol=1e-9):
    ok = np.allclose(np.asarray(mine, float), np.asarray(want, float), rtol=tol, atol=atol)
    n["p" if ok else "f"] += 1; print(("PASS " if ok else "FAIL ") + f"{label}: {np.round(np.asarray(mine, float), 5)}")
like = lambda v, l, k: [m * v / (2 * l) for m in range(1, k + 1)]
unlike = lambda v, l, k: [(2 * m + 1) * v / (4 * l) for m in range(k)]
print("== 31.1"); chk("like ends [MHz]", np.array(like(1.8e8, 45, 3)) / 1e6, [2, 4, 6]); chk("unlike ends [MHz]", np.array(unlike(1.8e8, 45, 3)) / 1e6, [1, 3, 5])
print("== 31.2"); chk("(b) cos(n pi/2) for n = 1, 2: zero only for odd n", [np.cos(pi / 2), np.cos(pi)], [0, -1])
print("== 31.3"); chk("unlike ends 12 m, 2.4e8 [MHz]; the student's like-end values", np.array(unlike(2.4e8, 12, 3) + like(2.4e8, 12, 3)) / 1e6, [5, 15, 25, 10, 20, 30])
print("== 31.4"); v, l, Z0 = 3e8, 90.0, 75.0
chk("f3 [MHz], lambda [m]", [3 * v / (2 * l) / 1e6, 2 * l / 3], [5, 60])
z = np.linspace(0, l, 9001); I = np.sin(3 * pi * z / l); V = np.cos(3 * pi * z / l)
chk("current nulls [m]", z[np.abs(I) < 1e-9], [0, 30, 60, 90]); chk("voltage nulls [m]", z[np.abs(V) < 1e-9], [15, 45, 75]); chk("peak current [A]", 12 / Z0, 0.16)
print("== 31.5"); v, l, Z0 = 3e8, 150.0, 100.0
chk("f_n [MHz]", np.array(unlike(v, l, 3)) / 1e6, [0.5, 1.5, 2.5])
w = 2 * pi * 1.5e6; b = w / v; chk("omega [rad/us]/pi, beta*100/pi, lambda [m], l/lambda", [w / 1e6 / pi, b * 100 / pi, 2 * pi / b, l * b / (2 * pi)], [3, 1, 200, 0.75])
L_ = Z0 / v; C_ = 1 / (Z0 * v)
Vf = lambda z, t: 20 * np.sin(b * z) * np.cos(w * t); If = lambda z, t: -0.2 * np.cos(b * z) * np.sin(w * t)
z0, t0, hz, ht = 37.0, 2.3e-7, 1e-4, 1e-12
r1 = (Vf(z0 + hz, t0) - Vf(z0 - hz, t0)) / (2 * hz) + L_ * (If(z0, t0 + ht) - If(z0, t0 - ht)) / (2 * ht)
r2 = (If(z0 + hz, t0) - If(z0 - hz, t0)) / (2 * hz) + C_ * (Vf(z0, t0 + ht) - Vf(z0, t0 - ht)) / (2 * ht)
chk("telegrapher residuals (scaled), V(0), I(l)", [r1 / (20 * b), r2 / (0.2 * b), Vf(0, t0), If(l, t0)], [0, 0, 0, 0], atol=1e-6)
chk("V = 0 everywhere at t = 1/6 us and 1/2 us; |sin| there", [np.cos(3 * pi / 6), np.cos(3 * pi / 2), abs(np.sin(3 * pi / 6))], [0, 0, 1])
print("== 31.6"); chk("ratio; v = 4 l f0; eps_r; like ends [MHz]", [7.5 / 2.5, 4 * 20 * 2.5e6, (3e8 / 2e8) ** 2] + list(np.array(like(2e8, 20, 3)) / 1e6), [3, 2e8, 2.25, 5, 10, 15])
print("== 31.7"); v, l = 2.5e8, 50.0
f = np.array(unlike(v, l, 3)); chk("f_n [MHz]; omega/(pi 1e6)", list(f / 1e6) + list(2 * f / 1e6), [1.25, 3.75, 6.25, 2.5, 7.5, 12.5])
lam = v / f[1]; chk("lambda [m], l/lambda, V nulls d [m], I nulls d [m], like-end lowest [MHz]", [lam, l / lam, lam / 4, 3 * lam / 4, 0, lam / 2, v / (2 * l) / 1e6], [66.6667, 0.75, 16.6667, 50, 0, 33.3333, 2.5], tol=1e-5)
print("== 31.8 (characteristics: two travelling-wave arrays, open at z=0, short at z=l)")
N = 900; c = 3e8; dt = 1.0 / c; Z0 = 50.0
fw = np.zeros(N); bw = np.zeros(N); fw[:600] = 5.0
chk("(a) I in the pulse [A]; pulse length [m]", [5 / Z0, 2e-6 * c], [0.1, 600])
rec = {}
for m in range(int(round(12.5e-6 / dt)) + 1):
    t = 2e-6 + m * dt
    rec[round(t * 1e6, 4)] = (fw[449] + bw[449], (fw[449] - bw[449]) / Z0, fw + bw, (fw - bw) / Z0)
    fo, bo = fw[-1], bw[0]
    fw = np.concatenate(([bo], fw[:-1])); bw = np.concatenate((bw[1:], [-fo]))    # open: +1, short: -1
g = lambda t: rec[round(t, 4)][:2]
chk("(b) period 4l/v [us], fundamental [kHz]", [4 * 900 / 300, 1e3 / 12], [12, 83.3333], tol=1e-5)
chk("(c) (V, I) at 450 m at t = 3, 4, 5.5, 7, 8.5, 10, 11.5, 13, 13.8 us",
    np.array([g(t) for t in (3, 4, 5.5, 7, 8.5, 10, 11.5, 13, 13.8)]).ravel(), [5, .1, 0, 0, -5, .1, 0, 0, -5, -.1, 0, 0, 5, -.1, 0, 0, 5, .1])
chk("    window edges: just inside 3.4, 4.6, 6.4, 7.6, 9.4, 10.6, 12.4, 13.6; just outside 3.6, 4.4",
    [g(t)[0] for t in (3.4, 4.6, 6.4, 7.6, 9.4, 10.6, 12.4, 13.6, 3.6, 4.4)], [5, -5, -5, -5, -5, 5, 5, 5, 0, 0])
L_ = Z0 / c; C_ = 1 / (Z0 * c); V4, I4 = rec[4.0][2], rec[4.0][3]
chk("(d) energy delivered [uJ]; at 4 us: electric, magnetic [uJ]; V and I on 600-900 m; outside",
    [5 * 0.1 * 2e-6 * 1e6, 0.5 * C_ * np.sum(V4 ** 2) * 1e6, 0.5 * L_ * np.sum(I4 ** 2) * 1e6, V4[700], I4[700], abs(V4[:600]).max() + abs(I4[:600]).max(), L_ * 1e6],
    [1, 0, 1, 0, 0.2, 0, 0.166667], tol=1e-5)
chk("    check: V(t + 6 us) = -V(t) at 450 m (t = 3, 5.5)", [g(9)[0] + g(3)[0], g(11.5)[0] + g(5.5)[0]], [0, 0])
print(f"\nSUMMARY: {n['p']} PASS, {n['f']} FAIL")
