#!/usr/bin/env python3
"""L18 practice checks: wave equation and plane TEM waves (numpy only).

Every number, sign and direction on practice/18-wave-equation-and-plane-waves.md is printed here.
Directions use np.cross; every claimed solution is checked by finite differences against the
wave equation AND against Faraday's law and the Ampere-Maxwell law (plus both divergences).
"""
import numpy as np

eps0 = 8.8541878128e-12
mu0 = 4e-7 * np.pi
c = 2.99792458e8
eta0 = np.sqrt(mu0 / eps0)
X, Y, Z = np.eye(3)
NAMES = {(1, 0, 0): "+x", (-1, 0, 0): "-x", (0, 1, 0): "+y", (0, -1, 0): "-y", (0, 0, 1): "+z", (0, 0, -1): "-z"}


def dname(v):
    v = np.asarray(v, float)
    n = v / np.linalg.norm(v)
    key = tuple(int(round(a)) for a in n)
    if np.allclose(n, key):
        return NAMES.get(key, str(key))
    return "(" + ", ".join(f"{a:+.4f}" for a in n) + ")"


def hdr(s):
    print("\n" + "=" * 78 + "\n" + s + "\n" + "=" * 78)


def U(s, w):  # smoothed unit step (for finite-difference checks of pulse fields)
    return 0.5 * (1 + np.tanh(s / w))


# ---------------------------------------------------------------- finite-difference vector calculus
def jac(F, r, t, h):
    r = np.asarray(r, float)
    J = np.zeros((3, 3))
    for j in range(3):
        e = np.zeros(3); e[j] = h
        J[:, j] = (F(r + e, t) - F(r - e, t)) / (2 * h)
    return J


def curl(F, r, t, h):
    J = jac(F, r, t, h)
    return np.array([J[2, 1] - J[1, 2], J[0, 2] - J[2, 0], J[1, 0] - J[0, 1]])


def div(F, r, t, h):
    return np.trace(jac(F, r, t, h))


def ddt(F, r, t, ht):
    return (F(r, t + ht) - F(r, t - ht)) / (2 * ht)


def lap(F, r, t, h):
    r = np.asarray(r, float)
    out = -6 * F(r, t)
    for j in range(3):
        e = np.zeros(3); e[j] = h
        out = out + F(r + e, t) + F(r - e, t)
    return out / h**2


def d2dt2(F, r, t, ht):
    return (F(r, t + ht) - 2 * F(r, t) + F(r, t - ht)) / ht**2


def rel(a, b):
    a, b = np.asarray(a, float), np.asarray(b, float)
    s = max(np.linalg.norm(a), np.linalg.norm(b), 1e-300)
    return np.linalg.norm(a - b) / s


def maxwell(label, E, H, mu, eps, pts, h, ht, h2=None, ht2=None):
    """Faraday, Ampere-Maxwell, both divergences, and the wave equation for E and H."""
    h2 = h2 or 30 * h
    ht2 = ht2 or 30 * ht
    rf = ra = dmax = we = wh = 0.0
    scaleE = scaleH = 0.0
    for (r, t) in pts:
        cE, dH = curl(E, r, t, h), -mu * ddt(H, r, t, ht)
        cH, dE = curl(H, r, t, h), eps * ddt(E, r, t, ht)
        rf = max(rf, rel(cE, dH)); ra = max(ra, rel(cH, dE))
        scaleE = max(scaleE, np.linalg.norm(cE)); scaleH = max(scaleH, np.linalg.norm(cH))
        dmax = max(dmax, abs(div(E, r, t, h)) / max(np.linalg.norm(cE), 1e-300) * 1.0,
                   abs(div(H, r, t, h)) / max(np.linalg.norm(cH), 1e-300))
        we = max(we, rel(lap(E, r, t, h2), mu * eps * d2dt2(E, r, t, ht2)))
        wh = max(wh, rel(lap(H, r, t, h2), mu * eps * d2dt2(H, r, t, ht2)))
    ok = max(rf, ra, we, wh) < 1e-4 and dmax < 1e-6
    print(f"  [{label}] Faraday rel.res {rf:.1e} | Ampere-Maxwell {ra:.1e} | div/curl {dmax:.1e} | "
          f"wave eq E {we:.1e}, H {wh:.1e}  -> {'OK' if ok else 'FAIL'}")
    return ok


def cross_line(a, b, an, bn):
    r = np.cross(a, b)
    print(f"  {an} x {bn} = {np.round(r, 6)}  ({dname(r)})")
    return r


rng = np.random.default_rng(18)
ALL = []

# =========================================================================================== 18.1
hdr("18.1 Which way and how fast (multiple choice)")


def vel(phi_t, grad):
    grad = np.asarray(grad, float)
    return -phi_t * grad / grad.dot(grad)


vp = vel(2 * np.pi * 1e8, [0.8 * np.pi, 0, 0])
vq = vel(-1.0, [0, 0, 0.004])
vr = vel(1.0, [0, 0.0125, 0])
print("p = 5 cos(2pi 1e8 t + 0.8 pi x): v =", vp, "m/s ->", dname(vp), f"speed {np.linalg.norm(vp):.4e}")
print("q = u(0.004 z - t):              v =", vq, "m/s ->", dname(vq), f"speed {np.linalg.norm(vq):.4g}")
print("r = exp(-(t + 0.0125 y)^2):      v =", vr, "m/s ->", dname(vr), f"speed {np.linalg.norm(vr):.4g}")
# feature tracking
for t in [0.0, 1.0, 2.0]:
    zz = np.linspace(-100, 800, 900001)
    q = U(0.004 * zz - t, 1e-6)
    zedge = zz[np.argmin(abs(q - 0.5))]
    yy = np.linspace(-300, 100, 400001)
    ypk = yy[np.argmax(np.exp(-(t + 0.0125 * yy) ** 2))]
    print(f"  t = {t:.0f} s: edge of q at z = {zedge:.3f} m; peak of r at y = {ypk:.3f} m")
for tn in [0.0, 1.0, 2.0]:  # crest of p (phase 0) in ns
    t = tn * 1e-9
    xs = np.linspace(-0.8, 0.3, 1100001)
    ph = 2 * np.pi * 1e8 * t + 0.8 * np.pi * xs
    xc = xs[np.argmin(abs(ph))]
    print(f"  t = {tn:.0f} ns: crest (phase 0) of p at x = {xc:.4f} m")
