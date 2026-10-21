#!/usr/bin/env python3
"""L27 practice checks: guided TEM waves on transmission lines (numpy + scipy only).

Every number, sign and direction on practice/27-transmission-line-basics.md is printed here.
Line parameters from the geometrical factor and again from the field definitions; signs of
surface charge and current by n.D and n x H with np.cross; telegrapher's-equation derivatives by
finite differences; power by quadrature of the Poynting vector; moving waves checked by an
independent solver (spectral exact propagator or FDTD of the telegrapher's equations); the LC
ladder by integrating its circuit ODEs; the coax curl reduction by finite-difference curls of the
full 3-D fields. Course constants: eps0 = 1e-9/36pi, c = 3e8, eta0 = 120pi.
"""
import numpy as np
from scipy import integrate

mu0 = 4e-7 * np.pi
eps0 = 1e-9 / (36 * np.pi)          # course value
c = 1 / np.sqrt(mu0 * eps0)          # 3e8 exactly
eta0 = np.sqrt(mu0 / eps0)           # 120 pi exactly
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


def plates(W, d, er=1.0, mur=1.0):
    GF = W / d
    eps, mu = er * eps0, mur * mu0
    L, C = mu / GF, eps * GF
    return dict(GF=GF, L=L, C=C, v=1 / np.sqrt(L * C), Z0=np.sqrt(L / C), eta=np.sqrt(mu / eps))


# ---------------------------------------------------------------------------
hdr("27.1 Strip-line parameters: W = 6 mm, d = 0.5 mm, er = 2.25")
p = plates(6e-3, 0.5e-3, 2.25)
print(f"  GF = {p['GF']:.4f}; eta = {p['eta']:.4f} = {p['eta']/np.pi:.4f} pi")
print(f"  L = {p['L']*1e9:.4f} nH/m, C = {p['C']*1e12:.4f} pF/m, v = {p['v']:.6e}, Z0 = {p['Z0']:.4f} ohm")
close("L = mu0/12", p['L'], mu0 / 12)
close("C = 27 eps0 = 0.75e-9/pi", p['C'], 0.75e-9 / np.pi)
close("v = 2e8", p['v'], 2e8)
close("Z0 = 20pi/3", p['Z0'], 20 * np.pi / 3)
close("Z0 = L v (second route)", p['L'] * p['v'], p['Z0'])
print(f"  delay over 0.30 m = {0.30/p['v']*1e9:.4f} ns")
close("delay 1.5 ns", 0.30 / p['v'], 1.5e-9)
Wd50 = p['eta'] / 50
print(f"  W/d for 50 ohm = {Wd50:.4f}; W = {Wd50*0.5:.4f} mm")
close("W/d = 80pi/50", Wd50, 80 * np.pi / 50)
close("check Z0 of new width", plates(Wd50 * 0.5e-3, 0.5e-3, 2.25)['Z0'], 50)

# ---------------------------------------------------------------------------
hdr("27.2 True/false on the telegrapher's equations")
# (c) V/I of a sum of waves is not constant
Z0, v = 50.0, 2e8
f = lambda s: np.exp(-(s / 1e-9) ** 2)
g = lambda s: 0.5 * np.exp(-((s - 2.5e-9) / 0.7e-9) ** 2)
zz, tt = np.array([0.0, 0.1, 0.3]), 1e-9
V = f(tt - zz / v) + g(tt + zz / v)
I = (f(tt - zz / v) - g(tt + zz / v)) / Z0
print(f"  V/I for f+g at z = 0, 0.1, 0.3 m: {np.round(V/I, 3)}")
check("(c) V/I of a sum varies with z (False)", np.ptp(V / I) > 1)
Vb = g(tt + zz / v); Ib = -g(tt + zz / v) / Z0
close("(d) backward wave V/I = -Z0 (True)", Vb / Ib, -Z0 * np.ones(3))
# (e) coax in air, thinner inner conductor
for a in (1e-3, 0.5e-3):
    b = 3.5e-3
    Lc = mu0 / (2 * np.pi) * np.log(b / a); Cc = 2 * np.pi * eps0 / np.log(b / a)
    print(f"  air coax a = {a*1e3} mm, b = 3.5 mm: Z0 = {np.sqrt(Lc/Cc):.3f} ohm, v = {1/np.sqrt(Lc*Cc):.6e}")
