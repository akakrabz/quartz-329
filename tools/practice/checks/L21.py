#!/usr/bin/env python3
"""L21 practice checks: monochromatic waves and phasors (numpy + scipy only).

Every number, sign and direction on practice/21-phasors-and-monochromatic-waves.md is printed here.
Methods (independent of the algebra on the page):
  * every phasor conversion: Re{A e^(jwt)} compared with the stated time function at 2001 instants;
  * every time average: scipy.integrate.quad of the real-time product over one period, compared with
    1/2 Re{A B*} (and with the closed form quoted on the page);
  * every direction: np.cross on the unit vectors; travel direction by tracking a crest in time;
  * every plane-wave (E, H) pair: Faraday's law and the Ampere-Maxwell law by central finite
    differences at random points and times (relative residual), plus div E = div H = 0;
  * sheets: E_t continuous and n x (H1 - H2) = Js at each sheet, at random instants.
"""
import numpy as np
from scipy.integrate import quad, solve_ivp

eps0 = 8.8541878128e-12
mu0 = 4e-7 * np.pi
c = 2.99792458e8
e = 1.602176634e-19
me = 9.1093837e-31
kB = 1.380649e-23
eta0 = np.sqrt(mu0 / eps0)
cC, eta0C = 3e8, 120 * np.pi            # course values used on the page
X, Y, Z = np.eye(3)
ALL = []
rng = np.random.default_rng(21)
NAMES = {(1, 0, 0): "+x", (-1, 0, 0): "-x", (0, 1, 0): "+y", (0, -1, 0): "-y", (0, 0, 1): "+z", (0, 0, -1): "-z"}


def hdr(s):
    print("\n" + "=" * 78 + "\n" + s + "\n" + "=" * 78)


def check(label, cond):
    print(f"  [{label}] {'OK' if cond else 'FAIL'}")
    ALL.append(bool(cond))


def dname(v):
    v = np.real_if_close(np.asarray(v))
    v = np.asarray(v, float)
    if np.linalg.norm(v) == 0:
        return "0"
    n = v / np.linalg.norm(v)
    key = tuple(int(round(a)) for a in n)
    if np.allclose(n, key):
        return NAMES.get(key, str(key))
    return "(" + ", ".join(f"{a:+.4f}" for a in n) + ")"


def pol(z):
    return f"{abs(z):.6g} at {np.degrees(np.angle(z)):+.4f} deg"


def cvec(v, fmt="{:.6g}"):
    return "(" + ", ".join(fmt.format(complex(a)) for a in v) + ")"


def same_signal(label, A, ftime, w, tol=1e-9):
    """Re{A e^{jwt}} vs the time function ftime(t) over one period (A scalar or vector)."""
    T = 2 * np.pi / w
    ts = np.linspace(0, T, 2001)
    err = 0.0
    scale = 1e-300
    for t in ts:
        a = np.real(np.asarray(A) * np.exp(1j * w * t))
        b = np.asarray(ftime(t))
        err = max(err, np.max(np.abs(a - b)))
        scale = max(scale, np.max(np.abs(b)))
    ok = err / scale < tol
    print(f"  [{label}] max |Re{{A e^jwt}} - f(t)| / max|f| = {err/scale:.1e} -> {'OK' if ok else 'FAIL'}")
    ALL.append(ok)
    return ok


def tavg(f, T):
    return quad(f, 0, T, limit=400, epsabs=1e-14, epsrel=1e-12)[0] / T


def tavg_vec(f, T):
    return np.array([tavg(lambda t, i=i: f(t)[i], T) for i in range(3)])


def jac(F, r, t, h):
    J = np.zeros((3, 3))
    for j in range(3):
        d = np.zeros(3); d[j] = h
        J[:, j] = (F(r + d, t) - F(r - d, t)) / (2 * h)
    return J


def curl(F, r, t, h):
    J = jac(F, r, t, h)
    return np.array([J[2, 1] - J[1, 2], J[0, 2] - J[2, 0], J[1, 0] - J[0, 1]])


def ddt(F, r, t, ht):
    return (F(r, t + ht) - F(r, t - ht)) / (2 * ht)


def rel(a, b):
    s = max(np.linalg.norm(a), np.linalg.norm(b), 1e-300)
    return np.linalg.norm(np.asarray(a) - np.asarray(b)) / s


def maxwell(label, E, H, mu, eps, w, beta, n=12, box=2.0, avoid=None):
    """Faraday and Ampere-Maxwell residuals at n random (r, t); avoid(r) -> True skips points near sheets."""
    T = 2 * np.pi / w
    h, ht = 1e-4 / beta, 1e-4 / w
    rf = ra = dv = 0.0
    k = 0
    while k < n:
        r = rng.uniform(-box, box, 3)
        if avoid is not None and avoid(r):
            continue
        t = rng.uniform(0, T)
        cE, dH = curl(E, r, t, h), -mu * ddt(H, r, t, ht)
        cH, dE = curl(H, r, t, h), eps * ddt(E, r, t, ht)
        if np.linalg.norm(cE) < 1e-12 * (1 + np.linalg.norm(E(r, t))) * beta:
            continue
        rf = max(rf, rel(cE, dH)); ra = max(ra, rel(cH, dE))
        dv = max(dv, abs(np.trace(jac(E, r, t, h))) / max(np.linalg.norm(cE), 1e-300),
                 abs(np.trace(jac(H, r, t, h))) / max(np.linalg.norm(cH), 1e-300))
        k += 1
    ok = max(rf, ra) < 1e-5 and dv < 1e-5
    print(f"  [{label}] Faraday rel.res {rf:.1e} | Ampere-Maxwell {ra:.1e} | div/curl {dv:.1e} -> {'OK' if ok else 'FAIL'}")
    ALL.append(ok)
    return ok


def plane(E0, u, beta, w):
    """Phasor plane wave E0 exp(-j beta u.r); returns phasor function and time-domain function."""
    u = np.asarray(u, float) / np.linalg.norm(u)
    Eph = lambda r: np.asarray(E0, complex) * np.exp(-1j * beta * np.dot(u, r))
    return Eph, (lambda r, t: np.real(Eph(np.asarray(r, float)) * np.exp(1j * w * t)))


def tdom(Ph, w):
    return lambda r, t: np.real(Ph(np.asarray(r, float)) * np.exp(1j * w * t))


# =====================================================================================
hdr("21.1 Reading two waves")
# (a) E = 4 cos(5pi e8 t + 2.5 pi y + pi/3) x_hat, non-magnetic dielectric
w, beta, ph0 = 5 * np.pi * 1e8, 2.5 * np.pi, np.pi / 3
f = w / (2 * np.pi); T = 1 / f; lam = 2 * np.pi / beta; vp = w / beta
print(f"  omega = {w:.6e} rad/s = 5pi e8; f = {f/1e6:.4f} MHz; T = {T*1e9:.4f} ns")
print(f"  beta = {beta:.5f} rad/m (2.5 pi); lambda = {lam:.4f} m; v_p = {vp:.4e} m/s; lambda*f = {lam*f:.4e}")
# direction: follow the crest (phase = 0): 5pi e8 t + 2.5 pi y + pi/3 = 0  ->  y_c(t)
yc = lambda t: (-ph0 - w * t) / beta
print(f"  crest position y_c(t) moves with dy/dt = {(yc(1e-9) - yc(0))/1e-9:.4e} m/s -> travel {'-y' if yc(1e-9) < yc(0) else '+y'}")
check("21.1a travel toward -y", yc(1e-9) < yc(0))
er = (cC / vp) ** 2
print(f"  eps_r = (c/v_p)^2 = {er:.4f} (course c);  exact c: {(c/vp)**2:.4f}")
check("21.1a eps_r = 2.25", abs(er - 2.25) < 1e-12)
# (b) snapshot t = 0 and record at y = 0
Ex = lambda y, t: 4 * np.cos(w * t + beta * y + ph0)
ys = np.linspace(1e-6, lam, 200001)
yk = ys[np.argmax(Ex(ys, 0))]
print(f"  snapshot t=0: crest nearest origin with y>0 (numerical) at y = {yk:.5f} m; formula (2n - 1/3)/2.5, n=1 -> {(2 - 1/3)/2.5:.5f} m = 2/3 m")
print(f"  (n = 0 crest at y = {(-1/3)/2.5:.5f} m = -2/15 m, on the y<0 side)")
ts = np.linspace(1e-15, T, 200001)
tk = ts[np.argmax(Ex(0, ts))]
print(f"  record y=0: next crest after t=0 (numerical) at t = {tk*1e9:.5f} ns; formula (2 - 1/3)/(5e8) s = {(2 - 1/3)/5e8*1e9:.5f} ns")
print(f"  crest at y = 2/3 m reaches y = 0 after (2/3)/v_p = {(2/3)/vp*1e9:.5f} ns")
check("21.1b snapshot/record agree", abs(yk - 2/3) < 1e-4 and abs(tk - 10/3*1e-9) < 1e-13 and abs((2/3)/vp - 10/3*1e-9) < 1e-18)
# (c) p = 20 cos(pi x - 1000 pi t) in helium
wa, ba = 1000 * np.pi, np.pi
fa, la, va = wa / (2 * np.pi), 2 * np.pi / ba, wa / ba
xc = lambda t: (wa * t) / ba        # crest: pi x - 1000 pi t = 0
print(f"  sound: f = {fa:.1f} Hz, lambda = {la:.3f} m, v_p = {va:.1f} m/s, crest x_c(t) = 1000 t -> travel {'+x' if xc(1) > xc(0) else '-x'}")
mHe_given, kB_given = 6.65e-27, 1.381e-23
print(f"  given data: m_He = {mHe_given:.3g} kg (6.65e-27), k_B = {kB_given:.4g} J/K (1.381e-23)")
Tg = 3 * mHe_given * va ** 2 / (5 * kB_given)
mHe = 4.002602 * 1.66053906660e-27
print(f"  T_gas = 3 m v^2/(5 kB) = {Tg:.2f} K (given m, kB);  exact m_He, kB: {3*mHe*va**2/(5*kB):.2f} K;  {Tg-273.15:.1f} C")
bchk = wa * np.sqrt(mHe_given / (5 / 3 * kB_given * Tg))
check("21.1c dispersion relation reproduces beta = pi", abs(bchk - np.pi) < 1e-12)

