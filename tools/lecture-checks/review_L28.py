#!/usr/bin/env python3
"""Independent review checks for Lecture 28 (bounce diagrams). numpy/scipy only.

Three independent engines:
  FDTD  - Yee leapfrog of the telegrapher's equations, resistive half-cell terminations (Paul).
  CHAR  - exact characteristic (lattice) solver: forward/backward samples shift one cell per step;
          at each end the unknown outgoing wave is found by solving the circuit laws (KVL, Ohm),
          never from a Gamma formula.
  FREQ  - phasor solution of the terminated line (2x2 linear solve) vs the page's series.
"""
import sys
import numpy as np

sys.path.insert(0, "/home/claude/work")
NPASS = NFAIL = 0


def check(name, ok, info=""):
    global NPASS, NFAIL
    if ok:
        NPASS += 1
    else:
        NFAIL += 1
    print(("PASS " if ok else "FAIL ") + name + (("  | " + info) if info else ""))


def close(a, b, tol=1e-9):
    return np.allclose(a, b, rtol=tol, atol=tol)


# ----------------------------------------------------------------------------- engines
def char_solve(Z0, Rg, RL, N, nsteps, fi):
    """exact lattice: a[k] forward, b[k] backward at node k (k=0..N); one cell per step.
    fi(n) = source sample at step n. Returns V[n,k], I[n,k]."""
    a = np.zeros(N + 1); b = np.zeros(N + 1)
    V = np.zeros((nsteps, N + 1)); I = np.zeros((nsteps, N + 1))
    for n in range(nsteps):
        if n > 0:
            a[1:] = a[:-1].copy(); b[:-1] = b[1:].copy()
        # generator node: unknown a0; V=a0+b0, I=(a0-b0)/Z0, fi = Rg*I + V
        # -> linear in a0: (Rg/Z0 + 1) a0 = fi - b0 + Rg*b0/Z0
        # solve generically: unknowns x=[V, I, a0]
        A = np.array([[1.0, 0.0, -1.0],          # V - a0 = b0
                      [0.0, Z0, -1.0],           # Z0 I - a0 = -b0
                      [1.0, Rg, 0.0]])           # V + Rg I = fi
        rhs = np.array([b[0], -b[0], fi(n)])
        x = np.linalg.solve(A, rhs); a[0] = x[2]
        # load node: unknown bN; V=aN+bN, I=(aN-bN)/Z0, I = GL V (GL = 1/RL; RL=inf -> 0; RL=0 -> V=0)
        if RL == 0:
            A = np.array([[1.0, 0.0, -1.0], [0.0, Z0, 1.0], [1.0, 0.0, 0.0]]); rhs = np.array([a[N], a[N], 0.0])
        else:
            GL = 0.0 if np.isinf(RL) else 1.0 / RL
            A = np.array([[1.0, 0.0, -1.0], [0.0, Z0, 1.0], [-GL, 1.0, 0.0]]); rhs = np.array([a[N], a[N], 0.0])
        x = np.linalg.solve(A, rhs); b[N] = x[2]
        V[n] = a + b; I[n] = (a - b) / Z0
    return V, I


def fdtd(Z0, Rg, RL, N, nsteps, fi_t, dt, S=1.0):
    """Yee scheme with Courant number S (dt = S dz/v; S = 1 decouples odd/even sublattices for a step,
    so step runs use S = 0.5). V at integer nodes/times, I at half nodes/times.
    fi_t(t) source. Returns V[n,k] (t=n dt) and I[n,k] (t=(n-1/2)dt at z=(k+1/2)dz)."""
    V = np.zeros(N + 1); I = np.zeros(N)
    Vs = np.zeros((nsteps, N + 1)); Is = np.zeros((nsteps, N))
    for n in range(nsteps):
        Vs[n] = V; Is[n] = I
        I = I - S * (V[1:] - V[:-1]) / Z0
        Vn = V.copy()
        Vn[1:-1] = V[1:-1] - S * Z0 * (I[1:] - I[:-1])
        fs = fi_t((n + 0.5) * dt)
        if Rg == 0:
            Vn[0] = fi_t((n + 1) * dt)
        else:
            Vn[0] = (V[0] * (1 / (S * Z0) - 1 / Rg) + 2 * fs / Rg - 2 * I[0]) / (1 / (S * Z0) + 1 / Rg)
        if RL == 0:
            Vn[-1] = 0.0
        else:
            GL = 0.0 if np.isinf(RL) else 1.0 / RL
            Vn[-1] = (V[-1] * (1 / (S * Z0) - GL) + 2 * I[-1]) / (1 / (S * Z0) + GL)
        V = Vn
    return Vs, Is


