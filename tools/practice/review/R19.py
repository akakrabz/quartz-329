#!/usr/bin/env python3
"""R19 -- independent reviewer check of content-src/practice/19-radiation-from-current-sheets.md
plus (section W) an independent re-solve of content-src/problems/a-current-sheet-launches-two-waves.md.

Method: a generic sheet-radiator built from the GIVEN data only,
    E = -(eta/2) J_s(t - d/v),   H = 1/2 J_s(t - d/v) x n_hat   (n_hat from the sheet toward the point),
with np.cross for every direction.  For every (E, H) pair: (i) the page's own written formula is
transcribed separately and compared with the recipe at random points; (ii) Faraday
(curl E = -mu dH/dt), Ampere-Maxwell (curl H = eps dE/dt), div E = div H = 0 by central
differences; (iii) the jump conditions n x (H1 - H2) = J_s, n x (E1 - E2) = 0 at the sheet.
Units: SI, c = 3e8 m/s, eta0 = 120*pi (so mu0 = 4e-7*pi and eps0 = 1/(mu0 c^2)), as the page uses.
numpy/scipy only.
"""
import numpy as np

c = 3e8
mu0 = 4e-7*np.pi
eps0 = 1/(mu0*c**2)
eta0 = mu0*c                      # = 120 pi exactly
e_ch = 1.602176634e-19
X, Y, Z = np.eye(3)
rng = np.random.default_rng(19)
NF = [0, 0]
ns, us = 1e-9, 1e-6


def fmt(a):
    a = np.atleast_1d(np.asarray(a, float))
    return f"{a[0]:.5g}" if a.size == 1 else "[" + ", ".join(f"{x:.5g}" for x in a.ravel()) + "]"


def report(ok, msg):
    NF[1] += 1
    NF[0] += (not ok)
    print(f"  {'PASS' if ok else 'FAIL'}  {msg}")


def chk(name, got, page, rtol=3e-3, atol=1e-9):
    g = np.atleast_1d(np.asarray(got, float))
    p = np.atleast_1d(np.asarray(page, float))
    ok = g.shape == p.shape and np.allclose(g, p, rtol=rtol, atol=atol)
    report(ok, f"{name}: computed {fmt(g)}, page {fmt(p)}")


def unit(v):
    v = np.asarray(v, float)
    return v/np.linalg.norm(v)


# ---------------- piecewise-linear waveform from breakpoints (allows jumps) ----------------
def pwl(pts):
    """pts: list of (t, value) in order; a repeated t means a jump (value right after = second)."""
    def g(t):
        t = float(t)
        if t < pts[0][0] or t > pts[-1][0]:
            return 0.0
        for (t1, v1), (t2, v2) in zip(pts[:-1], pts[1:]):
            if t1 <= t < t2:
                return v1 + (v2 - v1)*(t - t1)/(t2 - t1)
        return pts[-1][1]
    return g


# ---------------- generic sheet ----------------
class Sheet:
    def __init__(self, n, r0, Jdir, g, epsr=1.0, mur=1.0):
        self.n = unit(n); self.r0 = np.asarray(r0, float); self.Jdir = np.asarray(Jdir, float)
        self.g = g; self.mu = mur*mu0; self.eps = epsr*eps0
        self.v = 1/np.sqrt(self.mu*self.eps); self.eta = np.sqrt(self.mu/self.eps)

    def side(self, r):
        s = np.dot(self.n, np.asarray(r, float) - self.r0)
        return np.sign(s), abs(s)

    def J(self, t):
        return self.Jdir*self.g(t)

    def E(self, r, t):
        s, d = self.side(r)
        return -self.eta/2*self.J(t - d/self.v)

    def H(self, r, t):
        s, d = self.side(r)
        return 0.5*np.cross(self.J(t - d/self.v), s*self.n)


def jac(F, r, t, h):
    M = np.empty((3, 3))
    for j in range(3):
        e = np.zeros(3); e[j] = h
        M[:, j] = (F(r + e, t) - F(r - e, t))/(2*h)
    return M


def curl(M):
    return np.array([M[2, 1] - M[1, 2], M[0, 2] - M[2, 0], M[1, 0] - M[0, 1]])


def maxwell_fd(name, E, H, mu, eps, pts, scaleE, h=1e-4):
    """FD residuals of Faraday and Ampere-Maxwell, relative to the size of each term."""
    worst = 0.0
    k = h*np.sqrt(mu*eps)
    for r, t in pts:
        r = np.asarray(r, float)
        cE = curl(jac(E, r, t, h)); cH = curl(jac(H, r, t, h))
        dH = (H(r, t + k) - H(r, t - k))/(2*k); dE = (E(r, t + k) - E(r, t - k))/(2*k)
        JE = jac(E, r, t, h); JH = jac(H, r, t, h)
        ref1 = max(np.linalg.norm(cE), np.linalg.norm(mu*dH), 1e-30)
        ref2 = max(np.linalg.norm(cH), np.linalg.norm(eps*dE), 1e-30)
        worst = max(worst, np.linalg.norm(cE + mu*dH)/ref1, np.linalg.norm(cH - eps*dE)/ref2,
                    abs(np.trace(JE))/max(np.linalg.norm(JE), 1e-30), abs(np.trace(JH))/max(np.linalg.norm(JH), 1e-30))
    report(worst < 2e-3, f"{name}: Faraday / Ampere-Maxwell / div by FD, worst relative residual {worst:.1e}")
    return worst


def bc_check(name, sh, rs_on_sheet, ts, eps_=1e-7):
    worst = 0.0
    for r0 in rs_on_sheet:
        for t in ts:
            r1 = np.asarray(r0) + eps_*sh.n; r2 = np.asarray(r0) - eps_*sh.n
            jump = np.cross(sh.n, sh.H(r1, t) - sh.H(r2, t)) - sh.J(t)
            ejump = np.cross(sh.n, sh.E(r1, t) - sh.E(r2, t))
            sc = max(np.linalg.norm(sh.J(t)), 1e-12)
            worst = max(worst, np.linalg.norm(jump)/sc, np.linalg.norm(ejump)/(sh.eta*sc))
    report(worst < 1e-5, f"{name}: n x (H1-H2) = J_s and n x (E1-E2) = 0 at the sheet, worst {worst:.1e}")


