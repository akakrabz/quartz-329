#!/usr/bin/env python3
"""R18 -- independent reviewer check of content-src/practice/18-wave-equation-and-plane-waves.md.

Every (E, H) pair is tested by finite differences against Faraday's law (curl E = -mu dH/dt),
the Ampere-Maxwell law (curl H = eps dE/dt) and div E = div H = 0, every H = u x E / eta and every
E x H direction with np.cross, and every moving pulse is re-propagated from the GIVEN data with my
own shift rule and, independently, with a 1-D Yee (FDTD) solver of the vector curl equations.
numpy/scipy only.
"""
import numpy as np
from scipy import integrate, optimize

mu0 = 4e-7*np.pi
eps0 = 8.8541878128e-12
c0 = 1/np.sqrt(mu0*eps0)          # 2.998e8 m/s
eta0 = np.sqrt(mu0/eps0)          # 376.73 ohm
X, Y, Z = np.eye(3)
rng = np.random.default_rng(1818)
NF = [0, 0]                       # [fails, checks]


def fmt(a):
    a = np.atleast_1d(a)
    return f"{a[0]:.5g}" if a.size == 1 else "[" + ", ".join(f"{x:.5g}" for x in a.ravel()) + "]"


def report(ok, msg):
    NF[1] += 1
    NF[0] += (not ok)
    print(f"  {'PASS' if ok else 'FAIL'}  {msg}")


def chk(name, got, page, rtol=4e-3, atol=1e-12):
    g = np.atleast_1d(np.asarray(got, float))
    p = np.atleast_1d(np.asarray(page, float))
    ok = g.shape == p.shape and np.allclose(g, p, rtol=rtol, atol=atol)
    report(ok, f"{name}: computed {fmt(g)}, page {fmt(p)}")


def unit(v):
    v = np.asarray(v, float)
    return v/np.linalg.norm(v)


# ---------------- finite-difference Maxwell checker (SI units) ----------------
def jac(F, r, t, h):
    J = np.empty((3, 3))
    for j in range(3):
        e = np.zeros(3)
        e[j] = h
        J[:, j] = (F(r + e, t) - F(r - e, t))/(2*h)
    return J


def curlJ(J):
    return np.array([J[2, 1] - J[1, 2], J[0, 2] - J[2, 0], J[1, 0] - J[0, 1]])


def ddt(F, r, t, k):
    return (F(r, t + k) - F(r, t - k))/(2*k)


def maxwell_res(E, H, mu, eps, pts, h, k):
    cE, mH, cH, eE, dE, dH, sE, sH = [], [], [], [], [], [], [], []
    for r, t in pts:
        JE, JH = jac(E, r, t, h), jac(H, r, t, h)
        cE.append(curlJ(JE)); cH.append(curlJ(JH))
        mH.append(-mu*ddt(H, r, t, k)); eE.append(eps*ddt(E, r, t, k))
        dE.append(np.trace(JE)); dH.append(np.trace(JH))
        sE.append(np.abs(JE).max()); sH.append(np.abs(JH).max())
    cE, mH, cH, eE = map(np.array, (cE, mH, cH, eE))
    rF = np.abs(cE - mH).max()/max(np.abs(cE).max(), np.abs(mH).max())
    rA = np.abs(cH - eE).max()/max(np.abs(cH).max(), np.abs(eE).max())
    return rF, rA, np.abs(dE).max()/max(sE), np.abs(dH).max()/max(max(sH), 1e-300)


def chk_pair(name, E, H, mu, eps, pts, h, k, expect=True, tol=2e-5):
    rF, rA, rdE, rdH = maxwell_res(E, H, mu, eps, pts, h, k)
    txt = f"rel. residuals: Faraday {rF:.1e}, Ampere-Maxwell {rA:.1e}, divE {rdE:.1e}, divH {rdH:.1e}"
    if expect:
        report(max(rF, rA, rdE, rdH) < tol, f"{name} satisfies Maxwell ({txt})")
    else:
        report(max(rF, rA) > 1e-2, f"{name} must VIOLATE Maxwell ({txt})")
    return rF, rA, rdE


def rpts(n, lo, hi, tlo, thi):
    lo, hi = np.asarray(lo, float), np.asarray(hi, float)
    return [(lo + (hi - lo)*rng.random(3), tlo + (thi - tlo)*rng.random()) for _ in range(n)]


# ---------------- 1-D Yee solver (units m, us; Ht = eta*H) ----------------
def fdtd(w, v, za, zb, dz, E0f, Ht0f, t0, t1, snaps=(), probes=()):
    """Fields depending on s = w.r only: curl F = w x dF/ds, so
    dE/dt = v w x dHt/ds and dHt/dt = -v w x dE/ds.  Courant number 1 (exact in 1-D)."""
    zE = np.arange(za, zb + dz/2, dz)
    zH = 0.5*(zE[1:] + zE[:-1])
    dt = np.sign(t1 - t0)*dz/v
    E = E0f(zE, t0)
    Ht = Ht0f(zH, t0 + dt/2)
    n = int(round((t1 - t0)/dt))
    S, P = {}, {p: ([], [], []) for p in probes}
    idx = {p: int(round((p - za)/dz)) for p in probes}
    for m in range(n + 1):
        t = t0 + m*dt
        for ts in snaps:
            if abs(t - ts) < abs(dt)/2:
                S[ts] = (zE.copy(), E.copy(), 0.5*np.vstack([Ht[:1], Ht[1:] + Ht[:-1], Ht[-1:]]))
        for p in probes:
            i = idx[p]
            P[p][0].append(t); P[p][1].append(E[i].copy()); P[p][2].append(0.5*(Ht[i - 1] + Ht[i]))
        if m == n:
            break
        E[1:-1] += v*dt/dz*np.cross(w, Ht[1:] - Ht[:-1])
        Ht += -v*dt/dz*np.cross(w, E[1:] - E[:-1])
    return S, {p: tuple(np.array(a) for a in P[p]) for p in probes}


def runs(xs, vals, tol=1e-6):
    """maximal runs of equal non-zero values: list of (x_first, x_last, value)."""
    out, i, n = [], 0, len(xs)
    while i < n:
        if abs(vals[i]) < tol:
            i += 1
            continue
        j = i
        while j + 1 < n and abs(vals[j + 1] - vals[i]) < max(tol, 1e-6*abs(vals[i])):
            j += 1
        if j > i:                       # ignore isolated edge samples
            out.append((xs[i], xs[j], vals[i]))
        i = j + 1
    return out


