"""Independent check of practice/27-transmission-line-basics.md."""
import numpy as np
from scipy.integrate import quad, solve_ivp

mu0 = 4e-7 * np.pi
e0 = 1e-9 / (36 * np.pi)   # page's eps0
c = 3e8
eta0 = 120 * np.pi
NPASS = NFAIL = 0


def chk(name, got, want, rel=6e-3, absol=None):
    global NPASS, NFAIL
    ok = abs(got - want) <= (absol if absol is not None else rel * abs(want))
    NPASS += ok
    NFAIL += (not ok)
    print(f"{'PASS' if ok else 'FAIL'}  {name}: computed {got:.6g}, page {want:.6g}")


def chkv(name, got, want):
    chk(name, float(np.max(np.abs(np.asarray(got) - np.asarray(want)))), 0.0, absol=1e-9)


# ---- generic line parameters from field integrals ----
def plates_LC(W, d, eps, mu=mu0):
    # C: Q/V with uniform E; L: flux/I with uniform H
    V = 1.0
    E = V / d
    C = eps * E * W / V
    I = 1.0
    H = I / W
    L = mu * H * d / I
    return L, C


def coax_LC(a, b, eps, mu=mu0):
    # energy integrals: W_e = Q^2/2C, W_m = L I^2/2
    Q = 1.0
    We = quad(lambda r: 0.5 * eps * (Q / (2 * np.pi * eps * r))**2 * 2 * np.pi * r, a, b)[0]
    C = Q**2 / (2 * We)
    I = 1.0
    Wm = quad(lambda r: 0.5 * mu * (I / (2 * np.pi * r))**2 * 2 * np.pi * r, a, b)[0]
    L = 2 * Wm / I**2
    return L, C


def twin_LC(a, D, eps, mu=mu0):
    # image line charges at +-h; verify equipotential surface, Gauss, flux
    h = np.sqrt((D / 2)**2 - a**2)
    rl = 1.0
    def pot(x, y):
        return rl / (2 * np.pi * eps) * np.log(np.hypot(x + h, y) / np.hypot(x - h, y))
    th = np.linspace(0, 2 * np.pi, 721)
    Vr = pot(D / 2 + a * np.cos(th), a * np.sin(th))      # wire at +D/2
    Vl = pot(-D / 2 + a * np.cos(th), a * np.sin(th))
    assert np.ptp(Vr) < 1e-9 * abs(Vr.mean())
    # Gauss: flux of eps E around right wire = rl
    dd = 1e-7 * a
    x = D / 2 + a * np.cos(th[:-1]); y = a * np.sin(th[:-1])
    Ex = -(pot(x + dd, y) - pot(x - dd, y)) / (2 * dd)
    Ey = -(pot(x, y + dd) - pot(x, y - dd)) / (2 * dd)
    flux = np.sum(eps * (Ex * np.cos(th[:-1]) + Ey * np.sin(th[:-1]))) * a * (2 * np.pi / 720)
    C = flux / (Vr.mean() - Vl.mean())
    # L: currents +-I at the same image points; flux between wire surfaces
    I = 1.0
    s = D / 2 - a
    By = lambda xx: mu * I / (2 * np.pi) * (1 / (h - xx) + 1 / (h + xx))
    L = quad(By, -s, s)[0] / I
    return L, C


# ======================= 27.1 =======================
print("== 27.1")
W, d, er = 6e-3, 0.5e-3, 2.25
L, C = plates_LC(W, d, er * e0)
v = 1 / np.sqrt(L * C); Z0 = np.sqrt(L / C)
chk("L nH/m", L * 1e9, 104.7)
chk("C pF/m", C * 1e12, 239)
chk("v", v, 2e8)
chk("Z0", Z0, 20 * np.pi / 3)
chk("Z0 20.9", Z0, 20.9)
chk("LC = mu eps", L * C, mu0 * er * e0, rel=1e-12)
chk("(b) ns", 0.3 / v * 1e9, 1.5)
eta = eta0 / np.sqrt(er)
Wn = d * eta / 50
chk("(c) W/d", Wn / d, 5.03)
chk("(c) W mm", Wn * 1e3, 2.51)
L2, C2 = plates_LC(Wn, d, er * e0)
chk("(c) Z0 back", np.sqrt(L2 / C2), 50, rel=1e-9)
chk("check L v", L * v, 20.9)

