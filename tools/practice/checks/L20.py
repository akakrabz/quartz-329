#!/usr/bin/env python3
"""L20 practice checks: Poynting's theorem and power (numpy + scipy only).

Every number, sign and direction on practice/20-poynting-theorem-and-power.md is printed here.
Directions by np.cross; curls, divergences and time derivatives by central finite differences;
time averages by scipy.integrate.quad over whole periods; volume and surface integrals by quad/dblquad;
the RC charging law by solve_ivp. Course (exam) constants c = 3e8, eta0 = 120 pi, eps0 = 1e-9/(36 pi)
are used where the page says so; SI eps0 = 8.8541878128e-12 for the calculator problems.
"""
import warnings
import numpy as np
from scipy.integrate import quad, dblquad, solve_ivp, fixed_quad, IntegrationWarning
from scipy.optimize import brentq

eps0 = 8.8541878128e-12
mu0 = 4e-7 * np.pi
c = 2.99792458e8
eta0 = np.sqrt(mu0 / eps0)
cC, etaC, eps0C = 3e8, 120 * np.pi, 1e-9 / (36 * np.pi)   # course values used on the page
X, Y, Z = np.eye(3)
NAMES = {(1, 0, 0): "+x", (-1, 0, 0): "-x", (0, 1, 0): "+y", (0, -1, 0): "-y", (0, 0, 1): "+z", (0, 0, -1): "-z"}
ALL = []


def dname(v):
    v = np.asarray(v, float)
    if np.linalg.norm(v) == 0:
        return "0"
    n = v / np.linalg.norm(v)
    key = tuple(int(round(a)) for a in n)
    if np.allclose(n, key, atol=1e-9):
        return NAMES.get(key, str(key))
    return "(" + ", ".join(f"{a:+.4f}" for a in n) + ")"


def hdr(s):
    print("\n" + "=" * 78 + "\n" + s + "\n" + "=" * 78)


def check(label, cond):
    print(f"  [{label}] {'OK' if cond else 'FAIL'}")
    ALL.append(bool(cond))


def close(label, a, b, rtol=1e-6, atol=0.0):
    ok = np.allclose(a, b, rtol=rtol, atol=atol)
    print(f"  [{label}] {np.round(a, 10)} vs {np.round(b, 10)} -> {'OK' if ok else 'FAIL'}")
    ALL.append(bool(ok))
    return ok


def jac(F, r, t, h):
    J = np.zeros((3, 3))
    for j in range(3):
        d = np.zeros(3); d[j] = h
        J[:, j] = (F(r + d, t) - F(r - d, t)) / (2 * h)
    return J


def curl(F, r, t, h):
    J = jac(F, r, t, h)
    return np.array([J[2, 1] - J[1, 2], J[0, 2] - J[2, 0], J[1, 0] - J[0, 1]])


def div(F, r, t, h):
    return np.trace(jac(F, r, t, h))


def ddt(F, r, t, ht):
    return (F(r, t + ht) - F(r, t - ht)) / (2 * ht)


def rel(a, b):
    s = max(np.linalg.norm(a), np.linalg.norm(b), 1e-300)
    return np.linalg.norm(np.asarray(a) - np.asarray(b)) / s


def maxwell(label, E, H, mu, eps, pts, h, ht, J=None):
    """Faraday curl E = -mu dH/dt and Ampere-Maxwell curl H = J + eps dE/dt (J default 0)."""
    rf = ra = 0.0
    for (r, t) in pts:
        r = np.asarray(r, float)
        cE, dH = curl(E, r, t, h), -mu * ddt(H, r, t, ht)
        jj = np.zeros(3) if J is None else J(r, t)
        cH, dE = curl(H, r, t, h), jj + eps * ddt(E, r, t, ht)
        rf = max(rf, rel(cE, dH)); ra = max(ra, rel(cH, dE))
    ok = max(rf, ra) < 1e-4
    print(f"  [{label}] Faraday rel.res {rf:.1e} | Ampere-Maxwell {ra:.1e} -> {'OK' if ok else 'FAIL'}")
    ALL.append(ok)
    return ok


def poynting_point(label, E, H, mu, eps, r, t, h, ht, J=None, eps_fun=None):
    """Return (dw/dt, div S, J.E) at (r,t) by finite differences and check that they sum to 0."""
    r = np.asarray(r, float)
    epsv = (lambda rr, tt: eps) if eps_fun is None else eps_fun
    w = lambda rr, tt: 0.5 * epsv(rr, tt) * np.dot(E(rr, tt), E(rr, tt)) + 0.5 * mu * np.dot(H(rr, tt), H(rr, tt))
    dw = (w(r, t + ht) - w(r, t - ht)) / (2 * ht)
    S = lambda rr, tt: np.cross(E(rr, tt), H(rr, tt))
    dS = div(S, r, t, h)
    JE = 0.0 if J is None else np.dot(J(r, t), E(r, t))
    tot = dw + dS + JE
    scale = max(abs(dw), abs(dS), abs(JE), 1e-300)
    ok = abs(tot) / scale < 1e-5
    print(f"  [{label}] dw/dt = {dw:.6g}, div S = {dS:.6g}, J.E = {JE:.6g}, sum = {tot:.2e} (rel {abs(tot)/scale:.1e}) -> {'OK' if ok else 'FAIL'}")
    ALL.append(ok)
    return dw, dS, JE


def tavg(f, T, t0=0.0):
    """time average of a scalar function over one period [t0, t0+T]"""
    return quad(f, t0, t0 + T, limit=400, epsabs=1e-13, epsrel=1e-11)[0] / T


# =========================================================================================== 20.1
hdr("20.1 Reading the energy ledger (true or false)")
# (a) units by exponent vectors over (kg, m, s, A)
U = {"kg": np.array([1, 0, 0, 0]), "m": np.array([0, 1, 0, 0]), "s": np.array([0, 0, 1, 0]), "A": np.array([0, 0, 0, 1])}
W_ = U["kg"] + 2 * U["m"] - 3 * U["s"]          # watt
J_ = W_ + U["s"]                                 # joule
V_ = W_ - U["A"]                                 # volt
F_ = U["A"] + U["s"] - V_                        # farad = C/V
Hy_ = V_ + U["s"] - U["A"]                       # henry = V s / A
uE, uH = V_ - U["m"], U["A"] - U["m"]
u_eps, u_mu = F_ - U["m"], Hy_ - U["m"]
u_w = u_eps + 2 * uE
check("units: eps E^2 = mu H^2 = J/m^3", np.array_equal(u_w, J_ - 3 * U["m"]) and np.array_equal(u_mu + 2 * uH, J_ - 3 * U["m"]))
check("units: dw/dt = W/m^3", np.array_equal(u_w - U["s"], W_ - 3 * U["m"]))
check("units: E x H = W/m^2", np.array_equal(uE + uH, W_ - 2 * U["m"]))
check("units: div S = W/m^3", np.array_equal(uE + uH - U["m"], W_ - 3 * U["m"]))
check("units: J.E = (A/m^2)(V/m) = W/m^3", np.array_equal((U["A"] - 2 * U["m"]) + uE, W_ - 3 * U["m"]))
# (b) the radiating sheet: Js.E = -(eta/2)|Js|^2
print(f"  (b) sheet with Js = 1 A/m in vacuum: Js.E = -(eta0/2)*1 = {-eta0/2:.2f} W/m^2 (< 0: a source)")
# (c) battery: current from - terminal to + terminal, terminal field from + to -
Vb, Lb, Ib, Ab = 1.5, 0.05, 1.0, 1e-4
Eb = -Z * Vb / Lb      # + terminal at z = Lb, - terminal at z = 0: field points -z
Jb = Z * Ib / Ab
print(f"  (c) battery (1.5 V, 5 cm, 1 A, 1 cm^2): E = {Eb} V/m, J = {Jb} A/m^2, J.E = {np.dot(Jb, Eb):.1f} W/m^3,"
      f" over the volume {np.dot(Jb, Eb) * Ab * Lb:.2f} W = -VI")
check("(c) J.E < 0 inside the battery", np.dot(Jb, Eb) < 0)