def chk_runs(name, got, page, pos_tol, rtol=4e-3):
    ok = len(got) == len(page)
    if ok:
        for (a, b, val), (pa, pb, pv) in zip(got, page):
            ok &= abs(a - pa) <= pos_tol and abs(b - pb) <= pos_tol and abs(val - pv) <= rtol*abs(pv)
    g = "; ".join(f"({a:.4g},{b:.4g}):{val:.4g}" for a, b, val in got)
    p = "; ".join(f"({a:.4g},{b:.4g}):{val:.4g}" for a, b, val in page)
    report(ok, f"{name}: computed {g} | page {p}")


def box(s, a, b):
    s = np.asarray(s, float)
    return ((s > a) & (s < b)).astype(float)


def sbox(s, a, b, w):               # smooth box for finite differences
    return 0.5*(np.tanh((s - a)/w) - np.tanh((s - b)/w))


# =====================================================================================
print("18.1 velocities read from arguments")


def vel(a, k):                      # phase a t + k.r is constant on planes moving with v = -a k/|k|^2
    k = np.asarray(k, float)
    return -a*k/np.dot(k, k)


vp, vq, vr = vel(2*np.pi*1e8, 0.8*np.pi*X), vel(-1.0, 0.004*Z), vel(1.0, 0.0125*Y)
chk("18.1 v_p [m/s]", vp, -2.5e8*X)
chk("18.1 v_q [m/s]", vq, 250*Z)
chk("18.1 v_r [m/s]", vr, -80*Y)
# brute force: follow a crest of p, the edge of q, the peak of r
xc = 0.0
for t in np.linspace(0, 1e-9, 41):
    xc = optimize.minimize_scalar(lambda x: -np.cos(2*np.pi*1e8*t + 0.8*np.pi*x),
                                  bounds=(xc - 0.05, xc + 0.05), method="bounded", options={"xatol": 1e-10}).x
chk("18.1 crest of p that is at x=0 at t=0, position at t=1 ns [m]", xc, -0.25)
zg = np.arange(-100, 700, 0.01)
edges = [zg[np.argmax(np.heaviside(0.004*zg - t, 1) > 0.5)] for t in (0, 1, 2)]
chk("18.1 step edge of q at t = 0, 1, 2 s [m]", edges, [0, 250, 500], atol=0.02)
yp = [optimize.minimize_scalar(lambda y: -np.exp(-(t + 0.0125*y)**2), bounds=(-500, 500), method="bounded").x
      for t in (0, 1)]
chk("18.1 peak of r at t = 0, 1 s [m]", yp, [0, -80], atol=1e-3)
opts = {"a": [2.5e8*X, 250*Z, -80*Y], "b": [-2.5e8*X, -250*Z, -80*Y], "c": [-2.5e8*X, 250*Z, -80*Y],
        "d": [-2.5e8*X, 0.004*Z, -0.0125*Y], "e": [-2.5e8*X, 250*Z, 80*Y]}
match = [k for k, o in opts.items() if all(np.allclose(oi, ci) for oi, ci in zip(o, (vp, vq, vr)))]
report(match == ["c"], f"18.1 only option (c) matches: {match}")
diffs = {k: [i for i, (oi, ci) in enumerate(zip(o, (vp, vq, vr))) if not np.allclose(oi, ci)] for k, o in opts.items()}
report(diffs == {"a": [0], "b": [1], "c": [], "d": [1, 2], "e": [2]},
       f"18.1 distractors differ in (p,q,r index) {diffs} = (a) p sign, (b) q sign, (d) q,r slowness, (e) r sign")
chk("18.1 eps_r for p in a non-magnetic medium", (c0/2.5e8)**2, 1.44)

# =====================================================================================
print("\n18.2 partner fields (page constants eta0 = 376.7, c = 3.00e8)")
ep, cp = 376.7, 3.00e8
Ha = np.cross(Z, 6*Y)/ep
chk("18.2(a) H amplitude vector [mA/m]", Ha*1e3, -15.9*X)
chk("18.2(a) E x H direction", unit(np.cross(6*Y, Ha)), Z)
chk("18.2(a) B [nT]", 6/cp*1e9, 20.0)
Hb = np.cross(-Y, 3*X)/ep
chk("18.2(b) H amplitude vector [mA/m]", Hb*1e3, 7.96*Z)
chk("18.2(b) E x H direction", unit(np.cross(3*X, Hb)), -Y)
chk("18.2(b) B [nT]", 3/cp*1e9, 10.0)
Ec = ep*np.cross(0.05*Z, X)
chk("18.2(c) E amplitude vector [V/m]", Ec, 18.8*Y)
chk("18.2(c) back: u x E/eta0 [mA/m]", np.cross(X, Ec)/ep*1e3, 50*Z)
chk("18.2(c) E x H direction", unit(np.cross(Ec, Z)), X)
chk("18.2(c) B = mu0 H and E/c [nT]", [mu0*0.05*1e9, np.linalg.norm(Ec)/cp*1e9], [62.8, 62.8])
w2, tau2 = 2*np.pi*1e8, 2e-9
P2 = rpts(40, [-2, -2, -2], [2, 2, 2], 0, 1e-8)
chk_pair("18.2(a) pair", lambda r, t: 6*np.cos(w2*(t - r[2]/c0))*Y,
         lambda r, t: -6/eta0*np.cos(w2*(t - r[2]/c0))*X, mu0, eps0, P2, 1e-4, 1e-13)
chk_pair("18.2(b) pair", lambda r, t: 3*np.exp(-((t + r[1]/c0)/tau2)**2)*X,
         lambda r, t: 3/eta0*np.exp(-((t + r[1]/c0)/tau2)**2)*Z, mu0, eps0,
         rpts(40, [-1, -1, -1], [1, 1, 1], -5e-9, 5e-9), 1e-4, 1e-13)
chk_pair("18.2(c) pair", lambda r, t: eta0*0.05*np.cos(w2*(t - r[0]/c0))*Y,
         lambda r, t: 0.05*np.cos(w2*(t - r[0]/c0))*Z, mu0, eps0, P2, 1e-4, 1e-13)

# =====================================================================================
print("\n18.3 phase rate and snapshot period")
w3, b3 = 6*np.pi/10e-9, 2*np.pi/0.4
v3 = w3/b3
er3, eta3 = (c0/v3)**2, mu0*v3
E3 = lambda x, t: 12*np.cos(w3*t - b3*x)
tt = np.linspace(0, 10e-9, 200001)[:-1]
sig = np.sign(E3(0.13, tt))
report(np.count_nonzero(np.diff(sig) != 0) == 6, "18.3 probe sees 3 full cycles (6 zero crossings) in 10 ns -> phase grows 6 pi")
xx = np.linspace(0, 2, 2001)
report(np.allclose(E3(xx + 0.4, 1.7e-9), E3(xx, 1.7e-9)) and np.allclose(E3(xx + 0.2, 1.7e-9), -E3(xx, 1.7e-9)),
       "18.3 snapshot repeats every 0.4 m (and 0.2 m gives -E, so 0.4 m is the fundamental period)")
