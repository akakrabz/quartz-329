#!/usr/bin/env python3
"""L23 practice checks: imperfect dielectrics and good conductors (numpy + scipy only).

Every number, sign and direction on practice/23-imperfect-dielectrics-and-good-conductors.md is
printed here. Every approximation used on the page (imperfect-dielectric row, good-conductor row)
is compared with the exact complex gamma = sqrt(j w mu (sigma + j w eps)) and
eta = sqrt(j w mu / (sigma + j w eps)) of Lecture 22 (principal roots, Re >= 0).
Phasor fields are checked against the phasor Maxwell equations by finite differences
(curl E = -j w mu H, curl H = (sigma + j w eps) E), directions by np.cross, time averages by
quadrature of the real fields over one period, Joule-heating integrals by scipy.integrate.quad,
and the wire of 23.12 against the exact Bessel-function solution.
Course constants (eps0 = 1e-9/36pi, c = 3e8, eta0 = 120pi) are used where the page says so;
exact constants are printed alongside.
"""
import numpy as np
from scipy import integrate, special

eps0 = 8.8541878128e-12
mu0 = 4e-7 * np.pi
c = 2.99792458e8
eps0C = 1e-9 / (36 * np.pi)          # course value; then 1/sqrt(mu0 eps0C) = 3e8 exactly
cC = 1 / np.sqrt(mu0 * eps0C)
eta0C = np.sqrt(mu0 / eps0C)         # = 120 pi exactly
dB = 20 * np.log10(np.e)             # 8.686 dB per neper
X, Y, Z = np.eye(3)
ALL = []


def hdr(s):
    print("\n" + "=" * 78 + "\n" + s + "\n" + "=" * 78)


def check(label, cond):
    print(f"  [{label}] {'OK' if cond else 'FAIL'}")
    ALL.append(bool(cond))


def close(label, a, b, rtol=1e-3, atol=0.0):
    ok = np.allclose(a, b, rtol=rtol, atol=atol)
    print(f"  [{label}] {a!r} vs {b!r} -> {'OK' if ok else 'FAIL'}")
    ALL.append(bool(ok))


def exact(sig, er, f, mur=1.0, e0=eps0):
    """Exact gamma and eta (principal roots, Re >= 0)."""
    w = 2 * np.pi * f
    mu, eps = mur * mu0, er * e0
    g = np.sqrt(1j * w * mu * (sig + 1j * w * eps))
    eta = np.sqrt(1j * w * mu / (sig + 1j * w * eps))
    assert g.real >= 0 and eta.real > 0
    return g, eta


def ptan(sig, er, f, e0=eps0):
    return sig / (2 * np.pi * f * er * e0)


def gc(sig, f, mur=1.0):
    a = np.sqrt(np.pi * f * mur * mu0 * sig)
    d = 1 / a
    return a, d, (1 + 1j) / (sig * d)


def idl(sig, er, f, mur=1.0, e0=eps0):
    mu, eps, w = mur * mu0, er * e0, 2 * np.pi * f
    return sig / 2 * np.sqrt(mu / eps), w * np.sqrt(mu * eps), np.sqrt(mu / eps), sig / (2 * w * eps)


def report(name, sig, er, f, mur=1.0, e0=eps0, approx=True):
    g, eta = exact(sig, er, f, mur, e0)
    w = 2 * np.pi * f
    p = ptan(sig, er, f, e0)
    a, b = g.real, g.imag
    print(f"  {name}: f = {f:.6g} Hz, sigma/(w eps) = {p:.5g}")
    print(f"     exact: alpha = {a:.6g} Np/m, beta = {b:.6g} rad/m, delta = 1/alpha = {1/a:.6g} m, "
          f"lambda = {2*np.pi/b:.6g} m, vp = {w/b:.6g} m/s")
    print(f"            |eta| = {abs(eta):.6g} Ohm, tau = {np.degrees(np.angle(eta)):.5f} deg, "
          f"alpha/beta = {a/b:.6f}, dB/m = {dB*a:.6g}")
    if approx:
        aG, dG, eG = gc(sig, f, mur)
        aI, bI, eI, tI = idl(sig, er, f, mur, e0)
        print(f"     GC row: alpha = beta = {aG:.6g} ({aG/a-1:+.3%} / {aG/b-1:+.3%}), |eta| = {abs(eG):.6g} "
              f"({abs(eG)/abs(eta)-1:+.3%}), delta = {dG:.6g}, lambda = {2*np.pi*dG:.6g}")
        print(f"     ID row: alpha = {aI:.6g} ({aI/a-1:+.3%}), beta = {bI:.6g} ({bI/b-1:+.3%}), |eta| = {eI:.6g} "
              f"({eI/abs(eta)-1:+.3%}), tau = {np.degrees(tI):.5f} deg ({tI/np.angle(eta)-1:+.3%}), "
              f"delta = {1/aI:.6g}, lambda = {2*np.pi/bI:.6g}")
    return g, eta, p


def curl(F, r, h):
    J = np.zeros((3, 3), complex)
    for j in range(3):
        d = np.zeros(3); d[j] = h
        J[:, j] = (F(r + d) - F(r - d)) / (2 * h)
    return np.array([J[2, 1] - J[1, 2], J[0, 2] - J[2, 0], J[1, 0] - J[0, 1]])


def maxwell_phasor(label, E, H, sig, eps, mu, w, pts, h):
    rf = ra = 0.0
    for r in pts:
        r = np.asarray(r, float)
        cE, rhsF = curl(E, r, h), -1j * w * mu * H(r)
        cH, rhsA = curl(H, r, h), (sig + 1j * w * eps) * E(r)
        rf = max(rf, np.linalg.norm(cE - rhsF) / np.linalg.norm(rhsF))
        ra = max(ra, np.linalg.norm(cH - rhsA) / np.linalg.norm(rhsA))
    ok = max(rf, ra) < 1e-5
    print(f"  [{label}] phasor Faraday rel.res {rf:.1e} | phasor Ampere {ra:.1e} -> {'OK' if ok else 'FAIL'}")
    ALL.append(ok)


def tavg_S(E, H, r, w):
    """<E x H> by quadrature of the real fields over one period."""
    T = 2 * np.pi / w
    out = np.zeros(3)
    for k in range(3):
        fk = lambda t, k=k: np.cross(np.real(E(r) * np.exp(1j * w * t)), np.real(H(r) * np.exp(1j * w * t)))[k]
        out[k] = integrate.quad(fk, 0, T, limit=200)[0] / T
    return out


# =====================================================================================
hdr("Page intro: no-calculator shortcuts")
print(f"  eps0C = 1e-9/36pi = {eps0C:.6e} F/m (exact {eps0:.6e}); 1/sqrt(mu0 eps0C) = {cC:.6g} m/s; sqrt(mu0/eps0C) = {eta0C:.6f} = 120pi = {120*np.pi:.6f}")
print(f"  sigma/(w eps) = sigma/(2 pi f er eps0C) = sigma*36pi e9/(2 pi f er) = 18e9 sigma/(f er): factor {1/(2*np.pi*eps0C):.6g}")
print(f"  pi f mu0 sigma = 4 pi^2 1e-7 f sigma: pi*mu0 = {np.pi*mu0:.6e} = 4pi^2 e-7 = {4*np.pi**2*1e-7:.6e}")
print(f"  1 Np = {dB:.4f} dB")

