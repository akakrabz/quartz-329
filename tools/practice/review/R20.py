#!/usr/bin/env python3
"""R20.py -- independent reviewer check of content-src/practice/20-poynting-theorem-and-power.md

Every final number, sign and direction on the page is recomputed from the problem data, by a
route independent of the page's algebra where possible: finite-difference Maxwell / divergence /
curl checks, np.cross for every direction, sampled time averages over a period, scipy quadrature,
an ODE solve, root finding, and a sphere-flux quadrature for the static charge + magnet case.
`rchk` checks that a page value is the correct rounding of the computed value (to the digits shown).
"""
import numpy as np
from scipy import integrate, optimize

NP = NF = 0


def rep(ok, label, msg):
    global NP, NF
    NP += bool(ok)
    NF += (not ok)
    print(("PASS " if ok else "FAIL ") + label + ": " + msg)


def chk(label, got, page, rtol=2e-3, atol=1e-12):
    g = np.asarray(got, float)
    p = np.asarray(page, float)
    rep(np.allclose(g, p, rtol=rtol, atol=atol), label,
        f"computed {np.array2string(g, precision=6)}  page {np.array2string(p, precision=6)}")


def rchk(label, got, page_str, unit=None):
    """page_str must be the correct rounding of got to the digits shown (or within +-unit/2)."""
    page = float(page_str)
    if unit is None:
        mant, _, ex = page_str.lower().partition("e")
        dec = len(mant.split(".")[1]) if "." in mant else 0
        unit = 10.0 ** ((int(ex) if ex else 0) - dec)
    rep(abs(got - page) <= 0.5 * unit * 1.02 + 1e-12 * abs(page), label,
        f"computed {got:.6g}  page {page_str}")


def tf(label, val, page):
    rep(bool(val) == page, label, f"computed {'T' if val else 'F'}  page {'T' if page else 'F'}")


def section(s):
    print("\n=== " + s + " ===")


def tavg(fun, T, N=2048, t0=0.0):
    """mean over one period by midpoint sampling (exact for trig polynomials of degree < N)"""
    t = t0 + (np.arange(N) + 0.5) * T / N
    return np.mean(np.array([fun(tt) for tt in t]), axis=0)


def travel_dir(comp, axis, lam, T):
    """track a crest of comp(s, t) along the coordinate s for T/50: returns +-axis"""
    s = np.linspace(-lam / 4, lam / 4, 40001)
    s0 = s[np.argmax(comp(s, 0.0))]
    s1 = s[np.argmax(comp(s, T / 50))]
    return np.sign(s1 - s0) * axis


X, Y, Z = np.eye(3)
c = 3e8
eta0 = 120 * np.pi
mu0 = 4e-7 * np.pi
eps0x = 1e-9 / (36 * np.pi)          # exam epsilon_0: 1/sqrt(mu0 eps0x) = 3e8, sqrt(mu0/eps0x) = 120 pi
print(f"constants: 1/sqrt(mu0*eps0x) = {1/np.sqrt(mu0*eps0x):.6g}, sqrt(mu0/eps0x)/pi = {np.sqrt(mu0/eps0x)/np.pi:.6g}")

# ---------------------------------------------------------------------------------------------
section("20.1 Reading the energy ledger (true/false)")
# (a) dimensions as exponent vectors [kg, m, s, A]
V_, A_, m_, s_ = np.array([1, 2, -3, -1]), np.array([0, 0, 0, 1]), np.array([0, 1, 0, 0]), np.array([0, 0, 1, 0])
J_, W_ = np.array([1, 2, -2, 0]), np.array([1, 2, -3, 0])
E_d, H_d, w_d, Jc_d = V_ - m_, A_ - m_, J_ - 3 * m_, A_ - 2 * m_
terms = [w_d - s_, (E_d + H_d) - m_, Jc_d + E_d]
ok_a = all(np.array_equal(q, W_ - 3 * m_) for q in terms) and np.array_equal(E_d + H_d, W_ - 2 * m_)
tf("20.1(a) every term W/m^3, S in W/m^2", ok_a, True)
# (b) a radiating sheet in vacuum, |Js| = 1 A/m: E on the sheet = -(eta0/2) Js
JsE = np.dot(1.0 * X, -(eta0 / 2) * 1.0 * X)
rchk("20.1(b) Js.E for 1 A/m in vacuum [W/m^2] (page 'about -188')", JsE, "-188", unit=2)
tf("20.1(b) 'J.E can never be negative'", JsE >= 0, False)
# (c) battery: - terminal at x=0, + at x=L; terminal-charge field from + to - (-x); current from - to + (+x)
Lb, Ab, Vt, Ib = 0.05, 1e-4, 1.5, 1.0
Eb, Jb = -Vt / Lb * X, Ib / Ab * X
tf("20.1(c) J.E < 0 inside a battery", np.dot(Jb, Eb) < 0, True)
chk("20.1(c) -int J.E dV, 1.5 V cell at 1 A [W]", -np.dot(Jb, Eb) * Ab * Lb, 1.5)


# (d),(e): 1-D fields from a potential psi so that Faraday holds identically; J defined by Ampere-Maxwell
def ledger(eps_fun, psi, mu=1.3, z=0.37, t=0.81, h=1e-3, hh=1e-5):
    Ex = lambda z, t: -(psi(z, t + hh) - psi(z, t - hh)) / (2 * hh)
    Hy = lambda z, t: (psi(z + hh, t) - psi(z - hh, t)) / (2 * hh) / mu
    Dx = lambda z, t: eps_fun(z, t) * Ex(z, t)
    Jx = -(Hy(z + h, t) - Hy(z - h, t)) / (2 * h) - (Dx(z, t + h) - Dx(z, t - h)) / (2 * h)
    w = lambda z, t: 0.5 * eps_fun(z, t) * Ex(z, t) ** 2 + 0.5 * mu * Hy(z, t) ** 2
    S = lambda z, t: Ex(z, t) * Hy(z, t)
    dwdt = (w(z, t + h) - w(z, t - h)) / (2 * h)
    dSdz = (S(z + h, t) - S(z - h, t)) / (2 * h)
    deps = (eps_fun(z, t + h) - eps_fun(z, t - h)) / (2 * h)
    EdD = Ex(z, t) * (Dx(z, t + h) - Dx(z, t - h)) / (2 * h)
    dwe = (0.5 * eps_fun(z, t + h) * Ex(z, t + h) ** 2 - 0.5 * eps_fun(z, t - h) * Ex(z, t - h) ** 2) / (2 * h)
    return dict(res=dwdt + dSdz + Jx * Ex(z, t), scale=abs(dwdt) + abs(dSdz) + abs(Jx * Ex(z, t)),
                Jx=Jx, extra=EdD - dwe, half_E2_deps=0.5 * Ex(z, t) ** 2 * deps)


psi_gen = lambda z, t: np.sin(1.3 * z - 0.7 * t) * np.exp(-0.1 * z * z) + 0.4 * np.cos(0.9 * z + 1.1 * t) * np.cos(0.3 * t)
vw = 1 / np.sqrt(1.3 * 2.0)
L0 = ledger(lambda z, t: 2.0 + 0 * z, lambda z, t: np.exp(-(z - vw * t) ** 2) * np.cos(3 * (z - vw * t)), h=3e-4)
print(f"      plane wave: J from Ampere-Maxwell {L0['Jx']:.1e} (FD truncation), residual {L0['res']:.1e}, scale {L0['scale']:.3f}")
tf("20.1(d) J = 0 plane wave: dw/dt + div S = 0 (continuity form)",
   abs(L0['Jx']) < 1e-4 and abs(L0['res']) < 1e-5 * L0['scale'], True)
for z0, t0 in [(0.37, 0.81), (-1.2, 2.3)]:
    Lg = ledger(lambda z, t: 2.0 + 0.8 * np.tanh(3 * z) + 0.3 * np.sin(2 * z), psi_gen, z=z0, t=t0)
    print(f"      graded eps(z): residual {Lg['res']:.2e}, scale {Lg['scale']:.3f}")
    tf(f"20.1(e) theorem fails for graded eps(z)  [z={z0}, t={t0}]", abs(Lg['res']) > 1e-5 * Lg['scale'], False)
