#!/usr/bin/env python3
"""Verification script for content-src/practice/09-static-fields-in-dielectric-media.md
(ECE 329, Lecture 9: static fields in dielectric media).

numpy / scipy only.  Every number, sign and direction quoted on the page is printed below,
and each closed form is checked against a brute-force computation:
  * potentials by numerical integration of E through EVERY layer (scipy quad, split at interfaces);
  * boundary conditions with explicit vectors:  n x (E1 - E2) = 0 (np.cross),
    n . (D1 - D2) = rho_s (np.dot), n pointing from medium 2 into medium 1;
  * conductor surfaces: rho_s = n . D with n out of the metal;
  * bound charge: rho_sb = P . n (outward normal of the dielectric), rho_b = -div P by finite
    differences, and the total bound charge of every dielectric body summed to zero;
  * Gauss's law by numerical flux integrals (dblquad) over closed surfaces.
Convention: V(b) - V(a) = -int_a^b E . dl.
"""
import numpy as np
from scipy import integrate

eps0 = 8.8541878128e-12          # F/m
pi = np.pi
RESULTS = []


def check(label, value, expected, rtol=1e-7, atol=0.0):
    ok = bool(np.allclose(np.asarray(value, dtype=float), np.asarray(expected, dtype=float),
                          rtol=rtol, atol=atol))
    RESULTS.append((label, ok))
    print(f"  [{'ok' if ok else 'FAIL'}] {label}: computed {np.round(np.asarray(value, dtype=float), 10)}"
          f"  vs  expected {np.round(np.asarray(expected, dtype=float), 10)}")
    return ok


def say(label, value):
    print(f"  {label}: {value}")


def quad(f, a, b, points=None):
    """quad that also accepts an infinite upper limit and interior break points."""
    if points is None or np.isinf(b):
        return integrate.quad(f, a, b, epsabs=1e-13, epsrel=1e-12, limit=400)[0]
    return integrate.quad(f, a, b, points=points, epsabs=1e-13, epsrel=1e-12, limit=400)[0]


def ddx(f, x, h=1e-5):
    return (f(x + h) - f(x - h)) / (2 * h)


zhat = np.array([0.0, 0.0, 1.0])
xhat = np.array([1.0, 0.0, 0.0])

# =====================================================================================
print("=" * 88)
print("9.1  Three layers between charged plates  (plates z=0 [-6 eps0, V=0] and z=3 m [+6 eps0])")
layers = [(0.0, 1.0, 1.0), (1.0, 2.0, 2.0), (2.0, 3.0, 3.0)]          # (z_lo, z_hi, eps_r)
rho_bot = -6 * eps0
# Gauss pillbox at the bottom plate: n = +z (out of the metal into the gap), rho_s = n.D
n_bot = zhat
D = rho_bot * n_bot / np.dot(n_bot, n_bot)                          # D is the same in every layer
check("D_z / eps0 (all three layers)", D[2] / eps0, -6)
say("D_z numeric [C/m^2]", f"{D[2]:.3e}")


def epsr_91(z):
    return 1.0 if z < 1 else (2.0 if z < 2 else 3.0)


def Ez_91(z):
    return D[2] / (epsr_91(z) * eps0)


for (zl, zh, er) in layers:
    E = D / (er * eps0)
    P = D - eps0 * E
    print(f"   layer {zl:.0f}<z<{zh:.0f}, eps_r={er:.0f}:  E_z = {E[2]:+.4f} V/m,  P_z/eps0 = {P[2] / eps0:+.4f}")
check("E_z in the three layers [V/m]", [Ez_91(0.5), Ez_91(1.5), Ez_91(2.5)], [-6, -3, -2])
check("P_z/eps0 in the three layers", [(D[2] - eps0 * Ez_91(z)) / eps0 for z in (0.5, 1.5, 2.5)], [0, -3, -4])
V91 = {z: -quad(Ez_91, 0, z, points=[p for p in (1.0, 2.0) if p < z]) for z in (1.0, 2.0, 3.0)}
check("V(1), V(2), V(3) [V] by quad through every layer", [V91[1.0], V91[2.0], V91[3.0]], [6, 9, 11])
# top plate: n = -z (out of the metal, into the gap)
check("top-plate rho_s/eps0 = (-z).D(3^-)", np.dot(-zhat, D) / eps0, 6)
# interfaces z=1, z=2: n = +z from lower (2) to upper (1) layer; no free charge
for zi in (1.0, 2.0):
    E1 = np.array([0, 0, Ez_91(zi + 1e-9)]); E2 = np.array([0, 0, Ez_91(zi - 1e-9)])
    D1 = epsr_91(zi + 1e-9) * eps0 * E1; D2 = epsr_91(zi - 1e-9) * eps0 * E2
    check(f"z={zi:.0f}: n.(D1-D2) = 0 (no free charge)", np.dot(zhat, D1 - D2) / eps0, 0, atol=1e-12)

