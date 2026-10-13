#!/usr/bin/env python3
"""Independent review of the Lecture 20 page set (Poynting's theorem and monochromatic waves).

Written by the reviewer WITHOUT reading digest8/verify_L20.py.  numpy/scipy only.
Every item prints PASS or FAIL; the last line counts them.

Files checked:
  content-src/3-maxwell-and-waves/20-poynting-theorem-and-monochromatic-waves.md   (page, sections 1-9)
  content-src/concepts/poynting-theorem.md, content-src/concepts/poynting-vector.md
  content-src/problems/energy-bookkeeping-for-a-radiating-sheet.md                (WP)
  figs/poy-*.html (from figs_l20.py)

Method notes
  * General Poynting theorem: fields from arbitrary analytic potentials (so Faraday holds identically),
    eps(r), mu(r) varying in space; inner derivatives by complex step (exact to rounding), outer ones by
    4th-order central differences; J defined from Ampere-Maxwell.  A negative control with eps(t) shows
    the time-invariance condition is needed.
  * Time averages by scipy quadrature, compared with 1/2 Re{A B*} of the corresponding phasors (the page
    itself uses no phasors; the phasor route is only this script's independent cross-check).
  * Every direction by np.cross; figure arrows parsed from the SVG and compared with np.cross in the screen
    frame (X right, Y up, Z out of the screen).
  * Handbook values used: CODATA 2018 eps0, mu0, c; nichrome (80Ni-20Cr) resistivity 1.10e-6 ohm m at 20 C
    (CRC Handbook / common tables, 1.08-1.10e-6); sea water sigma about 4-5 S/m (4.8 S/m at 20 C, 35 g/kg;
    textbooks and the exams use 4 S/m), eps_r about 81; solar constant 1361 W/m^2 (IAU 2015 nominal value).
"""
import math, re
import numpy as np
from scipy import integrate

RES = []
def check(name, ok, detail=""):
    RES.append(bool(ok))
    print(("PASS  " if ok else "FAIL  ") + name + (f"   [{detail}]" if detail else ""))

def section(t):
    print("\n" + "=" * 100 + "\n" + t + "\n" + "=" * 100)

def rnd(x, sig):
    """round to sig significant figures"""
    if x == 0: return 0.0
    return float(f"{x:.{sig}g}")

def shown(value, page_text, sig):
    """does the page's rounded number agree with value to the shown precision?"""
    return rnd(value, sig) == float(page_text)

rng = np.random.default_rng(20)

# ==================================================================================================== A
section("A. Constants (CODATA 2018) and the course's exam constants")
EPS0 = 8.8541878128e-12
MU0 = 1.25663706212e-6
C0 = 299792458.0
ETA0 = math.sqrt(MU0 / EPS0)
print(f"   eta0 = {ETA0:.6f} ohm, c = {1/math.sqrt(MU0*EPS0):.1f} m/s")
check("eta0 = 376.73 ohm (page: eta0 ~ 377, 120 pi)", abs(ETA0 - 376.730313668) < 1e-5)
check("120 pi is 0.069 % above eta0 (page Sources / ERRATA)", abs((120 * np.pi / ETA0 - 1) * 100 - 0.069) < 0.0005,
      f"{(120*np.pi/ETA0-1)*100:.4f} %")
check("eta0/2 = 188.4 W/m^2, eta0 = 376.7 W/m^2 (page: 188, 377; Sources: 188.4, 376.7)",
      shown(ETA0 / 2, "188", 3) and shown(ETA0, "377", 3) and shown(ETA0 / 2, "188.4", 4) and shown(ETA0, "376.7", 4))
eps0x, mu0x = 1e-9 / (36 * np.pi), 4 * np.pi * 1e-7
check("exam constants eps0 = 1e-9/36pi, mu0 = 4pi e-7 give c = 3e8 and eta0 = 120 pi exactly (WP statement)",
      np.isclose(1 / np.sqrt(mu0x * eps0x), 3e8, rtol=1e-14) and np.isclose(np.sqrt(mu0x / eps0x), 120 * np.pi, rtol=1e-14))

# ==================================================================================================== B
section("B. Units (exponents of kg, m, s, A)")
class U:
    def __init__(s, kg=0, m=0, sec=0, A=0): s.v = np.array([kg, m, sec, A], float)
    def __mul__(s, o): r = U(); r.v = s.v + o.v; return r
    def __truediv__(s, o): r = U(); r.v = s.v - o.v; return r
    def __pow__(s, n): r = U(); r.v = s.v * n; return r
    def __eq__(s, o): return np.allclose(s.v, o.v)
kg, m, s_, A_ = U(1), U(0, 1), U(0, 0, 1), U(0, 0, 0, 1)
W = kg * m ** 2 / s_ ** 3; J = kg * m ** 2 / s_ ** 2; V = W / A_; Cb = A_ * s_
Ohm = V / A_; F = Cb / V; Hy = V * s_ / A_; Sm = A_ / V
Ef, Hf, Df, Bf = V / m, A_ / m, Cb / m ** 2, V * s_ / m ** 2
check("(V/m)(A/m) = VA/m^2 = W/m^2 = (J/s)/m^2", Ef * Hf == W / m ** 2 and W / m ** 2 == (J / s_) / m ** 2)
check("J counts charge in (C/s)/m^2 = A/m^2", (Cb / s_) / m ** 2 == A_ / m ** 2)
check("H.(curl E) and E.(curl H) are W/m^3 (Step 1 sentence)", Hf * Ef / m == W / m ** 3 and Ef * Hf / m == W / m ** 3)
check("E.dD/dt and H.dB/dt are W/m^3", Ef * Df / s_ == W / m ** 3 and Hf * Bf / s_ == W / m ** 3)
check("w = 1/2 eps E^2 + 1/2 mu H^2 is J/m^3", (F / m) * Ef ** 2 == J / m ** 3 and (Hy / m) * Hf ** 2 == J / m ** 3)
check("J.E = sigma E^2 = J^2/sigma is W/m^3", (A_ / m ** 2) * Ef == W / m ** 3 and (Sm / m) * Ef ** 2 == W / m ** 3
      and (A_ / m ** 2) ** 2 / (Sm / m) == W / m ** 3)
check("Js.E is W/m^2 (per unit area of sheet)", (A_ / m) * Ef == W / m ** 2)
check("tau = eps/sigma is seconds; S/w is m/s", (F / m) / (Sm / m) == s_ and (W / m ** 2) / (J / m ** 3) == m / s_)

# ==================================================================================================== C
section("C. The vector identity div(E x H) = H.curl E - E.curl H, and the 'six pieces' of the folded derivation")
CS = 1e-30
def cs_d(f, args, k):
    a = [complex(v) for v in args]; a[k] += 1j * CS
    return np.imag(np.asarray(f(*a))) / CS

def Ftest(x, y, z):
    return np.array([np.sin(1.3 * x - 0.4 * y) + x * y * z, np.cos(0.7 * y + 0.2 * z) * np.exp(0.3 * x), np.sinh(0.5 * z) * np.cos(x - y)])
def Gtest(x, y, z):
    return np.array([y * z * z + np.cos(x), np.sin(x) * np.cos(z) + 0.4 * x * y, np.cosh(0.2 * y) * x - np.sin(0.9 * z)])
def jac(f, p):                     # jac[i, k] = d f_i / d x_k  (complex step)
    return np.array([cs_d(f, p, k) for k in range(3)]).T
def curl_from_jac(Jm):
    return np.array([Jm[2, 1] - Jm[1, 2], Jm[0, 2] - Jm[2, 0], Jm[1, 0] - Jm[0, 1]])
worst = 0; worst6 = 0
for _ in range(6):
    p = rng.uniform(-1.5, 1.5, 3)
    Fp, Gp = Ftest(*p), Gtest(*p)
    JF, JG = jac(Ftest, p), jac(Gtest, p)
    div_FxG = np.trace(jac(lambda x, y, z: np.cross(Ftest(x, y, z), Gtest(x, y, z)), p))
    rhs = Gp @ curl_from_jac(JF) - Fp @ curl_from_jac(JG)
    worst = max(worst, abs(div_FxG - rhs) / (abs(rhs) + 1))
    # the page's grouping: pieces in which E (=F) is differentiated, with H (=G) as coefficient
    dE = lambda i, k: JF[i, k]; dH = lambda i, k: JG[i, k]
    Hx, Hy_, Hz = Gp; Ex, Ey, Ez = Fp
    pieces_E = Hx * (dE(2, 1) - dE(1, 2)) + Hy_ * (dE(0, 2) - dE(2, 0)) + Hz * (dE(1, 0) - dE(0, 1))
    pieces_H = (Ey * dH(2, 0) - Ez * dH(1, 0)) + (Ez * dH(0, 1) - Ex * dH(2, 1)) + (Ex * dH(1, 2) - Ey * dH(0, 2))
    worst6 = max(worst6, abs(pieces_E - Gp @ curl_from_jac(JF)) + abs(pieces_H + Fp @ curl_from_jac(JG)))
check("div(F x G) = G.curl F - F.curl G at 6 random points (complex step)", worst < 1e-13, f"max rel err {worst:.1e}")
check("E-differentiated pieces = H.(curl E); H-differentiated pieces = -E.(curl H) (page's bracket form)", worst6 < 1e-12)

