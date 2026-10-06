#!/usr/bin/env python3
"""Figures for Lecture 17 (magnetization, Maxwell's equations in matter): mag-*.

Same helpers and conventions as figs.py (currentColor + CSS variables, no blank lines).
Screen frame for every direction check: x right, y up, z out of the screen;
odot = out of the page, otimes = into the page.  The cross products quoted in the
comments are verified in digest6/verify_L17.py (sections A4, C1, C3, G5, I-fig).
Run:  python3 figs_l17.py   ->  writes /home/claude/work/figs/mag-*.html
"""
import math
import numpy as np
from figs import *
from figs import _odot, _otimes, _sub, _tint


def _arc(cx, cy, r, a0, a1, color="currentColor", w=1.6, arrow_end=False, dash=None):
    """circular arc from math angle a0 to a1 (degrees, counter-clockwise on screen if a1 > a0)."""
    pts = []
    n = max(8, int(abs(a1 - a0) / 3))
    for k in range(n + 1):
        t = math.radians(a0 + (a1 - a0) * k / n)
        pts.append((cx + r * math.cos(t), cy - r * math.sin(t)))
    return path("M" + " L".join(f"{X:.1f},{Y:.1f}" for X, Y in pts), stroke=color, w=w, arrow=arrow_end, dash=dash)


