#!/usr/bin/env python3
"""Verification of every number, sign and direction on
content-src/practice/13-current-sheets-solenoids-and-vector-potential.md

numpy/scipy only.  Methods:
  * sheet fields by explicit np.cross(J_s, n_hat)/2, cross-checked by integrating
    infinite-filament fields across a (very wide) sheet;
  * slab profiles by superposing sheets and by a finite-difference curl;
  * curls/divergences/Laplacians of given A by central finite differences;
  * loop / Helmholtz / solenoid / toroid fields by numerical Biot-Savart
    on discretised polygons.
"""
import numpy as np
from scipy import integrate, optimize

mu0 = 4 * np.pi * 1e-7
X, Y, Z = np.eye(3)
np.set_printoptions(precision=6, suppress=True)


def hdr(s):
    print("\n" + "=" * 78 + "\n" + s + "\n" + "=" * 78)


def vec(v, unit="A/m", nd=4):
    v = np.asarray(v, float)
    v = np.where(np.abs(v) < 1e-12 * max(1.0, np.abs(v).max()), 0.0, v)
    return "(" + ", ".join(f"{c:.{nd}g}" for c in v) + ") " + unit


def sheet_H(Js, nhat):
    """H = 1/2 J_s x n_hat, n_hat from the sheet toward the field point."""
    return 0.5 * np.cross(np.asarray(Js, float), np.asarray(nhat, float))


def sheet_H_point(Js, p0, normal, r):
    """Sheet through p0 with unit normal `normal`; field point r."""
    side = np.sign(np.dot(np.asarray(r, float) - p0, normal))
    return sheet_H(Js, side * np.asarray(normal, float))


def sheet_H_bruteforce(Js, p0, normal, r, L=1e7):
    """Integrate infinite-filament fields H = dI/(2 pi rho) (j x rho_hat) across a sheet
    of half-width L (filaments at transverse coordinate s in [-L, L] measured from p0).
    The offset u = s0 - s from the field point's foot is substituted u = |h| sinh t,
    which turns the sharply peaked integrand into a smooth one."""
    Js = np.asarray(Js, float); normal = np.asarray(normal, float)
    K = np.linalg.norm(Js); jh = Js / K
    th = np.cross(jh, normal)                     # in-plane unit vector transverse to the current
    d = np.asarray(r, float) - np.asarray(p0, float)
    h = d @ normal; s0 = d @ th
    ah = abs(h)
    t_lo, t_hi = np.arcsinh((s0 - L) / ah), np.arcsinh((s0 + L) / ah)
    def comp(e):
        # rho = h n + u t ; integrand (j x rho)/|rho|^2 du = (j x (h n + u t)) |h| cosh t /(h^2 cosh^2 t) dt
        f = lambda t: (np.cross(jh, h * normal + ah * np.sinh(t) * th) @ e) / (ah * np.cosh(t))
        val, _ = integrate.quad(f, t_lo, t_hi, limit=400)
        return K / (2 * np.pi) * val            # H = B/mu0
    return np.array([comp(X), comp(Y), comp(Z)])


def curl_fd(F, r, h=1e-6):
    r = np.asarray(r, float)
    J = np.zeros((3, 3))
    for j in range(3):
        e = np.zeros(3); e[j] = h
        J[:, j] = (F(r + e) - F(r - e)) / (2 * h)   # J[i,j] = dF_i/dx_j
    return np.array([J[2, 1] - J[1, 2], J[0, 2] - J[2, 0], J[1, 0] - J[0, 1]])


def div_fd(F, r, h=1e-6):
    r = np.asarray(r, float)
    s = 0.0
    for j in range(3):
        e = np.zeros(3); e[j] = h
        s += (F(r + e)[j] - F(r - e)[j]) / (2 * h)
    return s


def lap_fd_scalar(f, r, h=1e-4):
    r = np.asarray(r, float)
    s = 0.0
    for j in range(3):
        e = np.zeros(3); e[j] = h
        s += (f(r + e) - 2 * f(r) + f(r - e)) / h ** 2
    return s


def bs_polyline(P, I, r):
    """Biot-Savart B (tesla) at point r from closed polygon P (M x 3), current I,
    midpoint rule on each straight segment: dB = mu0 I dl x R / (4 pi R^3)."""
    P1 = np.roll(P, -1, axis=0)
    dl = P1 - P
    mid = 0.5 * (P + P1)
    R = np.asarray(r, float) - mid
    Rn = np.linalg.norm(R, axis=1)
    return mu0 * I / (4 * np.pi) * np.sum(np.cross(dl, R) / Rn[:, None] ** 3, axis=0)


def ring(a, z0, M=4000):
    t = np.linspace(0, 2 * np.pi, M, endpoint=False)          # counter-clockwise seen from +z
    return np.column_stack([a * np.cos(t), a * np.sin(t), np.full(M, z0)])


def bs_rings(a, zlist, I, r, M=2000):
    """sum of rings (all counter-clockwise from +z) of radius a at heights zlist."""
    t = np.linspace(0, 2 * np.pi, M, endpoint=False)
    c, s = np.cos(t), np.sin(t)
    dphi = 2 * np.pi / M
    B = np.zeros(3)
    r = np.asarray(r, float)
    for z0 in zlist:
        P = np.column_stack([a * c, a * s, np.full(M, z0)])
        dl = np.column_stack([-a * s, a * c, np.zeros(M)]) * dphi   # exact tangent * dphi
        R = r - P
        Rn = np.linalg.norm(R, axis=1)
        B += mu0 * I / (4 * np.pi) * np.sum(np.cross(dl, R) / Rn[:, None] ** 3, axis=0)
    return B


def loop_axis(N, I, a, z):
    return mu0 * N * I * a ** 2 / (2 * (a ** 2 + z ** 2) ** 1.5)


