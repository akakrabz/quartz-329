#!/usr/bin/env python3
"""Verification script for practice/03-gauss-law-at-work.md (Lecture 3).

Every number, sign and direction quoted on the page is printed here, and every
closed form is compared with an independent brute-force computation (direct
Coulomb integration, numerical surface integrals, sheet superposition, or a
numerical Gauss integral) at >= 2 parameter sets where the result is symbolic.
numpy + scipy only.
"""
import numpy as np
from scipy.integrate import quad, dblquad
from scipy.optimize import brentq, minimize_scalar

eps0 = 8.8541878128e-12
PI = np.pi
fails = []


def check(label, got, want, rtol=1e-6, atol=0.0):
    ok = np.allclose(got, want, rtol=rtol, atol=atol)
    print(f"   [{'ok' if ok else 'FAIL'}] {label}: got {np.round(got, 10)}  want {np.round(want, 10)}")
    if not ok:
        fails.append(label)


def hdr(s):
    print("\n" + "=" * 78 + "\n" + s + "\n" + "=" * 78)


# ---------------------------------------------------------------------------
hdr("3.1 Two sheets of charge")
rs1, z1 = 4e-9, 0.0
rs2, z2 = -1e-9, 2.0


def E_sheets(z):
    return (rs1 * np.sign(z - z1) + rs2 * np.sign(z - z2)) / (2 * eps0)


def E_disk_bruteforce(rs, z0, z, R=1e7):
    """Coulomb integral of a huge disk (radius R) on plane z0, field on its axis.
    Rings of radius r' = exp(s): dE_z = rs h/(4 pi eps0 (r'^2+h^2)^1.5) 2 pi r' dr', dr' = r' ds."""
    h = z - z0
    f = lambda s: rs * h / (4 * PI * eps0 * (np.exp(2 * s) + h**2) ** 1.5) * 2 * PI * np.exp(2 * s)
    return quad(f, np.log(1e-9), np.log(R), points=[np.log(abs(h))], limit=500)[0]


for z in (-1.0, 1.0, 3.0):
    bf = E_disk_bruteforce(rs1, z1, z) + E_disk_bruteforce(rs2, z2, z)
    print(f"   z = {z:+.1f} m: E_z = {E_sheets(z):9.3f} V/m (brute-force disk R=1e7 m: {bf:9.3f})")
    check(f"3.1 E_z({z})", bf, E_sheets(z), rtol=1e-5)
print(f"   rounded: z<0: {E_sheets(-1):.0f} V/m, 0<z<2: {E_sheets(1):+.0f} V/m, z>2: {E_sheets(3):+.0f} V/m")
print(f"   jump of eps0*E_z at z=0: {eps0*(E_sheets(1)-E_sheets(-1))*1e9:.3f} nC/m^2 (= rho_s1 = 4)")
print(f"   jump of eps0*E_z at z=2: {eps0*(E_sheets(3)-E_sheets(1))*1e9:.3f} nC/m^2 (= rho_s2 = -1)")

# ---------------------------------------------------------------------------
hdr("3.2 Flux through a tilted window")
c0 = np.array([0.0, 0, 0])
u = np.array([0.0, 2, 0])          # (0,0,0)->(0,2,0)
v = np.array([3.0, 0, 4])          # (0,0,0)->(3,0,4)
print("   corners: (0,0,0) (0,2,0) (3,2,4) (3,0,4); 4th corner = u+v =", u + v)
print("   u.v =", u @ v, "(edges perpendicular -> rectangle) ; edge lengths |u| =", np.linalg.norm(u),
      "m, |v| =", np.linalg.norm(v), "m")
uxv = np.cross(u, v)
print("   u x v =", uxv, " |u x v| = area =", np.linalg.norm(uxv), "m^2")
n = uxv if uxv[2] > 0 else -uxv
nhat = n / np.linalg.norm(n)
print("   n-hat (positive z component) =", nhat)
A = np.linalg.norm(uxv)
for lab, E in (("(a)", np.array([0.0, 0, 500])), ("(b)", np.array([300.0, 0, 400]))):
    # brute-force: midpoint-rule surface integral over a 50x50 parameter grid
    s = (np.arange(50) + 0.5) / 50
    flux_bf = 0.0
    dS = np.cross(u / 50, v / 50) * (1 if uxv[2] > 0 else -1)
    for si in s:
        for ti in s:
            flux_bf += E @ dS
    flux = (E @ nhat) * A
    print(f"   {lab} |E| = {np.linalg.norm(E):.0f} V/m, E.n = {E @ nhat:.1f} V/m, int E.dS = {flux:.1f} V*m"
          f" (grid sum {flux_bf:.1f}), psi_E = int D.dS = {eps0*flux:.4e} C = {eps0*flux*1e9:.2f} nC")
    check(f"3.2{lab} flux grid vs formula", flux_bf, flux, atol=1e-9)
print("   shadow of the window on the xy-plane: 3 m x 2 m = 6 m^2 ; 500*6 =", 500 * 6, "V*m")
check("3.2(a) value", (np.array([0, 0, 500.0]) @ nhat) * A, 3000.0)
check("3.2(b) value", (np.array([300.0, 0, 400]) @ nhat) * A, 0.0, atol=1e-9)

