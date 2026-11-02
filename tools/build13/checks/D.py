"""Agent D checks: slides Lectures 27, 28, 29 (guided waves, bounce diagrams)."""
import numpy as np

ok_all = True


def chk(name, cond):
    global ok_all
    ok_all &= bool(cond)
    print(("PASS " if cond else "FAIL ") + name)


x, y, z = np.eye(3)
eta0 = 120 * np.pi          # slides use 120*pi
c = 3e8


# ---------- independent line simulation: FDTD leapfrog, magic time step ----------
def fdtd(Z0, Rg, RL, T, vs, tmax, N=480):
    """Lossless line, length 1, delay T. vs(t) open-circuit source.
    Returns (zV, zI, ts, Vhist, Ihist): V at nodes, I at half nodes."""
    dz = 1.0 / N
    dt = T / N                          # v dt = dz
    V = np.zeros(N + 1)
    I = np.zeros(N)
    nsteps = int(round(tmax / dt))
    Vh = np.zeros((nsteps + 1, N + 1))
    Ih = np.zeros((nsteps + 1, N))
    ts = np.arange(nsteps + 1) * dt
    a = 1 / (2 * Z0)
    for n in range(nsteps):
        I = I - (V[1:] - V[:-1]) / Z0               # I at n+1/2
        Vn = V.copy()
        Vn[1:-1] = V[1:-1] - Z0 * (I[1:] - I[:-1])
        s = vs((n + 0.5) * dt)
        if Rg == 0:
            Vn[0] = vs((n + 1) * dt)
        else:
            Vn[0] = (V[0] * (a - 1 / (2 * Rg)) + s / Rg - I[0]) / (a + 1 / (2 * Rg))
        gL = 0 if RL == np.inf else 1 / (2 * RL)
        Vn[-1] = (V[-1] * (a - gL) + I[-1]) / (a + gL)
        V = Vn
        Vh[n + 1] = V
        Ih[n + 1] = I                                # I at t_{n+1} - dt/2
    zV = np.linspace(0, 1, N + 1)
    zI = (np.arange(N) + 0.5) * dz
    return zV, zI, ts, Vh, Ih


def sample(zg, ts, H, zq, tq):
    # mean of two time steps: removes the (-1)^n leapfrog mode
    i = np.argmin(abs(ts - tq))
    k = np.argmin(abs(zg - zq))
    return 0.5 * (H[i, k] + H[i + 1, k])


# ---------- bounce-diagram sum (site's L28 formula, any input) ----------
def coeffs(Z0, Rg, RL):
    tg = Z0 / (Rg + Z0)
    Gg = (Rg - Z0) / (Rg + Z0) if Rg != np.inf else 1.0
    GL = (RL - Z0) / (RL + Z0) if RL != np.inf else 1.0
    return tg, Gg, GL


def bounce(Z0, Rg, RL, T, fi, zz, t, nmax=60):
    """zz in units of the line length (0..1)."""
    tg, Gg, GL = coeffs(Z0, Rg, RL)
    Vp = Vm = 0.0
    for n in range(nmax):
        w = tg * (GL * Gg) ** n
        Vp += w * fi(t - zz * T - 2 * n * T)
        Vm += w * GL * fi(t + zz * T - 2 * (n + 1) * T)
    return Vp + Vm, (Vp - Vm) / Z0


u = lambda t: np.heaviside(t, 1.0) * 1.0

# =====================================================================
# L27
# =====================================================================
# slide 6 slip: [rho_s] = a_n . D, slide writes a cross product
D = 2.0 * x                       # eps*E_x along x
chk("L27 s6: x cross x = 0 (slide's x), dot gives eps*E_x",
    np.allclose(np.cross(x, D), 0) and np.isclose(np.dot(x, D), 2.0))
chk("L27 s6: top plate n=-x gives -eps*E_x", np.isclose(np.dot(-x, D), -2.0))
# slide 7: J_s = n x H on both plates
H = 3.0 * y
chk("L27 s7: Js(x=0) = +H_y z", np.allclose(np.cross(x, H), 3 * z))
chk("L27 s7: Js(x=d) = -H_y z", np.allclose(np.cross(-x, H), -3 * z))
chk("L27 s8: S = E x H along +z", np.allclose(np.cross(x, y), z))