# =============================================================================
hdr("13.1  One sheet on z = 0")
Js = np.array([0, 8.0, 0])
p0 = np.zeros(3)
P1 = np.array([0, 0, 0.5]); P2 = np.array([3, -2, -40.0])
H1 = sheet_H_point(Js, p0, Z, P1); H2 = sheet_H_point(Js, p0, Z, P2)
print("H(P1) =", vec(H1), "  brute force:", vec(sheet_H_bruteforce(Js, p0, Z, P1)))
print("H(P2) =", vec(H2), "  brute force:", vec(sheet_H_bruteforce(Js, p0, Z, P2)))
print(f"B(P1) = mu0*H = {mu0*H1[0]:.4e} T along x  (= {mu0*H1[0]*1e6:.3f} uT); 4*mu0 = {4*mu0:.4e}")
print(f"B(P2) = {mu0*H2[0]:.4e} T along x")
Jsb = np.array([6.0, 8.0, 0])
Hb = sheet_H(Jsb, Z)
print("(b) H above =", vec(Hb), " |H| =", np.linalg.norm(Hb), " |Js|/2 =", np.linalg.norm(Jsb) / 2,
      " H.Js =", Hb @ Jsb)
print("    H below =", vec(sheet_H(Jsb, -Z)))
print("    brute force above at (1,2,0.3):", vec(sheet_H_bruteforce(Jsb, p0, Z, [1, 2, 0.3])))
print("    x^ cross z^ =", np.cross(X, Z), " y^ cross z^ =", np.cross(Y, Z))

# =============================================================================
hdr("13.2  MC: H_t jump at a sheet on x = 0 with a normal component")
Js = np.array([0, 0, 3.0]); n = X
H2 = np.array([2.0, -1.0, 0])
H1 = H2 + np.cross(Js, n)        # (H1-H2)_t = Js x n ; normal part continuous
print("Js x n =", vec(np.cross(Js, n)))
print("correct H1 (x>0) =", vec(H1), "  check n x (H1-H2) =", vec(np.cross(n, H1 - H2)), " = Js?",
      np.allclose(np.cross(n, H1 - H2), Js))
print("second route: sheet self-field x<0:", vec(sheet_H(Js, -X)), " x>0:", vec(sheet_H(Js, X)))
Hext = H2 - sheet_H(Js, -X)
print("  external (continuous) field =", vec(Hext), " -> H1 =", vec(Hext + sheet_H(Js, X)))
print("distractors:")
print("  (a) n x Js used:", vec(H2 + np.cross(n, Js)))
print("  (c) jump added to normal comp: (2+3, -1, 0) =", vec(H2 + 3 * X))
print("  (d) Js added:", vec(H2 + Js))
print("  (e) half jump:", vec(H2 + 0.5 * np.cross(Js, n)), " (= external field)")
print("  (f) normal flipped:", vec(np.array([-2.0, 2.0, 0])))
for lab, Hc in [("a", H2 + np.cross(n, Js)), ("c", H2 + 3 * X), ("d", H2 + Js),
                ("e", H2 + 0.5 * np.cross(Js, n)), ("f", np.array([-2.0, 2, 0]))]:
    print(f"  ({lab}) n x (H1-H2) = {vec(np.cross(n, Hc - H2))};  normal comp continuous: {np.isclose(Hc[0], H2[0])}")

# =============================================================================
hdr("13.3  Solenoid, flux, nested solenoid")
n1, I1, a1 = 2000.0, 0.5, 0.02
n2, a2 = 400.0, 0.01
H0 = n1 * I1
B0 = mu0 * H0
print(f"H inside = n1 I1 = {H0:.1f} A/m ; B = {B0:.5e} T (4 pi e-4 = {4*np.pi*1e-4:.5e})")
Psi = B0 * np.pi * a1 ** 2
print(f"Psi through cross-section = {Psi:.5e} Wb ; 16 pi^2 e-8 = {16*np.pi**2*1e-8:.5e}")
I2 = -n1 * I1 / n2
print(f"I2 = -n1 I1 / n2 = {I2:.3f} A  (negative = clockwise seen from +z)")
Psi_ann = B0 * np.pi * (a1 ** 2 - a2 ** 2)
print(f"annulus H = {H0:.0f} A/m ; flux through r<=2 cm = {Psi_ann:.5e} Wb ; 12 pi^2 e-8 = {12*np.pi**2*1e-8:.5e}")
# H_t jump at r = a2: n = r_hat (from core into annulus); J_s(inner) = n2 I2 phi_hat
r_hat, phi_hat = X, Y        # at the point (a2, 0, 0)
print("jump at r=a2: r^ x (H_ann - H_core) =", vec(np.cross(r_hat, H0 * Z - 0 * Z)),
      " ; inner winding n2 I2 phi^ =", vec(n2 * I2 * phi_hat))
# numerical Biot-Savart: long finite solenoids as ring stacks (length 2 m, ring spacing 1/n)
Lsol = 2.0
z1 = np.arange(-Lsol / 2 + 0.5 / n1, Lsol / 2, 1 / n1)
z2 = np.arange(-Lsol / 2 + 0.5 / n2, Lsol / 2, 1 / n2)
Bc1 = bs_rings(a1, z1, I1, [0, 0, 0.00025], M=400)
print(f"BS outer alone at centre: Bz = {Bc1[2]:.5e} T  (mu0 n1 I1 = {B0:.5e}; ratio {Bc1[2]/B0:.5f})")
Bc2 = bs_rings(a2, z2, I2, [0, 0, 0.00025], M=400)
print(f"BS inner alone at centre: Bz = {Bc2[2]:.5e} T ; sum = {Bc1[2]+Bc2[2]:.3e} T (should be ~0)")
pt = [0.015, 0, 0.00025]
Bann = bs_rings(a1, z1, I1, pt, M=400) + bs_rings(a2, z2, I2, pt, M=400)
print(f"BS both at r = 1.5 cm: B = {vec(Bann,'T')} ; H = {Bann[2]/mu0:.1f} A/m (expect {H0:.0f})")
pt = [0.03, 0, 0.00025]
Bout = bs_rings(a1, z1, I1, pt, M=400) + bs_rings(a2, z2, I2, pt, M=400)
print(f"BS both at r = 3 cm (outside): H = {Bout[2]/mu0:.2f} A/m (expect ~0; finite-length leakage)")

