#!/usr/bin/env python3
"""Independent reviewer checks for the Lecture 21 page set (ECE 329 study site, build 8).

Written by the reviewer WITHOUT reading the writer's digest8/verify_L21.py. It re-derives every equation and
recomputes every number of
  content-src/3-maxwell-and-waves/21-monochromatic-waves-and-phasor-notation.md      (the page, sections 1-9)
  content-src/concepts/phasors.md, dispersion-relation.md, plane-waves.md             (concept pages)
  content-src/problems/phasors-e-and-power-from-a-given-h.md                          (worked problem)
  figs_l21.py                                                                          (figure numbers, directions)
with numpy/scipy only:
  * fields reconstructed from phasors, Re{X e^{jwt}}, are checked against Maxwell's curl equations by central
    finite differences (Faraday and Ampere-Maxwell, 3-D curl);
  * every time average is done by quadrature (scipy quad or a uniform periodic rule) and compared with 1/2 Re{A B*};
  * every direction is an explicit np.cross;
  * material numbers are compared with the handbook values stated next to each check.
Constants: CODATA via scipy.constants; the "no-calculator" set c = 3e8 m/s, eta0 = 120 pi Ohm where the page uses it.
Run: python3 review_L21.py > review_L21.out
"""
import re
import numpy as np
from scipy import constants as K
from scipy.integrate import quad

PI = np.pi
c0, e0, mu0, qe, me, kB, amu = K.c, K.epsilon_0, K.mu_0, K.e, K.m_e, K.k, K.atomic_mass
C3, ETA0 = 3e8, 120 * PI                       # exam constants used on the page
MU0x, EPS0x = ETA0 / C3, 1 / (ETA0 * C3)        # = 4 pi 1e-7 and 1e-9/(36 pi): consistent with C3, ETA0
X, Y, Z = np.eye(3)
NP = [0, 0]


def check(label, ok, info=""):
    ok = bool(ok)
    NP[0 if ok else 1] += 1
    print(f"{'PASS' if ok else 'FAIL'}  {label}" + (f"   [{info}]" if info else ""))


def rounds(x, quoted, dp):
    """x rounds to the quoted value at dp decimals"""
    return abs(x - quoted) <= 0.5 * 10.0 ** (-dp) + 1e-12


def sec(title):
    print("\n== " + title)


# ------------------------------------------------------------------ numerical helpers
def curl(F, r, t, h):
    Jm = np.zeros((3, 3))                       # Jm[i, j] = dF_i / dx_j
    for j in range(3):
        d = np.zeros(3); d[j] = h
        Jm[:, j] = (F(r + d, t) - F(r - d, t)) / (2 * h)
    return np.array([Jm[2, 1] - Jm[1, 2], Jm[0, 2] - Jm[2, 0], Jm[1, 0] - Jm[0, 1]])


def ddt(F, r, t, ht):
    return (F(r, t + ht) - F(r, t - ht)) / (2 * ht)


def maxwell_res(E, H, eps, mu, w, beta, npts=8, seed=3, region=None):
    """worst relative residual of curl E + mu dH/dt = 0 and curl H - eps dE/dt = 0 (source-free)"""
    rng = np.random.default_rng(seed)
    lam, T = 2 * PI / beta, 2 * PI / w
    h, ht = lam * 2e-5, T * 2e-5
    r1, r2, s1, s2 = [], [], [], []
    for _ in range(npts):
        r = rng.uniform(-lam, lam, 3)
        if region is not None:
            r = region(r)
        t = rng.uniform(0, T)
        cE, dH = curl(E, r, t, h), mu * ddt(H, r, t, ht)
        cH, dE = curl(H, r, t, h), eps * ddt(E, r, t, ht)
        r1.append(np.abs(cE + dH).max()); r2.append(np.abs(cH - dE).max())
        s1.append(max(np.abs(cE).max(), np.abs(dH).max())); s2.append(max(np.abs(cH).max(), np.abs(dE).max()))
    return max(max(r1) / max(s1), max(r2) / max(s2))


def tavg(f, T, n=4096):
    """time average over one period with the uniform periodic rule (exact for trig polynomials of degree < n)"""
    t = np.arange(n) * T / n
    return np.mean([f(tt) for tt in t], axis=0)


def tavg_quad(f, T):
    return quad(f, 0, T, limit=200, epsabs=1e-13, epsrel=1e-12)[0] / T


def from_phasor(P, w):
    """time-domain vector field (r, t) -> Re{P(r) e^{jwt}}"""
    return lambda r, t: np.real(P(r) * np.exp(1j * w * t))


def crest_speed(field1d, k, w, t1, t2, x0=0.0):
    """track the crest of field1d(x, t) near x0 between t1 and t2; returns the crest speed"""
    lam = 2 * PI / k
    xs = np.linspace(x0 - lam / 2, x0 + lam / 2, 200001)
    xa = xs[np.argmax(field1d(xs, t1))]
    xs2 = np.linspace(xa - lam / 4, xa + lam / 4, 200001)
    xb = xs2[np.argmax(field1d(xs2, t2))]
    return (xb - xa) / (t2 - t1)


rng = np.random.default_rng(21)

# =========================================================================================== A
sec("A. Page §1 — monochromatic waves, T, lambda, v_p, the 200 MHz example")
w = 2 * PI * 3.7e7; epsr = 2.5; v = 1 / np.sqrt(mu0 * epsr * e0); beta = w / v
t = rng.uniform(0, 1e-6, 200); z = rng.uniform(-10, 10, 200)
check("A1 A cos[w(t -+ z/v)] = A cos(wt -+ beta z) with beta = w/v",
      np.allclose(np.cos(w * (t - z / v)), np.cos(w * t - beta * z)) and np.allclose(np.cos(w * (t + z / v)), np.cos(w * t + beta * z)))
check("A2 beta = w/v = w sqrt(mu eps)", np.isclose(beta, w * np.sqrt(mu0 * epsr * e0)))
T = 2 * PI / w; lam = 2 * PI / beta; f = w / (2 * PI)
check("A3 fixed z: repeats after T = 2pi/w = 1/f; fixed t: repeats after lambda = 2pi/beta",
      np.allclose(np.cos(w * (t + T) - beta * z), np.cos(w * t - beta * z)) and np.allclose(np.cos(w * t - beta * (z + lam)), np.cos(w * t - beta * z)) and np.isclose(T, 1 / f))
vc = crest_speed(lambda x, tt: np.cos(w * tt - beta * x), beta, w, 0.0, T / 37)
check("A4 a crest of cos(wt - beta z) moves at dz/dt = w/beta (tracked numerically)", np.isclose(vc, w / beta, rtol=1e-3), f"{vc:.5e} vs {w/beta:.5e}")
check("A5 one wavelength per period: v_p = w/beta = lambda/T = lambda f", np.isclose(w / beta, lam / T) and np.isclose(lam / T, lam * f))
tt = 0.3 * T; zz = np.linspace(-3, 3, 101)
check("A6 snapshot at t = (t=0 snapshot) slid toward +z by (w/beta) t", np.allclose(np.cos(w * tt - beta * zz), np.cos(-beta * (zz - (w / beta) * tt))))
check("A7 TEM in a perfect dielectric: v_p = 1/sqrt(mu eps) for every w", np.allclose([ww / (ww * np.sqrt(mu0 * epsr * e0)) for ww in (1e3, 1e9, 1e15)], v))
# the 200 MHz example: E = 12 cos(4 pi 1e8 t - (8 pi/3) y) z_hat V/m
w = 4 * PI * 1e8; beta = 8 * PI / 3; f = w / (2 * PI); T = 1 / f; lam = 2 * PI / beta; vp = w / beta
check("A8 example: f = 200 MHz, T = 5 ns", np.isclose(f, 200e6) and np.isclose(T, 5e-9))
check("A9 example: beta = 8 pi/3 = 8.38 rad/m, lambda = 0.75 m", rounds(beta, 8.38, 2) and np.isclose(lam, 0.75), f"beta = {beta:.5f}")
vc = crest_speed(lambda y, tt: np.cos(w * tt - beta * y), beta, w, 0.0, T / 29)
check("A10 example: crest moves toward +y at v_p = 1.5e8 m/s = c/2 (c = 3e8); lambda f the same",
      vc > 0 and np.isclose(vp, 1.5e8) and np.isclose(vp, C3 / 2) and np.isclose(lam * f, vp), f"tracked {vc:.4e}")
murer = (C3 / vp) ** 2; etaex = ETA0 / np.sqrt(murer)
check("A11 example: c/v_p = 2 -> mu_r eps_r = 4 -> eps_r = 4 (non-magnetic), eta = eta0/2 = 60 pi = 188 Ohm",
      np.isclose(murer, 4) and np.isclose(etaex, 60 * PI) and rounds(etaex, 188, 0), f"eta = {etaex:.3f}")
dy = 0.25; lag = beta * dy; dly = dy / vp
Ey = lambda y, tt: 12 * np.cos(w * tt - beta * y)
check("A12 example: probe 25 cm downstream lags by beta dy = 2pi/3 (120 deg); sees the same cosine dy/v_p = 1.67 ns = T/3 later",
      np.isclose(lag, 2 * PI / 3) and rounds(dly * 1e9, 1.67, 2) and np.isclose(dly, T / 3)
      and np.allclose(Ey(dy, np.linspace(0, T, 50) + dly), Ey(0, np.linspace(0, T, 50))))

# =========================================================================================== B
sec("B. Page §1 — the spectrum table f = c/lambda (c = 3e8) and the memorized pairs")
table = [("radio", 1e3, 300e3), ("microwave", 1e-2, 30e9), ("infrared", 1e-5, 30e12), ("visible", 0.5e-6, 600e12),
         ("ultraviolet", 1e-8, 3e16), ("X-ray", 1e-10, 3e18), ("gamma", 1e-12, 3e20)]
for name, L, fq in table:
    check(f"B {name}: lambda = {L:g} m -> f = {fq:.3g} Hz", np.isclose(C3 / L, fq))
pairs = [(1e6, 300), (100e6, 3), (1e9, 0.30), (10e9, 0.03)]
check("B memorized: 1 MHz<->300 m, 100 MHz<->3 m, 1 GHz<->30 cm, 10 GHz<->3 cm", all(np.isclose(C3 / fq, L) for fq, L in pairs))
check("B visible: 400 nm -> 750 THz, 700 nm -> 430 THz", np.isclose(C3 / 400e-9, 750e12) and rounds(C3 / 700e-9 / 1e12, 430, -1),
      f"{C3/700e-9/1e12:.1f} THz")

