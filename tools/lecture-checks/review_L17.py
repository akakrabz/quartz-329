#!/usr/bin/env python3
"""Reviewer's independent checks for Lecture 17 (magnetization, Maxwell in matter).
numpy only.  Writes review_L17.out next to this file.
Screen frame for figure directions: X right, Y up, Z out of the screen (odot = +Z)."""
import math, os
import numpy as np
from numpy import pi, cross, dot

OUT = []
def P(*a):
    s = " ".join(str(v) for v in a); OUT.append(s); print(s)
NFAIL = 0
def ok(c, label):
    global NFAIL
    if not c: NFAIL += 1
    P(("OK    " if c else "FAIL  ") + label)

mu0 = 4e-7 * pi
e, kB, muB, NA = 1.602176634e-19, 1.380649e-23, 9.2740100783e-24, 6.02214076e23
X, Y, Z = np.eye(3)
close = lambda a, b, r=1e-6: np.allclose(a, b, rtol=r, atol=r)

def curl_fd(Mf, r, h=1e-6):
    J = np.zeros((3, 3))
    for j in range(3):
        d = np.zeros(3); d[j] = h
        J[:, j] = (Mf(r + d) - Mf(r - d)) / (2 * h)
    return np.array([J[2, 1] - J[1, 2], J[0, 2] - J[2, 0], J[1, 0] - J[0, 1]])

def div_fd(Pf, r, h=1e-6):
    s = 0.0
    for j in range(3):
        d = np.zeros(3); d[j] = h
        s += (Pf(r + d)[j] - Pf(r - d)[j]) / (2 * h)
    return s

P("== A. curls of every M on the pages (finite differences)")
Mz = lambda r: np.array([0, 0, 3 * math.sin(2 * r[0])])            # M = Mz(x) z
r0 = np.array([0.3, -0.2, 0.7])
ok(close(curl_fd(Mz, r0), [0, -6 * math.cos(0.6), 0], 1e-5), "M=Mz(x) z: curl M = -dMz/dx y  (page S3)")
M0, d = 5.0, 0.2
Mg = lambda r: np.array([0, 0, M0 * r[0] / d])
ok(close(curl_fd(Mg, r0), [0, -M0 / d, 0], 1e-5), "graded M0(x/d) z: curl = -(M0/d) y  (concept magnetization)")
ok(close(curl_fd(lambda r: np.array([9.9, 0, 0]), r0), [0, 0, 0]), "uniform slab M: curl M = 0 inside")
# A3 discrete lattice of loops (cells side s in the xy plane, CCW seen from +z, I_i = M(x_i) s)
s, L = 1e-3, 0.05
Mx = lambda x: 2.0 * (1 + 0.3 * math.sin(x / L))
xs = np.arange(0, 0.2, s)
Iy = [(Mx(xi) * s - Mx(xi + s) * s) / s**2 for xi in xs]      # right edge of left cell (+y) minus left edge of right cell
exact = [-2.0 * 0.3 * math.cos((xi + s / 2) / L) / L for xi in xs]
ok(np.max(np.abs(np.array(Iy) - exact)) < 1e-3 * np.max(np.abs(exact)), "loop lattice: leftover shared-edge current density = -dM/dx along +y")
# A4 thin surface layer: integral of curl M across the layer = M x n (n outward), twin of P.n
def layer_integral(Min, n, rs, w=1e-2):
    n = n / np.linalg.norm(n)
    Mf = lambda r: Min * 0.5 * (1 - math.tanh(dot(r - rs, n) / w))
    Pf = Mf
    ts = np.linspace(-20 * w, 20 * w, 4001)
    cu = np.array([curl_fd(Mf, rs + t * n, 1e-6) for t in ts])
    dv = np.array([-div_fd(Pf, rs + t * n, 1e-6) for t in ts])
    return np.trapezoid(cu, ts, axis=0) if hasattr(np, "trapezoid") else np.trapz(cu, ts, axis=0), \
           (np.trapezoid(dv, ts) if hasattr(np, "trapezoid") else np.trapz(dv, ts))
