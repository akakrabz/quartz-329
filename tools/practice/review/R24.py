# Independent review checks for practice page 24
import numpy as np
from scipy.optimize import brentq

c = 3e8
eta0 = 120 * np.pi
mu0 = eta0 / c
eps0 = 1 / (eta0 * c)
X, Y, Z = np.eye(3)
NF = 0


def chk(name, page, val, rtol=2e-3, atol=1e-12):
    global NF
    page = np.asarray(page, dtype=complex)
    val = np.asarray(val, dtype=complex)
    ok = np.allclose(page, val, rtol=rtol, atol=atol)
    NF += (not ok)
    fm = lambda a: np.array2string(np.atleast_1d(a), formatter={'complex_kind': lambda z: f"{z.real:.5g}{z.imag:+.5g}j" if abs(z.imag) > 1e-12 * max(1, abs(z)) else f"{z.real:.5g}"}, max_line_width=200)
    print(f"{'PASS' if ok else 'FAIL'}  {name}: page={fm(page)} computed={fm(val)}")


def chks(name, page, val):
    global NF
    ok = page == val
    NF += (not ok)
    print(f"{'PASS' if ok else 'FAIL'}  {name}: page={page!r} computed={val!r}")


def real_field(Eph, w):
    # time-domain field from a phasor function
    return lambda r, t: np.real(Eph(np.asarray(r, float)) * np.exp(1j * w * t))


def travel(Ereal, v, T):
    # brute force: which axis does the pattern move along?
    rng = np.random.default_rng(0)
    hits = []
    for s in (1, -1):
        for e, n in ((X, 'x'), (Y, 'y'), (Z, 'z')):
            u = s * e
            err = 0
            for _ in range(20):
                r0 = rng.uniform(-2, 2, 3); t0 = rng.uniform(0, T); dt = 0.137 * T
                d = Ereal(r0 + u * v * dt, t0 + dt) - Ereal(r0, t0)
                err = max(err, np.abs(d).max())
            scale = np.abs(Ereal(np.zeros(3), 0.3 * T)).max() + np.abs(Ereal(np.zeros(3), 0.1 * T)).max()
            if err < 1e-7 * scale:
                hits.append(('+' if s > 0 else '-') + n)
    assert len(hits) == 1, hits
    return hits[0]


UV = {'+x': X, '-x': -X, '+y': Y, '-y': -Y, '+z': Z, '-z': -Z}


def pol(Ereal, r0, u, T, N=4000):
    # rotate the real field at a fixed point; sweep>0 about u = right
    ts = np.linspace(0, T, N + 1)
    Es = np.array([Ereal(r0, t) for t in ts])
    a = X if abs(u @ X) < 0.9 else Y
    e1 = a - (a @ u) * u; e1 /= np.linalg.norm(e1); e2 = np.cross(u, e1)
    p1, p2 = Es @ e1, Es @ e2
    mag = np.hypot(p1, p2)
    assert np.abs(Es @ u).max() < 1e-9 * mag.max() + 1e-15
    ratio = mag.min() / mag.max()
    if ratio < 1e-6:
        return 'linear', mag.max(), mag.min(), Es[np.argmax(mag)]
    sweep = np.unwrap(np.arctan2(p2, p1))
    sweep = sweep[-1] - sweep[0]
    hand = 'right' if sweep > 0 else 'left'
    shape = 'circular' if ratio > 1 - 1e-6 else 'elliptical'
    return f"{hand} {shape}", mag.max(), mag.min(), None


def curl(F, r, h=1e-6):
    r = np.asarray(r, float)
    J = np.zeros((3, 3), complex)
    for j in range(3):
        e = np.zeros(3); e[j] = h
        J[:, j] = (F(r + e) - F(r - e)) / (2 * h)
    return np.array([J[2, 1] - J[1, 2], J[0, 2] - J[2, 0], J[1, 0] - J[0, 1]])