# ---------------------------------------------------------------------------
hdr("3.3 Finite line inside a closed cylinder (MC)")
rl, zs1, zs2 = 3e-9, -1.0, 1.0       # segment -1<z<1, 3 nC/m
Rc, zc1, zc2 = 1.0, -2.0, 2.0        # closed cylinder r<=1, -2<=z<=2


def Dr_seg(r, z):
    return quad(lambda zp: rl * r / (4 * PI * ((z - zp) ** 2 + r**2) ** 1.5), zs1, zs2)[0]


def Dz_seg(r, z):
    return quad(lambda zp: rl * (z - zp) / (4 * PI * ((z - zp) ** 2 + r**2) ** 1.5), zs1, zs2)[0]


side = quad(lambda z: Dr_seg(Rc, z) * 2 * PI * Rc, zc1, zc2, limit=200)[0]
top = quad(lambda r: Dz_seg(r, zc2) * 2 * PI * r, 0, Rc, limit=200)[0]
bot = quad(lambda r: -Dz_seg(r, zc1) * 2 * PI * r, 0, Rc, limit=200)[0]
print(f"   side flux = {side*1e9:.4f} nC, top cap = {top*1e9:.4f} nC, bottom cap = {bot*1e9:.4f} nC")
print(f"   total = {(side+top+bot)*1e9:.4f} nC ; Q_enc = rho_l*2 m = {rl*2*1e9:.1f} nC")
print(f"   closed form side = rho_l*(sqrt10 - sqrt2) = {rl*(np.sqrt(10)-np.sqrt(2))*1e9:.4f} nC ;"
      f" caps together = {(rl*2 - rl*(np.sqrt(10)-np.sqrt(2)))*1e9:.4f} nC")
check("3.3 total flux = 6 nC", side + top + bot, 6e-9, rtol=1e-6)
check("3.3 side closed form", side, rl * (np.sqrt(10) - np.sqrt(2)), rtol=1e-6)
print("   distractor (d): rho_l * 4 m =", rl * 4 * 1e9, "nC")

# ---------------------------------------------------------------------------
hdr("3.4 Charges written with delta functions")
sig = 1e-3
g = lambda x, x0: np.exp(-((x - x0) ** 2) / (2 * sig**2)) / (sig * np.sqrt(2 * PI))
I = lambda x0: quad(lambda x: g(x, x0), -2, 2, points=[x0] if -2 < x0 < 2 else None, limit=200)[0]
L = 4.0  # cube side, |x|,|y|,|z|<2
terms = {
    "4 d(x-1)d(y+1)d(z)    point 4 nC at (1,-1,0)": 4 * I(1) * I(-1) * I(0),
    "-2 d(x+1)d(y)         line -2 nC/m || z through (-1,0)": -2 * I(-1) * I(0) * L,
    "0.5 d(z-1)            sheet 0.5 nC/m^2 on z=1": 0.5 * I(1) * L * L,
    "2 d(x)d(y-3)d(z)      point 2 nC at (0,3,0)": 2 * I(0) * I(3) * I(0),
}
tot = 0.0
for k, val in terms.items():
    print(f"   {k:58s} -> {val:8.4f} nC inside the cube")
    tot += val
print(f"   total enclosed charge = {tot:.4f} nC = flux of D out of the cube")
print(f"   line length inside the cube = {L:.0f} m ; sheet area inside the cube = {L*L:.0f} m^2 ;"
      f" (0,3,0) outside since |y| = 3 > 2")
check("3.4 total charge", tot, 4.0, rtol=1e-6)
print("   units: 3 deltas -> nC ; 2 deltas -> nC/m ; 1 delta -> nC/m^2 (each delta carries 1/m)")

# ---------------------------------------------------------------------------
hdr("3.5 Magnetic flux through a dome (MC)")
a5 = 0.5
B = np.array([0.3, 0.0, 0.4])


def dome_flux(Bvec):
    f = lambda th, ph: (Bvec[0] * np.sin(th) * np.cos(ph) + Bvec[1] * np.sin(th) * np.sin(ph)
                        + Bvec[2] * np.cos(th)) * a5**2 * np.sin(th)
    return dblquad(f, 0, 2 * PI, 0, PI / 2)[0]


psi_dome = dome_flux(B)
psi_base = B @ np.array([0, 0, -1.0]) * PI * a5**2
print(f"   |B| = {np.linalg.norm(B):.2f} T ; base area pi a^2 = {a5**2:.2f}*pi = {PI*a5**2:.4f} m^2 ;"
      f" dome area 2 pi a^2 = {2*a5**2:.2f}*pi = {2*PI*a5**2:.4f} m^2")
print(f"   base (outward -z): psi_base = {psi_base:.6f} Wb = {psi_base/PI:.4f}*pi")
print(f"   dome by direct surface integral = {psi_dome:.6f} Wb = {psi_dome/PI:.4f}*pi")
print(f"   dome + base = {psi_dome+psi_base:.2e} (closed surface -> 0)")
print(f"   x-part alone through the dome: {dome_flux(np.array([0.3,0,0])):.2e} Wb")
check("3.5 dome flux = 0.1 pi", psi_dome, 0.1 * PI)
print(f"   answer (b) 0.1*pi = {0.1*PI:.4f} Wb ; distractors: (c) 0.4*2*pi*a^2 = {0.4*2*PI*a5**2/PI:.3f}*pi = {0.4*2*PI*a5**2:.3f};"
      f" (d) |B|*2*pi*a^2 = {np.linalg.norm(B)*2*PI*a5**2/PI:.3f}*pi = {np.linalg.norm(B)*2*PI*a5**2:.3f};"
      f" (e) |B|*pi*a^2 = {np.linalg.norm(B)*PI*a5**2/PI:.3f}*pi = {np.linalg.norm(B)*PI*a5**2:.3f}")