Lt = ledger(lambda z, t: 2.0 + 0.5 * np.sin(1.7 * t), psi_gen)
chk("20.1(e) eps(t): extra term in E.dD/dt equals +1/2 E^2 d(eps)/dt", Lt['extra'], Lt['half_E2_deps'], rtol=1e-4)
print(f"      eps(t): ledger residual {Lt['res']:.4e} = -1/2 E^2 deps/dt = {-Lt['half_E2_deps']:.4e}")

# (f) point charge + magnetic dipole: closed-surface flux of E x H, sphere enclosing both, off-centre
rq, rm, mvec = np.array([-0.5, 0.0, 0.1]), np.array([0.5, 0.2, 0.0]), np.array([0.3, 0.4, 1.0])


def Ef(r):
    R = r - rq
    return R / np.linalg.norm(R, axis=-1, keepdims=True) ** 3


def Hf(r):
    R = r - rm
    Rn = np.linalg.norm(R, axis=-1, keepdims=True)
    Rh = R / Rn
    return (3 * np.sum(mvec * Rh, axis=-1, keepdims=True) * Rh - mvec) / (4 * np.pi * Rn ** 3)


uu, wu = np.polynomial.legendre.leggauss(120)
ph = (np.arange(240) + 0.5) * 2 * np.pi / 240
U, P = np.meshgrid(uu, ph, indexing="ij")
WU = np.meshgrid(wu, ph, indexing="ij")[0]
nh = np.stack([np.sqrt(1 - U ** 2) * np.cos(P), np.sqrt(1 - U ** 2) * np.sin(P), U], -1)
cen, R0 = np.array([0.2, -0.1, 0.3]), 2.0
pts = cen + R0 * nh
Sn = np.sum(np.cross(Ef(pts), Hf(pts)) * nh, -1)
flux = np.sum(WU * Sn) * (2 * np.pi / 240) * R0 ** 2
absf = np.sum(WU * np.abs(Sn)) * (2 * np.pi / 240) * R0 ** 2
print(f"      static charge + magnet: net flux {flux:.2e}, integral of |S.n| {absf:.4f}")
tf("20.1(f) E x H != 0 around the pair", absf > 1e-3, True)
tf("20.1(f) 'energy flows steadily out of any closed surface'", abs(flux) > 1e-8 * absf, False)

# ---------------------------------------------------------------------------------------------
section("20.2 Joule heating at a point")
sig = 0.02
Jz = lambda wt: -0.1 * np.sin(wt)
Ez = lambda wt: Jz(wt) / sig
rchk("20.2(a) E_z at wt = pi/2 (E = -z 5 sin wt) [V/m]", Ez(np.pi / 2), "-5")
tf("20.2(a) E parallel to J at every instant", np.all(Jz(np.linspace(0.1, 6, 50)) * Ez(np.linspace(0.1, 6, 50)) > 0), True)
wt = np.linspace(0, 2 * np.pi, 400001)[:-1]
JE = Jz(wt) * Ez(wt)
rchk("20.2(b) max J.E [W/m^3]", JE.max(), "0.5")
pk = wt[(JE > JE.max() * (1 - 1e-9))]
chk("20.2(b) instants of the maximum, wt/pi", [pk[pk < np.pi].mean() / np.pi, pk[pk > np.pi].mean() / np.pi], [0.5, 1.5])
rchk("20.2(b) <J.E> [W/m^3]", tavg(lambda t: Jz(t) * Ez(t), 2 * np.pi), "0.25")
rchk("20.2(c) <J.E> per litre [mW]", tavg(lambda t: Jz(t) * Ez(t), 2 * np.pi) * 1e-3 * 1e3, "0.25")
tf("20.2(c) never negative, zero twice per period", JE.min() >= 0 and np.sum(np.abs(np.sin(wt)) < 1e-12) == 2, True)
rchk("20.2(d) same E, 2 sigma: <J.E> [W/m^3]", tavg(lambda t: (2 * sig * Ez(t)) * Ez(t), 2 * np.pi), "0.5")
rchk("20.2(d) same J, 2 sigma: <J.E> [W/m^3]", tavg(lambda t: Jz(t) * (Jz(t) / (2 * sig)), 2 * np.pi), "0.125")

# ---------------------------------------------------------------------------------------------
section("20.3 A laser pointer's beam")
E0 = 240 * np.pi
om = 2 * np.pi * 4.74e14
be = om / c
lam, T = 2 * np.pi / be, 2 * np.pi / om
u3 = travel_dir(lambda y, t: E0 * np.cos(om * t + be * y), Y, lam, T)
chk("20.3(a) direction of travel", u3, -Y)
E3 = lambda y, t: Z * E0 * np.cos(om * t + be * y)
H3 = lambda y, t: np.cross(u3, E3(y, t)) / eta0
chk("20.3(a) H at the crest (y=0,t=0) = -x 2 A/m", H3(0.0, 0.0), -2 * X)
# Faraday check of that H at a lower frequency (only omega/beta = c matters)
omF, beF, hF = 2 * np.pi * 1e8, 2 * np.pi * 1e8 / c, 1e-4
E3F = lambda y, t: Z * E0 * np.cos(omF * t + beF * y)
H3F = lambda y, t: np.cross(-Y, E3F(y, t)) / eta0
y0, t0 = 0.31, 1.7e-9
curlE = np.array([(E3F(y0 + hF, t0)[2] - E3F(y0 - hF, t0)[2]) / (2 * hF), 0, 0])  # (dEz/dy, 0, 0)
dHdt = (H3F(y0, t0 + hF / c) - H3F(y0, t0 - hF / c)) / (2 * hF / c)
chk("20.3(a) Faraday: curl E = -mu0 dH/dt", curlE, -mu0 * dHdt, rtol=1e-5, atol=1e-6)
S3 = lambda t: np.cross(E3(0.0, t), H3(0.0, t))
chk("20.3(b) peak S vector (t=0) [W/m^2]", S3(0.0), -Y * 480 * np.pi)
rchk("20.3(b) 480 pi", 480 * np.pi, "1508")
Sav3 = tavg(S3, T)
chk("20.3(b) <S> vector [W/m^2]", Sav3, -Y * 240 * np.pi)
rchk("20.3(b) |<S>|", -Sav3[1], "754")
chk("20.3(b) <S> = E0^2/(2 eta0)", -Sav3[1], E0 ** 2 / (2 * eta0))
P3 = -Sav3[1] * 1e-6
rchk("20.3(c) beam power [mW]", P3 * 1e3, "0.754")
print(f"      intensity / sunlight = {-Sav3[1]/1361:.3f} (page: 'just over half')")
tf("20.3(c) just over half of sunlight", 0.5 < -Sav3[1] / 1361 < 0.6, True)
wav = tavg(lambda t: 0.5 * eps0x * np.dot(E3(0, t), E3(0, t)) + 0.5 * mu0 * np.dot(H3(0, t), H3(0, t)), T)
chk("20.3(d) <w> = 8 pi e-7 J/m^3", wav, 8 * np.pi * 1e-7, rtol=1e-6)
rchk("20.3(d) <w> [uJ/m^3]", wav * 1e6, "2.51")
chk("20.3(d) <w> = <S>/c", wav, -Sav3[1] / c, rtol=1e-6)
rchk("20.3(d) energy in 1 m of beam [pJ]", wav * 1e-6 * 1.0 * 1e12, "2.51")
rchk("20.3(d) P/c [pJ]", P3 / c * 1e12, "2.51")
rchk("20.3(d) light travel time over 1 m [ns]", 1 / c * 1e9, "3.33")
we_av = tavg(lambda t: 0.5 * eps0x * np.dot(E3(0, t), E3(0, t)), T)
chk("20.3(d) half electric", we_av / wav, 0.5, rtol=1e-6)

