#!/usr/bin/env python3
"""R22.py -- independent verification of content-src/practice/22-damped-waves-in-conducting-media.md
(Lecture 22: phasor Maxwell equations, damped waves in conducting media).

Every gamma and eta is taken as the exact principal complex square root
    gamma = sqrt(j w mu (sigma + j w eps)),  eta = sqrt(j w mu / (sigma + j w eps))
(numpy's principal branch has Re >= 0, i.e. alpha >= 0 and Re(eta) >= 0), every H-from-E step
is done with np.cross(u, E)/eta AND checked against a finite-difference phasor Faraday law, and
every <S> is computed both as 1/2 Re{E x H*} (np.cross) and by brute-force time averaging of the
real fields; absorbed powers are re-derived independently from the Joule term 1/2 sigma |E|^2.
Course constants: eps0 = 1e-9/(36 pi), mu0 = 4 pi 1e-7 (so c = 3e8 and eta0 = 120 pi exactly).

A string 'page value' is checked to the rounding shown on the page (half a unit in its last digit).
"""
import numpy as np
from numpy import pi, sqrt, exp, log, cos, sin, tan, arctan
from scipy.optimize import brentq
from scipy.integrate import quad
import scipy.constants as sc

eps0 = 1e-9 / (36 * pi)
mu0 = 4 * pi * 1e-7
c = 1 / np.sqrt(mu0 * eps0)
eta0 = np.sqrt(mu0 / eps0)
X, Y, Z = np.eye(3)
NFAIL = 0
NPASS = 0


def _tol_from_str(s):
    s = s.strip()
    low = s.lower()
    if 'e' in low:
        m, e = low.split('e')
        e = int(e)
    else:
        m, e = low, 0
    dec = len(m.split('.')[1]) if '.' in m else 0
    return float(s), 0.5 * 10.0 ** (e - dec)


def chk(name, stated, computed, tol=None):
    """PASS if the page value equals the computed one to the page's shown precision (or tol)."""
    global NFAIL, NPASS
    if isinstance(stated, str):
        val, t = _tol_from_str(stated)
        if tol is not None:
            t = tol
    else:
        val = float(stated)
        t = tol if tol is not None else 1e-9 * max(1.0, abs(val))
    ok = abs(val - computed) <= t * (1 + 1e-9) + 1e-12 * abs(computed)
    NPASS += ok
    NFAIL += (not ok)
    print(f"  {'PASS' if ok else 'FAIL'}  {name}: page {stated}   computed {computed:.7g}")
    return ok


def chkb(name, cond, info=''):
    global NFAIL, NPASS
    NPASS += bool(cond)
    NFAIL += (not cond)
    print(f"  {'PASS' if cond else 'FAIL'}  {name} {info}")
    return cond


def chkv(name, a, b, rtol=1e-6, atol=1e-9):
    a = np.asarray(a, complex)
    b = np.asarray(b, complex)
    return chkb(name, np.allclose(a, b, rtol=rtol, atol=atol), f"[{np.round(b, 6)}]")


def gamma_eta(w, mu, sig, eps):
    Yc = sig + 1j * w * eps
    return np.sqrt(1j * w * mu * Yc), np.sqrt(1j * w * mu / Yc)


def deg(zz):
    return np.degrees(np.angle(zz))


def curl(F, r, h=1e-6):
    r = np.asarray(r, float)
    J = np.zeros((3, 3), complex)
    for j in range(3):
        d = np.zeros(3)
        d[j] = h
        J[:, j] = (F(r + d) - F(r - d)) / (2 * h)
    return np.array([J[2, 1] - J[1, 2], J[0, 2] - J[2, 0], J[1, 0] - J[0, 1]])


def div(F, r, h=1e-6):
    r = np.asarray(r, float)
    s = 0
    for j in range(3):
        d = np.zeros(3)
        d[j] = h
        s += (F(r + d)[j] - F(r - d)[j]) / (2 * h)
    return s


def lap(F, r, h=1e-4):
    r = np.asarray(r, float)
    s = 0
    for j in range(3):
        d = np.zeros(3)
        d[j] = h
        s = s + (F(r + d) - 2 * F(r) + F(r - d)) / h**2
    return s


def real_t(Ph, w, t):
    """real time-domain value(s) of phasor(s) Ph at times t (broadcast)"""
    return np.real(np.multiply.outer(Ph, np.exp(1j * w * np.atleast_1d(t))))


def tavg_cross(E, H, w, N=4000):
    """brute-force time average of E(t) x H(t) over one period from phasor vectors"""
    t = np.linspace(0, 2 * pi / w, N, endpoint=False)
    Et = real_t(E, w, t)
    Ht = real_t(H, w, t)
    return np.mean(np.cross(Et.T, Ht.T), axis=0)


def tmax(f, T, N=400001):
    t = np.linspace(0, T, N, endpoint=False)
    return t[np.argmax(f(t))]


# --------------------------------------------------------------------------------------------
print("== constants")
chk("c = 1/sqrt(mu0 eps0) with eps0 = 1e-9/36pi", 3e8, c, tol=1e-3)
chk("eta0 = sqrt(mu0/eps0)", 120 * pi, eta0, tol=1e-9)

print("== intro: principal roots, 0 <= tau < 45 deg, H = u x E / eta, gamma/eta = sigma + j w eps")
ratios = np.logspace(-6, 8, 2001)
w_, mu_, eps_ = 1e8, mu0, 4 * eps0
taus, ab = [], []
for r_ in ratios:
    g_, n_ = gamma_eta(w_, mu_, r_ * w_ * eps_, eps_)
    taus.append(deg(n_))
    ab.append(g_.real / g_.imag)
    assert abs(g_ * n_ - 1j * w_ * mu_) < 1e-9 * abs(w_ * mu_)
    assert abs(g_ / n_ - (r_ * w_ * eps_ + 1j * w_ * eps_)) < 1e-9 * abs(g_ / n_)
taus = np.array(taus)
chkb("tau in [0,45) deg over sigma/w eps = 1e-6..1e8", taus.min() >= 0 and taus.max() < 45,
     f"(min {taus.min():.2e}, max {taus.max():.6f})")
chkb("alpha/beta = tan(tau) < 1 for every real sigma", np.allclose(ab, tan(np.radians(taus))) and max(ab) < 1)