# slide 9: d = 1 cm, w = 20 cm, eps_r = 2.25
d, w = 0.01, 0.2
eta = eta0 / 1.5
Z0 = eta * d / w
chk("L27 s9: eta = 80 pi, Z0 = 4 pi = 12.57 ohm",
    np.isclose(eta, 80 * np.pi) and np.isclose(Z0, 4 * np.pi))


def power_from(E=None, Hy=None, V=None, Ic=None):
    if E is not None:
        Hy = E / eta
    elif Hy is not None:
        E = eta * Hy
    elif V is not None:
        E = V / d
        Hy = E / eta
    else:
        Hy = Ic / w
        E = eta * Hy
    P_field = E * Hy * w * d
    P_circ = (E * d) * (Hy * w)
    return P_field, P_circ, E * d, Hy * w


Pa = power_from(E=300 * np.pi)
Pb = power_from(Hy=7.5)
Pc = power_from(V=4 * np.pi)
Pd = power_from(Ic=0.5)
chk("L27 s9a: E=300pi -> V=3pi, I=0.75, P=2.25pi=7.07 W",
    np.isclose(Pa[0], 2.25 * np.pi) and np.isclose(Pa[1], Pa[0]) and np.isclose(Pa[2], 3 * np.pi)
    and np.isclose(Pa[3], 0.75) and abs(Pa[0] - 7.07) < 0.005)
chk("L27 s9b: H=7.5 -> V=6pi, I=1.5, P=9pi=28.3 W",
    np.isclose(Pb[0], 9 * np.pi) and np.isclose(Pb[2], 6 * np.pi) and np.isclose(Pb[3], 1.5)
    and abs(Pb[0] - 28.27) < 0.005)
chk("L27 s9c: V=4pi -> I=1 A, P=4pi=12.6 W",
    np.isclose(Pc[3], 1.0) and np.isclose(Pc[0], 4 * np.pi) and abs(Pc[0] - 12.57) < 0.005)
chk("L27 s9d: I=0.5 -> V=2pi, P=pi=3.14 W",
    np.isclose(Pd[2], 2 * np.pi) and np.isclose(Pd[0], np.pi))

# slide 10: 300 MHz, 25 cm open line
lam = c / 300e6
chk("L27 s10: lambda = 1 m, 25 cm = lambda/4", np.isclose(lam, 1.0) and np.isclose(0.25, lam / 4))
beta = 2 * np.pi / lam
zz = np.linspace(0, 0.25, 6)
Iz = np.sin(beta * (0.25 - zz))           # open end: I(l) = 0
chk("L27 s10: open quarter-wave current max at source, 0 at open end",
    np.isclose(Iz[0], 1) and np.isclose(Iz[-1], 0) and np.all(np.diff(Iz) < 0))

# slide 21 challenge: (a) false
Wd = eta0 / 50
chk("L27 s21: 50-ohm air plates W/d = 7.54", abs(Wd - 7.54) < 0.01)
ba = np.exp(2 * np.pi * 50 / (eta0 / 1.5))
Zc = (eta0 / 1.5) / (2 * np.pi) * np.log(ba)
chk("L27 s21(c): 50-ohm PE coax b/a=3.49, v=2e8 vs air plates v=3e8, same Z0",
    np.isclose(Zc, 50) and abs(ba - 3.49) < 0.01 and np.isclose(c / 1.5, 2e8))
chk("L27 s21(a): Z0 = eta/GF differs from eta0 (e.g. 12.6 vs 377)", abs(4 * np.pi - eta0) > 1)
# (d) energy split equal for a forward wave
Lp, Cp = Z0 / (c / 1.5), 1 / (Z0 * c / 1.5)
Vf = 1.0
chk("L27 s21(d): (1/2)L I^2 = (1/2)C V^2 for one wave",
    np.isclose(0.5 * Lp * (Vf / Z0) ** 2, 0.5 * Cp * Vf ** 2))

# =====================================================================
# L28 slides 11-22: 100 V, Rg = 40, Z0 = 60, RL = 120, T = 1 us
# =====================================================================
Z0, Rg, RL, T, V0 = 60.0, 40.0, 120.0, 1.0, 100.0
tg, Gg, GL = coeffs(Z0, Rg, RL)
chk("L28 s11: tau_g=0.6, V+=60 V, I+=1 A, GL=1/3, Gg=-1/5",
    np.isclose(tg, 0.6) and np.isclose(tg * V0, 60) and np.isclose(tg * V0 / Z0, 1)
    and np.isclose(GL, 1 / 3) and np.isclose(Gg, -0.2))
