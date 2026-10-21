#!/usr/bin/env python3
"""Independent review checks for Lecture 24 (signal transmission, circular polarization).

Handedness convention (Kudeki notes p. 3-4): right-circular <=> right-hand thumb along the travel direction u,
fingers curl with the rotation of E at a fixed point <=> u . (E x dE/dt) > 0; equivalently clockwise as seen
looking along u (viewer behind the wave). Rao 4.5 uses the same convention.
"""
import numpy as np

R = []


def chk(name, ok, info=""):
    R.append(ok)
    print(("PASS " if ok else "FAIL ") + name + (f"  [{info}]" if info else ""))


def close(a, b, rtol=1e-3, atol=1e-12):
    return np.allclose(a, b, rtol=rtol, atol=atol)


X, Y, Z = np.eye(3)
c0 = 299792458.0
mu0 = 4e-7 * np.pi
eps0 = 1 / (mu0 * c0 ** 2)
eta0 = np.sqrt(mu0 / eps0)
e_ch, m_e = 1.602176634e-19, 9.1093837e-31          # CODATA 2018

# ---------------------------------------------------------------- handedness by numerical rotation
def rotation(Et, u, n=721):
    """Et(t) -> 3-vector at a fixed point, period 1. Returns ('right'|'left'|'linear', mean u.(E x dE/dt))."""
    t = np.linspace(0, 1, n)
    E = np.array([Et(tt) for tt in t])
    dE = np.gradient(E, t, axis=0)
    L = np.mean(np.einsum("ij,j->i", np.cross(E, dE), u))
    scale = np.mean(np.sum(E ** 2, axis=1)) + 1e-30
    if abs(L) < 1e-6 * scale:
        return "linear", L
    return ("right" if L > 0 else "left"), L


def screen_sense(Et, u, n=721):
    """sense on a screen viewed looking ALONG u: screen X x Y = -u (Z toward the viewer = -u)."""
    a = np.cross(u, X if abs(u @ X) < 0.9 else Y)
    a /= np.linalg.norm(a)
    b = np.cross(-u, a)            # X=a, Y=b with a x b = -u
    assert close(np.cross(a, b), -u)
    t = np.linspace(0, 1, n)
    E = np.array([Et(tt) for tt in t])
    xs, ys = E @ a, E @ b
    area = 0.5 * np.sum(xs[:-1] * ys[1:] - xs[1:] * ys[:-1])    # >0 counterclockwise on screen
    return "ccw" if area > 1e-9 else ("cw" if area < -1e-9 else "none")


def phasor_field(Ep, kvec, r):
    """time-domain E(r, t) of phasor Ep e^{-j k.r}, period 1"""
    return lambda t: np.real(Ep * np.exp(-1j * (kvec @ r)) * np.exp(2j * np.pi * t))


def recipe(Ep, u):
    E0, E4 = np.real(Ep), -np.imag(Ep)
    s = u @ np.cross(E0, E4)
    return "linear" if abs(s) < 1e-12 else ("right" if s > 0 else "left")


print("== D. Handedness: the notes' own statements, by rotating E at a fixed point ==")
# notes p.4: cos wt x + sin wt y (x - jy), travel +z: right; x + jy: left
h, _ = rotation(lambda t: np.cos(2 * np.pi * t) * X + np.sin(2 * np.pi * t) * Y, Z)
chk("notes p.4: cos x + sin y, +z travel -> right", h == "right")
chk("notes p.3: right-circular looks clockwise viewed along travel",
    screen_sense(lambda t: np.cos(2 * np.pi * t) * X + np.sin(2 * np.pi * t) * Y, Z) == "cw")
h, _ = rotation(lambda t: np.cos(2 * np.pi * t) * X - np.sin(2 * np.pi * t) * Y, Z)
chk("notes p.4: cos x - sin y, +z travel -> left", h == "left")
chk("notes p.3: left-circular counterclockwise viewed along travel",
    screen_sense(lambda t: np.cos(2 * np.pi * t) * X - np.sin(2 * np.pi * t) * Y, Z) == "ccw")
# phasor correspondences
for Ep, sgn in ((X - 1j * Y, +1), (X + 1j * Y, -1)):
    t = np.linspace(0, 1, 50)
    lhs = np.array([np.real(Ep * np.exp(2j * np.pi * tt)) for tt in t])
    rhs = np.array([np.cos(2 * np.pi * tt) * X + sgn * np.sin(2 * np.pi * tt) * Y for tt in t])
    chk(f"phasor {'x-jy' if sgn > 0 else 'x+jy'} <-> cos x {'+' if sgn > 0 else '-'} sin y", close(lhs, rhs))
