#!/usr/bin/env python3
"""Independent check of practice page 14 (Faraday's law and induced emf).

Every emf is computed (i) from the flux Psi(t) through the oriented loop (dS from the
loop's sense by the right-hand rule), with E = -dPsi/dt by central finite difference,
and (ii) where it applies, from the line integrals oint E.dl (induced E from -dA/dt)
and oint (v x B).dl with np.cross.  Voltmeter readings (14.10) are computed as the
line integral of E (induced + electrostatic) along each meter's actual lead path,
with the induced E built from a brute-force sum of current rings (elliptic integrals).
"""
import numpy as np
from scipy import integrate, optimize, special, interpolate

NP = NF = 0


def fmt(x):
    a = np.atleast_1d(np.asarray(x, float))
    return ", ".join(f"{v:.6g}" for v in a)


def check(label, got, page, rtol=3e-3, atol=1e-9):
    global NP, NF
    ok = bool(np.allclose(got, page, rtol=rtol, atol=atol))
    NP += ok
    NF += (not ok)
    print(f"{'PASS' if ok else 'FAIL'}  {label}: computed [{fmt(got)}]  page [{fmt(page)}]")


def checkb(label, cond):
    global NP, NF
    NP += bool(cond)
    NF += (not cond)
    print(f"{'PASS' if cond else 'FAIL'}  {label}")


GX, GW = np.polynomial.legendre.leggauss(48)


def seg_int(F, p, q, nsub=8):
    """int_p^q F(r).dl along the straight segment p->q (F: (n,3)->(n,3))."""
    p = np.asarray(p, float); q = np.asarray(q, float); d = q - p
    tot = 0.0
    for k in range(nsub):
        s0, s1 = k / nsub, (k + 1) / nsub
        s = s0 + (s1 - s0) * 0.5 * (GX + 1)
        pts = p + s[:, None] * d
        tot += 0.5 * (s1 - s0) * np.sum(GW * (F(pts) @ d))
    return tot


def path_int(F, pts, closed=False, nsub=8):
    P = [np.asarray(x, float) for x in pts]
    if closed:
        P = P + [P[0]]
    return sum(seg_int(F, P[i], P[i + 1], nsub) for i in range(len(P) - 1))


def seg_force(I, Bf, p, q, nsub=8):
    """I * int dl x B along p->q."""
    p = np.asarray(p, float); q = np.asarray(q, float); d = q - p
    tot = np.zeros(3)
    for k in range(nsub):
        s0, s1 = k / nsub, (k + 1) / nsub
        s = s0 + (s1 - s0) * 0.5 * (GX + 1)
        pts = p + s[:, None] * d
        tot += 0.5 * (s1 - s0) * np.sum(GW[:, None] * np.cross(d, Bf(pts)), axis=0)
    return I * tot


def flux_patch(Bf, c0, c1, c2, c3, n=40):
    """flux of B through the bilinear patch c0->c1->c2->c3 (dS by the right-hand rule)."""
    gx, gw = np.polynomial.legendre.leggauss(n)
    u = 0.5 * (gx + 1); w = 0.5 * gw
    U, V = np.meshgrid(u, u, indexing="ij"); W = np.outer(w, w)
    c0, c1, c2, c3 = (np.asarray(c, float) for c in (c0, c1, c2, c3))
    e = lambda f: f[..., None]
    R = e((1 - U) * (1 - V)) * c0 + e(U * (1 - V)) * c1 + e(U * V) * c2 + e((1 - U) * V) * c3
    Ru = e(-(1 - V)) * c0 + e(1 - V) * c1 + e(V) * c2 + e(-V) * c3
    Rv = e(-(1 - U)) * c0 + e(-U) * c1 + e(U) * c2 + e(1 - U) * c3
    dS = np.cross(Ru, Rv)
    Bv = Bf(R.reshape(-1, 3)).reshape(R.shape)
    return np.sum(W * np.sum(Bv * dS, axis=-1))


def flux_tri(Bf, p0, p1, p2, n=40):
    """flux through triangle p0->p1->p2 (Duffy map), oriented by the right-hand rule."""
    gx, gw = np.polynomial.legendre.leggauss(n)
    u = 0.5 * (gx + 1); w = 0.5 * gw
    U, V = np.meshgrid(u, u, indexing="ij"); W = np.outer(w, w)
    p0, p1, p2 = (np.asarray(c, float) for c in (p0, p1, p2))
    R = p0 + U[..., None] * (p1 - p0) + (U * V)[..., None] * (p2 - p1)
    Ru = (p1 - p0) + V[..., None] * (p2 - p1)
    Rv = U[..., None] * (p2 - p1)
    dS = np.cross(Ru, Rv)
    Bv = Bf(R.reshape(-1, 3)).reshape(R.shape)
    return np.sum(W * np.sum(Bv * dS, axis=-1))


def ddt(f, t, h=1e-6):
    return (f(t + h) - f(t - h)) / (2 * h)


def uniformB(vec):
    vec = np.asarray(vec, float)
    return lambda P: np.tile(vec, (len(P), 1))


def ring(center, radius, N=4000, normal_z=True):
    ph = np.linspace(0, 2 * np.pi, N, endpoint=False)
    return [np.array([center[0] + radius * np.cos(p), center[1] + radius * np.sin(p), 0.0]) for p in ph]


zhat = np.array([0, 0, 1.0]); xhat = np.array([1.0, 0, 0]); yhat = np.array([0, 1.0, 0])

