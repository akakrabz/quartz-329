#!/usr/bin/env python3
"""Verification of every number, sign and direction on the Lecture 21 pages of the ECE 329 study site.

Pages checked:
  content-src/3-maxwell-and-waves/21-monochromatic-waves-and-phasor-notation.md   (sections B-J, M)
  content-src/concepts/phasors.md, concepts/dispersion-relation.md, the new section of concepts/plane-waves.md (L)
  content-src/problems/phasors-e-and-power-from-a-given-h.md                      (K)
  figs_l21.py (directions in the screen frame X right, Y up, Z out of the screen; plotted shifts and averages) (F)
numpy only. Phasor identities are checked by sampling Re{A e^{jwt}} on a fine time grid; every time average is a
quadrature over one period (mean over N equally spaced samples, exact for trigonometric polynomials of degree < N)
compared with 1/2 Re{A B*}; every vector direction is an explicit np.cross; Maxwell's curl equations are checked
by central finite differences.
"""
import numpy as np

mu0 = 1.25663706212e-6
eps0 = 8.8541878128e-12
c = 1 / np.sqrt(mu0 * eps0)
eta0 = np.sqrt(mu0 / eps0)
kB = 1.380649e-23                 # J/K (exact, SI 2019)
amu = 1.66053906660e-27           # kg
qe = 1.602176634e-19              # C
me = 9.1093837015e-31             # kg
X, Y, Z = np.eye(3)
cr = np.cross
rng = np.random.default_rng(21)
ok_count = 0

def ok(cond, msg):
    global ok_count
    assert cond, "FAILED: " + msg
    ok_count += 1
    print("ok  ", msg)

def _fmt(a):
    a = np.real_if_close(np.asarray(a))
    if a.size == 1:
        return f"{complex(a.item()):.6g}".strip("()").replace("+0j", "") if np.iscomplexobj(a) else f"{float(a.item()):.6g}"
    with np.printoptions(precision=5, suppress=False, linewidth=200):
        return str(a) if a.size <= 8 else f"[{a.size} values, max {np.max(np.abs(a)):.4g}]"

def close(a, b, msg, rtol=1e-6, atol=1e-12):
    ok(np.allclose(a, b, rtol=rtol, atol=atol), f"{msg}: {_fmt(a)} vs {_fmt(b)}")

def tavg(f, w, N=4096):
    """time average of f(t) over one period 2 pi / w (rectangle rule on a periodic grid: exact for low-order trig polynomials)"""
    t = np.arange(N) * (2 * np.pi / w) / N
    return np.mean(f(t), axis=-1)

def re_t(Ph, w, t):
    """time function Re{Ph e^{jwt}} for scalar or vector phasor Ph (vector: shape (3,)), t array"""
    Ph = np.asarray(Ph, dtype=complex)
    if Ph.ndim == 0:
        return np.real(Ph * np.exp(1j * w * t))
    return np.real(Ph[:, None] * np.exp(1j * w * t)[None, :])

def ang_deg(zc):
    return np.degrees(np.angle(zc))

print("=== A. constants")
close(c, 2.99792458e8, "c")
close(eta0, 376.730313, "eta0 [ohm]")
close(120 * np.pi, 376.991118, "120 pi")
close(60 * np.pi, 188.4956, "60 pi = eta0/2 with eta0 = 120 pi", rtol=1e-6)

print("=== B. Section 1 example: E = 12 cos(4pi e8 t - (8pi/3) y) z in a non-magnetic lossless medium")
w1, b1 = 4 * np.pi * 1e8, 8 * np.pi / 3
close(w1 / (2 * np.pi), 200e6, "f = 200 MHz")
close(2 * np.pi / w1, 5e-9, "T = 5 ns")
close(b1, 8.37758, "beta = 8 pi/3 = 8.38 rad/m", rtol=1e-5)
close(2 * np.pi / b1, 0.75, "lambda = 0.75 m")
close(w1 / b1, 1.5e8, "v_p = 1.5e8 m/s")
close((2 * np.pi / b1) * (w1 / (2 * np.pi)), 1.5e8, "lambda f = v_p")
close((3e8 / (w1 / b1)) ** 2, 4.0, "eps_r = (c/v_p)^2 = 4 with c = 3e8 (mu_r = 1)")
close((c / (w1 / b1)) ** 2, 3.9945, "eps_r with exact c = 3.994 (page says 'taking c = 3e8')", rtol=1e-4)
eta1 = 120 * np.pi / 2
close(eta1, 60 * np.pi, "eta = eta0/sqrt(4) = 60 pi = 188 ohm")
close(b1 * 0.25, 2 * np.pi / 3, "probes 25 cm apart: phase lag beta*dy = 2pi/3 rad (120 deg)")
close(0.25 / (w1 / b1), 1.6667e-9, "delay dy/v_p = 1.67 ns", rtol=1e-4)
close(0.25 / (w1 / b1), (2 * np.pi / w1) / 3, "delay = T/3")
# direction: crest of cos(wt - b y) moves toward +y
t0, dt = 0.0, 1e-11
ycrest = lambda t: (w1 * t) / b1          # phase zero
ok(ycrest(t0 + dt) > ycrest(t0), "crest of cos(wt - beta y) moves toward +y")

print("=== C. spectrum table (notes p.4 chart), f = c/lambda with c = 3e8; memorized pairs")
for lam, f_page in ((1e3, 300e3), (1e-2, 30e9), (1e-5, 30e12), (0.5e-6, 600e12), (1e-8, 3e16), (1e-10, 3e18), (1e-12, 3e20)):
    close(3e8 / lam, f_page, f"lambda = {lam:g} m -> f = {f_page:g} Hz")
for f, lam_page in ((1e6, 300), (100e6, 3), (1e9, 0.30), (10e9, 0.03)):
    close(3e8 / f, lam_page, f"{f:g} Hz <-> {lam_page} m")
close(3e8 / 400e-9, 750e12, "400 nm <-> 750 THz")
close(3e8 / 700e-9, 428.6e12, "700 nm <-> 430 THz", rtol=2e-3)
# the chart's frequency bar is schematic: tick x-positions read with a pixel ruler on the 220-dpi render of p.4
# (pdftoppm -r 220; original pixels), labels 10^4, 10^8, 10^12, 10^15, 10^16, 10^18, 10^20 Hz
ticks = {4: 517, 8: 777, 12: 1065, 15: 1339, 16: 1506, 18: 1726, 20: 1938}
keys = sorted(ticks)
pxdec = [(ticks[b] - ticks[a]) / (b - a) for a, b in zip(keys, keys[1:])]
print("     px per decade between chart ticks:", [round(p) for p in pxdec])
ok(max(pxdec) / min(pxdec) > 2, "chart frequency bar is not evenly spaced in decades (schematic): 65 to 167 px per decade")
# the microwave label (10^-2 m, i.e. 3e10 Hz) stands over x ~ 865 px, which the bar's local scale reads as ~2e9 Hz
logf = 8 + 4 * (865 - ticks[8]) / (ticks[12] - ticks[8])
close(10 ** logf, 1.7e9, "microwave label sits over ~2e9 Hz on the bar, not 3e10 Hz", rtol=0.1)

print("=== D. dispersion relations")
# D1. TEM in a dielectric: beta = w sqrt(mu eps), v_p independent of w
for f in (1e6, 1e8, 1e10):
    w = 2 * np.pi * f; eps = 4 * eps0
    close(w / (w * np.sqrt(mu0 * eps)), 1 / np.sqrt(mu0 * eps), f"TEM eps_r=4: v_p = 1/sqrt(mu eps) at f = {f:g} Hz")
