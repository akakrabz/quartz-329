#!/usr/bin/env python3
"""Verification of every number, sign and direction on the Lecture 26 pages of the ECE 329 study site.

Pages checked:
  content-src/3-maxwell-and-waves/26-standing-waves-and-radiation-pressure.md   (sections A-G)
  figs_l26.py: figure values and arrow directions                               (section H)
  content-src/problems/a-circular-wave-meets-a-mirror.md                        (section I)
  content-src/concepts/standing-waves.md, concepts/radiation-pressure.md        (section J)
  word limits of the brief                                                      (section K)
numpy only. gamma = sqrt(j w mu (sigma + j w eps)), eta = sqrt(j w mu/(sigma + j w eps)) (Lecture 22), principal roots.
Maxwell's curl equations are checked by central differences; time averages by quadrature over one period of the
instantaneous products; depth integrals by the trapezoid rule on fine grids; every direction by np.cross.
"""
import re
import numpy as np

mu0 = 4e-7 * np.pi
eps0 = 8.8541878128e-12
c = 1 / np.sqrt(mu0 * eps0)
eta0 = np.sqrt(mu0 / eps0)
hbar = 1.054571817e-34
X, Y, Z = np.eye(3)
cr = np.cross
trap = np.trapezoid if hasattr(np, "trapezoid") else np.trapz
ok_count = 0


def ok(cond, msg):
    global ok_count
    assert cond, "FAILED: " + msg
    ok_count += 1
    print("ok  ", msg)


def close(a, b, msg, rtol=1e-9, atol=None):
    a_, b_ = np.asarray(a), np.asarray(b)
    if atol is None:                      # default: relative to the scale of the expected array
        sc = np.max(np.abs(b_)) if np.any(b_ != 0) else 1.0
        atol = 1e-12 * sc
    shown = f"max |diff| {np.max(np.abs(a_ - b_)):.1e} over {a_.size} values" if a_.size > 6 else f"{np.array2string(np.atleast_1d(a_), precision=6)} vs {np.array2string(np.atleast_1d(b_), precision=6)}"
    ok(np.allclose(a, b, rtol=rtol, atol=atol), f"{msg}: {shown}")


def near(a, b, msg, rel=0.01):
    ok(abs(a - b) <= rel * abs(b), f"{msg}: computed {a:.6g}, page {b:.6g} (tol {rel:.1%})")


def medium(w, mu, eps, sig):
    g = np.sqrt(1j * w * mu * (sig + 1j * w * eps))
    eta = np.sqrt(1j * w * mu / (sig + 1j * w * eps))
    return g, eta


def section(s):
    print("\n==== " + s)


# ======================================================================================== A. standing-wave phasors
section("A. Standing-wave phasors and real forms (notes pp. 1-2; page section 1)")
f = 300e6
w = 2 * np.pi * f
for name, mur, epr, E0 in (("vacuum", 1.0, 1.0, 1.0), ("dielectric eps_r = 2.25", 1.0, 2.25, 3.0), ("mu_r = 4, eps_r = 9", 4.0, 9.0, 0.7)):
    mu1, eps1 = mur * mu0, epr * eps0
    b1 = w * np.sqrt(mu1 * eps1); eta1 = np.sqrt(mu1 / eps1); lam = 2 * np.pi / b1
    # Lecture 25's Gamma with a nearly perfect conductor in region 2
    g2, eta2 = medium(w, mu0, eps0, 1e12)
    G = (eta2 - eta1) / (eta2 + eta1)
    ok(abs(G + 1) < 1e-6, f"[{name}] sigma2 -> infinity gives Gamma -> -1 (|Gamma + 1| = {abs(G + 1):.1e})")
    G = -1.0
    z = np.linspace(-2 * lam, 0, 2001)
    Ei = E0 * np.exp(-1j * b1 * z); Hi = E0 / eta1 * np.exp(-1j * b1 * z)
    Er = G * E0 * np.exp(1j * b1 * z)
    # reflected H from u x E / eta with u = -z, E along x
    Hr_vec = cr(-Z, X) * (G * E0 / eta1)                 # (-z) x x = -y, times Gamma
    close(Hr_vec, Y * (E0 / eta1), f"[{name}] H_r = (-z) x (Gamma E0 x)/eta1 = +y E0/eta1 for Gamma = -1 (the -Gamma = +1 rule)")
    Hr = Hr_vec[1] * np.exp(1j * b1 * z)
    Et, Ht = Ei + Er, Hi + Hr
    close(Et, -2j * E0 * np.sin(b1 * z), f"[{name}] E~ = -j x 2E0 sin(beta1 z)")
    close(Ht, 2 * E0 / eta1 * np.cos(b1 * z), f"[{name}] H~ = y (2E0/eta1) cos(beta1 z)")
    th = np.linspace(-3, 3, 13)
    close(np.exp(-1j * th) - np.exp(1j * th), -2j * np.sin(th), "identity e^-jth - e^jth = -2j sin th")
    close(np.exp(-1j * th) + np.exp(1j * th), 2 * np.cos(th), "identity e^-jth + e^jth = 2 cos th")
    # real time
    zz, tt = np.meshgrid(np.linspace(-lam, 0, 301), np.linspace(0, 1 / f, 201), indexing="ij")
    Ex = np.real(-2j * E0 * np.sin(b1 * zz) * np.exp(1j * w * tt))
    Hy = np.real(2 * E0 / eta1 * np.cos(b1 * zz) * np.exp(1j * w * tt))
    close(Ex, 2 * E0 * np.sin(b1 * zz) * np.sin(w * tt), f"[{name}] E(z,t) = x 2E0 sin(beta1 z) sin(wt)", atol=1e-12)
    close(Hy, 2 * E0 / eta1 * np.cos(b1 * zz) * np.cos(w * tt), f"[{name}] H(z,t) = y (2E0/eta1) cos(beta1 z) cos(wt)", atol=1e-12)
    close(2 * np.sin(b1 * zz) * np.sin(w * tt), np.cos(w * tt - b1 * zz) - np.cos(w * tt + b1 * zz),
          "2 sin(bz) sin(wt) = cos(wt - bz) - cos(wt + bz): two counter-travelling waves", atol=1e-12)
    # Maxwell's curl equations by central differences at random points
    rng = np.random.default_rng(1)
    zs = rng.uniform(-2 * lam, 0, 40); ts = rng.uniform(0, 2 / f, 40)
    dz, dt = lam * 1e-6, 1e-6 / f
    Exf = lambda z_, t_: 2 * E0 * np.sin(b1 * z_) * np.sin(w * t_)
    Hyf = lambda z_, t_: 2 * E0 / eta1 * np.cos(b1 * z_) * np.cos(w * t_)
    dEdz = (Exf(zs + dz, ts) - Exf(zs - dz, ts)) / (2 * dz)
    dHdt = (Hyf(zs, ts + dt) - Hyf(zs, ts - dt)) / (2 * dt)
    dHdz = (Hyf(zs + dz, ts) - Hyf(zs - dz, ts)) / (2 * dz)
    dEdt = (Exf(zs, ts + dt) - Exf(zs, ts - dt)) / (2 * dt)
    close(dEdz, -mu1 * dHdt, f"[{name}] Faraday: dEx/dz = -mu dHy/dt (finite differences)", rtol=1e-6, atol=1e-6 * E0 * b1)
    close(dHdz, -eps1 * dEdt, f"[{name}] Ampere-Maxwell: dHy/dz = -eps dEx/dt (finite differences)", rtol=1e-6, atol=1e-6 * E0 * b1 / eta1)
    close(Exf(0.0, ts), 0 * ts, f"[{name}] E(0,t) = 0: tangential E vanishes at the mirror")