# =====================================================================================
print("=== 14.1 Flux through a tilted loop ===")
C1 = [np.array(c) for c in [(0, 0, 0), (0.2, 0, 0), (0.2, 0.1, 0.1 * np.sqrt(3)), (0, 0.1, 0.1 * np.sqrt(3))]]
a = C1[1] - C1[0]; b = C1[2] - C1[1]
axb = np.cross(a, b)
check("14.1 |a|, |b|", [np.linalg.norm(a), np.linalg.norm(b)], [0.2, 0.2])
check("14.1 a.b (perpendicular)", a @ b, 0.0, atol=1e-12)
check("14.1 a x b [m^2]", axb, [0, -0.02 * np.sqrt(3), 0.02], atol=1e-12)
check("14.1 |a x b|", np.linalg.norm(axb), 0.04)
nhat = axb / np.linalg.norm(axb)
check("14.1 n-hat", nhat, [0, -np.sqrt(3) / 2, 0.5], atol=1e-12)
check("14.1 tilt angle [deg]", np.degrees(np.arccos(nhat @ zhat)), 60.0)
B1 = lambda t: uniformB((0, 0, 0.8 - 2 * t))
Psi1 = lambda t: flux_patch(B1(t), *C1)
check("14.1 Psi(0), Psi(0.1) [Wb] (page 0.016-0.04t)", [Psi1(0), Psi1(0.1)], [0.016, 0.012])
apex = np.mean(C1, axis=0) + np.array([0.05, -0.03, 0.2])
tent = sum(flux_tri(B1(0.1), C1[i], C1[(i + 1) % 4], apex) for i in range(4))
check("14.1 tent-surface flux at t=0.1 s [Wb]", tent, 0.012)
emf1 = -ddt(Psi1, 0.05)
# induced E for uniform dB/dt: E = -1/2 (dB/dt) x r  (curl E = -dB/dt)
E1 = lambda P: -0.5 * np.cross(np.array([0, 0, -2.0]), P)
check("14.1 emf: -dPsi/dt and oint E.dl along C [V]", [emf1, path_int(E1, C1, closed=True)], [0.04, 0.04])
check("14.1 I [A]", emf1 / 0.5, 0.08)
checkb("14.1 current flows along C (emf > 0)", emf1 > 0)

# =====================================================================================
print("\n=== 14.2 Current from a ramping field ===")
C2 = [np.array(c) for c in [(0, 0, 0), (0.2, 0, 0), (0.2, 0.3, 0), (0, 0.3, 0)]]  # ccw from +z
B2 = lambda t: uniformB((0, 0, 0.7 - 5 * t))
Psi2 = lambda t: flux_patch(B2(t), *C2)
check("14.2 A [m^2], Psi(0) [Wb]", [np.linalg.norm(np.cross(C2[1] - C2[0], C2[3] - C2[0])), Psi2(0)], [0.06, 0.042])
E2 = lambda P: -0.5 * np.cross(np.array([0, 0, -5.0]), P)
emf2a, emf2b = -ddt(Psi2, 0.05), -ddt(Psi2, 0.3)
check("14.2 emf ccw before/after B reverses, and oint E.dl [V]", [emf2a, emf2b, path_int(E2, C2, True)], [0.3, 0.3, 0.3])
check("14.2 I [A]", emf2a / 3, 0.1)
checkb("14.2 current counter-clockwise seen from +z (emf>0 for ccw C) -> key (b)", emf2a > 0 and emf2b > 0)
check("14.2 time at which B_z = 0 [s]", optimize.brentq(lambda t: 0.7 - 5 * t, 0, 1), 0.14)
check("14.2 distractor (d): 0.6 m^2 -> I [A]; 0.006 m^2 -> I [A]", [5 * 0.6 / 3, 5 * 0.006 / 3], [1.0, 0.01])
h = 1e-4
curlz = ((E2(np.array([[h, 0, 0]]))[0, 1] - E2(np.array([[-h, 0, 0]]))[0, 1]) / (2 * h)
         - (E2(np.array([[0, h, 0]]))[0, 0] - E2(np.array([[0, -h, 0]]))[0, 0]) / (2 * h))
check("14.2 (curl E)_z = -dBz/dt [T/s]", curlz, 5.0)
# start from -0.7 T instead
Psi2m = lambda t: flux_patch(uniformB((0, 0, -0.7 - 5 * t)), *C2)
check("14.2 start at -0.7 T: Psi(0), emf", [Psi2m(0), -ddt(Psi2m, 0.05)], [-0.042, 0.3])

# =====================================================================================
print("\n=== 14.3 Magnet pulled up through a ring (point dipole, k = mu0/4pi = 1) ===")
bring = 0.05
RING = ring((0, 0), bring, 3000)


def dipA(m, rm):
    return lambda P: np.cross(m, P - rm) / np.linalg.norm(P - rm, axis=1)[:, None] ** 3


def dipB(m, rm):
    def f(P):
        R = P - rm; Rn = np.linalg.norm(R, axis=1)[:, None]; Rh = R / Rn
        return (3 * (Rh @ m)[:, None] * Rh - m) / Rn ** 3
    return f


def ring_flux(m, zm):
    return path_int(dipA(m, np.array([0, 0, zm])), RING, closed=True, nsub=1)


def ring_force_z(m, zm, I):
    Bf = dipB(m, np.array([0, 0, zm]))
    P = RING + [RING[0]]
    return sum(seg_force(I, Bf, P[i], P[i + 1], nsub=1) for i in range(len(P) - 1))[2]


m_up = np.array([0, 0, 1.0])
zm_up = lambda t: -0.3 + 1.0 * t          # pulled up at 1 m/s, passes z=0 at t=0.3
Psi3 = lambda t: ring_flux(m_up, zm_up(t))
tt = np.array([0.15, 0.28, 0.32, 0.45])
psis = [Psi3(t) for t in tt]
emfs = [-ddt(Psi3, t, 1e-5) for t in tt]
print("   t =", tt, " Psi =", fmt(psis), " emf(ccw) =", fmt(emfs))
checkb("14.3 flux along +z throughout (Psi > 0)", all(p > 0 for p in psis))
checkb("14.3 approaching: emf < 0 -> clockwise from +z", emfs[0] < 0 and emfs[1] < 0)
checkb("14.3 receding: emf > 0 -> counter-clockwise from +z  => key (b)", emfs[2] > 0 and emfs[3] > 0)
tpk = optimize.minimize_scalar(lambda t: -Psi3(t), bounds=(0.2, 0.4), method="bounded").x
check("14.3 flux peaks when the magnet is in the ring's plane (z_m at peak)", zm_up(tpk), 0.0, atol=1e-4)
Fa = ring_force_z(m_up, zm_up(0.25), -ddt(Psi3, 0.25, 1e-5))
Fr = ring_force_z(m_up, zm_up(0.35), -ddt(Psi3, 0.35, 1e-5))
checkb(f"14.3 force on ring along +z in both phases (Fz = {Fa:.3g}, {Fr:.3g}); magnet held back", Fa > 0 and Fr > 0)
m_dn = np.array([0, 0, -1.0]); zm_dn = lambda t: 0.3 - 1.0 * t
Psi3o = lambda t: ring_flux(m_dn, zm_dn(t))
e_app, e_rec = -ddt(Psi3o, 0.2, 1e-5), -ddt(Psi3o, 0.4, 1e-5)
checkb("14.3 exam set-up (N down, falling): ccw approaching, cw after -> pattern (a)", e_app > 0 and e_rec < 0)

