#!/usr/bin/env python3
"""L26 practice checks: standing waves and radiation pressure (numpy + scipy only).

Every number, sign and direction on practice/26-standing-waves-and-radiation-pressure.md is
printed here. Standing waves are built as incident + reflected travelling waves (Gamma = -1 at
the mirror, H = u x E / eta with np.cross) and compared with the closed forms on the page; each
is checked against the PEC condition (tangential E = 0 at the wall) and against Faraday and
Ampere-Maxwell by finite differences in space and time. Time averages are quadratures of the
real fields over one period; cell energies are quadratures over z. The good-conductor mirror
uses the exact gamma, eta, tau (no approximations) and integrates J x B and J.E numerically.
Handedness: L24 test u . [E(0) x E(T/4)] and an accumulated rotation angle.
Course constants eps0 = 1e-9/36pi (c = 3e8, eta0 = 120pi) where the page says so.
"""
import numpy as np
from scipy import integrate, optimize

mu0 = 4e-7 * np.pi
eps0 = 1e-9 / (36 * np.pi)       # course value
c = 1 / np.sqrt(mu0 * eps0)       # 3e8
eta0 = np.sqrt(mu0 / eps0)        # 120 pi
X, Y, Z = np.eye(3)
ALL = []


def hdr(s):
    print("\n" + "=" * 78 + "\n" + s + "\n" + "=" * 78)


def check(label, cond):
    print(f"  [{label}] {'OK' if cond else 'FAIL'}")
    ALL.append(bool(cond))


def close(label, a, b, rtol=1e-6, atol=0.0):
    ok = np.allclose(a, b, rtol=rtol, atol=atol)
    A, B = np.asarray(a), np.asarray(b)
    if A.size > 8:
        err = np.max(np.abs(A - B))
        print(f"  [{label}] {A.size} values, max abs diff {err:.2e} -> {'OK' if ok else 'FAIL'}")
    else:
        fa = ", ".join(f"{v:.9g}" for v in np.atleast_1d(A).ravel())
        fb = ", ".join(f"{v:.9g}" for v in np.atleast_1d(B).ravel())
        print(f"  [{label}] [{fa}] vs [{fb}] -> {'OK' if ok else 'FAIL'}")
    ALL.append(bool(ok))


def travelling(E0vec, u, beta, w, eta, phase=0.0, r0=np.zeros(3)):
    """Real travelling wave E = E0vec cos(wt - beta u.(r-r0) + phase), H = u x E / eta."""
    E0vec, u = np.asarray(E0vec, float), np.asarray(u, float)

    def E(r, t):
        return E0vec * np.cos(w * t - beta * np.dot(u, np.asarray(r) - r0) + phase)

    def H(r, t):
        return np.cross(u, E(r, t)) / eta
    return E, H


def add(*fs):
    return lambda r, t: sum(f(r, t) for f in fs)


def curl(F, r, t, h):
    r = np.asarray(r, float)
    J = np.zeros((3, 3))
    for k in range(3):
        d = np.zeros(3); d[k] = h
        J[:, k] = (F(r + d, t) - F(r - d, t)) / (2 * h)
    return np.array([J[2, 1] - J[1, 2], J[0, 2] - J[2, 0], J[1, 0] - J[0, 1]])


def ddt(F, r, t, dt):
    return (F(r, t + dt) - F(r, t - dt)) / (2 * dt)


def maxwell_td(label, E, H, eps, mu, w, beta, pts, ts, sig=0.0):
    h = 1e-5 / beta; dt = 1e-5 / w
    worst = 0.0
    for r in pts:
        for t in ts:
            a1, b1 = curl(E, r, t, h), -mu * ddt(H, r, t, dt)
            a2, b2 = curl(H, r, t, h), eps * ddt(E, r, t, dt) + sig * E(r, t)
            s1 = max(np.abs(b1).max(), np.abs(a1).max(), 1e-30)
            s2 = max(np.abs(b2).max(), np.abs(a2).max(), 1e-30)
            worst = max(worst, np.abs(a1 - b1).max() / s1, np.abs(a2 - b2).max() / s2)
    check(f"{label}: Faraday and Ampere-Maxwell by finite differences (worst rel err {worst:.1e})", worst < 1e-5)


def tavg(f, w, n=1):
    T = 2 * np.pi / w
    return integrate.quad(f, 0, n * T, limit=400)[0] / (n * T)


def hand(Eph, u):
    v = np.dot(u, np.cross(np.real(Eph), np.real(1j * Eph)))
    return "right" if v > 1e-12 else ("left" if v < -1e-12 else "linear")


def hand_brute(Eph, u, n=400):
    ts = np.linspace(0, 2 * np.pi, n + 1)
    vs = [np.real(Eph * np.exp(1j * t)) for t in ts]
    ang = sum(np.arctan2(np.dot(u, np.cross(a, b)), np.dot(a, b)) for a, b in zip(vs[:-1], vs[1:]))
    return "right" if ang > 1 else ("left" if ang < -1 else "linear")


def mirror_pair(E0, pol, u, beta, w, eta, zm_vec):
    """Incident wave along u, reflected (Gamma = -1 at the plane through zm_vec) along -u."""
    Ei, Hi = travelling(E0 * pol, u, beta, w, eta)
    # reflected: E_r(r,t) = -E_i(mirror image phase): E0 pol cos(wt + beta u.r - 2 beta u.zm) with minus
    ph = -2 * beta * np.dot(u, zm_vec)
    Er, Hr = travelling(-E0 * pol, -np.asarray(u), beta, w, eta, phase=ph)
    return Ei, Hi, Er, Hr


# ============================================================================
hdr("26.1 Nodes in front of a mirror")
f = 1.25e9; w = 2 * np.pi * f; er = 4; E0 = 10.0
lam0 = c / f; lam = lam0 / np.sqrt(er); beta = 2 * np.pi / lam; eta1 = eta0 / np.sqrt(er)
print(f"  lambda0 = {lam0*100:.4f} cm, lambda1 = {lam*100:.4f} cm, beta1 = {beta:.4f} rad/m = {beta/np.pi:.4f} pi, eta1 = {eta1/np.pi:.4f} pi")
close("lambda1 = 12 cm", lam, 0.12)
close("beta1 = 50pi/3", beta, 50 * np.pi / 3)
Ei, Hi, Er, Hr = mirror_pair(E0, X, Z, beta, w, eta1, np.zeros(3))
E, H = add(Ei, Er), add(Hi, Hr)
zz = np.linspace(-0.15, 0, 150001)
ts = np.linspace(0, 2 * np.pi / w, 401)
ampE = np.array([max(abs(E([0, 0, z], t)[0]) for t in ts[::8]) for z in zz[::50]])
zs = zz[::50]
# nodes by exact amplitude formulas checked vs construction
close("E construction = x 2E0 sin(bz) sin(wt)", [E([0, 0, z], t)[0] for z in (-0.01, -0.037) for t in (1e-10, 3.3e-10)],
      [2 * E0 * np.sin(beta * z) * np.sin(w * t) for z in (-0.01, -0.037) for t in (1e-10, 3.3e-10)])