def H_from_E(Eph, w, mu):
    return lambda r: -curl(Eph, r) / (1j * w * mu)


def S_avg(Eph, Hph, w, r0=(0.3, -0.2, 0.1), N=720):
    # brute-force time average of E x H
    T = 2 * np.pi / w
    ts = np.arange(N) * T / N
    Er, Hr = real_field(Eph, w), real_field(Hph, w)
    return np.mean([np.cross(Er(r0, t), Hr(r0, t)) for t in ts], axis=0)


def vg_fd(beta, w, h=None):
    h = h or w * 1e-6
    return 2 * h / (beta(w + h) - beta(w - h))


def beta_plasma(fp):
    wp = 2 * np.pi * fp
    return lambda w: np.sqrt(w ** 2 - wp ** 2) / c


def pulse_delay(beta, f0, L, sig, tmax, n=2 ** 14):
    # FFT-propagate a Gaussian envelope; peak time of output
    t = np.linspace(0, tmax, n, endpoint=False)
    t0 = tmax * 0.1
    m = np.exp(-((t - t0) / sig) ** 2 / 2)
    W = 2 * np.pi * np.fft.fftfreq(n, t[1] - t[0])
    w0 = 2 * np.pi * f0
    with np.errstate(invalid='ignore'):
        bW = beta(w0 + W)
    ok = np.isfinite(bW) & (np.abs(W) < 0.5 * w0)  # drop negligible tails
    Hf = np.zeros(n, complex)
    Hf[ok] = np.exp(-1j * bW[ok] * L)
    out = np.fft.ifft(np.fft.fft(m) * Hf)
    tt = np.linspace(0, tmax, 20 * n)
    env = np.abs(np.interp(tt, t, np.abs(out)))
    return tt[np.argmax(env)] - t0


print("=== 24.1 ===")
fp, f, L = 4e9, 5e9, 0.9
w = 2 * np.pi * f
b = beta_plasma(fp)
vp, vg = w / b(w), vg_fd(b, w)
chk("v_p", 5e8, vp); chk("v_g (FD dw/dbeta)", 1.8e8, vg); chk("v_p v_g", 9e16, vp * vg)
chk("pulse time L/v_g", 5e-9, L / vg); chk("vacuum time", 3e-9, L / c); chk("crest time", 1.8e-9, L / vp)
chk("pulse sim delay (FFT)", 5e-9, pulse_delay(b, f, L, 2e-9, 60e-9), rtol=1e-2)

print("=== 24.2 ===")
bd = lambda w: w * np.sqrt(4) / c
wa = 2 * np.pi * 1e9
print("(a) v_g, v_p dielectric:", vg_fd(bd, wa) / c, (wa / bd(wa)) / c, "-> crests not c/4: statement false")
chks("(a) false", True, not np.isclose(wa / bd(wa), c / 4))
u_, b0 = 2e8, 3.0
bl = lambda w: b0 + w / u_
vps = [w_ / bl(w_) for w_ in (1e9, 2e9)]
chks("(b) false: v_p varies on straight non-origin line", True, not np.isclose(*vps))
chk("(b) v_g = u", u_, vg_fd(bl, 1e9))
ws = 2 * np.pi * np.linspace(4.01e9, 40e9, 50)
pp = np.array([(w_ / b(w_), vg_fd(b, w_)) for w_ in ws])
chk("(c) v_p v_g = c^2 (all w)", np.full(50, c ** 2), pp[:, 0] * pp[:, 1])
chks("(c) true: never both < c", True, bool(np.all(pp.max(axis=1) > c)))
chks("(d) false: v_g < c always", True, bool(np.all(pp[:, 1] < c)))
dbdw = (b(w + 1) - b(w - 1)) / 2
chk("(e) dbeta/dw = 1/v_g (s/m)", 1 / vg, dbdw)

