#!/usr/bin/env python3
"""L24 practice checks: group velocity and wave polarization (numpy only).

Every number, sign, direction and handedness on practice/24-group-velocity-and-polarization.md
is printed here. Handedness is never read off a formula: the real field E(r0, t) is sampled over
one period at a fixed point, consecutive vectors are crossed (np.cross), and the sign of
u . (E(t) x E(t+dt)) decides (positive = right-handed: right thumb along u, fingers with the
rotation; the Lecture 24 page's convention). Linear = all cross products ~ 0; circular =
|E| constant. Travel direction is checked by E(r0 + d u, t + d/v) = E(r0, t). H phasors are
checked against Faraday's law by finite-difference curls; <S> by quadrature of E(t) x H(t)
over a period; group velocities by finite differences of omega(beta).
Course constants (c = 3e8, eta0 = 120 pi) where the page uses them; exact ones for 24.11(a).
"""
import numpy as np

eps0 = 8.8541878128e-12
mu0 = 4e-7 * np.pi
e = 1.602176634e-19
me = 9.1093837e-31
cC = 3e8
eta0 = 120 * np.pi
X, Y, Z = np.eye(3)
ALL = []


def hdr(s):
    print("\n" + "=" * 78 + "\n" + s + "\n" + "=" * 78)


def check(label, cond):
    print(f"  [{label}] {'OK' if cond else 'FAIL'}")
    ALL.append(bool(cond))


def close(label, a, b, rtol=1e-6, atol=1e-12):
    ok = np.allclose(a, b, rtol=rtol, atol=atol)
    print(f"  [{label}] {np.round(a, 10)!r} vs {np.round(b, 10)!r} -> {'OK' if ok else 'FAIL'}")
    ALL.append(bool(ok))


def phasor_field(E0, kvec, w):
    """Real field E(r,t) = Re{E0 exp(-j k.r) exp(j w t)}; kvec = beta * u."""
    E0 = np.asarray(E0, dtype=complex)
    kvec = np.asarray(kvec, float)
    return lambda r, t: np.real(E0 * np.exp(-1j * kvec @ np.asarray(r, float)) * np.exp(1j * w * t))


def classify(Efun, u, r0, T, n=4001):
    """Rotate the real field numerically at r0 over one period."""
    ts = np.linspace(0, T, n)
    E = np.array([Efun(r0, t) for t in ts])
    mags = np.linalg.norm(E, axis=1)
    cr = np.cross(E[:-1], E[1:]) @ np.asarray(u, float)
    scale = mags.max() ** 2
    if np.max(np.abs(cr)) < 1e-9 * scale:
        kind = "linear"
    else:
        kind = "circular" if mags.min() > (1 - 1e-6) * mags.max() else "elliptical"
    if kind == "linear":
        hand = "-"
    else:
        s = np.sign(cr.sum())
        assert np.all(np.sign(cr[np.abs(cr) > 1e-9 * scale]) == s), "rotation reverses?"
        hand = "right" if s > 0 else "left"
    return kind, hand, mags.max(), mags.min()


def travels(Efun, u, v, T, r0=(0.1, 0.2, 0.3)):
    """True if E(r0 + d u, t + d/v) == E(r0, t) for several d, t."""
    u = np.asarray(u, float)
    ok = True
    for d in (0.13, 0.71, 1.9):
        for t in np.linspace(0, T, 7):
            ok &= np.allclose(Efun(np.asarray(r0) + d * u, t + d / v), Efun(r0, t), atol=1e-9)
    return ok


def curl_phasor(F, r, h=1e-6):
    """Finite-difference curl of a complex vector phasor field F(r)."""
    r = np.asarray(r, float)
    J = np.zeros((3, 3), complex)  # J[i, k] = dF_i / dx_k
    for k in range(3):
        dr = np.zeros(3); dr[k] = h
        J[:, k] = (F(r + dr) - F(r - dr)) / (2 * h)
    return np.array([J[2, 1] - J[1, 2], J[0, 2] - J[2, 0], J[1, 0] - J[0, 1]])


def avgS(Efun, Hfun, r0, T, n=20000):
    ts = np.linspace(0, T, n, endpoint=False)
    return np.mean([np.cross(Efun(r0, t), Hfun(r0, t)) for t in ts], axis=0)


def report_pol(name, Efun, u, v, T, r0=(0, 0, 0)):
    k, h, mx, mn = classify(Efun, u, r0, T)
    tr = travels(Efun, u, v, T)
    print(f"  {name}: travel u = {np.round(u, 3)} (check {tr}); {k}, {h}-handed; |E| max {mx:.6g}, min {mn:.6g}")
    return k, h, tr


# =============================================================================
hdr("24.1 Crests and envelope in a plasma (f_p = 4 GHz, f = 5 GHz, 0.9 m column)")
fp, f = 4e9, 5e9
wp, w = 2 * np.pi * fp, 2 * np.pi * f
beta = np.sqrt(w**2 - wp**2) / cC
vp = w / beta
wofb = lambda b: np.sqrt(wp**2 + cC**2 * b**2)
vg_fd = (wofb(beta + 1e-3) - wofb(beta - 1e-3)) / 2e-3
vg = cC * np.sqrt(1 - (fp / f) ** 2)
print(f"  sqrt(1 - fp^2/f^2) = {np.sqrt(1-(fp/f)**2):.6f}")
print(f"  vp = {vp:.6g} m/s = {vp/cC:.6f} c ; vg (formula) = {vg:.6g} = {vg/cC:.4f} c ; vg (FD of omega(beta)) = {vg_fd:.6g}")
close("24.1 vg FD = c sqrt(1-fp^2/f^2)", vg_fd, vg)
close("24.1 vp = 5e8", vp, 5e8)
close("24.1 vg = 1.8e8", vg, 1.8e8)
close("24.1 vp vg = c^2 = 9e16", vp * vg, 9e16)
L = 0.9
print(f"  envelope delay {L/vg*1e9:.6g} ns ; vacuum {L/cC*1e9:.6g} ns ; crest transit {L/vp*1e9:.6g} ns")
close("24.1 envelope delay 5 ns", L / vg, 5e-9)
close("24.1 vacuum 3 ns", L / cC, 3e-9)
close("24.1 crest 1.8 ns", L / vp, 1.8e-9)
print(f"  beta = {beta:.6g} rad/m, lambda in plasma = {2*np.pi/beta:.6g} m (vacuum {cC/f:.6g} m)")

