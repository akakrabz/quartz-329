#!/usr/bin/env python3
"""R12.py -- independent re-solution of practice page 12
(magnetic force, Biot-Savart, Ampere's law).

Rules followed:
* every Biot-Savart field is a DIRECT numerical sum of  mu0 I/(4 pi) dl x R_hat / R^2
  over the actual wire geometry (polyline, segment midpoints, R_hat from source to field point);
  infinite / semi-infinite lines use nodes s = h tan(theta) reaching |s| ~ 1e7 h;
* every force / direction comes from np.cross;
* Ampere problems are re-done by numerical I_enc (scipy quad) AND by a 2-D Biot-Savart
  sum over the conductor cross-section (each cell = infinite filament, whose field
  mu0 I/(2 pi rho) phi_hat is itself checked by direct summation in 12.1/12.2/12.9/12.10).
Page values (after the reviewer's edits) are transcribed and compared: PASS/FAIL.
"""
import numpy as np
from scipy import integrate, optimize

MU0 = 4e-7*np.pi
QE = 1.602176634e-19
xh, yh, zh = np.eye(3)
O3 = np.zeros(3)

NP = NF = 0


def chk(label, got, want, rtol=3e-3, atol=0.0):
    """PASS if every component agrees within rtol*max|want| + atol."""
    global NP, NF
    g = np.atleast_1d(np.asarray(got, float))
    w = np.atleast_1d(np.asarray(want, float))
    tol = rtol*max(np.max(np.abs(w)), 1e-300) + atol
    ok = g.shape == w.shape and bool(np.all(np.abs(g - w) <= tol))
    NP += ok
    NF += (not ok)

    def f(a):
        return (np.array2string(a, precision=5, separator=', ', suppress_small=False)
                if a.size > 1 else f"{a[0]:.6g}")
    print(f"  {'PASS' if ok else 'FAIL'}  {label}: computed {f(g)} | page {f(w)}")
    return ok


def bs(nodes, I, P):
    """Direct Biot-Savart sum: mu0 I/(4 pi) * sum_k dl_k x R_hat_k / R_k^2,
    dl_k = node_{k+1}-node_k (current flows in node order), R from segment midpoint to P."""
    nodes = np.asarray(nodes, float)
    dl = np.diff(nodes, axis=0)
    mid = 0.5*(nodes[1:] + nodes[:-1])
    P = np.atleast_2d(np.asarray(P, float))
    out = np.zeros_like(P)
    for k, p in enumerate(P):
        R = p - mid
        Rn = np.linalg.norm(R, axis=1)
        Rhat = R/Rn[:, None]
        out[k] = MU0*I/(4*np.pi)*np.sum(np.cross(dl, Rhat)/(Rn**2)[:, None], axis=0)
    return out if len(out) > 1 else out[0]


def line_nodes(p0, u, P, N=40001, eps=1e-7):
    """Infinite line p0 + s u (current along u); nodes s = s_foot + h tan(theta)."""
    u = np.asarray(u, float)/np.linalg.norm(u)
    p0 = np.asarray(p0, float)
    P = np.asarray(P, float)
    sf = np.dot(P - p0, u)
    h = np.linalg.norm(P - p0 - sf*u)
    th = np.linspace(-np.pi/2 + eps, np.pi/2 - eps, N)
    return p0 + (sf + h*np.tan(th))[:, None]*u


def B_line(p0, u, I, P):
    """Field of an infinite straight wire by direct summation (one adapted grid per field point)."""
    P = np.atleast_2d(np.asarray(P, float))
    out = np.array([bs(line_nodes(p0, u, p), I, p) for p in P])
    return out if len(out) > 1 else out[0]


def ray_nodes(end, u_out, scale, N=40001, eps=1e-7):
    """Semi-infinite line end + s u_out, s in [0, scale/eps], ordered outward from `end`."""
    th = np.linspace(0.0, np.pi/2 - eps, N)
    return np.asarray(end, float) + (scale*np.tan(th))[:, None]*np.asarray(u_out, float)


def seg_nodes(A, B, N=20001):
    t = np.linspace(0.0, 1.0, N)[:, None]
    return (1 - t)*np.asarray(A, float) + t*np.asarray(B, float)


def cells(Jxy, h, half, origin=(0.0, 0.0)):
    """Cell centres origin + (i h, j h) covering [-half, half]^2 with J != 0; returns x, y, I = J h^2."""
    ox, oy = origin
    ix = np.arange(np.floor((-half - ox)/h), np.ceil((half - ox)/h) + 1)
    iy = np.arange(np.floor((-half - oy)/h), np.ceil((half - oy)/h) + 1)
    X, Y = np.meshgrid(ox + ix*h, oy + iy*h, indexing='ij')
    J = Jxy(X, Y)
    m = J != 0
    return X[m], Y[m], J[m]*h*h