print("=== 24.3 ===")
w = 1.0; T = 2 * np.pi; bt = 1.0
fa = lambda r, t: 2 * np.sin(w * t - bt * r[2]) * X + 2 * np.cos(w * t - bt * r[2]) * Y
fb = lambda r, t: 3 * np.cos(w * t + bt * r[0]) * Y - 3 * np.sin(w * t + bt * r[0]) * Z
fc = lambda r, t: 2 * np.sin(w * t - bt * r[1]) * Z - 2 * np.sin(w * t - bt * r[1]) * X
fd = lambda r, t: 4 * np.cos(w * t - bt * r[2]) * X + 4 * np.cos(w * t - bt * r[2] - np.pi / 3) * Y
for lab, fn, pu, pp_ in (('a', fa, '+z', 'left circular'), ('b', fb, '-x', 'right circular'),
                         ('c', fc, '+y', 'linear'), ('d', fd, '+z', 'right elliptical')):
    u = travel(fn, 1.0, T)
    chks(f"({lab}) travel", pu, u)
    p = pol(fn, np.zeros(3), UV[u], T)
    chks(f"({lab}) polarization", pp_, p[0])
    if p[0] == 'linear':
        d = p[3] / np.linalg.norm(p[3]); print("    linear along", np.round(d, 4), "(page z - x)")
        chk("(c) direction || z-x", 0, np.linalg.norm(np.cross(d, Z - X)))
chk("(d) u.(E0 x E(T/4))", 8 * np.sqrt(3), Z @ np.cross(fd(np.zeros(3), 0), fd(np.zeros(3), T / 4)))
chk("(b) u.(E0 x E(T/4))", 9, -X @ np.cross(fb(np.zeros(3), 0), fb(np.zeros(3), T / 4)))
chk("(a) u.(E0 x E(T/4))", -4, Z @ np.cross(fa(np.zeros(3), 0), fa(np.zeros(3), T / 4)))

print("=== 24.4 ===")
def E44(B, ph):
    return lambda r: (6 * Y + B * np.exp(1j * ph) * Z) * np.exp(1j * bt * r[0])
def p44(B, ph):
    Er = real_field(E44(B, ph), w)
    return pol(Er, np.zeros(3), UV[travel(Er, 1.0, T)], T)[0]
chks("travel", '-x', travel(real_field(E44(3, 1), w), 1.0, T))
chks("(i) phi=pi linear all B", True, all(p44(B, np.pi) == 'linear' for B in (0.5, 3, 6, 10)))
chks("(ii) B=0 linear all phi", True, all(p44(0, ph) == 'linear' for ph in np.linspace(0, 6, 7)))
chks("(iii) (pi/2,6)", 'right circular', p44(6, np.pi / 2))
chks("(iv) (3pi/2,6) [page: F, left]", 'left circular', p44(6, 3 * np.pi / 2))
chks("(v) (pi/2,3) [page: F, right ell.]", 'right elliptical', p44(3, np.pi / 2))
chks("(vi) B=6 not always circular", True, any('circular' not in p44(6, ph) for ph in (0, np.pi / 4)))
print("    (vi) phi=0:", p44(6, 0), " phi=pi/4:", p44(6, np.pi / 4))
chks("watch out: +x travel swaps (iii)", 'left circular',
     pol(real_field(lambda r: (6 * Y + 6j * Z) * np.exp(-1j * r[0]), w), np.zeros(3), X, T)[0])