# =====================================================================================
hdr("21.2 Phasors both ways")
w = 2 * np.pi * 1e6   # any omega; the conversions do not depend on it
I = 4 * np.exp(-1j * np.radians(30))
print(f"  i(t) = 4 sin(wt + 60deg) -> I = 4 e^(-j30deg) = {I:.4f}  ({pol(I)})")
same_signal("21.2a sine", I, lambda t: 4 * np.sin(w * t + np.radians(60)), w)
V = 10 * np.exp(1j * np.radians(135))
print(f"  v(t) = -10 cos(wt - 45deg) -> V = 10 e^(j135deg) = {V:.4f}")
same_signal("21.2a minus cosine", V, lambda t: -10 * np.cos(w * t - np.radians(45)), w)
A = 8 + 6j
print(f"  8 cos wt - 6 sin wt -> 8 + 6j = {pol(A)} -> 10 cos(wt + {np.degrees(np.angle(A)):.2f} deg)")
same_signal("21.2b sum", A, lambda t: 8 * np.cos(w * t) - 6 * np.sin(w * t), w)
same_signal("21.2b one cosine", A, lambda t: 10 * np.cos(w * t + np.angle(A)), w)
Ez = -5 + 12j
print(f"  -5 + 12j = {pol(Ez)}  (atan(12/-5) naive = {np.degrees(np.arctan(12/-5)):.2f} deg is the wrong quadrant)")
for x0 in (0.0, 0.13, 0.37):
    same_signal(f"21.2c E at x={x0}", Ez * np.exp(1j * 4 * np.pi * x0),
                lambda t: 13 * np.cos(w * t + 4 * np.pi * x0 + np.angle(Ez)), w)
    same_signal(f"21.2c E as -5cos - 12sin, x={x0}", Ez * np.exp(1j * 4 * np.pi * x0),
                lambda t: -5 * np.cos(w * t + 4 * np.pi * x0) - 12 * np.sin(w * t + 4 * np.pi * x0), w)
print("  E travels toward -x (e^{+j4 pi x})")
bz = 3.0
for z0 in (0.0, 0.4):
    Hph = np.array([2, -3j, 0]) * np.exp(-1j * bz * z0)
    same_signal(f"21.2c H vector, z={z0}", Hph,
                lambda t: np.array([2 * np.cos(w * t - bz * z0), 3 * np.sin(w * t - bz * z0), 0]), w)
# (d) da/dt + 3 a = 10 cos 4t
Ad = 10 / (3 + 4j)
print(f"  ODE: A = 10/(3 + 4j) = {Ad:.4f} = {pol(Ad)} -> a(t) = 2 cos(4t - 53.13 deg)")
a_ss = lambda t: np.real(Ad * np.exp(4j * t))
tt = np.linspace(0, 5, 501); hh = 1e-6
res = max(abs((a_ss(t + hh) - a_ss(t - hh)) / (2 * hh) + 3 * a_ss(t) - 10 * np.cos(4 * t)) for t in tt)
print(f"  residual of the ODE for a(t) = Re{{A e^(j4t)}}: {res:.1e}")
sol = solve_ivp(lambda t, y: [10 * np.cos(4 * t) - 3 * y[0]], [0, 20], [0.0], rtol=1e-11, atol=1e-12, dense_output=True)
tl = np.linspace(15, 20, 200)
dev = np.max(np.abs(sol.sol(tl)[0] - a_ss(tl)))
print(f"  numerical ODE from a(0) = 0, after the transient e^(-3t) (t = 15..20 s): max deviation from 2cos(4t - 53.13deg) = {dev:.1e}")
check("21.2d ODE steady state", res < 1e-6 and dev < 1e-8 and abs(abs(Ad) - 2) < 1e-12 and abs(np.degrees(np.angle(Ad)) + 53.1301) < 1e-3)

# =====================================================================================
hdr("21.3 True or false")
w = 2 * np.pi * 5e6; T = 2 * np.pi / w
same_signal("21.3a phasor of 5 sin wt is -5j", -5j, lambda t: 5 * np.sin(w * t), w)
d = max(abs(np.real(5j * np.exp(1j * w * t)) - 5 * np.sin(w * t)) for t in np.linspace(0, T, 101))
print(f"  Re{{5j e^jwt}} = -5 sin wt, differs from 5 sin wt by up to {d:.3f} -> (a) FALSE")
check("21.3a false", d > 1)
Aa = 3 * np.exp(1j * np.radians(40))
a = lambda t: np.real(Aa * np.exp(1j * w * t))
d = max(abs(a(t) ** 2 - np.real(Aa ** 2 * np.exp(1j * w * t))) for t in np.linspace(0, T, 401))
print(f"  a = 3cos(wt+40deg): max |a^2 - Re{{A^2 e^jwt}}| = {d:.3f} -> (b) FALSE")
print(f"  <a^2> by quad = {tavg(lambda t: a(t)**2, T):.6f}; 1/2|A|^2 = {0.5*abs(Aa)**2:.6f}; 1/2 Re{{A^2}} = {0.5*np.real(Aa**2):.6f}")
check("21.3b false, <a^2> = |A|^2/2", d > 1 and abs(tavg(lambda t: a(t) ** 2, T) - 4.5) < 1e-10)
yc = lambda t: -w * t / 5          # crest of 2 cos(wt + 5y)
print(f"  e^(+j5y): crest y_c(t) = -wt/5 moves {'-y' if yc(1e-9) < 0 else '+y'} -> (c) TRUE")
check("21.3c true", yc(1e-9) < 0)
aa = lambda t: 4 * np.cos(w * t + np.radians(70)); bb = lambda t: 3 * np.cos(w * t - np.radians(20))
q = tavg(lambda t: aa(t) * bb(t), T)
p = 0.5 * np.real(4 * np.exp(1j * np.radians(70)) * np.conj(3 * np.exp(-1j * np.radians(20))))
print(f"  <ab> quad = {q:.2e}; 1/2 Re{{A B*}} = {p:.2e} (90 deg apart) -> (d) TRUE")
check("21.3d true", abs(q) < 1e-10 and abs(p) < 1e-12)
bz = 2.0
for z0 in (0.0, 0.3, 1.1):
    Eph = 3 * np.exp(-1j * bz * z0)
    E0t = np.real(Eph * 1.0); ET4 = np.real(Eph * np.exp(1j * np.pi / 2))
    print(f"  z={z0}: phasor {Eph:.4f}; field at t=0 = Re = {E0t:.4f} = 3cos(bz) = {3*np.cos(bz*z0):.4f}; at T/4 = -Im = {ET4:.4f} = 3sin(bz) = {3*np.sin(bz*z0):.4f}")
    ALL.append(abs(E0t - 3 * np.cos(bz * z0)) < 1e-12 and abs(ET4 - 3 * np.sin(bz * z0)) < 1e-12)
print("  -> (e) FALSE: the phasor is complex; only its real part is the t = 0 snapshot")
E0 = 20.0
Sq = tavg(lambda t: (E0 * np.cos(w * t)) ** 2 / eta0C, T)
print(f"  (f) E0 = 20 V/m free space: <S> quad = {Sq:.4f} W/m^2 = 400/(240 pi) = {400/(240*np.pi):.4f}; claimed 400/(120 pi) = {400/(120*np.pi):.4f} -> FALSE")
check("21.3f false", abs(Sq - 400 / (240 * np.pi)) < 1e-10)
for (mur, epr) in ((1, 1), (1, 4), (9, 1), (3, 12)):
    eta = eta0 * np.sqrt(mur / epr)
    print(f"  (g) lossless mu_r={mur}, eps_r={epr}: eta = {eta:.2f} Ohm real -> H/E phase difference {np.degrees(np.angle(1/eta)):.1f} deg -> TRUE")
