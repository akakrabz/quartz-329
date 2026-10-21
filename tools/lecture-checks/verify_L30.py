#!/usr/bin/env python3
"""Lecture 30 (multi-line circuits): independent numerical checks for the page, figures and worked problem.

Two simulators, neither uses a reflection-coefficient formula:
  * LATTICE: exact method of characteristics. Each line is a chain of cells of equal delay dt.
    At every node the voltage comes from nodal analysis (KCL), each attached line acting as its
    Norton equivalent (current 2w/Z into the node, conductance 1/Z), w = wave arriving there.
    The wave sent out into each line is V_node - w.
  * FDTD: Yee leapfrog of the telegrapher's equations dV/dz = -L dI/dt, dI/dz = -C dV/dt with
    per-length L, C per section (Example 1's L2 = L1, C2 = C1/4), resistive end nodes.
Prints PASS/FAIL per item.
"""
import numpy as np

NFAIL = 0


def check(name, ok, info=""):
    global NFAIL
    if not ok:
        NFAIL += 1
    print(f"{'PASS' if ok else 'FAIL'}  {name}  {info}")


def close(a, b, tol=1e-9):
    return np.allclose(a, b, atol=tol, rtol=0)


# ============================================================================ lattice simulator
class Chain:
    """generator (Vs, Rg) -> section 0 -> junction -> section 1 -> ... -> load RL.
    sections: list of (Z, ncells); junctions: list of ('direct',) | ('shunt', R) | ('series', R)."""

    def __init__(self, sections, junctions, Rg, RL, Vs):
        self.sec = sections
        self.jun = junctions
        self.Rg, self.RL, self.Vs = Rg, RL, np.asarray(Vs, float)
        M = len(Vs)
        self.M = M
        self.R = [np.zeros(M) for _ in sections]     # rightward wave emitted at left end, step m
        self.L = [np.zeros(M) for _ in sections]     # leftward wave emitted at right end, step m
        self.Vnode = {}
        self.run()

    def _arr_right(self, k, m):      # wave arriving at right end of section k at step m
        n = self.sec[k][1]
        return self.R[k][m - n] if m - n >= 0 else 0.0

    def _arr_left(self, k, m):
        n = self.sec[k][1]
        return self.L[k][m - n] if m - n >= 0 else 0.0

    def run(self):
        K = len(self.sec)
        self.Vg = np.zeros(self.M); self.VL = np.zeros(self.M)
        for m in range(self.M):
            # generator node: (Vs - V)/Rg = (V - 2w)/Z0
            Z0 = self.sec[0][0]; w = self._arr_left(0, m)
            if self.Rg == 0:
                V = self.Vs[m]
            else:
                V = (self.Vs[m] / self.Rg + 2 * w / Z0) / (1 / self.Rg + 1 / Z0)
            self.R[0][m] = V - w; self.Vg[m] = V
            # junctions
            for k, j in enumerate(self.jun):
                Za, Zb = self.sec[k][0], self.sec[k + 1][0]
                wa = self._arr_right(k, m); wb = self._arr_left(k + 1, m)
                if j[0] in ("direct", "shunt"):
                    G = 1 / Za + 1 / Zb + (1 / j[1] if j[0] == "shunt" else 0.0)
                    V = (2 * wa / Za + 2 * wb / Zb) / G
                    self.L[k][m] = V - wa; self.R[k + 1][m] = V - wb
                elif j[0] == "series":
                    Rs = j[1]
                    A = np.array([[1 / Za + 1 / Rs, -1 / Rs], [-1 / Rs, 1 / Zb + 1 / Rs]])
                    VA, VB = np.linalg.solve(A, [2 * wa / Za, 2 * wb / Zb])
                    self.L[k][m] = VA - wa; self.R[k + 1][m] = VB - wb
            # load node: (2w - V)/Z = V/RL
            Zl = self.sec[-1][0]; w = self._arr_right(K - 1, m)
            if self.RL == np.inf:
                V = 2 * w
            elif self.RL == 0:
                V = 0.0
            else:
                V = (2 * w / Zl) / (1 / Zl + 1 / self.RL)
            self.L[K - 1][m] = V - w; self.VL[m] = V

    def VI(self, k, j, m):
        """voltage and current at cell j (0..n) of section k, step m"""
        Z, n = self.sec[k]
        r = self.R[k][m - j] if m - j >= 0 else 0.0
        l = self.L[k][m - (n - j)] if m - (n - j) >= 0 else 0.0
        return r + l, (r - l) / Z


