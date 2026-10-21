#!/usr/bin/env python3
"""Independent review checks for Lecture 26 (standing waves, radiation pressure).
numpy/scipy only. Prints PASS/FAIL per item; output saved to review_L26.out."""
import numpy as np
from scipy.integrate import quad

NP = NF = 0
def chk(name, ok, extra=""):
    global NP, NF
    if ok: NP += 1
    else: NF += 1
    print(("PASS " if ok else "FAIL ") + name + (("  " + extra) if extra else ""))

def close(a, b, rtol=1e-9, atol=1e-12):
    return np.allclose(a, b, rtol=rtol, atol=atol)

# handbook constants (CODATA 2018)
c = 299792458.0
mu0 = 1.25663706212e-6
eps0 = 8.8541878128e-12
eta0 = np.sqrt(mu0 / eps0)
hbar = 1.054571817e-34
X, Y, Z = np.eye(3)

print("== A. standing wave in front of a PEC (region 1: eps_r=2.25, mu_r=1)")
f = 1.5e9; w = 2 * np.pi * f
eps1 = 2.25 * eps0; mu1 = mu0
eta1 = np.sqrt(mu1 / eps1); b1 = w * np.sqrt(mu1 * eps1); lam = 2 * np.pi / b1
E0 = 3.7
z = np.linspace(-1.3 * lam, 0, 2001)
Ei = np.outer(E0 * np.exp(-1j * b1 * z), X); Er = np.outer(-E0 * np.exp(1j * b1 * z), X)
ui, ur = Z, -Z
Hi = np.cross(ui, Ei) / eta1; Hr = np.cross(ur, Er) / eta1
chk("A1 H_i = +y E0/eta1 e^{-jbz} (np.cross)", close(Hi, np.outer(E0 / eta1 * np.exp(-1j * b1 * z), Y)))
chk("A2 H_r = +y E0/eta1 e^{+jbz} (keeps incident sign)", close(Hr, np.outer(E0 / eta1 * np.exp(1j * b1 * z), Y)))
Et = Ei + Er; Ht = Hi + Hr
chk("A3 E~ = -j x 2E0 sin(bz)", close(Et, np.outer(-2j * E0 * np.sin(b1 * z), X)))
chk("A4 H~ = y (2E0/eta1) cos(bz)", close(Ht, np.outer(2 * E0 / eta1 * np.cos(b1 * z), Y)))
def Ex(zz, t): return 2 * E0 * np.sin(b1 * zz) * np.sin(w * t)
def Hy(zz, t): return 2 * E0 / eta1 * np.cos(b1 * zz) * np.cos(w * t)
tt = np.linspace(0, 1 / f, 37)
re_ok = all(close(np.real(Et[:, 0] * np.exp(1j * w * t)), Ex(z, t)) and close(np.real(Ht[:, 1] * np.exp(1j * w * t)), Hy(z, t)) for t in tt)
chk("A5 real forms = Re{phasor e^{jwt}}", re_ok)
# two travelling waves identity
chk("A6 2 sin bz sin wt = cos(wt-bz) - cos(wt+bz)", all(close(np.sin(b1 * z) * np.sin(w * t) * 2, np.cos(w * t - b1 * z) - np.cos(w * t + b1 * z)) for t in tt))
# Maxwell curl equations by central differences (only z-dependence)
hz, ht = lam * 1e-5, 1e-5 / f
zs = np.linspace(-1.2 * lam, -0.01 * lam, 50); ts = np.linspace(0, 1 / f, 23)
ZZ, TT = np.meshgrid(zs, ts)
curlE_y = (Ex(ZZ + hz, TT) - Ex(ZZ - hz, TT)) / (2 * hz)                 # (curl E)_y = dEx/dz
dHy_dt = (Hy(ZZ, TT + ht) - Hy(ZZ, TT - ht)) / (2 * ht)
curlH_x = -(Hy(ZZ + hz, TT) - Hy(ZZ - hz, TT)) / (2 * hz)                # (curl H)_x = -dHy/dz
dEx_dt = (Ex(ZZ, TT + ht) - Ex(ZZ, TT - ht)) / (2 * ht)
sc = 2 * E0 * b1
chk("A7 Faraday curl E = -mu dH/dt (FD)", np.max(np.abs(curlE_y + mu1 * dHy_dt)) < 1e-6 * sc)
chk("A8 Ampere curl H = eps dE/dt (FD)", np.max(np.abs(curlH_x - eps1 * dEx_dt)) < 1e-6 * sc / eta1)
chk("A9 PEC boundary: E_x(0,t) = 0 for all t", np.max(np.abs(Ex(0.0, tt))) < 1e-12)
# nodes and antinodes
m = np.arange(0, 4)
chk("A10 E nodes at -m lam/2", close(np.sin(b1 * (-m * lam / 2)), 0, atol=1e-12))
chk("A11 H nodes at -(2m+1) lam/4", close(np.cos(b1 * (-(2 * m + 1) * lam / 4)), 0, atol=1e-12))
chk("A12 E antinodes |E~|=2E0 at -(2m+1)lam/4", close(np.abs(2 * E0 * np.sin(b1 * (-(2 * m + 1) * lam / 4))), 2 * E0))
chk("A13 |E~| period lam/2", close(np.abs(np.sin(b1 * z)), np.abs(np.sin(b1 * (z - lam / 2))), atol=1e-12))
# mirror at z=d: replacing z by z-d also needs the phase e^{-jbd}
d = 0.37 * lam
Ed = E0 * np.exp(-1j * b1 * z) - E0 * np.exp(-2j * b1 * d) * np.exp(1j * b1 * z)
chk("A14 mirror at d: E~ = -j2E0 e^{-jbd} sin b(z-d) (phase factor needed)", close(Ed, -2j * E0 * np.exp(-1j * b1 * d) * np.sin(b1 * (z - d))))
chk("A15 ... and without e^{-jbd} it is NOT equal (so 'z-d for z' needs E0 at mirror)", not close(Ed, -2j * E0 * np.sin(b1 * (z - d))))