# D2. sound in a monatomic gas: v = sqrt(5 kB T / 3 m)
vs = lambda A, T, g=5 / 3: np.sqrt(g * kB * T / (A * amu))
close(vs(4.002602, 300), 1019.1, "helium 300 K: 1019 m/s", rtol=1e-4)
close(vs(39.948, 300), 322.6, "argon 300 K: 323 m/s", rtol=1e-3)
close(vs(4.002602, 293.15), 1007, "helium 20 C: 1007 m/s (handbook 1007 m/s)", rtol=1e-3)
close(vs(39.948, 293.15), 319, "argon 20 C: 319 m/s (handbook 319 m/s)", rtol=1e-3)
close(vs(28.9647, 293.15, 7 / 5), 343.2, "air 20 C with gamma = 7/5: 343 m/s (handbook 343 m/s)", rtol=1e-3)
close(vs(28.9647, 293.15, 5 / 3), 374.5, "air 20 C with the monatomic 5/3: 375 m/s (wrong for air)", rtol=1e-3)
close(vs(4.002602, 300) / 440, 2.32, "440 Hz in helium: lambda = 2.32 m", rtol=2e-3)
close(vs(39.948, 300) / 440, 0.733, "440 Hz in argon: lambda = 0.73 m", rtol=2e-3)
close(vs(4.002602, 300) / vs(39.948, 300), np.sqrt(39.948 / 4.002602), "ratio = sqrt(m_Ar/m_He)")
close(np.sqrt(39.95 / 4.003), 3.159, "sqrt(39.95/4.003) = 3.16", rtol=1e-3)
# dispersion relation form: beta = w sqrt(m / (5/3 kB T)) gives v = w/beta
A_, T_ = 4.002602, 300.0
for f in (100.0, 440.0, 1e4):
    w = 2 * np.pi * f; beta = w * np.sqrt(A_ * amu / (5 / 3 * kB * T_))
    close(w / beta, vs(A_, T_), f"acoustic v_p = w/beta independent of f ({f:g} Hz)")
# D3. plasma
coef = np.sqrt(qe ** 2 / (me * eps0)) / (2 * np.pi)
close(coef, 8.98, "f_p = 8.98 sqrt(N) Hz", rtol=1e-3)
close(coef ** 2, 80.6, "(f_p^2 = 80.6 N, Rao's form)", rtol=1e-3)
N = 1e12; fp = coef * np.sqrt(N); wp = 2 * np.pi * fp
close(fp, 8.98e6, "N = 1e12 m^-3: f_p = 8.98 MHz (about 9 MHz)", rtol=1e-3)
# handbook: daytime F2-layer peak densities ~ 3e11 to 2e12 m^-3, critical frequencies foF2 ~ 4 to 13 MHz
ok(4e6 < coef * np.sqrt(3e11) < 13e6 and 4e6 < coef * np.sqrt(2e12) < 13e6, f"typical daytime N 3e11..2e12 m^-3 -> f_p {coef*np.sqrt(3e11)/1e6:.1f}..{coef*np.sqrt(2e12)/1e6:.1f} MHz (handbook foF2 range)")
def plasma(f):
    w = 2 * np.pi * f; beta = np.sqrt(w ** 2 - wp ** 2) / c
    return w, beta, 2 * np.pi / beta, w / beta, c ** 2 * beta / w     # w, beta, lambda, v_p, v_g = dw/dbeta
w10, bt10, l10, vp10, vg10 = plasma(10e6)
close(bt10, 0.0923, "10 MHz: beta = 0.0923 rad/m", rtol=2e-3)
close(l10, 68.1, "10 MHz: lambda = 68.1 m", rtol=1e-3)
close(c / 10e6, 29.98, "10 MHz vacuum lambda = 30.0 m", rtol=1e-3)
close(vp10, 6.81e8, "10 MHz: v_p = 6.81e8 m/s", rtol=1e-3)
close(vp10 / c, 2.27, "10 MHz: v_p = 2.27 c", rtol=2e-3)
close(l10 * 10e6, vp10, "v_p = lambda f")
close(vg10 / c, 0.440, "10 MHz: v_g = 0.440 c", rtol=1e-3)
close(vp10 * vg10, c ** 2, "v_p v_g = c^2")
# v_g as a numerical derivative dw/dbeta of the dispersion relation
bb = lambda w: np.sqrt(w ** 2 - wp ** 2) / c
dw = 1e-6 * w10
close((2 * dw) / (bb(w10 + dw) - bb(w10 - dw)), vg10, "v_g = dw/dbeta numerically", rtol=1e-6)
close(plasma(100e6)[3] / c, 1.004, "100 MHz: v_p = 1.004 c", rtol=2e-4)
ok(8e6 ** 2 - fp ** 2 < 0, "below f_p (8 MHz): beta^2 < 0, no travelling wave")
# figure P: w = 1.5 w_p
bP = np.sqrt(1.5 ** 2 - 1)
close(1.5 / bP, 1.342, "figure P: v_p = 1.34 c", rtol=1e-3)
close(bP / 1.5, 0.745, "figure P: v_g = 0.75 c", rtol=1e-3)
close((1.5 / bP) * (bP / 1.5), 1.0, "figure P: v_p v_g = c^2")
# D4. the plasma derivation: d2E/dz2 = mu0 dJ/dt + mu0 eps0 d2E/dt2 with dJ/dt = (N e^2/m) E, trial cos(wt - beta z)
w = w10; beta = bt10; E0 = 1.0
Ef = lambda z, t: E0 * np.cos(w * t - beta * z)
z0, t0 = 3.7, 2.1e-8; hz, ht = 1e-2, 1e-11
d2z = (Ef(z0 + hz, t0) - 2 * Ef(z0, t0) + Ef(z0 - hz, t0)) / hz ** 2
d2t = (Ef(z0, t0 + ht) - 2 * Ef(z0, t0) + Ef(z0, t0 - ht)) / ht ** 2
rhs = mu0 * (N * qe ** 2 / me) * Ef(z0, t0) + mu0 * eps0 * d2t
close(d2z, rhs, "plasma wave equation with the collisionless current holds for beta^2 = (w^2 - wp^2)/c^2", rtol=1e-4)
# the collisionless current lags E by 90 deg: m dv/dt = -eE -> v = -(e/(m w)) E0 sin(wt) for E = E0 cos wt; J = -N e v
tt = np.linspace(0, 2 * np.pi / w, 2001)
J = N * qe ** 2 / (me * w) * E0 * np.sin(w * tt)          # = (N e^2/m) * integral of E dt
dJdt = np.gradient(J, tt)
close(dJdt[100:-100], (N * qe ** 2 / me) * E0 * np.cos(w * tt[100:-100]), "dJ/dt = (N e^2/m) E", rtol=1e-4, atol=1e-6 * N * qe ** 2 / me)
sig = N * qe ** 2 / (me * (0 + 1j * w))
close(sig, -1j * N * qe ** 2 / (me * w), "Drude sigma with nu = 0 is -j N e^2/(m w) (purely imaginary)")
close(eps0 + sig / (1j * w), eps0 * (1 - wp ** 2 / w ** 2), "effective permittivity eps0 (1 - wp^2/w^2) (concept page)")

print("=== E. phasor rules")
w = 2 * np.pi * 50.0
t = np.linspace(0, 0.05, 5001)
for A_, th in ((1.0, 0.0), (2.5, 0.7), (0.3, -2.2)):
    close(re_t(A_ * np.exp(1j * th), w, t), A_ * np.cos(w * t + th), f"Re{{A e^(j th) e^(jwt)}} = A cos(wt + th), A = {A_}, th = {th}")
# sine rule and the conversion table (8 rows)
bz, zz = 1.3, 0.47
rows = [
    (lambda t: 2 * np.cos(w * t), 2.0, "A cos wt -> A"),
    (lambda t: 2 * np.sin(w * t), -2j, "A sin wt -> -jA"),
    (lambda t: -2 * np.cos(w * t), -2.0, "-A cos wt -> -A"),
    (lambda t: -2 * np.sin(w * t), 2j, "-A sin wt -> +jA"),
    (lambda t: 2 * np.cos(w * t + 0.8), 2 * np.exp(0.8j), "A cos(wt + th) -> A e^(j th)"),
    (lambda t: 2 * np.sin(w * t + 0.8), -2j * np.exp(0.8j), "A sin(wt + th) -> -jA e^(j th)"),
    (lambda t: 2 * np.cos(w * t - bz * zz), 2 * np.exp(-1j * bz * zz), "A cos(wt - beta z) -> A e^(-j beta z)"),
    (lambda t: 2 * np.sin(w * t + bz * zz), -2j * np.exp(1j * bz * zz), "A sin(wt + beta y) -> -jA e^(j beta y)"),
]
for f, ph, msg in rows:
    close(re_t(ph, w, t), f(t), "table row: " + msg)
