#!/usr/bin/env python3
"""Verification for practice/12-magnetic-force-biot-savart-and-ampere.md (Lecture 12).

Rules followed (SPEC section 1):
  * every Biot-Savart result is checked by direct numerical integration of I dl x R^ / R^2
    (bs_curve / bs_line / bs_segment below, scipy quad_vec), never by the closed form alone;
  * every direction comes from an explicit np.cross;
  * every Ampere result is checked by numerically integrating J over the enclosed area (dblquad);
  * every number, sign and direction printed on the page is printed here.
numpy + scipy only.
"""
import numpy as np
from scipy.integrate import quad, quad_vec, dblquad, solve_ivp
from scipy.optimize import brentq

eps0 = 8.8541878128e-12
mu0 = 4 * np.pi * 1e-7
e = 1.602176634e-19
me = 9.1093837e-31
c0 = 2.99792458e8
X, Y, Z = np.eye(3)
O = np.zeros(3)


def vec(v, fmt="{:+.6g}"):
    return "(" + ", ".join(fmt.format(float(x)) for x in v) + ")"


def close(a, b, rtol=1e-6, atol=0.0):
    ok = np.allclose(np.asarray(a, float), np.asarray(b, float), rtol=rtol, atol=atol)
    return "OK" if ok else "MISMATCH <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"


# ----------------------------------------------------------------------------- Biot-Savart engine
def bs_curve(P, rfun, drfun, t0, t1, I, epsrel=1e-11):
    """B at P from current I along the curve r(t), t0 -> t1 (current flows toward increasing t):
    B = mu0 I/(4 pi) * integral of (dr/dt x R^)/R^2 dt, with R = P - r(t) from source to field point."""
    P = np.asarray(P, float)

    def f(t):
        R = P - rfun(t)
        Rn = np.linalg.norm(R)
        return np.cross(drfun(t), R / Rn) / Rn**2

    val, _ = quad_vec(f, t0, t1, epsrel=epsrel, epsabs=0.0, limit=5000)
    return mu0 * I / (4 * np.pi) * val


def bs_line(P, r0, u, I):
    """Infinite straight wire through r0, current I along unit vector u (split at the foot of the perpendicular)."""
    u = np.asarray(u, float) / np.linalg.norm(u)
    r0 = np.asarray(r0, float)
    ts = float(np.dot(np.asarray(P, float) - r0, u))
    rf = lambda t: r0 + t * u
    df = lambda t: u
    return bs_curve(P, rf, df, -np.inf, ts, I) + bs_curve(P, rf, df, ts, np.inf, I)


def bs_segment(P, A, B, I):
    """Straight segment, current I flowing from A to B."""
    A = np.asarray(A, float)
    B = np.asarray(B, float)
    return bs_curve(P, lambda t: A + t * (B - A), lambda t: (B - A), 0.0, 1.0, I)


def wire_formula(P, r0, u, I):
    """Closed form mu0 I/(2 pi r) phi^, phi^ = u x r^ (used only to compare with the quadrature)."""
    u = np.asarray(u, float) / np.linalg.norm(u)
    d = np.asarray(P, float) - np.asarray(r0, float)
    rperp = d - np.dot(d, u) * u
    r = np.linalg.norm(rperp)
    return mu0 * I / (2 * np.pi * r) * np.cross(u, rperp / r)


print("constants: mu0 = %.10e H/m, mu0/(2 pi) = %.3e, e = %.9e C, me = %.7e kg" % (mu0, mu0 / (2 * np.pi), e, me))

# ============================================================================= 12.1
print("\n=== 12.1 A charge passing a wire (MC)")
I = 2.0
P = np.array([0.0, 1.0, -3.0])
u = -Y                                   # current direction
r_vec = P - np.dot(P, u) * u             # perpendicular vector from the y axis to P
r = np.linalg.norm(r_vec)
rhat = r_vec / r
phihat = np.cross(u, rhat)
print("distance r =", r, " rhat =", vec(rhat), " phihat = (-y) x rhat =", vec(phihat))
B = bs_line(P, O, u, I)
print("B (Biot-Savart quadrature) =", vec(B), "T ; closed form mu0 I/(2 pi r) phihat =", vec(wire_formula(P, O, u, I)),
      close(B, wire_formula(P, O, u, I), atol=1e-20))
print("|B| = %.6e T  (= 2e-7*2/3 = %.6e)" % (np.linalg.norm(B), 2e-7 * 2 / 3))
v = 5 * Z
F = np.cross(v, B)                       # per coulomb of Q
print("F/Q = v x B =", vec(F), "N/C  -> direction +y, magnitude %.4e N per coulomb" % np.linalg.norm(F))
print("F.v =", np.dot(F, v), " F.B =", np.dot(F, B))
print("distractor (d): B x v =", vec(np.cross(B, v)), " (reversed order gives -y)")
print("distractor (a)/(b): B itself is along", vec(B / np.linalg.norm(B)))
print("watch-out: v = 5 x^ gives v x B =", vec(np.cross(5 * X, B)), " (zero: v parallel to B)")
print("radial velocity component v.rhat =", np.dot(v, rhat), " (negative: the charge is heading toward the wire)")
print("page 12.1: r = %g m, |B| = %.3g T along +x, |F|/Q = %.3g N/C along +y" % (r, np.linalg.norm(B), np.linalg.norm(F)))

