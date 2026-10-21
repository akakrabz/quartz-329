#!/usr/bin/env python3
"""Lecture 26 figures (stand-*) for the ECE 329 notes: standing waves and radiation pressure.

Same helpers and conventions as figs.py (plot helpers from figs_l18.py).
Running this module writes /home/claude/work/figs/<name>.html.
Every curve is computed from its formula with numpy.
Screen frame: X right, Y up, Z out of the screen. In stand-skin-layer the physics axes map as
z (travel, into the mirror) -> screen right, x (E, J) -> screen up, y (H, B) -> out of the screen (odot):
a proper rotation, since right x up = out  <->  z x x = y. Directions checked in digest10/verify_L26.py, section H.
"""
from figs import *
from figs import _odot, _otimes, _sub, _tint
from figs_l18 import lin, poly, _rdp

PI = np.pi
TW = 2 * PI                     # beta * lambda


def _legend_line(x, y, color, dash=None, w=2.2, length=24):
    return line(x, y, x + length, y, stroke=color, w=w, dash=dash)


def _fill(xs, ys, MX, MY, color, op):
    """closed filled polygon, simplified in screen space"""
    pts = _rdp([(float(MX(a)), float(MY(b))) for a, b in zip(xs, ys)], 0.25)
    d = "M" + " L".join(f"{X:.1f},{Y:.1f}" for X, Y in pts)
    return f'<path d="{d} Z" fill="{color}" fill-opacity="{op}" stroke="none"/>'


def _zticks(o, MZ, Y, ticks, size=10):
    for zv, zl in ticks:
        o.append(line(MZ(zv), Y - 3, MZ(zv), Y + 3, w=1.0))
        o.append(text(MZ(zv), Y + 15, zl, size=size, fill="var(--muted)"))


# ------------------------------------------------------------------------------------------------ 1. snapshots
def fig_stand_snapshots():
    W, H = 640, 360
    o = [svg_open(W, H)]
    MZ = lin(-1.25, 0.0, 60, 530)                  # z in units of lambda
    z = np.linspace(-1.25, 0, 900)
    bz = TW * z
    A = 46
    inst = ((0.0, "var(--accent2)", "ωt = 0"), (PI / 4, "var(--hi)", "ωt = π/4"), (PI / 2, "var(--accent)", "ωt = π/2"))
    panels = (
        (110, "a  " + _sub("E", "x") + " / 2" + _sub("E", "0") + " = sin βz · sin ωt", lambda wt: np.sin(bz) * np.sin(wt), np.abs(np.sin(bz)),
         (0.0, -0.5, -1.0), "E nodes"),
        (260, "b  " + _sub("η", "1") + _sub("H", "y") + " / 2" + _sub("E", "0") + " = cos βz · cos ωt", lambda wt: np.cos(bz) * np.cos(wt), np.abs(np.cos(bz)),
         (-0.25, -0.75), "H nodes"),
    )
    for Yc, title, fn, env, nodes, nlab in panels:
        MY = lambda v, Yc=Yc: Yc - A * v
        o.append(text(20, Yc - 58, title, size=12.5, anchor="start", weight=600))
        o.append(_tint(MZ(0), Yc - 52, 70, 104, "var(--muted)", op=0.22))
        o.append(line(MZ(-1.25), Yc, MZ(0) + 70, Yc, w=1.0))
        o.append(line(MZ(0), Yc - 52, MZ(0), Yc + 52, w=2.0))
        for k in range(1, 6):                       # faint lines at multiples of lambda/4
            o.append(line(MZ(-0.25 * k), Yc - 50, MZ(-0.25 * k), Yc + 50, stroke="var(--muted)", w=0.7, dash="2 3"))
        o.append(poly(z, env, MZ, MY, stroke="currentColor", w=1.0, dash="5 4"))
        o.append(poly(z, -env, MZ, MY, stroke="currentColor", w=1.0, dash="5 4"))
        for wt, col, _ in inst:
            o.append(poly(z, fn(wt), MZ, MY, stroke=col, w=2.3))
        for zn in nodes:
            o.append(circle(MZ(zn), Yc, 4.0, fill="currentColor", stroke="none"))
        o.append(text(MZ(0) + 35, Yc - 30, "PEC", size=11.5, weight=600))
        o.append(text(MZ(0) + 35, Yc + 42, "fields 0", size=10.5, fill="var(--muted)"))
        o.append(text(MZ(0) - 6, Yc - 58, "● " + nlab, size=10.5, anchor="end", fill="var(--muted)"))
    # spacing annotations: E nodes lambda/2 apart (panel a), E node to H node lambda/4 (panel b)
    ya = 110 + 64
    o.append(line(MZ(-1.0), ya - 6, MZ(-0.5), ya - 6, w=1.1, arrow=True, small=True))
    o.append(line(MZ(-0.5), ya - 6, MZ(-1.0), ya - 6, w=1.1, arrow=True, small=True))
    o.append(text(MZ(-0.75), ya + 7, "λ/2", size=11))
    yb = 260 + 64
    o.append(line(MZ(-0.5), yb - 6, MZ(-0.25), yb - 6, w=1.1, arrow=True, small=True))
    o.append(line(MZ(-0.25), yb - 6, MZ(-0.5), yb - 6, w=1.1, arrow=True, small=True))
    o.append(text(MZ(-0.375), yb + 7, "λ/4", size=11))
    _zticks(o, MZ, 344, ((0, "0"), (-0.25, "−λ/4"), (-0.5, "−λ/2"), (-0.75, "−3λ/4"), (-1.0, "−λ"), (-1.25, "−5λ/4")))
    o.append(text(MZ(0) + 74, 348, "z", size=12, anchor="start", math=True))
    lx, ly = 360, 22
    for i, (_, col, lab) in enumerate(inst):
        o.append(_legend_line(lx + 92 * i, ly - 4, col, w=2.3, length=20))
        o.append(text(lx + 92 * i + 24, ly, lab, size=11, anchor="start"))
    o.append(svg_close())
    figure("stand-snapshots", "".join(o),
           "<strong>The standing wave in front of a mirror at three instants.</strong> The shape never moves; only its size "
           "oscillates. <b>E</b> is zero everywhere at ωt = 0, when <b>H</b> peaks, and the reverse at ωt = π/2. "
           "Dashed: the envelopes 2<i>E</i><sub>0</sub>|sin βz| and (2<i>E</i><sub>0</sub>/η<sub>1</sub>)|cos βz|.")


