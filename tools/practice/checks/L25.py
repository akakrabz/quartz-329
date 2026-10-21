#!/usr/bin/env python3
"""L25 practice checks: reflection and transmission at normal incidence (numpy + scipy only).

Every number, sign and direction on practice/25-reflection-and-transmission.md is printed here.
Gamma and tau are found twice: from the formula (eta2 - eta1)/(eta2 + eta1), 1 + Gamma, and by
solving the 2x2 tangential-E / tangential-H boundary system numerically. Every phasor field is
built from H = u x E / eta with np.cross, checked against the phasor Maxwell curl equations by
finite differences, checked for continuity of tangential E and H at the interface, and its
time-average Poynting vector is checked by quadrature of the real fields over one period.
Handedness uses the L24 recipe u . [E(0) x E(T/4)] (>0 right, <0 left) and a brute-force
rotation test. Course constants eps0 = 1e-9/36pi (so c = 3e8, eta0 = 120pi) where the page says so.
"""
import numpy as np
from scipy import integrate

mu0 = 4e-7 * np.pi
eps0 = 8.8541878128e-12
eps0C = 1e-9 / (36 * np.pi)
cC = 1 / np.sqrt(mu0 * eps0C)
eta0 = np.sqrt(mu0 / eps0C)          # 120 pi exactly
X, Y, Z = np.eye(3)
ALL = []


def hdr(s):
    print("\n" + "=" * 78 + "\n" + s + "\n" + "=" * 78)


def check(label, cond):
    print(f"  [{label}] {'OK' if cond else 'FAIL'}")
    ALL.append(bool(cond))


def close(label, a, b, rtol=1e-6, atol=1e-12):
    ok = np.allclose(a, b, rtol=rtol, atol=atol)
    print(f"  [{label}] {np.round(a, 10)!r} vs {np.round(b, 10)!r} -> {'OK' if ok else 'FAIL'}")
    ALL.append(bool(ok))


def medium(w, mur=1.0, er=1.0, sig=0.0, e0=eps0C):
    mu, eps = mur * mu0, er * e0
    g = np.sqrt(1j * w * mu * (sig + 1j * w * eps))
    eta = np.sqrt(1j * w * mu / (sig + 1j * w * eps))
    if g.real < 0:
        g = -g
    return dict(mu=mu, eps=eps, sig=sig, g=g, eta=eta)


def gamma_tau(eta1, eta2):
    G = (eta2 - eta1) / (eta2 + eta1)
    return G, 1 + G


def gamma_tau_bc(eta1, eta2):
    # unknowns (G, t): 1 + G = t ; (1 - G)/eta1 = t/eta2
    A = np.array([[1, -1], [-1 / eta1, -1 / eta2]], dtype=complex)
    b = np.array([-1, -1 / eta1], dtype=complex)
    return np.linalg.solve(A, b)


class Wave:
    """Plane-wave phasor E = E0 exp(-gamma u.(r - r0)), H = u x E / eta."""
    def __init__(self, E0, u, g, eta, r0=np.zeros(3)):
        self.E0, self.u, self.g, self.eta, self.r0 = np.array(E0, complex), np.array(u, float), g, eta, r0

    def E(self, r):
        return self.E0 * np.exp(-self.g * np.dot(self.u, np.asarray(r) - self.r0))

    def H(self, r):
        return np.cross(self.u, self.E(r)) / self.eta

    def S(self, r):
        return 0.5 * np.real(np.cross(self.E(r), np.conj(self.H(r))))


def curl(F, r, h=1e-6):
    r = np.asarray(r, float)
    J = np.zeros((3, 3), complex)
    for k in range(3):
        d = np.zeros(3); d[k] = h
        J[:, k] = (F(r + d) - F(r - d)) / (2 * h)
    return np.array([J[2, 1] - J[1, 2], J[0, 2] - J[2, 0], J[1, 0] - J[0, 1]])


def maxwell(label, waves, med, w, r):
    Ef = lambda q: sum(wv.E(q) for wv in waves)
    Hf = lambda q: sum(wv.H(q) for wv in waves)
    lhs1, rhs1 = curl(Ef, r), -1j * w * med["mu"] * Hf(r)
    lhs2, rhs2 = curl(Hf, r), (med["sig"] + 1j * w * med["eps"]) * Ef(r)
    s1 = max(np.abs(rhs1).max(), 1e-30); s2 = max(np.abs(rhs2).max(), 1e-30)
    ok = np.abs(lhs1 - rhs1).max() / s1 < 1e-5 and np.abs(lhs2 - rhs2).max() / s2 < 1e-5
    check(f"{label}: curl E = -jw mu H, curl H = (sig + jw eps) E", ok)


def tavg_S(waves, r, w):
    """Time-average Poynting vector by quadrature of real fields over one period."""
    T = 2 * np.pi / w
    E = sum(wv.E(r) for wv in waves); H = sum(wv.H(r) for wv in waves)
    out = []
    for k in range(3):
        f = lambda t: np.cross(np.real(E * np.exp(1j * w * t)), np.real(H * np.exp(1j * w * t)))[k]
        out.append(integrate.quad(f, 0, T, limit=200)[0] / T)
    return np.array(out)


def hand(Eph, u):
    """L24 recipe: u . [E(0) x E(T/4)], with E(0) = Re E, E(T/4) = Re{jE}."""
    v = np.dot(u, np.cross(np.real(Eph), np.real(1j * Eph)))
    return "right" if v > 1e-12 else ("left" if v < -1e-12 else "linear")