# =============================================================================
hdr("13.4  Toroid, rectangular cross-section")
N, I, a, b, h = 600, 2.0, 0.04, 0.06, 0.02
for r in [0.04, 0.05, 0.06]:
    Hr = N * I / (2 * np.pi * r)
    print(f"r = {r*100:.0f} cm: H = NI/(2 pi r) = {Hr:.2f} A/m ; B = {mu0*Hr*1e3:.4f} mT")
print(f"B(a)/B(b) = {b/a:.3f}")
print(f"mu0/(2pi) = {mu0/(2*np.pi):.3e} ; mu0 N I/(2 pi) = {mu0*N*I/(2*np.pi):.3e} T m")


def toroid_points(N, a, b, h, nseg=40):
    """N rectangular turns; at angle phi_k: up the inner wall (r=a, +z), out along the
    top (z=+h/2), down the outer wall (r=b), back in along the bottom."""
    polys = []
    for k in range(N):
        ph = 2 * np.pi * (k + 0.5) / N
        u = np.array([np.cos(ph), np.sin(ph), 0.0])
        s = np.linspace(0, 1, nseg, endpoint=False)
        side1 = np.array([a * u + (-h / 2 + h * t) * Z for t in s])           # up at r=a
        side2 = np.array([(a + (b - a) * t) * u + (h / 2) * Z for t in s])    # out on top
        side3 = np.array([b * u + (h / 2 - h * t) * Z for t in s])            # down at r=b
        side4 = np.array([(b - (b - a) * t) * u - (h / 2) * Z for t in s])    # in on bottom
        polys.append(np.vstack([side1, side2, side3, side4]))
    return polys


polys = toroid_points(N, a, b, h, nseg=30)
for r in [0.03, 0.045, 0.05, 0.055, 0.07]:
    pt = np.array([r, 0.0, 0.0])
    B = sum(bs_polyline(P, I, pt) for P in polys)
    Hexp = N * I / (2 * np.pi * r) if a < r < b else 0.0
    print(f"BS toroid at r = {r*100:.1f} cm: H = {vec(B/mu0)} ; expected H_phi = {Hexp:.2f} (phi^ = +y here)")

# =============================================================================
hdr("13.5  True/false checks")
K = 6.0
for d in [1.0, 2.0]:
    print(f"(i) sheet K={K}: brute-force |H| at {d} m = {np.linalg.norm(sheet_H_bruteforce([0,K,0],np.zeros(3),Z,[0,0,d])):.6f} A/m")
n_, I_ = 1000.0, 1.0
for aa in [0.01, 0.02]:
    Lc = 4.0
    Bcen = mu0 * n_ * I_ * (Lc / 2) / np.sqrt((Lc / 2) ** 2 + aa ** 2)
    print(f"(ii) solenoid length 4 m, radius {aa*100:.0f} cm: B centre = {Bcen:.6e} T ; flux = {Bcen*np.pi*aa**2:.4e} Wb")
print("(iii) sheet self-field is tangential: 1/2 Js x n . n =", sheet_H([3, 4, 0], Z) @ Z)
B0t = 0.7
A1 = lambda r: 0.5 * B0t * np.array([-r[1], r[0], 0.0])
A2 = lambda r: B0t * np.array([0.0, r[0], 0.0])
for r in [np.array([0.3, -1.2, 2.0]), np.array([-2.0, 0.5, -0.7])]:
    print(f"(iv) curl A1 = {vec(curl_fd(A1, r),'T')} ; curl A2 = {vec(curl_fd(A2, r),'T')} ; div A1 = {div_fd(A1,r):.1e}, div A2 = {div_fd(A2,r):.1e}")
    lam = lambda q: 0.5 * B0t * q[0] * q[1]
    gl = np.array([(lam(r + e * 1e-6) - lam(r - e * 1e-6)) / 2e-6 for e in np.eye(3)])
    print(f"     A2 - A1 = {vec(A2(r)-A1(r),'')} ; grad(B0 x y/2) = {vec(gl,'')}")
for zz in [2, 4, 8, 16]:
    Bz = bs_polyline(ring(1.0, 0.0, 4000), 1.0, [0, 0, zz])[2]
    print(f"(v) loop a=1, I=1: Bz({zz}) = {Bz:.6e} ; Bz z^3 = {Bz*zz**3:.6e} (mu0/2 = {mu0/2:.6e}); Bz z^2 = {Bz*zz**2:.3e}")

# =============================================================================
hdr("13.6  Find the error: parallel-plate line (plates y = 0 and y = d)")
I, w, d = 8.0, 0.04, 0.002
K = I / w
Jtop, Jbot = K * X, -K * X
print(f"K = I/w = {K:.1f} A/m")
# student's version: n = +y for both
Hs = sheet_H(Jtop, Y) + sheet_H(Jbot, Y)
print("student (n=+y for both): top", vec(sheet_H(Jtop, Y)), " bottom", vec(sheet_H(Jbot, Y)), " sum", vec(Hs))
Hbetween = sheet_H(Jtop, -Y) + sheet_H(Jbot, Y)
Habove = sheet_H(Jtop, Y) + sheet_H(Jbot, Y)
Hbelow = sheet_H(Jtop, -Y) + sheet_H(Jbot, -Y)
print("correct between:", vec(Hbetween), " top part", vec(sheet_H(Jtop, -Y)), " bottom part", vec(sheet_H(Jbot, Y)))
print("above:", vec(Habove), " below:", vec(Hbelow))
print(f"B between = {mu0*Hbetween[2]:.4e} T along z  ({mu0*K*1e6:.1f} uT magnitude)")
print("jump at top plate: y^ x (H_above - H_between) =", vec(np.cross(Y, Habove - Hbetween)), " J_top =", vec(Jtop))
print("brute-force (filament) between, top plate at y=d:",
      vec(sheet_H_bruteforce(Jtop, np.array([0, d, 0]), Y, [0, d / 2, 0]) +
          sheet_H_bruteforce(Jbot, np.zeros(3), Y, [0, d / 2, 0])))
