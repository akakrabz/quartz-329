"""R30 -- independent checks for practice/30-multi-line-circuits.md.

Junctions: Gamma, tau by direct KVL/KCL linear solves (no Gamma formulas).
Bounce diagrams: own FDTD of the telegrapher's equations (magic time step,
Courant 1 on every line) with every resistor a lumped nodal element
(generator as Norton source, shunt/series/load resistors as conductances).
"""
import numpy as np
from scipy.sparse import lil_matrix, csc_matrix
from scipy.sparse.linalg import splu
from scipy.optimize import brentq, fsolve

NF = 0


def chk(name, got, want, tol=1e-6):
    global NF
    ok = abs(got - want) <= tol * max(1.0, abs(want))
    NF += (not ok)
    print(f"{'PASS' if ok else 'FAIL'}  {name}: computed {got:.6g}, page {want:.6g}")


def chkb(name, cond):
    global NF
    NF += (not cond)
    print(f"{'PASS' if cond else 'FAIL'}  {name}")


# ---------------- junction by direct KVL/KCL ----------------
def junction(Zj, Zk, shunt=None, series=0.0, branches=None):
    """Incident V+ = 1 from line j. Unknowns: Vm (reflected), Vpp (into k).
    Returns voltage/current ratios and power fractions."""
    br = branches if branches is not None else [Zk]
    if series == 0.0:
        # KVL: 1 + Vm = Vpp ; KCL: (1 - Vm)/Zj = Vpp*sum(1/Zb) + Vpp/R
        g = sum(1.0 / z for z in br) + (0.0 if shunt is None else 1.0 / shunt)
        A = np.array([[1.0, -1.0], [-1.0 / Zj, -g]])
        b = np.array([-1.0, -1.0 / Zj])
        Vm, Vpp = np.linalg.solve(A, b)
        I1 = (1 - Vm) / Zj
        P_in = 1.0 / Zj
        P_R = 0.0 if shunt is None else Vpp**2 / shunt / P_in
        P_br = [Vpp**2 / z / P_in for z in br]
    else:
        # line-1 side: V1 = 1+Vm, I = (1-Vm)/Zj ; series R: V1 - I*R = Vpp ; I = Vpp/Zk
        A = np.array([[1.0 + series / Zj, -1.0], [-1.0 / Zj, -1.0 / Zk]])
        b = np.array([series / Zj - 1.0, -1.0 / Zj])
        Vm, Vpp = np.linalg.solve(A, b)
        I1 = (1 - Vm) / Zj
        P_in = 1.0 / Zj
        P_R = I1**2 * series / P_in
        P_br = [Vpp**2 / Zk / P_in]
    return dict(G=Vm, tau=Vpp, Ir=-Vm / Zj / (1 / Zj), It=(Vpp / br[0]) / (1 / Zj),
                Pr=Vm**2, Pt=P_br, PR=P_R, I1=I1)