# =========================================================================================== C
sec("C. Page §2 / dispersion-relation.md — the three dispersion relations; sound and ionosphere numbers")
# acoustic: v = sqrt(gamma kB T / m); handbook values: Zuckerwar (Handbook of the Speed of Sound in Real Gases) at 20 C,
# 1 atm: He 1007 m/s, Ar 319 m/s; CRC: Ar 323 m/s at 27 C; dry air 343.2 m/s at 20 C (and 331.3 m/s at 0 C).
mHe, mAr, mAir = 4.002602 * amu, 39.948 * amu, 28.9647 * amu
vs = lambda g, TK, m: np.sqrt(g * kB * TK / m)
b_ac = lambda ww, TK, m: ww * np.sqrt(m / (5 / 3 * kB * TK))
check("C1 acoustic: beta = w sqrt(m/(5/3 kB T)) -> w/beta = sqrt(5 kB T/3m) for every w (non-dispersive)",
      np.allclose([ww / b_ac(ww, 300, mHe) for ww in (10.0, 1e3, 1e5)], vs(5 / 3, 300, mHe)))
vHe300, vAr300, vHe20, vAr20 = vs(5/3, 300, mHe), vs(5/3, 300, mAr), vs(5/3, 293.15, mHe), vs(5/3, 293.15, mAr)
check("C2 He 300 K = 1019 m/s, Ar 300 K = 323 m/s", rounds(vHe300, 1019, 0) and rounds(vAr300, 323, 0), f"{vHe300:.2f}, {vAr300:.2f}")
check("C3 He 20 C = 1007 m/s, Ar 20 C = 319 m/s (handbook 1007, 319 at 20 C; Ar 323 at 27 C)",
      rounds(vHe20, 1007, 0) and rounds(vAr20, 319, 0) and abs(vHe20 / 1007 - 1) < 0.005 and abs(vAr20 / 319 - 1) < 0.005
      and abs(vs(5/3, 300.15, mAr) / 323 - 1) < 0.005, f"{vHe20:.2f}, {vAr20:.2f}")
vAir, vAir53 = vs(7/5, 293.15, mAir), vs(5/3, 293.15, mAir)
check("C4 air (gamma 7/5) at 20 C = 343 m/s (handbook 343.2), at 0 C 331 m/s (handbook 331.3); with 5/3 it would be 375 m/s",
      rounds(vAir, 343, 0) and abs(vAir - 343.2) < 0.5 and abs(vs(7/5, 273.15, mAir) - 331.3) < 0.5 and rounds(vAir53, 375, 0),
      f"{vAir:.2f}, {vs(7/5, 273.15, mAir):.2f}, {vAir53:.2f}")
check("C5 440 Hz: lambda = 2.32 m in He and 0.73 m in Ar at 300 K", rounds(vHe300 / 440, 2.32, 2) and rounds(vAr300 / 440, 0.73, 2),
      f"{vHe300/440:.4f}, {vAr300/440:.4f}")
check("C6 v_p ratio He/Ar = sqrt(39.95/4.003) = 3.16", rounds(np.sqrt(39.95 / 4.003), 3.16, 2) and rounds(vHe300 / vAr300, 3.16, 2))
check("C7 sound slope on the omega-beta diagram ~ 1e-6 c", 0.5e-6 < vAir / c0 < 2e-6, f"{vAir/c0:.2e}")

# plasma
coef = np.sqrt(qe ** 2 / (me * e0)) / (2 * PI)
check("C8 f_p = w_p/2pi = 8.98 sqrt(N) Hz (N in m^-3); Rao §10.1: f_N = sqrt(80.6 N)", rounds(coef, 8.98, 2) and rounds(coef ** 2, 80.6, 1), f"{coef:.5f}")
fpN = coef * np.sqrt(1e12)
check("C9 ionosphere N ~ 1e12 m^-3 -> f_p ~ 9 MHz", rounds(fpN / 1e6, 9, 0), f"{fpN/1e6:.4f} MHz")
bpl = lambda ff, fp: 2 * PI / c0 * np.sqrt(ff ** 2 - fp ** 2)
for fp, tag in ((8.98e6, "f_p = 8.98 MHz as stated"), (fpN, "f_p from N = 1e12 exactly")):
    b10 = bpl(10e6, fp); l10 = 2 * PI / b10; vp10 = l10 * 10e6; vg10 = c0 * np.sqrt(1 - (fp / 10e6) ** 2)
    print(f"      10 MHz, {tag}: beta = {b10:.5f} rad/m, lambda = {l10:.3f} m, v_p = {vp10:.4e} = {vp10/c0:.4f} c, v_g = {vg10/c0:.4f} c")
b_st = bpl(10e6, 8.98e6)
check("C10 10 MHz, f_p = 8.98 MHz: beta = 0.0922 rad/m (page now says 0.0922; 0.0923 only with f_p = 8.979 MHz)", rounds(b_st, 0.0922, 4), f"{b_st:.5f}")
l10 = 2 * PI / b_st; vp10 = l10 * 10e6
check("C11 10 MHz: lambda = 68.1 m (30.0 m in vacuum), v_p = lambda f = 6.81e8 m/s = 2.27 c",
      rounds(l10, 68.1, 1) and rounds(c0 / 10e6, 30.0, 1) and rounds(vp10 / 1e8, 6.81, 2) and rounds(vp10 / c0, 2.27, 2)
      and rounds(2 * PI / bpl(10e6, fpN), 68.1, 1))
vg10 = c0 * np.sqrt(1 - (8.98 / 10) ** 2)
check("C12 10 MHz: v_g = c sqrt(1 - w_p^2/w^2) = 0.440 c < c and v_p v_g = c^2", rounds(vg10 / c0, 0.440, 3) and np.isclose(vp10 * vg10, c0 ** 2))
vp100 = c0 / np.sqrt(1 - (8.98 / 100) ** 2)
check("C13 100 MHz: v_p = 1.004 c", rounds(vp100 / c0, 1.004, 3), f"{vp100/c0:.5f}")
check("C14 below f_p: beta^2 = (w^2 - w_p^2)/c^2 < 0, no real beta", (2 * PI * 5e6) ** 2 - (2 * PI * 8.98e6) ** 2 < 0)
# group velocity as d omega / d beta (finite difference of omega(beta) = sqrt(w_p^2 + c^2 beta^2))
wp = 2 * PI * 8.98e6; wfun = lambda b: np.sqrt(wp ** 2 + (c0 * b) ** 2); hb = b_st * 1e-6
vg_fd = (wfun(b_st + hb) - wfun(b_st - hb)) / (2 * hb)
check("C15 v_g = d omega/d beta (finite difference) = c sqrt(1 - w_p^2/w^2)", np.isclose(vg_fd, vg10, rtol=1e-8), f"{vg_fd/c0:.6f} c")
# narrowband pulse in a collisionless plasma: the envelope moves at v_g, the crests at v_p (units w_p = c = 1)
w0, tau, Lp = 1.5, 60.0, 3000.0
tg = np.arange(-600, 5800, 0.25); s0 = np.exp(-tg ** 2 / (2 * tau ** 2)) * np.exp(1j * w0 * tg)
S = np.fft.fft(s0); om = 2 * PI * np.fft.fftfreq(tg.size, d=0.25)
kk = np.where(np.abs(om) > 1, np.sign(om) * np.sqrt(np.abs(om ** 2 - 1) + 0j), -1j * np.sqrt(np.abs(1 - om ** 2) + 0j))
sL = np.fft.ifft(S * np.exp(-1j * kk * Lp))
i = np.argmax(np.abs(sL)); y0, y1, y2 = np.abs(sL[i - 1:i + 2]); tpk = tg[i] + 0.25 * 0.5 * (y0 - y2) / (y0 - 2 * y1 + y2)
vg_pulse = Lp / tpk; vg_th = np.sqrt(1 - 1 / w0 ** 2)
check("C16 narrowband pulse (w0 = 1.5 w_p) propagated by FFT: envelope speed = v_g = 0.745 c < c",
      abs(vg_pulse / vg_th - 1) < 2e-3 and vg_pulse < 1, f"measured {vg_pulse:.4f} c, theory {vg_th:.4f} c")
# the plasma derivation: collisionless Drude current, wave equation with J, dispersion relation
N = 1e12; w = 2 * PI * 10e6; wp2 = N * qe ** 2 / (me * e0); beta = np.sqrt(w ** 2 - wp2) / c0
sig = N * qe ** 2 / (me * (0 + 1j * w))
check("C17 collisionless Drude: sigma = Ne^2/(m(nu + jw)) at nu = 0 is -j Ne^2/(m w): J lags E by 90 deg",
      np.isclose(sig, -1j * N * qe ** 2 / (me * w)) and np.isclose(np.degrees(np.angle(sig)), -90))
Ex = lambda zz, tt: np.cos(w * tt - beta * zz)
Jx = lambda zz, tt: np.real(sig * np.exp(1j * (w * tt - beta * zz)))
vx = lambda zz, tt: Jx(zz, tt) / (-N * qe)
z1, t1 = 3.7, 1.3e-8; hz, ht = (2 * PI / beta) * 1e-4, (2 * PI / w) * 1e-4
dvdt = (vx(z1, t1 + ht) - vx(z1, t1 - ht)) / (2 * ht)
check("C18 the phasor current satisfies m dv/dt = -e E (time domain, finite difference)", np.isclose(me * dvdt, -qe * Ex(z1, t1), rtol=1e-6))
dJdt = (Jx(z1, t1 + ht) - Jx(z1, t1 - ht)) / (2 * ht)
check("C19 dJ/dt = (Ne^2/m) E", np.isclose(dJdt, N * qe ** 2 / me * Ex(z1, t1), rtol=1e-6))
d2z = lambda F, zz, tt, h: (F(zz + h, tt) - 2 * F(zz, tt) + F(zz - h, tt)) / h ** 2
d2t = lambda F, zz, tt, h: (F(zz, tt + h) - 2 * F(zz, tt) + F(zz, tt - h)) / h ** 2
pts = [(rng.uniform(-50, 50), rng.uniform(0, 1e-6)) for _ in range(6)]
res = max(abs(d2z(Ex, a, b, hz) - mu0 * N * qe ** 2 / me * Ex(a, b) - mu0 * e0 * d2t(Ex, a, b, ht)) for a, b in pts) / (w ** 2 / c0 ** 2)
check("C20 E = cos(wt - beta z) with beta^2 = (w^2 - w_p^2)/c^2 solves d2E/dz2 = mu0 (Ne^2/m) E + mu0 eps0 d2E/dt2", res < 1e-5, f"rel residual {res:.1e}")
Ev = lambda zz, tt: np.cos(w * tt - w / c0 * zz)
res_v = max(abs(d2z(Ev, a, b, hz) - mu0 * N * qe ** 2 / me * Ev(a, b) - mu0 * e0 * d2t(Ev, a, b, ht)) for a, b in pts) / (w ** 2 / c0 ** 2)
check("C21 ... and the vacuum beta = w/c does not (control)", res_v > 0.1, f"rel residual {res_v:.2f}")
eps_eff = e0 + sig / (1j * w)
check("C22 effective permittivity eps0 + sigma/(jw) = eps0(1 - w_p^2/w^2) gives the same beta",
      np.isclose(eps_eff, e0 * (1 - wp2 / w ** 2)) and np.isclose(w * np.sqrt(mu0 * eps_eff), beta))
