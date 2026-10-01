"""V2-magnetics: independent re-solution of 11.8, 12.10, 13.9, 14.10, 15.3, 15.10.
Brute-force routes: sheet superposition and method-of-lines PDE (11.8), numerical
Biot-Savart quadrature + least-squares null search (12.10), thin-sheet sums and FD
curls (13.9), line integrals of the induced field with node potentials (14.10),
FD grad/curl/d/dt (15.3), np.cross sheet fields, finite-strip Biot-Savart, shoelace
orientation (15.10). Page values are transcribed and compared at their stated precision."""
import numpy as np
from scipy.integrate import quad, solve_ivp
from scipy.optimize import brentq, least_squares

e = 1.602176634e-19; me = 9.1093837015e-31; eps0 = 8.8541878128e-12
mu0 = 4e-7*np.pi; c0 = 299792458.0
xh, yh, zh = np.eye(3)
NF = [0]

def ok(label, cond, info=""):
    print(f"{'PASS' if cond else 'FAIL'}  {label}  {info}")
    if not cond:
        NF[0] += 1

def sig(label, val, stated, n):
    """page value `stated` given to n significant figures"""
    if stated == 0:
        good = abs(val) < 1e-9
    else:
        ulp = 10.0**(np.floor(np.log10(abs(stated))) - n + 1)
        good = abs(val - stated) <= 0.5*ulp*1.02
    ok(label, good, f"computed {val:.6g} | page {stated:g} ({n} s.f.)")

def vec(label, val, stated, tol):
    val = np.asarray(val, float)
    ok(label, np.allclose(val, stated, atol=tol, rtol=0),
       f"computed {np.array2string(val, precision=6)} | page {stated}")

def shoelace(pts):
    p = np.asarray(pts, float)
    return 0.5*np.sum(p[:, 0]*np.roll(p[:, 1], -1) - np.roll(p[:, 0], -1)*p[:, 1])

def curl(F, r, h=1e-5):
    Jm = np.zeros((3, 3))
    for j in range(3):
        dr = np.zeros(3); dr[j] = h
        Jm[:, j] = (F(r + dr) - F(r - dr))/(2*h)
    return np.array([Jm[2, 1]-Jm[1, 2], Jm[0, 2]-Jm[2, 0], Jm[1, 0]-Jm[0, 1]]), Jm

# =====================================================================
print("== 11.8 Relaxation time versus collision time ==")
eps_si = 11.7*eps0; N_si = 1.0e20; m_st = 0.26*me; tau_si = 1.8e-13
rho0 = 46.8*eps0; beta = 2.0
mob = e*tau_si/m_st
sig_si = N_si*e**2*tau_si/m_st
taur_si = eps_si/sig_si
sig("11.8b mobility e*tau/m* [m^2/Vs]", mob, 0.122, 3)
sig("11.8b sigma [S/m]", sig_si, 1.95, 3)
sig("11.8b tau_r [s]", taur_si, 5.31e-11, 3)
sig("11.8b tau_r [ps]", taur_si*1e12, 53, 2)

def Ex_sheets(x, Lt=200*np.pi):
    """E_x at x = sum of sheets rho dx'/(2 eps) sgn(x - x') = [Q(left of x) - Q(right of x)]/(2 eps).
    The infinite sum is only conditionally convergent (a sharp cut leaves an end dipole layer, i.e. an
    applied uniform field), so the ripple gets a smooth Gaussian taper exp(-(x'/Lt)^2) centred on x = 0
    (a zero of rho, not a crest): no applied field, and no symmetry about a crest is assumed.
    Oscillatory quadrature (QAWO, weight sin(beta x'))."""
    w = lambda xp: np.exp(-(xp/Lt)**2)
    left = quad(w, -6*Lt, x, weight='sin', wvar=beta, limit=5000)[0]
    right = quad(w, x, 6*Lt, weight='sin', wvar=beta, limit=5000)[0]
    return rho0*(left - right)/(2*eps_si)

sig("11.8b amplitude rho0/(beta eps) [V/m]", rho0/(beta*eps_si), 2, 3)
E0 = Ex_sheets(0.0)*xh
J0 = sig_si*E0
v0 = J0/(N_si*(-e))
sig("11.8b E_x(0) by sheet superposition [V/m]", E0[0], -2, 3)
sig("11.8b J_x(0) [A/m^2]", J0[0], -3.90, 3)
sig("11.8b v_x(0) [m/s]", v0[0], 0.244, 3)
ok("11.8a E_x = 0 on crest x=pi/4 and trough x=-pi/4", abs(Ex_sheets(np.pi/4)) < 2e-5 and abs(Ex_sheets(-np.pi/4)) < 2e-5,
   f"E(pi/4)={Ex_sheets(np.pi/4):.2e}, E(-pi/4)={Ex_sheets(-np.pi/4):.2e}")
