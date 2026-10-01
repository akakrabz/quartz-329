#!/usr/bin/env python3
"""Numerical checks for practice/11-lorentz-drude-models.md (Lecture 11: Lorentz-Drude models).

numpy/scipy only. Every number that appears in an answer on the page is printed here.
Symbolic results are checked against brute-force computations (ODE integration of the
Drude and Lorentz equations, finite differences, Monte Carlo counting, root finding)
at two or more parameter sets.
"""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq, curve_fit

eps0 = 8.8541878128e-12
mu0 = 4e-7 * np.pi
e = 1.602176634e-19
me = 9.1093837e-31
c = 2.99792458e8

rng = np.random.default_rng(329)
FAIL = []


def hdr(s):
    print("\n" + "=" * 78 + "\n" + s + "\n" + "=" * 78)


def check(name, got, want, rtol=1e-6, atol=0.0):
    ok = np.allclose(got, want, rtol=rtol, atol=atol)
    print(f"  [{'ok' if ok else 'FAIL'}] {name}: got {got!r}  expected {want!r}")
    if not ok:
        FAIL.append(name)
    return ok


def drude_step(q, m, tau, E0, n_tau=40.0):
    """Integrate m dv/dt = qE0 - m v/tau from v(0)=0 in the scaled time s = t/tau.
    Returns (t array [s], v array [m/s])."""
    vscale = abs(q) * tau * E0 / m
    sol = solve_ivp(lambda s, y: [np.sign(q) * 1.0 - y[0]], (0, n_tau), [0.0],
                    rtol=1e-11, atol=1e-14, dense_output=True)
    s = np.linspace(0, n_tau, 400001)
    return s * tau, sol.sol(s)[0] * vscale


def crossing_time(t, v, frac):
    """First time at which |v| reaches frac*|v_final| (linear interpolation)."""
    vf = v[-1]
    idx = np.argmax(np.abs(v) >= frac * abs(vf))
    t0, t1, v0, v1 = t[idx - 1], t[idx], abs(v[idx - 1]), abs(v[idx])
    return t0 + (frac * abs(vf) - v0) * (t1 - t0) / (v1 - v0)


# ----------------------------------------------------------------------------------------
hdr("Constants")
print(f"eps0 = {eps0:.4g} F/m, e = {e:.4g} C, m_e = {me:.4g} kg, c = {c:.4g} m/s   (page values)")
e2_over_m_eps0 = e**2 / (me * eps0)
print(f"e^2/(m_e eps0) = {e2_over_m_eps0:.6g} m^3/s^2   (page: about 3.18e3)")
print(f"N e for copper (N = 8.5e28): {8.5e28 * e:.6g} C/m^3")

# ----------------------------------------------------------------------------------------
hdr("11.1 Drift speed in a house wire")
N_cu = 8.5e28
A = 1.5e-6        # m^2
I = 10.0          # A
J = I / A
print(f"A = 1.5 mm^2 = {A:.2g} m^2")
v = J / (N_cu * e)
t1m = 1.0 / v
print(f"J = I/A = {J:.6g} A/m^2   (page 6.67e6 A/m^2)")
print(f"|v| = J/(N e) = {v:.6g} m/s = {v*1e3:.4g} mm/s   (page 4.9e-4 m/s, 0.49 mm/s)")
print(f"electron velocity direction: v = J/(N q) with q = -e  ->  sign(v.J) = {np.sign(1/(N_cu*(-e)))}  (opposite to I)")
print(f"time to drift 1 m: {t1m:.6g} s = {t1m/60:.4g} min   (page 2.0e3 s, about 34 min)")
# Monte Carlo brute force of J = N q v with zero-mean random (thermal) velocities on top of the drift.
for (vd, sth, M) in [(v, 5 * v, 1_000_000), (2.5 * v, 3 * 2.5 * v, 2_000_000)]:
    L = 1e-3; Abox = 1e-6                     # periodic box: length L along x, cross-section Abox
    Nbox = M / (L * Abox)                      # number density represented by the M particles
    q = -e
    x0 = rng.uniform(0, L, M)
    u = vd + sth * rng.standard_normal(M)      # u = drift + random part (delta v)
    dt = L / vd
    net = np.floor((x0 + u * dt) / L) - np.floor(x0 / L)   # signed crossings of the plane x = 0 (mod L)
    J_mc = q * net.sum() / (Abox * dt)
    J_th = Nbox * q * vd
    rel = abs(J_mc / J_th - 1)
    print(f"  Monte Carlo J = {J_mc:.5g}, N q v = {J_th:.5g}, rel. diff {rel:.2%} (statistical)")
    if rel > 0.02:
        FAIL.append("11.1 Monte Carlo")

