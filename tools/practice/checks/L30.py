#!/usr/bin/env python3
"""L30 practice checks: multi-line circuits (numpy + scipy only).

Every number on practice/30-multi-line-circuits.md is printed here.
Three independent routes:
  1. Junction coefficients from the page formulas, and by solving the KVL/KCL system
     of each junction (direct, shunt R, series R) as a linear system.
  2. Bounce diagrams from an event-driven wave bookkeeper that uses the page's
     coefficients (Gamma_g, tau_g, Gamma_L, Gamma_jk, tau_jk).
  3. An FDTD (Yee leapfrog, Courant number 1 on every line) of the telegrapher's
     equations with lumped circuit elements at the nodes: no reflection
     coefficient enters it. V(z,t), I(z,t), impulse weights (pulse areas) and the
     t -> infinity limits are read from it and compared with route 2.
Conventions as on the Lecture 28 page: z = 0 at the generator, +z toward the load,
I(z,t) along +z on the upper conductor; forward waves I = +V/Z0, backward I = -V/Z0.
"""
import heapq
import numpy as np
from fractions import Fraction as F
from scipy.sparse import diags, lil_matrix
from scipy.sparse.linalg import splu

ALL = []


def hdr(s):
    print("\n" + "=" * 78 + "\n" + s + "\n" + "=" * 78)


def close(label, a, b, rtol=1e-9, atol=1e-12):
    ok = np.allclose(a, b, rtol=rtol, atol=atol)
    A, B = np.asarray(a, dtype=float), np.asarray(b, dtype=float)
    if A.size > 8:
        print(f"  [{label}] {A.size} samples, max |diff| = {np.max(np.abs(A - B)):.2e} -> {'OK' if ok else 'FAIL'}")
    else:
        print(f"  [{label}] {np.round(A, 6)!r} vs {np.round(B, 6)!r} -> {'OK' if ok else 'FAIL'}")
    ALL.append(bool(ok))


def check(label, cond):
    print(f"  [{label}] {'OK' if cond else 'FAIL'}")
    ALL.append(bool(cond))


# ---------------------------------------------------------------- route 1
def coef_formula(Zj, Zk, kind="direct", R=None):
    """Page formulas for a wave arriving from line j into line k."""
    if kind == "direct":
        G = (Zk - Zj) / (Zk + Zj); t = 1 + G
    elif kind == "shunt":
        Zeq = R * Zk / (R + Zk); G = (Zeq - Zj) / (Zeq + Zj); t = 1 + G
    elif kind == "series":
        Zeq = R + Zk; G = (Zeq - Zj) / (Zeq + Zj); t = (1 + G) * Zk / (R + Zk)
    return G, t


def coef_solve(Zj, Zk, kind="direct", R=None, Vp=1.0):
    """Solve KVL/KCL at the junction for V-, V++ (incident V+ = Vp from line j)."""
    if kind in ("direct", "shunt"):
        g = 0.0 if kind == "direct" else 1.0 / R
        # unknowns Vm, Vpp:  Vp + Vm - Vpp = 0 ; (Vp - Vm)/Zj - Vpp*(g + 1/Zk) = 0
        A = np.array([[1.0, -1.0], [-1.0 / Zj, -(g + 1.0 / Zk)]])
        b = np.array([-Vp, -Vp / Zj])
        Vm, Vpp = np.linalg.solve(A, b)
        PR = Vpp ** 2 * g
    else:
        # unknowns Vm, Vpp, Icur: Va = Vp+Vm; Icur = (Vp-Vm)/Zj; Va - Icur*R = Vpp; Icur = Vpp/Zk
        A = np.array([[1.0, -1.0, -R], [1.0 / Zj, 0.0, 1.0], [0.0, 1.0 / Zk, -1.0]])
        b = np.array([-Vp, Vp / Zj, 0.0])
        Vm, Vpp, Icur = np.linalg.solve(A, b)
        PR = Icur ** 2 * R
    Pin = Vp ** 2 / Zj
    return Vm / Vp, Vpp / Vp, (Vm ** 2 / Zj) / Pin, (Vpp ** 2 / Zk) / Pin, PR / Pin


def junction_report(name, Zj, Zk, kind="direct", R=None):
    Gf, tf = coef_formula(Zj, Zk, kind, R)
    Gs, ts, pr, pt, pR = coef_solve(Zj, Zk, kind, R)
    print(f"  {name}: Gamma = {Gf:.6f} ({F(Gf).limit_denominator(1000)}), tau = {tf:.6f} "
          f"({F(tf).limit_denominator(1000)}); current refl -Gamma = {-Gf:.6f}, current transm "
          f"(tau*Zj/Zk) = {tf * Zj / Zk:.6f}")
    print(f"     power fractions: reflected {pr:.6f} ({F(pr).limit_denominator(1000)}), "
          f"transmitted {pt:.6f} ({F(pt).limit_denominator(1000)}), resistor {pR:.6f} "
          f"({F(pR).limit_denominator(1000)}), sum {pr + pt + pR:.12f}")
    close(name + " formula vs KVL/KCL solve", [Gf, tf], [Gs, ts])
    close(name + " power sums to 1", pr + pt + pR, 1.0)
    return Gf, tf


