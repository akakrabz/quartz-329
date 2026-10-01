#!/usr/bin/env python3
"""Numerical verification for content-src/practice/02-coulombs-law-superposition-and-gauss.md

numpy + scipy only.  For every problem the closed form used on the page is evaluated and
compared with an independent brute-force computation (direct superposition sum, numerical
line/surface integral, ODE integration, root finding).  Every number, sign and direction that
appears on the page is printed below with a label.
"""
import numpy as np
from scipy import integrate, optimize

eps0 = 8.8541878128e-12
mu0 = 4e-7 * np.pi
e = 1.602176634e-19
me = 9.1093837e-31
c = 2.99792458e8
k = 1.0 / (4 * np.pi * eps0)          # 1/(4 pi eps0)
u = 1.6605e-27                         # atomic mass unit as stated on the page

np.set_printoptions(precision=6, suppress=False)
NFAIL = 0


def hdr(s):
    print("\n" + "=" * 78 + "\n" + s + "\n" + "=" * 78)


def show(label, val, unit=""):
    if isinstance(val, (list, tuple, np.ndarray)):
        v = np.asarray(val, float)
        print(f"  {label:58s} = [{', '.join(f'{x:.6g}' for x in v)}] {unit}")
    else:
        print(f"  {label:58s} = {val:.6g} {unit}")


def chk(label, a, b, rtol=1e-6, atol=1e-12):
    global NFAIL
    a = np.asarray(a, float)
    b = np.asarray(b, float)
    ok = np.allclose(a, b, rtol=rtol, atol=atol)
    tag = "OK " if ok else "FAIL"
    if not ok:
        NFAIL += 1
    print(f"  [{tag}] {label}: {np.array2string(np.atleast_1d(a), precision=7)}  vs  "
          f"{np.array2string(np.atleast_1d(b), precision=7)}")


def E_point(Q, rq, r):
    """Coulomb field of Q at rq, evaluated at r (vector, V/m)."""
    R = np.asarray(r, float) - np.asarray(rq, float)
    Rm = np.linalg.norm(R)
    return k * Q * R / Rm ** 3


def D_point(Q, rq, r):
    return eps0 * E_point(Q, rq, r)


# =============================================================================
hdr("Constants used on the page")
show("eps0", eps0, "F/m")
show("1/(4 pi eps0)", k, "m/F")
show("e", e, "C")
show("u (atomic mass unit, as stated in 2.11)", u, "kg")

# =============================================================================
hdr("2.1  Coulomb force as a vector")
Q1, r1 = 2e-6, np.array([1.0, 0.0, 2.0])
Q2, r2 = -3e-6, np.array([3.0, 2.0, 1.0])
R = r2 - r1
Rm = np.linalg.norm(R)
Rhat = R / Rm
show("R = r2 - r1 (from Q1 to Q2)", R, "m")
show("|R|", Rm, "m")
show("|R|^2", Rm ** 2, "m^2")
show("R-hat * 3", 3 * Rhat)
coef = k * Q1 * Q2 / Rm ** 2
show("Q1 Q2 /(4 pi eps0 R^2)", coef * 1e3, "mN")
F2 = Q2 * E_point(Q1, r1, r2)            # brute force: q E of the other charge
F1 = Q1 * E_point(Q2, r2, r1)
chk("F2 closed form vs q*E(other)", coef * Rhat, F2, rtol=1e-12)
show("F2 (force on Q2)", F2 * 1e3, "mN")
show("|F2|", np.linalg.norm(F2) * 1e3, "mN")
show("F1 (force on Q1)", F1 * 1e3, "mN")
chk("F1 + F2 = 0 (Newton 3)", F1 + F2, np.zeros(3), atol=1e-15)
show("F2 . R-hat  (<0 means toward Q1: attractive)", F2 @ Rhat * 1e3, "mN")
show("|Q1 Q2|", abs(Q1 * Q2), "C^2")
show("estimate with 1/(4 pi eps0) ~ 9e9: |F|", 6e-12 * 9e9 / 9 * 1e3, "mN")

# =============================================================================
hdr("2.2  Null point of +q at x=0 and -4q at x=3 m (units: k q = 1)")
charges = [(1.0, 0.0), (-4.0, 3.0)]


def Ex_line(x):
    return sum(Q * np.sign(x - xq) / (x - xq) ** 2 for Q, xq in charges)


roots = []
for lo_, hi_ in [(-200.0, -1e-6), (1e-6, 3 - 1e-6), (3 + 1e-6, 200.0)]:
    xs = np.linspace(lo_, hi_, 400001)
    f = Ex_line(xs)
    idx = np.where(np.sign(f[:-1]) * np.sign(f[1:]) < 0)[0]
    for i in idx:
        roots.append(optimize.brentq(Ex_line, xs[i], xs[i + 1]))
    print(f"  region ({lo_:g}, {hi_:g}): sign changes found = {len(idx)}")
show("all zeros of E_x on the x axis", roots, "m")
chk("unique null point", roots, [-3.0], rtol=1e-9)
show("field of +q at x=-3 (units kq)", -1 / 9)
show("field of -4q at x=-3 (units kq)", 4 / 36)
for xt in (1.0, 2.0, 6.0):
    show(f"E_x at distractor x = {xt:g} m (units kq/m^2)", Ex_line(xt))
