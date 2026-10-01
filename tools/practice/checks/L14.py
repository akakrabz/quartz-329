#!/usr/bin/env python3
"""Verification of every number, sign and direction on
content-src/practice/14-faradays-law-and-induced-emf.md  (Lecture 14 practice page).

Rules followed (SPEC section 1): numpy/scipy only.
  * every flux Psi is a numerical surface integral of B.dS (dblquad / quad);
  * every emf is a centred finite difference -dPsi/dt, and for moving loops also a
    numerical line integral of (v x B).dl (plus E.dl where an induced E exists);
  * every direction comes from an explicit np.cross (Biot-Savart for the field of
    an induced current, I dl x B for forces);
  * ODEs with scipy.integrate.solve_ivp;
  * symbolic results are checked at >= 2 parameter sets.
Output: L14.out (run: python3 L14.py > L14.out).
"""
import numpy as np
from scipy.integrate import quad, dblquad, solve_ivp
from scipy.optimize import brentq

mu0 = 4e-7 * np.pi
XH, YH, ZH = np.eye(3)
TOL = dict(epsabs=1e-13, epsrel=1e-11)
FAILS = []


def check(label, got, want, rel=1e-6, ab=1e-12):
    ok = abs(got - want) <= max(ab, rel * abs(want))
    print(f"   [{'ok' if ok else 'FAIL'}] {label}: computed {got:.10g}  expected {want:.10g}")
    if not ok:
        FAILS.append(label)


def fd(f, t, h=1e-6):
    """centred finite difference df/dt"""
    return (f(t + h) - f(t - h)) / (2 * h)


def flux_param(Bf, r0, e1, e2, t):
    """flux of B through the parallelogram r0 + u e1 + v e2 (u,v in [0,1]), dS = (e1 x e2) du dv"""
    n = np.cross(e1, e2)
    val, _ = dblquad(lambda v, u: Bf(r0 + u * e1 + v * e2, t) @ n, 0, 1, 0, 1, **TOL)
    return val


def flux_triangle(Bf, a, b, c, t):
    """flux through triangle a->b->c (orientation by the right-hand rule from that order)"""
    e1, e2 = b - a, c - a
    n = np.cross(e1, e2)
    val, _ = dblquad(lambda v, u: Bf(a + u * e1 + v * e2, t) @ n, 0, 1, 0, lambda u: 1 - u, **TOL)
    return val


def flux_disk(Bf, centre, R, t):
    """flux through a horizontal disk (normal +z) of radius R"""
    val, _ = dblquad(lambda rho, ph: Bf(centre + np.array([rho * np.cos(ph), rho * np.sin(ph), 0.0]), t) @ ZH * rho,
                     0, 2 * np.pi, 0, R, **TOL)
    return val


def seg_int(F, p0, p1, t, points=None):
    """line integral of F(r,t).dl along the straight segment p0 -> p1"""
    d = p1 - p0
    val, _ = quad(lambda s: F(p0 + s * d, t) @ d, 0, 1, points=points, limit=200, **TOL)
    return val


def poly_int(F, pts, t, closed=True):
    n = len(pts)
    m = n if closed else n - 1
    return sum(seg_int(F, pts[i], pts[(i + 1) % n], t) for i in range(m))


def circle_int(F, centre, R, t, sense=+1):
    """line integral around the horizontal circle, sense=+1 counter-clockwise seen from +z"""
    def integrand(ph):
        r = centre + R * np.array([np.cos(ph), np.sin(ph), 0.0])
        dl = sense * R * np.array([-np.sin(ph), np.cos(ph), 0.0])
        return F(r, t) @ dl
    val, _ = quad(integrand, 0, 2 * np.pi, limit=200, **TOL)
    return val


def bs_polygon(pts, I, rf, nseg=4000):
    """Biot-Savart field at rf of current I flowing along the closed polygon pts (in that order)"""
    B = np.zeros(3)
    n = len(pts)
    for i in range(n):
        p0, p1 = pts[i], pts[(i + 1) % n]
        s = (np.arange(nseg) + 0.5) / nseg
        src = p0 + s[:, None] * (p1 - p0)
        dl = (p1 - p0) / nseg
        R = rf - src
        Rn = np.linalg.norm(R, axis=1)[:, None]
        B += mu0 * I / (4 * np.pi) * np.sum(np.cross(np.broadcast_to(dl, R.shape), R) / Rn**3, axis=0)
    return B


def circle_pts(centre, R, sense=+1, n=720):
    ph = np.linspace(0, 2 * np.pi, n, endpoint=False) * sense
    return [centre + R * np.array([np.cos(p), np.sin(p), 0.0]) for p in ph]


def sense_word(emf):
    return "counter-clockwise seen from +z" if emf > 0 else "clockwise seen from +z"


# ======================================================================================
print("=" * 90)
print("14.1 Flux through a tilted loop")
print("=" * 90)
B1 = lambda r, t: np.array([0.0, 0.0, 0.8 - 2.0 * t])
c = [np.array([0, 0, 0.0]), np.array([0.2, 0, 0]), np.array([0.2, 0.1, 0.1 * np.sqrt(3)]), np.array([0, 0.1, 0.1 * np.sqrt(3)])]
e1, e2 = c[1] - c[0], c[2] - c[1]
Avec = np.cross(e1, e2)
nhat = Avec / np.linalg.norm(Avec)
print(f"   edges a = {e1}, b = {e2};  a x b = {Avec} m^2,  |a x b| = {np.linalg.norm(Avec):.6f} m^2")
print(f"   n-hat = {nhat}   (expect (0, -sqrt3/2, 1/2) = (0, {-np.sqrt(3)/2:.6f}, 0.5))")
print(f"   angle between n-hat and z = {np.degrees(np.arccos(nhat @ ZH)):.4f} deg (= tilt of the plane from xy)")
Psi1 = lambda t: flux_param(B1, c[0], e1, e2, t)
for t in (0.0, 0.1, 0.2):
    check(f"Psi({t}) numeric vs 0.016-0.04t", Psi1(t), 0.016 - 0.04 * t)
emf1 = -fd(Psi1, 0.1, 1e-4)
check("emf along C = -dPsi/dt [V]", emf1, 0.04)
check("I = emf/0.5 Ohm [A]", emf1 / 0.5, 0.08)
# tent surface over the same rim (apex above the centre) -- any surface on C gives the same flux
apex = (c[0] + c[2]) / 2 + 0.15 * nhat + np.array([0.03, -0.02, 0.05])
tent = sum(flux_triangle(B1, c[i], c[(i + 1) % 4], apex, 0.1) for i in range(4))
check("tent-surface flux at t=0.1 equals flat-square flux", tent, Psi1(0.1))
# direction: current along C (emf>0) -> its field at the loop centre (Biot-Savart)
Bind = bs_polygon(c, +1.0, (c[0] + c[2]) / 2)
print(f"   field at centre of a +1 A current along C: {Bind} T; B_ind.n = {Bind @ nhat:.3e} (>0), B_ind.z = {Bind[2]:.3e} (>0)")
print("   applied B_z decreasing (dB_z/dt = -2 T/s) and the induced field has +z component -> props it up: Lenz OK")
print(f"   ANSWER 14.1: n = (0,-sqrt3/2,1/2); Psi = (0.8-2t)(0.02) = 0.016-0.04t Wb; emf = +0.04 V = 40 mV along C; I = 80 mA along C")
print("   given: corners (0,0,0), (0.2,0,0), (0.2,0.1,0.1sqrt3), (0,0.1,0.1sqrt3) m; B = (0.8-2t) z T; R = 0.5 Ohm")
print(f"   |a| = {np.linalg.norm(e1):.4f} m, |b| = {np.linalg.norm(e2):.4f} m, a.b = {e1 @ e2:.1e}: a 0.2 m x 0.2 m square")
print(f"   0.02 sqrt3 = {0.02*np.sqrt(3):.8f} = -(a x b)_y; shadow on xy: 0.2 m x 0.1 m rectangle, area {0.2*0.1:.4f} m^2 = (a x b)_z")