# ============================================================================= 12.2
print("\n=== 12.2 Two antiparallel wires")
I1, I2, d = 10.0, 6.0, 0.04
B1_at2 = bs_line([0, d, 0], O, X, I1)
print("B1 at wire 2 =", vec(B1_at2), "T  closed form", vec(wire_formula([0, d, 0], O, X, I1)),
      close(B1_at2, wire_formula([0, d, 0], O, X, I1), atol=1e-20))
F2 = I2 * np.cross(-X, B1_at2)
print("force per metre on wire 2 = I2 (-x^) x B1 =", vec(F2), "N/m  (away from wire 1 -> repel)")
print("mu0 I1 I2/(2 pi d) = %.6e N/m" % (mu0 * I1 * I2 / (2 * np.pi * d)))
B2_at1 = bs_line(O, [0, d, 0], -X, I2)
F1 = I1 * np.cross(X, B2_at1)
print("B2 at wire 1 =", vec(B2_at1), " force per metre on wire 1 =", vec(F1), " (Newton 3:", close(F1, -F2, atol=1e-18), ")")
Pm = np.array([0, 0.02, 0])
B1m = bs_line(Pm, O, X, I1)
B2m = bs_line(Pm, [0, d, 0], -X, I2)
print("midway: B1 =", vec(B1m), " B2 =", vec(B2m), " total =", vec(B1m + B2m), "T")
print("   phi^ for wire 2 at midpoint: (-x) x (-y) =", vec(np.cross(-X, -Y)))
print("page 12.2: B1 at wire 2 = %.1e T (+z); F2/l = %.1e N/m (+y, repel); midpoint %.1e + %.1e = %.1e T (+z); B2 at wire 1 = %.1e T (+z); F1/l = %.1e N/m (y)" %
      (B1_at2[2], F2[1], B1m[2], B2m[2], (B1m + B2m)[2], B2_at1[2], F1[1]))

# ============================================================================= 12.3
print("\n=== 12.3 An electron in Earth's field (calculator)")
v0, B0 = 2e5, 5e-5
R = me * v0 / (e * B0)
T = 2 * np.pi * me / (e * B0)
f = 1 / T
print("R = me v/(e B) = %.6e m = %.4f cm" % (R, R * 100))
print("T = 2 pi me/(e B) = %.6e s = %.4f us ; f = %.6e Hz = %.4f MHz" % (T, T * 1e6, f, f / 1e6))
print("2 pi R / v =", 2 * np.pi * R / v0, " (same T)")
Fdir = (-e) * np.cross(v0 * X, B0 * Z)
print("force on electron moving +x in B z^: (-e) v x B =", vec(Fdir), "N -> pushed toward +y (turns left)")


def rhs(t, s):
    vv = s[3:]
    a = (-e / me) * np.cross(vv, B0 * Z)
    return np.concatenate([vv, a])


sol = solve_ivp(rhs, [0, T], [0, 0, 0, v0, 0, 0], rtol=1e-11, atol=1e-14, dense_output=True)
ts = np.linspace(0, T, 4001)[:-1]
pos = sol.sol(ts)[:3].T
vel = sol.sol(ts)[3:].T
ctr = pos.mean(axis=0)
rad = np.linalg.norm(pos - ctr, axis=1)
Lz = np.cross(pos - ctr, vel)[:, 2]
print("simulated: centre =", vec(ctr), " radius mean %.6e (min %.6e, max %.6e)" % (rad.mean(), rad.min(), rad.max()))
print("simulated: |r(T)-r(0)| = %.3e m ; speed drift = %.3e" % (np.linalg.norm(sol.y[:3, -1]), abs(np.linalg.norm(sol.y[3:, -1]) - v0) / v0))
print("simulated: sign of (r - c) x v . z^ :", "positive -> counter-clockwise seen from +z" if np.all(Lz > 0) else "NOT all positive")
print("work per revolution: integral F.v dt =", quad(lambda t: np.dot((-e) * np.cross(sol.sol(t)[3:], B0 * Z), sol.sol(t)[3:]), 0, T)[0], "J")
print("proton would go:", "clockwise" if np.cross(Y * 0 + X, (e) * np.cross(X, Z))[2] < 0 else "counter-clockwise",
      "(force on +q moving +x is", vec(np.cross(X, Z)), ")")
print("page 12.3: F = %.2e N (+y); R = %.2f cm; T = %.2e s = %.3f us; f = %.2f MHz; centre (0, %.2f cm, 0), counter-clockwise seen from +z" %
      (np.linalg.norm(Fdir), R * 100, T, T * 1e6, f / 1e6, ctr[1] * 100))

# ============================================================================= 12.4
print("\n=== 12.4 Could this be a magnetic field (MC)")
B0c, ac = 1.3, 0.7
fields = {
    "(a) (B0/a)(x,y,0)": lambda p: (B0c / ac) * np.array([p[0], p[1], 0.0]),
    "(b) (B0/a)(x,-y,z)": lambda p: (B0c / ac) * np.array([p[0], -p[1], p[2]]),
    "(c) (B0/a)(y,-x,0)": lambda p: (B0c / ac) * np.array([p[1], -p[0], 0.0]),
    "(d) B0 r^ (spherical)": lambda p: B0c * np.asarray(p) / np.linalg.norm(p),
}
h = 1e-5


def div(F, p):
    p = np.asarray(p, float)
    return sum((F(p + h * E)[k] - F(p - h * E)[k]) / (2 * h) for k, E in enumerate(np.eye(3)))


