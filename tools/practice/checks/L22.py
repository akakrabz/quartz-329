#!/usr/bin/env python3
"""L22 practice checks: phasor Maxwell equations and damped waves in conducting media (numpy only).

Every number, sign and direction on practice/22-damped-waves-in-conducting-media.md is printed here.

* gamma and eta: principal complex square roots (np.sqrt, Re >= 0, so alpha >= 0 and Re eta >= 0) of
  j w mu (sigma + j w eps) and j w mu / (sigma + j w eps), compared with the hand values and with
  gamma*eta = j w mu and gamma/eta = sigma + j w eps. Both roots are printed where the page discusses them.
* H from E: np.cross(u, E~)/eta with complex phasor vectors (E from H: eta * np.cross(H~, u)).
* Every (E~, H~) pair: phasor Faraday and Ampere-Maxwell (with sigma E) and both divergences by finite
  differences; the time-domain fields Re{X~ e^{jwt}} against the time-domain laws (curl E = -mu dH/dt,
  curl H = sigma E + eps dE/dt) by finite differences in space and time.
* Every time-domain formula written on the page (with its rounded numbers) is compared with Re{X~ e^{jwt}}.
* Time averages <E x H> are brute-force means over one period, compared with 1/2 Re{E~ x H~*}.
Course constants (as on the exams): eps0 = 1e-9/(36 pi), mu0 = 4 pi 1e-7, c = 3e8, eta0 = 120 pi;
the exact constants are printed alongside where they change a printed digit.
"""
import numpy as np

mu0 = 4e-7 * np.pi
eps0 = 8.8541878128e-12          # exact
c = 2.99792458e8
qe = 1.602176634e-19
me = 9.1093837e-31
eps0c = 1e-9 / (36 * np.pi)      # course value
cC = 3e8
eta0c = 120 * np.pi
eta0 = np.sqrt(mu0 / eps0)
X, Y, Z = np.eye(3)
ALL = []
rng = np.random.default_rng(22)
NAMES = {(1, 0, 0): "+x", (-1, 0, 0): "-x", (0, 1, 0): "+y", (0, -1, 0): "-y", (0, 0, 1): "+z", (0, 0, -1): "-z"}


def hdr(s):
    print("\n" + "=" * 78 + "\n" + s + "\n" + "=" * 78)


def check(label, cond):
    print(f"  [{label}] {'OK' if cond else 'FAIL'}")
    ALL.append(bool(cond))


def close(label, a, b, rtol=1e-9, atol=0.0):
    ok = np.allclose(a, b, rtol=rtol, atol=atol)
    print(f"  [{label}] {a} vs {b} -> {'OK' if ok else 'FAIL'}")
    ALL.append(bool(ok))
    return ok


def deg(z):
    return np.degrees(np.angle(z))


def pol(z, d=4):
    return f"{abs(z):.{d}f} e^(j{deg(z):.{max(d - 2, 2)}f} deg)"


def rect(z, d=4):
    return f"{z.real:.{d}f} {z.imag:+.{d}f}j"


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


def media(omega, mu, sigma, eps, label=""):
    """principal roots; prints gamma^2, both roots, eta^2, both roots."""
    y = sigma + 1j * omega * eps
    g2 = 1j * omega * mu * y
    g = np.sqrt(g2)
    n2 = 1j * omega * mu / y
    n = np.sqrt(n2)
    assert g.real >= 0 and n.real >= 0
    if label:
        print(f"  {label}: sigma + j w eps = {rect(y, 6)} S/m, sigma/(w eps) = {sigma / (omega * eps):.6f}")
        print(f"  {label}: gamma^2 = {rect(g2, 6)} 1/m^2 -> roots +/-({rect(g, 6)}); principal gamma = {pol(g)}")
        print(f"  {label}: eta^2 = {rect(n2, 4)} Ohm^2 -> roots +/-({rect(n, 4)}); principal eta = {pol(n)} Ohm")
        print(f"  {label}: gamma*eta = {rect(g * n, 6)} vs j w mu = {rect(1j * omega * mu, 6)}; "
              f"gamma/eta = {rect(g / n, 8)} vs sigma + j w eps = {rect(y, 8)}")
        check(f"{label} gamma*eta = j w mu and gamma/eta = sigma + j w eps",
              np.isclose(g * n, 1j * omega * mu) and np.isclose(g / n, y))
    return g2, g, n2, n


def general(omega, mu, sigma, eps):
    """closed forms of Lecture 22 section 5"""
    x = sigma / (omega * eps)
    pre = omega * np.sqrt(mu * eps / 2)
    a = pre * np.sqrt(np.sqrt(1 + x ** 2) - 1)
    b = pre * np.sqrt(np.sqrt(1 + x ** 2) + 1)
    neta = np.sqrt(mu / eps) / (1 + x ** 2) ** 0.25
    tau = 0.5 * np.arctan(x)
    return a, b, neta, tau


# ------------------------------------------------------------- finite-difference machinery
def jac_c(F, r, h):
    J = np.zeros((3, 3), complex)
    for j in range(3):
        d = np.zeros(3); d[j] = h
        J[:, j] = (F(r + d) - F(r - d)) / (2 * h)
    return J


def curl_c(F, r, h):
    J = jac_c(F, r, h)
    return np.array([J[2, 1] - J[1, 2], J[0, 2] - J[2, 0], J[1, 0] - J[0, 1]])


def div_c(F, r, h):
    return np.trace(jac_c(F, r, h))


def lap_c(F, r, h):
    out = -6 * F(r)
    for j in range(3):
        d = np.zeros(3); d[j] = h
        out = out + F(r + d) + F(r - d)
    return out / h ** 2


def rel(a, b):
    s = max(np.linalg.norm(a), np.linalg.norm(b), 1e-300)
    return np.linalg.norm(np.asarray(a) - np.asarray(b)) / s


def phasor_maxwell(label, Ef, Hf, omega, mu, sigma, eps, pts, h):
    rf = ra = dv = 0.0
    for r in pts:
        r = np.asarray(r, float)
        cE, cH = curl_c(Ef, r, h), curl_c(Hf, r, h)
        rf = max(rf, rel(cE, -1j * omega * mu * Hf(r)))
        ra = max(ra, rel(cH, (sigma + 1j * omega * eps) * Ef(r)))
        dv = max(dv, abs(div_c(Ef, r, h)) / max(np.linalg.norm(cE), 1e-300),
                 abs(div_c(Hf, r, h)) / max(np.linalg.norm(cH), 1e-300))
    ok = max(rf, ra) < 1e-6 and dv < 1e-6
    print(f"  [{label}] phasor Faraday rel.res {rf:.1e} | Ampere-Maxwell (sigma + j w eps) {ra:.1e} | div/curl {dv:.1e}"
          f" -> {'OK' if ok else 'FAIL'}")
    ALL.append(ok)
    return ok


def time_maxwell(label, Ef, Hf, omega, mu, sigma, eps, pts, h):
    E = lambda r, t: np.real(Ef(r) * np.exp(1j * omega * t))
    H = lambda r, t: np.real(Hf(r) * np.exp(1j * omega * t))
    ht = 1e-4 / omega
    rf = ra = 0.0
    for r in pts:
        r = np.asarray(r, float)
        t = rng.uniform(0, 2 * np.pi / omega)

        def Et(rr): return E(rr, t)

        def Ht(rr): return H(rr, t)
        cE = np.real(curl_c(Et, r, h)); cH = np.real(curl_c(Ht, r, h))
        dH = (H(r, t + ht) - H(r, t - ht)) / (2 * ht)
        dE = (E(r, t + ht) - E(r, t - ht)) / (2 * ht)
        scale_f = max(np.linalg.norm(cE), np.linalg.norm(mu * dH), 1e-300)
        scale_a = max(np.linalg.norm(cH), np.linalg.norm(sigma * E(r, t) + eps * dE), 1e-300)
        rf = max(rf, np.linalg.norm(cE + mu * dH) / scale_f)
        ra = max(ra, np.linalg.norm(cH - sigma * E(r, t) - eps * dE) / scale_a)
    ok = max(rf, ra) < 1e-5
    print(f"  [{label}] time domain: curl E = -mu dH/dt rel.res {rf:.1e} | curl H = sigma E + eps dE/dt {ra:.1e}"
          f" -> {'OK' if ok else 'FAIL'}")
    ALL.append(ok)
    return ok


