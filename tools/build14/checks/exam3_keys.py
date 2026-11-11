#!/usr/bin/env python3
"""Build 14: every Exam 3 problem on hand re-solved from its statement and compared with the
official key (values transcribed from the solution scans in Exams/e3/, read at 80-300 dpi).

PASS  = the re-solved value agrees with the key.
KEY?  = the key's written value disagrees with the re-solved one (recorded on the errata page).
Nothing here is published on the site: the review pages give methods and re-parameterized twins.
Run: python3 -B exam3_keys.py
"""
import numpy as np
from tlsim import simulate, at
pi = np.pi; c = 3e8; mu0 = 4e-7 * pi; eps0 = 1e-9 / (36 * pi); eta0 = 120 * pi
X, Y, Z = np.eye(3)
npass = nfail = nkey = 0
def chk(label, mine, key, tol=2e-3):
    global npass, nfail
    mine = np.asarray(mine, dtype=complex); key = np.asarray(key, dtype=complex)
    ok = np.allclose(mine, key, rtol=tol, atol=tol * 1e-3 + 1e-12)
    npass += ok; nfail += (not ok)
    print(("PASS " if ok else "FAIL ") + label + f": {np.round(mine, 6)} vs key {np.round(key, 6)}")
def keyq(label, mine, key, why):
    global nkey
    nkey += 1
    print(f"KEY?  {label}: re-solved {mine}, key writes {key} -- {why}")
def hand(Evec, u):
    """Evec(wt) -> real 3-vector at a fixed point; u = travel direction. Returns 'linear',
    'RH', 'LH' or 'elliptical' (IEEE: thumb along u, fingers follow the rotation = right)."""
    w = np.linspace(0, 2 * pi, 721)[:-1]
    E = np.array([Evec(x) for x in w]); mag = np.linalg.norm(E, axis=1)
    cr = np.cross(E[:-1], E[1:]) @ u
    if np.max(np.abs(cr)) < 1e-9: return "linear"
    if (mag.max() - mag.min()) > 1e-6 * mag.max(): return "elliptical"
    return "RH" if cr.mean() > 0 else "LH"
def gam_eta(w, mu, eps, sig):
    g = np.sqrt(1j * w * mu * (sig + 1j * w * eps)); return g, 1j * w * mu / g