# =====================================================================================
print("=" * 88)
print("9.2  Two dielectrics side by side  (z=0 grounded, z=2 mm at +10 V; eps_r=2 for x<0, 5 for x>0)")
V0, d = 10.0, 2e-3
E = np.array([0, 0, -V0 / d])                       # same in both halves
check("E_z [V/m] (both halves)", E[2], -5000)
check("V(d)-V(0) = -int E_z dz [V]", -quad(lambda z: E[2], 0, d), 10)
DL, DR = 2 * eps0 * E, 5 * eps0 * E                 # x<0 (medium 2), x>0 (medium 1)
# interface x = 0: n = +x from left (2) into right (1)
check("x=0: n x (E1-E2) = 0", np.cross(xhat, E - E), [0, 0, 0], atol=1e-15)
check("x=0: n.(D1-D2) = 0 (D is tangential to the interface)", np.dot(xhat, DR - DL), 0, atol=1e-25)
check("D_z left / eps0 , right / eps0", [DL[2] / eps0, DR[2] / eps0], [-1e4, -2.5e4])
say("D_z left, right [nC/m^2]", f"{DL[2] * 1e9:.2f}, {DR[2] * 1e9:.2f}")
rho_top_L, rho_top_R = np.dot(-zhat, DL), np.dot(-zhat, DR)   # n out of the top plate = -z
say("top-plate free rho_s left, right [nC/m^2]", f"{rho_top_L * 1e9:.2f}, {rho_top_R * 1e9:.2f}")
check("top-plate rho_s left, right [nC/m^2]", [rho_top_L * 1e9, rho_top_R * 1e9], [88.541878128, 221.35469532])
PL, PR = DL - eps0 * E, DR - eps0 * E
say("P_z left, right [nC/m^2]", f"{PL[2] * 1e9:.2f}, {PR[2] * 1e9:.2f}  (= {PL[2] / eps0:.0f} eps0, {PR[2] / eps0:.0f} eps0)")
check("P_z/eps0 left, right", [PL[2] / eps0, PR[2] / eps0], [-5000, -20000])
# bound charge on the dielectrics' top faces (outward normal +z) and net charge at the top surface
sbL, sbR = np.dot(PL, zhat), np.dot(PR, zhat)
say("bound rho_sb on top faces left, right [nC/m^2]", f"{sbL * 1e9:.2f}, {sbR * 1e9:.2f}")
check("net (free+bound) at top, left = right = eps0*|E| [nC/m^2]",
      [(rho_top_L + sbL) * 1e9, (rho_top_R + sbR) * 1e9], [eps0 * 5000 * 1e9] * 2)
say("eps0*|E| [nC/m^2]", f"{eps0 * 5000 * 1e9:.2f}")

# =====================================================================================
print("=" * 88)
print("9.3  MC: graded dielectric, no free charge -- test each option on Lecture 9 Example 4")
#   eps(z) = 4 eps0/(4-z), D_z = 2 eps0  ->  E_z = 2(1 - z/4), V(0)=0
eps93 = lambda z: 4 * eps0 / (4 - z)
Dz93 = 2 * eps0
E93 = lambda z: Dz93 / eps93(z)
V93 = lambda z: -quad(E93, 0, z)
P93 = lambda z: Dz93 - eps0 * E93(z)
for z in (0.5, 1.0, 1.5):
    lapV = (V93(z + 1e-3) - 2 * V93(z) + V93(z - 1e-3)) / 1e-6
    divE = ddx(E93, z)
    divP = ddx(P93, z) / eps0
    div_eps_gradV = ddx(lambda s: eps93(s) * ddx(V93, s, 1e-4), z, 1e-3) / eps0
    print(f"   z={z}:  (a) lap V = {lapV:+.4f} V/m^2   (b) div E = {divE:+.4f} V/m^2   "
          f"(d) div P/eps0 = {divP:+.4f}   (c) div(eps grad V)/eps0 = {div_eps_gradV:+.2e}")
check("(a) lap V = +1/2 V/m^2", (V93(1.0 + 1e-3) - 2 * V93(1.0) + V93(1.0 - 1e-3)) / 1e-6, 0.5, rtol=1e-4)
check("(b) div E = -1/2 V/m^2", ddx(E93, 1.0), -0.5, rtol=1e-6)
check("(d) div P = +eps0/2  ->  rho_b = -eps0/2", ddx(P93, 1.0) / eps0, 0.5, rtol=1e-6)
check("(c) div(eps grad V) = 0", ddx(lambda s: eps93(s) * ddx(V93, s, 1e-4), 1.0, 1e-3) / eps0, 0, atol=1e-5)

# =====================================================================================
print("=" * 88)
print("9.4  MC: refraction into glass eps_r = 4, incidence 45 deg from the normal")
E0 = 1.0
th1 = np.radians(45)
# air above (medium 1, z>0), glass below (medium 2, z<0), n = +z from 2 into 1; field heading into the glass
E1 = E0 * np.array([np.sin(th1), 0, -np.cos(th1)])
er2 = 4.0
E2 = np.array([E1[0], E1[1], E1[2] * 1.0 / er2])        # E_t copied, eps1 E1n = eps2 E2n
D1, D2 = eps0 * E1, er2 * eps0 * E2
check("n x (E1-E2) = 0", np.cross(zhat, E1 - E2), [0, 0, 0], atol=1e-15)
check("n.(D1-D2) = 0", np.dot(zhat, D1 - D2), 0, atol=1e-25)
th2 = np.degrees(np.arctan2(np.hypot(E2[0], E2[1]), abs(E2[2])))
check("tan(theta2) = 4", np.tan(np.radians(th2)), 4)
say("theta2 [deg]", f"{th2:.2f}")
check("|E2|/E0 = sqrt(17/32)", np.linalg.norm(E2) / E0, np.sqrt(17 / 32))
say("|E2|/E0", f"{np.linalg.norm(E2) / E0:.4f}")
check("|D2|/(eps0 E0) = sqrt(8.5)", np.linalg.norm(D2) / (eps0 * E0), np.sqrt(8.5))
say("|D2|/(eps0 E0)", f"{np.linalg.norm(D2) / (eps0 * E0):.4f}")
say("E2 tangential, normal (units of E0)", f"{E2[0]:.4f} (= 1/sqrt2), {E2[2]:.4f} (= -1/(4 sqrt2))")
# option (d): whole vector scaled by 1/4 -> violates n x (E1-E2)=0
E2d = E1 / 4
say("option (d) violates tangential continuity: |n x (E1-E2d)|", f"{np.linalg.norm(np.cross(zhat, E1 - E2d)):.4f} (should be 0)")

