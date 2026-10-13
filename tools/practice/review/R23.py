#!/usr/bin/env python3
"""R23 -- independent re-solution of practice/23-imperfect-dielectrics-and-good-conductors.md.

Every regime shortcut is checked against the exact gamma = sqrt(j w mu (sigma + j w eps)) and
eta = sqrt(j w mu / (sigma + j w eps)) (principal roots), plus brute-force routes:
ODE integration of the 1-D phasor Maxwell equations (23.9), finite-difference Poynting balance and
quad of the Joule heat (23.7, 23.12), Bessel-function round wire (23.12), np.cross for directions,
random sampling for alpha < beta.  numpy/scipy only.
"""
import numpy as np
from scipy import integrate, special

E0A = 1e-9 / (36 * np.pi)          # course constant
E0 = 8.8541878128e-12              # CODATA
MU0 = 4e-7 * np.pi
CA = 1 / np.sqrt(MU0 * E0A)        # exactly 3e8
C = 1 / np.sqrt(MU0 * E0)
ETA0A = 120 * np.pi
ETA0 = np.sqrt(MU0 / E0)
DB = 20 * np.log10(np.e)           # 8.686 dB per neper
X, Y, Z = np.eye(3)
NFAIL = 0


def ulp(s):
    s = s.lower()
    m, e = (s.split('e') + ['0'])[:2]
    d = len(m.split('.')[1]) if '.' in m else 0
    return 10.0 ** (int(e) - d)


def chk(name, val, stated, tol=None):
    """PASS if val rounds to the stated string (half a unit in its last digit) or is within tol."""
    global NFAIL
    tgt = float(stated)
    t = 0.5 * ulp(stated) * (1 + 1e-9) if tol is None else tol
    ok = abs(val - tgt) <= t
    NFAIL += (not ok)
    print(f"  {'PASS' if ok else 'FAIL'}  {name}: computed {val:.6g}  page {stated}")
    return ok


def same(name, cond, note=''):
    global NFAIL
    NFAIL += (not cond)
    print(f"  {'PASS' if cond else 'FAIL'}  {name} {note}")


def exact(sig, er, f, e0=E0A, mur=1.0):
    w = 2 * np.pi * f
    eps, mu = er * e0, mur * MU0
    g = np.sqrt(1j * w * mu * (sig + 1j * w * eps))
    eta = np.sqrt(1j * w * mu / (sig + 1j * w * eps))
    assert g.real >= 0 and g.imag > 0 and eta.real > 0
    return dict(w=w, p=sig / (w * eps), g=g, eta=eta, a=g.real, b=g.imag, d=1 / g.real,
                lam=2 * np.pi / g.imag, vp=w / g.imag, ea=abs(eta), tau=np.degrees(np.angle(eta)))


def good(sig, f, mur=1.0):
    d = 1 / np.sqrt(np.pi * f * mur * MU0 * sig)
    return dict(d=d, a=1 / d, b=1 / d, lam=2 * np.pi * d, vp=2 * np.pi * f * d,
                eta=(1 + 1j) / (sig * d), ea=np.sqrt(2) / (sig * d))


def diel(sig, er, f, e0=E0A, eta0=None):
    w = 2 * np.pi * f
    ea = np.sqrt(MU0 / (er * e0)) if eta0 is None else eta0 / np.sqrt(er)
    b = w * np.sqrt(MU0 * er * e0)
    return dict(a=sig / 2 * ea, b=b, ea=ea, tau=np.degrees(sig / (2 * w * er * e0)),
                d=2 / (sig * ea), lam=2 * np.pi / b, vp=w / b)


def regime(p):
    return 'GC' if p > 10 else ('ID' if p < 0.1 else 'neither')


# ---------------------------------------------------------------------------------------------
print("23.1  six media at 3 MHz")
media = [('copper', 5.8e7, 1, '1.04e18', '3.5e11', 'GC'), ('seawater', 4, 81, '0.889e9', '296', 'GC'),
         ('moist soil', 1e-2, 10, '18e6', '6.0', 'neither'), ('fresh water', 1e-3, 80, '225e3', '0.075', 'ID'),
         ('dry earth', 1e-5, 5, '36e3', '0.012', 'ID'), ('Bakelite', 1e-9, 4.9, '3.67', '1.2e-6', 'ID')]
for nm, s, er, fcs, ps, v in media:
    fc = s / (2 * np.pi * er * E0A)
    p = exact(s, er, 3e6)['p']
    chk(f'f_c {nm}', fc, fcs)
    chk(f'p(3 MHz) {nm}', p, ps)
    same(f'verdict {nm} = {v}', regime(p) == v, f'({regime(p)})')
    # precise eps0 must not change any verdict
    same(f'verdict {nm} with CODATA eps0', regime(exact(s, er, 3e6, E0)['p']) == v)
m, g = exact(1e-2, 10, 3e6), good(1e-2, 3e6)
chk('moist soil: GC alpha too high [%]', 100 * (g['a'] / m['a'] - 1), '8.6', tol=0.06)
chk('moist soil: GC beta too low [%]', 100 * (1 - g['b'] / m['b']), '8.0')
chk('(c) fresh water with eps0 alone', 18e9 * 1e-3 / 3e6, '6')
same('(c) verdict with eps0 alone is neither', regime(6) == 'neither')
chk('seawater ID above 10 f_c [GHz]', 10 * 4 / (2 * np.pi * 81 * E0A) / 1e9, '9', tol=0.12)
chk('Bakelite GC below f_c/10 [Hz]', 1e-9 / (2 * np.pi * 4.9 * E0A) / 10, '0.37')