def curl(F, p):
    p = np.asarray(p, float)
    J = np.array([[(F(p + h * E)[i] - F(p - h * E)[i]) / (2 * h) for E in np.eye(3)] for i in range(3)])  # J[i][j] = dF_i/dx_j
    return np.array([J[2][1] - J[1][2], J[0][2] - J[2][0], J[1][0] - J[0][1]])


pts = [np.array([0.3, -0.4, 0.5]), np.array([1.1, 0.2, -0.7])]
for name, F in fields.items():
    print(name, " div at pts:", ["%.6f" % div(F, p) for p in pts])
print("expected: (a) 2B0/a = %.6f, (b) B0/a = %.6f, (c) 0, (d) 2B0/r = %s" % (2 * B0c / ac, B0c / ac,
      ["%.6f" % (2 * B0c / np.linalg.norm(p)) for p in pts]))
Fc = fields["(c) (B0/a)(y,-x,0)"]
cc = curl(Fc, pts[0])
print("curl of (c) =", vec(cc), " expected (0,0,-2B0/a) =", vec([0, 0, -2 * B0c / ac]))
p = pts[0]
rr = np.hypot(p[0], p[1])
phih = np.array([-p[1] / rr, p[0] / rr, 0])
print("(c) vs -(B0 r/a) phi^ :", vec(Fc(p)), vec(-(B0c * rr / ac) * phih), close(Fc(p), -(B0c * rr / ac) * phih))
print("(c) at (1,0,0):", vec(Fc([1, 0, 0])), " at (0,1,0):", vec(Fc([0, 1, 0])), " -> clockwise seen from +z")
print("J for (c) = curl B/mu0 = -(2B0/(mu0 a)) z^ ; uniform-wire check |B| = mu0|J|r/2 :",
      close(mu0 * (2 * B0c / (mu0 * ac)) * rr / 2, np.linalg.norm(Fc(p))))

# ============================================================================= 12.5
print("\n=== 12.5 Counting current in delta functions")
Istrip = quad(lambda y: 6 * y * (1 - y), 0, 1)[0]
print("strip total current integral_0^1 6y(1-y) dy = %.12f A (flows in -z)" % Istrip)
print("max J_s at y=0.5:", 6 * 0.5 * 0.5, "A/m")
sig = 1e-3


def sift(x0, lo, hi):
    """integral over [lo, hi] of a narrow normalized Gaussian centred at x0 (a delta-sequence),
    split so that the peak window [x0-10 sig, x0+10 sig] is integrated on its own."""
    g = lambda u: np.exp(-(u - x0)**2 / (2 * sig**2)) / (np.sqrt(2 * np.pi) * sig)
    cuts = sorted({lo, hi, min(max(x0 - 10 * sig, lo), hi), min(max(x0 + 10 * sig, lo), hi)})
    return sum(quad(g, p_, q_, limit=200)[0] for p_, q_ in zip(cuts[:-1], cuts[1:]) if q_ > p_)


wx1, wy1, wx2 = sift(1, 0, 3), sift(1, 0, 3), sift(2, 0, 3)
line_part = 4 * wx1 * wy1
strip_part = -quad(lambda y: 6 * y * (1 - y), 0, 1)[0] * wx2
print("delta-sequence weights: %.9f %.9f %.9f" % (wx1, wy1, wx2))
print("narrow-Gaussian sifting over 0<x<3, 0<y<3: line %+.9f A, strip %+.9f A, net %+.9f A" % (line_part, strip_part, line_part + strip_part))
lp2 = 4 * sift(1, 1.5, 3) * sift(1, 0, 3)
sp2 = -quad(lambda y: 6 * y * (1 - y), 0, 1)[0] * sift(2, 1.5, 3)
print("same over 1.5<x<3 (line excluded): line %+.9f A, strip %+.9f A, net %+.9f A" % (lp2, sp2, lp2 + sp2))
print("page 12.5: line %.0f A (+z), strip %.0f A (peak J_s %.1f A/m), (b) %+.0f A, (c) %+.0f A, (b)-(c) = %.0f A" %
      (line_part, strip_part, 6 * 0.5 * 0.5, line_part + strip_part, lp2 + sp2, (line_part + strip_part) - (lp2 + sp2)))

# ============================================================================= 12.6
print("\n=== 12.6 The centre of a square loop (find the error)")
a, I = 0.1, 5.0
h2 = a / 2
corners = [np.array([-h2, -h2, 0]), np.array([h2, -h2, 0]), np.array([h2, h2, 0]), np.array([-h2, h2, 0])]  # CCW from +z
Bsides = [bs_segment(O, corners[k], corners[(k + 1) % 4], I) for k in range(4)]
for k, Bk in enumerate(Bsides):
    print("side %d (from %s to %s): B =" % (k, vec(corners[k], "{:+.2f}"), vec(corners[(k + 1) % 4], "{:+.2f}")), vec(Bk), "T")
Btot = sum(Bsides)
print("one side closed form sqrt2 mu0 I/(2 pi a) = %.6e T" % (np.sqrt(2) * mu0 * I / (2 * np.pi * a)))
print("finite-segment formula mu0 I/(4 pi d)(sin a2 - sin a1), d=a/2, a=+-45deg: %.6e T" %
      (mu0 * I / (4 * np.pi * h2) * (np.sin(np.pi / 4) - np.sin(-np.pi / 4))))
