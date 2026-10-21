"""Independent check of practice/28-bounce-diagrams.md.

Time-domain simulator: lossless line as N-cell delay lines (method of
characteristics, Courant 1, exact).  Interior: V = F + B, I = (F - B)/Z0.
Each end is solved from KVL / Ohm as a 3x3 linear system (no Gamma formulas):
  generator: V + Rg I = fi,  V = a + b,  Z0 I = a - b   (unknowns V, I, a)
  load:      V - RL I = 0 (or I = 0 open, V = 0 short), same wave relations.
"""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

FAILS = []


def chk(name, got, want, tol=1e-6):
    ok = np.allclose(np.atleast_1d(got), np.atleast_1d(want), rtol=tol, atol=tol)
    print(f"{'PASS' if ok else 'FAIL'}  {name}: sim={np.round(np.atleast_1d(got), 6).tolist()} page={np.atleast_1d(want).tolist()}")
    if not ok:
        FAILS.append(name)


def sim(Z0, Rg, RL, N, fi):
    """fi: source samples at t_n = n dt (dt = T/N). Returns V, I, F, B [n, k]."""
    ns = len(fi)
    F = np.zeros(N + 1); B = np.zeros(N + 1)
    Vh = np.zeros((ns, N + 1)); Ih = np.zeros_like(Vh)
    Fh = np.zeros_like(Vh); Bh = np.zeros_like(Vh)
    for n in range(ns):
        if n > 0:
            F[1:] = F[:-1].copy(); B[:-1] = B[1:].copy()
        # generator end: x = [V, I, a], b = B[0] known
        b = B[0]
        A = np.array([[1, Rg, 0], [1, 0, -1], [0, Z0, -1.0]])
        V0, I0, a = np.linalg.solve(A, [fi[n], b, -b])
        F[0] = a
        # load end: x = [V, I, b], a = F[N] known
        a = F[N]
        if RL == np.inf:
            row = [0, 1, 0]
        elif RL == 0:
            row = [1, 0, 0]
        else:
            row = [1, -RL, 0]
        A = np.array([row, [1, 0, -1], [0, Z0, 1.0]], float)
        VL, IL, bb = np.linalg.solve(A, [0, a, a])
        B[N] = bb
        Fh[n] = F; Bh[n] = B
        Vh[n] = F + B; Ih[n] = (F - B) / Z0
        # sanity: end KVL
        assert abs(Vh[n, 0] + Rg * Ih[n, 0] - fi[n]) < 1e-9
    return Vh, Ih, Fh, Bh


def coeffs(Z0, Rg, RL, N=4):
    """Measure tau_g, Gamma_g, Gamma_L (voltage and current) from an impulse."""
    fi = np.zeros(2 * N + 1); fi[0] = 1.0
    V, I, F, B = sim(Z0, Rg, RL, N, fi)
    tau = F[0, 0]
    GL = B[N, N] / F[N, N]
    Gg = F[2 * N, 0] / B[2 * N, 0]
    GLi = (-B[N, N]) / F[N, N]
    Ggi = F[2 * N, 0] / (-B[2 * N, 0])
    return tau, Gg, GL, Ggi, GLi


def step(V0, ns):
    return np.full(ns, float(V0))


print("== 28.1 ==")
tau, Gg, GL, Ggi, GLi = coeffs(60, 20, 180)
chk("tau_g, Gamma_g, Gamma_L", [tau, Gg, GL], [3/4, -1/2, 1/2])
chk("current coeffs load, gen", [GLi, Ggi], [-1/2, 1/2])
V, I, F, B = sim(60, 20, 180, 10, step(16, 15))
chk("first wave V, I (t<2T)", [V[5, 0], I[5, 0]], [12, 0.2])

print("== 28.2 ==")
V, I, F, B = sim(50, 25, 200, 20, step(12, 100))
r = V[50, 5] / I[50, 5]
print(f"(a) V/I after echo at z=l/4, t=2.5T: {r:.3f} != 50  -> False", "PASS" if abs(r - 50) > 1 else "FAIL")
c1 = coeffs(50, 30, 150);
fi = np.zeros(9); fi[0] = 2.0
V, I, F, B = sim(50, 30, 150, 4, fi)
chk("(c) Gamma_g independent of amplitude", F[8, 0] / B[8, 0], c1[1])
rng = np.random.default_rng(1)
ok = True
for RL in [0, 7, 50, 333, np.inf]:
    fi = rng.normal(size=200)
    V, I, F, B = sim(50, 0, RL, 13, fi)
    ok &= np.allclose(V[:, 0], fi)