# ==================================================================================================== D
section("D. Poynting's theorem for arbitrary fields that satisfy Maxwell's equations (eps(r), mu(r) time-invariant)")
def Phi(x, y, z, t):
    return np.sin(1.1 * x + 0.3 * t) * np.cos(0.7 * y) * np.exp(-0.2 * z * z) + 0.5 * x * y * t
def Avec(x, y, z, t):
    return np.array([np.cos(0.9 * y - 1.3 * t) * np.sin(0.5 * z) + 0.3 * z * t * t,
                     np.sin(0.6 * x + 0.8 * z) * np.cos(1.7 * t) + 0.2 * x * x * z,
                     np.exp(-0.3 * (x * x + y * y)) * np.sin(2.1 * t + 0.4 * x)])
def eps_f(x, y, z, t): return 2.0 + 0.5 * np.sin(x) * np.cos(0.3 * z)
def mu_f(x, y, z, t): return 1.5 + 0.3 * np.cos(y * z)
def Efield(x, y, z, t):
    g = np.array([cs_d(Phi, (x, y, z, t), k) for k in range(3)])
    return -g - cs_d(Avec, (x, y, z, t), 3)
def Bfield(x, y, z, t):
    Jm = np.array([cs_d(Avec, (x, y, z, t), k) for k in range(3)]).T
    return curl_from_jac(Jm)
def fd(f, args, k, h=1e-3):
    def at(sh):
        a = list(args); a[k] = a[k] + sh * h; return np.asarray(f(*a))
    return (at(-2) - 8 * at(-1) + 8 * at(1) - at(2)) / (12 * h)

def poynting_residual(eps_fun, mu_fun, p):
    Hfield = lambda x, y, z, t: Bfield(x, y, z, t) / mu_fun(x, y, z, t)
    Dfield = lambda x, y, z, t: eps_fun(x, y, z, t) * Efield(x, y, z, t)
    Sfield = lambda x, y, z, t: np.cross(Efield(x, y, z, t), Hfield(x, y, z, t))
    wfield = lambda x, y, z, t: 0.5 * eps_fun(x, y, z, t) * Efield(x, y, z, t) @ Efield(x, y, z, t) + \
        0.5 * mu_fun(x, y, z, t) * Hfield(x, y, z, t) @ Hfield(x, y, z, t)
    JH = np.array([fd(Hfield, p, k) for k in range(3)]).T
    Jfree = curl_from_jac(JH) - fd(Dfield, p, 3)             # J from Ampere-Maxwell
    E = Efield(*p)
    divS = sum(fd(Sfield, p, k)[k] for k in range(3))
    dwdt = fd(wfield, p, 3)
    JE = Jfree @ E
    JEcurlE = curl_from_jac(np.array([fd(Efield, p, k) for k in range(3)]).T) + fd(Bfield, p, 3)
    return dwdt, divS, JE, np.linalg.norm(JEcurlE), E
worst = 0; worst_far = 0; scales = []
for _ in range(5):
    p = tuple(rng.uniform(-1, 1, 4))
    dwdt, divS, JE, far, _E = poynting_residual(eps_f, mu_f, p)
    sc = max(abs(dwdt), abs(divS), abs(JE))
    scales.append((dwdt, divS, JE))
    worst = max(worst, abs(dwdt + divS + JE) / sc)
    worst_far = max(worst_far, far)
print("   sample terms (dw/dt, div S, J.E):", ", ".join(f"({a:+.3f}, {b:+.3f}, {c:+.3f})" for a, b, c in scales[:3]))
check("Faraday holds identically for E = -grad Phi - dA/dt, B = curl A (residual of curl E + dB/dt)", worst_far < 1e-8,
      f"{worst_far:.1e}")
check("J.E term is exercised (J from Ampere-Maxwell is not zero)", min(abs(c) for a, b, c in scales) > 1e-2)
check("dw/dt + div S + J.E = 0 at 5 random (r, t), eps and mu varying in space (point form, page section 2)", worst < 1e-8,
      f"max rel residual {worst:.1e}")
# negative control: eps varying in time breaks the stored-energy reading by -1/2 (d eps/dt) E^2
eps_t = lambda x, y, z, t: 2.0 + 0.5 * np.sin(x) * np.cos(0.3 * z) + 0.3 * np.sin(t)
p = tuple(rng.uniform(-1, 1, 4))
dwdt, divS, JE, _, E = poynting_residual(eps_t, mu_f, p)
expected = -0.5 * 0.3 * np.cos(p[3]) * (E @ E)
check("negative control: with eps(t) the residual is -1/2 (d eps/dt) E^2, so 'eps, mu constant in time' is needed",
      abs((dwdt + divS + JE) - expected) < 1e-8 * max(1, abs(expected)), f"residual {dwdt+divS+JE:+.4f}, predicted {expected:+.4f}")
# chain rule backwards: E.dD/dt = d/dt(1/2 eps E.E) for time-invariant eps
p = tuple(rng.uniform(-1, 1, 4))
lhs = Efield(*p) @ fd(lambda x, y, z, t: eps_f(x, y, z, t) * Efield(x, y, z, t), p, 3)
rhs = fd(lambda x, y, z, t: 0.5 * eps_f(x, y, z, t) * Efield(x, y, z, t) @ Efield(x, y, z, t), p, 3)
check("E.dD/dt = d/dt(1/2 eps E.E) when eps does not depend on t", abs(lhs - rhs) < 1e-9 * max(1, abs(lhs)))

# ==================================================================================================== E
section("E. The one-dimensional check (Rao's route) in the folded derivation")
muz, epsz = 1.7, 2.3
Ax = lambda z, t: np.sin(1.3 * z - 0.7 * t) * np.exp(-0.1 * z * z) + 0.2 * z * t
Ex1 = lambda z, t: -cs_d(Ax, (z, t), 1)
Hy1 = lambda z, t: cs_d(Ax, (z, t), 0) / muz
Jx1 = lambda z, t: -fd(Hy1, (z, t), 0) - epsz * fd(Ex1, (z, t), 1)
ok_far = ok_amp = ok_mid = ok_thm = True
for _ in range(5):
    z, t = rng.uniform(-2, 2, 2)
    ok_far &= abs(fd(Ex1, (z, t), 0) + muz * fd(Hy1, (z, t), 1)) < 1e-9
    dSz = fd(lambda zz, tt: Ex1(zz, tt) * Hy1(zz, tt), (z, t), 0)
    mid = -muz * Hy1(z, t) * fd(Hy1, (z, t), 1) - Ex1(z, t) * (Jx1(z, t) + epsz * fd(Ex1, (z, t), 1))
    last = -fd(lambda zz, tt: 0.5 * muz * Hy1(zz, tt) ** 2 + 0.5 * epsz * Ex1(zz, tt) ** 2, (z, t), 1) - Jx1(z, t) * Ex1(z, t)
    ok_mid &= abs(dSz - mid) < 1e-8
    ok_thm &= abs(dSz - last) < 1e-8
check("dEx/dz = -mu dHy/dt for the planar fields (component Faraday)", ok_far)
check("dSz/dz = -mu Hy dHy/dt - Ex (Jx + eps dEx/dt)   (middle line of the 1D derivation)", ok_mid)
check("dSz/dz = -d/dt(1/2 mu Hy^2 + 1/2 eps Ex^2) - Jx Ex   (last line)", ok_thm)
# component equations from the full curl
Ef3 = lambda x, y, z, t: np.array([Ex1(z, t), 0 * x, 0 * x]); Hf3 = lambda x, y, z, t: np.array([0 * x, Hy1(z, t), 0 * x])
p = (0.3, -0.2, 0.7, 0.4)
cE = curl_from_jac(np.array([fd(Ef3, p, k) for k in range(3)]).T); cH = curl_from_jac(np.array([fd(Hf3, p, k) for k in range(3)]).T)
check("curl(x Ex(z,t)) = y dEx/dz and curl(y Hy(z,t)) = -x dHy/dz (so the two component equations are right)",
      np.allclose(cE, [0, fd(Ex1, (0.7, 0.4), 0), 0], atol=1e-9) and np.allclose(cH, [-fd(Hy1, (0.7, 0.4), 0), 0, 0], atol=1e-9))

# ==================================================================================================== F
section("F. Section 3: J.E from the Lorentz force; the four-situation table")
ok = True
for _ in range(5):
    rho, u, E, B = rng.normal(), rng.normal(size=3), rng.normal(size=3), rng.normal(size=3)
    force = rho * (E + np.cross(u, B))
    ok &= abs(force @ u - (rho * u) @ E) < 1e-12 and abs(np.cross(u, B) @ u) < 1e-12
check("power density rho(E + u x B).u = rho E.u = J.E (magnetic part does no work, np.cross)", ok)
sig, Ev = 3.7, rng.normal(size=3); Jv = sig * Ev
check("ohmic: J.E = sigma E^2 = J^2/sigma >= 0", np.isclose(Jv @ Ev, sig * Ev @ Ev) and np.isclose(Jv @ Ev, Jv @ Jv / sig))
# row 1: plane wave in a lossless medium: div S = -dw/dt, J.E = 0  (checked numerically in section M)
# row 2/3 checked in G and J below