# ---------------------------------------------------------------------------------------------
section("20.4 Standing waves, true or false")
E0, lam = 1.0, 1.0
be = 2 * np.pi / lam
om = be * c
T = 2 * np.pi / om
e0n, m0n = 1 / (eta0 * c), eta0 / c
xs = np.linspace(0, lam, 401)
ts = (np.arange(256) + 0.5) * T / 256
XX, TT = np.meshgrid(xs, ts, indexing="ij")
E1 = E0 * np.cos(om * TT - be * XX)[..., None] * Y
E2 = E0 * np.cos(om * TT + be * XX)[..., None] * Y
H1 = np.cross(X, E1) / eta0
H2 = np.cross(-X, E2) / eta0
E4, H4 = E1 + E2, H1 + H2
chk("20.4 stem E = y 2E0 cos wt cos bx", E4[..., 1], 2 * E0 * np.cos(om * TT) * np.cos(be * XX), atol=1e-12)
chk("20.4 stem H = z (2E0/eta0) sin wt sin bx", H4[..., 2], 2 * E0 / eta0 * np.sin(om * TT) * np.sin(be * XX), atol=1e-14)
S4 = np.cross(E4, H4)
w4 = 0.5 * e0n * np.sum(E4 ** 2, -1) + 0.5 * m0n * np.sum(H4 ** 2, -1)
chk("20.4 S = x (E0^2/eta0) sin 2wt sin 2bx", S4[..., 0], E0 ** 2 / eta0 * np.sin(2 * om * TT) * np.sin(2 * be * XX), atol=1e-14)
chk("20.4 w formula", w4, 2 * e0n * E0 ** 2 * (np.cos(om * TT) ** 2 * np.cos(be * XX) ** 2 + np.sin(om * TT) ** 2 * np.sin(be * XX) ** 2), atol=1e-20)
tf("20.4(a) S = 0 at every point and instant", np.abs(S4).max() < 1e-12, False)
q = [lam / 4, lam / 2, 3 * lam / 4]
tf("20.4(a) S = 0 on the quarter-wave planes", all(np.abs(np.interp(xq, xs, np.abs(S4[..., 0]).max(1))) < 1e-15 for xq in q), True)
Sav4 = S4.mean(1)
tf("20.4(b) <S> = 0 at every point", np.abs(Sav4).max() < 1e-15, True)
wav4 = w4.mean(1)
chk("20.4(c) <w> = eps0 E0^2 at every x", [wav4.min(), wav4.max()], [e0n * E0 ** 2] * 2, rtol=1e-9)
tf("20.4(c) energy density zero throughout", wav4.max() < 1e-30, False)
iq = np.argmin(np.abs(xs - lam / 4))
tf("20.4(d) E always zero at x = lambda/4", np.abs(E4[iq]).max() < 1e-12, True)
chk("20.4(d) w(lambda/4, t) = 2 eps0 E0^2 sin^2 wt", w4[iq], 2 * e0n * E0 ** 2 * np.sin(om * ts) ** 2, rtol=1e-9, atol=1e-25)
tf("20.4(d) energy density zero at all times there", w4[iq].max() < 1e-30, False)
xe = np.linspace(lam / 4, 3 * lam / 4, 2001)
Wq = []
for tt in np.linspace(0, T, 13):
    e = 2 * E0 * np.cos(om * tt) * np.cos(be * xe)
    hh = 2 * E0 / eta0 * np.sin(om * tt) * np.sin(be * xe)
    Wq.append(integrate.simpson(0.5 * e0n * e ** 2 + 0.5 * m0n * hh ** 2, x=xe))
Wq = np.array(Wq)
chk("20.4(e) stored energy between E-nodes = eps0 E0^2 lambda/2 (all t)", [Wq.min(), Wq.max()], [e0n * E0 ** 2 * lam / 2] * 2, rtol=1e-8)
tf("20.4(e) does not change with time", np.ptp(Wq) < 1e-8 * Wq.mean(), True)
E2h = 0.5 * E2
S4f = np.cross(E1 + E2h, H1 + np.cross(-X, E2h) / eta0)
Sf = S4f[..., 0].mean(1)
chk("20.4(f) <S_x> with E0/2 backward wave (all x) [units E0^2/eta0]", [Sf.min() * eta0, Sf.max() * eta0], [3 / 8, 3 / 8], rtol=1e-9)
tf("20.4(f) statement (3E0^2/(8 eta0) along +x)", abs(Sf.mean() * eta0 - 3 / 8) < 1e-9 and Sf.min() > 0, True)
Hz_chk = (H1 + np.cross(-X, E2h) / eta0)[..., 2]
chk("20.4(f) H_z = (E1y - E2y)/eta0", Hz_chk, (E1[..., 1] - E2h[..., 1]) / eta0, atol=1e-15)

# ---------------------------------------------------------------------------------------------
section("20.5 How far a station reaches (find the error)")
Pt, Emin = 6000.0, 0.01
rs = np.sqrt(eta0 * Pt / (4 * np.pi)) / Emin
rchk("20.5 student's sqrt(30P)/E (with <S> = E0^2/eta0) [km]", rs / 1e3, "42.4")
chk("20.5 eta0/(4 pi) = 30", eta0 / (4 * np.pi), 30)
Sfac = tavg(lambda t: np.cos(t) ** 2, 2 * np.pi)
chk("20.5 <cos^2> = 1/2 (so <S> = E0^2/(2 eta0))", Sfac, 0.5, rtol=1e-12)
rt = optimize.brentq(lambda r: Pt / (4 * np.pi * r ** 2) - Sfac * Emin ** 2 / eta0, 1.0, 1e7)
rchk("20.5 corrected range [km]", rt / 1e3, "60")
chk("20.5 sqrt(60 P) = 600", np.sqrt(60 * Pt), 600, rtol=1e-12)
rchk("20.5 <S> at 60 km from P/(4 pi r^2) [1e-7 W/m^2]", Pt / (4 * np.pi * 6e4 ** 2) * 1e7, "1.33")
rchk("20.5 E0^2/(2 eta0) at 10 mV/m [1e-7 W/m^2]", Emin ** 2 / (2 * eta0) * 1e7, "1.33")
chk("20.5 ratio of ranges = sqrt 2", rt / rs, np.sqrt(2), rtol=1e-9)

# ---------------------------------------------------------------------------------------------
section("20.6 Split, then add")
f6, er = 75e6, 4.0
v6, eta6 = c / np.sqrt(er), eta0 / np.sqrt(er)
om = 2 * np.pi * f6
be = om / v6
lam, T = 2 * np.pi / be, 1 / f6
chk("20.6(a) v [m/s]", v6, 1.5e8)
rchk("20.6(a) eta [ohm]", eta6, "188.5")
chk("20.6(a) eta = 60 pi", eta6, 60 * np.pi, rtol=1e-12)
chk("20.6(a) beta = pi rad/m, lambda = 2 m", [be, lam], [np.pi, 2.0], rtol=1e-12)
E6 = lambda z, t: X * 6 * np.cos(om * t + be * z) - Y * 8 * np.sin(om * t + be * z)
u6 = travel_dir(lambda z, t: 6 * np.cos(om * t + be * z), Z, lam, T)
chk("20.6(a) direction", u6, -Z)
H6 = lambda z, t: np.cross(u6, E6(z, t)) / eta6
for (zz, tt) in [(0.3, 1.1e-9), (-0.7, 4.2e-9)]:
    chk(f"20.6(b) H = -y 6/(60pi) cos - x 8/(60pi) sin  at z={zz}", H6(zz, tt),
        -Y * 6 / (60 * np.pi) * np.cos(om * tt + be * zz) - X * 8 / (60 * np.pi) * np.sin(om * tt + be * zz), atol=1e-12)
    h = 1e-4
    dEdz = (E6(zz + h, tt) - E6(zz - h, tt)) / (2 * h)
    dHdz = (H6(zz + h, tt) - H6(zz - h, tt)) / (2 * h)
    dHdt = (H6(zz, tt + h / v6) - H6(zz, tt - h / v6)) / (2 * h / v6)
    dEdt = (E6(zz, tt + h / v6) - E6(zz, tt - h / v6)) / (2 * h / v6)
    chk(f"20.6(b) Faraday curl E = -mu0 dH/dt at z={zz}", np.array([-dEdz[1], dEdz[0], 0]), -mu0 * dHdt, rtol=1e-5, atol=1e-9)
    chk(f"20.6(b) Ampere curl H = eps dE/dt at z={zz}", np.array([-dHdz[1], dHdz[0], 0]), er / (eta0 * c) * dEdt, rtol=1e-5, atol=1e-12)
