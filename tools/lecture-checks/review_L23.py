#!/usr/bin/env python3
"""Independent review script for the Lecture 23 page set (ECE 329 study site, build 8).

Re-derives every equation and recomputes every number on
  content-src/3-maxwell-and-waves/23-imperfect-dielectrics-and-good-conductors.md
  content-src/concepts/loss-tangent.md, concepts/skin-depth.md,
  concepts/conductivity-and-susceptibility-models.md (the "At high frequency, in waves" section),
  content-src/problems/a-radio-wave-into-moist-ground.md,
and the figure annotations of figs_l23.py, with numpy only.  Written without reading the
writer's verify_L23.py.  Prints PASS/FAIL per item and a summary.

Conventions: exact constants are CODATA (eps0 = 8.8541878128e-12 F/m, mu0 = 4 pi 1e-7 H/m);
the course's calculator-free constants are eps0 ~ 1e-9/(36 pi), eta0 ~ 120 pi.  A stated number
"agrees" when the computed value rounds to it at the precision it is printed with.
Section letters:
  A handbook values        B crossover and classification     C exact gamma, eta and the limits
  D Example 1 and Maxwell  E energy balance (Poynting)        F good conductor, Examples 2-3
  G seawater and submarines H metals                          I inverse example (200 MHz)
  J worked problem          K concept pages                    L figures
  M exam-key carry-over     N notation scan                    Z findings fixed in review
"""
import re
import numpy as np

PI = np.pi
MU0 = 4e-7 * PI
EPS0 = 8.8541878128e-12
C0 = 1 / np.sqrt(MU0 * EPS0)
ETA0 = np.sqrt(MU0 / EPS0)
EPS0C = 1e-9 / (36 * PI)           # course value
ETA0C = 120 * PI
NP2DB = 20 * np.log10(np.e)        # 8.6859 dB per neper

ROOT = "/home/claude/work/content-src/"
PAGE = ROOT + "3-maxwell-and-waves/23-imperfect-dielectrics-and-good-conductors.md"
L22 = ROOT + "3-maxwell-and-waves/22-phasor-maxwell-equations-and-damped-waves.md"
CLT = ROOT + "concepts/loss-tangent.md"
CSD = ROOT + "concepts/skin-depth.md"
CCS = ROOT + "concepts/conductivity-and-susceptibility-models.md"
PROB = ROOT + "problems/a-radio-wave-into-moist-ground.md"
FIGMOD = "/home/claude/work/figs_l23.py"

NPASS = NFAIL = 0
SEC = ""


def sec(s):
    global SEC
    SEC = s
    print(f"\n=== {s} ===")


def report(ok, name, detail=""):
    global NPASS, NFAIL
    if ok:
        NPASS += 1
    else:
        NFAIL += 1
    print(f"{'PASS' if ok else 'FAIL'} [{SEC[0]}] {name}" + (f"  ({detail})" if detail else ""))


def claim(name, cond, detail=""):
    report(bool(cond), name, detail)


def close(name, x, y, rtol=1e-9, atol=0.0):
    ok = np.allclose(x, y, rtol=rtol, atol=atol)
    report(ok, name, f"{np.asarray(x).ravel()[0]:.6g} vs {np.asarray(y).ravel()[0]:.6g}")


def agree(name, x, stated, scale=1.0, sf=None):
    """x (in the units of `stated` after dividing by scale) rounds to the printed string `stated`
    (at its last printed decimal, or at `sf` significant figures for numbers such as '4,240' or '950')."""
    s = stated.replace(",", "")
    m = re.fullmatch(r"([+-]?\d*\.?\d+)(?:e([+-]?\d+))?", s)
    v = float(s)
    mant = m.group(1)
    dec = len(mant.split(".")[1]) if "." in mant else 0
    exp = int(m.group(2)) if m.group(2) else 0
    half = 0.5 * 10.0 ** (exp - dec)
    xv = x / scale
    if sf is not None:
        half = 0.5 * 10.0 ** (np.floor(np.log10(abs(v))) - sf + 1)
    ok = abs(xv - v) <= half * (1 + 1e-9) + 1e-15
    report(ok, f"{name} = {stated}" + (f" ({sf} s.f.)" if sf else ""), f"computed {xv:.6g}")


def exact(f, sig, er, mur=1.0, eps0=EPS0):
    w = 2 * PI * f
    mu, eps = mur * MU0, er * eps0
    g = np.sqrt(1j * w * mu * (sig + 1j * w * eps))
    eta = np.sqrt(1j * w * mu / (sig + 1j * w * eps))
    if np.ndim(g) == 0:
        if g.real < 0:
            g = -g
        if eta.real < 0:
            eta = -eta
    return dict(a=g.real, b=g.imag, eta=eta, aeta=abs(eta), tau=np.angle(eta), p=sig / (w * eps), g=g, w=w,
                mu=mu, eps=eps, sig=sig)


def gc(f, sig, mur=1.0):
    """good-conductor shortcut: delta, alpha=beta, eta"""
    d = 1 / np.sqrt(PI * f * mur * MU0 * sig)
    return dict(d=d, a=1 / d, b=1 / d, eta=(1 + 1j) / (sig * d), aeta=np.sqrt(2 * PI * f * mur * MU0 / sig))


def fc(sig, er, eps0=EPS0):
    return sig / (2 * PI * er * eps0)


def tavg(fun, w, n=4096):
    """time average over one period by the rectangle rule (exact for trig polynomials)"""
    t = np.arange(n) * (2 * PI / w) / n
    return np.mean(fun(t), axis=-1)


rng = np.random.default_rng(23)

# ======================================================================================== A
sec("A  Handbook material values (stated here) against the page's values")
print("Handbook values used for comparison:")
print("  copper: IACS 100 % = 1/(1.7241e-8 ohm m) = 5.800e7 S/m; pure annealed Cu at 20 C 5.96e7 S/m (CRC rho = 1.678e-8)")
print("  aluminium: pure Al at 20 C rho = 2.65e-8 ohm m -> 3.77e7 S/m (CRC); EC grade (61 % IACS) 3.54e7; Rao Table 5.1: 3.5e7")
print("  seawater: 4.29 S/m at S = 35, 15 C (PSS-78 reference C(35,15,0) = 42.914 mS/cm); 3-6 S/m over 0-30 C;")
print("            static eps_r about 70-81 (pure water 80.1 at 20 C; salt lowers it; ITU-R P.368 uses 70 for sea water)")
print("  fresh water: 1e-4 .. 1e-2 S/m (ITU-R P.368 'fresh water' 3e-3 S/m, eps_r 80); eps_r 80.1 at 20 C")
print("  loam / moist soil: ITU-R P.527-6 sec. 4.1 'normally on the order of 1e-2 S/m', 'as low as 1e-4 S/m' dried;")
print("            eps_r of wet soils 10-30 (Rao 'wet earth' 10; ITU-R P.368 'wet ground' 30)")
print("  dry earth: Rao 1e-5 S/m, eps_r 5; ITU-R P.368 'very dry ground' 1e-4 S/m, eps_r 3")
print("  Bakelite (phenolic): volume resistivity 1e9..1e12 ohm m -> 1e-12..1e-9 S/m; eps_r 4.4-7 (Rao 4.9)")
print("  mica (muscovite): volume resistivity 1e11..1e15 ohm m; eps_r 5.4-8.7 (Rao 6)")
print("  copper Drude collision rate nu = N e^2/(m sigma) with N = 8.47e28 m^-3")
HB = {  # name: (page value, low, high) of the handbook range
    "copper sigma [S/m]": (5.8e7, 5.80e7 * 0.999, 5.96e7),
    "aluminium sigma [S/m]": (3.5e7, 3.4e7, 3.77e7),
    "seawater sigma [S/m]": (4.0, 3.0, 6.0),
    "seawater eps_r (notes 81)": (81, 70, 81),
    "fresh water sigma [S/m]": (1e-3, 1e-4, 1e-2),
    "fresh water eps_r": (80, 78, 88),
    "moist soil (loam) sigma [S/m]": (1e-2, 1e-3, 3e-2),
    "moist soil eps_r (Rao wet earth)": (10, 10, 30),
    "dry earth sigma [S/m]": (1e-5, 1e-5, 1e-3),
    "dry earth eps_r": (5, 3, 7),
    "Bakelite sigma [S/m]": (1e-9, 1e-12, 1e-9),
    "Bakelite eps_r": (4.9, 4.4, 7.0),
    "mica sigma [S/m]": (1e-11, 1e-15, 1e-11),
    "mica eps_r": (6, 5.4, 8.7),
}
for k, (v, lo, hi) in HB.items():
    claim(f"{k}: page {v:g} within handbook range [{lo:g}, {hi:g}]", lo <= v <= hi)
claim("copper 5.8e7 S/m is the IACS value 1/1.7241e-8 to 0.01 %", abs(1 / 1.7241e-8 / 5.8e7 - 1) < 1e-4)
claim("aluminium 3.5e7 is 7 % below pure Al (3.77e7): skin depth 3.8 % larger than pure-Al value (noted, not an error)",
      abs(np.sqrt(3.77e7 / 3.5e7) - 1.038) < 0.002)
nu_cu = 8.47e28 * (1.602176634e-19) ** 2 / (9.1093837e-31 * 5.8e7)
agree("copper Drude nu [1e13 s^-1] ('about 4e13')", nu_cu, "4", scale=1e13)
close("eta0 = 376.73 ohm", ETA0, 376.730, rtol=1e-5)

# ======================================================================================== B
sec("B  Crossover frequencies, classification, the media table")
TABLE = [  # name, sigma, eps_r, stated fc, scale, stated 'GC below', stated 'ID above'
    ("copper", 5.8e7, 1, "1.0", 1e18, None, None),
    ("seawater", 4, 81, "0.89", 1e9, ("89", 1e6), ("8.9", 1e9)),
    ("moist soil", 1e-2, 10, "18", 1e6, ("1.8", 1e6), ("180", 1e6)),
    ("notes Ex. 1 medium", 1e-3, 4, "4.5", 1e6, ("450", 1e3), ("45", 1e6)),
    ("fresh water", 1e-3, 80, "225", 1e3, ("22", 1e3), ("2.2", 1e6)),
    ("dry earth", 1e-5, 5, "36", 1e3, ("3.6", 1e3), ("360", 1e3)),
    ("Bakelite", 1e-9, 4.9, "3.7", 1, ("0.37", 1), ("37", 1)),
    ("mica", 1e-11, 6, "0.03", 1, None, ("0.3", 1)),
]
for name, s, er, st, sc, gcb, ida in TABLE:
    F = fc(s, er)
    agree(f"f_c {name}", F, st, scale=sc)
    if gcb:
        agree(f"  {name} good conductor below f_c/10", F / 10, gcb[0], scale=gcb[1], sf=2)
    if ida:
        agree(f"  {name} imperfect dielectric above 10 f_c", 10 * F, ida[0], scale=ida[1], sf=2)
    close(f"  {name}: sigma/(w eps) = 1 at f_c", exact(F, s, er)["p"], 1.0)