# x=1 is the other root of (3-x)^2 = 4 x^2 :
show("roots of (3-x)^2 = 4x^2", np.roots([3, 6, -9]))

# =============================================================================
hdr("2.3  Point charge at a cube corner")


def box_face_fluxes(Q, rq, lo, hi):
    """Outward flux of D of a point charge Q at rq through the six faces of a box."""
    rq = np.asarray(rq, float)
    out = {}
    for ax in range(3):
        o = [i for i in range(3) if i != ax]
        for side, val, sgn in (("lo", lo[ax], -1.0), ("hi", hi[ax], +1.0)):
            def f(t, s, ax=ax, o=o, val=val, sgn=sgn):
                p = np.zeros(3)
                p[ax], p[o[0]], p[o[1]] = val, s, t
                Rv = p - rq
                Rn = np.linalg.norm(Rv)
                if Rn < 1e-14:
                    return 0.0
                return sgn * Q * Rv[ax] / (4 * np.pi * Rn ** 3)
            v, _ = integrate.dblquad(f, lo[o[0]], hi[o[0]], lo[o[1]], hi[o[1]],
                                     epsabs=1e-15, epsrel=1e-11)
            out["xyz"[ax] + "=" + f"{val:g}"] = v
    return out


Q = 12e-9
a = 2.0
fl = box_face_fluxes(Q, [0, 0, 0], [0, 0, 0], [a, a, a])
for kf, v in fl.items():
    show(f"corner charge: flux through face {kf}", v * 1e9, "nC")
tot = sum(fl.values())
chk("total outward flux = Q/8", tot, Q / 8, rtol=1e-8)
chk("far face x=2 = Q/24", fl["x=2"], Q / 24, rtol=1e-8)
show("Q/8", Q / 8 * 1e9, "nC")
show("Q/24", Q / 24 * 1e9, "nC")
fl_c = box_face_fluxes(Q, [1, 1, 1], [0, 0, 0], [a, a, a])
for kf, v in fl_c.items():
    show(f"centred charge: flux through face {kf}", v * 1e9, "nC")
chk("centred: each face = Q/6", list(fl_c.values()), [Q / 6] * 6, rtol=1e-8)
show("Q/6", Q / 6 * 1e9, "nC")
# second parameter set: different size and charge
fl2 = box_face_fluxes(-5.0, [0, 0, 0], [0, 0, 0], [0.3, 0.3, 0.3])
chk("2nd set (Q=-5 C, side 0.3 m): far face = Q/24", fl2["z=0.3"], -5.0 / 24, rtol=1e-8)

# =============================================================================
hdr("2.4  Velocity selector")
v = np.array([2e5, 0, 0])
B = np.array([0, 0.25, 0])
vxB = np.cross(v, B)
show("v x B", vxB, "V/m")
Esel = -vxB
show("E = -v x B", Esel, "V/m")
show("|E| = vB", np.linalg.norm(Esel), "V/m")
for name, q in (("proton", e), ("electron", -e)):
    F = q * (Esel + np.cross(v, B))
    chk(f"force on {name} at the selected speed", F, np.zeros(3), atol=1e-30)
vfast = np.array([4e5, 0, 0])
F = e * (Esel + np.cross(vfast, B))
show("force on proton at 4e5 m/s", F, "N")
show("  electric part qE", e * Esel, "N")
show("  magnetic part q v x B", e * np.cross(vfast, B), "N")

# =============================================================================
hdr("2.5  Sphere (R=3 m, centre (0,0,1)) cutting the charged plane z=0, rho_s=-3 C/m^2")
rho_s, Rs, c0 = -3.0, 3.0, np.array([0, 0, 1.0])
r_cut = np.sqrt(Rs ** 2 - 1.0)
show("radius of the circle cut from the plane", r_cut, "m")
show("r_cut^2", r_cut ** 2, "m^2")
Qenc = rho_s * np.pi * r_cut ** 2
show("Q_enc = rho_s * pi * 8", Qenc, "C")
show("Q_enc / pi", Qenc / np.pi, "C")


def sphere_flux(Dfun, centre, Rad, th_split=None):
    def f(ph, th):
        n = np.array([np.sin(th) * np.cos(ph), np.sin(th) * np.sin(ph), np.cos(th)])
        p = centre + Rad * n
        return Dfun(p) @ n * Rad ** 2 * np.sin(th)
    edges = [0.0] + ([th_split] if th_split is not None else []) + [np.pi]
    tot_ = 0.0
    for t0, t1 in zip(edges[:-1], edges[1:]):
        v_, _ = integrate.dblquad(f, t0, t1, 0, 2 * np.pi, epsabs=1e-12, epsrel=1e-10)
        tot_ += v_
    return tot_


th0 = np.arccos(-1.0 / 3.0)           # where the sphere meets z = 0
flux_sheet = sphere_flux(lambda p: np.array([0, 0, 0.5 * rho_s * np.sign(p[2])]), c0, Rs, th0)
chk("flux of the (infinite) sheet's D through the sphere = rho_s*8*pi", flux_sheet, Qenc, rtol=1e-8)
flux_pt = sphere_flux(lambda p: D_point(10.0, [0, 0, 5.0], p), c0, Rs)
show("flux of the +10 C charge at (0,0,5) (outside)", flux_pt, "C")
show("distance of +10 C charge from the centre", np.linalg.norm(np.array([0, 0, 5.0]) - c0), "m")
show("answer (b) -24 pi", -24 * np.pi, "C")
show("distractor (a) -27 pi", -27 * np.pi, "C")
show("distractor (c) 10 - 24 pi", 10 - 24 * np.pi, "C")
show("distractor (d) -12 pi", -12 * np.pi, "C")

