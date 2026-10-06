#!/usr/bin/env python3
"""Lecture 18 figures (wave-*) for the ECE 329 notes: plane waves in source-free media.

Same helpers and conventions as figs.py. Running this module writes /home/claude/work/figs/<name>.html.
Direction conventions in the drawings (checked by explicit cross products in digest6/verify_L18.py, section F and L):
  physics axes drawn as  x = up,  z = right,  y = out of the page (the slides' frame; right-handed)
  screen frame for the checks: X right, Y up, Z out of the screen, so x^ -> (0,1,0), y^ -> (0,0,1), z^ -> (1,0,0).
  odot = out of the page (+y here), otimes = into the page (-y here).
"""
from figs import *
from figs import _odot, _otimes, _sub, _tint

C_LIGHT = 2.99792458e8

def lin(a0, a1, b0, b1):
    """affine map a -> b with a0 -> b0, a1 -> b1"""
    return lambda a: b0 + (a - a0) * (b1 - b0) / (a1 - a0)

def _rdp(pts, tol):
    """Ramer-Douglas-Peucker simplification of a screen-space polyline (keeps the shape to within tol px)"""
    if len(pts) < 3:
        return pts
    (x0, y0), (x1, y1) = pts[0], pts[-1]
    dx, dy = x1 - x0, y1 - y0
    nrm = math.hypot(dx, dy)
    if nrm == 0:
        dists = [math.hypot(x - x0, y - y0) for x, y in pts[1:-1]]
    else:
        dists = [abs(dy * (x - x0) - dx * (y - y0)) / nrm for x, y in pts[1:-1]]
    i = int(np.argmax(dists)) + 1
    if dists[i - 1] > tol:
        return _rdp(pts[:i + 1], tol)[:-1] + _rdp(pts[i:], tol)
    return [pts[0], pts[-1]]

def poly(xs, ys, MX, MY, tol=0.25, **kw):
    pts = [(float(MX(x)), float(MY(y))) for x, y in zip(xs, ys)]
    pts = _rdp(pts, tol)
    d = "M" + " L".join(f"{X:.1f},{Y:.1f}" for X, Y in pts)
    return path(d, **kw)

def haxis(X0, X1, Y, label, ticks, MX, tick_labels=True, size=10.5):
    """horizontal axis with arrow, tick marks and labels"""
    s = [line(X0, Y, X1, Y, w=1.3, arrow=True), text(X1 + 4, Y + 4, label, size=12.5, anchor="start", math=True)]
    for tv, tl in ticks:
        X = MX(tv)
        s.append(line(X, Y - 3, X, Y + 3, w=1.1))
        if tick_labels and tl is not None:
            s.append(text(X, Y + 15, tl, size=size, fill="var(--muted)"))
    return "".join(s)

