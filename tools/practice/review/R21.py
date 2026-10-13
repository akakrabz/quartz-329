#!/usr/bin/env python3
"""R21.py -- independent re-solution of practice page 21 (monochromatic waves and phasors, lossless media).

Brute-force routes only, written without looking at the author's checks:
  * phasors are MEASURED from time samples by projection over one period (a Fourier coefficient);
  * partner fields come from integrating Faraday's law (mu dH/dt = -curl E) or the Ampere-Maxwell law
    (eps dE/dt = curl H) in time, with finite-difference curls -- never from eta and a rotation;
  * directions of travel come from a rigid-translation test F(r + u v tau, t + tau) = F(r, t) and np.cross;
  * time averages come from sampling a whole period (exact for trigonometric polynomials) or scipy quad;
  * ODEs by solve_ivp, crests by grid search with parabolic refinement, root finding by fsolve.
The definition a(t) = Re{A e^{jwt}} is used only to turn a phasor GIVEN in a statement into a time function.
numpy/scipy only.
"""
import warnings
import numpy as np
from scipy import integrate, optimize

c = 3e8
mu0 = 4e-7*np.pi
eps0 = 1/(mu0*c**2)          # consistent with c = 3e8 and eta0 = 120 pi
eta0 = mu0*c                 # = 120 pi exactly
DEG = np.pi/180
tally = {'PASS': 0, 'FAIL': 0}
warnings.filterwarnings('ignore', category=integrate.IntegrationWarning)   # quad of an exactly-zero average


def fmt(x):
    x = np.asarray(x)
    if np.iscomplexobj(x):
        if x.ndim == 0:
            return f"{x.real:.6g}{x.imag:+.6g}j"
        return "(" + ", ".join(f"{v.real:.5g}{v.imag:+.5g}j" for v in x.ravel()) + ")"
    if x.ndim == 0:
        return f"{float(x):.6g}"
    return "(" + ", ".join(f"{v:.5g}" for v in x.ravel()) + ")"


def rep(label, ok, detail):
    tally['PASS' if ok else 'FAIL'] += 1
    print(f"{'PASS' if ok else 'FAIL'}  {label}: {detail}")


def num(label, got, page, rtol=5e-3, atol=1e-12):
    ok = bool(np.allclose(np.asarray(got), np.asarray(page), rtol=rtol, atol=atol))
    rep(label, ok, f"computed {fmt(got)} | page {fmt(page)}")


def rounded(label, got, page):
    """page values as printed (strings): pass if the computed value rounds to each of them"""
    got = np.atleast_1d(np.asarray(got, float))
    ok = True
    for g, sv in zip(got, page):
        mant = sv.lower().split('e')
        dec = len(mant[0].split('.')[1]) if '.' in mant[0] else 0
        ex = int(mant[1]) if len(mant) > 1 else 0
        ok &= bool(abs(g - float(sv)) <= 0.5*10.0**(ex - dec)*(1 + 1e-9))
    rep(label, ok, f"computed {fmt(got)} | page {', '.join(page)} (rounding check)")


def same(label, got, page):
    rep(label, got == page, f"computed {got} | page {page}")


def small(label, err, tol):
    rep(label, bool(err < tol), f"residual {err:.2e} (tol {tol:.0e})")


# ---------------------------------------------------------------- generic brute-force tools
def tgrid(w, N=1024):
    return np.arange(N)*(2*np.pi/w)/N


def phasor(samples, t, w):
    """measured phasor (cosine reference, peak value) of samples covering whole periods on a uniform grid"""
    return 2*np.mean(samples*np.exp(-1j*w*t), axis=-1)


def from_phasor(P, w):
    """definition a(t) = Re{A e^{jwt}}: only used to turn a GIVEN phasor field into a time function"""
    return lambda r, t: np.real(np.asarray(P(np.asarray(r, float)), complex)[:, None]*np.exp(1j*w*np.atleast_1d(t)))


def avg_quad(f):
    """time average over one period by quad, f a function of the phase wt"""
    return integrate.quad(f, 0, 2*np.pi, limit=400, epsabs=1e-13, epsrel=1e-12)[0]/(2*np.pi)


def curl_t(F, r, t, h):
    r = np.asarray(r, float)
    D = np.empty((3, 3, np.size(t)))
    for j in range(3):
        e = np.zeros(3)
        e[j] = h
        D[:, j] = (F(r + e, t) - F(r - e, t))/(2*h)
    return np.array([D[2, 1] - D[1, 2], D[0, 2] - D[2, 0], D[1, 0] - D[0, 1]])


def antiderivative(y, t):
    """zero-mean time integral of zero-mean periodic samples (trapezoid, uniform grid)"""
    dt = t[1] - t[0]
    Y = np.concatenate([np.zeros(y.shape[:-1] + (1,)),
                        np.cumsum(0.5*(y[..., 1:] + y[..., :-1])*dt, axis=-1)], axis=-1)
    return Y - Y.mean(axis=-1, keepdims=True)


def H_faraday(E, r, t, mu, h):
    """steady-state H from mu dH/dt = -curl E (no static part)"""
    return -antiderivative(curl_t(E, r, t, h), t)/mu


def E_ampere(H, r, t, eps, h):
    """steady-state E from eps dE/dt = curl H (source-free region)"""
    return antiderivative(curl_t(H, r, t, h), t)/eps


def S_avg(E, H):
    return np.mean(np.cross(E.T, H.T), axis=0)


AXES = {'+x': (1, 0, 0), '-x': (-1, 0, 0), '+y': (0, 1, 0), '-y': (0, -1, 0), '+z': (0, 0, 1), '-z': (0, 0, -1)}


def travel(F, v, w, cands=AXES):
    """direction u along which the waveform moves rigidly at speed v: F(r + u v tau, t + tau) = F(r, t)"""
    rng = np.random.default_rng(3)
    T = 2*np.pi/w
    errs = {}
    for name, u in cands.items():
        u = np.asarray(u, float)
        e = 0.0
        for _ in range(10):
            r = rng.uniform(-1, 1, 3)*v*T
            t = rng.uniform(0, T, 6)
            tau = rng.uniform(0.1, 0.4)*T
            e = max(e, float(np.max(np.abs(F(r + u*v*tau, t + tau) - F(r, t)))))
        errs[name] = e
    return min(errs, key=errs.get), errs


def crests(fun, a, b, n=200001):
    """positions of the maxima of fun on [a, b] (grid search + parabolic refinement)"""
    x = np.linspace(a, b, n)
    f = fun(x)
    k = np.where((f[1:-1] > f[:-2]) & (f[1:-1] >= f[2:]))[0] + 1
    d = 0.5*(f[k-1] - f[k+1])/(f[k-1] - 2*f[k] + f[k+1])
    return x[k] + d*(x[1] - x[0])


def maxwell_res(E, H, eps, mu, r, w, h):
    """relative residuals of curl E = -mu dH/dt and curl H = eps dE/dt (finite differences in r and t)"""
    T = 2*np.pi/w
    t = np.linspace(0, T, 48, endpoint=False)
    dt = T*1e-5
    cE, cH = curl_t(E, r, t, h), curl_t(H, r, t, h)
    dH = (H(r, t + dt) - H(r, t - dt))/(2*dt)
    dE = (E(r, t + dt) - E(r, t - dt))/(2*dt)
    return (np.max(np.abs(cE + mu*dH))/np.max(np.abs(cE)), np.max(np.abs(cH - eps*dE))/np.max(np.abs(cH)))