print("=== 24.5 ===")
w = 2 * np.pi * 1e8; T = 1 / 1e8; bt = w / c
E5 = lambda r: 5 * (X + 1j * Y) * np.exp(1j * bt * r[2])
Er = real_field(E5, w)
u = travel(Er, c, T); chks("travel", '-z', u)
chks("polarization", 'right circular', pol(Er, np.zeros(3), UV[u], T)[0])
H5 = H_from_E(E5, w, mu0)
r0 = np.array([0.1, 0.2, 0.37])
chk("H~ (curl) vs page 5(jx-y)e^{jbz}/eta0", 5 * (1j * X - Y) * np.exp(1j * bt * r0[2]) / eta0, H5(r0))
chk("student H~ = -correct", -H5(r0), 5 * (Y - 1j * X) * np.exp(1j * bt * r0[2]) / eta0)
chk("<S> (time avg)", -25 / eta0 * Z, S_avg(E5, H5, w)); chk("-25/eta0", -0.0663, -25 / eta0, rtol=1e-3)
chk("check: student <S> +z", 25 / eta0 * Z, S_avg(E5, lambda r: 5 * (Y - 1j * X) * np.exp(1j * bt * r[2]) / eta0, w))

print("=== 24.6 ===")
f = 50e6; w = 2 * np.pi * f; er = 4; v = c / np.sqrt(er); eta = eta0 / 2
bt = w / v; T = 1 / f
chk("T", 20e-9, T); chk("lambda", 3, v / f); chk("beta", 2 * np.pi / 3, bt); chk("eta", 60 * np.pi, eta)
E6 = lambda r: 3 * (Z - 1j * X) * np.exp(1j * 2 * np.pi / 3 * r[1])  # page
Er = real_field(E6, w)
chk("snapshot t=0", 3 * Z, Er(np.zeros(3), 0)); chk("snapshot T/4", 3 * X, Er(np.zeros(3), T / 4))
u = travel(Er, v, T); chks("travel", '-y', u)
chks("polarization", 'left circular', pol(Er, np.zeros(3), UV[u], T)[0])
E6t = lambda r, t: 3 * np.cos(w * t + 2 * np.pi / 3 * r[1]) * Z + 3 * np.sin(w * t + 2 * np.pi / 3 * r[1]) * X
rr = [np.array([0.3, 1.1, -.2]), 7e-9]
chk("time-domain E vs Re{E~ e^jwt}", Er(*rr), E6t(*rr))
H6 = H_from_E(E6, w, mu0)
r0 = np.array([0.2, 0.7, -0.4])
chk("H~ (curl)", -(X + 1j * Z) * np.exp(1j * 2 * np.pi / 3 * r0[1]) / (20 * np.pi), H6(r0))
chk("<S>", -3 / (20 * np.pi) * Y, S_avg(E6, H6, w)); chk("3/(20pi)", 0.0477, 3 / (20 * np.pi), rtol=1e-3)

print("=== 24.7 ===")
R, Lc = np.array([1, -1j]), np.array([1, 1j])
ab = np.linalg.solve(np.column_stack([R, Lc]), np.array([0, 4]))
chk("(a) a,b", [2j, -2j], ab)
w = 1.0; T = 2 * np.pi
for vec, nm in ((R, 'x-jy'), (Lc, 'x+jy')):
    Er = real_field(lambda r, vec=vec: np.array([vec[0], vec[1], 0]) * np.exp(-1j * r[2]), w)
    print(f"    basis {nm}: travel {travel(Er, 1.0, T)}, {pol(Er, np.zeros(3), Z, T)[0]}")
Pw = lambda Ev: np.sum(np.abs(Ev) ** 2) / (2 * eta0)  # one-direction plane wave
chk("(a) each part", 4 / eta0, Pw(ab[0] * R)); chk("(a) total", 8 / eta0, Pw(ab[0] * R) + Pw(ab[1] * Lc))
chk("(a) linear", 1 / (15 * np.pi), Pw(np.array([0, 4]))); chk("0.0212", 0.0212, 1 / (15 * np.pi), rtol=2e-3)
s = 3 * R + 1 * Lc; chk("(b) sum", [4, -2j], s)
Er = real_field(lambda r: np.array([s[0], s[1], 0]) * np.exp(-1j * r[2]), w)
p = pol(Er, np.zeros(3), Z, T)
chks("(b) polarization", 'right elliptical', p[0]); chk("(b) |E| max,min", [4, 2], [p[1], p[2]])
E7 = lambda r: np.array([s[0], s[1], 0]) * np.exp(-1j * 2 * np.pi * 1e8 / c * r[2])
H7 = H_from_E(E7, 2 * np.pi * 1e8, mu0)
chk("(c) <S> brute", 10 / eta0 * Z, S_avg(E7, H7, 2 * np.pi * 1e8))
chk("(c) circular parts", 10 / eta0, Pw(3 * R) + Pw(Lc)); chk("(c) 1/(12pi)", 0.0265, 1 / (12 * np.pi), rtol=2e-3)