# ======================= 27.2 =======================
print("== 27.2")
# (e) air coax b=3.5 mm, a = 1 and 0.5 mm, from field integrals
for a_, want in [(1e-3, 75.2), (0.5e-3, 116.8)]:
    L, C = coax_LC(a_, 3.5e-3, e0)
    chk(f"(e) Z0 a={a_*1e3} mm", np.sqrt(L / C), want)
    chk(f"(e) v a={a_*1e3} mm", 1 / np.sqrt(L * C), c)
# (b) swapped ladder (series C, shunt L) is high-pass: |H| at low/high f
def ladder_gain(Zs, Yp, n=20):
    # cascade ABCD, matched-ish 1 ohm load irrelevant; ratio Vout/Vin open
    M = np.eye(2, dtype=complex)
    for _ in range(n):
        M = M @ np.array([[1, Zs], [0, 1]]) @ np.array([[1, 0], [Yp, 1]])
    return abs(1 / M[0, 0])
Ls, Cs = 1e-6, 1e-9
wlo, whi = 1e5, 1e9
print("  swapped ladder |gain| low, high:",
      ladder_gain(1 / (1j * wlo * Cs), 1 / (1j * wlo * Ls)),
      ladder_gain(1 / (1j * whi * Cs), 1 / (1j * whi * Ls)))
# (c),(d) by finite differences on f+g and on g alone
Z0, v = 50.0, 2e8
f = lambda s: np.exp(-(s * 1e9)**2); g = lambda s: 0.5 * np.exp(-((s - 1e-9) * 1e9)**2)
Lp, Cp = Z0 / v, 1 / (Z0 * v)
Vf = lambda z, t: f(t - z / v) + g(t + z / v)
If = lambda z, t: (f(t - z / v) - g(t + z / v)) / Z0
z0, t0, hz, ht = 0.07, 0.2e-9, 1e-5, 1e-14
r1 = -(Vf(z0 + hz, t0) - Vf(z0 - hz, t0)) / (2 * hz) - Lp * (If(z0, t0 + ht) - If(z0, t0 - ht)) / (2 * ht)
r2 = -(If(z0 + hz, t0) - If(z0 - hz, t0)) / (2 * hz) - Cp * (Vf(z0, t0 + ht) - Vf(z0, t0 - ht)) / (2 * ht)
print(f"  telegrapher residuals for V=f+g, I=(f-g)/Z0: {r1:.2e}, {r2:.2e}")
zz = np.array([0.0, 0.1]); tt = 0.3e-9
print("  V/I for f+g at two z:", Vf(zz, tt) / If(zz, tt), "(varies)")
chk("(d) V/I backward", (g(tt + 0.1 / v)) / (-g(tt + 0.1 / v) / Z0), -Z0, rel=1e-12)

# ======================= 27.3 =======================
print("== 27.3")
xh, yh, zh = np.eye(3)
Ey = 1.0; etam = 1.0
E = Ey * yh
H = np.cross(zh, E) / etam
chkv("H = -x Ey/eta", H, -xh * Ey / etam)
n0, nd = yh, -yh
chk("rho_s(y=0) sign", np.sign(np.dot(n0, E)), 1, absol=0)
chk("rho_s(y=d) sign", np.sign(np.dot(nd, E)), -1, absol=0)
chkv("Js(y=0) = +z", np.cross(n0, H), zh * Ey / etam)
chkv("Js(y=d) = -z", np.cross(nd, H), -zh * Ey / etam)
chkv("S along +z", np.cross(E, H) / np.linalg.norm(np.cross(E, H)), zh)
print("  key (c): only (c) true -> PASS by the above")

