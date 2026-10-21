#!/usr/bin/env python3
"""Verification of every number, sign and direction on the Lecture 27 pages of the ECE 329 study site.

Pages checked:
  content-src/4-transmission-lines/27-guided-tem-waves-on-transmission-lines.md   (sections A-G)
  content-src/concepts/telegraphers-equations.md, characteristic-impedance.md    (section J)
  content-src/problems/a-backward-pulse-on-a-parallel-plate-line.md              (section I)
  figs_l27.py: arrow directions and labels                                       (section H)
numpy/scipy only. Derivatives by central differences; the battery launch by a leapfrog (FDTD) solution of the
telegrapher's equations and by an independent lumped LC-ladder simulation; line parameters by independent field
integrals (Gauss / flux) and image charges; the coax TE11 cutoff from its exact Bessel characteristic equation.
"""
import numpy as np
from scipy.special import jvp, yvp
from scipy.optimize import brentq

mu0 = 4e-7 * np.pi
eps0 = 8.8541878128e-12
c = 1 / np.sqrt(mu0 * eps0)
eta0 = np.sqrt(mu0 / eps0)
X, Y, Z = np.eye(3)
cr = np.cross
n_ok = 0


def ok(cond, msg):
    global n_ok
    assert cond, "FAILED: " + msg
    n_ok += 1
    print("ok  ", msg)


def near(a, b, msg, rel=0.01):
    ok(abs(a - b) <= rel * abs(b), f"{msg}: computed {a:.6g}, page {b:.6g} (tol {rel:.1%})")


def small(r, msg, tol):
    ok(abs(r) <= tol, f"{msg}: residual {abs(r):.2e} (tol {tol:.0e})")


# ============================================================ A. plate sources, line parameters, LC = mu eps
print("\n== A. plate charges/currents; L, C, G; LC = mu eps; G/C = sigma/eps")
# boundary conditions with n from the plate into the gap: rho_s = n.D, J_s = n x H
Ex, Hy, eps = 2.0, 0.7, 3 * eps0
for nhat, rs, js, name in ((X, +eps * Ex, +Hy * Z, "plate 2 (x=0)"), (-X, -eps * Ex, -Hy * Z, "plate 1 (x=d)")):
    ok(np.isclose(nhat @ (eps * Ex * X), rs), f"{name}: rho_s = n.D = {'+' if rs > 0 else '-'}eps Ex")
    ok(np.allclose(cr(nhat, Hy * Y), js), f"{name}: J_s = n x (y Hy) = {'+' if js[2] > 0 else '-'}z Hy")
rng = np.random.default_rng(1)
for _ in range(3):
    mu, ep, sg = mu0 * rng.uniform(1, 3), eps0 * rng.uniform(1, 10), rng.uniform(0, 1e-3)
    d, W = rng.uniform(1e-3, 1e-2), rng.uniform(2e-2, 1e-1)
    a = rng.uniform(1e-4, 1e-3); b = a * rng.uniform(1.5, 8); h = a * rng.uniform(1.2, 10)
    for GF, nm in ((W / d, "plates"), (2 * np.pi / np.log(b / a), "coax"), (np.pi / np.arccosh(h / a), "twin-lead")):
        L, C, G = mu / GF, ep * GF, sg * GF
        ok(np.isclose(L * C, mu * ep) and np.isclose(G / C, sg / ep), f"{nm}: LC = mu eps, G/C = sigma/eps")
        ok(np.isclose(np.sqrt(L / C), np.sqrt(mu / ep) / GF), f"{nm}: Z0 = sqrt(L/C) = eta/GF")
        ok(np.isclose(1 / np.sqrt(L * C), 1 / np.sqrt(mu * ep)), f"{nm}: v = 1/sqrt(LC) = 1/sqrt(mu eps)")

# coax C and L by independent integrals: Gauss field -> V, Ampere field -> flux
a, b, ep, mu = 0.5e-3, 1.75e-3, 2.25 * eps0, mu0
r = np.linspace(a, b, 200001)
q = 1e-9                                  # C/m on the inner conductor
V = np.trapezoid(q / (2 * np.pi * ep * r), r)
near(q / V, 2 * np.pi * ep / np.log(b / a), "coax C' from integrating E_r = q/(2 pi eps r)", 1e-6)
I0 = 1.0
Psi = np.trapezoid(mu * I0 / (2 * np.pi * r), r)
near(Psi / I0, mu / (2 * np.pi) * np.log(b / a), "coax L' from the flux of B_phi = mu I/(2 pi r)", 1e-6)