rchk("20.6(b) 6/(60 pi)", 6 / (60 * np.pi), "0.0318")
rchk("20.6(b) 8/(60 pi)", 8 / (60 * np.pi), "0.0424")
E61 = lambda z, t: X * np.dot(E6(z, t), X)
H61 = lambda z, t: np.cross(u6, E61(z, t)) / eta6
S61 = tavg(lambda t: np.cross(E61(0.37, t), H61(0.37, t)), T)
chk("20.6(c) <E1 x H1> = -z 3/(10 pi)", S61, -Z * 3 / (10 * np.pi), rtol=1e-9, atol=1e-14)
rchk("20.6(c) 3/(10 pi)", 3 / (10 * np.pi), "0.0955")
S6 = tavg(lambda t: np.cross(E6(0.37, t), H6(0.37, t)), T)
chk("20.6(d) <E x H> = -z 5/(6 pi)", S6, -Z * 5 / (6 * np.pi), rtol=1e-9, atol=1e-14)
rchk("20.6(d) 5/(6 pi)", 5 / (6 * np.pi), "0.265")
rchk("20.6(d) y part 64/(2 eta)", 64 / (2 * eta6), "0.170")
for phs in [0.0, 0.7, np.pi / 2]:
    Ep = lambda z, t: X * 6 * np.cos(om * t + be * z) - Y * 8 * np.sin(om * t + be * z + phs)
    Sp = tavg(lambda t: np.cross(Ep(0.0, t), np.cross(u6, Ep(0.0, t)) / eta6), T)
    chk(f"20.6(d) <S> independent of the shift (extra phase {phs:.2f})", Sp[2], -5 / (6 * np.pi), rtol=1e-9)
wt = np.linspace(0, 2 * np.pi, 720001)[:-1]
Smag = np.array([np.linalg.norm(np.cross(E6(0, w_ / om), H6(0, w_ / om))) for w_ in wt[::1000]])
Smag_f = (36 * np.cos(wt) ** 2 + 64 * np.sin(wt) ** 2) / eta6
chk("20.6(e) |S| sampled = (36 cos^2 + 64 sin^2)/eta", Smag, Smag_f[::1000], rtol=1e-9)
rchk("20.6(e) min |S| [W/m^2]", Smag_f.min(), "0.191")
rchk("20.6(e) max |S| [W/m^2]", Smag_f.max(), "0.340")
mins = wt[Smag_f < Smag_f.min() + 1e-12]
maxs = wt[Smag_f > Smag_f.max() - 1e-12]
chk("20.6(e) wt of minima / pi", sorted(set(np.round(mins / np.pi, 6))), [0.0, 1.0])
chk("20.6(e) wt of maxima / pi", sorted(set(np.round(maxs / np.pi, 6))), [0.5, 1.5])
chk("20.6(e) E at the minima = +-x 6, at maxima = -+y 8", [E6(0, 0)[0], E6(0, np.pi / om)[0], E6(0, np.pi / 2 / om)[1], E6(0, 1.5 * np.pi / om)[1]], [6, -6, -8, 8], atol=1e-9)
rchk("20.6(e) linear 10 V/m wave peak 100/eta", 100 / eta6, "0.531")
P6 = abs(S6[2]) * 0.25
rchk("20.6(f) power through 0.5 m square [mW]", P6 * 1e3, "66.3")
chk("20.6(f) = 5/(24 pi)", P6, 5 / (24 * np.pi), rtol=1e-9)
w6 = tavg(lambda t: 0.5 * er / (eta0 * c) * np.dot(E6(0, t), E6(0, t)) + 0.5 * mu0 * np.dot(H6(0, t), H6(0, t)), T)
rchk("20.6 check <w> [1e-9 J/m^3]", w6 * 1e9, "1.77")
rchk("20.6 check v<w> [W/m^2]", v6 * w6, "0.265")

# ---------------------------------------------------------------------------------------------
section("20.7 A leaky spherical capacitor (eps0 = 8.85e-12 as stated)")
e0 = 8.85e-12
a, b, eps, sg, V0 = 0.01, 0.03, 6 * 8.85e-12, 2.0e-7, 1000.0
tau = eps / sg
rchk("20.7(a) tau [us]", tau * 1e6, "266")
Vq = integrate.quad(lambda r: 1.0 / (4 * np.pi * eps * r ** 2), a, b)[0]   # V for Q = 1 C, V(a)-V(b) = -int_b^a E dr
C7 = 1.0 / Vq
rchk("20.7(a) C [pF]", C7 * 1e12, "10.0")
Q0 = C7 * V0
rchk("20.7(a) Q0 [nC]", Q0 * 1e9, "10.0")
E7 = lambda r, t: Q0 * np.exp(-t / tau) / (4 * np.pi * eps * r ** 2)
chk("20.7(a) E r^2 at t=0 [V m]", E7(0.02, 0) * 0.02 ** 2, 15.0, rtol=1e-3)
rchk("20.7(a) E(a,0) [1e5 V/m]", E7(a, 0) / 1e5, "1.50")
rchk("20.7(a) E(b,0) [1e4 V/m]", E7(b, 0) / 1e4, "1.67")
chk("20.7(b) sigma * 15 V m = 3.0e-6 A", sg * E7(0.02, 0) * 0.02 ** 2, 3.0e-6, rtol=1e-3)
rchk("20.7(b) J(a,0) [A/m^2]", sg * E7(a, 0), "0.030")
hT = tau * 1e-5
dDdt = eps * (E7(0.017, 0.3 * tau + hT) - E7(0.017, 0.3 * tau - hT)) / (2 * hT)
chk("20.7(b) J + dD/dt = 0 (finite difference)", sg * E7(0.017, 0.3 * tau) + dDdt, 0.0, atol=1e-9 * sg * E7(0.017, 0))
w7 = 0.5 * eps * E7(a, 0) ** 2
rchk("20.7(c) w(a,0) [J/m^3]", w7, "0.597")
rchk("20.7(c) J.E(a,0) [W/m^3]", sg * E7(a, 0) ** 2, "4500")
dwdt7 = (0.5 * eps * E7(0.023, 0.4 * tau + hT) ** 2 - 0.5 * eps * E7(0.023, 0.4 * tau - hT) ** 2) / (2 * hT)
chk("20.7(c) dw/dt = -J.E (finite difference)", dwdt7, -sg * E7(0.023, 0.4 * tau) ** 2, rtol=1e-7)
chk("20.7(c) 2w/tau = J.E at r=a", 2 * w7 / tau, sg * E7(a, 0) ** 2, rtol=1e-9)
W7 = lambda t: integrate.quad(lambda r: 0.5 * eps * E7(r, t) ** 2 * 4 * np.pi * r ** 2, a, b)[0]
P7 = lambda t: integrate.quad(lambda r: sg * E7(r, t) ** 2 * 4 * np.pi * r ** 2, a, b)[0]
rchk("20.7(d) W(0) = int 1/2 eps E^2 dV [uJ]", W7(0) * 1e6, "5.00")
rchk("20.7(d) W(0) = 1/2 C V0^2 [uJ]", 0.5 * C7 * V0 ** 2 * 1e6, "5.00")
rchk("20.7(d) G = P(0)/V0^2 [1e-8 S]", P7(0) / V0 ** 2 * 1e8, "3.77")
rchk("20.7(d) P(0) [mW]", P7(0) * 1e3, "37.7")
chk("20.7(d) P(0) = 2 W(0)/tau", P7(0), 2 * W7(0) / tau, rtol=1e-9)
heat = integrate.quad(P7, 0, 40 * tau, limit=200)[0]
rchk("20.7(d) total heat int_0^inf P dt [uJ]", heat * 1e6, "5.00")
chk("20.7(d) heat = W(0)", heat, W7(0), rtol=1e-6)
chk("20.7(d) P(t) = P(0) exp(-2t/tau) at t=tau", P7(tau), P7(0) * np.exp(-2), rtol=1e-9)
th = optimize.brentq(lambda t: W7(t) - W7(0) / 2, 0, 5 * tau)
tq = optimize.brentq(lambda t: E7(a, t) - E7(a, 0) / 2, 0, 5 * tau)
rchk("20.7(d) half the energy gone [us]", th * 1e6, "92")
rchk("20.7(d) half the charge gone [us]", tq * 1e6, "184")
print(f"      (with eps0 = 8.854e-12 instead: w(a,0) = {0.5*6*8.854e-12*E7(a,0)**2:.4f} J/m^3, W(0) = {0.5*4*np.pi*6*8.854e-12*0.015*V0**2*1e6:.4f} uJ)")