# ---------------------------------------------------------------- route 2
class Circuit:
    """Cascade of lines. lines: list of (Z, T one-way delay, length or None).
    joints[i] between line i and i+1: ('direct',) | ('shunt', R) | ('series', R).
    RL: None = open, 0 = short."""

    def __init__(self, Rg, lines, joints, RL):
        self.Rg, self.lines, self.joints, self.RL = Rg, lines, joints, RL
        Z0 = lines[0][0]
        self.tau_g = Z0 / (Rg + Z0)
        self.Gam_g = (Rg - Z0) / (Rg + Z0)
        ZN = lines[-1][0]
        self.Gam_L = 1.0 if RL is None else (RL - ZN) / (RL + ZN)
        self.right, self.left = [], []   # joint i: (Gamma, tau) for right-/left-moving waves
        for i, jt in enumerate(joints):
            Za, Zb = lines[i][0], lines[i + 1][0]
            kind = jt[0]; R = jt[1] if len(jt) > 1 else None
            self.right.append(coef_formula(Za, Zb, kind, R))
            self.left.append(coef_formula(Zb, Za, kind, R))

    def bounce(self, tmax):
        """Segments (line, dir, t_start, weight) of the impulse response, t_start < tmax."""
        segs = []
        q = [(0.0, 0, +1, self.tau_g)]
        nL = len(self.lines)
        while q:
            t0, i, d, w = heapq.heappop(q)
            if t0 >= tmax or abs(w) < 1e-14:
                continue
            segs.append((i, d, t0, w))
            t1 = t0 + self.lines[i][1]
            if d == +1:
                if i == nL - 1:
                    heapq.heappush(q, (t1, i, -1, w * self.Gam_L))
                else:
                    G, t = self.right[i]
                    heapq.heappush(q, (t1, i, -1, w * G))
                    heapq.heappush(q, (t1, i + 1, +1, w * t))
            else:
                if i == 0:
                    heapq.heappush(q, (t1, 0, +1, w * self.Gam_g))
                else:
                    G, t = self.left[i - 1]
                    heapq.heappush(q, (t1, i, +1, w * G))
                    heapq.heappush(q, (t1, i - 1, -1, w * t))
        return segs

    def crossings(self, i, s, tmax):
        """Impulses of V at local position s (in delay units, 0..T_i) on line i:
        list of (time, voltage weight, current weight * Z_i)."""
        out = []
        T = self.lines[i][1]
        for (li, d, t0, w) in self.bounce(tmax):
            if li != i:
                continue
            tc = t0 + (s if d == +1 else T - s)
            if tc < tmax:
                out.append((tc, w, d * w))
        return sorted(out)

    def step_VI(self, i, s, t, V0=1.0):
        Z = self.lines[i][0]
        cr = self.crossings(i, s, t)
        return V0 * sum(c[1] for c in cr), V0 * sum(c[2] for c in cr) / Z


# ---------------------------------------------------------------- route 3: FDTD
class FDTD:
    """Yee leapfrog on every line with dz = v dt (Courant 1): cell L = Z dt, cell C = dt/Z.
    Lumped resistors (generator, load, shunt, series) enter the node equations
    with trapezoidal averaging; a sparse LU handles series resistors."""

    def __init__(self, Rg, lines, joints, RL, dt):
        self.dt = dt
        nodes_C = []
        self.line_nodes = []
        br_a, br_b, br_Z = [], [], []
        ser = []       # (a, b, R)
        shunt = {}     # node -> G
        cur = None
        for i, (Z, T, _) in enumerate(lines):
            N = int(round(T / dt))
            assert abs(N * dt - T) < 1e-9 * T, "delay not a multiple of dt"
            Ccell = dt / Z
            if i == 0:
                start = 0; nodes_C.append(0.0)
            else:
                jt = joints[i - 1]
                if jt[0] == "series":
                    start = len(nodes_C); nodes_C.append(0.0); ser.append((cur, start, jt[1]))
                else:
                    start = cur
                    if jt[0] == "shunt":
                        shunt[start] = shunt.get(start, 0.0) + 1.0 / jt[1]
            idx = [start] + list(range(len(nodes_C), len(nodes_C) + N))
            nodes_C.extend([0.0] * N)
            for k in range(N):
                br_a.append(idx[k]); br_b.append(idx[k + 1]); br_Z.append(Z)
                nodes_C[idx[k]] += Ccell / 2; nodes_C[idx[k + 1]] += Ccell / 2
            self.line_nodes.append(idx)
            cur = idx[-1]
        n = len(nodes_C)
        self.n = n
        C = np.array(nodes_C)
        G = np.zeros(n)
        G[0] += 1.0 / Rg
        if RL is not None:
            G[cur] += 1e9 if RL == 0 else 1.0 / RL
        for k, g in shunt.items():
            G[k] += g
        self.Rg = Rg
        self.a = np.array(br_a); self.b = np.array(br_b); self.Zb = np.array(br_Z)
        self.I = np.zeros(len(br_a))
        self.V = np.zeros(n)
        if ser:
            Lap = lil_matrix((n, n))
            for (p, q, R) in ser:
                g = 1.0 / R
                Lap[p, p] += g; Lap[q, q] += g; Lap[p, q] -= g; Lap[q, p] -= g
            Lap = Lap.tocsc()
            A = diags(C / dt + G / 2).tocsc() + 0.5 * Lap
            self.B = diags(C / dt - G / 2).tocsc() - 0.5 * Lap
            self.lu = splu(A.tocsc())
        else:
            self.Ad = C / dt + G / 2
            self.Bd = C / dt - G / 2
            self.lu = None

    def run(self, fi, tmax, probesV=(), probesI=()):
        """probesV: list of global node indices; probesI: list of branch indices.
        Returns times (V at n dt, I at (n+1/2) dt) and records."""
        steps = int(round(tmax / self.dt))
        recV = np.zeros((steps + 1, len(probesV)))
        recI = np.zeros((steps, len(probesI)))
        pv = np.array(probesV, dtype=int); pi = np.array(probesI, dtype=int)
        recV[0] = self.V[pv]
        dt = self.dt
        for nstep in range(steps):
            # currents to n+1/2 (cell L = Z dt -> dt/L = 1/Z)
            self.I += (self.V[self.a] - self.V[self.b]) / self.Zb
            net = np.bincount(self.b, self.I, self.n) - np.bincount(self.a, self.I, self.n)
            net[0] += 0.5 * (fi(nstep * dt) + fi((nstep + 1) * dt)) / self.Rg   # trapezoid
            if self.lu is None:
                self.V = (self.Bd * self.V + net) / self.Ad
            else:
                self.V = self.lu.solve(self.B @ self.V + net)
            recV[nstep + 1] = self.V[pv]
            recI[nstep] = self.I[pi]
        tV = np.arange(steps + 1) * dt
        tI = (np.arange(steps) + 0.5) * dt
        return tV, recV, tI, recI

    def node_at(self, i, s):
        """global node on line i at local delay s (0..T_i)."""
        return self.line_nodes[i][int(round(s / self.dt))]

    def branch_at(self, i, s):
        """branch (cell) on line i just after local delay s."""
        k = int(round(s / self.dt))
        node_a = self.line_nodes[i][min(k, len(self.line_nodes[i]) - 2)]
        return int(np.where(self.a == node_a)[0][0])


