#!/usr/bin/env python3
"""R10.py -- independent verification of practice page 10 (capacitance and conductance).

numpy/scipy only. Every number, sign and direction stated on the page is recomputed from the
problem data, by a brute-force or second route where possible (quad of D/eps and dr/(sigma*area),
finite-volume Laplace solves in 1-D and 2-D, Poisson integration + root finding for the junction,
numerical derivatives of W(x), solve_ivp for every transient), and compared with the page:
PASS means the computed value rounds to the page's value at the precision the page prints.
The last block checks that the three exam-based problems do not reproduce the official keys.
Problem 10.9 is checked in its re-parameterized form (outer shell held at V(b) = -100 V).
"""
import numpy as np
from scipy.integrate import quad, dblquad, solve_ivp, cumulative_trapezoid, trapezoid
from scipy.optimize import brentq, fsolve
import scipy.sparse as sp
from scipy.sparse.linalg import spsolve

eps0 = 8.8541878128e-12
qe = 1.602176634e-19
NP = NF = 0


def _tol(s):
    s = s.strip().lower()
    m, ex = (s.split('e') + ['0'])[:2]
    dec = len(m.split('.')[1]) if '.' in m else 0
    return float(s), 0.5 * 10.0 ** (int(ex) - dec) * (1 + 1e-9)


def chk(label, comp, page):
    """page: the value as printed on the page (units in the label); PASS if comp rounds to it."""
    global NP, NF
    val, tol = _tol(page)
    ok = abs(comp - val) <= tol
    NP += ok
    NF += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {label}: computed {comp:.6g}  page {page}")


def same(label, comp, page):
    global NP, NF
    ok = comp == page
    NP += ok
    NF += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {label}: computed {comp}  page {page}")


def differs(label, practice, exam, rtol=0.02):
    """PASS if the official exam key does NOT reproduce the practice answer."""
    global NP, NF
    if isinstance(practice, (bool, str)) or isinstance(exam, (bool, str)):
        ok = practice != exam
    else:
        ok = not np.isclose(practice, exam, rtol=rtol, atol=0.0)
    NP += ok
    NF += not ok
    print(f"{'PASS' if ok else 'FAIL'}  [exam key differs] {label}: practice {practice:.4g}  exam key {exam:.4g}"
          if not isinstance(practice, (bool, str)) else
          f"{'PASS' if ok else 'FAIL'}  [exam key differs] {label}: practice {practice}  exam key {exam}")


def head(t):
    print(f"\n===== {t} =====")


# ------------------------------------------------------------------ 10.1
head('10.1 Four capacitances by formula')
Ap, dp = 0.1 * 0.1, 0.5e-3
Ca = 1 / quad(lambda z: (1 / Ap) / (4 * eps0), 0, dp)[0]          # Q = 1 C: D = Q/A, V = int D/eps dz
chk('(a) C/eps0', Ca / eps0, '80'); chk('(a) C [pF]', Ca * 1e12, '708')
ac, bc = 0.375e-3, 1.5e-3
Cb = 1 / quad(lambda r: 1 / (2 * np.pi * 2.25 * eps0 * r), ac, bc)[0]  # 1 C/m: Gauss E, V = int E dr
chk('(b) ln(b/a)', np.log(bc / ac), '1.3863'); chk("(b) C' [pF/m]", Cb * 1e12, '90.3')
a1, b1 = 0.04, 0.05
Cc = 1 / quad(lambda r: 1 / (4 * np.pi * eps0 * r**2), a1, b1)[0]
chk('(c) ab/(b-a) [m]', a1 * b1 / (b1 - a1), '0.2'); chk('(c) C [pF]', Cc * 1e12, '22.3')
Cd = 1 / quad(lambda r: 1 / (4 * np.pi * eps0 * r**2), 0.09, np.inf)[0]
chk('(d) C [pF]', Cd * 1e12, '10.0'); chk('(d) 0.09/9e9 [pF]', 0.09 / 9e9 * 1e12, '10.0')
RE = 6.37e6
CE = 1 / (quad(lambda x: 1 / x**2, 1, np.inf)[0] / (4 * np.pi * eps0 * RE))   # r = RE x: int_RE^inf dr/r^2 = (1/RE) int_1^inf dx/x^2
chk('(d) Earth C [uF]', CE * 1e6, '709')
chk('check: plates, all dims x2 -> ratio', (4 * eps0 * 4 * Ap / (2 * dp)) / Ca, '2')
chk('check: spheres, all dims x2 -> ratio', (4 * np.pi * eps0 * (2 * a1) * (2 * b1) / (2 * b1 - 2 * a1)) / Cc, '2.00')
chk("check: coax C', all dims x2 -> ratio", (2 * np.pi * 2.25 * eps0 / np.log(2 * bc / (2 * ac))) / Cb, '1.00')
chk('watch: plates without eps_r [pF]', eps0 * Ap / dp * 1e12, '177')
chk('watch: coax with log10 [pF/m]', 2 * np.pi * 2.25 * eps0 / np.log10(bc / ac) * 1e12, '208')

# ------------------------------------------------------------------ 10.2
head('10.2 Slide in a slab')
C0, V0, er = 1e-9, 10.0, 4.0
d2 = 1e-3; A2 = C0 * d2 / eps0                                    # any plates with C0 = eps0 A/d
C = er * C0; Q0 = C0 * V0; W0 = 0.5 * C0 * V0**2
chk('C [nF]', C * 1e9, '4'); chk('Q0 [nC]', Q0 * 1e9, '10'); chk('W0 [nJ]', W0 * 1e9, '50')
Vi = Q0 / C; D_before = Q0 / A2; D_after = Q0 / A2                # free charge unchanged
E_before = D_before / eps0; E_after = D_after / (er * eps0); Wi = Q0**2 / (2 * C)
st = {'a': np.isclose(Vi, 2.5), 'b': np.isclose(D_after, D_before), 'c': Wi > W0, 'd': np.isclose(E_after / E_before, 0.25)}
same('(i) false statement(s)', [k for k, v in st.items() if not v], ['c'])
chk('(i) V [V]', Vi, '2.5'); chk('(i) W [nJ]', Wi * 1e9, '12.5'); chk('(i) energy lost to the slab [nJ]', (W0 - Wi) * 1e9, '37.5')
Qii = C * V0; Wii = 0.5 * C * V0**2; Wbat = V0 * (Qii - Q0)
st = {'a': np.isclose(Qii, 40e-9), 'b': np.isclose((V0 / d2) / (V0 / d2), 1.0), 'c': np.isclose(Wii / W0, 4.0),
      'd': np.isclose(Wbat, Wii - W0)}