def H_cells(cx, cy, Ic, P):
    """2-D Biot-Savart over a cross-section of +z filaments: H = sum I zhat x rho /(2 pi rho^2).
    A cell centred exactly on P (aligned grid) is skipped: a uniform square cell has no field at its centre."""
    P = np.atleast_2d(np.asarray(P, float))
    out = np.zeros((len(P), 2))
    for k, (px, py) in enumerate(P):
        rx = px - cx
        ry = py - cy
        r2 = rx*rx + ry*ry
        ok = r2 > 0
        out[k] = [np.sum(-Ic[ok]*ry[ok]/r2[ok]), np.sum(Ic[ok]*rx[ok]/r2[ok])]
    out /= 2*np.pi
    return out if len(out) > 1 else out[0]


def H_aligned(Jxy, h, half, P, Itot=None):
    """2-D sum with the grid aligned so P is a cell centre; optional renormalisation of the
    discretised total current to Itot (removes the staircase error of the circular boundary)."""
    cx, cy, Ic = cells(Jxy, h, half, origin=P)
    if Itot is not None:
        Ic = Ic*Itot/Ic.sum()
    return H_cells(cx, cy, Ic, P)


# ---------------------------------------------------------------- 12.1
print("12.1  charge passing a wire (wire on y axis, 2 A along -y; Q at (0,1,-3) m, v = 5 z m/s)")
P = np.array([0.0, 1.0, -3.0])
B = B_line(O3, -yh, 2.0, P)
chk("B at the charge [T]", B, [1.33e-7, 0, 0])
v = 5*zh
F = np.cross(v, B)                       # per coulomb of Q
chk("F/Q = v x B [N/C]", F, [0, 6.67e-7, 0])
print("   unit F =", np.round(F/np.linalg.norm(F), 6), "-> option (c) +y")
Bwrong = B_line(O3, +yh, 2.0, P)
print("   (a) B dir:", np.round(B/np.linalg.norm(B), 6), " (b) B with current +y:",
      np.round(Bwrong/np.linalg.norm(Bwrong), 6),
      " (d) B x v dir:", np.round(np.cross(B, v)/np.linalg.norm(np.cross(B, v)), 6))
print(f"   F.v = {np.dot(F, v):.2e}, F.B = {np.dot(F, B):.2e}; v along x gives |F| = "
      f"{np.linalg.norm(np.cross(xh, B)):.2e}")

# ---------------------------------------------------------------- 12.2
print("\n12.2  antiparallel wires (10 A +x on x axis; 6 A -x on y = 4 cm)")
I1, I2, d = 10.0, 6.0, 0.04
B1 = B_line(O3, xh, I1, [0, d, 0])
chk("(a) B1 at wire 2 [T]", B1, [0, 0, 5e-5])
F2 = I2*np.cross(-xh, B1)
chk("(b) F2 per metre [N/m] (+y: repel)", F2, [0, 3e-4, 0])
chk("(b) mu0 I1 I2/(2 pi d) [N/m]", MU0*I1*I2/(2*np.pi*d), 3e-4)
mid = [0, d/2, 0]
B1m = B_line(O3, xh, I1, mid)
B2m = B_line([0, d, 0], -xh, I2, mid)
chk("(c) wire 1 at midpoint [T]", B1m, [0, 0, 1e-4])
chk("(c) wire 2 at midpoint [T]", B2m, [0, 0, 6e-5])
chk("(c) total at midpoint [T]", B1m + B2m, [0, 0, 1.6e-4])
B2 = B_line([0, d, 0], -xh, I2, O3)
chk("check: B2 at wire 1 [T]", B2, [0, 0, 3e-5])
chk("check: F1 per metre [N/m]", I1*np.cross(xh, B2), [0, -3e-4, 0])

# ---------------------------------------------------------------- 12.3
print("\n12.3  electron in B = 5e-5 z T, v0 = 2e5 x m/s (e = 1.602e-19 C, m = 9.109e-31 kg)")
e3, me = 1.602e-19, 9.109e-31
Bv = 5e-5*zh
q = -e3
F0 = q*np.cross(2e5*xh, Bv)
chk("(a) F(0) [N]", F0, [0, 1.60e-18, 0])


def rhs(t, s):
    return np.concatenate([s[3:], q/me*np.cross(s[3:], Bv)])


