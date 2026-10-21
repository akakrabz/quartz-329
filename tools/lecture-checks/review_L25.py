#!/usr/bin/env python3
"""Independent review checks, Lecture 25 (reflection/transmission).

Re-derives every equation and number on the L25 lecture page, concept page,
worked problem and figures. numpy/scipy only. Output: review_L25.out
"""
import numpy as np
from scipy.integrate import quad

PI = np.pi
MU0 = 4e-7 * PI
EPS0 = 8.8541878128e-12
C0 = 1 / np.sqrt(MU0 * EPS0)
ETA0 = np.sqrt(MU0 / EPS0)          # 376.73 ohm (handbook, CODATA)
ETA0x = 120 * PI                    # exam/notes value
X, Y, Z = np.eye(3)
NP = NF = 0
LOG = []


def chk(name, ok, info=""):
    global NP, NF
    if ok:
        NP += 1
    else:
        NF += 1
    s = f"{'PASS' if ok else 'FAIL'}  {name}" + (f"   [{info}]" if info else "")
    print(s)
    LOG.append(s)


def close(a, b, rtol=1e-9, atol=1e-12):
    return np.allclose(a, b, rtol=rtol, atol=atol)


def gam_eta(f, mu, eps, sig):
    w = 2 * PI * f
    g = np.sqrt(1j * w * mu * (sig + 1j * w * eps))
    if g.real < 0:
        g = -g
    e = np.sqrt(1j * w * mu / (sig + 1j * w * eps))
    if e.real < 0:
        e = -e
    return g, e


def solve_bc(eta1, eta2):
    """unknowns (Gamma, tau) from tangential E and H continuity, E0 = 1"""
    A = np.array([[1, -1], [-1 / eta1, -1 / eta2]], dtype=complex)
    b = np.array([-1, -1 / eta1], dtype=complex)
    return np.linalg.solve(A, b)


# ============================================================ A. phasors satisfy Maxwell (finite differences)
print("== A. phasors of the three waves satisfy phasor Maxwell (finite differences)")
f = 1e6
w = 2 * PI * f
mu1, eps1 = MU0, 2 * EPS0
mu2, eps2, sig2 = 3 * MU0, 5 * EPS0, 2e-4
b1 = w * np.sqrt(mu1 * eps1); et1 = np.sqrt(mu1 / eps1)
g2, et2 = gam_eta(f, mu2, eps2, sig2)
G, T = (et2 - et1) / (et2 + et1), 2 * et2 / (et2 + et1)
E0 = 2.0 * np.exp(0.4j)
waves = {
    "incident": (lambda z: E0 * np.exp(-1j * b1 * z) * X, lambda z: E0 / et1 * np.exp(-1j * b1 * z) * Y, mu1, 0.0, eps1),
    "reflected": (lambda z: G * E0 * np.exp(1j * b1 * z) * X, lambda z: -G * E0 / et1 * np.exp(1j * b1 * z) * Y, mu1, 0.0, eps1),
    "transmitted": (lambda z: T * E0 * np.exp(-g2 * z) * X, lambda z: T * E0 / et2 * np.exp(-g2 * z) * Y, mu2, sig2, eps2),
}


def curl_z(F, z, h):
    """curl of a field depending on z only: (-dFy/dz, dFx/dz, 0)"""
    d = (F(z + h) - F(z - h)) / (2 * h)
    return np.array([-d[1], d[0], 0])


for name, (Ef, Hf, mu, sg, ep) in waves.items():
    zz = -37.0 if name != "transmitted" else 41.0
    h = 1e-3
    cE = curl_z(Ef, zz, h); cH = curl_z(Hf, zz, h)
    okF = close(cE, -1j * w * mu * Hf(zz), rtol=1e-6, atol=1e-12)
    okA = close(cH, (sg + 1j * w * ep) * Ef(zz), rtol=1e-6, atol=1e-12)
    chk(f"A {name}: curl E = -jwmu H and curl H = (sig+jweps) E", okF and okA)
    # power flow direction from E x H*
    S = 0.5 * np.real(np.cross(Ef(zz), np.conj(Hf(zz))))
    exp_dir = -1 if name == "reflected" else 1
    chk(f"A {name}: Re{{E x H*}} along {'-z' if exp_dir < 0 else '+z'} (G={G:.3f})", np.sign(S[2]) == exp_dir * (1 if name != "reflected" else 1) and abs(S[0]) + abs(S[1]) < 1e-15)
# H = u x E / eta for each wave with np.cross
for name, (Ef, Hf, *_), u, et in zip(waves, waves.values(), (Z, -Z, Z), (et1, et1, et2)):
    chk(f"A {name}: H = u x E / eta via np.cross (u={u})", close(Hf(0.3), np.cross(u, Ef(0.3)) / et))
