"""Agent A checks: Lecture 20 and Lectures 21-22a slide numbers added to the site."""
import numpy as np

c = 299792458.0
mu0 = 4e-7 * np.pi
eps0 = 1 / (mu0 * c**2)
eta0 = np.sqrt(mu0 / eps0)
X, Y, Z = np.eye(3)
n_pass = n_fail = 0


def check(name, ok):
    global n_pass, n_fail
    print(("PASS " if ok else "FAIL ") + name)
    if ok:
        n_pass += 1
    else:
        n_fail += 1


def close(a, b, rtol=1e-6, atol=1e-12):
    return bool(np.allclose(a, b, rtol=rtol, atol=atol))


# ---------- L20 slide 8: time-averaged power of the sheet's wave ----------
Js0, w = 2.7, 2 * np.pi * 1e6
beta = w / c
T = 2 * np.pi / w
t = np.linspace(0, T, 200001)
for z in (0.0, 13.0, 77.7):
    Ex = eta0 * Js0 / 2 * np.cos(w * t - beta * z)
    Hy = Js0 / 2 * np.cos(w * t - beta * z)
    Sz = Ex * Hy
    avg = np.trapezoid(Sz, t) / T
    check(f"L20 s8 <Sz> = eta0 Js0^2/8 at z={z}", close(avg, eta0 * Js0**2 / 8, rtol=1e-6))
H0 = Js0 / 2
check("L20 s8 eta0 Js0^2/8 = eta0 H0^2/2 with H0 = Js0/2", close(eta0 * Js0**2 / 8, eta0 * H0**2 / 2))
# direction for z>0 and z<0 (sheet -x Js0 cos wt): E = +x (eta0/2)J, H = +-y J/2
Jvec = -X * Js0
for side, nhat in ((+1, Z), (-1, -Z)):
    E = -eta0 / 2 * Jvec
    H = 0.5 * np.cross(Jvec, nhat)
    S = np.cross(E, H)
    check(f"L20 s2-3,8 S points away from sheet (side {side})", close(S / np.linalg.norm(S), nhat))

# ---------- L20 slide 7 slip: S = |Ex||Hy| a_z only for z>0 ----------
Jt = 1.3
Ex_below, Hy_below = eta0 / 2 * Jt, -0.5 * Jt
Sz_below = Ex_below * Hy_below
check("L20 s7 z<0: Sz = ExHy < 0 while |Ex||Hy| > 0", Sz_below < 0 and abs(Ex_below) * abs(Hy_below) > 0)
check("L20 s7 ink: Ey = 0 for this wave, so ExEy = 0 != Sz", abs(Ex_below * 0.0) == 0 and Sz_below != 0)

# ---------- L20 slides 6-7: 1-D box route, d(ExHy)/dz = -d/dt(1/2 mu0 Hy^2 + 1/2 eps0 Ex^2) ----------
f = lambda u: np.exp(-((u - 3e-7) / 5e-8) ** 2) * np.cos(4e7 * u)
z0, t0, dz, dt = 40.0, 4.2e-7, 1e-4, 1e-13
Exf = lambda z, t: eta0 * f(t - z / c)
Hyf = lambda z, t: f(t - z / c)
dSdz = (Exf(z0 + dz, t0) * Hyf(z0 + dz, t0) - Exf(z0 - dz, t0) * Hyf(z0 - dz, t0)) / (2 * dz)
wf = lambda z, t: 0.5 * mu0 * Hyf(z, t) ** 2 + 0.5 * eps0 * Exf(z, t) ** 2
dwdt = (wf(z0, t0 + dt) - wf(z0, t0 - dt)) / (2 * dt)
check("L20 s7 box: dSz/dz = -dw/dt off the sheet", close(dSdz, -dwdt, rtol=1e-5))