def gamma(R, Z0):
    return 1.0 if np.isinf(R) else (R - Z0) / (R + Z0)


def impulse_list(V_t, I_t, dtn, thr=1e-12):
    """from a lattice record with a single-sample impulse, list (t, Vweight, Iweight)"""
    idx = np.nonzero(np.abs(V_t) + np.abs(I_t) > thr)[0]
    return [(i * dtn, V_t[i] * dtn, I_t[i] * dtn) for i in idx]


print("=" * 100)
print("[A] Algebra: load condition, KVL at z = 0, recursion, tau_g, Gamma_g, DC limit (random circuits)")
rng = np.random.default_rng(28)
okA = []
for _ in range(200):
    Z0, Rg, RL = rng.uniform(5, 300, 3)
    f = rng.normal()
    # load: Z0 (f+g)/(f-g) = RL -> solve for g numerically (linear)
    g = np.linalg.solve([[Z0 + RL]], [RL * f - Z0 * f])[0]
    okA.append(np.isclose(g / f, (RL - Z0) / (RL + Z0)))
check("A1 load: g(t+T)/f(t-T) = (R_L - Z0)/(R_L + Z0) from V/I = R_L (200 random circuits)", all(okA))
okB, okC, okD, okE = [], [], [], []
for _ in range(200):
    Z0, Rg, RL = rng.uniform(5, 300, 3)
    GL = (RL - Z0) / (RL + Z0)
    fi, fprev = rng.normal(size=2)
    # KVL: fi = Rg*(f - GL fprev)/Z0 + f + GL fprev; solve for f
    fsol = (fi - GL * fprev * (1 - Rg / Z0)) / (1 + Rg / Z0)
    lhs = Rg * (fsol - GL * fprev) / Z0 + fsol + GL * fprev
    okB.append(np.isclose(lhs, fi))
    tg = Z0 / (Rg + Z0); Gg = (Rg - Z0) / (Rg + Z0)
    okC.append(np.isclose(fsol, tg * fi + Gg * GL * fprev))
    okD.append(np.isclose(tg, (1 - Gg) / 2))
    # DC
    VDC = tg * (1 + GL) / (1 - GL * Gg); IDC = tg * (1 - GL) / (1 - GL * Gg) / Z0
    okE.append(np.isclose(VDC, RL / (Rg + RL)) and np.isclose(IDC, 1 / (Rg + RL)))
check("A2 KVL expansion f_i = (Rg/Z0)[f - G_L f(t-2T)] + f + G_L f(t-2T) and regrouped form", all(okB))
check("A3 recursion f = tau_g f_i + Gamma_g Gamma_L f(t-2T)", all(okC))
check("A4 tau_g = (1 - Gamma_g)/2", all(okD))
check("A5 DC limit tau_g(1+G_L)/(1-G_L G_g) = R_L/(R_g+R_L), tau_g(1-G_L)/(1-G_L G_g)/Z0 = 1/(R_g+R_L)", all(okE))
# derivation box identities
okF = []
for _ in range(100):
    Z0, Rg, RL = rng.uniform(5, 300, 3)
    GL = (RL - Z0) / (RL + Z0); Gg = (Rg - Z0) / (Rg + Z0); tg = Z0 / (Rg + Z0)
    d = (RL + Z0) * (Rg + Z0)
    okF.append(np.isclose(1 - GL * Gg, 2 * Z0 * (RL + Rg) / d) and np.isclose(tg * (1 + GL), 2 * Z0 * RL / d)
               and np.isclose(tg * (1 - GL), 2 * Z0 ** 2 / d))