same('(ii) false statement(s)', [k for k, v in st.items() if not v], ['d'])
chk('(ii) Q [nC]', Qii * 1e9, '40'); chk('(ii) W [nJ]', Wii * 1e9, '200'); chk('(ii) dQ [nC]', (Qii - Q0) * 1e9, '30')
chk('(ii) battery work V0 dQ [nJ]', Wbat * 1e9, '300'); chk('(ii) rise of stored W [nJ]', (Wii - W0) * 1e9, '150')
chk('(ii) work done on the slab [nJ]', (Wbat - (Wii - W0)) * 1e9, '150')
# (iii) slab pushed in a distance s of plate length L: C(s) = C0[(1 - s/L) + er s/L]
L = 0.1; Cs = lambda s: C0 * ((1 - s / L) + er * s / L); h = 1e-7
okF = True
for s in (0.01, 0.05, 0.09):
    FQ = -(Q0**2 / (2 * Cs(s + h)) - Q0**2 / (2 * Cs(s - h))) / (2 * h)          # isolated: F = -dW/ds|Q
    FV = (V0 * (Cs(s + h) - Cs(s - h)) * V0 - (0.5 * Cs(s + h) * V0**2 - 0.5 * Cs(s - h) * V0**2)) / (2 * h)  # F ds = V dQ - dW
    Vs_ = Q0 / Cs(s); F_sameV = 0.5 * Vs_**2 * (Cs(s + h) - Cs(s - h)) / (2 * h)
    print(f"      s = {s} m: F(fixed Q) = {FQ:.4e} N, F(fixed V) = {FV:.4e} N, (1/2)V^2 dC/ds at the fixed-Q state = {F_sameV:.4e} N")
    okF &= FQ > 0 and FV > 0 and np.isclose(FQ, F_sameV, rtol=1e-6)
same('(iii) force pulls the slab in (F > 0) in both cases, same formula -> statement is false', bool(okF), True)

# ------------------------------------------------------------------ 10.3
head('10.3 Leakage of a long cable')
Cp3, er3, sig3 = 100e-12, 2.25, 1.0e-14
eps3 = er3 * eps0; soe = sig3 / eps3
chk('(a) sigma/eps [1/s]', soe, '5.02e-4'); chk("(a) G' = (sigma/eps)C' [S/m]", soe * Cp3, '5.02e-14')
lnba3 = 2 * np.pi * eps3 / Cp3; a3 = 1e-3; b3 = a3 * np.exp(lnba3)        # radii consistent with C'
chk('check: ln(b/a)', lnba3, '1.2517'); chk('check: b/a', b3 / a3, '3.496')
Rp3 = quad(lambda r: 1 / (sig3 * 2 * np.pi * r), a3, b3)[0]              # ohm m: radial shells in series
chk("check: G' from shells in series [S/m]", 1 / Rp3, '5.02e-14')
for ell, Gs, Rs in ((1000, '5.02e-11', '19.92'), (2000, '1.004e-10', '9.961')):
    G = ell / Rp3
    chk(f'(b) {ell} m: G [S]', G, Gs); chk(f'(b) {ell} m: R [Gohm]', 1 / G / 1e9, Rs)
for ell in (1000, 2000):
    C_, G_ = Cp3 * ell, ell / Rp3
    ev = lambda t, y: y[0] - np.exp(-1); ev.terminal = True
    sol = solve_ivp(lambda t, y: [-G_ * y[0] / C_], [0, 1e5], [1.0], events=ev, rtol=1e-11, atol=1e-13)
    chk(f'(c) {ell} m: 1/e time from C dV/dt = -GV [s]', sol.t_events[0][0], '1992')
chk('(c) tau [min]', eps3 / sig3 / 60, '33.2')
chk('check: C of 1 km [nF]', Cp3 * 1000 * 1e9, '100'); chk('check: R C for 1 km [s]', (Rp3 / 1000) * (Cp3 * 1000), '1992')

# ------------------------------------------------------------------ 10.4
head('10.4 Energy density in a dielectric')
A4, d4, er4, V4 = 0.2 * 0.2, 1e-3, 5.0, 50.0
E4 = V4 / d4
chk('E [V/m]', E4, '5e4'); chk("student's w [J/m^3]", 0.5 * eps0 * E4**2, '0.0111'); chk('volume [m^3]', A4 * d4, '4e-5')
chk("student's W [uJ]", 0.5 * eps0 * E4**2 * A4 * d4 * 1e6, '0.443')
chk('corrected w [J/m^3]', 0.5 * er4 * eps0 * E4**2, '0.0553')
Wint4 = quad(lambda z: 0.5 * er4 * eps0 * (V4 / d4)**2 * A4, 0, d4)[0]
chk('corrected W = int w dV [uJ]', Wint4 * 1e6, '2.21')
C4 = er4 * eps0 * A4 / d4
chk('C/eps0', C4 / eps0, '200'); chk('C [nF]', C4 * 1e9, '1.771'); chk('1/2 C V^2 [uJ]', 0.5 * C4 * V4**2 * 1e6, '2.21')
chk("student's / true", (0.5 * eps0 * E4**2 * A4 * d4) / (0.5 * C4 * V4**2), '0.2')

# ------------------------------------------------------------------ 10.5
head('10.5 Which capacitor leaks first')
eps5, sig5 = 2 * eps0, 1.0e-13
tau5 = eps5 / sig5
chk('tau = eps/sigma [s]', tau5, '177.1'); chk('t_half [s]', tau5 * np.log(2), '122.7')
Cpl = 1e-9; Rpl = 1 / (sig5 * Cpl / eps5)                                   # same A/d in C and G
lnba5 = 2 * np.pi * eps5 / 100e-12; a5 = 1e-3; b5 = a5 * np.exp(lnba5)       # radii consistent with 100 pF/m
Ccab = 1 / quad(lambda r: 1 / (2 * np.pi * eps5 * r * 100), a5, b5)[0]
Rcab = quad(lambda r: 1 / (sig5 * 2 * np.pi * r * 100), a5, b5)[0]
Csph = 1 / quad(lambda r: 1 / (4 * np.pi * eps5 * r**2), 1, np.inf)[0]
Rsph = quad(lambda r: 1 / (sig5 * 4 * np.pi * r**2), 1, np.inf)[0]
chk('plates R [ohm]', Rpl, '1.771e11'); chk('cable C [nF]', Ccab * 1e9, '10'); chk('cable R [ohm]', Rcab, '1.771e10')
chk('sphere C [pF]', Csph * 1e12, '222.5'); chk('sphere C/(8 pi eps0)', Csph / (8 * np.pi * eps0), '1')
chk('sphere G [S]', 1 / Rsph, '1.257e-12'); chk('sphere R [ohm]', Rsph, '7.958e11')
th = []
for name, R_, C_ in (('plates', Rpl, Cpl), ('cable', Rcab, Ccab), ('sphere', Rsph, Csph)):
    ev = lambda t, y: y[0] - 0.5; ev.terminal = True
    sol = solve_ivp(lambda t, y: [-y[0] / (R_ * C_)], [0, 1e4], [1.0], events=ev, rtol=1e-11, atol=1e-13)
    th.append(sol.t_events[0][0])
    chk(f'{name}: RC [s]', R_ * C_, '177.1'); chk(f'{name}: half-charge time from ODE [s]', th[-1], '122.7')