print(f"  slownesses: q 0.004 s/m -> 1/0.004 = {1/0.004:.0f} m/s; r 0.0125 s/m -> {1/0.0125:.0f} m/s")
print(f"  p slower than c: non-magnetic eps_r = (c/v)^2 = {(c/2.5e8)**2:.4f} (c = 3e8: {(3e8/2.5e8)**2:.4f})")
print("  options: (a) +2.5e8 x, +250 z, -80 y  (b) -2.5e8 x, -250 z, -80 y  (c) -2.5e8 x, +250 z, -80 y [correct]")
print("           (d) -2.5e8 x, +0.004 z, -0.0125 y  (e) -2.5e8 x, +250 z, +80 y")

# =========================================================================================== 18.2
hdr("18.2 The partner field (free space)")
w2 = 2 * np.pi * 1e9
tau = 1e-9
# (a)
uA, eA = Z, Y
hA = np.cross(uA, eA)
print("(a) E = 6 y cos(w(t - z/c)):  u = +z")
cross_line(uA, eA, "z", "y")
print(f"    |H| = 6/eta0 = {6/eta0*1e3:.3f} mA/m (120pi: {6/(120*np.pi)*1e3:.3f}); |B| = 6/c = {6/c*1e9:.3f} nT")
cross_line(eA, hA, "E(y)", "H(-x)")
E = lambda r, t: 6 * Y * np.cos(w2 * (t - r[2] / c))
H = lambda r, t: hA * 6 / eta0 * np.cos(w2 * (t - r[2] / c))
pts = [(rng.uniform(-0.5, 0.5, 3), rng.uniform(0, 2e-9)) for _ in range(6)]
ALL.append(maxwell("18.2a", E, H, mu0, eps0, pts, 1e-6, 1e-6 / c))
# (b)
uB, eB = -Y, X
hB = np.cross(uB, eB)
print("(b) E = 3 x exp(-((t + y/c)/tau)^2):  u = -y")
cross_line(uB, eB, "(-y)", "x")
print(f"    |H| = 3/eta0 = {3/eta0*1e3:.3f} mA/m; |B| = 3/c = {3/c*1e9:.3f} nT")
cross_line(eB, hB, "E(x)", "H(+z)")
E = lambda r, t: 3 * X * np.exp(-((t + r[1] / c) / tau) ** 2)
H = lambda r, t: hB * 3 / eta0 * np.exp(-((t + r[1] / c) / tau) ** 2)
pts = [(np.array([0.1, -0.2, 0.3]) + rng.uniform(-0.1, 0.1, 3), rng.uniform(-1e-9, 1e-9)) for _ in range(6)]
ALL.append(maxwell("18.2b", E, H, mu0, eps0, pts, 1e-6, 1e-6 / c))
# (c) reverse: E = eta H x u
uC, hC = X, Z
eC = np.cross(hC, uC)
print("(c) H = 0.05 z cos(w(t - x/c)) A/m:  u = +x;  E = eta0 H x u")
cross_line(hC, uC, "z", "x")
print(f"    |E| = eta0*0.05 = {eta0*0.05:.3f} V/m (120pi: {120*np.pi*0.05:.3f}); |B| = mu0*0.05 = {mu0*0.05*1e9:.3f} nT"
      f" = E/c = {eta0*0.05/c*1e9:.3f} nT")
cross_line(eC, hC, "E(+y)", "H(z)")
print("    check also H = u x E/eta0:", np.cross(uC, eC), "= z")
E = lambda r, t: eC * eta0 * 0.05 * np.cos(w2 * (t - r[0] / c))
H = lambda r, t: hC * 0.05 * np.cos(w2 * (t - r[0] / c))
pts = [(rng.uniform(-0.5, 0.5, 3), rng.uniform(0, 2e-9)) for _ in range(6)]
ALL.append(maxwell("18.2c", E, H, mu0, eps0, pts, 1e-6, 1e-6 / c))

# =========================================================================================== 18.3
hdr("18.3 Phase rate and snapshot period (SP18 Exam 2 #1(vii) style)")
w3 = 6 * np.pi / 10e-9
b3 = 2 * np.pi / 0.4
v3 = w3 / b3
er3 = (c / v3) ** 2
eta3 = mu0 * v3
print(f"omega = 6pi/10 ns = {w3:.4e} rad/s (= 6pi x 1e8); beta = 2pi/0.4 = {b3:.4f} rad/m (= 5pi)")
print(f"v = omega/beta = {v3:.4e} m/s; temporal period 2pi/omega = {2*np.pi/w3*1e9:.4f} ns; 0.4 m / period = {0.4/(2*np.pi/w3):.4e}")
print(f"eps_r = (c/v)^2 = {er3:.4f} (c = 3e8: {(3e8/v3)**2:.4f}); eta = mu0 v = {eta3:.3f} Ohm = {eta3/np.pi:.3f} pi;"
      f" eta0/sqrt(eps_r) = {eta0/np.sqrt(er3):.3f}")
print(f"H amplitude = 12/eta = {12/eta3*1e3:.3f} mA/m; B = 12/v = {12/v3*1e9:.3f} nT = mu0 H = {mu0*12/eta3*1e9:.3f} nT")
cross_line(X, Y, "u(+x)", "E(y)")
cross_line(Y, Z, "E(y)", "H(z)")
E = lambda r, t: 12 * Y * np.cos(w3 * t - b3 * r[0])
H = lambda r, t: Z * 12 / eta3 * np.cos(w3 * t - b3 * r[0])
pts = [(rng.uniform(-1, 1, 3), rng.uniform(0, 5e-9)) for _ in range(6)]
ALL.append(maxwell("18.3", E, H, mu0, er3 * eps0, pts, 1e-6, 1e-6 / v3))