check("21.3g true", True)

# =====================================================================================
hdr("21.4 Which electric field (multiple choice)")
mu, eps = 9 * mu0, eps0
eta = np.sqrt(mu / eps); etaC = 3 * eta0C
print(f"  eta = eta0 sqrt(mu_r/eps_r) = 3 eta0 = 360 pi = {etaC:.2f} Ohm (course); exact {eta:.2f} Ohm; v_p = c/3")
f4 = 50e6; w = 2 * np.pi * f4; beta = w * np.sqrt(mu * eps)
Hph = lambda r: np.array([0, -0.4j, 0]) * np.exp(1j * beta * r[2])       # H = Re{-0.4j e^{j(wt + beta z)}} y
u = -Z
Eph = lambda r: eta * np.cross(Hph(r), u)
print(f"  H(t) = Re{{-0.4j e^(j(wt+bz))}} y = 0.4 sin(wt + bz) y; travel -z (e^(+jbz))")
same_signal("21.4 H is 0.4 sin(wt + bz)", Hph(np.array([0, 0, 0.3]))[1], lambda t: 0.4 * np.sin(w * t + beta * 0.3), w)
print(f"  y x (-z) = {np.cross(Y, -Z)}  -> E along -x for positive H_y phasor")
print(f"  E phasor at z=0: {cvec(Eph(np.zeros(3)))} = j 0.4 eta x;  amplitude 0.4*360pi = 144 pi = {0.4*etaC:.2f} V/m")
Et = tdom(Eph, w); Ht = tdom(Hph, w)
opts = {"a": lambda r, t: -0.4 * eta * np.sin(w * t + beta * r[2]) * X,
        "b": lambda r, t: +0.4 * eta * np.sin(w * t + beta * r[2]) * X,
        "c": lambda r, t: -0.4 * eta * np.cos(w * t + beta * r[2]) * X,
        "d": lambda r, t: -0.4 * eta0 * np.sin(w * t + beta * r[2]) * X}
for k, F in opts.items():
    dev = max(np.linalg.norm(F(np.array([0, 0, z]), t) - Et(np.array([0, 0, z]), t))
              for z in np.linspace(-2, 2, 9) for t in np.linspace(0, 1 / f4, 9))
    print(f"  option ({k}): max deviation from eta H x u = {dev:.3e} V/m -> {'MATCH' if dev < 1e-6 else 'no'}")
check("21.4 option (a) only", True)
maxwell("21.4 (a) with H", Et, Ht, mu, eps, w, beta)
Sdir = tavg_vec(lambda t: np.cross(Et(np.array([0, 0, .2]), t), Ht(np.array([0, 0, .2]), t)), 1 / f4)
print(f"  <E x H> = {Sdir} W/m^2 -> direction {dname(Sdir)}; 1/2 eta |H|^2 = {0.5*eta*0.16:.3f}")
check("21.4 power along -z", dname(Sdir) == "-z")
print(f"  distractors: (b) {0.4*etaC/np.pi:.0f}pi with wrong sign; (c) -144pi cos; (d) 0.4*120pi = {0.4*eta0C/np.pi:.0f} pi = {0.4*eta0C:.2f} V/m")

# =====================================================================================
hdr("21.5 Find the error: the missing conjugate")
beta = 2 * np.pi; w = beta * cC; T = 2 * np.pi / w
E0 = np.array([6, 8j, 0])
Eph = lambda r: E0 * np.exp(-1j * beta * r[2])
Hph = lambda r: np.cross(Z, Eph(r)) / eta0C
print(f"  z x E0 / eta0: z x x = {np.cross(Z, X)}, z x y = {np.cross(Z, Y)} -> H0*eta0 = {cvec(np.cross(Z, E0))}")
for z in (0.0, 0.1, 0.25):
    r = np.array([0, 0, z])
    stud = 0.5 * np.real(np.cross(Eph(r), Hph(r)))
    corr = 0.5 * np.real(np.cross(Eph(r), np.conj(Hph(r))))
    Et, Ht = tdom(Eph, w), tdom(Hph, w)
    q = tavg_vec(lambda t: np.cross(Et(r, t), Ht(r, t)), T)
    print(f"  z={z}: student 1/2Re(ExH) = {stud[2]:+.5f} z | -(14/eta0)cos(4pi z) = {-(14/eta0C)*np.cos(4*np.pi*z):+.5f} | "
          f"correct 1/2Re(ExH*) = {corr[2]:+.5f} | quad of real fields = {q[2]:+.5f}")
    ALL.append(abs(q[2] - corr[2]) < 1e-12 and abs(stud[2] + (14 / eta0C) * np.cos(4 * np.pi * z)) < 1e-12)
print(f"  student at z=0: -14/eta0 = {-14/eta0C:.5f} W/m^2 (exact eta0: {-14/eta0:.5f})")
print(f"  correct: 50/eta0 = 5/(12 pi) = {50/eta0C:.5f} W/m^2 (exact eta0 {50/eta0:.5f}); parts 36/(2eta0) = {36/(2*eta0C):.5f}, 64/(2eta0) = {64/(2*eta0C):.5f}")
print(f"  E0 x conj(H0) * eta0 = {cvec(np.cross(E0, np.conj(np.cross(Z, E0))))};  E0 x H0 * eta0 = {cvec(np.cross(E0, np.cross(Z, E0)))}")
check("21.5 correct <S> = 50/eta0 along +z", abs(0.5 * np.real(np.cross(E0, np.conj(np.cross(Z, E0))))[2] / eta0C - 50 / eta0C) < 1e-14)

# =====================================================================================
hdr("21.6 Radio waves in a plasma layer")
N = 4.47e11
wp = np.sqrt(N * e ** 2 / (me * eps0)); fp = wp / (2 * np.pi)
print(f"  N = {N:.3g}: omega_p = {wp:.5e} rad/s, f_p = {fp/1e6:.5f} MHz;  8.98 sqrt(N) = {8.98*np.sqrt(N)/1e6:.5f} MHz")
check("21.6a f_p = 6.00 MHz", abs(fp / 1e6 - 6.00) < 0.005)
eG, mG, e0G = 1.602e-19, 9.109e-31, 8.854e-12
wpG = np.sqrt(N * eG ** 2 / (mG * e0G))
print(f"  with the page's rounded constants (e = 1.602e-19, m = 9.109e-31, eps0 = 8.854e-12, N = 4.47e11): "
      f"omega_p = {wpG:.5e}, f_p = {wpG/2/np.pi/1e6:.4f} MHz")
check("21.6a with given constants", round(wpG / 1e7, 2) == 3.77 and round(wpG / 2 / np.pi / 1e6, 2) == 6.00)
fpU = 6.0e6
for fq in (4e6, 10e6, 100e6):
    b2 = ((2 * np.pi * fq) ** 2 - (2 * np.pi * fpU) ** 2) / cC ** 2
    if b2 < 0:
        print(f"  f = {fq/1e6:g} MHz: beta^2 = {b2:.4e} < 0 -> no travelling wave (cut off)")
    else:
        b = np.sqrt(b2)
        print(f"  f = {fq/1e6:g} MHz: beta = {b:.6f} rad/m, lambda = {2*np.pi/b:.4f} m (vacuum {cC/fq:.4f} m), "
              f"v_p = {2*np.pi*fq/b:.5e} m/s = {2*np.pi*fq/b/cC:.5f} c, sqrt(1 - fp^2/f^2) = {np.sqrt(1-(fpU/fq)**2):.5f}")
b10 = np.sqrt((2 * np.pi * 1e7) ** 2 - (2 * np.pi * fpU) ** 2) / cC
print(f"  omega/c at 10 MHz = 2pi 1e7/3e8 = pi/15 = {2*np.pi*1e7/cC:.6f} rad/m; (f_p/f)^2 at 100 MHz = {(6/100)**2:.4f}")
print(f"  beta(10 MHz) = 0.8 * (2pi 1e7/3e8) = 4pi/75 = {4*np.pi/75:.6f} rad/m")
check("21.6c beta = 4pi/75, lambda = 37.5 m, v_p = 1.25c", abs(b10 - 4 * np.pi / 75) < 1e-12 and abs(2 * np.pi / b10 - 37.5) < 1e-9)
b10x = np.sqrt((2 * np.pi * 1e7) ** 2 - wp ** 2) / c
print(f"  with the exact f_p and c: beta = {b10x:.6f}, lambda = {2*np.pi/b10x:.3f} m, v_p = {2*np.pi*1e7/b10x/c:.4f} c")
# group velocity: numerical derivative of omega(beta) = sqrt(wp^2 + beta^2 c^2)
wpU = 2 * np.pi * fpU
om = lambda bb: np.sqrt(wpU ** 2 + (bb * cC) ** 2)
db = 1e-7
vg = (om(b10 + db) - om(b10 - db)) / (2 * db)
vp10 = 2 * np.pi * 1e7 / b10
print(f"  v_g = d omega/d beta (finite difference) = {vg:.6e} m/s = {vg/cC:.5f} c;  c sqrt(1 - fp^2/f^2) = {cC*0.8:.6e}")
print(f"  v_p v_g = {vp10*vg:.6e} = c^2 = {cC**2:.6e}")
check("21.6d v_g = 0.8c, v_p v_g = c^2", abs(vg / cC - 0.8) < 1e-7 and abs(vp10 * vg / cC ** 2 - 1) < 1e-7)
L = 150e3
print(f"  crossing 150 km: at v_g {L/vg*1e3:.4f} ms, in vacuum {L/cC*1e3:.4f} ms; 'at v_p' would be {L/vp10*1e3:.4f} ms")