# finite-width strips (width w in z, infinite in x): field at mid-gap
Bstrip = 2 * (mu0 * K / np.pi) * np.arctan(w / (2 * (d / 2)))
print(f"finite-width strips w={w}, d={d}: B mid-gap = {Bstrip:.4e} T = {Bstrip/(mu0*K):.4f} mu0 K (edge effect)")
# numerical check of the strip formula by quad over the width
f = lambda zp: (d / 2) / ((d / 2) ** 2 + zp ** 2)
val, _ = integrate.quad(f, -w / 2, w / 2)
print(f"   quad check: one strip B = mu0 K/(2pi) * {val:.6f} -> two strips {2*mu0*K/(2*np.pi)*val:.4e} T")
print(f"scaling d->2d, I->I/2: |B| factor = {(mu0*(I/2)/w)/(mu0*I/w):.2f}")

# =============================================================================
hdr("13.7  Graded slab J = J0 (x/d) z^, 0<x<d")
J0, d = 400.0, 0.05
Jz = lambda x: J0 * x / d if 0 < x < d else 0.0
Ktot = integrate.quad(Jz, 0, d)[0]
print(f"K = int J dx = {Ktot:.6f} A/m ; J0 d/2 = {J0*d/2}")
Hy_an = lambda x: (-J0 * d / 4 if x <= 0 else (J0 * x ** 2 / (2 * d) - J0 * d / 4 if x < d else J0 * d / 4))
# brute force: superpose sheets dK = J dx' : H_y(x) = 1/2 int J(x') sgn(x - x') dx'  (z^ x x^ = y^)
def Hy_bf(x):
    val, _ = integrate.quad(lambda xp: 0.5 * Jz(xp) * np.sign(x - xp), 0, d, points=[min(max(x, 0), d)], limit=200)
    return val
print("z^ x x^ =", np.cross(Z, X))
for x in [-0.02, 0.0, 0.0125, 0.025, d / np.sqrt(2), 0.04, d, 0.08]:
    print(f"x = {x*100:7.4f} cm: H_y analytic = {Hy_an(x):+.5f}  superposed sheets = {Hy_bf(x):+.5f} A/m")
x0 = optimize.brentq(Hy_an, 1e-6, d - 1e-6)
print(f"zero at x0 = {x0*100:.4f} cm ; d/sqrt2 = {d/np.sqrt(2)*100:.4f} cm")
print(f"current below x0 = {integrate.quad(Jz,0,x0)[0]:.4f}, above = {integrate.quad(Jz,x0,d)[0]:.4f} A/m")
for x in [0.01, 0.03, 0.045]:
    dHdx = (Hy_an(x + 1e-7) - Hy_an(x - 1e-7)) / 2e-7
    print(f"curl check x={x}: dHy/dx = {dHdx:.4f} ; J_z = {Jz(x):.4f}")
print(f"H_y = 4000 x^2 - 5 ? at x=0.025: {4000*0.025**2-5}")

# =============================================================================
hdr("13.8  Three sheets z=0,1,2 m with different directions")
Js1, Js2 = 4.0 * X, 6.0 * Y
Js3 = -(Js1 + Js2)
print("Js3 =", vec(Js3))
zs = [0.0, 1.0, 2.0]; Jss = [Js1, Js2, Js3]
def Htot(zp):
    return sum(sheet_H(J, np.sign(zp - z0) * Z) for J, z0 in zip(Jss, zs))
for zp in [-1.0, 0.5, 1.5, 3.0]:
    Ht = Htot(zp)
    bf = sum(sheet_H_bruteforce(J, np.array([0, 0, z0]), Z, [0.2, -0.3, zp]) for J, z0 in zip(Jss, zs))
    print(f"z = {zp:4.1f}: H = {vec(Ht)} |H| = {np.linalg.norm(Ht):.4f} ; brute force {vec(bf)}")
print(f"|H| in 1<z<2: sqrt(52) = {np.sqrt(52):.4f} ; B = {mu0*np.sqrt(52)*1e6:.3f} uT ; B(0<z<1) = {mu0*4*1e6:.3f} uT")
Hb = [Htot(-0.5), Htot(0.5), Htot(1.5), Htot(2.5)]
for k, (J, z0) in enumerate(zip(Jss, zs)):
    print(f"jump at z={z0}: z^ x (H_above - H_below) = {vec(np.cross(Z, Hb[k+1]-Hb[k]))} ; Js = {vec(J)}")
print("marching: H(0<z<1) = Js1 x z^ =", vec(np.cross(Js1, Z)), "; H(1<z<2) = (Js1+Js2) x z^ =", vec(np.cross(Js1 + Js2, Z)))

# =============================================================================
hdr("13.9  Two slabs (+ sheet) along y; slabs normal to z")
J1, z1a, z1b = 3.0, -3.0, -1.0
J2, z2a, z2b = -2.0, 0.0, 3.0
print("y^ x z^ =", np.cross(Y, Z), "(so a +y current gives +x field above, -x below)")
def Jy(zp, with_sheet=False):
    j = 0.0
    if z1a < zp < z1b: j += J1
    if z2a < zp < z2b: j += J2
    return j
def Hx_slabs(zp):
    # superposition of sheets dK = J dz': H = 1/2 int J(z') sgn(z - z') dz'  (x-component)
    tot = 0.0
    for (J, za, zb) in [(J1, z1a, z1b), (J2, z2a, z2b)]:
        val, _ = integrate.quad(lambda zz: 0.5 * J * np.sign(zp - zz), za, zb,
                                points=[min(max(zp, za), zb)], limit=200)
        tot += val
    return tot