# --------------------------------------------------------------------------- 1. atomic moment, torque, alignment
def fig_mag_moment_torque():
    W, H = 640, 300
    o = [svg_open(W, H)]
    # ---- panel A: an orbit is a current loop
    cx, cy, rx, ry = 105, 150, 72, 24
    o.append(text(cx, 24, "an orbit is a current loop", size=12.5, weight=600, fill="var(--accent)"))
    o.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="var(--accent2)" fill-opacity="0.10" stroke="currentColor" stroke-width="1.6"/>')
    o.append(arrow(cx, cy - 12, cx, 50, stroke="var(--accent2)", w=2.6))
    o.append(text(cx + 8, 60, "m = I A", size=12.5, anchor="start", fill="var(--accent2)", weight=600))
    o.append(charge(cx, cy, "+", r=8))
    o.append(text(cx + 44, cy + 5, "A", size=12, math=True, fill="var(--muted)"))
    # electron on the near (lower) side moving LEFT; conventional current on the near side points RIGHT.
    # page frame of this panel: x right, z up, viewer at -y, so the near side is y = -a.
    # right-hand rule: z x (-y) = +x, so a +x current on the near side means m along +z (up)   [verify A2]
    o.append(charge(cx, cy + ry, "-", r=6, fill="var(--accent)"))
    o.append(arrow(cx - 8, cy + ry + 16, cx - 46, cy + ry + 16, stroke="var(--accent)", w=1.8, small=True))
    o.append(text(cx - 50, cy + ry + 20, "v", size=12, math=True, anchor="end", fill="var(--accent)"))
    pts = []
    for k in range(13):
        t = math.radians(82 - 40 * k / 12)               # SVG ellipse parameter: 90 deg = bottom (near side)
        pts.append((cx + rx * math.cos(t), cy + ry * math.sin(t)))
    o.append(path("M" + " L".join(f"{X:.1f},{Y:.1f}" for X, Y in pts), stroke="var(--hi)", w=2.6, arrow=True))
    o.append(text(cx + 58, cy + ry + 14, "I", size=13, math=True, fill="var(--hi)", weight=600))
    o.append(text(cx, 222, "I flows opposite to the electron's v", size=11))
    o.append(text(cx, 238, "m ⟂ loop by the right-hand rule", size=11))
    o.append(text(cx, 262, "spin: a built-in moment ≈ μ" + _sub("", "B"), size=11, fill="var(--muted)"))
    # ---- panel B: a tilted loop in a uniform B0
    bx, by, half, th = 320, 140, 58, math.radians(35)
    o.append(text(bx, 24, "a field turns it: T = m × B₀", size=12.5, weight=600, fill="var(--accent)"))
    for X0 in (222, 418):
        o.append(arrow(X0, 198, X0, 44, stroke="var(--muted)", w=1.4))
    o.append(text(412, 52, "B₀", size=12.5, anchor="end", fill="var(--muted)", weight=600))
    deg = math.degrees(th)
    o.append(f'<ellipse cx="{bx}" cy="{by}" rx="{half}" ry="8" transform="rotate({deg:.1f} {bx} {by})" fill="var(--accent2)" fill-opacity="0.10" stroke="currentColor" stroke-width="1.6"/>')
    # ends of the edge-on loop: P_R lower right, P_L upper left (SVG y down)
    PRx, PRy = bx + half * math.cos(th), by + half * math.sin(th)
    PLx, PLy = bx - half * math.cos(th), by - half * math.sin(th)
    # m tilted right of vertical: m_hat = (sin th, cos th) in the screen frame.
    # current at P_R: m x r_R = (sin,cos,0) x (cos,-sin,0) = -z  -> otimes ; at P_L: +z -> odot   [verify A4]
    o.append(_otimes(PRx, PRy, r=7, color="var(--hi)"))
    o.append(_odot(PLx, PLy, r=7, color="var(--hi)"))
    # forces I dl x B0 with B0 = +y:  (-z) x y = +x at P_R (right) ; (+z) x y = -x at P_L (left)        [verify A4]
    o.append(arrow(PRx + 10, PRy, PRx + 40, PRy, stroke="var(--hi)", w=2.2))
    o.append(text(PRx + 26, PRy - 9, "F", size=13, math=True, fill="var(--hi)", weight=600))
    o.append(arrow(PLx - 10, PLy, PLx - 40, PLy, stroke="var(--hi)", w=2.2))
    o.append(text(PLx - 26, PLy - 9, "F", size=13, math=True, fill="var(--hi)", weight=600))
    mx, my = bx + 74 * math.sin(th), by - 74 * math.cos(th)
    o.append(line(bx, by, bx, by - 70, dash="4 3", w=1.1, opacity=0.6))
    o.append(arrow(bx, by, mx, my, stroke="var(--accent2)", w=2.6))
    o.append(text(mx + 6, my + 4, "m", size=13, math=True, anchor="start", fill="var(--accent2)", weight=600))
    o.append(_arc(bx, by, 26, 90 - deg, 90, color="currentColor", w=1.1))
    o.append(text(bx + 8, by - 32, "θ", size=12, math=True, anchor="start"))
    # torque T = m x B0 = +z (out of the screen): counter-clockwise rotation, drawn below the loop      [verify A4]
    o.append(_arc(bx, by, 36, 200, 292, color="currentColor", w=1.6, arrow_end=True))
    o.append(text(bx - 30, by + 50, "T", size=13, math=True, anchor="end", weight=600))
    o.append(text(bx, 222, "I dl × B₀ on opposite sides: equal,", size=11))
    o.append(text(bx, 238, "opposite and offset — a couple", size=11))
    o.append(text(bx, 262, "T = m × B₀ (⊙ here): m turns to B₀", size=11, fill="var(--muted)"))
    # ---- panel C: random vs aligned
    rng = np.random.default_rng(7)
    def box(y0, title, aligned):
        o.append(text(538, y0 - 8, title, size=11.5, weight=600))
        o.append(rect(452, y0, 172, 92, stroke="currentColor", sw=1.2, rx=4))
        for i in range(5):
            for j in range(3):
                X0, Y0 = 470 + i * 34, y0 + 18 + j * 28
                ang = rng.uniform(0, 2 * math.pi) if not aligned else math.pi / 2 + rng.uniform(-0.45, 0.45)
                dx, dy = 11 * math.cos(ang), -11 * math.sin(ang)
                o.append(circle(X0, Y0, 2.4, fill="var(--accent2)", stroke="none", opacity=0.7))
                o.append(arrow(X0 - dx * 0.6, Y0 - dy * 0.6, X0 + dx, Y0 + dy, stroke="var(--accent2)", w=1.6, small=True))
    box(46, "no field: random, M = 0", False)
    box(170, "field B₀ ↑: aligned, M = N m", True)
    o.append(text(538, 286, "M = N m   [A/m]", size=12.5, weight=600))
    o.append(svg_close())
    figure("mag-moment-torque", "".join(o),
           "<strong>An atom is a current loop, and a field turns it.</strong> Left: an electron circling a nucleus is a loop current I that flows <em>opposite</em> to the electron's velocity; its moment <b>m</b> = I<b>A</b> is normal to the loop by the right-hand rule (here up — antiparallel to the electron's own angular momentum). The electron's spin adds a moment of the same size that has no classical picture. Middle: in a uniform field <b>B</b>₀ the forces I d<b>l</b> × <b>B</b>₀ on the two sides of a tilted loop are equal and opposite, so there is no net force — but they act along different lines, a couple, whose torque <b>T</b> = <b>m</b> × <b>B</b>₀ (out of the page here) turns <b>m</b> toward <b>B</b>₀, as a compass needle turns north. Right: with no field the moments point every which way and average to zero; a field lines them up (partly — thermal jostling fights it) and the material acquires a magnetization <b>M</b> = N<b>m</b>, the dipole moment per unit volume, in A/m — the same unit as <b>H</b>.")