check("C23 <J E> = 0 for the collisionless current (quadrature)", abs(tavg_quad(lambda tt: Jx(0.0, tt) * Ex(0.0, tt), 2 * PI / w)) < 1e-9 * abs(sig))
nu = 3e7; sdc = N * qe ** 2 / (me * nu)
check("C24 with collisions sigma = sigma_DC/(1 + jw/nu), Re sigma = sigma_DC/(1 + w^2/nu^2) > 0",
      np.isclose(N * qe ** 2 / (me * (nu + 1j * w)), sdc / (1 + 1j * w / nu)) and np.isclose((sdc / (1 + 1j * w / nu)).real, sdc / (1 + w ** 2 / nu ** 2)))
# the figure's point P at w = 1.5 w_p
bP = np.sqrt(1.5 ** 2 - 1)
check("C25 figure P (w = 1.5 w_p): v_p = 1.34 c, v_g = 0.75 c, v_p v_g = c^2", rounds(1.5 / bP, 1.34, 2) and rounds(bP / 1.5, 0.75, 2)
      and np.isclose((1.5 / bP) * (bP / 1.5), 1), f"{1.5/bP:.4f}, {bP/1.5:.4f}")
check("C26 plasma: v_p > c and v_g < c at every w > w_p", all((x / np.sqrt(x * x - 1) > 1) and (np.sqrt(x * x - 1) / x < 1) for x in np.linspace(1.001, 50, 500)))

# =========================================================================================== D
sec("D. Page §3 / phasors.md — definition, sine rule, table, complex moves, calculus rules")
w = 2 * PI * 1e6; T = 2 * PI / w; tt = np.linspace(0, 2 * T, 997)
A, th = 2.7, 0.83
check("D1 A cos(wt + theta) = Re{A e^{j theta} e^{jwt}}", np.allclose(A * np.cos(w * tt + th), np.real(A * np.exp(1j * th) * np.exp(1j * w * tt))))
check("D2 sin(wt + theta) = cos(wt + theta - pi/2) -> phasor A e^{j(theta - pi/2)} = -j A e^{j theta}",
      np.allclose(np.sin(w * tt + th), np.cos(w * tt + th - PI / 2)) and np.isclose(A * np.exp(1j * (th - PI / 2)), -1j * A * np.exp(1j * th)))
check("D3 Re{-j e^{jwt}} = sin wt", np.allclose(np.real(-1j * np.exp(1j * w * tt)), np.sin(w * tt)))
b_, y_, z_ = 3.1, rng.uniform(-2, 2, 7), rng.uniform(-2, 2, 7)
rows = [("A cos wt", lambda t_, s: A * np.cos(w * t_), lambda s: A + 0j),
        ("A sin wt", lambda t_, s: A * np.sin(w * t_), lambda s: -1j * A),
        ("-A cos wt", lambda t_, s: -A * np.cos(w * t_), lambda s: -A + 0j),
        ("-A sin wt", lambda t_, s: -A * np.sin(w * t_), lambda s: 1j * A),
        ("A cos(wt + theta)", lambda t_, s: A * np.cos(w * t_ + th), lambda s: A * np.exp(1j * th)),
        ("A sin(wt + theta)", lambda t_, s: A * np.sin(w * t_ + th), lambda s: -1j * A * np.exp(1j * th)),
        ("A cos(wt - beta z)", lambda t_, s: A * np.cos(w * t_ - b_ * s), lambda s: A * np.exp(-1j * b_ * s)),
        ("A sin(wt + beta y)", lambda t_, s: A * np.sin(w * t_ + b_ * s), lambda s: -1j * A * np.exp(1j * b_ * s))]
for name, fn, ph in rows:
    ok = all(np.allclose(fn(tt, s), np.real(ph(s) * np.exp(1j * w * tt))) for s in y_)
    check(f"D4 table row: {name}", ok)
check("D5 sine-rule row: -jA e^{j theta} = A e^{j(theta - pi/2)}", np.isclose(-1j * A * np.exp(1j * th), A * np.exp(1j * (th - PI / 2))))
check("D6 -4 + 3j is at 143.1 deg (its own quadrant); arctan(3/(-4)) = -36.9 deg",
      rounds(np.degrees(np.angle(-4 + 3j)), 143.1, 1) and rounds(np.degrees(np.arctan(3 / -4)), -36.9, 1))
# rotations as cross products in the screen frame (Re right, Im up, z out of the screen)
zc = 0.6 + 0.8j; vec = np.array([zc.real, zc.imag, 0.0])
rot_p = np.cross(Z, vec); rot_m = np.cross(-Z, vec)
check("D7 j z = z_hat x (Re, Im, 0): +90 deg (counterclockwise); -j z = -z_hat x (..): -90 deg; -1 = e^{j pi} half a turn",
      np.allclose(rot_p[:2], [(1j * zc).real, (1j * zc).imag]) and np.allclose(rot_m[:2], [(-1j * zc).real, (-1j * zc).imag])
      and np.isclose(np.exp(1j * PI), -1) and np.isclose(1 / 1j, -1j) and np.isclose(np.exp(-1j * PI / 2), -1j))
zr = 1.7 - 2.2j
check("D8 conjugate: (r e^{j phi})* = r e^{-j phi}, z z* = |z|^2, Re z = (z + z*)/2; products multiply lengths, add angles",
      np.isclose(np.conj(3 * np.exp(0.7j)), 3 * np.exp(-0.7j)) and np.isclose(zr * np.conj(zr), abs(zr) ** 2) and np.isclose(zr.real, (zr + np.conj(zr)) / 2)
      and np.isclose(2 * np.exp(0.3j) * 5 * np.exp(1.1j), 10 * np.exp(1.4j)))
ph = 4 - 3j; bz = 0.37
check("D9 4 - 3j = 5 e^{-j36.9 deg}", np.isclose(abs(ph), 5) and rounds(np.degrees(np.angle(ph)), -36.9, 1))
ok = np.allclose(np.real(ph * np.exp(-1j * bz) * np.exp(1j * w * tt)), 5 * np.cos(w * tt - bz + np.angle(ph))) and \
     np.allclose(5 * np.cos(w * tt - bz + np.angle(ph)), 4 * np.cos(w * tt - bz) + 3 * np.sin(w * tt - bz))
check("D10 (4 - 3j)e^{-j beta z} -> 5 cos(wt - beta z - 36.9 deg) = 4 cos(..) + 3 sin(..)", ok)
check("D11 the slip Re{A} cos(wt) keeps the 4 and loses the 3", not np.allclose(ph.real * np.cos(w * tt), np.real(ph * np.exp(1j * w * tt))))
Ap = 1.3 * np.exp(-2.1j); a = lambda t_: np.real(Ap * np.exp(1j * w * t_))
check("D12 uniqueness: a(0) = Re{A}, a(T/4) = -Im{A} recover the phasor", np.isclose(a(0), Ap.real) and np.isclose(a(T / 4), -Ap.imag))
h = T * 1e-5; t1 = 0.37 * T
check("D13 d/dt -> jw (finite difference)", np.isclose((a(t1 + h) - a(t1 - h)) / (2 * h), np.real(1j * w * Ap * np.exp(1j * w * t1)), rtol=1e-8))
Ai = lambda t_: np.real(Ap / (1j * w) * np.exp(1j * w * t_))
check("D14 integral -> 1/(jw): d/dt Re{A/(jw) e^{jwt}} = a(t)", np.isclose((Ai(t1 + h) - Ai(t1 - h)) / (2 * h), a(t1), rtol=1e-8))
tau = 0.21 * T
check("D15 delay: a(t - tau) = Re{A e^{-jw tau} e^{jwt}}", np.allclose(a(tt - tau), np.real(Ap * np.exp(-1j * w * tau) * np.exp(1j * w * tt))))
Bp = 0.7 * np.exp(0.4j); bb = lambda t_: np.real(Bp * np.exp(1j * w * t_))
check("D16 products have no phasor: a b != Re{A B e^{jwt}}", not np.allclose(a(tt) * bb(tt), np.real(Ap * Bp * np.exp(1j * w * tt))))
tg = np.linspace(0, T, 100001, endpoint=False)
check("D17 d/dt cos wt = -w sin wt peaks a quarter period before cos wt (at t = 3T/4 = -T/4)",
      np.isclose(tg[np.argmax(-w * np.sin(w * tg))], 0.75 * T, atol=T * 1e-4))
Cc = 2e-9; Vp = 3 * np.exp(0.2j); v_ = lambda t_: np.real(Vp * np.exp(1j * w * t_))
check("D18 ECE 210: i = C dv/dt -> I = jwC V, impedance 1/(jwC)", np.isclose(Cc * (v_(t1 + h) - v_(t1 - h)) / (2 * h), np.real(1j * w * Cc * Vp * np.exp(1j * w * t1)), rtol=1e-7))
# Drude in phasors (Lecture 11): j w m v = qE - m nu v -> sigma = N q^2/(m(nu + jw))
m_, q_, nu_, N_ = me, -qe, 4e13, 8.5e28; w11 = 2 * PI * 1e13; Ep = 2.0 + 0.5j
vph = q_ * Ep / (m_ * (nu_ + 1j * w11))
vt = lambda t_: np.real(vph * np.exp(1j * w11 * t_)); Et = lambda t_: np.real(Ep * np.exp(1j * w11 * t_))
h11 = (2 * PI / w11) * 1e-5; t11 = 0.3 * 2 * PI / w11
check("D19 Lecture 11 Drude in phasors: v(t) solves m dv/dt = qE - m nu v, sigma = Nq^2/(m(nu + jw))",
      np.isclose(m_ * (vt(t11 + h11) - vt(t11 - h11)) / (2 * h11), q_ * Et(t11) - m_ * nu_ * vt(t11), rtol=1e-6)
      and np.isclose(N_ * q_ * vph / Ep, N_ * q_ ** 2 / (m_ * (nu_ + 1j * w11))))