# ----------------------------------------------------------------------------------------
hdr("11.2 Conductivity of aluminum from collisions")
N_al = 1.8e29
tau_al = 7.5e-15
sig_al = N_al * e**2 * tau_al / me
mu_al = e * tau_al / me
v_al = mu_al * 0.1
print(f"sigma = N e^2 tau / m_e = {sig_al:.6g} S/m   (page 3.8e7 S/m)")
print(f"mobility = e tau / m_e = {mu_al:.6g} m^2/(V s)   (page 1.32e-3)")
print(f"drift at E = 0.1 V/m: {v_al:.6g} m/s   (page 1.32e-4 m/s, against E)")
check("sigma = N e mu", N_al * e * mu_al, sig_al)
# copper comparison numbers used in the solution (lecture example: sigma = 5.96e7)
mu_cu_lect = 5.96e7 / (N_cu * e)
print(f"copper mobility (lecture example, sigma = 5.96e7): {mu_cu_lect:.4g} m^2/(V s)   (page 4.4e-3)")
print(f"N_Al/N_Cu = {N_al/N_cu:.4g} (page 'twice'),  mu_Cu/mu_Al = {mu_cu_lect/mu_al:.4g} (page 'a third')")
# brute force: integrate the Drude ODE for an electron in E = 0.1 x V/m
t, vv = drude_step(-e, me, tau_al, 0.1)
print(f"ODE: final drift = {vv[-1]:.6g} m/s (negative: against E); formula -mu E = {-v_al:.6g}")
check("11.2 ODE steady drift", vv[-1], -v_al, rtol=1e-4)
t63 = crossing_time(t, vv, 1 - np.exp(-1))
check("11.2 ODE 63% time equals tau", t63, tau_al, rtol=1e-4)

# ----------------------------------------------------------------------------------------
hdr("11.3 Which change doubles the conductivity (multiple choice)")
def sigma(N, q, m, nu):
    return N * q**2 / (m * nu)
base = dict(N=8.5e28, q=-e, m=me, nu=4.1e13)
s0 = sigma(**base)
opts = {
    "(a) double E (sigma does not contain E)": s0,
    "(b) double |q|": sigma(base["N"], 2 * base["q"], base["m"], base["nu"]),
    "(c) halve nu": sigma(base["N"], base["q"], base["m"], base["nu"] / 2),
    "(d) double m": sigma(base["N"], base["q"], 2 * base["m"], base["nu"]),
    "(e) q -> -q": sigma(base["N"], -base["q"], base["m"], base["nu"]),
}
for k, val in opts.items():
    print(f"  {k}: sigma/sigma0 = {val/s0:.6g}")
# (a) via the force balance: doubling E doubles v and J, ratio J/E unchanged
for Efield in (1.0, 2.0):
    vdr = base["q"] * Efield / (base["m"] * base["nu"])
    Jx = base["N"] * base["q"] * vdr
    print(f"  E = {Efield}: v = {vdr:.4g} m/s, J = {Jx:.4g} A/m^2, J/E = {Jx/Efield:.6g} S/m")
# (e) direction: J along E for either sign of q
for qq in (e, -e):
    vdr = qq * 1.0 / (me * 4.1e13)
    print(f"  q = {qq:+.3g}: v_x = {vdr:+.3g}, J_x = N q v_x = {base['N']*qq*vdr:+.4g} (always +)")

# ----------------------------------------------------------------------------------------
hdr("11.4 True or false")
# (i) Lorentz oscillator, static E: integrate m r'' = -eE - m w0^2 r - 2 m alpha r' (scaled units)
for (w0, alpha, E0) in [(1.0, 0.05, 1.0), (2.0, 0.2, -3.0)]:
    # units: m = 1, e = 1; steady state r = -E0/w0^2
    sol = solve_ivp(lambda t, y: [y[1], -E0 - w0**2 * y[0] - 2 * alpha * y[1]], (0, 400 / alpha),
                    [0.0, 0.0], rtol=1e-10, atol=1e-13)
    r_end = sol.y[0, -1]
    print(f"  (i) w0={w0}, alpha={alpha}, E={E0}: r_ss = {r_end:.6g}, -eE/(m w0^2) = {-E0/w0**2:.6g}, "
          f"sign(r*E) = {np.sign(r_end*E0):+.0f} (antiparallel), p = -e r has sign(p*E) = {np.sign(-r_end*E0):+.0f}")
    check("11.4(i) Lorentz static r", r_end, -E0 / w0**2, rtol=1e-6)
