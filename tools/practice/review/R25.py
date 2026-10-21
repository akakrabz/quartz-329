"""Independent check of practice page 25 (reflection/transmission)."""
import numpy as np
from scipy.integrate import quad

eta0 = 120*np.pi
c = 3e8
e0 = 1e-9/(36*np.pi)
mu0 = 4e-7*np.pi
X, Y, Z = np.eye(3)
fails = 0


def chk(name, got, want, tol=5e-3, rel=True):
    global fails
    got = np.asarray(got, dtype=complex)
    want = np.asarray(want, dtype=complex)
    err = np.max(np.abs(got-want))
    scale = max(np.max(np.abs(want)), 1e-300) if rel else 1
    ok = err <= tol*scale
    fails += (not ok)
    print(f"{'PASS' if ok else 'FAIL'}  {name}: got {np.round(got,6)} want {np.round(want,6)}")


def solve_bc(Ei0, u, eta1, eta2, pec=False):
    """Brute-force BC solve: unknown reflected/transmitted vectors.
    Tangential E and H continuous (no J_s), or E_tan=0 for PEC."""
    # basis of tangential plane
    t = [v for v in (X, Y, Z) if abs(np.dot(v, u)) < 1e-12]
    Hi0 = np.cross(u, Ei0)/eta1
    # unknowns: Er components along t (2), Et components along t (2)
    A = np.zeros((4, 4), complex)
    b = np.zeros(4, complex)
    for k, tk in enumerate(t):
        # E: Ei + Er = Et
        A[k, k] = 1
        A[k, 2+k] = 0 if pec else -1
        b[k] = -np.dot(Ei0, tk)
    if pec:
        A[2, 2] = 1
        A[3, 3] = 1
    else:
        for k, tk in enumerate(t):
            # H: Hi + Hr = Ht, Hr = (-u) x Er/eta1, Ht = u x Et/eta2
            for m, tm in enumerate(t):
                A[2+k, m] = np.dot(np.cross(-u, tm), tk)/eta1
                A[2+k, 2+m] = -np.dot(np.cross(u, tm), tk)/eta2
            b[2+k] = -np.dot(Hi0, tk)
    s = np.linalg.solve(A, b)
    Er = s[0]*t[0]+s[1]*t[1]
    Et = s[2]*t[0]+s[3]*t[1]
    return Er, Et


def gam_eta(w, mu, eps, sig):
    sc = sig+1j*w*eps
    g = np.sqrt(1j*w*mu*sc)
    if g.real < 0:
        g = -g
    eta = np.sqrt(1j*w*mu/sc)
    if eta.real < 0:
        eta = -eta
    return g, eta


print("=== 25.1 ===")
cases = {"a": (1, 1, 1, 4), "b": (1, 4, 1, 1), "c": (1, 1, 16, 4)}
want = {"a": (-1/3, 2/3), "b": (1/3, 4/3), "c": (1/3, 4/3)}
for k, (m1, e1, m2, e2) in cases.items():
    eta1 = eta0*np.sqrt(m1/e1)
    eta2 = eta0*np.sqrt(m2/e2)
    Er, Et = solve_bc(X, Z, eta1, eta2)
    chk(f"25.1{k} Gamma", Er[0], want[k][0])
    chk(f"25.1{k} tau", Et[0], want[k][1])
    St = 0.5*np.real(np.cross(Et, np.conj(np.cross(Z, Et)/eta2)))[2]
    Si = 0.5/eta1
    chk(f"25.1{k} refl %", abs(Er[0])**2*100, 11.1, tol=5e-3)
    chk(f"25.1{k} balance", abs(Er[0])**2+St/Si, 1)
Er, Et = solve_bc(X, Z, eta0, 0, pec=True)
chk("25.1d Gamma", Er[0], -1)
chk("25.1d tau", Et[0], 0, rel=False)