close(-2j * np.exp(0.8j), 2 * np.exp(1j * (0.8 - np.pi / 2)), "-jA e^(j th) = A e^(j(th - pi/2))")
close(re_t(-1j, w, t), np.sin(w * t), "Re{-j e^(jwt)} = sin wt")
# back to the time domain: (4 - 3j) -> 5 cos(phi - 36.9 deg) = 4 cos + 3 sin
Pz = 4 - 3j
close(abs(Pz), 5.0, "|4 - 3j| = 5"); close(ang_deg(Pz), -36.87, "angle(4 - 3j) = -36.9 deg", rtol=1e-4)
phi = np.linspace(0, 2 * np.pi, 400)
close(np.real(Pz * np.exp(1j * phi)), 5 * np.cos(phi + np.angle(Pz)), "Re{(4-3j) e^(j phi)} = 5 cos(phi - 36.9 deg)")
close(np.real(Pz * np.exp(1j * phi)), 4 * np.cos(phi) + 3 * np.sin(phi), "= 4 cos phi + 3 sin phi")
ok(not np.allclose(np.real(Pz) * np.cos(phi), np.real(Pz * np.exp(1j * phi))), "Re{A} cos wt (the slip) differs: it loses the 3 sin part")
close(ang_deg(-4 + 3j), 143.13, "-4 + 3j is at 143.1 deg (its own quadrant)", rtol=1e-4)
close(np.degrees(np.arctan(3 / -4)), -36.87, "tan^-1(3/(-4)) = -36.9 deg (wrong quadrant)", rtol=1e-4)
# derivative, integral, delay rules (numerically)
Ph = 1.7 * np.exp(0.4j)
a = re_t(Ph, w, t)
close(np.gradient(a, t)[5:-5], re_t(1j * w * Ph, w, t)[5:-5], "d/dt -> j w", rtol=1e-3, atol=1e-3 * w)
close(re_t(Ph / (1j * w), w, t), 1.7 * np.sin(w * t + 0.4) / w, "integral -> 1/(j w) (zero-mean antiderivative)")
tau = 3.1e-3
close(re_t(Ph, w, t - tau), re_t(Ph * np.exp(-1j * w * tau), w, t), "delay tau -> e^(-j w tau)")
close(np.gradient(np.cos(w * t), t)[5:-5], -w * np.sin(w * t)[5:-5], "d/dt cos wt = -w sin wt", rtol=1e-3, atol=1e-3 * w)
close(re_t(1j * w, w, t), -w * np.sin(w * t), "Re{j w e^(jwt)} = -w sin wt")
# derivative of a cosine peaks a quarter period early
ad = re_t(1j * w * 1.0, w, t); a0 = re_t(1.0, w, t)
T50 = 2 * np.pi / w
tpk = lambda s, lo, tarr=None: (t if tarr is None else tarr)[lo:][np.argmax(s[lo:])]
ok(abs((tpk(a0, 50) - tpk(ad, 50)) % T50 - T50 / 4) < 2e-5, "d/dt(cos) peaks T/4 before cos")
# uniqueness: t = 0 gives Re parts, w t = pi/2 gives Im parts
Pa, Pb = 0.3 + 1.1j, 0.3 + 1.1j
ok(np.isclose(np.real(Pa), re_t(Pa, w, np.array([0.0]))[0]) and np.isclose(-np.imag(Pa), re_t(Pa, w, np.array([np.pi / 2 / w]))[0]),
   "uniqueness: a(0) = Re{A}, a(pi/(2w)) = -Im{A} determine A")
# linearity
Pc = -0.9 + 0.2j
close(re_t(Pa + Pc, w, t), re_t(Pa, w, t) + re_t(Pc, w, t), "phasor of a sum = sum of phasors")
# products have no phasor at w
prod = re_t(Pa, w, t) * re_t(Pc, w, t)
ok(not np.allclose(prod, re_t(Pa * Pc, w, t)), "Re{A B e^(jwt)} is NOT a(t) b(t)")
close(prod, 0.5 * np.real(Pa * np.conj(Pc)) + 0.5 * np.real(Pa * Pc * np.exp(2j * w * t)), "a b = 1/2 Re{A B*} + 1/2 Re{A B e^(j2wt)} (the 2w term)")
close(np.cos(w * t) ** 2, 0.5 + 0.5 * np.cos(2 * w * t), "cos^2 = 1/2 + 1/2 cos 2wt")

zt = 1.3 - 2.1j
close(np.real(zt), 0.5 * (zt + np.conj(zt)), "Re{z} = (z + z*)/2"); close(zt * np.conj(zt), abs(zt) ** 2, "z z* = |z|^2")
close((2 * np.exp(0.4j)) * (3 * np.exp(-1.1j)), 6 * np.exp(-0.7j), "products multiply lengths and add angles")
close(1 / 1j, -1j, "1/j = -j"); close(np.exp(1j * np.pi / 2), 1j, "e^(j pi/2) = j"); close(np.exp(1j * np.pi), -1, "e^(j pi) = -1", atol=1e-15)

print("=== F. rotations and the figures (screen frame X right, Y up, Z out of the screen)")
th = np.pi / 6
v = np.array([np.cos(th), np.sin(th), 0.0])
vj = 1j * np.exp(1j * th); vj = np.array([vj.real, vj.imag, 0.0])
vmj = -1j * np.exp(1j * th); vmj = np.array([vmj.real, vmj.imag, 0.0])
close(vj, cr(Z, v), "multiplying by j = turning by +90 deg (counterclockwise): z_hat x (Re, Im, 0)")
close(vmj, -cr(Z, v), "multiplying by -j = turning by -90 deg (clockwise)")
# rotating arrow: positions at t = kT/8 turn counterclockwise (cross product of successive position vectors > 0)
pos = [np.array([np.cos(th + k * np.pi / 4), np.sin(th + k * np.pi / 4), 0.0]) for k in range(9)]
ok(all(cr(pos[k], pos[k + 1])[2] > 0 for k in range(8)), "fig phas-rotating-arrow: A e^(j(wt+th)) turns counterclockwise as t grows")
# SVG drawing: screen point (cx + r cos a, cy - r sin a); Y up means screen y decreases for positive sin
cx, cy, R = 165, 200, 100
Xs = lambda a: (cx + R * np.cos(a), cy - R * np.sin(a))
ok(Xs(th)[1] < cy and Xs(th)[0] > cx, "fig: the phasor at 30 deg is drawn up and to the right of the centre")
ok(Xs(th - np.pi / 2)[1] > cy, "fig: -jA (at -60 deg) is drawn below the Re axis")
ok(Xs(th + np.pi / 2)[0] < cx and Xs(th + np.pi / 2)[1] < cy, "fig: jA (at 120 deg) is drawn up and to the left")
close(np.exp(1j * (th - np.pi / 2)), np.exp(1j * (th + 6 * np.pi / 4)), "fig: -jA coincides with position 6 (a quarter period earlier, mod 8)")
close(np.exp(1j * (th + np.pi / 2)), np.exp(1j * (th + 2 * np.pi / 4)), "fig: jA coincides with position 2 (a quarter period later)")
# shadow of -jA peaks T/4 after a(t)
T1 = 1.0; wq = 2 * np.pi; tq = np.linspace(0, 3, 30001)
s0 = np.cos(wq * tq + th); s1 = np.real(-1j * np.exp(1j * th) * np.exp(1j * wq * tq))
close(s1, np.sin(wq * tq + th), "fig: the -jA shadow is A sin(wt + th)")
d = (tpk(s1, 0, tq) - tpk(s0, 0, tq)) % T1
close(d, 0.25, "fig: the dashed (sine) curve peaks a quarter period later", rtol=1e-3)
close(np.cos(th), 0.866, "fig: a(0) = A cos 30 deg = 0.866", rtol=1e-3)
# direction-trap dials: e^(-j beta z) turns clockwise with z (cross z-component < 0), e^(+j beta z) counterclockwise
for sgn, name in ((-1, "e^(-j beta z)"), (+1, "e^(+j beta z)")):
    dv = [np.array([np.cos(sgn * 2 * np.pi * k / 8), np.sin(sgn * 2 * np.pi * k / 8), 0]) for k in range(9)]
    zc = [cr(dv[k], dv[k + 1])[2] for k in range(8)]
    ok(all(np.sign(zc) == sgn), f"fig phas-direction-trap: dials of {name} turn {'clockwise' if sgn < 0 else 'counterclockwise'} as z grows")
    zg = np.linspace(0.5, 1.5, 200001)
    crest0 = zg[np.argmax(np.cos(sgn * 2 * np.pi * zg))]
    crest1 = zg[np.argmax(np.cos(np.pi / 4 + sgn * 2 * np.pi * zg))]
    close(crest1 - crest0, -sgn / 8, f"fig: {name}: the crest near z = lambda moves {'+' if sgn < 0 else '-'}lambda/8 in T/8", rtol=1e-4)