def smooth_step(rise):
    def f(t):
        if t <= 0:
            return 0.0
        if t >= rise:
            return 1.0
        return 0.5 - 0.5 * np.cos(np.pi * t / rise)
    return f


def gauss_pulse(t0, sig):
    return lambda t: np.exp(-0.5 * ((t - t0) / sig) ** 2) / (sig * np.sqrt(2 * np.pi))


def area(t, y, a, b):
    m = (t >= a) & (t <= b)
    return np.trapezoid(y[m], t[m]) if hasattr(np, "trapezoid") else np.trapz(y[m], t[m])


us = 1e-6
ns = 1e-9

# =====================================================================================
hdr("30.1 Coefficients both ways: 50 ohm -> 75 ohm")
G12, t12 = junction_report("50->75", 50.0, 75.0)
G21, t21 = junction_report("75->50", 75.0, 50.0)
Vp = 10.0
Vm, Vpp = G12 * Vp, t12 * Vp
Ii, Ir, It = Vp / 50, -Vm / 50, Vpp / 75
print(f"  10 V wave: V- = {Vm:.4f} V, V++ = {Vpp:.4f} V; I_inc = {Ii:.4f} A, I_refl = {Ir:.4f} A, I_trans = {It:.4f} A")
close("V continuity 10+2=12", Vp + Vm, Vpp)
close("I continuity 0.2-0.04=0.16", Ii + Ir, It)
print(f"  power: incident {Vp**2/50:.4f} W, reflected {Vm**2/50:.4f} W, transmitted {Vpp**2/75:.4f} W")
close("power balance", Vp ** 2 / 50, Vm ** 2 / 50 + Vpp ** 2 / 75)
# FDTD: matched generator, 50 ohm line (1 us) -> 75 ohm line (1 us) -> 75 ohm load
sim = FDTD(50.0, [(50.0, 1 * us, None), (75.0, 1 * us, None)], [("direct",)], 75.0, dt=5 * ns)
nJ1 = sim.node_at(0, 0.5 * us); nJ2 = sim.node_at(1, 0.5 * us)
tV, rV, tI, rI = sim.run(lambda t: 2 * Vp * smooth_step(20 * ns)(t), 3.0 * us, [nJ1, nJ2])
k = np.searchsorted(tV, 1.9 * us)
close("FDTD line 1 at 1.9 us (V+ + V-) = 12 V", rV[k, 0], Vp + Vm, rtol=2e-3)
close("FDTD line 2 at 1.9 us (V++) = 12 V", rV[k, 1], Vpp, rtol=2e-3)

# =====================================================================================
hdr("30.2 True or false")
# (a) Z2 = Z1, v2 = 2 v1 -> Gamma = 0 (FDTD with different delays per length is the same Z)
print(f"  (a) Gamma(Z1=Z2) = {coef_formula(50.0, 50.0)[0]}")
# (b) tau = 4/3 -> Z2 = 2 Z1 ; transmitted power fraction tau^2 Z1/Z2
tb = coef_formula(1.0, 2.0)[1]
print(f"  (b) Z2 = 2Z1: tau = {tb:.6f}, transmitted power fraction = {tb**2 * 0.5:.6f} = {F(tb**2*0.5).limit_denominator(100)}")
close("(b) 8/9", tb ** 2 * 0.5, 8 / 9)
# (c) Gamma21 = -Gamma12 ; tau12 + tau21 = 2 for several pairs
for (a, b) in [(50, 75), (50, 200), (300, 75)]:
    g12, tt12 = coef_formula(a, b); g21, tt21 = coef_formula(b, a)
    close(f"(c) {a}/{b}: G21=-G12, t12+t21=2", [g21, tt12 + tt21], [-g12, 2.0])
# (d) 50 ohm into two 100 ohm lines in parallel: Zeq = 50 -> Gamma 0, tau 1; each branch half power
Zeq = 1 / (1 / 100 + 1 / 100)
gd = (Zeq - 50) / (Zeq + 50)
print(f"  (d) Zeq = {Zeq}, Gamma = {gd}, tau = {1 + gd}, power per branch = {(1 + gd)**2 * 50 / 100}")
# FDTD of the splitter: model branches as a shunt resistor 100 (a matched 100-ohm line looks like 100 ohm)
sim = FDTD(50.0, [(50.0, 1 * us, None), (100.0, 1 * us, None)], [("shunt", 100.0)], 100.0, dt=5 * ns)
n1 = sim.node_at(0, 0.5 * us)
tV, rV, _, _ = sim.run(lambda t: 2.0 * smooth_step(20 * ns)(t), 3.0 * us, [n1])
close("(d) FDTD: line 1 voltage stays 1 V after the junction echo time (no reflection)",
      rV[np.searchsorted(tV, 1.9 * us), 0], 1.0, rtol=2e-3)
# (e) current transmission = 1 - Gamma = tau Z1/Z2, not tau
g, t = coef_formula(50.0, 200.0)
print(f"  (e) 50->200: tau = {t}, current ratio = {1 - g} = tau*Z1/Z2 = {t * 50 / 200}")
# (f) open line 2: junction sees Z2 until 2 T2  (FDTD)
sim = FDTD(50.0, [(50.0, 1 * us, None), (150.0, 1 * us, None)], [("direct",)], None, dt=5 * ns)
nj = sim.node_at(0, 1 * us)
tV, rV, _, _ = sim.run(lambda t: 2.0 * smooth_step(20 * ns)(t), 3.5 * us, [nj])
g, t = coef_formula(50.0, 150.0)
close("(f) FDTD junction V for 1<t<3 us equals tau*1 (line 2 acts as 150 ohm)",
      rV[np.searchsorted(tV, 2.5 * us), 0], t, rtol=2e-3)
print(f"  (f) junction V for 3<t<... after the open-end echo: {rV[np.searchsorted(tV, 3.4*us), 0]:.4f} (changes at 2T2 after arrival)")

