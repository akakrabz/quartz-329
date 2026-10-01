#!/usr/bin/env python3
"""
L08.py -- numerical verification for
content-src/practice/08-conductors-dielectrics-and-polarization.md
(Practice, Lecture 8: conductors, dielectrics and polarization).

numpy + scipy only.  Every number, sign and direction that appears in an
answer on the page is printed below, and every symbolic result is checked
against an independent brute-force computation (numerical integration,
finite-difference divergence, direct superposition, or a numerical solve)
at two or more parameter sets.

Run:  python3 L08.py > L08.out
"""
import numpy as np
from scipy import integrate

eps0 = 8.8541878128e-12          # F/m
k_e = 1.0 / (4.0 * np.pi * eps0)  # m/F
FAILS = []


# ----------------------------------------------------------------- helpers
def section(title):
    print("\n" + "=" * 78)
    print(title)
    print("=" * 78)


def fmt(x):
    a = np.asarray(x, dtype=float)
    if a.ndim == 0:
        return f"{float(a):.6g}"
    return "[" + ", ".join(f"{v:.6g}" for v in a.ravel()) + "]"


def val(label, x, unit=""):
    print(f"  {label} = {fmt(x)} {unit}".rstrip())


def note(s):
    print("  -> " + s)


def check(label, got, want, rtol=1e-6, atol=0.0):
    got = np.asarray(got, dtype=float)
    want = np.asarray(want, dtype=float)
    ok = bool(np.allclose(got, want, rtol=rtol, atol=atol))
    print(f"  [{'OK  ' if ok else 'FAIL'}] {label}: got {fmt(got)}, expected {fmt(want)}")
    if not ok:
        FAILS.append(label)
    return ok


def check_true(label, cond):
    print(f"  [{'OK  ' if cond else 'FAIL'}] {label}")
    if not cond:
        FAILS.append(label)


def div_fd(F, p, h):
    """Central-difference divergence of a Cartesian vector field F at point p."""
    p = np.asarray(p, dtype=float)
    s = 0.0
    for i in range(3):
        e = np.zeros(3)
        e[i] = h
        s += (F(p + e)[i] - F(p - e)[i]) / (2.0 * h)
    return s


def shell_Ez_axis(Q, Rs, z0):
    """Brute-force E_z on the z axis at z0 from a uniform spherical shell (radius Rs,
    total charge Q) centred at the origin: Coulomb integral over theta (phi done exactly)."""
    f = lambda th: np.sin(th) * (z0 - Rs * np.cos(th)) / (Rs**2 + z0**2 - 2 * Rs * z0 * np.cos(th)) ** 1.5
    # absolute tolerance relative to the natural scale 2/max(z0,Rs)^2 (the result is
    # exactly 0 inside the shell, so a purely relative tolerance cannot be met there)
    I, _ = integrate.quad(f, 0.0, np.pi, limit=400, epsabs=1e-13 / max(z0, Rs)**2, epsrel=1e-11)
    return k_e * Q / 2.0 * I


def shell_V_axis(Q, Rs, z0):
    """Brute-force potential on the z axis at z0 from a uniform spherical shell."""
    f = lambda th: np.sin(th) / np.sqrt(Rs**2 + z0**2 - 2 * Rs * z0 * np.cos(th))
    I, _ = integrate.quad(f, 0.0, np.pi, limit=400, epsabs=0, epsrel=1e-11)
    return k_e * Q / 2.0 * I


# ======================================================================= 8.1
section("8.1  Resistance of a copper wire")
sigma, ell, A, I = 5.8e7, 58.0, 1.0e-6, 2.0
R = ell / (sigma * A)
J = I / A
E = J / sigma
V = E * ell
val("R = l/(sigma A)", R, "ohm")
val("J = I/A", J, "A/m^2")
val("E = J/sigma", E, "V/m")
val("E in mV/m", E * 1e3, "mV/m")
val("V = E l", V, "V")
check("V = E l equals I R", V, I * R)
# brute force: series sum of thin slices dR = dz/(sigma A) along the wire
Rbf, _ = integrate.quad(lambda z: 1.0 / (sigma * A), 0.0, ell)
check("R by integrating dz/(sigma A)", Rbf, R)
# drawn to twice the length at fixed volume
ell2 = 2 * ell
A2 = (ell * A) / ell2
R2 = ell2 / (sigma * A2)
val("stretched: A' = A/2", A2, "m^2")
val("stretched: R'", R2, "ohm")
check("R' = 4 R", R2, 4 * R)
note("E and J point along the current; electrons drift the opposite way")

# ======================================================================= 8.2
section("8.2  Relaxation times tau = eps/sigma")
materials = [("copper", 1.0, 5.8e7), ("sea water", 81.0, 4.0),
             ("distilled water", 81.0, 1e-4), ("glass", 6.0, 1e-12)]
taus = {}
for name, er, sg in materials:
    tau = er * eps0 / sg
    taus[name] = tau
    val(f"tau({name}), eps_r={er:g}, sigma={sg:g} S/m", tau, "s")
val("tau(sea water) in ns", taus["sea water"] * 1e9, "ns")
val("tau(distilled water) in microseconds", taus["distilled water"] * 1e6, "us")
t1 = taus["sea water"] * np.log(100.0)
val("ln(100)", np.log(100.0))
val("sea water: time to fall to 1% = tau ln 100", t1, "s")
val("   ... in ns", t1 * 1e9, "ns")
# brute force: integrate d rho/dt = -(sigma/eps) rho numerically (time in units of
# 1 ns to keep the solver well scaled) and locate the 1% crossing with an event
tau = taus["sea water"]
rate_ns = 1e-9 / tau          # sigma/eps in 1/ns
ev = lambda s, y: y[0] - 0.01
ev.terminal = True
sol = integrate.solve_ivp(lambda s, y: -rate_ns * y, (0, 10.0), [1.0], method="DOP853",
                          rtol=1e-12, atol=1e-15, events=ev)
tcross = sol.t_events[0][0] * 1e-9
check("1% time from numerical ODE solve (event detection)", tcross, t1, rtol=1e-8)
for name in taus:
    ratio = 1e-3 / taus[name]
    val(f"(1 ms)/tau({name})", ratio)
    note(f"{name}: {'conductor-like (tau << 1 ms)' if ratio > 10 else 'insulator-like (tau >> 1 ms)'} on a 1 ms time scale")

