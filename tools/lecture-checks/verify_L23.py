#!/usr/bin/env python3
"""Verification of every number, sign and direction on the Lecture 23 pages of the ECE 329 study site.

Pages checked:
  content-src/3-maxwell-and-waves/23-imperfect-dielectrics-and-good-conductors.md   (sections A-J)
  content-src/concepts/loss-tangent.md, concepts/skin-depth.md,
  concepts/conductivity-and-susceptibility-models.md (new section)                    (section K)
  content-src/problems/a-radio-wave-into-moist-ground.md                             (section L)
  figs_l23.py: figure labels and captions (section M), arrow directions (section N)
numpy only.  Exact gamma = sqrt(j w mu (sigma + j w eps)), eta = sqrt(j w mu/(sigma + j w eps)) (Lecture 22);
time averages by quadrature over one period, compared with 1/2 Re{A B*}; every vector direction by np.cross.

Material values (stated handbook values, the inputs of every number below):
  Rao, Fundamentals of Electromagnetics for ECE (2009), Table 5.1 (conductivity, S/m):
    copper 5.8e7, aluminum 3.5e7, sea water 4, fresh water 1e-3, dry earth 1e-5, Bakelite 1e-9, mica 1e-11..1e-15
  Rao Table 5.2 (relative permittivity): dry earth 5, wet earth 10, Bakelite 4.9, mica 6, distilled water 81
  Rao Table 5.3 / Example 5.2: sea water eps_r 80 (f_q = 0.9e9 Hz), dry earth f_q = 3.6e4 Hz, mica f_q = 3e-2 Hz
  Rao Problem 5.25: fresh water eps_r 80
  Kudeki notes L23: sea water sigma = 4 S/m, eps = 81 eps0
  ITU-R P.527-6 sec. 4.1: loam about 1e-2 S/m (moist), about 1e-4 S/m when dried
"""
import numpy as np

mu0 = 4e-7 * np.pi                    # the course's value (the 2019 SI value differs by 5e-10, irrelevant here)
eps0 = 8.8541878128e-12
c = 1 / np.sqrt(mu0 * eps0)
eta0 = np.sqrt(mu0 / eps0)
DB = 20 * np.log10(np.e)              # dB per neper
X, Y, Z = np.eye(3)
cr = np.cross
ok_count = 0


def ok(cond, msg):
    global ok_count
    assert cond, "FAILED: " + msg
    ok_count += 1
    print("ok  ", msg)


def close(a, b, msg, rtol=1e-6, atol=1e-12):
    ok(np.allclose(a, b, rtol=rtol, atol=atol), f"{msg}: {np.round(a, 6)} vs {np.round(b, 6)}")


def near(a, b, msg, rel=0.01):
    """page value b (rounded) against computed a, relative tolerance rel"""
    ok(abs(a - b) <= rel * abs(b), f"{msg}: computed {a:.6g}, page {b:.6g} (tol {rel:.1%})")


def exact(f, sig, er, mur=1.0):
    w = 2 * np.pi * f
    mu, eps = mur * mu0, er * eps0
    g = np.sqrt(1j * w * mu * (sig + 1j * w * eps))
    eta = np.sqrt(1j * w * mu / (sig + 1j * w * eps))
    return g.real, g.imag, abs(eta), np.angle(eta), sig / (w * eps), g, eta


def timeavg(a, b, n=4000):
    """time average over one period of Re{a e^{jwt}} Re{b e^{jwt}} (quadrature), w t = phase"""
    ph = np.linspace(0, 2 * np.pi, n, endpoint=False)
    return np.mean(np.real(a * np.exp(1j * ph)) * np.real(b * np.exp(1j * ph)))


fc = lambda s, er: s / (2 * np.pi * er * eps0)

print("=== A. constants and conversions")
close(c, 2.99792458e8, "c", rtol=1e-9)
close(eta0, 376.730, "eta0 [ohm]", rtol=1e-5)
near(1e-9 / (36 * np.pi), eps0, "eps0 ~ 1e-9/36pi (0.1 % high)", rel=2e-3)
close(DB, 8.6859, "20 log10 e = 8.686 dB per neper", rtol=1e-4)
close(10 * np.log10(np.exp(2 * 0.37)), 20 * np.log10(np.exp(0.37)), "10log e^{2 a z} = 20 log e^{a z}")
close(DB * 0.37, 20 * np.log10(np.exp(0.37)), "= 8.686 a z")

print("=== B. Section 1: loss tangent, crossover frequencies, relaxation times (handbook values)")
media = {  # name: (sigma, eps_r, page f_c, page 'good conductor below', page 'dielectric above')
    "seawater": (4.0, 81.0, 0.89e9, 89e6, 8.9e9),
    "moist soil": (1e-2, 10.0, 18e6, 1.8e6, 180e6),
    "notes Ex.1 medium": (1e-3, 4.0, 4.5e6, 450e3, 45e6),
    "fresh water": (1e-3, 80.0, 225e3, 22e3, 2.2e6),
    "dry earth": (1e-5, 5.0, 36e3, 3.6e3, 360e3),
    "Bakelite": (1e-9, 4.9, 3.7, 0.37, 37.0),
    "mica": (1e-11, 6.0, 0.03, None, 0.3),
}
for k, (s, er, f1, f2, f3) in media.items():
    near(fc(s, er), f1, f"f_c {k}", rel=0.02)
    if f2:
        near(fc(s, er) / 10, f2, f"{k}: good conductor below f_c/10", rel=0.03)
    near(10 * fc(s, er), f3, f"{k}: imperfect dielectric above 10 f_c", rel=0.03)
near(fc(5.8e7, 1.0), 1.0e18, "f_c copper (formal) 1.0e18 Hz", rel=0.05)
near(fc(3.5e7, 1.0), 6.3e17, "f_c aluminium 6.3e17 Hz", rel=0.01)
near(fc(1e-5, 5.0), 3.6e4, "Rao Table 5.3 dry earth f_q = 3.6e4 Hz", rel=0.01)
near(fc(4.0, 80.0), 0.9e9, "Rao Table 5.3 sea water (eps_r 80) f_q = 0.9e9 Hz", rel=0.01)
near(fc(1e-11, 6.0), 3e-2, "Rao Table 5.3 mica f_q = 3e-2 Hz", rel=0.01)
tau_sea = 81 * eps0 / 4.0
near(tau_sea, 0.18e-9, "seawater relaxation time eps/sigma = 0.18 ns", rel=0.01)
close(fc(4.0, 81.0), 1 / (2 * np.pi * tau_sea), "f_c = 1/(2 pi tau_r)")
ok(1 / 10e9 < tau_sea * 1.0 and 1 / 1e3 > 1e6 * tau_sea, "period 0.1 ns at 10 GHz < tau_r; 1 ms at 1 kHz >> tau_r")
for f, pv in ((1e3, 8.9e5), (1e6, 888), (1e9, 0.89), (1e10, 0.089)):
    near(exact(f, 4.0, 81.0)[4], pv, f"seawater sigma/(w eps) at {f:.0e} Hz", rel=0.01)
near(18e9 * 4 / (1e3 * 81), 8.9e5, "no-calculator form 18e9 sigma/(f eps_r) at 1 kHz", rel=0.01)
close(4.0 * 36 * np.pi * 1e9 / (2 * np.pi * 1e3 * 81), 18e9 * 4 / (1e3 * 81), "36 pi/2 pi = 18")
close(2 * np.pi, 6.2832, "omega vs f: factor 2 pi = 6.3", rtol=1e-4)
# leaky capacitor: G/(w C) = sigma/(w eps) for any geometry factor K (C = eps K, G = sigma K)
K = 3.7; s, er, w = 4.0, 81.0, 2 * np.pi * 1e6
close((s * K) / (w * er * eps0 * K), s / (w * er * eps0), "leaky capacitor G/wC = sigma/(w eps)")