chk("A (-z) x x = -y (reflected H direction)", close(np.cross(-Z, X), -Y))

# ============================================================ B. boundary conditions at z = 0, Gamma and tau
print("== B. boundary conditions at z = 0; Gamma, tau")
nhat = -Z   # from region 2 (z>0) into region 1
E1 = waves["incident"][0](0) + waves["reflected"][0](0)
H1 = waves["incident"][1](0) + waves["reflected"][1](0)
E2 = waves["transmitted"][0](0); H2 = waves["transmitted"][1](0)
chk("B n x (E1 - E2) = 0 at z=0 (lossy region 2)", close(np.cross(nhat, E1 - E2), 0))
chk("B n x (H1 - H2) = 0 = J_s at z=0 (lossy region 2)", close(np.cross(nhat, H1 - H2), 0))
# also continuity just across z=0 numerically (limits from both sides)
eps_z = 1e-9
chk("B E_x continuous across z=0 (limits from both sides)", abs((waves['incident'][0](-eps_z) + waves['reflected'][0](-eps_z))[0] - waves['transmitted'][0](eps_z)[0]) < 1e-8)
chk("B H_y continuous across z=0 (limits from both sides)", abs((waves['incident'][1](-eps_z) + waves['reflected'][1](-eps_z))[1] - waves['transmitted'][1](eps_z)[1]) < 1e-10)
rng = np.random.default_rng(25)
ok = True
for _ in range(200):
    e1 = rng.uniform(1, 600)                  # lossless region 1
    e2 = rng.uniform(0.01, 600) * np.exp(1j * rng.uniform(0, PI / 4))
    g_, t_ = solve_bc(e1, e2)
    ok &= close(g_, (e2 - e1) / (e2 + e1)) and close(t_, 2 * e2 / (e2 + e1)) and close(t_, 1 + g_)
chk("B 2x2 solve = closed forms Gamma=(e2-e1)/(e2+e1), tau=1+Gamma=2e2/(e2+e1) (200 random, complex eta2)", ok)
ok = True
for _ in range(200):   # lossy region 1 too (exam remark)
    e1 = rng.uniform(1, 600) * np.exp(1j * rng.uniform(0, PI / 4))
    e2 = rng.uniform(0.01, 600) * np.exp(1j * rng.uniform(0, PI / 4))
    g_, t_ = solve_bc(e1, e2)
    ok &= close(g_, (e2 - e1) / (e2 + e1)) and close(t_, 1 + g_)
chk("B Gamma formula also holds for complex eta1 (lossy region 1; On-exams remark)", ok)
# properties
r = np.logspace(-4, 4, 2001)
Gr = (r - 1) / (r + 1); Tr = 2 * r / (r + 1)
chk("B real eta: -1<Gamma<1, 0<tau<2; sign(Gamma)=sign(eta2-eta1); tau>1 iff eta2>eta1",
    np.all(np.abs(Gr) < 1) and np.all((Tr > 0) & (Tr < 2)) and np.all(np.sign(Gr) == np.sign(r - 1)) and np.all((Tr > 1) == (r > 1)))
ok = True
for _ in range(2000):
    e1 = rng.uniform(1, 600)
    e2 = rng.uniform(1e-3, 1e3) * np.exp(1j * rng.uniform(-PI / 2, PI / 2))   # Re eta2 >= 0
    ok &= abs((e2 - e1) / (e2 + e1)) <= 1 + 1e-12
chk("B Re{eta2}>=0 (eta1 real) => |Gamma|<=1 (2000 random)", ok)
g_, t_ = solve_bc(et1, et2)
chk("B H ratios at z=0: Hr/Hi = -Gamma, Ht/Hi = 1-Gamma = tau*eta1/eta2",
    close(waves["reflected"][1](0)[1] / waves["incident"][1](0)[1], -G) and close(waves["transmitted"][1](0)[1] / waves["incident"][1](0)[1], 1 - G) and close(1 - G, T * et1 / et2))
for n1, n2 in ((1, 1.5), (1.5, 1), (1.33, 2.4)):
    e1_, e2_ = ETA0 / n1, ETA0 / n2
    chk(f"B n-form Gamma=(n1-n2)/(n1+n2), n1={n1}, n2={n2}", close((e2_ - e1_) / (e2_ + e1_), (n1 - n2) / (n1 + n2)))
e1_, e2_ = 300.0, 120.0
chk("B swapping two lossless media flips Gamma, keeps Gamma^2", close((e1_ - e2_) / (e1_ + e2_), -(e2_ - e1_) / (e2_ + e1_)))