print("=== 24.8 ===")
mur = 4; v = c / np.sqrt(mur); eta = eta0 * np.sqrt(mur); bt = 2 * np.pi; w = bt * v; f = w / (2 * np.pi); T = 1 / f
chk("v", 1.5e8, v); chk("eta", 240 * np.pi, eta); chk("f", 150e6, f)
Ht = lambda r, t: 0.1 * np.cos(w * t - bt * r[0]) * Y + 0.1 * np.sin(w * t - bt * r[0]) * Z
H8 = lambda r: 0.1 * (Y - 1j * Z) * np.exp(-1j * bt * r[0])  # page
rr = [np.array([0.3, 1.1, -.2]), 1.7e-9]
chk("H~ reproduces H(x,t)", Ht(*rr), real_field(H8, w)(*rr))
E8 = lambda r: curl(H8, r) / (1j * w * eps0)  # Ampere
r0 = np.array([0.37, 0.1, 0.2])
chk("E~ (Ampere) vs page", -24 * np.pi * (Z + 1j * Y) * np.exp(-1j * bt * r0[0]), E8(r0))
E8t = lambda r, t: 24 * np.pi * np.sin(w * t - bt * r[0]) * Y - 24 * np.pi * np.cos(w * t - bt * r[0]) * Z
Er = real_field(E8, w)
chk("E(x,t) page vs Re", Er(*rr), E8t(*rr), rtol=1e-4)
u = travel(Er, v, T); chks("travel", '+x', u)
chks("E polarization", 'right circular', pol(Er, np.zeros(3), UV[u], T)[0])
chks("H polarization", 'right circular', pol(Ht, np.zeros(3), UV[u], T)[0])
Sinst = np.array([np.cross(E8t(r0, t), Ht(r0, t)) for t in np.linspace(0, T, 37)])
chk("S(t) const = 2.4pi x", np.tile(2.4 * np.pi * X, (37, 1)), Sinst, rtol=1e-4, atol=1e-6)
chk("<S>", 2.4 * np.pi * X, S_avg(E8, H8, w)); chk("7.54", 7.54, 2.4 * np.pi)
chk("check E x H at 0,0", 2.4 * np.pi * X, np.cross(E8t(np.zeros(3), 0), Ht(np.zeros(3), 0)))

print("=== 24.9 ===")
f = 75e6; w = 2 * np.pi * f; T = 1 / f; bt = w / c
chk("lambda", 4, c / f); chk("beta", np.pi / 2, bt); chk("T", 13.33e-9, T)
found = []
for sgn in (1, -1):  # E(T/4) = sgn*6x; E~(0)=E(0)-jE(T/4)
    E0 = 6 * Y - 1j * sgn * 6 * X
    Ec = lambda r, E0=E0: E0 * np.exp(1j * bt * r[2])
    Er = real_field(Ec, w)
    u = travel(Er, c, T)
    if u == '-z' and pol(Er, np.zeros(3), Z * -1, T)[0] == 'right circular':
        found.append(E0)