# ---------------------------------------------------------------------------------------------
print("23.2  good-conductor multiple choice (sample: seawater at 1 kHz)")
sw = exact(4, 81, 1e3)
gsw = good(4, 1e3)
chk('tau seawater 1 kHz [deg]', sw['tau'], '44.99997')
chk('tau seawater 1 kHz, CODATA eps0 [deg]', exact(4, 81, 1e3, E0)['tau'], '44.99997')
chk('T/8 at 1 kHz [us]', 1e6 / 1e3 / 8, '125')
chk('(a) v_p = w delta [m/s]', gsw['vp'], '5e4')
chk('(a) exact v_p [m/s]', sw['vp'], '5e4')
chk('(a) lossless 1/sqrt(mu eps) [m/s]', CA / 9, '3.3e7')
same('(a) false: v_p << 1/sqrt(mu eps)', sw['vp'] < CA / 9)
chk('(b) delta(2f)/delta(f) [%]', 100 * good(4, 2e3)['d'] / gsw['d'], '71')
same('(b) false: ratio != 0.5', abs(good(4, 2e3)['d'] / gsw['d'] - 0.5) > 0.1)
same('(c) true: H lags E by tau -> T/8', abs(sw['tau'] - 45) < 1e-4)
chk('(d) |eta| seawater [ohm]', sw['ea'], '0.0444')
chk('(d) sqrt(mu/eps) [ohm]', np.sqrt(MU0 / (81 * E0A)), '41.9')
chk('(d) sqrt(mu/eps) CODATA [ohm]', np.sqrt(MU0 / (81 * E0)), '41.9')
chk('(e) field over 1 lambda 1/e^{-2pi}', np.exp(2 * np.pi), '535')
chk('(e) power over 1 lambda', np.exp(-2 * sw['a'] * sw['lam']), '3.5e-6')
chk('(e) dB per wavelength', 10 * np.log10(np.exp(2 * sw['a'] * sw['lam'])), '54.6')
same('(e) false: power factor is e^{-4pi}, not e^{-2pi}', abs(np.exp(-2 * sw['a'] * sw['lam']) - np.exp(-2 * np.pi)) > 1e-3)

# ---------------------------------------------------------------------------------------------
print("23.3  true/false")
# (a) phasor angle: displacement current leads total current by atan(sigma/w eps)
for sig, er, f in [(4, 81, 1e9), (1e-3, 80, 1e6), (1e-2, 10, 3e6)]:
    w = 2 * np.pi * f
    Jc, Jd = sig * 1.0, 1j * w * er * E0A * 1.0
    lead = np.angle(Jd) - np.angle(Jc + Jd)
    same(f'(a) tan(lead of J_d over J_tot) = sigma/w eps  (f={f:g})', abs(np.tan(lead) - sig / (w * er * E0A)) < 1e-9 * max(1, sig / (w * er * E0A)))
fw1 = exact(1e-3, 80, 1e6)
chk('(b) fresh water 1 MHz p', fw1['p'], '0.225')
same('(b) false: neither regime', regime(fw1['p']) == 'neither')
chk('(b) with eps0 only', 18e9 * 1e-3 / 1e6, '18')
fcs = 4 / (2 * np.pi * 81 * E0A)
chk('(c) seawater f_c [GHz]', fcs / 1e9, '0.89')
chk('(c) GC below [MHz]', fcs / 10 / 1e6, '89')
chk('(c) p at 1 GHz', exact(4, 81, 1e9)['p'], '0.89')
chk('(c) p at 10 GHz', exact(4, 81, 1e10)['p'], '0.089')
rng = np.random.default_rng(23)
N = 200000
sig = 10 ** rng.uniform(-12, 8, N); er = 10 ** rng.uniform(0, 2, N); mur = 10 ** rng.uniform(0, 3, N); f = 10 ** rng.uniform(0, 12, N)
w = 2 * np.pi * f
gam = np.sqrt(1j * w * mur * MU0 * (sig + 1j * w * er * E0A))
pp = sig / (w * er * E0A)
same('(d) alpha < beta strictly in random media with p < 1e12', np.all(gam.real[pp < 1e12] < gam.imag[pp < 1e12]), f'({np.sum(pp < 1e12)} media)')
same('(d) alpha <= beta (1 + 1e-12) in all 200000 random media', np.all(gam.real <= gam.imag * (1 + 1e-12)))
same('(d) tau < 45 deg in all random media', np.all(np.angle(np.sqrt(1j * w * mur * MU0 / (sig + 1j * w * er * E0A))) < np.pi / 4 + 1e-15))
for ff, bs in [(1e8, '18.7'), (2e8, '37.5')]:
    m = exact(1e-3, 80, ff)
    chk(f'(e) fresh water exact alpha at {ff:g} Hz', m['a'], '0.0211')
    chk(f'(e) fresh water exact beta at {ff:g} Hz', m['b'], bs)
m = exact(1e-3, 80, 1e8)
chk('(f) p at 100 MHz', m['p'], '0.00225')
chk('(f) penetration depth (2/sigma)sqrt(eps/mu) [m]', diel(1e-3, 80, 1e8)['d'], '47')
chk('(f) exact 1/alpha [m]', m['d'], '47')
chk('(f) skin-depth formula [m]', good(1e-3, 1e8)['d'], '1.6')
chk('(f) ratio', m['d'] / good(1e-3, 1e8)['d'], '30')