# ---------------------------------------------------------------------------
hdr("3.6 Sphere with a graded density rho0(1-r/a)")


def sph_E_closed(r, rho0, a):
    return np.where(r < a, rho0 / eps0 * (r / 3 - r**2 / (4 * a)), rho0 * a**3 / (12 * eps0 * r**2))


def sph_E_gauss_numeric(r, rho0, a):
    rho = lambda rr: rho0 * (1 - rr / a) if rr < a else 0.0
    Q = quad(lambda rr: rho(rr) * 4 * PI * rr**2, 0, r, points=[a] if r > a else None)[0]
    return Q / (4 * PI * eps0 * r**2)


def sph_E_coulomb_rays(s, rho0, a):
    """Direct Coulomb integral by rays from P=(0,0,s): E_z = -(1/4 pi eps0) int u_z (int rho dt) dOmega."""
    def ray_int(th):
        c = np.cos(th)
        disc = a**2 - s**2 * (1 - c**2)
        if disc <= 0:
            return 0.0
        t1, t2 = -s * c - np.sqrt(disc), -s * c + np.sqrt(disc)
        t1 = max(t1, 0.0)
        if t2 <= t1:
            return 0.0
        rho_t = lambda t: rho0 * (1 - np.sqrt(max(t * t + 2 * s * t * c + s * s, 0.0)) / a)
        return quad(rho_t, t1, t2, limit=200, epsabs=0, epsrel=1e-11)[0]
    # breakpoint at the tangent ray when P is outside (integrand ~ sqrt there); epsabs=0 because
    # the integrand is ~1e-7 in SI units and quad's default epsabs (1.5e-8) would dominate the error
    pts = [PI / 2] + ([PI - np.arcsin(a / s)] if s > a else [])
    val = quad(lambda th: np.cos(th) * np.sin(th) * ray_int(th), 0, PI, limit=400, points=pts,
               epsabs=0, epsrel=1e-10)[0]
    return -(2 * PI) / (4 * PI * eps0) * val


for (rho0, a) in ((2e-6, 0.09), (5e-6, 0.2)):
    print(f"   parameter set rho0 = {rho0:g} C/m^3, a = {a:g} m")
    for frac in (0.3, 2 / 3, 0.9, 1.5):
        r = frac * a
        e_cf = float(sph_E_closed(r, rho0, a))
        e_g = sph_E_gauss_numeric(r, rho0, a)
        e_c = sph_E_coulomb_rays(r, rho0, a)
        print(f"      r = {frac:.3f}a: closed {e_cf:10.3f}  Gauss-quad {e_g:10.3f}  Coulomb-rays {e_c:10.3f} V/m")
        check(f"3.6 E closed vs Gauss r={frac:.3f}a", e_g, e_cf, rtol=1e-8)
        check(f"3.6 E closed vs Coulomb r={frac:.3f}a", e_c, e_cf, rtol=1e-8)
    res = minimize_scalar(lambda r: -float(sph_E_closed(r, rho0, a)), bounds=(0, a), method="bounded",
                          options={"xatol": 1e-12})
    check("3.6 r_max = 2a/3", res.x, 2 * a / 3, rtol=1e-5)
    check("3.6 E_max = rho0 a/(9 eps0)", -res.fun, rho0 * a / (9 * eps0), rtol=1e-8)
    Qtot = quad(lambda rr: rho0 * (1 - rr / a) * 4 * PI * rr**2, 0, a)[0]
    check("3.6 Q = pi rho0 a^3/3", Qtot, PI * rho0 * a**3 / 3)
rho0, a = 2e-6, 0.09
Q6 = PI * rho0 * a**3 / 3
print(f"   PAGE: Q = {Q6:.4e} C = {Q6*1e9:.3f} nC ; r_max = 2a/3 = {200*a/3:.1f} cm ;"
      f" E_max = {rho0*a/(9*eps0):.1f} V/m ; E(a) = {rho0*a/(12*eps0):.1f} V/m ; ratio E(a)/E_max = {9/12}")
b6 = 2 * a
rs6 = -Q6 / (4 * PI * b6**2)
print(f"   shell at b = 2a = {b6*100:.0f} cm: rho_s = -Q/(4 pi b^2) = {rs6:.4e} C/m^2 = {rs6*1e9:.3f} nC/m^2"
      f" ; -rho0 a/48 = {-rho0*a/48*1e9:.3f} nC/m^2")
check("3.6 rho_s = -rho0 a /48", rs6, -rho0 * a / 48)
check("3.6 continuity at r=a", rho0 / eps0 * (a / 3 - a / 4), rho0 * a**3 / (12 * eps0 * a**2))

# ---------------------------------------------------------------------------
hdr("3.7 Point-charge flux through a disk")


def disk_flux_closed(Q, h, a):
    return Q / 2 * (1 - h / np.sqrt(h**2 + a**2))


def disk_flux_bf(Q, h, a):
    # D . (-z) at (r cos p, r sin p, 0) from Q at (0,0,h), integrated over the disk
    f = lambda r, p: Q * h / (4 * PI * (r**2 + h**2) ** 1.5) * r
    return dblquad(f, 0, 2 * PI, 0, a)[0]