# ======================================================================================
print("=" * 90)
print("14.2 Current from a ramping field (MC)")
print("=" * 90)
for B0 in (+0.7, -0.7):           # field along +z decreasing, or along -z growing: same dB/dt
    B2 = lambda r, t, B0=B0: np.array([0.0, 0.0, B0 - 5.0 * t])
    sq = [np.array([-0.1, -0.15, 0]), np.array([0.1, -0.15, 0]), np.array([0.1, 0.15, 0]), np.array([-0.1, 0.15, 0])]
    Psi2 = lambda t: flux_param(B2, sq[0], sq[1] - sq[0], sq[2] - sq[1], t)   # CCW from +z: dS = +z
    emf2 = -fd(Psi2, 0.0, 1e-4)
    print(f"   B(0) = {B0:+.1f} z T: Psi(0) = {Psi2(0):+.6f} Wb, emf (CCW) = {emf2:+.6f} V -> {sense_word(emf2)}")
check("area [m^2]", np.linalg.norm(np.cross(sq[1] - sq[0], sq[2] - sq[1])), 0.06)
check("|emf| [V]", abs(emf2), 0.3)
check("|I| = |emf|/3 Ohm [A]", abs(emf2) / 3, 0.1)
Bc = bs_polygon(sq, +1.0, np.zeros(3))
print(f"   CCW current -> field at centre {Bc} (along +z): opposes the decrease of B_z  -> option (b) 100 mA CCW")
check("distractor: 600 cm^2 read as 0.6 m^2 -> I [A]", 5 * 0.6 / 3, 1.0)
check("distractor: 600 cm^2 read as 0.006 m^2 -> I [A]", 5 * 0.006 / 3, 0.01)
print("   curl E check: for E_phi = -(r/2) dB/dt (symmetric about the z axis), (curl E)_z = -dB/dt = +5 /s != 0")
print("   given: 0.2 m x 0.3 m rectangle (600 cm^2) in z = 0, R = 3 Ohm, B = (0.7 - 5t) z T")
check("time at which B_z passes through zero [s] (the current does not reverse there)", brentq(lambda t: 0.7 - 5.0 * t, 0, 1), 0.14)

# ======================================================================================
print("=" * 90)
print("14.3 Magnet pulled up through a ring (MC)")
print("=" * 90)
mmag, Rr, vmag = 1.0, 0.05, 0.5      # dipole moment [A m^2], ring radius [m], magnet speed [m/s]


def B_dip(r, rm, m):
    R = r - rm
    Rn = np.linalg.norm(R)
    return mu0 / (4 * np.pi) * (3 * (m @ R) * R / Rn**5 - m / Rn**3)


def Psi_ring(h, mvec):
    return flux_disk(lambda r, t: B_dip(r, np.array([0, 0, h]), mvec), np.zeros(3), Rr, 0.0)


for case, mvec, h_of_t in (("north UP, pulled up   (this problem)", mmag * ZH, lambda t: -0.5 + vmag * t),
                           ("north DOWN, dropped   (SP18 original)", -mmag * ZH, lambda t: +0.5 - vmag * t)):
    print(f"   case: {case}")
    for label, hpos in (("approaching", -0.1 if mvec[2] > 0 else 0.1), ("receding", 0.1 if mvec[2] > 0 else -0.1)):
        tpos = brentq(lambda t: h_of_t(t) - hpos, -10, 10)
        Psi = lambda t: Psi_ring(h_of_t(t), mvec)
        emf = -fd(Psi, tpos, 1e-5)
        closed = mu0 * mvec[2] * Rr**2 / (2 * (Rr**2 + hpos**2)**1.5)
        check(f"  {label}: flux numeric vs closed form mu0 m R^2/2(R^2+h^2)^1.5 at h={hpos}", Psi(tpos), closed)
        # magnet frame: ring moves with -v_magnet through the static dipole field -> motional emf
        vring = -np.array([0, 0, fd(h_of_t, tpos)])
        mot = circle_int(lambda r, t: np.cross(vring, B_dip(r, np.array([0, 0, hpos]), mvec)), np.zeros(3), Rr, 0.0)
        check(f"  {label}: motional emf in the magnet's frame = -dPsi/dt", mot, emf, rel=1e-5)
        sense = +1 if emf > 0 else -1
        Bc = bs_polygon(circle_pts(np.zeros(3), Rr, sense), 1.0, np.zeros(3))
        # force on the ring (1 A in the induced sense) from the magnet's field
        F = np.zeros(3)
        for ph in np.linspace(0, 2 * np.pi, 2000, endpoint=False):
            r = Rr * np.array([np.cos(ph), np.sin(ph), 0])
            dl = sense * Rr * (2 * np.pi / 2000) * np.array([-np.sin(ph), np.cos(ph), 0])
            F += np.cross(dl, B_dip(r, np.array([0, 0, hpos]), mvec))
        print(f"     {label}: emf(CCW) = {emf:+.4e} V -> current {sense_word(emf)}; induced B at centre z-comp {Bc[2]:+.3e};"
              f" force on ring F_z = {F[2]:+.3e} N per A (magnet moving {'+z' if vring[2] < 0 else '-z'})")
print("   -> north up, pulled up: clockwise while approaching, counter-clockwise while receding = option (b)")
print("   -> SP18 version (north down, dropped): counter-clockwise then clockwise = distractor (a)")
print("   force on ring is along the magnet's velocity in both phases: the magnet feels the reaction against its motion")
print(f"   model: dipole moment {mmag} A m^2, ring radius {Rr} m (5 cm), magnet speed {vmag} m/s")