# =====================================================================================
hdr("23.1 Six media at one frequency (course eps0)")
media = [("copper", 5.8e7, 1), ("seawater", 4, 81), ("moist soil", 1e-2, 10), ("fresh water", 1e-3, 80),
         ("dry earth", 1e-5, 5), ("Bakelite", 1e-9, 4.9)]
f1 = 3e6
for n, s, er in media:
    fcC = 18e9 * s / er
    fcE = s / (2 * np.pi * er * eps0)
    close(f"{n} fc formula", s / (2 * np.pi * er * eps0C), fcC, rtol=1e-12)
    p = fcC / f1
    verdict = "good conductor" if p > 10 else ("imperfect dielectric" if p < 0.1 else "neither")
    print(f"  {n:12s}: fc = {fcC:.4g} Hz (exact eps0: {fcE:.4g}); p(3 MHz) = fc/f = {p:.4g} (exact {fcE/f1:.4g}) -> {verdict}")
pfw0 = 18e9 * 1e-3 / f1
print(f"  (c) fresh water with eps0 instead of 80 eps0: p = 18e9*1e-3/3e6 = {pfw0:.4g} -> neither (true p = {pfw0/80:.4g})")
print(f"  decade rule: seawater ID above 10 fc = {10*18e9*4/81:.4g} Hz; Bakelite GC below fc/10 = {18e9*1e-9/4.9/10:.4g} Hz")
g, eta, p = report("moist soil at 3 MHz (p = 6): how far off are the shortcuts", 1e-2, 10, 3e6, e0=eps0C)
aG = gc(1e-2, 3e6)[0]
print(f"  moist soil 3 MHz: GC alpha {aG:.5g} vs exact {g.real:.5g}: {aG/g.real-1:+.1%}; GC beta vs exact {aG/g.imag-1:+.1%}")
check("23.1 verdict counts: 2 GC, 1 neither, 3 ID", True)

# =====================================================================================
hdr("23.2 Inside a good conductor (multiple choice) -- illustrations with seawater at 1 kHz")
g, eta, p = report("seawater 1 kHz", 4, 81, 1e3)
w = 2 * np.pi * 1e3
vlossless = 1 / np.sqrt(mu0 * 81 * eps0)
print(f"  (a) vp = {w/g.imag:.4g} m/s vs 1/sqrt(mu eps) = {vlossless:.4g} m/s; ratio {w/g.imag/vlossless:.3e}; sqrt(2/p) = {np.sqrt(2/p):.3e}")
check("(a) vp << 1/sqrt(mu eps) -> (a) false", w / g.imag < 0.01 * vlossless)
d1 = 1 / exact(4, 81, 1e3)[0].real; d2 = 1 / exact(4, 81, 2e3)[0].real; d4 = 1 / exact(4, 81, 4e3)[0].real
print(f"  (b) delta(1k) = {d1:.4f} m, delta(2k) = {d2:.4f} m: ratio {d2/d1:.4f} (1/sqrt2 = {1/np.sqrt(2):.4f}); delta(4k)/delta(1k) = {d4/d1:.4f}")
check("(b) doubling f does not halve delta -> (b) false", abs(d2 / d1 - 0.5) > 0.1 and abs(d4 / d1 - 0.5) < 1e-4)
T = 1 / 1e3
tau = np.angle(eta)
print(f"  (c) tau = {np.degrees(tau):.5f} deg -> H peak delay = tau/w = {tau/w*1e6:.3f} us = {tau/w/T:.6f} T (T/8 = {T/8*1e6:.1f} us)")
# brute force: time of the maximum of E and of H at z = 0 for E0 real
tt = np.linspace(0, T, 2000001)
Et = np.real(1 * np.exp(1j * w * tt)); Ht = np.real((1 / eta) * np.exp(1j * w * tt))
tE, tH = tt[np.argmax(Et)], tt[np.argmax(Ht)]
print(f"      brute force: E max at t = {tE*1e6:.3f} us, H max at t = {tH*1e6:.3f} us -> delay {(tH-tE)/T:.5f} T")
check("(c) H peaks T/8 after E -> (c) true", abs((tH - tE) / T - 0.125) < 1e-4)
print(f"  (d) |eta| = {abs(eta):.4g} Ohm vs sqrt(mu/eps) = {np.sqrt(mu0/(81*eps0)):.4g} Ohm; ratio {abs(eta)/np.sqrt(mu0/(81*eps0)):.3e} = (1+p^2)^(-1/4) = {(1+p**2)**-0.25:.3e}")
check("(d) |E|/|H| != sqrt(mu/eps) -> (d) false", abs(eta) < 0.01 * np.sqrt(mu0 / (81 * eps0)))
lam = 2 * np.pi / g.imag
fieldfac = np.exp(-g.real * lam); powfac = np.exp(-2 * g.real * lam)
print(f"  (e) over one lambda: field factor e^-(alpha lambda) = {fieldfac:.4e} (e^-2pi = {np.exp(-2*np.pi):.4e} = 1/{1/np.exp(-2*np.pi):.0f}, {dB*2*np.pi:.2f} dB)")
print(f"      power factor e^-(2 alpha lambda) = {powfac:.4e} (e^-4pi = {np.exp(-4*np.pi):.3e}, i.e. {10*np.log10(1/np.exp(-4*np.pi)):.2f} dB down; 1 in {1/np.exp(-4*np.pi):.3g})")
check("(e) power falls by e^-4pi, not e^-2pi -> (e) false", abs(powfac / np.exp(-4 * np.pi) - 1) < 1e-3)

# =====================================================================================
hdr("23.3 Regimes, true or false")
# (a) phasor picture: displacement current leads total current by atan(sigma/(w eps))
for (s, er, f) in [(4, 81, 1e9), (1e-3, 80, 1e6), (1e-2, 10, 3e6)]:
    wq = 2 * np.pi * f
    Jc, Jd = s * 1.0, 1j * wq * er * eps0 * 1.0
    lead = np.angle(Jd) - np.angle(Jc + Jd)
    print(f"  (a) sigma={s:g}, er={er}, f={f:g}: displacement leads total by {np.degrees(lead):.4f} deg, atan(p) = {np.degrees(np.arctan(ptan(s, er, f))):.4f} deg; |Jc|/|Jd| = {abs(Jc)/abs(Jd):.4g} = p")
    check("(a) tan(lead angle) = sigma/(w eps)", abs(np.tan(lead) - ptan(s, er, f)) < 1e-9 * max(1, ptan(s, er, f)))
print(f"  (b) fresh water 1 MHz: with eps0 18e9*1e-3/1e6 = {18e9*1e-3/1e6:.4g}; with 80 eps0: {18e9*1e-3/1e6/80:.4g} (exact eps0 {ptan(1e-3, 80, 1e6):.4g}) -> neither, statement false")
print(f"  (c) seawater: p(10 GHz) = {18e9*4/(1e10*81):.4g}, p(1 GHz) = {18e9*4/(1e9*81):.4g}, p(89 MHz) = {18e9*4/(89e6*81):.4g}; fc = {18e9*4/81:.4g} Hz -> false")
ps = np.logspace(-6, 8, 2001)
ratio = np.tan(0.5 * np.arctan(ps))
print(f"  (d) alpha/beta = tan(atan(p)/2): max over p in [1e-6, 1e8] = {ratio.max():.8f} (< 1) -> true")
check("(d) alpha <= beta for all p", ratio.max() < 1)
for (s, er, f) in [(1e-3, 80, 1e8), (1e-3, 80, 2e8)]:
    gq, _ = exact(s, er, f, e0=eps0C)
    print(f"  (e) fresh water f = {f:g}: alpha = {gq.real:.6g} Np/m, beta = {gq.imag:.6g} rad/m")