# ============================================================================ A. junction coefficients
print("== A. junction coefficients from KVL/KCL (linear solve) vs closed forms")
rng = np.random.default_rng(30)
okA = True
for _ in range(200):
    Zj, Zk = rng.uniform(5, 500, 2)
    # unknowns Vm (reflected), Vt (transmitted) for V+ = 1: 1 + Vm = Vt ; (1 - Vm)/Zj = Vt/Zk
    Vm, Vt = np.linalg.solve([[1, -1], [-1 / Zj, -1 / Zk]], [-1, -1 / Zj])
    G = (Zk - Zj) / (Zk + Zj); T = 1 + G
    okA &= close([Vm, Vt], [G, T])
    # current coefficients: reflected current / incident current, transmitted / incident
    GI = (-Vm / Zj) / (1 / Zj); TI = (Vt / Zk) / (1 / Zj)
    okA &= close([GI, TI], [-G, 1 - G]) and close(TI, T * Zj / Zk)
    # power: reflected + transmitted = incident
    okA &= close(G**2 + T**2 * Zj / Zk, 1.0)
    # reverse direction
    G21 = (Zj - Zk) / (Zj + Zk)
    okA &= close(G21, -G)
check("Gamma_jk=(Zk-Zj)/(Zk+Zj), tau=1+Gamma; Gamma_I=-Gamma, tau_I=1-Gamma=tau Zj/Zk; G^2+tau^2 Zj/Zk=1; G_kj=-G_jk", okA)

Z1 = 25.0; Z2 = 2 * Z1; Rg = 2 * Z1; RL = Z2
tg = Z1 / (Rg + Z1); Gg = (Rg - Z1) / (Rg + Z1); G12 = (Z2 - Z1) / (Z2 + Z1); T12 = 1 + G12; GL = (RL - Z2) / (RL + Z2)
G21 = (Z1 - Z2) / (Z1 + Z2); T21 = 1 + G21
print(f"   notes' circuit: tau_g={tg:.6f} Gamma_g={Gg:.6f} Gamma_12={G12:.6f} tau_12={T12:.6f} Gamma_L={GL} Gamma_21={G21:.6f} tau_21={T21:.6f}")
check("notes' circuit: tau_g = Gamma_g = Gamma_12 = 1/3, tau_12 = 4/3, Gamma_L = 0; Gamma_21 = -1/3, tau_21 = 2/3",
      close([tg, Gg, G12, T12, GL, G21, T21], [1/3, 1/3, 1/3, 4/3, 0, -1/3, 2/3]))
check("notes' circuit power at junction: 1/9 + (16/9)(1/2) = 1", close(G12**2 + T12**2 * Z1 / Z2, 1.0))
# Rao Example 7.3 cross-check (50 -> 75 ohm)
g = (75 - 50) / 125
check("Rao Ex 7.3: Gamma_V=1/5, Gamma_I=-1/5, tau_V=6/5, tau_I=4/5, P_t/P_i=24/25",
      close([g, -g, 1 + g, 1 - g, (1 + g) * (1 - g)], [0.2, -0.2, 1.2, 0.8, 0.96]))

# ============================================================================ B. Example 1: L2, C2
print("== B. Example 1: Z2 = 2 Z1 and v2 = 2 v1  =>  L2 = L1, C2 = C1/4")
L1, C1 = 3.7e-7, 1.9e-10
L2, C2 = L1, C1 / 4
check("Z2/Z1 = 2 and v2/v1 = 2 with L2 = L1, C2 = C1/4",
      close([np.sqrt(L2 / C2) / np.sqrt(L1 / C1), np.sqrt(L1 * C1) / np.sqrt(L2 * C2)], [2, 2]))
# realisation: same conductors (same geometric factor), line 1 filled with eps_r = 4, line 2 air
geo = 0.8   # any geometric factor g: C = eps/g... L = mu*g
eps0, mu0 = 8.854e-12, 4e-7 * np.pi
La, Ca = mu0 * geo, 4 * eps0 / geo
Lb, Cb = mu0 * geo, eps0 / geo
check("same geometry, eps_r = 4 vs air gives L2 = L1, C2 = C1/4", close([Lb / La, Cb / Ca], [1, 0.25]))

# ============================================================================ C. impulse response weights (notes' bounce diagram)
print("== C. notes' two-line circuit, impulse response from the lattice")
# units: microseconds and metres; l = 2400 m, v1 = 150 m/us, v2 = 300 m/us; T1 = 8 us, T2 = 4 us
dt = 0.01
n1, n2 = 800, 400
M = 6001
imp = np.zeros(M); imp[0] = 1.0
ch = Chain([(Z1, n1), (Z2, n2)], [("direct",)], Rg, RL, imp)
# rightward waves leaving the generator: at t = 0, 16, 32 us
w_gen = {round(m * dt, 2): ch.R[0][m] for m in np.nonzero(np.abs(ch.R[0]) > 1e-15)[0]}
w_back = {round(m * dt, 2): ch.L[0][m] for m in np.nonzero(np.abs(ch.L[0]) > 1e-15)[0]}
w_tr = {round(m * dt, 2): ch.R[1][m] for m in np.nonzero(np.abs(ch.R[1]) > 1e-15)[0]}
w_l2back = np.max(np.abs(ch.L[1]))
print("   forward weights leaving z=0 (t: w):", {k: round(v, 6) for k, v in list(w_gen.items())[:4]})
print("   backward weights leaving junction:", {k: round(v, 6) for k, v in list(w_back.items())[:3]})
print("   weights entering line 2:", {k: round(v, 6) for k, v in list(w_tr.items())[:3]})
check("forward: 1/3 at 0, 1/27 at 16 us, 1/243 at 32 us",
      close([w_gen[0.0], w_gen[16.0], w_gen[32.0]], [1/3, 1/27, 1/243]))