def hand_brute(Eph, u, n=400):
    """Accumulate the signed rotation angle of E(t) about u over one period."""
    ts = np.linspace(0, 2 * np.pi, n + 1)
    vs = [np.real(Eph * np.exp(1j * t)) for t in ts]
    ang = 0.0
    for a, b in zip(vs[:-1], vs[1:]):
        ang += np.arctan2(np.dot(u, np.cross(a, b)), np.dot(a, b))
    return "right" if ang > 1 else ("left" if ang < -1 else "linear")


def pct(x):
    return f"{100 * x:.4g} %"


# ============================================================================
hdr("25.1 Four interfaces")
cases = [("(a) air -> er=4", eta0, eta0 / 2),
         ("(b) er=4 -> air", eta0 / 2, eta0),
         ("(c) air -> mur=16, er=4", eta0, eta0 * np.sqrt(16 / 4)),
         ("(d) air -> PEC", eta0, 0.0)]
expect = {"(a)": (-1 / 3, 2 / 3), "(b)": (1 / 3, 4 / 3), "(c)": (1 / 3, 4 / 3), "(d)": (-1, 0)}
for name, e1, e2 in cases:
    G, t = gamma_tau(e1, e2)
    print(f"  {name}: eta1 = {e1/np.pi:.4g} pi, eta2 = {e2/np.pi:.4g} pi, Gamma = {G:.6f}, tau = {t:.6f}, "
          f"reflected {pct(G**2)}, transmitted {pct(1 - G**2)}")
    close(f"{name[:3]} Gamma, tau", (G, t), expect[name[:3]])
    if e2 > 0:
        close(f"{name[:3]} power balance G^2 + t^2 e1/e2 = 1", G**2 + t**2 * e1 / e2, 1.0)
    close(f"{name[:3]} BC solve agrees", gamma_tau_bc(e1, e2) if e2 > 0 else np.array([G, t]), (G, t))
print("  (a) and (b): same |Gamma|, opposite sign; (b) and (c) identical Gamma since eta2/eta1 = 2 in both")

# ============================================================================
hdr("25.2 True or false")
# (i) eta2 < eta1 -> Gamma < 0 -> E_r(0) opposite E_i(0)
for e1, e2 in [(eta0, eta0 / 3), (eta0 / 2, eta0 / 5)]:
    G, t = gamma_tau(e1, e2)
    check(f"(i) eta2<eta1: Gamma = {G:.4f} < 0 (E_r inverted)", G < 0)
    # (ii) H_r/H_i at z=0 = -Gamma > 0: same direction
    w = 1.0
    inc = Wave(E0=X, u=Z, g=1j, eta=e1); ref = Wave(E0=G * X, u=-Z, g=1j, eta=e1)
    Hi, Hr = inc.H(np.zeros(3)), ref.H(np.zeros(3))
    print(f"     H_i(0) = {np.round(Hi*e1, 6)}/eta1, H_r(0) = {np.round(Hr*e1, 6)}/eta1, ratio = {Hr[1]/Hi[1]:.4f} = -Gamma")
    check("(ii) reflected H along incident H (statement false)", np.dot(np.real(Hi), np.real(Hr)) > 0)
# (iii) tau = 4/3 from eta2 = 2 eta1: fraction transmitted 8/9 < 1
G, t = gamma_tau(1.0, 2.0)
print(f"  (iii) eta2 = 2 eta1: tau = {t:.6f}, transmitted fraction tau^2 eta1/eta2 = {t**2/2:.6f} = 1 - Gamma^2 = {1-G**2:.6f}")
check("(iii) transmitted power < incident (statement false)", t**2 / 2 < 1)
# (iv) total tangential E continuous at every instant: (1+G) = tau as phasors -> real fields equal at all t
G, t = gamma_tau(eta0, eta0 / 2)
ts = np.linspace(0, 2 * np.pi, 7)
check("(iv) Re{(1+G)e^{jwt}} = Re{tau e^{jwt}} for all t", np.allclose(np.real((1 + G) * np.exp(1j * ts)), np.real(t * np.exp(1j * ts))))
# (v) mur = er = 3: eta = eta0, v = c/3
G, t = gamma_tau(eta0, eta0 * np.sqrt(3 / 3))
print(f"  (v) mur = er = 3: eta2 = {eta0*np.sqrt(3/3)/np.pi:.4g} pi, Gamma = {G}, v = c/{np.sqrt(9):.4g}")
check("(v) Gamma = 0 (statement true)", abs(G) < 1e-15)

# ============================================================================
hdr("25.3 Free space onto a good conductor (multiple choice)")
for w in [1e6, 2 * np.pi * 1e9]:          # answer independent of w: sigma given as 3600 w eps0
    m2 = medium(w, er=9, sig=3600 * w * eps0C)
    G, t = gamma_tau(eta0, m2["eta"])
    print(f"  w = {w:.3g}: sigma/(w eps) = {m2['sig']/(w*m2['eps']):.4g}, eta2 = {m2['eta']:.5f} Ohm "
          f"= {abs(m2['eta']):.5f} angle {np.degrees(np.angle(m2['eta'])):.4f} deg; |eta2|/eta0 = 1/{eta0/abs(m2['eta']):.4f}")
    print(f"     Gamma = {G:.5f}, |Gamma| = {abs(G):.5f}, reflected {pct(abs(G)**2)}")
    check("     Gamma close to -1 (option d)", abs(G + 1) < 0.04)