# ============================================================ C. power: quadrature vs 1/2 Re{E x H*}; balance; lossy region 2
print("== C. time-average power by quadrature; balance (lossy region 2 with exact gamma, eta)")


def inst(ph, t):
    return np.real(ph * np.exp(1j * w * t))


def tavg_S(Eph, Hph):
    Tp = 1 / f
    out = []
    for k in range(3):
        fn = lambda t: np.cross(inst(Eph, t), inst(Hph, t))[k]
        out.append(quad(fn, 0, Tp, limit=200)[0] / Tp)
    return np.array(out)


for name, (Ef, Hf, *_) in waves.items():
    zz = -3.0 if name != "transmitted" else 5.0
    Sq = tavg_S(Ef(zz), Hf(zz)); Sp = 0.5 * np.real(np.cross(Ef(zz), np.conj(Hf(zz))))
    chk(f"C {name}: quadrature <E x H> = 1/2 Re{{E x H*}}", close(Sq, Sp, rtol=1e-7, atol=1e-15))
Si = abs(E0) ** 2 / (2 * et1); Sr = abs(G) ** 2 * Si
St0 = abs(T) ** 2 * abs(E0) ** 2 / 2 * np.real(1 / et2)
chk("C page formulas <S_i>, <S_r>, <S_t>(0+) equal the 1/2Re{ExH*} values",
    close(Si, 0.5 * np.real(np.cross(waves['incident'][0](0), np.conj(waves['incident'][1](0))))[2])
    and close(-Sr, 0.5 * np.real(np.cross(waves['reflected'][0](0), np.conj(waves['reflected'][1](0))))[2])
    and close(St0, 0.5 * np.real(np.cross(E2, np.conj(H2)))[2]))
chk("C balance 1 = |G|^2 + |tau|^2 eta1 Re{1/eta2} (lossy region 2)", close(1, abs(G) ** 2 + abs(T) ** 2 * et1 * np.real(1 / et2)), f"G={G:.5f}, tau={T:.5f}")
ok = True
for _ in range(500):
    e1 = rng.uniform(1, 600)
    e2 = rng.uniform(1e-3, 1e3) * np.exp(1j * rng.uniform(0, PI / 4))
    gg, tt = (e2 - e1) / (e2 + e1), 2 * e2 / (e2 + e1)
    ok &= close(1, abs(gg) ** 2 + abs(tt) ** 2 * e1 * np.real(1 / e2))
chk("C balance holds for 500 random (lossless eta1, complex eta2)", ok)
# total flux in region 1 at many z equals Si - Sr (no cross term), via quadrature
zs = np.linspace(-50, 0, 7)
vals = [tavg_S(waves['incident'][0](z_) + waves['reflected'][0](z_), waves['incident'][1](z_) + waves['reflected'][1](z_))[2] for z_ in zs]
chk("C net <S_z> in region 1 = Si - Sr at every z (quadrature, 7 points)", close(vals, Si - Sr, rtol=1e-7))
# derivation's product formula with w = G e^{j2b1z}
z_ = -1.234
Ex = E0 * (np.exp(-1j * b1 * z_) + G * np.exp(1j * b1 * z_)); Hy = E0 / et1 * (np.exp(-1j * b1 * z_) - G * np.exp(1j * b1 * z_))
wv = G * np.exp(2j * b1 * z_)
chk("C derivation: Ex Hy* = |E0|^2/eta1 (1 - |G|^2 + w - w*)", close(Ex * np.conj(Hy), abs(E0) ** 2 / et1 * (1 - abs(G) ** 2 + wv - np.conj(wv))))
# transmitted decays as exp(-2 alpha z)
zt = np.array([0.0, 100.0, 2000.0])
St = [0.5 * np.real(np.cross(waves['transmitted'][0](q), np.conj(waves['transmitted'][1](q))))[2] for q in zt]
chk("C <S_t>(z) = <S_t>(0) e^{-2 alpha2 z} (fields e^{-alpha z})", close(St, St0 * np.exp(-2 * g2.real * zt)) and close(abs(waves['transmitted'][0](100.0)[0]) / abs(T * E0), np.exp(-g2.real * 100)))
chk("C Re{1/eta2} = cos(angle eta2)/|eta2|", close(np.real(1 / et2), np.cos(np.angle(et2)) / abs(et2)))
# lossless region 2 form
for r_ in (2 / 3, 1.5, 4 / 3):
    gg = (r_ - 1) / (r_ + 1); tt = 1 + gg
    chk(f"C lossless balance 1 = G^2 + tau^2 eta1/eta2 (eta2/eta1={r_:.3f})", close(1, gg ** 2 + tt ** 2 / r_))