for (Q, h, a) in ((12e-9, 0.04, 0.03), (5e-9, 0.1, 0.37), (12e-9, 0.04, 0.04 * np.sqrt(3))):
    cf, bf = disk_flux_closed(Q, h, a), disk_flux_bf(Q, h, a)
    print(f"   Q={Q*1e9:g} nC h={h:g} m a={a:.5f} m: closed {cf*1e9:.6f} nC, brute-force {bf*1e9:.6f} nC")
    check("3.7 disk flux", bf, cf, rtol=1e-8)
Q, h = 12e-9, 0.04
print(f"   PAGE (b): sqrt(h^2+a^2) = {np.hypot(0.04,0.03)*100:.1f} cm, cos(alpha) = {0.04/np.hypot(0.04,0.03):.2f},"
      f" psi = {disk_flux_closed(Q,h,0.03)*1e9:.3f} nC = Q/{Q/disk_flux_closed(Q,h,0.03):.0f}")
aq = brentq(lambda a: disk_flux_closed(Q, h, a) - Q / 4, 1e-6, 1.0)
print(f"   PAGE (c): radius for Q/4: {aq*100:.4f} cm ; sqrt(3) h = {np.sqrt(3)*4:.4f} cm")
check("3.7 a(Q/4) = sqrt3 h", aq, np.sqrt(3) * h, rtol=1e-9)
print(f"   PAGE (d): a -> inf: psi -> {disk_flux_closed(Q,h,1e9)*1e9:.6f} nC (Q/2 = {Q/2*1e9:g} nC)")
# solid-angle check: cap of radius R=sqrt(h^2+a^2) centred on Q
for a in (0.03, 0.07):
    R = np.hypot(h, a)
    cosal = h / R
    cap = Q * (2 * PI * R**2 * (1 - cosal)) / (4 * PI * R**2)
    check(f"3.7 cap (solid angle) a={a}", cap, disk_flux_closed(Q, h, a))

# ---------------------------------------------------------------------------
hdr("3.8 Find the error: odd slab rho0 x/a")


def odd_E_closed(x, rho0, a):
    return np.where(np.abs(x) < a, -rho0 * (a**2 - x**2) / (2 * eps0 * a), 0.0)


def odd_E_sheets(x, rho0, a):
    f = lambda xp: rho0 * xp / a * np.sign(x - xp)
    pts = [x] if -a < x < a else None
    return quad(f, -a, a, points=pts, limit=200)[0] / (2 * eps0)


for (rho0, a) in ((1e-6, 1.0), (3e-6, 0.25)):
    print(f"   parameter set rho0 = {rho0:g} C/m^3, a = {a:g} m")
    for frac in (-1.5, -0.7, -0.2, 0.0, 0.4, 0.95, 1.3):
        x = frac * a
        cf, bf = float(odd_E_closed(x, rho0, a)), odd_E_sheets(x, rho0, a)
        print(f"      x = {frac:+.2f}a: closed {cf: .6e}  sheet-sum {bf: .6e} V/m")
        check(f"3.8 E({frac}a)", bf, cf, rtol=1e-8, atol=1e-12 * abs(rho0 * a / eps0))
    # E is EVEN in x (so the symmetric pillbox's cap fluxes cancel identically)
    for frac in (0.2, 0.6):
        check(f"3.8 E even: E({frac}a) = E(-{frac}a)", odd_E_sheets(-frac * a, rho0, a), odd_E_sheets(frac * a, rho0, a))
    check("3.8 |E(0)| = rho0 a/(2 eps0) = (1/eps0) int_0^a rho", -odd_E_sheets(0.0, rho0, a), rho0 * a / (2 * eps0))
    # the student's symmetric pillbox: Q_enc between -x and x is zero
    print(f"      student's Q_enc(-0.5a..0.5a) = {quad(lambda xp: rho0*xp/a, -0.5*a, 0.5*a)[0]:.2e} (zero, but uninformative)")
print("   E points -x (negative E_x) inside: from the positive right half toward the negative left half")

# ---------------------------------------------------------------------------
hdr("3.9 Two slabs and a sheet (fields in V/m because rho is given in units of eps0)")
r1, r2 = 3 * eps0, -2 * eps0          # slab 1: -3<z<-1 ; slab 2: 0<z<3
rs9, zs9 = 4 * eps0, -1.0


def rho9(z):
    if -3 < z < -1:
        return r1
    if 0 < z < 3:
        return r2
    return 0.0


def slab_field(z, rho, z_lo, z_hi):
    W, zc = z_hi - z_lo, (z_lo + z_hi) / 2
    return rho / eps0 * (z - zc) if z_lo < z < z_hi else rho * W / (2 * eps0) * np.sign(z - zc)


def E9_blocks(z, sheet=False):
    e = slab_field(z, r1, -3, -1) + slab_field(z, r2, 0, 3)
    if sheet:
        e += rs9 / (2 * eps0) * np.sign(z - zs9)
    return e


def E9_bf(z, sheet=False):
    e = quad(lambda zp: rho9(zp) * np.sign(z - zp), -3, 3, points=[-1, 0, z], limit=200)[0] / (2 * eps0)
    if sheet:
        e += rs9 / (2 * eps0) * np.sign(z - zs9)
    return e