# =============================================================================
hdr("2.6  Ring of charge on its axis")


def ring_E_numeric(rho_l, a_, p):
    p = np.asarray(p, float)
    def comp(phi, i):
        rp = np.array([a_ * np.cos(phi), a_ * np.sin(phi), 0.0])
        Rv = p - rp
        return k * rho_l * a_ * Rv[i] / np.linalg.norm(Rv) ** 3
    scale = abs(k * rho_l / a_)          # natural field scale; zero components need an absolute tolerance
    return np.array([integrate.quad(comp, 0, 2 * np.pi, args=(i,), epsabs=1e-10 * scale, epsrel=1e-12,
                                    limit=200)[0] for i in range(3)])


def ring_Ez(rho_l, a_, z):
    return rho_l * a_ * z / (2 * eps0 * (a_ ** 2 + z ** 2) ** 1.5)


rl, ar = 5e-9, 0.10
Qr = 2 * np.pi * ar * rl
show("Q = 2 pi a rho_l", Qr * 1e9, "nC")
show("Q/(4 pi eps0)", k * Qr, "V m")
for (rl_, a_, zs) in ((rl, ar, (0.1, 1.0, -0.05, 0.0)), (-3e-9, 0.25, (0.07, -0.4, 2.0))):
    for z in zs:
        En = ring_E_numeric(rl_, a_, [0, 0, z])
        chk(f"ring rho_l={rl_:g}, a={a_:g}: E at z={z:g} (closed form vs integral)",
            [0, 0, ring_Ez(rl_, a_, z)], En, rtol=1e-9, atol=1e-9)
show("E_z at z = 10 cm", ring_Ez(rl, ar, 0.1), "V/m")
show("E_z at z = 1 m", ring_Ez(rl, ar, 1.0), "V/m")
show("point-charge estimate at z = 1 m", k * Qr / 1.0, "V/m")
show("relative error of point estimate at 1 m (%)", (k * Qr / 1.0 / ring_Ez(rl, ar, 1.0) - 1) * 100)
res = optimize.minimize_scalar(lambda z: -ring_Ez(rl, ar, z), bounds=(1e-4, 1.0), method="bounded",
                               options={"xatol": 1e-12})
show("z of maximum (numerical)", res.x, "m")
chk("z_max = a/sqrt(2)", res.x, ar / np.sqrt(2), rtol=1e-6)
Emax = rl / (3 * np.sqrt(3) * eps0 * ar)
chk("E_max = rho_l/(3 sqrt3 eps0 a)", Emax, ring_Ez(rl, ar, res.x), rtol=1e-9)
show("E_max", Emax, "V/m")
show("2/(3 sqrt 3)", 2 / (3 * np.sqrt(3)))
# derivative check of the maximum condition by finite difference
h = 1e-7
dEdz = (ring_Ez(rl, ar, ar / np.sqrt(2) + h) - ring_Ez(rl, ar, ar / np.sqrt(2) - h)) / (2 * h)
show("finite-difference dE/dz at a/sqrt2 (should be ~0)", dEdz, "V/m^2")

# =============================================================================
hdr("2.7  Semicircular arc at its centre (find the error)")
for rl_, a_ in ((2e-9, 0.05), (7e-9, 0.2)):
    Ex_ = integrate.quad(lambda ph: k * rl_ * a_ * (-np.cos(ph)) / a_ ** 2, 0, np.pi)[0]
    Ey_ = integrate.quad(lambda ph: k * rl_ * a_ * (-np.sin(ph)) / a_ ** 2, 0, np.pi)[0]
    chk(f"arc rho_l={rl_:g}, a={a_:g}: E = -(rho_l/(2 pi eps0 a)) y-hat", [Ex_, Ey_],
        [0, -rl_ / (2 * np.pi * eps0 * a_)], rtol=1e-10, atol=1e-9)
    Eline = integrate.quad(lambda z: k * rl_ * a_ / (a_ ** 2 + z ** 2) ** 1.5, -np.inf, np.inf)[0]
    chk("  infinite line at distance a gives the same magnitude", Eline, -Ey_, rtol=1e-9)
rl, aa = 2e-9, 0.05
show("correct |E| = rho_l/(2 pi eps0 a)", rl / (2 * np.pi * eps0 * aa), "V/m")
show("student's |E| = rho_l/(4 eps0 a)", rl / (4 * eps0 * aa), "V/m")
show("ratio student/correct (= pi/2)", (rl / (4 * eps0 * aa)) / (rl / (2 * np.pi * eps0 * aa)))
show("pi/2", np.pi / 2)
show("int_0^pi cos(phi) dphi", integrate.quad(np.cos, 0, np.pi)[0])
show("int_0^pi sin(phi) dphi", integrate.quad(np.sin, 0, np.pi)[0])

# =============================================================================
hdr("2.8  Dipole on axis and bisector: -Q at (0,0,d/2), +Q at (0,0,-d/2)")
Qd, d = 3e-9, 4e-3
p_vec = Qd * (np.array([0, 0, -d / 2]) - np.array([0, 0, d / 2]))
show("p = Q (r+ - r-)", p_vec, "C m")