def tavg_S(Ef, Hf, omega, r, N=4000):
    r = np.asarray(r, float)
    ts = np.arange(N) / N * 2 * np.pi / omega
    Ev, Hv = Ef(r), Hf(r)
    acc = np.zeros(3)
    for t in ts:
        acc += np.cross(np.real(Ev * np.exp(1j * omega * t)), np.real(Hv * np.exp(1j * omega * t)))
    brute = acc / N
    formula = 0.5 * np.real(np.cross(Ev, np.conj(Hv)))
    return brute, formula


def formula_vs_phasor(label, fF, Fph, omega, pts, rtol):
    """compare a time-domain formula as written on the page with Re{F~ e^{jwt}}."""
    worst = 0.0
    for r in pts:
        r = np.asarray(r, float)
        for _ in range(5):
            t = rng.uniform(0, 2 * np.pi / omega)
            a = fF(r, t)
            b = np.real(Fph(r) * np.exp(1j * omega * t))
            amp = np.linalg.norm(Fph(r))
            worst = max(worst, np.linalg.norm(a - b) / amp)
    ok = worst < rtol
    print(f"  [{label}] page's time-domain formula vs Re(phasor e^jwt): max rel. dev. {worst:.1e} (tol {rtol:g})"
          f" -> {'OK' if ok else 'FAIL'}")
    ALL.append(ok)


def rpts(n, lo, hi):
    return [rng.uniform(lo, hi, 3) for _ in range(n)]


# =====================================================================================================
hdr("22.1 Phasor Maxwell, true or false")
# (a) phasor Faraday / Ampere-Maxwell in a conducting medium: test on the 22.6 medium's +z wave
w6, s6, e6 = 3e8, 1 / (10 * np.pi), 5 * eps0c
g2_6, g6, n2_6, n6 = media(w6, mu0, s6, e6)
Ef = lambda r: X * 2.0 * np.exp(-g6 * r[2])
Hf = lambda r: np.cross(Z, Ef(r)) / n6
phasor_maxwell("(a) curl E~ = -j w mu H~, curl H~ = (sigma + j w eps) E~ on a damped wave", Ef, Hf, w6, mu0, s6, e6,
               rpts(6, -1, 1), 1e-5)
# (b) continuity: phasor of d(rho)/dt is +j w rho~  ->  div J~ + j w rho~ = 0  ->  div J~ = -j w rho~
rho_ph, w1 = 2 * np.exp(0.3j), 2 * np.pi * 1e6
for t in (0.11e-6, 0.37e-6, 0.83e-6):
    ht = 1e-12
    fd = (np.real(rho_ph * np.exp(1j * w1 * (t + ht))) - np.real(rho_ph * np.exp(1j * w1 * (t - ht)))) / (2 * ht)
    ph = np.real(1j * w1 * rho_ph * np.exp(1j * w1 * t))
    check(f"(b) d rho/dt at t = {t:.2e}: finite difference {fd:.6e} = Re(+j w rho~ e^jwt) {ph:.6e}", np.isclose(fd, ph, rtol=1e-6))
print("  (b) so continuity is div J~ + j w rho~ = 0, i.e. div J~ = -j w rho~ (statement's +j w rho~ is FALSE)")
# (c) div of Ampere-Maxwell + continuity -> div D~ = rho~ (any smooth J~, H~)
Hs = lambda r: np.array([np.sin(r[1]) * np.exp(1j * r[2]), r[0] ** 2 * np.cos(r[2]), np.exp(r[0] + 1j * r[1])])
Js = lambda r: np.array([r[0] * r[1] + 1j * r[2] ** 2, np.sin(r[0]) * np.exp(1j * r[1]), r[2] * np.cos(r[0])])
wc = 7.0
Ds = lambda r: (curl_c(Hs, r, 1e-4) - Js(r)) / (1j * wc)
worst = 0.0
for r in rpts(5, -1, 1):
    divD = div_c(Ds, r, 1e-3)
    rho_c = -div_c(Js, r, 1e-4) / (1j * wc)
    worst = max(worst, abs(divD - rho_c) / abs(rho_c))
check(f"(c) div D~ (with D~ from Ampere-Maxwell) equals rho~ = -div J~/(j w): max rel. dev. {worst:.1e}", worst < 1e-5)
# (d) relaxation: (sigma + j w eps) rho~ = 0
sd, ed, wd = 0.1, 10 * eps0c, 2 * np.pi * 1e6
yd = sd + 1j * wd * ed
print(f"  (d) sigma + j w eps = {rect(yd, 6)} S/m (nonzero) -> rho~ = 0 for any field strength")
print(f"  (d) relaxation time eps/sigma = {ed / sd:.4e} s = {ed / sd * 1e9:.3f} ns (exact eps0: {10 * eps0 / sd * 1e9:.3f} ns);"
      f" period at 1 MHz = {1 / 1e6 * 1e6:.1f} us; ratio period/(eps/sigma) = {1e-6 / (ed / sd):.0f}")
check("(d) sigma + j w eps != 0", abs(yd) > 0)
# (e) complex permittivity
r_c = sd / (wd * eps0c)
print(f"  (e) sigma/(w eps0) = {r_c:.4f} (course eps0) / {sd / (wd * eps0):.1f} (exact eps0) -> eps_c/eps0 = 10 - j{r_c:.0f}")
epsc = ed - 1j * sd / wd
check("(e) j w eps_c = sigma + j w eps", np.isclose(1j * wd * epsc, yd))
print(f"  (e) sigma/(w eps) = {sd / (wd * ed):.1f}  (conduction current 180 x displacement current)")
# (f) phases of the two currents relative to E
print(f"  (f) angle of sigma (conduction current / E): {deg(sd + 0j):.1f} deg; angle of j w eps (displacement / E): {deg(1j * wd * ed):.1f} deg"
      " -> conduction in phase, displacement leads by 90 deg (statement reversed: FALSE)")
print("  ANSWER 22.1: (a) T (b) F (c) T (d) F (e) T (f) F")

# =====================================================================================================
hdr("22.2 Which phasors are allowed (gamma^2 = -8 + j6 1/m^2)")
G2 = -8 + 6j
G = np.sqrt(G2)
print(f"  principal sqrt(-8 + 6j) = {rect(G)}  (1 + j3), |gamma| = sqrt(10) = {abs(G):.4f}")
check("(1 + 3j)^2 = -8 + 6j", np.isclose((1 + 3j) ** 2, G2))
g = 1 + 3j
u_obl = np.array([0, 0.6, 0.8])
cands = {
    "(a) x 2e^{-(1+3j)z}": lambda r: X * 2 * np.exp(-g * r[2]),
    "(b) y 2e^{+(1+3j)z}": lambda r: Y * 2 * np.exp(g * r[2]),
    "(c) x 2e^{-(3+j)z}": lambda r: X * 2 * np.exp(-(3 + 1j) * r[2]),
    "(d) x 2e^{-(1-3j)z}": lambda r: X * 2 * np.exp(-(1 - 3j) * r[2]),
    "(e) z 2e^{-(1+3j)z}": lambda r: Z * 2 * np.exp(-g * r[2]),
    "(f) x 2e^{-(1+3j)(0.6y+0.8z)}": lambda r: X * 2 * np.exp(-g * (0.6 * r[1] + 0.8 * r[2])),
}
verdicts = {}
for name, F in cands.items():
    r0 = np.array([0.13, -0.21, 0.37])
    L = lap_c(F, r0, 1e-3)
    comp = np.argmax(np.abs(F(r0)))
    ratio = L[comp] / F(r0)[comp]
    dv = div_c(F, r0, 1e-5)
    helm = abs(ratio - G2) < 1e-4 * abs(G2)
    gauss = abs(dv) < 1e-6 * np.linalg.norm(F(r0)) * abs(G)
    verdicts[name] = helm and gauss
    print(f"  {name:32s} lap/E = {rect(ratio, 4)} (need -8+6j: {'yes' if helm else 'NO'}); "
          f"div E = {abs(dv):.2e} ({'0' if gauss else 'NONZERO'}) -> {'ALLOWED' if helm and gauss else 'not allowed'}")
print(f"  (c) (3+j)^2 = {(3 + 1j) ** 2}; (d) (1-3j)^2 = {(1 - 3j) ** 2}; (f) 0.6^2 + 0.8^2 = {0.36 + 0.64:.2f}")
print("  (d) e^{-(1-3j)z} = e^{-z} e^{+j3z}: phase says travel -z, amplitude grows toward -z (grows along its travel)")
print("  (e) div E~ = dEz/dz = -gamma Ez != 0")
check("22.2 key = (a), (b), (f)", [k for k, v in verdicts.items() if v] == ["(a) x 2e^{-(1+3j)z}", "(b) y 2e^{+(1+3j)z}",
                                                                          "(f) x 2e^{-(1+3j)(0.6y+0.8z)}"])