print("== B. power and energy of the standing wave")
Sav = 0.5 * np.real(np.cross(Et, np.conj(Ht)))
chk("B1 <S> = 1/2 Re{E x H*} = 0 (np.cross)", np.max(np.abs(Sav)) < 1e-12 * E0 ** 2 / eta1)
zq = np.linspace(-lam, 0, 41)
Sq = np.array([quad(lambda t: Ex(zz, t) * Hy(zz, t), 0, 1 / f, limit=200)[0] * f for zz in zq])
chk("B2 <S_z> by quadrature = 0", np.max(np.abs(Sq)) < 1e-9 * E0 ** 2 / eta1)
S_inst = lambda zz, t: Ex(zz, t) * Hy(zz, t)
chk("B3 S = z (E0^2/eta1) sin2bz sin2wt", all(close(S_inst(z, t), E0 ** 2 / eta1 * np.sin(2 * b1 * z) * np.sin(2 * w * t)) for t in tt))
wfun = lambda zz, t: 0.5 * eps1 * Ex(zz, t) ** 2 + 0.5 * mu1 * Hy(zz, t) ** 2
chk("B4 w = 2 eps E0^2 [sin^2 sin^2 + cos^2 cos^2]", all(close(wfun(z, t), 2 * eps1 * E0 ** 2 * (np.sin(b1 * z) ** 2 * np.sin(w * t) ** 2 + np.cos(b1 * z) ** 2 * np.cos(w * t) ** 2)) for t in tt))
wq = np.array([quad(lambda t: wfun(zz, t), 0, 1 / f, limit=200)[0] * f for zz in zq])
chk("B5 <w> = eps1 E0^2 at every z (quadrature)", close(wq, eps1 * E0 ** 2, rtol=1e-8))
chk("B6 S = 0 at multiples of lam/4, all t", all(np.max(np.abs(S_inst(-k * lam / 4, tt))) < 1e-9 * E0 ** 2 / eta1 for k in range(5)))
cell = [quad(lambda zz: wfun(zz, t), -lam / 4, 0)[0] for t in tt] + [quad(lambda zz: wfun(zz, t), -lam / 2, -lam / 4)[0] for t in tt]
chk("B7 energy per lam/4 cell constant = eps E0^2 lam/4", close(cell, eps1 * E0 ** 2 * lam / 4, rtol=1e-8))
# Poynting theorem dS/dz + dw/dt = 0 by FD
dSdz = (S_inst(ZZ + hz, TT) - S_inst(ZZ - hz, TT)) / (2 * hz)
dwdt = (wfun(ZZ, TT + ht) - wfun(ZZ, TT - ht)) / (2 * ht)
chk("B8 Poynting theorem dS/dz + dw/dt = 0 (FD)", np.max(np.abs(dSdz + dwdt)) < 1e-6 * np.max(np.abs(dwdt)))
chk("B9 wt=0 all magnetic (w_E=0), wt=pi/2 all electric (w_H=0)", np.max(np.abs(Ex(z, 0))) == 0 and np.max(np.abs(Hy(z, 0.25 / f))) < 1e-9)
# zeros of w
zg = np.linspace(-lam, 0, 4001); tg = np.linspace(0, 1 / f, 4001)
ZG, TG = np.meshgrid(zg, tg)
W = (np.sin(b1 * ZG) ** 2 * np.sin(w * TG) ** 2 + np.cos(b1 * ZG) ** 2 * np.cos(w * TG) ** 2)
idx = np.argwhere(W < 1e-7)
zz0 = zg[idx[:, 1]]; tt0 = tg[idx[:, 0]]
onE = np.abs(np.sin(b1 * zz0)) < 1e-3; onH = np.abs(np.cos(b1 * zz0)) < 1e-3
okz = np.all((onE & (np.abs(np.cos(w * tt0)) < 1e-3)) | (onH & (np.abs(np.sin(w * tt0)) < 1e-3)))
chk("B10 w = 0 only at E node with cos wt = 0 or H node with sin wt = 0", okz and len(idx) > 0)