Mslab = np.array([9.9, 0, 0])
top, sig = layer_integral(Mslab, Z, np.zeros(3))
ok(close(top, [0, -9.9, 0], 1e-4), f"slab top face: int curl M dn = {np.round(top, 4)} = M x z = -9.9 y")
bot, _ = layer_integral(Mslab, -Z, np.zeros(3))
ok(close(bot, [0, 9.9, 0], 1e-4), f"slab bottom face: {np.round(bot, 4)} = +9.9 y")
Pv = np.array([1.0, 2.0, 3.0]); _, sb = layer_integral(Pv, Z, np.zeros(3))
ok(abs(sb - 3.0) < 1e-4, f"twin: int(-div P)dn = {sb:.5f} = P.n (rho_sb)")
phi, a = 0.7, 1.0
rs = np.array([a * math.cos(phi), a * math.sin(phi), 0])
rod, _ = layer_integral(np.array([0, 0, 2.0]), rs.copy(), rs)
ok(close(rod, 2.0 * np.array([-math.sin(phi), math.cos(phi), 0]), 1e-4), "rod M z, side n = r: M x r = M phi (solenoid sense)")
ok(close(cross(Z, Z), 0 * Z) and close(cross(Z, -Z), 0 * Z), "rod end faces: M x (+-z) = 0")
# interface: M2 below (z<0) -> M1 above, smooth step; total = n x (M1 - M2), n = +z from 2 into 1
M1, M2 = np.array([4., -3, -9]), np.array([20., -15, -15])
w = 1e-2
Mi = lambda r: M2 + (M1 - M2) * 0.5 * (1 + math.tanh(r[2] / w))
ts = np.linspace(-0.2, 0.2, 4001)
cu = np.array([curl_fd(Mi, np.array([0, 0, t])) for t in ts])
tot = np.trapezoid(cu, ts, axis=0) if hasattr(np, "trapezoid") else np.trapz(cu, ts, axis=0)
ok(close(tot, cross(Z, M1 - M2), 1e-4) and close(tot, [-12, -16, 0], 1e-4), f"interface: int curl M dz = {np.round(tot, 3)} = n x (M1-M2) = (-12,-16,0)")
ok(close(cross(M2, Z) + cross(M1, -Z), cross(Z, M1 - M2)), "two faces: M2 x n + M1 x (-n) = n x (M1-M2)")
ok(close(cross(M2, Z), [-15, -20, 0]) and close(cross(M1, -Z), [3, 4, 0]), "problem (e) faces: (-15,-20) and (+3,+4)")
ok(close(cross(M2, Z) + cross(M1, Z), [-18, -24, 0]), "problem trap: same normal for both faces gives (-18,-24)")

P("== B. torque on loops (np.cross, discretised)")
def loop_FT(verts, I, B, nseg=400):
    F = np.zeros(3); T = np.zeros(3); m = np.zeros(3)
    for k in range(len(verts)):
        A_, B_ = verts[k], verts[(k + 1) % len(verts)]
        for t in (np.arange(nseg) + 0.5) / nseg:
            r = A_ + t * (B_ - A_); dl = (B_ - A_) / nseg
            dF = I * cross(dl, B); F += dF; T += cross(r, dF); m += 0.5 * I * cross(r, dl)
    return F, T, m
th, l, I, B0 = math.radians(35), 0.3, 2.0, 0.7
u = np.array([0, math.cos(th), -math.sin(th)])
ok(close(cross(X, u), [0, math.sin(th), math.cos(th)]), "square loop: x cross u = m_hat = (0, sin, cos)")
verts = [(-l/2) * X + (-l/2) * u, (l/2) * X + (-l/2) * u, (l/2) * X + (l/2) * u, (-l/2) * X + (l/2) * u]   # +x side at -l/2 u
F, T, m = loop_FT(verts, I, B0 * Z)
ok(close(m, I * l * l * np.array([0, math.sin(th), math.cos(th)]), 1e-6), "discretised m = I l^2 (0, sin, cos)")
ok(close(F, 0 * X, 1e-9), "net force zero in uniform B")
ok(close(T, cross(m, B0 * Z), 1e-6) and close(T, I * l * l * B0 * math.sin(th) * X, 1e-6), "torque = m x B = I l^2 B sin(theta) x")
ok(close(I * l * cross(X, B0 * Z), -I * l * B0 * Y) and close(cross(u, Y), math.sin(th) * X), "F(+x side) = -IlB y ; u x y = sin(theta) x")
ok(close(I * l * cross(u, B0 * Z), I * l * B0 * math.cos(th) * X), "u-sides: forces +-IlB cos(theta) x, along their own position line (no torque)")
Rx = lambda a_: np.array([[1, 0, 0], [0, math.cos(a_), -math.sin(a_)], [0, math.sin(a_), math.cos(a_)]])
mh = m / np.linalg.norm(m); ok(dot(Rx(1e-3) @ mh, Z) > dot(mh, Z), "rotation about +T turns m toward B")
# circular tilted loop
circ = [0.2 * (math.cos(t) * X + math.sin(t) * u) for t in np.linspace(0, 2 * pi, 361)[:-1]]
F2, T2, m2 = loop_FT(circ, I, B0 * Z, 4)
ok(close(T2, cross(m2, B0 * Z), 1e-6) and close(np.linalg.norm(F2), 0, 1e-9), "circular tilted loop: T = m x B, F = 0")