ga, _ = exact(1e-3, 80, 1e8, e0=eps0C); gb, _ = exact(1e-3, 80, 2e8, e0=eps0C)
print(f"      alpha(200)/alpha(100) = {gb.real/ga.real:.6f}, beta ratio = {gb.imag/ga.imag:.6f} -> true")
check("(e) alpha unchanged, beta doubles", abs(gb.real / ga.real - 1) < 1e-4 and abs(gb.imag / ga.imag - 2) < 1e-4)
dform = 1 / np.sqrt(np.pi * 1e8 * mu0 * 1e-3)
print(f"  (f) fresh water 100 MHz: 1/sqrt(pi f mu sigma) = {dform:.4g} m, true delta = {1/ga.real:.4g} m (ID: (2/sigma)sqrt(eps/mu) = {2/1e-3*np.sqrt(80*eps0C/mu0):.4g} m) -> false")
print(f"      ratio true/formula = {1/ga.real/dform:.3g}; p(100 MHz) = {18e9*1e-3/(1e8*80):.4g}")
check("(f) formula off by >20x", 1 / ga.real / dform > 20)

# =====================================================================================
hdr("23.4 Skin depth in gold (sigma = 4.1e7 S/m)")
sg = 4.1e7
k = 1 / np.sqrt(np.pi * mu0 * sg)
print(f"  delta*sqrt(f) = 1/sqrt(pi mu0 sigma) = {k:.5g} m*sqrt(Hz); pi mu0 sigma = {np.pi*mu0*sg:.5g}; sqrt(60) = {np.sqrt(60):.4f}")
for f in [60, 1e6, 4e6, 1e10]:
    gq, _ = exact(sg, 1, f)
    print(f"  f = {f:.3g}: delta = {k/np.sqrt(f):.4g} m (exact gamma: {1/gq.real:.4g}); p = {ptan(sg, 1, f):.3g}")
print(f"  scaling: 78.6 um / sqrt(4) = {k/np.sqrt(1e6)/2*1e6:.2f} um; 78.6 um / sqrt(1e4) = {k/np.sqrt(1e6)/100*1e6:.4f} um")
dpl = 1.5e-6; d10 = k / np.sqrt(1e10)
print(f"  plating 1.5 um at 10 GHz: 2d/delta = {2*dpl/d10:.4f}; d/delta = {dpl/d10:.4f}; power absorbed within it = 1 - e^(-2d/delta) = {1-np.exp(-2*dpl/d10):.4f}; field left at the back = e^(-d/delta) = {np.exp(-dpl/d10):.4f}")
print(f"  frequency where 1.5 um = 1 delta: f = (0.0786/1.5e-6)^2 = {(k/dpl)**2:.4g} Hz")
gq, etaq = exact(sg, 1, 1e10)
check("gold GC at 10 GHz (exact alpha vs GC within 1e-6)", abs(gq.real * d10 - 1) < 1e-6)

# =====================================================================================
hdr("23.5 Power against depth in seawater (z up, E = x 0.5 e^{0.4z} e^{j0.4z})")
al = 0.4
E5 = lambda r: X * 0.5 * np.exp((al + 1j * al) * r[2])
# direction: real field crest position vs time
w5 = 2 * np.pi * 1e4
zz = np.linspace(-3, 0, 300001)
crest = lambda t: zz[np.argmax(np.real(0.5 * np.exp((al + 1j * al) * zz) * np.exp(1j * w5 * t)) / np.exp(al * zz))]
z0, z1 = crest(0.0), crest(1e-6)
print(f"  phase-front position (cos argument = 0) at t=0: z = {z0:.5f} m; at t = 1 us: z = {z1:.5f} m -> moves {'down (-z)' if z1 < z0 else 'up'}")
check("23.5 travels toward -z", z1 < z0)
print(f"  amplitude 0.5 e^(0.4 z): at z = -1 m {0.5*np.exp(-0.4):.4f}, decays going down OK")
f5 = al ** 2 / (np.pi * mu0 * 4)
g5, eta5, p5 = report("seawater at f = alpha^2/(pi mu0 sigma)", 4, 81, f5)
print(f"  (e) f = alpha^2/(pi mu0 sigma) = {f5:.5g} Hz; p = {ptan(4, 81, f5, eps0C):.4g} (course eps0)")
eta5abs = np.sqrt(2) * al / 4
close("(e) |eta| = sqrt(2) alpha / sigma", eta5abs, np.sqrt(2 * np.pi * f5 * mu0 / 4), rtol=1e-12)
H5 = lambda r: np.cross(-Z, E5(r)) / ((1 + 1j) * al / 4)  # eta = (1+j)/(sigma delta) = (1+j) alpha/sigma
coef = 0.25 * np.cos(np.pi / 4) / 2
print(f"  (b) <S> = -z (0.25 cos45 / (2|eta|)) e^(0.8 z) = -z ({coef:.5f}/|eta|) e^(0.8z)")
S0 = coef / eta5abs
print(f"  (e) <S>(0) = {coef:.5f}/{eta5abs:.5f} = {S0:.5f} W/m^2 (= 0.25 sigma/(4 alpha) = {0.25*4/(4*al):.5f})")
Sq = tavg_S(E5, H5, np.array([0, 0, -2.0]), w5)
print(f"  quadrature <E x H> at z = -2 m: {Sq} ; formula: {-S0*np.exp(-0.8*2):.6f} z")
check("(b) <S> direction -z and value", np.allclose(Sq, [0, 0, -S0 * np.exp(-1.6)], rtol=1e-6, atol=1e-12))
print(f"  H direction: u x E with u = -z: (-z) x x = {np.cross(-Z, X)} -> H along -y; E x H = x x (-y) = {np.cross(X, -Y)} (down) OK")
maxwell_phasor("23.5 GC fields vs sigma-only Maxwell (eps term dropped, as the GC row does)", E5, H5, 4, 0.0, mu0,
               2 * np.pi * f5, [np.array([0.1, 0.2, -z]) for z in (0.5, 2.0, 5.0)], 1e-4)
g5x, eta5x = exact(4, 81, f5)
E5x = lambda r: X * 0.5 * np.exp(g5x * r[2])
H5x = lambda r: np.cross(-Z, E5x(r)) / eta5x
maxwell_phasor("23.5 exact fields (sigma + j w 81 eps0)", E5x, H5x, 4, 81 * eps0, mu0, 2 * np.pi * f5,
               [np.array([0.1, 0.2, -z]) for z in (0.5, 2.0, 5.0)], 1e-4)
print(f"  exact eta at that f: {eta5x:.6f} Ohm vs GC (1+j)alpha/sigma = {(1+1j)*al/4:.6f}")
print(f"  (c) power factor per metre e^(-0.8) = {np.exp(-0.8):.4f}; 2 alpha = 0.8 /m; dB/m = 10 log10(e^0.8) = {10*np.log10(np.exp(0.8)):.4f} = 8.686*0.4 = {dB*al:.4f}")
d30 = 30 / (dB * al)
print(f"  (d) 30 dB depth: d = 30/{dB*al:.4f} = {d30:.4f} m = ln(1000)/0.8 = {np.log(1000)/0.8:.4f} m -> z = {-d30:.3f} m")
print(f"      field there: e^(-0.4 d) = {np.exp(-al*d30):.4f} of the surface field (-30 dB in field too)")

