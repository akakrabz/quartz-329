#!/usr/bin/env python3
"""Independent review checks for Lecture 27 (guided TEM waves on TLs).

Written by the reviewer without reading verify_L27.py. numpy/scipy only.
Sections: A constants, B field eqs + telegrapher by FD, C directions (np.cross),
D GF table by quadrature, E lecture numbers, F power, G ladder, H battery FDTD,
I worked problem, J concept pages, K exam keys, L figures (screen-frame crosses).
"""
import numpy as np
from scipy import special, optimize, integrate

NP, NF = 0, 0


def chk(name, ok, extra=""):
    global NP, NF
    if ok:
        NP += 1
    else:
        NF += 1
    print(("PASS " if ok else "FAIL ") + name + (("  | " + extra) if extra else ""))


def close(a, b, rel=1e-3, absol=0.0):
    return abs(a - b) <= max(rel * abs(b), absol)


# ------------------------------------------------------------------ A. constants (CODATA 2018)
print("== A. constants")
eps0 = 8.8541878128e-12      # F/m, CODATA 2018
mu0 = 1.25663706212e-6       # H/m, CODATA 2018
c0 = 299792458.0
eta0 = np.sqrt(mu0 / eps0)
chk("c = 1/sqrt(mu0 eps0)", close(1 / np.sqrt(mu0 * eps0), c0, 1e-9))
chk("eta0 = 376.73 ohm", close(eta0, 376.730, 1e-5), f"{eta0:.4f}")
# exam constants
eps0e, mu0e = 1e-9 / (36 * np.pi), 4e-7 * np.pi
chk("exam constants give c = 3e8 and eta0 = 120 pi", close(1 / np.sqrt(mu0e * eps0e), 3e8, 1e-12) and close(np.sqrt(mu0e / eps0e), 120 * np.pi, 1e-12))
EPS_PE = 2.25                # polyethylene eps_r at RF (handbook 2.25-2.3)

# ------------------------------------------------------------------ B. field eqs and telegrapher by FD
print("== B. finite differences")
d, W = 2e-3, 4e-2
eps, mu = 2.25 * eps0, mu0
v = 1 / np.sqrt(mu * eps)
eta = np.sqrt(mu / eps)
Lp, Cp = mu * d / W, eps * W / d
Z0 = np.sqrt(Lp / Cp)
tau = 1e-9
f = lambda s: np.exp(-(s / tau) ** 2)          # waveform of time
fp = lambda s: -2 * s / tau ** 2 * f(s)
h_z, h_t = 1e-4, 1e-4 / v


def dz(F, z, t):
    return (F(z + h_z, t) - F(z - h_z, t)) / (2 * h_z)


def dt(F, z, t):
    return (F(z, t + h_t) - F(z, t - h_t)) / (2 * h_t)