# =========================================================================================== 18.4
hdr("18.4 What the derivation needs (true or false)")
# (a) without dD/dt: curl curl E = -mu d(curl H)/dt = 0 -> grad div E - lap E = 0 -> lap E = 0 (div E = 0).
w4, v4 = 2 * np.pi * 1e8, c
E = lambda r, t: X * np.cos(w4 * (t - r[2] / v4))
r0, t0 = np.array([0.1, 0.2, 0.3]), 1.3e-9
L = lap(E, r0, t0, 1e-3)
print(f"(a) travelling wave: lap E_x = {L[0]:.4f}, -(w/v)^2 E_x = {-(w4/v4)**2*E(r0,t0)[0]:.4f}  -> lap E != 0, so it"
      " cannot satisfy Laplace's equation (what remains without dD/dt)")
# (b) fixed non-uniform rho(x) = rho0 x/a, J = 0; static E_x = rho0 x^2/(2 eps a) plus a wave
rho0, a4, eps4 = 1e-9, 1.0, 4 * eps0
Es = lambda r, t: X * rho0 * r[0] ** 2 / (2 * eps4 * a4)
Ew = lambda r, t: Y * 3 * np.cos(w4 * (t - r[2] * np.sqrt(mu0 * eps4)))
Etot = lambda r, t: Es(r, t) + Ew(r, t)
r0 = np.array([0.7, -0.2, 0.4]); t0 = 2.1e-9
print(f"(b) div(eps E) = rho check: eps*dEx/dx = {eps4*div(Es, r0, t0, 1e-4):.4e} vs rho = {rho0*r0[0]/a4:.4e}")
lhs = lap(Etot, r0, t0, 1e-3) - mu0 * eps4 * d2dt2(Etot, r0, t0, 1e-12)
print(f"    lap E - mu eps d2E/dt2 = {np.round(lhs, 4)}; grad(rho)/eps = {np.round(X*rho0/(a4*eps4), 4)}  -> extra term, statement FALSE")
# (c) graded eps(x) = eps0 (1 + x/a): E = x E0/(1 + x/a) has div D = 0 but div E != 0
E0c = 2.0
Ec = lambda r, t: X * E0c / (1 + r[0] / a4)
Dc = lambda r, t: eps0 * (1 + r[0] / a4) * Ec(r, t)
print(f"(c) div D = {div(Dc, np.zeros(3), 0, 1e-5):.3e} (zero); div E at x=0 = {div(Ec, np.zeros(3), 0, 1e-5):.5f} V/m^2"
      f" = -E0/a = {-E0c/a4:.5f}  -> FALSE")
# (d) z-polarized along z
vd = c
Ez = lambda r, t: Z * np.cos(w4 * (t - r[2] / vd))
r0, t0 = np.array([0, 0, 0.2]), 0.7e-9
res1d = rel(lap(Ez, r0, t0, 1e-3), mu0 * eps0 * d2dt2(Ez, r0, t0, 1e-3 / c))
print(f"(d) E = z cos(w(t - z/v)): 1D wave-equation rel. residual {res1d:.1e} (solves it), but div E = {div(Ez, r0, t0, 1e-5):.4f}"
      f" vs (w/v) sin(.) = {(w4/vd)*np.sin(w4*(t0 - r0[2]/vd)):.4f}  -> violates Gauss (rho = 0): FALSE")
print(f"    and curl E = {np.round(curl(Ez, r0, t0, 1e-5), 12)} -> Faraday gives no H partner")

# =========================================================================================== 18.5
hdr("18.5 Find the error: H pointing the wrong way")
w5, b5 = 1.5 * np.pi * 1e8, 2 * np.pi
v5 = w5 / b5
er5 = (c / v5) ** 2
eta5 = mu0 * v5
print(f"E = z 12 cos(1.5pi e8 t + 2pi x): same signs -> travels -x; v = {v5:.4e} m/s; eps_r = {er5:.3f} (c=3e8: {(3e8/v5)**2:.3f})")
print(f"eta = mu0 v = {eta5:.3f} Ohm = {eta5/np.pi:.3f} pi (eta0/4 = {eta0/4:.3f}); |H| = 12/eta = {12/eta5:.5f} A/m = {12/eta5*1e3:.1f} mA/m")
uu = -X
Hc = cross_line(uu, Z, "u(-x)", "z")          # correct
Hs = cross_line(Z, uu, "z", "u(-x)")          # student's order
cross_line(Z, Hc, "E(z)", "H_correct")
cross_line(Z, Hs, "E(z)", "H_student")
E = lambda r, t: 12 * Z * np.cos(w5 * t + b5 * r[0])
Hgood = lambda r, t: Hc * 12 / eta5 * np.cos(w5 * t + b5 * r[0])
Hbad = lambda r, t: Hs * 12 / eta5 * np.cos(w5 * t + b5 * r[0])
pts = [(rng.uniform(-1, 1, 3), rng.uniform(0, 20e-9)) for _ in range(6)]
ALL.append(maxwell("18.5 correct H = +y", E, Hgood, mu0, er5 * eps0, pts, 1e-6, 1e-6 / v5))
r0, t0 = pts[0]
print(f"  [18.5 student's H = -y] Faraday rel.res {rel(curl(E, r0, t0, 1e-6), -mu0*ddt(Hbad, r0, t0, 1e-6/v5)):.2f} (2 = opposite sign) -> FAILS")

# =========================================================================================== 18.6
hdr("18.6 Which fields can be waves (mu eps = 1e-16 s^2/m^2, mu = mu0)")
me = 1e-16
v6 = 1 / np.sqrt(me)
eps6 = me / mu0
eta6 = mu0 * v6
print(f"v = 1/sqrt(mu eps) = {v6:.4e} m/s; eps_r = {eps6/eps0:.4f}; eta = mu0 v = {eta6:.4f} Ohm = {eta6/np.pi:.4f} pi")
w6, b6 = 2e8, 2.0
cands = {
    "E1 = 4 cos(2e8 t - 2z)": lambda z, t: 4 * np.cos(w6 * t - b6 * z),
    "E2 = 4 cos(2e8 t) cos(2z)": lambda z, t: 4 * np.cos(w6 * t) * np.cos(b6 * z),
    "E3 = 4 cos(2e8 t - 6z)": lambda z, t: 4 * np.cos(w6 * t - 6 * z),
    "E4 = 4 cos(2e8 t - 2z) cos(2e8 t + 2z)": lambda z, t: 4 * np.cos(w6 * t - b6 * z) * np.cos(w6 * t + b6 * z),
}
for name, f in cands.items():
    worst = 0
    for _ in range(8):
        z, t = rng.uniform(-2, 2), rng.uniform(0, 1e-7)
        hz, ht = 1e-4, 1e-4 / v6
        fzz = (f(z + hz, t) - 2 * f(z, t) + f(z - hz, t)) / hz**2
        ftt = (f(z, t + ht) - 2 * f(z, t) + f(z, t - ht)) / ht**2
        worst = max(worst, abs(fzz - me * ftt) / max(abs(fzz), abs(me * ftt), 1e-9))
    print(f"  {name:<42} max rel. residual of d2/dz2 - mu eps d2/dt2: {worst:.2e} -> {'SOLVES' if worst < 1e-5 else 'fails'}")