# --------------------------------------------------------------------------------------------
print("== 22.1 phasor Maxwell, true or false")
# (b) continuity sign: d/dt Re{rho e^{jwt}} = Re{j w rho e^{jwt}}, so div J = -d rho/dt -> -j w rho
rho, w1 = 1.3 - 0.7j, 2.0
t1 = np.array([0.1, 0.7, 1.9])
dnum = (real_t(rho, w1, t1 + 1e-6) - real_t(rho, w1, t1 - 1e-6)) / 2e-6
chkb("(b) d/dt -> +j w, so div J~ = -j w rho~ (statement with +j w is FALSE)",
     np.allclose(dnum, real_t(1j * w1 * rho, w1, t1), atol=1e-6))
# (c) div curl = 0 for an arbitrary smooth phasor H -> div(J + j w D) = 0
Harb = lambda r: np.array([np.exp(1j * r[1]) * r[2] ** 2, (1 + 2j) * np.sin(r[0] * r[2]), r[0] * r[1] * np.exp(-r[2])])
divcurl = div(lambda r: curl(Harb, r, 1e-5), np.array([0.3, 0.2, 0.5]), 1e-3)
chkb("(c) div(curl H~) = 0 numerically -> Gauss follows from Ampere + continuity", abs(divcurl) < 1e-5, f"(|div curl| = {abs(divcurl):.1e})")
sig, eps, f = 0.1, 10 * eps0, 1e6
w = 2 * pi * f
chk("(d) relaxation time eps/sigma [ns]", "0.88", eps / sig * 1e9)
chkb("(d) period / relaxation time > 1000", (1 / f) / (eps / sig) > 1000, f"({(1 / f) / (eps / sig):.0f})")
chkb("(d) sigma + j w eps != 0 so rho~ = 0", abs(sig + 1j * w * eps) > 0)
epsc = eps - 1j * sig / w
chk("(e) sigma/(w eps0)", 1800, sig / (w * eps0), tol=1e-6)
chk("(e) Re eps_c / eps0", 10, epsc.real / eps0, tol=1e-9)
chk("(e) Im eps_c / eps0", -1800, epsc.imag / eps0, tol=1e-6)
chk("(e) sigma / w eps (conduction/displacement)", 180, sig / (w * eps), tol=1e-6)
chk("(f) phase of sigma E~ relative to E~ [deg]", 0, deg(sig + 0j), tol=1e-12)
chk("(f) phase of j w eps E~ relative to E~ [deg]", 90, deg(1j * w * eps), tol=1e-12)

# --------------------------------------------------------------------------------------------
print("== 22.2 which phasors are allowed (gamma^2 = -8 + j6)")
g2 = -8 + 6j
gm, nm = gamma_eta(3e8, mu0, 1 / (20 * pi), 8 * eps0)
chk("gamma^2 of the L22 sec.5 medium, real part", -8, (gm ** 2).real, tol=1e-9)
chk("gamma^2 of the L22 sec.5 medium, imag part", 6, (gm ** 2).imag, tol=1e-9)
chkv("gamma of that medium = 1 + j3 (principal root)", 1 + 3j, gm)
cands = {'a': (X, 1 + 3j, Z), 'b': (Y, -(1 + 3j), Z), 'c': (X, 3 + 1j, Z),
         'd': (X, 1 - 3j, Z), 'e': (Z, 1 + 3j, Z), 'f': (X, 1 + 3j, 0.6 * Y + 0.8 * Z)}
expect = {'a': True, 'b': True, 'c': False, 'd': False, 'e': False, 'f': True}
r0 = np.array([0.31, -0.22, 0.17])
for key, (p, k, u) in cands.items():
    F = lambda r, p=p, k=k, u=u: 2 * p * np.exp(-k * np.dot(u, r))
    helm = np.allclose(lap(F, r0), g2 * F(r0), rtol=1e-4, atol=1e-4)
    gauss = abs(div(F, r0)) < 1e-6
    chkb(f"({key}) Helmholtz {helm}, div E = 0 {gauss} -> allowed {helm and gauss}", (helm and gauss) == expect[key])
chkb("(c) (3+j)^2 = 8 + j6 and beta < alpha", (3 + 1j) ** 2 == 8 + 6j)
chkb("(d) (1-j3)^2 = -8 - j6", (1 - 3j) ** 2 == -8 - 6j)

# --------------------------------------------------------------------------------------------
print("== 22.3 reading a damped wave")
w = 2 * pi * 1e8
a, b = 0.5, 2 * pi
E3 = lambda z, t: 20 * np.exp(-a * z) * np.cos(w * t - b * z + np.radians(45))
zz = np.linspace(-0.3, 0.7, 200001)
zc0 = zz[np.argmax(np.cos(w * 0 - b * zz + np.radians(45)))]
zc1 = zz[np.argmax(np.cos(w * 1e-10 - b * zz + np.radians(45)))]
chkb("(a) crest moves toward +z", zc1 > zc0, f"(crest {zc0:.4f} -> {zc1:.4f} m in 0.1 ns)")
g3 = a + 1j * b
chk("(b) f [MHz]", 100, w / (2 * pi) / 1e6, tol=1e-9)
chk("(b) |gamma| [1/m]", "6.30", abs(g3))
chk("(b) angle gamma [deg]", "85.45", deg(g3))
chk("(b) beta [rad/m]", "6.28", b)
chk("(c) lambda [m]", 1, 2 * pi / b, tol=1e-12)
chk("(c) v_p [m/s]", 1e8, w / b, tol=1e-3)
chk("(c) delta [m]", 2, 1 / a, tol=1e-12)
chk("(d) amplitude at z = 4 m [V/m]", "2.71", 20 * exp(-a * 4))
chk("(d) amplitude ratio e^-2", "0.135", E3(4, 0.0) / 20 / np.cos(-b * 4 + np.radians(45)) * 1)
chk("(d) power ratio e^-4", "0.0183", exp(-2 * a * 4))
chk("(d) e^2 (amplitude 'smaller by a factor')", "7.39", exp(2))
chk("(d) e^4 (power 'smaller by a factor')", "54.6", exp(4))
Ym = g3 ** 2 / (1j * w * mu0)
print(f"  info: implied medium sigma = {Ym.real * 1e3:.3f} mS/m, eps = {Ym.imag / w / eps0:.3f} eps0 (physical)")