# ---------------- FDTD with lumped resistors ----------------
def fdtd(lines, Rg, RL, src, dt, tmax, junc=None, theta=0.5, probes=()):
    """lines: [(Z, T)] one-way delays; junc[k]: dict(shunt=R or None, series=R or 0)
    between line k and k+1. RL None = open. src(t) = open-circuit generator voltage.
    probes: list of (line k, fraction x) -> node; returns t, V, I (node current est.)."""
    junc = junc or [{}] * (len(lines) - 1)
    node_of = []          # per line: array of node indices
    nn = 0
    for k, (Z, T) in enumerate(lines):
        N = int(round(T / dt))
        assert abs(N * dt - T) < 1e-9
        if k == 0 or junc[k - 1].get('series', 0.0):
            idx = np.arange(nn, nn + N + 1); nn += N + 1
        else:
            first = node_of[-1][-1]
            idx = np.concatenate([[first], np.arange(nn, nn + N)]); nn += N
        node_of.append(idx)
    left = np.concatenate([n[:-1] for n in node_of])
    right = np.concatenate([n[1:] for n in node_of])
    Zc = np.concatenate([np.full(len(n) - 1, Z) for n, (Z, T) in zip(node_of, lines)])
    Cdt = np.bincount(left, 1 / (2 * Zc), nn) + np.bincount(right, 1 / (2 * Zc), nn)
    G = lil_matrix((nn, nn))
    g0 = node_of[0][0]; G[g0, g0] += 1 / Rg
    gl = node_of[-1][-1]
    if RL is not None:
        G[gl, gl] += 1 / RL
    for k, j in enumerate(junc):
        a, b = node_of[k][-1], node_of[k + 1][0]
        if j.get('shunt') is not None:
            G[a, a] += 1 / j['shunt']
        if j.get('series', 0.0):
            gs = 1 / j['series']
            G[a, a] += gs; G[b, b] += gs; G[a, b] -= gs; G[b, a] -= gs
    G = csc_matrix(G)
    from scipy.sparse import diags
    A = splu(csc_matrix(diags(Cdt) + theta * G))
    B = csc_matrix(diags(Cdt) - (1 - theta) * G)
    V = np.zeros(nn); I = np.zeros(len(Zc))
    pn = []
    for (k, x) in probes:
        n = node_of[k][int(round(x * (len(node_of[k]) - 1)))]
        # cell index adjacent (right if exists, else left) for current
        c = np.where(left == n)[0]
        c = c[0] if len(c) else np.where(right == n)[0][0]
        pn.append((n, c))
    nst = int(round(tmax / dt))
    tt = np.arange(nst + 1) * dt
    Vs = np.zeros((nst + 1, len(pn))); Is = np.zeros((nst + 1, len(pn)))
    Iprev = I.copy()
    for s in range(nst):
        Iprev = I.copy()
        I -= (V[right] - V[left]) / Zc
        inj = np.bincount(right, I, nn) - np.bincount(left, I, nn)
        J = np.zeros(nn)
        J[g0] = (theta * src(tt[s + 1]) + (1 - theta) * src(tt[s])) / Rg
        V = A.solve(B @ V + inj + J)
        for i, (n, c) in enumerate(pn):
            Vs[s + 1, i] = V[n]
            Is[s + 1, i] = I[c]   # at plateaus the half-step offset is irrelevant
    return tt, Vs, Is, (node_of, V, I)


def plateau(*ys):
    """mask of samples away from any front (half-step V/I offset)."""
    m = np.ones(len(ys[0]), bool)
    for y in ys:
        d = np.abs(np.diff(y))
        bad = np.zeros(len(y), bool)
        for k in range(-3, 4):
            bad |= np.roll(np.concatenate([[False], d > 1e-12]), k)
        m &= ~bad
    return m


def at(tt, y, t):
    return y[int(round(t / (tt[1] - tt[0])))]


step = lambda V0: (lambda t: V0 if t > 0 else 0.0)

# ======================= 30.1 =======================
print("== 30.1")
j = junction(50, 75); chk("G12", j['G'], 0.2); chk("tau12", j['tau'], 1.2)
chk("I refl ratio", j['Ir'], -0.2); chk("I trans ratio", j['It'], 0.8)
j = junction(75, 50); chk("G21", j['G'], -0.2); chk("tau21", j['tau'], 0.8)
chk("I refl ratio 21", j['Ir'], 0.2); chk("I trans ratio 21", j['It'], 1.2)
tt, Vs, Is, _ = fdtd([(50, 1.0), (75, 1.0)], 50, 75, step(20.0), 0.01, 3.0,
                     probes=[(0, 0.5), (1, 0.5)])