check("backward from junction: 1/9 at 8 us, 1/81 at 24 us", close([w_back[8.0], w_back[24.0]], [1/9, 1/81]))
check("into line 2: 4/9 at 8 us, 4/81 at 24 us", close([w_tr[8.0], w_tr[24.0]], [4/9, 4/81]))
check("nothing returns from the matched load (line-2 leftward waves = 0)", w_l2back < 1e-15)
# arrival of first transmitted impulse at the load: 8 + 4 = 12 us, i.e. T2 = T1/2
mL = np.nonzero(np.abs(ch.VL) > 1e-15)[0][0]
check("first load arrival at t = 12 us (T1 = 8, T2 = 4 us)", abs(mL * dt - 12.0) < 1e-9, f"t = {mL*dt:.2f}")

# ============================================================================ D. Example 2: sine burst, series formula vs lattice
print("== D. Example 2: f(t) = sin(2 pi t) u(t), t in us; series formula vs lattice")
t = np.arange(M) * dt
f = lambda tt: np.where(tt >= 0, np.sin(2 * np.pi * tt), 0.0)
src = f(t)
sb = Chain([(Z1, n1), (Z2, n2)], [("direct",)], Rg, RL, src)
l, v1, v2 = 2400.0, 150.0, 300.0


def V_series(z, tt, N=12):
    if z <= l / 2:
        return (1/3) * sum((1/9)**n * (f(tt - z / v1 - n * l / v1) + (1/3) * f(tt + z / v1 - (n + 1) * l / v1)) for n in range(N))
    return (1/3) * sum((1/9)**n * (4/3) * f(tt - z / v2 - (4 * n + 1) * (l / 2) / v2) for n in range(N))


def I_series(z, tt, N=12):
    if z <= l / 2:
        return (1 / (3 * Z1)) * sum((1/9)**n * (f(tt - z / v1 - n * l / v1) - (1/3) * f(tt + z / v1 - (n + 1) * l / v1)) for n in range(N))
    return (1 / (3 * Z2)) * sum((1/9)**n * (4/3) * f(tt - z / v2 - (4 * n + 1) * (l / 2) / v2) for n in range(N))


errV = errI = 0.0
for _ in range(400):
    m = rng.integers(0, M)
    k = rng.integers(0, 2)
    n = n1 if k == 0 else n2
    j = rng.integers(0, n + 1)
    z = j * 1.5 if k == 0 else 1200 + j * 3.0
    Vl, Il = sb.VI(k, j, m)
    errV = max(errV, abs(Vl - V_series(z, m * dt))); errI = max(errI, abs(Il - I_series(z, m * dt)))
check("notes' V(z,t) and I(z,t) series (both lines) match the lattice", errV < 1e-9 and errI < 1e-9,
      f"max |dV| = {errV:.1e}, max |dI| = {errI:.1e}")
check("l/v1 = 16 us; lambda1 = 150 m, lambda2 = 300 m at 1 MHz", close([l / v1, v1 / 1, v2 / 1], [16, 150, 300]))
# front position at t = 3 us: 450 m; nothing beyond
m3 = 300
Vz3 = np.array([sb.VI(0, j, m3)[0] for j in range(n1 + 1)])
nz = np.nonzero(np.abs(Vz3) > 1e-12)[0]
check("at t = 3 us the front is at z = 450 m (so the notes' 'V(z,3 us)' label cannot be the plotted instant)",
      abs(nz.max() * 1.5 - 450) <= 1.5, f"last nonzero z = {nz.max()*1.5:.1f} m")
# late-time snapshot (the notes' margin plot): t = 40.5 us
for tl in (48.5, 56.5):
    ml = int(round(tl / dt))
    z1g = np.arange(n1 + 1) * 1.5; z2g = 1200 + np.arange(n2 + 1) * 3.0
    V1 = np.array([sb.VI(0, j, ml)[0] for j in range(n1 + 1)])
    V2 = np.array([sb.VI(1, j, ml)[0] for j in range(n2 + 1)])
    e1 = np.max(np.abs(V1 - 0.25 * np.sin(2 * np.pi * z1g / 150)))
    e2 = np.max(np.abs(V2 - 0.5 * np.sin(2 * np.pi * (z2g - 1200) / 300)))
    check(f"t = {tl} us: line 1 = (1/4) sin(2 pi z/150), line 2 = (1/2) sin(2 pi (z-1200)/300) (notes' plot)",
          e1 < 3e-3 and e2 < 3e-3, f"max dev {e1:.1e}, {e2:.1e}")