# --------------------------------------------------------------------------- 2. loops cancel inside, survive on the surface
def fig_mag_loops_surface_current():
    W, H = 640, 300
    o = [svg_open(W, H)]
    x0, y0, s, ncol, nrow = 34, 58, 54, 4, 3
    o.append(text(x0 + ncol * s / 2, 30, "a slab of atomic loops  (M ⊙)", size=12.5, weight=600))
    o.append(_tint(x0, y0, ncol * s, nrow * s, "var(--accent2)", 0.10))
    ins = 7
    for i in range(ncol):
        for j in range(nrow):
            L, R = x0 + i * s + ins, x0 + (i + 1) * s - ins
            T, B = y0 + j * s + ins, y0 + (j + 1) * s - ins
            c = "var(--accent)"
            # counter-clockwise as seen by the viewer (moment out of the page): bottom ->, right up, top <-, left down
            o.append(arrow(L + 6, B, R - 6, B, stroke=c, w=1.5, small=True))
            o.append(arrow(R, B - 6, R, T + 6, stroke=c, w=1.5, small=True))
            o.append(arrow(R - 6, T, L + 6, T, stroke=c, w=1.5, small=True))
            o.append(arrow(L, T + 6, L, B - 6, stroke=c, w=1.5, small=True))
            o.append(_odot((L + R) / 2, (T + B) / 2, r=4.5, color="var(--accent2)"))
    # surviving boundary current, counter-clockwise; M x n: right edge z x x = +y (up), top z x y = -x (left)   [verify C1]
    gx0, gy0, gx1, gy1 = x0 - 4, y0 - 4, x0 + ncol * s + 4, y0 + nrow * s + 4
    o.append(rect(gx0, gy0, gx1 - gx0, gy1 - gy0, stroke="var(--hi)", sw=2.4, rx=3))
    midx, midy = (gx0 + gx1) / 2, (gy0 + gy1) / 2
    o.append(arrow(midx - 14, gy1, midx + 14, gy1, stroke="var(--hi)", w=2.6))       # bottom: right
    o.append(arrow(gx1, midy + 14, gx1, midy - 14, stroke="var(--hi)", w=2.6))       # right: up
    o.append(arrow(midx + 14, gy0, midx - 14, gy0, stroke="var(--hi)", w=2.6))       # top: left
    o.append(arrow(gx0, midy - 14, gx0, midy + 14, stroke="var(--hi)", w=2.6))       # left: down
    tx = x0 + ncol * s / 2
    o.append(text(tx, 246, "interior edges: opposite currents cancel", size=11.5, fill="var(--accent)"))
    o.append(text(tx, 263, "boundary edges survive:  " + _sub("J", "sM") + " = M × n̂", size=11.5, fill="var(--hi)", weight=600))
    o.append(text(tx, 284, "M non-uniform → leftover volume current ∇×M", size=11, fill="var(--muted)"))
    # ---- right: the rod seen from the side, M up
    rx0, rx1, ry0, ry1 = 330, 420, 52, 222
    o.append(text((rx0 + rx1) / 2 + 60, 30, "a uniformly magnetized rod", size=12.5, weight=600))
    o.append(_tint(rx0, ry0, rx1 - rx0, ry1 - ry0, "var(--accent2)", 0.14))
    o.append(rect(rx0, ry0, rx1 - rx0, ry1 - ry0, stroke="currentColor", sw=1.4))
    # M up (+y screen). side faces: right n = +x -> M x n = y x x = -z (otimes); left n = -x -> +z (odot)   [verify C3]
    for k in range(7):
        yy = ry0 + 14 + k * (ry1 - ry0 - 28) / 6
        o.append(_odot(rx0, yy, r=6.5, color="var(--hi)"))
        o.append(_otimes(rx1, yy, r=6.5, color="var(--hi)"))
    for X0 in (rx0 + 26, rx1 - 26):
        o.append(arrow(X0, ry1 - 16, X0, ry0 + 16, stroke="var(--accent2)", w=2.4))
    o.append(text((rx0 + rx1) / 2, (ry0 + ry1) / 2 + 5, "M", size=15, math=True, fill="var(--accent2)", weight=600))
    o.append(text((rx0 + rx1) / 2, ry1 + 22, "⊙ out of page, ⊗ into page", size=11, fill="var(--muted)"))
    lx = 438
    o.append(text(lx, 70, _sub("J", "sM") + " = M × n̂ on the side:", size=11.5, anchor="start", weight=600))
    o.append(text(lx, 88, "⊙ on the left, ⊗ on the right —", size=11.5, anchor="start"))
    o.append(text(lx, 105, "a solenoid winding with nI → M", size=11.5, anchor="start"))
    o.append(text(lx, 132, "end faces: M × n̂ = 0", size=11.5, anchor="start"))
    o.append(text(lx, 158, "long rod, no free current:", size=11.5, anchor="start"))
    o.append(text(lx, 175, "B ≈ μ₀M inside  (like μ₀nI)", size=11.5, anchor="start", fill="var(--accent2)", weight=600))
    o.append(text(lx, 202, "M, nI and " + _sub("J", "s") + " are all in A/m", size=11.5, anchor="start", fill="var(--muted)"))
    o.append(svg_close())
    figure("mag-loops-surface-current", "".join(o),
           "<strong>Why a magnetized body behaves like a coil.</strong> Left: model the material as a lattice of identical atomic current loops, each circulating counter-clockwise as you look at it (moment out of the page). Wherever two loops share an edge their currents run in opposite directions and cancel; only the outer edges have no partner, so the net effect of a <em>uniform</em> magnetization is a single current circulating around the boundary. With loops of current I on cells of side s, M = I s²/s³ = I/s — exactly the current per unit length on the boundary, so the surface magnetization current is <b>J</b><sub>sM</sub> = <b>M</b> × n̂ in A/m. If M varies from cell to cell the shared edges no longer cancel and a volume current ∇×<b>M</b> is left inside. Right: a uniformly magnetized rod therefore carries a sheet of current around its side, like a solenoid's winding with nI replaced by M, and none on its end faces; a long rod with no free current has B ≈ μ₀M inside, the solenoid's μ₀nI.")


