#!/usr/bin/env python3
"""Verification of every number, sign and direction on the Lecture 18 pages of the ECE 329 site:
  3-maxwell-and-waves/18-the-wave-equation-and-plane-tem-waves.md
  concepts/wave-equation.md, concepts/plane-waves.md, concepts/intrinsic-impedance.md
  problems/a-pulse-on-the-move.md
  (+ the one-sentence additions to displacement-current, faradays-law, coax-inductance-and-the-lc-product)
  figures wave-* in /home/claude/work/figs_l18.py
numpy only (no sympy). Derivatives by central differences. Every direction by an explicit np.cross.
Output: verify_L18.out (run: python3 verify_L18.py > verify_L18.out)
"""
import numpy as np

NP = NF = 0
def check(label, ok, detail=""):
    global NP, NF
    if ok:
        NP += 1; tag = "PASS"
    else:
        NF += 1; tag = "FAIL"
    print(f"[{tag}] {label}" + (f"  ::  {detail}" if detail else ""))

def rel(a, b):
    a, b = np.asarray(a, float), np.asarray(b, float)
    return float(np.max(np.abs(a - b)) / max(np.max(np.abs(b)), 1e-300))

def section(s):
    print("\n" + "=" * 100 + "\n" + s + "\n" + "=" * 100)

# ------------------------------------------------------------------ constants
mu0 = 4e-7 * np.pi
eps0 = 8.8541878128e-12
c = 1 / np.sqrt(mu0 * eps0)
eta0 = np.sqrt(mu0 / eps0)

X, Y, Z = np.eye(3)          # unit vectors x^, y^, z^ (physics frame)

# finite-difference helpers on fields F(x, y, z, t) -> 3-vector
def dpart(F, i, p, h):
    p1 = np.array(p, float); p2 = np.array(p, float)
    p1[i] += h; p2[i] -= h
    return (np.asarray(F(*p1), float) - np.asarray(F(*p2), float)) / (2 * h)

def curl(F, p, h):
    dx, dy, dz = (dpart(F, i, p, h) for i in range(3))
    return np.array([dy[2] - dz[1], dz[0] - dx[2], dx[1] - dy[0]])

def div(F, p, h):
    return dpart(F, 0, p, h)[0] + dpart(F, 1, p, h)[1] + dpart(F, 2, p, h)[2]

def lap(F, p, h):
    out = 0
    for i in range(3):
        p1 = np.array(p, float); p2 = np.array(p, float); p1[i] += h; p2[i] -= h
        out = out + (np.asarray(F(*p1)) - 2 * np.asarray(F(*p)) + np.asarray(F(*p2))) / h**2
    return out

def d2t(F, p, ht):
    p1 = np.array(p, float); p2 = np.array(p, float); p1[3] += ht; p2[3] -= ht
    return (np.asarray(F(*p1)) - 2 * np.asarray(F(*p)) + np.asarray(F(*p2))) / ht**2

# =====================================================================================
section("A. Constants (Lecture 18 sections 4, 5, 7; toolkit values)")
check("c = 1/sqrt(mu0 eps0) = 2.998e8 m/s", abs(c - 2.998e8) < 0.0005e8, f"c = {c:.6e} m/s")
check("c x 1 us = 299.8 m (~300 m)", abs(c * 1e-6 - 299.8) < 0.05, f"{c*1e-6:.3f} m")
check("c x 1 ms = 299.8 km (~300 km)", abs(c * 1e-3 / 1e3 - 299.8) < 0.05, f"{c*1e-3/1e3:.3f} km")
check("c x 1 ns = 0.2998 m (~30 cm)", abs(c * 1e-9 - 0.2998) < 5e-5, f"{c*1e-9:.5f} m")
check("eta0 = sqrt(mu0/eps0) = 376.73 ohm", abs(eta0 - 376.73) < 0.005, f"eta0 = {eta0:.4f} ohm")
check("120 pi = 376.99 ohm; relative difference from eta0 = 6.9e-4",
      abs(120 * np.pi - 376.99) < 0.005 and abs((120 * np.pi - eta0) / eta0 - 6.9e-4) < 0.05e-4,
      f"120pi = {120*np.pi:.4f}, rel diff = {(120*np.pi-eta0)/eta0:.3e}")
check("eta0 c eps0 = 1 (so eps0 c = 1/eta0)", abs(eta0 * c * eps0 - 1) < 1e-12, f"{eta0*c*eps0:.15f}")
check("mu0 c = eta0 (so eta = mu v in vacuum)", abs(mu0 * c - eta0) / eta0 < 1e-12, f"mu0 c = {mu0*c:.4f}")
check("slides' S22 '3e8' and '377': c/3e8 = 0.99931, eta0/377 = 0.99928",
      abs(c / 3e8 - 0.99931) < 1e-5 and abs(eta0 / 377 - 0.99928) < 1e-5, f"{c/3e8:.5f}, {eta0/377:.5f}")

# =====================================================================================
section("B. The curl-curl identity and the 3D vector wave equation (section 2)")
def Etest(x, y, z, t=0.0):
    return np.array([np.sin(x * y) + z**2, x * np.cos(y + z), x * y * z])
p0 = (0.4, -0.7, 0.9, 0.0)
h = 1e-3
cc = curl(lambda x, y, z, t: curl(Etest, (x, y, z, t), h), p0, h)
gdiv = np.array([dpart(lambda x, y, z, t: np.array([div(Etest, (x, y, z, t), h)] * 3), i, p0, h)[0] for i in range(3)])
lapE = lap(Etest, p0, h)
check("curl curl E = grad div E - lap E (test field, Cartesian components)", rel(cc, gdiv - lapE) < 1e-5,
      f"LHS {np.round(cc,5)}, RHS {np.round(gdiv-lapE,5)}")