print("integral_{-d}^{d} dx/(x^2+d^2)^{3/2} (d=a/2) = %.6f ; sqrt2/d^2 = %.6f" %
      (quad(lambda x: (x * x + h2 * h2)**-1.5, -h2, h2)[0], np.sqrt(2) / h2**2))
print("total B (quadrature) =", vec(Btot), "T ; closed form 2 sqrt2 mu0 I/(pi a) = %.6e" % (2 * np.sqrt(2) * mu0 * I / (np.pi * a)),
      close(Btot[2], 2 * np.sqrt(2) * mu0 * I / (np.pi * a)))
print("direction check: bottom side dl = +x, R^ from (0,-a/2) to centre = +y: x cross y =", vec(np.cross(X, Y)))
Rc = a / 2
Bcirc = bs_curve(O, lambda t: Rc * np.array([np.cos(t), np.sin(t), 0]), lambda t: Rc * np.array([-np.sin(t), np.cos(t), 0]), 0, 2 * np.pi, I)
print("circle radius a/2 (quadrature) =", vec(Bcirc), " closed form mu0 I/(2R) = mu0 I/a = %.6e" % (mu0 * I / a))
print("ratio square/circle = %.6f ; 2 sqrt2/pi = %.6f" % (Btot[2] / Bcirc[2], 2 * np.sqrt(2) / np.pi))


def B_square(Pt):
    return sum(bs_segment(Pt, corners[k], corners[(k + 1) % 4], I) for k in range(4))


rs = a / 4
phis = np.linspace(0, 2 * np.pi, 9)[:-1]
Hs = np.array([B_square(rs * np.array([np.cos(p_), np.sin(p_), 0])) / mu0 for p_ in phis])
print("student's circle r=a/4: max |H_x|,|H_y| = %.3e A/m ; H_z ranges %.4f .. %.4f A/m" %
      (np.abs(Hs[:, :2]).max(), Hs[:, 2].min(), Hs[:, 2].max()))
circ = quad(lambda p_: np.dot(B_square(rs * np.array([np.cos(p_), np.sin(p_), 0])) / mu0,
                              rs * np.array([-np.sin(p_), np.cos(p_), 0])), 0, 2 * np.pi, limit=200)[0]
print("circulation of H around it (quadrature) = %.3e A  (zero, but H is not)" % circ)
print("H at the centre = %.4f A/m" % (Btot[2] / mu0))
print("page 12.6: per side %.2e T; total %.2e T (+z); H = %.1f A/m (+z); circle radius a/2: %.2e T; ratio %.3f; student's circle H_z %.1f..%.1f A/m" %
      (Bsides[0][2], Btot[2], Btot[2] / mu0, Bcirc[2], Btot[2] / Bcirc[2], Hs[:, 2].min(), Hs[:, 2].max()))

# ============================================================================= 12.7
print("\n=== 12.7 A wire with a nonuniform current (exemplar)")
a7, J0 = 1e-3, 3e6
Jz7 = lambda rr: J0 * rr / a7 if rr < a7 else 0.0


def Ienc7(rr):
    return dblquad(lambda rp, ph: Jz7(rp) * rp, 0, 2 * np.pi, 0, min(rr, a7), epsabs=1e-12, epsrel=1e-12)[0]


Itot7 = Ienc7(a7)
print("I = integral J dA = %.9f A ; 2 pi J0 a^2/3 = %.9f ; 2 pi = %.9f" % (Itot7, 2 * np.pi * J0 * a7**2 / 3, 2 * np.pi))
for rr in [0.5e-3, 1e-3, 2e-3]:
    Hn = Ienc7(rr) / (2 * np.pi * rr)
    Hf = J0 * rr**2 / (3 * a7) if rr <= a7 else J0 * a7**2 / (3 * rr)
    print("r = %.1f mm: H = I_enc/(2 pi r) = %.6f A/m ; formula %.6f %s" % (rr * 1e3, Hn, Hf, close(Hn, Hf)))
print("J0 a/12 = %.3f, J0 a/6 = %.3f, J0 a/3 = %.3f A/m" % (J0 * a7 / 12, J0 * a7 / 6, J0 * a7 / 3))
Hin = lambda rr: J0 * rr**2 / (3 * a7)
for rr in [0.3e-3, 0.7e-3]:
    dh = 1e-9
    curlz = ((rr + dh) * Hin(rr + dh) - (rr - dh) * Hin(rr - dh)) / (2 * dh) / rr
    print("curl check r=%.1f mm: (1/r)d(rH)/dr = %.6e ; J = %.6e %s" % (rr * 1e3, curlz, Jz7(rr), close(curlz, Jz7(rr), rtol=1e-5)))
print("page 12.7: I = 2 pi = %.2f A; H(0.5 mm) = %.0f A/m; H(2 mm) = %.0f A/m; at r = a: J0 a/3 = %.0f A/m" %
      (Itot7, Ienc7(0.5e-3) / (2 * np.pi * 0.5e-3), Ienc7(2e-3) / (2 * np.pi * 2e-3), J0 * a7 / 3))