# snapshot-record figure: record at z = lambda/4 delayed T/4; snapshot at T/8 shifted +lambda/8
tg = np.linspace(0.5, 1.5, 200001)
close((tg[np.argmax(np.cos(2 * np.pi * tg - np.pi / 2))] - tg[np.argmax(np.cos(2 * np.pi * tg))]), 0.25, "fig phas-snapshot-record: record at lambda/4 peaks T/4 later", rtol=1e-4)
close((tg[np.argmax(np.cos(np.pi / 4 - 2 * np.pi * tg))] - tg[np.argmax(np.cos(2 * np.pi * tg))]), 0.125, "fig: snapshot at T/8 is shifted +lambda/8", rtol=1e-4)
close(np.cos(np.pi / 4), 0.7071, "fig: dashed snapshot starts at cos(pi/4) at z = 0", rtol=1e-4)
# time-average figure: a = cos wt, b = 0.8 cos(wt - phi)
for phd, avg_page in ((0, 0.40), (60, 0.20), (90, 0.0)):
    ph = np.radians(phd)
    q = tavg(lambda t: np.cos(2 * np.pi * t) * 0.8 * np.cos(2 * np.pi * t - ph), 2 * np.pi)
    close(q, avg_page, f"fig phas-time-average: phi = {phd} deg: <ab> = {avg_page}", atol=1e-12)
    close(q, 0.5 * np.real(1.0 * np.conj(0.8 * np.exp(-1j * ph))), f"   = 1/2 Re{{A B*}} (phi = {phd} deg)", atol=1e-12)
tt2 = np.linspace(0, 2, 4001)
ok(np.all(np.cos(2 * np.pi * tt2) * 0.8 * np.cos(2 * np.pi * tt2) >= -1e-15), "fig: in phase, the product never goes negative")
ok(np.min(np.cos(2 * np.pi * tt2) * 0.8 * np.cos(2 * np.pi * tt2 - np.radians(60))) < 0, "fig: at 60 deg the product is negative for part of the period")

print("=== G. plane-wave phasors and the direction of travel")
v_, f_ = 2e8, 300e6; w_ = 2 * np.pi * f_; b_ = w_ / v_
for zv in (0.0, 0.31, 1.7):
    close(np.exp(-1j * w_ * zv / v_), np.exp(-1j * b_ * zv), f"delay z/v -> e^(-j beta z) at z = {zv}")
    close(re_t(3 * np.exp(-1j * b_ * zv), w_, t[:50] * 1e-6), 3 * np.cos(w_ * t[:50] * 1e-6 - b_ * zv), "Re{E0 e^(-j beta z) e^(jwt)} = E0 cos(wt - beta z)")
# crest positions: e^(-j b z) -> +z, e^(+j b z) -> -z
for sgn, dirn in ((-1, +1), (+1, -1)):
    crest = lambda tt: (-w_ * tt) / (sgn * b_)        # phase w t + sgn b z = 0
    ok(np.sign(crest(1e-10) - crest(0.0)) == dirn, f"e^({'+' if sgn > 0 else '-'}j beta z) travels toward {'+' if dirn > 0 else '-'}z")
# template e^{j(ax+by+cz)}: (a,b,c) = -beta u
for u in (np.array([0, 0, -1.0]), np.array([1, 1, 0]) / np.sqrt(2), np.array([0.6, 0, 0.8])):
    beta = 2.5; abc = -beta * u; r = np.array([0.3, -1.2, 0.7])
    close(np.exp(1j * abc @ r), np.exp(-1j * beta * u @ r), f"template (a,b,c) = -beta u for u = {np.round(u, 3)}")
    close(np.linalg.norm(abc), beta, "a^2 + b^2 + c^2 = beta^2")
b450 = 2 * np.pi * 450e6 * np.sqrt(4) / 3e8
close(b450, 6 * np.pi, "450 MHz, eps_r = 4: beta = 6 pi rad/m")
ok(np.allclose(-b450 * np.array([0, 0, -1.0]), [0, 0, 6 * np.pi]), "toward -z: (a, b, c) = (0, 0, +6 pi)")
ud = (X + Y) / np.sqrt(2)
close(-2 * np.pi * ud, [-np.sqrt(2) * np.pi, -np.sqrt(2) * np.pi, 0], "toward (x+y)/sqrt2 with beta = 2 pi: a = b = -sqrt2 pi")
close(-np.sqrt(2) * np.pi, -4.443, "-sqrt2 pi = -4.44 rad/m", rtol=1e-3)
close(2 * np.pi * ud @ np.array([1.0, 1.0, 0]), np.sqrt(2) * np.pi * 2, "beta u.r = sqrt2 pi (x + y) at x = y = 1")
ok(abs(ud @ Z) < 1e-15 and abs(ud @ (X - Y)) < 1e-15, "z_hat and (x_hat - y_hat) are perpendicular to (x_hat + y_hat)/sqrt2")

print("=== H. E <-> H: divide by eta and rotate; Example 1; Example 2; the 200 MHz example")
eta = 250.0
for trial in range(5):
    u = rng.normal(size=3); u /= np.linalg.norm(u)
    E0 = rng.normal(size=3) + 1j * rng.normal(size=3); E0 -= (E0 @ u) * u          # E0 perpendicular to u
    H0 = cr(u, E0) / eta
    close(eta * cr(H0, u), E0, f"trial {trial}: E = eta H x u recovers E (round trip)")
    S = cr(E0, np.conj(H0))
    close(S, np.vdot(E0, E0).real / eta * u, f"trial {trial}: E x H* = |E|^2/eta u (real, along u)")
    close(np.vdot(E0, E0).real, np.sum(np.abs(E0) ** 2), "|E|^2 = sum of |components|^2")
    close(np.linalg.norm(E0) / np.linalg.norm(H0), eta, "|E|/|H| = eta")
    # without the conjugate the product oscillates along u as e^{-2j beta s}: its real part is not constant
    beta = 3.0; s = np.linspace(0, 2, 7)
    noconj = np.array([np.real(cr(E0 * np.exp(-1j * beta * si), H0 * np.exp(-1j * beta * si))) for si in s])
    ok(np.ptp(noconj @ u) > 1e-6 * np.linalg.norm(S), f"trial {trial}: 1/2 Re{{E x H}} (no conjugate) varies along the travel")
# Faraday/Ampere in phasor form for E = x Ex(z), H = y Hy(z)
w = 2 * np.pi * 1e8; mu, eps = mu0, 4 * eps0; beta = w * np.sqrt(mu * eps); eta = np.sqrt(mu / eps)
close(beta / (w * mu), 1 / eta, "beta/(w mu) = 1/eta")
close(beta / eta, w * eps, "beta/eta = w eps (Ampere is satisfied too)")
for sgn in (+1, -1):        # e^{-+j beta z}: sgn = +1 is travel toward +z
    Ex = lambda z: 2.0 * np.exp(-sgn * 1j * beta * z); Hy = lambda z: sgn * Ex(z) / eta
    z0, h = 0.37, 1e-6
    dEx = (Ex(z0 + h) - Ex(z0 - h)) / (2 * h); dHy = (Hy(z0 + h) - Hy(z0 - h)) / (2 * h)
    close(dEx, -1j * w * mu * Hy(z0), f"travel {'+' if sgn > 0 else '-'}z: dEx/dz = -j w mu Hy with Hy = {'+' if sgn > 0 else '-'}Ex/eta", rtol=1e-6)
    close(-dHy, 1j * w * eps * Ex(z0), f"travel {'+' if sgn > 0 else '-'}z: -dHy/dz = j w eps Ex", rtol=1e-6)