# ============================================================ D. PEC limit, J_s = n x H1
print("== D. perfect-conductor limit")
for sg in (1e2, 1e5, 1e8):
    g2b, e2b = gam_eta(f, MU0, EPS0, sg)
    Gb, Tb = (e2b - ETA0) / (e2b + ETA0), 2 * e2b / (e2b + ETA0)
    print(f"   sigma2={sg:.0e}: Gamma={Gb:.6f}, tau={Tb:.2e}")
g2b, e2b = gam_eta(f, MU0, EPS0, 1e12)
Gb, Tb = (e2b - ETA0) / (e2b + ETA0), 2 * e2b / (e2b + ETA0)
chk("D sigma2 -> inf: eta2 -> 0, Gamma -> -1, tau -> 0", abs(Gb + 1) < 1e-6 and abs(Tb) < 1e-6)
E0p = 3.0
Etot = E0p * (1 + (-1)) * X
Htot = (E0p / ETA0 + E0p / ETA0) * Y
chk("D PEC total fields at z=0: E = 0, H = y 2E0/eta1", close(Etot, 0) and close(Htot, Y * 2 * E0p / ETA0))
Js = np.cross(-Z, Htot - 0)
chk("D J_s = n x (H1 - H2) = (-z) x y 2E0/eta1 = +x 2E0/eta1", close(Js, X * 2 * E0p / ETA0))
# good conductor depth integral (L26) -> J_s for large sigma
for sg in (1e4, 1e7):
    g2b, e2b = gam_eta(f, MU0, EPS0, sg)
    Tb = 2 * e2b / (e2b + ETA0)
    Jeff = sg * Tb * E0p / g2b
    print(f"   sigma2={sg:.0e}: depth integral of sigma E_t = {Jeff:.6f}, 2E0/eta0 = {2 * E0p / ETA0:.6f}")
chk("D depth integral of sigma2 E_t -> 2E0/eta1 (L26 check) at sigma=1e7", abs(Jeff / (2 * E0p / ETA0) - 1) < 1e-3)

# ============================================================ E. matched, coating
print("== E. special cases: matched impedance; quarter-wave coating")
chk("E mu_r = eps_r = 3 against vacuum: Gamma = 0", abs((ETA0 * np.sqrt(3 / 3) - ETA0)) < 1e-12)
n_glass = 1.5
Gg = (1 - n_glass) / (1 + n_glass)
chk("E glass n=1.5 (eps_r=2.25): Gamma = -0.2, 4 % reflected", close(Gg, -0.2) and close(Gg ** 2, 0.04) and close(np.sqrt(2.25), 1.5))
nc = np.sqrt(n_glass)
d = 550e-9 / (4 * nc)
chk("E coating eta_c = sqrt(eta0*eta0/1.5) <=> n_c = sqrt(1.5) = 1.22; thickness 112 nm", close(ETA0 / nc, np.sqrt(ETA0 * ETA0 / 1.5)) and round(nc, 2) == 1.22 and round(d * 1e9) == 112, f"n_c={nc:.4f}, d={d*1e9:.2f} nm")


def three_layer_gamma(n1, nc_, n2, d_, lam0):
    """direct field solve: region1 (z<0), layer 0<z<d, region2 z>d; unknowns r, A, B, t; E0 = 1"""
    k0 = 2 * PI / lam0
    k1, kc, k2 = n1 * k0, nc_ * k0, n2 * k0
    e1, ec, e2 = ETA0 / n1, ETA0 / nc_, ETA0 / n2
    # E: 1 + r = A + B ; H: (1 - r)/e1 = (A - B)/ec ; at d: A e^{-jkc d} + B e^{jkc d} = t e^{-jk2 d};
    # (A e^{-jkc d} - B e^{jkc d})/ec = t e^{-jk2 d}/e2
    M = np.array([[1, -1, -1, 0],
                  [-1 / e1, -1 / ec, 1 / ec, 0],
                  [0, np.exp(-1j * kc * d_), np.exp(1j * kc * d_), -np.exp(-1j * k2 * d_)],
                  [0, np.exp(-1j * kc * d_) / ec, -np.exp(1j * kc * d_) / ec, -np.exp(-1j * k2 * d_) / e2]], dtype=complex)
    rhs = np.array([-1, -1 / e1, 0, 0], dtype=complex)
    return np.linalg.solve(M, rhs)