# ======================= 27.4 =======================
print("== 27.4")
W, d = 1.5e-2, 1e-3
L, C = plates_LC(W, d, e0)
Z0 = np.sqrt(L / C)
chk("Z0", Z0, 8 * np.pi)
chk("Z0 25.1", Z0, 25.1)
P = 100 / (2 * Z0)
chk("<P>", P, 1.99)
chk("<P> exact", P, 100 / (16 * np.pi), rel=1e-12)
chk("student", 100 / (2 * eta0), 0.133)
Ex = 10 / d; Hy = Ex / eta0
chk("Ex", Ex, 1e4); chk("Hy", Hy, 26.5)
S = 0.5 * Ex * Hy
chk("<S> kW/m2", S / 1e3, 132.6)
chk("<S>Wd", S * W * d, 1.99)
chk("I = Hy W", Hy * W, 0.398)
chk("ratio W/d", P / (100 / (2 * eta0)), 15)

# ======================= 27.5 =======================
print("== 27.5")
L, C = 0.4e-6, 40e-12
v = 1 / np.sqrt(L * C); Z0 = np.sqrt(L / C); er = (c / v)**2
chk("v", v, 2.5e8); chk("Z0", Z0, 100); chk("er", er, 1.44)
chk("delay ns", 10 / v * 1e9, 40)
eps = er * e0
# coax: find b/a with field-integral Z0 = 100 (root-find)
from scipy.optimize import brentq
ba = brentq(lambda q: np.sqrt(np.divide(*coax_LC(1e-3, q * 1e-3, eps))) - 100, 1.5, 50)
chk("coax b/a", ba, 7.39)
Lc, Cc = coax_LC(1e-3, ba * 1e-3, eps)
chk("coax L back", Lc, 0.4e-6)
chk("coax C back", Cc, 40e-12)
D2a = brentq(lambda q: np.sqrt(np.divide(*twin_LC(1e-3, 2e-3 * q, eps))) - 100, 1.01, 50)
chk("twin D/2a", D2a, 1.54)
Lt, Ct = twin_LC(1e-3, 2e-3 * D2a, eps)
chk("twin LC = mu eps", Lt * Ct, mu0 * eps, rel=1e-6)
chk("LC = mu0*1.44eps0", L * C, mu0 * 1.44 * e0, rel=1e-9)

# ======================= 27.6 =======================
print("== 27.6")
w, b = 1e9, 5.0
Vf = lambda z, t: 12 * np.cos(w * t + b * z)
If = lambda z, t: -0.2 * np.cos(w * t + b * z)
rng = np.random.default_rng(1)
zs = rng.uniform(0, 1, 5); ts = rng.uniform(0, 1e-8, 5)
hz, ht = 1e-6, 1e-15
dVz = (Vf(zs + hz, ts) - Vf(zs - hz, ts)) / (2 * hz)
dVt = (Vf(zs, ts + ht) - Vf(zs, ts - ht)) / (2 * ht)
dIz = (If(zs + hz, ts) - If(zs - hz, ts)) / (2 * hz)
dIt = (If(zs, ts + ht) - If(zs, ts - ht)) / (2 * ht)
L = np.median(-dVz / dIt); C = np.median(-dIz / dVt)
chk("L nH/m", L * 1e9, 300); chk("C pF/m", C * 1e12, 83.3)
v = 1 / np.sqrt(L * C)
chk("v", v, 2e8)
# direction: track phase constant point
t1, t2 = 0.0, 1e-9
zph = lambda t: (0 - w * t) / b
print("  phase point moves", zph(t2) - zph(t1), "m in 1 ns (negative = -z)")
chk("Z0", np.sqrt(L / C), 60)
chk("V/I", Vf(0.3, 1e-9) / If(0.3, 1e-9), -60)
chk("er", (c / v)**2, 2.25)
tt = np.linspace(0, 2 * np.pi / w, 20001)
pav = np.trapezoid(Vf(0.3, tt) * If(0.3, tt), tt) / tt[-1]
chk("<P>", pav, -1.2)
chk("60 sin coef", -dVz[0] / np.sin(w * ts[0] + b * zs[0]), 60)
chk("2e8 coef", dIt[0] / np.sin(w * ts[0] + b * zs[0]), 2e8)
chk("1.2e10 coef", -dVt[0] / np.sin(w * ts[0] + b * zs[0]), 1.2e10)
chk("LC", L * C, 2.5e-17)