# ======================================================================= 8.3
section("8.3  MC: total field from a known P in eps = 3 eps0")
for Pvec in (np.array([2e-6, 0, 0]), np.array([1e-7, -3e-7, 5e-8])):
    er = 3.0
    eps = er * eps0
    chi = er - 1
    Ecorrect = Pvec / ((er - 1) * eps0)          # option (b) P/(2 eps0)
    check("chi_e = eps_r - 1", chi, 2.0)
    check("option (b) P/(2eps0) satisfies P = eps0 chi E", eps0 * chi * Ecorrect, Pvec)
    D = eps * Ecorrect
    check("D = eps E equals eps0 E + P", D, eps0 * Ecorrect + Pvec)
    opts = {"(a) P/(3eps0)": Pvec / (3 * eps0), "(b) P/(2eps0)": Pvec / (2 * eps0),
            "(c) 2P/eps0": 2 * Pvec / eps0, "(d) P/eps0": Pvec / eps0,
            "(e) 3P/(2eps0)": 3 * Pvec / (2 * eps0)}
    for key, Eo in opts.items():
        ok = np.allclose(eps0 * chi * Eo, Pvec)
        print(f"     {key}: satisfies P = eps0*chi*E ? {ok}")
    # distractor interpretations
    check("(a) is what P = eps E would give", opts["(a) P/(3eps0)"], Pvec / eps)
    check("(c) is what P = eps0 E / chi would give", opts["(c) 2P/eps0"], chi * Pvec / eps0)
    check("(e) equals D/eps0 (vacuum field of the same D)", opts["(e) 3P/(2eps0)"], D / eps0)

# ======================================================================= 8.4
section("8.4  Neutral conducting slab 0<z<2 cm in E0 = 10 kV/m z-hat")
E0, t_slab = 1.0e4, 0.02
rho_bot = -eps0 * E0     # n-hat = -z at z = 0
rho_top = +eps0 * E0     # n-hat = +z at z = t
val("rho_s(z=0) = n.D = (-z).(eps0 E0 z)", rho_bot, "C/m^2")
val("rho_s(z=0) in nC/m^2", rho_bot * 1e9, "nC/m^2")
val("rho_s(z=2cm) in nC/m^2", rho_top * 1e9, "nC/m^2")
check("faces equal and opposite (slab neutral)", rho_bot + rho_top, 0.0, atol=1e-20)


def Ez_total(z):
    # applied uniform field + two induced sheets, each rho/(2 eps0) sgn(z - z0)
    return (E0 + rho_bot / (2 * eps0) * np.sign(z - 0.0)
            + rho_top / (2 * eps0) * np.sign(z - t_slab))


for z, want, where in ((-0.01, E0, "below"), (0.01, 0.0, "inside"), (0.03, E0, "above")):
    check(f"E_z {where} the slab (z={z} m) by superposition", Ez_total(z), want, atol=1e-9)
dV_with = -integrate.quad(Ez_total, 0.0, t_slab, points=[0.0, t_slab])[0]
dV_without = -E0 * t_slab
check("V(2cm)-V(0) with the slab (equipotential)", dV_with, 0.0, atol=1e-9)
val("V(2cm)-V(0) WITHOUT the slab (distractor in (e))", dV_without, "V")
note("electrons pushed toward -z (against E0): bottom face negative, top face positive")

# ======================================================================= 8.5
section("8.5  Find the error: graded slab P = P0 (1 + z/d) z-hat, 0<z<d")
for P0, d in ((5e-6, 1e-3), (2.0, 3.0)):
    Pz = lambda z: P0 * (1 + z / d)
    h = d * 1e-5
    zs = np.linspace(0.1 * d, 0.9 * d, 5)
    rhob_fd = np.array([-(Pz(z + h) - Pz(z - h)) / (2 * h) for z in zs])
    check(f"rho_b = -dPz/dz = -P0/d by FD (P0={P0}, d={d})", rhob_fd, -P0 / d * np.ones(5), rtol=1e-6)
    sb0_correct = Pz(0) * (-1.0)   # outward normal -z
    sbd = Pz(d) * (+1.0)
    vol = integrate.quad(lambda z: -P0 / d, 0, d)[0]
    total_correct = vol + sb0_correct + sbd
    total_student = vol + Pz(0) * (+1.0) + sbd
    val("  rho_sb(0) correct (n=-z)", sb0_correct, "C/m^2")
    val("  rho_sb(d) (n=+z)", sbd, "C/m^2")
    val("  integral of rho_b over thickness", vol, "C/m^2")
    check("  total bound charge per area (correct) = 0", total_correct, 0.0, atol=1e-12 * abs(P0))
    check("  student's total = 2 P0", total_student, 2 * P0)
    # field check: D = 0 (no free charge, neutral infinite slab), E = -P/eps0 inside;
    # Gauss with total charge: eps0 dE/dz = rho_b
    Ez = lambda z: -Pz(z) / eps0
    check("  eps0 dEz/dz = rho_b (E = -P/eps0)", eps0 * (Ez(0.5 * d + h) - Ez(0.5 * d - h)) / (2 * h), -P0 / d, rtol=1e-6)
    check("  jump eps0*(E(0+) - E(0-)) = rho_sb(0)", eps0 * (Ez(0.0) - 0.0), sb0_correct)
    check("  jump eps0*(E(d+) - E(d-)) = rho_sb(d)", eps0 * (0.0 - Ez(d)), sbd)

# ======================================================================= 8.6
section("8.6  Coaxial-shell resistor, radial current")


def radial_R_closed(a, b, L, sg):
    return np.log(b / a) / (2 * np.pi * sg * L)