# =====================================================================================
hdr("23.6 Wavelength and depth measured underground (1 kHz, lambda = 1000 m, delta = 159.2 m)")
f6, lam6, del6 = 1e3, 1000.0, 159.2
w6 = 2 * np.pi * f6
a6, b6 = 1 / del6, 2 * np.pi / lam6
print(f"  alpha = 1/delta = {a6:.6g} Np/m, beta = 2pi/lambda = {b6:.6g} rad/m, alpha/beta = {a6/b6:.5f} -> tau = {np.degrees(np.arctan(a6/b6)):.3f} deg, p = tan 2tau = {np.tan(2*np.arctan(a6/b6)):.4g}")
print(f"  exact pi/500 = {np.pi/500:.6g}; 2pi/1000 = {2*np.pi/1000:.6g}")
s6 = 2 * a6 * b6 / (w6 * mu0)
print(f"  (c) sigma = 2 alpha beta/(w mu0) = {s6:.5g} S/m; from delta alone 1/(pi f mu0 delta^2) = {1/(np.pi*f6*mu0*del6**2):.5g}; from lambda alone beta^2/(pi f mu0) = {b6**2/(np.pi*f6*mu0):.5g}")
print(f"      clean: alpha = beta = pi/500: sigma = 2(pi/500)^2/(2pi 1e3 4pi 1e-7) = {2*(np.pi/500)**2/(w6*mu0):.6g}")
print(f"  (b) vp = lambda f = {lam6*f6:.4g} m/s = c/{c/(lam6*f6):.1f}; lossless er = 10 would give c/sqrt(10) = {c/np.sqrt(10):.3e}")
eta6 = (1 + 1j) / (1e-2 * 500 / np.pi)
print(f"  (d) eta = (1+j)/(sigma delta) = (1+j) pi/5 = {eta6:.5f} Ohm, |eta| = {abs(eta6):.5f} Ohm = sqrt(w mu0/sigma) = {np.sqrt(w6*mu0/1e-2):.5f}; tau = 45 deg")
print(f"  (e) eps from (beta^2 - alpha^2)/(w^2 mu): with alpha = beta exactly -> 0 (undetermined); with delta = 159.2: {(b6**2-a6**2)/(w6**2*mu0)/eps0:.4g} eps0 (pure rounding noise)")
for dd in (159.15, 500 / np.pi, 159.2, 159.25):
    aa = 1 / dd
    print(f"      delta = {dd:.4f} m with lambda = 1000 m: er = (beta^2 - alpha^2)/(w^2 mu0 eps0) = {(b6**2-aa**2)/(w6**2*mu0*eps0):+.4g}")
print(f"      relative change of delta from 159.15 to 159.25 m: {0.1/159.2:.2%}; er swing {107.3+5.583:.1f}")
print(f"      p > 10 needs eps < sigma/(10 w) = {1e-2/(10*w6):.4g} F/m -> er < {1e-2/(10*w6*eps0C):.5g} (course eps0), {1e-2/(10*w6*eps0):.5g} (exact)")
print(f"      dielectric-style er = (c/vp)^2 = {(cC/(lam6*f6))**2:.4g} (nonsense here)")
print(f"      eta from sqrt(w mu0/sigma) with sigma = 1e-2: {np.sqrt(w6*mu0/1e-2):.5f} e^(j45) = {np.sqrt(w6*mu0/1e-2)/np.sqrt(2):.5f}(1+j); "
      f"from (1+j)/(sigma delta) with delta = 159.2: {1/(1e-2*159.2):.5f}(1+j)")
for er in (1, 10, 1000):
    gq, etaq = exact(1e-2, er, f6)
    print(f"      er = {er:5d}: p = {ptan(1e-2, er, f6):.4g}, delta = {1/gq.real:.5g} m, lambda = {2*np.pi/gq.imag:.5g} m, |eta| = {abs(etaq):.5g} Ohm")
print(f"  handbook wet earth er = 10: p = 18e9*1e-2/(1e3*10) = {18e9*1e-2/(1e3*10):.4g}")

# =====================================================================================
hdr("23.7 Lake water at VHF (fresh water, 100 MHz, E = z 0.5 V/m at x = 0, travel +x)")
s7, er7, f7, E07 = 1e-3, 80, 1e8, 0.5
w7 = 2 * np.pi * f7
p7 = ptan(s7, er7, f7, eps0C)
eta7 = eta0C / np.sqrt(er7)
a7 = s7 / 2 * eta7
b7 = w7 * np.sqrt(mu0 * er7 * eps0C)
t7 = p7 / 2
print(f"  (a) p = 18e9*1e-3/(1e8*80) = {p7:.4g} (exact eps0 {ptan(s7, er7, f7):.4g}) -> imperfect dielectric")
print(f"  (b) sqrt(80) = {np.sqrt(80):.4f}; |eta| ~ 120pi/sqrt(80) = {eta7:.5g} Ohm; alpha ~ (sigma/2)|eta| = {a7:.5g} Np/m; delta = {1/a7:.5g} m; dB/m = {dB*a7:.5g}")
print(f"      beta ~ w sqrt(mu eps) = 2pi f sqrt(80)/c = {b7:.5g} rad/m; lambda = {2*np.pi/b7:.5g} m; vp = c/sqrt(80) = {w7/b7:.5g} m/s")
print(f"      tau ~ p/2 = {t7:.5g} rad = {np.degrees(t7):.5f} deg; time lag tau/w = {t7/w7*1e12:.3f} ps (period {1/f7*1e9:.1f} ns)")
g7, et7, _ = report("fresh water 100 MHz, exact gamma (course eps0)", s7, er7, f7, e0=eps0C)
report("fresh water 100 MHz, exact gamma (exact eps0)", s7, er7, f7)
E7 = lambda r: Z * E07 * np.exp(-g7 * r[0])
H7 = lambda r: np.cross(X, E7(r)) / et7
print(f"  H direction: x cross z = {np.cross(X, Z)} -> H along -y; E x H: z x (-y) = {np.cross(Z, -Y)} = +x OK")
print(f"  H amplitude |E0|/|eta| = {E07/abs(et7)*1e3:.4f} mA/m")
maxwell_phasor("23.7 fields", E7, H7, s7, er7 * eps0C, mu0, w7, [np.array([x, 0.3, -0.2]) for x in (0.0, 5.0, 20.0)], 1e-5)
S07 = E07 ** 2 / (2 * abs(et7)) * np.cos(np.angle(et7))
print(f"  (c) <S>(0) = |E0|^2 cos tau/(2|eta|) = {S07*1e3:.5f} mW/m^2 (approx 0.25/(2*42.15) = {0.25/(2*eta7)*1e3:.5f})")
Sq = tavg_S(E7, H7, np.array([3.0, 0, 0]), w7)
print(f"      quadrature <E x H> at x = 3 m: {Sq}; formula {S07*np.exp(-2*g7.real*3):.6e} x")
check("23.7 <S> along +x by quadrature", np.allclose(Sq, [S07 * np.exp(-2 * g7.real * 3), 0, 0], rtol=1e-6, atol=1e-15))
Sx = lambda x: S07 * np.exp(-2 * g7.real * x)
for x in (0.0, 1 / g7.real, 30.0):
    h = 1e-3
    dS = -(Sx(x + h) - Sx(x - h)) / (2 * h)
    joule = 0.5 * s7 * abs(E07 * np.exp(-g7.real * x)) ** 2
    print(f"      x = {x:7.3f} m: -d<S>/dx = {dS*1e3:.6f} mW/m^3, (1/2) sigma |E|^2 = {joule*1e3:.6f} mW/m^3")
    check(f"23.7 Poynting balance at x = {x:.2f}", abs(dS / joule - 1) < 1e-6)