# =====================================================================================
print("=" * 88)
print("9.5  Find the error: coated wire  (rho_l = 10 nC/m, a = 1 mm, b = 2 mm, eps_r = 2.5)")
rl, a5, b5, er5 = 10e-9, 1e-3, 2e-3, 2.5
Dr = lambda r: rl / (2 * pi * r)
# Gauss for D by a brute-force flux integral over a cylinder of radius b+ and length 1 m
flux = integrate.dblquad(lambda z, phi: Dr(b5) * b5, 0, 2 * pi, 0, 1.0)[0]
check("flux of D through cylinder r=b, L=1 m [nC]", flux * 1e9, 10)
E_in, E_out = Dr(b5) / (er5 * eps0), Dr(b5) / eps0
say("E(b-) [kV/m] (student's number, valid INSIDE the coating)", f"{E_in / 1e3:.2f}")
say("E(b+) [kV/m] (correct outside value)", f"{E_out / 1e3:.2f}")
k_c = (2.99792458e8) ** 2 * 1e-7          # 1/(4 pi eps0) from c and mu0 = 4 pi 1e-7, independent reference
check("E(b-), E(b+) [V/m] vs 2k rho_l/(eps_r b), 2k rho_l/b", [E_in, E_out], [2 * k_c * rl / (er5 * b5), 2 * k_c * rl / b5], rtol=1e-6)
Pb = (1 - 1 / er5) * Dr(b5)
say("D(b) [uC/m^2]", f"{Dr(b5) * 1e6:.3f}")
say("bound rho_sb on outer face = P(b) [uC/m^2]", f"{Pb * 1e6:.3f}")
check("eps0 [E(b+) - E(b-)] = rho_sb(b)", eps0 * (E_out - E_in), Pb)

# =====================================================================================
print("=" * 88)
print("9.6  Graded dielectric at fixed voltage  (eps_r = (1+z)^2, V(0)=6 V, V(1)=0)")
er6 = lambda z: (1 + z) ** 2
Ival = quad(lambda z: 1 / er6(z), 0, 1)
check("int_0^1 dz/eps_r = 1/2 [m]", Ival, 0.5)
D6 = (6.0 - 0.0) * eps0 / Ival                     # V(0)-V(1) = (D/eps0) int dz/eps_r
check("D_z/eps0", D6 / eps0, 12)
say("D_z numeric [C/m^2]", f"{D6:.3e}")
check("bottom plate rho_s/eps0 = (+z).D ; top plate = (-z).D", [D6 / eps0, -D6 / eps0], [12, -12])
E6 = lambda z: D6 / (eps0 * er6(z))
check("E_z(0), E_z(1) [V/m]", [E6(0), E6(1)], [12, 3])
V6 = lambda z: 6.0 - quad(E6, 0, z)
check("V(0.5) [V]  (homogeneous fill would give 3 V)", V6(0.5), 2.0)
check("V(1) [V]", V6(1.0), 0.0, atol=1e-10)
check("V(z) = 6 - 12 z/(1+z) at z=0.25,0.75", [V6(0.25), V6(0.75)], [6 - 12 * 0.25 / 1.25, 6 - 12 * 0.75 / 1.75])
P6 = lambda z: D6 - eps0 * E6(z)
check("P_z(0)/eps0, P_z(1)/eps0", [P6(0) / eps0, P6(1) / eps0], [0, 9])
rhob6 = lambda z: -ddx(P6, z)
for z in (0.0, 0.5, 1.0):
    check(f"rho_b({z})/eps0 = -24/(1+z)^3", rhob6(z) / eps0, -24 / (1 + z) ** 3, rtol=1e-6)
bulk = quad(lambda z: -24 * eps0 / (1 + z) ** 3, 0, 1)
sb_top, sb_bot = np.dot(P6(1) * zhat, zhat), np.dot(P6(0) * zhat, -zhat)
check("bound: bulk/eps0, top face/eps0, bottom face/eps0", [bulk / eps0, sb_top / eps0, sb_bot / eps0], [-9, 9, 0], atol=1e-12)
check("total bound charge per m^2 = 0", (bulk + sb_top + sb_bot) / eps0, 0, atol=1e-9)
for z in (0.3, 0.8):   # Gauss for ALL charge: eps0 E(z) = rho_s(0) + rho_sb(0) + int_0^z rho_b
    tot = D6 + sb_bot + quad(lambda s: -24 * eps0 / (1 + s) ** 3, 0, z)
    check(f"eps0 E_z({z}) = enclosed free+bound  (in units of eps0)", E6(z), tot / eps0)

# =====================================================================================
print("=" * 88)
print("9.7  Charged sheet on a dielectric interface (plates z=0,3 m grounded; eps_r=2 below z=1; sheet 10 eps0)")
# unknowns V = A1 z + B1 (0<z<1, eps 2eps0), V = A2 z + B2 (1<z<3, eps0)
# rows: V(0)=0 ; V(3)=0 ; continuity at 1 ; n.(D_above - D_below) = rho_s with n=+z, D=-eps dV/dz
M = np.array([[0, 1, 0, 0],
              [0, 0, 3, 1],
              [1, 1, -1, -1],
              [2, 0, -1, 0]], dtype=float)       # eps0*(-A2) - 2eps0*(-A1) = 10 eps0