# (d)/(e) fields from potentials (Faraday holds automatically); J defined by Ampere-Maxwell with eps(r) or eps(t)
def A_pot(r, t):
    x, y, z = r
    return np.array([np.sin(1.3 * y + 0.7 * t) * np.cos(0.4 * z), 0.5 * np.cos(0.9 * x - 1.1 * t + 0.3 * z), np.sin(x * z + 0.6 * t)])


def Phi_pot(r, t):
    x, y, z = r
    return np.cos(0.8 * x + 0.5 * y - 0.9 * t) + 0.3 * z * np.sin(t)


hh, hT = 1e-4, 1e-4
mu_t = 1.0                                      # unit system: the identity is algebraic, mu = 1, eps ~ 1


def Efield(r, t):
    g = np.array([(Phi_pot(r + d, t) - Phi_pot(r - d, t)) / (2 * hh) for d in np.eye(3) * hh])
    return -g - (A_pot(r, t + hT) - A_pot(r, t - hT)) / (2 * hT)


def Hfield(r, t):
    return curl(A_pot, r, t, hh) / mu_t


eps_space = lambda r, t: 2.0 + np.sin(r[0])      # varies in space only
eps_time = lambda r, t: 2.0 + 0.5 * np.sin(t)     # varies in time
r0, t0 = np.array([0.3, -0.2, 0.5]), 0.4
h2, ht2 = 2e-3, 2e-3
for lab, ef in (("eps(x)", eps_space), ("eps(t)", eps_time)):
    D = lambda r, t, ef=ef: ef(r, t) * Efield(r, t)
    Jf = lambda r, t, D=D: curl(Hfield, r, t, h2) - (D(r, t + ht2) - D(r, t - ht2)) / (2 * ht2)
    w = lambda r, t, ef=ef: 0.5 * ef(r, t) * np.dot(Efield(r, t), Efield(r, t)) + 0.5 * mu_t * np.dot(Hfield(r, t), Hfield(r, t))
    dw = (w(r0, t0 + ht2) - w(r0, t0 - ht2)) / (2 * ht2)
    Sf = lambda r, t: np.cross(Efield(r, t), Hfield(r, t))
    dS = div(Sf, r0, t0, h2)
    JE = np.dot(Jf(r0, t0), Efield(r0, t0))
    res = dw + dS + JE
    extra = 0.5 * np.dot(Efield(r0, t0), Efield(r0, t0)) * (ef(r0, t0 + ht2) - ef(r0, t0 - ht2)) / (2 * ht2)
    print(f"  (e) {lab}: dw/dt + div S + J.E = {res:+.3e}   (1/2 E^2 d(eps)/dt = {extra:+.3e})")
    if lab == "eps(x)":
        check("(e) theorem holds when eps varies in space", abs(res) < 1e-4 * max(abs(dw), abs(dS), abs(JE)))
    else:
        check("(e) eps(t): residual equals -(1/2)E^2 d(eps)/dt (theorem as written fails)", abs(res + extra) < 1e-4 * abs(extra) * 10 + 1e-6 and abs(res) > 1e-3)

# (f) static point charge + magnetic dipole: S != 0, div S = 0, closed-surface flux = 0
q, mvec, rm = 1e-9, np.array([0.0, 0.0, 1.0]), np.array([0.4, 0.0, 0.0])


def Estat(r, t=0.0):
    return q / (4 * np.pi * eps0) * r / np.linalg.norm(r) ** 3


def Hstat(r, t=0.0):
    R = r - rm; Rn = np.linalg.norm(R); Rh = R / Rn
    return (3 * np.dot(mvec, Rh) * Rh - mvec) / (4 * np.pi * Rn ** 3)


Sst = lambda r, t=0.0: np.cross(Estat(r), Hstat(r))
pt = np.array([0.2, 0.3, 0.1])
print(f"  (f) at (0.2,0.3,0.1) m: |S| = {np.linalg.norm(Sst(pt)):.3e} W/m^2, div S = {div(Sst, pt, 0.0, 1e-6):.2e}")
cen, Rs = np.array([0.1, 0.05, -0.1]), 1.0


def flux_int(th, ph):
    n = np.array([np.sin(th) * np.cos(ph), np.sin(th) * np.sin(ph), np.cos(th)])
    return np.dot(Sst(cen + Rs * n), n) * Rs ** 2 * np.sin(th)


with warnings.catch_warnings():          # the net flux is ~0, so quad reports round-off: expected
    warnings.simplefilter("ignore", IntegrationWarning)
    fl = dblquad(flux_int, 0, 2 * np.pi, 0, np.pi, epsabs=1e-16, epsrel=1e-9)[0]
absfl = dblquad(lambda th, ph: abs(flux_int(th, ph)), 0, 2 * np.pi, 0, np.pi, epsabs=1e-16, epsrel=1e-7)[0]
print(f"  (f) closed sphere around both: net flux {fl:.2e} W vs integral of |S.n| dA {absfl:.2e} W")
check("(f) net flux of E x H through a closed surface ~ 0", abs(fl) < 1e-6 * absfl)
print("  Answers: (a) T (b) F (c) T (d) T (e) F (f) F")

# =========================================================================================== 20.2
hdr("20.2 Joule heating at a point: sigma = 0.02 S/m, J = -z 0.1 sin(wt) A/m^2")
sig2, J20 = 0.02, 0.1
E20 = J20 / sig2
print(f"  E = J/sigma = -z {E20:.3f} sin(wt) V/m (parallel to J)")
w2 = 2 * np.pi * 60.0
T2 = 2 * np.pi / w2
JE2 = lambda t: np.dot(-Z * J20 * np.sin(w2 * t), -Z * E20 * np.sin(w2 * t))
ts = np.linspace(0, T2, 200001)
vals = np.array([J20 * E20 * np.sin(w2 * t) ** 2 for t in ts])
print(f"  J.E = {J20*E20:.3f} sin^2(wt) W/m^3; max = {vals.max():.4f} W/m^3 at wt = {w2*ts[vals.argmax()]/np.pi:.4f} pi; min = {vals.min():.2e}")
avg2 = tavg(JE2, T2)
print(f"  <J.E> = {avg2:.5f} W/m^3  (= sigma E0^2/2 = {sig2*E20**2/2:.5f}, = J0^2/(2 sigma) = {J20**2/(2*sig2):.5f}); per litre {avg2*1e-3*1e3:.3f} mW")
check("20.2 max 0.5, avg 0.25", np.isclose(vals.max(), 0.5) and np.isclose(avg2, 0.25))
print(f"  <J><E> = {tavg(lambda t: -J20*np.sin(w2*t), T2) * tavg(lambda t: -E20*np.sin(w2*t), T2):.2e} (product of averages, not the average)")
print(f"  (d) same E, 2 sigma: <J.E> = {2*sig2*E20**2/2:.4f} W/m^3 ; same J, 2 sigma: <J.E> = {J20**2/(2*2*sig2):.4f} W/m^3")
check("20.2(d) 0.5 and 0.125", np.isclose(2 * sig2 * E20 ** 2 / 2, 0.5) and np.isclose(J20 ** 2 / (4 * sig2), 0.125))

