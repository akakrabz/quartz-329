#!/usr/bin/env python3
"""Verification of every number, sign and direction on the Lecture 20 pages of the ECE 329 study site.

Pages checked:
  content-src/3-maxwell-and-waves/20-poynting-theorem-and-monochromatic-waves.md
  content-src/concepts/poynting-theorem.md, content-src/concepts/poynting-vector.md (new sections)
  content-src/problems/energy-bookkeeping-for-a-radiating-sheet.md
  figs_l20.py (arrow directions; screen frame X right, Y up, Z out of the screen)
numpy only. Derivatives by central finite differences, time averages by quadrature over whole periods,
every vector direction by an explicit np.cross. Run: python3 verify_L20.py > verify_L20.out
"""
import numpy as np

mu0 = 1.25663706212e-6
eps0 = 8.8541878128e-12
c = 1 / np.sqrt(mu0 * eps0)
eta0 = np.sqrt(mu0 / eps0)
# the course's exam constants (SP17-SP19 print them): self-consistent, c = 3e8 and eta0 = 120 pi exactly
eps0x = 1e-9 / (36 * np.pi)
mu0x = 4 * np.pi * 1e-7
X, Y, Z = np.eye(3)
cr = np.cross
ok_count = 0

def ok(cond, msg):
    global ok_count
    assert cond, "FAILED: " + msg
    ok_count += 1
    print("ok  ", msg)

def close(a, b, msg, rtol=1e-6, atol=1e-12):
    ok(np.allclose(a, b, rtol=rtol, atol=atol), f"{msg}: {np.round(a, 6)} vs {np.round(b, 6)}")

def tavg(f, T, n=20000):
    """time average of f(t) over one period T (midpoint rule, exact for trig polynomials)"""
    t = (np.arange(n) + 0.5) * T / n
    return np.mean(f(t))

print("=== A. constants")
close(c, 2.99792458e8, "c")
close(eta0, 376.730313, "eta0 [ohm]")
close(120 * np.pi, 376.991118, "120 pi")
close((120 * np.pi - eta0) / eta0, 6.92e-4, "120 pi is 0.069 % high", rtol=1e-2)
close(1 / np.sqrt(mu0x * eps0x), 3e8, "exam constants: c = 3e8 exactly")
close(np.sqrt(mu0x / eps0x), 120 * np.pi, "exam constants: eta0 = 120 pi exactly")
close([60 * np.pi, eta0 / 2], [188.4956, 188.3652], "60 pi vs eta0/2 (W/m^2 per side in the notes' example)", rtol=1e-6)

print("=== B. Poynting's theorem holds identically for any fields obeying Faraday + Ampere-Maxwell (finite differences)")
# Build fields from arbitrary potentials so that Faraday's law holds automatically:
#   B = curl A, E = -grad V - dA/dt; H = B/mu; then DEFINE J = curl H - eps dE/dt (Ampere-Maxwell).
# Poynting's theorem must then hold at every point: dw/dt + div(E x H) + J.E = 0, with w = eps E.E/2 + mu H.H/2.
eps_, mu_ = 2.3, 0.7          # any constants (linear, time-invariant medium)
def A_(r, t):
    x, y, z = r
    return np.array([np.sin(1.1 * y + 0.4 * t) * np.cos(0.7 * z),
                     np.cos(0.9 * x - 0.6 * t) + 0.3 * z * np.sin(t),
                     np.exp(-0.2 * x * x) * np.sin(0.8 * y - 0.5 * t) + 0.1 * x * y])
def V_(r, t):
    x, y, z = r
    return np.sin(0.5 * x + 0.3 * y - 0.9 * t) * np.cos(0.4 * z) + 0.2 * x * z * np.cos(0.3 * t)
h = 1e-4
def d_dt(F, r, t):
    return (F(r, t + h) - F(r, t - h)) / (2 * h)
def grad(f, r, t):
    return np.array([(f(r + h * e, t) - f(r - h * e, t)) / (2 * h) for e in np.eye(3)])
def jac(F, r, t):            # J[i, j] = dF_i/dx_j
    return np.array([(F(r + h * e, t) - F(r - h * e, t)) / (2 * h) for e in np.eye(3)]).T
def curl(F, r, t):
    Jm = jac(F, r, t)
    return np.array([Jm[2, 1] - Jm[1, 2], Jm[0, 2] - Jm[2, 0], Jm[1, 0] - Jm[0, 1]])
def div(F, r, t):
    return np.trace(jac(F, r, t))
E_ = lambda r, t: -grad(V_, r, t) - d_dt(A_, r, t)
B_ = lambda r, t: curl(A_, r, t)
H_ = lambda r, t: B_(r, t) / mu_
Jv = lambda r, t: curl(H_, r, t) - eps_ * d_dt(E_, r, t)
w_ = lambda r, t: 0.5 * eps_ * E_(r, t) @ E_(r, t) + 0.5 * mu_ * H_(r, t) @ H_(r, t)
S_ = lambda r, t: cr(E_(r, t), H_(r, t))
rng = np.random.default_rng(20)
h = 2e-3   # outer step for the second-level derivatives (inner ones reuse the same h; error O(h^2))
for k in range(4):
    r0 = rng.uniform(-1.5, 1.5, 3); t0 = rng.uniform(0, 3)
    dwdt = (w_(r0, t0 + h) - w_(r0, t0 - h)) / (2 * h)
    divS = sum((S_(r0 + h * e, t0) - S_(r0 - h * e, t0))[i] / (2 * h) for i, e in enumerate(np.eye(3)))
    JE = Jv(r0, t0) @ E_(r0, t0)
    scale = abs(dwdt) + abs(divS) + abs(JE)
    ok(abs(dwdt + divS + JE) < 2e-4 * scale, f"point {k}: dw/dt = {dwdt:+.5f}, div S = {divS:+.5f}, J.E = {JE:+.5f}, sum = {dwdt + divS + JE:+.1e}")
    # the identity div(E x H) = H.curl E - E.curl H on its own
    idt = H_(r0, t0) @ curl(E_, r0, t0) - E_(r0, t0) @ curl(H_, r0, t0)
    ok(abs(divS - idt) < 2e-4 * (abs(divS) + abs(idt)), f"point {k}: div(E x H) = H.curl E - E.curl H ({divS:+.5f} vs {idt:+.5f})")