# ---------------------------------------------------------------------------------------------
print("23.4  gold sigma = 4.1e7 S/m")
K = np.pi * MU0 * 4.1e7
chk('pi mu0 sigma', K, '161.9')
chk('delta sqrt(f) [m]', 1 / np.sqrt(K), '0.0786')
chk('delta 60 Hz [mm]', 1e3 * good(4.1e7, 60)['d'], '10.1')
chk('delta 1 MHz [um]', 1e6 * good(4.1e7, 1e6)['d'], '78.6')
chk('delta 4 MHz [um]', 1e6 * good(4.1e7, 4e6)['d'], '39.3')
chk('delta 10 GHz [um]', 1e6 * good(4.1e7, 1e10)['d'], '0.786')
chk('exact delta 10 GHz [um]', 1e6 * exact(4.1e7, 1, 1e10, E0)['d'], '0.786')
chk('sigma/(w eps0) at 10 GHz', exact(4.1e7, 1, 1e10, E0)['p'], '7e7')
n = 1.5e-6 / good(4.1e7, 1e10)['d']
chk('(c) plating in skin depths', n, '1.91')
chk('(c) power left at back [%]', 100 * np.exp(-2 * n), '2.2')
chk('(c) power absorbed [%]', 100 * (1 - np.exp(-2 * n)), '97.8')
chk('(c) field at back [%]', 100 * np.exp(-n), '15')
chk('(c) f where delta = 1.5 um [GHz]', 1 / (K * 1.5e-6 ** 2) / 1e9, '2.75')

# ---------------------------------------------------------------------------------------------
print("23.5  E = x 0.5 e^{0.4z} e^{j0.4z}, z up, water z<0")
a = b = 0.4
# crest position omega t + 0.4 z = 0 -> dz/dt = -omega/0.4 < 0 : downward
same('(a) travel toward -z', -1 / 0.4 < 0)
u = -Z
Hdir = np.cross(u, X)
same('(a)/(b) H along -y', np.allclose(Hdir, -Y))
Sdir = np.cross(X, Hdir)
same('(b) S along -z', np.allclose(Sdir, -Z))
chk('(b) |S| coefficient 0.25 cos45/2', 0.25 * np.cos(np.pi / 4) / 2, '0.0884')
chk('(c) factor per metre', np.exp(-0.8), '0.449')
chk('(c) dB/m', 10 * np.log10(np.exp(0.8)), '3.47')
d30 = 3 * np.log(10) / 0.8
chk('(d) 30 dB depth [m]', d30, '8.63')
chk('(d) field there [%]', 100 * np.exp(-0.4 * d30), '3.2')
fz = a ** 2 / (np.pi * MU0 * 4)
chk('(e) f [kHz]', fz / 1e3, '10.1')
m = exact(4, 81, fz)
chk('(e) p with 81 eps0', m['p'], '8.8e4')
chk('(e) exact alpha at that f', m['a'], '0.4', tol=1e-4)
chk('(e) exact beta at that f', m['b'], '0.4', tol=1e-4)
chk('(e) |eta| [ohm]', m['ea'], '0.141')
# brute force: build phasors with the exact eta and take 1/2 Re{E x H*} at z = 0 and z = -3
for zz in (0.0, -3.0):
    Ev = X * 0.5 * np.exp(m['g'] * zz)
    Hv = np.cross(u, Ev) / m['eta']
    S = 0.5 * np.real(np.cross(Ev, np.conj(Hv)))
    chk(f'(e) S_z(z={zz}) brute force vs -0.625 e^(0.8z)', S[2], f'{-0.625 * np.exp(0.8 * zz):.4g}', tol=2e-3 * 0.625)
chk('(e) <S>(0) magnitude [W/m^2]', 0.25 * np.cos(np.pi / 4) / 2 / m['ea'], '0.625')

# ---------------------------------------------------------------------------------------------
print("23.6  measured lambda = 1000 m, delta = 159.2 m at 1 kHz")
f = 1e3; w = 2 * np.pi * f
al, be = 1 / 159.2, 2 * np.pi / 1000
chk('(a) alpha [1/m]', al, '6.28e-3')
chk('(a) beta [1/m]', be, '6.28e-3')
chk('(a) alpha/beta', al / be, '0.9997')
tau = np.arctan(al / be)
same('(a) tan(2 tau) in the thousands', 1000 <= np.tan(2 * tau) < 10000, f'({np.tan(2 * tau):.0f})')
chk('(b) v_p [m/s]', w / be, '1e6')
chk('(b) c/v_p', CA / (w / be), '300')
chk('(b) c/sqrt(10) [m/s]', CA / np.sqrt(10), '9.5e7')
chk('(b) slow-down factor', CA / np.sqrt(10) / (w / be), '100', tol=10)
sgc = 1 / (np.pi * f * MU0 * 159.2 ** 2)
chk('(c) sigma GC [S/m]', sgc, '9.99e-3')
sex = 2 * al * be / (w * MU0)                     # Re{gamma/eta} from gamma eta = j w mu
g_ = al + 1j * be; eta_ = 1j * w * MU0 / g_
same('(c) Re{gamma/eta} equals 2 alpha beta/(w mu)', abs((g_ / eta_).real - sex) < 1e-12)
chk('(c) sigma exact route [S/m]', sex, '1.0e-2')
md = exact(1e-2, 10, f)                            # moist soil check (any small eps_r)
chk('(d) |eta| with sigma=1e-2 [ohm]', np.sqrt(w * MU0 / 1e-2), '0.889')
chk('(d) Re eta [ohm]', np.sqrt(w * MU0 / 1e-2) / np.sqrt(2), '0.628')
chk('(d) 1/(sigma delta) [ohm]', 1 / (1e-2 * 159.2), '0.628')
chk('(d) |eta| directly from data, j w mu/gamma [ohm]', abs(eta_), '0.889')
chk('(d) angle eta from data [deg]', np.degrees(np.angle(eta_)), '45', tol=0.05)
for dd, s in [(159.15, '-5.6'), (159.2, '51'), (159.25, '107')]:
    a_ = 1 / dd
    chk(f'(e) eps_r from delta={dd}', (be ** 2 - a_ ** 2) / (w ** 2 * MU0 * E0A), s)
    chk(f'(e) eps_r from delta={dd}, CODATA', (be ** 2 - a_ ** 2) / (w ** 2 * MU0 * E0), s)