# =====================================================================================
hdr("30.3 No echo back to the source (shunt R at the junction) -- symbolic checks at numbers")
# (d) conditions: R || ZB = ZA and RL = ZB.  Example: ZA = 50, ZB = 75, R = 150, RL = 75
for (ZA, ZB, R, RL, Rg) in [(50.0, 75.0, 150.0, 75.0, 20.0), (60.0, 100.0, 150.0, 100.0, 200.0)]:
    c = Circuit(Rg, [(ZA, 1 * us, None), (ZB, 1.3 * us, None)], [("shunt", R)], RL)
    back = [s for s in c.bounce(30 * us) if s[0] == 0 and s[1] == -1]
    print(f"  ZA={ZA}, ZB={ZB}, R={R}, RL={RL}, Rg={Rg}: R||ZB = {R*ZB/(R+ZB)}, backward segments on A: {len(back)}")
    check("(d) no backward wave on line A", len(back) == 0)
    sim = FDTD(Rg, [(ZA, 1 * us, None), (ZB, 1.3 * us, None)], [("shunt", R)], RL, dt=5 * ns)
    br = sim.branch_at(0, 0.5 * us); n = sim.node_at(0, 0.5 * us)
    tV, rV, tI, rI = sim.run(smooth_step(20 * ns), 8 * us, [n], [br])
    tg = ZA / (Rg + ZA)       # forward wave alone: V = tau_g, Z_A I = tau_g, for all t > 0.52 us
    m = tV > 0.6 * us
    dev = max(np.max(np.abs(rV[m, 0] - tg)), np.max(np.abs(ZA * rI[tI > 0.6 * us, 0] - tg)))
    print(f"     FDTD max |V - tau_g|, |Z_A I - tau_g| on line A after the front (0-8 us): {dev:.2e}")
    check("(d) FDTD: only the forward wave on line A", dev < 2e-3)
# (b) ZB = ZA with R present: Gamma < 0
ZA = 50.0; R = 150.0
g = coef_formula(ZA, ZA, "shunt", R)[0]
print(f"  (b) ZB = ZA = 50, R = 150: Gamma = {g:.4f} (nonzero)")
# (c) only R||ZB = ZA, RL != ZB: echo returns with tau_BA = 2(R||ZA)/(R||ZA + ZB)
ZB = 75.0; RL = 300.0
Zp = R * ZA / (R + ZA)
print(f"  (c) R||ZA = {Zp}, tau_BA = {2 * Zp / (Zp + ZB):.4f} (nonzero)")
c = Circuit(20.0, [(ZA, 1 * us, None), (ZB, 1 * us, None)], [("shunt", R)], RL)
back = [s for s in c.bounce(10 * us) if s[0] == 0 and s[1] == -1]
check("(c) mismatched load: some backward wave on A", len(back) > 0)
# (a) Rg = ZA alone does not prevent arrivals
c = Circuit(ZA, [(ZA, 1 * us, None), (ZB, 1 * us, None)], [("shunt", R * 10)], RL)
back = [s for s in c.bounce(10 * us) if s[0] == 0 and s[1] == -1]
check("(a) Rg = ZA alone: backward waves still exist", len(back) > 0)

# =====================================================================================
hdr("30.4 Line parameters: Z2 = Z1/2, v2 = v1/3")
for (L1, C1) in [(250e-9, 100e-12), (400e-9, 40e-12)]:
    Z1 = np.sqrt(L1 / C1); v1 = 1 / np.sqrt(L1 * C1)
    Z2 = Z1 / 2; v2 = v1 / 3
    L2 = Z2 / v2; C2 = 1 / (Z2 * v2)    # Z = sqrt(L/C), v = 1/sqrt(LC) -> L = Z/v, C = 1/(Zv)
    print(f"  L1={L1:.3e}, C1={C1:.3e}: L2/L1 = {L2/L1:.6f}, C2/C1 = {C2/C1:.6f}")
    close("L2 = 1.5 L1, C2 = 6 C1", [L2 / L1, C2 / C1], [1.5, 6.0])
g, t = coef_formula(1.0, 0.5)
print(f"  Gamma12 = {g:.6f}, tau12 = {t:.6f}")
close("Gamma12 = -1/3, tau12 = 2/3", [g, t], [-1 / 3, 2 / 3])
# same geometry (same GF): L = mu/GF, C = eps GF -> mu_r2 = 1.5, eps_r2 = 6 with air line 1
mur, er = 1.5, 6.0
close("v2/v1 = 1/sqrt(mur er) = 1/3, Z2/Z1 = sqrt(mur/er) = 1/2",
      [1 / np.sqrt(mur * er), np.sqrt(mur / er)], [1 / 3, 1 / 2])

# =====================================================================================
hdr("30.5 Find the error: echo from line 2 (Z1 = 50, Z2 = 200), 25 V arriving from the right")
G12, t12 = junction_report("50->200", 50.0, 200.0)
G21, t21 = junction_report("200->50", 200.0, 50.0)
Vin = 25.0
print(f"  student: into line 1 tau12*25 = {t12*Vin}, back G12*25 = {G12*Vin}")
print(f"  correct: into line 1 tau21*25 = {t21*Vin}, back G21*25 = {G21*Vin}")
# currents along +z: arriving backward wave on line 2: -25/200; reflected forward on line 2: +Vr/200
for name, Vt, Vr in [("correct", t21 * Vin, G21 * Vin), ("student", t12 * Vin, G12 * Vin)]:
    I2 = -Vin / 200 + Vr / 200
    I1 = -Vt / 50
    print(f"  {name}: V line2 side {Vin + Vr:.4f}, line1 side {Vt:.4f}; I line2 side {I2:.4f} A, line1 side {I1:.4f} A")
close("correct: I continuous (-0.2 A)", [-Vin / 200 + G21 * Vin / 200, -t21 * Vin / 50], [-0.2, -0.2])
check("student: I discontinuous", abs((-Vin / 200 + G12 * Vin / 200) - (-t12 * Vin / 50)) > 0.1)
# FDTD: backward 25 V wave from the right. Build: generator on the 200 ohm side (mirror), matched.
sim = FDTD(200.0, [(200.0, 1 * us, None), (50.0, 1 * us, None)], [("direct",)], 50.0, dt=5 * ns)
n_src = sim.node_at(0, 0.5 * us); n_out = sim.node_at(1, 0.5 * us)
tV, rV, _, _ = sim.run(lambda t: 50.0 * smooth_step(20 * ns)(t), 3 * us, [n_src, n_out])
k = np.searchsorted(tV, 1.9 * us)
close("FDTD (mirror): transmitted 10 V", rV[k, 1], 10.0, rtol=2e-3)
close("FDTD (mirror): reflected -15 V (total 10 V on the arriving side)", rV[k, 0] - 25.0, -15.0, rtol=2e-3)

