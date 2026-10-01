#!/usr/bin/env python3
"""Independent check of practice page 02 (Coulomb, superposition, Gauss).
numpy/scipy only. Every number on the (fixed) page is transcribed and compared:
PASS/FAIL lines count; 'ORIG-FAIL' lines document values of the original page that were wrong."""
import numpy as np
from scipy import integrate, optimize

eps0 = 8.8541878128e-12
k = 1/(4*np.pi*eps0)
e = 1.602e-19
u = 1.6605e-27
nfail = 0


def tol_of(s):
    s = s.strip().lower().replace('+', '')
    mant, ex = (s.split('e')[0], int(s.split('e')[1])) if 'e' in s else (s, 0)
    dec = len(mant.split('.')[1]) if '.' in mant else 0
    return 0.5*10.0**(-dec)*10.0**ex


def chk(label, computed, stated, unit=1.0, tol=None):
    global nfail
    c = computed/unit
    t = tol if tol is not None else tol_of(stated)*1.000001
    ok = abs(c - float(stated)) <= t
    nfail += (not ok)
    print(f"  {'PASS' if ok else 'FAIL'}  {label}: computed {c:.6g}, page {stated}")


def chkb(label, cond):
    global nfail
    nfail += (not cond)
    print(f"  {'PASS' if cond else 'FAIL'}  {label}")


def orig(label, computed, stated, unit=1.0):
    c = computed/unit
    ok = abs(c - float(stated)) <= tol_of(stated)*1.000001
    print(f"  {'(orig ok)' if ok else 'ORIG-FAIL'}  {label}: computed {c:.6g}, ORIGINAL page {stated}")


def coulombE(Q, rq, r):
    R = np.asarray(r, float) - np.asarray(rq, float)
    return k*Q*R/np.linalg.norm(R)**3


def face_fraction(rq, lo, hi, axis, val, sgn):
    """flux fraction (per unit charge) of a point charge at rq through the cube face coord[axis]=val."""
    rq = np.asarray(rq, float)
    oth = [i for i in range(3) if i != axis]

    def f(b, a):
        p = np.empty(3); p[axis] = val; p[oth[0]] = a; p[oth[1]] = b
        R = p - rq; n = np.linalg.norm(R)
        return 0.0 if n == 0 else sgn*R[axis]/(4*np.pi*n**3)
    return integrate.dblquad(f, lo, hi, lo, hi, epsabs=1e-12, epsrel=1e-10)[0]


def cube_faces(rq, lo, hi):
    out = {}
    for ax, name in enumerate('xyz'):
        out[f'{name}={lo:g}'] = face_fraction(rq, lo, hi, ax, lo, -1)
        out[f'{name}={hi:g}'] = face_fraction(rq, lo, hi, ax, hi, +1)
    return out


def sphere_fraction(rq, c, Rs):
    rq = np.asarray(rq, float); c = np.asarray(c, float)

    def f(th, ph):
        n = np.array([np.sin(th)*np.cos(ph), np.sin(th)*np.sin(ph), np.cos(th)])
        R = c + Rs*n - rq
        return (R @ n)/(4*np.pi*np.linalg.norm(R)**3)*Rs**2*np.sin(th)
    return integrate.dblquad(f, 0, 2*np.pi, 0, np.pi, epsabs=1e-12, epsrel=1e-10)[0]


# ---------------------------------------------------------------- 2.1
print("2.1 Coulomb force as a vector")
Q1, r1, Q2, r2 = 2e-6, np.array([1., 0, 2]), -3e-6, np.array([3., 2, 1])
F2 = Q2*coulombE(Q1, r1, r2)          # force on Q2 = Q2 * (field of Q1 at r2)
F1 = Q1*coulombE(Q2, r2, r1)          # computed separately, not as -F2
R = r2 - r1; Rm = np.linalg.norm(R); Rh = R/Rm
chk("R [m]", Rm, "3", tol=1e-12)
for i, s in enumerate(["-3.99", "-3.99", "2.00"]):
    chk(f"F2_{'xyz'[i]} [mN]", F2[i], s, 1e-3)
chk("|F2| [mN]", np.linalg.norm(F2), "5.99", 1e-3)
chk("scalar Q1Q2/(4 pi eps0 R^2) [mN]", k*Q1*Q2/Rm**2, "-5.99", 1e-3)
for i, s in enumerate(["3.99", "3.99", "-2.00"]):
    chk(f"F1_{'xyz'[i]} [mN]", F1[i], s, 1e-3)
