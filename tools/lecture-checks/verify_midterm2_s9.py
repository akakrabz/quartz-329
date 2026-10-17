import numpy as np
e0=8.854e-12; m0=4e-7*np.pi; er,mr=2.5,1.7; eps=er*e0; mu=mr*m0; eta=np.sqrt(mu/eps); v=1/np.sqrt(mu*eps)
w=2*np.pi*1e6; b=w/v; t=np.linspace(0,2*np.pi/w,20001)[:-1]; ok=lambda c,m: print("PASS" if c else "FAIL", m)
# wire: E along z, H phi at surface (point on +x axis: phi = +y)
S=np.cross([0,0,1.0],[0,1.0,0]); ok(np.allclose(S,[-1,0,0]),"wire S points -r (into wire)")
I,a,l,sig=3.0,1e-3,2.0,5.8e7; E=I/(np.pi*a**2*sig); ok(np.isclose(E*I/(2*np.pi*a)*2*np.pi*a*l, I**2*l/(sig*np.pi*a**2)),"side flux = I^2R")
# plane wave averages
E0=7.0; z=0.3; Ex=E0*np.cos(w*t-b*z); Hy=Ex/eta
Savg=np.mean(Ex*Hy); wavg=np.mean(0.5*eps*Ex**2+0.5*mu*Hy**2)
ok(np.isclose(Savg,E0**2/(2*eta)),"<S>=E0^2/2eta"); ok(np.isclose(wavg,0.5*eps*E0**2),"<w>=eps E0^2/2"); ok(np.isclose(Savg,v*wavg),"<S>=v<w>")
ok(np.isclose(np.max(Ex*Hy),E0**2/eta,rtol=1e-6),"peak S = E0^2/eta")
ok(np.isclose(np.mean(sig*(E0*np.cos(w*t))**2),0.5*sig*E0**2),"<J.E>=sigma E0^2/2")
# sheet Js = x J0 cos wt at z=0: E=-(eta/2)J0 cos(wt-b|z|) x; H = 1/2 Js x n
J0=1.3
for zz in [0.4,-0.4]:
    n=np.array([0,0,np.sign(zz)]); Ez=-(eta/2)*J0*np.cos(w*t-b*abs(zz)); Hv=np.outer(0.5*J0*np.cos(w*t-b*abs(zz)),np.cross([1,0,0],n))
    Sv=np.cross(np.outer(Ez,[1,0,0]),Hv); ok(np.isclose(np.mean(Sv@n),eta*J0**2/8),f"<S> away from sheet = eta J0^2/8 (z={zz})")
JE=J0*np.cos(w*t)*(-(eta/2)*J0*np.cos(w*t)); ok(np.isclose(np.mean(-JE),eta*J0**2/4),"<-Js.E>=eta J0^2/4")
# pillbox instant: n from 2 (z<0) into 1 (z>0)
S1=(eta/4)*J0**2*np.cos(w*t)**2; S2=-(eta/4)*J0**2*np.cos(w*t)**2; ok(np.allclose(S1-S2,-JE),"n.(S1-S2) = -Js.E")
ok(np.isclose(377/2,188.5,atol=0.6),"notes J0=2 vacuum: eta0/2 ~ 188 W/m2 per side (eta0*4/8)")
# standing wave
zs=np.linspace(0,2,7); 
for zz in zs:
    E=E0*(np.cos(w*t-b*zz)+np.cos(w*t+b*zz)); H=(E0/eta)*(np.cos(w*t-b*zz)-np.cos(w*t+b*zz))
    assert abs(np.mean(E*H))<1e-9*E0**2/eta
ok(True,"standing wave <S>=0 at all z (w nonzero)")
# hole in wire field uniform: H = (J/2) z x d
J=2.0; d=np.array([0.3,0.1,0]); pts=np.random.rand(5,3)*0.05; pts[:,2]=0
Hs=[0.5*J*np.cross([0,0,1],p) - 0.5*J*np.cross([0,0,1],p-d) for p in pts]; ok(np.allclose(Hs,Hs[0]),"field in hole uniform")
