#!/usr/bin/env python3
"""Lecture 30 figures (mline-*) for the ECE 329 notes: multi-line circuits.

Same helpers and conventions as figs.py (plot helpers from figs_l18.py).
Running this module writes /home/claude/work/figs/<name>.html.
Bounce diagrams: z to the right, t downward (as in the notes). Every segment's end points and
weight come from the bounce bookkeeping checked in digest10/verify_L30.py (sections C and H);
the burst snapshots are computed with numpy from the notes' Example 2 series (section D there).
No vector directions are drawn, so no cross products are needed.
"""
from figs import *
from figs import _odot, _otimes, _sub, _tint, _zigzag
from figs_l18 import lin, poly

PI = np.pi
C1, C2 = "var(--accent)", "var(--hi)"     # waves on line 1, line 2


# ------------------------------------------------------------------------------------------------ shared drawing
def _circuit_strip(o, X0, Xj, X1, Yt, Yb, labels):
    """generator (Thevenin) at the left, line 1 X0..Xj, line 2 Xj..X1, load resistor at the right"""
    xs = X0 - 62
    ym = (Yt + Yb) / 2
    o.append(circle(xs, ym, 10))
    o.append(text(xs, ym - 2, "+", size=10)); o.append(text(xs, ym + 8, "−", size=10))
    o.append(line(xs, Yt, xs, ym - 10, w=1.4)); o.append(line(xs, ym + 10, xs, Yb, w=1.4))
    o.append(line(xs, Yt, xs + 10, Yt, w=1.4))
    o.append(_zigzag(xs + 10, Yt, X0 - 12, Yt, n=6, amp=5, color="currentColor", w=1.4))
    o.append(line(X0 - 12, Yt, X0, Yt, w=1.4)); o.append(line(xs, Yb, X0, Yb, w=1.4))
    o.append(text(xs, Yb + 16, labels["src"], size=11))
    o.append(text((xs + X0) / 2 + 2, Yt - 12, labels["Rg"], size=11))
    for (xa, xb, col, w) in ((X0, Xj, C1, 3.2), (Xj, X1, C2, 4.6)):
        o.append(line(xa, Yt, xb, Yt, stroke=col, w=w)); o.append(line(xa, Yb, xb, Yb, stroke=col, w=w))
    o.append(text((X0 + Xj) / 2, ym + 4, labels["l1"], size=11.5))
    o.append(text((Xj + X1) / 2, ym + 4, labels["l2"], size=11.5))
    o.append(line(X1, Yt, X1 + 18, Yt, w=1.4)); o.append(line(X1, Yb, X1 + 18, Yb, w=1.4))
    o.append(_zigzag(X1 + 18, Yt, X1 + 18, Yb, n=6, amp=5, color="currentColor", w=1.4))
    o.append(text(X1 + 28, ym + 4, labels["RL"], size=11, anchor="start"))
    for X, s in ((X0, labels["z0"]), (Xj, labels["zj"]), (X1, labels["z1"])):
        o.append(text(X, Yb + 16, s, size=10.5, fill="var(--muted)"))