chk("18.3 omega [rad/s]", w3, 6*np.pi*1e8)
chk("18.3 beta [rad/m]", [b3, b3], [5*np.pi, 15.7])
chk("18.3 v [m/s]", v3, 1.2e8)
chk("18.3 temporal period [ns]", 2*np.pi/w3*1e9, 3.33)
chk("18.3 eps_r with c = 2.998e8 and with 3e8", [er3, (3e8/v3)**2], [6.24, 6.25])
chk("18.3 eta [ohm]", [eta3, eta3], [48*np.pi, 150.8])
H3 = np.cross(X, 12*Y)/eta3
chk("18.3 H amplitude vector [mA/m]", H3*1e3, 79.6*Z)
chk("18.3 E x H direction", unit(np.cross(Y, H3)), X)
chk("18.3 B = E/v = mu0 H [nT]", [12/v3*1e9, mu0*np.linalg.norm(H3)*1e9], [100, 100])
chk("18.3 H / (12/eta0) = sqrt(eps_r)", np.linalg.norm(H3)/(12/eta0), 2.5)
chk_pair("18.3 pair", lambda r, t: 12*np.cos(w3*t - b3*r[0])*Y, lambda r, t: 12/eta3*np.cos(w3*t - b3*r[0])*Z,
         mu0, er3*eps0, rpts(40, [-1, -1, -1], [1, 1, 1], 0, 1e-8), 1e-5, 1e-14)

# =====================================================================================
print("\n18.4 what the derivation needs")
va, wa = 1e8, 2e8
Ea = lambda r, t: np.cos(wa*(t - r[2]/va))*X


def lap(F, r, t, h):
    return sum((F(r + h*e, t) - 2*F(r, t) + F(r - h*e, t))/h**2 for e in (X, Y, Z))


r0, t0 = np.array([0.1, 0.2, 0.37]), 3.1e-9
chk("18.4(a) lap E_x / E_x = -(omega/v)^2", lap(Ea, r0, t0, 1e-4)[0]/Ea(r0, t0)[0], -(wa/va)**2, rtol=1e-5)
rho0, a4, e4 = 1e-6, 2.0, 4*eps0
Eb = lambda r, t: rho0*r[0]**2/(2*e4*a4)*X
rb = np.array([0.7, -0.3, 0.2])
chk("18.4(b) div E = rho/eps", np.trace(jac(Eb, rb, 0, 1e-4)), rho0*rb[0]/a4/e4, rtol=1e-6)
chk("18.4(b) curl E = 0 (static field is consistent)", np.linalg.norm(curlJ(jac(Eb, rb, 0, 1e-4))), 0, atol=1e-6)
chk("18.4(b) lap E = rho0/(eps a) x (nonzero), = grad(rho)/eps", lap(Eb, rb, 0, 1e-3), rho0/(e4*a4)*X, rtol=1e-6)
a4c, E0c = 0.5, 10.0
eps_c = lambda r: eps0*(1 + r[0]/a4c)
Ec4 = lambda r, t: E0c/(1 + r[0]/a4c)*X
Dc4 = lambda r, t: eps_c(r)*Ec4(r, t)
rc = np.array([0.31, 0.1, -0.2])
chk("18.4(c) div D = 0", np.trace(jac(Dc4, rc, 0, 1e-5))/eps0, 0, atol=1e-6)
chk("18.4(c) div E at x=0 = -E0/a", np.trace(jac(Ec4, np.zeros(3), 0, 1e-6)), -E0c/a4c, rtol=1e-6)
chk("18.4(c) div E = -E.grad(eps)/eps at x = 0.31", np.trace(jac(Ec4, rc, 0, 1e-6)),
    -Ec4(rc, 0)[0]*(eps0/a4c)/eps_c(rc), rtol=1e-6)
Ed = lambda r, t: 5*np.cos(wa*(t - r[2]/va))*Z
d2z = (Ed(r0 + 1e-4*Z, t0) - 2*Ed(r0, t0) + Ed(r0 - 1e-4*Z, t0))[2]/1e-8
d2t = (Ed(r0, t0 + 1e-13) - 2*Ed(r0, t0) + Ed(r0, t0 - 1e-13))[2]/1e-26
chk("18.4(d) d2E/dz2 = (1/v^2) d2E/dt2", d2z, d2t/va**2, rtol=1e-5)
chk("18.4(d) div E = (omega E0/v) sin(...)", np.trace(jac(Ed, r0, t0, 1e-5)),
    wa*5/va*np.sin(wa*(t0 - r0[2]/va)), rtol=1e-6)
chk("18.4(d) curl E = 0", np.linalg.norm(curlJ(jac(Ed, r0, t0, 1e-5))), 0, atol=1e-6)

# =====================================================================================
print("\n18.5 find the error")
w5, b5 = 1.5*np.pi*1e8, 2*np.pi
v5 = w5/b5
chk("18.5 v [m/s]", v5, 7.5e7)
chk("18.5 eps_r (c0) and (3e8)", [(c0/v5)**2, (3e8/v5)**2], [15.98, 16])
chk("18.5 eta = mu0 v = 30 pi and eta0/4 [ohm]", [mu0*v5, 30*np.pi, eta0/4], [94.2, 94.2, 94.2])
eta5 = mu0*v5
Hc5 = np.cross(-X, 12*Z)/eta5
Hs5 = np.cross(12*Z, -X)/eta5
chk("18.5 correct H = u x E/eta [A/m]", Hc5, 0.127*Y)
chk("18.5 student's E x u / eta [A/m] (their arithmetic is right for their formula)", Hs5, -0.127*Y)
chk("18.5 E x H(correct) direction", unit(np.cross(Z, Hc5)), -X)
chk("18.5 E x H(student) direction", unit(np.cross(Z, Hs5)), X)
E5 = lambda r, t: 12*np.cos(w5*t + b5*r[0])*Z
P5 = rpts(40, [-1, -1, -1], [1, 1, 1], 0, 2e-8)
chk_pair("18.5 corrected pair", E5, lambda r, t: 12/eta5*np.cos(w5*t + b5*r[0])*Y, mu0, 1/(mu0*v5**2), P5, 1e-5, 1e-14)
chk_pair("18.5 student's pair", E5, lambda r, t: -12/eta5*np.cos(w5*t + b5*r[0])*Y, mu0, 1/(mu0*v5**2), P5, 1e-5,
         1e-14, expect=False)
lhs = [jac(E5, r, t, 1e-6)[2, 0] for r, t in P5[:5]]
rhs = [mu0*ddt(lambda rr, tt: 12/eta5*np.cos(w5*tt + b5*rr[0])*Y, r, t, 1e-14)[1] for r, t in P5[:5]]
chk("18.5 dEz/dx = mu0 dHy/dt (page's scalar form) at 5 points", lhs, rhs, rtol=1e-5, atol=1e-6)

