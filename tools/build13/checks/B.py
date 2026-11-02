"""Agent B checks: slides Lectures 22b-23 (waves in material) and 24 (polarization)."""
import numpy as np

ok_all = True


def chk(name, cond):
    global ok_all
    ok_all &= bool(cond)
    print(("PASS " if cond else "FAIL ") + name)


x, y, z = np.eye(3)
mu0 = 4e-7 * np.pi
eps0 = 8.8541878128e-12
c = 1 / np.sqrt(mu0 * eps0)
eta0 = np.sqrt(mu0 / eps0)


def gam_eta(sig, eps, mu, w):
    g = np.sqrt(1j * w * mu * (sig + 1j * w * eps))
    if g.real < 0:
        g = -g
    return g, 1j * w * mu / g


def hand(Et, u):
    """Recipe: u . [E(0) x E(T/4)] > 0 right, < 0 left (phasor at exponent 1)."""
    E0, E4 = np.real(Et), -np.imag(Et)
    s = np.dot(u, np.cross(E0, E4))
    return "R" if s > 1e-12 else ("L" if s < -1e-12 else "lin")


# ---------- deck 22b-23 ----------
# slide 7: |eta| and tau from eta^2; tau = (1/2) atan(sigma/(w eps)) (site's tau)
rng = np.random.default_rng(7)
for _ in range(5):
    sig, epsr, w = 10 ** rng.uniform(-4, 2), rng.uniform(1, 80), 2 * np.pi * 10 ** rng.uniform(3, 10)
    eps = epsr * eps0
    g, e = gam_eta(sig, eps, mu0, w)
    eta2 = w * mu0 * (w * eps + 1j * sig) / (sig ** 2 + (w * eps) ** 2)
    ok = np.isclose(e ** 2, eta2) and np.isclose(abs(e), np.sqrt(w * mu0 / np.sqrt(sig ** 2 + (w * eps) ** 2))) \
        and np.isclose(np.angle(e), 0.5 * np.arctan(sig / (w * eps)))
    chk(f"s7 eta^2, |eta|, tau = atan(p)/2 (p={sig/(w*eps):.3g})", ok)
# slide 4 closed forms
sig, eps, w = 0.04, 4 * eps0, 2 * np.pi * 1.8e8
g, e = gam_eta(sig, eps, mu0, w)
p = sig / (w * eps)
a = w * np.sqrt(mu0 * eps / 2) * np.sqrt(np.sqrt(1 + p ** 2) - 1)
b = w * np.sqrt(mu0 * eps / 2) * np.sqrt(np.sqrt(1 + p ** 2) + 1)
chk("s4 closed forms alpha, beta", np.isclose(g.real, a) and np.isclose(g.imag, b))

# slide 8: gamma = 0.05 + j0.1 /m, f = 1 MHz, mu0
f = 1e6
w = 2 * np.pi * f
g = 0.05 + 0.1j
chk("s8a 1/alpha = 20 m", np.isclose(1 / g.real, 20))
chk("s8b 1/beta = 10 m", np.isclose(1 / g.imag, 10))
d = w / g.imag * 1e-6
chk("s8c v_p * 1us = 20 pi = 62.8 m", np.isclose(d, 20 * np.pi) and round(d, 1) == 62.8)
eta = 1j * w * mu0 / g
chk("s8d |eta| = 70.6 ohm", round(abs(eta), 1) == 70.6)
tau = np.angle(eta)
chk("s8e tau = pi/2 - atan(2) = 26.6 deg = 0.464 rad",
    np.isclose(tau, np.pi / 2 - np.arctan(0.1 / 0.05)) and round(np.degrees(tau), 1) == 26.6
    and round(tau, 3) == 0.464)
g2 = g ** 2
chk("s8 gamma^2 = -0.0075 + j0.01", np.isclose(g2, -0.0075 + 0.01j))
sig8 = g2.imag / (w * mu0)
eps8 = -g2.real / (w ** 2 * mu0)
chk("s8 sigma = 1.27 mS/m", round(sig8 * 1e3, 2) == 1.27)
chk("s8 eps_r = 17.1", round(eps8 / eps0, 1) == 17.1)
p8 = sig8 / (w * eps8)
chk("s8 sigma/(w eps) = 4/3 = tan(2 tau)", np.isclose(p8, 4 / 3) and np.isclose(np.tan(2 * tau), 4 / 3))
gg, ee = gam_eta(sig8, eps8, mu0, w)
chk("s8 medium reproduces gamma and eta", np.isclose(gg, g) and np.isclose(ee, eta))
# E = eta H: angle(E) = angle(H) + tau
H = 1.0
chk("s8 ink: angle E = angle H + tau", np.isclose(np.angle(eta * H), np.angle(H) + tau))