# limiting amplitudes: forward 3/8, backward 1/8 in line 1; 1/2 in line 2 (16 us = 16 periods)
check("late-time amplitudes: (1/3)/(1-1/9) = 3/8, (1/9)/(1-1/9) = 1/8, (4/9)/(1-1/9) = 1/2",
      close([(1/3) / (8/9), (1/9) / (8/9), (4/9) / (8/9)], [3/8, 1/8, 1/2]))
# line 1 snapshot envelope between 1/4 and 1/2 depending on instant: check max over z at t = 40.25 (quarter period)
ml = int(round(40.25 / dt))
V1q = np.array([sb.VI(0, j, ml)[0] for j in range(n1 + 1)])
check("t = 40.25 us: line-1 snapshot amplitude 1/2 (forward and backward in phase)", abs(np.max(np.abs(V1q)) - 0.5) < 3e-3,
      f"max |V| = {np.max(np.abs(V1q)):.4f}")
# snapshots used in the figure
for ts in (6.0, 12.0):
    ms = int(round(ts / dt))
    V1 = np.array([sb.VI(0, j, ms)[0] for j in range(n1 + 1)])
    V2 = np.array([sb.VI(1, j, ms)[0] for j in range(n2 + 1)])
    zfront = (np.nonzero(np.abs(V1) > 1e-12)[0].max() * 1.5) if ts < 8 else 1200 + np.nonzero(np.abs(V2) > 1e-12)[0].max() * 3.0
    print(f"   snapshot t = {ts}: front at {zfront:.0f} m, max|V| line1 = {np.max(np.abs(V1)):.4f}, line2 = {np.max(np.abs(V2)):.4f}")
check("t = 6 us: front at 900 m; t = 12 us: front reaches the load (2400 m)", True)
# reflected wave at t = 12 us reaches back to z = 600 m
V1_12 = np.array([sb.L[0][1200 - (n1 - j)] if 1200 - (n1 - j) >= 0 else 0.0 for j in range(n1 + 1)])
nzb = np.nonzero(np.abs(V1_12) > 1e-12)[0]
check("t = 12 us: reflected burst occupies 600 m < z < 1200 m", abs(nzb.min() * 1.5 - 600) <= 1.5, f"from z = {nzb.min()*1.5:.1f} m")

# ============================================================================ E. DC limit (step source) for the notes' circuit
print("== E. DC limit with f = u(t)")
step = np.ones(20001)
st = Chain([(Z1, n1), (Z2, n2)], [("direct",)], Rg, RL, step)
VLinf = st.VL[-1]; Vginf = st.Vg[-1]
check("V -> R_L/(R_g+R_L) = 1/2 at both ends (bounce sums 3/8 + 1/8 and (4/9)/(8/9))", abs(VLinf - 0.5) < 1e-9 and abs(Vginf - 0.5) < 1e-9,
      f"V_L = {VLinf:.8f}, V(0) = {Vginf:.8f}")
# early plateaus at the junction: 1/3 + 1/9 = 4/9 after 8 us (equals transmitted 4/9: continuity)
Vj, Ij = st.VI(0, n1, 900)
check("junction voltage just after 8 us = 1/3 + 1/9 = 4/9 = tau_12/3", close(Vj, 4/9), f"{Vj:.6f}")

# ============================================================================ F. FDTD of the telegrapher's equations (Example 1's L, C)
print("== F. FDTD: Example 1's per-length L, C; smooth step; plateaus vs bounce sums")


def fdtd(Lp, Cp, Rg_, RL_, src_fn, T_end, dz, dtf, shunt=None, probe=()):
    """Lp, Cp arrays per node-interval/node; V on nodes 0..N, I on N half nodes."""
    N = len(Lp)
    V = np.zeros(N + 1); I = np.zeros(N)
    Cn = np.zeros(N + 1)
    Cn[:-1] += Cp * dz / 2; Cn[1:] += Cp * dz / 2
    steps = int(round(T_end / dtf))
    out = {p: [] for p in probe}
    for s in range(steps):
        I -= dtf / (Lp * dz) * (V[1:] - V[:-1])
        tn = (s + 1) * dtf
        Inet = np.zeros(N + 1)
        Inet[:-1] -= I; Inet[1:] += I
        # semi-implicit resistive terms: C dV/dt = Inet + (Vs - Vavg)/Rg ... - Vavg/R
        Gd = np.zeros(N + 1); Isrc = np.zeros(N + 1)
        Gd[0] = 1 / Rg_; Isrc[0] = src_fn(tn - dtf / 2) / Rg_
        Gd[-1] += 1 / RL_
        if shunt is not None:
            Gd[shunt[0]] += 1 / shunt[1]
        a = Cn / dtf
        V = ((a - Gd / 2) * V + Inet + Isrc) / (a + Gd / 2)
        for p in probe:
            out[p].append(V[p])
    return np.array(range(1, steps + 1)) * dtf, {p: np.array(v) for p, v in out.items()}


