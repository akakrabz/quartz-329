#!/usr/bin/env python3
"""R11.py -- independent re-solution of practice page 11 (Lorentz-Drude models).

Every number on the page is recomputed from the problem data, by a brute-force route where
possible: ODE integration of the Drude and Lorentz equations, convolution with the Drude impulse
response (for sigma(omega)), finite differences, charge-sheet superposition, a method-of-lines
solution of the relaxation PDE, eigenvalues of the modal state matrix, and time-domain fits.
PASS = agrees with the page to the last digit the page quotes (half a unit in that digit).
11.8 (a)-(b) are checked in their REWORKED form (rho0 sin(beta x) in lightly doped silicon).
"""
import re
import numpy as np
from scipy.integrate import solve_ivp, quad
from scipy.optimize import brentq, minimize_scalar

e, me, eps0, c0 = 1.602e-19, 9.109e-31, 8.854e-12, 2.998e8      # constants the page uses
NPASS = NFAIL = 0


def _unit(s):
    m = re.fullmatch(r'\s*[+-]?(\d+)(?:\.(\d+))?(?:e([+-]?\d+))?\s*', s)
    dec = len(m.group(2)) if m.group(2) else 0
    ex = int(m.group(3)) if m.group(3) else 0
    return 10.0 ** (ex - dec)


def chk(label, val, stated, tol=None):
    global NPASS, NFAIL
    ref = float(stated)
    t = 0.5 * _unit(stated) * (1 + 1e-9) if tol is None else tol
    ok = abs(val - ref) <= t
    NPASS += ok
    NFAIL += (not ok)
    print(f"{'PASS' if ok else 'FAIL'}  {label}: computed {val:.6g}   page {stated}")


def chk_true(label, cond, detail=""):
    global NPASS, NFAIL
    NPASS += bool(cond)
    NFAIL += (not cond)
    print(f"{'PASS' if cond else 'FAIL'}  {label} {detail}")


def drude_steady(N, q, m, tau, E):
    """Integrate m dv/dt = qE - m v/tau from rest to 40 tau. Returns v_final, J = Nqv, solution."""
    sol = solve_ivp(lambda t, v: q * E / m - v / tau, [0, 40 * tau], [0.0], method='LSODA',
                    rtol=1e-11, atol=1e-30, dense_output=True)
    v = sol.y[0, -1]
    return v, N * q * v, sol


def drude_conv_sigma(omega, tau, sig_dc, npts=24):
    """AC sigma by brute force: J(t) = (sig_dc/tau) int_0^inf exp(-s/tau) E(t-s) ds (the Drude impulse
    response) with E = cos(wt); fit J = a cos wt + b sin wt; Re{sigma e^{jwt}} gives sigma = a - j b."""
    T = 2 * np.pi / omega
    ts = np.linspace(0, T, npts, endpoint=False)
    J = [sig_dc / tau * quad(lambda s: np.exp(-s / tau) * np.cos(omega * (t - s)), 0, 60 * tau,
                             limit=800, epsabs=1e-12 * tau, epsrel=1e-10)[0] for t in ts]
    M = np.column_stack([np.cos(omega * ts), np.sin(omega * ts)])
    a, b = np.linalg.lstsq(M, np.array(J), rcond=None)[0]
    return a - 1j * b


# dimension vectors (kg, m, s, A) for the unit claims
KG, MM, S, AMP = np.eye(4)
C_ = AMP + S
V_ = KG + 2 * MM - 3 * S - AMP
F_ = C_ - V_
SIEM = AMP - V_

print("=== 11.1 Drift speed in a house wire ===")
A, I, N = 1.5e-6, 10.0, 8.5e28
J = np.array([0, 0, I / A])
v = J / (N * (-e))
chk("J_z [A/m^2]", J[2], "6.67e6")
chk("v_z [m/s]", v[2], "-4.9e-4")
chk("|v| [mm/s]", abs(v[2]) * 1e3, "0.49")
chk_true("v antiparallel to J (electrons drift along -z):", np.dot(v, J) < 0 and v[2] < 0)
t1 = 1.0 / abs(v[2])
chk("time to drift 1 m [s]", t1, "2.0e3")
chk("  in minutes", t1 / 60, "34")
chk("Ne [C/m^3]", N * e, "1.36e10")
chk("Ne|v| [A/m^2]", N * e * abs(v[2]), "6.67e6")