# page: x - jy along -z is left-circular
h, _ = rotation(phasor_field(X - 1j * Y, -Z, np.zeros(3)), -Z)
chk("page trap: (x - jy)e^{+jbz} (travel -z) -> left", h == "left")
# Example 1: (z + jy) e^{+j beta x}: travel -x; rotation y -> z; left
k = -X * 2 * np.pi
Ep = Z + 1j * Y
h, _ = rotation(phasor_field(Ep, k, np.zeros(3)), -X)
chk("Example 1: (z+jy)e^{jbx} -> left", h == "left")
Et = phasor_field(Ep, k, np.zeros(3))
chk("Example 1: E(-T/4) = +y, E(0) = +z (y points first)", close(Et(-0.25), Y, atol=1e-12) and close(Et(0), Z))
chk("Example 1 recipe: z x (-y) = +x, (-x).(+x) < 0", recipe(Ep, -X) == "left" and close(np.cross(Z, -Y), X))
chk("Example 1: right thumb along -x curls z -> y (z x y = -x)", close(np.cross(Z, Y), -X))
# Example 2: J_s = cos x + sin y; E+- = -(eta/2) J_s(t -+ z/v)
for side, u in ((+1, Z), (-1, -Z)):
    zz = 0.37 * side
    Et = lambda t, zz=zz, side=side: -0.5 * (np.cos(2 * np.pi * (t - side * zz)) * X + np.sin(2 * np.pi * (t - side * zz)) * Y)
    h, _ = rotation(Et, u)
    chk(f"Example 2: E{'+' if side > 0 else '-'} -> {'right' if side > 0 else 'left'}", h == ("right" if side > 0 else "left"))
    # E x H along travel, with H = 1/2 J_s x n
    Ht = lambda t, zz=zz, side=side: 0.5 * np.cross(np.cos(2 * np.pi * (t - side * zz)) * X + np.sin(2 * np.pi * (t - side * zz)) * Y, u)
    S = np.mean([np.cross(Et(t), Ht(t)) for t in np.linspace(0, 1, 101)], axis=0)
    chk(f"Example 2: E x H along {'+z' if side > 0 else '-z'} (H = 1/2 Js x n)", S @ u > 0)
# notes margin p.8: J_s = x f(t): H- = y 1/2 f(t + z/v)
chk("notes p.8 margin: H- = 1/2 Js x (-z) = +y/2 for Js = x", close(0.5 * np.cross(X, -Z), 0.5 * Y))
# Recipe and section-5 rule vs numerical rotation for random phasors and directions
rng = np.random.default_rng(1)
bad_recipe = bad_rule = bad_lead = 0
for _ in range(400):
    u = rng.normal(size=3); u /= np.linalg.norm(u)
    a = np.cross(u, rng.normal(size=3)); a /= np.linalg.norm(a)
    b = np.cross(u, a)                       # a x b = u: (a, b, u) right-handed, like (x, y, z)
    A, B = rng.uniform(0.1, 2, 2)
    phi = rng.uniform(-np.pi, np.pi)
    Ep = (A * a + B * np.exp(1j * phi) * b) * np.exp(1j * rng.uniform(0, 2 * np.pi))
    kvec = 3.0 * u
    r0 = rng.normal(size=3)
    h, _ = rotation(phasor_field(Ep, kvec, r0), u)
    if recipe(Ep * np.exp(-1j * (kvec @ r0)), u) != h:
        bad_recipe += 1
    rule = "right" if np.sin(phi) < 0 else "left"
    if rule != h:
        bad_rule += 1
    # "leading component points first -> turns from leading axis to lagging axis"
    lead_is_a = np.sin(phi) < 0            # b lags a
    turns_a_to_b = (h == "right")          # rotation a -> b is right-handed about u
    if lead_is_a != turns_a_to_b:
        bad_lead += 1