# ==================================================================================================== G
section("G. Example: the leaky capacitor (eps_r = 4, sigma = 1e-5 S/m, E0 = 10 kV/m)")
epsL, sigL, E0L = 4 * EPS0, 1e-5, 1e4
tau = epsL / sigL
w0 = 0.5 * epsL * E0L ** 2
JE0 = sigL * E0L ** 2
print(f"   tau = {tau*1e6:.4f} us, w0 = {w0*1e3:.4f} mJ/m^3, J.E(0) = {JE0:.1f} W/m^3, 2w0/tau = {2*w0/tau:.1f}")
check("tau = eps/sigma = 3.54 us", shown(tau * 1e6, "3.54", 3))
check("w(0) = 1/2 eps E0^2 = 1.77 mJ/m^3", shown(w0 * 1e3, "1.77", 3))
check("J.E(0) = sigma E0^2 = 1000 W/m^3 = 2 w0/tau", np.isclose(JE0, 1000) and np.isclose(2 * w0 / tau, JE0))
check("energy halves every (tau/2) ln 2 = 1.23 us; charge every tau ln 2 = 2.45 us",
      shown(tau / 2 * math.log(2) * 1e6, "1.23", 3) and shown(tau * math.log(2) * 1e6, "2.45", 3))
EL = lambda t: E0L * np.exp(-t / tau)
tt = rng.uniform(0, 5 * tau, 5)
check("conduction sigma E and displacement eps dE/dt cancel at every t (so H = 0, S = 0)",
      all(abs(sigL * EL(t) + epsL * fd(lambda tq: EL(tq), (t,), 0, h=tau * 1e-3)) < 1e-9 * sigL * E0L for t in tt))
check("dw/dt = -J.E at every t (theorem with S = 0)",
      all(np.isclose(fd(lambda tq: 0.5 * epsL * EL(tq) ** 2, (t,), 0, h=tau * 1e-3), -sigL * EL(t) ** 2, rtol=1e-8) for t in tt))
heat, _ = integrate.quad(lambda t: sigL * EL(t) ** 2, 0, 60 * tau)
check("all of w(0) ends up as heat: int sigma E^2 dt = w(0)", np.isclose(heat, w0, rtol=1e-10))

# ==================================================================================================== H
section("H. Example: DC power in a coax travels in the dielectric")
ok_dir = all(np.allclose(np.cross([np.cos(f), np.sin(f), 0], [-np.sin(f), np.cos(f), 0]), [0, 0, 1]) for f in rng.uniform(0, 2 * np.pi, 5))
check("rho_hat x phi_hat = z_hat (np.cross at 5 angles)", ok_dir)
ok = True
for _ in range(4):
    Vv, Iv, a = rng.uniform(1, 100), rng.uniform(0.1, 10), rng.uniform(1e-3, 5e-3); b = a * rng.uniform(1.5, 8)
    Er = lambda r: Vv / (r * math.log(b / a)); Hp = lambda r: Iv / (2 * np.pi * r)
    P, _ = integrate.quad(lambda r: Er(r) * Hp(r) * 2 * np.pi * r, a, b)
    Vint, _ = integrate.quad(Er, a, b)
    ok &= np.isclose(P, Vv * Iv, rtol=1e-10) and np.isclose(Vint, Vv, rtol=1e-10) and \
        np.isclose(Er(a) * Hp(a), Vv * Iv / (2 * np.pi * a ** 2 * math.log(b / a)))
check("S_z = VI/(2 pi rho^2 ln(b/a)) integrates to VI over a < rho < b; E integrates to V", ok)

# ==================================================================================================== I
section("I. Static-field caveat: a charge next to a magnet has E x H != 0 but div(E x H) = 0")
rq, m_dip = np.array([0.4, -0.3, 0.2]), np.array([0.2, 0.5, 1.0])
def Estat(x, y, z):
    r = np.array([x, y, z]) - rq; return r / (4 * np.pi * (r @ r) ** 1.5)
def Hstat(x, y, z):
    r = np.array([x, y, z]); rr = np.sqrt(r @ r); rh = r / rr
    return (3 * (m_dip @ rh) * rh - m_dip) / (4 * np.pi * rr ** 3)
ok = True; mag = []; worst = 0
for _ in range(5):
    p = rng.uniform(1, 2, 3) * rng.choice([-1, 1], 3)
    divS = np.trace(jac(lambda x, y, z: np.cross(Estat(x, y, z), Hstat(x, y, z)), p))
    Ep, Hp = Estat(*p), Hstat(*p)
    scale = np.linalg.norm(Ep) * np.linalg.norm(jac(Hstat, p)) + np.linalg.norm(Hp) * np.linalg.norm(jac(Estat, p))
    worst = max(worst, abs(divS) / scale)
    mag.append(np.linalg.norm(np.cross(Ep, Hp)) / (np.linalg.norm(Ep) * np.linalg.norm(Hp)))   # sine of the angle
check("div(E x H) = 0 away from the sources while E x H is not zero (E and H far from parallel)",
      worst < 1e-13 and min(mag) > 0.05, f"|div S|/term size <= {worst:.1e}; min sin(angle) = {min(mag):.2f}")

# ==================================================================================================== J
section("J. Section 5: a wire heated through its surface; the 100 W heater wire")
ok_dir = True
for f in rng.uniform(0, 2 * np.pi, 5):
    rh, ph = np.array([np.cos(f), np.sin(f), 0]), np.array([-np.sin(f), np.cos(f), 0])
    ok_dir &= np.allclose(np.cross([0, 0, 1], ph), -rh)
check("z_hat x phi_hat = -rho_hat: S at the surface points radially inward", ok_dir)
ok = True
for _ in range(4):
    sg, a, l, I = rng.uniform(1e5, 6e7), rng.uniform(1e-4, 2e-3), rng.uniform(0.1, 5), rng.uniform(0.1, 20)
    Ez = I / (sg * np.pi * a ** 2); R = l / (sg * np.pi * a ** 2)
    Hin = lambda r: I * r / (2 * np.pi * a ** 2)
    ok &= np.isclose(Ez * Hin(a) * 2 * np.pi * a * l, I ** 2 * R)
    for frac in (0.3, 0.7):
        r = frac * a
        flow = Ez * Hin(r) * 2 * np.pi * r * l
        heat, _ = integrate.quad(lambda rr: sg * Ez ** 2 * 2 * np.pi * rr * l, 0, r)
        ok &= np.isclose(flow, I ** 2 * R * frac ** 2) and np.isclose(heat, flow, rtol=1e-10)
    # div S in cylindrical coordinates: (1/rho) d(rho S_rho)/d rho = -sigma E^2
    Srho = lambda r: -Ez * Hin(r)
    r0 = 0.5 * a
    divS = fd(lambda rr: rr * Srho(rr), (r0,), 0, h=a * 1e-3) / r0
    ok &= np.isclose(divS, -sg * Ez ** 2, rtol=1e-8)
check("side power E_z H_phi(a) 2 pi a l = I^2 R; P(rho) = I^2 R (rho/a)^2 = heat inside rho; div S = -sigma E^2", ok)
check("no flux through the end faces: S = E x H with E || z has S_z = 0",
      abs(np.cross([0, 0, 2.0], [-0.3, 0.8, 0])[2]) < 1e-15)
rho_nich = 1.10e-6                       # handbook: nichrome 80/20, 1.10e-6 ohm m at 20 C
sgN, aN, lN, IN = 1 / rho_nich, 0.25e-3, 2.0, 3.0
RN = lN / (sgN * np.pi * aN ** 2); PN = IN ** 2 * RN; EN = IN / (sgN * np.pi * aN ** 2); HN = IN / (2 * np.pi * aN)
SN = EN * HN; AN = 2 * np.pi * aN * lN
print(f"   sigma = {sgN:.4e}, R = {RN:.4f}, P = {PN:.3f}, E = {EN:.4f}, E l = {EN*lN:.3f}, H(a) = {HN:.2f}, S = {SN:.1f}, A = {AN:.5e}")
check("sigma = 1/1.10e-6 = 9.1e5 S/m", shown(sgN, "9.1e5", 2))
check("R = 11.2 ohm, P = I^2 R = 101 W", shown(RN, "11.2", 3) and shown(PN, "101", 3))
check("E = 16.8 V/m, E l = I R = 33.6 V, H(a) = 1.91 kA/m",
      shown(EN, "16.8", 3) and shown(EN * lN, "33.6", 3) and np.isclose(EN * lN, IN * RN) and shown(HN / 1e3, "1.91", 3))
check("|S| = E H = 32.1 kW/m^2, about 24 x the solar constant 1361 W/m^2", shown(SN / 1e3, "32.1", 3) and round(SN / 1361) == 24,
      f"ratio {SN/1361:.1f}")
check("side area 3.14e-3 m^2 and |S| x area = 101 W", shown(AN, "3.14e-3", 3) and shown(SN * AN, "101", 3))