print("(d) Rg=0 -> V(0,t)=fi for all RL:", "PASS" if ok else "FAIL")
t, gg, *_ = coeffs(50, 150, 75)
chk("(e) Rg=3Z0: tau_g, 1+Gamma_g", [t, 1 + gg], [1/4, 3/2])

print("== 28.3 ==")
for RL, row in [(np.inf, [1, 6, 12, 0]), (0, [-1, -6, 0, 0.24]), (50, [0, 0, 6, 0.12]), (25, [-1/3, -2, 4, 0.16])]:
    V, I, F, B = sim(50, 50, RL, 10, step(12, 15))  # matched gen launches 6 V
    a = F[12, 10]; b = B[12, 10]
    chk(f"RL={RL}: Gamma_L, refl, V_L, I_L", [b / a, b, V[12, 10], I[12, 10]], row)

print("== 28.4 ==")
fi = np.zeros(300); fi[0] = 1
V, I, F, B = sim(50, 20, 120, 30, fi)  # dz = 10 m, dt = 0.05 us
dt = 1.5 / 30
times = np.nonzero(np.abs(V[:, 10]) > 1e-12)[0][:4] * dt
chk("arrival times at z=100 m", times, [0.5, 2.5, 3.5, 5.5])

print("== 28.5 ==")
tau, Gg, GL, *_ = coeffs(50, 75, 200)
chk("tau_g, Gamma_g, Gamma_L", [tau, Gg, GL], [0.4, 0.2, 0.6])
V, I, F, B = sim(50, 75, 200, 10, step(10, 2000))
chk("V(l) on T..3T, DC", [V[20, 10], V[-1, 10]], [6.4, 7.272727], 1e-5)

print("== 28.6 ==")  # T = 0.5 us, N = 20 -> dt = 0.025 us
tau, Gg, GL, *_ = coeffs(100, 0, 300)
chk("tau_g, Gamma_g, Gamma_L", [tau, Gg, GL], [1, -1, 0.5])
fi = np.zeros(80); fi[0] = 20
V, I, F, B = sim(100, 0, 300, 20, fi)
w = [F[0, 0], B[20, 20], F[40, 0], B[60, 20]]
chk("weights 1-4", w, [20, 10, -10, -5])
V, I, F, B = sim(100, 0, 300, 20, step(20, 4000))
dt = 0.025
idx = lambda t: int(round(t / dt))
chk("V(l,t) 0.25,1,2,3,4 us", [V[idx(t), 20] for t in [0.25, 1, 2, 3, 4]], [0, 30, 15, 22.5, 18.75])
chk("I(0,t) 0.5,1.5,2.5,3.5 us", [I[idx(t), 0] for t in [0.5, 1.5, 2.5, 3.5]], [0.2, 0, 0.1, 0.05])
chk("V(0,t) always 20", np.ptp(V[:, 0]) + 20, 20)
chk("DC V, I", [V[-1, 10], I[-1, 10]], [20, 0.0666667], 1e-5)

print("== 28.7 ==")  # v = 200 m/us; l = 240 m -> T = 1.2 us, N = 24 -> dt = 0.05
dt = 0.05
V, I, F, B = sim(50, 50, 100, 24, step(12, 200))
jump = np.nonzero(np.abs(np.diff(V[:, 0])) > 1e-9)[0] + 1
chk("record 6 then 8, jump at 2.4 us", [V[10, 0], V[150, 0], jump[0] * dt, len(jump)], [6, 8, 2.4, 1])
RLfit = brentq(lambda R: sim(50, 50, R, 4, step(12, 20))[0][-1, 0] - 8, 1, 1e4)
tau, Gg, GL, *_ = coeffs(50, 50, RLfit)
chk("R_L from record, Gamma_L", [RLfit, GL], [100, 1/3])
chk("length = v*jump/2", 200 * jump[0] * dt / 2, 240)
for RL, late in [(25, 4), (0, 0)]:
    V, I, F, B = sim(50, 50, RL, 24, step(12, 200))
    chk(f"(c) RL={RL}: early, late", [V[10, 0], V[150, 0]], [6, late])