rhs = np.array([0, 0, 0, 10.0])
A1, B1, A2, B2 = np.linalg.solve(M, rhs)
V1 = A1 * 1 + B1
check("V(1) [V]", V1, 4)
Eb, Ea = -A1, -A2
check("E_z below, above [V/m]", [Eb, Ea], [-4, 2])
Db, Da = 2 * Eb, 1 * Ea                           # in units of eps0
check("D_z/eps0 below, above", [Db, Da], [-8, 2])
check("n.(D1-D2)/eps0 at z=1 (n=+z, 1=above) = 10", np.dot(zhat, np.array([0, 0, Da]) - np.array([0, 0, Db])), 10)
rho0, rho3 = np.dot(zhat, [0, 0, Db]), np.dot(-zhat, [0, 0, Da])
check("plate charges/eps0 at z=0, z=3", [rho0, rho3], [-8, -2])
check("sum of plate charges = -rho_s", rho0 + rho3, -10)
Pb7 = Db - Eb                                     # P/eps0 in the dielectric
check("P_z/eps0 below", Pb7, -4)
check("bound faces/eps0: top (z=1-, n=+z), bottom (z=0+, n=-z)", [Pb7 * 1, Pb7 * -1], [-4, 4])
check("eps0(E_above - E_below) = rho_s + rho_sb  (/eps0)", Ea - Eb, 10 + Pb7 * 1)
check("potential via quad: V(3)-V(0) = 0", -quad(lambda z: Eb if z < 1 else Ea, 0, 3, points=[1.0]), 0, atol=1e-12)
# (d) top plate raised to Vt (unknown) so that the region above is field-free: A2 = 0
M2 = np.array([[0, 1, 0, 0, 0],
               [0, 0, 3, 1, -1],
               [1, 1, -1, -1, 0],
               [2, 0, -1, 0, 0],
               [0, 0, 1, 0, 0]], dtype=float)
A1d, B1d, A2d, B2d, Vt = np.linalg.solve(M2, np.array([0, 0, 0, 10.0, 0]))
check("(d) V(3) needed [V]", Vt, 5)
check("(d) E_z below [V/m], D_z below/eps0", [-A1d, -2 * A1d], [-5, -10])
check("(d) plate charges/eps0 z=0, z=3", [np.dot(zhat, [0, 0, -2 * A1d]), np.dot(-zhat, [0, 0, -A2d])], [-10, 0], atol=1e-12)
check("(d) V(3)-V(0) by quad", -quad(lambda z: -A1d if z < 1 else -A2d, 0, 3, points=[1.0]), 5)

# =====================================================================================
print("=" * 88)
print("9.8  Charged surface of a dielectric rod (R = 2 m, eps_r = 4; E(2-) = 3, E(2+) = 8 V/m)")
R8, er8, Ein8, Eout8 = 2.0, 4.0, 3.0, 8.0
rhat = np.array([np.cos(0.7), np.sin(0.7), 0.0])    # any radial direction
D1 = eps0 * Eout8 * rhat          # medium 1 = air (outside)
D2 = er8 * eps0 * Ein8 * rhat     # medium 2 = rod
rs8 = np.dot(rhat, D1 - D2)
check("rho_s/eps0 = n.(D1 - D2)", rs8 / eps0, -4)
say("rho_s numeric [C/m^2]", f"{rs8:.3e}")
rl8 = 2 * pi * R8 * er8 * eps0 * Ein8
check("rho_l/(pi eps0)", rl8 / (pi * eps0), 48)
say("rho_l numeric [C/m]", f"{rl8:.3e}")
Er8 = lambda r: rl8 / (2 * pi * er8 * eps0 * r) if r < R8 else (rl8 + 2 * pi * R8 * rs8) / (2 * pi * eps0 * r)
check("E inside = 6/r : E(1), E(2-)", [Er8(1.0), Er8(2 - 1e-12)], [6, 3])
check("E outside = 16/r : E(2+), E(4)", [Er8(2 + 1e-12), Er8(4.0)], [8, 4])
# Gauss for D: flux through a cylinder r=3, L=1 by dblquad equals the enclosed free charge
fl = integrate.dblquad(lambda z, phi: eps0 * Er8(3.0) * 3.0, 0, 2 * pi, 0, 1.0)[0]
check("flux of D through r=3 m cylinder (per m) / (pi eps0)", fl / (pi * eps0), 48 - 16)
P8 = lambda r: (er8 - 1) * eps0 * Er8(r)            # inside
check("P_r(2-)/eps0 = rho_sb on the surface", P8(2 - 1e-12) / eps0, 9)
sb_len = P8(2 - 1e-12) * 2 * pi * R8
check("bound surface charge per length /(pi eps0)", sb_len / (pi * eps0), 36)
# bound line charge on the axis: Q_b = -(flux of P out of a thin cylinder of radius r0)
for r0 in (1e-3, 0.5):
    line = -P8(r0) * 2 * pi * r0
    check(f"bound line charge (r0={r0}) /(pi eps0) = -(chi/eps_r) rho_l", line / (pi * eps0), -36)
check("total charge at r=2 (free + bound)/eps0 = eps0 (E+ - E-)/eps0", (rs8 + P8(2 - 1e-12)) / eps0, Eout8 - Ein8)
V14 = quad(lambda r: Er8(r), 1, 4, points=[2.0])  # V(1) - V(4) = + int_1^4 E_r dr
check("V(1) - V(4) = 22 ln 2 [V]", V14, 22 * np.log(2))
say("V(1) - V(4) [V]", f"{V14:.3f}")