def _bounce(o, X0, Xj, X1, Y0, MY, MZ, tmax, segs, coefs, tticks, tunit):
    """segs: (za, ta, zb, tb, label, line_no, frac, side); side = +1 label above-right, -1 below-left"""
    Yend = MY(tmax)
    for tv, tl in tticks:
        o.append(line(X0, MY(tv), X1, MY(tv), stroke="var(--muted)", w=0.7, dash="2 4"))
        o.append(text(X0 - 7, MY(tv) + 4, tl, size=10, anchor="end", fill="var(--muted)"))
    o.append(line(X0, Y0, X1 + 28, Y0, w=1.3, arrow=True)); o.append(text(X1 + 34, Y0 + 4, "z", size=12.5, anchor="start", math=True))
    o.append(line(X0, Y0, X0, Yend + 14, w=1.3, arrow=True))
    o.append(text(X0 - 7, Yend + 26, tunit, size=11, anchor="end", math=False))
    for X in (Xj, X1):
        o.append(line(X, Y0, X, Yend + 6, stroke="currentColor", w=0.9, dash="3 3"))
    for X, s, anc, dy in coefs:
        o.append(text(X, Y0 - 8 - dy, s, size=10.5, anchor=anc))
    for (za, ta, zb, tb, lab, ln, frac, side) in segs:
        xa, ya, xb, yb = MZ(za), MY(ta), MZ(zb), MY(tb)
        col = C1 if ln == 1 else C2
        o.append(arrow(xa, ya, xb, yb, stroke=col, w=1.9, small=True))
        xm, ym = xa + frac * (xb - xa), ya + frac * (yb - ya)
        dx, dy = xb - xa, yb - ya
        L = math.hypot(dx, dy)
        nx, ny = dy / L, -dx / L            # a unit normal; flip so that side=+1 is above (screen y smaller)
        if ny > 0:
            nx, ny = -nx, -ny
        off = 11 * side
        o.append(text(xm + nx * off, ym + ny * off + 4, lab, size=11, fill=col, weight=600))


# ------------------------------------------------------------------------------------------------ 1. notes' circuit
def fig_mline_bounce():
    W, H = 640, 470
    o = [svg_open(W, H)]
    X0, Xj, X1 = 120, 335, 550
    _circuit_strip(o, X0, Xj, X1, 32, 68, dict(
        src=_sub("f", "i") + "(t)", Rg=_sub("R", "g") + " = 2" + _sub("Z", "1"),
        l1=_sub("Z", "1") + ",  " + _sub("v", "1"), l2=_sub("Z", "2") + " = 2" + _sub("Z", "1") + ",  " + _sub("v", "2") + " = 2" + _sub("v", "1"),
        RL=_sub("R", "L") + " = " + _sub("Z", "2"), z0="0", zj="ℓ/2", z1="ℓ"))
    Y0 = 128
    MZ = lin(0, 2400, X0, X1)
    MY = lin(0, 32, Y0, Y0 + 300)
    segs = [
        (0, 0, 1200, 8, "1/3", 1, 0.5, 1),
        (1200, 8, 0, 16, "1/9", 1, 0.5, 1),
        (1200, 8, 2400, 12, "4/9", 2, 0.5, 1),
        (0, 16, 1200, 24, "1/27", 1, 0.5, 1),
        (1200, 24, 0, 32, "1/81", 1, 0.5, 1),
        (1200, 24, 2400, 28, "4/81", 2, 0.5, 1),
    ]
    coefs = [(X0 - 4, _sub("τ", "g") + " = " + _sub("Γ", "g") + " = 1/3", "start", 0),
             (Xj, _sub("Γ", "12") + " = 1/3,  " + _sub("τ", "12") + " = 4/3", "middle", 16),
             (X1 + 4, _sub("Γ", "L") + " = 0", "end", 0)]
    ticks = [(8, "8"), (12, "12"), (16, "16"), (24, "24"), (28, "28"), (32, "32")]
    _bounce(o, X0, Xj, X1, Y0, MY, MZ, 32, segs, coefs, ticks, "t (μs)")
    # nothing comes back from line 2: note
    o.append(text(X1 - 9, MY(20), "no echo:", size=10.5, anchor="end", fill="var(--muted)"))
    o.append(text(X1 - 9, MY(20) + 14, _sub("R", "L") + " = " + _sub("Z", "2"), size=10.5, anchor="end", fill="var(--muted)"))
    o.append(svg_close())
    figure("mline-bounce", "".join(o),
           "<strong>The notes' two-line circuit and its impulse bounce diagram.</strong> Times are Example 2's: "
           "T<sub>1</sub> = 8 μs one way on line 1, T<sub>2</sub> = 4 μs on line 2, so line-2 paths are flatter. "
           "Each arrival at z = ℓ/2 splits in two; the matched load returns nothing.")