V1, I1 = at(tt, Vs[:, 0], 1.8), at(tt, Is[:, 0], 1.8)
Vb = (V1 - 50 * I1) / 2          # backward component on line 1
chk("sim V- (V)", Vb, 2.0); chk("sim I- (A)", -Vb / 50, -0.04)
chk("sim V++ (V)", at(tt, Vs[:, 1], 1.8), 12.0); chk("sim I++ (A)", at(tt, Is[:, 1], 1.8), 0.16)
chk("sim I line1 total", I1, 0.16)
chk("P in (W)", 10**2 / 50, 2.0); chk("P refl (W)", 2**2 / 50, 0.08); chk("P trans (W)", 12**2 / 75, 1.92)

# ======================= 30.2 =======================
print("== 30.2")
G = brentq(lambda g: (1 + g) - 4 / 3, -1, 1); Z2 = (1 + G) / (1 - G)  # Z2/Z1 from tau
j = junction(1.0, Z2); chk("(b) tau=4/3 -> Z2/Z1", Z2, 2.0); chk("(b) Pt", j['Pt'][0], 8 / 9)
jf, jb = junction(50, 80), junction(80, 50)
chk("(c) G21+G12", jf['G'] + jb['G'], 0.0); chk("(c) tau12+tau21", jf['tau'] + jb['tau'], 2.0)
j = junction(50, None, branches=[100, 100]); chk("(d) G", j['G'], 0.0); chk("(d) tau", j['tau'], 1.0)
chk("(d) power per branch", j['Pt'][0], 0.5)
j = junction(50, 75); chk("(e) It != tau", abs(j['It'] - j['tau']), 0.4)
tt, Vs, Is, _ = fdtd([(50, 1.0), (100, 0.5)], 50, None, step(10.0), 0.01, 2.5,
                     probes=[(1, 0.0)])
r = at(tt, Vs[:, 0], 1.5) / at(tt, Is[:, 0], 1.5)
chk("(f) V/I into open line 2 before echo", r, 100.0)

# ======================= 30.3 =======================
print("== 30.3")
def back_on_A(ZA, ZB, R, RL, Rg):
    tt, Vs, Is, _ = fdtd([(ZA, 1.0), (ZB, 0.7)], Rg, RL, step(1.0), 0.01, 12.0,
                         junc=[dict(shunt=R)], probes=[(0, 0.5)])
    m = plateau(Vs[:, 0], Is[:, 0])
    return np.max(np.abs((Vs[m, 0] - ZA * Is[m, 0]) / 2))
chkb("(d) RZB/(R+ZB)=ZA, RL=ZB, Rg mismatched -> no backward wave",
     back_on_A(50, 100, 100, 100, 20) < 1e-9)
chkb("(c) only (RL != ZB) -> backward wave appears", back_on_A(50, 100, 100, 300, 20) > 1e-3)
chkb("(b) ZB=ZA with R -> backward wave", back_on_A(50, 50, 100, 50, 20) > 1e-3)
chkb("(a) Rg=ZA only -> backward wave", back_on_A(50, 100, 300, 100, 50) > 1e-3)
Zp = 100 * 50 / 150
chk("(c) tau_BA = 2Z'/(Z'+ZB)", junction(100, 50, shunt=100)['tau'], 2 * Zp / (Zp + 100))

# ======================= 30.4 =======================
print("== 30.4")
L1, C1 = 1.0, 1.0; Z1, v1 = np.sqrt(L1 / C1), 1 / np.sqrt(L1 * C1)
sol = fsolve(lambda p: [np.sqrt(p[0] / p[1]) - Z1 / 2, 1 / np.sqrt(p[0] * p[1]) - v1 / 3], [1, 1])
chk("L2/L1", sol[0], 1.5); chk("C2/C1", sol[1], 6.0)
j = junction(1.0, 0.5); chk("G12", j['G'], -1 / 3); chk("tau12", j['tau'], 2 / 3)
chk("mu_r", sol[0] / L1, 1.5); chk("eps_r", sol[1] / C1, 6.0)