# =========================================================================================== 20.3
hdr("20.3 Laser beam: E = z 240 pi cos(wt + beta y) V/m in air, A = 1 mm^2 (course constants)")
E03 = 240 * np.pi
f3 = 1e9                                  # any frequency; FD check uses 1 GHz
w3, b3 = 2 * np.pi * f3, 2 * np.pi * f3 / cC
u3 = -Y                                   # wt + beta y -> travel -y
E3 = lambda r, t: Z * E03 * np.cos(w3 * t + b3 * r[1])
H3 = lambda r, t: np.cross(u3, E3(r, t)) / etaC
print(f"  E0 = {E03:.3f} V/m, travel {dname(u3)} (wt + beta y)")
print(f"  H = u x E / eta0: (-y) x z = {dname(np.cross(-Y, Z))}; H0 = E0/eta0 = {E03/etaC:.6f} A/m")
print(f"  E x H direction: {dname(np.cross(Z, np.cross(u3, Z)))}")
maxwell("20.3 fields (mu0, eps0 course)", E3, H3, mu0, eps0C, [(np.random.default_rng(3).uniform(-1, 1, 3), 1.3e-10 * k) for k in range(5)], 1e-5, 1e-14)
Speak = E03 * E03 / etaC
print(f"  S = {dname(np.cross(Z, -X))} {Speak:.2f} cos^2(...) W/m^2 (= 480 pi = {480*np.pi:.2f})")
T3 = 1 / f3
avgS3 = tavg(lambda t: np.cross(E3(np.zeros(3), t), H3(np.zeros(3), t))[1], T3)
print(f"  <S_y> by quadrature = {avgS3:.4f} W/m^2 (= -240 pi = {-240*np.pi:.4f})")
check("20.3 <S> = -y 240 pi", np.isclose(avgS3, -240 * np.pi))
P3 = 240 * np.pi * 1e-6
print(f"  P = <S> A = {P3*1e3:.4f} mW")
w3avg = 240 * np.pi / cC
w3b = tavg(lambda t: 0.5 * eps0C * np.dot(E3(np.zeros(3), t), E3(np.zeros(3), t)) + 0.5 * mu0 * np.dot(H3(np.zeros(3), t), H3(np.zeros(3), t)), T3)
print(f"  <w> = <S>/c = {w3avg:.5e} J/m^3 (8 pi e-7 = {8*np.pi*1e-7:.5e}); by quadrature of 1/2 eps0 E^2 + 1/2 mu0 H^2: {w3b:.5e}")
print(f"  1/2 eps0 E0^2 = {0.5*eps0C*E03**2:.5e} J/m^3 (electric + magnetic averages: {0.25*eps0C*E03**2:.4e} + {0.25*mu0*(E03/etaC)**2:.4e})")
check("20.3 <w> = 8 pi e-7", np.isclose(w3b, 8 * np.pi * 1e-7, rtol=1e-9))
print(f"  energy in 1 m of beam = <w> A (1 m) = {w3avg*1e-6:.4e} J = P/c = {P3/cC:.4e} J")
print(f"  ratio to sunlight 1361 W/m^2: {240*np.pi/1361:.3f} ; light needs {1/cC*1e9:.2f} ns per metre")

# =========================================================================================== 20.4
hdr("20.4 Standing wave from y E0 cos(wt - bx) + y E0 cos(wt + bx), free space")
E04, f4 = 1.0, 1e8
w4, b4 = 2 * np.pi * f4, 2 * np.pi * f4 / c
lam4, T4 = 2 * np.pi / b4, 1 / f4
E4a = lambda r, t: Y * E04 * np.cos(w4 * t - b4 * r[0])
H4a = lambda r, t: np.cross(X, E4a(r, t)) / eta0
E4b = lambda r, t: Y * E04 * np.cos(w4 * t + b4 * r[0])
H4b = lambda r, t: np.cross(-X, E4b(r, t)) / eta0
E4 = lambda r, t: E4a(r, t) + E4b(r, t)
H4 = lambda r, t: H4a(r, t) + H4b(r, t)
rng = np.random.default_rng(4)
okf = True
for k in range(6):
    r = rng.uniform(-3, 3, 3); t = rng.uniform(0, 3 * T4)
    okf &= np.allclose(E4(r, t), Y * 2 * E04 * np.cos(w4 * t) * np.cos(b4 * r[0]), atol=1e-12)
    okf &= np.allclose(H4(r, t), Z * 2 * E04 / eta0 * np.sin(w4 * t) * np.sin(b4 * r[0]), atol=1e-14)
    okf &= np.allclose(np.cross(E4(r, t), H4(r, t)), X * E04 ** 2 / eta0 * np.sin(2 * w4 * t) * np.sin(2 * b4 * r[0]), atol=1e-14)
check("20.4 E = y 2E0 cos wt cos bx, H = z (2E0/eta0) sin wt sin bx, S = x (E0^2/eta0) sin 2wt sin 2bx", okf)
print(f"  H of the -x wave: (-x) x y = {dname(np.cross(-X, Y))}")
maxwell("20.4 standing wave", E4, H4, mu0, eps0, [(rng.uniform(-2, 2, 3), rng.uniform(0, T4)) for _ in range(5)], 1e-4, 1e-13)
xa = 0.1 * lam4
Sx = lambda t: np.cross(E4(np.array([xa, 0, 0]), t), H4(np.array([xa, 0, 0]), t))[0]
print(f"  (a) at x = 0.1 lambda, t = T/8: S_x = {Sx(T4/8):.4e} W/m^2 (nonzero) ; at t = 3T/8: {Sx(3*T4/8):.4e}")
check("(a) S not identically zero", abs(Sx(T4 / 8)) > 1e-4)
avgs = [tavg(lambda t, x=x: np.cross(E4(np.array([x, 0, 0]), t), H4(np.array([x, 0, 0]), t))[0], T4) for x in (0.05 * lam4, 0.13 * lam4, 0.31 * lam4)]
print(f"  (b) <S_x> at three x: {avgs}")
check("(b) <S> = 0", max(abs(a) for a in avgs) < 1e-12)
w4f = lambda r, t: 0.5 * eps0 * np.dot(E4(r, t), E4(r, t)) + 0.5 * mu0 * np.dot(H4(r, t), H4(r, t))
avw = [tavg(lambda t, x=x: w4f(np.array([x, 0, 0]), t), T4) for x in (0.0, 0.1 * lam4, 0.25 * lam4, 0.4 * lam4)]
print(f"  (c) <w> at x = 0, 0.1, 0.25, 0.4 lambda: {[f'{a:.6e}' for a in avw]}  ; eps0 E0^2 = {eps0*E04**2:.6e}")
check("(c) <w> = eps0 E0^2 everywhere (not zero)", np.allclose(avw, eps0 * E04 ** 2, rtol=1e-9))
xn = lam4 / 4      # E node: cos(bx) = 0
wn = [w4f(np.array([xn, 0, 0]), t) for t in (0, T4 / 8, T4 / 4, T4 / 2)]
print(f"  (d) at the E node x = lambda/4: |E| = {np.linalg.norm(E4(np.array([xn,0,0]), 0.3*T4)):.1e}; w(t = 0, T/8, T/4, T/2) = {wn}")
print(f"      2 eps0 E0^2 sin^2(wt) at T/8: {2*eps0*E04**2*np.sin(w4*T4/8)**2:.6e}; at T/4: {2*eps0*E04**2:.6e}")
check("(d) w at E node = 2 eps0 E0^2 sin^2 wt (not always 0)", np.isclose(wn[2], 2 * eps0 * E04 ** 2) and wn[0] < 1e-30)
Wseg = [quad(lambda x, t=t: w4f(np.array([x, 0, 0]), t), lam4 / 4, 3 * lam4 / 4, epsabs=0, epsrel=1e-11)[0] for t in (0, 0.1 * T4, 0.3 * T4, 0.77 * T4)]
print(f"  (e) energy between E nodes lambda/4 .. 3lambda/4 at four times: {[f'{a:.8e}' for a in Wseg]} ; eps0 E0^2 lambda/2 = {eps0*E04**2*lam4/2:.8e}")
print(f"      S_x at the nodes: {np.cross(E4(np.array([lam4/4,0,0]), 0.13*T4), H4(np.array([lam4/4,0,0]), 0.13*T4))[0]:.2e}, {np.cross(E4(np.array([3*lam4/4,0,0]), 0.13*T4), H4(np.array([3*lam4/4,0,0]), 0.13*T4))[0]:.2e}")
check("(e) constant energy between nodes", np.allclose(Wseg, eps0 * E04 ** 2 * lam4 / 2, rtol=1e-8))
E4c = lambda r, t: E4a(r, t) + 0.5 * E4b(r, t)
H4c = lambda r, t: H4a(r, t) + 0.5 * H4b(r, t)
avgf = tavg(lambda t: np.cross(E4c(np.array([0.37, 0, 0]), t), H4c(np.array([0.37, 0, 0]), t))[0], T4)
print(f"  (f) amplitude E0/2 for the -x wave: <S_x> = {avgf:.6e} vs 3 E0^2/(8 eta0) = {3*E04**2/(8*eta0):.6e}")
check("(f) <S> = 3E0^2/(8 eta0) along +x", np.isclose(avgf, 3 * E04 ** 2 / (8 * eta0), rtol=1e-9))
print("  Answers: (a) F (b) T (c) F (d) F (e) T (f) T")