# ---------- L20 slide 9 ----------
w9, b9 = 6 * np.pi * 1e7, 0.2 * np.pi
check("L20 s9 f = 30 MHz", close(w9 / (2 * np.pi), 30e6))
check("L20 s9 lambda = 10 m", close(2 * np.pi / b9, 10.0))
check("L20 s9 v_p = 3e8 m/s (= c to 0.07 %)", close(w9 / b9, 3e8) and abs(w9 / b9 / c - 1) < 1e-3)
E9 = X * eta0
H9 = Y * 1.0
check("L20 s9 S = E x H along +z", close(np.cross(E9, H9) / eta0, Z))
Pa = eta0 * 1.0**2 * np.cos(0) ** 2 * 1.0
check("L20 s9(a) P(t=0) = eta0 H0^2 ~ 377 H0^2 W", close(Pa, eta0) and round(eta0) == 377 and close(120 * np.pi, 377.0, rtol=1e-3))
ph = w9 * (1 / 8) * 1e-6
check("L20 s9(b) wt = 7.5 pi", close(ph, 7.5 * np.pi))
check("L20 s9(b) cos^2(7.5pi) = 0 -> P = 0", abs(np.cos(ph) ** 2) < 1e-20)
check("L20 s9(b) ink cos(15pi/2) also 0", abs(np.cos(15 * np.pi / 2)) < 1e-12)
check("L20 s9(c) Pavg = eta0/2 H0^2 = 60pi H0^2 ~ 188", close(eta0 / 2, 60 * np.pi, rtol=1e-3) and round(eta0 / 2) == 188)

# ---------- L20 slide 13 challenge ----------
H0 = 1.0
bet = 1.0  # cos(ct + x): beta = 1 rad/m, omega = c
om = c * bet
lam = 2 * np.pi / bet
Ev, Hv = Z * eta0 * H0, Y * H0
Sdir = np.cross(Ev, Hv)
check("L20 s13 S along -x", close(Sdir / np.linalg.norm(Sdir), -X))
uhat = -X
check("L20 s13 H = u x E / eta0 (valid wave toward -x)", close(np.cross(uhat, Ev) / eta0, Hv))
tt = np.linspace(0, 2 * np.pi / om, 1001)
Sx = lambda x, t: -eta0 * H0**2 * np.cos(om * t + bet * x) ** 2
outflow = Sx(1.0, tt) * 1 + Sx(0.0, tt) * (-1)
check("L20 s13(a) net outflow = eta0 H0^2[cos^2 ct - cos^2(ct+1)]",
      close(outflow, eta0 * H0**2 * (np.cos(om * tt) ** 2 - np.cos(om * tt + 1) ** 2)))
check("L20 s13(a) net outflow not zero at all times", np.max(np.abs(outflow)) > 0.1 * eta0)
xs = np.linspace(0, 1, 20001)
We = np.array([np.trapezoid(0.5 * eps0 * (eta0 * H0 * np.cos(om * ti + bet * xs)) ** 2, xs) for ti in tt[::50]])
check("L20 s13(c) electric energy in slab varies in time", (We.max() - We.min()) / We.mean() > 0.1)
check("L20 s13(c) 1 m is not a multiple of lambda/2 = pi m", abs(1.0 / (lam / 2) - round(1.0 / (lam / 2))) > 0.1)
for x in (0.0, 0.3, 0.9):
    we_avg = np.trapezoid(0.5 * eps0 * (eta0 * H0 * np.cos(om * tt + bet * x)) ** 2, tt) / tt[-1]
    check(f"L20 s13(d) <w_e>(x={x}) = mu0 H0^2/4", close(we_avg, mu0 * H0**2 / 4, rtol=1e-4))
check("L20 s13(d) eps0 eta0^2 = mu0", close(eps0 * eta0**2, mu0))
wtot = 0.5 * eps0 * (eta0 * H0 * np.cos(om * tt + 0.4)) ** 2 + 0.5 * mu0 * (H0 * np.cos(om * tt + 0.4)) ** 2
check("L20 s13(e) w = mu0 H0^2 cos^2(ct+x), varies", close(wtot, mu0 * H0**2 * np.cos(om * tt + 0.4) ** 2) and np.ptp(wtot) > 0)