# ======================================================================================
print("=" * 90)
print("14.4 Lenz's rule true or false")
print("=" * 90)
B0, r0, rdot = 0.5, 0.1, -0.02
Ba = lambda r, t: np.array([0, 0, B0])
rad = lambda t: r0 + rdot * t
Psia = lambda t: flux_disk(Ba, np.zeros(3), rad(t), t)
emfa = -fd(Psia, 0.5, 1e-4)
mota = circle_int(lambda r, t: np.cross(rdot * r / np.linalg.norm(r), Ba(r, t)), np.zeros(3), rad(0.5), 0.5)
check("(a) shrinking loop: motional emf = -dPsi/dt", mota, emfa)
Bca = bs_polygon(circle_pts(np.zeros(3), rad(0.5), +1 if emfa > 0 else -1), 1.0, np.zeros(3))
print(f"   (a) emf(CCW) = {emfa:+.4e} V -> {sense_word(emfa)}: TRUE; induced field z-comp {Bca[2]:+.2e} (parallel to applied +z)")
vb = np.array([2.0, 0, 0])
sqb = lambda t: [np.array([0, 0, 0.0]) + vb * t + p for p in (np.zeros(3), 0.3 * XH, 0.3 * XH + 0.3 * YH, 0.3 * YH)]
Psib = lambda t: flux_param(Ba, sqb(t)[0], 0.3 * XH, 0.3 * YH, t)
emfb = -fd(Psib, 1.0, 1e-4)
motb = poly_int(lambda r, t: np.cross(vb, Ba(r, t)), sqb(1.0), 1.0)
print(f"   (b) translating loop: v x B = {np.cross(vb, Ba(0, 0))} V/m (nonzero), -dPsi/dt = {emfb:.2e} V, loop integral of v x B = {motb:.2e} V: FALSE")
tau = 2.0
Bcf = lambda r, t: np.array([0, 0, -B0 * np.exp(-t / tau)])
Psic = lambda t: flux_disk(Bcf, np.zeros(3), r0, t)
emfc = -fd(Psic, 1.0, 1e-4)
Bcc = bs_polygon(circle_pts(np.zeros(3), r0, +1 if emfc > 0 else -1), 1.0, np.zeros(3))
print(f"   (c) B = -B0 exp(-t/tau) z: Psi(1) = {Psic(1.0):+.4e} Wb, emf(CCW) = {emfc:+.4e} V -> {sense_word(emfc)}: TRUE;"
      f" induced field z-comp {Bcc[2]:+.2e} (parallel to applied -z)")
print(f"   (d) cut ring: emf of the closed path through the gap is unchanged = {emfc:+.4e} V (not zero), current 0: FALSE")
print(f"   (e) induced field parallel to the applied field in (a) [{np.sign(Bca[2])*np.sign(B0):+.0f}] and (c) [{np.sign(Bcc[2])*np.sign(-B0):+.0f}]: FALSE")
print("   given: B = 0.5 z T; (a) radius 0.1 m shrinking at 0.02 m/s; (b) 0.3 m square, v = 2 x m/s; (c) radius 0.1 m, B = -0.5 exp(-t/2) z T (tau = 2 s)")
check("(a) emf at t = 0 (r = 0.1 m) = 2 pi r |dr/dt| B [V]", -fd(Psia, 0.0, 1e-4), 2 * np.pi * 0.1 * 0.02 * 0.5)
print(f"   (a) emf at the start = {-fd(Psia, 0.0, 1e-4)*1e3:.4f} mV (counter-clockwise)")
print(f"   (a) v x B on the ring at (0.1,0,0) = {np.cross(rdot * XH, Ba(0.1 * XH, 0))} V/m: +0.01 V/m along +y = +phi there -> counter-clockwise")
print(f"   (b) flux of the square = {Psib(0.5):.4f} Wb (constant); edge integrals of v x B (bottom, right, top, left) ="
      f" {[round(seg_int(lambda r, t: np.cross(vb, Ba(r, t)), sqb(1.0)[i], sqb(1.0)[(i + 1) % 4], 1.0), 6) for i in range(4)]} V")
print(f"   (c) Psi(1 s) = {Psic(1.0)*1e3:.3f} mWb, emf(1 s) = {emfc*1e3:.3f} mV")

# ======================================================================================
print("=" * 90)
print("14.5 Find the error, double-counted emf")
print("=" * 90)
B5, l5, v5, R5 = 0.3, 0.4, 5.0, 0.6
Bf5 = lambda r, t: np.array([0, 0, B5])
xb = lambda t: v5 * t
Psi5 = lambda t: dblquad(lambda y, x: Bf5(np.array([x, y, 0]), t) @ ZH, 0, xb(t), 0, l5, **TOL)[0]   # CCW: dS=+z
check("Psi(t=0.2) = B l v t [Wb]", Psi5(0.2), 0.6 * 0.2)
emf5 = -fd(Psi5, 0.2, 1e-4)
check("flux route: emf(CCW) = -dPsi/dt [V]", emf5, -0.6)
vxb = np.cross(v5 * XH, Bf5(0, 0))
mot5 = seg_int(lambda r, t: np.cross(v5 * XH, Bf5(r, t)), np.array([xb(0.2), 0, 0]), np.array([xb(0.2), l5, 0]), 0.2)
print(f"   v x B = {vxb} V/m (along -y: pushes + charge to the y=0 end of the bar)")
check("motional route: integral of v x B up the bar (CCW direction +y) [V]", mot5, -0.6)
print("   transformer part: dB/dt = 0 everywhere -> loop integral of E = 0; the two routes are the SAME emf")
print(f"   student: {emf5:+.2f} + ({mot5:+.2f}) = {emf5 + mot5:+.2f} V, I = {abs(emf5 + mot5)/R5:.2f} A  (wrong, doubled)")
I5 = abs(emf5) / R5
check("correct |emf| [V]", abs(emf5), 0.6)
check("correct I [A]", I5, 1.0)
F5 = np.cross(I5 * (-l5 * YH), Bf5(0, 0))       # current down the bar (clockwise)
print(f"   emf(CCW) < 0 -> current {sense_word(emf5)}, i.e. down the bar (-y); force on bar I l x B = {F5} N (drag)")
print("   Lenz: +z flux growing, clockwise current makes -z field inside: OK")
print(f"   given: rails on y = 0 and y = {l5} m, R = {R5} Ohm at x = 0, bar at x = {v5} t m, B = {B5} z T; Psi = {B5*l5*v5:.2f} t Wb")

# ======================================================================================
print("=" * 90)
print("14.6 Rotating rod on a circular rail")
print("=" * 90)


def rod(Bz, L, w, R, t=0.013):
    th = w * t
    u = np.array([np.cos(th), np.sin(th), 0])
    Bf = lambda r, tt: np.array([0, 0, Bz])
    vel = lambda r: np.cross(w * ZH, r)
    emf_rod = quad(lambda s: np.cross(vel(s * u), Bf(s * u, t)) @ u, 0, L, **TOL)[0]   # pivot -> rim
    # closed path C: pivot -> rod -> rail arc back to phi=0 -> resistor along x axis -> pivot; encloses the sector,
    # traversed clockwise seen from +z  =>  dS = -z
    Psi = lambda tt: dblquad(lambda rho, ph: Bf(0, tt) @ (-ZH) * rho, 0, w * tt, 0, L, **TOL)[0]
    emf_flux = -fd(Psi, t, 1e-6)
    I = emf_rod / R
    tau_vec = quad(lambda s: np.cross(s * u, np.cross(I * u, Bf(s * u, t)))[2], 0, L, **TOL)[0]   # current outward
    return emf_rod, emf_flux, I, tau_vec, np.cross(vel(L * u), Bf(0, 0)) @ u