print("=== 25.2 ===")
eta1, eta2 = 1.0, 0.5
Er, Et = solve_bc(X, Z, eta1, eta2)
Hi = np.cross(Z, X)/eta1
Hr = np.cross(-Z, Er)/eta1
print("(a) Er.Ei<0:", np.real(Er[0]) < 0, " (b) Hr.Hi<0:", np.real(np.dot(Hr, Hi)) < 0)
chk("25.2a key T", float(np.real(Er[0]) < 0), 1)
chk("25.2b key F", float(np.real(np.dot(Hr, Hi)) < 0), 0)
# (c) tau=4/3 -> eta2/eta1
r = (1+1/3)/(1-1/3)
Er, Et = solve_bc(X, Z, 1.0, r)
chk("25.2c eta2/eta1", r, 2)
chk("25.2c tau", Et[0], 4/3)
chk("25.2c transmitted frac", abs(Et[0])**2/r, 8/9)
# (d) Ei+Er = Et for random etas
Er, Et = solve_bc(X, Z, 1.0, 0.3)
chk("25.2d E continuity", 1+Er[0], Et[0])
# (e)
Er, Et = solve_bc(X, Z, eta0, eta0*np.sqrt(3/3))
chk("25.2e Gamma", Er[0], 0, rel=False)
chk("25.2e speed/c", 1/np.sqrt(9), 1/3)

print("=== 25.3 ===")
w = 1.0  # arbitrary; sigma scales with w
for w in (1e6, 1e9):
    g2, eta2 = gam_eta(w, mu0, 9*e0, 3600*w*e0)
    Er, Et = solve_bc(X, Z, eta0, eta2)
    G = Er[0]
    print(f"w={w:g}: eta2={eta2:.4f} Gamma={G:.5f}")
chk("25.3 loss tangent", 3600/9, 400)
chk("25.3 |eta2| approx eta0/60", eta0/60, 6.3, tol=5e-3)
chk("25.3 eta2 approx", np.sqrt(1j*w*mu0/(3600*w*e0)), eta0/60*np.exp(1j*np.pi/4))
chk("25.3 Gamma exact", G, -0.976+0.023j, tol=2e-3)
chk("25.3 |Gamma|", abs(G), 0.977, tol=1e-3)
chk("25.3 |Gamma|^2 %", abs(G)**2*100, 95.4, tol=1e-3)
# distractors
chk("25.3 (b) lossless", (eta0/3-eta0)/(eta0/3+eta0), -0.5)
chk("25.3 (c) swapped lossless", (eta0-eta0/3)/(eta0/3+eta0), 0.5)
chk("25.3 (e) leaving conductor ~+1", (eta0-eta2)/(eta0+eta2), 1, tol=0.05)

print("=== 25.4 ===")
eta2 = eta0/4
chk("25.4 eta2/pi", eta2/np.pi, 30)
chk("25.4 student Gamma", (eta0-eta2)/(eta0+eta2), 0.6)
Er, Et = solve_bc(5*X, Z, eta0, eta2)
chk("25.4 Er(0)", Er, -3*X)
chk("25.4 Et(0)", Et, 2*X)
chk("25.4 Gamma", Er[0]/5, -0.6)
chk("25.4 tau", Et[0]/5, 0.4)
chk("25.4 correct balance", 0.36+0.16*4, 1)
chk("25.4 student balance", 0.36+1.6**2*4, 10.6)
chk("25.4 trans %", abs(Et[0])**2/eta2/(25/eta0)*100, 64)

print("=== 25.5 ===")
# brute: scan eps_r for Gamma=-1/2
from scipy.optimize import brentq
er = brentq(lambda e: ((1/np.sqrt(e)-1)/(1/np.sqrt(e)+1)) + 0.5, 1.01, 100)
chk("25.5a eps_r", er, 9)
chk("25.5b enter %", (1-0.25)*100, 75)
mr = brentq(lambda m: np.sqrt(m/9)-1, 0.1, 100)
chk("25.5c mu_r", mr, 9)

