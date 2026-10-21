#!/usr/bin/env python3
"""Lecture 29 figures (bex-*) for the ECE 329 notes: bounce-diagram examples.

Same helpers and conventions as figs.py (plot helpers from figs_l18.py).
Running this module writes /home/claude/work/figs/<name>.html.
Every curve is computed with numpy from the bounce-diagram series below (the page's formulas);
digest10/verify_L29.py compares these functions with two independent time-steppings of the line.
Units: microseconds, metres, volts. Bounce diagrams: z to the right, t downward (the notes' layout).
No vector directions in these figures (only line voltages and currents).
"""
from figs import *
from figs import _odot, _otimes, _sub, _tint
from figs_l18 import lin, poly

C = 300.0                                   # m/us


# ------------------------------------------------------------------------------------------------ the model
def series(z, t, fi, tg, GL, Gg, T1, nmax=40):
    """V(z,t) and Z0*I(z,t) from the bounce-diagram series (one-way time T1 = l/v, z in units of T1 via zt)."""
    z = np.asarray(z, dtype=float); t = np.asarray(t, dtype=float)
    zt = z  # caller passes z/v in us
    V = np.zeros(np.broadcast(z, t).shape); ZI = np.zeros_like(V)
    for n in range(nmax):
        wf = tg * (GL * Gg) ** n
        wb = tg * GL * (GL * Gg) ** n
        F = wf * fi(t - zt - 2 * n * T1)
        B = wb * fi(t + zt - 2 * (n + 1) * T1)
        V = V + F + B
        ZI = ZI + F - B
    return V, ZI


def legs(tg, GL, Gg, T1, tmax):
    """bounce-diagram segments (z0/l, t0, z1/l, t1, weight) up to tmax"""
    out = []; w = tg; t0 = 0.0; fwd = True
    while t0 < tmax - 1e-9 and abs(w) > 1e-12:
        t1 = t0 + T1
        out.append((0.0, t0, 1.0, t1, w) if fwd else (1.0, t0, 0.0, t1, w))
        w = w * (GL if fwd else Gg); fwd = not fwd; t0 = t1
    return out


# example circuits
EX1 = dict(tg=0.5, GL=1 / 3, Gg=0.0, T1=3.0)          # l = 900 m, v = c
EX2 = dict(tg=1.0, GL=1 / 3, Gg=-1.0, T1=8.0)         # l = 2400 m, Z0 = 50, Rg = 0, RL = 100
PRB = dict(tg=2 / 3, GL=0.5, Gg=-1 / 3, T1=3.0)       # worked problem: l = 600 m, v = 200 m/us


def f_ex1(t):
    return np.sin(2 * np.pi * t) * (t >= 0)          # omega/2pi = 1 MHz, t in us


def f_step(t):
    return 1.0 * (np.asarray(t) >= 0)


def f_ex3(t):
    t = np.asarray(t, dtype=float)                   # rect(t) + 2 rect(t - 1), T = 1 us
    return 1.0 * ((t > -0.5) & (t < 0.5)) + 2.0 * ((t > 0.5) & (t < 1.5))


def f_ramp(t):
    t = np.asarray(t, dtype=float)                   # 3 t/T V for 0 < t < T, T = 1 us
    return 3.0 * t * ((t > 0) & (t < 1))


def frac(w):
    """weight as a short fraction label"""
    from fractions import Fraction
    F = Fraction(w).limit_denominator(100)
    s = f"{abs(F.numerator)}/{F.denominator}" if F.denominator != 1 else f"{abs(F.numerator)}"
    return ("−" if F < 0 else "") + s


