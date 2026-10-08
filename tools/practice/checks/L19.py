#!/usr/bin/env python3
"""L19 practice checks: d'Alembert solutions and radiation from current sheets (numpy only).

Every number, sign and direction on practice/19-radiation-from-current-sheets.md is printed here.
For every sheet: E = -(eta/2) Js(t - d/v) on both sides, H = 1/2 Js(t - d/v) x n (n from the sheet
toward the field point), directions by np.cross; boundary conditions at the sheet (E_t continuous,
n x (H1 - H2) = Js); Faraday and Ampere-Maxwell by finite differences for every (E, H) pair.
"""
import numpy as np

eps0 = 8.8541878128e-12
mu0 = 4e-7 * np.pi
c = 2.99792458e8
eta0 = np.sqrt(mu0 / eps0)
e = 1.602176634e-19
X, Y, Z = np.eye(3)
cC, etaC = 3e8, 120 * np.pi          # course values used on the page
NAMES = {(1, 0, 0): "+x", (-1, 0, 0): "-x", (0, 1, 0): "+y", (0, -1, 0): "-y", (0, 0, 1): "+z", (0, 0, -1): "-z"}
ALL = []


def dname(v):
    v = np.asarray(v, float)
    if np.linalg.norm(v) == 0:
        return "0"
    n = v / np.linalg.norm(v)
    key = tuple(int(round(a)) for a in n)
    if np.allclose(n, key):
        return NAMES.get(key, str(key))
    return "(" + ", ".join(f"{a:+.4f}" for a in n) + ")"


def hdr(s):
    print("\n" + "=" * 78 + "\n" + s + "\n" + "=" * 78)


def jac(F, r, t, h):
    J = np.zeros((3, 3))
    for j in range(3):
        d = np.zeros(3); d[j] = h
        J[:, j] = (F(r + d, t) - F(r - d, t)) / (2 * h)
    return J


def curl(F, r, t, h):
    J = jac(F, r, t, h)
    return np.array([J[2, 1] - J[1, 2], J[0, 2] - J[2, 0], J[1, 0] - J[0, 1]])


def ddt(F, r, t, ht):
    return (F(r, t + ht) - F(r, t - ht)) / (2 * ht)


def rel(a, b):
    s = max(np.linalg.norm(a), np.linalg.norm(b), 1e-300)
    return np.linalg.norm(np.asarray(a) - np.asarray(b)) / s


def maxwell(label, E, H, mu, eps, pts, h, ht):
    rf = ra = dv = 0.0
    for (r, t) in pts:
        r = np.asarray(r, float)
        cE, dH = curl(E, r, t, h), -mu * ddt(H, r, t, ht)
        cH, dE = curl(H, r, t, h), eps * ddt(E, r, t, ht)
        rf = max(rf, rel(cE, dH)); ra = max(ra, rel(cH, dE))
        dv = max(dv, abs(np.trace(jac(E, r, t, h))) / max(np.linalg.norm(cE), 1e-300),
                 abs(np.trace(jac(H, r, t, h))) / max(np.linalg.norm(cH), 1e-300))
    ok = max(rf, ra) < 1e-4 and dv < 1e-5
    print(f"  [{label}] Faraday rel.res {rf:.1e} | Ampere-Maxwell {ra:.1e} | div/curl {dv:.1e} -> {'OK' if ok else 'FAIL'}")
    ALL.append(ok)
    return ok


def check(label, cond):
    print(f"  [{label}] {'OK' if cond else 'FAIL'}")
    ALL.append(bool(cond))


def sheet(p0, nvec, Jdir, g, mu, eps):
    """Sheet through point p0 with unit normal nvec; Js(t) = Jdir * g(t). Returns E(r,t), H(r,t)."""
    nvec = np.asarray(nvec, float) / np.linalg.norm(nvec)
    v, eta = 1 / np.sqrt(mu * eps), np.sqrt(mu / eps)

    def side(r):
        s = np.dot(np.asarray(r, float) - p0, nvec)
        return s, (nvec if s > 0 else -nvec)

    def E(r, t):
        s, n = side(r)
        return -eta / 2 * Jdir * g(t - abs(s) / v)

    def H(r, t):
        s, n = side(r)
        return 0.5 * np.cross(Jdir, n) * g(t - abs(s) / v)
    return E, H, v, eta


def bc(label, E, H, p0, nvec, Jdir, g, ts, delta=1e-9):
    nvec = np.asarray(nvec, float) / np.linalg.norm(nvec)
    ok = True
    for t in ts:
        r1, r2 = p0 + delta * nvec, p0 - delta * nvec
        Et1 = E(r1, t) - np.dot(E(r1, t), nvec) * nvec
        Et2 = E(r2, t) - np.dot(E(r2, t), nvec) * nvec
        jump = np.cross(nvec, H(r1, t) - H(r2, t))
        ok &= np.linalg.norm(Et1 - Et2) < 1e-4  # V/m, absolute (fields here are O(1..1000) V/m)
        ok &= np.allclose(jump, Jdir * g(t), atol=1e-6 * max(1, abs(g(t))))
    print(f"  [{label}] at the sheet: E_t continuous and n x (H1 - H2) = Js -> {'OK' if ok else 'FAIL'}")
    ALL.append(bool(ok))