# (ii) perfect dielectric: J_p = dP/dt nonzero for time-varying E, zero for constant E
chi = 2.0; w = 2 * np.pi * 50.0; E0 = 100.0
tt = np.linspace(0, 0.04, 40001)
P = eps0 * chi * E0 * np.cos(w * tt)
Jp = np.gradient(P, tt)
print(f"  (ii) max |dP/dt| for E0 cos(wt): {np.max(np.abs(Jp)):.5g} A/m^2 vs w eps0 chi E0 = {w*eps0*chi*E0:.5g}")
check("11.4(ii) J_p amplitude", np.max(np.abs(Jp)), w * eps0 * chi * E0, rtol=1e-4)
Pc = eps0 * chi * E0 * np.ones_like(tt)
print(f"  (ii) constant E: max |dP/dt| = {np.max(np.abs(np.gradient(Pc, tt))):.3g}")
# (iii) chi_e for N_d = 5e28, w0 = 2e16
chi_iii = 5e28 * e2_over_m_eps0 / (2e16)**2
print(f"  (iii) chi_e = {chi_iii:.6g} (page 0.40), eps_r = 1 + chi_e = {1+chi_iii:.6g} (page 1.40)")
# (iv) copper: Drude tau vs eps0/sigma
sig_cu = 5.8e7
tau_cu = sig_cu * me / (N_cu * e**2)
taur_cu = eps0 / sig_cu
print(f"  (iv) copper (sigma=5.8e7, N=8.5e28): Drude tau = {tau_cu:.6g} s (page 2.4e-14), "
      f"eps0/sigma = {taur_cu:.6g} s (page 1.5e-19), ratio = {tau_cu/taur_cu:.4g} (page 'about 10^5')")
# (v) copper at 10 GHz with nu = 4e13
x = 2 * np.pi * 1e10 / 4e13
dev = abs(1 / (1 + 1j * x) - 1)
print(f"  (v) w/nu at 10 GHz = {x:.6g} (page 1.6e-3); |sigma(w)/sigma_DC - 1| = {dev:.6g} (page 0.16%)")

# ----------------------------------------------------------------------------------------
hdr("11.5 Sea water's two ions (find the error)")
Ni = 3.0e26
mup, mum = 4.0e-8, 6.0e-8
mp, mm = 3.8e-26, 5.9e-26
sig_student = Ni * e * (mup - mum)
sig_sw = Ni * e * (mup + mum)
print(f"N = 3.0e26 m^-3 is {Ni/6.02214076e23/1000:.4g} mol/L")
print(f"mu+ + mu- = {mup+mum:.2g} m^2/(V s); mu+ - mu- = {mup-mum:.2g} m^2/(V s)")
print(f"student: sigma = N e (mu+ - mu-) = {sig_student:.6g} S/m   (page -0.96 S/m)")
print(f"correct: sigma = N e (mu+ + mu-) = {sig_sw:.6g} S/m   (page 4.8 S/m)")
print(f"fractions: Na+ {mup/(mup+mum):.4g}, Cl- {mum/(mup+mum):.4g}   (page 40%, 60%)")
print(f"species conductivities: Na+ {Ni*e*mup:.5g} S/m, Cl- {Ni*e*mum:.5g} S/m")
# brute force with signed charges and signed velocities from each ion's force balance
Evec = np.array([1.0, 0.0, 0.0])
taup = mup * mp / e
taum = mum * mm / e
Jtot = np.zeros(3)
for (q, m, tau) in [(+e, mp, taup), (-e, mm, taum)]:
    vel = q * tau / m * Evec          # steady state of m dv/dt = qE - m v/tau
    Js = Ni * q * vel
    print(f"  q = {q:+.4g}: v = {vel} m/s, J_s = {Js} A/m^2")
    Jtot += Js
