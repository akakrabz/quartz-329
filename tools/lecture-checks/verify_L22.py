#!/usr/bin/env python3
"""Verification of every number, sign and direction on the Lecture 22 pages of the ECE 329 study site.

Pages checked:
  content-src/3-maxwell-and-waves/22-phasor-maxwell-equations-and-damped-waves.md
  content-src/concepts/propagation-constant.md, content-src/concepts/intrinsic-impedance.md (lossy section)
  content-src/problems/decoding-a-damped-wave.md
  figs_l22.py (curves are computed from the same formulas; directions/rotation senses checked here)
  digest8/ERRATA-L22.md (the numeric parts)
numpy/scipy only; derivatives by central finite differences; time averages by quadrature over one period;
every vector direction by an explicit np.cross.
"""
import numpy as np
from scipy.integrate import quad

mu0 = 1.25663706212e-6
eps0 = 8.8541878128e-12
c = 1 / np.sqrt(mu0 * eps0)
eta0 = np.sqrt(mu0 / eps0)
# the exam / no-calculator constants
mu0x = 4e-7 * np.pi
eps0x = 1e-9 / (36 * np.pi)
cx = 1 / np.sqrt(mu0x * eps0x)
eta0x = np.sqrt(mu0x / eps0x)
X, Y, Z = np.eye(3)
cr = np.cross
deg = np.degrees
ok_count = 0


def ok(cond, msg):
    global ok_count
    assert cond, "FAILED: " + msg
    ok_count += 1
    print("ok  ", msg)


def close(a, b, msg, rtol=1e-6, atol=1e-15):
    ok(np.allclose(a, b, rtol=rtol, atol=atol), f"{msg}: {np.round(a, 6)} vs {np.round(b, 6)}")


def gamma_eta(w, mu, eps, sig):
    """principal roots: Re >= 0 for gamma (decay along the travel), Re >= 0 for eta"""
    g = np.sqrt(1j * w * mu * (sig + 1j * w * eps))
    e = np.sqrt(1j * w * mu / (sig + 1j * w * eps))
    return g, e


def closed_forms(w, mu, eps, sig):
    s = sig / (w * eps)
    k = w * np.sqrt(mu * eps)
    a = k / np.sqrt(2) * np.sqrt(np.sqrt(1 + s**2) - 1)
    b = k / np.sqrt(2) * np.sqrt(np.sqrt(1 + s**2) + 1)
    mag = np.sqrt(mu / eps) / (1 + s**2) ** 0.25
    tau = 0.5 * np.arctan(s)
    return a, b, mag, tau


def tavg(f, T):
    """time average over one period by quadrature"""
    return quad(f, 0, T, limit=200)[0] / T


print("=== A. constants")
close(c, 2.99792458e8, "c")
close(eta0, 376.730313, "eta0")
close(cx, 3e8, "exam constants: 1/sqrt(mu0 eps0) = 3e8 exactly with eps0 = 1e-9/36pi")
close(eta0x, 120 * np.pi, "exam constants: eta0 = 120 pi exactly")
close(20 * np.log10(np.e), 8.686, "1 Np = 20 log10(e) = 8.686 dB (field)", rtol=1e-4)

print("=== B. phasor rules (L21 tools used on this page)")
w = 2 * np.pi * 1e6; T = 2 * np.pi / w
A = 1.7 * np.exp(1j * 0.4); B = 0.9 * np.exp(-1j * 1.1)
a_t = lambda t: np.real(A * np.exp(1j * w * t))
b_t = lambda t: np.real(B * np.exp(1j * w * t))
t0, h = 0.31e-6, 1e-12
close((a_t(t0 + h) - a_t(t0 - h)) / (2 * h), np.real(1j * w * A * np.exp(1j * w * t0)), "d/dt Re{A e^jwt} = Re{jw A e^jwt}", rtol=1e-5)
close(tavg(lambda t: a_t(t) * b_t(t), T), 0.5 * np.real(A * np.conj(B)), "<a(t) b(t)> = (1/2) Re{A B*} by quadrature", rtol=1e-8)
# a phasor with angle phi gives cos(wt + phi)
close(a_t(0.0), abs(A) * np.cos(np.angle(A)), "Re{A} = |A| cos(angle A)")

print("=== C. phasor Maxwell: what is implied")
# divergence of phasor Ampere + phasor continuity -> phasor Gauss (for w != 0): 0 = div J + jw div D and
# div J = -jw rho  =>  div D = rho.  Homogeneous conductor: (jw + sig/eps) rho = 0 -> rho = 0 (phasor form of L8)
for sig, eps in ((4.0, 81 * eps0), (5.8e7, eps0), (1e-3, 4 * eps0), (0.0, eps0)):
    fac = 1j * w + sig / eps
    ok(abs(fac) > 0, f"sig={sig:g}: jw + sig/eps = {fac:.3g} != 0, so rho~ = 0 in a homogeneous medium")
close((1j * w + 4 / (81 * eps0)) * 81 * eps0, 4 + 1j * w * 81 * eps0, "eps (jw + sig/eps) = sig + jw eps (same combination as in Ampere)")
# L8 relaxation times and crossover frequencies sig/(2 pi eps)
tr_sw = 81 * eps0 / 4
close(tr_sw * 1e9, 0.179, "seawater eps/sig = 0.18 ns (eps = 81 eps0, sig = 4 S/m)", rtol=3e-3)
close(4 / (2 * np.pi * 81 * eps0), 0.888e9, "seawater crossover sig/(2 pi eps) = 0.89 GHz", rtol=2e-3)
close(4 / (2 * np.pi * 80 * eps0), 0.9e9, "Rao Table 5.3: f_q = 0.9 GHz with eps_r = 80", rtol=1.5e-2)
tr10 = 2 * eps0 / 2e-6
close(tr10 * 1e6, 8.854, "L10 lossy medium (2 eps0, 2e-6 S/m): eps/sig = 8.85 us", rtol=1e-3)
close(2e-6 / (2 * np.pi * 2 * eps0), 17975, "L10 lossy medium crossover = 18 kHz", rtol=1e-3)

print("=== D. lossless check: Helmholtz, H from phasor Faraday")
mu, eps = mu0, 4 * eps0
w = 2 * np.pi * 1e8
beta = w * np.sqrt(mu * eps); eta = np.sqrt(mu / eps)
for sgn in (+1, -1):
    Ex = lambda z: np.exp(-sgn * 1j * beta * z)
    z0, dz = 0.37, 1e-5
    d2 = (Ex(z0 + dz) - 2 * Ex(z0) + Ex(z0 - dz)) / dz**2
    close(d2 + w**2 * mu * eps * Ex(z0), 0, f"sign {sgn:+d}: d2Ex/dz2 + w^2 mu eps Ex = 0", atol=1e-3)
    dE = (Ex(z0 + dz) - Ex(z0 - dz)) / (2 * dz)
    Hy = -dE / (1j * w * mu)                      # y-component of phasor Faraday: dEx/dz = -jw mu Hy
    close(Hy, sgn * Ex(z0) / eta, f"sign {sgn:+d}: Hy = +-Ex/eta from phasor Faraday", rtol=1e-6)