# ------------------------------------------------------------------------------------------------ 2. sinusoidal burst snapshots
def _f(t):
    return np.where(t >= 0, np.sin(2 * PI * t), 0.0)


def V_ex2(z, t, N=12):
    """notes' Example 2: ell = 2400 m, v1 = 150 m/us, v2 = 300 m/us; z in m, t in us"""
    l, v1, v2 = 2400.0, 150.0, 300.0
    z = np.asarray(z, float)
    V = np.zeros_like(z)
    m1 = z <= l / 2
    for n in range(N):
        a = (1 / 9) ** n / 3
        V[m1] += a * (_f(t - z[m1] / v1 - n * l / v1) + _f(t + z[m1] / v1 - (n + 1) * l / v1) / 3)
        V[~m1] += a * (4 / 3) * _f(t - z[~m1] / v2 - (4 * n + 1) * (l / 2) / v2)
    return V


def fig_mline_burst():
    W, H = 640, 420
    o = [svg_open(W, H)]
    MZ = lin(0, 2400, 70, 590)
    A = 66
    panels = [(6.0, "t = 6 μs: the burst is still on line 1 (front at 900 m)"),
              (12.0, "t = 12 μs: the front reaches the load; the 1/9 echo has come back to 600 m"),
              (48.5, "t = 48.5 μs: late time, as in the notes' margin plot")]
    Yc0 = 72
    for i, (tt, title) in enumerate(panels):
        Yc = Yc0 + i * 128
        MY = lambda v, Yc=Yc: Yc - A * v
        o.append(text(20, Yc - 46, title, size=12, anchor="start", weight=600))
        o.append(_tint(MZ(1200), Yc - 38, MZ(2400) - MZ(1200), 76, "var(--hi)", op=0.07))
        o.append(line(MZ(0), Yc, MZ(2400) + 8, Yc, w=1.0, arrow=True))
        o.append(text(MZ(2400) + 14, Yc + 4, "z", size=12, anchor="start", math=True))
        o.append(line(MZ(1200), Yc - 38, MZ(1200), Yc + 38, w=1.0, dash="3 3"))
        o.append(line(MZ(0), Yc - 38, MZ(0), Yc + 38, w=1.0))
        for v in (0.5, -0.5):
            o.append(line(MZ(0) - 3, MY(v), MZ(0) + 3, MY(v), w=1.0))
            o.append(text(MZ(0) - 6, MY(v) + 4, f"{v:+.1f}", size=9.5, anchor="end", fill="var(--muted)"))
        z1 = np.linspace(0, 1200, 2401); z2 = np.linspace(1200, 2400, 1201)
        o.append(poly(z1, V_ex2(z1, tt), MZ, MY, stroke=C1, w=1.7))
        o.append(poly(z2, V_ex2(z2, tt), MZ, MY, stroke=C2, w=1.7))
        if i == 0:
            for zv, zl in ((0, "0"), (1200, "1200 m"), (2400, "2400 m")):
                o.append(text(MZ(zv), Yc + 52, zl, size=10, fill="var(--muted)"))
    o.append(text(MZ(600), Yc0 + 2 * 128 + 54, "line 1: amplitude 1/4 at this instant", size=10.5, fill=C1))
    o.append(text(MZ(1800), Yc0 + 2 * 128 + 54, "line 2: amplitude 1/2", size=10.5, fill=C2))
    o.append(svg_close())
    figure("mline-burst", "".join(o),
           "<strong>Example 2: V(z, t) for f<sub>i</sub>(t) = sin(2πt)u(t), t in μs</strong> (volts per volt of source). "
           "Line 2 (shaded) carries twice the wavelength of line 1, 300 m against 150 m. "
           "Line 1 holds the 1/3 wave plus its echoes.")


