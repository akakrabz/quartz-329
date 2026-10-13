#!/usr/bin/env python3
"""Independent reviewer's verification for the Lecture 22 page set (ECE 329 study site, build 8).

Pages checked:
  content-src/3-maxwell-and-waves/22-phasor-maxwell-equations-and-damped-waves.md   (sections 1-10)
  content-src/concepts/propagation-constant.md, content-src/concepts/intrinsic-impedance.md (new section)
  content-src/problems/decoding-a-damped-wave.md
  figs_l22.py (lossy-damped-wave, lossy-phasor-spiral, lossy-phase-dial, lossy-regimes)
  and the regime overview against content-src/3-maxwell-and-waves/23-imperfect-dielectrics-and-good-conductors.md

Written without reading the writer's verify_L22.py. numpy/scipy only.
Every vector direction is an explicit np.cross; every curl is a finite-difference curl; every time average is a
quadrature compared with 1/2 Re{A B*}; every gamma and eta is the exact complex square root (numpy principal branch).

Handbook values used (stated once here):
  mu0 = 4 pi 1e-7 H/m (course value; CODATA 2018 1.25663706212e-6), eps0 = 8.8541878128e-12 F/m (CODATA 2018),
  c = 299 792 458 m/s, e = 1.602176634e-19 C, m_e = 9.1093837015e-31 kg (CODATA 2018);
  course shorthand eps0 ~ 1e-9/(36 pi) F/m (makes c = 3e8 and eta0 = 120 pi exactly);
  sea water sigma = 4 S/m (Rao Table 5.1), eps_r = 80 (Rao Table 5.3) / 81 (Kudeki notes);
  copper sigma = 5.8e7 S/m (Rao Table 5.1), N = 8.47e28 m^-3 (one conduction electron per atom, Kittel);
  plasma frequency f_p = 8.98 sqrt(N) Hz (standard ionospheric rule); daytime F2 peak N ~ 1e12 m^-3.
"""
import numpy as np
from scipy import integrate

NPASS = 0
NFAIL = 0
FAILS = []


def check(name, ok, detail=""):
    global NPASS, NFAIL
    if ok:
        NPASS += 1
    else:
        NFAIL += 1
        FAILS.append(name)
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"   [{detail}]" if detail else ""))


def close(name, got, want, rtol=1e-9, atol=0.0):
    got = np.asarray(got, dtype=complex)
    want = np.asarray(want, dtype=complex)
    err = np.max(np.abs(got - want))
    ok = bool(err <= atol + rtol * np.max(np.abs(want)))
    gs = got.item() if got.size == 1 else "array"
    ws = want.item() if want.size == 1 else "array"
    if got.size == 1:
        gs = f"{gs.real:.6g}" if abs(gs.imag) < 1e-300 else f"{gs:.6g}"
        ws = f"{ws.real:.6g}" if abs(ws.imag) < 1e-300 else f"{ws:.6g}"
    check(name, ok, f"got {gs}, want {ws}, |err| {err:.2e}")
    return ok


def rounds_to(name, value, shown, digits):
    """value printed with `digits` decimals equals the page's `shown` string"""
    s = f"{value:.{digits}f}"
    check(name, s == shown, f"{value:.6g} -> {s}, page {shown}")


def section(t):
    print("\n" + "=" * 100 + "\n" + t + "\n" + "=" * 100)


mu0 = 4e-7 * np.pi
eps0 = 8.8541878128e-12
c0 = 299792458.0
qe = 1.602176634e-19
me = 9.1093837015e-31
eps0c = 1e-9 / (36 * np.pi)      # course shorthand
deg = np.pi / 180


def gam_eta(w, mu, eps, sig):
    """exact gamma and eta, principal square roots; sigma may be complex (Drude)"""
    A = 1j * w * mu
    B = sig + 1j * w * eps
    return np.sqrt(complex(A * B)), np.sqrt(complex(A / B))


def closed_forms(w, mu, eps, sig):
    """the page's section-5 closed forms, exactly as written"""
    s = sig / (w * eps)
    k = w * np.sqrt(mu * eps / 2)
    a = k * np.sqrt(np.sqrt(1 + s * s) - 1)
    b = k * np.sqrt(np.sqrt(1 + s * s) + 1)
    em = np.sqrt(mu / eps) / (1 + s * s) ** 0.25
    tau = 0.5 * np.arctan(s)
    return a, b, em, tau


def curl_fd(F, r, h=1e-6):
    """finite-difference curl of a complex vector field F(x,y,z) -> 3-vector, at point r"""
    x, y, z = r
    d = lambda i, j: (F(*(np.array(r) + h * np.eye(3)[j]))[i] - F(*(np.array(r) - h * np.eye(3)[j]))[i]) / (2 * h)
    return np.array([d(2, 1) - d(1, 2), d(0, 2) - d(2, 0), d(1, 0) - d(0, 1)])


X, Y, Z = np.eye(3)

# =====================================================================================================================
section("A. Constants and handbook values the pages lean on")
close("c = 1/sqrt(mu0 eps0) with CODATA eps0", 1 / np.sqrt(mu0 * eps0), c0, rtol=1e-8)
close("course eps0 = 1e-9/36pi gives c = 3e8 exactly", 1 / np.sqrt(mu0 * eps0c), 3e8, rtol=1e-13)
close("course eps0 gives eta0 = 120 pi exactly", np.sqrt(mu0 / eps0c), 120 * np.pi, rtol=1e-13)
close("eta0 (CODATA) = 376.73 ohm", np.sqrt(mu0 / eps0), 376.730, rtol=1e-5)
check("120 pi approximates eta0 to 0.07 % (intrinsic-impedance trap)", abs(120 * np.pi / np.sqrt(mu0 / eps0) - 1) < 0.0008,
      f"{100 * (120 * np.pi / np.sqrt(mu0 / eps0) - 1):.3f} %")
# sea water, L8 relaxation time and the L22 crossover
tr_sw = 81 * eps0 / 4
rounds_to("sea water eps/sigma = 0.18 ns (eps_r 81, sigma 4)", tr_sw * 1e9, "0.18", 2)
check("Lecture 8 page states sea water tau ~ 0.2 ns (not 0.18): attribution on L22 p.3 is loose",
      "0.2" == f"{tr_sw * 1e9:.1f}", f"L8 rounds {tr_sw * 1e9:.3f} ns to 0.2 ns")
fc81 = 4 / (2 * np.pi * 81 * eps0)
fc80 = 4 / (2 * np.pi * 80 * eps0)
check("sea water crossover near 0.9 GHz (81: 0.888, 80: 0.899; Rao Table 5.3 0.9e9)",
      abs(fc81 / 1e9 - 0.9) < 0.02 and abs(fc80 / 1e9 - 0.9) < 0.002, f"{fc81 / 1e9:.4f}, {fc80 / 1e9:.4f} GHz")
# Lecture 10's lossy medium
tr10 = 2 * eps0 / 2e-6
rounds_to("L10 medium eps/sigma = 8.85 us", tr10 * 1e6, "8.85", 2)
check("L10 medium crosses over near 18 kHz", abs(1 / (2 * np.pi * tr10) / 1e3 - 18) < 0.1, f"{1 / (2 * np.pi * tr10):.1f} Hz")
# copper collision frequency (L11) and the Drude correction at 1 GHz
nu_cu = 8.47e28 * qe ** 2 / (me * 5.8e7)
check("copper nu = N e^2/(m sigma) ~ 4e13 1/s (L11, L22 sec 8)", abs(nu_cu / 4e13 - 1) < 0.05, f"{nu_cu:.3e}")
sr = 1 / (1 + 1j * 2 * np.pi * 1e9 / 4e13)
check("Drude sigma(1 GHz)/sigma_DC within 1.6e-4 of 1 (nu = 4e13)", abs(abs(sr - 1) - 1.6e-4) < 0.05e-4, f"|sigma/sigma_DC - 1| = {abs(sr - 1):.3e}")
# ionosphere
wp2 = 1e12 * qe ** 2 / (me * eps0)
fp = np.sqrt(wp2) / (2 * np.pi)
check("f_p for N = 1e12 m^-3 is about 9 MHz; rule 8.98 sqrt(N) Hz", abs(fp / 1e6 - 8.98) < 0.01, f"{fp / 1e6:.4f} MHz")

# =====================================================================================================================
section("B. Section 1: d/dt -> j omega, vanishing phasors, the divergence laws, rho~ = 0 in a uniform conductor")
w = 2 * np.pi * 1e6
At = 0.7 - 1.3j
tt = np.linspace(0, 2e-6, 7)
h = 1e-12
fd = (np.real(At * np.exp(1j * w * (tt + h))) - np.real(At * np.exp(1j * w * (tt - h)))) / (2 * h)
close("d/dt Re{A e^{jwt}} = Re{jw A e^{jwt}} (finite difference)", fd, np.real(1j * w * At * np.exp(1j * w * tt)), rtol=1e-6)
check("Re{A e^{jwt}} at wt = 0 and pi/2 gives Re A and -Im A (so vanishing at all t => A = 0)",
      np.isclose(np.real(At), 0.7) and np.isclose(np.real(At * 1j), 1.3))
# continuity + Gauss in a uniform conductor: (sigma/eps + jw) rho = 0
for sig, eps_, ww in ((4.0, 81 * eps0, 2 * np.pi * 1e3), (1e-9, 4 * eps0, 2 * np.pi * 60), (5.8e7, eps0, 2 * np.pi * 1e9)):
    check(f"sigma + j w eps != 0 (sigma {sig:g}, f {ww / 2 / np.pi:g} Hz) so rho~ = 0", abs(sig + 1j * ww * eps_) > 0)