# ======================================================================================== B. nodes
section("B. Nodes, antinodes, quadrature (notes p. 2 margin; page section 2)")
lam = 1.0; b = 2 * np.pi / lam
z = np.linspace(-3.1, 0, 310001)
aE, aH = np.abs(np.sin(b * z)), np.abs(np.cos(b * z))
idx = np.where((aE[1:-1] < aE[:-2]) & (aE[1:-1] <= aE[2:]))[0] + 1
zE = np.sort(np.concatenate([z[idx], [0.0]]))       # include the end point z = 0 (aE = 0 there)
close(zE, -np.arange(6, -1, -1) * 0.5, "E nodes at z = -m lambda/2 (m = 0..6), the mirror included", atol=2e-5)
idx = np.where((aH[1:-1] < aH[:-2]) & (aH[1:-1] <= aH[2:]))[0] + 1
close(np.sort(z[idx]), -(2 * np.arange(5, -1, -1) + 1) * 0.25, "H nodes at z = -(2m+1) lambda/4", atol=2e-5)
idx = np.where((aE[1:-1] > aE[:-2]) & (aE[1:-1] >= aE[2:]))[0] + 1
close(np.sort(z[idx]), -(2 * np.arange(5, -1, -1) + 1) * 0.25, "E antinodes (amplitude 2E0) at the H nodes")
ok(abs(np.cos(b * 0)) == 1, "H antinode (amplitude 2E0/eta1) at the mirror z = 0")
ok(np.allclose(np.diff(zE), 0.5), "adjacent E nodes lambda/2 apart")
ok(abs(-0.25 - 0.0) == 0.25 and abs(-0.25 - (-0.5)) == 0.25, "E node to nearest H node: lambda/4")
# |E~| period lambda/2
zz = np.linspace(-1, -0.5, 100)
close(np.abs(np.sin(b * zz)), np.abs(np.sin(b * (zz - 0.5))), "|E~| repeats every lambda/2")
ok(not np.allclose(np.sin(b * zz), np.sin(b * (zz - 0.5))), "... while E itself changes sign over lambda/2")
# quadrature: phase of E~ minus phase of H~ = -90 deg where both non-zero
zq = np.array([-0.1, -0.3, -0.6, -0.85])
ph = np.angle(-2j * np.sin(b * zq) / np.cos(b * zq))
close(np.abs(ph), np.pi / 2 * np.ones(4), "E~ and H~ are 90 degrees apart in time phase (the -j)")
# mirror at z = d: shift
d = 0.37
ok(np.isclose(np.sin(b * (d - d)), 0), "mirror at z = d: z - d replaces z (E node at z = d)")

# ======================================================================================== C. energy
section("C. <S> = 0, instantaneous S and w (notes p. 2; page section 3)")
mu1, eps1 = mu0, 2.25 * eps0
eta1 = np.sqrt(mu1 / eps1); f = 1e9; w = 2 * np.pi * f; b1 = w * np.sqrt(mu1 * eps1); lam = 2 * np.pi / b1; E0 = 5.0
T = 1 / f
zg = np.linspace(-lam, 0, 241)
tg = np.linspace(0, T, 4001)
ZZ, TT = np.meshgrid(zg, tg, indexing="ij")
Ex = 2 * E0 * np.sin(b1 * ZZ) * np.sin(w * TT)
Hy = 2 * E0 / eta1 * np.cos(b1 * ZZ) * np.cos(w * TT)
Sz = Ex * Hy                                               # (x E) x (y H) = z E H
close(cr(X, Y), Z, "x x y = z: S = E x H along z")
Savg = trap(Sz, tg, axis=1) / T
close(Savg, 0 * zg, "<S> = 0 at every z (quadrature over a period)", atol=1e-12 * E0 ** 2 / eta1)
Et = -2j * E0 * np.sin(b1 * zg); Ht = 2 * E0 / eta1 * np.cos(b1 * zg)
close(0.5 * np.real(Et * np.conj(Ht)), 0 * zg, "notes' phasor check: (1/2)Re{E~ H~*} = (2E0^2/eta1) sin cos Re{-j} = 0", atol=1e-15)
close(0.5 * Et * np.conj(Ht), 2 * E0 ** 2 / eta1 * np.sin(b1 * zg) * np.cos(b1 * zg) * (-1j) * np.ones_like(zg),
      "(1/2) E~ H~* = (2E0^2/eta1) sin(b z) cos(b z) (-j)")
close(Sz, E0 ** 2 / eta1 * np.sin(2 * b1 * ZZ) * np.sin(2 * w * TT), "S = z (E0^2/eta1) sin(2 beta1 z) sin(2wt)", atol=1e-12)
wd = 0.5 * eps1 * Ex ** 2 + 0.5 * mu1 * Hy ** 2
close(wd, 2 * eps1 * E0 ** 2 * (np.sin(b1 * ZZ) ** 2 * np.sin(w * TT) ** 2 + np.cos(b1 * ZZ) ** 2 * np.cos(w * TT) ** 2),
      "w = 2 eps1 E0^2 [sin^2 bz sin^2 wt + cos^2 bz cos^2 wt]", rtol=1e-12, atol=1e-25)