# ------------------------------------------------------------------------------------------------ drawing helpers
def _bounce(o, X0, X1, Y0, Y1, tmax, prm, tticks, zlab_l, zlab_r, gg_lab, gl_lab, cuts_t=(), cut_z=None, cut_lab=None,
            at=0.3, below=False, at_b=None):
    """bounce diagram: z from X0 (z = 0) to X1 (z = l), t from Y0 down to Y1 (= tmax)"""
    MT = lin(0, tmax, Y0, Y1)
    o.append(line(X0, Y0, X1 + 22, Y0, w=1.3, arrow=True)); o.append(text(X1 + 26, Y0 + 4, "z", size=12.5, anchor="start", math=True))
    o.append(line(X0, Y0, X0, Y1 + 16, w=1.3, arrow=True)); o.append(text(X0 + 2, Y1 + 30, "t", size=12.5, math=True))
    o.append(line(X1, Y0, X1, Y1 + 4, w=1.0, dash="2 3", stroke="var(--muted)"))
    o.append(text(X0, Y0 - 8, zlab_l, size=10.5, fill="var(--muted)"))
    o.append(text(X1, Y0 - 8, zlab_r, size=10.5, fill="var(--muted)"))
    o.append(text(X0, Y0 - 24, gg_lab, size=10.5, fill="var(--muted)"))
    o.append(text(X1, Y0 - 24, gl_lab, size=10.5, fill="var(--muted)"))
    for tv, tl in tticks:
        o.append(line(X0 - 3, MT(tv), X0 + 3, MT(tv), w=1.0))
        o.append(text(X0 - 6, MT(tv) + 4, tl, size=10, anchor="end", fill="var(--muted)"))
    for tc, lab in cuts_t:
        o.append(line(X0, MT(tc), X1, MT(tc), w=1.0, dash="4 3", stroke="var(--hi)"))
        o.append(text(X1 + 5, MT(tc) + 4, lab, size=10.5, anchor="start", fill="var(--hi)", weight=600))
    if cut_z is not None:
        Xc = X0 + cut_z * (X1 - X0)
        o.append(line(Xc, Y0, Xc, Y1, w=1.0, dash="4 3", stroke="var(--hi)"))
        if cut_lab:
            o.append(text(Xc, Y1 + 14, cut_lab, size=10.5, fill="var(--hi)", weight=600))
    for (za, ta, zb, tb, w) in legs(prm["tg"], prm["GL"], prm["Gg"], prm["T1"], tmax):
        tb_c = min(tb, tmax); zb_c = za + (zb - za) * (tb_c - ta) / (tb - ta)
        xa, ya = X0 + za * (X1 - X0), MT(ta); xb, yb = X0 + zb_c * (X1 - X0), MT(tb_c)
        col = "var(--accent)" if zb > za else "var(--accent2)"
        o.append(line(xa, ya, xb, yb, stroke=col, w=2.4, arrow=(tb_c == tb)))
        # weight label a fraction `at` along the full leg, offset 11 px along the upward normal
        f_ = at if (zb > za or at_b is None) else at_b
        xm, ym = xa + f_ * (X0 + zb * (X1 - X0) - xa), ya + f_ * (MT(tb) - ya)
        dx, dy = xb - xa, yb - ya; L_ = math.hypot(dx, dy)
        nx, ny = (dy / L_, -dx / L_) if dx > 0 else (-dy / L_, dx / L_)     # the normal with ny < 0 (screen up)
        if below and zb > za:
            nx, ny = -nx, -ny
        o.append(text(xm + 12 * nx, ym + 12 * ny + 4, frac(w), size=10.5, fill=col, weight=600))
        if cut_z is not None and min(za, zb_c) <= cut_z <= max(za, zb_c):
            tcross = ta + (tb - ta) * (cut_z - za) / (zb - za)
            o.append(circle(X0 + cut_z * (X1 - X0), MT(tcross), 3.2, fill="var(--hi)", stroke="none"))
    return MT


def _panel_axes(o, X0, X1, Yc, MY, title, zticks, MZ, vticks, zlabel="z (m)"):
    """axis at V = 0; tick labels below the lowest guide line so curves never cover them"""
    o.append(text(X0, MY(max(v for v, _ in vticks)) - 8, title, size=11.5, anchor="start", weight=600))
    o.append(line(X0, MY(0), X1 + 8, MY(0), w=1.1, arrow=True, small=True))
    o.append(text(X1 + 12, MY(0) + 4, zlabel, size=10.5, anchor="start", fill="var(--muted)"))
    ylab = MY(min(0, min(v for v, _ in vticks))) + 13
    for zv, zl in zticks:
        o.append(line(MZ(zv), MY(0) - 2.5, MZ(zv), MY(0) + 2.5, w=1.0))
        if zl:
            o.append(text(MZ(zv), ylab, zl, size=9.5, fill="var(--muted)"))
    for vv, vl in vticks:
        o.append(line(X0, MY(vv), X1, MY(vv), w=0.7, dash="2 3", stroke="var(--muted)"))
        o.append(text(X0 - 4, MY(vv) + 3.5, vl, size=9.5, anchor="end", fill="var(--muted)"))


