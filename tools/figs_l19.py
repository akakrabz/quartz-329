#!/usr/bin/env python3
"""Lecture 19 figures (sheet-*) for the ECE 329 notes: d'Alembert solutions and radiation from current sheets.

Same helpers and conventions as figs.py (and the plotting helpers of figs_l18.py).
Running this module writes /home/claude/work/figs/<name>.html.
Direction checks (explicit cross products in digest7/verify_L19.py, section N), screen frame X right, Y up, Z out:
  sheet figures: physics x = up (0,1,0), y = out of the page (0,0,1), z = right (1,0,0)  (right-handed: x cross y = z)
  problem figure: physics x = right, y = up, z = out of the page (worked problem: J_s along +z, out of the page).
  odot = out of the page, otimes = into the page.
"""
from figs import *
from figs import _odot, _otimes, _sub, _tint
from figs_l18 import lin, poly, haxis

def vaxis(X, Y0, Y1, label, ticks, MY, size=10.5):
    """vertical axis (Y0 bottom, Y1 top) with tick labels on the left"""
    s = [line(X, Y0, X, Y1, w=1.2, arrow=True), text(X + 5, Y1 + 4, label, size=12, anchor="start")]
    for tv, tl in ticks:
        Yt = MY(tv)
        s.append(line(X - 3, Yt, X + 3, Yt, w=1.1))
        if tl is not None:
            s.append(text(X - 6, Yt + 4, tl, size=size, anchor="end", fill="var(--muted)"))
    return "".join(s)

def blabels(ticks, MX, Yl, size=10):
    """tick labels on their own baseline (below a panel), so curves never cross them"""
    return "".join(text(MX(tv), Yl, tl, size=size, fill="var(--muted)") for tv, tl in ticks)

