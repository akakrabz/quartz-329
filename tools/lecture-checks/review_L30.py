#!/usr/bin/env python3
"""Independent review checks for Lecture 30 (multi-line circuits) and its worked problem.

Two independent simulators:
  * LAT: exact characteristic-lattice bookkeeping (forward/backward samples shifted one cell per step,
    Courant 1 on every line); every end/junction solved from its KVL/KCL with np.linalg.solve,
    never from a Gamma/tau formula.
  * FDTD: Yee leapfrog of the telegrapher's equations (V nodes, I half-nodes), lumped half-cell
    capacitances at the ends and the junction; no wave decomposition at all.
Every number on the page / problem / figures is compared; PASS/FAIL printed per item.
"""
import numpy as np, sys, importlib

np.random.seed(30)
NF = 0
def chk(name, got, want, tol=1e-9):
    global NF
    got = np.asarray(got, float); want = np.asarray(want, float)
    ok = np.allclose(got, want, rtol=tol, atol=tol)
    if not ok: NF += 1
    print(f"{'PASS' if ok else 'FAIL'}  {name}: got {np.round(got, 6).tolist()} want {np.round(want, 6).tolist()}")
    return ok

def tru(name, cond):
    global NF
    if not cond: NF += 1
    print(f"{'PASS' if cond else 'FAIL'}  {name}")

# ---------------------------------------------------------------------------------------- junction solvers
def solve_junction(kind, Z1, Z2, R=None, a1=1.0, b2=0.0):
    """incoming a1 (on line 1, rightward) and b2 (on line 2, leftward) -> outgoing b1, a2 (+ resistor current)."""
    if kind == "direct":
        # a1+b1 = a2+b2 ; (a1-b1)/Z1 = (a2-b2)/Z2
        A = np.array([[1, -1], [-1 / Z1, -1 / Z2]]); rhs = np.array([b2 - a1, -a1 / Z1 - b2 / Z2])
    elif kind == "shunt":
        # a1+b1 = a2+b2 ; (a1-b1)/Z1 = (a2-b2)/Z2 + (a2+b2)/R
        A = np.array([[1, -1], [-1 / Z1, -1 / Z2 - 1 / R]]); rhs = np.array([b2 - a1, -a1 / Z1 - b2 / Z2 + b2 / R])
    elif kind == "series":
        # (a1+b1) - (a2+b2) = R (a1-b1)/Z1 ; (a1-b1)/Z1 = (a2-b2)/Z2
        A = np.array([[1 + R / Z1, -1], [-1 / Z1, -1 / Z2]]); rhs = np.array([b2 - a1 + R * a1 / Z1, -a1 / Z1 - b2 / Z2])
    b1, a2 = np.linalg.solve(A, rhs)
    return b1, a2

print("== A. junction coefficients (Sec. 1) ==")
for trial in range(5):
    Zj, Zk = np.random.uniform(5, 300, 2)
    b1, a2 = solve_junction("direct", Zj, Zk)
    G = (Zk - Zj) / (Zk + Zj)
    chk(f"Gamma_jk, tau_jk = 1+G = 2Zk/(Zk+Zj)  (Zj={Zj:.1f}, Zk={Zk:.1f})", [b1, a2, a2], [G, 1 + G, 2 * Zk / (Zk + Zj)])
    # reverse direction: wave from k into j
    a1r, b2r = 0.0, 1.0
    b1r, a2r = solve_junction("direct", Zj, Zk, a1=0.0, b2=1.0)   # b1r = transmitted into j, a2r = reflected on k
    chk("  Gamma_kj = -Gamma_jk, tau_kj = 1-Gamma_jk", [a2r, b1r], [-G, 1 - G])
    # currents: incident a1/Zj; reflected -b1/Zj; transmitted a2/Zk
    chk("  current refl -G, current trans 1-G = tau Zj/Zk", [(-b1 / Zj) / (1 / Zj), (a2 / Zk) / (1 / Zj), (1 + G) * Zj / Zk], [-G, 1 - G, 1 - G])
    # power: incident 1/Zj, reflected b1^2/Zj, transmitted a2^2/Zk
    chk("  power G^2 + tau^2 Zj/Zk = 1", [b1 ** 2 + a2 ** 2 * Zj / Zk], [1.0])