check("D20 phasors.md: 3 sin(wt - 30 deg) = 3 cos(wt - 120 deg) -> 3 e^{-j120 deg} = -1.5 - 2.60j",
      np.allclose(3 * np.sin(w * tt - PI / 6), 3 * np.cos(w * tt - 2 * PI / 3)) and np.isclose(3 * np.exp(-2j * PI / 3).real, -1.5) and rounds(3 * np.exp(-2j * PI / 3).imag, -2.60, 2))
check("D21 phasors.md: 6 cos wt + 6 sin wt -> 6 - 6j = 6 sqrt2 e^{-j45 deg} -> 8.49 cos(wt - 45 deg)",
      np.allclose(6 * np.cos(w * tt) + 6 * np.sin(w * tt), 6 * np.sqrt(2) * np.cos(w * tt - PI / 4)) and rounds(6 * np.sqrt(2), 8.49, 2))
check("D22 phasors.md: j turns the arrow +90 deg, its shadow peaks a quarter period EARLIER",
      np.isclose((tg[np.argmax(np.real(np.exp(1j * w * tg)))] - tg[np.argmax(np.real(1j * np.exp(1j * w * tg)))]) % T, T / 4, atol=T * 1e-4))

# =========================================================================================== E
sec("E. Page §4 / plane-waves.md — plane-wave phasors and the direction of travel")
w = 2 * PI * 3e8; v = c0; beta = w / v; E0 = 1.4 * np.exp(0.6j)
zz = rng.uniform(-1, 1, 9)
check("E1 delay rule: Re{E0 e^{-j beta z} e^{jwt}} = Re{E0 e^{jw(t - z/v)}} (the point z sees the origin z/v earlier)",
      all(np.allclose(np.real(E0 * np.exp(-1j * beta * s) * np.exp(1j * w * tt)), np.real(E0 * np.exp(1j * w * (tt - s / v)))) for s in zz))
for sgn, tgt in ((-1, +1), (+1, -1)):
    vc = crest_speed(lambda x, t_: np.real(np.exp(1j * sgn * beta * x) * np.exp(1j * w * t_)), beta, w, 0.0, (2 * PI / w) / 23)
    check(f"E2 e^{{{'+' if sgn > 0 else '-'}j beta z}} travels toward {'+' if tgt > 0 else '-'}z (crest tracked)", np.sign(vc) == tgt and np.isclose(abs(vc), w / beta, rtol=2e-3), f"{vc:.4e}")
u = np.array([1.0, -2.0, 0.5]); u /= np.linalg.norm(u)
F = lambda s, t_: np.real(np.exp(-1j * beta * s) * np.exp(1j * w * t_))      # along r = s u (u.r = s)
vc = crest_speed(F, beta, w, 0.0, (2 * PI / w) / 19)
p = np.cross(u, [0.3, 0.1, 0.9]); p /= np.linalg.norm(p)
check("E3 E0 e^{-j beta u.r} travels toward +u; its phase is constant on planes u.r = const",
      vc > 0 and np.isclose(np.exp(-1j * beta * u @ (0.37 * u + 2.1 * p)), np.exp(-1j * beta * 0.37)))
# template e^{j(ax + by + cz)} with (a, b, c) = -beta u
r0 = rng.uniform(-1, 1, 3); abc = -beta * u
check("E4 template e^{j(ax+by+cz)} = e^{-j beta u.r} with (a,b,c) = -beta u, a^2 + b^2 + c^2 = beta^2",
      np.isclose(np.exp(1j * abc @ r0), np.exp(-1j * beta * u @ r0)) and np.isclose(abc @ abc, beta ** 2))
b450 = 2 * PI * 450e6 * np.sqrt(4) / C3
check("E5 450 MHz, eps_r = 4, toward -z: beta = 6 pi rad/m, factor e^{+j6 pi z}, (a,b,c) = (0,0,+6 pi)",
      np.isclose(b450, 6 * PI) and np.allclose(-b450 * (-Z), [0, 0, 6 * PI]))
ud = (X + Y) / np.sqrt(2); abc = -2 * PI * ud
check("E6 toward (x+y)/sqrt2, beta = 2 pi: e^{-j sqrt2 pi (x+y)}, a = b = -sqrt2 pi = -4.44 rad/m, c = 0",
      np.allclose(abc, [-np.sqrt(2) * PI, -np.sqrt(2) * PI, 0]) and rounds(-np.sqrt(2) * PI, -4.44, 2)
      and np.isclose(np.exp(-1j * 2 * PI * ud @ r0), np.exp(-1j * np.sqrt(2) * PI * (r0[0] + r0[1]))))
check("E7 amplitude perpendicular to u: z_hat and x_hat - y_hat (and complex combinations) are; x_hat is not",
      np.isclose(Z @ ud, 0) and np.isclose((X - Y) @ ud, 0) and np.isclose(((1 + 2j) * Z + (0.5 - 1j) * (X - Y)) @ ud, 0) and not np.isclose(X @ ud, 0))
check("E8 |E(r)| is the same everywhere for E0 e^{-j beta u.r}",
      np.allclose([np.linalg.norm(np.array([1, 2j, 0]) * np.exp(-1j * beta * u @ rng.uniform(-3, 3, 3))) for _ in range(5)], np.sqrt(5)))

# =========================================================================================== F
sec("F. Page §5 — the E <-> H rule, the complex Poynting vector, the Faraday derivation, Maxwell by finite differences")
eta = 60 * PI; eps = 4 * EPS0x; mu = MU0x; w = 2 * PI * 2e8; beta = w * np.sqrt(mu * eps)
for k_ in range(3):
    u = rng.normal(size=3); u /= np.linalg.norm(u)
    E0v = rng.normal(size=3) + 1j * rng.normal(size=3); E0v -= u * (u @ E0v)          # complex, perpendicular to u
    H0v = np.cross(u, E0v) / eta
    check(f"F1.{k_} random complex E0 perp u: E = eta H x u recovers E, and E x H* = |E|^2/eta u",
          np.allclose(eta * np.cross(H0v, u), E0v) and np.allclose(np.cross(E0v, np.conj(H0v)), (np.vdot(E0v, E0v).real / eta) * u))
    Ef = from_phasor(lambda r: E0v * np.exp(-1j * beta * u @ r), w)
    Hf = from_phasor(lambda r: H0v * np.exp(-1j * beta * u @ r), w)
    res = maxwell_res(Ef, Hf, eps, mu, w, beta, seed=k_)
    Hbad = from_phasor(lambda r: -H0v * np.exp(-1j * beta * u @ r), w)
    check(f"F2.{k_} ... Re{{E e^jwt}}, Re{{H e^jwt}} satisfy both curl equations (FD); the reversed rotation does not",
          res < 1e-6 and maxwell_res(Ef, Hbad, eps, mu, w, beta, seed=k_) > 0.5, f"residual {res:.1e}")
# without the conjugate: E x H = (E.E)/eta u turns along z; Re{1/2 E x H} = (E0^2/2 eta) cos 2 beta z for a linear wave; 0 for circular
zs = np.linspace(0, 1, 7)
lin_ = [0.5 * np.real(np.cross(3 * X * np.exp(-1j * beta * s), 3 / eta * Y * np.exp(-1j * beta * s)))[2] for s in zs]
cir = np.cross((X - 1j * Y), np.cross(Z, X - 1j * Y) / eta)
check("F3 without the conjugate: E x H = (E.E/eta) u, still along u but with a coefficient turning as e^{-2j beta z};"
      " Re{1/2 E x H} = (E0^2/2eta) cos 2 beta z for a linear wave and 0 for a circular one",
      np.allclose(lin_, 9 / (2 * eta) * np.cos(2 * beta * zs)) and np.allclose(cir, 0))
# Faraday in phasor form: dEx/dz = -jw mu Hy, -dHy/dz = jw eps Ex with Hy = +-Ex/eta
for sgn in (+1, -1):
    Exz = lambda s: 2.0 * np.exp(-1j * sgn * beta * s); Hyz = lambda s: sgn * Exz(s) / eta
    s0, hs = 0.31, 1e-6
    d1 = (Exz(s0 + hs) - Exz(s0 - hs)) / (2 * hs); d2 = (Hyz(s0 + hs) - Hyz(s0 - hs)) / (2 * hs)
    check(f"F4 Ex = E0 e^{{{'-' if sgn > 0 else '+'}j beta z}}, Hy = {'+' if sgn > 0 else '-'}Ex/eta satisfies both 1-D phasor curl equations",
          np.isclose(d1, -1j * w * mu * Hyz(s0), rtol=1e-6) and np.isclose(-d2, 1j * w * eps * Exz(s0), rtol=1e-6))
check("F5 beta/(w mu) = sqrt(eps/mu) = 1/eta and beta/eta = w eps", np.isclose(beta / (w * mu), 1 / eta) and np.isclose(beta / eta, w * eps))

# =========================================================================================== G
sec("G. Page §5 — the notes' Example 1 table (every row)")
eta = ETA0; w = 2 * PI * 1e8; beta = w / C3; eps, mu = EPS0x, MU0x
E1 = lambda r: np.exp(1j * beta * r[1]) * Z
E1t = from_phasor(E1, w)
check("G1 row 1: E = cos(wt + beta y) z_hat <-> e^{j beta y} z_hat",
      all(np.allclose(E1t(r, t_), np.cos(w * t_ + beta * r[1]) * Z) for r, t_ in [(rng.uniform(-1, 1, 3), rng.uniform(0, 1e-8)) for _ in range(5)]))