# slide 13: E = z 10 cos(3pi e7 t - 0.2 pi x), mu0, lossless
w = 3 * np.pi * 1e7
beta = 0.2 * np.pi
chk("s13a f = 15 MHz", np.isclose(w / (2 * np.pi), 15e6))
chk("s13b lambda = 10 m", np.isclose(2 * np.pi / beta, 10))
vp = w / beta
chk("s13c v_p = 1.5e8 m/s", np.isclose(vp, 1.5e8))
chk("s13c v_p = c/2 with c = 3e8 (exact c: 1.0007 c/2)", np.isclose(vp, 3e8 / 2) and abs(vp / (c / 2) - 1) < 1e-3)
epsr = (3e8 / vp) ** 2
chk("s13d eps_r = 4", np.isclose(epsr, 4))
eta13 = 120 * np.pi * np.sqrt(1 / epsr)
chk("s13e eta = eta0/2 = 60 pi = 188 ohm", np.isclose(eta13, 60 * np.pi) and round(eta13) == 188)
u = x
Hdir = np.cross(u, z)
chk("s13e H along x cross z = -y", np.allclose(Hdir, -y))
Hamp = 10 / eta13
chk("s13e |H| = 53.1 mA/m", round(Hamp * 1e3, 1) == 53.1)
chk("s13e E x H along +x", np.allclose(np.cross(z, -y), x))

# slides 17-18: imperfect dielectric shortcuts within ~0.1 % at p = 0.1 (site's "within 0.3 %")
w = 2 * np.pi * 1e9
eps = 4 * eps0
sig = 0.1 * w * eps
g, e = gam_eta(sig, eps, mu0, w)
chk("s17 alpha ~ (sigma/2)sqrt(mu/eps) within 0.3 % at p = 0.1",
    abs(sig / 2 * np.sqrt(mu0 / eps) / g.real - 1) < 3e-3)
chk("s18 tau ~ sigma/(2 w eps) within 0.4 % at p = 0.1", abs(0.05 / np.angle(e) - 1) < 4e-3)

# slide 16 chart thresholds 0.01 / 100 vs site 0.1 / 10: errors of the shortcuts
for pp in (0.01, 0.1):
    sig = pp * w * eps
    g, e = gam_eta(sig, eps, mu0, w)
    err = abs(sig / 2 * np.sqrt(mu0 / eps) / g.real - 1)
    chk(f"s16/17 imperfect-dielectric alpha error at p={pp}: {100*err:.3f} %", err < 3e-3)
for pp, lim in ((10, 0.06), (100, 0.006)):
    sig = pp * w * eps
    g, e = gam_eta(sig, eps, mu0, w)
    err = abs(np.sqrt(w * mu0 * sig / 2) / g.real - 1)
    chk(f"s16 good-conductor alpha error at p={pp}: {100*err:.2f} %", err < lim)

# slides 20-21: sqrt(j) = (1+j)/sqrt2 = e^{j45}; alpha = beta; |eta| = sqrt(w mu/sigma), tau -> 45
chk("s20 sqrt(j) = (1+j)/sqrt2 = e^{j pi/4}",
    np.isclose(np.sqrt(1j), (1 + 1j) / np.sqrt(2)) and np.isclose(np.angle(np.sqrt(1j)), np.pi / 4))
sig, eps, w = 5.8e7, eps0, 2 * np.pi * 1e6
g, e = gam_eta(sig, eps, mu0, w)
chk("s20 copper 1 MHz alpha = beta = sqrt(w mu sigma/2)",
    np.isclose(g.real, np.sqrt(w * mu0 * sig / 2), rtol=1e-6) and np.isclose(g.imag, g.real, rtol=1e-6))
chk("s21 |eta| = sqrt(w mu/sigma), tau = pi/4 (to 1e-6)",
    np.isclose(abs(e), np.sqrt(w * mu0 / sig), rtol=1e-6) and abs(np.angle(e) - np.pi / 4) < 1e-6)