# plane wave in a dielectric eps_r = 4, mu_r = 1, Gaussian waveform (time scale 1 ns)
epsr = 4.0
mu, eps = mu0, epsr * eps0
v = 1 / np.sqrt(mu * eps); eta = np.sqrt(mu / eps)
f = lambda s: np.exp(-((s - 2e-9) / 0.7e-9) ** 2)
E_pw = lambda x, y, z, t: np.array([f(t - z / v), 0.0, 0.0])
H_pw = lambda x, y, z, t: np.array([0.0, f(t - z / v) / eta, 0.0])
ht = 2e-12; hz = v * ht
for (zz, tt) in ((0.05, 2.3e-9), (-0.08, 1.1e-9), (0.11, 3.4e-9)):
    p = (0.3, -0.2, zz, tt)
    dE = div(E_pw, p, hz); dH = div(H_pw, p, hz)
    far = curl(E_pw, p, hz); dHt = (np.array(H_pw(*p[:3], tt + ht)) - np.array(H_pw(*p[:3], tt - ht))) / (2 * ht)
    amp = curl(H_pw, p, hz); dEt = (np.array(E_pw(*p[:3], tt + ht)) - np.array(E_pw(*p[:3], tt - ht))) / (2 * ht)
    LE = lap(E_pw, p, hz); TE = d2t(E_pw, p, ht)
    LH = lap(H_pw, p, hz); TH = d2t(H_pw, p, ht)
    check(f"source-free Maxwell for E = x f(t-z/v), H = y f/eta at z={zz}, t={tt:.1e}: div E = div H = 0",
          abs(dE) < 1e-6 and abs(dH) < 1e-8, f"divE={dE:.1e}, divH={dH:.1e}")
    check("   Faraday curl E = -mu dH/dt", rel(far, -mu * dHt) < 1e-5, f"{far[1]:.6e} vs {-mu*dHt[1]:.6e}")
    check("   Ampere-Maxwell curl H = eps dE/dt (J = 0)", rel(amp, eps * dEt) < 1e-5, f"{amp[0]:.6e} vs {eps*dEt[0]:.6e}")
    check("   vector wave equation for E and for H", rel(LE, mu * eps * TE) < 1e-4 and rel(LH, mu * eps * TH) < 1e-4,
          f"lapEx={LE[0]:.5e}, mu eps d2Ex/dt2={mu*eps*TE[0]:.5e}")
# without the displacement current: the curl-curl step gives lap E = 0, which this travelling pulse violates
p = (0.0, 0.0, 0.05, 2.3e-9)
check("a travelling pulse has lap E != 0, so 'lap E = 0' (no displacement current) has no such wave",
      abs(lap(E_pw, p, hz)[0]) > 1.0, f"lap Ex = {lap(E_pw, p, hz)[0]:.3e} V/m^3 (not 0; scale f''/v^2 ~ 1e2)")
# grad(eps) term: if eps varied, div(eps E) = 0 would not give div E = 0
epsfun = lambda x, y, z: eps0 * (1 + z**2)
Etry = lambda x, y, z, t: np.array([0.0, 0.0, 1.0 / (1 + z**2)])
D = lambda x, y, z, t: epsfun(x, y, z) * Etry(x, y, z, t)
check("variable eps: div D = 0 but div E != 0 (why constant eps is assumed)",
      abs(div(D, (0, 0, 0.5, 0), 1e-4)) < 1e-15 and abs(div(Etry, (0, 0, 0.5, 0), 1e-4)) > 0.1,
      f"div D = {div(D,(0,0,0.5,0),1e-4):.1e}, div E = {div(Etry,(0,0,0.5,0),1e-4):.3f}")

# =====================================================================================
section("C. Component equations (section 3): signs of the two scalar equations")
Ex_only = lambda x, y, z, t: np.array([np.sin(3 * z) * np.cos(t), 0.0, 0.0])
Hy_only = lambda x, y, z, t: np.array([0.0, np.cos(2 * z) * np.sin(t), 0.0])
pp = (0.2, 0.1, 0.37, 0.8)
cE = curl(Ex_only, pp, 1e-5); cH = curl(Hy_only, pp, 1e-5)
check("curl(x Ex(z,t)) = y dEx/dz  ->  dEx/dz = -mu dHy/dt", rel(cE, [0, 3 * np.cos(3 * 0.37) * np.cos(0.8), 0]) < 1e-8, f"{cE}")
check("curl(y Hy(z,t)) = -x dHy/dz ->  -dHy/dz = eps dEx/dt", rel(cH, [2 * np.sin(2 * 0.37) * np.sin(0.8), 0, 0]) < 1e-8, f"{cH}")
check("div(x Ex(z,t)) = dEx/dx = 0 automatically (trial field obeys Gauss)", abs(div(Ex_only, pp, 1e-5)) < 1e-10)
# slides S9: with H = y Hy(z,t) and no x,y dependence: Faraday x-component -> dEy/dz = 0, Gauss -> dEz/dz = 0
Fgen = lambda x, y, z, t: np.array([np.sin(z - t), 0.0, 0.0])   # Ey = Ez = 0
check("S9: curl of a field with no x,y dependence has x-comp -dEy/dz and z-comp 0",
      abs(curl(lambda x, y, z, t: np.array([0.0, z**2, 0.0]), (0, 0, 1.3, 0), 1e-5)[0] + 2 * 1.3) < 1e-8
      and abs(curl(lambda x, y, z, t: np.array([0.0, z**2, 0.0]), (0, 0, 1.3, 0), 1e-5)[2]) < 1e-12,
      "(curl (0, z^2, 0))_x = -2z, _z = 0")

# =====================================================================================
section("D. 1D wave equation: cosines, factorization, d'Alembert (section 4)")
w = 2 * np.pi * 1e8
for sgn in (-1, +1):
    Ec = lambda z, t: np.cos(w * (t + sgn * z / v))
    z0, t0 = 0.37, 1.3e-9
    hz2, ht2 = 1e-4, 1e-4 / v
    Ezz = (Ec(z0 + hz2, t0) - 2 * Ec(z0, t0) + Ec(z0 - hz2, t0)) / hz2**2
    Ett = (Ec(z0, t0 + ht2) - 2 * Ec(z0, t0) + Ec(z0, t0 - ht2)) / ht2**2
    check(f"cos(w(t {'+' if sgn>0 else '-'} z/v)) solves d2E/dz2 = mu eps d2E/dt2 (eps_r = 4)",
          abs(Ezz - mu * eps * Ett) < 1e-5 * abs(Ezz), f"{Ezz:.6e} vs {mu*eps*Ett:.6e}")