def _legend(o, x, y, items):
    for i, (col, dash, lab) in enumerate(items):
        o.append(line(x, y + 16 * i - 4, x + 22, y + 16 * i - 4, stroke=col, w=2.2, dash=dash))
        o.append(text(x + 27, y + 16 * i, lab, size=10.5, anchor="start"))


# ------------------------------------------------------------------------------------------------ 1. Example 1
def fig_bex_example1():
    W, H = 640, 330
    o = [svg_open(W, H)]
    o.append(text(20, 20, "Example 1: matched generator, one echo", size=12.5, anchor="start", weight=600))
    _bounce(o, 62, 212, 62, 300, 7.0, EX1, [(0, "0"), (3, "3"), (6, "6 μs")], "0", "900 m",
            "Γ" + "<tspan baseline-shift=\"sub\" style=\"font-size:8px\">g</tspan> = 0",
            "Γ" + "<tspan baseline-shift=\"sub\" style=\"font-size:8px\">L</tspan> = 1/3",
            cuts_t=[(1, "a"), (2, "b"), (4.5, "c")])
    # right: snapshots
    X0, X1 = 320, 590
    MZ = lin(0, 900, X0, X1)
    zz = np.linspace(0, 900, 1801)
    for k, (tv, lab) in enumerate(((1.0, "a  t = 1 μs"), (2.0, "b  t = 2 μs"), (4.5, "c  t = 4.5 μs (this site)"))):
        Yc = 95 + 88 * k
        MY = lambda v, Yc=Yc: Yc - 50 * v
        _panel_axes(o, X0, X1, Yc, MY, lab, [(0, "0"), (300, "300"), (450, "450") if k == 2 else (450, None), (600, "600"), (900, "900")],
                    MZ, [(0.5, "½"), (-0.5, "−½")])
        V, ZI = series(zz / C, tv, f_ex1, **EX1)
        o.append(poly(zz, V, MZ, MY, stroke="var(--accent)", w=2.2))
    o.append(svg_close())
    figure("bex-example1", "".join(o),
           "<strong>Example 1.</strong> The burst enters at half the source voltage, reflects with Γ<sub>L</sub> = 1/3 "
           "and is absorbed at the matched generator. Horizontal cuts a–c are the snapshots on the right. "
           "In c the echo has reached z = 450 m and adds to the burst.")