# ============================================================================= 12.8
print("\n=== 12.8 A hairpin of current")
a8, I8 = 0.02, 3.0
B_up = bs_curve(O, lambda t: np.array([t, a8, 0]), lambda t: X, -np.inf, 0.0, I8)
B_arc = bs_curve(O, lambda s: a8 * np.array([np.sin(s), np.cos(s), 0]), lambda s: a8 * np.array([np.cos(s), -np.sin(s), 0]), 0.0, np.pi, I8)
B_lo = bs_curve(O, lambda t: np.array([-t, -a8, 0]), lambda t: -X, 0.0, np.inf, I8)
print("arc direction at (a,0,0): dl =", vec(a8 * np.array([np.cos(np.pi / 2), -np.sin(np.pi / 2), 0]) / a8), " dl x R^ = (-y) x (-x) =", vec(np.cross(-Y, -X)))
print("integral_{-inf}^0 dx/(x^2+a^2)^{3/2} = %.6f ; 1/a^2 = %.6f" % (quad(lambda x: (x * x + a8 * a8)**-1.5, -np.inf, 0)[0], 1 / a8**2))
print("upper leg  B =", vec(B_up), " closed form -mu0 I/(4 pi a) z^ = %.6e" % (-mu0 * I8 / (4 * np.pi * a8)))
print("semicircle B =", vec(B_arc), " closed form -mu0 I/(4a) z^ = %.6e" % (-mu0 * I8 / (4 * a8)))
print("lower leg  B =", vec(B_lo))
Bh = B_up + B_arc + B_lo
print("total B =", vec(Bh), " closed form -(mu0 I/(4a))(1+2/pi) = %.6e" % (-(mu0 * I8 / (4 * a8)) * (1 + 2 / np.pi)),
      close(Bh[2], -(mu0 * I8 / (4 * a8)) * (1 + 2 / np.pi)))
Bfull = bs_curve(O, lambda s: a8 * np.array([np.sin(s), np.cos(s), 0]), lambda s: a8 * np.array([np.cos(s), -np.sin(s), 0]), 0.0, 2 * np.pi, I8)
print("full circle (clockwise) check:", vec(Bfull), " mu0 I/(2a) = %.6e" % (mu0 * I8 / (2 * a8)))
print("1 + 2/pi = %.6f ; infinite pair of legs would give 2 mu0 I/(2 pi a) = %.6e (legs give half: %.6e)" %
      (1 + 2 / np.pi, 2 * mu0 * I8 / (2 * np.pi * a8), 2 * mu0 * I8 / (4 * np.pi * a8)))
print("page 12.8: each leg %.1e T (z); semicircle %.2e T (z); total %.2e T (z); full clockwise circle %.2e T (z); legs together %.0e T (z) vs two infinite wires %.0e T" %
      (B_up[2], B_arc[2], Bh[2], Bfull[2], B_up[2] + B_lo[2], 2 * mu0 * I8 / (2 * np.pi * a8)))

# ============================================================================= 12.9
print("\n=== 12.9 A rectangular loop beside a wire")
I1, I2, d9, b9, L9 = 20.0, 5.0, 0.01, 0.02, 0.10
Bw = lambda Pt: bs_line(Pt, O, Z, I1)
for xx in [d9, d9 + b9]:
    Bq = Bw([xx, 0, 0.05])
    print("B of wire at (x=%.2f m, y=0): %s T ; mu0 I1/(2 pi x) = %.6e %s" % (xx, vec(Bq), mu0 * I1 / (2 * np.pi * xx), close(Bq, [0, mu0 * I1 / (2 * np.pi * xx), 0], atol=1e-18)))
print("phi^ at (x>0, y=0) = z x x =", vec(np.cross(Z, X)))
F_near = quad_vec(lambda z: I2 * np.cross(Z, Bw([d9, 0, z])), 0, L9, epsrel=1e-10)[0]
F_far = quad_vec(lambda z: I2 * np.cross(-Z, Bw([d9 + b9, 0, z])), 0, L9, epsrel=1e-10)[0]
F_top = quad_vec(lambda x: I2 * np.cross(X, Bw([x, 0, L9])), d9, d9 + b9, epsrel=1e-10)[0]
F_bot = quad_vec(lambda x: I2 * np.cross(-X, Bw([x, 0, 0.0])), d9, d9 + b9, epsrel=1e-10)[0]
k9 = mu0 * I1 * I2 / (2 * np.pi)
print("shorthand mu0 I1 I2/(2 pi) = %.6e N" % k9)
print("mu0 I1 I2 L/(2 pi) = %.6e N m ; mu0 I1 I2/(2 pi) ln3 = %.6e N ; ln 3 = %.6f" % (k9 * L9, k9 * np.log(3), np.log(3)))
print("F_near =", vec(F_near), " closed -mu0I1I2L/(2pi d) = %.6e" % (-k9 * L9 / d9))
print("F_far  =", vec(F_far), " closed +mu0I1I2L/(2pi(d+b)) = %.6e" % (k9 * L9 / (d9 + b9)))
print("F_top  =", vec(F_top), " closed +(mu0I1I2/2pi) ln((d+b)/d) = %.6e" % (k9 * np.log((d9 + b9) / d9)))
print("F_bot  =", vec(F_bot))
Fnet = F_near + F_far + F_top + F_bot
print("net F on loop =", vec(Fnet), " closed -mu0 I1 I2 L b/(2 pi d (d+b)) = %.6e" % (-k9 * L9 * b9 / (d9 * (d9 + b9))),
      close(Fnet[0], -k9 * L9 * b9 / (d9 * (d9 + b9))))
print("1/d - 1/(d+b) = %.4f 1/m" % (1 / d9 - 1 / (d9 + b9)))
loopc = [np.array([d9, 0, 0]), np.array([d9, 0, L9]), np.array([d9 + b9, 0, L9]), np.array([d9 + b9, 0, 0])]