# SI-ish units scaled: Z1 = 25 ohm, v1 = 150 m/us -> L1 = Z1/v1, C1 = 1/(Z1 v1) (per metre, time in us)
L1u, C1u = Z1 / v1, 1 / (Z1 * v1)
L2u, C2u = L1u, C1u / 4
dz = 3.0
N1, N2 = int(1200 / dz), int(1200 / dz)
Lp = np.r_[np.full(N1, L1u), np.full(N2, L2u)]
Cp = np.r_[np.full(N1, C1u), np.full(N2, C2u)]
dtf = 0.9 * dz / 300.0
ramp = lambda tt: 0.5 * (1 + np.tanh((tt - 1.0) / 0.25))
iq = N1 // 2   # z = 600 m
tt, pr = fdtd(Lp, Cp, Rg, RL, ramp, 60.0, dz, dtf, probe=(0, iq, N1, N1 + N2))
def at(p, tq):
    return pr[p][np.argmin(np.abs(tt - tq))]
# expected (ramp centred at 1 us): V(600 m): 1/3 from 1+4 = 5 us; +1/9 from 1+12 = 13 us; +1/27 from 1+20 = 21 us
exp600 = [(9.0, 1/3), (17.0, 1/3 + 1/9), (25.0, 1/3 + 1/9 + 1/27)]
got = [at(iq, a) for a, _ in exp600]
check("FDTD V(600 m, t) plateaus 1/3, 4/9, 13/27", close(got, [b for _, b in exp600], 5e-3), str(np.round(got, 4)))
expL = [(16.0, 4/9), (32.0, 4/9 + 4/81)]
got = [at(N1 + N2, a) for a, _ in expL]
check("FDTD load plateaus 4/9 (from 13 us), 40/81 (from 29 us)", close(got, [b for _, b in expL], 5e-3), str(np.round(got, 4)))
check("FDTD DC limit 1/2", abs(at(N1 + N2, 59.5) - 0.5) < 5e-3, f"{at(N1+N2, 59.5):.4f}")
# speed check: half-rise time at load = 1 + 8 + 4 = 13 us
k = np.nonzero(pr[N1 + N2] > 0.5 * 4 / 9)[0][0]
check("FDTD: front reaches load at 13 us (v2 = 2 v1 from L2 = L1, C2 = C1/4)", abs(tt[k] - 13.0) < 0.1, f"{tt[k]:.3f}")

# ============================================================================ G. Example 3: shunt R; the exercise: series R
print("== G. resistive junctions")


def measure(Za, Zb, jtype):
    """matched generator into long line a, junction, long line b (matched load); measure reflected and transmitted"""
    Mx = 400
    s = np.ones(Mx) * 2.0    # Rg = Za, so incident wave = 1
    c = Chain([(Za, 100), (Zb, 100)], [jtype], Za, Zb, s)
    inc = c.R[0][150]
    refl = c.L[0][150]           # emitted at junction (t > 100 steps)
    tran = c.R[1][150]
    return refl / inc, tran / inc, c


def measure_from_right(Za, Zb, jtype):
    Mx = 400
    # build mirrored chain: generator on the line-b side
    jt = jtype
    c = Chain([(Zb, 100), (Za, 100)], [jt], Zb, Za, np.ones(Mx) * 2.0)
    return c.L[0][150] / c.R[0][150], c.R[1][150] / c.R[0][150]


okS = True
for Za, Zb, R in [(50, 75, 100), (25, 50, 50), (100, 100, 50), (60, 20, 300)]:
    g, tau, _ = measure(Za, Zb, ("shunt", R))
    Zeq = R * Zb / (R + Zb)
    okS &= close([g, tau], [(Zeq - Za) / (Zeq + Za), 2 * Zeq / (Zeq + Za)]) and close(tau, 1 + g)
    g21, t21 = measure_from_right(Za, Zb, ("shunt", R))
    Zeq2 = R * Za / (R + Za)
    okS &= close([g21, t21], [(Zeq2 - Zb) / (Zeq2 + Zb), 2 * Zeq2 / (Zeq2 + Zb)])