# =====================================================================================
hdr("30.6 Shunt resistor that matches: Z1 = 50, Z2 = 75")
R = 1 / (1 / 50 - 1 / 75)
print(f"  R = {R:.6f} ohm")
close("R = 150", R, 150.0)
junction_report("from line 1 (shunt 150)", 50.0, 75.0, "shunt", 150.0)
print(f"  Zeq from the right = 150||50 = {150*50/200}")
junction_report("from line 2 (shunt 150)", 75.0, 50.0, "shunt", 150.0)
close("from right: Gamma21 = -1/3, tau21 = 2/3", coef_formula(75.0, 50.0, "shunt", 150.0), [-1 / 3, 2 / 3])
p = coef_solve(75.0, 50.0, "shunt", 150.0)
close("from right: 1/9, 2/3, 2/9", p[2:], [1 / 9, 2 / 3, 2 / 9])
p = coef_solve(50.0, 75.0, "shunt", 150.0)
close("from left: 0, 2/3, 1/3", p[2:], [0, 2 / 3, 1 / 3])
for (gen_side, lines) in [("left", [(50.0, 1 * us, None), (75.0, 1 * us, None)]),
                          ("right", [(75.0, 1 * us, None), (50.0, 1 * us, None)])]:
    Zs, Zl = lines[0][0], lines[1][0]
    sim = FDTD(Zs, lines, [("shunt", 150.0)], Zl, dt=5 * ns)
    n0 = sim.node_at(0, 0.5 * us); n1 = sim.node_at(1, 0.5 * us)
    tV, rV, _, _ = sim.run(lambda t: 2.0 * smooth_step(20 * ns)(t), 3 * us, [n0, n1])
    k = np.searchsorted(tV, 1.9 * us)
    g, t = coef_formula(Zs, Zl, "shunt", 150.0)
    close(f"FDTD from {gen_side}: line-a V = 1+Gamma, line-b V = tau", rV[k], [1 + g, t], rtol=2e-3)

# =====================================================================================
hdr("30.7 Series resistor in the splice: Z1 = 50, Z2 = 75, R = 25")
junction_report("from line 1 (series 25)", 50.0, 75.0, "series", 25.0)
junction_report("from line 2 (series 25)", 75.0, 50.0, "series", 25.0)
close("from left Gamma=1/3 tau=1", coef_formula(50.0, 75.0, "series", 25.0), [1 / 3, 1.0])
close("from right Gamma=0 tau=2/3", coef_formula(75.0, 50.0, "series", 25.0), [0.0, 2 / 3])
p = coef_solve(50.0, 75.0, "series", 25.0)
close("left: 1/9, 2/3, 2/9", p[2:], [1 / 9, 2 / 3, 2 / 9])
p = coef_solve(75.0, 50.0, "series", 25.0)
close("right: 0, 2/3, 1/3", p[2:], [0.0, 2 / 3, 1 / 3])
print(f"  1+Gamma12 = {1 + 1/3:.6f} vs tau12 = 1 ; divider Z2/(R+Z2) = {75/100}")
print(f"  current through R = (1-Gamma12)V+/Z1 = {(2/3)/50:.6f} V+ ; = tau12 V+/Z2 = {1/75:.6f} V+")
close("series current continuity", (2 / 3) / 50, 1 / 75)
for (gen_side, lines) in [("left", [(50.0, 1 * us, None), (75.0, 1 * us, None)]),
                          ("right", [(75.0, 1 * us, None), (50.0, 1 * us, None)])]:
    Zs, Zl = lines[0][0], lines[1][0]
    sim = FDTD(Zs, lines, [("series", 25.0)], Zl, dt=5 * ns)
    n0 = sim.node_at(0, 0.5 * us); n1 = sim.node_at(1, 0.5 * us)
    tV, rV, _, _ = sim.run(lambda t: 2.0 * smooth_step(20 * ns)(t), 3 * us, [n0, n1])
    k = np.searchsorted(tV, 1.9 * us)
    g, t = coef_formula(Zs, Zl, "series", 25.0)
    close(f"FDTD from {gen_side}: line-a V = 1+Gamma, line-b V = tau", rV[k], [1 + g, t], rtol=2e-3)

# =====================================================================================
hdr("30.8 Three sections (FA23 E3 #3a style): Rg 25; 75 (2 us), 150 (1 us), 50 (3 us); RL 50; f_i = delta")
lines = [(75.0, 2 * us, None), (150.0, 1 * us, None), (50.0, 3 * us, None)]
joints = [("direct",), ("direct",)]
c = Circuit(25.0, lines, joints, 50.0)
print(f"  tau_g = {c.tau_g:.6f}, Gamma_g = {c.Gam_g:.6f}, Gamma_L = {c.Gam_L}")
print(f"  junction 1-2 right: Gamma = {c.right[0][0]:.6f}, tau = {c.right[0][1]:.6f}; left: Gamma = {c.left[0][0]:.6f}, tau = {c.left[0][1]:.6f}")
print(f"  junction 2-3 right: Gamma = {c.right[1][0]:.6f}, tau = {c.right[1][1]:.6f}; current refl = {-c.right[1][0]:.6f}")
close("tau_g 3/4, Gamma_g -1/2, G12 1/3, G23 -1/2, current refl +1/2",
      [c.tau_g, c.Gam_g, c.right[0][0], c.right[1][0], -c.right[1][0]], [0.75, -0.5, 1 / 3, -0.5, 0.5])
cr = c.crossings(0, 0.0, 9 * us)   # at z = 0: backward arrivals + forward departures coincide
arr = [(t, w) for (t, w, wi) in cr if wi < 0]          # backward arrivals at z=0
print("  backward arrivals at z = 0 (time us, weight):", [(round(t / us, 3), F(w).limit_denominator(1000)) for t, w in arr])
V0imp = {}
for (t, w, wi) in cr:
    V0imp[round(t / us, 6)] = V0imp.get(round(t / us, 6), 0) + w
print("  impulses in V(0,t) incl. (1+Gamma_g) (time us, weight):",
      [(k_, F(v).limit_denominator(1000)) for k_, v in sorted(V0imp.items())])
