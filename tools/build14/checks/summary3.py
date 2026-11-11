#!/usr/bin/env python3
"""Numbers and identities on content/0-toolkit/09-midterm-3-summary.md that twins.py does not already print."""
import numpy as np
pi = np.pi; c = 3e8; mu0 = 4e-7 * pi; eps0 = 1e-9 / (36 * pi); eta0 = 120 * pi
X, Y, Z = np.eye(3); n = dict(p=0, f=0)
def chk(label, mine, want, tol=1e-6):
    ok = np.allclose(np.asarray(mine, complex), np.asarray(want, complex), rtol=tol, atol=1e-9)
    n["p" if ok else "f"] += 1; print(("PASS " if ok else "FAIL ") + f"{label}: {np.round(np.asarray(mine, complex if np.iscomplexobj(np.asarray(mine)) else float), 5)}")
def med(w, mu, eps, sig):
    g = np.sqrt(1j * w * mu * (sig + 1j * w * eps)); return g, 1j * w * mu / g
print("== S1 no-calculator triangles")
chk("3-4-5 angles [deg] round to 37 and 53", np.round(np.degrees([np.arctan2(3, 4), np.arctan2(4, 3)])), [37, 53])
print("== S3 decode identities, random media")
rng = np.random.default_rng(3)
for k in range(3):
    w = 10 ** rng.uniform(5, 10); mu = mu0 * rng.uniform(1, 4); eps = eps0 * rng.uniform(1, 80); sig = 10 ** rng.uniform(-4, 1)
    g, eta = med(w, mu, eps, sig); tau = np.angle(eta)
    chk(f" medium {k}: gamma*eta/(j w mu), (gamma/eta)/(sigma + j w eps), tan(2 tau)/(sigma/(w eps)), angle(gamma)+tau [deg]",
        [g * eta / (1j * w * mu), (g / eta) / (sig + 1j * w * eps), np.tan(2 * tau) / (sig / (w * eps)), np.degrees(np.angle(g) + tau)], [1, 1, 1, 90])
    chk(f" medium {k}: 0 <= tau <= 45 deg and alpha <= beta", [0 <= np.degrees(tau) <= 45, g.real <= g.imag], [1, 1])
    # <S> = |E0|^2/(2|eta|) e^{-2 alpha z} cos(tau) against (1/2) Re{E x H*}
    z = 0.37 / g.real; E = 3.0 * np.exp(-g * z); H = E / eta
    chk(f" medium {k}: (1/2)Re(E H*) vs formula", 0.5 * np.real(E * np.conj(H)), 9 / (2 * abs(eta)) * np.exp(-2 * g.real * z) * np.cos(tau))
chk("tau = 30 deg gives sigma/(w eps) = sqrt 3", np.tan(np.radians(60)), np.sqrt(3))
print("== S4 regime table against the exact gamma, eta")
w = 2 * pi * 1e8; mu = mu0; eps = 4 * eps0
sig = 0.01 * w * eps; g, eta = med(w, mu, eps, sig)
chk("imperfect dielectric (loss tangent 0.01): beta, alpha, |eta|, tau [rad] (approx/exact)",
    [w * np.sqrt(mu * eps) / g.imag, sig / 2 * np.sqrt(mu / eps) / g.real, np.sqrt(mu / eps) / abs(eta), sig / (2 * w * eps) / np.angle(eta)], [1, 1, 1, 1], tol=1e-3)
chk(" delta = (2/sigma) sqrt(eps/mu) vs 1/alpha", 2 / sig * np.sqrt(eps / mu) * g.real, 1, tol=1e-3)
sig = 1e4 * w * eps; g, eta = med(w, mu, eps, sig); f = w / (2 * pi); a = np.sqrt(pi * f * mu * sig)
chk("good conductor (loss tangent 1e4): alpha, beta, |eta|, tau [deg], lambda/(2 pi delta) (approx/exact)",
    [a / g.real, a / g.imag, np.sqrt(w * mu / sig) / abs(eta), np.degrees(np.angle(eta)) / 45, (2 * pi / g.imag) / (2 * pi / g.real)], [1, 1, 1, 1, 1], tol=1e-3)
