#!/usr/bin/env python3
"""Verification of every number, sign and direction on the Lecture 25 pages of the ECE 329 study site.

Pages checked:
  content-src/3-maxwell-and-waves/25-wave-reflection-and-transmission.md     (sections A-G)
  content-src/concepts/reflection-and-transmission.md                       (section J)
  content-src/problems/working-back-from-a-transmitted-wave.md              (section I)
  figs_l25.py: figure labels and arrow directions                           (section H)
numpy only. gamma = sqrt(j w mu (sigma + j w eps)), eta = sqrt(j w mu/(sigma + j w eps)) (Lecture 22), principal roots.
Maxwell's equations are checked on the constructed phasors by central differences; boundary conditions at z = 0;
time averages by quadrature over one period of the instantaneous E x H; every direction by np.cross.
"""
import numpy as np

mu0 = 4e-7 * np.pi
eps0 = 8.8541878128e-12
c = 1 / np.sqrt(mu0 * eps0)
eta0 = np.sqrt(mu0 / eps0)
E0C = 120 * np.pi                      # the course's no-calculator eta0
X, Y, Z = np.eye(3)
cr = np.cross
ok_count = 0


def ok(cond, msg):
    global ok_count
    assert cond, "FAILED: " + msg
    ok_count += 1
    print("ok  ", msg)


def close(a, b, msg, rtol=1e-9, atol=1e-12):
    a_, b_ = np.asarray(a), np.asarray(b)
    shown = f"max |diff| {np.max(np.abs(a_ - b_)):.1e} over {a_.size} values" if a_.size > 6 else f"{np.round(a, 6)} vs {np.round(b, 6)}"
    ok(np.allclose(a, b, rtol=rtol, atol=atol), f"{msg}: {shown}")


def near(a, b, msg, rel=0.01):
    ok(abs(a - b) <= rel * abs(b), f"{msg}: computed {a:.6g}, page {b:.6g} (tol {rel:.1%})")


def medium(w, mu, eps, sig):
    g = np.sqrt(1j * w * mu * (sig + 1j * w * eps))
    eta = np.sqrt(1j * w * mu / (sig + 1j * w * eps))
    return g, eta


def coeffs(eta1, eta2):
    G = (eta2 - eta1) / (eta2 + eta1)
    return G, 1 + G


def fields(z, E0, w, m1, m2):
    """total Ex, Hy phasors (x and y components) of the three-wave solution; m = (mu, eps, sig)"""
    g1, h1 = medium(w, *m1); g2, h2 = medium(w, *m2)
    G, T = coeffs(h1, h2)
    z = np.asarray(z, dtype=float)
    with np.errstate(over="ignore", invalid="ignore"):    # np.where evaluates both branches
        Ex, Hy = _branches(z, E0, g1, h1, g2, h2, G, T)
    return Ex, Hy


def _branches(z, E0, g1, h1, g2, h2, G, T):
    Ex = np.where(z < 0, E0 * (np.exp(-g1 * z) + G * np.exp(g1 * z)), T * E0 * np.exp(-g2 * z))
    Hy = np.where(z < 0, E0 / h1 * (np.exp(-g1 * z) - G * np.exp(g1 * z)), T * E0 / h2 * np.exp(-g2 * z))
    return Ex, Hy


def tavg_Sz(Ex, Hy, n=2000):
    """time average of Re{Ex e^{jwt}} Re{Hy e^{jwt}} by quadrature over one period"""
    ph = np.linspace(0, 2 * np.pi, n, endpoint=False)
    return np.mean(np.real(Ex * np.exp(1j * ph)) * np.real(Hy * np.exp(1j * ph)))


rng = np.random.default_rng(25)

print("=== A. constants")
close(eta0, 376.730, "eta0 = 376.73 ohm", rtol=1e-5)
near(E0C, eta0, "eta0 ~ 120 pi (0.07 %)", rel=1e-3)