# ---------------------------------------------------------------------------------------------
section("20.8 Energy flows into a solenoid")
a, n, k, t8 = 0.02, 1000.0, 50.0, 0.2
I8 = lambda t: k * t
Hin = lambda t: Z * n * I8(t)                                      # given (Lecture 13)
Psi = lambda r, t: mu0 * n * I8(t) * np.pi * min(r, a) ** 2         # flux through a circle of radius r


def E8(x, y, t, h=1e-4):
    r = np.hypot(x, y)
    Ephi = -(Psi(r, t + h) - Psi(r, t - h)) / (2 * h) / (2 * np.pi * r)   # Faraday on a circle, ccw from +z
    return Ephi * np.array([-y / r, x / r, 0.0])


rchk("20.8(a) E_phi(a) [1e-4 V/m]", E8(a, 0, t8)[1] / 1e-4, "-6.28")
chk("20.8(a) E = -phi mu0 n k r/2 at r = 1.3 cm", E8(0.0, 0.013, t8)[0], mu0 * n * k * 0.013 / 2, rtol=1e-6)   # at (0,r): -phi = +x
tf("20.8(a) clockwise from +z (E_phi < 0), against the +phi winding current", E8(a, 0, t8)[1] < 0, True)
chk("20.8(a) I and H at t=0.2 s", [I8(t8), Hin(t8)[2]], [10, 1e4])
S8 = lambda x, y, t: np.cross(E8(x, y, t), Hin(t))
Sa = S8(a, 0, t8)
chk("20.8(a) S at (a,0): direction -r (= -x here)", Sa / np.linalg.norm(Sa), -X, atol=1e-9)
rchk("20.8(a) |S(a)| [W/m^2]", np.linalg.norm(Sa), "6.28")
hT = 1e-3
w8 = lambda t: 0.5 * mu0 * np.dot(Hin(t), Hin(t)) + 0.5 * e0 * np.dot(E8(0.011, 0.004, t), E8(0.011, 0.004, t))
dwdt8 = (w8(t8 + hT) - w8(t8 - hT)) / (2 * hT)
rchk("20.8(b) dw/dt [W/m^3]", dwdt8, "628")
print(f"      1/2 eps0 E^2 at r=a: {0.5*e0*E8(a,0,t8)[1]**2:.2e} J/m^3 (page 'about 1e-18'); its d/dt: {(0.5*e0*np.dot(E8(a,0,t8+hT),E8(a,0,t8+hT))-0.5*e0*np.dot(E8(a,0,t8-hT),E8(a,0,t8-hT)))/(2*hT):.1e}")
x0, y0, hx = 0.011, 0.004, 1e-5
divS = ((S8(x0 + hx, y0, t8)[0] - S8(x0 - hx, y0, t8)[0]) + (S8(x0, y0 + hx, t8)[1] - S8(x0, y0 - hx, t8)[1])) / (2 * hx)
rchk("20.8(b) div S [W/m^3]", divS, "-628")
chk("20.8(b) dw/dt + div S + 0 = 0", dwdt8 + divS, 0.0, atol=1e-4)
curlEz = ((E8(x0 + hx, y0, t8)[1] - E8(x0 - hx, y0, t8)[1]) - (E8(x0, y0 + hx, t8)[0] - E8(x0, y0 - hx, t8)[0])) / (2 * hx)
chk("20.8(b) curl E = -z mu0 n k", curlEz, -mu0 * n * k, rtol=1e-6)
rchk("20.8(b) H.(curl E) [W/m^3]", Hin(t8)[2] * curlEz, "-628")
chk("20.8(b) identity: div S = H.curlE - E.curlH (curl H = 0)", divS, Hin(t8)[2] * curlEz - 0.0, rtol=1e-6)
phs = (np.arange(720) + 0.5) * 2 * np.pi / 720
Pin = sum(-np.dot(S8(a * np.cos(p), a * np.sin(p), t8), np.array([np.cos(p), np.sin(p), 0])) for p in phs) * a * (2 * np.pi / 720)
rchk("20.8(c) inflow through r=a per metre [W/m]", Pin, "0.790")
Lp = n * Psi(a, 1.0) / I8(1.0)
rchk("20.8(c) inductance per metre [1e-3 H/m]", Lp * 1e3, "1.58")
dWm = (0.5 * Lp * I8(t8 + hT) ** 2 - 0.5 * Lp * I8(t8 - hT) ** 2) / (2 * hT)
rchk("20.8(c) d/dt(1/2 L I^2) [W/m]", dWm, "0.790")
chk("20.8(c) inflow = d/dt(1/2 L I^2)", Pin, dWm, rtol=1e-6)
Eout = E8(a * (1 + 1e-9), 0, t8)
JsE8 = np.dot(Y * n * I8(t8), Eout)     # at (a,0): phi = +y
rchk("20.8(d) Js.E on the winding [W/m^2]", JsE8, "-6.28")
chk("20.8(d) E continuous across the winding", Eout, E8(a * (1 - 1e-9), 0, t8), rtol=1e-6)
chk("20.8(d) sheet form r.(S1 - S2) = -Js.E", np.dot(X, np.cross(Eout, 0 * Z) - Sa), -JsE8, rtol=1e-6)

# ---------------------------------------------------------------------------------------------
section("20.9 A coax with a resistive core")
a, b, ell, Rp, V0, RL = 1e-3, 4e-3, 10.0, 1.0, 100.0, 40.0
sg9 = 1 / (Rp * np.pi * a ** 2)
rchk("20.9 sigma for R' = 1 ohm/m [1e5 S/m]", sg9 / 1e5, "3.18")
rchk("20.9 R' with the rounded sigma 3.18e5 [ohm/m]", 1 / (3.18e5 * np.pi * a ** 2), "1.00")
I9 = V0 / (Rp * ell + RL)
rchk("20.9(a) I [A]", I9, "2")
Vz = lambda z: V0 - I9 * Rp * z
rchk("20.9(a) V(ell) [V]", Vz(ell), "80")
chk("20.9(a) V(ell) = I R_L", Vz(ell), I9 * RL)
chk("20.9(a) battery, inner conductor, load [W]", [V0 * I9, I9 ** 2 * Rp * ell, Vz(ell) * I9], [200, 40, 160])
Phi = lambda r, z: Vz(z) * np.log(b / r) / np.log(b / a)
r0, z0, hr = 2.5e-3, 4.0, 1e-6
d1 = lambda r: (Phi(r + hr, z0) - Phi(r - hr, z0)) / (2 * hr)
lap = ((r0 + hr / 2) * (Phi(r0 + hr, z0) - Phi(r0, z0)) - (r0 - hr / 2) * (Phi(r0, z0) - Phi(r0 - hr, z0))) / (r0 * hr ** 2) \
    + (Phi(r0, z0 + 1e-2) - 2 * Phi(r0, z0) + Phi(r0, z0 - 1e-2)) / 1e-4
