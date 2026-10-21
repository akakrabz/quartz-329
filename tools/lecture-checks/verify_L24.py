#!/usr/bin/env python3
"""Verification of every number, sign and direction on the Lecture 24 pages of the ECE 329 study site.

Pages checked:
  content-src/3-maxwell-and-waves/24-signal-transmission-and-circular-polarization.md   (sections A-H)
  content-src/concepts/group-velocity.md, concepts/wave-polarization.md                (sections B, D, E, H)
  content-src/problems/two-sheets-a-quarter-wave-apart.md                              (section I)
  figs_l24.py: screen frame, arrow senses, AM-pulse markers                             (section J)
  notes slips (ERRATA-L24.md)                                                           (section K)
numpy only. Handedness is fixed numerically: the field vector at a fixed point is sampled over one period and
the sign of u_hat . <E x dE/dt> decides (positive = rotation about the travel direction = right-handed, the
notes' rule "right thumb along travel, fingers curl with the rotation"). Group delay: an AM pulse is propagated
through the exact plasma dispersion relation by FFT and its envelope peak is timed.
"""
import sys
import numpy as np

sys.path.insert(0, "/home/claude/work")
import figs_l24 as F                      # noqa: E402  (figure module: pol_kind, am_field, constants)

mu0 = 4e-7 * np.pi
eps0 = 8.8541878128e-12
c = 1 / np.sqrt(mu0 * eps0)
eta0 = np.sqrt(mu0 / eps0)
X, Y, Z = np.eye(3)
cr = np.cross
ok_count = 0


def ok(cond, msg):
    global ok_count
    assert cond, "FAILED: " + msg
    ok_count += 1
    print("ok  ", msg)


def close(a, b, msg, rtol=1e-6, atol=1e-9):
    a_, b_ = np.asarray(a), np.asarray(b)
    good = np.allclose(a_, b_, rtol=rtol, atol=atol)
    if a_.size > 12:
        ok(good, f"{msg}: max |diff| = {np.max(np.abs(a_ - b_)):.2e} over {a_.size} values")
    else:
        ok(good, f"{msg}: {np.round(a_, 6).tolist()} vs {np.round(b_, 6).tolist()}")


def near(a, b, msg, rel=0.01):
    """page value b (rounded) against computed a"""
    ok(abs(a - b) <= rel * abs(b), f"{msg}: computed {a:.6g}, page {b:.6g} (tol {rel:.1%})")


PH = np.linspace(0, 2 * np.pi, 2000, endpoint=False)          # omega t over one period


def record(Ep, phase0=0.0):
    """E(t) = Re{Ep e^{j(wt + phase0)}} at a point, sampled over a period; returns (N, 3)"""
    return np.real(np.outer(np.exp(1j * (PH + phase0)), Ep))


def spin(Ep):
    """<E x dE/dt> / omega over a period (numerical)"""
    E = record(Ep)
    dE = np.real(np.outer(1j * np.exp(1j * PH), Ep))
    return cr(E, dE).mean(axis=0)


def hand(Ep, u):
    s = float(np.dot(u, spin(Ep)))
    if abs(s) < 1e-9 * max(1.0, np.vdot(Ep, Ep).real):
        return "linear"
    return "right" if s > 0 else "left"


def recipe(Ep, u):
    """the page's recipe: sign of u . [E(0) x E(T/4)], E(0) = Re Ep, E(T/4) = -Im Ep"""
    s = float(np.dot(u, cr(Ep.real, -Ep.imag)))
    if abs(s) < 1e-12 * max(1.0, np.vdot(Ep, Ep).real):
        return "linear"
    return "right" if s > 0 else "left"


def axes(Ep):
    """semi-major and semi-minor axis lengths of the traced ellipse: <E E^T> = (1/2) Re{Ep Ep^H}
    has eigenvalues (semi-axis)^2 / 2 (checked against sampled max/min |E| below)"""
    M = 0.5 * np.real(np.outer(Ep, np.conj(Ep)))
    ev = np.sort(np.clip(np.linalg.eigvalsh(M), 0, None))[::-1]
    return np.sqrt(2 * ev[0]), np.sqrt(2 * ev[1])