# ---------- L21-22a slides 8-18: cosine sheet in a lossy medium ----------
sig, epsr, mur, fr, Js0 = 0.02, 4.0, 1.0, 50e6, 1.6
eps, mu, w = epsr * eps0, mur * mu0, 2 * np.pi * fr
gam = np.sqrt(1j * w * mu * (sig + 1j * w * eps))
eta = np.sqrt(1j * w * mu / (sig + 1j * w * eps))
al, be = gam.real, gam.imag
tau = np.angle(eta)
check("L21-22a s12 gamma has alpha>0, beta>0", al > 0 and be > 0)
check("L21-22a s12 gamma*eta = j w mu", close(gam * eta, 1j * w * mu))
A, theta = abs(eta) * Js0 / 2, tau  # slide 16 result


def Ex(z, t):
    s = np.sign(z)
    return A * np.exp(-al * abs(z)) * np.cos(w * t - s * be * z + theta)


def Hy(z, t):
    s = np.sign(z)
    return s * Js0 / 2 * np.exp(-al * abs(z)) * np.cos(w * t - s * be * z)


# PDEs on both sides: dEx/dz = -mu dHy/dt, dHy/dz = -sig Ex - eps dEx/dt
hz, ht = 1e-5, 1e-13
for zz in (0.7, -1.3):
    for t0 in (0.0, 3.3e-9):
        l1 = (Ex(zz + hz, t0) - Ex(zz - hz, t0)) / (2 * hz)
        r1 = -mu * (Hy(zz, t0 + ht) - Hy(zz, t0 - ht)) / (2 * ht)
        l2 = (Hy(zz + hz, t0) - Hy(zz - hz, t0)) / (2 * hz)
        r2 = -sig * Ex(zz, t0) - eps * (Ex(zz, t0 + ht) - Ex(zz, t0 - ht)) / (2 * ht)
        check(f"L21-22a s17 Faraday z={zz} t={t0}", close(l1, r1, rtol=1e-5, atol=1e-6))
        check(f"L21-22a s17 Ampere z={zz} t={t0}", close(l2, r2, rtol=1e-5, atol=1e-6))
tt = np.linspace(0, 1 / fr, 7)
check("L21-22a s15 Ex continuous at z=0", close(Ex(1e-12, tt), Ex(-1e-12, tt), rtol=1e-6, atol=1e-9))
for t0 in tt:
    H1 = Y * Hy(1e-12, t0)
    H2 = Y * Hy(-1e-12, t0)
    Js = -X * Js0 * np.cos(w * t0)
    if not close(np.cross(Z, H1 - H2), Js, rtol=1e-6, atol=1e-9):
        check("L21-22a s16 n x (H1 - H2) = Js", False)
        break
else:
    check("L21-22a s16 n x (H1 - H2) = Js at all sampled t", True)