tru("tau>1 iff Zk>Zj (Zk=2Zj gives 4/3)", solve_junction("direct", 1, 2)[1] > 1 and solve_junction("direct", 2, 1)[1] < 1)
chk("Zk = Zj: no reflection", [solve_junction("direct", 50, 50)[0]], [0.0])
chk("Gamma_jk equals Lecture 28 Gamma_L with R_L -> Z_k (a resistor Zk)", [solve_junction("shunt", 30, 1e15, R=90)[0]], [(90 - 30) / 120], 1e-9)

print("\n== B. resistive junctions (Sec. 4) ==")
for trial in range(4):
    Z1, Z2, R = np.random.uniform(5, 300, 3)
    b1, a2 = solve_junction("shunt", Z1, Z2, R)
    Zeq = R * Z2 / (R + Z2)
    G = (Zeq - Z1) / (Zeq + Z1)
    chk(f"shunt: G12, tau12=1+G=2Zeq/(Zeq+Z1) (Z1={Z1:.0f},Z2={Z2:.0f},R={R:.0f})", [b1, a2, a2], [G, 1 + G, 2 * Zeq / (Zeq + Z1)])
    b1r, a2r = solve_junction("shunt", Z1, Z2, R, a1=0, b2=1)
    Zeq2 = R * Z1 / (R + Z1); G21 = (Zeq2 - Z2) / (Zeq2 + Z2)
    chk("  shunt from the right: G21 with R||Z1, tau21 = 1+G21 = 2Zeq/(Zeq+Z2)", [a2r, b1r, b1r], [G21, 1 + G21, 2 * Zeq2 / (Zeq2 + Z2)])
    b1, a2 = solve_junction("series", Z1, Z2, R)
    G = (R + Z2 - Z1) / (R + Z2 + Z1)
    chk("series: G12 with R+Z2; tau12 = (1+G)Z2/(R+Z2) = 2Z2/(R+Z1+Z2)", [b1, a2, a2], [G, (1 + G) * Z2 / (R + Z2), 2 * Z2 / (R + Z1 + Z2)])
    tru("  series: tau12 != 1+G12", abs(a2 - (1 + G)) > 1e-6)
    # power balance with resistor: refl + into line 2 < 1
    b1s, a2s = solve_junction("shunt", Z1, Z2, R)
    tru("  with R: G^2 + P2/Pinc < 1 (shunt and series)", b1s ** 2 + a2s ** 2 * Z1 / Z2 < 1 and b1 ** 2 + a2 ** 2 * Z1 / Z2 < 1)
chk("shunt R->inf recovers direct", list(solve_junction("shunt", 40, 70, 1e14)), list(solve_junction("direct", 40, 70)), 1e-9)
chk("shunt R->0: G=-1, tau=0", list(solve_junction("shunt", 40, 70, 1e-12)), [-1, 0], 1e-9)
# three equal lines: arriving line 1 sees lines 2 and 3 in parallel; solve KCL with 3 unknowns
Z0 = 75.0
# unknowns b1, a2, a3: V = 1+b1 = a2 = a3 ; (1-b1)/Z0 = a2/Z0 + a3/Z0
A = np.array([[1, -1, 0], [1, 0, -1], [-1 / Z0, -1 / Z0, -1 / Z0]]); rhs = np.array([-1, -1, -1 / Z0])
b1, a2, a3 = np.linalg.solve(A, rhs)
chk("three equal lines: G=-1/3, tau=2/3 into each branch", [b1, a2, a3], [-1 / 3, 2 / 3, 2 / 3])
b1, a2 = solve_junction("shunt", 25, 50, 50)
chk("shunt matching example: Zeq = 25, G=0, tau=1", [50 * 50 / 100, b1, a2], [25, 0, 1])
Pinc = 1 / 25; P2 = a2 ** 2 / 50; PR = (1 + b1) ** 2 / 50
chk("  line 2 gets half, R burns half, 3.01 dB", [P2 / Pinc, PR / Pinc, 10 * np.log10(Pinc / P2)], [0.5, 0.5, 3.0103], 1e-4)