chk("after one delta: field, power", [np.exp(-1), np.exp(-2)], [0.37, 0.135], tol=1e-2)
chk("dB per metre per Np/m: field 20 log10 e, power 10 log10 e^2", [20 * np.log10(np.e), 10 * np.log10(np.e ** 2)], [8.686, 8.686], tol=1e-4)
chk("sigma/(w eps) = 18e9 sigma/(f eps_r) with eps0 = 1e-9/36 pi (sample)", 4 / (2 * pi * 1e3 * 81 * eps0), 18e9 * 4 / (1e3 * 81))
chk("seawater: crossover [MHz]; delta at 1 kHz [m] = 25/pi; lambda [m]; loss tangent at 1 GHz",
    [18e9 * 4 / 81 / 1e6, 1 / np.sqrt(pi * 1e3 * mu0 * 4), 2 * pi / np.sqrt(pi * 1e3 * mu0 * 4), 18e9 * 4 / (1e9 * 81)], [888.889, 25 / pi, 50, 0.888889])
chk("copper at 60 Hz, sigma = 5.8e7: delta [mm]", 1e3 / np.sqrt(pi * 60 * mu0 * 5.8e7), 8.5, tol=5e-3)
print("== S5 polarization")
def hand(Ex, Ey):   # travel +z; sense of rotation of Re{(Ex, Ey) e^{jwt}}
    t = np.array([0, 0.01]); e = np.array([np.real(Ex * np.exp(1j * t)), np.real(Ey * np.exp(1j * t))])
    cz = e[0, 0] * e[1, 1] - e[1, 0] * e[0, 1]; return "RH" if cz > 0 else "LH"