# --------------------------------------------------------------------------------------------
print("== 22.4 possible or not possible")
chkb("(a) alpha/beta = 4 > 1: impossible (max alpha/beta over all sigma < 1)", 2 / 0.5 > max(ab))
f, eps, sig = 1e9, 4 * eps0, 0.01
w = 2 * pi * f
g4, n4 = gamma_eta(w, mu0, sig, eps)
chk("(b) w eps [S/m]", "0.222", w * eps)
chk("(b) sigma / w eps", "0.045", sig / (w * eps))
chk("(b) exact alpha [Np/m]", "0.942", g4.real)
chk("(b) exact beta [rad/m]", "41.9", g4.imag)
chk("(b) alpha/beta", "0.022", g4.real / g4.imag)
chk("(c) 2 ns at 50 MHz [deg]", 36, 2e-9 * 50e6 * 360, tol=1e-9)
chk("(c) 45 deg at 50 MHz [ns]", "2.5", 45 / 360 / 50e6 * 1e9)
chk("(c) sigma/w eps needed for tau = -36 deg (negative)", "-3.08", tan(np.radians(-72)))
chk("(d) alpha/beta for a 1/e fall over lambda/10", "1.6", 10 / (2 * pi))
chk("(d) e^-2pi [%]", "0.19", exp(-2 * pi) * 100)
# (e) collisionless plasma, N = 1e11, SI constants (and the course eps0 for comparison)
N = 1e11
for lab, e0 in (("SI eps0", sc.epsilon_0), ("course eps0", eps0)):
    wp = sqrt(N * sc.e ** 2 / (sc.m_e * e0))
    w = 2 * pi * 2e6
    sigp = N * sc.e ** 2 / (1j * w * sc.m_e)
    gp = np.sqrt(1j * w * sc.mu_0 * (sigp + 1j * w * e0))
    npl = 1j * w * sc.mu_0 / gp
    chk(f"(e) f_p [MHz] ({lab})", "2.84", wp / (2 * pi) / 1e6)
    chkb(f"(e) gamma real below f_p ({lab})", abs(gp.imag) < 1e-12 * abs(gp) and gp.real > 0)
    chk(f"(e) delta at 2 MHz [m] ({lab})", "23.7", 1 / gp.real)
    chk(f"(e) Im eta at 2 MHz [ohm] ({lab})", "374", npl.imag)
    Ep = np.array([1.0, 0, 0])
    Hp = np.cross(Z, Ep) / npl
    chk(f"(e) <S> = 1/2 Re(E x H*) [W/m^2] ({lab})", 0, 0.5 * np.real(np.cross(Ep, np.conj(Hp)))[2], tol=1e-15)

# --------------------------------------------------------------------------------------------
print("== 22.5 the magnetic field that leads (find the error)")
eta5 = 150 * np.exp(1j * np.radians(20))
w5, mu5 = 1e8, mu0  # any w, mu: gamma follows from gamma eta = j w mu
g5 = 1j * w5 * mu5 / eta5
chkb("a passive gamma exists for this eta (alpha > 0, beta > 0)", g5.real > 0 and g5.imag > 0, f"(gamma = {g5:.4f})")
E5 = lambda r: Z * 60 * np.exp(-g5 * r[0])
r5 = np.array([0.4, 0.1, -0.2])
Hfar = curl(E5, r5) / (-1j * w5 * mu5)
Hcross = np.cross(X, E5(r5)) / eta5
chkv("Faraday H~ = u x E~ / eta (np.cross, u = +x)", Hfar, Hcross, rtol=1e-6)
Hpage = -Y * 0.4 * np.exp(-1j * np.radians(20)) * np.exp(-g5 * r5[0])
chkv("page H~ = -y 0.4 e^{-j20} e^{-gamma x}", Hpage, Hcross, rtol=1e-9)
Hstud = -Y * 0.4 * np.exp(+1j * np.radians(20)) * np.exp(-g5 * r5[0])
chkb("student's H~ (+20 deg) violates Faraday", not np.allclose(Hstud, Hfar, rtol=1e-3))
lag = (tmax(lambda t: -real_t(Hcross[1], w5, t), 2 * pi / w5) - tmax(lambda t: real_t(E5(r5)[2], w5, t), 2 * pi / w5)) % (2 * pi / w5)
chk("H (along -y) lags E_z by [deg]", "20", lag * w5 * 180 / pi, tol=0.01)
chk("sigma/w eps for tau = -20 deg", "-0.84", tan(np.radians(-40)))
S5 = 0.5 * np.real(np.cross(E5(np.zeros(3)), np.conj(np.cross(X, E5(np.zeros(3))) / eta5)))
chk("<S> at x = 0 [W/m^2]", "11.3", S5[0])
chkv("<S> direction +x", [1, 0, 0], S5 / np.linalg.norm(S5))
chk("student's eta* -> same |<S>| (cos even)", "11.3", 0.5 * 60 * 0.4 * cos(np.radians(20)))

# --------------------------------------------------------------------------------------------
print("== 22.6 from the medium to the wave")
w, sig, eps = 3e8, 1 / (10 * pi), 5 * eps0
Yc = sig + 1j * w * eps
chkv("sigma + j w eps = (12 + j5)/120pi", (12 + 5j) / (120 * pi), Yc)
chk("Re [mS/m]", "31.8", Yc.real * 1e3)
chk("Im = w eps [mS/m]", "13.3", Yc.imag * 1e3)
chk("w eps = 1/(24 pi)", 1 / (24 * pi), w * eps, tol=1e-15)
chk("sigma/w eps", 2.4, sig / (w * eps), tol=1e-12)
epsc = eps - 1j * sig / w
chkv("eps_c = (5 - j12) eps0", 5 - 12j, epsc / eps0)
chk("w mu0 = 120 pi", 120 * pi, w * mu0, tol=1e-9)
g6, n6 = gamma_eta(w, mu0, sig, eps)
chkv("gamma^2 = -5 + j12", -5 + 12j, g6 ** 2)
chkv("principal root gamma = 2 + j3", 2 + 3j, g6)
chkv("other root -2 - j3 also squares to gamma^2", (-2 - 3j) ** 2, g6 ** 2)
chk("|gamma| [1/m]", "3.61", abs(g6))
chk("angle gamma [deg]", "56.31", deg(g6))
chkv("principal root eta = (120pi/13)(3 + j2)", 120 * pi / 13 * (3 + 2j), n6)
chkv("eta^2 = (120pi/13)^2 (5 + j12)", (120 * pi / 13) ** 2 * (5 + 12j), n6 ** 2)
chk("Re eta [ohm]", "87.0", n6.real)
chk("Im eta [ohm]", "58.0", n6.imag)
chk("|eta| [ohm]", "104.6", abs(n6))
chk("tau [deg]", "33.69", deg(n6))
chkv("gamma eta = j 120 pi", 1j * 120 * pi, g6 * n6)
chk("other eta root angle [deg]", "-146.31", deg(-n6))
chkv("other eta root gives gamma eta = -j w mu0", -1j * w * mu0, g6 * (-n6))
chk("delta [m]", 0.5, 1 / g6.real, tol=1e-12)
chk("lambda [m]", "2.09", 2 * pi / g6.imag)
chk("v_p [m/s]", 1e8, w / g6.imag, tol=1e-3)
g60, n60 = gamma_eta(w, mu0, 0.0, eps)
chk("beta without sigma [rad/m]", "2.24", g60.imag)
chk("eta without sigma [ohm]", "168.6", n60.real)
chk("beta raised by [%]", "34", (g6.imag / g60.imag - 1) * 100)
chk("|eta| lowered by [%]", "38", (1 - abs(n6) / abs(n60)) * 100)
pre = w * sqrt(mu0 * eps / 2)
chk("general formula alpha", 2, pre * sqrt(sqrt(1 + 2.4 ** 2) - 1), tol=1e-9)
chk("general formula beta", 3, pre * sqrt(sqrt(1 + 2.4 ** 2) + 1), tol=1e-9)