claim("copper 'good conductor below' = every radio and microwave frequency (f_c/10 = 1e17 Hz > 300 GHz)", fc(5.8e7, 1) / 10 > 3e11)
claim("mica: f_c/10 = 3 mHz, no practical good-conductor band (page '-')", fc(1e-11, 6) / 10 < 0.01)
agree("Rao Table 5.3 f_q dry earth [1e4 Hz]", fc(1e-5, 5), "3.6", scale=1e4)
agree("Rao Table 5.3 f_q seawater with eps_r = 80 [1e9 Hz]", fc(4, 80), "0.9", scale=1e9)
# seawater relaxation time and periods
taur = 81 * EPS0 / 4
agree("seawater tau_r = eps/sigma [ns]", taur, "0.18", scale=1e-9)
close("f_c = 1/(2 pi tau_r)", fc(4, 81), 1 / (2 * PI * taur))
claim("1 kHz period (1 ms) >> tau_r; 10 GHz period 0.1 ns < tau_r", 1e-3 / taur > 1e6 and 1e-10 < taur)
# leaky capacitor: G/(wC) = sigma/(w eps) for any geometry factor K (C = eps K, G = sigma K)
K, s_, e_, w_ = 0.37, 2e-3, 3 * EPS0, 2 * PI * 1e5
close("leaky capacitor G/(wC) = sigma/(w eps), G = (sigma/eps) C", (s_ * K) / (w_ * e_ * K), s_ / (w_ * e_))
# seawater at four frequencies
for f, st, sc in ((1e3, "8.9", 1e5), (1e6, "888", 1), (1e9, "0.89", 1), (1e10, "0.089", 1)):
    agree(f"seawater sigma/(w eps) at {f:g} Hz", exact(f, 4, 81)["p"], st, scale=sc)
claim("seawater regimes: GC at 1 kHz and 1 MHz (>10), between at 1 GHz, ID at 10 GHz (<0.1)",
      exact(1e3, 4, 81)["p"] > 10 and exact(1e6, 4, 81)["p"] > 10 and 0.1 < exact(1e9, 4, 81)["p"] < 10
      and exact(1e10, 4, 81)["p"] < 0.1)
# quick calculator-free formula
for s, er, f in ((4, 81, 1e3), (1e-2, 10, 1e5), (1e-3, 1, 100), (1e-3, 4, 1e9)):
    close(f"18e9 sigma/(f eps_r) = sigma/(w eps) with eps0 = 1e-9/36pi (sigma={s:g}, f={f:g})",
          18e9 * s / (f * er), exact(f, s, er, eps0=EPS0C)["p"], rtol=1e-12)
agree("quick value at 1 kHz: 18e9*4/(1e3*81)", 18e9 * 4 / (1e3 * 81), "8.9", scale=1e5)
close("trap: eps0 instead of 81 eps0 makes the ratio 81x too large", exact(1e6, 4, 1)["p"] / exact(1e6, 4, 81)["p"], 81)
agree("trap: dropping 2 pi changes the ratio by", 2 * PI, "6.3")
claim("trap: the table's dry earth is a good conductor at 100 Hz (sigma/w eps > 10)", exact(100, 1e-5, 5)["p"] > 10,
      f"{exact(100, 1e-5, 5)['p']:.0f}")
claim("abstract: seawater GC below about 90 MHz, dielectric above about 9 GHz",
      abs(fc(4, 81) / 10 / 90e6 - 1) < 0.02 and abs(10 * fc(4, 81) / 9e9 - 1) < 0.02)
fwfc = fc(1e-3, 1)
agree("On exams: S20 'dry earth' (1e-3 S/m, eps0) f_c [MHz]", fwfc, "18", scale=1e6)

# ======================================================================================== C
sec("C  Exact gamma and eta vs the polar 'one-knob' forms and the regime limits")
for k in range(200):
    f = 10 ** rng.uniform(0, 11)
    s = 10 ** rng.uniform(-12, 8)
    er = rng.uniform(1, 90)
    mur = rng.choice([1.0, 1.0, 3.0, 200.0])
    E = exact(f, s, er, mur)
    p = E["p"]
    th = np.arctan(p)
    sc_b = E["w"] * np.sqrt(E["mu"] * E["eps"])
    sc_e = np.sqrt(E["mu"] / E["eps"])
    ok = (np.isclose(E["a"], sc_b * (1 + p * p) ** 0.25 * np.sin(th / 2), rtol=1e-8, atol=1e-300)
          and np.isclose(E["b"], sc_b * (1 + p * p) ** 0.25 * np.cos(th / 2), rtol=1e-9)
          and np.isclose(E["aeta"], sc_e * (1 + p * p) ** -0.25, rtol=1e-9)
          and np.isclose(E["tau"], th / 2, rtol=1e-8, atol=1e-15)
          and np.isclose(E["a"] / E["b"], np.tan(E["tau"]), rtol=1e-7, atol=1e-300)
          and np.isclose(abs(E["g"]) * E["aeta"], E["w"] * E["mu"], rtol=1e-9)
          and np.isclose(E["g"] / E["eta"], s + 1j * E["w"] * E["eps"], rtol=1e-8)
          and np.isclose(E["g"], 1j * sc_b * np.sqrt(1 - 1j * p), rtol=1e-9)
          and np.isclose(E["eta"], sc_e / np.sqrt(1 - 1j * p), rtol=1e-9)
          and 0 <= E["tau"] <= PI / 4 * (1 + 1e-12) and E["a"] <= E["b"] * (1 + 1e-12))
    if not ok:
        print("  first failing medium:", f, s, er, mur, E["a"], E["b"], E["tau"])
        break
claim("200 random media (f 1 Hz-100 GHz, sigma 1e-12..1e8, eps_r 1-90, mu_r 1/3/200): alpha, beta, |eta|, tau = theta/2, "
      "alpha/beta = tan tau, |gamma||eta| = w mu, gamma/eta = sigma + j w eps, polar forms, 0 <= tau < 45 deg, alpha <= beta", ok)
# L22 general (Rao) closed forms agree with the polar forms
p = 2.7
th = np.arctan(p)
close("L22 alpha = w sqrt(mu eps/2) [sqrt(1+p^2)-1]^1/2 equals (1+p^2)^1/4 sin(theta/2)",
      np.sqrt(0.5 * (np.sqrt(1 + p * p) - 1)), (1 + p * p) ** 0.25 * np.sin(th / 2))
close("L22 beta form equals (1+p^2)^1/4 cos(theta/2)", np.sqrt(0.5 * (np.sqrt(1 + p * p) + 1)), (1 + p * p) ** 0.25 * np.cos(th / 2))
close("sigma/(w eps) = tan(2 tau)", np.tan(2 * (th / 2)), p)
close("notes' small-p phase tan^-1(p/2) - (1/2)tan^-1(p) = p^3/8 + O(p^5): agree beyond first order (p=1e-2)",
      np.arctan(0.5e-2) - 0.5 * np.arctan(1e-2), 1e-6 / 8, rtol=1e-3)


def errs(p):
    th = np.arctan(p)
    a = (1 + p * p) ** 0.25 * np.sin(th / 2)
    b = (1 + p * p) ** 0.25 * np.cos(th / 2)
    e = (1 + p * p) ** -0.25
    return a, b, e, th / 2


a, b, e, t = errs(0.1)
print(f"  p = 0.1: ID alpha +{100 * (0.05 / a - 1):.4f} %, beta {100 * (1 / b - 1):.4f} %, |eta| +{100 * (1 / e - 1):.4f} %, "
      f"tau +{100 * (0.05 / t - 1):.4f} %")
agree("p = 0.1: ID alpha error [%] ('about 0.12 %')", 100 * (0.05 / a - 1), "0.12")
agree("p = 0.1: ID beta error [%] ('about 0.12 %')", 100 * abs(1 / b - 1), "0.12")
agree("p = 0.1: ID |eta| error [%]", 100 * (1 / e - 1), "0.25")
agree("p = 0.1: ID tau error [%]", 100 * (0.05 / t - 1), "0.33")
claim("p = 0.1: all four within 'about 0.3 %' (max 0.33 %)", max(0.05 / a - 1, abs(1 / b - 1), 1 / e - 1, 0.05 / t - 1) < 0.0035)
a, b, e, t = errs(10.0)
agree("p = 10: GC alpha too high by [%]", 100 * (np.sqrt(5) / a - 1), "5")
agree("p = 10: GC beta too low by [%]", 100 * (1 - np.sqrt(5) / b), "5")
agree("p = 10: true tau [deg]", np.degrees(t), "42.1")
a, b, e, t = errs(1.0)
agree("p = 1: ID alpha high by [%]", 100 * (0.5 / a - 1), "10")
agree("p = 1: GC alpha high by [%]", 100 * (np.sqrt(0.5) / a - 1), "55")
a3, *_ = errs(0.3)
a4, *_ = errs(3.0)
agree("p = 0.3: ID alpha still within [%] (added in review)", 100 * (0.15 / a3 - 1), "1.1")
agree("p = 3: GC alpha high by [%] (added in review)", 100 * (np.sqrt(1.5) / a4 - 1), "18")
# the table's limits against exact values at extreme p
E = exact(1e3, 1e-12, 4)
close("table ID row: alpha -> (sigma/2) sqrt(mu/eps) for p << 1", E["a"], 0.5e-12 * np.sqrt(MU0 / (4 * EPS0)), rtol=1e-6)
close("table ID row: beta -> w sqrt(mu eps)", E["b"], E["w"] * np.sqrt(MU0 * 4 * EPS0), rtol=1e-9)
close("table ID row: tau -> sigma/(2 w eps)", E["tau"], E["p"] / 2, rtol=1e-6)
close("table ID row: delta = (2/sigma) sqrt(eps/mu)", 1 / E["a"], 2 / 1e-12 * np.sqrt(4 * EPS0 / MU0), rtol=1e-6)
close("notes' ID alpha = beta * (1/2) sigma/(w eps) is the same thing", E["b"] * E["p"] / 2, 0.5e-12 * np.sqrt(MU0 / (4 * EPS0)),
      rtol=1e-6)