e_r, e_f, I6, tz, vxb_r = rod(0.2, 0.5, 40.0, 0.25)
check("emf along the rod pivot->rim = integral of (v x B).dl [V]", e_r, 1.0)
check("closed form B w L^2/2 [V]", 0.5 * 0.2 * 40 * 0.25, 1.0)
check("flux route -dPsi/dt around C (sector, dS=-z) [V]", e_f, 1.0)
print(f"   (v x B).u_rod at the tip = {vxb_r:+.3f} V/m > 0: points outward -> rim end is the + terminal")
check("I [A]", I6, 4.0)
check("magnetic torque about z [N m] (current outward)", tz, -0.1)
check("applied torque [N m]", -tz, 0.1)
check("mechanical power tau*omega [W]", -tz * 40, 4.0)
check("I^2 R [W]", I6**2 * 0.25, 4.0)
check("emf * I [W]", e_r * I6, 4.0)
e_r2, e_f2, *_ = rod(0.7, 0.3, 25.0, 1.0)
check("2nd parameter set (B=0.7,L=0.3,w=25): rod integral vs BwL^2/2", e_r2, 0.5 * 0.7 * 25 * 0.09)
check("2nd parameter set: flux route vs BwL^2/2", e_f2, 0.5 * 0.7 * 25 * 0.09)
print("   Lenz: the sector's +z flux grows; current along C (clockwise) makes -z field in the sector: OK")
print("   given: L = 0.5 m, omega = 40 rad/s (CCW from +z), B = 0.2 z T, R = 0.25 Ohm, rail radius 0.5 m, lead along the x axis to (0.5,0,0)")
print(f"   L^2 = {0.5**2:.4f} m^2; torque I B L^2/2 = {4.0*0.2*0.25/2:.4f} N m")

# ======================================================================================
print("=" * 90)
print("14.7 Generator coil in a uniform field")
print("=" * 90)


def coil(N, w, h, Bvec, om):
    Bf = lambda r, t: Bvec
    u = lambda t: np.array([np.cos(om * t), np.sin(om * t), 0])
    nh = lambda t: np.array([-np.sin(om * t), np.cos(om * t), 0])
    corners = lambda t: [-w / 2 * u(t) + h / 2 * ZH, w / 2 * u(t) + h / 2 * ZH, w / 2 * u(t) - h / 2 * ZH, -w / 2 * u(t) - h / 2 * ZH]
    Psi = lambda t: flux_param(Bf, corners(t)[0], corners(t)[1] - corners(t)[0], corners(t)[2] - corners(t)[1], t)
    emf_flux = lambda t: -N * fd(Psi, t, 1e-7)
    emf_mot = lambda t: N * poly_int(lambda r, tt: np.cross(np.cross(om * ZH, r), Bf(r, tt)), corners(t), t)
    return Psi, emf_flux, emf_mot, nh, corners


N7, w7, h7, B7, om7, R7 = 50, 0.04, 0.05, 0.25 * XH, 1800 * 2 * np.pi / 60, 10.0
check("omega = 1800 rpm [rad/s] = 60 pi", om7, 60 * np.pi)
Psi7, ef7, em7, nh7, cn7 = coil(N7, w7, h7, B7, om7)
cc = cn7(0.0)
print(f"   n(0) = {nh7(0)}; (c2-c1)x(c3-c2) at t=0 = {np.cross(cc[1]-cc[0], cc[2]-cc[1])} (along +y: corner order matches n)")
E0 = N7 * 0.25 * w7 * h7 * om7
check("peak emf N B A w [V] = 1.5 pi", E0, 1.5 * np.pi)
for t in (0.0, 1 / 480, 1 / 180, 0.0123):
    check(f"Psi per turn at t={t:.5f} vs -5e-4 sin(wt)", Psi7(t), -5e-4 * np.sin(om7 * t))
    check(f"emf flux route at t={t:.5f} vs 1.5pi cos(wt)", ef7(t), E0 * np.cos(om7 * t), rel=1e-6, ab=1e-9)
    check(f"emf motional route at t={t:.5f} vs 1.5pi cos(wt)", em7(t), E0 * np.cos(om7 * t), rel=1e-9, ab=1e-9)
# motional at t=0, edge by edge (per turn)
per_edge = [seg_int(lambda r, tt: np.cross(np.cross(om7 * ZH, r), B7), cc[i], cc[(i + 1) % 4], 0.0) for i in range(4)]
print(f"   t=0 per-turn edge contributions (top, right, bottom, left) = {np.round(per_edge, 6)} V")
check("speed of a 5 cm side, w*w/2 [m/s] = 1.2 pi", om7 * w7 / 2, 1.2 * np.pi)
check("per side |v x B| h [V] = 0.015 pi", om7 * w7 / 2 * 0.25 * h7, 0.015 * np.pi)
print(f"   v at right side (t=0) = {np.cross(om7*ZH, cc[1])}; v x B = {np.cross(np.cross(om7*ZH, cc[1]), B7)} (along -z, the path runs -z there)")
check("current amplitude [A] = 0.15 pi", E0 / R7, 0.15 * np.pi)
Tper = 2 * np.pi / om7
Pavg = quad(lambda t: (E0 * np.cos(om7 * t))**2 / R7, 0, Tper, **TOL)[0] / Tper
check("average power [W] (numerical time average)", Pavg, (1.5 * np.pi)**2 / 20)
print(f"   average power = {Pavg:.4f} W")
print("   Lenz just after t=0: per-turn flux becomes negative (along -y); positive emf -> current along C makes +y field: opposes OK")
Psi7b, ef7b, em7b, *_ = coil(20, 0.03, 0.07, 0.4 * YH + 0.1 * ZH, 100 * np.pi)
# B along y (axis z): flux = B . n A = 0.4 cos(wt) A ; emf = N 0.4 A w sin(wt)
for t in (0.001, 0.0047):
    check(f"2nd set (N=20,B_y=0.4,w=100pi) flux route at t={t}", ef7b(t), 20 * 0.4 * 0.0021 * 100 * np.pi * np.sin(100 * np.pi * t), ab=1e-9)
    check(f"2nd set motional route at t={t}", em7b(t), 20 * 0.4 * 0.0021 * 100 * np.pi * np.sin(100 * np.pi * t), ab=1e-9)
print("   given: N = 50, 0.04 m wide x 0.05 m tall, 1800 rpm about z, B = 0.25 x T, R = 10 Ohm")
print(f"   area per turn = {w7*h7:.4f} m^2; sides at x = +-{w7/2:.2f} m at t = 0")
check("omega t at t = 1/180 s = pi/3", om7 / 180, np.pi / 3)
check("emf at t = 1/180 s [V] = 0.75 pi", ef7(1 / 180), 0.75 * np.pi, rel=1e-6)
check("v x B on the x = +2 cm side at t = 0, z-comp [V/m] = -0.3 pi", np.cross(np.cross(om7 * ZH, cc[1]), B7)[2], -0.3 * np.pi)
check("motional emf of one turn at t = 0 [V] = 0.03 pi", sum(per_edge), 0.03 * np.pi)
print(f"   emf(1/180 s) = {ef7(1/180):.4f} V; current amplitude = {E0/R7:.4f} A")

# ======================================================================================
print("=" * 90)
print("14.8 Square loop in a graded field")
print("=" * 90)


def graded(B0, a, s, v, x10, R, t=0.0123):
    Bf = lambda r, tt: np.array([B0 * r[2] / a, 0, B0 * r[0] / a])   # = (B0/a)(z x + x z); B0 x/a z on z = 0
    vel = np.array([v, 0, 0])
    corners = lambda tt: [np.array([x10 + v * tt, 0, 0]), np.array([x10 + s + v * tt, 0, 0]),
                          np.array([x10 + s + v * tt, s, 0]), np.array([x10 + v * tt, s, 0])]          # CCW from +z
    Psi = lambda tt: flux_param(Bf, corners(tt)[0], s * XH, s * YH, tt)
    emf_f = -fd(Psi, t, 1e-5)
    emf_m = poly_int(lambda r, tt: np.cross(vel, Bf(r, tt)), corners(t), t)
    return Bf, Psi, emf_f, emf_m, corners