# =====================================================================================
print("=" * 88)
print("9.9  Glass slab (eps_r = 3, 0<z<3 cm) in E0 = 40 x + 30 z V/m")
E0v = np.array([40.0, 0, 30.0]); er9 = 3.0; t9 = 0.03
# bottom face z=0: medium 1 = glass (above), medium 2 = air (below), n = +z
Eg = np.array([E0v[0], E0v[1], E0v[2] / er9])
check("glass E [V/m]", Eg, [40, 0, 10])
check("z=0: n x (E1-E2) = 0", np.cross(zhat, Eg - E0v), [0, 0, 0], atol=1e-14)
check("z=0: n.(D1-D2) = 0", np.dot(zhat, er9 * Eg - E0v), 0, atol=1e-12)
Dg, Pg = er9 * eps0 * Eg, er9 * eps0 * Eg - eps0 * Eg
check("D_glass/eps0", Dg / eps0, [120, 0, 30])
check("P_glass/eps0", Pg / eps0, [80, 0, 20])
say("D_glass numeric [C/m^2]", f"({Dg[0]:.3e}, 0, {Dg[2]:.3e})")
say("P_glass numeric [C/m^2]", f"({Pg[0]:.3e}, 0, {Pg[2]:.3e})")
tha = np.degrees(np.arctan2(E0v[0], E0v[2])); thg = np.degrees(np.arctan2(Eg[0], Eg[2]))
say("angle from normal: air, glass [deg]", f"{tha:.2f}, {thg:.2f}")
check("tan(th_air)/tan(th_glass) = eps_air/eps_glass", np.tan(np.radians(tha)) / np.tan(np.radians(thg)), 1 / 3)
# top face z=t: medium 1 = air above, medium 2 = glass, n = +z
Eabove = np.array([Eg[0], Eg[1], er9 * Eg[2]])
check("E above the slab [V/m] = E0", Eabove, E0v)
check("z=t: n x (E1-E2) = 0 ; n.(D1-D2) = 0",
      [np.linalg.norm(np.cross(zhat, Eabove - Eg)), np.dot(zhat, Eabove - er9 * Eg)], [0, 0], atol=1e-12)
sb_top9, sb_bot9 = np.dot(Pg, zhat), np.dot(Pg, -zhat)
check("rho_sb top, bottom /eps0", [sb_top9 / eps0, sb_bot9 / eps0], [20, -20])
say("rho_sb numeric [C/m^2]", f"{sb_top9:.3e}")
# field of the two bound sheets by superposition: sheet s at z0 -> s/(2 eps0) sgn(z - z0) z-hat
Esheets = lambda z: (sb_top9 / (2 * eps0)) * np.sign(z - t9) + (sb_bot9 / (2 * eps0)) * np.sign(z - 0.0)
check("bound sheets' E_z below / inside / above [V/m]", [Esheets(-0.01), Esheets(0.015), Esheets(0.05)], [0, -20, 0])
check("E0 + sheets inside = glass field", E0v + np.array([0, 0, Esheets(0.015)]), Eg)
# (d) field line through A=(0,0,0): straight inside (uniform E) with dx/dz = Ex/Ez
A9 = np.array([0.0, 0, 0]); B9 = A9 + t9 * Eg / Eg[2]
check("exit point B [m]", B9, [0.12, 0, 0.03])
Efield9 = lambda r: E0v if (r[2] < 0 or r[2] > t9) else Eg


def line_V(path_pts, n=1):
    """V(end) - V(start) = -sum int E.dl over straight segments, each by quad."""
    tot = 0.0
    for p, q in zip(path_pts[:-1], path_pts[1:]):
        p, q = np.asarray(p, float), np.asarray(q, float)
        f = lambda s: np.dot(Efield9(p + s * (q - p) + 1e-12 * zhat * 0), q - p)
        tot -= quad(f, 0, 1)
    return tot


# keep paths strictly inside the slab (z in (0, t)) except the endpoints' own faces
eps_in = 1e-9
V_AB_line = line_V([A9 + eps_in * zhat, B9 - eps_in * zhat])
V_AB_stair = line_V([A9 + eps_in * zhat, np.array([0, 0, t9 - eps_in]), B9 - eps_in * zhat])
V_AB_below = line_V([A9 - eps_in * zhat, np.array([0.12, 0, -eps_in]), np.array([0.12, 0, eps_in]), B9 - eps_in * zhat])
check("V(B)-V(A): along the field line, staircase, via air below [V]", [V_AB_line, V_AB_stair, V_AB_below], [-5.1] * 3, rtol=1e-6)
check("pieces: up the z axis, then along x [V]", [-Eg[2] * t9, -Eg[0] * 0.12], [-0.3, -4.8])
check("|E_glass| * length along line = 5.1 V", np.linalg.norm(Eg) * np.linalg.norm(B9 - A9), 5.1)
x_noslab = t9 * E0v[0] / E0v[2]
check("x where the line would reach z=3 cm without slab [m]; lateral shift [m]", [x_noslab, B9[0] - x_noslab], [0.04, 0.08])

# =====================================================================================
print("=" * 88)
print("9.10 Sphere, shell and two dielectric layers (Q1=+2 C at r<=1; eps_r=4 in 1<r<2; shell 2..3 with -6 C;")
print("     eps_r=2 coating 3<r<4; free space r>4)")
Q1, Qshell = 2.0, -6.0


def region(r):
    if r < 1: return "core"
    if r < 2: return "diel1"
    if r <= 3: return "shell"
    if r < 4: return "coat"
    return "air"


epsr10 = {"diel1": 4.0, "coat": 2.0, "air": 1.0}


def Dr10(r):
    reg = region(r)
    if reg in ("core", "shell"):
        return 0.0
    Qenc = Q1 if reg == "diel1" else Q1 + Qshell
    return Qenc / (4 * pi * r ** 2)


def Er10(r):
    reg = region(r)
    return 0.0 if reg in ("core", "shell") else Dr10(r) / (epsr10[reg] * eps0)


def Pr10(r):
    reg = region(r)
    return 0.0 if reg in ("core", "shell") else Dr10(r) - eps0 * Er10(r)


# Gauss's law brute force: flux of D over spheres by dblquad equals enclosed free charge
for rr, Qexp in ((1.5, 2.0), (3.5, -4.0), (5.0, -4.0)):
    fl = integrate.dblquad(lambda th, ph: Dr10(rr) * rr ** 2 * np.sin(th), 0, 2 * pi, 0, pi)[0]
    check(f"flux of D over sphere r={rr} [C]", fl, Qexp)