def gauss(t0, w):
    return lambda t: np.exp(-((t - t0) / w) ** 2)


rng = np.random.default_rng(19)


def rpts(n, box, tmin, tmax, avoid=None):
    out = []
    while len(out) < n:
        r = rng.uniform(-box, box, 3)
        if avoid is not None and abs(avoid(r)) < 0.05 * box:
            continue
        out.append((r, rng.uniform(tmin, tmax)))
    return out


# =========================================================================================== 19.1
hdr("19.1 Which is a uniform plane TEM wave (multiple choice)")
f = gauss(0.0, 2e-9)
a = 1.0
cands = {
    "(a) E=z f(t-z/c), H=x f/eta0": (lambda r, t: Z * f(t - r[2] / c), lambda r, t: X * f(t - r[2] / c) / eta0),
    "(b) E=y f(t-z/c), H=+x f/eta0": (lambda r, t: Y * f(t - r[2] / c), lambda r, t: X * f(t - r[2] / c) / eta0),
    "(c) E=z f(t+x/c), H=+y f/eta0": (lambda r, t: Z * f(t + r[0] / c), lambda r, t: Y * f(t + r[0] / c) / eta0),
    "(d) E=x e^-(y/a)^2 f(t-z/c), H=y ... ": (lambda r, t: X * np.exp(-(r[1] / a) ** 2) * f(t - r[2] / c),
                                             lambda r, t: Y * np.exp(-(r[1] / a) ** 2) * f(t - r[2] / c) / eta0),
    "(e) E=x f(t-z/c), H=y f/(2 eta0)": (lambda r, t: X * f(t - r[2] / c), lambda r, t: Y * f(t - r[2] / c) / (2 * eta0)),
}
pts = [(np.array([0.3, 0.2, 0.4]), 1.0e-9), (np.array([-0.5, 0.7, -0.2]), -1.5e-9), (np.array([0.1, -0.4, 0.9]), 3.5e-9)]
for k, (E, H) in cands.items():
    rf = ra = dvE = 0
    for r, t in pts:
        rf = max(rf, rel(curl(E, r, t, 1e-4), -mu0 * ddt(H, r, t, 1e-13)))
        ra = max(ra, rel(curl(H, r, t, 1e-4), eps0 * ddt(E, r, t, 1e-13)))
        dvE = max(dvE, abs(np.trace(jac(E, r, t, 1e-4))) / (np.linalg.norm(curl(E, r, t, 1e-4)) + 1e-30))
    ok = rf < 1e-4 and ra < 1e-4 and dvE < 1e-5
    print(f"  {k:42s} Faraday {rf:.1e}  Ampere {ra:.1e}  divE/|curlE| {dvE:.1e}  -> {'satisfies Maxwell' if ok else 'FAILS'}")
    ALL.append(ok == k.startswith("(c)"))
cross = np.cross
print("  (b) E x H direction:", dname(cross(Y, X)), " but travel +z")
print("  (c) E x H direction:", dname(cross(Z, Y)), " travel -x (t + x/c);  u x E = (-x) x z =", dname(cross(-X, Z)))
print("  (a) E along z, travel along z: div E = dEz/dz != 0 -> not TEM")

# =========================================================================================== 19.2
hdr("19.2 Sheet on y = 0 with Js = +z g(t), free space")
print("  y>0: n=+y, Js x n: z x y =", dname(cross(Z, Y)), "-> H = -1/2 g x_hat")
print("  y<0: n=-y, z x (-y) =", dname(cross(Z, -Y)), "-> H = +1/2 g x_hat")
print(f"  eta0/2 * 0.5 = {etaC/2*0.5:.2f} V/m (60pi*0.5 = 30pi = {30*np.pi:.2f}); exact eta0: {eta0/2*0.5:.2f}")
g2 = lambda t: 0.5 * ((t > 0) & (t < 2e-6)) * 1.0
E, H, v, eta = sheet(np.zeros(3), Y, Z, g2, mu0, eps0)
Ec, Hc = (lambda r, t: E(r, t) * eta0 / eta0), H
for yy in (150.0, -450.0):
    r = np.array([0, yy, 0]); t = 1e-6
    delay = abs(yy) / cC
    gv = g2(t - delay)
    print(f"  y={yy:+.0f} m, t=1 us: delay {delay*1e6:.2f} us, source time {(t-delay)*1e6:+.2f} us, g = {gv}"
          f" -> E = {(-etaC/2*gv*Z)} V/m, H = {0.5*gv*np.cross(Z, np.sign(yy)*Y)} A/m")