# ------------------------------------------------------------------------------------------------ 1. radiated fields
def fig_sheet_radiated_fields():
    W, H = 640, 330
    o = [svg_open(W, H)]
    xs, top, bot, ym = 320, 50, 230, 140
    o.append(text(W / 2, 22, "Notes' orientation: " + _sub("J", "s") + " = x̂ " + _sub("J", "x") + "(t) on the plane z = 0, seen edge-on",
                  size=13, weight=600))
    # the sheet, current UP (+x is up on the page)
    o.append(line(xs, top, xs, bot, stroke="var(--hi)", w=2.6))
    for yy in (62, 112, 162):
        o.append(arrow(xs + 7, yy + 26, xs + 7, yy, stroke="var(--hi)", w=1.6, small=True))
    o.append(text(xs, bot + 18, _sub("J", "s") + " (drawn for " + _sub("J", "x") + " &gt; 0)", size=11.5, fill="var(--hi)", weight=600))
    # E = -x (DOWN) on both sides: opposite to J_s, same on both sides
    for dx in (-48, 48):
        o.append(arrow(xs + dx, 110, xs + dx, 172, stroke="var(--accent)", w=2.6))
    o.append(text(xs + 56, 176, "E", size=14, anchor="start", fill="var(--accent)", weight=700, math=True))
    o.append(text(xs - 56, 176, "E", size=14, anchor="end", fill="var(--accent)", weight=700, math=True))
    # H = 1/2 J_s x n:  z>0 (right): (0,1,0) x (1,0,0) = (0,0,-1) -> into the page (otimes) = -y
    #                   z<0 (left):  (0,1,0) x (-1,0,0) = (0,0,+1) -> out of the page (odot) = +y
    o.append(_otimes(xs + 100, ym, r=8, color="var(--accent2)"))
    o.append(_odot(xs - 100, ym, r=8, color="var(--accent2)"))
    o.append(text(xs + 100, ym - 16, "H", size=14, fill="var(--accent2)", weight=700, math=True))
    o.append(text(xs - 100, ym - 16, "H", size=14, fill="var(--accent2)", weight=700, math=True))
    # travel = E x H: right: (0,-1,0) x (0,0,-1) = (1,0,0) -> right;  left: (0,-1,0) x (0,0,1) = (-1,0,0) -> left
    o.append(arrow(xs + 128, ym, xs + 200, ym, stroke="currentColor", w=3))
    o.append(arrow(xs - 128, ym, xs - 200, ym, stroke="currentColor", w=3))
    o.append(text(xs + 164, ym - 10, "E × H", size=12, weight=600))
    o.append(text(xs - 164, ym - 10, "E × H", size=12, weight=600))
    # region formulas
    o.append(text(xs + 160, 70, "z &gt; 0  (forward wave)", size=12, weight=600))
    o.append(text(xs + 160, 88, "E = −x̂ (η/2) " + _sub("J", "x") + "(t − z/v)", size=11.5))
    o.append(text(xs + 160, 106, "H = −ŷ ½ " + _sub("J", "x") + "(t − z/v)", size=11.5))
    o.append(text(xs - 160, 70, "z &lt; 0  (backward wave)", size=12, weight=600))
    o.append(text(xs - 160, 88, "E = −x̂ (η/2) " + _sub("J", "x") + "(t + z/v)", size=11.5))
    o.append(text(xs - 160, 106, "H = +ŷ ½ " + _sub("J", "x") + "(t + z/v)", size=11.5))
    # boundary-condition footer
    o.append(text(W / 2, 274, "at z = 0:  E continuous (the same on both faces);   ẑ × (H⁺ − H⁻) = " + _sub("J", "s"), size=12, weight=600))
    o.append(text(W / 2, 294, "E opposes " + _sub("J", "s") + "  ⇒  " + _sub("J", "s") + " · E &lt; 0: the sheet gives energy to the two waves", size=11.5, fill="var(--muted)"))
    # axis icon: x up, z right, y out of the page
    ax, ay = 34, 312
    o.append(arrow(ax, ay, ax, ay - 34, stroke="currentColor", w=1.4, small=True)); o.append(text(ax + 7, ay - 28, "x", size=12, anchor="start", math=True))
    o.append(arrow(ax, ay, ax + 34, ay, stroke="currentColor", w=1.4, small=True)); o.append(text(ax + 38, ay + 4, "z", size=12, anchor="start", math=True))
    o.append(_odot(ax, ay, r=5)); o.append(text(ax - 8, ay + 4, "y", size=12, anchor="end", math=True))
    o.append(svg_close())
    figure("sheet-radiated-fields", "".join(o),
           "<strong>What a time-varying current sheet radiates, at one instant while J<sub>x</sub> &gt; 0.</strong> "
           "The page is the xz-plane (x up, z right, y out of the page). Next to the sheet, <b>E</b> points down on "
           "<em>both</em> sides, opposite to the current, with size (η/2)J<sub>x</sub>. <b>H</b> has the Lecture 13 static "
           "pattern, ½<b>J</b><sub>s</sub> × n̂: into the page (⊗) on the right, out of it (⊙) on the left. Check each side "
           "with a cross product: (−x̂) × (−ŷ) = +ẑ on the right and (−x̂) × (+ŷ) = −ẑ on the left, so <b>E</b> × <b>H</b> "
           "points away from the sheet on both faces. That is the direction each wave travels. "
           "Farther out, the fields are the same but delayed by |z|/v. The two jump conditions of Lecture 16 hold at "
           "z = 0: tangential <b>E</b> is continuous and tangential <b>H</b> jumps by J<sub>s</sub>.")