def Hx_piece(zp):
    if zp < -3: return 0.0
    if zp < -1: return 3 * zp + 9
    if zp < 0: return 6.0
    if zp < 3: return 6 - 2 * zp
    return 0.0
print(f"K1 = {J1*(z1b-z1a)} A/m, K2 = {J2*(z2b-z2a)} A/m")
pts = [-4.0, -2.0, -0.5, 1.5, 4.0]
for zp in pts:
    print(f"z = {zp:5.1f}: Hx (sheets superposed) = {Hx_slabs(zp):+.5f} ; piecewise = {Hx_piece(zp):+.5f} A/m")
for zp in [-3, -1, 0, 3]:
    print(f"continuity at z={zp}: Hx(z-) = {Hx_slabs(zp-1e-9):+.6f}, Hx(z+) = {Hx_slabs(zp+1e-9):+.6f}")
for zp in [-2.5, -1.7, 0.7, 2.2]:
    dH = (Hx_piece(zp + 1e-6) - Hx_piece(zp - 1e-6)) / 2e-6
    print(f"curl check z={zp}: (curl H)_y = dHx/dz = {dH:+.4f} ; J_y = {Jy(zp):+.1f}")
Jsh = -2.0 * Y; zsh = 1.0
def Hx_all(zp):
    return Hx_slabs(zp) + sheet_H(Jsh, np.sign(zp - zsh) * Z)[0]
print("sheet field below z=1:", vec(sheet_H(Jsh, -Z)), " above:", vec(sheet_H(Jsh, Z)))
for zp in pts:
    print(f"with sheet: z = {zp:5.1f}: Hx = {Hx_all(zp):+.5f} A/m")
for (lo, hi) in [(-3, -1), (-1, 0), (0, 1), (1, 3)]:
    try:
        r0 = optimize.brentq(Hx_all, lo + 1e-9, hi - 1e-9)
        print(f"zero of Hx in ({lo},{hi}): z = {r0:.6f} m")
    except ValueError:
        print(f"no zero in ({lo},{hi})  [Hx ends: {Hx_all(lo+1e-9):+.3f}, {Hx_all(hi-1e-9):+.3f}]")
print(f"outside: Hx(z<-3) = {Hx_all(-5):+.3f}, Hx(z>3) = {Hx_all(5):+.3f}")
Hlo, Hhi = Hx_all(1 - 1e-9), Hx_all(1 + 1e-9)
print(f"jump at z=1: below {Hlo:+.4f}, above {Hhi:+.4f}; z^ x (Habove-Hbelow) x^ =",
      vec(np.cross(Z, (Hhi - Hlo) * X)), " Js =", vec(Jsh))
print("with sheet, the ramp 3z+10 in slab 1 would vanish at z =", -10 / 3, "(outside the slab -> no zero there)")
# (d) A = mu0 |z-1| y^
A = lambda r: np.array([0.0, mu0 * abs(r[2] - 1.0), 0.0])
for r in [np.array([0.4, -0.2, 2.3]), np.array([-1.0, 0.7, -0.6])]:
    B = curl_fd(A, r)
    print(f"(d) at z={r[2]}: div A = {div_fd(A, r):.2e} ; curl A = {vec(B,'T')} ; H = B/mu0 = {vec(B/mu0)}")
# J from the Laplacian: integrate d2A_y/dz2 across z=1  -> jump of dA_y/dz
dA_up = (A([0, 0, 1.2])[1] - A([0, 0, 1.1])[1]) / 0.1
dA_dn = (A([0, 0, 0.9])[1] - A([0, 0, 0.8])[1]) / 0.1
print(f"jump of dA_y/dz across z=1: {dA_up - dA_dn:.4e} = 2 mu0 ({2*mu0:.4e}) -> J_s,y = -(jump)/mu0 = {-(dA_up-dA_dn)/mu0:+.4f} A/m")
print("H_t jump from B = curl A:", vec(np.cross(Z, curl_fd(A, [0, 0, 1.5]) / mu0 - curl_fd(A, [0, 0, 0.5]) / mu0)))

# =============================================================================
hdr("13.10  Vector potentials of a wire and of a solenoid")
I = 10.0
r0 = 0.37   # arbitrary reference radius
Aw = lambda r: np.array([0.0, 0.0, mu0 * I / (2 * np.pi) * np.log(r0 / np.hypot(r[0], r[1]))])
for r in [np.array([0.03, 0.04, 0.0]), np.array([-0.02, 0.05, 0.3])]:
    B = curl_fd(Aw, r, h=1e-7)
    rr = np.hypot(r[0], r[1])
    phi = np.array([-r[1] / rr, r[0] / rr, 0])
    print(f"r = {r}: curl A = {vec(B*1e6,'uT')} ; mu0 I/(2 pi r) phi^ = {vec(mu0*I/(2*np.pi*rr)*phi*1e6,'uT')} ; div A = {div_fd(Aw,r):.1e}")
    print(f"   Laplacian of A_z (r>0) = {lap_fd_scalar(lambda q: Aw(q)[2], r):.2e}")
print(f"|B| at (3,4) cm = {mu0*I/(2*np.pi*0.05)*1e6:.3f} uT ; phi^ = (-0.8, 0.6, 0)")
# Laplacian of A_z integrated over a small disk = -mu0 I  (line source): flux of grad A_z through circle
for rc in [0.01, 0.2]:
    th = np.linspace(0, 2 * np.pi, 2001)[:-1]
    flux = 0.0
    for t in th:
        p = np.array([rc * np.cos(t), rc * np.sin(t), 0.0])
        e = np.array([np.cos(t), np.sin(t), 0.0])
        g = (Aw(p + 1e-7 * e)[2] - Aw(p - 1e-7 * e)[2]) / 2e-7
        flux += g * rc * (2 * np.pi / len(th))
    print(f"   circle r={rc}: closed-line integral of dA_z/dr = {flux:.6e} ; -mu0 I = {-mu0*I:.6e}")