# =====================================================================================
print("\n=== 14.4 Lenz true/false ===")
r4 = lambda t: 0.1 - 0.02 * t
Psi4a = lambda t: integrate.quad(lambda rho: 0.5 * 2 * np.pi * rho, 0, r4(t))[0]
emf4a = -ddt(Psi4a, 0.0)
v4 = lambda P: -0.02 * P / np.linalg.norm(P, axis=1)[:, None]
vxB4 = lambda P: np.cross(v4(P), np.tile([0, 0, 0.5], (len(P), 1)))
mot4a = path_int(vxB4, ring((0, 0), 0.1), closed=True, nsub=1)
check("14.4(a) emf ccw at t=0, flux and motional routes [V]", [emf4a, mot4a], [6.28e-3, 6.28e-3])
P0 = np.array([[0.1, 0, 0]])
check("14.4(a) v x B . phi-hat at (0.1,0,0) [V/m]", vxB4(P0)[0] @ yhat, 0.01)
checkb("14.4(a) TRUE (ccw)", emf4a > 0)
sq = lambda t: [np.array(c) + np.array([2 * t, 0, 0]) for c in [(0, 0, 0), (0.3, 0, 0), (0.3, 0.3, 0), (0, 0.3, 0)]]
Psi4b = lambda t: flux_patch(uniformB((0, 0, 0.5)), *sq(t))
vxB4b = lambda P: np.cross(np.tile([2.0, 0, 0], (len(P), 1)), np.tile([0, 0, 0.5], (len(P), 1)))
S = sq(0)
sides = [seg_int(vxB4b, S[i], S[(i + 1) % 4]) for i in range(4)]
check("14.4(b) Psi at t=0 and t=1 [Wb]", [Psi4b(0), Psi4b(1)], [0.045, 0.045])
check("14.4(b) v x B [V/m]", vxB4b(P0)[0], [0, -1, 0])
check("14.4(b) side emfs (right, left) and total [V]", [sides[1], sides[3], sum(sides)], [-0.3, 0.3, 0.0], atol=1e-12)
checkb("14.4(b) FALSE (no emf)", abs(sum(sides)) < 1e-12 and abs(-ddt(Psi4b, 0.5)) < 1e-9)
Bz4c = lambda t: -0.5 * np.exp(-t / 2)
Psi4c = lambda t: integrate.quad(lambda rho: Bz4c(t) * 2 * np.pi * rho, 0, 0.1)[0]
emf4c = -ddt(Psi4c, 1.0)
dBdt4 = 0.25 * np.exp(-0.5)
E4c = lambda P: -0.5 * np.cross(np.array([0, 0, dBdt4]), P)
check("14.4(c) Psi(1 s) [Wb], emf(1 s) [V], oint E.dl [V]", [Psi4c(1.0), emf4c, path_int(E4c, ring((0, 0), 0.1), True, 1)],
      [-9.53e-3, -4.76e-3, -4.76e-3])
checkb("14.4(c) TRUE (emf<0 -> clockwise)", emf4c < 0)
gap = 1e-3 / 0.1
arc = [np.array([0.1 * np.cos(p), 0.1 * np.sin(p), 0]) for p in np.linspace(gap / 2, 2 * np.pi - gap / 2, 4000)]
check("14.4(d) emf around ring + gap chord at t=1 s [V]", path_int(E4c, arc, closed=True, nsub=1), -4.76e-3)
checkb("14.4(e) FALSE: in (a) and (c) induced field is parallel to the applied field",
       (emf4a > 0) == (0.5 > 0) and (emf4c > 0) == (Bz4c(1) > 0))

# =====================================================================================
print("\n=== 14.5 Sliding bar, find the error ===")
Psi5 = lambda t: integrate.dblquad(lambda y, x: 0.3, 0, 5 * t, 0, 0.4)[0]
emf5 = -ddt(Psi5, 0.4, 1e-4)
vxB5 = lambda P: np.cross(np.tile([5.0, 0, 0], (len(P), 1)), np.tile([0, 0, 0.3], (len(P), 1)))
mot5 = seg_int(vxB5, (2, 0, 0), (2, 0.4, 0))
check("14.5 Psi(t)=0.6t at t=0.4 [Wb]; emf ccw (flux) [V]; motional up the bar [V]", [Psi5(0.4), emf5, mot5], [0.24, -0.6, -0.6])
I5 = emf5 / 0.6
check("14.5 |I| [A] (student: 2 A)", abs(I5), 1.0)
checkb("14.5 current clockwise (down the bar, -y)", I5 < 0)
F5 = seg_force(1.0, lambda P: np.tile([0, 0, 0.3], (len(P), 1)), (2, 0.4, 0), (2, 0, 0))
check("14.5 force on bar [N]", F5, [-0.12, 0, 0], atol=1e-12)