# =========================================================================== 21.1
print("=== 21.1 Reading two waves ===")
w1, b1 = 5*np.pi*1e8, 2.5*np.pi
E1 = lambda y, t: 4*np.cos(w1*t + b1*y + np.pi/3)
tc = crests(lambda t: E1(0.0, t), 0, 20e-9)
T1 = np.mean(np.diff(tc))
yc0 = crests(lambda y: E1(y, 0.0), -2, 2)
lam1 = np.mean(np.diff(yc0))
tau = 0.3e-9
yc1 = crests(lambda y: E1(y, tau), -2, 2)
y0 = yc0[yc0 > 0].min()
vel = (yc1[np.argmin(abs(yc1 - y0))] - y0)/tau
num("21.1a omega = 2pi/T [rad/s]", 2*np.pi/T1, 5*np.pi*1e8)
num("21.1a omega decimal", 2*np.pi/T1, 1.571e9, rtol=1e-3)
num("21.1a f [MHz]", 1/T1/1e6, 250)
num("21.1a T [ns]", T1*1e9, 4)
num("21.1a beta = 2pi/lambda [rad/m]", 2*np.pi/lam1, 7.85, rtol=1e-3)
num("21.1a lambda [m]", lam1, 0.8)
num("21.1a crest velocity along y [m/s] (sign = direction)", vel, -2e8)
same("21.1a direction (rigid translation)", travel(lambda r, t: E1(r[1], t), 2e8, w1)[0], '-y')
num("21.1a eps_r = (c/v_p)^2", (c/abs(vel))**2, 2.25)
num("21.1b crest nearest origin with y>0 at t=0 [m]", y0, 2/3)
tn = tc[tc > 0].min()
num("21.1b next crest recorded at y=0 [ns]", tn*1e9, 10/3)
num("21.1b (2/3 m)/v_p [ns]", y0/abs(vel)*1e9, 3.33, rtol=2e-3)
p1 = lambda x, t: 20*np.cos(np.pi*x - 1000*np.pi*t)
tcp = crests(lambda t: p1(0.0, t), 0, 0.01)
xc0 = crests(lambda x: p1(x, 0.0), -5, 5)
xc1 = crests(lambda x: p1(x, 1e-4), -5, 5)
x0 = xc0[np.argmin(abs(xc0))]
vp1 = (xc1[np.argmin(abs(xc1 - x0))] - x0)/1e-4
num("21.1c f [Hz]", 1/np.mean(np.diff(tcp)), 500)
num("21.1c lambda [m]", np.mean(np.diff(xc0)), 2)
num("21.1c crest velocity along x [m/s]", vp1, 1000)
same("21.1c direction (rigid translation)", travel(lambda r, t: p1(r[0], t), 1000, 1000*np.pi)[0], '+x')
m_He, kB = 6.65e-27, 1.381e-23
Tg = 3*m_He*vp1**2/(5*kB)
num("21.1c T_gas [K]", Tg, 289, rtol=2e-3)
num("21.1c dispersion check omega*sqrt(m/(5/3 kB T)) = beta", 1000*np.pi*np.sqrt(m_He/(5/3*kB*Tg)), np.pi)
num("21.1c T_gas in deg C (page: about 16)", Tg - 273.15, 16, atol=0.5)

# =========================================================================== 21.2
print("\n=== 21.2 Phasors both ways ===")
w = 2*np.pi*1e3
t = tgrid(w)
I2 = phasor(4*np.sin(w*t + 60*DEG), t, w)
num("21.2a I phasor [A]", I2, 3.46 - 2j, rtol=2e-3)
num("21.2a |I|, angle [deg]", [abs(I2), np.angle(I2)/DEG], [4, -30])
V2 = phasor(-10*np.cos(w*t - 45*DEG), t, w)
num("21.2a V phasor [V]", V2, -7.07 + 7.07j, rtol=1e-3)
num("21.2a |V|, angle [deg]", [abs(V2), np.angle(V2)/DEG], [10, 135])
S2 = phasor(8*np.cos(w*t) - 6*np.sin(w*t), t, w)
num("21.2b amplitude, phase [deg]", [abs(S2), np.angle(S2)/DEG], [10, 36.9], rtol=2e-3)
small("21.2b 10cos(wt + 36.87 deg) = 8cos wt - 6sin wt (max abs error)",
      np.max(abs(10*np.cos(w*t + np.angle(S2)) - (8*np.cos(w*t) - 6*np.sin(w*t)))), 1e-9)
Ec2 = from_phasor(lambda r: np.array([0, 0, (-5 + 12j)*np.exp(1j*4*np.pi*r[0])]), w)
rng = np.random.default_rng(5)
e1 = e2 = 0.0
for _ in range(20):
    x = rng.uniform(-1, 1)
    tt = rng.uniform(0, 2*np.pi/w, 8)
    th = w*tt + 4*np.pi*x
    ref = Ec2(np.array([x, 0, 0]), tt)[2]
    e1 = max(e1, np.max(abs(ref - 13*np.cos(th + 112.6*DEG))))
    e2 = max(e2, np.max(abs(ref - (-5*np.cos(th) - 12*np.sin(th)))))
small("21.2c E = 13cos(wt + 4pi x + 112.6 deg) z (max abs error, V/m; 112.6 is rounded)", e1, 0.02)
small("21.2c E = [-5cos(...) - 12sin(...)] z (max abs error)", e2, 1e-9)
num("21.2c |-5+12j|, angle [deg]", [abs(-5 + 12j), np.angle(-5 + 12j)/DEG], [13, 112.6], rtol=1e-3)
num("21.2c calculator atan(12/-5) [deg]", np.arctan(12/-5)/DEG, -67.4, rtol=1e-3)
same("21.2c E direction (rigid translation)", travel(lambda r, t: Ec2(r, t)[2], w/(4*np.pi), w)[0], '-x')
bz = 3.0
Hc2 = from_phasor(lambda r: np.array([2, -3j, 0])*np.exp(-1j*bz*r[2]), w)
eH = 0.0
for _ in range(20):
    z = rng.uniform(-1, 1)
    tt = rng.uniform(0, 2*np.pi/w, 8)
    th = w*tt - bz*z
    eH = max(eH, np.max(abs(Hc2(np.array([0, 0, z]), tt) - np.array([2*np.cos(th), 3*np.sin(th), 0*th]))))
small("21.2c H = 2cos(wt - bz) x + 3sin(wt - bz) y (max abs error)", eH, 1e-9)
same("21.2c H direction (rigid translation)", travel(Hc2, w/bz, w)[0], '+z')
sol = integrate.solve_ivp(lambda tt, a: 10*np.cos(4*tt) - 3*a, (0, 30), [0.0], rtol=1e-11, atol=1e-13,
                          dense_output=True)
td = 8*np.pi + tgrid(4.0, 2000)          # start after the e^{-3t} transient, at a whole number of periods
ad = sol.sol(td)[0]
Ad = phasor(ad, td, 4.0)
num("21.2d steady-state phasor (solve_ivp)", Ad, 1.2 - 1.6j, rtol=1e-6)
num("21.2d amplitude, phase [deg]", [abs(Ad), np.angle(Ad)/DEG], [2, -53.1], rtol=2e-3)
small("21.2d solve_ivp vs 2cos(4t - 53.13 deg)", np.max(abs(ad - 2*np.cos(4*td - np.arctan2(4, 3)))), 1e-7)