xg = np.linspace(-np.pi/2, np.pi/2, 361)
Eg = np.array([Ex_sheets(x) for x in xg])
ok("11.8a page E_x(x,0) = -(rho0/(beta eps)) cos(beta x) matches sheet sum",
   np.allclose(Eg, -2*np.cos(2*xg), atol=2e-5), f"max dev {np.max(abs(Eg + 2*np.cos(2*xg))):.1e}")
ok("11.8a |E_x| max where rho = 0 (x = n pi/beta)", np.allclose(sorted(abs(xg[np.argsort(-abs(Eg))[:3]])), [0, np.pi/2, np.pi/2], atol=0.01))
ok("11.8b current at x=0 along -x, crest (rho>0) at +pi/4: charge flows crest -> trough", J0[0] < 0 and np.sin(beta*np.pi/4) > 0)
ok("11.8b electrons drift +x (trough -> crest)", v0[0] > 0)
sig("11.8b crest position pi/(2 beta) [m]", np.pi/(2*beta), 0.785, 3)
sig("11.8b rho0/e [m^-3]", rho0/e, 2.6e9, 2)

# method of lines on one period, spectral Gauss (zero-mean E) + continuity
Ng = 32; xgr = np.arange(Ng)*(2*np.pi/beta)/Ng
kk = np.fft.fftfreq(Ng, d=(2*np.pi/beta)/Ng)*2*np.pi
def E_of_rho(rho, eps):
    rk = np.fft.fft(rho); Ek = np.zeros_like(rk); nz = kk != 0
    Ek[nz] = rk[nz]/(eps*1j*kk[nz]); return np.real(np.fft.ifft(Ek))
def ddx(f): return np.real(np.fft.ifft(1j*kk*np.fft.fft(f)))
ic = Ng//4                       # x = pi/4 (crest; period is pi)
solA = solve_ivp(lambda t, r: -ddx(sig_si*E_of_rho(r, eps_si)), [0, taur_si], rho0*np.sin(beta*xgr), rtol=1e-11, atol=1e-25)
sig("11.8a rho(crest, tau_r)/rho0 = e^-1 (J = sigma E, MOL)", solA.y[ic, -1]/rho0, np.exp(-1), 6)

def drude_run(sigma, eps, tau, t_end, method, t_eval=None, rtol=1e-11):
    def f(t, yv):
        rho, J = yv[:Ng], yv[Ng:]
        return np.concatenate([-ddx(J), (sigma*E_of_rho(rho, eps) - J)/tau])
    y0 = np.concatenate([np.sin(beta*xgr), np.zeros(Ng)])
    Jsc = max(np.sqrt(sigma/(eps*tau)), sigma/eps)/beta      # current scale -> per-component atol (FFT round-off in empty modes)
    atol = np.concatenate([np.full(Ng, 1e-13), np.full(Ng, 1e-13*Jsc)])
    return solve_ivp(f, [0, t_end], y0, method=method, t_eval=t_eval, rtol=rtol, atol=atol, dense_output=True)

sig_cu = 5.8e7; N_cu = 8.5e28
taur_cu = eps0/sig_cu
tau_cu = sig_cu*me/(N_cu*e**2)
sig("11.8c Cu tau_r [s] (2 s.f.)", taur_cu, 1.5e-19, 2)
sig("11.8d Cu tau_r [s] (3 s.f.)", taur_cu, 1.53e-19, 3)
sig("11.8c Cu Drude tau [s]", tau_cu, 2.4e-14, 2)
sig("11.8c Cu tau/tau_r", tau_cu/taur_cu, 1.6e5, 2)
sig("11.8c Si tau_r/tau", taur_si/tau_si, 295, 3)
wp2 = sig_cu/(eps0*tau_cu)
sig("11.8d Cu sigma/(eps0 tau) [s^-2]", wp2, 2.705e32, 4)
sig("11.8d Cu N e^2/(m eps0) (tau cancels)", N_cu*e**2/(me*eps0), 2.705e32, 4)
wp = np.sqrt(wp2)
sig("11.8d omega_p [rad/s]", wp, 1.64e16, 3)
sig("11.8d Cu 4 sigma tau/eps0", 4*sig_cu*tau_cu/eps0, 6.3e5, 2)
r_cu = np.roots([1, 1/tau_cu, sig_cu/(eps0*tau_cu)])
sig("11.8d Cu Re s [1/s]", r_cu[0].real, -2.06e13, 3)
sig("11.8d Cu |Im s| [rad/s]", abs(r_cu[0].imag), 1.64e16, 3)
fp = wp/(2*np.pi)
sig("11.8d f_p [Hz]", fp, 2.6e15, 2)
sig("11.8d 2 tau [s]", 2*tau_cu, 4.8e-14, 2)
sig("11.8d oscillations per time constant f_p*2tau", fp*2*tau_cu, 127, 3)
sig("11.8d omega_p tau", wp*tau_cu, 398, 3)
# brute force: Drude MOL for copper over one time constant 2 tau
te = np.linspace(0, 2*tau_cu, 60001)
sc = drude_run(sig_cu, eps0, tau_cu, 2*tau_cu, "DOP853", te, rtol=1e-10)
rc = sc.y[ic]
zc = np.where(np.sign(rc[:-1]) != np.sign(rc[1:]))[0]
tz = te[zc] - rc[zc]*(te[zc+1]-te[zc])/(rc[zc+1]-rc[zc])
wd_sim = np.pi/np.mean(np.diff(tz))
rdot = np.array([-ddx(sc.y[Ng:, i])[ic] for i in range(0, te.size, 50)])
amp_env = np.sqrt(rc[::50]**2 + (rdot/wd_sim)**2)
slope = np.polyfit(te[::50], np.log(amp_env), 1)[0]
sig("11.8d Cu simulated oscillation omega [rad/s]", wd_sim, 1.64e16, 3)
sig("11.8d Cu simulated envelope time constant [s]", -1/slope, 4.8e-14, 2)
ok("11.8d Cu: number of zero crossings over 2 tau ~ 2*127", abs(len(tz)/2 - fp*2*tau_cu) < 1.0, f"{len(tz)} crossings")