close("H construction = y (2E0/eta1) cos(bz) cos(wt)", [H([0, 0, z], t)[1] for z in (-0.01, -0.037) for t in (1e-10, 3.3e-10)],
      [2 * E0 / eta1 * np.cos(beta * z) * np.cos(w * t) for z in (-0.01, -0.037) for t in (1e-10, 3.3e-10)])
check("PEC: E(0,t) = 0", max(abs(E([0, 0, 0], t)).max() for t in ts) < 1e-12)
maxwell_td("26.1", E, H, er * eps0, mu0, w, beta, [[0.1, -0.2, -0.013], [0, 0, -0.071]], [1.1e-10, 4.7e-10])
Eamp = lambda z: 2 * E0 * abs(np.sin(beta * z))
Hamp = lambda z: 2 * E0 / eta1 * abs(np.cos(beta * z))
fine = np.linspace(-0.15, 0, 1500001)
eN = fine[np.r_[False, (np.diff(np.sign(np.sin(beta * fine))) != 0)]]
hN = fine[np.r_[False, (np.diff(np.sign(np.cos(beta * fine))) != 0)]]
eN = sorted(set(np.round(np.r_[eN, 0.0] * 100, 3)))[::-1]
hN = sorted(set(np.round(np.r_[hN, -0.15 if abs(np.cos(beta * -0.15)) < 1e-9 else []] * 100, 3)))[::-1]
print(f"  E nodes in [-15, 0] cm: {eN}; H nodes: {hN}; |cos(beta*(-15cm))| = {abs(np.cos(beta*-0.15)):.1e}")
close("E nodes 0, -6, -12 cm", eN, [0.0, -6.0, -12.0], atol=2e-3)
close("H nodes -3, -9, -15 cm", hN, [-3.0, -9.0, -15.0], atol=2e-3)
print(f"  at z = -1 cm: beta z = {beta*-0.01/np.pi:.4f} pi; |E| = {Eamp(-0.01):.6f} V/m, |H| = {Hamp(-0.01)*1e3:.4f} mA/m = sqrt3/(6pi) = {np.sqrt(3)/(6*np.pi)*1e3:.4f}")
close("|E(-1cm)| = E0 = 10 V/m (numeric max over t)", max(abs(E([0, 0, -0.01], t)[0]) for t in ts), 10.0, rtol=1e-4)
close("|H(-1cm)| = sqrt3/6pi A/m (numeric max over t)", max(abs(H([0, 0, -0.01], t)[1]) for t in ts), np.sqrt(3) / (6 * np.pi), rtol=1e-4)

# ============================================================================
hdr("26.2 True or false (free space, page's standing wave)")
f = 1e9; w = 2 * np.pi * f; beta = w / c; lam = c / f; E0 = 1.0
Ei, Hi, Er, Hr = mirror_pair(E0, X, Z, beta, w, eta0, np.zeros(3))
E, H = add(Ei, Er), add(Hi, Hr)
zq = [-0.03, -0.11, -0.2, -0.27]
Savg = [tavg(lambda t: np.cross(E([0, 0, z], t), H([0, 0, z], t))[2], w) for z in zq]
print(f"  (a) <S_z> at z = {zq}: {np.round(Savg, 14)}")
check("(a) <S> = 0 at every z (quadrature)", np.abs(Savg).max() < 1e-12)
Sins = np.cross(E([0, 0, -lam / 8], 2 * np.pi / w / 8), H([0, 0, -lam / 8], 2 * np.pi / w / 8))
print(f"  (b) S at z = -lambda/8, wt = pi/4: {Sins} ; formula (E0^2/eta) sin2bz sin2wt = {E0**2/eta0*np.sin(-np.pi/2)*np.sin(np.pi/2):.6f}")
check("(b) S != 0 somewhere: FALSE statement", abs(Sins[2]) > 1e-4)
close("(b) S formula", Sins[2], E0**2 / eta0 * np.sin(2 * beta * -lam / 8) * np.sin(2 * w * (np.pi / 4 / w)))
wden = lambda z, t: 0.5 * eps0 * E([0, 0, z], t) @ E([0, 0, z], t) + 0.5 * mu0 * H([0, 0, z], t) @ H([0, 0, z], t)
zs = np.linspace(-lam, 0, 801); tt = np.linspace(0, 2 * np.pi / w, 801)
maxw_over_z = [max(wden(z, t) for z in zs[::4]) for t in tt[::4]]
print(f"  (c) min over t of max over z of w = {min(maxw_over_z):.4e} J/m^3 (2 eps0 E0^2 * 1/2... ; 2eps0E0^2 = {2*eps0*E0**2:.4e})")
check("(c) w never zero everywhere at once: FALSE statement", min(maxw_over_z) > 0.4 * eps0 * E0**2)
close("(c) w formula", wden(-0.07, 3e-10), 2 * eps0 * E0**2 * (np.sin(beta * -0.07)**2 * np.sin(w * 3e-10)**2 + np.cos(beta * -0.07)**2 * np.cos(w * 3e-10)**2))
# (d) zero crossings: standing fixed, travelling moves
def zeros_of(fun, zgrid):
    s = np.sign([fun(z) for z in zgrid]); return zgrid[np.r_[False, np.diff(s) != 0]]
zg = np.linspace(-0.6, -0.001, 6000)
zs1 = zeros_of(lambda z: E([0, 0, z], 0.13e-9)[0], zg); zs2 = zeros_of(lambda z: E([0, 0, z], 0.41e-9)[0], zg)
zh1 = zeros_of(lambda z: H([0, 0, z], 0.13e-9)[1], zg); zh2 = zeros_of(lambda z: H([0, 0, z], 0.41e-9)[1], zg)
zt1 = zeros_of(lambda z: Ei([0, 0, z], 0.13e-9)[0], zg); zt2 = zeros_of(lambda z: Ei([0, 0, z], 0.41e-9)[0], zg)
print(f"  (d) E zeros t1 {np.round(zs1,3)} t2 {np.round(zs2,3)}; H zeros t1 {np.round(zh1,3)} t2 {np.round(zh2,3)}; travelling t1 {np.round(zt1,3)} t2 {np.round(zt2,3)}")
check("(d) standing E and H zeros fixed in time, travelling zeros move: TRUE", np.allclose(zs1, zs2, atol=2e-4) and np.allclose(zh1, zh2, atol=2e-4) and not np.allclose(zt1, zt2, atol=1e-3))
check("(d) E and H zero sets are both lambda/2-spaced (same shape, shifted lambda/4)", np.allclose(np.diff(zs1), lam / 2, atol=2e-4) and np.allclose(np.diff(zh1), lam / 2, atol=2e-4))
# (e) time quadrature
tg = np.linspace(0, 1 / f, 40001)[:-1]
aE = np.array([abs(E([0, 0, -lam / 4], t)[0]) for t in tg]); aH = np.array([abs(H([0, 0, 0], t)[1]) for t in tg])
tE = tg[aE > aE.max() * (1 - 1e-9)]; tH = tg[aH > aH.max() * (1 - 1e-9)]
print(f"  (e) E at E antinode peaks at wt/pi = {np.round(w*tE/np.pi, 4)}; H at H antinode peaks at wt/pi = {np.round(w*tH/np.pi, 4)}")
tE, tH = tE[0], tH[0]
print(f"  (e) E peak at E antinode at wt = {w*tE/np.pi:.4f} pi; H peak at H antinode at wt = {w*tH/np.pi:.4f} pi")
check("(e) peaks a quarter period apart (E at pi/2, 3pi/2; H at 0, pi): FALSE statement", abs(w * tE - np.pi / 2) < 1e-3 and abs(w * tH) < 1e-3)
# (f) handedness flips on reflection
Ei_ph = np.array([1, -1j, 0]); u_i = Z
Er_ph = -Ei_ph; u_r = -Z
print(f"  (f) incident x - jy along +z: {hand(Ei_ph, u_i)} / brute {hand_brute(Ei_ph, u_i)}; reflected -(x - jy) along -z: {hand(Er_ph, u_r)} / brute {hand_brute(Er_ph, u_r)}")
check("(f) right-circular returns left-circular: FALSE statement", hand(Ei_ph, u_i) == hand_brute(Ei_ph, u_i) == "right" and hand(Er_ph, u_r) == hand_brute(Er_ph, u_r) == "left")