# (b) and (f): the full wave (H from Faraday) satisfies both phasor curl equations in some medium with gamma^2 = -8+6j
# pick the Lecture 22 section-5 medium: omega = 3e8, mu0 -> sigma + j w eps = gamma^2/(j w mu0)
w2 = 3e8
y2 = G2 / (1j * w2 * mu0)
n2v = 1j * w2 * mu0 / G
print(f"  medium with this gamma^2 at w = 3e8, mu0: sigma + j w eps = {rect(y2, 6)} (sigma = 1/(20 pi) = {1 / (20 * np.pi):.6f},"
      f" eps = {y2.imag / w2 / eps0c:.3f} eps0); eta = {pol(n2v)}")
for name, F, u in (("(a)", cands["(a) x 2e^{-(1+3j)z}"], Z), ("(b)", cands["(b) y 2e^{+(1+3j)z}"], -Z),
                   ("(f)", cands["(f) x 2e^{-(1+3j)(0.6y+0.8z)}"], u_obl)):
    Hf = (lambda F, u: (lambda r: np.cross(u, F(r)) / n2v))(F, u)
    phasor_maxwell(f"22.2 {name} with H~ = u x E~/eta", F, Hf, w2, mu0, y2.real, y2.imag / w2, rpts(4, -1, 1), 1e-5)

# =====================================================================================================
hdr("22.3 Reading a damped wave: E = x 20 e^{-0.5z} cos(2pi 1e8 t - 2pi z + 45deg) V/m")
w3, a3, b3 = 2 * np.pi * 1e8, 0.5, 2 * np.pi
g3 = a3 + 1j * b3
print(f"  travel: opposite signs on t and z -> +z; e^(-0.5 z) decays toward +z (consistent)")
print(f"  omega = {w3:.4e} rad/s, f = {w3 / 2 / np.pi / 1e6:.1f} MHz, alpha = {a3} Np/m, beta = {b3:.4f} rad/m")
print(f"  gamma = {rect(g3)} 1/m = {pol(g3)} 1/m")
print(f"  lambda = 2pi/beta = {2 * np.pi / b3:.4f} m, v_p = w/beta = {w3 / b3:.4e} m/s, delta = 1/alpha = {1 / a3:.1f} m")
print(f"  e^-2 = {np.exp(-2):.5f}, e^-4 = {np.exp(-4):.5f}")
print(f"  at z = 4 m: amplitude 20 e^-2 = {20 * np.exp(-a3 * 4):.4f} V/m ({np.exp(-2) * 100:.2f} %), power fraction e^-4 = {np.exp(-4):.5f} ({np.exp(-4) * 100:.2f} %)")
print(f"  per wavelength the amplitude is multiplied by e^(-alpha lambda) = e^-0.5 = {np.exp(-0.5):.4f}")
print(f"  alpha/beta = {a3 / b3:.4f} -> tau = {np.degrees(np.arctan(a3 / b3)):.2f} deg, sigma/(w eps) = 2ab/(b^2-a^2) = {2 * a3 * b3 / (b3 ** 2 - a3 ** 2):.4f}")
print(f"  (for reference, eps of a non-magnetic medium with this gamma: (b^2-a^2)/(w^2 mu0) = {(b3 ** 2 - a3 ** 2) / (w3 ** 2 * mu0) / eps0c:.3f} eps0)")
fE = lambda r, t: X * 20 * np.exp(-0.5 * r[2]) * np.cos(2 * np.pi * 1e8 * t - 2 * np.pi * r[2] + np.radians(45))
Eph3 = lambda r: X * 20 * np.exp(1j * np.radians(45)) * np.exp(-g3 * r[2])
formula_vs_phasor("22.3 E", fE, Eph3, w3, rpts(4, 0, 3), 1e-12)

# =====================================================================================================
hdr("22.4 Possible or not possible")
xs = np.logspace(-6, 8, 20001)
taus = 0.5 * np.arctan(xs)
print(f"  scan sigma/(w eps) from 1e-6 to 1e8: max alpha/beta = tan tau = {np.tan(taus).max():.8f} (< 1), "
      f"max tau = {np.degrees(taus.max()):.6f} deg (< 45)")
# (a)
print(f"  (a) alpha/beta = 2/0.5 = {2 / 0.5:.0f} > 1 -> NOT POSSIBLE")
check("(a) beta >= alpha always", np.tan(taus).max() < 1)
# (b)
w4 = 2 * np.pi * 1e9
x4 = 0.01 / (w4 * 4 * eps0c)
print(f"  (b) w eps = 2 pi 1e9 * 4e-9/(36 pi) = {w4 * 4 * eps0c:.4f} S/m (= 8/36)")
_, g4, _, n4 = media(w4, mu0, 0.01, 4 * eps0c)
print(f"  (b) sigma/(w eps) = {x4:.6f} (course eps0; = 9/200) / {0.01 / (w4 * 4 * eps0):.5f} (exact) -> imperfect dielectric")
print(f"  (b) exact alpha = {g4.real:.5f} Np/m, beta = {g4.imag:.4f} rad/m, alpha/beta = {g4.real / g4.imag:.5f}")
print(f"  (b) shortcuts: (sigma/2)sqrt(mu/eps) = {0.005 * 60 * np.pi:.4f} Np/m, w sqrt(mu eps) = {w4 * 2 / cC:.4f} rad/m")
check("(b) alpha << beta", g4.real / g4.imag < 0.05)
# (c)
lead = 2 * np.pi * 50e6 * 2e-9
print(f"  (c) 2 ns at 50 MHz = {np.degrees(lead):.1f} deg; H lags E by tau >= 0, so a lead is NOT POSSIBLE;"
      f" the largest possible lag is 45 deg = {0.125 / 50e6 * 1e9:.2f} ns")
# (d)
ab_d = 10 / (2 * np.pi)
dl = 1 / (2 * np.pi * np.tan(taus))
print(f"  (d) delta = lambda/10 -> alpha lambda = 10 -> alpha/beta = 10/(2 pi) = {ab_d:.4f} > 1 -> NOT POSSIBLE;"
      f" min delta/lambda over the scan = {dl.min():.6f} -> 1/(2 pi) = {1 / (2 * np.pi):.6f}")
print(f"  (d) good-conductor limit: per wavelength e^(-2 pi) = {np.exp(-2 * np.pi):.5f} ({np.exp(-2 * np.pi) * 100:.2f} %)")
check("(d) delta >= lambda/(2 pi)", dl.min() > 1 / (2 * np.pi) * (1 - 1e-9))
# (e) collisionless plasma below cutoff: N = 1e11, f = 2 MHz
Np = 1e11
wp = np.sqrt(Np * qe ** 2 / (me * eps0))
fp = wp / 2 / np.pi
w_e = 2 * np.pi * 2e6
sig_pl = Np * qe ** 2 / (1j * w_e * me)
_, gpl, _, npl = media(w_e, mu0, sig_pl, eps0)
print(f"  (e) plasma N = 1e11 m^-3: f_p = {fp / 1e6:.3f} MHz (9 sqrt(N) = {9 * np.sqrt(Np) / 1e6:.3f} MHz)")
print(f"  (e) at 2 MHz: sigma = {rect(sig_pl, 8)} S/m (purely imaginary), gamma = {rect(gpl, 6)} 1/m (real),"
      f" delta = {1 / gpl.real:.2f} m, eta = {rect(npl, 3)} Ohm (purely imaginary)")
check("(e) plasma: sqrt((wp^2 - w^2))/c = gamma", np.isclose(gpl.real, np.sqrt(wp ** 2 - w_e ** 2) / c, rtol=1e-9))
Ef = lambda r: X * np.exp(-gpl * r[2]); Hf = lambda r: np.cross(Z, Ef(r)) / npl
brute, form = tavg_S(Ef, Hf, w_e, [0, 0, 3.0])
print(f"  (e) <S> at z = 3 m: brute {brute} formula {form} W/m^2 (zero); Re(sigma) = {sig_pl.real} -> no Joule heating")
check("(e) <S> = 0 below cutoff", np.linalg.norm(brute) < 1e-12 and abs(form[2]) < 1e-15)
print("  ANSWER 22.4: (a) NP (b) P (c) NP (d) NP (e) P")

# =====================================================================================================
hdr("22.5 Find the error: E = z 60 e^{-ax} cos(wt - bx), travel +x, eta = 150 e^{j20 deg} Ohm")
eta5 = 150 * np.exp(1j * np.radians(20))
u5, E5 = X, Z * 60
H5 = np.cross(u5, E5) / eta5
print(f"  u x E-hat = x x z = {dname(np.cross(X, Z))}; H~(0) = {H5} -> |H| = {abs(H5[1]):.3f} A/m, phase {deg(H5[1]) - 180:.1f} deg"
      " relative to -y")