chkb("F1 = -F2 (independent computation)", np.allclose(F1, -F2, rtol=1e-12))
chkb("F2 x Rhat = 0 (along the line)", np.linalg.norm(np.cross(F2, Rh)) < 1e-12*np.linalg.norm(F2))
chk("F2 . Rhat [mN] (negative: attractive)", F2 @ Rh, "-5.99", 1e-3)
chk("quick estimate [mN]", 6e-12*9e9/9, "6", 1e-3, tol=1e-9)
orig("F2_x with the page's quoted 1/(4 pi eps0) = 8.99e9", 8.99e9*Q1*Q2/9*2/3, "-3.99", 1e-3)
chk("F2_x with the fixed quoted constant 8.988e9", 8.988e9*Q1*Q2/9*2/3, "-3.99", 1e-3)
chk("F2_z with 8.988e9", 8.988e9*Q1*Q2/9*(-1/3), "2.00", 1e-3)
chk("scalar with 8.988e9", 8.988e9*Q1*Q2/9, "-5.99", 1e-3)

# ---------------------------------------------------------------- 2.2
print("2.2 null point (units q/(4 pi eps0) per m^2)")
Ex = lambda x: np.sign(x)/x**2 - 4*np.sign(x - 3)/(x - 3)**2
xs = np.linspace(-200, 200, 2_000_001)
xs = xs[(np.abs(xs) > 1e-6) & (np.abs(xs - 3) > 1e-6)]
v = Ex(xs); idx = np.where(np.sign(v[:-1]) != np.sign(v[1:]))[0]
roots = sorted(set(round(optimize.brentq(Ex, xs[i], xs[i+1]), 9) for i in idx
                  if not (xs[i] < 0 < xs[i+1] or xs[i] < 3 < xs[i+1])))
chkb(f"axis scan [-200,200]: exactly one zero, at {roots}", len(roots) == 1 and abs(roots[0] + 3) < 1e-9)
chk("contribution of +q at x=-3", -1/9, str(-1/9), tol=1e-12)
chk("contribution of -4q at x=-3 (computed)", -4*np.sign(-6)/36, str(1/9), tol=1e-12)
chk("E_x(1)", Ex(1.0), "2", tol=1e-12)
chk("E_x(2)", Ex(2.0), "4.25", tol=1e-12)
chk("E_x(6)", Ex(6.0), "-0.417")
chk("E_x(6) exact -5/12", Ex(6.0), str(-5/12), tol=1e-12)


def E3(r):
    r = np.asarray(r, float)
    return r/np.linalg.norm(r)**3 - 4*(r - [3, 0, 0])/np.linalg.norm(r - [3, 0, 0])**3


rng = np.random.default_rng(1); sols = []
for x0 in rng.uniform(-8, 8, (300, 3)):
    s = optimize.root(E3, x0, method='hybr')
    if s.success and np.linalg.norm(s.x) < 50 and np.linalg.norm(E3(s.x)) < 1e-10:
        sols.append(np.round(s.x, 6))
sols = np.unique(np.array(sols), axis=0)
chkb(f"3-D root search: null points {sols.tolist()}", len(sols) == 1 and np.allclose(sols[0], [-3, 0, 0], atol=1e-5))

# ---------------------------------------------------------------- 2.3
print("2.3 charge at a cube corner (Q = 12 nC)")
Q = 12.0  # nC
fr = cube_faces([0, 0, 0], 0, 2)
for f in ['x=0', 'y=0', 'z=0']:
    chk(f"face {f} [nC]", Q*fr[f], "0", tol=1e-8)
for f in ['x=2', 'y=2', 'z=2']:
    chk(f"face {f} [nC]", Q*fr[f], "0.5", tol=1e-8)
chk("whole cube [nC]", Q*sum(fr.values()), "1.5", tol=1e-8)
frc = cube_faces([1, 1, 1], 0, 2)
for f, val in frc.items():
    chk(f"centred charge, face {f} [nC]", Q*val, "2", tol=1e-8)