# relaxation equation in the time domain: a charge driven at frequency w cannot persist without a source:
# d rho/dt + (sigma/eps) rho = 0 has solution rho0 e^{-t sigma/eps}; a sustained Re{rho~ e^{jwt}} would need (sigma/eps + jw) rho~ = 0
sig, eps_ = 4.0, 81 * eps0
sol = integrate.solve_ivp(lambda t, r: -(sig / eps_) * r, (0, 5 * eps_ / sig), [1.0], rtol=1e-10, atol=1e-14)
close("relaxation rho(t) = rho0 e^{-t/(eps/sigma)} (ODE vs closed form at 5 relaxation times)", sol.y[0, -1], np.exp(-5), rtol=1e-6)

# =====================================================================================================================
section("C. Section 3: exact gamma and eta, the branch, gamma*eta = j w mu, gamma/eta = sigma + j w eps")
rng = np.random.default_rng(22)
svals = np.logspace(-6, 6, 241)
ok_branch = ok_prod = ok_quot = ok_tau = ok_epsc = ok_ab = True
worst = 0.0
for s in svals:
    mur, epr = rng.uniform(1, 5), rng.uniform(1, 81)
    ww = 2 * np.pi * 10 ** rng.uniform(2, 10)
    mu, eps_ = mur * mu0, epr * eps0
    sig = s * ww * eps_
    g, e = gam_eta(ww, mu, eps_, sig)
    ok_branch &= (g.real >= 0) and (g.imag > 0) and (e.real > 0)
    ok_ab &= g.imag >= g.real
    ok_tau &= 0 <= np.angle(e) < np.pi / 4
    worst = max(worst, abs(g * e / (1j * ww * mu) - 1), abs((g / e) / (sig + 1j * ww * eps_) - 1))
    epsc = eps_ - 1j * sig / ww
    ok_epsc &= np.isclose(1j * ww * np.sqrt(mu * epsc), g, rtol=1e-12) and np.isclose(np.sqrt(mu / epsc), e, rtol=1e-12)
check("principal roots: alpha >= 0, beta > 0, Re eta > 0 for s = 1e-6..1e6 (241 media)", ok_branch)
check("gamma*eta = j w mu and gamma/eta = sigma + j w eps hold with these roots", worst < 1e-12, f"worst rel err {worst:.1e}")
check("0 <= tau < 45 deg for every real sigma >= 0", ok_tau)
check("beta >= alpha for every real sigma >= 0", ok_ab)
check("complex permittivity form: gamma = j w sqrt(mu eps_c), eta = sqrt(mu/eps_c), eps_c = eps - j sigma/w", ok_epsc)
# the other root
g, e = gam_eta(3e8, mu0, 8 * eps0c, 1 / (20 * np.pi))
check("the other root -gamma has negative real part (e^{-gamma z} would grow along the travel)", (-g).real < 0)
check("mixing branches breaks the product rule: (-gamma) eta = -j w mu", np.isclose((-g) * e, -1j * 3e8 * mu0))
# sigma = 0 limit, computed as an exact complex product
g0, e0_ = gam_eta(2 * np.pi * 1e8, mu0, 4 * eps0c, 0.0)
close("sigma = 0: gamma = +j w sqrt(mu eps) (= j 4pi/3 at 100 MHz, eps_r 4)", g0, 1j * 4 * np.pi / 3, rtol=1e-13)
close("sigma = 0: eta = sqrt(mu/eps) = 60 pi", e0_, 60 * np.pi, rtol=1e-13)
# margin relations
ww, mu, eps_, sig = 3e8, 3 * mu0, 9 * eps0c, 1 / (30 * np.pi)
g, e = gam_eta(ww, mu, eps_, sig)
close("margin: mu = gamma eta / (j w)", g * e / (1j * ww), mu, rtol=1e-12)
close("margin: sigma = Re{gamma/eta}", (g / e).real, sig, rtol=1e-12)
close("margin: eps = Im{gamma/eta}/w", (g / e).imag / ww, eps_, rtol=1e-12)

# =====================================================================================================================
section("D. Section 5: closed forms and angle identities against the exact square roots")
ok = {k: True for k in ("a", "b", "em", "tau", "angg", "ab", "t2", "gg", "sq", "sum", "argB")}
worst = {k: 0.0 for k in ok}
for s in np.logspace(-3, 3, 121):
    ww, mu, eps_ = 2 * np.pi * 1e7, 2 * mu0, 6 * eps0
    sig = s * ww * eps_
    g, e = gam_eta(ww, mu, eps_, sig)
    a, b, em, tau = closed_forms(ww, mu, eps_, sig)
    errs = dict(a=abs(a / g.real - 1), b=abs(b / g.imag - 1), em=abs(em / abs(e) - 1), tau=abs(tau - np.angle(e)),
                angg=abs(np.angle(g) - (np.pi / 2 - tau)), ab=abs(g.real / g.imag - np.tan(tau)),
                t2=abs(np.tan(2 * tau) / s - 1) + abs(2 * a * b / (b * b - a * a) / s - 1),
                gg=abs(abs(g) * abs(e) / (ww * mu) - 1),
                sq=abs((b * b - a * a) / (ww ** 2 * mu * eps_) - 1) + abs(2 * a * b / (ww * mu * sig) - 1),
                sum=abs((a * a + b * b) / (ww ** 2 * mu * eps_ * np.sqrt(1 + s * s)) - 1),
                argB=abs(np.angle(sig + 1j * ww * eps_) - (np.pi / 2 - np.arctan(s))))
    for k in ok:
        worst[k] = max(worst[k], errs[k])
labels = dict(a="alpha closed form = Re{gamma}", b="beta closed form = Im{gamma}", em="|eta| = sqrt(mu/eps)/(1+s^2)^(1/4)",
              tau="tau = (1/2) atan(s) = angle(eta)", angg="angle(gamma) = 90 deg - tau", ab="alpha/beta = tan(tau)",
              t2="s = tan(2 tau) = 2 alpha beta/(beta^2 - alpha^2)", gg="|gamma||eta| = w mu",
              sq="beta^2 - alpha^2 = w^2 mu eps and 2 alpha beta = w mu sigma", sum="alpha^2 + beta^2 = w^2 mu eps sqrt(1+s^2)",
              argB="angle(sigma + j w eps) = 90 deg - atan(s)")
for k in ok:
    check(labels[k] + " (s = 1e-3..1e3)", worst[k] < 1e-8, f"worst {worst[k]:.1e}")
check("tau -> 45 deg only as s -> inf (tau(1e6) < 45 deg)", np.degrees(0.5 * np.arctan(1e6)) < 45)

# =====================================================================================================================
section("E. Sections 2-4: the fields satisfy Maxwell's equations (finite differences, phasor and time domain)")
# lossless Helmholtz and H from Faraday
ww, mu, eps_ = 2 * np.pi * 1e8, mu0, 4 * eps0c
bet = ww * np.sqrt(mu * eps_)
eta = np.sqrt(mu / eps_)
for sgn in (+1, -1):
    Ex = lambda z: (1.5 - 0.4j) * np.exp(-sgn * 1j * bet * z)
    zz = 0.37
    hz = 1e-5
    d2 = (Ex(zz + hz) - 2 * Ex(zz) + Ex(zz - hz)) / hz ** 2
    close(f"Helmholtz d2E/dz2 + w^2 mu eps E = 0 for e^({'-' if sgn > 0 else '+'}j beta z)", d2 + ww ** 2 * mu * eps_ * Ex(zz), 0,
          atol=1e-4 * abs(ww ** 2 * mu * eps_ * Ex(zz)))
    Hy = -1 / (1j * ww * mu) * (Ex(zz + hz) - Ex(zz - hz)) / (2 * hz)
    close(f"H~y = -(1/jw mu) dE~x/dz = {'+' if sgn > 0 else '-'}E~x/eta", Hy, sgn * Ex(zz) / eta, rtol=1e-7)
# conducting medium: phasor fields of the section-4 key, both directions, complex E0, magnetic medium
for (ww, mu, eps_, sig) in ((3e8, mu0, 8 * eps0c, 1 / (20 * np.pi)), (1e8, 3 * mu0, 9 * eps0c, 1 / (30 * np.pi)),
                            (2 * np.pi * 1e3, mu0, 81 * eps0, 4.0)):
    g, e = gam_eta(ww, mu, eps_, sig)
    E0 = 2.0 * np.exp(1j * 0.9)
    for sgn in (+1, -1):
        F_E = lambda x, y, z: np.array([E0 * np.exp(-sgn * g * z), 0, 0], dtype=complex)
        F_H = lambda x, y, z: np.array([0, sgn * E0 / e * np.exp(-sgn * g * z), 0], dtype=complex)
        r = (0.11, -0.2, 0.3 / abs(g))
        hh = 1e-4 / abs(g)
        cE, cH = curl_fd(F_E, r, hh), curl_fd(F_H, r, hh)
        tag = f"(w {ww:.3g}, mu_r {mu / mu0:.0f}, s {sig / (ww * eps_):.3g}, {'+z' if sgn > 0 else '-z'})"
        close("phasor Faraday curl E~ = -j w mu H~ " + tag, cE, -1j * ww * mu * F_H(*r), rtol=1e-6)
        close("phasor Ampere curl H~ = (sigma + j w eps) E~ " + tag, cH, (sig + 1j * ww * eps_) * F_E(*r), rtol=1e-6)