Gl, _ = gamma_tau(eta0, eta0 / 3)
print(f"  distractor (b): ignore sigma, eta2 = eta0/3 -> Gamma = {Gl:.6f}")
close("(b) value -1/2", Gl, -0.5)
G_out, _ = gamma_tau(m2["eta"], eta0)
print(f"  distractor (e): leaving the conductor into air gives Gamma = {G_out:.5f} (close to +1)")
print(f"  |eta2| = eta0/60 approx: eta0/60 = {eta0/60:.4f} = 2 pi = {2*np.pi:.4f}")
G_approx = -1 + 2 * m2["eta"] / eta0
print(f"  first-order Gamma = -1 + 2 eta2/eta0 = {G_approx:.5f}")

# ============================================================================
hdr("25.4 Find the error: air onto er = 16")
e1, e2 = eta0, eta0 / 4
Gs = (e1 - e2) / (e1 + e2); ts_ = 1 + Gs
G, t = gamma_tau(e1, e2)
print(f"  student: Gamma = {Gs:.4f}, tau = {ts_:.4f}, E_t(0) = {5*ts_:.4f} V/m; power sum G^2 + t^2 e1/e2 = {Gs**2 + ts_**2*e1/e2:.4f}")
print(f"  correct: Gamma = {G:.4f}, tau = {t:.4f}, E_r(0) = {5*G:.4f} V/m, E_t(0) = {5*t:.4f} V/m; "
      f"power sum = {G**2 + t**2*e1/e2:.6f}")
close("correct Gamma, tau", (G, t), (-0.6, 0.4))
close("BC solve", gamma_tau_bc(e1, e2), (G, t))
print(f"  beta2/beta1 = sqrt(16) = {np.sqrt(16):.4g}; reflected {pct(G**2)}, transmitted {pct(1-G**2)}")

# ============================================================================
hdr("25.5 Permittivity from a measured Gamma")
G = -0.5
r = (1 + G) / (1 - G)                     # eta2/eta1
er = (1 / r) ** 2
print(f"  Gamma = -1/2 -> eta2/eta1 = {r:.6f}, n = {1/r:.6f}, er = {er:.6f}; transmitted {pct(1-G**2)}")
close("er = 9", er, 9.0)
G2, t2 = gamma_tau(eta0, eta0 / 3)
close("forward check Gamma(er=9) = -1/2", G2, -0.5)
close("transmitted fraction t^2 eta1/eta2 = 0.75", t2**2 * 3, 0.75)
Gm, _ = gamma_tau(eta0, eta0 * np.sqrt(9 / 9))
close("mur = 9 with er = 9 gives Gamma = 0", Gm, 0.0)

# ============================================================================
hdr("25.6 Same speed, different impedance (glass er=4 z>0 onto mur=4 z<0, travel -z)")
f = 1e8; w = 2 * np.pi * f
m1 = medium(w, er=4); m2 = medium(w, mur=4)
b0 = w / cC
print(f"  beta0 = {b0:.6f} = {b0/np.pi:.6f} pi; beta1 = {m1['g'].imag/np.pi:.6f} pi, beta2 = {m2['g'].imag/np.pi:.6f} pi rad/m")
print(f"  eta1 = {m1['eta'].real/np.pi:.6f} pi, eta2 = {m2['eta'].real/np.pi:.6f} pi Ohm; v1 = v2 = {w/m1['g'].imag:.6g} m/s")
G, t = gamma_tau(m1["eta"], m2["eta"])
close("Gamma, tau = 0.6, 1.6", (G, t), (0.6, 1.6))
close("BC solve", gamma_tau_bc(m1["eta"], m2["eta"]), (G, t))
E0 = 10
inc = Wave(E0 * Y, -Z, m1["g"], m1["eta"])
ref = Wave(G * E0 * Y, Z, m1["g"], m1["eta"])
tra = Wave(t * E0 * Y, -Z, m2["g"], m2["eta"])
o = np.zeros(3)
for nm, wv, sc in [("H_i", inc, 6), ("H_r", ref, 10), ("H_t", tra, 15)]:
    Hv = wv.H(o)
    print(f"  {nm}(0) = {np.round(Hv.real, 8)} A/m; times {sc} pi = {np.round(Hv.real*sc*np.pi, 8)}")