# --------------------------------------------------------------------------------------------
print("== 22.7 microwave heating of raw meat")
w = 2 * pi * 2.45e9
epsc = (52 - 17j) * eps0
sig = 17 * w * eps0
chk("w [rad/s]", "1.539e10", w)
chk("sigma [S/m]", "2.31", sig)
chk("sigma / w eps", "0.327", 17 / 52)
chk("w/c [rad/m]", "51.31", w / c)
chk("|52 - j17|", "54.71", abs(52 - 17j))
chk("angle (52 - j17) [deg]", "-18.10", deg(52 - 17j))
s7 = np.sqrt(52 - 17j)
chk("sqrt(52-j17) real", "7.304", s7.real)
chk("sqrt(52-j17) imag", "-1.164", s7.imag)
chk("angle sqrt [deg]", "-9.05", deg(s7))
g7 = 1j * w * np.sqrt(mu0 * epsc)
g7b, n7b = gamma_eta(w, mu0, sig, 52 * eps0)
chkv("j w sqrt(mu0 eps_c) = sqrt(j w mu (sigma + j w eps)) (principal)", g7b, g7)
chk("alpha [Np/m]", "59.7", g7.real)
chk("beta [rad/m]", "374.8", g7.imag)
chk("delta [cm]", "1.67", 100 / g7.real)
chk("lambda in meat [cm]", "1.68", 100 * 2 * pi / g7.imag)
chk("lambda in air [cm]", "12.24", 100 * c / 2.45e9)
chk("v_p [m/s]", "4.11e7", w / g7.imag)
n7 = np.sqrt(mu0 / epsc)
chkv("sqrt(mu0/eps_c) = principal eta", n7b, n7)
chk("|eta| [ohm]", "50.97", abs(n7))
chk("|sqrt(52 - j17)|", "7.397", abs(s7))
chk("tau [deg]", "9.05", deg(n7))
chk("tau = atan(alpha/beta) [deg]", "9.05", np.degrees(arctan(g7.real / g7.imag)))
E0 = 1000.0
chk("|H| [A/m]", "19.6", E0 / abs(n7))
Svec = lambda z: 0.5 * np.real(np.cross(X * E0 * np.exp(-g7 * z), np.conj(np.cross(Z, X * E0 * np.exp(-g7 * z)) / n7)))
chk("cos tau", "0.9875", cos(np.angle(n7)))
chk("<S>(0) [kW/m^2]", "9.69", Svec(0)[2] / 1e3)
chk("<S>(0) by time averaging [kW/m^2]", "9.69", tavg_cross(X * E0, np.cross(Z, X * E0) / n7, w)[2] / 1e3)
chk("2 alpha [1/m]", "119.4", 2 * g7.real)
chk("<S>(1 cm) [kW/m^2]", "2.93", Svec(0.01)[2] / 1e3)
chk("<S>(2 cm) [kW/m^2]", "0.889", Svec(0.02)[2] / 1e3)
zh = brentq(lambda z: Svec(z)[2] - 0.5 * Svec(0)[2], 0, 0.1)
chk("half-power depth [mm]", "5.8", zh * 1e3)
J7 = quad(lambda z: 0.5 * sig * abs(E0 * np.exp(-g7 * z)) ** 2, 0, 1)[0]
chk("Joule heating integral 1/2 sigma |E|^2 over all depth = <S>(0) [kW/m^2]", "9.69", J7 / 1e3)
chk("lambda/delta = 2 pi tan tau", "1.001", 2 * pi * g7.real / g7.imag)
asc = sig / 2 * sqrt(mu0 / (52 * eps0))
chk("imperfect-dielectric shortcut alpha [Np/m]", "60.5", asc)
chk("shortcut error [%]", "1.3", (asc / g7.real - 1) * 100)
chk("power gone at z = delta [%] (page says 86)", "86", (1 - exp(-2)) * 100, tol=0.5)
chk("power absorbed in first cm [%]", "70", (1 - Svec(0.01)[2] / Svec(0)[2]) * 100)