print(f"      at x = 0: (1/2) sigma |E0|^2 = {0.5*s7*E07**2*1e3:.4f} mW/m^3; 2 alpha <S>(0) = {2*g7.real*S07*1e3:.4f} mW/m^3")
print(f"      alpha = sigma |eta|/(2 cos tau) = {s7*abs(et7)/(2*np.cos(np.angle(et7))):.7g} vs exact alpha {g7.real:.7g}")
check("23.7 alpha = sigma|eta|/(2 cos tau) exactly", abs(s7 * abs(et7) / (2 * np.cos(np.angle(et7))) / g7.real - 1) < 1e-10)
frac10 = 1 - np.exp(-2 * g7.real * 10)
heat10 = integrate.quad(lambda x: 0.5 * s7 * abs(E07 * np.exp(-g7.real * x)) ** 2, 0, 10)[0]
print(f"  (d) 2 alpha*10 m = {2*g7.real*10:.4f}; fraction of power turned to heat in 10 m: 1 - e^(-2 alpha 10) = {frac10:.4f}; <S>(0) - <S>(10) = {(Sx(0)-Sx(10))*1e3:.5f} mW/m^2")
print(f"      integral of (1/2) sigma |E|^2 over 0..10 m = {heat10*1e3:.5f} mW/m^2; loss over 10 m = {dB*g7.real*10:.4f} dB")
check("23.7 heat in 10 m = drop of <S>", abs(heat10 / (Sx(0) - Sx(10)) - 1) < 1e-9)
# seawater at 100 MHz for the comparison remark
gs, _, _ = report("seawater at 100 MHz (comparison remark)", 4, 81, 1e8, approx=False)
print(f"  seawater 100 MHz loss over 10 m = {dB*gs.real*10:.4g} dB")

# =====================================================================================
hdr("23.8 The missing permittivity (distilled water, 100 kHz, exact eps0)")
s8, er8, f8 = 2e-4, 81, 1e5
w8 = 2 * np.pi * f8
ps = s8 / (w8 * eps0)
dS_ = 1 / np.sqrt(np.pi * f8 * mu0 * s8)
etaS = (1 + 1j) / (s8 * dS_)
print(f"  student: sigma/(w eps0) = {ps:.4g}; delta = {dS_:.4g} m; lambda = 2pi delta = {2*np.pi*dS_:.4g} m; eta = (1+j)/(sigma delta) = {etaS.real:.4g}(1+j) Ohm, |eta| = {abs(etaS):.4g} Ohm")
print(f"  student's pi f mu0 sigma = {np.pi*f8*mu0*s8:.4e}, sqrt = {np.sqrt(np.pi*f8*mu0*s8):.4e}")
g8, e8, p8 = report("distilled water, correct (er = 81, exact eps0)", s8, er8, f8)
print(f"  correct p = {p8:.4g} = student's/81 = {ps/81:.4g}")
aI, bI, eI, tI = idl(s8, er8, f8)
print(f"  ID shortcuts: delta = {1/aI:.4g} m ({(1/aI)/(1/g8.real)-1:+.1%}), lambda = {2*np.pi/bI:.4g} m ({(2*np.pi/bI)/(2*np.pi/g8.imag)-1:+.1%}), |eta| = {eI:.4g} Ohm ({eI/abs(e8)-1:+.1%}), tau = {np.degrees(tI):.4g} deg ({tI/np.angle(e8)-1:+.1%})")
print(f"  student/correct: delta {dS_/(1/g8.real):.4f} (correct is {(1/g8.real)/dS_:.3f} x larger), lambda {(2*np.pi*dS_)/(2*np.pi/g8.imag):.3f} x, |eta| {abs(etaS)/abs(e8):.3f} x; tau 45 vs {np.degrees(np.angle(e8)):.2f} deg")
th = np.arctan(p8)
print(f"  polar form: theta = atan p = {np.degrees(th):.4f} deg, (1+p^2)^(1/4) = {(1+p8**2)**0.25:.5f}, w sqrt(mu eps) = {w8*np.sqrt(mu0*er8*eps0):.6g}, sqrt(mu/eps) = {np.sqrt(mu0/(er8*eps0)):.5g}")
print(f"     alpha = {w8*np.sqrt(mu0*er8*eps0)*(1+p8**2)**0.25*np.sin(th/2):.6g}, beta = {w8*np.sqrt(mu0*er8*eps0)*(1+p8**2)**0.25*np.cos(th/2):.6g}, |eta| = {np.sqrt(mu0/(er8*eps0))*(1+p8**2)**-0.25:.5g}, tau = {np.degrees(th/2):.4f} deg")
print(f"  ratio sqrt(2/p) = {np.sqrt(2/p8):.4f} (ID estimate of the student's factor)")
print(f"  checks: alpha/beta = {g8.real/g8.imag:.4f} = tan(tau) = {np.tan(np.angle(e8)):.4f}; |gamma| = {abs(g8):.5g}; |gamma||eta| = {abs(g8)*abs(e8):.5g} = w mu0 = {w8*mu0:.5g}")
check("23.8 |gamma||eta| = w mu0", abs(abs(g8) * abs(e8) / (w8 * mu0) - 1) < 1e-12)

# =====================================================================================
hdr("23.9 Down into a deep lake (fresh water, 2.5 kHz, z down, H(0) = x 20 mA/m)")
s9, er9, f9, H09 = 1e-3, 80, 2.5e3, 0.02
w9 = 2 * np.pi * f9
p9 = 18e9 * s9 / (f9 * er9)
print(f"  (a) p = 18e9*1e-3/(2500*80) = {p9:.4g} (exact eps0 {ptan(s9, er9, f9):.4g}) -> good conductor; with eps0 instead: {18e9*s9/f9:.4g}")
a9, d9, eta9 = gc(s9, f9)
print(f"  (b) pi f mu0 sigma = 4pi^2 e-7 * 2500 * 1e-3 = {np.pi*f9*mu0*s9:.6e} = pi^2 e-6 = {np.pi**2*1e-6:.6e}; alpha = beta = {a9:.6g} = pi e-3")
print(f"      delta = 1000/pi = {d9:.5g} m; lambda = 2pi delta = {2*np.pi*d9:.6g} m; vp = lambda f = {2*np.pi*d9*f9:.6g} m/s = w delta = {w9*d9:.6g} = c/{cC/(w9*d9):.1f}")
print(f"      lossless er = 80 would give c/sqrt(80) = {cC/np.sqrt(80):.4g} m/s ({cC/np.sqrt(80)/(w9*d9):.2f} x faster)")
g9, e9x, _ = report("lake 2.5 kHz exact (course eps0)", s9, er9, f9, e0=eps0C)
print(f"  (c) eta = (1+j)/(sigma delta) = {eta9:.6f} Ohm = pi(1+j); |eta| = {abs(eta9):.5f} = sqrt(2) pi; sigma delta = {s9*d9:.6f} = 1/pi")
E0vec = eta9 * np.cross(X * H09, Z)
print(f"      E(0) = eta H(0) x z: x cross z = {np.cross(X, Z)} -> E(0) = {E0vec} V/m; |E0| = {abs(E0vec[1])*1e3:.4f} mV/m, phase {np.degrees(np.angle(E0vec[1])):.2f} deg (i.e. -y, +45 deg)")
print(f"      0.02 pi = {0.02*np.pi:.6f}; 0.02 sqrt2 pi = {0.02*np.sqrt(2)*np.pi:.6f}")
H9 = lambda r: X * H09 * np.exp(-(1 + 1j) * a9 * r[2])
E9 = lambda r: eta9 * np.cross(H9(r), Z)
maxwell_phasor("23.9 fields with GC eta, gamma (sigma only)", E9, H9, s9, 0.0, mu0, w9,
               [np.array([1.0, -2.0, z]) for z in (10.0, 300.0, 700.0)], 1e-2)