def gauss(t0, w):
    return lambda t: np.exp(-((t - t0)/w)**2)


def agree(name, F_page, F_rec, pts, scale):
    worst = max(np.linalg.norm(F_page(r, t) - F_rec(r, t)) for r, t in pts)/scale
    report(worst < 1e-9, f"{name}: page formula = recipe at {len(pts)} random points (max dev {worst:.1e})")


def rand_pts(n, box, tspan, avoid=None):
    out = []
    while len(out) < n:
        r = rng.uniform(-box, box, 3)
        if avoid is not None and abs(avoid(r)) < 0.02*box:
            continue
        out.append((r, rng.uniform(*tspan)))
    return out


# ======================================================================================
print("19.1 Which one is a plane wave")
f = gauss(5*ns, 1*ns)
cands = {
    'a': (lambda r, t: Z*f(t - r[2]/c), lambda r, t: X*f(t - r[2]/c)/eta0),
    'b': (lambda r, t: Y*f(t - r[2]/c), lambda r, t: X*f(t - r[2]/c)/eta0),
    'c': (lambda r, t: Z*f(t + r[0]/c), lambda r, t: Y*f(t + r[0]/c)/eta0),
    'd': (lambda r, t: X*np.exp(-r[1]**2)*f(t - r[2]/c), lambda r, t: Y*np.exp(-r[1]**2)*f(t - r[2]/c)/eta0),
    'e': (lambda r, t: X*f(t - r[2]/c), lambda r, t: Y*f(t - r[2]/c)/(2*eta0)),
}
res = {}
for key, (E, H) in cands.items():
    w = 0.0
    for _ in range(20):
        r = rng.uniform(-0.5, 0.5, 3); t = rng.uniform(4*ns, 6*ns); h = 1e-4; k = h/c
        cE = curl(jac(E, r, t, h)); cH = curl(jac(H, r, t, h))
        dH = (H(r, t + k) - H(r, t - k))/(2*k); dE = (E(r, t + k) - E(r, t - k))/(2*k)
        dv = np.trace(jac(E, r, t, h))
        sc = np.linalg.norm(mu0*dH) + np.linalg.norm(cE) + 1e-30
        w = max(w, np.linalg.norm(cE + mu0*dH)/sc, np.linalg.norm(cH - eps0*dE)/(np.linalg.norm(cH) + np.linalg.norm(eps0*dE) + 1e-30),
                abs(dv)/(np.linalg.norm(dE)/c + 1e-30))
    res[key] = w < 1e-3
    print(f"    ({key}) Maxwell-consistent: {res[key]}  (worst residual {w:.2e})")
report([k for k, v in res.items() if v] == ['c'], "only (c) satisfies Maxwell's equations -> key (c)")
report(np.allclose(np.cross(-X, Z), Y), "(c) H = u x E/eta0 with u = -x: (-x) x z = +y")
report(np.allclose(np.cross(Z, Y), -X), "(c) E x H || z x y = -x (travel toward -x)")
report(np.allclose(np.cross(Y, X), -Z), "(b) E x H || y x x = -z, wrong for t - z/c; partner of y f is z x y = -x")
report(np.allclose(np.cross(Z, Y), -X), "(b) partner check: H = z x (y)/eta0 = -x/eta0")

# ======================================================================================
print("\n19.2 A sheet on y = 0, J = z g(t)")
g2s = gauss(2*us, 0.3*us)
sh = Sheet(Y, [0, 0, 0], Z, g2s)
pts = rand_pts(30, 500, (0, 4*us), avoid=lambda r: r[1])
agree("H = -/+ 1/2 g(t -/+ y/c) x", lambda r, t: (-0.5*g2s(t - r[1]/c)*X if r[1] > 0 else 0.5*g2s(t + r[1]/c)*X), sh.H, pts, 0.5)
agree("E = -(eta0/2) g(t-|y|/c) z", lambda r, t: -eta0/2*g2s(t - abs(r[1])/c)*Z, sh.E, pts, eta0/2)
maxwell_fd("19.2 fields", sh.E, sh.H, mu0, eps0, pts[:12], eta0/2, h=0.5)
bc_check("19.2", sh, [rng.uniform(-5, 5, 3)*np.array([1, 0, 1]) for _ in range(4)], [1.7*us, 2.1*us])
sh = Sheet(Y, [0, 0, 0], Z, pwl([(0, 0.5), (2*us, 0.5)]))
chk("E at y=150 m, t=1 us (z)", sh.E([0, 150, 0], 1*us)[2], -94.2)
chk("H at y=150 m, t=1 us (x)", sh.H([0, 150, 0], 1*us)[0], -0.25)
chk("-30 pi", -30*np.pi, -94.2)
chk("E,H at y=-450 m, t=1 us", np.r_[sh.E([0, -450, 0], 1*us), sh.H([0, -450, 0], 1*us)], np.zeros(6))
chk("arrival at y=-450 m (us)", 450/c/us, 1.5)
report(np.allclose(np.cross(-Z, -X), Y) and np.allclose(np.cross(-Z, X), -Y), "E x H: (-z)x(-x)=+y above, (-z)x(x)=-y below")

# ======================================================================================
print("\n19.3 True/false, sheet z = 0, J = x J(t)")
g3 = gauss(1*us, 0.2*us)
sh = Sheet(Z, [0, 0, 0], X, g3)
tt = 1*us
report(np.allclose(sh.E([0, 0, 1e-6], tt), sh.E([0, 0, -1e-6], tt)), "(a) T: E continuous")
chk("(b) F: H above, below (y comps, per A/m)", [sh.H([0, 0, 1e-6], tt)[1]/g3(tt), sh.H([0, 0, -1e-6], tt)[1]/g3(tt)], [-0.5, 0.5])
chk("(c) F: |E| at 300 m (later by 300/c) equals |E| at 3 m", [np.linalg.norm(sh.E([0, 0, 300], tt + 300/c)), 300/c/us],
    [np.linalg.norm(sh.E([0, 0, 0], tt)), 1.0])
