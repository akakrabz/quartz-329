# R26: independent checks, Lecture 26 practice
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq, minimize_scalar

pi = np.pi
c = 3e8; eta0 = 120*pi; mu0 = 4*pi*1e-7; eps0 = 1e-9/(36*pi)
X, Y, Z = np.eye(3)
nf = 0
def chk(name, got, want, rtol=5e-3, atol=0.0):
    global nf
    g = np.asarray(got, float); w = np.asarray(want, float)
    ok = np.allclose(g, w, rtol=rtol, atol=atol)
    nf += (not ok)
    fm = lambda a: np.array2string(np.atleast_1d(a), formatter={'float_kind': lambda x: f'{x:.5g}'})
    print(f"{'PASS' if ok else 'FAIL'}  {name}: got {fm(g)} want {fm(w)}")
def tavg(fun, T, n=4000):
    t = np.linspace(0, T, n, endpoint=False)
    return np.mean([fun(ti) for ti in t], axis=0)

# generic PEC-reflected linear wave: incident along +z in medium (v, eta)
def pec_fields(E0vec, w, v, eta, zm=0.0):
    """E,H at (z,t); incident cos(wt - w z/v), mirror at zm."""
    E0vec = np.asarray(E0vec, float)
    Ei = lambda z, t: E0vec*np.cos(w*(t - z/v))
    Er = lambda z, t: -Ei(zm, t + (z - zm)/v)  # PEC: Er(zm)=-Ei(zm), travels -z
    E = lambda z, t: Ei(z, t) + Er(z, t)
    H = lambda z, t: np.cross(Z, Ei(z, t))/eta + np.cross(-Z, Er(z, t))/eta
    return E, H, Ei, Er

def zeros_of(fun, a, b, n=20001):
    z = np.linspace(a, b, n); g = np.array([fun(zi) for zi in z]); r = []
    for i in range(n-1):
        if g[i] == 0: r.append(z[i])
        elif g[i]*g[i+1] < 0: r.append(brentq(fun, z[i], z[i+1]))
    return np.array(r)

print("=== 26.1 ===")
f = 1.25e9; w = 2*pi*f; er = 4; v = c/np.sqrt(er); eta1 = eta0/np.sqrt(er); E0 = 10
lam = v/f; chk("lambda1 [cm]", lam*100, 12)
chk("beta1 = 50pi/3", w/v, 50*pi/3)
E, H, _, _ = pec_fields(E0*X, w, v, eta1)
T = 1/f; ts = np.linspace(0, T, 721)
ampE = lambda z: max(abs(E(z, t)[0]) for t in ts)
ampH = lambda z: max(abs(H(z, t)[1]) for t in ts)
# E standing: E_x(z,T/4) carries sign; H_y(z,0)
zE = zeros_of(lambda z: E(z, T/4)[0], -0.1501, 0.0001)
zH = zeros_of(lambda z: H(z, 0)[1], -0.1501, 0.0001)
chk("E nodes [cm]", np.sort(zE)*100, [-12, -6, 0], atol=1e-6)
chk("H nodes [cm]", np.sort(zH)*100, [-15, -9, -3], atol=1e-6)
chk("|Ex| at -1 cm", ampE(-0.01), 10)
chk("|Hy| at -1 cm [mA/m]", ampH(-0.01)*1e3, 91.9)
chk("sqrt3/6pi", np.sqrt(3)/(6*pi)*1e3, 91.9)