check("v = 1/sqrt(mu eps) has units m/s and equals c/2 for eps_r = 4", abs(v - c / 2) < 1e-6 * c, f"v = {v:.5e}")
# operator factorization (tau = z/v): (d_tau + d_t)(d_tau - d_t) E = E_tautau - E_tt
Ef = lambda tau, t: np.exp(-(t - 0.3 * tau) ** 2) * np.sin(2 * tau + t)
ta0, tt0, hh = 0.4, -0.2, 1e-3
def dta(F): return lambda a, b: (F(a + hh, b) - F(a - hh, b)) / (2 * hh)
def dtt(F): return lambda a, b: (F(a, b + hh) - F(a, b - hh)) / (2 * hh)
inner = lambda a, b: dta(Ef)(a, b) - dtt(Ef)(a, b)
lhs = dta(inner)(ta0, tt0) + dtt(inner)(ta0, tt0)
rhs = ((Ef(ta0 + hh, tt0) - 2 * Ef(ta0, tt0) + Ef(ta0 - hh, tt0)) - (Ef(ta0, tt0 + hh) - 2 * Ef(ta0, tt0) + Ef(ta0, tt0 - hh))) / hh**2
check("(d_tau + d_t)(d_tau - d_t)E = d2E/dtau2 - d2E/dt2 (factorization of the wave operator)", abs(lhs - rhs) < 1e-5, f"{lhs:.6f} vs {rhs:.6f}")
fa = lambda s: np.exp(-s**2) * (1 + s)
Ff = lambda tau, t: fa(t - tau); Gg = lambda tau, t: fa(t + tau)
check("(d_tau + d_t) f(t - tau) = 0  [S19: Af'(-1) = -Af']", abs(dta(Ff)(0.3, 0.9) + dtt(Ff)(0.3, 0.9)) < 1e-6)
check("(d_tau - d_t) g(t + tau) = 0  [S19: Bg' = Bg']", abs(dta(Gg)(0.3, 0.9) - dtt(Gg)(0.3, 0.9)) < 1e-6)
check("tau = z sqrt(mu0 eps0) = z/c: 1 m -> 3.3356 ns", abs(1 * np.sqrt(mu0 * eps0) - 3.3356e-9) < 1e-13, f"{np.sqrt(mu0*eps0):.5e} s")
# characteristic coordinates: d_tau + d_t = 2 d_zeta, d_tau - d_t = -2 d_xi (xi = t - tau, zeta = t + tau)
Wf = lambda xi, ze: np.sin(xi) * np.exp(0.3 * ze) + xi**2 * ze
E_tt = lambda tau, t: Wf(t - tau, t + tau)
d_ze = (Wf(0.2 - 0.5, 0.2 + 0.5 + hh) - Wf(0.2 - 0.5, 0.2 + 0.5 - hh)) / (2 * hh)
d_xi = (Wf(0.2 - 0.5 + hh, 0.2 + 0.5) - Wf(0.2 - 0.5 - hh, 0.2 + 0.5)) / (2 * hh)
sum_ = dta(E_tt)(0.5, 0.2) + dtt(E_tt)(0.5, 0.2); dif_ = dta(E_tt)(0.5, 0.2) - dtt(E_tt)(0.5, 0.2)
check("in xi = t - tau, zeta = t + tau: (d_tau + d_t) = 2 d_zeta and (d_tau - d_t) = -2 d_xi (so E = F(xi) + G(zeta))",
      abs(sum_ - 2 * d_ze) < 1e-5 and abs(dif_ + 2 * d_xi) < 1e-5, f"{sum_:.6f} vs {2*d_ze:.6f}; {dif_:.6f} vs {-2*d_xi:.6f} (FD error ~ h^2)")
# Fourier (LTI) superposition of cosines travels rigidly and solves the wave equation
rng = np.random.default_rng(18)
An, wn, th = rng.uniform(0.2, 1, 6), rng.uniform(0.5, 3, 6) * 1e8 * 2 * np.pi, rng.uniform(0, 2 * np.pi, 6)
fsum = lambda s: np.sum(An * np.cos(wn * s + th))
z0, t0 = 0.6, 4e-9
check("sum_n A_n cos(w_n (t - z/v) + th_n) at (z,t) equals the z = 0 waveform at t - z/v", abs(fsum(t0 - z0 / v) - np.sum(An * np.cos(wn * (t0 - z0 / v) + th))) < 1e-12)
hz2 = 1e-4; ht2 = hz2 / v
Ezz = (fsum(t0 - (z0 + hz2) / v) - 2 * fsum(t0 - z0 / v) + fsum(t0 - (z0 - hz2) / v)) / hz2**2
Ett = (fsum(t0 + ht2 - z0 / v) - 2 * fsum(t0 - z0 / v) + fsum(t0 - ht2 - z0 / v)) / ht2**2
check("the Fourier-synthesized waveform solves the 1D wave equation", abs(Ezz - mu * eps * Ett) < 1e-5 * abs(Ezz), f"{Ezz:.5e} vs {mu*eps*Ett:.5e}")

# =====================================================================================
section("E. H from E: Faraday (notes) and Ampere (slides); eta; sign flip for -z (section 5)")
gb = lambda s: np.maximum(0, 1 - np.abs(s - 1e-9) / 0.8e-9) ** 2
A_, B_ = 1.7, -0.6
Ex = lambda z, t: A_ * f(t - z / v) + B_ * gb(t + z / v)
Hy = lambda z, t: (A_ * f(t - z / v) - B_ * gb(t + z / v)) / eta
Hy_wrong = lambda z, t: (A_ * f(t - z / v) + B_ * gb(t + z / v)) / eta
z0, t0 = 0.03, 1.2e-9
hz3 = 1e-6; ht3 = hz3 / v
dEz = (Ex(z0 + hz3, t0) - Ex(z0 - hz3, t0)) / (2 * hz3); dEt = (Ex(z0, t0 + ht3) - Ex(z0, t0 - ht3)) / (2 * ht3)
dHz = (Hy(z0 + hz3, t0) - Hy(z0 - hz3, t0)) / (2 * hz3); dHt = (Hy(z0, t0 + ht3) - Hy(z0, t0 - ht3)) / (2 * ht3)
dHzw = (Hy_wrong(z0 + hz3, t0) - Hy_wrong(z0 - hz3, t0)) / (2 * hz3)
check(f"both waves present here: f = {f(t0-z0/v):.4f}, g = {gb(t0+z0/v):.4f}", f(t0 - z0 / v) > 0.01 and gb(t0 + z0 / v) > 0.01)
check("Faraday dEx/dz = -mu dHy/dt with Hy = (A f - B g)/eta", abs(dEz + mu * dHt) < 1e-6 * abs(dEz), f"{dEz:.6e} vs {-mu*dHt:.6e}")
check("Ampere -dHy/dz = eps dEx/dt with Hy = (A f - B g)/eta", abs(-dHz - eps * dEt) < 1e-6 * abs(eps * dEt), f"{-dHz:.6e} vs {eps*dEt:.6e}")
check("with +Bg instead of -Bg Ampere fails", abs(-dHzw - eps * dEt) > 0.1 * abs(eps * dEt), f"{-dHzw:.4e} vs {eps*dEt:.4e}")
check("notes: amplitude 1/(mu v) = sqrt(eps/mu) = 1/eta", abs(1 / (mu * v) - 1 / eta) < 1e-12 / eta)
check("slides: eps v = 1/eta (the z-antiderivative route)", abs(eps * v - 1 / eta) < 1e-12 / eta)
check("eta = mu v = 1/(eps v) (eps_r = 4 medium)", abs(mu * v - eta) < 1e-9 * eta and abs(1 / (eps * v) - eta) < 1e-9 * eta, f"eta = {eta:.4f}")
Ep = lambda z, t: f(t - z / v); Hp = lambda z, t: f(t - z / v) / eta
Em = lambda z, t: gb(t + z / v); Hm = lambda z, t: -gb(t + z / v) / eta
check("Ex/Hy = +eta for the +z wave, -eta for the -z wave",
      abs(Ep(0.1, 2e-9) / Hp(0.1, 2e-9) - eta) < 1e-9 and abs(Em(-0.05, 1.5e-9) / Hm(-0.05, 1.5e-9) + eta) < 1e-9,
      f"{Ep(0.1,2e-9)/Hp(0.1,2e-9):.3f}, {Em(-0.05,1.5e-9)/Hm(-0.05,1.5e-9):.3f} ohm")
