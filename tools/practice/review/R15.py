#!/usr/bin/env python3
"""R15: independent re-solution of content-src/practice/15-inductance-and-magnetic-energy.md.

numpy/scipy only.  Every number printed on the page (final version, after this review's edits)
is transcribed below as the page prints it (converted to SI) and checked:
  sf()    PASS if the computed value rounds to the page's printed digits,
  close() PASS if two independently computed quantities agree to a tight tolerance,
  vec()   directions / vectors (np.cross, finite differences, Biot-Savart sums).
Routes: inductance by flux linkage N*Psi/I AND by energy 2W/I^2 (numerical integrals); RL
transients by solve_ivp; fields from potentials by finite differences; Biot-Savart sums of
straight segments for solenoid, toroid, wire, strips.
"""
import numpy as np
from scipy import integrate, optimize

mu0 = 4e-7*np.pi
eps0 = 8.8541878128e-12
c0 = 1/np.sqrt(mu0*eps0)
X, Y, Z = np.eye(3)

npass = 0
nfail = 0


def _rep(ok, name, msg):
    global npass, nfail
    if ok:
        npass += 1
    else:
        nfail += 1
    print(f"{'PASS' if ok else 'FAIL'}  {name}: {msg}")


def sf(name, computed, stated):
    """PASS if `computed` rounds to the page's printed value `stated` (string, SI)."""
    s = stated.strip().lower()
    mant, _, ex = s.partition('e')
    exp = int(ex) if ex else 0
    digits = mant.lstrip('+-')
    dec = len(digits.split('.')[1]) if '.' in digits else 0
    ulp = 10.0**(exp - dec)
    ok = abs(computed - float(s)) <= 0.5*ulp*(1 + 1e-9)
    _rep(ok, name, f"computed {computed:.6g}, page {stated}")


def close(name, computed, expected, rtol=1e-6, atol=0.0):
    ok = bool(np.isclose(computed, expected, rtol=rtol, atol=atol))
    _rep(ok, name, f"computed {computed:.8g}, expected {expected:.8g}")


def vec(name, computed, expected, atol=1e-9, rtol=1e-6):
    computed = np.asarray(computed, float)
    expected = np.asarray(expected, float)
    ok = bool(np.allclose(computed, expected, atol=atol, rtol=rtol))
    _rep(ok, name, f"computed {np.array2string(computed, precision=6)}, "
                   f"expected {np.array2string(expected, precision=6)}")


def truth(name, cond, msg=""):
    _rep(bool(cond), name, msg)


def info(msg):
    print(f"INFO  {msg}")


def section(t):
    print(f"\n=== {t} ===")


# ---------- finite-difference operators (F(x, y, z, t) -> scalar or 3-vector) ----------
def grad(f, p, t, h=1e-5):
    p = np.asarray(p, float)
    g = np.zeros(3)
    for i in range(3):
        e = np.zeros(3)
        e[i] = h
        g[i] = (f(*(p + e), t) - f(*(p - e), t))/(2*h)
    return g


def jac(F, p, t, h=1e-5):
    p = np.asarray(p, float)
    J = np.zeros((3, 3))
    for j in range(3):
        e = np.zeros(3)
        e[j] = h
        J[:, j] = (np.asarray(F(*(p + e), t)) - np.asarray(F(*(p - e), t)))/(2*h)
    return J  # J[i, j] = dF_i/dx_j


def curl(F, p, t, h=1e-5):
    J = jac(F, p, t, h)
    return np.array([J[2, 1] - J[1, 2], J[0, 2] - J[2, 0], J[1, 0] - J[0, 1]])


def ddt(F, p, t, h=1e-5):
    return (np.asarray(F(*p, t + h)) - np.asarray(F(*p, t - h)))/(2*h)


# ---------- exact Biot-Savart field of straight segments, current I from A to B ----------
def bs_segments(P, A, B, I=1.0):
    d = B - A
    dh = d/np.linalg.norm(d, axis=1)[:, None]
    r1 = P - A
    r2 = P - B
    cr = np.cross(dh, r1)                       # direction dl x R (R from source to P)
    rho2 = np.sum(cr**2, axis=1)
    f = (np.sum(dh*r1, axis=1)/np.linalg.norm(r1, axis=1)
         - np.sum(dh*r2, axis=1)/np.linalg.norm(r2, axis=1))
    return mu0*I/(4*np.pi)*np.sum((f/rho2)[:, None]*cr, axis=0)


# =========================================================================================
section("15.1 long solenoid: L by flux linkage and by energy")


def solenoid_L(N, ell, a):
    n = N/ell
    psi1 = integrate.quad(lambda r: mu0*n*2*np.pi*r, 0, a)[0]               # flux/turn per A
    w1 = integrate.quad(lambda r: 0.5*mu0*n**2*2*np.pi*r*ell, 0, a)[0]      # energy at 1 A
    return N*psi1, 2*w1


N1, ell1, a1, I1 = 500, 0.25, 0.01, 2.0
Lf1, Le1 = solenoid_L(N1, ell1, a1)
sf("15.1(a) L, flux route N*Psi/I [H]", Lf1, "0.395e-3")
sf("15.1(a) L, energy route 2W/I^2 [H]", Le1, "0.395e-3")
close("15.1(a) L = 4 pi^2 x 1e-5 H", Lf1, 4*np.pi**2*1e-5)
zk = (np.arange(N1) + 0.5)*ell1/N1 - ell1/2
Bc = np.sum(mu0*I1*a1**2/(2*(a1**2 + zk**2)**1.5))
info(f"15.1 Biot-Savart sum of {N1} loops: B at centre {Bc:.6g} T vs mu0 n I {mu0*N1/ell1*I1:.6g} T "
     f"(ratio {Bc/(mu0*N1/ell1*I1):.5f}); the ideal formula is intended ('ignore end effects')")
sf("15.1(b)(i) L, 1000 turns on 25 cm [H]", solenoid_L(1000, 0.25, a1)[0], "1.58e-3")
sf("15.1(b)(ii) L, 500 turns on 50 cm [H]", solenoid_L(500, 0.50, a1)[1], "0.197e-3")
H1 = N1/ell1*I1
sf("15.1(c) H = nI [A/m]", H1, "4000")
sf("15.1(c) w = 1/2 mu0 H^2 [J/m^3]", 0.5*mu0*H1**2, "10.1")
close("15.1(c) w = 3.2 pi", 0.5*mu0*H1**2, 3.2*np.pi)
sf("15.1(c) interior volume [m^3]", np.pi*a1**2*ell1, "7.85e-5")
Wfield1 = integrate.quad(lambda r: 0.5*mu0*H1**2*2*np.pi*r*ell1, 0, a1)[0]
sf("15.1(c) W = 1/2 L I^2 [J]", 0.5*Lf1*I1**2, "0.790e-3")
sf("15.1(c) W = int 1/2 mu0 H^2 dV [J]", Wfield1, "0.790e-3")
close("15.1(c) W = 8 pi^2 x 1e-5 J", Wfield1, 8*np.pi**2*1e-5)