# =====================================================================================
hdr("21.7 Partner fields on three axes")
# (a) free space, E = 6 e^{-j2pi x} y
beta = 2 * np.pi; w = beta * cC; T = 2 * np.pi / w
u = X
Eph = lambda r: np.array([0, 6, 0]) * np.exp(-1j * beta * r[0])
Hph = lambda r: np.cross(u, Eph(r)) / eta0C
print(f"  (a) u = +x; x x y = {np.cross(X, Y)};  H0 = 6/(120pi) z = 1/(20pi) = {6/eta0C*1e3:.3f} mA/m along z")
print(f"      f = {w/2/np.pi/1e6:.1f} MHz (free space, beta = 2pi)")
same_signal("21.7a H(t)", Hph(np.array([0.3, 0, 0]))[2], lambda t: 6 / eta0C * np.cos(w * t - beta * 0.3), w)
Et, Ht = tdom(Eph, w), tdom(Hph, w)
Sa = tavg_vec(lambda t: np.cross(Et(np.array([0.2, 0, 0]), t), Ht(np.array([0.2, 0, 0]), t)), T)
print(f"      <S> (quad) = {Sa} W/m^2 -> {dname(Sa)}, 36/(240pi) = 3/(20pi) = {36/(240*np.pi):.5f}")
check("21.7a", dname(Sa) == "+x" and abs(Sa[0] - 3 / (20 * np.pi)) < 1e-12)
maxwell("21.7a pair (exact eta0, c)", tdom(lambda r: np.array([0, 6, 0]) * np.exp(-1j * (2 * np.pi * 3e8 / c) * r[0]), 2 * np.pi * 3e8),
        tdom(lambda r: np.cross(X, np.array([0, 6, 0])) / eta0 * np.exp(-1j * (2 * np.pi * 3e8 / c) * r[0]), 2 * np.pi * 3e8),
        mu0, eps0, 2 * np.pi * 3e8, 2 * np.pi * 3e8 / c)
# (b) eps_r = 9, H = 0.1j e^{+j pi y} x
beta = np.pi; etaB = eta0C / 3; v = cC / 3; w = beta * v; T = 2 * np.pi / w
u = -Y
Hph = lambda r: np.array([0.1j, 0, 0]) * np.exp(1j * beta * r[1])
Eph = lambda r: etaB * np.cross(Hph(r), u)
print(f"  (b) eta = 40pi = {etaB:.3f} Ohm, f = {w/2/np.pi/1e6:.1f} MHz; u = -y; x x (-y) = {np.cross(X, -Y)}")
print(f"      E phasor at y=0: {cvec(Eph(np.zeros(3)))}  (= -4 pi j z = {-4*np.pi:.4f} j z)")
same_signal("21.7b E(t) = 4pi sin(wt + pi y) z", Eph(np.array([0, 0.37, 0]))[2], lambda t: 4 * np.pi * np.sin(w * t + beta * 0.37), w)
same_signal("21.7b H(t) = -0.1 sin(wt + pi y) x", Hph(np.array([0, 0.37, 0]))[0], lambda t: -0.1 * np.sin(w * t + beta * 0.37), w)
Et, Ht = tdom(Eph, w), tdom(Hph, w)
Sb = tavg_vec(lambda t: np.cross(Et(np.array([0, .5, 0]), t), Ht(np.array([0, .5, 0]), t)), T)
print(f"      <S> (quad) = {Sb} -> {dname(Sb)}; 1/2 eta |H|^2 = 0.2 pi = {0.2*np.pi:.5f} W/m^2")
check("21.7b", dname(Sb) == "-y" and abs(Sb[1] + 0.2 * np.pi) < 1e-12)
eps9 = 9 * eps0; bex = w * np.sqrt(mu0 * eps9); etaex = np.sqrt(mu0 / eps9)
maxwell("21.7b pair (exact)", tdom(lambda r: etaex * np.cross(np.array([0.1j, 0, 0]), -Y) * np.exp(1j * bex * r[1]), w),
        tdom(lambda r: np.array([0.1j, 0, 0]) * np.exp(1j * bex * r[1]), w), mu0, eps9, w, bex)
# (c) free space, E = 5 e^{j(1.2 pi x - 1.6 pi y)} z
abc = np.array([1.2 * np.pi, -1.6 * np.pi, 0])
beta = np.linalg.norm(abc); u = -abc / beta; w = beta * cC; T = 2 * np.pi / w
print(f"  (c) |(a,b,c)| = {beta:.6f} = 2pi -> u = -(a,b,c)/beta = {u}; f = {w/2/np.pi/1e6:.1f} MHz")
print(f"      1.2^2 = {1.2**2:.2f}, 1.6^2 = {1.6**2:.2f}, pi sqrt(1.44 + 2.56) = {np.pi*np.sqrt(1.44+2.56):.6f}")
Eph = lambda r: np.array([0, 0, 5]) * np.exp(1j * np.dot(abc, r))
Hph = lambda r: np.cross(u, Eph(r)) / eta0C
H0 = np.cross(u, np.array([0, 0, 5.0])) / eta0C
print(f"      u x z = {np.cross(u, Z)};  H0 = {H0*1e3} mA/m = (0.8 x + 0.6 y)/(24 pi): 1/(24pi) = {1/(24*np.pi)*1e3:.4f} mA/m")
print(f"      components: 0.8/(24pi) = {0.8/(24*np.pi)*1e3:.4f} mA/m, 0.6/(24pi) = {0.6/(24*np.pi)*1e3:.4f} mA/m")
Et, Ht = tdom(Eph, w), tdom(Hph, w)
r0 = np.array([0.3, -0.2, 0.7])
Sc = tavg_vec(lambda t: np.cross(Et(r0, t), Ht(r0, t)), T)
print(f"      <S> (quad) = {Sc} W/m^2, |<S>| = {np.linalg.norm(Sc):.5f} = 25/(240pi) = 5/(48pi) = {5/(48*np.pi):.5f}; direction {dname(Sc)}")
check("21.7c", np.allclose(Sc / np.linalg.norm(Sc), u) and abs(np.linalg.norm(Sc) - 5 / (48 * np.pi)) < 1e-12)
same_signal("21.7c H(t)", Hph(r0), lambda t: H0 * np.cos(w * t + np.dot(abc, r0)), w)
bex = w / c
maxwell("21.7c pair (exact)", tdom(lambda r: np.array([0, 0, 5]) * np.exp(-1j * bex * np.dot(u, r)), w),
        tdom(lambda r: np.cross(u, np.array([0, 0, 5.0])) / eta0 * np.exp(-1j * bex * np.dot(u, r)), w), mu0, eps0, w, bex)