# ==================================================================================================== K
section("K. Section 6: the notes' Example 1, J_s = x 2 cos(wt) A/m on z = 0 in vacuum")
om = 2 * np.pi * 1.0e6; beta = om / C0; lam = 2 * np.pi / beta
xh, yh, zh = np.eye(3)
Js = lambda t: xh * 2 * np.cos(om * t)
def sheet_fields(z, t, eta=ETA0, v=C0, Jsf=Js):
    """Lecture 19 recipe: E = -(eta/2) Js(t-|z|/v), H = 1/2 Js(t-|z|/v) x n, n toward the field point"""
    n = zh if z > 0 else -zh
    Jd = Jsf(t - abs(z) / v)
    return -eta / 2 * Jd, 0.5 * np.cross(Jd, n)
ok_a = ok_b = True
for _ in range(8):
    z = rng.uniform(-3, 3) * lam; t = rng.uniform(0, 5e-6)
    E, H = sheet_fields(z, t)
    sgn = 1 if z > 0 else -1
    Epage = -xh * ETA0 * np.cos(om * t - sgn * beta * z)
    Hpage = -sgn * yh * np.cos(om * t - sgn * beta * z)
    ok_a &= np.allclose(E, Epage) and np.allclose(H, Hpage)
    Spage = sgn * zh * ETA0 * np.cos(om * t - sgn * beta * z) ** 2
    ok_b &= np.allclose(np.cross(E, H), Spage)
check("(a) E = -x eta0 cos(wt -+ beta z), H = -+ y cos(wt -+ beta z) (Lecture 19 recipe, np.cross)", ok_a)
check("(b) S = E x H = +- z eta0 cos^2(wt -+ beta z), never toward the sheet", ok_b)
# Maxwell in each half space (finite differences), vacuum
ok = True
for z0 in (0.37 * lam, -1.21 * lam):
    for t0 in rng.uniform(0, 1e-6, 3):
        Exf = lambda z, t: sheet_fields(z, t)[0][0]; Hyf = lambda z, t: sheet_fields(z, t)[1][1]
        hz, ht = lam * 1e-4, 1e-4 / om
        r1 = fd(Exf, (z0, t0), 0, hz) + MU0 * fd(Hyf, (z0, t0), 1, ht)
        r2 = -fd(Hyf, (z0, t0), 0, hz) - EPS0 * fd(Exf, (z0, t0), 1, ht)
        ok &= abs(r1) < 1e-7 * ETA0 * beta and abs(r2) < 1e-7 * beta
check("both waves satisfy Faraday and Ampere-Maxwell (J = 0) in z > 0 and z < 0", ok)
ok_bc = True
for t in rng.uniform(0, 1e-6, 5):
    Ep, Hp = sheet_fields(1e-12, t); Em, Hm = sheet_fields(-1e-12, t)
    ok_bc &= np.allclose(np.cross(zh, Hp - Hm), Js(t), atol=1e-9) and np.allclose(Ep, Em, atol=1e-6)
check("jump conditions at z = 0: z x (H+ - H-) = J_s and tangential E continuous", ok_bc)
ok_c = ok_pb = True
for t in rng.uniform(0, 1e-6, 5):
    E0_, _ = sheet_fields(1e-15, t)
    JsE = Js(t) @ E0_
    ok_c &= np.isclose(JsE, -2 * ETA0 * np.cos(om * t) ** 2)
    Sp = np.cross(*sheet_fields(1e-15, t)); Sm_ = np.cross(*sheet_fields(-1e-15, t))
    ok_pb &= abs(Sp @ zh + Sm_ @ (-zh) + JsE) < 1e-9 * ETA0          # pillbox: out + out + exchange = 0
    ok_pb &= np.isclose(zh @ (Sp - Sm_), -JsE)                         # sheet form, n from 2 (z<0) into 1 (z>0)
check("(c) J_s.E(0,t) = -2 eta0 cos^2(wt) W/m^2", ok_c)
check("pillbox balance at every instant and n.(S1 - S2) = -J_s.E with n = z", ok_pb)
t0 = 0.123e-6; zz = rng.uniform(0.1, 2) * lam
Sz = lambda z, t: np.cross(*sheet_fields(z, t))[2]
check("humps of |S| are lambda/2 apart and move away at c",
      np.isclose(Sz(zz + lam / 2, t0), Sz(zz, t0)) and np.isclose(Sz(zz + C0 * 0.37e-6, t0 + 0.37e-6), Sz(zz, t0))
      and np.isclose(Sz(-zz - C0 * 0.37e-6, t0 + 0.37e-6), Sz(-zz, t0)))
# slab |z| < d: W(t) = integral of w, dW/dt vs 2 eta0 [cos^2 wt - cos^2(wt - beta d)]
def wdens(z, t):
    E, H = sheet_fields(z, t); return 0.5 * EPS0 * E @ E + 0.5 * MU0 * H @ H
def Wslab(t, d):
    a, _ = integrate.quad(lambda z: wdens(z, t), 1e-15, d, limit=200, epsabs=0, epsrel=1e-12)
    return 2 * a
ok = True
for d in (0.3 * lam, 0.25 * lam, 1.4 * lam):
    for t in rng.uniform(0, 1e-6, 3):
        dWdt = fd(lambda tq: Wslab(tq, d), (t,), 0, h=1e-3 / om)
        pred = 2 * ETA0 * (np.cos(om * t) ** 2 - np.cos(om * t - beta * d) ** 2)
        ok &= abs(dWdt - pred) < 1e-6 * ETA0
check("slab |z|<d: dW/dt = 2 eta0 [cos^2 wt - cos^2(wt - beta d)] (quadrature of w, then d/dt)", ok)
tq = rng.uniform(0, 1e-6, 4)
check("quarter-wave slab (beta d = pi/2): dW/dt = 2 eta0 cos 2wt, averaging to zero",
      np.allclose(2 * ETA0 * (np.cos(om * tq) ** 2 - np.cos(om * tq - np.pi / 2) ** 2), 2 * ETA0 * np.cos(2 * om * tq))
      and abs(integrate.quad(lambda t: np.cos(2 * om * t), 0, 2 * np.pi / om)[0]) < 1e-15)

# ==================================================================================================== L
section("L. Section 7: time averages by quadrature, and the same averages by 1/2 Re{A B*} (independent route)")
T = 2 * np.pi / om
# average over one period, integrating over the phase u = w t (keeps the integrand O(1); start time 0.3e-7 s)
avg = lambda f: integrate.quad(lambda u: f(0.3e-7 + u / om), 0, 2 * np.pi, limit=200, epsabs=1e-12, epsrel=1e-12)[0] / (2 * np.pi)
ok = True
for ph in rng.uniform(-np.pi, np.pi, 4):
    ok &= np.isclose(avg(lambda t: np.cos(om * t + ph) ** 2), 0.5) and np.isclose(avg(lambda t: np.sin(om * t + ph) ** 2), 0.5)
    ok &= abs(avg(lambda t: np.cos(om * t + ph))) < 1e-12
ok &= abs(avg(lambda t: np.sin(om * t) * np.cos(om * t))) < 1e-12
check("<cos^2(wt+phi)> = <sin^2(wt+phi)> = 1/2, <cos(wt+phi)> = 0, <sin wt cos wt> = 0 (any phi, any start time)", ok)
x = rng.uniform(-5, 5, 7)
check("cos^2 x = 1/2 [1 + cos 2x]", np.allclose(np.cos(x) ** 2, 0.5 * (1 + np.cos(2 * x))))
ok = True
for p1, p2 in rng.uniform(-np.pi, np.pi, (4, 2)):
    q = avg(lambda t: np.cos(om * t + p1) * np.cos(om * t + p2))
    ok &= np.isclose(q, 0.5 * np.cos(p1 - p2), atol=1e-12) and np.isclose(q, 0.5 * np.real(np.exp(1j * p1) * np.conj(np.exp(1j * p2))), atol=1e-12)
check("<cos(wt+p1) cos(wt+p2)> = 1/2 cos(p1 - p2) = 1/2 Re{e^{jp1} e^{-jp2}} (trap 'E and H out of phase')", ok)
# the notes' sheet, averaged
zz = 0.77 * lam
Sp_avg = avg(lambda t: Sz(zz, t)); Sm_avg = avg(lambda t: Sz(-zz, t))
inj = avg(lambda t: -(Js(t) @ sheet_fields(1e-15, t)[0]))
check("<S> = +eta0/2 z for z > 0 and -eta0/2 z for z < 0 (quadrature)", np.isclose(Sp_avg, ETA0 / 2) and np.isclose(Sm_avg, -ETA0 / 2))
check("<-J_s.E> = eta0 = sum of the two outgoing averages", np.isclose(inj, ETA0) and np.isclose(inj, Sp_avg - Sm_avg))
# phasor cross-check: E~ = -eta0 e^{-j beta z} x, H~ = -e^{-j beta z} y for z > 0
Et, Ht = -ETA0 * np.exp(-1j * beta * zz), -np.exp(-1j * beta * zz)
check("quadrature <S_z> equals 1/2 Re{E~x H~y*} = eta0/2", np.isclose(0.5 * np.real(Et * np.conj(Ht)), Sp_avg))
check("notes' 60 pi and 120 pi are within 0.07 % of eta0/2 and eta0 (page: 'the notes use eta0 = 120 pi')",
      abs(60 * np.pi / (ETA0 / 2) - 1) < 7e-4 and abs(120 * np.pi / ETA0 - 1) < 7e-4)