chk("(b) A,B,C (brute force)", [-6j, 6, 0], found[0]); chks("unique", 1, len(found))
chk("(a) (a,b,c): exponent j(cz) with c=+beta", [0, 0, np.pi / 2], [0, 0, bt])
E9 = lambda r: found[0] * np.exp(1j * bt * r[2]); Er = real_field(E9, w)
E9t = lambda r, t: 6 * np.sin(w * t + np.pi / 2 * r[2]) * X + 6 * np.cos(w * t + np.pi / 2 * r[2]) * Y
rr = [np.array([0.3, 1.1, -.7]), 2.9e-9]
chk("E(z,t) page vs Re", Er(*rr), E9t(*rr))
H9 = H_from_E(E9, w, mu0); r0 = np.array([0.1, 0.2, 0.3])
chk("H~ (curl)", (X + 1j * Y) * np.exp(1j * np.pi / 2 * r0[2]) / (20 * np.pi), H9(r0))
chk("<S>", -3 / (10 * np.pi) * Z, S_avg(E9, H9, w)); chk("0.0955", 0.0955, 3 / (10 * np.pi), rtol=1e-3)
chk("one component", 3 / (20 * np.pi), 36 / (2 * eta0))
chk("(d) E(z=-1,0)", -6 * X, Er(np.array([0, 0, -1.]), 0)); chk("(d) E(z=+1,0)", 6 * X, Er(np.array([0, 0, 1.]), 0))
g = lambda t: np.linalg.norm(Er(np.array([0, 0, -1.]), t) - 6 * Y)
ts = np.linspace(0, T, 200001); tf = ts[np.argmin([g(t) for t in ts[::100]]) * 100]
chk("(d) first t>=0 probe reads 6y", 3.33e-9, tf, rtol=2e-3)
chk("check E x H at origin along -z", -6 / (20 * np.pi) * Z, np.cross(Er(np.zeros(3), 0), real_field(H9, w)(np.zeros(3), 0)))

print("=== 24.10 ===")
w = 2 * np.pi * 1e8; T = 1e-8; bt = w / c
def E10t(E1, E2, ph):
    return lambda r, t: E1 * np.cos(w * t + bt * r[0]) * Y + E2 * np.cos(w * t + bt * r[0] + ph) * Z
E10 = lambda E1, E2, ph: (lambda r: (E1 * Y + E2 * np.exp(1j * ph) * Z) * np.exp(1j * bt * r[0]))
rr = [np.array([0.3, 1.1, -.7]), 2.9e-9]
chk("E~ reproduces E(x,t)", E10t(4, 3, 1.1)(*rr), real_field(E10(4, 3, 1.1), w)(*rr))
chks("travel", '-x', travel(E10t(4, 3, 1.1), c, T))
r0 = np.array([0.4, 0.2, 0.3])
for (E1, E2, ph) in ((4, 3, 1.1), (2, 5, 4.0)):
    Hc = H_from_E(E10(E1, E2, ph), w, mu0)(r0)
    chk(f"(a) H~ page form {E1, E2, ph}", (E2 * np.exp(1j * ph) * Y - E1 * Z) * np.exp(1j * bt * r0[0]) / eta0, Hc)
Ss = [S_avg(E10(4, 3, ph), H_from_E(E10(4, 3, ph), w, mu0), w) for ph in np.linspace(0, 6, 5)]
chk("(b) <S> indep of phi", np.tile(-25 / (2 * eta0) * X, (5, 1)), Ss)
bad = 0
for E1, E2 in ((4, 3), (3, 3), (1, 5)):
    for ph in np.linspace(0, 2 * np.pi, 49)[:-1]:
        got = pol(E10t(E1, E2, ph), np.zeros(3), -X, T)[0]
        sp = np.sin(ph)
        if abs(sp) < 1e-9: exp = 'linear'
        else:
            hand = 'right' if sp > 0 else 'left'
            shape = 'circular' if (E1 == E2 and abs(abs(sp) - 1) < 1e-9) else 'elliptical'
            exp = f"{hand} {shape}"
        bad += got != exp