scale = abs((Phi(r0 + hr, z0) - 2 * Phi(r0, z0) + Phi(r0 - hr, z0)) / hr ** 2)
tf(f"20.9(b) Laplace: |lap Phi| / |d2Phi/dr2| = {abs(lap)/scale:.1e} small", abs(lap) / scale < 1e-4, True)
chk("20.9(b) Phi(a,z) = V(z), Phi(b,z) = 0", [Phi(a, 3.0), Phi(b, 3.0)], [Vz(3.0), 0.0], atol=1e-12)


def E9(r, z, h=1e-8, hz=1e-2):    # E = -grad Phi, finite differences in Cartesian at (x=r, y=0, z)
    P3 = lambda x, y, zz: Phi(np.hypot(x, y), zz)
    return -np.array([(P3(r + h, 0, z) - P3(r - h, 0, z)) / (2 * h), (P3(r, h, z) - P3(r, -h, z)) / (2 * h),
                      (P3(r, 0, z + hz) - P3(r, 0, z - hz)) / (2 * hz)])


H9 = lambda r: Y * I9 / (2 * np.pi * r)       # at (x=r, y=0): phi-hat = +y
rchk("20.9(b) E_z(a) [V/m]", E9(a, 3.0)[2], "2")
chk("20.9(b) E_z(a) = J/sigma inside the core", E9(a, 3.0)[2], I9 / (sg9 * np.pi * a ** 2), rtol=1e-6)
chk("20.9(b) E_z(b) = 0", E9(b, 3.0)[2], 0.0, atol=1e-9)
rchk("20.9(b) E_r(a, z=0) [kV/m]", E9(a, 0.0)[0] / 1e3, "72.1")
rchk("20.9(b) E_r(a, z=ell) [kV/m]", E9(a, ell)[0] / 1e3, "57.7")
rchk("20.9(b) ln 4", np.log(4), "1.386")
rchk("20.9(b) H(a) [A/m]", H9(a)[1], "318")
S9 = lambda r, z: np.cross(E9(r, z), H9(r))
Sz_flow = lambda z: integrate.quad(lambda r: S9(r, z)[2] * 2 * np.pi * r, a, b, epsabs=1e-10)[0]
rchk("20.9(c) power through the cross-section at z=0 [W]", Sz_flow(0.0), "200")
rchk("20.9(c) power through the cross-section at z=ell [W]", Sz_flow(ell), "160")
rchk("20.9(c) S_z(a, z=0) [1e7 W/m^2]", S9(a, 0.0)[2] / 1e7, "2.30")
rchk("20.9(d) S_r(a) [W/m^2]", S9(a, 5.0)[0], "-637")
chk("20.9(d) S_r(b) = 0", S9(b, 5.0)[0], 0.0, atol=1e-6)
rchk("20.9(d) power into the core per metre [W/m]", -S9(a, 5.0)[0] * 2 * np.pi * a, "4")
rchk("20.9(d) over 10 m [W]", -S9(a, 5.0)[0] * 2 * np.pi * a * ell, "40")
z1, z2 = 2.0, 3.0
f_end2, f_end1 = Sz_flow(z2), -Sz_flow(z1)
f_in = np.dot(S9(a, 2.5), -X) * 2 * np.pi * a * (z2 - z1)
f_out = np.dot(S9(b, 2.5), X) * 2 * np.pi * b * (z2 - z1)
chk("20.9(d) ring 2<z<3: end fluxes, inner wall, outer wall [W]", [f_end2, f_end1, f_in, f_out], [188, -192, 4, 0], atol=1e-6)
chk("20.9(d) ring ledger total", f_end2 + f_end1 + f_in + f_out, 0.0, atol=1e-6)
for zz, sv, ang in [(0.0, "2.77e-5", "0.0016"), (ell, "3.47e-5", "0.0020")]:
    s = S9(a, zz)
    rchk(f"20.9(e) |S_r|/S_z at r=a, z={zz:g}", abs(s[0]) / s[2], sv)
    rchk(f"20.9(e) tilt [deg] at z={zz:g}", np.degrees(np.arctan2(abs(s[0]), s[2])), ang)

# ---------------------------------------------------------------------------------------------
section("20.10 A sheet in a magnetic medium")
mu, eps = 4 * mu0, 4 * eps0x
v10, eta10 = 1 / np.sqrt(mu * eps), np.sqrt(mu / eps)
om = 5 * np.pi * 1e6
T = 2 * np.pi / om
be = om / v10
rchk("20.10(a) f [MHz]", om / (2 * np.pi) / 1e6, "2.5")
chk("20.10(a) v [m/s]", v10, 7.5e7, rtol=1e-9)
chk("20.10(a) eta = 120 pi", eta10, 120 * np.pi, rtol=1e-9)
rchk("20.10(a) eta [ohm]", eta10, "377")
chk("20.10(a) beta = pi/15", be, np.pi / 15, rtol=1e-9)
rchk("20.10(a) beta [rad/m]", be, "0.209")
chk("20.10(a) lambda = 2 pi/beta = v/f = 30 m", [2 * np.pi / be, v10 / (om / 2 / np.pi)], [30, 30], rtol=1e-9)
Js10 = lambda t: -X * (t >= 0) * np.sin(om * t)
E10 = lambda y, t: -(eta10 / 2) * Js10(t - abs(y) / v10)
H10 = lambda y, t: 0.5 * np.cross(Js10(t - abs(y) / v10), np.sign(y) * Y)
for yy in (7.0, -7.0):
    tt = 3e-6
    chk(f"20.10(b) E at y={yy:g} = +x 60pi sin(wt - b|y|)", E10(yy, tt), X * 60 * np.pi * np.sin(om * tt - be * abs(yy)), atol=1e-9)
    chk(f"20.10(b) H at y={yy:g} = -+z 0.5 sin(wt -+ by)", H10(yy, tt), -np.sign(yy) * Z * 0.5 * np.sin(om * tt - np.sign(yy) * be * yy), atol=1e-12)
    h = 1e-3
    dEx_dy = (E10(yy + h, tt)[0] - E10(yy - h, tt)[0]) / (2 * h)
    dHz_dt = (H10(yy, tt + h / v10)[2] - H10(yy, tt - h / v10)[2]) / (2 * h / v10)
    dHz_dy = (H10(yy + h, tt)[2] - H10(yy - h, tt)[2]) / (2 * h)
    dEx_dt = (E10(yy, tt + h / v10)[0] - E10(yy, tt - h / v10)[0]) / (2 * h / v10)
    chk(f"20.10(b) Faraday (dEx/dy = mu dHz/dt) at y={yy:g}", dEx_dy, mu * dHz_dt, rtol=1e-5)
    chk(f"20.10(b) Ampere (dHz/dy = eps dEx/dt) at y={yy:g}", dHz_dy, eps * dEx_dt, rtol=1e-5)
    s = np.cross(E10(yy, 2.03e-6), H10(yy, 2.03e-6))
    chk(f"20.10(b) E x H points away from the sheet at y={yy:g}", np.sign(s[1]), np.sign(yy))