print(f"   per-area charges: slab1 = {r1*2/eps0:+.0f} eps0 C/m^2, slab2 = {r2*3/eps0:+.0f} eps0 C/m^2, net = {(r1*2+r2*3)/eps0:.0f}")
print(f"   each slab alone outside: |E| = {abs(r1*2/(2*eps0)):.0f} V/m")
pts9 = (-4, -2, -0.5, 1.5, 4)
want_b = (0, 3, 6, 3, 0)
want_c = (-2, 1, 8, 5, 2)
for z, wb, wc in zip(pts9, want_b, want_c):
    eb, ebf = E9_blocks(z), E9_bf(z)
    ec, ecf = E9_blocks(z, True), E9_bf(z, True)
    print(f"   z = {z:+5.1f} m: (b) E_z = {eb:+.4f} (sheet-sum {ebf:+.4f}) ; (c) with sheet E_z = {ec:+.4f} (sheet-sum {ecf:+.4f}) V/m")
    check(f"3.9(b) z={z}", (eb, ebf), (wb, wb), atol=1e-9)
    check(f"3.9(c) z={z}", (ec, ecf), (wc, wc), atol=1e-9)
print("   piecewise (b): z<-3: 0 ; -3<z<-1: 3z+9 ; -1<z<0: 6 ; 0<z<3: 6-2z ; z>3: 0")
for z in (-2.5, -1.2, -0.3, 0.7, 2.2):
    want = 3 * z + 9 if -3 < z < -1 else (6 if -1 < z < 0 else 6 - 2 * z)
    check(f"3.9 piecewise (b) z={z}", E9_bf(z), want, atol=1e-9)
print("   piecewise (c): z<-3: -2 ; -3<z<-1: 3z+7 ; -1<z<0: 8 ; 0<z<3: 8-2z ; z>3: +2")
for z in (-3.5, -2.5, -1.2, -0.3, 0.7, 2.2, 3.5):
    want = -2 if z < -3 else (3 * z + 7 if z < -1 else (8 if z < 0 else (8 - 2 * z if z < 3 else 2)))
    check(f"3.9 piecewise (c) z={z}", E9_bf(z, True), want, atol=1e-9)
print("   break points (b): E(-3)=0, E(-1)=6, E(0)=6, E(3)=0 ; (c): E(-3)=-2, E(-1-)=4, E(-1+)=8, E(0)=8, E(3)=2")
zz = brentq(lambda z: E9_bf(z, True), -2.9, -1.1)
print(f"   (d) E = 0 at z = {zz:.6f} m (-7/3 = {-7/3:.6f})")
check("3.9(d) zero", zz, -7 / 3, rtol=1e-9)
jump = E9_bf(-1 + 1e-9, True) - E9_bf(-1 - 1e-9, True)
print(f"   jump at z=-1: {jump:.6f} V/m -> eps0*jump = {jump:.3f} eps0 = rho_s ; far fields: net 4 eps0 -> +-{4/2:.0f} V/m")
check("3.9 jump = rho_s/eps0", jump, 4.0, rtol=1e-6)
# no other zero: scan
zs = np.linspace(-6, 6, 120001)
vals = np.array([E9_blocks(z, True) for z in zs])
sgn_changes = zs[1:][np.sign(vals[1:]) != np.sign(vals[:-1])]
print("   sign changes of E_z (with sheet) on [-6,6]:", np.round(sgn_changes, 4), "-> the only zero is z = -7/3 m")
check("3.9(d) single zero", len(sgn_changes), 1)

# ---------------------------------------------------------------------------
hdr("3.10 Sphere with an off-centre cavity (rho = 30 eps0)")
rho10 = 30 * eps0
a10, b10 = 1.0, 0.4
d10 = np.array([0.5, 0.0, 0.0])
k10 = rho10 / (3 * eps0)
print(f"   rho/(3 eps0) = {k10:.6f} V/m^2")


def ball_field(P, c, R, rho):
    rv = np.asarray(P, float) - c
    r = np.linalg.norm(rv)
    if r <= R:
        return rho / (3 * eps0) * rv
    return rho * R**3 / (3 * eps0) * rv / r**3


def E10_superpose(P):
    return ball_field(P, np.zeros(3), a10, rho10) + ball_field(P, d10, b10, -rho10)


def seg_len(P, uvec, c, R):
    """length of ray P + t u (t>=0) inside sphere (c,R); arrays over directions."""
    w = P - c
    bq = uvec @ w
    disc = bq**2 - (w @ w - R**2)
    sq = np.sqrt(np.clip(disc, 0, None))
    t1 = np.clip(-bq - sq, 0, None)
    t2 = np.clip(-bq + sq, 0, None)
    return np.where(disc > 0, t2 - t1, 0.0)


def E10_coulomb_rays(P, nmu=1200, nphi=2400):
    """Direct Coulomb integral over (big ball minus cavity) with rays from P (no superposition used)."""
    P = np.asarray(P, float)
    mu, wmu = np.polynomial.legendre.leggauss(nmu)
    phi = (np.arange(nphi) + 0.5) * 2 * PI / nphi
    MU, PH = np.meshgrid(mu, phi, indexing="ij")
    ST = np.sqrt(1 - MU**2)
    U = np.stack([ST * np.cos(PH), ST * np.sin(PH), MU], axis=-1).reshape(-1, 3)
    Lm = seg_len(P, U, np.zeros(3), a10) - seg_len(P, U, d10, b10)
    W = (wmu[:, None] * np.ones((1, nphi))).reshape(-1) * (2 * PI / nphi)
    return -(rho10 / (4 * PI * eps0)) * (U * (Lm * W)[:, None]).sum(axis=0)