# =====================================================================================
print("\n18.6 which fields can be waves")
me = 1e-16
v6, eps6 = 1/np.sqrt(me), me/mu0
eta6 = mu0*v6
chk("18.6 v, eps_r, eta", [v6, eps6/eps0, eta6], [1e8, 9, 40*np.pi], rtol=2e-3)
om, be = 2e8, 2.0
cands = {1: lambda z, t: 4*np.cos(om*t - be*z), 2: lambda z, t: 4*np.cos(om*t)*np.cos(be*z),
         3: lambda z, t: 4*np.cos(om*t - 6*z), 4: lambda z, t: 4*np.cos(om*t - be*z)*np.cos(om*t + be*z)}
zt = [(rng.uniform(-3, 3), rng.uniform(0, 5e-8)) for _ in range(60)]
d2 = lambda f, z, t: ((f(z + 1e-3, t) - 2*f(z, t) + f(z - 1e-3, t))/1e-6,
                      (f(z, t + 1e-12) - 2*f(z, t) + f(z, t - 1e-12))/1e-24)
okw = {}
for i, f in cands.items():
    a = np.array([d2(f, z, t) for z, t in zt])
    okw[i] = bool(np.abs(a[:, 0] - me*a[:, 1]).max()/np.abs(np.r_[a[:, 0], me*a[:, 1]]).max() < 1e-5)
report(okw == {1: True, 2: True, 3: False, 4: False}, f"18.6(a) satisfies the wave equation: {okw}")
chk("18.6(a) E1 speed, E3 speed [m/s]", [om/be, om/6], [1e8, 3.33e7])
chk("18.6(a) eps_r that E3 would need", (6/om)**2/mu0/eps0, 81, rtol=3e-3)
chk("18.6(a) E4 = 2cos4z + 2cos(4e8 t) at 60 points", [cands[4](z, t) for z, t in zt],
    [2*np.cos(4*z) + 2*np.cos(4e8*t) for z, t in zt], rtol=1e-9, atol=1e-9)
tq = np.pi/4e8
d2z4, d2t4 = d2(cands[4], 0.0, tq)
chk("18.6(a) E4 at z=0, t=7.85 ns: d2E/dz2 and me d2E/dt2 [V/m^3]", [tq*1e9, d2z4, me*d2t4], [7.85, -32, 32])
Hy6 = lambda z, t: 4/eta6*np.sin(om*t)*np.sin(be*z)
dEdz = lambda z, t: (cands[2](z + 1e-6, t) - cands[2](z - 1e-6, t))/2e-6
Hint = [integrate.quad(lambda s: -dEdz(z, s)/mu0, 0, t, epsabs=1e-12)[0] for z, t in zt[:6]]
chk("18.6(b) H_y by time-integrating Faraday vs (4/eta) sin wt sin bz", Hint, [Hy6(z, t) for z, t in zt[:6]],
    rtol=1e-6, atol=1e-9)
chk("18.6(b) amplitude 4/eta [mA/m]", 4/eta6*1e3, 31.8)
chk_pair("18.6(b) E2, H pair", lambda r, t: cands[2](r[2], t)*X, lambda r, t: Hy6(r[2], t)*Y, mu0, eps6,
         rpts(40, [-1, -1, -3], [1, 1, 3], 0, 5e-8), 1e-5, 1e-14)
chk("18.6(c) E2 = 2cos(wt-bz) + 2cos(wt+bz)", [cands[2](z, t) for z, t in zt[:10]],
    [2*np.cos(om*t - be*z) + 2*np.cos(om*t + be*z) for z, t in zt[:10]], rtol=1e-9, atol=1e-9)
chk("18.6(c) (Af - Bg)/eta = H_y", [(2*np.cos(om*t - be*z) - 2*np.cos(om*t + be*z))/eta6 for z, t in zt[:10]],
    [Hy6(z, t) for z, t in zt[:10]], rtol=1e-9, atol=1e-12)
zz = np.linspace(0, 4, 4001)
td = np.pi/(2*om)
chk("18.6(d) t when E2 = 0 everywhere [ns]; max|E2| then", [td*1e9, np.abs(cands[2](zz, td)).max()], [7.85, 0],
    atol=1e-9)
zmax = optimize.minimize_scalar(lambda z: -Hy6(z, td), bounds=(0, 1.5), method="bounded").x
chk("18.6(d) H then: peak [mA/m] and first z of the peak [m]", [Hy6(zmax, td)*1e3, zmax], [31.8, 0.785])
chk("18.6(d) quarter period later max|H|", np.abs(Hy6(zz, td + np.pi/(2*om))).max(), 0, atol=1e-12)
z1, t1 = 0.3, 2.2e-9
chk("18.6 check: E/H = eta cot wt cot bz", cands[2](z1, t1)/Hy6(z1, t1), eta6/np.tan(om*t1)/np.tan(be*z1), rtol=1e-9)

# =====================================================================================
print("\n18.7 strip line and matching coax")
W, d, Lline, T = 8e-3, 1e-3, 3.0, 18e-9
v7 = Lline/T
er7 = (3e8/v7)**2
eps7 = er7*eps0
chk("18.7(a) v, eps_r", [v7, er7], [1.67e8, 3.24])
chk("18.7(a) eta: 120pi/sqrt(er), mu0 v, sqrt(mu0/eps)", [120*np.pi/np.sqrt(er7), mu0*v7, np.sqrt(mu0/eps7)],
    [209, 209, 209], rtol=3e-3)
C7, L7 = eps7*W/d, mu0*d/W
chk("18.7(b) C [pF/m], L [nH/m]", [C7*1e12, L7*1e9], [229.5, 157.1], rtol=1e-3)
chk("18.7(b) 1/sqrt(LC) [m/s]", 1/np.sqrt(L7*C7), 1.67e8)
Z7 = np.sqrt(L7/C7)
chk("18.7(c) sqrt(L/C) direct and eta d/W [ohm]", [Z7, np.sqrt(mu0/eps7)*d/W, mu0*v7*d/W], [26.2, 26.2, 26.2])


def C_coax(q):                      # per metre, from V = int E dr with rho_l = 1
    return 1/integrate.quad(lambda r: 1/(2*np.pi*eps7*r), 1.0, q)[0]


def L_coax(q):                      # flux per metre per ampere
    return integrate.quad(lambda r: mu0/(2*np.pi*r), 1.0, q)[0]


