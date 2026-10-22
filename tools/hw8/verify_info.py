#!/usr/bin/env python3
"""Numbers and directions for the two HW8 #5 infographics (figs_hw8.py).

Every number printed on info-wave-anatomy / info-wave-journey is computed here; every
direction claim is an np.cross. Run: python3 verify_info.py | tee verify_info.out
"""
import numpy as np

MU0 = 4e-7 * np.pi
EPS0 = 8.8541878128e-12
fails = 0


def check(name, got, want, tol=5e-3):
    global fails
    ok = abs(got - want) <= tol * max(abs(want), 1e-30)
    fails += 0 if ok else 1
    print(f"{'PASS' if ok else 'FAIL'}  {name}: computed {got:.6g}, shown {want:.6g}")


def check_vec(name, got, want):
    global fails
    ok = np.allclose(got, want)
    fails += 0 if ok else 1
    print(f"{'PASS' if ok else 'FAIL'}  {name}: {np.round(got, 6).tolist()} == {[float(v) for v in want]}")


xh, yh, zh = np.eye(3)

# ---------------------------------------------------------------- constants shared by both versions
c = 1 / np.sqrt(MU0 * EPS0)
eta0 = np.sqrt(MU0 / EPS0)
print("== constants")
check("c = 1/sqrt(mu0 eps0)  [m/s]", c, 3.0e8, tol=2e-3)
check("eta0 = sqrt(mu0/eps0) [ohm]", eta0, 377.0, tol=2e-3)
check("c in m per microsecond", c * 1e-6, 300.0, tol=2e-3)
# the panels round eta0 to 377 and c to 3e8; worked examples below use the exact values and then round

# ---------------------------------------------------------------- version A: 100 MHz, E0 = 3 V/m
print("== version A worked example (100 MHz, E0 = 3 V/m)")
f, E0 = 100e6, 3.0
lam = c / f
w = 2 * np.pi * f
beta = w / c
H0 = E0 / eta0
Savg = E0 ** 2 / (2 * eta0)
check("lambda = c/f [m]", lam, 3.0, tol=2e-3)
check("beta = 2 pi / lambda [rad/m]", 2 * np.pi / lam, 2.094, tol=2e-3)
check("beta = omega / c agrees", beta, 2 * np.pi / lam, tol=1e-9)
check("omega = 2 pi f [rad/s]", w, 6.283e8, tol=1e-3)
check("H0 = E0/eta0 [mA/m]", H0 * 1e3, 7.96, tol=2e-3)
check("<S> = E0^2 / 2 eta0 [mW/m^2]", Savg * 1e3, 11.9, tol=5e-3)
check("<S> = E0 H0 / 2 agrees [mW/m^2]", E0 * H0 / 2 * 1e3, Savg * 1e3, tol=1e-9)
check("period T = 1/f [ns]", 1 / f * 1e9, 10.0, tol=1e-6)
# the snapshot plotted in the figure: E/E0 = cos(wt - beta z) at t = 0 over 0..2 lambda; crest spacing = lambda
z = np.linspace(0, 2 * lam, 4001)
Ez = E0 * np.cos(-beta * z)
crests = z[np.r_[False, (Ez[1:-1] > Ez[:-2]) & (Ez[1:-1] > Ez[2:]), False]]
check("snapshot crest spacing [m]", float(np.diff(np.r_[0.0, crests])[-1]), lam, tol=1e-3)