check("(e) v unchanged, Z0 rises when a shrinks (statement False)", True)
# (b) series L / shunt C gives the telegrapher's equations; the swapped ladder does not
# swapped: series C, shunt L -> dispersion w = 1/(sqrt(LC) * 2 sin(k dz/2)) ... high-pass; check low-k slope
dz, Lp, Cp = 1e-3, 250e-9, 100e-12
k = np.array([1.0, 2.0, 4.0])
w_LC = 2 / np.sqrt(Lp * dz * Cp * dz) * np.sin(k * dz / 2)          # series L, shunt C
w_CL = 1 / (2 * np.sqrt(Lp * dz * Cp * dz) * np.sin(k * dz / 2))    # series C, shunt L
print(f"  series-L ladder w/k = {np.round(w_LC/k, 1)} (constant); series-C ladder w/k = {np.round(w_CL/k, 1)}")
check("(b) only series-L/shunt-C ladder is non-dispersive at low k", np.ptp(w_LC / k) / 2e8 < 1e-4 and np.ptp(w_CL / k) > 1e8)
kall = np.linspace(1e-3, np.pi / dz, 2000)
w_CL_all = 1 / (2 * np.sqrt(Lp * dz * Cp * dz) * np.sin(kall * dz / 2))
print(f"  swapped ladder passes only w >= {w_CL_all.min():.4e} rad/s = 1/(2 sqrt(L1 C1)) = {1/(2*np.sqrt(Lp*dz*Cp*dz)):.4e} (high-pass)")
close("swapped ladder lowest passband frequency", w_CL_all.min(), 1 / (2 * np.sqrt(Lp * dz * Cp * dz)), rtol=1e-6)

# ---------------------------------------------------------------------------
hdr("27.3 Plates on y = 0 and y = d; E = y E0 cos(wt - beta z)")
eta, E0, eps = 377.0, 1.0, 2 * eps0
E = E0 * Y
H = np.cross(Z, E) / eta
print(f"  H direction = {H/np.linalg.norm(H)} (expect -x)")
close("H = -x E0/eta", H, -X * E0 / eta)
close("E x H along +z", np.cross(E, H) / np.linalg.norm(np.cross(E, H)), Z)
n0, nd = Y, -Y
rho0, rhod = np.dot(n0, eps * E), np.dot(nd, eps * E)
J0, Jd = np.cross(n0, H), np.cross(nd, H)
print(f"  y=0: rho_s = {rho0:+.3e} (positive), J_s dir = {J0/np.linalg.norm(J0)}")
print(f"  y=d: rho_s = {rhod:+.3e} (negative), J_s dir = {Jd/np.linalg.norm(Jd)}")
check("(a),(b) false: y=0 positive, y=d negative", rho0 > 0 and rhod < 0)
close("(c) true: J_s on y=d along -z", Jd / np.linalg.norm(Jd), -Z)
close("y=0 plate J_s along +z", J0 / np.linalg.norm(J0), Z)
check("(e) false: J_s perpendicular to H", abs(np.dot(Jd, H)) < 1e-15)
# (d) path independence: B_z = 0 so circulation in a z = const plane vanishes; H has no z component
check("(d) false: H_z = 0 (B_z = 0)", H[2] == 0)

# ---------------------------------------------------------------------------
hdr("27.4 Find the error: power on an air plate line W = 1.5 cm, d = 1 mm, V = 10 V")
p = plates(1.5e-2, 1e-3)
V0 = 10.0
P_student = V0**2 / (2 * eta0)
P = V0**2 / (2 * p['Z0'])
print(f"  Z0 = {p['Z0']:.4f} = {p['Z0']/np.pi:.4f} pi ohm")
print(f"  student P = {P_student:.4f} W; correct P = {P:.4f} W; ratio = {P/P_student:.4f}")
close("Z0 = 8 pi", p['Z0'], 8 * np.pi)
close("P = 100/(16 pi)", P, 100 / (16 * np.pi))
close("student 100/(240pi)", P_student, 100 / (240 * np.pi))
Ex = V0 / 1e-3; Hy = Ex / eta0
S = 0.5 * Ex * Hy
print(f"  E = {Ex:.1f} V/m, H = {Hy:.4f} A/m, <S> = {S/1e3:.4f} kW/m^2, <S> W d = {S*1.5e-5:.4f} W")
close("<S> W d = P", S * 1.5e-5, P)
close("I = V/Z0 = H W", V0 / p['Z0'], Hy * 1.5e-2)
print(f"  I = {V0/p['Z0']:.4f} A")
# quadrature time average of v i
w = 2 * np.pi * 1e8
avg = integrate.quad(lambda t: (V0 * np.cos(w * t)) * (V0 / p['Z0'] * np.cos(w * t)), 0, 2 * np.pi / w)[0] * w / (2 * np.pi)
close("quadrature <v i>", avg, P)

# ---------------------------------------------------------------------------
hdr("27.5 Datasheet: L = 0.4 uH/m, C = 40 pF/m")
L, C = 0.4e-6, 40e-12
v = 1 / np.sqrt(L * C); Z0 = np.sqrt(L / C); er = (c / v) ** 2; eta = eta0 / np.sqrt(er)
print(f"  v = {v:.6e}, Z0 = {Z0:.4f}, er = {er:.6f}, eta = {eta:.4f} = {eta/np.pi:.4f} pi")
close("v = 2.5e8", v, 2.5e8); close("Z0 = 100", Z0, 100); close("er = 1.44", er, 1.44)
close("eta = 100 pi", eta, 100 * np.pi)
print(f"  delay 10 m = {10/v*1e9:.4f} ns")
close("40 ns", 10 / v, 40e-9)
lnba = 2 * np.pi * Z0 / eta; ach = np.pi * Z0 / eta
print(f"  coax ln(b/a) = {lnba:.6f}, b/a = {np.exp(lnba):.4f}; twin acosh(D/2a) = {ach:.6f}, D/2a = {np.cosh(ach):.4f}")
close("ln(b/a) = 2", lnba, 2); close("acosh = 1", ach, 1)
# second route: geometry back to L and C
Lco = mu0 / (2 * np.pi) * lnba; Cco = 2 * np.pi * er * eps0 / lnba
close("coax L, C from b/a", [Lco, Cco], [L, C])
Ltw = mu0 / np.pi * ach; Ctw = np.pi * er * eps0 / ach
close("twin-lead L, C from D/2a", [Ltw, Ctw], [L, C])
close("LC = mu eps", L * C, mu0 * er * eps0, rtol=1e-9, atol=0)
print(f"  LC = {L*C:.4e} s^2/m^2 = mu0 * 1.44 eps0 = {mu0*1.44*eps0:.4e}; coax L back = {Lco*1e6:.4f} uH/m")