# =========================================================================================
section("15.2 shorted coil: ODE L dI/dt = -R I")
L2, I02, R2 = 40e-3, 2.0, 8.0
s2 = integrate.solve_ivp(lambda t, y: [-R2*y[0]/L2, R2*y[0]**2], [0, 0.25], [I02, 0.0],
                         method='DOP853', rtol=1e-12, atol=1e-14, dense_output=True)
I2f = lambda t: s2.sol(t)[0]
tau2 = optimize.brentq(lambda t: I2f(t) - I02/np.e, 1e-6, 0.05, xtol=1e-15)
close("15.2(a) tau (1/e time of the ODE) = 5 ms", tau2, 5e-3, rtol=1e-7)
tt = np.linspace(0, 0.03, 13)
vec("15.2(a) I(t) = 2 exp(-200 t) A", I2f(tt), 2*np.exp(-200*tt), atol=1e-9)
Itau2 = I2f(tau2)
sf("15.2(b) I(tau) [A]", Itau2, "0.736")
VL2 = L2*(-R2*Itau2/L2)          # L dI/dt with dI/dt from the ODE right-hand side
sf("15.2(b) V = L dI/dt [V]", VL2, "-5.89")
sf("15.2(b) self-emf -L dI/dt [V]", -VL2, "5.89")
sf("15.2(b) R I [V]", R2*Itau2, "5.89")
W02 = 0.5*L2*I02**2
Wt2 = 0.5*L2*Itau2**2
sf("15.2(c) W0 [J]", W02, "80e-3")
sf("15.2(c) W(tau) [J]", Wt2, "10.8e-3")
sf("15.2(c) W(tau)/W0", Wt2/W02, "0.135")
th2 = optimize.brentq(lambda t: 0.5*L2*I2f(t)**2 - W02/2, 1e-7, 0.02, xtol=1e-15)
sf("15.2(c) half-energy time [s]", th2, "1.73e-3")
close("15.2(c) half-energy time = (tau/2) ln 2", th2, 2.5e-3*np.log(2), rtol=1e-7)
sf("15.2(c) I at that time [A]", I2f(th2), "1.41")
sf("15.2 check: heat int I^2 R dt [J]", s2.sol(0.25)[1], "0.08")
close("15.2 check: heat = W0", s2.sol(0.25)[1], W02, rtol=1e-6)

# =========================================================================================
section("15.3 fields from given potentials (finite differences); page: A = -4yt y^ + 5x z^")
kz = 5.0
Phi3 = lambda x, y, z, t: 2*y**2
A3 = lambda x, y, z, t: np.array([0.0, -4*y*t, kz*x])
rng = np.random.default_rng(329)
pts = rng.uniform(-2, 2, size=(6, 3))
tms = rng.uniform(0, 3, size=6)
match = {k: True for k in 'abcd'}
for p, t in zip(pts, tms):
    E = -grad(Phi3, p, t) - ddt(A3, p, t)
    B = curl(A3, p, t)
    y = p[1]
    opts = {'a': (np.zeros(3), [0, -5, 0]), 'b': ([0, -4*y, 0], [0, -5, 0]),
            'c': (np.zeros(3), [0, 5, 0]), 'd': ([0, -8*y, 0], [0, -5, 0])}
    for k, (Eo, Bo) in opts.items():
        if not (np.allclose(E, Eo, atol=1e-6) and np.allclose(B, Bo, atol=1e-6)):
            match[k] = False
truth("15.3 key (a) E = 0, B = -5 y^ T is the only option matching FD fields at 6 random (r,t)",
      match['a'] and not (match['b'] or match['c'] or match['d']), str(match))
p, t = pts[0], tms[0]
y = p[1]
vec("15.3 distractor (b) = -grad Phi only", -grad(Phi3, p, t), [0, -4*y, 0], atol=1e-6)
J3 = jac(A3, p, t)
close("15.3 distractor (c) = reversed curl_y (dAz/dx - dAx/dz)", J3[2, 0] - J3[0, 2], 5.0, rtol=1e-8)
vec("15.3 distractor (d) = -grad Phi + dA/dt", -grad(Phi3, p, t) + ddt(A3, p, t), [0, -8*y, 0], atol=1e-6)
vec("15.3 curl x and z components vanish", curl(A3, p, t)[[0, 2]], [0, 0], atol=1e-6)
lam3 = lambda x, y, z, t: -2*y**2*t
vec("15.3 gauge: grad(-2y^2 t) = -4yt y^", grad(lam3, p, t), [0, -4*y*t, 0], atol=1e-6)
close("15.3 gauge: -d lambda/dt = Phi", -(lam3(*p, t + 1e-5) - lam3(*p, t - 1e-5))/2e-5, Phi3(*p, t), rtol=1e-7)
vec("15.3 static pair: curl(5x z^) = -5 y^", curl(lambda x, y, z, t: np.array([0, 0, kz*x]), p, t), [0, -5, 0], atol=1e-6)
E3 = lambda x, y, z, t: -grad(Phi3, (x, y, z), t) - ddt(A3, (x, y, z), t)
vec("15.3 check: curl E = 0", curl(E3, p, t, h=1e-3), np.zeros(3), atol=1e-5)
vec("15.3 check: dB/dt = 0", (curl(A3, p, t + 1e-3) - curl(A3, p, t - 1e-3))/2e-3, np.zeros(3), atol=1e-5)
# exam comparison (SP18 E2 #1(v): Phi = 3x^2, A = -6xt x^ + 3y y^; key: (a) both E and B zero)
PhiX = lambda x, y, z, t: 3*x**2
AX = lambda x, y, z, t: np.array([-6*x*t, 3*y, 0.0])
vec("15.3 re-param: exam potentials give E = 0", -grad(PhiX, p, t) - ddt(AX, p, t), np.zeros(3), atol=1e-6)
vec("15.3 re-param: exam potentials give B = 0 (key 'both zero')", curl(AX, p, t), np.zeros(3), atol=1e-6)
truth("15.3 re-param: page B != 0, so the exam key does not carry over",
      np.linalg.norm(curl(A3, p, t)) > 1)
info("15.3 re-param: exam coefficients {3, -6, 3}; page {2, -4, 5} (static term was 3x z^, "
     "repeating the exam's 3, before this review); gauge axis x -> y; static term curl-free -> B != 0")