check("L21-22a s16 A = |eta| Js0/2, theta = tau", close(2 * A / abs(eta), Js0) and theta == tau)
# phasor form slide 18 equals site's E~ = -(eta/2) J~s e^{-gamma d}
Jt = -X * Js0
zz = 0.9
Ep_site = -eta / 2 * Jt * np.exp(-gam * zz)
Ep_slide = X * eta * Js0 / 2 * np.exp(-gam * zz)
check("L21-22a s18 slides' phasor = site's -(eta/2)J~s e^{-gamma d}", close(Ep_site, Ep_slide))
t0 = 1.234e-9
check("L21-22a s17/18 time domain = Re{phasor e^{jwt}}", close((Ep_slide[0] * np.exp(1j * w * t0)).real, Ex(zz, t0)))
# E leads H by tau; crest shift tau/beta <= lambda/8
check("L21-22a s23 E leads H by tau (0<tau<pi/4)", 0 < tau < np.pi / 4)
check("L21-22a s23 tau = (1/2) atan(sig/(w eps))", close(tau, 0.5 * np.arctan(sig / (w * eps))))
taus = [np.angle(np.sqrt(1j * w * mu0 / (s + 1j * w * eps0))) for s in np.logspace(-6, 8, 200)]
check("L21-22a s21-23 tau < 45 deg for all sigma", max(taus) < np.pi / 4)
check("L21-22a s21-23 dz = tau/beta < lambda/8", max(taus) / (2 * np.pi) < 1 / 8)
# crest positions at t = 0 for z>0: E crest where -beta z + tau = 0, H crest at z = 0
zE = tau / be
check("L21-22a s19 E crest tau/beta ahead of H crest", close(np.cos(-be * zE + tau), 1.0))
# slide 18: E~x = eta H~y only for z>0
zz = -0.8
Exm = eta * Js0 / 2 * np.exp(gam * zz)
Hym = -Js0 / 2 * np.exp(gam * zz)
check("L21-22a s18 z<0: E~x = -eta H~y", close(Exm, -eta * Hym))
zz = 0.8
Exp = lambda z: eta * Js0 / 2 * np.exp(-gam * z)
Hyp = -(Exp(zz + 1e-6) - Exp(zz - 1e-6)) / 2e-6 / (1j * w * mu)  # phasor Faraday
check("L21-22a s18 z>0: E~x = eta H~y (H~y from phasor Faraday)", close(Exp(zz), eta * Hyp, rtol=1e-6))
check("L21-22a s18 z>0: H~y = Js0/2 e^{-gamma z}, in phase with the source at z=0", close(Hyp, Js0 / 2 * np.exp(-gam * zz), rtol=1e-6))
# slide 22: |eta| != eta0 here
check("L21-22a s22 |eta| != eta0 in the example medium", abs(abs(eta) - eta0) > 1)

# ---------- slide 21 slip: red box is E, written as H with a_x ----------
Ewritten = Js0 / 2  # amplitude written in the box
check("L21-22a s21 box amplitude Js0/2 != |eta| Js0/2 (it is H's)", abs(Ewritten - A) > 1)
check("L21-22a s21 dB/m = 8.686 x Np/m", close(20 * np.log10(np.e), 8.686, rtol=1e-4))
# ---------- slide 23 slip: E along a_y ----------
check("L21-22a s23 E,H both along y give S = 0 (wrong)", close(np.cross(Y, Y), np.zeros(3)))
check("L21-22a s23 E along x, H along y give S along +z", close(np.cross(X, Y), Z))

# ---------- slide 25 challenge: sigma = 0, eps = 2 eps0, mu = mu0 ----------
eps25 = 2 * eps0
g25 = np.sqrt(1j * w * mu0 * (0 + 1j * w * eps25))
e25 = np.sqrt(1j * w * mu0 / (0 + 1j * w * eps25))
check("L21-22a s25 alpha = 0", abs(g25.real) < 1e-12 * abs(g25))
check("L21-22a s25 tau = 0", abs(np.angle(e25)) < 1e-12)
vp25 = w / g25.imag
check("L21-22a s25 v_p = c/sqrt2 = 2.12e8 m/s", close(vp25, c / np.sqrt(2)) and round(vp25 / 1e6) == 212)
check("L21-22a s25 eta = eta0/sqrt2 ~ 266 ohm", close(abs(e25), eta0 / np.sqrt(2)) and round(abs(e25)) == 266)

# ---------- slide 24: 'nonlinear' beta(omega); affine also disperses ----------
ws = np.linspace(1e6, 1e9, 5)
a_, b_ = 1 / c, 0.3
vp_aff = ws / (a_ * ws + b_)
check("L21-22a s24 beta = a w + b gives w-dependent v_p", np.ptp(vp_aff) > 1e6)

# ---------- slide 2 (repeat of L17 s18): solenoid core changes B, not H ----------
n_turns, I = 1000.0, 0.5
for mur_core in (1.0, 500.0):
    Hcore = n_turns * I  # Ampere's law, free current only
    Bcore = mur_core * mu0 * Hcore
check("L21-22a s2 long solenoid: H = nI independent of mu_r, B scales", Hcore == 500.0 and close(Bcore, 500 * mu0 * 500.0))

print(f"\n{n_pass} PASS, {n_fail} FAIL")