E = exact(1e3, 5.8e7, 1)
G = gc(1e3, 5.8e7)
close("table GC row: alpha -> sqrt(pi f mu sigma) (copper 1 kHz)", E["a"], G["a"], rtol=1e-6)
close("table GC row: beta -> sqrt(pi f mu sigma)", E["b"], G["b"], rtol=1e-6)
close("table GC row: |eta| -> sqrt(w mu/sigma)", E["aeta"], G["aeta"], rtol=1e-6)
close("table GC row: tau -> 45 deg", np.degrees(E["tau"]), 45, rtol=1e-6)
close("table GC row: lambda = 2 pi delta", 2 * PI / E["b"], 2 * PI * G["d"], rtol=1e-6)
close("p >> 1 limit: w sqrt(mu eps) sqrt(p)/sqrt2 = sqrt(w mu sigma/2) = sqrt(pi f mu sigma)",
      E["w"] * np.sqrt(E["mu"] * E["eps"]) * np.sqrt(E["p"] / 2), np.sqrt(PI * 1e3 * MU0 * 5.8e7))
close("p >> 1 limit: sqrt(mu/eps)/sqrt(p) = sqrt(w mu/sigma)", np.sqrt(MU0 / EPS0) / np.sqrt(E["p"]), G["aeta"])
# the attenuation plateau
plat = 4 / 2 * np.sqrt(MU0 / (81 * EPS0))
agree("seawater plateau alpha [Np/m]", plat, "84")
agree("seawater plateau penetration depth [cm]", 100 / plat, "1.2")
close("exact seawater alpha at 1 THz -> plateau (constant eps)", exact(1e12, 4, 81)["a"], plat, rtol=1e-3)
for f in (1e2, 1e5, 1e7):
    close(f"Rao 5.26: GC alpha = plateau * sqrt(2 w eps/sigma) (seawater {f:g} Hz)",
          gc(f, 4)["a"], plat * np.sqrt(2 * 2 * PI * f * 81 * EPS0 / 4))

# ======================================================================================== D
sec("D  Example 1 (notes): numbers, directions, Maxwell by finite differences, time averages by quadrature")
f1, s1, er1, E0 = 1e9, 1e-3, 4.0, 2.0
Ec = exact(f1, s1, er1, eps0=EPS0C)       # the notes use 1e-9/36pi
Ex1 = exact(f1, s1, er1)                    # exact constants
agree("Ex1 sigma/(w eps) [1e-3]", Ec["p"], "4.5", scale=1e-3)
agree("Ex1 tau ~ sigma/(2 w eps) [1e-3 rad]", Ec["p"] / 2, "2.25", scale=1e-3)
agree("Ex1 tau [deg]", np.degrees(Ex1["tau"]), "0.13")
agree("Ex1 |eta| ~ eta0/2 = 60 pi [ohm]", 60 * PI, "188")
agree("Ex1 exact |eta| [ohm]", Ex1["aeta"], "188")
alpha1 = s1 / 2 * 60 * PI
close("Ex1 alpha = (sigma/2)|eta| = 30 pi 1e-3", alpha1, 30 * PI * 1e-3)
agree("Ex1 alpha [Np/m]", alpha1, "0.094")
agree("Ex1 exact alpha [Np/m]", Ex1["a"], "0.094")
agree("Ex1 beta [rad/m]", 2 * PI * f1 * np.sqrt(MU0 * er1 * EPS0), "41.9")
agree("Ex1 lambda [cm]", 100 * 2 * PI / Ex1["b"], "15")
# direction: H = u x E / eta with u = z, E along y
u, eE = np.array([0, 0, 1.0]), np.array([0, 1.0, 0])
claim("Ex1 z x y = -x", np.allclose(np.cross(u, eE), [-1, 0, 0]))
claim("Ex1 y x (-x) = +z (E x H along travel)", np.allclose(np.cross(eE, [-1, 0, 0]), [0, 0, 1]))
agree("Ex1 2/|eta| [mA/m]", 2 / (60 * PI), "10.6", scale=1e-3)


def fd_maxwell_z(E, E0, sgn=+1, npts=40, h=None):
    """E = x E0 e^{-a d} cos(wt - b d), H = sgn*y (E0/|eta|) e^{-a d} cos(wt - b d - tau), d = sgn*z.
    Returns max relative residuals of Faraday (dEx/dz = -mu dHy/dt) and Ampere (-dHy/dz = sigma Ex + eps dEx/dt)."""
    a, b, ae, ta, w, mu, eps, sig = E["a"], E["b"], E["aeta"], E["tau"], E["w"], E["mu"], E["eps"], E["sig"]
    Exf = lambda z, t: E0 * np.exp(-a * sgn * z) * np.cos(w * t - b * sgn * z)
    Hyf = lambda z, t: sgn * E0 / ae * np.exp(-a * sgn * z) * np.cos(w * t - b * sgn * z - ta)
    L = 1 / max(a, b)
    hz = 1e-5 * L if h is None else h
    ht = 1e-5 / w
    rf = ra = 0.0
    for _ in range(npts):
        z = rng.uniform(-2, 2) * L
        t = rng.uniform(0, 2 * PI / w)
        dEz = (Exf(z + hz, t) - Exf(z - hz, t)) / (2 * hz)
        dHt = (Hyf(z, t + ht) - Hyf(z, t - ht)) / (2 * ht)
        dHz = (Hyf(z + hz, t) - Hyf(z - hz, t)) / (2 * hz)
        dEt = (Exf(z, t + ht) - Exf(z, t - ht)) / (2 * ht)
        env = abs(E0) * np.exp(-a * sgn * z)          # amplitude scale at this depth
        scale_f = abs(a + 1j * b) * env                 # size of dE/dz
        scale_a = abs(sig + 1j * w * eps) * env         # size of the total current density
        rf = max(rf, abs(dEz + mu * dHt) / scale_f)
        ra = max(ra, abs(-dHz - sig * Exf(z, t) - eps * dEt) / scale_a)
    return rf, ra


rf, ra = fd_maxwell_z(Ex1, E0)
claim("Ex1 time-domain E and H (H lags by tau) satisfy Faraday and Ampere with sigma (finite differences)",
      rf < 1e-6 and ra < 1e-6, f"residuals {rf:.1e}, {ra:.1e}")
rf2, ra2 = fd_maxwell_z(Ex1, E0, sgn=-1)
claim("-z travelling version (lower signs of the notes' margin pair, H = -y ...) also satisfies both", rf2 < 1e-6 and ra2 < 1e-6)
# time average by quadrature vs 1/2 Re{E x H*} vs the formula
for z in (0.0, 10.0):
    tt = np.arange(4096) * (2 * PI / Ex1["w"]) / 4096
    Evec = np.outer(E0 * np.exp(-Ex1["a"] * z) * np.cos(Ex1["w"] * tt - Ex1["b"] * z), [0, 1, 0])
    Hvec = np.outer(E0 / Ex1["aeta"] * np.exp(-Ex1["a"] * z) * np.cos(Ex1["w"] * tt - Ex1["b"] * z - Ex1["tau"]), [-1, 0, 0])
    Sq = np.cross(Evec, Hvec).mean(axis=0)            # time average of the instantaneous E x H
    Ep = np.array([0, 1, 0]) * E0 * np.exp(-Ex1["g"] * z)
    Hp = np.array([-1, 0, 0]) * E0 / Ex1["eta"] * np.exp(-Ex1["g"] * z)
    Sp = 0.5 * np.real(np.cross(Ep, np.conj(Hp)))
    Sf = np.array([0, 0, 1]) * E0 ** 2 / (2 * Ex1["aeta"]) * np.cos(Ex1["tau"]) * np.exp(-2 * Ex1["a"] * z)
    claim(f"Ex1 <S>(z={z:g}): quadrature = 1/2 Re(E x H*) = z |E0|^2 cos(tau) e^-2az/(2|eta|)",
          np.allclose(Sq, Sp, rtol=1e-9) and np.allclose(Sp, Sf, rtol=1e-9), f"{Sp[2]:.5g} W/m^2")
agree("Ex1 <S>(0) = 1/(30 pi) [mW/m^2]", 1 / (30 * PI), "10.6", scale=1e-3)
fac10 = np.exp(-2 * 30 * PI * 1e-3 * 10)
close("Ex1 e^{-2 alpha 10} = e^{-0.6 pi}", fac10, np.exp(-0.6 * PI))
agree("Ex1 power factor after 10 m", fac10, "0.15")
agree("Ex1 <S>(10 m) [mW/m^2]", fac10 / (30 * PI), "1.6", scale=1e-3)
agree("Ex1 power left after 10 m [%]", 100 * fac10, "15")
agree("Ex1 loss [dB/m] = 8.686 alpha", NP2DB * alpha1, "0.82")
agree("Ex1 loss over 10 m [dB]", NP2DB * alpha1 * 10, "8.2")
agree("Ex1 penetration depth 1/alpha [m]", 1 / alpha1, "10.6")
# general key callout with complex E0
E0c = 1.7 * np.exp(1j * 0.9)
Em = exact(3e7, 0.02, 9)
z = 0.37
Sp = 0.5 * np.real(np.cross(np.array([1, 0, 0]) * E0c * np.exp(-Em["g"] * z), np.conj(np.array([0, 1, 0]) * E0c / Em["eta"]
                                                                                          * np.exp(-Em["g"] * z))))
Sq = tavg(lambda t: np.abs(E0c) * np.exp(-Em["a"] * z) * np.cos(Em["w"] * t - Em["b"] * z + np.angle(E0c))
          * np.abs(E0c) / Em["aeta"] * np.exp(-Em["a"] * z) * np.cos(Em["w"] * t - Em["b"] * z + np.angle(E0c) - Em["tau"]),
          Em["w"])