print("=== 26.2 ===")
f = 1e9; w = 2*pi*f; T = 1/f; lam = c/f; E0 = 1
E, H, Ei, Er = pec_fields(E0*X, w, c, eta0)
S = lambda z, t: np.cross(E(z, t), H(z, t))
zz = np.linspace(-lam, 0, 37)
Sav = np.array([tavg(lambda t: S(z, t), T, 800) for z in zz])
chk("(a) max|<S>| ~ 0", np.abs(Sav).max(), 0, atol=1e-12)
Smax = max(np.linalg.norm(S(z, t)) for z in np.linspace(-lam, 0, 161) for t in np.linspace(0, T, 161))
chk("(b) max|S| = E0^2/eta0 (nonzero)", Smax, E0**2/eta0, rtol=1e-2)
zb, tb = -0.37*lam, 0.13*T
chk("(b) S formula", S(zb, tb)[2], E0**2/eta0*np.sin(2*w/c*zb)*np.sin(2*w*tb))
wd = lambda z, t: 0.5*eps0*E(z, t)@E(z, t) + 0.5*mu0*H(z, t)@H(z, t)
zg = np.linspace(-lam, 0, 201)
mx = min(max(wd(z, t) for z in zg) for t in np.linspace(0, T, 401))
print("     (c) min over t of max over z of w / (2 eps0 E0^2) =", mx/(2*eps0*E0**2), "(>0 => False)")
chk("(c) never zero everywhere", mx > 0.1*eps0, True)
# (d) zeros fixed in time
z1 = zeros_of(lambda z: E(z, 0.1*T)[0], -2*lam+1e-4, -1e-4)
z2 = zeros_of(lambda z: E(z, 0.35*T)[0], -2*lam+1e-4, -1e-4)
chk("(d) Ex zeros same at two t", z1, z2, atol=1e-9)
chk("(d) spacing lambda/2", np.diff(z1)/lam, [0.5]*(len(z1)-1))
# (e) peak instants at antinodes
tt = np.linspace(0, T/2, 20001, endpoint=False)
tE = tt[np.argmax([abs(E(-lam/4, t)[0]) for t in tt])]
tH = tt[np.argmax([abs(H(0.0, t)[1]) for t in tt])]
chk("(e) peak instants differ by T/4", abs(tE - tH)/T, 0.25, atol=1e-3)
# (f) handedness: u.[E(0) x E(T/4)], Lecture 24
Eci = lambda z, t: X*np.cos(w*(t - z/c)) + Y*np.sin(w*(t - z/c))
Ecr = lambda z, t: -Eci(0.0, t + z/c)
zf = -0.3*lam
hi = Z@np.cross(Eci(zf, 0), Eci(zf, T/4)); hr = (-Z)@np.cross(Ecr(zf, 0), Ecr(zf, T/4))
print(f"     incident hand {'R' if hi>0 else 'L'}, reflected hand {'R' if hr>0 else 'L'}")
chk("(f) reflected is left (False)", hr < 0 and hi > 0, True)

print("=== 26.3 ===")
def G(eta2): return (eta2 - eta0)/(eta2 + eta0)
zp = np.linspace(0, 1.0, 20001)  # air z>0, lambda=1 m, beta=2pi
for name, eta2 in [("(i) PEC", 0.0), ("(ii) er=4", eta0/2), ("(iii) er=mur=5", eta0*np.sqrt(5/5))]:
    g = G(eta2)
    mag = np.abs(np.exp(1j*2*pi*zp) + g*np.exp(-1j*2*pi*zp))
    print(f"     {name}: Gamma={g:+.4f}, |E| in [{mag.min():.4f},{mag.max():.4f}], argmin z={zp[np.argmin(mag)]:.4f}")
chk("(ii) Gamma", G(eta0/2), -1/3)
mag = np.abs(np.exp(1j*2*pi*zp) + G(eta0/2)*np.exp(-1j*2*pi*zp))
chk("(ii) min,max", [mag.min(), mag.max()], [2/3, 4/3])
chk("(ii) min at interface", mag[0], 2/3)
chk("(iii) Gamma=0", G(eta0), 0, atol=1e-15)

print("=== 26.4 ===")
P = 3; Ab = 2e-6; Am = 4e-4
chk("student S", P/Ab, 1.5e6); chk("student p", 2*P/Ab/c, 1e-2); chk("student F [uN]", 2*P/Ab/c*Am*1e6, 4)
chk("mirror F [nN]", 2*P/Ab/c*Ab*1e9, 20); chk("absorber F [nN]", P/c*1e9, 10)
chk("ratio", Am/Ab, 200)

print("=== 26.5 ===")
Si = 600; E0 = np.sqrt(2*eta0*Si)
f = 1e9; w = 2*pi*f; T = 1/f
E, H, _, _ = pec_fields(E0*X, w, c, eta0)
Js = lambda t: np.cross(-Z, H(0.0, t))
# J_s x (mean B on two faces) = J_s x mu0 H/2
Pm = tavg(lambda t: np.cross(Js(t), 0.5*mu0*H(0.0, t)), T)
chk("mirror p [uPa] (Js x B/2)", Pm[2]*1e6, 4); chk("absorber p [uPa]", Si/c*1e6, 2)
chk("forces [mN]", [Pm[2]*400*1e3, Si/c*400*1e3], [1.6, 0.8])
chk("E0 [V/m]", E0, 673, rtol=1e-3)
chk("Js peak [A/m]", max(np.linalg.norm(Js(t)) for t in np.linspace(0, T, 1001)), 3.57)
chk("eps0 E0^2 [uPa]", eps0*E0**2*1e6, 4)