print("=== 25.6 ===")
f = 100e6
w = 2*np.pi*f
eta1, eta2 = eta0*np.sqrt(1/4), eta0*np.sqrt(4/1)
b1, b2 = w/c*np.sqrt(4), w/c*np.sqrt(4)
chk("25.6 eta1/pi", eta1/np.pi, 60)
chk("25.6 eta2/pi", eta2/np.pi, 240)
chk("25.6 beta1", b1, 4*np.pi/3)
chk("25.6 beta2", b2, 4*np.pi/3)
u = -Z
Ei0 = 10*Y
Er, Et = solve_bc(Ei0, u, eta1, eta2)
chk("25.6 Gamma", Er[1]/10, 0.6)
chk("25.6 tau", Et[1]/10, 1.6)
Hr = np.cross(-u, Er)/eta1
Ht = np.cross(u, Et)/eta2
Hi = np.cross(u, Ei0)/eta1
chk("25.6 Er", Er, 6*Y)
chk("25.6 Hr", Hr, -X/(10*np.pi))
chk("25.6 Et", Et, 16*Y)
chk("25.6 Ht", Ht, X/(15*np.pi))
chk("25.6 Hi", Hi, X/(6*np.pi))
# exponent signs: reflected travels +z -> e^{-jbz}; transmitted -z -> e^{+jbz}
print("  reflected u=+z => e^{-j b z}; transmitted u=-z => e^{+j b z} (page: same)")
Si = 0.5*np.real(np.cross(Ei0, np.conj(Hi)))
Sr = 0.5*np.real(np.cross(Er, np.conj(Hr)))
St = 0.5*np.real(np.cross(Et, np.conj(Ht)))
chk("25.6 |Si|", np.linalg.norm(Si), 0.265, tol=2e-3)
chk("25.6 |Sr|", np.linalg.norm(Sr), 0.095, tol=6e-3)
chk("25.6 |St|", np.linalg.norm(St), 0.170, tol=3e-3)
chk("25.6 refl %", np.linalg.norm(Sr)/np.linalg.norm(Si)*100, 36)
chk("25.6 enter %", np.linalg.norm(St)/np.linalg.norm(Si)*100, 64)
print("  Si dir", np.round(Si/np.linalg.norm(Si), 3), "Sr dir", np.round(Sr/np.linalg.norm(Sr), 3))

print("=== 25.7 ===")
f = 300e6
w = 2*np.pi*f
b = w/c
chk("25.7 beta", b, 2*np.pi)
# phasor of 3 sin(wt+by) zhat: fit by sampling
t = np.linspace(0, 1/f, 1000, endpoint=False)


def phasor_from_time(fun):
    """Phasor via Fourier projection over one period."""
    ts = np.linspace(0, 2*np.pi/w, 1000, endpoint=False)
    vals = np.array([fun(tt) for tt in ts])
    return 2*np.mean(vals*np.exp(-1j*w*ts)[:, None], axis=0)


y0 = 0.13
Ei = phasor_from_time(lambda tt: 3*np.sin(w*tt+b*y0)*Z)
chk("25.7 Ei phasor at y0", Ei, -3j*Z*np.exp(1j*2*np.pi*y0))
u = -Y
Hi = np.cross(u, Ei)/eta0
chk("25.7 Hi at y0", Hi, X*1j/(40*np.pi)*np.exp(1j*2*np.pi*y0))
Ei00 = -3j*Z
Er0, _ = solve_bc(Ei00, u, eta0, 0, pec=True)
Er = Er0*np.exp(-1j*b*y0)
Hr = np.cross(-u, Er)/eta0
chk("25.7 Er at y0", Er, 3j*Z*np.exp(-1j*2*np.pi*y0))
chk("25.7 Hr at y0", Hr, X*1j/(40*np.pi)*np.exp(-1j*2*np.pi*y0))
tt = 0.37/f
chk("25.7 Er(t)", np.real(Er*np.exp(1j*w*tt)), -Z*3*np.sin(w*tt-2*np.pi*y0))
Htot = np.cross(u, Ei00)/eta0+np.cross(-u, Er0)/eta0
chk("25.7 H total y=0", Htot, X*1j/(20*np.pi))
n = Y  # from conductor (y<0) into air
Js = np.cross(n, Htot)
chk("25.7 Js phasor", Js, -Z*1j/(20*np.pi))
for tt in (0.1/f, 0.33/f):
    chk("25.7 Js(t)", np.real(Js*np.exp(1j*w*tt)), Z/(20*np.pi)*np.sin(w*tt))
chk("25.7 |Js| mA/m", 1e3/(20*np.pi), 15.9, tol=2e-3)
chk("25.7 2*3/eta0", 6/eta0, 1/(20*np.pi))