close("key: <S_z> for complex E0 = |E0|^2 cos(tau) e^-2az/(2|eta|) (phasor and quadrature)", [Sp[2], Sq],
      abs(E0c) ** 2 * np.cos(Em["tau"]) / (2 * Em["aeta"]) * np.exp(-2 * Em["a"] * z) * np.ones(2), rtol=1e-9)
close("power at z = delta/2 is 1/e of the surface value", np.exp(-2 * Em["a"] * (0.5 / Em["a"])), np.exp(-1))
close("dB: 10 log10 e^{2az} = 20 log10 e^{az} = 8.686 a z", 10 * np.log10(np.exp(2 * 0.3)), NP2DB * 0.3)
agree("one neper in dB", NP2DB, "8.686")
close("cos(tau) = 1/sqrt2 in a good conductor (copper 1 kHz)", np.cos(exact(1e3, 5.8e7, 1)["tau"]), 2 ** -0.5, rtol=1e-6)

# ======================================================================================== E
sec("E  Energy balance: div<S> = -<J.E>, alpha = sigma|eta|/(2 cos tau) exactly")
ok = True
for k in range(200):
    f = 10 ** rng.uniform(0, 11)
    s = 10 ** rng.uniform(-10, 8)
    er = rng.uniform(1, 90)
    E = exact(f, s, er, rng.choice([1.0, 5.0]))
    ok &= np.isclose(E["a"], s * E["aeta"] / (2 * np.cos(E["tau"])), rtol=1e-8)
    ok &= np.isclose((E["g"] / E["eta"]).real, s, rtol=1e-8)
claim("200 random media: alpha = sigma |eta| / (2 cos tau) and Re{gamma/eta} = sigma", ok)
for E, nm in ((Ex1, "Ex1 medium"), (exact(1e3, 4, 81), "seawater 1 kHz"), (exact(1e9, 4, 81), "seawater 1 GHz")):
    z0, w = 0.3 / E["a"], E["w"]
    h = 1e-4 / E["a"]
    S = lambda z: E0 ** 2 / (2 * E["aeta"]) * np.cos(E["tau"]) * np.exp(-2 * E["a"] * z)
    divS = (S(z0 + h) - S(z0 - h)) / (2 * h)
    JE = tavg(lambda t: E["sig"] * (E0 * np.exp(-E["a"] * z0) * np.cos(w * t - E["b"] * z0)) ** 2, w)
    claim(f"{nm}: -d<S_z>/dz (finite difference) = <J.E> (quadrature)", np.isclose(-divS, JE, rtol=1e-6),
          f"{JE:.4g} W/m^3")
agree("Ex1 heating at z=0: (1/2) sigma |E0|^2 [mW/m^3]", 0.5 * 1e-3 * 4, "2.0", scale=1e-3)
agree("Ex1 2 alpha <S>(0) [mW/m^3]", 2 * 30 * PI * 1e-3 / (30 * PI), "2.0", scale=1e-3)
claim("energy-balance statement: NET INFLOW -d<S_z>/dz > 0 equals the power delivered <J.E> > 0 (sign check)",
      -divS > 0 and JE > 0 and np.isclose(-divS, JE, rtol=1e-6), "div<S> = -<J.E> < 0: more power enters than leaves")

# ======================================================================================== F
sec("F  Good conductor: delta, gamma, eta, time-domain fields, energy ratio; Examples 2 and 3")
for f, s in ((1e3, 4.0), (60.0, 5.8e7), (1e9, 3.5e7)):
    G = gc(f, s)
    w = 2 * PI * f
    close(f"delta = 1/sqrt(pi f mu sigma) = sqrt(2/(w mu sigma)) (f={f:g}, sigma={s:g})", G["d"], np.sqrt(2 / (w * MU0 * s)))
    close("  eta = (1+j)/(sigma delta) = sqrt(w mu/sigma) e^{j pi/4}", G["eta"], np.sqrt(w * MU0 / s) * np.exp(1j * PI / 4))
    close("  sqrt(w mu/(2 sigma)) = 1/(sigma delta)", np.sqrt(w * MU0 / (2 * s)), 1 / (s * G["d"]))
    close("  gamma = (1+j)/delta = sqrt(j w mu sigma)", (1 + 1j) / G["d"], np.sqrt(1j * w * MU0 * s))
    close("  v_p = w/beta = w delta = sqrt(2 w/(mu sigma))", w * G["d"], np.sqrt(2 * w / (MU0 * s)))
    close("  1/|eta| = sigma delta/sqrt2", 1 / G["aeta"], s * G["d"] / np.sqrt(2))
    close("  power: |E0|^2 cos(45)/(2|eta|) = sigma delta E0^2/4 (E0=1)", np.cos(PI / 4) / (2 * G["aeta"]), s * G["d"] / 4)
close("sqrt(j) = e^{j pi/4} = (1+j)/sqrt2", np.sqrt(1j), (1 + 1j) / np.sqrt(2))
# Maxwell check of the key's time-domain pair using exact parameters for seawater at 1 kHz
Esw = exact(1e3, 4, 81)
rf, ra = fd_maxwell_z(Esw, 1.0)
claim("seawater 1 kHz: E, H (lag tau) satisfy Faraday and Ampere (finite differences, exact parameters)",
      rf < 1e-6 and ra < 1e-6, f"{rf:.1e}, {ra:.1e}")
Gsw = gc(1e3, 4)
Eapprox = dict(Esw)
Eapprox.update(a=Gsw["a"], b=Gsw["b"], aeta=Gsw["aeta"], tau=PI / 4)
rf, ra = fd_maxwell_z(Eapprox, 1.0)
claim("the key's good-conductor pair (alpha = beta = 1/delta, tau = 45 deg) satisfies Faraday exactly and Ampere to "
      "O(w eps/sigma) = 1.1e-6", rf < 1e-8 and ra < 3e-6, f"{rf:.1e}, {ra:.1e}")
# directions
claim("GC key: z x x = y (H along +y for E along +x, travel +z)", np.allclose(np.cross([0, 0, 1], [1, 0, 0]), [0, 1, 0]))
claim("GC key: x x y = z (E x H along travel)", np.allclose(np.cross([1, 0, 0], [0, 1, 0]), [0, 0, 1]))
# time-average power by quadrature for the key
G = gc(1e3, 4)
w = 2 * PI * 1e3
zz = 2.0
Sq = tavg(lambda t: np.exp(-zz / G["d"]) * np.cos(w * t - zz / G["d"]) * 4 * G["d"] / np.sqrt(2) * np.exp(-zz / G["d"])
          * np.cos(w * t - zz / G["d"] - PI / 4), w)
close("GC key: quadrature <E_x H_y> = sigma delta E0^2/4 e^{-2z/delta}", Sq, 4 * G["d"] / 4 * np.exp(-2 * zz / G["d"]))
agree("e^{2 pi} ('1/535')", np.exp(2 * PI), "535")
agree("field drop per wavelength [dB]", 20 * np.log10(np.exp(2 * PI)), "54.6")
agree("seawater 1 kHz lambda = 2 pi delta [m]", 2 * PI * gc(1e3, 4)["d"], "50")
agree("seawater 1 kHz v_p [1e4 m/s]", 2 * PI * 1e3 * gc(1e3, 4)["d"], "5", scale=1e4)
agree("lossless eps_r=81: c/9 [1e7 m/s]", C0 / 9, "3.3", scale=1e7)
agree("copper 1 MHz lambda [mm]", 2 * PI * gc(1e6, 5.8e7)["d"] * 1e3, "0.42")
agree("copper 1 MHz v_p [m/s]", 2 * PI * 1e6 * gc(1e6, 5.8e7)["d"], "415")
agree("seawater 1 kHz 1/|eta| [(A/m)/(V/m)]", 1 / gc(1e3, 4)["aeta"], "22.5")
# stored energies by quadrature, exact seawater 1 kHz
Es = exact(1e3, 4, 81)
we = tavg(lambda t: 0.5 * Es["eps"] * np.cos(Es["w"] * t) ** 2, Es["w"])
wm = tavg(lambda t: 0.5 * Es["mu"] * (np.cos(Es["w"] * t - Es["tau"]) / Es["aeta"]) ** 2, Es["w"])
close("<w_e>/<w_m> = eps|eta|^2/mu = 1/sqrt(1+p^2) (quadrature, exact)", we / wm, 1 / np.sqrt(1 + Es["p"] ** 2), rtol=1e-9)
agree("<w_e>/<w_m> seawater 1 kHz [1e-6]", we / wm, "1.1", scale=1e-6)
close("  ~ w eps/sigma", we / wm, 1 / Es["p"], rtol=1e-6)
El = exact(1e3, 0.0, 81)
claim("lossless: <w_e> = <w_m>", np.isclose(El["eps"] * El["aeta"] ** 2 / El["mu"], 1.0))
# intuition: surface resistance, absorbed power
s, d = 5.8e7, gc(1e9, 5.8e7)["d"]
l = 0.01
close("square slab l x l, thickness delta: R = l/(sigma l delta) = 1/(sigma delta) = Re{eta}", l / (s * l * d), gc(1e9, s)["eta"].real)
H0 = 3.0
close("absorbed power 1/2 Re{eta} |H0|^2 = |H0|^2/(2 sigma delta)", 0.5 * gc(1e9, s)["eta"].real * H0 ** 2, H0 ** 2 / (2 * s * d))
close("  = sigma delta E0^2/4 with E0 = |eta| H0", s * d * (gc(1e9, s)["aeta"] * H0) ** 2 / 4, H0 ** 2 / (2 * s * d))
# Example 2
agree("Ex2 notes' sigma/(w eps) with eps = 4 eps0 [1e7]", 4 * 36 * PI * 1e9 / (2 * PI * 1e3 * 4), "1.8", scale=1e7)
agree("Ex2 with seawater's 81 eps0 [1e5]", exact(1e3, 4, 81, eps0=EPS0C)["p"], "8.9", scale=1e5)
eta2 = np.sqrt(2 * PI * 1e3 * MU0 / 4)
close("Ex2 |eta| = pi sqrt2/100", eta2, PI * np.sqrt(2) / 100)
agree("Ex2 |eta| [ohm]", eta2, "0.0444")
a2 = np.sqrt(PI * 1e3 * MU0 * 4)
close("Ex2 alpha = sqrt(16 pi^2 1e-4) = pi/25", a2, PI / 25)
agree("Ex2 alpha [Np/m]", a2, "0.126")
agree("Ex2 |H| = 2/|eta| [A/m]", 2 / eta2, "45")
agree("Ex2 H ratio to Ex1 ('4,240')", (2 / eta2) / (2 / (60 * PI)), "4240", sf=3)
S2 = 2 / eta2 * np.cos(PI / 4)
close("Ex2 <S>(0) = 100/pi", S2, 100 / PI)
agree("Ex2 <S>(0) [W/m^2]", S2, "31.8")
agree("Ex2 / Ex1 power ratio", S2 / (1 / (30 * PI)), "3000")
close("Ex2 e^{-2 (pi/25) 10} = e^{-0.8 pi}", np.exp(-2 * a2 * 10), np.exp(-0.8 * PI))
agree("Ex2 factor after 10 m", np.exp(-0.8 * PI), "0.081")
agree("Ex2 <S>(10 m) [W/m^2]", S2 * np.exp(-0.8 * PI), "2.6")
agree("Ex2 power left [%]", 100 * np.exp(-0.8 * PI), "8")
agree("Ex2 loss [dB/m]", NP2DB * a2, "1.09")
claim("Ex2 exact parameters (seawater eps) agree with GC values to < 1e-6", abs(exact(1e3, 4, 81)["a"] / a2 - 1) < 1e-6)
# Example 3
agree("Ex3 72e9/(81e3) [1e5]", 72e9 / 81e3, "8.9", scale=1e5)
close("Ex3 delta = 1/sqrt(16 pi^2 1e-4) = 100/(4 pi) = 25/pi", 1 / np.sqrt(PI * 1e3 * MU0 * 4), 25 / PI)
agree("Ex3 delta [m] (notes print 7.95: truncation)", 25 / PI, "7.96")
claim("notes' 7.95 m is not the rounding of 25/pi", abs(25 / PI - 7.95) > 0.005)
close("Ex3 exact delta (eps = 81 eps0) vs 25/pi", 1 / exact(1e3, 4, 81)["a"], 25 / PI, rtol=1e-5)