close(w * mu / beta, eta, "w mu / beta = sqrt(mu/eps) = eta")
# the curl-curl identity used: curl curl E = grad div E - lap E, with div E = 0 for E = x Ex(z)
ok(True, "div (x Ex(z)) = dEx/dx = 0 (Ex depends on z only)")

print("=== E. lossy medium: gamma, eta, and the phasor / time-domain field equations")
rng = np.random.default_rng(22)
for trial in range(6):
    mur = rng.uniform(1, 5); epr = rng.uniform(1, 80); sig = 10 ** rng.uniform(-4, 2); f = 10 ** rng.uniform(3, 10)
    mu, eps, w = mur * mu0, epr * eps0, 2 * np.pi * f
    g, e = gamma_eta(w, mu, eps, sig)
    a, b = g.real, g.imag
    ok(a >= 0 and b > 0 and e.real > 0 and e.imag >= 0, f"trial {trial}: Re g, Im g > 0; Re eta > 0, Im eta >= 0 (principal roots)")
    close(g * e, 1j * w * mu, f"trial {trial}: gamma eta = j w mu")
    close(g / e, sig + 1j * w * eps, f"trial {trial}: gamma / eta = sig + j w eps")
    close((g * e / (1j * w)).real, mu, f"trial {trial}: mu = gamma eta / (j w)")
    close((g / e).real, sig, f"trial {trial}: sig = Re(gamma/eta)")
    close((g / e).imag / w, eps, f"trial {trial}: eps = Im(gamma/eta) / w")
    epsc = eps - 1j * sig / w
    close(1j * w * np.sqrt(mu * epsc), g, f"trial {trial}: gamma = j w sqrt(mu eps_c), eps_c = eps - j sig/w")
    close(np.sqrt(mu / epsc), e, f"trial {trial}: eta = sqrt(mu / eps_c)")
    # notes p.6 form: gamma = j w sqrt(mu eps) (1 - j sig/(w eps))^(1/2)
    close(1j * w * np.sqrt(mu * eps) * np.sqrt(1 - 1j * sig / (w * eps)), g, f"trial {trial}: notes' j w sqrt(mu eps)(1 - j s)^(1/2)")
    # closed forms (Rao 5.56-5.57 in the site's notation) and the angle identities
    a2, b2, mag, tau = closed_forms(w, mu, eps, sig)
    close([a2, b2], [a, b], f"trial {trial}: closed-form alpha, beta")
    close([mag, tau], [abs(e), np.angle(e)], f"trial {trial}: |eta| = sqrt(mu/eps)/(1+s^2)^(1/4), tau = (1/2) atan(s)")
    close(np.angle(g) + np.angle(e), np.pi / 2, f"trial {trial}: angle(gamma) + angle(eta) = 90 deg")
    close(a / b, np.tan(tau), f"trial {trial}: alpha/beta = tan(tau)")
    close(abs(g) * abs(e), w * mu, f"trial {trial}: |gamma||eta| = w mu")
    s = sig / (w * eps)
    close(s, np.tan(2 * tau), f"trial {trial}: sig/(w eps) = tan(2 tau)")
    close(s, 2 * a * b / (b**2 - a**2), f"trial {trial}: sig/(w eps) = 2 alpha beta / (beta^2 - alpha^2)", rtol=1e-5)
    close(sig, 2 * a * b / (w * mu), f"trial {trial}: sig = 2 alpha beta/(w mu)", rtol=1e-6)
    close(eps, (b**2 - a**2) / (w**2 * mu), f"trial {trial}: eps = (beta^2 - alpha^2)/(w^2 mu)", rtol=1e-5)
    close(abs(g) ** 2, w**2 * mu * eps * np.sqrt(1 + s**2), f"trial {trial}: alpha^2 + beta^2 = w^2 mu eps sqrt(1+s^2)")
    ok(np.pi / 4 <= np.angle(g) <= np.pi / 2 and 0 <= tau < np.pi / 4 and b >= a, f"trial {trial}: 45 <= angle(g) <= 90, 0 <= tau < 45, beta >= alpha")
    # phasor field equations for both directions, and the time-domain equations by finite differences
    E0 = 2.0 * np.exp(1j * 0.7)
    for sgn in (+1, -1):
        Ex = lambda z: E0 * np.exp(-sgn * g * z)
        Hy = lambda z: sgn * E0 / e * np.exp(-sgn * g * z)
        L = 1 / max(a, 1e-30); lam = 2 * np.pi / b
        z0 = 0.3 * min(L, lam); dz = 1e-6 * min(L, lam)
        dEx = (Ex(z0 + dz) - Ex(z0 - dz)) / (2 * dz)
        dHy = (Hy(z0 + dz) - Hy(z0 - dz)) / (2 * dz)
        close(dEx, -1j * w * mu * Hy(z0), f"trial {trial} sign {sgn:+d}: phasor Faraday dEx/dz = -jw mu Hy", rtol=1e-6)
        close(-dHy, (sig + 1j * w * eps) * Ex(z0), f"trial {trial} sign {sgn:+d}: phasor Ampere -dHy/dz = (sig + jw eps) Ex", rtol=1e-6)
        # time domain: E = |E0| e^{-+a z} cos(wt -+ b z + angE0), H = +-(|E0|/|eta|) e^{..} cos(... - tau)
        Et = lambda z, t: abs(E0) * np.exp(-sgn * a * z) * np.cos(w * t - sgn * b * z + np.angle(E0))
        Ht = lambda z, t: sgn * abs(E0) / abs(e) * np.exp(-sgn * a * z) * np.cos(w * t - sgn * b * z + np.angle(E0) - np.angle(e))
        close(Et(z0, 0.123 / w), np.real(Ex(z0) * np.exp(1j * 0.123)), f"trial {trial} sign {sgn:+d}: E(z,t) = Re{{Ex~ e^jwt}}")
        close(Ht(z0, 0.123 / w), np.real(Hy(z0) * np.exp(1j * 0.123)), f"trial {trial} sign {sgn:+d}: H(z,t) carries the phase -tau")
        t1, dt = 0.37 / w, 1e-6 / w
        dEz = (Et(z0 + dz, t1) - Et(z0 - dz, t1)) / (2 * dz)
        dHt = (Ht(z0, t1 + dt) - Ht(z0, t1 - dt)) / (2 * dt)
        dHz = (Ht(z0 + dz, t1) - Ht(z0 - dz, t1)) / (2 * dz)
        dEt = (Et(z0, t1 + dt) - Et(z0, t1 - dt)) / (2 * dt)
        scale = abs(dEz) + w * mu * abs(Ht(z0, t1)) + 1e-30
        ok(abs(dEz + mu * dHt) < 1e-5 * scale, f"trial {trial} sign {sgn:+d}: time-domain Faraday dE/dz = -mu dH/dt")
        scale2 = abs(dHz) + abs(sig * Et(z0, t1)) + abs(eps * dEt) + 1e-30
        ok(abs(-dHz - sig * Et(z0, t1) - eps * dEt) < 1e-5 * scale2, f"trial {trial} sign {sgn:+d}: time-domain Ampere -dH/dz = sig E + eps dE/dt")
        # the time-domain wave equation with the mu sig dE/dt term promised in L18
        d2z = (Et(z0 + dz, t1) - 2 * Et(z0, t1) + Et(z0 - dz, t1)) / dz**2
        d2t = (Et(z0, t1 + dt) - 2 * Et(z0, t1) + Et(z0, t1 - dt)) / dt**2
        sc3 = abs(d2z) + abs(mu * sig * dEt) + abs(mu * eps * d2t)
        ok(abs(d2z - mu * sig * dEt - mu * eps * d2t) < 2e-3 * sc3, f"trial {trial} sign {sgn:+d}: d2E/dz2 = mu sig dE/dt + mu eps d2E/dt2")