# ---------------------------------------------------------------------------------------- simulators
class Lattice:
    """lines: list of (Z, ncell); dt common; junction kinds between consecutive lines."""
    def __init__(self, lines, Rg, RL, juncs, f):
        self.lines = lines; self.Rg = Rg; self.RL = RL; self.juncs = juncs; self.f = f
        self.fw = [np.zeros(n + 1) for _, n in lines]; self.bw = [np.zeros(n + 1) for _, n in lines]
    def step(self, m):
        L = self.lines
        for k in range(len(L)):
            self.fw[k][1:] = self.fw[k][:-1].copy(); self.bw[k][:-1] = self.bw[k][1:].copy()
        Z1 = L[0][0]; b = self.bw[0][0]
        # generator: f = Rg (a-b)/Z1 + a + b  -> solve for a
        A = np.array([[self.Rg / Z1 + 1]]); rhs = np.array([self.f(m) - b * (1 - self.Rg / Z1)])
        self.fw[0][0] = np.linalg.solve(A, rhs)[0]
        for k, (kind, R) in enumerate(self.juncs):
            Za, Zb = L[k][0], L[k + 1][0]
            b1, a2 = solve_junction(kind, Za, Zb, R, a1=self.fw[k][-1], b2=self.bw[k + 1][0])
            self.bw[k][-1] = b1; self.fw[k + 1][0] = a2
        ZN = L[-1][0]; a = self.fw[-1][-1]
        # load: a+b = RL (a-b)/ZN
        if np.isinf(self.RL):
            self.bw[-1][-1] = a
        else:
            A = np.array([[1 + self.RL / ZN]]); rhs = np.array([a * (self.RL / ZN - 1)])
            self.bw[-1][-1] = np.linalg.solve(A, rhs)[0]
    def VI(self, k, i):
        Z = self.lines[k][0]
        return self.fw[k][i] + self.bw[k][i], (self.fw[k][i] - self.bw[k][i]) / Z
    def fb(self, k, i):
        return self.fw[k][i], self.bw[k][i]


def fdtd_two_line(Z1, v1, len1, Z2, v2, len2, Rg, RL, f, dt, tmax, probes, Rshunt=np.inf, cour=0.5):
    """Yee scheme; dz = v dt / cour on each line (Courant 1 excites the odd-even mode at lumped ends). probes: list of z; returns t, V[z], I[z] (I at nearest half node)."""
    dz1, dz2 = v1 * dt / cour, v2 * dt / cour
    n1, n2 = int(round(len1 / dz1)), int(round(len2 / dz2))
    Lp1, Cp1, Lp2, Cp2 = Z1 / v1, 1 / (Z1 * v1), Z2 / v2, 1 / (Z2 * v2)
    N = n1 + n2
    zV = np.concatenate([np.arange(n1 + 1) * dz1, len1 + np.arange(1, n2 + 1) * dz2])
    zI = np.concatenate([(np.arange(n1) + 0.5) * dz1, len1 + (np.arange(n2) + 0.5) * dz2])
    Cn = np.zeros(N + 1); Cn[:n1 + 1] += Cp1 * dz1; Cn[n1:] += Cp2 * dz2
    Cn[0] -= Cp1 * dz1 / 2; Cn[n1] -= (Cp1 * dz1 + Cp2 * dz2) / 2; Cn[N] -= Cp2 * dz2 / 2
    Lc = np.concatenate([np.full(n1, Lp1 * dz1), np.full(n2, Lp2 * dz2)])
    V = np.zeros(N + 1); I = np.zeros(N)
    iv = [int(np.argmin(abs(zV - z))) for z in probes]; ii = [int(np.argmin(abs(zI - z))) for z in probes]
    nst = int(round(tmax / dt)); T = []; PV = []; PI = []; snaps = {}
    for m in range(nst + 1):
        t = m * dt
        T.append(t); PV.append(V[iv].copy()); PI.append(I[ii].copy())
        # I at t+dt/2
        I -= dt / Lc * (V[1:] - V[:-1])
        # V at t+dt (semi-implicit lumped terms)
        dI = np.zeros(N + 1); dI[1:] += I; dI[:-1] -= I            # current into node
        fs = f(t + dt / 2)
        Vn = V + dt / np.where(Cn > 0, Cn, 1) * dI
        # node 0: Cn dV/dt = (fs - Vavg)/Rg + dI
        c, g = Cn[0] / dt, 1 / Rg
        Vn[0] = (c * V[0] + fs * g - g * V[0] / 2 + dI[0]) / (c + g / 2)
        if np.isfinite(RL):
            c, g = Cn[N] / dt, 1 / RL
            Vn[N] = (c * V[N] - g * V[N] / 2 + dI[N]) / (c + g / 2)
        if np.isfinite(Rshunt):
            c, g = Cn[n1] / dt, 1 / Rshunt
            Vn[n1] = (c * V[n1] - g * V[n1] / 2 + dI[n1]) / (c + g / 2)
        V = Vn
    return np.array(T), np.array(PV), np.array(PI), zV, V