def dip_E(P):
    return E_point(-Qd, [0, 0, d / 2], P) + E_point(Qd, [0, 0, -d / 2], P)


def E_axis_closed(D):
    return -k * Qd * 2 * D * d / (D ** 2 - d ** 2 / 4) ** 2     # z-component


def E_bis_closed(D):
    return k * Qd * d / (D ** 2 + d ** 2 / 4) ** 1.5             # z-component


for D in (0.02, 0.005, 0.3):
    chk(f"axis D={D:g}: closed form vs superposition", [0, 0, E_axis_closed(D)], dip_E([0, 0, D]),
        rtol=1e-12, atol=1e-9)
    chk(f"bisector D={D:g}: closed form vs superposition", [0, 0, E_bis_closed(D)], dip_E([D, 0, 0]),
        rtol=1e-12, atol=1e-9)
D = 0.02
show("Q/(4 pi eps0)", k * Qd, "V m")
show("p magnitude Qd", Qd * d, "C m")
Ea, Eb = dip_E([0, 0, D]), dip_E([D, 0, 0])
show("P1: distances to -Q and to +Q", [(D - d / 2) * 100, (D + d / 2) * 100], "cm")
show("P1: field of -Q at (0,0,d/2)", E_point(-Qd, [0, 0, d / 2], [0, 0, D]), "V/m")
show("P1: field of +Q at (0,0,-d/2)", E_point(Qd, [0, 0, -d / 2], [0, 0, D]), "V/m")
show("exact E at P1=(0,0,2cm)", Ea, "V/m")
show("exact E at P2=(2cm,0,0)", Eb, "V/m")
Ea_far = 2 * p_vec * k / D ** 3
Eb_far = -p_vec * k / D ** 3
show("far-field 2p/(4 pi eps0 D^3) at P1", Ea_far, "V/m")
show("far-field -p/(4 pi eps0 D^3) at P2", Eb_far, "V/m")
show("axis: far/exact - 1 (%)", (Ea_far[2] / Ea[2] - 1) * 100)
show("bisector: far/exact - 1 (%)", (Eb_far[2] / Eb[2] - 1) * 100)
show("ratio exact axis/bisector magnitudes at 2 cm", abs(Ea[2] / Eb[2]))
for DD in (0.5, 5.0):   # far away the ratio -> 2 and fields scale as 1/D^3
    show(f"ratio |E_axis|/|E_bis| at D={DD:g} m", abs(E_axis_closed(DD) / E_bis_closed(DD)))
show("E_axis(1 m)/E_axis(2 m) (-> 8 for 1/D^3)", E_axis_closed(1.0) / E_axis_closed(2.0))
def rel_err_axis(D_):
    """|far - exact|/exact on the axis (far-field value is the smaller one there)."""
    far = -2 * k * Qd * d / D_ ** 3
    return abs(far - E_axis_closed(D_)) / abs(E_axis_closed(D_))


Dstar = optimize.brentq(lambda D_: rel_err_axis(D_) - 0.01, 0.6 * d, 100 * d)
show("axis: D where |far-exact|/exact = 1% (exact root), in units of d", Dstar / d)
show("  binomial estimate 1/sqrt(0.02)", 1 / np.sqrt(0.02))
show("  D in cm", Dstar * 100, "cm")

# =============================================================================
hdr("2.9  Finite line charge 0<=z<=4 m, rho_l = 60 pi eps0 C/m")
rho_l = 60 * np.pi * eps0
show("rho_l = 60 pi eps0", rho_l * 1e9, "nC/m")
show("rho_l/(4 pi eps0)", k * rho_l, "V")
show("rho_l/(4 pi eps0 r) at r = 3 m", k * rho_l / 3, "V/m")


def seg_E_numeric(rho, z1, z2, P):
    P = np.asarray(P, float)
    def comp(zp, i):
        Rv = P - np.array([0, 0, zp])
        return k * rho * Rv[i] / np.linalg.norm(Rv) ** 3
    return np.array([integrate.quad(comp, z1, z2, args=(i,), epsabs=1e-14, epsrel=1e-12)[0]
                     for i in range(3)])


def seg_E_closed(rho, z1, z2, r, z):
    """(E_r, E_z) of a segment z1..z2 at (r, z) from the page formula with angles."""
    s1, s2 = (z1 - z) / np.hypot(r, z1 - z), (z2 - z) / np.hypot(r, z2 - z)
    c1, c2 = r / np.hypot(r, z1 - z), r / np.hypot(r, z2 - z)
    return k * rho / r * (s2 - s1), k * rho / r * (c2 - c1)