# ------------------------------------------------------------------------------------------------ 2. energy
def fig_stand_energy():
    W, H = 640, 330
    o = [svg_open(W, H)]
    MZ = lin(-1.0, 0.0, 70, 560)
    z = np.linspace(-1.0, 0, 800)
    bz = TW * z
    A = 48
    rows = ((90, 0.0, "ωt = 0: all magnetic"), (175, PI / 4, "ωt = π/4: uniform"), (260, PI / 2, "ωt = π/2: all electric"))
    for Yb, wt, lab in rows:
        MY = lambda v, Yb=Yb: Yb - A * v
        wE = np.sin(bz) ** 2 * np.sin(wt) ** 2          # w_E / (2 eps E0^2)
        wH = np.cos(bz) ** 2 * np.cos(wt) ** 2          # w_H / (2 eps E0^2)
        zz = np.concatenate([z, z[::-1]])
        o.append(_fill(zz, np.concatenate([wE, np.zeros_like(wE)]), MZ, MY, "var(--accent)", 0.45))
        o.append(_fill(zz, np.concatenate([wE + wH, wE[::-1]]), MZ, MY, "var(--accent2)", 0.45))
        o.append(poly(z, wE + wH, MZ, MY, stroke="currentColor", w=1.4))
        o.append(line(MZ(-1.0), Yb, MZ(0) + 8, Yb, w=1.0))
        o.append(text(MZ(-1.0), Yb - A - 6, lab, size=11.5, anchor="start", weight=600))
        o.append(_tint(MZ(0), Yb - A - 2, 50, A + 2, "var(--muted)", op=0.22))
        o.append(text(MZ(0) + 25, Yb - 12, "PEC", size=10.5, weight=600))
    for k in range(0, 5):
        X = MZ(-0.25 * k)
        o.append(line(X, 34, X, 262, stroke="var(--muted)", w=0.8, dash="2 3"))
    # S_z ~ sin(2 beta z) sin(2 wt): for 0 < wt < pi/2, sign of sin(2 beta z)
    for zc in (-0.125, -0.375, -0.625, -0.875):
        sgn = np.sign(np.sin(2 * TW * zc))
        X = MZ(zc)
        o.append(arrow(X - 18 * sgn, 297, X + 18 * sgn, 297, stroke="var(--hi)", w=2.0, small=True))
    o.append(text(MZ(-0.5), 318, "S during 0 &lt; ωt &lt; π/2: from H antinodes to E antinodes; S = 0 on the dotted lines", size=11, fill="var(--hi)"))
    _zticks(o, MZ, 262, ((0, "0"), (-0.25, "−λ/4"), (-0.5, "−λ/2"), (-0.75, "−3λ/4"), (-1.0, "−λ")), size=9.5)
    lx, ly = 360, 18
    o.append(rect(lx, ly - 9, 16, 10, fill="var(--accent)", sw=0, opacity=0.6)); o.append(text(lx + 22, ly, "electric " + _sub("w", "E"), size=11, anchor="start"))
    o.append(rect(lx + 110, ly - 9, 16, 10, fill="var(--accent2)", sw=0, opacity=0.6)); o.append(text(lx + 132, ly, "magnetic " + _sub("w", "H"), size=11, anchor="start"))
    o.append(svg_close())
    figure("stand-energy", "".join(o),
           "<strong>Energy density of the standing wave, stacked, in units of 2ε<sub>1</sub><i>E</i><sub>0</sub><sup>2</sup>.</strong> "
           "Each quarter period the energy moves between the <b>H</b> antinodes and the <b>E</b> antinodes. "
           "It never crosses a multiple of λ/4, so each λ/4 cell keeps its energy.")