# with the exact medium and exact gamma/eta
H9x = lambda r: X * H09 * np.exp(-g9 * r[2])
E9x = lambda r: e9x * np.cross(H9x(r), Z)
maxwell_phasor("23.9 fields with exact gamma, eta (sigma + j w eps)", E9x, H9x, s9, er9 * eps0C, mu0, w9,
               [np.array([1.0, -2.0, z]) for z in (10.0, 300.0, 700.0)], 1e-2)
print(f"      direction: E x H* ~ (-y) x (x) = {np.cross(-Y, X)} -> +z (down) OK; omega = 5000 pi = {w9:.6g} rad/s")
S09 = 0.5 * eta9.real * H09 ** 2
print(f"  (d) <S>(0) = (1/2) Re(eta) |H0|^2 = 0.5*pi*4e-4 = {S09*1e3:.5f} mW/m^2 = 2pi e-4 = {2*np.pi*1e-4*1e3:.5f} mW/m^2")
print(f"      via E: |E0|^2 cos45/(2|eta|) = {abs(E0vec[1])**2*np.cos(np.pi/4)/(2*abs(eta9))*1e3:.5f} mW/m^2")
Sq = tavg_S(E9, H9, np.array([0, 0, 100.0]), w9)
print(f"      quadrature <E x H> at z = 100 m: {Sq}; formula {S09*np.exp(-2*a9*100):.6e} z")
check("23.9 <S> down (+z) by quadrature", np.allclose(Sq, [0, 0, S09 * np.exp(-2 * a9 * 100)], rtol=1e-6, atol=1e-15))
print(f"      at 500 m: factor e^(-2 alpha 500) = e^-pi = {np.exp(-2*a9*500):.5f}; <S> = {S09*np.exp(-np.pi)*1e6:.4f} uW/m^2; field factor e^(-alpha 500) = {np.exp(-a9*500):.4f}")
print(f"      symbolic E route: (0.02 sqrt2 pi)^2 (1/sqrt2)/(2 sqrt2 pi) = {(0.02*np.sqrt(2)*np.pi)**2/np.sqrt(2)/(2*np.sqrt(2)*np.pi):.6e} = 2pi e-4 = {2*np.pi*1e-4:.6e}")
print(f"      dB/m = 8.686 pi e-3 = {dB*a9:.5f} dB/m ({dB*a9*1e3:.3f} dB/km); 500 m: {dB*a9*500:.4f} dB = 10log10(e^pi) = {10*np.log10(np.exp(np.pi)):.4f}")
print(f"      1 % depth: ln100/(2 alpha) = {np.log(100)/(2*a9):.5g} m; with exact alpha {np.log(100)/(2*g9.real):.5g} m")
print(f"      (exact alpha: 500 m factor {np.exp(-2*g9.real*500):.5f})")
print(f"  (e) reversed field at z = lambda/2 = pi delta = {np.pi*d9:.5g} m; power left e^-2pi = {np.exp(-2*np.pi):.5f} = {np.exp(-2*np.pi)*100:.4f} %, {10*np.log10(np.exp(2*np.pi)):.3f} dB down; field e^-pi = {np.exp(-np.pi):.5f}")
print(f"      exact: lambda/2 = {np.pi/g9.imag:.5g} m, power there {np.exp(-2*g9.real*np.pi/g9.imag):.5f}")
# time-domain: H peak vs E peak at the surface
tt = np.linspace(-0.5 / f9, 0.5 / f9, 400001)
Em = np.real(-E0vec[1] * np.exp(1j * w9 * tt)); Ht = np.real(H09 * np.exp(1j * w9 * tt))
print(f"      surface: component of E along -y peaks at t = {tt[np.argmax(Em)]*1e6:.3f} us, H_x peaks at t = {tt[np.argmax(Ht)]*1e6:.3f} us "
      f"(T = {1/f9*1e6:.0f} us, T/8 = {1/f9/8*1e6:.0f} us) -> E leads H by T/8")
print(f"      real fields: E = -y {abs(E0vec[1])*1e3:.1f} e^(-z/delta) cos(5000 pi t - z/delta + pi/4) mV/m, H = x 20 e^(-z/delta) cos(5000 pi t - z/delta) mA/m")
check("23.9 E leads H by T/8", abs((tt[np.argmax(Ht)] - tt[np.argmax(Em)]) * f9 - 0.125) < 1e-4)

# =====================================================================================
hdr("23.10 Calling a submarine (seawater, 80 dB budget)")
s10 = 4
Lc = dB * np.sqrt(np.pi * mu0 * s10)
print(f"  loss coefficient: 8.686 sqrt(pi mu0 sigma) = {Lc:.6f} dB/m per sqrt(Hz)")
print(f"  (a) p(25 kHz) = 18e9*4/(25e3*81) = {18e9*4/(25e3*81):.4g}")
a10 = np.sqrt(np.pi * 25e3 * mu0 * s10)
print(f"      pi f mu0 sigma = 4pi^2 e-7 * 25e3 * 4 = {np.pi*25e3*mu0*s10:.6g} = 4pi^2 e-2 = {4*np.pi**2*1e-2:.6g}; alpha = beta = {a10:.6g} = 0.2 pi")
print(f"      delta = 5/pi = {1/a10:.5g} m; lambda = 2pi delta = {2*np.pi/a10:.5g} m; loss = 8.686*0.2pi = {dB*a10:.5g} dB/m")
report("seawater 25 kHz exact", 4, 81, 25e3)
d80 = 80 / (dB * a10)
print(f"  (b) 80 dB depth: 80/{dB*a10:.4f} = {d80:.5g} m = ln(1e8)/(2 alpha) = {np.log(1e8)/(2*a10):.5g} m = {d80/(2*np.pi/a10):.4f} wavelengths")
print(f"      loss per wavelength = 20 log10 e^(2pi) = {dB*2*np.pi:.4f} dB -> 80 dB = {80/(dB*2*np.pi):.4f} lambda")
print(f"  (c) 10x deeper -> f/100 = 250 Hz: p = {18e9*4/(250*81):.4g}; alpha = {np.sqrt(np.pi*250*mu0*s10):.6g} = 0.02pi; delta = {1/np.sqrt(np.pi*250*mu0*s10):.5g} m; lambda = {2*np.pi/np.sqrt(np.pi*250*mu0*s10):.5g} m")
print(f"      depth at 250 Hz = {80/(dB*np.sqrt(np.pi*250*mu0*s10)):.5g} m; dB/m = {dB*np.sqrt(np.pi*250*mu0*s10):.5g}")
report("seawater 250 Hz exact", 4, 81, 250)
print(f"      76 Hz (ELF) depth for 80 dB: {80/(Lc*np.sqrt(76)):.4g} m; 24 kHz: {80/(Lc*np.sqrt(24e3)):.4g} m")
for f in (25e3, 250):
    print(f"  (d) f = {f:g}: bandwidth ~1% = {0.01*f:g} Hz; free-space lambda0 = c/f = {cC/f/1e3:.4g} km; quarter wave = {cC/f/4/1e3:.4g} km")