vc = crest_speed(lambda yy, t_: np.cos(w * t_ + beta * yy), beta, w, 0, 1e-9)
check("G2 row 1 travels toward -y (u = -y_hat)", vc < 0)
uG = -Y; H1 = lambda r: np.cross(uG, E1(r)) / eta
check("G3 row 2: H = (1/eta)(-y) x z e^{j beta y} = -(e^{j beta y}/eta) x_hat; S direction z x (-x) = -y",
      np.allclose(H1(np.zeros(3)), -X / eta) and np.allclose(np.cross(Z, -X), -Y) and np.allclose(np.real(np.cross(E1(np.zeros(3)), np.conj(H1(np.zeros(3))))), -Y / eta))
check("G4 rows 1-2 satisfy Maxwell (FD)", maxwell_res(E1t, from_phasor(H1, w), eps, mu, w, beta) < 1e-6)
H3 = lambda r: -1j * np.exp(-1j * beta * r[2]) * Y
check("G5 row 3: H = sin(wt - beta z) y_hat <-> -j e^{-j beta z} y_hat (toward +z)",
      all(np.allclose(from_phasor(H3, w)(r, t_), np.sin(w * t_ - beta * r[2]) * Y) for r, t_ in [(rng.uniform(-1, 1, 3), rng.uniform(0, 1e-8)) for _ in range(5)])
      and crest_speed(lambda zz_, t_: np.sin(w * t_ - beta * zz_), beta, w, 0, 1e-9) > 0)
E4 = lambda r: eta * np.cross(H3(r), Z)
check("G6 row 4: E = eta H x z = -j eta e^{-j beta z} x_hat <-> eta sin(wt - beta z) x_hat (y x z = x)",
      np.allclose(E4(np.zeros(3)), -1j * eta * X) and np.allclose(np.cross(Y, Z), X)
      and all(np.allclose(from_phasor(E4, w)(r, t_), eta * np.sin(w * t_ - beta * r[2]) * X) for r, t_ in [(rng.uniform(-1, 1, 3), rng.uniform(0, 1e-8)) for _ in range(5)]))
check("G7 rows 3-4 satisfy Maxwell (FD)", maxwell_res(from_phasor(E4, w), from_phasor(H3, w), eps, mu, w, beta) < 1e-6)

# =========================================================================================== H
sec("H. Page §5 — the notes' Example 2 (two waves, one rule each)")
Hp, Hm = 0.7, 1.9
Ht = lambda r, t_: Hp * np.cos(w * t_ - beta * r[2]) * X + Hm * np.sin(w * t_ + beta * r[2]) * Y
Hph = lambda r: Hp * np.exp(-1j * beta * r[2]) * X - 1j * Hm * np.exp(1j * beta * r[2]) * Y
pts = [(rng.uniform(-2, 2, 3), rng.uniform(0, 1e-8)) for _ in range(6)]
check("H1 H~ = x H+ e^{-j beta z} - j y H- e^{j beta z}", all(np.allclose(from_phasor(Hph, w)(r, t_), Ht(r, t_)) for r, t_ in pts))
Eplus = lambda r: eta * np.cross(Hp * np.exp(-1j * beta * r[2]) * X, Z)
Eminus = lambda r: eta * np.cross(-1j * Hm * np.exp(1j * beta * r[2]) * Y, -Z)
check("H2 +z wave: eta H+ e^{-j beta z}(x X z) = -y eta H+ e^{-j beta z};  -z wave: eta(-j H- e^{j beta z})(y X -z) = +j x eta H- e^{j beta z}",
      np.allclose(Eplus(np.zeros(3)), -Y * eta * Hp) and np.allclose(Eminus(np.zeros(3)), 1j * X * eta * Hm))
Eph = lambda r: -Y * eta * Hp * np.exp(-1j * beta * r[2]) + 1j * X * eta * Hm * np.exp(1j * beta * r[2])
Et = lambda r, t_: -Y * eta * Hp * np.cos(w * t_ - beta * r[2]) - X * eta * Hm * np.sin(w * t_ + beta * r[2])
check("H3 E~ = -y eta H+ e^{-j beta z} + j x eta H- e^{j beta z} <-> E = -y eta H+ cos(wt - beta z) - x eta H- sin(wt + beta z)",
      all(np.allclose(from_phasor(Eph, w)(r, t_), Et(r, t_)) for r, t_ in pts) and np.isclose(np.real(1j * np.exp(0.77j)), -np.sin(0.77)))
check("H4 the notes' Example 2 satisfies both curl equations (FD): no sign error", maxwell_res(Et, Ht, eps, mu, w, beta) < 1e-6)
Ebad = from_phasor(lambda r: eta * np.cross(Hph(r), Z), w)
check("H5 using one u (= +z) for the whole sum breaks Faraday (one term flips)", maxwell_res(Ebad, Ht, eps, mu, w, beta) > 0.3)
Sp = np.cross(Eplus(np.zeros(3)), np.conj(Hp * X)); Sm = np.cross(Eminus(np.zeros(3)), np.conj(-1j * Hm * Y))
check("H6 each wave: E x H* along its own u (+z and -z)", Sp[2].real > 0 and Sm[2].real < 0 and np.allclose(Sp.imag, 0) and np.allclose(Sm.imag, 0))

# =========================================================================================== I
sec("I. Page §5/§7 — the 200 MHz wave's partner and power")
eta = 60 * PI; w = 4 * PI * 1e8; beta = 8 * PI / 3; eps, mu = 4 * EPS0x, MU0x
E200 = lambda r: 12 * np.exp(-1j * beta * r[1]) * Z
H200 = lambda r: np.cross(Y, E200(r)) / eta
check("I1 H~ = (1/60pi) y x z 12 e^{..} = (1/5pi) e^{..} x_hat = 63.7 mA/m; z x x = +y",
      np.allclose(H200(np.zeros(3)), X / (5 * PI)) and rounds(1e3 / (5 * PI), 63.7, 1) and np.allclose(np.cross(Z, X), Y))
check("I2 the 200 MHz E and H satisfy Maxwell in eps_r = 4 (FD)", maxwell_res(from_phasor(E200, w), from_phasor(H200, w), eps, mu, w, beta) < 1e-6)
S200 = tavg(lambda t_: np.cross(from_phasor(E200, w)(np.array([0, 0.3, 0]), t_), from_phasor(H200, w)(np.array([0, 0.3, 0]), t_)), 2 * PI / w, 64)
check("I3 <S> = 144/(120 pi) y = 0.382 y W/m^2 (quadrature) = 1/2 Re{E x H*}",
      np.allclose(S200, 144 / (120 * PI) * Y) and rounds(144 / (120 * PI), 0.382, 3)
      and np.allclose(0.5 * np.real(np.cross(E200(np.zeros(3)), np.conj(H200(np.zeros(3))))), S200))

# =========================================================================================== J
sec("J. Page §6 — the monochromatic current sheet in phasors (notes' Example 3 and the sine variation)")
eta = ETA0; w = 2 * PI * 1e8; beta = w / C3; eps, mu = EPS0x, MU0x
Js = 2 * X
def sheet(Jsph):
    def E(r):
        return -eta / 2 * Jsph * np.exp(-1j * beta * abs(r[2]))
    def H(r):
        n = Z if r[2] > 0 else -Z
        return 0.5 * np.cross(Jsph, n) * np.exp(-1j * beta * abs(r[2]))
    return E, H
Es, Hs = sheet(Js)
for zp in (0.37, -0.37):
    s = 1 if zp > 0 else -1
    r = np.array([0.1, -0.2, zp])
    check(f"J1 z {'>' if s > 0 else '<'} 0: box gives E~ = -eta e^{{-+j beta z}} x, H~ = {'-' if s > 0 else '+'}e^{{-+j beta z}} y (the notes' phasors)",
          np.allclose(Es(r), -eta * np.exp(-1j * s * beta * zp) * X) and np.allclose(Hs(r), -s * np.exp(-1j * s * beta * zp) * Y))
check("J2 1/2 (2x) X (+-z) = -+y;  (-eta x) X (-y) = +eta z above, (-eta x) X (+y) = -eta z below",
      np.allclose(0.5 * np.cross(2 * X, Z), -Y) and np.allclose(0.5 * np.cross(2 * X, -Z), Y)
      and np.allclose(np.cross(-eta * X, -Y), eta * Z) and np.allclose(np.cross(-eta * X, Y), -eta * Z))
for side in (+1, -1):
    reg = (lambda r: np.array([r[0], r[1], abs(r[2]) + 0.05])) if side > 0 else (lambda r: np.array([r[0], r[1], -abs(r[2]) - 0.05]))
    check(f"J3 sheet fields satisfy Maxwell on the {'z>0' if side > 0 else 'z<0'} side (FD)",
          maxwell_res(from_phasor(Es, w), from_phasor(Hs, w), eps, mu, w, beta, region=reg) < 1e-6)
tq = rng.uniform(0, 1e-8, 5)
Ep0, Em0 = from_phasor(Es, w), from_phasor(Es, w)
ok = all(np.allclose(from_phasor(Es, w)(np.array([0, 0, 1e-12]), t_), from_phasor(Es, w)(np.array([0, 0, -1e-12]), t_), atol=1e-6) for t_ in tq) and \
     all(np.allclose(np.cross(Z, from_phasor(Hs, w)(np.array([0, 0, 1e-12]), t_) - from_phasor(Hs, w)(np.array([0, 0, -1e-12]), t_)), 2 * np.cos(w * t_) * X, atol=1e-9) for t_ in tq)
check("J4 boundary conditions at z = 0: E continuous, z x (H(0+) - H(0-)) = J_s (n from medium 2 (z<0) into 1)", ok)
Ss = lambda zp: np.cross(Es(np.array([0, 0, zp])), np.conj(Hs(np.array([0, 0, zp]))))
check("J5 each wave's E x H* is along +n (away from the sheet)", Ss(0.4)[2].real > 0 and Ss(-0.4)[2].real < 0)
Es2, Hs2 = sheet(-2j * X)
check("J6 sine current 2 sin(wt) x: J~ = -2j x; E~ = j eta e^{-+j beta z} x, H~ = +-j e^{-+j beta z} y",
      np.allclose(np.real(-2j * np.exp(1j * w * tq)), 2 * np.sin(w * tq))
      and np.allclose(Es2(np.array([0, 0, 0.3])), 1j * eta * np.exp(-1j * beta * 0.3) * X) and np.allclose(Hs2(np.array([0, 0, 0.3])), 1j * np.exp(-1j * beta * 0.3) * Y)
      and np.allclose(Hs2(np.array([0, 0, -0.3])), -1j * np.exp(-1j * beta * 0.3) * Y))