sol = integrate.solve_ivp(rhs, [0, 2e-6], [0, 0, 0, 2e5, 0, 0], method='DOP853', rtol=1e-11,
                          atol=np.r_[[1e-13]*3, [1e-6]*3], dense_output=True)
ts = np.linspace(1e-12, 2e-6, 400001)
xs = sol.sol(ts)[0]
up = np.where((xs[:-1] < 0) & (xs[1:] >= 0))[0]
T = optimize.brentq(lambda t: sol.sol(t)[0], ts[up[0]], ts[up[0] + 1], xtol=1e-18)
tt = np.linspace(0, T, 20001)[:-1]
S = sol.sol(tt)
c = S[:3].mean(axis=1)
R = np.mean(np.linalg.norm(S[:3].T - c, axis=1))
Lz = np.mean(np.cross(S[:3].T - c, S[3:].T)[:, 2])
chk("(b) R [m] (ODE)", R, 0.0227)
chk("(b) T [s] (ODE)", T, 0.714e-6)
chk("(b) f [Hz]", 1/T, 1.40e6)
chk("(c) centre [m]", c, [0, 0.0227, 0])
print(f"   (c) Lz about centre = {Lz:+.3e} -> {'counter-clockwise' if Lz > 0 else 'clockwise'} seen from +z")
print("   check: proton force direction", np.round(np.cross(2e5*xh, Bv)/np.linalg.norm(np.cross(2e5*xh, Bv)), 6))

# ---------------------------------------------------------------- 12.4
print("\n12.4  which field is magnetic (B0 = 1 T, a = 1 m, finite differences)")
B0 = a = 1.0
fields = {'a': lambda r: B0/a*np.array([r[0], r[1], 0.0]),
          'b': lambda r: B0/a*np.array([r[0], -r[1], r[2]]),
          'c': lambda r: B0/a*np.array([r[1], -r[0], 0.0]),
          'd': lambda r: B0*r/np.linalg.norm(r)}


def div(f, r, h=1e-5):
    return sum((f(r + h*e)[i] - f(r - h*e)[i])/(2*h) for i, e in enumerate(np.eye(3)))


def curl(f, r, h=1e-5):
    G = np.array([(f(r + h*e) - f(r - h*e))/(2*h) for e in np.eye(3)])  # G[j,i] = d f_i/d x_j
    return np.array([G[1, 2] - G[2, 1], G[2, 0] - G[0, 2], G[0, 1] - G[1, 0]])


r0 = np.array([0.3, -0.7, 0.4])
chk("(a) div B", div(fields['a'], r0), 2*B0/a)
chk("(b) div B", div(fields['b'], r0), B0/a)
chk("(c) div B", div(fields['c'], r0), 0.0, atol=1e-8)
chk("(d) div B", div(fields['d'], r0), 2*B0/np.linalg.norm(r0))
chk("(c) J = curl B/mu0 [A/m^2]", curl(fields['c'], r0)/MU0, [0, 0, -2*B0/(MU0*a)])
print("   (c) B on +x axis:", fields['c'](np.array([1.0, 0, 0])), " on +y axis:", fields['c'](np.array([0, 1.0, 0])),
      "-> clockwise seen from +z")
rr = np.hypot(r0[0], r0[1])
chk("(c) |B| = mu0|Jz| r/2", np.linalg.norm(fields['c'](r0)), MU0*(2*B0/(MU0*a))*rr/2)

# ---------------------------------------------------------------- 12.5
print("\n12.5  delta-function currents (deltas -> Gaussians, sigma = 1 mm)")
sg = 1e-3


def g(u):
    return np.exp(-u**2/(2*sg**2))/(np.sqrt(2*np.pi)*sg)


def qd(f, lo, hi, pts=()):
    p = [x for x in pts if lo < x < hi]
    return integrate.quad(f, lo, hi, points=p or None, limit=400)[0]


def strip_y(y):
    return 6*y*(1 - y)*(abs(y - 0.5) < 0.5)


def I_region(x0, x1, y0, y1):
    line = 4*qd(lambda x: g(x - 1), x0, x1, [1])*qd(lambda y: g(y - 1), y0, y1, [1])
    strip = -qd(lambda x: g(x - 2), x0, x1, [2])*qd(strip_y, y0, y1, [0, 1])
    return line, strip