# =============================================================================
hdr("24.2 Which velocity carries the message (MC)")
# (a) dielectric eps_r = 4: beta = w sqrt(mu eps) -> vp = vg = c/2
er = 4
bD = lambda ww: ww * np.sqrt(er) / cC
ww = 2 * np.pi * 1e8
vgD = 1 / ((bD(ww * 1.001) - bD(ww * 0.999)) / (0.002 * ww))
print(f"  (a) eps_r=4: vp = {ww/bD(ww):.6g}, vg = {vgD:.6g} (both c/2 = {cC/2:.6g}); 'c/4' is false")
close("24.2a vg = vp = c/2", [ww / bD(ww), vgD], [cC / 2, cC / 2])
# (b) affine beta = b0 + w/u: straight line, yet vp depends on w and vp != vg
b0, uu = 2.0, 2e8
for wtest in (2 * np.pi * 1e7, 2 * np.pi * 1e8):
    print(f"  (b) beta = {b0} + w/{uu:.0e}: at w = {wtest:.4g}: vp = {wtest/(b0+wtest/uu):.6g}, vg = {uu:.6g}")
check("24.2b affine beta is dispersive (vp varies)", abs(2*np.pi*1e7/(b0+2*np.pi*1e7/uu) - 2*np.pi*1e8/(b0+2*np.pi*1e8/uu)) > 1e6)
# (c) plasma vp vg = c^2 for several w: true -> if one < c the other > c
for r in (1.1, 1.5, 3.0, 10.0):
    wq = r * wp
    bq = np.sqrt(wq**2 - wp**2) / cC
    vpq = wq / bq
    vgq = (wofb(bq + 1e-4) - wofb(bq - 1e-4)) / 2e-4
    print(f"  (c) w = {r} wp: vp = {vpq/cC:.6f} c, vg = {vgq/cC:.6f} c, vp vg / c^2 = {vpq*vgq/cC**2:.9f}")
    check(f"24.2c vp vg = c^2 at w = {r} wp; vg < c < vp", np.isclose(vpq * vgq, cC**2) and vgq < cC < vpq)
# (d) message time across 90 km at 10 MHz with fp = 6 MHz vs vacuum
print(f"  (d) e.g. fp = 6 MHz, f = 10 MHz: vg = {cC*0.8:.4g} < c -> message slower than in vacuum")
# (e) d beta/d omega = 1/vg (units s/m)
print(f"  (e) dbeta/domega at 24.1's carrier = {1/vg:.6g} s/m = 1/vg (not a speed)")

# =============================================================================
hdr("24.3 Name four polarizations")
w = 2 * np.pi
T = 1.0
b = 1.0      # beta; v = w / b
v = w / b
fa = lambda r, t: 2 * np.sin(w * t - b * r[2]) * X + 2 * np.cos(w * t - b * r[2]) * Y
fb = lambda r, t: 3 * np.cos(w * t + b * r[0]) * Y - 3 * np.sin(w * t + b * r[0]) * Z
fc = lambda r, t: 2 * np.sin(w * t - b * r[1]) * Z - 2 * np.sin(w * t - b * r[1]) * X
fd = lambda r, t: 4 * np.cos(w * t - b * r[2]) * X + 4 * np.cos(w * t - b * r[2] - np.pi / 3) * Y
res3 = {}
res3["a"] = report_pol("(a) 2 sin(wt-bz) x + 2 cos(wt-bz) y", fa, Z, v, T)
res3["b"] = report_pol("(b) 3 cos(wt+bx) y - 3 sin(wt+bx) z", fb, -X, v, T)
res3["c"] = report_pol("(c) 2 sin(wt-by) z - 2 sin(wt-by) x", fc, Y, v, T)
res3["d"] = report_pol("(d) 4 cos(wt-bz) x + 4 cos(wt-bz-pi/3) y", fd, Z, v, T)
check("24.3a left circular", res3["a"][:2] == ("circular", "left") and res3["a"][2])
check("24.3b right circular", res3["b"][:2] == ("circular", "right") and res3["b"][2])
check("24.3c linear", res3["c"][0] == "linear" and res3["c"][2])
check("24.3d right elliptical", res3["d"][:2] == ("elliptical", "right") and res3["d"][2])
print("  (a) at z=0: E(0) =", fa((0, 0, 0), 0), " E(T/4) =", np.round(fa((0, 0, 0), 0.25), 12))
print("  (b) at x=0: E(0) =", fb((0, 0, 0), 0), " E(T/4) =", np.round(fb((0, 0, 0), 0.25), 12))
print("  (c) direction of the line: (z - x)/sqrt2; E(T/4) =", np.round(fc((0, 0, 0), 0.25), 12))
print("  (d) E(0) =", np.round(fd((0, 0, 0), 0), 6), " E(T/4) =", np.round(fd((0, 0, 0), 0.25), 6))
# phasors
Pa = -2j * X + 2 * Y            # 2 sin -> -2j ; 2 cos -> 2
print("  (a) phasor:", Pa, "= -2j (x + j y) e^{-j b z}:", np.allclose(Pa, -2j * (X + 1j * Y)))
check("24.3a phasor -2j(x + jy)", np.allclose(Pa, -2j * (X + 1j * Y)))
Pd = 4 * X + 4 * np.exp(-1j * np.pi / 3) * Y
print("  (d) phasor: 4x + 4 e^{-j pi/3} y, phi = -60 deg, sin(phi) =", np.sin(-np.pi / 3))
# (d) ellipse axes
_, _, mx, mn = classify(fd, Z, (0, 0, 0), T)
print(f"  (d) semi-axes: max |E| = {mx:.6f} (= 4 sqrt(3/2) = {4*np.sqrt(1.5):.6f}), min = {mn:.6f} (= 4 sqrt(1/2) = {4*np.sqrt(.5):.6f})")

# =============================================================================
hdr("24.4 True or false on one wave: E = (6 y + B e^{j phi} z) e^{+j beta x}")
u = -X
res4 = {}
for (phi, B) in [(np.pi, 0.0), (np.pi, 3.0), (np.pi, 6.0), (np.pi, 10.0), (0.7, 0.0), (2.0, 0.0),
                 (np.pi / 2, 6.0), (3 * np.pi / 2, 6.0), (np.pi / 2, 3.0), (3 * np.pi / 2, 3.0),
                 (0.0, 6.0), (np.pi / 4, 6.0)]:
    E0 = 6 * Y + B * np.exp(1j * phi) * Z
    fun = phasor_field(E0, b * u, w)
    k, h, mx, mn = classify(fun, u, (0, 0, 0), T)
    tr = travels(fun, u, v, T)
    res4[(round(phi, 4), B)] = (k, h)
    print(f"  phi = {phi:.4f} ({np.degrees(phi):.0f} deg), B = {B}: {k}, {h}; travels -x: {tr}")