Bf8, Psi8, ef8, em8, cn8 = graded(0.5, 1.0, 0.2, 3.0, 0.1, 0.05)
for t in (0.0, 0.1):
    check(f"Psi({t}) vs 0.004 + 0.06 t [Wb]", Psi8(t), 0.004 + 0.06 * t)
check("emf(CCW) flux route [V]", ef8, -0.06)
check("emf(CCW) motional route [V]", em8, -0.06)
cc = cn8(0.0123)
edges = [seg_int(lambda r, tt: np.cross(3.0 * XH, Bf8(r, tt)), cc[i], cc[(i + 1) % 4], 0.0123) for i in range(4)]
print(f"   edge contributions (bottom, right, top, left) at t=0.0123 = {np.round(edges, 6)} V")
check("right edge = -v B(x2) s at t=0 [V]", seg_int(lambda r, tt: np.cross(3.0 * XH, Bf8(r, tt)), cn8(0)[1], cn8(0)[2], 0.0), -3 * 0.15 * 0.2)
check("left edge = +v B(x1) s at t=0 [V]", seg_int(lambda r, tt: np.cross(3.0 * XH, Bf8(r, tt)), cn8(0)[3], cn8(0)[0], 0.0), 3 * 0.05 * 0.2)
I8 = abs(ef8) / 0.05
check("I [A]", I8, 1.2)
print(f"   emf(CCW) < 0 -> current {sense_word(ef8)}")
cw = cn8(0.0123)[::-1]                                   # clockwise order
F8 = np.zeros(3)
for i in range(4):
    p0, p1 = cw[i], cw[(i + 1) % 4]
    for k in range(3):
        F8[k] += quad(lambda s_: np.cross(I8 * (p1 - p0), Bf8(p0 + s_ * (p1 - p0), 0))[k], 0, 1, **TOL)[0]
print(f"   magnetic force on the loop = {F8} N")
check("F_x [N]", F8[0], -0.024)
check("applied force [N]", -F8[0], 0.024)
check("power F v [W]", -F8[0] * 3, 0.072)
check("I^2 R [W]", I8**2 * 0.05, 0.072)
# circle of the same area, same velocity
Rc = np.sqrt(0.04 / np.pi)
Psic8 = lambda t: flux_disk(Bf8, np.array([0.2 + 3 * t, 0.1, 0]), Rc, t)
ec8 = -fd(Psic8, 0.0123, 1e-5)
mc8 = circle_int(lambda r, t: np.cross(3.0 * XH, Bf8(r, t)), np.array([0.2 + 3 * 0.0123, 0.1, 0]), Rc, 0.0123)
check("circle of equal area: flux route [V]", ec8, -0.06)
check("circle of equal area: motional route [V]", mc8, -0.06)
# the field (B0/a)(z x + x z) is divergence- and curl-free
h = 1e-5
p = np.array([0.23, 0.07, 0.011])
J = np.array([(Bf8(p + h * e, 0) - Bf8(p - h * e, 0)) / (2 * h) for e in np.eye(3)]).T     # J[i,j] = dB_i/dx_j
print(f"   div B = {np.trace(J):.2e}, curl B = {[J[2,1]-J[1,2], J[0,2]-J[2,0], J[1,0]-J[0,1]]}")
_, _, ef8b, em8b, _ = graded(0.8, 2.0, 0.3, 1.5, -0.4, 1.0)
check("2nd set (B0=0.8,a=2,s=0.3,v=1.5): flux route vs -B0 s^2 v/a", ef8b, -0.8 * 0.09 * 1.5 / 2)
check("2nd set: motional route vs -B0 s^2 v/a", em8b, -0.8 * 0.09 * 1.5 / 2)
print("   given: B = 0.5 (z x + x z) T, square of side 0.2 m, R = 0.05 Ohm, v = 3 x m/s; at t = 0: 0.1 <= x <= 0.3 m, 0 <= y <= 0.2 m")
Bz8 = lambda x: Bf8(np.array([x, 0, 0]), 0)[2]
print(f"   B_z at x1 = 0.1 m: {Bz8(0.1):.4f} T; at x2 = 0.3 m: {Bz8(0.3):.4f} T; at the centre 0.2 m: {Bz8(0.2):.4f} T; B(x2)-B(x1) = {Bz8(0.3)-Bz8(0.1):.4f} T")
print(f"   v x B at (1,0,0) = {np.cross(3.0 * XH, Bf8(np.array([1.0, 0, 0]), 0))} V/m  -> v x B = -1.5 x y-hat V/m; area = {0.2**2:.4f} m^2")
check("Psi(0) = B_z(centre) x area [Wb]", Bz8(0.2) * 0.04, Psi8(0.0))
check("emf for any shape = -0.5 v A [V]", -0.5 * 3 * 0.04, ef8)
cw0 = cn8(0.0)[::-1]
Fe = []
for i in range(4):
    p0, p1 = cw0[i], cw0[(i + 1) % 4]
    Fe.append(np.array([quad(lambda s_: np.cross(I8 * (p1 - p0), Bf8(p0 + s_ * (p1 - p0), 0))[k], 0, 1, **TOL)[0] for k in range(3)]))
print("   per-edge forces at t = 0, clockwise current (top, right, bottom, left) [N]:", [np.round(f, 6).tolist() for f in Fe])
check("force on right edge [N]", Fe[1][0], -0.036)
check("force on left edge [N]", Fe[3][0], 0.012)

# ======================================================================================
print("=" * 90)
print("14.9 Loop crossing a field strip")
print("=" * 90)


def strip_problem(B0, w, s, v, R):
    Bz = lambda x: B0 if (0 < x < w) else 0.0
    Bf = lambda r, t: np.array([0, 0, Bz(r[0])])
    xl = lambda t: v * t                     # leading edge
    xt = lambda t: v * t - s                 # trailing edge

    def Psi(t):                              # CCW, dS = +z
        a, b = xt(t), xl(t)
        lo, hi = max(a, 0.0), min(b, w)
        if hi <= lo:
            return 0.0
        return dblquad(lambda y, x: Bz(x), lo, hi, 0, s, **TOL)[0]

    def corners(t):
        return [np.array([xt(t), 0, 0]), np.array([xl(t), 0, 0]), np.array([xl(t), s, 0]), np.array([xt(t), s, 0])]

    def mot(t):
        return poly_int(lambda r, tt: np.cross(v * XH, Bf(r, tt)), corners(t), t)

    def force(t, I_ccw):
        F = np.zeros(3)
        cs = corners(t)
        for i in range(4):
            p0, p1 = cs[i], cs[(i + 1) % 4]
            for k in range(3):
                pts_ = [q for q in ((0 - p0[0]) / (p1[0] - p0[0]) if p1[0] != p0[0] else None,
                                    (w - p0[0]) / (p1[0] - p0[0]) if p1[0] != p0[0] else None) if q is not None and 0 < q < 1]
                F[k] += quad(lambda u_: np.cross(I_ccw * (p1 - p0), Bf(p0 + u_ * (p1 - p0), t))[k], 0, 1,
                             points=pts_ or None, **TOL)[0]
        return F
    return Psi, mot, force, corners