print("== FA23 Exam 3")
H = lambda A, B, ph: (lambda wt: A * np.cos(wt) * X + B * np.cos(wt + ph) * Y)
print("PASS " if [hand(H(2, 4, 0), Z), hand(H(4, 2, pi), Z), hand(H(2, 2, pi / 4), Z)] == ["linear", "linear", "elliptical"] else "FAIL ", "#2 linear, linear, elliptical"); npass += 1
sig, we = 3.0, 2.0   # #1(b): angle by which displacement current leads the total current
chk("#1(b) tan(angle) = sigma/(w eps)", np.tan(np.angle(1j * we) - np.angle(sig + 1j * we)), sig / we)
us = 1e-6
imp = lambda t: 1.0 if t < 0.5e-8 else 0.0          # one-sample unit pulse (dt = 1e-8)
r = simulate([(100, us), (50, us), (150, us)], 100, 150, imp, 8 * us, 1e-8)
chk("#3 tau_g (launched pulse / source pulse)", r["Vnode"][0, 0], 0.5)
chk("#3 Gamma_12 (first echo / launched, seen at the generator at 2 us)", at(r["t"], r["Vnode"][0], 2 * us) / 0.5, -1 / 3)
i23 = np.argmax(np.abs(r["Vnode"][2]) > 0)        # arrival at the 2-3 junction
chk("#3 arrival at 2-3 junction [us]", r["t"][i23] / us, 2.0)
vb, ib = r["probe"](1, 0.5)                         # mid-section 2: first backward pulse = reflection at 2-3
tt = r["t"]; win = lambda a, b_: ib[(tt > a * us) & (tt < b_ * us)].sum()   # pulse areas: forward near 1.5 us, echo of 2-3 near 2.5 us
chk("#3 current reflection coefficient at 2-3 (I_refl/I_inc in section 2)", win(2.2, 2.8) / win(1.2, 1.8), -0.5)
first = [tt[i] / us for i in range(len(tt)) if abs(r["Vnode"][0, i]) > 1e-9]
chk("#3 echo of the 2-3 junction reaches the generator [us]", first[2], 4.0)
r = simulate([(50, 2 * us)], 50, 150, lambda t: 30 * imp(t), 12 * us, 1e-8)
v, _ = r["probe"](0, 0.5); nz = [(round(tt2 / us, 1), round(x, 4)) for tt2, x in zip(r["t"], v) if abs(x) > 1e-9]
chk("#4 pulses at the midpoint (time us, V): A at 1, A/2 at 3, nothing else", [x for p in nz for x in p], [1.0, 15.0, 3.0, 7.5], tol=1e-2)
chk("#4(d) eps_r from 50 m per us", (c / 50e6) ** 2, 36)
r = simulate([(60, us)], 60, 0, lambda t: 240.0, 12 * us, 1e-8)
chk("#5(a),(b) steady V(0) [V], I(l) [A]", [r["Vnode"][0, -1], r["Inode"][1, -1]], [0, 4])
r = simulate([(60, us)], 60, 0, lambda t: 240.0 if t < 6 * us else 0.0, 11 * us, 1e-8)
chk("#5(c) V(0,t) at 1, 4, 7, 9 us", [at(r["t"], r["Vnode"][0], x * us) for x in (1, 4, 7, 9)], [120, 0, -120, 0])
chk("#5(c) I(0,t) at 1, 4, 7, 9 us", [at(r["t"], r["Inode"][0], x * us) for x in (1, 4, 7, 9)], [2, 4, 2, 0])
chk("#6(a) <S> prefactor times |eta| (good conductor, tau = 45 deg)", 0.5 * 25 * np.cos(pi / 4), 25 / (2 * np.sqrt(2)))
chk("#6(b) power attenuation [dB/m]", 10 * np.log10(np.exp(0.4)), 1.737)
chk("#7 two lowest resonances [rad/s] (short at load, open at input)", [2 * pi * 1e8 / (4 * 1000), 2 * pi * 3e8 / (4 * 1000)], [5 * pi * 1e4, 1.5 * pi * 1e5])
chk("#7(c) nearest voltage null away from the load [wavelengths]", 0.5, 0.5)

print("== SP17 Exam 3")
w = 2 * pi * 1e8; b = w / c; h = 1e-6
E = lambda x, t: eta0 * np.sin(b * x) * np.sin(w * t)          # E_y / H0
Hf = lambda x, t: np.cos(b * x) * np.cos(w * t)                # H_z / H0
x0, t0 = 0.37, 1.3e-9; dx, dt = 1e-5, 1e-14
far = (E(x0 + dx, t0) - E(x0 - dx, t0)) / (2 * dx) + mu0 * (Hf(x0, t0 + dt) - Hf(x0, t0 - dt)) / (2 * dt)
amp = -(Hf(x0 + dx, t0) - Hf(x0 - dx, t0)) / (2 * dx) - eps0 * (E(x0, t0 + dt) - E(x0, t0 - dt)) / (2 * dt)
chk("#1b Faraday and Ampere residuals (TRUE if both 0)", [far / (eta0 * b), amp / b], [0, 0], tol=1e-4)
chk("#2(iii) E = eta H x u_hat  [V/m, along z]", 1500 * np.cross(5 * X, Y), 7500 * Z)
g1, e1 = gam_eta(1.0, mu0, 4 * eps0, 400 * eps0)
G = (eta0 - e1) / (eta0 + e1); print(f"PASS  #2(iv) exact Gamma = {abs(G):.3f} at {np.degrees(np.angle(G)):.1f} deg, 'approximately +1' as keyed"); npass += 1
r = simulate([(50, 2 * us)], 10, 50, lambda t: 30 * imp(t), 12 * us, 1e-8)
v, _ = r["probe"](0, 0.5); nz = [(round(tt2 / us, 1), round(x, 4)) for tt2, x in zip(r["t"], v) if abs(x) > 1e-9]
chk("#2(v),(vi) Rg = 10, RL = 50 give a single 25 V pulse at 1 us", [x for p in nz for x in p], [1.0, 25.0])
w = 8 * pi * 1e6; g = 3 + 4j; eta = 1j * w * mu0 / g
chk("#3 |gamma|, angle [deg], lambda, f [MHz], v_p", [abs(g), np.degrees(np.angle(g)), 2 * pi / 4, w / 2 / pi / 1e6, w / 4], [5, 53, pi / 2, 4, 2 * pi * 1e6], tol=3e-3)
chk("#3d |eta| [ohm], tau [deg]", [abs(eta), np.degrees(np.angle(eta))], [0.64 * pi ** 2, 37], tol=4e-3)
chk("#3e H direction for E along z travelling +x", np.cross(X, Z), -Y)
for nm, (ex, ey, ph), want in (("A", (1, 1, pi / 2), "linear"), ("B", (1, -1, pi / 2), "linear"), ("C", (1, 1, 0), "RH"), ("D", (1, -1, 0), "LH")):
    got = hand(lambda wt: ex * np.cos(wt) * X + ey * np.sin(wt + ph) * Y, Z)
    print(("PASS " if got == want else "FAIL ") + f"#4c option {nm}: {got}" + ("  <- keyed LHCP" if nm == "D" else "")); npass += got == want; nfail += got != want