# --------------------------------------------------------------------------- 3. slide-16 slab between two current sheets
def fig_mag_slab_between_sheets():
    W, H = 640, 320
    o = [svg_open(W, H)]
    xl, xr = 30, 262
    yt, yb = 66, 224                  # free sheets
    st, sb = 94, 196                  # slab faces
    o.append(text((xl + xr) / 2, 36, "H = 0,  B = 0", size=11.5, fill="var(--muted)"))
    o.append(text((xl + xr) / 2, 256, "H = 0,  B = 0", size=11.5, fill="var(--muted)"))
    o.append(_tint(xl, st, xr - xl, sb - st, "var(--accent2)", 0.16))
    o.append(rect(xl, st, xr - xl, sb - st, stroke="currentColor", sw=1.2))
    # page frame: x right, z up, y INTO the page.  page -y = screen +z (out).
    # top free sheet -0.1 y -> odot ; bottom +0.1 y -> otimes                                   [verify G5]
    o.append(line(xl - 8, yt, xr + 8, yt, stroke="var(--hi)", w=1.4, dash="3 3", opacity=0.7))
    o.append(line(xl - 8, yb, xr + 8, yb, stroke="var(--hi)", w=1.4, dash="3 3", opacity=0.7))
    for k in range(8):
        X0 = xl + 11 + k * 30
        o.append(_odot(X0, yt, r=6, color="var(--hi)"))
        o.append(_otimes(X0, yb, r=6, color="var(--hi)"))
    o.append(text(xr + 14, yt + 4, "−0.1 ŷ A/m", size=11.5, anchor="start", fill="var(--hi)", weight=600))
    o.append(text(xr + 14, yb + 4, "+0.1 ŷ A/m", size=11.5, anchor="start", fill="var(--hi)", weight=600))
    # magnetization currents on the slab faces: M x n = 9.9 x times z = -9.9 y -> odot (top); +9.9 y -> otimes (bottom) [verify G3, G5]
    for k in range(7):
        X0 = xl + 26 + k * 30
        o.append(_odot(X0, st, r=4.5, color="var(--accent2)"))
        o.append(_otimes(X0, sb, r=4.5, color="var(--accent2)"))
    o.append(text(xr + 14, st + 4, "−9.9 ŷ A/m", size=11.5, anchor="start", fill="var(--accent2)", weight=600))
    o.append(text(xr + 14, sb + 4, "+9.9 ŷ A/m", size=11.5, anchor="start", fill="var(--accent2)", weight=600))
    o.append(text((xl + xr) / 2, st + 30, "slab, μᵣ = 100", size=12.5, weight=600))
    # H, M, B all along +x (right)                                                                [verify G5]
    o.append(arrow(96, st + 52, 196, st + 52, stroke="var(--accent)", w=2.8))
    o.append(text((xl + xr) / 2, st + 76, "H, M and B all along +x̂", size=11.5, fill="var(--accent)"))
    # axes icon: x right, z up, y into the page (otimes)
    ax, ay = 40, 298
    o.append(arrow(ax, ay, ax + 30, ay, stroke="currentColor", w=1.4, small=True))
    o.append(arrow(ax, ay, ax, ay - 30, stroke="currentColor", w=1.4, small=True))
    o.append(_otimes(ax, ay, r=5))
    o.append(text(ax + 34, ay + 4, "x", size=12, math=True, anchor="start"))
    o.append(text(ax + 4, ay - 30, "z", size=12, math=True, anchor="start"))
    o.append(text(ax - 9, ay + 4, "y", size=12, math=True, anchor="end"))
    o.append(text(ax + 52, ay + 4, "(y into the page)", size=10.5, anchor="start", fill="var(--muted)"))
    o.append(text(xr + 14, st + 22, "M × n̂ on the", size=10.5, anchor="start", fill="var(--accent2)"))
    o.append(text(xr + 14, st + 36, "slab faces", size=10.5, anchor="start", fill="var(--accent2)"))
    o.append(text(xr + 14, yt - 14, "free sheets", size=10.5, anchor="start", fill="var(--hi)"))
    # right column: the four steps
    tx = 384
    rows = [
        (40, "1.  H from the free sheets only", True, None),
        (58, "each sheet: ½ Jₛ × n̂ = 0.05 x̂ inside", False, None),
        (74, "H = 0.1 x̂ A/m between, 0 outside", False, None),
        (100, "2.  no free current on the slab faces", True, None),
        (118, "Hₜ continuous: H = 0.1 x̂ A/m in the slab", False, None),
        (144, "3.  the medium sets B and M", True, None),
        (162, "B = μ₀μᵣH = 1.26×10⁻⁵ x̂ T  (12.6 μT)", False, None),
        (178, "M = χₘH = 99 × 0.1 = 9.9 x̂ A/m", False, None),
        (204, "4.  check with the bound currents", True, None),
        (222, "M × n̂ = ∓9.9 ŷ A/m: same sense as", False, None),
        (238, "the free sheets; 0.1 + 9.9 = 10 A/m", False, None),
        (254, "B = μ₀ (10 A/m) = 100 μ₀H  ✓", False, "var(--accent2)"),
        (282, "μᵣ = 1: same H, B = 0.126 μT, M = 0", False, "var(--muted)"),
    ]
    for yy, s_, bold, col in rows:
        o.append(text(tx, yy, s_, size=11.5, anchor="start", weight=600 if bold else None, fill=col or "currentColor"))
    o.append(svg_close())
    figure("mag-slab-between-sheets", "".join(o),
           "<strong>The slide example: a magnetic slab between two opposite current sheets.</strong> The free sheets (red; −0.1 ŷ A/m on top, out of the page, and +0.1 ŷ A/m below, into it) are all that <b>H</b> knows about: each contributes ½<b>J</b><sub>s</sub> × n̂ = 0.05 x̂ A/m between them and the contributions cancel outside. The slab faces carry no free current, so tangential <b>H</b> passes into the slab unchanged — the same 0.1 x̂ A/m as with no slab at all. The material then sets <b>B</b> = μ<b>H</b> (100 times larger) and <b>M</b> = χ<sub>m</sub><b>H</b> = 9.9 x̂ A/m. The check: <b>M</b> × n̂ puts magnetization currents ∓9.9 ŷ A/m on the slab faces (green), in the same sense as the free sheets; free plus bound, 10 A/m per face, inserted in the <em>vacuum</em> sheet formula gives B = μ₀ × 10 A/m = 100 μ₀H inside the slab, and still μ₀H in any gap between a sheet and the slab.")