print("\n=== 11.2 Conductivity of aluminum ===")
N, tau, E = 1.8e29, 7.5e-15, 0.1
v, Jx, sol = drude_steady(N, -e, me, tau, E)
mob = abs(v) / E
chk("sigma = J/E from ODE steady state [S/m]", Jx / E, "3.8e7")
chk("mobility |v|/E [m^2/Vs]", mob, "1.32e-3")
chk("v_x [m/s] (E = 0.1 x V/m)", v, "-1.32e-4")
chk("v(tau)/v_final [%]", sol.sol(tau)[0] / v * 100, "63")
chk("check N e x 1.32e-3 [S/m]", N * e * 1.32e-3, "3.8e7")
mob_cu = 5.96e7 / (8.5e28 * e)
chk("copper mobility [m^2/Vs]", mob_cu, "4.4e-3")
chk("N_Al/N_Cu", N / 8.5e28, "2.1")
chk("mob_Cu/mob_Al", mob_cu / mob, "3.3")
chk_true("units: e tau/m == m^2/(V s):", np.allclose(C_ + S - KG, 2 * MM - V_ - S))

print("\n=== 11.3 Which change doubles sigma ===")
Ncu, nu = 8.5e28, 4.1e13


def sig_of(Nn=Ncu, q=-e, m=me, nn=nu, Ef=1.0):
    vv, JJ, _ = drude_steady(Nn, q, m, 1 / nn, Ef)
    return JJ / Ef, vv, JJ


s0, v1, J1 = sig_of()
sa, v2, J2 = sig_of(Ef=2.0)
chk("sigma_0 copper [S/m]", s0, "5.84e7")
chk("drift at 1 V/m [mm/s]", abs(v1) * 1e3, "4.29")
chk("drift at 2 V/m [mm/s]", abs(v2) * 1e3, "8.58")
chk("J at 1 V/m [A/m^2]", J1, "5.84e7")
chk("J at 2 V/m [A/m^2]", J2, "1.17e8")
chk("(a) J/E at 2 V/m [S/m]", sa, "5.84e7")
rat = {'a': sa / s0, 'b': sig_of(q=-2 * e)[0] / s0, 'c': sig_of(nn=nu / 2)[0] / s0,
       'd': sig_of(m=2 * me)[0] / s0, 'e': sig_of(q=+e)[0] / s0}
print("   sigma/sigma0 by option:", {k: round(r, 6) for k, r in rat.items()})
chk("(b) ratio", rat['b'], "4")
chk("(c) ratio", rat['c'], "2")
chk("(d) ratio", rat['d'], "0.5")
chk("(e) ratio", rat['e'], "1")
chk_true("only (c) doubles sigma (key = c):", [k for k, r in rat.items() if abs(r - 2) < 1e-6] == ['c'])
_, ve, Je = sig_of(q=+e)
chk_true("(e) positive carriers drift along E and J still along E:", ve > 0 and Je > 0 and J1 > 0 and v1 < 0)

print("\n=== 11.4 True or false ===")
w0 = 2e16
rx = brentq(lambda r: -e * 1.0 - me * w0 ** 2 * r, -1, 1, xtol=1e-40)       # static force balance, E = +x
px = -e * rx
chk_true("(i) FALSE: electron pulled against E and p = -e r along E:", rx < 0 and px > 0,
         f"(r_x = {rx:.3e} m, p_x = {px:.3e} C m)")