# ---------------------------------------------------------------------------------------- C. the notes' circuit
print("\n== C. notes' circuit (Sec. 2-3): Z1=25, Rg=50, Z2=50, RL=50, v1=150, v2=300 m/us, l=2400 m ==")
Z1, Z2, Rg, RL = 25.0, 50.0, 50.0, 50.0
dt = 0.02                        # us
n1, n2 = int(8 / dt), int(4 / dt)  # T1=8 us, T2=4 us
dz1, dz2 = 150 * dt, 300 * dt
def zidx(z):
    return (0, int(round(z / dz1))) if z <= 1200 else (1, int(round((z - 1200) / dz2)))
# discrete impulse
lat = Lattice([(Z1, n1), (Z2, n2)], Rg, RL, [("direct", None)], lambda m: 1.0 if m == 0 else 0.0)
probes = [300.0, 600.0, 1050.0, 1500.0, 1800.0, 2400.0]
NT = int(70 / dt)
rec = {z: [] for z in probes}
recI = {z: [] for z in probes}
full = []
for m in range(NT + 1):
    lat.step(m)
    for z in probes:
        k, i = zidx(z); v, cur = lat.VI(k, i); rec[z].append(v); recI[z].append(cur)
tt = np.arange(NT + 1) * dt
def imp_at(z, t):
    m = int(round(t / dt)); return rec[z][m], recI[z][m]
# weights at segment midpoints of fig mline-bounce: (za,ta,zb,tb,w)
segs = [(0, 0, 1200, 8, 1 / 3), (1200, 8, 0, 16, 1 / 9), (1200, 8, 2400, 12, 4 / 9), (0, 16, 1200, 24, 1 / 27),
        (1200, 24, 0, 32, 1 / 81), (1200, 24, 2400, 28, 4 / 81)]
for za, ta, zb, tb, w in segs:
    zm, tm = (za + zb) / 2, (ta + tb) / 2
    lt = Lattice([(Z1, n1), (Z2, n2)], Rg, RL, [("direct", None)], lambda m: 1.0 if m == 0 else 0.0)
    mm = int(round(tm / dt))
    for m in range(mm + 1): lt.step(m)
    k, i = zidx(zm)
    chk(f"fig mline-bounce segment ({za},{ta})->({zb},{tb}) weight", [lt.VI(k, i)[0]], [w])
# impulse response formula (key callout) against lattice at all probes / times
def formula_V(z, t, Z1=25.0, Z2=50.0):
    T1 = 8.0; v1, v2 = 150.0, 300.0
    terms = []  # (time, Vweight, Iweight)
    for n in range(10):
        if z < 1200:
            terms.append((z / v1 + 2 * n * T1, (1 / 3) / 9 ** n, (1 / 3) / 9 ** n / Z1))
            terms.append((-z / v1 + 2 * (n + 1) * T1, (1 / 9) / 9 ** n, -(1 / 9) / 9 ** n / Z1))
        else:
            tz = T1 + (z - 1200) / v2
            terms.append((tz + 2 * n * T1, (4 / 9) / 9 ** n, (4 / 9) / 9 ** n / Z2))
            # notes' form of the delay
            assert abs((tz + 2 * n * T1) - (z / v2 + (4 * n + 1) * 1200 / v2)) < 1e-12
    return terms
maxdev = 0.0; maxdevI = 0.0
for z in probes[:-1]:
    Vf = np.zeros(NT + 1); If = np.zeros(NT + 1)
    for t0, wv, wi in formula_V(z, 0):
        m = int(round(t0 / dt))
        if m <= NT: Vf[m] += wv; If[m] += wi
    maxdev = max(maxdev, np.max(abs(Vf - np.array(rec[z])))); maxdevI = max(maxdevI, np.max(abs(If - np.array(recI[z]))))
chk("impulse-response key (V, all probes, 0-70 us) vs lattice: max deviation", [maxdev], [0.0], 1e-12)
chk("impulse-response key (I with -second sum, /Z1 or /Z2) vs lattice", [maxdevI], [0.0], 1e-12)
chk("notes' delay z/v2+(4n+1)(l/2)/v2 equals t_z+2nT1 (asserted for n<10)", [1], [1])
# coefficient numbers
chk("tau_g, Gamma_g, Gamma_12, tau_12, Gamma_L (notes' circuit)",
    [Z1 / (Rg + Z1), (Rg - Z1) / (Rg + Z1), *solve_junction("direct", Z1, Z2), (RL - Z2) / (RL + Z2)],
    [1 / 3, 1 / 3, 1 / 3, 4 / 3, 0])