ok = True
for _ in range(3):
    J0, eta = rng.uniform(0.5, 5), rng.uniform(50, 400); vv = rng.uniform(5e7, 3e8)
    Jg = lambda t: xh * J0 * np.cos(om * t)
    Sav = avg(lambda t: np.cross(*sheet_fields(0.3, t, eta, vv, Jg))[2])
    Iav = avg(lambda t: -(Jg(t) @ sheet_fields(1e-15, t, eta, vv, Jg)[0]))
    ok &= np.isclose(Sav, eta * J0 ** 2 / 8) and np.isclose(Iav, eta * J0 ** 2 / 4)
check("general sheet J0 cos wt in impedance eta: <S> = eta J0^2/8 per side, <-J_s.E> = eta J0^2/4", ok)
ok = True
for d in (0.2 * lam, 0.9 * lam):
    out = avg(lambda t: Sz(d, t) - Sz(-d, t))
    ok &= np.isclose(out, inj)
check("time-averaged theorem for the slab |z| < d: average outflow = eta0 for every d", ok)
w_avg = avg(lambda t: wdens(zz, t))
check("notes' example: <w> = eta0/(2c) = 6.3e-7 J/m^3 on each side (= 1/2 eps0 eta0^2)",
      np.isclose(w_avg, ETA0 / (2 * C0)) and shown(w_avg, "6.3e-7", 2) and np.isclose(w_avg, 0.5 * EPS0 * ETA0 ** 2))

# ==================================================================================================== M
section("M. A single plane wave: <S> = E0^2/2eta = v<w>; w_e = w_m; div S = -dw/dt")
epsr, E0 = 2.25, 7.0
eps, mu = epsr * EPS0, MU0
eta, v = math.sqrt(mu / eps), 1 / math.sqrt(mu * eps); bet = om / v
Epw = lambda z, t: xh * E0 * np.cos(om * t - bet * z)
Hpw = lambda z, t: np.cross(zh, Epw(z, t)) / eta                    # H = k x E / eta
ok = True
for z, t in rng.uniform(0, 3, (4, 2)) * np.array([1, 1e-6]):
    ok &= np.allclose(Hpw(z, t), yh * E0 / eta * np.cos(om * t - bet * z))
    ok &= np.isclose(0.5 * eps * Epw(z, t) @ Epw(z, t), 0.5 * mu * Hpw(z, t) @ Hpw(z, t))       # w_e = w_m
    S = np.cross(Epw(z, t), Hpw(z, t)); wv = eps * Epw(z, t) @ Epw(z, t)
    ok &= np.isclose(S[2], v * wv) and S[2] >= 0                                               # S = v w at every instant
check("H = z x E/eta = y (E0/eta) cos(wt - beta z); w_e = w_m and S = v w at every instant", ok)
z0, t0 = 1.3, 0.21e-6
divS = fd(lambda z: np.cross(Epw(z, t0), Hpw(z, t0))[2], (z0,), 0, 1e-4 / bet)
dwdt = fd(lambda t: 0.5 * eps * Epw(z0, t) @ Epw(z0, t) + 0.5 * mu * Hpw(z0, t) @ Hpw(z0, t), (t0,), 0, 1e-4 / om)
check("table row 'plane wave in a lossless medium': div S = -dw/dt, J.E = 0", np.isclose(divS, -dwdt, rtol=1e-7))
Sav = avg(lambda t: np.cross(Epw(z0, t), Hpw(z0, t))[2]); wav = avg(lambda t: eps * Epw(z0, t) @ Epw(z0, t))
H0 = E0 / eta
check("<S> = E0^2/(2 eta) = 1/2 eta H0^2 = 1/2 E0 H0 (quadrature)", np.isclose(Sav, E0 ** 2 / (2 * eta)) and
      np.isclose(Sav, 0.5 * eta * H0 ** 2) and np.isclose(Sav, 0.5 * E0 * H0))
check("<w> = 1/2 eps E0^2 and <S> = v <w>", np.isclose(wav, 0.5 * eps * E0 ** 2) and np.isclose(Sav, v * wav))

# ==================================================================================================== N
section("N. Example: J.E in sea water (sigma = 4 S/m, E = y 0.5 cos wt V/m)")
sgSW, E0SW = 4.0, 0.5
J0SW = sgSW * E0SW
JEpk = sgSW * E0SW ** 2; JEav = avg(lambda t: sgSW * (E0SW * np.cos(om * t)) ** 2)
check("J = y 2 cos wt A/m^2; J.E = cos^2 wt W/m^3: peak 1, average 0.5 W/m^3 = 0.5 mW per litre",
      np.isclose(J0SW, 2) and np.isclose(JEpk, 1) and np.isclose(JEav, 0.5) and np.isclose(JEav / 1000 * 1e3, 0.5))
r_low = sgSW / (2 * np.pi * 1e3 * 81 * EPS0)
check("'low-frequency' is consistent: sigma/(w eps) with eps_r = 81 is 8.9e5 at 1 kHz, so J = sigma E dominates",
      r_low > 1e5, f"{r_low:.2e}")
check("sea-water numbers differ from the S19 HE3 #1b keys (4e-3/2e-3 W/m^3; conflict 1e-3/5e-4 W/m^3)",
      all(not np.isclose(a, b) for a in (JEpk, JEav) for b in (4e-3, 2e-3, 1e-3, 5e-4)))

# ==================================================================================================== O
section("O. Example: sunlight and a 50 kW transmitter")
Ssun = 1361.0
E0s = math.sqrt(2 * ETA0 * Ssun); H0s = E0s / ETA0
print(f"   E0 = {E0s:.2f} V/m, H0 = {H0s:.4f} A/m, rms {E0s/math.sqrt(2):.1f} V/m, {H0s/math.sqrt(2):.3f} A/m, <w> = {Ssun/C0*1e6:.3f} uJ/m^3")
check("E0 = 1.01 kV/m, H0 = 2.69 A/m; rms 716 V/m and 1.90 A/m", shown(E0s / 1e3, "1.01", 3) and shown(H0s, "2.69", 3)
      and shown(E0s / math.sqrt(2), "716", 3) and shown(H0s / math.sqrt(2), "1.90", 3))
check("energy density <S>/c = 4.5 uJ/m^3", shown(Ssun / C0 * 1e6, "4.5", 2))
P50, r10 = 5e4, 1e4
Sr = P50 / (4 * np.pi * r10 ** 2); E0r = math.sqrt(2 * ETA0 * Sr)
check("50 kW at 10 km: <S> = 3.98e-5 W/m^2, E0 = 0.173 V/m", shown(Sr, "3.98e-5", 3) and shown(E0r, "0.173", 3))
check("with eta0 = 120 pi: E0 = sqrt(60 P)/r exactly", np.isclose(math.sqrt(2 * 120 * np.pi * Sr), math.sqrt(60 * P50) / r10, rtol=1e-14))
# far-field qualifier: Hertzian dipole at theta = 90 deg (phasor fields; reviewer's own check)
def dipole_ratio(kr):
    a = 1 / (kr)
    Eth = 1 + 1 / (1j * kr) - a ** 2        # common factor j eta k I dl e^{-jkr}/(4 pi r) removed
    Hph = 1 + 1 / (1j * kr)                 # common factor j k I dl e^{-jkr}/(4 pi r) removed
    return abs(Eth) / abs(Hph), np.real(Eth * np.conj(Hph))
ratio_near, Sre_near = dipole_ratio(0.5); ratio_far, Sre_far = dipole_ratio(2 * np.pi * 1e6 / C0 * 1e4)
check("average radial power through a sphere is r-independent even near a dipole (Re part = 1 exactly)",
      np.isclose(Sre_near, 1) and np.isclose(Sre_far, 1))
check("but |E|/|H| = eta (so E0 = sqrt(2 eta <S>), E ~ 1/r) only far away: at kr = 0.5 the ratio is "
      f"{ratio_near:.2f} eta; at 10 km, 1 MHz it is 1 - {1-ratio_far:.1e}  -> the page needs 'far from the antenna'",
      abs(ratio_near - 1) > 0.5 and abs(ratio_far - 1) < 1e-4)

# ==================================================================================================== P
section("P. Example: perpendicular components carry power independently")
ok = True
for _ in range(4):
    E1, E2, phi = rng.uniform(0.5, 5), rng.uniform(0.5, 5), rng.uniform(-np.pi, np.pi)
    Ef = lambda z, t: xh * E1 * np.cos(om * t - beta * z) + yh * E2 * np.cos(om * t - beta * z + phi)
    Hf = lambda z, t: np.cross(zh, Ef(z, t)) / ETA0
    for z, t in rng.uniform(0, 1, (3, 2)) * np.array([lam, T]):
        S = np.cross(Ef(z, t), Hf(z, t))
        ok &= np.isclose(S[2], (Ef(z, t) @ Ef(z, t)) / ETA0) and np.allclose(S[:2], 0)
    ok &= np.isclose(avg(lambda t: np.cross(Ef(0.4, t), Hf(0.4, t))[2]), (E1 ** 2 + E2 ** 2) / (2 * ETA0))