# --------------------------------------------------------------------------- 4. hysteresis loop
def fig_mag_hysteresis():
    W, H = 640, 320
    o = [svg_open(W, H)]
    ox, oy, sx, sy = 200, 165, 52, 105
    Bs, Hc, w = 1.0, 0.9, 0.8
    Bd = lambda h: Bs * math.tanh((h + Hc) / w)          # descending branch (coming down from +saturation)
    Ba = lambda h: Bs * math.tanh((h - Hc) / w)          # ascending branch
    Bv = lambda h: Bs * math.tanh((h / w) ** 2 / (1 + h / w))   # virgin curve, h >= 0 (inside the loop: verify F1)
    P = lambda h, b: (ox + sx * h, oy - sy * b)
    o.append(line(36, oy, 372, oy, w=1.4, arrow=True)); o.append(text(378, oy + 5, "H", size=15, math=True, anchor="start"))
    o.append(line(ox, 308, ox, 22, w=1.4, arrow=True)); o.append(text(ox + 8, 26, "B", size=15, math=True, anchor="start"))
    # vacuum line B = mu0 H, almost flat on this scale
    o.append(line(*P(-3.1, -0.06), *P(3.1, 0.06), dash="5 4", w=1.2, opacity=0.8, stroke="var(--muted)"))
    o.append(text(*P(3.1, 0.12), "B = μ₀H (vacuum)", size=10.5, anchor="end", fill="var(--muted)"))
    hs = np.linspace(3.0, -3.0, 121)
    o.append(path("M" + " L".join("{:.1f},{:.1f}".format(*P(h, Bd(h))) for h in hs), stroke="var(--accent)", w=2.6))
    o.append(path("M" + " L".join("{:.1f},{:.1f}".format(*P(h, Ba(h))) for h in hs[::-1]), stroke="var(--accent)", w=2.6))
    hv = np.linspace(0, 3.0, 61)
    o.append(path("M" + " L".join("{:.1f},{:.1f}".format(*P(h, Bv(h))) for h in hv), stroke="var(--accent2)", w=2, dash="6 4"))
    # direction arrows: upper branch traversed leftward, lower branch rightward (counter-clockwise loop) [verify F1]
    def tangent_arrow(fn, h0, h1, col):
        x0_, y0_ = P(h0, fn(h0)); x1_, y1_ = P(h1, fn(h1))
        o.append(arrow(x0_, y0_, x1_, y1_, stroke=col, w=2.6))
    tangent_arrow(Bd, -1.25, -1.5, "var(--accent)")
    tangent_arrow(Ba, 1.25, 1.5, "var(--accent)")
    tangent_arrow(Bv, 0.95, 1.15, "var(--accent2)")
    # B_r and H_c markers
    Br = Bd(0)
    for (h, b) in ((0, Br), (0, -Br), (-Hc, 0), (Hc, 0)):
        o.append(circle(*P(h, b), 4, fill="var(--hi)", stroke="none"))
    o.append(text(P(0, Br)[0] - 8, P(0, Br)[1] - 6, _sub("B", "r") + "  (H = 0)", size=12, anchor="end", fill="var(--hi)", weight=600))
    o.append(text(P(0, -Br)[0] + 8, P(0, -Br)[1] + 16, "−" + _sub("B", "r"), size=12, anchor="start", fill="var(--hi)", weight=600))
    o.append(text(P(-Hc, 0)[0] - 4, oy - 10, "−" + _sub("H", "c"), size=12, anchor="end", fill="var(--hi)", weight=600))
    o.append(text(P(Hc, 0)[0] + 4, oy + 20, "+" + _sub("H", "c"), size=12, anchor="start", fill="var(--hi)", weight=600))
    o.append(text(*P(2.2, 1.12), "saturation", size=11, fill="var(--muted)"))
    o.append(text(*P(-2.2, -1.2), "saturation", size=11, fill="var(--muted)"))
    # right column
    tx = 400
    rows = [(44, "what the loop says", True, None),
            (66, "virgin curve (dashed): domains grow", False, "var(--accent2)"),
            (82, "and turn as H is first raised", False, "var(--accent2)"),
            (106, _sub("B", "r") + ", remanence: B ≠ 0 at H = 0 —", False, "var(--hi)"),
            (122, "a permanent magnet", False, "var(--hi)"),
            (146, _sub("H", "c") + ", coercivity: the reverse H", False, "var(--hi)"),
            (162, "needed to bring B back to zero", False, "var(--hi)"),
            (186, "B depends on H and on the history:", False, None),
            (202, "μ = B/H is not a material constant", False, None),
            (226, "loop area = energy lost per m³", False, None),
            (242, "per cycle (heats transformer cores)", False, None),
            (268, "soft magnets: narrow loop, small " + _sub("H", "c"), False, "var(--muted)"),
            (284, "hard magnets: wide loop, large " + _sub("B", "r") + ", " + _sub("H", "c"), False, "var(--muted)")]
    for yy, s_, bold, col in rows:
        o.append(text(tx, yy, s_, size=11.5, anchor="start", weight=600 if bold else None, fill=col or "currentColor"))
    o.append(svg_close())
    figure("mag-hysteresis", "".join(o),
           "<strong>A ferromagnet remembers.</strong> Start with an unmagnetized sample (domains pointing every which way, M = 0) and raise H: B climbs along the dashed virgin curve as favourably oriented domains grow and the others turn, until nearly every moment is aligned and B saturates. Now lower H. B does not retrace its path: at H = 0 there is still a remanent flux density B<sub>r</sub> — the sample has become a permanent magnet — and a reverse field −H<sub>c</sub> (the coercivity) is needed to bring B to zero. Driving H back and forth traces the loop counter-clockwise; its area is the energy per unit volume turned into heat each cycle. Because B depends on the history, μ = B/H is not a constant for these materials; the vacuum line B = μ₀H is almost flat on this scale, which is what χ<sub>m</sub> ≫ 1 means. The shape is schematic.")