h = 1e-4

print("=== C. 1D (Rao) route: E = x Ex(z,t), H = y Hy(z,t), J = x Jx: d(ExHy)/dz = -d/dt(eps Ex^2/2 + mu Hy^2/2) - Jx Ex")
# pick Ex, Hy arbitrary, define Faraday-consistent pair: choose Hy then Ex from dEx/dz = -mu dHy/dt by construction
Hy1 = lambda z, t: np.sin(2 * z - 3 * t) + 0.4 * np.cos(z + t)
Ex1 = lambda z, t: mu_ * (1.5 * np.sin(2 * z - 3 * t) - 0.4 * np.cos(z + t))   # dEx/dz = -mu dHy/dt
z0, t0 = 0.37, 0.81
dEx_dz = (Ex1(z0 + h, t0) - Ex1(z0 - h, t0)) / (2 * h); dHy_dt = (Hy1(z0, t0 + h) - Hy1(z0, t0 - h)) / (2 * h)
close(dEx_dz, -mu_ * dHy_dt, "constructed pair obeys Faraday's y-component", rtol=1e-6)
Jx1 = -(Hy1(z0 + h, t0) - Hy1(z0 - h, t0)) / (2 * h) - eps_ * (Ex1(z0, t0 + h) - Ex1(z0, t0 - h)) / (2 * h)   # Ampere x-comp
dS = (Ex1(z0 + h, t0) * Hy1(z0 + h, t0) - Ex1(z0 - h, t0) * Hy1(z0 - h, t0)) / (2 * h)
wz = lambda t: 0.5 * eps_ * Ex1(z0, t) ** 2 + 0.5 * mu_ * Hy1(z0, t) ** 2
dw = (wz(t0 + h) - wz(t0 - h)) / (2 * h)
close(dS, -dw - Jx1 * Ex1(z0, t0), "1D Poynting theorem", rtol=1e-6)

print("=== D. J.E is the power the field delivers to moving charges; units")
q, u = 1.6e-19, np.array([3e5, -2e5, 1e5]); Ev = np.array([10., 0, 4]); Bv = np.array([0.1, 0.3, -0.2])
F = q * (Ev + cr(u, Bv))
close(F @ u, q * Ev @ u, "F.u = qE.u: the magnetic force does no work ((u x B).u = 0)")
# dimensions as exponents of (kg, m, s, A)
D = lambda kg=0, m=0, s=0, A=0: np.array([kg, m, s, A], float)
Vd, Ad, Wd, Jd = D(1, 2, -3, -1), D(0, 0, 0, 1), D(1, 2, -3), D(1, 2, -2)
Fd, Hd = D(-1, -2, 4, 2), D(1, 2, -2, -2)          # farad, henry
per = lambda n: D(m=-n)
close((Fd + per(1)) + 2 * (Vd + per(1)), Jd + per(3), "eps E^2: (F/m)(V/m)^2 = J/m^3")
close((Hd + per(1)) + 2 * (Ad + per(1)), Jd + per(3), "mu H^2: (H/m)(A/m)^2 = J/m^3")
close((Vd + per(1)) + (Ad + per(1)), Wd + per(2), "E x H: (V/m)(A/m) = W/m^2")
close((Ad + per(2)) + (Vd + per(1)), Wd + per(3), "J.E: (A/m^2)(V/m) = W/m^3")
close((Ad + per(1)) + (Vd + per(1)), Wd + per(2), "Js.E: (A/m)(V/m) = W/m^2 (per unit area of sheet)")
close(Jd + per(3) - D(s=1), Wd + per(3), "dw/dt: (J/m^3)/s = W/m^3")