f = 50.0
t = np.linspace(0, 1 / f, 400001)
Pt = eps0 * 2.0 * 100.0 * np.cos(2 * np.pi * f * t)
Jp = np.gradient(Pt, t)
chk("(ii) |J_p| amplitude by finite differences [A/m^2]", np.max(np.abs(Jp)), "5.56e-7")
Kc = e ** 2 / (me * eps0)
chk("e^2/(m_e eps0) [m^3/s^2]", Kc, "3.18e3")
chi3 = 5e28 * Kc / (2e16) ** 2
chk("(iii) chi_e", chi3, "0.40")
chk("(iii) eps_r", 1 + chi3, "1.40")
sc, Nc = 5.8e7, 8.5e28
tau_c = sc * me / (Nc * e ** 2)
tr_c = eps0 / sc
chk("(iv) Drude tau [s]", tau_c, "2.4e-14")
chk("(iv) eps0/sigma [s]", tr_c, "1.5e-19")
chk("(iv) ratio", tau_c / tr_c, "1.6e5")
x5 = 2 * np.pi * 1e10 / 4e13
chk("(v) omega/nu", x5, "1.6e-3")
sr = drude_conv_sigma(2 * np.pi * 1e10, 1 / 4e13, 1.0)
chk("(v) |sigma/sigma_DC - 1| by convolution [%]", abs(sr - 1) * 100, "0.16")
chk("(v) closed form x/sqrt(1+x^2) [%]", x5 / np.sqrt(1 + x5 ** 2) * 100, "0.16")

print("\n=== 11.5 Sea water's two ions ===")
N = 3.0e26
mup, mum, mp, mm = 4.0e-8, 6.0e-8, 3.8e-26, 5.9e-26
chk("0.5 mol/L in m^-3", 0.5e3 * 6.022e23, "3.0e26")
Ev = np.array([1.0, 0, 0])
vp, vm = mup * Ev, -mum * Ev
Jpv, Jmv = N * e * vp, N * (-e) * vm
sig = (Jpv + Jmv)[0]
chk("student's sigma [S/m]", N * e * (mup - mum), "-0.96")
chk("sigma [S/m]", sig, "4.8")
chk_true("both species' J along E:", Jpv[0] > 0 and Jmv[0] > 0)
chk("Na+ part [S/m]", Jpv[0], "1.92")
chk("Cl- part [S/m]", Jmv[0], "2.88")
chk("Na+ share [%]", Jpv[0] / sig * 100, "40")
chk("Cl- share [%]", Jmv[0] / sig * 100, "60")
taup, taum = mup * mp / e, mum * mm / e
chk("tau+ [s]", taup, "9.5e-15")
chk("tau- [s]", taum, "2.2e-14")
chk("nu+ [1/s]", 1 / taup, "1.05e14")
chk("nu- [1/s]", 1 / taum, "4.5e13")
w10 = 2 * np.pi * 1e10
chk("omega/nu+ at 10 GHz", w10 * taup, "5.96e-4")
chk("omega/nu- at 10 GHz", w10 * taum, "1.39e-3")
_, Jps, _ = drude_steady(N, +e, mp, taup, 1.0)
_, Jms, _ = drude_steady(N, -e, mm, taum, 1.0)
chk("species sum from two ODE steady states [S/m]", Jps + Jms, "4.8")
chk("Na+ N e^2/(m+ nu+) [S/m]", N * e ** 2 * taup / mp, "1.92")
s_ac = N * e ** 2 / (mp * (1 / taup + 1j * w10)) + N * e ** 2 / (mm * (1 / taum + 1j * w10))
chk("|sigma(10 GHz)| [S/m]", abs(s_ac), "4.8")
chk_true("J.E = sigma E^2 > 0 for the corrected sigma, < 0 for the student's:", sig > 0 and N * e * (mup - mum) < 0)

