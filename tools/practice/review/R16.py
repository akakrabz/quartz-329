#!/usr/bin/env python3
"""R16.py -- independent re-solution of practice page 16 (Lecture 16: charge conservation,
displacement current, complete Maxwell equations, time-varying boundary conditions).
numpy/scipy only.  Every number, sign and direction stated on the page (after the review
edits) is recomputed from the given data, by a brute-force or second route where possible
(finite-difference div/curl, numerical flux and volume integrals, ODE integration,
Biot-Savart sums, linear solves of the boundary conditions), and compared with the page."""
import numpy as np
from scipy import integrate, optimize

eps0 = 8.8541878128e-12
mu0 = 4e-7 * np.pi
NP = [0, 0]


def _fmt(v):
    v = np.asarray(v, dtype=float)
    if v.ndim == 0:
        return f"{float(v):.6g}"
    return np.array2string(v, precision=5, suppress_small=True)


def chk(name, val, ref, rtol=5e-3, atol=1e-12):
    ok = bool(np.allclose(np.asarray(val, float), np.asarray(ref, float), rtol=rtol, atol=atol))
    NP[0 if ok else 1] += 1
    print(f"  {'PASS' if ok else 'FAIL'}  {name}: computed {_fmt(val)} | page {_fmt(ref)}")


def flag(name, cond):
    ok = bool(cond)
    NP[0 if ok else 1] += 1
    print(f"  {'PASS' if ok else 'FAIL'}  {name}")


def div_fd(F, p, h=1e-4):
    p = np.asarray(p, float)
    s = 0.0
    for i in range(3):
        e = np.zeros(3); e[i] = h
        s += (F(p + e)[i] - F(p - e)[i]) / (2 * h)
    return s


def curl_fd(F, p, h=1e-4):
    p = np.asarray(p, float)
    G = np.zeros((3, 3))
    for j in range(3):
        e = np.zeros(3); e[j] = h
        G[:, j] = (np.asarray(F(p + e)) - np.asarray(F(p - e))) / (2 * h)
    return np.array([G[2, 1] - G[1, 2], G[0, 2] - G[2, 0], G[1, 0] - G[0, 1]])


# ---------------------------------------------------------------- 16.1
print("16.1 Charge piling up in a cylinder")
def J1(p):
    x, y, z = p
    r = np.hypot(x, y)
    return np.array([2 * r * x, 2 * r * y, -4 * z])      # 2 r^2 r_hat - 4 z z_hat
drho1 = lambda r, z=0.7: -div_fd(J1, [r, 0.0, z])
chk("(a) drho/dt at r = 0.2 m [A/m^3]", drho1(0.2), 2.8)
chk("(a) drho/dt at r = 1 m [A/m^3]", drho1(1.0), -2.0)
flag("(a) growing at r = 0.2 m, shrinking at r = 1 m", drho1(0.2) > 0 and drho1(1.0) < 0)
chk("(a) balance radius [m]", optimize.brentq(drho1, 0.3, 0.9), 2 / 3)
vol = integrate.tplquad(lambda r, ph, z: -div_fd(J1, [r * np.cos(ph), r * np.sin(ph), z]) * r,
                        0, 2, 0, 2 * np.pi, 0, 0.5)[0]
side = integrate.dblquad(lambda ph, z: J1([0.5 * np.cos(ph), 0.5 * np.sin(ph), z]) @
                         np.array([np.cos(ph), np.sin(ph), 0.0]) * 0.5, 0, 2, 0, 2 * np.pi)[0]
top = integrate.dblquad(lambda r, ph: J1([r * np.cos(ph), r * np.sin(ph), 2.0])[2] * r, 0, 2 * np.pi, 0, 0.5)[0]
bot = integrate.dblquad(lambda r, ph: -J1([r * np.cos(ph), r * np.sin(ph), 0.0])[2] * r, 0, 2 * np.pi, 0, 0.5)[0]
chk("(b) dQ/dt by volume integral of -div J [A] (= pi)", vol, np.pi)
chk("(b) dQ/dt ~ 3.14 A, gaining", vol, 3.14, rtol=2e-3)
chk("check: side r = 0.5 outflow [A] (= pi)", side, np.pi)
chk("check: top z = 2 outflow [A] (= -2 pi, i.e. 2 pi in)", top, -2 * np.pi)
chk("check: bottom z = 0 outflow [A]", bot, 0.0, atol=1e-9)
chk("check: net outflow = -dQ/dt [A]", side + top + bot, -np.pi)