chk("L28 s8/12: current coefficients -Gg=1/5, -GL=-1/3", np.isclose(-Gg, 0.2) and np.isclose(-GL, -1 / 3))
wts = [60, 60 * GL, 60 * GL * Gg, 60 * GL * Gg * GL]
chk("L28 s15: weights 60, 20, -4, -4/3 V", np.allclose(wts, [60, 20, -4, -4 / 3]))
iw = [1.0, 1.0 * (-GL), 1.0 * (-GL) * (-Gg)]
chk("L28 s15: current weights 1, -1/3, -1/15 A", np.allclose(iw, [1, -1 / 3, -1 / 15]))
chk("L28 s15: current levels 1, 2/3, 3/5 A", np.allclose(np.cumsum(iw), [1, 2 / 3, 3 / 5]))

# slide 23 (summary) current diagram: weights with -Gg, -GL at the ends
vw, cw = [tg], [tg]
for k in range(1, 6):
    end_v = GL if k % 2 else Gg
    vw.append(vw[-1] * end_v)
    cw.append(cw[-1] * (-end_v))
vw, cw = np.array(vw), np.array(cw)
chk("L28 s23 errata: current weights = voltage weights on forward segments, minus them on backward",
    np.allclose(cw[0::2], vw[0::2]) and np.allclose(cw[1::2], -vw[1::2]))
chk("L28 s23 errata: example's first echo -1/3 A (slide 14), not +1/3 A",
    np.isclose(cw[1] * V0 / Z0, -1 / 3) and np.isclose(vw[1] * V0 / Z0, 1 / 3))

step = lambda t: V0 * u(t)
zV, zI, ts, Vh, Ih = fdtd(Z0, Rg, RL, T, step, tmax=6.0)
cases = [  # (z, t, V expected)  slides 17-19 snapshots, slide 20 V(l/4, t)
    (0.10, 0.25, 60), (0.40, 0.25, 0),
    (0.50, 0.75, 60), (0.90, 0.75, 0),
    (0.25, 1.50, 60), (0.75, 1.50, 80),
    (0.25, 0.10, 0), (0.25, 1.00, 60), (0.25, 2.00, 80), (0.25, 2.50, 76), (0.25, 3.50, 76),
]
for zq, tq, Vex in cases:
    Vb, _ = bounce(Z0, Rg, RL, T, step, zq, tq)
    Vf_ = sample(zV, ts, Vh, zq, tq)
    chk(f"L28 V(z={zq}l, t={tq}us) = {Vex} V (bounce {Vb:.3f}, FDTD {Vf_:.3f})",
        np.isclose(Vb, Vex) and abs(Vf_ - Vex) < 0.05)
for tq, Iex in [(1.0, 1.0), (2.0, 2 / 3), (2.5, 0.6)]:
    _, Ib = bounce(Z0, Rg, RL, T, step, 0.25, tq)
    If_ = sample(zI, ts, Ih, 0.25, tq)
    chk(f"L28 s21: I(l/4, {tq}us) = {Iex:.4f} A (bounce {Ib:.4f}, FDTD {If_:.4f})",
        np.isclose(Ib, Iex) and abs(If_ - Iex) < 2e-3)
chk("L28 s20-21: crossing times at l/4 are 0.25, 1.75, 2.25 us",
    np.allclose([0.25, 2 - 0.25, 2 + 0.25], [0.25, 1.75, 2.25]))
Vnext, _ = bounce(Z0, Rg, RL, T, step, 0.25, 3.9)
chk("L28: next level at l/4 from 3.75 us is 74.67 V", np.isclose(Vnext, 76 - 4 / 3))

# slide 22 challenge: 30 V, Rg 20, Z0 10, RL 30, T 1 us: V(L, 1.01 us)
Z0c, Rgc, RLc = 10.0, 20.0, 30.0
s30 = lambda t: 30 * u(t)
tgc, Ggc, GLc = coeffs(Z0c, Rgc, RLc)
Vb, _ = bounce(Z0c, Rgc, RLc, 1.0, s30, 1.0, 1.01)
zV2, zI2, ts2, Vh2, Ih2 = fdtd(Z0c, Rgc, RLc, 1.0, s30, tmax=40.0, N=400)
Vf_ = sample(zV2, ts2, Vh2, 1.0, 1.01)
chk(f"L28 s22: tau_g=1/3, V+=10 V, GL=1/2, V(L,1.01us)=15 V (b) (FDTD {Vf_:.3f})",
    np.isclose(tgc, 1 / 3) and np.isclose(GLc, 0.5) and np.isclose(Vb, 15) and abs(Vf_ - 15) < 0.05)