print("=== 26.6 ===")
f = 3e8; w = 2*pi*f; T = 1/f; d = 0.375; bt = w/c
E, H, Ei, Er = pec_fields(5*Y, w, c, eta0, zm=d)
chk("beta, beta d", [bt, bt*d], [2*pi, 3*pi/4])
zs = np.linspace(-0.6, d, 23); tsm = np.linspace(0, T, 17)
dEr = max(abs(Er(z, t)[1] - 5*np.sin(w*t + 2*pi*z)) for z in zs for t in tsm)
chk("(a) Er = y5 sin(wt+2pi z)", dEr, 0, atol=1e-9)
chk("(a) Er x,z comps", max(abs(Er(z, t)[[0, 2]]).max() for z in zs for t in tsm), 0, atol=1e-12)
dE = max(abs(E(z, t)[1] - 10*np.sin(bt*(z-d))*np.sin(w*t-bt*d)) for z in zs for t in tsm)
chk("(b) E form", dE, 0, atol=1e-9)
dH = max(np.abs(H(z, t) - (-X)*(1/(12*pi))*np.cos(bt*(z-d))*np.cos(w*t-bt*d)).max() for z in zs for t in tsm)
chk("(b) H form", dH, 0, atol=1e-12)
# Faraday by FD: dEy/dz = mu0 dHx/dt
h = 1e-6; ht = 1e-13
res = max(abs((E(z+h, t)[1]-E(z-h, t)[1])/(2*h) - mu0*(H(z, t+ht)[0]-H(z, t-ht)[0])/(2*ht)) for z in zs[:5] for t in tsm[:5])
chk("(b) Faraday FD residual", res, 0, atol=1e-3)
tq = T*0.137
zE = zeros_of(lambda z: E(z, tq)[1], -0.4999, d+1e-4); zE = zE[zE <= d+1e-9]
zH = zeros_of(lambda z: H(z, tq)[0], -0.4999, d)
chk("(c) E nodes [cm]", np.sort(zE)*100, [-12.5, 37.5], atol=1e-5)
chk("(c) H nodes [cm]", np.sort(zH)*100, [-37.5, 12.5], atol=1e-5)
dJ = max(np.abs(np.cross(-Z, H(d, t)) - Y*(1/(12*pi))*np.cos(w*t-3*pi/4)).max() for t in tsm)
chk("(d) Js form", dJ, 0, atol=1e-12); chk("(d) 1/12pi [mA/m]", 1e3/(12*pi), 26.5)
chk("(d) Js = 2Ei(d)/eta0", max(np.abs(np.cross(-Z, H(d, t)) - 2*Ei(d, t)/eta0).max() for t in tsm), 0, atol=1e-12)
tt = np.linspace(0, T, 200001)
Ey0 = np.array([E(0.0, t)[1] for t in tt[::50]]); Hx0 = np.array([H(0.0, t)[0] for t in tt[::50]])
chk("(e) |Ey|,|Hx| [V/m, mA/m]", [abs(Ey0).max(), abs(Hx0).max()*1e3], [7.07, 18.8])
# first local max of |Ey(0,t)| for t>0
r = minimize_scalar(lambda tn: -abs(E(0.0, tn*1e-9)[1]), bounds=(1e-6, T/4*1e9), method='bounded', options={'xatol': 1e-9})
chk("(e) first peak t [ns]", r.x, 0.417)
chk("(e) 1/8f [ns]", 1/(8*f)*1e9, 0.417)