# (a) uniform ball interior field by Gauss vs Coulomb rays (full ball, no cavity)
for P in ([0.3, 0.0, 0.0], [0.2, -0.5, 0.4]):
    P = np.array(P)
    mu, wmu = np.polynomial.legendre.leggauss(800)
    phi = (np.arange(1600) + 0.5) * 2 * PI / 1600
    MU, PH = np.meshgrid(mu, phi, indexing="ij")
    ST = np.sqrt(1 - MU**2)
    U = np.stack([ST * np.cos(PH), ST * np.sin(PH), MU], axis=-1).reshape(-1, 3)
    Wt = (wmu[:, None] * np.ones((1, 1600))).reshape(-1) * (2 * PI / 1600)
    Eb = -(rho10 / (4 * PI * eps0)) * (U * (seg_len(P, U, np.zeros(3), a10) * Wt)[:, None]).sum(axis=0)
    print(f"   (a) full ball at {P}: Coulomb rays {np.round(Eb,6)} vs rho r/(3eps0) {np.round(k10*P,6)}")
    check("3.10(a) uniform ball interior", Eb, k10 * P, rtol=1e-6, atol=1e-9)

# (b) cavity: uniform field rho d/(3 eps0)
print(f"   (b) predicted cavity field = rho d/(3 eps0) = {k10*d10} V/m")
rng = np.random.default_rng(1)
for i in range(4):
    while True:
        q = d10 + rng.uniform(-b10, b10, 3)
        if np.linalg.norm(q - d10) < 0.9 * b10:
            break
    Ebf = E10_coulomb_rays(q)
    print(f"      point {np.round(q,3)} in cavity: Coulomb rays {np.round(Ebf,5)} ; superposition {np.round(E10_superpose(q),5)}")
    check("3.10(b) cavity field uniform", Ebf, k10 * d10, rtol=1e-4, atol=2e-4)

# (c) P = (0.5, 0.5, 0)
P = np.array([0.5, 0.5, 0.0])
print(f"   (c) |P| = {np.linalg.norm(P):.4f} m < a ; |P-d| = {np.linalg.norm(P-d10):.4f} m > b (in the material)")
print(f"       b^3 = {b10**3:.3f} m^3 ; |P-d|^3 = {np.linalg.norm(P-d10)**3:.3f} m^3 ;"
      f" (P-d)/|P-d|^3 = {(P-d10)/np.linalg.norm(P-d10)**3} m^-2 ; at S: |S| = 2.5 m, |S-d| = {np.linalg.norm(np.array([2.5,0,0])-d10):.1f} m")
big = ball_field(P, np.zeros(3), a10, rho10)
small = ball_field(P, d10, b10, -rho10)
Ec = E10_superpose(P)
Ec_bf = E10_coulomb_rays(P)
print(f"      big ball {np.round(big,6)} ; cavity (-rho) {np.round(small,6)} ; total {np.round(Ec,6)} V/m, |E| = {np.linalg.norm(Ec):.4f}")
print(f"      Coulomb rays (no superposition): {np.round(Ec_bf,5)}")
check("3.10(c) superposition", Ec, [5.0, 2.44, 0.0], atol=1e-12)
check("3.10(c) brute force", Ec_bf, [5.0, 2.44, 0.0], rtol=1e-4, atol=2e-4)

# (d) S = (2.5, 0, 0)
S = np.array([2.5, 0.0, 0.0])
Ed = E10_superpose(S)
Ed_bf = E10_coulomb_rays(S)
print(f"   (d) at S: big {k10*a10**3/2.5**2:.4f} x ; cavity {-k10*b10**3/2.0**2:.4f} x ; total {np.round(Ed,6)} ; rays {np.round(Ed_bf,5)}")
print(f"       without cavity: {k10*a10**3/2.5**2:.4f} V/m along +x")
check("3.10(d) superposition", Ed, [1.44, 0, 0], atol=1e-12)
check("3.10(d) brute force", Ed_bf, [1.44, 0, 0], rtol=1e-4, atol=1e-4)
# wall continuity check at (0.5, 0.4, 0)
Wp = np.array([0.5, 0.4, 0.0])
inside_form = k10 * d10
outside_form = k10 * Wp - k10 * b10**3 * (Wp - d10) / np.linalg.norm(Wp - d10) ** 3
print(f"   wall point (0.5,0.4,0): cavity formula {inside_form} ; material formula {np.round(outside_form,12)}")
check("3.10 wall continuity", outside_form, inside_form, atol=1e-12)
print(f"   big-ball term at wall point: {np.round(k10*Wp,6)} ; cavity term: {np.round(-k10*b10**3*(Wp-d10)/np.linalg.norm(Wp-d10)**3,6)}")

# ---------------------------------------------------------------------------
hdr("3.11 Coaxial cable with a graded core")


def coax_rho1(rho0, a, b, c):
    return 2 * rho0 * a**2 / (3 * (c**2 - b**2))