q7 = optimize.brentq(lambda q: np.sqrt(L_coax(q)/C_coax(q)) - Z7, 1.01, 50)
chk("18.7(d) b/a and ln(b/a)", [q7, np.log(q7), np.exp(np.pi/4)], [2.19, 0.785, 2.19])
chk("18.7(d) coax L [nH/m], C [pF/m]", [L_coax(q7)*1e9, C_coax(q7)*1e12], [157.1, 229.5], rtol=1e-3)
chk("18.7(d) coax delay over 3 m [ns]", Lline*np.sqrt(L_coax(q7)*C_coax(q7))*1e9, 18, rtol=2e-3)

# =====================================================================================
print("\n18.8 probe record -> snapshots (+x travel, E along z; c = 300 m/us, eta0 = 120 pi)")
c8, e8 = 300.0, 120*np.pi
F8 = lambda s: 5*box(s, 0, 1) - 2*box(s, 1, 3)
E8 = lambda x, t: F8(t - x/c8)                # +x travel: feature at x0 at t0 is at x0 + c(t - t0)
xs = np.arange(-1500, 2000.001, 0.5)
chk_runs("18.8(b) snapshot at t=2 us [x m]", runs(xs, E8(xs, 2.0)), [(-300, 300, -2), (300, 600, 5)], 1.0)
ts = np.arange(0, 8, 0.001)
chk_runs("18.8(c) record at x=900 m [t us]", runs(ts, E8(900, ts)), [(3, 4, 5), (4, 6, -2)], 0.002)
for xq, Ez, Hp, Bp in ((450, 5, -13.3, 16.7), (0, -2, 5.31, 6.67)):
    Eq = E8(xq, 2.0)*Z
    Hq = np.cross(X, Eq)/e8
    chk(f"18.8(d) at x={xq} m: E_z [V/m], H [mA/m], B [nT]", [Eq[2], *(Hq*1e3), np.linalg.norm(Eq)/3e8*1e9],
        [Ez, 0, Hp, 0, Bp])
    chk(f"18.8(d) at x={xq} m: E x H direction", unit(np.cross(Eq, Hq)), X)
S8, P8 = fdtd(X, c8, -2500, 2500, 0.5, lambda z, t: E8(z, t)[:, None]*Z, lambda z, t: np.cross(X, E8(z, t)[:, None]*Z),
              -1.0, 6.5, snaps=(2.0,), probes=(0.0, 900.0))
tP, EP, _ = P8[0.0]
chk_runs("18.8 FDTD: record at x=0 reproduces the GIVEN record", runs(tP, EP[:, 2]), [(0, 1, 5), (1, 3, -2)], 0.01)
tP, EP, _ = P8[900.0]
chk_runs("18.8 FDTD: record at x=900 m", runs(tP, EP[:, 2]), [(3, 4, 5), (4, 6, -2)], 0.01)
zE, ES, HS = S8[2.0]
chk_runs("18.8 FDTD: snapshot at 2 us", runs(zE, ES[:, 2]), [(-300, 300, -2), (300, 600, 5)], 1.5)
i450, i0 = np.argmin(abs(zE - 450)), np.argmin(abs(zE - 0))
chk("18.8 FDTD: H_y at (450 m, 2 us) and (0, 2 us) [mA/m]", [HS[i450, 1]/e8*1e3, HS[i0, 1]/e8*1e3], [-13.3, 5.31])
ws8 = 0.05
F8s = lambda s: 5*sbox(s, 0, 1, ws8) - 2*sbox(s, 1, 3, ws8)
chk_pair("18.8 pair (smoothed edges)", lambda r, t: F8s(t*1e6 - r[0]/c8)*Z, lambda r, t: -F8s(t*1e6 - r[0]/c8)/e8*Y,
         mu0, 1/(e8*3e8), rpts(200, [-400, -1, -1], [1000, 1, 1], 0, 4e-6), 1e-3, 1e-12)

# =====================================================================================
print("\n18.9 triangle pulse toward -z at 150 m/us")
v9, eta9 = 150.0, 2*mu0*1.5e8


def g9(z):
    z = np.asarray(z, float)
    return np.where((z >= 300) & (z <= 450), 0.04*(z - 300), np.where((z > 450) & (z <= 900), (900 - z)/75, 0.0))


def Ea9(z):                          # page (a)
    z = np.asarray(z, float)
    return np.where((z >= 600) & (z <= 750), 0.04*(z - 600), np.where((z > 750) & (z <= 1200), (1200 - z)/75, 0.0))


def F9(s):                           # page (b)
    s = np.asarray(s, float)
    return np.where((s >= 4) & (s <= 5), 6*(s - 4), np.where((s > 5) & (s <= 8), 2*(8 - s), 0.0))


E9 = lambda z, t: g9(z + v9*(t - 2))           # -z travel: feature at z0 at 2 us is at z0 - v(t - 2)
zs = np.arange(-3000, 3000.001, 0.25)
chk("18.9 given profile: peak 6 V/m at 450 m, support 300..900 m",
    [g9(zs).max(), zs[np.argmax(g9(zs))], zs[g9(zs) > 0].min(), zs[g9(zs) > 0].max()], [6, 450, 300, 900], atol=0.3)
chk("18.9(a) max|my E(z,0) - page (a)|", np.abs(E9(zs, 0) - Ea9(zs)).max(), 0, atol=1e-12)
chk("18.9(a) peak position at t=0 [m]", zs[np.argmax(E9(zs, 0))], 750)
devb = max(np.abs(E9(zs, t) - F9(t + zs/v9)).max() for t in (0, 2, 5.3, 11.5))
chk("18.9(b) max|my E(z,t) - page F(t + z/v)| at t = 0, 2, 5.3, 11.5", devb, 0, atol=1e-9)
chk("18.9 setup: peak at t = 0, 2, 4, 11.5 [m] = 750 - 150 t",
    [zs[np.argmax(E9(zs, t))] for t in (0, 2, 4, 11.5)], [750 - 150*t for t in (0, 2, 4, 11.5)])
tr = np.arange(0, 16, 0.0005)
rec = E9(-750, tr)
nz = tr[rec > 1e-9]
chk("18.9(c) record at z=-750: start, peak time, end [us], peak [V/m]", [nz.min(), tr[np.argmax(rec)], nz.max(), rec.max()],
    [9, 10, 13, 6], atol=1e-3)
chk("18.9(c) readings at 9.5 and 11.5 us [V/m]", [E9(-750, 9.5), E9(-750, 11.5)], [3, 3])
chk("18.9(c) snapshot at 11.5 us is g(z + 1425): value at -750", g9(-750 + 1425), 3)
rise_rec, fall_rec = tr[np.argmax(rec)] - nz.min(), nz.max() - tr[np.argmax(rec)]
zz2 = zs[g9(zs) > 0]
rise_sn, fall_sn = (450 - zz2.min())/v9, (zz2.max() - 450)/v9
report(rise_rec < fall_rec and rise_sn < fall_sn,
       f"18.9(c) NOT mirrored: record rise {rise_rec:.3g} us then fall {fall_rec:.3g} us; snapshot (low->high z) "
       f"rise {rise_sn:.3g} us-equivalent then fall {fall_sn:.3g}")