Eg, Hg, _, _ = sheet(np.zeros(3), Y, Z, gauss(5e-9, 2e-9), mu0, eps0)
maxwell("19.2 fields", Eg, Hg, mu0, eps0, rpts(6, 2.0, 0, 2e-8, lambda r: r[1]), 1e-4, 1e-13)
bc("19.2", Eg, Hg, np.zeros(3), Y, Z, gauss(5e-9, 2e-9), [3e-9, 5e-9, 7e-9])
jump = cross(Y, (-0.25 * X) - (0.25 * X))
print("  jump check with g=0.5: y x (H+ - H-) =", jump, "= +0.5 z ✓" if np.allclose(jump, 0.5 * Z) else "FAIL")
print("  S direction y>0: (-z) x (-x) =", dname(cross(-Z, -X)), "; y<0: (-z) x (+x) =", dname(cross(-Z, X)))
print("  static (Lecture 13) sheet 0.5 A/m: H = 1/2 Js x n = ", 0.5 * cross(0.5 * Z, Y), "above (same as radiated, undelayed)")

# =========================================================================================== 19.3
hdr("19.3 True or false (sheet facts)")
print("  (a) E just above = E just below: T (E even); (b) H equal: F (H reverses, jump = Js)")
print("  (c) plane wave does not decay with distance: amplitude independent of d -> F")
print("  (d) Js.E = -(eta/2)|Js|^2 < 0 -> T; e.g. Js=1 A/m: Js.E =", -eta0 / 2, "W/m^2")
for er in (1, 4):
    et = eta0 / np.sqrt(er)
    print(f"  (e) er={er}: E amp per 1 A/m = {et/2:.1f} V/m, H amp = 0.5 A/m, v = {c/np.sqrt(er):.4e}")
print("  (e) ratio E(er=4)/E(er=1) =", 0.5, " -> T")
print("  (f) z<0 side of sheet on z=0 (Js = x f): E x H = (-x) x (+y) =", dname(cross(-X, Y)), " -> 'along +z' is F")

# =========================================================================================== 19.4
hdr("19.4 Reading wave parameters: H = 0.05 cos(6pi e8 t - 4 pi z) x_hat A/m")
w, b = 6 * np.pi * 1e8, 4 * np.pi
vp = w / b
print(f"  omega = {w:.4e} rad/s, f = {w/2/np.pi:.4e} Hz, beta = {b:.4f} rad/m, lambda = {2*np.pi/b:.4f} m")
print(f"  v_p = {vp:.4e} m/s, er = (c/v)^2 = {(cC/vp)**2:.4f} (course c) / {(c/vp)**2:.4f} (exact c)")
etam = mu0 * vp
print(f"  eta = mu0 v_p = {etam:.4f} Ohm (= 60 pi = {60*np.pi:.4f}); eta0/2 = {eta0/2:.2f}")
print(f"  E amplitude = eta*0.05 = {etam*0.05:.4f} V/m (3 pi = {3*np.pi:.4f})")
Edir = np.cross(X, Z)
print("  E = eta H x u: x x z =", dname(Edir), "-> E = -y 9.42 cos(...)")
print("  check E x H: (-y) x x =", dname(cross(-Y, X)), " = travel +z ✓")
ee = 4.0
E4 = lambda r, t: -Y * etam * 0.05 * np.cos(w * t - b * r[2])
H4 = lambda r, t: X * 0.05 * np.cos(w * t - b * r[2])
maxwell("19.4 fields (mu0, eps = mu0^-1 v^-2)", E4, H4, mu0, 1 / (mu0 * vp**2), rpts(5, 1.0, 0, 1e-8), 1e-5, 1e-13)

# =========================================================================================== 19.5
hdr("19.5 Find the error: sheet on x = 0, Js = -y g(t)")
print("  correct x>0: (-y) x (+x) =", dname(cross(-Y, X)), "-> H = +1/2 g z")
print("  correct x<0: (-y) x (-x) =", dname(cross(-Y, -X)), "-> H = -1/2 g z")
print("  E = -(eta0/2)(-y) g = +(eta0/2) g y on both sides")
print("  student x<0: H = +1/2 g z, E = eta0 H x u, u=-x: z x (-x) =", dname(cross(Z, -X)), "-> student E = -(eta0/2) g y (wrong)")
print("  student x>0: z x x =", dname(cross(Z, X)), "-> +(eta0/2) g y (accidentally right)")
gg = gauss(4e-9, 1.5e-9)
E5, H5, _, _ = sheet(np.zeros(3), X, -Y, gg, mu0, eps0)
maxwell("19.5 correct fields", E5, H5, mu0, eps0, rpts(6, 2.0, 0, 2e-8, lambda r: r[0]), 1e-4, 1e-13)
bc("19.5 correct", E5, H5, np.zeros(3), X, -Y, gg, [3e-9, 4e-9, 5.5e-9])
Hs = lambda r, t: 0.5 * Z * gg(t - abs(r[0]) / c)
Es = lambda r, t: (eta0 / 2) * Y * gg(t - abs(r[0]) / c) * np.sign(r[0])
t = 4e-9
print("  student jump x(H+ - H-) =", np.round(cross(X, Hs(np.array([1e-9, 0, 0]), t) - Hs(np.array([-1e-9, 0, 0]), t)), 6),
      " vs Js =", -Y * gg(t), " -> student violates the H jump")