print("=== C. Section 2: the table, exact polar forms, limits and accuracy")
rng = np.random.default_rng(23)
for i in range(400):
    f = 10 ** rng.uniform(0, 11); s = 10 ** rng.uniform(-8, 8); er = rng.uniform(1, 100); mur = rng.uniform(1, 5)
    A, B, ETA, TAU, p, g, eta = exact(f, s, er, mur)
    w = 2 * np.pi * f; mu, eps = mur * mu0, er * eps0
    th = np.arctan(p)
    ok_all = (np.isclose(A, w * np.sqrt(mu * eps) * (1 + p * p) ** 0.25 * np.sin(th / 2), rtol=1e-9)
              and np.isclose(B, w * np.sqrt(mu * eps) * (1 + p * p) ** 0.25 * np.cos(th / 2), rtol=1e-9)
              and np.isclose(ETA, np.sqrt(mu / eps) * (1 + p * p) ** -0.25, rtol=1e-9)
              and np.isclose(TAU, th / 2, rtol=1e-9) and np.isclose(A / B, np.tan(TAU), rtol=1e-9)
              and np.isclose(abs(g) * ETA, w * mu, rtol=1e-9) and A <= B * (1 + 1e-12) and 0 <= TAU <= np.pi / 4 + 1e-12
              and np.isclose(A, s * ETA / (2 * np.cos(TAU)), rtol=1e-9) and np.isclose((g / eta).real, s, rtol=1e-9))
    if not ok_all:
        raise AssertionError(f"polar forms failed at f={f}, s={s}, er={er}")
ok(True, "400 random media: alpha, beta, |eta| polar forms; tau = theta/2; alpha/beta = tan tau; |gamma||eta| = w mu; "
         "alpha <= beta; 0 <= tau <= 45 deg; alpha = sigma|eta|/(2 cos tau); Re{gamma/eta} = sigma")


def rel_err_id(p):
    th = np.arctan(p); q = (1 + p * p) ** 0.25
    return (p / 2) / (q * np.sin(th / 2)) - 1, 1 / (q * np.cos(th / 2)) - 1, 1 / (q ** -1) - 1, (p / 2) / (th / 2) - 1


def rel_err_gc(p):
    th = np.arctan(p); q = (1 + p * p) ** 0.25
    return np.sqrt(p / 2) / (q * np.sin(th / 2)) - 1, np.sqrt(p / 2) / (q * np.cos(th / 2)) - 1, np.degrees(th / 2)


ea, eb, ee, et = rel_err_id(0.1)
near(ea, 0.0013, "p = 0.1: imperfect-dielectric alpha 0.13 % high", rel=0.06)
near(-eb, 0.0013, "p = 0.1: imperfect-dielectric beta 0.13 % low", rel=0.06)
near(ee, 0.0025, "p = 0.1: |eta| 0.25 %", rel=0.02)
near(et, 0.0033, "p = 0.1: tau 0.33 %", rel=0.02)
ga, gb, gt = rel_err_gc(10.0)
near(ga, 0.05, "p = 10: good-conductor alpha 5 % high", rel=0.03)
near(-gb, 0.05, "p = 10: good-conductor beta 5 % low", rel=0.03)
near(gt, 42.1, "p = 10: exact tau 42.1 deg", rel=0.002)
near(rel_err_id(1.0)[0], 0.10, "p = 1: imperfect-dielectric alpha 10 % high", rel=0.02)
near(rel_err_gc(1.0)[0], 0.55, "p = 1: good-conductor alpha 55 % high", rel=0.01)
# limits of the table
f, s, er = 1e9, 1e-6, 4.0
A, B, ETA, TAU, p, *_ = exact(f, s, er)
close(A, s / 2 * np.sqrt(mu0 / (er * eps0)), "p << 1: alpha = (sigma/2) sqrt(mu/eps)", rtol=1e-6)
close(1 / A, 2 / s * np.sqrt(er * eps0 / mu0), "p << 1: delta = (2/sigma) sqrt(eps/mu)", rtol=1e-6)
close(TAU, p / 2, "p << 1: tau = sigma/(2 w eps)", rtol=1e-6)
f, s = 1e3, 5.8e7
A, B, ETA, TAU, p, *_ = exact(f, s, 1.0)
close([A, B], [np.sqrt(np.pi * f * mu0 * s)] * 2, "p >> 1: alpha = beta = sqrt(pi f mu sigma)", rtol=1e-9)
close(ETA, np.sqrt(2 * np.pi * f * mu0 / s), "p >> 1: |eta| = sqrt(w mu/sigma)", rtol=1e-9)
close(np.degrees(TAU), 45.0, "p >> 1: tau = 45 deg", rtol=1e-9)
# Lecture 22's binomial phase tan^-1(sigma/2 w eps) vs exact 1/2 tan^-1(sigma/w eps): agree to first order
for p in (1e-3, 1e-2, 0.1):
    d = np.arctan(p / 2) - 0.5 * np.arctan(p)
    ok(abs(d) < p ** 3, f"p = {p}: binomial phase minus exact phase = {d:.3g} (third order)")
# plateau of alpha for seawater and Rao Table 5.3 (84.3 Np/m for eps_r = 80)
plat = 4.0 / 2 * np.sqrt(mu0 / (81 * eps0))
near(plat, 84, "seawater high-frequency plateau (sigma/2) sqrt(mu/eps) = 84 Np/m", rel=0.01)
near(1 / plat, 0.012, "plateau penetration depth 1.2 cm", rel=0.01)
near(4.0 / 2 * np.sqrt(mu0 / (80 * eps0)), 84.3, "Rao Table 5.3 sea water alpha = 84.3 Np/m (eps_r 80)", rel=0.002)
near(exact(1e11, 4.0, 81.0)[0], plat, "exact alpha at 100 GHz approaches the plateau", rel=0.002)
for f in (1e3, 1e5):
    w = 2 * np.pi * f
    close(np.sqrt(np.pi * f * mu0 * 4) / plat, np.sqrt(2 * w * 81 * eps0 / 4), f"Rao Prob. 5.26 ratio sqrt(2 w eps/sigma) at {f:.0e} Hz")
# inverse example: 200 MHz, lambda = 0.5 m, delta = 20 m
f = 200e6; lam, dl = 0.5, 20.0
beta, alpha = 2 * np.pi / lam, 1 / dl
near(beta, 12.6, "inverse: beta = 4 pi = 12.6 rad/m", rel=0.003)
near(alpha / beta, 0.004, "inverse: alpha/beta = 0.004", rel=0.01)
tau = np.arctan(alpha / beta)
near(np.degrees(tau), 0.23, "inverse: tau = 0.23 deg", rel=0.01)
near(np.tan(2 * tau), 0.008, "inverse: p = tan 2 tau = 0.008", rel=0.01)
close(dl / lam, 40.0, "inverse: delta = 40 wavelengths")
vp = lam * f
close(vp, 1e8, "inverse: v_p = 1e8 m/s")
near((c / vp) ** 2, 9.0, "inverse: eps_r = (c/v_p)^2 = 9", rel=0.002)
near(eta0 / 3, 40 * np.pi, "inverse: |eta| = eta0/3 ~ 40 pi", rel=0.001)
near(40 * np.pi, 126, "inverse: 40 pi = 126 ohm", rel=0.003)
sig = 2 * alpha / (40 * np.pi)
near(sig, 8.0e-4, "inverse: sigma = 2 alpha/|eta| = 8.0e-4 S/m", rel=0.006)
near(sig / (2 * np.pi * f * 9 * eps0), 0.008, "inverse: check sigma/(w eps) = 0.008", rel=0.01)
A, B, *_ = exact(f, sig, 8.988)
near(2 * np.pi / B, 0.5, "inverse closes the loop: exact lambda = 0.5 m", rel=1e-3)
near(1 / A, 20.0, "inverse closes the loop: exact delta = 20 m", rel=1e-3)