rchk("20.10(b) 60 pi", 60 * np.pi, "188.5")
tt = 1.37e-6
chk("20.10(b) y x (H+ - H-) = Js at y=0", np.cross(Y, H10(1e-12, tt) - H10(-1e-12, tt)), Js10(tt), atol=1e-9)
JsE10 = lambda t: np.dot(Js10(t), E10(0.0, t))
chk("20.10(c) Js.E = -60 pi sin^2 wt", JsE10(tt), -60 * np.pi * np.sin(om * tt) ** 2, rtol=1e-9)
JsE_av = tavg(JsE10, T, t0=5 * T)
rchk("20.10(c) <Js.E> [W/m^2]", JsE_av, "-94.2")
chk("20.10(c) = -30 pi = -eta J0^2/4", JsE_av, -eta10 / 4, rtol=1e-9)
Sp = tavg(lambda t: np.cross(E10(7.0, t), H10(7.0, t)), T, t0=5 * T)
Sm = tavg(lambda t: np.cross(E10(-7.0, t), H10(-7.0, t)), T, t0=5 * T)
chk("20.10(d) <S> at y = +7 and -7 m (y components)", [Sp[1], Sm[1]], [15 * np.pi, -15 * np.pi], rtol=1e-9)
rchk("20.10(d) 15 pi", 15 * np.pi, "47.1")
chk("20.10(d) balance 15pi + 15pi = -<Js.E>", Sp[1] - Sm[1], -JsE_av, rtol=1e-9)
Sinst = np.cross(E10(1e-12, tt), H10(1e-12, tt))[1] - np.cross(E10(-1e-12, tt), H10(-1e-12, tt))[1]
chk("20.10(d) instantaneous balance at the sheet", Sinst, -JsE10(tt), rtol=1e-6)
w10 = tavg(lambda t: 0.5 * eps * np.dot(E10(7.0, t), E10(7.0, t)) + 0.5 * mu * np.dot(H10(7.0, t), H10(7.0, t)), T, t0=5 * T)
chk("20.10(e) <w> = 2 pi e-7", w10, 2 * np.pi * 1e-7, rtol=1e-9)
rchk("20.10(e) <w> [1e-7 J/m^3]", w10 * 1e7, "6.28")
chk("20.10(e) <S>/<w> = v", Sp[1] / w10, 7.5e7, rtol=1e-9)
Ev = -(eta0 / 2) * 1.0
Hv = 0.5
wv = tavg(lambda t: 0.5 * eps0x * (Ev * np.sin(t)) ** 2 + 0.5 * mu0 * (Hv * np.sin(t)) ** 2, 2 * np.pi)
Sv = tavg(lambda t: abs(Ev) * Hv * np.sin(t) ** 2, 2 * np.pi)
chk("20.10(e) vacuum: E0, H0, <S> unchanged", [abs(Ev), Hv, Sv], [60 * np.pi, 0.5, 15 * np.pi], rtol=1e-9)
rchk("20.10(e) vacuum <w> [1e-7 J/m^3]", wv * 1e7, "1.57")
chk("20.10(e) vacuum <w> 4 times smaller, lambda 4 times longer", [w10 / wv, (2 * np.pi * c / om) / (2 * np.pi / be)], [4, 4], rtol=1e-9)
rchk("20.10(e) vacuum lambda [m]", 2 * np.pi * c / om, "120")
Js2 = lambda t: -X * (t >= 0) * (np.sin(om * t) + 0.5 * np.sin(3 * om * t))
E2s = lambda y, t: -(eta10 / 2) * Js2(t - abs(y) / v10)
H2s = lambda y, t: 0.5 * np.cross(Js2(t - abs(y) / v10), np.sign(y) * Y)
inj = tavg(lambda t: -np.dot(Js2(t), E2s(0.0, t)), T, t0=5 * T)
rchk("20.10(f) <-Js.E> [W/m^2]", inj, "118")
chk("20.10(f) = 37.5 pi", inj, 37.5 * np.pi, rtol=1e-9)
chk("20.10(f) <sin wt sin 3wt> = 0, <0.25 sin^2 3wt> = 0.125",
    [tavg(lambda t: np.sin(t) * np.sin(3 * t), 2 * np.pi), tavg(lambda t: 0.25 * np.sin(3 * t) ** 2, 2 * np.pi)], [0, 0.125], atol=1e-12)
Sp2 = tavg(lambda t: np.cross(E2s(11.0, t), H2s(11.0, t)), T, t0=5 * T)
rchk("20.10(f) <S> into y>0 [W/m^2]", Sp2[1], "58.9")
chk("20.10(f) = 18.75 pi", Sp2[1], 18.75 * np.pi, rtol=1e-9)
chk("20.10(f) third harmonic adds 7.5 pi", inj - 30 * np.pi, 7.5 * np.pi, rtol=1e-9)

# ---------------------------------------------------------------------------------------------
section("20.11 Two sheets in step")
J0, f11 = 1.0, 100e6
om = 2 * np.pi * f11
be = om / c
T = 1 / f11
chk("20.11(a) beta = 2 pi/3, lambda = 3 m", [be, 2 * np.pi / be], [2 * np.pi / 3, 3.0], rtol=1e-12)
rchk("20.11(a) beta [rad/m]", be, "2.09")
Jsh = lambda t: X * J0 * np.cos(om * t)


def fields(z, t, d):
    Et, Ht = np.zeros(3), np.zeros(3)
    for z0 in (0.0, d):
        tr = t - abs(z - z0) / c
        Et = Et - (eta0 / 2) * Jsh(tr)
        Ht = Ht + 0.5 * np.cross(Jsh(tr), np.sign(z - z0) * Z)
    return Et, Ht


Sav11 = lambda z, d: tavg(lambda t: np.cross(*fields(z, t, d)), T)
for d in (0.6, 0.75, 1.5, 1e-7):
    cc = np.cos(be * d / 2) ** 2
    up, dn = Sav11(d + 0.37, d), Sav11(-0.41, d)
    chk(f"20.11(b) <S_z> above/below = +-60 pi cos^2(bd/2), d={d:g}", [up[2], dn[2]], [60 * np.pi * cc, -60 * np.pi * cc], rtol=1e-9, atol=1e-9)
    if d > 1e-3:
        mid = Sav11(d / 2 + 0.05 * d, d)
        chk(f"20.11(e) <S> between the sheets = 0, d={d:g}", mid, np.zeros(3), atol=1e-9)
    injA = tavg(lambda t: -np.dot(Jsh(t), fields(0.0, t, d)[0]), T)
    injB = tavg(lambda t: -np.dot(Jsh(t), fields(d, t, d)[0]), T)
    chk(f"20.11(c) <-JA.E>, <-JB.E> = 60 pi cos^2(bd/2), d={d:g}", [injA, injB], [60 * np.pi * cc] * 2, rtol=1e-9, atol=1e-9)
    chk(f"20.11(c) injected = outflow, d={d:g}", injA + injB, up[2] - dn[2], rtol=1e-9, atol=1e-9)
    if d > 1e-3:
        jumpA = Sav11(1e-9, d)[2] - Sav11(-1e-9, d)[2]
        chk(f"20.11(e) sheet form at A: <S_z(0+)> - <S_z(0-)> = <-JA.E>, d={d:g}", jumpA, injA, rtol=1e-6, atol=1e-6)
d = 0.6
for (z, t) in [(1.9, 2.3e-9), (2.4, 7.7e-9)]:
    chk(f"20.11(a) closed form above, d=0.6, z={z}", fields(z, t, d)[0][0], -120 * np.pi * np.cos(be * d / 2) * np.cos(om * t - be * z + be * d / 2), atol=1e-9)
    chk(f"20.11(a) closed form below, d=0.6, z={-z}", fields(-z, t, d)[0][0], -120 * np.pi * np.cos(be * d / 2) * np.cos(om * t + be * (-z) - be * d / 2), atol=1e-9)
rchk("20.11(d) one sheet alone injects eta0 J0^2/4", eta0 * J0 ** 2 / 4, "94.2")
rchk("20.11(d) one sheet alone, each way", eta0 * J0 ** 2 / 8, "47.1")
rchk("20.11(d) d=0.75: per sheet", 60 * np.pi * np.cos(be * 0.75 / 2) ** 2, "94.2")
rchk("20.11(d) d=0.75: per side", Sav11(0.75 + 0.37, 0.75)[2], "94.2")
rchk("20.11(d) d=0.75: amplitude 120pi/sqrt2 [V/m]", 120 * np.pi * abs(np.cos(be * 0.75 / 2)), "267")
tf("20.11(d) d=1.5: E = 0 on each sheet at every instant",
   max(np.abs(fields(0.0, t, 1.5)[0]).max() + np.abs(fields(1.5, t, 1.5)[0]).max() for t in np.linspace(0, T, 37)) < 1e-9, True)