# ---------------------------------------------------------------- version B: 50 kW isotropic at 10 km
print("== version B worked example (50 kW isotropic, r = 10 km)")
P, r = 50e3, 10e3
S = P / (4 * np.pi * r ** 2)
E0b = np.sqrt(2 * eta0 * S)
H0b = E0b / eta0
tau = r / c
check("<S> = P / 4 pi r^2 [uW/m^2]", S * 1e6, 39.8, tol=2e-3)
check("E0 = sqrt(2 eta0 <S>) [V/m]", E0b, 0.173, tol=2e-3)
check("H0 = E0/eta0 [mA/m]", H0b * 1e3, 0.459, tol=3e-3)
check("delay r/c [us]", tau * 1e6, 33.3, tol=2e-3)
check("sphere area 4 pi r^2 [km^2]", 4 * np.pi * r ** 2 * 1e-6, 1257.0, tol=1e-3)
check("doubling r quarters <S>: S(20 km)/S(10 km)", (P / (4 * np.pi * (2 * r) ** 2)) / S, 0.25, tol=1e-9)
check("1 us of travel [m]", c * 1e-6, 300.0, tol=2e-3)
# current sheet: |E| = eta0 |Js| / 2 ; sample Js = 1 mA/m used in the station-1 sketch caption
Js = 1e-3
check("sheet: |E| = eta0 Js/2 for Js = 1 mA/m [V/m]", eta0 * Js / 2, 0.188, tol=3e-3)
check("sheet: |H| = Js/2 [mA/m]", Js / 2 * 1e3, 0.5, tol=1e-9)
# common-mistakes strip: v in glass (eps_r = 2.25) is c/1.5 ; peak vs average factor 2
check("v in eps_r = 2.25 is c/n, n = 1.5", c / np.sqrt(2.25) / c, 1 / 1.5, tol=1e-9)
check("peak power density / average = 2", (E0b ** 2 / eta0) / S, 2.0, tol=1e-9)

# ---------------------------------------------------------------- directions (all np.cross)
print("== directions")
# plane wave: E along x, H along y, travel along z
check_vec("x_hat x y_hat = z_hat  (E x H -> +z travel)", np.cross(xh, yh), zh)
# H = z_hat x E / eta0 for a +z wave with E along x: z_hat x x_hat = y_hat
check_vec("z_hat x x_hat = y_hat  (H = z x E/eta0 is along +y)", np.cross(zh, xh), yh)
# a -z wave: H = (-z_hat) x E / eta0 -> along -y, and E x H -> -z
Hm = np.cross(-zh, xh)
check_vec("(-z) x x = -y  (H of a -z wave)", Hm, -yh)
check_vec("E x H for the -z wave points to -z", np.cross(xh, Hm), -zh)
# current sheet Js = Js x_hat at z = 0: E = -eta0 Js/2 x_hat both sides, H = -(Js/2) y for z>0, +(Js/2) y for z<0
Jvec = Js * xh
Eplus = -eta0 / 2 * Jvec
Hplus = np.cross(zh, Eplus) / eta0
Hminus = np.cross(-zh, Eplus) / eta0
check_vec("sheet: E direction = -Js direction", Eplus / np.linalg.norm(Eplus), -xh)
check_vec("sheet: Ampere jump z x (H+ - H-) = Js", np.cross(zh, Hplus - Hminus), Jvec)
check_vec("sheet: E x H for z>0 points to +z (away)", np.cross(Eplus, Hplus) / np.linalg.norm(np.cross(Eplus, Hplus)), zh)
check_vec("sheet: E x H for z<0 points to -z (away)", np.cross(Eplus, Hminus) / np.linalg.norm(np.cross(Eplus, Hminus)), -zh)
# drawn frame of the anatomy figure: screen right = z, screen up = x, toward the viewer (oblique down-right) = y
R, U, O = np.eye(3)                  # screen right, up, out-of-page (toward viewer); right-handed: R x U = O
check_vec("screen frame right-handed: R x U = O", np.cross(R, U), O)
x_draw, y_draw, z_draw = U, O, R     # x drawn up, y drawn toward the viewer, z drawn to the right
check_vec("drawn frame: x_draw x y_draw = z_draw (right-handed)", np.cross(x_draw, y_draw), z_draw)
# journey figure station sketches: E up (x), H out of page (odot = +y), travel right (+z)
check_vec("journey sketch: up x out = right  (E x H along travel)", np.cross(U, O), R)

print("== summary")
print(f"{'PASS' if fails == 0 else 'FAIL'}  {fails} failures")