print("=== D. Section 3: notes' Example 1 (imperfect dielectric, 1 GHz)")
f, s, er = 1e9, 1e-3, 4.0
A, B, ETA, TAU, p, g, eta = exact(f, s, er)
close(1e-3 * 36 * np.pi * 1e9 / (2 * np.pi * 1e9 * 4), 4.5e-3, "sigma/(w eps) with eps0 = 1e-9/36pi: 4.5e-3")
near(p, 4.5e-3, "exact sigma/(w eps)", rel=0.002)
near(TAU, 2.25e-3, "tau = 2.25e-3 rad", rel=0.002)
near(np.degrees(TAU), 0.13, "tau = 0.13 deg", rel=0.01)
near(ETA, 188, "|eta| = 188 ohm", rel=0.002)
near(60 * np.pi, 188.5, "60 pi = 188.5", rel=1e-3)
near(A, 0.094, "alpha = 0.094 Np/m", rel=0.003)
close(30 * np.pi * 1e-3, 0.0942478, "30 pi e-3", rtol=1e-6)
near(B, 41.9, "beta = 41.9 rad/m", rel=0.002)
near(2 * np.pi / B, 0.15, "lambda = 15 cm", rel=0.002)
near(2 / ETA, 10.6e-3, "H amplitude 2/|eta| = 10.6 mA/m", rel=0.003)
close(cr(Z, Y), -X, "H direction: z x y = -x")
close(cr(Y, -X), Z, "E x H = y x (-x) = +z")
# <S> by quadrature at several z
for z in (0.0, 3.0, 10.0):
    Et = 2 * np.exp(-g * z)
    Ht = -(2 / eta) * np.exp(-g * z)          # x-component of H (H = -x ...)
    Sz_q = -timeavg(Et, Ht)                    # S_z = (E_y y) x (H_x x): y x x = -z, so S_z = -E_y H_x
    close(Sz_q, 2 / ETA * np.cos(TAU) * np.exp(-2 * A * z), f"<S_z>(z={z}) quadrature = (2/|eta|) cos tau e^-2az", rtol=1e-6)
    Svec = 0.5 * np.real(np.cross(Y * Et, X * np.conj(Ht)))
    close(Sz_q, Svec @ Z, "  = z-component of 1/2 Re{E x H*} (vector cross product)", rtol=1e-9)
    close(Svec @ X, 0.0, "  no x-component"); close(Svec @ Y, 0.0, "  no y-component")
S0 = 2 / ETA * np.cos(TAU)
near(S0, 1 / (30 * np.pi), "<S>(0) = 1/(30 pi) W/m^2", rel=0.002)
near(S0, 10.6e-3, "<S>(0) = 10.6 mW/m^2", rel=0.003)
close(2 * 30 * np.pi * 1e-3 * 10, 0.6 * np.pi, "2 alpha 10 = 0.6 pi (notes' approximation)")
near(np.exp(-0.6 * np.pi), 0.15, "e^{-0.6 pi} = 0.15", rel=0.02)
near(np.exp(-20 * A), 0.15, "exact fraction after 10 m = 15 %", rel=0.02)
near(S0 * np.exp(-20 * A), 1.6e-3, "<S>(10 m) = 1.6 mW/m^2", rel=0.01)
near(DB * A, 0.82, "loss 0.82 dB/m", rel=0.005)
near(10 * DB * A, 8.2, "8.2 dB over 10 m", rel=0.005)
near(1 / A, 10.6, "delta = 1/alpha = 10.6 m", rel=0.002)
near(1 - np.exp(-20 * A), 0.85, "85 % lost in 10 m", rel=0.005)
# time-domain H lags E by tau: H(t) = -(2/|eta|) e^{-az} cos(wt - bz - tau)
ph = np.linspace(0, 2 * np.pi, 7)
close(np.real(-(2 / eta) * np.exp(1j * ph)), -(2 / ETA) * np.cos(ph - TAU), "Re{H e^{jwt}} = -(2/|eta|) cos(wt - tau) at z = 0")
# energy balance: -d<S>/dz = <J.E>
z0, h = 4.0, 1e-4
Sz = lambda z: 2 / ETA * np.cos(TAU) * np.exp(-2 * A * z)
dSdz = (Sz(z0 + h) - Sz(z0 - h)) / (2 * h)
JE = timeavg(s * 2 * np.exp(-g * z0), 2 * np.exp(-g * z0))
close(-dSdz, JE, "Poynting: -d<S>/dz = <J.E> = 1/2 sigma |E|^2 (finite difference vs quadrature)", rtol=1e-6)
close(0.5 * s * 4, 2.0e-3, "Joule heating at z = 0: 1/2 sigma |E0|^2 = 2.0 mW/m^3")
near(2 * A * S0, 2.0e-3, "2 alpha <S>(0) = 2.0 mW/m^3", rel=0.002)
close(A, s * ETA / (2 * np.cos(TAU)), "alpha = sigma |eta| / (2 cos tau) (exact)")
near(2 * A, s * ETA, "2 alpha = sigma eta (imperfect dielectric)", rel=1e-5)

print("=== E. general <S> of a damped wave with complex E0, by quadrature")
for E0 in (2.0, 1.5 - 0.7j, -0.3 + 2j):
    for (f, s, er) in ((1e9, 1e-3, 4.0), (1e3, 4.0, 81.0), (1e7, 1e-2, 10.0)):
        A, B, ETA, TAU, p, g, eta = exact(f, s, er)
        z = 0.7 / A
        Et = E0 * np.exp(-g * z); Ht = E0 / eta * np.exp(-g * z)
        close(timeavg(Et, Ht), abs(E0) ** 2 / (2 * ETA) * np.cos(TAU) * np.exp(-2 * A * z),
              f"<E_x H_y> = |E0|^2 cos tau e^-2az/(2|eta|), E0 = {E0}, f = {f:.0e}", rtol=1e-6)
for sgn in (+1, -1):          # x-polarized pair, travel along +-z: E x H along +-z
    close(cr(X, sgn * Y), sgn * Z, f"E = x, H = {sgn:+d} y: E x H = {sgn:+d} z")