print("=== F. directions of the damped plane wave (x-polarized, along z) and nodes vs peaks")
close(cr(X, Y), Z, "upper signs: x cross y = +z (travel +z)")
close(cr(X, -Y), -Z, "lower signs: x cross (-y) = -z (travel -z)")
# Re{E x H*} along the travel for complex eta: Re{eta*} > 0
for tau_ in (0.0, 0.3, 0.7):
    e = 50 * np.exp(1j * tau_)
    S = 0.5 * np.real(np.cross(X * 1.0, np.conj(Y * 1.0 / e)))
    ok(S[2] > 0, f"tau = {tau_}: (1/2)Re{{x E0 x (y E0/eta)*}} points +z (Re 1/eta* > 0)")
# zero crossings of e^{-az}cos(wt - bz) move at w/b; snapshot maxima sit at wt - bz = tau (mod 2 pi)
a, b = 0.6, 2 * np.pi
tauw = np.arctan(a / b)
zz = np.linspace(0, 3, 300001)
for wt in (0.0, np.pi / 4):
    f = np.exp(-a * zz) * np.cos(wt - b * zz)
    zc = zz[1:][np.sign(f[1:]) != np.sign(f[:-1])]
    close(zc[:3], (wt + np.pi / 2 + np.pi * np.arange(3)) / b, f"wt = {wt:.3f}: zero crossings at (wt + pi/2 + n pi)/beta", rtol=1e-4)
    i_max = np.argmax(f[(zz > 0.3) & (zz < 1.3)]) + np.searchsorted(zz, 0.3)
    zmax = zz[i_max]
    close(zmax, (wt - tauw + 2 * np.pi) / b, f"wt = {wt:.3f}: snapshot maximum at (wt - tau + 2pi)/beta, i.e. tau/beta toward the source", rtol=1e-4)
close(np.exp(-1), 0.3679, "1/e = 37 %", rtol=1e-4)
close(np.exp(-2), 0.1353, "power over one delta: e^-2 = 13.5 %", rtol=1e-3)
close(np.exp(-2 * np.pi), 0.001867, "good conductor: amplitude after one wavelength e^-2pi = 0.19 %", rtol=1e-3)

print("=== G. the phase dial: gamma/(w sqrt(mu eps)) and eta/sqrt(mu/eps) against s = sig/(w eps)")
for s in (0, 0.25, 0.5, 1, np.sqrt(3), 2, 4, 10):
    gn = 1j * np.sqrt(1 - 1j * s)                 # gamma / (w sqrt(mu eps))
    en = 1 / np.sqrt(1 - 1j * s)                  # eta / sqrt(mu/eps)
    close(gn * en, 1j, f"s = {s:.3g}: normalized gamma*eta = j")
    close([abs(gn), deg(np.angle(gn))], [(1 + s * s) ** 0.25, 90 - 0.5 * deg(np.arctan(s))], f"s = {s:.3g}: |g| = (1+s^2)^(1/4), angle = 90 - atan(s)/2 = {90 - 0.5*deg(np.arctan(s)):.2f} deg")
    close([abs(en), deg(np.angle(en))], [(1 + s * s) ** -0.25, 0.5 * deg(np.arctan(s))], f"s = {s:.3g}: |eta| = (1+s^2)^(-1/4), tau = {0.5*deg(np.arctan(s)):.2f} deg")
close(0.5 * deg(np.arctan(np.sqrt(3))), 30.0, "s = sqrt(3): tau = 30 deg, angle(gamma) = 60 deg")
close(0.5 * deg(np.arctan(1.0)), 22.5, "s = 1: tau = 22.5 deg")
close(0.5 * deg(np.arctan(4 / 3)), deg(np.arctan(0.5)), "s = 4/3: tau = (1/2) atan(4/3) = atan(1/2) = 26.57 deg")
close(0.5 * deg(np.arctan(3 / 4)), deg(np.arctan(1 / 3)), "s = 3/4: tau = (1/2) atan(3/4) = atan(1/3) = 18.43 deg")

print("=== H. the four regimes (notes pp. 5-8) and the penetration-depth limits")
mu, eps = mu0, 4 * eps0
for s, name in ((1e-2, "imperfect dielectric"), (1e-3, "imperfect dielectric")):
    w = 2 * np.pi * 1e9; sig = s * w * eps
    g, e = gamma_eta(w, mu, eps, sig)
    aID = sig / 2 * np.sqrt(mu / eps); bID = w * np.sqrt(mu * eps)
    eID = np.sqrt(mu / eps) * (1 + 1j * s / 2)
    close([g.real, g.imag], [aID, bID], f"{name} s = {s:g}: alpha ~ (sig/2)sqrt(mu/eps), beta ~ w sqrt(mu eps)", rtol=s**2)
    close(e, eID, f"{name} s = {s:g}: eta ~ sqrt(mu/eps)(1 + j s/2)", rtol=s**2)
    close(np.angle(e), s / 2, f"{name} s = {s:g}: tau ~ s/2", rtol=s**2)
    close(np.sqrt(mu / eps) * np.exp(1j * np.arctan(s / 2)), e, f"{name} s = {s:g}: notes' sqrt(mu/eps) e^(j atan(s/2))", rtol=s**2)
    # notes' eta route uses (1 - j s)^(-1/2) ~ 1 + j s/2  (p = -1/2, not the stated p = +1/2)
    close((1 - 1j * s) ** -0.5, 1 + 1j * s / 2, f"(1 - j s)^(-1/2) ~ 1 + j s/2 (exponent -1/2)", rtol=s**2)
    close(1 / g.real, 2 / (sig * np.sqrt(mu / eps)), f"{name}: delta ~ 2/(sig sqrt(mu/eps)), independent of frequency", rtol=s**2)