# =========================================================================== 21.3
print("\n=== 21.3 Phasor pitfalls, true or false ===")
w = 2*np.pi*1e6
t = tgrid(w)
key = {}
A3 = phasor(5*np.sin(w*t), t, w)
num("21.3a measured phasor of 5 sin wt (claim 5j)", A3, -5j, atol=1e-9)
key['a'] = bool(np.isclose(A3, 5j))
small("21.3a Re{5j e^{jwt}} = -5 sin wt", np.max(abs(np.real(5j*np.exp(1j*w*t)) + 5*np.sin(w*t))), 1e-12)
At = 3*np.exp(1j*40*DEG)
a3 = np.real(At*np.exp(1j*w*t))
cw, c2w = phasor(a3**2, t, w), phasor(a3**2, t, 2*w)
num("21.3b component of a^2 at w (claim: A^2 = 9e^{j80deg})", abs(cw), 0, atol=1e-9)
num("21.3b component of a^2 at 2w (= A^2/2)", c2w, At**2/2)
num("21.3b <a^2> = |A|^2/2", np.mean(a3**2), abs(At)**2/2)
key['b'] = bool(np.isclose(cw, At**2))
F3c = from_phasor(lambda r: np.array([0, 0, 2*np.exp(1j*5*r[1])]), w)
key['c'] = travel(lambda r, t: F3c(r, t)[2], w/5, w)[0] == '-y'
ab3 = avg_quad(lambda th: 4*np.cos(th + 70*DEG)*3*np.cos(th - 20*DEG))
num("21.3d <ab> by quad", ab3, 0, atol=1e-10)
key['d'] = abs(ab3) < 1e-9
be = 2.0
P3e = lambda z: 3*np.exp(-1j*be*z)
F3e = from_phasor(lambda r: np.array([P3e(r[2]), 0, 0]), w)
zz = np.linspace(0.1, 1.4, 6)
f_t0 = np.array([F3e(np.array([0, 0, z]), 0.0)[0, 0] for z in zz])
f_tq = np.array([F3e(np.array([0, 0, z]), np.pi/(2*w))[0, 0] for z in zz])
small("21.3e field at t=0 = Re{phasor} = 3cos(bz)", np.max(abs(f_t0 - 3*np.cos(be*zz))), 1e-12)
small("21.3e field at t=T/4 = -Im{phasor} = 3sin(bz)", np.max(abs(f_tq - 3*np.sin(be*zz))), 1e-12)
key['e'] = bool(np.allclose(P3e(zz), f_t0))
be, w = 2*np.pi, 2*np.pi*c
t = tgrid(w, 2048)
E3f = from_phasor(lambda r: np.array([20*np.exp(-1j*be*r[2]), 0, 0]), w)
r = np.array([0, 0, 0.3])
S3f = S_avg(E3f(r, t), H_faraday(E3f, r, t, mu0, 1e-5))
num("21.3f <S> by Faraday + time average [W/m^2]", S3f, [0, 0, 400/(240*np.pi)], atol=1e-7)
num("21.3f |<S>| (page 0.531; claim 400/(120 pi))", [S3f[2], 400/(120*np.pi)], [0.531, 1.06], rtol=2e-3)
key['f'] = bool(np.isclose(S3f[2], 400/(120*np.pi), rtol=1e-3))
v, be = c/2, 2*np.pi
w = be*v
t = tgrid(w, 2048)
worst = 0.0
for P in (lambda r: np.array([(2 + 1.5j)*np.exp(-1j*be*r[2]), 0, 0]),       # toward +z, E along x
          lambda r: np.array([0, 0, (-1 + 2j)*np.exp(1j*be*r[1])])):          # toward -y, E along z
    F = from_phasor(P, w)
    for rr in ([0, 0, 0], [0.2, -0.4, 0.31], [0.5, 0.77, -0.2]):
        rr = np.array(rr, float)
        PE = phasor(F(rr, t), t, w)
        PH = phasor(H_faraday(F, rr, t, mu0, 1e-5), t, w)
        iE, iH = np.argmax(abs(PE)), np.argmax(abs(PH))
        worst = max(worst, abs(np.imag(PH[iH]/PE[iE]))/abs(PH[iH]/PE[iE]))
small("21.3g single lossless wave: H~/E~ is real at every point (|Im/abs| of the ratio)", worst, 1e-6)
key['g'] = worst < 1e-6
same("21.3 key (a)-(g)", ''.join('T' if key[k] else 'F' for k in 'abcdefg'), 'FFTTFFT')

# =========================================================================== 21.4
print("\n=== 21.4 Which electric field ===")
num("21.4 eta = sqrt(9 mu0/eps0) [ohm]", [np.sqrt(9*mu0/eps0), np.sqrt(9*mu0/eps0)/np.pi], [1131, 360], rtol=1e-3)
num("21.4 144 pi", 144*np.pi, 452, rtol=1e-3)
for fs in (1e8, 7e6):
    w = 2*np.pi*fs
    mu, eps = 9*mu0, eps0
    v = 1/np.sqrt(mu*eps)
    be = w/v
    lam = 2*np.pi/be
    H4 = lambda r, t, w=w, be=be: np.array([0*np.atleast_1d(t),
                                            np.real(-0.4j*np.exp(1j*(w*np.atleast_1d(t) + be*r[2]))),
                                            0*np.atleast_1d(t)])
    t = tgrid(w, 2048)
    opts = {'a': lambda z, t: -144*np.pi*np.sin(w*t + be*z), 'b': lambda z, t: 144*np.pi*np.sin(w*t + be*z),
            'c': lambda z, t: -144*np.pi*np.cos(w*t + be*z), 'd': lambda z, t: -48*np.pi*np.sin(w*t + be*z)}
    errs = {k: 0.0 for k in opts}
    for z in (0.0, 0.37*lam, 0.81*lam):
        rr = np.array([0, 0, z])
        E = E_ampere(H4, rr, t, eps, 1e-4*lam)
        sc = np.max(abs(E[0]))
        for k, fn in opts.items():
            errs[k] = max(errs[k], np.max(abs(E[0] - fn(z, t)))/sc, np.max(abs(E[1:]))/sc)
    best = min(errs, key=errs.get)
    print(f"      f = {fs:.0e} Hz: relative mismatch of each option with the Ampere-integrated E: "
          + ", ".join(f"({k}) {e:.2e}" for k, e in errs.items()))
    same(f"21.4 key at f = {fs:.0e} Hz", best, 'a')
    small(f"21.4 option (a) matches (f = {fs:.0e})", errs['a'], 1e-5)
    Ea = lambda r, t, w=w, be=be: np.array([-144*np.pi*np.sin(w*np.atleast_1d(t) + be*r[2]),
                                            0*np.atleast_1d(t), 0*np.atleast_1d(t)])
    rF, rA = maxwell_res(Ea, H4, eps, mu, np.array([0, 0, 0.3*lam]), w, 1e-4*lam)
    small(f"21.4 (a) with the given H: Faraday and Ampere residuals (f = {fs:.0e})", max(rF, rA), 1e-5)
same("21.4 direction of the given H (rigid translation)", travel(H4, v, w)[0], '-z')
# what each distractor is (page's explanations), and its power flow
t = tgrid(w, 2048)
eta = np.sqrt(mu/eps)
Ht = lambda z: -0.4j*np.exp(1j*be*z)*np.array([0, 1, 0])
zs = 0.29*lam
Hg = H4(np.array([0, 0, zs]), t)
mk = lambda Ev: np.real(Ev[:, None]*np.exp(1j*w*t))
Eb1 = mk(eta*np.cross(Ht(zs), [0, 0, 1]))                  # rotate with u = +z
Eb2 = mk(eta*np.cross([0, 0, -1], Ht(zs)))                 # u x H instead of H x u
Ec = mk(eta*np.cross(0.4*np.exp(1j*be*zs)*np.array([0, 1, 0]), [0, 0, -1]))   # -j dropped
Ed = mk(eta0*np.cross(Ht(zs), [0, 0, -1]))                 # eta0 instead of eta
small("21.4 distractor (b) = rotation with u=+z", np.max(abs(Eb1[0] - opts['b'](zs, t)))/452, 1e-9)
small("21.4 distractor (b) = eta u x H~", np.max(abs(Eb2[0] - opts['b'](zs, t)))/452, 1e-9)
small("21.4 distractor (c) = -j dropped", np.max(abs(Ec[0] - opts['c'](zs, t)))/452, 1e-9)
small("21.4 distractor (d) = eta0 used", np.max(abs(Ed[0] - opts['d'](zs, t)))/150, 1e-9)
num("21.4 <E x H> of keyed (a) [z-comp, sign]", np.sign(S_avg(mk(np.array([144j*np.pi*np.exp(1j*be*zs), 0, 0])), Hg)[2]), -1)
num("21.4 <E x H> of (b) with the given H points +z", np.sign(S_avg(Eb1, Hg)[2]), 1)
num("21.4 <E x H> of (c) with the given H is zero", S_avg(Ec, Hg), [0, 0, 0], atol=1e-9)
num("21.4 v_p/c in the material", v/c, 1/3)

# =========================================================================== 21.5
print("\n=== 21.5 The power that flowed backward ===")
be = 2*np.pi
w = be*c
t = tgrid(w, 2048)
E5p = lambda r: np.array([6, 8j, 0])*np.exp(-1j*be*r[2])
E5 = from_phasor(E5p, w)
Hs_p = lambda r: np.array([-8j, 6, 0])/eta0*np.exp(-1j*be*r[2])      # the student's H
Hs = from_phasor(Hs_p, w)
errH, Sv = 0.0, []
for z in (0.0, 0.13, 0.37):
    rr = np.array([0, 0, z])
    Hb = H_faraday(E5, rr, t, mu0, 1e-5)
    errH = max(errH, np.max(abs(Hb - Hs(rr, t)))/np.max(abs(Hb)))
    Sv.append(S_avg(E5(rr, t), Hb))
