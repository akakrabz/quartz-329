#!/usr/bin/env python3
"""Build 14: FA26 HW9 re-solved (exact constants) and compared with the posted solution set.
PASS = agreement; KEY? = a slip in the posted solutions (recorded on the errata page).
The page content/homework/hw9-... quotes only numbers printed here."""
import numpy as np
pi = np.pi; c = 2.99792458e8; mu0 = 4e-7 * pi; eps0 = 8.8541878128e-12; eta0 = np.sqrt(mu0 / eps0)
X, Y, Z = np.eye(3); n = dict(p=0, f=0, k=0)
def chk(label, mine, key, tol=3e-3):
    ok = np.allclose(np.asarray(mine, complex), np.asarray(key, complex), rtol=tol, atol=1e-12)
    n["p" if ok else "f"] += 1; print(("PASS " if ok else "FAIL ") + f"{label}: {np.round(np.asarray(mine), 5)} (key {key})")
def keyq(label, mine, key, why):
    n["k"] += 1; print(f"KEY?  {label}: re-solved {mine}; posted solution writes {key} -- {why}")
print("== 1a  mu0, 12 eps0, E along x, S along -y, w = 12 pi 1e14")
w = 12 * pi * 1e14; f = w / 2 / pi; eta = eta0 / np.sqrt(12); v = c / np.sqrt(12); lam = v / f
chk("eta [ohm], v [m/s], lambda [nm], lambda0 [nm], beta [1/m]", [eta, v, lam * 1e9, c / f * 1e9, 2 * pi / lam], [108.83, 8.66e7, 144.3, 500, 4.35e7])
chk("H direction = u x E, u = -y, E = x", np.cross(-Y, X), Z)
chk("complex S direction x cross z", np.cross(X, Z), -Y)
print("== 1b  mu0, v = c/2, H along z, E along y, lambda = 1 um")
v = c / 2; lam = 1e-6; w = 2 * pi * v / lam
chk("eps_r, eta/pi, w [rad/s], T [s], lambda0 [um]", [(c / v) ** 2, eta0 / 2 / pi, w, 2 * pi / w, 2 * lam * 1e6], [4, 60, 9.42e14, 6.67e-15, 2])
chk("travel direction E x H = y x z", np.cross(Y, Z), X)
print("== 1c  eps0, v = c, RHCP toward +z, 3 GHz")
lam = c / 3e9; chk("lambda [m], beta/pi", [lam, 2 * pi / lam / pi], [0.1, 20])
E = np.array([1, -1j, 0]); H = np.cross(Z, E) / eta0
chk("H phasor (times eta) = y + j x", H * eta0, [1j, 1, 0]); chk("complex S (times eta), <S> (times eta)", [np.cross(E, np.conj(H))[2] * eta0, 0.5 * np.real(np.cross(E, np.conj(H)))[2] * eta0], [2, 1])
print("== 2  sheet x Jso sin(wt), 2 W/m^2 each side")
E0 = np.sqrt(4 * eta0); H0 = E0 / eta0
chk("E0 [V/m], H0 [A/m], Jso [A/m] (= 2 H0 = 8/E0)", [E0, H0, 2 * H0, 8 / E0], [38.83, 0.103, 0.206, 0.206])
chk("phasor of -x E0 sin(.) is +j E0 x; of -y H0 sin(.) is +j H0 y", [-1 * (-1j), -1 * (-1j)], [1j, 1j])
keyq("2c general line", "H~ = (+/-) j H0 e^{-/+ j beta z} y", "(+/-) j E0 e^{-/+ j beta z} y", "E0 typed for H0; the explicit lines below it (0.103 j) are right")
print("== 3  H = x 25 e^{-z} cos(8 pi 1e6 t - sqrt3 z - pi/3), mu0")
w = 8 * pi * 1e6; g = 1 + 1j * np.sqrt(3); eta = 1j * w * 4e-7 * pi / g; q = g / eta
chk("eta [ohm] = (4 pi^2/5)(sqrt3 + j)", eta, 4 * pi ** 2 / 5 * (np.sqrt(3) + 1j)); chk("|eta|, angle [deg]", [abs(eta), np.degrees(np.angle(eta))], [8 * pi ** 2 / 5, 30])
chk("gamma/eta [S/m], eps [F/m], sigma [S/m], eps_r", [q, q.imag / w, q.real], [0.110 + 0.0633j, 2.52e-9, 0.110], tol=5e-3); print(f"      eps_r = {q.imag / w / eps0:.1f}, loss tangent = {q.real / q.imag:.4f}")
Eamp = abs(eta) * 25; chk("|E| [V/m] = 40 pi^2, E direction = H x u = x cross z, E phase [deg]", [Eamp, *np.cross(X, Z), np.degrees(-pi / 3 + np.angle(eta))], [40 * pi ** 2, 0, -1, 0, -30])
S0 = 0.5 * Eamp * 25 * np.cos(np.angle(eta)); chk("<S> at z=0 [W/m^2] = 250 sqrt3 pi^2", S0, 250 * np.sqrt(3) * pi ** 2)
P = S0 * (1 - np.exp(-2)); Pj = 0.5 * q.real * Eamp ** 2 * (1 - np.exp(-2)) / 2      # volume integral of (1/2) sigma |E|^2
chk("3f power dissipated in the unit cube [W]: flux difference = Joule integral", P, Pj)
print(f"      3f = {P:.1f} W = {P / 1e3:.3f} kW")
keyq("3f", f"{P / 1e3:.3f} kW", "3.7441 kW", "250 sqrt3 pi^2 (1 - e^-2) = 4273.7 x 0.8647; the posted number is 1.3% high (arithmetic)")
print("== 4  seawater sigma = 4, eps_r = 81")
for fq, kd, kl in ((90e3, 3.8627, 5.27), (900.0, 38.63, 52.70)):
    a = np.sqrt(pi * fq * 4e-7 * pi * 4); me = np.sqrt(2 * pi * fq * 4e-7 * pi / 4)
    ge = np.sqrt(1j * 2 * pi * fq * mu0 * (4 + 1j * 2 * pi * fq * 81 * eps0))
    print(f"      f = {fq:g} Hz: loss tangent {4 / (2 * pi * fq * 81 * eps0):.3g}, alpha = beta = {a:.4f} (exact gamma {ge.real:.4f} + j{ge.imag:.4f}), |eta| = {me:.4f} ohm at 45 deg, eta = {me / np.sqrt(2):.4f}(1+j), delta = {1 / a:.3f} m")
    chk(f"1% depth [m], lambda [m] at {fq:g} Hz", [np.log(100) / a, 2 * pi / a], [kd, kl], tol=2e-3)