sig_sw = 4.0; eps_sw = 81*eps0; tau_sw = 1.5e-14
sig("11.8d sea sigma/eps [1/s]", sig_sw/eps_sw, 5.58e9, 3)
sig("11.8d sea 1/tau [1/s]", 1/tau_sw, 6.67e13, 3)
sig("11.8d sea 4 sigma tau/eps", 4*sig_sw*tau_sw/eps_sw, 3.3e-4, 2)
r_sw = np.sort(np.roots([1, 1/tau_sw, sig_sw/(eps_sw*tau_sw)]).real)
sig("11.8d sea s1 [1/s]", r_sw[0], -6.67e13, 3)
sig("11.8d sea s2 [1/s]", r_sw[1], -5.58e9, 3)
ss = drude_run(sig_sw, eps_sw, tau_sw, 1.2e-9, "Radau")
t1, t2 = 3e-10, 1.1e-9
rate_sw = np.log(ss.sol(t1)[ic]/ss.sol(t2)[ic])/(t2 - t1)
sig("11.8d sea slow time constant (MOL sim) [s]", 1/rate_sw, 1.79e-10, 3)
sig("11.8d sea slow time constant (roots) [s]", -1/r_sw[1], 1.79e-10, 3)
sig("11.8d sea eps/sigma [ns]", eps_sw/sig_sw*1e9, 0.18, 2)
sig("11.8d sea tau_r = eps/sigma [s]", eps_sw/sig_sw, 1.79e-10, 3)
sig("11.8d sea relative difference (sim)", (eps_sw/sig_sw - 1/rate_sw)/(eps_sw/sig_sw), 8.4e-5, 2)
sig("11.8d sea 4 tau [s]", 4*tau_sw, 6e-14, 1)
sig("11.8d Si 4 tau [s]", 4*tau_si, 7.2e-13, 2)
ssi = drude_run(sig_si, eps_si, tau_si, 3.5e-10, "Radau")
t1, t2 = 1e-10, 3.4e-10
rate_si = np.log(ssi.sol(t1)[ic]/ssi.sol(t2)[ic])/(t2 - t1)
r_si = np.sort(np.roots([1, 1/tau_si, sig_si/(eps_si*tau_si)]).real)
sig("11.8d Si slow time constant (MOL sim) [s]", 1/rate_si, 5.29e-11, 3)
sig("11.8d Si slow time constant (roots) [s]", -1/r_si[1], 5.29e-11, 3)
sig("11.8d Si percent below tau_r", 100*(1 - (1/rate_si)/taur_si), 0.34, 2)
sig("11.8d Cu 4 tau [s]", 4*tau_cu, 9.69e-14, 3)
ok("11.8d underdamped iff tau_r < 4 tau (Cu yes, sea no, Si no)",
   (taur_cu < 4*tau_cu) and not (eps_sw/sig_sw < 4*tau_sw) and not (taur_si < 4*tau_si)
   and np.iscomplex(r_cu[0]) and np.isreal(np.roots([1, 1/tau_sw, sig_sw/(eps_sw*tau_sw)])).all())