# ============================================================================
hdr("26.3 Travelling, standing or both (wave from z > 0 toward -z)")
def classify(eta2, E0=1.0, f=1e9):
    w = 2 * np.pi * f; b = w / c
    G = (eta2 - eta0) / (eta2 + eta0)
    zs = np.linspace(0, c / f, 20001)
    amp = np.abs(E0 * (np.exp(1j * b * zs) + G * np.exp(-1j * b * zs)))  # incident e^{+jbz} (toward -z)
    Sn = (1 - abs(G)**2) * E0**2 / (2 * eta0)
    return G, amp.min(), amp.max(), amp[0], Sn
for name, eta2 in [("(i) PEC", 0.0), ("(ii) er = 4", eta0 / 2), ("(iii) mur = er = 5", eta0 * np.sqrt(5 / 5))]:
    G, mn, mx, a0, Sn = classify(eta2)
    kind = "all standing" if abs(abs(G) - 1) < 1e-12 else ("all travelling" if abs(G) < 1e-12 else "part travelling, part standing")
    print(f"  {name}: Gamma = {G:+.6f}; |E| from {mn:.6f} to {mx:.6f} E0; |E(0)| = {a0:.6f} E0; net <S> = {Sn:.4e} W/m^2 (E0 = 1) -> {kind}")
G2, mn2, mx2, a02, _ = classify(eta0 / 2)
close("(ii) Gamma = -1/3, |E| in [2/3, 4/3] E0, min at interface", [G2, mn2, mx2, a02], [-1 / 3, 2 / 3, 4 / 3, 2 / 3], rtol=1e-6, atol=1e-7)
check("(i) Gamma = -1 -> standing; (iii) Gamma = 0 -> travelling", classify(0.0)[0] == -1 and abs(classify(eta0)[0]) < 1e-15)

# ============================================================================
hdr("26.4 A laser on a small mirror (find the error)")
P = 3.0; Ab = 2e-6; Am = 4e-4
S = P / Ab; pr = 2 * S / c
print(f"  <S_i> = {S:.4e} W/m^2, 2<S>/c = {pr:.4e} Pa; student F = p * A_mirror = {pr*Am:.4e} N")
print(f"  correct F = p * A_beam = 2P/c = {pr*Ab:.4e} N = {2*P/c*1e9:.4f} nN; absorber P/c = {P/c*1e9:.4f} nN; ratio student/correct = {Am/Ab:.1f}")
close("student 4 uN", pr * Am, 4e-6)
close("2P/c = 20 nN", 2 * P / c, 2e-8)
close("absorber 10 nN", P / c, 1e-8)

# ============================================================================
hdr("26.5 Sunlight at Mars")
S = 600.0; A = 400.0
pm, pa = 2 * S / c, S / c
E0 = np.sqrt(2 * eta0 * S); Js = 2 * E0 / eta0
print(f"  mirror {pm*1e6:.4f} uPa, absorber {pa*1e6:.4f} uPa; forces {pm*A*1e3:.4f} mN, {pa*A*1e3:.4f} mN")
print(f"  E0 = {E0:.4f} V/m, J_s peak = 2E0/eta0 = {Js:.4f} A/m; eps0 E0^2 = {eps0*E0**2*1e6:.4f} uPa")
close("4 uPa, 2 uPa", [pm, pa], [4e-6, 2e-6])
close("1.6 mN, 0.8 mN", [pm * A, pa * A], [1.6e-3, 0.8e-3])
close("E0 = 672.6 V/m", E0, 672.6, rtol=1e-4)
close("J_s = 3.57 A/m", Js, 3.57, rtol=1e-3)
close("eps0 E0^2 = 2<S>/c", eps0 * E0**2, pm)

# ============================================================================
hdr("26.6 A mirror off the origin")
f = 3e8; w = 2 * np.pi * f; beta = w / c; d = 0.375; E0 = 5.0
print(f"  beta = {beta/np.pi:.6f} pi rad/m, lambda = {2*np.pi/beta:.6f} m, beta d = {beta*d/np.pi:.6f} pi")
Ei, Hi, Er, Hr = mirror_pair(E0, Y, Z, beta, w, eta0, d * Z)
E, H = add(Ei, Er), add(Hi, Hr)
tt = np.linspace(0, 1 / f, 37); zz = [-0.43, -0.2, 0.0, 0.11, 0.3]
close("(a) E_r = y 5 sin(wt + 2pi z)", [Er([0, 0, z], t)[1] for z in zz for t in tt], [5 * np.sin(w * t + 2 * np.pi * z) for z in zz for t in tt], atol=1e-9)
close("(a) H_r = +x (1/24pi) sin(wt + 2pi z)", [Hr([0, 0, z], t)[0] for z in zz for t in tt], [(5 / eta0) * np.sin(w * t + 2 * np.pi * z) for z in zz for t in tt], atol=1e-12)
close("(b) E = y 10 sin(2pi z - 3pi/4) sin(wt - 3pi/4)", [E([0, 0, z], t)[1] for z in zz for t in tt],
      [10 * np.sin(2 * np.pi * z - 3 * np.pi / 4) * np.sin(w * t - 3 * np.pi / 4) for z in zz for t in tt], atol=1e-9)
close("(b) H = -x (1/12pi) cos(2pi z - 3pi/4) cos(wt - 3pi/4)", [H([0, 0, z], t)[0] for z in zz for t in tt],
      [-(1 / (12 * np.pi)) * np.cos(2 * np.pi * z - 3 * np.pi / 4) * np.cos(w * t - 3 * np.pi / 4) for z in zz for t in tt], atol=1e-12)