print(f"  omega^2 = (2e8)^2 = {w6**2:.0e} rad^2/s^2; beta^2 = {b6**2:.0f}; mu eps omega^2 = {me*w6**2:.0f}")
print(f"  E3: d2/dz2 = -36 E, mu eps d2/dt2 = -{me*w6**2:.0f} E; own speed 2e8/6 = {2e8/6:.4e} m/s; needs mu eps = {(6/2e8)**2:.1e}"
      f" -> eps_r = {(6/2e8)**2/(mu0*eps0):.2f}")
z, t = 0.0, np.pi / 4e8
print(f"  E4 = 2cos(4z) + 2cos(4e8 t): at z = 0, t = pi/4e8 = {t*1e9:.4f} ns: d2/dz2 = {-32*np.cos(4*z):.1f},"
      f" mu eps d2/dt2 = {me*(-2*16e16*np.cos(4e8*t)):.1f}")
zz, tt = rng.uniform(-2, 2, 5), rng.uniform(0, 1e-7, 5)
print("  E4 identity check:", np.allclose(cands["E4 = 4 cos(2e8 t - 2z) cos(2e8 t + 2z)"](zz, tt), 2*np.cos(4*zz) + 2*np.cos(4e8*tt)))
H0 = 4 / eta6
print(f"(b) H for E2: H_y = (E0/eta) sin(wt) sin(bz), E0/eta = {H0:.6f} A/m = {H0*1e3:.2f} mA/m (= 1/(10 pi) = {1/(10*np.pi):.6f})")
E = lambda r, t: X * 4 * np.cos(w6 * t) * np.cos(b6 * r[2])
H = lambda r, t: Y * H0 * np.sin(w6 * t) * np.sin(b6 * r[2])
pts = [(rng.uniform(-2, 2, 3), rng.uniform(0, 1e-7)) for _ in range(8)]
ALL.append(maxwell("18.6 standing pair (E2, H2)", E, H, mu0, eps6, pts, 1e-6, 1e-6 / v6))
Hwrong = lambda r, t: -Y * H0 * np.sin(w6 * t) * np.sin(b6 * r[2])
r0, t0 = pts[0]
print(f"  with the opposite sign of H: Faraday rel.res {rel(curl(E, r0, t0, 1e-6), -mu0*ddt(Hwrong, r0, t0, 1e-6/v6)):.2f} (fails)")
# (c) decomposition
zz, tt = rng.uniform(-3, 3, 7), rng.uniform(0, 1e-7, 7)
Esum = 2 * np.cos(w6 * tt - b6 * zz) + 2 * np.cos(w6 * tt + b6 * zz)
Hsum = (2 * np.cos(w6 * tt - b6 * zz) - 2 * np.cos(w6 * tt + b6 * zz)) / eta6
print("(c) E2 = 2cos(wt-bz) + 2cos(wt+bz):", np.allclose(Esum, 4*np.cos(w6*tt)*np.cos(b6*zz)),
      "; H = (2/eta)[cos(wt-bz) - cos(wt+bz)] = H2:", np.allclose(Hsum, H0*np.sin(w6*tt)*np.sin(b6*zz)))
print(f"    each travelling part: E amplitude 2 V/m, H amplitude 2/eta = {2/eta6*1e3:.2f} mA/m")
tz = np.pi / (2 * w6)
print(f"(d) E = 0 everywhere when w t = pi/2: t = {tz*1e9:.4f} ns; then H_y = {H0*1e3:.2f} sin(2z) mA/m,"
      f" largest at z = pi/4 = {np.pi/4:.4f} m (and every pi/2 = {np.pi/2:.4f} m)")
print(f"    E2 nodes (E = 0 at all t): cos(2z) = 0 -> z = pi/4 + n pi/2; H2 nodes: sin(2z) = 0 -> z = n pi/2")

# =========================================================================================== 18.7
hdr("18.7 A cable and its filling (parallel strips W = 8 mm, d = 1 mm)")
W, d, ell, T7 = 8e-3, 1e-3, 3.0, 18e-9
v7 = ell / T7
er7, er7c = (c / v7) ** 2, (3e8 / v7) ** 2
eta7 = mu0 * v7
print(f"v = 3 m / 18 ns = {v7:.5e} m/s; eps_r = (c/v)^2 = {er7:.4f} (c = 3e8: {er7c:.4f} = 1.8^2)")
print(f"eta = mu0 v = {eta7:.3f} Ohm; eta0/1.8 = {eta0/1.8:.3f}; 120pi/1.8 = {120*np.pi/1.8:.3f}")
for er in (er7c, er7):
    Cp = er * eps0 * W / d
    Lp = mu0 * d / W
    print(f"  eps_r = {er:.4f}: C' = eps W/d = {Cp*1e12:.2f} pF/m; L' = mu0 d/W = {Lp*1e9:.2f} nH/m ({Lp*1e6:.4f} uH/m);"
          f" 1/sqrt(L'C') = {1/np.sqrt(Lp*Cp):.5e} m/s; sqrt(L'/C') = {np.sqrt(Lp/Cp):.3f} Ohm;"
          f" eta d/W = {np.sqrt(mu0/(er*eps0))*d/W:.3f} Ohm; L'C' = {Lp*Cp:.4e} = mu eps = {mu0*er*eps0:.4e}")