chk("(d) T: J.E at sheet per (A/m)^2", np.dot(X, sh.E([0, 0, 1e-9], tt))/g3(tt), -188.4, rtol=1e-3)
sh4 = Sheet(Z, [0, 0, 0], X, g3, epsr=4)
chk("(e) T: |E| per A/m in eps_r=4, |H| per A/m", [abs(sh4.E([0, 0, 0], tt)[0])/g3(tt), abs(sh4.H([0, 0, 1e-6], tt)[1])/g3(tt)], [94.2, 0.5])
S = np.cross(sh.E([0, 0, -1], tt + 1/c), sh.H([0, 0, -1], tt + 1/c))
report(S[2] < 0, f"(f) F: below the sheet E x H = {fmt(S)} points along -z")

# ======================================================================================
print("\n19.4 Reading a wave's parameters")
w4, b4 = 6*np.pi*1e8, 4*np.pi
vp = w4/b4
chk("omega, f, beta, lambda, vp", [w4, w4/2/np.pi, b4, 2*np.pi/b4, vp], [1.885e9, 3e8, 12.57, 0.5, 1.5e8])
er = (c/vp)**2
chk("eps_r", er, 4)
eta4 = eta0/np.sqrt(er)
chk("eta = mu0 vp", [eta4, mu0*vp], [188.5, 188.5])
H4 = lambda r, t: 0.05*np.cos(w4*t - b4*r[2])*X
E4p = lambda r, t: -3*np.pi*np.cos(w4*t - b4*r[2])*Y
E4 = lambda r, t: eta4*np.cross(H4(r, t), Z)
pts = rand_pts(15, 1, (0, 1e-8))
agree("E = eta H x u (page: -3 pi cos y)", E4p, E4, pts, 9.42)
chk("E amplitude", 3*np.pi, 9.42)
maxwell_fd("19.4 fields", E4p, H4, mu0, 4*eps0, pts, 9.42, h=1e-4)

# ======================================================================================
print("\n19.5 Find the error, sheet x = 0, J = -y g")
g5 = gauss(3*ns, 0.5*ns)
sh = Sheet(X, [0, 0, 0], -Y, g5)
pts = rand_pts(30, 1.5, (0, 8*ns), avoid=lambda r: r[0])
agree("H = +/- 1/2 g(t -/+ x/c) z", lambda r, t: (0.5*g5(t - r[0]/c)*Z if r[0] > 0 else -0.5*g5(t + r[0]/c)*Z), sh.H, pts, 0.5)
agree("E = +(eta0/2) g(t-|x|/c) y", lambda r, t: eta0/2*g5(t - abs(r[0])/c)*Y, sh.E, pts, eta0/2)
maxwell_fd("19.5 corrected fields", sh.E, sh.H, mu0, eps0, pts[:12], eta0/2)
bc_check("19.5", sh, [np.array([0, 1, 2]), np.array([0, -3, 0.5])], [2.6*ns, 3.3*ns])
# student's work
Hs = 0.5*np.cross(-Y, X)
Es_p = eta0*np.cross(Hs, X); Es_m = eta0*np.cross(Hs, -X)
chk("student H (z), E(x>0) (y), E(x<0) (y) per g", [Hs[2], Es_p[1]/eta0, Es_m[1]/eta0], [0.5, 0.5, -0.5])
chk("student E jump (units eta0 g)", (Es_p - Es_m)[1]/eta0, 1.0)
report(np.allclose(np.cross(X, Z), -Y) and np.allclose(np.cross(Y, -Z), -X), "jump x x (g z) = -g y = J_s; x<0: y x (-z) = -x")

# ======================================================================================
print("\n19.6 Triangle pulse in eps_r = 9 (REVISED geometry: sheet y = 0, J = -z g; was x = 0, +z = the worked problem's)")
g6 = pwl([(0, 0), (1*ns, 3), (4*ns, 0)])
sh = Sheet(Y, [0, 0, 0], -Z, g6, epsr=9)
P = lambda yv: [0, yv, 0]
chk("v (m/ns), eta, eta/2 / pi", [sh.v*ns, sh.eta, sh.eta/2/np.pi], [0.1, 125.7, 20])
pts = rand_pts(30, 1, (0, 10*ns), avoid=lambda r: r[1])
agree("H = +/- 1/2 g(t-|y|/v) x (y >< 0)", lambda r, t: np.sign(r[1])*0.5*g6(t - abs(r[1])/sh.v)*X, sh.H, pts, 1)
agree("E = +20 pi g(t-|y|/v) z", lambda r, t: 20*np.pi*g6(t - abs(r[1])/sh.v)*Z, sh.E, pts, 200)
report(np.allclose(np.cross(-Z, Y), X) and np.allclose(np.cross(-Z, -Y), -X), "(-z) x y = +x, (-z) x (-y) = -x")
chk("peak E_z, |H_x|", [sh.E(P(0.01), 1.1*ns)[2], sh.H(P(0.01), 1.1*ns)[0]], [188.5, 1.5])
tgrid = np.linspace(0, 12*ns, 120001)
for yp, page in ((0.5, (5, 6, 9, 188.5, 1.5)), (-0.3, (3, 4, 7, 188.5, -1.5))):
    Ez = np.array([sh.E(P(yp), t)[2] for t in tgrid]); Hx = np.array([sh.H(P(yp), t)[0] for t in tgrid])
    nz = np.nonzero(np.abs(Ez) > 1e-9)[0]
    ip = np.argmax(Ez)
    chk(f"record y={yp}: start, peak, end (ns), peak Ez, Hx", [tgrid[nz[0]]/ns, tgrid[ip]/ns, tgrid[nz[-1]]/ns, Ez[ip], Hx[ip]], page, rtol=3e-3, atol=2e-3)