check("A6 derivation-box identities (1-G_L G_g, tau_g(1+G_L), tau_g(1-G_L))", all(okF))
# backward term delay: Gamma_L f(t + z/v - 2T) = Gamma_L f(t - z/v - 2(l-z)/v)
z, v, l = 0.37, 1.0, 1.0
check("A7 backward term = forward delayed by round trip 2(l-z)/v", np.isclose(z / v - 2 * l / v, -z / v - 2 * (l - z) / v))
# erratum 1: delta(t + z/v - 2l/v) = delta(t - T_z) with T_z = 2l/v - z/v > 0
check("A8 erratum 1: backward delay T_z = 2l/v - z/v (>0 for 0<z<l), notes' z/v - 2l/v < 0",
      (2 * l / v - z / v) > 0 and (z / v - 2 * l / v) < 0)
# |Gamma| <= 1 for passive resistors
Rs = np.concatenate([np.linspace(0, 1e4, 1001), [1e12]])
check("A9 |Gamma| <= 1 for 0 <= R <= inf", np.all(np.abs((Rs - 50) / (Rs + 50)) <= 1 + 1e-12))
# L25 analogy: Gamma = (eta2 - eta1)/(eta2 + eta1) with eta1 -> Z0, eta2 -> R_L
check("A10 L25 mapping eta1->Z0, eta2->R_L gives Gamma_L", np.isclose((30 - 50) / (30 + 50), gamma(30, 50)))

print("=" * 100)
print("[B] Frequency domain: page's impulse-response series vs direct phasor solution of the terminated line")
okG = []
for Z0, Rg, RL in [(50, 150, 50 / 3), (75, 25, 37.5), (50, 0.0, 1e9), (50, 10.0, 1e12), (60, 60, 0.0), (100, 20, 400)]:
    T = 1.0; v = 1.0; l = 1.0
    tg = Z0 / (Rg + Z0); Gg = (Rg - Z0) / (Rg + Z0); GL = (RL - Z0) / (RL + Z0)
    for w in [0.3, 1.1, 2.7, 5.0]:
        A = np.array([[1 + Rg / Z0, 1 - Rg / Z0],
                      [np.exp(-1j * w * T) * (1 - RL / Z0), np.exp(1j * w * T) * (1 + RL / Z0)]])
        Af, Bf = np.linalg.solve(A, [1.0, 0.0])
        for z in [0.0, 0.25, 0.5, 0.9, 1.0]:
            Vd = Af * np.exp(-1j * w * z / v) + Bf * np.exp(1j * w * z / v)
            Id = (Af * np.exp(-1j * w * z / v) - Bf * np.exp(1j * w * z / v)) / Z0
            if abs(GL * Gg) < 0.9:
                n = np.arange(400)
                S = np.sum((GL * Gg) ** n * np.exp(-2j * w * n * T))
            else:
                S = 1 / (1 - GL * Gg * np.exp(-2j * w * T))
            Vs = tg * S * (np.exp(-1j * w * z / v) + GL * np.exp(-1j * w * (2 * T - z / v)))
            Is = tg / Z0 * S * (np.exp(-1j * w * z / v) - GL * np.exp(-1j * w * (2 * T - z / v)))
            okG.append(np.isclose(Vd, Vs, rtol=1e-6) and np.isclose(Id, Is, rtol=1e-6))
check("B1 Fourier transform of the series V(z,t), I(z,t) = phasor solution (6 circuits x 4 freqs x 5 z)", all(okG),
      f"{sum(okG)}/{len(okG)}")