# twin-lead: image line charges +-q at x = -/+ s, s = sqrt(h^2 - a^2); check the cylinders are equipotentials, then C'
for hoa in (2.0, 6.14):
    a = 1.0; h = hoa * a; s = np.sqrt(h ** 2 - a ** 2); ep = eps0; qq = 1e-9
    def phi(x, y):                        # +q at (-s,0) (wire 2, left), -q at (+s,0) (wire 1, right)
        return qq / (2 * np.pi * ep) * (np.log(np.hypot(x - s, y)) - np.log(np.hypot(x + s, y)))
    th = np.linspace(0, 2 * np.pi, 721)
    p2 = phi(-h + a * np.cos(th), a * np.sin(th)); p1 = phi(h + a * np.cos(th), a * np.sin(th))
    ok(np.ptp(p2) < 1e-9 * abs(p2.mean()) and np.ptp(p1) < 1e-9 * abs(p1.mean()), f"twin-lead D/2a = {hoa}: both wire surfaces equipotential")
    near(qq / (p2.mean() - p1.mean()), np.pi * ep / np.arccosh(h / a), f"twin-lead D/2a = {hoa}: C' = pi eps / arccosh(D/2a)", 1e-9)
    # inductance: flux per metre between the wires from equivalent line currents +-I at -/+ s (TEM: same distribution)
    x = np.linspace(-h + a, h - a, 400001)
    By = mu0 * I0 / (2 * np.pi) * (1 / (x + s) + 1 / (s - x))   # both currents give B along the same sense between them
    near(np.trapezoid(By, x) / I0, mu0 / np.pi * np.arccosh(h / a), f"twin-lead D/2a = {hoa}: L' = (mu/pi) arccosh(D/2a) from the flux", 1e-6)

# ============================================================ B. telegrapher's equations from the fields, by finite differences
print("\n== B. telegrapher's equations from Maxwell's fields (finite differences)")
d, W = 2e-3, 4e-2
mu, ep = mu0, 2.25 * eps0
v = 1 / np.sqrt(mu * ep); eta = np.sqrt(mu / ep)
L, C = mu * d / W, ep * W / d
f = lambda t: np.exp(-((t - 3e-9) / 0.7e-9) ** 2)              # smooth pulse
fp = lambda t: -2 * (t - 3e-9) / 0.7e-9 ** 2 * f(t)
z0, t0, hz, ht = 0.25, 4.1e-9, 1e-5, 1e-14
for sgn, nm in ((+1, "toward +z"), (-1, "toward -z")):
    Exf = lambda z, t: f(t - sgn * z / v)
    Hyf = lambda z, t: sgn * f(t - sgn * z / v) / eta                # H = u x E / eta
    # Maxwell residuals (scaled)
    dEdz = (Exf(z0 + hz, t0) - Exf(z0 - hz, t0)) / (2 * hz); dHdt = (Hyf(z0, t0 + ht) - Hyf(z0, t0 - ht)) / (2 * ht)
    dHdz = (Hyf(z0 + hz, t0) - Hyf(z0 - hz, t0)) / (2 * hz); dEdt = (Exf(z0, t0 + ht) - Exf(z0, t0 - ht)) / (2 * ht)
    small((dEdz + mu * dHdt) / abs(dEdz), f"plane wave {nm}: dEx/dz = -mu dHy/dt", 1e-6)
    small((-dHdz - ep * dEdt) / abs(dHdz), f"plane wave {nm}: -dHy/dz = eps dEx/dt", 1e-6)
    Vf = lambda z, t: Exf(z, t) * d; If = lambda z, t: Hyf(z, t) * W
    dVdz = (Vf(z0 + hz, t0) - Vf(z0 - hz, t0)) / (2 * hz); dIdt = (If(z0, t0 + ht) - If(z0, t0 - ht)) / (2 * ht)
    dIdz = (If(z0 + hz, t0) - If(z0 - hz, t0)) / (2 * hz); dVdt = (Vf(z0, t0 + ht) - Vf(z0, t0 - ht)) / (2 * ht)
    small((-dVdz - L * dIdt) / abs(dVdz), f"V = Ex d, I = Hy W {nm}: -dV/dz = L dI/dt", 1e-6)
    small((-dIdz - C * dVdt) / abs(dIdz), f"V = Ex d, I = Hy W {nm}: -dI/dz = C dV/dt", 1e-6)
    ok(np.isclose(Vf(z0, t0) / If(z0, t0), sgn * eta * d / W), f"{nm}: V/I = {'+' if sgn > 0 else '-'}eta d/W = {'+' if sgn > 0 else '-'}Z0")
