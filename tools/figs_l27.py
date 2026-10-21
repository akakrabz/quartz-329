#!/usr/bin/env python3
"""Lecture 27 figures (tl-*) for the ECE 329 notes: guided TEM waves on transmission lines.

Same helpers and conventions as figs.py (plot helpers from figs_l18.py).
Running this module writes /home/claude/work/figs/<name>.html. Curves and field lines are computed with numpy.
Screen frame: X right, Y up, Z out of the screen (SVG y runs down; signs below are in the screen frame).
- tl-guided-pulse (side view): physics z -> right, x -> up, y -> out (odot). E up x H out = right = +z.
- tl-cross-sections (looking along +z, into the page): x -> up, y -> right, z -> into the page.
  E up x H right = into the page = +z. Conductor 2 (+, current along +z) is drawn with otimes.
- tl-ladder: wire 2 on top (+), wire 1 below, current along +z (right) on wire 2.
All directions checked with np.cross in digest10/verify_L27.py, section H.
"""
from figs import *
from figs import _odot, _otimes, _sub, _tint, _coil
from figs_l18 import lin, poly, _rdp

PI = np.pi


# ------------------------------------------------------------------------------------------------ 1. a guided pulse
def fig_tl_guided_pulse():
    W, H = 640, 300
    o = [svg_open(W, H)]
    X0, X1 = 150, 620
    MX = lin(0, 1, X0, X1)
    zc, sg = 0.55, 0.12
    f = lambda z: np.exp(-((z - zc) / sg) ** 2)
    YT, YB = 125, 215                                  # plate 1 (x = d) on top, plate 2 (x = 0) below
    YM = (YT + YB) / 2
    # profile of V(z, t0) above the line
    zz = np.linspace(0, 1, 600)
    BASE, AMP = 70, 46
    o.append(line(X0, BASE, X1, BASE, stroke="var(--muted)", w=1.0))
    o.append(poly(zz, f(zz), MX, lambda v: BASE - AMP * v, stroke="currentColor", w=2.2))
    o.append(text(MX(zc) - 70, BASE - AMP - 4, "V(z, t₀) = f(t₀ − z/v)", size=12, anchor="end", math=False))
    o.append(arrow(MX(zc) + 52, BASE - 34, MX(zc) + 108, BASE - 34, stroke="currentColor", w=2.0, small=True))
    o.append(text(MX(zc) + 80, BASE - 42, "v", size=13, math=True))
    # plates
    o.append(line(X0, YT, X1, YT, w=4.5)); o.append(line(X0, YB, X1, YB, w=4.5))
    o.append(text(X0 - 10, YT + 4, "plate 1, x = d", size=12, anchor="end"))
    o.append(text(X0 - 10, YB + 4, "plate 2, x = 0", size=12, anchor="end"))
    # E arrows (up, +x) and H (odot, +y out of the screen) between the plates
    zs = np.arange(0.20, 0.92, 0.05)
    for zk in zs:
        fk = f(zk)
        if fk < 0.12:
            continue
        Lh = max(36 * fk, 9)
        o.append(arrow(MX(zk), YM + Lh, MX(zk), YM - Lh, stroke="var(--accent)", w=1.4 + 1.2 * fk, small=True))
        o.append(text(MX(zk), YB - 8, "+", size=10 + 5 * fk, fill="var(--hi)", weight=700))   # +rho_s on plate 2
        o.append(text(MX(zk), YT + 15, "−", size=10 + 5 * fk, fill="var(--hi)", weight=700))  # -rho_s on plate 1
    for zk in zs[:-1] + 0.025:
        fk = f(zk)
        if fk < 0.15:
            continue
        g = _odot(MX(zk), YM, r=3 + 4 * fk, color="var(--accent2)")
        o.append(f'<g opacity="{0.35 + 0.65 * fk:.2f}">{g}</g>')
    o.append(text(MX(0.80) + 30, YM - 8, _sub("E", "x") + " = V/d", size=12, anchor="start", fill="var(--accent)"))
    o.append(text(MX(0.80) + 30, YM + 12, _sub("H", "y") + " = I/W  (⊙)", size=12, anchor="start", fill="var(--accent2)"))
    # surface currents: plate 2 along +z (right), plate 1 along -z (left); n x H checked in verify section H
    o.append(arrow(MX(zc - 0.12), YB + 14, MX(zc + 0.12), YB + 14, stroke="var(--hi)", w=2.2, small=True))
    o.append(text(MX(zc), YB + 34, "I = " + _sub("H", "y") + "W along +z;   " + _sub("ρ", "s") + " = +ε" + _sub("E", "x"), size=12, fill="var(--hi)"))
    o.append(arrow(MX(zc + 0.12), YT - 12, MX(zc - 0.12), YT - 12, stroke="var(--hi)", w=2.2, small=True))
    o.append(text(MX(zc - 0.13) - 6, YT - 8, "return current;   " + _sub("ρ", "s") + " = −ε" + _sub("E", "x"), size=12, anchor="end", fill="var(--hi)"))
    # axis triad: z right, x up, y out of the screen
    tx, ty = 40, 270
    o.append(arrow(tx, ty, tx + 36, ty, stroke="currentColor", w=1.4, small=True)); o.append(text(tx + 42, ty + 4, "z", size=12, anchor="start", math=True))
    o.append(arrow(tx, ty, tx, ty - 32, stroke="currentColor", w=1.4, small=True)); o.append(text(tx, ty - 38, "x", size=12, math=True))
    o.append(_odot(tx, ty, r=5)); o.append(text(tx + 2, ty + 20, "y (out)", size=11))
    o.append(svg_close())
    figure("tl-guided-pulse", "".join(o),
           "<strong>A pulse V = f(t − z/v) on a parallel-plate line, side view.</strong> <b>E</b> (up) and <b>H</b> (⊙, out of "
           "the page) fill the gap; <b>E</b> × <b>H</b> points along +z. The x = 0 plate carries +ρ<sub>s</sub> and current "
           "along +z, the x = d plate the opposite.")