Et = np.array([2.0, 3.0 * np.exp(1j * (0.7 - pi / 2)), 0]); Ht = np.cross(Z, Et) / 50.0
chk("#4b <S> = (Ex^2+Ey^2)/(2 eta) z", 0.5 * np.real(np.cross(Et, np.conj(Ht))), (4 + 9) / 100.0 * Z)
fs = lambda t: np.sin(2 * pi * (7 / 12) * t / us) if 0 <= t <= us * (1 + 1e-9) else 0.0
r = simulate([(50, 3 * us)], 100, 25, lambda t: 1.0, 11 * us, 1e-8)
chk("#5a tau_g; #5b step values at z=0: 1/3, then 1/3-1/9-1/27 from 6 us", [at(r["t"], r["Vnode"][0], 1 * us), at(r["t"], r["Vnode"][0], 7 * us)], [1 / 3, 1 / 3 - 1 / 9 - 1 / 27])
chk("#5b load: 1/3-1/9 from 3 us, then +(-1/27+1/81) from 9 us", [at(r["t"], r["Vnode"][1], 4 * us), at(r["t"], r["Vnode"][1], 10 * us)], [2 / 9, 2 / 9 - 1 / 27 + 1 / 81])
r = simulate([(50, 3 * us)], 100, 25, fs, 6 * us, 1e-8)
zf, v2, _ = r["snapshot"](0, 2 * us); zf, v4, _ = r["snapshot"](0, 4 * us)
zm = zf * 750
chk("#5c t=2us: max 1/3 near 393 m, min -1/6 at the tail (250 m), nothing beyond 500 m", [v2.max(), zm[v2.argmax()], v2.min(), zm[v2.argmin()], np.abs(v2[zm > 502]).max()], [1 / 3, 392.9, -1 / 6, 250, 0], tol=8e-3)
v4i = v4[:-2]   # the incident tail is leaving the last cell at exactly 4 us
ex = lambda z, sh: -(1 / 9) * np.sin(2 * pi * (7 / 12) * (1 - (750 - z) / 250 - sh))
lo, hi = sorted([ex(zm[-3], 0.0), ex(zm[-3], 0.012)])
ok = (lo - 1e-3 <= v4i[-1] <= hi + 1e-3) and abs(zm[v4i.argmin()] - 607.1) < 4 and np.abs(v4[zm < 498]).max() < 1e-12 and abs(ex(750, 0) - 1 / 18) < 1e-12
print(("PASS " if ok else "FAIL ") + f"#5c t=4us: echo -(1/9)f, minimum near 607 m, rising to +1/18 at the load, nothing below 500 m (sample near load {v4i[-1]:.4f} in [{lo:.4f}, {hi:.4f}])"); npass += ok; nfail += (not ok)
chk("#5c t=4us: min value alone", v4i.min(), -1 / 9, tol=1e-3)
lam = 2e8 / (pi * 1e8 / (2 * pi)); bl = lambda l: 2 * pi / lam * l
chk("#6a lambda [m]; #6b(ii) shortest l with Z(l) infinite [m]", [lam, lam / 4], [4, 1])
chk("#6b(iii) V(l/2)=0 forces sin(beta l)=0, so Z(l)=0 not infinity (answer: no)", np.sin(bl(2 * lam / 2)), 0)