close("V(0,t) impulses: 3/4 @0, 1/8 @4, -1/6 @6", [V0imp[0.0], V0imp[4.0], V0imp[6.0]], [0.75, 1 / 8, -1 / 6])
w23 = c.tau_g * c.right[0][1] * c.right[1][0] * c.left[0][1]
print(f"  2-3 echo arriving at z=0: tau_g*tau12*G23*tau21 = {w23:.6f} at t = 2(T1+T2) = {2*(2+1)} us")
close("2-3 echo arrival -1/3", w23, -1 / 3)
crL = c.crossings(2, 3 * us, 12 * us)
print("  load impulses (time us, weight):", [(round(t / us, 3), F(w).limit_denominator(1000)) for (t, w, _) in crL])
close("first load impulse 1/2 at 6 us", [crL[0][0] / us, crL[0][1]], [6.0, 0.5])
# FDTD with a narrow Gaussian (unit area)
sim = FDTD(25.0, lines, joints, 50.0, dt=5 * ns)
n0 = sim.node_at(0, 0.0); nL = sim.node_at(2, 3 * us)
t0p = 0.2 * us
tV, rV, _, _ = sim.run(gauss_pulse(t0p, 25 * ns), 9.0 * us, [n0, nL])
for (tc, wexp) in [(0.0, 0.75), (4.0, 1 / 8), (6.0, -1 / 6)]:
    a_ = area(tV, rV[:, 0], (tc - 0.3) * us + t0p, (tc + 0.3) * us + t0p)
    close(f"FDTD area of V(0,t) near {tc} us", a_, wexp, rtol=3e-3, atol=1e-4)
a_ = area(tV, rV[:, 0], 1.0 * us, 3.8 * us)
close("FDTD: nothing at z=0 between 1 and 3.8 us", a_, 0.0, atol=1e-4)
a_ = area(tV, rV[:, 1], (6 - 0.3) * us + t0p, (6 + 0.3) * us + t0p)
close("FDTD load impulse at 6 us", a_, 0.5, rtol=3e-3)
a_ = area(tV, rV[:, 1], 0, 5.5 * us)
close("FDTD: nothing at load before 6 us", a_, 0.0, atol=1e-4)

# =====================================================================================
hdr("30.9 SP19 E3 #4 style: 80u(t) V, Rg 50; line1 150 ohm 400 m 2e8; line2 50 ohm 300 m 3e8; RL 50")
lines = [(150.0, 400 / 2e8, 400.0), (50.0, 300 / 3e8, 300.0)]
joints = [("direct",)]
c = Circuit(50.0, lines, joints, 50.0)
V0 = 80.0
print(f"  T1 = {lines[0][1]/us} us, T2 = {lines[1][1]/us} us")
print(f"  tau_g = {c.tau_g}, Gamma_g = {c.Gam_g}, Gamma_L = {c.Gam_L}")
print(f"  Gamma12 = {c.right[0][0]}, tau12 = {c.right[0][1]}, current refl = {-c.right[0][0]}, current transm = {1 - c.right[0][0]}")
print(f"  Gamma21 = {c.left[0][0]}, tau21 = {c.left[0][1]}; round trip Gamma12*Gamma_g = {c.right[0][0]*c.Gam_g}")
segs = c.bounce(10.5 * us)
print("  segments (line, dir, start us, end us, weight V):")
for (i, d, t0, w) in segs:
    print(f"     line {i+1} {'->' if d > 0 else '<-'} {t0/us:6.2f} -> {(t0 + lines[i][1])/us:6.2f} : {V0*w:9.4f}")
s100 = 100 / 2e8
cr = c.crossings(0, s100, 9 * us)
print("  crossings at z = 100 m (t us, V weight):", [(round(t / us, 3), round(V0 * w, 4)) for (t, w, _) in cr])
V5, I5 = c.step_VI(0, s100, 5 * us, V0)
print(f"  V(100 m, 5 us) = {V5:.4f} V, I = {I5:.4f} A")
close("V = 45 V, I = 0.7 A", [V5, I5], [45.0, 0.7])
crL = c.crossings(1, lines[1][1], 15 * us)
VL = np.cumsum([V0 * w for (_, w, _) in crL])
print("  load: (t us, arriving V, V_L after):", [(round(t / us, 3), round(V0 * w, 4), round(v, 4)) for (t, w, _), v in zip(crL, VL)])
close("V_L = 30 (3-7 us), 37.5 (7-11 us)", VL[:2], [30.0, 37.5])
VLinf = V0 * c.tau_g * c.right[0][1] / (1 - c.right[0][0] * c.Gam_g)
print(f"  V_L(inf) = {VLinf:.6f} V, I_L(inf) = {VLinf/50:.6f} A; lumped {V0*50/100} V, {V0/100} A")
close("DC", [VLinf, VLinf / 50], [40.0, 0.8])
fsum = V0 * c.tau_g / (1 - c.right[0][0] * c.Gam_g); bsum = V0 * c.tau_g * c.right[0][0] / (1 - c.right[0][0] * c.Gam_g)
print(f"  line-1 forward sum {fsum}, backward sum {bsum}, V = {fsum + bsum}, I = {(fsum - bsum)/150}")
# FDTD
sim = FDTD(50.0, lines, joints, 50.0, dt=2.5 * ns)
n100 = sim.node_at(0, s100); nL = sim.node_at(1, lines[1][1]); b100 = sim.branch_at(0, s100)
tV, rV, tI, rI = sim.run(lambda t: V0 * smooth_step(10 * ns)(t), 60 * us, [n100, nL], [b100])
for tt in [1.0, 4.0, 5.0, 6.0, 8.0, 9.0]:
    Ve, Ie = c.step_VI(0, s100, tt * us, V0)
    close(f"FDTD V,I at 100 m, t = {tt} us", [rV[np.searchsorted(tV, tt * us), 0], rI[np.searchsorted(tI, tt * us), 0]],
          [Ve, Ie], rtol=3e-3, atol=2e-3)
for tt in [2.0, 5.0, 9.0, 12.0]:
    Ve = sum(V0 * w for (t, w, _) in crL if t < tt * us)
    close(f"FDTD V_L at {tt} us", rV[np.searchsorted(tV, tt * us), 1], Ve, rtol=3e-3, atol=2e-3)
close("FDTD V_L, I at 100 m at 60 us -> 40 V, 0.8 A", [rV[-1, 1], rI[-1, 0]], [40.0, 0.8], rtol=1e-3)