chk('(e) 0.1 m change in delta [%]', 100 * 0.1 / 159.2, '0.06')
chk('(e) eps bound sigma/(10 w) [F/m]', 1e-2 / (10 * w), '1.6e-7')
chk('(e) eps_r bound', 1e-2 / (10 * w) / E0A, '1.8e4')
chk('(e) eps_r bound CODATA', 1e-2 / (10 * w) / E0, '1.8e4')
for er, ds, ls in [(1, '159.2', '1000'), (10, '159.2', '1000'), (1000, '159.6', '997')]:
    m = exact(1e-2, er, f)
    chk(f'check eps_r={er} delta [m]', m['d'], ds)
    chk(f'check eps_r={er} lambda [m]', m['lam'], ls)
chk('check p for eps_r = 10', exact(1e-2, 10, f)['p'], '1.8e4')
chk('watch-out (c/v_p)^2', (CA / 1e6) ** 2, '9e4')

# ---------------------------------------------------------------------------------------------
print("23.7  fresh water 100 MHz, divers 10 m apart")
f = 1e8
m = exact(1e-3, 80, f)
d = diel(1e-3, 80, f, eta0=ETA0A)
chk('(a) p', m['p'], '2.25e-3')
chk('(b) |eta| ID [ohm]', d['ea'], '42.1')
chk('(b) tau [deg]', d['tau'], '0.064')
chk('(b) tau [rad]', np.radians(d['tau']), '1.125e-3')
chk('(b) alpha [Np/m]', d['a'], '0.0211')
chk('(b) delta [m]', d['d'], '47.5')
chk('(b) beta [rad/m]', d['b'], '18.7')
chk('(b) lambda [m]', d['lam'], '0.335')
chk('(b) v_p [m/s]', d['vp'], '3.35e7')
same('(b) H along -y', np.allclose(np.cross(X, Z), -Y))
same('(b) E x H along +x', np.allclose(np.cross(Z, -Y), X))
chk('(b) |H0| [mA/m]', 1e3 * 0.5 / d['ea'], '11.9')
rel = max(abs(m['a'] / d['a'] - 1), abs(m['b'] / d['b'] - 1), abs(m['ea'] / d['ea'] - 1))
same('check: exact vs ID alpha, beta, |eta| better than 1e-5 (same constants)', rel < 1e-5, f'({rel:.1e})')
S0 = 0.25 * np.cos(np.radians(d['tau'])) / (2 * d['ea'])
chk('(c) <S>(0) [mW/m^2]', 1e3 * S0, '2.97')
chk('(c) heating at 0 [mW/m^3]', 1e3 * 0.5 * 1e-3 * 0.25, '0.125')
chk('(c) 2 alpha <S> [mW/m^3]', 1e3 * 2 * d['a'] * S0, '0.125')
# finite-difference Poynting balance with the EXACT fields at x = 3 m
Sx = lambda x: 0.5 * np.real(0.5 * np.exp(-m['g'] * x) * np.conj(0.5 * np.exp(-m['g'] * x) / m['eta']))
h = 1e-3
dSdx = (Sx(3 + h) - Sx(3 - h)) / (2 * h)
same('(c) -dS/dx = 1/2 sigma |E|^2 at x=3 m (exact fields, FD)', abs(-dSdx / (0.5e-3 * abs(0.5 * np.exp(-m['g'] * 3)) ** 2) - 1) < 1e-6)
same('(c) alpha = sigma |eta|/(2 cos tau) exactly', abs(1e-3 * m['ea'] / (2 * np.cos(np.radians(m['tau']))) / m['a'] - 1) < 1e-12)
chk('(d) fraction heated in 10 m [%]', 100 * (1 - np.exp(-2 * m['a'] * 10)), '34.4')
chk('(d) dB over 10 m', DB * m['a'] * 10, '1.83')
heat, _ = integrate.quad(lambda x: 0.5e-3 * abs(0.5 * np.exp(-m['g'] * x)) ** 2, 0, 10)
chk('(d) heat per m^2 by quad [mW/m^2]', 1e3 * heat, '1.02')
chk('(d) drop in <S_x> [mW/m^2]', 1e3 * (Sx(0) - Sx(10)), '1.02')
ms = exact(4, 81, f)
chk('check: seawater 100 MHz p', ms['p'], '8.9')
chk('check: seawater 100 MHz loss [dB/m]', DB * ms['a'], '326')