for s in (1e2, 1e3):
    w = 2 * np.pi * 1e3; sig = s * w * eps
    g, e = gamma_eta(w, mu, eps, sig)
    f = w / (2 * np.pi)
    aGC = np.sqrt(np.pi * f * mu * sig)
    close([g.real, g.imag], [aGC, aGC], f"good conductor s = {s:g}: alpha ~ beta ~ sqrt(pi f mu sig)", rtol=1 / s)
    close(np.sqrt(1j * w * mu * sig), (1 + 1j) * np.sqrt(w * mu * sig / 2), "sqrt(j w mu sig) = (1+j) sqrt(w mu sig/2)")
    close(w * np.sqrt(1j * mu * sig / w), (1 + 1j) * np.sqrt(w * mu * sig / 2), "notes p.6: w sqrt(j mu sig / w) = (1+j) sqrt(w mu sig/2)")
    close(e, np.sqrt(w * mu / sig) * np.exp(1j * np.pi / 4), f"good conductor s = {s:g}: eta ~ sqrt(w mu/sig) e^(j pi/4)", rtol=1 / s)
    close(np.sqrt(mu / (-1j * sig / w)), np.sqrt(1j * w * mu / sig), "notes p.6: sqrt(mu/(-j sig/w)) = sqrt(j w mu/sig)")
    close(1 / g.real, np.sqrt(2 / (mu * w * sig)), f"good conductor: delta ~ sqrt(2/(mu w sig)) = 1/sqrt(pi f mu sig)", rtol=1 / s)
# perfect conductor: sig -> infinity
w = 2 * np.pi * 1e6
for sig in (1e8, 1e12, 1e16):
    g, e = gamma_eta(w, mu0, eps0, sig)
    ok(1 / g.real < 1e-4 and abs(e) < 1e-2, f"sig = {sig:g}: delta = {1/g.real:.2e} m, |eta| = {abs(e):.2e} ohm -> 0 (perfect conductor)")
# frequency dependence for a fixed medium: delta and lambda/(2 pi) in units of delta_inf; normalized x = w eps / sig
for x_ in (0.01, 0.1, 1, 10, 100):
    s = 1 / x_
    a_ = np.sqrt(2) * x_ * np.sqrt(np.sqrt(1 + s * s) - 1)      # alpha / alpha_inf
    b_ = np.sqrt(2) * x_ * np.sqrt(np.sqrt(1 + s * s) + 1)      # beta / alpha_inf
    sig = 1.0; eps = 1e-10; mu = mu0
    w = x_ * sig / eps
    g, e = gamma_eta(w, mu, eps, sig)
    ainf = sig / 2 * np.sqrt(mu / eps)
    close([g.real / ainf, g.imag / ainf], [a_, b_], f"x = w eps/sig = {x_}: normalized alpha {a_:.4f}, beta {b_:.4f}")
    print(f"      x = {x_:6g}: delta/delta_inf = {1/a_:.4f}, lambda/(2 pi delta_inf) = {1/b_:.4f}, "
          f"tau = {0.5*deg(np.arctan(s)):.2f} deg, |eta|/sqrt(mu/eps) = {(1+s*s)**-0.25:.4f}")
close(1 / (np.sqrt(2) * 0.01 * np.sqrt(np.sqrt(1 + 1e4) - 1)), 7.107, "x = 0.01: delta/delta_inf = 7.1", rtol=1e-3)
close(1 / np.sqrt(2 * 0.01), 7.071, "x = 0.01: good-conductor asymptote 1/sqrt(2x) = 7.07", rtol=1e-3)
# normalized asymptotes used in figure 4
x_ = 1e-4; s = 1 / x_
close(np.sqrt(2) * x_ * np.sqrt(np.sqrt(1 + s * s) - 1), np.sqrt(2 * x_), "x -> 0: alpha/alpha_inf -> sqrt(2x)", rtol=1e-3)
x_ = 1e4; s = 1 / x_
close(np.sqrt(2) * x_ * np.sqrt(np.sqrt(1 + s * s) + 1), 2 * x_, "x -> inf: beta/alpha_inf -> 2x", rtol=1e-6)
close(np.sqrt(2) * x_ * np.sqrt(np.sqrt(1 + s * s) - 1), 1.0, "x -> inf: alpha/alpha_inf -> 1", rtol=1e-6)

print("=== I. Example: a medium exactly at the crossover (eps_r = 4, sig = 0.04 S/m, f = 180 MHz)")
w = 2 * np.pi * 180e6; mu, eps, sig = mu0x, 4 * eps0x, 0.04
close(sig / (w * eps), 1.0, "exam constants: sig/(w eps) = 1")
close(sig / (w * 4 * eps0), 0.99863, "exact eps0: sig/(w eps) = 0.9986", rtol=1e-4)
g, e = gamma_eta(w, mu, eps, sig)
close(w * np.sqrt(mu * eps), 2.4 * np.pi, "w sqrt(mu eps) = 2.4 pi = 7.540 rad/m")
close([g.real, g.imag], [3.4313, 8.2838], "alpha = 3.431 Np/m, beta = 8.284 rad/m", rtol=1e-4)
close([abs(e), deg(np.angle(e))], [158.51, 22.5], "|eta| = 60 pi / 2^(1/4) = 158.5 ohm, tau = 22.5 deg", rtol=1e-4)
close([1 / g.real, 2 * np.pi / g.imag, w / g.imag], [0.29143, 0.75849, 1.3653e8], "delta = 0.291 m, lambda = 0.758 m, v_p = 1.365e8 m/s", rtol=1e-4)
aID, bID = sig / 2 * np.sqrt(mu / eps), w * np.sqrt(mu * eps)
close([aID, bID, deg(sig / (2 * w * eps))], [3.7699, 7.5398, 28.648], "imperfect-dielectric shortcut: alpha 3.770, beta 7.540, tau 28.6 deg", rtol=1e-4)
close([aID / g.real - 1, bID / g.imag - 1], [0.0987, -0.0898], "shortcut errors: alpha +9.9 %, beta -9.0 %", rtol=1e-2)
aGC = np.sqrt(w * mu * sig / 2)
close(aGC, 5.3314, "good-conductor shortcut: alpha = beta = 5.331", rtol=1e-4)
close([aGC / g.real - 1, aGC / g.imag - 1], [0.5538, -0.3564], "good-conductor shortcut errors: alpha +55 %, beta -36 %", rtol=1e-2)
close(w / (w * np.sqrt(mu * eps)), 1.5e8, "lossless v = c/2 = 1.5e8 m/s for comparison")