# =====================================================================================
print("\n=== 14.6 Rotating rod ===")
L6, w6, B6, R6 = 0.5, 40.0, 0.2, 0.25
th = 0.7
Bv6 = lambda P: np.tile([0, 0, B6], (len(P), 1))
vxB6 = lambda P: np.cross(np.cross(np.tile([0, 0, w6], (len(P), 1)), P), Bv6(P))
tip = L6 * np.array([np.cos(th), np.sin(th), 0])
emf6 = seg_int(vxB6, (0, 0, 0), tip)
check("14.6 |v x B| at tip [V/m]; emf pivot->rim [V]", [np.linalg.norm(vxB6(tip[None])[0]), emf6], [4.0, 1.0])
checkb("14.6 v x B points outward (rim is + terminal)", vxB6(tip[None])[0] @ tip > 0)
A6 = lambda P: 0.5 * np.cross(Bv6(P), P)   # vector potential of the uniform field


def path6(t):
    th_t = w6 * t
    arc6 = [L6 * np.array([np.cos(p), np.sin(p), 0]) for p in np.linspace(th_t, 0, 6000)]
    return [np.zeros(3)] + arc6     # pivot -> rod tip -> arc back to phi=0 -> (lead) pivot


Psi6 = lambda t: path_int(A6, path6(t), closed=True, nsub=1)
t6 = 0.03
check("14.6 Psi at t=0.03 s (= -B L^2 wt/2) [Wb]", Psi6(t6), -B6 * 0.5 * L6 ** 2 * w6 * t6)
check("14.6 flux-rule emf along the path [V]", -ddt(Psi6, t6, 1e-5), 1.0)
I6 = emf6 / R6
check("14.6 I [A]", I6, 4.0)
s = np.linspace(0, L6, 2001)
rr = s[:, None] * np.array([1.0, 0, 0])[None, :]
dF = I6 * np.cross(np.tile([1.0, 0, 0], (len(s), 1)), Bv6(rr))
tau = integrate.trapezoid(np.cross(rr, dF)[:, 2], s)
check("14.6 magnetic torque on rod [N m]", tau, -0.1)
check("14.6 powers: tau*w, I^2 R, E I [W]", [-tau * w6, I6 ** 2 * R6, emf6 * I6], [4, 4, 4])

# =====================================================================================
print("\n=== 14.7 Generator coil ===")
N7, B7, R7 = 50, 0.25, 10.0
w7 = 1800 * 2 * np.pi / 60
check("14.7 omega [rad/s]", w7, 188.5)
c7 = [np.array(c) for c in [(-0.02, 0, 0.025), (0.02, 0, 0.025), (0.02, 0, -0.025), (-0.02, 0, -0.025)]]
n0 = np.cross(c7[1] - c7[0], c7[3] - c7[0])
check("14.7 area vector of C at t=0 (+y, A)", n0, [0, 0.002, 0], atol=1e-12)
Rz = lambda a: np.array([[np.cos(a), -np.sin(a), 0], [np.sin(a), np.cos(a), 0], [0, 0, 1]])
check("14.7 n-hat(t) = Rz(wt) y-hat at wt=0.4", Rz(0.4) @ yhat, [-np.sin(0.4), np.cos(0.4), 0])
coil = lambda t: [Rz(w7 * t) @ c for c in c7]
Bf7 = uniformB((B7, 0, 0))
Psi7 = lambda t: flux_patch(Bf7, *coil(t))
tq = np.array([0.001, 0.004])
check("14.7 Psi(t) = -5e-4 sin(wt)", [Psi7(t) for t in tq], -5e-4 * np.sin(w7 * tq))
emf7 = lambda t: -N7 * ddt(Psi7, t, 1e-7)
check("14.7 emf(0) = 1.5 pi, emf(1/180) = 0.75 pi [V]", [emf7(0), emf7(1 / 180)], [4.71, 2.36])
checkb("14.7 Lenz: Psi just after t=0 is negative", Psi7(1e-4) < 0)
vxB7 = lambda P: np.cross(np.cross(np.tile([0, 0, w7], (len(P), 1)), P), Bf7(P))
sides7 = [seg_int(vxB7, c7[i], c7[(i + 1) % 4]) for i in range(4)]
check("14.7 side speed [m/s] = 1.2 pi", w7 * 0.02, 3.77)
check("14.7 v x B on the x=+2 cm side [V/m]", vxB7(np.array([[0.02, 0, 0]]))[0], [0, 0, -0.3 * np.pi])
check("14.7 per-side emfs (top, +x side, bottom, -x side) [V]", sides7, [0, 0.015 * np.pi, 0, 0.015 * np.pi], atol=1e-12)
check("14.7 one turn, 50 turns [V]", [sum(sides7), N7 * sum(sides7)], [0.03 * np.pi, 1.5 * np.pi])
I07 = emf7(0) / R7
T7 = 2 * np.pi / w7
Pavg = integrate.quad(lambda t: emf7(t) ** 2 / R7, 0, T7, limit=200)[0] / T7
check("14.7 I0 [A], <P> [W]", [I07, Pavg], [0.471, 1.11])