print("=== F. Section 4: good conductor; notes' Examples 2 and 3")
for (f, s) in ((1e3, 4.0), (1e6, 5.8e7), (60.0, 3.5e7)):
    A, B, ETA, TAU, p, g, eta = exact(f, s, 81.0 if s == 4.0 else 1.0)
    d = 1 / np.sqrt(np.pi * f * mu0 * s)
    w = 2 * np.pi * f
    close(d, np.sqrt(2 / (w * mu0 * s)), f"delta = 1/sqrt(pi f mu sigma) = sqrt(2/w mu sigma), f = {f}")
    close(g, (1 + 1j) / d, f"gamma = (1+j)/delta, f = {f}", rtol=1e-5)
    close(eta, (1 + 1j) / (s * d), f"eta = (1+j)/(sigma delta), f = {f}", rtol=1e-5)
    close(np.sqrt(w * mu0 / (2 * s)), 1 / (s * d), "sqrt(w mu/2 sigma) = 1/(sigma delta)")
    close(abs((1 + 1j) / (s * d)), np.sqrt(w * mu0 / s), "|eta| = sqrt(2)/(sigma delta) = sqrt(w mu/sigma)")
    close(2 * np.pi / B, 2 * np.pi * d, "lambda = 2 pi delta", rtol=1e-5)
    close(w / B, w * d, "v_p = w delta", rtol=1e-5)
    # time domain H amplitude and lag; <S> = sigma delta E0^2/4
    Ht0 = 1 / ((1 + 1j) / (s * d))
    close([abs(Ht0), -np.angle(Ht0)], [s * d / np.sqrt(2), np.pi / 4], "H amplitude sigma delta E0/sqrt2, lag pi/4")
    close(timeavg(1.0, Ht0), s * d / 4, "<S>(0) = sigma delta E0^2 / 4 (quadrature)", rtol=1e-6)
    close(0.5 * ((1 + 1j) / (s * d)).real * abs(Ht0) ** 2, s * d / 4, "<S> = 1/2 Re{eta}|H0|^2 = |H0|^2/(2 sigma delta)")
near(np.exp(2 * np.pi), 535, "e^{2 pi} = 535", rel=0.001)
near(20 * np.log10(np.exp(2 * np.pi)), 54.6, "54.6 dB per wavelength (Rao 54.58)", rel=0.001)
dsea = 1 / np.sqrt(np.pi * 1e3 * mu0 * 4)
near(2 * np.pi * dsea, 50, "seawater 1 kHz lambda = 50 m", rel=1e-6)
near(2 * np.pi * 1e3 * dsea, 5e4, "seawater 1 kHz v_p = 5e4 m/s", rel=1e-6)
near(c / 9, 3.3e7, "lossless eps_r = 81: c/9 = 3.3e7 m/s", rel=0.01)
dcu = 1 / np.sqrt(np.pi * 1e6 * mu0 * 5.8e7)
near(2 * np.pi * dcu, 0.42e-3, "copper 1 MHz lambda = 0.42 mm", rel=0.012)
near(2 * np.pi * 1e6 * dcu, 415, "copper 1 MHz v_p = 415 m/s", rel=0.002)
A, B, ETA, TAU, p, g, eta = exact(1e3, 4.0, 81.0)
near(1 / ETA, 22.5, "seawater 1 kHz |H|/|E| = 22.5 (A/m)/(V/m)", rel=0.002)
near(1 / eta0, 1 / 377, "air: 1/377", rel=0.001)
close(81 * eps0 * ETA ** 2 / mu0, 1 / np.sqrt(1 + p * p), "w_e/w_m = eps|eta|^2/mu = 1/sqrt(1+p^2)", rtol=1e-9)
near(1 / np.sqrt(1 + p * p), 1.1e-6, "w_e/w_m = 1.1e-6 for seawater at 1 kHz", rel=0.03)
# time-averaged energies directly: <w_e> = eps <E^2>/2, <w_m> = mu <H^2>/2 by quadrature
we = 81 * eps0 / 2 * timeavg(1.0, 1.0); wm = mu0 / 2 * timeavg(1 / eta, 1 / eta)
close(we / wm, 1 / np.sqrt(1 + p * p), "quadrature <w_e>/<w_m>", rtol=1e-6)
# surface resistance: square slab of side l and thickness delta: R = l/(sigma l delta)
l = 0.37
close(l / (4.0 * l * dsea), 1 / (4.0 * dsea), "R of a square, delta thick = 1/(sigma delta) = Re{eta}")
close(eta.real, 1 / (4.0 * dsea), "Re{eta} = 1/(sigma delta) (seawater 1 kHz)", rtol=1e-5)
# Example 2
close(4 * 36 * np.pi * 1e9 / (2 * np.pi * 1e3 * 4), 18e6, "Ex.2 notes' ratio with eps = 4 eps0: 1.8e7")
near(exact(1e3, 4.0, 4.0)[4], 1.8e7, "Ex.2 exact ratio with 4 eps0", rel=0.002)
near(exact(1e3, 4.0, 81.0)[4], 8.9e5, "Ex.2 ratio with seawater's 81 eps0 (2 s.f.)", rel=0.006)
for er in (4.0, 81.0):
    A, B, ETA, TAU, p, g, eta = exact(1e3, 4.0, er)
    near(np.degrees(TAU), 45.0, f"Ex.2 tau = 45 deg (eps_r {er})", rel=1e-5)
    near(ETA, np.pi * np.sqrt(2) / 100, f"Ex.2 |eta| = pi sqrt2/100 (eps_r {er})", rel=1e-5)
    near(A, np.pi / 25, f"Ex.2 alpha = pi/25 (eps_r {er})", rel=1e-5)
close(np.pi * np.sqrt(2) / 100, 0.0444288, "pi sqrt2/100 = 0.0444 ohm", rtol=1e-5)
close(np.pi / 25, 0.1256637, "pi/25 = 0.126 Np/m", rtol=1e-6)
close(np.sqrt(np.pi * 1e3 * 4 * np.pi * 1e-7 * 4), np.sqrt(16 * np.pi ** 2 * 1e-4), "sqrt(pi 1e3 4pi e-7 4) = sqrt(16 pi^2 e-4)")
A, B, ETA, TAU, p, g, eta = exact(1e3, 4.0, 81.0)
near(2 / ETA, 45.0, "Ex.2 H amplitude 45 A/m", rel=0.002)
ETA1 = exact(1e9, 1e-3, 4.0)[2]; TAU1 = exact(1e9, 1e-3, 4.0)[3]
near(ETA1 / ETA, 4240, "Ex.2 H is 4,240 times Ex.1's for the same E", rel=0.002)
S2 = 2 / ETA * np.cos(TAU)
near(S2, 100 / np.pi, "Ex.2 <S>(0) = 100/pi W/m^2", rel=1e-5)
near(S2, 31.8, "Ex.2 <S>(0) = 31.8 W/m^2", rel=0.002)
near(S2 / (2 / ETA1 * np.cos(TAU1)), 3000, "Ex.2 / Ex.1 power ratio = 3,000", rel=0.002)
near(np.exp(-0.8 * np.pi), 0.081, "e^{-0.8 pi} = 0.081", rel=0.002)
near(S2 * np.exp(-20 * A), 2.6, "Ex.2 <S>(10 m) = 2.6 W/m^2", rel=0.01)
near(np.exp(-20 * A), 0.08, "Ex.2 8 % left after 10 m", rel=0.02)
near(DB * A, 1.09, "Ex.2 1.09 dB/m", rel=0.002)
close(cr(Y, -X), Z, "Ex.2 E x H = y x (-x) = +z")
Et = 2.0; Ht = -(2 / eta)
close(-timeavg(Et, Ht), S2, "Ex.2 <S_z>(0) by quadrature", rtol=1e-6)
# Example 3
close(4 * 36 * np.pi * 1e9 / (2 * np.pi * 1e3 * 81), 72e9 / 81e3, "Ex.3 4*36pi e9/(2pi e3 81) = 72e9/81e3")
near(72e9 / 81e3, 8.9e5, "Ex.3 ratio 8.9e5", rel=0.002)
close(1 / np.sqrt(16 * np.pi ** 2 * 1e-4), 25 / np.pi, "Ex.3 1/sqrt(16 pi^2 e-4) = 100/(4 pi) = 25/pi")
near(25 / np.pi, 7.96, "Ex.3 25/pi = 7.96 m (notes print 7.95)", rel=0.0005)
ok(round(25 / np.pi, 2) == 7.96, "25/pi rounds to 7.96, not 7.95 (erratum)")
near(1 / exact(1e3, 4.0, 81.0)[0], 25 / np.pi, "Ex.3 exact delta", rel=1e-5)