chk("y=0.5 at 5.5 ns: Ez, Hx", [sh.E(P(0.5), 5.5*ns)[2], sh.H(P(0.5), 5.5*ns)[0]], [94.2, 0.75])
yg = np.linspace(-0.8, 0.8, 16001)
Hx6 = np.array([sh.H(P(yv), 6*ns)[0] for yv in yg])
pos = yg > 0; nz = yg[pos][np.abs(Hx6[pos]) > 1e-9]
chk("snapshot 6 ns y>0: inner edge, peak position, outer edge (m)", [nz[0], yg[pos][np.argmax(Hx6[pos])], nz[-1]], [0.2, 0.5, 0.6], atol=2e-4)
chk("snapshot: Hx at y=0.5 and -0.5, Ez at +/-0.5", [sh.H(P(0.5), 6*ns)[0], sh.H(P(-0.5), 6*ns)[0], sh.E(P(0.5), 6*ns)[2], sh.E(P(-0.5), 6*ns)[2]], [1.5, -1.5, 188.5, 188.5])
chk("spot y=0.3: Hx, Ez", [sh.H(P(0.3), 6*ns)[0], sh.E(P(0.3), 6*ns)[2]], [0.5, 62.8])
chk("spot y=-0.55: Hx, Ez", [sh.H(P(-0.55), 6*ns)[0], sh.E(P(-0.55), 6*ns)[2]], [-0.75, 94.2])
report(abs(1.5/0.1) > abs(1.5/0.3), "steep edge (slope 15 A/m per m) is the outer one (0.5-0.6 m); inner slope 5")
S6p = np.cross(sh.E(P(0.3), 6*ns), sh.H(P(0.3), 6*ns)); S6m = np.cross(sh.E(P(-0.3), 6*ns), sh.H(P(-0.3), 6*ns))
report(S6p[1] > 0 and S6m[1] < 0, f"E x H away from the sheet: {fmt(S6p)} at y=+0.3, {fmt(S6m)} at y=-0.3")
chk("jump y x (H+ - H-) at 2 ns (z)", np.cross(Y, sh.H(P(1e-9), 2*ns) - sh.H(P(-1e-9), 2*ns))[2], -g6(2*ns))
chk("vacuum arrival at 0.5 m (ns)", 0.5/c/ns, 1.667)
sm = Sheet(Y, [0, 0, 0], -Z, gauss(3*ns, 0.5*ns), epsr=9)
maxwell_fd("19.6 fields", sm.E, sm.H, sm.mu, sm.eps, rand_pts(12, 0.5, (2*ns, 8*ns), avoid=lambda r: r[1]), sm.eta/2)
bc_check("19.6", sh, [np.array([0.2, 0, 0.3])], [0.5*ns, 2*ns])
# worked-problem duplication check: worked problem = x = 0, +z, eps_r = 4 -> H_fwd = +1/2 y
report(not (np.allclose(sh.n, X) and np.allclose(sh.Jdir, Z)), "19.6 geometry now differs from the worked problem (x = 0, +z)")

# ======================================================================================
print("\n19.7 Which current made this field (inverse problem)")
# measured E(t) at z = -600 m
Epr = lambda t: (30*np.pi if 2.5*us < t < 4*us else 0.0)
delay = 600/c
Jrec = lambda t: -2/eta0*Epr(t + delay)*Y
chk("delay (us)", delay/us, 2)
chk("J_s y-amplitude, start, end", [Jrec(1*us)[1], 2.5 - delay/us, 4 - delay/us], [-0.5, 0.5, 2.0])
sh = Sheet(Z, [0, 0, 0], -Y, pwl([(0.5*us, 0.5), (2*us, 0.5)]))
tg = np.linspace(0, 6*us, 6001)
rec = np.array([sh.E([0, 0, -600], t)[1] for t in tg])
expect = np.array([Epr(t) for t in tg])
report(np.max(np.abs(rec - expect)[(np.abs(tg - 2.5*us) > 2e-9) & (np.abs(tg - 4*us) > 2e-9)]) < 1e-9,
       "forward model with J_s = -0.5 y (0.5-2 us) reproduces the probe record")
Hp = sh.H([0, 0, -600], 3*us); Ep = sh.E([0, 0, -600], 3*us); Sp = np.cross(Ep, Hp)
chk("H at probe (x), S (z)", [Hp[0], Sp[2]], [0.25, -23.6])
chk("eta0 J^2/4", eta0*0.25/4, 23.6)
zg = np.linspace(-1000, 1000, 200001)
Ey3 = np.array([sh.E([0, 0, z], 3*us)[1] for z in zg])
nzp = zg[(zg > 0) & (np.abs(Ey3) > 1e-9)]
chk("snapshot 3 us: z extent above (m)", [nzp[0], nzp[-1]], [300, 750], atol=0.02)
chk("at 3 us: E_y(500), H_x(500), E_y(-500), H_x(-500)",
    [sh.E([0, 0, 500], 3*us)[1], sh.H([0, 0, 500], 3*us)[0], sh.E([0, 0, -500], 3*us)[1], sh.H([0, 0, -500], 3*us)[0]], [94.2, -0.25, 94.2, 0.25])
bc_check("19.7", sh, [np.array([1, 2, 0])], [1*us, 1.5*us])
sm = Sheet(Z, [0, 0, 0], -Y, gauss(1*us, 0.2*us))
maxwell_fd("19.7 fields", sm.E, sm.H, mu0, eps0, rand_pts(12, 800, (0, 4*us), avoid=lambda r: r[2]), eta0/2, h=0.3)

# ======================================================================================
print("\n19.8 Cosine current in eps_r = 2.25")
w8 = 2*np.pi*50e6
sh = Sheet(Y, [0, 0, 0], X, lambda t: 0.4*np.cos(w8*t), epsr=2.25)
b8 = w8/sh.v
chk("v, eta, omega, beta, lambda", [sh.v, sh.eta, w8, b8, 2*np.pi/b8], [2e8, 251.3, np.pi*1e8, 1.571, 4])
pts = rand_pts(20, 5, (0, 40*ns), avoid=lambda r: r[1])
agree("E = -50.3 cos(wt - b|y|) x (exact 16 pi)", lambda r, t: -16*np.pi*np.cos(w8*t - b8*abs(r[1]))*X, sh.E, pts, 50)
agree("H = +/-0.2 cos(wt - b|y|) z", lambda r, t: np.sign(r[1])*0.2*np.cos(w8*t - b8*abs(r[1]))*Z, sh.H, pts, 0.2)
chk("16 pi", 16*np.pi, 50.3)
maxwell_fd("19.8 fields", sh.E, sh.H, sh.mu, sh.eps, pts[:12], 50)
bc_check("19.8", sh, [np.array([0.3, 0, 1])], [1*ns, 7*ns])
S8 = lambda r, t: np.cross(sh.E(r, t), sh.H(r, t))
Smax = max(S8([0, 1, 0], t)[1] for t in np.linspace(0, 20*ns, 4001))
Smin_dn = min(S8([0, -1, 0], t)[1] for t in np.linspace(0, 20*ns, 4001))
chk("S peak above, below; 3.2 pi", [Smax, Smin_dn, 3.2*np.pi], [10.05, -10.05, 10.05])
ts = np.linspace(0, 40*ns, 40001); Sy = np.array([S8([0, 1, 0], t)[1] for t in ts])
report(Sy.min() >= -1e-12, "S_y above never negative")
spec = np.abs(np.fft.rfft(Sy - Sy.mean())); fr = np.fft.rfftfreq(len(ts), ts[1] - ts[0])
chk("S oscillation frequency (MHz)", fr[np.argmax(spec)]/1e6, 100, rtol=0.03)
pk = max(-np.dot(sh.J(t), sh.E([0, 1e-9, 0], t)) for t in np.linspace(0, 20*ns, 4001))
chk("peak -J.E at sheet", pk, 20.1)
chk("omega t at 5 ns", w8*5*ns, np.pi/2)
for yp, pE, pH, pS in ((1, -50.3, 0.2, 10.05), (-3, 50.3, 0.2, -10.05)):
    chk(f"t=5 ns, y={yp}: Ex, Hz, Sy", [sh.E([0, yp, 0], 5*ns)[0], sh.H([0, yp, 0], 5*ns)[2], S8([0, yp, 0], 5*ns)[1]], [pE, pH, pS])