small("21.5 student's H~ agrees with the Faraday-integrated H", errH, 1e-6)
num("21.5 <S> at z = 0, 0.13, 0.37 m [W/m^2]", np.array(Sv), [[0, 0, 50/eta0]]*3, atol=1e-9)
num("21.5 <S>_z = 50/eta0 = 5/(12 pi) ~ 0.133", [Sv[0][2], 5/(12*np.pi)], [0.133, 50/eta0], rtol=3e-3)
for lbl, msk, pg in (('x', [1, 0, 0], 0.048), ('y', [0, 1, 0], 0.085)):
    Fm = lambda r, t, m=np.array(msk, float): E5(r, t)*m[:, None]
    rr = np.array([0, 0, 0.21])
    num(f"21.5 power of the {lbl} part alone [W/m^2]", S_avg(Fm(rr, t), H_faraday(Fm, rr, t, mu0, 1e-5))[2], pg,
        rtol=1e-2)
nc = lambda z: 0.5*np.real(np.cross(E5p(np.array([0, 0, z])), Hs_p(np.array([0, 0, z]))))[2]
num("21.5 student's (no conjugate) value at z=0 [W/m^2]", nc(0.0), -0.0371, rtol=2e-3)
num("21.5 student's expression = -(14/eta0)cos(4 pi z) at z=0.05, 0.125", [nc(0.05), nc(0.125)],
    [-14/eta0*np.cos(4*np.pi*0.05), 0], atol=1e-12)
num("21.5 E0.E0 (no conjugate)", np.dot([6, 8j, 0], [6, 8j, 0]), -28)

# =========================================================================== 21.6
print("\n=== 21.6 Radio waves in a plasma ===")
e, me, e0 = 1.602e-19, 9.109e-31, 8.854e-12
N6 = 4.47e11
wp = np.sqrt(N6*e**2/(me*e0))
num("21.6a omega_p [rad/s]", wp, 3.77e7, rtol=1e-3)
num("21.6a f_p [MHz]", wp/2/np.pi/1e6, 6.00, rtol=1e-3)
num("21.6a shortcut 8.98 sqrt(N) [MHz]", 8.98*np.sqrt(N6)/1e6, 6.00, rtol=1e-3)
trav = [f"{f/1e6:g} MHz" for f in (4e6, 10e6, 100e6) if (2*np.pi*f)**2 - wp**2 > 0]
same("21.6b frequencies with real beta", trav, ['10 MHz', '100 MHz'])
f = 10e6
w = 2*np.pi*f
be6 = np.sqrt(w**2 - wp**2)/c
num("21.6c sqrt(1 - fp^2/f^2)", np.sqrt(1 - (wp/w)**2), 0.8, rtol=1e-3)
num("21.6c omega/c [rad/m]", w/c, np.pi/15)
num("21.6c beta [rad/m] vs 4pi/75 (page uses fp = 6.00 exactly)", be6, 4*np.pi/75, rtol=1e-3)
rounded("21.6c beta [rad/m]", be6, ['0.168'])
num("21.6c lambda [m]", 2*np.pi/be6, 37.5, rtol=1e-3)
num("21.6c v_p [m/s], v_p/c", [w/be6, w/be6/c], [3.75e8, 1.25], rtol=1e-3)
num("21.6c free-space lambda [m]", c/f, 30)
w100 = 2*np.pi*100e6
num("21.6c 100 MHz: fp^2/f^2, v_p/c", [(wp/w100)**2, w100/np.sqrt(w100**2 - wp**2)], [0.0036, 1.0018], rtol=2e-3)
om = lambda b: np.sqrt(wp**2 + (b*c)**2)
hb = be6*1e-5
vg = (om(be6 + hb) - om(be6 - hb))/(2*hb)
num("21.6d v_g = d omega/d beta (numerical) [m/s]", vg, 2.4e8, rtol=1e-3)
num("21.6d v_g/c", vg/c, 0.8, rtol=1e-3)
num("21.6d v_p v_g = c^2", (w/be6)*vg, c**2, rtol=1e-6)
num("21.6d crossing times [ms]: group, light", [150e3/vg*1e3, 150e3/c*1e3], [0.625, 0.500], rtol=1e-3)
# brute force: a narrowband packet around 10 MHz crossing 150 km, envelope peak arrival time
df = np.linspace(-20e3, 20e3, 401)
wk = 2*np.pi*(f + df)
Ak = np.exp(-df**2/(2*4e3**2))*np.exp(-1j*np.sqrt(wk**2 - wp**2)/c*150e3)
tt = np.arange(0.40e-3, 0.85e-3, 0.1e-6)
env = np.abs(np.exp(1j*np.outer(tt, wk - w)) @ Ak)
k = np.argmax(env)
tpk = tt[k] + 0.5*(env[k-1] - env[k+1])/(env[k-1] - 2*env[k] + env[k+1])*(tt[1] - tt[0])
num("21.6d packet envelope arrival after 150 km [ms] (brute force)", tpk*1e3, 0.625, rtol=2e-3)

# =========================================================================== 21.7
print("\n=== 21.7 Partner fields on three axes ===")
h = 1e-5
be = 2*np.pi
w = be*c
t = tgrid(w, 2048)
E7a = from_phasor(lambda r: np.array([0, 6*np.exp(-1j*be*r[0]), 0]), w)
same("21.7a direction (rigid translation)", travel(E7a, c, w)[0], '+x')
num("21.7a f [MHz]", w/2/np.pi/1e6, 300)
err = 0.0
for x in (0.0, 0.3):
    rr = np.array([x, 0, 0])
    Hb = H_faraday(E7a, rr, t, mu0, h)
    err = max(err, np.max(abs(Hb - np.array([0*t, 0*t, np.cos(w*t - be*x)/(20*np.pi)])))*20*np.pi)
    S7a = S_avg(E7a(rr, t), Hb)
small("21.7a H = (1/(20 pi))cos(wt - 2 pi x) z (Faraday)", err, 1e-5)
PH = phasor(H_faraday(E7a, np.zeros(3), t, mu0, h), t, w)
num("21.7a H~ at x=0 [mA/m]", PH*1e3, [0, 0, 15.9], rtol=2e-3, atol=1e-9)
num("21.7a <S> [W/m^2]", S7a, [0.0477, 0, 0], rtol=2e-3, atol=1e-9)
num("21.7a <S> = 3/(20 pi)", S7a[0], 3/(20*np.pi), rtol=1e-6)
v = c/3
be = np.pi
w = be*v
eps = 9*eps0
t = tgrid(w, 2048)
H7b = from_phasor(lambda r: np.array([0.1j*np.exp(1j*be*r[1]), 0, 0]), w)
same("21.7b direction (rigid translation)", travel(H7b, v, w)[0], '-y')
num("21.7b lambda [m], f [MHz]", [2*np.pi/be, w/2/np.pi/1e6], [2, 50])
num("21.7b eta [ohm]", np.sqrt(mu0/eps), 40*np.pi)
err = errg = 0.0
for y in (0.0, 0.45):
    rr = np.array([0, y, 0])
    Eb = E_ampere(H7b, rr, t, eps, h)
    err = max(err, np.max(abs(Eb - np.array([0*t, 0*t, 4*np.pi*np.sin(w*t + be*y)])))/(4*np.pi))
    errg = max(errg, np.max(abs(H7b(rr, t)[0] + 0.1*np.sin(w*t + be*y)))/0.1)
    S7b = S_avg(Eb, H7b(rr, t))
small("21.7b E = 4 pi sin(wt + pi y) z (Ampere)", err, 1e-5)
small("21.7b given H = -0.1 sin(wt + pi y) x", errg, 1e-12)
PE = phasor(E_ampere(H7b, np.zeros(3), t, eps, h), t, w)
num("21.7b E~ at y=0 [V/m]", PE, [0, 0, -4j*np.pi], rtol=1e-5, atol=1e-6)
rounded("21.7b E amplitude [V/m]", abs(PE[2]), ['12.6'])
num("21.7b E~ x H~* at y=0", np.cross(PE, np.conj([0.1j, 0, 0])), [0, -0.4*np.pi, 0], rtol=1e-5, atol=1e-6)
num("21.7b <S> [W/m^2]", S7b, [0, -0.628, 0], rtol=2e-3, atol=1e-9)
P7c = lambda r: np.array([0, 0, 5*np.exp(1j*(1.2*np.pi*r[0] - 1.6*np.pi*r[1]))])
hh = 1e-4
abc = np.array([np.angle(P7c(hh*ev)[2]/P7c(-hh*ev)[2])/(2*hh) for ev in np.eye(3)])
be = np.linalg.norm(abc)
u = -abc/be
num("21.7c beta [rad/m]", be, 2*np.pi)
num("21.7c u", u, [-0.6, 0.8, 0], atol=1e-9)
w = be*c
t = tgrid(w, 2048)
E7c = from_phasor(P7c, w)
same("21.7c direction (rigid translation among +-u and the axes)",
     travel(E7c, c, w, cands={'u': u, '-u': -u, **AXES})[0], 'u')