rchk("20.11(d) d->0: per sheet / per side", 60 * np.pi, "188.5")
rchk("20.11(d) d->0: total", 120 * np.pi, "377")
chk("20.11(d) d->0: total = 4 x one sheet = eta0 (2J0)^2/4", [120 * np.pi / (eta0 / 4), eta0 * (2 * J0) ** 2 / 4], [4, 120 * np.pi])

# ---------------------------------------------------------------------------------------------
section("20.12 Charging a leaky capacitor (eps0 = 8.85e-12 as stated)")
a, d, eps, R, I = 0.05, 2e-3, 4 * 8.85e-12, 10e6, 10e-6
A = np.pi * a ** 2
C12 = eps * A / d
sg12 = d / (R * A)
tau = R * C12
rchk("20.12(a) A [1e-3 m^2]", A * 1e3, "7.85")
rchk("20.12(a) C [pF]", C12 * 1e12, "139")
rchk("20.12(a) sigma [1e-8 S/m]", sg12 * 1e8, "2.55")
rchk("20.12(a) tau [ms]", tau * 1e3, "1.39")
chk("20.12(a) tau = eps/sigma", eps / sg12, tau, rtol=1e-12)
sol = integrate.solve_ivp(lambda t, V: [(I - V[0] / R) / C12], [0, 20 * tau], [0.0], rtol=1e-11, atol=1e-12, dense_output=True)
Vt = lambda t: sol.sol(t)[0]
chk("20.12(a) ODE V(t) = 100 (1 - e^-t/tau)", [Vt(0.5 * tau), Vt(2 * tau)], [100 * (1 - np.exp(-0.5)), 100 * (1 - np.exp(-2))], rtol=1e-7)
rchk("20.12(a) V(tau) [V]", Vt(tau), "63.2")
dVdt = lambda t: (I - Vt(t) / R) / C12
Ef12 = lambda t: Vt(t) / d          # bottom plate (z=0) positive -> E along +z
rchk("20.12(b) E(inf) = IR/d [1e4 V/m]", I * R / d / 1e4, "5")
rchk("20.12(b) E(tau) [kV/m]", Ef12(tau) / 1e3, "31.6")
for tt in (0.01 * tau, tau, 3 * tau):
    chk(f"20.12(b) J + dD/dt = I/A at t={tt/tau:g} tau", sg12 * Ef12(tt) + eps * dVdt(tt) / d, I / A, rtol=1e-7)
rchk("20.12(b) I/A [1e-3 A/m^2]", I / A * 1e3, "1.27")
rchk("20.12(b) J(tau) [1e-4 A/m^2]", sg12 * Ef12(tau) * 1e4, "8.05")
rchk("20.12(b) dD/dt(tau) [1e-4 A/m^2]", eps * dVdt(tau) / d * 1e4, "4.68")
Hphi = lambda r, t: (sg12 * Ef12(t) + eps * dVdt(t) / d) * np.pi * r ** 2 / (2 * np.pi * r)   # Ampere-Maxwell, ccw from +z
chk("20.12(b) H = I r/(2 pi a^2), time-independent", [Hphi(0.03, 0.2 * tau), Hphi(0.03, 4 * tau)], [I * 0.03 / (2 * np.pi * a ** 2)] * 2, rtol=1e-7)
rchk("20.12(b) H(a) [1e-5 A/m]", Hphi(a, tau) * 1e5, "3.18")
rchk("20.12(b) H(a/2) [1e-5 A/m]", Hphi(a / 2, tau) * 1e5, "1.59")


def S12(x, y, t):
    r = np.hypot(x, y)
    return np.cross(Z * Ef12(t), Hphi(r, t) * np.array([-y / r, x / r, 0.0]))


s = S12(a, 0, tau)
chk("20.12(c) S at (a,0) points -r (inward)", s / np.linalg.norm(s), -X, atol=1e-9)
rchk("20.12(c) |S(a)| at tau [W/m^2]", np.linalg.norm(s), "1.01")
rchk("20.12(c) side area [1e-4 m^2]", 2 * np.pi * a * d * 1e4, "6.28")
phs = (np.arange(360) + 0.5) * 2 * np.pi / 360
inflow = sum(-np.dot(S12(a * np.cos(p), a * np.sin(p), tau), [np.cos(p), np.sin(p), 0]) for p in phs) * a * (2 * np.pi / 360) * d
rchk("20.12(c) inflow at tau [mW]", inflow * 1e3, "0.632")
chk("20.12(c) inflow = V(t) I at 0.3 tau, tau, 2 tau",
    [sum(-np.dot(S12(a * np.cos(p), a * np.sin(p), tt), [np.cos(p), np.sin(p), 0]) for p in phs) * a * (2 * np.pi / 360) * d for tt in (0.3 * tau, tau, 2 * tau)],
    [Vt(tt) * I for tt in (0.3 * tau, tau, 2 * tau)], rtol=1e-7)
chk("20.12(e) no flux through the plates (S_z = 0)", s[2], 0.0, atol=1e-15)
rchk("20.12(d) dE/dt at tau [1e7 V/(m s)]", dVdt(tau) / d / 1e7, "1.32")
hT = tau * 1e-4
wq = lambda t: 0.5 * eps * Ef12(t) ** 2 + 0.5 * mu0 * Hphi(a / 2, t) ** 2
dwdt12 = (wq(tau + hT) - wq(tau - hT)) / (2 * hT)
rchk("20.12(d) dw/dt at r=a/2, tau [W/m^3]", dwdt12, "14.8")
x0, y0, hx = a / 2 * np.cos(0.5), a / 2 * np.sin(0.5), 1e-6
divS12 = ((S12(x0 + hx, y0, tau)[0] - S12(x0 - hx, y0, tau)[0]) + (S12(x0, y0 + hx, tau)[1] - S12(x0, y0 - hx, tau)[1])) / (2 * hx)
rchk("20.12(d) div S at r=a/2, tau [W/m^3]", divS12, "-40.2")
JE12 = sg12 * Ef12(tau) ** 2
rchk("20.12(d) J.E [W/m^3]", JE12, "25.4")
chk("20.12(d) sum = 0", dwdt12 + divS12 + JE12, 0.0, atol=1e-5)
chk("20.12(d) div S = -E.(curl H) = -E I/A", divS12, -Ef12(tau) * I / A, rtol=1e-6)
Vol = A * d
rchk("20.12(e) gap volume [1e-5 m^3]", Vol * 1e5, "1.57")
rchk("20.12(e) dW/dt [uW]", dwdt12 * Vol * 1e6, "232.5")
rchk("20.12(e) int J.E dV [uW]", JE12 * Vol * 1e6, "399.6")
chk("20.12(e) int J.E dV = V^2/R", JE12 * Vol, Vt(tau) ** 2 / R, rtol=1e-7)
rchk("20.12(e) closed-surface flux [uW]", -inflow * 1e6, "-632.1")
chk("20.12(e) ledger -dW/dt = flux + int J.E", -dwdt12 * Vol, -inflow + JE12 * Vol, rtol=1e-6)
frac = lambda t: C12 * Vt(t) * dVdt(t) / (Vt(t) * I)
chk("20.12(e) stored fraction at 0+, tau, 15 tau", [frac(1e-7 * tau), frac(tau), frac(15 * tau)], [1.0, np.exp(-1), 0.0], rtol=1e-5, atol=1e-6)
rchk("20.12(e) stored fraction at tau [%]", 100 * frac(tau), "36.8")

print(f"\nTOTAL: {NP} PASS, {NF} FAIL")