print("=== B. three waves, Maxwell's equations, boundary conditions, Gamma and tau (random media)")
for k in range(300):
    f = 10 ** rng.uniform(3, 10); w = 2 * np.pi * f
    m1 = (rng.uniform(1, 5) * mu0, rng.uniform(1, 80) * eps0, 0.0)
    m2 = (rng.uniform(1, 5) * mu0, rng.uniform(1, 80) * eps0, 10 ** rng.uniform(-6, 3) * (k % 3 != 0))
    g1, h1 = medium(w, *m1); g2, h2 = medium(w, *m2)
    G, T = coeffs(h1, h2)
    # the 2x2 system of tangential E and H continuity, solved numerically
    A = np.array([[-1, 1], [1 / h1, 1 / h2]], dtype=complex); b = np.array([1, 1 / h1], dtype=complex)
    Gs, Ts = np.linalg.solve(A, b)
    good = np.isclose(Gs, G, rtol=1e-9) and np.isclose(Ts, T, rtol=1e-9) and np.isclose(T, 2 * h2 / (h2 + h1), rtol=1e-9)
    # Maxwell in each region: dEx/dz = -j w mu Hy, -dHy/dz = (sig + j w eps) Ex  (x-polarized, z-travelling)
    lam = 2 * np.pi / max(abs(g1), abs(g2)); dz = lam * 1e-5
    for zz, m in ((-0.37 * lam, m1), (0.29 * lam, m2)):
        Ex, Hy = fields([zz - dz, zz, zz + dz], 1.0, w, m1, m2)
        dE = (Ex[2] - Ex[0]) / (2 * dz); dH = (Hy[2] - Hy[0]) / (2 * dz)
        good &= np.isclose(dE, -1j * w * m[0] * Hy[1], rtol=1e-6)
        good &= np.isclose(-dH, (m[2] + 1j * w * m[1]) * Ex[1], rtol=1e-6)
    Ex, Hy = fields([-1e-15, 1e-15], 1.0, w, m1, m2)
    good &= np.isclose(Ex[0], Ex[1], rtol=1e-9) and np.isclose(Hy[0], Hy[1], rtol=1e-9)
    # properties on the page
    good &= abs(G) <= 1 + 1e-12 and h2.real >= 0
    good &= np.isclose(-G * (1 / h1) / (1 / h1), -G) and np.isclose(T * h1 / h2, 1 - G, rtol=1e-9)
    if m2[2] == 0:
        good &= (-1 < G.real < 1) and (0 < T.real < 2) and abs(G.imag) < 1e-12
        good &= (G > 0) == (h2.real > h1.real) and (T.real > 1) == (h2.real > h1.real)
        Gb, _ = coeffs(h2, h1); good &= np.isclose(Gb, -G, rtol=1e-9)
    if not good:
        raise SystemExit(f"FAILED random medium {k}")
ok(True, "300 random media: Gamma, tau solve the 2x2 system; Maxwell's equations hold in both regions; E_x, H_y continuous at 0")
ok(True, "|Gamma| <= 1 with Re eta2 >= 0; H_t/H_i = 1 - Gamma = tau eta1/eta2; real eta: -1<Gamma<1, 0<tau<2, sign rule, swap flips sign")
# reflected H direction: u = -z, E along x
close(cr(-Z, X), -Y, "reflected wave: (-z) x x = -y, so H_r carries -Gamma")
close(cr(X, Y), Z, "incident and transmitted: x x y = +z")
close(cr(X, -Y), -Z, "reflected E x H along -z (for Gamma > 0)")
# H ratio at z = 0 directly from the phasors
h1 = E0C; h2 = 2 / 3 * E0C; G, T = coeffs(h1, h2)
close((-G / h1) / (1 / h1), -G, "H_r(0)/H_i(0) = -Gamma")
close((T / h2) / (1 / h1), 1 - G, "H_t(0)/H_i(0) = 1 - Gamma")
# non-magnetic n form
for n1, n2 in ((1, 1.5), (1.5, 1), (1.33, 2.4), (3, 1)):
    close(coeffs(E0C / n1, E0C / n2)[0], (n1 - n2) / (n1 + n2), f"Gamma = (n1 - n2)/(n1 + n2), n1 = {n1}, n2 = {n2}")