close("H_i(0) = +x 1/(6pi)", inc.H(o), X / (6 * np.pi))
close("H_r(0) = -x 1/(10pi)", ref.H(o), -X / (10 * np.pi))
close("H_t(0) = +x 1/(15pi)", tra.H(o), X / (15 * np.pi))
close("E_r(0) = 6 y, E_t(0) = 16 y", (ref.E(o), tra.E(o)), (6 * Y, 16 * Y))
# exponent signs: E_r at z = 0.1 should be 6 exp(-j beta1 0.1)
close("E_r exponent e^{-j 4pi z/3}", ref.E(0.1 * Z)[1], 6 * np.exp(-1j * 4 * np.pi / 3 * 0.1))
close("E_t exponent e^{+j 4pi z/3}", tra.E(-0.1 * Z)[1], 16 * np.exp(1j * 4 * np.pi / 3 * (-0.1)))
maxwell("region 1 (i + r)", [inc, ref], m1, w, np.array([0.1, 0.2, 0.37]))
maxwell("region 2 (t)", [tra], m2, w, np.array([0.1, 0.2, -0.37]))
check("tangential E continuous at z=0", np.allclose(inc.E(o) + ref.E(o), tra.E(o)))
check("tangential H continuous at z=0", np.allclose(inc.H(o) + ref.H(o), tra.H(o)))
Si, Sr, St = inc.S(o), ref.S(o), tra.S(o)
print(f"  <S_i> = {np.round(Si, 6)}, <S_r> = {np.round(Sr, 6)}, <S_t> = {np.round(St, 6)} W/m^2")
print(f"  exact forms: 100/(120pi) = {100/(120*np.pi):.6f}, 36/(120pi) = {36/(120*np.pi):.6f}, 256/(480pi) = {256/(480*np.pi):.6f}")
close("quadrature <S_i>", tavg_S([inc], 0.3 * Z, w), Si, rtol=1e-6, atol=1e-9)
close("quadrature <S_t>", tavg_S([tra], -0.3 * Z, w), St, rtol=1e-6, atol=1e-9)
close("balance |Si| = |Sr| + |St|", abs(Si[2]), abs(Sr[2]) + abs(St[2]))
print(f"  reflected {pct(G**2)}, transmitted {pct(t**2*m1['eta'].real/m2['eta'].real)}")
check("E x H directions: inc -z, ref +z, tra -z", Si[2] < 0 and Sr[2] > 0 and St[2] < 0)

# ============================================================================
hdr("25.7 A mirror at y = 0 (PEC in y<0, wave in air travelling -y)")
f = 3e8; w = 2 * np.pi * f
b = w / cC
print(f"  beta = {b:.6f} = {b/np.pi:.6f} pi rad/m")
# E_i(y,t) = z 3 sin(wt + beta y) -> phasor -3j z e^{+j beta y}
inc = Wave(-3j * Z, -Y, 1j * b, eta0)
ref = Wave(+3j * Z, Y, 1j * b, eta0)     # Gamma = -1
o = np.zeros(3)
yy = 0.13
tt = np.linspace(0, 1 / f, 9)
Ei_t = [np.real(inc.E(yy * Y) * np.exp(1j * w * s)) for s in tt]
check("phasor of z 3 sin(wt + beta y)", np.allclose([e[2] for e in Ei_t], 3 * np.sin(w * tt + b * yy)))
print(f"  H_i(0) = {np.round(inc.H(o), 8)} ; 1/(40pi) = {1/(40*np.pi):.8f}")
close("H_i = x j/(40pi) e^{j2pi y}", inc.H(yy * Y), 1j * X / (40 * np.pi) * np.exp(1j * 2 * np.pi * yy))
close("H_r = x j/(40pi) e^{-j2pi y}", ref.H(yy * Y), 1j * X / (40 * np.pi) * np.exp(-1j * 2 * np.pi * yy))
Er_t = [np.real(ref.E(yy * Y) * np.exp(1j * w * s)) for s in tt]
check("E_r(y,t) = -z 3 sin(wt - 2pi y)", np.allclose([e[2] for e in Er_t], -3 * np.sin(w * tt - b * yy)))
Hr_t = [np.real(ref.H(yy * Y) * np.exp(1j * w * s)) for s in tt]
check("H_r(y,t) = -x (1/40pi) sin(wt - 2pi y)", np.allclose([h[0] for h in Hr_t], -np.sin(w * tt - b * yy) / (40 * np.pi)))
maxwell("air (i + r)", [inc, ref], medium(w), w, np.array([0.2, 0.31, -0.1]))
Etot0 = inc.E(o) + ref.E(o); Htot0 = inc.H(o) + ref.H(o)
print(f"  total at y=0: E = {Etot0}, H = {np.round(Htot0, 8)}; 1/(20pi) = {1/(20*np.pi):.8f} A/m")
close("total E(0) = 0", Etot0, np.zeros(3))
n = Y   # from PEC (y<0) into air
Js = np.cross(n, Htot0)
print(f"  J_s phasor = n x H = {np.round(Js, 8)} ; |J_s| = {abs(Js[2])*1e3:.5f} mA/m = 2*3/eta0 = {6/eta0*1e3:.5f} mA/m")
Js_t = [np.real(Js * np.exp(1j * w * s)) for s in tt]
check("J_s(t) = z (1/20pi) sin wt", np.allclose([j[2] for j in Js_t], np.sin(w * tt) / (20 * np.pi)))
check("J_s along incident E at y=0", np.allclose(Js, 2 * inc.E(o) / eta0))
print(f"  net <S> in air: {np.round(inc.S(0.2*Y) + ref.S(0.2*Y), 12)} (each wave {np.round(inc.S(o), 8)}, {np.round(ref.S(o), 8)})")