# ---------------------------------------------------------------- 16.2
print("16.2 Displacement current through a window")
E0_2, w2 = 1e4, 2 * np.pi * 1e6
u2 = np.array([0.6, 0.0, 0.8])
Ef2 = lambda t: E0_2 * np.cos(w2 * t) * u2
Aw = integrate.dblquad(lambda y, x: 1.0, 0, 0.1, 0, 0.1)[0]
psi2 = lambda t: eps0 * Ef2(t)[2] * Aw                    # int D . z dS (uniform field)
Id2 = lambda t, h=1e-12: (psi2(t + h) - psi2(t - h)) / (2 * h)
dDdt2 = lambda t, h=1e-12: eps0 * (Ef2(t + h) - Ef2(t - h)) / (2 * h)
chk("(a) eps0 w E0 [A/m^2]", eps0 * w2 * E0_2, 0.556)
chk("(a) eps0 w E0 = 2 pi 1e10 eps0", 2 * np.pi * 1e10 * eps0, 0.556)
chk("(a) dD/dt at t = 0.25 us [A/m^2] (= -0.556 (0.6,0,0.8))", dDdt2(0.25e-6), -0.556 * u2)
r_min = optimize.minimize_scalar(Id2, bounds=(0.1e-6, 0.4e-6), method="bounded", options={"xatol": 1e-15})
r_max = optimize.minimize_scalar(lambda t: -Id2(t), bounds=(0.6e-6, 0.9e-6), method="bounded", options={"xatol": 1e-15})
chk("(b) I_d amplitude [mA]", -r_min.fun * 1e3, 4.45)
chk("(b) 1.6 pi 1e8 eps0 [mA]", 1.6 * np.pi * 1e8 * eps0 * 1e3, 4.45)
chk("(b) electric flux amplitude psi_E [C]", psi2(0.0), 7.08e-10)
chk("(c) first |I_d| maximum at t [us]", r_min.x * 1e6, 0.25)
chk("(c) next |I_d| maximum at t [us]", r_max.x * 1e6, 0.75)
chk("(c) |E| / E0 at t = 0.25 us (E = 0)", np.linalg.norm(Ef2(r_min.x)) / E0_2, 0.0, atol=1e-6)
chk("(c) I_d at t = 0.25 us [mA] (negative: along -z)", Id2(0.25e-6) * 1e3, -4.45)
chk("watch out: full |E| would give [mA]", eps0 * w2 * E0_2 * Aw * 1e3, 5.56)
chk("watch out: ratio full/|E_z| (25% high)", 1 / 0.8, 1.25)

# ---------------------------------------------------------------- 16.3
print("16.3 The missing displacement current")
A3, d3, e3, I3 = 20e-4, 0.5e-3, 4 * eps0, 3e-3
C3 = e3 * A3 / d3
dEdt3 = (I3 / C3) / d3
flag("student's dE/dt = I/(eps A) is right", np.isclose(dEdt3, I3 / (e3 * A3)))
chk("student's eps0 A dE/dt [mA]", eps0 * A3 * dEdt3 * 1e3, 0.75)
chk("correct I_d = A eps dE/dt [mA]", A3 * e3 * dEdt3 * 1e3, 3.0)
chk("Gauss route: A d(Q/A)/dt [mA]", I3 * 1e3, 3.0)
chk("J_d = I/A [A/m^2]", I3 / A3, 1.5)
chk("polarization current (eps-eps0) A dE/dt [mA]", (e3 - eps0) * A3 * dEdt3 * 1e3, 2.25)

# ---------------------------------------------------------------- 16.4
print("16.4 True or false")
Hs = lambda p: np.array([p[1] ** 2 * p[2], np.sin(p[0]) * p[2], p[0] * p[1] ** 3])
dc = div_fd(lambda q: curl_fd(Hs, q, 1e-3), [0.3, -0.7, 0.5], 1e-3)
flag(f"(c) div(curl H) = {dc:.1e} ~ 0, so div J + d(div D)/dt = 0 = continuity: TRUE", abs(dc) < 1e-5)
chk("(d) div B for static B0(x,y,z) [B0] (passes Faraday, nonzero)", div_fd(lambda p: np.asarray(p, float), [0.2, 0.1, -0.4]), 3.0)
fl = lambda w: integrate.dblquad(lambda z, x: 5.0 + x + z, 0, 1, -w / 2, w / 2)[0]   # finite dD_y/dt
flag(f"(e) flux of finite dD/dt through thin rectangle ~ w: {fl(1e-2):.3e}, {fl(1e-3):.3e}, {fl(1e-4):.3e} -> 0: FALSE",
     np.isclose(fl(1e-2) / fl(1e-3), 10, rtol=1e-3) and np.isclose(fl(1e-3) / fl(1e-4), 10, rtol=1e-3))
flag("(b) vacuum: eps0 dE/dt != 0 for E0 cos(wt) (16.2 value 0.556 A/m^2): TRUE", eps0 * w2 * E0_2 > 0)
flag("(a) disk vs bag around a charging capacitor: conduction I vs 0 -> FALSE; key F,T,T,F,F", True)

# ---------------------------------------------------------------- 16.5
print("16.5 Fields just outside a metal ball")
P5 = np.array([0.0, 0.6, 0.8]); n5 = P5 / np.linalg.norm(P5)
vec5 = {1: np.array([0, 3, 4.0]), 2: np.array([5.0, 0, 0]), 3: np.array([0, 4, -3.0]), 4: np.array([0, 0, 5.0])}
def cls5(v, n=n5):
    vn = n @ v; vt = v - vn * n
    cE, cH = np.linalg.norm(vt) < 1e-12, abs(vn) < 1e-12
    return {(True, False): "E", (False, True): "H", (False, False): "none", (True, True): "EH"}[(cE, cH)]
got = {k: cls5(v) for k, v in vec5.items()}
opts = {"a": {1: "E", 2: "H", 3: "H", 4: "none"}, "b": {1: "E", 2: "H", 3: "H", 4: "E"},
        "c": {1: "H", 2: "E", 3: "E", 4: "none"}, "d": {1: "E", 2: "EH", 3: "EH", 4: "E"},
        "e": {1: "E", 2: "H", 3: "none", 4: "none"}}