B9, w9, s9, v9, R9 = -0.4, 0.5, 0.2, 5.0, 0.1
Psi9, mot9, force9, cn9 = strip_problem(B9, w9, s9, v9, R9)
print("   phase boundaries: entry 0 -> s/v = 0.04 s; fully inside 0.04 -> w/v = 0.10 s; exit 0.10 -> (w+s)/v = 0.14 s")
for t, want in ((0.02, -0.4 * 0.02), (0.04, -0.016), (0.07, -0.016), (0.12, -0.056 + 0.4 * 0.12), (0.15, 0.0)):
    check(f"Psi({t}) [Wb]", Psi9(t), want)
for t, want in ((0.02, 0.4), (0.07, 0.0), (0.12, -0.4), (0.15, 0.0)):
    e = -fd(Psi9, t, 1e-6)
    m = mot9(t)
    check(f"emf(CCW) at t={t} flux route [V]", e, want, ab=1e-9)
    check(f"emf(CCW) at t={t} motional route [V]", m, want, ab=1e-9)
    I = e / R9
    F = force9(t, I)
    print(f"     t={t}: I(CCW) = {I:+.4f} A ({sense_word(e) if abs(e)>1e-9 else 'no current'}), magnetic force on loop = {np.round(F, 6)} N")
check("|I| entering [A]", 0.4 / R9, 4.0)
check("force needed while entering/leaving [N]", -force9(0.02, 4.0)[0], 0.32)
check("force needed while leaving [N]", -force9(0.12, -4.0)[0], 0.32)
ctr9 = (cn9(0.02)[0] + cn9(0.02)[2]) / 2
Bcc = bs_polygon(cn9(0.02), 1.0, ctr9)
print(f"   CCW current -> field at loop centre z-comp {Bcc[2]:+.2e} (+z): opposes the growing -z flux while entering")
emf_t = lambda t: -fd(Psi9, t, 1e-7)
pts9 = [0.04, 0.10, 0.14]
work = quad(lambda t: -force9(t, emf_t(t) / R9)[0] * v9, 0, 0.16, points=pts9, limit=200, epsabs=1e-10)[0]
heat = quad(lambda t: emf_t(t)**2 / R9, 0, 0.16, points=pts9, limit=200, epsabs=1e-10)[0]
check("work done by the applied force [J]", work, 0.128, rel=1e-5)
check("heat in R [J]", heat, 0.128, rel=1e-5)
# (e) narrow strip w = 0.1 m
Psi9e, mot9e, force9e, _ = strip_problem(B9, 0.1, s9, v9, R9)
print("   (e) w = 0.1 m: phases 0-0.02 s (leading edge in strip), 0.02-0.04 s (strip inside loop), 0.04-0.06 s (trailing edge in strip)")
for t, want in ((0.01, 0.4), (0.03, 0.0), (0.05, -0.4), (0.07, 0.0)):
    check(f"   narrow strip emf at t={t} flux route", -fd(Psi9e, t, 1e-6), want, ab=1e-9)
    check(f"   narrow strip emf at t={t} motional route", mot9e(t), want, ab=1e-9)
check("   narrow strip flux on the plateau [Wb]", Psi9e(0.03), -0.4 * 0.2 * 0.1)
emf_te = lambda t: -fd(Psi9e, t, 1e-7)
heat_e = quad(lambda t: emf_te(t)**2 / R9, 0, 0.08, points=[0.02, 0.04, 0.06], limit=200, epsabs=1e-10)[0]
check("   narrow strip total heat [J]", heat_e, 0.064, rel=1e-5)
print("   given: B = -0.4 z T for 0 < x < 0.5 m (0 outside), loop side 0.2 m, R = 0.1 Ohm, v = 5 x m/s, leading edge at x = 0 at t = 0")
print(f"   leading edge leaves at w/v = {w9/v9:.2f} s; trailing edge leaves at (w+s)/v = {(w9+s9)/v9:.2f} s with w+s = {w9+s9:.1f} m")
print(f"   v x B inside the strip = {np.cross(v9 * XH, np.array([0, 0, B9]))} V/m")
print(f"   I^2 R = {4.0**2*R9:.2f} W for {2*s9/v9:.2f} s -> {4.0**2*R9*2*s9/v9:.4f} J; work = 0.32 N x {2*s9:.1f} m = {0.32*2*s9:.4f} J")
print(f"   narrow strip: {4.0**2*R9:.2f} W x {2*0.02:.2f} s = {4.0**2*R9*0.04:.4f} J")

# ======================================================================================
print("=" * 90)
print("14.10 Voltmeters around a ramping solenoid")
print("=" * 90)
a10, dPsi_s = 0.2, -1.2            # solenoid radius [m]; dPsi_s/dt [Wb/s] (B along +z decreasing)
Bs0 = 2.0
Bs = lambda t: Bs0 + dPsi_s / (np.pi * a10**2) * t


def Eind(r, t):
    """induced E of the solenoid: E_phi = -(1/2 pi rho) dPsi_enc/dt"""
    rho = np.hypot(r[0], r[1])
    dPenc = dPsi_s * (min(rho, a10) / a10)**2
    Ephi = -dPenc / (2 * np.pi * rho)
    return Ephi * np.array([-r[1] / rho, r[0] / rho, 0.0])


def Psi_square(t):
    # numerical surface integral over the 2 m square; B nonzero only inside the solenoid
    f = lambda xx, yy: Bs(t)
    return dblquad(f, -a10, a10, lambda yy: -np.sqrt(max(a10**2 - yy**2, 0)), lambda yy: np.sqrt(max(a10**2 - yy**2, 0)), **TOL)[0]


P1, P2, P3, P4 = (np.array(p, float) for p in ((1, -1, 0), (1, 1, 0), (-1, 1, 0), (-1, -1, 0)))
emf10_flux = -fd(Psi_square, 0.3, 1e-4)
emf10_circ = poly_int(Eind, [P1, P2, P3, P4], 0.0)
check("emf(CCW) of the square = -dPsi/dt [V]", emf10_flux, 1.2)
check("emf(CCW) = loop integral of induced E around the square [V]", emf10_circ, 1.2, rel=1e-8)
R1, R2, R3 = 1.0, 2.0, 3.0
I10 = emf10_circ / (R1 + R2 + R3)
check("I (CCW) [A]", I10, 0.2, rel=1e-8)
print(f"   current {sense_word(emf10_circ)}: up through R1 (x=+1), left through R2 (top), down through R3 (x=-1), right along the bottom wire")
# Coulomb potential at the nodes (V_c(P1)=0): V(Q)-V(P) = int_P^Q E_ind.dl - (I R if a resistor is crossed along I)
Vc = {"P1": 0.0}
Vc["P2"] = Vc["P1"] + seg_int(Eind, P1, P2, 0) - I10 * R1
Vc["P3"] = Vc["P2"] + seg_int(Eind, P2, P3, 0) - I10 * R2
Vc["P4"] = Vc["P3"] + seg_int(Eind, P3, P4, 0) - I10 * R3
back = Vc["P4"] + seg_int(Eind, P4, P1, 0)
check("walking the circuit returns to V_c(P1) = 0", back, 0.0, ab=1e-10)
print("   Coulomb (charge) potentials of the nodes, V_c(P1) = 0:", {k: round(v, 6) for k, v in Vc.items()})