print("=== 25.8 ===")
f = 10e9
w = 2*np.pi*f
sig = 5.8e7
e0t = 8.854e-12
chk("25.8 sig/(w e0)", sig/(w*e0t), 1.0e8, tol=0.05)
d = 1/np.sqrt(np.pi*f*mu0*sig)
chk("25.8 delta um", d*1e6, 0.661, tol=1e-3)
eta2a = (1+1j)/(sig*d)
chk("25.8 eta2", eta2a, 0.0261*(1+1j), tol=2e-3)
g2, eta2 = gam_eta(w, mu0, e0t, sig)
print("  exact vs approx eta rel diff:", abs(eta2-eta2a)/abs(eta2a))
Er, Et = solve_bc(X, Z, eta0, eta2)
G = Er[0]
absorbed = 1-abs(G)**2
chk("25.8 absorbed frac", absorbed, 2.77e-4, tol=3e-3)
chk("25.8 formula", 4*eta0*eta2.real/abs(eta0+eta2)**2, absorbed)
chk("25.8 approx 4Re/eta1", 4*eta2.real/eta0, 2.77e-4, tol=3e-3)
chk("25.8 Gamma", G, -0.99986+1.4e-4j, tol=5e-6)
chk("25.8 absorbed mW/m2", 100*absorbed*1e3, 27.7, tol=3e-3)
chk("25.8 reflected W/m2", 100*abs(G)**2, 99.97, tol=1e-4)
chk("25.8 trans side", abs(Et[0])**2*eta0*np.real(1/eta2), absorbed)

print("=== 25.9 ===")
f = 50e6
w = 2*np.pi*f
eta1, eta2 = eta0/3, eta0
b2 = w/c
b1 = 3*b2
chk("25.9 eta1/pi", eta1/np.pi, 40)
chk("25.9 beta2", b2, np.pi/3)
chk("25.9 beta1", b1, np.pi)
u = -Z
Er1, Et1 = solve_bc(Y, u, eta1, eta2)
chk("25.9 Gamma", Er1[1], 0.5)
chk("25.9 tau", Et1[1], 1.5)
z0 = -0.41
Et = phasor_from_time(lambda tt: 3*np.sin(w*tt+b2*z0)*Y) * 1
chk("25.9 Et phasor z0", Et, -3j*Y*np.exp(1j*np.pi*z0/3))
Et0 = -3j*Y
Ht0 = np.cross(u, Et0)/eta2
chk("25.9 Ht(0)", Ht0, -X*1j/(40*np.pi))
Ei0 = Et0/Et1[1]
Er0 = Er1[1]*Ei0
Hi0 = np.cross(u, Ei0)/eta1
Hr0 = np.cross(-u, Er0)/eta1
chk("25.9 Ei(0)", Ei0, -2j*Y)
chk("25.9 Er(0)", Er0, -1j*Y)
chk("25.9 Hi(0)", Hi0, -X*1j/(20*np.pi))
chk("25.9 Hr(0)", Hr0, X*1j/(40*np.pi))
chk("25.9 H tangential", Hi0+Hr0, Ht0)
Si = 0.5*np.real(np.cross(Ei0, np.conj(Hi0)))
Sr = 0.5*np.real(np.cross(Er0, np.conj(Hr0)))
St = 0.5*np.real(np.cross(Et0, np.conj(Ht0)))
chk("25.9 Si", Si, -Z/(20*np.pi))
chk("25.9 Sr", Sr, Z/(80*np.pi))
chk("25.9 St", St, -Z*3/(80*np.pi))
chk("25.9 Si mW", Si[2]*1e3, -15.9, tol=2e-3)
chk("25.9 Sr mW", Sr[2]*1e3, 3.98, tol=2e-3)
chk("25.9 St mW", St[2]*1e3, -11.9, tol=5e-3)
chk("25.9 trans frac", St[2]/Si[2], 0.75)
z0 = 0.27
tt = 0.21/f
Er_t = np.real(Er0*np.exp(-1j*b1*z0)*np.exp(1j*w*tt))
chk("25.9 Er(z,t)", Er_t, Y*np.sin(w*tt-np.pi*z0))