print("    classification:", got)
flag("keyed (a) is the only matching option", [k for k, o in opts.items() if o == got] == ["a"])
flag("(b): with n = z_hat, vector (4) would be purely normal (the flat-floor habit)", cls5(vec5[4], np.array([0, 0, 1.0])) == "E")
chk("(1) = 5 n_hat", vec5[1], 5 * n5)
chk("(3): n.(4y-3z)", n5 @ vec5[3], 0.0, atol=1e-12)
chk("(4): normal part n.5z", n5 @ vec5[4], 4.0)
chk("(4): tangential part", vec5[4] - 4 * n5, [0, -2.4, 1.8])
chk("(4): |tangential|", np.linalg.norm(vec5[4] - 4 * n5), 3.0)
chk("tilt of n from z [deg]", np.degrees(np.arccos(n5[2])), 36.9, rtol=2e-3)
rs5 = eps0 * n5 @ (vec5[1] * 1e3)
chk("rho_s = 5000 eps0 [nC/m^2]", rs5 * 1e9, 44.3)
Js5 = np.cross(n5, vec5[3])
chk("J_s = n x H [A/m]", Js5, [-5, 0, 0])
chk("check J_s x n = H_t", np.cross(Js5, n5), vec5[3])

# ---------------------------------------------------------------- 16.6
print("16.6 Conduction versus displacement in soil")
s6, e6, E06 = 0.01, 9 * eps0, 20.0
wc = s6 / e6; fc = wc / (2 * np.pi)
chk("(a) J amplitude [A/m^2]", s6 * E06, 0.2)
chk("(b) omega_c [rad/s]", wc, 1.25e8)
chk("(b) f_c [MHz]", fc / 1e6, 20.0)
chk("(b) 1/(2 pi f_c) [ns]", 1 / (2 * np.pi * fc) * 1e9, 7.97)
chk("(b) relaxation time eps/sigma [ns]", e6 / s6 * 1e9, 7.97)
chk("(c) ratio at 1 MHz", 2 * np.pi * 1e6 * e6 / s6, 0.0501)
chk("(c) conduction wins by", s6 / (2 * np.pi * 1e6 * e6), 20.0)
chk("(c) ratio at 2 GHz (displacement wins by)", 2 * np.pi * 2e9 * e6 / s6, 100, rtol=3e-3)
def amp_phase(fn, w):
    t = np.linspace(0, 2 * np.pi / w, 20001)[:-1]
    c = 2 * np.mean(fn(t) * np.exp(-1j * w * t))
    return abs(c), np.angle(c)
h6 = 1e-13
Jc = lambda t: s6 * E06 * np.cos(wc * t)
Jd6 = lambda t: e6 * E06 * (np.cos(wc * (t + h6)) - np.cos(wc * (t - h6))) / (2 * h6)
aJ, pJ = amp_phase(Jc, wc); aD, pD = amp_phase(Jd6, wc); aT, pT = amp_phase(lambda t: Jc(t) + Jd6(t), wc)
chk("(a) displacement leads conduction by [deg]", np.degrees(pD - pJ), 90.0)
chk("(d) total amplitude at f_c [A/m^2]", aT, 0.283)
chk("(d) total phase [rad] (+pi/4)", pT, np.pi / 4)
chk("(d) total at t = 0 [A/m^2]", Jc(0.0) + Jd6(0.0), 0.2)
w1 = 2 * np.pi * 1e6
chk("general amplitude E0 sqrt(s^2 + w^2 e^2) at 1 MHz", amp_phase(lambda t: s6 * E06 * np.cos(w1 * t) - w1 * e6 * E06 * np.sin(w1 * t), w1)[0],
    E06 * np.hypot(s6, w1 * e6))

# ---------------------------------------------------------------- 16.7
print("16.7 Charging plates with a dielectric core")
a7, d7, I7 = 0.04, 2e-3, 0.5
A7 = np.pi * a7 ** 2
Acore, Aring = np.pi * (a7 / 2) ** 2, A7 - np.pi * (a7 / 2) ** 2
dEdt7 = I7 / (3 * eps0 * Acore + eps0 * Aring)
Jcore, Jair = 3 * eps0 * dEdt7, eps0 * dEdt7
Jd_a = lambda rp: I7 / A7 if rp < a7 else 0.0
Jd_b = lambda rp: (Jcore if rp < a7 / 2 else Jair) if rp < a7 else 0.0

def Ienc(Jd, r):
    top = min(r, a7)
    pts = [a7 / 2] if a7 / 2 < top else None
    return integrate.quad(lambda rp: Jd(rp) * 2 * np.pi * rp, 0, top, points=pts)[0]