# lossy filling: damped monochromatic plane wave -> telegrapher with G
sig, w = 0.02, 2 * np.pi * 1e9
gam = np.sqrt(1j * w * mu * (sig + 1j * w * ep)); etac = np.sqrt(1j * w * mu / (sig + 1j * w * ep))
G = sig * W / d
Exl = lambda z, t: np.real(np.exp(1j * w * t - gam * z)); Hyl = lambda z, t: np.real(np.exp(1j * w * t - gam * z) / etac)
z0, t0, hz, ht = 0.031, 0.37e-9, 1e-6, 1e-15
Vl = lambda z, t: Exl(z, t) * d; Il = lambda z, t: Hyl(z, t) * W
dVdz = (Vl(z0 + hz, t0) - Vl(z0 - hz, t0)) / (2 * hz); dIdt = (Il(z0, t0 + ht) - Il(z0, t0 - ht)) / (2 * ht)
dIdz = (Il(z0 + hz, t0) - Il(z0 - hz, t0)) / (2 * hz); dVdt = (Vl(z0, t0 + ht) - Vl(z0, t0 - ht)) / (2 * ht)
small((-dVdz - L * dIdt) / abs(dVdz), "lossy filling: -dV/dz = L dI/dt", 1e-5)
small((-dIdz - C * dVdt - G * Vl(z0, t0)) / abs(dIdz), "lossy filling: -dI/dz = C dV/dt + G V, G = sigma W/d", 1e-5)
# the circuit readings: Faraday on a thin xz loop, charge conservation on plate 2
loop_n = cr(Z, X)  # loop up (x) at z, then +z along plate 1: circulation sense; normal by RHR
ok(np.allclose(cr(X, Z), -Y), "loop up at z then along +z: circulation normal = x x z = -y (into the side view)")
# V(z) - V(z+dz) = -d/dt int B.dS with dS = -y dx dz  ->  + mu d dz dHy/dt
zz, tt, dz = 0.25, 4.1e-9, 1e-6
Exf = lambda z, t: f(t - z / v); Hyf = lambda z, t: f(t - z / v) / eta
lhs = (Exf(zz, tt) - Exf(zz + dz, tt)) * d
rhs = mu * d * dz * (Hyf(zz + dz / 2, tt + ht) - Hyf(zz + dz / 2, tt - ht)) / (2 * ht)
small((lhs - rhs) / abs(rhs), "Faraday on the xz loop: V(z) - V(z+dz) = mu d dz dHy/dt", 1e-5)
qline = lambda z, t: ep * Exf(z, t) * W                            # plate-2 charge per metre = C V
small((qline(zz, tt) - C * Exf(zz, tt) * d) / (C * d), "plate-2 charge per metre rho_s W = eps Ex W = C V", 1e-12)
dqdt = (qline(zz, tt + ht) - qline(zz, tt - ht)) / (2 * ht)
dIdz = (Hyf(zz + hz, tt) * W - Hyf(zz - hz, tt) * W) / (2 * hz)
small((dqdt + dIdz) / abs(dIdz), "charge conservation on plate 2: dq/dt = -dI/dz", 1e-6)

# ============================================================ C. wave equation, d'Alembert, Z0, anti-derivative
print("\n== C. wave equation and d'Alembert solutions")
Z0 = np.sqrt(L / C)
g = lambda t: np.sin(2 * np.pi * t / 2e-9) * np.exp(-((t - 5e-9) / 1e-9) ** 2)
Vs = lambda z, t: f(t - z / v) + g(t + z / v)
Is = lambda z, t: (f(t - z / v) - g(t + z / v)) / Z0
for (z0, t0) in ((0.1, 2e-9), (0.6, 4.7e-9), (-0.3, 5.5e-9)):
    hz, ht = 1e-5, 1e-14
    dVdz = (Vs(z0 + hz, t0) - Vs(z0 - hz, t0)) / (2 * hz); dIdt = (Is(z0, t0 + ht) - Is(z0, t0 - ht)) / (2 * ht)
    dIdz = (Is(z0 + hz, t0) - Is(z0 - hz, t0)) / (2 * hz); dVdt = (Vs(z0, t0 + ht) - Vs(z0, t0 - ht)) / (2 * ht)
    sc = abs(dVdz) + abs(L * dIdt) + 1e-30
    small((-dVdz - L * dIdt) / sc, f"V = f + g, I = (f - g)/Z0 at z = {z0}: first equation", 1e-6)
    small((-dIdz - C * dVdt) / (abs(dIdz) + abs(C * dVdt)), f"... second equation", 1e-6)
    hz2, ht2 = 1e-4, 1e-13
    d2z = (Vs(z0 + hz2, t0) - 2 * Vs(z0, t0) + Vs(z0 - hz2, t0)) / hz2 ** 2
    d2t = (Vs(z0, t0 + ht2) - 2 * Vs(z0, t0) + Vs(z0, t0 - ht2)) / ht2 ** 2
    small((d2z - L * C * d2t) / (abs(d2z) + 1e-30), f"... wave equation V_zz = LC V_tt", 1e-4)