# =========================================================================================== 20.5
hdr("20.5 Find the error: isotropic 6 kW transmitter, E_min = 10 mV/m (eta0 = 120 pi)")
P5, Em5 = 6000.0, 0.01
r_student = np.sqrt(etaC * P5 / (4 * np.pi)) / Em5
r_correct = np.sqrt(etaC * P5 / (2 * np.pi)) / Em5
print(f"  eta0/(4 pi) = {etaC/(4*np.pi):.4f} ; eta0/(2 pi) = {etaC/(2*np.pi):.4f}")
print(f"  student: r = sqrt(30 P)/E = sqrt({30*P5:.0f})/0.01 = {r_student/1e3:.3f} km")
print(f"  correct: r = sqrt(60 P)/E = sqrt({60*P5:.0f}) / 0.01 = {np.sqrt(60*P5):.3f}/0.01 = {r_correct/1e3:.3f} km ; ratio {r_correct/r_student:.5f} = sqrt 2")
rb = brentq(lambda r: np.sqrt(2 * etaC * P5 / (4 * np.pi * r ** 2)) - Em5, 1e3, 1e6)
print(f"  brute force: E0(r) = sqrt(2 eta0 <S>) = 10 mV/m at r = {rb/1e3:.6f} km")
check("20.5 range 60 km", np.isclose(rb, 6e4))
S60 = P5 / (4 * np.pi * 6e4 ** 2)
print(f"  at 60 km: <S> = {S60:.4e} W/m^2 ; E0^2/(2 eta0) = {Em5**2/(2*etaC):.4e}")
print(f"  field at 60 km if r were 42.4 km... student's E0 at 60 km would be {np.sqrt(etaC*S60):.5f} V/m (= rms value {Em5/np.sqrt(2):.5f})")

# =========================================================================================== 20.6
hdr("20.6 Split, then add: E = x 6 cos(wt + bz) - y 8 sin(wt + bz) V/m, eps_r = 4, f = 75 MHz")
f6, er6 = 75e6, 4.0
v6 = cC / np.sqrt(er6); eta6 = etaC / np.sqrt(er6)
w6 = 2 * np.pi * f6; b6 = w6 / v6
print(f"  v = {v6:.4e} m/s, eta = {eta6:.4f} Ohm (60 pi = {60*np.pi:.4f}), beta = {b6:.6f} rad/m (pi = {np.pi:.6f}), lambda = {2*np.pi/b6:.4f} m")
u6 = -Z
E6 = lambda r, t: X * 6 * np.cos(w6 * t + b6 * r[2]) - Y * 8 * np.sin(w6 * t + b6 * r[2])
H6 = lambda r, t: np.cross(u6, E6(r, t)) / eta6
print(f"  (-z) x x = {dname(np.cross(-Z, X))} ; (-z) x (-y) = {dname(np.cross(-Z, -Y))} ; x x (-y) = {dname(np.cross(X, -Y))} ; (-y) x (-x) = {dname(np.cross(-Y, -X))}")
print(f"  H amplitudes: 6/eta = {6/eta6:.6f} (1/(10 pi) = {1/(10*np.pi):.6f}), 8/eta = {8/eta6:.6f} (2/(15 pi) = {2/(15*np.pi):.6f}) A/m")
r6, t6 = np.array([0.1, 0.2, 0.3]), 1.234e-9
ph = w6 * t6 + b6 * r6[2]
close("H = -y 0.0318 cos - x 0.0424 sin", H6(r6, t6), -Y * (6 / eta6) * np.cos(ph) - X * (8 / eta6) * np.sin(ph), rtol=1e-12)
maxwell("20.6 fields (mu0, 4 eps0 course)", E6, H6, mu0, er6 * eps0C, [(np.random.default_rng(6).uniform(-1, 1, 3), 1e-9 * k) for k in range(5)], 1e-5, 1e-13)
T6 = 1 / f6
E1 = lambda r, t: X * 6 * np.cos(w6 * t + b6 * r[2])
H1 = lambda r, t: np.cross(u6, E1(r, t)) / eta6
S1 = tavg(lambda t: np.cross(E1(np.zeros(3), t), H1(np.zeros(3), t))[2], T6)
E2_ = lambda r, t: -Y * 8 * np.sin(w6 * t + b6 * r[2])
H2_ = lambda r, t: np.cross(u6, E2_(r, t)) / eta6
S2 = tavg(lambda t: np.cross(E2_(np.zeros(3), t), H2_(np.zeros(3), t))[2], T6)
Sall = tavg(lambda t: np.cross(E6(np.array([0, 0, 0.7]), t), H6(np.array([0, 0, 0.7]), t))[2], T6)
print(f"  (c) <E1 x H1>_z = {S1:.6f} W/m^2 ; 36/(2 eta) = {36/(2*eta6):.6f} ; 3/(10 pi) = {3/(10*np.pi):.6f}")
print(f"      y part alone: {S2:.6f} W/m^2 ; 8/(15 pi) = {8/(15*np.pi):.6f}")
print(f"  (d) <E x H>_z = {Sall:.6f} W/m^2 ; 100/(2 eta) = {100/(2*eta6):.6f} ; 5/(6 pi) = {5/(6*np.pi):.6f}")
check("(c),(d) -z 0.0955 and -z 0.265, sum of parts", np.isclose(S1, -3 / (10 * np.pi)) and np.isclose(Sall, -5 / (6 * np.pi)) and np.isclose(S1 + S2, Sall))
tt = np.linspace(0, T6, 400001)
Sm = np.array([np.linalg.norm(np.cross(E6(np.zeros(3), t), H6(np.zeros(3), t))) for t in tt[::40]])
tsub = tt[::40]
print(f"  (e) |S| at z = 0: min {Sm.min():.5f} at wt = {w6*tsub[Sm.argmin()]/np.pi:.4f} pi ; max {Sm.max():.5f} at wt = {w6*tsub[Sm.argmax()]/np.pi:.4f} pi")
print(f"      36/eta = {36/eta6:.5f}, 64/eta = {64/eta6:.5f}; single linear wave of amplitude 10: 0 .. {100/eta6:.5f}")
check("(e) min 36/eta, max 64/eta", np.isclose(Sm.min(), 36 / eta6, rtol=1e-6) and np.isclose(Sm.max(), 64 / eta6, rtol=1e-6))
print(f"      E at wt = 0: {E6(np.zeros(3), 0.0)} ; at wt = pi/2: {np.round(E6(np.zeros(3), T6/4), 9)}")
print(f"  (f) window 0.5 m x 0.5 m: P = {abs(Sall)*0.25*1e3:.3f} mW ; 5/(24 pi) = {5/(24*np.pi)*1e3:.3f} mW")
w6avg = tavg(lambda t: 0.5 * er6 * eps0C * np.dot(E6(np.zeros(3), t), E6(np.zeros(3), t)) + 0.5 * mu0 * np.dot(H6(np.zeros(3), t), H6(np.zeros(3), t)), T6)
print(f"  check: <w> = {w6avg:.5e} J/m^3 (50 eps = {50*er6*eps0C:.5e}); v <w> = {v6*w6avg:.6f} W/m^2")
check("v<w> = <S>", np.isclose(v6 * w6avg, 5 / (6 * np.pi)))