# =========================================================================================
section("15.4 gauge transformations, true/false (finite differences)")
B0 = 0.7
pairs = {'a': (lambda x, y, z, t: 0.0, lambda x, y, z, t: np.array([-B0*y, 0.0, 0.0]), True),
         'b': (lambda x, y, z, t: 0.0, lambda x, y, z, t: np.array([0.0, B0*x, 2*t]), False),
         'c': (lambda x, y, z, t: -2*z, lambda x, y, z, t: np.array([0.0, B0*x, 2*t]), True),
         'd': (lambda x, y, z, t: 0.0, lambda x, y, z, t: np.array([B0*y, 0.0, 0.0]), False)}
A40 = lambda x, y, z, t: np.array([0.0, B0*x, 0.0])
vec("15.4 reference pair: B = B0 z^", curl(A40, pts[1], 0.3), [0, 0, B0], atol=1e-6)
for k, (Ph, Ap, key) in pairs.items():
    same = True
    for p, t in zip(pts, tms):
        E = -grad(Ph, p, t) - ddt(Ap, p, t)
        same &= np.allclose(E, 0, atol=1e-6) and np.allclose(curl(Ap, p, t), [0, 0, B0], atol=1e-6)
    truth(f"15.4({k}) page key {'true' if key else 'false'}", same == key, f"FD: same fields = {same}")
p, t = pts[2], tms[2]
vec("15.4(b) E' = -2 z^ V/m", -grad(pairs['b'][0], p, t) - ddt(pairs['b'][1], p, t), [0, 0, -2], atol=1e-6)
vec("15.4(d) B' = -B0 z^", curl(pairs['d'][1], p, t), [0, 0, -B0], atol=1e-6)
vec("15.4(d) curl(A'-A) = -2 B0 z^", curl(lambda x, y, z, t: pairs['d'][1](x, y, z, t) - A40(x, y, z, t), p, t),
    [0, 0, -2*B0], atol=1e-6)
vec("15.4(a) A + grad(-B0 x y) = A'", A40(*p, t) + grad(lambda x, y, z, t: -B0*x*y, p, t), pairs['a'][1](*p, t),
    atol=1e-6)
lamc = lambda x, y, z, t: 2*z*t
vec("15.4(c) grad(2zt) = 2t z^", grad(lamc, p, t), [0, 0, 2*t], atol=1e-6)
close("15.4(c) -d(2zt)/dt = -2z = Phi'", -(lamc(*p, t + 1e-5) - lamc(*p, t - 1e-5))/2e-5, -2*p[2], rtol=1e-7)

# =========================================================================================
section("15.5 two-wire line, find the error")
a5, D5, I5 = 1e-3, 1e-2, 1.0
Lw5 = 100.0


def wireB(P, x0, sgn, I=I5):   # long straight wire at (x0, 0) carrying I along sgn*z^
    return bs_segments(np.asarray(P, float), np.array([[x0, 0, -sgn*Lw5]]), np.array([[x0, 0, sgn*Lw5]]), I)


vec("15.5 wire 1 in the gap: z^ x x^ = +y^", np.cross(Z, X), Y)
vec("15.5 wire 2 in the gap: (-z^) x (-x^) = +y^", np.cross(-Z, -X), Y)
b1 = wireB([0.3*D5, 0, 0], 0.0, +1)
b2 = wireB([0.3*D5, 0, 0], D5, -1)
truth("15.5 Biot-Savart: both wires give +y^ at x = 0.3D", b1[1] > 0 and b2[1] > 0
      and abs(b1[0]) + abs(b2[0]) + abs(b1[2]) + abs(b2[2]) < 1e-15, f"B1 = {b1}, B2 = {b2}")
Lstud = integrate.quad(lambda x: wireB([x, 0, 0], 0.0, +1)[1], a5, D5 - a5, epsrel=1e-11)[0]/I5
Lcorr = integrate.quad(lambda x: wireB([x, 0, 0], 0.0, +1)[1] + wireB([x, 0, 0], D5, -1)[1],
                       a5, D5 - a5, epsrel=1e-11)[0]/I5
sf("15.5 student's value, wire 1 only [H/m]", Lstud, "0.44e-6")
sf("15.5(a) corrected L' (both wires, flux between surfaces) [H/m]", Lcorr, "0.879e-6")
sf("15.5 ln 9", np.log(9), "2.197")
close("15.5(a) corrected = 2 x student", Lcorr/Lstud, 2.0, rtol=1e-7)


def H2w(x, y):
    r1s = x*x + y*y
    r2s = (x - D5)**2 + y*y
    return (I5/(2*np.pi)*(-y/r1s + y/r2s), I5/(2*np.pi)*(x/r1s - (x - D5)/r2s))


Rmax5 = 1e5*D5
fen = lambda u, th: 0.5*mu0*sum(hh*hh for hh in H2w(np.exp(u)*np.cos(th), np.exp(u)*np.sin(th)))*np.exp(2*u)
up5 = lambda th: min(np.log((D5/2)/np.cos(th)), np.log(Rmax5)) if np.cos(th) > 1e-12 else np.log(Rmax5)
Wl = (integrate.dblquad(fen, -np.pi/2, np.pi/2, lambda th: np.log(a5), up5, epsrel=1e-9)[0]
      + integrate.dblquad(fen, np.pi/2, 3*np.pi/2, lambda th: np.log(a5), lambda th: np.log(Rmax5), epsrel=1e-9)[0])
Len5 = 2*(2*Wl)/I5**2
info(f"15.5 energy route with the same line-current fields, outside both wires: 2W'/I^2 = {Len5*1e6:.4f} uH/m "
     f"(~(mu0/pi)ln(D/a) = {mu0/np.pi*np.log(D5/a5)*1e6:.4f}); exact two-wire (mu0/pi)arccosh(D/2a) = "
     f"{mu0/np.pi*np.arccosh(D5/(2*a5))*1e6:.4f} uH/m. The page's 0.879 is the 'flux between the surfaces' "
     f"approximation the statement prescribes (about 4-5 % low); not an error.")
sf("15.5 note: exact (mu0/pi)arccosh(D/2a) above 0.879 [%]", 100*(mu0/np.pi*np.arccosh(D5/(2*a5))/Lcorr - 1), "4")
sf("15.5 note: DC energy route (line-current fields outside both wires) above 0.879 [%]", 100*(Len5/Lcorr - 1), "5")
rl5 = 1.0
V5 = integrate.quad(lambda x: rl5/(2*np.pi*eps0)*(1/x + 1/(D5 - x)), a5, D5 - a5)[0]
C5 = rl5/V5
sf("15.5(b) C' (line charges, V between surfaces) [F/m]", C5, "12.7e-12")
close("15.5(b) C' = pi eps0/ln9", C5, np.pi*eps0/np.log(9))
sf("15.5(b) L'C' corrected [s^2/m^2]", Lcorr*C5, "1.11e-17")
close("15.5(b) L'C' = mu0 eps0", Lcorr*C5, mu0*eps0, rtol=1e-7)
close("15.5(b) student's L'C' = mu0 eps0 / 2", Lstud*C5, mu0*eps0/2, rtol=1e-7)
sf("15.5(b) student's 1/sqrt(L'C') [m/s]", 1/np.sqrt(Lstud*C5), "4.24e8")