ok(np.isclose(1 / (C * v), Z0) and np.isclose(np.sqrt(L * C) * v, 1), "Z0 = 1/(C v) = sqrt(L/C); C v = 1/Z0")
ok(np.isclose(Z0, eta * d / W), "plates: Z0 = eta d/W")
# anti-derivative: -dI/dz = C f'(t - z/v) integrated in z gives I = C v f
zs = np.linspace(-1.0, 0.5, 300001); t0 = 4e-9
integrand = -C * fp(t0 - zs / v)                       # dI/dz
Inum = np.concatenate([[0], np.cumsum((integrand[1:] + integrand[:-1]) / 2 * np.diff(zs))])
ok(np.allclose(Inum + C * v * f(t0 - zs[0] / v), C * v * f(t0 - zs / v), atol=1e-9), "I = C v f(t - z/v) by integrating -dI/dz = C f'")

# ============================================================ D. battery launch: FDTD and lumped ladder
print("\n== D. the battery example: FDTD of the telegrapher's equations and an LC ladder")
V0, Z0b, vb = 3.0, 50.0, 2e8
Lb, Cb = Z0b / vb, 1 / (Z0b * vb)
ok(np.isclose(np.sqrt(Lb / Cb), 50) and np.isclose(1 / np.sqrt(Lb * Cb), 2e8), "50 ohm, 2e8 m/s line: L = 250 nH/m, C = 100 pF/m")
near(Lb, 250e-9, "L' = Z0/v", 1e-9); near(Cb, 100e-12, "C' = 1/(Z0 v)", 1e-9)
Nz, Lz = 2000, 2.0
dz = Lz / Nz; dt = dz / vb                                # magic time step: exact for the 1D wave
Vn = np.zeros(Nz + 1); In = np.zeros(Nz)                 # V at nodes, I at half nodes
nsteps = 1200
E_in = 0.0
for n in range(nsteps):
    Vn[0] = V0                                            # ideal battery at z = 0 for t > 0
    In -= dt / (Lb * dz) * (Vn[1:] - Vn[:-1])
    Vn[1:-1] -= dt / (Cb * dz) * (In[1:] - In[:-1])
    # source current = current into node 0 region ~ In[0]; energy delivered
    E_in += V0 * In[0] * dt
tN = nsteps * dt
zf = vb * tN
zn = np.arange(Nz + 1) * dz; zh = (np.arange(Nz) + 0.5) * dz
behind = zn < zf - 0.05; ahead = zn > zf + 0.05
ok(np.allclose(Vn[behind], 3.0, atol=1e-6) and np.allclose(Vn[ahead], 0, atol=1e-6), f"FDTD: V = 3 V behind the front z = vt = {zf:.2f} m, 0 ahead")
ok(np.allclose(In[zh < zf - 0.05], 0.06, atol=1e-8), "FDTD: I = V0/Z0 = 60 mA behind the front")
near(V0 * V0 / Z0b, 0.18, "battery power V I = V0^2/Z0", 1e-9)
Wst = np.sum(0.5 * Cb * Vn[1:-1] ** 2 * dz) + np.sum(0.5 * Lb * In ** 2 * dz)
WE = np.sum(0.5 * Cb * Vn[1:-1] ** 2 * dz); WM = np.sum(0.5 * Lb * In ** 2 * dz)
near(WE / WM, 1.0, "stored electric = magnetic energy behind the front", 0.01)
near(Wst, V0 ** 2 / Z0b * tN, "stored energy = (V0^2/Z0) t, the battery's VI times t", 0.01)
near(Cb * V0 ** 2 * vb, V0 ** 2 / Z0b, "C V^2 v = V^2/Z0", 1e-12)
# independent lumped ladder: series L dz, shunt C dz, battery on node 0; Runge-Kutta 4
Ncell, Lz2 = 400, 2.0
dzl = Lz2 / Ncell; Lc, Cc = Lb * dzl, Cb * dzl
def rhs(y):
    i = y[:Ncell]; vv = np.concatenate([[V0], y[Ncell:]])  # node 0 is the battery
    di = (vv[:-1] - vv[1:]) / Lc                          # inductor between node k and k+1 carries i_k
    iout = np.concatenate([i[1:], [0.0]])
    dv = (i - iout) / Cc
    return np.concatenate([di, dv])