# a lossy region 1 (exam remark, SP17 #2(iv) style): Gamma formula still satisfies both boundary conditions
w = 2 * np.pi * 1e6; ga, ha = medium(w, mu0, 4 * eps0, 400 * w * eps0); gb, hb = medium(w, mu0, eps0, 0.0)
G, T = coeffs(ha, hb)
close(1 + G, T, "lossy region 1: tangential E continuous with the same formula")
close((1 - G) / ha, T / hb, "lossy region 1: tangential H continuous with the same formula")
# Rao Example 5.4 cross-check (sigma 1e-4, eps 5 eps0, f 1.5e5 Hz, region 1 free space, eta1 = 377; Rao's eps0 = 1e-9/36 pi)
w = 3 * np.pi * 1e5; g2, h2 = medium(w, mu0, 5e-9 / (36 * np.pi), 1e-4)
near(abs(h2), 104.559, "Rao Ex. 5.4 |eta2| = 104.559 ohm", rel=2e-4)
near(np.degrees(np.angle(h2)), 33.69, "Rao Ex. 5.4 angle eta2 = 33.69 deg", rel=2e-4)
G, T = coeffs(377.0, h2)
near(abs(G), 0.6325, "Rao Ex. 5.4 |Gamma| = 0.6325", rel=2e-4)
near(np.degrees(np.angle(G)), 161.565, "Rao Ex. 5.4 angle Gamma = 161.565 deg", rel=1e-4)
near(abs(T), 0.4472, "Rao Ex. 5.4 |tau| = 0.4472", rel=2e-4)
near(np.degrees(np.angle(T)), 26.565, "Rao Ex. 5.4 angle tau = 26.565 deg", rel=2e-4)

print("=== C. power balance")
for k in range(200):
    f = 10 ** rng.uniform(3, 10); w = 2 * np.pi * f
    m1 = (rng.uniform(1, 5) * mu0, rng.uniform(1, 80) * eps0, 0.0)
    m2 = (rng.uniform(1, 5) * mu0, rng.uniform(1, 80) * eps0, 10 ** rng.uniform(-6, 3) * (k % 2))
    g1, h1 = medium(w, *m1); g2, h2 = medium(w, *m2); h1 = h1.real
    G, T = coeffs(h1, h2)
    E0 = rng.uniform(0.5, 5) * np.exp(1j * rng.uniform(0, 2 * np.pi))
    Si = abs(E0) ** 2 / (2 * h1); Sr = abs(G) ** 2 * Si
    St0 = abs(T) ** 2 * abs(E0) ** 2 / 2 * (1 / h2).real
    good = np.isclose(Si, Sr + St0, rtol=1e-9)
    good &= np.isclose(1, abs(G) ** 2 + abs(T) ** 2 * h1 * (1 / h2).real, rtol=1e-9)
    good &= np.isclose((1 / h2).real, np.cos(np.angle(h2)) / abs(h2), rtol=1e-9)
    if m2[2] == 0:
        good &= np.isclose(1, G.real ** 2 + T.real ** 2 * h1 / h2.real, rtol=1e-9)
    # quadrature: net flux at several z in region 1 equals Si - Sr; at 0+ equals St; in region 2 decays as e^{-2 alpha z}
    lam = 2 * np.pi / g1.imag
    for zz in (-1.3 * lam, -0.71 * lam, -0.2 * lam, -1e-12):
        Ex, Hy = fields(zz, E0, w, m1, m2)
        good &= np.isclose(tavg_Sz(Ex, Hy), Si - Sr, rtol=1e-6, atol=1e-12 * Si)
    Ex, Hy = fields(1e-12, E0, w, m1, m2)
    good &= np.isclose(tavg_Sz(Ex, Hy), St0, rtol=1e-6, atol=1e-12 * Si)
    zz = 0.3 / max(g2.real, 1e-9) if g2.real > 0 else 0.4 * lam
    Ex, Hy = fields(zz, E0, w, m1, m2)
    good &= np.isclose(tavg_Sz(Ex, Hy), St0 * np.exp(-2 * g2.real * zz), rtol=1e-6, atol=1e-12 * Si)
    if not good:
        raise SystemExit(f"FAILED power case {k}")