# ------------------------------------------------------------------------------------------------ 2. Example 4
def fig_sheet_ramp_radiation():
    W, H = 640, 520
    o = [svg_open(W, H)]
    # ---- panel 1: the source J_x(t), a ramp from -1 to +1 A/m over |t| < 0.5 us
    MT = lin(-1.2, 1.2, 70, 250); Y1 = 92; A1 = 34
    MY1 = lambda e: Y1 - A1 * e
    o.append(text(20, 22, "1  Source: " + _sub("J", "x") + "(t) = 2t rect(t / 1 µs) A/m  (t in µs)", size=12.5, anchor="start", weight=600))
    tt1 = [(-1, "−1"), (-0.5, "−0.5"), (0.5, "0.5"), (1, "1")]
    o.append(haxis(58, 262, Y1, "t", tt1, MT, tick_labels=False)); o.append(blabels(tt1, MT, Y1 + A1 + 14))
    o.append(text(262, Y1 + A1 + 14, "µs", size=10.5, anchor="start", fill="var(--muted)"))
    o.append(poly([-1.2, -0.5, -0.5, 0.5, 0.5, 1.2], [0, 0, -1, 1, 0, 0], MT, MY1, stroke="var(--hi)", w=2.4))
    o.append(text(MT(0.5) + 6, MY1(1) + 4, "+1 A/m", size=10.5, anchor="start", fill="var(--hi)"))
    o.append(text(MT(-0.5) - 6, MY1(-1) + 2, "−1 A/m", size=10.5, anchor="end", fill="var(--hi)"))
    o.append(text(330, 58, "At t = 2 µs each wave has travelled", size=11.5, anchor="start"))
    o.append(text(330, 74, "c × 2 µs = 600 m from the sheet.", size=11.5, anchor="start"))
    o.append(text(330, 96, "The source ramp (1 µs long) becomes a", size=11.5, anchor="start", fill="var(--muted)"))
    o.append(text(330, 112, "300 m long ramp on each side.", size=11.5, anchor="start", fill="var(--muted)"))
    MZ = lin(-950, 950, 52, 600)
    zt = [(-900, "−900"), (-600, "−600"), (-300, "−300"), (0, "0"), (300, "300"), (600, "600"), (900, "900")]
    def sheet_mark(Ytop, Ybot):
        o.append(line(MZ(0), Ytop, MZ(0), Ybot, stroke="var(--hi)", w=2, dash="4 3"))
    # ---- panel 2: H_y(z, 2 us)
    Y2 = 246; A2 = 90
    MY2 = lambda h: Y2 - A2 * h
    o.append(text(20, 156, "2  " + _sub("H", "y") + "(z, 2 µs): odd in z (it flips across the sheet)", size=12.5, anchor="start", weight=600))
    sheet_mark(MY2(0.62), MY2(-0.62))
    o.append(haxis(40, 610, Y2, "z", zt, MZ, tick_labels=False))
    o.append(blabels(zt, MZ, Y2 + 0.5 * A2 + 20)); o.append(text(612, Y2 + 0.5 * A2 + 20, "m", size=10.5, anchor="start", fill="var(--muted)"))
    zs = [-950, -750, -750, -450, -450, 450, 450, 750, 750, 950]
    o.append(poly(zs, [0, 0, -0.5, 0.5, 0, 0, -0.5, 0.5, 0, 0], MZ, MY2, stroke="var(--accent2)", w=2.6))
    for hv, lab in ((0.5, "+0.5"), (-0.5, "−0.5")):
        o.append(line(MZ(-950), MY2(hv), MZ(-950) + 6, MY2(hv), w=1.0))
        o.append(text(MZ(-950) + 9, MY2(hv) + 4, lab + " A/m", size=10.5, anchor="start", fill="var(--muted)"))
    o.append(text(MZ(0) + 8, MY2(0.36), "z &gt; 0:", size=11, anchor="start", fill="var(--accent2)"))
    o.append(text(MZ(0) + 8, MY2(0.36) + 14, "−½ " + _sub("J", "x") + "(t − z/c)", size=11, anchor="start", fill="var(--accent2)"))
    o.append(text(MZ(0) - 8, MY2(0.36), "z &lt; 0:", size=11, anchor="end", fill="var(--accent2)"))
    o.append(text(MZ(0) - 8, MY2(0.36) + 14, "+½ " + _sub("J", "x") + "(t + z/c)", size=11, anchor="end", fill="var(--accent2)"))
    o.append(text(MZ(0) + 6, MY2(0.56), "sheet", size=10.5, anchor="start", fill="var(--hi)"))
    # ---- panel 3: E_x(z, 2 us)
    Y3 = 414; A3 = 90
    MY3 = lambda e: Y3 - A3 * e      # e in units of 60 pi V/m
    o.append(text(20, 326, "3  " + _sub("E", "x") + "(z, 2 µs): even in z, and opposite to the source", size=12.5, anchor="start", weight=600))
    sheet_mark(MY3(0.62), MY3(-0.62))
    o.append(haxis(40, 610, Y3, "z", zt, MZ, tick_labels=False))
    o.append(blabels(zt, MZ, Y3 + 0.5 * A3 + 20)); o.append(text(612, Y3 + 0.5 * A3 + 20, "m", size=10.5, anchor="start", fill="var(--muted)"))
    o.append(poly(zs, [0, 0, 0.5, -0.5, 0, 0, -0.5, 0.5, 0, 0], MZ, MY3, stroke="var(--accent)", w=2.6))
    for ev, lab in ((0.5, "+60π"), (-0.5, "−60π")):
        o.append(line(MZ(-950), MY3(ev), MZ(-950) + 6, MY3(ev), w=1.0))
        o.append(text(MZ(-950) + 9, MY3(ev) + 4, lab + " V/m", size=10.5, anchor="start", fill="var(--muted)"))
    o.append(text(MZ(0), H - 10, _sub("E", "x") + " = −(η₀/2) " + _sub("J", "x") + "(t − |z|/c) on both sides;  peak 60π ≈ 188 V/m", size=11.5, weight=600))
    o.append(svg_close())
    figure("sheet-ramp-radiation", "".join(o),
           "<strong>The notes' Example 4: a ramp of sheet current and the two waves it launches, at t = 2 µs.</strong> "
           "Panel 1 is the source. Panels 2 and 3 are snapshots computed from H<sub>y</sub> = ∓½J<sub>x</sub>(t ∓ z/c) and "
           "E<sub>x</sub> = −(η₀/2)J<sub>x</sub>(t ∓ z/c). Both waves are shifted, rescaled copies of the source, 600 m from "
           "the sheet. On the right the ramp is mirrored, because a +z wave lays the time record out backwards in space. On "
           "the left it keeps its order. E<sub>x</sub> is the same function of |z| on both sides, so it is continuous at the "
           "sheet. H<sub>y</sub> changes sign across it, so it jumps there by J<sub>x</sub>. Pick any point and check: at "
           "z = +700 m, E<sub>x</sub> &gt; 0 and H<sub>y</sub> &gt; 0, and x̂ × ŷ = +ẑ points away from the sheet.")