# ------------------------------------------------------------------------------------------------ 3. resistive junctions
def fig_mline_junctions():
    W, H = 640, 250
    o = [svg_open(W, H)]
    Yt, Yb = 70, 120
    panels = [(20, "a  direct", None), (232, "b  shunt R", "shunt"), (444, "c  series R", "series")]
    for x0, title, kind in panels:
        xj = x0 + 88
        o.append(text(x0, 24, title, size=12.5, anchor="start", weight=600))
        o.append(line(x0, Yt, xj, Yt, stroke=C1, w=3.2)); o.append(line(x0, Yb, xj, Yb, stroke=C1, w=3.2))
        x2 = xj if kind != "series" else xj + 40
        o.append(line(x2, Yt, x0 + 176, Yt, stroke=C2, w=4.6)); o.append(line(x2, Yb, x0 + 176, Yb, stroke=C2, w=4.6))
        if kind == "shunt":
            o.append(_zigzag(xj, Yt, xj, Yb, n=6, amp=5, color="currentColor", w=1.5))
            o.append(text(xj + 9, (Yt + Yb) / 2 + 4, "R", size=12, anchor="start", math=True))
        if kind == "series":
            o.append(_zigzag(xj, Yt, x2, Yt, n=6, amp=5, color="currentColor", w=1.5))
            o.append(line(xj, Yb, x2, Yb, w=1.5))
            o.append(text((xj + x2) / 2, Yt - 10, "R", size=12, math=True))
        o.append(text(x0 + 40, (Yt + Yb) / 2 + 4, _sub("Z", "1"), size=12))
        o.append(text(x0 + 150, (Yt + Yb) / 2 + 4, _sub("Z", "2"), size=12))
        o.append(arrow(x0 + 10, Yt - 14, x0 + 50, Yt - 14, stroke=C1, w=1.5, small=True))
        o.append(text(x0 + 30, Yt - 20, "V⁺", size=11, fill=C1))
        o.append(arrow(xj - 8, Yb + 16, xj - 48, Yb + 16, stroke=C1, w=1.5, small=True))
        o.append(text(xj - 28, Yb + 32, "V⁻", size=11, fill=C1))
        o.append(arrow(x0 + 130, Yt - 14 if kind != "series" else Yt - 26, x0 + 170, Yt - 14 if kind != "series" else Yt - 26, stroke=C2, w=1.5, small=True))
        o.append(text(x0 + 150, (Yt - 20) if kind != "series" else (Yt - 32), "V⁺⁺", size=11, fill=C2))
    G, T_, Z1s, Z2s, Zeq = _sub("Γ", "12"), _sub("τ", "12"), _sub("Z", "1"), _sub("Z", "2"), _sub("Z", "eq")
    rows = [
        (f"{G} = ({Z2s} − {Z1s})/({Z2s} + {Z1s})", f"{T_} = 1 + {G}"),
        (f"{Zeq} = R‖{Z2s} in {G}", f"{T_} = 1 + {G}"),
        (f"{Zeq} = R + {Z2s} in {G}", f"{T_} = (1 + {G})·{Z2s}/(R + {Z2s})"),
    ]
    for (x0, _, _), (r1, r2) in zip(panels, rows):
        o.append(text(x0 + 88, 182, r1, size=11.5))
        o.append(text(x0 + 88, 202, r2, size=11.5, fill=C2 if "·" in r2 else "currentColor", weight=600 if "·" in r2 else None))
    o.append(text(W / 2, 236, _sub("Γ", "12") + " = (" + _sub("Z", "eq") + " − " + _sub("Z", "1") + ")/(" + _sub("Z", "eq") + " + " + _sub("Z", "1") + ") in all three", size=11, fill="var(--muted)"))
    o.append(svg_close())
    figure("mline-junctions", "".join(o),
           "<strong>Three junctions, wave incident from line 1.</strong> Γ<sub>12</sub> uses the resistance the arriving wave sees, "
           "with line 2 counted as Z<sub>2</sub>. τ<sub>12</sub> = 1 + Γ<sub>12</sub> only when line 2 is directly across the junction (a, b); "
           "a series R divides the voltage first (c).")