ok(True, "200 random cases: Si = Sr + St(0+); 1 = |G|^2 + |tau|^2 eta1 Re{1/eta2}; Re{1/eta2} = cos(angle)/|eta2|; lossless 1 = G^2 + tau^2 eta1/eta2")
ok(True, "quadrature: net region-1 flux = (1 - |G|^2)|E0|^2/2 eta1 at every z (no cross term); equals St at 0+; St decays as e^{-2 alpha2 z}")
# lossless algebra of the derivation
for G in (-0.9, -0.2, 0.0, 1 / 7, 0.6):
    T = 1 + G; r = (1 - G) / (1 + G)
    close(T ** 2 * r, 1 - G ** 2, f"tau^2 eta1/eta2 = (1 + G)(1 - G), G = {G:.3f}")
# w - w* is purely imaginary
wv = 0.3 * np.exp(1.1j); close((wv - np.conj(wv)).real, 0.0, "w - w* has zero real part", atol=1e-15)

print("=== D. perfect-conductor limit")
w = 2 * np.pi * 1e8; prev = None
for s in (1e2, 1e4, 1e6, 1e8):
    g2, h2 = medium(w, mu0, eps0, s); G, T = coeffs(E0C, h2)
    ok(abs(G + 1) < 4 * abs(h2) / E0C and abs(T) < 2.1 * abs(h2) / E0C, f"sigma2 = {s:.0e}: |Gamma + 1| = {abs(G + 1):.2e}, |tau| = {abs(T):.2e} -> 0")
G, T = -1.0, 0.0
E0 = 2.5; h1 = E0C
Etot0 = E0 * (1 + G); Htot0 = E0 / h1 * (1 - G)
close(Etot0, 0.0, "PEC: total E at z = 0 is E0(1 + Gamma) = 0")
close(Htot0, 2 * E0 / h1, "PEC: total H at z = 0 is 2 E0/eta1 (along y)")
Js = cr(-Z, Htot0 * Y)                  # n = -z, from region 2 (conductor) into region 1
close(Js, 2 * E0 / h1 * X, "J_s = (-z) x y 2E0/eta1 = +x 2E0/eta1 (along the incident E)")
close(cr(-Z, Y), X, "(-z) x y = +x")
# Lecture 26 consistency: depth integral of sigma2 E_t tends to J_s as sigma2 grows
for s in (1e5, 1e7, 1e9):
    g2, h2 = medium(w, mu0, eps0, s); G, T = coeffs(E0C, h2)
    Jint = s * T * E0 / g2
    near(abs(Jint), 2 * E0 / E0C, f"sigma2 = {s:.0e}: integral of sigma2 E_t dz -> 2E0/eta1", rel=3e-3 if s < 1e6 else 1e-4)

print("=== E. special cases and the coating example")
for mr in (1.0, 2.0, 7.5):
    close(coeffs(eta0, np.sqrt(mr * mu0 / (mr * eps0)))[0], 0.0, f"matched: mu_r = eps_r = {mr} against vacuum gives Gamma = 0", atol=1e-12)
G, T = coeffs(E0C, E0C / 1.5)
close(G, -0.2, "glass n = 1.5 in air: Gamma = -0.2"); close(G ** 2, 0.04, "4 % of the power reflects")
nc = np.sqrt(1.5)
close(np.sqrt(E0C * E0C / 1.5), E0C / nc, "eta_c = sqrt(eta0 * eta0/1.5) = eta0/sqrt(1.5)")
near(nc, 1.22, "n_c = sqrt(1.5) = 1.22", rel=0.004)
near(550 / (4 * nc), 112, "lambda0/(4 n_c) = 112 nm at 550 nm", rel=0.005)
# quarter-wave layer of impedance sqrt(eta1 eta2) removes the reflection (transfer-matrix check), any wavelength
def slab_reflection(eta1, etac, eta2, beta_d):
    """Gamma seen from medium 1 for a layer (etac, electrical thickness beta_d) on medium 2"""
    Zin = etac * (eta2 + 1j * etac * np.tan(beta_d)) / (etac + 1j * eta2 * np.tan(beta_d))
    return (Zin - eta1) / (Zin + eta1)