check("24.4(i) phi=pi linear for B = 0,3,6,10", all(res4[(round(np.pi, 4), B)][0] == "linear" for B in (0.0, 3.0, 6.0, 10.0)))
check("24.4(ii) B=0 linear for any phi", all(res4[(round(p, 4), 0.0)][0] == "linear" for p in (np.pi, 0.7, 2.0)))
check("24.4(iii) (pi/2, 6) right circular -> TRUE", res4[(round(np.pi / 2, 4), 6.0)] == ("circular", "right"))
check("24.4(iv) (3pi/2, 6) left circular -> 'right' FALSE", res4[(round(3 * np.pi / 2, 4), 6.0)] == ("circular", "left"))
check("24.4(v) (pi/2, 3) right elliptical -> 'left elliptical' FALSE", res4[(round(np.pi / 2, 4), 3.0)] == ("elliptical", "right"))
check("24.4(vi) B=6 not circular for phi = 0 (linear) and pi/4 (elliptical)",
      res4[(0.0, 6.0)][0] == "linear" and res4[(round(np.pi / 4, 4), 6.0)][0] == "elliptical")
# the statement-(iii) recipe numbers
E0 = 6 * Y + 6j * Z
print("  (iii) E(0) = Re =", np.real(E0), " E(T/4) = -Im =", -np.imag(E0),
      " E(0) x E(T/4) =", np.cross(np.real(E0), -np.imag(E0)), " u.(..) =", u @ np.cross(np.real(E0), -np.imag(E0)))

# =============================================================================
hdr("24.5 Find the error: E = 5 (x + j y) e^{+j beta z} in free space")
E0 = 5 * (X + 1j * Y)
u = -Z
fun = phasor_field(E0, b * u, w)
k, h, _ = report_pol("Ehat", fun, u, v, T)
check("24.5 right circular (travel -z)", (k, h) == ("circular", "right"))
H_true = np.cross(u, E0) / eta0
H_stud = np.cross(Z, E0) / eta0
print("  correct H*eta0 =", H_true * eta0, "(= 5(j x - y))")
print("  student H*eta0 =", H_stud * eta0, "(= 5(y - j x) = -correct)")
close("24.5 H = 5(jx - y)/eta0", H_true, 5 * (1j * X - Y) / eta0)
close("24.5 student H = -correct", H_stud, -H_true)
# Faraday check: curl E = -j w mu H, phasor with real beta, w; use physical numbers f=1e8
ff = 1e8; wf = 2 * np.pi * ff; bf = wf / cC
Ef = lambda r: E0 * np.exp(1j * bf * r[2])
Hf = -curl_phasor(Ef, np.array([0.1, 0.2, 0.3])) / (1j * wf * mu0)
close("24.5 Faraday: H(r)", Hf, H_true * np.exp(1j * bf * 0.3) * (eta0 / np.sqrt(mu0 / (1 / (mu0 * cC**2)))), rtol=1e-5)
S = 0.5 * np.real(np.cross(E0, np.conj(H_true)))
print(f"  <S> = {S} W/m^2 = 25/eta0 = {25/eta0:.6g} along -z")
close("24.5 <S> = -25/eta0 z", S, -25 / eta0 * Z)
Ss = 0.5 * np.real(np.cross(E0, np.conj(H_stud)))
print("  student's <S> =", Ss, "(points +z: contradicts e^{+j beta z})")

# =============================================================================
hdr("24.6 From two snapshots to a phasor (travel -y, f = 50 MHz, eps_r = 4)")
f6 = 50e6; er6 = 4
v6 = cC / np.sqrt(er6); eta6 = eta0 / np.sqrt(er6)
b6 = 2 * np.pi * f6 / v6
print(f"  v = {v6:.6g} m/s, T = {1/f6*1e9:.6g} ns, lambda = {v6/f6:.6g} m, beta = {b6:.6g} rad/m = {b6/np.pi:.6g} pi, eta = {eta6:.6g} = {eta6/np.pi:.6g} pi")
close("24.6 T, lambda, beta", [1 / f6, v6 / f6, b6], [2e-8, 3.0, 2 * np.pi / 3])
E0 = 3 * (Z - 1j * X)
u = -Y
w6 = 2 * np.pi * f6
fun = phasor_field(E0, b6 * u, w6)
print("  E(origin, 0) =", fun((0, 0, 0), 0), " E(origin, T/4) =", np.round(fun((0, 0, 0), 0.25 / f6), 12))
close("24.6 snapshot t=0: 3z", fun((0, 0, 0), 0), 3 * Z)
close("24.6 snapshot T/4: 3x", fun((0, 0, 0), 0.25 / f6), 3 * X)
print("  recipe: u.(E(0) x E(T/4)) =", u @ np.cross(3 * Z, 3 * X))
k, h, _ = report_pol("Ehat = 3(z - j x) e^{j 2pi y/3}", fun, u, v6, 1 / f6)
check("24.6 left circular", (k, h) == ("circular", "left"))
H6 = np.cross(u, E0) / eta6
print("  H*20pi =", H6 * 20 * np.pi, "(= -(x + j z))", " 1/(20 pi) =", 1 / (20 * np.pi))
close("24.6 H = -(x + jz)/(20pi)", H6, -(X + 1j * Z) / (20 * np.pi))
eps6 = er6 / (mu0 * cC**2)
Ef = lambda r: E0 * np.exp(1j * b6 * r[1])
Hf = -curl_phasor(Ef, np.array([0.1, 0.2, 0.3])) / (1j * w6 * mu0)
close("24.6 Faraday H(r)", Hf, H6 * np.exp(1j * b6 * 0.2) * (eta6 / np.sqrt(mu0 / eps6)), rtol=1e-5)
Etd6 = lambda r, t: 3 * np.cos(w6 * t + b6 * r[1]) * Z + 3 * np.sin(w6 * t + b6 * r[1]) * X
check("24.6 time-domain form 3cos(wt + 2pi y/3) z + 3 sin(wt + 2pi y/3) x",
      all(np.allclose(fun((0, yy, 0), t), Etd6((0, yy, 0), t)) for yy in (-0.4, 0.3) for t in np.linspace(0, 1 / f6, 7)))
fH6 = phasor_field(H6, b6 * u, w6)
print("  H(origin, 0) =", np.round(fH6((0, 0, 0), 0), 9), " H(origin, T/4) =", np.round(fH6((0, 0, 0), 0.25 / f6), 9))
check("24.6 H also left circular", classify(fH6, u, (0, 0, 0), 1 / f6)[:2] == ("circular", "left"))
S6 = 0.5 * np.real(np.cross(E0, np.conj(H6)))
print(f"  <S> = {S6} = 18/(2*60pi) = 3/(20 pi) = {3/(20*np.pi):.6g} W/m^2 along -y")
close("24.6 <S>", S6, -3 / (20 * np.pi) * Y)