# Example 1 (notes' table)
eta = 377.0; beta = 2.0; yv, zv = 0.41, -0.83
uE1 = -Y
E1 = np.exp(1j * beta * yv) * Z
H1 = cr(uE1, E1) / eta
close(H1, -np.exp(1j * beta * yv) / eta * X, "Ex.1 row 2: H = (1/eta)(-y) x z e^(j beta y) = -(e^(j beta y)/eta) x")
close(cr(Z, -X), -Y, "Ex.1 row 2 check: z x (-x) = -y (travel -y)")
close(np.real(cr(E1, np.conj(H1))), np.abs(E1 @ np.conj(E1)) / eta * uE1, "Ex.1: E x H* along -y")
tt_ = np.linspace(0, 1, 9)
close(re_t(np.exp(1j * beta * yv), 2 * np.pi, tt_), np.cos(2 * np.pi * tt_ + beta * yv), "Ex.1 row 1: cos(wt + beta y) <-> e^(j beta y)")
H3 = -1j * np.exp(-1j * beta * zv) * Y
close(re_t(H3[1], 2 * np.pi, tt_), np.sin(2 * np.pi * tt_ - beta * zv), "Ex.1 row 3: sin(wt - beta z) <-> -j e^(-j beta z)")
E3 = eta * cr(H3, Z)
close(E3, -1j * eta * np.exp(-1j * beta * zv) * X, "Ex.1 row 4: E = eta H x z = -j eta e^(-j beta z) x")
close(cr(Y, Z), X, "Ex.1 row 4: y x z = x")
close(re_t(E3[0], 2 * np.pi, tt_), eta * np.sin(2 * np.pi * tt_ - beta * zv), "Ex.1 row 4: E = eta sin(wt - beta z) x")
close(np.real(cr(E3, np.conj(H3))), eta * Z, "Ex.1 rows 3-4: E x H* = +eta z (travel +z)")
# Example 2
Hp, Hm = 0.7, 0.4
Ht = lambda z: Hp * np.exp(-1j * beta * z) * X - 1j * Hm * np.exp(1j * beta * z) * Y
Et = lambda z: -Y * eta * Hp * np.exp(-1j * beta * z) + 1j * X * eta * Hm * np.exp(1j * beta * z)
for zv in (0.0, 0.37, -1.1):
    wave_p = eta * cr(Hp * np.exp(-1j * beta * zv) * X, Z)                  # +z wave: E = eta H x z
    wave_m = eta * cr(-1j * Hm * np.exp(1j * beta * zv) * Y, -Z)            # -z wave: E = eta H x (-z)
    close(wave_p + wave_m, Et(zv), f"Ex.2: E = eta H x u per wave reproduces the notes' E phasor at z = {zv}")
close(cr(X, Z), -Y, "Ex.2: x x z = -y");  close(cr(Y, -Z), -X, "Ex.2: y x (-z) = -x")
wq = 2 * np.pi
Etime = lambda z, t: (-Y[:, None] * eta * Hp * np.cos(wq * t - beta * z) - X[:, None] * eta * Hm * np.sin(wq * t + beta * z))
Htime = lambda z, t: (X[:, None] * Hp * np.cos(wq * t - beta * z) + Y[:, None] * Hm * np.sin(wq * t + beta * z))
tt3 = np.linspace(0, 1, 13)
for zv in (0.0, 0.37):
    close(re_t(Et(zv), wq, tt3), Etime(zv, tt3), f"Ex.2: Re{{E e^(jwt)}} = -y eta H+ cos(wt - bz) - x eta H- sin(wt + bz) at z = {zv}")
    close(re_t(Ht(zv), wq, tt3), Htime(zv, tt3), f"Ex.2: H phasor <-> the given H(z,t) at z = {zv}")
# Example 2 satisfies Lecture 18's curl equations (1D): curl E = (-dEy/dz, dEx/dz, 0) = -mu dH/dt; curl H = (-dHy/dz, dHx/dz, 0) = eps dE/dt
mu_e, eps_e = 1.0, 1.0 / eta ** 2 * 1.0          # choose mu, eps with sqrt(mu/eps) = eta and w sqrt(mu eps) = beta
mu_e = beta * eta / wq; eps_e = beta / (eta * wq)
close(np.sqrt(mu_e / eps_e), eta, "Ex.2 FD setup: sqrt(mu/eps) = eta"); close(wq * np.sqrt(mu_e * eps_e), beta, "Ex.2 FD setup: w sqrt(mu eps) = beta")
z0, t0, hz, ht = 0.29, 0.13, 1e-5, 1e-6
dEdz = (Etime(z0 + hz, np.array([t0])) - Etime(z0 - hz, np.array([t0])))[:, 0] / (2 * hz)
dHdz = (Htime(z0 + hz, np.array([t0])) - Htime(z0 - hz, np.array([t0])))[:, 0] / (2 * hz)
dEdt = (Etime(z0, np.array([t0 + ht])) - Etime(z0, np.array([t0 - ht])))[:, 0] / (2 * ht)
dHdt = (Htime(z0, np.array([t0 + ht])) - Htime(z0, np.array([t0 - ht])))[:, 0] / (2 * ht)
curlE = np.array([-dEdz[1], dEdz[0], 0.0]); curlH = np.array([-dHdz[1], dHdz[0], 0.0])
close(curlE, -mu_e * dHdt, "Ex.2: Faraday holds for the notes' (E, H) (no sign error)", rtol=1e-6, atol=1e-6)
close(curlH, eps_e * dEdt, "Ex.2: Ampere-Maxwell holds for the notes' (E, H)", rtol=1e-6, atol=1e-8)
# the 200 MHz example: H = (1/eta) y x E
E200 = 12 * Z; H200 = cr(Y, E200) / (60 * np.pi)
close(H200, X / (5 * np.pi), "200 MHz example: H = (1/(5 pi)) x A/m")
close(1 / (5 * np.pi) * 1e3, 63.66, "1/(5 pi) = 63.7 mA/m", rtol=1e-4)
close(cr(Z, X), Y, "200 MHz example: z x x = +y")

print("=== I. the current sheet in phasor form (notes' Example 3) and the sine variant")
eta = 120 * np.pi; beta = 2 * np.pi / 3.0; w = beta * c
Js = 2.0 * X
def sheet(Js_ph, z):
    n = Z if z > 0 else -Z; d = abs(z)
    return -eta / 2 * Js_ph * np.exp(-1j * beta * d), 0.5 * cr(Js_ph, n) * np.exp(-1j * beta * d)
for zv in (0.8, -0.8, 1e-12, -1e-12):
    Eph, Hph = sheet(Js, zv); s = 1 if zv > 0 else -1
    close(Eph, -eta * np.exp(-s * 1j * beta * zv) * X, f"Ex.3: E = -eta e^(-+j beta z) x at z = {zv:g}")
    close(Hph, -s * np.exp(-s * 1j * beta * zv) * Y, f"Ex.3: H = -+ e^(-+j beta z) y at z = {zv:g}")
    close(np.real(cr(Eph, np.conj(Hph))), s * eta * Z, f"Ex.3: E x H* = {'+' if s > 0 else '-'}eta z (away from the sheet)")
close(0.5 * cr(Js, Z), -Y, "(1/2)(2x) x z = -y"); close(0.5 * cr(Js, -Z), Y, "(1/2)(2x) x (-z) = +y")
# time domain equals Lecture 19's Ex = -(eta/2) f(t -+ z/v), Hy = -+ (1/2) f(t -+ z/v) with f = 2 cos wt
tt4 = np.linspace(0, 2 * np.pi / w, 11)
for zv in (0.8, -0.8):
    Eph, Hph = sheet(Js, zv); s = 1 if zv > 0 else -1
    f_ = lambda tt: 2 * np.cos(w * tt)
    close(re_t(Eph, w, tt4)[0], -eta / 2 * f_(tt4 - abs(zv) / c), f"Ex.3: Re{{E}} = -(eta/2) f(t - |z|/c) at z = {zv}", rtol=1e-6, atol=1e-9)
    close(re_t(Hph, w, tt4)[1], -s * 0.5 * f_(tt4 - abs(zv) / c), f"Ex.3: Re{{H}} = -+(1/2) f(t - |z|/c) at z = {zv}", rtol=1e-6, atol=1e-9)