print("=== 25.10 ===")
w = 3e8
eps = 2*e0
sig = np.sqrt(3)*w*eps
chk("25.10 sigma", sig, np.sqrt(3)/(60*np.pi))
chk("25.10 sigma mS", sig*1e3, 9.19, tol=1e-3)
g2, eta2 = gam_eta(w, mu0*1.0, eps, sig)
mu0b = eta0/c  # consistent mu0 with eta0=120pi, c
g2, eta2 = gam_eta(w, mu0b, eps, sig)
chk("25.10 beta1", w/c, 1)
chk("25.10 eta2", eta2, 60*np.pi*np.exp(1j*np.pi/6))
chk("25.10 gamma2", g2, 1+1j*np.sqrt(3))
Er, Et = solve_bc(10*X, Z, eta0, eta2)
G, T = Er[0]/10, Et[0]/10
chk("25.10 Gamma", G, (-3+2j)/(5+2*np.sqrt(3)))
chk("25.10 Gamma rect", G, -0.354+0.236j, tol=2e-3)
chk("25.10 |Gamma|", abs(G), 0.426, tol=1e-3)
chk("25.10 arg Gamma", np.degrees(np.angle(G)), 146.3, tol=1e-3)
chk("25.10 tau rect", T, 0.646+0.236j, tol=2e-3)
chk("25.10 |tau|", abs(T), 0.687, tol=1e-3)
chk("25.10 arg tau", np.degrees(np.angle(T)), 20.1, tol=3e-3)
Ht0 = np.cross(Z, Et)/eta2
chk("25.10 |Ht| mA", abs(Ht0[1])*1e3, 36.5, tol=2e-3)
chk("25.10 arg Ht", np.degrees(np.angle(Ht0[1])), -9.9, tol=1e-2)
chk("25.10 |Gamma|^2", abs(G)**2, 13/(5+2*np.sqrt(3))**2)
chk("25.10 refl %", abs(G)**2*100, 18.1, tol=3e-3)
chk("25.10 enter %", (1-abs(G)**2)*100, 81.9, tol=1e-3)
Si = 100/(2*eta0)
chk("25.10 Si", Si, 0.1326, tol=1e-3)
St0 = 0.5*np.real(Et[0]*np.conj(Ht0[1]))
chk("25.10 |tau E0|^2", abs(Et[0])**2, 47.26, tol=1e-3)
chk("25.10 St(0+)", St0, 0.1086, tol=1e-3)
chk("25.10 St/Si", St0/Si, 0.819, tol=1e-3)
alpha = g2.real
J, _ = quad(lambda z: 0.5*sig*abs(Et[0])**2*np.exp(-2*alpha*z), 0, np.inf)
chk("25.10 Joule", J, St0)
H1 = (1-G)*10/eta0
chk("25.10 H check", H1, 0.0359-0.0063j, tol=3e-3)
chk("25.10 H check2", H1, Ht0[1])

print("=== 25.11 ===")
b = np.pi
f = c*b/(2*np.pi)
w = 2*np.pi*f
chk("25.11 f MHz", f/1e6, 150)
chk("25.11 lambda", 2*np.pi/b, 2)
y0 = -0.3
Ei_ph = phasor_from_time(lambda tt: 4*np.cos(w*tt-np.pi*y0)*Z-4*np.sin(w*tt-np.pi*y0)*X)
chk("25.11 Ei phasor", Ei_ph, 4*(Z+1j*X)*np.exp(-1j*np.pi*y0))


def hand(Eph, u):
    """Rotate field numerically at fixed point: sign of u.(E x dE)."""
    ts = np.linspace(0, 1/f, 400, endpoint=False)
    E = np.real(np.outer(np.exp(1j*w*ts), Eph))
    L = np.cross(E[:-1], E[1:]) @ u
    s = np.mean(np.sign(L))
    return "right" if s > 0.99 else ("left" if s < -0.99 else "mixed")


Ei0 = 4*(Z+1j*X)
ui = Y
print("  incident hand:", hand(Ei0, ui))
chk("25.11a left", float(hand(Ei0, ui) == "left"), 1)
# sanity: L24 convention x cos + y sin, travel +z is right
chk("L24 sanity right", float(hand(X-1j*Y, Z) == "right"), 1)
Er0, _ = solve_bc(Ei0, ui, eta0, 0, pec=True)
chk("25.11 Er(0)", Er0, -4*(Z+1j*X))
print("  reflected hand:", hand(Er0, -ui))
chk("25.11b right", float(hand(Er0, -ui) == "right"), 1)
y0, tt = -0.37, 0.19/f
chk("25.11 Er(y,t)", np.real(Er0*np.exp(1j*b*y0)*np.exp(1j*w*tt)),
    -Z*4*np.cos(w*tt+np.pi*y0)+X*4*np.sin(w*tt+np.pi*y0))