print("=== J. Page example: decode E = y 6 e^{-x} cos(3e8 t - 3x) V/m, mu = mu0 (exam constants)")
w, mu = 3e8, mu0x
g = 1 + 3j
close([abs(g), deg(np.angle(g))], [np.sqrt(10), 71.565], "gamma = 1 + j3 = sqrt(10) at 71.57 deg", rtol=1e-5)
e = 1j * w * mu / g
close(e, 12 * np.pi * (3 + 1j), "eta = j w mu0 / gamma = 12 pi (3 + j) ohm")
close([e.real, e.imag, abs(e), deg(np.angle(e))], [113.097, 37.699, 119.21, 18.435], "eta = 113.1 + j37.7 = 119.2 ohm at 18.43 deg", rtol=1e-4)
close(abs(e), 12 * np.pi * np.sqrt(10), "|eta| = 12 pi sqrt(10)")
close(g * g, -8 + 6j, "gamma^2 = -8 + 6j")
ge = g / e
close([ge.real, ge.imag / w], [1 / (20 * np.pi), 8 * eps0x], "sig = 1/(20 pi) = 15.9 mS/m, eps = 8 eps0", rtol=1e-9)
close(ge.real, 0.015915, "sig = 0.0159 S/m", rtol=1e-4)
close(ge.real / ge.imag, 0.75, "sig/(w eps) = 3/4")
a2, b2, mag, tau = closed_forms(w, mu, 8 * eps0x, 1 / (20 * np.pi))
close([a2, b2], [1, 3], "check: closed forms return alpha = 1, beta = 3")
close([1 / 1, 2 * np.pi / 3, w / 3, w / (2 * np.pi)], [1, 2.0944, 1e8, 4.7746e7], "delta = 1 m, lambda = 2.094 m, v_p = 1e8 m/s, f = 47.7 MHz", rtol=1e-4)
close(cx / np.sqrt(8), 1.0607e8, "lossless eps_r = 8 would give c/sqrt(8) = 1.06e8 m/s", rtol=1e-4)
close(6 / abs(e), 0.050331, "H amplitude 6/|eta| = 50.3 mA/m", rtol=1e-4)
# direction: travel +x, E along y -> H = x cross E / eta along +z; E x H along +x
close(cr(X, Y), Z, "H direction: x cross y = +z")
close(cr(Y, Z), X, "E x H: y cross z = +x (travel +x)")
# time domain H lags E by tau: H = z 50.3 e^{-x} cos(3e8 t - 3x - 18.4 deg)
Ht = np.real(6 / e * np.exp(-g * 0.2) * np.exp(1j * 0.5))
close(Ht, 0.050331 * np.exp(-0.2) * np.cos(0.5 - 0.6 - np.radians(18.435)), "H(x=0.2, wt=0.5) = 50.3 e^-x cos(wt - 3x - 18.4 deg) mA/m", rtol=1e-4)
# the mu trap does not change sig/(w eps): ratio of Re to Im of gamma^2/(j w mu) is mu-independent
for mur in (1, 2, 3):
    q = g * g / (1j * w * mur * mu0x)
    close(q.real / q.imag, 0.75, f"mu = {mur} mu0: sig/(w eps) still 3/4 (mu cancels)")

print("=== K. Lecture 19's sheet in this medium: J_s = x 2 cos(wt) A/m on z = 0 (eps 8 eps0, sig 1/(20 pi), w 3e8)")
J0 = 2.0
Js = J0 * X
Hp = lambda z: -Y * (J0 / 2) * np.exp(-g * z)            # z > 0
Hm = lambda z: +Y * (J0 / 2) * np.exp(g * z)             # z < 0
Ep = lambda z: -X * e * (J0 / 2) * np.exp(-g * z)
Em = lambda z: -X * e * (J0 / 2) * np.exp(g * z)
close(cr(Z, Hp(0) - Hm(0)), Js, "jump: z cross (H(0+) - H(0-)) = J_s (n from 2 = z<0 into 1 = z>0)")
close(Ep(0), Em(0), "tangential E continuous at the sheet")
close(cr(X, Z) * 0.5, -Y * 0.5, "H(0+) = (1/2) J_s x n = (1/2)(2x) x z = -y")
close(cr(X, -Z) * 0.5, Y * 0.5, "H(0-) = (1/2)(2x) x (-z) = +y")
Sp = 0.5 * np.real(cr(Ep(0), np.conj(Hp(0))))
Sm = 0.5 * np.real(cr(Em(0), np.conj(Hm(0))))
close(Sp, Z * 18 * np.pi, "<S>(0+) = +z Re(eta)/2 = 18 pi = 56.5 W/m^2")
close(Sm, -Z * 18 * np.pi, "<S>(0-) = -z 56.5 W/m^2 (away from the sheet)")
P = 0.5 * np.real(np.dot(-Js, np.conj(Ep(0))))
close(P, 36 * np.pi, "<-J_s . E> = (J0^2/4) Re(eta) = 36 pi = 113.1 W/m^2 (both sides together)")
close(P, J0**2 / 4 * abs(e) * np.cos(np.angle(e)), "= (J0^2/4)|eta| cos(tau)")
close(abs(e) * J0 / 2, 119.21, "E amplitude at the sheet = |eta| J0/2 = 119.2 V/m", rtol=1e-4)
# time-domain check of the sheet fields: Maxwell in each region (finite differences) and E leads H by tau
mu, eps, sig = mu0x, 8 * eps0x, 1 / (20 * np.pi)
Ext = lambda z, t: np.real(-e * (J0 / 2) * np.exp(-g * abs(z)) * np.exp(1j * w * t))
Hyt = lambda z, t: np.real(-np.sign(z) * (J0 / 2) * np.exp(-g * abs(z)) * np.exp(1j * w * t))
for z0 in (0.4, -0.7):
    t1, dt, dz = 1.1 / w, 1e-6 / w, 1e-6
    dEz = (Ext(z0 + dz, t1) - Ext(z0 - dz, t1)) / (2 * dz)
    dHt = (Hyt(z0, t1 + dt) - Hyt(z0, t1 - dt)) / (2 * dt)
    dHz = (Hyt(z0 + dz, t1) - Hyt(z0 - dz, t1)) / (2 * dz)
    dEt = (Ext(z0, t1 + dt) - Ext(z0, t1 - dt)) / (2 * dt)
    close(dEz, -mu * dHt, f"z = {z0}: dEx/dz = -mu dHy/dt", rtol=1e-5)
    close(-dHz, sig * Ext(z0, t1) + eps * dEt, f"z = {z0}: -dHy/dz = sig Ex + eps dEx/dt", rtol=1e-5)