# =====================================================================
print("== 12.10 Two crossing line currents ==")
def B_wire_bs(r, u, I):
    """numerical Biot-Savart for an infinite wire through the origin along u (current along u)"""
    r = np.asarray(r, float); u = np.asarray(u, float); s0 = r @ u
    out = np.zeros(3)
    for k in range(3):
        f = lambda s: (mu0*I/(4*np.pi)*np.cross(u, r - s*u)/np.linalg.norm(r - s*u)**3)[k]
        out[k] = quad(f, -np.inf, s0, limit=400, epsabs=1e-17)[0] + quad(f, s0, np.inf, limit=400, epsabs=1e-17)[0]
    return out
wires = [(zh, 3.0), (-xh, 1.0)]
P = np.array([2.0, 0.0, 1.0])
B1 = B_wire_bs(P, *wires[0]); B2 = B_wire_bs(P, *wires[1]); BP = B1 + B2
vec("12.10a B from z wire at P [T]", B1, [0, 3e-7, 0], 1e-12)
vec("12.10a B from x wire at P [T]", B2, [0, 2e-7, 0], 1e-12)
vec("12.10a total B at P [T]", BP, [0, 5e-7, 0], 1e-12)
sig("12.10a 5 mu0/(4 pi)", 5*mu0/(4*np.pi), 5e-7, 3)
def B_page(r):
    x, y, z = r
    return 3*mu0/(2*np.pi)*np.array([-y, x, 0])/(x**2 + y**2) + mu0/(2*np.pi)*np.array([0, z, -y])/(y**2 + z**2)
rng = np.random.default_rng(1)
dev = 0
for _ in range(6):
    r = rng.uniform(-3, 3, 3)
    Bn = B_wire_bs(r, *wires[0]) + B_wire_bs(r, *wires[1])
    dev = max(dev, np.linalg.norm(Bn - B_page(r))/np.linalg.norm(Bn))
ok("12.10b page formula = numerical Biot-Savart at 6 random points", dev < 1e-6, f"max rel dev {dev:.1e}")
def B_cf(r):  # generic infinite-wire field built with np.cross (not the page formula)
    out = np.zeros(3)
    for u, I in wires:
        rp = r - (r @ u)*u; out += mu0*I/(2*np.pi)*np.cross(u, rp)/(rp @ rp)
    return out
def resid(r):
    s = sum(mu0*I/(2*np.pi)/np.linalg.norm(r - (r @ u)*u) for u, I in wires)
    return B_cf(r)/s
nulls = []
for _ in range(300):
    r0 = rng.uniform(-4, 4, 3)
    sol = least_squares(resid, r0, bounds=([-6]*3, [6]*3), xtol=1e-14, ftol=1e-14, gtol=1e-14)
    if np.linalg.norm(resid(sol.x)) < 1e-9:
        nulls.append(sol.x)
nulls = np.array(nulls)
ok("12.10c least-squares nulls found from random starts", len(nulls) > 20, f"{len(nulls)} converged")
ok("12.10c every null has y = 0 and z = -x/3", np.allclose(nulls[:, 1], 0, atol=1e-7) and np.allclose(nulls[:, 2], -nulls[:, 0]/3, atol=1e-7),
   f"max |y| {np.max(abs(nulls[:, 1])):.1e}, max |z+x/3| {np.max(abs(nulls[:, 2] + nulls[:, 0]/3)):.1e}")
By = lambda x, z: (B_wire_bs([x, 0, z], *wires[0]) + B_wire_bs([x, 0, z], *wires[1]))[1]
sig("12.10c null at x=3 (Biot-Savart, brentq): z", brentq(lambda z: By(3, z), -2, -0.5, xtol=1e-12), -1, 4)
sig("12.10c null at x=-3: z", brentq(lambda z: By(-3, z), 0.5, 2, xtol=1e-12), 1, 4)
sig("12.10 check null on x=2: z", brentq(lambda z: By(2, z), -2, -0.3, xtol=1e-12), -2/3, 4)
Bn = B_wire_bs([3, 0, -1], *wires[0]) + B_wire_bs([3, 0, -1], *wires[1])
ok("12.10c |B(3,0,-1)| ~ 0 by Biot-Savart", np.linalg.norm(Bn) < 1e-13, f"{np.linalg.norm(Bn):.1e} T")
ok("12.10 check at P the two fields are parallel (add)", B1 @ B2 > 0)
v = 1e5*xh
F = e*np.cross(v, BP)
Ebal = -np.cross(v, BP)
vec("12.10d F on proton [N]", F/1e-21, [0, 0, 8.01], 0.005)
vec("12.10d balancing E [V/m]", Ebal, [0, 0, -0.05], 1e-6)
ok("12.10d E/B = v and E perpendicular to v, B", np.isclose(np.linalg.norm(Ebal)/np.linalg.norm(BP), 1e5) and abs(Ebal @ v) < 1e-12 and abs(Ebal @ BP) < 1e-20)