# ------------------------------------------------------------------------------------------------ 1. current sheet
def fig_wave_current_sheet():
    W, H = 640, 300
    o = [svg_open(W, H)]
    top, bot = 62, 222
    # ---- left panel: the static sheet of Lecture 13
    xL = 150
    o.append(text(xL, 22, "static sheet (Lecture 13)", size=13, weight=600))
    o.append(text(xL, 40, _sub("J", "s") + " constant in time", size=11.5, fill="var(--muted)"))
    o.append(line(xL, top, xL, bot, stroke="var(--hi)", w=2.4))
    # J_s = -J_s x^ : x is up, so the current arrows point DOWN along the sheet
    for yy in (78, 128, 178):
        o.append(arrow(xL + 7, yy, xL + 7, yy + 26, stroke="var(--hi)", w=1.6, small=True))
    o.append(text(xL + 12, bot + 18, _sub("J", "s") + " = −" + _sub("J", "s") + " x̂", size=12, fill="var(--hi)", weight=600))
    # H = 1/2 J_s x n^ with n^ toward the field point.
    # right side (n = +z): screen (0,-1,0) x (1,0,0) = (0,0,+1) -> out of the page (odot) = +y
    # left side  (n = -z): screen (0,-1,0) x (-1,0,0) = (0,0,-1) -> into the page (otimes) = -y
    for yy in (95, 142, 189):
        o.append(_odot(xL + 52, yy, r=7, color="var(--accent2)"))
        o.append(_otimes(xL - 52, yy, r=7, color="var(--accent2)"))
    o.append(text(xL + 66, 146, "H = +ŷ " + _sub("J", "s") + "/2", size=12, anchor="start", fill="var(--accent2)", weight=600))
    o.append(text(xL - 66, 146, "H = −ŷ " + _sub("J", "s") + "/2", size=12, anchor="end", fill="var(--accent2)", weight=600))
    o.append(text(xL, 262, "H only, E = 0;  H = ½ " + _sub("J", "s") + " × n̂", size=11.5))
    o.append(line(305, 30, 305, 270, stroke="var(--muted)", w=1, dash="3 4"))
    # ---- right panel: the time-varying sheet (slides S4-S11)
    xR = 470
    o.append(text(xR, 22, "time-varying sheet " + _sub("J", "s") + "(t) (slides)", size=13, weight=600))
    o.append(text(xR, 40, "waves leave both faces:  " + _sub("E", "x") + "(z,t),  " + _sub("H", "y") + "(z,t)", size=11.5, fill="var(--muted)"))
    o.append(line(xR, top, xR, bot, stroke="var(--hi)", w=2.4))
    for yy in (78, 128, 178):
        o.append(arrow(xR + 7, yy, xR + 7, yy + 26, stroke="var(--hi)", w=1.6, small=True))
    o.append(text(xR + 12, bot + 18, _sub("J", "s") + "(t), drawn for " + _sub("J", "s") + " &gt; 0", size=11.5, fill="var(--hi)", anchor="middle"))
    # E = +x (up) on both sides: opposite to J_s (the slides' ink)
    for dx in (-40, 40):
        o.append(arrow(xR + dx, 172, xR + dx, 112, stroke="var(--accent)", w=2.6))
    o.append(text(xR + 47, 108, "E", size=13, anchor="start", fill="var(--accent)", weight=700, math=True))
    o.append(text(xR - 47, 108, "E", size=13, anchor="end", fill="var(--accent)", weight=700, math=True))
    # H: +y (odot) for z > 0, -y (otimes) for z < 0, as in the static case
    o.append(_odot(xR + 82, 142, r=8, color="var(--accent2)"))
    o.append(_otimes(xR - 82, 142, r=8, color="var(--accent2)"))
    o.append(text(xR + 82, 168, "H", size=13, fill="var(--accent2)", weight=700, math=True))
    o.append(text(xR - 82, 168, "H", size=13, fill="var(--accent2)", weight=700, math=True))
    # travel = E x H: screen (0,1,0) x (0,0,1) = (1,0,0) -> right (+z);  (0,1,0) x (0,0,-1) = (-1,0,0) -> left (-z)
    o.append(arrow(xR + 108, 142, xR + 158, 142, stroke="currentColor", w=3))
    o.append(arrow(xR - 108, 142, xR - 158, 142, stroke="currentColor", w=3))
    o.append(text(xR + 133, 130, "+z", size=12, weight=600))
    o.append(text(xR - 133, 130, "−z", size=12, weight=600))
    o.append(text(xR, 262, "E × H points away from the sheet on both sides", size=11.5, weight=600))
    o.append(text(xR, 280, "E opposite to " + _sub("J", "s") + " (slides' ink); the amplitude is Lecture 19", size=10.5, fill="var(--muted)"))
    # ---- axis icon: x up, z right, y out of the page (x cross y = z: (0,1,0) x (0,0,1) = (1,0,0))
    ax, ay = 30, 282
    o.append(arrow(ax, ay, ax, ay - 34, stroke="currentColor", w=1.4, small=True)); o.append(text(ax + 7, ay - 30, "x", size=12, anchor="start", math=True))
    o.append(arrow(ax, ay, ax + 34, ay, stroke="currentColor", w=1.4, small=True)); o.append(text(ax + 38, ay + 4, "z", size=12, anchor="start", math=True))
    o.append(_odot(ax, ay, r=5)); o.append(text(ax - 8, ay + 4, "y", size=12, anchor="end", math=True))
    o.append(svg_close())
    figure("wave-current-sheet", "".join(o),
           "<strong>The slides' source: an infinite sheet of current in the plane z = 0, seen edge-on.</strong> "
           "The page is the xz-plane (x up, z right, y out of the page — a right-handed frame). "
           "Left: the Lecture 13 case, a steady sheet current J<sub>s</sub> = −J<sub>s</sub> x̂. Ampère's law gives "
           "<b>H</b> = ½<b>J</b><sub>s</sub> × n̂ — out of the page (⊙, +ŷ) for z &gt; 0, into it (⊗, −ŷ) for z &lt; 0 — and no <b>E</b>. "
           "Right: let J<sub>s</sub> vary in time. Symmetry and the source-free equations still allow only E<sub>x</sub>(z,t) "
           "and H<sub>y</sub>(z,t), but now both are nonzero. The arrows show the directions next to the sheet while "
           "J<sub>s</sub> &gt; 0: <b>E</b> points along +x̂, opposite to <b>J</b><sub>s</sub> (the in-class ink), and "
           "<b>H</b> has the same pattern as in the static case. "
           "Check one side: x̂ × ŷ = +ẑ on the right and x̂ × (−ŷ) = −ẑ on the left. So <b>E</b> × <b>H</b> "
           "points away from the sheet on both sides, which is the direction the waves travel. Lecture 19 derives "
           "how strong these fields are.")