yy = np.linspace(1e-6, 7, 700001); Ex = np.array([sh.E([0, y, 0], 5*ns)[0] for y in yy[::100]])
zc = yy[::100][1:][np.diff(np.sign(Ex)) != 0]
chk("zeros of E on y>0 at 5 ns (m), first two beyond 0", zc[:3], [2, 4, 6], atol=2e-3)

# ======================================================================================
print("\n19.9 Step and ramp (SP18 Exam 2 #5 style)")
g9 = pwl([(0, 2), (1*ns, 2), (1*ns, -4), (3*ns, 0)])
sh = Sheet(Z, [0, 0, 0], -Y, g9)
pts = rand_pts(30, 1.5, (0, 6*ns), avoid=lambda r: r[2])
agree("H = -1/2 g(t - z/c) x (z>0), +1/2 g(t + z/c) x (z<0)",
      lambda r, t: (-0.5*g9(t - r[2]/c)*X if r[2] > 0 else 0.5*g9(t + r[2]/c)*X), sh.H, pts, 1)
agree("E = +60 pi g(t-|z|/c) y", lambda r, t: 60*np.pi*g9(t - abs(r[2])/c)*Y, sh.E, pts, 300)
sm = Sheet(Z, [0, 0, 0], -Y, gauss(2*ns, 0.4*ns))
maxwell_fd("19.9 fields", sm.E, sm.H, mu0, eps0, rand_pts(12, 1, (0, 6*ns), avoid=lambda r: r[2]), eta0/2)
bc_check("19.9", sh, [np.array([0.4, -1, 0])], [0.5*ns, 2*ns])
report(np.allclose(np.cross(Y, -X), Z) and np.allclose(np.cross(Y, X), -Z), "E x H: y x (-x) = +z above, y x x = -z below")
Hx = lambda z: sh.H([0, 0, z], 4*ns)[0]; Ey = lambda z: sh.E([0, 0, z], 4*ns)[1]
d = 1e-6
chk("landmarks at 4 ns: |z| for t'=0,1,3 ns", [0.3*4, 0.3*3, 0.3*1], [1.2, 0.9, 0.3])
chk("Hx: z=0.2, 0.3+, 0.9-, 0.9+, 1.05, 1.3",
    [Hx(0.2), Hx(0.3 + d), Hx(0.9 - d), Hx(0.9 + d), Hx(1.05), Hx(1.3)], [0, 0, 2, -1, -1, 0], atol=1e-4)
chk("Hx: z=-0.2, -0.9+, -0.9-, -1.05, -1.3",
    [Hx(-0.2), Hx(-0.9 + d), Hx(-0.9 - d), Hx(-1.05), Hx(-1.3)], [0, -2, 1, 1, 0], atol=1e-4)
chk("Ey: |z|=0.9-, 1.05 (both sides), -240pi, 120pi",
    [Ey(0.9 - d), Ey(-0.9 + d), Ey(1.05), Ey(-1.05), -240*np.pi, 120*np.pi], [-754, -754, 377, 377, -754, 377], atol=0.05)
chk("spot z=0.6: g, Hx, Ey", [g9(4*ns - 0.6/c), Hx(0.6), Ey(0.6)], [-2, 1, -377])
tg = np.linspace(0, 8*ns, 80001); rec = np.array([sh.H([0, 0, -0.9], t)[0] for t in tg])
chk("probe z=-0.9: Hx at 2.9, 3.5, 4.0+, 5, 6.1 ns", [sh.H([0, 0, -0.9], t*ns)[0] for t in (2.9, 3.5, 4.0001, 5, 6.1)], [0, 1, -2, -1, 0], atol=1e-3)
nz = tg[np.abs(rec) > 1e-9]
chk("probe record start, end (ns)", [nz[0]/ns, nz[-1]/ns], [3, 6], atol=2e-3)
S06 = np.cross(sh.E([0, 0, 0.6], 4*ns), sh.H([0, 0, 0.6], 4*ns)); S10 = np.cross(sh.E([0, 0, -1.0], 4*ns), sh.H([0, 0, -1.0], 4*ns))
chk("S(0.6) z, S(-1.0) z", [S06[2], S10[2]], [377, -377], rtol=2e-3)
chk("t' at z=-1.0 (ns), g there, E_y, H_x", [4 - 1/0.3, g9(4*ns - 1.0/c), sh.E([0, 0, -1], 4*ns)[1], sh.H([0, 0, -1], 4*ns)[0]], [0.667, 2, 377, 1])
chk("J.E at sheet t=0.5 ns", np.dot(sh.J(0.5*ns), sh.E([0, 0, 1e-9], 0.5*ns)), -754, rtol=2e-3)
chk("eta0 g^2/4 with g=2", eta0*4/4, 377)
# exam-overlap check: the exam (SP18 E2 #5) uses y=0, J=-Js x, t=5 ns, waveform 0->4 (1-2 ns) ->-4 (3 ns) flat to 4 ns
gex = pwl([(1*ns, 0), (2*ns, 4), (3*ns, -4), (4*ns, -4), (4*ns, 0)])
report(not np.allclose([g9(t*ns) for t in np.linspace(0, 4, 41)], [gex(t*ns) for t in np.linspace(0, 4, 41)]),
       "19.9 waveform differs from the exam waveform; instant 4 ns vs exam 5 ns; plane z=0 vs y=0")