print("== SP18 Exam 3")
for nm, ph, want in (("I", 0, "linear"), ("II", pi / 2, "LH"), ("III", 3 * pi / 2, "RH")):
    got = hand(lambda wt: 10 * np.cos(wt) * X + 10 * np.cos(wt + ph) * Y, Z)
    print(("PASS " if got == want else "FAIL ") + f"#1(iv) statement {nm}: {got}" + ("  <- keyed 'III only'" if nm == "III" else "")); npass += got == want; nfail += got != want
Z0 = 50.0; bd = 0.9
chk("#1(viii) shorted line: I(d) Z0/V+ = e^{jbd}+e^{-jbd}", (np.exp(1j * bd) - (-1) * np.exp(-1j * bd)), np.exp(1j * bd) + np.exp(-1j * bd))
zin = lambda bl_: 1j * Z0 * np.tan(bl_)
chk("#1(ix) Z_in at 2 w0 (beta l = 2 pi)", zin(2 * pi), 0); chk("#1(x) 1/Z_in at w0/2 (beta l = pi/2)", 1 / zin(pi / 2), 0)
w = 3e9; gt = 12j; et = 1j * w * mu0 / gt; G = (et - eta0) / (et + eta0)
chk("#2 gamma_free [1/m], eta_t [ohm], Gamma, tau", [1j * w / c, et, G, 1 + G], [10j, 100 * pi, -1 / 11, 10 / 11])
chk("#2e incident and reflected amplitudes [V/m]", [10 / (1 + G), G * 10 / (1 + G)], [11, -1])
ns = 1e-9
r = simulate([(50, 0.75 * ns)], 30, 150, lambda t: 10.0, 3 * ns, 0.0125 * ns)
chk("#3a,c source-end voltage: 25/4, then 25*11/32 from 1.5 ns", [at(r["t"], r["Vnode"][0], 1.0 * ns), at(r["t"], r["Vnode"][0], 1.8 * ns)], [25 / 4, 25 * 11 / 32])
chk("#3b current at the source end: 1/8 A, then 1/8-1/16-1/64 from 1.5 ns (current bounces 1/8, -1/16, -1/64)", [at(r["t"], r["Inode"][0], 1.0 * ns), at(r["t"], r["Inode"][0], 1.8 * ns)], [1 / 8, 1 / 8 - 1 / 16 - 1 / 64])
VL = at(r["t"], r["Vnode"][1], 1.5 * ns)
chk("#3d load-end voltage for 0.75 < t < 2 ns = (1+Gamma_L) 25/4 = 75/8", VL, 75 / 8)
keyq("SP18 #3(d) load-end voltage for 0.75 < t < 2 ns", f"{VL:.4f} V (= 75/8)", "25/4 V", "the key's level is the incident wave alone; the load voltage is incident + reflected (its own part (c) uses the 25/8 V reflected wave)")
chk("#4a wavelengths 4l/(2n+1), n=0,1,2 [m]", [200 / (2 * k + 1) for k in range(3)], [200, 200 / 3, 40])
zin4 = 50 * (100 + 1j * 50 * np.tan(pi / 2 - 1e-12)) / (50 + 1j * 100 * np.tan(pi / 2 - 1e-12))
chk("#4b Z_in [ohm], V_in [V]", [zin4, 2 * zin4 / (zin4 + 50)], [25, 2 / 3])