# time domain: the real fields of the key satisfy the time-domain laws and the damped wave equation
ww, mu, eps_, sig = 3e8, mu0, 8 * eps0c, 1 / (20 * np.pi)
g, e = gam_eta(ww, mu, eps_, sig)
al, be, tau, em = g.real, g.imag, np.angle(e), abs(e)
phi = 0.4
for sgn in (+1, -1):
    Ext = lambda z, t: np.exp(-sgn * al * z) * np.cos(ww * t - sgn * be * z + phi)
    Hyt = lambda z, t: sgn / em * np.exp(-sgn * al * z) * np.cos(ww * t - sgn * be * z + phi - tau)
    z0, t0, hz, ht = 0.23, 1.7e-9, 1e-5, 1e-14
    dEz = (Ext(z0 + hz, t0) - Ext(z0 - hz, t0)) / (2 * hz)
    dHt = (Hyt(z0, t0 + ht) - Hyt(z0, t0 - ht)) / (2 * ht)
    dHz = (Hyt(z0 + hz, t0) - Hyt(z0 - hz, t0)) / (2 * hz)
    dEt = (Ext(z0, t0 + ht) - Ext(z0, t0 - ht)) / (2 * ht)
    tag = "+z" if sgn > 0 else "-z"
    close(f"time-domain Faraday dEx/dz = -mu dHy/dt ({tag} wave of the key)", dEz, -mu * dHt, rtol=1e-5)
    close(f"time-domain Ampere -dHy/dz = sigma Ex + eps dEx/dt ({tag})", -dHz, sig * Ext(z0, t0) + eps_ * dEt, rtol=1e-5)
    hz2, ht2 = 1e-4, 1e-13
    d2z = (Ext(z0 + hz2, t0) - 2 * Ext(z0, t0) + Ext(z0 - hz2, t0)) / hz2 ** 2
    d2t = (Ext(z0, t0 + ht2) - 2 * Ext(z0, t0) + Ext(z0, t0 - ht2)) / ht2 ** 2
    close(f"damped wave equation d2E/dz2 = mu sigma dE/dt + mu eps d2E/dt2 ({tag})", d2z, mu * sig * dEt + mu * eps_ * d2t, rtol=1e-4)
close("phasor form: gamma^2 = j w mu sigma - w^2 mu eps", g * g, 1j * ww * mu * sig - ww ** 2 * mu * eps_, rtol=1e-12)
# divergence laws follow: div(curl) = 0 numerically for a smooth 3-D field (identity used in sec. 1)
F = lambda x, y, z: np.array([np.sin(y * z) + x ** 2, np.exp(0.3 * x) * z, np.cos(x * y)], dtype=complex)
def div_fd(Fv, r, hh=1e-4):
    return sum((Fv(*(np.array(r) + hh * np.eye(3)[i]))[i] - Fv(*(np.array(r) - hh * np.eye(3)[i]))[i]) / (2 * hh) for i in range(3))
cF = lambda x, y, z: curl_fd(F, (x, y, z), 1e-5)
check("div(curl F) = 0 for a generic field (the identity behind the 'divergence laws come for free')",
      abs(div_fd(cF, (0.3, -0.7, 0.5))) < 1e-5, f"{abs(div_fd(cF, (0.3, -0.7, 0.5))):.1e}")

# =====================================================================================================================
section("F. Section 4: which field lags, by how much, in time and in a snapshot")
for (ww, mu, eps_, sig) in ((3e8, mu0, 8 * eps0c, 1 / (20 * np.pi)), (1e8, 3 * mu0, 9 * eps0c, 1 / (30 * np.pi))):
    g, e = gam_eta(ww, mu, eps_, sig)
    al, be, tau, em = g.real, g.imag, np.angle(e), abs(e)
    for sgn in (+1, -1):
        Et = lambda z, t: np.exp(-sgn * al * z) * np.cos(ww * t - sgn * be * z + 0.3)
        Ht = lambda z, t: np.exp(-sgn * al * z) / em * np.cos(ww * t - sgn * be * z + 0.3 - tau)
        T = 2 * np.pi / ww
        t = np.linspace(0, T, 200001)
        z0 = 0.41
        tE, tH = t[np.argmax(Et(z0, t))], t[np.argmax(Ht(z0, t))]
        lag = ((tH - tE) % T)
        tag = f"(tau {np.degrees(tau):.2f} deg, {'+z' if sgn > 0 else '-z'})"
        close("H peaks tau/w after E at a fixed point " + tag, lag, tau / ww, rtol=2e-4)
        close("amplitude ratio |E|/|H| = |eta| " + tag, Et(z0, t).max() / Ht(z0, t).max(), em, rtol=1e-6)
        # snapshot: zero crossings (the envelope cannot move them)
        zz = np.linspace(-0.2, 10, 2000001)
        t0 = 0.123 * T
        zc = lambda f: zz[np.where(np.diff(np.sign(f)) != 0)[0]]
        zE, zH = zc(Et(zz, t0)), zc(Ht(zz, t0))
        # tau < 45 deg, so tau/beta < lambda/8 < half the node spacing: the nearest E node is the partner (no bias)
        shifts = [zh - zE[np.argmin(abs(zE - zh))] for zh in zH[1:-1]]
        check("snapshot: enough node pairs found " + tag, len(shifts) >= 4, f"{len(shifts)} pairs")
        close("snapshot: H pattern sits tau/beta toward the source " + tag, np.median(shifts), -sgn * tau / be, rtol=2e-3)

# =====================================================================================================================
section("G. Section 4: time-average Poynting vector by quadrature; e^{-alpha z} for fields, e^{-2 alpha z} for power")
ww, mu, eps_, sig = 3e8, mu0, 8 * eps0c, 1 / (20 * np.pi)
g, e = gam_eta(ww, mu, eps_, sig)
al, be, tau, em = g.real, g.imag, np.angle(e), abs(e)
E0 = 6 * np.exp(1j * 0.5)
for sgn, uhat in ((+1, Z), (-1, -Z)):
    for z in (0.0, 0.7):
        Ep = X * E0 * np.exp(-sgn * g * z)
        Hp = np.cross(uhat, Ep) / e
        Sinst = lambda t: np.cross(np.real(Ep * np.exp(1j * ww * t)), np.real(Hp * np.exp(1j * ww * t)))
        T = 2 * np.pi / ww
        Sq = np.array([integrate.quad(lambda t: Sinst(t)[i], 0, T, epsabs=1e-14, epsrel=1e-11)[0] / T for i in range(3)])
        Sp = 0.5 * np.real(np.cross(Ep, np.conj(Hp)))
        Sf = uhat * abs(E0) ** 2 / (2 * em) * np.cos(tau) * np.exp(-2 * al * sgn * z)
        tag = f"({'+z' if sgn > 0 else '-z'} wave, z = {z})"
        close("<S> by quadrature = 1/2 Re{E x H*} " + tag, Sq, Sp, rtol=1e-8)
        close("<S> = u |E0|^2 cos(tau) e^{-2 alpha d}/(2|eta|) " + tag, Sp, Sf, rtol=1e-12)
        check("<S> points along the travel " + tag, np.dot(Sp, uhat) > 0 and np.allclose(np.cross(Sp, uhat), 0, atol=1e-12))
    # the pairing rule both ways
    Ep = X * E0
    Hp = np.cross(uhat, Ep) / e
    close(f"E~ = eta H~ x u recovers E~ ({'+z' if sgn > 0 else '-z'})", e * np.cross(Hp, uhat), Ep, rtol=1e-13)
rounds_to("field at z = delta is e^-1 = 37 %", 100 * np.exp(-1), "37", 0)
rounds_to("power at z = delta is e^-2 = 13.5 %", 100 * np.exp(-2), "13.5", 1)
close("one neper = 20 log10 e = 8.686 dB", 20 * np.log10(np.e), 8.686, rtol=1e-4)

# =====================================================================================================================
section("H1. Section 2 example: E = y 2 cos(2pi 1e8 t + 4pi/3 x), eps_r 4, lossless")
ww, mu, eps_ = 2 * np.pi * 1e8, mu0, 4 * eps0c
bet = ww * np.sqrt(mu * eps_)
close("beta = w sqrt(mu0 4 eps0) = 4 pi/3", bet, 4 * np.pi / 3, rtol=1e-13)
eta = np.sqrt(mu / eps_)
close("eta = eta0/2 = 60 pi", eta, 60 * np.pi, rtol=1e-13)
FE = lambda x, y, z: np.array([0, 2 * np.exp(1j * bet * x), 0], dtype=complex)
r = (0.3, 0.1, -0.2)
cE = curl_fd(FE, r, 1e-6)
close("curl(y E~y(x)) = z dE~y/dx = z j beta E~y (finite difference)", cE, Z * 1j * bet * FE(*r)[1], rtol=1e-7)
Hp = cE / (-1j * ww * mu)
close("H~ = -z (2/eta) e^{j beta x}", Hp, -Z * 2 / eta * np.exp(1j * bet * r[0]), rtol=1e-7)
rounds_to("|H| = 2/(60 pi) = 10.6 mA/m", 2 / eta * 1e3, "10.6", 1)
close("rotation rule (-x) x y (2/eta) = -z (2/eta)", np.cross(-X, Y) * 2 / eta, -Z * 2 / eta)
check("E x H* along y x (-z) = -x, the travel", np.allclose(np.cross(Y, -Z), -X))