print("  student E jump: E(0+) - E(0-) =", np.round(Es(np.array([1e-9, 0, 0]), t) - Es(np.array([-1e-9, 0, 0]), t), 3),
      " (= eta0 g y) -> violates E_t continuity")
print("  S check correct x<0: (+y) x (-z) =", dname(cross(Y, -Z)), "(away ✓)")
print("  E vs Js: E along +y, Js along -y -> opposite ✓")

# =========================================================================================== 19.6
hdr("19.6 Triangle pulse sheet on x = 0, Js = +z g(t), er = 9")
v6, eta6 = cC / 3, etaC / 3
print(f"  v = {v6:.3e} m/s = {v6*1e-9:.3f} m/ns (exact {c/3:.4e}); eta = 40 pi = {eta6:.2f} Ohm (exact {eta0/3:.2f})")
print(f"  eta/2 = 20 pi = {eta6/2:.2f}; peak E = 20pi*3 = 60 pi = {eta6/2*3:.1f} V/m; peak H = 1.5 A/m")
print("  x>0: z x x =", dname(cross(Z, X)), "-> H = +1/2 g y;  x<0: z x (-x) =", dname(cross(Z, -X)), "-> H = -1/2 g y")


def g6(tn):  # tn in ns: rise 0->3 over 0..1, fall to 0 at 4
    tn = np.asarray(tn, float)
    return np.where((tn > 0) & (tn <= 1), 3 * tn, np.where((tn > 1) & (tn < 4), 3 * (4 - tn) / 3, 0.0))


for xp in (0.5, -0.3):
    d = abs(xp) / 0.1
    print(f"  probe x={xp:+.1f} m: delay {d:.0f} ns; record nonzero {d:.0f}..{d+4:.0f} ns, peak at {d+1:.0f} ns: "
          f"E_z peak {-eta6/2*3:.1f} V/m, H_y peak {np.sign(xp)*1.5:+.1f} A/m")
    for tn in (d + 0.5, d + 1, d + 2.5):
        gv = g6(tn - d)
        print(f"     t={tn:.1f} ns: g={gv:.2f}  E_z={-eta6/2*gv:.1f}  H_y={np.sign(xp)*0.5*gv:+.3f}")
print("  snapshot t = 6 ns: |x| = 0.1 (6 - t')")
for tp in (0, 1, 4):
    print(f"     source time {tp} ns -> |x| = {0.1*(6-tp):.1f} m, g = {float(g6(tp)) if tp!=1 else 3.0}")
for xx in (0.55, 0.3, -0.3, -0.55):
    gv = float(g6(6 - abs(xx) / 0.1))
    print(f"     x={xx:+.2f}: g={gv:.2f}, H_y={np.sign(xx)*0.5*gv:+.3f} A/m, E_z={-eta6/2*gv:.1f} V/m")
eps9 = 9 * eps0
E6, H6, v6x, eta6x = sheet(np.zeros(3), X, Z, gauss(3e-9, 1e-9), mu0, eps9)
maxwell("19.6 fields in er=9", E6, H6, mu0, eps9, rpts(6, 0.8, 0, 1.5e-8, lambda r: r[0]), 2e-5, 2e-14)
bc("19.6", E6, H6, np.zeros(3), X, Z, gauss(3e-9, 1e-9), [2e-9, 3e-9, 4e-9])
print("  S x>0: (-z) x (+y) =", dname(cross(-Z, Y)), "; x<0: (-z) x (-y) =", dname(cross(-Z, -Y)))

# =========================================================================================== 19.7
hdr("19.7 Inverse problem: sheet on z = 0, probe at z = -600 m records E = +y 30pi V/m for 2.5<t<4 us")
Ep = 30 * np.pi
print(f"  30 pi = {Ep:.2f} V/m; delay 600/300 = {600/300:.1f} us")
Js_amp = -2 * Ep / etaC
print(f"  Js = -(2/eta0) E(t + 2us) = {Js_amp:+.4f} y A/m for 0.5<t<2 us   (exact eta0: {-2*Ep/eta0:+.5f})")
Js = Js_amp * Y
Hp = 0.5 * cross(Js, -Z)
print("  H at probe (n=-z): 1/2 Js x (-z) =", Hp, dname(Hp))
Sp = cross(Ep * Y, Hp)
print("  S at probe = E x H =", np.round(Sp, 3), dname(Sp), f"|S| = {np.linalg.norm(Sp):.2f} W/m^2 (= eta0 Js^2/4 = {etaC*0.25/4:.2f})")
print("  z>0: H = 1/2 Js x z =", 0.5 * cross(Js, Z), dname(0.5 * cross(Js, Z)))
print("  snapshot t=3 us: |z| = 300 (3 - t'), t' in (0.5, 2) ->", 300 * (3 - 2), "..", 300 * (3 - 0.5), "m")
for zz in (-500.0, 500.0, 200.0, 800.0):
    tp = 3 - abs(zz) / 300
    on = 0.5 < tp < 2
    print(f"     z={zz:+.0f}: t'={tp:.3f} us, on={on}, E={Ep*on:.2f} y, H={0.5*cross(Js*on, np.sign(zz)*Z)}")