print("== C. partial reflection (site's addition)")
for G in (-0.5, 0.5, 0.3 * np.exp(1j * 2.1), 0.8 * np.exp(-1j * 0.7)):
    aG, th = abs(G), np.angle(G)
    Ep = E0 * np.exp(-1j * b1 * z) * (1 + G * np.exp(2j * b1 * z))
    dec = (1 - aG) * E0 * np.exp(-1j * b1 * z) + 2 * aG * E0 * np.exp(1j * th / 2) * np.cos(b1 * z + th / 2)
    chk(f"C1 decomposition travelling+standing, Gamma={G:.3f}", close(Ep, dec))
    zf = np.linspace(-2 * lam, 0, 20001)
    mag = np.abs(1 + G * np.exp(2j * b1 * zf))
    chk(f"C2 |E| between (1-|G|)E0 and (1+|G|)E0", abs(mag.max() - (1 + aG)) < 1e-6 and abs(mag.min() - (1 - aG)) < 1e-6)
    chk(f"C3 period lam/2", close(np.abs(1 + G * np.exp(2j * b1 * z)), np.abs(1 + G * np.exp(2j * b1 * (z + lam / 2))), atol=1e-12))
    Hp = E0 / eta1 * np.exp(-1j * b1 * z) * (1 - G * np.exp(2j * b1 * z))
    Exr = lambda zz, t: np.real(E0 * np.exp(-1j * b1 * zz) * (1 + G * np.exp(2j * b1 * zz)) * np.exp(1j * w * t))
    Hyr = lambda zz, t: np.real(E0 / eta1 * np.exp(-1j * b1 * zz) * (1 - G * np.exp(2j * b1 * zz)) * np.exp(1j * w * t))
    Sq2 = [quad(lambda t: Exr(zz, t) * Hyr(zz, t), 0, 1 / f, limit=200)[0] * f for zz in (-0.13 * lam, -0.61 * lam)]
    chk(f"C4 <S> = (1-|G|^2)E0^2/2eta1 (quadrature)", close(Sq2, (1 - aG ** 2) * E0 ** 2 / (2 * eta1), rtol=1e-7))
# concept-page example: vacuum onto eps_r = 9
G9 = (eta0 / 3 - eta0) / (eta0 / 3 + eta0)
mag0 = abs(1 + G9)
chk("C5 eps_r=9: Gamma=-1/2, |E| 0.5..1.5 E0, min at interface", abs(G9 + 0.5) < 1e-12 and abs(mag0 - 0.5) < 1e-12)
print("   negative real Gamma -> min at z=0; positive -> max:", abs(1 - 0.5), abs(1 + 0.5))

print("== D. surface current on the mirror; sheet check")
H0t = Hy(0.0, tt)
Js = np.array([np.cross(-Z, h * Y) for h in H0t])
chk("D1 J_s = n x H with n = -z (2 into 1) = +x (2E0/eta1) cos wt", close(Js, np.outer(2 * E0 / eta1 * np.cos(w * tt), X)))
chk("D2 J_s in phase with incident E at mirror (along +x when E_i(0,0)=+x E0)", close(Js[:, 0] * eta1 / 2, E0 * np.cos(w * tt)))
chk("D3 J_s phasor = x 2E0/eta1 (L25)", close(np.cross(-Z, Ht[-1]), 2 * E0 / eta1 * X))
# sheet in uniform eta1 radiates E = -(eta/2) Js(t - |xi|/v), H = 1/2 Js x n (n toward field point)
v = 1 / np.sqrt(mu1 * eps1)
Jsf = lambda t: 2 * E0 / eta1 * np.cos(w * t)
zp = np.linspace(0.01, 1.3, 40) * lam; zm = -zp
okp = all(close(-eta1 / 2 * Jsf(t - zp / v), -E0 * np.cos(w * t - b1 * zp)) for t in tt)
okm = all(close(-eta1 / 2 * Jsf(t - np.abs(zm) / v), -E0 * np.cos(w * t + b1 * zm)) for t in tt)
chk("D4 sheet field into z>0 = -x E0 cos(wt-bz) (cancels incident)", okp)
chk("D5 sheet field into z<0 = -x E0 cos(wt+bz) = reflected wave", okm)
Hp_dir = 0.5 * np.cross(X, Z); Hm_dir = 0.5 * np.cross(X, -Z)
chk("D6 sheet H: z>0 along -y (cancels H_i), z<0 along +y (= H_r)", close(Hp_dir, -0.5 * Y) and close(Hm_dir, 0.5 * Y))