chk("alpha at 90 kHz and 900 Hz [Np/m], |eta| [ohm]", [np.sqrt(pi * 90e3 * 4e-7 * pi * 4), np.sqrt(pi * 900 * 4e-7 * pi * 4), np.sqrt(2 * pi * 90e3 * 4e-7 * pi / 4), np.sqrt(2 * pi * 900 * 4e-7 * pi / 4)], [1.1922, 0.119, 0.4215, 0.0421], tol=3e-3)
keyq("4a", "eta = 0.4215 at 45 deg ohm (0.298(1+j))", "'|eta| = 0.4215' then 'eta = 0.243 at 45 deg'", "the second line contradicts the first; 0.4215 is right")
keyq("4d loss tangent at 900 Hz", f"{4 / (2 * pi * 900 * 81 * eps0):.3g}", "2.96e6 (computed with 300 Hz)", "still >> 1, conclusion unchanged")
keyq("4d wavelength at 900 Hz", f"{2 * pi / np.sqrt(pi * 900 * 4e-7 * pi * 4):.2f} m", "57.71 m", "2 pi/0.1192 = 52.7 m (digits transposed)")
print("== 5  sheet 2cos(6 pi 1e8 t) y at x = 2 m, eps = (9/4) eps0")
w = 6 * pi * 1e8; v = 3e8 / 1.5; eta = 120 * pi / 1.5
chk("v [m/s], beta/pi, lambda [m], eta/pi", [v, w / v / pi, 2 * pi / (w / v), eta / pi], [2e8, 3, 2 / 3, 80])
chk("E = -(eta/2) Js: amplitude/eta; H for x>2 = (1/2) Js x x_hat: direction, amplitude", [1.0, *np.cross(Y, X), 1.0], [1, 0, 0, -1, 1])
chk("5f <P> through 2 m^2 [W] = eta = 80 pi", 0.5 * eta * 1 * 2, 80 * pi); chk("5g <Js.E> [W/m^2] = -eta = -2 x one-sided <S>", [-0.5 * 2 * eta, -2 * 0.5 * eta], [-80 * pi, -80 * pi])
keyq("5g units", "<Js.E> in W/m^2 (surface current)", "W/m^3", "units only")
print(f"\nSUMMARY: {n['p']} PASS, {n['f']} FAIL, {n['k']} KEY?")