ln, st = I_region(0, 3, 0, 3)
chk("(b) line part [A]", ln, 4.0)
chk("(b) strip part [A]", st, -1.0)
chk("(b) net I [A]", ln + st, 3.0)
ln, st = I_region(1.5, 3, 0, 3)
chk("(c) net I [A]", ln + st, -1.0)
res = optimize.minimize_scalar(lambda y: -strip_y(y), bounds=(0, 1), method='bounded')
chk("(a) strip peak |Js| [A/m] at y = %.4f m" % res.x, -res.fun, 1.5)

# ---------------------------------------------------------------- 12.6
print("\n12.6  square loop a = 10 cm, I = 5 A, CCW seen from +z")
a, I = 0.10, 5.0
h = a/2
cor = [(-h, -h, 0), (h, -h, 0), (h, h, 0), (-h, h, 0), (-h, -h, 0)]
sides = [seg_nodes(cor[k], cor[k + 1]) for k in range(4)]


def B_sq(P):
    return sum(bs(s, I, P) for s in sides)


Bc = B_sq(O3)
chk("(b) bottom side alone [T]", bs(sides[0], I, O3), [0, 0, 1.41e-5])
chk("(b) B at centre [T]", Bc, [0, 0, 5.66e-5])
chk("(b) H at centre [A/m]", Bc/MU0, [0, 0, 45.0])
ph = np.linspace(0, 2*np.pi, 721)[:-1]
Pc = np.c_[a/4*np.cos(ph), a/4*np.sin(ph), 0*ph]
Hc = B_sq(Pc)/MU0
print(f"   (a) circle r = a/4: max|H_x|,|H_y| = {np.abs(Hc[:, :2]).max():.1e} A/m; "
      f"circulation = {np.sum(Hc[:, 0]*(-np.sin(ph)) + Hc[:, 1]*np.cos(ph))*(a/4)*(2*np.pi/720):.1e} A")
chk("(a) min H_z on circle [A/m]", Hc[:, 2].min(), 53.0, rtol=1e-3)
chk("(a) max H_z on circle [A/m]", Hc[:, 2].max(), 54.7, rtol=1e-3)
t = np.linspace(0, 2*np.pi, 40001)
Bcirc = bs(np.c_[h*np.cos(t), h*np.sin(t), 0*t], I, O3)
chk("(c) circular loop R = a/2 [T]", Bcirc, [0, 0, 6.28e-5])
chk("(c) square/circle", Bc[2]/Bcirc[2], 0.900)
chk("check: finite-segment formula per side [T]", MU0*I/(4*np.pi*h)*(2*np.sin(np.pi/4)), 1.41e-5)

# ---------------------------------------------------------------- 12.7
print("\n12.7  nonuniform wire J = J0 r/a, a = 1 mm, J0 = 3e6 A/m^2")
a, J0 = 1e-3, 3e6
Itot = integrate.quad(lambda r: J0*r/a*2*np.pi*r, 0, a)[0]
chk("(a) I [A]", Itot, 6.28)


def H7(r):
    return integrate.quad(lambda s: J0*s/a*2*np.pi*s, 0, min(r, a))[0]/(2*np.pi*r)


chk("(c) H(0.5 mm) Ampere [A/m]", H7(0.5e-3), 250)
chk("(c) H(2 mm) Ampere [A/m]", H7(2e-3), 500)
chk("check: H(a) [A/m]", H7(a), J0*a/3)
J7 = lambda X, Y: np.where(X*X + Y*Y < a*a, J0*np.hypot(X, Y)/a, 0.0)
chk("(c) H at (0.5 mm,0) 2-D B-S sum [A/m]", H_aligned(J7, 2e-6, a, (0.5e-3, 0.0), Itot), [0, 250])
chk("(c) H at (2 mm,0) 2-D B-S sum [A/m]", H_aligned(J7, 2e-6, a, (2e-3, 0.0), Itot), [0, 500])
r = 0.6e-3
dd = 1e-7
chk("check: (1/r) d(rH)/dr = Jz at 0.6 mm", ((r + dd)*H7(r + dd) - (r - dd)*H7(r - dd))/(2*dd)/r, J0*r/a)