# =========================================================================================
section("15.6 RL switch-on: ODE L dI/dt = V0 - R I")
V0, L6, R6 = 12.0, 0.2, 10.0
rhs6 = lambda t, y: [(V0 - R6*y[0])/L6, V0*y[0], R6*y[0]**2]   # I, battery energy, heat
s6 = integrate.solve_ivp(rhs6, [0, 1.0], [0, 0, 0], method='DOP853', rtol=1e-12, atol=1e-14, dense_output=True)
I6 = lambda t: s6.sol(t)[0]
tau6 = optimize.brentq(lambda t: I6(t) - 1.2*(1 - 1/np.e), 1e-6, 0.2, xtol=1e-15)
close("15.6(a) tau (63.2 % time of the ODE) = 20 ms", tau6, 0.02, rtol=1e-7)
tt = np.linspace(0, 0.1, 11)
vec("15.6(a) I(t) = 1.2(1 - exp(-50 t)) A", I6(tt), 1.2*(1 - np.exp(-50*tt)), atol=1e-9)
It6 = I6(tau6)
dI6 = (V0 - R6*It6)/L6
sf("15.6(b) I(tau) [A]", It6, "0.759")
sf("15.6(b) V_R [V]", R6*It6, "7.59")
sf("15.6(b) V_L [V]", L6*dI6, "4.41")
close("15.6(b) V_R + V_L = 12 V", R6*It6 + L6*dI6, 12.0)
W6 = 0.5*L6*It6**2
sf("15.6(c) W [J]", W6, "57.5e-3")
sf("15.6(c) I(tau) to 4 s.f. as displayed [A]", It6, "0.7585")
sf("15.6(c) literal 1/2(0.2)(0.7585)^2 [J]", 0.5*0.2*0.7585**2, "57.5e-3")
info(f"15.6 old literal 1/2(0.2)(0.759)^2 = {0.5*0.2*0.759**2*1e3:.2f} mJ (page said 57.5; fixed to 0.7585)")
Pb, PR, dW6 = V0*It6, It6**2*R6, L6*It6*dI6
sf("15.6(c) P_battery [W]", Pb, "9.10")
sf("15.6(c) P_R [W]", PR, "5.75")
sf("15.6(c) dW/dt [W]", dW6, "3.35")
dWnum = (0.5*L6*I6(tau6 + 1e-6)**2 - 0.5*L6*I6(tau6 - 1e-6)**2)/2e-6
close("15.6(c) dW/dt from numerical derivative of 1/2 L I(t)^2", dWnum, dW6, rtol=1e-6)
close("15.6(c) balance P_battery = P_R + dW/dt", Pb, PR + dW6)
close("15.6(c) integrated: battery energy - heat = 1/2 L I^2 at tau", s6.sol(tau6)[1] - s6.sol(tau6)[2], W6, rtol=1e-8)
Winf6 = 0.5*L6*(V0/R6)**2
sf("15.6(d) W_inf [J]", Winf6, "144e-3")
th6 = optimize.brentq(lambda t: 0.5*L6*I6(t)**2 - Winf6/2, 1e-6, 0.2, xtol=1e-15)
sf("15.6(d) half-energy time [s]", th6, "24.6e-3")
sf("15.6(d) t/tau", th6/tau6, "1.228")
sf("15.6 watch-out: half-current time [s]", optimize.brentq(lambda t: I6(t) - 0.6, 1e-6, 0.2, xtol=1e-15), "13.9e-3")
close("15.6 check: V_L(0+) = V0", L6*rhs6(0, [0, 0, 0])[0], 12.0)
close("15.6 check: I(inf) = 1.2 A", I6(1.0), 1.2, rtol=1e-9)

# =========================================================================================
section("15.7 internal inductance of a round wire")
I7 = 1.0
for a7 in (1e-3, 4e-3):
    J7 = I7/(np.pi*a7**2)
    Ienc7 = lambda r: integrate.quad(lambda rp: J7*2*np.pi*rp, 0, min(r, a7))[0]
    H7 = lambda r: Ienc7(r)/(2*np.pi*r)
    tag = f"a = {a7*1e3:g} mm"
    for fr in (0.3, 0.8):
        close(f"15.7(a) H(r = {fr}a) by Ampere = I r/(2 pi a^2), {tag}", H7(fr*a7), I7*fr*a7/(2*np.pi*a7**2), rtol=1e-9)
    Wp7 = integrate.quad(lambda r: 0.5*mu0*H7(r)**2*2*np.pi*r, 0, a7, epsrel=1e-12)[0]
    sf(f"15.7(b) W' at 1 A, {tag} [J/m]", Wp7, "2.5e-8")
    sf(f"15.7(b) L'_int = 2W'/I^2, {tag} [H/m]", 2*Wp7/I7**2, "50e-9")
    close(f"15.7(b) L'_int = mu0/(8 pi), {tag}", 2*Wp7/I7**2, mu0/(8*np.pi), rtol=1e-8)
    sf(f"15.7(c) strip flux / I, {tag} [H/m]", integrate.quad(lambda r: mu0*H7(r), 0, a7)[0]/I7, "100e-9")
    close(f"15.7(c) flux weighted by enclosed fraction / I = mu0/(8 pi), {tag}",
          integrate.quad(lambda r: (Ienc7(r)/I7)*mu0*H7(r), 0, a7)[0]/I7, mu0/(8*np.pi), rtol=1e-8)
Lint7 = mu0/(8*np.pi)
Lext5 = mu0/np.pi*np.log(9)
sf("15.7(d) L' with both internal terms [H/m]", Lext5 + 2*Lint7, "0.979e-6")
sf("15.7(d) increase [%]", 100*2*Lint7/Lext5, "11")

# =========================================================================================
section("15.8 two coaxial solenoids")
l8, a8, b8, n81, n82 = 0.5, 0.01, 0.02, 2000, 1000
N81, N82 = n81*l8, n82*l8
sf("15.8 N1", N81, "1000")
sf("15.8 N2", N82, "500")
B81 = lambda r: mu0*n81*(r < a8)      # per ampere
B82 = lambda r: mu0*n82*(r < b8)
L81f = N81*integrate.quad(lambda r: B81(r)*2*np.pi*r, 0, a8)[0]
L81e = 2*l8*integrate.quad(lambda r: 0.5*B81(r)**2/mu0*2*np.pi*r, 0, a8)[0]
L82f = N82*integrate.quad(lambda r: B82(r)*2*np.pi*r, 0, b8)[0]
L82e = 2*l8*integrate.quad(lambda r: 0.5*B82(r)**2/mu0*2*np.pi*r, 0, b8)[0]
for nm, v in [("L1 flux route", L81f), ("L1 energy route", L81e), ("L2 flux route", L82f), ("L2 energy route", L82e)]:
    sf(f"15.8(a) {nm} [H]", v, "0.790e-3")