# =====================================================================
print("== 13.9 Two opposite slabs and a sheet ==")
slabs = [(-3.0, -1.0, 3.0), (0.0, 4.0, -1.5)]
def H_num(z, sheet, n=20000):
    H = np.zeros(3)
    for a, b, J in slabs:
        zp = a + (np.arange(n) + 0.5)*(b - a)/n
        H += 0.5*J*(b - a)/n*np.sum(np.sign(z - zp))*np.cross(yh, zh)
    if sheet:
        H += 0.5*np.cross(-3.0*yh, np.sign(z - 1.0)*zh)
    return H
def Ha(z):
    return np.piecewise(z, [z < -3, (z > -3) & (z < -1), (z > -1) & (z < 0), (z > 0) & (z < 4), z > 4],
                        [0, lambda z: 3*z + 9, 6, lambda z: 6 - 1.5*z, 0])
def Hb(z):
    return np.piecewise(z, [z < -3, (z > -3) & (z < -1), (z > -1) & (z < 0), (z > 0) & (z < 1), (z > 1) & (z < 4), z > 4],
                        [1.5, lambda z: 3*z + 10.5, 7.5, lambda z: 7.5 - 1.5*z, lambda z: 4.5 - 1.5*z, -1.5])
zt = np.array([-4.3, -2.71, -1.37, -0.43, 0.371, 0.83, 1.62, 2.93, 3.77, 5.2])
Hn_a = np.array([H_num(z, False) for z in zt]); Hn_b = np.array([H_num(z, True) for z in zt])
ok("13.9a H = H_x xhat only", np.allclose(Hn_a[:, 1:], 0) and np.allclose(Hn_b[:, 1:], 0))
ok("13.9a page piecewise H_x = thin-sheet sum", np.allclose(Hn_a[:, 0], Ha(zt), atol=1e-3), f"max dev {np.max(abs(Hn_a[:, 0]-Ha(zt))):.1e}")
ok("13.9b page piecewise H_x = thin-sheet sum", np.allclose(Hn_b[:, 0], Hb(zt), atol=1e-3), f"max dev {np.max(abs(Hn_b[:, 0]-Hb(zt))):.1e}")
Hab = H_num(1 + 1e-7, True); Hbe = H_num(1 - 1e-7, True)
sig("13.9b H_x just below z=1", Hbe[0], 6, 3); sig("13.9b H_x just above z=1", Hab[0], 3, 3)
vec("13.9b zhat x (H1 - H2) at z=1 [A/m]", np.cross(zh, Hab - Hbe), [0, -3, 0], 1e-3)
for zf, val in [(-3, 1.5), (-1, 7.5), (0, 7.5), (4, -1.5)]:
    lo, hi = H_num(zf - 1e-7, True)[0], H_num(zf + 1e-7, True)[0]
    ok(f"13.9b continuity at z={zf}: {val}", abs(lo - val) < 1e-3 and abs(hi - val) < 1e-3, f"{lo:.4f}/{hi:.4f}")
zz = np.linspace(-6, 7, 2601) + 0.0013    # offset: no grid point on a root
Ha_n = np.array([H_num(z, False, 2000)[0] for z in zz])
zero_a = zz[abs(Ha_n) < 1e-9]
ok("13.9c no sheet: H = 0 exactly for z<-3 and z>4, nowhere in (-3,4)",
   np.all((zero_a <= -3 + 1e-9) | (zero_a >= 4 - 1e-9)) and np.all(abs(Ha_n[(zz < -3) | (zz > 4)]) < 1e-9),
   f"min |H| on (-2.99,3.99): {np.min(abs(Ha_n[(zz > -2.99) & (zz < 3.99)])):.3f}")
Hb_n = np.array([H_num(z, True, 2000)[0] for z in zz])
sc_idx = np.where(Hb_n[:-1]*Hb_n[1:] < 0)[0]
roots = [brentq(lambda z: H_num(z, True)[0], zz[i], zz[i+1]) for i in sc_idx if abs(zz[i] - 1) > 0.01]
ok("13.9c with sheet: single zero", len(roots) == 1 and np.min(abs(Hb_n)) > 0, f"roots {np.round(roots, 6)}")
sig("13.9c zero of H with sheet [m]", roots[0], 3, 4)
ok("13.9c with sheet: outside values +1.5 (z<-3), -1.5 (z>4)", np.isclose(H_num(-5, True)[0], 1.5) and np.isclose(H_num(6, True)[0], -1.5))
sig("13.9c 3z+10.5 would vanish at", -10.5/3, -3.5, 2)
for zf, sl in [(-2.5, 3), (-1.5, 3), (2.0, -1.5), (3.5, -1.5)]:
    hfd = (H_num(zf + 0.01, True)[0] - H_num(zf - 0.01, True)[0])/0.02
    sig(f"13.9 check slope dH_x/dz at z={zf}", hfd, sl, 3)