# ------------------------------------------------------------------------------------------------ 3. partial reflection
def fig_stand_partial():
    W, H = 640, 270
    o = [svg_open(W, H)]
    MZ = lin(-1.0, 0.0, 70, 540)
    MY = lin(0, 2.0, 220, 50)
    z = np.linspace(-1.0, 0, 800)
    cases = ((-1.0, "var(--accent)", None, "Γ = −1 (PEC)"), (-0.5, "var(--hi)", None, "Γ = −1/2"),
             (0.5, "var(--accent2)", "6 4", "Γ = +1/2"), (0.0, "currentColor", "2 3", "Γ = 0 (matched)"))
    o.append(_tint(MZ(0), 44, 70, 176, "var(--muted)", op=0.22))
    o.append(text(MZ(0) + 35, 66, "region 2", size=11, weight=600))
    for yv in (0.5, 1.0, 1.5, 2.0):
        o.append(line(MZ(-1.0), MY(yv), MZ(0), MY(yv), stroke="var(--muted)", w=0.7, dash="3 3"))
        o.append(text(MZ(-1.0) - 6, MY(yv) + 4, f"{yv:g}", size=10.5, anchor="end", fill="var(--muted)"))
    o.append(line(MZ(-1.0), MY(0), MZ(0) + 70, MY(0), w=1.1))
    o.append(line(MZ(0), 44, MZ(0), MY(0), w=2.0))
    o.append(text(MZ(-1.0) - 6, MY(0) + 4, "0", size=10.5, anchor="end", fill="var(--muted)"))
    o.append(text(20, 30, "|" + _sub("Ẽ", "x") + "| / " + _sub("E", "0") + " = |1 + Γ e<tspan baseline-shift=\"super\" style=\"font-size:9px\">j2βz</tspan>| in region 1",
                  size=12.5, anchor="start", weight=600))
    for G, col, dash, lab in cases:
        mag = np.abs(1 + G * np.exp(2j * TW * z))
        o.append(poly(z, mag, MZ, MY, stroke=col, w=2.3, dash=dash))
    lx, ly = 92, 250
    for i, (_, col, dash, lab) in enumerate(cases):
        o.append(_legend_line(lx + 128 * i, ly - 4, col, w=2.3, dash=dash, length=20))
        o.append(text(lx + 128 * i + 24, ly, lab, size=11, anchor="start"))
    _zticks(o, MZ, MY(0), ((0, ""), (-0.25, ""), (-0.5, ""), (-0.75, ""), (-1.0, "")))
    for zv, zl in ((0, "0"), (-0.25, "−λ/4"), (-0.5, "−λ/2"), (-0.75, "−3λ/4"), (-1.0, "−λ")):
        o.append(text(MZ(zv), MY(0) + 15, zl, size=10, fill="var(--muted)"))
    o.append(text(MZ(0) + 74, MY(0) + 4, "z", size=12, anchor="start", math=True))
    o.append(svg_close())
    figure("stand-partial", "".join(o),
           "<strong>The field magnitude in region 1 for four Γ's.</strong> |Γ| &lt; 1 gives ripples between "
           "(1 ± |Γ|)<i>E</i><sub>0</sub> with period λ/2 and no true nulls. A negative Γ puts a minimum at the interface, "
           "a positive one a maximum.")