Hi0 = np.cross(ui, Ei0)/eta0
Hr0 = np.cross(-ui, Er0)/eta0
chk("25.11 Hi(0)", Hi0, (X-1j*Z)/(30*np.pi))
chk("25.11 Hr(0)", Hr0, (X-1j*Z)/(30*np.pi))
n = -Y  # from conductor (y>0) into air
Js = np.cross(n, Hi0+Hr0)
chk("25.11 Js phasor", Js, (Z+1j*X)/(15*np.pi))
for tt in (0.07/f, 0.6/f):
    chk("25.11 Js(t)", np.real(Js*np.exp(1j*w*tt)),
        (Z*np.cos(w*tt)-X*np.sin(w*tt))/(15*np.pi))
chk("25.11 |Js| mA", 1e3/(15*np.pi), 21.2, tol=2e-3)
chk("25.11 Js=2Ei/eta0", Js, 2*Ei0/eta0)
print("  Js hand about -n (into conductor? n=-y):", hand(Js, ui))
Si = 0.5*np.real(np.cross(Ei0, np.conj(Hi0)))
Sr = 0.5*np.real(np.cross(Er0, np.conj(Hr0)))
chk("25.11 Si", Si, Y*2/(15*np.pi))
chk("25.11 Si mW", Si[1]*1e3, 42.4, tol=2e-3)
chk("25.11 Sr", Sr, -Si)
# dielectric eps_r=9 check
Er9, Et9 = solve_bc(Ei0, ui, eta0, eta0/3)
chk("25.11 chk Gamma", Er9[2]/4, -0.5)
chk("25.11 chk |Er|", abs(Er9[2]), 2)
chk("25.11 chk |Et|", abs(Et9[2]), 2)
print("  eps9 reflected hand:", hand(Er9, -ui), " transmitted hand:", hand(Et9, ui))

print("=== 25.12 ===")
f = 100e6
w = 2*np.pi*f
G = 2/10
chk("25.12 Gamma", G, 0.2)
eta2 = brentq(lambda e: (e-eta0)/(e+eta0)-G, 1, 1e4)
chk("25.12 eta2/pi", eta2/np.pi, 180)
b0 = w/c
b2 = 2*np.pi/1.5
chk("25.12 b0", b0, 2*np.pi/3)
chk("25.12 b2", b2, 4*np.pi/3)
mu2 = (1j*b2)*eta2/(1j*w)
eps2 = (1j*b2)/eta2/(1j*w)
mu0b = eta0/c
e0b = 1/(eta0*c)
chk("25.12 mu_r", mu2/mu0b, 3)
chk("25.12 eps_r", eps2/e0b, 4/3)
Er, Et = solve_bc(10*X, Z, eta0, eta2)
chk("25.12 tau", Et[0]/10, 1.2)
chk("25.12 Et amp", Et[0], 12)
Ht = np.cross(Z, Et)/eta2
chk("25.12 Ht", Ht, Y/(15*np.pi))
chk("25.12 Ht mA", 1e3/(15*np.pi), 21.2, tol=2e-3)
Si, Sr, St = 100/(2*eta0), 4/(2*eta0), 144/(2*eta2)
chk("25.12 Si", Si, 5/(12*np.pi))
chk("25.12 Sr", Sr, 1/(60*np.pi))
chk("25.12 St", St, 2/(5*np.pi))
chk("25.12 mW", [Si*1e3, Sr*1e3, St*1e3], [132.6, 5.3, 127.3], tol=1e-3)
chk("25.12 balance", Si-Sr, St)
chk("25.12d mu_r", brentq(lambda m: np.sqrt(m/(4/3))-1, .1, 10), 4/3)
# watch out: Gamma=-0.2
eta2m = eta0*0.8/1.2
chk("25.12 swapped mu_r", b2/b0*eta2m/eta0, 4/3)
chk("25.12 swapped eps_r", b2/b0*eta0/eta2m, 3)

print("\nTOTAL FAILS:", fails)