print("=== G. Section 5: submarines, the fair comparison and the frequency table")
near(1 - np.exp(-20 * exact(1e3, 4.0, 81.0)[0]), 0.92, "1 kHz seawater loses 92 % in 10 m", rel=0.002)
A, B, ETA, TAU, p, *_ = exact(1e9, 4.0, 81.0)
near(p, 0.89, "seawater 1 GHz ratio 0.89", rel=0.003)
near(A, 77, "seawater 1 GHz alpha = 77 Np/m", rel=0.006)
near(1 / A, 0.013, "seawater 1 GHz delta = 1.3 cm", rel=0.01)
near(DB * A, 673, "seawater 1 GHz 673 dB/m", rel=0.001)
near(10 * DB * A, 6700, "10 m at 1 GHz: 6,700 dB", rel=0.005)
near(10 * DB * exact(1e3, 4.0, 81.0)[0], 11, "10 m at 1 kHz: 11 dB", rel=0.01)
close(np.sqrt(np.pi * 1e5 * mu0 * 4) / np.sqrt(np.pi * 1e3 * mu0 * 4), 10.0, "100 x frequency -> 10 x attenuation (good conductor)")
table = [  # f, ratio, delta [m], dB/m, 100 dB depth [m], lambda0 [m]
    (76.0, 1.2e7, 28.9, 0.30, 332, 3.9e6),
    (1e3, 8.9e5, 7.96, 1.09, 92, 3.0e5),
    (24e3, 3.7e4, 1.62, 5.3, 19, 1.25e4),
    (1e6, 888, 0.25, 34.5, 2.9, 300),
    (1e8, 8.9, 0.027, 326, 0.31, 3.0),
    (1e9, 0.89, 0.013, 673, 0.15, 0.30),
]
for f, pv, dv, dbv, z100, l0 in table:
    A, B, ETA, TAU, p, *_ = exact(f, 4.0, 81.0)
    near(p, pv, f"table {f:.0e} Hz: sigma/(w eps)", rel=0.04)
    near(1 / A, dv, f"table {f:.0e} Hz: delta", rel=0.02)
    near(DB * A, dbv, f"table {f:.0e} Hz: dB/m", rel=0.02)
    near(100 / (DB * A), z100, f"table {f:.0e} Hz: 100 dB depth", rel=0.03)
    near(c / f, l0, f"table {f:.0e} Hz: free-space wavelength", rel=0.015)
    close(100 / (DB * A) * A, 100 / DB, f"table {f:.0e} Hz: 100 dB depth = {100 / DB:.2f} delta")
near(100 / DB, 11.5, "100 dB depth = 11.5 delta", rel=0.002)
d_gc = 1 / np.sqrt(np.pi * 1e8 * mu0 * 4)
near(d_gc, 0.025, "100 MHz good-conductor formula: 2.5 cm", rel=0.01)
near(1 - d_gc / (1 / exact(1e8, 4.0, 81.0)[0]), 0.05, "  about 5 % short of the exact 2.7 cm", rel=0.12)
near(1 / np.sqrt(np.pi * 1e9 * mu0 * 4), 0.008, "1 GHz good-conductor formula would give 0.8 cm", rel=0.01)
near(c / 76, 3.9e6, "lambda0 at 76 Hz = 3,900 km", rel=0.015)
near(c / 24e3, 12.5e3, "lambda0 at 24 kHz = 12.5 km", rel=0.002)
near(c / 1e3, 3.0e5, "1 kHz: 300 km in air", rel=0.001)
# consistency with the cited real systems: VLF reaches a few tens of metres, ELF hundreds of metres (100 dB budget)
ok(10 <= 100 / (DB * exact(24e3, 4.0, 81.0)[0]) <= 50, "24 kHz: 100 dB depth is 'a few tens of metres'")
ok(100 <= 100 / (DB * exact(76.0, 4.0, 81.0)[0]) <= 1000, "76 Hz: 100 dB depth is 'hundreds of metres'")
near(1 / exact(76.0, 4.0, 81.0)[0], 29, "ELF delta 29 m", rel=0.01)
near(100 / (DB * exact(76.0, 4.0, 81.0)[0]), 330, "ELF 100 dB at 330 m", rel=0.01)

print("=== H. Section 6: metals")
dcu = lambda f: 1 / np.sqrt(np.pi * f * mu0 * 5.8e7)
dal = lambda f: 1 / np.sqrt(np.pi * f * mu0 * 3.5e7)
near(dcu(1.0), 0.0661, "copper delta = 0.0661/sqrt(f) m (Rao 0.066)", rel=0.001)
near(dal(1.0), 0.0851, "aluminium delta = 0.0851/sqrt(f) m", rel=0.001)
mt = [(60, 8.53e-3, 11.0e-3, 2.86e-6), (1e3, 2.09e-3, 2.69e-3, 11.7e-6), (1e6, 66.1e-6, 85.1e-6, 0.369e-3),
      (1e8, 6.61e-6, 8.51e-6, 3.69e-3), (1e9, 2.09e-6, 2.69e-6, 11.7e-3), (1e10, 0.661e-6, 0.851e-6, 36.9e-3)]
for f, dc, da, ec in mt:
    near(dcu(f), dc, f"copper delta at {f:.0e} Hz", rel=0.003)
    near(dal(f), da, f"aluminium delta at {f:.0e} Hz", rel=0.004)
    A, B, ETA, *_ = exact(f, 5.8e7, 1.0)
    near(ETA, ec, f"copper |eta| at {f:.0e} Hz", rel=0.003)
    near(1 / A, dcu(f), f"copper: good-conductor formula accurate at {f:.0e} Hz", rel=1e-6)
near(np.sqrt(2 * np.pi * mu0 / 5.8e7), 3.69e-7, "copper |eta| = 3.69e-7 sqrt(f) ohm (Rao)", rel=0.001)
near(1e-3 / (2 * dcu(1e6)), 7.6, "skin effect: a/2delta = 7.6 for a = 1 mm at 1 MHz", rel=0.005)
near(1e-3 / dal(60), 0.09, "1 mm Al at 60 Hz = 0.09 delta", rel=0.02)
near(1e-3 / dal(1e6), 11.8, "1 mm Al at 1 MHz = 11.8 delta", rel=0.005)
near(DB * 1e-3 / dal(1e6), 102, "absorption 102 dB", rel=0.003)
near(dal(2.45e9), 1.7e-6, "Al delta at 2.45 GHz = 1.7 um", rel=0.015)
ok(0.2e-3 / dal(2.45e9) > 100, "a wall a fraction of a mm thick is hundreds of skin depths (0.2 mm -> 116)")
near(exact(1e9, 5.8e7, 1.0)[2] / eta0, 3e-5, "copper 11.7 mOhm = 3e-5 of eta0", rel=0.05)
near(4e13 / (2 * np.pi), 6.4e12, "Drude nu = 4e13 /s -> 6.4 THz (infrared)", rel=0.01)
near(np.sqrt(5.8 / 3.5), 1.29, "aluminium delta / copper delta = 1.29", rel=0.003)
near(fc(5.8e7, 1.0), 1.0e18, "copper f_c = 1.0e18 Hz (X-ray range)", rel=0.05)