print("== E. good conductor: copper at 10 GHz (sigma = 5.8e7 S/m handbook, mu=mu0, eps=eps0)")
sig = 5.8e7; f2 = 10e9; w2 = 2 * np.pi * f2
g2 = np.sqrt(1j * w2 * mu0 * (sig + 1j * w2 * eps0)); n2 = np.sqrt(1j * w2 * mu0 / (sig + 1j * w2 * eps0))
a2 = g2.real
dlt = 1 / np.sqrt(np.pi * f2 * mu0 * sig)
Rs = 1 / (sig * dlt)
G2 = (n2 - eta0) / (n2 + eta0); tau = 1 + G2
print(f"   delta = {dlt*1e6:.4f} um, Rs = {Rs*1e3:.3f} mOhm, Re eta2 = {n2.real*1e3:.3f} mOhm, 4Rs/eta0 = {4*Rs/eta0:.4e}, 1-|G|^2 = {1-abs(G2)**2:.4e}")
chk("E1 delta = 0.661 um", abs(dlt * 1e6 - 0.661) < 0.0005)
chk("E2 Rs = 26.1 mOhm", abs(Rs * 1e3 - 26.1) < 0.05)
chk("E3 Rs = sqrt(pi f mu/sigma) = alpha/sigma (approx) = Re eta2", abs(Rs - np.sqrt(np.pi * f2 * mu0 / sig)) < 1e-15 and abs(a2 / sig / Rs - 1) < 1e-6 and abs(n2.real / Rs - 1) < 1e-6)
chk("E4 gamma2 = (1+j)/delta (good-conductor approx, rel 1e-6)", abs(g2 / ((1 + 1j) / dlt) - 1) < 1e-6)
chk("E5 4Rs/eta0 = 2.77e-4", abs(4 * Rs / eta0 - 2.77e-4) < 0.005e-4)
chk("E6 1-|Gamma|^2 (exact) = 2.77e-4, reflects 99.97 %", abs((1 - abs(G2) ** 2) - 2.77e-4) < 0.005e-4 and abs(abs(G2) ** 2 * 100 - 99.97) < 0.005)
chk("E7 dissipation 1/2 Rs (2E0/eta0)^2 = (4Rs/eta0)<S_i>", close(0.5 * Rs * (2 * E0 / eta0) ** 2, 4 * Rs / eta0 * E0 ** 2 / (2 * eta0)))
chk("E8 sigma*eta2 ~ gamma2 (good conductor)", abs(sig * n2 / g2 - 1) < 1e-6)
# depth integral of J_t (exact fields, numerical quadrature)
Jt = lambda zz: sig * tau * E0 * np.exp(-g2 * zz)
zgrid = np.linspace(0, 40 * dlt, 400001)
Jint = np.trapezoid(Jt(zgrid), zgrid)
chk("E9 int J_t dz = 2E0/eta0 (rel 3e-4)", abs(Jint / (2 * E0 / eta0) - 1) < 3e-4, f"ratio-1 = {abs(Jint/(2*E0/eta0)-1):.2e}")
# surface resistance: J(z) = Js gamma e^{-gamma z}
Js0 = 2 * E0 / eta0
Jz = Js0 * g2 * np.exp(-g2 * zgrid); Ez = Jz / sig
pd = 0.5 * np.real(Jz * np.conj(Ez))
chk("E10 int Js gamma e^{-gamma z} dz = Js", abs(np.trapezoid(Jz, zgrid) / Js0 - 1) < 1e-6)
chk("E11 <J.E> = 1/2 |Js gamma|^2 e^{-2az}/sigma", close(pd, 0.5 * abs(Js0 * g2) ** 2 * np.exp(-2 * a2 * zgrid) / sig))
chk("E12 int <J.E> dz = 1/2 Rs |Js|^2 (Rs = alpha/sigma)", abs(np.trapezoid(pd, zgrid) / (0.5 * a2 / sig * Js0 ** 2) - 1) < 1e-6)
# five conductors: depth integral and 1-|G|^2 vs 4Rs/eta0
for name, s_, ff in (("Al 1 MHz", 3.5e7, 1e6), ("Fe-free brass 100 MHz", 1.5e7, 1e8), ("seawater 1 kHz", 4.0, 1e3), ("graphite 1 GHz", 7e4, 1e9)):
    ww = 2 * np.pi * ff
    gg = np.sqrt(1j * ww * mu0 * (s_ + 1j * ww * eps0)); nn = np.sqrt(1j * ww * mu0 / (s_ + 1j * ww * eps0))
    tt_ = 2 * nn / (nn + eta0)
    Jn = s_ * tt_ / gg
    chk(f"E13 depth integral ~ 2/eta0, {name}", abs(Jn * eta0 / 2 - 1) < 3 * abs(nn) / eta0 + 1e-6, f"rel err {abs(Jn*eta0/2-1):.1e}")