chk("toward +z: x - jy right, x + jy left (1 = as stated)", [hand(1, -1j) == "RH", hand(1, 1j) == "LH"], [1, 1])
chk("sin(wt + th) has phasor -j e^{j th}: Re{-j e^{j0.4} e^{j1.3}} vs sin(1.7)", np.real(-1j * np.exp(0.4j) * np.exp(1.3j)), np.sin(1.7))
E0 = 2.0; chk("circular (E0 each) vs linear (peak E0): <S> eta", [(E0 ** 2 + E0 ** 2) / 2, E0 ** 2 / 2], [E0 ** 2, E0 ** 2 / 2])
chk("x = (x - jy)/2 + (x + jy)/2", 0.5 * np.array([1, -1j]) + 0.5 * np.array([1, 1j]), [1, 0])
wp = 3.0; w = 5.0; b = np.sqrt(w ** 2 - wp ** 2) / c; vp = w / b; vg = c ** 2 * b / w
chk("plasma: v_p v_g / c^2, and v_g = dw/db numerically", [vp * vg / c ** 2, (np.sqrt(wp ** 2 + (b * 1.000001 * c) ** 2) - w) / (b * 1e-6) / vg], [1, 1], tol=1e-4)
print("== S6 reflection, standing wave, pressure")
e1, e2 = eta0, eta0 / 2; G = (e2 - e1) / (e2 + e1); T = 1 + G
chk("air -> eps_r = 4: Gamma, tau, 2 eta2/(eta1+eta2), |G|^2, tau^2 eta1/eta2, sum", [G, T, 2 * e2 / (e1 + e2), G ** 2, T ** 2 * e1 / e2, G ** 2 + T ** 2 * e1 / e2], [-1 / 3, 2 / 3, 2 / 3, 1 / 9, 8 / 9, 1])
chk(" boundary: tangential E and H continuous (E_i + E_r - E_t, H_i + H_r - H_t)", [1 + G - T, 1 / e1 - G / e1 - T / e2], [0, 0])
# mirror: E = 2 E0 sin(bz) sin(wt) x, H = (2E0/eta) cos(bz) cos(wt) y satisfy Faraday and Ampere in free space
w = 2 * pi * 1e8; b = w / c; E0 = 1.0
Ex = lambda z, t: 2 * E0 * np.sin(b * z) * np.sin(w * t); Hy = lambda z, t: 2 * E0 / eta0 * np.cos(b * z) * np.cos(w * t)
z0, t0, hz, ht = -0.83, 2.1e-9, 1e-6, 1e-15
far = (Ex(z0 + hz, t0) - Ex(z0 - hz, t0)) / (2 * hz) + mu0 * (Hy(z0, t0 + ht) - Hy(z0, t0 - ht)) / (2 * ht)
amp = -(Hy(z0 + hz, t0) - Hy(z0 - hz, t0)) / (2 * hz) - eps0 * (Ex(z0, t0 + ht) - Ex(z0, t0 - ht)) / (2 * ht)
chk("mirror standing wave: Faraday and Ampere residuals (relative), E at the mirror", [far / (b * E0), amp / (b * E0 / eta0), Ex(0, t0)], [0, 0, 0], tol=1e-5)
chk(" phasor sum: e^{-jbz} - e^{+jbz} = -2j sin(bz); e^{-jbz} + e^{+jbz} = 2 cos(bz)", [np.exp(-0.7j) - np.exp(0.7j), np.exp(-0.7j) + np.exp(0.7j)], [-2j * np.sin(0.7), 2 * np.cos(0.7)])
Gm = 0.4 * np.exp(1.1j); zz = np.linspace(-3, 0, 200001); mag = abs(np.exp(-2j * pi * zz) + Gm * np.exp(2j * pi * zz))
chk("partial reflection |Gamma| = 0.4: max, min of |E|/E0", [mag.max(), mag.min()], [1.4, 0.6], tol=1e-6)
chk("radiation pressure, 1 kW/m^2: absorber, mirror [uPa]", [1e3 / c * 1e6, 2e3 / c * 1e6], [3.3, 6.7], tol=2e-2)
print("== S7 lines")
W, d = 0.05, 0.002; eps = 2.25 * eps0; L = mu0 * d / W; C = eps * W / d; eta = np.sqrt(mu0 / eps)
chk("plates: sqrt(L/C) vs eta d/W; 1/sqrt(LC) vs 1/sqrt(mu eps)", [np.sqrt(L / C) / (eta * d / W), 1 / np.sqrt(L * C) * np.sqrt(mu0 * eps)], [1, 1])
V = 3.0; Z0 = eta * d / W; chk(" power: <S> W d vs |V|^2/(2 Z0), with E = V/d", [(V / d) ** 2 / (2 * eta) * W * d, V ** 2 / (2 * Z0)], [V ** 2 / (2 * Z0)] * 2)
a_, b_ = 1e-3, 3.5e-3; chk("coax: sqrt(L/C) vs (eta/2 pi) ln(b/a)", np.sqrt((mu0 / (2 * pi) * np.log(b_ / a_)) / (2 * pi * eps / np.log(b_ / a_))), eta / (2 * pi) * np.log(b_ / a_))
print("== S8 bounce example and junction")
Z0, Rg, RL, V0 = 50, 25, 100, 9
tg = Z0 / (Rg + Z0); GL = (RL - Z0) / (RL + Z0); Gg = (Rg - Z0) / (Rg + Z0); V1 = tg * V0
chk("tau_g, Gamma_L, Gamma_g, launched, load at T, source end at 2T, steady V, steady I [A]",
    [tg, GL, Gg, V1, V1 * (1 + GL), V1 + V1 * GL + V1 * GL * Gg, V0 * RL / (Rg + RL), V0 / (Rg + RL)], [2 / 3, 1 / 3, -1 / 3, 6, 8, 22 / 3, 7.2, 0.072])