# ------------------------------------------------------------------------------------------------ 2. pulse at two times
def fig_wave_pulse_two_times():
    W, H = 640, 420
    o = [svg_open(W, H)]
    a = 0.5e-9
    f = lambda t: np.where(t > 0, (t / a) * np.exp(1 - t / a), 0.0)   # time record at a fixed point
    # ---- row 1: time history at z = 0
    MT = lin(-1.0, 5.0, 70, 330); Y1 = 98; A1 = 46
    MY1 = lambda e: Y1 - A1 * e
    o.append(text(20, 24, "1  The record of a probe at z = 0 (the same for both waves below)", size=12.5, anchor="start", weight=600))
    o.append(haxis(58, 342, Y1, "t", [(k, f"{k}" if k else "0") for k in range(0, 5)], MT))
    o.append(text(342, Y1 + 15, "ns", size=10.5, anchor="start", fill="var(--muted)"))
    ts = np.linspace(-1.0, 4.6, 400)
    o.append(poly(ts, f(ts * 1e-9), MT, MY1, stroke="var(--accent)", w=2.4))
    o.append(text(MT(0.5) + 6, MY1(1.0) - 4, "fast rise", size=11, anchor="start", fill="var(--accent)"))
    o.append(text(MT(2.4), MY1(0.42), "slow tail", size=11, anchor="start", fill="var(--accent)"))
    o.append(text(372, 56, "The front of the pulse reaches the probe first,", size=11.5, anchor="start"))
    o.append(text(372, 72, "so in a time record it sits on the LEFT (early t).", size=11.5, anchor="start"))
    o.append(text(372, 92, "In space the front leads in the direction of", size=11.5, anchor="start", fill="var(--muted)"))
    o.append(text(372, 108, "travel: right for +z, left for −z.", size=11.5, anchor="start", fill="var(--muted)"))
    # ---- rows 2 and 3: snapshots in z at t = 0 and t = 8 ns (v = c)
    MZ = lin(-3.3, 3.3, 52, 600)
    zs = np.linspace(-3.3, 3.3, 1400)
    t1 = 8e-9
    d = C_LIGHT * t1           # 2.40 m
    def row(Y, title, sign):
        # sign = +1: f(t - z/v) (travel +z); sign = -1: f(t + z/v) (travel -z)
        A = 50
        MY = lambda e: Y - A * e
        o.append(text(20, Y - A - 46, title, size=12.5, anchor="start", weight=600))
        o.append(haxis(40, 610, Y, "z", [(k, f"{k}") for k in range(-3, 4)], MZ))
        o.append(text(612, Y + 15, "m", size=10.5, anchor="start", fill="var(--muted)"))
        e0 = f(0 - sign * zs / C_LIGHT); e1 = f(t1 - sign * zs / C_LIGHT)
        o.append(poly(zs, e0, MZ, MY, stroke="var(--muted)", w=2, dash="5 4"))
        o.append(poly(zs, e1, MZ, MY, stroke="var(--accent)", w=2.6))
        # peak positions: f peaks where its argument t -/+ z/c equals a, i.e. z = sign * c (t - a)
        zpk0 = sign * C_LIGHT * (0 - a)
        zpk1 = sign * C_LIGHT * (t1 - a)
        # labels: 't = 0' just beyond the front of the dashed snapshot (its front is at z = 0);
        # 't = 8 ns' beside the solid peak on the tail side, at peak height (the tail stays within ~6 px of the peak there)
        o.append(text(MZ(0) + sign * 8, MY(0.55), "t = 0", size=11, anchor="start" if sign > 0 else "end", fill="var(--muted)"))
        o.append(text(MZ(zpk1) - sign * 20, MY(1.0) + 4, "t = 8 ns", size=11, anchor="end" if sign > 0 else "start", fill="var(--accent)", weight=600))
        # displacement arrow between the peaks, just above them
        ya = MY(1.0) - 10
        o.append(arrow(MZ(zpk0), ya, MZ(zpk1), ya, stroke="currentColor", w=1.8))
        o.append(text((MZ(zpk0) + MZ(zpk1)) / 2, ya - 6, "c × 8 ns = 2.4 m", size=11))
        # mark the front (the steep edge) of the later snapshot
        zfront = sign * d
        o.append(text(MZ(zfront) + sign * 6, MY(0.25), "front", size=11, anchor="start" if sign > 0 else "end", fill="var(--hi)", weight=600))
    row(254, "2  +z wave:  " + _sub("E", "x") + " = f(t − z/v)  — snapshot = record mirrored", +1)
    row(398, "3  −z wave:  " + _sub("E", "x") + " = f(t + z/v)  — snapshot has the record's order", -1)
    o.append(svg_close())
    figure("wave-pulse-two-times", "".join(o),
           "<strong>One waveform, two directions of travel.</strong> Row 1 is what a probe at z = 0 records: a pulse that rises in "
           "about half a nanosecond and decays over a few nanoseconds. Rows 2 and 3 are snapshots in space at t = 0 (dashed) and "
           "t = 8 ns (solid), computed from f(t ∓ z/v) with v = c. Both pulses move without changing shape, 2.4 m in 8 ns. The "
           "steep front always leads, so the <em>spatial</em> picture of a +z wave is the time record reversed left-to-right "
           "(E<sub>x</sub>(z,0) = f(−z/v)). The −z wave keeps the record's left-to-right order (E<sub>x</sub>(z,0) = f(z/v)). "
           "Forgetting this reversal is the commonest error when a problem gives the pulse at one instant and asks what a "
           "probe will see.")