chk("unused Gamma_21, tau_21", list(solve_junction("direct", Z1, Z2, a1=0, b2=1))[::-1], [-1 / 3, 2 / 3])
chk("T1 = (l/2)/v1, T2 = (l/2)/v2 = T1/2, 2T1", [1200 / 150, 1200 / 300, 2400 / 150], [8, 4, 16])
# step response: DC check
lat = Lattice([(Z1, n1), (Z2, n2)], Rg, RL, [("direct", None)], lambda m: 1.0)
for m in range(int(400 / dt)): lat.step(m)
k, i = zidx(600); f_, b_ = lat.fb(k, i); v600, i600 = lat.VI(k, i)
k, i = zidx(1800); v1800, i1800 = lat.VI(k, i)
chk("step DC: line-1 forward total 3/8, backward 1/8, V=1/2 everywhere", [f_, b_, v600, v1800], [3 / 8, 1 / 8, 0.5, 0.5], 1e-9)
chk("step DC: I = 1/(Rg+RL) = 1/100 A per volt on both lines", [i600, i1800], [1 / 100, 1 / 100], 1e-9)
chk("line-2 sum 4/9/(1-1/9), divider RL/(Rg+RL)", [4 / 9 / (1 - 1 / 9), RL / (Rg + RL)], [0.5, 0.5])
# FDTD of the same circuit, step input, Courant 1
ramp = lambda t, w: 0.0 if t <= 0 else (1.0 if t >= w else 0.5 - 0.5 * np.cos(np.pi * t / w))
T, PV, PI, zV, Vend = fdtd_two_line(25, 150, 1200, 50, 300, 1200, 50, 50, lambda t: ramp(t, 0.3), 0.01, 120, [600, 1800])
def at(arr, t): return arr[int(round(t / 0.01))]
chk("FDTD step at z=600: 1/3 (t=6), 4/9 (t=14), 4/9+1/27 (t=22), DC 1/2 (t=120)",
    [at(PV, 6)[0], at(PV, 14)[0], at(PV, 22)[0], at(PV, 120)[0]], [1 / 3, 4 / 9, 4 / 9 + 1 / 27, 0.5], 2e-3)
chk("FDTD step at z=1800: 0 (t=9), 4/9 (t=12), 4/9+4/81 (t=28), DC 1/2",
    [at(PV, 9)[1], at(PV, 12)[1], at(PV, 28)[1], at(PV, 120)[1]], [0, 4 / 9, 4 / 9 + 4 / 81, 0.5], 2e-3)
chk("FDTD step currents at z=600 t=6 (1/3/25) and t=14 ((1/3-1/9)/25)", [at(PI, 6)[0], at(PI, 14)[0]], [1 / 75, (1 / 3 - 1 / 9) / 25], 2e-3)

# ---------------------------------------------------------------------------------------- D. Example 2 (sine)
print("\n== D. Example 2: f = sin(2 pi t)u(t), t in us ==")
dt = 0.01; n1, n2 = 800, 400; dz1, dz2 = 1.5, 3.0
lat = Lattice([(Z1, n1), (Z2, n2)], Rg, RL, [("direct", None)], lambda m: np.sin(2 * np.pi * m * dt))
z1 = np.arange(n1 + 1) * dz1; z2 = 1200 + np.arange(n2 + 1) * dz2
want_t = {6.0: None, 12.0: None, 48.5: None}
late = []
sys.path.insert(0, "/home/claude/work")
import figs_l30 as F   # the figure's own curve function, to compare against
for m in range(int(120 / dt) + 1):
    lat.step(m)
    t = round(m * dt, 6)
    if t in want_t:
        V1 = lat.fw[0] + lat.bw[0]; V2 = lat.fw[1] + lat.bw[1]
        want_t[t] = (V1.copy(), V2.copy(), lat.fw[0].copy(), lat.bw[0].copy())
    if t >= 100 and t < 101:
        late.append((t, lat.fw[0] + lat.bw[0], lat.fw[1] + lat.bw[1], lat.fw[0].copy(), lat.bw[0].copy()))