def B_loop(Pt):
    return sum(bs_segment(Pt, loopc[k], loopc[(k + 1) % 4], I2) for k in range(4))


fw = lambda z: I1 * np.cross(Z, B_loop([0, 0, z]))
F_wire = (quad_vec(fw, -np.inf, 0.0, epsrel=1e-9)[0] + quad_vec(fw, 0.0, L9, epsrel=1e-9)[0] + quad_vec(fw, L9, np.inf, epsrel=1e-9)[0])
print("force of the loop on the wire (double quadrature) =", vec(F_wire), " Newton 3:", close(F_wire, -Fnet, rtol=1e-6, atol=1e-12))
print("limits: b->0 net=%.3e ; b->inf net=%.6e (near side alone)" % (-k9 * L9 * 1e-9 / (d9 * (d9 + 1e-9)), -k9 * L9 / d9))
print("page 12.9: B near %.0e T, far %.2e T (+y); mu0 I1 I2/2pi = %.0e N; F_near %.0e N (x); F_far %.2e N (x); F_top %.2e N (z), F_bot %.2e N (z); mu0 I1 I2 L/2pi = %.0e N m; 1/d-1/(d+b) = %.1f 1/m; net %.2e N (x); on wire %+.2e N (x)" %
      (mu0 * I1 / (2 * np.pi * d9), mu0 * I1 / (2 * np.pi * (d9 + b9)), k9, F_near[0], F_far[0], F_top[2], F_bot[2], k9 * L9, 1 / d9 - 1 / (d9 + b9), Fnet[0], F_wire[0]))

# ============================================================================= 12.10
print("\n=== 12.10 Two crossing line currents (Summer 2020 HE2 #2a style)")
Iz, Ix = 4.0, 2.0                        # 4 A along +z on the z axis; 2 A along -x on the x axis
B1 = lambda Pt: bs_line(Pt, O, Z, Iz)
B2 = lambda Pt: bs_line(Pt, O, -X, Ix)
P = np.array([2.0, 0.0, 1.0])
b1, b2 = B1(P), B2(P)
print("at P=(2,0,1): z-wire r=2, r^=x, phi^ = z x x =", vec(np.cross(Z, X)), "; x-wire r=1, r^=z, phi^ = (-x) x z =", vec(np.cross(-X, Z)))
print("B(z-wire) =", vec(b1), " B(x-wire) =", vec(b2), " total =", vec(b1 + b2), "T ; 2 mu0/pi = %.6e" % (2 * mu0 / np.pi))
print("mu0/pi = %.6e" % (mu0 / np.pi))


def B_closed(Pt):
    x, y, z = Pt
    return (2 * mu0 / np.pi) * np.array([-y, x, 0]) / (x * x + y * y) + (mu0 / np.pi) * np.array([0, z, -y]) / (y * y + z * z)


Q = np.array([0.7, -1.3, 0.4])
print("closed-form general B vs quadrature at", vec(Q, "{:+.1f}"), ":", close(B1(Q) + B2(Q), B_closed(Q)))
for Pt in [[2, 0, -1], [-2, 0, 1], [4, 0, -2], [-1, 0, 0.5]]:
    Bt = B1(Pt) + B2(Pt)
    print("candidate null", vec(Pt, "{:+.1f}"), " |B| = %.3e T (scale mu0/pi = %.1e)" % (np.linalg.norm(Bt), mu0 / np.pi))
for Pt in [[2, 0.1, -1], [2, 0, -1.1], [2, 0, 1]]:
    print("non-null check", vec(Pt, "{:+.1f}"), " B =", vec(B1(Pt) + B2(Pt)))
zroot = brentq(lambda z: (B1([2, 0, z]) + B2([2, 0, z]))[1], -5, -0.01)
print("on x=2, y=0: B_y=0 at z = %.9f (expected -1); for z>0 B_y > 0 everywhere:" % zroot,
      all((B1([2, 0, z]) + B2([2, 0, z]))[1] > 0 for z in [0.1, 0.5, 1, 3, 10]))
vp = 1e5 * X
Fp = e * np.cross(vp, b1 + b2)
print("proton F = e v x B =", vec(Fp), "N ; v x B =", vec(np.cross(vp, b1 + b2)), "V/m")
print("E for zero force = -v x B =", vec(-np.cross(vp, b1 + b2)), "V/m ; |E|/|B| = %.6e m/s" % (np.linalg.norm(np.cross(vp, b1 + b2)) / np.linalg.norm(b1 + b2)))
print("page 12.10: z wire %.0e T (+y), x wire %.0e T (+y), total %.0e T (+y); F = %.2e N (+z); v x B = %.2f V/m (+z); E = %.2f V/m (z); |B| at (2,0,-1) and (-2,0,1): %.0e, %.0e T" %
      (b1[1], b2[1], (b1 + b2)[1], Fp[2], np.cross(vp, b1 + b2)[2], -np.cross(vp, b1 + b2)[2],
       np.linalg.norm(B1([2, 0, -1]) + B2([2, 0, -1])), np.linalg.norm(B1([-2, 0, 1]) + B2([-2, 0, 1]))))

# ============================================================================= 12.11
print("\n=== 12.11 A coax with unequal currents")
a, b, c, I1, I2 = 1e-3, 2e-3, 6e-3, 3.0, 8.0
J1 = I1 / (np.pi * a**2)
J2 = -I2 / (np.pi * (c**2 - b**2))
print("J1 = %.6e A/m^2 (+z) ; J2 = %.6e A/m^2 (z-component)" % (J1, J2))