# ------------------------------------------------------------------------------------------------ 3. E, H, travel triads
def fig_wave_eh_triads():
    W, H = 640, 340
    o = [svg_open(W, H)]
    # drawing directions (SVG coords, y down): physics x -> up, z -> right, y (out of page) -> down-left
    UX = np.array([0.0, -1.0]); UZ = np.array([1.0, 0.0]); UY = np.array([-0.62, 0.48])
    def vec(e):   # physics 3-vector -> SVG 2-vector
        return e[0] * UX + e[1] * UY + e[2] * UZ
    cells = [  # (col, row, E, H, u, E text, H text, S text)
        # x-pol +z: x^ cross y^ = z^     (screen: (0,1,0) x (0,0,1) = (1,0,0) -> right)
        (0, 0, (1, 0, 0), (0, 1, 0), (0, 0, 1), "E = x̂ f(t − z/v)", "H = +ŷ f(t − z/v)/η", "E × H along +ẑ"),
        # x-pol -z: x^ cross (-y^) = -z^ (screen: (0,1,0) x (0,0,-1) = (-1,0,0) -> left)
        (1, 0, (1, 0, 0), (0, -1, 0), (0, 0, -1), "E = x̂ f(t + z/v)", "H = −ŷ f(t + z/v)/η", "E × H along −ẑ"),
        # y-pol +z: y^ cross (-x^) = z^  (screen: (0,0,1) x (0,-1,0) = (1,0,0) -> right)
        (0, 1, (0, 1, 0), (-1, 0, 0), (0, 0, 1), "E = ŷ f(t − z/v)", "H = −x̂ f(t − z/v)/η", "E × H along +ẑ"),
        # y-pol -z: y^ cross x^ = -z^    (screen: (0,0,1) x (0,1,0) = (-1,0,0) -> left)
        (1, 1, (0, 1, 0), (1, 0, 0), (0, 0, -1), "E = ŷ f(t + z/v)", "H = +x̂ f(t + z/v)/η", "E × H along −ẑ"),
    ]
    o.append(text(190, 22, "travel toward +z", size=13, weight=600))
    o.append(text(500, 22, "travel toward −z", size=13, weight=600))
    o.append(text(16, 112, "x-polarized", size=12.5, weight=600, rotate=-90))
    o.append(text(16, 268, "y-polarized", size=12.5, weight=600, rotate=-90))
    o.append(line(34, 186, 630, 186, stroke="var(--muted)", w=1, dash="3 4"))
    o.append(line(340, 34, 340, 330, stroke="var(--muted)", w=1, dash="3 4"))
    for col, rowi, E, Hh, u, tE, tH, tS in cells:
        ox = 40 + col * 305 + 88; oy = 108 + rowi * 156
        # faint axes
        for e, lab in (((1, 0, 0), "x"), ((0, 1, 0), "y"), ((0, 0, 1), "z")):
            dv = vec(np.array(e, float)) * 46
            o.append(line(ox, oy, ox + dv[0], oy + dv[1], stroke="var(--muted)", w=1, dash="3 3"))
            o.append(text(ox + dv[0] * 1.18 + (4 if lab == "z" else 0), oy + dv[1] * 1.18 + 4, lab, size=11, fill="var(--muted)", math=True))
        # travel arrow (E x H), then E and H
        dS = vec(np.array(u, float)) * 64
        o.append(arrow(ox, oy, ox + dS[0], oy + dS[1], stroke="currentColor", w=3.2))
        dE = vec(np.array(E, float)) * 56
        o.append(arrow(ox, oy, ox + dE[0], oy + dE[1], stroke="var(--accent)", w=2.6))
        dH = vec(np.array(Hh, float)) * 50
        o.append(arrow(ox, oy, ox + dH[0], oy + dH[1], stroke="var(--accent2)", w=2.6))
        def lab_at(dv, s, col_, extra=(0, 0)):
            n = np.hypot(*dv); ux, uy = dv / n
            X, Y = ox + dv[0] + 12 * ux + extra[0], oy + dv[1] + 12 * uy + 4 + extra[1]
            return text(X, Y, s, size=13, fill=col_, weight=700, math=True)
        o.append(lab_at(dE, "E", "var(--accent)", (8 if E[1] == 0 else -4, 0)))
        o.append(lab_at(dH, "H", "var(--accent2)", (8 if Hh[1] == 0 else 0, 0)))
        o.append(text(ox + 0.55 * dS[0], oy - 8, "travel", size=11, anchor="middle"))
        # text block
        tx = 40 + col * 305 + 172
        o.append(text(tx, oy - 34, tE, size=11.5, anchor="start", fill="var(--accent)", weight=600))
        o.append(text(tx, oy - 16, tH, size=11.5, anchor="start", fill="var(--accent2)", weight=600))
        o.append(text(tx, oy + 2, tS, size=11.5, anchor="start"))
    o.append(svg_close())
    figure("wave-eh-triads", "".join(o),
           "<strong>Divide by η and rotate by 90°, choosing the rotation that makes E × H point the way the wave travels.</strong> "
           "The axes are drawn as on the slides: x up, z right, y out of the page (drawn toward the lower left). "
           "Top row: an x-polarized wave has <b>H</b> along +ŷ when it travels toward +z, and along −ŷ when it travels toward −z. "
           "That is the sign flip in H<sub>y</sub> = (Af − Bg)/η. "
           "Bottom row: a y-polarized wave needs <b>H</b> along −x̂ for +z travel, because ŷ × (−x̂) = +ẑ, and along +x̂ for −z travel. "
           "In every case <b>E</b> ⊥ <b>H</b>, both are perpendicular to the direction of travel, and |<b>E</b>|/|<b>H</b>| = η. "
           "In vector form, <b>H</b> = û × <b>E</b>/η and <b>E</b> = η<b>H</b> × û, with û the direction of travel.")

