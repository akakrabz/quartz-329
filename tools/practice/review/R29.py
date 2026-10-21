"""R29: independent check of practice/29-bounce-diagram-examples.md.
Own time-domain simulator: forward/backward delay lines on a Courant-1 grid
(exact for a lossless line).  Each end is solved every step as a 3x3 linear
system from KVL/Ohm (V + Rg I = f_i at z=0; V = RL I, I = 0 or V = 0 at z=l)
with V = F + B, Z0 I = F - B.  No Gamma/tau formulas are used."""
import numpy as np

NF = 0
def chk(name, got, exp, tol=1e-6):
    global NF
    got = np.asarray(got, float); exp = np.asarray(exp, float)
    ok = np.all(np.abs(got - exp) <= tol * np.maximum(1, np.abs(exp)))
    NF += (not ok)
    print(f"{'PASS' if ok else 'FAIL'}  {name}: got {np.round(got, 5).tolist()} expected {np.round(exp, 5).tolist()}")

class Line:
    def __init__(s, Z0, v, ell, Rg, RL, f, dt, tmax):
        N = int(round(ell / (v * dt))); assert abs(N * v * dt - ell) < 1e-9 * ell
        s.N, s.dz, s.dt, s.Z0 = N, ell / N, dt, Z0
        nt = int(round(tmax / dt)) + 1
        s.t = np.arange(nt) * dt
        Mg = np.linalg.inv(np.array([[1, Rg, 0], [1, 0, -1], [0, Z0, -1.]]))
        if RL == np.inf: row = [0, 1, 0]
        elif RL == 0: row = [1, 0, 0]
        else: row = [1, -RL, 0]
        Ml = np.linalg.inv(np.array([row, [1, 0, -1], [0, Z0, 1.]]))
        F = np.zeros(N + 1); B = np.zeros(N + 1)
        s.V = np.zeros((nt, N + 1)); s.I = np.zeros((nt, N + 1))
        for n in range(nt):
            F[1:] = F[:-1].copy(); B[:-1] = B[1:].copy()
            F[0] = (Mg @ np.array([f(s.t[n]), B[0], -B[0]]))[2]
            B[N] = (Ml @ np.array([0, F[N], F[N]]))[2]
            s.V[n] = F + B; s.I[n] = (F - B) / Z0
    def at(s, z, t, q='V'):
        A = s.V if q == 'V' else s.I
        return A[int(round(t / s.dt)), int(round(z / s.dz))]

def rect(a, b, h=1.0):
    return lambda t: h if a < t < b else 0.0

# ---------------- 29.1 ----------------
print("== 29.1")
f = lambda t: 2.0 if 0 < t < 1 else (6.0 if 1 < t < 2 else 0.0)
L = Line(50, 200, 1000, 50, 100, f, 0.005, 4)
chk("V at 300,500 m (t=3)", [L.at(300, 3), L.at(500, 3)], [3, 1])
chk("V at 100,700 m (t=3)", [L.at(100, 3), L.at(700, 3)], [0, 0])
chk("I at 300,500 m mA", [1e3 * L.at(300, 3, 'I'), 1e3 * L.at(500, 3, 'I')], [60, 20])

# ---------------- 29.2 ----------------
print("== 29.2")
rng = np.random.default_rng(1)
# (a) sine never settles
L = Line(50, 200, 400, 30, 140, lambda t: 5 * np.sin(2 * np.pi * t) if t > 0 else 0, 0.01, 60)
seg = L.V[-200:, 200]; chk("(a) late V(200,t) still oscillates (pk-pk>1 V)", seg.max() - seg.min() > 1, 1)
# (b) Rg = Z0 burst D: line at rest after 2T+D
okb = []
for RL in [0, np.inf, 13.0, 170.0]:
    D = 1.3
    L = Line(50, 200, 400, 50, RL, lambda t: np.sin(5 * t) + 2 if 0 < t < D else 0, 0.01, 8)
    n0 = int(round((4 + D) / 0.01)) + 1
    okb.append(np.abs(L.V[n0:]).max() < 1e-12 and np.abs(L.I[n0:]).max() < 1e-12)