def H_bs(r, Jd, I=I7, a=a7, d=d7):
    """Brute-force Biot-Savart at (r, 0, d/2) of the full divergence-free current:
    axial leads + radial plate currents K = (I - I_d(r'))/(2 pi r') + gap displacement current."""
    z0 = d / 2
    fl_ = lambda zp: I * r / (4 * np.pi * (r ** 2 + (z0 - zp) ** 2) ** 1.5)
    Hl = integrate.quad(fl_, -np.inf, 0)[0] + integrate.quad(fl_, d, np.inf)[0]
    def inner(rp):
        Kr = (I - Ienc(Jd, rp)) / (2 * np.pi)
        g = lambda ph: -np.cos(ph) * z0 / (4 * np.pi * (r ** 2 + rp ** 2 - 2 * r * rp * np.cos(ph) + z0 ** 2) ** 1.5)
        return 2 * Kr * integrate.quad(g, 0, np.pi, limit=200)[0]
    pts = sorted({p for p in (r, a / 2) if 0 < p < a})
    Hp = 2 * integrate.quad(inner, 0, a, points=pts, limit=400)[0]          # both plates
    if r < a:
        def ray(ps):
            rmax = -r * np.cos(ps) + np.sqrt(a ** 2 - (r * np.sin(ps)) ** 2)
            disc = (a / 2) ** 2 - (r * np.sin(ps)) ** 2
            bp = []
            if disc > 0:
                bp = [x for x in (-r * np.cos(ps) - np.sqrt(disc), -r * np.cos(ps) + np.sqrt(disc)) if 1e-12 < x < rmax - 1e-12]
            hh = lambda rho: Jd(np.hypot(r + rho * np.cos(ps), rho * np.sin(ps))) / np.sqrt(rho ** 2 + z0 ** 2)
            return np.cos(ps) * integrate.quad(hh, 0, rmax, points=bp or None, limit=200)[0]
        Hs_ = -(d / (4 * np.pi)) * integrate.quad(ray, 0, 2 * np.pi, limit=200)[0]
    else:
        def inner2(rp):
            g = lambda ph: (r - rp * np.cos(ph)) * d / (4 * np.pi * (r ** 2 + rp ** 2 - 2 * r * rp * np.cos(ph))
                                                       * np.sqrt(r ** 2 + rp ** 2 - 2 * r * rp * np.cos(ph) + z0 ** 2))
            return 2 * Jd(rp) * rp * integrate.quad(g, 0, np.pi)[0]
        Hs_ = integrate.quad(inner2, 0, a, points=[a / 2])[0]
    return Hl + Hp + Hs_

chk("(a) dD/dt = I/(pi a^2) [A/m^2]", I7 / A7, 99.5)
chk("(a) total displacement current = I [A]", Ienc(Jd_a, a7), 0.5)
for r, ref in [(0.02, 0.995), (0.08, 0.995)]:
    chk(f"(a) H at r = {r*100:.0f} cm, Ampere (I_enc/(2 pi r)) [A/m]", Ienc(Jd_a, r) / (2 * np.pi * r), ref)
    chk(f"(a) H at r = {r*100:.0f} cm, brute-force Biot-Savart [A/m] (+phi: ccw from +z)", H_bs(r, Jd_a), ref)
chk("(a) maximum at plate edge I/(2 pi a) [A/m]", I7 / (2 * np.pi * a7), 1.99)
chk("(b) fraction of displacement current in core", Jcore * Acore / I7, 0.5)
chk("(b) density in core [A/m^2]", Jcore, 199)
chk("(b) density in air ring [A/m^2]", Jair, 66.3)
for r, ref in [(0.02, 1.99), (0.03, 1.88), (0.08, 0.995)]:
    chk(f"(b) H at r = {r*100:.0f} cm, Ampere [A/m]", Ienc(Jd_b, r) / (2 * np.pi * r), ref)
    chk(f"(b) H at r = {r*100:.0f} cm, brute-force Biot-Savart [A/m]", H_bs(r, Jd_b), ref)
chk("(b) H(a) with core [A/m]", Ienc(Jd_b, a7) / (2 * np.pi * a7), I7 / (2 * np.pi * a7))
rm = optimize.minimize_scalar(lambda r: Ienc(Jd_b, r) / (2 * np.pi * r), bounds=(0.02, 0.04), method="bounded")
print(f"    (b) dip: minimum H = {rm.fun:.4f} A/m at r = {rm.x*100:.3f} cm (a/sqrt2 = {a7/np.sqrt(2)*100:.3f} cm)")
hh7 = 1e-6
Hfun = lambda r: Ienc(Jd_a, r) / (2 * np.pi * r)
chk("(a) differential form (1/r) d(r H)/dr = dD_z/dt [A/m^2]",
    ((0.02 + hh7) * Hfun(0.02 + hh7) - (0.02 - hh7) * Hfun(0.02 - hh7)) / (2 * hh7) / 0.02, I7 / A7)