En = seg_E_numeric(rho_l, 0, 4, [3, 0, 0])
Er_, Ez_ = seg_E_closed(rho_l, 0, 4, 3, 0)
chk("E at (3,0,0): closed form vs numerical integral", [Er_, 0, Ez_], En, rtol=1e-10, atol=1e-12)
show("E at P=(3,0,0)", En, "V/m")
show("|E|", np.linalg.norm(En), "V/m")
show("angle below +x (deg)", np.degrees(np.arctan2(-En[2], En[0])), "deg")
show("distance from P=(3,0,0) to the far end (0,0,4)", np.linalg.norm(np.array([0, 0, 4.0]) - np.array([3, 0, 0.0])), "m")
show("sin(alpha2), cos(alpha2)", [4 / 5, 3 / 5])
# bisector-of-angle check
P = np.array([3, 0, 0.0])
uA = (np.array([0, 0, 0.0]) - P) / np.linalg.norm(np.array([0, 0, 0.0]) - P)
uB = (np.array([0, 0, 4.0]) - P) / np.linalg.norm(np.array([0, 0, 4.0]) - P)
bis = uA + uB
show("sum of unit vectors from P to the two ends", bis)
show("cross(E, bisector) (zero => parallel)", np.cross(En, bis))
show("dot(E, bisector) (<0 => E points away from the segment)", En @ bis)
# general point (not in the plane of an end), second parameter set
Pg = np.array([2.0, 1.0, 1.5])
rg = np.hypot(Pg[0], Pg[1])
Erg, Ezg = seg_E_closed(-2e-9, -0.5, 2.5, rg, Pg[2])
Eng = seg_E_numeric(-2e-9, -0.5, 2.5, Pg)
chk("general point (2,1,1.5), rho=-2 nC/m, segment -0.5..2.5", [Erg * Pg[0] / rg, Erg * Pg[1] / rg, Ezg], Eng,
    rtol=1e-10, atol=1e-12)
# symmetric segment -> bisector formula of Lecture 2
aa_, rr_ = 1.3, 0.7
Er_s, Ez_s = seg_E_closed(rho_l, -aa_, aa_, rr_, 0.0)
chk("symmetric segment: E_r = rho_l/(4 pi eps0 r) 2a/sqrt(a^2+r^2), E_z = 0",
    [Er_s, Ez_s], [k * rho_l / rr_ * 2 * aa_ / np.hypot(aa_, rr_), 0.0], rtol=1e-12, atol=1e-12)
# infinite and semi-infinite lines (numerical, infinite limits)
Einf = seg_E_numeric(rho_l, -np.inf, np.inf, [3, 0, 0])
chk("infinite line at r=3: rho_l/(2 pi eps0 r) x-hat", Einf, [rho_l / (2 * np.pi * eps0 * 3), 0, 0],
    rtol=1e-8, atol=1e-10)
show("infinite line E_r at r=3 m", Einf[0], "V/m")
Esemi = seg_E_numeric(rho_l, 0, np.inf, [3, 0, 0])
chk("semi-infinite line at (3,0,0): (rho/(4 pi eps0 r))(1, 0, -1)", Esemi, [5, 0, -5], rtol=1e-8, atol=1e-10)
show("semi-infinite line E at (3,0,0)", Esemi, "V/m")
show("semi-infinite line: angle of E below +x (deg)", np.degrees(np.arctan2(-Esemi[2], Esemi[0])), "deg")
show("contribution of 4<=z<inf at P", Esemi - En, "V/m")
# Gauss check (i): infinite line through a closed coaxial cylinder r, h
for rcyl, hcyl in ((3.0, 2.0), (0.4, 7.0)):
    side = eps0 * (rho_l / (2 * np.pi * eps0 * rcyl)) * 2 * np.pi * rcyl * hcyl
    chk(f"infinite line: flux through cylinder r={rcyl:g}, h={hcyl:g} = rho_l h", side, rho_l * hcyl,
        rtol=1e-12)
# Gauss check (ii): finite segment, closed cylinder r<=3, -1<=z<=5 (numerical surface integral)
Rc, zb, zt = 3.0, -1.0, 5.0
side = integrate.quad(lambda z: eps0 * seg_E_closed(rho_l, 0, 4, Rc, z)[0] * 2 * np.pi * Rc, zb, zt,
                      epsabs=1e-16, epsrel=1e-12)[0]


def Ez_seg_any(r, z):   # valid also on the axis r -> 0 (outside the segment)
    return k * rho_l * (1 / np.hypot(r, 4 - z) - 1 / np.hypot(r, 0 - z))


# validate Ez_seg_any against the numerical integral at a cap point
chk("cap-point field check (1.2, 0, 5)", Ez_seg_any(1.2, 5.0), seg_E_numeric(rho_l, 0, 4, [1.2, 0, 5.0])[2],
    rtol=1e-10)
top = integrate.quad(lambda r: eps0 * Ez_seg_any(r, zt) * 2 * np.pi * r, 0, Rc, epsabs=1e-16, epsrel=1e-12)[0]
bot = integrate.quad(lambda r: -eps0 * Ez_seg_any(r, zb) * 2 * np.pi * r, 0, Rc, epsabs=1e-16, epsrel=1e-12)[0]
show("finite segment: flux through side", side * 1e9, "nC")
show("finite segment: flux through top cap z=5", top * 1e9, "nC")
show("finite segment: flux through bottom cap z=-1", bot * 1e9, "nC")
chk("total = Q_enc = 4 rho_l", side + top + bot, 4 * rho_l, rtol=1e-9)
show("Q_enc = 4 m * 60 pi eps0 = 240 pi eps0", 240 * np.pi * eps0 * 1e9, "nC")
# E on that cylinder is not constant: sample E_r and E_z on the side
for z in (-1.0, 2.0, 5.0):
    show(f"segment field on the side r=3 at z={z:g}: (E_r, E_z)", seg_E_closed(rho_l, 0, 4, 3.0, z), "V/m")