Afun = lambda r: 1.5*mu0*abs(r[2] - 1.0)*yh
for zp, Bx in [(-0.6, 1.885e-6), (2.3, -1.885e-6)]:
    Bfd, Jm = curl(Afun, np.array([0.3, -0.2, zp]))
    vec(f"13.9d FD curl A at z={zp} [uT]", Bfd*1e6, [Bx*1e6, 0, 0], 0.0006)
    ok(f"13.9d FD div A at z={zp} = 0", abs(np.trace(Jm)) < 1e-12)
    vec(f"13.9d H = B/mu0 at z={zp} vs sheet field 1/2 Js x n", Bfd/mu0, 0.5*np.cross(-3*yh, np.sign(zp - 1)*zh), 1e-6)
h = 1e-4; Ay = lambda z: Afun(np.array([0, 0, z]))[1]
jump = (Ay(1 + 2*h) - Ay(1 + h))/h - (Ay(1 - h) - Ay(1 - 2*h))/h
sig("13.9d slope jump of A_y at z=1 [Wb/m^2]", jump, 3.7699e-6, 5)
vec("13.9d Js = -(jump)/mu0 yhat [A/m]", -jump/mu0*yh, [0, -3, 0], 1e-6)
sig("13.9 check net current K1+K2+Js", 3*2 + (-1.5)*4 + (-3), -3, 3)

# =====================================================================
print("== 14.10 Voltmeters around a ramping solenoid ==")
a_s = 0.2; dPsi = -2.0
def E_ind(p):
    x, y = p; r = np.hypot(x, y)
    Ephi = (-dPsi)/(2*np.pi*r) if r > a_s else (-dPsi)*r/(2*np.pi*a_s**2)
    return Ephi*np.cross(zh, [x/r, y/r, 0])[:2]
def lint(pts):
    tot = 0.0
    for A, Bq in zip(pts[:-1], pts[1:]):
        A = np.array(A, float); dd = np.array(Bq, float) - A
        tot += quad(lambda s: E_ind(A + s*dd) @ dd, 0, 1, epsabs=1e-13, epsrel=1e-12, limit=200)[0]
    return tot
P1, P2, P3, P4 = (1.5, -1), (1.5, 1), (-1.5, 1), (-1.5, -1)
ok("14.10 P1->P2->P3->P4 is counter-clockwise seen from +z", shoelace([P1, P2, P3, P4]) > 0)
ok("14.10 solenoid (r<0.2) inside rectangle", 0.2 < 1.0)
sides = [[P1, P2], [P2, P3], [P3, P4], [P4, P1]]; Rs = [4.0, 6.0, 10.0, 0.0]
G = [lint(s) for s in sides]
emf = sum(G)
sig("14.10a emf around P1P2P3P4 (line integral of induced E) [V]", emf, 2, 4)
I = emf/sum(Rs)
sig("14.10a I (positive = P1->P2, ccw) [A]", I, 0.1, 3)
for k, (Rk, page) in enumerate(zip(Rs[:3], [0.4, 0.6, 1.0])):
    sig(f"14.10a drop across R{k+1} [V]", I*Rk, page, 3)
V = {0: 0.0}
for k in range(3):
    V[k+1] = V[k] + G[k] - I*Rs[k]
ok("14.10 node potentials close around the loop", abs(V[3] + G[3] - I*Rs[3] - V[0]) < 1e-10)
Vn = {"P1": V[0], "P2": V[1], "P3": V[2], "P4": V[3]}
# Lenz: field at the centre from the ccw current (numerical Biot-Savart of the 4 sides)
def B_seg(r, A, Bq, Icur, n=4000):
    A = np.array([*A, 0.0]); Bq = np.array([*Bq, 0.0]); s = (np.arange(n) + 0.5)/n
    src = A + np.outer(s, Bq - A); dl = (Bq - A)/n; Rv = r - src
    return mu0*Icur/(4*np.pi)*np.sum(np.cross(dl, Rv)/np.linalg.norm(Rv, axis=1)[:, None]**3, axis=0)
Bc = sum(B_seg(np.zeros(3), *s, I) for s in sides)
ok("14.10a Lenz: ccw current makes +z field at the centre (props up falling +z flux)", Bc[2] > 0, f"Bz = {Bc[2]:.2e} T")
for r in (0.5, 1.0):
    Ev = E_ind((r, 0.0))
    sig(f"14.10b E_phi at r={r} [V/m]", Ev[1], {0.5: 0.637, 1.0: 0.318}[r], 3)
    ok(f"14.10b E at r={r} is +phi (ccw seen from +z)", Ev @ np.cross(zh, xh)[:2] > 0 and abs(Ev[0]) < 1e-12)