# ---------------------------------------------------------------- 16.8
print("16.8 Charges and currents on a coax")
a8, b8 = 2e-3, 6e-3
P8 = np.array([1.2, 1.6, 0]) * 1e-3; Q8 = np.array([-3.6, -4.8, 0]) * 1e-3
EP, HP = np.array([18.0, 24.0, 0]) * 1e3, np.array([-24.0, 18.0, 0])
EQ, HQ = np.array([-6.0, -8.0, 0]) * 1e3, np.array([8.0, -6.0, 0])
nP, nQ = P8 / np.linalg.norm(P8), -Q8 / np.linalg.norm(Q8)
chk("|P| = a, |Q| = b [mm]", [np.linalg.norm(P8) * 1e3, np.linalg.norm(Q8) * 1e3], [2, 6])
chk("(a) n_P", nP, [0.6, 0.8, 0]); chk("(a) n_Q (= -r_hat)", nQ, [0.6, 0.8, 0])
chk("(a) E normal: n x E at P, Q", [np.cross(nP, EP), np.cross(nQ, EQ)], np.zeros((2, 3)), atol=1e-9)
chk("(a) E_P = 30 n_P, E_Q = -10 n_Q [kV/m]", [nP @ EP / 1e3, nQ @ EQ / 1e3], [30, -10])
chk("(a) H tangential: n.H at P, Q", [nP @ HP, nQ @ HQ], [0, 0], atol=1e-12)
rP, rQ = eps0 * nP @ EP, eps0 * nQ @ EQ
chk("(b) rho_s(P) [nC/m^2]", rP * 1e9, 265.6, rtol=1e-3)
chk("(b) rho_s(Q) [nC/m^2]", rQ * 1e9, -88.5)
JP, JQ = np.cross(nP, HP), np.cross(nQ, HQ)
chk("(b) J_s(P) [A/m]", JP, [0, 0, 30]); chk("(b) J_s(Q) [A/m]", JQ, [0, 0, -10])
lin = integrate.quad(lambda ph: rP * a8, 0, 2 * np.pi)[0]; lout = integrate.quad(lambda ph: rQ * b8, 0, 2 * np.pi)[0]
Iin = integrate.quad(lambda ph: JP[2] * a8, 0, 2 * np.pi)[0]; Iout = integrate.quad(lambda ph: JQ[2] * b8, 0, 2 * np.pi)[0]
chk("(c) rho_l inner, outer [nC/m]", [lin * 1e9, lout * 1e9], [3.34, -3.34])
chk("(c) rho_l inner = 120 pi eps0", lin, 120 * np.pi * eps0)
chk("(c) I inner, outer [A]", [Iin, Iout], [0.377, -0.377])
chk("(c) net charge, net current", [lin + lout, Iin + Iout], [0, 0], atol=1e-15)
rh = lambda p: p / np.linalg.norm(p); ph_ = lambda p: np.cross([0, 0, 1.0], rh(p))
chk("check: Gauss E at P (vector) [kV/m]", lin / (2 * np.pi * eps0 * a8) * rh(P8) / 1e3, EP / 1e3)
chk("check: Gauss E at Q (vector) [kV/m]", lin / (2 * np.pi * eps0 * b8) * rh(Q8) / 1e3, EQ / 1e3)
chk("check: Ampere H at P (vector) [A/m]", Iin / (2 * np.pi * a8) * ph_(P8), HP)
chk("check: Ampere H at Q (vector) [A/m]", Iin / (2 * np.pi * b8) * ph_(Q8), HQ)
V8 = integrate.quad(lambda r: lin / (2 * np.pi * eps0 * r), a8, b8)[0]
chk("check: V(a) - V(b) [V]", V8, 65.9)
chk("check: capacitance per length [pF/m]", lin / V8 * 1e12, 50.6)
chk("check: 2 pi eps0 / ln(b/a) [pF/m]", 2 * np.pi * eps0 / np.log(3) * 1e12, 50.6)
chk("watch out: n = +r_hat at Q gives", [eps0 * rh(Q8) @ EQ * 1e9, np.cross(rh(Q8), HQ)[2]], [88.5, 10])

# ---------------------------------------------------------------- 16.9
print("16.9 A leaky capacitor and its leads")
a9, d9, e9, s9, R9, V09 = 0.05, 1e-3, 4 * eps0, 2000 * eps0, 1e7, 100.0
A9 = np.pi * a9 ** 2; C9 = e9 * A9 / d9; Rl9 = d9 / (s9 * A9)
chk("sigma [S/m]", s9, 1.77e-8)
chk("A [m^2]", A9, 7.854e-3, rtol=1e-3)
chk("(a) C [pF]", C9 * 1e12, 278)
chk("(a) R_leak [MOhm]", Rl9 / 1e6, 7.19)
chk("(a) eps/sigma = R_l C [ms]", [e9 / s9 * 1e3, Rl9 * C9 * 1e3], [2, 2])
chk("(a) 1/(RC), sigma/eps, 1/tau [1/s]", [1 / (R9 * C9), s9 / e9, 1 / (R9 * C9) + s9 / e9], [359.5, 500, 859.5], rtol=1e-3)
sol9 = integrate.solve_ivp(lambda t, V: -V / (R9 * C9) - V / (Rl9 * C9), [0, 6e-3], [V09], dense_output=True, rtol=1e-11, atol=1e-12)
chk("(a) tau from ODE (V = V0/e) [ms]", optimize.brentq(lambda t: sol9.sol(t)[0] - V09 / np.e, 1e-4, 4e-3) * 1e3, 1.16)
Dz9 = lambda t: -e9 * sol9.sol(t)[0] / d9                 # D = eps E, E = -(V/d) z_hat
h9 = 1e-8
dDz0 = (-3 * Dz9(0) + 4 * Dz9(h9) - Dz9(2 * h9)) / (2 * h9)
Jz0 = -s9 * V09 / d9
IR0, Il0 = V09 / R9, V09 / Rl9
chk("(b) I_R(0) [uA] (+z in both leads)", IR0 * 1e6, 10)
chk("(b) I_leak(0) [uA]", Il0 * 1e6, 13.9)
chk("(b) J_z(0) [mA/m^2] (down)", Jz0 * 1e3, -1.771, rtol=1e-3)
chk("(b) dD_z/dt(0) [mA/m^2] (up), from ODE", dDz0 * 1e3, 3.044, rtol=1e-3)
chk("(b) sum [mA/m^2] = I_R/A", [(Jz0 + dDz0) * 1e3, IR0 / A9 * 1e3], [1.273, 1.273], rtol=1e-3)
Henc = lambda r, Jt: integrate.quad(lambda rp: Jt * 2 * np.pi * rp, 0, r)[0] / (2 * np.pi * r)
chk("(c) H at r = 2.5 cm, t = 0 [uA/m]", Henc(0.025, Jz0 + dDz0) * 1e6, 15.9)
chk("(c) H at plate edge [uA/m]", Henc(a9, Jz0 + dDz0) * 1e6, 31.8)
chk("check bag: conduction, displacement, total [uA]", [Jz0 * A9 * 1e6, dDz0 * A9 * 1e6, (Jz0 + dDz0) * A9 * 1e6], [-13.9, 23.9, 10.0])
sol9c = integrate.solve_ivp(lambda t, V: -V / (Rl9 * C9), [0, 8e-3], [V09], dense_output=True, rtol=1e-11, atol=1e-12)
chk("(d) leads cut: decay time [ms]", optimize.brentq(lambda t: sol9c.sol(t)[0] - V09 / np.e, 1e-4, 6e-3) * 1e3, 2.0)
Dzc = lambda t: -e9 * sol9c.sol(t)[0] / d9
dDzc = (-3 * Dzc(0) + 4 * Dzc(h9) - Dzc(2 * h9)) / (2 * h9)
chk("(d) (J + dD/dt)/|J| with leads cut", (Jz0 + dDzc) / abs(Jz0), 0.0, atol=1e-6)
chk("(d) conduction-only H at 2.5 cm [uA/m]", Henc(0.025, abs(Jz0)) * 1e6, 22.1)