lnba = 2 * np.pi * d / W
print(f"coax with the same sqrt(L'/C'): (eta/2pi) ln(b/a) = eta d/W -> ln(b/a) = 2pi d/W = {lnba:.4f} (pi/4); b/a = {np.exp(lnba):.4f}")
Lc = mu0 / (2 * np.pi) * lnba
Cc = 2 * np.pi * er7c * eps0 / lnba
print(f"  coax L' = {Lc*1e9:.2f} nH/m, C' = {Cc*1e12:.2f} pF/m (identical to the strips); delay over 3 m = {ell*np.sqrt(Lc*Cc)*1e9:.2f} ns"
      f" (with c=3e8 eps_r: {ell/v7*1e9:.1f} ns)")
print(f"  sqrt(L'/C') coax = {np.sqrt(Lc/Cc):.3f} Ohm")

# =========================================================================================== 18.8
hdr("18.8 A probe record turned into snapshots (vacuum, travel +x, E along z; c = 300 m/us, eta0 = 120 pi)")
ETA = 120 * np.pi
cus = 300.0  # m/us


def F8(s):  # record at x = 0 (s in us)
    s = np.asarray(s, float)
    return np.where((s > 0) & (s < 1), 5.0, np.where((s > 1) & (s < 3), -2.0, 0.0))


for x in [-400, -300, -100, 0, 100, 299, 301, 450, 599, 601, 700]:
    print(f"  snapshot t = 2 us: x = {x:5d} m -> s = {2 - x/cus:+.4f} us, E_z = {float(F8(2 - x/cus)):+.0f} V/m")
for t in [2.9, 3.1, 3.9, 4.1, 5.9, 6.1]:
    print(f"  probe x = 900 m: t = {t:.1f} us -> E_z = {float(F8(t - 900/cus)):+.0f} V/m")
print(f"  probe x = 900 m: starts at t = {900/cus:.0f} us, sign change at t = {900/cus+1:.0f} us, ends at {900/cus+3:.0f} us")
u8 = X
hdir = np.cross(u8, Z)
print("  H = u x E/eta0 with E = E_z z:", end=" "); cross_line(X, Z, "x", "z")
for (x, t) in [(450, 2.0), (0, 2.0)]:
    Ez = float(F8(t - x / cus))
    Hv = np.cross(u8, Ez * Z) / ETA
    print(f"  at x = {x} m, t = {t} us: E = {Ez:+.0f} z V/m, H = {np.round(Hv*1e3, 3)} mA/m ({dname(Hv)}), |B| = |E|/c ="
          f" {abs(Ez)/3e8*1e9:.3f} nT; E x H -> {dname(np.cross(Ez*Z, Hv))}")
# smooth stand-in: Maxwell check of E = z F(t - x/c), H = -y F/eta0 (SI units)
wsm = 0.02e-6


def F8s(s):
    return 5 * (U(s, wsm) - U(s - 1e-6, wsm)) - 2 * (U(s - 1e-6, wsm) - U(s - 3e-6, wsm))


E = lambda r, t: Z * F8s(t - r[0] / c)
H = lambda r, t: np.cross(X, Z) * F8s(t - r[0] / c) / eta0
# (points chosen off the exact inflection of the tanh edges, where both sides of the wave equation vanish to round-off)
pts = [(np.array([xx, 0.3, -0.2]), tt) for xx, tt in [(0, 1.01e-6), (150, 1.508e-6), (300, 2.012e-6), (100, 1.33e-6)]]
ALL.append(maxwell("18.8 smoothed record", E, H, mu0, eps0, pts, 0.01, 0.01 / c, 0.3, 0.3 / c))
Hbad8 = lambda r, t: np.cross(Z, X) * F8s(t - r[0] / c) / eta0
r0, t0 = pts[1]
print(f"  with H = +y E_z/eta0 instead: Faraday rel.res {rel(curl(E, r0, t0, 0.01), -mu0*ddt(Hbad8, r0, t0, 0.01/c)):.2f} (fails)")

# =========================================================================================== 18.9
hdr("18.9 SP18 Exam 2 #4 style: triangle pulse moving -z at 150 m/us, x-polarized")
v9 = 150.0  # m/us


def g9(zz):  # snapshot at t1 = 2 us, z in m
    zz = np.asarray(zz, float)
    return np.where((zz >= 300) & (zz <= 450), 0.04 * (zz - 300),
                    np.where((zz > 450) & (zz <= 900), (900 - zz) / 75, 0.0))


def F9(s):  # d'Alembert form, s = t + z/150 in us
    s = np.asarray(s, float)
    return np.where((s >= 4) & (s <= 5), 6 * (s - 4), np.where((s > 5) & (s <= 8), 2 * (8 - s), 0.0))


print(f"  snapshot peak g(450) = {float(g9(450)):.2f} V/m; g(300) = {float(g9(300)):.2f}; g(900) = {float(g9(900)):.2f}")
zz = rng.uniform(-2000, 3000, 20000); tt = rng.uniform(-5, 20, 20000)
print("  E(z,t) = g(z + 150 t - 300) equals F(t + z/150):", np.allclose(g9(zz + v9 * tt - 300), F9(tt + zz / v9)))
print("  E(z,0) = g(z - 300):", [(z, float(g9(z - 300))) for z in (600, 675, 750, 975, 1200)])
print("  E(z,0) formula 0.04(z-600) on [600,750], (1200-z)/75 on [750,1200]:",
      np.allclose(g9(zz - 300), np.where((zz >= 600) & (zz <= 750), 0.04 * (zz - 600),
                                          np.where((zz > 750) & (zz <= 1200), (1200 - zz) / 75, 0))))
print("  front (6 V/m side... front edge) z_front(t) = 600 - 150 t; at t=2:", 600 - 150 * 2, "; reaches -750 m at t =", (600 + 750) / 150, "us")
for t in [9.0, 9.5, 10.0, 11.5, 13.0]:
    print(f"  probe z = -750 m, t = {t:4.1f} us: s = {t - 750/v9:.2f}, E_x = {float(F9(t - 750/v9)):.2f} V/m")