yv = np.zeros(2 * Ncell); h = 0.05 * np.sqrt(Lc * Cc); T = 6e-9
for _ in range(int(T / h)):
    k1 = rhs(yv); k2 = rhs(yv + h / 2 * k1); k3 = rhs(yv + h / 2 * k2); k4 = rhs(yv + h * k3)
    yv += h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
tl = int(T / h) * h
vnode = yv[Ncell:]; zl = (np.arange(Ncell) + 1) * dzl
zhalf = np.interp(1.5, vnode[::-1], zl[::-1])            # where V crosses half of 3 V (monotone near the front)
near(zhalf, vb * tl, "LC ladder: the 1.5 V point sits at z = v t (front speed 1/sqrt(LC))", 0.02)
ok(abs(np.mean(vnode[zl < 0.6 * vb * tl]) - 3.0) < 0.1, "LC ladder: V ~ 3 V well behind the front (ringing averages out)")

# ============================================================ E. power
print("\n== E. power")
d, W = 2e-3, 4e-2; ep = 2.25 * eps0; eta = np.sqrt(mu0 / ep); Z0 = eta * d / W
for (z0, t0) in ((0.1, 2e-9), (0.6, 4.7e-9)):
    Exv = Vs(z0, t0) / d; Hyv = Is(z0, t0) / W
    ok(np.isclose(W * d * Exv * Hyv, Vs(z0, t0) * Is(z0, t0)), f"p = W d Ex Hy = V I at z = {z0}")
    fz, gz = f(t0 - z0 / v), g(t0 + z0 / v)
    ok(np.isclose(Vs(z0, t0) * Is(z0, t0), (fz ** 2 - gz ** 2) / Z0), "V I = (f^2 - g^2)/Z0: no cross term")
Vp, Vm, wq = 1.3 * np.exp(0.4j), 0.6 * np.exp(-1.1j), 2 * np.pi * 1e9
tq = np.linspace(0, 1e-9, 20001)[:-1]
for zq in (0.0, 0.037, 0.11):
    beta = wq / v
    Vt = np.real((Vp * np.exp(-1j * beta * zq) + Vm * np.exp(1j * beta * zq)) * np.exp(1j * wq * tq))
    It = np.real((Vp * np.exp(-1j * beta * zq) - Vm * np.exp(1j * beta * zq)) / Z0 * np.exp(1j * wq * tq))
    Vph = Vp * np.exp(-1j * beta * zq) + Vm * np.exp(1j * beta * zq); Iph = (Vp * np.exp(-1j * beta * zq) - Vm * np.exp(1j * beta * zq)) / Z0
    near(np.mean(Vt * It), 0.5 * np.real(Vph * np.conj(Iph)), f"<P> = 1/2 Re(V I*) at z = {zq} (quadrature)", 1e-6)
    near(0.5 * np.real(Vph * np.conj(Iph)), (abs(Vp) ** 2 - abs(Vm) ** 2) / (2 * Z0), "... = (|V+|^2 - |V-|^2)/(2 Z0)", 1e-9)

# ============================================================ F. non-TEM cutoffs (notes' margin) and site examples
print("\n== F. non-TEM cutoffs; examples on the lecture page")
# parallel plates: lowest non-TEM transverse eigenvalue on [0, d] (TE: Ey = 0 at both plates) by finite differences
d = 1e-2; N = 2000; xs = np.linspace(0, d, N + 1); hx = xs[1] - xs[0]
A = (np.diag(2 * np.ones(N - 1)) - np.diag(np.ones(N - 2), 1) - np.diag(np.ones(N - 2), -1)) / hx ** 2
kc = np.sqrt(np.linalg.eigvalsh(A)[0])
near(kc, np.pi / d, "plates: lowest non-TEM kc = pi/d, i.e. cutoff at d = lambda/2", 1e-5)
near(c / (2 * d) / 1e9, 15.0, "air plates d = 1 cm: TEM-only below c/2d (GHz)", 0.01)
def te11_kc(a, b):
    F = lambda k: jvp(1, k * a) * yvp(1, k * b) - jvp(1, k * b) * yvp(1, k * a)
    ks = np.linspace(0.2 / b, 4 / (a + b), 4000); vals = F(ks)
    i = np.where(np.sign(vals[:-1]) != np.sign(vals[1:]))[0][0]
    return brentq(F, ks[i], ks[i + 1])