# ============================================================================
hdr("25.8 How good a mirror is copper (10 GHz)")
f = 1e10; w = 2 * np.pi * f; sig = 5.8e7
p = sig / (w * eps0C)
delta = 1 / np.sqrt(np.pi * f * mu0 * sig)
eta_gc = (1 + 1j) / (sig * delta)
m2 = medium(w, sig=sig)
print(f"  sigma/(w eps0) = {p:.4g}; delta = {delta*1e6:.5f} um; sigma delta = {sig*delta:.5f} S; 1/(sigma delta) = {1/(sig*delta):.6f} Ohm")
print(f"  eta2 (good conductor) = {eta_gc:.6f}; exact = {m2['eta']:.6f}")
close("good-conductor eta vs exact", eta_gc, m2["eta"], rtol=1e-6)
G, t = gamma_tau(eta0, m2["eta"])
absorbed = 1 - abs(G)**2
formula = 4 * eta0 * m2["eta"].real / abs(eta0 + m2["eta"])**2
approx = 4 * m2["eta"].real / eta0
print(f"  Gamma = {G.real:.6f} + j{G.imag:.3e}; |Gamma| = {abs(G):.8f}")
print(f"  1 - |Gamma|^2 = {absorbed:.5e}; 4 eta1 Re eta2/|eta1+eta2|^2 = {formula:.5e}; 4 Re eta2/eta1 = {approx:.5e}")
close("identity 1-|G|^2 = 4 e1 Re e2/|e1+e2|^2", absorbed, formula, rtol=1e-6)
close("approximation 4 Re eta2/eta0", approx, absorbed, rtol=1e-3)
close("power balance |t|^2 eta1 Re(1/eta2) = 1 - |G|^2", abs(t)**2 * eta0 * np.real(1 / m2["eta"]), absorbed, rtol=1e-6)
print(f"  of 100 W/m^2 incident: absorbed {100*absorbed*1e3:.4f} mW/m^2; reflected {100*abs(G)**2:.5f} W/m^2")
print(f"  percent absorbed = {100*absorbed:.4f} %")
# check identity with a random complex eta2 too
for e2 in [3 + 4j, 50 + 10j]:
    Gt, _ = gamma_tau(eta0, e2)
    close(f"identity with eta2 = {e2}", 1 - abs(Gt)**2, 4 * eta0 * e2.real / abs(eta0 + e2)**2)

# ============================================================================
hdr("25.9 Out of the glass (er=9 in z>0, air z<0, travel -z, E_t given)")
f = 5e7; w = 2 * np.pi * f
m1 = medium(w, er=9); m2 = medium(w)
print(f"  beta1 = {m1['g'].imag/np.pi:.6f} pi, beta2 = {m2['g'].imag/np.pi:.6f} pi rad/m; eta1 = {m1['eta'].real/np.pi:.6f} pi, eta2 = {m2['eta'].real/np.pi:.6f} pi")
G, t = gamma_tau(m1["eta"], m2["eta"])
close("Gamma, tau = 1/2, 3/2", (G, t), (0.5, 1.5))
close("BC solve", gamma_tau_bc(m1["eta"], m2["eta"]), (G, t))
# E_t(z,t) = y 3 sin(wt + beta0 z): phasor -3j y e^{+j beta0 z}
tra = Wave(-3j * Y, -Z, m2["g"], m2["eta"])
zz = -0.4
tt = np.linspace(0, 1 / f, 9)
check("phasor of y 3 sin(wt + pi z/3)", np.allclose([np.real(tra.E(zz * Z) * np.exp(1j * w * s))[1] for s in tt], 3 * np.sin(w * tt + np.pi / 3 * zz)))
o = np.zeros(3)
Ei0 = tra.E(o) / t; Er0 = G * Ei0
inc = Wave(Ei0, -Z, m1["g"], m1["eta"])
ref = Wave(Er0, Z, m1["g"], m1["eta"])
print(f"  E_i(0) = {Ei0}, E_r(0) = {Er0}")
close("E_i(0) = -2j y, E_r(0) = -j y", (Ei0, Er0), (-2j * Y, -1j * Y))
close("H_t = x (-j/40pi) e^{j pi z/3}", tra.H(zz * Z), X * (-1j / (40 * np.pi)) * np.exp(1j * np.pi / 3 * zz))
close("H_i = x (-j/20pi) e^{j pi z}", inc.H(0.3 * Z), X * (-1j / (20 * np.pi)) * np.exp(1j * np.pi * 0.3))
close("H_r = x (+j/40pi) e^{-j pi z}", ref.H(0.3 * Z), X * (1j / (40 * np.pi)) * np.exp(-1j * np.pi * 0.3))
check("tangential E continuous", np.allclose(inc.E(o) + ref.E(o), tra.E(o)))
check("tangential H continuous", np.allclose(inc.H(o) + ref.H(o), tra.H(o)))
maxwell("glass (i + r)", [inc, ref], m1, w, np.array([0.1, 0.2, 0.37]))
maxwell("air (t)", [tra], m2, w, np.array([0.1, 0.2, -0.37]))
Si, Sr, St = inc.S(o), ref.S(o), tra.S(o)
print(f"  <S_i> = {Si[2]*1e3:.5f} z, <S_r> = {Sr[2]*1e3:.5f} z, <S_t> = {St[2]*1e3:.5f} z mW/m^2")
close("<S_i> = -z 1/(20pi)", Si, -Z / (20 * np.pi))
close("<S_r> = +z 1/(80pi)", Sr, Z / (80 * np.pi))
close("<S_t> = -z 3/(80pi)", St, -3 * Z / (80 * np.pi))
close("quadrature <S_t>", tavg_S([tra], -0.2 * Z, w), St, rtol=1e-6, atol=1e-10)
close("balance", abs(Si[2]), abs(Sr[2]) + abs(St[2]))
print(f"  reflected {pct(G**2)}, transmitted {pct(t**2*m1['eta'].real/m2['eta'].real)} (tau^2 eta1/eta2 = {t**2/3:.6f})")
Er_t = [np.real(ref.E(0.3 * Z) * np.exp(1j * w * s))[1] for s in tt]
check("E_r(z,t) = y sin(wt - pi z)", np.allclose(Er_t, np.sin(w * tt - np.pi * 0.3)))
Ei_t = [np.real(inc.E(0.3 * Z) * np.exp(1j * w * s))[1] for s in tt]
check("E_i(z,t) = y 2 sin(wt + pi z)", np.allclose(Ei_t, 2 * np.sin(w * tt + np.pi * 0.3)))