# =============================================================================
hdr("24.7 Linear and circular building blocks (free space, +z)")
R = X - 1j * Y   # right for +z
Lc = X + 1j * Y  # left for +z
fR = phasor_field(R, b * Z, w); fL = phasor_field(Lc, b * Z, w)
print("  basis check: x - jy ->", classify(fR, Z, (0, 0, 0), T)[:2], "; x + jy ->", classify(fL, Z, (0, 0, 0), T)[:2])
check("24.7 x - jy right, x + jy left (+z)", classify(fR, Z, (0, 0, 0), T)[:2] == ("circular", "right")
      and classify(fL, Z, (0, 0, 0), T)[:2] == ("circular", "left"))
# (a) 4 y = a R + c L
M = np.array([[1, 1], [-1j, 1j]])
a_, c_ = np.linalg.solve(M, np.array([0, 4]))
print(f"  (a) 4y = ({a_:.6g}) (x - jy) + ({c_:.6g}) (x + jy)")
close("24.7a weights 2j, -2j", [a_, c_], [2j, -2j])
P_lin = 16 / (2 * eta0); P_R = abs(a_) ** 2 * 2 / (2 * eta0); P_L = abs(c_) ** 2 * 2 / (2 * eta0)
print(f"  (a) powers: linear 16/(2 eta0) = 8/eta0 = {P_lin:.6g} W/m^2; right part {P_R:.6g} (= 4/eta0); left part {P_L:.6g}; sum {P_R+P_L:.6g}")
close("24.7a powers add", P_R + P_L, P_lin)
print(f"      8/eta0 = {8/eta0:.6g} = 1/(15 pi) = {1/(15*np.pi):.6g}")
# each circular part at z=0, t=0
print("  (a) right part at origin, t=0: Re{2j(x - jy)} =", np.real(2j * R), "; left part:", np.real(-2j * Lc))
# (b) 3 R + 1 L
Eb = 3 * R + 1 * Lc
print("  (b) 3(x - jy) + (x + jy) =", Eb)
close("24.7b sum = 4x - 2jy", Eb, 4 * X - 2j * Y)
fb7 = phasor_field(Eb, b * Z, w)
k, h, mx, mn = classify(fb7, Z, (0, 0, 0), T)
print(f"  (b) {k}, {h}; max |E| = {mx:.6f} (a_R + a_L = 4), min |E| = {mn:.6f} (a_R - a_L = 2)")
check("24.7b right elliptical, axes 4 and 2", (k, h) == ("elliptical", "right") and np.isclose(mx, 4) and np.isclose(mn, 2))
print("  (b) E(0) =", fb7((0, 0, 0), 0), " E(T/4) =", np.round(fb7((0, 0, 0), 0.25), 12), " (major axis x, minor y)")
Pb = (16 + 4) / (2 * eta0); PbR = 9 * 2 / (2 * eta0); PbL = 1 * 2 / (2 * eta0)
print(f"  (c) <S> total = 20/(2 eta0) = 10/eta0 = {Pb:.6g} W/m^2; right 9/eta0 = {PbR:.6g}; left 1/eta0 = {PbL:.6g}; sum = {PbR+PbL:.6g}")
close("24.7c circular powers add", PbR + PbL, Pb)
Hb = np.cross(Z, Eb) / eta0
Sq = avgS(fb7, phasor_field(Hb, b * Z, w), (0, 0, 0), T)
close("24.7c quadrature <S>", Sq, Pb * Z, rtol=1e-4)
print(f"      10/eta0 = {10/eta0:.6g} = 1/(12 pi) = {1/(12*np.pi):.6g}")

# =============================================================================
hdr("24.8 Starting from H (mu_r = 4, eps_r = 1, beta = 2 pi rad/m, +x)")
mur8 = 4; v8 = cC / 2; eta8 = eta0 * 2
b8 = 2 * np.pi
f8 = b8 * v8 / (2 * np.pi)
w8 = 2 * np.pi * f8
print(f"  v = {v8:.6g}, f = {f8:.6g} Hz, lambda = {2*np.pi/b8:.6g} m, eta = {eta8:.6g} = {eta8/np.pi:.6g} pi")
close("24.8 f = 150 MHz", f8, 1.5e8)
H0 = 0.1 * (Y - 1j * Z)   # 0.1 cos y + 0.1 sin z
Ht = lambda r, t: 0.1 * np.cos(w8 * t - b8 * r[0]) * Y + 0.1 * np.sin(w8 * t - b8 * r[0]) * Z
fH = phasor_field(H0, b8 * X, w8)
check("24.8 H phasor 0.1(y - jz) reproduces the time-domain H",
      all(np.allclose(Ht((0.3, 0, 0), t), fH((0.3, 0, 0), t)) for t in np.linspace(0, 1 / f8, 9)))
E8 = eta8 * np.cross(H0, X)
print("  E = eta H x u =", E8, "= -24 pi (z + j y):", np.allclose(E8, -24 * np.pi * (Z + 1j * Y)))
close("24.8 E = -24pi(z + jy)", E8, -24 * np.pi * (Z + 1j * Y))
print(f"  24 pi = {24*np.pi:.6g} V/m")
fE = phasor_field(E8, b8 * X, w8)
Et = lambda r, t: 24 * np.pi * np.sin(w8 * t - b8 * r[0]) * Y - 24 * np.pi * np.cos(w8 * t - b8 * r[0]) * Z
check("24.8 time-domain E = 24pi sin(wt-2pi x) y - 24pi cos(wt-2pi x) z",
      all(np.allclose(Et((0.3, 0, 0), t), fE((0.3, 0, 0), t)) for t in np.linspace(0, 1 / f8, 9)))