# =========================================================================================== 20.7
hdr("20.7 Leaky spherical capacitor: a = 1 cm, b = 3 cm, eps = 6 eps0, sigma = 2e-7 S/m, V0 = 1 kV")
a7, b7, er7, s7, V07 = 0.01, 0.03, 6.0, 2e-7, 1000.0
e7 = er7 * eps0
tau7 = e7 / s7
C7 = 4 * np.pi * e7 * a7 * b7 / (b7 - a7)
Q07 = C7 * V07
print(f"  tau = eps/sigma = {tau7*1e6:.2f} us ; C = 4 pi eps ab/(b-a) = {C7*1e12:.4f} pF ; Q0 = {Q07*1e9:.4f} nC")
K7 = V07 * a7 * b7 / (b7 - a7)
print(f"  E(r,t) = r_hat K/r^2 e^(-t/tau), K = V0 ab/(b-a) = {K7:.4f} V m ; Q0/(4 pi eps) = {Q07/(4*np.pi*e7):.4f}")
Ea = K7 / a7 ** 2
print(f"  E(a,0) = {Ea:.4e} V/m ; E(b,0) = {K7/b7**2:.4e} V/m")
print(f"  J = sigma E = r_hat {s7*K7:.3e}/r^2 e^(-t/tau) A/m^2 ; J(a,0) = {s7*Ea:.4f} A/m^2")
E7 = lambda r, t: K7 * np.exp(-t / tau7) / np.linalg.norm(r) ** 2 * r / np.linalg.norm(r)
rp, tp = np.array([0.012, 0.009, -0.005]), 0.7 * tau7
dD = e7 * ddt(E7, rp, tp, 1e-9 * tau7)
Jp = s7 * E7(rp, tp)
print(f"  at a test point: J = {Jp}, dD/dt = {dD} -> J + dD/dt = {Jp + dD}")
check("20.7 J + dD/dt = 0 (no source for curl H)", np.linalg.norm(Jp + dD) < 1e-6 * np.linalg.norm(Jp))
wa = 0.5 * e7 * Ea ** 2
print(f"  w(a,0) = {wa:.4f} J/m^3 ; J.E(a,0) = sigma E^2 = {s7*Ea**2:.2f} W/m^3 ; 2w/tau = {2*wa/tau7:.2f}")
wfun = lambda t: 0.5 * e7 * np.dot(E7(rp, t), E7(rp, t))
dw7 = (wfun(tp + 1e-6 * tau7) - wfun(tp - 1e-6 * tau7)) / (2e-6 * tau7)
print(f"  dw/dt (FD) = {dw7:.6e} ; -sigma E^2 = {-s7*np.dot(E7(rp,tp),E7(rp,tp)):.6e}")
check("20.7 dw/dt = -J.E", np.isclose(dw7, -s7 * np.dot(E7(rp, tp), E7(rp, tp)), rtol=1e-6))
W07 = 0.5 * C7 * V07 ** 2
Wint = quad(lambda r: 0.5 * e7 * (K7 / r ** 2) ** 2 * 4 * np.pi * r ** 2, a7, b7)[0]
P07 = quad(lambda r: s7 * (K7 / r ** 2) ** 2 * 4 * np.pi * r ** 2, a7, b7)[0]
G7 = 4 * np.pi * s7 * a7 * b7 / (b7 - a7)
print(f"  W(0) = 1/2 C V0^2 = {W07*1e6:.4f} uJ ; by integrating 1/2 eps E^2 dV: {Wint*1e6:.4f} uJ")
print(f"  P(0) = int sigma E^2 dV = {P07*1e3:.4f} mW ; G V0^2 = {G7*V07**2*1e3:.4f} mW (G = {G7:.4e} S) ; 2W0/tau = {2*W07/tau7*1e3:.4f} mW")
heat = quad(lambda t: P07 * np.exp(-2 * t / tau7), 0, 50 * tau7)[0]
print(f"  total heat int_0^inf P dt = {heat*1e6:.4f} uJ")
check("20.7 total heat = W(0)", np.isclose(heat, W07, rtol=1e-8) and np.isclose(Wint, W07))
th_e = brentq(lambda t: np.exp(-2 * t / tau7) - 0.5, 0, 5 * tau7)
th_q = brentq(lambda t: np.exp(-t / tau7) - 0.5, 0, 5 * tau7)
print(f"  half the energy at {th_e*1e6:.2f} us ((tau/2) ln 2) ; half the charge at {th_q*1e6:.2f} us (tau ln 2)")
print("  H = 0 by symmetry and J + dD/dt = 0 -> S = 0")

# =========================================================================================== 20.8
hdr("20.8 Ramping solenoid: n = 1000 /m, a = 2 cm, I = k t, k = 50 A/s, t = 0.2 s")
n8, a8, k8, t8 = 1000.0, 0.02, 50.0, 0.2


def E8(r, t):
    x, y, _ = r
    return -(mu0 * n8 * k8 / 2) * np.array([-y, x, 0.0])     # = -phi_hat mu0 n k r / 2


def H8(r, t):
    return Z * n8 * k8 * t


rr8 = np.array([0.006, -0.008, 0.3])   # r = 1 cm
cE = curl(E8, rr8, t8, 1e-5); dHt = -mu0 * ddt(H8, rr8, t8, 1e-3)
print(f"  curl E = {cE} ; -mu0 dH/dt = {dHt}")
check("20.8 Faraday inside", np.allclose(cE, dHt, rtol=1e-6))
print(f"  curl H = {curl(H8, rr8, t8, 1e-5)} ; eps0 dE/dt = {eps0*ddt(E8, rr8, t8, 1e-3)} (both 0: Ampere-Maxwell holds with J = 0)")
Ephia = mu0 * n8 * k8 * a8 / 2
print(f"  E_phi(a) = -mu0 n k a/2 = -{Ephia:.4e} V/m ; I(0.2 s) = {k8*t8:.1f} A ; H = n I = {n8*k8*t8:.0f} A/m")
ra8 = np.array([a8, 0, 0])
S8 = np.cross(E8(ra8, t8), H8(ra8, t8))
print(f"  S at r = a (on +x axis): {S8} W/m^2 -> {dname(S8)} (inward), |S| = {np.linalg.norm(S8):.4f} ; mu0 n^2 k^2 a t/2 = {mu0*n8**2*k8**2*a8*t8/2:.4f}")
print(f"  phi_hat x z_hat on +x axis: phi=+y: {dname(np.cross(Y, Z))} = r_hat")
dw8, dS8, JE8 = poynting_point("20.8 point form at r = 1 cm", E8, H8, mu0, eps0, rr8, t8, 1e-5, 1e-3)
print(f"  mu0 n^2 k^2 t = {mu0*n8**2*k8**2*t8:.5f} W/m^3")
HcE = np.dot(H8(rr8, t8), curl(E8, rr8, t8, 1e-5)); EcH = np.dot(E8(rr8, t8), curl(H8, rr8, t8, 1e-5))
print(f"  H.(curl E) = {HcE:.5f} ; E.(curl H) = {EcH:.2e} ; H.curlE - E.curlH = {HcE-EcH:.5f} vs div S = {dS8:.5f}")
check("20.8 identity", np.isclose(HcE - EcH, dS8, rtol=1e-6))
Pin = quad(lambda ph: -np.dot(np.cross(E8(a8 * np.array([np.cos(ph), np.sin(ph), 0]), t8), H8(0, t8)), np.array([np.cos(ph), np.sin(ph), 0])) * a8, 0, 2 * np.pi)[0]
L8 = mu0 * n8 ** 2 * np.pi * a8 ** 2
print(f"  power in through r = a per metre (surface integral) = {Pin:.5f} W/m ; script-L = {L8:.5e} H/m ; L I k = {L8*k8*t8*k8:.5f} W/m")
check("20.8 inflow = d/dt(1/2 L I^2)", np.isclose(Pin, L8 * k8 * t8 * k8, rtol=1e-8))
Js8 = np.array([0, 1, 0]) * n8 * k8 * t8          # phi_hat at (a,0,0) is +y
print(f"  winding: Js = phi_hat {n8*k8*t8:.0f} A/m, E(a) = {E8(ra8, t8)} -> Js.E = {np.dot(Js8, E8(ra8, t8)):.4f} W/m^2")
check("20.8 -Js.E = inward |S| at a", np.isclose(-np.dot(Js8, E8(ra8, t8)), np.linalg.norm(S8)))
print(f"  electric energy density 1/2 eps0 E^2 at r = a: {0.5*eps0*Ephia**2:.2e} J/m^3 (constant in time)")

# =========================================================================================== 20.9
hdr("20.9 Coax with resistive inner conductor: a = 1 mm, b = 4 mm, R' = 1 Ohm/m, l = 10 m, V0 = 100 V, RL = 40 Ohm")
a9, b9, Rp, l9, V09, RL9 = 1e-3, 4e-3, 1.0, 10.0, 100.0, 40.0
sig9 = 1 / (np.pi * a9 ** 2 * Rp)
print(f"  sigma = 1/(pi a^2 R') = {sig9:.4e} S/m")
I9 = V09 / (Rp * l9 + RL9)
Vz = lambda z: V09 - I9 * Rp * z
print(f"  I = {I9:.3f} A ; V(z) = {V09:.0f} - {I9*Rp:.0f} z V ; V(l) = {Vz(l9):.1f} V = I RL = {I9*RL9:.1f} V")
print(f"  powers: battery {V09*I9:.1f} W ; inner conductor I^2 R' l = {I9**2*Rp*l9:.1f} W ; load {Vz(l9)*I9:.1f} W")
L4 = np.log(b9 / a9)
Phi9 = lambda r, z: Vz(z) * np.log(b9 / r) / L4