# boundary conditions at the sheet
Ea, Ha = sheet(Js, 1e-15); Eb, Hb = sheet(Js, -1e-15)
close(Ea, Eb, "Ex.3: tangential E continuous at z = 0")
close(cr(Z, Ha - Hb), Js, "Ex.3: z x (H+ - H-) = J_s")
# sine variant: J_s = 2 sin(wt) x -> J = -2j x; every phasor times -j
Jsin = -2j * X
close(re_t(Jsin, w, tt4), (2 * np.sin(w * tt4))[None, :] * X[:, None], "sine sheet: Re{-2j x e^(jwt)} = 2 sin wt x")
for zv in (0.8, -0.8):
    Eph, Hph = sheet(Jsin, zv); s = 1 if zv > 0 else -1
    close(Eph, 1j * eta * np.exp(-s * 1j * beta * zv) * X, f"sine sheet: E = j eta e^(-+j beta z) x at z = {zv}")
    close(Hph, s * 1j * np.exp(-s * 1j * beta * zv) * Y, f"sine sheet: H = +-j e^(-+j beta z) y at z = {zv}")
    close(re_t(Eph, w, tt4)[0], -eta * np.sin(w * tt4 - s * beta * zv), f"sine sheet: Ex = -eta sin(wt -+ beta z) at z = {zv}")
    close(re_t(Hph, w, tt4)[1], -s * np.sin(w * tt4 - s * beta * zv), f"sine sheet: Hy = -+ sin(wt -+ beta z) at z = {zv}")

print("=== J. time averages: <ab> = 1/2 Re{A B*}, <E x H>, <J.E>")
w = 2 * np.pi * 7.0
for trial in range(6):
    Aph = rng.normal() + 1j * rng.normal(); Bph = rng.normal() + 1j * rng.normal()
    q = tavg(lambda t: re_t(Aph, w, t) * re_t(Bph, w, t), w)
    close(q, 0.5 * np.real(Aph * np.conj(Bph)), f"trial {trial}: <ab> by quadrature = 1/2 Re{{A B*}}")
    close(q, 0.5 * abs(Aph) * abs(Bph) * np.cos(np.angle(Aph) - np.angle(Bph)), "   = 1/2 AB cos(th_a - th_b)")
    close(0.5 * np.real(Aph * np.conj(Bph)), 0.5 * np.real(np.conj(Aph) * Bph), "   Re{A B*} = Re{A* B}")
    ph = np.exp(1j * rng.uniform(0, 2 * np.pi))
    close(0.5 * np.real(Aph * ph * np.conj(Bph * ph)), 0.5 * np.real(Aph * np.conj(Bph)), "   a common phase cancels")
    close(tavg(lambda t: 0.5 * np.real(Aph * Bph * np.exp(2j * w * t)), w), 0.0, "   the 2w term averages to zero", atol=1e-12)
for Aph in (1.0, 2.0 * np.exp(0.3j)):
    close(tavg(lambda t: re_t(Aph, w, t) ** 2, w), 0.5 * abs(Aph) ** 2, f"<a^2> = 1/2 |A|^2 (|A| = {abs(Aph)})")
close(tavg(lambda t: np.cos(w * t) ** 2, w), 0.5, "<cos^2> = 1/2 (Lecture 20)")
close(tavg(lambda t: 2 * np.cos(w * t) * 3 * np.cos(w * t + np.pi / 2), w), 0.0, "quadrature: <ab> = 0", atol=1e-12)
close(tavg(lambda t: 2 * np.cos(w * t) * 3 * np.cos(w * t + np.pi), w), -3.0, "antiphase: <ab> = -1/2 AB")
close(tavg(lambda t: 3 * np.cos(w * t + np.radians(20)) * 2 * np.cos(w * t - np.radians(40)), w), 1.5, "example: 3cos(wt+20) 2cos(wt-40) -> 1.5")
# vector versions
for trial in range(4):
    E = rng.normal(size=3) + 1j * rng.normal(size=3); H = rng.normal(size=3) + 1j * rng.normal(size=3)
    q = tavg(lambda t: cr(re_t(E, w, t).T, re_t(H, w, t).T).T, w)
    close(q, 0.5 * np.real(cr(E, np.conj(H))), f"trial {trial}: <E x H> by quadrature = 1/2 Re{{E x H*}}")
    q2 = tavg(lambda t: np.sum(re_t(E, w, t) * re_t(H, w, t), axis=0), w)
    close(q2, 0.5 * np.real(E @ np.conj(H)), f"trial {trial}: <J . E> by quadrature = 1/2 Re{{J . E*}}")
# single wave in a lossless medium
eta = 60 * np.pi; E0 = 12 * Z; u = Y; H0 = cr(u, E0) / eta
close(0.5 * np.real(cr(E0, np.conj(H0))), 144 / (2 * eta) * Y, "200 MHz wave: <S> = 144/(120 pi) y")
close(144 / (120 * np.pi), 0.382, "= 0.382 W/m^2", rtol=1e-3)
close(144 / (2 * eta), 6 / (5 * np.pi), "= 6/(5 pi)")
# the notes' sheet: two routes (Lecture 20 by cos^2, Lecture 21 by phasors)
eta = 120 * np.pi; beta = 2 * np.pi / 3.0; w = beta * c
for zv, s in ((0.6, +1), (-0.6, -1)):
    Eph, Hph = sheet(2.0 * X, zv)
    ph_route = 0.5 * np.real(cr(Eph, np.conj(Hph)))
    td_route = tavg(lambda t: cr(re_t(Eph, w, t).T, re_t(Hph, w, t).T).T, w)
    close(ph_route, s * eta / 2 * Z, f"sheet: <S> = {'+' if s > 0 else '-'}(eta/2) z by phasors at z = {zv}")
    close(td_route, ph_route, "   = the time-domain average of +-eta cos^2(wt -+ beta z) z (Lecture 20)", atol=1e-9)
    close(tavg(lambda t: s * eta * np.cos(w * t - s * beta * zv) ** 2, w), s * eta / 2, "   +-eta <cos^2> = +-eta/2", atol=1e-9)
close(eta / 2, 60 * np.pi, "eta/2 = 60 pi"); close(60 * np.pi, 188.5, "60 pi = 188 W/m^2", rtol=1e-3)
E0s, _ = sheet(2.0 * X, 1e-15)
close(0.5 * np.real(-(2.0 * X) @ np.conj(E0s)), eta, "sheet: <-J_s . E(0,t)> = 1/2 Re{-J . E*(0)} = eta = 120 pi")
close(tavg(lambda t: 2 * eta * np.cos(w * t) ** 2, w), eta, "   = <2 eta cos^2 wt> (Lecture 20)", atol=1e-9)
close(eta, 377.0, "120 pi = 377 W/m^2", rtol=1e-3)
close(eta, eta / 2 + eta / 2, "energy balance: eta = eta/2 + eta/2")
Es, Hs = sheet(-2j * X, 0.6)
close(0.5 * np.real(cr(Es, np.conj(Hs))), eta / 2 * Z, "sine sheet: same <S> (the -j cancels against its conjugate)")
Es0, _ = sheet(-2j * X, 1e-15)
close(0.5 * np.real(-(-2j * X) @ np.conj(Es0)), eta, "sine sheet: same <-J.E> = eta")
# Example 2 power: <S> = (eta/2)(H+^2 - H-^2) z
eta = 377.0; beta = 2.0; Hp, Hm = 0.7, 0.4; wq = 2 * np.pi
for zv in (0.0, 0.41, -1.3):
    Ep = -Y * eta * Hp * np.exp(-1j * beta * zv) + 1j * X * eta * Hm * np.exp(1j * beta * zv)
    Hpz = Hp * np.exp(-1j * beta * zv) * X - 1j * Hm * np.exp(1j * beta * zv) * Y
    close(cr(Ep, np.conj(Hpz)), eta * (Hp ** 2 - Hm ** 2) * Z, f"Ex.2 power: E x H* = eta (H+^2 - H-^2) z at z = {zv}")
    close(tavg(lambda t: cr(re_t(Ep, wq, t).T, re_t(Hpz, wq, t).T).T, wq), eta / 2 * (Hp ** 2 - Hm ** 2) * Z, "   time-domain average agrees", atol=1e-9)