print(f"  shift at t = 11.5 us: z + 150*11.5 - 300 = z + {150*11.5 - 300:.0f}")
print("  cross-check snapshot at t = 11.5 us, z = -750: g(z + 150*11.5 - 300) =", float(g9(-750 + 150 * 11.5 - 300)))
zw = np.linspace(-500, 1500, 200001); nz = zw[g9(zw + 300) > 0]
print(f"  wrong shift g(z + 300) at t = 0 occupies [{nz.min():.0f}, {nz.max():.0f}] m (pulse at [300, 900] m at 2 us -> would mean +z travel)")
mrer = (c / 1.5e8) ** 2
eta_meas = 6 / 15.9e-3
ratio = (eta_meas / eta0) ** 2
mur, epr = np.sqrt(mrer * ratio), np.sqrt(mrer / ratio)
print(f"  mu_r eps_r = (c/v)^2 = {mrer:.4f}; measured eta = 6/15.9 mA/m = {eta_meas:.2f} Ohm (eta0 = {eta0:.2f});"
      f" mu_r/eps_r = {ratio:.4f} -> mu_r = {mur:.3f}, eps_r = {epr:.3f}")
eta9 = 2 * mu0 * 1.5e8
print(f"  with mu_r = eps_r = 2: eta = mu v = 2 mu0 (1.5e8) = {eta9:.3f} Ohm (= 120 pi = {120*np.pi:.3f}); eta0 sqrt(1) = {eta0:.3f}")
print(f"  peak H = 6/eta = {6/eta9*1e3:.3f} mA/m; peak B = mu H = {2*mu0*6/eta9*1e9:.3f} nT = E/v = {6/1.5e8*1e9:.3f} nT")
u9 = -Z
h9 = cross_line(u9, X, "u(-z)", "x")
cross_line(X, h9, "E(x)", "H(-y)")
print(f"  H at probe z = -750 m, t = 11.5 us: {np.round(h9*3/eta9*1e3, 3)} mA/m")
# Maxwell check: exact piecewise-linear F at interior points (first derivatives), and a smooth stand-in for the wave equation
mu9, eps9 = 2 * mu0, 2 * eps0
v9si = 1 / np.sqrt(mu9 * eps9)
eta9x = np.sqrt(mu9 / eps9)
print(f"  exact constants: v = {v9si:.5e} m/s, eta = {eta9x:.3f} Ohm")
E = lambda r, t: X * F9((t + r[2] / v9si) * 1e6)
H = lambda r, t: np.cross(-Z, X) * F9((t + r[2] / v9si) * 1e6) / eta9x
for (z, t) in [(-750, 9.5e-6), (-750, 11.5e-6), (300, 2.3e-6), (600, 1.0e-6)]:
    r = np.array([0.1, 0.2, z])
    s = (t + z / v9si) * 1e6
    cE, dH = curl(E, r, t, 1e-3), -mu9 * ddt(H, r, t, 1e-3 / v9si)
    cH, dE = curl(H, r, t, 1e-3), eps9 * ddt(E, r, t, 1e-3 / v9si)
    print(f"    z = {z} m, t = {t*1e6:.1f} us (s = {s:.3f}): Faraday rel.res {rel(cE, dH):.1e}, Ampere {rel(cH, dE):.1e},"
          f" |curl E| = {np.linalg.norm(cE):.3e}")
Fs = lambda s: 6 * np.exp(-((s - 5e-6) / 1e-6) ** 2)
E = lambda r, t: X * Fs(t + r[2] / v9si)
H = lambda r, t: np.cross(-Z, X) * Fs(t + r[2] / v9si) / eta9x
pts = [(np.array([0, 0, z]), t) for z, t in [(-750, 10e-6), (-600, 9.4e-6), (0, 4.6e-6)]]
ALL.append(maxwell("18.9 smooth stand-in, same direction/eta", E, H, mu9, eps9, pts, 0.01, 0.01 / v9si, 1.0, 1.0 / v9si))

# =========================================================================================== 18.10
hdr("18.10 Two pulses passing through each other (vacuum, c = 300 m/us, eta0 = 120 pi)")


def fA(s):  # +z pulse, s = t - z/300 (us)
    s = np.asarray(s, float); return np.where((s > 1) & (s < 2), 6.0, 0.0)


def gB(s):  # -z pulse, s = t + z/300 (us)
    s = np.asarray(s, float); return np.where((s > 1) & (s < 3), 3.0, 0.0)


def gBp(s):  # replacement pulse B': -6 V/m on 300 < z < 600 at t = 0
    s = np.asarray(s, float); return np.where((s > 1) & (s < 2), -6.0, 0.0)


def fields10(z, t, g=gB):
    a, b = fA(t - z / cus), g(t + z / cus)
    return a + b, (a - b) / ETA


for (lbl, g) in [("A alone", None), ("B alone", None)]:
    pass
print(f"  A: H_y = +6/eta0 = {6/ETA*1e3:.3f} mA/m; B: H_y = -3/eta0 = {-3/ETA*1e3:.3f} mA/m")
cross_line(Z, X, "u_A(+z)", "x"); cross_line(-Z, X, "u_B(-z)", "x")
print("  at t = 0: A occupies z in (-600,-300):", float(fA(0 + 450 / cus)), "at z=-450; B occupies (300,900):", float(gB(0 + 600 / cus)), "at z=600")
for z in [-200, -149, -100, 0, 100, 149, 151, 300, 449, 451]:
    E, Hy = fields10(z, 1.5)
    print(f"  t = 1.5 us, z = {z:5d} m: E_x = {float(E):.0f} V/m, H_y = {float(Hy)*1e3:+.3f} mA/m"
          + (f", E/H = {float(E)/float(Hy):.1f} Ohm" if abs(float(Hy)) > 0 else ""))
print(f"  overlap ratio E_x/H_y = 9/(3/eta0) = 3 eta0 = {3*ETA:.1f} Ohm (360 pi); single pulse: +/- eta0 = {ETA:.1f}")
for t in [0.9, 1.2, 1.8, 2.2, 2.8, 3.2]:
    E, Hy = fields10(0.0, t)
    print(f"  probe z = 0, t = {t:.1f} us: E_x = {float(E):.0f} V/m, H_y = {float(Hy)*1e3:+.3f} mA/m")
for z in [-800, -600, -301, -299, 0, 599, 601, 750, 899, 901]:
    E, Hy = fields10(z, 4.0)
    print(f"  t = 4 us, z = {z:5d} m: E_x = {float(E):.0f}, H_y = {float(Hy)*1e3:+.3f} mA/m")