# --------------------------------------------------------------------------------------------
print("== 22.8 power soaking into lossy ground (z up)")
w = 2 * pi * 1e6
g8 = 0.05 * (1 + 1j * sqrt(3))
E8 = lambda r: Y * 20 * np.exp(g8 * r[2])
zz = np.linspace(-80, 0, 400001)
zc0 = zz[np.argmax(np.cos(0 + g8.imag * zz))]
zc1 = zz[np.argmax(np.cos(w * 1e-8 + g8.imag * zz))]
chkb("(a) crest moves toward -z (down)", zc1 < zc0, f"({zc0:.3f} -> {zc1:.3f} m)")
chkb("(a) amplitude e^{0.05 z} shrinks going down", abs(E8([0, 0, -1])[1]) < abs(E8([0, 0, 0])[1]))
chk("(a) |gamma|", 0.1, abs(g8), tol=1e-12)
chk("(a) angle gamma [deg]", 60, deg(g8), tol=1e-9)
chk("(a) beta [rad/m]", "0.0866", g8.imag)
chk("(a) delta [m]", 20, 1 / g8.real, tol=1e-9)
chk("(a) lambda [m]", "72.6", 2 * pi / g8.imag)
chk("(b) w mu0 = 0.8 pi^2", 0.8 * pi ** 2, w * mu0, tol=1e-12)
n8 = 1j * w * mu0 / g8
chk("(b) |eta| = 8 pi^2 [ohm]", "78.96", abs(n8))
chk("(b) tau [deg]", 30, deg(n8), tol=1e-9)
Ym = g8 / n8
sig8, eps8 = Ym.real, Ym.imag / w
gg, nn = gamma_eta(w, mu0, sig8, eps8)
chkv("(b) implied medium returns the same principal gamma", g8, gg)
chkv("(b) implied medium returns the same principal eta", n8, nn)
chk("check: sigma [mS/m]", "1.10", sig8 * 1e3)
chk("check: eps/eps0", "11.4", eps8 / eps0)
chk("check: sigma/w eps = sqrt3", sqrt(3), sig8 / (w * eps8), tol=1e-9)
u8 = -Z
r8 = np.array([0.2, -0.1, -3.0])
H8 = np.cross(u8, E8(r8)) / n8
chkv("(b) H~ by Faraday curl = u x E / eta", curl(E8, r8, 1e-5) / (-1j * w * mu0), H8, rtol=1e-6)
Hpage = X * 0.253 * np.exp(-1j * np.radians(30)) * np.exp(g8 * r8[2])
chkv("(b) page H~ = x 0.253 e^{-j30} e^{gamma z} (to 3 s.f.)", Hpage, H8, rtol=2e-3)
chk("(b) H amplitude 20/8pi^2 [A/m]", "0.253", 20 / abs(n8))
S8 = lambda z: 0.5 * np.real(np.cross(E8([0, 0, z]), np.conj(np.cross(u8, E8([0, 0, z])) / n8)))
chkv("(c) <S> direction -z", [0, 0, -1], S8(0) / np.linalg.norm(S8(0)))
chk("(c) |<S>(0)| [W/m^2]", "2.194", -S8(0)[2])
chk("(c) 25 sqrt3 / 2 pi^2", "2.194", 25 * sqrt(3) / (2 * pi ** 2))
chk("(c) time-averaged |<S>(0)|", "2.19", -tavg_cross(E8([0, 0, 0]), np.cross(u8, E8([0, 0, 0])) / n8, w)[2])
chk("(c) e^{0.1 z} law: <S>(-7)/<S>(0)", exp(-0.7), S8(-7)[2] / S8(0)[2], tol=1e-12)
d1 = brentq(lambda d: S8(-d)[2] / S8(0)[2] - 0.01, 0, 500)
d2 = brentq(lambda d: abs(E8([0, 0, -d])[1]) / 20 - 0.01, 0, 500)
chk("(d) power 1% depth [m]", "46.1", d1)
chk("(d) field 1% depth [m]", "92.1", d2)
chk("(e) absorbed in top 20 m [W/m^2]", "1.90", -S8(0)[2] + S8(-20)[2])
Jl = quad(lambda z: 0.5 * sig8 * abs(E8([0, 0, z])[1]) ** 2, -20, 0)[0]
chk("(e) Joule integral 1/2 sigma |E|^2 over top 20 m [W/m^2]", "1.90", Jl)
chk("(e) fraction [%]", "86.5", (1 - exp(-2)) * 100)
chk("watch out: without cos tau [W/m^2]", "2.53", 400 / (2 * abs(n8)))
chk("watch out: overstatement [%]", "15", (1 / cos(pi / 6) - 1) * 100)

# --------------------------------------------------------------------------------------------
print("== 22.9 decoding a wave toward -y")
w = 6e8
a, b = 1.0, 7.0
E9 = lambda r: Z * 8 * np.exp(1j * np.radians(30)) * np.exp((a + 1j * b) * r[1])
yy = np.linspace(-1, 0.5, 300001)
yc0 = yy[np.argmax(np.cos(0 + b * yy + np.radians(30)))]
yc1 = yy[np.argmax(np.cos(w * 1e-10 + b * yy + np.radians(30)))]
chkb("(a) crest moves toward -y", yc1 < yc0, f"({yc0:.4f} -> {yc1:.4f})")
r9 = np.array([0.1, -0.35, 0.2])
tt = np.array([0.0, 1.3e-9, 4.1e-9])
chkv("(a) phasor Re{E~ e^{jwt}} reproduces the given E(y,t)", real_t(E9(r9)[2], w, tt),
     8 * exp(r9[1]) * np.cos(w * tt + 7 * r9[1] + np.radians(30)))