check("D_r * 2 pi r^2 in 1<r<2 (= 1)", Dr10(1.5) * 2 * pi * 1.5 ** 2, 1.0)
check("D_r * pi r^2 in 3<r<4 and r>4 (= -1)", [Dr10(3.5) * pi * 3.5 ** 2, Dr10(6) * pi * 36], [-1, -1])
check("E_r * 8 pi eps0 r^2 in 1<r<2 (= 1)", Er10(1.5) * 8 * pi * eps0 * 1.5 ** 2, 1.0)
check("E_r * 2 pi eps0 r^2 in 3<r<4 (= -1)", Er10(3.5) * 2 * pi * eps0 * 3.5 ** 2, -1.0)
check("E_r * pi eps0 r^2 in r>4 (= -1)", Er10(6.0) * pi * eps0 * 36, -1.0)
check("P_r * 8 pi r^2/3 in 1<r<2 (= 1)", Pr10(1.5) * 8 * pi * 1.5 ** 2 / 3, 1.0)
check("P_r * 2 pi r^2 in 3<r<4 (= -1); P in air = 0", [Pr10(3.5) * 2 * pi * 3.5 ** 2, Pr10(6.0)], [-1, 0], atol=1e-15)
# free surface charge from boundary conditions with explicit vectors, n = r-hat (from inner (2) to outer (1))
nhat = np.array([np.sin(1.1) * np.cos(0.4), np.sin(1.1) * np.sin(0.4), np.cos(1.1)])
rs10 = {}
for rb in (1.0, 2.0, 3.0, 4.0):
    D_out, D_in = Dr10(rb + 1e-12) * nhat, Dr10(rb - 1e-12) * nhat
    E_out, E_in = Er10(rb + 1e-12) * nhat, Er10(rb - 1e-12) * nhat
    rs10[rb] = np.dot(nhat, D_out - D_in)
    assert np.linalg.norm(np.cross(nhat, E_out - E_in)) < 1e-6   # tangential E continuous (both radial)
check("free rho_s at r=1,2,3,4 [C/m^2]", [rs10[1.0], rs10[2.0], rs10[3.0], rs10[4.0]],
      [1 / (2 * pi), -1 / (8 * pi), -1 / (9 * pi), 0], atol=1e-12)
say("free rho_s numeric r=1,2,3", f"{rs10[1.0]:.4f}, {rs10[2.0]:.4f}, {rs10[3.0]:.4f} C/m^2")
check("shell: inner + outer surface charge = -6 C", 4 * pi * 4 * rs10[2.0] + 4 * pi * 9 * rs10[3.0], -6)
check("shell inner, outer surface totals [C]", [4 * pi * 4 * rs10[2.0], 4 * pi * 9 * rs10[3.0]], [-2, -4])
# bound surface charge: rho_sb = P.n, n = outward normal of each dielectric layer
sb = {1.0: np.dot(Pr10(1 + 1e-12) * nhat, -nhat), 2.0: np.dot(Pr10(2 - 1e-12) * nhat, nhat),
      3.0: np.dot(Pr10(3 + 1e-12) * nhat, -nhat), 4.0: np.dot(Pr10(4 - 1e-12) * nhat, nhat)}
check("rho_sb at r=1,2,3,4 [C/m^2]", [sb[1.0], sb[2.0], sb[3.0], sb[4.0]],
      [-3 / (8 * pi), 3 / (32 * pi), 1 / (18 * pi), -1 / (32 * pi)])
say("rho_sb numeric r=1,2,3,4", ", ".join(f"{sb[k]:.4f}" for k in (1.0, 2.0, 3.0, 4.0)) + " C/m^2")
tot = {k: 4 * pi * k ** 2 * sb[k] for k in sb}
check("bound totals [C] at r=1,2,3,4", [tot[1.0], tot[2.0], tot[3.0], tot[4.0]], [-1.5, 1.5, 2.0, -2.0])
# rho_b = -div P = -(1/r^2) d(r^2 P_r)/dr inside each layer (should vanish)
for rr in (1.5, 3.5):
    rhob = -ddx(lambda s: s ** 2 * Pr10(s), rr, 1e-4) / rr ** 2
    check(f"rho_b at r={rr} (= 0)", rhob, 0, atol=1e-8)
check("each layer neutral: (r=1)+(r=2), (r=3)+(r=4)", [tot[1.0] + tot[2.0], tot[3.0] + tot[4.0]], [0, 0], atol=1e-9)
check("at r=4: eps0(E+ - E-) = free + bound", eps0 * (Er10(4 + 1e-12) - Er10(4 - 1e-12)), rs10[4.0] + sb[4.0])
# potentials by quad through EVERY region, from infinity inward: V(r) = int_r^inf E_r dr
Vshell = quad(Er10, 3, 4) + quad(Er10, 4, np.inf)
V0c = quad(Er10, 0, 1) + quad(Er10, 1, 2) + quad(Er10, 2, 3) + Vshell
check("V(shell) * pi eps0 = -7/24", Vshell * pi * eps0, -7 / 24)
check("V(centre) * pi eps0 = -11/48", V0c * pi * eps0, -11 / 48)
check("V(centre) - V(shell) = 1/(16 pi eps0)", (V0c - Vshell) * 16 * pi * eps0, 1.0)
say("V(shell), V(centre), V(centre)-V(shell) [V]", f"{Vshell:.3e}, {V0c:.3e}, {V0c - Vshell:.3e}")
say("1/(pi eps0) [V m/C]", f"{1 / (pi * eps0):.4e}")