P("== C. atomic numbers")
a0, v = 5.29e-11, 2.19e6
Ib = e * v / (2 * pi * a0); mb = Ib * pi * a0**2
P(f"   Bohr loop I = {Ib*1e3:.3f} mA ; area = {pi*a0**2:.3e} m^2 ; m = {mb:.4e} (e v a0/2 = {e*v*a0/2:.4e}) ; muB = {muB:.4e}")
ok(abs(Ib - 1.05e-3) < 0.006e-3 and abs(mb - 9.27e-24) < 0.01e-24, "Bohr: I = 1.05 mA, m = 9.27e-24 A m^2 = muB")
# direction: electron CW seen from +z (at (0,-a) moving -x) -> current CCW -> m +z ; L_e along -z
ok(close(cross(np.array([0, -1, 0]), np.array([-1, 0, 0])), [0, 0, -1]), "electron at -y moving -x: L along -z ; current +x there -> CCW -> m +z (antiparallel)")
Nfe = 7874 / 55.845e-3 * NA; Mfe = Nfe * 2.2 * muB
P(f"   iron N = {Nfe:.3e} /m^3, M_sat = {Mfe:.3e} A/m, mu0 M = {mu0*Mfe:.3f} T")
ok(abs(Nfe - 8.5e28) / 8.5e28 < 0.01 and abs(Mfe - 1.7e6) / 1.7e6 < 0.03 and abs(mu0 * Mfe - 2.2) < 0.05, "iron saturation numbers")
Mpm = 1.3 / mu0; ok(abs(Mpm - 1.0e6) / 1e6 < 0.05, f"permanent magnet M = {Mpm:.4e} A/m ~ 1000 turns/m x 1000 A")
ncu = 8960 / 63.546e-3 * NA * 29
ok(abs(ncu * 1e-9 - 2.5e21) / 2.5e21 < 0.03, f"copper electrons: {ncu:.3e} /m^3, {ncu*1e-9:.3e} per mm^3")
r_th = kB * 300 / (muB * 1.0); P(f"   kT(300 K) = {kB*300:.3e} J ; muB*1T = {muB:.3e} J ; ratio {r_th:.0f}")
ok(400 < r_th < 470, "thermal: muB B is ~1/450 of kT")

P("== D. solenoid / core / inductance / demagnetization")
n, I0, chi = 1000, 2.0, 99
H = n * I0; B0v = mu0 * H; Mc = chi * H; Bc = mu0 * (H + Mc)
P(f"   H = {H} A/m ; B0 = {B0v*1e3:.3f} mT ; M = {Mc:.3e} ; mu0 M = {mu0*Mc:.4f} T ; B_core = {Bc:.4f} T ; ratio {Bc/B0v:.1f}")
ok(abs(B0v - 2.51e-3) < 0.01e-3 and abs(mu0 * Mc - 0.249) < 0.001 and abs(Bc - 0.251) < 0.001, "coil-with-core numbers")
ok(abs(mu0 * 5000 * H - 12.6) < 0.05, f"iron mu_r 5000 linear: {mu0*5000*H:.2f} T")
L0 = n**2 * mu0 * 1e-4 * 0.1; ok(abs(L0 - 12.6e-6) < 0.05e-6 and abs(100 * L0 - 1.26e-3) < 0.005e-3, f"L air = {L0*1e6:.2f} uH, x100 = {100*L0*1e3:.3f} mH")
for mur in (100, 5000, 1e9, 0.99999):
    Hin = 3 / (mur + 2); Ms = (mur - 1) * Hin
    ok(abs(Hin - (1 - Ms / 3)) < 1e-12, f"sphere mu_r={mur:g}: H_in = H0 - M/3 = 3H0/(mu_r+2) = {Hin:.6g} H0 ; B_in/(mu0 H0) = {mur*Hin:.6g}")