series = V1 * (1 + GL) / (1 - GL * Gg)
chk(" bounce series sums to the DC divider", series, 7.2)
Zj, Zk, R = 50.0, 75.0, 30.0
G = (Zk - Zj) / (Zk + Zj); chk("junction: tau = 1 + Gamma = 2Zk/(Zk+Zj); back: -Gamma, 1 - Gamma; current refl, trans", [1 + G, (Zj - Zk) / (Zj + Zk), 2 * Zj / (Zj + Zk), -G, (1 + G) * Zj / Zk], [2 * Zk / (Zk + Zj), -G, 1 - G, -G, 1 - G])
Ze = R * Zk / (R + Zk); Gs = (Ze - Zj) / (Ze + Zj)
chk(" shunt R: junction voltage (1+Gamma) V+ is the voltage on line k (KCL residual)", (1 - Gs) / Zj - (1 + Gs) / R - (1 + Gs) / Zk, 0)
Gr = (R + Zk - Zj) / (R + Zk + Zj); tr = (1 + Gr) * Zk / (R + Zk)
chk(" series R: tau = (1+Gamma) Zk/(R+Zk) = 2Zk/(R+Zj+Zk); KVL/KCL residual", [tr, (1 - Gr) / Zj - tr / Zk], [2 * Zk / (R + Zj + Zk), 0])
print("== S9 steady state")
Z0 = 50.0; bl = 0.9
zin = lambda ZL, bl: Z0 * (ZL + 1j * Z0 * np.tan(bl)) / (Z0 + 1j * ZL * np.tan(bl))
chk("short: j Z0 tan; open (ZL -> 1e12): -j Z0 cot", [zin(0, bl), zin(1e12, bl)], [1j * Z0 * np.tan(bl), -1j * Z0 / np.tan(bl)], tol=1e-6)
ZL = 20 + 35j; GLc = (ZL - Z0) / (ZL + Z0); Vp = 1.3 - 0.4j; Vm = GLc * Vp
Vd = lambda bd: Vp * np.exp(1j * bd) + Vm * np.exp(-1j * bd); Id = lambda bd: (Vp * np.exp(1j * bd) - Vm * np.exp(-1j * bd)) / Z0
chk("quarter wave: Zin ZL / Z0^2, I_L / (-j V_in/Z0); half wave: Zin/ZL, V_in/V_L, I_in/I_L",
    [Vd(pi / 2) / Id(pi / 2) * ZL / Z0 ** 2, Id(0) / (-1j * Vd(pi / 2) / Z0), Vd(pi) / Id(pi) / ZL, Vd(pi) / Vd(0), Id(pi) / Id(0)], [1, 1, 1, -1, -1])