close(np.real(-e * np.exp(1j * 0.3)), -abs(e) * np.cos(0.3 + np.angle(e)), "E(0,t) = -x 119.2 cos(wt + 18.4 deg): E leads H by tau")
close(tavg(lambda t: -J0 * np.cos(w * t) * Ext(0.0, t), 2 * np.pi / w), 36 * np.pi, "quadrature: <-J_s(t) E_x(0,t)> = 113.1 W/m^2", rtol=1e-8)

print("=== L. Drude sigma(w) and the collisionless plasma (L11, L21)")
e_ch, m_e = 1.602176634e-19, 9.1093837015e-31
N = 1e12
wp = np.sqrt(N * e_ch**2 / (m_e * eps0))
close(wp / (2 * np.pi), 8.98e6, "N = 1e12 m^-3: f_p = 8.98 MHz", rtol=1e-3)
close(8.98 * np.sqrt(N), wp / (2 * np.pi), "rule f_p ~ 9 sqrt(N) Hz", rtol=1e-3)
for f in (5e6, 20e6, 100e6):
    w = 2 * np.pi * f
    sigd = N * e_ch**2 / (m_e * 1j * w)                     # Drude with nu -> 0
    close(sigd + 1j * w * eps0, 1j * w * eps0 * (1 - wp**2 / w**2), f"f = {f/1e6:g} MHz: sig + jw eps0 = jw eps0 (1 - wp^2/w^2)")
    g, e = gamma_eta(w, mu0, eps0, sigd)
    if w > wp:
        close(g, 1j * np.sqrt(w**2 - wp**2) / c, f"f = {f/1e6:g} MHz > f_p: gamma = j sqrt(w^2 - wp^2)/c (L21's dispersion relation)", rtol=1e-6)
        ok(abs(e.imag) < 1e-9 * abs(e) and e.real > eta0, f"f = {f/1e6:g} MHz: eta real and > eta0 ({e.real:.1f} ohm)")
    else:
        close(g, np.sqrt(wp**2 - w**2) / c, f"f = {f/1e6:g} MHz < f_p: gamma real = sqrt(wp^2 - w^2)/c (no oscillation, evanescent)", rtol=1e-6)
        ok(abs(e.real) < 1e-9 * abs(e), f"f = {f/1e6:g} MHz: eta purely imaginary (reactive)")
w = 2 * np.pi * 5e6
close(np.sqrt(wp**2 - w**2) / c, 0.1562, "5 MHz: alpha = 0.156 Np/m", rtol=1e-3)
close(c / np.sqrt(wp**2 - w**2), 6.40, "5 MHz: delta = 6.4 m", rtol=2e-3)
w = 2 * np.pi * 20e6
close([np.sqrt(w**2 - wp**2) / c, w / c], [0.3743, 0.4192], "20 MHz: beta = 0.374 rad/m vs 0.419 in vacuum", rtol=1e-3)
# with collisions the Drude sigma is complex; the 'sigma' and 'eps' read off gamma/eta are then effective values
nu = 4e13; sdc = 5.8e7
sw = sdc / (1 + 1j * 2 * np.pi * 1e9 / nu)
close(abs(sw / sdc - 1), 1.57e-4, "copper at 1 GHz: |sigma/sigma_DC - 1| = 1.6e-4 (Lecture 11's number)", rtol=1e-2)

print("=== M. Worked problem: H = z 0.2 e^{x} cos(1e8 t + 2x + 60 deg) A/m, x < 0, mu = 3 mu0 (exam constants)")
w, mu = 1e8, 3 * mu0x
a, b = 1.0, 2.0
g = a + 1j * b
ok(True, "argument 1e8 t + 2x: same signs -> travel toward -x; amplitude e^{x} decays toward -x (e^{-alpha |x|})")
close([w / (2 * np.pi), 2 * np.pi / b, w / b, 1 / a], [15.915e6, np.pi, 5e7, 1.0], "f = 15.9 MHz, lambda = pi m, v_p = 5e7 m/s, delta = 1 m", rtol=1e-4)
close([abs(g), deg(np.angle(g))], [np.sqrt(5), 63.435], "gamma = 1 + j2 = sqrt(5) at 63.43 deg", rtol=1e-5)
e = 1j * w * mu / g
close(w * mu, 120 * np.pi, "w mu = 1e8 * 3 * 4 pi e-7 = 120 pi")
close(e, 24 * np.pi * (2 + 1j), "eta = j 120 pi/(1 + j2) = 24 pi (2 + j) ohm")
close([e.real, e.imag, abs(e), deg(np.angle(e))], [150.80, 75.398, 168.60, 26.565], "eta = 150.8 + j75.4 = 168.6 ohm at 26.57 deg", rtol=1e-4)
close(abs(e), 120 * np.pi / np.sqrt(5), "|eta| = 120 pi/sqrt(5) = 24 pi sqrt(5)")
close(g * g, -3 + 4j, "gamma^2 = -3 + 4j (a 3-4-5 triangle)")
q = g / e
close(q, (4 + 3j) / (120 * np.pi), "gamma/eta = (4 + 3j)/(120 pi)")
close([q.real, q.imag / w / eps0x], [1 / (30 * np.pi), 9.0], "sig = 1/(30 pi) = 10.6 mS/m, eps = 9 eps0", rtol=1e-9)
close(q.real, 0.010610, "sig = 0.0106 S/m", rtol=1e-4)
close(q.real / q.imag, 4 / 3, "sig/(w eps) = 4/3")
close(0.5 * deg(np.arctan(4 / 3)), 26.565, "tau = (1/2) atan(4/3) = 26.57 deg", rtol=1e-4)
a2, b2, mag, tau = closed_forms(w, mu, 9 * eps0x, 1 / (30 * np.pi))
close([a2, b2, mag, deg(tau)], [1, 2, 120 * np.pi / np.sqrt(5), 26.565], "general formulas give back alpha 1, beta 2, |eta|, tau", rtol=1e-5)
close(w * np.sqrt(mu * 9 * eps0x), np.sqrt(3), "w sqrt(mu eps) = sqrt(3)")
close(np.sqrt(1 + (4 / 3) ** 2), 5 / 3, "sqrt(1 + (4/3)^2) = 5/3")
close(np.sqrt(mu / (9 * eps0x)), 120 * np.pi / np.sqrt(3), "lossless sqrt(mu/eps) = 120 pi/sqrt(3) = 217.7 ohm")
# phasors and directions: travel u = -x; E = eta H x u
Ht0 = 0.2 * np.exp(1j * np.pi / 3)
close(cr(Z, -X), -Y, "E direction: H x u = z x (-x) = -y")
close(cr(-Y, Z), -X, "check: E x H = (-y) x z = -x (travel -x)")
Et0 = e * Ht0
close([abs(Et0), deg(np.angle(Et0))], [33.719, 86.565], "E~ = -y 33.7 e^{j86.6 deg} e^{(1+j2)x} V/m", rtol=1e-4)
close(abs(Et0), 4.8 * np.pi * np.sqrt(5), "0.2 |eta| = 4.8 pi sqrt(5) = 33.7 V/m")
close(Et0, 4.8 * np.pi * (2 + 1j) * np.exp(1j * np.pi / 3), "0.2 eta e^{j60} = 4.8 pi (2 + j) e^{j60 deg}")
# time-domain E from the phasor at a sample point, and Maxwell checks in the time domain (wave along -x)
eps, sig = 9 * eps0x, 1 / (30 * np.pi)
Hz_t = lambda x, t: 0.2 * np.exp(a * x) * np.cos(w * t + b * x + np.pi / 3)
Ey_t = lambda x, t: -abs(Et0) * np.exp(a * x) * np.cos(w * t + b * x + np.angle(Et0))
for x0 in (-0.3, -1.7):
    t1, dt, dx = 0.8 / w, 1e-6 / w, 1e-6
    close(Ey_t(x0, t1), np.real(-Et0 * np.exp(g * x0) * np.exp(1j * w * t1)), f"x = {x0}: E_y(x,t) = Re{{E~ e^jwt}}")
    # Faraday (curl E)_z = dEy/dx = -mu dHz/dt
    dEy = (Ey_t(x0 + dx, t1) - Ey_t(x0 - dx, t1)) / (2 * dx)
    dHz_t = (Hz_t(x0, t1 + dt) - Hz_t(x0, t1 - dt)) / (2 * dt)
    close(dEy, -mu * dHz_t, f"x = {x0}: Faraday dEy/dx = -mu dHz/dt", rtol=1e-5)
    # Ampere (curl H)_y = -dHz/dx = sig Ey + eps dEy/dt
    dHz_x = (Hz_t(x0 + dx, t1) - Hz_t(x0 - dx, t1)) / (2 * dx)
    dEy_t = (Ey_t(x0, t1 + dt) - Ey_t(x0, t1 - dt)) / (2 * dt)
    close(-dHz_x, sig * Ey_t(x0, t1) + eps * dEy_t, f"x = {x0}: Ampere -dHz/dx = sig Ey + eps dEy/dt", rtol=1e-5)