mu8 = mur8 * mu0
Ef = lambda r: E8 * np.exp(-1j * b8 * r[0])
Hf = -curl_phasor(Ef, np.array([0.1, 0.2, 0.3])) / (1j * w8 * mu8)
eps8 = 1 / (mu0 * cC**2)
close("24.8 Faraday (mu = 4 mu0): curl E -> H", Hf, H0 * np.exp(-1j * b8 * 0.1) * (eta8 / np.sqrt(mu8 / eps8)), rtol=1e-5)
kE = report_pol("E", fE, X, v8, 1 / f8)
kH = report_pol("H", fH, X, v8, 1 / f8)
check("24.8 E and H both right circular", kE[:2] == ("circular", "right") and kH[:2] == ("circular", "right"))
print("  H(0) =", fH((0, 0, 0), 0), "H(T/4) =", np.round(fH((0, 0, 0), 0.25 / f8), 12))
print("  E(0) =", np.round(fE((0, 0, 0), 0), 9), "E(T/4) =", np.round(fE((0, 0, 0), 0.25 / f8), 9))
print("  recipe on H: x.(H(0) x H(T/4)) =", X @ np.cross(fH((0, 0, 0), 0), fH((0, 0, 0), 0.25 / f8)))
S8 = 0.5 * np.real(np.cross(E8, np.conj(H0)))
print(f"  <S> = {S8} ; 2.4 pi = {2.4*np.pi:.6g} W/m^2 ; eta |H|^2/2 = {eta8*np.vdot(H0,H0).real/2:.6g}")
close("24.8 <S> = 2.4 pi x", S8, 2.4 * np.pi * X)
Sinst = [np.cross(fE((0.2, 0, 0), t), fH((0.2, 0, 0), t)) for t in np.linspace(0, 1 / f8, 13)]
check("24.8 instantaneous S constant = 2.4 pi x", np.allclose(Sinst, 2.4 * np.pi * X))
print("  instantaneous S samples (x comp):", np.round([s_[0] for s_ in Sinst[:4]], 9))

# =============================================================================
hdr("24.9 Building a right-circular wave (free space, -z, 75 MHz, E = 6y at origin t=0)")
f9 = 75e6; w9 = 2 * np.pi * f9
lam9 = cC / f9; b9 = 2 * np.pi / lam9
print(f"  lambda = {lam9:.6g} m, beta = {b9:.6g} = {b9/np.pi:.6g} pi rad/m, T = {1/f9*1e9:.6g} ns")
close("24.9 lambda 4 m, beta pi/2", [lam9, b9], [4.0, np.pi / 2])
u = -Z
# template E = (A x + B y + C z) exp(j(ax + by + cz)) -> (a,b,c) = -beta u = (0,0,+beta)
abc = -b9 * u
print("  (a,b,c) =", abc, "(c = +pi/2 rad/m)")
close("24.9 (a,b,c)", abc, [0, 0, np.pi / 2])
# right-circular for u = -z, E(0) = 6y: E(T/4) must satisfy u.(E0 x E1) > 0 with |E1| = 6, E1 perp
for cand in (6 * X, -6 * X):
    print(f"  candidate E(T/4) = {cand}: u.(E(0) x E(T/4)) = {u @ np.cross(6*Y, cand)}")
E9 = 6 * Y - 1j * (6 * X)    # Re = 6y, -Im = 6x
print("  E phasor amplitude (A,B,C) =", E9)
close("24.9 (A,B,C) = (-6j, 6, 0)", E9, np.array([-6j, 6, 0]))
f9E = phasor_field(E9, b9 * u, w9)
k, h, _ = report_pol("E", f9E, u, cC, 1 / f9)
check("24.9 right circular", (k, h) == ("circular", "right"))
check("24.9 E(origin, 0) = 6y", np.allclose(f9E((0, 0, 0), 0), 6 * Y))
print("  -6j(x + jy) =", -6j * (X + 1j * Y), "same:", np.allclose(E9, -6j * (X + 1j * Y)))
H9 = np.cross(u, E9) / eta0
print("  H*20pi =", H9 * 20 * np.pi, "(= x + j y)")
close("24.9 H = (x + jy)/(20 pi) e^{j pi z/2}", H9, (X + 1j * Y) / (20 * np.pi))
Ef = lambda r: E9 * np.exp(1j * b9 * r[2])
Hf = -curl_phasor(Ef, np.array([0.1, 0.2, 0.3])) / (1j * w9 * mu0)
eps0C = 1 / (mu0 * cC**2)
close("24.9 Faraday", Hf, H9 * np.exp(1j * b9 * 0.3) * (eta0 / np.sqrt(mu0 / eps0C)), rtol=1e-5)
f9H = phasor_field(H9, b9 * u, w9)
print("  H(origin,0) =", np.round(f9H((0, 0, 0), 0), 9), " 1/(20pi) =", 1 / (20 * np.pi))
print("  H(origin,T/4) =", np.round(f9H((0, 0, 0), 0.25 / f9), 9))
S9 = 0.5 * np.real(np.cross(E9, np.conj(H9)))
print(f"  <S> = {S9} ; 3/(10 pi) = {3/(10*np.pi):.6g} W/m^2 ; one component 36/(2 eta0) = {36/(2*eta0):.6g} = 3/(20 pi)")
close("24.9 <S> = -(3/(10pi)) z", S9, -3 / (10 * np.pi) * Z)
close("24.9 quadrature", avgS(f9E, f9H, (0, 0, 0.7), 1 / f9), S9, rtol=1e-4)
# time domain E(z,t) = 6 sin(wt + bz) x + 6 cos(wt + bz) y
Etd = lambda r, t: 6 * np.sin(w9 * t + b9 * r[2]) * X + 6 * np.cos(w9 * t + b9 * r[2]) * Y
check("24.9 time-domain E", all(np.allclose(Etd((0, 0, zz), t), f9E((0, 0, zz), t))
                                for zz in (-1.3, 0.4) for t in np.linspace(0, 1 / f9, 7)))
print("  E(z = -1 m, t = 0) =", np.round(f9E((0, 0, -1), 0), 12), "; E(z = +1 m, t = 0) =", np.round(f9E((0, 0, 1), 0), 12))
close("24.9 E(-1 m, 0) = -6x", f9E((0, 0, -1), 0), -6 * X)
close("24.9 E(+1 m, 0) = +6x", f9E((0, 0, 1), 0), 6 * X)
print("  probe at z = -1 m sees 6y at t = (1 m)/c =", 1 / cC * 1e9, "ns = T/4 =", 0.25 / f9 * 1e9, "ns:",
      np.round(f9E((0, 0, -1), 1 / cC), 12))
close("24.9 probe at -1 m: 6y at t = 10/3 ns", f9E((0, 0, -1), 1 / cC), 6 * Y)

# =============================================================================
hdr("24.10 A wave with a free phase: E = E1 cos(wt + bx) y + E2 cos(wt + bx + phi) z, free space")
u = -X
f10 = 1.0; w10 = 2 * np.pi; b10 = 1.0; v10 = w10 / b10
def wave10(E1, E2, phi):
    return lambda r, t: E1 * np.cos(w10 * t + b10 * r[0]) * Y + E2 * np.cos(w10 * t + b10 * r[0] + phi) * Z