print("  correct: H = -y 0.4 e^{-ax} cos(wt - bx - 20deg) A/m (H lags E by 20 deg); student: +20 deg (leads)")
# a consistent medium for a numeric test: mu0, omega = 1e8 -> |gamma| = w mu0/|eta|, angle 70 deg
w5 = 1e8
g5 = w5 * mu0 / 150 * np.exp(1j * np.radians(70))
print(f"  test medium: w = 1e8, mu0 -> gamma = {rect(g5)} (|gamma| = {abs(g5):.4f}, angle 70 deg); "
      f"sigma + j w eps = gamma/eta = {rect(g5 / eta5, 6)} (Re > 0: passive)")
Ef = lambda r: Z * 60 * np.exp(-g5 * r[0])
Hc = lambda r: -Y * 0.4 * np.exp(-1j * np.radians(20)) * np.exp(-g5 * r[0])
Hs = lambda r: -Y * 0.4 * np.exp(+1j * np.radians(20)) * np.exp(-g5 * r[0])
y5 = g5 / eta5
phasor_maxwell("22.5 corrected H", Ef, Hc, w5, mu0, y5.real, y5.imag / w5, rpts(4, -2, 2), 1e-5)
r0 = np.array([0.3, 0.1, -0.2])
res_s = rel(curl_c(Ef, r0, 1e-5), -1j * w5 * mu0 * Hs(r0))
print(f"  student's H in Faraday's law: rel. residual {res_s:.3f} (fails)")
check("22.5 student's H fails Faraday", res_s > 0.1)
for lab, Hf in (("correct", Hc), ("student", Hs)):
    brute, form = tavg_S(Ef, Hf, w5, [0, 0, 0])
    print(f"  <S> at x = 0 with the {lab} H: brute {brute[0]:.4f} x-hat, formula {form[0]:.4f} W/m^2")
print(f"  1/2 * 60 * 0.4 * cos 20 = {0.5 * 60 * 0.4 * np.cos(np.radians(20)):.4f} W/m^2 for both -> power cannot detect the slip")
print(f"  a lead (tau = -20 deg) would need sigma/(w eps) = tan(-40 deg) = {np.tan(np.radians(-40)):.3f} < 0 (active medium)")

# =====================================================================================================
hdr("22.6 From the medium to the wave: mu0, eps = 5 eps0, sigma = 1/(10 pi) S/m, w = 3e8 rad/s")
we = w6 * e6
print(f"  w eps = {we:.6f} S/m = 1/(24 pi) = {1 / (24 * np.pi):.6f}; sigma = {s6:.6f} S/m = 1/(10 pi)")
print(f"  sigma + j w eps = {rect(s6 + 1j * we, 6)} S/m = (12 + 5j)/(120 pi): {rect((12 + 5j) / (120 * np.pi), 6)}")
print(f"  in mS/m: {s6 * 1e3:.1f} + j{we * 1e3:.1f}; sigma/(w eps) = {s6 / we:.4f}")
print(f"  eps_c/eps0 = 5 - j sigma/(w eps0) = 5 - j{s6 / (w6 * eps0c):.4f}")
g2_6, g6, n2_6, n6 = media(w6, mu0, s6, e6, "22.6")
check("22.6 gamma^2 = -5 + 12j", np.isclose(g2_6, -5 + 12j))
check("22.6 gamma = 2 + 3j (principal root)", np.isclose(g6, 2 + 3j))
print(f"  other root: {rect(-g6)} (alpha < 0); e^(-(-2-3j)z) = e^(+2z) e^(+j3z): travels -z, grows along its travel")
print(f"  |gamma| = sqrt(13) = {np.sqrt(13):.4f}, angle = {deg(g6):.2f} deg")
check("22.6 eta = (120 pi/13)(3 + 2j)", np.isclose(n6, 120 * np.pi / 13 * (3 + 2j)))
print(f"  120 pi/13 = {120 * np.pi / 13:.4f} Ohm; eta = {rect(n6, 2)} Ohm = {pol(n6, 2)} Ohm; |eta| = 120 pi/sqrt(13) = {120 * np.pi / np.sqrt(13):.2f}")
print(f"  eta^2 = (120 pi/13)^2 (5 + 12j) = {rect((120 * np.pi / 13) ** 2 * (5 + 12j), 1)} Ohm^2 (computed {rect(n2_6, 1)})")
print(f"  other eta root {rect(-n6, 2)} has Re < 0 (angle {deg(-n6):.2f} deg): would give <S> against the travel")
print(f"  tau = atan(2/3) = {np.degrees(np.arctan(2 / 3)):.2f} deg; 90 - angle(gamma) = {90 - deg(g6):.2f} deg")
print(f"  delta = {1 / g6.real:.3f} m, lambda = 2pi/3 = {2 * np.pi / g6.imag:.4f} m, v_p = {w6 / g6.imag:.4e} m/s")
bL = w6 * np.sqrt(mu0 * e6); nL = np.sqrt(mu0 / e6)
print(f"  lossless (sigma = 0): beta = sqrt(5) = {bL:.4f} rad/m (course c: {w6 * np.sqrt(5) / cC:.4f}), eta = 120 pi/sqrt 5 = {120 * np.pi / np.sqrt(5):.2f} Ohm")
print(f"  beta/beta_L = {g6.imag / bL:.4f} (+{(g6.imag / bL - 1) * 100:.0f} %), |eta|/eta_L = {abs(n6) / nL:.4f} (-{(1 - abs(n6) / nL) * 100:.0f} %)")
a_, b_, ne_, ta_ = general(w6, mu0, s6, e6)
print(f"  general formulas: w sqrt(mu eps/2) = sqrt(5/2) = {w6 * np.sqrt(mu0 * e6 / 2):.4f}, sqrt(1 + 2.4^2) = {np.sqrt(1 + 2.4 ** 2):.4f}"
      f" -> alpha = {a_:.6f}, beta = {b_:.6f}, |eta| = {ne_:.3f}, tau = {np.degrees(ta_):.3f} deg")
check("22.6 general formulas agree", np.allclose([a_, b_, ne_, ta_], [g6.real, g6.imag, abs(n6), np.angle(n6)]))
_, g6x, _, n6x = media(w6, mu0, s6, 5 * eps0)
print(f"  with the exact eps0: gamma = {rect(g6x)}, eta = {pol(n6x, 2)}")
Ef = lambda r: X * np.exp(-g6 * r[2]); Hf = lambda r: np.cross(Z, Ef(r)) / n6
phasor_maxwell("22.6 +z wave", Ef, Hf, w6, mu0, s6, e6, rpts(5, -1, 1), 1e-5)
time_maxwell("22.6 +z wave", Ef, Hf, w6, mu0, s6, e6, rpts(5, -1, 1), 1e-5)

# =====================================================================================================
hdr("22.7 Microwave heating: eps_c = (52 - j17) eps0 at 2.45 GHz, mu0, E0 = 1000 V/m just inside (z = 0+), travel +z")
w7 = 2 * np.pi * 2.45e9
sig7c, sig7x = w7 * eps0c * 17, w7 * eps0 * 17
print(f"  omega = {w7:.5e} rad/s; sigma = w eps0 * 17 = {sig7c:.4f} S/m (course eps0) / {sig7x:.4f} S/m (exact)")
print(f"  sigma/(w eps) = 17/52 = {17 / 52:.4f}")
sq = np.sqrt(52 - 17j)
print(f"  |sqrt(52 - 17j)| = {abs(sq):.6f}")
print(f"  sqrt(52 - 17j) = {rect(sq)} = {pol(sq)}; |52 - 17j| = {abs(52 - 17j):.3f}, angle(52 - 17j) = {deg(52 - 17j):.3f} deg, halved {deg(52 - 17j) / 2:.3f}")
k7c, k7x = w7 / cC, w7 / c
g7 = 1j * k7c * sq
g7x = 1j * k7x * sq
print(f"  w/c = {k7c:.4f} (c = 3e8) / {k7x:.4f} (exact) rad/m")
print(f"  gamma = j (w/c) sqrt(52 - 17j) = {rect(g7, 3)} 1/m (course) / {rect(g7x, 3)} (exact c)")
_, g7m, _, n7m = media(w7, mu0, sig7c, 52 * eps0c, "22.7 (course constants)")
check("22.7 j w sqrt(mu0 eps_c) = sqrt(j w mu (sigma + j w eps))", np.isclose(g7, g7m))
a7, b7 = g7.real, g7.imag
print(f"  alpha = {a7:.3f} Np/m, beta = {b7:.3f} rad/m; delta = {1 / a7 * 100:.4f} cm, lambda = {2 * np.pi / b7 * 100:.4f} cm,"
      f" free-space lambda = {cC / 2.45e9 * 100:.2f} cm, v_p = {w7 / b7:.4e} m/s")