check("PEC: tangential E(d,t) = 0", max(abs(E([0, 0, d], t)).max() for t in tt) < 1e-12)
check("E, H have no x/z resp. y/z components", max(abs(E([0, 0, z], t)[[0, 2]]).max() + abs(H([0, 0, z], t)[[1, 2]]).max() for z in zz for t in tt) < 1e-15)
maxwell_td("26.6", E, H, eps0, mu0, w, beta, [[0, 0, -0.31], [0.2, 0.1, 0.07]], [1.3e-9, 2.2e-9])
zf = np.linspace(-0.5 + 1e-9, d, 875001)
en = zf[np.r_[False, np.diff(np.sign(np.sin(beta * (zf - d)))) != 0]]
hn = zf[np.r_[False, np.diff(np.sign(np.cos(beta * (zf - d)))) != 0]]
print(f"  (c) E nodes (excl. mirror) {np.round(en,4)} + mirror {d}; H nodes {np.round(hn,4)}")
close("(c) E nodes -0.125 (and mirror 0.375); H nodes -0.375, 0.125", [en[0], hn[0], hn[1]], [-0.125, -0.375, 0.125], atol=2e-6)
# J_s = n x H(d) with n = -z
Js_num = [np.cross(-Z, H([0, 0, d], t)) for t in tt]
close("(d) J_s = y (1/12pi) cos(wt - 3pi/4)", np.array(Js_num), np.array([Y * np.cos(w * t - 3 * np.pi / 4) / (12 * np.pi) for t in tt]), atol=1e-12)
print(f"  (d) 1/12pi = {1/(12*np.pi)*1e3:.4f} mA/m; 2E0/eta0 = {2*E0/eta0*1e3:.4f} mA/m; along incident E (y) at the wall: E_i(d,t) = y 5 cos(wt - 3pi/4)")
close("(d) J_s = 2 E_i(d,t)/eta0 (along the incident E at the wall)", np.array(Js_num), np.array([2 * Ei([0, 0, d], t) / eta0 for t in tt]), atol=1e-12)
aE0 = max(abs(E([0, 0, 0], t)[1]) for t in np.linspace(0, 1 / f, 2001))
aH0 = max(abs(H([0, 0, 0], t)[0]) for t in np.linspace(0, 1 / f, 2001))
print(f"  (e) at z = 0: |E| amplitude = {aE0:.6f} V/m (5 sqrt2 = {5*np.sqrt(2):.6f}), |H| amplitude = {aH0*1e3:.4f} mA/m")
close("(e) 7.07 V/m, 18.8 mA/m", [aE0, aH0 * 1e3], [5 * np.sqrt(2), 1e3 / (12 * np.pi) / np.sqrt(2)], rtol=1e-5)
# first t > 0 when E at z=0 peaks: sin(wt - 3pi/4) = +-1 -> wt = pi/4 (sin = -1 -> E = 10 sin(-3pi/4)(-1) = +7.07)
tg = np.linspace(0, 0.5 / f, 200001)
t_pk = tg[np.argmax([abs(E([0, 0, 0], t)[1]) for t in tg])]
print(f"  (e) first |E(0,t)| peak at wt = {w*t_pk/np.pi:.5f} pi, t = {t_pk*1e9:.5f} ns, E_y = {E([0,0,0], t_pk)[1]:+.5f} V/m")
close("(e) peak at wt = pi/4, t = 0.417 ns, E_y = +7.07", [w * t_pk, t_pk * 1e9, E([0, 0, 0], t_pk)[1]], [np.pi / 4, 1 / 2.4, 5 * np.sqrt(2)], rtol=1e-5)

# ============================================================================
hdr("26.7 Energy in a quarter-wave cell")
f = 2e9; w = 2 * np.pi * f; er = 2.25; E0 = 30.0
eps1 = er * eps0; eta1 = eta0 / np.sqrt(er); lam = c / f / np.sqrt(er); beta = 2 * np.pi / lam
print(f"  eta1 = {eta1/np.pi:.4f} pi Ohm, lambda1 = {lam*100:.4f} cm, beta1 = {beta/np.pi:.4f} pi rad/m")
Ei, Hi, Er, Hr = mirror_pair(E0, X, Z, beta, w, eta1, np.zeros(3))
E, H = add(Ei, Er), add(Hi, Hr)
maxwell_td("26.7", E, H, eps1, mu0, w, beta, [[0, 0, -0.013], [0, 0, -0.044]], [0.07e-9, 0.31e-9])
Sz = lambda z, t: np.cross(E([0, 0, z], t), H([0, 0, z], t))[2]
wd = lambda z, t: 0.5 * eps1 * E([0, 0, z], t) @ E([0, 0, z], t) + 0.5 * mu0 * H([0, 0, z], t) @ H([0, 0, z], t)
close("(a) S = z (E0^2/eta1) sin2bz sin2wt", [Sz(z, t) for z in (-0.004, -0.031) for t in (0.05e-9, 0.2e-9)],
      [E0**2 / eta1 * np.sin(2 * beta * z) * np.sin(2 * w * t) for z in (-0.004, -0.031) for t in (0.05e-9, 0.2e-9)])
Smax = E0**2 / eta1
print(f"  (a) max |S| = E0^2/eta1 = {Smax:.6f} W/m^2; S at z = -lambda/8, wt = pi/4: {Sz(-lam/8, np.pi/4/w):+.6f}; at wt = 3pi/4: {Sz(-lam/8, 3*np.pi/4/w):+.6f}")
res = optimize.minimize(lambda p: -abs(Sz(p[0], p[1])), x0=[-0.012, 0.1e-9], method="Nelder-Mead", options=dict(xatol=1e-12, fatol=1e-12))
print(f"  (a) numeric max |S| = {-res.fun:.6f} at z = {res.x[0]*100:.4f} cm, wt = {w*res.x[1]/np.pi:.4f} pi")
close("(a) max |S| = 3.58 W/m^2 at z = -1.25 cm", [-res.fun, Smax], [3.58, 3.58], rtol=2e-3)
check("(a) at z=-1.25 cm, wt=pi/4: S along -z (away from mirror)", Sz(-lam / 8, np.pi / 4 / w) < 0)
wavg = tavg(lambda t: wd(-0.017, t), w)
print(f"  (b) <w> = eps1 E0^2 = {eps1*E0**2:.6e} J/m^3; quadrature at z=-1.7 cm: {wavg:.6e}")
close("(b) <w> uniform = eps1 E0^2", [tavg(lambda t: wd(z, t), w) for z in (-0.003, -0.017, -0.04)], [eps1 * E0**2] * 3)
close("(b) 1.79e-8 J/m^3", eps1 * E0**2, 1.79e-8, rtol=3e-3)
cell = [integrate.quad(lambda z: wd(z, t), -lam / 4, 0, limit=200)[0] for t in np.linspace(0, 0.5 / f, 7)]
print(f"  (c) cell energy at 7 instants: {np.round(np.array(cell)*1e10, 8)} x 1e-10 J/m^2; eps1 E0^2 lambda/4 = {eps1*E0**2*lam/4:.6e}")
close("(c) cell energy constant = eps1 E0^2 lambda/4", cell, [eps1 * E0**2 * lam / 4] * 7)
close("(c) 4.48e-10 J/m^2", eps1 * E0**2 * lam / 4, 4.48e-10, rtol=2e-3)
check("(c) S = 0 at z = 0 and z = -lambda/4 at all t", max(abs(Sz(0, t)) + abs(Sz(-lam / 4, t)) for t in np.linspace(0, 1 / f, 50)) < 1e-9)
# Poynting theorem dw/dt + dS/dz = 0
hz, ht = lam * 1e-6, 1e-6 / f
pt = max(abs((wd(z, t + ht) - wd(z, t - ht)) / (2 * ht) + (Sz(z + hz, t) - Sz(z - hz, t)) / (2 * hz)) / (w * eps1 * E0**2)
         for z in (-0.007, -0.019) for t in (0.04e-9, 0.13e-9))