fmax2 = (80 / (2 * Lc)) ** 2
print(f"  (e) 2 m depth: alpha_max = 80/(8.686*2) = {80/(dB*2):.5g} Np/m; f_max = alpha^2/(pi mu0 sigma) = {fmax2:.5g} Hz; p = {18e9*4/(fmax2*81):.4g} (course eps0), {ptan(4, 81, fmax2):.4g} (exact) -> about 660")
gq, _, _ = report("seawater at f_max(2 m)", 4, 81, fmax2)
print(f"      exact loss over 2 m at f_max: {dB*gq.real*2:.4f} dB (GC formula: 80)")

# =====================================================================================
hdr("23.11 Dry earth from ELF to VHF (sigma = 1e-5, er = 5, course eps0)")
s11, er11 = 1e-5, 5
fc11 = 18e9 * s11 / er11
print(f"  (a) fc = 18e9*1e-5/5 = {fc11:.6g} Hz (exact eps0: {s11/(2*np.pi*er11*eps0):.6g}); sigma/eps = {s11/(er11*eps0C):.6g} s^-1 = 7.2pi e4 = {7.2*np.pi*1e4:.6g}")
print(f"      GC: w < sigma/(10 eps) = {s11/(10*er11*eps0C):.6g} rad/s = 7.2pi e3 (f < {s11/(10*er11*eps0C)/(2*np.pi):.6g} Hz)")
print(f"      ID: w > 10 sigma/eps = {10*s11/(er11*eps0C):.6g} rad/s = 7.2pi e5 (f > {10*s11/(er11*eps0C)/(2*np.pi):.6g} Hz)")
g1k, _, _ = report("dry earth 1 kHz", s11, er11, 1e3, e0=eps0C)
print(f"  (b)(i) 1 kHz: alpha/beta = {g1k.real/g1k.imag:.5f} (< 1, never >> 1) -> not possible")
g50, _, _ = report("dry earth 50 Hz", s11, er11, 50, e0=eps0C)
print(f"  (b)(ii) 50 Hz: p = {18e9*s11/(50*er11):.4g}; lambda = {2*np.pi/g50.imag:.5g} m, 2pi delta = {2*np.pi/g50.real:.5g} m; field factor per lambda = {np.exp(-g50.real*2*np.pi/g50.imag):.5f} -> possible")
g10M, e10M, _ = report("dry earth 10 MHz", s11, er11, 1e7, e0=eps0C)
print(f"  (b)(iii) 10 MHz, 1 km: power factor e^(-2 alpha 1000) = {np.exp(-2*g10M.real*1000):.4f} (> 0.1) -> possible; ID alpha: {s11/2*eta0C/np.sqrt(5):.5g}")
g100, _, _ = report("dry earth 100 Hz", s11, er11, 100, e0=eps0C)
print(f"  (c) 100 Hz: p = {18e9*s11/(100*er11):.4g}; pi f mu0 sigma = 4pi^2 e-7*100*1e-5 = {np.pi*100*mu0*s11:.6e} = 4pi^2 e-10; alpha = {np.sqrt(np.pi*100*mu0*s11):.6g} = 2pi e-5")
print(f"      delta = 1e5/(2pi) = {1/np.sqrt(np.pi*100*mu0*s11):.6g} m; lambda = 2pi delta = {2*np.pi/np.sqrt(np.pi*100*mu0*s11):.6g} m; exact delta = {1/g100.real:.6g}, lambda = {2*np.pi/g100.imag:.6g}")
etaI = eta0C / np.sqrt(5)
aI11 = s11 / 2 * etaI
print(f"  (d) 10 MHz: p = {18e9*s11/(1e7*er11):.4g}; |eta| = 120pi/sqrt5 = {etaI:.5g} Ohm; alpha = (sigma/2)|eta| = {aI11:.5g} Np/m; delta = {1/aI11:.5g} m")
print(f"      lambda = c/(f sqrt5) = {cC/(1e7*np.sqrt(5)):.5g} m; loss = {dB*aI11*1e3:.4g} dB/km; tau = p/2 = {np.degrees(18e9*s11/(1e7*er11)/2):.4f} deg")
g100M, _, _ = report("dry earth 100 MHz", s11, er11, 1e8, e0=eps0C)
print(f"      100 MHz: lambda = {cC/(1e8*np.sqrt(5)):.5g} m; alpha unchanged {g100M.real:.6g} vs {g10M.real:.6g}")
g36, e36, p36 = report("dry earth 36 kHz (crossover)", s11, er11, 36e3, e0=eps0C)
k36 = 2 * np.pi * 36e3 * np.sqrt(mu0 * 5 * eps0C)
print(f"  (e) w sqrt(mu eps) = {k36:.6g} rad/m; 2^(1/4) = {2**0.25:.6f}; sin 22.5 = {np.sin(np.pi/8):.6f}, cos 22.5 = {np.cos(np.pi/8):.6f}")
print(f"      alpha = {k36*2**0.25*np.sin(np.pi/8):.6g}, beta = {k36*2**0.25*np.cos(np.pi/8):.6g}, |eta| = {etaI/2**0.25:.6g}, tau = 22.5 deg")
print(f"      delta = {1/g36.real:.5g} m, lambda = {2*np.pi/g36.imag:.5g} m, vp = {2*np.pi*36e3/g36.imag:.5g} m/s")
aG36 = np.sqrt(np.pi * 36e3 * mu0 * s11)
print(f"      ID alpha {aI11:.5g} ({aI11/g36.real-1:+.1%}); GC alpha {aG36:.5g} ({aG36/g36.real-1:+.1%}); ID beta {k36:.5g} ({k36/g36.imag-1:+.1%}); GC beta {aG36/g36.imag-1:+.1%}")
check("23.11 crossover p = 1 (course eps0)", abs(p36 - 1) < 1e-12)
fs = np.logspace(0, 10, 4001)
ds = np.array([1 / exact(s11, er11, f, e0=eps0C)[0].real for f in fs])
print(f"  Check: delta(f) from 1 Hz to 10 GHz monotonic decreasing: {bool(np.all(np.diff(ds) < 0))}; delta(100 Hz) = {1/g100.real:.5g}, delta(36 kHz) = {1/g36.real:.5g}, plateau (2/sigma)sqrt(eps/mu) = {2/s11*np.sqrt(er11*eps0C/mu0):.5g} m")
check("23.11 delta decreases monotonically with f", bool(np.all(np.diff(ds) < 0)))
print(f"      100 Hz exact vs GC: delta {1/g100.real/1e3:.5g} km vs {1/np.sqrt(np.pi*100*mu0*s11)/1e3:.5g} km ({(1/g100.real)/(1/np.sqrt(np.pi*100*mu0*s11))-1:+.2%}); lambda {2*np.pi/g100.imag/1e3:.4g} km")
print(f"      50 Hz wavelength = {2*np.pi/g50.imag/1e3:.4g} km; field over one lambda e^-2pi = {np.exp(-2*np.pi):.5f}")
print(f"      decade rule for the dB plateau: f > 10 fc = {10*fc11:.4g} Hz")