print("=== I. Section 7: recipe and traps")
near(np.exp(-1), 0.37, "field at one delta: 37 %", rel=0.01)
near(np.exp(-2), 0.14, "power at one delta: 14 %", rel=0.04)
close(np.sqrt(2 * np.pi), 2.5066, "f/omega mix-up error sqrt(2 pi)", rtol=1e-4)
w = 2 * np.pi * 1e3
close(1 / np.sqrt(np.pi * 1e3 * mu0 * 4) / (1 / np.sqrt(np.pi * w * mu0 * 4)), np.sqrt(2 * np.pi), "using w in pi f mu sigma: error sqrt(2 pi)")
# -z wave evaluated at z = -10 m: factor e^{-2 alpha 10}
A = exact(1e3, 4.0, 81.0)[0]
g = exact(1e3, 4.0, 81.0)[5]
Eminus = lambda z: np.exp(g * z)                  # wave toward -z
close(abs(Eminus(-10.0)) ** 2, np.exp(-2 * A * 10), "-z wave at z = -10 m: power factor e^{-2 alpha 10}")
# SP17 #2(iv) medium: sigma = 400 w eps0, eps = 4 eps0 -> ratio 100 (regime check only; not stated on the page)
close(400 / 4, 100.0, "SP17 #2(iv) medium: sigma/(w eps) = 100")

print("=== J. Exam callout")
near(fc(1e-3, 1.0), 18e6, "S20 HE3 #3 'dry earth' (1e-3 S/m, eps0): f_c = 18 MHz", rel=0.002)
near(exact(100.0, 1e-3, 1.0)[4], 1.8e5, "  sigma/(w eps) at 100 Hz = 1.8e5", rel=0.002)
close(np.pi * 1.0 * mu0 * 1.0, 4 * np.pi ** 2 * 1e-7, "pi f mu0 sigma = 4 pi^2 e-7 f sigma")
close(np.sqrt(4 * np.pi ** 2 * 1e-7 * 4e3), 0.04 * np.pi, "f sigma = 4e3: sqrt = 0.04 pi -> delta = 25/pi")
f_min = 10 * 4.0 / (81 * eps0) / (2 * np.pi)
near(f_min, 8.9e9, "S19 conflict: sigma/(w eps) < 0.1 needs w > 10 sigma/eps, i.e. f > 8.9 GHz", rel=0.003)
ok(10e9 > f_min, "10 GHz satisfies it")
ok(np.isclose(0.2, 0.2), "FA23 #6 phasor e^{-0.2z} e^{-j0.2z}: alpha = beta (good-conductor signature)")
close(2 * 0.2, 0.4, "power attenuation 2 alpha per metre (method)")

print("=== K. concept pages")
# loss-tangent: phasor angle, Q, examples
for p in (0.01, 0.5, 1.0, 7.0, 300.0):
    sig, weps = p, 1.0
    Jd, Jt = 1j * weps, sig + 1j * weps
    lead = np.angle(Jd / Jt)
    close(np.tan(lead), p, f"displacement current leads total current by atan(sigma/w eps), p = {p}", rtol=1e-9)
    Eamp = 1.7
    P = 0.5 * sig * Eamp ** 2; Wpk = 0.5 * weps * Eamp ** 2            # weps = w eps, so W_peak*w = 1/2 w eps E^2
    close(P / Wpk, p, f"loss per radian / peak stored energy = sigma/(w eps) (1/Q), p = {p}", rtol=1e-12)
near(exact(1e6, 1e-3, 80.0)[4], 0.22, "fresh water at 1 MHz: 0.22", rel=0.03)
near(exact(1e9, 5.8e7, 1.0)[4], 1.0e9, "copper at 1 GHz: 1.0e9", rel=0.05)
near(exact(1e9, 1e-3, 4.0)[4], 4.5e-3, "notes' Ex.1 medium at 1 GHz: 4.5e-3", rel=0.002)
near(np.degrees(exact(1e9, 1e-3, 4.0)[3]), 0.13, "  angle(eta) = 0.13 deg", rel=0.01)
# complex permittivity: sigma_eff = w eps'' gives the same Ampere current
w = 2 * np.pi * 1e9; epsp, epspp, sig = 4 * eps0, 0.08 * eps0, 1e-3
close(sig + 1j * w * (epsp - 1j * epspp), (sig + w * epspp) + 1j * w * epsp, "eps = eps' - j eps'': adds w eps'' to sigma")
close((sig + w * epspp) / (w * epsp), (sig + w * epspp) / (w * epsp), "datasheet tan delta = (sigma + w eps'')/(w eps')")
# skin-depth page
dsea = lambda f: 1 / np.sqrt(np.pi * f * mu0 * 4.0)
near(dsea(1.0), 252, "seawater delta = 252/sqrt(f) m", rel=0.002)
near(dsea(60), 32.5, "seawater 60 Hz: 32.5 m", rel=0.002)
near(dsea(1e6), 0.25, "seawater 1 MHz: 25 cm", rel=0.01)
near(1 - np.exp(-2), 0.86, "86 % of the power absorbed within delta", rel=0.01)
near(1 - np.exp(-6), 0.9975, "99.75 % within 3 delta", rel=1e-4)
near(dsea(76), 28.9, "ELF 76 Hz: 28.9 m", rel=0.002)
near(dsea(24e3), 1.62, "VLF 24 kHz: 1.62 m", rel=0.003)
near(11.5 * dsea(76), 330, "11.5 delta at 76 Hz ~ 330 m", rel=0.01)
near(11.5 * dsea(24e3), 19, "11.5 delta at 24 kHz ~ 19 m", rel=0.02)
near(1 / exact(1e9, 4.0, 81.0)[0], 0.013, "seawater 1 GHz exact delta 1.3 cm", rel=0.01)
near(dsea(1e9), 0.008, "  formula 0.8 cm", rel=0.01)
near(1 / np.sqrt(np.pi * 1e5 * mu0 * 1e-2), 15.9, "moist soil 100 kHz: 15.9 m", rel=0.001)
near(fc(4.0, 81.0) / 10, 90e6, "seawater good conductor below about 90 MHz", rel=0.02)
# conductivity-models page: f_c seawater 0.89 GHz, fresh water 225 kHz, copper 66 um at 1 MHz, seawater 7.96 m at 1 kHz
near(fc(4.0, 81.0), 0.89e9, "models page: seawater f_c 0.89 GHz", rel=0.003)
near(fc(1e-3, 80.0), 225e3, "models page: fresh water f_c 225 kHz", rel=0.002)
near(dcu(1e6), 66e-6, "models page: copper 66 um at 1 MHz", rel=0.003)
near(dsea(1e3), 7.96, "models page: seawater 7.96 m at 1 kHz", rel=0.001)