r_mix = Ex(z0, t0) / Hy(z0, t0)
check("with both waves present Ex/Hy is NOT +-eta (trap on the impedance page)", abs(abs(r_mix) - eta) > 0.05 * eta, f"Ex/Hy = {r_mix:.2f} ohm vs eta = {eta:.2f}")
# integration 'constant' h(t) in the Ampere route must be constant by Faraday
hfun = lambda t: 0.3 * np.sin(1e9 * t)
Hy_h = lambda z, t: Hy(z, t) + hfun(t)
dHt_h = (Hy_h(z0, t0 + ht3) - Hy_h(z0, t0 - ht3)) / (2 * ht3)
check("adding a time-varying h(t) to Hy breaks Faraday (so the 'constant' is a static field, dropped)",
      abs(dEz + mu * dHt_h) > 1e-3 * abs(dEz), f"residual {dEz + mu*dHt_h:.3e}")

print("\n-- sign table with explicit cross products (u = direction of travel) --")
rows = [("x-pol, +z", X, Y, Z), ("x-pol, -z", X, -Y, -Z), ("y-pol, +z", Y, -X, Z), ("y-pol, -z", Y, X, -Z)]
for name, Ehat, Hhat, uhat in rows:
    S = np.cross(Ehat, Hhat)
    check(f"{name}: E={Ehat}, H={Hhat}: E x H = {S} = travel {uhat}", np.allclose(S, uhat))
    check(f"{name}: H = (1/eta) u x E  and  E = eta H x u", np.allclose(np.cross(uhat, Ehat), Hhat) and np.allclose(np.cross(Hhat, uhat), Ehat))
# y-polarized via Faraday: curl(y Ey(z,t)) = -x dEy/dz
Ey_f = lambda x, y, z, t: np.array([0.0, f(t - z / v), 0.0])
p = (0, 0, 0.07, 2.1e-9)
cEy = curl(Ey_f, p, hz)     # curl(y Ey(z,t)) = -x dEy/dz
Hx_pred = lambda z, t: -f(t - z / v) / eta
dHx_pred = (Hx_pred(0.07, 2.1e-9 + ht) - Hx_pred(0.07, 2.1e-9 - ht)) / (2 * ht)
check("y-pol +z by Faraday: (curl E)_x = -mu dHx/dt holds with Hx = -f/eta", abs(cEy[0] + mu * dHx_pred) < 1e-5 * abs(cEy[0]), f"{cEy[0]:.5e} vs {-mu*dHx_pred:.5e}")
# z-polarized: div != 0, curl = 0, yet solves the 1D wave equation
Ez_f = lambda x, y, z, t: np.array([0.0, 0.0, f(t - z / v)])
p = (0, 0, 0.07, 2.1e-9)
dz_ = div(Ez_f, p, hz)
check("z-pol along z: div E = -f'/v != 0 (forbidden by Gauss with rho = 0)", abs(dz_) > 1.0, f"div E = {dz_:.4e} V/m^2")
check("z-pol along z: curl E = 0, so Faraday gives no H at all", np.max(np.abs(curl(Ez_f, p, hz))) < 1e-6)
LE = lap(Ez_f, p, hz)[2]; TE = d2t(Ez_f, p, ht)[2]
check("... yet E_z = f(t - z/v) satisfies the wave equation (necessary, not sufficient)", abs(LE - mu * eps * TE) < 1e-4 * abs(LE), f"{LE:.5e} vs {mu*eps*TE:.5e}")

# =====================================================================================
section("F. Current sheet (slides S4-S11; section 3 and figure wave-current-sheet)")
Js = -X   # J_s = -J_s(t) x^ with J_s(t) > 0
Hp_static = 0.5 * np.cross(Js, Z); Hm_static = 0.5 * np.cross(Js, -Z)
check("static sheet (Lecture 13): H(z>0) = 1/2 Js x z = +y/2", np.allclose(Hp_static, 0.5 * Y), f"{Hp_static}")
check("static sheet: H(z<0) = 1/2 Js x (-z) = -y/2", np.allclose(Hm_static, -0.5 * Y), f"{Hm_static}")
check("static sheet: z x (H+ - H-) = Js (jump condition, consistent)", np.allclose(np.cross(Z, Hp_static - Hm_static), Js))
E_both = X   # slides' ink: E always opposite of J_s
check("slides' ink 'E always opposite of J_s': E = +x when J_s = -x", np.dot(E_both, Js) < 0)
check("z>0: E x H = x x y = +z (away from the sheet)", np.allclose(np.cross(E_both, Y), Z))
check("z<0: E x H = x x (-y) = -z (away from the sheet)", np.allclose(np.cross(E_both, -Y), -Z))
# slides' 3D axes: x up, z right, y toward the viewer; screen frame (X right, Y up, Z out of the screen)
sx, sy, sz = np.array([0, 1, 0]), np.array([0, 0, 1]), np.array([1, 0, 0])   # physics x, y, z in screen coords
check("figure frame (x up, y out of page, z right) is right-handed: x cross y = z", np.allclose(np.cross(sx, sy), sz))
check("notes' p.6 frame (x right, y into page, z up) is right-handed", np.allclose(np.cross([1, 0, 0], [0, 0, -1]), [0, 1, 0]))
# in the figure (edge-on view, page = xz-plane): J_s drawn down, H right = out (odot), H left = into (otimes)
Js_scr = -sx
check("figure: 1/2 Js x n(right) on screen = out of the page (odot) = +y", np.allclose(0.5 * np.cross(Js_scr, sz) / 0.5, sy))
check("figure: 1/2 Js x n(left) on screen = into the page (otimes) = -y", np.allclose(np.cross(Js_scr, -sz), -sy))
check("figure: E up x H odot = right (+z travel); E up x H otimes = left (-z travel)",
      np.allclose(np.cross(sx, sy), sz) and np.allclose(np.cross(sx, -sy), -sz))