ok = all(np.isclose(from_phasor(Es2, w)(np.array([0, 0, zp]), t_)[0], -eta * np.sin(w * t_ - beta * abs(zp))) and
         np.isclose(from_phasor(Hs2, w)(np.array([0, 0, zp]), t_)[1], -np.sign(zp) * np.sin(w * t_ - beta * abs(zp)))
         for zp in (0.3, -0.3) for t_ in tq)
check("J7 ... in time: E_x = -eta sin(wt -+ beta z), H_y = -+ sin(wt -+ beta z)", ok)

# =========================================================================================== K
sec("K. Page §7 — the product rule <ab> = 1/2 Re{A B*} (proof, quadrature, special cases, vector forms)")
w = 2 * PI * 50.0; T = 2 * PI / w
for k_ in range(4):
    Ap, Bp = (rng.normal() + 1j * rng.normal()), (rng.normal() + 1j * rng.normal())
    a = lambda t_: np.real(Ap * np.exp(1j * w * t_)); b = lambda t_: np.real(Bp * np.exp(1j * w * t_))
    tt = rng.uniform(0, T, 9)
    exp_ok = np.allclose(a(tt) * b(tt), 0.5 * np.real(Ap * np.conj(Bp)) + 0.5 * np.real(Ap * Bp * np.exp(2j * w * tt)))
    q = tavg_quad(lambda t_: a(t_) * b(t_), T)
    check(f"K1.{k_} ab = 1/2 Re{{A B*}} + 1/2 Re{{A B e^{{j2wt}}}} pointwise; <ab> (quad) = 1/2 Re{{A B*}} = 1/2 AB cos(theta_a - theta_b)",
          exp_ok and np.isclose(q, 0.5 * np.real(Ap * np.conj(Bp)), atol=1e-12) and np.isclose(q, 0.5 * abs(Ap) * abs(Bp) * np.cos(np.angle(Ap) - np.angle(Bp)), atol=1e-12))
check("K2 the 2w term averages to zero over a period", abs(tavg_quad(lambda t_: np.real((0.3 + 2j) * np.exp(2j * w * t_)), T)) < 1e-12)
check("K3 common phase cancels: <ab> unchanged when both phasors get e^{j phi}", np.isclose(0.5 * np.real(Ap * np.exp(0.9j) * np.conj(Bp * np.exp(0.9j))), 0.5 * np.real(Ap * np.conj(Bp))))
check("K4 <a^2> = 1/2 |A|^2; A = 1: <cos^2> = 1/2", np.isclose(tavg_quad(lambda t_: np.real(Ap * np.exp(1j * w * t_)) ** 2, T), 0.5 * abs(Ap) ** 2) and np.isclose(tavg_quad(lambda t_: np.cos(w * t_) ** 2, T), 0.5))
A_, B_ = 3.0, 2.0
ok = np.isclose(tavg_quad(lambda t_: A_ * np.cos(w * t_) * B_ * np.cos(w * t_), T), A_ * B_ / 2) and \
     abs(tavg_quad(lambda t_: A_ * np.cos(w * t_) * B_ * np.sin(w * t_), T)) < 1e-12 and \
     np.isclose(tavg_quad(lambda t_: A_ * np.cos(w * t_) * -B_ * np.cos(w * t_), T), -A_ * B_ / 2)
check("K5 in phase 1/2 AB, quadrature 0, antiphase -1/2 AB", ok)
q = tavg_quad(lambda t_: 3 * np.cos(w * t_ + np.radians(20)) * 2 * np.cos(w * t_ - np.radians(40)), T)
check("K6 example 3 cos(wt + 20 deg), 2 cos(wt - 40 deg): <ab> = 1/2 3 2 cos 60 deg = 1.5", np.isclose(q, 1.5))
# vector forms with random complex vectors
Ev, Hv, Jv = [rng.normal(size=3) + 1j * rng.normal(size=3) for _ in range(3)]
et = lambda t_: np.real(Ev * np.exp(1j * w * t_)); ht = lambda t_: np.real(Hv * np.exp(1j * w * t_)); jt = lambda t_: np.real(Jv * np.exp(1j * w * t_))
check("K7 <E x H> = 1/2 Re{E x H*} (quadrature, random complex vectors)",
      np.allclose([tavg_quad(lambda t_, i=i: np.cross(et(t_), ht(t_))[i], T) for i in range(3)], 0.5 * np.real(np.cross(Ev, np.conj(Hv)))))
check("K8 <J . E> = 1/2 Re{J . E*} (quadrature)", np.isclose(tavg_quad(lambda t_: jt(t_) @ et(t_), T), 0.5 * np.real(Jv @ np.conj(Ev))))
check("K9 order inside: 1/2 Re{E x H*} = 1/2 Re{E* x H} (either conjugate)", np.allclose(np.real(np.cross(Ev, np.conj(Hv))), np.real(np.cross(np.conj(Ev), Hv))))
E0c = np.array([1.2 * np.exp(0.4j), -0.7j, 0]); eta = 377.0
Sav = 0.5 * np.real(np.cross(E0c, np.conj(np.cross(Z, E0c) / eta)))
check("K10 one lossless wave: <S> = |E0|^2/(2 eta) u = eta |H0|^2/2 u; |E0|^2 adds perpendicular components whatever their phases",
      np.allclose(Sav, (1.2 ** 2 + 0.7 ** 2) / (2 * eta) * Z) and np.isclose(Sav[2], eta * np.vdot(np.cross(Z, E0c) / eta, np.cross(Z, E0c) / eta).real / 2))
check("K11 rms phasors (|A|/sqrt2) drop the 1/2: <ab> = Re{A_rms B_rms*}", np.isclose(np.real((Ap / np.sqrt(2)) * np.conj(Bp / np.sqrt(2))), 0.5 * np.real(Ap * np.conj(Bp))))

# =========================================================================================== L
sec("L. Page §7 — power examples: the notes' sheet two ways, Example 2's power, the traps")
eta = ETA0; w = 2 * PI * 1e8; beta = w / C3; T = 2 * PI / w
Es, Hs = sheet(2 * X)
for zp in (0.41, -0.41):
    r = np.array([0, 0, zp])
    qS = tavg(lambda t_: np.cross(from_phasor(Es, w)(r, t_), from_phasor(Hs, w)(r, t_)), T, 64)
    check(f"L1 <S> at z = {zp:+.2f}: quadrature = 1/2 Re{{E x H*}} = {'+' if zp > 0 else '-'}eta/2 z = {'+' if zp > 0 else '-'}60 pi z (188 W/m^2)",
          np.allclose(qS, np.sign(zp) * eta / 2 * Z) and np.allclose(0.5 * np.real(np.cross(Es(r), np.conj(Hs(r)))), qS) and rounds(60 * PI, 188, 0))
qJ = tavg_quad(lambda t_: -(2 * np.cos(w * t_)) * from_phasor(Es, w)(np.array([0, 0, 1e-15]), t_)[0], T)
check("L2 <-J_s . E(0,t)> = 1/2 Re{-J_s . E*(0)} = eta = 120 pi = 377 W/m^2 (quadrature; L20 route 2 eta cos^2 wt)",
      np.isclose(qJ, eta) and np.isclose(0.5 * np.real(-(2 * X) @ np.conj(Es(np.array([0, 0, 1e-15])))), eta)
      and np.isclose(tavg_quad(lambda t_: 2 * eta * np.cos(w * t_) ** 2, T), eta) and rounds(eta, 377, 0))
check("L3 energy balance: injected eta = eta/2 + eta/2 leaving the two faces", np.isclose(eta, eta / 2 + eta / 2))
Es2, Hs2 = sheet(-2j * X)
check("L4 sine current: (-j)(-j)* = 1, same averages", np.isclose((-1j) * np.conj(-1j), 1)
      and np.allclose(0.5 * np.real(np.cross(Es2(np.array([0, 0, .3])), np.conj(Hs2(np.array([0, 0, .3]))))), eta / 2 * Z))
check("L5 the e^{-+j beta z} factors cancel: <S> the same at every z", np.allclose([0.5 * np.real(np.cross(Es(np.array([0, 0, s])), np.conj(Hs(np.array([0, 0, s])))))[2] for s in (0.1, 0.5, 3.3)], eta / 2))
# Example 2's power
Hp, Hm = 0.7, 1.9
Hph = lambda r: Hp * np.exp(-1j * beta * r[2]) * X - 1j * Hm * np.exp(1j * beta * r[2]) * Y
Eph = lambda r: -Y * eta * Hp * np.exp(-1j * beta * r[2]) + 1j * X * eta * Hm * np.exp(1j * beta * r[2])
r = np.array([0.2, 0.1, 0.77])
check("L6 Example 2: H~* = x H+ e^{j beta z} + j y H- e^{-j beta z}", np.allclose(np.conj(Hph(r)), Hp * np.exp(1j * beta * r[2]) * X + 1j * Hm * np.exp(-1j * beta * r[2]) * Y))
check("L7 Example 2: E x H* = eta[(H+)^2 - (H-)^2] z; <S> (quadrature) = eta/2 [(H+)^2 - (H-)^2] z",
      np.allclose(np.cross(Eph(r), np.conj(Hph(r))), eta * (Hp ** 2 - Hm ** 2) * Z)
      and np.allclose(tavg(lambda t_: np.cross(from_phasor(Eph, w)(r, t_), from_phasor(Hph, w)(r, t_)), T, 64), eta / 2 * (Hp ** 2 - Hm ** 2) * Z))
# parallel polarizations: cross terms in S~ purely imaginary; instantaneous cross terms cancel exactly
E1a, E2a = 1.3 * np.exp(0.2j), 0.8 * np.exp(-1.1j)
Epar = lambda r: X * (E1a * np.exp(-1j * beta * r[2]) + E2a * np.exp(1j * beta * r[2]))
Hpar = lambda r: Y * (E1a * np.exp(-1j * beta * r[2]) - E2a * np.exp(1j * beta * r[2])) / eta
Sc = np.cross(Epar(r), np.conj(Hpar(r)))
check("L8 parallel counter-propagating waves: S~ = [(|E1|^2 - |E2|^2) + (purely imaginary cross terms)]/eta z",
      np.isclose(Sc[2].real, (abs(E1a) ** 2 - abs(E2a) ** 2) / eta) and abs(Sc[2].imag) > 1e-6)