chks("(c) page rule vs rotation, 144 cases", 0, bad)
p = pol(E10t(4, 3, np.pi / 2), np.zeros(3), -X, T)
chks("(d) polarization", 'right elliptical', p[0]); chk("(d) |E| max,min", [4, 3], [p[1], p[2]])
Hd = H_from_E(E10(4, 3, np.pi / 2), w, mu0)
chk("(d) H~", (3j * Y - 4 * Z) * np.exp(1j * bt * r0[0]) / (120 * np.pi), Hd(r0))
chk("(d) <S>", -5 / (48 * np.pi) * X, S_avg(E10(4, 3, np.pi / 2), Hd, w)); chk("0.0332", 0.0332, 5 / (48 * np.pi), rtol=3e-3)

print("=== 24.11 ===")
f1, f2, t1, t2 = 15e6, 20e6, 1e-3, 0.75e-3
tau = lambda f, fp, L: L / vg_fd(beta_plasma(fp), 2 * np.pi * f)
fp = brentq(lambda fp: tau(f1, fp, 1) / tau(f2, fp, 1) - t1 / t2, 1e6, 14.9e6)
L = t1 * vg_fd(beta_plasma(fp), 2 * np.pi * f1)
chk("f_p", 12e6, fp); chk("L", 180e3, L); chk("tau2 consistency", t2, tau(f2, fp, L))
chk("s1,s2", [0.6, 0.8], [vg_fd(beta_plasma(fp), 2 * np.pi * f1) / c, vg_fd(beta_plasma(fp), 2 * np.pi * f2) / c])
me, e = 9.109e-31, 1.602e-19
N = (2 * np.pi * fp) ** 2 * me * eps0 / e ** 2
N2 = (2 * np.pi * fp) ** 2 * me * 8.854e-12 / e ** 2
chk("N", 1.79e12, N2, rtol=3e-3)
for ff, pg in ((f1, 0.36e-3), (f2, 0.48e-3)):
    wv = 2 * np.pi * ff
    chk(f"(c) crest time {ff/1e6:.0f} MHz", pg, L / (wv / beta_plasma(fp)(wv)))
chk("(c) vacuum", 0.6e-3, L / c)
ta, tb = tau(19.95e6, fp, L), tau(20.05e6, fp, L)
chk("(d) tau(19.95)", 0.75106e-3, ta, rtol=2e-6); chk("(d) tau(20.05)", 0.74895e-3, tb, rtol=2e-6)
chk("(d) spread", 2.1e-6, ta - tb, rtol=1e-2)
dtdf = (tau(20e6 + 1e3, fp, L) - tau(20e6 - 1e3, fp, L)) / 2e3
chk("(d) derivative formula", (L / c) * fp ** 2 / (f2 ** 3 * 0.8 ** 3), -dtdf, rtol=1e-4)
chk("(d) fp^2/f^3", 1.8e-8, fp ** 2 / f2 ** 3)
print(f"    feature 1/df = {1/1e5*1e6:.0f} us; spread/feature = {(ta-tb)/1e-5:.2f}")
d1 = pulse_delay(beta_plasma(fp), f1, L, 20e-6, 2e-3); d2 = pulse_delay(beta_plasma(fp), f2, L, 20e-6, 2e-3)
chk("pulse sim delays", [1e-3, 0.75e-3], [d1, d2], rtol=5e-3)
chks("(e) 10 MHz below f_p: beta^2<0", True, (2 * np.pi * 10e6) ** 2 - (2 * np.pi * fp) ** 2 < 0)
chk("check vp*vg", [9e16, 9e16], [5e8 * 1.8e8, 3.75e8 * 2.4e8])