print("\n=== 11.6 A conductor as a low-pass filter ===")
N, mst, tau = 1.0e22, 0.26 * me, 1.8e-13
chk("m* [kg]", mst, "2.37e-31")
mob = e * tau / mst
chk("mobility [m^2/Vs]", mob, "0.122")
chk("mobility [cm^2/Vs]", mob * 1e4, "1220", tol=5)
sdc = N * e * mob
chk("sigma_DC [S/m]", sdc, "195")
chk("check N e^2 tau/m* [S/m]", N * e ** 2 * tau / mst, "195")
v, _, sol = drude_steady(N, -e, mst, tau, 1.0)
chk("v_final for E0 = 1 V/m [m/s] (ODE)", v, "-0.122")
t99 = brentq(lambda tt: sol.sol(tt)[0] / v - 0.99, 0.1 * tau, 20 * tau, xtol=1e-30)
chk("1% settling time / tau (ODE)", t99 / tau, "4.6")
chk("1% settling time [s]", t99, "8.3e-13")
nu = 1 / tau
chk("nu [rad/s]", nu, "5.56e12")
chk("f = nu/2pi [THz]", nu / 2 / np.pi / 1e12, "0.88")
sw = drude_conv_sigma(nu, tau, sdc)
chk("Re sigma(omega = nu) by convolution [S/m]", sw.real, "97.5")
chk("-Im sigma(omega = nu) [S/m]", -sw.imag, "97.5")
chk("|sigma| [S/m]", abs(sw), "138")
chk("angle [deg]", np.degrees(np.angle(sw)), "-45")


def Jt(tt):
    return sdc / tau * quad(lambda s: np.exp(-s / tau) * np.cos(nu * (tt - s)), 0, 60 * tau,
                            limit=800, epsabs=0, epsrel=1e-12)[0]


res = minimize_scalar(lambda tt: -Jt(tt), bounds=(0, np.pi / nu), method='bounded', options={'xatol': 1e-19})
chk("current peak after field peak (brute force) [s]", res.x, "1.41e-13")
chk("(pi/4) tau [s]", np.pi / 4 * tau, "1.41e-13")
chk("peak J / E0 [S/m]", -res.fun, "138")
xs = brentq(lambda x: abs(1 / (1 + 1j * x) - 1) - 0.01, 1e-6, 1)
chk("x = omega/nu at 1%", xs, "0.0100005")
chk("f_max silicon [GHz]", xs * nu / 2 / np.pi / 1e9, "8.8")
chk("f_max copper [GHz]", xs * 4.1e13 / 2 / np.pi / 1e9, "65")
chk("|sigma|/sigma_DC at f_max", 1 / np.sqrt(1 + xs ** 2), "0.99995")
chk("phase at f_max [deg]", -np.degrees(np.arctan(xs)), "-0.57")