# ======================= 27.7 =======================
print("== 27.7")
ell = 20.0
C = 1.6e-9 / ell; v = ell / 100e-9; er = (c / v)**2
L = 1 / (C * v**2); Z0 = 1 / (C * v)
chk("C", C, 80e-12); chk("v", v, 2e8); chk("er", er, 2.25)
chk("L nH", L * 1e9, 312.5); chk("Z0", Z0, 62.5)
chk("lambda km", v / 1e3 / 1e3, 200); chk("l/lambda", ell / (v / 1e3), 1e-4)
G = 2e-9 / ell
chk("G nS/m", G * 1e9, 0.1)
sig = er * e0 * G / C
chk("sigma", sig, 2.5e-11, rel=0.02)
print(f"  sigma exact {sig:.4g} S/m")
chk("sqrt(L/C)", np.sqrt(L / C), 62.5)
chk("LC", L * C, mu0 * 2.25 * e0, rel=1e-9)
om = 2 * np.pi * 1e3
gam = np.sqrt(1j * om * L * (G + 1j * om * C)); Zc = np.sqrt(1j * om * L / (G + 1j * om * C))
Yin = np.tanh(gam * ell) / Zc
Ylump = G * ell + 1j * om * C * ell
print(f"  open-line Yin vs lumped rel diff {abs(Yin/Ylump-1):.2e}")
chk("Yin = lumped to 6 digits", abs(Yin / Ylump - 1), 0, absol=5e-7)

# ======================= 27.8 =======================
print("== 27.8")
L1, C1, N = 0.5e-6, 200e-12, 30
chk("Z0", np.sqrt(L1 / C1), 50)
chk("delay/section ns", np.sqrt(L1 * C1) * 1e9, 10)
chk("total ns", N * np.sqrt(L1 * C1) * 1e9, 300)
chk("coax length", N * np.sqrt(L1 * C1) * c / 1.5, 60)
chk("I", 2 / 50, 0.04)
chk("charge count", C1 * 2 / np.sqrt(L1 * C1), 0.04)
chk("f max MHz", 1 / (10 * np.sqrt(L1 * C1)) / 1e6, 10)
Tr = 100e-9
vs = lambda t: 2 * np.clip(t / Tr, 0, 1)
def rhs(t, y):
    I = y[:N]; V = y[N:]
    Vprev = np.concatenate(([vs(t)], V[:-1]))
    Inext = np.concatenate((I[1:], [V[-1] / 50.0]))
    return np.concatenate(((Vprev - V) / L1, (I - Inext) / C1))
ts = np.linspace(0, 700e-9, 70001)
sol = solve_ivp(rhs, (0, ts[-1]), np.zeros(2 * N), t_eval=ts, rtol=1e-9, atol=1e-13, max_step=1e-9)
Vout = sol.y[-1]; Iin = sol.y[0]
t50 = ts[np.argmax(Vout >= 1.0)]
delay = t50 - 50e-9
print(f"  ladder delay {delay*1e9:.2f} ns, Iin at 250 ns {np.interp(250e-9, ts, Iin)*1e3:.3f} mA")
chk("sim delay ~300 ns (2%)", delay * 1e9, 300, rel=0.02)
chk("sim Iin ~40 mA (1%)", np.interp(250e-9, ts, Iin), 0.04, rel=0.01)
# ladder Bloch cutoff vs 10 MHz
print(f"  ladder cutoff {1/(np.pi*np.sqrt(L1*C1))/1e6:.1f} MHz")