# curl components used: for E = y Ey(x): curl E = z dEy/dx ; for H = z Hz(x): curl H = -y dHz/dx
ok(True, "curl(y Ey(x)) = z dEy/dx; curl(z Hz(x)) = -y dHz/dx (Cartesian curl)")
# 10 % distance and per-wavelength decay
close([np.log(10), np.log(10) / np.pi, np.exp(-np.pi)], [2.3026, 0.7329, 0.04321], "10 %: 2.30 m = 0.733 lambda; one wavelength: e^-pi = 4.3 %", rtol=1e-4)
# shortcut comparison
aID = sig / 2 * np.sqrt(mu / eps)
close(aID, 2 / np.sqrt(3), "imperfect-dielectric shortcut alpha = 2/sqrt(3) = 1.155 (+15 %)")
aGC = np.sqrt(w * mu * sig / 2)
close([w * mu * sig, aGC], [4.0, np.sqrt(2)], "good-conductor shortcut alpha = beta = sqrt(2) = 1.414")
# the mu = mu0 trap
e_trap = 1j * w * mu0x / g
q_trap = g / e_trap
close([abs(e_trap), q_trap.real, q_trap.imag / w / eps0x, q_trap.real / q_trap.imag], [56.199, 0.031831, 27.0, 4 / 3],
      "trap mu = mu0: |eta| = 56.2 (3x small), sig = 31.8 mS/m and eps = 27 eps0 (3x big), ratio still 4/3", rtol=1e-4)
close(0.2 * abs(e_trap), 11.24, "trap mu = mu0: E amplitude 0.2 |eta| = 11.2 V/m (3x small)", rtol=1e-3)
close(deg(np.angle(e_trap)), 26.565, "trap mu = mu0: tau unchanged (26.6 deg)", rtol=1e-4)
close((1 + 2j) * (2 + 1j), 5j, "check (b): (1 + j2)(2 + j) = 5j, so gamma eta = 24 pi * 5j = j 120 pi")
close(9 * eps0x * 1e11, 7.9577, "eps = 9 eps0 = 7.96e-11 F/m", rtol=1e-4)
close([60 - deg(np.angle(e)), deg(np.angle(Et0)) - 180], [33.435, -93.435], "wrong-sign phase 60 - 26.6 = 33.4 deg; alternate form -y cos(.. + 86.6) = +y cos(.. - 93.4)", rtol=1e-4)
close(-abs(Et0) * np.cos(0.4 + np.angle(Et0)), abs(Et0) * np.cos(0.4 + np.angle(Et0) - np.pi), "-cos(u) = cos(u - 180 deg)")
close(np.degrees(np.arctan(4 / 3)), 53.130, "tan^-1(4/3) = 53.13 deg = 2 tau", rtol=1e-4)
# phasor Faraday check via gamma*eta = j w mu (wave along -x: E~_y = -0.2 eta e^{j60} e^{gamma x})
Eyp = lambda x: -Et0 * np.exp(g * x)
Hzp = lambda x: Ht0 * np.exp(g * x)
x0, dx = -0.6, 1e-6
close((Eyp(x0 + dx) - Eyp(x0 - dx)) / (2 * dx), -1j * w * mu * Hzp(x0), "phasor Faraday: dEy~/dx = gamma Ey~ = -j w mu Hz~ (wave along -x)")
close(cr(Y, Z) * 0 + cr(-Y, Z), -X, "(-y) x z = -x")
# time average sanity: <S> along -x, using (1/2)Re{E x H*}
S0 = 0.5 * np.real(cr(-Y * Et0, np.conj(Z * Ht0)))
close(S0, -X * 0.5 * 0.2**2 * e.real, "<S>(x=0) = -x (1/2)|H|^2 Re(eta) = -x 3.02 W/m^2")
close(0.5 * 0.04 * e.real, 3.0159, "(1/2)(0.2)^2 (48 pi) = 3.02 W/m^2", rtol=1e-4)

