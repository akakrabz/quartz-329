#!/usr/bin/env python3
"""Independent review checks for Lecture 19 (page, figures, concept pages, worked problem)."""
import numpy as np
mu0 = 1.25663706212e-6; eps0 = 8.8541878128e-12
c = 1/np.sqrt(mu0*eps0); eta0 = np.sqrt(mu0/eps0)
X, Y, Z = np.eye(3)
cr = np.cross
def p(*a): print(*a)

def curl(F, r, t, h=1e-4):
    J = np.zeros((3, 3))
    for k in range(3):
        d = np.zeros(3); d[k] = h
        J[:, k] = (F(r + d, t) - F(r - d, t)) / (2*h)       # J[i,k] = dF_i/dx_k
    return np.array([J[2,1]-J[1,2], J[0,2]-J[2,0], J[1,0]-J[0,1]])
def ddt(F, r, t, dt):
    return (F(r, t+dt) - F(r, t-dt)) / (2*dt)
def maxwell(name, E, H, pts, mu=mu0, eps=eps0, T=1e-8):
    worst = 0
    for r, t in pts:
        r = np.array(r, float)
        dt = T*1e-4
        f = curl(E, r, t) + mu*ddt(H, r, t, dt)
        a = curl(H, r, t) - eps*ddt(E, r, t, dt)
        sF = np.linalg.norm(curl(E, r, t)) + 1e-30; sA = np.linalg.norm(curl(H, r, t)) + 1e-30
        worst = max(worst, np.linalg.norm(f)/sF, np.linalg.norm(a)/sA)
    p(f"[Maxwell FD] {name}: worst relative residual (Faraday, Ampere-Maxwell) = {worst:.1e}", "OK" if worst < 1e-4 else "FAIL")

g = lambda s: np.exp(-(s/2e-9)**2) * np.cos(2*np.pi*3e8*s)      # smooth test waveform (s in seconds)

p("== constants"); p(f"c = {c:.6e}, eta0 = {eta0:.4f}, 120pi = {120*np.pi:.4f}, rel = {120*np.pi/eta0-1:.2e}, eta0/2 = {eta0/2:.2f}, 1/eta0 = {1e3/eta0:.4f} mA/m")

p("\n== Sec 3 notes' sheet J = x f(t) on z=0 (general medium eps_r=2.5)")
er = 2.5; eps = er*eps0; v = 1/np.sqrt(mu0*eps); eta = np.sqrt(mu0/eps)
En = lambda r, t: -X*eta/2*g(t - abs(r[2])/v)
Hn = lambda r, t: -np.sign(r[2])*Y*0.5*g(t - abs(r[2])/v)
maxwell("notes sheet z>0 and z<0", En, Hn, [((0.1,0.2,0.37),1e-9), ((0,0,-0.52),2e-9), ((0,0,0.9),3e-9)], eps=eps)
t0 = 0.4e-9; d = 1e-7
p("E continuity:", En(np.array([0,0,d]),t0)[0], En(np.array([0,0,-d]),t0)[0])
p("jump z x (H+ - H-) =", cr(Z, Hn(np.array([0,0,d]),t0) - Hn(np.array([0,0,-d]),t0)), " J_s =", X*g(t0))
p("E x H dir above/below:", np.sign(cr(-X, -Y)), np.sign(cr(-X, Y)), "  static 1/2 J x n:", 0.5*cr(X, Z), 0.5*cr(X, -Z))

p("\n== Sec 4 slides' sheet J = -Js x, free space: E = x eta0/2 Js, H = +-y Js/2")
Es = lambda r, t: X*eta0/2*g(t - abs(r[2])/c)
Hs = lambda r, t: np.sign(r[2])*Y*0.5*g(t - abs(r[2])/c)
maxwell("slides sheet", Es, Hs, [((0,0,0.4),1e-9), ((0,0,-0.4),1.5e-9)])
p("jump: z x (H1-H2) =", cr(Z, Hs(np.array([0,0,d]),t0)-Hs(np.array([0,0,-d]),t0)), " vs J_s =", -X*g(t0))
p("recipe 1/2 J x n with J=-x:", 0.5*cr(-X, Z), 0.5*cr(-X, -Z), " E=-eta/2 J ->", -0.5*(-X))

p("\n== Example 1: E = x tri((t-y/c)/tau)")
tau = 1e-6
tri = lambda u: np.maximum(0, 1-2*abs(u))
E1 = lambda r, t: X*tri((t - r[1]/c)/tau)
H1 = lambda r, t: -Z*tri((t - r[1]/c)/tau)/eta0
maxwell("Example 1", E1, H1, [((0,40,0),0.05e-6), ((0,-30,0),0.02e-6)], T=1e-6)
r = np.array([0,40.,0]); t = 0.05e-6
dBdt = mu0*ddt(H1, r, t, 1e-12)[2]; rhs = -curl(E1, r, t, h=1e-3)[2]
p(f"dBz/dt = {dBdt:.4e} T/s, -(curl E)_z = {rhs:.4e}; H dir y x x = {cr(Y,X)}, E x H = {cr(X,-Z)}")
p("\n== Example 2 ratios:", 1e6/c, 2e8/c)

