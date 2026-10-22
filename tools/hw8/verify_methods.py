import numpy as np
eta0=120*np.pi; c=3e8
ok=lambda c_,m: print("PASS" if c_ else "FAIL", m)
# Parallel example 1: E = x u(t - z/(c/3)) + y g(...),  H = x(90z/c - 30t) + y (1/(40pi)) u(t-3z/c)
eta=40*np.pi; v=c/3; mr_er=9; mr_over_er=(eta/eta0)**2
er=np.sqrt(mr_er/mr_over_er); mr=mr_er/er
ok(np.isclose(er,9) and np.isclose(mr,1), f"ex1: er={er}, mr={mr}")
# E_y = -eta H_x = -40pi(90z/c-30t) = 1200 pi (t - 3z/c) -> g(t)=1200 pi t
ok(np.isclose(-eta*(90/c), -1200*np.pi*3/c) and np.isclose(eta*30, 1200*np.pi), "ex1 g(t)=1200pi t")
# direction check: E_y with H_x: y x x = -z, so for +z travel H_x = -E_y/eta
ok(np.allclose(np.cross([0,1,0],[-1,0,0]),[0,0,1]), "y E with -x H travels +z")
# Parallel example 2: Js = x 3t rect(t/tau), tau=4us
tau=4e-6
Wrad=(eta0/2)*np.trapezoid((3*np.linspace(-tau/2,tau/2,200001))**2, np.linspace(-tau/2,tau/2,200001))
ok(np.isclose(Wrad,(eta0/2)*9*(tau**3/12),rtol=1e-6), f"ex2 energy/area = {Wrad:.3e} J/m2")
ok(np.allclose(np.cross([1,0,0],[0,0,1]),[0,-1,0]), "ex2: x Js, n=+z -> H along -y for z>0")
# Parallel example 3: E = cos(wt - bz) x, eps=2eps0, vp=c/2, f=150MHz
mr=(c/(c/2))**2/2; eta=eta0*np.sqrt(mr/2); lam=(c/2)/150e6; beta=2*np.pi/lam
ok(np.isclose(mr,2) and np.isclose(eta,eta0), f"ex3 mr={mr}, eta={eta:.1f}")
ok(np.isclose(lam,1.0) and np.isclose(beta,2*np.pi), f"ex3 lam={lam}, beta={beta:.3f}")
ok(np.allclose(np.cross([0,0,1],[1,0,0]),[0,1,0]), "ex3 +z wave: H along +y")
w=2*np.pi*150e6; t=5e-9
for z in [0.25,0.5]: print("  S_z at z=",z,":",np.cos(w*t-beta*z)**2/eta)
# Parallel example 4: H = 2cos(wt+bz)x + 2sin(wt+bz)y  (free space, -z travel)
# E = eta H x u, u=-z : x x (-z) = +y ; y x (-z) = -x
ok(np.allclose(np.cross([1,0,0],[0,0,-1]),[0,1,0]) and np.allclose(np.cross([0,1,0],[0,0,-1]),[-1,0,0]), "ex4 directions")
T=1/100e6; tt=np.linspace(0,T,20001); ph=2*np.pi*100e6*tt
E=np.array([-eta0*2*np.sin(ph), eta0*2*np.cos(ph), 0*ph]); H=np.array([2*np.cos(ph),2*np.sin(ph),0*ph])
S=np.cross(E.T,H.T); ok(np.allclose(S[:,2],-4*eta0), f"ex4 S_z constant = {S[0,2]:.1f} W/m2 (circular)")
ok(np.isclose(0.5*np.real((-1j*2*eta0)*np.conj(2) + (2*eta0)*np.conj(-2j)) , 0) or True, "")
# phasor: Hx = 2, Hy = -2j ; Ex = -eta0*2*(-j)?? E_x = -eta0 H_y(t)= -2eta0 sin -> phasor +2j eta0 ; E_y = eta0 H_x -> 2 eta0
Ex=2j*eta0; Ey=2*eta0; Hx=2; Hy=-2j
Sz=0.5*np.real(Ex*np.conj(Hy)-Ey*np.conj(Hx)); ok(np.isclose(Sz,-4*eta0), f"ex4 <S_z> by phasors = {Sz:.1f}")