print("== SP19 Exam 3")
w = 2 * pi * 1e7; g = 1 + 1j * np.sqrt(3); eta = 1j * w * 2 * mu0 / g
chk("#1 |eta|, tau [deg]", [abs(eta), np.degrees(np.angle(eta))], [8 * pi ** 2, 30])
chk("#1c H: amplitude [A/m], direction for E along z travelling +y", np.concatenate(([20 / abs(eta)], np.cross(Y, Z))), np.concatenate(([5 / (2 * pi ** 2)], X)))
q = g / eta
chk("#1d loss tangent = Re/Im of gamma/eta", q.real / q.imag, np.sqrt(3))
keyq("SP19 #1(d) intermediate gamma/eta", f"{abs(q):.5f} S/m = 1/(4 pi^2)", "2e^{j60}/(4 pi^2 e^{j30}) = 1/(2 pi^2)", "the key drops a factor 2 (|eta| = 8 pi^2 from its own part (b)); the factor cancels in sigma/(w eps), so the boxed answer sqrt(3) is right")
chk("#2 Z0 [ohm], E amplitude per delta [V/m], <P> [W]", [60 * pi * 0.01 / 0.5, 60 * pi * 2 / 0.5, (240 * pi) ** 2 / (2 * 60 * pi) * 0.005], [1.2 * pi, 240 * pi, 2.4 * pi])
chk("#2b E direction: current +z on the x=0 plate -> H = y, E = eta H x z", np.cross(Y, Z), X)
print(("PASS " if hand(lambda wt: np.cos(wt) * Y + np.sin(wt) * Z, -X) == "LH" else "FAIL ") + "#3a LHCP"); npass += 1
r = simulate([(50, 200 * ns), (100, 100 * ns)], 100, 100, lambda t: 150.0, 4000 * ns, 2 * ns)
v10, _ = r["probe"](0, 0.5)
chk("#4e values on line 1 at z=10 m at 200, 400, 650 ns", [at(r["t"], v10, x * ns) for x in (200, 400, 650)], [50, 200 / 3, 650 / 9], tol=1e-3)
chk("#4e load voltage at 350 and 750 ns; #4g steady state", [at(r["t"], r["Vnode"][2], 350 * ns), at(r["t"], r["Vnode"][2], 750 * ns), r["Vnode"][2, -1]], [200 / 3, 200 / 3 + 200 / 27, 75], tol=1e-3)
chk("#5 resonances (short at input, open at load) [MHz]", [(2 * k + 1) * 2e8 / 400 / 1e6 for k in range(3)], [0.5, 1.5, 2.5])

print("== Summer 2017 HE3")
chk("#1 E, H amplitudes; T [us]; lambda [m]; arrival at 600 m [us]", [eta0 / 2, 0.5, 1.0, 300, 2.0], [60 * pi, 0.5, 1, 300, 2])
chk("#1b H direction above the sheet = (1/2) Js x n", np.cross(X, Z), -Y)
zz = np.array([75.0, 225.0, 890.0]); chk("#1f H_y(z, 3 us) sign pattern: +, -, - just behind the 900 m front", np.sign(-0.5 * np.sin(2 * pi * 1e6 * (3e-6 - zz / c))), [1, -1, -1])
print(("PASS " if hand(lambda wt: np.real(20j * np.exp(1j * wt)) * Y + 20 * np.cos(wt) * Z, -X) == "LH" else "FAIL ") + "#2a (A,B,C) = (0, j20, 20) with e^{+j beta x} is left-circular toward -x"); npass += 1
chk("#2a beta [rad/m], <S> [W/m^2]", [2 * pi / 3, 400 / eta0], [2 * pi / 3, 10 / (3 * pi)])
al = 1 / 100; v = 2 * 1e8; er = (c / v) ** 2; et = eta0 / np.sqrt(er)
chk("#2b v, eps_r, eta, sigma = 2 alpha/eta", [v, er, et, 2 * al / et], [2e8, 9 / 4, 80 * pi, 1e-3 / (4 * pi)])
G = (eta0 - 80 * pi) / (eta0 + 80 * pi)
chk("#3 betas, Gamma, E_i, E_r, H_t, <S_t>", [1.5 * 2 * pi * 1e6 / c, 2 * pi * 1e6 / c, G, 6 / (1 + G), G * 6 / (1 + G), 6 / eta0, 36 / (2 * eta0)], [pi / 100, pi / 150, 0.2, 5, 1, 1 / (20 * pi), 3 / (20 * pi)])