# =====================================================================================
hdr("30.10 Locating a splice: Rg = 50, Z1 = 50 (v 2e8), splice, Z2 = ?, air line, short; 18 V 10 ns pulse")
Vs = 18.0
print(f"  launched: {Vs*0.5} V")
G12 = 3.0 / 9.0
Z2 = 50 * (1 + G12) / (1 - G12)
print(f"  Gamma12 = 3/9 = {G12:.6f} -> Z2 = {Z2:.6f} ohm")
d = 2e8 * 1.0 * us / 2
l2 = 3e8 * (1.8 - 1.0) * us / 2
print(f"  splice at {d} m, line-2 length {l2} m")
t12 = 1 + G12; G21 = -G12; t21 = 1 + G21
GL = -8.0 / (9 * t12 * t21)
print(f"  tau12 tau21 = {t12*t21:.6f}; second echo 9*tau12*GL*tau21 = -8 -> GL = {GL:.6f}")
print(f"  ratio of later echoes Gamma21*GL = {G21*GL:.6f}; next echo = {-8/3*G21*GL:.6f} V at {2.6+0.8} us")
lines = [(50.0, d / 2e8, d), (Z2, l2 / 3e8, l2)]
c = Circuit(50.0, lines, [("direct",)], 0)
cr = c.crossings(0, 0.0, 4 * us)
print("  V(0,t) impulses (t us, V):", [(round(t / us, 3), round(Vs * w, 6)) for (t, w, _) in cr])
close("echoes 9, 3, -8, -8/3, -8/9", [Vs * w for (_, w, _) in cr], [9, 3, -8, -8 / 3, -8 / 9])
close("times 0, 1.0, 1.8, 2.6, 3.4 us", [t / us for (t, _, _) in cr], [0, 1.0, 1.8, 2.6, 3.4])
# (e) Rg = 25: launched 12 V, splice echo at 1 us adds (1+Gamma_g)*Gamma12*12
c25 = Circuit(25.0, lines, [("direct",)], 0)
cr25 = c25.crossings(0, 0.0, 1.5 * us)
print(f"  Rg=25: tau_g = {c25.tau_g:.6f}, Gamma_g = {c25.Gam_g:.6f}; V(0) impulses: {[(round(t/us,3), round(Vs*w,6)) for (t,w,_) in cr25]}")
close("Rg = 25: 12 V at 0, 8/3 V at 1 us", [Vs * cr25[0][1], Vs * (cr25[1][1] + cr25[2][1])], [12.0, 8 / 3])
# FDTD with the actual 10 ns pulse (smoothed edges), measure areas / 10 ns
pulse = lambda t: Vs * (smooth_step(2 * ns)(t - 20 * ns) - smooth_step(2 * ns)(t - 30 * ns))
for Rg, expect in [(50.0, [(0.0, 9.0), (1.0, 3.0), (1.8, -8.0), (2.6, -8 / 3), (3.4, -8 / 9)]),
                   (25.0, [(0.0, 12.0), (1.0, 8 / 3)])]:
    sim = FDTD(Rg, lines, [("direct",)], 0, dt=0.5 * ns)
    n0 = sim.node_at(0, 0.0)
    tV, rV, _, _ = sim.run(pulse, 3.6 * us, [n0])
    for (tc, h) in expect:
        a_ = area(tV, rV[:, 0], tc * us - 100 * ns, tc * us + 150 * ns) / (10 * ns)
        close(f"FDTD Rg={Rg}: pulse height near {tc} us", a_, h, rtol=3e-3, atol=3e-3)

# =====================================================================================
hdr("30.11 Tap resistor and open stub: 100u(t), Rg 50, Z1 50 (1 us), shunt 50, Z2 50 (0.5 us), open")
lines = [(50.0, 1 * us, None), (50.0, 0.5 * us, None)]
joints = [("shunt", 50.0)]
c = Circuit(50.0, lines, joints, None)
V0 = 100.0
print(f"  tau_g = {c.tau_g}, Gamma_g = {c.Gam_g}, Gamma_L = {c.Gam_L}")
print(f"  right: Gamma12 = {c.right[0][0]:.6f}, tau12 = {c.right[0][1]:.6f}; left: Gamma21 = {c.left[0][0]:.6f}, tau21 = {c.left[0][1]:.6f}")
close("coefs -1/3, 2/3 both ways", [*c.right[0], *c.left[0]], [-1 / 3, 2 / 3, -1 / 3, 2 / 3])
segs = c.bounce(4.01 * us)
print("  segments (line, dir, start us, end us, weight V):")
for (i, d, t0, w) in segs:
    print(f"     line {i+1} {'->' if d > 0 else '<-'} {t0/us:6.2f} -> {(t0 + lines[i][1])/us:6.2f} : {V0*w:9.4f}  ({F(V0*w).limit_denominator(1000)})")
# junction voltage = running sum of crossings at line-2 local s=0 (forward departures + backward arrivals)
crJ = c.crossings(1, 0.0, 5.01 * us)
VJ = {}
for (t, w, _) in crJ:
    VJ[round(t / us, 6)] = VJ.get(round(t / us, 6), 0) + V0 * w
run = np.cumsum([VJ[k_] for k_ in sorted(VJ)])
print("  V_J steps (t us, V after):", [(k_, round(v, 4), F(v).limit_denominator(1000)) for k_, v in zip(sorted(VJ), run)])
close("V_J: 100/3, 500/9, 1300/27, 4100/81", run[:4], [100 / 3, 500 / 9, 1300 / 27, 4100 / 81])
print(f"  current in R at 2.5 us = {run[1]/50:.6f} A")
crO = c.crossings(1, 0.5 * us, 5.01 * us)
VO = {}
for (t, w, _) in crO:
    VO[round(t / us, 6)] = VO.get(round(t / us, 6), 0) + V0 * w
runO = np.cumsum([VO[k_] for k_ in sorted(VO)])
print("  V_open steps (t us, V after):", [(k_, round(v, 4), F(v).limit_denominator(1000)) for k_, v in zip(sorted(VO), runO)])
# generator current
cr0 = c.crossings(0, 0.0, 4.01 * us)
I0 = {}
for (t, w, wi) in cr0:
    I0[round(t / us, 6)] = I0.get(round(t / us, 6), 0) + V0 * wi / 50