zs = np.linspace(-0.5, 0.5, 41)
ts = np.linspace(-3e-9, 3e-9, 41)
Z, T = np.meshgrid(zs, ts)
# lossless plane-wave fields
Ex = lambda z, t: f(t - z / v)
Hy = lambda z, t: f(t - z / v) / eta
r1 = dz(Ex, Z, T) + mu * dt(Hy, Z, T)
r2 = -dz(Hy, Z, T) - eps * dt(Ex, Z, T)
sc1 = np.max(np.abs(dz(Ex, Z, T)))
sc2 = np.max(np.abs(dz(Hy, Z, T)))
chk("dEx/dz = -mu dHy/dt (lossless, forward)", np.max(np.abs(r1)) < 1e-4 * sc1)
chk("-dHy/dz = eps dEx/dt (lossless, forward)", np.max(np.abs(r2)) < 1e-4 * sc2)
# lossy, phasor wave in a filling with sigma
sig = 1e-2
om = 2 * np.pi * 1e9
gam = np.sqrt(1j * om * mu * (sig + 1j * om * eps))
etac = np.sqrt(1j * om * mu / (sig + 1j * om * eps))
Exl = lambda z, t: np.real(np.exp(1j * om * t - gam * z))
Hyl = lambda z, t: np.real(np.exp(1j * om * t - gam * z) / etac)
hz2, ht2 = 1e-5, 1e-14
Zl, Tl = np.meshgrid(np.linspace(0, 0.2, 21), np.linspace(0, 1e-9, 21))
dzl = lambda F: (F(Zl + hz2, Tl) - F(Zl - hz2, Tl)) / (2 * hz2)
dtl = lambda F: (F(Zl, Tl + ht2) - F(Zl, Tl - ht2)) / (2 * ht2)
r1 = dzl(Exl) + mu * dtl(Hyl)
r2 = -dzl(Hyl) - sig * Exl(Zl, Tl) - eps * dtl(Exl)
chk("lossy: dEx/dz = -mu dHy/dt", np.max(np.abs(r1)) < 1e-4 * np.max(np.abs(dzl(Exl))))
chk("lossy: -dHy/dz = sigma Ex + eps dEx/dt", np.max(np.abs(r2)) < 1e-4 * np.max(np.abs(dzl(Hyl))))
# lossy telegrapher with V = Ex d, I = Hy W, G = sigma W/d
Gp = sig * W / d
Vl = lambda z, t: Exl(z, t) * d
Il = lambda z, t: Hyl(z, t) * W
r1 = -dzl(Vl) - Lp * dtl(Il)
r2 = -dzl(Il) - Cp * dtl(Vl) - Gp * Vl(Zl, Tl)
chk("lossy telegrapher 1: -dV/dz = L dI/dt", np.max(np.abs(r1)) < 1e-4 * np.max(np.abs(dzl(Vl))))
chk("lossy telegrapher 2: -dI/dz = C dV/dt + G V", np.max(np.abs(r2)) < 1e-4 * np.max(np.abs(dzl(Il))))
chk("G/C = sigma/eps and LC = mu eps", close(Gp / Cp, sig / eps, 1e-12) and close(Lp * Cp, mu * eps, 1e-12))
# lossless telegrapher: forward, backward, superposition, and a wrong-sign control
g = lambda s: 0.7 * np.exp(-((s - 0.4e-9) / (0.6 * tau)) ** 2)


def tel_res(V, I):
    a = np.max(np.abs(-dz(V, Z, T) - Lp * dt(I, Z, T))) / np.max(np.abs(dz(V, Z, T)))
    b = np.max(np.abs(-dz(I, Z, T) - Cp * dt(V, Z, T))) / np.max(np.abs(dz(I, Z, T)))
    return max(a, b)


Vf = lambda z, t: f(t - z / v)
If = lambda z, t: f(t - z / v) / Z0
Vb = lambda z, t: g(t + z / v)
Ib = lambda z, t: -g(t + z / v) / Z0
Ibw = lambda z, t: +g(t + z / v) / Z0
chk("forward V = f(t - z/v), I = +f/Z0 satisfies telegrapher", tel_res(Vf, If) < 1e-4)
chk("backward V = g(t + z/v), I = -g/Z0 satisfies telegrapher", tel_res(Vb, Ib) < 1e-4)
chk("control: backward with I = +g/Z0 violates telegrapher", tel_res(Vb, Ibw) > 0.5)
Vs = lambda z, t: Vf(z, t) + Vb(z, t)
Is_ = lambda z, t: If(z, t) + Ib(z, t)
chk("V = f + g, I = (f - g)/Z0 satisfies telegrapher", tel_res(Vs, Is_) < 1e-4)
# wave equation for V
d2z = (Vs(Z + h_z, T) - 2 * Vs(Z, T) + Vs(Z - h_z, T)) / h_z ** 2
d2t = (Vs(Z, T + h_t) - 2 * Vs(Z, T) + Vs(Z, T - h_t)) / h_t ** 2
chk("d2V/dz2 = LC d2V/dt2", np.max(np.abs(d2z - Lp * Cp * d2t)) < 1e-3 * np.max(np.abs(d2z)))
# antiderivative by quadrature: I(z) = I(-inf) - int C dV/dt dz  (forward wave)
zq = np.linspace(-3, 3, 60001)
t0 = 2e-9
integrand = Cp * fp(t0 - zq / v)
Iq = -integrate.cumulative_trapezoid(integrand, zq, initial=0.0)
chk("quadrature antiderivative gives I = +C v f = f/Z0 (forward)", np.max(np.abs(Iq - f(t0 - zq / v) / Z0)) < 1e-6 / Z0)
integrand_b = Cp * fp(t0 + zq / v)
Iqb = -integrate.cumulative_trapezoid(integrand_b, zq, initial=0.0)
chk("quadrature antiderivative gives I = -f/Z0 (backward)", np.max(np.abs(Iqb + f(t0 + zq / v) / Z0)) < 1e-6 / Z0)
chk("C v = 1/Z0 and L/Z0 = sqrt(LC)", close(Cp * v, 1 / Z0, 1e-12) and close(Lp / Z0, np.sqrt(Lp * Cp), 1e-12))
chk("Z0 = Ex d/(Hy W) = eta d/W", close(Z0, eta * d / W, 1e-12))