for z in [-200, -100, 0, 100, 140, 160]:
    E, Hy = fields10(z, 1.5, gBp)
    print(f"  B' case, t = 1.5 us, z = {z:4d} m: E_x = {float(E):.0f} V/m, H_y = {float(Hy)*1e3:+.3f} mA/m")
print(f"  B' alone: H_y = -(-6)/eta0 = {6/ETA*1e3:.3f} mA/m; overlap H_y = 12/eta0 = {12/ETA*1e3:.3f} mA/m")
cross_line(-Z, -6 * X, "u_B'(-z)", "(-6x)")
for z in [-500, -400, -200, 200, 300, 449, 550]:
    E, Hy = fields10(z, 2.5, gBp)
    print(f"  B' case, t = 2.5 us, z = {z:4d} m: E_x = {float(E):.0f} V/m, H_y = {float(Hy)*1e3:+.3f} mA/m")
# Maxwell check of the total smoothed field (SI)
ws = 0.01e-6
fAs = lambda s: 6 * (U(s - 1e-6, ws) - U(s - 2e-6, ws))
gBs = lambda s: 3 * (U(s - 1e-6, ws) - U(s - 3e-6, ws))
E = lambda r, t: X * (fAs(t - r[2] / c) + gBs(t + r[2] / c))
H = lambda r, t: Y * (fAs(t - r[2] / c) - gBs(t + r[2] / c)) / eta0
pts = [(np.array([0, 0, z]), t) for z, t in [(-147, 1.5e-6), (149, 1.5e-6), (0.5, 1.0e-6), (448, 1.5e-6), (0, 2.0e-6)]]
ALL.append(maxwell("18.10 total field, E adds / H subtracts", E, H, mu0, eps0, pts, 0.01, 0.01 / c, 0.3, 0.3 / c))
H_bad = lambda r, t: Y * (fAs(t - r[2] / c) + gBs(t + r[2] / c)) / eta0
r0, t0 = np.array([0, 0, 449.0]), 1.5e-6   # on the back edge of B, where g changes
print(f"  with H = (f + g)/eta0 instead: Ampere rel.res {rel(curl(H_bad, r0, t0, 0.01), eps0*ddt(E, r0, t0, 0.01/c)):.2f} (fails)")

# =========================================================================================== 18.11
hdr("18.11 The derivation along x: E = z E_z(x,t), H = y H_y(x,t)")
mu_, eps_ = mu0, 3 * eps0
v11 = 1 / np.sqrt(mu_ * eps_)
eta11 = np.sqrt(mu_ / eps_)
f11 = lambda s: np.exp(-(s / 2e-9) ** 2)
g11 = lambda s: np.cos(3e8 * s) * np.exp(-(s / 5e-9) ** 2)
A_, B_ = 1.7, -0.8
E = lambda r, t: Z * (A_ * f11(t - r[0] / v11) + B_ * g11(t + r[0] / v11))
H = lambda r, t: Y * (-A_ * f11(t - r[0] / v11) + B_ * g11(t + r[0] / v11)) / eta11
r0, t0 = np.array([0.3, -0.1, 0.2]), 1.1e-9
cE = curl(E, r0, t0, 1e-5)
dEzdx = (E(r0 + 1e-5 * X, t0) - E(r0 - 1e-5 * X, t0))[2] / 2e-5
print(f"  curl(z E_z) = {np.round(cE, 6)}; -dE_z/dx y = {np.round(-dEzdx*Y, 6)}  (Faraday y-comp: dEz/dx = mu dHy/dt)")
cH = curl(H, r0, t0, 1e-5)
dHydx = (H(r0 + 1e-5 * X, t0) - H(r0 - 1e-5 * X, t0))[1] / 2e-5
print(f"  curl(y H_y) = {np.round(cH, 8)}; +dH_y/dx z = {np.round(dHydx*Z, 8)}  (Ampere z-comp: dHy/dx = eps dEz/dt)")
print(f"  dEz/dx = {dEzdx:.6e}; mu dHy/dt = {mu_*ddt(H, r0, t0, 1e-5/v11)[1]:.6e}")
print(f"  dHy/dx = {dHydx:.6e}; eps dEz/dt = {eps_*ddt(E, r0, t0, 1e-5/v11)[2]:.6e}")
pts = [(rng.uniform(-1, 1, 3), rng.uniform(-3e-9, 3e-9)) for _ in range(6)]
ALL.append(maxwell("18.11 H_y = (Bg - Af)/eta", E, H, mu_, eps_, pts, 1e-6, 1e-6 / v11))
Hz_sign = lambda r, t: Y * (A_ * f11(t - r[0] / v11) - B_ * g11(t + r[0] / v11)) / eta11
print(f"  with the z-case formula H_y = (Af - Bg)/eta: Faraday rel.res {rel(curl(E, r0, t0, 1e-6), -mu_*ddt(Hz_sign, r0, t0, 1e-6/v11)):.2f} (fails)")
cross_line(X, Z, "u(+x)", "z"); cross_line(-X, Z, "u(-x)", "z")
cross_line(Z, -Y, "E(z)", "H(-y)"); cross_line(Z, Y, "E(z)", "H(+y)")
# numbers for (d)
w11, b11 = 5 * np.pi * 1e8, 4 * np.pi
v11n = w11 / b11
er11 = (c / v11n) ** 2
eta11n = mu0 * v11n
print(f"(d) E = z 10 cos(5pi e8 t + 4pi x): toward -x, v = {v11n:.4e} m/s, eps_r = {er11:.4f} (c=3e8: {(3e8/v11n)**2:.4f}),"
      f" eta = mu0 v = {eta11n:.3f} Ohm = {eta11n/np.pi:.2f} pi; H amplitude 10/eta = {10/eta11n*1e3:.3f} mA/m;"
      f" B = 10/v = {10/v11n*1e9:.2f} nT")
E = lambda r, t: Z * 10 * np.cos(w11 * t + b11 * r[0])
H = lambda r, t: Y * 10 / eta11n * np.cos(w11 * t + b11 * r[0])
pts = [(rng.uniform(-1, 1, 3), rng.uniform(0, 1e-8)) for _ in range(6)]
ALL.append(maxwell("18.11(d) E = z 10cos(.), H = +y 63.7 mA/m cos(.)", E, H, mu0, er11 * eps0, pts, 1e-6, 1e-6 / v11n))
Ex_add = lambda r, t: X * 3 * np.cos(w11 * t + b11 * r[0])
r0, t0 = np.array([0.05, 0, 0]), 0.0
print(f"(e) adding E_x = 3cos(5pi e8 t + 4pi x): div E = {div(Ex_add, r0, t0, 1e-6):.4f} vs -12 pi sin(4pi x) = "
      f"{-12*np.pi*np.sin(b11*0.05):.4f}; amplitude 12 pi = {12*np.pi:.3f} V/m^2")