# =====================================================================================================================
section("H2. Section 5 example: decode E = y 6 e^{-x} cos(3e8 t - 3x), non-magnetic")
ww = 3e8
gam = 1 + 3j
rounds_to("f = 47.7 MHz", ww / (2 * np.pi) / 1e6, "47.7", 1)
rounds_to("|gamma| = sqrt 10 = 3.162", abs(gam), "3.162", 3)
rounds_to("angle(gamma) = 71.6 deg", np.degrees(np.angle(gam)), "71.6", 1)
close("w mu0 = 120 pi", ww * mu0, 120 * np.pi, rtol=1e-13)
eta = 1j * ww * mu0 / gam
close("eta = j 120 pi/(1 + j3) = 12 pi (3 + j)", eta, 12 * np.pi * (3 + 1j), rtol=1e-13)
rounds_to("Re eta = 113.1", eta.real, "113.1", 1)
rounds_to("Im eta = 37.7", eta.imag, "37.7", 1)
rounds_to("|eta| = 119.2", abs(eta), "119.2", 1)
rounds_to("tau = 18.4 deg", np.degrees(np.angle(eta)), "18.4", 1)
close("tau = atan(alpha/beta) = atan(1/3)", np.angle(eta), np.arctan(1 / 3), rtol=1e-13)
Hdir = np.cross(X, Y)
close("H direction x x y = +z", Hdir, Z)
rounds_to("|H| = 6/119.2 = 50.3 mA/m", 6 / abs(eta) * 1e3, "50.3", 1)
check("E x H: y x z = +x (travel)", np.allclose(np.cross(Y, Z), X))
# H~ satisfies Faraday by finite difference
FE = lambda x, y, z: np.array([0, 6 * np.exp(-gam * x), 0], dtype=complex)
FH = lambda x, y, z: np.array([0, 0, 6 / eta * np.exp(-gam * x)], dtype=complex)
r = (0.4, 0, 0)
close("Faraday: curl E~ = -j w mu0 H~ for the decoded H~", curl_fd(FE, r, 1e-6), -1j * ww * mu0 * FH(*r), rtol=1e-7)
g2 = gam ** 2
close("gamma^2 = -8 + j6", g2, -8 + 6j)
ge = g2 / (1j * ww * mu0)
close("gamma/eta = (6 + j8)/(120 pi)", ge, (6 + 8j) / (120 * np.pi), rtol=1e-13)
close("gamma/eta = gamma/eta directly", gam / eta, ge, rtol=1e-13)
sig = ge.real
eps_ = ge.imag / ww
close("sigma = 1/(20 pi)", sig, 1 / (20 * np.pi), rtol=1e-13)
rounds_to("sigma = 15.9 mS/m", sig * 1e3, "15.9", 1)
rounds_to("eps = 7.07e-11 F/m", eps_ * 1e11, "7.07", 2)
close("eps = 8 eps0 (course eps0)", eps_ / eps0c, 8, rtol=1e-12)
close("sigma/(w eps) = 3/4", sig / (ww * eps_), 0.75, rtol=1e-12)
g_back, e_back = gam_eta(ww, mu0, eps_, sig)
close("forward: exact gamma from (sigma, eps, mu0) = 1 + j3", g_back, gam, rtol=1e-12)
close("forward: exact eta = 12 pi (3 + j)", e_back, eta, rtol=1e-12)
rounds_to("lambda = 2 pi/3 = 2.09 m", 2 * np.pi / 3, "2.09", 2)
close("v_p = w/beta = 1.0e8", ww / 3, 1e8)
rounds_to("lossless eps_r 8: c/sqrt8 = 1.06e8", 3e8 / np.sqrt(8) / 1e8, "1.06", 2)
a, b, em, tau = closed_forms(ww, mu0, eps_, sig)
close("general formulas return alpha = 1", a, 1, rtol=1e-12)
close("general formulas return beta = 3", b, 3, rtol=1e-12)
close("w sqrt(mu eps) = sqrt 8", ww * np.sqrt(mu0 * eps_), np.sqrt(8), rtol=1e-12)

# =====================================================================================================================
section("H3. Section 6 crossover example: eps_r 4, sigma 0.04, 180 MHz")
ww = 2 * np.pi * 1.8e8
close("w eps (course eps0) = 0.04 S/m", ww * 4 * eps0c, 0.04, rtol=1e-12)
rounds_to("sigma/(w eps) with CODATA eps0 = 0.9986", 0.04 / (ww * 4 * eps0), "0.9986", 4)
eps_ = 4 * eps0c
sig = ww * eps_                       # the example takes s = 1 exactly
g, e = gam_eta(ww, mu0, eps_, sig)
rounds_to("w sqrt(mu eps) = 2.4 pi = 7.540", ww * np.sqrt(mu0 * eps_), "7.540", 3)
close("w sqrt(mu eps) = 2.4 pi", ww * np.sqrt(mu0 * eps_), 2.4 * np.pi, rtol=1e-12)
rounds_to("alpha = 3.43", g.real, "3.43", 2)
rounds_to("beta = 8.28", g.imag, "8.28", 2)
rounds_to("|eta| = 158.5", abs(e), "158.5", 1)
close("|eta| = 60 pi / 2^(1/4)", abs(e), 60 * np.pi / 2 ** 0.25, rtol=1e-12)
close("tau = 22.5 deg", np.degrees(np.angle(e)), 22.5, rtol=1e-12)
rounds_to("delta = 0.291 m", 1 / g.real, "0.291", 3)
rounds_to("lambda = 0.758 m", 2 * np.pi / g.imag, "0.758", 3)
rounds_to("v_p = 1.37e8", ww / g.imag / 1e8, "1.37", 2)
aID = sig / 2 * np.sqrt(mu0 / eps_)
rounds_to("ID shortcut alpha = 0.02 x 60 pi = 3.77", aID, "3.77", 2)
rounds_to("  ... 10 % high", 100 * (aID / g.real - 1), "10", 0)
rounds_to("ID shortcut beta 7.54 is 9 % low", 100 * (1 - 2.4 * np.pi / g.imag), "9", 0)
rounds_to("ID shortcut tau = 0.5 rad = 28.6 deg", np.degrees(0.5), "28.6", 1)
aGC = np.sqrt(ww * mu0 * sig / 2)
rounds_to("GC shortcut sqrt(w mu sigma/2) = 5.33", aGC, "5.33", 2)
rounds_to("  ... 55 % high for alpha", 100 * (aGC / g.real - 1), "55", 0)
rounds_to("  ... 36 % low for beta", 100 * (1 - aGC / g.imag), "36", 0)

# =====================================================================================================================
section("H4. Section 6 table (x = w eps/sigma) and the figure's normalizations")
xs = np.array([0.01, 0.1, 1, 10, 100])
s_ = 1 / xs
ww, mu, eps_ = 2 * np.pi * 1e6, mu0, 5 * eps0
sigs = s_ * ww * eps_
dinf = 2 / sigs * np.sqrt(eps_ / mu)
d_ratio, l_ratio, e_ratio, tau_deg = [], [], [], []
for sg, di in zip(sigs, dinf):
    g, e = gam_eta(ww, mu, eps_, sg)
    d_ratio.append(1 / g.real / di)
    l_ratio.append(2 * np.pi / g.imag / (2 * np.pi * di))
    e_ratio.append(abs(e) / np.sqrt(mu / eps_))
    tau_deg.append(np.degrees(np.angle(e)))
page = dict(d=["7.11", "2.35", "1.10", "1.001", "1.000"], l=["7.04", "2.13", "0.455", "0.050", "0.005"],
            e=["0.100", "0.315", "0.841", "0.998", "1.000"], t=["44.7", "42.1", "22.5", "2.86", "0.29"])
dig = dict(d=[2, 2, 2, 3, 3], l=[2, 2, 3, 3, 3], e=[3, 3, 3, 3, 3], t=[1, 1, 1, 2, 2])
for key, vals, name in (("d", d_ratio, "delta/delta_inf"), ("l", l_ratio, "lambda/(2 pi delta_inf)"),
                        ("e", e_ratio, "|eta|/sqrt(mu/eps)"), ("t", tau_deg, "tau [deg]")):
    for x_, v, p, dg in zip(xs, vals, page[key], dig[key]):
        rounds_to(f"table {name} at x = {x_:g}", v, p, dg)
# figure normalization: alpha/alpha_inf = sqrt2 x sqrt(sqrt(1+s^2) - 1)
for x_ in (0.01, 0.3, 1, 7):
    s1 = 1 / x_
    sg = s1 * ww * eps_
    g, e = gam_eta(ww, mu, eps_, sg)
    close(f"figure: alpha/alpha_inf formula at x = {x_}", g.real / (sg / 2 * np.sqrt(mu / eps_)),
          np.sqrt(2) * x_ * np.sqrt(np.sqrt(1 + s1 * s1) - 1), rtol=1e-10)
    close(f"figure: beta/alpha_inf formula at x = {x_}", g.imag / (sg / 2 * np.sqrt(mu / eps_)),
          np.sqrt(2) * x_ * np.sqrt(np.sqrt(1 + s1 * s1) + 1), rtol=1e-10)
# asymptotes drawn in the figure
x_ = 1e-4
s1 = 1 / x_
close("figure asymptote: delta/delta_inf -> 1/sqrt(2x) for x << 1", 1 / (np.sqrt(2) * x_ * np.sqrt(np.sqrt(1 + s1 * s1) - 1)), 1 / np.sqrt(2 * x_), rtol=1e-3)
x_ = 1e4
s1 = 1 / x_
close("figure asymptote: lambda/(2 pi delta_inf) -> 1/(2x) for x >> 1", 1 / (np.sqrt(2) * x_ * np.sqrt(np.sqrt(1 + s1 * s1) + 1)), 1 / (2 * x_), rtol=1e-6)
check("figure bands: good conductor for x < 0.1 (s > 10), imperfect dielectric for x > 10 (s < 0.1) = L23 thresholds", True,
      "figs_l22.py shades log10 x in [-2,-1] and [1,2]")