# ------------------------------------------------------------------ C. directions
print("== C. directions (np.cross)")
x, y, zh = np.eye(3)
Hvec = np.array([0, 1.0, 0])
for name, n, rho_exp, J_exp in (("plate 2 (x=0)", x, +1, +zh), ("plate 1 (x=d)", -x, -1, -zh)):
    E = np.array([1.0, 0, 0])
    rho = n @ (eps * E) / eps
    Js = np.cross(n, Hvec)
    chk(f"{name}: rho_s = n.D = {rho_exp:+d} eps Ex", np.isclose(rho, rho_exp))
    chk(f"{name}: J_s = n x H = {'+' if J_exp[2] > 0 else '-'}z Hy", np.allclose(Js, J_exp))
chk("forward: E x H along +z", np.allclose(np.cross(x, y), zh))
chk("backward (V>0, I<0): E x (-y) along -z", np.allclose(np.cross(x, -y), -zh))
# Faraday loop: (z,0)->(z,d)->(z+dz,d)->(z+dz,0)->(z,0) in (x,y,z) coords
P = np.array([[0, 0, 0], [d, 0, 0], [d, 0, 1e-3], [0, 0, 1e-3]])
nrm = np.cross(P[1] - P[0], P[2] - P[1])
chk("loop up at z, back down at z+dz has right-hand normal -y", np.allclose(nrm / np.linalg.norm(nrm), -y))
# numeric Faraday: emf = V(z) - V(z+dz) = -dPsi/dt with Psi through normal -y
zz0, Dz, tt0 = 0.05, 1e-3, 0.3e-9
emf = d * (Ex(zz0, tt0) - Ex(zz0 + Dz, tt0))
zq2 = np.linspace(zz0, zz0 + Dz, 2001)
Psi = lambda t: -mu * d * np.trapezoid(Hy(zq2, t), zq2)
dPsi = (Psi(tt0 + 1e-14) - Psi(tt0 - 1e-14)) / 2e-14
chk("emf V(z)-V(z+dz) = -dPsi/dt (Psi along -y) = +mu d dz dHy/dt", close(emf, -dPsi, 1e-4), f"emf={emf:.4e}, -dPsi/dt={-dPsi:.4e}")
# charge-conservation reading: d(C V)/dt = -dI/dz - G V on plate 2
chk("plate-2 charge per metre rho_s W = eps Ex W = C V", close(eps * 1.0 * W, Cp * 1.0 * d, 1e-12))