# ---------------------------------------------------------------- 2.4
print("2.4 velocity selector")
vv, B = np.array([2e5, 0, 0]), np.array([0, 0.25, 0])
vxB = np.cross(vv, B); E = -vxB
chk("(v x B)_z [V/m]", vxB[2], "5e4", tol=1e-6)
chk("E_z [V/m]", E[2], "-5e4", tol=1e-6)
chkb("E has no x, y components", np.allclose(E[:2], 0))
chk("|E| [kV/m]", np.linalg.norm(E), "50", 1e3, tol=1e-9)
chkb("electron at same v: force e(E+vxB) = 0", np.allclose(-e*(E + np.cross(vv, B)), 0))
vp = np.array([4e5, 0, 0]); Fe = e*E; Fm = e*np.cross(vp, B); Fn = Fe + Fm
chk("proton F_E,z [N]", Fe[2], "-8.01e-15")
chk("proton F_B,z [N]", Fm[2], "1.60e-14")
chk("proton net F_z [N]", Fn[2], "8.01e-15")
chkb("net force along +z only", Fn[2] > 0 and np.allclose(Fn[:2], 0))
chk("F_B / F_B(selected speed)", Fm[2]/(e*vxB[2]), "2", tol=1e-12)

# ---------------------------------------------------------------- 2.5
print("2.5 sphere cutting a charged plane")
c5, R5 = [0, 0, 1], 3.0
chk("distance centre -> point charge [m]", np.linalg.norm(np.subtract([0, 0, 5], c5)), "4", tol=1e-12)
chk("flux of the +10 C point charge [C]", 10*sphere_fraction([0, 0, 5], c5, R5), "0", tol=1e-8)
th0 = np.arccos(-1/3)
g = lambda th: 0.5*np.sign(1 + 3*np.cos(th))*np.cos(th)*R5**2*np.sin(th)*2*np.pi
sheet = -3*integrate.quad(g, 0, np.pi, points=[th0], epsabs=1e-13)[0]
chk("flux of the sheet field over the sphere [C]", sheet, "-75.4")
chk("same, in units of pi C", sheet/np.pi, "-24", tol=1e-8)
area = integrate.quad(lambda x: 2*np.sqrt(max(0.0, R5**2 - 1 - x*x)), -3, 3, points=[-8**0.5, 8**0.5])[0]
chk("area of plane inside sphere / pi [m^2]", area/np.pi, "8", tol=1e-7)
chk("disk radius [m]", np.sqrt(R5**2 - 1), "2.83")
print(f"  info: distractors (a) {-27*np.pi:.1f} C, (c) {10-24*np.pi:.1f} C, (d) {-12*np.pi:.1f} C")

# ---------------------------------------------------------------- 2.6
print("2.6 ring on its axis")
a6, rl6, N = 0.1, 5e-9, 20000
ph = (np.arange(N) + 0.5)*2*np.pi/N
src = np.stack([a6*np.cos(ph), a6*np.sin(ph), 0*ph], 1); dQ = rl6*a6*2*np.pi/N


def Ering(z):
    Rv = np.array([0, 0, z]) - src
    return k*dQ*(Rv/np.linalg.norm(Rv, axis=1)[:, None]**3).sum(0)


Qr = 2*np.pi*a6*rl6
chk("Q [nC]", Qr, "3.14", 1e-9)
chk("Q/(4 pi eps0) [V m]", k*Qr, "28.2")
E01, E1 = Ering(0.1), Ering(1.0)
chk("E_z(10 cm) [V/m]", E01[2], "998")
chk("E_z(1 m) [V/m]", E1[2], "27.8")
chkb("E_x, E_y = 0 on axis", np.abs(E01[:2]).max() < 1e-9*abs(E01[2]))
chk("point charge at 1 m [V/m]", k*Qr/1.0, "28.2")
chk("point/ring - 1 at 1 m [%]", 100*(k*Qr/E1[2] - 1), "1.5")
opt = optimize.minimize_scalar(lambda z: -Ering(z)[2], bounds=(0.01, 0.5), method='bounded',
                               options={'xatol': 1e-9})
chk("z of max (numerical) [cm]", opt.x, "7.07", 1e-2)
chk("E_max (numerical) [V/m]", -opt.fun, "1087")
chk("E_max = rho_l/(3 sqrt3 eps0 a) [V/m]", rl6/(3*np.sqrt(3)*eps0*a6), "1087")
chk("2/(3 sqrt3)", 2/(3*np.sqrt(3)), "0.385")
chk("E_z(-10 cm) [V/m] (odd)", Ering(-0.1)[2], "-998")
chk("E_z(0) [V/m]", Ering(0.0)[2], "0", tol=1e-6)