# =============================================================================
hdr("2.10  Disk a=30 cm, rho_s=-5 uC/m^2, on its axis; annulus with b=10 cm")
rs, ad = -5e-6, 0.30


def disk_Ez(rho, a_, z):
    return rho / (2 * eps0) * (np.sign(z) - z / np.sqrt(z ** 2 + a_ ** 2))


def disk_E_numeric(rho, a_, z, b_=0.0):
    """Brute-force 2-D integral over the disk (or annulus b_<r'<a_) of the Coulomb field of
    dQ = rho r' dr' dphi' at the axis point (0,0,z); all three Cartesian components."""
    def inner(rp, i):
        def f(phi):
            Rv = np.array([-rp * np.cos(phi), -rp * np.sin(phi), z])
            return k * rho * rp * Rv[i] / np.linalg.norm(Rv) ** 3
        return integrate.quad(f, 0, 2 * np.pi, epsabs=1e-9 * scale, epsrel=1e-12, limit=200)[0]
    scale = abs(k * rho)                 # natural field scale (V/m per metre of radius)
    pts = [abs(z)] if b_ < abs(z) < a_ else None
    return np.array([integrate.quad(inner, b_, a_, args=(i,), points=pts, epsabs=1e-9 * scale, epsrel=1e-11,
                                    limit=400)[0] for i in range(3)])


for (rho_, a_, z) in ((rs, ad, 0.01), (rs, ad, 3.0), (rs, ad, -0.2), (2e-6, 0.5, 0.2), (2e-6, 0.5, -0.7)):
    chk(f"disk rho_s={rho_:g}, a={a_:g}: E at z={z:g}", [0, 0, disk_Ez(rho_, a_, z)],
        disk_E_numeric(rho_, a_, z), rtol=1e-8, atol=1e-6)
show("rho_s/(2 eps0)", rs / (2 * eps0), "V/m")
for z in (0.01, 3.0):
    show(f"z/sqrt(z^2+a^2) at z={z:g}", z / np.hypot(z, ad))
    show(f"1 - z/sqrt(z^2+a^2) at z={z:g}", 1 - z / np.hypot(z, ad))
E1 = disk_Ez(rs, ad, 0.01)
E3 = disk_Ez(rs, ad, 3.0)
show("E_z at z = 1 cm", E1, "V/m")
show("sheet approximation rho_s/(2 eps0)", rs / (2 * eps0), "V/m")
show("sheet/exact - 1 (%)", (rs / (2 * eps0) / E1 - 1) * 100)
Qd_ = np.pi * ad ** 2 * rs
show("Q = pi a^2 rho_s", Qd_ * 1e6, "uC")
show("E_z at z = 3 m", E3, "V/m")
Ept = k * Qd_ / 3.0 ** 2
show("point-charge approximation at 3 m", Ept, "V/m")
show("point/exact - 1 (%)", (Ept / E3 - 1) * 100)
# binomial check of the far limit at two heights
for z in (3.0, 10.0):
    show(f"exact / (point approx) at z={z:g}", disk_Ez(rs, ad, z) / (k * Qd_ / z ** 2))
zh = optimize.brentq(lambda z: disk_Ez(rs, ad, z) - rs / (4 * eps0), 1e-6, 10)
chk("half of the sheet value at z = a/sqrt(3)", zh, ad / np.sqrt(3), rtol=1e-9)
show("a/sqrt(3)", ad / np.sqrt(3) * 100, "cm")
show("jump E_z(0+) - E_z(0-)", disk_Ez(rs, ad, 1e-12) - disk_Ez(rs, ad, -1e-12), "V/m")
show("rho_s/eps0", rs / eps0, "V/m")
bd = 0.10
Ean = rs / (2 * eps0) * (0.1 / np.hypot(0.1, bd) - 0.1 / np.hypot(0.1, ad))
chk("annulus at z=10 cm: closed form vs numerical integral", [0, 0, Ean], disk_E_numeric(rs, ad, 0.1, bd),
    rtol=1e-8, atol=1e-6)
show("z/sqrt(z^2+b^2) at z=0.1", 0.1 / np.hypot(0.1, bd))
show("z/sqrt(z^2+a^2) at z=0.1", 0.1 / np.hypot(0.1, ad))
show("annulus factor", 0.1 / np.hypot(0.1, bd) - 0.1 / np.hypot(0.1, ad))
show("annulus E_z at z = 10 cm", Ean, "V/m")
show("full disk E_z at z = 10 cm", disk_Ez(rs, ad, 0.1), "V/m")
show("hole (disk b) E_z at z = 10 cm", disk_Ez(rs, bd, 0.1), "V/m")
chk("annulus = disk(a) - disk(b)", Ean, disk_Ez(rs, ad, 0.1) - disk_Ez(rs, bd, 0.1), rtol=1e-12)
show("annulus E_z at z -> 0+ (1e-9 m)", rs / (2 * eps0) * (1e-9 / np.hypot(1e-9, bd) - 1e-9 / np.hypot(1e-9, ad)),
     "V/m")