amp = 5/(120*np.pi)
err = 0.0
for rr in (np.zeros(3), np.array([0.2, -0.3, 0.1])):
    Hb = H_faraday(E7c, rr, t, mu0, h)
    ph = w*t + 1.2*np.pi*rr[0] - 1.6*np.pi*rr[1]
    err = max(err, np.max(abs(Hb - amp*np.array([0.8*np.cos(ph), 0.6*np.cos(ph), 0*ph])))/amp)
    S7c = S_avg(E7c(rr, t), Hb)
small("21.7c H = (5/120pi)(0.8x + 0.6y)cos(wt + 1.2pi x - 1.6pi y) (Faraday)", err, 1e-5)
PH = phasor(H_faraday(E7c, np.zeros(3), t, mu0, h), t, w)
num("21.7c H~ at origin [mA/m]", PH*1e3, [10.6, 7.96, 0], rtol=2e-3, atol=1e-9)
num("21.7c <S> [W/m^2]", S7c, [-0.0199, 0.0265, 0], rtol=3e-3, atol=1e-9)
num("21.7c |<S>| = 5/(48 pi)", [np.linalg.norm(S7c), 5/(48*np.pi)], [0.0332, np.linalg.norm(S7c)], rtol=2e-3)

# =========================================================================== 21.8
print("\n=== 21.8 A driven electron in phasors ===")
N8, E08, f = 1e12, 0.2, 20e6
w = 2*np.pi*f
T = 1/f
sol = integrate.solve_ivp(lambda tt, vv: [-e*E08*np.cos(w*tt)/me], (0, 3*T), [0.0], rtol=1e-12, atol=1e-12,
                          dense_output=True)
t = 2*T + tgrid(w, 4096)
vx = sol.sol(t)[0]
vx = vx - vx.mean()                     # steady state: remove the free drift (no static part)
Vt = phasor(vx, t, w)
num("21.8 omega [rad/s]", w, 1.257e8, rtol=1e-3)
num("21.8a |v~| [m/s]", abs(Vt), 280, rtol=1e-3)
num("21.8a phase of v relative to E [deg] (+90 = leads)", np.angle(Vt)/DEG, 90)
small("21.8a v(t) = -280 sin wt (rel. error; 280 rounds 279.9)", np.max(abs(vx + 280*np.sin(w*t)))/280, 1e-3)
Jx = -N8*e*vx
Jt = phasor(Jx, t, w)
num("21.8b J0 [A/m^2]", abs(Jt), 4.48e-5, rtol=1e-3)
num("21.8b phase of J relative to E [deg] (-90 = lags)", np.angle(Jt)/DEG, -90)
small("21.8b J(t) = 44.8 sin wt uA/m^2 (rel. error)", np.max(abs(Jx - 44.8e-6*np.sin(w*t)))/44.8e-6, 2e-3)
num("21.8b <J.E> (sampled) / (J0 E0 / 2)", np.mean(Jx*E08*np.cos(w*t))/(abs(Jt)*E08/2), 0, atol=1e-6)
dt = 1e-6*T
Jd = e0*E08*(np.cos(w*(t + dt)) - np.cos(w*(t - dt)))/(2*dt)
Jdt = phasor(Jd, t, w)
rounded("21.8c displacement amplitude [uA/m^2]", abs(Jdt)*1e6, ['223'])
num("21.8c phase(J) - phase(eps0 dE/dt) [deg] (antiphase)", (np.angle(Jt) - np.angle(Jdt))/DEG, -180)
ratio = abs(Jt)/abs(Jdt)
wp8 = np.sqrt(N8*e**2/(me*e0))
rounded("21.8c amplitude ratio", ratio, ['0.202'])
num("21.8c ratio = wp^2/w^2", ratio, (wp8/w)**2, rtol=1e-6)
num("21.8c eps_eff/eps0", 1 - ratio, 0.798, rtol=1e-3)
num("21.8c J~ + j w eps0 E~ = j w eps0 (1 - wp^2/w^2) E~", Jt + Jdt, 1j*w*e0*(1 - wp8**2/w**2)*E08, rtol=1e-6)
be8 = w/c*np.sqrt(1 - ratio)
num("21.8c beta [rad/m]", be8, 0.374, rtol=2e-3)
num("21.8c beta = sqrt(w^2 - wp^2)/c", be8, np.sqrt(w**2 - wp8**2)/c, rtol=1e-6)
num("21.8c (w/c), sqrt(eps_eff)", [w/c, np.sqrt(1 - ratio)], [0.419, 0.894], rtol=2e-3)
num("21.8c lambda [m]", 2*np.pi/be8, 16.8, rtol=3e-3)
num("21.8c v_p [m/s], v_p/c", [w/be8, w/be8/c], [3.36e8, 1.12], rtol=2e-3)
rounded("21.8 check f_p [MHz], (f_p/f)^2", [wp8/2/np.pi/1e6, (wp8/w)**2], ['8.98', '0.202'])
mu0p = 1/(e0*c**2)


def wave_res(beta):
    Ef = lambda z, tt: E08*np.cos(w*tt - beta*z)
    Jf = lambda z, tt: np.real(Jt*np.exp(1j*(w*tt - beta*z)))   # the measured electron current, local response
    hz, ht = 1e-3/beta, 1e-3/w
    res = sc = 0.0
    for z in (0.0, 3.3, 7.1):
        for tt in np.linspace(0, T, 9):
            d2z = (Ef(z + hz, tt) - 2*Ef(z, tt) + Ef(z - hz, tt))/hz**2
            d2t = (Ef(z, tt + ht) - 2*Ef(z, tt) + Ef(z, tt - ht))/ht**2
            dJ = (Jf(z, tt + ht) - Jf(z, tt - ht))/(2*ht)
            res = max(res, abs(d2z - mu0p*e0*d2t - mu0p*dJ))
            sc = max(sc, abs(d2z))
    return res/sc


small("21.8c wave equation with the electron current holds at beta = 0.374", wave_res(be8), 1e-4)
rep("21.8c ... and fails at the vacuum beta = w/c", wave_res(w/c) > 0.1, f"residual {wave_res(w/c):.2e}")

# =========================================================================== 21.9
print("\n=== 21.9 A phasor from two snapshots ===")
u = np.array([-4, 3, 0])/5
f = 1e8
w = 2*np.pi*f
T = 1/f
v = c/1.5
eps = 2.25*eps0
be = w/v
lam = 2*np.pi/be
num("21.9a beta [rad/m], lambda [m]", [be, lam], [np.pi, 2])
num("21.9a eta [ohm]", [np.sqrt(mu0/eps), np.sqrt(mu0/eps)], [80*np.pi, 251], rtol=2e-3)
a0, b0 = np.array([0, 0, 4.0]), np.array([3, 4, 0.0])        # E(0,0) and E(0,T/4)
num("21.9b snapshots . u", [a0 @ u, b0 @ u], [0, 0], atol=1e-12)
E9 = lambda r, t: (a0[:, None]*np.cos(w*(np.atleast_1d(t) - u @ np.asarray(r, float)/v))
                   + b0[:, None]*np.sin(w*(np.atleast_1d(t) - u @ np.asarray(r, float)/v)))
t = tgrid(w, 2048)
P0 = phasor(E9(np.zeros(3), t), t, w)
num("21.9b (A, B, C) [V/m]", P0, [-3j, -4j, 4], atol=1e-9)
abc = np.array([np.angle(phasor(E9(hh*ev, t), t, w)[2]/phasor(E9(-hh*ev, t), t, w)[2])/(2*hh) for ev in np.eye(3)])
num("21.9a (a, b, c) [rad/m] (measured phase gradient)", abc, [0.8*np.pi, -0.6*np.pi, 0], atol=1e-6)
num("21.9a (a, b, c) decimals", abc, [2.51, -1.88, 0], rtol=3e-3, atol=1e-6)
tm = lambda r: np.array([-3j, -4j, 4])*np.exp(1j*(0.8*np.pi*r[0] - 0.6*np.pi*r[1]))
rng = np.random.default_rng(9)
small("21.9 template reproduces the measured phasor at random points",
      max(np.max(abs(phasor(E9(rr, t), t, w) - tm(rr))) for rr in rng.uniform(-2, 2, (8, 3))), 1e-9)