check("11.5 J_x/E_x = N e (mu+ + mu-)", Jtot[0], sig_sw, rtol=1e-12)
print(f"tau(Na+) = mu m / e = {taup:.6g} s (page 9.5e-15), nu = {1/taup:.6g} s^-1 (page 1.05e14)")
print(f"tau(Cl-) = mu m / e = {taum:.6g} s (page 2.2e-14), nu = {1/taum:.6g} s^-1 (page 4.5e13)")
check("sigma_+ via N q^2/(m nu)", Ni * e**2 / (mp * (1 / taup)), Ni * e * mup)
check("sigma_- via N q^2/(m nu)", Ni * e**2 / (mm * (1 / taum)), Ni * e * mum)
for nm, tau in (("Na+", taup), ("Cl-", taum)):
    x = 2 * np.pi * 1e10 * tau
    print(f"  {nm}: w/nu at 10 GHz = {x:.4g} (page: below 1.4e-3)")
# power check: J.E >= 0 for the corrected sigma, < 0 for the student's
print(f"J.E per (V/m)^2: student {sig_student:.3g} (negative -> would generate power), correct {sig_sw:.3g}")

# ----------------------------------------------------------------------------------------
hdr("11.6 A conductor as a low-pass filter (n-type silicon)")
Nsi = 1.0e22
mstar = 0.26 * me
tau_si = 1.8e-13
nu_si = 1 / tau_si
mu_si = e * tau_si / mstar
sDC = Nsi * e**2 * tau_si / mstar
print(f"m* = {mstar:.6g} kg")
print(f"mobility = e tau/m* = {mu_si:.6g} m^2/(V s)   (page 0.122 = 1220 cm^2/(V s))")
print(f"sigma_DC = N e^2 tau/m* = {sDC:.6g} S/m   (page 195 S/m)")
check("sigma_DC = N e mu", Nsi * e * mu_si, sDC)
# (a) step response via ODE, two parameter sets
t99_formula = tau_si * np.log(100)
print(f"(a) 99% time = tau ln 100 = {np.log(100):.6g} tau = {t99_formula:.6g} s   (page 4.6 tau = 8.3e-13 s)")
for (q, m, tau, E0) in [(-e, mstar, tau_si, 1.0), (-e, me, 2.4e-14, 50.0)]:
    t, vv = drude_step(q, m, tau, E0)
    # compare to analytic v(t) = (q tau E0/m)(1 - exp(-t/tau))
    va = q * tau * E0 / m * (1 - np.exp(-t / tau))
    err = np.max(np.abs(vv - va)) / abs(va[-1])
    t99 = crossing_time(t, vv, 0.99)
    print(f"  ODE (tau={tau:.3g}): max rel err vs analytic {err:.2e}; final v = {vv[-1]:.6g}; "
          f"t99 = {t99:.6g} s = {t99/tau:.6g} tau")
    if err > 1e-6:
        FAIL.append("11.6 step response")
    check("11.6 t99/tau = ln 100", t99 / tau, np.log(100), rtol=1e-4)
# (c) AC at w = nu
w = nu_si
sig_w = Nsi * e**2 / (mstar * (nu_si + 1j * w))
print(f"(c) w = nu = {w:.6g} rad/s, f = {w/(2*np.pi):.6g} Hz   (page 5.56e12 rad/s, 0.88 THz)")
print(f"    sigma(w) = {sig_w.real:.6g} {sig_w.imag:+.6g} j S/m   (page 97.5(1 - j))")
print(f"    |sigma| = {abs(sig_w):.6g} S/m (page 138), phase = {np.degrees(np.angle(sig_w)):.6g} deg (page -45)")
T = 2 * np.pi / w
print(f"    period T = {T:.6g} s, lag T/8 = {T/8:.6g} s = (pi/4) tau = {np.pi/4*tau_si:.6g} s   (page 1.4e-13 s)")
check("|sigma| = sigma_DC/sqrt2", abs(sig_w), sDC / np.sqrt(2))
# brute force: drive the Drude ODE with E0 cos(wt) to steady state, fit J(t)
for (tau, wfac) in [(tau_si, 1.0), (tau_si, 0.3), (2.4e-14, 2.0)]:
    ww = wfac / tau
    E0 = 1.0
    sDC_here = Nsi * e**2 * tau / mstar
    # scaled time s = t/tau; dv/ds = (q tau E0/m) cos(wfac s) - v ; J = N q v
    sol = solve_ivp(lambda s, y: [(-e * tau * E0 / mstar) * np.cos(wfac * s) - y[0]], (0, 60),
                    [0.0], rtol=1e-11, atol=1e-16, dense_output=True)
    s = np.linspace(40, 60, 20001)
    Jt = Nsi * (-e) * sol.sol(s)[0]
    Mx = np.column_stack([np.cos(wfac * s), np.sin(wfac * s)])
    a, b = np.linalg.lstsq(Mx, Jt, rcond=None)[0]
    amp = np.hypot(a, b); ph = np.degrees(np.arctan2(-b, a))   # J = amp cos(wt + ph)
    sig_pred = sDC_here / (1 + 1j * wfac)
    print(f"  ODE w/nu = {wfac}: J amp = {amp:.6g} (pred {abs(sig_pred):.6g}), phase = {ph:.5g} deg "
          f"(pred {np.degrees(np.angle(sig_pred)):.5g})")
    check(f"11.6 AC amplitude w/nu={wfac}", amp, abs(sig_pred), rtol=1e-5)
    check(f"11.6 AC phase w/nu={wfac}", ph, np.degrees(np.angle(sig_pred)), rtol=0, atol=1e-3)