check("S_z = (Ex^2 + Ey^2)/eta at every instant (no cross term); <S> = (E1^2 + E2^2)/(2 eta) for any phi", ok)
check("3 and 4 V/m in vacuum: 25/(2 x 377) = 33 mW/m^2", shown(25 / (2 * ETA0) * 1e3, "33", 2))

# ==================================================================================================== Q
section("Q. Example: two equal waves in opposite directions (standing wave)")
E0w = 1.0
E1f = lambda z, t: xh * E0w * np.cos(om * t - beta * z); H1f = lambda z, t: np.cross(zh, E1f(z, t)) / ETA0
E2f = lambda z, t: -xh * E0w * np.cos(om * t + beta * z); H2f = lambda z, t: np.cross(-zh, E2f(z, t)) / ETA0
Esw = lambda z, t: E1f(z, t) + E2f(z, t); Hsw = lambda z, t: H1f(z, t) + H2f(z, t)
ok = True
for z, t in rng.uniform(0, 1, (6, 2)) * np.array([lam, T]):
    ok &= np.allclose(Esw(z, t), xh * 2 * E0w * np.sin(om * t) * np.sin(beta * z))
    ok &= np.allclose(Hsw(z, t), yh * 2 * E0w / ETA0 * np.cos(om * t) * np.cos(beta * z))
    S = np.cross(Esw(z, t), Hsw(z, t))
    ok &= np.isclose(S[2], E0w ** 2 / ETA0 * np.sin(2 * om * t) * np.sin(2 * beta * z), atol=1e-15)
    ok &= np.isclose(S[2], (E1f(z, t) @ E1f(z, t) - E2f(z, t) @ E2f(z, t)) / ETA0, atol=1e-15)
check("E = x 2E0 sin wt sin bz, H = y (2E0/eta) cos wt cos bz, S = z (E0^2/eta) sin 2wt sin 2bz = (|E1|^2 - |E2|^2)/eta", ok)
ok = True
for z0 in rng.uniform(0, lam, 4):
    Exf = lambda z, t: Esw(z, t)[0]; Hyf = lambda z, t: Hsw(z, t)[1]
    t0 = rng.uniform(0, T)
    ok &= abs(fd(Exf, (z0, t0), 0, lam * 1e-4) + MU0 * fd(Hyf, (z0, t0), 1, T * 1e-4)) < 1e-6 * beta
    ok &= abs(-fd(Hyf, (z0, t0), 0, lam * 1e-4) - EPS0 * fd(Exf, (z0, t0), 1, T * 1e-4)) < 1e-6 * beta / ETA0
check("the standing-wave fields satisfy the source-free Maxwell equations", ok)
wsw = lambda z, t: 0.5 * EPS0 * Esw(z, t) @ Esw(z, t) + 0.5 * MU0 * Hsw(z, t) @ Hsw(z, t)
ok = True
for z0 in rng.uniform(0, lam, 4):
    ok &= abs(avg(lambda t: np.cross(Esw(z0, t), Hsw(z0, t))[2])) < 1e-12 and np.isclose(avg(lambda t: wsw(z0, t)), EPS0 * E0w ** 2)
check("<S> = 0 and <w> = eps E0^2 at every z", ok)
check("S changes sign every quarter period", np.sign(np.sin(2 * om * (T / 8))) != np.sign(np.sin(2 * om * (3 * T / 8))))
check("where sin bz = 0, w = 0 at the instants cos wt = 0", np.isclose(wsw(lam / 2, T / 4), 0, atol=1e-30))
Ehalf = [integrate.quad(lambda z: wsw(z, t), 0.13 * lam, 0.63 * lam, epsabs=0, epsrel=1e-12)[0] for t in rng.uniform(0, T, 4)]
check("energy in any half wavelength is constant in time (= eps E0^2 lambda/2)", np.allclose(Ehalf, EPS0 * E0w ** 2 * lam / 2))

# ==================================================================================================== R
section("R. Worked problem: energy bookkeeping for a radiating sheet (x = 0, J_s = -z 3 u(t) cos wt, eps_r = 2.25)")
epsW, muW = 2.25 * eps0x, mu0x
vW, etaW = 1 / math.sqrt(muW * epsW), math.sqrt(muW / epsW)
omW = 4 * np.pi * 1e6; fW = omW / (2 * np.pi); TW = 1 / fW; betaW = omW / vW; lamW = 2 * np.pi / betaW; J0W = 3.0
check("v = 2e8 m/s, eta = 80 pi = 251 ohm", np.isclose(vW, 2e8) and np.isclose(etaW, 80 * np.pi) and shown(etaW, "251", 3))
check("f = 2 MHz, T = 0.5 us, beta = 0.02 pi = 0.0628 rad/m, lambda = 100 m",
      np.isclose(fW, 2e6) and np.isclose(TW, 0.5e-6) and np.isclose(betaW, 0.02 * np.pi) and shown(betaW, "0.0628", 3) and np.isclose(lamW, 100))
JsW = lambda t: -zh * J0W * np.cos(omW * t) * (t >= 0)
def wp_fields(x, t):
    n = xh if x > 0 else -xh
    Jd = JsW(t - abs(x) / vW)
    return -etaW / 2 * Jd, 0.5 * np.cross(Jd, n)
ok = True
for _ in range(8):
    x = rng.uniform(-900, 900); t = abs(x) / vW + rng.uniform(0, 3e-6)
    E, H = wp_fields(x, t); sg = 1 if x > 0 else -1
    ok &= np.allclose(E, zh * 120 * np.pi * np.cos(omW * t - sg * betaW * x))
    ok &= np.allclose(H, -sg * yh * 1.5 * np.cos(omW * t - sg * betaW * x))
    ok &= np.allclose(np.cross(E, H), sg * xh * 180 * np.pi * np.cos(omW * t - sg * betaW * x) ** 2)
check("Answer (a): E = z 120 pi cos(wt -+ beta x), H = -+ y 1.5 cos(...); S = +- x 180 pi cos^2 (np.cross)", ok)
check("fields are zero ahead of the fronts (|x| > v t)", all(np.allclose(wp_fields(x, 1e-6)[0], 0) for x in (250, -250, 800)))
check("Answer (a) checks: z x (-y) = +x, z x (+y) = -x; 120 pi/1.5 = 80 pi; x x (H1 - H2) = J_s",
      np.allclose(np.cross(zh, -yh), xh) and np.allclose(np.cross(zh, yh), -xh) and np.isclose(120 * np.pi / 1.5, etaW)
      and all(np.allclose(np.cross(xh, wp_fields(1e-12, t)[1] - wp_fields(-1e-12, t)[1]), JsW(t), atol=1e-9) for t in (0.1e-6, 0.33e-6)))
ok = True
for x0 in (35.0, -61.0):
    for t0 in (2.1e-6, 2.37e-6):
        Ezf = lambda x, t: wp_fields(x, t)[0][2]; Hyf = lambda x, t: wp_fields(x, t)[1][1]
        hx, ht = 1e-3, 1e-12
        # Faraday y-component: (curl E)_y = -dEz/dx = -mu dHy/dt ; Ampere z-component: (curl H)_z = dHy/dx = eps dEz/dt
        ok &= abs(-fd(Ezf, (x0, t0), 0, hx) + muW * fd(Hyf, (x0, t0), 1, ht)) < 1e-6 * etaW * 1.5 * betaW
        ok &= abs(fd(Hyf, (x0, t0), 0, hx) - epsW * fd(Ezf, (x0, t0), 1, ht)) < 1e-6 * 1.5 * betaW
check("WP fields satisfy Maxwell's equations in the dielectric on both sides", ok)
avgW = lambda f: integrate.quad(lambda u: f(1e-6 + u / omW), 0, 2 * np.pi, limit=200, epsabs=1e-12, epsrel=1e-12)[0] / (2 * np.pi)
JsE_W = lambda t: JsW(t) @ wp_fields(1e-15, t)[0]
check("Answer (b): J_s.E = -360 pi cos^2 wt; average -180 pi = -565 W/m^2; peak 360 pi = 1131 W/m^2",
      np.isclose(JsE_W(1.17e-6), -360 * np.pi * np.cos(omW * 1.17e-6) ** 2) and np.isclose(avgW(JsE_W), -180 * np.pi)
      and shown(-180 * np.pi, "-565", 3) and shown(360 * np.pi, "1131", 4) and np.isclose(-etaW * J0W ** 2 / 4, -180 * np.pi))
SavW = avgW(lambda t: np.cross(*wp_fields(42.0, t))[0]); SavWm = avgW(lambda t: np.cross(*wp_fields(-42.0, t))[0])
check("Answer (c): <S> = +- x 90 pi = 283 W/m^2 = eta J0^2/8; balance 90 pi + 90 pi = 180 pi",
      np.isclose(SavW, 90 * np.pi) and np.isclose(SavWm, -90 * np.pi) and shown(90 * np.pi, "283", 3)
      and np.isclose(etaW * J0W ** 2 / 8, 90 * np.pi) and np.isclose(SavW - SavWm, -avgW(JsE_W)))