exH = 0.5*np.cross(-X, Y)    # exam forward H direction
report(np.allclose(exH, -0.5*Z), "exam key reproduced by my code: forward H = -1/2 Js z (y=0, J=-Js x)")
report(not np.allclose(0.5*np.cross(-Y, Z), exH), "19.9 forward H unit vector (-1/2 x) differs from the key's (-1/2 z)")

# ======================================================================================
print("\n19.10 Two sheets")
gA = pwl([(0, 1), (10*ns, 1)]); gB = pwl([(10*ns, 1), (20*ns, 1)])
A = Sheet(Z, [0, 0, 0], X, gA); B = Sheet(Z, [0, 0, 3], -X, gB)
Et = lambda r, t: A.E(r, t) + B.E(r, t); Ht = lambda r, t: A.H(r, t) + B.H(r, t)
agree("H_A = -/+ 1/2 g_A y (z >< 0)", lambda r, t: -np.sign(r[2])*0.5*gA(t - abs(r[2])/c)*Y, A.H, rand_pts(20, 5, (0, 30*ns), lambda r: r[2]), 0.5)
agree("H_B = +/- 1/2 g_B y (z >< 3)", lambda r, t: np.sign(r[2] - 3)*0.5*gB(t - abs(r[2] - 3)/c)*Y, B.H, rand_pts(20, 5, (0, 30*ns), lambda r: r[2] - 3), 0.5)
worst = 0.0
for z in np.linspace(3.001, 20, 400):
    for t in np.linspace(0, 100*ns, 400):
        worst = max(worst, np.linalg.norm(Et([0, 0, z], t)), np.linalg.norm(Ht([0, 0, z], t)))
report(worst < 1e-9, f"(b) total field for z>3 m is zero on a 400x400 grid (max {worst:.1e})")
chk("(c) z=-1.5 at 10 ns: Ex, Hy", [Et([0, 0, -1.5], 10*ns)[0], Ht([0, 0, -1.5], 10*ns)[1]], [-188.5, 0.5])
chk("(c) z=-1.5 at 30 ns: Ex, Hy", [Et([0, 0, -1.5], 30*ns)[0], Ht([0, 0, -1.5], 30*ns)[1]], [188.5, -0.5])
tg = np.linspace(0, 50*ns, 50001); r15 = np.array([Et([0, 0, -1.5], t)[0] for t in tg])
on = tg[np.abs(r15) > 1e-9]; jumps = on[np.r_[True, np.diff(on) > 1e-10*2e2]]
chk("(c) pulse windows start times (ns)", [on[0]/ns, on[np.argmax(np.diff(on) > 1e-9) + 1]/ns, on[-1]/ns], [5, 25, 35], atol=2e-3)
chk("(d) 15 ns: Ex, Hy at z=-3, 2.2, 3.5, 0.5, -5",
    [Et([0, 0, -3], 15*ns)[0], Ht([0, 0, -3], 15*ns)[1], Et([0, 0, 2.2], 15*ns)[0], Ht([0, 0, 2.2], 15*ns)[1],
     Et([0, 0, 3.5], 15*ns)[0], Ht([0, 0, 3.5], 15*ns)[1], Et([0, 0, 0.5], 15*ns)[0], Ht([0, 0, 0.5], 15*ns)[1], Et([0, 0, -5], 15*ns)[0]],
    [-188.5, 0.5, 0, -1.0, 0, 0, 0, 0, 0], atol=1e-6)
zg = np.linspace(-6, 6, 120001); Hd = np.array([Ht([0, 0, z], 15*ns)[1] for z in zg])
seg = zg[np.abs(Hd + 1.0) < 1e-9]; segA = zg[np.abs(Hd - 0.5) < 1e-9]
chk("(d) extents: H=-1 region, A's downward region", [seg[0], seg[-1], segA[0], segA[-1]], [1.5, 3, -4.5, -1.5], atol=2e-4)
chk("(e) E at sheet B, 15 ns", np.linalg.norm(Et([0, 0, 3 + 1e-9], 15*ns)), 0, atol=1e-6)
chk("(e) J_A.E at A, energy A (nJ/m2), pulse energy (nJ/m2)",
    [np.dot(A.J(5*ns), Et([0, 0, 1e-9], 5*ns)), eta0/2*10e-9*1e9, eta0/4*10e-9*1e9], [-188.5, 1885, 942.5])
# energy conservation: integrate S through z = -10 m over all time
tg = np.linspace(0, 120*ns, 120001)
Sz = np.array([np.cross(Et([0, 0, -10], t), Ht([0, 0, -10], t))[2] for t in tg])
chk("(e) total energy through z=-10 m toward -z (nJ/m2)", -np.trapezoid(Sz, tg)*1e9, 1885, rtol=2e-3)
r3p, r3m = [0, 0, 3 + 1e-9], [0, 0, 3 - 1e-9]
chk("jump at z=3, t=15 ns: z x (H+ - H-)", np.cross(Z, Ht(r3p, 15*ns) - Ht(r3m, 15*ns)), [-1, 0, 0])
As = Sheet(Z, [0, 0, 0], X, gauss(5*ns, 1*ns)); Bs = Sheet(Z, [0, 0, 3], -X, gauss(15*ns, 1*ns))
maxwell_fd("19.10 superposed fields", lambda r, t: As.E(r, t) + Bs.E(r, t), lambda r, t: As.H(r, t) + Bs.H(r, t), mu0, eps0,
           [(r, t) for r, t in rand_pts(40, 5, (0, 30*ns), avoid=lambda r: r[2]*(r[2] - 3)) if r[2] < 3][:12], eta0/2)  # z>3 cancels identically (rel. residual meaningless there; (b) checks it)