print("== 28.8 ==")  # l = 400, v = 200 -> T = 2 us; N = 40 -> dz = 10 m, dt = 0.05
dt = 0.05
V, I, F, B = sim(50, 30, 0, 40, step(16, 20000))
for t, vals in [(3, [10, 0.2, 0, 0.4]), (5, [2.5, 0.45, 0, 0.4])]:
    n = int(round(t / dt))
    chk(f"t={t}: V,I z<200 (z=100); V,I z>200 (z=300)", [V[n, 10], I[n, 10], V[n, 30], I[n, 30]], vals)
    front = np.nonzero(np.abs(np.diff(V[n])) > 1e-9)[0]
    # front edge between nodes k, k+1; node 20 (200 m) is on it
    chk(f"t={t}: front at z = 200 m", 1.0 * (200 in (front[0] * 10, (front[0] + 1) * 10) and len(front) == 1), 1.0)
chk("DC V, I", [V[-1, 20], I[-1, 20]], [0, 0.533333], 1e-5)

print("== 28.9 ==")  # T = 0.2 m / (0.2 m/ns) = 1 ns; N = 40, dt = 0.025 ns
c = 0.299792458  # m/ns; page uses c = 0.3
v = 2 / 3 * 0.3
chk("T (ns)", 0.2 / v, 1)
tau, Gg, GL, Ggi, GLi = coeffs(50, 25, 200)
chk("tau_g, Gamma_g, Gamma_L", [tau, Gg, GL], [2/3, -1/3, 0.6])
chk("current coeffs load, gen", [GLi, Ggi], [-0.6, 1/3])
N = 40; dt = 1 / N
fi = np.zeros(6 * N); fi[0] = 12
V, I, F, B = sim(50, 25, 200, N, fi)
segV = [F[0, 0], B[N, N], F[2 * N, 0], B[3 * N, N], F[4 * N, 0]]
segI = [F[0, 0] / 50, -B[N, N] / 50, F[2 * N, 0] / 50, -B[3 * N, N] / 50, F[4 * N, 0] / 50]
chk("segment V weights", segV, [8, 4.8, -1.6, -0.96, 0.32])
chk("segment I weights", segI, [0.16, -0.096, -0.032, 0.0192, 0.0064])
V, I, F, B = sim(50, 25, 200, N, step(12, 4000))
mid = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5]
chk("V(0,t) table", [V[int(round(t / dt)), 0] for t in mid], [8, 8, 11.2, 11.2, 10.56, 10.56])
chk("V(l,t) table", [V[int(round(t / dt)), N] for t in mid], [0, 12.8, 12.8, 10.24, 10.24, 10.752])
chk("(d) V, I at z=5 cm, t=3.5 ns", [V[int(round(3.5 / dt)), 10], I[int(round(3.5 / dt)), 10]], [11.2, 0.032])
chk("(e) DC V_L, I_L", [V[-1, N], I[-1, N]], [10.666667, 0.0533333], 1e-5)
chk("check: I_L on 1-3 ns", I[int(round(2 / dt)), N], 0.064)

print("== 28.10 ==")  # T = 3 us; N = 30, dt = 0.1 us
N = 30; dt = 0.1
V, I, F, B = sim(50, 50, 150, N, step(200, 2000))
chk("(a) DC V(0), I(l)", [V[-1, 0], I[-1, N]], [150, 1])
chk("(a) V(0) settled from 6 us", np.ptp(V[60:, 0]), 0)
ns = 121
fi = np.where(np.arange(ns) * dt < 4 - 1e-9, 200.0, 0.0)
V, I, F, B = sim(50, 50, 150, N, fi)
g = lambda t, k: (V[int(round(t / dt)), k], I[int(round(t / dt)), k])
chk("(b) V(0), I(0) at 2,5,8,11 us", sum([list(g(t, 0)) for t in [2, 5, 8, 11]], []), [100, 2, 0, 0, 50, -1, 0, 0])
chk("(c) V, I at 300 m: 1,3,5,7,10 us", sum([list(g(t, 15)) for t in [1, 3, 5, 7, 10]], []),
    [0, 0, 100, 2, 150, 1, 50, -1, 0, 0])