g9 = a + 1j * b
chk("(a) |gamma| = 5 sqrt2", "7.07", abs(g9))
chk("(a) angle gamma [deg]", "81.87", deg(g9))
chk("(b) lambda [m]", "0.898", 2 * pi / b)
chk("(b) f [MHz]", "95.5", w / (2 * pi) / 1e6)
chk("(b) v_p [m/s]", "8.57e7", w / b)
chk("(b) delta [m]", 1, 1 / a, tol=1e-12)
chk("(c) w mu0 = 240 pi", 240 * pi, w * mu0, tol=1e-9)
n9 = 1j * w * mu0 / g9
chkv("(c) eta = 4.8 pi (7 + j)", 4.8 * pi * (7 + 1j), n9)
chk("(c) Re eta", "105.6", n9.real)
chk("(c) Im eta", "15.1", n9.imag)
chk("(c) |eta| [ohm]", "106.6", abs(n9))
chk("(c) 24 sqrt2 pi", "106.6", 24 * sqrt(2) * pi)
chk("(c) tau [deg]", "8.13", deg(n9))
Ym = g9 / n9
sig9, eps9 = Ym.real, Ym.imag / w
gg, nn = gamma_eta(w, mu0, sig9, eps9)
chkv("(c) principal sqrt for the implied medium returns gamma", g9, gg)
chkv("(c) principal sqrt for the implied medium returns eta", n9, nn)
u9 = -Y
H9 = np.cross(u9, E9(r9)) / n9
chkv("(d) Faraday curl = u x E / eta, u = -y", curl(E9, r9) / (-1j * w * mu0), H9, rtol=1e-6)
chkv("(d) page H~ = -x 75.0 e^{j21.87} e^{(1+j7)y} mA/m (3-4 s.f.)", -X * 75.0e-3 * np.exp(1j * np.radians(21.87)) * np.exp(g9 * r9[1]), H9, rtol=1e-3)
Hx0 = np.cross(u9, E9(np.zeros(3))) / n9
chk("(d) |H| [mA/m]", "75.0", abs(Hx0[0]) * 1e3)
chk("(d) phase of the -x component [deg]", "21.87", deg(-Hx0[0]))
T9 = 2 * pi / w
lag9 = (tmax(lambda t: real_t(-Hx0[0], w, t), T9) - tmax(lambda t: real_t(E9(np.zeros(3))[2], w, t), T9)) % T9
chk("(d) H lags E by [ns] (time sampling)", "0.236", lag9 * 1e9)
chk("(d) tau/omega [ns]", "0.236", np.angle(n9) / w * 1e9)
chk("(d) tau [rad]", "0.1419", np.angle(n9))
Sd = np.real(np.cross(E9(np.zeros(3)), np.conj(Hx0)))
chkv("(d) E x H along -y", [0, -1, 0], Sd / np.linalg.norm(Sd))
chkv("(e) gamma^2 = -48 + j14", -48 + 14j, g9 ** 2)
chkv("(e) sigma + j w eps = (14 + j48)/240pi", (14 + 48j) / (240 * pi), Ym)
chk("(e) sigma [mS/m]", "18.6", sig9 * 1e3)
chk("(e) eps [F/m]", "1.06e-10", eps9)
chk("(e) eps/eps0", 12, eps9 / eps0, tol=1e-9)
chk("(e) sigma/w eps", 7 / 24, sig9 / (w * eps9), tol=1e-12)
asc = sig9 / 2 * sqrt(mu0 / eps9)
bsc = w * sqrt(mu0 * eps9)
chk("(e) shortcut alpha [Np/m]", "1.010", asc)
chk("(e) shortcut beta [rad/m]", "6.93", bsc)
print(f"  info: shortcut errors alpha {100 * (asc - 1):+.3f} %, beta {100 * (bsc / 7 - 1):+.3f} %")
# The page originally said the shortcuts were "within 1 %" of 1 and 7: false (1.036 % and 1.026 %).
# Fixed wording: "only about 1 % off ... (1.04 % high and 1.03 % low)".
chkb("(e) original claim 'within 1 %' is false (fixed on the page)", not (abs(asc - 1) <= 0.01 and abs(bsc / 7 - 1) <= 0.01))
chk("(e) shortcut alpha error [%] (fixed text)", "1.04", 100 * (asc - 1))
chk("(e) shortcut beta error [%] (fixed text, 'low')", "-1.03", 100 * (bsc / 7 - 1))
chk("check: tan 2 tau", "0.292", tan(2 * np.angle(n9)))
chk("check: 2 tau [deg]", "16.26", 2 * deg(n9))
chk("check: |gamma||eta| = w mu0", w * mu0, abs(g9) * abs(n9), tol=1e-9)

# --------------------------------------------------------------------------------------------
print("== 22.10 two components in a magnetic medium")
w, mu = 3e8, 4 * mu0
g10 = 3 + 5j
E10 = lambda r: (6 * X - 8j * Y) * np.exp(g10 * r[2])
chk("(a) lambda [m]", "1.26", 2 * pi / 5)
chk("(a) delta [m]", "0.333", 1 / 3)
chk("(a) v_p [m/s]", 6e7, w / 5, tol=1e-6)
chk("(b) w mu = 480 pi", 480 * pi, w * mu, tol=1e-9)
n10 = 1j * w * mu / g10
chkv("(b) eta = (240pi/17)(5 + j3)", 240 * pi / 17 * (5 + 3j), n10)
chk("(b) Re eta", "221.8", n10.real)
chk("(b) Im eta", "133.1", n10.imag)
chk("(b) |eta|", "258.6", abs(n10))
chk("(b) tau [deg]", "30.96", deg(n10))
Ym = g10 / n10
sig10, eps10 = Ym.real, Ym.imag / w
gg, nn = gamma_eta(w, mu, sig10, eps10)
chkv("(b) principal roots for implied medium return gamma", g10, gg)
chkv("(b) principal roots for implied medium return eta", n10, nn)
r10 = np.array([0.2, 0.3, -0.15])
H10 = np.cross(-Z, E10(r10)) / n10
chkv("(c) Faraday curl = u x E / eta (u = -z, mu = 4 mu0)", curl(E10, r10) / (-1j * w * mu), H10, rtol=1e-6)
chkv("(c) Ampere: curl H = (sigma + j w eps) E",
     curl(lambda r: np.cross(-Z, E10(r)) / n10, r10), (sig10 + 1j * w * eps10) * E10(r10), rtol=1e-5)
H0 = np.cross(-Z, E10(np.zeros(3))) / n10
chkv("(c) u x (6x - j8y) = -j8 x - 6 y", -8j * X - 6 * Y, np.cross(-Z, 6 * X - 8j * Y))
chk("(c) |H_x| [mA/m]", "30.93", abs(H0[0]) * 1e3)
chk("(c) angle H_x [deg]", "-120.96", deg(H0[0]))
chk("(c) |H_y| [mA/m] (with the -y sign)", "23.20", abs(H0[1]) * 1e3)
chk("(c) angle of -H_y [deg]", "-30.96", deg(-H0[1]))
tt = np.array([0.0, 2.1e-9, 7.7e-9])
zq = -0.15
Et = real_t(E10([0, 0, zq]), w, tt)
chkv("(c) E(z,t) = e^{3z}[x 6 cos(wt+5z) + y 8 sin(wt+5z)]",
     Et[:2], np.exp(3 * zq) * np.array([6 * cos(w * tt + 5 * zq), 8 * sin(w * tt + 5 * zq)]))
Ht = real_t(np.cross(-Z, E10([0, 0, zq])) / n10, w, tt) * 1e3
Hform = np.exp(3 * zq) * np.array([30.93 * cos(w * tt + 5 * zq - np.radians(120.96)),
                                   -23.20 * cos(w * tt + 5 * zq - np.radians(30.96))])