print("=== 26.7 ===")
er = 2.25; f = 2e9; w = 2*pi*f; T = 1/f; v = c/np.sqrt(er); eta1 = eta0/np.sqrt(er); e1 = er*eps0; E0 = 30
lam = v/f; b1 = w/v
chk("eta1/pi, lam [cm], beta/pi", [eta1/pi, lam*100, b1/pi], [80, 10, 20])
E, H, _, _ = pec_fields(E0*X, w, v, eta1)
S = lambda z, t: np.cross(E(z, t), H(z, t))
zg = np.linspace(-lam, 0, 161); tg = np.linspace(0, T, 161)
Sm = max(np.linalg.norm(S(z, t)) for z in zg for t in tg)
chk("(a) max|S| [W/m2]", Sm, 3.58)
chk("(a) S at z=-1.25cm, wt=pi/4", S(-0.0125, T/8), [0, 0, -3.58])
wd = lambda z, t: 0.5*e1*E(z, t)@E(z, t) + 0.5*mu0*H(z, t)@H(z, t)
wav = [tavg(lambda t: wd(z, t), T, 400) for z in [-0.003, -0.011, -0.027]]
chk("(b) <w> at 3 z [J/m3]", wav, [1.79e-8]*3)
Wt = [quad(lambda z: wd(z, t), -lam/4, 0)[0] for t in np.linspace(0, T, 7)]
chk("(c) W(t) const [J/m2]", Wt, [4.48e-10]*7)
chk("(c) eps1 E0^2 lam/4", e1*E0**2*lam/4, 4.48e-10)
h = 1e-6; ht = 1e-14
res = max(abs((wd(z, t+ht)-wd(z, t-ht))/(2*ht) + (S(z+h, t)[2]-S(z-h, t)[2])/(2*h)) for z in zg[::20] for t in tg[::20])
chk("check: Poynting FD residual / scale", res/(w*e1*E0**2), 0, atol=1e-4)
zc = np.linspace(-lam/4, 0, 2001)
chk("(d) wt=0: max|E| ~0", max(abs(E(z, 0)[0]) for z in zc), 0, atol=1e-9)
chk("(d) wt=0: w peak z [cm]", zc[np.argmax([wd(z, 0) for z in zc])]*100, 0, atol=1e-6)
chk("(d) wt=pi/2: max|H| ~0", max(abs(H(z, T/4)[1]) for z in zc), 0, atol=1e-12)
chk("(d) wt=pi/2: w peak z [cm]", zc[np.argmax([wd(z, T/4) for z in zc])]*100, -2.5, atol=1e-6)
Sz = [S(z, t)[2] for z in zc[1:-1:50] for t in np.linspace(0.01*T, 0.24*T, 9)]
chk("(d) Sz<0 in cell for 0<wt<pi/2", max(Sz) < 0, True)
Sz2 = [S(z, t)[2] for z in zc[1:-1:50] for t in np.linspace(0.26*T, 0.49*T, 9)]
chk("(d) Sz>0 for pi/2<wt<pi (returns)", min(Sz2) > 0, True)

print("=== 26.8 ===")
er = 4; f = 1.5e9; E0 = 7.5; eta2 = eta0/np.sqrt(er); g = (eta2-eta0)/(eta2+eta0); b0 = 2*pi*f/c
zn = np.linspace(-0.3, 0, 30001)
mag = np.abs(E0*(np.exp(-1j*b0*zn) + g*np.exp(1j*b0*zn)))
chk("(a)(b) max,min", [mag.max(), mag.min()], [10, 5])
mins = zn[1:-1][(mag[1:-1] < mag[:-2]) & (mag[1:-1] < mag[2:])]
mins = np.append(mins, 0.0) if mag[-1] <= mag[-2] else mins
chk("(b) minima [cm]", np.sort(mins)*100, [-20, -10, 0], atol=1e-2)
chk("(a) Gamma", g, -1/3)
wv = 2*pi*f; T = 1/f; tau = 1+g
Ex = lambda z, t: E0*np.cos(wv*t - b0*z) + g*E0*np.cos(wv*t + b0*z)
Hy = lambda z, t: (E0*np.cos(wv*t - b0*z) - g*E0*np.cos(wv*t + b0*z))/eta0
Sav = [tavg(lambda t: Ex(z, t)*Hy(z, t), T, 2000) for z in [-0.013, -0.071]]
chk("(c) <S> air [mW/m2]", np.array(Sav)*1e3, [66.3, 66.3])
St = tavg(lambda t: (tau*E0*np.cos(wv*t))**2/eta2, T, 2000)
chk("(c) <S> transmitted [mW/m2]", St*1e3, 66.3)
chk("(c) fraction", St/(E0**2/(2*eta0)), 0.889, rtol=1e-3)
gs = [(eta0/np.sqrt(e)-eta0)/(eta0/np.sqrt(e)+eta0) for e in np.linspace(1.0001, 100, 500)]
chk("(d) all er>1 give Gamma<0", max(gs) < 0, True)
chk("(d) Gamma=+1/3 needs er", ((1-1/3)/(1+1/3))**2, 0.25)