print("=== E. Notes' Example 1: Js = x 2 cos(wt) A/m on z = 0, vacuum")
for eta, lab in ((eta0, "eta0"), (120 * np.pi, "120 pi")):
    J0 = 2.0; om = 2 * np.pi * 1e6; beta = om / c; T = 2 * np.pi / om
    Js = lambda t: X * J0 * np.cos(om * t)
    def E1(z, t):  return -(eta / 2) * Js(t - abs(z) / c)                         # recipe -(eta/2) Js(t - d/v)
    def H1(z, t):  return 0.5 * cr(Js(t - abs(z) / c), Z if z > 0 else -Z)       # recipe 1/2 Js x n
    for z, t in ((40.0, 0.3e-6), (-75.0, 0.71e-6)):
        sg = 1 if z > 0 else -1
        close(E1(z, t), -X * eta * np.cos(om * t - sg * beta * z), f"[{lab}] E = -x eta cos(wt -+ bz) at z = {z}")
        close(H1(z, t), -sg * Y * np.cos(om * t - sg * beta * z), f"[{lab}] H = -+y cos(wt -+ bz) at z = {z}")
        close(cr(E1(z, t), H1(z, t)), sg * Z * eta * np.cos(om * t - sg * beta * z) ** 2, f"[{lab}] S = +-z eta cos^2 at z = {z}")
    # Maxwell in each region (finite differences of the scalar components)
    for z0 in (37.0, -52.0):
        t0 = 0.413e-6; dz = 1e-3; dt = dz / c
        Ex = lambda z, t: E1(z, t)[0]; Hy = lambda z, t: H1(z, t)[1]
        f1 = (Ex(z0 + dz, t0) - Ex(z0 - dz, t0)) / (2 * dz); f2 = -mu0 * (Hy(z0, t0 + dt) - Hy(z0, t0 - dt)) / (2 * dt)
        a1 = -(Hy(z0 + dz, t0) - Hy(z0 - dz, t0)) / (2 * dz); a2 = eps0 * (Ex(z0, t0 + dt) - Ex(z0, t0 - dt)) / (2 * dt)
        if lab == "eta0":
            close(f1, f2, f"Faraday dEx/dz = -mu0 dHy/dt at z = {z0}", rtol=1e-5)
            close(a1, a2, f"Ampere -dHy/dz = eps0 dEx/dt at z = {z0}", rtol=1e-5)
    # jumps at the sheet
    t0 = 0.123e-6
    close(cr(Z, H1(1e-9, t0) - H1(-1e-9, t0)), Js(t0), f"[{lab}] z x (H+ - H-) = Js", rtol=1e-6, atol=1e-6)
    close(E1(1e-9, t0), E1(-1e-9, t0), f"[{lab}] E continuous at the sheet", rtol=1e-6)
    JE = lambda t: Js(t) @ E1(0.0, t)
    close(JE(t0), -2 * eta * np.cos(om * t0) ** 2, f"[{lab}] Js.E = -2 eta cos^2(wt)")
    # instantaneous pillbox balance: z.(S(0+) - S(0-)) = -Js.E
    for t in np.linspace(0, T, 7):
        Sp = cr(E1(1e-12, t), H1(1e-12, t)); Sm = cr(E1(-1e-12, t), H1(-1e-12, t))
        close(Z @ (Sp - Sm), -JE(t), f"[{lab}] pillbox, t = {t*1e6:.3f} us: z.(S+ - S-) = -Js.E = {-JE(t):.2f}", rtol=1e-6, atol=1e-6)
    # time averages by quadrature
    Sav_p = tavg(lambda t: np.array([cr(E1(0.3 * c * T, tt), H1(0.3 * c * T, tt))[2] for tt in t]), T, 4000)
    Sav_m = tavg(lambda t: np.array([cr(E1(-1.7 * c * T, tt), H1(-1.7 * c * T, tt))[2] for tt in t]), T, 4000)
    inj = tavg(lambda t: np.array([-JE(tt) for tt in t]), T, 4000)
    close([Sav_p, Sav_m, inj], [eta / 2, -eta / 2, eta], f"[{lab}] <S_z> = +eta/2 (z>0), -eta/2 (z<0); <-Js.E> = eta", rtol=1e-6)
    close(abs(Sav_p) + abs(Sav_m), inj, f"[{lab}] energy balance: |<S+>| + |<S->| = <-Js.E> = {inj:.2f} W/m^2", rtol=1e-6)
close(eta0 / 4, 94.18, "L19 cross-check: peak S per side for Js0 = 1 A/m is eta0/4 = 94.2 W/m^2", rtol=1e-3)
# slab |z| < d around the sheet: dW/dt = (injected) - (out through the two faces); averages to zero
om = 2 * np.pi * 1e6; beta = om / c; T = 2 * np.pi / om; eta = eta0
for bd in (np.pi / 2, 1.0, 2.7):
    d = bd / beta
    zz = (np.arange(20000) + 0.5) / 20000 * d
    Wslab = lambda t: 2 * np.mean(eps0 * (eta * np.cos(om * t - beta * zz)) ** 2) * d     # w = eps0 E^2 (w_e = w_m), both sides
    for t in (0.1 * T, 0.37 * T, 0.8 * T):
        dt = T * 1e-6
        dWdt = (Wslab(t + dt) - Wslab(t - dt)) / (2 * dt)
        rhs = 2 * eta * np.cos(om * t) ** 2 - 2 * eta * np.cos(om * t - bd) ** 2
        close(dWdt, rhs, f"slab beta d = {bd:.3f}, t = {t/T:.2f} T: dW/dt = 2 eta [cos^2 wt - cos^2(wt - beta d)]", rtol=1e-5, atol=1e-6)
    close(tavg(lambda t: 2 * eta * np.cos(om * t) ** 2 - 2 * eta * np.cos(om * t - bd) ** 2, T), 0.0, f"slab beta d = {bd:.3f}: <dW/dt> = 0", atol=1e-9)
t = 0.13 * T
close(2 * eta * np.cos(om * t) ** 2 - 2 * eta * np.sin(om * t) ** 2, 2 * eta * np.cos(2 * om * t), "beta d = pi/2 (quarter wavelength): dW/dt = 2 eta cos(2 wt)")

print("=== F. General amplitude J0, energy density, energy speed")
for J0 in (1.0, 2.0, 3.0):
    om = 1.0; T = 2 * np.pi
    S_peak = eta0 * J0 ** 2 / 4
    close(tavg(lambda t: S_peak * np.cos(om * t) ** 2, T), eta0 * J0 ** 2 / 8, f"J0 = {J0}: <S> per side = eta J0^2/8")
    close(tavg(lambda t: (eta0 / 2) * J0 ** 2 * np.cos(om * t) ** 2, T), eta0 * J0 ** 2 / 4, f"J0 = {J0}: <-Js.E> = eta J0^2/4")