# ---------------------------------------------------------------- 12.8
print("\n12.8  hairpin a = 2 cm, I = 3 A (+x on upper leg)")
a, I = 0.02, 3.0
up = ray_nodes([0, a, 0], -xh, a)[::-1]        # from x = -inf to (0,a,0): current +x
t = np.linspace(np.pi/2, -np.pi/2, 40001)      # (0,a) -> (a,0) -> (0,-a)
arc = np.c_[a*np.cos(t), a*np.sin(t), 0*t]
low = ray_nodes([0, -a, 0], -xh, a)            # from (0,-a,0) to x = -inf: current -x
Bu, Ba, Bl = bs(up, I, O3), bs(arc, I, O3), bs(low, I, O3)
chk("(a) upper leg [T]", Bu, [0, 0, -1.5e-5])
chk("(a) semicircle [T]", Ba, [0, 0, -4.71e-5])
chk("(a) lower leg [T]", Bl, [0, 0, -1.5e-5])
chk("(b) total [T]", Bu + Ba + Bl, [0, 0, -7.71e-5])
t = np.linspace(np.pi/2, np.pi/2 - 2*np.pi, 40001)
chk("check: full clockwise loop [T]", bs(np.c_[a*np.cos(t), a*np.sin(t), 0*t], I, O3), [0, 0, -9.42e-5])
chk("check: two infinite antiparallel wires [T]",
    B_line([0, a, 0], xh, I, O3) + B_line([0, -a, 0], -xh, I, O3), [0, 0, -6e-5])

# ---------------------------------------------------------------- 12.9
print("\n12.9  loop beside a wire (I1 = 20 A on z axis; loop x = 1..3 cm, z = 0..10 cm, I2 = 5 A)")
I1, I2, d, b, L = 20.0, 5.0, 0.01, 0.02, 0.10
chk("(a) B on near side [T]", B_line(O3, zh, I1, [d, 0, L/2]), [0, 4e-4, 0])
chk("(a) B on far side [T]", B_line(O3, zh, I1, [d + b, 0, L/2]), [0, 1.33e-4, 0])
xg, wg = np.polynomial.legendre.leggauss(40)


def side_force(A, Bp):
    A = np.asarray(A, float)
    Lv = np.asarray(Bp, float) - A
    pts = A + ((xg + 1)/2)[:, None]*Lv
    Bs = B_line(O3, zh, I1, pts)
    return np.sum((wg/2)[:, None]*I2*np.cross(Lv, Bs), axis=0)


c = [(d, 0, 0), (d, 0, L), (d + b, 0, L), (d + b, 0, 0), (d, 0, 0)]
Fs = [side_force(c[k], c[k + 1]) for k in range(4)]
chk("(b) near side [N]", Fs[0], [-2e-4, 0, 0])
chk("(b) top side [N]", Fs[1], [0, 0, 2.20e-5])
chk("(b) far side [N]", Fs[2], [6.67e-5, 0, 0])
chk("(b) bottom side [N]", Fs[3], [0, 0, -2.20e-5])
Fnet = sum(Fs)
chk("(c) net force on loop [N]", Fnet, [-1.33e-4, 0, 0])
chk("shorthand mu0 I1 I2/(2 pi) [N]", MU0*I1*I2/(2*np.pi), 2e-5)
chk("shorthand mu0 I1 I2 L/(2 pi) [N m]", MU0*I1*I2*L/(2*np.pi), 2e-6)
chk("shorthand b/(d(d+b)) [1/m]", b/(d*(d + b)), 66.7)
loop = np.vstack([seg_nodes(c[k], c[k + 1], 4001)[:-1] for k in range(4)] + [np.array(c[0])[None, :]])
th, wt = np.polynomial.legendre.leggauss(400)
th, wt = th*np.pi/2, wt*np.pi/2
zs = L/2 + L*np.tan(th)
Bax = bs(loop, I2, np.c_[0*zs, 0*zs, zs])
Fw = np.sum((wt*L/np.cos(th)**2)[:, None]*I1*np.cross(zh, Bax), axis=0)
chk("(d) force on the wire from the loop's B-S field [N]", Fw, [1.33e-4, 0, 0])
print(f"   Newton III residual |F_loop + F_wire| = {np.linalg.norm(Fnet + Fw):.1e} N")
Ff = lambda bb: -MU0*I1*I2*L/(2*np.pi)*(1/d - 1/(d + bb))
print(f"   limits: b -> 0: {Ff(1e-9):.2e} N ; b -> inf: {Ff(1e9):.4e} N")
chk("check: b -> inf limit [N]", Ff(1e9), -2e-4)

# ---------------------------------------------------------------- 12.10
print("\n12.10 crossing wires (RE-PARAMETERIZED: 3 A along +z on z axis, 1 A along -x on x axis)")
Iz, Ix = 3.0, 1.0
P = np.array([2.0, 0.0, 1.0])
B1 = B_line(O3, zh, Iz, P)
B2 = B_line(O3, -xh, Ix, P)
chk("(a) z wire at P [T]", B1, [0, 3e-7, 0])
chk("(a) x wire at P [T]", B2, [0, 2e-7, 0])
Bt = B1 + B2
chk("(a) total at P [T]", Bt, [0, 5e-7, 0])
chk("(a) total = 5 mu0/(4 pi) [T]", Bt[1], 5*MU0/(4*np.pi))