p("\n== Example 3: f = 2t rect(t) V/m (t in us), c = 300 m/us")
f3 = lambda t: np.where(abs(t) < 0.5, 2*t, 0.0)
p("E(600,t) at t=1.5001,2,2.4999:", f3(np.array([1.5001,2,2.4999])-2))
p("E(z,0) at z=-149.9,0,149.9:", f3(-np.array([-149.9,0,149.9])/300))
p("E(z,2) at z=450.1,600,749.9:", f3(2-np.array([450.1,600,749.9])/300), "  H dir z x x =", cr(Z,X))

p("\n== Example 4: J = x f(t), f = 2t rect A/m, t=2 us")
for zz in (-749.9,-600,-450.1,450.1,600,700,749.9):
    s = 2 - abs(zz)/300; fv = f3(s)
    Hy = -np.sign(zz)*0.5*fv; Ex = -60*np.pi*fv
    p(f"  z={zz:7.1f}: Hy={Hy:+.3f} A/m, Ex={Ex/np.pi:+.2f} pi V/m")

p("\n== Slide 17: J = -Js z on y=0")
p("H (y>0, y<0):", 0.5*cr(-Z, Y), 0.5*cr(-Z, -Y), " E = -eta/2 J dir:", 0.5*Z, " ExH:", cr(Z, X), cr(Z, -X))
w = 2*np.pi*1e8; beta = w/c
E17 = lambda r, t: Z*eta0*np.cos(w*t - beta*abs(r[1]))
H17 = lambda r, t: np.sign(r[1])*X*np.cos(w*t - beta*abs(r[1]))
maxwell("slide 17 cosine", E17, H17, [((0,0.3,0),1e-9), ((0.1,-0.7,0.2),2e-9)])

p("\n== Slide 11: F profile, v = 100 m/s")
zp = np.array([-100,0,100,300,400.]); Fp = np.array([0,1,-1,0,0.])
F = lambda z: np.interp(z, zp, Fp, left=0, right=0)
p("(a) E(z,1) at 0,100,200,400,500:", F(np.array([0,100,200,400,500.])-100), " zero crossing t=0 at", np.interp(0,[1,-1],[0,100]), "(between B and C: falling in z)")
p("    E(50,1)=", F(50-100.), " -> 50 m now sits on the A'-B' rising edge; crossing at 150 m is on B'-C' (falling)")
tt = np.array([-4,-3,-1,-0.5,0,1.])
p("(b) E(0,t) at", tt, "=", F(-100*tt), " first corner to cross z=0: E (t=-4), last: A (t=+1)")
tt = np.array([-2,-1,0,1,1.5,2,3.])
p("(c) E(200,t) at", tt, "=", F(200-100*tt))

p("\n== Sec 7 numbers")
f = 100e6; p(f"beta = {2*np.pi*f/3e8:.4f} rad/m, lambda = {3e8/f:.3f} m; peak S per side (Js0=1) = {eta0/4:.2f} W/m^2")
Es7 = lambda r, t: X*eta0/2*np.cos(w*t - beta*abs(r[2])); Hs7 = lambda r, t: np.sign(r[2])*Y*0.5*np.cos(w*t-beta*abs(r[2]))
for zz in (0.4,-0.4):
    rr = np.array([0,0,zz]); S = cr(Es7(rr,1e-9), Hs7(rr,1e-9)); p(f"  S(z={zz}) = {S}, formula = {np.sign(zz)*eta0/4*np.cos(w*1e-9-beta*0.4)**2:.4f}")
p("  sum of both sides at sheet vs -J.E:", 2*eta0/4, -np.dot(-X*1, X*eta0/2))
p("  #1(vii)-style replacement: 4pi rad in 5 us -> w =", 4*np.pi/5e-6, " f =", 4*np.pi/5e-6/2/np.pi, " lambda =", 3e8/(4*np.pi/5e-6/2/np.pi))