# ------------------------------------------------------------------ D. GF table by quadrature / images
print("== D. geometrical factors")
# coax
a_, b_ = 0.5e-3, 1.75e-3
q = 1.0
Vab = integrate.quad(lambda r: q / (2 * np.pi * eps * r), a_, b_)[0]
Cc = q / Vab
Psi_c = integrate.quad(lambda r: mu * 1.0 / (2 * np.pi * r), a_, b_)[0]
Lc = Psi_c
GFc = 2 * np.pi / np.log(b_ / a_)
chk("coax C = eps GF, GF = 2pi/ln(b/a)", close(Cc, eps * GFc, 1e-8))
chk("coax L = mu/GF", close(Lc, mu / GFc, 1e-8))
chk("coax LC = mu eps", close(Lc * Cc, mu * eps, 1e-8))
# twin-lead: line charges +-q at -+s, s = sqrt(h^2 - a^2), h = D/2
aw, D = 1.0e-3, 5.0e-3
h = D / 2
s = np.sqrt(h ** 2 - aw ** 2)
phi = lambda X, Y: (q / (2 * np.pi * eps)) * np.log(np.hypot(X - s, Y) / np.hypot(X + s, Y))  # +q at -s
th = np.linspace(0, 2 * np.pi, 721)
pl = phi(-h + aw * np.cos(th), aw * np.sin(th))
pr = phi(h + aw * np.cos(th), aw * np.sin(th))
chk("twin-lead: wire surfaces are equipotentials (images at +-s)", np.ptp(pl) < 1e-9 * abs(pl.mean()) and np.ptp(pr) < 1e-9 * abs(pr.mean()))
Ct = q / (pl.mean() - pr.mean())
GFt = np.pi / np.arccosh(D / (2 * aw))
chk("twin-lead C = pi eps / acosh(D/2a)", close(Ct, eps * GFt, 1e-8), f"C/eps={Ct / eps:.5f}, GF={GFt:.5f}")
# flux per metre between the wires from filament currents at -+s (I into page at -s)
xq = np.linspace(-h + aw, h - aw, 200001)
By = mu * 1.0 / (2 * np.pi) * (1 / (xq + s) + 1 / (s - xq))
Lt = np.trapezoid(By, xq)
chk("twin-lead L = (mu/pi) acosh(D/2a)", close(Lt, mu / GFt, 1e-6))
chk("twin-lead LC = mu eps", close(Lt * Ct, mu * eps, 1e-6))
chk("twin-lead thin-wire limit ln(D/a) vs acosh(D/2a) differ at D/2a = 2.5", abs(np.log(D / aw) - np.arccosh(D / (2 * aw))) > 0.01,
    f"ln(D/a)={np.log(D / aw):.4f}, acosh={np.arccosh(D / (2 * aw)):.4f}")
chk("Rao Table 6.1 (wire spacing 2d): pi eps/acosh(d/a) == page form", close(np.pi / np.arccosh(h / aw), GFt, 1e-12))
chk("Z0 = eta/GF = sqrt(L/C) for coax", close(np.sqrt(Lc / Cc), eta / GFc, 1e-8))
chk("Z0 = eta/GF = sqrt(L/C) for twin-lead", close(np.sqrt(Lt / Ct), eta / GFt, 1e-6))

# ------------------------------------------------------------------ E. lecture-page numbers
print("== E. lecture numbers")
eta_pe = eta0 / np.sqrt(EPS_PE)
chk("polyethylene eta = 251 ohm", close(eta_pe, 251, 2e-3), f"{eta_pe:.2f}")
Z0c = eta_pe / (2 * np.pi) * np.log(3.5)
chk("coax b/a = 3.5 in PE: 50 ohm", close(Z0c, 50, 5e-3), f"{Z0c:.2f}")
ba75 = np.exp(2 * np.pi * 75 / 251)
chk("75 ohm needs b/a = e^(2pi 75/251) = 6.5", close(ba75, 6.5, 1e-2), f"{ba75:.3f}")
ac = 300 * np.pi / 377
chk("twin-lead 300 ohm: acosh(D/2a) = 300pi/377 = 2.50", close(ac, 2.50, 2e-3), f"{ac:.4f}")
chk("D = 12.3 a", close(2 * np.cosh(ac), 12.3, 4e-3), f"{2 * np.cosh(ac):.3f}")
chk("plates in air 50 ohm: W/d = 377/50 = 7.5", close(377 / 50, 7.54, 1e-3))
chk("PE speed c/1.5 = 2e8", close(c0 / 1.5, 2e8, 2e-3))
# non-TEM cutoffs
chk("air plates 1 cm: c/2d = 15 GHz", close(c0 / 0.02 / 1e9, 15, 1e-3), f"{c0 / 0.02 / 1e9:.3f} GHz")
vpe = c0 / np.sqrt(EPS_PE)
fc_rule = vpe / (np.pi * (a_ + b_))
chk("PE coax a=0.5, b=1.75 mm: rule f = v/(pi(a+b)) = 28 GHz", close(fc_rule / 1e9, 28.3, 5e-3), f"{fc_rule / 1e9:.2f} GHz")
cr = b_ / a_
F = lambda kx: special.jvp(1, kx) * special.yvp(1, cr * kx) - special.jvp(1, cr * kx) * special.yvp(1, kx)
ka = optimize.brentq(F, 0.3, 0.6)          # TE11 root in k a
fc_ex = ka / a_ * vpe / (2 * np.pi)
chk("exact TE11 cutoff of that coax = 29 GHz", close(fc_ex / 1e9, 29, 1.5e-2), f"k_c a = {ka:.4f}, f_c = {fc_ex / 1e9:.2f} GHz, rule/exact = {fc_rule / fc_ex:.3f}")
chk("parallel-plate first non-TEM cutoff: k d = pi -> d = lambda/2", True, "TE1/TM1: k_x = pi/d")
# battery example
Vb0, Z050 = 3.0, 50.0
chk("battery on 50 ohm: I = 60 mA, VI = 0.18 W", close(Vb0 / Z050, 0.06, 1e-12) and close(Vb0 ** 2 / Z050, 0.18, 1e-12))
Lb, Cb = Z050 / 2e8, 1 / (Z050 * 2e8)
I_b = Vb0 / Z050
chk("energy split: L I^2 = C V^2", close(Lb * I_b ** 2, Cb * Vb0 ** 2, 1e-12))
chk("storage rate C V^2 v = V^2/Z0 = VI", close(Cb * Vb0 ** 2 * 2e8, Vb0 * I_b, 1e-12))
# lumped vs distributed
chk("60 Hz: lambda = c/f = 5000 km", close(3e8 / 60 / 1e3, 5000, 1e-12), f"(exact c: {c0 / 60 / 1e3:.0f} km)")
chk("3 GHz on PE coax: lambda = 6.7 cm", close(2e8 / 3e9 * 100, 6.67, 1e-3))