a_, b_ = 0.01, 0.04
flux_A = Aw([a_, 0, 0])[2] - Aw([b_, 0, 0])[2]
flux_B = integrate.quad(lambda r: mu0 * I / (2 * np.pi * r), a_, b_)[0]
print(f"(b) flux per metre: A_z(a) - A_z(b) = {flux_A:.6e} Wb/m ; int B dr = {flux_B:.6e} ; (mu0 I/2pi) ln 4 = {mu0*I/(2*np.pi)*np.log(4):.6e}")
# loop integral of A around the rectangle x in [a,b], z in [0,1] at y=0, normal +y
def line_int(F, P, Q, n=2001):
    t = np.linspace(0, 1, n)
    pts = P[None, :] + t[:, None] * (Q - P)[None, :]
    vals = np.array([F(p) @ (Q - P) for p in pts])
    return integrate.simpson(vals, x=t)
corners = [np.array([a_, 0, 0.0]), np.array([a_, 0, 1.0]), np.array([b_, 0, 1.0]), np.array([b_, 0, 0.0])]
circ = sum(line_int(Aw, corners[k], corners[(k + 1) % 4]) for k in range(4))
print(f"   rectangle up at r=a, out, down at r=b, in: loop integral = {circ:.6e} Wb ; normal = z^ x x^ = {np.cross(Z, X)}")
# brute-force A of a long finite wire (Coulomb integral) -> differences independent of length
for Lw in [10.0, 1000.0]:
    Afin = lambda r: mu0 * I / (4 * np.pi) * 2 * np.arcsinh(Lw / r)
    print(f"   finite wire half-length {Lw}: A(a)-A(b) = {Afin(a_)-Afin(b_):.6e} ; A(a) itself = {Afin(a_):.4e} (grows with L)")
# solenoid
n, Isol, R = 1000.0, 2.0, 0.01
B0 = mu0 * n * Isol
print(f"(c) B0 = mu0 n I = {B0:.5e} T")
Ain = lambda r: 0.5 * np.cross(B0 * Z, r)
Aout = lambda r: 0.5 * B0 * R ** 2 * np.array([-r[1], r[0], 0.0]) / (r[0] ** 2 + r[1] ** 2)
for r in [np.array([0.004, -0.003, 0.2]), np.array([-0.006, 0.002, -1.0])]:
    print(f"   inside: curl A = {vec(curl_fd(Ain, r, h=1e-6),'T')} ; div A = {div_fd(Ain, r):.1e}")
for r in [np.array([0.015, 0.01, 0.0]), np.array([-0.03, -0.02, 0.5])]:
    print(f"   outside: curl A = {vec(curl_fd(Aout, r, h=1e-7),'T')} ; div A = {div_fd(Aout, r, h=1e-7):.1e}")
print(f"   A_phi(R) inside formula = {B0*R/2:.5e}, outside formula = {B0*R**2/(2*R):.5e} Wb/m (continuous)")
print(f"   A_phi(2R) = {B0*R**2/(2*2*R):.5e} Wb/m")
for rc in [0.02, 0.05]:
    th = np.linspace(0, 2 * np.pi, 4001)[:-1]
    tot = 0.0
    for t in th:
        p = np.array([rc * np.cos(t), rc * np.sin(t), 0.0])
        dlv = np.array([-np.sin(t), np.cos(t), 0.0]) * rc * (2 * np.pi / len(th))
        tot += Aout(p) @ dlv
    print(f"   loop integral of A at r = {rc}: {tot:.5e} Wb ; flux B0 pi R^2 = {B0*np.pi*R**2:.5e} Wb")
# brute-force A of a long finite solenoid from the Coulomb integral (rings, z'-integral analytic)
Lh = 200.0   # half-length
def Aphi_bf(r):
    f = lambda p: np.cos(p) * 2 * np.arcsinh(Lh / np.sqrt(r * r + R * R - 2 * r * R * np.cos(p)))
    val, _ = integrate.quad(f, -np.pi, np.pi, limit=400, points=[0.0])
    return mu0 * n * Isol * R / (4 * np.pi) * val
for r in [0.005, 0.01, 0.02, 0.04]:
    expect = B0 * r / 2 if r <= R else B0 * R ** 2 / (2 * r)
    print(f"   Coulomb-integral A_phi(r={r}) = {Aphi_bf(r):.5e} ; formula {expect:.5e}")

# =============================================================================
hdr("13.11  Loop on axis, Helmholtz pair, far field")
N, I, a = 50, 2.0, 0.20
P = ring(a, 0.0, 6000)
for zz in [0.0, 0.1, 0.3]:
    Bbs = N * bs_polyline(P, I, [0, 0, zz])
    print(f"single coil z = {zz}: BS = {vec(Bbs*1e3,'mT')} ; formula = {loop_axis(N,I,a,zz)*1e3:.6f} mT")