# ---------------------------------------------------------------------------
hdr("27.6 Reading a line: V = 12 cos(1e9 t + 5 z), I = -0.2 cos(1e9 t + 5 z)")
w, b = 1e9, 5.0
Vf = lambda z, t: 12 * np.cos(w * t + b * z)
If = lambda z, t: -0.2 * np.cos(w * t + b * z)
print(f"  direction: phase w t + b z const -> dz/dt = -w/b = {-w/b:.3e} (toward -z)")
close("v = 2e8", w / b, 2e8)
h, ht = 1e-6, 1e-15
Ls, Cs = [], []
for (z, t) in [(0.1, 0.3e-9), (0.37, 1.1e-9), (1.3, 2.2e-9)]:
    dVdz = (Vf(z + h, t) - Vf(z - h, t)) / (2 * h)
    dIdt = (If(z, t + ht) - If(z, t - ht)) / (2 * ht)
    dIdz = (If(z + h, t) - If(z - h, t)) / (2 * h)
    dVdt = (Vf(z, t + ht) - Vf(z, t - ht)) / (2 * ht)
    Ls.append(-dVdz / dIdt); Cs.append(-dIdz / dVdt)
print(f"  L from FD = {np.round(np.array(Ls)*1e9, 4)} nH/m; C from FD = {np.round(np.array(Cs)*1e12, 4)} pF/m")
print("  -dV/dz = 60 sin(psi), dI/dt = 2e8 sin(psi), -dI/dz = -1 sin(psi), dV/dt = -1.2e10 sin(psi)")
psi = 1e9 * 0.3e-9 + 5 * 0.1
close("FD coefficients", [-(Vf(0.1 + h, 0.3e-9) - Vf(0.1 - h, 0.3e-9)) / (2 * h) / np.sin(psi), (If(0.1, 0.3e-9 + ht) - If(0.1, 0.3e-9 - ht)) / (2 * ht) / np.sin(psi), -(If(0.1 + h, 0.3e-9) - If(0.1 - h, 0.3e-9)) / (2 * h) / np.sin(psi), (Vf(0.1, 0.3e-9 + ht) - Vf(0.1, 0.3e-9 - ht)) / (2 * ht) / np.sin(psi)], [60, 2e8, -1, -1.2e10], rtol=1e-5)
close("L = 300 nH/m", np.array(Ls), 300e-9 * np.ones(3), rtol=1e-5)
close("C = 83.33 pF/m", np.array(Cs), 1 / 1.2e10 * np.ones(3), rtol=1e-5)
L, C = 300e-9, 1 / 1.2e10
close("Z0 = sqrt(L/C) = 60", np.sqrt(L / C), 60)
close("V/I = -60 (backward)", 12 / -0.2, -60)
close("v = 1/sqrt(LC)", 1 / np.sqrt(L * C), 2e8)
print(f"  LC = {L*C:.4e} s^2/m^2; p = VI = -2.4 cos^2(psi): amplitude product {12*-0.2}")
print(f"  er = {(c*np.sqrt(L*C))**2:.6f}")
close("er = 2.25", (c * np.sqrt(L * C)) ** 2, 2.25)
T = 2 * np.pi / w
Pav = integrate.quad(lambda t: Vf(0.2, t) * If(0.2, t), 0, T)[0] / T
print(f"  <VI> = {Pav:.6f} W")
close("<P> = -1.2 W", Pav, -1.2)
close("phasor 1/2 Re{V I*}", 0.5 * (12 * -0.2), -1.2)