# ---------------------------------------------------------------------------------------------
print("23.8  distilled water 2e-4 S/m, eps_r 81, 100 kHz (CODATA constants, as the student)")
f = 1e5; w = 2 * np.pi * f
chk('student p with eps0', 2e-4 / (w * E0), '36')
gs = good(2e-4, f)
chk('student delta [m]', gs['d'], '113')
chk('student lambda [m]', gs['lam'], '707')
chk('student Re eta [ohm]', gs['eta'].real, '44.4')
chk('student |eta| [ohm]', abs(gs['eta']), '62.8')
m = exact(2e-4, 81, f, E0)
mA = exact(2e-4, 81, f, E0A)
chk('true p', m['p'], '0.444')
same('true regime neither', regime(m['p']) == 'neither')
th = np.degrees(np.arctan(m['p']))
chk('theta [deg]', th, '23.9')
chk('theta/2 [deg]', th / 2, '11.97')
chk('(1+p^2)^(1/4)', (1 + m['p'] ** 2) ** 0.25, '1.046')
chk('w sqrt(mu eps) [rad/m]', w * np.sqrt(MU0 * 81 * E0), '0.01886')
chk('sqrt(mu/eps) [ohm]', ETA0 / 9, '41.86')
chk('alpha [Np/m]', m['a'], '4.09e-3')
chk('delta [m]', m['d'], '244')
chk('beta [rad/m]', m['b'], '0.0193')
chk('lambda [m]', m['lam'], '326')
chk('|eta| [ohm]', m['ea'], '40.0')
chk('tau [deg]', m['tau'], '12.0')
for k in ('d', 'lam', 'ea', 'tau'):   # course constants must not change the 3-figure answers
    pass
chk('delta with 1e-9/36pi [m]', mA['d'], '244')
chk('lambda with 1e-9/36pi [m]', mA['lam'], '326')
chk('|eta| with 1e-9/36pi [ohm]', mA['ea'], '40.0')
chk('delta factor', m['d'] / gs['d'], '2.17')
chk('lambda factor', gs['lam'] / m['lam'], '2.17')
chk('|eta| factor', abs(gs['eta']) / m['ea'], '1.57')
chk('check alpha/beta', m['a'] / m['b'], '0.212')
chk('check |gamma||eta|', abs(m['g']) * m['ea'], '0.790')
chk('check w mu0', w * MU0, '0.790')
di = diel(2e-4, 81, f, E0)
chk('ID delta [m]', di['d'], '239')
chk('ID delta short [%]', 100 * (1 - di['d'] / m['d']), '2.3')
chk('ID lambda [m]', di['lam'], '333')
chk('ID lambda long [%]', 100 * (di['lam'] / m['lam'] - 1), '2.3')
chk('ID |eta| [ohm]', di['ea'], '41.9')
chk('ID |eta| high [%]', 100 * (di['ea'] / m['ea'] - 1), '4.6')
chk('ID tau = p/2 [deg]', di['tau'], '12.7')

# ---------------------------------------------------------------------------------------------
print("23.9  fresh water 2.5 kHz, z down, H(0) = x 20 mA/m")
f = 2.5e3; w = 2 * np.pi * f
m = exact(1e-3, 80, f)
g = good(1e-3, f)
chk('(a) p', m['p'], '90')
chk('(a) p with eps0', 18e9 * 1e-3 / f, '7200')
chk('(b) alpha/pi [1e-3/m]', g['a'] / np.pi * 1e3, '1')
chk('(b) delta [m]', g['d'], '318')
chk('(b) lambda [m]', g['lam'], '2000')
chk('(b) v_p [m/s]', g['vp'], '5e6')
chk('(b) c/v_p', CA / g['vp'], '60')
chk('(b) c/sqrt80 [m/s]', CA / np.sqrt(80), '3.35e7')
chk('(b) ratio', CA / np.sqrt(80) / g['vp'], '6.7')
chk('(c) Re eta / pi', g['eta'].real / np.pi, '1')
chk('(c) |eta| [ohm]', g['ea'], '4.44')
Edir = np.cross(X, Z)
same('(c) E = eta H x z along -y', np.allclose(Edir, -Y))
chk('(c) |E0| [mV/m]', 1e3 * g['ea'] * 0.02, '88.9')
same('(c) E x H along +z', np.allclose(np.cross(-Y, X), Z))
chk('(c) T/8 [us]', 1e6 / f / 8, '50')
# brute force: integrate dEy/dz = j w mu Hx, dHx/dz = (sigma + j w eps) Ey from the surface
def run(sig, eps, eta, zmax):
    rhs = lambda z, y: [1j * w * MU0 * y[1], (sig + 1j * w * eps) * y[0]]
    return integrate.solve_ivp(rhs, (0, zmax), [complex(-eta * 0.02), 0.02 + 0j], method='DOP853',
                               rtol=1e-11, atol=1e-16, dense_output=True)