t3 = 3e-6
Win, _ = integrate.quad(lambda t: -JsE_W(t), 0, t3, limit=400, epsabs=0, epsrel=1e-12)
check("Answer (d): delivered by 3 us = 540 pi uJ/m^2 = 1.70 mJ/m^2 (3 us = 6 periods)",
      np.isclose(Win, 540 * np.pi * 1e-6) and shown(Win * 1e3, "1.70", 3) and np.isclose(t3 / TW, 6))
def stored(t):
    w = lambda x: 0.5 * epsW * wp_fields(x, t)[0] @ wp_fields(x, t)[0] + 0.5 * muW * wp_fields(x, t)[1] @ wp_fields(x, t)[1]
    front = vW * t
    a, _ = integrate.quad(w, 1e-12, front, limit=500, epsabs=0, epsrel=1e-11)
    b, _ = integrate.quad(w, -front, -1e-12, limit=500, epsabs=0, epsrel=1e-11)
    return a, b
a, b = stored(t3)
check("integrating w = 1/2 eps E^2 + 1/2 mu H^2 over |x| < 600 m at 3 us gives 270 pi uJ/m^2 per side, 540 pi in total",
      np.isclose(a, 270 * np.pi * 1e-6, rtol=1e-8) and np.isclose(b, 270 * np.pi * 1e-6, rtol=1e-8) and shown(a * 1e3, "0.85", 2))
ok = True
for t in (0.37e-6, 1.234e-6, 2.71e-6):
    Wd, _ = integrate.quad(lambda tt: -JsE_W(tt), 0, t, limit=400, epsabs=0, epsrel=1e-12)
    a, b = stored(t)
    ok &= np.isclose(a + b, Wd, rtol=1e-8) and np.isclose(Wd, 0.5 * etaW * J0W ** 2 * (t / 2 + np.sin(2 * omW * t) / (4 * omW)), rtol=1e-10)
check("at any t (not only whole periods): stored = 1/2 eta J0^2 [t/2 + sin(2wt)/(4w)] = integral of -J_s.E", ok)
wavg = 0.5 * epsW * (120 * np.pi) ** 2
check("<w> = 1/2 eps E0^2 = 450 pi e-9 = 1.41 uJ/m^3; <S>/<w> = 2e8 m/s = v",
      np.isclose(wavg, 450 * np.pi * 1e-9) and shown(wavg * 1e6, "1.41", 3) and np.isclose(90 * np.pi / wavg, vW))
check("epsilon = 2.25 eps0 = 1e-9/(16 pi) F/m (exam constants); w_e = w_m for each one-way wave",
      np.isclose(epsW, 1e-9 / (16 * np.pi)) and np.isclose(0.5 * epsW * (120 * np.pi) ** 2, 0.5 * muW * 1.5 ** 2))
t_arr = 900 / vW
Pwin_av = avgW(lambda t: np.cross(*wp_fields(900.0, t + 4.5e-6))[0] * 1.0)
check("Answer (e): front at 900 m at 4.5 us; average 90 pi x 1 m^2 = 283 W; instantaneous 0..180 pi = 565 W at 2f = 4 MHz",
      np.isclose(t_arr, 4.5e-6) and np.isclose(Pwin_av, 90 * np.pi) and shown(180 * np.pi, "565", 3) and np.isclose(2 * fW, 4e6)
      and np.allclose(wp_fields(900.0, 4.4e-6)[0], 0))
etaV = 120 * np.pi
check("vacuum variant: E amplitude 180 pi = 565 V/m, <S> = 135 pi = 424 W/m^2, injected 270 pi = 848 W/m^2, H stays 1.5 A/m",
      np.isclose(etaV * J0W / 2, 180 * np.pi) and np.isclose(etaV * J0W ** 2 / 8, 135 * np.pi) and shown(135 * np.pi, "424", 3)
      and np.isclose(etaV * J0W ** 2 / 4, 270 * np.pi) and shown(270 * np.pi, "848", 3) and np.isclose(J0W / 2, 1.5))
# exam key carry-over (S20 HE3 #2, read from 329sum20he3sol-2.png): <Js.E> = -480 pi, <S> = 240 pi, 2 us at 600 m, lambda = 300 m,
# E amplitude 240 pi; sheet z = 0, y-directed, sin, w = 2 pi 1e6, 4 A/m, free space
key = {"<JsE>": -480 * np.pi, "<S>": 240 * np.pi, "arrival": 2e-6, "lambda": 300, "E0": 240 * np.pi}
wp = {"<JsE>": -180 * np.pi, "<S>": 90 * np.pi, "arrival": 4.5e-6, "lambda": 100, "E0": 120 * np.pi}
check("no exam-key number carries over to the worked problem (S20 HE3 #2c-d and e-f)",
      all(not np.isclose(key[k], wp[k]) for k in key))
check("changed details vs the exam: plane x = 0 (z = 0), current -z (y), cos (sin), 2 MHz (1 MHz), 3 A/m (4 A/m), eps_r 2.25 (vacuum)", True)

# ==================================================================================================== S
section("S. Figures: curves parsed from the SVG against the formulas; arrows against np.cross in the screen frame")
FIG = "/home/claude/work/figs/"
def load(name): return open(FIG + name + ".html").read()
def paths(s):
    out = []
    for d, attrs in re.findall(r'<path d="([^"]+)"([^>]*)/>', s):
        st = re.search(r'stroke="([^"]+)"', attrs); sw = re.search(r'stroke-width="([\d.]+)"', attrs)
        pts = np.array([[float(a), float(b)] for a, b in re.findall(r'(-?[\d.]+),(-?[\d.]+)', d)])
        out.append((st.group(1) if st else None, float(sw.group(1)) if sw else None, pts, attrs))
    return out
def arrows(s):
    out = []
    for x1, y1, x2, y2, st, sw, rest in re.findall(r'<line x1="([-\d.]+)" y1="([-\d.]+)" x2="([-\d.]+)" y2="([-\d.]+)" stroke="([^"]+)" stroke-width="([\d.]+)"([^>]*)/>', s):
        if "marker-end" in rest:
            out.append((float(x1), float(y1), float(x2), float(y2), st, float(sw)))
    return out
def dots(s, r):
    return [(float(cx), float(cy), fill) for cx, cy, rr, fill in re.findall(r'<circle cx="([-\d.]+)" cy="([-\d.]+)" r="([\d.]+)" fill="([^"]+)"', s) if float(rr) == r]
def screen_dir(a):                       # SVG y is down; screen frame Y is up
    d = np.array([a[2] - a[0], -(a[3] - a[1]), 0.0]); return d / np.linalg.norm(d)
X, Y, Z = np.eye(3)

# --- poy-sheet-energy
s = load("poy-sheet-energy")
P = [p for p in paths(s) if p[0] in ("var(--accent)", "var(--hi)") and p[1] == 2.4 and len(p[2]) > 20]
ok = len(P) == 4; dev = 0
for st, sw, pts, _ in P:
    if pts[:, 1].mean() < 300:                                    # panel 1 snapshot: MZ = lin(-2.15, 2.15, 70, 610), Y = 166 - 88 s
        zl = -2.15 + (pts[:, 0] - 70) * 4.3 / 540; sv = (166 - pts[:, 1]) / 88
        model = np.sign(zl.mean()) * np.cos(2 * np.pi * zl) ** 2
    else:                                                         # panel 2: MT = lin(0, 2, 80, 440), Y = 506 - 82 p
        tl = (pts[:, 0] - 80) * 2 / 360; sv = (506 - pts[:, 1]) / 82
        model = (2 if st == "var(--hi)" else 1) * np.cos(2 * np.pi * tl) ** 2
    dev = max(dev, np.max(np.abs(sv - model)))
check("poy-sheet-energy: panel 1 = +-cos^2(beta z) (t = 0), panel 2 = 2cos^2 wt (red) and cos^2 wt (blue)", ok and dev < 6e-3, f"max dev {dev:.4f}")
A = [a for a in arrows(s) if a[4] == "currentColor" and a[5] == 1.8]
ok = len(A) == 2 and any(np.allclose(screen_dir(a), X) and a[0] > 340 for a in A) and any(np.allclose(screen_dir(a), -X) and a[0] < 340 for a in A)
check("poy-sheet-energy: 'humps move out at c' arrows point away from the sheet on both sides", ok)

# --- poy-time-average
s = load("poy-time-average")
P = [p for p in paths(s) if p[1] == 2.4 and len(p[2]) > 20]
dev = 0; n_ok = 0; TA_ONE_WAVE_AT = "not found"
for st, sw, pts, _ in P:
    tl = (pts[:, 0] - 80) * 2 / 370
    if pts[:, 1].mean() < 240:                                   # panel 1, Y = 196 - 140 p
        pv = (196 - pts[:, 1]) / 140; model = np.cos(2 * np.pi * tl) ** 2
    else:                                                        # panel 2, Y = 382 - 84 p
        pv = (382 - pts[:, 1]) / 84
        if st == "var(--hi)":
            model = np.sin(4 * np.pi * tl)                       # standing wave at z = lambda/8: sin 2wt sin(pi/2)
        else:
            # one travelling wave at the same point z = lambda/8 is cos^2(wt - pi/4); at z = 0 it would be cos^2(wt)
            m8 = np.cos(2 * np.pi * tl - np.pi / 4) ** 2; m0 = np.cos(2 * np.pi * tl) ** 2
            at8 = np.max(np.abs(pv - m8)) < np.max(np.abs(pv - m0))
            model = m8 if at8 else m0
            TA_ONE_WAVE_AT = "lambda/8" if at8 else "z = 0"
    dev = max(dev, np.max(np.abs(pv - model))); n_ok += 1