# ---------------------------------------------------------------------------
hdr("27.7 Two bench measurements: 20 m, C = 1.6 nF, G = 2 nS, delay 100 ns")
ell = 20.0
Cp = 1.6e-9 / ell; Gp = 2e-9 / ell; v = ell / 100e-9
er = (c / v) ** 2
Lp = 1 / (Cp * v**2); Z0 = 1 / (Cp * v)
print(f"  C' = {Cp*1e12:.4f} pF/m, v = {v:.4e}, er = {er:.6f}, L' = {Lp*1e9:.4f} nH/m, Z0 = {Z0:.4f}")
close("C' = 80 pF/m", Cp, 80e-12); close("v = 2e8", v, 2e8); close("er = 2.25", er, 2.25)
close("L' = 312.5 nH/m", Lp, 312.5e-9); close("Z0 = 62.5", Z0, 62.5)
close("Z0 = sqrt(L/C)", np.sqrt(Lp / Cp), 62.5)
close("L'C' = mu0 eps", Lp * Cp, mu0 * er * eps0, rtol=1e-9, atol=0)
print(f"  L'C' = {Lp*Cp:.4e} s^2/m^2; L'/C' = {Lp/Cp:.1f} -> sqrt = {np.sqrt(Lp/Cp):.2f}")
lam = v / 1e3
print(f"  lambda at 1 kHz = {lam/1e3:.1f} km; ell/lambda = {ell/lam:.2e}")
sig = er * eps0 * Gp / Cp
print(f"  G' = {Gp*1e9:.4f} nS/m, sigma = eps G'/C' = {sig:.4e} S/m")
close("G' = 0.1 nS/m", Gp, 1e-10)
close("sigma = 2.49e-11", sig, 2.25 * eps0 * 1e-10 / 80e-12)
print(f"  G'/(w C') at 1 kHz = {Gp/(2*np.pi*1e3*Cp):.3e}")
# lumped check: input admittance of an open lossy line at 1 kHz vs j w C ell + G ell
wq = 2 * np.pi * 1e3
gam = np.sqrt((1j * wq * Lp) * (Gp + 1j * wq * Cp)); Zc = np.sqrt(1j * wq * Lp / (Gp + 1j * wq * Cp))
Yin = np.tanh(gam * ell) / Zc
print(f"  exact Y_in = {Yin:.6e}; lumped G + jwC = {2e-9 + 1j*wq*1.6e-9:.6e}")
close("open line at 1 kHz = lumped G + j w C", Yin, 2e-9 + 1j * wq * 1.6e-9, rtol=1e-6)

# ---------------------------------------------------------------------------
hdr("27.8 Artificial line: 30 sections, L1 = 0.5 uH, C1 = 200 pF")
L1, C1, N = 0.5e-6, 200e-12, 30
Z0 = np.sqrt(L1 / C1); tau1 = np.sqrt(L1 * C1)
print(f"  Z0 = {Z0:.4f} ohm, per-section delay = {tau1*1e9:.4f} ns, total = {N*tau1*1e9:.2f} ns")
close("Z0 = 50", Z0, 50); close("tau1 = 10 ns", tau1, 10e-9); close("total 300 ns", N * tau1, 300e-9)
print(f"  coax length (v = 2e8) = {N*tau1*2e8:.2f} m")
close("60 m", N * tau1 * 2e8, 60)
V0 = 2.0
print(f"  step current V0/Z0 = {V0/Z0*1e3:.3f} mA; charge-rate check C1 V0/tau1 = {C1*V0/tau1*1e3:.3f} mA")
close("40 mA both ways", [V0 / Z0, C1 * V0 / tau1], [0.04, 0.04])
print(f"  charge per capacitor C1 V0 = {C1*V0*1e12:.1f} pC every {tau1*1e9:.1f} ns")
print(f"  f_max (10 sections per wavelength) = {1/(10*tau1)/1e6:.3f} MHz")
close("10 MHz", 1 / (10 * tau1), 10e6)
# ODE: ideal source with smooth ramp (rise ~ 100 ns) into ladder, matched 50 ohm load at the end
trise = 100e-9
src = lambda t: V0 * 0.5 * (1 + np.tanh((t - 150e-9) / (trise / 4)))
# state: i_k (k=0..N-1) inductor currents, v_k (k=0..N-1) capacitor voltages (after inductor k)
def rhs(t, y):
    i, vv = y[:N], y[N:]
    vin = np.concatenate([[src(t)], vv[:-1]])
    di = (vin - vv) / L1
    iout = np.concatenate([i[1:], [vv[-1] / Z0]])
    dv = (i - iout) / C1
    return np.concatenate([di, dv])
sol = integrate.solve_ivp(rhs, (0, 900e-9), np.zeros(2 * N), max_step=0.5e-9, rtol=1e-8, atol=1e-12, dense_output=True)
ts = np.linspace(0, 900e-9, 90001)
vout = sol.sol(ts)[2 * N - 1]
vin_ = src(ts)
t_half_in = ts[np.argmax(vin_ >= V0 / 2)]; t_half_out = ts[np.argmax(vout >= V0 / 2)]
print(f"  ladder ODE: half-amplitude delay source->section 30 = {(t_half_out - t_half_in)*1e9:.2f} ns")
check("ODE delay within 2% of 300 ns", abs((t_half_out - t_half_in) - 300e-9) < 6e-9)
i0 = sol.sol(np.array([200e-9]))[0][0]
print(f"  ladder ODE: source current at t = 200 ns = {i0*1e3:.3f} mA vs src/Z0 = {src(200e-9)/Z0*1e3:.3f} mA")
check("source current = V/Z0 within 2%", abs(i0 - src(200e-9) / Z0) < 0.02 * src(200e-9) / Z0)
print(f"  final output = {vout[-1]:.4f} V (matched: equals V0)")