# ------------------------------------------------------------------------------------------------ 3. slide 11, z-t diagram
def fig_sheet_space_time():
    W, H = 640, 660
    o = [svg_open(W, H)]
    zp = np.array([-100, 0, 100, 300, 400.]); Fp = np.array([0, 1, -1, 0, 0.])
    names = ["A", "B", "C", "D", "E"]
    # ---- panel 1: z-t diagram. World lines of a +z wave at 100 m/s: z = z0 + 100 t (positive slope in the z-t plane)
    MZ = lin(-150, 550, 80, 590); MT = lin(-4.4, 3.4, 268, 44)
    o.append(text(20, 18, "1  z–t diagram: every feature rides a world line z = z₀ + (100 m/s) t", size=12.5, anchor="start", weight=600))
    o.append(rect(MZ(-150), MT(3.4), MZ(550) - MZ(-150), MT(-4.4) - MT(3.4), stroke="var(--muted)", sw=0.8))
    for tv in range(-4, 4):
        o.append(line(MZ(-150) - 3, MT(tv), MZ(-150), MT(tv), w=1))
        o.append(text(MZ(-150) - 6, MT(tv) + 4, f"{tv}".replace("-", "−"), size=10, anchor="end", fill="var(--muted)"))
    o.append(text(MZ(-150) - 30, MT(3.4) + 6, "t (s)", size=11, anchor="middle"))
    for zv in range(-100, 501, 100):
        o.append(line(MZ(zv), MT(-4.4), MZ(zv), MT(-4.4) + 3, w=1))
        o.append(text(MZ(zv), MT(-4.4) + 15, f"{zv}".replace("-", "−"), size=10, fill="var(--muted)"))
    o.append(text(MZ(550) + 4, MT(-4.4) + 15, "z (m)", size=11, anchor="start"))
    # given line t = 0, target lines t = 1 s (a), z = 0 (b), z = 200 m (c)
    o.append(line(MZ(-150), MT(0), MZ(550), MT(0), stroke="currentColor", w=2.2))
    o.append(text(MZ(550) - 4, MT(0) + 14, "given: t = 0", size=10.5, anchor="end", weight=600))
    o.append(line(MZ(-150), MT(1), MZ(550), MT(1), stroke="var(--accent)", w=1.6, dash="6 4"))
    o.append(text(MZ(550) - 4, MT(1) - 5, "(a) t = 1 s", size=10.5, anchor="end", fill="var(--accent)", weight=600))
    o.append(line(MZ(0), MT(-4.4), MZ(0), MT(3.4), stroke="var(--accent2)", w=1.6, dash="6 4"))
    o.append(text(MZ(0) - 4, MT(3.4) - 5, "(b) z = 0", size=10.5, anchor="end", fill="var(--accent2)", weight=600))
    o.append(line(MZ(200), MT(-4.4), MZ(200), MT(3.4), stroke="var(--hi)", w=1.6, dash="6 4"))
    o.append(text(MZ(200) + 4, MT(3.4) - 5, "(c) z = 200 m", size=10.5, anchor="start", fill="var(--hi)", weight=600))
    for z0, nm in zip(zp, names):
        t0 = max(-4.4, (-150 - z0) / 100); t1 = min(3.4, (550 - z0) / 100)
        o.append(line(MZ(z0 + 100 * t0), MT(t0), MZ(z0 + 100 * t1), MT(t1), stroke="var(--muted)", w=1.3))
        o.append(circle(MZ(z0), MT(0), 3.5, fill="currentColor", stroke="none"))
        o.append(text(MZ(z0) + 5, MT(0) - 5, nm, size=11.5, anchor="start", weight=700))
        # intersections with the three target lines
        o.append(circle(MZ(z0 + 100), MT(1), 3.2, fill="var(--accent)", stroke="none"))
        tb = -z0 / 100
        if -4.4 <= tb <= 3.4:
            o.append(circle(MZ(0), MT(tb), 3.2, fill="var(--accent2)", stroke="none"))
        tc = (200 - z0) / 100
        if -4.4 <= tc <= 3.4:
            o.append(circle(MZ(200), MT(tc), 3.2, fill="var(--hi)", stroke="none"))
    # ---- panel 2: E(z,0) (given, dashed) and E(z,1 s) (a)
    MZ2 = lin(-150, 550, 80, 590); Y2 = 362; A2 = 38
    MY2 = lambda e: Y2 - A2 * e
    o.append(text(20, 306, "2  (a) the snapshot at t = 1 s is the given one slid 100 m toward +z", size=12.5, anchor="start", weight=600))
    zt2 = [(k, f"{k}".replace("-", "−")) for k in range(-100, 501, 100)]
    o.append(haxis(68, 600, Y2, "z", zt2, MZ2, tick_labels=False)); o.append(blabels(zt2, MZ2, Y2 + A2 + 16))
    o.append(text(602, Y2 + A2 + 16, "m", size=10.5, anchor="start", fill="var(--muted)"))
    o.append(poly([-150, *zp, 550], [0, *Fp, 0], MZ2, MY2, stroke="var(--muted)", w=2, dash="5 4"))
    o.append(poly([-150, *(zp + 100), 550], [0, *Fp, 0], MZ2, MY2, stroke="var(--accent)", w=2.6))
    o.append(text(MZ2(-70) - 8, MY2(0.75), "t = 0", size=10.5, anchor="end", fill="var(--muted)"))
    o.append(text(MZ2(100) + 8, MY2(1) + 4, "t = 1 s", size=10.5, anchor="start", fill="var(--accent)", weight=600))
    for ev, lab in ((1, "+1"), (-1, "−1")):
        o.append(line(MZ2(-150) - 3, MY2(ev), MZ2(-150) + 3, MY2(ev), w=1)); o.append(text(MZ2(-150) - 6, MY2(ev) + 4, lab, size=10, anchor="end", fill="var(--muted)"))
    # ---- panel 3: E(0,t) (b) and E(200 m,t) (c)
    MT3 = lin(-5, 4, 80, 590); Y3 = 548; A3 = 38
    MY3 = lambda e: Y3 - A3 * e
    o.append(text(20, 470, "3  (b) the record at z = 0 and (c) the record at z = 200 m: the profile reversed in time", size=12.5, anchor="start", weight=600))
    tt3 = [(k, f"{k}".replace("-", "−")) for k in range(-5, 5)]
    o.append(haxis(68, 600, Y3, "t", tt3, MT3, tick_labels=False)); o.append(blabels(tt3, MT3, Y3 + A3 + 16))
    o.append(text(602, Y3 + A3 + 16, "s", size=10.5, anchor="start", fill="var(--muted)"))
    o.append(poly([-5, -4, -3, -1, 0, 1, 4], [0, 0, 0, -1, 1, 0, 0], MT3, MY3, stroke="var(--accent2)", w=2.6))
    o.append(poly([-5, -2, -1, 1, 2, 3, 4], [0, 0, 0, -1, 1, 0, 0], MT3, MY3, stroke="var(--hi)", w=2.4, dash="7 3"))
    o.append(text(MT3(0) - 6, MY3(1) - 4, "(b) E(0, t)", size=10.5, anchor="end", fill="var(--accent2)", weight=600))
    o.append(text(MT3(2) + 6, MY3(1) - 4, "(c) E(200 m, t)", size=10.5, anchor="start", fill="var(--hi)", weight=600))
    for ev, lab in ((1, "+1"), (-1, "−1")):
        o.append(line(MT3(-5) - 3, MY3(ev), MT3(-5) + 3, MY3(ev), w=1)); o.append(text(MT3(-5) - 6, MY3(ev) + 4, lab, size=10, anchor="end", fill="var(--muted)"))
    o.append(text(W / 2, H - 24, "B (the +1 peak) reaches z = 0 at t = 0 and z = 200 m at t = 2 s;  E and D (the front) cross first, A last", size=11.5))
    o.append(text(W / 2, H - 6, "E(200 m, t) = E(0, t − 2 s): the same record, 2 s later", size=11, fill="var(--muted)"))
    o.append(svg_close())
    figure("sheet-space-time", "".join(o),
           "<strong>Slide 11, \"transforming time and space\", done with a z–t diagram.</strong> A wave moving toward +z at "
           "100 m/s is given at t = 0 (panel 2, dashed): a piecewise-linear profile with corners A–E at z = −100, 0, 100, 300 "
           "and 400 m. Each corner keeps its value along its world line z = z₀ + 100t, which has positive slope in the z–t "
           "plane (the slide's ink: \"+ slope\"). To answer any question, follow the world lines from the given line to the "
           "target line. (a) The horizontal line t = 1 s gives the same profile 100 m to the right. (b) The vertical line "
           "z = 0 gives a time record: A arrives at t = +1 s, but C, D and E crossed at t = −1, −3 and −4 s, so the record "
           "is the profile reversed. (c) The line z = 200 m gives the same record 2 s later. Parts (a) and (b) are worked in "
           "ink in the deck; (c) is left to the student and solved here.")