n7 = eta0c / sq
n7x = eta0 / sq
print(f"  eta = 120 pi/sqrt(52 - 17j) = {pol(n7, 3)} Ohm = {rect(n7, 3)} (exact eta0: {pol(n7x, 3)})")
check("22.7 eta = j w mu0/gamma", np.isclose(n7, 1j * w7 * mu0 / g7))
print(f"  tau = {deg(n7):.3f} deg = atan(alpha/beta) = {np.degrees(np.arctan(a7 / b7)):.3f}; |H| just inside = {1000 / abs(n7):.3f} A/m")
print(f"  tan tau = alpha/beta = {a7 / b7:.5f}; lambda/delta = 2 pi tan tau = {2 * np.pi * a7 / b7:.4f}"
      f" (lambda > delta needs sigma/(w eps) > tan(2 atan(1/2pi)) = {np.tan(2 * np.arctan(1 / (2 * np.pi))):.5f}; here {17 / 52:.5f})")
S0 = 1000 ** 2 / (2 * abs(n7)) * np.cos(np.angle(n7))
print(f"  <S>(0) = E0^2 cos tau/(2|eta|) = {S0:.1f} W/m^2; cos tau = {np.cos(np.angle(n7)):.6f}; 1e6/(2*{abs(n7):.2f}) = {1e6 / (2 * abs(n7)):.1f}")
print(f"  2 alpha = {2 * a7:.3f} 1/m; 2 alpha * 0.01 = {2 * a7 * 0.01:.4f}; 2 alpha * 0.02 = {2 * a7 * 0.02:.4f}")
for zz in (0.01, 0.02):
    print(f"  <S>({zz * 100:.0f} cm) = {S0 * np.exp(-2 * a7 * zz):.1f} W/m^2 (factor e^(-2 alpha z) = {np.exp(-2 * a7 * zz):.5f})")
print(f"  fraction absorbed in the first 1 cm: {1 - np.exp(-2 * a7 * 0.01):.4f}; half-power depth ln2/(2 alpha) = {np.log(2) / (2 * a7) * 1e3:.3f} mm")
print(f"  lossless comparison eps_r = 52: beta = {k7c * np.sqrt(52):.2f} rad/m, eta = {eta0c / np.sqrt(52):.2f} Ohm;"
      f" imperfect-dielectric shortcut alpha = (sigma/2) sqrt(mu/eps) = {sig7c / 2 * eta0c / np.sqrt(52):.3f} Np/m"
      f" ({(sig7c / 2 * eta0c / np.sqrt(52) / a7 - 1) * 100:+.1f} %)")
Ef = lambda r: X * 1000 * np.exp(-g7 * r[2]); Hf = lambda r: np.cross(Z, Ef(r)) / n7
phasor_maxwell("22.7 +z wave", Ef, Hf, w7, mu0, sig7c, 52 * eps0c, rpts(4, 0, 0.03), 1e-7)
for zz in (0.0, 0.01):
    brute, form = tavg_S(Ef, Hf, w7, [0, 0, zz])
    print(f"  brute-force <S> at z = {zz * 100:.0f} cm: {brute[2]:.1f} W/m^2 (formula {form[2]:.1f}), direction {dname(brute)}")
    check(f"22.7 <S> at {zz * 100:.0f} cm", np.isclose(brute[2], form[2], rtol=1e-6) and np.isclose(form[2], S0 * np.exp(-2 * a7 * zz)))

# =====================================================================================================
hdr("22.8 Power into lossy ground: E~ = y 20 e^{0.05(1 + j sqrt3) z} V/m (z <= 0, z up), f = 1 MHz, mu0")
w8 = 2 * np.pi * 1e6
g8 = 0.05 * (1 + 1j * np.sqrt(3))
print(f"  gamma = {rect(g8, 5)} = {pol(g8)} 1/m; alpha = 0.05 Np/m, beta = 0.05 sqrt3 = {g8.imag:.5f} rad/m")
print(f"  e^(+gamma z): phase e^(+j beta z) -> travel -z (down); amplitude e^(0.05 z) shrinks as z decreases (consistent)")
print(f"  delta = {1 / g8.real:.1f} m, lambda = {2 * np.pi / g8.imag:.4f} m")
n8 = 1j * w8 * mu0 / g8
print(f"  w mu0 = 0.8 pi^2 = {w8 * mu0:.4f} Ohm/m; eta = j w mu0/gamma = {pol(n8, 3)} = {rect(n8, 3)} Ohm; 8 pi^2 = {8 * np.pi ** 2:.3f}")
check("22.8 eta = 8 pi^2 e^{j30}", np.isclose(n8, 8 * np.pi ** 2 * np.exp(1j * np.pi / 6)))
u8 = -Z
E8 = Y * 20
H8 = np.cross(u8, E8) / n8
print(f"  u x E-hat = (-z) x y = {dname(np.cross(-Z, Y))}; H~(0) = {H8} A/m -> |H| = {abs(H8[0]):.4f}, phase {deg(H8[0]):.2f} deg")
S8 = 400 / (2 * abs(n8)) * np.cos(np.angle(n8))
print(f"  <S> = -z (400/(2*8 pi^2)) cos30 e^(0.1 z) = -z {S8:.4f} e^(0.1z) W/m^2; 25 sqrt3/(2 pi^2) = {25 * np.sqrt(3) / (2 * np.pi ** 2):.4f}")
print(f"  without cos tau: {400 / (2 * abs(n8)):.4f} W/m^2 (15 % too large: 1/cos30 = {1 / np.cos(np.pi / 6):.4f})")
d1p = np.log(100) / 0.1; d1f = np.log(100) / 0.05
print(f"  10 ln 100 = {d1p:.4f} m, 20 ln 100 = {d1f:.4f} m")
print(f"  power 1 % at depth ln(100)/(2 alpha) = {d1p:.2f} m; field 1 % at ln(100)/alpha = {d1f:.2f} m")
print(f"  absorbed per m^2 in the top 20 m: {S8 * (1 - np.exp(-2)):.4f} W/m^2 = {(1 - np.exp(-2)) * 100:.1f} % of {S8:.4f}")
sig8 = 2 * g8.real * g8.imag / (w8 * mu0); eps8 = (g8.imag ** 2 - g8.real ** 2) / (w8 ** 2 * mu0)
print(f"  the ground (check): sigma = {sig8:.4e} S/m, eps = {eps8:.4e} F/m = {eps8 / eps0c:.2f} eps0 (exact {eps8 / eps0:.2f}), sigma/(w eps) = {sig8 / (w8 * eps8):.4f} = sqrt3")
Ef = lambda r: Y * 20 * np.exp(g8 * r[2]); Hf = lambda r: np.cross(-Z, Ef(r)) / n8
phasor_maxwell("22.8 -z wave", Ef, Hf, w8, mu0, sig8, eps8, rpts(4, -30, 0), 1e-3)
time_maxwell("22.8 -z wave", Ef, Hf, w8, mu0, sig8, eps8, rpts(4, -30, 0), 1e-3)
for zz in (0.0, -20.0, -46.05):
    brute, form = tavg_S(Ef, Hf, w8, [0, 0, zz])
    print(f"  brute-force <S> at z = {zz} m: {brute} W/m^2 ({dname(brute)}), formula -{S8 * np.exp(0.1 * zz):.5f}")
    check(f"22.8 <S> at z = {zz}", np.isclose(brute[2], -S8 * np.exp(0.1 * zz), rtol=1e-6))
fH = lambda r, t: X * 0.2533 * np.exp(0.05 * r[2]) * np.cos(w8 * t + 0.05 * np.sqrt(3) * r[2] - np.pi / 6)
formula_vs_phasor("22.8 H = x 0.253 e^{0.05z} cos(wt + 0.0866 z - 30deg)", fH, Hf, w8, rpts(4, -30, 0), 2e-4)