print("== F. radiation pressure")
B2 = lambda zz: mu0 * tau * E0 / n2 * np.exp(-g2 * zz)
fz = 0.5 * np.real(np.cross(np.outer(Jt(zgrid), X), np.conj(np.outer(B2(zgrid), Y))))
chk("F1 J x B* along +z only (x cross y = z)", np.max(np.abs(fz[:, :2])) == 0 and np.all(fz[:, 2] >= 0))
P_av = np.trapezoid(fz[:, 2], zgrid)
Si = E0 ** 2 / (2 * eta0)
print(f"   <P_rad>/(2<S_i>/c) - 1 = {P_av/(2*Si/c)-1:.3e};  vs (1+|G|^2)<S_i>/c: {P_av/((1+abs(G2)**2)*Si/c)-1:.2e}")
chk("F2 <P_rad> = 2<S_i>/c within 2e-4 (copper, exact fields)", abs(P_av / (2 * Si / c) - 1) < 2e-4)
chk("F3 <P_rad> = (1+|G|^2)<S_i>/c (copper, exact)", abs(P_av / ((1 + abs(G2) ** 2) * Si / c) - 1) < 1e-6)
# (1+|G|^2) law for other sigma (eps2 = eps0, mu2 = mu0), semi-infinite: J x B on conduction current
for s_ in (1e-2, 1.0, 1e2, 1e5):
    gg = np.sqrt(1j * w2 * mu0 * (s_ + 1j * w2 * eps0)); nn = np.sqrt(1j * w2 * mu0 / (s_ + 1j * w2 * eps0))
    GG = (nn - eta0) / (nn + eta0); TT_ = 1 + GG
    # analytic depth integral of 1/2 Re{sigma tau E0 e^{-gz} (mu0 tau E0/nn e^{-gz})^*} = 1/2 Re{sigma mu0 |tau E0|^2 / nn^*} / (2 alpha)
    Pa = 0.5 * np.real(s_ * mu0 * abs(TT_ * E0) ** 2 / np.conj(nn)) / (2 * gg.real)
    chk(f"F4 (1+|G|^2)<S_i>/c for sigma = {s_:g} S/m at 10 GHz", abs(Pa / ((1 + abs(GG) ** 2) * Si / c) - 1) < 1e-9, f"|G|^2 = {abs(GG)**2:.4f}")
# instantaneous push, exact copper fields: int J x B dz = 1/2 mu0 H_y(0,t)^2 (to eps0 w/sigma)
okt = True; worst = 0
for t in np.linspace(0, 1 / f2, 17):
    Jr = np.real(Jt(zgrid) * np.exp(1j * w2 * t)); Br = np.real(B2(zgrid) * np.exp(1j * w2 * t))
    Pt = np.trapezoid(Jr * Br, zgrid)
    H0 = np.real(tau * E0 / n2 * np.exp(1j * w2 * t))
    ref = 0.5 * mu0 * H0 ** 2
    worst = max(worst, abs(Pt - ref) / (4 * Si / c))