# =====================================================================================
print("\n=== 14.8 Square loop in a graded field ===")
Bf8 = lambda P: 0.5 * np.stack([P[:, 2], np.zeros(len(P)), P[:, 0]], axis=1)
hh = 1e-4; p8 = np.array([[0.3, 0.2, 0.1]])
divB = sum((Bf8(p8 + hh * e[None])[0, i] - Bf8(p8 - hh * e[None])[0, i]) / (2 * hh) for i, e in enumerate(np.eye(3)))
J = np.array([[(Bf8(p8 + hh * e[None])[0, i] - Bf8(p8 - hh * e[None])[0, i]) / (2 * hh) for e in np.eye(3)] for i in range(3)])
curlB = np.array([J[2, 1] - J[1, 2], J[0, 2] - J[2, 0], J[1, 0] - J[0, 1]])
check("14.8 div B, |curl B|", [divB, np.linalg.norm(curlB)], [0, 0], atol=1e-9)
sq8 = lambda t: [np.array(c) + np.array([3 * t, 0, 0]) for c in [(0.1, 0, 0), (0.3, 0, 0), (0.3, 0.2, 0), (0.1, 0.2, 0)]]
Psi8 = lambda t: flux_patch(Bf8, *sq8(t))
check("14.8 Psi(0), Psi(0.2) [Wb] (0.004+0.06t)", [Psi8(0), Psi8(0.2)], [0.004, 0.016])
emf8 = -ddt(Psi8, 0.1)
check("14.8 emf ccw [V]", emf8, -0.06)
vxB8 = lambda P: np.cross(np.tile([3.0, 0, 0], (len(P), 1)), Bf8(P))
S8 = sq8(0)
e8 = [seg_int(vxB8, S8[i], S8[(i + 1) % 4]) for i in range(4)]
check("14.8 edge emfs bottom/right/top/left [V]", e8, [0, -0.09, 0, 0.03], atol=1e-12)
check("14.8 motional total [V]", sum(e8), -0.06)
I8 = emf8 / 0.05
check("14.8 |I| [A]", abs(I8), 1.2)
checkb("14.8 clockwise (emf<0 for ccw)", I8 < 0)
F8 = [seg_force(I8, Bf8, S8[i], S8[(i + 1) % 4]) for i in range(4)]   # I8<0 along ccw = clockwise current
check("14.8 F right, F left (x comps) [N]", [F8[1][0], F8[3][0]], [-0.036, 0.012])
check("14.8 F bottom, F top (y comps) [N]", [F8[0][1], F8[2][1]], [0.024, -0.024])
Fnet8 = sum(F8)
check("14.8 net magnetic force [N]", Fnet8, [-0.024, 0, 0], atol=1e-12)
check("14.8 power F v and I^2 R [W]", [-Fnet8[0] * 3, I8 ** 2 * 0.05], [0.072, 0.072])
rc = np.sqrt(0.04 / np.pi)
Psi8c = lambda t: integrate.dblquad(lambda rho, ph: 0.5 * (0.2 + 3 * t + rho * np.cos(ph)) * rho, 0, 2 * np.pi, 0, rc)[0]
circ8 = [np.array([0.2 + rc * np.cos(p), 0.1 + rc * np.sin(p), 0]) for p in np.linspace(0, 2 * np.pi, 4000, endpoint=False)]
check("14.8 circle of 0.04 m^2: flux and motional emf [V]", [-ddt(Psi8c, 0.0, 1e-4), path_int(vxB8, circ8, True, 1)], [-0.06, -0.06])

# =====================================================================================
print("\n=== 14.9 Loop crossing a field strip ===")


def run9(w):
    Bz = lambda x: np.where((x > 0) & (x < w), -0.4, 0.0)
    BfB = lambda P: np.stack([np.zeros(len(P)), np.zeros(len(P)), Bz(P[:, 0])], axis=1)
    lead = lambda t: 5 * t
    def Psi(t):
        lo, hi = lead(t) - 0.2, lead(t)
        pts = [p for p in (0.0, w) if lo < p < hi]
        return 0.2 * integrate.quad(lambda x: float(Bz(np.array([x]))[0]), lo, hi, points=pts or None, limit=200)[0]
    def loop(t):
        x1 = lead(t)
        return [np.array(c) for c in [(x1 - 0.2, 0, 0), (x1, 0, 0), (x1, 0.2, 0), (x1 - 0.2, 0.2, 0)]]
    vxB = lambda P: np.cross(np.tile([5.0, 0, 0], (len(P), 1)), BfB(P))
    emf = lambda t: -ddt(Psi, t, 1e-7)
    def force(t):
        Lp = loop(t); I = emf(t) / 0.1
        return sum(seg_force(I, BfB, Lp[i], Lp[(i + 1) % 4], nsub=20) for i in range(4))
    return Bz, Psi, loop, vxB, emf, force


Bz9, Psi9, loop9, vxB9, emf9, force9 = run9(0.5)
check("14.9 Psi at t=0.02, 0.07, 0.12, 0.15 s [Wb]", [Psi9(t) for t in (0.02, 0.07, 0.12, 0.15)], [-0.008, -0.016, -0.008, 0.0], atol=1e-9)
check("14.9 Psi = -0.4t at t=0.03 [Wb]", Psi9(0.03), -0.012)
check("14.9 emf (ccw) entering / inside / leaving / after [V]", [emf9(t) for t in (0.02, 0.07, 0.12, 0.16)], [0.4, 0, -0.4, 0], atol=1e-6)
check("14.9 |I| entering, leaving [A]", [abs(emf9(0.02)) / 0.1, abs(emf9(0.12)) / 0.1], [4, 4])
check("14.9 v x B in the slab [V/m]", vxB9(np.array([[0.3, 0, 0]]))[0], [0, 2, 0])
for tl, val in ((0.02, 0.4), (0.07, 0.0), (0.12, -0.4)):
    Lp = loop9(tl)
    check(f"14.9 oint (v x B).dl at t={tl} s [V]", sum(seg_int(vxB9, Lp[i], Lp[(i + 1) % 4], 50) for i in range(4)), val, atol=1e-9)
check("14.9 magnetic force entering / inside / leaving (x) [N]", [force9(t)[0] for t in (0.02, 0.07, 0.12)], [-0.32, 0, -0.32], atol=1e-6)
check("14.9 y-force cancels (entering) [N]", force9(0.02)[1], 0.0, atol=1e-6)
tm = (np.arange(1400) + 0.5) * (0.14 / 1400)
work = np.sum([-force9(t)[0] * 5 for t in tm]) * (0.14 / 1400)
heat = np.sum([emf9(t) ** 2 / 0.1 for t in tm]) * (0.14 / 1400)
check("14.9 work and heat [J]", [work, heat], [0.128, 0.128])
Bz9e, Psi9e, loop9e, vxB9e, emf9e, force9e = run9(0.1)
check("14.9(e) emf at t=0.01, 0.03, 0.05, 0.07 [V]", [emf9e(t) for t in (0.01, 0.03, 0.05, 0.07)], [0.4, 0, -0.4, 0], atol=1e-6)
check("14.9(e) Psi in the middle phase [Wb]", Psi9e(0.03), -0.008)
tm = (np.arange(600) + 0.5) * (0.06 / 600)
work_e = np.sum([-force9e(t)[0] * 5 for t in tm]) * (0.06 / 600)
heat_e = np.sum([emf9e(t) ** 2 / 0.1 for t in tm]) * (0.06 / 600)
check("14.9(e) work and heat [J]", [work_e, heat_e], [0.064, 0.064])