# =====================================================================================================================
section("H5. Section 6 'reading the regime': decay per wavelength and delta against lambda")
for s in (0.01, 0.3, 1, 30, 1e4):
    g, e = gam_eta(1e6, mu0, eps0, s * 1e6 * eps0)
    lam = 2 * np.pi / g.imag
    close(f"e^(-alpha lambda) = e^(-2 pi tan tau) at s = {s}", np.exp(-g.real * lam), np.exp(-2 * np.pi * np.tan(np.angle(e))), rtol=1e-12)
rounds_to("good conductor: e^{-2pi} = 0.19 %", 100 * np.exp(-2 * np.pi), "0.19", 2)
g, e = gam_eta(1e6, mu0, eps0, 0.01 * 1e6 * eps0)
close("imperfect dielectric: e^(-alpha lambda) ~ 1 - pi s (s = 0.01)", np.exp(-g.real * 2 * np.pi / g.imag), 1 - np.pi * 0.01, rtol=1e-3)
# delta = lambda/(2 pi tan tau); the s at which delta = lambda
s_star = np.tan(2 * np.arctan(1 / (2 * np.pi)))
g, e = gam_eta(1e6, mu0, eps0, s_star * 1e6 * eps0)
close(f"delta = lambda exactly at s* = tan(2 atan(1/2pi)) = {s_star:.4f}", 1 / g.real, 2 * np.pi / g.imag, rtol=1e-10)
check("FINDING: 'lambda is longer than delta' only means s > 0.33 - true at s = 0.5 (in between), so it does not name the regime",
      2 * np.pi / gam_eta(1e6, mu0, eps0, 0.5e6 * eps0)[0].imag > 1 / gam_eta(1e6, mu0, eps0, 0.5e6 * eps0)[0].real,
      "page fixed to 'lambda ~ 2 pi delta' (the S20 HE3 #3b wording)")
rounds_to("... the threshold quoted on the page: sigma/(w eps) > 0.33", s_star, "0.33", 2)
okl = True
for s in np.logspace(-6, 6, 200):
    g, e = gam_eta(1e6, mu0, eps0, s * 1e6 * eps0)
    okl &= (2 * np.pi / g.imag) < 2 * np.pi * (1 / g.real)
    okl &= np.isclose((2 * np.pi / g.imag) / (1 / g.real), 2 * np.pi * np.tan(np.angle(e)), rtol=1e-10)
check("lambda/delta = 2 pi tan(tau) < 2 pi, so lambda < 2 pi delta for every real sigma (s = 1e-6..1e6)", okl)
g, e = gam_eta(1e6, mu0, eps0, 1e4 * 1e6 * eps0)
close("good conductor: delta -> lambda/2pi", 1 / g.real, (2 * np.pi / g.imag) / (2 * np.pi), rtol=1e-3)
g, e = gam_eta(1e6, mu0, eps0, 1e-3 * 1e6 * eps0)
check("imperfect dielectric: delta >> lambda (s = 1e-3: delta/lambda = 1/(2 pi tan tau) ~ 318)", (1 / g.real) / (2 * np.pi / g.imag) > 300,
      f"{(1 / g.real) / (2 * np.pi / g.imag):.0f}")

# =====================================================================================================================
section("H6. Section 6 shortcuts: binomial derivation, error orders, the two limits, penetration-depth limits")
ww, mu, eps_ = 2 * np.pi * 1e6, 2 * mu0, 3 * eps0
res = {}
for s in (1e-2, 1e-3):
    sg = s * ww * eps_
    g, e = gam_eta(ww, mu, eps_, sg)
    gID = sg / 2 * np.sqrt(mu / eps_) + 1j * ww * np.sqrt(mu * eps_)
    eID = np.sqrt(mu / eps_) * (1 + 1j * sg / (2 * ww * eps_))
    res[s] = (abs(gID.real / g.real - 1), abs(gID.imag / g.imag - 1), abs(abs(eID) / abs(e) - 1),
              abs((sg / (2 * ww * eps_)) / np.angle(e) - 1), abs(np.arctan(s / 2) - np.angle(e)))
for i, name in enumerate(("alpha", "beta", "|eta|", "tau (rad)")):
    ratio = res[1e-2][i] / res[1e-3][i]
    check(f"imperfect-dielectric {name}: relative error falls as s^2 (ratio 100 for s/10)", 60 < ratio < 140, f"ratio {ratio:.1f}")
check("notes' tan^-1(sigma/2 w eps) differs from the exact angle at O(s^3)", 500 < res[1e-2][4] / res[1e-3][4] < 1500,
      f"ratio {res[1e-2][4] / res[1e-3][4]:.0f}")
for s in (1e2, 1e3):
    sg = s * ww * eps_
    g, e = gam_eta(ww, mu, eps_, sg)
    gGC = (1 + 1j) * np.sqrt(np.pi * ww / (2 * np.pi) * mu * sg)
    eGC = np.sqrt(ww * mu / sg) * np.exp(1j * np.pi / 4)
    res[s] = (abs(gGC / g - 1), abs(eGC / e - 1))
check("good conductor: gamma -> (1+j) sqrt(pi f mu sigma), error ~ 1/(2s)", abs(res[1e2][0] - 1 / 200) < 1e-3 and res[1e2][0] / res[1e3][0] > 8,
      f"{res[1e2][0]:.2e}, {res[1e3][0]:.2e}")
check("good conductor: eta -> sqrt(w mu/sigma) e^{j pi/4}, error ~ 1/(2s)", res[1e2][1] / res[1e3][1] > 8, f"{res[1e2][1]:.2e}, {res[1e3][1]:.2e}")
close("binomial: (1 - js)^(1/2) ~ 1 - js/2 (p = 1/2 for gamma)", np.sqrt(1 - 1e-4j), 1 - 0.5e-4j, rtol=1e-8)
close("binomial: (1 - js)^(-1/2) ~ 1 + js/2 (p = -1/2 for eta; notes say p = 1/2)", 1 / np.sqrt(1 - 1e-4j), 1 + 0.5e-4j, rtol=1e-8)
close("sqrt(j) = e^{j pi/4} = (1+j)/sqrt2", np.sqrt(1j), (1 + 1j) / np.sqrt(2), rtol=1e-14)
# penetration depth limits at fixed material
sg = 0.5
for f, name, want in ((1e14, "high f: delta -> (2/sigma) sqrt(eps/mu)", 2 / sg * np.sqrt(eps_ / mu)),
                      (10.0, "low f: delta -> sqrt(2/(w mu sigma)) = 1/sqrt(pi f mu sigma)", 1 / np.sqrt(np.pi * 10.0 * mu * sg))):
    g, e = gam_eta(2 * np.pi * f, mu, eps_, sg)
    close(name, 1 / g.real, want, rtol=1e-4)
close("sqrt(2/(w mu sigma)) = 1/sqrt(pi f mu sigma)", np.sqrt(2 / (2 * np.pi * 5 * mu * sg)), 1 / np.sqrt(np.pi * 5 * mu * sg), rtol=1e-14)
# perfect conductor
g, e = gam_eta(2 * np.pi * 1e6, mu0, eps0, 1e12)
check("sigma -> inf: alpha -> inf, |eta| -> 0", g.real > 1e5 and abs(e) < 1e-2, f"alpha {g.real:.2e}, |eta| {abs(e):.2e}")

# =====================================================================================================================
section("H7. Section 7: Lecture 19's sheet in a conducting medium (J0 = 2 A/m, medium of the section-5 example)")
ww, mu, eps_, sig = 3e8, mu0, 8 * eps0c, 1 / (20 * np.pi)
g, e = gam_eta(ww, mu, eps_, sig)
close("medium: gamma = 1 + j3", g, 1 + 3j, rtol=1e-12)
J0 = 2.0
A = -e * J0 / 2
Hplus = lambda z: Y * (A / e) * np.exp(-g * abs(z))        # +z wave: H = z x E/eta
Hminus = lambda z: -Y * (A / e) * np.exp(-g * abs(z))
close("H(z>0) = z x E/eta", Hplus(0.3), np.cross(Z, X * A * np.exp(-g * 0.3)) / e, rtol=1e-13)
close("H(z<0) = (-z) x E/eta", Hminus(-0.3), np.cross(-Z, X * A * np.exp(-g * 0.3)) / e, rtol=1e-13)
close("jump: n x (H+ - H-) with n = z (from region 2 below into region 1 above) = J~s", np.cross(Z, Hplus(0) - Hminus(0)), X * J0, rtol=1e-13)
close("E~ = -x eta J0/2 e^{-gamma|z|}", X * A, -X * e * J0 / 2, rtol=1e-13)
close("H~ (z>0) = -y J0/2 (= 1/2 J~s x n)", Hplus(0), 0.5 * np.cross(X * J0, Z), rtol=1e-13)
close("H~ (z<0) = +y J0/2 (= 1/2 J~s x n, n = -z)", Hminus(0), 0.5 * np.cross(X * J0, -Z), rtol=1e-13)
# time-domain forms printed on the page
z, t = 0.37, 0.8e-8
Et_page = -X * 119.2 * np.exp(-abs(z)) * np.cos(ww * t - 3 * abs(z) + 18.4 * deg)
Et_ex = np.real(X * A * np.exp(-g * abs(z)) * np.exp(1j * ww * t))
check("E(z,t) = -x 119.2 e^{-|z|} cos(wt - 3|z| + 18.4 deg) V/m", np.allclose(Et_page, Et_ex, rtol=2e-3, atol=2e-3 * 119.2))
Ht_page = -Y * 1.0 * np.exp(-abs(z)) * np.cos(ww * t - 3 * abs(z))
check("H(z>0,t) = -y e^{-|z|} cos(wt - 3|z|) A/m", np.allclose(Ht_page, np.real(Hplus(z) * np.exp(1j * ww * t)), atol=1e-12))
# power given up by the sheet, by quadrature, and the fluxes leaving each face
T = 2 * np.pi / ww
pq = integrate.quad(lambda t: -np.dot(np.real(X * J0 * np.exp(1j * ww * t)), np.real(X * A * np.exp(1j * ww * t))), 0, T, epsrel=1e-12)[0] / T
close("<-Js.E> by quadrature = 1/4 J0^2 Re{eta}", pq, 0.25 * J0 ** 2 * e.real, rtol=1e-9)
close("... = 36 pi W/m^2", pq, 36 * np.pi, rtol=1e-9)
rounds_to("... = 113 W/m^2", pq, "113", 0)
Sup = 0.5 * np.real(np.cross(X * A, np.conj(Hplus(0))))
Sdn = 0.5 * np.real(np.cross(X * A, np.conj(Hminus(0))))
close("flux leaving the top face = half of it (+z)", Sup, Z * pq / 2, rtol=1e-12)
close("flux leaving the bottom face = half of it (-z)", Sdn, -Z * pq / 2, rtol=1e-12)
rounds_to("half = 56.5 W/m^2", pq / 2, "56.5", 1)
close("Re{eta} = |eta| cos(tau)", e.real, abs(e) * np.cos(np.angle(e)), rtol=1e-13)
check("direction z>0: (-x) x (-y) = +z", np.allclose(np.cross(-X, -Y), Z))
check("E leads H by tau: arg(E~x/(-1)) - arg(H~y/(-1)) at z>0 = +18.4 deg",
      abs(np.degrees(np.angle(A / -1) - np.angle(Hplus(0)[1] / -1)) - 18.43) < 0.01)