# ============================================================================
hdr("25.10 Into lossy ground (er=2, sigma/(w eps) = sqrt3, w = 3e8)")
w = 3e8
er = 2
sig = np.sqrt(3) * w * er * eps0C
print(f"  sigma = sqrt3 w eps = {sig:.6e} S/m; sqrt3/(60pi) = {np.sqrt(3)/(60*np.pi):.6e}; with exact eps0: {np.sqrt(3)*w*er*eps0:.6e}")
close("sigma = sqrt3/(60pi)", sig, np.sqrt(3) / (60 * np.pi))
m1 = medium(w); m2 = medium(w, er=er, sig=sig)
print(f"  beta0 = {m1['g'].imag:.6f} rad/m")
print(f"  gamma2 = {m2['g']:.6f}; 1 + j sqrt3 = {1+1j*np.sqrt(3):.6f}")
print(f"  eta2 = {m2['eta']:.6f} = {abs(m2['eta'])/np.pi:.6f} pi angle {np.degrees(np.angle(m2['eta'])):.6f} deg")
close("gamma2 = 1 + j sqrt3", m2["g"], 1 + 1j * np.sqrt(3))
close("eta2 = 60 pi e^{j30}", m2["eta"], 60 * np.pi * np.exp(1j * np.pi / 6))
close("gamma eta = j w mu0", m2["g"] * m2["eta"], 1j * w * mu0)
close("gamma/eta = sigma + j w eps", m2["g"] / m2["eta"], sig + 1j * w * er * eps0C)
G, t = gamma_tau(m1["eta"], m2["eta"])
Gx = (-3 + 2j) / (5 + 2 * np.sqrt(3)); tx = (2 + 2 * np.sqrt(3) + 2j) / (5 + 2 * np.sqrt(3))
print(f"  Gamma = {G:.6f} = {abs(G):.6f} angle {np.degrees(np.angle(G)):.4f} deg")
print(f"  tau = {t:.6f} = {abs(t):.6f} angle {np.degrees(np.angle(t)):.4f} deg")
close("Gamma exact form (-3+2j)/(5+2sqrt3)", G, Gx)
close("tau exact form", t, tx)
close("BC solve", gamma_tau_bc(m1["eta"], m2["eta"]), (G, t))
print(f"  |Gamma|^2 = {abs(G)**2:.6f} = 13/(5+2sqrt3)^2 = {13/(5+2*np.sqrt(3))**2:.6f}; 1-|G|^2 = {1-abs(G)**2:.6f}; |tau|^2 = {abs(t)**2:.6f}")
E0 = 10
inc = Wave(E0 * X, Z, m1["g"], m1["eta"])
ref = Wave(G * E0 * X, -Z, m1["g"], m1["eta"])
tra = Wave(t * E0 * X, Z, m2["g"], m2["eta"])
o = np.zeros(3)
Et0 = tra.E(o)[0]; Ht0 = tra.H(o)[1]; Er0 = ref.E(o)[0]; Hr0 = ref.H(o)[1]
print(f"  E_t(0) = {Et0:.5f} = {abs(Et0):.5f} angle {np.degrees(np.angle(Et0)):.4f} deg V/m")
print(f"  H_t(0) = {Ht0:.6f} = {abs(Ht0)*1e3:.5f} mA/m angle {np.degrees(np.angle(Ht0)):.4f} deg")
print(f"  E_r(0) = {Er0:.5f} = {abs(Er0):.5f} angle {np.degrees(np.angle(Er0)):.4f} deg; H_r(0) = {Hr0:.6f} = {abs(Hr0)*1e3:.5f} mA/m angle {np.degrees(np.angle(Hr0)):.4f}")
check("H_t along +y (E x H along +z)", tra.S(o)[2] > 0)
maxwell("air (i + r)", [inc, ref], m1, w, np.array([0.1, 0.2, -0.37]))
maxwell("ground (t)", [tra], m2, w, np.array([0.1, 0.2, 0.37]))
check("tangential E continuous", np.allclose(inc.E(o) + ref.E(o), tra.E(o)))
check("tangential H continuous", np.allclose(inc.H(o) + ref.H(o), tra.H(o)))
Si, Sr, St = inc.S(o), ref.S(o), tra.S(o)
print(f"  <S_i> = {Si[2]:.6f}, <S_r> = {Sr[2]:.6f}, <S_t>(0+) = {St[2]:.6f} W/m^2; 100/(240pi) = {100/(240*np.pi):.6f}")
close("balance", Si[2], -Sr[2] + St[2])
close("quadrature <S_t>(0.2)", tavg_S([tra], 0.2 * Z, w), tra.S(0.2 * Z), rtol=1e-6, atol=1e-10)
close("<S_t> decays e^{-2z}", tra.S(0.5 * Z)[2], St[2] * np.exp(-1.0))
# net flux in air region at several z equals transmitted (no cross term)
for zq in [-0.3, -1.1]:
    close(f"net <S> in air at z={zq}", tavg_S([inc, ref], zq * Z, w)[2], St[2], rtol=1e-6, atol=1e-10)