# ------------------------------------------------------------------------------------------------ 4. skin layer and force
def fig_stand_skin_layer():
    W, H = 640, 300
    o = [svg_open(W, H)]
    # ---- left: directions at the mirror face (drawn at an instant with cos(wt) > 0)
    XF = 170
    o.append(_tint(XF, 40, 120, 210, "var(--muted)", op=0.22))
    o.append(line(XF, 40, XF, 250, w=2.2))
    o.append(text(XF - 75, 30, "vacuum", size=11.5, weight=600))
    o.append(text(XF + 60, 30, "good conductor", size=11.5, weight=600))
    o.append(arrow(40, 70, 130, 70, stroke="currentColor", w=2.0, small=True)); o.append(text(85, 62, "incident", size=10.5, fill="var(--muted)"))
    o.append(arrow(130, 222, 40, 222, stroke="currentColor", w=2.0, small=True)); o.append(text(85, 240, "reflected", size=10.5, fill="var(--muted)"))
    # J along +x (screen up), B along +y (out of screen, odot), J x B = x x y = +z (screen right)
    o.append(arrow(XF + 16, 175, XF + 16, 105, stroke="var(--accent)", w=2.6))
    o.append(text(XF + 28, 112, "J (x̂)", size=12, anchor="start", fill="var(--accent)", weight=600))
    o.append(_odot(XF + 46, 140, r=8, color="var(--accent2)"))
    o.append(text(XF + 58, 160, "B (ŷ)", size=12, anchor="start", fill="var(--accent2)", weight=600))
    o.append(arrow(XF + 34, 205, XF + 104, 205, stroke="var(--hi)", w=2.6))
    o.append(text(XF + 69, 196, "J × B", size=12, fill="var(--hi)", weight=600))
    o.append(text(XF + 60, 268, "half a period later J and B", size=10.5, fill="var(--muted)"))
    o.append(text(XF + 60, 282, "both flip; J × B does not", size=10.5, fill="var(--muted)"))
    tx, ty = 52, 150
    o.append(arrow(tx, ty, tx + 34, ty, stroke="currentColor", w=1.3, small=True)); o.append(text(tx + 40, ty + 4, "z", size=11.5, anchor="start", math=True))
    o.append(arrow(tx, ty, tx, ty - 32, stroke="currentColor", w=1.3, small=True)); o.append(text(tx, ty - 37, "x", size=11.5, math=True))
    o.append(_odot(tx, ty, r=5)); o.append(text(tx - 8, ty + 18, "y", size=11.5, math=True))
    # ---- right: depth profile in units of delta
    MZ = lin(0, 4.0, 360, 610)
    MY = lin(-1.0, 1.0, 230, 70)
    o.append(text(485, 30, "inside, against depth z/δ", size=11.5, weight=600))
    o.append(line(MZ(0), MY(-1.05), MZ(0), MY(1.08), w=1.6))
    o.append(line(MZ(0), MY(0), MZ(4.0) + 6, MY(0), w=1.0, arrow=True, small=True))
    for k in range(1, 5):
        o.append(line(MZ(k), MY(0) - 3, MZ(k), MY(0) + 3, w=1.0)); o.append(text(MZ(k), MY(0) + 15, f"{k}", size=10, fill="var(--muted)"))
    s = np.linspace(0, 4.0, 500)                    # s = z / delta
    fz = np.exp(-2 * s)                             # <f_z>(z) / <f_z>(0)
    o.append(_fill(np.concatenate([s, s[::-1]]), np.concatenate([fz, 0 * fz]), MZ, MY, "var(--hi)", 0.25))
    for wt, op in ((0.0, 1.0), (PI / 2, 0.65), (PI, 0.4), (3 * PI / 2, 0.25)):
        Jz = np.exp(-s) * np.cos(wt - s + PI / 4)   # J_x(z,t) / [ (2E0/eta0) sqrt2/delta ]
        o.append(poly(s, Jz, MZ, MY, stroke="var(--accent)", w=2.0, opacity=op))
    o.append(poly(s, np.exp(-s), MZ, MY, stroke="currentColor", w=1.0, dash="4 3"))
    o.append(poly(s, -np.exp(-s), MZ, MY, stroke="currentColor", w=1.0, dash="4 3"))
    o.append(text(MZ(1.1), MY(0.62), _sub("J", "x") + "(z,t), four instants", size=10.5, anchor="start", fill="var(--accent)"))
    o.append(text(MZ(1.6), MY(0.36), "shaded: ⟨" + _sub("f", "z") + "⟩ ∝ " + "e<tspan baseline-shift=\"super\" style=\"font-size:8px\">−2z/δ</tspan>", size=10.5, anchor="start", fill="var(--hi)"))
    o.append(svg_close())
    figure("stand-skin-layer", "".join(o),
           "<strong>Where the push acts.</strong> Left: <b>J</b> along x̂ and <b>B</b> along ŷ give <b>J</b> × <b>B</b> along +ẑ, into the mirror. "
           "Right: the current decays and lags with depth; its depth integral is <i>J</i><sub>s</sub>(<i>t</i>). "
           "Shaded: the time-averaged force density, total 2⟨<i>S</i><sub>i</sub>⟩/<i>c</i>.")


if __name__ == "__main__":
    for fn in (fig_stand_snapshots, fig_stand_energy, fig_stand_partial, fig_stand_skin_layer):
        fn()