print("=== 26.9 ===")
w = 3*pi*1e9; k = 20*pi
Ef = lambda y, t: X*120*np.cos(k*y)*np.cos(w*t)
Hu = lambda y, t: Z*np.sin(k*y)*np.sin(w*t)   # H for H0=1
h = 1e-7; ht = 1e-14
pts = [(y, t) for y in np.linspace(0.003, 0.09, 7) for t in np.linspace(1e-11, 6e-10, 7)]
# curl E (only d/dy): (dEz/dy, 0, -dEx/dy)
def curlE(y, t):
    dE = (Ef(y+h, t)-Ef(y-h, t))/(2*h); return np.array([dE[2], 0, -dE[0]])
A = np.array([-mu0*(Hu(y, t+ht)-Hu(y, t-ht))[2]/(2*ht) for y, t in pts])
B = np.array([curlE(y, t)[2] for y, t in pts])
H0 = (A@B)/(A@A)
chk("(a) H0 [A/m]", H0, -2/pi)
def curlH(y, t, H0=H0):
    dH = H0*(Hu(y+h, t)-Hu(y-h, t))/(2*h); return np.array([dH[2], 0, -dH[0]])
A2 = np.array([(Ef(y, t+ht)-Ef(y, t-ht))[0]/(2*ht) for y, t in pts])
B2 = np.array([curlH(y, t)[0] for y, t in pts])
eps = (A2@B2)/(A2@A2)
chk("(a) eps_r", eps/eps0, 4)
eta1 = np.sqrt(mu0/eps); v = 1/np.sqrt(mu0*eps)
chk("eta1/pi", eta1/pi, 60)
Ep = lambda y, t: X*60*np.cos(w*t - k*y); Em = lambda y, t: X*60*np.cos(w*t + k*y)
Hp = lambda y, t: np.cross(Y, Ep(y, t))/eta1; Hm = lambda y, t: np.cross(-Y, Em(y, t))/eta1
dd = max(np.abs(Ep(y, t)+Em(y, t)-Ef(y, t)).max() + np.abs(Hp(y, t)+Hm(y, t)-H0*Hu(y, t)).max() for y, t in pts)
chk("(b) two waves sum to given", dd, 0, atol=1e-6)
chk("(b) H+ = -z (1/pi)cos", Hp(0.013, 1e-10), -Z/pi*np.cos(w*1e-10 - k*0.013))
chk("(b) H- = +z (1/pi)cos", Hm(0.013, 1e-10), Z/pi*np.cos(w*1e-10 + k*0.013))
chk("(b) lambda [cm]", 2*pi/k*100, 10); chk("(b) v = c/2", v, c/2)
T = 2*pi/w
Sv = lambda y, t: np.cross(Ef(y, t), H0*Hu(y, t))
chk("(c) <S> ~ 0", max(np.abs(tavg(lambda t: Sv(y, t), T, 400)).max() for y in [0.011, 0.031, 0.062]), 0, atol=1e-9)
chk("(c) S formula", Sv(0.013, 1e-10)[1], 60/pi*np.sin(40*pi*0.013)*np.sin(2*w*1e-10))
wd = lambda y, t: 0.5*eps*Ef(y, t)@Ef(y, t) + 0.5*mu0*H0**2*Hu(y, t)@Hu(y, t)
chk("(c) <w> [J/m3]", [tavg(lambda t: wd(y, t), T, 400) for y in [0.011, 0.04]], [1.27e-7]*2)
y1 = brentq(lambda y: np.cos(k*y), 1e-4, 0.049)
chk("(d) y1 [cm]", y1*100, 2.5)
dJ = max(np.abs(np.cross(-Y, H0*Hu(y1, t)) - X*(2/pi)*np.sin(w*t)).max() for t in np.linspace(0, T, 13))
chk("(d) Js = x (2/pi) sin wt", dJ, 0, atol=1e-9)
chk("(e) y=0: E amp, H", [max(abs(Ef(0, t)[0]) for t in np.linspace(0, T, 101)), np.abs(Hu(0, 0.3*T)).max()], [120, 0], atol=1e-12)