chk("recipe u.[E(0) x E(T/4)] matches numerical rotation (400 random)", bad_recipe == 0, f"{bad_recipe} mismatches")
chk("section 5 rule: sin(phi)<0 right, >0 left, for +u travel (400 random)", bad_rule == 0, f"{bad_rule}")
chk("leading axis -> lagging axis rule (400 random)", bad_lead == 0, f"{bad_lead}")
# travel -z swaps
h, _ = rotation(phasor_field(X + 0.5 * np.exp(-0.7j) * Y, -Z * 2 * np.pi, np.zeros(3)), -Z)
chk("section 5: sin(phi)<0 with travel -z is left (swap)", h == "left")
# overall factor never changes the hand
ok = True
for f in (-1, 1j, -1j, 377.0, 2 * np.exp(0.3j)):
    ok &= rotation(phasor_field(f * (X - 1j * Y), Z, np.zeros(3)), Z)[0] == "right"
chk("overall factor (-1, j, eta, complex) never changes the hand", ok)
# H has the same polarization and hand as E
Ep = X + 0.6 * np.exp(-1.1j) * Y
Hp = np.cross(Z, Ep) / 377
chk("H = u x E / eta: same hand as E", rotation(phasor_field(Hp, Z, np.zeros(3)), Z)[0] == rotation(phasor_field(Ep, Z, np.zeros(3)), Z)[0])
# Section 5 rule on other axes: cyclic order (y,z | x), (z,x | y) works; anti-cyclic order flips the hand
ok_cyc, flips = True, True
for a_, b_, c_ in ((Y, Z, X), (Z, X, Y), (X, Y, Z)):
    for phi in (-2.0, -np.pi / 2, -0.4, 0.4, np.pi / 2, 2.3):
        for sgn in (+1, -1):
            u = sgn * c_
            Ep = a_ + 0.7 * np.exp(1j * phi) * b_
            h, _ = rotation(phasor_field(Ep, 2 * np.pi * u, np.zeros(3)), u)
            rule = ("right" if np.sin(phi) < 0 else "left")
            if sgn < 0:
                rule = {"right": "left", "left": "right"}[rule]
            ok_cyc &= (h == rule)
            Ep2 = b_ + 0.7 * np.exp(1j * phi) * a_          # anti-cyclic naming
            h2, _ = rotation(phasor_field(Ep2, 2 * np.pi * u, np.zeros(3)), u)
            flips &= (h2 != rule)
chk("section 5 rule with cyclic axes (y,z|+-x), (z,x|+-y) matches rotation", ok_cyc)
chk("anti-cyclic naming (e.g. z,y for x travel) flips the rule's answer", flips)
# Example 1 via the cyclic rule: (z + jy) = j(y - jz): first y, second z, phi = -pi/2 -> right for +x; travel -x -> left
chk("Example 1 via cyclic rule: j(y - jz)e^{jbx} -> left", np.allclose(Z + 1j * Y, 1j * (Y - 1j * Z)))
# FA23-type: H(z,t) = x A cos + y B cos(.+phi): hand of H = hand of E
for A_, B_, phi in ((2, 4, 0.0), (4, 2, np.pi), (2, 2, np.pi / 4)):
    Hp = A_ * X + B_ * np.exp(1j * phi) * Y
    Ep = -377 * np.cross(Z, Hp)          # E = -eta u x H
    hE = rotation(phasor_field(Ep, 2 * np.pi * Z, np.zeros(3)), Z)[0]
    hH = rotation(phasor_field(Hp, 2 * np.pi * Z, np.zeros(3)), Z)[0]
    chk(f"H and E share polarization (A={A_}, B={B_}, phi={phi:.3f}): {hH}", hE == hH)
# Figure frame: x up, y right, z into page. screen (X right, Y up, Z out): x=(0,1,0), y=(1,0,0)
xs, ys = np.array([0, 1, 0]), np.array([1, 0, 0])
chk("figure frame: x_up x y_right = into page (= +z, travel)", close(np.cross(xs, ys), [0, 0, -1]))
# on screen, x(up) -> y(right) is clockwise: z-component of up x right < 0
chk("figure: rotation up -> right is clockwise on the page", np.cross(xs, ys)[2] < 0)
# circular / elliptical / linear classification
def kind(A, B, phi):
    Ep = A * X + B * np.exp(1j * phi) * Y
    t = np.linspace(0, 1, 721)
    E = np.array([np.real(Ep * np.exp(2j * np.pi * tt)) for tt in t])
    m = np.linalg.norm(E, axis=1)
    h, _ = rotation(phasor_field(Ep, Z, np.zeros(3)), Z)
    if h == "linear":
        return "linear"
    return h + ("-circular" if np.ptp(m) < 1e-6 else "-elliptical")