# ------------------------------------------------------------------------------------------------ 4. worked problem
def fig_sheet_problem_snapshot():
    W, H = 640, 590
    o = [svg_open(W, H)]
    # ---- panel 1: J_s(t), ns
    MT = lin(-0.6, 5.6, 70, 330); Y1 = 100; A1 = 9.0
    MY1 = lambda j: Y1 - A1 * j
    o.append(text(20, 22, "1  Source: " + _sub("J", "s") + " = ẑ " + _sub("J", "s") + "(t) on the plane x = 0", size=12.5, anchor="start", weight=600))
    tt1 = [(k, f"{k}") for k in range(0, 6)]
    o.append(haxis(58, 342, Y1, "t", tt1, MT, tick_labels=False)); o.append(blabels(tt1, MT, Y1 + 2 * A1 + 16))
    o.append(text(342, Y1 + 2 * A1 + 16, "ns", size=10.5, anchor="start", fill="var(--muted)"))
    o.append(poly([-0.6, 0, 2, 2, 4, 4, 5.6], [0, 0, 6, -2, -2, 0, 0], MT, MY1, stroke="var(--hi)", w=2.4))
    o.append(text(MT(2) + 6, MY1(6) + 4, "6 A/m", size=10.5, anchor="start", fill="var(--hi)"))
    o.append(text(MT(4) + 6, MY1(-2) + 4, "−2 A/m", size=10.5, anchor="start", fill="var(--hi)"))
    o.append(text(372, 52, _sub("ε", "r") + " = 4:  v = 0.15 m/ns,  η ≈ 188 Ω", size=11.5, anchor="start"))
    o.append(text(372, 70, "At t = 6 ns the t = 0 front is 0.9 m out,", size=11.5, anchor="start"))
    o.append(text(372, 86, "the 2 ns step 0.6 m, the 4 ns end 0.3 m.", size=11.5, anchor="start"))
    MX = lin(-1.15, 1.15, 52, 600)
    xt = [(k / 10, (f"{k/10:.1f}" if k else "0").replace("-", "−")) for k in range(-9, 10, 3)]
    # ---- panel 2: H_y(x, 6 ns) = +-1/2 J_s(t -+ x/v)
    Y2 = 242; A2 = 20
    MY2 = lambda h: Y2 - A2 * h
    o.append(text(20, 150, "2  " + _sub("H", "y") + "(x, 6 ns): odd in x", size=12.5, anchor="start", weight=600))
    o.append(line(MX(0), MY2(3.5), MX(0), MY2(-3.5), stroke="var(--hi)", w=2, dash="4 3"))
    o.append(haxis(40, 610, Y2, "x", xt, MX, tick_labels=False))
    o.append(blabels(xt, MX, Y2 + 3 * A2 + 16)); o.append(text(612, Y2 + 3 * A2 + 16, "m", size=10.5, anchor="start", fill="var(--muted)"))
    xs = [-1.15, -0.9, -0.6, -0.6, -0.3, -0.3, 0.3, 0.3, 0.6, 0.6, 0.9, 1.15]
    hz = [0, 0, -3, 1, 1, 0, 0, -1, -1, 3, 0, 0]
    o.append(poly(xs, hz, MX, MY2, stroke="var(--accent2)", w=2.6))
    for hv, lab in ((3, "+3"), (1, "+1"), (-1, "−1"), (-3, "−3")):
        o.append(line(MX(-1.15), MY2(hv), MX(-1.15) + 6, MY2(hv), w=1.0))
        o.append(text(MX(-1.15) + 9, MY2(hv) + 4, lab, size=10, anchor="start", fill="var(--muted)"))
    o.append(text(MX(-1.15) + 30, MY2(3) + 4, "A/m", size=10, anchor="start", fill="var(--muted)"))
    o.append(text(MX(0.9) + 6, MY2(1.2), "front", size=10.5, anchor="start", fill="var(--accent2)"))
    o.append(text(MX(-0.9) - 4, MY2(0.6), "front", size=10.5, anchor="end", fill="var(--accent2)"))
    o.append(text(MX(0) + 6, MY2(3.2), "sheet", size=10.5, anchor="start", fill="var(--hi)"))
    # ---- panel 3: E_z(x, 6 ns) = -(eta/2) J_s(t - |x|/v)
    Y3 = 384; A3 = 0.13
    MY3 = lambda e: Y3 - A3 * e
    o.append(text(20, 344, "3  " + _sub("E", "z") + "(x, 6 ns): even in x, opposite to the source", size=12.5, anchor="start", weight=600))
    o.append(line(MX(0), MY3(600), MX(0), MY3(-600), stroke="var(--hi)", w=2, dash="4 3"))
    o.append(haxis(40, 610, Y3, "x", xt, MX, tick_labels=False))
    o.append(blabels(xt, MX, Y3 + 3 * 188.4 * A3 + 16)); o.append(text(612, Y3 + 3 * 188.4 * A3 + 16, "m", size=10.5, anchor="start", fill="var(--muted)"))
    eta = 188.365
    ey = [0, 0, -3 * eta, eta, eta, 0, 0, eta, eta, -3 * eta, 0, 0]
    o.append(poly(xs, ey, MX, MY3, stroke="var(--accent)", w=2.6))
    for ev, lab in ((eta, "+188"), (-3 * eta, "−565")):
        o.append(line(MX(-1.15), MY3(ev), MX(-1.15) + 6, MY3(ev), w=1.0))
        o.append(text(MX(-1.15) + 9, MY3(ev) + 4, lab + " V/m", size=10, anchor="start", fill="var(--muted)"))
    # geometry icon: x right, y up, z out of the page; J_s = +z (odot on the sheet) for J_s > 0:
    # x>0: 1/2 J x n = 1/2 (0,0,1) x (1,0,0) = (0,+1/2,0) -> up;  x<0: (0,0,1) x (-1,0,0) = (0,-1,0) -> down
    # E = -(eta/2) J -> (0,0,-1) -> otimes on both sides;  E x H: (0,0,-1) x (0,1,0) = (1,0,0) right; (0,0,-1) x (0,-1,0) = (-1,0,0) left
    gx, gy = 470, 540
    for ya, yb in ((-26, -15.5), (-4.5, 2.5), (13.5, 22)):
        o.append(line(gx, gy + ya, gx, gy + yb, stroke="var(--hi)", w=2.2))
    o.append(_odot(gx, gy - 10, r=4.5, color="var(--hi)")); o.append(_odot(gx, gy + 8, r=4.5, color="var(--hi)"))
    o.append(arrow(gx + 30, gy + 12, gx + 30, gy - 14, stroke="var(--accent2)", w=2, small=True))
    o.append(arrow(gx - 30, gy - 14, gx - 30, gy + 12, stroke="var(--accent2)", w=2, small=True))
    o.append(_otimes(gx + 52, gy, r=5, color="var(--accent)")); o.append(_otimes(gx - 52, gy, r=5, color="var(--accent)"))
    o.append(text(gx + 52, gy + 18, "E", size=10.5, fill="var(--accent)", weight=700)); o.append(text(gx - 52, gy + 18, "E", size=10.5, fill="var(--accent)", weight=700))
    o.append(text(gx + 30, gy + 26, "H", size=10.5, fill="var(--accent2)", weight=700)); o.append(text(gx - 30, gy + 26, "H", size=10.5, fill="var(--accent2)", weight=700))
    o.append(text(gx + 64, gy + 4, "x &gt; 0", size=10.5, anchor="start", fill="var(--muted)"))
    o.append(text(gx - 64, gy + 4, "x &lt; 0", size=10.5, anchor="end", fill="var(--muted)"))
    o.append(text(gx, gy + 42, _sub("J", "s") + " ⊙ for " + _sub("J", "s") + " &gt; 0 (x right, y up, z out)", size=10, fill="var(--muted)"))
    o.append(text(20, 540, "Level check:", size=11, anchor="start", weight=600))
    o.append(text(20, 558, _sub("E", "z") + " = −(η/2) " + _sub("J", "s") + ",  " + _sub("H", "y") + " = ±½ " + _sub("J", "s"), size=11, anchor="start"))
    o.append(svg_close())
    figure("sheet-problem-snapshot", "".join(o),
           "<strong>The worked problem's sheet current and the two waves at t = 6 ns.</strong> Panel 1 is the source. The "
           "panels below are snapshots from H<sub>y</sub> = ±½J<sub>s</sub>(t ∓ x/v) and E<sub>z</sub> = −(η/2)J<sub>s</sub>(t ∓ x/v) "
           "with v = 0.15 m/ns. Read panel 2 from the outside in. The front (the t = 0 start of the ramp) is 0.9 m out on each "
           "side. Next comes the ramp, up to 6 A/m of source current (|H| = 3 A/m) at 0.6 m, then the −2 A/m plateau (|H| = 1 A/m). "
           "Nothing remains within 0.3 m of the sheet, because the source switched off at 4 ns. On the right the ramp is mirrored "
           "in space. H<sub>y</sub> has opposite signs on the two sides (odd), E<sub>z</sub> the same sign (even). The icon shows "
           "the fields next to the sheet while J<sub>s</sub> &gt; 0 (current out of the page, ⊙): <b>H</b> = ½ẑ × x̂ = +½ŷ (up) on the right "
           "and down on the left; <b>E</b> into the page (⊗) on both sides; (−ẑ) × ŷ = +x̂, away from the sheet.")

if __name__ == "__main__":
    for fn in (fig_sheet_radiated_fields, fig_sheet_ramp_radiation, fig_sheet_space_time, fig_sheet_problem_snapshot):
        fn()