v, l = 2e8, 100.0
chk("resonances l = 100 m, v = 2e8: like ends n v/2l; unlike (2n-1) v/4l [MHz]", [k * v / (2 * l) / 1e6 for k in (1, 2, 3)] + [(2 * k - 1) * v / (4 * l) / 1e6 for k in (1, 2, 3)], [1, 2, 3, 0.5, 1.5, 2.5])
print("== S12 homework rows")
J = 2.0; eta = 80 * pi
chk("HW9 #5: <S> per side = eta J^2/8; <Js.E> = -eta J^2/4 [W/m^2]", [eta * J ** 2 / 8, -eta * J ** 2 / 4], [40 * pi, -80 * pi])
chk("HW8 #1 relations: mu_r eps_r = (c/v)^2, mu_r/eps_r = (eta/eta0)^2 for mu_r = 1.5, eps_r = 6", [(c / (c / 3)) ** 2, (eta0 / 2 / eta0) ** 2], [1.5 * 6, 1.5 / 6])
chk("HW10 #2: seawater loss tangent at 1 kHz and 1 GHz", [18e9 * 4 / (1e3 * 81), 18e9 * 4 / (1e9 * 81)], [8.889e5, 0.8889], tol=1e-3)
print("== S9 Lectures 1-10 table")
rho, a_, r_in, r_out = 2.0, 0.7, 0.4, 1.3
chk("uniform sphere: D_r inside = rho r/3 (Q_enc/4 pi r^2); outside from the total charge", [rho * 4 / 3 * pi * r_in ** 3 / (4 * pi * r_in ** 2), rho * 4 / 3 * pi * a_ ** 3 / (4 * pi * r_out ** 2)], [rho * r_in / 3, rho * a_ ** 3 / (3 * r_out ** 2)])
chk("uniform cylinder: D_r inside = rho r/2; slab from the mid-plane: D_x = rho x (per unit area)", [rho * pi * r_in ** 2 / (2 * pi * r_in), rho * 2 * 0.3 / 2], [rho * r_in / 2, rho * 0.3])
eps = 3.2 * eps0; a1, b1 = 1e-3, 4e-3
rr = np.linspace(a1, b1, 200001); Vc = np.trapz(1 / (2 * pi * eps * rr), rr)       # volts per (C/m)
chk("coax: C per metre from integrating E vs 2 pi eps/ln(b/a)", 1 / Vc, 2 * pi * eps / np.log(b1 / a1), tol=1e-6)
Vs = np.trapz(1 / (4 * pi * eps * rr ** 2), rr)
chk("concentric spheres: C from integrating E vs 4 pi eps a b/(b-a)", 1 / Vs, 4 * pi * eps * a1 * b1 / (b1 - a1), tol=1e-6)
h = 1e-4; r0 = 0.9
lap_cyl = lambda V, r: (V(r + h) - 2 * V(r) + V(r - h)) / h ** 2 + (V(r + h) - V(r - h)) / (2 * h) / r
lap_sph = lambda V, r: (V(r + h) - 2 * V(r) + V(r - h)) / h ** 2 + 2 * (V(r + h) - V(r - h)) / (2 * h) / r
chk("Laplace: ln r in a coax and 1/r between spheres (1 + residual)", [1 + lap_cyl(np.log, r0), 1 + lap_sph(lambda r: 1 / r, r0)], [1, 1], tol=1e-5)
sig = 1e-4; C0 = 3e-11; G0 = sig / eps * C0
chk("G = (sigma/eps) C gives RC = eps/sigma [s]; relaxation exponent sigma/eps [1/s]", [C0 / G0, sig / eps], [eps / sig, sig / eps])
chk("point charge: V = Q/(4 pi eps0 R) is -integral of E from infinity (R = 2 m, Q = 1 nC) [V]", np.trapz(1e-9 / (4 * pi * eps0 * np.linspace(2, 2e4, 2000001) ** 2), np.linspace(2, 2e4, 2000001)), 1e-9 / (4 * pi * eps0 * 2), tol=2e-4)
print("== S9 tools table (earlier lectures)")
eps = 2.3 * eps0; aa, bb, Wd, dd = 0.5e-3, 1.7e-3, 0.04, 0.003
Cc = 2 * pi * eps / np.log(bb / aa); Lc = mu0 / (2 * pi) * np.log(bb / aa); Cp = eps * Wd / dd; Lp = mu0 * dd / Wd
chk("line parameters: L C/(mu eps) for coax and plates; sqrt(L/C) vs (eta/2pi) ln(b/a) and eta d/W", [Lc * Cc / (mu0 * eps), Lp * Cp / (mu0 * eps), np.sqrt(Lc / Cc) / (np.sqrt(mu0 / eps) / (2 * pi) * np.log(bb / aa)), np.sqrt(Lp / Cp) / (np.sqrt(mu0 / eps) * dd / Wd)], [1, 1, 1, 1])
tt = np.linspace(0, 1, 200001); sg, E0 = 0.02, 3.0
chk("<J.E> = sigma E0^2/2 for E0 cos(wt); conduction/displacement amplitude ratio = sigma/(w eps)", [np.trapz(sg * (E0 * np.cos(2 * pi * tt)) ** 2, tt), sg * E0 / (2 * pi * 1e6 * eps * E0)], [sg * E0 ** 2 / 2, sg / (2 * pi * 1e6 * eps)], tol=1e-6)
Js = np.array([0.0, 2.0, 0.0]); nh = np.array([0.0, 0.0, 1.0]); eta_ = 120 * pi
E_ = -eta_ / 2 * Js; H_ = 0.5 * np.cross(Js, nh)
chk("sheet: E = -(eta/2) Js, H = (1/2) Js x n above the sheet; E x H along n; |E|/|H| = eta", [np.dot(np.cross(E_, H_), nh) > 0, np.linalg.norm(E_) / np.linalg.norm(H_) / eta_, *(np.cross(nh, E_) / eta_ - H_)], [1, 1, 0, 0, 0])
print(f"\nSUMMARY: {n['p']} PASS, {n['f']} FAIL")