# errata row: tau < 45 deg exactly; 42.1 deg at p = 10
tau10 = 0.5 * np.degrees(np.arctan(10))
chk("errata: exact tau at p = 10 is 42.1 deg (< 45)", round(tau10, 1) == 42.1)
w = 2 * np.pi * 1e9
eps = 4 * eps0
sig = 10 * w * eps
g, e = gam_eta(sig, eps, mu0, w)
chk("errata: at p = 10 boxed |eta| = sqrt(w mu/sigma) is 0.25 % high",
    round(100 * (np.sqrt(w * mu0 / sig) / abs(e) - 1), 2) == 0.25)
sig = 0.1 * w * eps
g, e = gam_eta(sig, eps, mu0, w)
chk("errata: imperfect alpha formula is approximate (0.12 % high at p = 0.1)",
    round(100 * (sig / 2 * np.sqrt(mu0 / eps) / g.real - 1), 2) == 0.12)

# slide 22: delta = 1/alpha = sqrt(2/(w mu sigma)) = 1/sqrt(pi f mu sigma)
f = 1e6
chk("s22 two forms of delta agree",
    np.isclose(np.sqrt(2 / (2 * np.pi * f * mu0 * 5.8e7)), 1 / np.sqrt(np.pi * f * mu0 * 5.8e7)))
# skin-effect ring: wire radius a >> delta, R ratio ~ a/(2 delta) (site value 7.6 for 1 mm Cu at 1 MHz)
a = 1e-3
dl = 1 / np.sqrt(np.pi * f * mu0 * 5.8e7)
ratio = (np.pi * a ** 2) / (2 * np.pi * a * dl)
chk("s22-23 ink R = L/(sigma A), A = 2 pi a delta: ratio a/(2 delta) = 7.6", round(ratio, 1) == 7.6)

# slide 24: perfect conductor alpha -> inf, delta -> 0
alphas = [gam_eta(s, eps0, mu0, 2 * np.pi * 1e6)[0].real for s in (1e6, 1e9, 1e12)]
chk("s24 alpha grows as sqrt(sigma) without bound (delta -> 0)",
    alphas[0] < alphas[1] < alphas[2] and np.isclose(alphas[2] / alphas[1], np.sqrt(1e3), rtol=1e-6))

# slide 25 summary: good-conductor v_p = sqrt(2 w/(sigma mu)), lambda = 2 pi / sqrt(pi f mu sigma)
sig, w = 4.0, 2 * np.pi * 1e3
g, e = gam_eta(sig, 81 * eps0, mu0, w)
chk("s25 v_p ~ sqrt(2w/(sigma mu))", np.isclose(w / g.imag, np.sqrt(2 * w / (sig * mu0)), rtol=1e-5))
sig, eps, w = 1e-3, 4 * eps0, 2 * np.pi * 1e9
g, e = gam_eta(sig, eps, mu0, w)
chk("s25 imperfect delta ~ (2/sigma) sqrt(eps/mu)", np.isclose(1 / g.real, 2 / sig * np.sqrt(eps / mu0), rtol=1e-4))

# ---------- deck 24 ----------
# slide 2: J = -J0 cos(wt) x on z=0 -> E = -(eta/2) J -> +x (eta0 J0/2) cos(wt -+ beta z)
J0 = 1.0
E_sheet = -(eta0 / 2) * (-J0 * x)
chk("L24 s2 E_x = +eta0 J0/2", np.allclose(E_sheet, eta0 / 2 * x))

# slide 7: linear, tilt alpha = atan(E2/E1)
E1, E2 = 1.0, 2.0
Et = E1 * x + E2 * y
chk("L24 s7 in phase -> linear", hand(Et, z) == "lin")
chk("L24 s7 180 deg -> linear", hand(E1 * x - E2 * y, z) == "lin")
chk("L24 s7 tilt atan(2) = 63.4 deg", round(np.degrees(np.arctan2(E2, E1)), 1) == 63.4)

# slide 10/12: cos x + sin y, +z travel -> right; ahead x behind = z
Et = x - 1j * y          # cos(wt) x + sin(wt) y
chk("L24 s12 cos x + sin y toward +z: right-handed", hand(Et, z) == "R")
chk("L24 s12 ahead x behind = x cross y = +z", np.allclose(np.cross(x, y), z))
chk("L24 s12 toward -z: left-handed", hand(Et, -z) == "L")

# slide 11 picture: x right, y up; tip at -y moving +x -> rotation axis +z
chk("L24 s11 circle: r=-y, v=+x -> axis +z (RHCP for +z)", np.allclose(np.cross(-y, x), z))