# ======================= 27.9 =======================
print("== 27.9")
a = 0.4e-3; lnba = 5 / 3; bb = a * np.exp(lnba); er = 4
eps = er * e0
chk("b mm", bb * 1e3, 2.12)
L, C = coax_LC(a, bb, eps)
v = 1 / np.sqrt(L * C); Z0 = np.sqrt(L / C)
chk("L", L * 1e9, 333); chk("C", C * 1e12, 133); chk("v", v, 1.5e8); chk("Z0", Z0, 50)
# outer carries +0.3 A along +z; conductor 2 = inner
I = -0.3; V = Z0 * I
chk("V", V, -15)
# E from Gauss with inner charge per m = C V; H from Ampere with inner current
ql = C * V
Er = lambda r: ql / (2 * np.pi * eps * r)
Hp = lambda r: I / (2 * np.pi * r)
chk("E r coeff", Er(1.0), -9)
chk("H r coeff", Hp(1.0), -0.0477)
chk("V = int E dr", quad(Er, a, bb)[0], -15)
rh, ph = np.array([1, 0, 0.]), np.array([0, 1, 0.])
chkv("ExH dir +z", np.sign(np.cross(np.sign(Er(1)) * rh, np.sign(Hp(1)) * ph)), zh)
chk("rho_s(a) uC", eps * Er(a) * 1e6, -0.796)
chk("rho_s(b) uC", -eps * Er(bb) * 1e6, 0.150)
chk("E(a) kV/m", Er(a) / 1e3, -22.5)
chk("Q/m inner nC", 2 * np.pi * a * eps * Er(a) * 1e9, -2.0)
chk("Q/m outer nC", 2 * np.pi * bb * (-eps * Er(bb)) * 1e9, 2.0)
P = quad(lambda r: Er(r) * Hp(r) * 2 * np.pi * r, a, bb)[0]
chk("P", P, 4.5); chk("VI", V * I, 4.5)
chk("Sz coeff", Er(1) * Hp(1), 2.7 / (2 * np.pi))
chk("energy nJ", P * 4e-9 * 1e9, 18); chk("length", v * 4e-9, 0.6)
Wper = 0.5 * C * V**2 + 0.5 * L * I**2
chk("W' v", Wper * v, 4.5)
chk("Lv", L * v, 50)
f = 300e6
Vt = 15e3 * a * lnba
chk("(d) V", Vt, 10)
beta = 2 * np.pi * f / v
chk("(d) beta", beta, 4 * np.pi); chk("(d) lambda", v / f, 0.5)
chk("(d) <P>", Vt**2 / (2 * Z0), 1)
chk("(d) a+b mm", (a + bb) * 1e3, 2.52)
chk("(d) lambda/pi mm", v / f / np.pi * 1e3, 159)
chk("(d) fc GHz", v / (np.pi * (a + bb)) / 1e9, 19, rel=0.01)

# ======================= 27.10 =======================
print("== 27.10")
Z0, v = 80.0, 2e8
Lp, Cp = Z0 / v, 1 / (Z0 * v)
fw = 0.5 * (12 + Z0 * 0.05); bw = 0.5 * (12 - Z0 * 0.05)
chk("f", fw, 8); chk("g", bw, 4)
# method of lines, staggered grid, DOP853, smoothed edges
dz = 2e-3; zn = np.arange(-6, 6 + dz / 2, dz); zh2 = zn[:-1] + dz / 2
wdt = 4e-3
box = lambda z: 0.5 * (np.tanh((z + 1) / wdt) - np.tanh((z - 1) / wdt))
V0 = 12 * box(zn); I0 = 0.05 * box(zh2)
M = len(zn)
def rhs(t, y):
    V = y[:M]; I = y[M:]
    dV = np.zeros(M); dV[1:-1] = -(I[1:] - I[:-1]) / dz / Cp
    dI = -(V[1:] - V[:-1]) / dz / Lp
    return np.concatenate((dV, dI))
sol = solve_ivp(rhs, (0, 10e-9), np.concatenate((V0, I0)), t_eval=[0, 2.5e-9, 10e-9],
                method="DOP853", rtol=1e-8, atol=1e-10)
def at(k, z):
    V = np.interp(z, zn, sol.y[:M, k]); I = np.interp(z, zh2, sol.y[M:, k]); return V, I
table = [(1, -1.0, 4, -0.05), (1, 0.0, 12, 0.05), (1, 1.0, 8, 0.1),
         (2, -2.0, 4, -0.05), (2, 2.0, 8, 0.1), (2, 0.0, 0, 0), (2, 4.0, 0, 0)]
for k, z, Vw, Iw in table:
    Vs, Is = at(k, z)
    tl = [0, 2.5, 10][k]
    chk(f"sim V t={tl} z={z}", Vs, Vw, rel=2e-3, absol=None if Vw else 1e-2)
    chk(f"sim I t={tl} z={z}", Is, Iw, rel=2e-3, absol=None if Iw else 1e-4)
for z, pw in [(-1.0, -0.2), (0.0, 0.6), (1.0, 0.8)]:
    Vs, Is = at(1, z); chk(f"VI z={z}", Vs * Is, pw, rel=3e-3)