for epsr, mur in ((1, 1), (2.25, 1), (4, 3)):
    eps, mu = epsr * eps0, mur * mu0; v, eta = 1 / np.sqrt(mu * eps), np.sqrt(mu / eps)
    E0 = 7.0; H0 = E0 / eta
    close(0.5 * eps * E0 ** 2, 0.5 * mu * H0 ** 2, f"single wave (epsr={epsr}, mur={mur}): w_e = w_m")
    close(E0 * H0, v * (0.5 * eps * E0 ** 2 + 0.5 * mu * H0 ** 2), "S = v w for a single plane wave")
    close(eps * eta ** 2 * v, eta, "eps eta^2 v = eta (used in the stored-energy integral)")
close(eta0 / (2 * c), 6.283e-7, "notes' example: <w> = eta0/(2c) = 6.28e-7 J/m^3", rtol=1e-3)
close(0.5 * eps0 * eta0 ** 2, eta0 / (2 * c), "<w> = eps0 E0^2/2 with E0 = eta0 (J0 = 2 A/m)")
close(eta0 / 2 / (eta0 / (2 * c)), c, "<S>/<w> = c")

print("=== G. time averages")
T = 2 * np.pi
for ph in (0.0, 0.4, 1.3, -2.2):
    close(tavg(lambda t: np.cos(t + ph) ** 2, T), 0.5, f"<cos^2(wt + {ph})> = 1/2")
    close(tavg(lambda t: np.cos(t + ph) ** 2, T / 2), 0.5, f"... also over half a period (cos^2 has period T/2)")
    close(tavg(lambda t: np.cos(t + ph), T), 0.0, f"<cos(wt + {ph})> = 0", atol=1e-12)
close(tavg(lambda t: np.sin(t) * np.cos(t), T), 0.0, "<sin cos> = 0", atol=1e-12)
for p1, p2 in ((0.3, 1.1), (0.0, np.pi / 4), (0.0, np.pi / 2), (1.0, 1.0)):
    close(tavg(lambda t: np.cos(t + p1) * np.cos(t + p2), T), 0.5 * np.cos(p1 - p2), f"<cos(wt+{p1:.3f}) cos(wt+{p2:.3f})> = cos(diff)/2")
# the same average in phasor form (Lecture 21's rule), for the record: <A cos(wt+p1) B cos(wt+p2)> = 1/2 Re{A e^{jp1} (B e^{jp2})*}
for A_, B_, p1, p2 in ((2.0, 3.0, 0.3, 1.1), (1.0, 5.0, -0.7, 2.0)):
    close(tavg(lambda t: A_ * np.cos(t + p1) * B_ * np.cos(t + p2), T), 0.5 * np.real(A_ * np.exp(1j * p1) * np.conj(B_ * np.exp(1j * p2))),
          f"<A cos B cos> = 1/2 Re(A B*) for phases {p1}, {p2}")
# the time average of the derivative of any periodic quantity is zero
wper = lambda t: 3 + np.cos(2 * t) ** 2 + 0.3 * np.sin(4 * t + 1)
close(tavg(lambda t: (wper(t + 1e-6) - wper(t - 1e-6)) / 2e-6, T), 0.0, "<dw/dt> = 0 for periodic w", atol=1e-8)
# cos^2 = 1/2 + 1/2 cos 2x
tt = np.linspace(0, 7, 50)
close(np.max(np.abs(np.cos(tt) ** 2 - 0.5 - 0.5 * np.cos(2 * tt))), 0.0, "cos^2 x = 1/2 (1 + cos 2x) (max deviation on 50 points)", atol=1e-15)

print("=== H. Two equal waves in opposite directions (standing wave): instantaneous S != 0, <S> = 0")
eta = eta0; E0 = 1.0; om = 2 * np.pi; beta = 2 * np.pi; T = 1.0; lam = 1.0; v = om / beta
Ex2 = lambda z, t: E0 * np.cos(om * t - beta * z) - E0 * np.cos(om * t + beta * z)
Hy2 = lambda z, t: (E0 / eta) * np.cos(om * t - beta * z) + (E0 / eta) * np.cos(om * t + beta * z)
for z, t in ((0.13, 0.31), (0.41, 0.77)):
    close(Ex2(z, t), 2 * E0 * np.sin(om * t) * np.sin(beta * z), f"E = 2E0 sin(wt) sin(bz) at ({z},{t})")
    close(Hy2(z, t), 2 * E0 / eta * np.cos(om * t) * np.cos(beta * z), f"H = (2E0/eta) cos(wt) cos(bz) at ({z},{t})")
    close(Ex2(z, t) * Hy2(z, t), E0 ** 2 / eta * np.sin(2 * om * t) * np.sin(2 * beta * z), "S_z = (E0^2/eta) sin(2wt) sin(2bz)")
    close(Ex2(z, t) * Hy2(z, t), (E0 ** 2 / eta) * (np.cos(om * t - beta * z) ** 2 - np.cos(om * t + beta * z) ** 2),
          "S_z = (|E1|^2 - |E2|^2)/eta: cross terms cancel (as on the poynting-vector page)")
for z in np.linspace(0, 1, 9):
    close(tavg(lambda t: Ex2(z, t) * Hy2(z, t), T), 0.0, f"<S_z> = 0 at z = {z:.3f} lambda", atol=1e-12)