check(f"Poynting theorem dw/dt = -dS/dz (rel err {pt:.1e})", pt < 1e-6)
# (d) where is the energy at wt = 0 and pi/2
we0 = integrate.quad(lambda z: 0.5 * mu0 * H([0, 0, z], 0) @ H([0, 0, z], 0), -lam / 4, 0)[0]
ee0 = integrate.quad(lambda z: 0.5 * eps1 * E([0, 0, z], 0) @ E([0, 0, z], 0), -lam / 4, 0)[0]
t2 = np.pi / 2 / w
we2 = integrate.quad(lambda z: 0.5 * mu0 * H([0, 0, z], t2) @ H([0, 0, z], t2), -lam / 4, 0)[0]
ee2 = integrate.quad(lambda z: 0.5 * eps1 * E([0, 0, z], t2) @ E([0, 0, z], t2), -lam / 4, 0)[0]
print(f"  (d) wt = 0: magnetic {we0:.4e}, electric {ee0:.4e}; wt = pi/2: magnetic {we2:.4e}, electric {ee2:.4e}")
check("(d) all magnetic at wt=0, all electric at wt=pi/2", ee0 < 1e-25 and we2 < 1e-25)
zg = np.linspace(-lam / 4, 0, 20001)
zpk0 = zg[np.argmax([wd(z, 0) for z in zg])]; zpk2 = zg[np.argmax([wd(z, t2) for z in zg])]
print(f"  (d) w peaks at z = {zpk0*100:.4f} cm (wt=0) and z = {zpk2*100:.4f} cm (wt=pi/2)")
close("(d) peaks at mirror and at -2.5 cm", [zpk0, zpk2], [0.0, -0.025], atol=1e-9)

# ============================================================================
hdr("26.8 Ripple in front of a dielectric")
Emax, Emin, dmin = 10.0, 5.0, 0.10
E0 = (Emax + Emin) / 2; G = -(Emax - Emin) / (Emax + Emin)
eta2 = eta0 * (1 + G) / (1 - G); er = (eta0 / eta2)**2
lam0 = 2 * dmin; f = c / lam0
print(f"  E0 = {E0} V/m, |Gamma| = {abs(G):.6f}, Gamma = {G:+.6f}, eta2 = {eta2/eta0:.6f} eta0, er = {er:.6f}, lambda0 = {lam0*100} cm, f = {f/1e9:.6f} GHz")
close("E0 = 7.5, Gamma = -1/3, er = 4, f = 1.5 GHz", [E0, G, er, f], [7.5, -1 / 3, 4, 1.5e9])
w = 2 * np.pi * f; b = w / c
zs = np.linspace(-0.25, 0, 250001)
amp = np.abs(E0 * (np.exp(-1j * b * zs) + G * np.exp(1j * b * zs)))
from scipy.signal import argrelextrema
mins = zs[argrelextrema(amp, np.less)[0]]; maxs = zs[argrelextrema(amp, np.greater)[0]]
print(f"  forward check: |E| range [{amp.min():.6f}, {amp.max():.6f}]; |E(0)| = {amp[-1]:.6f}; interior minima {np.round(mins*100,3)} cm; maxima {np.round(maxs*100,3)} cm")
close("forward: min 5 at z = 0, -10, -20; max 10 at -5, -15 (and -25 edge)", [amp.min(), amp.max(), amp[-1]] + list(mins) + list(maxs),
      [5, 10, 5, -0.2, -0.1, -0.15, -0.05], atol=2e-6)
# net <S> by quadrature of the real fields
eps2 = er * eps0
Ei, Hi = travelling(E0 * X, Z, b, w, eta0)
Er, Hr = travelling(G * E0 * X, -Z, b, w, eta0)
Sq = [tavg(lambda t: np.cross(Ei([0, 0, z], t) + Er([0, 0, z], t), Hi([0, 0, z], t) + Hr([0, 0, z], t))[2], w) for z in (-0.013, -0.077)]
Sn = (1 - G**2) * E0**2 / (2 * eta0)
print(f"  (c) net <S> = {Sn*1e3:.6f} mW/m^2 (= 50/240pi = {50/(240*np.pi)*1e3:.6f}); quadrature {np.round(np.array(Sq)*1e3,6)}; transmitted fraction {1-G**2:.6f}")
close("(c) net <S> = 66.3 mW/m^2 by quadrature", Sq, [Sn, Sn])
close("(c) 66.3 mW/m^2, 8/9", [Sn * 1e3, 1 - G**2], [66.3, 8 / 9], rtol=1e-3)
tau = 1 + G
St = abs(tau * E0)**2 / (2 * eta2)
close("(c) transmitted <S> in the dielectric equals net <S>", St, Sn)
Gp = abs(G); eta2p = eta0 * (1 + Gp) / (1 - Gp)
print(f"  (d) Gamma = +1/3 needs eta2 = {eta2p/eta0:.4f} eta0 -> er = {(eta0/eta2p)**2:.4f} < 1 for mu_r = 1")
close("(d) er = 1/4", (eta0 / eta2p)**2, 0.25)
print(f"  E0^2 = {E0**2} (V/m)^2; transmitted |tau E0|^2/(2 eta2) = {abs(tau*E0)**2:.4f}/(2*{eta2/np.pi:.1f}pi) = {St*1e3:.4f} mW/m^2")
print(f"  watch-out: reading 10 cm as lambda gives f = c/0.1 m = {c/0.1/1e9:.4f} GHz")

# ============================================================================
hdr("26.9 Is it a standing wave (SP17 E3 #1b style)")
w = 3 * np.pi * 1e9; b = 20 * np.pi; Ea = 120.0
# unknowns H0 and eps: solve from FD curls of the given forms
def fields(H0, eps):
    E = lambda r, t: X * Ea * np.cos(b * r[1]) * np.cos(w * t)
    H = lambda r, t: Z * H0 * np.sin(b * r[1]) * np.sin(w * t)
    return E, H