# ------------------------------------------------------------------------------------------------ 4. worked problem
def fig_mline_problem_bounce():
    W, H = 640, 500
    o = [svg_open(W, H)]
    X0, Xj, X1 = 120, 335, 550
    _circuit_strip(o, X0, Xj, X1, 32, 68, dict(
        src="120u(t) V", Rg="60 Ω", l1="60 Ω, 300 m, 1.5 μs", l2="180 Ω, 300 m, 1 μs",
        RL="540 Ω", z0="0", zj="300 m", z1="600 m"))
    Y0 = 128
    MZ = lin(0, 600, X0, X1)
    MY = lin(0, 8, Y0, Y0 + 336)
    segs = [
        (0, 0, 300, 1.5, "60", 1, 0.68, 1),
        (300, 1.5, 0, 3.0, "30", 1, 0.35, 1),
        (300, 1.5, 600, 2.5, "90", 2, 0.5, 1),
        (600, 2.5, 300, 3.5, "45", 2, 0.5, 1),
        (300, 3.5, 600, 4.5, "−22.5", 2, 0.5, 1),
        (300, 3.5, 0, 5.0, "22.5", 1, 0.35, 1),
        (600, 4.5, 300, 5.5, "−11.25", 2, 0.5, 1),
        (300, 5.5, 600, 6.5, "5.625", 2, 0.5, 1),
        (300, 5.5, 0, 7.0, "−5.625", 1, 0.35, 1),
        (600, 6.5, 300, 7.5, "2.81", 2, 0.5, 1),
    ]
    coefs = [(X0 - 4, _sub("τ", "g") + " = 1/2, " + _sub("Γ", "g") + " = 0", "start", 0),
             (Xj, _sub("Γ", "12") + " = 1/2, " + _sub("τ", "12") + " = 3/2", "middle", 16),
             (Xj, _sub("Γ", "21") + " = −1/2, " + _sub("τ", "21") + " = 1/2", "middle", 0),
             (X1 + 4, _sub("Γ", "L") + " = 1/2", "end", 0)]
    ticks = [(v, f"{v:g}") for v in np.arange(0.5, 8.01, 0.5)]
    _bounce(o, X0, Xj, X1, Y0, MY, MZ, 8, segs, coefs, ticks, "t (μs)")
    # offspring launched at 7.5 us, cut at the 8 us window edge (no arrowheads)
    for (zb, ln, lab, dx) in ((450, 2, "−1.41", 8), (200, 1, "1.41", -8)):
        o.append(line(MZ(300), MY(7.5), MZ(zb), MY(8), stroke=C2 if ln == 2 else C1, w=1.9))
        o.append(text(MZ(zb) + dx, MY(8) - 4, lab, size=10.5, anchor="start" if dx > 0 else "end",
                      fill=C2 if ln == 2 else C1, weight=600))
    # probe line z = 150 m
    o.append(line(MZ(150), Y0, MZ(150), MY(8) + 6, stroke="var(--accent2)", w=1.2, dash="1 3"))
    o.append(text(MZ(150), MY(8) + 20, "z = 150 m", size=10.5, fill="var(--accent2)"))
    o.append(svg_close())
    figure("mline-problem-bounce", "".join(o),
           "<strong>Voltage bounce diagram of the worked problem</strong> (volts, 0–8 μs). The matched generator absorbs "
           "everything that returns, so the echoes bounce only on line 2, between the junction and the load; each leaks once through line 1. "
           "The two short segments at the bottom left the junction at 7.5 μs.")


if __name__ == "__main__":
    for fn in (fig_mline_bounce, fig_mline_burst, fig_mline_junctions, fig_mline_problem_bounce):
        fn()