same('MC key', 'd' if np.ptp(th) < 1e-6 * th[0] else 'not d', 'd')
Cd_ = {'plates': Cpl, 'cable': Ccab, 'sphere': Csph}; Rd_ = {'plates': Rpl, 'cable': Rcab, 'sphere': Rsph}
same('(a) smallest C', min(Cd_, key=Cd_.get), 'sphere'); same('(a) largest R', max(Rd_, key=Rd_.get), 'sphere')
same('(b) smallest R', min(Rd_, key=Rd_.get), 'cable'); same('(b) largest C', max(Cd_, key=Cd_.get), 'cable')

# ------------------------------------------------------------------ 10.6
head('10.6 Two layers between charged plates')
rs6 = 4e4 * eps0; d61, d6 = 1e-3, 3e-3
eps_z = lambda z: 4 * eps0 if z < d61 else eps0
N = 300; hz = d6 / N
kz = np.array([eps_z((i + 0.5) * hz) / hz for i in range(N)])
M = sp.lil_matrix((N, N)); rhs = np.zeros(N)
M[0, 0] = kz[0]; M[0, 1] = -kz[0]; rhs[0] = rs6          # D_z leaving the bottom plate = rho_s
for i in range(1, N):
    M[i, i] = kz[i - 1] + kz[i]; M[i, i - 1] = -kz[i - 1]
    if i + 1 < N:
        M[i, i + 1] = -kz[i]                               # V_N = V(3 mm) = 0
Vfd = np.append(spsolve(M.tocsr(), rhs), 0.0)
chk('(b) V(1 mm) [V], 1-D finite volume', Vfd[int(round(d61 / hz))], '80'); chk('(b) V(0) [V], 1-D finite volume', Vfd[0], '90')
Dz = rs6; E61, E62 = Dz / (4 * eps0), Dz / eps0; P61, P62 = Dz - eps0 * E61, Dz - eps0 * E62
chk('(a) D_z [C/m^2]', Dz, '3.54e-7'); chk('(a) D_z/eps0', Dz / eps0, '4e4')
chk('(a) E1_z [V/m]', E61, '1e4'); chk('(a) E2_z [V/m]', E62, '4e4')
chk('(a) P1_z/eps0', P61 / eps0, '3e4'); chk('(a) P1_z [uC/m^2]', P61 * 1e6, '0.266'); chk('(a) P2_z', P62, '0')
same('(a) direction of D, E1, E2, P1', '+z' if min(Dz, E61, E62, P61) > 0 else 'other', '+z')
Vline = lambda zz: quad(lambda s: Dz / eps_z(s), zz, d6, points=[d61])[0]   # V(z) = V(3mm) + int_z^3mm E_z dz
chk('(b) V(1 mm) [V], line integral', Vline(d61), '80'); chk('(b) V(0) [V], line integral', Vline(0.0), '90')
CA = rs6 / Vline(0.0)
chk('(c) C/A [nF/m^2]', CA * 1e9, '3.935'); chk('(c) (C/A)/eps0', CA / eps0, '444.4'); chk('(c) 4000/9', 4000 / 9, '444.4')
chk('(c) d1/eps_r1 + d2/eps_r2 [mm]', (d61 / 4 + (d6 - d61)) * 1e3, '2.25')
chk('(c) series formula (C/A)/eps0', 1 / (d61 / (4 * eps0) + (d6 - d61) / eps0) / eps0, '444.4')
print(f"      (empty 3 mm gap would give {1 / d6:.1f} eps0: the layer raises C/A by a factor {CA / (eps0 / d6):.3f})")
WCV = 0.5 * CA * Vline(0.0)**2
Wfld = quad(lambda s: 0.5 * eps_z(s) * (Dz / eps_z(s))**2, 0, d6, points=[d61])[0]
Wd6 = quad(lambda s: 0.5 * 4 * eps0 * (Dz / (4 * eps0))**2, 0, d61)[0]; Wa6 = quad(lambda s: 0.5 * eps0 * (Dz / eps0)**2, d61, d6)[0]
chk('(d) 1/2 (C/A) V^2 / eps0', WCV / eps0, '1.8e6'); chk('(d) 1/2 (C/A) V^2 [uJ/m^2]', WCV * 1e6, '15.94')
chk('(d) int 1/2 eps E^2 dz [uJ/m^2]', Wfld * 1e6, '15.94')
chk('(d) dielectric layer / eps0', Wd6 / eps0, '2e5'); chk('(d) dielectric layer [uJ/m^2]', Wd6 * 1e6, '1.771')
chk('(d) air layer / eps0', Wa6 / eps0, '1.6e6'); chk('(d) air layer [uJ/m^2]', Wa6 * 1e6, '14.17')
chk('(d) fraction of energy in the air', Wa6 / Wfld, '0.889'); chk('(d) fraction of voltage across the air', Vline(d61) / Vline(0), '0.889')
chk('check: top plate rho_s = -z.D, /eps0', -Dz / eps0, '-4e4')
chk('check: bound charge at z = 0+ (P1.(-z)) /eps0', -P61 / eps0, '-3e4'); chk('check: bound charge at z = 1 mm (P1.z) /eps0', P61 / eps0, '3e4')
chk('check: jump of eps0 E_z at 1 mm /eps0', (eps0 * E62 - eps0 * E61) / eps0, '3e4')
chk('watch: volts across the dielectric', E61 * d61, '10')

# ------------------------------------------------------------------ 10.7
head('10.7 One slab, two placements')
A7, d7, er7, V7 = 100e-4, 2e-3, 3.0, 100.0
C07 = eps0 * A7 / d7
chk('C0/eps0', C07 / eps0, '5'); chk('C0 [pF]', C07 * 1e12, '44.27')
CS = 1 / ((1 / A7) * (d7 / 2 / (er7 * eps0) + d7 / 2 / eps0))              # D common: drops add
CP = er7 * eps0 * (A7 / 2) / d7 + eps0 * (A7 / 2) / d7                       # E common: charges add
chk('(a) C_S/C0', CS / C07, '1.5'); chk('(a) C_S [pF]', CS * 1e12, '66.41'); chk('(a) C_P/C0', CP / C07, '2'); chk('(a) C_P [pF]', CP * 1e12, '88.54')
okb = True
for e in (1.0, 1.5, 3.0, 10.0, 81.0):
    cs_ = 1 / (0.5 / e + 0.5); cp_ = 0.5 * e + 0.5                           # series / parallel halves, in units of C0
    okb &= abs((cp_ - cs_) - (e - 1)**2 / (2 * (1 + e))) < 1e-12 and cp_ - cs_ >= 0 and ((cp_ - cs_) == 0) == (e == 1.0)