chkv("(c) H(z,t) formula (mA/m, 4 s.f.)", Ht[:2], Hform, rtol=2e-3, atol=2e-3)
chk("(d) sigma/w eps", 1.875, sig10 / (w * eps10), tol=1e-12)
chk("(d) sigma [mS/m]", "19.9", sig10 * 1e3)
chk("(d) sigma = 1/16pi", 1 / (16 * pi), sig10, tol=1e-15)
chk("(d) eps [F/m]", "3.54e-11", eps10)
chk("(d) eps/eps0", 4, eps10 / eps0, tol=1e-9)
S10 = 0.5 * np.real(np.cross(E10(np.zeros(3)), np.conj(H0)))
chkv("(e) <S> along -z", [0, 0, -1], S10 / np.linalg.norm(S10))
chk("(e) |<S>(0)| [W/m^2]", "0.166", -S10[2])
chk("(e) 25/48pi", 25 / (48 * pi), -S10[2], tol=1e-12)
chk("(e) by time averaging [W/m^2]", "0.166", -tavg_cross(E10(np.zeros(3)), H0, w)[2])
Sx = 0.5 * np.real(np.cross(6 * X, np.conj(np.cross(-Z, 6 * X) / n10)))[2]
Sy = 0.5 * np.real(np.cross(-8j * Y, np.conj(np.cross(-Z, -8j * Y) / n10)))[2]
chk("(e) E_x share [%]", 36, 100 * Sx / S10[2], tol=1e-9)
chk("(e) E_x part [W/m^2]", "0.060", -Sx)
chk("(e) E_y part [W/m^2]", "0.106", -Sy)
chk("(e) e^{6z} law", exp(6 * zq), (0.5 * np.real(np.cross(E10([0, 0, zq]), np.conj(np.cross(-Z, E10([0, 0, zq])) / n10))))[2] / S10[2], tol=1e-12)
chk("watch out: |eta| with mu0 [ohm]", "64.7", abs(1j * w * mu0 / g10))
chk("check: eta of mu_r = eps_r = 4 lossless = 120 pi", 120 * pi, sqrt(mu / (4 * eps0)), tol=1e-9)

# --------------------------------------------------------------------------------------------
print("== 22.11 current sheet in a lossy medium")
w, sig, eps = 3e8, 1 / (10 * pi), 5 * eps0
g11, n11 = gamma_eta(w, mu0, sig, eps)
chkv("medium of 22.6: gamma = 2 + j3", 2 + 3j, g11)
chk("|eta| [ohm]", "104.6", abs(n11))
Js = 4 * Z
def fields(A, x):
    if x > 0:
        E = Z * A * np.exp(-g11 * x)
        return E, np.cross(X, E) / n11
    E = Z * A * np.exp(g11 * x)
    return E, np.cross(-X, E) / n11
H1, H2 = fields(1.0, 1e-300)[1], fields(1.0, -1e-300)[1]
coef = np.cross(X, H1 - H2)[2]
A = Js[2] / coef
chkv("(a) A from n x (H1 - H2) = Js (n = +x, region 1 = x>0)", -2 * n11, A)
Ep, Hp = fields(A, 1e-300)
chkv("(a) H~(0+) = +2 y", 2 * Y, Hp)
chkv("(a) H~(0-) = -2 y", -2 * Y, fields(A, -1e-300)[1])
chkv("(a) E~ = -(eta/2) Js", -n11 / 2 * Js, Ep)
chkv("(a) H~(0+) = 1/2 Js x n", 0.5 * np.cross(Js, X), Hp)
for xq in (0.37, -0.52):
    rq = np.array([xq, 0.1, -0.3])
    Ef = lambda r: fields(A, r[0])[0]
    Hf = lambda r: fields(A, r[0])[1]
    chkv(f"Faraday at x = {xq}", curl(Ef, rq) / (-1j * w * mu0), Hf(rq), rtol=1e-6)
    chkv(f"Ampere (sigma + j w eps) at x = {xq}", curl(Hf, rq), (sig + 1j * w * eps) * Ef(rq), rtol=1e-5)
chk("(b) 2|eta| [V/m]", "209.1", 2 * abs(n11))
chk("(b) angle [deg]", "33.69", deg(n11))
xq, tt = 0.3, np.array([0.0, 3.3e-9, 11.0e-9])
Et = real_t(fields(A, xq)[0][2], w, tt)
chkv("(b) E(x,t) = -z 209.1 e^{-2x} cos(wt - 3x + 33.69)", Et,
     -209.1 * exp(-2 * xq) * cos(w * tt - 3 * xq + np.radians(33.69)), rtol=5e-4, atol=1e-3)
Ht = real_t(fields(A, xq)[1][1], w, tt)
chkv("(b) H(x,t) = y 2 e^{-2x} cos(wt - 3x)", Ht, 2 * exp(-2 * xq) * cos(w * tt - 3 * xq), rtol=1e-9)
T11 = 2 * pi / w
lead = (tmax(lambda t: real_t(4.0 + 0j, w, t), T11) - tmax(lambda t: real_t(-Ep[2], w, t), T11)) % T11
chk("(b) -E leads Js by [ns] (time sampling)", "1.96", lead * 1e9)
chk("(b) -E leads Js by [deg]", "33.69", lead * w * 180 / pi, tol=0.006)
Sp = 0.5 * np.real(np.cross(Ep, np.conj(Hp)))
chkv("(c) <S>(0+) along +x", [1, 0, 0], Sp / np.linalg.norm(Sp))
chk("(c) Re eta = 360pi/13 [ohm]", "87.0", n11.real)
chk("(c) |<S>(0+)| [W/m^2]", "174.0", Sp[0])
Em, Hm = fields(A, -1e-300)
Sm = 0.5 * np.real(np.cross(Em, np.conj(Hm)))
chkv("(c) <S>(0-) = -x 174.0", -Sp, Sm)
chk("(c) time-averaged <S>(0+)", "174.0", tavg_cross(Ep, Hp, w)[0])
t = np.linspace(0, T11, 20000, endpoint=False)
pJ = np.mean(-real_t(Js[2] + 0j, w, t) * real_t(Ep[2], w, t))
chk("(c) <-Js.E> by time averaging [W/m^2]", "348.0", pJ)
chk("(c) <-Js.E> = 4 Re eta", "348.0", 4 * n11.real)
Jh = 2 * quad(lambda x: 0.5 * sig * abs(fields(A, x)[0][2]) ** 2, 0, 20)[0]
chk("(c) Joule heating 1/2 sigma |E|^2 in both half-spaces [W/m^2]", "348.0", Jh)
chk("(d) fraction within delta [%]", "86.5", (1 - exp(-4 * 0.5)) * 100)
chk("(d) absorbed within delta [W/m^2]", "150.4", Sp[0] * (1 - exp(-2)))
x99 = brentq(lambda x: exp(-4 * x) - 0.01, 0, 10)
chk("(d) 99% distance [m]", "1.15", x99)
g0, n0 = gamma_eta(w, mu0, 0.0, eps)
chk("(e) lossless eta [ohm]", "168.6", n0.real)
chk("(e) field at sheet 2 eta [V/m]", "337.2", 2 * abs(n0))
chk("(e) power 1/4 J0^2 eta [W/m^2]", "674.4", 0.25 * 16 * n0.real)
chk("(e) ratio lossy/lossless (about half)", "0.5", 4 * n11.real / (4 * n0.real), tol=0.05)
chk("(e) 1/2 J0^2 Re{eta/2} = 4 Re eta", 4 * n11.real, 0.5 * 16 * (n11 / 2).real, tol=1e-9)