small("21.9b E(0,t) = (3x+4y)sin wt + 4z cos wt",
      np.max(abs(E9(np.zeros(3), t) - (b0[:, None]*np.sin(w*t) + a0[:, None]*np.cos(w*t)))), 1e-12)
Hpg = from_phasor(lambda r: np.array([2.4, 3.2, 5j])/(80*np.pi)*np.exp(1j*(0.8*np.pi*r[0] - 0.6*np.pi*r[1])), w)
err = 0.0
for rr in (np.zeros(3), np.array([0.3, -0.2, 0.5])):
    Hb = H_faraday(E9, rr, t, mu0, h)
    err = max(err, np.max(abs(Hb - Hpg(rr, t)))/np.max(abs(Hb)))
    S9 = S_avg(E9(rr, t), Hb)
small("21.9c page H~ = (2.4, 3.2, 5j)/(80pi) e^{j(...)} vs Faraday-integrated H", err, 1e-6)
PH = phasor(H_faraday(E9, np.zeros(3), t, mu0, h), t, w)
num("21.9c H~ at origin [mA/m]", PH*1e3, [9.55, 12.7, 19.9j], rtol=3e-3)
num("21.9c |H~0| = sqrt(41)/(80 pi)", np.linalg.norm(PH), np.sqrt(41)/(80*np.pi), rtol=1e-6)
num("21.9d <S> [W/m^2]", S9, [-0.0653, 0.0489, 0], rtol=3e-3, atol=1e-9)
num("21.9d |<S>|, 41/(160 pi)", [np.linalg.norm(S9), 41/(160*np.pi)], [0.0816, np.linalg.norm(S9)], rtol=2e-3)
num("21.9d <S> along u", S9/np.linalg.norm(S9), u, atol=1e-6)
rr = np.array([0.4, 0.1, -0.3])
for lbl, msk, pg in (('z part', [0, 0, 1], 0.0318), ('xy part', [1, 1, 0], 0.0497)):
    Fm = lambda r, t, m=np.array(msk, float): E9(r, t)*m[:, None]
    Sm = S_avg(Fm(rr, t), H_faraday(Fm, rr, t, mu0, h))
    num(f"21.9d power of the {lbl} alone [W/m^2]", np.linalg.norm(Sm), pg, rtol=2e-3)
Pp = np.array([1, 0.5, 0])
num("21.9e u.r_P [m] (= -lambda/4)", u @ Pp, -0.5)
num("21.9e E(P, 0) [V/m]", E9(Pp, 0.0)[:, 0], [3, 4, 0], atol=1e-9)
num("21.9e E(0, T/4) [V/m]", E9(np.zeros(3), T/4)[:, 0], [3, 4, 0], atol=1e-9)

# =========================================================================== 21.10
print("\n=== 21.10 Two sheets, two current directions ===")
v = c/2
f = 75e6
w = 2*np.pi*f
be = w/v
lam = 2*np.pi/be
d = lam/4
eta = eta0/2
eps = 4*eps0
num("21.10a beta, lambda, d, eta/pi", [be, lam, d, eta/np.pi], [np.pi, 2, 0.5, 60])
JA = lambda t: np.array([2*np.cos(w*t), 0*t, 0*t])
JB = lambda t: np.array([0*t, np.sin(w*t), 0*t])
t = tgrid(w, 2048)
num("21.10a J~_A, J~_B (measured)", [phasor(JA(t)[0], t, w), phasor(JB(t)[1], t, w)], [2, -1j], atol=1e-12)


def sheets(lst):
    """Lecture 19 in the time domain: E = -(eta/2) J_s(t - |z - z_s|/v), H = (1/2) J_s(t - |z - z_s|/v) x n"""
    def E(r, t):
        t = np.atleast_1d(t)
        out = np.zeros((3, t.size))
        for zs, J in lst:
            out += -eta/2*J(t - abs(r[2] - zs)/v)
        return out

    def H(r, t):
        t = np.atleast_1d(t)
        out = np.zeros((3, t.size))
        for zs, J in lst:
            n = np.array([0, 0, np.sign(r[2] - zs)])
            out += 0.5*np.cross(J(t - abs(r[2] - zs)/v).T, n).T
        return out
    return E, H


EA, HA = sheets([(0.0, JA)])
EB, HB = sheets([(d, JB)])
E10, H10 = sheets([(0.0, JA), (d, JB)])
pg = {'A': (lambda z: -60*np.pi*np.exp(-1j*be*abs(z))*np.array([1, 0, 0]),
            lambda z: -np.sign(z)*np.exp(-1j*be*abs(z))*np.array([0, 1, 0])),
      'B': (lambda z: 30j*np.pi*np.exp(-1j*be*abs(z - d))*np.array([0, 1, 0]),
            lambda z: -np.sign(z - d)*0.5j*np.exp(-1j*be*abs(z - d))*np.array([1, 0, 0]))}
err = 0.0
for nm, (Ef, Hf) in (('A', (EA, HA)), ('B', (EB, HB))):
    for z in (-0.7, -0.1, 0.2, 0.4, 0.6, 1.3):
        rr = np.array([0, 0, z])
        err = max(err, np.max(abs(phasor(Ef(rr, t), t, w) - pg[nm][0](z)))/(30*np.pi),
                  np.max(abs(phasor(Hf(rr, t), t, w) - pg[nm][1](z)))/0.5)
small("21.10b each sheet alone: page E~ and H~ on both sides vs measured phasors", err, 1e-9)
reg = {'below': lambda z: -60*np.pi*np.exp(1j*be*z)*np.array([1, -0.5, 0]),
       'between': lambda z: -60*np.pi*np.exp(-1j*be*z)*np.array([1, 0, 0]) + 30*np.pi*np.exp(1j*be*z)*np.array([0, 1, 0]),
       'above': lambda z: -60*np.pi*np.exp(-1j*be*z)*np.array([1, 0.5, 0])}
zr = {'below': (-0.7, -0.2), 'between': (0.1, 0.35), 'above': (0.6, 1.3)}
Sreg = {}
for nm in reg:
    err = 0.0
    for z in zr[nm]:
        rr = np.array([0, 0, z])
        err = max(err, np.max(abs(phasor(E10(rr, t), t, w) - reg[nm](z)))/(60*np.pi))
        Sreg[nm] = S_avg(E10(rr, t), H10(rr, t))
    small(f"21.10c total E~ {nm} the sheets (page formula vs measured phasor)", err, 1e-9)
z = 0.83
Pz = phasor(E10(np.array([0, 0, z]), t), t, w)
num("21.10c P [V/m], Q", [Pz[0]*np.exp(1j*be*z), Pz[1]/Pz[0]], [-60*np.pi, 0.5], atol=1e-9)
num("21.10c P decimal", np.real(Pz[0]*np.exp(1j*be*z)), -188.5, rtol=1e-3)
num("21.10d <S>_z below, between, above [/pi]", [Sreg['below'][2]/np.pi, Sreg['between'][2]/np.pi, Sreg['above'][2]/np.pi],
    [-37.5, 22.5, 37.5])
num("21.10d decimals [W/m^2]", [Sreg['above'][2], Sreg['between'][2]], [118, 70.7], rtol=3e-3)
num("21.10d transverse <S> components vanish", [Sreg[k][:2] for k in Sreg], np.zeros((3, 2)), atol=1e-9)
num("21.10e total E~(0), E~(d) [/pi]", [phasor(E10(np.zeros(3), t), t, w)/np.pi,
                                        phasor(E10(np.array([0, 0, d]), t), t, w)/np.pi],
    [[-60, 30, 0], [60j, 30j, 0]], atol=1e-9)