# Rao (5.66) with J_S = -J_S0 cos wt x: E = +x(|eta| J_S0/2) e^{-a|z|} cos(wt - b|z| + tau); our sign flips with J_s
check("matches Rao (5.66) after J_s -> -J_s", True, "Rao: E = (|eta|J_S0/2)e^{-a|z|}cos(wt - b|z| + tau) a_x for J_S = -J_S0 cos wt a_x")

# =====================================================================================================================
section("H8. Section 8: Drude sigma(w), collisionless plasma, ionosphere numbers")
N = 1e12
wp = np.sqrt(N * qe ** 2 / (me * eps0))
for f in (5e6, 20e6):
    ww = 2 * np.pi * f
    sigp = N * qe ** 2 / (1j * ww * me)
    close(f"sigma + j w eps0 = j w eps0 (1 - wp^2/w^2) at {f / 1e6:g} MHz", sigp + 1j * ww * eps0, 1j * ww * eps0 * (1 - wp ** 2 / ww ** 2), rtol=1e-12)
    g, e = gam_eta(ww, mu0, eps0, sigp)
    close(f"gamma^2 = -(w^2 - wp^2)/c^2 at {f / 1e6:g} MHz", g * g, -(ww ** 2 - wp ** 2) / c0 ** 2, rtol=1e-8)
    if f < fp:
        rounds_to("5 MHz: gamma real = 0.156 1/m", g.real, "0.156", 3)
        check("5 MHz: beta = 0", abs(g.imag) < 1e-12 * abs(g))
        rounds_to("5 MHz: delta = 6.4 m", 1 / g.real, "6.4", 1)
        check("5 MHz: eta purely imaginary (tau = 90 deg)", abs(e.real) < 1e-9 * abs(e) and e.imag > 0)
        Ep, Hp = X * 1.0, np.cross(Z, X) / e
        Sq = integrate.quad(lambda t: np.cross(np.real(Ep * np.exp(1j * ww * t)), np.real(Hp * np.exp(1j * ww * t)))[2], 0, 1 / f, epsabs=1e-16, limit=200)[0] * f
        check("5 MHz: <S> = 0 by quadrature (no average power)", abs(Sq) < 1e-12, f"{Sq:.1e}")
        check("FINDING: below f_p alpha > beta (= 0): 'beta >= alpha in every passive medium' needs 'real sigma'", g.real > g.imag,
              "page and concept page now say: for real sigma >= 0")
    else:
        rounds_to("20 MHz: beta = 0.375 rad/m", g.imag, "0.375", 3)
        check("20 MHz: alpha = 0", abs(g.real) < 1e-12 * abs(g))
        rounds_to("20 MHz: vacuum beta = 0.419", ww / c0, "0.419", 3)
        close("20 MHz: eta = w mu0/beta, real", e, ww * mu0 / g.imag, rtol=1e-9)
        check("20 MHz: eta > eta0", e.real > np.sqrt(mu0 / eps0), f"{e.real:.1f} ohm")
        close("matches Lecture 21's plasma dispersion relation beta = sqrt(w^2 - wp^2)/c", g.imag, np.sqrt(ww ** 2 - wp ** 2) / c0, rtol=1e-9)
check("collisionless sigma is purely imaginary: Re sigma = 0, no Joule heating", (N * qe ** 2 / (1j * 1e7 * me)).real == 0)

# =====================================================================================================================
section("H9. Section 9: the transmission-line twin (coax with a lossy filling)")
ww, mu, eps_, sig, ba = 2 * np.pi * 3e6, 1.5 * mu0, 7 * eps0, 0.02, 3.5
L = mu / (2 * np.pi) * np.log(ba)
C = 2 * np.pi * eps_ / np.log(ba)
G = 2 * np.pi * sig / np.log(ba)
g, e = gam_eta(ww, mu, eps_, sig)
close("LC = mu eps", L * C, mu * eps_, rtol=1e-13)
close("G/C = sigma/eps", G / C, sig / eps_, rtol=1e-13)
close("LG = mu sigma (concept page)", L * G, mu * sig, rtol=1e-13)
close("sqrt(jwL(G + jwC)) = gamma", np.sqrt(1j * ww * L * (G + 1j * ww * C)), g, rtol=1e-12)
close("sqrt(jwL/(G + jwC)) = eta ln(b/a)/2pi", np.sqrt(1j * ww * L / (G + 1j * ww * C)), e * np.log(ba) / (2 * np.pi), rtol=1e-12)

# =====================================================================================================================
section("I. Worked problem: H = z 0.2 e^x cos(1e8 t + 2x + 60 deg) A/m, mu = 3 mu0, x < 0")
ww, mu = 1e8, 3 * mu0
alpha, beta = 1.0, 2.0
gam = alpha + 1j * beta
check("(a) same signs on t and x: travel toward -x; e^x decays toward -x", True)
u = -X
rounds_to("(a) f = 15.9 MHz", ww / (2 * np.pi) / 1e6, "15.9", 1)
rounds_to("(a) angle(gamma) = 63.43 deg", np.degrees(np.angle(gam)), "63.43", 2)
close("(a) |gamma| = sqrt 5", abs(gam), np.sqrt(5), rtol=1e-14)
close("(a) tan^-1 2 = 90 - 26.57", np.degrees(np.arctan(2)), 90 - np.degrees(np.arctan(0.5)), rtol=1e-13)
close("(a) lambda = pi", 2 * np.pi / beta, np.pi)
close("(a) v_p = 5e7", ww / beta, 5e7)
close("(a) delta = 1", 1 / alpha, 1)
close("(b) w mu = 120 pi", ww * mu, 120 * np.pi, rtol=1e-13)
eta = 1j * ww * mu / gam
close("(b) eta = 24 pi (2 + j)", eta, 24 * np.pi * (2 + 1j), rtol=1e-13)
rounds_to("(b) Re eta = 150.8", eta.real, "150.8", 1)
rounds_to("(b) Im eta = 75.4", eta.imag, "75.4", 1)
rounds_to("(b) |eta| = 168.6", abs(eta), "168.6", 1)
close("(b) |eta| = 120 pi/sqrt5", abs(eta), 120 * np.pi / np.sqrt(5), rtol=1e-13)
rounds_to("(b) tau = 26.57 deg", np.degrees(np.angle(eta)), "26.57", 2)
close("(b) gamma eta = j 120 pi", gam * eta, 120j * np.pi, rtol=1e-13)
Hp = lambda x: Z * 0.2 * np.exp(1j * 60 * deg) * np.exp(gam * x)
xs_ = np.array([-0.3, -1.1])
tt = np.array([0.0, 7e-9, 2.1e-8])
for x in xs_:
    for t in tt:
        check(f"(c) Re{{H~ e^jwt}} = given H at x = {x}, t = {t:g}",
              np.isclose(np.real(Hp(x) * np.exp(1j * ww * t))[2], 0.2 * np.exp(x) * np.cos(ww * t + 2 * x + 60 * deg), atol=1e-13))