ok = True
for _ in range(5):
    u = rng.normal(size=3); u /= np.linalg.norm(u)
    e1 = rng.normal(size=3); e1 -= u * (u @ e1); e2 = rng.normal(size=3); e2 -= u * (u @ e2)
    h1, h2 = np.cross(u, e1) / eta, -np.cross(u, e2) / eta
    ok &= np.allclose(np.cross(e1 + e2, h1 + h2), (e1 @ e1 - e2 @ e2) / eta * u)
check("L9 instantaneous S of two counter-propagating waves on one line: cross terms cancel exactly (Poynting-vector page)", ok)
# traps: 1/2 Re{E x H} varies; instantaneous S for one wave
check("L10 trap: 1/2 Re{E x H} (no conjugate) of one linear wave varies along z as cos 2 beta z (not an average)",
      np.allclose([0.5 * np.real(np.cross(np.exp(-1j * beta * s) * X, np.exp(-1j * beta * s) * Y / eta))[2] for s in zs], np.cos(2 * beta * zs) / (2 * eta)))
tg = np.linspace(0, T, 4001)
Slin = np.array([np.cross(np.cos(w * t_) * X, np.cos(w * t_) * Y / eta)[2] for t_ in tg])
check("L11 one LINEARLY polarized wave: instantaneous S swings between 0 and 2<S> at 2w",
      np.isclose(Slin.min(), 0, atol=1e-12) and np.isclose(Slin.max(), 2 * Slin.mean(), rtol=1e-3))
Eell = lambda t_: 3 * np.cos(w * t_) * X + 4 * np.cos(w * t_ + PI / 4) * Y
Sell = np.array([np.cross(Eell(t_), np.cross(Z, Eell(t_)) / eta)[2] for t_ in tg])
Scir = np.array([np.cross(np.cos(w * t_) * X + np.sin(w * t_) * Y, np.cross(Z, np.cos(w * t_) * X + np.sin(w * t_) * Y) / eta)[2] for t_ in tg])
check("L12 ... but NOT for one wave with out-of-phase perpendicular components (never 0) or a circular one (constant):"
      " the page's trap bullet must say 'linearly polarized' (fixed)", Sell.min() > 0.1 * Sell.mean() and np.allclose(Scir, Scir.mean()),
      f"elliptical min/mean = {Sell.min()/Sell.mean():.3f}, circular spread = {np.ptp(Scir):.1e}")
# Joule heating
for sgm in (5.8e7 + 0j, 2.0 - 3.0j, -1j * 4.0):
    Ec = np.array([1.1 + 0.4j, -0.3j, 0.2])
    q = tavg_quad(lambda t_: np.real(sgm * Ec * np.exp(1j * w * t_)) @ np.real(Ec * np.exp(1j * w * t_)), T)
    check(f"L13 J = sigma E with sigma = {sgm}: <J.E> (quad) = 1/2 Re{{sigma}} |E|^2", np.isclose(q, 0.5 * sgm.real * np.vdot(Ec, Ec).real, rtol=1e-9, atol=1e-12))
check("L14 real sigma: <sigma E^2> = 1/2 sigma E0^2", np.isclose(tavg_quad(lambda t_: 3.0 * (2 * np.cos(w * t_)) ** 2, T), 0.5 * 3.0 * 4))

# =========================================================================================== M
sec("M. Worked problem — phasors, E and power from a given H")
w = 2 * PI * 1e8; beta = 2 * PI
Hgiven = lambda r, t_: 0.3 * np.cos(w * t_ + beta * r[2]) * X - 0.4 * np.sin(w * t_ + beta * r[2] - PI / 4) * Y
f = w / (2 * PI); T = 1 / f; lam = 2 * PI / beta; vp = w / beta
check("M1 (a) f = 100 MHz, T = 10 ns, lambda = 1 m, v_p = 1e8 m/s = c/3", np.isclose(f, 1e8) and np.isclose(T, 1e-8) and np.isclose(lam, 1) and np.isclose(vp, C3 / 3))
check("M2 (a) same signs of t and z terms -> travels toward -z (crest tracked)", crest_speed(lambda zz_, t_: np.cos(w * t_ + beta * zz_), beta, w, 0, T / 17) < 0)
epsr = (C3 / vp) ** 2; eta = ETA0 / np.sqrt(epsr)
check("M3 (a) eps_r = 9 (non-magnetic), eta = 120 pi/3 = 40 pi = 125.7 Ohm", np.isclose(epsr, 9) and np.isclose(eta, 40 * PI) and rounds(eta, 125.7, 1))
Hph = lambda r: (0.3 * X + 0.4 * np.exp(1j * PI / 4) * Y) * np.exp(1j * beta * r[2])
pts = [(rng.uniform(-1, 1, 3), rng.uniform(0, T)) for _ in range(8)]
check("M4 (b) H~ = (0.3 x + 0.4 e^{j pi/4} y) e^{j 2 pi z}: reproduces the given H(z,t)", all(np.allclose(from_phasor(Hph, w)(r, t_), Hgiven(r, t_)) for r, t_ in pts))
check("M5 (b) -0.4 (-j) e^{-j pi/4} = 0.4 j e^{-j pi/4} = 0.4 e^{j pi/4}", np.isclose(-0.4 * (-1j) * np.exp(-1j * PI / 4), 0.4 * np.exp(1j * PI / 4)))
check("M6 (b) spot check H_y(0,0) = -0.4 sin(-pi/4) = +0.283 = Re{0.4 e^{j pi/4}}", rounds(-0.4 * np.sin(-PI / 4), 0.283, 3) and np.isclose(-0.4 * np.sin(-PI / 4), (0.4 * np.exp(1j * PI / 4)).real))
check("M7 (b) H_y = 0.4 cos(wt + 2 pi z + pi/4): leads the x component by 45 deg",
      np.allclose(-0.4 * np.sin(w * tt + 0.3 - PI / 4), 0.4 * np.cos(w * tt + 0.3 + PI / 4)))
true = PI / 4
wrong = {"drop the minus": np.angle(-1j * 0.4 * np.exp(-1j * PI / 4)), "forget the -j": np.angle(-0.4 * np.exp(-1j * PI / 4)), "forget both": np.angle(0.4 * np.exp(-1j * PI / 4))}
offs = {k_: abs((np.degrees(v_ - true) + 180) % 360 - 180) for k_, v_ in wrong.items()}
check("M8 (b) trap: the slips give 0.4 e^{-j3pi/4}, 0.4 e^{+j3pi/4}, 0.4 e^{-j pi/4}; off by 180, 90, 90 deg",
      np.isclose(wrong["drop the minus"], -3 * PI / 4) and np.isclose(wrong["forget the -j"], 3 * PI / 4) and np.isclose(wrong["forget both"], -PI / 4)
      and np.allclose(sorted(offs.values()), [90, 90, 180]), str({k_: round(v_) for k_, v_ in offs.items()}))
u = -Z
check("M9 (c) x X (-z) = +y, y X (-z) = -x", np.allclose(np.cross(X, u), Y) and np.allclose(np.cross(Y, u), -X))
Eph = lambda r: eta * np.cross(Hph(r), u)
check("M10 (c) E~ = eta H~ x u = (-16 pi e^{j pi/4} x + 12 pi y) e^{j 2 pi z}; -50.3, 37.7",
      np.allclose(Eph(np.zeros(3)), -16 * PI * np.exp(1j * PI / 4) * X + 12 * PI * Y) and rounds(16 * PI, 50.3, 1) and rounds(12 * PI, 37.7, 1))
Sc = np.cross(Eph(np.array([0, 0, 0.3])), np.conj(Hph(np.array([0, 0, 0.3]))))
check("M11 (c) E x H* = 40pi[0.09 y X x - 0.16 x X y] = -10 pi z (along -z); |E|/|H| = 20 pi/0.5 = 40 pi",
      np.allclose(Sc, -10 * PI * Z) and np.isclose(np.linalg.norm(Eph(np.zeros(3))), 20 * PI) and np.isclose(np.linalg.norm(Hph(np.zeros(3))), 0.5))
Et = lambda r, t_: -16 * PI * np.cos(w * t_ + beta * r[2] + PI / 4) * X + 12 * PI * np.cos(w * t_ + beta * r[2]) * Y
check("M12 (d) E(z,t) = -16 pi cos(wt + 2 pi z + pi/4) x + 12 pi cos(wt + 2 pi z) y = Re{E~ e^{jwt}} = eta H(t) x (-z)",
      all(np.allclose(from_phasor(Eph, w)(r, t_), Et(r, t_)) and np.allclose(eta * np.cross(Hgiven(r, t_), u), Et(r, t_)) for r, t_ in pts))
res = maxwell_res(Et, Hgiven, 9 * EPS0x, MU0x, w, beta)
check("M13 (d) the given H and the found E satisfy both curl equations in eps = 9 eps0, mu0 (FD)", res < 1e-6, f"residual {res:.1e}")
check("M14 (d) the reversed rotation (u = +z) fails Faraday", maxwell_res(lambda r, t_: -Et(r, t_), Hgiven, 9 * EPS0x, MU0x, w, beta) > 0.5)
Sq = tavg(lambda t_: np.cross(Et(np.array([0, 0, -3.0]), t_), Hgiven(np.array([0, 0, -3.0]), t_)), T, 64)
check("M15 (e) <S> (quadrature at z = -3 m) = 1/2 Re{E x H*} = -5 pi z = -15.7 z W/m^2", np.allclose(Sq, -5 * PI * Z) and rounds(5 * PI, 15.71, 2))
Hx_only = lambda r, t_: 0.3 * np.cos(w * t_ + beta * r[2]) * X
Hy_only = lambda r, t_: Hgiven(r, t_) - Hx_only(r, t_)
Sx = tavg(lambda t_: np.cross(eta * np.cross(Hx_only(np.zeros(3), t_), u), Hx_only(np.zeros(3), t_)), T, 64)
Sy = tavg(lambda t_: np.cross(eta * np.cross(Hy_only(np.zeros(3), t_), u), Hy_only(np.zeros(3), t_)), T, 64)
check("M16 (e) term by term: -1.8 pi = -5.65 and -3.2 pi = -10.05 W/m^2 (quadrature); they add to -5 pi",
      np.allclose(Sx, -1.8 * PI * Z) and np.allclose(Sy, -3.2 * PI * Z) and rounds(1.8 * PI, 5.65, 2) and rounds(3.2 * PI, 10.05, 2) and np.allclose(Sx + Sy, Sq))