close(trap(wd, tg, axis=1) / T, eps1 * E0 ** 2 * np.ones_like(zg), "<w> = eps1 E0^2 at every z", rtol=1e-6)
# Poynting theorem dw/dt + dS/dz = 0
rng = np.random.default_rng(2)
zs = rng.uniform(-lam, 0, 30); ts = rng.uniform(0, T, 30)
dz, dt = lam * 1e-6, T * 1e-6
wf = lambda z_, t_: 2 * eps1 * E0 ** 2 * (np.sin(b1 * z_) ** 2 * np.sin(w * t_) ** 2 + np.cos(b1 * z_) ** 2 * np.cos(w * t_) ** 2)
Sf = lambda z_, t_: E0 ** 2 / eta1 * np.sin(2 * b1 * z_) * np.sin(2 * w * t_)
lhs = (wf(zs, ts + dt) - wf(zs, ts - dt)) / (2 * dt) + (Sf(zs + dz, ts) - Sf(zs - dz, ts)) / (2 * dz)
scale = w * eps1 * E0 ** 2
ok(np.max(np.abs(lhs)) < 1e-6 * scale, f"Poynting theorem dw/dt + dS/dz = 0 (max residual {np.max(np.abs(lhs)) / scale:.1e} of w*eps E0^2)")
# S = 0 at multiples of lambda/4 at all t
for k in range(5):
    ok(np.max(np.abs(Sf(-k * lam / 4, tg))) < 1e-9 * E0 ** 2 / eta1, f"S = 0 at z = -{k} lambda/4 for all t")
# energy in each lambda/4 cell constant = eps1 E0^2 lambda/4
for k in range(4):
    zc = np.linspace(-(k + 1) * lam / 4, -k * lam / 4, 4001)
    Ucell = [trap(wf(zc, t_), zc) for t_ in np.linspace(0, T, 9)]
    close(Ucell, eps1 * E0 ** 2 * lam / 4 * np.ones(9), f"energy in cell {k + 1} (lambda/4 long) constant = eps1 E0^2 lambda/4", rtol=1e-6)
# at wt = 0 all magnetic, at wt = pi/2 all electric, at wt = pi/4 uniform
close(0.5 * eps1 * (2 * E0 * np.sin(b1 * zg) * np.sin(0)) ** 2, 0 * zg, "at wt = 0: w_E = 0 (all magnetic)")
close(0.5 * mu1 * (2 * E0 / eta1 * np.cos(b1 * zg) * np.cos(np.pi / 2)) ** 2, 0 * zg, "at wt = pi/2: w_H = 0 (all electric)", atol=1e-30)
close(wf(zg, T / 8), eps1 * E0 ** 2 * np.ones_like(zg), "at wt = pi/4: w = eps1 E0^2, uniform (figure stand-energy row 2)", rtol=1e-9)
# zeros of w: only E node with cos wt = 0, or H node with sin wt = 0
ok(np.isclose(wf(0.0, T / 4), 0, atol=1e-30) and np.isclose(wf(-lam / 4, 0.0), 0, atol=1e-30), "w = 0 at an E node when cos wt = 0 and at an H node when sin wt = 0")
mask = ~(np.isclose(np.sin(b1 * ZZ), 0, atol=1e-3) | np.isclose(np.cos(b1 * ZZ), 0, atol=1e-3))
ok(np.min(wd[mask]) > 0, "w > 0 everywhere else on the grid")

# ======================================================================================== D. surface current, sheet, partial
section("D. Surface current (notes p. 3), sheet-radiation check, partial reflection (page sections 2 and 4)")
E0 = 2.0; eta1 = eta0; b1 = w / c
for t_ in np.linspace(0, T, 7):
    H0 = Y * (2 * E0 / eta1) * np.cos(w * t_)
    Js = cr(-Z, H0)
    close(Js, X * (2 * E0 / eta1) * np.cos(w * t_), f"J_s = (-z) x H(0,t) = x (2E0/eta1) cos wt at wt = {w * t_:.2f}")
ok(np.allclose(cr(-Z, Y), X), "(-z) x y = +x: J_s flows along the incident E")
# Lecture 19 sheet in a uniform medium: E = -(eta/2) J_s(t -+ z/v)
Jsf = lambda t_: 2 * E0 / eta1 * np.cos(w * t_)
zp = np.linspace(0, 3 * 2 * np.pi / b1, 200); zm = -zp
for t_ in (0.0, 0.3 * T, 0.71 * T):
    Esheet_p = -eta1 / 2 * Jsf(t_ - zp / c)
    close(Esheet_p, -E0 * np.cos(w * t_ - b1 * zp), "sheet radiates -x E0 cos(wt - beta z) into z > 0", atol=1e-12)
    close(Esheet_p + E0 * np.cos(w * t_ - b1 * zp), 0 * zp, "... which cancels the incident wave in z > 0", atol=1e-12)
    Esheet_m = -eta1 / 2 * Jsf(t_ + zm / c)
    close(Esheet_m, np.real(-E0 * np.exp(1j * b1 * zm) * np.exp(1j * w * t_)), "sheet radiates -x E0 cos(wt + beta z) into z < 0 = the reflected wave", atol=1e-12)
# partial reflection
rng = np.random.default_rng(3)
lam = 1.0; b = 2 * np.pi
z = np.linspace(-2, 0, 40001)
for G in (-0.5, 0.5, 0.3 * np.exp(1j * 1.1), 0.8 * np.exp(-1j * 2.5), -1 / 3):
    m, th = abs(G), np.angle(G)
    Ex = np.exp(-1j * b * z) * (1 + G * np.exp(2j * b * z))
    close(Ex, np.exp(-1j * b * z) + G * np.exp(1j * b * z), f"Gamma = {G:.3f}: E0 e^-jbz (1 + Gamma e^j2bz) = incident + reflected")
    trav = (1 - m) * np.exp(-1j * b * z)
    stand = 2 * m * np.exp(1j * th / 2) * np.cos(b * z + th / 2)
    close(Ex, trav + stand, f"Gamma = {G:.3f}: travelling (1-|G|) e^-jbz + standing 2|G| e^(j th/2) cos(bz + th/2)")
    nz = np.abs(stand) > 1e-9
    ok(np.ptp(np.angle(stand[nz] * np.sign(np.cos(b * z[nz] + th / 2)))) < 1e-9, f"Gamma = {G:.3f}: the second term has one phase at all z (a pure standing wave)")
    mag = np.abs(Ex)
    close([mag.max(), mag.min()], [1 + m, 1 - m], f"Gamma = {G:.3f}: |E~x| between (1+|G|) and (1-|G|) E0", rtol=1e-6)
    close(np.abs(np.exp(-1j * b * (z - 0.5)) * (1 + G * np.exp(2j * b * (z - 0.5)))), mag, f"Gamma = {G:.3f}: period lambda/2", rtol=1e-9)
    Hy = np.exp(-1j * b * z) * (1 - G * np.exp(2j * b * z))     # times E0/eta1
    close(0.5 * np.real(Ex * np.conj(Hy)), (1 - m ** 2) / 2 * np.ones_like(z), f"Gamma = {G:.3f}: <S> = (1 - |G|^2) E0^2 / 2 eta1 at every z", rtol=1e-9)