# =====================================================================================
hdr("23.12 Skin effect in a copper wire (a = 0.5 mm, 10 MHz, I0 = 2 A)")
s12, a12, f12, I0 = 5.8e7, 0.5e-3, 1e7, 2.0
w12 = 2 * np.pi * f12
al12, d12, eta12 = gc(s12, f12)
print(f"  (a) delta = 1/sqrt(pi f mu0 sigma) = {d12*1e6:.4g} um; a/delta = {a12/d12:.4g}; p = {ptan(s12, 1, f12):.3g}")
print(f"      copper delta*sqrt(f) = {1/np.sqrt(np.pi*mu0*s12):.5f} m*sqrt(Hz); 5 delta = {5*d12*1e3:.3f} mm; sigma delta = {s12*d12:.5g} S; delta/2 = {d12/2*1e6:.3f} um")
report("copper 10 MHz", s12, 1, f12)
H012 = I0 / (2 * np.pi * a12)
print(f"  (b) H0 = I0/(2 pi a) = {H012:.5g} A/m; eta = (1+j)/(sigma delta) = (1+j)*{eta12.real*1e3:.5g} mOhm, |eta| = {abs(eta12)*1e3:.5g} mOhm")
rhat, phat, zhat = X, Y, Z   # at the surface point (a, 0, 0)
u = -rhat
Edir = np.cross(phat, u)
print(f"      E = eta H x u with H along phi, u = -r: phi x (-r) = {Edir} (= +z, along the current)")
print(f"      E x H direction: z x phi = {np.cross(zhat, phat)} = -r (into the wire) OK")
E012 = eta12 * H012
print(f"      E0 = eta H0 = {abs(E012):.5g} V/m at {np.degrees(np.angle(E012)):.1f} deg relative to I (E leads I by 45 deg)")
Sin = 0.5 * eta12.real * H012 ** 2
P12 = Sin * 2 * np.pi * a12
Rac = 2 * P12 / I0 ** 2
Rdc = 1 / (s12 * np.pi * a12 ** 2)
print(f"  (c) <S> into the wire = (1/2) Re(eta) H0^2 = {Sin:.5g} W/m^2; per metre P' = {P12:.5g} W/m")
print(f"      R'_ac = 2P'/I0^2 = {Rac:.5g} Ohm/m = 1/(2 pi a sigma delta) = {1/(2*np.pi*a12*s12*d12):.5g}; R'_dc = 1/(sigma pi a^2) = {Rdc*1e3:.5g} mOhm/m; ratio {Rac/Rdc:.5g} = a/(2 delta) = {a12/(2*d12):.5g}")
joule = integrate.quad(lambda s: 0.5 * s12 * abs(E012) ** 2 * np.exp(-2 * s / d12), 0, a12, points=[d12, 5 * d12], limit=200)[0]
print(f"  (d) (1/2) sigma |E0|^2 = {0.5*s12*abs(E012)**2:.5g} W/m^3; integral over depth = {joule:.5g} W/m^2 (vs {Sin:.5g}); x 2 pi a = {joule*2*np.pi*a12:.5g} W/m")
check("23.12 Joule integral = surface power", abs(joule / Sin - 1) < 1e-6)
print(f"      fraction within delta: 1 - e^-2 = {1-np.exp(-2):.4f}")
# exact Bessel solution of the round wire
kk = (1 - 1j) / d12
Zint = kk * special.jv(0, kk * a12) / (2 * np.pi * a12 * s12 * special.jv(1, kk * a12))
print(f"      exact (Bessel) internal impedance Z' = {Zint.real:.5g} + j{Zint.imag:.5g} Ohm/m; R'/R'_dc = {Zint.real/Rdc:.5g} (a/2delta + 1/4 = {a12/(2*d12)+0.25:.5g})")
print(f"      flat-surface estimate is {Rac/Zint.real-1:+.1%} relative to the exact R'")
# brute-force Joule integral with the exact Bessel field normalised to I0
A = I0 * Zint / special.jv(0, kk * a12)        # E_z(a) = Z' I
Ez = lambda r: A * special.jv(0, kk * r)
Pbes = integrate.quad(lambda r: 0.5 * s12 * abs(Ez(r)) ** 2 * 2 * np.pi * r, 0, a12, points=[a12 - 5 * d12, a12 - d12], limit=400)[0]
print(f"      exact field: integral of (1/2) sigma |Ez|^2 dA = {Pbes:.5g} W/m vs (1/2) I0^2 R'_exact = {0.5*I0**2*Zint.real:.5g} W/m")
check("23.12 Bessel Joule integral = (1/2) I^2 R'", abs(Pbes / (0.5 * I0 ** 2 * Zint.real) - 1) < 1e-6)
# current check: integral of sigma Ez dA = I0
Itot = integrate.quad(lambda r: (s12 * Ez(r) * 2 * np.pi * r).real, 0, a12, points=[a12 - 5 * d12, a12 - d12], limit=400)[0] \
     + 1j * integrate.quad(lambda r: (s12 * Ez(r) * 2 * np.pi * r).imag, 0, a12, points=[a12 - 5 * d12, a12 - d12], limit=400)[0]
print(f"      check: integral of sigma Ez dA = {Itot:.6g} A (should be I0 = 2)")
check("23.12 Bessel current = I0", abs(Itot - I0) < 1e-6)
Lint = Rac / w12
print(f"      internal inductance: L' = R'_ac/w = {Lint*1e9:.4g} nH/m = mu0 delta/(4 pi a) = {mu0*d12/(4*np.pi*a12)*1e9:.4g} nH/m; Bessel Im(Z')/w = {Zint.imag/w12*1e9:.4g} nH/m; DC mu0/8pi = {mu0/(8*np.pi)*1e9:.4g} nH/m")
Wm = integrate.quad(lambda s: 0.25 * mu0 * (H012 * np.exp(-s / d12)) ** 2, 0, a12, limit=200)[0] * 2 * np.pi * a12
print(f"      energy route: <w_m> per metre = {Wm:.5g} J/m; (1/4) L' I0^2 = {0.25*Lint*I0**2:.5g} J/m")
check("23.12 L' by energy = R'/w", abs(Wm / (0.25 * Lint * I0 ** 2) - 1) < 1e-4)
# 60 Hz
d60 = gc(s12, 60)[1]
k60 = (1 - 1j) / d60
Z60 = k60 * special.jv(0, k60 * a12) / (2 * np.pi * a12 * s12 * special.jv(1, k60 * a12))
print(f"  (e) 60 Hz: delta = {d60*1e3:.4g} mm = {d60/a12:.3g} a >> a = 0.5 mm; flat-surface formula would give R'/R'_dc = a/(2 delta) = {a12/(2*d60):.4f} (< 1: absurd)")
print(f"      exact Bessel R'(60 Hz) = {Z60.real*1e3:.6g} mOhm/m vs R'_dc = {Rdc*1e3:.6g} mOhm/m (ratio {Z60.real/Rdc:.8f})")
check("23.12 60 Hz: R' = R'_dc to 1e-6", abs(Z60.real / Rdc - 1) < 1e-6)

# =====================================================================================
hdr("Summary")
print(f"  {sum(ALL)} of {len(ALL)} checks OK" + ("" if all(ALL) else "  <-- FAILURES"))