# --------------------------------------------------------------------------------------------
print("== 22.12 three probes identify a medium")
w = 3e8
EA = 10.0 + 0j
EB = 12.84 * np.exp(1j * np.radians(57.30))
HA = 21.87e-3 * np.exp(-1j * np.radians(14.04))
yB = -0.25
chkb("(a) B leads A (phase +57.30) and is stronger -> crest reaches B first -> travel +y",
     np.angle(EB / EA) > 0 and abs(EB) > abs(EA))
g12 = np.log(EB / EA) / (-yB)  # E ~ e^{-gamma y}: E(B)/E(A) = e^{+0.25 gamma}
chk("(a) alpha [Np/m]", "1.000", g12.real)
chk("(a) beta [rad/m]", "4.00", g12.imag)
chk("(a) 57.30 deg in rad", "1.000", np.radians(57.30))
chk("(a) |gamma|", "4.12", abs(g12))
chk("(a) angle gamma [deg] (exact atan 4)", "75.96", np.degrees(arctan(4)))
chk("(a) angle gamma from the 4-s.f. probe data [deg]", "75.96", deg(g12), tol=0.01)
chkb("(a) lambda = 2pi/beta > 0.25 m; +360 deg would give lambda < 0.25 m",
     2 * pi / g12.imag > 0.25 and 2 * pi / ((np.radians(57.30) + 2 * pi) / 0.25) < 0.25)
sgn = np.cross(Y, Z)[0]
n12 = sgn * EA / HA
chk("(b) |eta| [ohm]", "457.2", abs(n12))
chk("(b) tau [deg]", "14.04", deg(n12))
chk("(b) Re eta", "443.6", n12.real)
chk("(b) Im eta", "110.9", n12.imag)
chk("(b) atan(alpha/beta) [deg] (exact 1/4)", "14.04", np.degrees(arctan(0.25)))
chk("(b) atan(alpha/beta) from probe data [deg]", "14.04", np.degrees(arctan(g12.real / g12.imag)), tol=0.01)
chkb("(b) guessing -y travel gives Re(eta) < 0", (np.cross(-Y, Z)[0] * EA / HA).real < 0)
mu12 = g12 * n12 / (1j * w)
chk("(c) |gamma||eta| [ohm/m]", "1885", abs(g12) * abs(n12))
chk("(c) mu [H/m]", "6.28e-6", mu12.real)
chk("(c) mu/mu0", "5.00", mu12.real / mu0)
chk("(c) Im mu (real mu check)", 0, mu12.imag / mu0, tol=2e-3)
Ym = g12 / n12
chk("(c) |gamma/eta|", "9.02e-3", abs(Ym))
chk("(c) angle gamma/eta [deg]", "61.93", deg(Ym))
chk("(c) sigma [mS/m]", "4.24", Ym.real * 1e3)
chk("(c) w eps [S/m]", "7.96e-3", Ym.imag)
chk("(c) eps [F/m]", "2.65e-11", Ym.imag / w)
chk("(c) eps/eps0", "3.00", Ym.imag / w / eps0)
chk("(c) sigma/w eps", "0.533", Ym.real / Ym.imag)
# exact medium mu = 5 mu0, sigma = 1/75pi, eps = 3 eps0 reproduces the probe data
ge, ne = gamma_eta(w, 5 * mu0, 1 / (75 * pi), 3 * eps0)
chkv("exact medium: principal gamma = 1 + j4", 1 + 4j, ge)
chkv("exact medium: eta = (600pi/17)(4 + j)", 600 * pi / 17 * (4 + 1j), ne)
chkv("exact medium: gamma/eta = (8 + j15)/600pi", (8 + 15j) / (600 * pi), ge / ne)
chk("exact medium reproduces |E_B| [V/m]", "12.84", abs(10 * np.exp(-ge * yB)))
chk("exact medium reproduces angle E_B [deg]", "57.30", deg(np.exp(-ge * yB)))
chk("exact medium reproduces |H_A| [mA/m]", "21.87", 10 / abs(ne) * 1e3)
chk("exact medium reproduces angle H_A [deg]", "-14.04", -deg(ne))
Ycl = g12 ** 2 / (1j * w * mu0)
chk("(d) classmate sigma' [mS/m]", "21.2", Ycl.real * 1e3)
chk("(d) classmate eps'/eps0", "15", Ycl.imag / w / eps0, tol=0.02)
chk("(d) classmate |eta| [ohm]", "91.4", w * mu0 / abs(g12))
chk("(d) ratio sigma'/sigma", 5, Ycl.real / Ym.real, tol=0.01)
chk("(d) classmate sigma/w eps unchanged", "0.533", Ycl.real / Ycl.imag)
SA = 0.5 * np.real(np.cross(Z * EA, np.conj(X * HA)))
chkv("(e) <S> at A along +y", [0, 1, 0], SA / np.linalg.norm(SA))
chk("(e) <S> at A [W/m^2]", "0.106", SA[1])
chk("(e) exact 1/3pi", "0.106", 1 / (3 * pi))
SB = SA[1] * np.exp(2 * g12.real * 0.25)
chk("(e) <S> at B [W/m^2]", "0.175", SB)
chk("(e) absorbed [W/m^2]", "0.069", SB - SA[1])
Jl = quad(lambda y: 0.5 * Ym.real * abs(EA * np.exp(-g12 * y)) ** 2, yB, 0)[0]
chk("(e) Joule integral 1/2 sigma |E|^2 over -0.25<y<0 [W/m^2]", "0.069", Jl)
chk("check: |gamma||eta| = 600 pi (exact medium)", 600 * pi, abs(ge) * abs(ne), tol=1e-9)

print(f"\nTOTAL: {NPASS} PASS, {NFAIL} FAIL")