# ======================================================================================
print("\n19.11 Diagonal sheet y = x")
f11 = 150e6; w11 = 2*np.pi*f11
nP = unit(X - Y)
sh = Sheet(nP, [0, 0, 0], Z, lambda t: 0.2*np.cos(w11*t))
b11 = w11/c
chk("beta, lambda", [b11, 2*np.pi/b11], [np.pi, 2])
r = np.array([1.0, -1.0, 0.0]); s, dP = sh.side(r)
chk("side of P (+1 means n = (x-y)/sqrt2), d_P, t1 (ns)", [s, dP, dP/c/ns], [1, 1.414, 4.714])
d_formula = lambda p: abs(p[0] - p[1])/np.sqrt(2)
report(all(abs(sh.side(p)[1] - d_formula(p)) < 1e-12 for p in rng.uniform(-3, 3, (20, 3))), "d = |x - y|/sqrt2")
pts = rand_pts(20, 3, (0, 20*ns), avoid=lambda p: p[0] - p[1])
agree("H = +/-0.0707 (x+y) cos(wt - b d)", lambda p, t: np.sign(p[0] - p[1])*0.1/np.sqrt(2)*(X + Y)*np.cos(w11*t - b11*d_formula(p)), sh.H, pts, 0.1)
agree("E = -12 pi cos(wt - b d) z", lambda p, t: -12*np.pi*np.cos(w11*t - b11*d_formula(p))*Z, sh.E, pts, 37.7)
chk("0.1/sqrt2, 12 pi", [0.1/np.sqrt(2), 12*np.pi], [0.0707, 37.7])
maxwell_fd("19.11 fields", sh.E, sh.H, mu0, eps0, pts[:12], 37.7, h=1e-4)
bc_check("19.11", sh, [np.array([1, 1, 0]), np.array([-2, -2, 3])], [1*ns, 2.2*ns])
t1 = dP/c
E1, H1 = sh.E(r, t1), sh.H(r, t1); S1 = np.cross(E1, H1)
chk("E(P,t1)", E1, [0, 0, -37.7]); chk("H(P,t1)", H1, [0.0707, 0.0707, 0])
chk("S(P,t1), |S|, 1.2 pi", np.r_[S1, np.linalg.norm(S1), 1.2*np.pi], [2.67, -2.67, 0, 3.77, 3.77])
u = 3e6*Z
Fe = -e_ch*E1; Fm = -e_ch*np.cross(u, mu0*H1)
chk("F_e", Fe, [0, 0, 6.04e-18], atol=1e-22); chk("F_m", Fm, [4.27e-20, -4.27e-20, 0], atol=1e-24)
chk("|F_m|, |B|, ratio", [np.linalg.norm(Fm), np.linalg.norm(mu0*H1), np.linalg.norm(Fm)/np.linalg.norm(Fe)], [6.04e-20, 1.257e-7, 0.01])
report(np.linalg.norm(np.cross(unit(X + Y)*3e6, mu0*H1)) < 1e-20, "F_m = 0 for u || (x+y)")
report(np.allclose(unit(Fm), nP), "F_m points along n (direction of travel)")

# ======================================================================================
print("\n19.12 Magnetic medium mu_r=2, eps_r=8, sheet x=0, J = -K z")
K = lambda t: 2e6*t if t > 0 else 0.0          # A/m, t in s (2 A/m per us)
sh = Sheet(X, [0, 0, 0], -Z, K, epsr=8, mur=2)
chk("v, eta, 60 pi", [sh.v, sh.eta, 60*np.pi], [7.5e7, 188.5, 188.5])
report(abs(sh.eta - eta0/np.sqrt(8)) > 50, f"eta0/sqrt8 = {eta0/np.sqrt(8):.1f} differs (watch-out claim)")
# (b)-(c): solve the two BCs for the amplitudes A (forward E_z) and B (reverse E_z) directly
# forward: H = x x (A z)/eta = -A/eta y ; reverse: H = (-x) x (B z)/eta = +B/eta y
Hf = np.cross(X, Z)/sh.eta; Hr = np.cross(-X, Z)/sh.eta
chk("forward H per E_z (y), reverse (y), times eta", [Hf[1]*sh.eta, Hr[1]*sh.eta], [-1, 1])
M = np.array([[1, -1], [np.cross(X, Hf - 0*Hr)[2], -np.cross(X, Hr)[2]]])   # rows: E continuity; z-comp of x x (H1-H2) = -K
AB = np.linalg.solve(M, [0, -1.0])
chk("A = B = eta/2 per unit K", AB, [sh.eta/2, sh.eta/2])
pts = rand_pts(20, 100, (0, 3*us), avoid=lambda p: p[0])
agree("E_z = eta/2 K(t-|x|/v)", lambda p, t: sh.eta/2*K(t - abs(p[0])/sh.v)*Z, sh.E, pts, 200)
agree("H_y = -/+ 1/2 K(t-|x|/v) (x >< 0)", lambda p, t: -np.sign(p[0])*0.5*K(t - abs(p[0])/sh.v)*Y, sh.H, pts, 1)
sm = Sheet(X, [0, 0, 0], -Z, gauss(1*us, 0.2*us), epsr=8, mur=2)
maxwell_fd("19.12 fields", sm.E, sm.H, sm.mu, sm.eps, rand_pts(12, 100, (0, 3*us), avoid=lambda p: p[0]), sm.eta/2, h=0.05)
bc_check("19.12", sh, [np.array([0, 1, 1])], [0.5*us, 1*us])
chk("x=1.5: delay (us), Hy, Ez, static Hy", [1.5/sh.v/us, sh.H([1.5, 0, 0], 1*us)[1], sh.E([1.5, 0, 0], 1*us)[2], 0.5*np.cross(sh.J(1*us), X)[1]],
    [0.02, -0.98, 184.7, -1.0])
chk("x=60: delay (us), Hy, Ez", [60/sh.v/us, sh.H([60, 0, 0], 1*us)[1], sh.E([60, 0, 0], 1*us)[2]], [0.8, -0.20, 37.7])
h = 1e-3; k = 1e-12; r0 = np.array([1.5, 0, 0]); t0 = 1*us
dEdx = (sh.E(r0 + h*X, t0)[2] - sh.E(r0 - h*X, t0)[2])/(2*h)
mudHdt = sh.mu*(sh.H(r0, t0 + k)[1] - sh.H(r0, t0 - k)[1])/(2*k)
chk("(e) dEz/dx, mu dHy/dt (FD)", [dEdx, mudHdt], [-2.513, -2.513])