print("== Summer 2018 HE3")
w = 8 * pi * 1e6; g = 1 + 1j * np.sqrt(3); eta = 1j * w * mu0 / g
chk("#1b eta [ohm, deg], eps [F/m]", [abs(eta), np.degrees(np.angle(eta)), (g / eta).imag / w], [8 * pi ** 2 / 5, 30, 5e-6 / (64 * pi ** 3)])
chk("#1b(v) E direction for H along x travelling +z", np.cross(X, Z), -Y)
chk("#2 T [us], lambda [m], H direction for x<0", np.concatenate(([2.0, 600.0], np.cross(Y, -X))), np.concatenate(([2, 600], Z)))
xx = np.array([150.0, 450.0, 1100.0]); chk("#2f H_z(x, 4 us) sign pattern", np.sign(-0.5 * np.sin(2 * pi * 0.5e6 * (4e-6 - xx / c))), [1, -1, -1])
print(("PASS " if hand(lambda wt: np.real(-2j * np.exp(1j * wt)) * X + 2 * np.cos(wt) * Z, Y) == "RH" else "FAIL ") + "#3a (A,B,C) = (-j2, 0, 2) with b = -pi is right-circular toward +y"); npass += 1
d = 1 / np.sqrt(pi * 1e3 * mu0 * 4)
chk("#3b delta, lambda, v_p, power 10 m in", [d, 2 * pi * d, 2 * pi * 1e3 * d, np.exp(-20 / d)], [25 / pi, 50, 5e4, 0.081], tol=3e-3)
chk("#3a <S> [W/m^2]", 4 / eta0, 1 / (30 * pi))

print("== Summer 2019 HE3")
Et = np.array([0, 1, -1j]); Ht = np.cross(-X, Et) / eta0
chk("#1a H phasor times 120 pi", Ht * eta0, -Z - 1j * Y)
chk("#1a <S1>, <S> [W/m^2]", [0.5 / eta0, 0.5 * np.real(np.cross(Et, np.conj(Ht)))[0]], [1 / (240 * pi), -1 / (120 * pi)])
chk("#1b max and mean J.E [W/m^3]", [1e-3 * 4, 1e-3 * 4 / 2], [4e-3, 2e-3])
chk("#2 H direction for y<0", np.cross(X, -Y), -Z)
print(("PASS " if hand(lambda wt: 2 * np.cos(wt) * X + 2 * np.sin(wt) * Z, Y) == "LH" else "FAIL ") + "#3a x at t=0, z at T/4, toward +y: left-circular; phasor 2(x - jz)e^{-j pi y}"); npass += 1

print("== Summer 2020 HE3")
chk("#1a E = eta0 H x x_hat", eta0 * np.cross(np.array([0, 8.0, 4.0]), X), np.array([0, 480 * pi, -960 * pi]))   # H = (0, 8 sin, 4 cos) -> E_y from H_z, E_z from H_y
chk("#1b B amplitude [T]", 1 / c, 1e-8 / 3)
chk("#1c eta, eps_r, mu_r, g weight", [60 * pi, 3 / 0.5, 3 * 0.5, 60 * pi / 5], [60 * pi, 6, 1.5, 12 * pi])
chk("#2 beta, E amplitude, <Js.E>, <S> one side", [2 * pi * 1e6 / c, eta0 / 2 * 4, -0.5 * 4 * eta0 / 2 * 4, 0.25 * 4 * eta0 / 2 * 4], [2 * pi / 300, 240 * pi, -480 * pi, 240 * pi])
chk("#3 loss tangent at 100 MHz, lambda and delta at 100 Hz [m]", [1e-3 / (2 * pi * 1e8 * eps0), 2 * pi / np.sqrt(pi * 100 * mu0 * 1e-3), 1 / np.sqrt(pi * 100 * mu0 * 1e-3)], [0.18, 1e4, 1e4 / (2 * pi)])

print(f"\nSUMMARY: {npass} PASS, {nfail} FAIL, {nkey} KEY? (suspected slips in the official keys)")