# ---------------------------------------------------------------- 2.7
print("2.7 semicircular arc")
a7, rl7 = 0.05, 2e-9
ph = (np.arange(N) + 0.5)*np.pi/N
src7 = np.stack([a7*np.cos(ph), a7*np.sin(ph), 0*ph], 1)
Rv = -src7
E7 = k*rl7*a7*np.pi/N*(Rv/np.linalg.norm(Rv, axis=1)[:, None]**3).sum(0)
chk("E_x at origin [V/m]", E7[0], "0", tol=1e-6)
chk("E_y at origin [V/m]", E7[1], "-719")
chk("student's rho_l/(4 eps0 a) [V/m]", rl7/(4*eps0*a7), "1129")
chk("ratio student/true", rl7/(4*eps0*a7)/abs(E7[1]), "1.57")
Einf = integrate.quad(lambda z: k*rl7*a7/(a7**2 + z*z)**1.5, -np.inf, np.inf, epsabs=1e-10)[0]
chk("infinite line at distance a (quad) [V/m]", Einf, "719")
chkb("sum of |dE| (1129) exceeds |E|", rl7/(4*eps0*a7) > np.linalg.norm(E7))

# ---------------------------------------------------------------- 2.8
print("2.8 dipole")
Q8, d = 3e-9, 4e-3
rm, rp = np.array([0, 0, d/2]), np.array([0, 0, -d/2])
p = Q8*(rp - rm)
chk("p_z [C m]", p[2], "-1.2e-11", tol=1e-20)
Edip = lambda r: coulombE(-Q8, rm, r) + coulombE(Q8, rp, r)
D = 0.02; P1, P2 = np.array([0, 0, D]), np.array([D, 0, 0])
chk("Q/(4 pi eps0) [V m]", k*Q8, "27.0")
chk("|E from -Q| at P1 [V/m]", coulombE(-Q8, rm, P1)[2], "-8.32e4")
chk("E from +Q at P1 [V/m]", coulombE(Q8, rp, P1)[2], "5.57e4")
Ea, Eb = Edip(P1), Edip(P2)
chk("E_z(P1) [V/m]", Ea[2], "-2.75e4")
chk("E_z(P2) [V/m]", Eb[2], "1.33e4")
chkb("E(P1), E(P2) have no x, y parts", np.abs(Ea[:2]).max() < 1e-9 and abs(Eb[0]) < 1e-9*abs(Eb[2]))
Fa, Fb = 2*k*p/D**3, -k*p/D**3
chk("far-field axis [V/m]", Fa[2], "-2.70e4")
chk("far-field bisector [V/m]", Fb[2], "1.35e4")
chk("axis: (|exact|-|far|)/|exact| [%]", 100*(abs(Ea[2]) - abs(Fa[2]))/abs(Ea[2]), "2.0")
chk("bisector: (|far|-|exact|)/|exact| [%]", 100*(abs(Fb[2]) - abs(Eb[2]))/abs(Eb[2]), "1.5")
chk("ratio axis/bisector at 2 cm", Ea[2]/Eb[2], "-2.07")
chk("ratio at D = 0.5 m", -Edip([0, 0, 0.5])[2]/Edip([0.5, 0, 0])[2], "2.0001")
print(f"  info: E_axis(4 cm)/E_axis(2 cm) = {Edip([0,0,0.04])[2]/Ea[2]:.4f} (1/8 = 0.125)")
rel = lambda DD: (Edip([0, 0, DD])[2] - 2*k*p[2]/DD**3)/Edip([0, 0, DD])[2]
Dst = optimize.brentq(lambda DD: rel(DD) - 0.01, 2*d, 50*d, xtol=1e-14)
chk("1% distance (exact) [d]", Dst/d, "7.06")
chk("1% distance (exact) [cm]", Dst, "2.82", 1e-2)
chk("first-order estimate 1/sqrt(0.02) [d]", 1/np.sqrt(0.02), "7.07")
chkb("E(P1) parallel to p, E(P2) antiparallel", Ea @ p > 0 and Eb @ p < 0)