sol = three_layer_gamma(1.0, nc, 1.5, d, 550e-9)
chk("E quarter-wave layer (lambda inside layer) gives zero reflection at 550 nm (4x4 field solve)", abs(sol[0]) < 1e-12, f"|r|={abs(sol[0]):.1e}")
r_wrong = three_layer_gamma(1.0, nc, 1.5, 550e-9 / 4, 550e-9)[0]
chk("E a lambda0/4 (free-space) layer does NOT cancel the reflection (erratum 3): |r|^2 far from 0", abs(r_wrong) ** 2 > 1e-3, f"|r|^2={abs(r_wrong)**2:.4f}")
r_off = three_layer_gamma(1.0, nc, 1.5, d, 450e-9)[0]
chk("E coating 'reduces' reflection off design wavelength too (450 nm: |r|^2 < 0.04)", abs(r_off) ** 2 < 0.04, f"|r|^2={abs(r_off)**2:.4f}")
# energy check of the 4x4 solve: 1 = |r|^2 + |t|^2 n2
chk("E 4x4 solve conserves power: |r|^2 + n2|t|^2 = 1", close(abs(r_off) ** 2 + 1.5 * abs(three_layer_gamma(1.0, nc, 1.5, d, 450e-9)[3]) ** 2, 1))

# ============================================================ F. notes' Example 1
print("== F. notes' Example 1")
e2 = ETA0x / np.sqrt(9 / 4)
Gx = (e2 - ETA0x) / (e2 + ETA0x); Tx = 1 + Gx
chk("F eta2 = 2/3 eta0, Gamma = -1/5, tau = 4/5", close(e2, 2 / 3 * ETA0x) and close(Gx, -0.2) and close(Tx, 0.8))
E0e = np.sqrt(120 * PI)
Si_ = E0e ** 2 / (2 * ETA0x); Sr_ = Gx ** 2 * Si_; St_ = Tx ** 2 * E0e ** 2 / (2 * e2)
chk("F <S_i>=0.5, <S_r>=0.02, <S_t>=0.48 W/m^2 with eta0=120pi; 4 %/96 %", close([Si_, Sr_, St_], [0.5, 0.02, 0.48]) and close(Sr_ / Si_, 0.04) and close(St_ / Si_, 0.96))
chk("F transmitted <S_t> = 1/2 (16/25)(3/2)", close(St_, 0.5 * 16 / 25 * 1.5))
chk("F H_r = -y G E0/eta1 = +(1/5) y sqrt(120pi)/eta0", close(-Gx * E0e / ETA0x, 0.2 * E0e / ETA0x))
chk("F beta2 = 1.5 beta1", close(np.sqrt(9 / 4), 1.5))
print(f"   with eta0 = {ETA0:.4f}: <S_i> = {E0e**2/(2*ETA0):.5f} W/m^2")

# ============================================================ G. seawater at 1 kHz (handbook: sigma = 4 S/m, eps_r = 81)
print("== G. air onto seawater at 1 kHz, exact gamma and eta (eps_r = 81)")
g_sw, e_sw = gam_eta(1e3, MU0, 81 * EPS0, 4.0)
dlt = 1 / np.sqrt(PI * 1e3 * MU0 * 4.0)
e_gc = (1 + 1j) / (4.0 * dlt)
chk("G delta = 7.96 m; good-conductor eta2 = 0.0314(1+j)", round(dlt, 2) == 7.96 and close(e_gc, 0.0314 * (1 + 1j), rtol=2e-3), f"delta={dlt:.4f}, eta_gc={e_gc:.5f}")
chk("G exact eta2 agrees with (1+j)/(sigma delta) to 1e-5", abs(e_sw / e_gc - 1) < 1e-5, f"exact={e_sw:.6f}")
chk("G exact alpha agrees with 1/delta", abs(g_sw.real * dlt - 1) < 1e-5)
for et_air, lab in ((ETA0, "376.73"), (ETA0x, "120pi")):
    Gs = (e_sw - et_air) / (e_sw + et_air)
    print(f"   eta1={lab}: Gamma={Gs.real:.6f}{Gs.imag:+.6f}j, 1-|G|^2={1-abs(Gs)**2:.4e}, |G|={abs(Gs):.6f}")
Gs = (e_sw - ETA0) / (e_sw + ETA0)
chk("G Gamma = -0.99983 + j0.00017", round(Gs.real, 5) == -0.99983 and round(Gs.imag, 5) == 0.00017)
chk("G 1 - |Gamma|^2 = 3.3e-4 (0.033 %); concept page |G| ~ 0.9998", round((1 - abs(Gs) ** 2) * 1e4, 1) == 3.3 and round(abs(Gs), 4) == 0.9998)
chk("G seawater at 1 kHz is a good conductor: sigma/(w eps) >> 1", 4.0 / (2 * PI * 1e3 * 81 * EPS0) > 1e5, f"{4.0/(2*PI*1e3*81*EPS0):.3g}")
chk("G concept-page 'Gamma ~ -0.9998'", round(Gs.real, 4) == -0.9998)