# =====================================================================================
print("=" * 88)
print("9.11 Graded coax with uniform field (a = 1 mm, b = 3 mm, eps = 6 eps0 a/r, V0 = 200 V)")
a11, b11, V011 = 1e-3, 3e-3, 200.0
eps11 = lambda r: 6 * eps0 * a11 / r
# brute force: D = rho_l/(2 pi r) (Gauss), V0 = int_a^b D/eps dr  ->  solve for rho_l
Iq = quad(lambda r: 1 / (2 * pi * r * eps11(r)), a11, b11)
rl11 = V011 / Iq
check("rho_l [nC/m] = 2 pi eps_a a V0/(b-a)", rl11 * 1e9, 2 * pi * 6 * eps0 * a11 * V011 / (b11 - a11) * 1e9)
say("rho_l [nC/m]", f"{rl11 * 1e9:.2f}")
E11 = lambda r: rl11 / (2 * pi * r * eps11(r))
check("E at r = a, 2a, b [V/m] (uniform)", [E11(a11), E11(2e-3), E11(b11)], [1e5] * 3)
check("V(a) - V(b) by quad [V]", quad(E11, a11, b11), 200)
D11 = lambda r: rl11 / (2 * pi * r)
say("D(a), D(b) [uC/m^2]", f"{D11(a11) * 1e6:.3f}, {D11(b11) * 1e6:.3f}")
check("r*D(r) [nC/m] = 6 eps0 a E", D11(2e-3) * 2e-3 * 1e9, 6 * eps0 * a11 * 1e5 * 1e9)
say("6 eps0 a E [C/m]", f"{6 * eps0 * a11 * 1e5:.3e}")
P11 = lambda r: D11(r) - eps0 * E11(r)
check("P(a)/(eps0 E), P(b)/(eps0 E)", [P11(a11) / (eps0 * 1e5), P11(b11) / (eps0 * 1e5)], [5, 1])
say("P(a), P(b) [uC/m^2]", f"{P11(a11) * 1e6:.3f}, {P11(b11) * 1e6:.4f}")
# rho_b = -(1/r) d(r P_r)/dr by finite differences, and independently by a Cartesian divergence
rhob11 = lambda r: -ddx(lambda s: s * P11(s), r, 1e-8) / r
for r in (a11 * 1.0001, 2e-3, b11 * 0.9999):
    check(f"rho_b({r * 1e3:.3f} mm) = eps0 E / r", rhob11(r), eps0 * 1e5 / r, rtol=1e-5)


def Pcart(x, y):
    r = np.hypot(x, y)
    return P11(r) * np.array([x / r, y / r])


def divP_cart(x, y, h=1e-8):
    return ((Pcart(x + h, y)[0] - Pcart(x - h, y)[0]) + (Pcart(x, y + h)[1] - Pcart(x, y - h)[1])) / (2 * h)


for (x, y) in ((1.2e-3, 0.9e-3), (-2.0e-3, 1.1e-3)):
    r = np.hypot(x, y)
    check(f"Cartesian -div P at ({x * 1e3:.1f},{y * 1e3:.1f}) mm = eps0 E/r", -divP_cart(x, y), eps0 * 1e5 / r, rtol=1e-5)
say("rho_b(a), rho_b(b) [mC/m^3]", f"{eps0 * 1e5 / a11 * 1e3:.3f}, {eps0 * 1e5 / b11 * 1e3:.3f}")
sba, sbb = np.dot(P11(a11), -1), np.dot(P11(b11), +1)
say("rho_sb(a), rho_sb(b) [uC/m^2]", f"{sba * 1e6:.3f}, {sbb * 1e6:.4f}")
la, lb = sba * 2 * pi * a11, sbb * 2 * pi * b11
lv = quad(lambda r: (eps0 * 1e5 / r) * 2 * pi * r, a11, b11)
check("bound per length / rho_l: inner face, outer face, volume", [la / rl11, lb / rl11, lv / rl11], [-5 / 6, 1 / 2, 1 / 3])
say("bound per length [nC/m]: inner, outer, volume", f"{la * 1e9:.2f}, {lb * 1e9:.2f}, {lv * 1e9:.2f}")
check("total bound per length = 0", (la + lb + lv) / rl11, 0, atol=1e-12)
for r in (1.5e-3, 2.5e-3):   # Gauss with ALL charge
    enc = rl11 + la + quad(lambda s: (eps0 * 1e5 / s) * 2 * pi * s, a11, r)
    check(f"2 pi r eps0 E = free+bound enclosed at r={r * 1e3} mm  [nC/m]", 2 * pi * r * eps0 * E11(r) * 1e9, enc * 1e9)
Emax_h = V011 / (a11 * np.log(b11 / a11))
check("homogeneous coax E(a) = V0/(a ln(b/a)) [V/m]", Emax_h, 182047.8, rtol=1e-6)
# brute force for the homogeneous case: rho_l from V0 = int E dr with E = rho_l/(2 pi eps r)
rl_h = V011 / quad(lambda r: 1 / (2 * pi * 3 * eps0 * r), a11, b11)
check("homogeneous: E(a) from Gauss + quad", rl_h / (2 * pi * 3 * eps0 * a11), Emax_h)
say("ratio of peak fields homogeneous/graded = 2/ln 3", f"{Emax_h / 1e5:.3f}")
check("epsr at a, b", [eps11(a11) / eps0, eps11(b11) / eps0], [6, 2])

# =====================================================================================
print("=" * 88)
print("9.12 Charged sphere floating in oil (a = 10 cm, Q = 30 nC, oil eps_r = 2 in z<0, air z>0)")
a12, Q12, er12 = 0.10, 30e-9, 2.0
A12 = Q12 / (2 * pi * (eps0 + er12 * eps0))
say("A = Q/(2 pi (eps0+eps)) [V m]", f"{A12:.2f}")


def eps12(theta):
    return eps0 if theta < pi / 2 else er12 * eps0


def Dr12(r, theta):
    return eps12(theta) * A12 / r ** 2


# Gauss's law brute force: flux of D (different in each half) over spheres r = 0.3, 1.0
for rr in (0.3, 1.0):
    fl = integrate.dblquad(lambda th, ph: Dr12(rr, th) * rr ** 2 * np.sin(th), 0, 2 * pi, 0, pi,
                           epsabs=1e-20, epsrel=1e-11)[0]
    check(f"flux of D over r={rr} m sphere [nC]", fl * 1e9, 30, rtol=1e-8)