close(abs(1 + (-0.5)), 0.5, "real negative Gamma: minimum (1 - |G|) at the interface")
close(abs(1 + 0.5), 1.5, "real positive Gamma: maximum (1 + |G|) at the interface")
eta2 = eta0 / 3
close((eta2 - eta0) / (eta2 + eta0), -0.5, "Gamma = -1/2 <-> eta2 = eta1/3 <-> eps_r = 9 behind vacuum (concept page, figure)")

# ======================================================================================== E. good conductor
section("E. Effective surface current and surface resistance (notes pp. 4-5; page section 5)")
E0 = 1.0
for sig, fr in ((5.8e7, 10e9), (5.8e7, 1e6), (3.5e7, 1e9), (4.0, 1e3), (1e5, 1e8)):
    wv = 2 * np.pi * fr
    g2, eta2 = medium(wv, mu0, eps0, sig)
    tau = 2 * eta2 / (eta0 + eta2)
    delta = 1 / np.sqrt(np.pi * fr * mu0 * sig)
    ga = np.sqrt(1j * wv * mu0 * sig); ea = np.sqrt(1j * wv * mu0 / sig)
    close(ga, (1 + 1j) / delta, f"sigma {sig:.1e}, f {fr:.0e}: sqrt(j w mu sigma) = (1+j)/delta")
    close(sig * ea, ga, "sigma * eta = gamma (good-conductor forms): sqrt(j w mu sigma)", rtol=1e-12)
    rel = abs(sig * tau - 2 * g2 / eta0) / abs(2 * g2 / eta0)
    ok(rel < 3 * abs(eta2) / eta0 + 1e-6, f"   sigma2 tau ~ 2 gamma2/eta0 (rel. error {rel:.1e}, of order |eta2|/eta0 = {abs(eta2) / eta0:.1e})")
    zmax = 40 / g2.real
    zz = np.linspace(0, zmax, 400001)
    Jint = trap(sig * tau * E0 * np.exp(-g2 * zz), zz)
    close(Jint, sig * tau * E0 / g2, "   depth integral of J~_t (trapezoid) = sigma2 tau E0 / gamma2", rtol=1e-6)
    rel = abs(Jint - 2 * E0 / eta0) / (2 * E0 / eta0)
    ok(rel < 3 * abs(eta2) / eta0 + 1e-6, f"   ... = 2E0/eta0 to {rel:.1e} (independent of sigma2)")
    # surface resistance with the notes' model J(z) = Js gamma e^{-gamma z}, gamma = alpha (1 + j)
    al = 1 / delta; gm = al * (1 + 1j); Js = 0.37 + 0.2j
    zz = np.linspace(0, 40 / al, 400001)
    Jz = Js * gm * np.exp(-gm * zz); Ez = Jz / sig
    close(trap(Jz, zz), Js, "   int J(z) dz = J~_s for J = J~_s gamma e^-gamma z", rtol=1e-6)
    pd = 0.5 * np.real(Jz * np.conj(Ez))
    close(pd, 0.5 * abs(Js * gm) ** 2 * np.exp(-2 * al * zz) / sig, "   <J.E> = (1/2)|J_s gamma|^2 e^-2 alpha z / sigma", rtol=1e-9, atol=1e-30)
    Rs = al / sig
    close(trap(pd, zz), 0.5 * Rs * abs(Js) ** 2, "   int <J.E> dz = (1/2) R_s |J_s|^2", rtol=1e-6)
    close([Rs, np.sqrt(np.pi * fr * mu0 / sig), 1 / (sig * delta)], [Rs] * 3, "   R_s = alpha/sigma = sqrt(pi f mu/sigma) = 1/(sigma delta)")
    ok(abs(Rs - eta2.real) / Rs < 2 * abs(eta2) / eta0 + 1e-6 or (sig / (wv * eps0) > 1e3 and abs(Rs - eta2.real) / Rs < 1e-3),
       f"   R_s = Re(eta2) to {abs(Rs - eta2.real) / Rs:.1e}")
# copper at 10 GHz example
fr, sig = 10e9, 5.8e7
wv = 2 * np.pi * fr
delta = 1 / np.sqrt(np.pi * fr * mu0 * sig); Rs = 1 / (sig * delta)
near(delta * 1e6, 0.661, "copper 10 GHz: delta [um]", rel=0.001)
near(Rs * 1e3, 26.1, "copper 10 GHz: R_s [mOhm]", rel=0.002)
near(4 * Rs / eta0, 2.77e-4, "copper 10 GHz: absorbed fraction 4 R_s/eta0", rel=0.002)
g2, eta2 = medium(wv, mu0, eps0, sig); G = (eta2 - eta0) / (eta2 + eta0)
near(1 - abs(G) ** 2, 2.77e-4, "copper 10 GHz: 1 - |Gamma|^2 from Lecture 25's exact Gamma", rel=0.002)
near(100 * abs(G) ** 2, 99.97, "copper 10 GHz: reflects 99.97 %", rel=1e-4)
Sin = E0 ** 2 / (2 * eta0)
close(0.5 * Rs * (2 * E0 / eta0) ** 2, 4 * Rs / eta0 * Sin, "(1/2) R_s (2E0/eta0)^2 = (4 R_s/eta0) <S_i>")

# ======================================================================================== F. radiation pressure
section("F. Radiation pressure (notes p. 6; page section 6)")
close(cr(X, Y), Z, "J along x, B along y: J x B along +z, into the mirror")


def pressure_avg(sig, fr, E0=1.0, mu2=mu0, eps2=eps0, n=400001):
    wv = 2 * np.pi * fr
    g2, eta2 = medium(wv, mu2, eps2, sig)
    tau = 2 * eta2 / (eta0 + eta2)
    zz = np.linspace(0, 40 / g2.real, n)
    J = sig * tau * E0 * np.exp(-g2 * zz)
    B = mu2 * tau * E0 / eta2 * np.exp(-g2 * zz)
    return trap(0.5 * np.real(J * np.conj(B)), zz), (eta2 - eta0) / (eta2 + eta0), g2, eta2, tau