# L19-preview consistency: E = -(eta/2) J_s at the sheet gives the same directions (not derived on the page)
E19 = -(eta0 / 2) * Js; H19p = np.cross(Z, E19) / eta0; H19m = np.cross(-Z, E19) / eta0
check("(L19 preview, not derived) E = -(eta/2)Js: H(0+) = +y/2, H(0-) = -y/2, the static jump J_s",
      np.allclose(H19p, 0.5 * Y) and np.allclose(H19m, -0.5 * Y) and np.allclose(np.cross(Z, H19p - H19m), Js))
# S5 typed recap sketch: y down, z right on screen -> x = y cross z out of the page
check("S5 sketch frame: x = y x z with y down, z right is out of the page", np.allclose(np.cross([0, -1, 0], [1, 0, 0]), [0, 0, 1]))
check("S5 arrows (H down at z<0, up at z>0) match J = +x (out of page), i.e. opposite to S4's -x",
      np.allclose(0.5 * np.cross([0, 0, 1], [1, 0, 0]), [0, 0.5, 0]) and np.allclose(0.5 * np.cross([0, 0, 1], [-1, 0, 0]), [0, -0.5, 0]))

# =====================================================================================
section("G. Reading a wave: slide 24 challenge (section 6)")
def velocity(a, k):
    k = np.asarray(k, float)
    return -a * k / np.dot(k, k)
vf = velocity(-1.0, [0, 0.05, 0]); vg = velocity(1.0, [0.02, 0, 0]); vh = velocity(2 * np.pi * 1e8, [0, 0, -2 * np.pi])
check("f = (0.05y - t)^2: velocity +20 y m/s", np.allclose(vf, [0, 20, 0]), f"{vf}")
check("g = u(t + 0.02x): velocity -50 x m/s", np.allclose(vg, [-50, 0, 0]), f"{vg}")
check("h = cos(2pi 1e8 t - 2pi z): velocity +1e8 z m/s", np.allclose(vh, [0, 0, 1e8]), f"{vh}")
opts = {"a": ([0, 0.05, 0], [-0.02, 0, 0], [0, 0, 1e8]), "b": ([0, 0.05, 0], [-0.02, 0, 0], [0, 0, -1e8]),
        "c": ([0, 20, 0], [-50, 0, 0], [0, 0, 1e8]), "d": ([0, 20, 0], [50, 0, 0], [0, 0, 1e8]),
        "e": ([0, 20, 0], [-50, 0, 0], [0, 0, -1e8])}
right = [k for k, (a1, a2, a3) in opts.items() if np.allclose(a1, vf) and np.allclose(a2, vg) and np.allclose(a3, vh)]
check("only option (c) matches", right == ["c"], f"{right}")
ff = lambda y, t: (0.05 * y - t) ** 2
check("the zero of f sits at y = 20 t: y = 0, 20, 40 m at t = 0, 1, 2 s", all(abs(ff(20 * t, t)) < 1e-12 for t in (0, 1, 2)))
check("(0.05y - t)^2 = (t - y/20)^2 (order of terms does not matter)", abs(ff(13.0, 0.4) - (0.4 - 13.0 / 20) ** 2) < 1e-14)
epsr_h = (c / 1e8) ** 2
check("h at 1e8 m/s in a non-magnetic medium needs eps_r = (c/v)^2 = 8.99 ~ 9", abs(epsr_h - 8.988) < 0.001, f"eps_r = {epsr_h:.4f}")
check("its eta = mu0 v = 40 pi = 125.66 ohm = eta0/3.00", abs(mu0 * 1e8 - 40 * np.pi) < 1e-9 and abs(eta0 / np.sqrt(epsr_h) - 125.66) < 0.01,
      f"mu0 v = {mu0*1e8:.4f}, eta0/sqrt(eps_r) = {eta0/np.sqrt(epsr_h):.4f}")
check("h repeats every 1 m in z and every 10 ns in t (1 m / 10 ns = 1e8 m/s)", abs(1 / (1e-8) - 1e8) < 1e-6)
# general rule for f(a t - b z), a, b > 0: speed a/b toward +z
a_, b_ = 3.0, 0.5
check("f(a t - b z) moves toward +z at a/b (a = 3, b = 0.5 -> 6 m/s)", np.allclose(velocity(a_, [0, 0, -b_]), [0, 0, 6]))
check("f(a t + b z) moves toward -z at a/b", np.allclose(velocity(a_, [0, 0, b_]), [0, 0, -6]))

# =====================================================================================
section("H. Shift identities (S25) and mirroring (section 6)")
vp = 100.0
E0 = lambda t: np.interp(t, [0, 1, 2, 4, 5], [0, 1, 1, 0, 0], left=0, right=0)   # S26 time history at z = 0
fwd = lambda z, t: E0(t - z / vp); bwd = lambda z, t: E0(t + z / vp)
fwd_t0 = lambda z: fwd(z, 0.0); bwd_t0 = lambda z: bwd(z, 0.0)
pts = [(150, 2.6), (-70, 0.9), (230, 3.3), (40, 1.7)]
check("+z: E(z,t) = E(0, t - z/v) = E(z - vt, 0)", all(abs(fwd(z, t) - fwd(0, t - z / vp)) < 1e-12 and abs(fwd(z, t) - fwd_t0(z - vp * t)) < 1e-12 for z, t in pts))
check("-z: E(z,t) = E(0, t + z/v) = E(z + vt, 0)", all(abs(bwd(z, t) - bwd(0, t + z / vp)) < 1e-12 and abs(bwd(z, t) - bwd_t0(z + vp * t)) < 1e-12 for z, t in pts))
check("forward check E(150, 2.6) = E(0, 1.1) = E(-110, 0) = 1", abs(fwd(150, 2.6) - 1) < 1e-12 and abs(fwd_t0(-110) - 1) < 1e-12)
zz = np.linspace(-500, 500, 1001)
check("+z wave: snapshot E(z,0) = E0(-z/v) is the time history mirrored", np.allclose(fwd(zz, 0), E0(-zz / vp)))
check("-z wave: snapshot E(z,0) = E0(+z/v) is the time history, not mirrored", np.allclose(bwd(zz, 0), E0(zz / vp)))

# =====================================================================================
section("I. Slide 26 moving waveform (-z at 100 m/s) (section 6 and figure wave-moving-waveform)")
cases = {"a": (200, 0.2, 0.9), "b": (-300, 3.4, 0.4), "c": (100, 0.6, 1.0)}
for k, (z, t, ans) in cases.items():
    arg = t + z / vp
    check(f"({k}) z = {z} m, t = {t} s: t + z/v = {arg:.1f} s -> E = {ans}", abs(bwd(z, t) - ans) < 1e-12, f"E = {bwd(z,t):.4f}")