joule = integrate.quad(lambda zq: 0.5 * sig * np.sum(np.abs(tra.E(zq * Z))**2), 0, np.inf)[0]
print(f"  Joule heating int 1/2 sigma |E_t|^2 dz = {joule:.6f} W/m^2; sigma|tau E0|^2/(4 alpha) = {sig*abs(t*E0)**2/4:.6f}")
close("Joule = <S_t>(0+)", joule, St[2])
close("Re(1/eta2) = sigma/(2 alpha) = sqrt3/(120pi)", (np.real(1 / m2["eta"]), sig / 2), (np.sqrt(3) / (120 * np.pi),) * 2)
print(f"  depth 1 m: power fraction e^-2 = {np.exp(-2):.5f}; <S_t>(1 m) = {St[2]*np.exp(-2)*1e3:.4f} mW/m^2")
print(f"  regime: sigma/(w eps) = {sig/(w*er*eps0C):.6f} (neither: between 0.1 and 10)")

# ============================================================================
hdr("25.11 A circular wave on a mirror (travel +y in air, PEC in y>0)")
f = 1.5e8; w = 2 * np.pi * f
b = w / cC
print(f"  beta = {b/np.pi:.6f} pi rad/m, lambda = {2*np.pi/b:.6f} m")
# E_i = z 4 cos(wt - pi y) - x 4 sin(wt - pi y)  -> phasor 4(z + j x) e^{-j pi y}
Ei_ph = 4 * Z + 4j * X
inc = Wave(Ei_ph, Y, 1j * b, eta0)
yy = -0.37
tt = np.linspace(0, 1 / f, 9)
Et = np.array([np.real(inc.E(yy * Y) * np.exp(1j * w * s)) for s in tt])
check("phasor 4(z + jx) e^{-j pi y} reproduces the given real field",
      np.allclose(Et[:, 2], 4 * np.cos(w * tt - b * yy)) and np.allclose(Et[:, 0], -4 * np.sin(w * tt - b * yy)))
o = np.zeros(3)
print(f"  incident at y=0: E(0) = {np.real(Ei_ph)}, E(T/4) = {np.real(1j*Ei_ph)}; u.[E0 x E(T/4)] = {np.dot(Y, np.cross(np.real(Ei_ph), np.real(1j*Ei_ph)))}")
print(f"  incident hand: recipe {hand(Ei_ph, Y)}, brute {hand_brute(Ei_ph, Y)}")
check("incident left-circular", hand(Ei_ph, Y) == "left" and hand_brute(Ei_ph, Y) == "left")
ref = Wave(-Ei_ph, -Y, 1j * b, eta0)
Ert = np.array([np.real(ref.E(yy * Y) * np.exp(1j * w * s)) for s in tt])
check("E_r(y,t) = -z 4 cos(wt + pi y) + x 4 sin(wt + pi y)",
      np.allclose(Ert[:, 2], -4 * np.cos(w * tt + b * yy)) and np.allclose(Ert[:, 0], 4 * np.sin(w * tt + b * yy)))
print(f"  reflected at y=0: E(0) = {np.real(-Ei_ph)}, E(T/4) = {np.real(-1j*Ei_ph)}; (-y).[..] = {np.dot(-Y, np.cross(np.real(-Ei_ph), np.real(-1j*Ei_ph)))}")
print(f"  reflected hand: recipe {hand(-Ei_ph, -Y)}, brute {hand_brute(-Ei_ph, -Y)}")
check("reflected right-circular", hand(-Ei_ph, -Y) == "right" and hand_brute(-Ei_ph, -Y) == "right")
Hi0, Hr0 = inc.H(o), ref.H(o)
print(f"  H_i(0) = {np.round(Hi0*30*np.pi, 8)}/(30pi), H_r(0) = {np.round(Hr0*30*np.pi, 8)}/(30pi)")
close("H_i = (x - jz)/(30pi) e^{-j pi y}", inc.H(yy * Y), (X - 1j * Z) / (30 * np.pi) * np.exp(-1j * b * yy))
close("H_r = (x - jz)/(30pi) e^{+j pi y}", ref.H(yy * Y), (X - 1j * Z) / (30 * np.pi) * np.exp(1j * b * yy))
maxwell("air (i + r)", [inc, ref], medium(w), w, np.array([0.2, -0.31, 0.1]))
Etot, Htot = inc.E(o) + ref.E(o), Hi0 + Hr0
close("total E at wall = 0", Etot, np.zeros(3))
close("total H at wall = (x - jz)/(15pi)", Htot, (X - 1j * Z) / (15 * np.pi))
n = -Y  # from PEC (y>0) into air (y<0)
Js = np.cross(n, Htot)
print(f"  J_s phasor = {np.round(Js*15*np.pi, 8)}/(15pi); |J_s| = {np.linalg.norm(np.real(Js)) *1e3:.5f} mA/m = 1/(15pi) = {1e3/(15*np.pi):.5f}")
close("J_s = (z + jx)/(15pi) = 2 E_i(0)/eta0", Js, 2 * Ei_ph / eta0)
Jst = np.array([np.real(Js * np.exp(1j * w * s)) for s in tt])
check("J_s(t) = (1/15pi)[z cos wt - x sin wt]", np.allclose(Jst[:, 2], np.cos(w * tt) / (15 * np.pi)) and np.allclose(Jst[:, 0], -np.sin(w * tt) / (15 * np.pi)))
check("|J_s(t)| constant", np.allclose(np.linalg.norm(Jst, axis=1), 1 / (15 * np.pi)))
Si, Sr = inc.S(o), ref.S(o)
print(f"  <S_i> = {np.round(Si*1e3, 5)} mW/m^2 = y 2/(15pi) = {2/(15*np.pi)*1e3:.5f}; <S_r> = {np.round(Sr*1e3, 5)}")
close("<S_i> = y 2/(15pi)", Si, 2 * Y / (15 * np.pi))
close("quadrature <S_i>", tavg_S([inc], yy * Y, w), Si, rtol=1e-6, atol=1e-10)
close("net <S> in air = 0", tavg_S([inc, ref], yy * Y, w), np.zeros(3), atol=1e-10)
print(f"  each component alone: 16/(240pi) = {16/(240*np.pi)*1e3:.5f} mW/m^2 (= 1/(15pi))")
# variant (e): dielectric er = 9 instead of PEC
Gd, td = gamma_tau(eta0, eta0 / 3)
print(f"  (e) er=9: Gamma = {Gd}, tau = {td}; reflected amplitude {4*abs(Gd)}, hand {hand(Gd*Ei_ph, -Y)}; "
      f"transmitted amplitude {4*td}, hand {hand(td*Ei_ph, Y)}")