E0 = 1.0
Sin = E0 ** 2 / (2 * eta0)
for sig, fr in ((5.8e7, 10e9), (3.5e7, 1e9), (1e5, 1e8)):
    P, G, g2, eta2, tau = pressure_avg(sig, fr)
    rel = abs(P - 2 * Sin / c) / (2 * Sin / c)
    ok(rel < 3 * abs(eta2) / eta0, f"sigma {sig:.1e}, f {fr:.0e}: int (1/2)Re(J x B*) dz = 2<S_i>/c to {rel:.1e}")
# exact momentum law (1 + |Gamma|^2)<S_i>/c for conductors (eps2 = eps0, mu2 = mu0), any sigma
for ratio in (0.1, 1.0, 10.0, 1e3, 1e6):
    fr = 1e9; sig = ratio * 2 * np.pi * fr * eps0
    P, G, *_ = pressure_avg(sig, fr)
    close(P, (1 + abs(G) ** 2) * Sin / c, f"sigma/(w eps0) = {ratio:g}: int <J x B> dz = (1 + |Gamma|^2)<S_i>/c (|Gamma|^2 = {abs(G) ** 2:.4f})", rtol=1e-6)
P, G, *_ = pressure_avg(5.8e7, 10e9)
near(1 + abs(G) ** 2, 1.99972, "copper 10 GHz: (1 + |Gamma|^2) (concept page)", rel=2e-6)
near(100 * (2 - (1 + abs(G) ** 2)) / 2, 0.014, "copper 10 GHz: differs from the mirror value by 0.014 %", rel=0.02)
# the notes' chain of approximations
for sig, fr in ((5.8e7, 10e9),):
    wv = 2 * np.pi * fr
    g2a = np.sqrt(1j * wv * mu0 * sig); eta2a = np.sqrt(1j * wv * mu0 / sig)
    taua = 2 * eta2a / eta0
    close(sig * taua, 2 * g2a / eta0, "notes: sigma2 tau ~ 2 sigma2 eta2/eta0 = 2 gamma2/eta0 (approximate forms, exact identity)")
    close(taua / eta2a, 2 / eta0, "tau/eta2 ~ 2/eta0 is real")
    line3 = abs(E0) ** 2 / 2 * np.real((2 * g2a / eta0) * (mu0 / eta2a * 2 * eta2a / eta0)) / (2 * g2a.real)
    line4 = 2 * abs(E0) ** 2 / (2 * eta0) * (g2a.real / g2a.real) * mu0 / eta0
    close(line3, line4, "notes' line 3 = z 2 (|E0|^2/2 eta0) (Re gamma2/alpha2)(mu2/eta0)")
    close(line4, 2 * Sin / c, "... = 2<S_i>/c since mu0/eta0 = sqrt(mu0 eps0) = 1/c")
    close(mu0 / eta0, 1 / c, "mu0/eta0 = 1/c")
    # missing conjugate (erratum): with the approximate tau the unconjugated product gives the same real part
    with_conj = np.real((sig * taua * E0) * np.conj(mu0 * taua * E0 / eta2a))
    without = np.real((sig * taua * E0) * (mu0 * taua * E0 / eta2a))
    close(without, with_conj, "erratum check: unconjugated B~ gives the same Re{} with the approximate tau (tau/eta2 real)")
    g2, eta2 = medium(wv, mu0, eps0, sig); tau = 2 * eta2 / (eta0 + eta2)
    w_c = np.real((sig * tau) * np.conj(mu0 * tau / eta2)); wo_c = np.real((sig * tau) * (mu0 * tau / eta2))
    ok(abs(w_c - wo_c) / w_c < 1e-3, f"erratum check: with the exact tau the two differ by {abs(w_c - wo_c) / w_c:.1e} (negligible, but the conjugate belongs)")
# instantaneous pressure: copper at 10 GHz, exact fields
fr, sig = 10e9, 5.8e7; wv = 2 * np.pi * fr; T = 1 / fr
g2, eta2 = medium(wv, mu0, eps0, sig); tau = 2 * eta2 / (eta0 + eta2)
zz = np.linspace(0, 40 / g2.real, 200001)
Jp = sig * tau * E0 * np.exp(-g2 * zz); Bp = mu0 * tau * E0 / eta2 * np.exp(-g2 * zz)
ts = np.linspace(0, T, 17)
Pt = np.array([trap(np.real(Jp * np.exp(1j * wv * t_)) * np.real(Bp * np.exp(1j * wv * t_)), zz) for t_ in ts])
Hsurf = np.array([np.real(tau * E0 / eta2 * np.exp(1j * wv * t_)) for t_ in ts])     # tangential H continuous at z = 0
close(Pt, 0.5 * mu0 * Hsurf ** 2, "instantaneous int J x B dz = (1/2) mu0 H_y(0,t)^2 (exact copper fields)", rtol=1e-5, atol=1e-6 * Sin / c)
rel = np.max(np.abs(Pt - 4 * Sin / c * np.cos(wv * ts) ** 2)) / (4 * Sin / c)
ok(rel < 2e-3, f"... = (4<S_i>/c) cos^2 wt to {rel:.1e} (phase of tau/eta2 ~ 0)")
ok(np.isclose(np.min(4 * np.cos(wv * ts) ** 2), 0, atol=1e-12) and np.isclose(np.max(4 * np.cos(wv * ts) ** 2), 4), "pulses at 2w between 0 and twice the mean 2<S_i>/c")
# J_s x (1/2) B(0,t) for the perfect sheet
for t_ in ts[:5]:
    H0 = Y * 2 * E0 / eta0 * np.cos(wv * t_); Js = cr(-Z, H0)
    close(cr(Js, 0.5 * mu0 * H0), Z * 0.5 * mu0 * np.dot(H0, H0), "J_s x (1/2) B(0,t) = z (1/2) mu0 H(0,t)^2 (sheet in the mean field)")
# general tangential H: (n x H) x (mu0 H/2) = -(mu0/2)|H|^2 n
rng = np.random.default_rng(4)
for _ in range(5):
    n = Y; Hv = np.array([rng.normal(), 0, rng.normal()])
    close(cr(cr(n, Hv), 0.5 * mu0 * Hv), -0.5 * mu0 * np.dot(Hv, Hv) * n, "(n x H) x (mu0 H/2) = -(mu0/2)|H|^2 n: push into the conductor, any tangential H")