chk("F5 P_rad(t) = 1/2 mu0 H_y(0,t)^2 (exact copper fields)", worst < 1e-5, f"max dev / (4<S_i>/c) = {worst:.1e}")
Hpec = lambda t: 2 * E0 / eta0 * np.cos(w2 * t)
chk("F6 1/2 mu0 (2E0/eta0)^2 cos^2 wt = (4<S_i>/c) cos^2 wt", close(0.5 * mu0 * Hpec(tt) ** 2, 4 * Si / c * np.cos(w2 * tt) ** 2))
chk("F7 sheet in mean field: Js x (B/2) = 1/2 mu0 H^2 along +z", close(np.cross(Hpec(0.1 / f2) * X, 0.5 * mu0 * Hpec(0.1 / f2) * Y), 0.5 * mu0 * Hpec(0.1 / f2) ** 2 * Z))
chk("F8 <P_rad> = eps0 E0^2 = <w> of standing wave", close(2 * Si / c, eps0 * E0 ** 2, rtol=1e-9))
chk("F9 mu0/eta0 = 1/c", close(mu0 / eta0, 1 / c))
# absorber
# absorber: |G| = 0 limit of (1+|G|^2) -> 1 ; mirror |G| = 1 -> 2
chk("F10 absorber <S_i>/c, mirror 2<S_i>/c as limits of (1+|G|^2)", (1 + 0 ** 2) == 1 and (1 + 1 ** 2) == 2)
# photons: density <S>/(w c hbar); momentum density <S>/c^2; spin density <S>/(w c)
Sx = 1361.0; wl = 2 * np.pi * 5.6e14
nph = Sx / (wl * c * hbar)
chk("F11 momentum per photon = hbar w / c", close((Sx / c ** 2) / nph, hbar * wl / c))
chk("F12 spin per photon = hbar", close((Sx / (wl * c)) / nph, hbar))
chk("F13 photon density = energy density / (hbar w)", close(nph, (Sx / c) / (hbar * wl)))

print("== G. numbers: sunlight (solar constant 1361 W/m^2, Kopp & Lean 2011), sail, laser")
E0s = np.sqrt(2 * eta0 * Sx)
print(f"   E0 = {E0s:.1f} V/m, 2S/c = {2*Sx/c*1e6:.3f} uPa, S/c = {Sx/c*1e6:.3f} uPa, sail = {2*Sx/c*1e4:.4f} N, Js = {2*E0s/eta0:.3f} A/m, laser = {2/c*1e9:.3f} nN")
chk("G1 E0 = 1.01 kV/m", abs(E0s - 1010) < 5)
chk("G2 mirror 9.08 uPa", abs(2 * Sx / c * 1e6 - 9.08) < 0.005)
chk("G3 absorber 4.54 uPa", abs(Sx / c * 1e6 - 4.54) < 0.005)
chk("G4 100 m x 100 m sail 0.091 N", abs(2 * Sx / c * 1e4 - 0.091) < 0.0005)
chk("G5 mirror current peak 2E0/eta0 = 5.4 A/m", abs(2 * E0s / eta0 - 5.4) < 0.05)
chk("G6 1 W laser reflected: 6.7 nN", abs(2 / c * 1e9 - 6.67) < 0.01)
chk("G7 copper: |G|^2 = 0.99972, 1+|G|^2 = 1.99972, within 0.014 % of 2", abs(abs(G2) ** 2 - 0.99972) < 5e-6 and abs((2 - (1 + abs(G2) ** 2)) / 2 * 100 - 0.014) < 0.0005)

print("== H. worked problem: circular wave on a mirror (y<0 PEC), f = 1.5 GHz, eta0 = 120 pi, c = 3e8")
cc = 3e8; et = 120 * np.pi; mu = et / cc; ep = 1 / (et * cc)
fw = 1.5e9; ww = 2 * np.pi * fw; bb = ww / cc; lw = 2 * np.pi / bb
chk("H1 beta = 10 pi rad/m, lambda = 20 cm", abs(bb - 10 * np.pi) < 1e-12 and abs(lw - 0.2) < 1e-15)
A = 60 * np.pi
Ei_t = lambda yy, t: A * (np.outer(np.cos(ww * t + bb * yy), X) + np.outer(np.sin(ww * t + bb * yy), Z))
Eip = lambda yy: A * np.outer(np.exp(1j * bb * yy), X - 1j * Z)
ys = np.linspace(0, 0.3, 61)
chk("H2 phasor E~_i = 60pi (x - j z) e^{j beta y}", all(close(np.real(Eip(ys) * np.exp(1j * ww * t)), Ei_t(ys, t)) for t in np.linspace(0, 1 / fw, 13)))
# travel direction from the phase: constant phase w t + b y => y decreases as t grows
tq = 1e-10; ypk = -ww * tq / bb   # crest of cos(wt+by) moves to y = -w t / b
chk("H3 incident travels along -y (crest tracking)", abs(np.cos(ww * tq + bb * ypk) - 1) < 1e-12 and ypk < 0)
def hand(Efun, u):
    tl = np.linspace(0, 1 / fw, 400, endpoint=False)
    Ev = np.array([Efun(t) for t in tl])
    dE = np.gradient(Ev, tl, axis=0)
    om = np.cross(Ev, dE)                      # rotation vector (right-hand rule)
    s = np.dot(om, u)
    return "right" if np.all(s > 0) else ("left" if np.all(s < 0) else "mixed")