epsv = 1 / (eta * v)   # eps such that eta = sqrt(mu/eps), v = 1/sqrt(mu eps) with mu = eta/v
muv = eta / v
w2 = lambda z, t: 0.5 * epsv * Ex2(z, t) ** 2 + 0.5 * muv * Hy2(z, t) ** 2
for z in (0.0, 0.1, 0.25, 0.37):
    close(tavg(lambda t: w2(z, t), T), epsv * E0 ** 2, f"<w> = eps E0^2 (uniform) at z = {z}")
close(w2(0.0, 0.25), 0.0, "w = 0 at an E-node (z = 0) when wt = pi/2 (H is zero there then)", atol=1e-20)
zz = (np.arange(4000) + 0.5) / 4000 * 0.5
for t in (0.0, 0.1, 0.25, 0.4):
    close(np.mean(w2(zz, t)) * 0.5, epsv * E0 ** 2 * lam / 2, f"energy in half a wavelength is constant (t = {t})")

print("=== I. J.E in a conductor (exam style, new numbers): sea water sigma = 4 S/m, E = 0.5 cos(wt) V/m")
sig, E0 = 4.0, 0.5
close(sig * E0 ** 2, 1.0, "peak J.E = sigma E0^2 = 1 W/m^3")
close(tavg(lambda t: sig * (E0 * np.cos(t)) ** 2, 2 * np.pi), 0.5, "<J.E> = 0.5 W/m^3")
close(0.5 * 1e-3, 5e-4, "one litre: 0.5 mW average")
close(81 * eps0 / 4, 1.79e-10, "relaxation time of sea water eps/sigma = 0.18 ns (eps_r = 81)", rtol=1e-2)

print("=== J. Leaky capacitor discharging (Lecture 10): S = 0, dw/dt = -J.E")
epsr, sig, E0 = 4.0, 1e-5, 1e4
eps = epsr * eps0; tau = eps / sig
Ec = lambda t: E0 * np.exp(-t / tau)
close(tau, 3.5417e-6, "tau = eps/sigma = 3.54 us", rtol=1e-4)
for t in (0.0, 1e-6, 5e-6):
    dEdt = (Ec(t + 1e-12) - Ec(t - 1e-12)) / 2e-12
    close(sig * Ec(t) + eps * dEdt, 0.0, f"t = {t*1e6} us: conduction + displacement current density = 0 (so H = 0)", atol=1e-6)
    wv = lambda tt: 0.5 * eps * Ec(tt) ** 2
    dwdt = (wv(t + 1e-12) - wv(t - 1e-12)) / 2e-12
    close(dwdt, -sig * Ec(t) ** 2, f"t = {t*1e6} us: dw/dt = -sigma E^2 = {-sig*Ec(t)**2:.2f} W/m^3", rtol=1e-5)
close(0.5 * eps * E0 ** 2, 1.7708e-3, "w(0) = 1.77e-3 J/m^3", rtol=1e-4)
close(sig * E0 ** 2, 1000.0, "J.E(0) = 1000 W/m^3")
close(tau / 2 * np.log(2), 1.2274e-6, "energy halves in (tau/2) ln 2 = 1.23 us", rtol=1e-3)
close(tau * np.log(2), 2.455e-6, "charge (and E) halves in tau ln 2 = 2.45 us: the energy halves twice as fast", rtol=1e-3)
close(2 * (0.5 * eps * E0 ** 2) / tau, sig * E0 ** 2, "-dw/dt(0) = 2 w(0)/tau = sigma E0^2")
close(0.5 * eps * E0 ** 2 * np.exp(-2 * 1e-6 / tau), 0.5 * eps * Ec(1e-6) ** 2, "w decays as exp(-2t/tau)")

print("=== K. Resistive wire: power enters through the surface, total I^2 R (nichrome, rho = 1.10e-6 ohm m)")
rho_e = 1.10e-6; sig = 1 / rho_e; a = 0.25e-3; ell = 2.0; I = 3.0
R = ell / (sig * np.pi * a ** 2); P = I ** 2 * R
Ez = I / (sig * np.pi * a ** 2); Hs = I / (2 * np.pi * a)
close(sig, 9.09e5, "sigma = 9.09e5 S/m", rtol=1e-3)
close(R, 11.20, "R = 11.2 ohm", rtol=1e-3)
close(P, 100.8, "P = I^2 R = 101 W", rtol=1e-3)
close(Ez, 16.81, "E = J/sigma = 16.8 V/m", rtol=1e-3)
close(Hs, 1909.9, "H(a) = I/(2 pi a) = 1.91 kA/m", rtol=1e-4)
close(Ez * Hs, 3.209e4, "|S| at the surface = 32.1 kW/m^2", rtol=1e-3)
close(Ez * Hs * 2 * np.pi * a * ell, P, "|S| x side area 2 pi a l = I^2 R")
close(Ez * ell, I * R, "E l = I R (voltage along the wire)")
close(Ez * Hs / 1361, 23.6, "about 24 times the solar flux", rtol=1e-2)
# direction: wire along +z, current +z. Field point at angle phi on the surface.
for phi in (0.0, 1.0, 2.5, 4.0):
    rhat = np.array([np.cos(phi), np.sin(phi), 0]); phat = cr(Z, rhat)
    Ev = Ez * Z; Hv = Hs * phat
    close(cr(Ev, Hv), -Ez * Hs * rhat, f"phi = {phi}: S = E x H = -(EH) rho_hat (inward)")
    ok(abs(cr(Ev, Hv) @ Z) < 1e-9, f"phi = {phi}: no S along the wire inside it (nothing through the end faces)")