# ------------------------------------------------------------------------------------------------ 2. three cross-sections
def _segments(xs, ys, keep):
    """split a sampled curve into runs where keep is True"""
    runs, cur = [], []
    for x, y, k in zip(xs, ys, keep):
        if k:
            cur.append((x, y))
        elif cur:
            runs.append(cur); cur = []
    if cur:
        runs.append(cur)
    return [r for r in runs if len(r) > 2]


def _pl(pts, **kw):
    pts = _rdp([(float(x), float(y)) for x, y in pts], 0.3)
    return path("M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts), **kw)


def fig_tl_cross_sections():
    W, H = 640, 290
    o = [svg_open(W, H)]
    CY = 128
    EC, HC = "var(--accent)", "var(--accent2)"
    # ---- parallel plates (centre 110)
    cx = 110; hw, hg = 72, 32                         # half width, half gap (px)
    o.append(text(cx, 30, "parallel plates", size=13, weight=600))
    o.append(rect(cx - hw, CY - hg - 6, 2 * hw, 6, fill="currentColor", stroke="none", opacity=0.55))   # plate 1, x = d
    o.append(rect(cx - hw, CY + hg, 2 * hw, 6, fill="currentColor", stroke="none", opacity=0.55))       # plate 2, x = 0
    for k in range(5):
        X = cx - hw + 16 + k * (2 * hw - 32) / 4
        o.append(arrow(X, CY + hg - 3, X, CY - hg + 4, stroke=EC, w=1.6, small=True))                  # E along +x (up)
    for Yh in (CY - 12, CY + 12):
        o.append(line(cx - hw + 4, Yh, cx + hw - 4, Yh, stroke=HC, w=1.5, dash="5 3"))
        o.append(arrow(cx + 6, Yh, cx + 18, Yh, stroke=HC, w=1.6, small=True))                         # H along +y (right)
    o.append(text(cx - hw - 6, CY + hg + 6, "+", size=15, anchor="end", fill="var(--hi)", weight=700))
    o.append(text(cx - hw - 6, CY - hg + 2, "−", size=15, anchor="end", fill="var(--hi)", weight=700))
    o.append(_otimes(cx + hw + 12, CY + hg + 3, r=5)); o.append(_odot(cx + hw + 12, CY - hg - 3, r=5))
    o.append(text(cx, CY + hg + 24, "W", size=12, math=True))
    o.append(text(cx + hw + 26, CY + 4, "d", size=12, math=True))
    o.append(text(cx, 236, "GF = W/d", size=12.5, weight=600))
    # ---- coax (centre 320)
    cx = 320; a, b = 18, 62
    o.append(text(cx, 30, "coax", size=13, weight=600))
    o.append(circle(cx, CY, b + 5, fill="currentColor", stroke="none", opacity=0.55))
    o.append(circle(cx, CY, b, fill="var(--paper)", stroke="none"))
    o.append(circle(cx, CY, a, fill="currentColor", stroke="none", opacity=0.55))
    for k in range(8):
        ang = k * 2 * PI / 8 + PI / 8
        o.append(arrow(cx + (a + 4) * np.cos(ang), CY + (a + 4) * np.sin(ang), cx + (b - 4) * np.cos(ang), CY + (b - 4) * np.sin(ang), stroke=EC, w=1.5, small=True))
    for rr in (32, 48):
        o.append(circle(cx, CY, rr, stroke=HC, w=1.5, dash="5 3"))
        # current into the page on the core: H clockwise on screen; at the top point it moves right
        o.append(arrow(cx - 5, CY - rr, cx + 7, CY - rr, stroke=HC, w=1.6, small=True))
    o.append(_otimes(cx, CY, r=6, color="var(--paper)"))
    o.append(text(cx - b - 14, CY + 5, "−", size=15, anchor="end", fill="var(--hi)", weight=700))
    o.append(text(cx - 0.707 * (a + 8), CY - 0.707 * (a + 8) + 4, "+", size=13, fill="var(--hi)", weight=700))
    o.append(text(cx, CY + a + 10, "a", size=11, math=True))
    o.append(text(cx, CY + b + 19, "b", size=11, math=True))
    o.append(text(cx, 236, "GF = 2π / ln(b/a)", size=12.5, weight=600))
    # ---- twin-lead (centre 530): wire 2 (+, current into page) left, wire 1 (-, out) right; D/2a = 2.5
    cx = 530; aw = 12.0; hh = 2.5 * aw; s = np.sqrt(hh ** 2 - aw ** 2)
    o.append(text(cx, 30, "twin-lead", size=13, weight=600))
    BX, BY = 96, 78                                   # clip box half sizes (px)
    th = np.linspace(0, 2 * PI, 1441)
    def outside(x, y):
        return ((np.hypot(x + hh, y) > aw + 1.5) & (np.hypot(x - hh, y) > aw + 1.5) & (np.abs(x) < BX) & (np.abs(y) < BY))
    # E lines: circles through (+-s, 0), centres (0, yc); plus the axis segment between the wires
    for yc in (-150, -45, -14, 14, 45, 150):
        R = np.hypot(s, yc)
        x = R * np.cos(th); y = yc + R * np.sin(th)
        for run in _segments(x, y, outside(x, y)):
            o.append(_pl([(cx + p, CY + q) for p, q in run], stroke=EC, w=1.4))
        ytop = yc - R if yc > 0 else yc + R            # crossing of x = 0 nearer the wires
        if abs(ytop) < BY - 4:
            o.append(arrow(cx - 6, CY + ytop, cx + 6, CY + ytop, stroke=EC, w=1.5, small=True))         # E: + (left) to - (right)
    o.append(line(cx - hh + aw + 2, CY, cx + hh - aw - 2, CY, stroke=EC, w=1.4))
    for side in (-1, 1):                               # outer axis parts
        o.append(line(cx + side * (hh + aw + 2), CY, cx + side * BX, CY, stroke=EC, w=1.4))
    # H lines: Apollonius circles around each wire, centre (+-hk, 0), radius rk, hk^2 - rk^2 = s^2
    for rk in (22.0, 42.0):
        hk = np.sqrt(rk ** 2 + s ** 2)
        for side in (-1, 1):
            x = side * hk + rk * np.cos(th); y = rk * np.sin(th)
            keep = (np.abs(x) < BX) & (np.abs(y) < BY)
            for run in _segments(x, y, keep):
                o.append(_pl([(cx + p, CY + q) for p, q in run], stroke=HC, w=1.4, dash="5 3"))
            Xt, Yt = cx + side * hk, CY - rk                # top of the circle (screen)
            if rk < BY - 2:
                # left wire (current into page): clockwise -> moves right at the top; right wire: counterclockwise -> left
                dx = 6 if side < 0 else -6
                o.append(arrow(Xt - dx, Yt, Xt + dx, Yt, stroke=HC, w=1.5, small=True))
    for side, sym, sign in ((-1, _otimes, "+"), (1, _odot, "−")):
        o.append(circle(cx + side * hh, CY, aw, fill="currentColor", stroke="none", opacity=0.55))
        o.append(sym(cx + side * hh, CY, r=5, color="var(--paper)"))
    o.append(text(cx - hh - aw - 5, CY + aw + 8, "+", size=13, anchor="end", fill="var(--hi)", weight=700))
    o.append(text(cx + hh + aw + 5, CY + aw + 8, "−", size=13, anchor="start", fill="var(--hi)", weight=700))
    o.append(text(cx, CY + BY + 14, "wire radius a, centres D apart", size=11, fill="var(--muted)"))
    o.append(text(cx, 236, "GF = π / cosh⁻¹(D/2a)", size=12.5, weight=600))
    # legend and viewing direction
    o.append(line(150, 268, 176, 268, stroke=EC, w=1.6)); o.append(text(182, 272, "E", size=12, anchor="start", weight=700))
    o.append(line(206, 268, 232, 268, stroke=HC, w=1.6, dash="5 3")); o.append(text(238, 272, "H", size=12, anchor="start", weight=700))
    o.append(_otimes(270, 268, r=5)); o.append(text(280, 272, "+z, the travel, into the page;  x up, y right", size=12, anchor="start"))
    o.append(svg_close())
    figure("tl-cross-sections", "".join(o),
           "<strong>Three TEM lines, looking along the travel (+z into the page).</strong> <b>E</b> runs from the + conductor "
           "(current along +z, ⊗) to the − one; <b>H</b> lines are its equipotentials. Same field pattern as statics; "
           "𝓒 = ε·GF, 𝓛 = μ/GF and Z<sub>0</sub> = η/GF.")


# ------------------------------------------------------------------------------------------------ 3. the ladder model
def _cap_v(X, Y1, Y2, color="var(--accent)"):
    """vertical shunt capacitor between wire levels Y1 (top) and Y2 (bottom)"""
    Ym = (Y1 + Y2) / 2
    return (line(X, Y1, X, Ym - 4, w=1.6) + line(X, Ym + 4, X, Y2, w=1.6) +
            line(X - 11, Ym - 4, X + 11, Ym - 4, stroke=color, w=2.4) + line(X - 11, Ym + 4, X + 11, Ym + 4, stroke=color, w=2.4))


def fig_tl_ladder():
    W, H = 640, 240
    o = [svg_open(W, H)]
    YT, YB = 80, 170
    XB = 52                                            # battery
    X0, CW, NC = 92, 84, 6
    Xf = X0 + 3 * CW + 4                               # front after the third cell
    o.append(_tint(X0, YT - 30, Xf - X0, YB - YT + 52, "var(--accent)", op=0.08))
    # battery: long plate (+) on top
    Ym = (YT + YB) / 2
    o.append(line(XB, YT, XB, Ym - 8, w=1.6)); o.append(line(XB, Ym + 2, XB, YB, w=1.6))
    o.append(line(XB - 14, Ym - 8, XB + 14, Ym - 8, w=2.4)); o.append(line(XB - 7, Ym + 2, XB + 7, Ym + 2, w=3.2))
    o.append(line(XB - 14, Ym + 8, XB + 14, Ym + 8, w=2.4, opacity=0));
    o.append(text(XB - 20, Ym - 4, "+", size=13, anchor="end", weight=700)); o.append(text(XB - 20, Ym + 12, "−", size=13, anchor="end", weight=700))
    o.append(text(XB - 20, Ym + 34, _sub("V", "0"), size=13, anchor="end", math=True))
    o.append(line(XB, YT, X0, YT, w=1.6)); o.append(line(XB, YB, X0, YB, w=1.6))
    for k in range(NC):
        xa = X0 + k * CW
        o.append(line(xa, YT, xa + 8, YT, w=1.6))
        o.append(_coil(xa + 8, YT, xa + 52, n=4, r=8))
        o.append(line(xa + 52, YT, xa + CW, YT, w=1.6))
        o.append(_cap_v(xa + 68, YT, YB))
        o.append(line(xa, YB, xa + CW, YB, w=1.6))
        if k < 3:                                      # charged: + on top plate, - below
            o.append(text(xa + 82, Ym - 6, "+", size=11, fill="var(--hi)", weight=700, anchor="end"))
            o.append(text(xa + 82, Ym + 15, "−", size=11, fill="var(--hi)", weight=700, anchor="end"))
    o.append(line(X0 + NC * CW, YT, X0 + NC * CW + 18, YT, w=1.6, dash="3 3")); o.append(line(X0 + NC * CW, YB, X0 + NC * CW + 18, YB, w=1.6, dash="3 3"))
    o.append(text(X0 + NC * CW + 18, YT - 8, "wire 2", size=11, anchor="end", fill="var(--muted)"))
    o.append(text(X0 + NC * CW + 18, YB + 16, "wire 1", size=11, anchor="end", fill="var(--muted)"))
    # labels on cell 1
    o.append(text(X0 + 30, YT - 14, "Δz𝓛", size=12.5, fill="var(--accent)"))
    o.append(text(X0 + 68 - 14, Ym + 4, "Δz𝓒", size=12.5, anchor="end", fill="var(--accent)"))
    o.append(line(X0, YB + 22, X0 + CW, YB + 22, w=1.0)); o.append(line(X0, YB + 17, X0, YB + 27, w=1.0)); o.append(line(X0 + CW, YB + 17, X0 + CW, YB + 27, w=1.0))
    o.append(text(X0 + CW / 2, YB + 38, "Δz ≪ λ", size=12))
    # currents behind the front: along +z on wire 2, back on wire 1
    o.append(arrow(X0 + CW + 4, YT - 24, X0 + CW + 40, YT - 24, stroke="var(--hi)", w=2.0, small=True))
    o.append(text(X0 + CW + 46, YT - 20, "I = " + _sub("V", "0") + "/" + _sub("Z", "0"), size=12, anchor="start", fill="var(--hi)"))
    o.append(arrow(X0 + 2 * CW + 40, YB + 14, X0 + 2 * CW + 4, YB + 14, stroke="var(--hi)", w=2.0, small=True))
    o.append(text(X0 + CW + 50, YB + 38, "V = " + _sub("V", "0"), size=12, fill="var(--hi)"))
    # the front
    o.append(line(Xf, YT - 40, Xf, YB + 30, stroke="currentColor", w=1.4, dash="5 4"))
    o.append(text(Xf, YT - 46, "front, z = vt", size=12))
    o.append(arrow(Xf + 6, YT - 30, Xf + 46, YT - 30, stroke="currentColor", w=1.8, small=True))
    o.append(text(Xf + 26, YT - 34, "v", size=12, math=True))
    o.append(text(Xf + 1.5 * CW, YB + 38, "V = 0, I = 0 (not reached yet)", size=12, fill="var(--muted)"))
    o.append(svg_close())
    figure("tl-ladder", "".join(o),
           "<strong>The distributed-circuit model.</strong> Each Δz ≪ λ of line is a series Δz𝓛 and a shunt Δz𝓒. "
           "After the battery connects at t = 0 the capacitors charge one after another: behind the front z = vt, "
           "V = V<sub>0</sub> and I = V<sub>0</sub>/Z<sub>0</sub>; ahead, nothing yet.")


if __name__ == "__main__":
    for fn in (fig_tl_guided_pulse, fig_tl_cross_sections, fig_tl_ladder):
        fn()