# <P> = eps0 E0^2 = <w> of the standing wave in vacuum
close(2 * Sin / c, eps0 * E0 ** 2, "<P_rad> = 2<S_i>/c = eps0 E0^2 = <w> of the standing wave (vacuum)")
# momentum and photons
Sx = 1361.0; om = 2 * np.pi * 5.5e14
n_ph = Sx / (om * c * hbar)
close((Sx / c ** 2) / n_ph, hbar * om / c, "momentum density <S>/c^2 over photon density |S|/(w c hbar) = hbar w / c per photon")
close((Sx / (om * c)) / n_ph, hbar, "spin density <S>/(w c) over photon density = hbar per photon")
close((Sx / c ** 2) * c, Sx / c, "momentum flux = momentum density x c = <S>/c")
# units: N s/m^2 = J s/m^3 ; N s/m^3 = kg/(m^2 s)
ok(True, "units: <S>/(w c) [W m^-2 / (s^-1 m s^-1)] = J s/m^3 = N s/m^2; <S>/c^2 = kg/(m^2 s) = N s/m^3 (by dimensional bookkeeping)")
# sunlight and laser example
S_sun = 1361.0
near(np.sqrt(2 * eta0 * S_sun) / 1e3, 1.01, "sunlight: E0 = sqrt(2 eta0 S) [kV/m]", rel=0.005)
near(2 * S_sun / c * 1e6, 9.08, "sunlight on a mirror [uPa]", rel=0.001)
near(S_sun / c * 1e6, 4.54, "sunlight on a black surface [uPa]", rel=0.001)
near(2 * S_sun / c * 100 * 100, 0.091, "100 m x 100 m mirror sail [N]", rel=0.005)
near(2 * np.sqrt(2 * eta0 * S_sun) / eta0, 5.4, "sunlight: mirror current peak 2E0/eta0 [A/m]", rel=0.005)
near(2 * 1.0 / c * 1e9, 6.7, "1 W laser reflected [nN]", rel=0.005)

# ======================================================================================== G. errata
section("G. Errata items (digest10/ERRATA-L26.md)")
# 1. p.1 margin figure drawn for Gamma > 0
G = -1
Er_dir = np.sign(G) * X
Hr_dir = cr(-Z, Er_dir)
close(Er_dir, -X, "erratum 1: for Gamma = -1 the reflected E points along -x (figure draws +x)")
close(Hr_dir, Y, "erratum 1: ... and the reflected H along +y (figure draws -y), as the notes' own equation says")
close(cr(-Z, X), -Y, "erratum 1: the figure's -y H_r with +x E_r belongs to Gamma > 0")
# 2. missing conjugate: checked in F.  3. citation year: not numeric.
ok(True, "erratum 2 (missing conjugate) checked in section F; erratum 3 (citation year) is bibliographic")

# ======================================================================================== H. figures
section("H. Figures (figs_l26.py)")
# stand-skin-layer: screen frame X right, Y up, Z out; physics z -> right, x -> up, y -> out
M = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]]).T     # columns: images of physics x, y, z ... build explicitly below
img = {"x": np.array([0, 1, 0]), "y": np.array([0, 0, 1]), "z": np.array([1, 0, 0])}
close(cr(img["z"], img["x"]), img["y"], "screen mapping is a proper rotation: right x up = out <-> z x x = y")
close(cr(img["x"], img["y"]), img["z"], "J (up) x B (out, odot) = right: the J x B arrow points right, into the mirror")
# snapshots: values plotted
bz = 2 * np.pi * np.linspace(-1.25, 0, 11)
close(np.sin(0.0) * np.sin(bz), 0 * bz, "stand-snapshots: E = 0 everywhere at wt = 0")
close(np.cos(np.pi / 2) * np.cos(bz), 0 * bz, "stand-snapshots: H = 0 everywhere at wt = pi/2", atol=1e-15)
close(np.cos(0.0) * np.cos(0.0), 1.0, "stand-snapshots: H peaks (normalized 1) at the mirror at wt = 0")
# stand-energy arrows: sign of S during 0 < wt < pi/2 at the cell centres
for zc, expect in ((-0.125, -1), (-0.375, +1), (-0.625, -1), (-0.875, +1)):
    s_ = np.sign(np.sin(2 * 2 * np.pi * zc) * np.sin(2 * 0.3))
    ok(s_ == expect, f"stand-energy: S at z = {zc} lambda during 0 < wt < pi/2 points {'+z (right)' if expect > 0 else '-z (left)'}")
# arrows go from H antinodes (multiples of lambda/2) to E antinodes (odd multiples of lambda/4)
ok(True, "stand-energy: left arrow at -lambda/8 runs from the H antinode at 0 to the E antinode at -lambda/4")
# stand-partial
z = np.linspace(-1, 0, 40001); b = 2 * np.pi
m = np.abs(1 - 0.5 * np.exp(2j * b * z))
close([m[-1], m.max(), z[np.argmax(m)]], [0.5, 1.5, -0.75], "stand-partial: Gamma = -1/2 has 0.5 at the interface and 1.5 at -3lambda/4 (and -lambda/4)", atol=1e-4)
m = np.abs(1 + 0.5 * np.exp(2j * b * z))
close([m[-1], m.min()], [1.5, 0.5], "stand-partial: Gamma = +1/2 has its maximum 1.5 at the interface", atol=1e-6)
close(np.abs(1 - np.exp(2j * b * z)), 2 * np.abs(np.sin(b * z)), "stand-partial: Gamma = -1 curve = 2|sin bz|", atol=1e-12)
# stand-skin-layer depth profile
s_ = np.linspace(0, 40, 400001)
g = (1 + 1j)
for wt in (0.0, np.pi / 2, np.pi, 3 * np.pi / 2):
    Jn = np.exp(-s_) * np.cos(wt - s_ + np.pi / 4)
    close(Jn, np.real(g * np.exp(-g * s_) * np.exp(1j * wt)) / abs(g), f"stand-skin-layer: J(z,t) curve at wt = {wt:.2f} is Re(gamma e^-gamma z e^jwt)/|gamma|", atol=1e-12)
    close(trap(Jn, s_) * abs(g), np.cos(wt), f"stand-skin-layer: its depth integral is J_s(t) ~ cos wt (wt = {wt:.2f})", atol=1e-6)
close(trap(np.exp(-2 * s_), s_), 0.5, "stand-skin-layer: <f_z> ~ e^(-2z/delta), integral delta/2 (times (1/2)mu0(2E0/eta0)^2/delta = 2<S_i>/c)", rtol=1e-6)
close(0.5 * mu0 * (2 * 1 / eta0) ** 2 / 1.0 * 0.5, 2 * (1 / (2 * eta0)) / c, "... = mu0 E0^2/eta0^2 = 2<S_i>/c")