P("   -> H_in < H0 only for chi_m > 0; a diamagnetic sphere has H_in slightly > H0 (page trap says 'smaller' unconditionally)")
Lr, ar = 20.0, 1.0
ok(abs(Lr / 2 / math.hypot(Lr / 2, ar) - 1) < 0.01, f"long rod L/a=20: B_centre/(mu0 M) = {Lr/2/math.hypot(Lr/2, ar):.4f}")
Al, Il, dx, dy, dz = 2.3e-3, 0.7, 0.11, 0.13, 0.05
ok(abs((Al / (dx * dy)) * mu0 * Il / dz - mu0 * (1 / (dx * dy * dz)) * Il * Al) < 1e-15, "notes' stack average = mu0 N I_l A_l")
Bt = 0.37; mu = 100 * mu0
ok(abs(Bt * (mu - mu0) / (mu * mu0) - 99 * Bt / mu) < 1e-9, "concept-map M = B(mu-mu0)/(mu mu0) = chi_m H")

P("== E. slab between two sheets (slide 16) + bound-current check")
def Hsheets(zp, sheets):
    Ht = np.zeros(3)
    for zs, Js in sheets:
        nh = Z if zp > zs else -Z
        Ht += 0.5 * cross(Js, nh)
    return Ht
free = [(1.0, -0.1 * Y), (-1.0, 0.1 * Y)]
ok(close(0.5 * cross(-0.1 * Y, -Z), 0.05 * X) and close(0.5 * cross(0.1 * Y, Z), 0.05 * X), "each sheet gives +0.05 x between")
ok(close(Hsheets(0.0, free), 0.1 * X) and close(Hsheets(2, free), 0 * X) and close(Hsheets(-2, free), 0 * X), "H = 0.1 x between, 0 outside")
mur = 100; Hs = 0.1 * X; Bs = mu0 * mur * Hs; Ms = (mur - 1) * Hs
P(f"   B_slab = {Bs[0]:.4e} T ; M = {Ms[0]:.2f} A/m ; mu0(H+M) = {mu0*(Hs+Ms)[0]:.4e} ; mu_r=1: B = {mu0*0.1:.4e} T")
ok(abs(Bs[0] - 1.26e-5) < 0.005e-5 and abs(Ms[0] - 9.9) < 1e-12 and abs(mu0 * 0.1 - 1.26e-7) < 0.005e-7, "slab numbers")
Jt, Jb = cross(Ms, Z), cross(Ms, -Z)
ok(close(Jt, -9.9 * Y) and close(Jb, 9.9 * Y), "bound faces: -9.9 y top, +9.9 y bottom (same sense as free)")
allc = free + [(0.6, Jt), (-0.6, Jb)]
ok(close(Hsheets(0.0, allc), 10 * X) and close(Hsheets(0.8, allc), 0.1 * X) and close(Hsheets(1.5, allc), 0 * X),
   "vacuum formula with free+bound: B/mu0 = 10 x in slab, 0.1 x in gap, 0 outside")
# page frame (x right, z up, y into page) -> screen (X=x, Y=z, Z=-y)
to_screen = lambda vp: np.array([vp[0], vp[2], -vp[1]])
ok(to_screen(-0.1 * Y)[2] > 0 and to_screen(0.1 * Y)[2] < 0 and to_screen(Jt)[2] > 0 and to_screen(Jb)[2] < 0,
   "fig slab: top free & bound odot, bottom free & bound otimes; y into page")
ok(close(cross(X, Y), Z) and close(cross(to_screen(X), to_screen(Y)), to_screen(Z)), "page frame (x right, z up, y into page) is right-handed")

P("== F. tables: chi_m <-> mu_r")
rows = [("bismuth", -1.7e-4, "0.99983"), ("silver", -7e-5, "0.99993"), ("copper", -0.94e-5, "0.999991"),
        ("water", -0.88e-5, "0.999991"), ("aluminum", 2.1e-5, "1.00002"), ("platinum", 2.9e-5, "1.000029"),
        ("liquid oxygen", 3.5e-5, "1.000035"), ("palladium", 8e-4, "1.0008")]
for nm, c, mr in rows:
    dec = len(mr.split(".")[1])
    ok(abs((1 + c) - float(mr)) <= 0.6 * 10**-dec + 1e-12, f"{nm}: 1 + ({c:g}) = {1+c:.7f} vs printed {mr}")