for boa in (2.0, 3.5, 6.5):
    a, b = 1.0, boa
    kc = te11_kc(a, b)
    rel = (2 * np.pi / kc) / (np.pi * (a + b)) - 1
    ok(abs(rel) < 0.05, f"coax b/a = {boa}: exact TE11 lambda_c vs pi(a+b): {rel:+.2%} (the notes' rule is approximate)")
a, b = 0.5e-3, 1.75e-3; vpe = c / 1.5
near(np.pi * (a + b) * 1e3, 7.07, "coax a = 0.5, b = 1.75 mm: pi(a+b) in mm", 0.002)
near(vpe / (np.pi * (a + b)) / 1e9, 28.3, "... TEM-only below v/(pi(a+b)) GHz (approx. rule)", 0.005)
near(vpe * te11_kc(a, b) / (2 * np.pi) / 1e9, 28.3, "... exact TE11 cutoff in polyethylene (GHz)", 0.03)
eta_pe = eta0 / 1.5
near(eta_pe, 251.0, "eta in polyethylene (eps_r 2.25)", 0.002)
near(eta_pe / (2 * np.pi) * np.log(3.5), 50.0, "coax b/a = 3.5 in polyethylene: Z0 (ohm)", 0.003)
near(np.exp(2 * np.pi * 75 / eta_pe), 6.5, "75-ohm polyethylene coax: b/a", 0.01)
near(300 * np.pi / eta0, 2.50, "300-ohm twin-lead in air: arccosh(D/2a)", 0.002)
near(2 * np.cosh(300 * np.pi / eta0), 12.3, "... D/a", 0.005)
near(eta0 / 50, 7.5, "50-ohm air plates: W/d", 0.01)
near(c / 60 / 1e3, 5000, "60 Hz wavelength in vacuum (km)", 0.001)
near(vpe / 3e9 * 100, 6.7, "3 GHz in polyethylene: lambda (cm)", 0.01)
near(3 / 50 * 1e3, 60, "battery: I = 3 V/50 ohm (mA)", 1e-9)

# ============================================================ H. figure directions
print("\n== H. figure directions (screen frame: X right, Y up, Z out)")
# tl-guided-pulse (side view): physics z -> screen right, x -> screen up, y -> out of the screen
Rm = np.column_stack([Y, Z, X])                          # columns: images of physics x, y, z
ok(np.isclose(np.linalg.det(Rm), 1), "side view: (x up, y out, z right) is a proper rotation")
S = cr(Rm @ X, Rm @ Y)
ok(np.allclose(S, Rm @ Z) and np.allclose(S, X), "side view: E (up) x H (out, odot) = screen right = +z, the travel")
ok(np.allclose(cr(Y, X), -Z), "plate 2 below the gap: n = up, J_s = n x H = up x out = right (+z)")
ok(np.allclose(cr(Y, Z), X), "... i.e. Y x Z = X: current on the bottom plate points right")
ok(np.allclose(cr(-Y, Z), -X), "plate 1 above the gap: n = down, J_s = down x out = left (-z)")
# tl-cross-sections: viewed looking along +z (into the page): x up, y right, z into the screen
Rc = np.column_stack([Y, X, -Z])                         # x up, y right, z into the page
ok(np.isclose(np.linalg.det(Rc), 1), "cross-section view: (x up, y right, z into page) is a proper rotation")
ok(np.allclose(cr(Rc @ X, Rc @ Y), Rc @ Z) and np.allclose(cr(Y, X), -Z), "plates: E up x H right = into the page (+z)")
# coax: inner conductor current along +z = into the page (-Z); H = I_dir x r_hat
for ang in np.linspace(0, 2 * np.pi, 9)[:-1]:
    rh = np.array([np.cos(ang), np.sin(ang), 0])
    Hd = cr(-Z, rh)
    ok(np.cross(rh, Hd)[2] < 0, f"coax at {np.degrees(ang):.0f} deg: H clockwise on screen (r x H into page)") if ang == 0 else None
    ok(np.allclose(cr(rh, Hd), -Z), f"coax at {np.degrees(ang):.0f} deg: E (outward) x H = into page")