print("=" * 100)
print("[C] Lattice (exact characteristics) vs FDTD vs page, impulse and step: page example Z0=60, Rg=180, RL=20\n"
      "    (review re-parameterized it from Z0=50, Rg=150, RL=50/3, whose Z0, RL equal S20 FE #5; all voltages unchanged)")
Z0, Rg, RL = 60.0, 180.0, 20.0
tg, Gg, GL = Z0 / (Rg + Z0), (Rg - Z0) / (Rg + Z0), (RL - Z0) / (RL + Z0)
check("C1 tau_g = 1/4, Gamma_g = 1/2, Gamma_L = -1/2", close([tg, Gg, GL], [0.25, 0.5, -0.5]))
N = 40                     # cells; one step = T/N
ns = 12 * N
Vl, Il = char_solve(Z0, Rg, RL, N, ns, lambda n: N * 1.0 if n == 0 else 0.0)   # unit impulse, area 1 (dt = 1/N)
imp = impulse_list(Vl[:, N // 2], Il[:, N // 2], 1 / N)
tt = [round(t, 9) for t, _, _ in imp][:6]
wv = [w for _, w, _ in imp][:6]; wi = [Z0 * w for _, _, w in imp][:6]
check("C2 impulse at l/2: times T/2, 3T/2, 5T/2, 7T/2, 9T/2, 11T/2", close(tt, [0.5, 1.5, 2.5, 3.5, 4.5, 5.5]), str(tt))
check("C3 V weights 1/4, -1/8, -1/16, 1/32, 1/64, -1/128", close(wv, [1 / 4, -1 / 8, -1 / 16, 1 / 32, 1 / 64, -1 / 128]),
      str(np.round(wv, 6)))
check("C4 Z0*I weights 1/4, +1/8, -1/16, -1/32, +1/64, +1/128 (page writes '- ...' after -1/32: next is +)",
      close(wi, [1 / 4, 1 / 8, -1 / 16, -1 / 32, 1 / 64, 1 / 128]), str(np.round(wi, 6)))
# page's series (section 4 key) vs lattice at several z
okS = []
for k in [0, 5, 13, 20, 33, 40]:
    zz = k / N
    imp = impulse_list(Vl[:, k], Il[:, k], 1 / N)
    pred = {}
    for n in range(8):
        for t, wV, wI in [(zz + 2 * n, tg * (GL * Gg) ** n, tg * (GL * Gg) ** n / Z0),
                          (2 * (n + 1) - zz, tg * GL * (GL * Gg) ** n, -tg * GL * (GL * Gg) ** n / Z0)]:
            key = round(t, 9)
            a, b = pred.get(key, (0, 0)); pred[key] = (a + wV, b + wI)
    for t, wV, wI in imp:
        if t < 11.5:
            p = pred.get(round(t, 9), (np.nan, np.nan))
            okS.append(np.isclose(wV, p[0], atol=1e-12) and np.isclose(wI, p[1], atol=1e-12))
check("C5 section-4 series (V and I, n = 0..7) = lattice at z = 0, 0.125l, ..., l (ends: arrival + reflection add)",
      all(okS), f"{len(okS)} impulses")
# recipe step 5: at the load the arrival and reflection add: (1+G_L) w
impL = impulse_list(Vl[:, N], Il[:, N], 1 / N)
check("C6 V(l,t) impulse at T = (1+G_L) tau_g = 1/8; I(l,t) = (1-G_L) tau_g/Z0", np.isclose(impL[0][1], (1 + GL) * tg)
      and np.isclose(impL[0][2], (1 - GL) * tg / Z0) and np.isclose(impL[0][0], 1.0))
# step: 12 V
V0 = 12.0
Vs_, Is_ = char_solve(Z0, Rg, RL, N, ns, lambda n: V0)
def at(Varr, t):
    return Varr[int(round(t * N))]
loads = [at(Vs_[:, N], t) for t in (2, 4, 6, 8)]
check("C7 V(l,t) on (T,3T),(3T,5T),(5T,7T),(7T,9T) = 1.5, 1.125, 1.219, 1.195",
      close(loads[:2], [1.5, 1.125]) and np.allclose(loads[2:], [1.219, 1.195], atol=6e-4), str(np.round(loads, 5)))
mids = [at(Vs_[:, N // 2], t) for t in (1, 2, 3, 4, 5)]
check("C8 V(l/2,t) steps 3, 1.5, 0.75, 1.125, 1.3125 at T/2 + kT", close(mids, [3, 1.5, 0.75, 1.125, 1.3125]), str(mids))
# long run for DC
VlongV, VlongI = char_solve(Z0, Rg, RL, N, 60 * N, lambda n: V0)
okDC = np.allclose(VlongV[-1], 1.2, atol=1e-9) and np.allclose(VlongI[-1], 0.060, atol=1e-9)
check("C9 DC: V = 1.2 V and I = 60 mA at every z (t = 60T)", okDC, f"V {VlongV[-1].min():.9f}..{VlongV[-1].max():.9f}")
check("C10 12*20/(180+20) = 1.2, 12/200 = 0.060", np.isclose(12 * 20 / (180 + 20), 1.2) and np.isclose(12 / 200, 0.060))
# overshoot/undershoot at load and midpoint
LV = [at(VlongV[:, N], t) for t in np.arange(2, 20, 2)]
sgn = np.sign(np.array(LV) - 1.2)
check("C11 load staircase alternates about 1.2 V (G_L G_g = -1/4 < 0)", np.all(sgn[1:] == -sgn[:-1]), str(np.round(LV, 4)))
MV = [at(VlongV[:, N // 2], t) for t in np.arange(1, 14, 1)]
check("C12 midpoint staircase both over- and undershoots 1.2 V", (np.max(MV) > 1.2) and (np.min(MV) < 1.2), str(np.round(MV, 4)))

# FDTD cross-check of the lattice for the same example (independent scheme)
from scipy.special import erf
Nf = 400; dt = 1.0 / Nf          # S = 1 with a smoothed step (erf edge, 0.01T wide, centred at 0.05T)
sstep = lambda t: V0 * 0.5 * (1 + erf((t - 0.05) / (0.01 * np.sqrt(2))))
Vf, If = fdtd(Z0, Rg, RL, Nf, 10 * Nf, sstep, dt)
fl = [Vf[int(round((t + 0.05) / dt)), Nf] for t in (2, 4, 6, 8)]
fm = [Vf[int(round((t + 0.05) / dt)), Nf // 2] for t in (1, 2, 3, 4, 5)]
check("C13 FDTD step: load 1.5, 1.125, 1.219, 1.195; midpoint 3, 1.5, 0.75, 1.125, 1.3125 (1e-3)",
      np.allclose(fl, [1.5, 1.125, 1.21875, 1.1953125], atol=1e-3) and np.allclose(fm, [3, 1.5, 0.75, 1.125, 1.3125], atol=1e-3),
      f"{np.round(fl, 4)} {np.round(fm, 4)}")
fi_mid = [If[int(round((t + 0.05) / dt)), Nf // 2] for t in (1, 2, 3, 4)]
pred_I = np.cumsum([3, 1.5, -0.75, -0.375]) / Z0
check("C14 FDTD step current at l/2: running sum of current weights (backward flipped)", np.allclose(fi_mid, pred_I, atol=2e-5),
      f"{np.round(fi_mid, 5)} vs {np.round(pred_I, 5)}")
# FDTD Gaussian pulse: impulse weights at l/2
sig = 0.01
Vg, Ig = fdtd(Z0, Rg, RL, Nf, 8 * Nf, lambda t: np.exp(-0.5 * ((t - 0.1) / sig) ** 2) / (sig * np.sqrt(2 * np.pi)), dt)
tg_ = np.arange(8 * Nf) * dt
w_meas = []; wI_meas = []
for tc in (0.5, 1.5, 2.5, 3.5):
    m = np.abs(tg_ - (tc + 0.1)) < 0.2
    w_meas.append(np.sum(Vg[m, Nf // 2]) * dt); wI_meas.append(Z0 * np.sum(Ig[m, Nf // 2]) * dt)
check("C15 FDTD Gaussian (area 1): V areas at l/2 = 1/4, -1/8, -1/16, 1/32; Z0*I = 1/4, 1/8, -1/16, -1/32",
      np.allclose(w_meas, [.25, -.125, -.0625, .03125], atol=2e-3) and np.allclose(wI_meas, [.25, .125, -.0625, -.03125], atol=2e-3),
      f"{np.round(w_meas, 4)} {np.round(wI_meas, 4)}")

GLold = gamma(50 / 3, 50); GLfe = gamma(50 / 3, 50)
check("C16 old example (Z0=50, RL=50/3) shared Gamma_L = -1/2 with S20 FE #5a (same Z0, RL); new Z0, Rg, RL match no exam setup",
      np.isclose(GLold, -0.5) and (Z0, Rg, RL) not in [(50, 25, 50 / 3), (50, 100, 25), (50, 30, 150), (60, 60, 0), (50, 100, 100)])
print("=" * 100)
print("[D] Section 6 terminations (lattice, impulse and step)")
N = 20
# matched load: no echo anywhere
V_, I_ = char_solve(50, 100, 50, N, 8 * N, lambda n: N if n == 0 else 0.0)
check("D1 matched load: one impulse at each z, nothing after", all(len(impulse_list(V_[:, k], I_[:, k], 1 / N)) == 1 for k in range(N + 1)))
# open load: I(l)=0, V(l) = 2 x arriving
V_, I_ = char_solve(50, 100, np.inf, N, 8 * N, lambda n: N if n == 0 else 0.0)
arr = 50 / 150
check("D2 open load: I(l,t) = 0 always; V(l,T) = 2 x arriving tau_g", np.allclose(I_[:, N], 0) and
      np.isclose(impulse_list(V_[:, N], I_[:, N], 1 / N)[0][1], 2 * arr))
V_, I_ = char_solve(50, 100, 0.0, N, 8 * N, lambda n: N if n == 0 else 0.0)
check("D3 short load: V(l,t) = 0 always; I(l,T) = 2 x arriving current", np.allclose(V_[:, N], 0) and
      np.isclose(impulse_list(V_[:, N], I_[:, N], 1 / N)[0][2], 2 * arr / 50))
V_, I_ = char_solve(50, 50, 200, N, 8 * N, lambda n: N if n == 0 else 0.0)
check("D4 matched generator: tau_g = 1/2, nothing on the line after t = 2T", np.allclose(V_[2 * N + 1:], 0) and
      np.isclose(impulse_list(V_[:, 0], I_[:, 0], 1 / N)[0][1], 0.5))
fsrc = lambda n: np.sin(0.3 * n) * (n < 3 * N)
V_, I_ = char_solve(50, 0.0, 200, N, 8 * N, fsrc)
check("D5 ideal source R_g = 0: V(0,t) = f_i(t) at all times, tau_g = 1", np.allclose(V_[:, 0], [fsrc(n) for n in range(8 * N)]))
# ideal source + open load: |G_L G_g| = 1, no decay
V_, I_ = char_solve(50, 0.0, np.inf, N, 20 * N, lambda n: N if n == 0 else 0.0)
w = [abs(x[1]) for x in impulse_list(V_[:, N // 2], I_[:, N // 2], 1 / N)]
check("D6 ideal source + open load: echoes never decay (|weights| all 1)", np.allclose(w, 1.0), f"{len(w)} impulses")

print("=" * 100)
print("[E] Worked problem: 120 m line, v = 150 m/us, Z0 = 75, observe at 30 m (lattice in physical units + FDTD)")
c = 300.0
v = 30 / 0.2; T = 120 / v
check("E1 v = 150 m/us, T = 0.8 us, eps_r = 4, echo at (2l - z)/v = 1.4 us",
      np.isclose(v, 150) and np.isclose(T, 0.8) and np.isclose((c / v) ** 2, 4) and np.isclose((240 - 30) / v, 1.4))
Z0 = 75.0
RLw = Z0 * (1 + (-1 / 3)) / (1 - (-1 / 3))
check("E2 R_L = 37.5 ohm from Gamma_L = -1/3; A = 24*75/150 = 12", np.isclose(RLw, 37.5) and np.isclose(24 * 75 / 150, 12))
N = 120                     # dz = 1 m; dt = 1/150 us
dtn = 1.0 / 150
def run_problem(Rg, src):
    return char_solve(Z0, Rg, 37.5, N, int(6 / dtn), src)
V_, I_ = run_problem(75.0, lambda n: 24 / dtn if n == 0 else 0.0)
imp = impulse_list(V_[:, 30], I_[:, 30], dtn)
check("E3 R_g = 75: exactly two impulses at 30 m, 12 at 0.2 us and -4 at 1.4 us",
      len(imp) == 2 and np.allclose([x[0] for x in imp], [0.2, 1.4]) and np.allclose([x[1] for x in imp], [12, -4]),
      str([(round(a, 4), round(b, 4)) for a, b, _ in imp]))
check("E4 current: 0.16 and +0.05333 A.us", np.allclose([x[2] for x in imp], [0.16, 4 / 75]), str([round(x[2], 5) for x in imp]))
# uniqueness: any other R_g gives a pulse at 1.8 us
V2, I2 = run_problem(76.0, lambda n: 24 / dtn if n == 0 else 0.0)
check("E5 R_g = 76 ohm would add a pulse at 1.8 us (so R_g = Z0 is forced)",
      any(np.isclose(x[0], 1.8) for x in impulse_list(V2[:, 30], I2[:, 30], dtn, 1e-9)))
V_, I_ = run_problem(25.0, lambda n: 24 / dtn if n == 0 else 0.0)
imp = [x for x in impulse_list(V_[:, 30], I_[:, 30], dtn) if x[0] < 3.5]
check("E6 R_g = 25: tau_g = 3/4, Gamma_g = -1/2, G_L G_g = 1/6", np.isclose(75 / 100, .75) and np.isclose(-50 / 100, -.5)
      and np.isclose((-1 / 3) * (-1 / 2), 1 / 6))
check("E7 impulses at 30 m for t < 3.5: 18@0.2, -6@1.4, 3@1.8, -1@3.0, 0.5@3.4",
      np.allclose([x[0] for x in imp], [0.2, 1.4, 1.8, 3.0, 3.4]) and np.allclose([x[1] for x in imp], [18, -6, 3, -1, 0.5]),
      str([(round(a, 4), round(b, 4)) for a, b, _ in imp]))
nxt = [x for x in impulse_list(V_[:, 30], I_[:, 30], dtn) if x[0] >= 3.5][0]
check("E8 next impulse after the window: -1/6 at 4.6 us (so 14.5 holds on (3.4, 4.6))", np.isclose(nxt[0], 4.6) and np.isclose(nxt[1], -1 / 6))
Vst, Ist = char_solve(Z0, 25.0, 37.5, N, int(200 / dtn), lambda n: 24.0)
pl = [Vst[int(round(t / dtn)), 30] for t in (0.8, 1.6, 2.4, 3.2, 4.0)]
check("E9 step 24u(t) at 30 m: 18, 12, 15, 14, 14.5", np.allclose(pl, [18, 12, 15, 14, 14.5]), str(np.round(pl, 6)))
check("E10 steady state V_L = 14.4 V, I_L = 0.384 A (t = 200 us)", np.isclose(Vst[-1, N], 14.4, atol=1e-9) and
      np.isclose(Ist[-1, N], 0.384, atol=1e-9), f"{Vst[-1, N]:.9f} {Ist[-1, N]:.9f}")
check("E11 series check 18*(2/3)/(5/6) = 14.4", np.isclose(18 * (2 / 3) / (5 / 6), 14.4))
# FDTD with Gaussian, physical units
Nf = 1200; dzf = 0.1; dtf = dzf / v
sig = 0.004
Vg, Ig = fdtd(Z0, 25.0, 37.5, Nf, int(4.0 / dtf), lambda t: 24 * np.exp(-0.5 * ((t - 0.03) / sig) ** 2) / (sig * np.sqrt(2 * np.pi)), dtf)
tf = np.arange(Vg.shape[0]) * dtf
areas = []
for tc in (0.2, 1.4, 1.8, 3.0, 3.4):
    m = np.abs(tf - (tc + 0.03)) < 0.15
    areas.append(np.sum(Vg[m, 300]) * dtf)
check("E12 FDTD Gaussian (R_g = 25): areas at 30 m = 18, -6, 3, -1, 0.5 V.us (2e-2)", np.allclose(areas, [18, -6, 3, -1, .5], atol=2e-2),
      str(np.round(areas, 3)))
Vg, Ig = fdtd(Z0, 75.0, 37.5, Nf, int(4.0 / dtf), lambda t: 24 * np.exp(-0.5 * ((t - 0.03) / sig) ** 2) / (sig * np.sqrt(2 * np.pi)), dtf)
areas = []; aI = []
for tc in (0.2, 1.4, 1.8, 3.0, 3.4):
    m = np.abs(tf - (tc + 0.03)) < 0.15
    areas.append(np.sum(Vg[m, 300]) * dtf); aI.append(np.sum(Ig[m, 300]) * dtf)
check("E13 FDTD Gaussian (R_g = 75): 12, -4, then nothing; I areas 0.16, 0.0533",
      np.allclose(areas, [12, -4, 0, 0, 0], atol=2e-2) and np.allclose(aI[:2], [0.16, 4 / 75], atol=5e-4), f"{np.round(areas, 3)} {np.round(aI, 4)}")

print("=" * 100)
print("[F] Figures: figs_l28.py data vs lattice")
import figs_l28 as F
w6 = F.example_weights(6)
check("F1 example_weights = 3, -1.5, -0.75, 0.375, 0.1875, -0.09375", close(w6, [3, -1.5, -.75, .375, .1875, -.09375]))
N = 40
Vs_, _ = char_solve(F.Z0, F.RG, F.RL, N, 8 * N + 1, lambda n: F.V0)
ttT = (np.arange(8 * N + 1) + 0.5) / N         # mid-sample times avoid the step edges
Vh, Vl_ = F.step_curves(ttT)
check("F2 step_curves(z = l/2, l) = lattice staircase (t < 8T)", np.allclose(Vh, Vs_[:, N // 2]) and np.allclose(Vl_, Vs_[:, N]))
zp = 0.3
cr = [(k + zp) if k % 2 == 0 else (k + 1 - zp) for k in range(6)]
check("F3 bounce-diagram crossing times at z_p = 0.3l: 0.3, 1.7, 2.3, 3.7, 4.3, 5.7 T", close(cr, [.3, 1.7, 2.3, 3.7, 4.3, 5.7]))
labels = [(0, 0), (1, 0), (1, 1), (2, 1), (2, 2), (3, 2)]
okL = all(nL == (k + 1) // 2 and ng == k // 2 for k, (nL, ng) in enumerate(labels))
check("F4 bounce-diagram segment labels tau_g G_L^{(k+1)//2} G_g^{k//2}", okL)
print("=" * 100)
print(f"TOTAL PASS {NPASS}  FAIL {NFAIL}")