check("(e) reflected right, transmitted left", hand(Gd * Ei_ph, -Y) == "right" and hand(td * Ei_ph, Y) == "left")

# ============================================================================
hdr("25.12 Identifying a material from reflection data")
f = 1e8; w = 2 * np.pi * f
b0 = w / cC
print(f"  beta0 = {b0/np.pi:.6f} pi rad/m, lambda0 = {2*np.pi/b0:.6f} m")
G = 2 / 10
t = 1 + G
eta2 = eta0 * (1 + G) / (1 - G)
b2 = 2 * np.pi / 1.5
print(f"  Gamma = {G}, tau = {t}, eta2 = {eta2/np.pi:.6f} pi Ohm, beta2 = {b2/np.pi:.6f} pi rad/m, n = {b2/b0:.6f}")
g2 = 1j * b2
mu2 = g2 * eta2 / (1j * w); eps2 = g2 / (1j * w * eta2)
mur, er = (mu2 / mu0).real, (eps2 / eps0C).real
print(f"  mu2 = gamma eta/(jw) -> mur = {mur:.6f}; eps2 = gamma/(jw eta) -> er = {er:.6f}")
close("mur = 3, er = 4/3", (mur, er), (3.0, 4 / 3))
m2 = medium(w, mur=3, er=4 / 3)
close("forward: eta2 = 180pi, beta2 = 4pi/3", (m2["eta"], m2["g"]), (180 * np.pi, 1j * 4 * np.pi / 3))
Gf, tf = gamma_tau(eta0, m2["eta"])
close("forward Gamma = 0.2", Gf, 0.2)
inc = Wave(10 * X, Z, 1j * b0, eta0)
ref = Wave(G * 10 * X, -Z, 1j * b0, eta0)
tra = Wave(t * 10 * X, Z, m2["g"], m2["eta"])
o = np.zeros(3)
tt = np.linspace(0, 1 / f, 9)
check("E_r(z,t) = x 2 cos(wt + beta0 z)", np.allclose([np.real(ref.E(-0.3 * Z) * np.exp(1j * w * s))[0] for s in tt], 2 * np.cos(w * tt + b0 * (-0.3))))
Ht0 = tra.H(o)
print(f"  E_t(0) = {tra.E(o)[0].real} V/m; H_t(0) = {np.round(Ht0, 8)} = y 1/(15pi) = {1/(15*np.pi):.8f} A/m = {1e3/(15*np.pi):.4f} mA/m")
close("H_t = y (1/15pi) e^{-j 4pi z/3}", tra.H(0.2 * Z), Y / (15 * np.pi) * np.exp(-1j * 4 * np.pi / 3 * 0.2))
check("tangential E, H continuous", np.allclose(inc.E(o) + ref.E(o), tra.E(o)) and np.allclose(inc.H(o) + ref.H(o), tra.H(o)))
maxwell("material (t)", [tra], m2, w, np.array([0.1, 0.2, 0.37]))
Si, Sr, St = inc.S(o), ref.S(o), tra.S(o)
print(f"  <S_i> = {Si[2]*1e3:.5f} z, <S_r> = {Sr[2]*1e3:.5f} z, <S_t> = {St[2]*1e3:.5f} z mW/m^2")
close("<S_i> = 5/(12pi), <S_r> = -1/(60pi), <S_t> = 2/(5pi)", (Si[2], Sr[2], St[2]), (5 / (12 * np.pi), -1 / (60 * np.pi), 2 / (5 * np.pi)))
close("balance", Si[2], -Sr[2] + St[2])
print(f"  reflected {pct(G**2)}, transmitted {pct(t**2*eta0/m2['eta'].real)}")
Gm, _ = gamma_tau(eta0, eta0 * np.sqrt((4 / 3) / (4 / 3)))
close("(d) mur = 4/3 with er = 4/3 matched", Gm, 0.0)
print(f"  (d) n = 4/3, lambda inside = {3/(4/3):.4f} m")
# wrong-sign check: an inverted reflection (Gamma = -0.2) would give eta2 = (2/3) eta0
print(f"  if E_r were inverted (Gamma = -0.2): eta2 = {(0.8/1.2):.6f} eta0 -> mur = {2*0.8/1.2:.6f}, er = {2/(0.8/1.2):.6f}")

# ============================================================================
print("\n" + "=" * 78)
print(f"TOTAL CHECKS: {len(ALL)}, FAILED: {ALL.count(False)}")
