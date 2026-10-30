"""Numbers for the waves-in-media figures (figs_media.py). Each check prints PASS/FAIL."""
import numpy as np
mu0 = 4e-7*np.pi; eps0 = 8.8541878128e-12; c0 = 1/np.sqrt(mu0*eps0); eta0 = np.sqrt(mu0/eps0)
DB = 20*np.log10(np.e)
ok = True
def chk(name, got, want, rtol=5e-3, atol=0):
    global ok
    good = np.allclose(got, want, rtol=rtol, atol=atol)
    ok &= good
    print(("PASS " if good else "FAIL ") + f"{name}: got {got}, want {want}")
def gam_eta(w, mu, sig, eps):
    return np.sqrt(1j*w*mu*(sig+1j*w*eps)), np.sqrt(1j*w*mu/(sig+1j*w*eps))

print("== 1. family tree: limits of gamma^2 = jw mu (sigma + jw eps)")
w = 2*np.pi*1e6; eps = 4*eps0
g, _ = gam_eta(w, mu0, 0.0, eps); chk("lossless gamma = j w sqrt(mu eps)", g, 1j*w*np.sqrt(mu0*eps))
g, _ = gam_eta(w, mu0, 5.8e7, eps0); chk("good conductor gamma ~ sqrt(j w mu sigma)", g, np.sqrt(1j*w*mu0*5.8e7))
delta = 1/np.sqrt(np.pi*1e6*mu0*5.8e7); chk("sqrt(j w mu sigma) = (1+j)/delta", np.sqrt(1j*w*mu0*5.8e7), (1+1j)/delta)
# plasma: sigma = -j N q^2/(m w) = -j w_p^2 eps0 / w
wp = 2*np.pi*9e6
for f in (5e6, 20e6):
    ww = 2*np.pi*f
    g, _ = gam_eta(ww, mu0, -1j*wp**2*eps0/ww, eps0)
    chk(f"plasma gamma^2 = (wp^2 - w^2)/c^2 at {f/1e6:.0f} MHz", g**2, (wp**2-ww**2)/c0**2)
Ne = 1e12; q = 1.602176634e-19; me = 9.1093837e-31
fp = np.sqrt(Ne*q**2/(me*eps0))/(2*np.pi)
chk("ionosphere f_p for N = 1e12 m^-3 ~ 9 MHz (Kudeki ECE 458: sqrt(80.6 N))", fp, np.sqrt(80.6*Ne), rtol=2e-3)
chk("  ... = 8.98 MHz", fp/1e6, 8.98, rtol=2e-3)
# TL: gamma^2 = (R + jwL)(G + jwC)  <->  jw mu (sigma + jw eps) with R = 0, L = mu, C = eps, G = sigma
L, C, G = mu0, eps, 1e-3
chk("TL gamma with R=0, L=mu, C=eps, G=sigma equals plane-wave gamma", np.sqrt((1j*w*L)*(G+1j*w*C)), gam_eta(w, mu0, G, eps)[0])
chk("TL Z0 with same map equals eta", np.sqrt((1j*w*L)/(G+1j*w*C)), gam_eta(w, mu0, G, eps)[1])

print("== 2. angle bookkeeping, theta = 50 deg")
th = np.radians(50); p = np.tan(th)
J = p + 1j            # (sigma + j w eps)/(w eps)
chk("angle of (sigma + j w eps) = 90 - theta", np.degrees(np.angle(J)), 40)
g2 = 1j*J; chk("angle of gamma^2 = 180 - theta", np.degrees(np.angle(g2)), 130)
g = np.sqrt(g2); chk("angle of gamma = 90 - theta/2", np.degrees(np.angle(g)), 65)
e2 = 1j/J; chk("angle of eta^2 = theta", np.degrees(np.angle(e2)), 50)
e = np.sqrt(e2); chk("tau = angle eta = theta/2", np.degrees(np.angle(e)), 25)
chk("|gamma|/(w sqrt(mu eps)) = (1+p^2)^(1/4)", abs(g), (1+p**2)**0.25)
chk("  ... = 1.247", abs(g), 1.247, rtol=1e-3)
chk("|eta|/sqrt(mu/eps) = (1+p^2)^(-1/4) = 0.802", abs(e), 0.802, rtol=1e-3)
chk("alpha/beta = tan tau = 0.466", g.real/g.imag, 0.466, rtol=2e-3)
chk("p = tan 50 = 1.19", p, 1.19, rtol=2e-3)

print("== 3. snapshot rows")
def row(p):
    t = np.arctan(p)/2; ab = np.tan(t)
    return np.degrees(t), ab, 1/(2*np.pi*ab)   # tau deg, alpha/beta, delta/lambda
for p, tau_w, ab_w, dl_w in ((0.2, 5.65, 0.0990, 1.61), (100, 44.71, 0.990, 0.161)):
    t, ab, dl = row(p)
    chk(f"p={p}: tau", t, tau_w, rtol=2e-3); chk(f"p={p}: alpha/beta", ab, ab_w, rtol=3e-3); chk(f"p={p}: delta/lambda", dl, dl_w, rtol=4e-3)