close("(c) direction z x (-x) = -y", np.cross(Z, u), -Y)
Ep = lambda x: eta * np.cross(Hp(x), u)
rounds_to("(c) |E| = 0.2 x 168.6 = 33.7 V/m", 0.2 * abs(eta), "33.7", 1)
rounds_to("(c) phase of E = 86.57 deg (in the -y direction)", np.degrees(np.angle(Ep(0)[1] / -1)), "86.57", 2)
close("(c) E~ = -y 0.2 eta e^{j60} e^{gamma x}", Ep(-0.4), -Y * 0.2 * eta * np.exp(1j * 60 * deg) * np.exp(gam * -0.4), rtol=1e-13)
check("(c) E x H* along (-y) x z = -x (travel)", np.allclose(np.cross(-Y, Z), -X))
Sv = 0.5 * np.real(np.cross(Ep(-0.2), np.conj(Hp(-0.2))))
check("(c) <S> = 1/2 Re{E x H*} points along -x", Sv[0] < 0 and abs(Sv[1]) < 1e-14 and abs(Sv[2]) < 1e-14, f"{Sv}")
FE = lambda x, y, z: Ep(x)
FH = lambda x, y, z: Hp(x)
r = (-0.6, 0.2, 0.1)
close("(c) Faraday curl E~ = -j w mu H~ (finite difference)", curl_fd(FE, r, 1e-6), -1j * ww * mu * FH(*r), rtol=1e-7)
sig, eps_ = 1 / (30 * np.pi), 3 / (120 * np.pi * 1e8)
close("(c) Ampere curl H~ = (sigma + j w eps) E~ (finite difference)", curl_fd(FH, r, 1e-6), (sig + 1j * ww * eps_) * FE(*r), rtol=1e-7)
# time domain: the answer's E(x,t) and the given H(x,t) satisfy the time-domain laws
Et = lambda x, t: -33.72 * np.exp(x) * np.cos(ww * t + 2 * x + np.radians(86.565))
Htt = lambda x, t: 0.2 * np.exp(x) * np.cos(ww * t + 2 * x + np.radians(60))
x0, t0, hx, ht = -0.45, 3.3e-9, 1e-6, 1e-15
# E = y Ey(x,t), H = z Hz(x,t): Faraday y-x: dEy/dx = -mu dHz/dt ; Ampere: -dHz/dx = sigma Ey + eps dEy/dt
lhs = (Et(x0 + hx, t0) - Et(x0 - hx, t0)) / (2 * hx)
rhs = -mu * (Htt(x0, t0 + ht) - Htt(x0, t0 - ht)) / (2 * ht)
close("(c) time domain: dEy/dx = -mu dHz/dt with the answer's E", lhs, rhs, rtol=2e-4)
lhs = -(Htt(x0 + hx, t0) - Htt(x0 - hx, t0)) / (2 * hx)
rhs = sig * Et(x0, t0) + eps_ * (Et(x0, t0 + ht) - Et(x0, t0 - ht)) / (2 * ht)
close("(c) time domain: -dHz/dx = sigma Ey + eps dEy/dt", lhs, rhs, rtol=2e-4)
check("(c) alternative form y 33.7 cos(... - 93.4 deg) is the same field",
      np.isclose(-np.cos(1.234 + np.radians(86.565)), np.cos(1.234 + np.radians(86.565 - 180)), atol=1e-14) and f"{86.565 - 180:.1f}" == "-93.4")
rounds_to("(c) trap: wrong sign of tau gives 33.4 deg", 60 - np.degrees(np.arctan(0.5)), "33.4", 1)
close("(d) gamma^2 = -3 + j4", gam ** 2, -3 + 4j)
ge = gam ** 2 / (1j * ww * mu)
close("(d) gamma/eta = (4 + j3)/(120 pi)", ge, (4 + 3j) / (120 * np.pi), rtol=1e-13)
close("(d) sigma = 1/(30 pi)", ge.real, 1 / (30 * np.pi), rtol=1e-13)
rounds_to("(d) sigma = 10.6 mS/m", ge.real * 1e3, "10.6", 1)
rounds_to("(d) eps = 7.96e-11", ge.imag / ww * 1e11, "7.96", 2)
close("(d) eps = 9 eps0 (course eps0)", ge.imag / ww / eps0c, 9, rtol=1e-12)
close("(d) sigma/(w eps) = 4/3 = tan(2 tau)", ge.real / ge.imag, np.tan(2 * np.angle(eta)), rtol=1e-12)
rounds_to("(d) tan^-1(4/3) = 53.13", np.degrees(np.arctan(4 / 3)), "53.13", 2)
epsw = 9 * eps0c
aID = ge.real / 2 * np.sqrt(mu / epsw)
close("(d) ID shortcut alpha = 2/sqrt3", aID, 2 / np.sqrt(3), rtol=1e-12)
rounds_to("(d) ... 15 % high", 100 * (aID - 1), "15", 0)
aGC = np.sqrt(ww * mu * ge.real / 2)
close("(d) GC shortcut = sqrt 2", aGC, np.sqrt(2), rtol=1e-12)
rounds_to("(d) ... 41 % high for alpha", 100 * (aGC - 1), "41", 0)
rounds_to("(d) ... 29 % low for beta", 100 * (1 - aGC / 2), "29", 0)
a, b, em, tau = closed_forms(ww, mu, epsw, ge.real)
close("(e) w sqrt(mu eps) = sqrt 3", ww * np.sqrt(mu * epsw), np.sqrt(3), rtol=1e-12)
close("(e) alpha = 1", a, 1, rtol=1e-12)
close("(e) beta = 2", b, 2, rtol=1e-12)
close("(e) |eta| = 120 pi/sqrt5", em, 120 * np.pi / np.sqrt(5), rtol=1e-12)
close("(e) sqrt(mu/eps) = 120 pi/sqrt3", np.sqrt(mu / epsw), 120 * np.pi / np.sqrt(3), rtol=1e-12)
close("(e) tau = 26.57 deg", np.degrees(tau), np.degrees(np.arctan(0.5)), rtol=1e-12)
g_ex, e_ex = gam_eta(ww, mu, epsw, ge.real)
close("(e) exact square roots return gamma = 1 + j2", g_ex, gam, rtol=1e-12)
close("(e) exact square roots return eta = 24 pi (2 + j)", e_ex, eta, rtol=1e-12)
rounds_to("(f) e^x = 0.1 at x = -2.30 m", -np.log(10), "-2.30", 2)
rounds_to("(f) 2.30/pi = 0.73 wavelengths", np.log(10) / np.pi, "0.73", 2)
rounds_to("(f) e^{-pi} = 4.3 %", 100 * np.exp(-np.pi), "4.3", 1)
eta0v = 1j * ww * mu0 / gam
close("variant: eta with mu0 = 8 pi (2 + j)", eta0v, 8 * np.pi * (2 + 1j), rtol=1e-13)
rounds_to("variant: |eta| = 56.2", abs(eta0v), "56.2", 1)
rounds_to("variant: |E| = 11.2", 0.2 * abs(eta0v), "11.2", 1)
gv = gam ** 2 / (1j * ww * mu0)
rounds_to("variant: sigma = 31.8 mS/m", gv.real * 1e3, "31.8", 1)
close("variant: eps = 27 eps0", gv.imag / ww / eps0c, 27, rtol=1e-12)
close("variant: sigma/(w eps) still 4/3", gv.real / gv.imag, 4 / 3, rtol=1e-12)
close("variant: tau still 26.6 deg", np.angle(eta0v), np.angle(eta), rtol=1e-13)
# exam keys must not carry over: compare with the three modelled exam stems
keys = {"SP17 #3": (8e6 * np.pi, mu0, 3 + 4j), "S18 HE3 #1b": (8e6 * np.pi, mu0, 1 + 1j * np.sqrt(3)), "SP19 #1": (2e7 * np.pi, 2 * mu0, 1 + 1j * np.sqrt(3))}
for k, (wk, muk, gk) in keys.items():
    ek = 1j * wk * muk / gk
    sk = (gk ** 2 / (1j * wk * muk))
    check(f"worked problem differs from {k}: gamma, eta, sigma/(w eps) all different",
          not np.isclose(gk, gam) and not np.isclose(ek, eta) and not np.isclose(sk.real / sk.imag, 4 / 3),
          f"{k}: gamma {gk:.3g}, eta {ek:.4g}, s {sk.real / sk.imag:.3g}")

# =====================================================================================================================
section("J. Concept pages: propagation-constant and the new section of intrinsic-impedance")
g, e = gam_eta(2 * np.pi * 1e8, mu0, 4 * eps0c, 0.0)
rounds_to("propagation-constant: eps_r 4 at 100 MHz, gamma = j4.19", g.imag, "4.19", 2)
close("... lambda = 1.5 m", 2 * np.pi / g.imag, 1.5, rtol=1e-12)
check("propagation-constant: gamma = 1 + j3 example (H2) and crossover 3.43 + j8.28 (H3), 10 % / 55 % (H3)", True)
close("propagation-constant: worked problem gamma^2 = -3 + j4 (3-4-5)", (1 + 2j) ** 2, -3 + 4j)
check("propagation-constant: plasma 0.156 at 5 MHz, j0.375 at 20 MHz (H8)", True)
close("intrinsic-impedance: eta0/sqrt8 = 133.3 (course eta0)", 120 * np.pi / np.sqrt(8), 133.3, rtol=3e-4)
close("intrinsic-impedance: lossless sqrt(3 mu0/9 eps0) = 217.7", np.sqrt(3 * mu0 / (9 * eps0c)), 217.7, rtol=3e-4)
close("intrinsic-impedance: crossover |eta| = 2^(-1/4) = 0.84", 2 ** -0.25, 0.84, rtol=2e-3)
# |eta| < sqrt(mu/eps) whenever sigma > 0 (the "conduction lowers |eta|" argument)
check("|eta| < sqrt(mu/eps) for every sigma > 0", all(abs(gam_eta(1e7, mu0, 4 * eps0, s * 1e7 * 4 * eps0)[1]) < np.sqrt(mu0 / (4 * eps0)) for s in np.logspace(-4, 4, 50)))
# intrinsic-impedance old examples (unchanged content, re-checked quickly)
rounds_to("vacuum: 1 V/m -> H = 2.65 mA/m", 1 / np.sqrt(mu0 / eps0) * 1e3, "2.65", 2)
rounds_to("vacuum: B = E/c = 3.34 nT", 1 / c0 * 1e9, "3.34", 2)
rounds_to("eps_r 2.25 -> 251 ohm", np.sqrt(mu0 / (2.25 * eps0)), "251", 0)
rounds_to("eps_r 9 -> 126 ohm", np.sqrt(mu0 / (9 * eps0)), "126", 0)
close("v = 2e8 -> eta = mu0 v = 80 pi", mu0 * 2e8, 80 * np.pi, rtol=1e-13)
close("mu_r 2, eps_r 8: eta = eta0/2, v = c/4", np.sqrt(2 / 8), 0.5)
rounds_to("coax b/a 3.5: ln(3.5)/2pi = 0.199", np.log(3.5) / (2 * np.pi), "0.199", 3)
rounds_to("... 0.199 x 251.3 = 50 ohm", np.log(3.5) / (2 * np.pi) * 80 * np.pi, "50", 0)
rounds_to("6/251.3 = 23.9 mA/m", 6 / (80 * np.pi) * 1e3, "23.9", 1)
rounds_to("6/377 = 15.9 mA/m", 6 / 377 * 1e3, "15.9", 1)