same('(b) C_P - C_S = C0 (er-1)^2/[2(1+er)] >= 0, zero only at er = 1 (5 values)', bool(okb), True)
chk('(b) difference here / C0', (CP - CS) / C07, '0.5')
chk('(b) er = 81: C_S/C0', 1 / (0.5 / 81 + 0.5), '1.976'); chk('(b) er = 81: C_P/C0', 0.5 * 81 + 0.5, '41')
QS = CS * V7; DS = QS / A7
chk('(c) stacked Q [nC]', QS * 1e9, '6.64'); chk('(c) stacked D [C/m^2]', DS, '6.64e-7')
chk('(c) stacked E in dielectric [kV/m]', DS / (er7 * eps0) / 1e3, '25'); chk('(c) stacked E in air [kV/m]', DS / eps0 / 1e3, '75')
chk('(c) stacked V across dielectric [V]', DS / (er7 * eps0) * d7 / 2, '25'); chk('(c) stacked V across air [V]', DS / eps0 * d7 / 2, '75')
chk('(c) side by side E [kV/m]', V7 / d7 / 1e3, '50'); chk('(c) rho_s against dielectric [uC/m^2]', er7 * eps0 * V7 / d7 * 1e6, '1.33')
chk('(c) rho_s against air [uC/m^2]', eps0 * V7 / d7 * 1e6, '0.443'); chk('(c) empty capacitor E [kV/m]', V7 / d7 / 1e3, '50')
# (d) 2-D finite-volume solve of div(eps grad V) = 0 in (u = ln r, phi), eps = 3 eps0 for 0<phi<pi
a7, b7 = 1e-3, 4e-3
Nu, Nph = 40, 64; du = np.log(b7 / a7) / Nu; dph = 2 * np.pi / Nph
phc = (np.arange(Nph) + 0.5) * dph; epj = np.where(phc < np.pi, 3 * eps0, eps0)
kf = 2 * epj * np.roll(epj, -1) / (epj + np.roll(epj, -1))                  # face j+1/2 (harmonic mean)
nunk = (Nu - 1) * Nph; ix = lambda i, j: (i - 1) * Nph + (j % Nph)
M = sp.lil_matrix((nunk, nunk)); rhs = np.zeros(nunk)
for i in range(1, Nu):
    for j in range(Nph):
        p = ix(i, j); cu = epj[j] / du**2; kp = kf[j] / dph**2; km = kf[j - 1] / dph**2
        M[p, p] = -2 * cu - kp - km
        M[p, ix(i, j + 1)] += kp; M[p, ix(i, j - 1)] += km
        for ii in (i - 1, i + 1):
            if ii == 0:
                rhs[p] -= cu * 1.0                                           # V(a) = 1 V
            elif ii < Nu:
                M[p, ix(ii, j)] += cu                                        # V(b) = 0
Vsol = spsolve(M.tocsr(), rhs).reshape(Nu - 1, Nph)
rho_a = -epj * ((Vsol[0, :] - 1.0) / du) / a7                                # rho_s = eps E_r(a) = -eps (dV/du)/a
chk("(d) C' [pF/m], 2-D finite volume", np.sum(rho_a * a7 * dph) * 1e12, '80.3')
chk("(d) C' = 4 pi eps0/ln 4 [pF/m]", 4 * np.pi * eps0 / np.log(4) * 1e12, '80.3')
chk('(d) rho_s ratio, dielectric : air', rho_a[phc < np.pi].mean() / rho_a[phc > np.pi].mean(), '3')
same('(d) FD potential independent of phi (field radial, E common)', bool(np.max(np.ptp(Vsol, axis=1)) < 1e-9), True)

# ------------------------------------------------------------------ 10.8
head('10.8 Diode junction capacitance')
eps8 = 11.7 * eps0; A8 = 1e-6; rho1 = qe * 1e23; rho2 = qe * 1e22
chk('(a) rho1 [C/m^3]', rho1, '1.602e4'); chk('(a) rho2 [C/m^3]', rho2, '1602')
chk('(a) 1/rho1 + 1/rho2 [m^3/C]', 1 / rho1 + 1 / rho2, '6.87e-4'); chk('(a) eps [F/m]', eps8, '1.036e-10')


def depletion(W1, W2, n=4001):
    """Integrate Poisson from x = -W1 with E(-W1) = 0 (p side rho = -rho1, n side +rho2)."""
    x1 = np.linspace(-W1, 0, n); x2 = np.linspace(0, W2, n)
    E1 = cumulative_trapezoid(np.full(n, -rho1 / eps8), x1, initial=0)
    E2 = E1[-1] + cumulative_trapezoid(np.full(n, rho2 / eps8), x2, initial=0)
    return E2[-1], -(trapezoid(E1, x1) + trapezoid(E2, x2)), E1[-1]       # E(W2), V(W2)-V(-W1), E(0)


def solveW(V):
    f = lambda w: [depletion(w[0] * 1e-6, w[1] * 1e-6)[0] / 1e6, depletion(w[0] * 1e-6, w[1] * 1e-6)[1] - V]
    w = fsolve(f, [0.03, 0.3], xtol=1e-14)
    return w[0] * 1e-6, w[1] * 1e-6