close("15.8(a) L1 = 0.8 pi^2 x 1e-4 H", L81f, 0.8*np.pi**2*1e-4)
M81 = N82*integrate.quad(lambda r: B81(r)*2*np.pi*r, 0, b8, points=[a8])[0]
M82 = N81*integrate.quad(lambda r: B82(r)*2*np.pi*r, 0, a8)[0]
M8e = l8*integrate.quad(lambda r: B81(r)*B82(r)/mu0*2*np.pi*r, 0, b8, points=[a8])[0]   # int mu0 H1.H2 dV = M I1 I2
sf("15.8(b) M route 1 (inner field through outer turns) [H]", M81, "0.395e-3")
sf("15.8(b) M route 2 (outer field through inner turns) [H]", M82, "0.395e-3")
sf("15.8(b) M from interaction energy int mu0 H1.H2 dV [H]", M8e, "0.395e-3")
close("15.8(b) M = 0.4 pi^2 x 1e-4 H", M81, 0.4*np.pi**2*1e-4)
sf("15.8(c) |emf| = M dI1/dt [V]", M81*100, "39.5e-3")
for sgn, nm, st in [(+1, "aiding", "2.37e-3"), (-1, "opposing", "0.790e-3")]:
    H8 = lambda r: (n81 + sgn*n82)*(r < a8) + n82*((r >= a8) & (r < b8))
    W8 = l8*integrate.quad(lambda r: 0.5*mu0*H8(r)**2*2*np.pi*r, 0, b8, points=[a8])[0]
    sf(f"15.8(d) L_{nm} = 2W/I^2 [H]", 2*W8, st)
    close(f"15.8(d) L_{nm} = L1 + L2 {'+' if sgn > 0 else '-'} 2M", 2*W8, L81f + L82f + sgn*2*M81, rtol=1e-8)
sf("15.8 check: k = M/sqrt(L1 L2)", M81/np.sqrt(L81f*L82f), "0.5")

# =========================================================================================
section("15.9 toroid with a two-layer core")
N9, a9, b9, h9, I9 = 1000, 0.05, 0.10, 0.02, 2.0
mu9 = lambda z: 9*mu0 if z < h9/2 else mu0
ph = 2*np.pi*np.arange(N9)/N9
cph, sph, zer = np.cos(ph), np.sin(ph), np.zeros(N9)
P1 = np.stack([a9*cph, a9*sph, zer], 1)          # bottom of inner face
P2 = np.stack([a9*cph, a9*sph, zer + h9], 1)     # up the inner face (+z^)
P3 = np.stack([b9*cph, b9*sph, zer + h9], 1)     # outward along the top
P4 = np.stack([b9*cph, b9*sph, zer], 1)          # down the outer face, then inward along the bottom
SA, SB = np.vstack([P1, P2, P3, P4]), np.vstack([P2, P3, P4, P1])
phf = np.pi/N9
phat = np.array([-np.sin(phf), np.cos(phf), 0.0])
Htor = lambda r, z: bs_segments(np.array([r*np.cos(phf), r*np.sin(phf), z]), SA, SB, I9)/mu0
info("15.9 Biot-Savart of the free currents (1000 closed rectangular turns); H does not depend on mu "
     "here (field tangential to the layer interface, Ampere has no mu)")
for r, z in [(0.06, 0.005), (0.075, 0.015), (0.095, 0.005)]:
    H = Htor(r, z)
    close(f"15.9(a) H_phi at r = {r} m, z = {z} m vs NI/(2 pi r)", H @ phat, N9*I9/(2*np.pi*r), rtol=2e-3)
    truth(f"15.9(a) H along +phi^ at r = {r} m", np.linalg.norm(H - (H @ phat)*phat) < 1e-3*np.linalg.norm(H), f"H = {H}")
for r, z, where in [(0.03, 0.01, "in the hole r < a"), (0.13, 0.01, "outside r > b"), (0.075, 0.035, "above the core")]:
    H = Htor(r, z)
    truth(f"15.9(a) H ~ 0 {where}", np.linalg.norm(H) < 1e-3*N9*I9/(2*np.pi*r), f"|H| = {np.linalg.norm(H):.3g} A/m")
close("15.9(a) H_phi equal just below/above the interface z = h/2", Htor(0.075, h9/2 - 1e-4) @ phat,
      Htor(0.075, h9/2 + 1e-4) @ phat, rtol=1e-3)
sf("15.9(a) H(r = a) [A/m]", N9*I9/(2*np.pi*a9), "6366")
sf("15.9(a) H(r = b) [A/m]", N9*I9/(2*np.pi*b9), "3183")
vec("15.9(b) turn normal: z^ (up inner face) x r^ (outward on top) = phi^ (at phi = 0)", np.cross(Z, X), Y)


def toroid(N):
    psi = sum(integrate.dblquad(lambda r, z: mu9(z)*N*I9/(2*np.pi*r), z0, z1, lambda z: a9, lambda z: b9,
                                epsrel=1e-11)[0] for z0, z1 in [(0, h9/2), (h9/2, h9)])
    return N*I9/(2*np.pi*0.075), psi, N*psi, N*psi/I9


_, Psi9, NPsi9, L9 = toroid(N9)
sf("15.9(b) mu0 N h/(2 pi) [Wb/A]", mu0*N9*h9/(2*np.pi), "4e-6")
sf("15.9(b) Psi/I per turn [Wb/A]", Psi9/I9, "1.39e-5")
sf("15.9(b) Psi/I to 4 s.f. as displayed [Wb/A]", Psi9/I9, "1.386e-5")
sf("15.9(b) literal (1.386e-5)(2) [Wb]", 1.386e-5*2, "2.77e-5")
sf("15.9(b) Psi per turn at 2 A [Wb]", Psi9, "2.77e-5")
sf("15.9(b) N Psi [Wb]", NPsi9, "2.77e-2")
sf("15.9(b) L = N Psi/I [H]", L9, "13.9e-3")
L9air = mu0*N9**2*h9*np.log(b9/a9)/(2*np.pi)
sf("15.9(b) all-air L [H]", L9air, "2.77e-3")
close("15.9(b) L/L_air = 5 (area-average mu_r)", L9/L9air, 5.0, rtol=1e-8)
sf("15.9(b) V = L dI/dt at 50 A/s [V]", L9*50, "0.693")
sf("15.9(b) L to 4 s.f. as displayed [H]", L9, "13.86e-3")
sf("15.9(b) literal (13.86 mH)(50 A/s) [V]", 13.86e-3*50, "0.693")
sf("15.9(c) literal 1/2(13.86 mH)(2 A)^2 [J]", 0.5*13.86e-3*4, "27.7e-3")
info(f"15.9 old literals: (1.39e-5)(2) = {1.39e-5*2:.3g}, (13.9 mH)(50) = {13.9e-3*50:.4g} V, 1/2(13.9 mH)(4) = {0.5*13.9e-3*4*1e3:.3g} mJ (page said 2.77e-5, 0.693, 27.7)")
Wf9 = integrate.dblquad(lambda r, z: 0.5*9*mu0*(N9*I9/(2*np.pi*r))**2*2*np.pi*r, 0, h9/2,
                        lambda z: a9, lambda z: b9, epsrel=1e-11)[0]