close(-eta * Hp ** 2 * cr(Y, X), eta * Hp ** 2 * Z, "Ex.2: -eta H+^2 (y x x) = +eta H+^2 z")
close(1j * 1j * eta * Hm ** 2 * cr(X, Y), -eta * Hm ** 2 * Z, "Ex.2: j*j eta H-^2 (x x y) = -eta H-^2 z")
# parallel polarizations: cross terms in S~ are purely imaginary
for trial in range(3):
    Aa = rng.normal() + 1j * rng.normal(); Bb = rng.normal() + 1j * rng.normal(); beta = 1.7
    for zv in (0.0, 0.33, 1.9):
        Ex_ = Aa * np.exp(-1j * beta * zv) + Bb * np.exp(1j * beta * zv)
        Hy_ = (Aa * np.exp(-1j * beta * zv) - Bb * np.exp(1j * beta * zv)) / eta
        Sz = Ex_ * np.conj(Hy_)
        close(np.real(Sz), (abs(Aa) ** 2 - abs(Bb) ** 2) / eta, f"parallel polarizations: Re{{S~}} = (|A|^2 - |B|^2)/eta (trial {trial}, z = {zv})")
# without the conjugate: 1/2 Re{E x H} varies as cos(2 beta z) for one wave
eta = 377.0; beta = 2.0
zs = np.linspace(0, np.pi / beta, 5)
nc = [0.5 * np.real(np.exp(-1j * beta * z) * np.exp(-1j * beta * z) / eta) for z in zs]
close(nc, 0.5 / eta * np.cos(2 * beta * zs), "1/2 Re{E x H} (no conjugate) = cos(2 beta z)/(2 eta) for E = e^(-j beta z): not the average")
# instantaneous S of one linearly polarized wave: between 0 and 2 <S>
wq = 2 * np.pi; tt5 = np.linspace(0, 1, 100001)
Sinst = np.cos(wq * tt5) ** 2 / eta
close([Sinst.min(), Sinst.max()], [0.0, 2 * (0.5 / eta)], "one wave: instantaneous S swings between 0 and 2 <S>", atol=1e-12)
# Joule heating with a complex sigma; the collisionless plasma absorbs nothing
for sig in (5.0, 2.0 - 3.0j, -4.0j):
    Eph = np.array([1.3 + 0.2j, -0.4j, 0.7])
    q = tavg(lambda t: np.sum(re_t(sig * Eph, w, t) * re_t(Eph, w, t), axis=0), w)
    close(q, 0.5 * np.real(sig) * np.sum(abs(Eph) ** 2), f"<J.E> = 1/2 Re{{sigma}} |E|^2 for sigma = {sig}", atol=1e-12)
sDC, nu = 6e7, 4e13
for f in (1e9, 1e13, 1e14):
    wq = 2 * np.pi * f; s_ = sDC / (1 + 1j * wq / nu)
    close(np.real(s_), sDC / (1 + wq ** 2 / nu ** 2), f"Drude: Re{{sigma}} = sigma_DC/(1 + w^2/nu^2) at {f:g} Hz")

print("=== K. worked problem: H = 0.3 cos(wt + 2 pi z) x - 0.4 sin(wt + 2 pi z - pi/4) y, non-magnetic")
w = 2 * np.pi * 1e8; beta = 2 * np.pi; cc = 3e8
close(w / (2 * np.pi), 1e8, "(a) f = 100 MHz"); close(2 * np.pi / w, 1e-8, "(a) T = 10 ns")
close(2 * np.pi / beta, 1.0, "(a) lambda = 1 m"); close(w / beta, 1e8, "(a) v_p = 1e8 m/s = c/3")
close((cc / (w / beta)) ** 2, 9.0, "(a) eps_r = 9"); eta = 120 * np.pi / 3
close(eta, 40 * np.pi, "(a) eta = 40 pi"); close(40 * np.pi, 125.66, "(a) 40 pi = 125.7 ohm", rtol=1e-4)
crest = lambda tt: -(w * tt) / beta
ok(crest(1e-9) < crest(0), "(a) same signs of t and z terms: travel toward -z")
u = -Z
Hph = np.array([0.3, 0.4 * np.exp(1j * np.pi / 4), 0])           # times e^{j 2 pi z}
Hgiven = lambda z, t: np.array([0.3 * np.cos(w * t + 2 * np.pi * z), -0.4 * np.sin(w * t + 2 * np.pi * z - np.pi / 4), 0 * t])
tt6 = np.linspace(0, 2e-8, 41)
for zv in (0.0, 0.37, -2.2):
    close(re_t(Hph * np.exp(1j * 2 * np.pi * zv), w, tt6), Hgiven(zv, tt6), f"(b) H phasor reproduces H(z,t) at z = {zv}")
close(-0.4 * (-1j) * np.exp(-1j * np.pi / 4), 0.4 * np.exp(1j * np.pi / 4), "(b) -0.4 (-j) e^(-j pi/4) = 0.4 e^(j pi/4)")
close(1j * np.exp(-1j * np.pi / 4), np.exp(1j * np.pi / 4), "(b) j e^(-j pi/4) = e^(j pi/4)")
close(+0.4 * (-1j) * np.exp(-1j * np.pi / 4), 0.4 * np.exp(-3j * np.pi / 4), "(b) trap: dropping the minus gives 0.4 e^(-j3pi/4)")
close(-0.4 * np.exp(-1j * np.pi / 4), 0.4 * np.exp(3j * np.pi / 4), "(b) trap: forgetting the -j gives 0.4 e^(+j3pi/4)")
close(+0.4 * np.exp(-1j * np.pi / 4), 0.4 * np.exp(-1j * np.pi / 4), "(b) trap: forgetting both gives 0.4 e^(-j pi/4)")
for wrong, off in ((np.exp(-3j * np.pi / 4), 180), (np.exp(3j * np.pi / 4), 90), (np.exp(-1j * np.pi / 4), 90)):
    close(abs(np.degrees(np.angle(np.exp(1j * np.pi / 4) / wrong))), off, f"(b) trap: that answer is {off} deg off")
close(-0.4 * np.sin(-np.pi / 4), 0.4 * np.cos(np.pi / 4), "(b) spot check: H_y(0,0) = 0.283 = Re{0.4 e^(j pi/4)}")
close(0.4 * np.cos(np.pi / 4), 0.283, "(b) 0.4 cos 45 = 0.283", rtol=1e-3)
ph_ = np.linspace(0, 2 * np.pi, 50)
close(-0.4 * np.sin(ph_ - np.pi / 4), 0.4 * np.cos(ph_ + np.pi / 4), "(b) -0.4 sin(phi - pi/4) = 0.4 cos(phi + pi/4): y leads x by 45 deg")
close(cr(X, -Z), Y, "(c) x x (-z) = +y"); close(cr(Y, -Z), -X, "(c) y x (-z) = -x")
Eph = eta * cr(Hph, u)
close(Eph, np.array([-16 * np.pi * np.exp(1j * np.pi / 4), 12 * np.pi, 0]), "(c) E = (-16 pi e^(j pi/4) x + 12 pi y) e^(j2 pi z)")
close([16 * np.pi, 12 * np.pi], [50.27, 37.70], "(c) 16 pi = 50.3, 12 pi = 37.7 V/m", rtol=1e-3)
S_ = cr(Eph, np.conj(Hph))
close(S_, -10 * np.pi * Z, "(c) E x H* = -10 pi z (along -z)")
close(eta * cr(0.3 * Y, 0.3 * X) - eta * cr(0.4 * X, 0.4 * Y), -10 * np.pi * Z, "(c) 40 pi [0.09 y x x - 0.16 x x y] = -10 pi z")
close(np.linalg.norm(Eph), 20 * np.pi, "(c) |E| = 20 pi"); close(np.linalg.norm(Hph), 0.5, "(c) |H| = 0.5")
close(np.linalg.norm(Eph) / np.linalg.norm(Hph), eta, "(c) |E|/|H| = eta")
Etime = lambda z, t: np.array([-16 * np.pi * np.cos(w * t + 2 * np.pi * z + np.pi / 4), 12 * np.pi * np.cos(w * t + 2 * np.pi * z), 0 * t])
for zv in (0.0, 0.37):
    close(re_t(Eph * np.exp(1j * 2 * np.pi * zv), w, tt6), Etime(zv, tt6), f"(d) E(z,t) at z = {zv}")
    close(eta * cr(Hgiven(zv, tt6).T, u).T, Etime(zv, tt6), f"(d) time-domain cross-check eta H x (-z) at z = {zv}")