# inside: S_rho = -E H_phi(rho) with H_phi = I rho /(2 pi a^2); div S = -J.E (finite differences, Cartesian)
def Sw(r):
    x, y = r[0], r[1]; rr = np.hypot(x, y); ph = np.array([-y, x, 0]) / rr
    return cr(Ez * Z, I * rr / (2 * np.pi * a ** 2) * ph)
r0 = np.array([0.6 * a, 0.3 * a, 0.0]); hh = 1e-8
divS = sum((Sw(r0 + hh * e) - Sw(r0 - hh * e))[i] / (2 * hh) for i, e in enumerate(np.eye(3)))
close(divS, -sig * Ez ** 2, "inside: div S = -J.E = -sigma E^2 (steady state)", rtol=1e-5)
for frac in (0.25, 0.5, 1.0):
    rr = frac * a
    close(Ez * I * rr / (2 * np.pi * a ** 2) * 2 * np.pi * rr * ell, P * frac ** 2, f"power still flowing in at rho = {frac} a: P (rho/a)^2")
# coax: S = z VI/(2 pi rho^2 ln(b/a)) integrates to VI
aa, bb, Vc, Ic = 1e-3, 3.5e-3, 10.0, 0.2
rr = np.linspace(aa, bb, 200001)
Sz = Vc * Ic / (2 * np.pi * rr ** 2 * np.log(bb / aa))
close(np.trapezoid(Sz * 2 * np.pi * rr, rr), Vc * Ic, "coax: integral of S over the annulus = VI = 2 W", rtol=1e-6)
Er = Vc / (rr[1000] * np.log(bb / aa)); Hp = Ic / (2 * np.pi * rr[1000])
close(cr(Er * X, Hp * Y), Sz[1000] * Z, "coax: rho_hat x phi_hat = z (E outward from the + inner conductor, H by the right-hand rule)")
# battery: J from - to + inside, E (from the terminal charges) from + to -
ok(np.dot(Z * 1.0, -Z * 1.0) < 0, "battery: J along +z (- to +) and E along -z: J.E < 0, a source")

print("=== L. Integral form with a sphere: isotropic radiator, and sunlight")
Prad, r = 50e3, 10e3
Sav = Prad / (4 * np.pi * r ** 2)
close(Sav, 3.979e-5, "50 kW at 10 km: <S> = 3.98e-5 W/m^2", rtol=1e-3)
close(np.sqrt(2 * eta0 * Sav), 0.17318, "E0 = sqrt(2 eta0 <S>) = 0.173 V/m", rtol=1e-3)
close(np.sqrt(60 * Prad) / r, np.sqrt(2 * 120 * np.pi * Sav), "E0 = sqrt(60 P)/r with eta0 = 120 pi")
E0r = np.sqrt(2 * eta0 * Sav)
close(tavg(lambda t: (E0r * np.cos(t)) ** 2 / eta0, 2 * np.pi), Sav, "<S> = E0^2/(2 eta0) by quadrature", rtol=1e-9)
Ssun = 1361.0
close(np.sqrt(2 * eta0 * Ssun), 1012.6, "sunlight 1361 W/m^2: E0 = 1.01 kV/m", rtol=1e-3)
close(np.sqrt(eta0 * Ssun), 716.0, "E_rms = sqrt(eta0 S) = 716 V/m", rtol=1e-3)
close(np.sqrt(2 * eta0 * Ssun) / eta0, 2.688, "H0 = 2.69 A/m", rtol=1e-3)
close(Ssun / c, 4.54e-6, "<w> = S/c = 4.54 uJ/m^3", rtol=1e-3)
close(np.sqrt(2 * eta0 * Ssun) / eta0 / np.sqrt(2), 1.90, "H_rms = 1.90 A/m", rtol=1e-2)

print("=== M. Orthogonal components: powers add (any relative phase)")
E1, E2 = 3.0, 4.0
for ph in (0.0, np.pi / 2, 1.0, np.pi):
    def Svec(t, z=0.2):
        Ev = X * E1 * np.cos(t - z) + Y * E2 * np.cos(t - z + ph)
        Hv = cr(Z, Ev) / eta0
        return cr(Ev, Hv)
    Szav = tavg(lambda t: np.array([Svec(tt)[2] for tt in t]), 2 * np.pi, 4000)
    close(Szav, (E1 ** 2 + E2 ** 2) / (2 * eta0), f"phi = {ph:.3f}: <S_z> = (E1^2 + E2^2)/(2 eta0)")
    ok(abs(tavg(lambda t: np.array([Svec(tt)[0] for tt in t]), 2 * np.pi, 400)) < 1e-12, "no transverse S")
    for tt_ in (0.3, 1.7):     # instantaneous: S_z = (Ex^2 + Ey^2)/eta, no cross term
        Ev = X * E1 * np.cos(tt_ - 0.2) + Y * E2 * np.cos(tt_ - 0.2 + ph)
        close(Svec(tt_)[2], (Ev @ Ev) / eta0, f"phi = {ph:.3f}, t = {tt_}: S_z = (Ex^2 + Ey^2)/eta instantaneously")
close((E1 ** 2 + E2 ** 2) / (2 * eta0), 0.03318, "E1 = 3, E2 = 4 V/m in vacuum: <S> = 33 mW/m^2", rtol=1e-3)