# phasor and H for symbolic check at random parameters
rng = np.random.default_rng(24)
okP = okH = okS = okHand = True
for _ in range(40):
    E1, E2 = rng.uniform(0.5, 5, 2); phi = rng.uniform(0, 2 * np.pi)
    P = E1 * Y + E2 * np.exp(1j * phi) * Z
    fun = phasor_field(P, b10 * u, w10)
    okP &= all(np.allclose(fun((0.3, 0, 0), t), wave10(E1, E2, phi)((0.3, 0, 0), t)) for t in np.linspace(0, 1, 5))
    Hp = np.cross(u, P) / eta0
    okH &= np.allclose(Hp, (-E1 * Z + E2 * np.exp(1j * phi) * Y) / eta0)
    S = 0.5 * np.real(np.cross(P, np.conj(Hp)))
    okS &= np.allclose(S, -(E1**2 + E2**2) / (2 * eta0) * X)
    k, h, _, _ = classify(fun, u, (0, 0, 0), 1.0, n=2001)
    if abs(np.sin(phi)) > 1e-3:
        okHand &= (h == ("right" if np.sin(phi) > 0 else "left"))
check("24.10 phasor E1 y + E2 e^{j phi} z (40 random sets)", okP)
check("24.10 H = (E2 e^{j phi} y - E1 z)/eta0", okH)
check("24.10 <S> = -(E1^2 + E2^2)/(2 eta0) x, independent of phi", okS)
check("24.10 right iff sin(phi) > 0, left iff sin(phi) < 0 (travel -x)", okHand)
for (E1, E2, phi, name) in [(3, 3, np.pi / 2, "E1=E2, pi/2"), (3, 3, 3 * np.pi / 2, "E1=E2, 3pi/2"), (3, 5, 0, "phi=0"),
                            (3, 5, np.pi, "phi=pi"), (4, 3, np.pi / 2, "4,3,pi/2"), (4, 3, np.pi / 3, "4,3,pi/3")]:
    fun = wave10(E1, E2, phi)
    k, h, mx, mn = classify(fun, u, (0, 0, 0), 1.0)
    print(f"  E1={E1}, E2={E2}, phi={np.degrees(phi):.0f} deg ({name}): {k}, {h}; |E| max {mx:.6g}, min {mn:.6g}; travels -x: {travels(fun, u, v10, 1.0)}")
check("24.10 (3,3,pi/2) right circular", classify(wave10(3, 3, np.pi / 2), u, (0, 0, 0), 1.0)[:2] == ("circular", "right"))
check("24.10 (3,3,3pi/2) left circular", classify(wave10(3, 3, 3 * np.pi / 2), u, (0, 0, 0), 1.0)[:2] == ("circular", "left"))
k, h, mx, mn = classify(wave10(4, 3, np.pi / 2), u, (0, 0, 0), 1.0)
check("24.10d (4,3,pi/2): right elliptical, axes 4 (y) and 3 (z)", (k, h) == ("elliptical", "right") and np.isclose(mx, 4) and np.isclose(mn, 3))
fd10 = wave10(4, 3, np.pi / 2)
print("  (d) E(0) =", np.round(fd10((0, 0, 0), 0), 12), " E(T/4) =", np.round(fd10((0, 0, 0), 0.25), 12))
P = 4 * Y + 3j * Z
print("  (d) phasor:", P, " recipe u.(E(0) x E(T/4)) =", u @ np.cross(np.real(P), -np.imag(P)))
Hd = np.cross(u, P) / eta0
print("  (d) H*eta0 =", Hd * eta0, "(= 3j y - 4 z)")
close("24.10d H = (3j y - 4 z)/eta0", Hd, (3j * Y - 4 * Z) / eta0)
Sd = 0.5 * np.real(np.cross(P, np.conj(Hd)))
print(f"  (d) <S> = {Sd} ; 25/(240 pi) = 5/(48 pi) = {5/(48*np.pi):.6g} W/m^2")
close("24.10d <S> = -(5/(48 pi)) x", Sd, -5 / (48 * np.pi) * X)
close("24.10d quadrature", avgS(fd10, phasor_field(Hd, b10 * u, w10), (0.2, 0, 0), 1.0), Sd, rtol=1e-4)
ff = 1e8; wf = 2 * np.pi * ff; bf = wf / cC
Ef = lambda r: P * np.exp(1j * bf * r[0])
Hf = -curl_phasor(Ef, np.array([0.1, 0.2, 0.3])) / (1j * wf * mu0)
eps0C = 1 / (mu0 * cC**2)
close("24.10d Faraday", Hf, Hd * np.exp(1j * bf * 0.1) * (eta0 / np.sqrt(mu0 / eps0C)), rtol=1e-5)
# (e) phi = pi/3 with 4,3: still right-handed elliptical
print("  (e) phi = pi/3:", classify(wave10(4, 3, np.pi / 3), u, (0, 0, 0), 1.0)[:2])
# (e) the SP17-style options: which give left circular?
for (E1, E2, phi) in [(3, 3, np.pi / 2), (3, 3, -np.pi / 2), (3, 3, 0)]:
    print(f"   E1=E2=3, phi = {np.degrees(phi):.0f} deg ->", classify(wave10(E1, E2, phi), u, (0, 0, 0), 1.0)[:2])

# =============================================================================
hdr("24.11 Reading the ionosphere from two delays (15 and 20 MHz, 1.00 and 0.75 ms)")
f1, f2 = 15e6, 20e6
t1, t2 = 1.00e-3, 0.75e-3
# solve tau(f) = L / (c sqrt(1 - fp^2/f^2)) for fp, L
r2 = (t1 / t2) ** 2
x = (r2 - 1) / (r2 / f1**2 - 1 / f2**2)   # fp^2
fp = np.sqrt(x)
s1, s2 = np.sqrt(1 - x / f1**2), np.sqrt(1 - x / f2**2)
L11 = t1 * cC * s1
print(f"  (t1/t2)^2 = {r2:.6g}; fp^2 = {x:.6g} -> fp = {fp/1e6:.6g} MHz ; s(15) = {s1:.6g}, s(20) = {s2:.6g} ; L = {L11/1e3:.6g} km (from t2: {t2*cC*s2/1e3:.6g})")
close("24.11 fp = 12 MHz, L = 180 km", [fp, L11], [12e6, 180e3])
# brute force: grid search of (fp, L)
fps = np.linspace(5e6, 14.9e6, 9901)
best = None
for fq in fps:
    Lq = t1 * cC * np.sqrt(1 - fq**2 / f1**2)
    err = abs(Lq / (cC * np.sqrt(1 - fq**2 / f2**2)) - t2)
    if best is None or err < best[0]:
        best = (err, fq, Lq)