# =====================================================================================
hdr("21.8 A driven electron in phasors")
N, fq, E0 = 1.0e12, 20e6, 0.2
w = 2 * np.pi * fq; T = 1 / fq
v0 = e * E0 / (me * w)
vph = -e * E0 / (1j * w * me)          # j omega m v = -e E
print(f"  omega = {w:.6e} rad/s; v phasor = -eE0/(j w m) = {vph:.4f} = j*{v0:.3f} m/s -> v(t) = -{v0:.2f} sin(wt) m/s")
same_signal("21.8a v(t)", vph, lambda t: -v0 * np.sin(w * t), w)
sol = solve_ivp(lambda t, y: [-e * E0 * np.cos(w * t) / me], [0, 3 * T], [0.0], rtol=1e-12, atol=1e-9, dense_output=True)
tl = np.linspace(0, 3 * T, 301)
dev = np.max(np.abs(sol.sol(tl)[0] - (-v0 * np.sin(w * tl))))
print(f"  ODE integrated from v(0) = 0 (no transient without collisions): max |v - (-v0 sin wt)| = {dev:.2e} m/s (v0 = {v0:.2f})")
check("21.8a", dev < 1e-6 * v0)
J0 = N * e * v0
Jph = -N * e * vph
print(f"  J phasor = -N e v = {Jph:.4e} = -j {J0:.4e} A/m^2 -> J(t) = {J0*1e6:.2f} sin(wt) uA/m^2 (lags E by 90 deg)")
same_signal("21.8b J(t)", Jph, lambda t: J0 * np.sin(w * t), w)
pJE = 0.5 * np.real(Jph * np.conj(E0))
qJE = tavg(lambda t: J0 * np.sin(w * t) * E0 * np.cos(w * t), T)
print(f"  <J.E> = 1/2 Re{{J E*}} = {pJE:.2e}; quad = {qJE:.2e} W/m^3")
check("21.8b <J.E> = 0", abs(pJE) < 1e-20 and abs(qJE) < 1e-15)
JD0 = w * eps0 * E0
wp2 = N * e ** 2 / (me * eps0)
print(f"  displacement current amplitude w eps0 E0 = {JD0:.4e} A/m^2 = {JD0*1e6:.1f} uA/m^2; phasor j w eps0 E0 (leads by 90)")
print(f"  ratio J0/JD0 = {J0/JD0:.5f};  omega_p^2/omega^2 = {wp2/w**2:.5f};  f_p = {np.sqrt(wp2)/2/np.pi/1e6:.4f} MHz")
tot = Jph + 1j * w * eps0 * E0
print(f"  total J + j w eps0 E = {tot:.4e} = j w eps0 (1 - wp^2/w^2) E0 = {1j*w*eps0*(1-wp2/w**2)*E0:.4e}")
check("21.8c effective permittivity", abs(tot - 1j * w * eps0 * (1 - wp2 / w ** 2) * E0) < 1e-18 and abs(J0 / JD0 - wp2 / w ** 2) < 1e-12)
er_eff = 1 - wp2 / w ** 2
for cc, lab in ((cC, "c = 3e8"), (c, "exact c")):
    b = w / cc * np.sqrt(er_eff)
    print(f"  eps_eff/eps0 = {er_eff:.5f}; sqrt = {np.sqrt(er_eff):.5f}; beta = {b:.5f} rad/m, lambda = {2*np.pi/b:.3f} m, "
          f"v_p = {w/b:.4e} m/s = {w/b/cc:.4f} c ({lab})")
print(f"  omega/c = {w/cC:.5f} rad/m (c = 3e8); omega = {w:.4e} rad/s")
eG, mG, e0G = 1.602e-19, 9.109e-31, 8.854e-12
v0G = eG * E0 / (mG * w); J0G = N * eG * v0G; JDG = w * e0G * E0; rG = N * eG ** 2 / (mG * e0G * w ** 2)
print(f"  with the page's rounded constants: v0 = {v0G:.2f} m/s, J0 = {J0G:.4e} A/m^2 ({J0G*1e6:.2f} uA/m^2), "
      f"w eps0 E0 = {JDG:.4e} A/m^2, ratio = {rG:.4f}, eps_eff = {1-rG:.4f}, beta = {w/cC*np.sqrt(1-rG):.4f} rad/m, "
      f"lambda = {2*np.pi/(w/cC*np.sqrt(1-rG)):.2f} m, v_p = {cC/np.sqrt(1-rG):.4e} m/s")
check("21.8 with given constants (3 s.f.)", round(v0G) == 280 and round(J0G * 1e6, 1) == 44.8 and round(JDG * 1e6) == 223
      and round(rG, 3) == 0.202 and round(1 - rG, 3) == 0.798 and round(w / cC * np.sqrt(1 - rG), 3) == 0.374)
b_disp = np.sqrt(w ** 2 - wp2) / cC
print(f"  dispersion relation (1/c)sqrt(w^2 - wp^2) = {b_disp:.5f} rad/m (same)")
check("21.8c beta agrees with the dispersion relation", abs(b_disp - w / cC * np.sqrt(er_eff)) < 1e-12)

# =====================================================================================
hdr("21.9 Building a phasor from two snapshots (template)")
f9, er9 = 100e6, 2.25
v9 = cC / np.sqrt(er9); beta = 2 * np.pi * f9 / v9; lam = 2 * np.pi / beta; eta9 = eta0C / np.sqrt(er9)
w = 2 * np.pi * f9; T = 1 / f9
u = np.array([-4, 3, 0]) / 5
abc = -beta * u
print(f"  v = {v9:.3e} m/s, beta = {beta:.6f} rad/m (pi), lambda = {lam:.4f} m, eta = 80pi = {eta9:.3f} Ohm, T = {T*1e9:.2f} ns")
print(f"  (a, b, c) = -beta u = {abc} = ({abc[0]/np.pi:.2f}pi, {abc[1]/np.pi:.2f}pi, {abc[2]/np.pi:.2f}pi) rad/m")
S0, S4 = np.array([0, 0, 4.0]), np.array([3, 4, 0.0])
print(f"  snapshots . u: {S0 @ u:.3f}, {S4 @ u:.3f}  (both perpendicular to u)")
E0v = S0 - 1j * S4
print(f"  E0 = E(0,0) - j E(0,T/4) = {cvec(E0v)} -> A = -3j, B = -4j, C = 4 V/m; E0 . u = {E0v @ u:.2e}")
Eph = lambda r: E0v * np.exp(1j * np.dot(abc, r))
Et = tdom(Eph, w)
print(f"  check: E(0,0) = {Et(np.zeros(3), 0)}, E(0,T/4) = {Et(np.zeros(3), T/4)}")
check("21.9b snapshots reproduced", np.allclose(Et(np.zeros(3), 0), S0) and np.allclose(Et(np.zeros(3), T / 4), S4))
same_signal("21.9b E(0,t) = 3 sin x + 4 sin y + 4 cos z", Eph(np.zeros(3)),
            lambda t: np.array([3 * np.sin(w * t), 4 * np.sin(w * t), 4 * np.cos(w * t)]), w)
H0v = np.cross(u, E0v) / eta9
print(f"  u x E0 = {cvec(np.cross(u, E0v))} -> H0 = {cvec(H0v*1e3)} mA/m")
print(f"  3/(100pi) = {3/(100*np.pi)*1e3:.4f} mA/m, 1/(25pi) = {1/(25*np.pi)*1e3:.4f} mA/m, 1/(16pi) = {1/(16*np.pi)*1e3:.4f} mA/m")
check("21.9c H0", np.allclose(H0v, np.array([3 / (100 * np.pi), 1 / (25 * np.pi), 1j / (16 * np.pi)])))
Hph = lambda r: H0v * np.exp(1j * np.dot(abc, r))
Ht = tdom(Hph, w)
for r0 in (np.zeros(3), np.array([0.7, -0.4, 1.3])):
    Sq = tavg_vec(lambda t: np.cross(Et(r0, t), Ht(r0, t)), T)
    print(f"  <S> at {r0} (quad) = {Sq} W/m^2, |<S>| = {np.linalg.norm(Sq):.5f}, dir {dname(Sq)}")
    ALL.append(np.allclose(Sq, 41 / (2 * eta9) * u, atol=1e-13))
print(f"  41/(160 pi) = {41/(160*np.pi):.5f} W/m^2; vector = {41/(160*np.pi)*u}")
print(f"  z part alone 16/(160pi) = {16/(160*np.pi):.5f}; xy part alone 25/(160pi) = {25/(160*np.pi):.5f}; sum {41/(160*np.pi):.5f}")
print(f"  1/2 Re(E0 x H0*) = {0.5*np.real(np.cross(E0v, np.conj(H0v)))}")
check("21.9d power", np.allclose(0.5 * np.real(np.cross(E0v, np.conj(H0v))), 41 / (160 * np.pi) * u))
P = np.array([1, 0.5, 0])
print(f"  P = (1, 0.5, 0): u.r = {u @ P:.3f} m (= -lambda/4), phase factor e^(-j beta u.r) = {np.exp(-1j*beta*(u@P)):.4f}")
print(f"  E(P, 0) = {Et(P, 0)} V/m  (= E(0, T/4))")
check("21.9e E(P,0) = 3x + 4y", np.allclose(Et(P, 0), S4))
bex = w * np.sqrt(mu0 * er9 * eps0)
maxwell("21.9 full field (exact)", tdom(lambda r: E0v * np.exp(-1j * bex * np.dot(u, r)), w),
        tdom(lambda r: np.cross(u, E0v) / np.sqrt(mu0 / (er9 * eps0)) * np.exp(-1j * bex * np.dot(u, r)), w), mu0, er9 * eps0, w, bex)

# =====================================================================================
hdr("21.10 Two sheets, two current directions")
f10, er10 = 75e6, 4.0
v10 = cC / 2; beta = 2 * np.pi * f10 / v10; lam = 2 * np.pi / beta; d = lam / 4; eta = eta0C / 2
w = 2 * np.pi * f10; T = 1 / f10
print(f"  v = {v10:.2e}, beta = {beta:.6f} (pi), lambda = {lam:.3f} m, d = {d:.3f} m, eta = 60pi = {eta:.3f} Ohm")