# ======================= 30.5 =======================
print("== 30.5")
j = junction(200, 50); chk("G21", j['G'], -0.6); chk("tau21", j['tau'], 0.4)
chk("into line 1 (V)", 25 * j['tau'], 10.0); chk("back to load (V)", 25 * j['G'], -15.0)
chk("I line-2 side", -25 / 200 + 25 * j['G'] / 200, -0.2); chk("I line-1 side", -25 * j['tau'] / 50, -0.2)
chk("student I line-2 side", -25 / 200 + 15 / 200, -0.05); chk("student I line-1 side", -40 / 50, -0.8)
tt, Vs, Is, _ = fdtd([(200, 1.0), (50, 1.0)], 200, 50, step(50.0), 0.01, 3.0, probes=[(0, 0.5), (1, 0.5)])
chk("sim transmitted (V)", at(tt, Vs[:, 1], 1.8), 10.0)
chk("sim reflected (V)", (at(tt, Vs[:, 0], 1.8) - 200 * at(tt, Is[:, 0], 1.8)) / 2, -15.0)

# ======================= 30.6 =======================
print("== 30.6")
R = brentq(lambda R: junction(50, 75, shunt=R)['G'], 60, 1e4); chk("R (ohm)", R, 150.0)
j = junction(50, 75, shunt=150); chk("tau12", j['tau'], 1.0)
chk("frac line 2", j['Pt'][0], 2 / 3); chk("frac R", j['PR'], 1 / 3)
j = junction(75, 50, shunt=150); chk("G21", j['G'], -1 / 3); chk("tau21", j['tau'], 2 / 3)
chk("refl frac", j['Pr'], 1 / 9); chk("line1 frac", j['Pt'][0], 2 / 3); chk("R frac", j['PR'], 2 / 9)
tt, Vs, Is, _ = fdtd([(75, 1.0), (50, 1.0)], 75, 50, step(2.0), 0.01, 3.0,
                     junc=[dict(shunt=150)], probes=[(0, 0.5), (1, 0.5)])
chk("sim G21", (at(tt, Vs[:, 0], 1.8) - 75 * at(tt, Is[:, 0], 1.8)) / 2, -1 / 3)
chk("sim tau21", at(tt, Vs[:, 1], 1.8), 2 / 3)
tt, Vs, Is, _ = fdtd([(50, 1.0), (75, 1.0)], 50, 75, step(2.0), 0.01, 3.0,
                     junc=[dict(shunt=150)], probes=[(0, 0.5), (1, 0.5)])
chk("sim G12 (shunt 150)", (at(tt, Vs[:, 0], 1.8) - 50 * at(tt, Is[:, 0], 1.8)) / 2, 0.0)

# ======================= 30.7 =======================
print("== 30.7")
j = junction(50, 75, series=25); chk("G12", j['G'], 1 / 3); chk("tau12", j['tau'], 1.0)
chk("refl", j['Pr'], 1 / 9); chk("trans", j['Pt'][0], 2 / 3); chk("R", j['PR'], 2 / 9)
chk("I line 1 = I line 2", j['I1'] * 50, 2 / 3)
j = junction(75, 50, series=25); chk("G21", j['G'], 0.0); chk("tau21", j['tau'], 2 / 3)
chk("R share of line-1 side V", 25 / (25 + 75), 0.25)
for (ZA, ZB, gw, tw) in [(50, 75, 1 / 3, 1.0), (75, 50, 0.0, 2 / 3)]:
    tt, Vs, Is, _ = fdtd([(ZA, 1.0), (ZB, 1.0)], ZA, ZB, step(2.0), 0.01, 3.0,
                         junc=[dict(series=25)], probes=[(0, 0.5), (1, 0.5)])
    chk(f"sim G from {ZA}", (at(tt, Vs[:, 0], 1.8) - ZA * at(tt, Is[:, 0], 1.8)) / 2, gw)
    chk(f"sim tau from {ZA}", at(tt, Vs[:, 1], 1.8), tw)