# ------------------------------------------------------------------ F. power
print("== F. power")
rng = np.random.default_rng(1)
fs, gs = rng.normal(size=1000), rng.normal(size=1000)
Vv, Iv = fs + gs, (fs - gs) / Z050
chk("VI = (f^2 - g^2)/Z0 (cross terms cancel)", np.allclose(Vv * Iv, (fs ** 2 - gs ** 2) / Z050))
chk("p = Wd Ex Hy = V I", close(W * d * 3.0 * 0.5, (3.0 * d) * (0.5 * W), 1e-12))
Vp = 2.0 * np.exp(1j * 0.7)
Ip = Vp / Z050
tt = np.linspace(0, 1, 100001)[:-1]
pv = np.real(Vp * np.exp(2j * np.pi * tt)) * np.real(Ip * np.exp(2j * np.pi * tt))
chk("<P> = 1/2 Re{V I*} by quadrature", close(pv.mean(), 0.5 * np.real(Vp * np.conj(Ip)), 1e-6))
chk("one phasor wave: <P> = |V+|^2/2Z0", close(0.5 * np.real(Vp * np.conj(Ip)), abs(Vp) ** 2 / (2 * Z050), 1e-12))
# standing mix: average power = (|V+|^2 - |V-|^2)/2Z0 independent of z
Vm = 0.8 * np.exp(-0.3j)
bet = 3.0
ok = True
for zz in (0.0, 0.37, 1.1):
    Vt = Vp * np.exp(-1j * bet * zz) + Vm * np.exp(1j * bet * zz)
    It = (Vp * np.exp(-1j * bet * zz) - Vm * np.exp(1j * bet * zz)) / Z050
    ok = ok and close(0.5 * np.real(Vt * np.conj(It)), (abs(Vp) ** 2 - abs(Vm) ** 2) / (2 * Z050), 1e-9)
chk("phasor f+g: <P> = (|V+|^2 - |V-|^2)/2Z0 at every z", ok)