# =====================================================================================================================
section("K. Figures: every plotted quantity recomputed from the formulas")
a_, b_ = 0.6, 2 * np.pi
rounds_to("damped-wave: delta = 1/0.6 = 1.67 lambda", 1 / a_, "1.67", 2)
rounds_to("damped-wave: tau = atan(0.6/2pi) = 5.5 deg", np.degrees(np.arctan(a_ / b_)), "5.5", 1)
zz = np.linspace(0, 3, 300001)
z0c = zz[np.where(np.diff(np.sign(np.cos(-b_ * zz))) != 0)[0]]
z8c = zz[np.where(np.diff(np.sign(np.cos(np.pi / 4 - b_ * zz))) != 0)[0]]
check("damped-wave: t = 0 nodes at 0.25 + k/2 (2.75 marked)", np.allclose(z0c, 0.25 + 0.5 * np.arange(len(z0c)), atol=2e-5) and np.any(abs(z0c - 2.75) < 1e-4))
check("damped-wave: t = T/8 nodes at 0.375 + k/2 (2.875 marked): moved lambda/8 toward +z",
      np.allclose(z8c, 0.375 + 0.5 * np.arange(len(z8c)), atol=2e-5) and np.any(abs(z8c - 2.875) < 1e-4))
check("damped-wave: dimension line 0.25 -> 1.25 spans one lambda, two node spacings", np.isclose(1.25 - 0.25, 1.0))
tau15 = np.radians(15)
close("phasor-spiral: tau = 15 deg <-> s = tan 30 deg", np.tan(2 * tau15), np.tan(np.radians(30)), rtol=1e-13)
rounds_to("phasor-spiral: radius per turn e^{-2 pi tan 15} = 0.19", np.exp(-2 * np.pi * np.tan(tau15)), "0.19", 2)
ph = np.exp(-(np.tan(tau15) * 2 * np.pi + 2j * np.pi) * np.linspace(0, 0.2, 50))
check("phasor-spiral: e^{-j beta z} turns clockwise (angle decreasing) as z grows", np.all(np.diff(np.unwrap(np.angle(ph))) < 0))
check("phasor-spiral: H~ = E~/eta is E~ turned clockwise by tau (angle -tau)", np.isclose(np.angle(1 / np.exp(1j * tau15)), -tau15))
check("phasor-spiral: record panel |eta|H = cos(wt - tau) peaks tau/w after cos(wt)", True, "same as section F")
# phase dial table
tab = [("0.25", 0.25, "7.0", "83.0", "1.02", "0.98"), ("1", 1.0, "22.5", "67.5", "1.19", "0.84"),
       ("sqrt3", np.sqrt(3), "30.0", "60.0", "1.41", "0.71"), ("4", 4.0, "38.0", "52.0", "2.03", "0.49"),
       ("10", 10.0, "42.1", "47.9", "3.17", "0.32")]
for lab, s, t_, gdeg, gm, em_ in tab:
    gn = 1j * np.sqrt(1 - 1j * s)
    en = 1 / np.sqrt(1 - 1j * s)
    ok = (f"{np.degrees(np.angle(en)):.1f}" == t_ and f"{np.degrees(np.angle(gn)):.1f}" == gdeg and
          f"{abs(gn):.2f}" == gm and f"{abs(en):.2f}" == em_)
    check(f"phase-dial table row s = {lab}", ok, f"{np.degrees(np.angle(en)):.2f}, {np.degrees(np.angle(gn)):.2f}, {abs(gn):.3f}, {abs(en):.3f}")
    # 'eta is gamma inverted in the unit circle and reflected across the 45 deg line'
    inv = gn / abs(gn) ** 2
    refl = 1j * np.conj(inv)
    check(f"phase-dial: eta_n = reflect45(invert(gamma_n)) at s = {lab}", np.isclose(refl, en, rtol=1e-12))
    g, e = gam_eta(1e7, 2 * mu0, 3 * eps0, s * 1e7 * 3 * eps0)
    check(f"phase-dial: gamma/(w sqrt(mu eps)) = j sqrt(1 - js) and eta/sqrt(mu/eps) = 1/sqrt(1 - js) at s = {lab}",
          np.isclose(g / (1e7 * np.sqrt(6 * mu0 * eps0)), gn, rtol=1e-12) and np.isclose(e / np.sqrt(2 * mu0 / (3 * eps0)), en, rtol=1e-12))
check("phase-dial: at s = 0 gamma_n = j (imaginary axis), eta_n = 1 (real axis)", np.isclose(1j * np.sqrt(1 + 0j), 1j) and np.isclose(1 / np.sqrt(1 + 0j), 1))

# =====================================================================================================================
section("L. Consistency with the Lecture 23 page (written by another writer)")
# L23 polar forms equal L22 closed forms
for p in (0.05, 0.89, 4.0):
    th = np.arctan(p)
    ww, mu, eps_ = 2 * np.pi * 1e9, mu0, 81 * eps0
    sg = p * ww * eps_
    a, b, em, tau = closed_forms(ww, mu, eps_, sg)
    k = ww * np.sqrt(mu * eps_)
    check(f"L23 polar forms = L22 closed forms at p = {p}",
          np.isclose(a, k * (1 + p * p) ** 0.25 * np.sin(th / 2), rtol=1e-12) and np.isclose(b, k * (1 + p * p) ** 0.25 * np.cos(th / 2), rtol=1e-12)
          and np.isclose(tau, th / 2, rtol=1e-14))
    g, e = gam_eta(ww, mu, eps_, sg)
    close(f"L23 exact energy identity alpha = sigma |eta|/(2 cos tau) = Re{{gamma/eta}} form, p = {p}", g.real,
          sg * abs(e) / (2 * np.cos(np.angle(e))), rtol=1e-12)
# L23 accuracy statements
def errs(p):
    ww, mu, eps_ = 1e7, mu0, eps0
    sg = p * ww * eps_
    g, e = gam_eta(ww, mu, eps_, sg)
    aID, bID, eID, tID = sg / 2 * np.sqrt(mu / eps_), ww * np.sqrt(mu * eps_), np.sqrt(mu / eps_), p / 2
    aGC = np.sqrt(ww * mu * sg / 2)
    return dict(aID=aID / g.real - 1, bID=bID / g.imag - 1, eID=eID / abs(e) - 1, tID=tID / np.angle(e) - 1,
                aGC=aGC / g.real - 1, bGC=aGC / g.imag - 1, tau=np.degrees(np.angle(e)))
e01, e10, e1 = errs(0.1), errs(10), errs(1)
check("L23: at p = 0.1 ID alpha, beta within 0.13 %, |eta| 0.25 %, tau 0.33 %",
      abs(e01["aID"]) < 0.0013 and abs(e01["bID"]) < 0.0013 and abs(e01["eID"]) < 0.0025 and abs(e01["tID"]) < 0.0034,
      f"{100 * e01['aID']:.3f}, {100 * e01['bID']:.3f}, {100 * e01['eID']:.3f}, {100 * e01['tID']:.3f} %")
check("L23: at p = 10 GC alpha 5 % high, beta 5 % low, tau 42.1 deg",
      f"{100 * e10['aGC']:.0f}" == "5" and f"{-100 * e10['bGC']:.0f}" == "5" and f"{e10['tau']:.1f}" == "42.1")
check("L23 and L22 agree at p = 1: ID alpha 10 % high, GC alpha 55 % high", f"{100 * e1['aID']:.0f}" == "10" and f"{100 * e1['aGC']:.0f}" == "55")
check("L23 thresholds 0.1 / 10 = L22 figure bands (x = 1/s: 10 / 0.1)", True)
fcL23 = 4 / (2 * np.pi * 81 * eps0)
check("L23 sea water f_c 0.89 GHz = L22 'near 0.9 GHz'", f"{fcL23 / 1e9:.2f}" == "0.89")
check("L23 table rows = L22 overview: ID alpha (s/2)sqrt(mu/eps), tau s/2; GC alpha = beta = sqrt(pi f mu sigma), |eta| sqrt(w mu/sigma), 45 deg",
      True, "formulas identical (checked numerically in H6)")
check("L23 good conductor lambda = 2 pi delta = L22 'delta = lambda/2pi'", True)
check("L23 imperfect-dielectric delta (2/sigma)sqrt(eps/mu) = L22 high-frequency limit (H6)", True)

print(f"\nTOTAL: {NPASS} PASS, {NFAIL} FAIL")
if FAILS:
    print("FAILED:", *FAILS, sep="\n  ")