# second parameter set for the annulus closed form
chk("annulus 2nd set (rho=2e-6, a=0.5, b=0.2, z=-0.3)",
    [0, 0, 2e-6 / (2 * eps0) * (-0.3 / np.hypot(0.3, 0.2) + 0.3 / np.hypot(0.3, 0.5))],
    disk_E_numeric(2e-6, 0.5, -0.3, 0.2), rtol=1e-8, atol=1e-6)

# =============================================================================
hdr("2.11  Boron mass spectrometer: selector E0 x-hat, B1 along -z; analyzer B2 = 0.5 z-hat T")
E0, B1m, B2m = 4e4, 0.10, 0.50
vsel = E0 / B1m
show("selected speed E0/B1", vsel, "m/s")
vv = np.array([0, vsel, 0])
for sgn in (+1, -1):
    B1 = np.array([0, 0, sgn * B1m])
    F = e * (np.array([E0, 0, 0]) + np.cross(vv, B1))
    show(f"B1 along {'+' if sgn > 0 else '-'}z: v x B1", np.cross(vv, B1), "V/m")
    show(f"B1 along {'+' if sgn > 0 else '-'}z: force on B+ at selected speed", F, "N")
B1 = np.array([0, 0, -B1m])
B2 = np.array([0, 0, B2m])
show("initial analyzer force direction q v x B2 / |.|", np.cross(vv, B2) / np.linalg.norm(np.cross(vv, B2)))
ions = {"10B+": (10 * u, e), "11B+": (11 * u, e), "11B2+": (11 * u, 2 * e)}
results = {}
for name, (m, q) in ions.items():
    # selector: zero force independent of q, m
    Fsel = q * (np.array([E0, 0, 0]) + np.cross(vv, B1))
    chk(f"{name}: zero force in selector", Fsel, np.zeros(3), atol=1e-30)
    Rr = m * vsel / (q * B2m)
    Th = np.pi * m / (q * B2m)

    def rhs(t, y, m=m, q=q):
        return np.concatenate([y[3:], q / m * np.cross(y[3:], B2)])

    def hit(t, y):
        return y[1]
    hit.terminal, hit.direction = True, -1
    sol = integrate.solve_ivp(rhs, [0, 3 * Th], [0, 0, 0, 0, vsel, 0], events=hit, rtol=1e-11, atol=1e-14,
                              max_step=Th / 2000)
    t_hit = sol.t_events[0][0]
    y_hit = sol.y_events[0][0]
    # a tiny initial interval also triggers y=0; take first event after t>Th/10
    ev = [(t_, y_) for t_, y_ in zip(sol.t_events[0], sol.y_events[0]) if t_ > Th / 10]
    t_hit, y_hit = ev[0]
    chk(f"{name}: landing x = 2R (ODE)", y_hit[0], 2 * Rr, rtol=1e-7)
    chk(f"{name}: time in analyzer = pi m/(qB2) (ODE)", t_hit, Th, rtol=1e-7)
    # sense of rotation: angular momentum about the orbit centre (R,0,0), z-component
    rc = np.array([Rr, 0, 0])
    Lz = np.cross(np.array([0, 0, 0]) - rc, np.array([0, vsel, 0]))[2]
    show(f"{name}: R", Rr * 100, "cm")
    show(f"{name}: landing point x = 2R", 2 * Rr * 100, "cm")
    show(f"{name}: time pi m/(q B2)", Th * 1e6, "us")
    show(f"{name}: Lz about centre (<0 = clockwise seen from +z)", Lz)
    show(f"{name}: speed at landing (unchanged)", np.linalg.norm(y_hit[3:]), "m/s")
    results[name] = Rr
show("separation of 10B+ and 11B+ spots 2(R11-R10)", 2 * (results["11B+"] - results["10B+"]) * 100, "cm")
show("mass of singly charged ion landing with 11B2+ (u)", 11 / 2)
vfast = 1.1 * vsel
Ffast = e * (np.array([E0, 0, 0]) + np.cross(np.array([0, vfast, 0]), B1))
show("10% fast: speed", vfast, "m/s")
show("10% fast: force on 11B+ in selector", Ffast, "N")
show("  electric part", e * np.array([E0, 0, 0]), "N")
show("  magnetic part", e * np.cross(np.array([0, vfast, 0]), B1), "N")
show("kinetic energy of 11B+ at 4e5 m/s", 0.5 * 11 * u * vsel ** 2 / e / 1e3, "keV")

# =============================================================================
hdr("2.12  Two charges that make a given field (Summer 2017 HE1 #1a style)")
pe = np.pi * eps0
# (a) Q1 at (0,0,2) gives E = -3 z-hat at the origin
rQ1 = np.array([0, 0, 2.0])
Q1 = 3 * 4 * np.pi * eps0 * 4            # from Q1/(4 pi eps0 4) = 3
show("Q1 / (pi eps0)", Q1 / pe)
show("Q1", Q1 * 1e9, "nC")
chk("E of Q1 at origin", E_point(Q1, rQ1, [0, 0, 0]), [0, 0, -3], rtol=1e-12)
# (b) |Q2| = 16 pi eps0 on the x axis; total field -4x -3z
Q2m = 16 * pe
show("|Q2|", Q2m * 1e9, "nC")
show("required E2 = E - E1", np.array([-4, 0, -3.0]) - E_point(Q1, rQ1, [0, 0, 0]), "V/m")
sols = []
for s in (+1, -1):
    # candidates: |Q2|/(4 pi eps0 X^2) = 4 gives |X| = 1; others shown for contrast
    for X in (+1.0, -1.0, +2.0, -0.5):
        Et = E_point(Q1, rQ1, [0, 0, 0]) + E_point(s * Q2m, [X, 0, 0], [0, 0, 0])
        good = np.allclose(Et, [-4, 0, -3], atol=1e-9)
        print(f"  Q2 = {s * 16:+d} pi eps0 at x = {X:+g} m -> E(0) = {np.array2string(Et, precision=5)}"
              f"  {'MATCH' if good else ''}")
        if good:
            sols.append((s, X))