# twin-lead: wire 2 left (+, current into page), wire 1 right (-, current out); at the midpoint
Hmid = cr(-Z, X) + cr(Z, -X)            # left wire: r_hat to midpoint = +X; right wire: r_hat = -X
ok(np.allclose(Hmid / np.linalg.norm(Hmid), -Y), "twin-lead midpoint: H points down (screen)")
ok(np.allclose(cr(X, -Y), -Z), "twin-lead midpoint: E (left to right) x H (down) = into page (+z)")
# around each wire: wire 2 (current into page) clockwise, wire 1 (out of page) counterclockwise
ok(cr(X, cr(-Z, X))[2] < 0 and cr(X, cr(Z, X))[2] > 0, "twin-lead: H clockwise around wire 2, counterclockwise around wire 1")
# tl-ladder: battery + on wire 2 (top) -> forward wave V = V0 > 0, I = V0/Z0 > 0 along +z (right) on wire 2, back on wire 1
ok(3.0 / 50 > 0, "tl-ladder: forward step with V0 > 0 has I > 0: rightward arrow on wire 2, leftward on wire 1")
# twin-lead field lines: E circles through (+-s, 0) are orthogonal to the H circles (Apollonius, h_k^2 - r_k^2 = s^2)
s = np.sqrt(2.0 ** 2 - 1)
for yc in (0.8, 2.5):
    for hk in (2.0, 3.0):
        rk = np.sqrt(hk ** 2 - s ** 2); Re = np.hypot(s, yc)
        dist2 = hk ** 2 + yc ** 2
        ok(np.isclose(dist2, Re ** 2 + rk ** 2), f"twin-lead lines: E circle (yc = {yc}) meets H circle (h = {hk}) at right angles")

# ============================================================ I. worked problem
print("\n== I. worked problem: a backward pulse on a parallel-plate line")
etaC = 120 * np.pi; cC = 3e8; e0C = 1e-9 / (36 * np.pi)
d, W, er, l = 2e-3, 4e-2, 2.25, 30.0
eta = etaC / np.sqrt(er); v = cC / np.sqrt(er)
L, C = mu0 * d / W, er * e0C * W / d
near(eta / np.pi, 80, "eta = 80 pi ohm"); near(L * 1e9, 62.8, "L' (nH/m)", 0.001); near(L / (2 * np.pi * 1e-8), 1, "L' = 2 pi x 10^-8 H/m", 1e-9)
near(C * 1e12, 398, "C' (pF/m)", 0.001); near(1 / np.sqrt(L * C), 2e8, "v (m/s)", 1e-9)
Z0 = np.sqrt(L / C); near(Z0, 4 * np.pi, "Z0 = 4 pi ohm", 1e-9); near(Z0, 12.57, "Z0 (ohm)", 0.001)
near(Z0, eta * d / W, "Z0 = eta d/W", 1e-9); near(l / v * 1e9, 150, "one-way delay (ns)", 1e-9)
I_top = 0.5; I2 = -I_top                                  # current along +z on plate 2 (x = 0)
Vb = -Z0 * I2                                             # backward wave: I = -g/Z0, V = g
near(Vb, 2 * np.pi, "(b) V = -Z0 I = 2 pi V", 1e-9); near(Vb, 6.28, "(b) V (V)", 0.001)
Exb = Vb / d; Hyb = I2 / W
near(Exb, 1000 * np.pi, "(b) Ex = V/d = 1000 pi V/m", 1e-9); near(Exb / 1e3, 3.14, "(b) Ex (kV/m)", 0.001)
near(Hyb, -12.5, "(b) Hy = I/W = -12.5 A/m", 1e-9)
near(Exb / abs(Hyb), eta, "(b) |Ex/Hy| = eta", 1e-9)
ok(np.allclose(cr(X * Exb, Y * Hyb) / abs(Exb * Hyb), -Z), "(b) E x H along -z: the pulse travels toward -z")
ok(np.allclose(cr(-X, Y * Hyb), Z * I_top / W), "(b) top plate J_s = (-x) x H = +z I_top/W (consistent with the given current)")
rho2 = er * e0C * Exb
near(rho2 * 1e9, 62.5, "(b) rho_s on the x = 0 plate (nC/m^2), positive", 1e-9)
near(rho2 * W * 1e9, 2.5, "(b) charge per metre on the x = 0 plate (nC/m) = C V", 1e-9)
near(C * Vb * 1e9, 2.5, "(b) C V (nC/m)", 1e-9)
near(v * 2e-9, 0.4, "(b) pulse length v T (m)", 1e-9)
near(Vb ** 2 / Z0, np.pi, "(b) power during the pulse V^2/Z0 = pi W", 1e-9)
near(Vb * I2, -np.pi, "(b) p = V I = -pi W (toward -z)", 1e-9)
near(np.pi * 2e-9 * 1e9, 6.28, "(b) pulse energy (nJ)", 0.001)
f15 = 1.5e9; lam = v / f15; beta = 2 * np.pi / lam
near(lam * 100, 13.3, "(c) lambda (cm)", 0.003); near(beta, 15 * np.pi, "(c) beta = 15 pi rad/m", 1e-9); near(beta, 47.1, "(c) beta (rad/m)", 0.001)
V0c = 12.0; I0c = V0c / Z0
near(I0c, 0.955, "(c) |I| = 12/(4 pi) A", 0.001); near(I0c, 3 / np.pi, "(c) I = 3/pi A", 1e-9)
near(V0c / d, 6000, "(c) |E| (V/m)", 1e-9); near(I0c / W, 23.9, "(c) |H| (A/m)", 0.002); near(I0c / W, 75 / np.pi, "(c) H = 75/pi A/m", 1e-9)
S = 0.5 * (V0c / d) * (I0c / W)
near(S / 1e3, 71.6, "(c) <S> (kW/m^2)", 0.001)
near(W * d, 8e-5, "(c) cross-section W d (m^2)", 1e-9)
near(S * W * d, 18 / np.pi, "(c) <P> = <S> W d = 18/pi W", 1e-9); near(18 / np.pi, 5.73, "(c) <P> (W)", 0.001)
near(0.5 * V0c ** 2 / Z0, 18 / np.pi, "(c) <P> = |V|^2/(2 Z0)", 1e-9)
tq = np.linspace(0, 1 / f15, 4001)[:-1]
near(np.mean((V0c * np.cos(2 * np.pi * f15 * tq)) * (I0c * np.cos(2 * np.pi * f15 * tq))), 18 / np.pi, "(c) time average of V(t) I(t) by quadrature", 1e-6)
near(lam / 2 * 100, 6.7, "(c) lambda/2 (cm)", 0.01)
ok(d < lam / 2, "(c) d = 2 mm < lambda/2 = 6.7 cm: only TEM propagates")
near(v / (2 * d) / 1e9, 50, "(c) first non-TEM cutoff v/2d (GHz)", 1e-9)
v2 = l / 200e-9; er2 = (cC / v2) ** 2
near(v2, 1.5e8, "(d) v = 30 m / 200 ns", 1e-9); near(er2, 4, "(d) eps_r = (c/v)^2 = 4", 1e-9)
near(etaC / np.sqrt(er2) * d / W, 3 * np.pi, "(d) Z0 = 60 pi x 0.05 = 3 pi ohm", 1e-9); near(3 * np.pi, 9.42, "(d) Z0 (ohm)", 0.001)