# =====================================================================================================
hdr("22.9 Decoding: E = z 8 e^{y} cos(6e8 t + 7y + 30 deg) V/m, non-magnetic")
w9 = 6e8
g9 = 1 + 7j
print(f"  same signs on t and y -> travel -y; e^(+y) shrinks toward -y (consistent); sqrt2 = {np.sqrt(2):.4f}")
print(f"  alpha = 1 Np/m, beta = 7 rad/m, gamma = {rect(g9)} = {pol(g9)} 1/m; |gamma| = 5 sqrt2 = {5 * np.sqrt(2):.4f}")
print(f"  angle gamma = {deg(g9):.2f} deg = 90 - atan(1/7) = {90 - np.degrees(np.arctan(1 / 7)):.2f}")
print(f"  f = {w9 / 2 / np.pi / 1e6:.2f} MHz, lambda = 2pi/7 = {2 * np.pi / 7:.4f} m, v_p = {w9 / 7:.4e} m/s, delta = 1 m")
n9 = 1j * w9 * mu0 / g9
print(f"  w mu0 = 240 pi = {w9 * mu0:.3f}; eta = {rect(n9, 3)} = {pol(n9, 3)} Ohm; 4.8 pi (7 + j) = {rect(4.8 * np.pi * (7 + 1j), 3)};"
      f" 24 sqrt2 pi = {24 * np.sqrt(2) * np.pi:.3f}")
check("22.9 eta = 4.8 pi (7 + j)", np.isclose(n9, 4.8 * np.pi * (7 + 1j)))
tau9 = np.angle(n9)
print(f"  tau = {np.degrees(tau9):.3f} deg = {tau9:.5f} rad = atan(1/7); lag time tau/w = {tau9 / w9 * 1e9:.6f} ns")
print(f"  2 tau = {np.degrees(2 * tau9):.3f} deg, tan(2 tau) = {np.tan(2 * tau9):.5f} = 7/24 = {7 / 24:.5f}")
u9, E9 = -Y, Z * 8 * np.exp(1j * np.radians(30))
H9 = np.cross(u9, E9) / n9
print(f"  u x E-hat = (-y) x z = {dname(np.cross(-Y, Z))}; H~(0) = {H9}; |H| = {np.linalg.norm(H9):.5f} A/m;"
      f" 1/(3 sqrt2 pi) = {1 / (3 * np.sqrt(2) * np.pi):.5f}")
print(f"  H phase (of the -x component's amplitude): {deg(-H9[0]):.2f} deg = 30 - 8.13")
g2_9 = g9 ** 2
y9 = g2_9 / (1j * w9 * mu0)
print(f"  gamma^2 = {g2_9}; gamma/eta = gamma^2/(j w mu0) = {rect(y9, 6)} = (14 + 48j)/(240 pi) = {rect((14 + 48j) / (240 * np.pi), 6)}")
s9, ep9 = y9.real, y9.imag / w9
print(f"  sigma = {s9:.6f} S/m = 7/(120 pi) = {7 / (120 * np.pi):.6f}; eps = {ep9:.4e} F/m = {ep9 / eps0c:.4f} eps0 (exact eps0: {ep9 / eps0:.3f})")
print(f"  sigma/(w eps) = {s9 / (w9 * ep9):.4f} = 7/24")
g9m = media(w9, mu0, s9, ep9, "22.9 medium")
check("22.9 medium reproduces gamma, eta", np.isclose(g9m[1], g9) and np.isclose(g9m[3], n9))
a_, b_, ne_, ta_ = general(w9, mu0, s9, ep9)
print(f"  general formulas: alpha {a_:.6f}, beta {b_:.6f}, |eta| {ne_:.4f}, tau {np.degrees(ta_):.4f} deg")
nL9 = np.sqrt(mu0 / ep9)
aid = s9 / 2 * nL9; bid = w9 * np.sqrt(mu0 * ep9)
print(f"  imperfect-dielectric shortcuts: alpha ~ (sigma/2) sqrt(mu/eps) = 7/(2 sqrt 12) = {aid:.4f} ({(aid - 1) * 100:+.1f} %),"
      f" beta ~ w sqrt(mu eps) = sqrt 48 = {bid:.4f} ({(bid / 7 - 1) * 100:+.1f} %), tau ~ sigma/(2 w eps) = 7/48 rad ="
      f" {np.degrees(7 / 48):.2f} deg; lossless eta = 120 pi/sqrt12 = {nL9:.2f} Ohm")
Ef = lambda r: E9 * np.exp(g9 * r[1]); Hf = lambda r: np.cross(-Y, Ef(r)) / n9
phasor_maxwell("22.9 -y wave", Ef, Hf, w9, mu0, s9, ep9, rpts(5, -1, 1), 1e-5)
time_maxwell("22.9 -y wave", Ef, Hf, w9, mu0, s9, ep9, rpts(5, -1, 1), 1e-5)
fE = lambda r, t: Z * 8 * np.exp(r[1]) * np.cos(6e8 * t + 7 * r[1] + np.radians(30))
fH = lambda r, t: -X * 0.0750 * np.exp(r[1]) * np.cos(6e8 * t + 7 * r[1] + np.radians(21.87))
formula_vs_phasor("22.9 E as given", fE, Ef, w9, rpts(4, -1, 1), 1e-12)
formula_vs_phasor("22.9 H = -x 75.0 e^y cos(6e8 t + 7y + 21.87 deg) mA/m", fH, Hf, w9, rpts(4, -1, 1), 1e-3)
brute, form = tavg_S(Ef, Hf, w9, [0, 0, 0])
print(f"  (not asked) <S>(y=0) = {brute} W/m^2, direction {dname(brute)}")

# =====================================================================================================
hdr("22.10 Two components in a magnetic medium: E~ = (6x - j8y) e^{(3 + j5)z} V/m, w = 3e8, mu = 4 mu0")
w10, mu10 = 3e8, 4 * mu0
g10 = 3 + 5j
print(f"  e^(+gamma z) with gamma = 3 + 5j: travel -z, decays toward -z; alpha = 3 Np/m, beta = 5 rad/m")
print(f"  lambda = 2pi/5 = {2 * np.pi / 5:.4f} m, delta = 1/3 = {1 / 3:.4f} m, v_p = {w10 / 5:.3e} m/s, |gamma| = sqrt34 = {np.sqrt(34):.4f},"
      f" angle {deg(g10):.2f} deg")
n10 = 1j * w10 * mu10 / g10
print(f"  w mu = 480 pi = {w10 * mu10:.3f}; eta = {rect(n10, 3)} = {pol(n10, 3)} Ohm; (240 pi/17)(5 + 3j) = {rect(240 * np.pi / 17 * (5 + 3j), 3)};"
      f" 240 pi/17 = {240 * np.pi / 17:.4f}; 480 pi/sqrt34 = {480 * np.pi / np.sqrt(34):.3f}")
check("22.10 eta", np.isclose(n10, 240 * np.pi / 17 * (5 + 3j)))
print(f"  tau = atan(3/5) = {np.degrees(np.arctan(3 / 5)):.3f} deg; cos tau = 5/sqrt34 = {5 / np.sqrt(34):.4f}")
E10 = np.array([6, -8j, 0])
H10 = np.cross(-Z, E10) / n10
print(f"  (-z) x x = {dname(np.cross(-Z, X))}, (-z) x y = {dname(np.cross(-Z, Y))}; (-z) x (6x - j8y) = {np.cross(-Z, E10)}")
print(f"  H~(0) = {H10}")
print(f"  H~x: |{abs(H10[0]) * 1e3:.3f}| mA/m, angle {deg(H10[0]):.2f} deg; H~y: |{abs(H10[1]) * 1e3:.3f}| mA/m, angle {deg(H10[1]):.2f} deg"
      f" (= 180 - {180 - deg(H10[1]):.2f})")
print(f"  8/|eta| = {8 / abs(n10) * 1e3:.3f} mA/m, 6/|eta| = {6 / abs(n10) * 1e3:.3f} mA/m")
y10 = g10 ** 2 / (1j * w10 * mu10)
s10, ep10 = y10.real, y10.imag / w10
print(f"  gamma^2 = {g10 ** 2}; gamma/eta = {rect(y10, 6)} = (30 + 16j)/(480 pi): sigma = {s10:.6f} = 1/(16 pi) = {1 / (16 * np.pi):.6f} S/m,"
      f" eps = {ep10:.4e} F/m = {ep10 / eps0c:.4f} eps0; sigma/(w eps) = {s10 / (w10 * ep10):.4f} = 15/8")