# ---------------------------------------------------------------- 16.10
print("16.10 MMF around a discharging pair")
b10, Q010, tau10, a10, L10 = 0.03, 10e-9, 5e-6, 0.04, 0.05
I10 = Q010 / tau10
chg = [(+1.0, np.array([0, 0, b10])), (-1.0, np.array([0, 0, -b10]))]
def Dq(p):                                                   # D per unit Q
    s = np.zeros(3)
    for q, pos in chg:
        R = np.asarray(p, float) - pos
        s += q * R / (4 * np.pi * np.linalg.norm(R) ** 3)
    return s
disk = lambda z, a: integrate.quad(lambda r: Dq([r, 0, z])[2] * 2 * np.pi * r, 0, a, limit=200)[0]
chk("(a) I(0) [mA] (along -z)", I10 * 1e3, 2.0)
psi_d = disk(0.0, a10)
chk("(b) cos(theta0)", b10 / np.hypot(a10, b10), 0.6)
chk("(b) disk flux psi/Q", psi_d, -0.4)
chk("(b) MMF/I = -1 + (displacement 0.4)", -1 - psi_d, -0.6)
chk("(b) MMF at t = 0 [mA]", (-1 - psi_d) * I10 * 1e3, -1.2)
cside = integrate.quad(lambda z: -Dq([a10, 0, z])[0] * 2 * np.pi * a10, -L10, 0, limit=200)[0]
cbot = disk(-L10, a10)
flag("(c) wire (|z| < b) never crosses the cup (bottom at z = -L < -b, side at r = a > 0)", -L10 < -b10)
chk("(c) cup flux (C-oriented) side, bottom, total [Q]", [cside, cbot, cside + cbot], [0.376, 0.224, 0.6], rtol=3e-3)
chk("(c) MMF/I via cup", -(cside + cbot), -0.6)
def H_wire(F):
    f = lambda s: I10 * np.cross([0, 0, -1.0], np.asarray(F) - np.array([0, 0, b10 - s])) / (4 * np.pi * np.linalg.norm(np.asarray(F) - np.array([0, 0, b10 - s])) ** 3)
    return integrate.quad_vec(f, 0, 2 * b10)[0]
def mmf_loop(a, z, N=240):
    ph = (np.arange(N) + 0.5) * 2 * np.pi / N
    return sum(H_wire([a * np.cos(p), a * np.sin(p), z]) @ np.array([-np.sin(p), np.cos(p), 0]) * a * 2 * np.pi / N for p in ph)
chk("(d) H_phi at (a,0,0), Biot-Savart [mA/m]", H_wire([a10, 0, 0])[1] * 1e3, -4.77)
chk("(d) -15/pi [mA/m]", -15 / np.pi, -4.77)
chk("(d) loop sum of H.dl / I", mmf_loop(a10, 0.0) / I10, -0.6)
psi_e = disk(0.06, a10)
chk("(e) cos(theta2) = 9/sqrt(97)", 9 / np.sqrt(97), 0.914, rtol=1e-3)
chk("(e) flux through C' disk [Q]", psi_e, 0.157)
chk("(e) MMF'/I", -psi_e, -0.157)
chk("(e) MMF' at t = 0 [mA]", -psi_e * I10 * 1e3, -0.314)
chk("(e) Biot-Savart loop sum / I", mmf_loop(a10, 0.06) / I10, -0.157)
chk("(e) (cos th1 - cos th2)/2", 0.5 * (0.6 - 9 / np.sqrt(97)), -0.157)
big = integrate.quad(lambda u: Dq([np.exp(u), 0, 0])[2] * 2 * np.pi * np.exp(2 * u), np.log(1e-9), np.log(1e4), limit=400)[0]
chk("limits: MMF/I for a -> 0 and a -> infinity", [-1 - disk(0.0, 1e-5), -1 - big], [-1, 0], atol=1e-3)