for k, (z, t, ans) in cases.items():
    argw = t - z / vp
    check(f"({k}) wrong sign t - z/v = {argw:.1f} s -> 0 (off the pulse)", abs(E0(argw)) < 1e-12)
check("(a) on the falling ramp: 1 - 0.2/2 = 0.9", abs((1 - (2.2 - 2) / 2) - 0.9) < 1e-12)
snapz = [-100, 0, 50, 100, 200, 300, 400, 500]
s0 = [0, 0, 0.5, 1, 1, 0.5, 0, 0]; s1 = [0, 1, 1, 1, 0.5, 0, 0, 0]
check(f"snapshot t = 0 at z = {snapz}: {s0}", np.allclose([bwd(z, 0) for z in snapz], s0))
check(f"snapshot t = 1 s at the same z: {s1} (shifted 100 m toward -z)", np.allclose([bwd(z, 1) for z in snapz], s1))
check("t = 0 snapshot support: rises 0->1 on 0..100 m, flat to 200 m, back to 0 at 400 m",
      bwd(0, 0) == 0 and bwd(100, 0) == 1 and bwd(200, 0) == 1 and bwd(400, 0) == 0 and abs(bwd(300, 0) - 0.5) < 1e-12)
check("a probe at z = -300 m sees E0(t - 3 s): the same history 3 s later", all(abs(bwd(-300, t) - E0(t - 3)) < 1e-12 for t in np.linspace(0, 10, 41)))

# =====================================================================================
section("J. In matter, and on a cable (section 7); concept-page numbers")
for er, vexp, etaexp in ((4.0, c / 2, 188.37), (9.0, c / 3, 125.58), (2.25, c / 1.5, 251.15)):
    vv = 1 / np.sqrt(mu0 * er * eps0); ee = np.sqrt(mu0 / (er * eps0))
    check(f"eps_r = {er}: v = c/sqrt(eps_r) = {vv:.4e} m/s, eta = eta0/sqrt(eps_r) = {ee:.2f} ohm",
          abs(vv - vexp) < 1e-6 * vexp and abs(ee - etaexp) < 0.01)
check("eps_r = 4: v = 1.499e8 m/s; eta = 188.4 ohm (60 pi = 188.5)", abs(c / 2 - 1.499e8) < 0.0005e8 and abs(eta0 / 2 - 188.4) < 0.05 and abs(60 * np.pi - 188.5) < 0.05,
      f"{c/2:.4e}, {eta0/2:.3f}, {60*np.pi:.3f}")
check("eps_r = 2.25: v = 1.999e8 ~ 2.00e8 m/s, eta = 251.2 ohm", abs(c / 1.5 - 1.9986e8) < 0.0001e8 and abs(eta0 / 1.5 - 251.15) < 0.01)
mr, er = 2.0, 8.0
vv = 1 / np.sqrt(mr * mu0 * er * eps0); ee = np.sqrt(mr * mu0 / (er * eps0))
check("general: v = c/sqrt(mu_r eps_r), eta = eta0 sqrt(mu_r/eps_r) (mu_r = 2, eps_r = 8: c/4, eta0/2)", abs(vv - c / 4) < 1e-6 * c and abs(ee - eta0 / 2) < 1e-9)
check("general: eta = mu v = 1/(eps v) for (mu_r, eps_r) = (2, 8)", abs(mr * mu0 * vv - ee) < 1e-9 and abs(1 / (er * eps0 * vv) - ee) < 1e-6)
# coax of the Lecture 15 worked problem (a = 0.5 mm, b = 1.75 mm, eps_r = 2.25)
lnba = np.log(1.75 / 0.5)
Lp = mu0 / (2 * np.pi) * lnba; Cp = 2 * np.pi * 2.25 * eps0 / lnba
check("coax: 1/sqrt(L'C') = 1/sqrt(mu eps) = 2.00e8 m/s (the plane-wave speed)", abs(1 / np.sqrt(Lp * Cp) - c / 1.5) < 1e-6 * c, f"{1/np.sqrt(Lp*Cp):.5e}")
check("coax: sqrt(L'/C') = (eta/2pi) ln(b/a) = 50.1 ohm with eta = 251 ohm",
      abs(np.sqrt(Lp / Cp) - (eta0 / 1.5) / (2 * np.pi) * lnba) < 1e-9 and abs(np.sqrt(Lp / Cp) - 50.08) < 0.01, f"Z0 = {np.sqrt(Lp/Cp):.3f}")
check("geometric factor ln(3.5)/2pi = 0.199", abs(lnba / (2 * np.pi) - 0.199) < 0.0005, f"{lnba/(2*np.pi):.4f}")
check("parallel plates: sqrt(L'/C') = eta d/W (mu d/W over eps W/d)", abs(np.sqrt((mu0 * 0.002 / 0.01) / (2.25 * eps0 * 0.01 / 0.002)) - (eta0 / 1.5) * 0.2) < 1e-9)
# concept-page numbers
check("free space: E = 1 V/m travelling -> H = 1/eta0 = 2.654 mA/m", abs(1 / eta0 - 2.654e-3) < 0.0005e-3, f"{1/eta0*1e3:.4f} mA/m")
check("free space: B = mu0 H = E/c = 3.336 nT for E = 1 V/m", abs(mu0 / eta0 - 1 / c) < 1e-20 and abs(1 / c - 3.336e-9) < 0.0005e-9, f"{1/c:.4e} T")
check("units: mu/eps in (H/m)/(F/m) = H/F = (ohm s)/(s/ohm) = ohm^2 -> eta in ohm", True, "dimensional, by inspection")
check("instantaneous E x H = E^2/eta along u for a single travelling wave (L20 preview)", abs(np.dot(np.cross(3 * X, 3 / eta0 * Y), Z) - 9 / eta0) < 1e-15)
# lecture page section 5 example: E = y^ 1 V/m travelling toward -z -> H = (-z) x y / eta0 = +x 2.65 mA/m
Hex = np.cross(-Z, 1.0 * Y) / eta0
check("example: E = y (1 V/m) toward -z: H = (-z) x y / eta0 = +x 2.65 mA/m; check y x x = -z",
      np.allclose(Hex, X / eta0) and abs(Hex[0] * 1e3 - 2.654) < 0.001 and np.allclose(np.cross(Y, X), -Z), f"H = {Hex*1e3} mA/m")