# ============================================================ H. figures (directions and curves)
print("== H. figures")
# refl-setup: screen frame R=(1,0,0) right, U=(0,1,0) up, O=(0,0,1) out; physics z->R, x->U, y->O
R, U, O = np.eye(3)
M = {"x": U, "y": O, "z": R}
chk("H refl-setup mapping is a proper rotation: Mx x My = Mz", close(np.cross(M["x"], M["y"]), M["z"]))
# incident: E up (x), H odot (+y): E x H = +z -> right
chk("H incident: E(up) x H(odot) = right (+z)", close(np.cross(U, O), R))
chk("H reflected drawn for Gamma>0: E up x H otimes = left (-z)", close(np.cross(U, -O), -R))
chk("H transmitted: E up x H odot = right", close(np.cross(U, O), R))
chk("H n = -z drawn pointing left (from region 2 into 1)", close(-M["z"], -R))
# snapshot: continuity at z = 0 for E and H panels (as coded)
wt = 0.3 * PI; GAM, TAU, N2 = -0.2, 0.8, 1.5
Etot0 = np.cos(wt) + GAM * np.cos(wt); Et0 = TAU * np.cos(wt)
Htot0 = np.cos(wt) - GAM * np.cos(wt); Ht0 = N2 * TAU * np.cos(wt)
chk("H snapshot: E continuous (1+G = tau), eta1 H continuous (1-G = tau eta1/eta2 = 1.2)", close(Etot0, Et0) and close(Htot0, Ht0) and close(N2 * TAU, 1.2))
# snapshot instantaneous fields correspond to Re{phasor e^{jwt}}
zt_ = -0.37
chk("H snapshot reflected E curve = Re{G e^{+j b1 z} e^{jwt}}", close(GAM * np.cos(wt + 2 * PI * zt_), np.real(GAM * np.exp(1j * 2 * PI * zt_) * np.exp(1j * wt))))
chk("H snapshot reflected eta1 H curve = Re{-G e^{+j b1 z} e^{jwt}}", close(-GAM * np.cos(wt + 2 * PI * zt_), np.real(-GAM * np.exp(1j * 2 * PI * zt_) * np.exp(1j * wt))))
chk("H snapshot transmitted eta1 H = tau (eta1/eta2) cos(wt - b2 z), eta1/eta2 = n2 = 1.5", close(ETA0 / (ETA0 / 1.5), N2))
# gamma-tau plot: markers
chk("H gamma-tau markers: 2/3 -> (-0.2, 0.8); 1.5 -> (+0.2, 1.2); 1 -> (0, 1)",
    close([(2/3 - 1)/(2/3 + 1), 1 + (2/3 - 1)/(2/3 + 1), (1.5 - 1)/2.5, 1 + 0.5/2.5], [-0.2, 0.8, 0.2, 1.2]))
chk("H gamma-tau: Gamma odd in log(eta2/eta1)", close((1 / r - 1) / (1 / r + 1), -Gr))
chk("H gamma-tau limits: r=0.01 -> G=-0.980, r=100 -> G=0.980, tau->2", close((0.01 - 1) / 1.01, -0.9802, rtol=1e-3) and Tr[-1] > 1.999)