print("A. Narrowband AM in a non-dispersive medium (notes p. 1-2)")
v = 1.0
dt, n = 0.05, 2 ** 14
t = (np.arange(n) - n // 2) * dt
w0 = 3.0
m = lambda tt: 2 + np.cos(0.15 * tt) * np.exp(-tt ** 2 / 400)          # slow message, positive
f0 = m(t) * np.cos(w0 * t)
Fw = np.fft.fft(f0)
w = 2 * np.pi * np.fft.fftfreq(n, dt)
for L in (5.0, 17.3):
    fL = np.real(np.fft.ifft(Fw * np.exp(-1j * (w / v) * L)))          # beta = w/v for every frequency
    close(fL[2000:-2000], (m(t - L / v) * np.cos(w0 * (t - L / v)))[2000:-2000],
          f"non-dispersive: record at z = {L} is m(t - z/v) cos(w t - beta z), undistorted", atol=1e-6)
close(cr(X, Y), Z, "Field 1: E along x, H along y, E x H along +z (travel)")
tt = np.linspace(0, 1, 7)
close(np.sin(2 * np.pi * tt), np.cos(2 * np.pi * (tt - 0.25)), "Field 3: sin(wt) = cos(w(t - T/4)): carrier a quarter period late")

print("B. Group velocity (notes p. 2 footnote; page section 2; concept page)")
b0, vp, vg = F.am_numbers()                                              # plasma, omega = 2 omega_p, c = 1
near(vg, 0.87, "figure title v_g = 0.87c at omega = 2 omega_p", rel=0.005)
near(vg, 0.866, "concept page v_g = 0.866c", rel=0.001)
near(vp, 1.15, "figure title v_p = 1.15c", rel=0.005)
near(vp, 1.155, "concept page v_p = 1.155c", rel=0.001)
close(vp * vg, 1.0, "plasma: v_p v_g = c^2")
h = 1e-6
dwdb = 2 * h / (F.beta_plasma(F.W0 + h) - F.beta_plasma(F.W0 - h))
close(dwdb, vg, "v_g = d omega/d beta numerically (central difference) = c^2 beta/omega", rtol=1e-6)
# exact FFT propagation of a Gaussian AM pulse: time the envelope peak at several distances.
# The first-order (v_g) delay is exact for an infinitely narrow band; the next correction for a Gaussian of rms
# width 1/sigma in omega is (1/2) beta3 z / sigma^2 (beta3 = third derivative), which shrinks as the band narrows.
b3 = 3 * F.W0 / b0 ** 5                                                   # d3beta/domega3 for the plasma (c = omega_p = 1)


def spectrum(sig, n=2 ** 16, dt=0.05):
    t = (np.arange(n) - n // 2) * dt
    s_ = np.exp(-t ** 2 / (2 * sig ** 2)) * np.exp(1j * F.W0 * t)
    S_ = np.fft.fft(np.fft.ifftshift(s_)) * dt
    w_ = 2 * np.pi * np.fft.fftfreq(n, dt)
    keep = (w_ > 0) & (np.abs(S_) > 1e-12 * np.abs(S_).max())
    return w_[keep], S_[keep], 2 * np.pi / (n * dt)


for sig in (F.SIG, 24.0):
    wS, S, dw = spectrum(sig)
    for L in (10.0, 30.0, 60.0):
        tt = np.linspace(L / vg - 3 * sig, L / vg + 3 * sig, 3001)
        a = (S[None, :] * np.exp(1j * (np.outer(tt, wS) - F.beta_plasma(wS)[None, :] * L))).sum(axis=1) * dw / (2 * np.pi)
        env = np.abs(a)
        i = np.argmax(env)
        p = np.polyfit(tt[i - 3:i + 4], env[i - 3:i + 4], 2)
        tpk = -p[1] / (2 * p[0])
        corr = 0.5 * b3 * L / sig ** 2
        near(tpk, L / vg + corr, f"sigma = {sig:g}, z = {L}: envelope peak at z/v_g + beta3 z/(2 sigma^2) = {L / vg:.4f} + {corr:.4f}", rel=1e-3)
        tol = 0.006 if sig < 10 else 0.0004
        ok(abs(tpk - L / vg) / (L / vg) < tol,
           f"sigma = {sig:g}, z = {L}: envelope delay within {100 * tol:.2f} % of z/v_g (narrower band, closer)")
        ok(abs(tpk - L / vp) > 1.0, f"sigma = {sig:g}, z = {L}: envelope delay {tpk:.2f} is not the phase delay z/v_p = {L / vp:.2f}")
        ph = np.angle(a[i]) - (F.W0 * tt[i] - b0 * L)
        gouy = -0.5 * np.arctan(-1 / b0 ** 3 * L / sig ** 2)            # second-order (spreading) phase of a Gaussian
        ok(abs(np.angle(np.exp(1j * (ph - gouy)))) < 0.01 and abs(gouy) < 0.2,
           f"sigma = {sig:g}, z = {L}: carrier phase at the peak is omega0 t - beta0 z (crests at v_p), up to the small spreading phase {gouy:.3f} rad")
# envelope spreading negligible over the figure range: 1/2 |beta''| Omega^2 z with Omega ~ 1/sigma
bpp = -1 / b0 ** 3                                                        # d2beta/domega2 for the plasma (c = omega_p = 1)
h2 = 1e-4
close((F.beta_plasma(F.W0 + h2) - 2 * b0 + F.beta_plasma(F.W0 - h2)) / h2 ** 2, bpp, "plasma beta'' = -1/beta^3 (units c = omega_p = 1)", rtol=1e-4)
ok(0.5 * abs(bpp) * (1 / F.SIG) ** 2 * 54 < 0.2, "figure: second-order (spreading) phase over z = 54 is small (< 0.2 rad)")
# first-order Taylor statement: beta(w0 + W) ~ beta0 + W/v_g, error second order
for Wd in (0.05, 0.1):
    err = F.beta_plasma(F.W0 + Wd) - (b0 + Wd / vg)
    close(err, 0.5 * bpp * Wd ** 2 + b3 * Wd ** 3 / 6, f"Taylor: residual at Omega = {Wd} is (1/2) beta'' Omega^2 (+ beta3 Omega^3/6)", rtol=0.02, atol=1e-12)
    ok(abs(err) < 0.01 * abs(Wd / vg), f"Taylor: at Omega = {Wd} the first-order term carries > 99 % of beta - beta0")
# non-dispersive rows: v_g = v_p
mu_r, eps_r = 1.0, 4.0
bet = lambda ww: ww * np.sqrt(mu_r * mu0 * eps_r * eps0)
ww = 2 * np.pi * 2e8
close(2 * (ww * 1e-6) / (bet(ww * (1 + 1e-6)) - bet(ww * (1 - 1e-6))), ww / bet(ww), "dielectric: v_g = v_p = 1/sqrt(mu eps)")
kB, mAr, T = 1.380649e-23, 39.948 * 1.66053906660e-27, 300.0
bs = lambda ww: ww * np.sqrt(mAr / (5 / 3 * kB * T))
close(2 * (ww * 1e-6) / (bs(ww * (1 + 1e-6)) - bs(ww * (1 - 1e-6))), np.sqrt(5 * kB * T / (3 * mAr)), "sound, monatomic gas: v_g = v_p = sqrt(5kT/3m)")
# ionosphere example
e, me = 1.602176634e-19, 9.1093837015e-31
N = 1e12
fp = np.sqrt(N * e ** 2 / (me * eps0)) / (2 * np.pi)
near(fp / 1e6, 8.98, "ionosphere: N = 1e12 m^-3 gives f_p = 8.98 MHz", rel=0.001)
near(fp / np.sqrt(N), 8.98, "f_p ~ 8.98 sqrt(N) Hz", rel=0.001)
r = np.sqrt(1 - (fp / 10e6) ** 2)
near(r, 0.440, "10 MHz: sqrt(1 - f_p^2/f^2) = v_g/c = 0.440", rel=0.002)
near(1 / r, 2.27, "10 MHz: v_p = 2.27c", rel=0.002)
near(300e3 / (r * c) * 1e3, 2.27, "300 km at v_g: 2.27 ms", rel=0.002)
near(300e3 / c * 1e3, 1.00, "300 km in vacuum: 1.00 ms", rel=0.002)
near(300e3 / (c / r) * 1e3, 0.44, "300 km at v_p: 0.44 ms", rel=0.01)
near(np.sqrt(1 - (fp / 100e6) ** 2), 0.996, "100 MHz: v_g = 0.996c", rel=0.0005)
# good conductor (concept page): exact beta from Lecture 22's gamma, seawater at 1 kHz
sig, er = 4.0, 81.0
beta_ex = lambda ww: np.sqrt(1j * ww * mu0 * (sig + 1j * ww * er * eps0)).imag
ww = 2 * np.pi * 1e3
vg_c = 2 * (ww * 1e-5) / (beta_ex(ww * (1 + 1e-5)) - beta_ex(ww * (1 - 1e-5)))
near(vg_c / (ww / beta_ex(ww)), 2.0, "good conductor (seawater, 1 kHz, exact beta): v_g = 2 v_p", rel=1e-4)
near(np.exp(-2 * np.pi), 0.0019, "good conductor: amplitude e^{-2 pi} = 0.19 % after one wavelength (alpha = beta)", rel=0.02)

print("C. Circular carrier (notes p. 2-3; page section 3)")
for z0 in (0.0, 0.3):
    E = np.cos(PH - z0)[:, None] * X + np.sin(PH - z0)[:, None] * Y      # Field 1 + Field 3 carriers
    Hc = np.cos(PH - z0)[:, None] * Y - np.sin(PH - z0)[:, None] * X
    close(cr(np.tile(Z, (len(PH), 1)), E), Hc, f"z = {z0}: H = z_hat x E / eta, = cos y - sin x (notes p. 3), eta factored")
    close(np.linalg.norm(E, axis=1), 1.0, f"z = {z0}: |E| constant: the vector rotates, not oscillates")
    ang = np.unwrap(np.arctan2(E[:, 1], E[:, 0]))
    close(ang[-1] - ang[0] + (PH[1] - PH[0]), 2 * np.pi, f"z = {z0}: angle advances 2 pi per period: rotation frequency = wave frequency", rtol=1e-6)
close(record(X - 1j * Y), np.cos(PH)[:, None] * X + np.sin(PH)[:, None] * Y, "phasor x - jy <-> cos wt x + sin wt y")
close(record(X + 1j * Y), np.cos(PH)[:, None] * X - np.sin(PH)[:, None] * Y, "phasor x + jy <-> cos wt x - sin wt y")

print("D. Handedness (notes p. 3-5; page section 4; Example 1)")
ok(hand(X - 1j * Y, Z) == "right", "x - jy, travel +z: right-circular (rotates x -> y)")
ok(hand(X + 1j * Y, Z) == "left", "x + jy, travel +z: left-circular")
ok(hand(X - 1j * Y, -Z) == "left", "trap: x - jy travelling -z is left-circular")
ok(hand(X + 1j * Y, -Z) == "right", "x + jy travelling -z is right-circular")
E = record(X - 1j * Y)
ok(E[0] @ X > 0.99 and E[len(PH) // 4] @ Y > 0.99, "x - jy: points along x at t = 0, along y at t = T/4 (x leads y)")
# clockwise when seen looking along +z: looking along +z means the viewer's line of sight is +z;
# rotation vector along +z = clockwise for that viewer (right-hand rule about the line of sight)
ok(spin(X - 1j * Y) @ Z > 0, "x - jy: rotation vector along +z = clockwise seen looking along +z")
# Example 1: (z + jy) e^{j beta x}: travel -x
Ep = Z + 1j * Y
close(record(Ep), np.cos(PH)[:, None] * Z - np.sin(PH)[:, None] * Y, "Example 1: E(x=0) = z cos wt - y sin wt")
Ey = record(Ep)[:, 1]; Ez = record(Ep)[:, 2]
ok((np.argmax(Ez) - np.argmax(Ey)) % len(PH) == len(PH) // 4,
   "Example 1: y peaks a quarter period before z (y leads z by 90 deg)")
ok(spin(Ep) @ X > 0, "Example 1: turns from y toward z (rotation vector +x = y x z)")
ok(hand(Ep, -X) == "left", "Example 1: travel -x, LEFT-circular (notes)")
close(cr(Ep.real, -Ep.imag), X, "Example 1 recipe line: z_hat x (-y_hat) = +x_hat")
ok(np.dot(-X, X) < 0, "Example 1 recipe: (-x) . x < 0 -> left")
# recipe == numerical rotation, and overall complex factors never change the hand
rng = np.random.default_rng(24)
for k in range(300):
    u = rng.normal(size=3); u /= np.linalg.norm(u)
    a = rng.normal(size=3); a -= (a @ u) * u
    b = rng.normal(size=3); b -= (b @ u) * u
    Ep = a + 1j * b
    g = rng.normal() + 1j * rng.normal()
    assert recipe(Ep, u) == hand(Ep, u) == hand(g * Ep, u) == recipe(g * Ep, u)
ok(True, "recipe sign u.[Re E x (-Im E)] = numerical rotation sense for 300 random (elliptical) phasors, and an overall complex factor never changes it")
for k in range(50):
    Ep = rng.normal(size=3) + 1j * rng.normal(size=3)
    assert np.allclose(spin(Ep), cr(Ep.real, -Ep.imag), atol=1e-9)
ok(True, "identity: <E x dE/dt>/omega = E(0) x E(T/4) = Re E x (-Im E) (50 random phasors)")

for Ep in (X + 0.5j * Y, 2 * X + np.exp(0.7j) * Y, (X + Y) * np.exp(0.3j)):
    r = np.linalg.norm(record(Ep), axis=1)
    close(axes(Ep), (r.max(), r.min()), "ellipse semi-axes from (1/2)Re{E E^H} = sampled max/min |E| (2000 samples)", rtol=1e-4, atol=3e-3)
print("E. Linear / circular / elliptical (page section 5; concept page table; figure pol-phase-family)")
for A, B in ((1.0, 1.0), (2.0, 4.0), (4.0, 2.0), (1.0, 0.0), (0.0, 1.0)):
    for phi in np.linspace(-np.pi, np.pi, 25):
        Ep = A * X + B * np.exp(1j * phi) * Y
        a1, a2 = axes(Ep)
        s = np.sin(phi)
        num = "linear" if a2 < 1e-6 * a1 else (("circular" if abs(a1 - a2) < 1e-6 * a1 else "elliptical"))
        rule_lin = abs(s) < 1e-9 or A == 0 or B == 0
        rule_circ = (A == B) and abs(abs(s) - 1) < 1e-9
        assert (num == "linear") == rule_lin, (A, B, phi, num)
        assert (num == "circular") == rule_circ, (A, B, phi, num)
        if not rule_lin:
            assert hand(Ep, Z) == ("right" if s < 0 else "left")
            assert hand(Ep * np.exp(0j), -Z) == ("left" if s < 0 else "right")
            if A == B == 1.0:
                assert F.pol_kind(phi) == hand(Ep, Z) + ("-circular" if rule_circ else "-elliptical")
        elif A == B == 1.0:
            assert F.pol_kind(phi) == "linear"
ok(True, "section 5 rule (linear phi = 0, pi or A or B = 0; circular A = B, phi = -/+ pi/2; elliptical otherwise; "
         "right iff sin phi < 0 for +z, swapped for -z) agrees with the traced ellipse and the rotation for 5 x 25 cases")
ok(hand(X + np.exp(-1j * np.pi / 2) * Y, Z) == "right" and hand(X + np.exp(1j * np.pi / 2) * Y, Z) == "left",
   "phi = -pi/2 right-circular, +pi/2 left-circular")

print("F. Bases (notes p. 5-6)")
R_, L_ = X - 1j * Y, X + 1j * Y
close(1 * X + (-1j) * Y, R_, "right = 1*x + (-j)*y")
close(1 * X + 1j * Y, L_, "left = 1*x + j*y")
close(0.5 * R_ + 0.5 * L_, X, "x = 1/2 R + 1/2 L")
close(-1 / 2j * R_ + 1 / 2j * L_, Y, "y = -1/(2j) R + 1/(2j) L")
close(np.vdot(R_, L_), 0, "R and L are orthogonal (Hermitian product)")

print("G. Example 2: rotating sheet current (notes p. 8)")
eta = eta0
mm = lambda tt: 1 + 0.3 * np.cos(0.01 * tt)
Js = lambda tt: mm(tt)[:, None] * (np.cos(tt)[:, None] * X + np.sin(tt)[:, None] * Y)
tt = np.linspace(0, 2 * np.pi, 400, endpoint=False)
vv = 1.0
for zz in (0.0, 0.7):
    Ep = -eta / 2 * Js(tt - zz / vv)
    Em = -eta / 2 * Js(tt + zz / vv)
    close(Ep, -eta / 2 * mm(tt - zz)[:, None] * (np.cos(tt - zz)[:, None] * X + np.sin(tt - zz)[:, None] * Y),
          f"E+ = -(eta/2) m(t - z/v)[cos(wt - bz) x + sin(wt - bz) y] at z = {zz} (w = b = v = 1)")
    close(Em, -eta / 2 * mm(tt + zz)[:, None] * (np.cos(tt + zz)[:, None] * X + np.sin(tt + zz)[:, None] * Y),
          f"E- = -(eta/2) m(t + z/v)[cos(wt + bz) x + sin(wt + bz) y] at z = -{zz}")
Ep0 = -eta / 2 * Js(tt)
Hp = cr(np.tile(Z, (len(tt), 1)), Ep0) / eta
Hm = cr(np.tile(-Z, (len(tt), 1)), Ep0) / eta
close(cr(np.tile(Z, (len(tt), 1)), Hp - Hm), Js(tt), "z = 0: n x (H+ - H-) = J_s with n = +z (Lecture 16 jump condition)")
close(Ep0 - Ep0, 0 * Ep0, "z = 0: E tangential continuous (E+ = E- at the sheet)")
ok(hand(-(X - 1j * Y), Z) == "right", "E+ carrier -(x - jy) e^{-jbz}: right-circular (minus sign adds 180 deg only)")
ok(hand(-(X - 1j * Y), -Z) == "left", "E- carrier -(x - jy) e^{+jbz}, travel -z: left-circular")
# margin figure: J_s = x f(t): E+ = -x (eta/2) f(t - z/v), H- = y (1/2) f(t + z/v)
close(cr(Z, -X * eta / 2) / eta, -Y / 2, "margin: H+ = z x E+/eta = -y (1/2) f")
close(cr(-Z, -X * eta / 2) / eta, Y / 2, "margin: H- = (-z) x E-/eta = +y (1/2) f (as printed)")
close(cr(-X, -Y), Z, "margin: S+ = E+ x H+ along +z")
close(cr(-X, Y), -Z, "margin: S- = E- x H- along -z")

print("H. Example 3 and power (notes p. 9; page section 8; concept page)")
Ec = X - 1j * Y
Hc = cr(Z, Ec) / eta0
close(Hc, (Y + 1j * X) / eta0, "H_c = z x E_c / eta0 = (y + jx)/eta0  [A/m]")
close(cr(-1j * Y, np.conj(1j * X)), Z, "(-j y) x (-j x) = j^2 (y x x) = +z")
close(cr(Ec, np.conj(Y + 1j * X)), 2 * Z, "(x - jy) x (y + jx)* = 2 z")
S_ph = 0.5 * np.real(cr(Ec, np.conj(Hc)))
Et = record(Ec); Ht = record(Hc)
S_q = cr(Et, Ht).mean(axis=0)
close(S_ph, Z / eta0, "<S> = z/eta0 (phasor)")
close(S_q, Z / eta0, "<S> = z/eta0 (time average by quadrature)")
near(1 / eta0 * 1e3, 2.65, "1/eta0 = 2.65 mW/m^2", rel=0.002)
near(1 / (120 * np.pi) * 1e3, 2.65, "1/(120 pi) = 2.65 mW/m^2", rel=0.002)
S_lin = 0.5 * np.real(cr(X, np.conj(cr(Z, X) / eta0)))
close(S_q, 2 * S_lin, "circular <S> is twice the linear 1/(2 eta0) of equal amplitude")
close(np.linalg.norm(cr(Et, Ht), axis=1), 1 / eta0, "circular: instantaneous S constant = <S>")
Sl = cr(record(X), record(cr(Z, X) / eta0))[:, 2]
close([Sl.max(), Sl.min()], [1 / eta0, 0.0], "linear: instantaneous S swings 0 .. 2<S> (pulses at 2 omega)")
for k in range(100):
    u = rng.normal(size=3); u /= np.linalg.norm(u)
    a = rng.normal(size=3) + 1j * rng.normal(size=3)
    a -= np.dot(u, a) * u
    et = rng.uniform(50, 400)
    S = 0.5 * np.real(cr(a, np.conj(cr(u, a) / et)))
    assert np.allclose(S, np.vdot(a, a).real / (2 * et) * u)
ok(True, "<S> = (|E_x|^2 + |E_y|^2) u/(2 eta) for 100 random plane waves (any phase between components)")

print("I. Worked problem: two crossed sheets a quarter wave apart")
f = 300e6
lam_ex = 3e8 / f
beta = 2 * np.pi / lam_ex
close([lam_ex, beta], [1.0, 2 * np.pi], "lambda = 1 m, beta = 2 pi rad/m (c = 3e8)")
e0 = 120 * np.pi
close(e0 / 2 * 0.1, 6 * np.pi, "eta0/2 x 0.1 A/m = 6 pi V/m")
near(-6 * np.pi, -18.8, "P = -6 pi = -18.8 V/m (3 s.f.)", rel=0.003)
d = lam_ex / 4


def total(z, phi):
    """phasor E of both sheets at z: -(eta0/2) J e^{-j beta |z - z0|}"""
    return (-e0 / 2 * 0.1 * X * np.exp(-1j * beta * abs(z - 0)) +
            -e0 / 2 * 0.1 * np.exp(1j * phi) * Y * np.exp(-1j * beta * abs(z - d)))


for phi in np.linspace(0, 2 * np.pi, 9, endpoint=False):
    Q = 1j * np.exp(1j * phi)
    for z in (0.3, 0.71, 2.2):
        assert np.allclose(total(z, phi), -6 * np.pi * np.exp(-1j * beta * z) * (X + Q * Y))
    for z in (-0.2, -1.37):
        assert np.allclose(total(z, phi), -6 * np.pi * np.exp(1j * beta * z) * (X + np.exp(1j * (phi - np.pi / 2)) * Y))
ok(True, "(a) z > lambda/4: E = -6 pi e^{-j beta z}(x + j e^{j phi} y); (c) z < 0: -6 pi [x + e^{j(phi - pi/2)} y] e^{j beta z}")
close(np.exp(1j * beta * lam_ex / 4), 1j, "e^{+j beta lambda/4} = j (sheet B's phase advance)")
cases = {np.pi / 2: "linear", 3 * np.pi / 2: "linear", np.pi: "right", 0.0: "left"}
for phi, want in cases.items():
    got = hand(total(0.5, phi) * np.exp(1j * beta * 0.5), Z)
    ok(got == want, f"(b) phi = {phi / np.pi:.2f} pi: {want} in z > lambda/4 (numerical rotation)")
close(1j * np.exp(1j * np.pi / 2), -1, "(b) phi = pi/2: Q = -1, linear along x - y")
close(1j * np.exp(1j * 3 * np.pi / 2), 1, "(b) phi = 3pi/2: Q = +1, linear along x + y")
grid = np.linspace(0, 2 * np.pi, 3600, endpoint=False)                  # 0.1 deg steps, contains pi/2, pi, 3pi/2
circ_R = [p for p in grid if abs(1j * np.exp(1j * p) + 1j) < 1e-9]
circ_L = [p for p in grid if abs(1j * np.exp(1j * p) - 1j) < 1e-9]
lin = [p for p in grid if abs((1j * np.exp(1j * p)).imag) < 1e-9]
close(circ_R + circ_L, [np.pi, 0.0], "(b) only phi = pi is right-circular and only phi = 0 left-circular in [0, 2 pi)")
close(lin, [np.pi / 2, 3 * np.pi / 2], "(b) only phi = pi/2, 3pi/2 are linear in [0, 2 pi)")
Ep = total(0.5, np.pi) * np.exp(1j * beta * 0.5)
close(Ep, -6 * np.pi * (X - 1j * Y), "(b) phi = pi: E = -6 pi (x - jy) e^{-j beta z}")
close([Ep.real, -Ep.imag], [-6 * np.pi * X, -6 * np.pi * Y], "(b) E(0) = -6 pi x, E(T/4) = -6 pi y")
close(cr(Ep.real, -Ep.imag), 36 * np.pi ** 2 * Z, "(b) E(0) x E(T/4) = 36 pi^2 z, along the travel: right")
close(record(Ep), -6 * np.pi * (np.cos(PH)[:, None] * X + np.sin(PH)[:, None] * Y), "(b) time domain -6 pi [cos x + sin y] at z = 0")
Em = total(-0.4, np.pi) * np.exp(-1j * beta * (-0.4))
close(Em, -6 * np.pi * (X + 1j * Y), "(c) phi = pi, z < 0: E = -6 pi (x + jy) e^{j beta z}")
close([Em.real, -Em.imag], [-6 * np.pi * X, 6 * np.pi * Y], "(c) E(0) = -6 pi x, E(T/4) = +6 pi y")
close(cr(Em.real, -Em.imag), -36 * np.pi ** 2 * Z, "(c) E(0) x E(T/4) = -36 pi^2 z, along u = -z")
ok(hand(Em, -Z) == "right", "(c) right-circular in z < 0 too (numerical rotation)")
ok(hand(total(-0.4, 0.0) * np.exp(-1j * beta * (-0.4)), -Z) == "left", "(c, aside) phi = 0: left-circular on both sides")
for phi in (np.pi / 2, 3 * np.pi / 2, np.pi, 0.0):
    Ep = total(0.5, phi)
    S = 0.5 * np.real(cr(Ep, np.conj(cr(Z, Ep) / e0)))
    close(S, 0.3 * np.pi * Z, f"(d) phi = {phi / np.pi:.2f} pi: <S> = 0.3 pi z W/m^2")
near(0.3 * np.pi, 0.94, "(d) 0.3 pi = 0.94 W/m^2", rel=0.005)
close((6 * np.pi) ** 2 / (2 * e0), 0.15 * np.pi, "(d) each sheet alone: 0.15 pi W/m^2")
# both sheets: jump conditions satisfied by the total phasor field (H from each travelling wave)
for z0, Jp in ((0.0, 0.1 * X), (d, 0.1 * np.exp(1j * 0.7) * Y)):
    def Hsheet(z, zs, J):
        u = Z if z > zs else -Z
        return cr(u, -e0 / 2 * J * np.exp(-1j * beta * abs(z - zs))) / e0
    jump = cr(Z, Hsheet(z0 + 1e-12, z0, Jp) - Hsheet(z0 - 1e-12, z0, Jp))
    close(jump, Jp, f"sheet at z = {z0}: z x (H(z0+) - H(z0-)) = J_s (phasor)")

print("J. Figures (figs_l24.py): screen frame and arrow senses")
# screen frame X right, Y up, Z out of the page. Polarization views: x_hat drawn up, y_hat drawn right.
xs, ys = np.array([0, 1, 0]), np.array([1, 0, 0])
close(cr(xs, ys), [0, 0, -1], "views: x_hat (up) x y_hat (right) = into the page: +z points into the page (otimes), frame right-handed")
toS = lambda E: E[0] * xs + E[1] * ys                     # physics (Ex, Ey) -> screen vector
for s, want in ((-1, "right"), (+1, "left")):
    Ep = X + s * 1j * Y                                     # s = -1: x - jy ; s = +1: x + jy
    E0, E8 = record(Ep)[0], record(Ep)[len(PH) // 8]
    zscr = cr(toS(E0), toS(E8))[2]
    ok((zscr < 0) == (want == "right"), f"pol-handedness panel s = {s}: t=0 -> t=T/8 is {'clockwise' if zscr < 0 else 'counterclockwise'} on the page = {want}")
    # the drawn vectors in the figure code: X = -s sin wt, Y = cos wt
    wt = np.pi / 4
    close(toS(E8)[:2], [-s * np.sin(wt), np.cos(wt)], f"pol-handedness panel s = {s}: drawn T/8 arrow matches the field")
    ok(hand(Ep, Z) == want, f"pol-handedness panel s = {s}: {want}-circular by the numerical rotation")
    # rotation arc from math angle pi/2 + s*0.12 to pi/2 + s*1.15: CCW iff s > 0
    ok((s * (1.15 - 0.12) > 0) == (want == "left"), f"pol-handedness arc for s = {s} drawn {'CCW' if s > 0 else 'CW'}")
for phi, lab in F.PHASES:
    Ep = X + np.exp(1j * phi) * Y
    kind = F.pol_kind(phi)
    if kind != "linear":
        a0 = 0.10; a1 = 0.75
        P0 = toS(np.real(Ep * np.exp(1j * a0))); P1 = toS(np.real(Ep * np.exp(1j * a1)))
        zscr = cr(P0, P1)[2]
        ok((zscr < 0) == kind.startswith("right"), f"pol-phase-family phi = {lab}: drawn sense {'CW' if zscr < 0 else 'CCW'} = {kind}")
    else:
        ok(axes(Ep)[1] < 1e-9, f"pol-phase-family phi = {lab}: linear (no arrow)")
    dot = toS(record(Ep)[0])
    close(dot[:2], [np.cos(phi), 1.0], f"pol-phase-family phi = {lab}: t = 0 dot at screen (cos phi, 1)")
# AM figure: markers sit where the exact field puts them
t1, dT = 20.0, 20.0
zz = np.linspace(0, 54, 5401)
for tt_ in (t1, t1 + dT):
    Ez, env = F.am_field(zz, tt_)
    near(zz[np.argmax(env)], vg * tt_, f"pol-am-group-delay t = {tt_}: envelope peak at v_g t", rel=0.01)
k = np.round((F.W0 * t1 - b0 * vg * t1) / (2 * np.pi))
zc1 = (F.W0 * t1 - 2 * np.pi * k) / b0
for tt_, zc in ((t1, zc1), (t1 + dT, zc1 + vp * dT)):
    zl = np.linspace(zc - 0.5, zc + 0.5, 2001)
    Ez, _ = F.am_field(zl, tt_)
    ok(abs(zl[np.argmax(Ez)] - zc) < 0.02 * 2 * np.pi / b0,
       f"pol-am-group-delay t = {tt_}: marked crest z = {zc:.3f} is within 2 % of a wavelength of the exact field's crest "
       f"{zl[np.argmax(Ez)]:.3f} (< 0.5 px; the envelope slope shifts the maximum slightly)")
ok(zc1 + vp * dT > vg * (t1 + dT), "pol-am-group-delay: the crest has moved ahead of the envelope peak")

print("K. Notes slips (ERRATA-L24.md)")
# Example 3: H_c = E/eta0 has units (V/m)/Ohm = A/m, not V/m as printed
ok(True, "Example 3: [E]/[eta] = (V/m)/(V/A) = A/m; the notes print V/m for H_c")
# footnote: v_g written as partial derivative; value checked in B. Example 3 sign chain checked in H.
ok(True, "Example 3 algebra (x - jy) x (y + jx)* = 2z and <S> = z/eta0: no sign error (section H)")

print(f"\nALL {ok_count} CHECKS PASSED")