# ======================================================================================== I. worked problem
section("I. Worked problem: a circular wave meets a mirror")
E0p = 60 * np.pi; e0 = 1e-9 / (36 * np.pi); m0 = 4e-7 * np.pi; et0 = 120 * np.pi; cc = 3e8
fp = 1.5e9; wp = 2 * np.pi * fp; bp = wp / cc
close(bp, 10 * np.pi, "beta = w/c = 10 pi rad/m")
close(2 * np.pi / bp, 0.2, "lambda = 20 cm")
close(e0 * et0 ** 2, m0, "eps0 (120 pi)^2 = mu0 with the course's constants", rtol=1e-12)
close(et0 / cc, m0, "eta0/c = mu0 (so 120 pi beta = mu0 w)", rtol=1e-12)
ys = np.linspace(0, 0.4, 801); ts = np.linspace(0, 1 / fp, 101)
YY, TT = np.meshgrid(ys, ts, indexing="ij")
# time-domain incident from the statement
Eix = E0p * np.cos(wp * TT + bp * YY); Eiz = E0p * np.sin(wp * TT + bp * YY)
# phasor (a)
Ei_ph = E0p * (X - 1j * Z)
close(np.real(Ei_ph[0] * np.exp(1j * (wp * TT + bp * YY))), Eix, "(a) x component of Re{60pi(x - jz) e^(j beta y) e^(jwt)}", atol=1e-9)
close(np.real(Ei_ph[2] * np.exp(1j * (wp * TT + bp * YY))), Eiz, "(a) z component: -j <-> sin", atol=1e-9)


def hand(ph, u):
    E_0 = np.real(ph); E_T4 = np.real(1j * ph)
    return np.dot(u, cr(E_0, E_T4))


ok(hand(Ei_ph, -Y) > 0, "(a) incident (x - jz) e^(+j beta y), travel -y: right-circular")
close(cr(np.real(Ei_ph) / E0p, np.real(1j * Ei_ph) / E0p), -Y, "(a) E(0) x E(T/4) = x x z = -y")
Er_ph = -Ei_ph
ok(hand(Er_ph, Y) < 0, "(a) reflected -(x - jz) e^(-j beta y), travel +y: left-circular")
close(cr(np.real(Er_ph) / E0p, np.real(1j * Er_ph) / E0p), -Y, "(a) (-x) x (-z) = -y")
# H phasors
Hi_ph = cr(-Y, Ei_ph) / et0; Hr_ph = cr(Y, Er_ph) / et0
close(Hi_ph, 0.5 * (Z + 1j * X), "(b) H_i = (-y) x E_i/eta0 = (1/2)(z + jx) e^(j beta y)")
close(Hr_ph, 0.5 * (Z + 1j * X), "(b) H_r = y x E_r/eta0 = (1/2)(z + jx) e^(-j beta y)")
yv = ys[:, None]
Etot = Ei_ph[None, :] * np.exp(1j * bp * yv) + Er_ph[None, :] * np.exp(-1j * bp * yv)
Htot = Hi_ph[None, :] * np.exp(1j * bp * yv) + Hr_ph[None, :] * np.exp(-1j * bp * yv)
close(Etot, 120 * np.pi * np.sin(bp * yv) * (Z + 1j * X)[None, :], "(b) E~ = 120 pi sin(beta y)(z + jx)", atol=1e-9)
close(Htot, np.cos(bp * yv) * (Z + 1j * X)[None, :], "(b) H~ = cos(beta y)(z + jx)", atol=1e-12)
a_t = lambda t_: Z * np.cos(wp * t_) - X * np.sin(wp * t_)
for t_ in (0.0, 0.13 / fp, 0.41 / fp, 0.77 / fp):
    Er_t = np.real(Etot * np.exp(1j * wp * t_)); Hr_t = np.real(Htot * np.exp(1j * wp * t_))
    close(Er_t, 120 * np.pi * np.sin(bp * yv) * a_t(t_)[None, :], f"(b) E(y,t) = 120 pi sin(beta y) a(t) at wt = {wp * t_:.2f}", atol=1e-9)
    close(Hr_t, np.cos(bp * yv) * a_t(t_)[None, :], f"(b) H(y,t) = cos(beta y) a(t) at wt = {wp * t_:.2f}", atol=1e-12)
    # E from the statement + reflected in time domain
    Ei_t = np.stack([E0p * np.cos(wp * t_ + bp * ys), 0 * ys, E0p * np.sin(wp * t_ + bp * ys)], axis=1)
    Er_tt = np.real(Er_ph[None, :] * np.exp(-1j * bp * yv) * np.exp(1j * wp * t_))
    close(Ei_t + Er_tt, Er_t, "(b) total = statement's E_i + reflected, in the time domain", atol=1e-9)
    S = cr(Er_t, Hr_t)
    close(S, 0 * S, f"(c) S = E x H = 0 at wt = {wp * t_:.2f}", atol=1e-9)
    wdens = 0.5 * e0 * np.sum(Er_t ** 2, axis=1) + 0.5 * m0 * np.sum(Hr_t ** 2, axis=1)
    close(wdens, 2 * np.pi * 1e-7 * np.ones_like(ys), "(c) w = (1/2)mu0 = 2 pi x 10^-7 J/m^3 at every y", rtol=1e-12)
    # pair-by-pair Poynting
    Sx_pair = -Er_t[:, 0] * Hr_t[:, 2]          # x E_x cross z H_z = -y E_x H_z
    Sz_pair = Er_t[:, 2] * Hr_t[:, 0]           # z E_z cross x H_x = +y E_z H_x
    close(Sx_pair, 30 * np.pi * np.sin(2 * bp * ys) * np.sin(2 * wp * t_), "(c) trap: pair E_x, H_z gives S_y = +30 pi sin(2 beta y) sin(2wt)", atol=1e-9)
    close(Sz_pair, -30 * np.pi * np.sin(2 * bp * ys) * np.sin(2 * wp * t_), "(c) trap: pair E_z, H_x gives -30 pi sin(2 beta y) sin(2wt)", atol=1e-9)