hi = hand(lambda t: Ei_t(np.array([0.0]), t)[0], -Y)
chk("H4 incident hand by numeric rotation (thumb along -y): right-circular", hi == "right", hi)
Erp = lambda yy: -A * np.outer(np.exp(-1j * bb * yy), X - 1j * Z)
chk("H5 E~_r(0) = -E~_i(0) (Gamma=-1 per component)", close(Erp(np.array([0.0])), -Eip(np.array([0.0]))))
hr = hand(lambda t: np.real(Erp(np.array([0.0]))[0] * np.exp(1j * ww * t)), Y)
chk("H6 reflected hand (thumb along +y): left-circular", hr == "left", hr)
# also check at y != 0 (hand independent of position)
hr2 = hand(lambda t: np.real(Erp(np.array([0.037]))[0] * np.exp(1j * ww * t)), Y)
hi2 = hand(lambda t: np.real(Eip(np.array([0.037]))[0] * np.exp(1j * ww * t)), -Y)
chk("H7 hands same at y = 3.7 cm", hr2 == "left" and hi2 == "right")
Hip = np.cross(-Y, Eip(ys)) / et; Hrp = np.cross(Y, Erp(ys)) / et
chk("H8 H~_i = 1/2 (z + j x) e^{j b y}", close(Hip, 0.5 * np.outer(np.exp(1j * bb * ys), Z + 1j * X)))
chk("H9 H~_r = 1/2 (z + j x) e^{-j b y}", close(Hrp, 0.5 * np.outer(np.exp(-1j * bb * ys), Z + 1j * X)))
Etot = Eip(ys) + Erp(ys); Htot = Hip + Hrp
chk("H10 E~ = 120pi sin(by) (z + j x)", close(Etot, 120 * np.pi * np.outer(np.sin(bb * ys), Z + 1j * X)))
chk("H11 H~ = cos(by) (z + j x)", close(Htot, np.outer(np.cos(bb * ys), Z + 1j * X)))
ahat = lambda t: Z * np.cos(ww * t) - X * np.sin(ww * t)
okre = all(close(np.real(Etot * np.exp(1j * ww * t)), 120 * np.pi * np.outer(np.sin(bb * ys), ahat(t))) and
           close(np.real(Htot * np.exp(1j * ww * t)), np.outer(np.cos(bb * ys), ahat(t))) for t in np.linspace(0, 1 / fw, 13))
chk("H12 E = 120pi sin(by) a(t), H = cos(by) a(t), a = z cos wt - x sin wt", okre)
chk("H13 E nodes y = 0,10,20 cm; H nodes 5,15,25 cm", close(np.sin(bb * np.array([0, .1, .2])), 0, atol=1e-12) and close(np.cos(bb * np.array([.05, .15, .25])), 0, atol=1e-12))
# Faraday and Ampere by FD (y-dependence only): curl F = x dFz/dy - z dFx/dy
Ef = lambda yy, t: 120 * np.pi * np.sin(bb * yy) * ahat(t)
Hf = lambda yy, t: np.cos(bb * yy) * ahat(t)
curl = lambda F, yy, t, h: np.array([(F(yy + h, t)[2] - F(yy - h, t)[2]) / (2 * h), 0.0, -(F(yy + h, t)[0] - F(yy - h, t)[0]) / (2 * h)])
hy_, ht_ = 1e-7, 1e-15
errF = errA = 0
for yy in np.linspace(0.003, 0.29, 23):
    for t in np.linspace(0, 1 / fw, 11):
        cE = curl(Ef, yy, t, hy_); dH = (Hf(yy, t + ht_) - Hf(yy, t - ht_)) / (2 * ht_)
        cH = curl(Hf, yy, t, hy_); dE = (Ef(yy, t + ht_) - Ef(yy, t - ht_)) / (2 * ht_)
        errF = max(errF, np.max(np.abs(cE + mu * dH)) / (120 * np.pi * bb))
        errA = max(errA, np.max(np.abs(cH - ep * dE)) / bb)