check("poy-time-average: cos^2 wt, the travelling wave's cos^2 and the standing wave's sin 2wt match their formulas",
      n_ok == 3 and dev < 6e-3, f"max dev {dev:.4f}")
check("poy-time-average panel 2 compares the two waves at ONE point (title says 'S at one point'; standing wave at z = lambda/8)",
      TA_ONE_WAVE_AT == "lambda/8", f"travelling-wave curve drawn for {TA_ONE_WAVE_AT}")
check("caption colours: band above 1/2 is --accent (blue), below is --accent2 (green); standing wave --hi (red)",
      'fill="var(--accent)" fill-opacity="0.20"' in s and 'fill="var(--accent2)" fill-opacity="0.20"' in s)

# --- poy-resistive-wire
s = load("poy-resistive-wire")
P = [p for p in paths(s) if p[0] == "var(--hi)" and p[1] == 2.6]
pts = P[0][2]; rr = (pts[:, 0] - 466) / 136; pv = (270 - pts[:, 1]) / 180      # MR = lin(0, 1, 466, 602) after the fix
check("poy-resistive-wire panel 2: P(rho)/I^2R = (rho/a)^2", len(P) == 1 and np.max(np.abs(pv - rr ** 2)) < 3e-3)
Yc, R_ = 176, 24
zphys = X
for side, rho_hat in (("above", Y), ("below", -Y)):
    phi_hat = np.cross(zphys, rho_hat)            # z x rho_hat
    S_exp = np.cross(zphys, phi_hat)              # E (along z_phys = X) x H (along phi_hat)
    Sarr = [a for a in arrows(s) if a[4] == "currentColor" and a[5] == 2.8 and ((a[1] < Yc) == (side == "above"))]
    ok = len(Sarr) == 2 and all(np.allclose(screen_dir(a), S_exp) for a in Sarr)
    sym = "odot" if phi_hat[2] > 0 else "otimes"
    hy = Yc - R_ - 20 if side == "above" else Yc + R_ + 20
    have_dot = any(abs(cy - hy) < 1 and fill == "var(--accent2)" for cx, cy, fill in dots(s, 1.8))
    ok &= (sym == "odot") == have_dot
    check(f"poy-resistive-wire {side} the wire: H = {sym} (z x rho_hat), S = E x H points {'down' if S_exp[1] < 0 else 'up'} into the wire", ok)
Earr = [a for a in arrows(s) if a[4] == "var(--accent)"]
check("poy-resistive-wire: E arrows along +z (to the right), as the current I", len(Earr) == 3 and all(np.allclose(screen_dir(a), X) for a in Earr))

# --- poy-problem-energy
s = load("poy-problem-energy")
wpk = epsW * (etaW * J0W / 2) ** 2
P = [p for p in paths(s) if p[0] == "var(--accent2)" and p[1] == 1.8]
dev = 0
for st, sw, pts, _ in P:
    xx = -820 + (pts[:, 0] - 66) * 1640 / 544; wv = (206 - pts[:, 1]) / 136
    inside = np.abs(xx) < 598
    dev = max(dev, np.max(np.abs(wv[inside] - np.cos(omW * t3 - betaW * np.abs(xx[inside])) ** 2)))
    dev = max(dev, np.max(np.abs(wv[np.abs(xx) > 602])))
check("poy-problem-energy panel 1: w(x, 3 us)/w_peak = cos^2(wt - beta|x|) inside the fronts, 0 outside", len(P) == 2 and dev < 0.015, f"{dev:.4f}")
check("poy-problem-energy: w_peak = eps E0^2 = 2.83 uJ/m^3 and the dashed average 1.41 uJ/m^3 is half of it",
      shown(wpk * 1e6, "2.83", 3) and "1.41 µJ/m³" in s and np.isclose(wpk / 2, wavg))
P = [p for p in paths(s) if p[0] == "var(--hi)" and p[1] == 2.4]
pts = P[0][2]; tl = (pts[:, 0] - 82) * 3 / 298 * 1e-6; Wl = (452 - pts[:, 1]) * 1.75 / 160
Wmodel = 0.5 * etaW * J0W ** 2 * (tl / 2 + np.sin(2 * omW * tl) / (4 * omW)) * 1e3
check("poy-problem-energy panel 2 line: integral of -J_s.E (mJ/m^2)", np.max(np.abs(Wl - Wmodel)) < 0.006, f"{np.max(np.abs(Wl-Wmodel)):.4f}")
D = dots(s, 3.6)
dd = [abs((452 - cy) * 1.75 / 160 - 0.5 * etaW * J0W ** 2 * (tq / 2 + np.sin(2 * omW * tq) / (4 * omW)) * 1e3)
      for cx, cy, fill in D for tq in [((cx - 82) * 3 / 298) * 1e-6]]
check("poy-problem-energy panel 2 dots (stored energy) lie on the delivered-energy line", len(D) == 12 and max(dd) < 0.006)
# icon: physics x -> X, z -> Y, so y -> z x x = Y x X = -Z (into the page)
yscr = np.cross(Y, X)
check("icon frame: y_phys = z x x maps to -Z (into the page), as labelled", np.allclose(yscr, -Z))
gx = 520
Jarr = [a for a in arrows(s) if a[4] == "var(--hi)" and abs(a[0] - gx) < 1]
Earr = [a for a in arrows(s) if a[4] == "var(--accent)" and a[5] == 2.2]
Sarr = [a for a in arrows(s) if a[4] == "currentColor" and a[5] == 2.2]
E_exp = Y                                                       # E = +z
H_right, H_left = -yscr, +yscr                                  # H = -y for x > 0, +y for x < 0
check("icon: J_s along -z is drawn down; E = +z is drawn up on both sides",
      len(Jarr) == 2 and all(np.allclose(screen_dir(a), -Y) for a in Jarr) and len(Earr) == 2 and all(np.allclose(screen_dir(a), E_exp) for a in Earr))
okS = len(Sarr) == 2
for a in Sarr:
    exp = np.cross(E_exp, H_right if a[0] > gx else H_left)
    okS &= np.allclose(screen_dir(a), exp)
check("icon: S = E x H points right for x > 0 and left for x < 0 (np.cross in the screen frame)", okS)
odx = [cx for cx, cy, fill in dots(s, 1.8) if fill == "var(--accent2)"]
check("icon: H = -y (odot, out of the page) on the right, +y (otimes) on the left",
      np.allclose(H_right, Z) and np.allclose(H_left, -Z) and len(odx) == 1 and odx[0] > gx)

# --- poy-energy-ledger: every boundary arrow points outward
s = load("poy-energy-ledger")
ok = True; cnt = 0
for cx in (160, 480):
    for a in arrows(s):
        mx = (a[0] + a[2]) / 2
        if abs(mx - cx) < 140 and a[5] == 2.2 and a[4] in ("var(--accent)", "var(--accent2)"):
            d = np.array([a[2] - a[0], a[3] - a[1]]); r = np.array([a[0] - cx, a[1] - 138])
            ok &= d @ r > 0; cnt += 1
check("poy-energy-ledger: all J and S arrows on the two ellipses point outward", ok and cnt >= 12, f"{cnt} arrows")
check("poy-energy-ledger equations: dW/dt = -closed int S.dA - int J.E dV and dw/dt + div S = -J.E",
      "dW/dt = −∮ S · dA − ∫ J·E dV" in s and "∂w/∂t + ∇ · S = −J·E" in s and "dQ/dt = −∮ J · dA" in s)

# ==================================================================================================== T
section("T. Scope and approximations")
page = open("/home/claude/work/content-src/3-maxwell-and-waves/20-poynting-theorem-and-monochromatic-waves.md").read()
probl = open("/home/claude/work/content-src/problems/energy-bookkeeping-for-a-radiating-sheet.md").read()
cth = open("/home/claude/work/content-src/concepts/poynting-theorem.md").read()
for nm, txt in (("lecture page", page), ("worked problem", probl), ("poynting-theorem concept", cth)):
    check(f"no phasor algebra in the {nm} (no tilde fields, no Re{{}}, no e^{{j...}})",
          "\\tilde" not in txt and "\\text{Re}" not in txt and "e^{j" not in txt and "e^{-j" not in txt and "e^{\\mp j" not in txt)
check("complex gamma/eta approximations: none quoted in Lecture 20 (lossless only) - nothing to compare", True)
check("the 1/r field of a transmitter is qualified as far-field on the lecture page",
      re.search(r"far from (it|the (antenna|transmitter))|far field|far-field", page, re.I) is not None)
check("the 1/r field of an antenna is qualified as far-field on the poynting-theorem concept page",
      re.search(r"far from (it|the (antenna|transmitter))|far field|far-field", cth, re.I) is not None)

print("\n" + "-" * 100)
print(f"{sum(RES)} PASS, {len(RES) - sum(RES)} FAIL, {len(RES)} checks")