Wa9 = integrate.dblquad(lambda r, z: 0.5*mu0*(N9*I9/(2*np.pi*r))**2*2*np.pi*r, h9/2, h9,
                        lambda z: a9, lambda z: b9, epsrel=1e-11)[0]
sf("15.9(c) W = 1/2 L I^2 [J]", 0.5*L9*I9**2, "27.7e-3")
sf("15.9(c) W in ferrite by int 1/2 mu H^2 dV [J]", Wf9, "24.95e-3")
sf("15.9(c) W in air [J]", Wa9, "2.77e-3")
sf("15.9(c) W total by int 1/2 mu H^2 dV [J]", Wf9 + Wa9, "27.7e-3")
sf("15.9(c) ferrite share [%]", 100*Wf9/(Wf9 + Wa9), "90")
close("15.9 check: 2W/I^2 = N Psi/I", 2*(Wf9 + Wa9)/I9**2, L9, rtol=1e-9)
q1, q2 = toroid(1000), toroid(500)
for nm, i, st in [("|B|", 0, "0.5"), ("Psi per turn", 1, "0.5"), ("N Psi", 2, "0.25"), ("L", 3, "0.25")]:
    sf(f"15.9(d) {nm} factor for N = 500", q2[i]/q1[i], st)
info(f"15.9 re-param: exam #2 is symbolic (key psi1 = mu0 N I h ln(b/a)/2pi); with the two-layer core the page's "
     f"Psi, N Psi, L and V are {L9/L9air:.0f}x the key's formula; the key's formula only reappears as the "
     f"all-air comparison in (b)")

# =========================================================================================
section("15.10 shorted parallel-plate line, gap filled with mu = 3 mu0, eps = 3 eps0")
W10, d10, l10, I10 = 0.05, 2e-3, 1.0, 10.0
mu10, ep10 = 3*mu0, 3*eps0


def Hsheets(yy, W=W10, d=d10, I=I10):          # sheet rule H = 1/2 Js x n^, n^ toward the field point
    Js = I/W
    return 0.5*np.cross(Js*X, np.sign(yy - d)*Y) + 0.5*np.cross(-Js*X, np.sign(yy)*Y)


sf("15.10(a) Js = I/W [A/m]", I10/W10, "200")
vec("15.10(a) top-sheet term between: 1/2 (200 x^) x (-y^)", 0.5*np.cross(200*X, -Y), [0, 0, -100])
vec("15.10(a) bottom-sheet term between: 1/2 (-200 x^) x y^", 0.5*np.cross(-200*X, Y), [0, 0, -100])
vec("15.10(a) H between [A/m]", Hsheets(d10/2), [0, 0, -200])
vec("15.10(a) H above both", Hsheets(3*d10), [0, 0, 0])
vec("15.10(a) H below both", Hsheets(-d10), [0, 0, 0])


def Hstrips(yy, zz, Wst, I=I10):    # 2-D Biot-Savart: filaments along x on y = d (+x^) and y = 0 (-x^)
    K = I/Wst
    out = np.zeros(3)
    for ys, sg in [(d10, +1.0), (0.0, -1.0)]:
        for k in range(3):
            f = lambda zp: sg*K/(2*np.pi)*np.cross(X, [0, yy - ys, zz - zp])[k]/((yy - ys)**2 + (zz - zp)**2)
            out[k] += integrate.quad(f, 0, Wst, points=[zz], limit=500, epsabs=1e-11)[0]
    return out


vec("15.10(a) Biot-Savart, very wide strips (W = 1000 d, Js = 200 A/m): H between", Hstrips(d10/2, 500*d10, 1000*d10, I=200*1000*d10),
    [0, 0, -200], atol=0.5, rtol=0)
truth("15.10(a) Biot-Savart, very wide strips: H above ~ 0", np.linalg.norm(Hstrips(2*d10, 500*d10, 1000*d10, I=200*1000*d10)) < 0.5)
Hreal = Hstrips(d10/2, W10/2, W10)
info(f"15.10 at the real W/d = 25 the vacuum strips give H_z = {Hreal[2]:.1f} A/m at the centre "
     f"({100*(1 + Hreal[2]/200):.1f} % fringing; ignored as the statement says)")
vec("15.10(a) BC at top strip: y^ x (H_above - H_between) = Js,top", np.cross(Y, Hsheets(2*d10) - Hsheets(d10/2)), 200*X)
Bgap = mu10*Hsheets(d10/2)
sf("15.10(a) |B| in the film [T]", -Bgap[2], "7.54e-4")
vec("15.10(a) B direction", np.sign(Bgap), [0, 0, -1])
verts = np.array([[0, d10], [l10, d10], [l10, 0], [0, 0]])     # source -> top -> short -> bottom (x-y plane)
area = 0.5*np.sum(verts[:, 0]*np.roll(verts[:, 1], -1) - np.roll(verts[:, 0], -1)*verts[:, 1])
truth("15.10(b) current path clockwise seen from +z (signed area < 0)", area < 0, f"signed area {area:.3g} m^2")
vec("15.10(b) dS: x^ (top) x (-y^) (short) = -z^", np.cross(X, -Y), -Z)


def plate_numbers(W, d, I):
    psi = integrate.dblquad(lambda yy, xx: (mu10*Hsheets(yy, W, d, I)) @ (-Z), 0, l10, lambda xx: 0, lambda xx: d)[0]
    wm = integrate.tplquad(lambda zz, yy, xx: 0.5*mu10*np.sum(Hsheets(yy, W, d, I)**2), 0, l10,
                           lambda xx: 0, lambda xx: d, lambda xx, yy: 0, lambda xx, yy: W)[0]
    Q = 1e-9                                       # Gauss: D = rho_s between the strips, V = int E dy
    V = integrate.quad(lambda yy: Q/(W*l10)/ep10, 0, d)[0]
    return mu10*I/W, psi, psi/I, Q/V/l10, wm