# =====================================================================
# L29 slides 2-5: steady state of the L28 circuit
# =====================================================================
r = GL * Gg
S = 1 / (1 - r)
chk("L29 s3: GL*Gg = -1/15, sum = 15/16", np.isclose(r, -1 / 15) and np.isclose(S, 15 / 16))
Vp, Vm = 60 * S, 20 * S
Ip, Im = 1 * S, -1 / 3 * S
chk("L29 s3: V+ss=56.25, V-ss=18.75, I+ss=0.9375, I-ss=-0.3125",
    np.allclose([Vp, Vm, Ip, Im], [56.25, 18.75, 0.9375, -0.3125]))
chk("L29 s4: Vss=75 V = 100*120/160, Iss=0.625 A = 100/160",
    np.isclose(Vp + Vm, 75) and np.isclose(V0 * RL / (Rg + RL), 75)
    and np.isclose(Ip + Im, 0.625) and np.isclose(V0 / (Rg + RL), 0.625))
Vss = sample(zV, ts, Vh, 0.5, 5.5)
Iss = sample(zI, ts, Ih, 0.5, 5.5)
chk(f"L29 s4: FDTD at 5.5 us, z=l/2: V={Vss:.3f}, I={Iss:.4f}", abs(Vss - 75) < 0.1 and abs(Iss - 0.625) < 2e-3)
chk("L29 s3: FDTD split (V+Z0 I)/2=56.25, (V-Z0 I)/2=18.75",
    abs((Vss + Z0 * Iss) / 2 - 56.25) < 0.1 and abs((Vss - Z0 * Iss) / 2 - 18.75) < 0.1)
chk("L29 s3-4: V+ss/I+ss = Z0, Vss/Iss = RL", np.isclose(Vp / Ip, Z0) and np.isclose((Vp + Vm) / (Ip + Im), RL))

# slide 5 challenge: I(L, inf) for the 30 V circuit
IL = sample(zI2, ts2, Ih2, 1.0, 39.0)
chk(f"L29 s5: I(L,inf) = 30/50 = 0.6 A (c) (FDTD {IL:.4f})", np.isclose(30 / (20 + 30), 0.6) and abs(IL - 0.6) < 2e-3)

# slide 3 slip: condition must be |Gg GL| < 1 (Gg=-1, GL=+1 gives -1 < 1 but never settles)
lev = []
for tq in [1, 3, 5, 7, 9, 11]:
    Vb, _ = bounce(1.0, 0.0, np.inf, 2.0, u, 0.5, tq, nmax=20)
    lev.append(Vb)
chk(f"L29 s3 errata: ideal source + open load (Gg*GL=-1) at l/2 cycles {lev}",
    np.allclose(lev, [1, 2, 1, 0, 1, 2]))

# =====================================================================
# L29 slides 6-9, 15: general solution (round-trip equation) vs FDTD for a pulse
# slides 10-14: Z0 50, v = c, l = 2400 m, Rg = 0, RL = 100 -> T = 8 us
# =====================================================================
Z0, Rg, RL, T = 50.0, 0.0, 100.0, 8.0
tg, Gg, GL = coeffs(Z0, Rg, RL)
chk("L29 s10: T = 2400/300 = 8 us, tau_g=1, Gg=-1, GL=1/3",
    np.isclose(2400 / 300, T) and np.isclose(tg, 1) and np.isclose(Gg, -1) and np.isclose(GL, 1 / 3))
# slide 6 time windows: backward segment n=0 at z=l at T, at z=0 at 2T
chk("L29 s6: delta(t-2T+z/v) fires at t=T (z=l) and t=2T (z=0)",
    np.isclose(2 * T - T * 1.0, T) and np.isclose(2 * T - 0, 2 * T))

# Example 1 (slide 10): h_1200(t) crossing times and weights
times, wts = [], []
for n in range(3):
    times += [T / 2 + 2 * n * T, 2 * T - T / 2 + 2 * n * T]
    wts += [tg * (GL * Gg) ** n, tg * GL * (GL * Gg) ** n]