def Bpair(r):
    return B_line(O3, zh, Iz, r) + B_line(O3, -xh, Ix, r)


def parts_formula(r):
    x, y, z = r
    return (3*MU0/(2*np.pi)*np.array([-y, x, 0.0])/(x*x + y*y),
            MU0/(2*np.pi)*np.array([0.0, z, -y])/(y*y + z*z))


rng = np.random.default_rng(12)
dev = 0.0
for p in rng.uniform(-3, 3, (6, 3)):
    bd = Bpair(p)
    bf = sum(parts_formula(p))
    dev = max(dev, np.linalg.norm(bd - bf)/np.linalg.norm(bf))
chk("(b) page formula vs direct sum, max rel. deviation (6 random points)", dev, 0.0, atol=1e-6)
for nul in ([3.0, 0, -1.0], [-3.0, 0, 1.0]):
    rel = np.linalg.norm(Bpair(nul))/np.linalg.norm(B_line(O3, zh, Iz, nul))
    chk(f"(c) |B|/|B_z-wire| at {nul}", rel, 0.0, atol=1e-6)
zr = optimize.brentq(lambda z: Bpair([2.0, 0, z])[1], -0.9, -0.4, xtol=1e-12)
chk("check: B_y = 0 on x = 2 m, y = 0 at z [m]", zr, -2/3, rtol=1e-6)
zz = np.r_[np.linspace(-3, -0.05, 300), np.linspace(0.05, 3, 300)]
By = np.array([sum(parts_formula([2.0, 0, z]))[1] for z in zz])
print("   sign changes of B_y on x = 2 m (z grid, wire at z = 0 skipped):",
      np.round(zz[np.where(np.sign(By[:-1]) != np.sign(By[1:]))[0]], 2), "(the 0.05 entry = jump across the x wire)")


def resid(r):
    b1, b2 = parts_formula(r)
    return (b1 + b2)/(np.linalg.norm(b1) + np.linalg.norm(b2))


zeros = []
for s in rng.uniform(-5, 5, (300, 3)):
    try:
        rs = optimize.least_squares(resid, s, xtol=1e-15, ftol=1e-15, gtol=1e-15)
    except Exception:
        continue
    if np.linalg.norm(rs.fun) < 1e-9:
        zeros.append(rs.x)
zeros = np.array(zeros)
print(f"   global null search: {len(zeros)} of 300 starts converged to B = 0; "
      f"max|y|/|x| = {np.max(np.abs(zeros[:, 1])/np.abs(zeros[:, 0])):.1e}, "
      f"max|z + x/3|/|x| = {np.max(np.abs(zeros[:, 2] + zeros[:, 0]/3)/np.abs(zeros[:, 0])):.1e}")
chk("(c) all nulls found lie on y = 0, z = -x/3 (max deviation)",
    np.max(np.abs(zeros[:, 2] + zeros[:, 0]/3)/np.abs(zeros[:, 0])) + np.max(np.abs(zeros[:, 1])/np.abs(zeros[:, 0])),
    0.0, atol=1e-6)
vp = 1e5*xh
Fp = QE*np.cross(vp, Bt)
chk("(d) F on proton [N]", Fp, [0, 0, 8.01e-21])
chk("(d) v x B [V/m]", np.cross(vp, Bt), [0, 0, 0.05])
Ef = -np.cross(vp, Bt)
chk("(d) E for zero force [V/m]", Ef, [0, 0, -0.05])
chk("(d) E/B [m/s]", np.linalg.norm(Ef)/np.linalg.norm(Bt), 1e5)
chk("(d) total Lorentz force with E [N]", QE*(Ef + np.cross(vp, Bt)), [0, 0, 0], atol=1e-30)

print("   --- exam overlap (catalogue setups) ---")


def B20(r):     # Summer 2020 HE2 #2a: 2 A along +x on x axis, 4 A along -y on y axis
    return B_line(O3, xh, 2.0, r) + B_line(O3, -yh, 4.0, r)


print("   2020 #2a key: B(1,1,0) =", B20([1.0, 1.0, 0.0]), "T  (= 3 mu0/pi z =", 3*MU0/np.pi, ")")
print("   2020 #2a key: |B(2,-1,0)| =", f"{np.linalg.norm(B20([2.0, -1.0, 0.0])):.1e}", "T -> null line z = 0, x = -2y")
n = np.array([0, 1, -1])/np.sqrt(2)
Rm = 2*np.outer(n, n) - np.eye(3)          # 180-degree rotation about (0,1,-1)/sqrt(2)