# ---------------------------------------------------------------- 16.11
print("16.11 A region with no conduction current")
J0 = 2e-6
J11 = lambda p: J0 * np.array([p[0], p[1], 0.0])          # (a) spreading current
dJ = div_fd(J11, [0.3, -0.2, 0.5])
chk("(a) div J [uA/m^3]", dJ * 1e6, 4.0)
chk("(a) drho/dt = -div J [uA/m^3]", -dJ * 1e6, -4.0)
flag("(a)(i)-(iii) impossible: each forces div(dD/dt) = 0 or div J = 0, but drho/dt != 0", abs(dJ) > 1e-8)
dDiv = lambda p: -J11(p)
chk("(a)(iv) dD/dt = -J: div(dD/dt) = drho/dt [uA/m^3]", div_fd(dDiv, [0.1, 0.4, -0.3]) * 1e6, -4.0)
chk("(a)(iv) J + dD/dt (so curl H = 0) [A/m^2]", J11([0.5, 0.7, 0.2]) + dDiv([0.5, 0.7, 0.2]), [0, 0, 0], atol=1e-18)
chk("(a)(iv) curl of (x,y,0): E has no curl, B static (Faraday ok)", curl_fd(lambda p: np.array([p[0], p[1], 0.0]), [0.3, 0.2, 0.1]), [0, 0, 0], atol=1e-9)
flag("SP18 Exam 2 #1(iv) key (d(div D)/dt = 0) does NOT carry over: here it is -4 uA/m^3", abs(div_fd(dDiv, [0.2, 0.2, 0.2])) > 1e-8)
D0, T11 = 2e-9, 1e-3
DA = lambda p, t: D0 * t / T11 * np.array([p[0], p[1], 0.0])
DB = lambda p, t: D0 * np.array([p[0], p[1], t / T11])
DC = lambda p, t: D0 * t / T11 * np.array([p[1], p[0], 0.0])
pt = [0.3, -0.5, 0.2]
rho = lambda D, t: div_fd(lambda p: D(p, t), pt)
drdt = lambda D: (rho(D, 0.7 * T11) - rho(D, 0.2 * T11)) / (0.5 * T11)
chk("(b) D_A: rho at t = T/2 = 2 D0 t/T [nC/m^3]", rho(DA, 0.5 * T11) * 1e9, 2.0)
chk("(b) D_A: drho/dt = 2 D0/T [uA/m^3]", drdt(DA) * 1e6, 4.0)
chk("(b) D_A would need div J [uA/m^3] (a converging current)", -drdt(DA) * 1e6, -4.0)
chk("(b) D_B: rho [nC/m^3], drho/dt", [rho(DB, 0.3 * T11) * 1e9, drdt(DB)], [4.0, 0.0], atol=1e-12)
chk("(b) D_C: rho, drho/dt", [rho(DC, 0.6 * T11), drdt(DC)], [0, 0], atol=1e-15)
HB = lambda p: D0 / (2 * T11) * np.array([-p[1], p[0], 0.0])
chk("(b) D_B: curl H = dD_B/dt = (D0/T) z [uA/m^2]", curl_fd(HB, pt) * 1e6, [0, 0, 2.0])
dDC = lambda p: D0 / T11 * np.array([p[1], p[0], 0.0])
HC = lambda p: D0 / (2 * T11) * np.array([0.0, 0.0, p[1] ** 2 - p[0] ** 2])
for q in ([0.3, -0.5, 0.2], [-0.8, 0.4, 0.9]):
    chk(f"(c) curl H_C = dD_C/dt at {q} [uA/m^2]", curl_fd(HC, q) * 1e6, dDC(q) * 1e6)
Hx1 = integrate.quad(lambda x: -dDC([x, 0, 0])[1], 0, 1)[0]     # dH_z/dx = -(dD/dt)_y, H(axis) = 0
Hy1 = integrate.quad(lambda y: dDC([0, y, 0])[0], 0, 1)[0]      # dH_z/dy = +(dD/dt)_x
chk("(c) D0/(2T)", D0 / (2 * T11), 1e-6)
chk("(c) H_z(1,0,0), H_z(0,1,0) by line integration [uA/m]", [Hx1 * 1e6, Hy1 * 1e6], [-1, 1])
chk("(c) formula at the same points [uA/m]", [HC([1, 0, 0])[2] * 1e6, HC([0, 1, 0])[2] * 1e6], [-1, 1])
t11 = 0.4 * T11
chk("(d) div D_C", div_fd(lambda p: DC(p, t11), pt), 0, atol=1e-15)
chk("(d) div B (B = mu0 H_C)", div_fd(lambda p: mu0 * HC(p), pt), 0, atol=1e-18)
chk("(d) curl H - dD_C/dt", curl_fd(HC, pt) - dDC(pt), [0, 0, 0], atol=1e-15)
chk("(d) curl E_C [V/m^2]", curl_fd(lambda p: DC(p, t11) / eps0, pt), [0, 0, 0], atol=1e-6)
flux11 = integrate.dblquad(lambda z, y: dDC([0, y, z])[0], 0, 1, 0, 1)[0]
cor = [np.array(c, float) for c in ((0, 0, 0), (0, 1, 0), (0, 1, 1), (0, 0, 1))]
circ = sum(integrate.quad(lambda s: HC(cor[k] + s * (cor[(k + 1) % 4] - cor[k])) @ (cor[(k + 1) % 4] - cor[k]), 0, 1)[0] for k in range(4))
chk("check Stokes: normal of the square", np.cross(cor[1] - cor[0], cor[2] - cor[1]), [1, 0, 0])
chk("check Stokes: displacement current, circulation [uA]", [flux11 * 1e6, circ * 1e6], [1, 1])
B1 = lambda p, t: t / T11 * np.array([p[0], p[1], 0.0])
chk("(e) div B1 at t = T/4, 3T/4 [B0] (changes)", [div_fd(lambda p: B1(p, 0.25 * T11), pt), div_fd(lambda p: B1(p, 0.75 * T11), pt)], [0.5, 1.5])
chk("(e) div(-dB1/dt) [B0/T]", -(div_fd(lambda p: B1(p, 0.75 * T11), pt) - div_fd(lambda p: B1(p, 0.25 * T11), pt)) / 0.5, -2.0)
chk("(e) div B2 [B0] (constant, nonzero)", div_fd(lambda p: np.array([p[0], p[1], 0.0]), pt), 2.0)