# ======================= 30.8 =======================
print("== 30.8")
chk("tau_g", 75 / 100, 0.75)
jg = junction(75, 25); chk("Gamma_g (KVL: 75-line into 25 ohm)", jg['G'], -0.5)
chk("G12", junction(75, 150)['G'], 1 / 3)
j23 = junction(150, 50); chk("current refl 2-3", j23['Ir'], 0.5)
tt, Vs, Is, _ = fdtd([(75, 2.0), (150, 1.0), (50, 3.0)], 25, 50, step(1.0), 0.01, 14.0,
                     probes=[(0, 0.0), (2, 1.0)])
s0 = Vs[:, 0]
chk("V(0) step 0<t<4", at(tt, s0, 2.0), 0.75)
chk("V(0) const until 4", at(tt, s0, 3.9) - at(tt, s0, 0.1), 0.0)
chk("impulse at 4 us", at(tt, s0, 5.0) - at(tt, s0, 3.0), 1 / 8)
chk("impulse at 6 us", at(tt, s0, 7.0) - at(tt, s0, 5.0), -1 / 6)
chk("nothing else before 8 us", at(tt, s0, 7.95) - at(tt, s0, 6.5), 0.0)
chkb("something at 8 us", abs(at(tt, s0, 8.5) - at(tt, s0, 7.5)) > 1e-3)
chk("load first impulse (t=6)", at(tt, Vs[:, 1], 6.5) - at(tt, Vs[:, 1], 5.5), 0.5)
chk("load nothing before 6", at(tt, Vs[:, 1], 5.9), 0.0)

# ======================= 30.9 =======================
print("== 30.9")
chk("tau_g", 150 / 200, 0.75); chk("Gamma_g", junction(150, 50)['G'], -0.5)
j = junction(150, 50); chk("G12", j['G'], -0.5); chk("tau12", j['tau'], 0.5)
chk("I refl", j['Ir'], 0.5); chk("I trans", j['It'], 1.5)
tt, Vs, Is, _ = fdtd([(150, 2.0), (50, 1.0)], 50, 50, step(80.0), 0.01, 60.0,
                     probes=[(0, 0.25), (1, 0.5), (1, 1.0)])
V, I = Vs[:, 0], Is[:, 0]
fw, bw = (V + 150 * I) / 2, (V - 150 * I) / 2
for (t1, t0, w, nm) in [(1, 0, 60, "launch"), (5, 4, 15, "gen echo 1"), (9, 8, 3.75, "gen echo 2")]:
    chk(f"fwd line1 {nm}", at(tt, fw, t1 - 0.0) - at(tt, fw, t0 + 0.0) if t0 == 0 else
        at(tt, fw, t1) - at(tt, fw, t0), w)
for (t1, t0, w) in [(4, 3, -30), (8, 7, -7.5), (12, 11, -1.875)]:
    chk(f"bwd line1 at {t0+0.5}", at(tt, bw, t1) - at(tt, bw, t0), w)
V2, I2 = Vs[:, 1], Is[:, 1]
for (t1, t0, w) in [(3, 2, 30), (7, 6, 7.5), (11, 10, 1.875)]:
    chk(f"line2 fwd at {t0+0.5}", at(tt, (V2 + 50 * I2) / 2, t1) - at(tt, (V2 + 50 * I2) / 2, t0), w)
m = plateau(V2, I2)
chk("line2 no backward (plateaus)", np.max(np.abs((V2[m] - 50 * I2[m]) / 2)), 0.0)
chk("V(100 m, 5 us)", at(tt, V, 5.0), 45.0); chk("I(100 m, 5 us)", at(tt, I, 5.0), 0.7)
VL = Vs[:, 2]
chk("VL t<3", at(tt, VL, 2.9), 0.0); chk("VL 3-7", at(tt, VL, 5.0), 30.0)
chk("VL 7-11", at(tt, VL, 10.0), 37.5); chk("VL(inf)", VL[-1], 40.0); chk("IL(inf)", Is[-1, 2], 0.8)
chk("line1 V(inf)", V[-1], 40.0); chk("line1 I(inf)", I[-1], 0.8)
chk("line1 fwd sum", fw[-1], 80.0); chk("line1 bwd sum", bw[-1], -40.0)