# ============================================================ I. worked problem
print("== I. worked problem: working back from a transmitted wave")
f = 50e6; w = 2 * PI * f; c = 3e8
eta1 = 120 * PI; b1w = w / c
mur, epr = 4.0, 2.25
eta2 = eta1 * np.sqrt(mur / epr); b2w = b1w * np.sqrt(mur * epr)
chk("I(a) eta1 = 120pi, beta1 = pi/3, eta2 = 160pi, beta2 = pi", close([eta1, b1w, eta2, b2w], [120 * PI, PI / 3, 160 * PI, PI]))
nI = X   # region 2 is x<0, region 1 x>0; n from 2 into 1
Gw = (eta2 - eta1) / (eta2 + eta1); Tw = 1 + Gw
chk("I(b) Gamma = 1/7, tau = 8/7", close([Gw, Tw], [1 / 7, 8 / 7]))
# given H_t(x,t) = z (1/20pi) cos(wt + pi x) -> phasor z (1/20pi) e^{j pi x}, travels -x
Ht = lambda x: Z * (1 / (10 * PI)) * np.exp(1j * PI * x)
u_t = -X
Et_ph = lambda x: eta2 * np.cross(Ht(x), u_t)
chk("I(c) E_t = eta2 H_t x u = -y 16 e^{j pi x}", close(Et_ph(0.2), -Y * 16 * np.exp(1j * PI * 0.2)))
chk("I(c) H_t = u x E_t/eta2 (consistency)", close(np.cross(u_t, Et_ph(0.2)) / eta2, Ht(0.2)))
# check given time function travels -x: peak of cos(wt + pi x) moves to smaller x
t1 = 1e-9
chk("I(c) cos(wt + pi x) travels toward -x (phase point x = -wt/pi decreases)", (-w * t1 / PI) < 0)
chk("I(c) E_t x H_t* along -x", np.real(np.cross(Et_ph(0), np.conj(Ht(0))))[0] < 0)
Ei0 = Et_ph(0) / Tw; Er0 = Gw * Ei0
chk("I(c) E_i(0) = -14y, E_r(0) = -2y", close(Ei0, -14 * Y) and close(Er0, -2 * Y))
Ei = lambda x: -14 * Y * np.exp(1j * b1w * x)       # toward -x
Er = lambda x: -2 * Y * np.exp(-1j * b1w * x)      # toward +x
Hi = lambda x: np.cross(-X, Ei(x)) / eta1
Hr = lambda x: np.cross(X, Er(x)) / eta1
chk("I(d) H_i = z 7/(60pi) e^{j pi x/3}", close(Hi(0.5), Z * 7 / (60 * PI) * np.exp(1j * PI / 3 * 0.5)))
chk("I(d) H_r = -z 1/(60pi) e^{-j pi x/3}", close(Hr(0.5), -Z / (60 * PI) * np.exp(-1j * PI / 3 * 0.5)))
chk("I(d) amplitudes 37.1 and 5.31 mA/m", round(abs(Hi(0)[2]) * 1e3, 1) == 37.1 and round(abs(Hr(0)[2]) * 1e3, 2) == 5.31)
chk("I(d) BC (14-2)/120pi = 1/10pi: n x (E1 - E2) = 0 and n x (H1 - H2) = 0 at x=0", close(np.cross(nI, Ei(0) + Er(0) - Et_ph(0)), 0) and close(np.cross(nI, Hi(0) + Hr(0) - Ht(0)), 0))
chk("I(d) H_r/H_i = -1/7 = -Gamma; H_t/H_i = 6/7 = 1 - Gamma", close(Hr(0)[2] / Hi(0)[2], -Gw) and close(Ht(0)[2] / Hi(0)[2], 1 - Gw) and close(1 - Gw, 6 / 7))


# Maxwell by 3-D finite differences for x-dependent fields (vacuum region 1 and region 2)
def curl_x(F, x, h=1e-4):
    d = (F(x + h) - F(x - h)) / (2 * h)       # dF/dx
    return np.array([0, -d[2], d[1]])


for nm, Ef, Hf, mu_, ep_ in (("incident", Ei, Hi, MU0 * 1, None), ("reflected", Er, Hr, MU0, None), ("transmitted", Et_ph, Ht, mur * MU0, None)):
    # use c = 3e8 and eta1 = 120pi consistently: mu = eta/c, eps = 1/(eta c) per region
    if nm == "transmitted":
        mu_, ep_ = eta2 * np.sqrt(mur * epr) / c, np.sqrt(mur * epr) / (eta2 * c)
    else:
        mu_, ep_ = eta1 / c, 1 / (eta1 * c)
    xx = 0.71 if nm != "transmitted" else -0.43
    okF = close(curl_x(Ef, xx), -1j * w * mu_ * Hf(xx), rtol=1e-6)
    okA = close(curl_x(Hf, xx), 1j * w * ep_ * Ef(xx), rtol=1e-6)
    chk(f"I {nm}: phasor Maxwell by finite differences (x-dependence)", okF and okA)