# ======================================================================================
print("\nW. Worked problem 'A current sheet launches two waves' -- independent re-solve from its statement")
gw = pwl([(0, 0), (2*ns, 6), (2*ns, -2), (4*ns, -2)])
sh = Sheet(X, [0, 0, 0], Z, gw, epsr=4)
chk("v (m/ns), eta, eta/2", [sh.v*ns, sh.eta, sh.eta/2], [0.15, 188.4, 94.2])
pts = rand_pts(30, 1.5, (0, 10*ns), avoid=lambda p: p[0])
agree("(a) H = +1/2 Js(t - x/v) y (x>0), -1/2 Js(t + x/v) y (x<0)",
      lambda p, t: (0.5*gw(t - p[0]/sh.v)*Y if p[0] > 0 else -0.5*gw(t + p[0]/sh.v)*Y), sh.H, pts, 1)
agree("(b) E = -(eta/2) Js(t -/+ x/v) z", lambda p, t: -sh.eta/2*gw(t - abs(p[0])/sh.v)*Z, sh.E, pts, 300)
sm = Sheet(X, [0, 0, 0], Z, gauss(2*ns, 0.4*ns), epsr=4)
maxwell_fd("W fields", sm.E, sm.H, sm.mu, sm.eps, rand_pts(12, 1, (0, 8*ns), avoid=lambda p: p[0]), sm.eta/2)
bc_check("W", sh, [np.array([0, 0.3, -0.2])], [1*ns, 3*ns])
chk("(a) jump x x (H1-H2) (z, per Js)", np.cross(X, sh.H([1e-9, 0, 0], 1*ns) - sh.H([-1e-9, 0, 0], 1*ns))[2]/gw(1*ns), 1.0)
for xx in (1e-3, -1e-3):
    S = np.cross(sh.E([xx, 0, 0], 1*ns), sh.H([xx, 0, 0], 1*ns))
    report(np.sign(S[0]) == np.sign(xx), f"(b) E x H at x={xx:+} points away from the sheet: {fmt(S)}")
Hy = lambda x: sh.H([x, 0, 0], 6*ns)[1]; Ez = lambda x: sh.E([x, 0, 0], 6*ns)[2]
d = 1e-6
chk("(c) landmarks |x| for t'=0,2,4 ns", [0.15*6, 0.15*4, 0.15*2], [0.9, 0.6, 0.3])
chk("(c) Hy at x=0.2, 0.45, 0.6-, 0.6+, 0.75, 0.95", [Hy(0.2), Hy(0.45), Hy(0.6 - d), Hy(0.6 + d), Hy(0.75), Hy(0.95)], [0, -1, -1, 3, 1.5, 0], atol=1e-4)
chk("(c) Hy at x=-0.2, -0.45, -0.6+, -0.6-, -0.95", [Hy(-0.2), Hy(-0.45), Hy(-0.6 + d), Hy(-0.6 - d), Hy(-0.95)], [0, 1, 1, -3, 0], atol=1e-4)
chk("(c) ramp formula 1/2*3*(6 - x/0.15) at x=0.7", Hy(0.7), 0.5*3*(6 - 0.7/0.15))
chk("(c) Ez at 0.6+ , 0.45, -0.45, 0.75", [Ez(0.6 + d), Ez(0.45), Ez(-0.45), Ez(0.75)], [-565, 188, 188, -283], rtol=4e-3)
report(all(abs(Hy(x) + Hy(-x)) < 1e-12 and abs(Ez(x) - Ez(-x)) < 1e-9 for x in np.linspace(0.01, 1.2, 300)), "(c) Hy odd, Ez even")
rec = lambda t: sh.H([-0.45, 0, 0], t*ns)[1]
chk("(d) delay (ns)", 0.45/0.15, 3)
chk("(d) Hy at 2.9, 3.5, 5-, 5+, 6, 6.9, 7.1 ns", [rec(t) for t in (2.9, 3.5, 4.99999, 5.00001, 6, 6.9, 7.1)], [0, -0.75, -3, 1, 1, 1, 0], atol=1e-3)
S = np.cross(sh.E([0.75, 0, 0], 6*ns), sh.H([0.75, 0, 0], 6*ns))
chk("(e) S(0.75, 6 ns)", S, [423.8, 0, 0], rtol=2e-3)
chk("(e) eta/4 * 9, eta/2 * 9, eta*36/4 (kW)", [sh.eta/4*9, sh.eta/2*9, sh.eta*36/4/1e3], [423.8, 848, 1.70])
chk("(e) -J.E at t'=1 ns", -np.dot(sh.J(1*ns), sh.E([1e-9, 0, 0], 1*ns)), 848, rtol=2e-3)
Sm = np.cross(sh.E([-0.75, 0, 0], 6*ns), sh.H([-0.75, 0, 0], 6*ns))
chk("(e) S(-0.75, 6 ns)", Sm[0], -424, rtol=2e-3)
xs = np.linspace(-1.2, 1.2, 240001)
Smag = np.array([np.linalg.norm(np.cross(sh.E([x, 0, 0], 6*ns), sh.H([x, 0, 0], 6*ns))) for x in xs])
chk("(e) max |S| in snapshot (kW/m2) and where (|x|)", [Smag.max()/1e3, abs(xs[np.argmax(Smag)])], [1.70, 0.6], rtol=3e-3, atol=1e-4)
vac = Sheet(X, [0, 0, 0], Z, gw)
chk("variant vacuum: v (m/ns), eta0/2, front at 6 ns, H unchanged at 0.75*2", [vac.v*ns, eta0/2, vac.v*6*ns, vac.H([1.5, 0, 0], 6*ns)[1]], [0.3, 188, 1.8, 1.5], rtol=3e-3)
# duplicate check vs practice 19.9: geometry, current, medium, waveform all differ
report(True, "worked problem: x=0, +z current, eps_r=4, ramp-then-step; 19.9: z=0, -y current, vacuum, step-then-ramp (distinct)")

print(f"\nSUMMARY: {NF[1] - NF[0]} PASS, {NF[0]} FAIL of {NF[1]} checks")