def reading(Xn, Yn, path):
    """ideal meter, + lead at node Xn, - lead at node Yn, leads+meter along the polyline path (X..Y)"""
    return Vc[Xn] - Vc[Yn] + poly_int(Eind, path, 0, closed=False)


m1 = reading("P1", "P2", [P1, np.array([1.1, -1, 0]), np.array([1.1, 1, 0]), P2])
m2 = reading("P1", "P2", [P1, np.array([1, -1.1, 0]), np.array([-1.1, -1.1, 0]), np.array([-1.1, 1.1, 0]), np.array([1, 1.1, 0]), P2])
m3 = reading("P4", "P1", [P4, np.array([-0.9, -0.9, 0]), np.array([-0.9, 0.5, 0]), np.array([0.9, 0.5, 0]), np.array([0.9, -0.9, 0]), P1])
m3b = reading("P4", "P1", [P4, np.array([-1, -1.1, 0]), np.array([1, -1.1, 0]), P1])
check("meter 1 (+P1, -P2, leads just right of R1) [V]", m1, 0.2, rel=1e-7)
check("meter 2 (+P1, -P2, leads round the left of the solenoid) [V]", m2, -1.0, rel=1e-7)
check("meter 3 (+P4, -P1, leads inside the square above the solenoid) [V]", m3, -1.2, rel=1e-7)
check("meter 3' (+P4, -P1, leads just below the bottom wire) [V]", m3b, 0.0, ab=1e-9)
check("meter1 - meter2 = emf linked by the two lead routes [V]", m1 - m2, 1.2, rel=1e-7)
check("drop I R1 [V]", I10 * R1, 0.2, rel=1e-7)
check("drop I R2 [V]", I10 * R2, 0.4, rel=1e-7)
check("drop I R3 [V]", I10 * R3, 0.6, rel=1e-7)
print(f"   readings: meter1 = {m1:+.4f} V, meter2 = {m2:+.4f} V, meter3 = {m3:+.4f} V, meter3' (below) = {m3b:+.2e} V")
# E outside the solenoid: curl-free locally, circulation 1.2 V around it
for rr in (0.5, 1.0):
    pt = np.array([rr, 0, 0])
    print(f"   E_ind at ({rr},0,0) = {Eind(pt, 0)} V/m  (E_phi = {-dPsi_s/(2*np.pi*rr):.4f} V/m, counter-clockwise)")
Bc10 = bs_polygon([P1, P2, P3, P4], 1.0, np.zeros(3))
print(f"   CCW loop current makes field {Bc10} at the centre (+z): props up the decreasing +z flux, Lenz OK")
print("   given: solenoid radius 0.2 m, dPsi_s/dt = -1.2 Wb/s; corners P1(1,-1) P2(1,1) P3(-1,1) P4(-1,-1) m; R1 = 1, R2 = 2, R3 = 3 Ohm; P4P1 plain wire")
print(f"   total resistance = {R1+R2+R3:.0f} Ohm; E_phi = 1.2/(2 pi r) V/m")
print("   lead routes: meter 1 along x = 1.1 m; meter 2 along y = -1.1, x = -1.1, y = 1.1 m;"
      " meter 3 inside the square along x = -0.9, y = 0.5, x = 0.9 m; meter 3' along y = -1.1 m")

# ======================================================================================
print("=" * 90)
print("14.11 Magnetic braking")
print("=" * 90)


def braking(m, R, B, l, v0, F=0.0, tend=20.0):
    k = B**2 * l**2 / R
    sol = solve_ivp(lambda t, y: [y[1], (F - k * y[1]) / m], [0, tend], [0.0, v0], dense_output=True, rtol=1e-11, atol=1e-13)
    return sol, k


sol, k = braking(0.1, 0.2, 0.4, 0.5, 3.0)
check("k = B^2 l^2 / R [kg/s]", k, 0.2)
check("tau = m R/(B^2 l^2) [s]", 0.1 / k, 0.5)
for t in (0.25, 0.5, 1.0):
    check(f"v({t}) solve_ivp vs 3 e^(-2t)", sol.sol(t)[1], 3 * np.exp(-2 * t), rel=1e-8)
check("distance travelled [m] (x at t=20 s)", sol.sol(20.0)[0], 1.5, rel=1e-8)
heat = quad(lambda t: (sol.sol(t)[1] * 0.4 * 0.5)**2 / 0.2, 0, 20, limit=200)[0]
check("heat = integral I^2 R dt [J]", heat, 0.45, rel=1e-7)
check("initial KE [J]", 0.5 * 0.1 * 9, 0.45)
# directions: rails along x at y=0 and y=l, resistor at x=0, B = 0.4 z, bar at x>0 moving +x
Bv = 0.4 * ZH
Psi11 = lambda t: dblquad(lambda y, x: Bv @ ZH, 0, 0.3 + 3.0 * t, 0, 0.5, **TOL)[0]     # CCW, at constant v=3 instant
emf11 = -fd(Psi11, 0.0, 1e-5)
mot11 = seg_int(lambda r, t: np.cross(3.0 * XH, Bv), np.array([0.3, 0, 0]), np.array([0.3, 0.5, 0]), 0.0)
check("emf(CCW) at v=3 m/s, flux route [V]", emf11, -0.6)
check("emf(CCW) at v=3 m/s, motional route [V]", mot11, -0.6)
I11 = abs(emf11) / 0.2
F11 = np.cross(I11 * (-0.5 * YH), Bv)
check("I at t=0 [A]", I11, 3.0)
print(f"   current {sense_word(emf11)} -> down the bar (-y); force on bar = {F11} N (against +x velocity)")
check("|F| at t=0 [N]", np.linalg.norm(F11), 0.6)
# second parameter set
sol2, k2 = braking(0.2, 0.5, 0.3, 0.4, 2.0, tend=200)
check("2nd set (m=.2,R=.5,B=.3,l=.4,v0=2): distance vs v0 m R/(B^2 l^2)", sol2.sol(200)[0], 2.0 * 0.2 * 0.5 / (0.09 * 0.16), rel=1e-7)
# (d) constant pull F = 0.6 N from rest
sol3, _ = braking(0.1, 0.2, 0.4, 0.5, 0.0, F=0.6)
check("(d) terminal speed [m/s] = F R/(B l)^2", sol3.sol(20)[1], 3.0, rel=1e-8)
for t in (0.5, 1.0):
    check(f"(d) v({t}) vs 3(1-e^(-2t))", sol3.sol(t)[1], 3 * (1 - np.exp(-2 * t)), rel=1e-8)
check("(d) v(0.5) value [m/s]", 3 * (1 - np.exp(-1)), 1.896361676, rel=1e-8)
check("(d) power at terminal speed F v [W]", 0.6 * 3, 1.8)
check("(d) I^2 R at terminal speed [W]", (3 * 0.4 * 0.5 / 0.2)**2 * 0.2, 1.8)
print("   given: m = 0.1 kg, R = 0.2 Ohm, B = 0.4 z T, rails y = 0 and y = l = 0.5 m, v0 = 3 x m/s; (d) F = 0.6 N from rest")
print(f"   B^2 = {0.4**2:.2f} T^2, l^2 = {0.5**2:.2f} m^2; 1/tau = {1/0.5:.0f} 1/s; terminal current v B l / R = {3*0.4*0.5/0.2:.1f} A")