print("=== N. Worked problem: Js = -z J0 u(t) cos(wt) on x = 0, eps_r = 2.25, f = 2 MHz, J0 = 3 A/m (exam constants)")
epsr = 2.25; eps = epsr * eps0x; mu = mu0x
v = 1 / np.sqrt(mu * eps); eta = np.sqrt(mu / eps)
f = 2e6; om = 2 * np.pi * f; T = 1 / f; beta = om / v; lam = v / f; J0 = 3.0
close([v / 1e8, eta, lam, beta, T * 1e6], [2.0, 80 * np.pi, 100.0, 0.02 * np.pi, 0.5], "v = 2e8 m/s, eta = 80 pi, lambda = 100 m, beta = 0.02 pi rad/m, T = 0.5 us")
close(eta, 251.327, "eta = 251 ohm", rtol=1e-5)
u = lambda s: np.where(s > 0, 1.0, 0.0)
Jsc = lambda t: J0 * u(t) * np.cos(om * t)          # scalar; Js = -z Jsc
Jsv = lambda t: -Z * Jsc(t)
def Ep(x, t): return -(eta / 2) * Jsv(t - abs(x) / v)
def Hp(x, t): return 0.5 * cr(Jsv(t - abs(x) / v), X if x > 0 else -X)
for x, t in ((130.0, 1.3e-6), (-245.0, 2.2e-6), (599.0, 3e-6)):
    sg = 1 if x > 0 else -1; ph = om * t - beta * abs(x)
    close(Ep(x, t), Z * (eta * J0 / 2) * np.cos(ph), f"E = +z (eta J0/2) cos(wt - b|x|) at x = {x}")
    close(Hp(x, t), -sg * Y * (J0 / 2) * np.cos(ph), f"H = -+y (J0/2) cos(wt -+ bx) at x = {x}")
    close(cr(Ep(x, t), Hp(x, t)), sg * X * (eta * J0 ** 2 / 4) * np.cos(ph) ** 2, f"S = +-x (eta J0^2/4) cos^2 at x = {x}: away from the sheet")
close(eta * J0 / 2, 120 * np.pi, "E amplitude eta J0/2 = 120 pi = 377 V/m")
ok(np.allclose(Ep(700.0, 3e-6), 0) and np.allclose(Hp(-601.0, 3e-6), 0), "nothing beyond the front |x| = v t = 600 m at 3 us")
# Maxwell (3D finite differences) in both regions, using vector fields of (x, t)
def curlx(F, x, t, dx=1e-3):           # field depends on x only
    dF = (F(x + dx, t) - F(x - dx, t)) / (2 * dx)
    return np.array([0.0, -dF[2], dF[1]])
for x0 in (123.4, -311.1):
    t0 = 2.71e-6; dt = 1e-12
    close(curlx(Ep, x0, t0), -mu * (Hp(x0, t0 + dt) - Hp(x0, t0 - dt)) / (2 * dt), f"Faraday at x = {x0}", rtol=1e-4, atol=1e-6)
    close(curlx(Hp, x0, t0), eps * (Ep(x0, t0 + dt) - Ep(x0, t0 - dt)) / (2 * dt), f"Ampere-Maxwell at x = {x0}", rtol=1e-4, atol=1e-9)
t0 = 1.234e-6
close(cr(X, Hp(1e-9, t0) - Hp(-1e-9, t0)), Jsv(t0), "x x (H+ - H-) = Js at the sheet", rtol=1e-6, atol=1e-9)
JEp = lambda t: Jsv(t) @ Ep(0.0, t)
close(JEp(t0), -(eta * J0 ** 2 / 2) * np.cos(om * t0) ** 2, "Js.E = -(eta J0^2/2) cos^2(wt) for t > 0")
JEav = tavg(lambda t: np.array([JEp(1e-6 + tt) for tt in t]), T, 4000)
close(JEav, -180 * np.pi, "<Js.E> = -eta J0^2/4 = -180 pi W/m^2", rtol=1e-6)
close(-JEav, 565.487, "= -565 W/m^2", rtol=1e-5)
Sxav = tavg(lambda t: np.array([cr(Ep(250.0, 2e-6 + tt), Hp(250.0, 2e-6 + tt))[0] for tt in t]), T, 4000)
Sxav_m = tavg(lambda t: np.array([cr(Ep(-250.0, 2e-6 + tt), Hp(-250.0, 2e-6 + tt))[0] for tt in t]), T, 4000)
close([Sxav, Sxav_m], [90 * np.pi, -90 * np.pi], "<S> = +-x 90 pi W/m^2 behind the front", rtol=1e-6)
close(90 * np.pi, 282.743, "90 pi = 283 W/m^2", rtol=1e-5)
for t in np.linspace(0.05e-6, 0.45e-6, 5):
    Sp = cr(Ep(1e-9, t), Hp(1e-9, t)); Sm = cr(Ep(-1e-9, t), Hp(-1e-9, t))
    close(X @ (Sp - Sm), -JEp(t), f"pillbox t = {t*1e6:.2f} us: x.(S+ - S-) = -Js.E", rtol=1e-5, atol=1e-6)