# =====================================================================================
print("\n=== 14.10 Voltmeters around a ramping solenoid (NEW numbers) ===")
MU0 = 4e-7 * np.pi
a10 = 0.2
dPsi_s = -2.0                    # Wb/s (page)
R1, R2, R3 = 4.0, 6.0, 10.0      # ohm (page)


def A_ring(r, z, a):
    """A_phi of a circular loop (radius a, unit current) at (r, z): elliptic-integral formula."""
    m = 4 * a * r / ((a + r) ** 2 + z ** 2)
    return MU0 / (np.pi * np.sqrt(m)) * np.sqrt(a / r) * ((1 - m / 2) * special.ellipk(m) - special.ellipe(m))


# validate the ring formula against a direct line integral A = mu0/(4 pi) oint dl'/R
ph = np.linspace(0, 2 * np.pi, 20000, endpoint=False)
rp = np.stack([a10 * np.cos(ph), a10 * np.sin(ph), 0 * ph], 1)
dl = np.stack([-a10 * np.sin(ph), a10 * np.cos(ph), 0 * ph], 1) * (2 * np.pi / len(ph))
fp = np.array([0.7, 0.0, 0.3])
Adir = MU0 / (4 * np.pi) * np.sum(dl / np.linalg.norm(fp - rp, axis=1)[:, None], axis=0)
check("14.10 ring A_phi: elliptic formula vs direct sum", A_ring(0.7, 0.3, a10), Adir[1], rtol=1e-6)
nturn = 1000.0
Lh = 400.0


def A_sol(r):   # per unit current, solenoid of n turns/m from -Lh to Lh
    f = lambda z: nturn * A_ring(r, z, a10)
    return 2 * (integrate.quad(f, 0, 5, limit=200)[0] + integrate.quad(f, 5, Lh, limit=200)[0])


Psi_s_perI = MU0 * nturn * np.pi * a10 ** 2
rg = np.linspace(0.4, 2.3, 96)
Ag = np.array([A_sol(r) for r in rg])
check("14.10 ring sum: 2 pi r A_phi(r) / Psi_s at r=0.5, 1, 2 m", [2 * np.pi * r * A_sol(r) / Psi_s_perI for r in (0.5, 1.0, 2.0)], [1, 1, 1], rtol=1e-4)
Aspl = interpolate.CubicSpline(rg, Ag)
dIdt = dPsi_s / Psi_s_perI
Ephi = lambda r: -dIdt * Aspl(r)        # E = -dA/dt (outside the solenoid)


def Eind(P):
    r = np.hypot(P[:, 0], P[:, 1])
    phi_hat = np.stack([-P[:, 1] / r, P[:, 0] / r, 0 * r], 1)
    return Ephi(r)[:, None] * phi_hat


check("14.10 E_phi at r=0.5, 1 m [V/m] (page 0.637, 0.318)", [Ephi(0.5), Ephi(1.0)], [0.637, 0.318])
checkb("14.10 E_phi > 0: counter-clockwise from +z", Ephi(0.5) > 0)
P1, P2, P3, P4 = (np.array(c, float) for c in [(1.5, -1, 0), (1.5, 1, 0), (-1.5, 1, 0), (-1.5, -1, 0)])
sides10 = [(P1, P2, R1), (P2, P3, R2), (P3, P4, R3), (P4, P1, 0.0)]
eind_side = [seg_int(Eind, p, q, 40) for p, q, _ in sides10]
emf_circ = sum(eind_side)
check("14.10 circuit emf (ccw) = oint E_ind.dl [V]", emf_circ, 2.0)
Rtot = R1 + R2 + R3
I10 = emf_circ / Rtot
check("14.10 I [A] (ccw)", I10, 0.1)
checkb("14.10 I > 0: counter-clockwise", I10 > 0)
check("14.10 drops I R1, I R2, I R3 [V]", [I10 * R1, I10 * R2, I10 * R3], [0.4, 0.6, 1.0])
# electrostatic potential of the nodes: phi(end)-phi(start) = -int E_es.dl = -int (E_tot - E_ind).dl
phi = {"P1": 0.0}
names = ["P1", "P2", "P3", "P4", "P1"]
cur = 0.0
for k, (p, q, Rk) in enumerate(sides10):
    cur = cur - I10 * Rk + eind_side[k]
    phi[names[k + 1] + ("_end" if k == 3 else "")] = cur
check("14.10 electrostatic potential closes around the circuit", phi["P1_end"], 0.0, atol=1e-9)


def meter(path, n_plus, n_minus):
    """reading = int E.dl along the leads from + to -, E = E_ind + E_es."""
    return path_int(Eind, path, closed=False, nsub=40) + phi[n_plus] - phi[n_minus]


m1 = [P1, (1.6, -1, 0), (1.6, 1, 0), P2]
m2 = [P1, (1.5, -1.1, 0), (-1.6, -1.1, 0), (-1.6, 1.1, 0), (1.5, 1.1, 0), P2]
m3a = [P4, (-1.5, -1.1, 0), (1.5, -1.1, 0), P1]
m3b = [P4, (-1.4, -0.9, 0), (-1.4, 0.5, 0), (1.4, 0.5, 0), (1.4, -0.9, 0), P1]
V1, V2, V3a, V3b = meter(m1, "P1", "P2"), meter(m2, "P1", "P2"), meter(m3a, "P4", "P1"), meter(m3b, "P4", "P1")
check("14.10 brute force: V1, V2 [V]", [V1, V2], [0.4, -1.6])
check("14.10 V1 - V2 [V]", V1 - V2, 2.0)
check("14.10 brute force: V3 below the wire, V3 inside (y=0.5) [V]", [V3a, V3b], [0.0, -2.0], atol=1e-6)