# loss per wavelength
for p, dbw in ((0.2, 5.40), (100, 54.0)):
    t = np.arctan(p)/2
    chk(f"p={p}: dB per wavelength = 2 pi 8.686 tan(tau)", 2*np.pi*DB*np.tan(t), dbw, rtol=4e-3)
# evanescent plasma row: f = fp/2 -> kappa = (w/c) sqrt(wp^2/w^2 - 1) ; eta = j X
ww = wp/2; kap = (ww/c0)*np.sqrt((wp/ww)**2-1)
g, et = gam_eta(ww, mu0, -1j*wp**2*eps0/ww, eps0)
chk("plasma at fp/2: gamma real = kappa", g, kap)
chk("plasma at fp/2: eta purely imaginary (angle 90 deg)", np.degrees(np.angle(et)), 90)
chk("plasma at fp/2: 1/kappa = 6.12 m", 1/kap, 6.12, rtol=3e-3)
chk("time-avg S = 1/2 Re{E H*} = 0 for imaginary eta", 0.5*np.real(1/np.conj(et)), 0, atol=1e-15)

print("== 4. phase velocity across media (exact)")
mats = {"copper": (5.8e7, 1), "seawater": (4.0, 81), "moist soil": (1e-2, 10), "fresh water": (1e-3, 80)}
def vp(f, s, er):
    g, _ = gam_eta(2*np.pi*f, mu0, s, er*eps0); return 2*np.pi*f/g.imag
for name, (s, er) in mats.items():
    print(f"     {name}: fc = {s/(2*np.pi*er*eps0):.3g} Hz")
chk("seawater fc = 0.89 GHz", 4/(2*np.pi*81*eps0)/1e9, 0.888, rtol=2e-3)
chk("moist soil fc = 18 MHz", 1e-2/(2*np.pi*10*eps0)/1e6, 18.0, rtol=3e-3)
chk("fresh water fc = 225 kHz", 1e-3/(2*np.pi*80*eps0)/1e3, 225, rtol=3e-3)
chk("copper vp at 60 Hz = sqrt(2w/mu sigma) = 3.22 m/s", vp(60, 5.8e7, 1), 3.22, rtol=3e-3)
chk("copper vp at 1 GHz = 13.1 km/s", vp(1e9, 5.8e7, 1)/1e3, 13.1, rtol=3e-3)
chk("seawater vp at 1 kHz = 5.0e4 m/s", vp(1e3, 4, 81), 5.0e4, rtol=3e-3)
chk("seawater vp at 100 GHz -> c/9", vp(1e11, 4, 81)/c0, 1/9, rtol=2e-3)
chk("dielectric eps_r = 4: vp = c/2", 1/np.sqrt(mu0*4*eps0)/c0, 0.5)
for f in (9.5e6, 12e6, 30e6):
    ww = 2*np.pi*f; vpp = c0/np.sqrt(1-(wp/ww)**2); vgg = c0*np.sqrt(1-(wp/ww)**2)
    chk(f"plasma at {f/1e6:g} MHz: vp vg = c^2", vpp*vgg, c0**2)
chk("plasma vp/c at 12 MHz = 1.51", 1/np.sqrt(1-(9/12)**2), 1.512, rtol=2e-3)
print("== 4b. loss per wavelength depends only on p")
for p, want in ((0.01, 0.273), (0.1, 2.72), (1, 22.6), (10, 49.4), (1e4, 54.6)):
    chk(f"p={p}: 2*pi*8.686*tan(atan(p)/2) dB/lambda", 2*np.pi*DB*np.tan(np.arctan(p)/2), want, rtol=4e-3)
chk("8.686 dB per skin depth in every medium", DB, 8.686, rtol=1e-4)

print("== 4c. material markers on the loss-per-wavelength panel")
for name, s_, er, f, want in (("seawater 1 GHz", 4.0, 81, 1e9, 20.7), ("moist soil 100 kHz", 1e-2, 10, 1e5, 54.3),
                              ("fresh water 100 MHz", 1e-3, 80, 1e8, 0.0614)):
    p = s_/(2*np.pi*f*er*eps0)
    chk(f"{name}: dB per lambda", 2*np.pi*DB*np.tan(np.arctan(p)/2), want, rtol=4e-3)
    g, _ = gam_eta(2*np.pi*f, mu0, s_, er*eps0)
    chk(f"{name}: same from exact gamma (8.686 * alpha * lambda)", DB*g.real*2*np.pi/g.imag, want, rtol=4e-3)
print("== 5. TL analogy directions")
chk("x cross y = z (E along x, H along y travels +z)", np.cross([1,0,0],[0,1,0]), [0,0,1])
print("ALL PASS" if ok else "SOME FAIL")