Ein = np.sum(V[:, 0] * I[:, 0]) * dt
EL = np.sum(V[:, N] * I[:, N]) * dt
Es = np.sum(fi * I[:, 0]) * dt
ERg = np.sum(I[:, 0] ** 2 * 50) * dt
chk("(d) energy in at z=0, at load (uJ)", [Ein, EL], [600, 600])
chk("check: source, Rg (uJ)", [Es, ERg], [1600, 1000])

print("== 28.11 ==")  # v = 300/3 = 100 m/us, T = 3 us; N = 30, dz = 10 m, dt = 0.1 us
v = 300 / np.sqrt(9)
chk("v, T", [v, 300 / v], [100, 3])
tau, Gg, GL, *_ = coeffs(60, 20, 300)
chk("tau_g, Gamma_g, Gamma_L", [tau, Gg, GL], [3/4, -1/2, 2/3])
N = 30; dt = 0.1
fi = np.zeros(141); fi[0] = 12
V, I, F, B = sim(60, 20, 300, N, fi)
nz = np.nonzero(np.abs(V[:, 10]) > 1e-12)[0]
chk("(b) impulse times at 100 m", nz * dt, [1, 5, 7, 11, 13])
chk("(b) V weights (V us)", V[nz, 10], [9, 6, -3, -2, 1])
chk("(c) I weights (A us)", I[nz, 10], [0.15, -0.1, -0.05, 0.0333333, 0.0166667], 1e-5)
V, I, F, B = sim(60, 20, 300, N, step(12, 5000))
chk("(d) step V at 0.5,3,6,9,12,13.5", [V[int(round(t / dt)), 10] for t in [0.5, 3, 6, 9, 12, 13.5]], [0, 9, 15, 12, 10, 11])
chk("(d) step I running sums", [I[int(round(t / dt)), 10] for t in [3, 6, 9, 12, 13.5]], [0.15, 0.05, 0, 0.0333333, 0.05], 1e-5)
chk("(d) DC V, I", [V[-1, 10], I[-1, 10]], [11.25, 0.0375], 1e-6)

print("== 28.12 ==")  # T = 0.5 us; N = 10, dt = 0.05 us
N = 10; dt = 0.05; T = 0.5
tau, Gg, GL, *_ = coeffs(50, 450, np.inf)
chk("tau_g, Gamma_g, Gamma_L", [tau, Gg, GL], [0.1, 0.8, 1])
V, I, F, B = sim(50, 450, np.inf, N, step(10, 1200))
chk("(a) V(l) at 0.5T, 2T, 4T, 6T", [V[int(round(k * T / dt)), N] for k in [0.5, 2, 4, 6]], [0, 2, 3.6, 4.88])
form = [10 * (1 - 0.8 ** (n + 1)) for n in range(25)]
chk("(b) closed form, n=0..24", [V[int(round((2 * n + 2) * T / dt)), N] for n in range(25)], form)
t99 = np.nonzero(V[:, N] >= 9.9)[0][0] * dt
chk("(b) first 99% time (us), = 41T", [t99, t99 / T], [20.5, 41])
Z0, vv, ell, Rg = 50, 200e6, 100, 450
Lp, Cp = Z0 / vv, 1 / (Z0 * vv)
chk("(c) Z0, v from L',C'", [np.sqrt(Lp / Cp), 1 / np.sqrt(Lp * Cp)], [50, 200e6])
C = ell * Cp
chk("(c) C (nF), RgC (us)", [C * 1e9, Rg * C * 1e6], [10, 4.5])
sol = solve_ivp(lambda t, q: [(10 - q[0]) / (Rg * C)], [0, 40e-6], [0], dense_output=True, rtol=1e-11, atol=1e-13)
t99rc = brentq(lambda t: sol.sol(t)[0] - 9.9, 1e-6, 40e-6)
chk("(c) RC 99% time (us)", t99rc * 1e6, 20.7, 2e-3)
chk("(d) e^{-1/4.5}", np.exp(-2 * Z0 / Rg), 0.8007, 1e-4)
x = Z0 / Rg
chk("(d) series", np.exp(-2 * (x + x**3 / 3 + x**5 / 5 + x**7 / 7)), (1 - x) / (1 + x), 1e-7)

print()
print("ALL PASS" if not FAILS else f"FAILS: {FAILS}")