print("  student trap: Js along +y would give E along -y (E opposes Js)")
g7 = gauss(1.25e-6, 0.3e-6)
E7, H7, _, _ = sheet(np.zeros(3), Z, -Y, g7, mu0, eps0)
maxwell("19.7 fields", E7, H7, mu0, eps0, rpts(6, 600, 0, 4e-6, lambda r: r[2]), 1e-2, 1e-11)
bc("19.7", E7, H7, np.zeros(3), Z, -Y, g7, [1e-6, 1.25e-6, 1.6e-6])

# =========================================================================================== 19.8
hdr("19.8 Cosine sheet on y = 0, Js = x 0.4 cos(wt), er = 2.25, f = 50 MHz")
v8 = cC / 1.5
eta8 = etaC / 1.5
w8 = 2 * np.pi * 50e6
b8 = w8 / v8
print(f"  v = {v8:.3e} m/s (exact {c/1.5:.4e}); eta = 80 pi = {eta8:.2f} Ohm (exact {eta0/1.5:.2f})")
print(f"  omega = {w8:.4e} = pi e8 rad/s; beta = {b8:.5f} rad/m (pi/2 = {np.pi/2:.5f}); lambda = {2*np.pi/b8:.3f} m")
print(f"  E amp = eta/2*0.4 = {eta8/2*0.4:.2f} V/m (16 pi = {16*np.pi:.2f}); H amp = 0.2 A/m")
print("  y>0: x x y =", dname(cross(X, Y)), "-> H = +0.2 z cos; y<0: x x (-y) =", dname(cross(X, -Y)), "-> H = -0.2 z cos")
S8 = eta8 * 0.16 / 4
print(f"  S peak = eta J0^2/4 = {S8:.3f} W/m^2 (3.2 pi = {3.2*np.pi:.3f}); E amp * H amp = {16*np.pi*0.2:.3f}")
print("  S dir y>0: (-x) x (+z) =", dname(cross(-X, Z)), "; y<0: (-x) x (-z) =", dname(cross(-X, -Z)))
t8 = 5e-9
print(f"  omega t at 5 ns = {w8*t8:.5f} (pi/2 = {np.pi/2:.5f})")
for yy in (1.0, -3.0, 2.0):
    ph = w8 * t8 - b8 * abs(yy)
    cs = np.cos(ph)
    Ev = -eta8 / 2 * 0.4 * cs * X
    Hv = 0.5 * 0.4 * cs * cross(X, np.sign(yy) * Y)
    Sv = cross(Ev, Hv)
    print(f"  y={yy:+.0f} m, t=5 ns: phase {ph/np.pi:+.3f} pi, cos={cs:+.4f}, E={np.round(Ev,3)}, H={np.round(Hv,4)}, S={np.round(Sv,3)}")
print("  zeros of E on y>0 at t=5 ns: pi/2 - pi y/2 = pi/2 + k pi -> y = 0, 2, 4, ... m (y = 2k)")
for k in range(3):
    print(f"     y={2*k}: cos = {np.cos(w8*t8 - b8*2*k):+.2e}")
print(f"  S time dependence at fixed y: cos^2 -> period {1/(2*50e6)*1e9:.0f} ns (twice the frequency: 100 MHz)")
print(f"  -Js.E at sheet, peak: eta/2 * 0.16 = {eta8/2*0.16:.3f} W/m^2 = 2 * S peak = {2*S8:.3f}")
E8, H8, _, _ = sheet(np.zeros(3), Y, X, lambda t: 0.4 * np.cos(w8 * t), mu0, 2.25 * eps0)
maxwell("19.8 fields in er=2.25", E8, H8, mu0, 2.25 * eps0, rpts(6, 3.0, 0, 2e-8, lambda r: r[1]), 1e-4, 1e-12)
bc("19.8", E8, H8, np.zeros(3), Y, X, lambda t: 0.4 * np.cos(w8 * t), [0, 3e-9, 7e-9])

# =========================================================================================== 19.9
hdr("19.9 SP18 E2 #5 style: sheet on z = 0, Js = -y g(t), free space, c = 0.3 m/ns")


def g9(tn):
    tn = np.asarray(tn, float)
    return np.where((tn > 0) & (tn < 1), 2.0, np.where((tn > 1) & (tn < 3), -4 + 2 * (tn - 1), 0.0))


print("  z>0: (-y) x (+z) =", dname(cross(-Y, Z)), "-> H = -1/2 g x;  z<0: (-y) x (-z) =", dname(cross(-Y, -Z)), "-> H = +1/2 g x")
print(f"  E = -(eta0/2)(-y) g = +60 pi g y, 60pi = {60*np.pi:.2f}")
print("  snapshot t = 4 ns, |z| = 0.3 (4 - t')")
for tp in (0, 1, 3):
    print(f"     t' = {tp} ns -> |z| = {0.3*(4-tp):.1f} m")