# --------------------------------------------------------------------------- 5. refraction of B at a magnetic interface; iron surface
def fig_mag_refraction():
    W, H = 640, 300
    o = [svg_open(W, H)]
    yI = 160
    # ---- left: worked-problem interface, mu1 = 2 mu0 over mu2 = 6 mu0, H1 = (t 5, n -9) -> H2 = (5, -3)   [verify I-fig]
    o.append(_tint(15, 40, 320, yI - 40, "var(--accent)", 0.06)); o.append(_tint(15, yI, 320, 290 - yI, "var(--accent2)", 0.16))
    o.append(line(15, yI, 335, yI, w=2))
    o.append(text(175, 24, "refraction at a magnetic interface", size=12.5, weight=600))
    o.append(text(328, 56, "medium 1:  μ₁ = 2μ₀", size=12, anchor="end"))
    o.append(text(22, 282, "medium 2:  μ₂ = 6μ₀", size=12, anchor="start"))
    cx, s_ = 150, 11
    o.append(arrow(cx, yI, cx, yI - 114, stroke="currentColor", w=1.5)); o.append(text(cx + 7, yI - 104, "n̂", size=14, anchor="start", weight=600))
    o.append(line(cx, yI, cx, yI + 64, w=1.1, dash="4 3", opacity=0.6))
    o.append(arrow(cx - 5 * s_, yI - 9 * s_, cx, yI, stroke="var(--accent)", w=3))
    o.append(arrow(cx, yI, cx + 5 * s_, yI + 3 * s_, stroke="var(--accent)", w=3))
    o.append(text(cx - 5 * s_ - 6, yI - 9 * s_ + 12, _sub("H", "1"), size=13, anchor="end", fill="var(--accent)", weight=600))
    o.append(text(cx + 5 * s_ + 6, yI + 3 * s_ + 4, _sub("H", "2"), size=13, anchor="start", fill="var(--accent)", weight=600))
    th1 = math.degrees(math.atan(5 / 9)); th2 = math.degrees(math.atan(5 / 3))
    o.append(_arc(cx, yI, 42, 90, 90 + th1, w=1.1))
    o.append(text(cx - 15, yI - 52, "θ₁", size=12, anchor="middle"))
    o.append(_arc(cx, yI, 30, 270, 270 + th2, w=1.1))
    o.append(text(cx + 20, yI + 48, "θ₂", size=12, anchor="middle"))
    rx_ = 196
    o.append(text(rx_, 84, "Hₜ = 5 on both sides", size=11.5, anchor="start"))
    o.append(text(rx_, 99, "(no free surface current)", size=10.5, anchor="start", fill="var(--muted)"))
    o.append(text(rx_, 124, "μ₁H₁ₙ = μ₂H₂ₙ:", size=11.5, anchor="start"))
    o.append(text(rx_, 140, "2(−9) = 6(−3)", size=11.5, anchor="start"))
    o.append(text(328, 236, "θ₁ = 29.1°,  θ₂ = 59.0°", size=11.5, anchor="end"))
    o.append(text(328, 256, "tan θ₁ / tan θ₂ = μ₁/μ₂ = 1/3", size=11.5, anchor="end", weight=600))
    # ---- right: air over iron, mu_r = 5000.  theta_iron = 85 deg -> theta_air = 0.13 deg       [verify H2]
    o.append(_tint(350, 40, 280, yI - 40, "var(--accent)", 0.06)); o.append(_tint(350, yI, 280, 290 - yI, "var(--accent2)", 0.34))
    o.append(line(350, yI, 630, yI, w=2))
    o.append(text(490, 24, "air over iron (μᵣ = 5000)", size=12.5, weight=600))
    o.append(text(357, 56, "air", size=12, anchor="start"))
    o.append(text(357, 282, "iron", size=12, anchor="start"))
    px = 470
    thI = math.radians(85)
    Lb = 108
    sx_, sy_ = px - Lb * math.sin(thI), yI + Lb * math.cos(thI)
    o.append(line(px, yI, px, yI + 26, w=1.1, dash="4 3", opacity=0.6))
    o.append(arrow(sx_, sy_, px - 2, yI + 1, stroke="var(--accent)", w=3))
    o.append(arrow(px, yI, px, yI - 104, stroke="var(--accent)", w=3))
    o.append(text(px + 9, yI - 58, "B in air: θ = 0.13°", size=11.5, anchor="start", fill="var(--accent)", weight=600))
    o.append(text(px + 9, yI - 42, "(leaves almost normally)", size=10.5, anchor="start", fill="var(--muted)"))
    o.append(text(sx_ + 4, sy_ + 32, "B in iron: θ = 85°", size=11.5, anchor="start", fill="var(--accent)", weight=600))
    o.append(text(490, 236, "tan θ" + _sub("", "air") + " = tan θ" + _sub("", "iron") + " / 5000", size=12, weight=600))
    o.append(text(490, 256, "(lengths not to scale)", size=10.5, fill="var(--muted)"))
    o.append(svg_close())
    figure("mag-refraction", "".join(o),
           "<strong>How field lines bend where μ changes.</strong> Left: the interface of the worked problem. Tangential <b>H</b> is continuous (no free surface current) and normal <b>B</b> is continuous, so the normal part of <b>H</b> scales by μ₁/μ₂: from −9 above to −3 below, while the tangential part stays 5. Entering the more permeable medium the line tilts away from the normal, and tan θ₁/tan θ₂ = μ₁/μ₂ — the refraction law of Lecture 9 with ε replaced by μ. <b>B</b> is parallel to <b>H</b> in each medium, so B lines bend by the same angles. Right: with iron (μ<sub>r</sub> ≈ 5000) the ratio is so extreme that a line running at 85° to the normal inside the iron leaves into the air at 0.13° — essentially perpendicular. Iron surfaces act for <b>B</b> the way conductor surfaces act for <b>E</b>, which is why the pole faces of a magnet set the direction of the field in its gap.")


if __name__ == "__main__":
    for f in (fig_mag_moment_torque, fig_mag_loops_surface_current, fig_mag_slab_between_sheets,
              fig_mag_hysteresis, fig_mag_refraction):
        f()