chk(f"L29 s10: h_1200 impulses at {times} us, weights 1, 1/3, -1/3, -1/9, 1/9, 1/27",
    np.allclose(times, [4, 12, 20, 28, 36, 44]) and np.allclose(wts, [1, 1 / 3, -1 / 3, -1 / 9, 1 / 9, 1 / 27]))

# Example 2 (slides 11-13): unit step; LTspice levels
zV, zI, ts, Vh, Ih = fdtd(Z0, Rg, RL, T, u, tmax=64.0, N=400)
for tq, Vex in [(2, 0), (8, 1), (16, 4 / 3), (24, 1), (32, 8 / 9), (40, 1), (48, 28 / 27)]:
    Vb, _ = bounce(Z0, Rg, RL, T, u, 0.5, tq)
    Vf_ = sample(zV, ts, Vh, 0.5, tq)
    chk(f"L29 s11: V(1200,{tq}us) = {Vex:.4f} (bounce {Vb:.4f}, FDTD {Vf_:.4f})",
        np.isclose(Vb, Vex) and abs(Vf_ - Vex) < 2e-3)
for tq, Iex in [(8, 20e-3), (24, 20e-3 / 3), (40, 5 / 9 * 20e-3), (56, 13 / 27 * 20e-3)]:
    _, Ib = bounce(Z0, Rg, RL, T, u, 0.0, tq)
    If_ = sample(zI, ts, Ih, 0.0, tq)
    chk(f"L29 s13: I(0,{tq}us) = {Iex*1e3:.2f} mA (bounce {Ib*1e3:.3f}, FDTD {If_*1e3:.3f})",
        np.isclose(Ib, Iex) and abs(If_ - Iex) < 5e-5)
for tq, Vex in [(4, 0), (16, 4 / 3), (32, 8 / 9), (48, 28 / 27)]:
    Vb, Ib = bounce(Z0, Rg, RL, T, u, 1.0, tq)
    Vf_ = sample(zV, ts, Vh, 1.0, tq)
    chk(f"L29 s13: V(2400,{tq}us) = {Vex:.4f}, I = V/100 (FDTD {Vf_:.4f})",
        np.isclose(Vb, Vex) and abs(Vf_ - Vex) < 2e-3 and np.isclose(Ib, Vex / 100))
chk("L29 s13: I(2400) levels 13.3, 8.89, 10.37 mA",
    np.allclose(np.round(np.array([4 / 3, 8 / 9, 28 / 27]) / 100 * 1e3, 2), [13.33, 8.89, 10.37]))
chk("L29 s13 errata: a trace first stepping at 8 us is z = v*8us = 2400 m, not 1200 m",
    np.isclose(300 * 8, 2400) and not np.isclose(300 * 8, 1200))
chk("L29 s12: steady state at 1200 m: 1 V, 10 mA", np.isclose(1 * RL / (0 + RL), 1) and np.isclose(1 / RL, 0.01))

# Example 3 (slide 14): f_i = u(t-4) - u(t), a -1 V pulse 0<t<4 us
f3 = lambda t: u(t - 4) - u(t)
chk("L29 s14: u(t-4)-u(t) = -1 on (0,4), 0 elsewhere",
    np.allclose([f3(-1), f3(2), f3(5)], [0, -1, 0]))
zV, zI, ts, Vh, Ih = fdtd(Z0, Rg, RL, T, f3, tmax=50.0, N=400)
exp3 = [(2, 0), (6, -1), (10, 0), (14, -1 / 3), (18, 0), (22, 1 / 3), (26, 0),
        (30, 1 / 9), (34, 0), (38, -1 / 9), (42, 0), (46, -1 / 27)]
for tq, Vex in exp3:
    Vb, _ = bounce(Z0, Rg, RL, T, f3, 0.5, tq)
    Vf_ = sample(zV, ts, Vh, 0.5, tq)
    chk(f"L29 s14: V(1200,{tq}us) = {Vex:+.4f} (bounce {Vb:+.4f}, FDTD {Vf_:+.4f})",
        np.isclose(Vb, Vex) and abs(Vf_ - Vex) < 2e-3)
Vlate, _ = bounce(Z0, Rg, RL, T, f3, 0.5, 400.0, nmax=200)
chk("L29 s14: settles to 0 (input settles to 0)", abs(Vlate) < 1e-9)

print("ALL PASS" if ok_all else "SOME FAILED")