cases = {(1, 1, -np.pi / 2): "right-circular", (1, 1, np.pi / 2): "left-circular", (1, 1, 0): "linear",
         (1, 1, np.pi): "linear", (1, 0, 0.7): "linear", (0, 1, 0.7): "linear", (1, 2, -np.pi / 2): "right-elliptical",
         (1, 1, np.pi / 4): "left-elliptical", (1, 1, -np.pi / 4): "right-elliptical", (1, 1, 3 * np.pi / 4): "left-elliptical",
         (1, 1, -3 * np.pi / 4): "right-elliptical"}
for (A, B, p), want in cases.items():
    got = kind(A, B, p)
    chk(f"classification A={A},B={B},phi={p:+.3f}: {want}", got == want, got)
# figure phase-family labels from figs_l24.pol_kind
import sys, io, contextlib
sys.path.insert(0, "/home/claude/work")
with contextlib.redirect_stdout(io.StringIO()):
    import figs_l24
okfig = all(figs_l24.pol_kind(p) == kind(1, 1, p) for p, _ in figs_l24.PHASES)
chk("figure pol-phase-family: all 8 panel labels match numerical rotation", okfig,
    "; ".join(f"{l}:{figs_l24.pol_kind(p)}" for p, l in figs_l24.PHASES))
# exam-style checks (methods only): FA23-type H field with phi=pi/4 equal amps -> elliptical
print()
print("== A. Fields 1-3, Maxwell by finite differences ==")
v = c0 / 2.0; eta = eta0 / 2.0; eps = 4 * eps0; mu = mu0
w = 2 * np.pi * 1e6; beta = w / v
chk("beta = w sqrt(mu eps)", close(beta, w * np.sqrt(mu * eps)))
m = lambda t: 1 + 0.5 * np.cos(2 * np.pi * 2e4 * t)
def Ef(z, t):
    return m(t - z / v) * np.array([np.cos(w * t - beta * z), np.sin(w * t - beta * z), 0 * z])
def Hf(z, t):
    return m(t - z / v) / eta * np.array([-np.sin(w * t - beta * z), np.cos(w * t - beta * z), 0 * z])
z0, t0, dz, dt = 13.0, 2.3e-6, 1e-3, 1e-12
dEdz = (Ef(z0 + dz, t0) - Ef(z0 - dz, t0)) / (2 * dz)
dHdz = (Hf(z0 + dz, t0) - Hf(z0 - dz, t0)) / (2 * dz)
dEdt = (Ef(z0, t0 + dt) - Ef(z0, t0 - dt)) / (2 * dt)
dHdt = (Hf(z0, t0 + dt) - Hf(z0, t0 - dt)) / (2 * dt)
curlE = np.array([-dEdz[1], dEdz[0], 0]); curlH = np.array([-dHdz[1], dHdz[0], 0])
chk("circular AM field: curl E = -mu dH/dt", close(curlE, -mu * dHdt, rtol=1e-5))
chk("circular AM field: curl H = eps dE/dt", close(curlH, eps * dEdt, rtol=1e-5))
chk("notes H = m[cos y - sin x]/eta equals z x E/eta", close(Hf(z0, t0), np.cross(Z, Ef(z0, t0)) / eta))
tt = np.linspace(0, 1e-6, 7)
chk("Field 3: sin(wt - bz) = cos(w(t - T/4) - bz)", close(np.sin(w * tt - 0.3), np.cos(w * (tt - 0.25 * 2 * np.pi / w) - 0.3)))
chk("circular carrier: |E| constant at fixed z (m=1)", np.ptp([np.linalg.norm(Ef(z0, t) / m(t - z0 / v)) for t in np.linspace(0, 3e-6, 50)]) < 1e-12)