print(f"centre: mu0 N I/(2a) = {mu0*N*I/(2*a):.5e} T")
Pl, Pu = ring(a, -a / 2, 6000), ring(a, a / 2, 6000)
Bmid_bs = N * (bs_polyline(Pl, I, [0, 0, 0]) + bs_polyline(Pu, I, [0, 0, 0]))
Bmid = 2 * loop_axis(N, I, a, a / 2)
print(f"Helmholtz midpoint: BS = {vec(Bmid_bs*1e3,'mT')} ; formula = {Bmid:.6e} T ; (4/5)^1.5 mu0 N I / a = {(0.8**1.5)*mu0*N*I/a:.6e}")
print(f"(4/5)^1.5 = {0.8**1.5:.5f} ; 8/(5 sqrt5) = {8/(5*np.sqrt(5)):.5f} ; mu0 N I/a = {mu0*N*I/a:.5e}")
Bpair = lambda z: loop_axis(N, I, a, z - a / 2) + loop_axis(N, I, a, z + a / 2)
hh = 1e-4
d1 = (Bpair(hh) - Bpair(-hh)) / (2 * hh)
d2 = (Bpair(hh) - 2 * Bpair(0) + Bpair(-hh)) / hh ** 2
d2single = (loop_axis(N, I, a, hh) - 2 * loop_axis(N, I, a, 0) + loop_axis(N, I, a, -hh)) / hh ** 2
print(f"dB/dz at midpoint = {d1:.3e} ; d2B/dz2 = {d2:.3e} T/m^2 (single coil at its centre: {d2single:.3e})")
zz = np.linspace(0.05, 0.15, 3)
# second derivative of (a^2+z^2)^-1.5 vanishes at z = a/2
g = lambda z: (a * a + z * z) ** -1.5
for z0 in [a / 2, a / 3]:
    print(f"d2/dz2 (a^2+z^2)^-1.5 at z={z0:.4f}: FD {(g(z0+1e-5)-2*g(z0)+g(z0-1e-5))/1e-10:.4e} ; formula 3(4z^2-a^2)/(a^2+z^2)^3.5 = {3*(4*z0**2-a*a)/(a*a+z0*z0)**3.5:.4e}")
dz = 0.02
rel_pair = Bpair(dz) / Bpair(0) - 1
rel_single = loop_axis(N, I, a, dz) / loop_axis(N, I, a, 0) - 1
print(f"at 2 cm: pair B/B0 - 1 = {rel_pair:.4e} ({rel_pair*100:.4f} %), (144/125)(z/a)^4 = {144/125*(dz/a)**4:.4e}")
print(f"         single B/B0 - 1 = {rel_single:.4e} ({rel_single*100:.3f} %)")
Bbs2 = N * (bs_polyline(Pl, I, [0, 0, dz]) + bs_polyline(Pu, I, [0, 0, dz]))
print(f"         BS pair at z=2cm: {Bbs2[2]:.6e} vs formula {Bpair(dz):.6e}")
m = 2 * N * I * np.pi * a ** 2
print(f"m = 2 N I pi a^2 = {m:.4f} A m^2 (8 pi = {8*np.pi:.4f})")
for zf in [2.0, 4.0]:
    Bex = Bpair(zf)
    Bdip = mu0 * m / (2 * np.pi * zf ** 3)
    Bbs3 = N * (bs_polyline(Pl, I, [0, 0, zf]) + bs_polyline(Pu, I, [0, 0, zf]))
    print(f"z = {zf} m: exact {Bex:.6e} T (BS {Bbs3[2]:.6e}) ; dipole {Bdip:.6e} T ; ratio {Bex/Bdip:.6f}")
print(f"B(2 m)/B(4 m) = {Bpair(2.0)/Bpair(4.0):.5f} (2^3 = 8)")
print(f"single coil at z = 10a: exact/dipole = {loop_axis(1,1,1,10)/(mu0/(2*1000)):.5f}")
# 1/z^5 coefficient for pair vs spacing: B z^3/(mu0 N I a^2) - 1 ~ c (a/z)^2
for spacing in [a, 0.5 * a]:
    Bp = lambda z: loop_axis(N, I, a, z - spacing / 2) + loop_axis(N, I, a, z + spacing / 2)
    zf = 50 * a
    print(f"spacing {spacing/a:.1f}a: (B/Bdip - 1)*(z/a)^2 at z=50a = {(Bp(zf)/(mu0*m/(2*np.pi*zf**3))-1)*(zf/a)**2:.5f} (theory 1.5((s/a)^2-1) = {1.5*((spacing/a)**2-1):.3f})")

# =============================================================================
hdr("13.12  Finite solenoid on its axis")
ell, a, N, I = 0.30, 0.03, 600, 1.5
n = N / ell
B_inf = mu0 * n * I
def Bsol(z):
    return 0.5 * B_inf * ((z + ell / 2) / np.sqrt((z + ell / 2) ** 2 + a ** 2) - (z - ell / 2) / np.sqrt((z - ell / 2) ** 2 + a ** 2))
print(f"n = {n:.1f}/m ; mu0 n I = {B_inf:.5e} T")
Bc, Be = Bsol(0.0), Bsol(ell / 2)
print(f"centre: {Bc:.5e} T = {Bc/B_inf:.6f} mu0 n I ; 5/sqrt(26) = {5/np.sqrt(26):.6f}")
print(f"end:    {Be:.5e} T = {Be/B_inf:.6f} mu0 n I ; (1/2)10/sqrt(101) = {0.5*10/np.sqrt(101):.6f}")
print(f"end/centre = {Be/Bc:.5f}")
# numerical Biot-Savart: N rings evenly spaced
zr = -ell / 2 + (np.arange(N) + 0.5) * ell / N
for zp in [0.0, ell / 2, 0.1, 1.5]:
    Bbs = bs_rings(a, zr, I, [0, 0, zp], M=800)
    print(f"BS (600 rings) at z = {zp}: Bz = {Bbs[2]:.6e} T ; formula {Bsol(zp):.6e} T")
# integral of loop formula over z' (independent of the closed form)
for zp in [0.0, ell / 2]:
    val, _ = integrate.quad(lambda zq: loop_axis(n, I, a, zp - zq), -ell / 2, ell / 2)
    print(f"quad of n dz' loops at z={zp}: {val:.6e} T")
f = lambda L_over_a: (L_over_a / 2) / np.sqrt((L_over_a / 2) ** 2 + 1) - 0.99
Lmin = optimize.brentq(f, 1, 100)
print(f"centre within 1%: ell/a >= {Lmin:.4f} ; 1.98/sqrt(0.0199) = {1.98/np.sqrt(0.0199):.4f}")
m = N * I * np.pi * a ** 2
for zf in [1.5, 3.0]:
    Bd = mu0 * m / (2 * np.pi * zf ** 3)
    print(f"z = {zf}: exact {Bsol(zf):.5e} T ; dipole mu0 m/(2 pi z^3) = {Bd:.5e} T ; ratio {Bsol(zf)/Bd:.5f}")