def Jz11(rr):
    if rr < a:
        return J1
    if b < rr < c:
        return J2
    return 0.0


def Ienc11(rr):
    tot = 0.0
    edges = [0, a, b, c, np.inf]
    for lo, hi in zip(edges[:-1], edges[1:]):
        if rr <= lo:
            break
        top = min(rr, hi)
        tot += dblquad(lambda rp, ph: Jz11(rp) * rp, 0, 2 * np.pi, lo, top, epsabs=1e-13, epsrel=1e-12)[0]
    return tot


def H11(rr):
    if rr < a:
        return I1 * rr / (2 * np.pi * a**2)
    if rr < b:
        return I1 / (2 * np.pi * rr)
    if rr < c:
        return (I1 - I2 * (rr**2 - b**2) / (c**2 - b**2)) / (2 * np.pi * rr)
    return (I1 - I2) / (2 * np.pi * rr)


for rr in [0.5e-3, 1e-3, 1.5e-3, 2e-3, 3e-3, 4e-3, 5e-3, 6e-3, 10e-3]:
    Hn = Ienc11(rr) / (2 * np.pi * rr)
    print("r = %4.1f mm: I_enc = %+.6f A, H_phi = %+10.4f A/m ; formula %+10.4f %s" % (rr * 1e3, Ienc11(rr), Hn, H11(rr), close(Hn, H11(rr), atol=1e-9)))
r0 = brentq(Ienc11, b * 1.0001, c * 0.9999)
print("zero of I_enc in the outer conductor: r0 = %.9f mm ; sqrt(b^2 + (I1/I2)(c^2-b^2)) = %.9f mm" %
      (r0 * 1e3, np.sqrt(b**2 + (I1 / I2) * (c**2 - b**2)) * 1e3))
print("(r0^2-b^2)/(c^2-b^2) = %.6f = I1/I2 = %.6f" % ((r0**2 - b**2) / (c**2 - b**2), I1 / I2))
for rr in [a, b, c]:
    print("continuity at r = %.0f mm: left %.6f right %.6f" % (rr * 1e3, H11(rr * (1 - 1e-12)), H11(rr * (1 + 1e-12))))
for rr in [3e-3, 5e-3]:
    dh = 1e-9
    curlz = ((rr + dh) * H11(rr + dh) - (rr - dh) * H11(rr - dh)) / (2 * dh) / rr
    print("curl check r=%.0f mm: (1/r)d(r H)/dr = %.6e ; J2 = %.6e %s" % (rr * 1e3, curlz, J2, close(curlz, J2, rtol=1e-5)))
print("outside: I1 - I2 = %.1f A -> H along -phi^ ; values 1500/pi=%.4f 750/pi=%.4f 1250/(3pi)=%.4f 250/pi=%.4f" %
      (I1 - I2, 1500 / np.pi, 750 / np.pi, 1250 / (3 * np.pi), 250 / np.pi))
# brute-force direction at (10 mm, 0): superpose line currents numerically over the cross-section
P11 = np.array([10e-3, 0.0, 0.0])


def H_brute(Pt):
    out = np.zeros(3)
    for lo, hi, Jv in [(0, a, J1), (b, c, J2)]:
        for k in range(2):
            fk = lambda rp, ph, k=k: (Jv / (2 * np.pi)) * np.cross(Z, (Pt - np.array([rp * np.cos(ph), rp * np.sin(ph), 0])))[k] / \
                np.sum((Pt - np.array([rp * np.cos(ph), rp * np.sin(ph), 0]))**2) * rp
            out[k] += dblquad(fk, 0, 2 * np.pi, lo, hi, epsabs=1e-10, epsrel=1e-10)[0]
    return out


print("H at (10 mm,0,0) by 2-D superposition of line currents =", vec(H_brute(P11)), "A/m ; -phi^ there = -y")
print("page 12.11: J1 = %.2e, J2 = %.2e A/m^2; (r mm: I_enc A / H_phi A/m) %s; H at r=a,b,c: %.1f, %.1f, %.1f A/m; r0^2 = %.0f mm^2, r0 = %.0f mm; outside I_enc = %.0f A; b^2 = %.0f, c^2 = %.0f, c^2-b^2 = %.0f, (3 mm)^2 = %.0f mm^2; I1/I2 = 3/8 = %.3f" %
      (J1, J2, ", ".join("%g: %.2f / %.1f" % (rr * 1e3, Ienc11(rr), H11(rr)) for rr in [0.5e-3, 1.5e-3, 3e-3, 5e-3, 10e-3]),
       H11(a), H11(b), H11(c), (r0 * 1e3)**2, r0 * 1e3, I1 - I2, (b * 1e3)**2, (c * 1e3)**2, (c * 1e3)**2 - (b * 1e3)**2, 3.0**2, I1 / I2))

# ============================================================================= 12.12
print("\n=== 12.12 A wire with an off-axis hole")
a, b, d, I = 0.03, 0.01, 0.015, 40.0
J = I / (np.pi * (a**2 - b**2))
print("J = I/(pi(a^2-b^2)) = %.6f A/m^2 ; 5e4/pi = %.6f" % (J, 5e4 / np.pi))
print("currents of the superposed cylinders: J pi a^2 = %.6f A, J pi b^2 = %.6f A" % (J * np.pi * a**2, J * np.pi * b**2))