print("\n=== 11.7 Conductor-like or dielectric-like ===")
Nd, w0, sg = 4.0e28, 1.0e16, 1.0e-12
wp2 = Nd * e ** 2 / (me * eps0)
chk("N_d e^2/(m eps0) [1/s^2]", wp2, "1.273e32")
chi = wp2 / w0 ** 2
chk("chi_e glass", chi, "1.27")
chk("eps_r glass", 1 + chi, "2.27")
fx = sg / (2 * np.pi * eps0 * chi)
chk("f_x glass [Hz]", fx, "0.0141")
chk("|J_p|/|J_c| at 60 Hz", 60 / fx, "4.2e3")
chk("omega0/2pi [Hz]", w0 / 2 / np.pi, "1.59e15")
dev = (1 / (1 - 0.01 ** 2) - 1) * 100
print(f"   Lorentz response at 0.01 omega0 vs static: +{dev:.6f} % (page now says 'by only 0.01%')")
chk("Lorentz deviation at 0.01 omega0 [%]", dev, "0.01")
chk("resonance wavelength 2 pi c/omega0 [nm]", 2 * np.pi * c0 / w0 * 1e9, "188")
T60 = 1 / 60
t = np.linspace(-T60 / 2, T60 / 2, 400001)
Jpt = np.gradient(eps0 * chi * np.cos(2 * np.pi * 60 * t), t)
chk("J_p peak time / T for E peak at t = 0 (-0.25 = leads by 90 deg)", t[np.argmax(Jpt)] / T60, "-0.25", tol=1e-4)
chk("amplitude ratio from FD amplitudes at 60 Hz", np.max(np.abs(Jpt)) / sg, "4.2e3")
ss, er = 4.0, 81.0
fxs = ss / (2 * np.pi * eps0 * (er - 1))
chk("f_x sea water [GHz]", fxs / 1e9, "0.90")
chk("f_x sea water (Check line) [GHz]", fxs / 1e9, "0.899")
chk("ratio at 20 kHz", 2e4 / fxs, "2.2e-5")
chk("conduction wins by", fxs / 2e4, "4.5e4")
chk("ratio at 10 GHz", 1e10 / fxs, "11")
chk("f/f_x at 1 GHz", 1e9 / fxs, "1.11")
trs = er * eps0 / ss
chk("tau_r sea [s]", trs, "1.79e-10")
chk("f_r sea [GHz]", 1 / (2 * np.pi * trs) / 1e9, "0.888")
trg = (1 + chi) * eps0 / sg
chk("tau_r glass [s]", trg, "20.1")
chk("f_r glass [Hz]", 1 / (2 * np.pi * trg), "0.00791")
chk("f_x/f_r sea", fxs * 2 * np.pi * trs, "1.0125")
chk("f_x/f_r glass", fx * 2 * np.pi * trg, "1.79")
chk("vacuum share of dD/dt, sea [%]", 100 / er, "1.2")
chk("vacuum share of dD/dt, glass [%]", 100 / (1 + chi), "44")
for name, s_, epsr, page in [("sea", ss, er, "0.888e9"), ("glass", sg, 1 + chi, "0.00791")]:
    Cp, Gp = epsr * eps0 * 1e-2 / 1e-3, s_ * 1e-2 / 1e-3        # plates A = 1e-2 m^2, d = 1 mm
    chk(f"f where omega C = G for a 1 cm^2... plate cap ({name}) [Hz]",
        brentq(lambda ff: 2 * np.pi * ff * Cp - Gp, 1e-8, 1e12), page)
chk("sqrt(eps_r) glass", np.sqrt(1 + chi), "1.51")

print("\n=== 11.8 Relaxation time versus collision time (reworked (a)-(b)) ===")
eps_si, Nsi, msi, tsi = 11.7 * eps0, 1.0e20, 0.26 * me, 1.8e-13
mob_si = e * tsi / msi
sig_si = Nsi * e ** 2 * tsi / msi
tr_si = eps_si / sig_si
chk("(b) Si mobility [m^2/Vs]", mob_si, "0.122")
chk("(b) Si sigma = N e^2 tau/m* [S/m]", sig_si, "1.95")
chk("(b) sigma via N e x 0.122 [S/m]", Nsi * e * 0.122, "1.95")
chk("(b) tau_r = eps/sigma [s]", tr_si, "5.31e-11")
chk("(b) tau_r [ps]", tr_si * 1e12, "53")
rho0, beta = 46.8 * eps0, 2.0
amp = rho0 / (beta * eps_si)
chk("(b) E_x amplitude rho0/(beta eps) [V/m]", amp, "2")
chk_true("units: rho0/(beta eps) is V/m:", np.allclose((C_ - 3 * MM) - (-MM + F_ - MM), V_ - MM))


def Ecl(x, tt):
    return -amp * np.cos(beta * x) * np.exp(-tt / tr_si)


def rcl(x, tt):
    return rho0 * np.sin(beta * x) * np.exp(-tt / tr_si)


# brute-force E at t = 0: superposition of charge sheets, dE_x = rho dx'/(2 eps) sgn(x - x'),
# over a window of 20 periods on each side, centred on the crest x0 = pi/(2 beta)
x0 = np.pi / (2 * beta)
Lw = 20 * np.pi / beta