def sheet_ph(J, z0, eta, beta):
    """phasor fields of a sheet on z = z0 with phasor current J (3-vector)."""
    J = np.asarray(J, complex)

    def E(r):
        return -eta / 2 * J * np.exp(-1j * beta * abs(r[2] - z0))

    def H(r):
        n = Z if r[2] > z0 else -Z
        return 0.5 * np.cross(J, n) * np.exp(-1j * beta * abs(r[2] - z0))
    return E, H


JA, JB = np.array([2, 0, 0], complex), np.array([0, -1j, 0])
print(f"  J_A = 2 cos wt x -> {cvec(JA)};  J_B = sin wt y -> {cvec(JB)}")
same_signal("21.10a J_B phasor", JB, lambda t: np.array([0, np.sin(w * t), 0]), w)
EA, HA = sheet_ph(JA, 0.0, eta, beta)
EB, HB = sheet_ph(JB, d, eta, beta)
print(f"  x x z = {np.cross(X, Z)}, x x (-z) = {np.cross(X, -Z)}, y x z = {np.cross(Y, Z)}, y x (-z) = {np.cross(Y, -Z)}")
for zz in (1.3, 0.2, -0.7):
    r = np.array([0, 0, zz])
    print(f"  z={zz:+.1f}: E_A = {cvec(EA(r))}, H_A = {cvec(HA(r))}, E_B = {cvec(EB(r))}, H_B = {cvec(HB(r))}")
Etot = lambda r: EA(r) + EB(r)
Htot = lambda r: HA(r) + HB(r)
for zz in (0.8, 1.7, 3.1):
    r = np.array([0, 0, zz])
    Pq = Etot(r)[0] / np.exp(-1j * beta * zz); Qq = Etot(r)[1] / Etot(r)[0]
    print(f"  z={zz} > d: E/e^(-j beta z) = {cvec(Etot(r)/np.exp(-1j*beta*zz))} -> P = {Pq:.4f} (= -60pi = {-60*np.pi:.4f}), Q = {Qq:.4f}")
    ALL.append(abs(Pq + 60 * np.pi) < 1e-9 and abs(Qq - 0.5) < 1e-12)
for zz in (-0.3, -1.6):
    r = np.array([0, 0, zz])
    print(f"  z={zz} < 0: E/e^(+j beta z) = {cvec(Etot(r)/np.exp(1j*beta*zz))} (= -60pi (x - y/2))")
    ALL.append(np.allclose(Etot(r) / np.exp(1j * beta * zz), -60 * np.pi * np.array([1, -0.5, 0])))
for zz in (0.1, 0.35):
    r = np.array([0, 0, zz])
    pred = -60 * np.pi * np.exp(-1j * beta * zz) * X + 30 * np.pi * np.exp(1j * beta * zz) * Y
    print(f"  0<z={zz}<d: E = {cvec(Etot(r))}; formula -60pi e^(-jbz) x + 30pi e^(+jbz) y -> {np.allclose(Etot(r), pred)}")
    ALL.append(np.allclose(Etot(r), pred))
    predH = -np.exp(-1j * beta * zz) * Y + 0.5 * np.exp(1j * beta * zz) * X
    print(f"           H = {cvec(Htot(r))}; formula -e^(-jbz) y + 1/2 e^(+jbz) x -> {np.allclose(Htot(r), predH)}")
    ALL.append(np.allclose(Htot(r), predH))
r = np.array([0, 0, 1.2]); print(f"  z>d: H e^(+j beta z) = {cvec(Htot(r)*np.exp(1j*beta*1.2))} (= x/2 - y)")
ALL.append(np.allclose(Htot(r) * np.exp(1j * beta * 1.2), np.array([0.5, -1, 0])))
r = np.array([0, 0, -1.2]); print(f"  z<0: H e^(-j beta z) = {cvec(Htot(r)*np.exp(-1j*beta*-1.2))} (= x/2 + y)")
ALL.append(np.allclose(Htot(r) * np.exp(1j * beta * 1.2), np.array([0.5, 1, 0])))
Et, Ht = tdom(Etot, w), tdom(Htot, w)
Sreg = {}
for zz, lab in ((1.4, "z>d"), (0.25, "0<z<d"), (-0.9, "z<0")):
    r = np.array([0, 0, zz])
    Sq = tavg_vec(lambda t: np.cross(Et(r, t), Ht(r, t)), T)
    Sp = 0.5 * np.real(np.cross(Etot(r), np.conj(Htot(r))))
    Sreg[lab] = Sq[2]
    print(f"  {lab}: <S>_z quad = {Sq[2]:+.5f} W/m^2 = {Sq[2]/np.pi:+.4f} pi; phasor rule {Sp[2]:+.5f}")
    ALL.append(abs(Sq[2] - Sp[2]) < 1e-9)
check("21.10d region powers 37.5pi, 22.5pi, -37.5pi",
      abs(Sreg["z>d"] - 37.5 * np.pi) < 1e-9 and abs(Sreg["0<z<d"] - 22.5 * np.pi) < 1e-9 and abs(Sreg["z<0"] + 37.5 * np.pi) < 1e-9)
print(f"  37.5 pi = {37.5*np.pi:.3f}, 22.5 pi = {22.5*np.pi:.3f}, 30 pi = {30*np.pi:.3f}, 7.5 pi = {7.5*np.pi:.3f} W/m^2")
JAt = lambda t: np.real(JA * np.exp(1j * w * t)); JBt = lambda t: np.real(JB * np.exp(1j * w * t))
EA0 = lambda t: 0.5 * (Et(np.array([0, 0, 1e-12]), t) + Et(np.array([0, 0, -1e-12]), t))
EBd = lambda t: 0.5 * (Et(np.array([0, 0, d + 1e-12]), t) + Et(np.array([0, 0, d - 1e-12]), t))
pA = tavg(lambda t: -JAt(t) @ EA0(t), T); pB = tavg(lambda t: -JBt(t) @ EBd(t), T)
print(f"  E(0) phasor = {cvec(Etot(np.array([0,0,1e-12])))};  E(d) phasor = {cvec(Etot(np.array([0,0,d+1e-12])))}")
print(f"  <-J_A.E> quad = {pA:.4f} = {pA/np.pi:.4f} pi;  phasor 1/2Re(-J_A.E*) = {0.5*np.real(-JA@np.conj(Etot(np.array([0,0,1e-12])))):.4f}")
print(f"  <-J_B.E> quad = {pB:.4f} = {pB/np.pi:.4f} pi;  phasor = {0.5*np.real(-JB@np.conj(Etot(np.array([0,0,d+1e-12])))):.4f}")
print(f"  supplied {pA+pB:.4f} = {(pA+pB)/np.pi:.3f} pi; carried out {Sreg['z>d']-Sreg['z<0']:.4f}")
check("21.10e energy balance", abs(pA - 60 * np.pi) < 1e-8 and abs(pB - 15 * np.pi) < 1e-8 and abs(pA + pB - (Sreg["z>d"] - Sreg["z<0"])) < 1e-8)
check("21.10e flux jumps: at A 22.5pi + 37.5pi = 60pi, at B 37.5pi - 22.5pi = 15pi",
      abs(Sreg["0<z<d"] - Sreg["z<0"] - pA) < 1e-8 and abs(Sreg["z>d"] - Sreg["0<z<d"] - pB) < 1e-8)
# boundary conditions at both sheets
ok = True
for t in rng.uniform(0, T, 7):
    for z0, J in ((0.0, JAt), (d, JBt)):
        E1, E2 = Et(np.array([0, 0, z0 + 1e-9]), t), Et(np.array([0, 0, z0 - 1e-9]), t)
        H1, H2 = Ht(np.array([0, 0, z0 + 1e-9]), t), Ht(np.array([0, 0, z0 - 1e-9]), t)
        ok &= np.allclose(E1[:2], E2[:2], atol=1e-5) and np.allclose(np.cross(Z, H1 - H2), J(t), atol=1e-6)
check("21.10 boundary conditions at both sheets", ok)
bex = w * np.sqrt(mu0 * er10 * eps0); etax = np.sqrt(mu0 / (er10 * eps0))
EAx, HAx = sheet_ph(JA, 0.0, etax, bex); EBx, HBx = sheet_ph(JB, np.pi / (2 * bex), etax, bex)
maxwell("21.10 total field (exact)", tdom(lambda r: EAx(r) + EBx(r), w), tdom(lambda r: HAx(r) + HBx(r), w), mu0, er10 * eps0, w, bex,
        avoid=lambda r: min(abs(r[2]), abs(r[2] - np.pi / (2 * bex))) < 1e-3)
# (f) parallel variant
JB2 = np.array([-1j, 0, 0])
EB2, HB2 = sheet_ph(JB2, d, eta, beta)
E2t = lambda r: EA(r) + EB2(r); H2t = lambda r: HA(r) + HB2(r)
for zz in (1.4, -0.9):
    r = np.array([0, 0, zz])
    Ep = E2t(r) / np.exp(-1j * beta * abs(zz))
    Sq = tavg_vec(lambda t: np.cross(tdom(E2t, w)(r, t), tdom(H2t, w)(r, t)), T)
    print(f"  (f) parallel, z={zz}: E/e^(-jb|z|) = {cvec(Ep)}; <S>_z = {Sq[2]:+.4f} = {Sq[2]/np.pi:+.3f} pi W/m^2")