# ======================= 30.10 =======================
print("== 30.10")
d = 200 * 1.0 / 2; chk("splice d (m)", d, 100.0)
Z2 = brentq(lambda Z: junction(50, Z)['G'] - 3 / 9, 51, 1e4); chk("Z2", Z2, 100.0)
t12, t21 = junction(50, 100)['tau'], junction(100, 50)['tau']
GL = -8 / (9 * t12 * t21); chk("Gamma_L", GL, -1.0)
chk("air line (m)", 300 * (1.8 - 1.0) / 2, 120.0)
# forward-simulate deduced circuit: step response jumps = pulse heights
tt, Vs, Is, _ = fdtd([(50, 0.5), (100, 0.4)], 50, 1e-9, step(18.0), 0.001, 4.0,
                     theta=1.0, probes=[(0, 0.0)])
s = Vs[:, 0]
for (t, w) in [(0.0, 9), (1.0, 3), (1.8, -8), (2.6, -8 / 3), (3.4, -8 / 9)]:
    jmp = at(tt, s, t + 0.05) - (at(tt, s, t - 0.05) if t > 0 else 0.0)
    chk(f"scope pulse at {t} us (V)", jmp, w, 1e-4)
chk("nothing between pulses", at(tt, s, 1.75) - at(tt, s, 1.05), 0.0, 1e-4)
# direct 10 ns pulse
pulse = lambda t: 18.0 if 0 < t <= 0.010 else 0.0
tt, Vs, Is, _ = fdtd([(50, 0.5), (100, 0.4)], 50, 1e-9, pulse, 0.00025, 3.6,
                     theta=1.0, probes=[(0, 0.0)])
for (t, w) in [(0.0, 9), (1.0, 3), (1.8, -8), (2.6, -8 / 3), (3.4, -8 / 9)]:
    chk(f"direct pulse mid at {t}", at(tt, Vs[:, 0], t + 0.006), w, 1e-3)
tt, Vs, Is, _ = fdtd([(50, 0.5), (100, 0.4)], 25, 1e-9, step(18.0), 0.001, 1.5,
                     theta=1.0, probes=[(0, 0.0)])
chk("(e) launched (V)", at(tt, Vs[:, 0], 0.5), 12.0, 1e-4)
chk("(e) scope at 1.0 us (V)", at(tt, Vs[:, 0], 1.05) - at(tt, Vs[:, 0], 0.95), 8 / 3, 1e-4)

# ======================= 30.11 =======================
print("== 30.11")
j = junction(50, 50, shunt=50); chk("G12", j['G'], -1 / 3); chk("tau12", j['tau'], 2 / 3)
chk("Gamma_g", junction(50, 50)['G'], 0.0)
tt, Vs, Is, _ = fdtd([(50, 1.0), (50, 0.5)], 50, None, step(100.0), 0.005, 60.0,
                     junc=[dict(shunt=50)], probes=[(1, 0.0), (1, 1.0), (0, 0.5), (1, 0.5)])
VJ, Vo = Vs[:, 0], Vs[:, 1]
for (t, w) in [(0.5, 0), (1.5, 100 / 3), (2.5, 500 / 9), (3.5, 1300 / 27)]:
    chk(f"VJ at {t}", at(tt, VJ, t), w)
chk("I_R(2.5)", at(tt, VJ, 2.5) / 50, 10 / 9)
for (t, w) in [(2.0, 200 / 3), (3.0, 400 / 9), (4.0, 1400 / 27)]:
    chk(f"open end at {t}", at(tt, Vo, t), w)