# ------------------------------------------------------------------------------------------------ 4. slide-26 moving waveform
def fig_wave_moving_waveform():
    W, H = 640, 360
    o = [svg_open(W, H)]
    tk = [0, 1, 2, 4, 5]; ek = [0, 1, 1, 0, 0]
    E0 = lambda t: np.interp(t, tk, ek, left=0, right=0)
    # ---- panel 1: record at z = 0
    MT = lin(-2.5, 7.0, 60, 590); Y1 = 118; A = 62
    MY1 = lambda e: Y1 - A * e
    o.append(text(20, 24, "1  The record at z = 0 (slide 26), and where the three questions land on it", size=12.5, anchor="start", weight=600))
    o.append(haxis(48, 602, Y1, "t", [(k, f"{k}") for k in range(-2, 8)], MT))
    o.append(text(604, Y1 + 15, "s", size=10.5, anchor="start", fill="var(--muted)"))
    o.append(poly([-2.5] + tk + [6.6], [0] + ek + [0], MT, MY1, stroke="var(--hi)", w=2.4))
    o.append(line(MT(-0.15), MY1(1), MT(0.15), MY1(1), w=1.1)); o.append(text(MT(-0.25), MY1(1) + 4, "1", size=10.5, anchor="end", fill="var(--muted)"))
    for lab, tq, eq, dx, dy in (("(b) 0.4", 0.4, 0.4, -10, -2), ("(c) 1.0", 1.6, 1.0, 0, -12), ("(a) 0.9", 2.2, 0.9, 12, -6)):
        o.append(circle(MT(tq), MY1(eq), 4.5, fill="var(--accent)", stroke="none"))
        o.append(text(MT(tq) + dx, MY1(eq) + dy, lab, size=11.5, anchor="end" if dx < 0 else ("start" if dx > 0 else "middle"), fill="var(--accent)", weight=700))
    for tw in (-1.8, -0.4, 6.4):
        X = MT(tw)
        o.append(line(X - 4, Y1 - 4, X + 4, Y1 + 4, stroke="var(--muted)", w=1.6)); o.append(line(X - 4, Y1 + 4, X + 4, Y1 - 4, stroke="var(--muted)", w=1.6))
    o.append(text(MT(4.25), Y1 - 64, "● t + z/v = 2.2, 0.4, 1.6 s", size=11, anchor="start", fill="var(--accent)", weight=600))
    o.append(text(MT(4.25), Y1 - 47, "× t − z/v = −1.8, 6.4, −0.4 s", size=11, anchor="start", fill="var(--muted)", weight=600))
    o.append(text(MT(4.25), Y1 - 32, "wrong sign: all three miss", size=11, anchor="start", fill="var(--muted)"))
    o.append(text(MT(4.25), Y1 - 18, "the pulse and read 0", size=11, anchor="start", fill="var(--muted)"))
    # ---- panel 2: snapshots in z
    MZ = lin(-320, 520, 60, 590); Y2 = 292
    MY2 = lambda e: Y2 - A * e
    o.append(text(20, 176, "2  Snapshots in space: E(z, t) = E(0, t + z/v), moving toward −z at v = 100 m/s", size=12.5, anchor="start", weight=600))
    o.append(haxis(48, 602, Y2, "z", [(k, f"{k}") for k in range(-300, 600, 100)], MZ, size=10))
    o.append(text(604, Y2 + 15, "m", size=10.5, anchor="start", fill="var(--muted)"))
    def snap(t):   # exact breakpoints: E0 at argument tau sits at z = 100 (tau - t)
        zb = [100.0 * (tau - t) for tau in tk]
        assert all(abs(float(E0(t + z / 100.0)) - e) < 1e-12 for z, e in zip(zb, ek))
        return [-320.0] + zb + [520.0], [0] + ek + [0]
    xs, es = snap(0.0); o.append(poly(xs, es, MZ, MY2, stroke="var(--accent)", w=2.6))
    xs, es = snap(1.0); o.append(poly(xs, es, MZ, MY2, stroke="var(--accent2)", w=2.2, dash="6 4"))
    o.append(text(MZ(150), MY2(1) - 8, "t = 0", size=11.5, fill="var(--accent)", weight=600))
    o.append(text(MZ(10), MY2(1) - 8, "t = 1 s", size=11.5, fill="var(--accent2)", weight=600))
    o.append(arrow(MZ(330), MY2(0.75), MZ(230), MY2(0.75), stroke="currentColor", w=2))
    o.append(text(MZ(340), MY2(0.75) + 4, "100 m in 1 s", size=11, anchor="start"))
    o.append(text(330, 344, "front (the part recorded first) at the −z end: same left-to-right order as the record — not mirrored", size=11, fill="var(--muted)"))
    o.append(svg_close())
    figure("wave-moving-waveform", "".join(o),
           "<strong>Slide 26's example: a wave travelling toward −z at 100 m/s.</strong> Panel 1 is the given record at z = 0. "
           "For a −z wave E(z,t) = E(0, t + z/v), so each question becomes a lookup at the shifted time t + z/v: "
           "2.2 s gives (a) 0.9, 0.4 s gives (b) 0.4, 1.6 s gives (c) 1.0. "
           "With the wrong sign, t − z/v, the three lookups land at −1.8, 6.4 and −0.4 s. All three miss the pulse and read 0 — "
           "a clear sign that the sign was wrong. "
           "Panel 2 converts the record into snapshots with E(z,0) = E(0, z/100): 1 s of record becomes 100 m of space, and the "
           "picture moves 100 m toward −z every second. For a −z wave the snapshot has the same left-to-right order as the "
           "record. A +z wave with the same record would appear reversed in space.")