pA2 = 0.5 * np.real(-JA @ np.conj(E2t(np.array([0, 0, 1e-12]))))
pB2 = 0.5 * np.real(-JB2 @ np.conj(E2t(np.array([0, 0, d + 1e-12]))))
print(f"  (f) E(0) = {cvec(E2t(np.array([0,0,1e-12])))}, E(d) = {cvec(E2t(np.array([0,0,d+1e-12])))}")
print(f"  (f) supplies: A {pA2/np.pi:.3f} pi, B {pB2/np.pi:.3f} pi, total {(pA2+pB2)/np.pi:.3f} pi;  67.5pi = {67.5*np.pi:.2f}, 7.5pi = {7.5*np.pi:.2f}")
check("21.10f parallel: 67.5pi and 7.5pi, total 75pi", abs(pA2 - 30 * np.pi) < 1e-9 and abs(pB2 - 45 * np.pi) < 1e-9)
# general: total radiated = (eta/8)(2|JA|^2 + 2|JB|^2 + 4 Re(JA.JB*) cos(beta d))
for dd in (0.25, 0.5, 0.75, 1.0):
    EBq, _ = sheet_ph(JB2, dd, eta, beta)
    Ep = EA(np.array([0, 0, 5.0])) + EBq(np.array([0, 0, 5.0])); Em = EA(np.array([0, 0, -5.0])) + EBq(np.array([0, 0, -5.0]))
    tot = (np.vdot(Ep, Ep).real + np.vdot(Em, Em).real) / (2 * eta)
    print(f"  (f) parallel currents, spacing {dd} m (beta d = {beta*dd/np.pi:.2f} pi): total radiated {tot/np.pi:.3f} pi W/m^2")
print("  (f) the total is (eta/8)[2|JA|^2 + 2|JB|^2 + 4 Re(JA.JB*) cos(beta d)]; here Re(JA.JB*) = Re(2 * j) = 0 (quadrature),")
print("      so the total stays 75 pi at every spacing; for comparison, IN-PHASE currents JB = 1 x (cos wt):")
for dd in (0.25, 0.5, 1.0):
    EBq, _ = sheet_ph(np.array([1, 0, 0], complex), dd, eta, beta)
    Ep = EA(np.array([0, 0, 5.0])) + EBq(np.array([0, 0, 5.0])); Em = EA(np.array([0, 0, -5.0])) + EBq(np.array([0, 0, -5.0]))
    tot = (np.vdot(Ep, Ep).real + np.vdot(Em, Em).real) / (2 * eta)
    form = eta / 8 * (2 * 4 + 2 * 1 + 4 * 2 * np.cos(beta * dd))
    print(f"      spacing {dd} m: total {tot/np.pi:.3f} pi (formula {form/np.pi:.3f} pi)")
    ALL.append(abs(tot - form) < 1e-9)

# =====================================================================================
hdr("21.11 Two waves on one line")
f11, er11 = 100e6, 9.0
v11 = cC / 3; beta = 2 * np.pi * f11 / v11; lam = 2 * np.pi / beta; eta = eta0C / 3; eps = er11 * eps0
w = 2 * np.pi * f11; T = 1 / f11
print(f"  v = {v11:.2e}, beta = {beta:.6f} rad/m (2pi), lambda = {lam:.3f} m, eta = 40pi = {eta:.4f} Ohm")
Eph = lambda r: (6 * np.exp(-1j * beta * r[2]) - 2j * np.exp(1j * beta * r[2])) * X
for z0 in (0.0, 0.21):
    same_signal(f"21.11a E phasor z={z0}", Eph(np.array([0, 0, z0])),
                lambda t: (6 * np.cos(w * t - beta * z0) + 2 * np.sin(w * t + beta * z0)) * X, w)
H1 = lambda r: np.cross(Z, 6 * np.exp(-1j * beta * r[2]) * X) / eta
H2 = lambda r: np.cross(-Z, -2j * np.exp(1j * beta * r[2]) * X) / eta
Hph = lambda r: H1(r) + H2(r)
print(f"  z x x = {np.cross(Z, X)}, (-z) x x = {np.cross(-Z, X)};  H phasor at z=0: {cvec(Hph(np.zeros(3))*eta)}/eta (= (6 + 2j) y/eta)")
for z0 in (0.0, 0.33):
    same_signal(f"21.11a H(t) z={z0}", Hph(np.array([0, 0, z0])),
                lambda t: (6 * np.cos(w * t - beta * z0) - 2 * np.sin(w * t + beta * z0)) / eta * Y, w)
print(f"  6/eta = {6/eta*1e3:.3f} mA/m, 2/eta = {2/eta*1e3:.3f} mA/m")
Et, Ht = tdom(Eph, w), tdom(Hph, w)
for z0 in (0.0, 0.07, 0.125, 0.3, 0.375):
    r = np.array([0, 0, z0])
    St = np.cross(Eph(r), np.conj(Hph(r)))
    Sq = tavg_vec(lambda t: np.cross(Et(r, t), Ht(r, t)), T)
    print(f"  z={z0:.3f}: E x H* = {St[2]:.5f} (eta: {St[2]*eta:.4f} = 32 - 24j cos 2bz = {32-24j*np.cos(2*beta*z0):.4f}); <S>_z quad = {Sq[2]:.6f}")
    ALL.append(abs(St[2] * eta - (32 - 24j * np.cos(2 * beta * z0))) < 1e-10 and abs(Sq[2] - 16 / eta) < 1e-12)
print(f"  <S> = 16/eta = 0.4/pi = {16/eta:.5f} W/m^2 (= 36/(2eta) - 4/(2eta) = {36/(2*eta):.5f} - {4/(2*eta):.5f})")
zs = np.linspace(0, lam / 2, 200001)[:-1]
Em = np.array([np.linalg.norm(Eph(np.array([0, 0, z]))) for z in zs[::50]]); zz = zs[::50]
Hm = np.array([np.linalg.norm(Hph(np.array([0, 0, z]))) for z in zz])
print(f"  |E| max {Em.max():.5f} V/m at z = {zz[Em.argmax()]:.4f} m; min {Em.min():.5f} at z = {zz[Em.argmin()]:.4f} m")
print(f"  |H| max {Hm.max()*1e3:.4f} mA/m at z = {zz[Hm.argmax()]:.4f} m; min {Hm.min()*1e3:.4f} mA/m at z = {zz[Hm.argmin()]:.4f} m")
print(f"  8/eta = {8/eta*1e3:.4f} mA/m, 4/eta = {4/eta*1e3:.4f} mA/m; |E|^2 = 40 + 24 sin(2bz) check at z=0.1: "
      f"{np.linalg.norm(Eph(np.array([0,0,0.1])))**2:.5f} vs {40+24*np.sin(2*beta*0.1):.5f}")
check("21.11c extremes", abs(Em.max() - 8) < 1e-6 and abs(zz[Em.argmax()] - 0.125) < 1e-4 and abs(Em.min() - 4) < 1e-6
      and abs(zz[Em.argmin()] - 0.375) < 1e-4)
for z0 in (0.125, 0.375, 0.0):
    r = np.array([0, 0, z0])
    print(f"  |E|/|H| at z = {z0}: {np.linalg.norm(Eph(r))/np.linalg.norm(Hph(r)):.4f} Ohm = {np.linalg.norm(Eph(r))/np.linalg.norm(Hph(r))/eta:.3f} eta")
# energy densities: use exact, mutually consistent constants (eta_x = sqrt(mu0/eps), v_x = 1/sqrt(mu0 eps))
eta_x, v_x = np.sqrt(mu0 / eps), 1 / np.sqrt(mu0 * eps)
Hph_x = lambda r: (6 * np.exp(-1j * beta * r[2]) + 2j * np.exp(1j * beta * r[2])) / eta_x * Y
Ht_x = tdom(Hph_x, w)
for z0 in (0.0, 0.125, 0.2, 0.375):
    r = np.array([0, 0, z0])
    we = tavg(lambda t: 0.5 * eps * Et(r, t)[0] ** 2, T)
    wm = tavg(lambda t: 0.5 * mu0 * Ht_x(r, t)[1] ** 2, T)
    print(f"  z={z0}: <w_e> quad = {we:.5e}, 1/4 eps|E|^2 = {0.25*eps*np.linalg.norm(Eph(r))**2:.5e}; <w_m> = {wm:.5e}, "
          f"1/4 mu|H|^2 = {0.25*mu0*np.linalg.norm(Hph_x(r))**2:.5e}; sum = {we+wm:.5e} J/m^3 (20 eps = {20*eps:.5e})")
    ALL.append(abs(we + wm - 20 * eps) < 1e-22 and abs(we - 0.25 * eps * np.linalg.norm(Eph(r)) ** 2) < 1e-22
               and abs(wm - 0.25 * mu0 * np.linalg.norm(Hph_x(r)) ** 2) < 1e-22)