g10m = media(w10, mu10, s10, ep10, "22.10 medium")
check("22.10 medium reproduces gamma, eta", np.isclose(g10m[1], g10) and np.isclose(g10m[3], n10))
print(f"  lossless eta of this medium (mu_r = eps_r = 4): {np.sqrt(mu10 / ep10):.2f} Ohm (= 120 pi)")
Ef = lambda r: E10 * np.exp(g10 * r[2]); Hf = lambda r: np.cross(-Z, Ef(r)) / n10
phasor_maxwell("22.10 -z wave", Ef, Hf, w10, mu10, s10, ep10, rpts(5, -1, 0.5), 1e-5)
time_maxwell("22.10 -z wave", Ef, Hf, w10, mu10, s10, ep10, rpts(5, -1, 0.5), 1e-5)
fE = lambda r, t: np.exp(3 * r[2]) * (X * 6 * np.cos(3e8 * t + 5 * r[2]) + Y * 8 * np.sin(3e8 * t + 5 * r[2]))
fH = lambda r, t: np.exp(3 * r[2]) * (X * 0.03093 * np.cos(3e8 * t + 5 * r[2] - np.radians(120.96))
                                      - Y * 0.02320 * np.cos(3e8 * t + 5 * r[2] - np.radians(30.96)))
formula_vs_phasor("22.10 E = e^{3z}[x 6 cos(wt+5z) + y 8 sin(wt+5z)]", fE, Ef, w10, rpts(4, -1, 0.5), 1e-12)
formula_vs_phasor("22.10 H = e^{3z}[x 30.93 cos(.. - 120.96) - y 23.20 cos(.. - 30.96)] mA/m", fH, Hf, w10, rpts(4, -1, 0.5), 5e-4)
S10 = 0.5 * 100 / abs(n10) * np.cos(np.angle(n10))
print(f"  <S> = -z (36 + 64)/(2|eta|) cos tau e^(6z) = -z {S10:.5f} e^(6z) W/m^2; 25/(48 pi) = {25 / (48 * np.pi):.5f}")
print(f"  x part: {S10 * 0.36:.5f} (36 %), y part: {S10 * 0.64:.5f} (64 %)")
for zz in (0.0, -0.2):
    brute, form = tavg_S(Ef, Hf, w10, [0.1, -0.2, zz])
    print(f"  brute <S> at z = {zz}: {brute} ({dname(brute)}); formula -{S10 * np.exp(6 * zz):.5f}")
    check(f"22.10 <S> at z = {zz}", np.isclose(brute[2], -S10 * np.exp(6 * zz), rtol=1e-6) and abs(brute[0]) + abs(brute[1]) < 1e-12)
for comp, E1 in (("x only", np.array([6, 0, 0])), ("y only", np.array([0, -8j, 0]))):
    Efc = (lambda E1: (lambda r: E1 * np.exp(g10 * r[2])))(E1)
    Hfc = (lambda Efc: (lambda r: np.cross(-Z, Efc(r)) / n10))(Efc)
    brute, _ = tavg_S(Efc, Hfc, w10, [0, 0, 0])
    print(f"  <S> of the {comp} part alone at z = 0: {brute[2]:.5f} W/m^2")
mu_wrong = 1j * w10 * mu0 / g10
print(f"  (mu0 trap) with mu0: |eta| = {abs(mu_wrong):.4f} Ohm (4x small), sigma = {2 * 15 / (w10 * mu0):.5f}, eps = {16 / (w10 ** 2 * mu0) / eps0c:.2f} eps0 (4x large), ratio still {30 / 16:.4f}")

# =====================================================================================================
hdr("22.11 Current sheet on x = 0, Js = z 4 cos(wt) A/m, in the 22.6 medium (gamma = 2 + 3j, eta = (120pi/13)(3 + 2j))")
J0 = 4.0
Js_ph = Z * J0
n11, g11 = n6, g6
# boundary-condition derivation: E~ = z A e^{-gamma|x|} both sides; H~ = u x E~/eta
# jump: x x (H1 - H2) = Js -> solve for A
H1u = np.cross(X, Z) / n11      # per unit A, x > 0
H2u = np.cross(-X, Z) / n11     # per unit A, x < 0
jump_per_A = np.cross(X, H1u - H2u)
A = J0 / jump_per_A[2]
print(f"  x x (H1 - H2) per unit A = {jump_per_A} -> A = Js/({jump_per_A[2]:.6f}) = {rect(A, 4)} = -2 eta: {rect(-2 * n11, 4)}")
check("22.11 A = -eta J0/2", np.isclose(A, -n11 * J0 / 2))
Ef = lambda r: Z * A * np.exp(-g11 * abs(r[0]))
Hf = lambda r: (np.cross(X, Ef(r)) if r[0] > 0 else np.cross(-X, Ef(r))) / n11
print(f"  H~(0+) = {Hf(np.array([1e-12, 0, 0]))}, H~(0-) = {Hf(np.array([-1e-12, 0, 0]))}  (= +/-y 2: 1/2 Js x n = "
      f"{0.5 * np.cross(Js_ph, X)} / {0.5 * np.cross(Js_ph, -X)})")
print(f"  |E| at the sheet = 2|eta| = {2 * abs(n11):.2f} V/m; angle of E~(0)/(-z) = {deg(-A):.2f} deg (E leads -Js by tau)")
print(f"  lead time tau/w = {np.angle(n11) / w6 * 1e9:.3f} ns")
for side, xs_ in (("x>0", rpts(4, 0.05, 1.5)), ("x<0", [np.array([-p[0], p[1], p[2]]) for p in rpts(4, 0.05, 1.5)])):
    phasor_maxwell(f"22.11 {side}", Ef, Hf, w6, mu0, s6, e6, xs_, 1e-5)
    time_maxwell(f"22.11 {side}", Ef, Hf, w6, mu0, s6, e6, xs_, 1e-5)
ok = True
for t in rng.uniform(0, 2 * np.pi / w6, 6):
    E1 = np.real(Ef(np.array([1e-9, 0, 0])) * np.exp(1j * w6 * t)); E2 = np.real(Ef(np.array([-1e-9, 0, 0])) * np.exp(1j * w6 * t))
    H1 = np.real(Hf(np.array([1e-9, 0, 0])) * np.exp(1j * w6 * t)); H2 = np.real(Hf(np.array([-1e-9, 0, 0])) * np.exp(1j * w6 * t))
    ok &= np.allclose(E1[1:], E2[1:], atol=1e-6) and np.allclose(np.cross(X, H1 - H2), Z * J0 * np.cos(w6 * t), atol=1e-7)
check("22.11 at the sheet (time domain): E_t continuous, x x (H1 - H2) = Js(t)", ok)
fE = lambda r, t: -Z * 209.1 * np.exp(-2 * abs(r[0])) * np.cos(w6 * t - 3 * abs(r[0]) + np.radians(33.69))
fH = lambda r, t: np.sign(r[0]) * Y * 2 * np.exp(-2 * abs(r[0])) * np.cos(w6 * t - 3 * abs(r[0]))
both = rpts(3, 0.05, 1.5) + [np.array([-p[0], p[1], p[2]]) for p in rpts(3, 0.05, 1.5)]
formula_vs_phasor("22.11 E = -z 209.1 e^{-2|x|} cos(wt - 3|x| + 33.69 deg)", fE, Ef, w6, both, 5e-4)
formula_vs_phasor("22.11 H = +/- y 2 e^{-2|x|} cos(wt - 3|x|)", fH, Hf, w6, both, 1e-12)
reta = n11.real
print(f"  Re eta = 360 pi/13 = {reta:.3f} Ohm ({360 * np.pi / 13:.3f}); 2 Re eta = {2 * reta:.2f} W/m^2 per (A/m)^2 ... <S>(0+) = {2 * reta:.2f} W/m^2")
for xx in (1e-9, -1e-9, 0.5, -0.5, 1.151):
    brute, form = tavg_S(Ef, Hf, w6, [xx, 0, 0])
    print(f"  brute <S> at x = {xx}: {brute} ({dname(brute)}), formula {np.sign(xx) * 2 * reta * np.exp(-4 * abs(xx)):.3f} x-hat")
    check(f"22.11 <S> at x = {xx}", np.isclose(brute[0], np.sign(xx) * 2 * reta * np.exp(-4 * abs(xx)), rtol=1e-6))
# power the sheet gives up: <-Js . E> at x = 0, brute force
ts = np.arange(4000) / 4000 * 2 * np.pi / w6
P = np.mean([-np.dot(Z * J0 * np.cos(w6 * t), np.real(Ef(np.array([0.0, 0, 0])) * np.exp(1j * w6 * t))) for t in ts])
print(f"  <-Js . E> brute = {P:.3f} W/m^2; 1/4 J0^2 Re eta = {0.25 * J0 ** 2 * reta:.3f}; two outgoing fluxes = {4 * reta:.3f}")
check("22.11 power balance at the sheet", np.isclose(P, 0.25 * J0 ** 2 * reta, rtol=1e-6) and np.isclose(P, 2 * 2 * reta))
print(f"  absorbed within delta = 0.5 m (one side): {(1 - np.exp(-2)) * 100:.1f} % = {2 * reta * (1 - np.exp(-2)):.1f} W/m^2;"
      f" 99 % within ln(100)/4 = {np.log(100) / 4:.3f} m")