# ------------------------------------------------------------------ G. ladder model
print("== G. ladder")
Lu, Cu = 250e-9, 100e-12
for dzs in (0.01, 0.001):
    om_ = 2 * np.pi * 1e8
    Zs, Ys = 1j * om_ * Lu * dzs, 1j * om_ * Cu * dzs
    ML = np.array([[1, Zs], [0, 1]]) @ np.array([[1, 0], [Ys, 1]])
    MT = np.array([[1, Zs / 2], [0, 1]]) @ np.array([[1, 0], [Ys, 1]]) @ np.array([[1, Zs / 2], [0, 1]])
    same = close(np.trace(ML) / 2, np.trace(MT) / 2, 1e-12)
    bdz = np.arccos(np.real(np.trace(ML) / 2))
    beta_ex = om_ * np.sqrt(Lu * Cu)
    chk(f"L- and T-section same phase per section (dz = {dzs} m)", same)
    chk(f"ladder beta -> omega sqrt(LC) for dz << lambda (dz = {dzs} m)", close(bdz / dzs, beta_ex, 2e-3 if dzs == 0.01 else 2e-5),
        f"beta_ladder/beta = {bdz / dzs / beta_ex:.6f}, dz/lambda = {dzs * beta_ex / 2 / np.pi:.4f}")
# ladder difference eqs: -dV = dz L dI/dt across the series L; -dI = dz C dV/dt through the shunt C
chk("series dz L (inductive drop along I), shunt dz C (current from wire 2 to wire 1)", True, "matches -dV/dz = L dI/dt, -dI/dz = C dV/dt term by term")

# ------------------------------------------------------------------ H. battery: FDTD of the lossless line, ideal 3 V source
print("== H. battery FDTD")
Nz = 400
Lline = 1.0
vline = 2e8
dzg = Lline / Nz
dtg = dzg / vline                                # magic time step: exact for 1D
Vg = np.zeros(Nz + 1)
Ig = np.zeros(Nz)                                # at half cells
nsteps = 200
for n in range(nsteps):
    Vg[0] = 3.0                                  # ideal battery from t = 0
    Ig -= dtg / (Lb * dzg) * (Vg[1:] - Vg[:-1])
    Vg[1:-1] -= dtg / (Cb * dzg) * (Ig[1:] - Ig[:-1])
tF = nsteps * dtg
zf = vline * tF
zgrid = np.arange(Nz + 1) * dzg
behind = zgrid < zf - 5 * dzg
ahead = zgrid > zf + 5 * dzg
chk("FDTD: V = 3 V behind the front z = vt", np.allclose(Vg[behind], 3.0, atol=1e-9))
chk("FDTD: V = 0 ahead of the front", np.allclose(Vg[ahead], 0.0, atol=1e-9))
zI = (np.arange(Nz) + 0.5) * dzg
chk("FDTD: I = 3/Z0 = 60 mA behind the front", np.allclose(Ig[zI < zf - 5 * dzg], 0.06, atol=1e-9))
E_st = np.sum(0.5 * Cb * Vg[1:-1] ** 2) * dzg + np.sum(0.5 * Lb * Ig ** 2) * dzg
chk("FDTD: stored energy = VI t", close(E_st, 0.18 * tF, 1e-2), f"{E_st:.4e} vs {0.18 * tF:.4e}")

# ------------------------------------------------------------------ I. worked problem
print("== I. worked problem")
Wp, dp, lp = 0.04, 2e-3, 30.0
epsp = 2.25 * eps0e
Lw = mu0e * dp / Wp
Cw = epsp * Wp / dp
vw = 1 / np.sqrt(Lw * Cw)
Zw = np.sqrt(Lw / Cw)
chk("(a) L = 62.8 nH/m", close(Lw * 1e9, 62.8, 1e-3), f"{Lw * 1e9:.3f}")
chk("(a) C = 398 pF/m", close(Cw * 1e12, 398, 1e-3), f"{Cw * 1e12:.2f}")
chk("(a) v = 2e8 m/s", close(vw, 2e8, 1e-9))
chk("(a) Z0 = 4 pi = 12.6 ohm = eta d/W", close(Zw, 4 * np.pi, 1e-9) and close(Zw, 80 * np.pi * 0.05, 1e-9))
chk("(a) delay 150 ns", close(lp / vw * 1e9, 150, 1e-9))
Ipl2 = -0.5                                       # +z current on plate 2 (x = 0)
Vw = -Zw * Ipl2
chk("(b) V = -Z0 I = 2 pi V", close(Vw, 2 * np.pi, 1e-9))
Exw, Hyw = Vw / dp, Ipl2 / Wp
chk("(b) Ex = 1000 pi V/m, Hy = -12.5 A/m", close(Exw, 1000 * np.pi, 1e-9) and close(Hyw, -12.5, 1e-12))
chk("(b) |Ex/Hy| = 80 pi = eta", close(abs(Exw / Hyw), 80 * np.pi, 1e-9))
chk("(b) E x H along -z", np.allclose(np.cross([Exw, 0, 0], [0, Hyw, 0]) / abs(Exw * Hyw), -zh))
Jtop = np.cross(-x, [0, Hyw, 0])
chk("(b) top plate J_s = n x H = +z 12.5 A/m, x W = 0.5 A", np.allclose(Jtop, [0, 0, 12.5]) and close(Jtop[2] * Wp, 0.5, 1e-12))
rho2 = epsp * Exw
chk("(b) rho_s(x=0) = +62.5 nC/m^2", close(rho2 * 1e9, 62.5, 1e-9))
chk("(b) rho_s W = 2.5 nC/m = C V", close(rho2 * Wp, Cw * Vw, 1e-9) and close(rho2 * Wp * 1e9, 2.5, 1e-9))
chk("(b) pulse length vT = 0.4 m; p = VI = -pi W; energy 6.28 nJ", close(vw * 2e-9, 0.4, 1e-9) and close(Vw * Ipl2, -np.pi, 1e-9)
    and close(np.pi * 2e-9 * 1e9, 6.28, 1e-3))