def coax_E_closed(r, rho0, a, b, c):
    if r < a:
        return rho0 * r**2 / (3 * eps0 * a)
    if r < b:
        return rho0 * a**2 / (3 * eps0 * r)
    if r < c:
        return rho0 * a**2 / (3 * eps0 * r) * (c**2 - r**2) / (c**2 - b**2)
    return 0.0


def coax_rho(r, rho0, a, b, c):
    if r < a:
        return rho0 * r / a
    if b < r < c:
        return -coax_rho1(rho0, a, b, c)
    return 0.0


def coax_E_gauss_numeric(r, rho0, a, b, c):
    pts = [p for p in (a, b, c) if p < r]
    lam = quad(lambda rr: coax_rho(rr, rho0, a, b, c) * 2 * PI * rr, 0, r, points=pts or None, limit=200)[0]
    return lam / (2 * PI * eps0 * r)


def coax_E_coulomb_rays(s, rho0, a, b, c):
    """2-D Coulomb (infinite line elements) by rays from P=(s,0):
    E_x = (1/2 pi eps0) int rho (P-r')/|P-r'|^2 dA' = -(1/2 pi eps0) int_0^{2pi} cos(phi) [int_0^inf rho(P+t u) dt] dphi."""
    def ray(phi):
        cph = np.cos(phi)
        sph2 = max(1 - cph**2, 0.0)
        cuts = []
        for R in (a, b, c):
            disc = R**2 - s**2 * sph2
            if disc > 0:
                for t in (-s * cph - np.sqrt(disc), -s * cph + np.sqrt(disc)):
                    if t > 0:
                        cuts.append(t)
        if not cuts:
            return 0.0
        cuts = sorted(cuts)
        f = lambda t: coax_rho(np.sqrt(max(s * s + 2 * s * t * cph + t * t, 0.0)), rho0, a, b, c)
        edges = [0.0] + cuts
        return sum(quad(f, t0, t1, limit=200, epsabs=1e-14)[0] for t0, t1 in zip(edges[:-1], edges[1:]))
    # break the phi-integral at the directions tangent to each circle that P lies outside of
    pts = [PI / 2, PI, 3 * PI / 2]
    for R in (a, b, c):
        if R < s:
            al = np.arcsin(R / s)
            pts += [PI - al, PI + al]
    pts = sorted(set(pts))
    edges = [0.0] + pts + [2 * PI]
    val = sum(quad(lambda ph: np.cos(ph) * ray(ph), p0, p1, limit=200, epsabs=1e-14)[0]
              for p0, p1 in zip(edges[:-1], edges[1:]))
    return -val / (2 * PI * eps0)


for (rho0, a, b, c) in ((3e-6, 0.01, 0.02, 0.03), (1e-6, 0.02, 0.05, 0.06)):
    print(f"   parameter set rho0={rho0:g}, a={a}, b={b}, c={c}: rho1 = {coax_rho1(rho0,a,b,c):.6e} C/m^3")
    lam_core = quad(lambda rr: rho0 * rr / a * 2 * PI * rr, 0, a)[0]
    check("3.11 core charge/length = 2 pi rho0 a^2/3", lam_core, 2 * PI * rho0 * a**2 / 3)
    for r in (0.5 * a, a, 0.5 * (a + b), b, 0.5 * (b + c), 0.8 * c + 0.2 * b, 1.2 * c):
        cf = coax_E_closed(r, rho0, a, b, c)
        gq = coax_E_gauss_numeric(r, rho0, a, b, c)
        cr = coax_E_coulomb_rays(r, rho0, a, b, c)
        print(f"      r = {r*100:.3f} cm: closed {cf:11.4f}  Gauss-quad {gq:11.4f}  Coulomb-rays {cr:11.4f} V/m")
        check(f"3.11 closed vs Gauss r={r}", gq, cf, rtol=1e-7, atol=1e-6)
        check(f"3.11 closed vs Coulomb r={r}", cr, cf, rtol=2e-5, atol=1e-3)
rho0, a, b, c = 3e-6, 0.01, 0.02, 0.03
print(f"   PAGE: rho1 = {coax_rho1(rho0,a,b,c)*1e6:.4f} uC/m^3 (shell density = -{coax_rho1(rho0,a,b,c)*1e6:.1f} uC/m^3)")
print(f"         core charge per length 2 pi rho0 a^2/3 = {2*PI*rho0*a**2/3:.4e} C/m = {2*PI*rho0*a**2/3*1e9:.4f} nC/m"
      f" (= 2 pi x 1e-10) ; c^2 - b^2 = {(c**2-b**2)*1e4:.0f} cm^2")
print(f"         E(a) = rho0 a/(3 eps0) = {coax_E_closed(a-1e-15,rho0,a,b,c):.2f} V/m (from outside {coax_E_closed(a+1e-15,rho0,a,b,c):.2f})")
print(f"         E(b) = rho0 a^2/(3 eps0 b) = {coax_E_closed(b-1e-15,rho0,a,b,c):.2f} V/m (shell side {coax_E_closed(b+1e-15,rho0,a,b,c):.2f})")
print(f"         E(2.5 cm) = {coax_E_closed(0.025,rho0,a,b,c):.2f} V/m ; factor (c^2-r^2)/(c^2-b^2) = {(c**2-0.025**2)/(c**2-b**2):.4f};"
      f" rho0 a^2/(3 eps0 r) at 2.5 cm = {rho0*a**2/(3*eps0*0.025):.2f}")