def radial_R_laplace(a, b, L, sg, N=4001):
    """Brute force: solve (1/r) d/dr (r dV/dr) = 0 by finite differences with
    V(a)=1, V(b)=0, then I = sigma * E * 2 pi r L at several radii, R = 1/I."""
    r = np.linspace(a, b, N)
    hh = r[1] - r[0]
    n = N - 2
    main = np.zeros(n)
    lo = np.zeros(n - 1)
    up = np.zeros(n - 1)
    rhs = np.zeros(n)
    for j in range(n):
        ri = r[j + 1]
        rp, rm = ri + hh / 2, ri - hh / 2
        main[j] = -(rp + rm)
        if j > 0:
            lo[j - 1] = rm
        else:
            rhs[j] -= rm * 1.0      # V(a) = 1
        if j < n - 1:
            up[j] = rp
        # V(b) = 0 adds nothing
    from scipy.linalg import solve_banded
    ab = np.zeros((3, n))
    ab[0, 1:] = up
    ab[1, :] = main
    ab[2, :-1] = lo
    Vin = solve_banded((1, 1), ab, rhs)
    Vfull = np.concatenate(([1.0], Vin, [0.0]))
    Er = -np.gradient(Vfull, r)
    Icur = sg * Er * 2 * np.pi * r * L
    return 1.0 / np.mean(Icur[N // 4: 3 * N // 4]), Icur


for (a, b, L, sg) in ((0.01, 0.02, 0.10, 2.0), (0.003, 0.012, 0.5, 0.37)):
    Rc = radial_R_closed(a, b, L, sg)
    Rq = integrate.quad(lambda r: 1.0 / (sg * 2 * np.pi * r * L), a, b)[0]
    Rl, Icur = radial_R_laplace(a, b, L, sg)
    check(f"R radial: closed form vs series-shell integral (a={a},b={b})", Rq, Rc)
    check("R radial: closed form vs FD Laplace solve", Rl, Rc, rtol=1e-5)
    spread = np.ptp(Icur[50:-50]) / np.mean(Icur[50:-50])
    check_true(f"  current through every cylinder the same (div J = 0), spread {spread:.1e}", spread < 1e-4)

a, b, L, sg, I = 0.01, 0.02, 0.10, 2.0, 3.0
Rr = radial_R_closed(a, b, L, sg)
Ja, Jb = I / (2 * np.pi * a * L), I / (2 * np.pi * b * L)
val("R_radial = ln(b/a)/(2 pi sigma L)", Rr, "ohm")
val("J(a) = I/(2 pi a L)", Ja, "A/m^2")
val("J(b)", Jb, "A/m^2")
val("E(a) = J(a)/sigma", Ja / sg, "V/m")
val("E(b)", Jb / sg, "V/m")
Vab = integrate.quad(lambda r: I / (2 * np.pi * r * L * sg), a, b)[0]
val("V(a)-V(b) = integral of E dr", Vab, "V")
check("V(a)-V(b) = I R", Vab, I * Rr)
val("1500/pi (J(a) exact form)", 1500 / np.pi, "A/m^2")
Rax = L / (sg * np.pi * (b**2 - a**2))
val("R_axial = L/(sigma pi (b^2-a^2))", Rax, "ohm")
val("R_axial / R_radial", Rax / Rr)
# thin-shell limit: R -> t/(sigma 2 pi a L)
for tfrac in (1e-3, 1e-5):
    bb = a * (1 + tfrac)
    check(f"thin wall limit t/a={tfrac}", radial_R_closed(a, bb, L, sg),
          (bb - a) / (sg * 2 * np.pi * a * L), rtol=tfrac)
# divergence of J = I/(2 pi r L) r-hat is zero (FD, Cartesian)
Jfield = lambda p: I / (2 * np.pi * L) * np.array([p[0], p[1], 0.0]) / (p[0]**2 + p[1]**2)
check("div J = 0 (FD) at (1.3cm, 0.4cm, 0)", div_fd(Jfield, [0.013, 0.004, 0.0], 1e-7), 0.0, atol=1e-3)
note("E and J point radially outward (+r-hat) from the inner electrode; V(a) > V(b)")

# ======================================================================= 8.7
section("8.7  Radially polarized ball, no free charge")


def ball_checks(P0, Rb, verbose=False):
    PA = lambda p: P0 * p / np.linalg.norm(p)            # P0 r-hat
    PB = lambda p: P0 * p / Rb                            # P0 (r/R) r-hat
    pts = [np.array([0.3, 0.2, -0.1]) * Rb, np.array([-0.5, 0.1, 0.6]) * Rb]
    for p in pts:
        r = np.linalg.norm(p)
        check(f"  A: -div P = -2P0/r by FD at r={r:.4g}", -div_fd(PA, p, 1e-6 * Rb), -2 * P0 / r, rtol=1e-6)
        check(f"  B: -div P = -3P0/R by FD at r={r:.4g}", -div_fd(PB, p, 1e-6 * Rb), -3 * P0 / Rb, rtol=1e-6)
    # totals by numerical integration
    QvA = integrate.quad(lambda r: (-2 * P0 / r) * 4 * np.pi * r**2, 0, Rb)[0]
    QvB = integrate.quad(lambda r: (-3 * P0 / Rb) * 4 * np.pi * r**2, 0, Rb)[0]
    Qs = P0 * 4 * np.pi * Rb**2
    check("  A: volume bound charge = -4 pi P0 R^2", QvA, -Qs)
    check("  B: volume bound charge = -4 pi P0 R^2", QvB, -Qs)
    check("  A: total bound charge = 0", QvA + Qs, 0.0, atol=1e-12 * Qs)
    check("  B: total bound charge = 0", QvB + Qs, 0.0, atol=1e-12 * Qs)
    # fields by Gauss with numerically integrated enclosed (total) charge
    for r in (0.25 * Rb, 0.8 * Rb):
        QA = integrate.quad(lambda s: (-2 * P0 / s) * 4 * np.pi * s**2, 0, r)[0]
        QB = integrate.quad(lambda s: (-3 * P0 / Rb) * 4 * np.pi * s**2, 0, r)[0]
        check(f"  A: E_r({r/Rb:.2f}R) = -P0/eps0", QA / (4 * np.pi * eps0 * r**2), -P0 / eps0)
        check(f"  B: E_r({r/Rb:.2f}R) = -P0 r/(eps0 R)", QB / (4 * np.pi * eps0 * r**2), -P0 * r / (eps0 * Rb))
    for r in (1.5 * Rb, 4 * Rb):
        check(f"  A,B: E_r({r/Rb:.1f}R) = 0 outside", (QvA + Qs) / (4 * np.pi * eps0 * r**2), 0.0,
              atol=1e-9 * P0 / eps0)
    # D = eps0 E + P = 0 inside
    r = 0.6 * Rb
    check("  B: D_r = eps0 E_r + P_r = 0 inside", eps0 * (-P0 * r / (eps0 * Rb)) + P0 * r / Rb, 0.0, atol=1e-20)
    # brute force: potential of the ball (B) by direct Coulomb integration over the
    # bound volume charge and the bound surface charge; then E = -dV/dz by FD.

    def V_ball_B(z0):
        def inner(rp):
            g = lambda th: np.sin(th) / np.sqrt(rp**2 + z0**2 - 2 * rp * z0 * np.cos(th))
            return integrate.quad(g, 0, np.pi, limit=200, epsrel=1e-11)[0]
        vol = integrate.quad(lambda rp: (-3 * P0 / Rb) * 2 * np.pi * rp**2 * inner(rp), 0, Rb,
                             points=[min(z0, Rb)] if z0 < Rb else None, limit=200, epsrel=1e-10)[0]
        surf = P0 * 2 * np.pi * Rb**2 * inner(Rb)
        return k_e * (vol + surf)
    for z0 in (0.5 * Rb, 2.0 * Rb):
        hz = 1e-4 * Rb
        Ez_bf = -(V_ball_B(z0 + hz) - V_ball_B(z0 - hz)) / (2 * hz)
        want = -P0 * z0 / (eps0 * Rb) if z0 < Rb else 0.0
        check(f"  B: brute-force Coulomb E_z at z={z0/Rb:.1f}R", Ez_bf, want, rtol=1e-5, atol=1e-6 * P0 / eps0)
    V0_bf = V_ball_B(1e-9 * Rb)
    check("  B: brute-force V(0) = -P0 R/(2 eps0)", V0_bf, -P0 * Rb / (2 * eps0), rtol=1e-6)
    return Qs


for (P0, Rb) in ((2e-6, 0.05), (7e-3, 1.3)):
    print(f" parameter set P0={P0}, R={Rb}")
    ball_checks(P0, Rb)

P0, Rb = 2e-6, 0.05
val("A: rho_b(R) = -2P0/R", -2 * P0 / Rb, "C/m^3")
val("A: rho_b(R/2) = -4P0/R", -4 * P0 / Rb, "C/m^3")
val("A,B: rho_sb = P0", P0, "C/m^2")
val("total surface bound charge 4 pi R^2 P0", 4 * np.pi * Rb**2 * P0, "C")
val("   ... in nC", 4 * np.pi * Rb**2 * P0 * 1e9, "nC")
val("B: rho_b = -3P0/R", -3 * P0 / Rb, "C/m^3")
val("A: E inside = -P0/eps0 (r-hat)", -P0 / eps0, "V/m")
val("B: E just inside surface = -P0/eps0", -P0 / eps0, "V/m")
val("B: E at r = R/2 = -P0/(2 eps0)", -P0 / (2 * eps0), "V/m")
val("B: V(0) - V(inf) = -P0 R/(2 eps0)", -P0 * Rb / (2 * eps0), "V")
note("E inside points inward (-r-hat); centre is at LOWER potential than infinity")

# ======================================================================= 8.8
section("8.8  Point charge q at the centre of a dielectric sphere")


def pc_in_dielectric(q, er, Rs):
    chi = er - 1
    D = lambda r: q / (4 * np.pi * r**2)
    Ein = lambda r: q / (4 * np.pi * er * eps0 * r**2)
    Eout = lambda r: q / (4 * np.pi * eps0 * r**2)
    Pin = lambda r: D(r) - eps0 * Ein(r)
    check("  P = eps0 chi E inside", Pin(0.5 * Rs), eps0 * chi * Ein(0.5 * Rs))
    check("  P = (1 - 1/er) D", Pin(0.5 * Rs), (1 - 1 / er) * D(0.5 * Rs))
    Pvec = lambda p: (1 - 1 / er) * q / (4 * np.pi) * p / np.linalg.norm(p)**3
    for p in (np.array([0.2, 0.1, 0.3]) * Rs, np.array([-0.4, 0.5, -0.2]) * Rs):
        dv = div_fd(Pvec, p, 1e-6 * Rs)
        scale = np.linalg.norm(Pvec(p)) / np.linalg.norm(p)
        check("  rho_b = -div P = 0 for 0<r<R (FD)", dv / scale, 0.0, atol=1e-6)
    sb = Pin(Rs)
    Qsb = sb * 4 * np.pi * Rs**2
    check("  total surface bound charge = (1-1/er) q", Qsb, (1 - 1 / er) * q)
    # bound charge hidden at the centre: Gauss with total charge on small spheres
    for r in (1e-3 * Rs, 0.1 * Rs, 0.9 * Rs):
        Qtot = eps0 * Ein(r) * 4 * np.pi * r**2
        check(f"  total charge inside r={r/Rs:g}R is q/er", Qtot, q / er)
        check(f"  bound charge inside r={r/Rs:g}R is -(1-1/er) q", Qtot - q, -(1 - 1 / er) * q)
    check("  total bound charge (centre + surface) = 0", -(1 - 1 / er) * q + Qsb, 0.0, atol=1e-12 * abs(q))
    check("  jump eps0 [E(R+) - E(R-)] = rho_sb", eps0 * (Eout(Rs) - Ein(Rs)), sb)
    check("  D_r continuous at R (no free surface charge)", eps0 * Eout(Rs), er * eps0 * Ein(Rs))
    # brute force: superpose free q + bound point charge at centre + bound shell, by Coulomb integral
    qb = -(1 - 1 / er) * q
    for z0, want in ((0.5 * Rs, Ein(0.5 * Rs)), (2.0 * Rs, Eout(2.0 * Rs))):
        Ebf = k_e * (q + qb) / z0**2 + shell_Ez_axis(Qsb, Rs, z0)
        check(f"  brute-force superposition E at r={z0/Rs:.1f}R", Ebf, want, rtol=1e-8)
    return D, Ein, Eout, Pin


pc_results = {}
for (q, er, Rs) in ((8e-9, 4.0, 0.03), (-3e-6, 2.5, 0.4)):
    print(f" parameter set q={q}, er={er}, R={Rs}")
    pc_results[(q, er, Rs)] = pc_in_dielectric(q, er, Rs)

q, er, Rs = 8e-9, 4.0, 0.03
D, Ein, Eout, Pin = pc_results[(q, er, Rs)]
val("chi_e = er - 1", er - 1)
val("D(R) = q/(4 pi R^2)", D(Rs), "C/m^2")
val("E(R-) = q/(4 pi eps R^2)", Ein(Rs), "V/m")
val("E(R+) = q/(4 pi eps0 R^2)", Eout(Rs), "V/m")
val("P(R-) = rho_sb(R) = (3/4) q/(4 pi R^2)", Pin(Rs), "C/m^2")
val("   ... in nC/m^2", Pin(Rs) * 1e9, "nC/m^2")
val("total surface bound charge", Pin(Rs) * 4 * np.pi * Rs**2 * 1e9, "nC")
val("bound point charge at centre", -(1 - 1 / er) * q * 1e9, "nC")
val("net charge at centre q/er", q / er * 1e9, "nC")
val("E(R+) - E(R-)", Eout(Rs) - Ein(Rs), "V/m")
val("eps0 * jump", eps0 * (Eout(Rs) - Ein(Rs)), "C/m^2")

# ======================================================================= 8.9
section("8.9  Point charge in the cavity of a thick conducting shell")
q, b, c, Qs = 3e-9, 0.02, 0.04, -5e-9
Qin, Qout = -q, Qs + q
rs_b = Qin / (4 * np.pi * b**2)
rs_c = Qout / (4 * np.pi * c**2)
val("inner-surface charge", Qin * 1e9, "nC")
val("outer-surface charge", Qout * 1e9, "nC")
val("rho_s(b)", rs_b, "C/m^2")
val("rho_s(b) in nC/m^2", rs_b * 1e9, "nC/m^2")
val("rho_s(c)", rs_c, "C/m^2")
val("rho_s(c) in nC/m^2", rs_c * 1e9, "nC/m^2")
val("k q", k_e * q, "V m")
val("k (q+Qs)", k_e * (q + Qs), "V m")


def E_cavity(r, q=q, Qin=Qin, Qout=Qout):
    # brute force: point charge + two uniform shells (Coulomb integrals)
    return k_e * q / r**2 + shell_Ez_axis(Qin, b, r) + shell_Ez_axis(Qout, c, r)


def V_cavity(r, q=q, Qin=Qin, Qout=Qout):
    return k_e * q / r + shell_V_axis(Qin, b, r) + shell_V_axis(Qout, c, r)


for r, want in ((0.01, k_e * q / 0.01**2), (0.03, 0.0), (0.05, k_e * (q + Qs) / 0.05**2)):
    Ebf = E_cavity(r)
    check(f"E_r(r={r} m) brute-force superposition", Ebf, want, rtol=1e-8, atol=1e-6)
    val(f"   E_r({r} m)", want, "V/m")
note("r<b: E outward (+r-hat); in the metal E = 0; r>c: E inward (-r-hat) since q+Qs < 0")
Vsh = k_e * (q + Qs) / c
V1 = Vsh + k_e * q * (1 / 0.01 - 1 / b)
val("V(shell) = k (q+Qs)/c", Vsh, "V")
val("V(1 cm) = V(shell) + k q (1/r - 1/b)", V1, "V")
check("V(shell) by brute-force superposition (r=3 cm)", V_cavity(0.03), Vsh, rtol=1e-8)
check("V(1 cm) by brute-force superposition", V_cavity(0.01), V1, rtol=1e-8)
# off-centre: inner-surface induced density from the (exact) image solution integrates to -q,
# and the potential it gives on r=b is constant (validates the formula used).
s = 0.01
sigma_in = lambda th: -q * (b**2 - s**2) / (4 * np.pi * b * (b**2 + s**2 - 2 * b * s * np.cos(th))**1.5)
Qind = integrate.quad(lambda th: sigma_in(th) * 2 * np.pi * b**2 * np.sin(th), 0, np.pi, epsrel=1e-12)[0]
check("off-centre q (s=1 cm): total induced inner charge still -q", Qind, -q, rtol=1e-9)
qimg, simg = -q * b / s, b**2 / s
Vb = [k_e * q / np.sqrt(b**2 + s**2 - 2 * b * s * np.cos(th)) +
      k_e * qimg / np.sqrt(b**2 + simg**2 - 2 * b * simg * np.cos(th)) for th in np.linspace(0, np.pi, 7)]
check("  image solution: q + image give V = 0 on r = b (formula sanity)", Vb, np.zeros(7), atol=1e-6)
val("  near-side / far-side inner density ratio (image method, not used on page)",
    sigma_in(0.0) / sigma_in(np.pi))
note("off-centre: inner total -q (unchanged), inner distribution non-uniform (densest nearest q);")
note("outer surface uniform with q+Qs; E in metal 0; E outside unchanged; V(shell) unchanged")
# grounded
Vg1 = k_e * q * (1 / 0.01 - 1 / b)
val("grounded: outer-surface charge", 0.0, "nC")
val("grounded: shell net charge", -q * 1e9, "nC")
val("grounded: charge that flows from ground onto shell", (-q - Qs) * 1e9, "nC")
val("grounded: V(1 cm) = k q (1/r - 1/b)", Vg1, "V")
check("grounded: V(1 cm) brute force", V_cavity(0.01, Qout=0.0), Vg1, rtol=1e-8)
check("grounded: V(shell) brute force = 0", V_cavity(0.03, Qout=0.0), 0.0, atol=1e-6)
check("grounded: E outside = 0", E_cavity(0.05, Qout=0.0), 0.0, atol=1e-6)
# second parameter set for the symbolic structure
q2, b2, c2, Qs2 = -7e-6, 0.3, 0.35, 2e-6
for r, want in ((0.1, k_e * q2 / 0.1**2), (0.32, 0.0), (0.9, k_e * (q2 + Qs2) / 0.81)):
    Ebf = k_e * q2 / r**2 + shell_Ez_axis(-q2, b2, r) + shell_Ez_axis(Qs2 + q2, c2, r)
    check(f"set 2: E_r(r={r}) brute force", Ebf, want, rtol=1e-8, atol=1e-3)

# ======================================================================= 8.10
section("8.10  Relaxation of rho(x,0) = 18 eps0 cos(3x) in eps = 9 eps0, sigma = 900 eps0")
eps_m, sig_m, rho0, kx = 9 * eps0, 900 * eps0, 18 * eps0, 3.0
tau = eps_m / sig_m
val("sigma = 900 eps0", sig_m, "S/m")
val("tau = eps/sigma", tau, "s")
Eamp = rho0 / (kx * eps_m)
Jamp = sig_m * Eamp
val("E amplitude rho0/(k eps)", Eamp, "V/m")
val("J amplitude sigma * E amplitude", Jamp, "A/m^2")
val("J amplitude / eps0", Jamp / eps0, "(x eps0) A/m^2")
rho = lambda x, t: rho0 * np.cos(kx * x) * np.exp(-t / tau)
Ex = lambda x, t: Eamp * np.sin(kx * x) * np.exp(-t / tau)
Jx = lambda x, t: sig_m * Ex(x, t)
for (x, t) in ((0.37, 0.0), (1.9, 0.004), (-2.2, 0.031)):
    hx, ht = 1e-6, 1e-9
    gauss = eps_m * (Ex(x + hx, t) - Ex(x - hx, t)) / (2 * hx)
    check(f"Gauss eps dEx/dx = rho at (x={x}, t={t})", gauss, rho(x, t), rtol=1e-6, atol=1e-9 * rho0)
    cont = (rho(x, t + ht) - rho(x, t - ht)) / (2 * ht) + (Jx(x + hx, t) - Jx(x - hx, t)) / (2 * hx)
    check(f"continuity d(rho)/dt + dJx/dx = 0 at (x={x}, t={t})", cont / (rho0 / tau), 0.0, atol=1e-6)
# ODE solved numerically at one point
x1 = 0.2
sol = integrate.solve_ivp(lambda t, y: -(sig_m / eps_m) * y, (0, 0.05), [rho(x1, 0)],
                          rtol=1e-11, atol=1e-25, t_eval=[0.01, 0.03])
check("numerical ODE solution vs rho0 cos(kx) exp(-t/tau)", sol.y[0], rho(x1, np.array([0.01, 0.03])), rtol=1e-8)
t1pct = tau * np.log(100)
val("time to 1% = tau ln 100", t1pct, "s")
val("E_x(pi/6, 10 ms) = (2/3) e^-1", Ex(np.pi / 6, 0.01), "V/m")
val("rho(0, 10 ms)/eps0", rho(0, 0.01) / eps0, "(x eps0) C/m^3")
drho_amp = -(1 / tau) * 18.0          # d(rho)/dt amplitude at t = 0, in units of eps0
dJ_amp = kx * Jamp / eps0              # dJx/dx amplitude at t = 0, in units of eps0
val("1/tau", 1 / tau, "1/s")
val("d(rho)/dt amplitude / eps0 = -(1/tau)(18)", drho_amp)
val("dJx/dx amplitude / eps0 = 3 (600)", dJ_amp)
check("continuity amplitudes cancel", drho_amp + dJ_amp, 0.0, atol=1e-9)
note("J at x slightly > 0 is +x, at x slightly < 0 is -x: current flows away from the crest at x=0")
print("  J_x(+0.1, 0) sign:", np.sign(Jx(0.1, 0)), "  J_x(-0.1, 0) sign:", np.sign(Jx(-0.1, 0)))
# net charge per period is zero
Qper = integrate.quad(lambda x: rho(x, 0), 0, 2 * np.pi / kx)[0]
check("net charge per spatial period = 0", Qper / rho0, 0.0, atol=1e-12)
# charge in a positive lump |x| < pi/6 (per unit area)
Qlump = integrate.quad(lambda x: rho(x, 0), -np.pi / 6, np.pi / 6)[0]
check("charge per area in one positive lump = 12 eps0", Qlump, 12 * eps0)


def brute_relax(kk, periods=2, N=2000, nsteps=600, tmax=None):
    """Explicit numerical solution of Gauss + continuity + Ohm on a periodic grid:
    E from rho by cumulative integration (zero mean = no uniform part), then
    d rho/dt = -d(sigma E)/dx by central differences, RK4 in time."""
    Lx = periods * 2 * np.pi / kk
    x = np.linspace(0, Lx, N, endpoint=False)
    hxx = x[1] - x[0]

    def E_of(r):
        cum = np.concatenate(([0.0], np.cumsum(0.5 * (r[1:] + r[:-1]) * hxx))) / eps_m
        return cum - cum.mean()

    def rhs(r):
        Ef = E_of(r)
        return -sig_m * (np.roll(Ef, -1) - np.roll(Ef, 1)) / (2 * hxx)
    tmax = tmax or 3 * tau
    dt = tmax / nsteps
    r = rho0 * np.cos(kk * x)
    E_init_max = np.max(np.abs(E_of(r)))
    for _ in range(nsteps):
        k1 = rhs(r)
        k2 = rhs(r + 0.5 * dt * k1)
        k3 = rhs(r + 0.5 * dt * k2)
        k4 = rhs(r + dt * k3)
        r = r + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    rate = -np.log(r[0] / rho0) / tmax
    return rate, E_init_max


for kk in (3.0, 30.0):
    rate, Emax = brute_relax(kk)
    check(f"brute-force grid solution, k={kk}: decay rate = 1/tau", rate, 1 / tau, rtol=2e-4)
    check(f"brute-force grid solution, k={kk}: initial |E|max = rho0/(k eps)", Emax, rho0 / (kk * eps_m), rtol=2e-4)
note("decay rate independent of the spatial period (k=3 and k=30 identical); E amplitude scales as 1/k")

# ======================================================================= 8.11
section("8.11  Composite sphere: core Q1, dielectric 3eps0, shell Q2, coat 2eps0, free space")


def composite(Q1, Q2, r1, r2, r3, r4, er2, er4, verbose=False):
    """Regions: (i) r<r1 metal Q1, (ii) r1<r<r2 eps=er2 eps0, (iii) r2<=r<=r3 metal Q2,
    (iv) r3<r<r4 eps=er4 eps0, (v) r>r4 vacuum."""
    # exact region-by-region formulas (one-sided limits taken by choosing the region)
    D_ii = lambda r: Q1 / (4 * np.pi * r**2)
    D_out = lambda r: (Q1 + Q2) / (4 * np.pi * r**2)          # regions (iv) and (v)
    P_ii = lambda r: D_ii(r) - eps0 * D_ii(r) / (er2 * eps0)
    P_iv = lambda r: D_out(r) - eps0 * D_out(r) / (er4 * eps0)

    def D(r):
        if r < r1 or (r2 < r < r3):
            return 0.0
        if r1 < r < r2:
            return D_ii(r)
        return D_out(r)

    def epsr(r):
        if r1 < r < r2:
            return er2
        if r3 < r < r4:
            return er4
        return 1.0

    def E(r):
        return D(r) / (epsr(r) * eps0)

    def P(r):
        return D(r) - eps0 * E(r)
    # free surface charges on metals (n-hat out of the metal, D on the dielectric side)
    f1 = +D_ii(r1)
    f2 = -D_ii(r2)
    f3 = +D_out(r3)
    # bound surface charges on dielectric faces (n-hat out of the dielectric)
    b1 = -P_ii(r1)
    b2 = +P_ii(r2)
    b3 = -P_iv(r3)
    b4 = +P_iv(r4)
    A = lambda r: 4 * np.pi * r**2
    return dict(D=D, E=E, P=P, epsr=epsr, f=(f1, f2, f3), b=(b1, b2, b3, b4),
                Qf=(f1 * A(r1), f2 * A(r2), f3 * A(r3)),
                Qb=(b1 * A(r1), b2 * A(r2), b3 * A(r3), b4 * A(r4)))


# page set: Q2 = -8 C (changed from -10 C so the outer layer does not repeat practice 9.10,
# which has Q1 + Q2 = -4 C with the same eps_r = 2 coating and radii 1, 2, 3, 4 m)
for pars in ((6.0, -8.0, 1.0, 2.0, 3.0, 4.0, 3.0, 2.0), (-2e-9, 5e-9, 0.01, 0.025, 0.03, 0.05, 5.5, 1.7)):
    Q1, Q2, r1, r2, r3, r4, er2, er4 = pars
    print(f" parameter set Q1={Q1}, Q2={Q2}, radii={r1},{r2},{r3},{r4}, er2={er2}, er4={er4}")
    C = composite(*pars)
    Qf, Qb = C["Qf"], C["Qb"]
    check("  free: core surface carries Q1", Qf[0], Q1)
    check("  free: shell inner surface carries -Q1", Qf[1], -Q1)
    check("  free: shell outer surface carries Q1+Q2", Qf[2], Q1 + Q2)
    check("  free: shell total = Q2", Qf[1] + Qf[2], Q2)
    # rho_b = -div P = 0 in both dielectrics, by FD
    for rr in (0.5 * (r1 + r2), 0.5 * (r3 + r4)):
        Pv = lambda p, rr=rr: C["P"](rr) * rr**2 * p / np.linalg.norm(p)**3   # P_r ~ 1/r^2 near rr
        p = rr * np.array([0.48, 0.6, 0.64])
        dv = div_fd(Pv, p, 1e-6 * rr)
        check(f"  rho_b = 0 by FD at r={rr:.4g}", dv * rr / abs(C["P"](rr)), 0.0, atol=1e-5)
    # total bound charge of each dielectric = volume (0) + both faces, by numerical integration
    vol_ii = integrate.quad(lambda r: 0.0 * 4 * np.pi * r**2, r1, r2)[0]
    vol_iv = integrate.quad(lambda r: 0.0 * 4 * np.pi * r**2, r3, r4)[0]
    check("  dielectric (ii): total bound charge = 0", vol_ii + Qb[0] + Qb[1], 0.0, atol=1e-12 * abs(Q1))
    check("  dielectric (iv): total bound charge = 0", vol_iv + Qb[2] + Qb[3], 0.0, atol=1e-12 * abs(Q1))
    check("  (ii) inner-face bound total = -(1-1/er2) Q1", Qb[0], -(1 - 1 / er2) * Q1)
    check("  (iv) inner-face bound total = -(1-1/er4)(Q1+Q2)", Qb[2], -(1 - 1 / er4) * (Q1 + Q2))
    # jumps: eps0 [E(r+) - E(r-)] = free + bound surface charge at each radius
    jumps = [(r1, C["f"][0] + C["b"][0]), (r2, C["f"][1] + C["b"][1]),
             (r3, C["f"][2] + C["b"][2]), (r4, C["b"][3])]
    for rr, sig_tot in jumps:
        dE = C["E"](rr * (1 + 1e-12)) - C["E"](rr * (1 - 1e-12))
        check(f"  eps0*jump in E_r at r={rr:g} equals free+bound surface charge", eps0 * dE, sig_tot, rtol=1e-9)
    check("  D_r continuous at r4 (no free charge)", C["D"](r4 * (1 + 1e-12)), C["D"](r4 * (1 - 1e-12)), rtol=1e-9)
    # brute force: superpose ALL surface charges (free + bound) as uniform shells (Coulomb integrals)
    shells = [(r1, Qf[0] + Qb[0]), (r2, Qf[1] + Qb[1]), (r3, Qf[2] + Qb[2]), (r4, Qb[3])]
    for rr in (0.5 * r1, 0.5 * (r1 + r2), 0.5 * (r2 + r3), 0.5 * (r3 + r4), 1.5 * r4):
        Ebf = sum(shell_Ez_axis(Qsh, Rsh, rr) for Rsh, Qsh in shells)
        scale = abs(Q1) / (4 * np.pi * eps0 * r1**2)
        check(f"  brute-force E_r at r={rr:.4g} vs D/eps", Ebf, C["E"](rr), rtol=1e-7, atol=1e-9 * scale)

C = composite(6.0, -8.0, 1.0, 2.0, 3.0, 4.0, 3.0, 2.0)
print(" printed values for the page (Q1=6 C, Q2=-8 C, radii 1,2,3,4 m, 3eps0, 2eps0):")
for rr in (1.5, 3.5, 5.0):
    val(f"  D_r({rr}) * pi r^2", C["D"](rr) * np.pi * rr**2, "C")
    val(f"  E_r({rr}) * pi eps0 r^2", C["E"](rr) * np.pi * eps0 * rr**2, "")
    val(f"  P_r({rr}) * pi r^2", C["P"](rr) * np.pi * rr**2, "C")
val("  D(ii) coefficient 3/(2 pi)", 3 / (2 * np.pi))
val("  free rho_s(r=1) = 3/(2pi)", C["f"][0], "C/m^2")
val("  free rho_s(r=2) = -3/(8pi)", C["f"][1], "C/m^2")
val("  free rho_s(r=3) = -1/(18pi)", C["f"][2], "C/m^2")
val("  bound rho_sb(r=1) = -1/pi", C["b"][0], "C/m^2")
val("  bound rho_sb(r=2) = 1/(4pi)", C["b"][1], "C/m^2")
val("  bound rho_sb(r=3) = 1/(36pi)", C["b"][2], "C/m^2")
val("  bound rho_sb(r=4) = -1/(64pi)", C["b"][3], "C/m^2")
val("  free totals (core, shell inner, shell outer)", C["Qf"], "C")
val("  bound totals (r=1,2,3,4)", C["Qb"], "C")
check("  1/(36pi) - 1/(18pi) = -1/(36pi) = eps0 E_r(3+)", C["f"][2] + C["b"][2], eps0 * C["E"](3.0 + 1e-12))
check("  values: 3/(2pi), -3/(8pi), -1/(18pi)", C["f"], [3 / (2 * np.pi), -3 / (8 * np.pi), -1 / (18 * np.pi)])
check("  values: -1/pi, 1/(4pi), 1/(36pi), -1/(64pi)", C["b"],
      [-1 / np.pi, 1 / (4 * np.pi), 1 / (36 * np.pi), -1 / (64 * np.pi)])
check("  E(ii) = 1/(2 pi eps0 r^2)", C["E"](1.5), 1 / (2 * np.pi * eps0 * 1.5**2))
check("  E(iv) = -1/(4 pi eps0 r^2)", C["E"](3.5), -1 / (4 * np.pi * eps0 * 3.5**2))
check("  E(v) = -1/(2 pi eps0 r^2)", C["E"](5.0), -1 / (2 * np.pi * eps0 * 25.0))
check("  P(ii) = 1/(pi r^2)", C["P"](1.5), 1 / (np.pi * 1.5**2))
check("  P(iv) = -1/(4 pi r^2)", C["P"](3.5), -1 / (4 * np.pi * 3.5**2))
# part (d) of the page: free + bound charge on each surface, and Gauss's law for eps0 E with it
Qf, Qb = C["Qf"], C["Qb"]
Qsurf = np.array([Qf[0] + Qb[0], Qf[1] + Qb[1], Qf[2] + Qb[2], Qb[3]])
Qenc = np.cumsum(Qsurf)
val("  free + bound charge on r = 1, 2, 3, 4", Qsurf, "C")
val("  total charge enclosed for 1<r<2, 2<r<3, 3<r<4, r>4", Qenc, "C")
for rr, Qe in zip((1.5, 2.5, 3.5, 5.0), Qenc):
    check(f"  Gauss with total charge at r={rr}: eps0 E_r 4 pi r^2 = enclosed total",
          eps0 * C["E"](rr) * 4 * np.pi * rr**2, Qe, atol=1e-9)
val("  -(1-1/er) x enclosed free charge, inner faces of (ii), (iv)", [-(1 - 1 / 3.0) * 6.0, -(1 - 1 / 2.0) * (-2.0)], "C")
val("  eps0 E_r(4-)", eps0 * C["E"](4.0 * (1 - 1e-12)), "C/m^2")
val("  eps0 E_r(4+)", eps0 * C["E"](4.0 * (1 + 1e-12)), "C/m^2")
check("  eps0 E_r(4-) = -1/(64pi)", eps0 * C["E"](4.0 * (1 - 1e-12)), -1 / (64 * np.pi), rtol=1e-9)
check("  eps0 E_r(4+) = -1/(32pi)", eps0 * C["E"](4.0 * (1 + 1e-12)), -1 / (32 * np.pi), rtol=1e-9)
note("D, E, P point outward (+r-hat) in (ii) and inward (-r-hat) in (iv), (v)")

# ======================================================================= 8.12
section("8.12  Uniformly (transversely) polarized rod, P = P0 x-hat, radius a")


def rod_field_bf(P0, a, x0, y0):
    """Brute force: 2-D Coulomb field of the bound surface charge P0 cos(phi') on r = a,
    each element a line charge rho_sb a dphi'."""
    def comp(i):
        def f(ph):
            xs, ys = a * np.cos(ph), a * np.sin(ph)
            dx, dy = x0 - xs, y0 - ys
            r2 = dx * dx + dy * dy
            return P0 * np.cos(ph) * a / (2 * np.pi * eps0) * (dx if i == 0 else dy) / r2
        return integrate.quad(f, 0, 2 * np.pi, limit=2000, epsabs=1e-12 * P0 / eps0, epsrel=1e-11)[0]
    return np.array([comp(0), comp(1)])


def rod_dipole_out(P0, a, r, ph):
    Er = P0 * a**2 * np.cos(ph) / (2 * eps0 * r**2)
    Ep = P0 * a**2 * np.sin(ph) / (2 * eps0 * r**2)
    return np.array([Er * np.cos(ph) - Ep * np.sin(ph), Er * np.sin(ph) + Ep * np.cos(ph)])


for (P0, a) in ((1e-6, 0.01), (3e-4, 0.25)):
    print(f" parameter set P0={P0}, a={a}")
    tot = integrate.quad(lambda ph: P0 * np.cos(ph) * a, 0, 2 * np.pi)[0]
    check("  total bound charge per unit length = 0", tot, 0.0, atol=1e-12 * P0 * a)
    Pconst = lambda p: np.array([P0, 0.0, 0.0])
    check("  rho_b = -div P = 0 (FD)", div_fd(Pconst, [0.1 * a, 0.2 * a, 0], 1e-6 * a), 0.0, atol=1e-12)
    # two displaced uniformly charged cylinders, finite d, field in the overlap region
    for dd in (1e-2 * a, 1e-4 * a):
        rhoc = P0 / dd
        for pt in (np.array([0.0, 0.0]), np.array([0.3 * a, -0.5 * a]), np.array([-0.7 * a, 0.1 * a])):
            Eplus = rhoc * (pt - np.array([dd / 2, 0])) / (2 * eps0)
            Eminus = -rhoc * (pt - np.array([-dd / 2, 0])) / (2 * eps0)
            check(f"  two cylinders (d={dd:.1e}) at {pt/a} a: E = -P/(2eps0)", Eplus + Eminus,
                  [-P0 / (2 * eps0), 0.0], rtol=1e-9, atol=1e-9 * P0 / eps0)
    # brute force Coulomb integral of the surface charge, inside
    for pt in ((0.0, 0.0), (0.4 * a, 0.3 * a), (-0.2 * a, -0.6 * a)):
        check(f"  brute-force surface-charge field inside at {np.array(pt)/a} a",
              rod_field_bf(P0, a, *pt), [-P0 / (2 * eps0), 0.0], rtol=1e-7, atol=1e-7 * P0 / eps0)
    # outside: compare to the 2-D dipole field, then the limit r -> a+
    for (r, ph) in ((3 * a, 0.0), (3 * a, np.pi / 2), (2 * a, np.deg2rad(30)), (1.002 * a, 0.0), (1.002 * a, np.pi / 2)):
        check(f"  brute-force outside at r={r/a:g}a, phi={np.rad2deg(ph):.0f} deg vs 2-D dipole",
              rod_field_bf(P0, a, r * np.cos(ph), r * np.sin(ph)), rod_dipole_out(P0, a, r, ph),
              rtol=1e-6, atol=1e-6 * P0 / eps0)
    Ein = np.array([-P0 / (2 * eps0), 0.0])
    for phd in (0.0, 30.0, 90.0, 137.0):
        ph = np.deg2rad(phd)
        nh = np.array([np.cos(ph), np.sin(ph)])
        th = np.array([-np.sin(ph), np.cos(ph)])
        Eo = rod_dipole_out(P0, a, a, ph)
        check(f"  BC at phi={phd:g}: E_t continuous", Eo @ th, Ein @ th, rtol=1e-12, atol=1e-12 * P0 / eps0)
        check(f"  BC at phi={phd:g}: eps0 (E_out,n - E_in,n) = P0 cos(phi)", eps0 * (Eo @ nh - Ein @ nh),
              P0 * np.cos(ph), rtol=1e-12, atol=1e-12 * P0)
        Din = eps0 * Ein + np.array([P0, 0.0])
        check(f"  BC at phi={phd:g}: D_n continuous (no free charge)", eps0 * (Eo @ nh), Din @ nh,
              rtol=1e-12, atol=1e-12 * P0)
    check("  E just outside at phi=0 = +P0/(2eps0) x-hat", rod_dipole_out(P0, a, a, 0.0), [P0 / (2 * eps0), 0.0],
          atol=1e-9 * P0 / eps0)
    check("  E just outside at phi=90 = -P0/(2eps0) x-hat", rod_dipole_out(P0, a, a, np.pi / 2),
          [-P0 / (2 * eps0), 0.0], atol=1e-9 * P0 / eps0)

P0 = 1e-6
val("P0/(2 eps0)", P0 / (2 * eps0), "V/m")
val("E inside = -P0/(2eps0) x-hat, x-component", -P0 / (2 * eps0), "V/m")
val("D inside = eps0 E + P = P0/2 (x-hat)", eps0 * (-P0 / (2 * eps0)) + P0, "C/m^2")
val("E just outside at phi=0, x-component", P0 / (2 * eps0), "V/m")
val("E just outside at phi=90 deg, x-component", -P0 / (2 * eps0), "V/m")
val("E at (3a, 0) = P0/(18 eps0), x-component", P0 / (18 * eps0), "V/m")
check("2-D dipole field at (3a, 0) equals P0/(18 eps0) x-hat", rod_dipole_out(P0, 0.01, 0.03, 0.0),
      [P0 / (18 * eps0), 0.0], atol=1e-9 * P0 / eps0)
check("2-D dipole field at (0, 3a) equals -P0/(18 eps0) x-hat", rod_dipole_out(P0, 0.01, 0.03, np.pi / 2),
      [-P0 / (18 * eps0), 0.0], atol=1e-9 * P0 / eps0)
# comparison: uniformly polarized sphere, field at the centre from surface charge P0 cos(theta)
Ez_sphere = -k_e * P0 * 2 * np.pi * integrate.quad(lambda th: np.cos(th)**2 * np.sin(th), 0, np.pi)[0]
check("sphere: field at centre from P0 cos(theta) surface charge = -P0/(3 eps0)", Ez_sphere, -P0 / (3 * eps0))
check("slab (normal P): field between sheets +-P0 = -P0/eps0", -P0 / eps0, -(P0 / (2 * eps0)) * 2)
val("slab / rod / sphere factors", [1.0, 0.5, 1 / 3.0])

# ======================================================================= summary
print("\n" + "=" * 78)
if FAILS:
    print(f"{len(FAILS)} CHECK(S) FAILED:")
    for f in FAILS:
        print("   ", f)
    raise SystemExit(1)
print("ALL CHECKS PASSED")