print()
print("== B. Group velocity: simulated AM pulse through a plasma ==")
wp = 1.0; cc = 1.0
bet = lambda w: np.sqrt(np.maximum(w ** 2 - wp ** 2, 0)) / cc
w0 = 2.0
b0 = bet(w0); vp = w0 / b0; vg = cc ** 2 * b0 / w0
h = 1e-5
vg_fd = 2 * h / (bet(w0 + h) - bet(w0 - h))
chk("v_g = 1/(dbeta/dw) (finite difference) = c^2 beta/w", close(vg_fd, vg, rtol=1e-8))
chk("v_p v_g = c^2", close(vp * vg, cc ** 2))
chk("v_g = c sqrt(1 - wp^2/w^2)", close(vg, np.sqrt(1 - wp ** 2 / w0 ** 2)))
chk("w = 2 wp: v_g = 0.866c, v_p = 1.155c (concept page; figure 0.87c, 1.15c)", round(vg, 3) == 0.866 and round(vp, 3) == 1.155)
# simulate: s(t) = m(t) e^{j w0 t}, Gaussian m; propagate with exact beta; measure envelope peak arrival at z
n, dt_ = 2 ** 17, 0.05
t = (np.arange(n) - n // 2) * dt_
sig = 25.0
s = np.exp(-t ** 2 / (2 * sig ** 2)) * np.exp(1j * w0 * t)
S = np.fft.fft(s)
wgrid = 2 * np.pi * np.fft.fftfreq(n, dt_)
for zz in (200.0, 600.0):
    out = np.fft.ifft(S * np.exp(-1j * bet(wgrid) * zz) * (wgrid > 0))
    env = np.abs(out)
    i = np.argmax(env)
    # parabolic refinement
    tpk = t[i] + dt_ * 0.5 * (env[i - 1] - env[i + 1]) / (env[i - 1] - 2 * env[i] + env[i + 1])
    chk(f"simulated envelope delay at z={zz:.0f}: {tpk:.3f} vs z/v_g = {zz / vg:.3f}", abs(tpk - zz / vg) / (zz / vg) < 2e-3,
        f"z/v_p = {zz / vp:.1f}")
# crest moves at v_p: phase of the analytic signal at the envelope peak
zz = 200.0
out1 = np.fft.ifft(S * np.exp(-1j * bet(wgrid) * zz) * (wgrid > 0))
i = np.argmin(abs(t - zz / vg))
ph1 = np.angle(out1[i] * np.exp(-1j * (w0 * t[i] - b0 * zz)))
chk("carrier phase at the envelope peak = w0 t - beta0 z (crests at v_p)", abs(ph1) < 0.15, f"residual {ph1:.3f} rad")
# non-dispersive medium: undistorted, delay z/v
out2 = np.fft.ifft(S * np.exp(-1j * wgrid / 0.5 * 100.0) * (wgrid > 0))
chk("non-dispersive: m(t - z/v) cos(wt - bz), undistorted", close(np.abs(out2), np.abs(np.roll(s, int(round(200 / dt_)))), atol=1e-9))
# second-order spreading estimate
b2 = (bet(w0 + 1e-3) - 2 * b0 + bet(w0 - 1e-3)) / 1e-6
chk("beta'' = -wp^2/(c (w^2-wp^2)^{3/2})", close(b2, -wp ** 2 / (cc * (w0 ** 2 - wp ** 2) ** 1.5), rtol=1e-4))
zz = 600.0
out = np.fft.ifft(S * np.exp(-1j * bet(wgrid) * zz) * (wgrid > 0))
env = np.abs(out); tc = np.sum(t * env ** 2) / np.sum(env ** 2)
sig_out = np.sqrt(np.sum((t - tc) ** 2 * env ** 2) / np.sum(env ** 2)) * np.sqrt(2)
pred = sig * np.sqrt(1 + (b2 * zz / sig ** 2) ** 2)
chk(f"envelope spreads only at 2nd order: width {sig_out:.3f} vs Gaussian prediction {pred:.3f}", close(sig_out, pred, rtol=1e-3))
# dielectric and gas rows: v_g = v_p
epsr = 2.25
bd = lambda w: w * np.sqrt(mu0 * epsr * eps0)
chk("dielectric: v_g = v_p = 1/sqrt(mu eps)", close(2e-3 / (bd(1e6 + 1e-3) - bd(1e6 - 1e-3)), 1 / np.sqrt(mu0 * epsr * eps0), rtol=1e-6))
kB, mHe, T = 1.380649e-23, 4.0026 * 1.66053907e-27, 300.0
bg = lambda w: w * np.sqrt(mHe / (5 / 3 * kB * T))
vg_g = 2e-3 / (bg(1e3 + 1e-3) - bg(1e3 - 1e-3))
chk(f"gas (He, 300 K): v_g = v_p = sqrt(5kT/3m) = {vg_g:.0f} m/s", close(vg_g, np.sqrt(5 * kB * T / (3 * mHe)), rtol=1e-6))
# good conductor beta = sqrt(w mu sigma/2): v_g = 2 v_p
sg = 5.8e7
bc = lambda w: np.sqrt(w * mu0 * sg / 2)
wc = 2 * np.pi * 1e6
chk("good conductor: v_g = 2 v_p", close(2 * wc * 1e-6 / (bc(wc * (1 + 1e-6)) - bc(wc * (1 - 1e-6))), 2 * wc / bc(wc), rtol=1e-6))
# ionosphere example (handbook: f_p = 8.98 sqrt(N) Hz; Rao 10.1: f_N = sqrt(80.6 N))
N = 1e12
fp = np.sqrt(N * e_ch ** 2 / (m_e * eps0)) / (2 * np.pi)
chk(f"f_p(N=1e12) = {fp / 1e6:.3f} MHz ~ 8.98 MHz; Rao sqrt(80.6N) = {np.sqrt(80.6 * N) / 1e6:.3f}", round(fp / 1e6, 2) == 8.98)
f = 10e6
r = np.sqrt(1 - fp ** 2 / f ** 2)
chk(f"10 MHz: sqrt(1-fp^2/f^2) = {r:.4f} -> 0.440", round(r, 3) == 0.440)
chk(f"10 MHz: v_p = {1 / r:.3f} c -> 2.27c", round(1 / r, 2) == 2.27)
L = 300e3
tg, tv, tp = L / (r * c0), L / c0, L * r / c0
chk(f"300 km: envelope {tg * 1e3:.3f} ms (2.27), vacuum {tv * 1e3:.3f} ms (1.00), crest {tp * 1e3:.3f} ms (0.44)",
    round(tg * 1e3, 2) == 2.27 and round(tv * 1e3, 2) == 1.00 and round(tp * 1e3, 2) == 0.44)
r100 = np.sqrt(1 - fp ** 2 / 100e6 ** 2)
chk(f"100 MHz: v_g = {r100:.4f} c -> 0.996c", round(r100, 3) == 0.996)
# narrowband condition for the ionosphere example? 300 km, a 10 kHz message
b2i = -(2 * np.pi * fp) ** 2 / (c0 * ((2 * np.pi * f) ** 2 - (2 * np.pi * fp) ** 2) ** 1.5)
Om = 2 * np.pi * 10e3
sp3 = 0.5 * abs(b2i) * (2 * np.pi * 3e3) ** 2 * L
chk(f"ionosphere example narrowband: 1/2|beta''|Omega^2 z (300 km, 10 MHz) = {sp3:.3f} for a 3 kHz voice band (<<1)", sp3 < 0.05,
    f"10 kHz: {0.5 * abs(b2i) * Om ** 2 * L:.2f}, not <<1")

print()
print("== C/H. Power of a circular wave ==")
Ep = X - 1j * Y
Hp = np.cross(Z, Ep) / eta0
chk("Example 3: H = (y + jx)/eta0", close(Hp, (Y + 1j * X) / eta0))
Sav = 0.5 * np.real(np.cross(Ep, np.conj(Hp)))
chk(f"Example 3: <S> = z/eta0 = {Sav[2] * 1e3:.3f} mW/m^2 (2.65)", close(Sav, Z / eta0) and round(Sav[2] * 1e3, 2) == 2.65)
chk("Example 3 step: (x - jy) x (y - jx) = 2z", close(np.cross(X - 1j * Y, Y - 1j * X), 2 * Z))
chk("Example 3 step: (-jy) x (-jx) = +z", close(np.cross(-1j * Y, -1j * X), Z))
tq = np.linspace(0, 1, 2001)[:-1]
Sinst = np.array([np.cross(np.real(Ep * np.exp(2j * np.pi * s_)), np.real(Hp * np.exp(2j * np.pi * s_))) for s_ in tq])
chk("quadrature <E x H> = 1/2 Re{E x H*}", close(Sinst.mean(axis=0), Sav))
chk("circular: instantaneous S constant = <S>", np.ptp(Sinst[:, 2]) < 1e-15 and close(Sinst[0], Sav))
Ep2 = X
Hp2 = np.cross(Z, Ep2) / eta0
S2 = np.array([np.cross(np.real(Ep2 * np.exp(2j * np.pi * s_)), np.real(Hp2 * np.exp(2j * np.pi * s_))) for s_ in tq])
chk("linear: <S> = 1/(2 eta0) (half), pulses at 2w", close(S2.mean(axis=0)[2], 1 / (2 * eta0)) and
    abs(np.fft.rfft(S2[:, 2])[2]) > 100 * abs(np.fft.rfft(S2[:, 2])[1]))
ok = True
for _ in range(50):
    Ep = rng.normal(size=2) + 1j * rng.normal(size=2); Ep = np.array([Ep[0], Ep[1], 0])
    for u in (Z, -Z):
        Hp = np.cross(u, Ep) / 300
        ok &= close(0.5 * np.real(np.cross(Ep, np.conj(Hp))), (abs(Ep[0]) ** 2 + abs(Ep[1]) ** 2) / 600 * u)
chk("<S> = (|Ex|^2+|Ey|^2)/(2 eta) u for any phase (50 random)", ok)

print()
print("== F. Bases ==")
chk("x = 1/2(x-jy) + 1/2(x+jy)", close(0.5 * (X - 1j * Y) + 0.5 * (X + 1j * Y), X))
chk("y = -1/(2j)(x-jy) + 1/(2j)(x+jy)", close(-1 / 2j * (X - 1j * Y) + 1 / 2j * (X + 1j * Y), Y))

print()
print("== I. Worked problem: two crossed sheets a quarter wave apart ==")
f = 300e6; cW = 3e8; etaW = 120 * np.pi
lam = cW / f; bW = 2 * np.pi * f / cW
chk("beta = 2 pi rad/m, lambda = 1 m", close(bW, 2 * np.pi) and close(lam, 1.0))
chk("eta0/2 * 0.1 = 6 pi V/m", close(etaW / 2 * 0.1, 6 * np.pi))

def E_time(z, t, phi):
    """direct time-domain superposition: E = -(eta/2) J_s(t - |z - z0|/c) for each sheet"""
    JA = lambda tt: 0.1 * np.cos(2 * np.pi * f * tt) * X
    JB = lambda tt: 0.1 * np.cos(2 * np.pi * f * tt + phi) * Y
    return -etaW / 2 * (JA(t - abs(z) / cW) + JB(t - abs(z - lam / 4) / cW))

def H_time(z, t, phi):
    JA = lambda tt: 0.1 * np.cos(2 * np.pi * f * tt) * X
    JB = lambda tt: 0.1 * np.cos(2 * np.pi * f * tt + phi) * Y
    nA = Z if z > 0 else -Z
    nB = Z if z > lam / 4 else -Z
    return 0.5 * (np.cross(JA(t - abs(z) / cW), nA) + np.cross(JB(t - abs(z - lam / 4) / cW), nB))

T = 1 / f
for phi in (0.3, np.pi, 0.0, np.pi / 2, 3 * np.pi / 2):
    P, Q = -6 * np.pi, 1j * np.exp(1j * phi)
    zz = 2.37
    Ep = P * np.exp(-1j * bW * zz) * (X + Q * Y)
    ok = all(close(E_time(zz, s_ * T, phi), np.real(Ep * np.exp(2j * np.pi * s_)), atol=1e-9) for s_ in np.linspace(0, 1, 13))
    chk(f"(a) phasor P e^(-jbz)(x + Qy), P=-6pi, Q=je^(j phi) matches time domain, phi={phi:.3f}", ok)
    zz = -0.81
    Ep = -6 * np.pi * (X + np.exp(1j * (phi - np.pi / 2)) * Y) * np.exp(1j * bW * zz)
    ok = all(close(E_time(zz, s_ * T, phi), np.real(Ep * np.exp(2j * np.pi * s_)), atol=1e-9) for s_ in np.linspace(0, 1, 13))
    chk(f"(c) z<0 phasor -6pi[x + e^(j(phi-pi/2)) y]e^(jbz) matches, phi={phi:.3f}", ok)

def classify_time(z, phi, u):
    h, _ = rotation(lambda s_: E_time(z, s_ * T, phi), u)
    if h == "linear":
        t_ = np.linspace(0, T, 400)
        E = np.array([E_time(z, tt, phi) for tt in t_])
        i = np.argmax(np.linalg.norm(E, axis=1))
        d = E[i] / np.linalg.norm(E[i])
        return "linear", d
    E = np.array([E_time(z, tt, phi) for tt in np.linspace(0, T, 400)])
    m_ = np.linalg.norm(E, axis=1)
    return h + ("-circular" if np.ptp(m_) < 1e-6 * m_.max() else "-elliptical"), None

k_, d = classify_time(2.37, np.pi / 2, Z)
chk("(b) phi = pi/2: linear along x - y", k_ == "linear" and abs(abs(d @ (X - Y) / np.sqrt(2)) - 1) < 1e-6)
k_, d = classify_time(2.37, 3 * np.pi / 2, Z)
chk("(b) phi = 3pi/2: linear along x + y", k_ == "linear" and abs(abs(d @ (X + Y) / np.sqrt(2)) - 1) < 1e-6)
chk("(b) phi = pi: right-circular in z > lambda/4", classify_time(2.37, np.pi, Z)[0] == "right-circular")
chk("(b) phi = 0: left-circular in z > lambda/4", classify_time(2.37, 0.0, Z)[0] == "left-circular")
chk("(c) phi = pi: right-circular in z < 0 (travel -z)", classify_time(-0.81, np.pi, -Z)[0] == "right-circular")
chk("     extra: phi = 0 in z < 0 is left-circular", classify_time(-0.81, 0.0, -Z)[0] == "left-circular")
chk("(b) phi=pi recipe: E(0) = -6pi x, E(T/4) = -6pi y at z=0",
    close(np.real(-6 * np.pi * (X - 1j * Y)), -6 * np.pi * X) and close(-np.imag(-6 * np.pi * (X - 1j * Y)), -6 * np.pi * Y))
chk("(b) recipe point z = 1 m (in z > lambda/4): actual E(0) = -6pi x, E(T/4) = -6pi y",
    close(E_time(1.0, 0.0, np.pi), -6 * np.pi * X, atol=1e-9) and close(E_time(1.0, T / 4, np.pi), -6 * np.pi * Y, atol=1e-9))
chk("     (z = 0 is outside z > lambda/4: there E(T/4) = +6pi y, the z<0 wave)",
    close(E_time(0.0, T / 4, np.pi), 6 * np.pi * Y, atol=1e-9))
chk("(c) recipe point z = 0: actual E(0) = -6pi x, E(T/4) = +6pi y",
    close(E_time(0.0, 0.0, np.pi), -6 * np.pi * X, atol=1e-9) and close(E_time(-1e-12, T / 4, np.pi), 6 * np.pi * Y, atol=1e-6))
chk("(b) time domain: -6pi[cos x + sin y]", close(E_time(2.37, 0.1 * T, np.pi),
    -6 * np.pi * (np.cos(2 * np.pi * 0.1 - bW * 2.37) * X + np.sin(2 * np.pi * 0.1 - bW * 2.37) * Y), atol=1e-9))
chk("(c) recipe: E(T/4) = +6pi y, cross = -36pi^2 z", close(-np.imag(-6 * np.pi * (X + 1j * Y)), 6 * np.pi * Y) and
    close(np.cross(-6 * np.pi * X, 6 * np.pi * Y), -36 * np.pi ** 2 * Z))
for phi in (np.pi / 2, 3 * np.pi / 2, np.pi, 0.0, 1.1):
    tq = np.linspace(0, T, 2001)[:-1]
    Sav = np.mean([np.cross(E_time(2.37, tt, phi), H_time(2.37, tt, phi)) for tt in tq], axis=0)
    chk(f"(d) <S> = 0.3 pi z = 0.942 W/m^2 by quadrature, phi={phi:.3f}", close(Sav, 0.3 * np.pi * Z, rtol=1e-6) and round(0.3 * np.pi, 2) == 0.94)
Sa = np.mean([np.cross(-etaW / 2 * 0.1 * np.cos(2 * np.pi * f * tt) * X, 0.5 * np.cross(0.1 * np.cos(2 * np.pi * f * tt) * X, Z))
              for tt in np.linspace(0, T, 2001)[:-1]], axis=0)
chk("(d) one sheet alone: 0.15 pi", close(Sa, 0.15 * np.pi * Z, rtol=1e-6))
# compare with exam key numbers (must differ): FE #4 key: P = 60pi, Q = -e^{j phi}, right pi/2, left -pi/2, <S> = 30 pi
chk("re-parameterized: no answer equals the Summer 2020 FE #4 key (P 60pi, <S> 30pi, right pi/2)",
    not close(-6 * np.pi, 60 * np.pi) and not close(0.3 * np.pi, 30 * np.pi) and not close(np.pi, np.pi / 2))

print()
print(f"{sum(R)}/{len(R)} PASS" + ("" if all(R) else "   <-- FAILURES"))