print(f"         E(c-) = {coax_E_closed(c-1e-12,rho0,a,b,c):.3e} (continuous to 0)")
rr = np.linspace(1e-5, 0.04, 40001)
EE = np.array([coax_E_closed(r, rho0, a, b, c) for r in rr])
print(f"         max |E| on a scan = {EE.max():.2f} V/m at r = {rr[EE.argmax()]*100:.3f} cm")
rs_thin = -(2 * PI * rho0 * a**2 / 3) / (2 * PI * b)
print(f"   thin shell at r=b alternative: rho_s = -rho0 a^2/(3b) = {rs_thin:.4e} C/m^2 = {rs_thin*1e9:.3f} nC/m^2")
check("3.11 thin shell", rs_thin, -5e-9)
check("3.11 E(a)", coax_E_closed(a, rho0, a, b, c), rho0 * a / (3 * eps0))

# ---------------------------------------------------------------------------
hdr("3.12 Flux bookkeeping, line and sheet (rho_l = 6 nC/m on z axis, rho_s = 4 nC/m^2 on z=0)")
rl12, rs12 = 6.0, 4.0     # work in nC units


def D12(x, y, z):
    r2 = x * x + y * y
    if r2 == 0.0:   # on the line itself: its (horizontal) field is undefined; contributes nothing to D_z
        return np.array([0.0, 0.0, rs12 / 2 * np.sign(z)])
    return np.array([rl12 * x / (2 * PI * r2), rl12 * y / (2 * PI * r2), rs12 / 2 * np.sign(z)])


# (b) closed cylinder r<=1, -1<=z<=2
top = dblquad(lambda r, p: D12(r * np.cos(p), r * np.sin(p), 2.0)[2] * r, 0, 2 * PI, 0, 1)[0]
bot = dblquad(lambda r, p: -D12(r * np.cos(p), r * np.sin(p), -1.0)[2] * r, 0, 2 * PI, 0, 1)[0]
sid = dblquad(lambda z, p: D12(np.cos(p), np.sin(p), z) @ np.array([np.cos(p), np.sin(p), 0.0]), 0, 2 * PI, -1, 2,
              epsabs=1e-11)[0]
print(f"   (b) top {top:.6f} nC (2 pi = {2*PI:.6f}) ; bottom {bot:.6f} nC ; side {sid:.6f} nC ; total {top+bot+sid:.6f} nC")
print(f"       Q_enc = rho_l*3 + rho_s*pi = {rl12*3 + rs12*PI:.6f} nC (18 + 4 pi)")
check("3.12(b) top", top, 2 * PI)
check("3.12(b) bottom", bot, 2 * PI)
check("3.12(b) side", sid, 18.0)
check("3.12(b) total", top + bot + sid, 18 + 4 * PI)
# (c) cube |x|<=1, |y|<=1, 1<=z<=3
faces = {
    "top z=3": dblquad(lambda y, x: D12(x, y, 3.0)[2], -1, 1, -1, 1)[0],
    "bottom z=1": dblquad(lambda y, x: -D12(x, y, 1.0)[2], -1, 1, -1, 1)[0],
    "x=+1": dblquad(lambda z, y: D12(1.0, y, z)[0], -1, 1, 1, 3)[0],
    "x=-1": dblquad(lambda z, y: -D12(-1.0, y, z)[0], -1, 1, 1, 3)[0],
    "y=+1": dblquad(lambda z, x: D12(x, 1.0, z)[1], -1, 1, 1, 3)[0],
    "y=-1": dblquad(lambda z, x: -D12(x, -1.0, z)[1], -1, 1, 1, 3)[0],
}
for k, val in faces.items():
    print(f"   (c) {k:10s}: {val:+.6f} nC")
print(f"       total {sum(faces.values()):.6f} nC = rho_l*2 = {rl12*2:.1f} nC")
check("3.12(c) top", faces["top z=3"], 8.0)
check("3.12(c) bottom", faces["bottom z=1"], -8.0)
for k in ("x=+1", "x=-1", "y=+1", "y=-1"):
    check(f"3.12(c) side {k}", faces[k], 3.0)
# (d) dome: centre (0,0,1), radius 1, z>=1
def dome_integrand(th, p):
    nv = np.array([np.sin(th) * np.cos(p), np.sin(th) * np.sin(p), np.cos(th)])
    pt = np.array([0, 0, 1.0]) + nv
    return D12(*pt) @ nv * np.sin(th)


dome = dblquad(dome_integrand, 0, 2 * PI, 1e-12, PI / 2, epsabs=1e-10)[0]
dome_sheet = dblquad(lambda th, p: (rs12 / 2) * np.cos(th) * np.sin(th), 0, 2 * PI, 0, PI / 2)[0]
print(f"   (d) dome flux (direct) = {dome:.6f} nC ; 6 + 2 pi = {6+2*PI:.6f} ; sheet part alone {dome_sheet:.6f} (2 pi)")
check("3.12(d) dome", dome, 6 + 2 * PI, rtol=1e-6)
check("3.12(d) sheet part", dome_sheet, 2 * PI)
print(f"   numbers: 2 pi = {2*PI:.2f} ; 18 + 4 pi = {18+4*PI:.2f} ; 6 + 2 pi = {6+2*PI:.2f} nC")

# ---------------------------------------------------------------------------
print("\n" + "=" * 78)
print("ALL CHECKS PASSED" if not fails else f"{len(fails)} CHECK(S) FAILED: {fails}")