# (d) frequency limit for 1% complex deviation
xlim = brentq(lambda x: x / np.sqrt(1 + x**2) - 0.01, 1e-6, 1)
print(f"(d) x = w/nu at 1%: {xlim:.8g}")
f_si = xlim * nu_si / (2 * np.pi)
f_cu = xlim * 4.1e13 / (2 * np.pi)
print(f"    silicon: f_max = {f_si:.6g} Hz   (page 8.8 GHz)")
print(f"    copper (nu = 4.1e13): f_max = {f_cu:.6g} Hz   (page 65 GHz)")
print(f"    at that point |sigma|/sigma_DC = {1/np.sqrt(1+xlim**2):.8g} (page within 0.005%), "
      f"phase = {-np.degrees(np.arctan(xlim)):.4g} deg (page -0.57)")
# direct check of the deviation at f_si
sig_f = sDC / (1 + 1j * 2 * np.pi * f_si / nu_si)
print(f"    |sigma(f_max) - sigma_DC|/sigma_DC = {abs(sig_f - sDC)/sDC:.6g}")
print(f"    copper nu from sigma=5.8e7, N=8.5e28: {1/tau_cu:.6g} s^-1 (page 4.1e13)")

# ----------------------------------------------------------------------------------------
hdr("11.7 Conductor-like or dielectric-like")
# (a) brute force: finite-difference dP/dt and compare amplitude/phase with the formula
for (sig, chi_, f) in [(4.0, 80.0, 1e9), (1e-12, 1.27, 0.05), (2e-3, 9.0, 3e6)]:
    w = 2 * np.pi * f
    E0 = 2.0
    tt = np.linspace(0, 5 / f, 200001)
    E = E0 * np.cos(w * tt)
    Jc = sig * E
    Jp = np.gradient(eps0 * chi_ * E, tt)
    # fit Jp = a cos + b sin
    Mx = np.column_stack([np.cos(w * tt), np.sin(w * tt)])
    a, b = np.linalg.lstsq(Mx[5:-5], Jp[5:-5], rcond=None)[0]
    ampp = np.hypot(a, b); php = np.degrees(np.arctan2(-b, a))
    print(f"  sigma={sig}, chi={chi_}, f={f:g}: |Jp| = {ampp:.6g} (w eps0 chi E0 = {w*eps0*chi_*E0:.6g}), "
          f"phase of Jp = {php:.4f} deg (+90 = leads), |Jp|/|Jc| = {ampp/(sig*E0):.6g} "
          f"vs w eps0 chi/sigma = {w*eps0*chi_/sig:.6g}")
    check("11.7(a) J_p amplitude", ampp, w * eps0 * chi_ * E0, rtol=1e-5)
    check("11.7(a) J_p phase +90", php, 90.0, rtol=0, atol=1e-3)