etaL = np.sqrt(mu0 / e6)
print(f"  lossless (sigma = 0): eta = {etaL:.2f} Ohm, |E| at sheet = 2 eta = {2 * etaL:.1f} V/m, power 1/4 J0^2 eta = {0.25 * J0 ** 2 * etaL:.1f} W/m^2")
print(f"  ratio of supplied powers lossy/lossless = {reta / etaL:.3f}; |E| ratio = {abs(n11) / etaL:.3f}")

# =====================================================================================================
hdr("22.12 Three probes identify a medium (w = 3e8 rad/s)")
w12 = 3e8
# design (hidden): mu = 5 mu0, eps = 3 eps0, sigma = 1/(75 pi)  ->  gamma = 1 + 4j, eta = 600 pi (4 + j)/17
s12d, e12d, mu12d = 1 / (75 * np.pi), 3 * eps0c, 5 * mu0
_, g12d, _, n12d = media(w12, mu12d, s12d, e12d, "22.12 design medium")
check("22.12 design gamma = 1 + 4j", np.isclose(g12d, 1 + 4j))
check("22.12 design eta = 600 pi (4 + j)/17", np.isclose(n12d, 600 * np.pi * (4 + 1j) / 17))
# records the page gives: E_z(0,t) = 10 cos wt; E_z(-0.25,t) = 12.84 cos(wt + 57.30 deg); H_x(0,t) = 21.87 cos(wt - 14.04 deg) mA/m
EzB_amp = 10 * np.exp(g12d.real * 0.25); EzB_ph = np.degrees(g12d.imag * 0.25)
Hx_amp = 10 / abs(n12d); Hx_ph = -deg(n12d)
print(f"  exact records: E_z(B) amplitude {EzB_amp:.4f} V/m, phase +{EzB_ph:.4f} deg; H_x(A) amplitude {Hx_amp * 1e3:.4f} mA/m, phase {Hx_ph:.4f} deg")
Ef = lambda r: Z * 10 * np.exp(-g12d * r[1]); Hf = lambda r: np.cross(Y, Ef(r)) / n12d
print(f"  direction of H for travel +y with E along z: y x z = {dname(np.cross(Y, Z))} (so H_x = +E_z/eta)")
check("22.12 records consistent: E(B) phasor", np.isclose(Ef(np.array([0, -0.25, 0]))[2], EzB_amp * np.exp(1j * np.radians(EzB_ph))))
check("22.12 records consistent: H(A) phasor", np.isclose(Hf(np.zeros(3))[0], Hx_amp * np.exp(1j * np.radians(Hx_ph))))
phasor_maxwell("22.12 design wave", Ef, Hf, w12, mu12d, s12d, e12d, rpts(4, -1, 1), 1e-5)
time_maxwell("22.12 design wave", Ef, Hf, w12, mu12d, s12d, e12d, rpts(4, -1, 1), 1e-5)
# decode from the rounded records
d = 0.25
a12 = np.log(12.84 / 10) / d
b12 = np.radians(57.30) / d
g12 = a12 + 1j * b12
n12 = 10 / (21.87e-3 * np.exp(-1j * np.radians(14.04)))
print(f"  from the rounded records: alpha = ln(1.284)/0.25 = {a12:.5f} Np/m, beta = (57.30 deg = {np.radians(57.30):.5f} rad)/0.25 = {b12:.5f} rad/m")
print(f"  gamma = {rect(g12, 5)}; |gamma| = {abs(g12):.5f} (sqrt17 = {np.sqrt(17):.5f}); tau check atan(alpha/beta) = {np.degrees(np.arctan(a12 / b12)):.3f} deg vs 14.04")
print(f"  eta = 10 V/m / (21.87 mA/m e^-j14.04) = {pol(n12, 3)} = {rect(n12, 3)} Ohm; design {pol(n12d, 3)} = {rect(n12d, 3)}")
print(f"  angle(gamma) + angle(eta) = {deg(g12):.3f} + {deg(n12):.3f} = {deg(g12) + deg(n12):.3f} deg (90 for real mu);"
      f" |gamma||eta| = {abs(g12) * abs(n12):.1f} Ohm/m (exact 600 pi = {600 * np.pi:.1f})")
print(f"  mu = |gamma||eta|/w = {abs(g12) * abs(n12) / w12:.4e} H/m = {abs(g12) * abs(n12) / w12 / mu0:.4f} mu0")
print(f"  gamma/eta = (|gamma|/|eta|) e^(j(angle diff)) = {abs(g12) / abs(n12):.4e} e^(j{deg(g12) - deg(n12):.3f} deg)")
mu12 = g12 * n12 / (1j * w12)
y12 = g12 / n12
print(f"  mu = gamma eta/(j w) = {rect(mu12, 10)} H/m -> mu/mu0 = {rect(mu12 / mu0, 4)}")
print(f"  gamma/eta = {rect(y12, 7)} S/m -> sigma = {y12.real * 1e3:.4f} mS/m (design 1/(75 pi) = {1e3 / (75 * np.pi):.4f}), "
      f"w eps = {y12.imag:.6f} -> eps = {y12.imag / w12:.4e} F/m = {y12.imag / w12 / eps0c:.4f} eps0")
print(f"  exact design: mu = 5 mu0 = {5 * mu0:.4e} H/m; gamma/eta = (8 + 15j)/(600 pi) = {rect((8 + 15j) / (600 * np.pi), 7)}")
print(f"  sigma/(w eps) = {y12.real / y12.imag:.4f} (design 8/15 = {8 / 15:.4f}); tau = {np.degrees(0.5 * np.arctan(8 / 15)):.3f} deg")
check("22.12 decoded mu_r ~ 5, eps_r ~ 3, sigma ~ 4.24 mS/m (from rounded records, 0.5 %)",
      abs(mu12.real / mu0 - 5) < 0.025 and abs(y12.imag / w12 / eps0c - 3) < 0.015 and abs(y12.real - s12d) < 0.005 * s12d
      and abs(mu12.imag) < 0.01 * abs(mu12))
print(f"  with mu0 assumed (no H probe): sigma' = 2 alpha beta/(w mu0) = 8/(120 pi) = {8 / (120 * np.pi) * 1e3:.2f} mS/m (x5),"
      f" eps' = 15/(w^2 mu0) = {15 / (w12 ** 2 * mu0) / eps0c:.2f} eps0 (x5), ratio {8 / 15:.4f} unchanged; eta' = j w mu0/gamma -> |eta'| = {w12 * mu0 / np.sqrt(17):.2f} Ohm")
SA = 0.5 * 10 * 21.87e-3 * np.cos(np.radians(14.04))
SAd = 0.5 * 100 * (n12d.real / abs(n12d) ** 2)
print(f"  <S>(A) = 1/2 (10)(21.87e-3) cos 14.04 = {SA:.5f} W/m^2 (+y); exact 1/(3 pi) = {1 / (3 * np.pi):.5f}")
print(f"  <S>(B) = <S>(A) e^(2 alpha 0.25) = {SAd * np.exp(0.5):.5f} W/m^2; absorbed between = {SAd * (np.exp(0.5) - 1):.5f} W/m^2")
for yy in (0.0, -0.25):
    brute, form = tavg_S(Ef, Hf, w12, [0, yy, 0])
    print(f"  brute <S> at y = {yy}: {brute} ({dname(brute)})")
    check(f"22.12 <S> at y = {yy}", np.isclose(brute[1], SAd * np.exp(-2 * g12d.real * yy), rtol=1e-6))
fEB = lambda r, t: Z * 12.84 * np.cos(w12 * t + np.radians(57.30))
formula_vs_phasor("22.12 record at B", fEB, Ef, w12, [np.array([0, -0.25, 0])], 1e-4)
fHA = lambda r, t: X * 21.87e-3 * np.cos(w12 * t - np.radians(14.04))
formula_vs_phasor("22.12 H record at A", fHA, Hf, w12, [np.zeros(3)], 1e-3)

# =====================================================================================================
hdr("summary")
print(f"  {sum(ALL)} of {len(ALL)} checks OK" + ("" if all(ALL) else "  <-- FAILURES"))