print(f"m = N I pi a^2 = {m:.5f} A m^2 (0.81 pi = {0.81*np.pi:.5f})")
print(f"semi-infinite check: end of a very long solenoid -> {0.5*B_inf*1000/np.sqrt(1000**2+a**2)/B_inf:.6f} mu0 n I")

# =============================================================================
hdr("Page values: derived checks and numbers rounded exactly as quoted on the page")
# 13.1 tangential jump for J_s = (6, 8, 0)
Jsb = np.array([6.0, 8.0, 0]); Hup, Hdn = sheet_H(Jsb, Z), sheet_H(Jsb, -Z)
print("13.1  H_above - H_below =", vec(Hup - Hdn), "; z^ x (H_above - H_below) =", vec(np.cross(Z, Hup - Hdn)), "= J_s")
# 13.3 rounded values and the jump at the outer winding
n1, I1, a1, n2, a2 = 2000.0, 0.5, 0.02, 400.0, 0.01
B0 = mu0 * n1 * I1
print(f"13.3  B = {B0*1e3:.3f} mT ; Psi = {B0*np.pi*a1**2*1e6:.2f} uWb ; Psi(annulus) = {B0*np.pi*(a1**2-a2**2)*1e6:.2f} uWb")
print("13.3  jump at r = a1 (n = r^ = x^ at (a1,0,0)): r^ x (0 - H_ann) =", vec(np.cross(X, -n1 * I1 * Z)),
      "; n1 I1 phi^ =", vec(n1 * I1 * Y))
# 13.4 rounded H and the Biot-Savart residue outside the core
Nt, It = 600, 2.0
print("13.4  H(4, 5, 6 cm) =", ", ".join(f"{Nt*It/(2*np.pi*r):.0f}" for r in [0.04, 0.05, 0.06]), "A/m")
for r in [0.03, 0.07]:
    Bres = sum(bs_polyline(P, It, np.array([r, 0.0, 0.0])) for P in polys)
    print(f"13.4  BS residue at r = {r*100:.0f} cm: H_phi = {Bres[1]/mu0:.2f} A/m")
# 13.5 rounded values
for aa in [0.01, 0.02]:
    Bcen = mu0 * 1000.0 * 1.0 * 2.0 / np.sqrt(4.0 + aa ** 2)
    print(f"13.5(ii)  a = {aa*100:.0f} cm: B = {Bcen*1e3:.4f} mT ; flux = {Bcen*np.pi*aa**2*1e6:.3g} uWb")
print("13.5(v)  B_z z^3 x 1e7 at z = 2, 4, 8, 16 m:",
      ", ".join(f"{bs_polyline(ring(1.0, 0.0, 4000), 1.0, [0, 0, zz])[2]*zz**3*1e7:.4g}" for zz in [2, 4, 8, 16]),
      f"; mu0/2 x 1e7 = {mu0/2*1e7:.4g}")
# 13.6 edge-effect deficit of the strip model
Kpp, wpp, dpp = 200.0, 0.04, 0.002
ratio = (2 / np.pi) * np.arctan(wpp / dpp)
print(f"13.6  strip/sheet = {ratio:.4f} -> sheet model high by {(1-ratio)*100:.1f} % ; w/d = {wpp/dpp:.0f}")
# 13.8 sheet-by-sheet contributions
Jss8 = [4.0 * X, 6.0 * Y, -(4.0 * X + 6.0 * Y)]; zs8 = [0.0, 1.0, 2.0]
for zp in [0.5, 1.5]:
    parts = [sheet_H(J, np.sign(zp - z0) * Z) for J, z0 in zip(Jss8, zs8)]
    print(f"13.8  z = {zp}: sheet 1 {vec(parts[0])}, sheet 2 {vec(parts[1])}, sheet 3 {vec(parts[2])}, sum {vec(sum(parts))}")
print("13.8  marching jumps J_s x z^:", ", ".join(vec(np.cross(J, Z)) for J in Jss8))
# 13.9 each slab alone, outside, as an equivalent sheet
for lab, Kk in [("slab 1 (K=+6)", 6.0), ("slab 2 (K=-6)", -6.0)]:
    print(f"13.9  {lab}: below {vec(sheet_H(Kk*Y, -Z))}, above {vec(sheet_H(Kk*Y, Z))}")
print("13.9  slabs + sheet, H_x at z = -3, -1, 0, 1-, 1+, 3:",
      ", ".join(f"{Hx_all(zz):+.3f}" for zz in [-3 + 1e-9, -1, 1e-9, 1 - 1e-9, 1 + 1e-9, 3 - 1e-9]))
# 13.10 rounded values
print(f"13.10  mu0 I/(2 pi) = {mu0*10.0/(2*np.pi):.1e} T m ; flux = {mu0*10.0/(2*np.pi)*np.log(4)*1e6:.2f} uWb")
# 13.11 rounded values
print(f"13.11  m = 8 pi = {8*np.pi:.2f} A m^2")
# 13.12 rounded values
Bi12 = mu0 * 2000.0 * 1.5
print(f"13.12  mu0 n I = {Bi12*1e3:.3f} mT ; centre {Bsol(0.0)*1e3:.3f} mT ; end {Bsol(0.15)*1e3:.3f} mT ;"
      f" centre deficit {(1-Bsol(0.0)/Bi12)*100:.1f} % ; ell/a >= {Lmin:.2f} ; this coil ell/a = {0.30/0.03:.0f}")
print(f"13.12  far field from slices: mu0 N I a^2/(2 z^3) at z = 1.5 m = {mu0*600*1.5*0.03**2/(2*1.5**3):.5e} T")

print("\nALL CHECKS PRINTED.")