show("number of (sign, position) solutions among candidates", len(sols))
# brute force: for each sign, find every X on each half-line with E_x(origin) = -4 (root finding)
allsol = []
for s in (+1, -1):
    gx = lambda X, s=s: (E_point(Q1, rQ1, [0, 0, 0]) + E_point(s * Q2m, [X, 0, 0], [0, 0, 0]))[0] + 4.0
    for lo_, hi_ in ((-50.0, -1e-4), (1e-4, 50.0)):
        Xs = np.linspace(lo_, hi_, 20001)
        g = np.array([gx(X) for X in Xs])
        for i in np.where(np.sign(g[:-1]) * np.sign(g[1:]) < 0)[0]:
            allsol.append((s, optimize.brentq(gx, Xs[i], Xs[i + 1], xtol=1e-14)))
for s, X in allsol:
    show(f"root-finding solution: sign {s:+d}, X", X, "m")
chk("exactly two solutions: (+, X=+1) and (-, X=-1)", sorted(s * X for s, X in allsol), [1.0, 1.0], rtol=1e-10)
show("|E| at origin", np.linalg.norm([-4, 0, -3.0]), "V/m")
# (c) null point with Q2 = +16 pi eps0 at (1,0,0)
rQ2 = np.array([1.0, 0, 0])
Q2 = +Q2m
Etot = lambda r: E_point(Q1, rQ1, r) + E_point(Q2, rQ2, r)
null_closed = np.array([(3 - np.sqrt(3)) / 2, 0, np.sqrt(3) - 1])
show("null point closed form ((3-sqrt3)/2, 0, sqrt3-1)", null_closed, "m")
rng = np.random.default_rng(0)
found = []
for _ in range(400):
    x0 = rng.uniform(-3, 4, 3)
    sol, info, ier, msg = optimize.fsolve(Etot, x0, full_output=True, xtol=1e-13)
    if ier == 1 and np.linalg.norm(Etot(sol)) < 1e-9:
        if not any(np.linalg.norm(sol - f_) < 1e-6 for f_ in found):
            found.append(sol)
show("distinct null points found from 400 random starts", len(found))
for f_ in found:
    show("  null point", f_, "m")
chk("null point matches closed form", found[0], null_closed, rtol=1e-8, atol=1e-10)
d1 = np.linalg.norm(null_closed - rQ1)
d2 = np.linalg.norm(null_closed - rQ2)
show("d1 (to Q1), d2 (to Q2)", [d1, d2], "m")
show("d1/d2 (should be sqrt 3)", d1 / d2)
show("segment length sqrt5", np.sqrt(5), "m")
show("d2 = sqrt5/(1+sqrt3)", np.sqrt(5) / (1 + np.sqrt(3)), "m")
show("1/(1+sqrt3)", 1 / (1 + np.sqrt(3)))
# fields on the line through the charges, outside the segment: same direction -> no null
for t in (-0.5, 1.5, 3.0):
    rpt = rQ2 + t * (rQ1 - rQ2)
    E1v, E2v = E_point(Q1, rQ1, rpt), E_point(Q2, rQ2, rpt)
    show(f"on the line, t={t:g}: E1.E2/(|E1||E2|)", E1v @ E2v / np.linalg.norm(E1v) / np.linalg.norm(E2v))
# (d) flux through sphere r=1.5 about origin, and through the cube [0,1]^3
fs1 = sphere_flux(lambda p: D_point(Q1, rQ1, p), np.zeros(3), 1.5)
fs2 = sphere_flux(lambda p: D_point(Q2, rQ2, p), np.zeros(3), 1.5)
show("sphere R=1.5: flux of Q1 (outside)", fs1 * 1e9, "nC")
show("sphere R=1.5: flux of Q2 (inside)", fs2 * 1e9, "nC")
chk("sphere total = Q2 = 16 pi eps0", fs1 + fs2, Q2, rtol=1e-8)
show("16 pi eps0", 16 * pe * 1e9, "nC")
fc1 = box_face_fluxes(Q1, rQ1, [0, 0, 0], [1, 1, 1])
fc2 = box_face_fluxes(Q2, rQ2, [0, 0, 0], [1, 1, 1])
show("cube: flux of Q1 (outside) total", sum(fc1.values()) * 1e12, "pC")
for kf, v in fc2.items():
    show(f"cube: flux of Q2 (corner) through face {kf}", v * 1e12, "pC")
chk("cube total = Q2/8 = 2 pi eps0", sum(fc1.values()) + sum(fc2.values()), 2 * pe, rtol=1e-8)
show("2 pi eps0", 2 * pe * 1e12, "pC")

print("\n" + ("ALL CHECKS PASSED" if NFAIL == 0 else f"{NFAIL} CHECK(S) FAILED"))