# ------------------------------------------------------------------------------------------------ 2. Example 2
def fig_bex_example2():
    W, H = 640, 360
    o = [svg_open(W, H)]
    o.append(text(20, 20, "Example 2: step input, the midpoint z = 1200 m", size=12.5, anchor="start", weight=600))
    _bounce(o, 62, 222, 62, 322, 56.0, EX2, [(0, "0"), (8, "8"), (16, "16"), (24, "24"), (32, "32"), (40, "40"), (48, "48 μs")],
            "0", "2400 m",
            "Γ" + "<tspan baseline-shift=\"sub\" style=\"font-size:8px\">g</tspan> = −1",
            "Γ" + "<tspan baseline-shift=\"sub\" style=\"font-size:8px\">L</tspan> = 1/3",
            cut_z=0.5, cut_lab="z = 1200 m", at=0.22, below=True, at_b=0.72)
    # right: V(1200, t) and Z0 I(1200, t)
    X0, X1 = 320, 580
    MTt = lin(0, 60, X0, X1)
    Ybase = 300
    MY = lambda v: Ybase - 150 * v
    o.append(text(X0 - 6, 52, "V (V)", size=10.5, anchor="end", fill="var(--accent)"))
    o.append(text(X1 + 6, 52, "I (mA)", size=10.5, anchor="start", fill="var(--accent2)"))
    for vv in (0.5, 1.0, 1.5):
        o.append(line(X0, MY(vv), X1, MY(vv), w=0.7, dash="2 3", stroke="var(--muted)"))
    for vv, vl in ((0, "0"), (0.5, "0.5"), (1.0, "1"), (1.5, "1.5")):
        o.append(text(X0 - 5, MY(vv) + 3.5, vl, size=9.5, anchor="end", fill="var(--accent)"))
        o.append(text(X1 + 5, MY(vv) + 3.5, f"{vv * 20:.0f}", size=9.5, anchor="start", fill="var(--accent2)"))
    o.append(line(X0, MY(0), X0, MY(1.62), w=1.1))
    o.append(line(X1, MY(0), X1, MY(1.62), w=1.1))
    o.append(line(X0, MY(0), X1 + 0, MY(0), w=1.1))
    o.append(text(X1, MY(0) + 30, "t (μs)", size=10.5, anchor="end", fill="var(--muted)"))
    for tv in range(0, 61, 10):
        o.append(line(MTt(tv), MY(0) - 2.5, MTt(tv), MY(0) + 2.5, w=1.0))
        o.append(text(MTt(tv), MY(0) + 14, f"{tv}", size=9.5, fill="var(--muted)"))
    tt = np.linspace(0, 60, 6001)
    V, ZI = series(1200 / C, tt, f_step, **EX2)
    o.append(poly(tt, ZI, MTt, MY, stroke="var(--accent2)", w=2.0, dash="6 3"))
    o.append(poly(tt, V, MTt, MY, stroke="var(--accent)", w=2.4))
    for tm, vv, lab in ((8, 1, "1"), (16, 4 / 3, "4/3"), (32, 8 / 9, "8/9"), (48, 28 / 27, "28/27")):
        o.append(text(MTt(tm), MY(vv) - 6, lab, size=10, fill="var(--accent)", weight=600))
    _legend(o, MTt(24), MY(0.8), [("var(--accent)", None, "V(1200, t)"), ("var(--accent2)", "6 3", "I(1200, t)")])
    o.append(svg_close())
    figure("bex-example2", "".join(o),
           "<strong>Example 2, unit step.</strong> Each dot on the vertical cut adds a step of its segment's weight. "
           "V(1200, t) (left scale) settles to 1 V and I(1200, t) (right scale) to 10 mA, the DC values. "
           "Every second level of V is exactly 1 V because Γ<sub>g</sub> = −1.")


# ------------------------------------------------------------------------------------------------ 3. Example 3
def fig_bex_example3():
    W, H = 640, 434                                  # room for panel c's z labels
    o = [svg_open(W, H)]
    S = 22                                           # px per volt
    # top row: the source waveform (left) and the legend (right)
    MT = lin(-1, 3, 52, 300); Yi = 72; MYi = lambda v: Yi - S * v
    o.append(text(52, MYi(2) - 8, "source " + _sub("f", "i") + "(t)", size=11.5, anchor="start", weight=600))
    o.append(line(MT(-1), MYi(0), MT(3) + 6, MYi(0), w=1.1, arrow=True, small=True))
    o.append(text(MT(3) + 10, MYi(0) + 4, "t (μs)", size=10.5, anchor="start", fill="var(--muted)"))
    tt = np.linspace(-1, 3, 1601)
    o.append(poly(tt, f_ex3(tt), MT, MYi, stroke="currentColor", w=2.0))
    for tv, tl in ((-0.5, "−0.5"), (0.5, "0.5"), (1.5, "1.5")):
        o.append(line(MT(tv), MYi(0) - 2.5, MT(tv), MYi(0) + 2.5, w=1.0))
        o.append(text(MT(tv), MYi(0) + 13, tl, size=9.5, fill="var(--muted)"))
    o.append(text(MT(0), MYi(1) - 4, "1 V", size=10, fill="var(--muted)"))
    o.append(text(MT(1), MYi(2) - 4, "2 V", size=10, fill="var(--muted)"))
    _legend(o, 420, 40, [("var(--accent)", None, "V (V)"), ("var(--accent2)", "5 3", _sub("Z", "0") + "I (V)")])
    X0, X1 = 52, 590
    MZ = lin(0, 2400, X0, X1)
    zz = np.linspace(0, 2400, 9601)
    rows = [(160, 3.0, "a  t = 3 μs", (0, 450, 750, 1050, 2400), [(1, "1"), (2, "2")]),
            (268, 9.0, "b  t = 9 μs (this site)", (0, 1950, 2250, 2400), [(1, "1"), (2, "2"), (-1, "−1")]),
            (386, 11.0, "c  t = 11 μs", (0, 1350, 1650, 1950, 2400), [(1, "1"), (2, "2"), (-1, "−1")])]
    for Yc, tv, lab, ticks, vt in rows:
        MY = lambda v, Yc=Yc: Yc - S * v
        _panel_axes(o, X0, X1, Yc, MY, lab, [(zv, f"{zv}") for zv in ticks], MZ, vt)
        V, ZI = series(zz / C, tv, f_ex3, **EX2)
        o.append(poly(zz, V, MZ, MY, stroke="var(--accent)", w=2.2))
        o.append(poly(zz, ZI, MZ, MY, stroke="var(--accent2)", w=1.8, dash="5 3"))
    o.append(svg_close())
    figure("bex-example3", "".join(o),
           "<strong>Example 3 snapshots.</strong> a: heading right, the 1 V part (sent first) in front. "
           "b: near the load the 2 V part overlaps its own echo; the 1 V part's echo heads left. c: the echo, ⅓ as large, 1 V part still in front. "
           "Z<sub>0</sub>I = V forward, −V backward.")