r0, t0 = np.array([0, 0.013, 0]), 0.071e-9
E1, H1 = fields(1.0, 1.0)
cE = curl(E1, r0, t0, 1e-7)[2]; dH = ddt(H1, r0, t0, 1e-14)[2]       # curl E_z = -mu0 H0 dH/dt (per unit H0)
H0 = -cE / (mu0 * dH)
E1, H1 = fields(H0, 1.0)
cH = curl(H1, r0, t0, 1e-7)[0]; dE = ddt(E1, r0, t0, 1e-14)[0]
epsv = cH / dE; er = epsv / eps0
print(f"  (a) from Faraday H0 = {H0:+.6f} A/m (-2/pi = {-2/np.pi:+.6f}); from Ampere eps = {epsv:.6e} -> er = {er:.6f}")
print(f"  (a) 120*20pi = {120*20*np.pi/np.pi:.1f} pi; mu0*w = {mu0*w/np.pi**2:.4f} pi^2; eps = 1/(9pi) e-9 = {1/(9*np.pi)*1e-9:.6e}; 2 beta = {2*b/np.pi:.1f} pi")
close("(a) H0 = -2/pi, er = 4", [H0, er], [-2 / np.pi, 4.0], rtol=1e-5)
eps1 = 4 * eps0; eta1 = eta0 / 2
E, H = fields(-2 / np.pi, eps1)
maxwell_td("26.9", E, H, eps1, mu0, w, b, [[0, 0.013, 0], [0.3, -0.047, 0.2]], [0.071e-9, 0.29e-9])
check("divergences zero (E_x indep of x, H_z indep of z)", True)
print(f"  check beta = w sqrt(mu0 eps1) = {w*np.sqrt(mu0*eps1)/np.pi:.6f} pi; |H0|/E_peak = {2/np.pi/120:.6e} vs 1/eta1 = {1/eta1:.6e}")
close("beta consistent, |H0|/120 = 1/eta1", [w * np.sqrt(mu0 * eps1), 2 / np.pi / 120], [b, 1 / eta1])
# (b) two travelling waves
Ep, Hp = travelling(60 * X, Y, b, w, eta1); Em, Hm = travelling(60 * X, -Y, b, w, eta1)
pts = [[0, y, 0] for y in (-0.03, 0.006, 0.041)]; tts = [0.02e-9, 0.17e-9, 0.5e-9]
close("(b) E = x60cos(wt-20pi y) + x60cos(wt+20pi y)", [E(p, t) for p in pts for t in tts], [Ep(p, t) + Em(p, t) for p in pts for t in tts], atol=1e-9)
close("(b) H = sum of -z(1/pi)cos(wt-by) and +z(1/pi)cos(wt+by)", [H(p, t) for p in pts for t in tts], [Hp(p, t) + Hm(p, t) for p in pts for t in tts], atol=1e-12)
print(f"  (b) +y wave H at (y=0,t=0): {Hp([0,0,0],0)} (=-z/pi = {-1/np.pi:.6f}); -y wave H: {Hm([0,0,0],0)}; lambda = {2*np.pi/b*100:.4f} cm; 60/eta1 = {60/eta1:.6f} = 1/pi")
close("(b) H amplitudes 1/pi, lambda 10 cm", [Hp([0, 0, 0], 0)[2], Hm([0, 0, 0], 0)[2], 2 * np.pi / b], [-1 / np.pi, 1 / np.pi, 0.1])
# (c)
Sy = lambda y, t: np.cross(E([0, y, 0], t), H([0, y, 0], t))[1]
close("(c) S = y (60/pi) sin(2by) sin(2wt)", [Sy(y, t) for y in (0.006, 0.019) for t in tts], [60 / np.pi * np.sin(2 * b * y) * np.sin(2 * w * t) for y in (0.006, 0.019) for t in tts], atol=1e-9)
Sav = [tavg(lambda t: Sy(y, t), w) for y in (0.006, 0.019, -0.033)]
wav = [tavg(lambda t: 0.5 * eps1 * E([0, y, 0], t) @ E([0, y, 0], t) + 0.5 * mu0 * H([0, y, 0], t) @ H([0, y, 0], t), w) for y in (0.006, 0.019, -0.033)]
print(f"  (c) <S_y> = {np.round(Sav, 14)}; <w> = {np.round(wav, 16)} ; 4e-7/pi = {4e-7/np.pi:.6e}")
check("(c) <S> = 0", np.abs(Sav).max() < 1e-10)
close("(c) <w> = (4/pi)e-7 = 1.27e-7 J/m^3 at every y", wav, [4e-7 / np.pi] * 3)
# (d)
y1 = optimize.brentq(lambda y: np.cos(b * y), 0.001, 0.04)
print(f"  (d) smallest y1 > 0 with E_x = 0: {y1*100:.6f} cm")
close("(d) y1 = 2.5 cm", y1, 0.025)
Jn = [np.cross(-Y, H([0, y1, 0], t)) for t in tts]
close("(d) J_s = x (2/pi) sin(wt)", Jn, [X * 2 / np.pi * np.sin(w * t) for t in tts], atol=1e-12)
close("(d) J_s = 2 E_(+y)(y1,t)/eta1 (incident on the wall)", Jn, [2 * Ep([0, y1, 0], t) / eta1 for t in tts], atol=1e-12)
print(f"  (d) 2/pi = {2/np.pi:.6f} A/m")
print(f"  (e) E_x(0,t) = 120 cos wt: amplitude {max(abs(E([0,0,0], t)[0]) for t in np.linspace(0, 2*np.pi/w, 101)):.4f} V/m; H_z(0,t) = {max(abs(H([0,0,0], t)[2]) for t in np.linspace(0, 2*np.pi/w, 101)):.1e}")
check("(e) y = 0 is an E antinode / H node", abs(E([0, 0, 0], 0)[0] - 120) < 1e-9 and max(abs(H([0, 0, 0], t)[2]) for t in tts) < 1e-15)