# ---------------------------------------------------------------- 2.9
print("2.9 finite line charge")
rl9 = 60*np.pi*eps0
chk("rho_l [nC/m]", rl9, "1.67", 1e-9)
chk("rho_l/(4 pi eps0) [V]", k*rl9, "15", tol=1e-9)


def Eseg(rho, z1, z2, P):
    P = np.asarray(P, float)
    def comp(i):
        f = lambda zp: k*rho*(P - [0, 0, zp])[i]/np.linalg.norm(P - [0, 0, zp])**3
        return integrate.quad(f, z1, z2, epsabs=1e-12, epsrel=1e-12, limit=400)[0]
    return np.array([comp(i) for i in range(3)])


def Eform(rho, z1, z2, r, z):
    h1, h2 = np.hypot(r, z1 - z), np.hypot(r, z2 - z)
    return k*rho/r*((z2 - z)/h2 - (z1 - z)/h1), k*rho/r*(r/h2 - r/h1)


P = [3, 0, 0]
Eb9 = Eseg(rl9, 0, 4, P)
chk("E_x(P) brute force [V/m]", Eb9[0], "4", tol=1e-9)
chk("E_z(P) brute force [V/m]", Eb9[2], "-2", tol=1e-9)
chk("|E| [V/m]", np.linalg.norm(Eb9), "4.47")
chk("angle below +x [deg]", np.degrees(np.arctan2(-Eb9[2], Eb9[0])), "26.6")
for (z1, z2, r, phi, z) in [(-1.5, 2.5, 2.0, 40, 0.7), (-1.5, 2.5, 2.0, 40, 4.0), (0, 4, 3, 0, 0)]:
    Pg = [r*np.cos(np.radians(phi)), r*np.sin(np.radians(phi)), z]
    Eg = Eseg(rl9, z1, z2, Pg)
    Er = Eg @ [np.cos(np.radians(phi)), np.sin(np.radians(phi)), 0]
    Ep = Eg @ [-np.sin(np.radians(phi)), np.cos(np.radians(phi)), 0]
    fr_, fz_ = Eform(rl9, z1, z2, r, z)
    chkb(f"formula (a) vs brute force, segment [{z1},{z2}], (r,phi,z)=({r},{phi},{z})",
         abs(Er - fr_) < 1e-9 and abs(Eg[2] - fz_) < 1e-9 and abs(Ep) < 1e-9)
u1 = (np.array([0, 0, 0]) - P)/3.0; u2 = (np.array([0, 0, 4]) - P)/5.0; sb = u1 + u2
chkb(f"bisector direction {sb.tolist()} = (-1.6, 0, 0.8)", np.allclose(sb, [-1.6, 0, 0.8]))
chkb("bisector x E = 0", np.linalg.norm(np.cross(sb, Eb9)) < 1e-9)
chk("bisector . E", sb @ Eb9, "-8", tol=1e-9)
Esemi = Eseg(rl9, 0, np.inf, P)
chk("semi-infinite E_x [V/m]", Esemi[0], "5", tol=1e-8)
chk("semi-infinite E_z [V/m]", Esemi[2], "-5", tol=1e-8)
Eadd = Eseg(rl9, 4, np.inf, P)
chk("added piece E_x [V/m]", Eadd[0], "1", tol=1e-8)
chk("added piece E_z [V/m]", Eadd[2], "-3", tol=1e-8)
Einf9 = Eseg(rl9, -np.inf, np.inf, P)
chk("infinite E_x [V/m]", Einf9[0], "10", tol=1e-8)
chk("infinite E_z [V/m]", Einf9[2], "0", tol=1e-8)
chk("rho_l/(2 pi eps0 r) [V/m]", rl9/(2*np.pi*eps0*3), "10", tol=1e-9)
E45 = Eseg(rl9, 0, np.inf, [7, 0, 0])
chkb("semi-infinite line: |E_r| = |E_z| opposite its end (r = 7 m)", abs(E45[0] + E45[2]) < 1e-9)
chk("Q_enc = 4 rho_l [nC]", 4*rl9, "6.68", 1e-9)
for zz, (sr, sz) in [(-1, ("2.71", "-2.17")), (2, ("5.55", "0")), (5, ("2.71", "2.17"))]:
    Es = Eseg(rl9, 0, 4, [3, 0, zz])
    chk(f"side z={zz}: E_r [V/m]", Es[0], sr)
    chk(f"side z={zz}: E_z [V/m]", Es[2], sz, tol=(1e-9 if sz == "0" else None))