def Phi9c(p):
    return Phi9(np.hypot(p[0], p[1]), p[2])


def E9(p, t=0.0):
    hh9 = 1e-7
    return -np.array([(Phi9c(p + d) - Phi9c(p - d)) / (2 * hh9) for d in np.eye(3) * hh9])


def H9(p, t=0.0):
    r = np.hypot(p[0], p[1])
    return I9 / (2 * np.pi * r) * np.array([-p[1], p[0], 0.0]) / r


p9 = np.array([1.7e-3, 1.1e-3, 3.0])
hl = 1e-6
terms = [(Phi9c(p9 + d) - 2 * Phi9c(p9) + Phi9c(p9 - d)) / hl ** 2 for d in np.eye(3) * hl]
lap = sum(terms)
print(f"  Laplacian of Phi at a test point (FD, h = 1 um): d2/dx2 {terms[0]:.4e}, d2/dy2 {terms[1]:.4e}, d2/dz2 {terms[2]:.2e}; sum {lap:.2e} V/m^2")
check("20.9 Phi satisfies Laplace", abs(lap) < 1e-6 * max(abs(t) for t in terms))
Er = lambda r, z: Vz(z) / (r * L4)
Ez = lambda r, z: I9 * Rp * np.log(b9 / r) / L4
pa = np.array([a9 * (1 + 1e-6), 0, 0.0])
print(f"  E at r = a+, z = 0 (FD): {E9(pa)} ; formulas E_r = {Er(a9,0):.4e}, E_z = {Ez(a9,0):.6f} V/m")
print(f"  inside the inner conductor E_z = J/sigma = I/(sigma pi a^2) = {I9/(sig9*np.pi*a9**2):.6f} V/m = I R' = {I9*Rp:.3f}")
check("20.9 E_z continuous at r = a", np.isclose(Ez(a9, 0), I9 / (sig9 * np.pi * a9 ** 2)))
pb = np.array([0, b9 * (1 - 1e-9), 4.0])
print(f"  E_z at r = b- (FD): {E9(pb)[2]:.2e} V/m ; E_r(a, z=0) = {Er(a9,0)/1e3:.2f} kV/m ; E_r(a, z=l) = {Er(a9,l9)/1e3:.2f} kV/m ; ln 4 = {L4:.4f}")
check("20.9 tangential E = 0 at r = b", abs(E9(pb)[2]) < 1e-4)
print(f"  H(a) = I/(2 pi a) = {I9/(2*np.pi*a9):.2f} A/m along phi_hat")
print(f"  r_hat x phi_hat = {dname(np.cross(X, Y))} ; z_hat x phi_hat (phi=+y at +x axis) = {dname(np.cross(Z, Y))}")
for z in (0.0, l9):
    Pz = quad(lambda r: Vz(z) * I9 / (2 * np.pi * r ** 2 * L4) * 2 * np.pi * r, a9, b9)[0]
    pt9 = np.array([a9 * 1.0000001, 0, z])
    Sv = np.cross(E9(pt9), H9(pt9))
    print(f"  z = {z:4.1f} m: power through cross-section = {Pz:.4f} W (V I = {Vz(z)*I9:.1f}) ; S at r = a+: {Sv} W/m^2")
print(f"  S_z(a, 0) = V I/(2 pi a^2 ln 4) = {Vz(0)*I9/(2*np.pi*a9**2*L4):.4e} W/m^2")
Sra = -I9 ** 2 * Rp / (2 * np.pi * a9)
print(f"  S_r(a+) = -I^2 R'/(2 pi a) = {Sra:.3f} W/m^2 ; times 2 pi a = {Sra*2*np.pi*a9:.4f} W/m (= -I^2 R')")
pbb = np.array([b9 * (1 - 1e-9), 0, 5.0])
print(f"  S_r(b-) = {np.cross(E9(pbb), H9(pbb))[0]:.2e} W/m^2")
check("20.9 S_r(a) and S_r(b)", np.isclose(np.cross(E9(np.array([a9, 0, 5.0])), H9(np.array([a9, 0, 5.0])))[0], Sra, rtol=1e-5)
      and abs(np.cross(E9(pbb), H9(pbb))[0]) < 1e-3)
# ring ledger z in [2, 3] m: outward flux of S through the 4 surfaces
z1, z2 = 2.0, 3.0
Sfun = lambda r, z: np.cross(E9(np.array([r, 0, z])), H9(np.array([r, 0, z])))
f_end2 = quad(lambda r: Sfun(r, z2)[2] * 2 * np.pi * r, a9, b9, epsrel=1e-10)[0]
f_end1 = quad(lambda r: -Sfun(r, z1)[2] * 2 * np.pi * r, a9, b9, epsrel=1e-10)[0]
f_in = fixed_quad(lambda zz: np.array([-Sfun(a9, z)[0] for z in zz]) * 2 * np.pi * a9, z1, z2, n=20)[0]   # outward normal -r_hat
f_out = fixed_quad(lambda zz: np.array([Sfun(b9 * (1 - 1e-12), z)[0] for z in zz]) * 2 * np.pi * b9, z1, z2, n=20)[0]
print(f"  ring 2 m < z < 3 m: out through z = 3: {f_end2:.5f} W ; through z = 2: {f_end1:.5f} W ; into the wire (r = a): {f_in:.5f} W ; r = b: {f_out:.2e} W")
print(f"  net outflow = {f_end2+f_end1+f_in+f_out:.2e} W (no storage, J = 0 in the dielectric)")
check("20.9 ring ledger balances", abs(f_end2 + f_end1 + f_in + f_out) < 1e-6)
rat0 = Ez(a9, 0) / Er(a9, 0); ratl = Ez(a9, l9) / Er(a9, l9)
print(f"  |S_r|/S_z at r = a: z = 0: {rat0:.4e} ({np.degrees(np.arctan(rat0)):.5f} deg) ; z = l: {ratl:.4e} ({np.degrees(np.arctan(ratl)):.5f} deg)")

# =========================================================================================== 20.10
hdr("20.10 Sheet on y = 0, Js = -x u(t) sin(wt) A/m, f = 2.5 MHz, mu_r = eps_r = 4")
mur, epr, f10 = 4.0, 4.0, 2.5e6
mu10, ep10 = mur * mu0, epr * eps0C
v10, eta10 = 1 / np.sqrt(mu10 * ep10), np.sqrt(mu10 / ep10)
w10 = 2 * np.pi * f10; b10 = w10 / v10; T10 = 1 / f10
print(f"  v = {v10:.4e} m/s ({v10/1e6:.1f} m/us), eta = {eta10:.4f} Ohm (120 pi = {120*np.pi:.4f}), omega = {w10:.4e} (5 pi e6 = {5*np.pi*1e6:.4e})")
print(f"  beta = {b10:.6f} rad/m (pi/15 = {np.pi/15:.6f}), lambda = {2*np.pi/b10:.4f} m, T = {T10*1e6:.2f} us")
J0 = 1.0
u_ = lambda t: 1.0 if t > 0 else 0.0
g10 = lambda t: J0 * u_(t) * np.sin(w10 * t)
Jdir = -X


def sheetfields(Jdir, g, mu, ep, p0=np.zeros(3), nvec=Y):
    v, eta = 1 / np.sqrt(mu * ep), np.sqrt(mu / ep)

    def E(r, t):
        s = np.dot(np.asarray(r, float) - p0, nvec)
        return -eta / 2 * Jdir * g(t - abs(s) / v)

    def H(r, t):
        s = np.dot(np.asarray(r, float) - p0, nvec)
        n = nvec if s > 0 else -nvec
        return 0.5 * np.cross(Jdir, n) * g(t - abs(s) / v)
    return E, H