chk("(f^2-g^2)/Z0 mid", (fw**2 - bw**2) / Z0, 0.6, rel=1e-12)
chk("C pF", Cp * 1e12, 62.5); chk("L nH", Lp * 1e9, 400)
W0 = np.trapezoid(0.5 * Cp * V0**2, zn) + np.trapezoid(0.5 * Lp * I0**2, zh2)
chk("W0 nJ (smoothed)", W0 * 1e9, 10, rel=5e-3)
chk("W0 exact", 2 * (0.5 * Cp * 144 + 0.5 * Lp * 0.0025) * 1e9, 10, rel=1e-12)
# energies of separated pulses at 10 ns from the simulation
Vt10 = sol.y[:M, 2]; It10 = sol.y[M:, 2]
right = zn > 0; righth = zh2 > 0
Wr = np.trapezoid(0.5 * Cp * Vt10[right]**2, zn[right]) + np.trapezoid(0.5 * Lp * It10[righth]**2, zh2[righth])
Wl = np.trapezoid(0.5 * Cp * Vt10[~right]**2, zn[~right]) + np.trapezoid(0.5 * Lp * It10[~righth]**2, zh2[~righth])
chk("sim forward pulse nJ", Wr * 1e9, 8, rel=5e-3); chk("sim backward pulse nJ", Wl * 1e9, 2, rel=5e-3)
chk("pass time ns", 2 / v * 1e9, 10)
chk("(e) I", 12 / Z0, 0.15)

# ======================= 27.11 =======================
print("== 27.11")
W, d = 3e-2, 1e-3
v = 30 / 200e-9; er = (c / v)**2
L, C = plates_LC(W, d, er * e0)
Z0 = np.sqrt(L / C)
chk("v", v, 1.5e8); chk("er", er, 4)
chk("v from LC", 1 / np.sqrt(L * C), 1.5e8)
chk("L nH", L * 1e9, 41.9); chk("C nF", C * 1e9, 1.06); chk("Z0", Z0, 2 * np.pi)
Vb = -12.0  # plate 2 (x=0) minus plate 1 (x=d, + terminal)
# FDTD Yee, ideal source V(0)=Vb
nz = 4000; dz = 40.0 / nz; dt = dz / v  # magic step
Vg = np.zeros(nz + 1); Ig = np.zeros(nz)
ts, Vp, Ib = [], [], []
k30 = int(round(30 / dz)); kb = int(round(10 / dz))
t = 0.0
while t < 230e-9:
    Ig -= dt / (L * dz) * (Vg[1:] - Vg[:-1])
    t += dt / 2
    Vg[1:-1] -= dt / (C * dz) * (Ig[1:] - Ig[:-1])
    Vg[0] = Vb
    t += dt / 2
    ts.append(t); Vp.append(Vg[k30]); Ib.append(Ig[kb])
ts = np.array(ts); Vp = np.array(Vp)
tarr = ts[np.argmax(Vp <= Vb / 2)]
chk("FDTD arrival ns", tarr * 1e9, 200.0, rel=2e-3)
chk("FDTD V behind", Vg[kb], -12, rel=1e-3)
chk("FDTD I behind", Ig[kb], -1.910, rel=1e-3)
I = Vb / Z0
chk("I", I, -6 / np.pi, rel=1e-12); chk("I -1.91", I, -1.91)
xh, yh, zh = np.eye(3)
E = xh * Vb / d; H = yh * I / W
chk("Ex kV", E[0] / 1e3, -12); chk("Hy", H[1], -63.7)
chkv("ExH dir", np.cross(np.sign(E), np.sign(H)), zh)
eps = er * e0
for n, rw, Jw in [(xh, -424, -63.7), (-xh, 424, 63.7)]:
    chk("rho_s nC", np.dot(n, eps * E) * 1e9, rw)
    chk("Js z", np.cross(n, H)[2], Jw)
    chk("Js x,y zero", np.abs(np.cross(n, H)[:2]).sum(), 0, absol=1e-12)