print("=== N. figure helpers: phasor spiral and rotation senses")
# E~(z)/E0 = e^{-a z} e^{-j b z}: the tip turns clockwise (angle decreasing) as z grows, radius shrinking
zz = np.linspace(0, 1, 5)
ph = np.exp(-(0.2 + 2j * np.pi) * zz * 0.25)
ok(np.all(np.diff(np.unwrap(np.angle(ph))) < 0) and np.all(np.diff(abs(ph)) < 0), "phasor e^{-gamma z}: angle decreases (clockwise), radius shrinks as z grows")
# H~|eta|/E0 = E~/E0 e^{-j tau}: rotated clockwise by tau (lags)
tau_ = np.radians(30)
ok(np.angle(np.exp(-1j * tau_)) < 0, "H~ |eta| = E~ e^{-j tau}: rotated clockwise by tau (lags)")
# time record: E(0,t) = cos(wt), |eta|H(0,t) = cos(wt - tau) peaks at wt = tau > 0 (later)
tt = np.linspace(0, 2 * np.pi, 100001)
close(tt[np.argmax(np.cos(tt - tau_))], tau_, "H peak at wt = tau: H lags E by tau/w", rtol=1e-4)
# snapshot at t = T/8 is the t = 0 snapshot shifted by lambda/8 toward +z (zero crossings)
close((np.pi / 4 + np.pi / 2) / (2 * np.pi) - (np.pi / 2) / (2 * np.pi), 1 / 8, "t = T/8: crossings shifted by lambda/8 toward +z")

print("=== O. Section 2 example: E = y 2 cos(2pi 1e8 t + (4pi/3) x) V/m, eps_r = 4, mu0 (exam constants)")
w = 2 * np.pi * 1e8
beta = w * np.sqrt(mu0x * 4 * eps0x)
close(beta, 4 * np.pi / 3, "beta = w sqrt(mu0 4 eps0) = 4 pi/3 rad/m")
eta = np.sqrt(mu0x / (4 * eps0x))
close(eta, 60 * np.pi, "eta = 60 pi")
Ey = lambda x: 2 * np.exp(1j * beta * x)
x0, dx = 0.21, 1e-6
dEy = (Ey(x0 + dx) - Ey(x0 - dx)) / (2 * dx)
Hz = -dEy / (1j * w * mu0x)                 # (curl E)_z = dEy/dx = -jw mu Hz
close(Hz, -Ey(x0) / eta, "curl: Hz = -(1/(jw mu)) dEy/dx = -Ey/eta")
close(2 / eta, 0.010610, "amplitude 2/(60 pi) = 10.6 mA/m", rtol=1e-4)
close(cr(Y, -Z), -X, "E x H = y cross (-z) = -x: travel -x, as the + sign in (wt + beta x) says")
close(cr(-X, Y), -Z, "rotation rule: H = u x E/eta with u = -x: (-x) cross y = -z")

print("=== P. the transmission-line twin (Unit 4 look-ahead): coax filled with a lossy medium")
a_, b_ = 1e-3, 3.5e-3
lnr = np.log(b_ / a_)
for (mur, epr, sig, f) in ((1, 2.25, 1e-4, 1e6), (2, 4, 1e-2, 1e8)):
    mu, eps, w = mur * mu0, epr * eps0, 2 * np.pi * f
    L = mu / (2 * np.pi) * lnr; C = 2 * np.pi * eps / lnr; G = 2 * np.pi * sig / lnr
    close(G / C, sig / eps, f"G = (sig/eps) C (Lecture 10), mu_r={mur}")
    close(L * C / (mu * eps), 1.0, "L C / (mu eps) = 1 (Lecture 15)")
    close(L * G / (mu * sig), 1.0, "L G / (mu sig) = 1")
    g, e = gamma_eta(w, mu, eps, sig)
    close(np.sqrt(1j * w * L * (G + 1j * w * C)), g, "line gamma = sqrt(jwL (G + jwC)) = plane-wave gamma")
    close(np.sqrt(1j * w * L / (G + 1j * w * C)), e * lnr / (2 * np.pi), "line Z0 = eta ln(b/a)/(2 pi)")

print("=== Q. regime bookkeeping used in the text")
for s_ in (0.01, 0.1):
    tau_ = 0.5 * np.arctan(s_)
    close(2 * np.pi * np.tan(tau_), np.pi * s_, f"s = {s_}: alpha lambda = 2 pi tan(tau) ~ pi s", rtol=s_)
close(np.exp(-2 * np.pi * np.tan(np.radians(15))), 0.1857, "tau = 15 deg: e^{-2 pi tan tau} = 0.19 per wavelength", rtol=1e-3)
close(np.arctan(0.6 / (2 * np.pi)), np.radians(5.455), "figure 1: alpha/beta = 0.6/2pi -> tau = 5.5 deg", rtol=1e-3)
close(0.6 / (2 * np.pi), 0.0955, "figure 1: alpha/beta = 0.095", rtol=1e-3)

print("=== S. errata: the notes' angle form agrees with the exact angle to O(s^3)")
for s_ in (0.1, 0.05):
    exact = 0.5 * np.arctan(s_); notes = np.arctan(s_ / 2)
    close(notes - exact, s_**3 * (1 / 6 - 1 / 24), f"s = {s_}: atan(s/2) - (1/2)atan(s) = s^3/8 + O(s^5)", rtol=0.03)
    close(exact, s_ / 2, f"s = {s_}: (1/2) atan(s) = s/2 + O(s^3)", rtol=s_**2)

print("=== R. concept-page numbers (propagation-constant, intrinsic-impedance)")
close(2 * np.pi / (4 * np.pi / 3), 1.5, "eps_r = 4 at 100 MHz: lambda = 2 pi / (4 pi/3) = 1.5 m")
close(eta0x / np.sqrt(8), 133.29, "eta0/sqrt(8) = 133.3 ohm (the decode medium without sigma)", rtol=1e-4)
close(eta0x / np.sqrt(8) / (1 + 0.75**2) ** 0.25, 12 * np.pi * np.sqrt(10), "|eta| = (eta0/sqrt8)/(1 + (3/4)^2)^(1/4) = 119.2 ohm")
close(2 ** -0.25, 0.8409, "2^(-1/4) = 0.84", rtol=1e-4)
close(np.sqrt(mu0x * 3 / (9 * eps0x)), 217.66, "worked problem lossless sqrt(mu/eps) = 217.7 ohm", rtol=1e-4)
# instantaneous ratio E(t)/H(t) is not constant when tau != 0
tt = np.linspace(0.1, 3.0, 7)
ratio = np.cos(tt + 0.3) / np.cos(tt)
ok(np.ptp(ratio) > 1.0, "E(t)/H(t) = cos(wt + tau)/cos(wt) varies with t when tau != 0")

print(f"\nALL {ok_count} CHECKS PASSED")