# ------------------------------------------------------------------------------------------------ 5. worked problem: ramp pulse
def fig_wave_ramp_pulse_problem():
    W, H = 640, 340
    o = [svg_open(W, H)]
    Et1 = lambda y: np.where((y > 400) & (y < 700), 0.02 * (y - 400), 0.0)       # V/m at t = 3 us
    Eyt = lambda y, t: Et1(y - 200.0 * (t - 3.0))                                 # +y at 200 m/us
    # ---- panel 1: snapshots
    MYp = lin(-420, 1420, 52, 596); Y1 = 144; A = 13.0                            # 6 V/m -> 78 px
    MV = lambda e: Y1 - A * e
    o.append(text(20, 24, "1  Snapshots: the pulse slides toward +y at 200 m/µs without changing shape", size=12.5, anchor="start", weight=600))
    o.append(haxis(40, 606, Y1, "y", [(k, f"{k}") for k in range(-400, 1401, 200)], MYp, size=10))
    o.append(text(608, Y1 + 15, "m", size=10.5, anchor="start", fill="var(--muted)"))
    def ramp_pts(t):     # exact breakpoints of E(y,t): back at 200t - 200 (0 V/m), front at 200t + 100 (6 V/m, then a jump to 0)
        yb, yf = 200 * t - 200, 200 * t + 100
        xs = [-420, yb, yf, yf, 1420]; es = [0, 0, 6, 0, 0]
        assert abs(float(Eyt(np.array(yf - 1e-6), t)) - 6) < 1e-6 and float(Eyt(np.array(yb + 1e-6), t)) < 1e-6
        return xs, es
    for t, st, ww, dsh in ((0.0, "var(--accent2)", 2.2, "6 4"), (3.0, "var(--accent)", 2.6, None), (5.0, "var(--muted)", 1.8, "2 3")):
        xs, es = ramp_pts(t)
        o.append(poly(xs, es, MYp, MV, stroke=st, w=ww, dash=dsh))
    # 6 V/m scale mark on the left end of the axis
    o.append(line(MYp(-400), MV(6), MYp(-400) + 6, MV(6), w=1.0)); o.append(text(MYp(-400) + 9, MV(6) + 4, "6 V/m", size=10.5, anchor="start", fill="var(--muted)"))
    # curve labels beside the ramps (left of each rising ramp, where the plot is empty)
    o.append(text(MYp(-215), MV(3.4), "t = 0", size=11.5, anchor="end", fill="var(--accent2)", weight=600))
    o.append(text(MYp(-215), MV(3.4) + 14, "(part a)", size=10.5, anchor="end", fill="var(--accent2)"))
    o.append(text(MYp(385), MV(3.4), "t = 3 µs", size=11.5, anchor="end", fill="var(--accent)", weight=600))
    o.append(text(MYp(385), MV(3.4) + 14, "(given)", size=10.5, anchor="end", fill="var(--accent)"))
    o.append(text(MYp(1100), MV(6) - 8, "t = 5 µs", size=11.5, fill="var(--muted)", weight=600))
    # displacement arrow from the t = 0 front (y = 100 m) to the t = 3 us front (y = 700 m), above the curves
    o.append(arrow(MYp(100), MV(7.2), MYp(700), MV(7.2), stroke="currentColor", w=1.8))
    o.append(text(MYp(400), MV(7.2) - 6, "600 m in 3 µs", size=11))
    o.append(line(MYp(1000), Y1 + 2, MYp(1000), MV(6.6), stroke="var(--hi)", w=1.6, dash="4 3"))
    o.append(text(MYp(1118), MV(3.6), "probe at", size=11, anchor="start", fill="var(--hi)", weight=600))
    o.append(text(MYp(1118), MV(3.6) + 14, "y = 1 km", size=11, anchor="start", fill="var(--hi)", weight=600))
    # ---- panel 2: time record at y = 1 km
    MT = lin(-0.3, 8.3, 52, 596); Y2 = 300
    MV2 = lambda e: Y2 - A * e
    o.append(text(20, 196, "2  What the probe at y = 1 km records: the snapshot reversed (part c)", size=12.5, anchor="start", weight=600))
    o.append(haxis(40, 606, Y2, "t", [(k, f"{k}") for k in range(0, 9)], MT))
    o.append(text(608, Y2 + 15, "µs", size=10.5, anchor="start", fill="var(--muted)"))
    # record at y = 1 km: E = 4(6 - t) for 4.5 < t < 6 us (jump up at 4.5 us)
    tsr = [-0.3, 4.5, 4.5, 6.0, 8.3]; esr = [0, 0, 6, 0, 0]
    assert all(abs(float(Eyt(np.array(1000.0), np.array(tq))) - eq) < 1e-9 for tq, eq in ((4.5001, 4 * (6 - 4.5001)), (5.0, 4.0), (5.9, 0.4), (7.0, 0.0)))
    o.append(poly(tsr, esr, MT, MV2, stroke="var(--hi)", w=2.6))
    o.append(circle(MT(5.0), MV2(4.0), 4.5, fill="var(--accent)", stroke="none"))
    o.append(text(MT(5.0) + 9, MV2(4.0) - 4, "t = 5 µs: 4 V/m", size=11.5, anchor="start", fill="var(--accent)", weight=700))
    o.append(text(MT(4.5) - 6, MV2(6.0) + 4, "front arrives, 4.5 µs", size=11, anchor="end"))
    o.append(text(MT(6.0) + 8, Y2 - 8, "back passes, 6 µs", size=11, anchor="start"))
    o.append(svg_close())
    figure("wave-ramp-pulse-problem", "".join(o),
           "<strong>The worked problem in two pictures.</strong> Panel 1: the given profile at t = 3 µs (solid) is a ramp whose "
           "6 V/m edge is the front. Because the pulse travels toward +y at 200 m/µs, at t = 0 it was 600 m further back "
           "(dashed, part a), and at t = 5 µs it is 400 m further on (dotted), straddling the probe. Panel 2: the probe at "
           "y = 1 km sees the front first, so its record jumps to 6 V/m at 4.5 µs and then falls linearly to zero at 6 µs. "
           "That is the snapshot reversed left-to-right, as for every wave travelling toward +y. At t = 5 µs the probe reads "
           "4 V/m, matching the dotted snapshot at y = 1000 m.")

if __name__ == "__main__":
    for fn in (fig_wave_current_sheet, fig_wave_pulse_two_times, fig_wave_eh_triads, fig_wave_moving_waveform,
               fig_wave_ramp_pulse_problem):
        fn()