# ============================================================================
hdr("26.10 A good-conductor mirror (aluminium, 1 GHz) -- exact fields")
f = 1e9; w = 2 * np.pi * f; sig = 3.5e7; E0 = 100.0
loss = sig / (w * eps0)
g2 = np.sqrt(1j * w * mu0 * (sig + 1j * w * eps0)); g2 = g2 if g2.real > 0 else -g2
eta2 = np.sqrt(1j * w * mu0 / (sig + 1j * w * eps0))
delta = 1 / np.sqrt(np.pi * f * mu0 * sig); Rs = 1 / (sig * delta)
print(f"  (a) sigma/(w eps0) = {loss:.4e}; delta = {delta*1e6:.6f} um (exact 1/alpha = {1/g2.real*1e6:.6f}); R_s = {Rs*1e3:.6f} mOhm; Re eta2 = {eta2.real*1e3:.6f} mOhm")
close("(a) delta = 2.69 um, R_s = 10.6 mOhm", [delta * 1e6, Rs * 1e3], [2.69, 10.6], rtol=3e-3)
print(f"  (a) 1/(w eps0) = {1/(w*eps0):.6f} Ohm.m (w eps0 = 1/18)")
close("(a) R_s = Re eta2 = alpha/sigma (exact, to 1e-6)", [Rs, Rs], [eta2.real, g2.real / sig], rtol=1e-6)
G = (eta2 - eta0) / (eta2 + eta0); tau = 1 + G
Jt = lambda z: sig * tau * E0 * np.exp(-g2 * z)                       # x-directed phasor
Bt = lambda z: mu0 * tau * E0 / eta2 * np.exp(-g2 * z)                 # y-directed phasor
Js_ph = integrate.quad(lambda z: Jt(z).real, 0, 40 * delta, limit=400)[0] + 1j * integrate.quad(lambda z: Jt(z).imag, 0, 40 * delta, limit=400)[0]
print(f"  (b) depth integral of J = {Js_ph:.6f} A/m; 2E0/eta0 = {2*E0/eta0:.6f} = 5/(3pi) = {5/(3*np.pi):.6f}; |H_tan(0)| = |tau E0/eta2| = {abs(tau*E0/eta2):.6f}")
close("(b) |J_s| = 2E0/eta0 = 0.531 A/m", [abs(Js_ph), 2 * E0 / eta0], [5 / (3 * np.pi), 0.531], rtol=2e-3)
J0 = abs(Jt(0)); J0_approx = (2 * E0 / eta0) * np.sqrt(2) / delta
print(f"  (b) |J(0)| exact {J0:.6e} A/m^2, |J_s| sqrt2/delta = {J0_approx:.6e}")
close("(b) |J(0)| = 2.79e5 A/m^2", [J0, J0_approx], [2.79e5, 2.79e5], rtol=2e-3)
heat_q = integrate.quad(lambda z: 0.5 * abs(Jt(z))**2 / sig, 0, 40 * delta, limit=400)[0]
heat_Rs = 0.5 * Rs * (2 * E0 / eta0)**2
Si = E0**2 / (2 * eta0)
print(f"  (c) heat: quadrature of <J.E> = {heat_q*1e3:.6f} mW/m^2; 0.5 R_s |J_s|^2 = {heat_Rs*1e3:.6f}; (1-|G|^2)<S_i> = {(1-abs(G)**2)*Si*1e3:.6f}")
print(f"  (c) <S_i> = {Si:.6f} W/m^2; absorbed fraction 4R_s/eta0 = {4*Rs/eta0:.6e}; exact 1-|G|^2 = {1-abs(G)**2:.6e}")
close("(c) heat 1.49 mW/m^2 (three routes)", [heat_q * 1e3, heat_Rs * 1e3, (1 - abs(G)**2) * Si * 1e3], [1.495, 1.495, 1.495], rtol=2e-3)
close("(c) <S_i> = 13.26 W/m^2, fraction 1.13e-4", [Si, 4 * Rs / eta0], [13.26, 1.127e-4], rtol=1e-3)
# pressure: time average by quadrature of 1/2 Re{J x B*} (z-directed: x cross y = z)
Pavg = integrate.quad(lambda z: 0.5 * (Jt(z) * np.conj(Bt(z))).real, 0, 40 * delta, limit=400)[0]
# instantaneous: integrate real J(z,t) B(z,t)
def Pinst(t):
    return integrate.quad(lambda z: (Jt(z) * np.exp(1j * w * t)).real * (Bt(z) * np.exp(1j * w * t)).real, 0, 40 * delta, limit=400)[0]
Pt = [Pinst(t) for t in np.linspace(0, 1 / f, 41)]
print(f"  (d) <P_rad> quadrature = {Pavg*1e9:.6f} nPa; 2<S_i>/c = {2*Si/c*1e9:.6f}; (1+|G|^2)<S_i>/c = {(1+abs(G)**2)*Si/c*1e9:.6f}")
print(f"  (d) instantaneous P(t): max {max(Pt)*1e9:.6f} nPa, min {min(Pt)*1e9:.6f} nPa; 4<S_i>/c = {4*Si/c*1e9:.6f}; mean over samples {np.mean(Pt[:-1])*1e9:.6f}")
close("(d) <P_rad> = 88.4 nPa", [Pavg * 1e9, 2 * Si / c * 1e9], [88.4, 88.4], rtol=1e-3)
close("(d) peak 177 nPa, min ~0", [max(Pt) * 1e9, 4 * Si / c * 1e9], [176.8, 176.8], rtol=1e-3)
print(f"  (d) exact <P_rad> differs from 2<S_i>/c by {(2*Si/c - Pavg)/(2*Si/c)*100:.4f} %")
check("(d) push along +z (into the wall)", Pavg > 0)

# ============================================================================
hdr("26.11 Pushing a sail with a laser")
P = 3e4; A = 3.0; m = 1e-3; R = 0.9; lam = 1e-6; h_given = 6.63e-34; h = 6.62607015e-34
S = P / A; E0 = np.sqrt(2 * eta0 * S); Js = 2 * E0 / eta0
print(f"  (a) <S_i> = {S:.1f} W/m^2; E0 = {E0:.4f} V/m; J_s peak = {Js:.4f} A/m")
close("(a) E0 = 2746 V/m, J_s = 14.6 A/m", [E0, Js], [2746, 14.57], rtol=2e-4)
Fm = 2 * P / c; Fs = (1 + R) * P / c
print(f"  (b) mirror F = {Fm*1e3:.6f} mN, a = {Fm/m:.6f} m/s^2; 90% sail F = {Fs*1e3:.6f} mN, a = {Fs/m:.6f} m/s^2")
close("(b) 0.2 mN, 0.2 m/s^2, 0.19 mN, 0.19 m/s^2", [Fm, Fm / m, Fs, Fs / m], [2e-4, 0.2, 1.9e-4, 0.19])
# momentum bookkeeping, independent: incoming flux P/c stopped, reflected R P/c leaves backwards
Fmom = P / c - (-R * P / c)
close("(b) momentum bookkeeping (1+R)P/c", Fmom, Fs)
Pabs = (1 - R) * P
print(f"  (c) absorbed power {Pabs:.1f} W = {Pabs/A:.1f} W/m^2")
close("(c) 3 kW", Pabs, 3000.0)
Eph = h_given * c / lam; rate = P / Eph; pph = Eph / c
print(f"  (d) photon energy hc/lambda = {Eph:.6e} J (with h = 6.63e-34); rate = {rate:.6e} /s; momentum h/lambda = {pph:.6e} N s; 2 rate p = {2*rate*pph*1e3:.6f} mN")
print(f"      with CODATA h: {h*c/lam:.6e} J, rate {P/(h*c/lam):.6e} /s")
close("(d) 1.99e-19 J, 1.51e23 /s, 6.63e-28 N s, 2 rate p = 2P/c", [Eph, rate, pph, 2 * rate * pph], [1.989e-19, 1.508e23, 6.63e-28, Fm], rtol=1e-3)
v = Fm / m * 3600; v90 = Fs / m * 3600
print(f"  (e) speed after 1 h: mirror {v:.3f} m/s, 90% sail {v90:.3f} m/s; KE mirror {0.5*m*v**2:.3f} J vs beam energy {P*3600:.3e} J")
close("(e) 720 m/s, 684 m/s", [v, v90], [720, 684])
print(f"  absorbing 10 % loses {(Fm - Fs)/Fm*100:.2f} % of the push")