ok(abs(1 + 0.99993 - 2 + 7e-5) < 1e-9, "silver: mu_r 0.99993 <-> chi -7e-5 (only if the table really says 0.99993)")
P("   physical reference values (molar susceptibilities, CGS 1e-6 cm^3/mol, CRC; reviewer's memory) -> SI volume chi:")
ref = {"Al": (16.5, 2.70, 26.98), "Bi": (-280.1, 9.78, 208.98), "Cu": (-5.46, 8.96, 63.546), "Pb": (-23.0, 11.34, 207.2),
       "Pd": (567.4, 12.02, 106.42), "Pt": (193.0, 21.45, 195.08), "Ag": (-19.5, 10.49, 107.87), "H2O": (-12.97, 0.998, 18.015),
       "O2 liq 90K": (7699.0, 1.141, 32.0), "O2 gas 293K": (3449.0, 1.331e-3, 32.0)}
for k_, (cm, rho, Mm) in ref.items():
    P(f"     {k_:12s} chi_SI = {4*pi*cm*1e-6*rho/Mm:+.2e}")
P("   -> slides: Pt +2.90e-5 (real ~ +2.7e-4: x10 low), liquid O2 +3.50e-5 (real ~ +3.5e-3: x100 low); Ag real -2.4e-5 (mu_r 0.99998)")

P("== G. boundary conditions, refraction, iron")
th_air = math.degrees(math.atan(math.tan(math.radians(85)) / 5000)); th2 = math.degrees(math.atan(math.tan(math.radians(89.9)) / 5000))
ok(abs(th_air - 0.13) < 0.005 and abs(th2 - 6.5) < 0.05, f"iron 85 deg -> {th_air:.3f} deg ; 89.9 deg -> {th2:.2f} deg")
H1 = np.array([4., -3, -9]); m1, m2 = 2, 6
H2 = np.array([4., -3, m1 / m2 * H1[2]]); B1, B2 = m1 * H1, m2 * H2      # in units of mu0
ok(close(H2, [4, -3, -3]) and close(B1, [8, -6, -18]) and close(B2, [24, -18, -18]), "problem (a),(b)")
ok(close(B1 - H1, [4, -3, -9]) and close(B2 - H2, [20, -15, -15]), "problem (c): M = B/mu0 - H")
ok(abs(np.linalg.norm(B1) * mu0 - 2.59e-5) < 0.005e-5 and abs(np.linalg.norm(B2) * mu0 - 4.40e-5) < 0.005e-5 and abs(-18 * mu0 + 2.26e-5) < 0.005e-5, "problem (b) magnitudes")
t1, t2 = 5 / 9, 5 / 3
ok(abs(math.degrees(math.atan(t1)) - 29.1) < 0.05 and abs(math.degrees(math.atan(t2)) - 59.0) < 0.05 and abs(t1 / t2 - m1 / m2) < 1e-12, "problem (d) angles 29.1, 59.0 ; ratio 1/3")
ok(close(cross(Z, B1 - B2), [-12, -16, 0]) and abs(dot([-12, -16, 0], H1 * [1, 1, 0])) < 1e-12 and close((1 - 5) * cross(Z, H1 * [1, 1, 0]), [-12, -16, 0]), "problem (e) check, J_sM perp H_t, (chi1-chi2) z x H1t")
ok((H1 - H2)[2] == -6 and -((B1 - H1) - (B2 - H2))[2] == -6, "normal H jump = -(normal M jump) = -6")
Js = 2 * Y; H2v = H1 * [1, 1, 0] - cross(Js, Z) + [0, 0, -3]
B2v, M2v = 6 * H2v, 5 * H2v
ok(close(H2v, [2, -3, -3]) and close(cross(Z, H1 - H2v), Js) and close(B2v, [12, -18, -18]) and close(M2v, [10, -15, -15]), "variant: H2, B2, M2")
ok(close(cross(Z, (B1 - H1) - M2v), [-12, -6, 0]) and close(cross(Z, B1 - B2v), Js + cross(Z, (B1 - H1) - M2v)), "variant: J_sM = (-12,-6), check (-12,-4)")
ok(abs(math.degrees(math.atan(math.sqrt(13) / 3)) - 50.2) < 0.05, "variant theta2 = 50.2 deg")
rng = np.random.default_rng(3)
for _ in range(200):
    a1, a2 = rng.uniform(0.5, 50, 2); Hh = rng.normal(size=3); Jv = rng.normal(size=3) * [1, 1, 0]
    Hb = Hh * [1, 1, 0] - cross(Jv, Z) + [0, 0, a1 / a2 * Hh[2]]
    Bt1, Bt2 = a1 * Hh, a2 * Hb; Mt1, Mt2 = Bt1 - Hh, Bt2 - Hb
    assert abs(Bt1[2] - Bt2[2]) < 1e-12 and close(cross(Z, Hh - Hb), Jv) and close(cross(Z, Bt1 - Bt2), Jv + cross(Z, Mt1 - Mt2))