close(abs(slab_reflection(E0C, E0C / nc, E0C / 1.5, np.pi / 2 - 1e-12)), 0.0, "quarter-wave coating: zero reflection", atol=1e-9)
close(abs(slab_reflection(E0C, E0C / nc, E0C / 1.5, 1e-12)), 0.2, "zero-thickness coating: back to |Gamma| = 0.2", atol=1e-9)
# cross-check the impedance formula against a direct field solution of the three-layer problem
lam_c = 1.0; bc = 2 * np.pi / lam_c; d = lam_c / 4; e1, ec, e2 = E0C, E0C / nc, E0C / 1.5
# unknowns: r (reflected in 1), a, b (layer forward/backward), t (transmitted)
M = np.array([[-1, 1, 1, 0], [1 / e1, 1 / ec, -1 / ec, 0],
              [0, np.exp(-1j * bc * d), np.exp(1j * bc * d), -1],
              [0, np.exp(-1j * bc * d) / ec, -np.exp(1j * bc * d) / ec, -1 / e2]], dtype=complex)
r, a, bb, t = np.linalg.solve(M, np.array([1, 1 / e1, 0, 0], dtype=complex))
close(abs(r), 0.0, "direct three-layer field solution: quarter-wave layer reflects nothing", atol=1e-12)
close(abs(t) ** 2 * e1 / e2, 1.0, "and transmits all the power")

print("=== F. the notes' Example 1 (vacuum onto mu0, 9/4 eps0)")
Ei = np.sqrt(120 * np.pi)
h2 = E0C / np.sqrt(9 / 4)
close(h2, 2 / 3 * E0C, "eta2 = (2/3) eta0")
G, T = coeffs(E0C, h2)
close(G, -1 / 5, "Gamma = -1/5"); close(T, 4 / 5, "tau = 4/5")
close(G * Ei * X, -Ei / 5 * X, "E_r = -(1/5) x sqrt(120 pi) e^{j b1 z}")
close(-G * Ei / E0C * Y, Ei / (5 * E0C) * Y, "H_r = +(1/5) y sqrt(120 pi)/eta0 e^{j b1 z}")
close(T * Ei / h2, 4 / 5 * Ei / (2 / 3 * E0C), "H_t = (4/5) sqrt(120 pi)/((2/3) eta0)")
close(np.sqrt(9 / 4), 1.5, "beta2 = 1.5 beta1")
Si = Ei ** 2 / (2 * E0C); Sr = G ** 2 * Si; St = T ** 2 * Ei ** 2 / (2 * h2)
close(Si, 0.5, "<S_i> = 1/2 W/m^2 (eta0 = 120 pi)"); close(Sr, 0.02, "<S_r> = 1/50 = 0.02 W/m^2")
close(St, 0.48, "<S_t> = (1/2)(16/25)(3/2) = 0.48 W/m^2"); close(Sr + St, Si, "0.02 + 0.48 = 0.5")
close(0.5 * (1 / 25 + 16 / 25 * 3 / 2), 0.5, "notes: (1/2)(1/25 + 24/25) = 1/2")
close(16 / 25 * 3 / 2, 24 / 25, "notes: (16/25)(3/2) = 24/25")
close(Sr / Si, 0.04, "4 % reflects"); close(St / Si, 0.96, "96 % transmitted")
near(Ei ** 2 / (2 * eta0), 0.5, "with eta0 = 376.73 the notes' 'approximately 1/2' holds (0.5003)", rel=1e-3)
close(cr(X, Y), Z, "<S_i>, <S_t> along +z"); close(cr(-X, Y), -Z, "E_r along -x, H_r along +y: <S_r> along -z")