def H_metal(Pt, C):
    """H at Pt (in the plane z=0) from the metal = disk(radius a, centre 0) minus hole(radius b, centre C),
    by 2-D superposition of infinite line currents J dA (each verified as mu0 I/2 pi r by Biot-Savart above),
    integrated in polar coordinates about the hole centre C: rho from b to the outer circle."""
    Pt = np.asarray(Pt, float)
    C = np.asarray(C, float)

    def rho_out(th):
        s = np.array([np.cos(th), np.sin(th), 0.0])
        cs = np.dot(C, s)
        return -cs + np.sqrt(cs**2 - np.dot(C, C) + a**2)

    res = np.zeros(3)
    for k in range(2):
        def fk(rho, th, k=k):
            Qp = C + rho * np.array([np.cos(th), np.sin(th), 0.0])
            Rv = Pt - Qp
            return (J / (2 * np.pi)) * np.cross(Z, Rv)[k] / np.dot(Rv, Rv) * rho
        res[k] = dblquad(fk, 0, 2 * np.pi, lambda th: b, rho_out, epsabs=1e-9, epsrel=1e-10)[0]
    return res


C = np.array([d, 0.0, 0.0])
Hhole = 0.5 * J * np.cross(Z, C)
print("vector form (1/2) J z^ x d =", vec(Hhole), "A/m ; magnitude J d/2 = %.6f = 375/pi = %.6f" % (J * d / 2, 375 / np.pi))
print("B in hole = mu0 H = %.6e T" % (mu0 * J * d / 2))
for Pt in [[0.015, 0, 0], [0.015, 0.006, 0], [0.021, -0.003, 0], [0.008, 0.004, 0]]:
    Hn = H_metal(Pt, C)
    print("hole point", vec(Pt, "{:+.3f}"), ": H (2-D brute force) =", vec(Hn), close(Hn, Hhole, rtol=1e-6, atol=1e-6))
print("concentric hole (d=0): H at (4 mm, 3 mm) =", vec(H_metal([0.004, 0.003, 0], O)), "A/m (expected 0)")
rr = 0.02
Ienc_conc = dblquad(lambda rp, ph: J * rp, 0, 2 * np.pi, b, rr)[0]
print("concentric, metal r=2 cm: I_enc = %.6f A ; J pi (r^2-b^2) = %.6f ; H = %.6f ; J(r^2-b^2)/(2r) = %.6f" %
      (Ienc_conc, J * np.pi * (rr**2 - b**2), Ienc_conc / (2 * np.pi * rr), J * (rr**2 - b**2) / (2 * rr)))
print("concentric, at r = a: J(a^2-b^2)/(2a) = %.6f = I/(2 pi a) = %.6f" % (J * (a**2 - b**2) / (2 * a), I / (2 * np.pi * a)))
P12 = np.array([0.06, 0.0, 0.0])
Hn = H_metal(P12, C)
Hbig = (J * np.pi * a**2) / (2 * np.pi * 0.06) * np.cross(Z, X)
Hsmall = -(J * np.pi * b**2) / (2 * np.pi * (0.06 - d)) * np.cross(Z, X)
print("at (6 cm, 0): brute force H =", vec(Hn), " ; big", vec(Hbig), "+ hole", vec(Hsmall), "=", vec(Hbig + Hsmall), close(Hn, Hbig + Hsmall, rtol=1e-6, atol=1e-6))
print("centred 40 A line at 6 cm: I/(2 pi r) = %.6f A/m ; ratio %.6f" % (I / (2 * np.pi * 0.06), (Hbig + Hsmall)[1] / (I / (2 * np.pi * 0.06))))


def H_two_lines(Pt):
    return wire_formula(Pt, O, Z, J * np.pi * a**2) / mu0 + wire_formula(Pt, C, Z, -J * np.pi * b**2) / mu0


circ = quad(lambda t: np.dot(H_two_lines(0.06 * np.array([np.cos(t), np.sin(t), 0])), 0.06 * np.array([-np.sin(t), np.cos(t), 0])), 0, 2 * np.pi, limit=200)[0]
Hmag = [np.linalg.norm(H_two_lines(0.06 * np.array([np.cos(t), np.sin(t), 0]))) for t in np.linspace(0, 2 * np.pi, 7)]
print("circulation around r = 6 cm = %.6f A (= I) while |H| on it varies %.3f .. %.3f A/m" % (circ, min(Hmag), max(Hmag)))
print("page 12.12: a^2-b^2 = %.0e m^2; J = %.2e A/m^2; pieces %.0f A and %.0f A; hole H = %.1f A/m (+y), B = %.1e T (+y); concentric: I_enc(2 cm) = %.0f A, H = %.1f A/m, at r=a %.1f A/m; at (6 cm,0,0): %.1f - %.1f = %.1f A/m (+y), centred line %.1f A/m, ratio %.3f; |H| on r = 6 cm %.1f..%.1f A/m; circulation %.0f A; hole axis to (6 cm,0,0) = %.3f m" %
      (a**2 - b**2, J, J * np.pi * a**2, J * np.pi * b**2, Hhole[1], mu0 * Hhole[1], Ienc_conc, Ienc_conc / (2 * np.pi * rr), I / (2 * np.pi * a),
       Hbig[1], -Hsmall[1], Hn[1], I / (2 * np.pi * 0.06), Hn[1] / (I / (2 * np.pi * 0.06)), min(Hmag), max(Hmag), circ, 0.06 - d))
print("\nAll checks printed.")