def winding(pts):
    P = np.array([np.asarray(p, float) for p in pts] + [np.asarray(pts[0], float)])
    ang = np.arctan2(P[:, 1], P[:, 0])
    d = np.diff(ang); d = (d + np.pi) % (2 * np.pi) - np.pi
    # refine: subdivide segments for an accurate angle sum
    tot = 0.0
    for i in range(len(P) - 1):
        ss = np.linspace(0, 1, 2001)
        Q = P[i] + ss[:, None] * (P[i + 1] - P[i])
        aa = np.unwrap(np.arctan2(Q[:, 1], Q[:, 0]))
        tot += aa[-1] - aa[0]
    return tot / (2 * np.pi)


# KVL route (page's method): V + int_{back along circuit} E_tot.dl = w * (-dPsi_s/dt)
w1 = winding(m1 + [P1][:0])                  # meter-1 leads closed straight back along side P1P2
w2 = winding(m2)
w3a = winding(m3a); w3b = winding(m3b)
check("14.10 winding numbers of meter loops (1, 2, 3a, 3b)", [w1, w2, w3a, w3b], [0, -1, 0, -1], atol=1e-6)
emf_ccw = -dPsi_s
check("14.10 KVL route: V1 = w1*2 + I R1, V2 = w2*2 + I R1 [V]", [w1 * emf_ccw + I10 * R1, w2 * emf_ccw + I10 * R1], [0.4, -1.6], atol=1e-6)
check("14.10 second route for V2: 0 - I R3 - I R2 [V]", 0 - I10 * R3 - I10 * R2, -1.6)
check("14.10 KVL route: V3 = w3*2 + 0 [V]", [w3a * emf_ccw, w3b * emf_ccw], [0, -2.0], atol=1e-6)
# flux route for the circuit: Psi(t) = oint A.dl (A from the ring sum), emf = -dPsi/dt
I_of_t = lambda t: 5.0 + dIdt * t
Psi_c = lambda t: I_of_t(t) * path_int(lambda P: (Aspl(np.hypot(P[:, 0], P[:, 1])))[:, None] * np.stack([-P[:, 1], P[:, 0], 0 * P[:, 0]], 1) / np.hypot(P[:, 0], P[:, 1])[:, None], [P1, P2, P3, P4], True, 40)
check("14.10 circuit emf from -dPsi/dt (Psi = oint A.dl) [V]", -ddt(Psi_c, 0.0, 1e-3), 2.0)

# --- the OLD 14.10 data (square +-1 m, R = 1, 2, 3 ohm, dPsi_s/dt = -1.2 Wb/s), same brute-force route
sc = -1.2 / dPsi_s
EindOld = lambda P: sc * Eind(P)
Q1, Q2, Q3, Q4 = (np.array(c, float) for c in [(1, -1, 0), (1, 1, 0), (-1, 1, 0), (-1, -1, 0)])
sidesO = [(Q1, Q2, 1.0), (Q2, Q3, 2.0), (Q3, Q4, 3.0), (Q4, Q1, 0.0)]
eO = [seg_int(EindOld, p, q, 40) for p, q, _ in sidesO]
IO = sum(eO) / 6.0
phO = {"Q1": 0.0}; cur = 0.0
for k, (p, q, Rk) in enumerate(sidesO[:3]):
    cur = cur - IO * Rk + eO[k]; phO[["Q2", "Q3", "Q4"][k]] = cur
mO = lambda path, a_, b_: path_int(EindOld, path, False, 40) + phO[a_] - phO[b_]
oldV = [mO([Q1, (1.1, -1, 0), (1.1, 1, 0), Q2], "Q1", "Q2"),
        mO([Q1, (1, -1.1, 0), (-1.1, -1.1, 0), (-1.1, 1.1, 0), (1, 1.1, 0), Q2], "Q1", "Q2"),
        mO([Q4, (-1, -1.1, 0), (1, -1.1, 0), Q1], "Q4", "Q1"),
        mO([Q4, (-0.9, -0.9, 0), (-0.9, 0.5, 0), (0.9, 0.5, 0), (0.9, -0.9, 0), Q1], "Q4", "Q1")]
check("14.10 OLD key: I [A], E_phi(0.5), E_phi(1) [V/m]", [IO, sc * Ephi(0.5), sc * Ephi(1.0)], [0.2, 0.382, 0.191])
check("14.10 OLD key: V1, V2, V3 (wire), V3 (inside) [V]", oldV, [0.2, -1.0, 0.0, -1.2], atol=1e-6)
print("   resemblance table (circuit | R values | dPsi/dt through circuit):")
print("   SU17 HE2 #3 : 1 m^2 square, uniform B     | 1, 3, 2 ohm + wire | -12 Wb/s (dB/dt=-12 T/s)")
print("   SU18 HE2 #3 : 2 m x 2 m square, uniform B | meters 3 kohm      | -12 Wb/s (B=-3t z, 4 m^2)")
print("   page (old)  : 2 m x 2 m square, solenoid  | 1, 2, 3 ohm + wire | -1.2 Wb/s")
print("   page (new)  : 3 m x 2 m rectangle, solenoid | 4, 6, 10 ohm + wire | -2 Wb/s")
checkb("14.10 new R set and rate differ from both exams", {4.0, 6.0, 10.0}.isdisjoint({1.0, 2.0, 3.0}) and dPsi_s not in (-12.0, -1.2))

# =====================================================================================
print("\n=== 14.11 Magnetic braking ===")
m11, l11, R11, B11 = 0.1, 0.5, 0.2, 0.4
Bv11 = np.array([0, 0, B11])


def fmag(v):
    vxB = np.cross([v, 0, 0], Bv11)
    emf = vxB @ yhat * l11             # oint along ccw C: up the bar (+y)
    I = emf / R11                      # ccw current
    F = I * np.cross(l11 * yhat, Bv11) # current along +y in the bar if I>0
    return emf, I, F


emf0, I0, F0 = fmag(3.0)
check("14.11 emf (ccw) at v=3 [V], |I| [A], F [N]", [emf0, abs(I0), F0[0]], [-0.6, 3.0, -0.6])
checkb("14.11 clockwise current (down the bar)", I0 < 0)
sol = integrate.solve_ivp(lambda t, y: [fmag(y[0])[2][0] / m11, y[0], fmag(y[0])[1] ** 2 * R11], (0, 20), [3.0, 0, 0],
                          rtol=1e-11, atol=1e-13, dense_output=True)