ok(True, "general pattern (200 random cases): B_n continuous, n x dH = Js, n x dB/mu0 = Js + n x dM")

P("== H. figure geometry (screen frame X right, Y up, Z out)")
mhat = np.array([math.sin(th), math.cos(th), 0]); rR = np.array([math.cos(th), -math.sin(th), 0])
ok(abs(dot(mhat, rR)) < 1e-12, "fig1: loop edge (P_L -> P_R) is perpendicular to m")
iR, iL = cross(mhat, rR), cross(mhat, -rR)
ok(iR[2] < 0 and iL[2] > 0, "fig1: current otimes at P_R (lower right), odot at P_L (upper left)")
FR, FL = cross(iR, Y), cross(iL, Y)
ok(FR[0] > 0 and FL[0] < 0, "fig1: F right at P_R, left at P_L")
Tq = cross(rR, FR) + cross(-rR, FL)
ok(Tq[2] > 0 and close(cross(mhat, Y), [0, 0, math.sin(th)]), "fig1: torque +Z (odot, CCW arc), = m x B0")
ok(close(cross(Z, -Y), X), "fig1 panel A: near side y=-a, CCW about +z has +x current there (m up)")
for nn, exp in ((X, Y), (Y, -X), (-X, -Y), (-Y, X)):
    ok(close(cross(Z, nn), exp), f"fig2 lattice M odot: edge n={nn} -> M x n = {exp}")
ok(cross(Y, X)[2] < 0 and cross(Y, -X)[2] > 0, "fig2 rod M up: right side otimes, left side odot")
# hysteresis functions of the figure
Bs_, Hc, wv = 1.0, 0.9, 0.8
Bd = lambda h: Bs_ * np.tanh((h + Hc) / wv); Ba = lambda h: Bs_ * np.tanh((h - Hc) / wv)
Bv = lambda h: Bs_ * np.tanh((h / wv)**2 / (1 + h / wv))
hh = np.linspace(1e-3, 3, 3000)
ok(np.all(Ba(hh) <= Bv(hh)) and np.all(Bv(hh) <= Bd(hh)) and Bd(0) > 0 and abs(Bd(-Hc)) < 1e-12, f"fig4: virgin curve inside loop; B_r = {Bd(0):.3f}; B(-Hc) = 0 on the descending branch")
hs = np.linspace(3, -3, 121); poly = [(h, Bd(h)) for h in hs] + [(h, Ba(h)) for h in hs[::-1]]
area = 0.5 * sum(x1 * y2 - x2 * y1 for (x1, y1), (x2, y2) in zip(poly, poly[1:] + poly[:1]))
ok(area > 0, f"fig4: upper branch leftward + lower rightward = counter-clockwise (signed area {area:.2f} > 0)")
s_ = 11; v1 = np.array([5 * s_, -9 * s_]); v2 = np.array([5 * s_, -3 * s_])   # screen vectors of H1, H2 (Y up)
ok(abs(math.degrees(math.atan2(abs(v1[0]), abs(v1[1]))) - 29.05) < 0.1 and abs(math.degrees(math.atan2(abs(v2[0]), abs(v2[1]))) - 59.04) < 0.1, "fig5: drawn H1, H2 at 29.1, 59.0 deg from the normal, both pointing down-right")
ok(abs(math.degrees(math.atan2(math.sin(math.radians(85)), math.cos(math.radians(85)))) - 85) < 1e-9, "fig5 right: iron line at 85 deg from normal")

P("== I. Lecture 16 slide exercises")
ok(abs(np.linalg.norm([1, -2, 2]) - 3) < 1e-12 and abs(-np.linalg.norm([1, 0, math.sqrt(3)]) + 2) < 1e-12, "rho_s = 3 D0 and -2 D0")

P(f"== {NFAIL} FAIL(s)")
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "review_L17.out"), "w") as f:
    f.write("\n".join(OUT) + "\n")