for t, (V1, V2, fw1, bw1) in want_t.items():
    dev = max(np.max(abs(V1 - F.V_ex2(z1, t))), np.max(abs(V2[1:] - F.V_ex2(z2[1:], t))))
    chk(f"fig mline-burst curve at t={t} vs lattice (max dev)", [dev], [0], 1e-9)
V1, V2, fw1, bw1 = want_t[6.0]
front = z1[np.nonzero(abs(V1) > 1e-12)[0].max()]
chk("t=6: front at 900 m (last nonzero sample)", [front], [900], 2e-3)
V1, V2, fw1, bw1 = want_t[12.0]
chk("t=12: line-2 amplitude 4/9; front at the load", [np.max(abs(V2)), np.nonzero(abs(V2) > 1e-9)[0].max() * 3 + 1200], [4 / 9, 2400], 2e-3)
nzb = z1[np.nonzero(abs(bw1) > 1e-12)[0]]
chk("t=12: 1/9 echo occupies 600..1200 m with amplitude 1/9; forward 1/3", [nzb.min(), nzb.max(), np.max(abs(bw1)), np.max(abs(fw1))], [600, 1200, 1 / 9, 1 / 3], 3e-3)
# wavelengths from zero crossings of snapshots at 48.5
V1, V2, _, _ = want_t[48.5]
def wl(z, v):
    s = np.nonzero(np.diff(np.sign(v[1:-1])) != 0)[0]
    return 2 * np.mean(np.diff(z[1:-1][s]))
chk("wavelengths 150 m and 300 m", [wl(z1, V1), wl(z2, V2)], [150, 300], 1e-2)
chk("t=48.5: line 1 ~ 1/4 sin(2 pi z/150), line 2 ~ 1/2 sin(2 pi (z-1200)/300) (max dev < 3e-3)",
    [np.max(abs(V1 - 0.25 * np.sin(2 * np.pi * z1 / 150))) < 3e-3, np.max(abs(V2 - 0.5 * np.sin(2 * np.pi * (z2 - 1200) / 300))) < 3e-3], [1, 1])
amps1 = [np.max(abs(v1[10:-10])) for (_, v1, _, _, _) in late]
amps2 = [np.max(abs(v2[1:])) for (_, _, v2, _, _) in late]
fwa = [np.max(abs(f)) for (_, _, _, f, _) in late]; bwa = [np.max(abs(b)) for (_, _, _, _, b) in late]
chk("late (100-101 us): line-1 snapshot amplitude spans [1/4, 1/2]", [min(amps1), max(amps1)], [0.25, 0.5], 2e-3)
chk("late: line-2 amplitude 1/2; line-1 forward 3/8, backward 1/8", [np.mean(amps2), np.mean(fwa), np.mean(bwa)], [0.5, 3 / 8, 1 / 8], 1e-3)
i_half = [a for (t, *_), a in zip(late, amps1) if abs(t - 100.5) < 1e-9][0]
chk("late: line-1 amplitude 1/4 at a half-integer microsecond", [i_half], [0.25], 1e-3)
chk("errata: front at 3 us is at 450 m", [150 * 3], [450])
chk("Example 2 timing: T1, T2, 2T1 (us)", [1200 / 150, 1200 / 300, 16], [8, 4, 16])

# ---------------------------------------------------------------------------------------- E. Example 1
print("\n== E. Example 1 and its dielectric realization ==")
L1, C1 = 3.1e-7, 4.7e-10
L2, C2 = L1, C1 / 4
chk("L2=L1, C2=C1/4 gives Z2=2Z1 and v2=2v1", [np.sqrt(L2 / C2) / np.sqrt(L1 / C1), (1 / np.sqrt(L2 * C2)) / (1 / np.sqrt(L1 * C1))], [2, 2])
mu0, eps0 = 4e-7 * np.pi, 8.854187817e-12
a, b = 0.5e-3, 1.75e-3
def coax(er):
    L = mu0 / (2 * np.pi) * np.log(b / a); C = 2 * np.pi * er * eps0 / np.log(b / a)
    return L, C, np.sqrt(L / C), 1 / np.sqrt(L * C)
La, Ca, Za, va = coax(4.0); Lb, Cb, Zb, vb = coax(1.0)
chk("coax eps_r=4 (line 1) vs air (line 2): L same, C/4, Z x2, v x2; v1 = c/2 = 150 m/us",
    [Lb / La, Cb / Ca, Zb / Za, vb / va, va / 1e6], [1, 0.25, 2, 2, 149.896], 1e-4)