def Bold(r):    # page's ORIGINAL 12.10: 4 A along +z on z axis, 2 A along -x on x axis
    return B_line(O3, zh, 4.0, r) + B_line(O3, -xh, 2.0, r)


dmax = max(np.linalg.norm(Bold(Rm @ p) - Rm @ B20(p))/np.linalg.norm(B20(p)) for p in rng.uniform(-3, 3, (4, 3)))
print(f"   ORIGINAL 12.10 = 2020 exam rotated (det R = {np.linalg.det(Rm):+.0f}): max |B_old(Rp) - R B_exam(p)|/|B| = {dmax:.1e}")
print("   rotated exam null points R(2,-1,0), R(-2,1,0) =", Rm @ [2, -1, 0], Rm @ [-2, 1, 0],
      "= the original page's null points (-2,0,1), (2,0,-1): the key carried over -> re-parameterized")
Hper = (B_line(O3, zh, 1.0, [1, 0, -1]) + B_line(O3, xh, 1.0, [1, 0, -1]))/MU0
print(f"   2017 #1a key: I0 = 4/H_y(per A) = {4/Hper[1]:.4f} A (4 pi = {4*np.pi:.4f})")
print("   new page values: currents 3 A, 1 A (exams: 2 A/4 A; equal I0); B(P) = 5e-7 y T; null line z = -x/3")

# ---------------------------------------------------------------- 12.11
print("\n12.11 coax with unequal currents (a = 1, b = 2, c = 6 mm; I1 = 3 A +z, I2 = 8 A -z)")
a, b, c, I1, I2 = 1e-3, 2e-3, 6e-3, 3.0, 8.0
J1 = I1/(np.pi*a*a)
J2 = -I2/(np.pi*(c*c - b*b))
chk("(a) J1 [A/m^2]", J1, 9.55e5)
chk("(a) J2 [A/m^2]", J2, -7.96e4)


def Jz(r):
    return J1 if r < a else (J2 if b < r < c else 0.0)


def Ienc(r):
    pts = [p for p in (a, b, c) if p < r]
    return integrate.quad(lambda s: Jz(s)*2*np.pi*s, 0, r, points=pts or None, limit=200)[0]


radii = [0.5e-3, 1.5e-3, 3e-3, 5e-3, 10e-3]
pI = [0.75, 3, 1.75, -2.25, -5]
pH = [238.7, 318.3, 92.8, -71.6, -79.6]
J11 = lambda X, Y: np.where(X*X + Y*Y < a*a, J1, np.where((X*X + Y*Y > b*b) & (X*X + Y*Y < c*c), J2, 0.0))
for r, ii, hh in zip(radii, pI, pH):
    chk(f"(c) I_enc({r*1e3:g} mm) [A]", Ienc(r), ii)
    chk(f"(c) H_phi({r*1e3:g} mm) Ampere [A/m]", Ienc(r)/(2*np.pi*r), hh, rtol=1e-3)
    cx, cy, Ic = cells(J11, 5e-6, c, origin=(r, 0.0))
    inner = cx*cx + cy*cy < a*a
    Ic = np.where(inner, Ic*I1/Ic[inner].sum(), Ic*(-I2)/Ic[~inner].sum())
    chk(f"(c) H at ({r*1e3:g} mm,0) 2-D B-S sum [A/m]", H_cells(cx, cy, Ic, (r, 0.0)), [0, hh], rtol=3e-3)
r0 = optimize.brentq(Ienc, b*1.0001, c*0.9999, xtol=1e-14)
chk("(d) null radius [mm]", r0*1e3, 4.0, rtol=1e-6)
for rb, val in ((a, 477.5), (b, 238.7), (c, -132.6)):
    chk(f"check: H_phi at r = {rb*1e3:g} mm [A/m]", Ienc(rb)/(2*np.pi*rb), val, rtol=1e-3)
r = 4.5e-3
dd = 1e-8
chk("check: (1/r) d(rH)/dr = J2 in outer conductor",
    ((r + dd)*Ienc(r + dd)/(2*np.pi*(r + dd)) - (r - dd)*Ienc(r - dd)/(2*np.pi*(r - dd)))/(2*dd)/r, J2)
print("   (d) outside: H_phi < 0 -> along -phi, clockwise seen from +z; at (10 mm,0,0) H =",
      np.round(Ienc(10e-3)/(2*np.pi*10e-3)*yh, 2), "A/m")