chk("VJ(inf)", VJ[-1], 50.0); chk("open(inf)", Vo[-1], 50.0); chk("I_R(inf)", VJ[-1] / 50, 1.0)
V1, I1 = Vs[:, 2], Is[:, 2]; bw1 = (V1 - 50 * I1) / 2
chk("line1 launch (V)", at(tt, (V1 + 50 * I1) / 2, 0.75), 50.0)
for (t1, t0, w) in [(2, 1, -50 / 3), (3, 2, 200 / 9), (4, 3, -200 / 27)]:
    chk(f"line1 bwd jump at {t0+0.5}", at(tt, bw1, t1) - at(tt, bw1, t0), w)
V2, I2 = Vs[:, 3], Is[:, 3]; f2, b2 = (V2 + 50 * I2) / 2, (V2 - 50 * I2) / 2
for (t, w) in [(1.25, 100 / 3), (2.25, -100 / 9), (3.25, 100 / 27)]:
    chk(f"line2 fwd jump at {t}", at(tt, f2, t + 0.1) - at(tt, f2, t - 0.1), w)
for (t, w) in [(1.75, 100 / 3), (2.75, -100 / 9), (3.75, 100 / 27)]:
    chk(f"line2 bwd jump at {t}", at(tt, b2, t + 0.1) - at(tt, b2, t - 0.1), w)

# ======================= 30.12 =======================
print("== 30.12")
chk("tau_g", 50 / 200, 0.25); chk("Gamma_g", junction(50, 150)['G'], 0.5)
j = junction(50, 25); chk("G12", j['G'], -1 / 3); chk("tau12", j['tau'], 2 / 3)
chk("T1", 600 / 200, 3.0); chk("T2", 450 / 300, 1.5)
tt, Vs, Is, _ = fdtd([(50, 3.0), (25, 1.5)], 150, 25, step(1.0), 0.01, 20.0, probes=[(1, 1.0)])
h = Vs[:, 0]
for (t, w) in [(4.5, 1 / 6), (10.5, -1 / 36), (16.5, 1 / 216)]:
    chk(f"h_L weight at {t}", at(tt, h, t + 0.2) - at(tt, h, t - 0.2), w)
chk("h_L nothing else 5-10", at(tt, h, 10.3) - at(tt, h, 4.7), 0.0)
for f, want in [(1.0, 2.0), (1.25, 2.8)]:
    src = lambda t, f=f: 14 * np.sin(2 * np.pi * f * t) if t > 0 else 0.0
    tt, Vs, Is, _ = fdtd([(50, 3.0), (25, 1.5)], 150, 25, src, 0.0025, 90.0, probes=[(1, 1.0)])
    VL = Vs[:, 0]
    if f == 1.0:
        m1 = (tt > 4.6) & (tt < 10.4); m2 = (tt > 10.6) & (tt < 16.4)
        e1 = np.max(np.abs(VL[m1] + 7 / 3 * np.sin(2 * np.pi * tt[m1])))
        e2 = np.max(np.abs(VL[m2] + 35 / 18 * np.sin(2 * np.pi * tt[m2])))
        chk("(c) 4.5-10.5 max err vs -7/3 sin", e1, 0.0, 2e-3)
        chk("(c) 10.5-16.5 max err vs -35/18 sin", e2, 0.0, 2e-3)
        m3 = (tt > 16.6) & (tt < 22.4)
        chk("(check) third amplitude", np.max(np.abs(VL[m3])), 434 / 216, 2e-3)
        chk("wavelength line 1 (m)", 200 / f, 200.0); chk("wavelength line 2 (m)", 300 / f, 300.0)
    late = tt > 80
    chk(f"(d) settled amplitude at {f} MHz", np.max(np.abs(VL[late])), want, 2e-3)
chk("DC divider", 14 * 25 / 175, 2.0)

print(f"\n{NF} FAIL(s)")