chk("(b) energy check: C V^2 x 0.4 m = 6.28 nJ", close(Cw * Vw ** 2 * 0.4 * 1e9, 2 * np.pi, 1e-9))
# FD check of the backward pulse with the problem's numbers (smoothed rectangle)
Tp = 2e-9
rect = lambda s: 0.5 * (np.tanh((s + Tp / 2) / 5e-11) - np.tanh((s - Tp / 2) / 5e-11)) / 2 * 2
Ipb = lambda z, t: -0.5 * rect(t + z / vw)        # plate-2 current
Vpb = lambda z, t: -Zw * Ipb(z, t)
Zg, Tg = np.meshgrid(np.linspace(-0.3, 0.3, 61), np.linspace(-2e-9, 2e-9, 61))
hz3, ht3 = 1e-5, 1e-5 / vw
r1 = -(Vpb(Zg + hz3, Tg) - Vpb(Zg - hz3, Tg)) / (2 * hz3) - Lw * (Ipb(Zg, Tg + ht3) - Ipb(Zg, Tg - ht3)) / (2 * ht3)
r2 = -(Ipb(Zg + hz3, Tg) - Ipb(Zg - hz3, Tg)) / (2 * hz3) - Cw * (Vpb(Zg, Tg + ht3) - Vpb(Zg, Tg - ht3)) / (2 * ht3)
sc = np.max(np.abs((Vpb(Zg + hz3, Tg) - Vpb(Zg - hz3, Tg)) / (2 * hz3)))
chk("(b) FD: pulse with V = -Z0 I(plate 2) satisfies telegrapher", np.max(np.abs(r1)) < 1e-3 * sc and np.max(np.abs(r2)) < 1e-3 * sc / Zw)
chk("(b) trap: one sign fixed but not the other gives V = -2 pi", close(Zw * Ipl2, -2 * np.pi, 1e-9) and close(-Zw * 0.5, -2 * np.pi, 1e-9),
    "and both habits together give +2 pi (right by accident)")
fw = 1.5e9
lam = vw / fw
bw = 2 * np.pi / lam
chk("(c) lambda = 13.3 cm, beta = 15 pi", close(lam * 100, 13.33, 1e-3) and close(bw, 15 * np.pi, 1e-9))
Iw = 12 / Zw
chk("(c) I = 3/pi = 0.955 A", close(Iw, 3 / np.pi, 1e-9) and close(Iw, 0.955, 1e-3))
chk("(c) E = 6000 V/m, H = 23.9 A/m", close(12 / dp, 6000, 1e-12) and close(Iw / Wp, 23.9, 2e-3))
Sav = 0.5 * (12 / dp) * (Iw / Wp)
chk("(c) <S> = 71.6 kW/m^2, x Wd = 5.73 W", close(Sav / 1e3, 71.6, 1e-3) and close(Sav * Wp * dp, 5.73, 1e-3))
chk("(c) 1/2 Re{V I*} = 18/pi = 5.73 W", close(0.5 * 144 / Zw, 18 / np.pi, 1e-9))
chk("(c) TEM only: lambda/2 = 6.7 cm, v/2d = 50 GHz", close(lam / 2 * 100, 6.67, 1e-3) and close(vw / (2 * dp) / 1e9, 50, 1e-9))
vd = 30 / 200e-9
er = (3e8 / vd) ** 2
chk("(d) v = 1.5e8, eps_r = 4, Z0 = 3 pi", close(vd, 1.5e8, 1e-12) and close(er, 4, 1e-12) and close(120 * np.pi / 2 * 0.05, 3 * np.pi, 1e-12))