# general: ahead x behind rule == recipe
for _ in range(20):
    A, B = rng.uniform(0.2, 2, 2)
    ph = rng.choice([np.pi / 2, -np.pi / 2])
    u = rng.choice([z, -z])
    Et = A * x + B * np.exp(1j * ph) * y
    ahead, behind = (y, x) if ph > 0 else (x, y)
    rule = "R" if np.dot(np.cross(ahead, behind), u) > 0 else "L"
    if hand(Et, u) != rule:
        chk("ahead x behind == recipe", False)
        break
else:
    chk("L24 s12 'ahead x behind' rule == site recipe (20 random cases)", True)

# slide 14: challenge question
w = 2 * np.pi * 1e8
opts = {"a": np.pi / 3, "b": -np.pi / 3, "c": np.pi / 6, "d": -np.pi / 6, "e": 5 * np.pi / 6}
res = {}
for k, phi in opts.items():
    Et = np.exp(1j * np.pi / 3) * x + np.exp(1j * phi) * y   # times e^{+j 2 pi z}: travel -z
    circ = np.isclose(abs(np.angle(np.exp(1j * (phi - np.pi / 3)))), np.pi / 2)
    res[k] = hand(Et, -z) if circ else "not circular"
chk("L24 s14 only (e) 5pi/6 gives right-circular toward -z",
    res["e"] == "R" and all(v != "R" for k, v in res.items() if k != "e"))
chk("L24 s14 y leads x by 90 deg at phi = 5pi/6", np.isclose(5 * np.pi / 6 - np.pi / 3, np.pi / 2))
chk("L24 s14 y x x = -z", np.allclose(np.cross(y, x), -z))
Et = np.exp(1j * np.pi / 3) * x + np.exp(1j * 5 * np.pi / 6) * y
chk("L24 s14 E(0) x E(T/4) = -z E0^2", np.allclose(np.cross(np.real(Et), -np.imag(Et)), -z))
# time-domain check: Lz = Ex dEy/dt - Ey dEx/dt < 0 (clockwise about +z = right-handed about -z)
t = np.linspace(0, 1e-8, 7)
Ex = np.cos(w * t + np.pi / 3)
Ey = np.cos(w * t + 5 * np.pi / 6)
dEx = -w * np.sin(w * t + np.pi / 3)
dEy = -w * np.sin(w * t + 5 * np.pi / 6)
chk("L24 s14 time-domain rotation about -z", np.all(Ex * dEy - Ey * dEx < 0))

# slide 15: E0 cos(wt + beta z) x (toward -z) = (E_R + E_L)/2
ER = x + 1j * y   # cos x + cos(.+pi/2) y = cos x - sin y
EL = x - 1j * y   # cos x + sin y
chk("L24 s15 x + jy toward -z is right-circular", hand(ER, -z) == "R")
chk("L24 s15 x - jy toward -z is left-circular", hand(EL, -z) == "L")
chk("L24 s15 (E_R + E_L)/2 = x", np.allclose((ER + EL) / 2, x))
th = 0.37
chk("L24 s15 time domain: Re{(x+jy)e^{jth}} = cos x - sin y",
    np.allclose(np.real(ER * np.exp(1j * th)), np.cos(th) * x - np.sin(th) * y))
chk("L24 s15 RHCP circle: r=+y, v=+x -> axis -z", np.allclose(np.cross(y, x), -z))
chk("L24 s15 LHCP circle: r=+x, v=+y -> axis +z", np.allclose(np.cross(x, y), z))

# slide 13 ink 'E1 != E2, phi != 0, +-90' : counterexamples
chk("L24 s13 E1 != E2 at phi = 90 deg is elliptical (not circular, not linear)",
    hand(1 * x + 2j * y, z) != "lin" and not np.isclose(1, 2))
chk("L24 s13 E1 = E2 at phi = 45 deg is elliptical", hand(x + np.exp(1j * np.pi / 4) * y, z) != "lin")
chk("L24 s13 E1 != E2 at phi = 180 deg is linear", hand(x - 2 * y, z) == "lin")
# ellipse at phi = 90, E1 != E2: axes along x and y (max |E| at t=0 along x, at T/4 along y)
Et = 1 * x + 2j * y
E0v, E4v = np.real(Et), -np.imag(Et)
chk("L24 s13 phi=90, unequal: semi-axes 1 along x, 2 along y",
    np.allclose(E0v, x) and np.allclose(np.abs(E4v), 2 * y))

print("ALL PASS" if ok_all else "SOME FAIL")