side = integrate.quad(lambda z: eps0*Eseg(rl9, 0, 4, [3, 0, z])[0]*2*np.pi*3, -1, 5, epsrel=1e-10)[0]
top = integrate.quad(lambda r: eps0*Eseg(rl9, 0, 4, [r, 0, 5])[2]*2*np.pi*r, 0, 3, epsrel=1e-10)[0]
bot = integrate.quad(lambda r: -eps0*Eseg(rl9, 0, 4, [r, 0, -1])[2]*2*np.pi*r, 0, 3, epsrel=1e-10)[0]
chk("flux through side [nC]", side, "4.45", 1e-9)
chk("flux through top cap [nC]", top, "1.11", 1e-9)
chk("flux through bottom cap [nC]", bot, "1.11", 1e-9)
chk("total flux [nC]", side + top + bot, "6.68", 1e-9)

# ---------------------------------------------------------------- 2.10
print("2.10 disk and annulus on axis")
a10, rs, b10 = 0.3, -5e-6, 0.1


def Ez_cart(z, a, b=0.0):
    """brute-force Cartesian 2-D Coulomb integral over the annulus b<r'<a (b=0: full disk)."""
    f = lambda yp, xp: z/(xp*xp + yp*yp + z*z)**1.5
    kw = dict(epsabs=1e-12, epsrel=1e-11)
    t = 2*integrate.dblquad(f, b, a, lambda x: -np.sqrt(a*a - x*x), lambda x: np.sqrt(a*a - x*x), **kw)[0]
    if b > 0:
        t += 2*integrate.dblquad(f, -b, b, lambda x: np.sqrt(b*b - x*x), lambda x: np.sqrt(a*a - x*x), **kw)[0]
    return k*rs*t


chk("rho_s/(2 eps0) [V/m]", rs/(2*eps0), "-2.82e5")
chk("z/sqrt(z^2+a^2) at 1 cm", 0.01/np.hypot(0.01, a10), "0.0333")
E1c = Ez_cart(0.01, a10)
chk("E_z(1 cm) [V/m]", E1c, "-2.73e5")
chk("E_z(-1 cm) [V/m] (toward disk from below)", Ez_cart(-0.01, a10), "2.73e5")
chk("sheet/disk - 1 at 1 cm [%]", 100*(rs/(2*eps0)/E1c - 1), "3.4")
chk("1 - z/sqrt(z^2+a^2) at 3 m", 1 - 3/np.hypot(3, a10), "0.00496")
E3m = Ez_cart(3.0, a10)
chk("E_z(3 m) [V/m]", E3m, "-1401")
Qd = np.pi*a10**2*rs
chk("Q [uC]", Qd, "-1.41", 1e-6)
chk("point charge at 3 m [V/m]", k*Qd/9, "-1412")
chk("point/disk - 1 at 3 m [%]", 100*(k*Qd/9/E3m - 1), "0.75")
zh = optimize.brentq(lambda z: Ez_cart(z, a10) - 0.5*rs/(2*eps0), 0.02, 1.0, xtol=1e-10)
chk("half-field height (brute force) [cm]", zh, "17.3", 1e-2)
chk("a/sqrt3 [cm]", a10/np.sqrt(3), "17.3", 1e-2)
print(f"  info: brute-force E_z(1e-4 m)/(rho_s/2eps0) = {Ez_cart(1e-4, a10)/(rs/(2*eps0)):.5f}")
Ean = Ez_cart(0.1, a10, b10)
chk("annulus E_z(10 cm) [V/m]", Ean, "-1.10e5")
chk("z/sqrt(z^2+b^2) at 10 cm", 0.1/np.hypot(0.1, b10), "0.707")
chk("z/sqrt(z^2+a^2) at 10 cm", 0.1/np.hypot(0.1, a10), "0.316")
chk("full disk E_z(10 cm) [V/m]", Ez_cart(0.1, a10), "-1.93e5")
chk("removed disk (radius b, +rho_s) E_z(10 cm) [V/m]", Ez_cart(0.1, b10), "-8.27e4")
chk("annulus E_z(0.1 mm) [V/m] (-> 0)", Ez_cart(1e-4, a10, b10), "0", tol=1e3)
chk("jump rho_s/eps0 [V/m]", rs/eps0, "-5.65e5")