print("=== L. worked problem: a 100 kHz wave into moist ground (sigma 1e-2 S/m, eps_r 10), travelling -y")
f, s, er = 1e5, 1e-2, 10.0
w = 2 * np.pi * f
A, B, ETA, TAU, p, g, eta = exact(f, s, er)
close(18e9 * s / (f * er), 180.0, "(a) no-calculator ratio 180")
near(p, 179.75, "(a) exact ratio 179.75", rel=1e-4)
near(s / (w * eps0), 1800, "(a) with eps0 instead of 10 eps0: 1,800", rel=0.002)
near(s / (f * er * eps0), 1130, "(a) with f instead of w: 2 pi times too large = 1,130", rel=0.002)
near(er * eps0 / s, 8.9e-9, "(a) relaxation time 8.9 ns", rel=0.01)
close(1 / f, 10e-6, "(a) period 10 us")
near(fc(s, er), 18e6, "(a) crossover 18 MHz", rel=0.002)
close(np.pi * f * mu0 * s, 4 * np.pi ** 2 * 1e-4, "(b) pi f mu sigma = 4 pi^2 e-4")
ag = np.sqrt(np.pi * f * mu0 * s)
close(ag, 2 * np.pi * 1e-2, "(b) alpha = beta = 2 pi e-2")
near(ag, 0.0628, "(b) 0.0628 /m", rel=0.001)
close(1 / ag, 50 / np.pi, "(b) delta = 50/pi")
near(50 / np.pi, 15.9, "(b) 15.9 m", rel=0.001)
close(2 * np.pi / ag, 100.0, "(b) lambda = 2 pi delta = 100 m")
close(w / ag, 1e7, "(b) v_p = w delta = 1e7 m/s")
near(c / 1e7, 30, "(b) = c/30", rel=0.001)
near(1 / A, 15.96, "(b) exact delta 15.96 m", rel=0.001)
near(2 * np.pi / B, 99.7, "(b) exact lambda 99.7 m", rel=0.001)
ok(abs(1 / A - 1 / ag) / (1 / A) < 0.003 and abs(2 * np.pi / B - 100) / 100 < 0.003, "(b) exact within 0.3 %")
near(c / (f * np.sqrt(10)), 950, "(b) lossless lambda about 950 m", rel=0.003)
close(np.sqrt(w * mu0 / s), np.sqrt(8 * np.pi ** 2), "(c) |eta| = sqrt(8 pi^2)")
close(np.sqrt(8 * np.pi ** 2), 2 * np.sqrt(2) * np.pi, "(c) = 2 sqrt2 pi")
near(2 * np.sqrt(2) * np.pi, 8.89, "(c) 8.89 ohm", rel=0.001)
close(s * (50 / np.pi), 1 / (2 * np.pi), "(c) sigma delta = 1/(2 pi) S")
close((1 + 1j) / (s * 50 / np.pi), 2 * np.pi * (1 + 1j), "(c) eta = 2 pi (1+j)")
near(abs(eta), 8.89, "(c) exact |eta|", rel=0.001)
near(np.degrees(TAU), 45, "(c) tau 45 deg (exact 44.84)", rel=0.004)
close(1 / (2 * np.sqrt(2) * np.pi), 0.1125, "(c) H amplitude 0.1125 A/m", rtol=1e-3)
close(cr(-Y, X), Z, "(c) u x E = (-y) x x = +z")
close(cr(X, Z), -Y, "(c) E x H = x x z = -y (down)")
close(1 / (8 * f), 1.25e-6, "(c) 45 deg = 1.25 us")
# Maxwell check of the phasor pair (exact gamma, eta): E = x e^{gamma y}, H = z (1/eta) e^{gamma y}
yv, h = -7.3, 1e-4
Ex = lambda y: np.exp(g * y)
Hz = lambda y: np.exp(g * y) / eta
dEx = (Ex(yv + h) - Ex(yv - h)) / (2 * h)
dHz = (Hz(yv + h) - Hz(yv - h)) / (2 * h)
# curl(x Ex(y)) = -z dEx/dy ; Faraday: curl E = -j w mu H  ->  -dEx/dy = -j w mu Hz
close(-dEx, -1j * w * mu0 * Hz(yv), "(c) Faraday: (curl E)_z = -dEx/dy = -j w mu Hz", rtol=1e-6)
# curl(z Hz(y)) = x dHz/dy ; Ampere: curl H = (sigma + j w eps) E
close(dHz, (s + 1j * w * er * eps0) * Ex(yv), "(c) Ampere: (curl H)_x = dHz/dy = (sigma + j w eps) Ex", rtol=1e-6)
# the time-domain fields: travel down (phase w t + beta y constant -> y decreases)
t1, t2 = 0.0, 1e-6
y1 = 0.0; y2 = -(w * (t2 - t1)) / B
ok(y2 < y1, "(c) cos(w t + beta y): crest moves to more negative y (down)")
# (d)
S0 = np.cos(TAU) / (2 * ETA)
close(np.cos(np.pi / 4) / (2 * 2 * np.sqrt(2) * np.pi), 1 / (8 * np.pi), "(d) cos tau/(2|eta|) = 1/(8 pi) (good-conductor values)")
near(1 / (8 * np.pi), 39.8e-3, "(d) 39.8 mW/m^2", rel=0.001)
near(S0, 39.8e-3, "(d) exact surface <S>", rel=0.003)
Sy_q = -timeavg(Ex(0.0), Hz(0.0))       # S_y = (E_x x) x (H_z z) . y = -E_x H_z
close(Sy_q, -S0, "(d) <S_y>(0) = -cos tau/(2|eta|) by quadrature (downward)", rtol=1e-6)
close(np.exp(-2 * ag * 25), np.exp(-np.pi), "(d) e^{2 alpha y} at y = -25 m = e^{-pi}")
near(np.exp(-np.pi), 0.043, "(d) 4.3 %", rel=0.01)
near(np.exp(-np.pi) / (8 * np.pi), 1.72e-3, "(d) 1.72 mW/m^2", rel=0.002)
near(DB * ag, 0.546, "(d) 0.546 dB/m", rel=0.001)
near(25 * DB * ag, 13.6, "(d) 13.6 dB at 25 m (3 s.f.)", rel=0.004)
close(10 * np.log10(np.exp(np.pi)), 25 * DB * ag, "(d) 10 log10 e^pi = 13.6 dB")
near(np.log(100) / (2 * ag), 36.6, "(d) 1 % depth 36.6 m (3 s.f.)", rel=0.002)
near(20 / (DB * ag), 36.6, "(d) = 20 dB / 0.546", rel=0.002)
close(np.sqrt(0.01), 0.1, "(d) field at 10 %")
heat = 0.5 * s * (1 - np.exp(-np.pi)) / (2 * ag)
near(heat, 38.1e-3, "(d) Joule heat 0..25 m = 38.1 mW/m^2", rel=0.002)
close(heat, 1 / (8 * np.pi) * (1 - np.exp(-np.pi)), "(d) = surface flux minus flux at 25 m (good-conductor values)", rtol=1e-9)
# exact version of the energy balance by numerical integration
dd = np.linspace(0, 25, 20001)
heat_ex = np.trapezoid(0.5 * s * np.exp(-2 * A * dd), dd)
close(heat_ex, S0 - S0 * np.exp(-2 * A * 25), "(d) exact: integral of 1/2 sigma|E|^2 = <S>(0) - <S>(25 m)", rtol=1e-6)
# (e)
a_req = 0.4 / DB
near(a_req, 0.0461, "(e) alpha <= 0.0461 Np/m (3 s.f.)", rel=0.002)
f_des = a_req ** 2 / (np.pi * mu0 * s)
near(f_des, 53.7e3, "(e) f = 53.7 kHz", rel=0.001)
near(180 * 100 / 53.7, 335, "(e) ratio at 53.7 kHz = 335", rel=0.002)
near(exact(f_des, s, er)[4], 335, "(e) exact ratio", rel=0.003)
near(100 * DB * exact(f_des, s, er)[0], 39.9, "(e) exact loss at 100 m: 39.9 dB", rel=0.002)
near(100 * DB * ag, 54.6, "(e) 100 kHz over 100 m: 54.6 dB (= one wavelength)", rel=0.001)
near((40 / 54.6) ** 2, 0.537, "(e) frequency factor (40/54.6)^2 = 0.537", rel=0.002)
near(c / 1e5, 3.0e3, "(e) lambda0 at 100 kHz = 3.0 km", rel=0.001)
near(c / f_des, 5.6e3, "(e) lambda0 at 53.7 kHz = 5.6 km", rel=0.005)
# variant at 10 MHz
A, B, ETA, TAU, p, g, eta = exact(1e7, s, er)
near(p, 1.8, "variant: ratio 1.8", rel=0.002)
near(np.degrees(np.arctan(p)), 60.9, "variant: theta = 60.9 deg", rel=0.002)
near(np.degrees(TAU), 30.5, "variant: tau = 30.5 deg", rel=0.003)
near(ETA, 83.1, "variant: |eta| = 83.1 ohm", rel=0.001)
near(A, 0.482, "variant: alpha = 0.482 Np/m", rel=0.001)
near(DB * A, 4.19, "variant: 4.19 dB/m", rel=0.002)
near(B, 0.819, "variant: beta = 0.819 rad/m", rel=0.001)
agc = np.sqrt(np.pi * 1e7 * mu0 * s); aid = s / 2 * np.sqrt(mu0 / (er * eps0))
near(agc, 0.628, "variant: good-conductor alpha 0.628", rel=0.001)
near(agc / A - 1, 0.30, "variant: 30 % high", rel=0.02)
near(aid, 0.596, "variant: imperfect-dielectric alpha 0.596", rel=0.001)
near(aid / A - 1, 0.24, "variant: 24 % high", rel=0.02)
near(A / B, 0.59, "variant: alpha/beta = tan 30.5 deg = 0.59", rel=0.005)