check("tau = z/v in vacuum: 1 m <-> 3.34 ns", abs(1 / c * 1e9 - 3.34) < 0.005)
# intrinsic-impedance page trap: with both waves present, Ex/Hy = eta (Af + Bg)/(Af - Bg)
fz, gz = f(t0 - z0 / v), gb(t0 + z0 / v)
check("superposition: Ex/Hy = eta (Af + Bg)/(Af - Bg) (not +-eta)", abs(r_mix - eta * (A_ * fz + B_ * gz) / (A_ * fz - B_ * gz)) < 1e-9 * abs(r_mix),
      f"{r_mix:.4f} vs {eta*(A_*fz+B_*gz)/(A_*fz-B_*gz):.4f}")
check("(mu_r, eps_r) = (2, 8): eta = eta0/2 = 188.4 ohm, the same as eps_r = 4 alone; speed c/4 = half of c/2",
      abs(ee - 188.37) < 0.01 and abs(vv / (c / 2) - 0.5) < 1e-12)
check("120 pi approximates eta0 to 0.07 %", abs((120 * np.pi - eta0) / eta0 * 100 - 0.07) < 0.005)

# =====================================================================================
section("K. Worked problem 'A pulse on the move' (eps_r = 2.25 non-magnetic; travel along +y; E along z)")
vP = 200.0          # m/us
t1 = 3.0            # us
def E_t1(y):        # given profile at t = 3 us, V/m
    y = np.asarray(y, float)
    return np.where((y > 400) & (y < 700), 0.02 * (y - 400), 0.0)
def E_yt(y, t):     # rigid translation toward +y
    return E_t1(np.asarray(y, float) - vP * (t - t1))
def E_formula(y, t):  # part (b) closed form, y in m, t in us
    y = np.asarray(y, float); arg = y - 200 * t
    return np.where((arg > -200) & (arg < 100), 0.02 * (arg + 200), 0.0)
def F(s):           # d'Alembert waveform: E_z = F(t - y/v), s in us
    s = np.asarray(s, float)
    return np.where((s > -0.5) & (s < 1.0), 4 * (1 - s), 0.0)
yy = np.linspace(-1500, 2500, 8001); tt = np.linspace(-2, 10, 49)
check("given profile: 0 at y = 400 m rising to 6 V/m at y = 700 m (front), zero elsewhere", abs(E_t1(699.999) - 6) < 1e-3 and E_t1(400.0001) < 1e-5 and E_t1(701) == 0 and E_t1(399) == 0)
check("(a) E(y,0) = E(y + 600, 3 us): 0.02(y + 200) on -200 < y < 100 m", np.allclose(E_yt(yy, 0), np.where((yy > -200) & (yy < 100), 0.02 * (yy + 200), 0)))
check("(a) at t = 0: front (6 V/m) at y = 100 m, back (0) at y = -200 m", abs(E_yt(99.999, 0) - 6) < 1e-3 and E_yt(-199.999, 0) < 1e-4)
check("(a) wrong-way shift E(y - 600, 3 us) would put the pulse on 1000 < y < 1300 m", np.allclose(E_t1(yy - 600), np.where((yy > 1000) & (yy < 1300), 0.02 * (yy - 1000), 0)))
check("(b) closed form 0.02(y - 200t + 200)[u(y - 200t + 200) - u(y - 200t - 100)] equals the translated profile",
      all(np.allclose(E_formula(yy, t), E_yt(yy, t)) for t in tt))
check("(b) d'Alembert form: E_z = F(t - y/v), F(s) = 4(1 - s) on -0.5 < s < 1 us", all(np.allclose(F(t - yy / vP), E_yt(yy, t)) for t in tt))
check("(b) F(-0.5) = 6 (front), F(1) = 0 (back); duration 1.5 us = 300 m / (200 m/us)", abs(4 * (1 + 0.5) - 6) < 1e-12 and abs(300 / vP - 1.5) < 1e-12)
th0 = np.linspace(-2, 3, 50001)
rec0 = E_yt(0.0, th0)
check("(b) a probe at y = 0 records F(t): front passes at t = -0.5 us (6 V/m), back at t = 1 us",
      abs(th0[np.argmax(rec0 > 0)] + 0.5) < 2e-4 and abs(th0[np.nonzero(rec0 > 0)[0][-1]] - 1.0) < 2e-4 and abs(rec0[np.argmax(rec0 > 0)] - 6) < 1e-3)
check("(b) y - 200t + 200 = 200(1 - s) with s = t - y/200", all(abs((y - 200 * t + 200) - 200 * (1 - (t - y / 200))) < 1e-9 for y, t in ((37.0, 1.3), (-150.0, -0.2), (999.0, 5.5))))
th = np.linspace(0, 10, 10001)
hist = E_yt(1000.0, th)
check("(c) at y = 1 km: E = 4(6 - t) V/m for 4.5 < t < 6 us, zero otherwise", np.allclose(hist, np.where((th > 4.5) & (th < 6), 4 * (6 - th), 0)))
check("(c) the front arrives at t = 4.5 us (y = 100 + 200t = 1000), the back leaves at 6 us (-200 + 200t = 1000)", abs((1000 - 100) / 200 - 4.5) < 1e-12 and abs((1000 + 200) / 200 - 6) < 1e-12)
check("(c) probe reading at y = 1 km, t = 5 us: 4 V/m", abs(E_yt(1000.0, 5.0) - 4) < 1e-12, f"{E_yt(1000.0, 5.0):.4f}")
check("(c) time history is the snapshot mirrored (+y travel): jump first, then falling ramp",
      abs(E_yt(1000, 4.5001) - 6) < 1e-3 and E_yt(1000, 5.99) < 0.05 and E_t1(699.9) > E_t1(400.1))
check("(c) snapshot at t = 5 us: 0.02(y - 800) on 800 < y < 1100 m, value at 1000 m = 4", abs(E_yt(1000.0, 5) - 0.02 * 200) < 1e-12 and abs(E_yt(1099.99, 5) - 6) < 1e-3)
v_SI = vP * 1e6
epsr_P = (c / v_SI) ** 2
check("(d) v = 200 m/us = 2.0e8 m/s; eps_r = (c/v)^2 = 2.247 ~ 2.25", abs(v_SI - 2e8) < 1 and abs(epsr_P - 2.247) < 0.001, f"eps_r = {epsr_P:.4f}")
check("(d) with c ~ 3e8: eps_r = 2.25 exactly", abs((3e8 / v_SI) ** 2 - 2.25) < 1e-12)
check("(d) shape and peak preserved: the 6 V/m front is 6 V/m at t = 0, 3, 4.5 us (no attenuation)",
      all(abs(E_yt(100 + 200 * t - 1e-3, t) - 6) < 1e-3 for t in (0, 3, 4.5)))