def E_sheets(x, centre):
    fr = lambda xp: rho0 * np.sin(beta * xp)
    left = quad(fr, centre - Lw, x, limit=4000, epsabs=1e-22, epsrel=1e-10)[0]
    right = quad(fr, x, centre + Lw, limit=4000, epsabs=1e-22, epsrel=1e-10)[0]
    return (left - right) / (2 * eps_si)


for xx in [0.0, 0.3, x0, -x0, 1.0, np.pi / beta]:
    print(f"   x = {xx:+.4f} m: E by sheets = {E_sheets(xx, x0):+.6f} V/m, closed form = {Ecl(xx, 0):+.6f} V/m")
print(f"   (trap: a window centred on the node x = 0 (10 periods each side) gives E(0) = {E_sheets(0.0, 0.0):+.4f} V/m instead of -2;"
      " the truncated slab's dipole layer adds a uniform field -- hence the symmetry argument)")
chk("(b) E_x(0,0) by sheet superposition [V/m]", E_sheets(0.0, x0), "-2")
chk("(a) E_x on the crest plane by sheets [V/m]", E_sheets(x0, x0), "0", tol=1e-6)
chk("(a) E_x on the trough plane by sheets [V/m]", E_sheets(-x0, x0), "0", tol=1e-6)
chk("(a) |E_x| at the node x = pi/beta by sheets [V/m]", abs(E_sheets(np.pi / beta, x0)), "2")
xt, tt, h, k = 0.37, 0.4 * tr_si, 1e-5, 1e-3 * tr_si
dEdx = (Ecl(xt + h, tt) - Ecl(xt - h, tt)) / (2 * h)
drdt = (rcl(xt, tt + k) - rcl(xt, tt - k)) / (2 * k)
chk_true("(a) closed forms satisfy Gauss (FD, rel. residual < 1e-6):",
         abs(dEdx - rcl(xt, tt) / eps_si) / abs(rcl(xt, tt) / eps_si) < 1e-6)