# (b) glass via the Lorentz model
Nd, w0 = 4.0e28, 1.0e16
chi_g = Nd * e2_over_m_eps0 / w0**2
epsr_g = 1 + chi_g
sig_g = 1.0e-12
fx_g = sig_g / (2 * np.pi * eps0 * chi_g)
print(f"(b) Nd e^2/(m eps0) = {Nd*e2_over_m_eps0:.6g} s^-2 (page 1.273e32)")
print(f"    glass chi_e = {chi_g:.6g} (page 1.27), eps_r = {epsr_g:.6g} (page 2.27), sqrt(eps_r) = {np.sqrt(epsr_g):.4g} (page 1.51)")
print(f"    lambda_0 = 2 pi c / w0 = {2*np.pi*c/w0*1e9:.4g} nm (page about 190 nm, ultraviolet)")
print(f"    f_x = sigma/(2 pi eps0 chi) = {fx_g:.6g} Hz (page 0.014 Hz)")
print(f"    ratio at 60 Hz = {60/fx_g:.6g} (page 4.2e3)")
print(f"    w0/(2 pi) = {w0/(2*np.pi):.4g} Hz  >> 60 Hz (DC chi valid)")
# brute-force chi from the Lorentz ODE at low frequency (scaled: time in 1/w0, alpha = 0.01 w0)
for (wfac, alpha) in [(1e-2, 0.01), (3e-3, 0.05)]:
    # r'' = -(e/m)E/w0^2... in scaled units: d2r/ds2 = -E(s) - r - 2 a dr/ds, with r in units of e E0/(m w0^2)
    sol = solve_ivp(lambda s, y: [y[1], -np.cos(wfac * s) - y[0] - 2 * alpha * y[1]],
                    (0, 3 * 2 * np.pi / wfac), [0.0, 0.0], rtol=1e-10, atol=1e-12, dense_output=True,
                    max_step=0.5)
    s = np.linspace(2 * 2 * np.pi / wfac, 3 * 2 * np.pi / wfac, 40001)
    r = sol.sol(s)[0]
    Mx = np.column_stack([np.cos(wfac * s), np.sin(wfac * s)])
    a, b = np.linalg.lstsq(Mx, r, rcond=None)[0]
    pred = -1 / (1 - wfac**2 + 2j * alpha * wfac)
    print(f"  Lorentz ODE w/w0={wfac}: r amp (units eE0/(m w0^2)) = {np.hypot(a,b):.6g}, in-phase coeff {a:.6g} "
          f"(DC model: -1, AC model: {pred.real:.6g})")
    check(f"11.7 Lorentz r tracks -eE/(m w0^2) at w/w0={wfac}", a, pred.real, rtol=1e-4)
# (c) sea water
sig_sw2, epsr_sw = 4.0, 81.0
chi_sw = epsr_sw - 1
fx_sw = sig_sw2 / (2 * np.pi * eps0 * chi_sw)
print(f"(c) sea water chi_e = eps_r - 1 = {chi_sw:g}")
print(f"(c) sea water f_x = {fx_sw:.6g} Hz (page 0.90 GHz)")
for f in (20e3, 10e9):
    r = 2 * np.pi * f * eps0 * chi_sw / sig_sw2
    print(f"    f = {f:g} Hz: |Jp|/|Jc| = {r:.6g}, |Jc|/|Jp| = {1/r:.6g}   (page 2.2e-5 / 4.5e4 at 20 kHz, 11 at 10 GHz)")
# ions' collision frequency vs 10 GHz
print(f"    ion nu ~ {1/taup:.3g}, {1/taum:.3g} s^-1; w(10 GHz)/nu <= {2*np.pi*1e10*taum:.3g}")
# (d) relaxation times and the capacitor crossover
for nm, sig, epsr, chi_, fx in (("sea water", sig_sw2, epsr_sw, chi_sw, fx_sw), ("glass", sig_g, epsr_g, chi_g, fx_g)):
    taur = epsr * eps0 / sig
    fr = 1 / (2 * np.pi * taur)
    print(f"(d) {nm}: tau_r = eps/sigma = {taur:.6g} s, f_r = 1/(2 pi tau_r) = {fr:.6g} Hz, "
          f"f_x/f_r = {fx/fr:.6g} = eps_r/chi_e = {epsr/chi_:.6g}, vacuum share 1/eps_r = {1/epsr:.4g}")
    # brute force: parallel plate with arbitrary A, d; |C dv/dt| / |G v| at f_r via finite differences
    for (Ap, dp) in [(1e-2, 1e-3), (3e-4, 2e-2)]:
        C = epsr * eps0 * Ap / dp
        G = sig * Ap / dp
        tt = np.linspace(0, 3 / fr, 300001)
        vt = 5.0 * np.cos(2 * np.pi * fr * tt)
        iC = C * np.gradient(vt, tt)
        iG = G * vt
        print(f"     A={Ap}, d={dp}: G/C = {G/C:.6g} = sigma/eps = {sig/(epsr*eps0):.6g}; "
              f"max|C dv/dt| / max|G v| at f_r = {np.max(np.abs(iC[5:-5]))/np.max(np.abs(iG)):.6f}")
        if abs(np.max(np.abs(iC[5:-5])) / np.max(np.abs(iG)) - 1) > 1e-4:
            FAIL.append("11.7(d) capacitor crossover")