print("=== 26.10 ===")
f = 1e9; w = 2*pi*f; sg = 3.5e7; E0 = 100; T = 1/f
chk("w eps0", w*eps0, 1/18); chk("sigma/w eps0", sg/(w*eps0), 6.3e8)
gam = np.sqrt(1j*w*mu0*(sg + 1j*w*eps0)); eta2 = 1j*w*mu0/gam
tau = 2*eta2/(eta2+eta0); Gm = (eta2-eta0)/(eta2+eta0)
dlt = 1/gam.real
chk("delta exact [um]", dlt*1e6, 2.69); chk("delta formula [um]", 1/np.sqrt(pi*f*mu0*sg)*1e6, 2.69)
chk("Rs = Re eta2 [mOhm]", eta2.real*1e3, 10.6); chk("1/(sigma delta) [mOhm]", sg*np.sqrt(pi*f*mu0*sg)**-1*0+1/(sg/np.sqrt(pi*f*mu0*sg))*1e3, 10.6)
Jz = lambda z: sg*tau*E0*np.exp(-gam*z)
Lz = 60*dlt
Jint = quad(lambda z: Jz(z).real, 0, Lz, limit=400)[0] + 1j*quad(lambda z: Jz(z).imag, 0, Lz, limit=400)[0]
chk("(b) |int J dz| [A/m]", abs(Jint), 0.531); chk("(b) 2E0/eta0", 2*E0/eta0, 0.531)
chk("(b) |int J dz| exact 4 sig", abs(Jint), 0.5305, rtol=2e-4)
chk("(b) |J(0)| [A/m2]", abs(Jz(0)), 2.79e5)
heat = quad(lambda z: 0.5*abs(Jz(z))**2/sg, 0, Lz, limit=400)[0]
Si = E0**2/(2*eta0)
chk("(c) heat [mW/m2]", heat*1e3, 1.49); chk("(c) <Si>", Si, 13.26, rtol=1e-3)
chk("(c) fraction", heat/Si, 1.13e-4); chk("(c) 1-|G|^2", 1-abs(Gm)**2, 1.13e-4)
chk("(c) 4Rs/eta0 (approx)", 4/(sg*dlt)/eta0 if False else 4*np.sqrt(pi*f*mu0/sg)/eta0, 1.13e-4)
Hz_ = lambda z: tau*E0/eta2*np.exp(-gam*z)
Pav = quad(lambda z: 0.5*np.real(Jz(z)*np.conj(mu0*Hz_(z))), 0, Lz, limit=400)[0]
chk("(d) <P> [nPa]", Pav*1e9, 88.4); chk("(d) <P> 4 sig", Pav*1e9, 88.41, rtol=1e-4)
chk("(d) (1+|G|^2)Si/c [nPa]", (1+abs(Gm)**2)*Si/c*1e9, Pav*1e9, rtol=1e-6)
print(f"     deficit vs mirror: {(1-Pav/(2*Si/c))*100:.4f} %")
dirv = np.cross(X*np.real(Jz(0)), Y*np.real(mu0*Hz_(0)))
chk("(d) direction +z", np.sign(dirv[2]), 1)
zq = np.linspace(0, Lz, 60001)
def Pinst(t):
    J = np.real(Jz(zq)*np.exp(1j*w*t)); Bv = np.real(mu0*Hz_(zq)*np.exp(1j*w*t))
    return np.trapezoid(J*Bv, zq)
tg = np.linspace(0, T/2, 2001)
Pt = np.array([Pinst(t) for t in tg])
chk("(d) peak inst [nPa]", Pt.max()*1e9, 177); chk("(d) min inst ~0 [nPa]", Pt.min()*1e9, 0, atol=0.05)
chk("(d) mean inst = <P>", Pt.mean()*1e9, Pav*1e9, rtol=1e-3)

print("=== 26.11 ===")
P = 3e4; A = 3; m = 1e-3; lam = 1e-6; hP = 6.63e-34
Si = P/A; E0 = np.sqrt(2*eta0*Si)
chk("(a) E0 [kV/m]", E0/1e3, 2.75); chk("(a) Js [A/m]", 2*E0/eta0, 14.6)
Fm = 2*P/c; F9 = (1 + 0.9)*P/c
chk("(b) F mirror, 90% [mN]", [Fm*1e3, F9*1e3], [0.2, 0.19]); chk("(b) a [m/s2]", [Fm/m, F9/m], [0.2, 0.19])
chk("(c) absorbed [kW]", 0.1*P/1e3, 3)
Eph = hP*c/lam; N = P/Eph
chk("(d) Eph [J]", Eph, 1.99e-19); chk("(d) rate", N, 1.51e23); chk("(d) h/lam", hP/lam, 6.63e-28)
chk("(d) F photons [N]", 2*N*hP/lam, 2e-4)
chk("(e) v [m/s]", [Fm/m*3600, F9/m*3600], [720, 684])
chk("check ratio", F9/Fm, 0.95)

