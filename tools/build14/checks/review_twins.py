#!/usr/bin/env python3
"""Build 14, independent second pass on the new twins and the summary's worked numbers.
Routes that do not reuse the pages' formulas: time-domain line simulation run to sinusoidal
steady state (tlsim: Kirchhoff at the nodes, no Gamma), spectra of free oscillations, a lumped
LC-ladder model for input impedances, finite-difference Maxwell checks and numerical time averages.
The expected values are transcribed from the pages."""
import numpy as np
from tlsim import simulate, at
pi = np.pi; c = 3e8; mu0 = 4e-7 * pi; eps0 = 1e-9 / (36 * pi)
X, Y, Z = np.eye(3); n = dict(p=0, f=0)
def chk(label, mine, page, tol=5e-3, atol=1e-9):
    ok = np.allclose(np.asarray(mine, complex), np.asarray(page, complex), rtol=tol, atol=atol)
    n["p" if ok else "f"] += 1; print(("PASS " if ok else "FAIL ") + f"{label}: simulated/independent {np.round(np.asarray(mine), 4)} vs page {page}")
def phasor(t, y, w, periods=4):
    """complex amplitude of y(t) at angular frequency w over the last few periods (cos reference)"""
    T = 2 * pi / w; m = t >= t[-1] - periods * T + 1e-15
    return 2 * np.mean(y[m] * np.exp(-1j * w * t[m]))
def ladder_zin(Z0, v, length, w, ZL, N=4000):
    """input impedance of N lumped L-C sections (series L/2, shunt C, series L/2 each) ending in ZL"""
    dz = length / N; L = Z0 / v * dz; C = dz / (Z0 * v); Zs = 1j * w * L / 2; Yp = 1j * w * C
    Zx = ZL
    for _ in range(N):
        Zx = Zx + Zs
        Zx = 1 / (Yp + (0 if np.isinf(abs(Zx)) else 1 / Zx))
        Zx = Zx + Zs
    return Zx

print("== S1 open stub (2 m, 75 ohm, v = 2.4e8) in series with 150 ohm, 6 V source")
T1 = 2 / 2.4e8
for f, pageI, pageVin in ((60e6, 0.0, 6.0), (30e6, 0.040, 0.0)):
    w = 2 * pi * f; dt = T1 / 100
    r = simulate([(75, T1)], 150, np.inf, lambda t: 6 * np.cos(w * t), 120 / f, dt)
    I0 = phasor(r["t"], r["Inode"][0], w); V0 = phasor(r["t"], r["Vnode"][0], w); VL = phasor(r["t"], r["Vnode"][1], w)
    chk(f"{f / 1e6:.0f} MHz: resistor current phasor [A], stub input voltage [V]", [I0, V0], [pageI, pageVin], atol=2e-3)
    if f == 60e6:
        vm, im = r["probe"](0, 0.5)
        chk("60 MHz: open-end voltage [V] (opposite phase), |V| at d = 1 m, |I| at d = 1 m [A]", [VL, abs(phasor(r["t"], vm, w)), abs(phasor(r["t"], im, w))], [-6, 0, 0.080], tol=2e-2, atol=0.1)
print("== S2 quarter-wave 60 ohm section, 20 ohm load, 12 V behind 60 ohm")
f = 100e6; w = 2 * pi * f; Tq = 1 / f / 4; dt = Tq / 100
r = simulate([(60, Tq)], 60, 20, lambda t: 12 * np.cos(w * t), 40 / f, dt)
chk("V_in, I_in, V_L, I_L phasors", [phasor(r["t"], r["Vnode"][0], w), phasor(r["t"], r["Inode"][0], w), phasor(r["t"], r["Vnode"][1], w), phasor(r["t"], r["Inode"][1], w)], [9, 0.05, -3j, -0.15j], atol=2e-3)
pin = np.mean((r["Vnode"][0] * r["Inode"][0])[-400:]); pl = np.mean((r["Vnode"][1] ** 2 / 20)[-400:])
chk("time-averaged power into the line and into the load [W]", [pin, pl], [0.225, 0.225])
r = simulate([(60, 2 * Tq)], 60, 20, lambda t: 12 * np.cos(w * t), 40 / f, dt)
chk("half-wave section instead: V_in, V_L [V], load power [W]", [phasor(r["t"], r["Vnode"][0], w), phasor(r["t"], r["Vnode"][1], w), np.mean((r["Vnode"][1] ** 2 / 20)[-400:])], [3, -3, 0.225], atol=2e-3)
print("== S3 free oscillations of a 60 m line, v = 1.5e8 (spectrum of the ringing after a current kick)")
Tl = 60 / 1.5e8; dt = Tl / 40; N = 32768
for RL, name, page in ((np.inf, "open-open", [1.25, 2.5, 3.75]), (0.0, "short at load, open at input", [0.625, 1.875, 3.125])):
    r = simulate([(50, Tl)], 1e7, RL, lambda t: 1e7 if t < 3 * dt else 0.0, N * dt, dt)
    y = r["Inode"][1] if RL == 0 else r["Vnode"][1]
    sp = np.abs(np.fft.rfft(y - y.mean())); fr = np.fft.rfftfreq(len(y), dt)
    pk = [fr[i] for i in range(1, len(sp) - 1) if sp[i] > sp[i - 1] and sp[i] > sp[i + 1] and sp[i] > 0.2 * sp.max()]
    chk(f"{name}: three lowest spectral peaks [MHz]", np.array(pk[:3]) / 1e6, page, tol=1e-2)