Bm, Psi10, L10, C10, Wm10 = plate_numbers(W10, d10, I10)
sf("15.10(b) Psi [Wb]", Psi10, "1.51e-6")
sf("15.10(b) L = Psi/I [H]", L10, "151e-9")
sf("15.10(b) L' = L/l [H/m]", L10/l10, "151e-9")
sf("15.10(c) W_m = int 1/2 mu H^2 dV [J]", Wm10, "7.54e-6")
sf("15.10(c) 1/2 L I^2 [J]", 0.5*L10*I10**2, "7.54e-6")
sf("15.10(c) L to 4 s.f. as displayed [H]", L10, "150.8e-9")
sf("15.10(c) literal 1/2(150.8 nH)(10 A)^2 [J]", 0.5*150.8e-9*100, "7.54e-6")
sf("15.10(c) literal 1/2(3)(4pi e-7)(200)^2(0.05)(0.002)(1) [J]", 0.5*3*4e-7*np.pi*200**2*0.05*0.002*1, "7.54e-6")
close("15.10(c) energy route 2W/I^2 = flux route Psi/I", 2*Wm10/I10**2, L10, rtol=1e-8)
sf("15.10(c) C' [F/m]", C10, "664e-12")
LC10 = L10/l10*C10
close("15.10(c) L'C' = mu eps", LC10, mu10*ep10, rtol=1e-8)
sf("15.10(c) L'C'/(mu0 eps0)", LC10/(mu0*eps0), "9")
sf("15.10(c) 1/sqrt(L'C') [m/s]", 1/np.sqrt(LC10), "9.99e7")
close("15.10(c) 1/sqrt(L'C') = c/3", 1/np.sqrt(LC10), c0/3, rtol=1e-8)
s10 = plate_numbers(2*W10, d10/2, 3*I10)
for nm, i, st in [("|B|", 0, "1.5"), ("Psi", 1, "0.75"), ("L", 2, "0.25"), ("C'", 3, "4")]:
    sf(f"15.10(d) {nm} factor", s10[i]/[Bm, Psi10, L10, C10][i], st)
close("15.10(d) L'C' unchanged", s10[2]*s10[3]/(L10*C10), 1.0, rtol=1e-8)
Lkey = mu0*l10*d10/W10
info(f"15.10 re-param: exam key psi = mu0 I l d/w, L = mu0 l d/w with these numbers give {mu0*I10/W10*d10*l10:.3g} Wb and "
     f"{Lkey*1e9:.1f} nH (the page's values before this review: the key carried over); with the fill the page has "
     f"{Psi10:.3g} Wb, {L10*1e9:.0f} nH, B {-Bgap[2]:.3g} T (key mu0 I/w = {mu0*I10/W10:.3g} T, along -y^ in the exam frame); "
     f"key scaling (2d, I/2) x0.5, x1.0, x2.0 vs page (d) x1.5, x0.75, x0.25, x4")
truth("15.10 re-param: key psi, L, B formulas no longer reproduce the page's answers",
      not np.isclose(Lkey, L10) and not np.isclose(mu0*I10/W10, -Bgap[2]))

# =========================================================================================
section("15.11 wire and rectangular loop")
d1, d2, h11, dIdt = 0.02, 0.08, 0.5, 1e4
Lw11 = 200.0
WA, WB = np.array([[0, 0, h11/2 - Lw11]]), np.array([[0, 0, h11/2 + Lw11]])   # centred on the loop
Bw = lambda x, z, I=1.0: bs_segments(np.array([x, 0, z]), WA, WB, I)
vec("15.11(a) Biot-Savart B at (d1, 0, h/2) per ampere", Bw(d1, h11/2), [0, mu0/(2*np.pi*d1), 0], rtol=1e-6, atol=1e-15)
vec("15.11(a) phi^ on y = 0, x > 0: z^ x x^ = +y^", np.cross(Z, X), Y)
vec("15.11(a) loop normal: z^ (up near side) x x^ (along top) = +y^", np.cross(Z, X), Y)
xg, wxg = np.polynomial.legendre.leggauss(60)
zg, wzg = np.polynomial.legendre.leggauss(8)
xs, zs = d1 + (xg + 1)*(d2 - d1)/2, (zg + 1)*h11/2
M11 = sum(wx*wz*Bw(xx, zz)[1] for xx, wx in zip(xs, wxg) for zz, wz in zip(zs, wzg))*(d2 - d1)/2*h11/2
sf("15.11(a) M = Psi/I (Biot-Savart flux) [H]", M11, "1.39e-7")
close("15.11(a) M = (mu0 h/2 pi) ln 4", M11, mu0*h11/(2*np.pi)*np.log(4), rtol=1e-6)
emf11 = -M11*dIdt
sf("15.11(b) emf in the reference direction [V]", emf11, "-1.39e-3")
# induced current flows against the reference: down the near side, +x^ along the bottom, up the far side, -x^ on top
Fnear = h11*np.cross(-Z, Bw(d1, h11/2))
Ffar = h11*np.cross(Z, Bw(d2, h11/2))
Fbot = integrate.quad(lambda xx: np.cross(X, Bw(xx, 0.0))[2], d1, d2)[0]*Z
Ftop = integrate.quad(lambda xx: np.cross(-X, Bw(xx, h11))[2], d1, d2)[0]*Z
vec("15.11(b) force on the near side along +x^ (away from the wire)", np.sign(Fnear), [1, 0, 0])
vec("15.11(b) force on the far side along -x^ (toward the wire)", np.sign(Ffar), [-1, 0, 0])
vec("15.11(b) top and bottom forces cancel", Fbot + Ftop, np.zeros(3), atol=1e-14)
Fnet = Fnear + Ffar + Fbot + Ftop
close("15.11(b) net F_x per (I i) = (mu0 h/2 pi)(1/d1 - 1/d2)", Fnet[0], mu0*h11/(2*np.pi)*(1/d1 - 1/d2), rtol=1e-6)
truth("15.11(b) loop repelled", Fnet[0] > 0)
Az = lambda x, y, z, t, r0: -mu0*(1.0 + dIdt*t)/(2*np.pi)*np.log(np.hypot(x, y)/r0)   # I(t) = 1 A + ramp
Avec = lambda r0: (lambda x, y, z, t: np.array([0.0, 0.0, Az(x, y, z, t, r0)]))
vec("15.11(c) curl A = B (finite differences) at (d1, 0, 0.2), t = 0", curl(Avec(1.0), [d1, 0, 0.2], 0.0, h=1e-7),
    Bw(d1, 0.2), rtol=1e-5, atol=1e-12)


def circA(r0, t=0.0):
    A_ = Avec(r0)
    near = integrate.quad(lambda zz: A_(d1, 0, zz, t) @ Z, 0, h11)[0]
    top = integrate.quad(lambda xx: A_(xx, 0, h11, t) @ X, d1, d2)[0]
    far = integrate.quad(lambda zz: A_(d2, 0, zz, t) @ (-Z), 0, h11)[0]
    bot = integrate.quad(lambda xx: A_(xx, 0, 0, t) @ (-X), d1, d2)[0]
    return near + top + far + bot