# Maxwell check of the (E, H) pair with mu0, eps = 9 eps0 (finite differences)
mu, eps = mu0, 9 * eps0
close(w * np.sqrt(mu * eps), beta, "(check) w sqrt(mu0 9 eps0) = 2 pi rad/m with exact c", rtol=1e-3)
close(np.sqrt(mu / eps), eta, "(check) sqrt(mu0/(9 eps0)) = 40 pi (120 pi approximation)", rtol=1e-3)
# exact Maxwell check with the medium the page's rounded constants describe: mu = eta beta / w, eps = beta / (eta w)
mu_k, eps_k = eta * beta / w, beta / (eta * w)
close(1 / np.sqrt(mu_k * eps_k), 1e8, "(check) the pair's medium: v = 1e8 m/s"); close(np.sqrt(mu_k / eps_k), eta, "(check) the pair's medium: eta = 40 pi")
z0, t0, hz, ht = 0.23, 3.1e-9, 1e-6, 1e-14
Ef = lambda z, t: Etime(z, np.array([t]))[:, 0]; Hf = lambda z, t: Hgiven(z, np.array([t]))[:, 0]
dEdz = (Ef(z0 + hz, t0) - Ef(z0 - hz, t0)) / (2 * hz); dHdz = (Hf(z0 + hz, t0) - Hf(z0 - hz, t0)) / (2 * hz)
dEdt = (Ef(z0, t0 + ht) - Ef(z0, t0 - ht)) / (2 * ht); dHdt = (Hf(z0, t0 + ht) - Hf(z0, t0 - ht)) / (2 * ht)
close(np.array([-dEdz[1], dEdz[0], 0.0]), -mu_k * dHdt, "(check) Faraday: curl E = -mu dH/dt for the worked problem's (E, H)", rtol=1e-5, atol=1e-6)
close(np.array([-dHdz[1], dHdz[0], 0.0]), eps_k * dEdt, "(check) Ampere-Maxwell: curl H = eps dE/dt for the worked problem's (E, H)", rtol=1e-5, atol=1e-8)
avg = 0.5 * np.real(S_)
close(avg, -5 * np.pi * Z, "(e) <S> = -5 pi z"); close(5 * np.pi, 15.71, "(e) 5 pi = 15.7 W/m^2", rtol=1e-3)
close(0.5 * eta * 0.3 ** 2, 1.8 * np.pi, "(e) x term alone: 1.8 pi"); close(1.8 * np.pi, 5.655, "(e) 1.8 pi = 5.65 W/m^2", rtol=1e-3)
close(0.5 * eta * 0.4 ** 2, 3.2 * np.pi, "(e) y term alone: 3.2 pi"); close(3.2 * np.pi, 10.05, "(e) 3.2 pi = 10.05 W/m^2", rtol=1e-3)
close(1.8 * np.pi + 3.2 * np.pi, 5 * np.pi, "(e) the component powers add")
qavg = tavg(lambda t: cr(Etime(0.37, t).T, Hgiven(0.37, t).T).T, w)
close(qavg, -5 * np.pi * Z, "(e) time-domain average of E x H = -5 pi z (Lecture 20 route)", atol=1e-9)
close(tavg(lambda t: np.sum(Hgiven(0.2, t) ** 2, axis=0), w), 0.125, "(e) <|H|^2> = 0.125")
for zv, tv in ((0.3, 1.7e-9), (-1.1, 4.4e-9)):
    Hn = Hgiven(zv, np.array([tv]))[:, 0]; En = Etime(zv, np.array([tv]))[:, 0]
    close(cr(En, Hn), -eta * (Hn @ Hn) * Z, f"(e) instantaneous S = -eta |H|^2 z at (z, t) = ({zv}, {tv:g})")
close((0.3 + 0.4) ** 2, 0.49, "(e) trap: (0.3 + 0.4)^2 = 0.49 (wrong)"); close(0.3 ** 2 + 0.4 ** 2, 0.25, "(e) 0.3^2 + 0.4^2 = 0.25")
close(eta * 0.25, 10 * np.pi, "(e) trap: eta |H|^2 = 10 pi is |S~|, not <S>")
close(5 * np.pi * 0.25, 1.25 * np.pi, "(f) window: 5 pi x 0.25 m^2 = 1.25 pi"); close(1.25 * np.pi, 3.93, "(f) = 3.93 W", rtol=1e-3)
H00 = Hgiven(0.0, np.array([0.0]))[:, 0]; E00 = Etime(0.0, np.array([0.0]))[:, 0]
close(H00, [0.3, 0.283, 0], "(f) H(0,0) = 0.300 x + 0.283 y", rtol=1e-3)
close(E00, [-35.54, 37.70, 0], "(f) E(0,0) = -35.5 x + 37.7 y", rtol=1e-3)
S00 = cr(E00, H00)
close(S00, [0, 0, -21.36], "(f) S(0,0) = -21.4 z W/m^2", rtol=1e-3)
close([E00[0] * H00[1], -E00[1] * H00[0]], [-10.05, -11.31], "(f) the two pieces -10.05 and -11.31", rtol=1e-3)
tt7 = np.linspace(0, 1e-8, 200001)
Sz = np.array([cr(e, h)[2] for e, h in zip(Etime(0.0, tt7[::50]).T, Hgiven(0.0, tt7[::50]).T)])
Hsq = np.sum(Hgiven(0.0, tt7) ** 2, axis=0)
close([eta * Hsq.min(), eta * Hsq.max()], [4.17, 27.24], "(f) instantaneous |S| between 4.2 and 27.2 W/m^2", rtol=2e-3)
ok(np.all(Sz < 0), "(f) S never reverses (always toward -z)")
ok(Hsq.min() > 0, "(f) |H|^2 never reaches zero (components not in phase)")
# variant: mu_r = 4, eps_r = 2.25
close(4 * 2.25, 9.0, "variant: mu_r eps_r = 9, same v_p and beta")
etav = 120 * np.pi * np.sqrt(4 / 2.25)
close(etav, 160 * np.pi, "variant: eta = 160 pi"); close(160 * np.pi, 502.65, "variant: 160 pi = 503 ohm", rtol=1e-4)
close(0.5 * etav * 0.25, 20 * np.pi, "variant: <S> = 20 pi"); close(20 * np.pi, 62.83, "variant: 20 pi = 62.8 W/m^2", rtol=1e-4)
close(etav / eta, 4.0, "variant: eta four times larger")

print("=== L. concept pages")
w = 2 * np.pi * 3.0; tt8 = np.linspace(0, 1, 301)
close(re_t(3 * np.exp(-1j * np.radians(120)), w, tt8), 3 * np.sin(w * tt8 - np.radians(30)), "phasors: 3 sin(wt - 30) <-> 3 e^(-j120)")
close(3 * np.exp(-1j * np.radians(120)), -1.5 - 2.598j, "phasors: 3 e^(-j120) = -1.5 - 2.60j", rtol=1e-4)
close(6 - 6j, 6 * np.sqrt(2) * np.exp(-1j * np.pi / 4), "phasors: 6 - 6j = 6 sqrt2 e^(-j45)")
close(6 * np.sqrt(2), 8.485, "phasors: 6 sqrt2 = 8.49", rtol=1e-4)
close(6 * np.cos(w * tt8) + 6 * np.sin(w * tt8), 6 * np.sqrt(2) * np.cos(w * tt8 - np.pi / 4), "phasors: 6 cos + 6 sin = 8.49 cos(wt - 45)")
close(2 * np.pi * 200e6 * np.sqrt(4) / 3e8, 8 * np.pi / 3, "dispersion: 200 MHz in eps_r = 4: beta = 8 pi/3")
close((3e8 / 1.5e8) ** 2, 4.0, "dispersion: mu_r eps_r = (c/v_p)^2 = 4")
close(1 / (5 * np.pi), (12 / (60 * np.pi)), "plane-waves: H amplitude 12/(60 pi) = 1/(5 pi) A/m")

print("=== M. Lecture 20 cross-check: the notes' sheet numbers")
close(120 * np.pi / 2, 60 * np.pi, "<E x H> = +-(eta/2) z = +-60 pi z W/m^2 (L20 and L21)")
close(2 * 120 * np.pi * 0.5, 120 * np.pi, "<-J_s . E> = 2 eta <cos^2> = eta = 120 pi W/m^2")

print(f"\nALL {ok_count} CHECKS PASSED")