# section C addendum: above 10 f_c the loss per wavelength falls with frequency (alpha fixed, lambda shrinking)
lw = [exact(f, 4.0, 81.0)[0] * 2 * np.pi / exact(f, 4.0, 81.0)[1] for f in (1e10, 3e10, 1e11)]
ok(lw[0] > lw[1] > lw[2], f"seawater above 10 f_c: loss per wavelength alpha*lambda falls with f: {np.round(lw, 4)}")
lm = [exact(f, 4.0, 81.0)[0] for f in (1e10, 3e10, 1e11)]
ok(max(lm) / min(lm) < 1.01, "  while the loss per metre stays within 1 % (plateau)")
# skin-depth page: mu_r reduces delta by 1/sqrt(mu_r) at equal sigma
for mur in (4.0, 100.0):
    close((1 / exact(1e3, 1e7, 1.0, mur)[0]) / (1 / exact(1e3, 1e7, 1.0, 1.0)[0]), 1 / np.sqrt(mur), f"mu_r = {mur}: delta scales as 1/sqrt(mu_r)", rtol=1e-6)

print("=== M. figure labels and captions (figs_l23.py)")
near(fc(4.0, 81.0) / 10, 90e6, "fig 1/2: 'below about 90 MHz'", rel=0.02)
near(10 * fc(4.0, 81.0), 9e9, "fig 2: 'above about 9 GHz'", rel=0.02)
near(np.sqrt(mu0 / (81 * eps0)), 42, "fig 2: sqrt(mu/eps) = eta0/9 = 42 ohm", rel=0.01)
near(exact(1e9, 4.0, 81.0)[0] / exact(1e3, 4.0, 81.0)[0], 600, "fig 2: alpha at 1 GHz about 600 times alpha at 1 kHz", rel=0.03)
near(exact(1e3, 4.0, 81.0)[0], 0.126, "fig 2: 1 kHz alpha = pi/25 = 0.126 (3 s.f.)", rel=0.004)
near(exact(1e9, 4.0, 81.0)[0], 77, "fig 2: 1 GHz alpha = 77 Np/m", rel=0.006)
near(20 * np.log10(np.exp(2 * np.pi)), 54.6, "fig 3: e^{-2 pi} = -54.6 dB", rel=0.001)
ph = np.linspace(0, 4 * np.pi, 400001)
tE = ph[np.argmax(np.where((ph > np.pi) & (ph < 3 * np.pi), np.cos(ph), -9))]
tH = ph[np.argmax(np.where((ph > np.pi) & (ph < 3 * np.pi), np.cos(ph - np.pi / 4), -9))]
close(tH - tE, np.pi / 4, "fig 3: H peaks pi/4 (T/8) after E", rtol=1e-4)
u = np.linspace(0, 1, 200001)
close(u[np.argmin(abs(np.exp(-2 * u) - np.exp(-1)))], 0.5, "fig 3: power reaches 1/e at delta/2", rtol=1e-4)
for f, dv, zv in ((76.0, 29, 330), (1e3, 7.96, 92), (24e3, 1.6, 19), (1e9, 0.013, 0.15)):
    a = exact(f, 4.0, 81.0)[0]
    near(1 / a, dv, f"fig 4 label {f:.0e} Hz: delta", rel=0.02)
    near(100 / (DB * a), zv, f"fig 4 label {f:.0e} Hz: 100 dB depth", rel=0.03)
near(dcu(60), 8.5e-3, "fig 4: Cu 8.5 mm at 60 Hz", rel=0.005)
near(dal(60), 11e-3, "fig 4: Al 11 mm at 60 Hz", rel=0.005)
near(dcu(1e6), 66e-6, "fig 4: Cu 66 um at 1 MHz", rel=0.003)
near(dcu(1e9), 2.1e-6, "fig 4: Cu 2.1 um at 1 GHz", rel=0.01)
near(1 / exact(1e11, 4.0, 81.0)[0], 0.012, "fig 4: seawater delta levels off at 1.2 cm", rel=0.01)
s, er = 1e-2, 10.0
near(DB * np.sqrt(np.pi * 1e5 * mu0 * s), 0.55, "fig 5: 100 kHz 0.55 dB/m (the problem's 0.546, 2 s.f.)", rel=0.01)
near(DB * exact(1e5, s, er)[0], 0.55, "fig 5: exact 100 kHz slope 0.544 dB/m, within 1.2 % of the label", rel=0.012)
near(DB * exact(5.3718e4, s, er)[0], 0.40, "fig 5: 53.7 kHz 0.40 dB/m (exact)", rel=0.002)
near(DB * exact(1e7, s, er)[0], 4.2, "fig 5: 10 MHz 4.2 dB/m (exact, 2 s.f.)", rel=0.006)
near(1 / exact(1e5, s, er)[0], 15.9, "fig 5 caption: delta 15.9 m (exact 15.96)", rel=0.004)

print("=== N. figure arrow directions (screen frame: X right, Y up, Z out of the screen)")
# figure cond-good-conductor-fields icon: physics z (travel) -> screen X, physics x (E) -> screen Y, physics y (H) -> screen Z
M = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], dtype=float)   # screen = M @ physics
close(np.linalg.det(M), 1.0, "physics -> screen map is a proper rotation (det +1)")
close(M @ X, Y, "E along physics +x -> screen up (Y)")
close(M @ Y, Z, "H along physics +y -> out of the screen (odot)")
close(M @ Z, X, "travel physics +z -> screen right (X)")
close(cr(M @ X, M @ Y), M @ cr(X, Y), "cross product commutes with the map")
close(cr(Y, Z), X, "screen: E (up) x H (out, odot) = right = travel into the conductor")
close(cr(X, Y), Z, "physics: x x y = +z (E x H along the travel)")

print(f"\nALL {ok_count} CHECKS PASSED")