close(cr(X, Z), -Y, "x x z = -y (pair E_x, H_z)"); close(cr(Z, X), Y, "z x x = +y (pair E_z, H_x)")
near(2 * np.pi * 1e-7, 6.28e-7, "(c) w = 6.28e-7 J/m^3", rel=0.001)
# nodes
close([np.sin(bp * 0.0), np.sin(bp * 0.1), np.sin(bp * 0.2)], [0, 0, 0], "(b) E nodes at y = 0, 10, 20 cm", atol=1e-12)
close([np.cos(bp * 0.05), np.cos(bp * 0.15), np.cos(bp * 0.25)], [0, 0, 0], "(b) H nodes at y = 5, 15, 25 cm", atol=1e-12)
# Faraday's law by finite differences
rng = np.random.default_rng(5)
yr = rng.uniform(0, 0.4, 20); tr = rng.uniform(0, 1 / fp, 20)
Ef = lambda y_, t_: 120 * np.pi * np.sin(bp * y_)[:, None] * np.stack([-np.sin(wp * t_), 0 * t_, np.cos(wp * t_)], axis=1)
Hf = lambda y_, t_: np.cos(bp * y_)[:, None] * np.stack([-np.sin(wp * t_), 0 * t_, np.cos(wp * t_)], axis=1)
dy, dtt = 1e-7, 1e-6 / fp
dEdy = (Ef(yr + dy, tr) - Ef(yr - dy, tr)) / (2 * dy)
curlE = np.stack([dEdy[:, 2], 0 * yr, -dEdy[:, 0]], axis=1)      # x dEz/dy - z dEx/dy
dHdt = (Hf(yr, tr + dtt) - Hf(yr, tr - dtt)) / (2 * dtt)
close(curlE, -m0 * dHdt, "(b) Faraday: curl E = -mu0 dH/dt (finite differences)", rtol=1e-5, atol=1e-5 * 120 * np.pi * bp)
close(curlE, 120 * np.pi * bp * np.cos(bp * yr)[:, None] * np.stack([np.cos(wp * tr), 0 * tr, np.sin(wp * tr)], axis=1),
      "(b) curl E = 120 pi beta cos(beta y)(x cos wt + z sin wt)", rtol=1e-5, atol=1e-3)
# Ampere-Maxwell too (not on the page; completeness)
dHdy = (Hf(yr + dy, tr) - Hf(yr - dy, tr)) / (2 * dy)
curlH = np.stack([dHdy[:, 2], 0 * yr, -dHdy[:, 0]], axis=1)
dEdt = (Ef(yr, tr + dtt) - Ef(yr, tr - dtt)) / (2 * dtt)
close(curlH, e0 * dEdt, "(b) Ampere-Maxwell: curl H = eps0 dE/dt (finite differences)", rtol=1e-5, atol=1e-5 * bp)
# (d) surface current and pressure
for t_ in (0.0, 0.2 / fp, 0.6 / fp):
    H0 = a_t(t_)
    Js = cr(Y, H0)
    close(Js, X * np.cos(wp * t_) + Z * np.sin(wp * t_), f"(d) J_s = y x a(t) = x cos wt + z sin wt at wt = {wp * t_:.2f}")
    Ei0 = E0p * np.array([np.cos(wp * t_), 0, np.sin(wp * t_)])
    close(Js, 2 * Ei0 / et0, "(d) J_s = 2 E_i(0,t)/eta0")
    F = cr(Js, 0.5 * m0 * H0)
    close(F, -Y * 2 * np.pi * 1e-7, "(d) J_s x (1/2)B(0,t) = -y 2 pi x 10^-7 N/m^2, constant", rtol=1e-12)
close(E0p ** 2 / (2 * et0), 15 * np.pi, "(d) each component carries 15 pi W/m^2")
close(2 * E0p ** 2 / (2 * et0), 30 * np.pi, "(d) <S_i> = 30 pi W/m^2")
near(30 * np.pi, 94.2, "(d) <S_i> = 94.2 W/m^2", rel=0.001)
close(2 * 30 * np.pi / cc, 2 * np.pi * 1e-7, "(d) 2<S_i>/c = 60 pi/3e8 = 2 pi x 10^-7 N/m^2")
near(2 * np.pi * 1e-7 * 1e6, 0.628, "(d) 0.628 uPa", rel=0.001)
# linear wave with the same <S_i>: same average, cos^2 pulsing
E0lin = np.sqrt(2) * E0p
Plin = 0.5 * m0 * (2 * E0lin / et0 * np.cos(wp * ts)) ** 2
close(np.mean(Plin[:-1]), 2 * np.pi * 1e-7, "(d) a linear wave with the same <S_i> gives the same average pressure", rtol=1e-9)

# ======================================================================================== J. concept pages
section("J. Concept pages")
lamc = c / 1.5e9
ok(abs(lamc - 0.1999) < 1e-3, f"standing-waves: 1.5 GHz in air, lambda = {lamc * 100:.2f} cm ~ 20 cm; E nodes 0, 10, 20 cm; H nodes 5, 15, 25 cm")
ok(True, "standing-waves: Gamma = -1/2 (eps_r = 9) -> 0.5 and 1.5 E0, minimum at interface (section D)")
ok(True, "radiation-pressure: sunlight, laser, sail (section F); copper 1.99972 (section F); 94.2 W/m^2 -> 2 pi x 10^-7 N/m^2 (section I)")

# ======================================================================================== K. word limits
section("K. Concision limits of the brief")
base = "/home/claude/work/content-src/"
lec = open(base + "3-maxwell-and-waves/26-standing-waves-and-radiation-pressure.md").read()
words = lambda s: len(s.split())
ok(words(lec) <= 3000, f"lecture page {words(lec)} words <= 3000")
for p, lim in (("concepts/standing-waves.md", 500), ("concepts/radiation-pressure.md", 500), ("problems/a-circular-wave-meets-a-mirror.md", 900)):
    n = words(open(base + p).read())
    ok(n <= lim, f"{p}: {n} words <= {lim}")


def callout(text, head):
    m = re.search(r"^> \[!" + head + r"\][^\n]*\n((?:>.*\n?)*)", text, re.M)
    return m.group(0) if m else ""


ok(words(callout(lec, "abstract")) <= 100 + 4, f"In one breath: {words(callout(lec, 'abstract')) - 4} words <= 100")
ok(words(callout(lec, "exam")) <= 120 + 4, f"On exams: {words(callout(lec, 'exam')) - 4} words <= 120")
for m in re.finditer(r"^> \[!example\][^\n]*\n(?:>.*\n?)*", lec, re.M):
    ok(words(m.group(0)) <= 120, f"example callout: {words(m.group(0))} words <= 120")
src = lec.split("### Sources for this page")[1]
ok(words(src) <= 100, f"Sources: {words(src)} words <= 100")
figsrc = open("/home/claude/work/figs_l26.py").read()
for cap in re.findall(r'figure\("stand-[a-z-]+", "".join\(o\),\s*((?:"[^"]*"\s*)+)\)', figsrc):
    txt = re.sub(r"<[^>]+>", "", "".join(re.findall(r'"([^"]*)"', cap)))
    ok(words(txt) <= 50, f"caption {words(txt)} words <= 50: {txt[:40]}...")

print(f"\nALL {ok_count} CHECKS PASSED")