runI = np.cumsum([I0[k_] for k_ in sorted(I0)])
print("  I(0,t) steps (t us, A after):", [(k_, round(v, 4), F(v).limit_denominator(1000)) for k_, v in zip(sorted(I0), runI)])
VJinf = V0 * c.tau_g * c.right[0][1] * (1 + (c.Gam_L * (1 + c.left[0][0])) / (1 - c.Gam_L * c.left[0][0]))
print(f"  V_J(inf) by series = {VJinf:.6f}; lumped 100*50/(50+50) = {100*50/100}; I_R(inf) = {VJinf/50}")
close("V_J inf 50", VJinf, 50.0)
sim = FDTD(50.0, lines, joints, None, dt=1 * ns)
nJ = sim.node_at(1, 0.0); nO = sim.node_at(1, 0.5 * us); n0 = sim.node_at(0, 0.0); b0 = sim.branch_at(0, 0.0)
tV, rV, tI, rI = sim.run(lambda t: V0 * smooth_step(5 * ns)(t), 40 * us, [nJ, nO, n0], [b0])
for (tt, ve) in [(1.5, 100 / 3), (2.5, 500 / 9), (3.5, 1300 / 27), (4.5, 4100 / 81)]:
    close(f"FDTD V_J at {tt} us", rV[np.searchsorted(tV, tt * us), 0], ve, rtol=3e-3)
for (tt, ve) in [(2.0, 200 / 3), (3.0, 400 / 9), (4.0, 1400 / 27)]:
    close(f"FDTD V_open at {tt} us", rV[np.searchsorted(tV, tt * us), 1], ve, rtol=3e-3)
for (tt, ie) in [(1.5, 1.0), (2.5, 4 / 3), (3.5, 8 / 9)]:
    close(f"FDTD I(0) at {tt} us", rI[np.searchsorted(tI, tt * us), 0], ie, rtol=3e-3)
close("FDTD 40 us: V_J, V_open -> 50 V; I(0) -> 1 A", [rV[-1, 0], rV[-1, 1], rI[-1, 0]], [50.0, 50.0, 1.0], rtol=1e-3)

# =====================================================================================
hdr("30.12 Switched-on sine: Rg 150; line1 50 ohm 600 m 2e8; line2 25 ohm 450 m 3e8; RL 25; 14 sin(2 pi f t)")
lines = [(50.0, 600 / 2e8, 600.0), (25.0, 450 / 3e8, 450.0)]
joints = [("direct",)]
c = Circuit(150.0, lines, joints, 25.0)
print(f"  T1 = {lines[0][1]/us} us, T2 = {lines[1][1]/us} us")
print(f"  tau_g = {c.tau_g}, Gamma_g = {c.Gam_g}, Gamma12 = {c.right[0][0]:.6f}, tau12 = {c.right[0][1]:.6f}, Gamma_L = {c.Gam_L}")
crL = c.crossings(1, lines[1][1], 40 * us)
print("  impulse response at the load (t us, weight):", [(round(t / us, 3), F(w).limit_denominator(100000)) for (t, w, _) in crL[:4]])
close("weights 1/6, -1/36, 1/216 at 4.5, 10.5, 16.5", [w for (_, w, _) in crL[:3]], [1 / 6, -1 / 36, 1 / 216])
close("times", [t / us for (t, _, _) in crL[:3]], [4.5, 10.5, 16.5])
print(f"  wavelengths at 1 MHz: line 1 {2e8/1e6} m, line 2 {3e8/1e6} m")


def VL_analytic(t, f):
    return sum(w * 14 * np.sin(2 * np.pi * f * (t - tc)) * (t > tc) for (tc, w, _) in crL)


for f in [1e6, 1.25e6]:
    sim = FDTD(150.0, lines, joints, 25.0, dt=5 * ns)
    nL = sim.node_at(1, lines[1][1])
    src = lambda t, f=f: 14 * np.sin(2 * np.pi * f * t) * (t > 0)
    tV, rV, _, _ = sim.run(src, 60 * us, [nL])
    ts = np.linspace(4.63, 22.4, 41) * us     # spans three epochs at the load
    ana = np.array([VL_analytic(t, f) for t in ts])
    num = np.interp(ts, tV, rV[:, 0])
    close(f"f={f/1e6} MHz: FDTD V_L vs impulse-response sum at sample times", num, ana, rtol=5e-3, atol=5e-3)
    late = np.max(np.abs(rV[tV > 50 * us, 0]))
    late_a = abs(sum(w * np.exp(-2j * np.pi * f * tc) for (tc, w, _) in c.crossings(1, lines[1][1], 400 * us))) * 14
    print(f"  f = {f/1e6} MHz: late amplitude FDTD {late:.5f} V, series {late_a:.6f} V")
    close(f"late amplitude f={f/1e6} MHz", [late, late_a], [2.0 if f == 1e6 else 2.8] * 2, rtol=3e-3)
# the epoch formulas at 1 MHz
for (lo, hi, amp) in [(4.5, 10.5, -7 / 3), (10.5, 16.5, -35 / 18)]:
    tt = np.linspace(lo + 0.01, hi - 0.01, 50) * us
    close(f"V_L = {amp:.6f} sin(2 pi t) on ({lo},{hi}) us", [VL_analytic(t, 1e6) for t in tt],
          amp * np.sin(2 * np.pi * 1e6 * tt), atol=1e-9)
a3 = -35 / 18 - 14 / 216   # third copy: (1/216) * 14 sin(2 pi t - 33 pi) = -(14/216) sin(2 pi t)
tt = np.linspace(16.51, 22.49, 50) * us
close("V_L = -(434/216) sin(2 pi t) on (16.5,22.5) us", [VL_analytic(t, 1e6) for t in tt], a3 * np.sin(2 * np.pi * 1e6 * tt), atol=1e-9)
print(f"  amplitudes per epoch: 7/3 = {7/3:.4f}, 35/18 = {35/18:.4f}, next {abs(a3):.4f} -> 2")
print(f"  DC divider 14*25/175 = {14*25/175}; 1.25 MHz period {1/1.25e6/us} us, 2T1 = {6/0.8} periods")

hdr(f"SUMMARY: {sum(ALL)}/{len(ALL)} checks OK")