E10, H10 = sheetfields(Jdir, g10, mu10, ep10)
print(f"  E amplitude eta J0/2 = {eta10*J0/2:.4f} V/m (60 pi = {60*np.pi:.4f}) ; H amplitude J0/2 = {J0/2}")
print(f"  y>0: (-x) x y = {dname(np.cross(-X, Y))} ; y<0: (-x) x (-y) = {dname(np.cross(-X, -Y))} ; E direction {dname(-eta10/2*Jdir)}")
print(f"  E x H: y>0 {dname(np.cross(X, -Z))}, y<0 {dname(np.cross(X, Z))}")
rng10 = np.random.default_rng(10)
pts10 = []
while len(pts10) < 6:
    r = rng10.uniform(-30, 30, 3); t = rng10.uniform(1.2e-6, 3e-6)
    if abs(r[1]) > 1 and t - abs(r[1]) / v10 > 0.05e-6:
        pts10.append((r, t))
maxwell("20.10 fields behind the front", E10, H10, mu10, ep10, pts10, 1e-3, 1e-11)
tt0 = 0.37e-6
jump = np.cross(Y, H10(np.array([0, 1e-9, 0]), tt0) - H10(np.array([0, -1e-9, 0]), tt0))
print(f"  jump y x (H+ - H-) at t = 0.37 us: {jump} ; Js = {Jdir*g10(tt0)}")
check("20.10 jump condition", np.allclose(jump, Jdir * g10(tt0), atol=1e-8))
JsE = lambda t: np.dot(Jdir * g10(t), E10(np.array([0, 1e-12, 0]), t))
tA = 10 * T10
print(f"  Js.E at wt = pi/2 (t = {tA*1e6 + T10/4*1e6:.2f} us): {JsE(tA + T10/4):.4f} W/m^2 (-60 pi = {-60*np.pi:.4f})")
avgJE10 = tavg(JsE, T10, tA)
print(f"  <Js.E> = {avgJE10:.4f} W/m^2 (-30 pi = {-30*np.pi:.4f})")
check("20.10 <Js.E> = -30 pi", np.isclose(avgJE10, -30 * np.pi))
Sp = tavg(lambda t: np.cross(E10(np.array([0, 20.0, 0]), t), H10(np.array([0, 20.0, 0]), t))[1], T10, tA)
Sm_ = tavg(lambda t: np.cross(E10(np.array([0, -20.0, 0]), t), H10(np.array([0, -20.0, 0]), t))[1], T10, tA)
print(f"  <S_y> at y = +20 m: {Sp:.4f} ; at y = -20 m: {Sm_:.4f} W/m^2 (15 pi = {15*np.pi:.4f})")
check("20.10 <S> = +-y 15 pi; balance", np.isclose(Sp, 15 * np.pi) and np.isclose(Sm_, -15 * np.pi) and np.isclose(Sp - Sm_, -avgJE10))
tq = tA + 0.123 * T10
Sup = np.cross(E10(np.array([0, 1e-12, 0]), tq), H10(np.array([0, 1e-12, 0]), tq))[1]
Sdn = np.cross(E10(np.array([0, -1e-12, 0]), tq), H10(np.array([0, -1e-12, 0]), tq))[1]
print(f"  instant check at the sheet: S(0+) - S(0-) = {Sup - Sdn:.4f} ; -Js.E = {-JsE(tq):.4f} ; peak S per side 30 pi = {30*np.pi:.4f}")
check("20.10 instantaneous sheet balance", np.isclose(Sup - Sdn, -JsE(tq)))
w10f = lambda t: 0.5 * ep10 * np.dot(E10(np.array([0, 20.0, 0]), t), E10(np.array([0, 20.0, 0]), t)) + 0.5 * mu10 * np.dot(H10(np.array([0, 20.0, 0]), t), H10(np.array([0, 20.0, 0]), t))
wav = tavg(w10f, T10, tA)
print(f"  <w> behind the front = {wav:.5e} J/m^3 (2 pi e-7 = {2*np.pi*1e-7:.5e}) ; <S>/<w> = {Sp/wav:.5e} m/s")
check("20.10 <S>/<w> = v", np.isclose(Sp / wav, v10))
print(f"  vacuum, same current: E0 = {etaC*J0/2:.2f}, H0 = {J0/2}, <S> = {etaC*J0**2/8:.4f} (15 pi), <w> = {etaC*J0**2/8/cC:.4e} J/m^3, lambda = {cC/f10:.0f} m")
print(f"  ratios medium/vacuum: <w> {wav/(etaC*J0**2/8/cC):.4f}, lambda {(2*np.pi/b10)/(cC/f10):.4f}")
g10b = lambda t: u_(t) * (np.sin(w10 * t) + 0.5 * np.sin(3 * w10 * t))
E10b, H10b = sheetfields(Jdir, g10b, mu10, ep10)
JsEb = lambda t: np.dot(Jdir * g10b(t), E10b(np.array([0, 1e-12, 0]), t))
avgb = tavg(JsEb, T10, tA)
Spb = tavg(lambda t: np.cross(E10b(np.array([0, 13.0, 0]), t), H10b(np.array([0, 13.0, 0]), t))[1], T10, tA)
print(f"  (f) two-frequency current: <-Js.E> = {-avgb:.4f} W/m^2 (37.5 pi = {37.5*np.pi:.4f} = 30 pi + 7.5 pi) ; each side {Spb:.4f} (18.75 pi = {18.75*np.pi:.4f})")
print(f"      <sin wt sin 3wt> = {tavg(lambda t: np.sin(w10*t)*np.sin(3*w10*t), T10):.2e}")
check("20.10(f) 37.5 pi and 18.75 pi", np.isclose(-avgb, 37.5 * np.pi) and np.isclose(Spb, 18.75 * np.pi))

# =========================================================================================== 20.11
hdr("20.11 Two sheets in step: x J0 cos wt on z = 0 and on z = d, free space, f = 100 MHz")
J011, f11 = 1.0, 100e6
w11 = 2 * np.pi * f11; b11 = w11 / cC; T11 = 1 / f11
print(f"  beta = {b11:.6f} rad/m (2 pi/3 = {2*np.pi/3:.6f}), lambda = {2*np.pi/b11:.4f} m")
gA = lambda t: J011 * np.cos(w11 * t)
print(f"  single sheet alone: injects eta0 J0^2/4 = {etaC/4:.4f} (30 pi), per side {etaC/8:.4f} (15 pi)")
for d in (0.75, 1.0, 1.5, 1e-7):
    EA, HA = sheetfields(X, gA, mu0, eps0C, np.zeros(3), Z)
    EB, HB = sheetfields(X, gA, mu0, eps0C, np.array([0, 0, d]), Z)
    Et = lambda r, t: EA(r, t) + EB(r, t)
    Ht = lambda r, t: HA(r, t) + HB(r, t)
    Sz = lambda z, t: np.cross(Et(np.array([0, 0, z]), t), Ht(np.array([0, 0, z]), t))[2]
    up = tavg(lambda t: Sz(d + 2.3, t), T11)
    dn = tavg(lambda t: Sz(-1.7, t), T11)
    mid = tavg(lambda t: Sz(d / 2, t), T11) if d > 1e-3 else float("nan")
    injA = tavg(lambda t: -np.dot(X * gA(t), Et(np.array([0, 0, 0.0]), t)), T11)
    injB = tavg(lambda t: -np.dot(X * gA(t), Et(np.array([0, 0, d]), t)), T11)
    formula = etaC * J011 ** 2 / 2 * np.cos(b11 * d / 2) ** 2
    print(f"  d = {d:g} m: <S_z> above {up:.4f}, below {dn:.4f}, between {mid:.2e}; <-JA.E> {injA:.4f}, <-JB.E> {injB:.4f}; 60 pi cos^2(beta d/2) = {formula:.4f}")
    check(f"20.11 d = {d:g}: outflow = injection = formula", np.isclose(up, formula, atol=1e-9) and np.isclose(-dn, formula, atol=1e-9)
          and np.isclose(injA, formula, atol=1e-9) and np.isclose(injB, formula, atol=1e-9) and np.isclose(up - dn, injA + injB, atol=1e-9))
    if d > 1e-3:
        check(f"20.11 d = {d:g}: <S> = 0 between the sheets", abs(mid) < 1e-9)
    # single-cosine form check above and below
    ok = True
    for (z, t) in ((d + 0.4, 0.31 * T11), (d + 1.9, 0.77 * T11)):
        ok &= np.isclose(Et(np.array([0, 0, z]), t)[0], -etaC * J011 * np.cos(b11 * d / 2) * np.cos(w11 * t - b11 * z + b11 * d / 2))
    for (z, t) in ((-0.4, 0.21 * T11), (-2.2, 0.66 * T11)):
        ok &= np.isclose(Et(np.array([0, 0, z]), t)[0], -etaC * J011 * np.cos(b11 * d / 2) * np.cos(w11 * t + b11 * z - b11 * d / 2))
    check(f"20.11 d = {d:g}: single-cosine forms", ok)
    if d == 1.5:
        print(f"    E on sheet A at several t: {[round(Et(np.zeros(3), t)[0], 9) for t in (0, 0.1*T11, 0.37*T11)]} (zero at every instant)")
    print(f"    amplitude outside = 120 pi |cos(beta d/2)| = {etaC*abs(np.cos(b11*d/2)):.3f} V/m ; cos^2 = {np.cos(b11*d/2)**2:.4f}")