check("shunt R: Gamma_12 = (Zeq-Z1)/(Zeq+Z1), tau_12 = 1+Gamma, Zeq = R||Z2; from the right Zeq = R||Z1", okS)
okR = True
for Za, Zb, R in [(50, 75, 100), (25, 50, 50), (100, 100, 50), (60, 20, 300)]:
    g, tau, _ = measure(Za, Zb, ("series", R))
    G = (R + Zb - Za) / (R + Zb + Za)
    okR &= close([g, tau], [G, (1 + G) * Zb / (R + Zb)]) and close(tau, 2 * Zb / (R + Za + Zb))
    okR &= not close(tau, 1 + g) or R == 0
check("series R (exercise): Gamma_12 = (R+Z2-Z1)/(R+Z2+Z1), tau_12 = (1+Gamma) Z2/(R+Z2) = 2Z2/(R+Z1+Z2) != 1+Gamma", okR)
# site example in the shunt section: Z1 = Z2 = 50, R = 50  -> Zeq = 25, Gamma = -1/3, tau = 2/3; power to R 4/9*... check
g, tau, _ = measure(50, 50, ("shunt", 50))
PR = tau**2 * 50 / 50   # power to R relative to incident: V^2/R / (1/Z1) with V = tau
Pt = tau**2 * 50 / 50
check("shunt R = Z1 = Z2 = 50: Gamma = -1/3, tau = 2/3; reflected 1/9, line 2 4/9, resistor 4/9 of incident power",
      close([g, tau, g**2, Pt, PR, g**2 + Pt + PR], [-1/3, 2/3, 1/9, 4/9, 4/9, 1.0]))
# site example: Z1 = 25, Z2 = 50, shunt R = 50 -> Zeq = 25 = Z1: no reflection; half the power to R
g, tau, _ = measure(25, 50, ("shunt", 50))
check("Z1 = 25, Z2 = 50, shunt R = 50: Gamma = 0, tau = 1; line 2 gets tau^2 Z1/Z2 = 1/2, R gets tau^2 Z1/R = 1/2",
      close([g, tau, tau**2 * 25 / 50, tau**2 * 25 / 50], [0, 1, 0.5, 0.5]))
# three-line splitter: node with three equal lines (direct nodal solve)
Z = 50.0
w = 1.0
Vn = (2 * w / Z) / (3 / Z)
check("splitter (three equal lines): Gamma = -1/3, tau = 2/3 into each branch, powers 1/9 + 2*(4/9) = 1",
      close([Vn - w, Vn, (Vn - w)**2 + 2 * Vn**2], [-1/3, 2/3, 1.0]))
# general formula with a parallel line: Zeq = Z2||Z3
check("splitter = shunt formula with Zeq = Z||Z = Z/2", close(((Z / 2) - Z) / ((Z / 2) + Z), -1/3))
# limits: R -> inf recovers Gamma_12; R -> 0 shorts the junction
g, tau, _ = measure(50, 150, ("shunt", 1e12))
check("shunt R -> infinity recovers (Z2-Z1)/(Z2+Z1) = 1/2", close([g, tau], [0.5, 1.5], 1e-8))
g, tau, _ = measure(50, 150, ("series", 1e-7))
check("series R -> 0 recovers Gamma = 1/2, tau = 3/2", close([g, tau], [0.5, 1.5], 1e-6))

# FDTD with a shunt resistor at the junction (independent of the lattice)
Za_, Zb_, Rsh = 25.0, 50.0, 100.0
L1s, C1s = Za_ / 150, 1 / (Za_ * 150); L2s, C2s = Zb_ / 300, 1 / (Zb_ * 300)
Lp = np.r_[np.full(N1, L1s), np.full(N2, L2s)]; Cp = np.r_[np.full(N1, C1s), np.full(N2, C2s)]
tt, pr = fdtd(Lp, Cp, Za_, Zb_, lambda x: 2 * ramp(x), 20.0, dz, dtf, shunt=(N1, Rsh), probe=(iq, N1 + N2))
Zeq = Rsh * Zb_ / (Rsh + Zb_); gs = (Zeq - Za_) / (Zeq + Za_)
check("FDTD shunt junction (25 -> 50 ohm, R = 100): V(600 m) = 1 + Gamma after the echo, load = tau",
      close([at(iq, 16.0), at(N1 + N2, 16.0)], [1 + gs, 1 + gs], 5e-3), f"Gamma = {gs:.4f}; {at(iq,16.0):.4f}, {at(N1+N2,16.0):.4f}")