# ---------------------------------------------------------------------------
hdr("27.9 Coax (SP19 E3 #2 style): a = 0.4 mm, ln(b/a) = 5/3, er = 4")
a = 0.4e-3; lnba = 5 / 3; b = a * np.exp(lnba); er = 4.0; eps = er * eps0
GF = 2 * np.pi / lnba
L = mu0 / GF; C = eps * GF; v = 1 / np.sqrt(L * C); Z0 = np.sqrt(L / C); eta = eta0 / 2
print(f"  b = {b*1e3:.4f} mm, GF = {GF:.4f}, L = {L*1e9:.4f} nH/m, C = {C*1e12:.4f} pF/m, v = {v:.4e}, Z0 = {Z0:.4f}")
close("L = 1/3 uH/m", L, 1e-6 / 3); close("C = 2/15 nF/m", C, 2e-9 / 15)
close("v = 1.5e8", v, 1.5e8); close("Z0 = 50", Z0, 50); close("Z0 = eta/GF", eta / GF, 50)
# (b) +z current on OUTER conductor, forward pulse
I = -0.3; V = Z0 * I
print(f"  I (inner, +z) = {I} A; V = Z0 I = {V} V")
close("V = -15", V, -15)
Er = lambda r: V / (r * lnba); Hphi = lambda r: I / (2 * np.pi * r)
print(f"  E_r = {V/lnba:.4f}/r V/m; E_r(a) = {Er(a)/1e3:.4f} kV/m, E_r(b) = {Er(b)/1e3:.4f} kV/m")
print(f"  H_phi = {I/(2*np.pi):.6f}/r A/m; H_phi(a) = {Hphi(a):.4f}, H_phi(b) = {Hphi(b):.4f} A/m")
close("E_r = -9/r", V / lnba, -9)
close("H_phi coefficient -0.0477", I / (2 * np.pi), -0.3 / (2 * np.pi))
close("V = int_a^b E_r dr", integrate.quad(Er, a, b)[0], V)
# direction at a point on +x axis: r_hat = x, phi_hat = y
Evec = Er(1e-3) * X; Hvec = Hphi(1e-3) * Y
close("E x H along +z", np.cross(Evec, Hvec) / np.linalg.norm(np.cross(Evec, Hvec)), Z)
# surface charge and current with n into the gap
rho_a = np.dot(X, eps * Er(a) * X); rho_b = np.dot(-X, eps * Er(b) * X)
Js_a = np.cross(X, Hphi(a) * Y); Js_b = np.cross(-X, Hphi(b) * Y)
print(f"  rho_s(a) = {rho_a*1e6:.4f} uC/m^2, rho_s(b) = {rho_b*1e6:.4f} uC/m^2")
print(f"  per metre: inner {2*np.pi*a*rho_a*1e9:.4f} nC/m, outer {2*np.pi*b*rho_b*1e9:.4f} nC/m; C V = {C*V*1e9:.4f} nC/m")
close("inner charge per m = C V", 2 * np.pi * a * rho_a, C * V)
close("outer charge per m = -C V", 2 * np.pi * b * rho_b, -C * V)
print(f"  J_s(a) = {Js_a} A/m -> total {2*np.pi*a*Js_a[2]:.4f} A along z; J_s(b) total {2*np.pi*b*Js_b[2]:.4f} A along z")
close("outer conductor carries +0.3 A along +z", 2 * np.pi * b * Js_b[2], 0.3)
close("inner conductor carries -0.3 A", 2 * np.pi * a * Js_a[2], -0.3)
# (c) Poynting integral
P = integrate.quad(lambda r: Er(r) * Hphi(r) * 2 * np.pi * r, a, b)[0]
print(f"  Poynting integral = {P:.6f} W; VI = {V*I:.6f} W; energy in 4 ns = {P*4e-9*1e9:.4f} nJ; length v T = {v*4e-9:.3f} m")
close("P = 4.5 W", P, 4.5); close("P = VI", P, V * I); close("energy 18 nJ", P * 4e-9, 18e-9)
close("closed form 9*0.3*ln(b/a)", 9 * 0.3 * lnba, 4.5)
# stored energy per metre x v = P
We = integrate.quad(lambda r: 0.5 * eps * Er(r)**2 * 2 * np.pi * r, a, b)[0]
Wm = integrate.quad(lambda r: 0.5 * mu0 * Hphi(r)**2 * 2 * np.pi * r, a, b)[0]
close("(We + Wm) v = P, We = Wm", [(We + Wm) * v, We], [4.5, Wm])
# (d) phasor wave
f0 = 300e6; beta = 2 * np.pi * f0 / v; lam = v / f0
Vt = 15e3 * a * lnba
print(f"  beta = {beta:.4f} rad/m = {beta/np.pi:.4f} pi; lambda = {lam:.4f} m; V~ = {Vt:.4f} V; <P> = {Vt**2/(2*Z0):.4f} W")
close("beta = 4 pi", beta, 4 * np.pi); close("V~ = 10 V", Vt, 10); close("<P> = 1 W", Vt**2 / (2 * Z0), 1)
Pfield = integrate.quad(lambda r: 0.5 * (Vt / (r * lnba)) * (Vt / Z0 / (2 * np.pi * r)) * 2 * np.pi * r, a, b)[0]
close("<P> by <S> integral", Pfield, 1)
print(f"  a + b = {(a+b)*1e3:.4f} mm; lambda/pi = {lam/np.pi*1e3:.2f} mm; v/(pi(a+b)) = {v/(np.pi*(a+b))/1e9:.2f} GHz")
check("TEM only at 300 MHz", a + b < lam / np.pi)