# ----------------------------------------------------------------------------------------
hdr("11.8 Relaxation time versus collision time")
# (a),(b) symbolic: rho = rho0 cos(beta x) e^{-sigma t/eps0}, E_x = rho0/(beta eps0) sin(beta x) e^{-sigma t/eps0}
def rho_f(x, t, rho0, beta, sig, eps):
    return rho0 * np.cos(beta * x) * np.exp(-sig * t / eps)
def Ex_f(x, t, rho0, beta, sig, eps):
    return rho0 / (beta * eps) * np.sin(beta * x) * np.exp(-sig * t / eps)
for (rho0, beta, sig, eps) in [(6 * eps0, 3.0, 1e-9, eps0), (2e-6, 1.7, 3e-10, 2.5 * eps0)]:
    taur = eps / sig
    for _ in range(3):
        x = rng.uniform(-2, 2); t = rng.uniform(0, 2) * taur
        hx = 1e-6; ht = 1e-6 * taur
        dEdx = (Ex_f(x + hx, t, rho0, beta, sig, eps) - Ex_f(x - hx, t, rho0, beta, sig, eps)) / (2 * hx)
        gauss = dEdx - rho_f(x, t, rho0, beta, sig, eps) / eps
        drdt = (rho_f(x, t + ht, rho0, beta, sig, eps) - rho_f(x, t - ht, rho0, beta, sig, eps)) / (2 * ht)
        dJdx = sig * dEdx
        cont = drdt + dJdx
        scale = abs(rho0) / taur
        print(f"  rho0={rho0:.3g}, beta={beta}, x={x:.3f}, t/tau_r={t/taur:.3f}: Gauss residual "
              f"{gauss*eps/abs(rho0):.2e}, continuity residual {cont/scale:.2e}")
        if abs(gauss * eps / abs(rho0)) > 1e-6 or abs(cont / scale) > 1e-6:
            FAIL.append("11.8 (a)/(b) residual")
    # zero-mean field: E_x is odd in x
    print(f"  E_x(-0.3)+E_x(0.3) = {Ex_f(-0.3,0,rho0,beta,sig,eps)+Ex_f(0.3,0,rho0,beta,sig,eps):.2e} (odd in x)")
print(f"(b) page numbers: rho0/(beta eps0) = 6 eps0/(3 eps0) = {6/3:.6g} V/m amplitude")
print(f"    E_x(0.1 m, 0) = 2 sin(0.3) = {2*np.sin(0.3):.6g} V/m > 0  ->  current along +x at x = 0.1 m")
print(f"    trough of rho at x = pi/3 = {np.pi/3:.6g} m")
# (c) copper numbers
print(f"(c) copper: tau_r = eps0/sigma = {taur_cu:.6g} s (page 1.5e-19), Drude tau = {tau_cu:.6g} s (page 2.4e-14), "
      f"ratio tau/tau_r = {tau_cu/taur_cu:.6g} (page 1.6e5)")
# (d) second-order equation: s^2 + s/tau + sigma/(eps tau) = 0
def roots(sig, eps, tau):
    return np.roots([1.0, 1.0 / tau, sig / (eps * tau)])
rc = roots(sig_cu, eps0, tau_cu)
wp2 = sig_cu / (eps0 * tau_cu)
wp = np.sqrt(wp2)
print(f"(d) copper: sigma/(eps0 tau) = {wp2:.6g} s^-2 = N e^2/(m eps0) = {N_cu*e2_over_m_eps0:.6g}")
print(f"    omega_p = {wp:.6g} rad/s (page 1.64e16), f_p = {wp/(2*np.pi):.6g} Hz (page 2.6e15), "
      f"lambda = c/f_p = {c/(wp/(2*np.pi))*1e9:.4g} nm (ultraviolet)")
print(f"    1/(2 tau) = {1/(2*tau_cu):.6g} s^-1 (page 2.1e13), 2 tau = {2*tau_cu:.6g} s (page 4.8e-14)")
print(f"    roots: {rc[0]:.6g}, {rc[1]:.6g}")
print(f"    damped frequency sqrt(wp^2 - 1/(4 tau^2)) = {np.sqrt(wp2 - 1/(4*tau_cu**2)):.6g} rad/s")
print(f"    4 sigma tau/eps0 = {4*sig_cu*tau_cu/eps0:.4g} (>> 1: underdamped); oscillations per 2tau: "
      f"{wp/(2*np.pi)*2*tau_cu:.4g} (page about 130); omega_p tau = {wp*tau_cu:.4g}")