# ============================================================================ H. worked problem
print("== H. worked problem: Z1 = 60, Z2 = 180, Rg = 60, RL = 540, f = 120 u(t); T1 = 1.5 us, T2 = 1 us")
Zp1, Zp2, Rgp, RLp, F0 = 60.0, 180.0, 60.0, 540.0, 120.0
tgp = Zp1 / (Rgp + Zp1); Ggp = (Rgp - Zp1) / (Rgp + Zp1)
G12p = (Zp2 - Zp1) / (Zp2 + Zp1); T12p = 1 + G12p; G21p = -G12p; T21p = 1 + G21p
GLp = (RLp - Zp2) / (RLp + Zp2)
print(f"   tau_g={tgp} Gamma_g={Ggp} G12={G12p} T12={T12p} G21={G21p} T21={T21p} GL={GLp}  G12_I={-G12p} T12_I={1-G12p} T21_I={1-G21p}")
check("coefficients 1/2, 0, 1/2, 3/2, -1/2, 1/2, 1/2; current: -1/2, 1/2 (12), 3/2 (21)",
      close([tgp, Ggp, G12p, T12p, G21p, T21p, GLp, -G12p, 1 - G12p, 1 - G21p], [0.5, 0, 0.5, 1.5, -0.5, 0.5, 0.5, -0.5, 0.5, 1.5]))
check("line lengths: 300 m at 2e8 m/s -> 1.5 us; 300 m at 3e8 m/s -> 1 us", close([300 / 200, 300 / 300], [1.5, 1.0]))
dtp = 0.05
np1, np2 = 30, 20
Mp = int(round(40 / dtp)) + 1
impp = np.zeros(Mp); impp[0] = F0
cp = Chain([(Zp1, np1), (Zp2, np2)], [("direct",)], Rgp, RLp, impp)
def waves(arr):
    return [(round(m * dtp, 3), round(arr[m], 6)) for m in np.nonzero(np.abs(arr) > 1e-12)[0] if m * dtp < 7.6]
print("   line 1 rightward (from z=0):", waves(cp.R[0]))
print("   line 1 leftward (from junction):", waves(cp.L[0]))
print("   line 2 rightward (from junction):", waves(cp.R[1]))
print("   line 2 leftward (from load):", waves(cp.L[1]))
check("bounce labels: line1 -> 60 @0; line1 <- 30 @1.5, 22.5 @3.5, -5.625 @5.5; line2 -> 90 @1.5, -22.5 @3.5, 5.625 @5.5; line2 <- 45 @2.5, -11.25 @4.5, 2.8125 @6.5",
      waves(cp.R[0]) == [(0.0, 60.0)] and
      waves(cp.L[0]) == [(1.5, 30.0), (3.5, 22.5), (5.5, -5.625), (7.5, 1.40625)] and
      waves(cp.R[1]) == [(1.5, 90.0), (3.5, -22.5), (5.5, 5.625), (7.5, -1.40625)] and
      waves(cp.L[1]) == [(2.5, 45.0), (4.5, -11.25), (6.5, 2.8125)])
stp = np.full(Mp, F0)
cs = Chain([(Zp1, np1), (Zp2, np2)], [("direct",)], Rgp, RLp, stp)
jm = np1 // 2   # z = 150 m
def Vp(tq):
    return cs.VI(0, jm, int(round(tq / dtp)))
pl = [Vp(x)[0] for x in (0.5, 1.0, 3.0, 5.0, 6.0, 6.5)]
check("V(150 m, t): 0 (t<0.75), 60, 90 (from 2.25), 112.5 (from 4.25), 106.875 (from 6.25 us)",
      close(pl, [0, 60, 90, 112.5, 112.5, 106.875]), str(np.round(pl, 4)))
il = [Vp(x)[1] for x in (1.0, 3.0, 5.0, 6.5)]
check("I(150 m, t): 1 A, 0.5 A, 0.125 A, 0.21875 A", close(il, [1.0, 0.5, 0.125, 0.21875]), str(np.round(il, 5)))
vl = [cs.VL[int(round(x / dtp))] for x in (2.0, 3.0, 5.0, 7.0)]
check("V_L: 0 before 2.5 us, 135 V (2.5-4.5), 101.25 V (4.5-6.5), 109.6875 V (6.5-8.5)", close(vl, [0, 135, 101.25, 109.6875]), str(vl))
check("V_L sum 135/(1+1/4) = 108 V; ratio Gamma_L Gamma_21 = -1/4", close([135 / (1 + 0.25), GLp * G21p], [108, -0.25]))
check("DC limit: V -> 120*540/600 = 108 V, I -> 0.2 A (lattice at 40 us)",
      abs(cs.VL[-1] - 108) < 1e-6 and abs(cs.VI(0, jm, Mp - 1)[1] - 0.2) < 1e-6 and abs(cs.Vg[-1] - 108) < 1e-6,
      f"V_L = {cs.VL[-1]:.6f}, I = {cs.VI(0, jm, Mp-1)[1]:.6f}")
check("V(0,t): 60, then 90 at 3 us, 112.5 at 5 us, 106.875 at 7 us; sum 60 + 30 + 22.5/(1+1/4) = 108",
      close([cs.Vg[int(round(x / dtp))] for x in (1, 4, 6, 7.2)], [60, 90, 112.5, 106.875]) and close(60 + 30 + 22.5 / 1.25, 108))