# =========================================================================================== 18.12
hdr("18.12 A wave on a slant: E = (6x - 8y) cos(7.5pi e8 t - 2.4pi x - 1.8pi y)")
w12 = 7.5 * np.pi * 1e8
k12 = np.array([2.4 * np.pi, 1.8 * np.pi, 0])
kmag = np.linalg.norm(k12)
u12 = k12 / kmag
v12 = w12 / kmag
er12 = (c / v12) ** 2
eta12 = mu0 * v12
E0v = np.array([6.0, -8.0, 0])
print(f"  |grad phase| = {kmag:.4f} rad/m = {kmag/np.pi:.4f} pi; u = {u12}; angle from x axis = {np.degrees(np.arctan2(u12[1], u12[0])):.2f} deg")
print(f"  velocity from phase: {vel(w12, -k12)} m/s;  v = {v12:.4e} m/s; eps_r = {er12:.4f} (c=3e8: {(3e8/v12)**2:.4f})")
print(f"  E0 . u = {E0v.dot(u12):.2e}; |E0| = {np.linalg.norm(E0v):.1f} V/m; eta = mu0 v = {eta12:.3f} Ohm = {eta12/np.pi:.2f} pi")
Hv = np.cross(u12, E0v) / eta12
print(f"  u x E0 = {np.round(np.cross(u12, E0v), 6)}  -> H0 = {np.round(Hv*1e3, 4)} mA/m ({dname(Hv)}), |H0| = {np.linalg.norm(Hv)*1e3:.3f} mA/m")
ExH = np.cross(E0v, Hv)
print(f"  E0 x H0 = {np.round(ExH, 6)} -> direction {dname(ExH)} (u = {u12})")
print(f"  pieces: 0.8x X (-8y) = {np.cross(0.8*X, -8*Y)}, 0.6y X 6x = {np.cross(0.6*Y, 6*X)}")
print(f"  pieces of E0 x (-z): 6x X (-z) = {np.cross(6*X, -Z)}, (-8y) X (-z) = {np.cross(-8*Y, -Z)}")
phi = lambda r, t: w12 * t - k12.dot(r)
E = lambda r, t: E0v * np.cos(phi(r, t))
H = lambda r, t: Hv * np.cos(phi(r, t))
pts = [(rng.uniform(-1, 1, 3), rng.uniform(0, 1e-8)) for _ in range(8)]
ALL.append(maxwell("18.12 (E, H)", E, H, mu0, er12 * eps0, pts, 1e-6, 1e-6 / v12))
r0, t0 = np.array([0.1, 0.05, 0]), 0.4e-9
sphi = np.sin(phi(r0, t0))
print(f"  curl E at a point = {np.round(curl(E, r0, t0, 1e-6), 4)}; -30 pi sin(phi) z = {np.round(-30*np.pi*sphi*Z, 4)};"
      f" 30 pi = {30*np.pi:.3f} V/m^2")
print(f"  -mu0 dH/dt = {np.round(-mu0*ddt(H, r0, t0, 1e-6/v12), 4)};  10 omega/v = {10*w12/v12:.4f} = 10*3pi")
print(f"  coefficients (multiples of pi): 6*2.4 = {6*2.4:.1f}, 8*1.8 = {8*1.8:.1f}, 8*2.4 = {8*2.4:.1f}, 6*1.8 = {6*1.8:.1f}; 19.2 + 10.8 = {8*2.4 + 6*1.8:.1f}")
print(f"  div E = {div(E, r0, t0, 1e-6):.2e}; terms 6*2.4pi = {6*2.4*np.pi:.4f}, -8*1.8pi = {-8*1.8*np.pi:.4f}")
cHv, eEv = curl(H, r0, t0, 1e-6) / sphi, er12 * eps0 * ddt(E, r0, t0, 1e-6 / v12) / sphi
print(f"  curl H / sin(phi) = {np.round(cHv, 5)}; eps dE/dt / sin(phi) = {np.round(eEv, 5)}; 3pi*10/eta = {3*np.pi*10/eta12:.4f}, 10 eps omega = {10*er12*eps0*w12:.4f}; direction {np.round(cHv/np.linalg.norm(cHv), 4)}")
print(f"  Ampere: eps omega/(1.8 pi) * 6 = H0 -> {er12*eps0*w12*6/(1.8*np.pi)*1e3:.4f} mA/m vs 10/eta = {10/eta12*1e3:.4f}")
E1v = np.array([8.0, 6.0, 0])
E1 = lambda r, t: E1v * np.cos(phi(r, t))
print(f"(e) E' = (8x + 6y)cos: E'.u = {E1v.dot(u12):.2f}; div E' = {div(E1, r0, t0, 1e-6):.4f} vs 30 pi sin(phi) = {30*np.pi*sphi:.4f}")
E2v = np.array([0, 0, 10.0])
H2v = np.cross(u12, E2v) / eta12
print(f"    E'' = 10 z cos: H'' = u x E''/eta = {np.round(H2v*1e3, 3)} mA/m = (0.6x - 0.8y) {10/eta12*1e3:.3f} mA/m")
print(f"    u x z = {np.round(np.cross(u12, Z), 4)}; E'' x H'' -> {dname(np.cross(E2v, H2v))}")
E = lambda r, t: E2v * np.cos(phi(r, t))
H = lambda r, t: H2v * np.cos(phi(r, t))
ALL.append(maxwell("18.12(e) z-polarized partner", E, H, mu0, er12 * eps0, pts, 1e-6, 1e-6 / v12))

hdr("SUMMARY")
print(f"constants: c = {c:.6e} m/s, eta0 = {eta0:.4f} Ohm, 120 pi = {120*np.pi:.4f} Ohm")
print(f"Maxwell/wave-equation checks passed: {sum(ALL)}/{len(ALL)}")