print("=== 26.12 ===")
L = 0.15; E0 = 50
fr = zeros_of(lambda f: np.sin(2*pi*f/c*L), 0.5e9, 3.5e9, 3001)
chk("(a) f_m [GHz]", fr/1e9, [1, 2, 3])
def cav(m):
    w = 2*pi*m*1e9; b = w/c
    E = lambda z, t: X*2*E0*np.sin(b*z)*np.sin(w*t)
    H = lambda z, t: Y*(2*E0/eta0)*np.cos(b*z)*np.cos(w*t)
    return w, b, E, H
w, b, E, H = cav(3); T = 2*pi/w
chk("(b) w/pi [1e9], beta/pi, lam[cm]", [w/pi/1e9, b/pi, 2*pi/b*100], [6, 20, 10])
chk("(b) 2E0/eta0", 2*E0/eta0, 5/(6*pi)); chk("(b) 0.265", 5/(6*pi), 0.265)
zE = zeros_of(lambda z: E(z, T/4)[0], 1e-4, L-1e-4); zH = zeros_of(lambda z: H(z, 0)[1], 1e-4, L-1e-4)
chk("(b) E nodes [cm]", zE*100, [5, 10], atol=1e-6); chk("(b) H nodes [cm]", zH*100, [2.5, 7.5, 12.5], atol=1e-6)
tg = np.linspace(0, T, 13)
J0 = lambda t: np.cross(Z, H(0.0, t)); JL = lambda t: np.cross(-Z, H(L, t))
chk("(c) Js(0) = -x .265 cos", max(np.abs(J0(t) - (-X)*5/(6*pi)*np.cos(w*t)).max() for t in tg), 0, atol=1e-12)
chk("(c) Js(L) = -x .265 cos", max(np.abs(JL(t) - (-X)*5/(6*pi)*np.cos(w*t)).max() for t in tg), 0, atol=1e-12)
P0 = tavg(lambda t: np.cross(J0(t), 0.5*mu0*H(0.0, t)), T); PL = tavg(lambda t: np.cross(JL(t), 0.5*mu0*H(L, t)), T)
chk("(d) <P> on z=0 wall [1e-8 Pa]", P0*1e8, [0, 0, -2.21], atol=1e-12)
chk("(d) <P> on z=L wall [1e-8 Pa]", PL*1e8, [0, 0, 2.21], atol=1e-12)
wd = lambda z, t: 0.5*eps0*E(z, t)@E(z, t) + 0.5*mu0*H(z, t)@H(z, t)
chk("(d) W(t) [nJ/m2]", [quad(lambda z: wd(z, t), 0, L)[0]*1e9 for t in np.linspace(0, T, 5)], [3.32]*5)
Ep = lambda z, t: X*E0*np.cos(w*t - b*z); Em = lambda z, t: -X*E0*np.cos(w*t + b*z)
chk("(e) two waves", max(np.abs(Ep(z, t)+Em(z, t)-E(z, t)).max() for z in np.linspace(0, L, 9) for t in tg), 0, atol=1e-9)
chk("(e) each <S> [W/m2]", E0**2/(2*eta0), 3.32); chk("(e) 2<S>/c [1e-8]", 2*E0**2/(2*eta0)/c*1e8, 2.21)
w2, b2, E2, H2 = cav(2)
r = np.cross(-Z, H2(L, 0.0))[0]/np.cross(Z, H2(0.0, 0.0))[0]
chk("(e) m=2: Js(L)/Js(0)", r, -1)
h = 1e-7; ht = 1e-14
res = max(abs((E(z+h, t)[0]-E(z-h, t)[0])/(2*h) + mu0*(H(z, t+ht)[1]-H(z, t-ht)[1])/(2*ht)) for z in [0.013, 0.07] for t in [1e-11, 7e-11])
chk("check Faraday FD (dEx/dz=-mu0 dHy/dt)", res, 0, atol=1e-2)
chk("check E=0 on walls", max(abs(E(0, t)[0]) + abs(E(L, t)[0]) for t in tg), 0, atol=1e-9)

print(f"\nFAIL count: {nf}")