print(f"  eps = 9 eps0 = {eps:.4e} F/m; <w_e> range: {0.25*eps*16:.4e} .. {0.25*eps*64:.4e} J/m^3 (4 eps .. 16 eps); "
      f"total 20 eps = {20*eps*1e9:.4f} nJ/m^3")
Sx = tavg(lambda t: Et(np.zeros(3), t)[0] * Ht_x(np.zeros(3), t)[1], T)
print(f"  exact constants: <S> = {Sx:.6f} W/m^2 (16/eta_x = {16/eta_x:.6f}); v<w> = {v_x*20*eps:.6f} (= 20/eta_x, the value if all"
      f" 40 units travelled forward); <S>/<w> = {Sx/(20*eps):.5e} m/s = {Sx/(20*eps)/v_x:.6f} v")
check("21.11d <S>/<w> = 0.8 v", abs(Sx / (20 * eps) / v_x - 0.8) < 1e-9)
print(f"  course numbers: v = 1e8 m/s -> 0.8 v = 8e7 m/s; 16/eta = 0.4/pi = {0.4/np.pi:.5f} W/m^2")
Sz0 = lambda t: Et(np.zeros(3), t)[0] * Ht(np.zeros(3), t)[1]
tl = np.linspace(0, T, 400001)[:-1]
Sv = np.array([Sz0(t) for t in tl[::20]])
frac = np.mean(Sv < 0)
print(f"  S_z(0,t) = (36 cos^2 - 4 sin^2)/eta: min {Sv.min():.5f} (-4/eta = {-4/eta:.5f}), max {Sv.max():.5f} (36/eta = {36/eta:.5f})")
print(f"  fraction of the period with S_z < 0: numerical {frac:.4f}; 1 - (2/pi) atan 3 = {1-2/np.pi*np.arctan(3):.4f}; |tan wt| > 3")
print(f"  negative intervals: wt in ({np.degrees(np.arctan(3)):.2f}, {180-np.degrees(np.arctan(3)):.2f}) deg and +180 deg")
check("21.11e reversal fraction", abs(frac - (1 - 2 / np.pi * np.arctan(3))) < 1e-3 and abs(tavg(Sz0, T) - 16 / eta) < 1e-12)
bex = w * np.sqrt(mu0 * eps); etax = np.sqrt(mu0 / eps)
maxwell("21.11 two-wave field (exact)",
        tdom(lambda r: (6 * np.exp(-1j * bex * r[2]) - 2j * np.exp(1j * bex * r[2])) * X, w),
        tdom(lambda r: (6 * np.exp(-1j * bex * r[2]) + 2j * np.exp(1j * bex * r[2])) / etax * Y, w), mu0, eps, w, bex)

# =====================================================================================
hdr("21.12 A medium from phasor readings")
f12 = 25e6; w = 2 * np.pi * f12; T = 1 / f12
E0, H0, ph = 37.7, 0.2, np.radians(30)
Ez0 = E0 * np.exp(1j * ph) * Y; Hz0 = H0 * np.exp(1j * ph) * X
St = np.cross(Ez0, np.conj(Hz0))
print(f"  E x H* at z=0 = {cvec(St)} -> travel {dname(np.real(St))}")
dphi = np.radians(75 - 30); dz = 0.25
print(f"  phase rises by {np.degrees(dphi):.0f} deg from z = 0 to z = 0.25 m -> phase lags toward -z -> travel -z")
beta = dphi / dz; lam = 2 * np.pi / beta; vp = w / beta
print(f"  beta = {beta:.6f} rad/m (pi); lambda = {lam:.3f} m; v_p = {vp:.4e} m/s = c/{cC/vp:.3f}; half wavelength {lam/2} m > 0.25 m")
eta = E0 / H0
murer = (cC / vp) ** 2; mu_over = (eta / eta0C) ** 2
mur = np.sqrt(murer * mu_over); epr = np.sqrt(murer / mu_over)
print(f"  eta = 37.7/0.2 = {eta:.2f} Ohm = {eta/eta0C:.5f} eta0 (60 pi = {60*np.pi:.2f})")
print(f"  mu_r eps_r = {murer:.4f}, mu_r/eps_r = {mu_over:.5f} -> mu_r = {mur:.4f}, eps_r = {epr:.4f}")
check("21.12b mu_r = 3, eps_r = 12", abs(mur - 3) < 1e-3 and abs(epr - 12) < 5e-3)
Eph = lambda r: E0 * np.exp(1j * ph) * np.exp(1j * beta * r[2]) * Y
Hph = lambda r: np.cross(-Z, Eph(r)) / (60 * np.pi)
print(f"  H from (1/eta)(-z) x E at z=0: {cvec(Hph(np.zeros(3)))}; (-z) x y = {np.cross(-Z, Y)}  (matches the reading 0.2 e^j30 x)")
print(f"  E at z = 0.25: {pol(Eph(np.array([0,0,0.25]))[1])}")
check("21.12a data consistent", abs(np.angle(Eph(np.array([0, 0, 0.25]))[1]) - np.radians(75)) < 1e-12)
same_signal("21.12c E(z,t) at z=0.6", Eph(np.array([0, 0, 0.6])), lambda t: 37.7 * np.cos(w * t + beta * 0.6 + ph) * Y, w)
Et, Ht = tdom(Eph, w), tdom(Hph, w)
Sq = tavg_vec(lambda t: np.cross(Et(np.array([0, 0, -4.0]), t), Ht(np.array([0, 0, -4.0]), t)), T)
print(f"  <S> at z=-4 m (quad) = {Sq} W/m^2; 1/2 E0 H0 = {0.5*E0*H0:.3f}; 1/2 eta H0^2 with eta = 60pi: {0.5*60*np.pi*0.04:.4f} (= 1.2 pi)")
print(f"  power through 2 m^2: {abs(Sq[2])*2:.3f} W (2.4 pi = {2.4*np.pi:.3f} W) toward -z")
print(f"  (rounded data: E = 37.7 V/m with eta = 60pi gives H = {37.7/(60*np.pi):.6f} A/m, so <S> = {0.5*37.7**2/(60*np.pi):.5f};"
      f" 1/2 x 37.7 x 0.2 = {0.5*37.7*0.2:.5f})")
check("21.12d power 3.77 W/m^2 toward -z, 7.54 W", abs(Sq[2] + 0.5 * 37.7 * 0.2) / 3.77 < 1e-4 and dname(Sq) == "-z"
      and round(abs(Sq[2]) * 2, 2) == 7.54)
Pm = Eph(np.array([0, 0, -0.5]))[1]
print(f"  probe z = -0.5 m: phasor {pol(Pm)} -> E(t) = 37.7 cos(wt - 60 deg) y; delay T/4 = {T/4*1e9:.1f} ns (T = {T*1e9:.0f} ns)")
same_signal("21.12e record at z=-0.5", Pm, lambda t: 37.7 * np.cos(w * (t - T / 4) + ph), w)
zs = np.linspace(-2, 0, 200001)
zpk = zs[np.argmax(37.7 * np.cos(beta * zs + ph))]
print(f"  snapshot t=0: E_y(z,0) = 37.7 cos(pi z + 30deg): peak on (-2, 0) at z = {zpk:.5f} m (-1/6 = {-1/6:.5f})")
check("21.12e snapshot peak", abs(zpk + 1 / 6) < 1e-4)
print(f"  that crest at t = T/4: z = {-1/6 - 0.5:.4f} m (moved lambda/4 toward -z)")
mu12, eps12 = 3 * mu0, 12 * eps0
bex = w * np.sqrt(mu12 * eps12); etax = np.sqrt(mu12 / eps12)
maxwell("21.12 pair in mu_r=3, eps_r=12 (exact)", tdom(lambda r: 37.7 * np.exp(1j * ph) * np.exp(1j * bex * r[2]) * Y, w),
        tdom(lambda r: 37.7 / etax * np.exp(1j * ph) * np.exp(1j * bex * r[2]) * X, w), mu12, eps12, w, bex)
print(f"  exact eta for mu_r=3, eps_r=12: {etax:.2f} Ohm; with E = 37.7 V/m, H = {37.7/etax:.4f} A/m")
print(f"  same speed, non-magnetic eps_r = 36: eta = eta0/6 = 20 pi = {eta0C/6:.2f} Ohm (vs 60 pi = {60*np.pi:.2f} Ohm)")
print(f"  lambda f = {2*25e6:.3e} m/s = v_p")

# =====================================================================================
print("\n" + "=" * 78)
print(f"ALL CHECKS: {sum(ALL)}/{len(ALL)} passed" + ("" if all(ALL) else "  <-- FAILURES"))