sol = run(1e-3, 0.0, g['eta'], 1000)            # good-conductor model (no displacement current)
zz = np.linspace(0, 1000, 2001)
Ey, Hx = sol.sol(zz)
alpha_fit = -np.polyfit(zz, np.log(abs(Hx)), 1)[0]
beta_fit = -np.polyfit(zz, np.unwrap(np.angle(Hx)), 1)[0]
chk('(b) ODE (sigma only): delta [m]', 1 / alpha_fit, '318')
chk('(b) ODE (sigma only): lambda [m]', 2 * np.pi / beta_fit, '2000')
Sz = lambda E_, H_: -0.5 * np.real(E_ * np.conj(H_))       # (y x x) = -z
chk('(d) ODE <S_z>(0) [mW/m^2]', 1e3 * Sz(Ey[0], Hx[0]), '0.628')
E5, H5 = sol.sol(500)
chk('(d) ODE <S_z>(500 m) [uW/m^2]', 1e6 * Sz(E5, H5), '27.2')
chk('(d) exp(-pi)', np.exp(-np.pi), '0.0432')
chk('(d) dB/m', DB * g['a'], '0.0273')
chk('(d) dB over 500 m', DB * g['a'] * 500, '13.6')
chk('(d) 1 % depth [m]', np.log(100) / (2 * g['a']), '733')
# (e): E(z) opposite to E(0) at every instant -> phase difference pi
E1, H1 = sol.sol(1000)
same('(e) at 1000 m the phase of E differs from the surface by pi', abs(np.angle(E1 / Ey[0]) - np.pi) < 1e-6 or abs(np.angle(E1 / Ey[0]) + np.pi) < 1e-6)
chk('(e) field left [%]', 100 * abs(E1 / Ey[0]), '4.3')
chk('(e) power left [%]', 100 * Sz(E1, H1) / Sz(Ey[0], Hx[0]), '0.19')
chk('(e) dB', 10 * np.log10(Sz(Ey[0], Hx[0]) / Sz(E1, H1)), '27.3')
chk('watch-out: field at 500 m [%]', 100 * np.exp(-g['a'] * 500), '21')
# exact medium (with displacement current), brute force by ODE launched with the exact eta
sol2 = run(1e-3, 80 * E0A, m['eta'], 1000)
Ey2, Hx2 = sol2.sol(zz)
a2 = -np.polyfit(zz, np.log(abs(Hx2)), 1)[0]; b2 = -np.polyfit(zz, np.unwrap(np.angle(Hx2)), 1)[0]
chk('check exact delta (ODE) [m]', 1 / a2, '320')
chk('check exact lambda (ODE) [m]', 2 * np.pi / b2, '1989')
chk('check exact tau [deg]', m['tau'], '44.7')
chk('check exact 1 % depth [m]', np.log(100) / (2 * m['a']), '737')
print(f"  info  exact vs shortcut: delta {100*(m['d']/g['d']-1):+.2f} %, lambda {100*(m['lam']/g['lam']-1):+.2f} %, tau {100*(m['tau']/45-1):+.2f} %")
# Maxwell residuals of the shortcut fields
gam_s, eta_s = (1 + 1j) / g['d'], g['eta']
far = abs(gam_s * eta_s - 1j * w * MU0) / (w * MU0)
amp = abs(gam_s / eta_s - (1e-3 + 1j * w * 80 * E0A)) / abs(1e-3 + 1j * w * 80 * E0A)
same('check: shortcut fields satisfy Faraday exactly', far < 1e-12, f'(residual {far:.1e})')
chk('check: shortcut fields Ampere-Maxwell residual [%] (page: only to 1.1 %)', 100 * amp, '1.1')
chk('check: w eps/|sigma + j w eps| ~ 1/90', 1 / abs(1e-3 / (w * 80 * E0A) + 1j), f'{1/90:.4f}', tol=2e-5)
same('check: exact delta and lambda within 0.6 % of shortcuts', abs(m['d'] / g['d'] - 1) < 0.006 and abs(m['lam'] / g['lam'] - 1) < 0.006)
same('check: tau differs from 45 deg by more than 0.6 % (page now says 44.7 instead of 45)', abs(m['tau'] / 45 - 1) > 0.006)

# ---------------------------------------------------------------------------------------------
print("23.10  seawater, submarine, 80 dB budget")
for f, ps, als, ds, ls, dbs, deps in [(25e3, '3.6e4', '0.628', '1.59', '10', '5.46', '14.7'),
                                      (250, '3.6e6', '0.0628', '15.9', '100', '0.546', '147')]:
    m, g = exact(4, 81, f), good(4, f)
    chk(f'{f:g} Hz p', m['p'], ps)
    chk(f'{f:g} Hz alpha', g['a'], als)
    chk(f'{f:g} Hz delta', g['d'], ds)
    chk(f'{f:g} Hz lambda', g['lam'], ls)
    chk(f'{f:g} Hz dB/m', DB * g['a'], dbs)
    chk(f'{f:g} Hz depth for 80 dB (exact alpha)', 80 / (DB * m['a']), deps)
    chk(f'{f:g} Hz depth in wavelengths', 80 / (DB * g['a']) / g['lam'], '1.47')
    err = max(abs(m['a'] / g['a'] - 1), abs(m['b'] / g['b'] - 1))
    print(f"  info  {f:g} Hz: exact vs GC alpha/beta differ by {100*err:.5f} %")
    same(f'check {f:g} Hz: exact vs GC alpha, delta, lambda within 0.002 % (page)', 100 * err < 0.002)
chk('(a) alpha/(0.2 pi)', good(4, 25e3)['a'] / (0.2 * np.pi), '1')
chk('(b) via ln(1e8)/(2 alpha)', np.log(1e8) / (2 * good(4, 25e3)['a']), '14.7')
chk('(c) frequency for 10x depth [Hz]', 25e3 / 100, '250')
chk('(c) dB per wavelength', 20 * np.log10(np.exp(2 * np.pi)), '54.6')
chk('(d) lambda0 at 25 kHz [km]', CA / 25e3 / 1e3, '12')
chk('(d) lambda0 at 250 Hz [km]', CA / 250 / 1e3, '1200')
chk('(d) quarter wave [km]', CA / 25e3 / 4e3, '3')
chk('(d) quarter wave [km]', CA / 250 / 4e3, '300')
amax = 80 / (DB * 2)
chk('(e) alpha max [Np/m]', amax, '4.61')
fmax = amax ** 2 / (np.pi * MU0 * 4)
chk('(e) f max [MHz]', fmax / 1e6, '1.34')
m = exact(4, 81, fmax)
chk('(e) p there', m['p'], '660', tol=5)
chk('(e) exact loss over 2 m [dB]', DB * m['a'] * 2, '79.94')
chk('(e) accuracy [%]', 100 * (1 - m['a'] / amax), '0.1', tol=0.05)
for f, s in [(76, '266'), (24e3, '15.0')]:
    chk(f'check depth at {f:g} Hz [m]', 80 / (DB * exact(4, 81, f)['a']), s)