prod = (c0/1.5e8)**2
eta_m = 6/15.9e-3
ratio = (eta_m/eta0)**2
chk("18.9(d) mu_r eps_r, eta measured [ohm], mu_r/eps_r", [prod, eta_m, ratio], [3.99, 377, 1.0], rtol=5e-3)
chk("18.9(d) mu_r, eps_r", [np.sqrt(prod*ratio), np.sqrt(prod/ratio)], [2, 2], rtol=3e-3)
chk("18.9(d) speed with mu_r = eps_r = 2 is c/2 [m/s]", c0/2, 1.5e8, rtol=1e-3)
H9dir = np.cross(-Z, X)
chk("18.9(e) H direction = (-z) x x", H9dir, -Y)
chk("18.9(e) E x H direction", np.cross(X, H9dir), -Z)
chk("18.9(e) eta = mu v [ohm], peak H [mA/m], peak B = mu H and E/v [nT]",
    [eta9, 120*np.pi, 6/eta9*1e3, 2*mu0*6/eta9*1e9, 6/1.5e8*1e9], [377, 377, 15.9, 40, 40])
chk("18.9(e) H at the probe at 11.5 us [mA/m]", -E9(-750, 11.5)/eta9*1e3, -7.96)
S9b, _ = fdtd(Z, v9, -3000, 2500, 0.5, lambda z, t: E9(z, t)[:, None]*X, lambda z, t: np.cross(-Z, E9(z, t)[:, None]*X),
              2.0, 0.0, snaps=(0.0,))
zE, ES, _ = S9b[0.0]
chk("18.9 FDTD (backward from the GIVEN data at 2 us): max|E(z,0) - page (a)|", np.abs(ES[:, 0] - Ea9(zE)).max(), 0,
    atol=1e-6)
S9f, P9 = fdtd(Z, v9, -3000, 2500, 0.5, lambda z, t: E9(z, t)[:, None]*X, lambda z, t: np.cross(-Z, E9(z, t)[:, None]*X),
               2.0, 14.0, snaps=(11.5,), probes=(-750.0,))
tP, EP, HP = P9[-750.0]
chk("18.9 FDTD: probe at -750 m reads E_x at 9.5, 10, 11.5, 13 us [V/m]",
    [np.interp(t, tP, EP[:, 0]) for t in (9.5, 10, 11.5, 13)], [3, 6, 3, 0], atol=1e-6)
chk("18.9 FDTD: H_y at the probe at 11.5 us [mA/m]", np.interp(11.5, tP, HP[:, 1])/eta9*1e3, -7.96)
zE, ES, _ = S9f[11.5]
chk("18.9 FDTD: snapshot at 11.5 us vs g(z + 1425)", np.abs(ES[:, 0] - g9(zE + 1425)).max(), 0, atol=1e-6)
P9fd = [p for p in rpts(400, [-1, -1, -1500], [1, 1, 1500], 0, 14e-6)
        if min(abs(p[1]*1e6 + p[0][2]/v9 - k) for k in (4, 5, 8)) > 1e-3]
eps9 = 1/(eta9*1.5e8)
print(f"  (medium used for the FD check: mu = 2 mu0, eps = {eps9/eps0:.4f} eps0, i.e. exactly v = 1.5e8, eta = 120 pi)")
chk_pair("18.9 pair E = F x, H = -F/eta y", lambda r, t: F9(t*1e6 + r[2]/v9)*X, lambda r, t: -F9(t*1e6 + r[2]/v9)/eta9*Y,
         2*mu0, eps9, P9fd, 1e-2, 1e-11)
chk_pair("18.9 wrong-sign pair H = +F/eta y", lambda r, t: F9(t*1e6 + r[2]/v9)*X,
         lambda r, t: F9(t*1e6 + r[2]/v9)/eta9*Y, 2*mu0, eps9, P9fd, 1e-2, 1e-11, expect=False)

# =====================================================================================
print("\n18.10 two pulses passing through each other (c = 300 m/us, eta0 = 120 pi)")
c10, e10 = 300.0, 120*np.pi
EA = lambda z, t: 6*box(z - c10*t, -600, -300)        # my own: rigid shift of the t=0 data
EB = lambda z, t: 3*box(z + c10*t, 300, 900)
EBp = lambda z, t: -6*box(z + c10*t, 300, 600)
f10 = lambda s: 6*box(s, 1, 2)                         # page (a)
g10 = lambda s: 3*box(s, 1, 3)
zg = np.arange(-1500, 1500.001, 0.5)
devA = max(np.abs(EA(zg, t) - f10(t - zg/c10)).max() for t in (0, 0.7, 1.5, 4))
devB = max(np.abs(EB(zg, t) - g10(t + zg/c10)).max() for t in (0, 0.7, 1.5, 4))
report(devA == 0 and devB == 0, "18.10(a) page f(t - z/c) on 1<s<2 and g(t + z/c) on 1<s<3 equal the shifted t=0 data")
HAy = np.cross(Z, X)[1]/e10
HBy = np.cross(-Z, X)[1]/e10
chk("18.10(a) H_y per V/m of A and of B (x eta0)", [HAy*e10, HBy*e10], [1, -1])
chk("18.10(a) H_y on A, on B [mA/m]", [6*HAy*1e3, 3*HBy*1e3], [15.9, -7.96])
Etot = lambda z, t: EA(z, t) + EB(z, t)
Htot = lambda z, t: EA(z, t)*HAy + EB(z, t)*HBy
chk_runs("18.10(b) E_x at 1.5 us [V/m]", runs(zg, Etot(zg, 1.5)), [(-150, 150, 9), (150, 450, 3)], 1.0)
chk_runs("18.10(b) H_y at 1.5 us [mA/m]", runs(zg, Htot(zg, 1.5)*1e3), [(-150, 150, 7.96), (150, 450, -7.96)], 1.0)
chk("18.10(b) E/H in overlap and in B alone [ohm]", [Etot(0, 1.5)/Htot(0, 1.5), Etot(300, 1.5)/Htot(300, 1.5)],
    [1131, -377])