chk("H14 Faraday curl E = -mu0 dH/dt (FD)", errF < 1e-5, f"{errF:.1e}")
chk("H15 Ampere curl H = eps0 dE/dt (FD)", errA < 1e-5, f"{errA:.1e}")
bh = lambda t: X * np.cos(ww * t) + Z * np.sin(ww * t)
chk("H16 page's Faraday: curl E = 120 pi beta cos(by) b(t), 120 pi beta = mu0 w", close(curl(Ef, 0.013, 1.1e-10, hy_), 120 * np.pi * bb * np.cos(bb * 0.013) * bh(1.1e-10), rtol=1e-6) and abs(120 * np.pi * bb - mu * ww) < 1e-6)
# S and w
Smax = max(np.max(np.abs(np.cross(Ef(yy, t), Hf(yy, t)))) for yy in ys for t in np.linspace(0, 1 / fw, 13))
chk("H17 S = E x H = 0 at every y, t", Smax < 1e-9)
wv = [0.5 * ep * np.dot(Ef(yy, t), Ef(yy, t)) + 0.5 * mu * np.dot(Hf(yy, t), Hf(yy, t)) for yy in ys for t in np.linspace(0, 1 / fw, 13)]
chk("H18 w = mu0/2 = 2 pi e-7 J/m^3 constant", close(wv, 2 * np.pi * 1e-7, rtol=1e-12))
# trap: pair Ex,Hz and pair Ez,Hx
yy, t = 0.031, 2.3e-10
Exv, Ezv = Ef(yy, t)[0], Ef(yy, t)[2]; Hxv, Hzv = Hf(yy, t)[0], Hf(yy, t)[2]
S1 = np.cross(Exv * X, Hzv * Z); S2 = np.cross(Ezv * Z, Hxv * X)
chk("H19 trap: Ex,Hz gives +30pi sin2by sin2wt y; Ez,Hx gives the negative",
    close(S1, 30 * np.pi * np.sin(2 * bb * yy) * np.sin(2 * ww * t) * Y) and close(S2, -30 * np.pi * np.sin(2 * bb * yy) * np.sin(2 * ww * t) * Y))
# (d) J_s and pressure
okJ = all(close(np.cross(Y, Hf(0.0, t)), X * np.cos(ww * t) + Z * np.sin(ww * t)) for t in np.linspace(0, 1 / fw, 13))
chk("H20 J_s = y x H(0,t) = x cos wt + z sin wt (n = +y out of conductor)", okJ)
chk("H21 J_s = 2 E_i(0,t)/eta0", all(close(np.cross(Y, Hf(0.0, t)), 2 * Ei_t(np.array([0.0]), t)[0] / et) for t in np.linspace(0, 1 / fw, 13)))
Fp = [np.cross(np.cross(Y, Hf(0.0, t)), 0.5 * mu * Hf(0.0, t)) for t in np.linspace(0, 1 / fw, 13)]
chk("H22 J_s x B/2 = -y 2pi e-7 N/m^2 at every instant", close(Fp, np.tile(-Y * 2 * np.pi * 1e-7, (13, 1)), rtol=1e-12))
Sic = 2 * A ** 2 / (2 * et)
chk("H23 <S_i> = 30 pi = 94.2 W/m^2; 2<S_i>/c = 2 pi e-7", abs(Sic - 30 * np.pi) < 1e-9 and abs(Sic - 94.25) < 0.01 and abs(2 * Sic / cc - 2 * np.pi * 1e-7) < 1e-20)
chk("H24 concept page: w = 2 eps0 E0^2 with E0 = 60 pi", abs(2 * ep * A ** 2 - 2 * np.pi * 1e-7) < 1e-20)
tl_ = np.linspace(0, 1 / fw, 401)
ex_ = np.array([Ef(0.05, t)[0] for t in tl_]); ez_ = np.array([Ef(0.05, t)[2] for t in tl_])
chk("H25 Ex and Ez standing waves 90 deg apart in time (<ExEz> = 0, equal rms)", abs(np.trapezoid(ex_ * ez_, tl_)) < 1e-9 * np.trapezoid(ez_ ** 2, tl_) and abs(np.trapezoid(ex_ ** 2, tl_) / np.trapezoid(ez_ ** 2, tl_) - 1) < 1e-9)

print("== I. concept-page example: 1.5 GHz in air")
lam_air = c / 1.5e9
chk("I1 lambda = 20 cm (c = 3e8), E nodes 0,10,20 cm, H nodes 5,15,25 cm", abs(lam_air - 0.2) < 2e-4)

print(f"\nTOTAL: {NP} PASS, {NF} FAIL")