close("15.11(c) closed integral of A.dl (r0 = 1 m) = Psi at 1 A", circA(1.0), M11, rtol=1e-6)
close("15.11(c) closed integral of A.dl independent of r0 (0.37 m)", circA(0.37), circA(1.0), rtol=1e-9)
Ez = lambda x, r0: -(Az(x, 0, 0, 1e-6, r0) - Az(x, 0, 0, -1e-6, r0))/2e-6
dE11 = Ez(d1, 1.0) - Ez(d2, 1.0)
sf("15.11(c) E_z(d1) - E_z(d2) [V/m]", dE11, "-2.77e-3")
close("15.11(c) E_z(d1) - E_z(d2) independent of r0", Ez(d1, 0.37) - Ez(d2, 0.37), dE11, rtol=1e-6)
sf("15.11(c) closed integral of E.dl = h [E_z(d1) - E_z(d2)] [V]", h11*dE11, "-1.39e-3")
close("15.11(c) equals the emf of (b)", h11*dE11, emf11, rtol=1e-6)
R11, L11 = 5e-3, 1e-6
s11 = integrate.solve_ivp(lambda t, y: [(-M11*dIdt - R11*y[0])/L11], [0, 5e-3], [0.0], method='DOP853',
                          rtol=1e-12, atol=1e-16, dense_output=True)
i11 = lambda t: s11.sol(t)[0]
iinf = i11(5e-3)
sf("15.11(d) i_inf [A]", iinf, "-0.277")
sf("15.11(d) emf to 4 s.f. as displayed [V]", emf11, "-1.386e-3")
sf("15.11(d) literal -1.386 mV / 5 mOhm [A]", -1.386e-3/5e-3, "-0.277")
info(f"15.11 old literal -1.39 mV / 5 mOhm = {-1.39e-3/5e-3:.4g} A (page said -0.277; fixed to -1.386)")
close("15.11(d) tau (63.2 % time of the ODE) = 0.2 ms", optimize.brentq(lambda t: i11(t) - (1 - 1/np.e)*iinf, 1e-9, 1e-3,
                                                                       xtol=1e-16), 2e-4, rtol=1e-6)
sf("15.11(d) 99 % time [s]", optimize.brentq(lambda t: i11(t) - 0.99*iinf, 1e-9, 4e-3, xtol=1e-16), "0.921e-3")

# =========================================================================================
section("15.12 coax with a magnetic sleeve")
a12, s12, b12, I12 = 1e-3, 2e-3, 4e-3, 1.0
mu12 = lambda r: 4*mu0 if a12 < r < s12 else mu0
ep12 = lambda r: 4*eps0 if a12 < r < s12 else eps0
J12 = I12/(np.pi*a12**2)
Ienc12 = lambda r: integrate.quad(lambda rp: J12*2*np.pi*rp, 0, min(r, a12))[0] - (I12 if r > b12 else 0.0)
H12 = lambda r: Ienc12(r)/(2*np.pi*r)
for r, ex in [(0.5e-3, 0.5e-3/(2*np.pi*a12**2)), (1.5e-3, 1/(2*np.pi*1.5e-3)), (3e-3, 1/(2*np.pi*3e-3)), (5e-3, 0.0)]:
    close(f"15.12(a) H_phi(r = {r*1e3:g} mm) by Ampere", H12(r), ex*I12, rtol=1e-9, atol=1e-9)
sf("15.12(a) H(a) [A/m]", H12(a12), "159")
close("15.12(a) H continuous at r = s", H12(s12*(1 - 1e-9)), H12(s12*(1 + 1e-9)), rtol=1e-6)
close("15.12(a) B jumps by 4 at r = s", mu12(s12*(1 - 1e-9))*H12(s12*(1 - 1e-9))/(mu12(s12*(1 + 1e-9))*H12(s12*(1 + 1e-9))),
      4.0, rtol=1e-6)
Wr = [integrate.quad(lambda r: 0.5*mu12(r)*H12(r)**2*2*np.pi*r, lo, hi, epsrel=1e-12)[0]
      for lo, hi in [(0, a12), (a12, s12), (s12, b12)]]
for k, st in enumerate(["2.50e-8", "2.77e-7", "6.93e-8"]):
    sf(f"15.12(b) W'_{k + 1} at 1 A [J/m]", Wr[k], st)
contrib = [2*w/I12**2 for w in Wr]
for k, st in enumerate(["50e-9", "554.5e-9", "138.6e-9"]):
    sf(f"15.12(b) 2W'_{k + 1}/I^2 [H/m]", contrib[k], st)
Ltot12 = sum(contrib)
sf("15.12(b) total L' [H/m]", Ltot12, "743e-9")
for k, st in enumerate(["6.7", "74.6", "18.7"]):
    sf(f"15.12(b) share of region {k + 1} [%]", 100*contrib[k]/Ltot12, st)
Lext12 = integrate.quad(lambda r: mu12(r)*H12(r), a12, b12, points=[s12], epsrel=1e-12)[0]/I12
sf("15.12(c) L'_ext by flux [H/m]", Lext12, "0.693e-6")
close("15.12(c) L'_ext = 1e-6 ln 2 H/m", Lext12, 1e-6*np.log(2), rtol=1e-8)
close("15.12(c) flux route = energy contributions of regions 2 + 3", Lext12, contrib[1] + contrib[2], rtol=1e-8)
rl12 = 1e-9
C12 = rl12/integrate.quad(lambda r: rl12/(2*np.pi*ep12(r)*r), a12, b12, points=[s12], epsrel=1e-12)[0]
sf("15.12(d) C' [F/m]", C12, "64.2e-12")
sf("15.12(d) L'_ext C' [s^2/m^2]", Lext12*C12, "4.45e-17")
close("15.12(d) L'_ext C' = 4 mu0 eps0", Lext12*C12, 4*mu0*eps0, rtol=1e-8)
sf("15.12(d) 1/sqrt(L'_ext C') [m/s]", 1/np.sqrt(Lext12*C12), "1.50e8")
sf("15.12(d) sleeve 1/sqrt(mu eps) [m/s]", 1/np.sqrt(16*mu0*eps0), "7.49e7")
Lu = integrate.quad(lambda r: 4*mu0*H12(r), a12, b12)[0]/I12
Cu = rl12/integrate.quad(lambda r: rl12/(2*np.pi*4*eps0*r), a12, b12)[0]
close("15.12 check: uniform fill gives L'_ext C' = mu eps", Lu*Cu, 16*mu0*eps0, rtol=1e-8)

print(f"\nSUMMARY: {npass} PASS, {nfail} FAIL")