# ---------------------------------------------------------------------------------------------
print("23.11  dry earth 1e-5 S/m, eps_r 5")
fc = 1e-5 / (2 * np.pi * 5 * E0A)
chk('(a) f_c [kHz]', fc / 1e3, '36')
chk('(a) sigma/eps [1/s]', 1e-5 / (5 * E0A), '2.26e5')
chk('(a) GC for w < [rad/s]', 1e-5 / (5 * E0A) / 10, '2.26e4')
chk('(a) ID for w > [rad/s]', 10 * 1e-5 / (5 * E0A), '2.26e6')
m = exact(1e-5, 5, 1e3)
chk('(b)(i) p at 1 kHz', m['p'], '36')
chk('(b)(i) exact alpha/beta at 1 kHz', m['a'] / m['b'], '0.973')
m = exact(1e-5, 5, 50)
chk('(b)(ii) p at 50 Hz', m['p'], '720')
chk('(b)(ii) field after one wavelength [%]', 100 * np.exp(-m['a'] * m['lam']), '0.19')
chk('(b)(ii) wavelength [km]', m['lam'] / 1e3, '141')
m = exact(1e-5, 5, 1e7)
chk('(b)(iii) power left after 1 km [%]', 100 * np.exp(-2 * m['a'] * 1e3), '18.5')
same('(b)(iii) possible (>10 %)', np.exp(-2 * m['a'] * 1e3) > 0.1)
g = good(1e-5, 100)
chk('(c) p at 100 Hz', exact(1e-5, 5, 100)['p'], '360')
chk('(c) alpha/(2 pi 1e-5)', g['a'] / (2 * np.pi * 1e-5), '1')
chk('(c) delta [km]', g['d'] / 1e3, '15.9')
chk('(c) lambda [km]', g['lam'] / 1e3, '100')
d = diel(1e-5, 5, 1e7, eta0=ETA0A)
chk('(d) p at 10 MHz', m['p'], '3.6e-3')
chk('(d) |eta| [ohm]', d['ea'], '168.6')
chk('(d) alpha [Np/m]', d['a'], '8.43e-4')
chk('(d) exact alpha [Np/m]', m['a'], '8.43e-4')
chk('(d) delta [m]', d['d'], '1186')
chk('(d) lambda [m]', d['lam'], '13.4')
chk('(d) dB/km', DB * d['a'] * 1e3, '7.32')
m100 = exact(1e-5, 5, 1e8)
chk('(d) 100 MHz exact lambda [m]', m100['lam'], '1.34')
chk('(d) 100 MHz exact alpha unchanged [Np/m]', m100['a'], '8.43e-4')
chk('(d) 100 MHz exact |eta| unchanged [ohm]', m100['ea'], '168.6')
m = exact(1e-5, 5, fc)
chk('(e) p at f_c', m['p'], '1')
chk('(e) w sqrt(mu eps)', 2 * np.pi * fc * np.sqrt(MU0 * 5 * E0A), '1.686e-3')
chk('(e) alpha', m['a'], '7.67e-4')
chk('(e) beta', m['b'], '1.852e-3')
chk('(e) |eta|', m['ea'], '141.8')
chk('(e) tau [deg]', m['tau'], '22.5')
chk('(e) delta [m]', m['d'], '1303')
chk('(e) lambda [m]', m['lam'], '3392')
gfc, dfc = good(1e-5, fc), diel(1e-5, 5, fc, eta0=ETA0A)
chk('(e) ID alpha too high [%]', 100 * (dfc['a'] / m['a'] - 1), '9.9')
chk('(e) GC alpha', gfc['a'], '1.192e-3')
chk('(e) GC alpha too high [%]', 100 * (gfc['a'] / m['a'] - 1), '55')
chk('(e) ID beta too low [%]', 100 * (1 - dfc['b'] / m['b']), '9.0')
chk('(e) GC beta too low [%]', 100 * (1 - gfc['b'] / m['b']), '36')
fs = np.logspace(1, 9, 2000)
ds_ = np.array([exact(1e-5, 5, ff)['d'] for ff in fs])
same('check: delta(f) monotonically decreasing 10 Hz..1 GHz', np.all(np.diff(ds_) < 0))
chk('check: plateau delta at 1 GHz [m]', exact(1e-5, 5, 1e9)['d'], '1186')
m = exact(1e-5, 5, 100)
chk('check: exact delta 100 Hz [km]', m['d'] / 1e3, '15.94')
chk('check: exact lambda 100 Hz [km]', m['lam'] / 1e3, '99.9')
chk('check: difference [%]', 100 * (m['d'] / g['d'] - 1), '0.14')