chk("1.91 A on + plate", np.cross(-xh, H)[2] * W, 1.91)
# Faraday loop: +x at z1, +z on x=d, -x, -z on x=0 -> normal
nrm = np.cross(xh, zh)
chkv("loop normal -y", nrm, -yh)
chk("C v", C * v, 0.159); chk("L v", L * v, 6.28)
chk("CvV", C * v * Vb, -1.91)
chk("VI W", Vb * I, 22.9)
chk("1/2CV^2 nJ", 0.5 * C * Vb**2 * 1e9, 76.4); chk("1/2LI^2 nJ", 0.5 * L * I**2 * 1e9, 76.4)
chk("storage rate", (0.5 * C * Vb**2 + 0.5 * L * I**2) * v, 22.9)
chk("plate-2 charge/m = CV", eps * E[0] * W, C * Vb, rel=1e-12)

# ======================= 27.12 =======================
print("== 27.12")
a, bb = 1e-3, np.e * 1e-3; lnba = 1.0
eps = 2.25 * e0; sig = 1e-5
Lc, Cc = coax_LC(a, bb, eps)
Gc = Cc * sig / eps  # same GF; verify by current integral below
Ileak = quad(lambda r: 0, 0, 1)[0]
# G by direct leakage: J = sigma E_r, total radial current per m / V
Vv = 1.0
Er = lambda r: Vv / (r * lnba)
Gdir = sig * Er(1.3e-3) * 2 * np.pi * 1.3e-3 / Vv
chk("L nH", Lc * 1e9, 200); chk("C pF", Cc * 1e12, 125)
chk("G uS", Gdir * 1e6, 62.8)
chk("G/C = sig/eps", Gdir / Cc, sig / eps, rel=1e-9)
chk("LC = mu0 eps", Lc * Cc, mu0 * eps, rel=1e-9)
chk("v", 1 / np.sqrt(Lc * Cc), 2e8); chk("Z0", np.sqrt(Lc / Cc), 40)
fx = sig / (2 * np.pi * eps)
chk("crossover kHz", fx / 1e3, 80)
chk("ratio at 10 MHz", sig / (2 * np.pi * 10e6 * eps), 0.008)
# FD curls of 3-D fields from exact lossy-line phasor wave at 50 kHz
om = 2 * np.pi * 50e3
gam = np.sqrt(1j * om * Lc * (Gdir + 1j * om * Cc)); Zc = np.sqrt(1j * om * Lc / (Gdir + 1j * om * Cc))
def fields(x, y, z):
    r2 = x * x + y * y
    V = np.exp(-gam * z); I = V / Zc
    E = np.array([V * x / (r2 * lnba), V * y / (r2 * lnba), 0 * V])
    H = np.array([-I * y / (2 * np.pi * r2), I * x / (2 * np.pi * r2), 0 * V])
    return E, H
def curl(F, p, h):
    J = np.zeros((3, 3), dtype=complex)
    for j, hj in enumerate((1e-6, 1e-6, 0.5)):
        dp = np.zeros(3); dp[j] = hj
        # 4th-order central difference
        J[:, j] = (-F(*(p + 2 * dp)) + 8 * F(*(p + dp)) - 8 * F(*(p - dp)) + F(*(p - 2 * dp))) / (12 * hj)
    return np.array([J[2, 1] - J[1, 2], J[0, 2] - J[2, 0], J[1, 0] - J[0, 1]])
worst = 0
for p in [np.array([1.5e-3, 0.4e-3, 100.0]), np.array([-1.1e-3, 1.7e-3, 2000.0])]:
    cE = curl(lambda x, y, z: fields(x, y, z)[0], p, 1e-7)
    cH = curl(lambda x, y, z: fields(x, y, z)[1], p, 1e-7)
    E, H = fields(*p)
    r1 = np.linalg.norm(cE + 1j * om * mu0 * H) / np.linalg.norm(cE)
    r2 = np.linalg.norm(cH - (sig + 1j * om * eps) * E) / np.linalg.norm(cH)
    worst = max(worst, r1, r2)
print(f"  worst FD curl residual {worst:.1e}")
chk("Maxwell curls satisfied (<1e-5)", worst, 0, absol=1e-5)
# J_s on inner conductor totals I
Iinner = quad(lambda ph: 1.0 / (2 * np.pi * a) * a, 0, 2 * np.pi)[0]
chk("(a) inner current", Iinner, 1.0)

print(f"\nTOTAL PASS {NPASS}  FAIL {NFAIL}")