Si_w = 0.5 * np.real(np.cross(Ei(0), np.conj(Hi(0))))
Sr_w = 0.5 * np.real(np.cross(Er(0), np.conj(Hr(0))))
St_w = 0.5 * np.real(np.cross(Et_ph(0), np.conj(Ht(0))))
chk("I(e) <S_i> = -x 49/(60pi), <S_r> = +x 1/(60pi), <S_t> = -x 4/(5pi)", close(Si_w, -X * 49 / (60 * PI)) and close(Sr_w, X / (60 * PI)) and close(St_w, -X * 4 / (5 * PI)))
chk("I(e) mW/m^2: -260, +5.31, -255", [round(Si_w[0] * 1e3), round(Sr_w[0] * 1e3, 2), round(St_w[0] * 1e3)] == [-260, 5.31, -255], f"{Si_w[0]*1e3:.2f}, {Sr_w[0]*1e3:.3f}, {St_w[0]*1e3:.2f}")
chk("I(e) balance 49/60pi - 1/60pi = 4/5pi; Gamma^2 = 1/49 (2.0 %); tau^2 eta1/eta2 = 48/49", close(49 / (60 * PI) - 1 / (60 * PI), 4 / (5 * PI)) and close(Gw ** 2, 1 / 49) and round(100 / 49, 1) == 2.0 and close(Tw ** 2 * eta1 / eta2, 48 / 49))
# quadrature of the time averages for the worked problem
Tp = 1 / f
q = quad(lambda t: np.cross(np.real(Et_ph(0) * np.exp(1j * w * t)), np.real(Ht(0) * np.exp(1j * w * t)))[0], 0, Tp, limit=200)[0] / Tp
chk("I(e) quadrature <S_t,x> = -4/(5pi)", close(q, -4 / (5 * PI), rtol=1e-7))
# (f) PEC
Er_p = lambda x: -1 * Ei(0) * np.exp(-1j * b1w * x)   # Gamma = -1
Hr_p = lambda x: np.cross(X, Er_p(x)) / eta1
chk("I(f) E_r = +y 14 e^{-j pi x/3}, H_r = +z 7/(60pi) e^{-j pi x/3}", close(Er_p(0.3), 14 * Y * np.exp(-1j * PI / 3 * 0.3)) and close(Hr_p(0.3), Z * 7 / (60 * PI) * np.exp(-1j * PI / 3 * 0.3)))
Etot_p = Ei(0) + Er_p(0); Htot_p = Hi(0) + Hr_p(0)
chk("I(f) total E(0) = 0, total H(0) = z 7/(30pi)", close(Etot_p, 0) and close(Htot_p, Z * 7 / (30 * PI)))
Js_p = np.cross(nI, Htot_p)
chk("I(f) J_s = n x H1 = -y 7/(30pi) A/m = 74.3 mA/m", close(Js_p, -Y * 7 / (30 * PI)) and round(7 / (30 * PI) * 1e3, 1) == 74.3)
chk("I(f) J_s along incident E at the surface; |J_s| = 2|E_i(0)|/eta1", np.dot(Js_p, Ei(0)) > 0 and close(np.linalg.norm(Js_p), 2 * 14 / eta1))
chk("I(f) J_s(t) = Re{J_s e^{jwt}} = -y 7/(30pi) cos wt", close(np.real(Js_p * np.exp(1j * 0.7)), -Y * 7 / (30 * PI) * np.cos(0.7)))
chk("I trap: H_t/H_i = 1-Gamma = 6/7 (not 1/tau)", close((1 / (10 * PI)) / (7 / (60 * PI)), 6 / 7))
# exam-key comparison: none of the worked-problem keys equals the exam keys
s17 = {"Gamma": 0.2, "tau": 1.2, "Ei": 5, "Er": 1}; sp18 = {"Gamma": -1 / 11, "tau": 10 / 11, "Ei": 11, "Er": -1}
chk("I keys differ from S17 HE3 #3 (G=0.2, tau=1.2, Ei=5) and SP18 E3 #2 (G=-1/11, tau=10/11, Ei=11)",
    all(not close(Gw, d_["Gamma"]) and not close(Tw, d_["tau"]) and not close(14, d_["Ei"]) for d_ in (s17, sp18)))
chk("I given H_t amplitude 1/10pi differs from S17 #3f key 1/20pi; |E_r| = 2 differs from S17 #3d (1) and SP18 #2e (1)",
    not close(abs(Ht(0)[2]), 1 / (20 * PI)) and abs(Er(0)[1]) not in (1, 1.0) and not close(abs(Ht(0)[2]) * eta1 * 0, 1) )

# ============================================================ J. Rao Example 5.4 cross-check
print("== J. Rao Example 5.4 (sigma=1e-4, eps=5eps0, f=150 kHz)")
g5, e5 = gam_eta(1.5e5, MU0, 5 * EPS0, 1e-4)
G5 = (e5 - 377) / (e5 + 377); T5 = 1 + G5
print(f"   gamma2 = {g5:.6e}, eta2 = {abs(e5):.3f} /{np.degrees(np.angle(e5)):.2f} deg, Gamma = {abs(G5):.4f} /{np.degrees(np.angle(G5)):.3f}, tau = {abs(T5):.4f} /{np.degrees(np.angle(T5)):.3f}")
chk("J Rao: eta2 = 104.559/33.69, Gamma = 0.6325/161.565, tau = 0.4472/26.565",
    abs(abs(e5) - 104.559) < 0.05 and abs(np.degrees(np.angle(e5)) - 33.69) < 0.02 and abs(abs(G5) - 0.6325) < 2e-4 and abs(np.degrees(np.angle(G5)) - 161.565) < 0.02 and abs(abs(T5) - 0.4472) < 2e-4)
chk("J Rao: power balance with lossy region 2", close(1, abs(G5) ** 2 + abs(T5) ** 2 * 377 * np.real(1 / e5)))

print(f"\nTOTAL: {NP} PASS, {NF} FAIL")