# ---------------------------------------------------------------- 2.11
print("2.11 boron mass spectrometer")
E0, B1m, B2m = 4e4, 0.10, 0.5
Ev = np.array([E0, 0, 0]); vs = E0/B1m
chk("selected speed [m/s]", vs, "4e5", tol=1e-6)
for sgn in (+1, -1):
    F = e*(Ev + np.cross([0, vs, 0], [0, 0, sgn*B1m]))
    if sgn > 0:
        chk("B1 = +z: force on a +e ion at 4e5 m/s, F_x [N]", F[0], "1.28e-14")
    else:
        chkb("B1 = -z: force zero at 4e5 m/s", np.allclose(F, 0, atol=1e-30))
B1v = np.array([0, 0, -B1m])
vf = np.array([0, 1.1*vs, 0])
chk("fast ion F_E,x [N]", e*E0, "6.41e-15")
chk("fast ion F_B,x [N]", e*np.cross(vf, B1v)[0], "-7.05e-15")
chk("fast ion net F_x [N]", e*(Ev + np.cross(vf, B1v))[0], "-6.41e-16")
chkb("slow ion (0.9 v) net F_x > 0", e*(Ev + np.cross(0.9*vf/1.1, B1v))[0] > 0)
B2v = np.array([0, 0, B2m])
chkb("initial analyzer force along +x", np.allclose(np.cross([0, 1, 0], B2v)/B2m, [1, 0, 0]))


def fly(m, q):
    rhs = lambda t, s: [s[2], s[3], q/m*s[3]*B2m, -q/m*s[2]*B2m]
    ev = lambda t, s: s[1]
    ev.terminal, ev.direction = True, -1
    sol = integrate.solve_ivp(rhs, [0, 1e-5], [0, 0, 0, vs], method='DOP853', events=ev,
                              rtol=1e-12, atol=[1e-15, 1e-15, 1e-7, 1e-7], max_step=1e-9)
    se = sol.y_events[0][0]
    return se[0], sol.t_events[0][0], np.hypot(se[2], se[3]), sol.y[0].max(), sol.y[0].min()


tab = {"10B+": (10*u, e, "8.29", "16.58", "0.651"), "11B+": (11*u, e, "9.12", "18.24", "0.716"),
       "11B2+": (11*u, 2*e, "4.56", "9.12", "0.358")}
land = {}
for name, (m, q, sR, sx, st) in tab.items():
    xl, tl, vend, xmax, _ = fly(m, q)
    land[name] = xl
    chk(f"{name} R = mv/(qB) [cm]", m*vs/(q*B2m), sR, 1e-2)
    chk(f"{name} R from ODE (max x / 2) [cm]", xmax/2, sR, 1e-2)
    chk(f"{name} landing x (ODE) [cm]", xl, sx, 1e-2)
    chk(f"{name} time (ODE) [us]", tl, st, 1e-6)
    chk(f"{name} speed at landing [m/s]", vend, "4e5", tol=1e-2)
# sense of rotation: L_z about the centre (R,0) at t = 0 is (0-R)*v - 0 < 0 -> clockwise from +z
chkb("clockwise seen from +z (L_z about centre < 0)", (0 - 0.0829)*vs < 0)
chk("10B+/11B+ spot separation (ODE) [cm]", land["11B+"] - land["10B+"], "1.66", 1e-2)
chk("m/q of 11B2+ [u/e]", (11*u/(2*e))/(u/e), "5.5", tol=1e-12)
chk("11B+ kinetic energy [keV]", 0.5*11*u*vs**2/e/1e3, "9.12")
xneg = fly(11*u, -e)
chkb(f"negative 11B- would curve to -x and land at x = -2R = {xneg[0]*100:.2f} cm (min x {xneg[4]*100:.2f})",
     abs(xneg[0] + 2*11*u*vs/(e*B2m)) < 1e-8)