# ---------------------------------------------------------------------------
hdr("27.10 Splitting a snapshot: Z0 = 80, v = 2e8, V = 12 V, I = 0.05 A on |z| < 1 m")
Z0, v = 80.0, 2e8
C = 1 / (Z0 * v); L = Z0 / v
fA = (12 + Z0 * 0.05) / 2; gA = (12 - Z0 * 0.05) / 2
print(f"  f = {fA} V, g = {gA} V; C' = {C*1e12:.3f} pF/m, L' = {L*1e9:.3f} nH/m")
close("f = 8, g = 4", [fA, gA], [8, 4])
# independent solver: exact spectral propagator of the telegrapher's equations on a periodic grid
Lbox, Nz = 40.0, 2**16
zg = (np.arange(Nz) - Nz // 2) * (Lbox / Nz)
wedge = 0.01
box = 0.5 * (np.tanh((zg + 1) / wedge) - np.tanh((zg - 1) / wedge))
V0g, I0g = 12 * box, 0.05 * box
kk = 2 * np.pi * np.fft.fftfreq(Nz, d=Lbox / Nz)
Vk, Ik = np.fft.fft(V0g), np.fft.fft(I0g)


def propagate(t):
    # dV/dt = -(1/C) dI/dz, dI/dt = -(1/L) dV/dz  ->  per k: d/dt [V,I] = -j k [[0,1/C],[1/L,0]] [V,I]
    w = kk * v
    cs, sn = np.cos(w * t), np.sin(w * t)
    Vt = cs * Vk - 1j * sn * Z0 * Ik
    It = cs * Ik - 1j * sn * Vk / Z0
    return np.real(np.fft.ifft(Vt)), np.real(np.fft.ifft(It))


def at(arr, z):
    return arr[np.argmin(abs(zg - z))]


for t, pts in [(2.5e-9, [-2.0, -1.0, 0.0, 1.0, 2.0]), (10e-9, [-2.0, 0.0, 2.0])]:
    Vt, It = propagate(t)
    for z in pts:
        print(f"  t = {t*1e9:4.1f} ns, z = {z:+.1f} m: V = {at(Vt, z):+.4f} V, I = {at(It, z)*1e3:+.3f} mA, VI = {at(Vt, z)*at(It, z):+.4f} W")
Vt, It = propagate(2.5e-9)
close("t=2.5ns: g-only, overlap, f-only V", [at(Vt, -1.0), at(Vt, 0.0), at(Vt, 1.0)], [4, 12, 8], rtol=1e-4, atol=1e-6)
close("t=2.5ns: I", [at(It, -1.0), at(It, 0.0), at(It, 1.0)], [-0.05, 0.05, 0.1], rtol=1e-4, atol=1e-8)
close("t=2.5ns: p", [at(Vt, -1.0) * at(It, -1.0), at(Vt, 0.0) * at(It, 0.0), at(Vt, 1.0) * at(It, 1.0)],
      [-gA**2 / Z0, (fA**2 - gA**2) / Z0, fA**2 / Z0], rtol=1e-4, atol=1e-8)
close("outside zero at t=2.5ns", [at(Vt, -2.0), at(Vt, 2.0)], [0, 0], atol=1e-6)
Vt, It = propagate(10e-9)
close("t=10ns: V at -2, 0, +2", [at(Vt, -2.0), at(Vt, 0.0), at(Vt, 2.0)], [4, 0, 8], rtol=1e-4, atol=1e-6)
close("t=10ns: I at -2, +2", [at(It, -2.0), at(It, 2.0)], [-0.05, 0.1], rtol=1e-4, atol=1e-8)
W0 = 2 * (0.5 * C * 144 + 0.5 * L * 0.05**2)
Wf = fA**2 / Z0 * (2 / v); Wg = gA**2 / Z0 * (2 / v)
print(f"  W(0) = {W0*1e9:.4f} nJ (electric {2*0.5*C*144*1e9:.3f}, magnetic {2*0.5*L*0.0025*1e9:.3f}); "
      f"forward {Wf*1e9:.4f} nJ, backward {Wg*1e9:.4f} nJ")
close("10 nJ = 8 + 2", [W0, Wf, Wg], [10e-9, 8e-9, 2e-9])
close("forward energy as 2 m x C f^2", 2 * C * fA**2, 8e-9)
# numeric energy from the spectral fields at t = 10 ns
dzg = Lbox / Nz
Wnum = np.sum(0.5 * C * Vt**2 + 0.5 * L * It**2) * dzg
print(f"  numeric total energy at 10 ns = {Wnum*1e9:.4f} nJ")
close("energy conserved (numeric, edge smoothing)", Wnum, 10e-9, rtol=2e-2)
print(f"  I for a purely forward pulse = V/Z0 = {12/Z0:.3f} A")

# ---------------------------------------------------------------------------
hdr("27.11 Battery and the front: W = 3 cm, d = 1 mm, 12 V with + on x = d, front at 30 m at 200 ns")
W, d = 3e-2, 1e-3
v = 30 / 200e-9; er = (c / v) ** 2
p = plates(W, d, er)
print(f"  v = {v:.3e}, er = {er:.4f}, L = {p['L']*1e9:.4f} nH/m, C = {p['C']*1e9:.5f} nF/m, Z0 = {p['Z0']:.5f} = {p['Z0']/np.pi:.4f} pi")
close("er = 4", er, 4); close("Z0 = 2 pi", p['Z0'], 2 * np.pi); close("v from L,C", p['v'], 1.5e8)
close("L = 41.9 nH/m", p['L'], mu0 / 30); close("C = 120 eps0", p['C'], 120 * eps0)
V = -12.0; I = V / p['Z0']
Ex = V / d; Hy = I / W; eps = er * eps0
print(f"  V = {V} V, I = {I:.5f} A (= -6/pi), E_x = {Ex/1e3:.3f} kV/m, H_y = {Hy:.4f} A/m (= -200/pi)")
close("I = -6/pi", I, -6 / np.pi); close("H_y = -200/pi", Hy, -200 / np.pi)
Evec, Hvec = Ex * X, Hy * Y
close("E x H along +z", np.cross(Evec, Hvec) / np.linalg.norm(np.cross(Evec, Hvec)), Z)
rho0 = np.dot(X, eps * Evec); rhod = np.dot(-X, eps * Evec)
J0 = np.cross(X, Hvec); Jd = np.cross(-X, Hvec)
print(f"  x=0: rho_s = {rho0*1e9:.3f} nC/m^2, J_s = {J0} A/m;  x=d: rho_s = {rhod*1e9:.3f} nC/m^2, J_s = {Jd} A/m")
close("rho_s(0) = -424.4 nC/m^2", rho0, -4.8e4 * eps0)
close("J_s(d) = +63.66 z", Jd, 200 / np.pi * Z)
close("J_s(0) = -63.66 z", J0, -200 / np.pi * Z)
close("top plate charge per m = C |V|", rhod * W, p['C'] * 12)
print(f"  charge per metre on top plate = {rhod*W*1e9:.4f} nC/m; top plate current = {Jd[2]*W:.4f} A")
# (c) front arguments
close("charge: I = C v V", p['C'] * v * V, I)
close("Faraday: V = L v I", p['L'] * v * I, V)
print(f"  C v = {p['C']*v:.5f} S; L v = {p['L']*v:.5f} ohm")
# signed Faraday loop: up at z1 (+x), +z along x=d, -x at z2, -z along x=0 ; normal = x cross z = -y
nloop = np.cross(X, Z)
close("loop normal = -y", nloop, -Y)
Lf_rate = v  # length of field region inside loop grows at v
dPsi_dt = np.dot(mu0 * Hvec, nloop) * d * Lf_rate
print(f"  dPsi/dt = {dPsi_dt:.5f} V; emf = V(z1) = {V}; -dPsi/dt = {-dPsi_dt:.5f}")
close("emf = -dPsi/dt", V, -dPsi_dt)
# energy check
Pb = V * I
Wper = 0.5 * p['C'] * V**2 + 0.5 * p['L'] * I**2
print(f"  battery power VI = {Pb:.4f} W; stored per metre = {Wper*1e9:.3f} nJ/m (each half {0.5*p['C']*V**2*1e9:.3f}); x v = {Wper*v:.4f} W")
close("VI = stored-energy rate", Wper * v, Pb)
close("electric = magnetic", 0.5 * p['C'] * V**2, 0.5 * p['L'] * I**2)
# FDTD: ideal source V(0,t) = -12 smooth ramp, check plateau values and arrival at 30 m
Lz, dzf = 60.0, 0.01
nz = int(Lz / dzf) + 1
dtf = 0.5 * dzf / v
Vg = np.zeros(nz); Ig = np.zeros(nz - 1)
tr = 5e-9
srcf = lambda t: V * 0.5 * (1 + np.tanh((t - 4 * tr) / tr))
t = 0.0; rec = []; tprobe = []
iprobe = int(round(30 / dzf))
nsteps = int(260e-9 / dtf)
for n in range(nsteps):
    Ig -= dtf / (p['L'] * dzf) * (Vg[1:] - Vg[:-1])
    t += dtf / 2
    Vg[1:-1] -= dtf / (p['C'] * dzf) * (Ig[1:] - Ig[:-1])
    t += dtf / 2
    Vg[0] = srcf(t)
    rec.append(Vg[iprobe]); tprobe.append(t)
rec, tprobe = np.array(rec), np.array(tprobe)
t50 = tprobe[np.argmax(rec <= V / 2)] - 4 * tr
print(f"  FDTD: probe at 30 m reaches V/2 at t = {t50*1e9:.2f} ns after the source's mid-ramp")
check("FDTD arrival 200 ns +- 1 ns", abs(t50 - 200e-9) < 1e-9)
jm = int(round(10 / dzf))
print(f"  FDTD at t = {t*1e9:.1f} ns, z = 10 m: V = {Vg[jm]:.4f} V, I = {Ig[jm]:.5f} A")
close("FDTD plateau V, I", [Vg[jm], Ig[jm]], [V, I], rtol=2e-3)

# ---------------------------------------------------------------------------
hdr("27.12 Leaky coax: fields -> telegrapher's equations; b/a = e, er = 2.25, sigma = 1e-5")
lnba = 1.0; er = 2.25; sig = 1e-5; eps = er * eps0
L = mu0 * lnba / (2 * np.pi); C = 2 * np.pi * eps / lnba; G = 2 * np.pi * sig / lnba
print(f"  L = {L*1e9:.4f} nH/m, C = {C*1e12:.4f} pF/m, G = {G*1e6:.4f} uS/m, v = {1/np.sqrt(L*C):.4e}, Z0 = {np.sqrt(L/C):.4f}")
close("L = 200 nH/m", L, 200e-9); close("C = 125 pF/m", C, 125e-12); close("G = 62.83 uS/m", G, 2 * np.pi * 1e-5)
close("v = 2e8", 1 / np.sqrt(L * C), 2e8); close("Z0 = 40", np.sqrt(L / C), 40)
close("LC = mu0 eps, G/C = sigma/eps", [L * C, G / C], [mu0 * eps, sig / eps])
fx = sig / (2 * np.pi * eps)
print(f"  crossover f = sigma/(2 pi eps) = {fx/1e3:.4f} kHz; G/(wC) at 10 MHz = {G/(2*np.pi*1e7*C):.5f}")
close("80 kHz", fx, 80e3)
print(f"  2 pi eps = {2*np.pi*eps:.4e} F/m"); close("ratio 0.008 at 10 MHz", G / (2 * np.pi * 1e7 * C), 0.008)
# full 3-D finite-difference check: build E, H from an exact lossy-line wave and test both curl equations
a_ = 1e-3; b_ = a_ * np.e
wq = 2 * np.pi * 50e3   # near the crossover so both terms matter
gam = np.sqrt((1j * wq * L) * (G + 1j * wq * C)); Zc = np.sqrt(1j * wq * L / (G + 1j * wq * C))
Vz = lambda z, t: np.real(np.exp(1j * wq * t - gam * z))
Iz = lambda z, t: np.real(np.exp(1j * wq * t - gam * z) / Zc)
print(f"  test wave at 50 kHz: gamma = {gam:.5e} 1/m, Zc = {Zc:.4f} ohm")


def Efield(x, y, z, t):
    r = np.hypot(x, y)
    return Vz(z, t) / (r * lnba) * np.array([x, y, 0.0]) / r


def Hfield(x, y, z, t):
    r = np.hypot(x, y)
    return Iz(z, t) / (2 * np.pi * r) * np.array([-y, x, 0.0]) / r


def d4(fun, h):
    # fourth-order central difference of a vector-valued function of one offset
    return (-fun(2 * h) + 8 * fun(h) - 8 * fun(-h) + fun(-2 * h)) / (12 * h)


def curl(F, x, y, z, t, h, hz=0.5):
    dFx = d4(lambda s: F(x + s, y, z, t), h)
    dFy = d4(lambda s: F(x, y + s, z, t), h)
    dFz = d4(lambda s: F(x, y, z + s, t), hz)
    return np.array([dFy[2] - dFz[1], dFz[0] - dFx[2], dFx[1] - dFy[0]])


worst = 0.0
for (x, y, z, t) in [(1.3e-3, 0.4e-3, 120.0, 3e-6), (-0.9e-3, 1.7e-3, 800.0, 7.1e-6), (0.2e-3, -2.1e-3, 2300.0, 1.3e-5)]:
    ht = 1e-10; hx = 1e-7
    cE = curl(Efield, x, y, z, t, hx)
    dHdt = (Hfield(x, y, z, t + ht) - Hfield(x, y, z, t - ht)) / (2 * ht)
    cH = curl(Hfield, x, y, z, t, hx)
    dEdt = (Efield(x, y, z, t + ht) - Efield(x, y, z, t - ht)) / (2 * ht)
    r1 = np.linalg.norm(cE + mu0 * dHdt) / np.linalg.norm(cE)
    r2 = np.linalg.norm(cH - (sig * Efield(x, y, z, t) + eps * dEdt)) / np.linalg.norm(cH)
    worst = max(worst, r1, r2)
    print(f"  point r = {np.hypot(x,y)*1e3:.3f} mm, z = {z} m: Faraday residual {r1:.2e}, Ampere residual {r2:.2e}")
check("Maxwell's curl equations hold for the telegrapher wave (rel. residual < 1e-4)", worst < 1e-4)
# and the r^{-1} cancellation: the phi-component of curl E divided by (1/r) is r-independent
vals = []
for r in [1.1e-3, 1.8e-3, 2.6e-3]:
    cE = curl(Efield, r, 0.0, 500.0, 2e-6, 1e-7)
    vals.append(cE[1] * r)
close("r (curl E)_phi independent of r", np.array(vals), vals[0] * np.ones(3), rtol=1e-5)

hdr(f"TOTAL CHECKS: {len(ALL)}, FAILED: {ALL.count(False)}")