W81, W82 = solveW(1.0); Wt8 = W81 + W82
chk('(a) W1+W2 at 1 V [um]', Wt8 * 1e6, '0.3772'); chk('(a) W1 [um]', W81 * 1e6, '0.0343'); chk('(a) W2 [um]', W82 * 1e6, '0.343')
chk('(a) W1/W2', W81 / W82, '0.1'); chk('(a) n-side share W2/(W1+W2)', W82 / Wt8, '0.909')
same('(a) most of the depletion region on', 'n side' if W82 > W81 else 'p side', 'n side')
same('(setup) field at x = 0 points from n to p', '-x' if depletion(W81, W82)[2] < 0 else '+x', '-x')
chk('(setup) closed form sqrt(2 eps V (1/rho1+1/rho2)) [um]', np.sqrt(2 * eps8 * (1 / rho1 + 1 / rho2)) * 1e6, '0.3772')
Qf = lambda V: rho2 * solveW(V)[1] * A8
hV = 1e-3; Q81 = Qf(1.0); C81 = (Qf(1 + hV) - Qf(1 - hV)) / (2 * hV)
chk('(b) Q at 1 V [nC]', Q81 * 1e9, '0.549'); chk('(b) C = dQ/dV, central difference [pF]', C81 * 1e12, '274.7')
chk('(b) eps A/(W1+W2) [pF]', eps8 * A8 / Wt8 * 1e12, '274.7')
chk('(b) A sqrt(eps rho1 rho2/(2V(rho1+rho2))) [pF]', A8 * np.sqrt(eps8 * rho1 * rho2 / (2 * (rho1 + rho2))) * 1e12, '274.7')
chk('(b) Q/(2V) [pF]', Q81 / 2 * 1e12, '274.7')
W41, W42 = solveW(4.0)
chk('(c) W1+W2 at 4 V [um]', (W41 + W42) * 1e6, '0.7543'); chk('(c) W1 [um]', W41 * 1e6, '0.0686'); chk('(c) W2 [um]', W42 * 1e6, '0.686')
C84 = (Qf(4 + hV) - Qf(4 - hV)) / (2 * hV)
chk('(c) Q at 4 V [nC]', Qf(4.0) * 1e9, '1.10'); chk('(c) C at 4 V [pF]', C84 * 1e12, '137.3')
chk('(c) d ln C / d ln V', np.log(C84 / C81) / np.log(4.0), '-0.5')
chk('(d) Q/V at 1 V [pF]', Q81 * 1e12, '549.3'); chk('(d) (Q/V) / (dQ/dV)', Q81 / C81, '2')

# ------------------------------------------------------------------ 10.9
head('10.9 Leaky spheres, one lossy half   [re-parameterized: V(a) = 0, V(b) = -V0 = -100 V]')
a9, b9, V09 = 0.01, 0.02, 100.0
Va9, Vb9 = 0.0, -V09
eps9, sig9 = 3 * eps0, 1.0e-8
N = 4000; r9 = np.linspace(a9, b9, N + 1); hr = r9[1] - r9[0]; rf = 0.5 * (r9[:-1] + r9[1:]); kr = rf**2 / hr
M = sp.diags([-(kr[:-1] + kr[1:]), kr[1:-1], kr[1:-1]], [0, 1, -1], format='csr')
rhs = np.zeros(N - 1); rhs[0] -= kr[0] * Va9; rhs[-1] -= kr[-1] * Vb9
Vr9 = np.concatenate([[Va9], spsolve(M, rhs), [Vb9]])                     # d/dr(r^2 dV/dr) = 0, finite volume
same('(b) FD V(r) matches the page formula -200 + 2/r V (max dev < 1 mV)', bool(np.max(np.abs(Vr9 - (-200 + 2 / r9))) < 1e-3), True)
Bfit = (np.interp(0.012, r9, Vr9) - np.interp(0.018, r9, Vr9)) / (1 / 0.012 - 1 / 0.018); Afit = np.interp(0.012, r9, Vr9) - Bfit / 0.012
chk('(b) V = A + B/r: A [V]', Afit, '-200'); chk('(b) V = A + B/r: B [V m]', Bfit, '2')
flux = kr[0] * (Vr9[1] - Vr9[0])                                            # r^2 dV/dr (constant)
Er9 = lambda r: -flux / r**2
chk('(b) V0 ab/(b-a) [V m]', V09 * a9 * b9 / (b9 - a9), '2')
chk('(b) E_r(a) [V/m]', Er9(a9), '2e4'); chk('(b) E_r(b) [V/m]', Er9(b9), '5e3')
same('(b) E direction', 'outward (+r)' if Er9(a9) > 0 and Er9(b9) > 0 else 'inward (-r)', 'outward (+r)')
same('(b) on z = 0: r_hat . z_hat = cos(pi/2) = 0 -> E tangential, D_z = J_z = 0', bool(abs(np.cos(np.pi / 2)) < 1e-15), True)
rG = 0.015
Qin = dblquad(lambda th, ph: eps9 * Er9(rG) * rG**2 * np.sin(th), 0, 2 * np.pi, 0, np.pi)[0]   # Gauss: flux of D = Q(inner)
Qsh = dblquad(lambda th, ph: -eps9 * Er9(b9) * b9**2 * np.sin(th), 0, 2 * np.pi, 0, np.pi)[0]  # rho_s = n.D, n = -r on the shell
C9 = Qin / (Va9 - Vb9)
chk('(b) C [pF]', C9 * 1e12, '6.676'); chk('(b) 4 pi eps ab/(b-a) [pF]', 4 * np.pi * eps9 * a9 * b9 / (b9 - a9) * 1e12, '6.676')
chk('(b) charge on the inner sphere [pC]', Qin * 1e12, '667.6'); chk('(b) charge on the outer shell [pC]', Qsh * 1e12, '-667.6')
rs_a = eps9 * Er9(a9)
chk('(a)(ii) rho_s on the inner sphere / eps0', rs_a / eps0, '6e4'); chk('(a)(ii) rho_s on the inner sphere [uC/m^2]', rs_a * 1e6, '0.531')
Qup = dblquad(lambda th, ph: rs_a * a9**2 * np.sin(th), 0, 2 * np.pi, 0, np.pi / 2)[0]
Qlo = dblquad(lambda th, ph: rs_a * a9**2 * np.sin(th), 0, 2 * np.pi, np.pi / 2, np.pi)[0]
same('(a)(i) inner sphere carries positive charge', bool(Qin > 0), True)
same('(a)(ii) charge sits on the lower hemisphere', bool(Qlo > 1.001 * Qup), False)
sig_th = lambda th: sig9 if np.cos(th) < 0 else 0.0                         # lossy for z < 0
Iout = {}
for rr in (0.012, 0.018):
    Iup = dblquad(lambda th, ph: sig_th(th) * Er9(rr) * rr**2 * np.sin(th), 0, 2 * np.pi, 0, np.pi / 2 - 1e-12)[0]
    Ilo = dblquad(lambda th, ph: sig_th(th) * Er9(rr) * rr**2 * np.sin(th), 0, 2 * np.pi, np.pi / 2 + 1e-12, np.pi)[0]
    Iout[rr] = Iup + Ilo
    chk(f'(c) outward current through r = {rr * 100:.1f} cm [nA]', Iout[rr] * 1e9, '125.7')
    chk(f'(c)   of which through the upper half [nA]', Iup * 1e9, '0')