# ======================================================================================== G
sec("G  Seawater at several frequencies, the fair comparison, submarines")
agree("1 kHz seawater loses over 10 m [%]", 100 * (1 - np.exp(-0.8 * PI)), "92")
agree("1 GHz Example 1 wave loses over 10 m [%]", 100 * (1 - np.exp(-0.6 * PI)), "85")
E1g = exact(1e9, 4, 81)
agree("seawater 1 GHz exact alpha [Np/m]", E1g["a"], "77")
agree("seawater 1 GHz delta [cm]", 100 / E1g["a"], "1.3")
agree("seawater 1 GHz loss [dB/m]", NP2DB * E1g["a"], "673")
agree("seawater 1 GHz loss over 10 m [dB] ('6,700')", NP2DB * E1g["a"] * 10, "6700", sf=2)
agree("seawater 1 kHz loss over 10 m [dB]", NP2DB * exact(1e3, 4, 81)["a"] * 10, "11")
close("GC: factor 100 lower in f -> dB/m down 10x", gc(1e5, 4)["a"] / gc(1e3, 4)["a"], 10)
FT = [  # f, sigma/(w eps), delta [m], dB/m, depth for 100 dB [m], lambda0 [m]
    (76.0, ("1.2", 1e7), ("28.9", 1), ("0.30", 1), ("332", 1), ("3900", 1e3)),
    (1e3, ("8.9", 1e5), ("7.96", 1), ("1.09", 1), ("92", 1), ("300", 1e3)),
    (24e3, ("3.7", 1e4), ("1.62", 1), ("5.3", 1), ("19", 1), ("12.5", 1e3)),
    (1e6, ("888", 1), ("25", 1e-2), ("34.5", 1), ("2.9", 1), ("300", 1)),
    (1e8, ("8.9", 1), ("2.7", 1e-2), ("326", 1), ("31", 1e-2), ("3", 1)),
    (1e9, ("0.89", 1), ("1.3", 1e-2), ("673", 1), ("15", 1e-2), ("30", 1e-2)),
]
for f, pp, dd, db, dep, lam in FT:
    E = exact(f, 4, 81)
    agree(f"table {f:g} Hz: sigma/(w eps)", E["p"], pp[0], scale=pp[1])
    agree(f"table {f:g} Hz: delta", 1 / E["a"], dd[0], scale=dd[1])
    agree(f"table {f:g} Hz: dB/m", NP2DB * E["a"], db[0], scale=db[1])
    agree(f"table {f:g} Hz: depth for 100 dB", 100 / (NP2DB * E["a"]), dep[0], scale=dep[1])
    lam0 = C0 / f
    if f == 76.0:
        claim("table 76 Hz: lambda0 = 3,945 km, printed '3,900 km' (2 s.f.)", round(lam0 / 1e3, -2) == 3900, f"{lam0 / 1e3:.0f} km")
    else:
        agree(f"table {f:g} Hz: free-space lambda0", lam0, lam[0], scale=lam[1])
agree("100 dB budget depth = 100/8.686 skin depths", 100 / NP2DB, "11.5")
G100 = gc(1e8, 4)["d"]
E100 = 1 / exact(1e8, 4, 81)["a"]
agree("100 MHz GC delta [cm]", 100 * G100, "2.5")
agree("100 MHz GC delta short of exact by [%] ('about 5 %')", 100 * (1 - G100 / E100), "5")
claim("1 GHz GC delta (0.80 cm) off the exact 1.29 cm by > 35 % ('badly wrong')", 1 - gc(1e9, 4)["d"] * exact(1e9, 4, 81)["a"] > 0.35)
# Wikipedia figures (Communication with submarines): VLF 3-30 kHz 'a few tens of metres', ~300 bit/s;
# ELF 76 Hz (US, dismantled Sept 2004) and 82 Hz (ZEVS) 'hundreds of metres', 'a few characters per minute'
d24 = 100 / (NP2DB * exact(24e3, 4, 81)["a"])
d76 = 100 / (NP2DB * exact(76, 4, 81)["a"])
claim("100 dB depth at 24 kHz (19 m) is 'a few tens of metres' order (10-60 m)", 10 < d24 < 60, f"{d24:.1f} m")
claim("100 dB depth at 76 Hz (332 m) is 'hundreds of metres'", 100 < d76 < 1000, f"{d76:.0f} m")
agree("air wavelength at 24 kHz [km]", C0 / 24e3 / 1e3, "12.5")
agree("in-water wavelength at 1 kHz (Rao's point) [m]", 2 * PI * gc(1e3, 4)["d"], "50")
agree("free-space wavelength at 1 kHz [km]", C0 / 1e3 / 1e3, "300")
close("Rao (5.75): lambda_conductor/lambda_dielectric = sqrt(2 w eps/sigma) (seawater, 25 kHz)",
      (2 * PI * gc(25e3, 4)["d"]) / (2 * PI / (2 * PI * 25e3 * np.sqrt(MU0 * 80 * EPS0))),
      np.sqrt(2 * 2 * PI * 25e3 * 80 * EPS0 / 4))

# ======================================================================================== H
sec("H  Metals: skin depths, |eta|, skin effect, shielding, copper f_c")
agree("copper delta*sqrt(f) [m]", 1 / np.sqrt(PI * MU0 * 5.8e7), "0.0661")
agree("Rao's copper figure 0.066/sqrt f", 1 / np.sqrt(PI * MU0 * 5.8e7), "0.066")
agree("aluminium delta*sqrt(f) [m]", 1 / np.sqrt(PI * MU0 * 3.5e7), "0.0851")
MT = [(60, "8.53", 1e-3, "11.0", 1e-3, "2.86", 1e-6), (1e3, "2.09", 1e-3, "2.69", 1e-3, "11.7", 1e-6),
      (1e6, "66.1", 1e-6, "85.1", 1e-6, "0.369", 1e-3), (1e8, "6.61", 1e-6, "8.51", 1e-6, "3.69", 1e-3),
      (1e9, "2.09", 1e-6, "2.69", 1e-6, "11.7", 1e-3), (1e10, "0.661", 1e-6, "0.851", 1e-6, "36.9", 1e-3)]
for f, dcu, s1_, dal, s2_, eta_s, s3_ in MT:
    agree(f"copper delta at {f:g} Hz", gc(f, 5.8e7)["d"], dcu, scale=s1_)
    agree(f"aluminium delta at {f:g} Hz", gc(f, 3.5e7)["d"], dal, scale=s2_)
    agree(f"copper |eta| at {f:g} Hz", gc(f, 5.8e7)["aeta"], eta_s, scale=s3_)
    claim(f"  copper is a good conductor at {f:g} Hz (exact delta within 1e-6)", abs(exact(f, 5.8e7, 1)["a"] * gc(f, 5.8e7)["d"] - 1) < 1e-6)
agree("copper |eta|/sqrt(f) [1e-7 ohm]", np.sqrt(2 * PI * MU0 / 5.8e7), "3.69", scale=1e-7)
agree("skin effect a/(2 delta), copper 1 mm radius, 1 MHz", 1e-3 / (2 * gc(1e6, 5.8e7)["d"]), "7.6")
claim("60 Hz copper delta 8.5 mm > radius of 12 AWG (1.03 mm) and 14 AWG (0.81 mm) house wire", gc(60, 5.8e7)["d"] > 1.03e-3)
agree("1 mm Al at 60 Hz in skin depths", 1e-3 / gc(60, 3.5e7)["d"], "0.09")
agree("1 mm Al at 1 MHz in skin depths", 1e-3 / gc(1e6, 3.5e7)["d"], "11.8")
agree("  absorption [dB]", NP2DB * 1e-3 / gc(1e6, 3.5e7)["d"], "102")
agree("Al delta at 2.45 GHz [um]", gc(2.45e9, 3.5e7)["d"], "1.7", scale=1e-6)
claim("0.5 mm wall at 2.45 GHz is 'hundreds of skin depths'", 100 < 0.5e-3 / gc(2.45e9, 3.5e7)["d"] < 1000,
      f"{0.5e-3 / gc(2.45e9, 3.5e7)['d']:.0f}")