# ---------------------------------------------------------------- 2.12
print("2.12 two charges, one given field")
Q1v = 3*4/k
chk("Q1 [pi eps0]", Q1v/(np.pi*eps0), "48", tol=1e-9)
chk("Q1 [nC]", Q1v, "1.34", 1e-9)
chkb("field of Q1 at origin = -3 z", np.allclose(coulombE(Q1v, [0, 0, 2], [0, 0, 0]), [0, 0, -3]))
Q2m = 16*np.pi*eps0
found = []
for sgn in (+1, -1):
    res = lambda X: coulombE(sgn*Q2m, [X, 0, 0], [0, 0, 0])[0] + 4
    Xs = np.linspace(-50, 50, 200001); Xs = Xs[np.abs(Xs) > 1e-9]
    rv = np.array([res(X) for X in Xs[::50]]); Xc = Xs[::50]
    for i in np.where(np.sign(rv[:-1]) != np.sign(rv[1:]))[0]:
        if Xc[i] < 0 < Xc[i+1]:
            continue
        X0 = optimize.brentq(res, Xc[i], Xc[i+1], xtol=1e-14)
        Et = coulombE(Q1v, [0, 0, 2], [0, 0, 0]) + coulombE(sgn*Q2m, [X0, 0, 0], [0, 0, 0])
        if np.allclose(Et, [-4, 0, -3], atol=1e-9):
            found.append((sgn, round(X0, 9)))
found = sorted(set(found))
chkb(f"all (sign, X) solutions: {found}", found == [(-1, -1.0), (1, 1.0)])
chk("|E| total [V/m]", np.hypot(4, 3), "5", tol=1e-12)
chk("+16 pi eps0 at x=-1 gives E_x [V/m]", coulombE(Q2m, [-1, 0, 0], [0, 0, 0])[0], "4", tol=1e-9)
rA, rB = np.array([0, 0, 2.]), np.array([1, 0, 0.])
Ef = lambda r: coulombE(Q1v, rA, r) + coulombE(Q2m, rB, r)
sols = []
for x0 in np.random.default_rng(2).uniform(-3, 3, (400, 3)):
    s = optimize.root(Ef, x0, method='hybr')
    scale = np.linalg.norm(coulombE(Q1v, rA, s.x)) + np.linalg.norm(coulombE(Q2m, rB, s.x))
    if s.success and np.linalg.norm(s.x) < 50 and np.linalg.norm(Ef(s.x)) < 1e-9*scale:
        sols.append(np.round(s.x, 7))
sols = np.unique(np.array(sols), axis=0)
chkb(f"null points from 400 starts: {sols.tolist()}", len(sols) == 1)
r0 = sols[0]
chk("x0 [m]", r0[0], "0.634"); chk("y0 [m]", r0[1], "0", tol=1e-6); chk("z0 [m]", r0[2], "0.732")
chk("x0 vs (3-sqrt3)/2", r0[0], str((3 - np.sqrt(3))/2), tol=1e-6)
chk("z0 vs sqrt3-1", r0[2], str(np.sqrt(3) - 1), tol=1e-6)
d1, d2 = np.linalg.norm(r0 - rA), np.linalg.norm(r0 - rB)
chk("segment length [m]", np.linalg.norm(rA - rB), "2.24")
chk("d2 [m]", d2, "0.818"); chk("d1 [m]", d1, "1.42"); chk("d1/d2", d1/d2, "1.73")
chk("sphere: flux of Q2 [nC]", Q2m*sphere_fraction(rB, [0, 0, 0], 1.5), "0.445", 1e-9)
chk("sphere: flux of Q1 [nC]", Q1v*sphere_fraction(rA, [0, 0, 0], 1.5), "0", 1e-9, tol=1e-9)
f2 = cube_faces(rB, 0, 1); f1 = cube_faces(rA, 0, 1)
for f in ['x=0', 'y=1', 'z=1']:
    chk(f"cube face {f}: flux of Q2 [pC]", Q2m*f2[f], "18.5", 1e-12)
for f in ['x=1', 'y=0', 'z=0']:
    chk(f"cube face {f}: flux of Q2 [pC]", Q2m*f2[f], "0", 1e-12, tol=1e-6)
chk("cube total, Q2 [pC]", Q2m*sum(f2.values()), "55.6", 1e-12)
chk("cube total, Q2 [pi eps0]", Q2m*sum(f2.values())/(np.pi*eps0), "2", tol=1e-7)
chk("cube total, Q1 (outside) [pC]", Q1v*sum(f1.values()), "0", 1e-12, tol=1e-6)

print(f"\n{'ALL PASS' if nfail == 0 else f'{nfail} FAIL(S)'}")