# ---------------------------------------------------------------------------------------- F. resistive junction by simulation
print("\n== F. resistive junctions by lattice simulation ==")
for kind, R in (("shunt", 80.0), ("series", 35.0), ("shunt", 50.0)):
    Za, Zb = 25.0, 50.0
    lt = Lattice([(Za, 100), (Zb, 100)], Za, Zb, [(kind, R)], lambda m: 2.0 if m == 0 else 0.0)  # matched ends, V+ = 1
    for m in range(151): lt.step(m)
    refl = lt.bw[0][50]; trans = lt.fw[1][50]
    if kind == "shunt":
        Zeq = R * Zb / (R + Zb); G = (Zeq - Za) / (Zeq + Za); tau = 1 + G
    else:
        G = (R + Zb - Za) / (R + Zb + Za); tau = (1 + G) * Zb / (R + Zb)
    chk(f"{kind} R={R}: simulated reflected / transmitted pulse vs page formula", [refl, trans], [G, tau])

# ---------------------------------------------------------------------------------------- G. worked problem
print("\n== G. worked problem: 120u(t), Rg=60, Z1=60 (300 m, 2e8), Z2=180 (300 m, 3e8), RL=540 ==")
def run_problem(RL, tmax=40.0, dt=0.01, kind="step"):
    n1, n2 = int(round(1.5 / dt)), int(round(1.0 / dt))
    f = (lambda m: 120.0) if kind == "step" else (lambda m: 120.0 if m == 0 else 0.0)
    lt = Lattice([(60.0, n1), (180.0, n2)], 60.0, RL, [("direct", None)], f)
    out = []
    for m in range(int(round(tmax / dt)) + 1):
        lt.step(m)
        out.append((lt.VI(0, int(round(150 / 2.0))), lt.VI(1, n2), [lt.fw[0].copy(), lt.bw[0].copy(), lt.fw[1].copy(), lt.bw[1].copy()] if kind != "step" else None))
    return out
dtp = 0.01
chk("(a) tau_g, Gamma_g, Gamma_L", [60 / 120, 0, (540 - 180) / 720], [0.5, 0, 0.5])
b1, a2 = solve_junction("direct", 60, 180); b1r, a2r = solve_junction("direct", 60, 180, a1=0, b2=1)
chk("(a) G12, tau12, G21, tau21", [b1, a2, a2r, b1r], [0.5, 1.5, -0.5, 0.5])
chk("(a) current coefficients right: -1/2, 1/2; left: +1/2, 3/2", [-b1, a2 * 60 / 180, -a2r, b1r * 180 / 60], [-0.5, 0.5, 0.5, 1.5])
chk("(a) T1, T2 (us)", [300 / 2e8 * 1e6, 300 / 3e8 * 1e6], [1.5, 1.0])
out = run_problem(540.0)
def P(t, which):  # which 0: (V,I) at 150 m, 1: load (V,I)
    return out[int(round(t / dtp))][which]
tmid = [0.4, 1.5, 3.0, 5.0, 7.0]
chk("(c) V(150 m) on 0-0.75, 0.75-2.25, 2.25-4.25, 4.25-6.25, 6.25-8.25", [P(t, 0)[0] for t in tmid], [0, 60, 90, 112.5, 106.875])
chk("(c) I(150 m) same intervals (A)", [P(t, 0)[1] for t in tmid], [0, 1, 0.5, 0.125, 0.21875])
chk("(c) last interval holds until 8.25: V at 8.2", [P(8.2, 0)[0]], [106.875])
chk("(d) V_L at 2.0, 3.5, 5.5, 7.5 us", [P(t, 1)[0] for t in (2.0, 3.5, 5.5, 7.5)], [0, 135, 101.25, 109.6875])
chk("(d) V_L jumps at 2.5/4.5/6.5 (just before/after)", [P(2.49, 1)[0], P(2.51, 1)[0], P(4.49, 1)[0], P(4.51, 1)[0], P(6.51, 1)[0]], [0, 135, 135, 101.25, 109.6875])
chk("(d) DC: V_L -> 108 V, I -> 0.2 A (t=40 us), V(150 m) -> 108", [P(40, 1)[0], P(40, 1)[1], P(40, 0)[0], P(40, 0)[1]], [108, 0.2, 108, 0.2], 1e-6)
chk("(d) 135/(1+1/4), lumped 120*540/600, 60+30+22.5/(1+1/4)", [135 / 1.25, 120 * 540 / 600, 60 + 30 + 22.5 / 1.25], [108, 108, 108])
# figure segments: impulse of 120 V (each segment's weight in volts at its midpoint)
outi = run_problem(540.0, tmax=8.0, kind="impulse")
psegs = [(0, 0, 300, 1.5, 60), (300, 1.5, 0, 3.0, 30), (300, 1.5, 600, 2.5, 90), (600, 2.5, 300, 3.5, 45),
         (300, 3.5, 600, 4.5, -22.5), (300, 3.5, 0, 5.0, 22.5), (600, 4.5, 300, 5.5, -11.25), (300, 5.5, 600, 6.5, 5.625),
         (300, 5.5, 0, 7.0, -5.625), (600, 6.5, 300, 7.5, 2.8125)]