agree("copper |eta| at 1 GHz / eta0 [1e-5]", gc(1e9, 5.8e7)["aeta"] / ETA0, "3", scale=1e-5)
agree("copper f_c [1e18 Hz]", fc(5.8e7, 1), "1.0", scale=1e18)
Eph = 6.62607015e-34 * fc(5.8e7, 1) / 1.602176634e-19
claim("photon energy at copper's f_c is in the X-ray range (0.1-100 keV)", 100 < Eph < 1e5, f"{Eph / 1e3:.1f} keV")
f1pc = np.sqrt(1 / 0.99 ** 2 - 1) * nu_cu / (2 * PI)
claim("Drude: knee nu/2pi = 6.5 THz (infrared), |sigma(w)| down 1 % near 0.9 THz: 'about 1e13 Hz' is the knee (left)",
      abs(nu_cu / (2 * PI) / 6.5e12 - 1) < 0.05 and 0.8e12 < f1pc < 1.0e12, f"1 % at {f1pc / 1e12:.2f} THz")
agree("aluminium / copper skin-depth ratio sqrt(5.8/3.5)", np.sqrt(5.8 / 3.5), "1.29")

# ======================================================================================== I
sec("I  Inverse example: 200 MHz, lambda = 0.5 m, delta = 20 m")
f, lam, dl = 2e8, 0.5, 20.0
b_, a_ = 2 * PI / lam, 1 / dl
w = 2 * PI * f
agree("beta [rad/m]", b_, "12.6")
agree("alpha/beta", a_ / b_, "0.004")
agree("tau [deg]", np.degrees(np.arctan(a_ / b_)), "0.23")
agree("p = tan 2 tau", np.tan(2 * np.arctan(a_ / b_)), "0.008")
agree("delta/lambda (wavelengths to 1/e)", dl / lam, "40")
agree("v_p [1e8 m/s]", lam * f, "1", scale=1e8)
agree("eps_r = (c/v_p)^2 with c = 3e8", (3e8 / (lam * f)) ** 2, "9")
er_ex = (b_ ** 2 - a_ ** 2) / (w ** 2 * MU0 * EPS0)
agree("exact eps_r = (beta^2 - alpha^2)/(w^2 mu0 eps0) (CODATA c)", er_ex, "9.0")
agree("|eta| = eta0/3 = 40 pi [ohm]", 40 * PI, "126")
agree("exact |eta| = w mu0/|gamma| [ohm]", w * MU0 / abs(a_ + 1j * b_), "126")
agree("sigma = 2 alpha/|eta| [1e-4 S/m]", 2 * a_ / (40 * PI), "8.0", scale=1e-4)
agree("exact sigma = 2 alpha beta/(w mu0) [1e-4 S/m]", 2 * a_ * b_ / (w * MU0), "8.0", scale=1e-4)
agree("check sigma/(w eps) with eps = 9 eps0", 7.96e-4 / (w * 9 * EPS0), "0.008")

# ======================================================================================== J
sec("J  Worked problem: moist soil, 100 kHz, travel along -y")
fp, sp, erp = 1e5, 1e-2, 10.0
Pc = exact(fp, sp, erp, eps0=EPS0C)
Pe = exact(fp, sp, erp)
Pg = gc(fp, sp)
close("(a) sigma/(w eps) = 180 (course eps0)", Pc["p"], 180, rtol=1e-12)
agree("(a) with eps0 = 8.854e-12", Pe["p"], "179.75")
agree("(a) eps/sigma [ns]", erp * EPS0 / sp, "8.9", scale=1e-9)
agree("(a) period [us]", 1 / fp, "10", scale=1e-6)
agree("(a) trap: eps0 instead of 10 eps0", 10 * Pc["p"], "1800")
agree("(a) trap: f instead of w", 2 * PI * Pc["p"], "1130", sf=3)
agree("(a) soil crossover [MHz]", fc(sp, erp), "18", scale=1e6)
close("(b) pi f mu0 sigma = 4 pi^2 1e-4", PI * fp * MU0 * sp, 4 * PI ** 2 * 1e-4)
agree("(b) alpha = beta = 2 pi 1e-2 [1/m]", Pg["a"], "0.0628")
agree("(b) delta = 50/pi [m]", Pg["d"], "15.9")
close("(b) delta = 50/pi", Pg["d"], 50 / PI)
agree("(b) lambda = 2 pi delta [m]", 2 * PI * Pg["d"], "100")
agree("(b) v_p = lambda f [1e7 m/s]", 2 * PI * Pg["d"] * fp, "1", scale=1e7)
agree("(b) v_p = c/30 (c = 3e8)", 3e8 / (2 * PI * Pg["d"] * fp), "30")
agree("(b) exact delta [m]", 1 / Pe["a"], "15.96")
agree("(b) exact lambda [m]", 2 * PI / Pe["b"], "99.7")
claim("(b) exact within 0.3 %", abs(1 / Pe["a"] / Pg["d"] - 1) < 0.003 and abs(2 * PI / Pe["b"] / 100 - 1) < 0.003)
agree("(b) lossless lambda with eps_r = 10 [m] ('≈950 m')", 3e8 / (fp * np.sqrt(10)), "950", sf=2)
agree("(b) shortening factor ('almost tenfold')", 3e8 / (fp * np.sqrt(10)) / 100, "9.5")
close("(c) |eta| = sqrt(8 pi^2) = 2 sqrt2 pi", Pg["aeta"], 2 * np.sqrt(2) * PI)
agree("(c) |eta| [ohm]", Pg["aeta"], "8.89")
close("(c) sigma delta = 1/(2 pi)", sp * Pg["d"], 1 / (2 * PI))
close("(c) eta = 2 pi (1+j)", Pg["eta"], 2 * PI * (1 + 1j))
claim("(c) (-y) x x = +z", np.allclose(np.cross([0, -1, 0], [1, 0, 0]), [0, 0, 1]))
claim("(c) x x z = -y (E x H down)", np.allclose(np.cross([1, 0, 0], [0, 0, 1]), [0, -1, 0]))
agree("(c) 1/|eta| [A/m]", 1 / Pg["aeta"], "0.1125")
agree("(c) T/8 [us]", 1 / fp / 8, "1.25", scale=1e-6)


def fd_maxwell_y(E, npts=40):
    """E = x e^{a y} cos(wt + b y), H = z (1/|eta|) e^{a y} cos(wt + b y - tau) for y < 0 (downward wave).
    Faraday: curl(x Ex(y)) = -z dEx/dy = -mu dHz/dt z.  Ampere: curl(z Hz(y)) = x dHz/dy = sigma Ex + eps dEx/dt."""
    a, b, ae, ta, w, mu, eps, sig = E["a"], E["b"], E["aeta"], E["tau"], E["w"], E["mu"], E["eps"], E["sig"]
    Exf = lambda y, t: np.exp(a * y) * np.cos(w * t + b * y)
    Hzf = lambda y, t: np.exp(a * y) * np.cos(w * t + b * y - ta) / ae
    hy, ht = 1e-5 / b, 1e-5 / w
    rf = ra = 0.0
    for _ in range(npts):
        y = -rng.uniform(0, 60)
        t = rng.uniform(0, 2 * PI / w)
        dEy = (Exf(y + hy, t) - Exf(y - hy, t)) / (2 * hy)
        dHt = (Hzf(y, t + ht) - Hzf(y, t - ht)) / (2 * ht)
        dHy = (Hzf(y + hy, t) - Hzf(y - hy, t)) / (2 * hy)
        dEt = (Exf(y, t + ht) - Exf(y, t - ht)) / (2 * ht)
        env = np.exp(a * y)
        rf = max(rf, abs(-dEy + mu * dHt) / (abs(a + 1j * b) * env))
        ra = max(ra, abs(dHy - sig * Exf(y, t) - eps * dEt) / (abs(sig + 1j * w * eps) * env))
    return rf, ra


rf, ra = fd_maxwell_y(Pe)
claim("(c) E = x e^{ay} cos(wt+by), H = z (1/|eta|) e^{ay} cos(wt+by-tau) satisfy Faraday and Ampere (exact params)",
      rf < 1e-6 and ra < 1e-6, f"{rf:.1e}, {ra:.1e}")