check("copper roots real part -1/(2 tau)", rc[0].real, -1 / (2 * tau_cu))
tau_sw = 1.5e-14
eps_sw = 81 * eps0
rs = np.sort(roots(4.0, eps_sw, tau_sw).real)
print(f"    sea water: roots = {rs[0]:.6g}, {rs[1]:.6g} s^-1 (page -6.7e13 and -5.6e9); sigma/eps = {4.0/eps_sw:.6g}, "
      f"1/tau = {1/tau_sw:.6g}")
print(f"    slow time constant 1/|s1| = {1/abs(rs[1]):.6g} s vs eps/sigma = {eps_sw/4.0:.6g} s (page 0.18 ns); "
      f"rel diff {abs(1/abs(rs[1])/(eps_sw/4.0)-1):.3g}")
print(f"    4 sigma tau/eps = {4*4.0*tau_sw/eps_sw:.4g} (<< 1: overdamped); eps/sigma = {eps_sw/4.0:.4g} vs 4 tau = {4*tau_sw:.3g}")
print(f"    copper: eps0/sigma = {taur_cu:.3g} vs 4 tau = {4*tau_cu:.3g}")
# limit tau -> 0 recovers -sigma/eps
for tau_small in (1e-16, 1e-18):
    r_ = np.sort(roots(4.0, eps_sw, tau_small).real)
    print(f"    tau = {tau_small:g}: slow root {r_[1]:.8g} vs -sigma/eps = {-4.0/eps_sw:.8g}")
# brute force: integrate the coupled mode equations (continuity + Drude + Gauss) for one Fourier mode
#   rho = R(t) cos(beta x), E_x = R/(beta eps) sin(beta x), J_x = Q(t) sin(beta x)
#   continuity: R' + beta Q = 0 ;  Drude: Q' = (sigma/tau) R/(beta eps) - Q/tau
def mode_run(sig, eps, tau, beta, R0, t_end, npts=400001):
    f = lambda t, y: [-beta * y[1], (sig / tau) * y[0] / (beta * eps) - y[1] / tau]
    sol = solve_ivp(f, (0, t_end), [R0, 0.0], method="DOP853", rtol=1e-11, atol=1e-30,
                    dense_output=True, max_step=t_end / 2e5)
    t = np.linspace(0, t_end, npts)
    return t, sol.sol(t)[0]
# copper: fit R(t) = A e^{-g t} cos(w t + phi)
t, R = mode_run(sig_cu, eps0, tau_cu, 3.0, 6 * eps0, 3 * tau_cu)
model = lambda t, A, g, w, ph: A * np.exp(-g * t) * np.cos(w * t + ph)
p, _ = curve_fit(model, t, R / (6 * eps0), p0=[1.0, 1 / (2 * tau_cu), wp, 0.0], maxfev=20000)
print(f"  copper mode ODE fit: decay rate {p[1]:.6g} (pred {1/(2*tau_cu):.6g}), angular freq {abs(p[2]):.6g} "
      f"(pred {np.sqrt(wp2-1/(4*tau_cu**2)):.6g})")
check("11.8 copper decay rate", p[1], 1 / (2 * tau_cu), rtol=1e-4)
check("11.8 copper oscillation", abs(p[2]), np.sqrt(wp2 - 1 / (4 * tau_cu**2)), rtol=1e-6)
# sea water: slow decay rate from the late-time log slope
t, R = mode_run(4.0, eps_sw, tau_sw, 3.0, 1.0, 5 * eps_sw / 4.0)
sel = t > 1e3 * tau_sw
slope = np.polyfit(t[sel], np.log(R[sel]), 1)[0]
print(f"  sea water mode ODE: late-time decay rate {slope:.6g} s^-1 (pred slow root {rs[1]:.6g}, sigma/eps {-4.0/eps_sw:.6g})")
check("11.8 sea water slow decay", slope, rs[1], rtol=1e-5)
# second parameter set (different beta must not matter)
t, R = mode_run(4.0, eps_sw, tau_sw, 0.4, 1.0, 5 * eps_sw / 4.0)
slope2 = np.polyfit(t[t > 1e3 * tau_sw], np.log(R[t > 1e3 * tau_sw]), 1)[0]
check("11.8 sea water slow decay independent of beta", slope2, rs[1], rtol=1e-5)

# ----------------------------------------------------------------------------------------
hdr("Summary")
print("All checks passed." if not FAIL else f"FAILED: {FAIL}")