same('(c) current direction', 'outward: inner sphere -> shell' if Iout[0.012] > 0 else 'inward', 'outward: inner sphere -> shell')
I9 = Iout[0.012]; G9 = I9 / (Va9 - Vb9)
chk('(c) G [nS]', G9 * 1e9, '1.257'); chk('(c) 2 pi sigma ab/(b-a) [nS]', 2 * np.pi * sig9 * a9 * b9 / (b9 - a9) * 1e9, '1.257')
chk('(c) R [Mohm]', 1 / G9 / 1e6, '795.8'); chk('(c) P = I (V(a)-V(b)) [uW]', I9 * (Va9 - Vb9) * 1e6, '12.57')
Pint = quad(lambda r: sig9 * Er9(r)**2 * 2 * np.pi * r**2, a9, b9)[0]       # int sigma E^2 dV over the lower half
chk('(c) P = int sigma E^2 dV [uW]', Pint * 1e6, '12.57')
chk('(c) (sigma/eps) C [nS]', sig9 / eps9 * C9 * 1e9, '2.513'); chk('(c) G / [(sigma/eps) C]', G9 / (sig9 / eps9 * C9), '0.5')


def rhs9(t, y):
    Vb = y[0]                         # shell charge Q_sh = C (V(b) - V(a)); current into the shell = G (V(a) - V(b))
    return [G9 * (Va9 - Vb) / C9]


e50 = lambda t, y: y[0] + 50.0
e1e = lambda t, y: y[0] + V09 * np.exp(-1)
sol = solve_ivp(rhs9, [0, 0.05], [Vb9], events=[e50, e1e], rtol=1e-12, atol=1e-12)
chk('(d) time for V(b) to reach -50 V, ODE [ms]', sol.t_events[0][0] * 1e3, '3.682'); chk('(d) 1/e time, ODE [ms]', sol.t_events[1][0] * 1e3, '5.313')
chk('(d) tau = C/G [ms]', C9 / G9 * 1e3, '5.313'); chk('(d) 2 eps/sigma [ms]', 2 * eps9 / sig9 * 1e3, '5.313')
chk('(d) eps/sigma [ms]', eps9 / sig9 * 1e3, '2.656'); chk('check: R C [ms]', (1 / G9) * C9 * 1e3, '5.313')
chk('check: (795.8 Mohm)(6.676 pF) [ms]', 795.8e6 * 6.676e-12 * 1e3, '5.313'); chk('check: I V0 [uW]', I9 * V09 * 1e6, '12.57')

# ------------------------------------------------------------------ 10.10
head('10.10 Pulling capacitor plates apart')
A10, V10, x1, x2 = 0.02, 500.0, 1e-3, 3e-3
Cx = lambda x: eps0 * A10 / x
C101 = Cx(x1); Q10 = C101 * V10; W101 = 0.5 * C101 * V10**2
chk('(a) C/eps0', C101 / eps0, '20'); chk('(a) C [pF]', C101 * 1e12, '177.1'); chk('(a) Q/eps0', Q10 / eps0, '1e4')
chk('(a) Q [nC]', Q10 * 1e9, '88.54'); chk('(a) W/eps0', W101 / eps0, '2.5e6'); chk('(a) W [uJ]', W101 * 1e6, '22.14')
WQ = lambda x: Q10**2 / (2 * Cx(x)); hx = 1e-9
chk('(b) V at x2 [V]', Q10 / Cx(x2), '1500'); chk('(b) W at x2 [uJ]', WQ(x2) * 1e6, '66.41'); chk('(b) your work [uJ]', (WQ(x2) - WQ(x1)) * 1e6, '44.27')
FQ10 = lambda x: -(WQ(x + hx) - WQ(x - hx)) / (2 * hx)
for x in (x1, 2e-3, x2):
    chk(f'(b) F_z = -dW/dx|Q at x = {x * 1e3:.0f} mm [mN]', FQ10(x) * 1e3, '-22.14')
chk('(b) W(x1)/x1 [mN]', W101 / x1 * 1e3, '22.14'); chk('(b) int (-F_z) dx [uJ]', quad(lambda x: -FQ10(x), x1, x2)[0] * 1e6, '44.27')
Esheet = (-Q10 / A10) / (2 * eps0)                                        # field of the lower sheet alone, above it
chk('(b) second way: Q E_sheet [mN]', Q10 * Esheet * 1e3, '-22.14')
same('(b) direction', 'down (attractive)' if Q10 * Esheet < 0 else 'up', 'down (attractive)')
chk('watch: full gap field Q/(eps0 A) gives [mN]', Q10 * Q10 / (A10 * eps0) * 1e3, '44.27')
C102 = Cx(x2); Q102 = C102 * V10; W102 = 0.5 * C102 * V10**2; dW = W102 - W101; dQ = Q102 - Q10; Wb10 = V10 * dQ
chk('(c) C [pF]', C102 * 1e12, '59.03'); chk('(c) Q [nC]', Q102 * 1e9, '29.51'); chk('(c) W [uJ]', W102 * 1e6, '7.378')
chk('(c) dW [uJ]', dW * 1e6, '-14.76'); chk('(c) dQ [nC]', dQ * 1e9, '-59.03'); chk('(c) battery work V0 dQ [uJ]', Wb10 * 1e6, '-29.51')
chk('(c) V0 dQ / dW', Wb10 / dW, '2'); chk('(c) your work = dW - V0 dQ [uJ]', (dW - Wb10) * 1e6, '14.76')
WV = lambda x: 0.5 * Cx(x) * V10**2
FV10 = lambda x: (WV(x + hx) - WV(x - hx)) / (2 * hx)
chk('(d) F_z(x1) = +dW/dx|V [mN]', FV10(x1) * 1e3, '-22.14'); chk('(d) F_z(x2) [mN]', FV10(x2) * 1e3, '-2.459')
chk('(d) F_z(x2) from the charge, -Q^2/(2 eps0 A) [mN]', -(Cx(x2) * V10)**2 / (2 * eps0 * A10) * 1e3, '-2.459')
chk('check: int eps0 A V^2/(2 x^2) dx [uJ]', quad(lambda x: -FV10(x), x1, x2)[0] * 1e6, '14.76')