print("=== 24.12 ===")
f = 150e6; w = 2 * np.pi * f; T = 1 / f; bt = w / c
chk("beta", np.pi, bt)
Js = lambda t: 0.2 * np.cos(w * t) * Y - 0.1 * np.sin(w * t) * Z
Jph = 0.2 * Y + 0.1j * Z
chk("J~ reproduces J(t)", Js(1.3e-9), np.real(Jph * np.exp(1j * w * 1.3e-9)))
Esheet = lambda r, t: -eta0 / 2 * Js(t - abs(r[0]) / c)  # Lecture 19 time domain
E12 = lambda r: -(12 * np.pi * Y + 6j * np.pi * Z) * np.exp(-1j * np.pi * abs(r[0]))  # page
for xs in (0.37, -0.81):
    rr = [np.array([xs, .2, .1]), 2.3e-9]
    chk(f"E page vs sheet formula x={xs}", Esheet(*rr), real_field(E12, w)(*rr))
for sg, xs in ((1, 0.37), (-1, -0.81)):
    r0 = np.array([xs, .2, .1])
    Hc = H_from_E(E12, w, mu0)(r0)
    chk(f"H~ (curl) x={xs}", sg * (0.05j * Y - 0.1 * Z) * np.exp(-1j * np.pi * abs(xs)), Hc)
    Hp = lambda r, sg=sg: sg * (0.05j * Y - 0.1 * Z) * np.exp(-1j * np.pi * abs(r[0]))
    chk(f"<S> x={xs}", sg * 0.75 * np.pi * X, S_avg(E12, Hp, w, r0=r0))
    side = lambda r, t, sg=sg: -eta0 / 2 * Js(t - sg * r[0] / c)  # valid on side sg
    chks(f"travel x={xs}", '+x' if sg > 0 else '-x', travel(side, c, T))
    p = pol(Esheet, np.array([sg * 1e-9, 0, 0]), sg * X, T)
    chks(f"polarization x={xs}", 'left elliptical' if sg > 0 else 'right elliptical', p[0])
    if sg > 0: chk("semi-axes", [12 * np.pi, 6 * np.pi], [p[1], p[2]])
Hjump = np.cross(X, (0.05j * Y - 0.1 * Z) - (-(0.05j * Y - 0.1 * Z)))
chk("n x (H1-H2) = J_s", Jph, Hjump)
chk("1/2 J x n", 0.05j * Y - 0.1 * Z, 0.5 * np.cross(Jph, X))
ts = np.arange(720) * T / 720
Psup = np.mean([-Js(t) @ Esheet(np.zeros(3), t) for t in ts])
chk("supplied <-J.E>", 1.5 * np.pi, Psup); chk("4.71", 4.71, 1.5 * np.pi, rtol=1e-3); chk("2.36", 2.36, 0.75 * np.pi, rtol=3e-3)
ab = np.linalg.solve(np.column_stack([[1, -1j], [1, 1j]]), np.array([-12 * np.pi, -6j * np.pi]))
chk("(d) a,b", [-3 * np.pi, -9 * np.pi], ab)
for vec, nm in (([1, -1j], 'y-jz'), ([1, 1j], 'y+jz')):
    Er = real_field(lambda r, vec=vec: (vec[0] * Y + vec[1] * Z) * np.exp(-1j * r[0]), 1.0)
    print(f"    {nm}, +x travel: {pol(Er, np.zeros(3), X, 2 * np.pi)[0]}")
chk("(d) powers", [0.075 * np.pi, 0.675 * np.pi], [2 * abs(ab[0]) ** 2 / (2 * eta0), 2 * abs(ab[1]) ** 2 / (2 * eta0)])

Jeq = lambda t: 0.2 * np.cos(w * t) * Y - 0.2 * np.sin(w * t) * Z  # equal amplitudes
Eeq = lambda r, t: -eta0 / 2 * Jeq(t - abs(r[0]) / c)
chks("check: equal amps, x>0", 'left circular', pol(Eeq, np.array([1e-9, 0, 0]), X, T)[0])
chks("check: equal amps, x<0", 'right circular', pol(Eeq, np.array([-1e-9, 0, 0]), -X, T)[0])

print(f"\n{NF} FAIL(s)")