Pa = dict(Pe)
Pa.update(a=Pg["a"], b=Pg["b"], aeta=Pg["aeta"], tau=PI / 4)
rf, ra = fd_maxwell_y(Pa)
claim("(c) the answer's GC numbers satisfy Maxwell to O(1/p) = 0.6 %", rf < 1e-6 and ra < 0.01, f"{rf:.1e}, {ra:.1e}")
# phasor check of the curl directly (complex): curl(x E(y)) = -z dE/dy; set = -j w mu H
yv = -7.3
Ey = lambda y: np.exp(Pe["g"] * y)
dEy = (Ey(yv + 1e-6) - Ey(yv - 1e-6)) / 2e-6
Hz_ph = Ey(yv) / Pe["eta"]
close("(c) phasor Faraday: -dE/dy = -j w mu H_z with H_z = E/eta (+z)", -dEy, -1j * Pe["w"] * MU0 * Hz_ph, rtol=1e-6)
# (d)
Sd = 0.5 * np.real(np.cross([1, 0, 0], [0, 0, 1]) * (1 / np.conj(Pg["eta"])))
close("(d) 1/2 Re{E x H*} at y=0 = -y cos(tau)/(2|eta|) = -y/(8 pi)", Sd, np.array([0, -1 / (8 * PI), 0]))
Sq = tavg(lambda t: np.cos(2 * PI * fp * t) * np.cos(2 * PI * fp * t - PI / 4) / Pg["aeta"], 2 * PI * fp)
close("(d) quadrature <E_x H_z> at the surface = 1/(8 pi)", Sq, 1 / (8 * PI))
agree("(d) surface [mW/m^2]", 1 / (8 * PI), "39.8", scale=1e-3)
close("(d) e^{2 alpha (-25)} = e^{-pi}", np.exp(-2 * Pg["a"] * 25), np.exp(-PI))
agree("(d) factor at 25 m", np.exp(-PI), "0.043")
agree("(d) <S> at 25 m [mW/m^2]", np.exp(-PI) / (8 * PI), "1.72", scale=1e-3)
agree("(d) power left at 25 m [%]", 100 * np.exp(-PI), "4.3")
agree("(d) dB/m", NP2DB * Pg["a"], "0.546")
agree("(d) dB at 25 m", NP2DB * Pg["a"] * 25, "13.6")
agree("(d) 10 log10 e^pi", 10 * np.log10(np.exp(PI)), "13.6")
agree("(d) depth for 1 % [m]", np.log(100) / (2 * Pg["a"]), "36.6")
agree("(d) ln 100", np.log(100), "4.605")
agree("(d) 2 alpha", 2 * Pg["a"], "0.1257")
agree("(d) 20 dB / 0.546 dB/m [m]", 20 / 0.546, "36.6")
close("(d) field at 1 %-power depth is 10 %", np.exp(-Pg["a"] * np.log(100) / (2 * Pg["a"])), 0.1)
J = 0.5 * sp * (1 - np.exp(-PI)) / (2 * Pg["a"])
ss = np.linspace(0, 25, 200001)
Jq = np.trapezoid(0.5 * sp * np.exp(-2 * Pg["a"] * ss), ss) if hasattr(np, "trapezoid") else np.trapz(0.5 * sp * np.exp(-2 * Pg["a"] * ss), ss)
close("(d) Joule integral closed form = quadrature", J, Jq, rtol=1e-8)
agree("(d) Joule heat 0-25 m [mW/m^2]", J, "38.1", scale=1e-3)
close("(d) Joule heat = <S>(0) - <S>(25 m) exactly (GC model)", J, (1 - np.exp(-PI)) / (8 * PI))
agree("(d) 0.005*0.957/0.1257 [mW/m^2]", 0.005 * 0.957 / 0.1257, "38.1", scale=1e-3)
# (e)
amax = 0.4 / NP2DB
agree("(e) alpha max [Np/m]", amax, "0.0461")
fe = amax ** 2 / (PI * MU0 * sp)
agree("(e) f max [kHz]", fe, "53.7", scale=1e3)
agree("(e) (40/54.6)^2", (40 / 20 / np.log10(np.exp(2 * PI))) ** 2, "0.537")
close("(e) both routes agree", fe, 1e5 * (40 / (20 * np.log10(np.exp(2 * PI)))) ** 2, rtol=1e-12)
agree("(e) sigma/(w eps) at f max (course)", 180 * 1e5 / fe, "335")
agree("(e) exact loss at 100 m [dB]", NP2DB * exact(fe, sp, erp)["a"] * 100, "39.9")
agree("(e) lambda0 at 100 kHz [km]", 3e8 / 1e5 / 1e3, "3.0")
agree("(e) lambda0 at f max [km]", 3e8 / fe / 1e3, "5.6")
# variant 10 MHz
V = exact(1e7, sp, erp)
agree("variant sigma/(w eps)", V["p"], "1.8")
agree("variant theta [deg]", np.degrees(np.arctan(V["p"])), "60.9")
agree("variant tau [deg]", np.degrees(V["tau"]), "30.5")
agree("variant |eta| [ohm]", V["aeta"], "83.1")
agree("variant alpha [Np/m]", V["a"], "0.482")
agree("variant dB/m (page had 4.19: double rounding, fixed)", NP2DB * V["a"], "4.18")
agree("variant beta [rad/m]", V["b"], "0.819")
agree("variant GC alpha [Np/m]", gc(1e7, sp)["a"], "0.628")
agree("variant GC too high by [%]", 100 * (gc(1e7, sp)["a"] / V["a"] - 1), "30")
aid = sp / 2 * np.sqrt(MU0 / (erp * EPS0))
agree("variant ID alpha [Np/m]", aid, "0.596")
agree("variant ID too high by [%]", 100 * (aid / V["a"] - 1), "24")
agree("variant alpha/beta = tan(30.5 deg)", V["a"] / V["b"], "0.59")
rf, ra = fd_maxwell_y(V)
claim("variant fields satisfy Maxwell (exact params)", rf < 1e-6 and ra < 1e-6)

# ======================================================================================== K
sec("K  Concept pages: loss tangent, skin depth, Lorentz-Drude 'at high frequency'")
# loss angle geometry
for p in (0.01, 0.7, 3.0, 400.0):
    Ic, Id = p, 1j  # conduction and displacement current per (w eps E), E real
    It = Ic + Id
    lead = np.angle(Id) - np.angle(It)
    close(f"displacement current leads total current by theta = arctan(p) (p={p:g})", lead, np.arctan(p))
    close(f"  total current at 90 deg - theta from E", np.angle(It), PI / 2 - np.arctan(p))
# 1/Q: energy lost per radian / peak stored electric energy
s_, e_, w_, Eamp = 0.03, 7 * EPS0, 2 * PI * 3e8, 2.0
loss_per_rad = tavg(lambda t: s_ * (Eamp * np.cos(w_ * t)) ** 2, w_) / w_
close("loss per radian / peak stored electric energy = sigma/(w eps) = 1/Q of G||C", loss_per_rad / (0.5 * e_ * Eamp ** 2), s_ / (w_ * e_))
close("|gamma| = w sqrt(mu eps)(1+p^2)^1/4", abs(exact(3e8, 0.03, 7)["g"]),
      w_ * np.sqrt(MU0 * 7 * EPS0) * (1 + (0.03 / (w_ * 7 * EPS0)) ** 2) ** 0.25)
# examples
agree("fresh water at 1 MHz", exact(1e6, 1e-3, 80)["p"], "0.22")
agree("copper at 1 GHz [1e9]", exact(1e9, 5.8e7, 1)["p"], "1.0", scale=1e9)
agree("Ex1 medium angle(eta) [deg]", np.degrees(exact(1e9, 1e-3, 4)["tau"]), "0.13")
agree("exam dry earth (1e-3 S/m, eps0) at 1 kHz [1e4] (re-parameterized in review from 100 Hz)",
      18e9 * 1e-3 / (1e3 * 1), "1.8", scale=1e4)
claim("datasheet tan delta = (sigma + w eps'')/(w eps') equals Im/Re of the total admittance",
      np.isclose(((0.01 + 1j * 2e8 * (5e-11 - 1j * 2e-12)) / 1j).imag * -1 / (2e8 * 5e-11), (0.01 + 2e8 * 2e-12) / (2e8 * 5e-11)))
# skin depth page
agree("seawater delta at 60 Hz [m]", gc(60, 4)["d"], "32.5")
agree("seawater delta at 1 MHz [cm]", 100 * gc(1e6, 4)["d"], "25")
agree("seawater delta*sqrt(f)", 1 / np.sqrt(PI * MU0 * 4), "252")
agree("power absorbed within delta [%]", 100 * (1 - np.exp(-2)), "86")
agree("power absorbed within 3 delta [%]", 100 * (1 - np.exp(-6)), "99.75")
close("magnetic metal: delta scales as 1/sqrt(mu_r)", gc(1e3, 1e7, 100)["d"] / gc(1e3, 1e7)["d"], 0.1)
close("four times the frequency halves delta", gc(4e3, 1e7)["d"] / gc(1e3, 1e7)["d"], 0.5)
agree("seawater 1 GHz GC formula [cm]", 100 * gc(1e9, 4)["d"], "0.8")
agree("power at z = delta [%]", 100 * np.exp(-2), "14")
agree("field at z = delta [%]", 100 * np.exp(-1), "37")
agree("moist soil 100 kHz delta [m]", gc(1e5, 1e-2)["d"], "15.9")
close("mixing f and w in delta: error factor sqrt(2 pi)", np.sqrt(2 / (2 * PI * 1e3 * MU0 * 4)) / np.sqrt(2 / (1e3 * MU0 * 4)),
      1 / np.sqrt(2 * PI))
# Lorentz-Drude page section
agree("L-D page: seawater f_c [GHz]", fc(4, 81) / 1e9, "0.89")
agree("L-D page: fresh water f_c [kHz]", fc(1e-3, 80) / 1e3, "225")
agree("L-D page: copper 1 MHz delta [um]", gc(1e6, 5.8e7)["d"], "66", scale=1e-6)
claim("L-D page: 'well above f_c ... weakens the wave only a little per wavelength' (seawater 100 GHz: e^{-alpha lambda})",
      np.exp(-exact(1e11, 4, 81)["a"] * 2 * PI / exact(1e11, 4, 81)["b"]) > 0.9)
claim("L-D page: but not 'slowly' per metre: seawater above 10 f_c still loses 84 Np/m (727 dB/m)",
      NP2DB * exact(1e11, 4, 81)["a"] > 700)

# ======================================================================================== L
sec("L  Figures: plotted annotations and arrow directions")
agree("fig regime map: f_c labels seawater [GHz]", fc(4, 81) / 1e9, "0.89")
claim("fig regime map: Bakelite's dielectric band starts at 37 Hz ('above a few tens of hertz')", 30 < 10 * fc(1e-9, 4.9) < 40)
claim("fig regime map: at 5 Hz Bakelite is in between (0.1 < p < 10)", 0.1 < exact(5, 1e-9, 4.9)["p"] < 10)
agree("fig seawater: 1 kHz alpha = pi/25", exact(1e3, 4, 81)["a"], "0.126")
agree("fig seawater: 1 GHz alpha", exact(1e9, 4, 81)["a"], "77")
agree("fig seawater: plateau", plat, "84")
agree("fig seawater: sqrt(mu/eps) = eta0/9 [ohm]", ETA0 / 9, "42")
agree("fig seawater: alpha(1 GHz)/alpha(1 kHz) ('about 600')", exact(1e9, 4, 81)["a"] / exact(1e3, 4, 81)["a"], "600", sf=1)
agree("fig seawater: tau at f_c [deg]", np.degrees(exact(fc(4, 81), 4, 81)["tau"]), "22.5")
agree("fig seawater: |eta| at 1 kHz [ohm] (label after review)", exact(1e3, 4, 81)["aeta"], "0.044")
claim("fig seawater: |eta| < sqrt(mu/eps)/3 throughout the GC band (below f_c/10)", exact(fc(4, 81) / 10, 4, 81)["aeta"] < ETA0 / 9 / 3,
      f"{exact(fc(4, 81) / 10, 4, 81)['aeta']:.1f} ohm at 89 MHz")