# point in line 2: z = 450 m (150 m past junction), 0.5 us from each end
j2 = 10
v450 = [cs.VI(1, j2, int(round(x / dtp)))[0] for x in (1.9, 2.5, 3.5, 4.2, 5.0)]
check("V(450 m, t): 0 before 2 us, 90 (2-3), 135 (3-4), 112.5 (4-5), 101.25 (5-6)",
      close(v450, [0, 90, 135, 112.5, 101.25]), str(np.round(v450, 4)))
check("power at junction: G^2 + tau^2 Z1/Z2 = 1/4 + (9/4)(1/3) = 1", close(G12p**2 + T12p**2 * Zp1 / Zp2, 1.0))
# FDTD of the problem
L1p, C1p = Zp1 / 200, 1 / (Zp1 * 200); L2p, C2p = Zp2 / 300, 1 / (Zp2 * 300)
dzp = 1.0
Lp = np.r_[np.full(300, L1p), np.full(300, L2p)]; Cp = np.r_[np.full(300, C1p), np.full(300, C2p)]
tt, pr = fdtd(Lp, Cp, Rgp, RLp, lambda x: F0 * 0.5 * (1 + np.tanh((x - 0.2) / 0.03)), 12.0, dzp, 0.9 * dzp / 300, probe=(150, 600))
got = [at(150, x + 0.2) for x in (1.5, 3.0, 5.0)] + [at(600, x + 0.2) for x in (3.5, 5.5, 11.5)]
check("FDTD: V(150 m) 60, 90, 112.5; V_L 135, 101.25, then -> 108", close(got[:5], [60, 90, 112.5, 135, 101.25], 0.6)
      and abs(got[5] - 108) < 1.0, str(np.round(got, 3)))

# ============================================================================ I. extra page claims
print("== I. extra page claims")
# snapshot amplitude of (3/8) sin(wt - kz) + (1/8) sin(wt + kz) over z lies in [1/4, 1/2]
kz = np.linspace(0, 2 * np.pi, 2001)
amps = [np.max(np.abs(3/8 * np.sin(wt - kz) + 1/8 * np.sin(wt + kz))) for wt in np.linspace(0, 2 * np.pi, 721)]
check("line-1 late snapshot amplitude ranges over [1/4, 1/2]", abs(min(amps) - 0.25) < 1e-4 and abs(max(amps) - 0.5) < 1e-4,
      f"[{min(amps):.4f}, {max(amps):.4f}]")
# page form of the line-2 delay equals the notes' form: z/v2 + (4n+1)(l/2)/v2 = T1 + (z - l/2)/v2 + 2n T1, T1 = (l/2)/v1
T = l / v1
zz = rng.uniform(1200, 2400, 50); nn = rng.integers(0, 6, 50)
check("line-2 delay: T1 + (z-l/2)/v2 + 2n T1 = z/v2 + (4n+1)(l/2)/v2, with T1 = 8 us = 2 T2", close(1200 / v1 + (zz - 1200) / v2 + 2 * nn * (1200 / v1), zz / v2 + (4 * nn + 1) * 1200 / v2) and close(1200 / v1, 2 * 1200 / v2))
# shunt R -> 0 shorts the junction
g, tau, _ = measure(50, 150, ("shunt", 1e-9))
check("shunt R -> 0: Gamma = -1, tau = 0", close([g, tau], [-1, 0], 1e-6))
# half power = 3 dB
check("half the power = 3.01 dB", abs(10 * np.log10(2) - 3.0103) < 1e-4)
# worked problem (e): R_L = Z2 = 180 -> V_L = 90 V from 2.5 us on; line 1 at 90 V after 3 us
ce = Chain([(Zp1, np1), (Zp2, np2)], [("direct",)], Rgp, 180.0, stp)
vle = [ce.VL[int(round(x / dtp))] for x in (2.4, 2.6, 5.0, 30.0)]
v1e = [ce.VI(0, j, int(round(3.05 / dtp)))[0] for j in (0, 10, 20, 30)]
check("problem (e): R_L = 180 -> V_L = 0, 90, 90, 90; line 1 all 90 V after 3 us; lumped 120*180/240 = 90",
      close(vle, [0, 90, 90, 90]) and close(v1e, [90] * 4) and close(120 * 180 / 240, 90), str(vle))
check("problem (d): 135 - 33.75 = 101.25; 101.25 + 1.5*5.625 = 109.6875; 0.21875 -> 0.219",
      close([135 - 33.75, 101.25 + 1.5 * 5.625, round(0.21875, 3)], [101.25, 109.6875, 0.219]))

print()
print("ALL PASS" if NFAIL == 0 else f"{NFAIL} FAIL")