th = np.linspace(0, 2*np.pi, 2001)
circ = [(0.5*np.cos(t), 0.5*np.sin(t)) for t in th]
sig("14.10b circulation on r=0.5 ccw = -dPsi/dt", lint(circ), 2, 4)
def reading(path, plus, minus):
    return lint(path) + Vn[plus] - Vn[minus]
m1 = [P1, (1.6, -1), (1.6, 1), P2]
m2 = [P1, (1.5, -1.1), (-1.6, -1.1), (-1.6, 1.1), (1.5, 1.1), P2]
m3a = [P4, (-1.5, -1.1), (1.5, -1.1), P1]
m3b = [P4, (-1.4, -0.9), (-1.4, 0.5), (1.4, 0.5), (1.4, -0.9), P1]
V1 = reading(m1, "P1", "P2"); V2 = reading(m2, "P1", "P2")
V3a = reading(m3a, "P4", "P1"); V3b = reading(m3b, "P4", "P1")
sig("14.10c meter 1 [V]", V1, 0.4, 3)
sig("14.10c meter 2 [V]", V2, -1.6, 3)
sig("14.10c V1 - V2 [V]", V1 - V2, 2, 3)
sig("14.10d meter 3, leads along y=-1.1 [V]", V3a, 0, 3)
sig("14.10d meter 3, leads along y=+0.5 [V]", V3b, -2, 3)
loop2 = m2 + [P1]; loop3 = m3b + [P4]
ok("14.10c meter-2 loop (leads + R1 side back) is clockwise seen from +z", shoelace(loop2[:-1]) < 0)
ok("14.10d meter-3 loop (leads at y=0.5 + wire back) is clockwise seen from +z", shoelace(loop3[:-1]) < 0)
sig("14.10 hint: emf of a CLOCKWISE loop around the solenoid = +dPsi/dt (not -dPsi/dt)", lint(loop2), dPsi, 4)
mins = min(np.hypot(*np.array(p)) for p in [(0, 0.5)])
ok("14.10d y=0.5 path stays outside the solenoid", mins > a_s)
ok("14.10c second route: 0 - IR3 - IR2 = -1.6", np.isclose(0 - I*10 - I*6, -1.6))

# =====================================================================
print("== 15.3 Fields from given potentials ==")
Phi = lambda r, t: 2*r[1]**2
Avec = lambda r, t: np.array([0.0, -4*r[1]*t, 5*r[0]])
def gradf(f, r, hh=1e-5):
    return np.array([(f(r + hh*u) - f(r - hh*u))/(2*hh) for u in np.eye(3)])
def fields(r, t, hh=1e-5):
    gP = gradf(lambda q: Phi(q, t), r)
    dAdt = (Avec(r, t + hh) - Avec(r, t - hh))/(2*hh)
    Bc, Jm = curl(lambda q: Avec(q, t), r)
    return -gP - dAdt, Bc, gP, dAdt, Jm
opts = {"a": (lambda y: np.zeros(3), -5*yh), "b": (lambda y: -4*y*yh, -5*yh),
        "c": (lambda y: np.zeros(3), 5*yh), "d": (lambda y: -8*y*yh, -5*yh)}
pts = [(np.array([0.3, -0.7, 1.1]), 0.8), (np.array([1.7, 2.2, -0.4]), 2.5), (np.array([-1.2, 0.9, 0.0]), 0.1)]
match = set("abcd")
for r, t in pts:
    E, B, gP, dAdt, Jm = fields(r, t)
    match &= {k for k, (Ef, Bf) in opts.items() if np.allclose(E, Ef(r[1]), atol=1e-6) and np.allclose(B, Bf, atol=1e-6)}
    ok(f"15.3 (b) = -grad Phi only at {r}", np.allclose(-gP, opts['b'][0](r[1]), atol=1e-6))
    ok(f"15.3 (c) = reversed y-curl order at {r}", np.isclose(Jm[2, 0] - Jm[0, 2], 5, atol=1e-6))
    ok(f"15.3 (d) = -grad Phi + dA/dt at {r}", np.allclose(-gP + dAdt, opts['d'][0](r[1]), atol=1e-6))