# ---------------------------------------------------------------------------------------------
print("23.12  copper wire a = 0.5 mm, I0 = 2 A, 10 MHz")
s, a, I0, f = 5.8e7, 0.5e-3, 2.0, 1e7
w = 2 * np.pi * f
g = good(s, f)
chk('setup sigma/(w eps0)', exact(s, 1, f, E0)['p'], '1.0e11')
chk('(a) 0.0661/sqrt(f) constant', 1 / np.sqrt(np.pi * MU0 * s), '0.0661')
chk('(a) delta [um]', g['d'] * 1e6, '20.9')
chk('(a) a/delta', a / g['d'], '23.9')
H0 = I0 / (2 * np.pi * a)
chk('(b) H0 [A/m]', H0, '637')
chk('(b) sigma delta [S]', s * g['d'], '1212')
chk('(b) Re eta [mohm]', 1e3 * g['eta'].real, '0.825')
chk('(b) |eta| [mohm]', 1e3 * g['ea'], '1.17')
# directions at the point phi = 0: r = x, phi = y, z = z
r_, ph_ = X, Y
same('(b) phi x (-r) = +z', np.allclose(np.cross(ph_, -r_), Z))
same('(b) E x H ~ z x phi = -r (into the wire)', np.allclose(np.cross(Z, ph_), -r_))
chk('(b) |E(a)| [V/m]', g['ea'] * H0, '0.743')
chk('(b) phase of E relative to I [deg]', np.degrees(np.angle(g['eta'])), '45')
Sin = 0.5 * g['eta'].real * H0 ** 2
chk('(c) <S> in [W/m^2]', Sin, '167')
P1 = Sin * 2 * np.pi * a
chk("(c) P' [W/m]", P1, '0.525')
Rac = 2 * P1 / I0 ** 2
chk("(c) R'ac [ohm/m]", Rac, '0.263')
chk("(c) R'ac = 1/(2 pi a sigma delta)", 1 / (2 * np.pi * a * s * g['d']), '0.263')
Rdc = 1 / (s * np.pi * a ** 2)
chk("(c) R'dc [mohm/m]", 1e3 * Rdc, '22.0')
chk("(c) R'ac/R'dc", Rac / Rdc, '12.0')
chk("(c) a/(2 delta)", a / (2 * g['d']), '12.0')
heat, _ = integrate.quad(lambda x: 0.5 * s * (g['ea'] * H0 * np.exp(-x / g['d'])) ** 2, 0, 50 * g['d'])
chk('(d) heat integral [W/m^2]', heat, '167')
chk('(d) 1/2 sigma |E|^2 at surface [W/m^3]', 0.5 * s * (g['ea'] * H0) ** 2, '1.60e7')
chk('(d) delta/2 [um]', 1e6 * g['d'] / 2, '10.4')
h1, _ = integrate.quad(lambda x: np.exp(-2 * x / g['d']), 0, g['d'])
chk('(d) fraction within delta [%]', 100 * h1 / (g['d'] / 2), '86.5')
g60 = good(s, 60)
chk('(e) delta 60 Hz [mm]', 1e3 * g60['d'], '8.53')
chk('(e) delta/a', g60['d'] / a, '17', tol=0.1)
chk('(e) flat-model ratio a/2delta', a / (2 * g60['d']), '0.029')
# exact round wire: Z' = k J0(ka) / (2 pi a sigma J1(ka)), k = (1 - j)/delta  (e^{jwt}, no displacement current)
def zwire(f):
    d_ = good(s, f)['d']
    k = (1 - 1j) / d_
    return k * special.jv(0, k * a) / (2 * np.pi * a * s * special.jv(1, k * a))
# independent check of the Bessel formula: integrate E'' + E'/r + k^2 E = 0 numerically
def zwire_ode(f):
    d_ = good(s, f)['d']; k2 = -1j * 2 * np.pi * f * MU0 * s
    r0 = 1e-9 * a
    sol = integrate.solve_ivp(lambda r, y: [y[1], -y[1] / r - k2 * y[0]], (r0, a), [1 + 0j, -k2 * r0 / 2 + 0j],
                              method='DOP853', rtol=1e-11, atol=1e-14)
    Ez, dEz = sol.y[0, -1], sol.y[1, -1]
    Hphi = dEz / (1j * 2 * np.pi * f * MU0)
    return Ez / (2 * np.pi * a * Hphi)
Zb, Zo = zwire(1e7), zwire_ode(1e7)
same('check: Bessel formula equals ODE integration at 10 MHz', abs(Zb / Zo - 1) < 1e-6, f'({abs(Zb/Zo-1):.1e})')
chk("check: exact R' at 10 MHz [ohm/m]", Zb.real, '0.268')
chk('check: above flat value [%]', 100 * (Zb.real / Rac - 1), '2.1')
chk('check: a/2delta + 1/4 times Rdc', (a / (2 * g['d']) + 0.25) * Rdc, '0.268')
z60 = zwire(60)
same("check: 60 Hz exact R' = R'dc to < 1e-6", abs(z60.real / Rdc - 1) < 1e-6, f'({z60.real/Rdc-1:.1e})')
chk('check: flat-model L\' = R\'ac/w [nH/m]', 1e9 * Rac / w, '4.2')
chk("check: exact L' at 10 MHz [nH/m]", 1e9 * Zb.imag / w, '4.2', tol=0.1)
chk('check: DC internal inductance mu0/8pi [nH/m]', 1e9 * MU0 / (8 * np.pi), '50')
chk("check: exact L' at 60 Hz [nH/m]", 1e9 * z60.imag / (2 * np.pi * 60), '50', tol=0.01)

print(f"\nTOTAL FAIL = {NFAIL}")