check("M17 (e) trap: (0.3 + 0.4)^2 = 0.49 != 0.25; eta |H|^2 = 10 pi is |S~|, not <S>", np.isclose(0.7 ** 2, 0.49) and np.isclose(eta * 0.25, 10 * PI))
check("M18 (e) S = -eta |H|^2 z at every instant; <|H|^2> = 0.125 (A/m)^2",
      all(np.allclose(np.cross(Et(r, t_), Hgiven(r, t_)), -eta * (Hgiven(r, t_) @ Hgiven(r, t_)) * Z) for r, t_ in pts)
      and np.isclose(tavg(lambda t_: Hgiven(np.zeros(3), t_) @ Hgiven(np.zeros(3), t_), T, 64), 0.125))
check("M19 (f) window 0.25 m^2: <P> = 5 pi 0.25 = 1.25 pi = 3.93 W", rounds(5 * PI * 0.25, 3.93, 2))
H00, E00 = Hgiven(np.zeros(3), 0.0), Et(np.zeros(3), 0.0)
S00 = np.cross(E00, H00)
check("M20 (f) H(0,0) = 0.300 x + 0.283 y; E(0,0) = -35.5 x + 37.7 y; S = (-10.05 - 11.31) z = -21.4 z W/m^2",
      np.allclose(H00, [0.3, 0.4 * np.sin(PI / 4), 0]) and rounds(E00[0], -35.5, 1) and rounds(E00[1], 37.7, 1)
      and rounds(E00[0] * H00[1], -10.05, 2) and rounds(-E00[1] * H00[0], -11.31, 2) and rounds(S00[2], -21.4, 1))
tg = np.linspace(0, T, 20001)
Sz = np.array([np.cross(Et(np.zeros(3), t_), Hgiven(np.zeros(3), t_))[2] for t_ in tg])
check("M21 (f) instantaneous S pulses at 2w between -4.2 and -27.2 W/m^2, never reverses, never reaches zero",
      rounds(Sz.max(), -4.2, 1) and rounds(Sz.min(), -27.2, 1) and Sz.max() < 0, f"{Sz.max():.3f} .. {Sz.min():.3f}")
k2 = np.abs(np.fft.rfft(Sz[:-1]))
check("M22 (f) ... the ripple is at 2w (2 cycles per period)", np.argmax(k2[1:]) + 1 == 2)
murv, epsv = 4, 2.25; etav = ETA0 * np.sqrt(murv / epsv)
check("M23 variant mu_r = 4, eps_r = 2.25: same mu_r eps_r = 9 (same beta, v_p); eta = 160 pi = 503 Ohm (4x); <S> = -20 pi = -62.8 W/m^2",
      np.isclose(murv * epsv, 9) and np.isclose(etav, 160 * PI) and rounds(etav, 503, 0) and np.isclose(etav / eta, 4)
      and np.isclose(-0.5 * etav * 0.25, -20 * PI) and rounds(-20 * PI, -62.8, 1))
check("M24 variant fields satisfy Maxwell in mu = 4 mu0, eps = 2.25 eps0 (FD)",
      maxwell_res(lambda r, t_: etav / eta * Et(r, t_), Hgiven, 2.25 * EPS0x, 4 * MU0x, w, beta) < 1e-6)
check("M25 phasors.md: with eta = 40 pi the whole wave carries 5 pi = 15.7 W/m^2", rounds(0.5 * 40 * PI * 0.25, 15.7, 1))

# =========================================================================================== N
sec("N. Figures (figs_l21.py) — numbers and directions drawn")
check("N1 snapshot-record: at z = lambda/4 the record is the z = 0 record delayed by T/4 (troughs at 1.5T and 1.75T)",
      np.isclose(np.cos(2 * PI * 1.5), -1) and np.isclose(np.cos(2 * PI * 1.75 - PI / 2), -1))
zz = np.linspace(1.9, 2.3, 400001)
check("N2 snapshot-record: the crest at z = 2 lambda moves to 2.125 lambda at t = T/8 (+z, lambda/8)", np.isclose(zz[np.argmax(np.cos(PI / 4 - 2 * PI * zz))], 2.125, atol=1e-5))
for sgn in (-1, +1):
    zz = np.linspace(0.8, 1.2, 400001)
    check(f"N3 direction-trap row {'A' if sgn < 0 else 'B'}: crest at lambda moves to {1 - sgn/8} lambda at T/8 (toward {'+' if sgn < 0 else '-'}z)",
          np.isclose(zz[np.argmax(np.cos(PI / 4 + sgn * 2 * PI * zz))], 1 - sgn / 8, atol=1e-5))
    phis = [sgn * 2 * PI * k_ / 8 for k_ in range(9)]
    turn = np.sign(np.cross([np.cos(phis[0]), np.sin(phis[0]), 0], [np.cos(phis[1]), np.sin(phis[1]), 0])[2])
    check(f"N4 direction-trap row {'A' if sgn < 0 else 'B'}: dial arrows turn {'clockwise' if sgn < 0 else 'counterclockwise'} as z grows (screen frame, z out)", turn == sgn)
th = PI / 6; a0 = np.array([np.cos(th), np.sin(th), 0])
check("N5 rotating-arrow: jA drawn at theta + 90 deg = z_hat x A; -jA at theta - 90 deg = -z_hat x A (screen frame)",
      np.allclose(np.cross(Z, a0), [np.cos(th + PI / 2), np.sin(th + PI / 2), 0]) and np.allclose(np.cross(-Z, a0), [np.cos(th - PI / 2), np.sin(th - PI / 2), 0]))
check("N6 rotating-arrow: dots at theta + k pi/4 turn counterclockwise (z component of successive cross products > 0)",
      all(np.cross([np.cos(th + k_ * PI / 4), np.sin(th + k_ * PI / 4), 0], [np.cos(th + (k_ + 1) * PI / 4), np.sin(th + (k_ + 1) * PI / 4), 0])[2] > 0 for k_ in range(8)))
check("N7 rotating-arrow: dashed curve A sin(wt + theta) is the shadow of -jA", np.allclose(np.real(-1j * np.exp(1j * th) * np.exp(1j * tt * 1e3)), np.sin(tt * 1e3 + th)))
check("N8 time-average: <ab> = 0.4 cos(phi) = 0.40, 0.20, 0 for phi = 0, 60, 90 deg; product min 0, -0.20, -0.40",
      np.allclose([tavg_quad(lambda t_, p_=p_: np.cos(t_) * 0.8 * np.cos(t_ - np.radians(p_)), 2 * PI) for p_ in (0, 60, 90)], [0.4, 0.2, 0], atol=1e-12)
      and np.allclose([min(np.cos(tg2) * 0.8 * np.cos(tg2 - np.radians(p_))) for p_ in (0, 60, 90) for tg2 in [np.linspace(0, 2 * PI, 20001)]], [0, -0.2, -0.4], atol=1e-6))
check("N9 dispersion diagram: dielectric eps_r = 4 is w = c beta/2; vacuum w = c beta; plasma hyperbola above the light line",
      all(np.sqrt(1 + b * b) > b for b in np.linspace(0, 3.2, 50)) and np.isclose(1 / np.sqrt(4), 0.5))

# =========================================================================================== Z
sec("Z. Page text after the review's fixes (the fixed wording is present, the old wording gone)")
P21 = open("/home/claude/work/content-src/3-maxwell-and-waves/21-monochromatic-waves-and-phasor-notation.md").read()
def has(s): return s in P21
check("Z1 power trap restricted to a linearly polarized wave", has("For one linearly polarized wave it swings between 0 and twice the average") and not has("For one wave it swings between 0"))
check("Z2 conjugate paragraph: E x H without conjugate is along u with a turning coefficient (no 'points nowhere')", not has("points nowhere in particular"))
check("Z3 Lecture 22 pointer: complex eta adds a phase between E and H (no 'breaks the rides along')", not has("breaks the \"rides along unchanged\""))
check("Z4 §2: no 'quantum mechanics' among the real-cosine wave equations", not has("plasma physics or quantum mechanics"))
check("Z5 §2 plasma: beta = 0.0922 rad/m with f_p = 8.98 MHz", has("$\\beta = 0.0922$ rad/m") and not has("0.0923"))
check("Z6 §1: 'time-harmonic' attributed to the notes, not to exam papers", not has("Exam papers also say *time-harmonic* or *co-sinusoidal*"))
check("Z7 On exams: S19 HE3 #1a(i) wording no longer pairs (wt + beta x) with SP17 #4a", not has("both with $(\\omega t + \\beta x)$"))
check("Z8 §2 opening calls w/beta the phase velocity", has("the phase velocity always follows from it as $v_p = \\omega/\\beta = \\lambda f$"))
check("Z9 conjugate trap restricted to a linearly polarized wave", has("for a single linearly polarized wave it varies along $z$ as $\\cos2\\beta z$"))
check("Z10 derivative rule: 'rises fastest' a quarter period before the peak (not 'steepest')", has("A cosine rises fastest a quarter period before its peak"))
check("Z11 the notes' margin plots are described as one above the other", has("one above the other in the margin") and not has("side by side in the margin"))
check("Z12 product-rule proof defines A, B, theta_a, theta_b", has("Here $\\tilde A = Ae^{j\\theta_a}$ and $\\tilde B = Be^{j\\theta_b}$"))
check("Z13 phone width: derivative-rule display split over two lines; plasma display without \\quad spacing",
      has("\\frac{d}{dt}\\text{Re}\\{\\tilde Ae^{j\\omega t}\\} &= ") and has("\\ \\Longrightarrow\\ \\beta^2"))
PH = open("/home/claude/work/content-src/concepts/phasors.md").read()
check("Z15 Lecture 22 pointer uses L22's notation: complex gamma = alpha + j beta (beta stays real), on the page and in phasors.md",
      has("a complex propagation constant $\\gamma = \\alpha + j\\beta$") and not has("complex $\\beta$ and $\\eta$")
      and "complex $\\beta$ and $\\eta$" not in PH)
# the worked problem's (f) numbers that the fixed trap bullet now points to: elliptical wave never reaches zero
check("Z14 the trap bullet's pointer is right: the worked problem's S(t) never reaches 0 (min 4.17 W/m^2)", Sz.max() < -4.0)

print(f"\n{NP[0]} PASS, {NP[1]} FAIL")