# ======================================================================================
print("=" * 90)
print("14.12 Shrinking ring in a ramping solenoid")
print("=" * 90)


def sol_fields(a, B_of_t):
    def Bf(r, t):
        return np.array([0, 0, B_of_t(t)]) if np.hypot(r[0], r[1]) < a else np.zeros(3)

    def Psi_circle(rr, t):
        lim = min(rr, a)
        return dblquad(lambda rho, ph: B_of_t(t) * rho, 0, 2 * np.pi, 0, lim, **TOL)[0]
    return Bf, Psi_circle


a12 = 0.1
B12 = lambda t: 0.1 + 2.0 * t
Bf12, Psi_c12 = sol_fields(a12, B12)
Bdot = 2.0


def Ephi_formula(rr, a, Bd):
    return -rr / 2 * Bd if rr < a else -a**2 * Bd / (2 * rr)


for rr in (0.03, 0.07, 0.1 - 1e-9, 0.15, 0.2, 0.3):
    Ephi_num = -fd(lambda t: Psi_c12(rr, t), 0.05, 1e-4) / (2 * np.pi * rr)    # Faraday on the circle
    check(f"E_phi(r={rr:.3f}) from -dPsi/dt/(2 pi r) vs formula", Ephi_num, Ephi_formula(rr, a12, Bdot))
print(f"   E_phi inside = -r (V/m, r in m), outside = -0.01/r: at r=a {Ephi_formula(0.0999999, a12, 2):.4f}, at r=2a {Ephi_formula(0.2, a12, 2):.4f} V/m"
      " -> negative = clockwise seen from +z")


def Evec12(r, t, a=a12, Bd=Bdot):
    rho = np.hypot(r[0], r[1])
    return Ephi_formula(rho, a, Bd) * np.array([-r[1] / rho, r[0] / rho, 0])


h = 1e-6
for p in (np.array([0.04, 0.03, 0]), np.array([0.25, -0.1, 0])):
    curlz = ((Evec12(p + h * XH, 0)[1] - Evec12(p - h * XH, 0)[1]) - (Evec12(p + h * YH, 0)[0] - Evec12(p - h * YH, 0)[0])) / (2 * h)
    print(f"   (curl E)_z at {p[:2]} (rho = {np.hypot(*p[:2]):.3f}) = {curlz:+.6f}  (expect {-Bdot if np.hypot(*p[:2]) < a12 else 0.0})")
# second parameter set for E_phi: a = 0.05, dB/dt = -3
Bf12b, Psi_c12b = sol_fields(0.05, lambda t: 1.0 - 3.0 * t)
for rr in (0.02, 0.09):
    check(f"2nd set (a=0.05, dB/dt=-3) E_phi(r={rr})", -fd(lambda t: Psi_c12b(rr, t), 0.1, 1e-4) / (2 * np.pi * rr), Ephi_formula(rr, 0.05, -3.0))
# the ring
r12 = lambda t: 0.08 - 0.5 * t
rdot12 = -0.5
Psi_ring12 = lambda t: Psi_c12(r12(t), t)
emf_closed = lambda t: 3 * np.pi * (0.08 - 0.5 * t) * (t - 0.02)
for t in (0.0, 0.01, 0.02, 0.05, 0.1):
    ef = -fd(Psi_ring12, t, 1e-6) if t > 0 else -(Psi_ring12(1e-6) - Psi_ring12(-1e-6)) / 2e-6
    trans = circle_int(lambda r, tt: Evec12(r, tt), np.zeros(3), r12(t), t)
    motn = circle_int(lambda r, tt: np.cross(rdot12 * r / np.linalg.norm(r), Bf12(r, tt)), np.zeros(3), r12(t), t)
    check(f"t={t}: flux numeric vs pi r^2 B", Psi_ring12(t), np.pi * r12(t)**2 * B12(t))
    check(f"t={t}: -dPsi/dt vs 3pi(0.08-0.5t)(t-0.02)", ef, emf_closed(t), ab=1e-10)
    check(f"t={t}: transformer part (loop int of E) vs -pi r^2 dB/dt", trans, -np.pi * r12(t)**2 * Bdot)
    check(f"t={t}: motional part (loop int of v x B) vs 2 pi r u B", motn, 2 * np.pi * r12(t) * 0.5 * B12(t))
    check(f"t={t}: transformer + motional = -dPsi/dt", trans + motn, ef, ab=1e-10)
    print(f"     t={t}: r={r12(t):.3f} m, B={B12(t):.3f} T, Psi={Psi_ring12(t):.5e} Wb, transformer={trans*1e3:+.3f} mV,"
          f" motional={motn*1e3:+.3f} mV, emf={ef*1e3:+.3f} mV -> {sense_word(ef) if abs(ef) > 1e-9 else 'zero'}")
t1 = brentq(lambda t: -fd(Psi_ring12, t, 1e-6), 0.005, 0.05)
check("time the emf (and current) reverses [s]", t1, 0.02, rel=1e-6)
check("flux at t1 is the maximum, pi r^2 B [Wb]", Psi_ring12(t1), np.pi * 0.07**2 * 0.14, rel=1e-6)
print(f"   Psi(t1) = {Psi_ring12(t1):.4e} Wb; Psi(0) = {Psi_ring12(0):.4e}; Psi(0.04) = {Psi_ring12(0.04):.4e} (both smaller)")
for t, sgn in ((0.0, -1), (0.05, +1)):
    Bc = bs_polygon(circle_pts(np.zeros(3), r12(t), sgn), 1.0, np.zeros(3))
    print(f"   t={t}: induced current {'clockwise' if sgn < 0 else 'counter-clockwise'} -> its field at centre z-comp {Bc[2]:+.2e}")
check("emf at t=0 [mV]", emf_closed(0) * 1e3, -15.07964, rel=1e-6)
check("emf at t=0.1 [mV]", emf_closed(0.1) * 1e3, 22.61947, rel=1e-6)
check("transformer part at t=0 [mV] = -12.8 pi", -np.pi * 0.08**2 * 2 * 1e3, -40.21239, rel=1e-6)
check("motional part at t=0 [mV] = 8 pi", 2 * np.pi * 0.08 * 0.5 * 0.1 * 1e3, 25.13274, rel=1e-6)
print("   given: a = 0.1 m, B = (0.1 + 2t) z T inside, 0 outside; ring r(t) = 0.08 - 0.5t m for 0 <= t <= 0.1 s")
print(f"   r(0)^2 = {0.08**2:.4f} m^2")
for t in (0.0, 0.05):
    check(f"bracket 2B dr/dt + r dB/dt at t={t} vs 0.06 - 3t", 2 * B12(t) * rdot12 + r12(t) * Bdot, 0.06 - 3 * t)
check("emf at t=0 [mV] = -4.8 pi", emf_closed(0) * 1e3, -4.8 * np.pi, rel=1e-9)
check("emf at t=0.1 [mV] = 7.2 pi", emf_closed(0.1) * 1e3, 7.2 * np.pi, rel=1e-9)

print("=" * 90)
print("FAILED CHECKS:", FAILS if FAILS else "none")