tt10 = np.arange(0, 5, 0.001)
chk_runs("18.10(c) probe E_x at z=0 [t us]", runs(tt10, Etot(0, tt10)), [(1, 2, 9), (2, 3, 3)], 0.002)
chk_runs("18.10(c) probe H_y at z=0 [mA/m]", runs(tt10, Htot(0, tt10)*1e3), [(1, 2, 7.96), (2, 3, -7.96)], 0.002)
chk_runs("18.10(d) E_x at 4 us", runs(zg, Etot(zg, 4.0)), [(-900, -300, 3), (600, 900, 6)], 1.0)
chk_runs("18.10(d) H_y at 4 us [mA/m]", runs(zg, Htot(zg, 4.0)*1e3), [(-900, -300, -7.96), (600, 900, 15.9)], 1.0)
HBpy = np.cross(-Z, -6*X)[1]/e10
chk("18.10(e) H_y of B' [mA/m]", HBpy*1e3, 15.9)
Etp = lambda z, t: EA(z, t) + EBp(z, t)
Htp = lambda z, t: EA(z, t)*HAy + EBp(z, t)*HBy
chk("18.10(e) max|E| at 1.5 us", np.abs(Etp(zg, 1.5)).max(), 0, atol=1e-12)
chk_runs("18.10(e) H_y at 1.5 us [mA/m]", runs(zg, Htp(zg, 1.5)*1e3), [(-150, 150, 31.8)], 1.0)
chk_runs("18.10(e) E_x at 2.5 us", runs(zg, Etp(zg, 2.5)), [(-450, -150, -6), (150, 450, 6)], 1.0)
chk_runs("18.10(e) H_y at 2.5 us [mA/m]", runs(zg, Htp(zg, 2.5)*1e3), [(-450, -150, 15.9), (150, 450, 15.9)], 1.0)
E0A = lambda z, t: EA(z, t)[:, None]*X
E0B = lambda z, t: EB(z, t)[:, None]*X
E0Bp = lambda z, t: EBp(z, t)[:, None]*X
S10, P10 = fdtd(Z, c10, -2500, 2500, 0.5, lambda z, t: E0A(z, t) + E0B(z, t),
                lambda z, t: np.cross(Z, E0A(z, t)) + np.cross(-Z, E0B(z, t)), 0.0, 4.0, snaps=(1.5, 4.0), probes=(0.0,))
zE, ES, HS = S10[1.5]
chk_runs("18.10 FDTD: E_x at 1.5 us", runs(zE, ES[:, 0]), [(-150, 150, 9), (150, 450, 3)], 1.5)
chk_runs("18.10 FDTD: H_y at 1.5 us [mA/m]", runs(zE, HS[:, 1]/e10*1e3), [(-150, 150, 7.96), (150, 450, -7.96)], 1.5)
zE, ES, HS = S10[4.0]
chk_runs("18.10 FDTD: E_x at 4 us", runs(zE, ES[:, 0]), [(-900, -300, 3), (600, 900, 6)], 1.5)
tP, EP, HP = P10[0.0]
chk_runs("18.10 FDTD: probe E_x at z=0", runs(tP, EP[:, 0]), [(1, 2, 9), (2, 3, 3)], 0.01)
S10p, _ = fdtd(Z, c10, -2500, 2500, 0.5, lambda z, t: E0A(z, t) + E0Bp(z, t),
               lambda z, t: np.cross(Z, E0A(z, t)) + np.cross(-Z, E0Bp(z, t)), 0.0, 2.5, snaps=(1.5, 2.5))
zE, ES, HS = S10p[1.5]
chk("18.10 FDTD (e): max|E| at 1.5 us; H_y at z=0 [mA/m]", [np.abs(ES).max(), HS[np.argmin(abs(zE)), 1]/e10*1e3],
    [0, 31.8], atol=1e-9)
zE, ES, HS = S10p[2.5]
chk_runs("18.10 FDTD (e): E_x at 2.5 us", runs(zE, ES[:, 0]), [(-450, -150, -6), (150, 450, 6)], 1.5)
ws = 0.05
fs = lambda s: 6*sbox(s, 1, 2, ws)
gs = lambda s: 3*sbox(s, 1, 3, ws)
P10fd = rpts(400, [-1, -1, -700], [1, 1, 1000], 0, 4e-6)
E10 = lambda r, t: (fs(t*1e6 - r[2]/c10) + gs(t*1e6 + r[2]/c10))*X
chk_pair("18.10 total pair, H = (f - g)/eta0", E10, lambda r, t: (fs(t*1e6 - r[2]/c10) - gs(t*1e6 + r[2]/c10))/e10*Y,
         mu0, 1/(e10*3e8), P10fd, 1e-3, 1e-12)
rF, rA, _ = chk_pair("18.10 total pair with H = (f + g)/eta0", E10,
                     lambda r, t: (fs(t*1e6 - r[2]/c10) + gs(t*1e6 + r[2]/c10))/e10*Y, mu0, 1/(e10*3e8), P10fd,
                     1e-3, 1e-12, expect=False)
report(rF > 0.1 and rA > 0.1, f"18.10 check: with (f + g) BOTH Faraday ({rF:.2f}) and Ampere-Maxwell ({rA:.2f}) fail")

# =====================================================================================
print("\n18.11 the derivation along x")
mu11, eps11 = 1.5*mu0, 3*eps0
v11, eta11 = 1/np.sqrt(mu11*eps11), np.sqrt(mu11/eps11)
fA = lambda s: np.exp(-((s - 2e-9)/1e-9)**2)
gB = lambda s: np.cos(3e9*s)*np.exp(-(s/2e-9)**2)
A11, B11 = 1.7, -0.6
E11 = lambda r, t: (A11*fA(t - r[0]/v11) + B11*gB(t + r[0]/v11))*Z
H11 = lambda r, t: (-A11*fA(t - r[0]/v11) + B11*gB(t + r[0]/v11))/eta11*Y
P11 = rpts(60, [-0.6, -1, -1], [0.6, 1, 1], -4e-9, 6e-9)
chk_pair("18.11(c) general pair, H_y = (Bg - Af)/eta", E11, H11, mu11, eps11, P11, 1e-5, 1e-14)
chk_pair("18.11(c) z-case sign transplanted, H_y = (Af - Bg)/eta", E11,
         lambda r, t: -H11(r, t), mu11, eps11, P11, 1e-5, 1e-14, expect=False)
s1 = [jac(E11, r, t, 1e-6)[2, 0] - mu11*ddt(H11, r, t, 1e-15)[1] for r, t in P11[:8]]
s2 = [jac(H11, r, t, 1e-6)[1, 0] - eps11*ddt(E11, r, t, 1e-15)[2] for r, t in P11[:8]]
sc1 = max(abs(jac(E11, r, t, 1e-6)[2, 0]) for r, t in P11[:8])
sc2 = max(abs(jac(H11, r, t, 1e-6)[1, 0]) for r, t in P11[:8])
chk("18.11(a) dEz/dx - mu dHy/dt and dHy/dx - eps dEz/dt (relative)", [max(map(abs, s1))/sc1, max(map(abs, s2))/sc2],
    [0, 0], atol=1e-5)