w2 = 2 * pi * 2.5e6
chk("open-ended line seen from d = 15 m at 2.5 MHz (ladder): |Z| -> 0 [ohm]", abs(ladder_zin(50, 1.5e8, 15, w2, np.inf)), 0, atol=0.1)
print("== S4 open stub: Z_in/Z0 at 0.5, 1.5, 3 w0 and Y_in at 2 w0 (lumped ladder, l = 1 m, v = 2e8, Z0 = 1)")
w0 = pi / 2 * 2e8 / 1.0
chk("Z_in/Z0 at 0.5 w0, 1.5 w0, 3 w0", [ladder_zin(1, 2e8, 1, k * w0, np.inf) for k in (0.5, 1.5, 3)], [-1j, 1j, 0], tol=1e-2, atol=2e-2)
chk("Y_in Z0 at 2 w0", 1 / ladder_zin(1, 2e8, 1, 2 * w0, np.inf), 0, atol=2e-2)
print("== S5 Z0 = 50, ZL = 150 (ladder): Gamma(d) = (Z(d) - Z0)/(Z(d) + Z0)")
wv = 2 * pi * 1e8; lam = 2e8 / 1e8
G = lambda d: (lambda z: (z - 50) / (z + 50))(ladder_zin(50, 2e8, d, wv, 150.0))
chk("Gamma at d = lambda/8, lambda/4, lambda/2; Z(lambda/4) [ohm]", [G(lam / 8), G(lam / 4), G(lam / 2), ladder_zin(50, 2e8, lam / 4, wv, 150.0)], [-0.5j, -0.5, 0.5, 16.667], tol=1e-2, atol=5e-3)
print("== T6 sheet on x = 0, Js = -z 3 u(t) sin(2 pi f t), eps = 4 eps0")
f = 1.5e6; w = 2 * pi * f; eps = 4 * eps0; v = 1.5e8
Ez = lambda x, t: 90 * pi * np.sin(w * (t - abs(x) / v)) * (t > abs(x) / v)
Hy = lambda x, t: -np.sign(x) * 1.5 * np.sin(w * (t - abs(x) / v)) * (t > abs(x) / v)
x0, t0, dx, dtt = 120.0, 2.37e-6, 1e-3, 1e-12       # E = z Ez(x,t): curl E = -y dEz/dx; H = y Hy: curl H = z dHy/dx
far = -(Ez(x0 + dx, t0) - Ez(x0 - dx, t0)) / (2 * dx) + mu0 * (Hy(x0, t0 + dtt) - Hy(x0, t0 - dtt)) / (2 * dtt)
amp = (Hy(x0 + dx, t0) - Hy(x0 - dx, t0)) / (2 * dx) - eps * (Ez(x0, t0 + dtt) - Ez(x0, t0 - dtt)) / (2 * dtt)
chk("Faraday and Ampere-Maxwell residuals at (120 m, 2.37 us), relative", [far / (mu0 * 1.5 * w), amp / (eps * 90 * pi * w)], [0, 0], atol=1e-5)
far = -(Ez(-x0 + dx, t0) - Ez(-x0 - dx, t0)) / (2 * dx) + mu0 * (Hy(-x0, t0 + dtt) - Hy(-x0, t0 - dtt)) / (2 * dtt)
chk("Faraday residual on the other side (-120 m)", far / (mu0 * 1.5 * w), 0, atol=1e-5)
tq = 0.4e-6; jump = np.cross(X, (Hy(1e-9, tq) - Hy(-1e-9, tq)) * Y)       # n x (H+ - H-), n = +x
chk("jump condition n x (H1 - H2) = Js at t = 0.4 us [A/m, z component]", jump[2], -3 * np.sin(w * tq))
ts = np.linspace(4e-6, 4e-6 + 2 / f, 20001)[:-1]
chk("<S_x> at +200 m and -200 m [W/m^2]", [np.mean(-Ez(200, ts) * Hy(200, ts)), np.mean(-Ez(-200, ts) * Hy(-200, ts))], [212.06, -212.06])   # (z Ez) x (y Hy) = -x Ez Hy
chk("<Js . E> at the sheet [W/m^2]", np.mean(-3 * np.sin(w * ts) * Ez(0, ts)), -424.1)
chk("record at 300 m: zero at 1.9 us, positive at 2.1 us; snapshot at 3 us: zero at 460 m, H_y(25 m), H_y(440 m)", [Ez(300, 1.9e-6), np.sign(Ez(300, 2.1e-6)), Hy(460, 3e-6), Hy(25, 3e-6), Hy(440, 3e-6)], [0, 1, 0, -1.5, -1.5 * np.sin(2 * pi * 4.4)], tol=1e-3)
print("== summary page: bounce example (50 ohm, Rg = 25, RL = 100, 9 V step, T = 1 us) and the glass interface")
us = 1e-6
r = simulate([(50, us)], 25, 100, lambda t: 9.0, 60 * us, 1e-8)
chk("launched 6 V; load after first arrival 8 V; source end after 2T: 6+2-2/3; steady 7.2 V", [at(r["t"], r["Vnode"][0], 0.5 * us), at(r["t"], r["Vnode"][1], 1.5 * us), at(r["t"], r["Vnode"][0], 2.5 * us), r["Vnode"][1, -1]], [6, 8, 6 + 2 - 2 / 3, 7.2], tol=1e-4)
A = np.array([[1, -1], [1 / (120 * pi), 1 / (60 * pi)]]); Er, Et = np.linalg.solve(A, [-1, 1 / (120 * pi)])   # E continuous: 1 + Er = Et ; H continuous: (1 - Er)/eta1 = Et/eta2
chk("air -> eps_r = 4: Gamma, tau, reflected and transmitted power fractions", [Er, Et, Er ** 2, Et ** 2 * 2], [-1 / 3, 2 / 3, 1 / 9, 8 / 9], tol=1e-9)
print(f"\nSUMMARY: {n['p']} PASS, {n['f']} FAIL")