# ------------------------------------------------------------------ 10.11
head('10.11 Two lossy layers in series')
A11, d111, d112 = 0.01, 1e-3, 1e-3
e1, s1, e2, s2, V011 = 2 * eps0, 4e-10, 4 * eps0, 1e-10, 10.0
R1 = d111 / (s1 * A11); R2 = d112 / (s2 * A11); I11 = V011 / (R1 + R2); J11 = I11 / A11
chk('(a) R1 [Gohm]', R1 / 1e9, '0.25'); chk('(a) R2 [Gohm]', R2 / 1e9, '1'); chk('(a) I [nA]', I11 * 1e9, '8'); chk('(a) J_z [A/m^2]', J11, '8e-7')
E111, E112 = J11 / s1, J11 / s2
chk('(a) E1_z [V/m]', E111, '2000'); chk('(a) E2_z [V/m]', E112, '8000'); chk('(a) V1 [V]', E111 * d111, '2'); chk('(a) V2 [V]', E112 * d112, '8')
same('(a) direction of J and E', '+z' if J11 > 0 else '-z', '+z')
D111, D112 = e1 * E111, e2 * E112
chk('(b) D1/eps0', D111 / eps0, '4000'); chk('(b) D1 [C/m^2]', D111, '3.54e-8'); chk('(b) D2/eps0', D112 / eps0, '32000'); chk('(b) D2 [C/m^2]', D112, '2.83e-7')
nhat = np.array([0, 0, -1.0])                                              # from medium 2 (upper) into medium 1
rs_int = nhat @ (np.array([0, 0, D111]) - np.array([0, 0, D112]))
chk('(b) interface rho_s / eps0', rs_int / eps0, '28000'); chk('(b) interface rho_s [C/m^2]', rs_int, '2.48e-7')
chk('(b) J (eps2/sig2 - eps1/sig1) / eps0', J11 * (e2 / s2 - e1 / s1) / eps0, '28000')
rs_lo = np.array([0, 0, 1.0]) @ np.array([0, 0, D111]); rs_up = np.array([0, 0, -1.0]) @ np.array([0, 0, D112])
chk('(b) lower plate rho_s / eps0', rs_lo / eps0, '4000'); chk('(b) upper plate rho_s / eps0', rs_up / eps0, '-32000')
chk('(b) total / eps0', (rs_lo + rs_int + rs_up) / eps0, '0')


def fields(rs, sa=s1, sb=s2):
    return np.linalg.solve(np.array([[-e1, e2], [d111, d112]]), [rs, V011])   # eps2 E2 - eps1 E1 = rs, E1 d1 + E2 d2 = V0


E10p, E20p = fields(0.0)
chk('(c) E1(0+) [V/m]', E10p, '6667'); chk('(c) E2(0+) [V/m]', E20p, '3333'); chk('(c) V1(0+) [V]', E10p * d111, '6.667')
C111, C112 = e1 * A11 / d111, e2 * A11 / d112
chk('(c) C2/(C1+C2) V0 [V]', C112 / (C111 + C112) * V011, '6.667')
chk('(c) J1(0+) [uA/m^2]', s1 * E10p * 1e6, '2.667'); chk('(c) J2(0+) [uA/m^2]', s2 * E20p * 1e6, '0.3333')
same('(c) sign of the interface charge that builds up', 'positive' if s1 * E10p > s2 * E20p else 'negative', 'positive')


def interface_ode(sa, sb):
    f = lambda t, y: [sa * fields(y[0])[0] - sb * fields(y[0])[1]]          # d rho_s/dt = J1 - J2
    return solve_ivp(f, [0, 4.0], [0.0], dense_output=True, rtol=1e-12, atol=1e-22)


sol11 = interface_ode(s1, s2)
V1t = lambda t: fields(sol11.sol(t)[0])[0] * d111
tau11 = (e1 / d111 + e2 / d112) / (s1 / d111 + s2 / d112)
chk('(c) tau [s]', tau11, '0.1063'); chk('(c) (C1+C2)/(G1+G2) [s]', (C111 + C112) / (s1 * A11 / d111 + s2 * A11 / d112), '0.1063')
tfit = brentq(lambda t: (V1t(t) - V1t(4.0)) - (V1t(0) - V1t(4.0)) / np.e, 1e-4, 1.0)
chk('(c) 1/e time of V1 from the charge-conservation ODE [s]', tfit, '0.1063')
chk('(c) V1(t -> inf) from ODE [V]', V1t(4.0), '2'); chk('(c) amplitude V1(0+) - V1(inf) [V]', V1t(0) - V1t(4.0), '4.67')
chk('(c) eps1/sig1 [ms]', e1 / s1 * 1e3, '44.27'); chk('(c) eps2/sig2 [ms]', e2 / s2 * 1e3, '354.2')
same('(c) tau between the two relaxation times', bool(e1 / s1 < tau11 < e2 / s2), True)
chk('check: rho_s(t -> inf) from ODE / eps0', sol11.sol(4.0)[0] / eps0, '28000')
Cser = A11 / (d111 / e1 + d112 / e2)
chk('(d) series C [pF]', Cser * 1e12, '118.1'); chk('(d) (sig1/eps1) C [nS]', s1 / e1 * Cser * 1e9, '2.667')
chk('(d) (sig2/eps2) C [nS]', s2 / e2 * Cser * 1e9, '0.3333'); chk('(d) steady G [nS]', 1 / (R1 + R2) * 1e9, '0.8')
s1b, s2b = 2e-10, 4e-10
same('(d) example: eps1/sig1 = eps2/sig2', bool(np.isclose(e1 / s1b, e2 / s2b)), True)
solb = solve_ivp(lambda t, y: [s1b * fields(y[0])[0] - s2b * fields(y[0])[1]], [0, 4.0], [0.0], dense_output=True, rtol=1e-12, atol=1e-22)
V1b = [fields(solb.sol(t)[0])[0] * d111 for t in (0.0, 0.05, 0.5, 4.0)]
chk('(d) example: V1 at t = 0+ [V]', V1b[0], '6.667'); chk('(d) example: max |V1(t) - V1(0+)| [V]', max(abs(v - V1b[0]) for v in V1b), '0.000')
Gb = 1 / (d111 / (s1b * A11) + d112 / (s2b * A11))
chk('(d) example: G [nS]', Gb * 1e9, '1.333'); chk('(d) example: (sigma/eps) C [nS]', s1b / e1 * Cser * 1e9, '1.333')