etaP = mu0 * v_SI
check("(e) eta = mu0 v = 80 pi = 251.3 ohm (= eta0/sqrt(eps_r))", abs(etaP - 80 * np.pi) < 1e-9 and abs(etaP - eta0 / np.sqrt(epsr_P)) < 1e-6 and abs(etaP - 251.3) < 0.05, f"eta = {etaP:.4f}")
check("(e) eta with eps_r rounded to 2.25: eta0/1.5 = 251.2 ohm (same to 0.1%)", abs(eta0 / 1.5 - 251.15) < 0.01 and abs(eta0 / 1.5 / etaP - 1) < 1e-3)
uP = Y; Ehat = Z
Hhat = np.cross(uP, Ehat)
check("(e) H direction: (1/eta) u x E = y x z = +x", np.allclose(Hhat, X), f"{Hhat}")
check("(e) check: E x H = z x x = +y (direction of travel)", np.allclose(np.cross(Ehat, X), Y))
check("(e) peak H = 6/eta = 23.9 mA/m", abs(6 / etaP - 0.02387) < 0.00001, f"{6/etaP*1e3:.3f} mA/m")
check("(e) H_x = F/eta = (1/(20 pi))(1 - s) A/m = 15.9(1 - s) mA/m", abs(4 / etaP - 1 / (20 * np.pi)) < 1e-12 and abs(4 / etaP * 1e3 - 15.92) < 0.01)
check("(e) slope: 0.02/eta = 7.96e-5 A/m per m", abs(0.02 / etaP - 7.96e-5) < 0.005e-5, f"{0.02/etaP:.4e}")
check("(e) peak B = mu0 H = E/v = 3.0e-8 T = 30 nT", abs(mu0 * 6 / etaP - 6 / v_SI) < 1e-20 and abs(6 / v_SI - 3e-8) < 1e-15)
check("(e) trap: using eta0 gives 6/376.7 = 15.9 mA/m (wrong medium)", abs(6 / eta0 * 1e3 - 15.93) < 0.01)
# Maxwell check of the problem's fields at interior points (SI units), with a smoothed copy of the edges irrelevant there
mud, epsd = mu0, epsr_P * eps0
EzP = lambda x, y, z, t: np.array([0.0, 0.0, float(F((t * 1e6) - y / vP))])     # t in s, y in m
HxP = lambda x, y, z, t: np.array([float(F((t * 1e6) - y / vP)) / etaP, 0.0, 0.0])
for (yq, tq) in ((1000.0, 5.0e-6), (950.0, 5.2e-6), (300.0, 1.4e-6)):
    p = (0.0, yq, 0.0, tq)
    hyy = 0.01; htt = hyy / v_SI
    cE = curl(EzP, p, hyy); dHt = (HxP(0, yq, 0, tq + htt) - HxP(0, yq, 0, tq - htt)) / (2 * htt)
    cH = curl(HxP, p, hyy); dEt = (EzP(0, yq, 0, tq + htt) - EzP(0, yq, 0, tq - htt)) / (2 * htt)
    check(f"(e) problem fields at y = {yq} m, t = {tq*1e6} us: Faraday and Ampere-Maxwell hold, div = 0",
          np.allclose(cE, -mud * dHt, rtol=1e-6, atol=1e-12) and np.allclose(cH, epsd * dEt, rtol=1e-6, atol=1e-18)
          and abs(div(EzP, p, hyy)) < 1e-9 and abs(div(HxP, p, hyy)) < 1e-12,
          f"(curlE)_x = {cE[0]:.4e}, -mu dHx/dt = {-mud*dHt[0]:.4e}")
# -y variant
E_var = lambda y, t: E_t1(np.asarray(y, float) + vP * (t - t1))
check("variant (-y travel): E(y,0) = E(y - 600, 3 us) occupies 1000 < y < 1300 m", np.allclose(E_var(yy, 0), np.where((yy > 1000) & (yy < 1300), 0.02 * (yy - 1000), 0)))
hist_v = E_var(1000.0, th)
check("variant: at y = 1 km the history is 4t V/m for 0 < t < 1.5 us (same shape as the snapshot: not mirrored)",
      np.allclose(hist_v, np.where((th > 0) & (th < 1.5), 4 * th, 0)))
check("variant: H = (1/eta)(-y) x z E = -x E/eta", np.allclose(np.cross(-Y, Z), -X))

# =====================================================================================
section("L. Figure geometry (figs_l18.py), screen frame X right, Y up, Z out of the screen")
# wave-eh-triads: projection of physics axes in the drawing: x up, z right, y out of page (drawn down-left)
for name, Ehat, Hhat, uhat in rows:
    Es = Ehat[0] * sx + Ehat[1] * sy + Ehat[2] * sz
    Hs = Hhat[0] * sx + Hhat[1] * sy + Hhat[2] * sz
    us = uhat[0] * sx + uhat[1] * sy + uhat[2] * sz
    check(f"triad {name}: E x H in the screen frame = {np.cross(Es, Hs)} = drawn travel arrow {us}", np.allclose(np.cross(Es, Hs), us))
# pulse figure: time history f(t) = (t/a) e^(1 - t/a), a = 0.5 ns, peak at t = a; front positions after 8 ns at c
a = 0.5e-9
fT = lambda t: np.where(t > 0, (t / a) * np.exp(1 - t / a), 0.0)
check("pulse-figure waveform peaks at t = a with value 1", abs(fT(a) - 1) < 1e-12 and fT(0.9 * a) < 1 and fT(1.1 * a) < 1)
check("pulse-figure waveform negligible after 4 ns (< 0.01)", fT(4e-9) < 0.01, f"f(4 ns) = {float(fT(4e-9)):.4f}")
check("pulse figure: in 8 ns at c the front moves 2.40 m", abs(c * 8e-9 - 2.398) < 0.001, f"{c*8e-9:.4f} m")
check("pulse figure: a 4 ns pulse is 1.20 m long at c", abs(c * 4e-9 - 1.199) < 0.001)
zf = np.linspace(-3, 3, 6001)
snap_p = fT(8e-9 - zf / c); snap_m = fT(8e-9 + zf / c)
check("+z snapshot at 8 ns: front (steep edge) at z = +2.40 m, tail toward -z", abs(zf[np.argmax(snap_p > 0)] - 2.398) > 1.0 and abs(zf[np.nonzero(snap_p > 0)[0][-1]] - 2.398) < 0.002)
check("-z snapshot at 8 ns: front (steep edge) at z = -2.40 m, tail toward +z", abs(zf[np.nonzero(snap_m > 0)[0][0]] + 2.398) < 0.002)
check("+z snapshot = time history mirrored; -z snapshot = time history (same orientation)",
      np.allclose(fT(-zf / c), fT(-zf / c)) and zf[np.argmax(fT(-zf / c))] < 0 and zf[np.argmax(fT(zf / c))] > 0)

print("\n" + "-" * 100)
print(f"TOTAL: {NP} PASS, {NF} FAIL")