pA = avg_quad(lambda th: float(-JA(np.array([th/w])).T[0] @ E10(np.zeros(3), np.array([th/w]))[:, 0]))
pB = avg_quad(lambda th: float(-JB(np.array([th/w])).T[0] @ E10(np.array([0, 0, d]), np.array([th/w]))[:, 0]))
num("21.10e <-J_A.E>, <-J_B.E> by quad [W/m^2]", [pA, pB], [188.5, 47.1], rtol=2e-3)
num("21.10e ... in units of pi", [pA/np.pi, pB/np.pi, (pA + pB)/np.pi], [60, 15, 75], rtol=1e-6)
num("21.10e outflow S(above) - S(below) [/pi], total [W/m^2]", [(Sreg['above'][2] - Sreg['below'][2])/np.pi, pA + pB],
    [75, 236], rtol=2e-3)
num("21.10e steps of S across A and across B [/pi]", [(Sreg['between'][2] - Sreg['below'][2])/np.pi,
                                                      (Sreg['above'][2] - Sreg['between'][2])/np.pi], [60, 15])
num("21.10e alone: eta J0^2/4 [/pi]", [eta*4/4/np.pi, eta*1/4/np.pi], [60, 15])
t1 = np.linspace(0, 1/f, 64, endpoint=False)
jA = np.cross([0, 0, 1], (H10(np.array([0, 0, 1e-10]), t1) - H10(np.array([0, 0, -1e-10]), t1)).T).T
jB = np.cross([0, 0, 1], (H10(np.array([0, 0, d + 1e-10]), t1) - H10(np.array([0, 0, d - 1e-10]), t1)).T).T
small("21.10 check: z x (H+ - H-) = J_s at both sheets", max(np.max(abs(jA - JA(t1))), np.max(abs(jB - JB(t1)))), 1e-6)
small("21.10 check: tangential E continuous at both sheets",
      max(np.max(abs(E10(np.array([0, 0, 1e-10]), t1) - E10(np.array([0, 0, -1e-10]), t1))),
          np.max(abs(E10(np.array([0, 0, d + 1e-10]), t1) - E10(np.array([0, 0, d - 1e-10]), t1))))/188, 1e-6)
small("21.10 check: H~_B is continuous at z=0 and equals x/2 there",
      abs(phasor(HB(np.zeros(3) + [0, 0, 1e-12], t), t, w)[0] - 0.5), 1e-9)
small("21.10 check: curl equations in each region", max(max(maxwell_res(E10, H10, eps, mu0, np.array([0, 0, z]), w, 1e-5))
                                                          for z in (-0.6, 0.27, 1.1)), 1e-6)
JBp = lambda t: np.array([np.sin(w*t), 0*t, 0*t])
E10f, H10f = sheets([(0.0, JA), (d, JBp)])
Sup = S_avg(E10f(np.array([0, 0, 0.9]), t), H10f(np.array([0, 0, 0.9]), t))
Sdn = S_avg(E10f(np.array([0, 0, -0.4]), t), H10f(np.array([0, 0, -0.4]), t))
num("21.10f <S>_z above, below [/pi]", [Sup[2]/np.pi, Sdn[2]/np.pi], [67.5, -7.5])
num("21.10f decimals [W/m^2]", [Sup[2], Sdn[2]], [212, -23.6], rtol=3e-3)
num("21.10f E~ above and below [/pi]", [phasor(E10f(np.array([0, 0, 0.9]), t), t, w)[0]*np.exp(1j*be*0.9)/np.pi,
                                        phasor(E10f(np.array([0, 0, -0.4]), t), t, w)[0]*np.exp(-1j*be*(-0.4))/np.pi],
    [-90, -30], atol=1e-9)
qA = avg_quad(lambda th: float(-JA(np.array([th/w])).T[0] @ E10f(np.zeros(3), np.array([th/w]))[:, 0]))
qB = avg_quad(lambda th: float(-JBp(np.array([th/w])).T[0] @ E10f(np.array([0, 0, d]), np.array([th/w]))[:, 0]))
num("21.10f deliveries A, B, total [/pi]", [qA/np.pi, qB/np.pi, (qA + qB)/np.pi], [30, 45, 75], rtol=1e-6)
num("21.10f per-side powers no longer the sum of the separate ones: above (separate 30pi+7.5pi)",
    [Sup[2]/np.pi, (Sreg['above'][2])/np.pi], [67.5, 37.5])

# =========================================================================== 21.11
print("\n=== 21.11 Two waves on one line ===")
v = c/3
f = 1e8
w = 2*np.pi*f
be = w/v
eta = eta0/3
eps = 9*eps0
num("21.11a beta, lambda, eta/pi", [be, 2*np.pi/be, eta/np.pi], [2*np.pi, 1, 40])


def E11(r, t):
    tt = np.atleast_1d(t)
    return np.array([6*np.cos(w*tt - be*r[2]) + 2*np.sin(w*tt + be*r[2]), 0*tt, 0*tt])


t = tgrid(w, 2048)
pgEp = lambda z: 6*np.exp(-1j*be*z) - 2j*np.exp(1j*be*z)
pgHp = lambda z: (6*np.exp(-1j*be*z) + 2j*np.exp(1j*be*z))/eta
err = errp = 0.0
Ss, crs = [], []
for z in np.linspace(0, 1, 7):
    rr = np.array([0, 0, z])
    Hb = H_faraday(E11, rr, t, mu0, h)
    pgH = (47.7e-3*np.cos(w*t - be*z) - 15.9e-3*np.sin(w*t + be*z))
    err = max(err, np.max(abs(Hb[1] - (6/eta*np.cos(w*t - be*z) - 2/eta*np.sin(w*t + be*z))))*eta/8,
              np.max(abs(Hb[[0, 2]]))*eta)
    errp = max(errp, abs(phasor(E11(rr, t)[0], t, w) - pgEp(z))/8, abs(phasor(Hb[1], t, w) - pgHp(z))*eta/8)
    Ss.append(S_avg(E11(rr, t), Hb)[2])
    crs.append(phasor(E11(rr, t)[0], t, w)*np.conj(phasor(Hb[1], t, w)) - (32 - 24j*np.cos(2*be*z))/eta)
small("21.11a H(z,t) = (6/eta)cos(wt - bz) - (2/eta)sin(wt + bz) (Faraday)", err, 1e-6)
small("21.11a page E~ and H~ formulas vs measured phasors", errp, 1e-6)
num("21.11a 6/eta, 2/eta [mA/m]", [6/eta*1e3, 2/eta*1e3], [47.7, 15.9], rtol=2e-3)
num("21.11b <S>_z at 7 points in 0..1 m [W/m^2]", Ss, [16/eta]*7, rtol=1e-6)
num("21.11b 16/eta = 0.4/pi", [16/eta, 0.4/np.pi], [0.127, 16/eta], rtol=3e-3)
small("21.11b E~ H~* = (32 - 24j cos 2bz)/eta (max abs deviation)", np.max(np.abs(crs)), 1e-6)
num("21.11b forward and backward powers [W/m^2]", [36/(2*eta), 4/(2*eta)], [0.143, 0.0159], rtol=3e-3)
zg = np.linspace(0, 0.5, 1001)[:-1]
t5 = tgrid(w, 256)
Em = np.array([abs(phasor(E11(np.array([0, 0, z]), t5)[0], t5, w)) for z in zg])
Hm = np.array([abs(phasor(H_faraday(E11, np.array([0, 0, z]), t5, mu0, h)[1], t5, w)) for z in zg])
num("21.11c |E~| max at z, value; min at z, value", [zg[Em.argmax()], Em.max(), zg[Em.argmin()], Em.min()],
    [0.125, 8, 0.375, 4], rtol=1e-4)
num("21.11c |H~| max at z, value [mA/m]; min at z, value", [zg[Hm.argmax()], Hm.max()*1e3, zg[Hm.argmin()], Hm.min()*1e3],
    [0.375, 63.7, 0.125, 31.8], rtol=2e-3)
num("21.11c |E~|/|H~| at 0.125 and 0.375 m, in units of eta", [Em[250]/Hm[250]/eta, Em[750]/Hm[750]/eta], [2, 0.5],
    rtol=1e-3)
we, wm = [], []
for z in zg[::50]:
    rr = np.array([0, 0, z])
    we.append(np.mean(0.5*eps*E11(rr, t)[0]**2))
    wm.append(np.mean(0.5*mu0*H_faraday(E11, rr, t, mu0, h)[1]**2))