# boundary conditions on the flat oil surface z = 0 (r > a), n = +z from oil (2) into air (1)
for (x, y) in ((0.15, 0.0), (0.3, -0.2), (-0.12, 0.5)):
    rv = np.array([x, y, 0.0]); r = np.linalg.norm(rv); rh = rv / r
    E1 = A12 / r ** 2 * rh; E2 = A12 / r ** 2 * rh
    D1 = eps0 * E1; D2 = er12 * eps0 * E2
    assert np.linalg.norm(np.cross(zhat, E1 - E2)) == 0.0
    check(f"oil surface at ({x},{y}): n.(D1-D2) = 0 and P.n = 0", [np.dot(zhat, D1 - D2), np.dot(D2 - eps0 * E2, zhat)], [0, 0], atol=1e-25)
# metal surface: E normal (radial) and V = A/r constant -> equipotential; Laplace: lap(1/r) = 0 numerically
Ea12 = A12 / a12 ** 2
say("E(a) [kV/m]", f"{Ea12 / 1e3:.2f}")
f_lap = lambda x, y, z: A12 / np.sqrt(x * x + y * y + z * z)
h = 1e-4; p = (0.2, 0.1, -0.05)
lap = sum((f_lap(*(np.array(p) + h * e)) - 2 * f_lap(*p) + f_lap(*(np.array(p) - h * e))) / h ** 2
          for e in np.eye(3))
check("Laplacian of A/r at an oil point, relative to A/r^3 (should be 0)", lap / (A12 / np.linalg.norm(p) ** 3), 0, atol=1e-6)
rs_top, rs_bot = eps0 * Ea12, er12 * eps0 * Ea12
say("free rho_s top, bottom [nC/m^2]", f"{rs_top * 1e9:.1f}, {rs_bot * 1e9:.1f}")
q_top = integrate.dblquad(lambda th, ph: Dr12(a12, th) * a12 ** 2 * np.sin(th), 0, 2 * pi, 0, pi / 2)[0]
q_bot = integrate.dblquad(lambda th, ph: Dr12(a12, th) * a12 ** 2 * np.sin(th), 0, 2 * pi, pi / 2, pi)[0]
check("free charge on upper, lower hemisphere [nC]", [q_top * 1e9, q_bot * 1e9], [10, 20])
# bound charge of the oil where it touches the sphere: n out of the oil = -r-hat
sb12 = np.dot((er12 - 1) * eps0 * Ea12 * nhat, -nhat)
say("bound rho_sb on oil at the sphere [nC/m^2]", f"{sb12 * 1e9:.1f}")
check("bound total on the lower hemisphere [nC]", sb12 * 2 * pi * a12 ** 2 * 1e9, -10)
check("net (free+bound) top = bottom [nC/m^2]", [rs_top * 1e9, (rs_bot + sb12) * 1e9], [rs_top * 1e9] * 2)
check("P_r in oil: r^2 P_r constant -> rho_b = 0", -ddx(lambda s: s ** 2 * (er12 - 1) * eps0 * A12 / s ** 2, 0.4) / 0.16, 0, atol=1e-18)
check("flux of P out through any far oil hemisphere (= +10 nC on the bath's far walls)",
      integrate.dblquad(lambda th, ph: (er12 - 1) * eps0 * A12 * np.sin(th), 0, 2 * pi, pi / 2, pi)[0] * 1e9, 10)
# Brute-force Coulomb superposition: the NET charge on r = a is uniform (10 nC per hemisphere = 20 nC);
# its field at points outside the sphere must equal A/r^2 r-hat everywhere (above and below the oil line).
sig_net = lambda th: (rs_top if th < pi / 2 else rs_bot + sb12)


def coulomb_E(pt):
    pt = np.asarray(pt, float)
    out = np.zeros(3)
    for k in range(3):
        def integrand(th, ph, k=k):
            src = a12 * np.array([np.sin(th) * np.cos(ph), np.sin(th) * np.sin(ph), np.cos(th)])
            R = pt - src
            return sig_net(th) * a12 ** 2 * np.sin(th) * R[k] / (4 * pi * eps0 * np.linalg.norm(R) ** 3)
        out[k] = (integrate.dblquad(integrand, 0, 2 * pi, 0, pi / 2, epsabs=1e-9, epsrel=1e-9)[0]
                  + integrate.dblquad(integrand, 0, 2 * pi, pi / 2, pi, epsabs=1e-9, epsrel=1e-9)[0])
    return out


for pt in ((0.0, 0.0, 0.25), (0.2, 0.05, -0.15), (0.3, 0.1, 0.0)):
    r = np.linalg.norm(pt)
    Eexp = A12 / r ** 2 * np.array(pt) / r
    check(f"Coulomb sum of net surface charge at {pt} = A/r^2 r-hat", coulomb_E(pt), Eexp, rtol=1e-6,
          atol=1e-6 * np.linalg.norm(Eexp))
Vs = quad(lambda r: A12 / r ** 2, a12, np.inf)
check("V(sphere) [V] by quad", Vs, A12 / a12)
V_air = Q12 / (4 * pi * eps0 * a12); V_oil = Q12 / (4 * pi * er12 * eps0 * a12)
say("V(sphere), all-air, all-oil [kV]", f"{Vs / 1e3:.3f}, {V_air / 1e3:.3f}, {V_oil / 1e3:.3f}")
check("V(sphere) = 2/3 of the all-air value", Vs / V_air, 2 / 3)
check("A = (20 nC)/(4 pi eps0): field of the net 20 nC in vacuum", A12, 20e-9 / (4 * pi * eps0))

# =====================================================================================
print("=" * 88)
nfail = sum(1 for _, ok in RESULTS if not ok)
print(f"{len(RESULTS)} checks, {nfail} failed")
if nfail:
    for lab, ok in RESULTS:
        if not ok:
            print("  FAILED:", lab)