for zz in (0.2, 0.31, 0.6, 0.89, 0.91, 1.05, 1.19, 1.3, -0.2, -0.6, -0.89, -0.91, -1.05):
    tp = 4 - abs(zz) / 0.3
    gv = float(g9(tp))
    Hx = -0.5 * gv if zz > 0 else 0.5 * gv
    print(f"     z={zz:+.2f}: t'={tp:.3f}, g={gv:+.3f}, H_x={Hx:+.3f} A/m, E_y={60*np.pi*gv:+.1f} V/m")
print(f"  at |z| -> 0.9 m (inside, t'->1+): g=-4 -> H_x(z>0)=+2, H_x(z<0)=-2, E_y = {60*np.pi*-4:.1f} V/m (-240 pi)")
print(f"  on 0.9<|z|<1.2: g=+2 -> H_x(z>0)=-1, H_x(z<0)=+1, E_y = {60*np.pi*2:.1f} V/m (120 pi)")
print("  probe z=-0.9 m: delay", 0.9 / 0.3, "ns; H_x(t)=+1/2 g(t-3)")
for tn in (3.5, 4.01, 5.0, 5.99, 6.5):
    print(f"     t={tn:.2f} ns: H_x = {0.5*float(g9(tn-3)):+.3f} A/m")
for zz in (0.6, -1.0):
    tp = 4 - abs(zz) / 0.3
    gv = float(g9(tp))
    Ev = 60 * np.pi * gv * Y
    Hv = 0.5 * gv * cross(-Y, np.sign(zz) * Z)
    Sv = cross(Ev, Hv)
    print(f"  S at z={zz:+.1f}, t=4 ns: t'={tp:.3f}, g={gv:+.2f}, E={np.round(Ev,1)}, H={Hv}, S={np.round(Sv,1)} ({dname(Sv)}) |S|={np.linalg.norm(Sv):.1f}"
          f"  eta0 g^2/4 = {etaC*gv**2/4:.1f}")
JE = np.dot(-2 * Y, 60 * np.pi * 2 * Y)
print(f"  t=0.5 ns at sheet: Js = -2 y, E = {60*np.pi*2:.1f} y; Js.E = {JE:.1f} W/m^2 = -(eta0/2) g^2 = {-etaC/2*4:.1f}; each side {etaC*4/4:.1f}")
g9s = gauss(2e-9, 0.7e-9)
E9, H9, _, _ = sheet(np.zeros(3), Z, -Y, g9s, mu0, eps0)
maxwell("19.9 fields", E9, H9, mu0, eps0, rpts(6, 1.5, 0, 8e-9, lambda r: r[2]), 1e-4, 1e-13)
bc("19.9", E9, H9, np.zeros(3), Z, -Y, g9s, [1.5e-9, 2e-9, 3e-9])
# check the piecewise waveform directly at smooth points (inside linear segments), FD
E9p, H9p, _, _ = sheet(np.zeros(3), Z, -Y, lambda t: g9(t * 1e9 * c / 3e8), mu0, eps0)  # (time scaled so c*t matches 0.3 m/ns)
maxwell("19.9 actual waveform (smooth points)", E9p, H9p, mu0, eps0,
        [(np.array([0.1, 0.2, 0.6]), 4e-9 * 3e8 / c), (np.array([0, 0, -0.5]), 3.8e-9 * 3e8 / c)], 1e-5, 1e-14)

# =========================================================================================== 19.10
hdr("19.10 Two sheets: A on z=0, Js=+x 1 A/m for 0<t<10 ns; B on z=3 m, Js=-x 1 A/m for 10<t<20 ns")
rect = lambda a, b: (lambda t: 1.0 * ((t > a) & (t < b)))
cn = 0.3  # m/ns, times in ns
gA, gB = rect(0, 10), rect(10, 20)


def fields10(z, tn):
    E = np.zeros(3); H = np.zeros(3)
    for z0, Jd, gfun in ((0.0, X, gA), (3.0, -X, gB)):
        d = abs(z - z0)
        n = Z if z > z0 else -Z
        gv = gfun(tn - d / cn)
        E += -etaC / 2 * Jd * gv
        H += 0.5 * cross(Jd, n) * gv
    return E, H


print("  A above: x x z =", dname(cross(X, Z)), "-> H_A=-1/2 y ; A below: x x (-z) =", dname(cross(X, -Z)), "-> +1/2 y")
print("  B above: (-x) x z =", dname(cross(-X, Z)), "-> +1/2 y ; B below: (-x) x (-z) =", dname(cross(-X, -Z)), "-> -1/2 y")
print(f"  E_A = -60pi x = {-60*np.pi:.1f} x ; E_B = +60pi x = {60*np.pi:.1f} x")
mx = 0
for zz in np.linspace(3.01, 30, 400):
    for tn in np.linspace(-5, 120, 600):
        E, H = fields10(zz, tn)
        mx = max(mx, np.linalg.norm(E), np.linalg.norm(H))