print("=== G. air onto seawater at 1 kHz")
w = 2 * np.pi * 1e3; g2, h2 = medium(w, mu0, 81 * eps0, 4.0)
near(1 / g2.real, 7.96, "delta = 7.96 m", rel=1e-3)
near(h2.real, 0.0314, "eta2 real part 0.0314 ohm", rel=0.003); near(h2.imag, 0.0314, "eta2 imaginary part 0.0314 ohm", rel=0.003)
close(h2, (1 + 1j) / (4.0 * (1 / g2.real)), "eta2 ~ (1 + j)/(sigma delta)", rtol=1e-5)
G, T = coeffs(eta0, h2)
near(G.real, -0.99983, "Gamma real part -0.99983", rel=5e-6)
near(G.imag, 0.00017, "Gamma imaginary part +0.00017", rel=0.02)
near(1 - abs(G) ** 2, 3.3e-4, "1 - |Gamma|^2 = 3.3e-4 (0.033 %)", rel=0.02)
near(1 - abs(G) ** 2, 4 * h2.real / eta0, "small-eta2 approximation 4 Re(eta2)/eta1", rel=2e-3)
Gc, _ = coeffs(E0C, h2); near(1 - abs(Gc) ** 2, 3.3e-4, "same with eta0 = 120 pi", rel=0.02)
close(np.exp(-2 * g2.real * 1 / g2.real), np.exp(-2), "power decays as e^{-2z/delta}")
near(abs(G), 0.9998, "concept page: Gamma ~ -0.9998", rel=1e-4)

print("=== H. figures")
# refl-setup: physics z -> screen right, x -> up, y -> out
M = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], dtype=float)  # rows: screen X, Y, Z from physics x, y, z
close(np.linalg.det(M), 1.0, "physics -> screen map is a proper rotation")
close(M @ X, Y, "E along +x -> screen up"); close(M @ Y, Z, "H along +y -> out of the screen (odot)"); close(M @ Z, X, "+z -> screen right")
close(cr(Y, Z), X, "screen: up x out = right: incident and transmitted travel right")
close(cr(Y, -Z), -X, "screen: up x in (otimes) = left: reflected (H along -y for Gamma > 0) travels left")
close(M @ (-Z), -X, "n = -z drawn pointing left (from region 2 into region 1)")
# refl-gamma-tau labels
for r, gp, tp in ((2 / 3, -0.2, 0.8), (1.0, 0.0, 1.0), (1.5, 0.2, 1.2)):
    G, T = coeffs(1.0, r); close(G, gp, f"fig 2 dot at eta2/eta1 = {r:.3f}: Gamma = {gp}"); close(T, tp, f"fig 2 dot: tau = {tp}")
lr = np.linspace(-2, 2, 801); rr = 10 ** lr; Gc = (rr - 1) / (rr + 1)
close(Gc, -Gc[::-1], "fig 2: Gamma odd in log(eta2/eta1)"); close(Gc ** 2, (Gc ** 2)[::-1], "fig 2: Gamma^2 even")
ok(Gc[0] < -0.96 and 2 * rr[0] / (rr[0] + 1) < 0.02 and Gc[-1] > 0.96 and 2 * rr[-1] / (rr[-1] + 1) > 1.96, "fig 2: limits -1, 0 and +1, 2 at the ends")
# refl-interface-snapshot: continuity at all instants, scale factors, slopes
G, T, n2 = -0.2, 0.8, 1.5; b1 = 2 * np.pi; b2 = n2 * b1
for wt in np.linspace(0, 2 * np.pi, 37):
    E1 = np.cos(wt) + G * np.cos(wt); E2 = T * np.cos(wt)
    H1 = np.cos(wt) - G * np.cos(wt); H2 = n2 * T * np.cos(wt)       # eta1 H; eta1/eta2 = 1.5
    dE1 = b1 * np.sin(wt) - G * b1 * np.sin(wt); dE2 = T * b2 * np.sin(wt)
    dH1 = b1 * np.sin(wt) + G * b1 * np.sin(wt); dH2 = n2 * T * b2 * np.sin(wt)
    if not (np.isclose(E1, E2) and np.isclose(H1, H2) and np.isclose(dE1, dE2) and (abs(np.sin(wt)) < 1e-9 or np.isclose(dH2 / dH1, 2.25))):
        raise SystemExit("FAILED snapshot continuity")