chk_true("(a) closed forms satisfy continuity with J = sigma E (FD):", abs(drdt + sig_si * dEdx) / abs(drdt) < 1e-6)
# method of lines: E from the sheet-sum matrix, d rho/dt = -sigma dE/dx by central differences
M, K = 128, 10
P = 2 * np.pi / beta                                          # period of sin(beta x)
dx = P / M
xg = np.arange(M) * dx
ms = np.arange(M // 4 - K * M, M // 4 + K * M + 1)           # x0 = P/4: window [x0 - K P, x0 + K P], trapezoid
wts = np.ones(ms.size)
wts[0] = wts[-1] = 0.5
G = np.zeros((M, M))
for i in range(M):
    np.add.at(G[i], ms % M, wts * np.sign(xg[i] - ms * dx) * dx / (2 * eps_si))
D = np.zeros((M, M))
for i in range(M):
    D[i, (i + 1) % M], D[i, (i - 1) % M] = 1 / (2 * dx), -1 / (2 * dx)
r_init = rho0 * np.sin(beta * xg)
print(f"   max |E_matrix - closed form| at t = 0: {np.max(np.abs(G @ r_init - Ecl(xg, 0))):.2e} V/m")
mol = solve_ivp(lambda tt_, r: -sig_si * D @ (G @ (r - r.mean())), [0, 2 * tr_si], r_init, method='RK45',
                rtol=1e-10, atol=1e-25, t_eval=[tr_si, 2 * tr_si])
for j, tj in enumerate(mol.t):
    err = np.max(np.abs(mol.y[:, j] - rcl(xg, tj))) / rho0
    print(f"   PDE at t = {tj / tr_si:.0f} tau_r: max |rho_num - rho_closed|/rho0 = {err:.2e}")
amp_num = np.max(np.abs(mol.y[:, 0])) / np.max(np.abs(r_init))
chk("(a) decay time from PDE amplitude at t = tau_r [s]", -tr_si / np.log(amp_num), "5.31e-11")
J0 = sig_si * Ecl(0, 0)
v0 = J0 / (Nsi * (-e))
chk("(b) E_x(0,0) [V/m]", Ecl(0, 0), "-2")
chk("(b) J_x(0,0) [A/m^2]", J0, "-3.90")
chk("(b) v_x(0,0) = J/(N(-e)) [m/s]", v0, "0.244")
chk("(b) v_x via -(e tau/m*) E [m/s]", -mob_si * Ecl(0, 0), "0.244")
chk("(b) crest at pi/(2 beta) [m]", x0, "0.785")
chk_true("(b) J at x = 0 along -x, from the crest (x = +pi/4, rho > 0) to the trough (x = -pi/4, rho < 0):",
         J0 < 0 and rcl(x0, 0) > 0 and rcl(-x0, 0) < 0)
chk_true("(b) electrons at x = 0 drift along +x (toward the crest):", v0 > 0)
chk("(b) rho0/e [m^-3]", rho0 / e, "2.6e9")
# constants check: CODATA values change nothing at the quoted precision
e2, me2, ep2 = 1.602176634e-19, 9.1093837015e-31, 8.8541878128e-12
s2 = 1e20 * e2 ** 2 * 1.8e-13 / (0.26 * me2)
print(f"   CODATA: sigma = {s2:.5g} S/m, tau_r = {11.7 * ep2 / s2:.5g} s, v = {2 * e2 * 1.8e-13 / (0.26 * me2):.5g} m/s,"
      f" J = {2 * s2:.5g} A/m^2")

print("--- (c) ---")
chk("(c) copper tau_r = eps0/sigma [s]", tr_c, "1.5e-19")
chk("(c) copper tau_r, 3 s.f. [s]", tr_c, "1.53e-19")
chk("(c) copper tau [s]", tau_c, "2.4e-14")
chk("(c) tau/tau_r copper", tau_c / tr_c, "1.6e5")
chk("(c) tau_r/tau silicon", tr_si / tsi, "295")

print("--- (d) eigenvalues of the modal state matrix (rho_hat, J_hat) ---")


def modal(sig, eps, tau, b):
    # rho = rh sin(bx), J_x = Jh cos(bx), E_x = -rh/(b eps) cos(bx):
    # continuity d rh/dt = b Jh ; Drude tau dJh/dt + Jh = sigma E_hat
    return np.array([[0.0, b], [-sig / (b * eps * tau), -1.0 / tau]])


cases = {"copper": (sc, eps0, tau_c), "sea water": (4.0, 81 * eps0, 1.5e-14), "silicon": (sig_si, eps_si, tsi)}
ev = {}
for name, (sig, eps, tau) in cases.items():
    ev[name] = np.sort_complex(np.linalg.eigvals(modal(sig, eps, tau, 2.0)))
    ev7 = np.sort_complex(np.linalg.eigvals(modal(sig, eps, tau, 7.0)))
    print(f"   {name}: s = {ev[name]} (beta = 2); beta = 7 gives the same: {np.allclose(ev[name], ev7, rtol=1e-9)}")
    chk_true(f"   {name}: roots independent of beta:", np.allclose(ev[name], ev7, rtol=1e-9))
wp2c = sc / (eps0 * tau_c)
chk("copper sigma/(eps0 tau) = omega_p^2 [1/s^2]", wp2c, "2.705e32")
chk("copper N e^2/(m eps0) [1/s^2]", Nc * e ** 2 / (me * eps0), "2.705e32")
print(f"   (page had 2.71e32; with CODATA constants it is {8.5e28 * 1.602176634e-19 ** 2 / (9.1093837015e-31 * 8.8541878128e-12):.5g}, so 2.705e32 is safe either way)")
chk("copper omega_p [rad/s]", np.sqrt(wp2c), "1.64e16")
chk("copper 4 sigma tau/eps0", 4 * sc * tau_c / eps0, "6.3e5")
chk("copper Re s [1/s]", ev["copper"][0].real, "-2.06e13")
chk("copper |Im s| [rad/s]", abs(ev["copper"][0].imag), "1.64e16")
chk("copper f_p [Hz]", np.sqrt(wp2c) / 2 / np.pi, "2.6e15")
chk("copper 2 tau [s]", 2 * tau_c, "4.8e-14")
chk("copper oscillations per 2 tau", abs(ev["copper"][0].imag) / 2 / np.pi * 2 * tau_c, "127")
chk("copper omega_p tau", np.sqrt(wp2c) * tau_c, "398")
ssw, esw, tsw = cases["sea water"]
chk("sea sigma/eps [1/s]", ssw / esw, "5.58e9")
chk("sea 1/tau [1/s]", 1 / tsw, "6.67e13")
chk("sea 4 sigma tau/eps", 4 * ssw * tsw / esw, "3.3e-4")
chk("sea s1 [1/s]", ev["sea water"][0].real, "-6.67e13")
chk("sea s2 [1/s]", ev["sea water"][1].real, "-5.58e9")
chk("sea 1/|s2| [s]", 1 / abs(ev["sea water"][1]), "1.79e-10")
chk("sea eps/sigma [ns]", esw / ssw * 1e9, "0.18")
chk("sea |1/|s2| - eps/sigma|/(eps/sigma) (1/|s2| is the shorter)", abs((1 / abs(ev["sea water"][1])) / (esw / ssw) - 1), "8.4e-5")
chk("sea 4 tau [s]", 4 * tsw, "6e-14")
chk("copper 4 tau [s]", 4 * tau_c, "9.69e-14")
chk("silicon 4 tau [s]", 4 * tsi, "7.2e-13")
print(f"   silicon 4 tau/tau_r = {4 * tsi / tr_si:.4g} (< 1: overdamped)")
chk_true("silicon overdamped (real roots):", np.all(np.abs(ev["silicon"].imag) == 0))
chk("silicon slow-root time constant [s]", 1 / abs(ev["silicon"][1]), "5.29e-11")
chk("silicon: below tau_r by [%]", (1 - (1 / abs(ev["silicon"][1])) / tr_si) * 100, "0.34")

print("--- (d) time-domain simulation of the Drude relaxation (t' = t/tau, u = rho/rho0) ---")
for name, (sig, eps, tau) in cases.items():
    a = sig * tau / eps
    if name == "copper":
        tp = np.linspace(0, 6, 300001)
        so = solve_ivp(lambda _t, y: [y[1], -a * y[0] - y[1]], [0, 6], [1.0, 0.0], method='DOP853',
                       rtol=1e-11, atol=1e-14, t_eval=tp)
        u = so.y[0]
        zc = np.where(np.sign(u[:-1]) != np.sign(u[1:]))[0]
        tz = tp[zc] - u[zc] * (tp[zc + 1] - tp[zc]) / (u[zc + 1] - u[zc])
        wsim = np.pi / np.mean(np.diff(tz)) / tau
        pk = np.where((u[1:-1] > u[:-2]) & (u[1:-1] > u[2:]))[0] + 1
        slope = np.polyfit(tp[pk], np.log(u[pk]), 1)[0]
        chk("copper: simulated oscillation [rad/s]", wsim, "1.64e16")
        chk("copper: simulated envelope time constant [s]", -tau / slope, "4.8e-14")
    else:
        tend = 4e4 if name == "sea water" else 1500.0
        tp = np.linspace(0.3 * tend, 0.8 * tend, 50)
        so = solve_ivp(lambda _t, y: [y[1], -a * y[0] - y[1]], [0, tend], [1.0, 0.0], method='Radau',
                       rtol=1e-12, atol=1e-16, t_eval=tp)
        slope = np.polyfit(tp, np.log(so.y[0]), 1)[0]
        tc = -tau / slope
        chk(f"{name}: simulated late-time decay constant [s]", tc, "1.79e-10" if name == "sea water" else "5.29e-11")
        print(f"   {name}: simulated tau_slow / (eps/sigma) - 1 = {tc / (eps / sig) - 1:+.3e}")

print(f"\nTOTAL: {NPASS} PASS, {NFAIL} FAIL")