check(f"19.10 fields beyond z = 3 m vanish at all times (max {mx:.1e})", mx < 1e-12)
print("  record z=-1.5 m:")
for tn in (3, 7, 14.9, 20, 27, 34.9, 40):
    E, H = fields10(-1.5, tn)
    print(f"     t={tn:5.1f} ns: E_x={E[0]:+.1f} V/m, H_y={H[1]:+.2f} A/m")
print("  snapshot t=15 ns:")
for zz in (-5, -4.4, -3, -1.6, -1.4, 0.5, 1.4, 1.6, 2.5, 2.99, 3.01, 4.0, 4.6):
    E, H = fields10(zz, 15)
    print(f"     z={zz:+5.2f} m: E_x={E[0]:+.1f}, H_y={H[1]:+.2f}")
E3 = -etaC / 2 * X * 1 + (-etaC / 2) * (-X) * 1
print(f"  E at sheet B during 10<t<20 (A's wave + B's own): {E3} -> J_B.E = {np.dot(-X, E3)}")
EA0 = -etaC / 2 * X
print(f"  sheet A during 0<t<10: E = {EA0[0]:.1f} x, J_A.E = {np.dot(X, EA0):.1f} W/m^2")
Sone = etaC / 4
print(f"  each pulse |S| = eta0/4 = {Sone:.2f} W/m^2, energy per pulse = S*10ns = {Sone*10:.1f} nJ/m^2; A supplies {etaC/2*10:.1f} nJ/m^2")
print("  B's pulse in z<0 arrives at z=-1.5 m at 25..35 ns (distance 4.5 m = 15 ns after 10..20 ns)")
# Maxwell check of the two-sheet superposition (smooth pulses)
gAs, gBs = gauss(5e-9, 2e-9), gauss(15e-9, 2e-9)
EA, HA, _, _ = sheet(np.zeros(3), Z, X, gAs, mu0, eps0)
EB, HB, _, _ = sheet(np.array([0, 0, 3.0]), Z, -X, gBs, mu0, eps0)
Et = lambda r, t: EA(r, t) + EB(r, t)
Ht = lambda r, t: HA(r, t) + HB(r, t)
maxwell("19.10 superposition", Et, Ht, mu0, eps0,
        [(np.array([0.2, 0.1, z]), t) for z, t in ((-1.5, 1e-8), (1.0, 1.2e-8), (2.2, 1.4e-8), (4.0, 2.5e-8), (-2.5, 2.8e-8))], 1e-4, 1e-13)
bc("19.10 sheet A", Et, Ht, np.zeros(3), Z, X, gAs, [3e-9, 5e-9])
bc("19.10 sheet B (A's wave present)", lambda r, t: Et(r, t), Ht, np.array([0, 0, 3.0]), Z, -X, gBs, [1.4e-8, 1.5e-8, 1.6e-8])

# =========================================================================================== 19.11
hdr("19.11 Sheet on the plane y = x, Js = z 0.2 cos(wt), f = 150 MHz, free space")
n11 = (X - Y) / np.sqrt(2)
w11 = 2 * np.pi * 150e6
b11 = w11 / cC
print(f"  beta = {b11:.5f} rad/m (pi), lambda = {2*np.pi/b11:.3f} m")
print("  n (side x>y) =", np.round(n11, 4), "; distance d = |x - y|/sqrt2")
H1 = 0.5 * 0.2 * cross(Z, n11)
print("  x>y: H amp vector = 1/2 Js x n =", np.round(H1, 5), dname(H1), f"|H| = {np.linalg.norm(H1):.3f}; 0.1/sqrt2 = {0.1/np.sqrt(2):.5f}")
print("  x<y: H amp vector =", np.round(0.5 * 0.2 * cross(Z, -n11), 5))
print(f"  E amp = eta0/2*0.2 = 12 pi = {etaC/2*0.2:.3f} V/m, along -z")
P = np.array([1.0, -1.0, 0.0])
dP = abs(np.dot(P, n11))
print(f"  P=(1,-1,0): d = {dP:.4f} m (sqrt2 = {np.sqrt(2):.4f}); t1 = d/c = {dP/cC*1e9:.3f} ns")
EP = -etaC / 2 * 0.2 * Z
HP = H1
SP = cross(EP, HP)
print("  at P, t1: E =", np.round(EP, 3), " H =", np.round(HP, 5), " S = E x H =", np.round(SP, 4), dname(SP),
      f"|S| = {np.linalg.norm(SP):.4f} W/m^2 (1.2 pi = {1.2*np.pi:.4f}); components +-{abs(SP[0]):.4f}")