chk("(b) at rest for t>2T+D (4 loads)", all(okb), 1)
# (c) final V independent of Z0 and length
fin = []
for Z0, ell in [(50, 400), (90, 600), (20, 200)]:
    L = Line(Z0, 200, ell, 30, 70, lambda t: 10.0 if t > 0 else 0, 0.01, 200)
    fin.append(L.V[-1, L.N // 2])
chk("(c) final V same for 3 lines (=10*70/100)", fin, [7, 7, 7], 1e-4)
# (d) echo: part sent first nearest generator
f = lambda t: 1.0 if 0 < t < 1 else (3.0 if 1 < t < 2 else 0.0)
L = Line(50, 200, 1000, 50, 150, f, 0.005, 10)
# t=8: echo of 1V part on 400-600 (z/v-... ), 3V part on 600-800
chk("(d) echo at t=8: z=500 (1st part), z=700 (2nd part)", [L.at(500, 8) / 0.25, L.at(700, 8) / 0.25], [1, 3])

# ---------------- 29.3 ----------------
print("== 29.3")
w = 4 * np.pi
L = Line(75, 300, 450, 75, 225, lambda t: 8 * np.sin(w * t) if t > 0 else 0, 0.0025, 6)
zz = np.arange(3, 300, 7.5)
chk("(a) V(z,1) = -4 sin(pi z/75)", [L.at(z, 1) for z in zz], -4 * np.sin(np.pi * zz / 75))
chk("(a) V beyond 300 m = 0", [L.at(z, 1) for z in [310, 400, 450]], [0, 0, 0])
chk("(a) I amplitude mA", 1e3 * 4 / 75, 53.3, 1e-3)
tt = np.arange(1.6, 6, 0.0475)
chk("(b) V(l,t) = 6 sin wt", [L.at(450, t) for t in tt], 6 * np.sin(w * tt), 1e-5)
chk("(b) I(l,t) = 26.7 sin wt mA", [1e3 * L.at(450, t, 'I') for t in tt], 26.6667 * np.sin(w * tt), 1e-4)

# ---------------- 29.4 ----------------
print("== 29.4")
f = lambda t: 4.0 if 0 < t < 1 else (2.0 if 1 < t < 2 else 0.0)
L = Line(60, 300, 900, 60, 20, f, 0.005, 6)
chk("V at 450, 750 m (t=5)", [L.at(450, 5), L.at(750, 5)], [-1, -0.5])
chk("I at 450, 750 m mA", [1e3 * L.at(450, 5, 'I'), 1e3 * L.at(750, 5, 'I')], [16.6667, 8.3333], 1e-4)
chk("V at 150 m (t=5) = 0", L.at(150, 5), 0)

# ---------------- 29.5 ----------------
print("== 29.5")
srcs = {'a': lambda t: 12.0 if t > 2 else 0, 'b': lambda t: (9.0 if t > 0 else 0) - (6.0 if t > 1 else 0),
        'd': lambda t: 10.0 if 0 < t < 3 else 0}
exp = {'a': (9.6, 96), 'b': (2.4, 24), 'd': (0, 0)}
for k, f in srcs.items():
    L = Line(50, 200, 300, 25, 100, f, 0.01, 80)
    chk(f"({k}) V, I(mA) at t=80 (z=0,150,300)", [L.V[-1, 0], L.V[-1, 75], L.V[-1, -1], 1e3 * L.I[-1, 0], 1e3 * L.I[-1, -1]],
        [exp[k][0]] * 3 + [exp[k][1]] * 2, 1e-6)
L = Line(50, 200, 300, 25, 100, lambda t: 6 * np.sin(2 * np.pi * t) if t > 0 else 0, 0.01, 80)
seg = L.V[-300:, 75]; chk("(c) late pk-pk of V > 1 V", seg.max() - seg.min() > 1, 1)

# ---------------- 29.6 (new numbers) ----------------
print("== 29.6  Z0=120, Rg=180, RL=40, 15 V on 0-1.5 ns, l=0.1 m, v=0.2 m/ns")
L = Line(120, 0.2, 0.1, 180, 40, rect(0, 1.5, 15), 0.01, 3.5)
mids = [0.5, 1.25, 1.75, 2.25, 2.75]
chk("(a) launched / 15 = tau_g", L.at(0, 0.5) / 15, 0.4)
chk("(b) KVL V = f_i - Rg I at 1.25, 1.75 ns", [15 - 180 * L.at(0, 1.25, 'I'), -180 * L.at(0, 1.75, 'I')], [2.4, -3.6])
chk("(b) V(0,t)", [L.at(0, t) for t in mids], [6, 2.4, -3.6, -3.24, 0.36])
chk("(b) I(0,t) mA", [1e3 * L.at(0, t, 'I') for t in mids], [50, 70, 20, 18, -2])
midsL = [0.25, 1.0, 1.75, 2.25, 2.75]
chk("(c) V(l,t)", [L.at(0.1, t) for t in midsL], [0, 3, 2.7, -0.3, -0.27])
chk("(c) I(l,t) mA", [1e3 * L.at(0.1, t, 'I') for t in midsL], [0, 75, 67.5, -7.5, -6.75])
# coefficients measured from an impulse run
Li = Line(120, 0.2, 0.1, 180, 40, lambda t: 1.0 if abs(t) < 1e-9 else 0, 0.01, 3.2)
a0 = Li.at(0.05, 0.25); b0 = Li.at(0.05, 0.75); a1 = Li.at(0.05, 1.25)
chk("(a) tau_g, Gamma_L, Gamma_g measured", [a0, b0 / a0, a1 / b0], [0.4, -0.5, 0.2])
chk("segment heights x15: fw 6,-0.6,0.06; bw -3,0.3,-0.03",
    [15 * Li.at(0.05, t) for t in [0.25, 1.25, 2.25, 0.75, 1.75, 2.75]], [6, -0.6, 0.06, -3, 0.3, -0.03])

# ---------------- 29.7 ----------------
print("== 29.7")
tri = lambda t: 24 * t if 0 < t <= 0.5 else (24 * (1 - t) if 0.5 < t < 1 else 0.0)
L = Line(50, 200, 400, 50, 0, tri, 0.005, 4)
z = np.arange(0, 401) * 1.0
Va = L.V[400]; Ia = L.I[400]
chk("(a) V(250), V(300), V(350), V(150)", [L.at(250, 2), L.at(300, 2), L.at(350, 2), L.at(150, 2)], [3, 6, 3, 0])
chk("(a) I(300) mA", 1e3 * L.at(300, 2, 'I'), 120)
zz = np.arange(301, 400, 9.0)
chk("(b) V = 0 on whole line (max|V|)", np.abs(L.V[500]).max(), 0, 1e-9)
chk("(b) I = 2.4(z-300) mA on 300-400", [1e3 * L.at(z_, 2.5, 'I') for z_ in zz], 2.4 * (zz - 300))
chk("(b) I(0..300) = 0", np.abs(L.I[500, :300]).max(), 0, 1e-9)
chk("(c) V(300), I(300) mA, V(250)", [L.at(300, 3), 1e3 * L.at(300, 3, 'I'), L.at(250, 3)], [-6, 120, -3])
C, Lp = 1 / (50 * 200e6), 50 / 200e6
trap = lambda y: np.sum(y[1:] + y[:-1]) / 2 * 1.0  # dz = 1 m
Ea = trap(0.5 * C * Va**2 + 0.5 * Lp * Ia**2)
Eb = trap(0.5 * C * L.V[500]**2 + 0.5 * Lp * L.I[500]**2)
chk("energy (a), (b) uJ; C pF/m, L uH/m", [Ea * 1e6, Eb * 1e6, C * 1e12, Lp * 1e6], [0.24, 0.24, 100, 0.25], 1e-3)

# ---------------- 29.8 ----------------
print("== 29.8")
f = rect(0, 1, 20)
v = 100 / 0.5
chk("(a) v m/us", v, 200)
hits = []
for Rg in np.arange(5, 100.1, 5):
    for RL in list(np.arange(10, 300.1, 10)) + [np.inf, 0]:
        L = Line(60, v, 300, Rg, RL, f, 0.01, 12)
        rec = L.V[:, int(round(100 / L.dz))]; t = L.t
        target = np.where((t > 0.5) & (t < 1.5), 15.0, 0.0)
        msk = (np.abs(t - 0.5) > 0.02) & (np.abs(t - 1.5) > 0.02)  # skip edges
        if np.allclose(rec[msk], target[msk], atol=1e-9):
            hits.append((Rg, RL))
chk("(b) unique (Rg, RL) in grid search", hits, [(20, 60)])
L = Line(60, 200, 300, 20, np.inf, f, 0.005, 8)
ts = [1, 2, 3, 4, 5, 6, 7, 7.75]
chk("(c) V(100,t) at 1,2,3,4,5,6,7,7.75", [L.at(100, t) for t in ts], [15, 0, 15, -7.5, 0, -7.5, 3.75, 0])
chk("(c) I(100,t) mA", [1e3 * L.at(100, t, 'I') for t in ts], [250, 0, -250, -125, 0, 125, 62.5, 0])

# ---------------- 29.9 (R_L = 10 ohm) ----------------
print("== 29.9  RL = 10 ohm")
f = lambda t: 12 * np.sin(2 * np.pi * t) if 0 < t < 1 else 0.0
L = Line(50, 200, 500, 150, 10, f, 0.0025, 7)
k = np.pi / 100
Li = Line(50, 200, 500, 150, 10, lambda t: 1.0 if abs(t) < 1e-9 else 0, 0.0025, 11)
amps = [12 * Li.at(250, t) for t in [1.25, 3.75, 6.25, 8.75]]
chk("(a) amplitudes of first 4 segments", amps, [3, -2, -1, 2 / 3])
chk("(a) tau_g, Gamma_L, Gamma_g", [amps[0] / 12, amps[1] / amps[0], amps[2] / amps[1]], [0.25, -2 / 3, 0.5])
zz = np.arange(201, 400, 6.0)
chk("(b) V(z,2) = -3 sin kz on 200-400", [L.at(z_, 2) for z_ in zz], -3 * np.sin(k * zz))
chk("(b) V(350), V(250), I peak mA", [L.at(350, 2), L.at(250, 2), 1e3 * L.at(250, 2, 'I')], [3, -3, -60])
chk("(b) zero outside 200-400", np.abs(np.r_[L.V[800, :400], L.V[800, 801:]]).max(), 0, 1e-9)
z1 = np.arange(351, 450, 6.0); z2 = np.arange(451, 500, 4.0)
chk("(c) V = -3cos kz on 350-450", [L.at(z_, 2.75) for z_ in z1], -3 * np.cos(k * z1))
chk("(c) I = -60cos kz mA on 350-450", [1e3 * L.at(z_, 2.75, 'I') for z_ in z1], -60 * np.cos(k * z1))
chk("(c) V = -cos kz on 450-500", [L.at(z_, 2.75) for z_ in z2], -1 * np.cos(k * z2))
chk("(c) I = -100cos kz mA on 450-500", [1e3 * L.at(z_, 2.75, 'I') for z_ in z2], -100 * np.cos(k * z2))
chk("(c) load V, I mA, V/I", [L.at(500, 2.75), 1e3 * L.at(500, 2.75, 'I'), L.at(500, 2.75) / L.at(500, 2.75, 'I')], [1, 100, 10])
chk("(c) zero on 0-350", np.abs(L.V[1100, :700]).max(), 0, 1e-9)
z3 = np.arange(1, 200, 6.0)
chk("(d) V(z,6) = sin kz on 0-200", [L.at(z_, 6) for z_ in z3], np.sin(k * z3))
chk("(d) I = V/50: peak mA at 150 (leading half negative)", [1e3 * L.at(150, 6, 'I'), L.at(150, 6)], [-20, -1])
chk("(d) zero on 200-500", np.abs(L.V[2400, 401:]).max(), 0, 1e-9)

# ---------------- 29.10 (ramp cut off at 5 us; (d) at t = 6) ----------------
print("== 29.10  f = 20t on 0<t<5, l = 300 m")
f = lambda t: 20 * t if 0 < t < 5 else 0.0
L = Line(50, 200, 300, 50, np.inf, f, 0.005, 10)
ta = np.array([1.3, 2.7, 3.4, 4.6, 5.5, 7.9, 8.5, 9.6])
Vexp = np.where(ta < 3, 10 * ta, np.where(ta < 5, 20 * ta - 30, np.where(ta < 8, 10 * (ta - 3), 0)))
Iexp = np.where(ta < 3, 0.2 * ta, np.where(ta < 5, 0.6, np.where(ta < 8, -0.2 * (ta - 3), 0)))
chk("(a) V(0,t)", [L.at(0, t) for t in ta], Vexp)
chk("(a) I(0,t) A", [L.at(0, t, 'I') for t in ta], Iexp)
tb = np.array([1.0, 2.0, 4.0, 6.4, 6.6, 9.0])
chk("(b) V(l,t) = 20(t-1.5) on 1.5-6.5", [L.at(300, t) for t in tb], np.where((tb > 1.5) & (tb < 6.5), 20 * (tb - 1.5), 0))
chk("(b) peak 100 V; I(l,t)=0", [L.at(300, 6.495), np.abs(L.I[:, -1]).max()], [99.9, 0], 1e-6)
zz = np.arange(0, 301, 25.0)
chk("(c) V(z,4.5) = 60", [L.at(z_, 4.5) for z_ in zz], 60 * np.ones_like(zz))
chk("(c) I = 0.6(1-z/300)", [L.at(z_, 4.5, 'I') for z_ in zz], 0.6 * (1 - zz / 300))
chk("(c) C*l nF and C*l*dV/dt A", [300 / (50 * 200e6) * 1e9, 300 / (50 * 200e6) * 20e6], [30, 0.6])
z1 = np.arange(0, 200, 13.0); z2 = np.arange(201, 301, 11.0)
chk("(d) V = 30 + z/20 on 0-200", [L.at(z_, 6) for z_ in z1], 30 + z1 / 20)
chk("(d) I = -(0.6 + z/1000) on 0-200", [L.at(z_, 6, 'I') for z_ in z1], -(0.6 + z1 / 1000))
chk("(d) V = 90 on 200-300", [L.at(z_, 6) for z_ in z2], 90 * np.ones_like(z2))
chk("(d) I = 0.6 - z/500 on 200-300", [L.at(z_, 6, 'I') for z_ in z2], 0.6 - z2 / 500)
ex = lambda q, a, b: 2 * L.at(a, 6, q) - L.at(b, 6, q)  # one-sided limits
dV = ex('V', 199, 198) - ex('V', 201, 202); dI = ex('I', 199, 198) - ex('I', 201, 202)
chk("(d) jump dV, dI at 200 m (left-right), dV/dI", [dV, dI, dV / dI], [-50, -1.0, 50])
chk("(d) V(0) = -Rg I(0) = 30 V", -50 * L.at(0, 6, 'I'), 30)

# ---------------- 29.11 ----------------
print("== 29.11")
Li = Line(50, 200, 400, 25, 100, lambda t: 1.0 if abs(t) < 1e-9 else 0, 0.005, 12)
tk = [1.5, 2.5, 5.5, 6.5, 9.5, 10.5]
chk("(a) impulse weights at 300 m", [Li.at(300, t) for t in tk], [2 / 3, 2 / 9, -2 / 27, -2 / 81, 2 / 243, 2 / 729])
chk("(a) Z0 I weights", [50 * Li.at(300, t, 'I') for t in tk], [2 / 3, -2 / 9, -2 / 27, 2 / 81, 2 / 243, -2 / 729])
nz = np.abs(Li.V[:, 300]) > 1e-12
chk("(a) no other impulses for t<12", np.round(Li.t[nz], 4).tolist(), tk)
f = lambda t: 13.5 * t if 0 < t < 2 else (27.0 if t >= 2 else 0.0)
L = Line(50, 200, 400, 25, 100, f, 0.005, 200)
tb = [1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5]
chk("(b) V(300,t)", [L.at(300, t) for t in tb], [0, 9, 21, 24, 24, 23, 65 / 3, 64 / 3, 64 / 3])
tl = np.arange(1.5, 9.5, 0.005); Vl = np.array([L.at(300, t) for t in tl])
lin = np.interp(tl, tb, [0, 9, 21, 24, 24, 23, 65 / 3, 64 / 3, 64 / 3])
chk("(b) piecewise linear between listed points (max dev)", np.abs(Vl - lin).max(), 0, 1e-9)
chk("(c) I(300) on 4.5-5.5 and 8.5-9.5 mA", [1e3 * L.at(300, 5, 'I'), 1e3 * L.at(300, 9, 'I')], [240, 213.333], 1e-5)
chk("(c) Z0 I = 18-6 = 12 V (no third ramp yet)", 50 * L.at(300, 5, 'I'), 12)
chk("(d) V, I(mA) at t=200", [L.V[-1, 300], 1e3 * L.I[-1, 300]], [21.6, 216], 1e-6)
chk("(d) peak V and overshoot", [L.V[:, 300].max(), L.V[:, 300].max() - 21.6], [24, 2.4])

# ---------------- 29.12 ----------------
print("== 29.12")
w = np.pi
L = Line(75, 200, 500, 75, 25, lambda t: 12 * np.sin(w * t) if t > 0 else 0, 0.005, 30)
tt = np.arange(2.6, 30, 0.135)
chk("(b) V(l,t) = -3cos(pi t)", [L.at(500, t) for t in tt], -3 * np.cos(w * tt), 1e-6)
chk("(b) I(l,t) = -120cos(pi t) mA", [1e3 * L.at(500, t, 'I') for t in tt], -120 * np.cos(w * tt), 1e-6)
b = np.pi / 200
z1 = np.arange(1, 200, 7.0); z2 = np.arange(201, 501, 7.0)
chk("(c) V = -6 sin bz on 0-200", [L.at(z_, 4) for z_ in z1], -6 * np.sin(b * z1))
chk("(c) I = -80 sin bz mA on 0-200", [1e3 * L.at(z_, 4, 'I') for z_ in z1], -80 * np.sin(b * z1))
chk("(c) V = -3 sin bz on 200-500", [L.at(z_, 4) for z_ in z2], -3 * np.sin(b * z2))
chk("(c) I = -120 sin bz mA on 200-500", [1e3 * L.at(z_, 4, 'I') for z_ in z2], -120 * np.sin(b * z2))
win = slice(int(26 / 0.005), int(30 / 0.005))
zp = [0, 100, 200, 300, 400, 500]
chk("(d) |V| amplitude at 0,100,..,500", [np.abs(L.V[win, int(z_)]).max() for z_ in zp], [9, 3, 9, 3, 9, 3], 1e-4)
chk("(d) |I| amplitude mA", [1e3 * np.abs(L.I[win, int(z_)]).max() for z_ in zp], [40, 120, 40, 120, 40, 120], 1e-4)
zz = np.arange(0, 501, 10)
chk("(d) V amp = sqrt(45+36cos2bz)", [np.abs(L.V[win, z_]).max() for z_ in zz], np.sqrt(45 + 36 * np.cos(2 * b * zz)), 2e-4)
chk("(d) V(0,t) = 9 sin wt, I = 40 sin wt mA", [L.at(0, 27.3), 1e3 * L.at(0, 27.3, 'I')], [9 * np.sin(w * 27.3), 40 * np.sin(w * 27.3)])

print("== originals before review re-parameterization (page's old numbers)")
L = Line(50, 0.2, 0.1, 75, 150, rect(0, 1.5, 10), 0.01, 3.5)
chk("old 29.6 V(0,t), I(0,t) mA", [L.at(0, t) for t in mids] + [1e3 * L.at(0, t, 'I') for t in mids], [4, 6.4, 2.4, 2.64, 0.24, 80, 48, -32, -35.2, -3.2])
chk("old 29.6 V(l,t), I(l,t) mA", [L.at(0.1, t) for t in midsL] + [1e3 * L.at(0.1, t, 'I') for t in midsL], [0, 6, 6.6, 0.6, 0.66, 0, 40, 44, 4, 4.4])
L = Line(50, 200, 500, 150, 25, lambda t: 12 * np.sin(2 * np.pi * t) if 0 < t < 1 else 0.0, 0.0025, 7)
chk("old 29.9 (c) V,I at 470 m; (d) V at 150 m", [L.at(470, 2.75), 1e3 * L.at(470, 2.75, 'I'), L.at(150, 6)], [-2 * np.cos(4.7 * np.pi), -80 * np.cos(4.7 * np.pi), -0.5])
L = Line(50, 200, 300, 50, np.inf, lambda t: 20 * t if 0 < t < 6 else 0.0, 0.005, 10)
chk("old 29.10 (d) t=7: V(100), I(100), V(250), I(250)", [L.at(100, 7), L.at(100, 7, 'I'), L.at(250, 7), L.at(250, 7, 'I')], [45, -0.9, 110, 0.1])

print("\nFAILS:", NF)