print(f"  grid search: fp = {best[1]/1e6:.4f} MHz, L = {best[2]/1e3:.4f} km")
check("24.11 grid search agrees", abs(best[1] - 12e6) < 2e3)
for f in (f1, f2):
    s = np.sqrt(1 - fp**2 / f**2)
    w = 2 * np.pi * f; wp = 2 * np.pi * fp; bq = np.sqrt(w**2 - wp**2) / cC
    vg_fd = (np.sqrt(wp**2 + cC**2 * (bq + 1e-5) ** 2) - np.sqrt(wp**2 + cC**2 * (bq - 1e-5) ** 2)) / 2e-5
    print(f"  f = {f/1e6:.4g} MHz: vg = {cC*s:.6g} (FD {vg_fd:.6g}), vp = {cC/s:.6g}, crest time {L11*s/cC*1e3:.6g} ms, envelope {L11/(cC*s)*1e3:.6g} ms")
    close(f"24.11 vg FD at {f/1e6:.4g} MHz", vg_fd, cC * s, rtol=1e-5)
print(f"  vacuum time over L: {L11/cC*1e3:.6g} ms")
wp = 2 * np.pi * fp
N = wp**2 * me * eps0 / e**2
print(f"  N = (2 pi fp)^2 m eps0 / e^2 = {N:.6g} m^-3")
close("24.11 N = 1.786e12", N, 1.786e12, rtol=1e-3)
tau = lambda f: L11 / (cC * np.sqrt(1 - (fp / f) ** 2))
spread = tau(19.95e6) - tau(20.05e6)
print(f"  (d) tau(19.95 MHz) = {tau(19.95e6)*1e3:.7g} ms, tau(20.05 MHz) = {tau(20.05e6)*1e3:.7g} ms, spread = {spread*1e6:.6g} us")
dtau = L11 * fp**2 / (cC * f2**3 * s2**3) * 0.1e6
print(f"  (d) derivative estimate |dtau/df| * 100 kHz = {dtau*1e6:.6g} us ; = (L/c)(fp^2/f^3)/s^3 * df with L/c = {L11/cC*1e3:.4g} ms, fp^2/f^3 = {fp**2/f2**3:.4g}, s^3 = {s2**3:.4g}")
close("24.11 spread ~ 2.1 us", spread, 2.109e-6, rtol=2e-3)
print(f"  (d) 15 vs 20 MHz lag: {(t1 - t2)*1e3:.6g} ms")
# (e) 10 MHz below cutoff
f5 = 10e6; b2 = ((2 * np.pi * f5) ** 2 - wp**2) / cC**2
print(f"  (e) 10 MHz: beta^2 = {b2:.6g} < 0 -> cut off (evanescent, 1/e depth {1/np.sqrt(-b2):.4g} m)")
check("24.11 10 MHz below cutoff", b2 < 0)

# =============================================================================
hdr("24.12 An elliptically rotating sheet current on x = 0 (free space, 150 MHz)")
f12 = 150e6; w12 = 2 * np.pi * f12; b12 = w12 / cC
print(f"  beta = {b12:.6g} = {b12/np.pi:.6g} pi, lambda = {2*np.pi/b12:.6g} m, eta0/2 = 60 pi = {eta0/2:.6g}")
Js = lambda t: 0.2 * np.cos(w12 * t) * Y - 0.1 * np.sin(w12 * t) * Z
J0 = 0.2 * Y + 0.1j * Z
check("24.12 Js phasor 0.2y + 0.1jz", all(np.allclose(np.real(J0 * np.exp(1j * w12 * t)), Js(t)) for t in np.linspace(0, 1 / f12, 9)))
# time-domain sheet fields: E = -(eta/2) Js(t - |x|/c), H = (1/2) Js(t - |x|/c) x n
Esh = lambda r, t: -eta0 / 2 * Js(t - abs(r[0]) / cC)
Hsh = lambda r, t: 0.5 * np.cross(Js(t - abs(r[0]) / cC), np.sign(r[0]) * X)
Ep = -eta0 / 2 * J0
print("  E phasor amplitude (both sides) = -(eta0/2) J =", Ep, " = -(12pi y + 6pi j z):", np.allclose(Ep, -(12 * np.pi * Y + 6j * np.pi * Z)))
close("24.12 E amplitude", Ep, -(12 * np.pi * Y + 6j * np.pi * Z))
print(f"  12 pi = {12*np.pi:.6g} V/m, 6 pi = {6*np.pi:.6g} V/m")
Hp = 0.5 * np.cross(J0, X); Hm = 0.5 * np.cross(J0, -X)
print("  H+ =", Hp, " (= -0.1 z + 0.05 j y);  H- =", Hm, " (= 0.1 z - 0.05 j y)")
close("24.12 H+ = -0.1z + 0.05jy", Hp, -0.1 * Z + 0.05j * Y)
close("24.12 H- = -H+", Hm, -Hp)
close("24.12 H+ = x x E/eta0", Hp, np.cross(X, Ep) / eta0)
close("24.12 H- = (-x) x E/eta0", Hm, np.cross(-X, Ep) / eta0)
# phasor vs time-domain consistency on each side
for side, sg in (("+", 1), ("-", -1)):
    fEp = phasor_field(Ep, b12 * sg * X, w12)
    ok = all(np.allclose(fEp((sg * 0.37, 0, 0), t), Esh((sg * 0.37, 0, 0), t)) for t in np.linspace(0, 1 / f12, 9))
    check(f"24.12 E{side} phasor matches -(eta/2) Js(t - |x|/c)", ok)