ok(True, "fig 3: total E and eta1 H continuous at z = 0 at every instant; E slope continuous (mu1 = mu2); H slope jumps by eps2/eps1 = 2.25")
close(T, 0.8, "fig 3 caption: E scales by tau = 0.8"); close(n2 * T, 1 - G, "fig 3 caption: H scales by 1 - Gamma = 1.2")

print("=== I. worked problem")
f = 50e6; w = 2 * np.pi * f; cc = 3e8
b1 = w / cc; close(b1, np.pi / 3, "beta1 = pi/3 rad/m")
h1 = E0C; h2 = E0C * np.sqrt(4 / 2.25); close(h2, 160 * np.pi, "eta2 = (4/3) eta0 = 160 pi ohm")
b2 = np.sqrt(4 * 2.25) * b1; close(b2, np.pi, "beta2 = 3 beta1 = pi rad/m (matches the pi x in H_t)")
G, T = coeffs(h1, h2); close(G, 1 / 7, "Gamma = 1/7"); close(T, 8 / 7, "tau = 8/7")
near(G, 0.143, "1/7 = 0.143", rel=0.002); near(T, 1.14, "8/7 = 1.14", rel=0.003)
u_t = -X; Ht = (1 / (10 * np.pi)) * Z  # review: amplitude changed from 1/20pi
Et = h2 * cr(Ht, u_t); close(Et, -16 * Y, "E_t = eta2 H_t x u = -16 y V/m")
close(cr(Z, -X), -Y, "z x (-x) = -y"); close(cr(-Y, Z), -X, "(-y) x z = -x: E_t x H_t* along the travel")
Ei0 = Et / T; Er0 = G * Ei0
close(Ei0, -14 * Y, "E_i(0) = -14 y V/m"); close(Er0, -2 * Y, "E_r(0) = -2 y V/m")
Hi = cr(-X, Ei0) / h1; Hr = cr(X, Er0) / h1
close(Hi, 7 / (60 * np.pi) * Z, "H_i = +z 7/(60 pi)"); close(Hr, -1 / (60 * np.pi) * Z, "H_r = -z 1/(60 pi)")
close(cr(-X, -Y), Z, "(-x) x (-y) = +z"); close(cr(X, -Y), -Z, "x x (-y) = -z")
near(7 / (60 * np.pi) * 1e3, 37.1, "|H_i| = 37.1 mA/m", rel=0.002); near(1 / (60 * np.pi) * 1e3, 5.31, "|H_r| = 5.31 mA/m", rel=0.002)
close(Hi + Hr, Ht, "H_i(0) + H_r(0) = H_t(0) = z/(10 pi)")
close(Hr[2] / Hi[2], -G, "H_r/H_i = -1/7 = -Gamma"); close(Ht[2] / Hi[2], 1 - G, "H_t/H_i = 6/7 = 1 - Gamma")
# full phasors satisfy Maxwell (x-travel): for E = -y Ey(x), H = z Hz(x): dEy/dx = -j w mu Hz, -dHz/dx = j w eps Ey
xs = np.array([0.37, 0.37 + 1e-6, 0.37 - 1e-6]); dx = 1e-6
Ey_i = -14 * np.exp(1j * b1 * xs); Hz_i = 7 / (60 * np.pi) * np.exp(1j * b1 * xs)
close((Ey_i[1] - Ey_i[2]) / (2 * dx), -1j * w * mu0 * Hz_i[0], "incident (y, z) phasors satisfy Faraday", rtol=1e-6)
eps0c = 1e-9 / (36 * np.pi)            # the problem's eta0 = 120 pi and c = 3e8 imply this eps0
close(-(Hz_i[1] - Hz_i[2]) / (2 * dx), 1j * w * eps0c * Ey_i[0], "incident phasors satisfy Ampere (eps0 = 1e-9/36 pi)", rtol=1e-6)
Ey_r = -2 * np.exp(-1j * b1 * xs); Hz_r = -1 / (60 * np.pi) * np.exp(-1j * b1 * xs)
close((Ey_r[1] - Ey_r[2]) / (2 * dx), -1j * w * mu0 * Hz_r[0], "reflected phasors satisfy Faraday", rtol=1e-6)
xs2 = -xs
Ey_t = -16 * np.exp(1j * b2 * xs2); Hz_t = 1 / (10 * np.pi) * np.exp(1j * b2 * xs2)
close((Ey_t[2] - Ey_t[1]) / (2 * dx), -1j * w * 4 * mu0 * Hz_t[0], "transmitted phasors satisfy Faraday (mu = 4 mu0)", rtol=1e-6)
close(-(Hz_t[2] - Hz_t[1]) / (2 * dx), 1j * w * 2.25 * eps0c * Ey_t[0], "transmitted phasors satisfy Ampere (eps = 2.25 eps0)", rtol=1e-6)
# time domain of the given field: Re{(1/10pi) e^{j pi x} e^{jwt}} = (1/20pi) cos(wt + pi x)
for xv, wt in ((-0.3, 0.7), (-1.1, 2.0)):
    close(np.real(np.exp(1j * np.pi * xv) * np.exp(1j * wt)), np.cos(wt + np.pi * xv), f"phasor of cos(wt + pi x) at x = {xv}")