check("14.11 k [kg/s], tau [s]", [B11 ** 2 * l11 ** 2 / R11, m11 * R11 / (B11 ** 2 * l11 ** 2)], [0.2, 0.5])
check("14.11 v(0.5), v(1) vs 3 e^{-2t} [m/s]", [sol.sol(0.5)[0], sol.sol(1.0)[0]], [3 * np.exp(-1), 3 * np.exp(-2)], rtol=1e-6)
check("14.11 distance [m], heat [J], KE0 [J]", [sol.y[1, -1], sol.y[2, -1], 0.5 * m11 * 9], [1.5, 0.45, 0.45])
sol2 = integrate.solve_ivp(lambda t, y: [(0.6 + fmag(y[0])[2][0]) / m11], (0, 20), [0.0], rtol=1e-11, atol=1e-13, dense_output=True)
check("14.11(d) v(0.5) [m/s], terminal [m/s]", [sol2.sol(0.5)[0], sol2.y[0, -1]], [1.90, 3.0])
check("14.11(d) v(0.3) vs 3(1-e^{-2t})", sol2.sol(0.3)[0], 3 * (1 - np.exp(-0.6)), rtol=1e-6)
vt = sol2.y[0, -1]
check("14.11(d) P_in, I, I^2 R at terminal speed", [0.6 * vt, abs(fmag(vt)[1]), fmag(vt)[1] ** 2 * R11], [1.8, 3.0, 1.8])

# =====================================================================================
print("\n=== 14.12 Shrinking ring in a ramping solenoid ===")
a12 = 0.1
Bz12 = lambda t: 0.1 + 2 * t
Psi_enc = lambda r, t: integrate.quad(lambda rho: Bz12(t) * 2 * np.pi * rho, 0, min(r, a12))[0]
Ephi12 = lambda r, t=0.0: -ddt(lambda tt: Psi_enc(r, tt), t) / (2 * np.pi * r)
check("14.12 E_phi at r=a, 2a [V/m]", [Ephi12(a12), Ephi12(2 * a12)], [-0.1, -0.05])
check("14.12 E_phi(r) = -r inside (r=0.05), -0.01/r outside (r=0.3)", [Ephi12(0.05), Ephi12(0.3)], [-0.05, -0.01 / 0.3])
hr = 1e-4
curl_in = (((0.05 + hr) * Ephi12(0.05 + hr)) - ((0.05 - hr) * Ephi12(0.05 - hr))) / (2 * hr) / 0.05
curl_out = (((0.15 + hr) * Ephi12(0.15 + hr)) - ((0.15 - hr) * Ephi12(0.15 - hr))) / (2 * hr) / 0.15
check("14.12 (curl E)_z inside, outside [T/s]", [curl_in, curl_out], [-2.0, 0.0], atol=1e-6)
r12 = lambda t: 0.08 - 0.5 * t
Psi12 = lambda t: Psi_enc(r12(t), t)
emf12 = lambda t: -ddt(Psi12, t, 1e-7)
ts = np.array([0.0, 0.01, 0.05, 0.1])
check("14.12 Psi(t) vs pi(0.08-0.5t)^2(0.1+2t)", [Psi12(t) for t in ts], np.pi * r12(ts) ** 2 * Bz12(ts))
check("14.12 emf(t) vs 3 pi (0.08-0.5t)(t-0.02)", [emf12(t) for t in ts], 3 * np.pi * r12(ts) * (ts - 0.02), atol=1e-9)


def parts(t):
    rc = r12(t)
    pts = [np.array([rc * np.cos(p), rc * np.sin(p), 0]) for p in np.linspace(0, 2 * np.pi, 3000, endpoint=False)]
    Ef = lambda P: (-0.5 * 2.0 * np.hypot(P[:, 0], P[:, 1]))[:, None] * np.stack([-P[:, 1], P[:, 0], 0 * P[:, 0]], 1) / np.hypot(P[:, 0], P[:, 1])[:, None]
    vxB = lambda P: np.cross(-0.5 * P / np.hypot(P[:, 0], P[:, 1])[:, None], np.tile([0, 0, Bz12(t)], (len(P), 1)))
    return path_int(Ef, pts, True, 1), path_int(vxB, pts, True, 1)


tr0, mo0 = parts(0.0)
check("14.12 t=0: transformer, motional, sum [mV]", [tr0 * 1e3, mo0 * 1e3, (tr0 + mo0) * 1e3], [-40.21, 25.13, -15.08])
check("14.12 t=0: in units of pi mV", [tr0 * 1e3 / np.pi, mo0 * 1e3 / np.pi], [-12.8, 8.0])
check("14.12 sum equals (b) at t=0", tr0 + mo0, emf12(0.0))
troot = optimize.brentq(emf12, 0.005, 0.05)
check("14.12 reversal time [s]", troot, 0.02)
tmax = optimize.minimize_scalar(lambda t: -Psi12(t), bounds=(0, 0.1), method="bounded")
check("14.12 time of max flux [s], max flux [Wb]", [tmax.x, Psi12(tmax.x)], [0.02, 2.16e-3], atol=1e-6)
tr2, mo2 = parts(0.02)
check("14.12 t=0.02: transformer, motional [mV]", [tr2 * 1e3, mo2 * 1e3], [-30.79, 30.79])
checkb("14.12 clockwise before (emf<0 at t=0.01), ccw after (emf>0 at 0.05)", emf12(0.01) < 0 and emf12(0.05) > 0)
tr10, mo10 = parts(0.1)
check("14.12 t=0.1: emf, transformer, motional [mV]", [emf12(0.1) * 1e3, tr10 * 1e3, mo10 * 1e3], [22.62, -5.65, 28.27])
check("14.12 emf(0.1) in units of pi mV", emf12(0.1) * 1e3 / np.pi, 7.2)

print(f"\nSUMMARY: {NP} PASS, {NF} FAIL")