chk("18.11(a) curl of Ez(x) z = -dEz/dx y; curl of Hy(x) y = +dHy/dx z (signs)",
    [curlJ(jac(E11, *P11[0], 1e-6))[1]/jac(E11, *P11[0], 1e-6)[2, 0], curlJ(jac(H11, *P11[0], 1e-6))[2]/jac(H11, *P11[0], 1e-6)[1, 0]],
    [-1, 1], rtol=1e-6)
w11, k11 = 5*np.pi*1e8, 4*np.pi
v11d = w11/k11
chk("18.11(d) v, eps_r (c0, 3e8), eta = mu0 v", [v11d, (c0/v11d)**2, (3e8/v11d)**2, mu0*v11d], [1.25e8, 5.75, 5.76, 50*np.pi])
H11d = np.cross(-X, 10*Z)/(mu0*v11d)
chk("18.11(d) H amplitude vector [mA/m]", H11d*1e3, 63.7*Y)
chk("18.11(d) E x H direction; B = E/v and mu0 H [nT]",
    [*unit(np.cross(Z, H11d)), 10/v11d*1e9, mu0*np.linalg.norm(H11d)*1e9], [-1, 0, 0, 80, 80], atol=1e-9)
E11d = lambda r, t: 10*np.cos(w11*t + k11*r[0])*Z
H11dd = lambda r, t: 10/(mu0*v11d)*np.cos(w11*t + k11*r[0])*Y
P11d = rpts(40, [-0.5, -1, -1], [0.5, 1, 1], 0, 1e-8)
chk_pair("18.11(d) pair", E11d, H11dd, mu0, 1/(mu0*v11d**2), P11d, 1e-5, 1e-14)
Eadd = lambda r, t: 3*np.cos(w11*t + k11*r[0])*X
r_, t_ = P11d[0]
chk("18.11(e) div of the added field vs -12 pi sin(...)", np.trace(jac(Eadd, r_, t_, 1e-6)),
    -12*np.pi*np.sin(w11*t_ + k11*r_[0]), rtol=1e-6)
chk("18.11(e) curl of the added field", np.linalg.norm(curlJ(jac(Eadd, r_, t_, 1e-6))), 0, atol=1e-6)
_, rAe, _ = chk_pair("18.11(e) field of (d) plus the x component", lambda r, t: E11d(r, t) + Eadd(r, t), H11dd, mu0,
                     1/(mu0*v11d**2), P11d, 1e-5, 1e-14, expect=False)

# =====================================================================================
print("\n18.12 a wave on a slant")
kv = np.array([2.4*np.pi, 1.8*np.pi, 0])
w12 = 7.5*np.pi*1e8
u12 = unit(kv)
v12 = w12/np.linalg.norm(kv)
eta12 = mu0*v12
chk("18.12(a) u, angle [deg], v, eps_r", [*u12, np.degrees(np.arctan2(u12[1], u12[0])), v12, (c0/v12)**2],
    [0.8, 0.6, 0, 36.9, 2.5e8, 1.44], atol=1e-12)
E0v = np.array([6, -8, 0.0])
chk("18.12(b) E0.u", E0v @ u12, 0, atol=1e-12)
phi = lambda r, t: w12*t - kv @ r
E12 = lambda r, t: E0v*np.cos(phi(r, t))
H0v = np.cross(u12, E0v)/eta12
chk("18.12(c) eta [ohm], |E0|", [eta12, np.linalg.norm(E0v)], [100*np.pi, 10])
chk("18.12(c) u x E0 and H amplitude vector [mA/m]", [*np.cross(u12, E0v), *(H0v*1e3)], [0, 0, -10, 0, 0, -31.8],
    atol=1e-9)
chk("18.12(c) E0 x (-z) = 10 u", np.cross(E0v, -Z), 10*u12, atol=1e-12)
H12 = lambda r, t: H0v*np.cos(phi(r, t))
P12 = rpts(40, [-1, -1, -1], [1, 1, 1], 0, 1e-8)
r_, t_ = P12[3]
sp = np.sin(phi(r_, t_))
J12 = jac(E12, r_, t_, 1e-6)
chk("18.12(b) div E (FD)", np.trace(J12), 0, atol=1e-5)
chk("18.12(d) dEy/dx, dEx/dy, curl E (per sin phi)", [J12[1, 0]/sp, J12[0, 1]/sp, *(curlJ(J12)/sp)],
    [-19.2*np.pi, 10.8*np.pi, 0, 0, -30*np.pi], rtol=1e-5, atol=1e-5)
chk("18.12(d) -mu0 dH/dt (per sin phi)", -mu0*ddt(H12, r_, t_, 1e-15)/sp, -30*np.pi*Z, rtol=1e-5, atol=1e-5)
cH = curlJ(jac(H12, r_, t_, 1e-6))/sp
chk("18.12(d) curl H direction and |curl H| = 30 pi/eta = 10 eps omega",
    [*unit(cH), np.linalg.norm(cH), 30*np.pi/eta12, 10*w12/(eta12*v12)], [-0.6, 0.8, 0, 0.3, 0.3, 0.3], atol=1e-9,
    rtol=1e-6)
chk_pair("18.12 pair (E, H)", E12, H12, mu0, 1/(mu0*v12**2), P12, 1e-5, 1e-14)
E1p = lambda r, t: np.array([8, 6, 0.0])*np.cos(phi(r, t))
chk("18.12(e) E'.u and div E' (per sin phi)", [np.array([8, 6, 0]) @ u12, np.trace(jac(E1p, r_, t_, 1e-6))/sp],
    [10, 30*np.pi], rtol=1e-6)
H2p = np.cross(u12, 10*Z)/eta12
chk("18.12(e) u x z and H'' amplitude vector [mA/m]", [*np.cross(u12, Z), *(H2p*1e3)], [0.6, -0.8, 0, 19.1, -25.5, 0],
    atol=1e-9)
chk("18.12(e) z x (0.6x - 0.8y) = u", np.cross(Z, [0.6, -0.8, 0]), u12, atol=1e-12)
chk_pair("18.12(e) pair (E'', H'')", lambda r, t: 10*np.cos(phi(r, t))*Z, lambda r, t: H2p*np.cos(phi(r, t)), mu0,
         1/(mu0*v12**2), P12, 1e-5, 1e-14)
r1 = maxwell_res(E1p, lambda r, t: np.zeros(3), mu0, 1/(mu0*v12**2), P12[:10], 1e-5, 1e-14)
report(r1[2] > 0.1, f"18.12(e) E' has div E' != 0 (rel. {r1[2]:.2f})")

print(f"\nSUMMARY: {NF[1] - NF[0]} PASS, {NF[0]} FAIL out of {NF[1]} checks")