# ------------------------------------------------------------------------------------------------ 4. worked problem
def fig_bex_ramp_problem():
    W, H = 640, 360
    o = [svg_open(W, H)]
    o.append(text(20, 20, "bounce diagram (weights × " + _sub("f", "i") + ")", size=11.5, anchor="start", weight=600))
    _bounce(o, 62, 232, 62, 300, 8.0, PRB, [(0, "0"), (3, "3"), (6, "6 μs")], "0", "600 m",
            "Γ" + "<tspan baseline-shift=\"sub\" style=\"font-size:8px\">g</tspan> = −1/3",
            "Γ" + "<tspan baseline-shift=\"sub\" style=\"font-size:8px\">L</tspan> = 1/2",
            cuts_t=[(2, "2"), (3.5, "3.5"), (5, "5")], at=0.45)   # cut labels: times, not part letters
    zz = np.linspace(0, 600, 2401)
    X0, X1 = 330, 590
    MZ = lin(0, 600, X0, X1)
    for k, (tv, lab) in enumerate(((2.0, "t = 2 μs, part (b)"), (3.5, "t = 3.5 μs, part (c)"), (5.0, "t = 5 μs, part (b)"))):
        Yc = 112 + 104 * k
        MY = lambda v, Yc=Yc: Yc - 24 * v
        _panel_axes(o, X0, X1, Yc, MY, lab, [(0, "0"), (200, "200"), (400, "400"), (500, "500" if k == 1 else None), (600, "600")],
                    MZ, [(1, "1"), (2, "2"), (-1, "−1")] if k == 2 else [(1, "1"), (2, "2")])
        V, ZI = series(zz / 200.0, tv, f_ramp, **PRB)
        o.append(poly(zz, V, MZ, MY, stroke="var(--accent)", w=2.2))
        o.append(poly(zz, ZI, MZ, MY, stroke="var(--accent2)", w=1.8, dash="5 3"))
    _legend(o, 470, 22, [("var(--accent)", None, "V (V)"), ("var(--accent2)", "5 3", _sub("Z", "0") + "I (V)")])
    o.append(svg_close())
    figure("bex-ramp-problem", "".join(o),
           "<strong>The ramp pulse.</strong> 2 μs: heading right, the ramp is drawn backwards (its 0 V start leads). "
           "3.5 μs: pulse and echo overlap on 500–600 m; V adds, I subtracts. 5 μs: the echo, half as large, heads left, "
           "drawn forwards. Z<sub>0</sub> = 50 Ω.")


if __name__ == "__main__":
    for fn in (fig_bex_example1, fig_bex_example2, fig_bex_example3, fig_bex_ramp_problem):
        fn()