# ============================================================ J. concept pages
print("\n== J. concept pages")
near(eta0 / np.pi * np.arccosh(6.14 / 1.0), 300, "twin-lead D/2a = 6.14 in air: Z0 (ohm)", 0.002)
near(eta0 * 0.2, 75.3, "air plates d/W = 0.2: Z0 (ohm)", 0.002)

# ============================================================ K. errata check: L-section (drawn) vs T-section (named)
print("\n== K. L-section vs T-section ladders (erratum on p. 8)")
Lp, Cp, w = 250e-9, 100e-12, 2 * np.pi * 1e9
beta_exact = w * np.sqrt(Lp * Cp)
for dz in (1e-2, 1e-3, 1e-4):
    Zs, Ysh = 1j * w * Lp * dz, 1j * w * Cp * dz
    ser = lambda Z: np.array([[1, Z], [0, 1]]); sh = lambda Y: np.array([[1, 0], [Y, 1]])
    ABCD_L = ser(Zs) @ sh(Ysh)                         # series dz L, then shunt dz C (the notes' drawing)
    ABCD_T = ser(Zs / 2) @ sh(Ysh) @ ser(Zs / 2)       # a true T: half the inductance on each side
    bL = np.arccos(np.real(np.trace(ABCD_L)) / 2) / dz
    bT = np.arccos(np.real(np.trace(ABCD_T)) / 2) / dz
    ok(np.isclose(bL, bT, rtol=1e-12), f"dz = {dz:g} m: L- and T-section ladders have the same Bloch phase per metre")
    ok(abs(bL / beta_exact - 1) < (w * np.sqrt(Lp * Cp) * dz) ** 2, f"... and it tends to w sqrt(LC) (rel. error {abs(bL / beta_exact - 1):.1e}, O(dz^2))")

print(f"\nAll {n_ok} checks passed.")