print(f"  60 pi = {60*np.pi:.4f}, 30 pi = {30*np.pi:.4f}, 120 pi = {120*np.pi:.4f} (d -> 0 total = 4 x 30 pi)")

# =========================================================================================== 20.12
hdr("20.12 Charging a leaky capacitor: a = 5 cm, d = 2 mm, eps = 4 eps0, R = 10 MOhm, I = 10 uA")
a12, d12, er12, R12, I12 = 0.05, 2e-3, 4.0, 1e7, 1e-5
A12 = np.pi * a12 ** 2
e12 = er12 * eps0
C12 = e12 * A12 / d12
s12 = d12 / (R12 * A12)
tau12 = R12 * C12
print(f"  A = {A12:.6e} m^2 ; C = {C12*1e12:.3f} pF ; sigma = d/(R A) = {s12:.4e} S/m ; tau = RC = {tau12*1e3:.4f} ms (eps/sigma = {e12/s12*1e3:.4f} ms)")
sol = solve_ivp(lambda t, V: [(I12 - V[0] / R12) / C12], (0, 5 * tau12), [0.0], rtol=1e-11, atol=1e-12, dense_output=True)
Vt = lambda t: I12 * R12 * (1 - np.exp(-t / tau12))
print(f"  V(t) = I R (1 - e^-t/tau) = {I12*R12:.0f}(1 - e^-t/tau) V ; V(tau) = {Vt(tau12):.4f} V ; ODE: {sol.sol(tau12)[0]:.4f} V")
check("20.12 V(t) from KCL ODE", np.isclose(sol.sol(tau12)[0], Vt(tau12), rtol=1e-7) and np.isclose(sol.sol(3 * tau12)[0], Vt(3 * tau12), rtol=1e-7))
Eg = lambda t: Vt(t) / d12
print(f"  E(tau) = {Eg(tau12):.5e} V/m (E_inf = {I12*R12/d12:.0f} V/m)")
dEdt = lambda t: I12 * R12 / d12 / tau12 * np.exp(-t / tau12)
Jtot = lambda t: s12 * Eg(t) + e12 * dEdt(t)
print(f"  J + dD/dt at t = 0+, tau, 3 tau: {Jtot(1e-12):.6e}, {Jtot(tau12):.6e}, {Jtot(3*tau12):.6e} A/m^2 ; I/A = {I12/A12:.6e}")
check("20.12 J + dD/dt = I/A at all t", np.allclose([Jtot(1e-12), Jtot(tau12), Jtot(3 * tau12)], I12 / A12))
print(f"  conduction J(tau) = {s12*Eg(tau12):.4e}, displacement (tau) = {e12*dEdt(tau12):.4e} A/m^2 ; dE/dt(tau) = {dEdt(tau12):.4e} V/(m s)")


def E12(r, t):
    return Z * Eg(t)


def H12(r, t):
    x, y, _ = r
    return I12 / (2 * np.pi * a12 ** 2) * np.array([-y, x, 0.0])      # phi_hat I r/(2 pi a^2)


def J12(r, t):
    return Z * s12 * Eg(t)


Hline = quad(lambda ph: np.dot(H12(np.array([0.5 * a12 * np.cos(ph), 0.5 * a12 * np.sin(ph), 0]), tau12), np.array([-np.sin(ph), np.cos(ph), 0])) * 0.5 * a12, 0, 2 * np.pi)[0]
Ienc = quad(lambda r: Jtot(tau12) * 2 * np.pi * r, 0, 0.5 * a12)[0]
print(f"  Ampere-Maxwell at r = a/2: circulation of H = {Hline:.6e} A ; enclosed J + dD/dt = {Ienc:.6e} A")
check("20.12 H from Ampere-Maxwell", np.isclose(Hline, Ienc))
print(f"  H(a) = I/(2 pi a) = {I12/(2*np.pi*a12):.4e} A/m ; H(a/2) = {I12/(4*np.pi*a12):.4e} A/m")
maxwell("20.12 gap fields (mu0, eps, J = sigma E)", E12, H12, mu0, e12, [(np.array([0.01, -0.02, 0.001]), tau12), (np.array([-0.03, 0.01, 0.0015]), 2.2 * tau12)], 1e-5, 1e-7, J=J12)
pa12 = np.array([a12, 0, 0.001])
S12 = np.cross(E12(pa12, tau12), H12(pa12, tau12))
print(f"  S at r = a, t = tau: {S12} W/m^2 -> {dname(S12)} ; |S| = {np.linalg.norm(S12):.4f} W/m^2")
Pside = quad(lambda ph: -np.dot(np.cross(E12(0, tau12), H12(np.array([a12 * np.cos(ph), a12 * np.sin(ph), 0]), tau12)), np.array([np.cos(ph), np.sin(ph), 0])) * a12 * d12, 0, 2 * np.pi)[0]
print(f"  power in through the side r = a (surface integral) = {Pside*1e3:.5f} mW ; V(tau) I = {Vt(tau12)*I12*1e3:.5f} mW ; side area 2 pi a d = {2*np.pi*a12*d12:.4e} m^2")
check("20.12 inflow = V I", np.isclose(Pside, Vt(tau12) * I12))
ph12 = np.array([0.5 * a12 / np.sqrt(2), 0.5 * a12 / np.sqrt(2), 0.001])
dw12, dS12, JE12 = poynting_point("20.12 point form at r = a/2, t = tau", E12, H12, mu0, e12, ph12, tau12, 1e-6, 1e-9, J=J12)
print(f"  formulas: eps E dE/dt = {e12*Eg(tau12)*dEdt(tau12):.4f} ; -E I/(pi a^2) = {-Eg(tau12)*I12/A12:.4f} ; sigma E^2 = {s12*Eg(tau12)**2:.4f} W/m^3")
vol = A12 * d12
dWdt, heat12, inflow = e12 * Eg(tau12) * dEdt(tau12) * vol, s12 * Eg(tau12) ** 2 * vol, Vt(tau12) * I12
print(f"  gap volume {vol:.4e} m^3: dW/dt = {dWdt*1e6:.2f} uW ; int J.E dV = {heat12*1e6:.2f} uW (V^2/R = {Vt(tau12)**2/R12*1e6:.2f}) ; outward flux = {-inflow*1e6:.2f} uW")
print(f"  -dW/dt = {-dWdt*1e6:.2f} uW ; flux + heat = {(-inflow + heat12)*1e6:.2f} uW")
check("20.12 integral ledger", np.isclose(-dWdt, -inflow + heat12))
for t in (1e-12, tau12, 50 * tau12):
    fr = C12 * dEdt(t) * d12 / I12
    print(f"  fraction of inflow stored at t = {t/tau12:g} tau: {fr:.4f} (e^-t/tau = {np.exp(-t/tau12):.4f})")

# ---------------------------------------------------------------------------------------------
print("\n" + "=" * 78)
print(f"SUMMARY: {sum(ALL)}/{len(ALL)} checks OK")
print("=" * 78)