# ---------------------------------------------------------------- 12.12
print("\n12.12 wire with off-axis hole (a = 3 cm, b = 1 cm, d = 1.5 cm, I = 40 A)")
a, b, d, I = 0.03, 0.01, 0.015, 40.0
J = I/(np.pi*(a*a - b*b))
chk("(a) J [A/m^2]", J, 1.59e4)
chk("(a) J = 5e4/pi", J, 5e4/np.pi, rtol=1e-9)
chk("(a) pieces J pi a^2, -J pi b^2 [A]", [J*np.pi*a*a, -J*np.pi*b*b], [45, -5])
metal = lambda X, Y: np.where((X*X + Y*Y < a*a) & ((X - d)**2 + Y*Y > b*b), J, 0.0)
cx, cy, Ic = cells(metal, 5e-5, a)
Ic *= I/Ic.sum()
hole_pts = [(0.015, 0), (0.015, 0.006), (0.021, -0.005), (0.008, 0.003), (0.015, -0.009)]
Hh = H_cells(cx, cy, Ic, hole_pts)
for p, hv in zip(hole_pts, Hh):
    chk(f"(b) H in hole at {p} m [A/m]", hv, [0, 119.4])
chk("(b) B in hole [T]", MU0*Hh.mean(axis=0), [0, 1.5e-4])
chk("(b) (J d/2) = 375/pi [A/m]", J*d/2, 375/np.pi, rtol=1e-9)
H6 = H_cells(cx, cy, Ic, (0.06, 0.0))
chk("(d) H at (6 cm,0,0) 2-D B-S sum [A/m]", H6, [0, 101.7])
chk("(d) pieces 45/(2 pi 0.06), 5/(2 pi 0.045) [A/m]",
    [45/(2*np.pi*0.06), 5/(2*np.pi*0.045)], [119.4, 17.7])
chk("(d) centred 40 A line [A/m]", I/(2*np.pi*0.06), 106.1)
chk("(d) ratio", H6[1]/(I/(2*np.pi*0.06)), 0.958)
cx2, cy2, Ic2 = cells(metal, 1e-4, a)
Ic2 *= I/Ic2.sum()
ph = np.linspace(0, 2*np.pi, 361)[:-1]
Pcirc = np.c_[0.06*np.cos(ph), 0.06*np.sin(ph)]
Hcir = H_cells(cx2, cy2, Ic2, Pcirc)
Hmag = np.linalg.norm(Hcir, axis=1)
Hr = Hcir[:, 0]*np.cos(ph) + Hcir[:, 1]*np.sin(ph)
Hp = -Hcir[:, 0]*np.sin(ph) + Hcir[:, 1]*np.cos(ph)
chk("(d) min |H| on r = 6 cm [A/m]", Hmag.min(), 101.7)
chk("(d) max |H| on r = 6 cm [A/m]", Hmag.max(), 108.8)
print(f"   (d) min at phi = {np.degrees(ph[Hmag.argmin()]):.0f} deg, max at phi = {np.degrees(ph[Hmag.argmax()]):.0f} deg; "
      f"max |H_r| = {np.abs(Hr).max():.2f} A/m (not purely along phi)")
chk("(d) circulation on r = 6 cm [A]", np.sum(Hp)*0.06*(2*np.pi/360), 40.0)
conc = lambda X, Y: np.where((X*X + Y*Y < a*a) & (X*X + Y*Y > b*b), J, 0.0)
cx3, cy3, Ic3 = cells(conc, 5e-5, a)
Ic3 *= I/Ic3.sum()
Hc0 = H_cells(cx3, cy3, Ic3, [(0.0, 0.0), (0.005, 0.004), (-0.007, 0.0)])
chk("(c) concentric: max |H| in hole [A/m]", np.abs(Hc0).max(), 0.0, atol=0.05)
chk("(c) concentric: I_enc(2 cm) [A]", J*np.pi*(0.02**2 - b*b), 15.0)
chk("(c) concentric: H at (2 cm,0) 2-D B-S sum, aligned grid [A/m]",
    H_aligned(conc, 5e-5, a, (0.02, 0.0), I), [0, 119.4])
chk("check: concentric H at r = a, inside form J(a^2-b^2)/(2a) [A/m]", J*(a*a - b*b)/(2*a), 212.2)
chk("check: concentric H at r = a, outside form I/(2 pi a) [A/m]", I/(2*np.pi*a), 212.2)

print(f"\nTOTAL: {NP} PASS, {NF} FAIL")