ok("15.3 keyed answer: only option (a) matches E and B at all points", match == {"a"}, f"matches {sorted(match)}")
r, t = pts[0]
lam = lambda q, tt: -2*q[1]**2*tt
ok("15.3 grad(lambda) = -4yt yhat", np.allclose(gradf(lambda q: lam(q, t), r), [0, -4*r[1]*t, 0], atol=1e-6))
ok("15.3 -d(lambda)/dt = 2y^2 = Phi", np.isclose(-(lam(r, t + 1e-5) - lam(r, t - 1e-5))/2e-5, Phi(r, t)))
Bdt = (fields(r, t + 1e-4)[1] - fields(r, t - 1e-4)[1])/2e-4
cE, _ = curl(lambda q: fields(q, t)[0], r, 1e-3)
ok("15.3 Faraday: curl E = 0 = -dB/dt", np.allclose(cE, 0, atol=1e-5) and np.allclose(Bdt, 0, atol=1e-6))

# =====================================================================
print("== 15.10 Shorted parallel-plate line ==")
W = 0.05; d = 2e-3; ell = 1.0; I = 10.0; mu = 3*mu0; eps = 3*eps0
Js = I/W
sig("15.10a Js [A/m]", Js, 200, 3)
Jtop, Jbot = Js*xh, -Js*xh
def H_ideal(y):
    return 0.5*np.cross(Jtop, np.sign(y - d)*yh) + 0.5*np.cross(Jbot, np.sign(y - 0.0)*yh)
vec("15.10a H between [A/m]", H_ideal(d/2), [0, 0, -200], 1e-9)
vec("15.10a H above [A/m]", H_ideal(3*d), [0, 0, 0], 1e-9)
vec("15.10a H below [A/m]", H_ideal(-d), [0, 0, 0], 1e-9)
def H_strips(y, z, n=40000):
    zp = (np.arange(n) + 0.5)*W/n; dI = Js*W/n; H = np.zeros(3)
    for ys, u in [(d, xh), (0.0, -xh)]:
        rv = np.stack([np.zeros(n), np.full(n, y - ys), z - zp], axis=1)
        H += dI/(2*np.pi)*np.sum(np.cross(u, rv)/np.sum(rv**2, axis=1)[:, None], axis=0)
    return H
Hc = H_strips(d/2, W/2)
ok("15.10a finite-width strips (Biot-Savart): centre field along -z, within 3% of ideal", Hc[2] < 0 and abs(Hc[2]/-200 - 1) < 0.03,
   f"H = {np.array2string(Hc, precision=2)} A/m")
Bf = mu*H_ideal(d/2)
vec("15.10a B in film [1e-4 T]", Bf/1e-4, [0, 0, -7.54], 0.005)
vec("15.10a yhat x (H1 - H2) at top strip [A/m]", np.cross(yh, H_ideal(d + 1e-9) - H_ideal(d - 1e-9)), [200, 0, 0], 1e-9)
path = [(0, d), (ell, d), (ell, 0), (0, 0)]
ok("15.10b current path is clockwise seen from +z -> dS = -z", shoelace(path) < 0)
nx, ny = 200, 50
Psi = np.sum(np.full((nx, ny), Bf @ (-zh))*(ell/nx)*(d/ny))
sig("15.10b Psi [Wb]", Psi, 1.51e-6, 3)
L = Psi/I
sig("15.10b L [nH]", L*1e9, 151, 3)
sig("15.10b script-L [nH/m]", L/ell*1e9, 151, 3)
sig("15.10c L used in 1/2 L I^2 [nH]", L*1e9, 150.8, 4)
Wm = np.sum(np.full((20, 20, 20), 0.5*mu*(H_ideal(d/2) @ H_ideal(d/2)))*(W*d*ell/8000))
sig("15.10c Wm = int 1/2 mu H^2 [uJ]", Wm*1e6, 7.54, 3)
sig("15.10c 1/2 L I^2 [uJ]", 0.5*L*I**2*1e6, 7.54, 3)
C = eps*W/d
sig("15.10c script-C [pF/m]", C*1e12, 664, 3)
sig("15.10c LC/(mu0 eps0)", (L/ell)*C/(mu0*eps0), 9, 4)
sig("15.10c 1/sqrt(LC) [m/s]", 1/np.sqrt((L/ell)*C), 9.99e7, 3)
sig("15.10c c/3 [m/s]", c0/3, 9.99e7, 3)
def quants(dd, WW, II):
    Bm = mu*II/WW; Ps = Bm*dd*ell; return Bm, Ps, Ps/II, eps*WW/dd
q0 = quants(d, W, I); q1 = quants(d/2, 2*W, 3*I)
for name, k, page in [("|B|", 0, 1.5), ("Psi", 1, 0.75), ("L", 2, 0.25), ("script-C", 3, 4)]:
    sig(f"15.10d factor {name}", q1[k]/q0[k], page, 3)
sig("15.10d factor LC", (q1[2]*q1[3])/(q0[2]*q0[3]), 1, 3)

print(f"\nTOTAL FAIL = {NF[0]}")