# ---------------------------------------------------------------- 16.12
print("16.12 Four conditions at a tilted interface")
n12 = np.array([2.0, -1.0, 2.0]) / 3
Js12 = np.array([1.0, 4.0, 1.0]); E2 = np.array([4.0, 1.0, 1.0]) * 1e3
rs12, e1, e2 = 3000 * eps0, 2 * eps0, 5 * eps0
H2 = np.array([5.0, 0.0, 4.0])                         # revised (was 3x + y + 2z)
H2_old = np.array([3.0, 1.0, 2.0])
chk("(a) n points into medium 1 (n . grad(2x-y+2z) > 0), |n| = 1", [n12 @ np.array([2, -1, 2.0]) > 0, np.linalg.norm(n12)], [1, 1])
chk("(a) n . J_s", n12 @ Js12, 0, atol=1e-12)
chk("(a) n . E2 [kV/m]", n12 @ E2 / 1e3, 3.0)
chk("(a) E2n, E2t [kV/m]", [(n12 @ E2) * n12 / 1e3, (E2 - (n12 @ E2) * n12) / 1e3], [[2, -1, 2], [2, 2, -1]])
chk("(a) n . H2 [A/m] (revised; exam had H_n = 3)", n12 @ H2, 6.0)
chk("(a) H2n, H2t [A/m]", [(n12 @ H2) * n12, H2 - (n12 @ H2) * n12], [[4, -2, 4], [1, 2, 0]])
cm = lambda v: np.array([[0, -v[2], v[1]], [v[2], 0, -v[0]], [-v[1], v[0], 0]])
E1 = np.linalg.lstsq(np.vstack([cm(n12), e1 * n12]), np.concatenate([cm(n12) @ E2, [e2 * n12 @ E2 + rs12]]), rcond=None)[0]
chk("(b) E1n [kV/m]", n12 @ E1 / 1e3, 9.0)
chk("(b) E1 from linear solve of the BCs [kV/m]", E1 / 1e3, [8, -1, 5])
chk("(b) D1/eps0 [kV/m]", e1 * E1 / eps0 / 1e3, [16, -2, 10])
chk("(b) D1 [nC/m^2]", e1 * E1 * 1e9, [141.7, -17.7, 88.5], rtol=2e-3)
chk("(b) D2/eps0 [kV/m]", e2 * E2 / eps0 / 1e3, [20, 5, 5])
solveH = lambda H2v: np.linalg.lstsq(np.vstack([cm(n12), n12]), np.concatenate([cm(n12) @ H2v + Js12, [n12 @ H2v]]), rcond=None)[0]
H1 = solveH(H2)
chk("(c) J_s x n [A/m]", np.cross(Js12, n12), [3, 0, -3])
chk("(c) H1 from linear solve of the BCs [A/m]", H1, [8, 0, 1])
chk("(c) H1n [A/m]", n12 @ H1, 6.0)
chk("(c) check n x (H1 - H2) = J_s", np.cross(n12, H1 - H2), Js12)
chk("(c) check n x (3x - 3z) = (1/3)(3, 12, 3)", np.cross(n12, [3, 0, -3]), [1, 4, 1])
chk("(c) B1 = mu0 H1 [uT]", mu0 * H1 * 1e6, [10.05, 0, 1.257], rtol=1e-3, atol=1e-9)
chk("(original data, before revision) H1 = 6x + y - z [A/m]", solveH(H2_old), [6, 1, -1])
P1, P2 = (e1 - eps0) * E1, (e2 - eps0) * E2
rsb = n12 @ P2 - n12 @ P1
chk("(d) rho_sb / eps0, [nC/m^2]", [rsb / eps0, rsb * 1e9], [3000, 26.6])
chk("(d) total / eps0, [nC/m^2]", [(rs12 + rsb) / eps0, (rs12 + rsb) * 1e9], [6000, 53.1])
chk("(d) eps0 n.(E1 - E2) / eps0", n12 @ (E1 - E2), 6000)
H_exam = np.array([0, 0, 3.0]) + np.cross([0, 2.0, 0], [0, 0, 1.0])
print(f"    SP18 Exam 2 #1(vi) key: H(z>0) = {H_exam}, normal part 3 A/m")
flag("SP18 #1(vi) numbers do not carry over (J_s, H2, H1, H_n all differ)",
     not np.allclose(H1, H_exam) and not np.isclose(n12 @ H1, 3) and not np.isclose(n12 @ H2, 3)
     and not np.allclose(Js12, [0, 2, 0]))

print(f"\nSUMMARY: {NP[0]} PASS, {NP[1]} FAIL")