agree("fig good conductor: e^{-2} [%]", 100 * np.exp(-2), "14")
agree("fig good conductor: two wavelengths [dB] (still nonzero: 'effectively gone')", 2 * 20 * np.log10(np.exp(2 * PI)), "109")
# screen frame for the icon: physics z = X (right), physics x = Y (up) -> physics y = z x x = X x Y = Z (out)
X, Y, Z = np.eye(3)
claim("fig icon: physics y = z x x maps to X x Y = Z (out of screen: odot)", np.allclose(np.cross(X, Y), Z))
claim("fig icon: E (Y) x H (Z) = X (right, into the conductor)", np.allclose(np.cross(Y, Z), X))
claim("fig icon: H = cos(-pi/4) > 0 when E is at its maximum, so E up and H out drawn together is consistent", np.cos(-PI / 4) > 0)
agree("fig skin depth: Cu 60 Hz [mm]", gc(60, 5.8e7)["d"] * 1e3, "8.5")
agree("fig skin depth: Al 60 Hz [mm]", gc(60, 3.5e7)["d"] * 1e3, "11")
agree("fig skin depth: seawater 76 Hz delta [m]", 1 / exact(76, 4, 81)["a"], "29")
agree("fig skin depth: 76 Hz 100 dB [m]", d76, "330", sf=2)
agree("fig skin depth: 24 kHz delta [m]", 1 / exact(24e3, 4, 81)["a"], "1.6")
agree("fig skin depth: seawater delta levels off [cm]", 100 / exact(1e11, 4, 81)["a"], "1.2")
agree("fig problem: 100 kHz slope label = the problem's GC answer 0.546 rounded [dB/m]", NP2DB * gc(1e5, sp)["a"], "0.55")
claim("fig problem: exact 100 kHz slope 0.544 dB/m differs from the GC 0.546 by 0.3 % (invisible on the plot)",
      abs(exact(1e5, sp, erp)["a"] / gc(1e5, sp)["a"] - 1) < 0.003)
agree("fig problem: 53.7 kHz slope [dB/m]", NP2DB * exact(5.3718e4, sp, erp)["a"], "0.40")
agree("fig problem: 10 MHz slope [dB/m]", NP2DB * exact(1e7, sp, erp)["a"], "4.2")
agree("fig problem: point A level [dB]", NP2DB * exact(1e5, sp, erp)["a"] * 25, "13.6")
claim("fig problem: point B at 36.6 m is at 20.0 dB on the exact line (plotted at -20)", abs(NP2DB * exact(1e5, sp, erp)["a"] * 36.65 - 20) < 0.1)
claim("fig problem: point C (100 m, 40 dB) on the 53.7 kHz exact line", abs(NP2DB * exact(5.3718e4, sp, erp)["a"] * 100 - 40) < 0.1)
src = open(FIGMOD, encoding="utf-8").read()
claim("fig module: no 'small fraction of an ohm' left (finding Z4 fixed)", "small fraction of an ohm" not in src)
claim("fig module: problem figure's axis no longer says 'loss [dB]' for negative values (Z5)", '"loss [dB]"' not in src)

# ======================================================================================== M
sec("M  Exam keys: no carry-over (keys read from the scans in sources/img)")
prob = open(PROB, encoding="utf-8").read()
page = open(PAGE, encoding="utf-8").read()
clt = open(CLT, encoding="utf-8").read()
# S18/S19 HE3 #3b key: delta = 25/pi m, lambda = 50 m, v_p = 50 km/s, 0.081 W/m^2 at z = -10 m
keys18 = [25 / PI, 50.0, 5e4, np.exp(-0.8 * PI)]
mine = [Pg["d"], 2 * PI * Pg["d"], 2 * PI * Pg["d"] * fp, np.exp(-PI)]
claim("worked problem: delta, lambda, v_p, power ratio all differ from the S18/S19 HE3 #3b key",
      all(abs(m / k - 1) > 0.05 for m, k in zip(mine, keys18)))
claim("worked problem changes medium, frequency and direction (soil, 100 kHz, -y) vs seawater, 1 kHz, -z",
      (sp, erp, fp) != (4, 81, 1e3))
# S17 HE3 #2b key: v = 2e8, eps_r = 9/4, |eta| = 80 pi, sigma = 1e-3/(4 pi)
keys17 = [2e8, 9 / 4, 80 * PI, 1e-3 / (4 * PI)]
mine17 = [1e8, 9.0, 40 * PI, 0.1 / (40 * PI)]
claim("inverse example: v, eps_r, |eta|, sigma all differ from the S17 HE3 #2b key",
      all(abs(m / k - 1) > 0.05 for m, k in zip(mine17, keys17)))
# S20 HE3 #3 key: 0.18 at 100 MHz, 18e4 at 100 Hz, lambda = 1e4 m, delta = 1e4/(2 pi) m
claim("loss-tangent page no longer quotes the S20 HE3 #3(c) key step 1.8e5 at 100 Hz",
      "1.8\\times10^{5}" not in clt and "18\\times10^{4}" not in clt)
claim("no page states the S20 HE3 #3 lambda = 1e4 m or delta = 1e4/2pi m",
      all("10^{4}\\ \\text{m}" not in t and "10^4/2" not in t for t in (page, clt, prob)))
# FA23 #6 key: 0.4 /m, 1.737 dB/m
claim("no page states the FA23 #6 key numbers (1.737 dB/m, 0.4 per metre)",
      all("1.737" not in t and "1.74" not in t for t in (page, clt, prob)))
# S19 conflict #3b(ii) key: w eps >> sigma
claim("On exams callout no longer states the S19 conflict inequality (omega > 10 sigma/eps)",
      "\\omega>10\\sigma/\\epsilon" not in page)
claim("On exams callout no longer quotes the S20 dry-earth f_c number", "medium's $f_c = 18$ MHz" not in page)

# ======================================================================================== N
sec("N  Notation and formatting scan (site rules)")
FILES = {"lecture": PAGE, "loss-tangent": CLT, "skin-depth": CSD, "L-D concept": CCS, "problem": PROB}
for nm, fpth in FILES.items():
    t = open(fpth, encoding="utf-8").read()
    maths = re.findall(r"\$\$(.+?)\$\$|\$([^$\n]+?)\$", t, flags=re.S)
    flat = [a or b for a, b in maths]
    claim(f"{nm}: no \\varepsilon / \\vec", "\\varepsilon" not in t and "\\vec" not in t)
    bad = [m for m in flat if re.search(r"[^\x00-\x7f]", m.replace("✓", ""))]
    claim(f"{nm}: no unicode inside $...$", not bad, f"{bad[:2]}" if bad else "")
    lines = t.split("\n")
    inside, broken = False, []
    for i, ln in enumerate(lines):
        if ln.startswith("> [!"):
            inside = True
        elif inside and ln.strip() == "":
            inside = False
        elif inside and not ln.startswith(">"):
            broken.append(i + 1)
    claim(f"{nm}: every callout line starts with '>'", not broken, f"lines {broken[:5]}")
    claim(f"{nm}: no '\\begin{{align}}'", "\\begin{align}" not in t)
claim("lecture: header says slides not available", "slides: not yet available" in page)
claim("lecture: front matter lecture: 23 and tags", "lecture: 23" in page and "tags: [lecture, waves]" in page)
l22 = open(L22, encoding="utf-8").read()
claim("L22 consistency: tau = (1/2) tan^-1(sigma/w eps) in both pages",
      "\\tau = \\frac12\\tan^{-1}\\frac{\\sigma}{\\omega\\epsilon}" in l22 and "\\frac12\\tan^{-1}\\frac{\\sigma}{\\omega\\epsilon}" in page)
claim("L22 consistency: L22 defers the power bookkeeping to L23, which has it (cos tau, e^-2az)",
      "Lecture 23 does that bookkeeping" in l22 and "e^{-2\\alpha z}" in page)

# ======================================================================================== Z
sec("Z  Findings in the original text, demonstrated (all fixed in the page set)")
# Z1 sign of the energy-balance sentence
divS_sign = -1  # div<S> = -<J.E> < 0 in a lossy medium
claim("Z1 'power flowing OUT of a small volume equals the power delivered' is false: net outflow = -<J.E> < 0",
      divS_sign * JE < 0)
# Z2 accuracy sentence: tau error 0.33 % is not 'within 0.3 %'; beta 0.124 % rounds to 0.12 %
a, b, e, t = errs(0.1)
claim("Z2 at p = 0.1 the tau error (0.332 %) exceeds 0.3 %, beta's (0.124 %) rounds to 0.12 %",
      0.05 / t - 1 > 0.003 and round(100 * abs(1 / b - 1), 2) == 0.12)
# Z3 'between 0.1 and 10 neither set is accurate' is too strong on the dielectric side
claim("Z3 at p = 0.3 the imperfect-dielectric alpha is still within 1.1 %", 0.15 / errs(0.3)[0] - 1 < 0.011)
# Z4 seawater figure: |eta| is not 'a small fraction of an ohm' across the good-conductor band
claim("Z4 seawater |eta| reaches 1.4 ohm at 1 MHz and 13 ohm at 89 MHz (GC band)",
      exact(1e6, 4, 81)["aeta"] > 1 and exact(fc(4, 81) / 10, 4, 81)["aeta"] > 10)
# Z5 problem figure plots negative values on an axis called 'loss'
claim("Z5 the plotted values are -8.686 alpha d < 0, so the axis is a level, not a loss", -NP2DB * Pg["a"] * 25 < 0)
# Z6 'for metals it is milliohms': copper 60 Hz |eta| is microohms
claim("Z6 copper |eta| at 60 Hz is 2.9 micro-ohm, not milliohms", gc(60, 5.8e7)["aeta"] < 1e-5)
# Z7 Bakelite 'insulator above a few hertz': in between at 5 Hz
claim("Z7 Bakelite at 5 Hz has sigma/(w eps) = 0.73: in between, not yet a dielectric", 0.1 < exact(5, 1e-9, 4.9)["p"] < 10)
# Z8 the table's approximate entries had '=': exact alpha differs from the shortcut
claim("Z8 table entries are limits, not identities (p = 0.05: ID alpha off by 0.03 %; p = 50: GC alpha off by 1 %)",
      0.025 / errs(0.05)[0] - 1 > 1e-4 and np.sqrt(25) / errs(50.0)[0] - 1 > 0.009)
# Z9 concept page: 'for large p, alpha = beta' is approximate
claim("Z9 alpha/beta = tan(tau) < 1 at any finite p (p = 1e4: 0.99990)", errs(1e4)[0] / errs(1e4)[1] < 1)
# Z10 skin-depth page 'soak in' vs L22's 'soak into' (diffusion): wording conflict
claim("Z10 L22 uses 'soak into a good conductor' for diffusion; skin-depth page no longer says 'cannot simply soak in'",
      "soak into a good conductor" in l22 and "cannot simply soak in" not in open(CSD, encoding="utf-8").read())

print(f"\nSUMMARY: {NPASS} PASS, {NFAIL} FAIL")