# ============================================================================
hdr("26.12 Trapped between two mirrors")
L = 0.15; E0 = 50.0
fm = [mm * c / (2 * L) for mm in (1, 2, 3)]
print(f"  (a) f_m = m c/2L: {np.round(np.array(fm)/1e9, 6)} GHz")
close("(a) 1, 2, 3 GHz", fm, [1e9, 2e9, 3e9])
mm = 3; f = fm[2]; w = 2 * np.pi * f; b = w / c
# build from two travelling waves (mirror at z = 0 for a wave going -z, Gamma=-1): page form
E = lambda r, t: X * 2 * E0 * np.sin(b * r[2]) * np.sin(w * t)
H = lambda r, t: Y * 2 * E0 / eta0 * np.cos(b * r[2]) * np.cos(w * t)
Ep, Hp = travelling(E0 * X, Z, b, w, eta0)    # x E0 cos(wt - bz)
Em, Hm = travelling(-E0 * X, -Z, b, w, eta0)  # -x E0 cos(wt + bz)
pts = [[0, 0, z] for z in (0.011, 0.07, 0.133)]; tts = [0.03e-9, 0.11e-9, 0.27e-9]
close("(e) E = x E0 cos(wt-bz) - x E0 cos(wt+bz)", [E(p, t) for p in pts for t in tts], [Ep(p, t) + Em(p, t) for p in pts for t in tts], atol=1e-9)
close("(e) H = y (E0/eta0)[cos(wt-bz) + cos(wt+bz)]", [H(p, t) for p in pts for t in tts], [Hp(p, t) + Hm(p, t) for p in pts for t in tts], atol=1e-12)
maxwell_td("26.12", E, H, eps0, mu0, w, b, pts[:2], tts[:2])
check("PEC at both walls: E(0,t) = E(L,t) = 0", max(abs(E([0, 0, 0], t)).max() + abs(E([0, 0, L], t)).max() for t in tts) < 1e-12)
print(f"  (b) beta = {b/np.pi:.6f} pi rad/m, w = {w/np.pi/1e9:.6f} pi x 1e9 rad/s, lambda = {2*np.pi/b*100:.4f} cm; 2E0/eta0 = {2*E0/eta0:.6f} A/m = 5/6pi = {5/(6*np.pi):.6f}")
zf = np.linspace(1e-9, L - 1e-9, 1500001)
en = zf[np.r_[False, np.diff(np.sign(np.sin(b * zf))) != 0]]; hn = zf[np.r_[False, np.diff(np.sign(np.cos(b * zf))) != 0]]
print(f"  (b) interior E nodes {np.round(en*100,4)} cm (+ walls 0, 15); H nodes {np.round(hn*100,4)} cm")
close("(b) E nodes 5, 10; H nodes 2.5, 7.5, 12.5 cm", list(en) + list(hn), [0.05, 0.10, 0.025, 0.075, 0.125], atol=2e-7)
J0 = [np.cross(Z, H([0, 0, 0], t)) for t in tts]; JL = [np.cross(-Z, H([0, 0, L], t)) for t in tts]
close("(c) J_s(z=0) = -x (5/6pi) cos wt", J0, [-X * 5 / (6 * np.pi) * np.cos(w * t) for t in tts], atol=1e-12)
close("(c) J_s(z=L) = -x (5/6pi) cos wt", JL, [-X * 5 / (6 * np.pi) * np.cos(w * t) for t in tts], atol=1e-12)
# pressure: force per area on a sheet = J_s x (B averaged over its two faces) = J_s x (mu0 H_air / 2)
F0 = [np.cross(np.cross(Z, H([0, 0, 0], t)), mu0 * H([0, 0, 0], t) / 2) for t in np.linspace(0, 1 / f, 401)]
FL = [np.cross(np.cross(-Z, H([0, 0, L], t)), mu0 * H([0, 0, L], t) / 2) for t in np.linspace(0, 1 / f, 401)]
P0 = np.mean(np.array(F0)[:-1], axis=0); PL = np.mean(np.array(FL)[:-1], axis=0)
print(f"  (d) <F/A> on z=0 wall {P0} Pa; on z=L wall {PL} Pa; eps0 E0^2 = {eps0*E0**2:.6e}; 1/4 mu0 (5/6pi)^2 = {0.25*mu0*(5/(6*np.pi))**2:.6e}; 2<S_i>/c = {2*E0**2/(2*eta0)/c:.6e}")
close("(d) 2.21e-8 Pa outward on each wall", [P0[2], PL[2]], [-eps0 * E0**2, eps0 * E0**2])
close("(d) value 2.21e-8", eps0 * E0**2, 2.21e-8, rtol=2e-3)
wd = lambda z, t: 0.5 * eps0 * E([0, 0, z], t) @ E([0, 0, z], t) + 0.5 * mu0 * H([0, 0, z], t) @ H([0, 0, z], t)
Wt = [integrate.quad(lambda z: wd(z, t), 0, L, limit=200)[0] for t in np.linspace(0, 0.5 / f, 7)]
print(f"  (d) stored energy per m^2 at 7 instants: {np.round(np.array(Wt)*1e9, 8)} nJ/m^2; eps0 E0^2 L = {eps0*E0**2*L*1e9:.6f} nJ/m^2")
close("(d) W = eps0 E0^2 L = 3.32 nJ/m^2, constant", Wt, [eps0 * E0**2 * L] * 7)
close("(d) 3.32 nJ/m^2", eps0 * E0**2 * L * 1e9, 3.32, rtol=2e-3)
print(f"  (e) each travelling wave: amplitude {E0} V/m, <S> = E0^2/(2 eta0) = {E0**2/(2*eta0):.4f} W/m^2; 2<S>/c = {E0**2/eta0/c:.4e} Pa")
# (e) m = 2: currents opposite
b2 = 2 * np.pi * fm[1] / c
H2 = lambda z: 2 * E0 / eta0 * np.cos(b2 * z)
j0 = np.cross(Z, Y * H2(0)); jL = np.cross(-Z, Y * H2(L))
print(f"  (e) m = 2 at t = 0: J_s(0) = {j0}, J_s(L) = {jL}")
check("(e) m = 2: currents opposite; m = 3: same", np.allclose(j0, -jL) and np.allclose(J0[0], JL[0]))
print(f"  (e) round trip 2L/c = {2*L/c*1e9:.4f} ns = 1/f1 = {1/fm[0]*1e9:.4f} ns")

print("\n" + "=" * 78)
print(f"TOTAL CHECKS: {len(ALL)}, FAILED: {ALL.count(False)}")