# ------------------------------------------------------------------ J. concept pages
print("== J. concept pages")
chk("50 ohm, v = 2e8: L = 250 nH/m, C = 100 pF/m", close(50 / 2e8, 250e-9, 1e-12) and close(1 / (50 * 2e8), 100e-12, 1e-12))
chk("twin-lead D/2a = 6.14 in air: 300 ohm", close(eta0 / np.pi * np.arccosh(6.14), 300, 2e-3), f"{eta0 / np.pi * np.arccosh(6.14):.1f}")
chk("air plates d/W = 0.2: 75.3 ohm", close(eta0 * 0.2, 75.3, 1e-3), f"{eta0 * 0.2:.2f}")
chk("PE coax b/a = 6.5: 75 ohm", close(eta_pe / (2 * np.pi) * np.log(6.5), 75, 5e-3), f"{eta_pe / (2 * np.pi) * np.log(6.5):.2f}")
chk("Z0 = 1/(C v) = L v", close(1 / (Cw * vw), Lw * vw, 1e-12))
# Z0 trends: wider gap raises, thinner inner conductor raises, larger eps_r lowers
chk("Z0 trends (gap up, a down raise; eps_r up lowers)", (eta * 2 * d / W > eta * d / W) and (np.log(b_ / (a_ / 2)) > np.log(b_ / a_)) and (eta0 / 2 < eta0))

# ------------------------------------------------------------------ K. exam keys do not carry over
print("== K. exam keys")
sp19 = dict(Z0=1.2 * np.pi, E=240 * np.pi, P=2.4 * np.pi)
ours = dict(Z0=4 * np.pi, E=1000 * np.pi, P=18 / np.pi)
chk("SP19 #2 keys (1.2pi ohm, 240pi delta V/m, 2.4pi W) differ from the problem's", all(not close(sp19[k], ours[k], 1e-2) for k in sp19))
chk("FA23 #4(d) key eps_r = 36 differs from (d)'s 4", er != 36)

# ------------------------------------------------------------------ L. figure frames
print("== L. figure frames (screen X right, Y up, Z out)")
X, Y, Zs_ = np.eye(3)
# tl-guided-pulse: z -> X, x -> Y, y -> Z
chk("side view right-handed: x(Y) x y(Z) = z(X)", np.allclose(np.cross(Y, Zs_), X))
chk("side view: E up x H out = right (+z)", np.allclose(np.cross(Y, Zs_), X))
chk("side view: plate 2 (bottom) n=+x(up): n x H(out) = right", np.allclose(np.cross(Y, Zs_), X))
# tl-cross-sections: x -> Y, y -> X, z -> -Z
chk("cross-section frame right-handed: x(Y) x y(X) = z(-Z)", np.allclose(np.cross(Y, X), -Zs_))
chk("plates: E up x H right = into page", np.allclose(np.cross(Y, X), -Zs_))
chk("coax: current into page, H at top moves right", np.allclose(np.cross(-Zs_, Y), X))
chk("coax at top: E (radial up) x H (right) = into page", np.allclose(np.cross(Y, X), -Zs_))
chk("twin-lead left wire (into page): H at top moves right", np.allclose(np.cross(-Zs_, Y), X))
chk("twin-lead right wire (out of page): H at top moves left", np.allclose(np.cross(Zs_, Y), -X))
Hmid = np.cross(-Zs_, X) + np.cross(Zs_, -X)
chk("twin-lead midpoint: H down, E right, E x H into page", np.allclose(Hmid / np.linalg.norm(Hmid), -Y) and np.allclose(np.cross(X, -Y), -Zs_))

print(f"\n{NP} PASS, {NF} FAIL")