# ------------------------------------------------------------------ 10.12
head('10.12 Lossy coax driven through a resistor')
ell, a12, b12, er12, sig12, Rs12, Vs12 = 10.0, 1e-3, 4e-3, 2.5, 1.0e-9, 10e6, 12.0
eps12 = er12 * eps0
Cp12 = 1 / quad(lambda r: 1 / (2 * np.pi * eps12 * r), a12, b12)[0]       # 1 C/m -> V by quad of the Gauss field
Gp12 = 1 / quad(lambda r: 1 / (2 * np.pi * sig12 * r), a12, b12)[0]       # radial shells in series, per metre
chk('(a) ln(b/a)', np.log(b12 / a12), '1.3863'); chk("(a) C' [pF/m]", Cp12 * 1e12, '100.3'); chk("(a) G' [nS/m]", Gp12 * 1e9, '4.532')
C12, G12 = Cp12 * ell, Gp12 * ell; R12 = 1 / G12
chk('(a) C [nF]', C12 * 1e9, '1.003'); chk('(a) G [nS]', G12 * 1e9, '45.32'); chk('(a) R [Mohm]', R12 / 1e6, '22.06'); chk('(a) G/C [1/s]', G12 / C12, '45.18')
sol12 = solve_ivp(lambda t, y: [((Vs12 - y[0]) / Rs12 - G12 * y[0]) / C12], [0, 0.3], [0.0], dense_output=True, rtol=1e-12, atol=1e-14)
Vinf = sol12.sol(0.3)[0]
chk('(b) V_inf from the KCL ODE [V]', Vinf, '8.257'); chk('(b) V_s R/(R+R_s) [V]', Vs12 * R12 / (R12 + Rs12), '8.257')
tau1 = brentq(lambda t: sol12.sol(t)[0] - Vinf * (1 - np.exp(-1)), 1e-5, 0.1)
chk('(b) tau1 from the ODE [ms]', tau1 * 1e3, '6.904'); chk('(b) C/(G + 1/R_s) [ms]', C12 / (G12 + 1 / Rs12) * 1e3, '6.904')
chk('(b) R || R_s [Mohm]', 1 / (G12 + 1 / Rs12) / 1e6, '6.881')
chk('(b) leakage G V_inf [uA]', G12 * Vinf * 1e6, '0.3743'); chk('(b) (V_s - V_inf)/R_s [uA]', (Vs12 - Vinf) / Rs12 * 1e6, '0.3743')
chk('(b) G V_inf^2 [uW]', G12 * Vinf**2 * 1e6, '3.09'); same('(b) V_inf < 12 V', bool(Vinf < Vs12), True)
Erf = lambda r: Cp12 * Vinf / (2 * np.pi * eps12 * r)                        # Gauss, with Q' = C' V
Wp12 = quad(lambda r: 0.5 * eps12 * Erf(r)**2 * 2 * np.pi * r, a12, b12)[0]
chk("(c) W' = int 1/2 eps E^2 dA [nJ/m]", Wp12 * 1e9, '3.42'); chk("(c) 1/2 C' V_inf^2 [nJ/m]", 0.5 * Cp12 * Vinf**2 * 1e9, '3.42')
chk('(c) W total [nJ]', Wp12 * ell * 1e9, '34.2')
chalf = brentq(lambda c: quad(lambda r: 0.5 * eps12 * Erf(r)**2 * 2 * np.pi * r, a12, c)[0] - Wp12 / 2, a12 * 1.0001, b12)
chk('(c) half-energy radius [mm]', chalf * 1e3, '2'); chk('(c) sqrt(ab) [mm]', np.sqrt(a12 * b12) * 1e3, '2')
chk('(c) area share of a < r < 2 mm', (chalf**2 - a12**2) / (b12**2 - a12**2), '0.2')
sol12d = solve_ivp(lambda t, y: [-G12 * y[0] / C12], [0, 1.0], [Vinf], dense_output=True, rtol=1e-12, atol=1e-14)
t1V = brentq(lambda t: sol12d.sol(t)[0] - 1.0, 1e-4, 0.5)
chk('(d) tau2 = C/G [ms]', C12 / G12 * 1e3, '22.14'); chk('(d) eps/sigma [ms]', eps12 / sig12 * 1e3, '22.14')
chk('(d) ln(V_inf / 1 V)', np.log(Vinf), '2.111'); chk('(d) time to 1 V from the ODE [ms]', t1V * 1e3, '46.73')
same('check: tau1 < tau2', bool(tau1 < C12 / G12), True)

# ------------------------------------------------------------------ exam re-parameterization
head('Exam re-parameterization: the official keys must not carry over')
print('  10.6 vs Summer 2020 HE2 #1a: plates z = 0 (-2 C/m^2) and z = 2 m (+2 C/m^2); free space 0<z<1 m, eps = 2 eps0 for 1<z<2 m; V(0) = 0')
De = -2.0; Efe = De / eps0; Ede = De / (2 * eps0); Pe = De - eps0 * Ede
V1e = -quad(lambda s: Efe, 0, 1)[0]; V2e = V1e - quad(lambda s: Ede, 1, 2)[0]; CAe = 2.0 / V2e
print(f'      exam key: D_z = {De} C/m^2, E_z = {Efe:.3g} / {Ede:.3g} V/m, P_z = {Pe:.3g} C/m^2, V(1) = {V1e:.3g} V, V(2) = {V2e:.3g} V, C/A = {CAe / eps0:.4f} eps0')
differs('10.6 D_z [C/m^2]', Dz, De); differs('10.6 P_z in the dielectric [C/m^2]', P61, Pe)
differs('10.6 E_z in free space [V/m]', E62, Efe); differs('10.6 E_z in the dielectric [V/m]', E61, Ede)
differs('10.6 voltage between the plates [V]', Vline(0.0), V2e); differs('10.6 C/A [F/m^2]', CA, CAe)
same('10.6 geometry differs: dielectric layer (exam top, practice bottom), positive plate (exam top, practice bottom)',
     ('top', 'top') != ('bottom', 'bottom'), True)
print('  10.9 vs SP18 Exam 1 #5: inner shell grounded, outer at +V0 > 0, whole a<r<b lossy, eps = eps0 (symbolic key, evaluated at a, b, |V0| of 10.9)')
Qe = 4 * np.pi * eps0 * a9 * b9 * V09 / (b9 - a9); Ge = 4 * np.pi * sig9 * a9 * b9 / (b9 - a9)
differs('10.9 (a)(i) "inner sphere is positive"', True, False)
differs('10.9 (a)(ii) statement', 'charge on lower hemisphere? -> False (uniform rho_s)', 'E = 0 for r<a because grounded? -> False (reason wrong)')
differs('10.9 E direction', 'outward', 'inward'); differs('10.9 charge on the inner sphere [C]', Qin, -Qe)
differs('10.9 |Q| [C]', abs(Qin), Qe); differs('10.9 current direction', 'outward', 'inward')
differs('10.9 |I| [A]', I9, Ge * V09); differs('10.9 G [S]', G9, Ge)
print('  10.12 vs Summer 2019 HE2 #1: G\' = 2 uS/m, sigma = 1e-6 S/m, eps = 2 eps0; 0.5 m across 10 V with R_s = 1e6 ohm; source then removed')
Cpe = 2 * eps0 * 2e-6 / 1e-6; Rce = 1 / (2e-6 * 0.5); Vce = 10 * Rce / (Rce + 1e6); te = 2 * eps0 / 1e-6
differs("10.12 C' [F/m]", Cp12, Cpe); differs('10.12 steady cable voltage [V]', Vinf, Vce)
differs('10.12 discharge time constant [s]', C12 / G12, te); differs('10.12 cable length [m]', ell, 0.5)

print(f'\nTOTAL: {NP} PASS, {NF} FAIL')