for za, ta, zb, tb, w in psegs:
    zm, tm = (za + zb) / 2, (ta + tb) / 2
    fw1, bw1, fw2, bw2 = outi[int(round(tm / dtp))][2]
    if zm <= 300:
        i = int(round(zm / 2.0)); v = fw1[i] + bw1[i]
    else:
        i = int(round((zm - 300) / 3.0)); v = fw2[i] + bw2[i]
    chk(f"fig problem-bounce segment ({za},{ta})->({zb},{tb})", [v], [w])
# segments starting at 7.5 us that the 0-8 us window contains
fw1, bw1, fw2, bw2 = outi[int(round(7.75 / dtp))][2]
chk("segments leaving the junction at 7.5 us (in window): -1.40625 toward load, +1.40625 into line 1",
    [fw2[int(round(75 / 3.0))] + bw2[int(round(75 / 3.0))], fw1[int(round(250 / 2.0))] + bw1[int(round(250 / 2.0))]], [-1.40625, 1.40625])
# (e)
oute = run_problem(180.0, tmax=10)
chk("(e) RL=180: V_L = 90 from 2.5 us on (t=2.6, 9)", [oute[260][1][0], oute[900][1][0]], [90, 90])
chk("(e) lumped 120*180/240", [120 * 180 / 240], [90])
# line 1 settles at 3 us: V(0,t) just before/after 3 us
def V0(o, t):
    return None
n1 = 150
lt = Lattice([(60.0, n1), (180.0, 100)], 60.0, 180.0, [("direct", None)], lambda m: 120.0)
Vz0 = []
for m in range(501):
    lt.step(m); Vz0.append(lt.VI(0, 0)[0])
chk("(e) V(0,t): 60 before 3 us, 90 after (t=2.9, 3.1, 5)", [Vz0[290], Vz0[310], Vz0[500]], [60, 90, 90])
# FDTD cross-check of the worked problem
T, PV, PI, zV, _ = fdtd_two_line(60, 2e8 * 1e-6, 300, 180, 3e8 * 1e-6, 300, 60, 540, lambda t: 120.0 * ramp(t, 0.06), 0.0025, 30, [150, 600])
def at(arr, t): return arr[int(round(t / 0.0025))]
chk("FDTD worked problem V(150 m) at 1.5, 3, 5, 7 us", [at(PV, t)[0] for t in (1.5, 3, 5, 7)], [60, 90, 112.5, 106.875], 3e-3)
chk("FDTD worked problem I(150 m) at 1.5, 3, 5, 7 us", [at(PI, t)[0] for t in (1.5, 3, 5, 7)], [1, 0.5, 0.125, 0.21875], 3e-3)
chk("FDTD V_L at 3.5, 5.5, 7.5, 30 us", [at(PV, t)[1] for t in (3.5, 5.5, 7.5, 30)], [135, 101.25, 109.6875, 108], 3e-3)
# (e) uniqueness: (1+GL)*90 = 120 RL/(60+RL) only for RL = 180 (RL>0)
RLs = np.linspace(1, 2000, 200001)
dev = (2 * RLs / (RLs + 180)) * 90 - 120 * RLs / (60 + RLs)
roots = RLs[np.nonzero(np.diff(np.sign(dev)))[0]]
chk("(e) only RL = 180 ohm makes the first load value final", [roots[0]], [180], 1e-3)

print(f"\n{'ALL PASS' if NF == 0 else str(NF) + ' FAIL'}")