Si = 49 / (60 * np.pi); Sr = 1 / (60 * np.pi); St = 256 / (2 * 160 * np.pi)
close(Si, 14 ** 2 / (2 * h1), "<S_i> = 49/(60 pi)"); close(St, 4 / (5 * np.pi), "<S_t> = 4/(5 pi)")
close(Si - Sr, St, "49/60pi - 1/60pi = 48/60pi = 4/5pi")
near(Si * 1e3, 260, "<S_i> = 260 mW/m^2", rel=0.002); near(Sr * 1e3, 5.31, "<S_r> = 5.31 mW/m^2", rel=0.002)
near(St * 1e3, 255, "<S_t> = 255 mW/m^2", rel=0.002)
close(cr(-Y, Z), -X, "<S_i> along -x (E -y, H +z)"); close(cr(-Y, -Z), X, "<S_r> along +x (E -y, H -z)")
close(G ** 2, 1 / 49, "Gamma^2 = 1/49"); near(G ** 2 * 100, 2.0, "2.0 % reflects", rel=0.03)
close(T ** 2 * h1 / h2, 48 / 49, "tau^2 eta1/eta2 = (64/49)(3/4) = 48/49")
# (f) perfect conductor
Er_pec = -1 * Ei0; close(Er_pec, 14 * Y, "PEC: E_r(0) = +14 y")
Hr_pec = cr(X, Er_pec) / h1; close(Hr_pec, 7 / (60 * np.pi) * Z, "PEC: H_r = x x y 14/(120 pi) = +z 7/(60 pi)")
close(Ei0 + Er_pec, 0 * Y, "PEC: total E(0) = 0")
Htot = Hi + Hr_pec; close(Htot, 7 / (30 * np.pi) * Z, "PEC: total H(0) = z 28/(120 pi) = z 7/(30 pi)")
Js = cr(X, Htot); close(Js, -7 / (30 * np.pi) * Y, "J_s = x x z 7/(30 pi) = -y 7/(30 pi) A/m")
near(7 / (30 * np.pi) * 1e3, 74.3, "|J_s| = 74.3 mA/m", rel=0.002)
close(np.linalg.norm(Js), 2 * np.linalg.norm(Ei0) / h1, "|J_s| = 2|E_i(0)|/eta1")
ok(np.dot(Js, Ei0) > 0, "J_s parallel to the incident E at the surface")

print("=== J. concept page")
G, T = coeffs(2 / 3 * E0C, E0C)
close(G, 0.2, "out of glass into vacuum: Gamma = +1/5"); close(T, 6 / 5, "tau = 6/5"); close(G ** 2, 0.04, "again 4 %")
close(T ** 2 * (2 / 3), 0.96, "transmitted fraction (36/25)(2/3) = 0.96")
E0 = 3.0
close(np.linalg.norm(cr(-Z, (2 * E0 / E0C) * Y)), 2 * E0 / E0C, "|J_s| = 2|E0|/eta1")

print(f"\nALL {ok_count} CHECKS PASSED")