kP = classify(Esh, X, (0.5, 0, 0), 1 / f12)
kM = classify(Esh, -X, (-0.5, 0, 0), 1 / f12)
print("  x > 0 (u = +x):", kP, " x < 0 (u = -x):", kM)
check("24.12 x>0 left elliptical, x<0 right elliptical", kP[:2] == ("elliptical", "left") and kM[:2] == ("elliptical", "right"))
print("  sheet current itself at t=0, T/4:", Js(0), np.round(Js(0.25 / f12), 12), "(turns y -> -z)")
print("  E at x=0+: t=0", np.round(Esh((1e-12, 0, 0), 0), 6), " T/4", np.round(Esh((1e-12, 0, 0), 0.25 / f12), 6))
Sside = (abs(Ep[1]) ** 2 + abs(Ep[2]) ** 2) / (2 * eta0)
print(f"  <S> each side = ((12pi)^2 + (6pi)^2)/(240 pi) = {Sside:.6g} W/m^2 = 0.75 pi = {0.75*np.pi:.6g}")
close("24.12 <S> per side 0.75 pi", Sside, 0.75 * np.pi)
SqP = avgS(Esh, Hsh, (0.8, 0, 0), 1 / f12)
SqM = avgS(Esh, Hsh, (-0.8, 0, 0), 1 / f12)
print("  quadrature <S> at x = +0.8:", SqP, " at x = -0.8:", SqM)
close("24.12 quadrature x>0", SqP, 0.75 * np.pi * X, rtol=1e-4)
close("24.12 quadrature x<0", SqM, -0.75 * np.pi * X, rtol=1e-4)
ts = np.linspace(0, 1 / f12, 20000, endpoint=False)
pJ = np.mean([-Js(t) @ Esh((0, 0, 0), t) for t in ts])
print(f"  <-Js . E> at the sheet = {pJ:.6g} W/m^2 = 1.5 pi = {1.5*np.pi:.6g} (= 2 x 0.75 pi)")
close("24.12 power balance", pJ, 1.5 * np.pi, rtol=1e-4)
print(f"  0.5 Re(-J . E*) = {0.5*np.real(-J0 @ np.conj(Ep)):.6g}")
# (d) decompose E+ into right + left for +x travel: basis (y - jz) right, (y + jz) left
fRb = phasor_field(Y - 1j * Z, b12 * X, w12); fLb = phasor_field(Y + 1j * Z, b12 * X, w12)
print("  +x basis: y - jz ->", classify(fRb, X, (0, 0, 0), 1 / f12)[:2], "; y + jz ->", classify(fLb, X, (0, 0, 0), 1 / f12)[:2])
check("24.12 y - jz right, y + jz left for +x", classify(fRb, X, (0, 0, 0), 1 / f12)[:2] == ("circular", "right")
      and classify(fLb, X, (0, 0, 0), 1 / f12)[:2] == ("circular", "left"))
M = np.array([[1, 1], [-1j, 1j]])
aR, aL = np.linalg.solve(M, np.array([Ep[1], Ep[2]]))
print(f"  E+ = ({aR:.6g})(y - jz) + ({aL:.6g})(y + jz) ; /pi: {aR/np.pi:.6g}, {aL/np.pi:.6g}")
close("24.12 weights -3pi (right), -9pi (left)", [aR, aL], [-3 * np.pi, -9 * np.pi])
PR = 2 * abs(aR) ** 2 / (2 * eta0); PL = 2 * abs(aL) ** 2 / (2 * eta0)
print(f"  powers: right {PR:.6g} = 0.075 pi = {0.075*np.pi:.6g}; left {PL:.6g} = 0.675 pi = {0.675*np.pi:.6g}; sum {PR+PL:.6g}")
close("24.12 circular powers add to 0.75 pi", PR + PL, 0.75 * np.pi)
print(f"  ellipse semi-axes at x>0: |aR|+|aL| = {abs(aR)+abs(aL):.6g} (12 pi = {12*np.pi:.6g}), |aL|-|aR| = {abs(aL)-abs(aR):.6g} (6 pi)")


# =============================================================================
hdr("Recipe values quoted on the page (u . [E(0) x E(T/4)])")
rv = lambda u, E0, E1: float(np.asarray(u, float) @ np.cross(E0, E1))
vals = {
    "24.3a": (rv(Z, 2 * Y, 2 * X), -4), "24.3b": (rv(-X, 3 * Y, -3 * Z), 9), "24.3c": (rv(Y, 0 * X, 2 * (Z - X)), 0),
    "24.3d": (rv(Z, 4 * X + 2 * Y, 2 * np.sqrt(3) * Y), 8 * np.sqrt(3)),
    "24.5": (rv(-Z, 5 * X, -5 * Y), 25), "24.6": (rv(-Y, 3 * Z, 3 * X), -9),
    "24.7b": (rv(Z, 4 * X, 2 * Y), 8), "24.8 E": (rv(X, -Z, Y), 1), "24.8 H": (rv(X, Y, Z), 1),
    "24.9": (rv(-Z, 6 * Y, 6 * X), 36),
}
for k_, (a_, b_) in vals.items():
    print(f"  {k_}: {a_:.6g} (page: {b_:.6g})")
check("recipe values match page", all(np.isclose(a_, b_) for a_, b_ in vals.values()))
# 24.4 and 24.10 general formulas: 6 B sin(phi) and E1 E2 sin(phi)
ok = True
for B_ in (0.0, 2.0, 6.0):
    for ph in np.linspace(0, 2 * np.pi, 9):
        E0 = 6 * Y + B_ * np.exp(1j * ph) * Z
        ok &= np.isclose(rv(-X, np.real(E0), -np.imag(E0)), 6 * B_ * np.sin(ph))
        E0 = 2.5 * Y + B_ * np.exp(1j * ph) * Z
        ok &= np.isclose(rv(-X, np.real(E0), -np.imag(E0)), 2.5 * B_ * np.sin(ph))
check("24.4: 6 B sin(phi); 24.10: E1 E2 sin(phi)", ok)
# 24.10 check: E x H at x=0, t=0 for (4, 3, pi/2)
Et0 = np.real(4 * Y + 3j * Z); Ht0 = np.real((3j * Y - 4 * Z) / eta0)
print("  24.10 E x H at origin, t=0 (times eta0):", np.cross(Et0, Ht0) * eta0, "(page: -16 x)")
check("24.10 E x H = -16 x / eta0", np.allclose(np.cross(Et0, Ht0) * eta0, -16 * X))
# 24.12 E(0) x E(T/4) at x = 0
Ep = -(12 * np.pi * Y + 6j * np.pi * Z)
c12 = np.cross(np.real(Ep), -np.imag(Ep))
print("  24.12 E(0) =", np.real(Ep), " E(T/4) =", -np.imag(Ep), " cross =", c12, " /pi^2 =", c12 / np.pi**2)
check("24.12 cross = -72 pi^2 x", np.allclose(c12, -72 * np.pi**2 * X))
# 24.9 check: E x H at origin, t=0
print("  24.9 E x H at origin, t=0:", np.cross(6 * Y, X / (20 * np.pi)), "(along -z)")
# 24.8 check: E x H at origin t=0
print("  24.8 E x H at origin, t=0:", np.cross(-24 * np.pi * Z, 0.1 * Y), " 2.4 pi =", 2.4 * np.pi)

# =============================================================================
hdr("Summary")
print(f"  {sum(ALL)} of {len(ALL)} checks OK")