we, wm = np.array(we), np.array(wm)
num(f"21.11d <w_e> + <w_m> at {len(we)} points = 20 eps [nJ/m^3]", (we + wm)*1e9, [20*eps*1e9]*len(we), rtol=1e-5)
num("21.11d 20 eps [nJ/m^3]", 20*eps*1e9, 1.59, rtol=3e-3)
num("21.11d <w_e> range = 4 eps .. 16 eps (eps0 = 1/(mu0 c^2), consistent with c, eta0 given)",
    [we.min()/eps, we.max()/eps], [4, 16], rtol=1e-5)
print(f"      INFO 16 eps = 144 eps0: {144*eps0*1e9:.5f} (c, eta0 given) | {144*8.854e-12*1e9:.5f} (eps0 = 8.854e-12)"
      f" | {144*8.8541878128e-12*1e9:.5f} (SI) nJ/m^3 -> old page value 1.28 only with full SI eps0;"
      f" 4 eps: {36*eps0*1e9:.4f} | {36*8.854e-12*1e9:.4f} (old page 0.319)")
for e0x in (eps0, 8.854e-12):
    rounded(f"21.11d FIXED range 'about 0.32 and 1.27 nJ/m^3' with eps0 = {e0x:.4e}", [36*e0x*1e9, 144*e0x*1e9],
            ['0.32', '1.27'])
    rounded(f"21.11d 20 eps = 180 eps0 with eps0 = {e0x:.4e}", 180*e0x*1e9, ['1.59'])
num("21.11d <S>/<w> [m/s], in units of v", [16/eta/(20*eps), 16/eta/(20*eps)/v], [8e7, 0.8])
num("21.11d v<w> = 20/eta", v*20*eps, 20/eta)
tf = tgrid(w, 200000)
Sz = E11(np.zeros(3), tf)[0]*H_faraday(E11, np.zeros(3), tf, mu0, h)[1]
neg = Sz < 0
k = np.where(np.diff(neg.astype(int)) != 0)[0]
num("21.11e fraction of the period with S_z < 0", neg.mean(), 0.205, rtol=3e-3)
num("21.11e 1 - (2/pi) atan 3", 1 - 2/np.pi*np.arctan(3), neg.mean(), rtol=1e-4)
num("21.11e first negative window [deg of wt]", (w*tf[k[:2]] + 0.5*w*(tf[1] - tf[0]))/DEG, [71.6, 108.4], rtol=1e-3)
num("21.11e min, max of S_z [W/m^2]", [Sz.min(), Sz.max()], [-0.0318, 0.286], rtol=3e-3)
num("21.11e average of S_z = 16/eta", Sz.mean(), 16/eta, rtol=1e-6)
small("21.11 check: curl equations (finite differences)",
      max(maxwell_res(E11, lambda r, t: np.array([0*np.atleast_1d(t), (6*np.cos(w*np.atleast_1d(t) - be*r[2])
                                                                     - 2*np.sin(w*np.atleast_1d(t) + be*r[2]))/eta,
                                                0*np.atleast_1d(t)]), eps, mu0, np.array([0, 0, 0.3]), w, 1e-5)), 1e-6)

# =========================================================================== 21.12
print("\n=== 21.12 A medium from phasor readings ===")
f = 25e6
w = 2*np.pi*f
T = 1/f
dz = 0.25
E_0, E_25, H_0 = 37.7*np.exp(30j*DEG), 37.7*np.exp(75j*DEG), 0.2*np.exp(30j*DEG)
t = tgrid(w, 2048)
Et = np.array([0*t, np.real(E_0*np.exp(1j*w*t)), 0*t])
Ht = np.array([np.real(H_0*np.exp(1j*w*t)), 0*t, 0*t])
S0 = S_avg(Et, Ht)
same("21.12a direction from the time average of E x H at z=0", '-z' if S0[2] < 0 else '+z', '-z')
num("21.12a (E~ x H~*)_z", np.cross([0, E_0, 0], np.conj([H_0, 0, 0]))[2], -7.54, rtol=1e-3)
sols = []
for name, sg in (('+z', 1), ('-z', -1)):
    for kk in range(-4, 5):
        bb = -sg*(45*DEG + 2*np.pi*kk)/dz      # phase(0.25) - phase(0) = -sg*beta*dz = 45 deg + 360k
        if bb > 0 and dz < np.pi/bb:
            sols.append((name, round(bb/np.pi, 9)))
same("21.12a/b (direction, beta/pi) allowed by the phases and spacing < lambda/2", sols, [('-z', 1.0)])
bz_plus = min(-(45*DEG + 2*np.pi*kk)/dz for kk in range(-4, 5) if -(45*DEG + 2*np.pi*kk)/dz > 0)
num("21.12a FIXED remark: +z would need a 315 deg lag, beta >= 7pi, lambda/2 = 1/7 m < 0.25 m",
    [bz_plus/np.pi, np.pi/bz_plus], [7, 1/7])
be = np.pi
vp = w/be
num("21.12b beta, lambda, v_p, c/v_p", [be, 2*np.pi/be, vp, c/vp], [np.pi, 2, 5e7, 6])
eta = abs(E_0)/abs(H_0)
num("21.12b eta [ohm], eta/eta0", [eta, eta/eta0], [188.5, 0.5], rtol=1e-3)
mr, er = optimize.fsolve(lambda p: [p[0]*p[1] - (c/vp)**2, p[0]/p[1] - (eta/eta0)**2], [1.0, 1.0])
num("21.12b (mu_r, eps_r)", [mr, er], [3, 12], rtol=1e-3)
mu, eps = 3*mu0, 12*eps0


def E12(r, t):
    tt = np.atleast_1d(t)
    return np.array([0*tt, 37.7*np.cos(w*tt + be*r[2] + 30*DEG), 0*tt])


def H12(r, t):
    tt = np.atleast_1d(t)
    return np.array([0.2*np.cos(w*tt + be*r[2] + 30*DEG), 0*tt, 0*tt])


small("21.12c curl equations with mu = 3mu0, eps = 12eps0 (37.7/0.2 vs exact eta: 2e-5)",
      max(maxwell_res(E12, H12, eps, mu, np.array([0, 0, 0.3]), w, 1e-4)), 1e-3)
PHb = phasor(H_faraday(E12, np.zeros(3), t, mu, 1e-4)[0], t, w)
num("21.12c Faraday-integrated H~(0): magnitude, phase [deg]", [abs(PHb), np.angle(PHb)/DEG], [0.2, 30], rtol=1e-3)
num("21.12c phase of E at z=0.25 [deg]", np.angle(phasor(E12(np.array([0, 0, 0.25]), t)[1], t, w))/DEG, 75)
num("21.12c omega [rad/s]", w, 5*np.pi*1e7)
S12 = S_avg(E12(np.array([0, 0, -4]), t), H12(np.array([0, 0, -4]), t))
num("21.12d <S> at z=-4 [W/m^2]", S12, [0, 0, -3.77], rtol=1e-3, atol=1e-9)
num("21.12d 1.2 pi", 1.2*np.pi, 3.77, rtol=1e-3)
num("21.12d power through 1 m x 2 m [W]", abs(S12[2])*2, 7.54, rtol=1e-3)
Pm = phasor(E12(np.array([0, 0, -0.5]), t)[1], t, w)
num("21.12e phasor at z=-0.5: magnitude, phase [deg]", [abs(Pm), np.angle(Pm)/DEG], [37.7, -60])
num("21.12e T/4 [ns]", T/4*1e9, 10)
small("21.12e E(-0.5, t) = E(0, t - T/4)", np.max(abs(E12(np.array([0, 0, -0.5]), t) - E12(np.zeros(3), t - T/4))), 1e-9)
cz0 = crests(lambda z: E12(np.array([0, 0, 0]), 0.0)[1]*0 + 37.7*np.cos(be*z + 30*DEG), -2, 0)
num("21.12e crests on -2<z<0 at t=0 [m]", cz0, [-1/6], rtol=1e-6)
cz1 = crests(lambda z: 37.7*np.cos(w*T/4 + be*z + 30*DEG), -2, 0)
num("21.12e same crest a quarter period later [m]", cz1, [-0.667], rtol=1e-3)
num("21.12 watch-out: non-magnetic eps_r=36: eta [ohm], c/v_p", [eta0/6, np.sqrt(36)], [62.8, 6], rtol=1e-3)

print(f"\nTOTAL: {tally['PASS']} PASS, {tally['FAIL']} FAIL")