p("\n== Sec 8 inverse problem (plot scale, peak 2 A/m)")
Fh = lambda xx: np.where((xx > 0) & (xx < 100), 0.02*xx, 0.0)
Hy8 = lambda x, t: np.where(x > 0, Fh(x - 300*(t-1)), -Fh(-x - 300*(t-1)))
tt = np.array([1.9999,2.0001,2.2,2.3333,2.34])
p("(a) H(400,t) at", tt, "=", Hy8(400., tt))
xx = np.array([-1000.1,-999.9,-950,-900,899.9,950,999.9,1000.1])
p("(b) H(x,4) at", xx, "=", Hy8(xx, 4.))
p("(c) E dir x>0: eta H x u = y x x =", cr(Y, X), "; E_z(+-399.9,2)=", -eta0*np.array([Fh(399.9-300), Fh(399.9-300)]), " 2*eta0=", 2*eta0)
tt = np.array([0.6,0.6668,0.8,0.9999,1.0001])
p("(d) Jz(t)=2 Hy(0+,t) at", tt, "=", 2*Fh(300*(1-tt)), "  x x (y) =", cr(X, Y))
# Maxwell for x-travelling pair with smooth waveform
E8 = lambda r, t: -Z*eta0*g(t - abs(r[0])/c); H8 = lambda r, t: np.sign(r[0])*Y*g(t - abs(r[0])/c)
maxwell("sec 8 x-sheet pair (E=-z eta0 H_y, H odd)", E8, H8, [((0.3,0,0),1e-9), ((-0.8,0.1,0),2e-9)])

p("\n== Sec 9 TL picture: parallel-plate Z0 = eta d/W; two halves in parallel -> E = eta Js/2")
W_, d_, Js = 2.0, 0.01, 3.0; Z0 = eta0*d_/W_; V = Js*W_*Z0/2; p("  E = V/d =", V/d_, " eta0 Js/2 =", eta0*Js/2)

p("\n== Worked problem (re-parameterized: J = z Js(t) on x = 0, eps_r = 4)")
er = 4; eps = er*eps0; v = 1/np.sqrt(mu0*eps); eta = np.sqrt(mu0/eps); vn = 0.15  # m/ns with c=3e8
p(f"  v = {v:.4e} m/s (0.15 m/ns with c=3e8), eta = {eta:.2f}, eta/2 = {eta/2:.2f}")
Jp = lambda t: np.where((t > 0) & (t < 2), 3*t, np.where((t >= 2) & (t < 4), -2.0, 0.0))
p("  H (x>0, x<0):", 0.5*cr(Z, X), 0.5*cr(Z, -X), "  E dir:", -Z, "  ExH:", cr(-Z, Y), cr(-Z, -Y))
p("  old version (J = y): H =", 0.5*cr(Y, X), 0.5*cr(Y, -X), " == SP18 #5 key (-1/2 z fwd, +1/2 z rev): carries over -> re-parameterize")
p("  jump x x (H+ - H-) per unit J =", cr(X, 0.5*Y - (-0.5*Y)))
Hy = lambda x, t: np.sign(x)*0.5*Jp(t - abs(x)/vn); Ez = lambda x, t: -eta/2*Jp(t - abs(x)/vn)
for xx in (0.2,0.45,0.5999,0.6001,0.75,0.8999,0.95,-0.2,-0.45,-0.5999,-0.6001,-0.75,-0.8999):
    p(f"   x={xx:+.4f}: Hy={float(Hy(xx,6.)):+.3f} A/m, Ez={float(Ez(xx,6.)):+8.1f} V/m")
for tt in (2.9,3.5,4.999,5.001,6,6.999,7.001):
    p(f"   probe x=-0.45, t={tt}: Hy={float(Hy(-0.45,tt)):+.3f}")
Ev = np.array([0,0,float(Ez(0.75,6.))]); Hv = np.array([0,float(Hy(0.75,6.)),0]); p("  S(0.75,6ns) =", cr(Ev,Hv), " eta/4*9 =", eta/4*9)
Ev = np.array([0,0,float(Ez(-0.75,6.))]); Hv = np.array([0,float(Hy(-0.75,6.)),0]); p("  S(-0.75,6ns) =", cr(Ev,Hv))
p("  -J.E at t'=1 ns:", eta/2*9, "  max |S| (Js=6):", eta*36/4)
Ew = lambda r, t: -Z*eta/2*g(t - abs(r[0])/v); Hw = lambda r, t: np.sign(r[0])*Y*0.5*g(t - abs(r[0])/v)
maxwell("worked problem pair (eps_r=4)", Ew, Hw, [((0.3,0,0),1e-9), ((-0.45,0.2,0.1),2e-9)], eps=eps)
p("  vacuum variant: front at", 0.3*6, "m; eta0/2 =", eta0/2)

p("\n== Poynting concept trap: two counter-propagating waves along z (arbitrary polarizations)")
rng = np.random.default_rng(1)
e1 = np.r_[rng.normal(size=2),0]; e2 = np.r_[rng.normal(size=2),0]
h1 = cr(Z, e1)/eta0; h2 = cr(-Z, e2)/eta0
S = cr(e1+e2, h1+h2); p("  S total =", S, " S1+S2 =", cr(e1,h1)+cr(e2,h2), " cross terms =", cr(e1,h2)+cr(e2,h1))
e3 = np.r_[rng.normal(size=2),0]; h3 = cr(Z, e3)/eta0
p("  co-propagating: S total =", cr(e1+e3,h1+h3), " S1+S3 =", cr(e1,h1)+cr(e3,h3))