u = 3e6 * Z
B = mu0 * HP
Fe = -e * EP
Fm = -e * cross(u, B)
print("  electron u = 3e6 z m/s: F_e =", Fe, dname(Fe), f"|F_e| = {np.linalg.norm(Fe):.3e} N")
print("  F_m = -e u x B =", Fm, dname(Fm), f"|F_m| = {np.linalg.norm(Fm):.3e} N; ratio = {np.linalg.norm(Fm)/np.linalg.norm(Fe):.5f}"
      f" (u/c with c=3e8: {3e6/cC:.3f}; with B = mu0 H and eta0=120pi exactly the ratio is u mu0/eta0 = {3e6*mu0/etaC:.5f})")
print(f"  |B| at P = {np.linalg.norm(B):.3e} T; |E|/c = {np.linalg.norm(EP)/cC:.3e}")
print("  u x B = 0 when u parallel to B: direction", dname(HP))
g11 = lambda t: 0.2 * np.cos(w11 * t)
E11, H11, _, _ = sheet(np.zeros(3), n11, Z, g11, mu0, eps0)
maxwell("19.11 fields", E11, H11, mu0, eps0, rpts(6, 2.0, 0, 1e-8, lambda r: (r[0] - r[1])), 1e-4, 1e-13)
bc("19.11", E11, H11, np.zeros(3), n11, Z, g11, [0, 1e-9, 2.3e-9])
print("  check H on x>y side at P, t1 from the sheet function:", np.round(H11(P, dP / c), 5), " E:", np.round(E11(P, dP / c), 3), "(exact eta0)")

# =========================================================================================== 19.12
hdr("19.12 Boundary-condition derivation: sheet on x = 0, Js = -z K(t), mu_r = 2, eps_r = 8")
mu12, eps12 = 2 * mu0, 8 * eps0
v12, eta12 = 1 / np.sqrt(mu12 * eps12), np.sqrt(mu12 / eps12)
print(f"  v = c/4 = {v12:.4e} m/s ({cC/4/1e6:.0f} m/us with c=3e8); eta = eta0/2 = {eta12:.2f} Ohm (60 pi = {60*np.pi:.2f})")
print("  +x wave: H = u x E/eta, x x z =", dname(cross(X, Z)), "-> H_y = -A f/eta")
print("  -x wave: (-x) x z =", dname(cross(-X, Z)), "-> H_y = +B g/eta")
print("  jump: x x (H1 - H2), H1-H2 = -2F/eta y; x x y =", dname(cross(X, Y)), "-> -2F/eta z = -K z -> F = eta K/2")
print("  recipe: x>0: (-z) x x =", dname(cross(-Z, X)), " ; x<0: (-z) x (-x) =", dname(cross(-Z, -X)))
Kp = 2e6  # A/m per s
vC12 = 75.0  # m/us
for xx in (1.5, 60.0):
    tt = 1.0
    dl = xx / vC12
    Hex = -0.5 * 2 * (tt - dl)
    Hqs = -0.5 * 2 * tt
    Ez = 30 * np.pi * 2 * (tt - dl)
    print(f"  x={xx} m, t=1 us: delay {dl:.3f} us, exact H_y = {Hex:+.3f} A/m, quasi-static {Hqs:+.3f}, rel err {(Hex-Hqs)/Hex*100:+.1f}%; E_z = (eta/2)K = {Ez:.2f} V/m")
dEdx = -(60 * np.pi / 2) / (vC12 * 1e6) * Kp
muH = 2 * mu0 * (-0.5) * Kp
print(f"  Faraday: dEz/dx = -(eta/2v) K' = {dEdx:.4f} V/m^2 ; mu dHy/dt = -(mu/2) K' = {muH:.4f} (exact eta/v = mu: {eta12/v12:.4e} vs {mu12:.4e})")
Kfun = lambda t: 2e6 * t * (t > 0)
E12, H12, _, _ = sheet(np.zeros(3), X, -Z, lambda t: np.cos(3e7 * t) + 0.3 * np.sin(1.1e7 * t), mu12, eps12)
maxwell("19.12 fields (mu_r=2, eps_r=8)", E12, H12, mu12, eps12, rpts(6, 20, 0, 1e-6, lambda r: r[0]), 1e-3, 1e-11)
bc("19.12", E12, H12, np.zeros(3), X, -Z, lambda t: np.cos(3e7 * t) + 0.3 * np.sin(1.1e7 * t), [0, 1e-7, 3e-7])
E12r, H12r, _, _ = sheet(np.zeros(3), X, -Z, Kfun, mu12, eps12)
r0 = np.array([1.5, 0, 0]); t0 = 1.5 / v12 + 0.98e-6
maxwell("19.12 ramp at x=1.5 m", E12r, H12r, mu12, eps12, [(r0, 1e-6), (np.array([-1.5, 0.3, 0.2]), 1e-6)], 1e-3, 1e-10)
print("  ramp fields from sheet function at x=1.5 m, t=1 us (exact c):", np.round(E12r(r0, 1e-6), 2), np.round(H12r(r0, 1e-6), 4))
print("  E opposes Js: E along", dname(E12r(r0, 1e-6)), "Js along -z")

hdr(f"SUMMARY: {sum(ALL)}/{len(ALL)} checks OK" + ("" if all(ALL) else "  <-- FAILURES"))