# (d) energy by t = 3 us
tt = (np.arange(600000) + 0.5) / 600000 * 3e-6
Winj = np.mean(-np.array([JEp(s) for s in tt[::50]])) * 3e-6
close(Winj, 540 * np.pi * 1e-6, "energy delivered by 3 us = (eta J0^2/4)(3 us) = 540 pi uJ/m^2", rtol=1e-5)
close(540 * np.pi * 1e-6, 1.6965e-3, "= 1.70 mJ/m^2", rtol=1e-4)
xx = (np.arange(1200000) + 0.5) / 1200000 * 600.0
wx = lambda x, t: 0.5 * eps * (eta * J0 / 2 * u(t - x / v) * np.cos(om * t - beta * x)) ** 2 + 0.5 * mu * (J0 / 2 * u(t - x / v) * np.cos(om * t - beta * x)) ** 2
Wside = np.mean(wx(xx, 3e-6)) * 600.0
close(2 * Wside, Winj, "stored energy in |x| < 600 m at 3 us = energy delivered (both sides)", rtol=1e-5)
close(Wside, 8.482e-4, "each side holds 0.848 mJ/m^2", rtol=1e-3)
wav = 90 * np.pi / v
close(wav, 1.4137e-6, "<w> behind the front = <S>/v = 1.41 uJ/m^3", rtol=1e-4)
close(0.5 * eps * (eta * J0 / 2) ** 2, wav, "<w> = eps E0^2/2 (w_e = w_m, each averaging eps E0^2/4)")
close(wav * 600, Wside, "<w> x 600 m = stored per side")
# exact stored energy at any t (not only whole periods): (eta J0^2/4) [t/2 + sin(2wt)/(4w)] per side
for t in (0.31e-6, 1.17e-6, 2.875e-6):
    n = int(800000 * t / 3e-6)
    xs = (np.arange(n) + 0.5) / n * v * t
    W1 = np.mean(wx(xs, t)) * v * t
    close(W1, (eta * J0 ** 2 / 4) * (t / 2 + np.sin(2 * om * t) / (4 * om)), f"stored per side at t = {t*1e6} us matches the injected half", rtol=2e-5)
# (e) window at x = 900 m
close(900 / v, 4.5e-6, "energy first reaches x = 900 m at 4.5 us")
close(90 * np.pi * 1.0, 282.743, "average power through 1 m^2 there: 283 W", rtol=1e-5)
# vacuum variant
close([120 * np.pi * J0 / 2, 120 * np.pi * J0 ** 2 / 8, 120 * np.pi * J0 ** 2 / 4], [180 * np.pi, 135 * np.pi, 270 * np.pi],
      "vacuum variant: E0 = 180 pi, <S> = 135 pi, injected 270 pi")
close([180 * np.pi, 135 * np.pi, 270 * np.pi], [565.487, 424.115, 848.230], "= 565 V/m, 424 W/m^2, 848 W/m^2", rtol=1e-5)
# not the exam key: S20 HE3 #2 (free space, 4 sin, z = 0) gives <Js.E> = -480 pi and <S> = 240 pi
ok(not np.isclose(-JEav, 480 * np.pi) and not np.isclose(90 * np.pi, 240 * np.pi) and not np.isclose(om, 2 * np.pi * 1e6),
   "worked problem's numbers (180 pi, 90 pi, 4 pi x 10^6 rad/s) differ from the S20 HE3 #2 key")

print("=== O. Figure arrow directions (screen frame X right, Y up, Z out)")
sX, sY, sZ = np.eye(3)
# wire figure: physics z -> screen X; above the wire rho_hat = +Y
for rh, lab, Hexp, Sexp in ((sY, "above", sZ, -sY), (-sY, "below", -sZ, sY)):
    ph = cr(sX, rh)                       # phi_hat = z x rho_hat
    close(ph, Hexp, f"wire, {lab}: H along {'out of the page (odot)' if Hexp[2] > 0 else 'into the page (otimes)'}")
    close(cr(sX, ph), Sexp, f"wire, {lab}: S = E x H points {'down' if Sexp[1] < 0 else 'up'}, into the wire")
# sheet figure (notes' orientation, L19 frame): physics x -> Y (up), y -> Z (out), z -> X (right)
close(cr(sY, sZ), sX, "frame check: x cross y = z  <->  Y cross Z = X")
close(cr(-sY, -sZ), sX, "sheet, z > 0: E = -x (down), H = -y (otimes): S to the right, away")
close(cr(-sY, sZ), -sX, "sheet, z < 0: E = -x (down), H = +y (odot): S to the left, away")
# problem icon: physics x -> X (right), z -> Y (up), y = z x x -> Y x X = -Z (into the page)
close(cr(sY, sX), -sZ, "problem frame: y_hat = z_hat x x_hat is into the page")
close(cr(sY, sZ), sX, "problem, x > 0: E = +z (up), H = -y (odot, out): S = +x (right)")
close(cr(sY, -sZ), -sX, "problem, x < 0: E = +z (up), H = +y (otimes, in): S = -x (left)")

print("=== P. Handbook values behind the material numbers on the page")
# Nichrome (80Ni-20Cr) resistivity at 20 C: about 1.08-1.12e-6 ohm m in handbook tables (page uses 1.10e-6)
ok(1.08e-6 <= 1.10e-6 <= 1.12e-6, "nichrome resistivity 1.10 uOhm m lies in the handbook range 1.08-1.12 uOhm m")
# Sea water conductivity: about 4-5 S/m (salinity ~35 g/kg, 15-25 C); the site uses 4 S/m throughout (Lecture 8 page)
ok(4.0 <= 4.0 <= 5.5, "sea water sigma = 4 S/m is within the handbook 4-5.5 S/m")
# Total solar irradiance at 1 AU: 1360.8 +- 0.5 W/m^2 (Kopp & Lean 2011); page uses 1361 W/m^2
ok(abs(1361 - 1360.8) <= 0.5, "solar constant 1361 W/m^2 matches 1360.8 +- 0.5 W/m^2")
# relative permittivity of sea water ~ 81 (static), used only in the relaxation-time remark
ok(70 <= 81 <= 85, "eps_r of water/sea water ~ 81 (static)")

print(f"\nALL {ok_count} CHECKS PASSED")
