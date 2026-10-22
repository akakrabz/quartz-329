#!/usr/bin/env python3
"""HW8 #5 infographics (info-*) for the ECE 329 site: wave propagation in free space, two styles.

Same helpers and conventions as figs.py. Running this module writes /home/claude/work/figs/<name>.html.
Version A (info-wave-anatomy): reference-poster style, one big labelled snapshot plus relations, units, example.
Version B (info-wave-journey): narrative flow style, four numbered stations, a story example, common mistakes.
Snapshot curves are numpy; every number and direction is checked in hw8/verify_info.py (np.cross).
Anatomy frame: screen right = z (travel), screen up = x (E), oblique down-right toward the viewer = y (H):
up x out = right, i.e. x_hat x y_hat = z_hat, a right-handed drawing.
Text widths are budgeted for a wide fallback sans (the preview has no Source Sans), so they fit on the site.
"""
from figs import *
from figs import _odot, _otimes, _sub, _tint
from figs_l18 import lin, poly

PI = np.pi
MU0 = 4e-7 * PI
EPS0 = 8.8541878128e-12
C = 1 / np.sqrt(MU0 * EPS0)
ETA0 = np.sqrt(MU0 / EPS0)
W = 760


def _lines(o, x, y, lines, size=14, lh=20, anchor="start", fill="currentColor", weight=None, math=False):
    for i, s in enumerate(lines):
        o.append(text(x, y + i * lh, s, size=size, anchor=anchor, fill=fill, weight=weight, math=math))


def _panel(o, x, y, w, h, color, op=0.10, rx=8, bar=True):
    o.append(_tint(x, y, w, h, color, op=op, rx=rx))
    if bar:
        o.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="5" height="{h:.1f}" rx="2" fill="{color}"/>')


def _pill(o, x, y, w, h, color, label, size=13):
    o.append(rect(x, y, w, h, fill="none", stroke=color, sw=1.4, rx=h / 2))
    o.append(text(x + w / 2, y + h / 2 + size * 0.36, label, size=size))


E0S, ETA0S, H0S = _sub("E", "0"), _sub("η", "0"), _sub("H", "0")
MU0S, EPS0S = _sub("μ", "0"), _sub("ε", "0")
JS = "J" + _sub("", "s")


# ================================================================================================ A. anatomy
def fig_info_anatomy():
    H = 1135
    o = [svg_open(W, H)]
    # ------------------------------------------------------------------ title band
    o.append(_tint(0, 0, W, 84, "var(--accent)", op=0.10))
    o.append(f'<rect x="0" y="0" width="{W}" height="6" fill="var(--accent)"/>')
    o.append(text(24, 44, "ANATOMY OF A PLANE WAVE", size=28, anchor="start", weight=700, fill="var(--accent)"))
    o.append(text(24, 68, "free space · x-polarized · travelling toward +z · everything you need on one sheet", size=14, anchor="start", fill="var(--muted)"))
    o.append(text(W - 24, 36, "ECE 329 · HW8 #5", size=12, anchor="end", fill="var(--muted)"))
    o.append(text(W - 24, 52, "version A · reference poster", size=12, anchor="end", fill="var(--muted)"))

    # ------------------------------------------------------------------ 1. snapshot
    o.append(text(24, 112, "1", size=18, anchor="start", weight=700, fill="var(--accent)"))
    o.append(text(42, 112, "The snapshot at t = 0: E, H and the direction of travel", size=18, anchor="start", weight=600))
    ox, oy = 118, 292                         # screen point of (x, y, z) = (0, 0, 0)
    lam = 1.0                                 # z in wavelengths
    kz, kx, ky = 258.0, 72.0, 70.0            # px per lambda, per E0, per H0

    def P3(x, y, z):
        return ox + kz * z + 0.60 * ky * y, oy - kx * x + 0.36 * ky * y

    z = np.linspace(0, 2 * lam, 801)
    e = np.cos(2 * PI * z / lam)              # E/E0 = cos(wt - beta z) at t = 0
    h = e.copy()                              # H/H0: same phase (eta0 real)
    # axes
    o.append(line(ox - 22, oy, ox + 2 * kz + 46, oy, w=1.3, arrow=True))
    o.append(text(ox + 2 * kz + 54, oy + 5, "z", size=15, anchor="start", math=True))
    o.append(line(ox, oy + 8, ox, oy - kx - 30, w=1.3, arrow=True))
    o.append(text(ox - 10, oy - kx - 26, "x", size=15, anchor="end", math=True))
    Xy, Yy = P3(0, 1.6, 0)
    o.append(line(ox, oy, Xy, Yy, w=1.3, arrow=True))
    o.append(text(ox + 52, oy + 58, "y", size=15, anchor="end", math=True))
    o.append(text(ox + 52, oy + 72, "(toward you)", size=11.5, anchor="end", fill="var(--muted)"))
    # field arrows every lambda/8, then the envelopes
    for zk in np.arange(0, 2 * lam + 1e-9, lam / 8):
        ek = float(np.cos(2 * PI * zk / lam))
        if abs(ek) < 0.05:
            continue
        X0, Y0 = P3(0, 0, zk)
        X1, Y1 = P3(ek, 0, zk)
        o.append(arrow(X0, Y0, X1, Y1, stroke="var(--accent)", w=1.5, small=True, opacity=0.85))
        X2, Y2 = P3(0, ek, zk)
        o.append(arrow(X0, Y0, X2, Y2, stroke="var(--accent2)", w=1.5, small=True, opacity=0.85))
    PX = [P3(ev, 0, zv) for ev, zv in zip(e, z)]
    o.append(path("M" + " L".join(f"{X:.1f},{Y:.1f}" for X, Y in PX), stroke="var(--accent)", w=2.6))
    PH = [P3(0, hv, zv) for hv, zv in zip(h, z)]
    o.append(path("M" + " L".join(f"{X:.1f},{Y:.1f}" for X, Y in PH), stroke="var(--accent2)", w=2.6))
    # lambda dimension between the crests at z = 0 and z = lambda
    Yd = oy - kx - 20
    o.append(line(ox, oy - kx - 4, ox, Yd - 8, w=0.9, dash="3 3", stroke="var(--muted)"))
    o.append(line(ox + kz, oy - kx - 4, ox + kz, Yd - 8, w=0.9, dash="3 3", stroke="var(--muted)"))
    o.append(arrow(ox + kz / 2, Yd, ox, Yd, stroke="currentColor", w=1.3, small=True))
    o.append(arrow(ox + kz / 2, Yd, ox + kz, Yd, stroke="currentColor", w=1.3, small=True))
    o.append(text(ox + kz / 2, Yd - 10, "λ = c/f = 2π/β  (crest to crest)", size=13.5, weight=600))
    # labels
    o.append(text(ox + 1.5 * kz, oy - kx - 34, "E = x̂ " + E0S + " cos(ωt − βz)   [V/m]", size=14.5, fill="var(--accent)", weight=600))
    Xc, Yc = P3(1, 0, 2 * lam)
    o.append(text(Xc + 8, Yc - 2, "crest: ωt − βz = 0", size=11.5, anchor="start", fill="var(--muted)"))
    o.append(text(ox + kz, oy + 100, "H = ŷ (" + E0S + "/" + ETA0S + ") cos(ωt − βz)   [A/m]", size=14.5, fill="var(--accent2)", weight=600))
    o.append(text(ox + kz, oy + 118, "same phase as E, perpendicular to E, |E|/|H| = " + ETA0S + " = 377 Ω everywhere", size=12.5, fill="var(--muted)"))
    Yt = oy + 152
    o.append(text(ox + kz, Yt - 10, "E × H = x̂ × ŷ = ẑ : the wave moves toward +z at c = 3×10⁸ m/s", size=13.5, fill="var(--hi)", weight=600))
    o.append(arrow(ox + 0.45 * kz, Yt + 2, ox + 1.55 * kz, Yt + 2, stroke="var(--hi)", w=2.6))
    o.append(text(ox + kz, Yt + 26, "every point of the pattern slides right by c·Δt; the shape itself never changes", size=12, fill="var(--muted)"))

    # ------------------------------------------------------------------ 2. relations
    y2 = 492
    o.append(text(24, y2, "2", size=18, anchor="start", weight=700, fill="var(--accent)"))
    o.append(text(42, y2, "The relations that define it", size=18, anchor="start", weight=600))
    cw, ch, gap = 232, 262, 8
    cols = [
        ("var(--accent)", "Wave equation", [
            ("∂²E/∂z² = " + MU0S + EPS0S + " ∂²E/∂t²", True),
            ("any f(t − z/c) solves it: +z", False),
            ("any g(t + z/c) solves it: −z", False),
            ("read direction from the sign:", False),
            ("(t − z/c) → +z,  (t + z/c) → −z", False),
            ("sinusoid: " + E0S + " cos(ωt − βz),", True),
            ("ωt − βz = ω(t − z/c)", True),
        ]),
        ("var(--accent2)", "Speed &amp; impedance", [
            ("v = c = 1/√(" + MU0S + EPS0S + ")", True),
            ("   ≈ 3×10⁸ m/s", True),
            (ETA0S + " = √(" + MU0S + "/" + EPS0S + ") ≈ 377 Ω", True),
            ("H = ẑ × E / " + ETA0S, True),
            ("|E| = " + ETA0S + " |H|, in phase", False),
            ("E ⊥ H ⊥ ẑ  (TEM wave)", False),
            ("no attenuation in free space", False),
        ]),
        ("var(--hi)", "λ, β and power", [
            ("λ = c/f,   ω = 2πf", True),
            ("β = 2π/λ = ω/c  [rad/m]", True),
            ("S = E × H  [W/m²]", True),
            ("⟨S⟩ = " + E0S + "²/(2" + ETA0S + ") = " + E0S + H0S + "/2", True),
            ("S is the Poynting vector;", False),
            ("⟨S⟩ ∥ ẑ: power rides the wave", False),
            ("peak S is twice ⟨S⟩", False),
        ]),
    ]
    for i, (color, title, items) in enumerate(cols):
        x = 24 + i * (cw + gap)
        _panel(o, x, y2 + 16, cw, ch, color)
        o.append(text(x + 16, y2 + 40, title, size=14.5, anchor="start", weight=700, fill=color))
        for j, (s, emph) in enumerate(items):
            o.append(text(x + 16, y2 + 70 + j * 30, s, size=14 if emph else 13, anchor="start",
                          fill="currentColor" if emph else "var(--muted)", weight=600 if emph else None))

    # ------------------------------------------------------------------ 3. units
    y3 = 804
    o.append(text(24, y3, "3", size=18, anchor="start", weight=700, fill="var(--accent)"))
    o.append(text(42, y3, "Units", size=18, anchor="start", weight=600))
    o.append(text(110, y3, "check: (V/m)·(A/m) = W/m²  and  (V/m)/(A/m) = Ω", size=13, anchor="start", fill="var(--muted)"))
    units = [("E", "V/m"), ("H", "A/m"), (ETA0S, "Ω"), ("S", "W/m²"), ("β", "rad/m"), ("ω", "rad/s"), ("f", "Hz"), ("λ", "m"), ("c", "m/s")]
    pw, ph, pg = 72, 28, 8
    for i, (q, u) in enumerate(units):
        _pill(o, 24 + i * (pw + pg), y3 + 14, pw, ph, "var(--accent)", f'<tspan style="font-weight:700">{q}</tspan>  {u}', size=13)

    # ------------------------------------------------------------------ 4. worked example
    y4 = 882
    o.append(text(24, y4, "4", size=18, anchor="start", weight=700, fill="var(--hi)"))
    o.append(text(42, y4, "Worked example: a 100 MHz wave with " + E0S + " = 3 V/m", size=18, anchor="start", weight=600))
    _panel(o, 24, y4 + 14, W - 48, 206, "var(--hi)", op=0.08)
    L = 40
    steps = [
        "λ = c/f = (3×10⁸ m/s)/(10⁸ Hz) = 3 m",
        "β = 2π/λ = 2π/3 = 2.094 rad/m  (= ω/c ✓)",
        "ω = 2πf = 2π×10⁸ = 6.283×10⁸ rad/s",
        H0S + " = " + E0S + "/" + ETA0S + " = 3/377 = 7.96 mA/m",
        "⟨S⟩ = " + E0S + "²/(2" + ETA0S + ") = 9/754 = 11.9 mW/m²",
    ]
    o.append(text(L, y4 + 40, "the five numbers", size=13, anchor="start", weight=700, fill="var(--hi)"))
    _lines(o, L, y4 + 64, steps, size=14, lh=27)
    R = 376
    o.append(text(R, y4 + 40, "the full fields", size=13, anchor="start", weight=700, fill="var(--hi)"))
    _lines(o, R, y4 + 64, [
        "E(z, t) = x̂ 3 cos(2π×10⁸ t − 2.094 z)  V/m",
        "H(z, t) = ŷ 7.96×10⁻³ cos(2π×10⁸ t − 2.094 z)  A/m",
    ], size=13, lh=27, weight=600)
    o.append(text(R, y4 + 118, "check: x̂ × ŷ = ẑ, and the −βz sign says +z ✓", size=13, anchor="start", fill="var(--muted)"))
    o.append(text(R, y4 + 136, "one period T = 1/f = 10 ns;  one wavelength = 3 m", size=13, anchor="start", fill="var(--muted)"))
    # one wavelength to scale next to a 1.7 m person
    MX = lin(0, 3, R, R + 200)
    yb = y4 + 182
    zz = np.linspace(0, 3, 301)
    o.append(poly(zz, np.cos(2 * PI * zz / 3), MX, lambda v: yb - 16 * v, stroke="var(--accent)", w=2))
    o.append(line(MX(0), yb, MX(3), yb, w=0.9, stroke="var(--muted)"))
    o.append(line(MX(0), yb + 12, MX(3), yb + 12, w=1.0, arrow=True, small=True)); o.append(line(MX(3), yb + 12, MX(0), yb + 12, w=1.0, arrow=True, small=True))
    o.append(text(MX(1.5), yb + 30, "λ = 3 m", size=12, fill="var(--muted)"))
    px = R + 250
    o.append(circle(px, yb - 29, 4, fill="currentColor", stroke="none"))
    o.append(line(px, yb - 25, px, yb - 8, w=1.6)); o.append(line(px, yb - 8, px - 6, yb + 4, w=1.6)); o.append(line(px, yb - 8, px + 6, yb + 4, w=1.6))
    o.append(line(px - 7, yb - 15, px + 7, yb - 15, w=1.6))
    o.append(text(px + 14, yb - 10, "1.7 m", size=12, anchor="start", fill="var(--muted)"))
    o.append(text(px + 14, yb + 4, "person", size=12, anchor="start", fill="var(--muted)"))

    o.append(text(24, H - 12, "AI-generated infographic for ECE 329 HW8 #5 (reference-poster prompt). Rounded constants: c ≈ 3×10⁸ m/s, " + ETA0S + " ≈ 377 Ω.",
                  size=11.5, anchor="start", fill="var(--muted)"))
    o.append(svg_close())
    figure("info-wave-anatomy", "".join(o),
           "<strong>Version A — Anatomy of a plane wave.</strong> AI-generated infographic made for HW8 #5 with a "
           "reference-poster prompt: one labelled snapshot (E along x, H along y, travel along z), the governing "
           "relations, a units strip and a worked 100 MHz example.")


# ================================================================================================ B. journey
SH = 190                                       # station panel height
TX = 300                                       # station text column


def _station(o, y, n, title, tag, body, punch):
    _panel(o, 24, y, W - 48, SH, "var(--accent2)", op=0.07, bar=False)
    o.append(circle(58, y + 34, 20, fill="var(--hi)", stroke="none"))
    o.append(text(58, y + 42, str(n), size=22, weight=700, fill="white"))
    o.append(text(92, y + 36, title, size=21, anchor="start", weight=700, fill="var(--accent2)"))
    o.append(text(92, y + 56, tag, size=13, anchor="start", fill="var(--muted)"))
    _lines(o, TX, y + 84, body, size=13.5, lh=20)
    o.append(text(TX, y + 182, punch, size=13, anchor="start", fill="var(--hi)", weight=600))


def fig_info_journey():
    H = 1288
    o = [svg_open(W, H)]
    # ------------------------------------------------------------------ title
    o.append(text(24, 42, "FROM ANTENNA TO RECEIVER", size=30, anchor="start", weight=700, fill="var(--accent2)"))
    o.append(text(24, 68, "a wave's journey through free space, told in four stops", size=16, anchor="start", math=True))
    o.append(text(W - 24, 36, "ECE 329 · HW8 #5", size=12, anchor="end", fill="var(--muted)"))
    o.append(text(W - 24, 52, "version B · narrative flow", size=12, anchor="end", fill="var(--muted)"))
    o.append(line(24, 84, W - 24, 84, w=1.2, stroke="var(--accent2)"))
    ys = [98, 302, 506, 710]
    o.append(line(58, ys[0] + 54, 58, ys[3] + 14, w=2.2, dash="6 6", stroke="var(--hi)", opacity=0.6))

    # ------------------------------------------------------------------ station 1: launch
    y = ys[0]
    _station(o, y, 1, "A current launches it", "the source: a sheet of current " + JS + " (an idealized antenna)", [
        "Shake charges and the field must respond. Right at a",
        "current sheet the field on BOTH sides is  E = −" + ETA0S + JS + "/2 :",
        "it points AGAINST the current, with magnitude",
        "(" + ETA0S + "/2) " + JS + " = 188 Ω × " + JS + ".  H = " + JS + "/2 completes the pair,",
        "and E × H points away from the sheet on each side.",
    ], "e.g. " + JS + " = 1 mA/m → |E| = 0.188 V/m, |H| = 0.5 mA/m")
    sx, sy = 170, y + 126                     # sheet sketch centre
    o.append(_tint(sx - 3, sy - 38, 6, 76, "var(--hi)", op=0.5))
    for k in (-22, 0, 22):
        o.append(arrow(sx, sy + k + 9, sx, sy + k - 9, stroke="var(--hi)", w=2, small=True))
    o.append(text(sx, sy - 46, JS + " (up)", size=12, fill="var(--hi)", weight=600))
    for side in (-1, 1):
        X = sx + side * 48
        o.append(arrow(X, sy - 12, X, sy + 12, stroke="var(--accent)", w=2.2))          # E down: opposite to Js
        o.append(text(X, sy + 28, "E", size=13, fill="var(--accent)", weight=700, math=True))
        o.append(arrow(sx + side * 22, sy + 42, sx + side * 80, sy + 42, stroke="currentColor", w=1.4, small=True))
    o.append(text(sx, sy + 56, "waves leave both ways", size=11.5, fill="var(--muted)"))

    # ------------------------------------------------------------------ station 2: travel
    y = ys[1]
    _station(o, y, 2, "It travels at c", "nothing in free space slows it or reshapes it", [
        "The field at distance z is a delayed copy of what the",
        "source did:  E(z, t) = f(t − z/c).  The delay is z/c,",
        "with  c = 1/√(" + MU0S + EPS0S + ") = 3×10⁸ m/s — 300 m every",
        "microsecond, 30 cm every nanosecond. The pulse keeps",
        "its shape; only its clock runs late by z/c.",
    ], "the minus sign in (t − z/c) is what says 'toward +z'")
    MX = lin(0, 450, 96, 262)
    yb = y + 146
    o.append(line(MX(0), yb, MX(450) + 8, yb, w=1.2, arrow=True)); o.append(text(MX(450) + 14, yb + 4, "z", size=13, anchor="start", math=True))
    for zm in (0, 300):
        o.append(line(MX(zm), yb - 3, MX(zm), yb + 3, w=1.0)); o.append(text(MX(zm), yb + 15, f"{zm} m", size=11.5, fill="var(--muted)"))
    zz = np.linspace(0, 450, 451)
    for z0, col, lab in ((0, "var(--accent)", "t = 0"), (300, "var(--accent2)", "t = 1 μs")):
        pulse = np.exp(-((zz - z0 - 40) / 28) ** 2)          # the same shape, shifted by c·t
        o.append(poly(zz, pulse, MX, lambda v: yb - 2 - 46 * v, stroke=col, w=2.4))
        o.append(text(MX(z0 + 40), yb - 56, lab, size=12, fill=col, weight=600))
    o.append(arrow(MX(95), yb - 28, MX(285), yb - 28, stroke="var(--hi)", w=1.6, small=True))
    o.append(text(MX(190), yb - 34, "c·Δt = 300 m", size=11.5, fill="var(--hi)"))

    # ------------------------------------------------------------------ station 3: power
    y = ys[2]
    _station(o, y, 3, "It carries power", "the Poynting vector S = E × H, in W/m²", [
        "Averaged over a cycle, a sinusoidal wave delivers",
        "⟨S⟩ = " + E0S + "²/(2" + ETA0S + ") watts through each square metre",
        "facing it, flowing along E × H.  A source radiating P",
        "equally in all directions spreads it over a sphere of",
        "area 4πr², so ⟨S⟩ = P/(4πr²): twice as far, ¼ as much.",
    ], "fields fall as 1/r, power density as 1/r²")
    cx, cy = 150, y + 124
    o.append(circle(cx, cy, 5, fill="var(--hi)", stroke="none"))
    for rr, op in ((18, 0.9), (36, 0.6), (54, 0.35)):
        o.append(circle(cx, cy, rr, stroke="var(--accent2)", w=1.6, opacity=op))
    for ang in np.linspace(-60, 60, 5):
        a = np.deg2rad(ang)
        o.append(arrow(cx + 8 * np.cos(a), cy + 8 * np.sin(a), cx + 62 * np.cos(a), cy + 62 * np.sin(a), stroke="var(--accent)", w=1.3, small=True, opacity=0.7))
    _lines(o, cx + 72, cy - 22, ["isotropic:", "r → 2r", "⟨S⟩ → ⟨S⟩/4", "P over 4πr²"], size=12, lh=16, fill="var(--muted)")

    # ------------------------------------------------------------------ station 4: receiver
    y = ys[3]
    _station(o, y, 4, "A receiver reads it", "what an antenna at z sees: E, and H for free", [
        "Whatever E arrives, H arrives with it, perpendicular",
        "and in phase: |H| = |E|/" + ETA0S + ", with " + ETA0S + " = √(" + MU0S + "/" + EPS0S + ") = 377 Ω",
        "fixed by vacuum. Which way did it come from? Read the",
        "argument, not the amplitude: cos(ωt − βz) is heading",
        "to +z, cos(ωt + βz) to −z.",
    ], "E × H always points the way the wave travels")
    ax, ay = 150, y + 118
    o.append(line(ax + 92, ay - 38, ax + 92, ay + 38, w=2.6))                                 # receiving antenna
    o.append(line(ax + 92, ay + 38, ax + 78, ay + 52, w=1.6)); o.append(line(ax + 92, ay + 38, ax + 106, ay + 52, w=1.6))
    o.append(text(ax + 92, ay + 66, "receiver", size=11.5, fill="var(--muted)"))
    o.append(arrow(ax - 20, ay + 18, ax - 20, ay - 26, stroke="var(--accent)", w=2.4))      # E up
    o.append(text(ax - 30, ay - 28, "E", size=13, anchor="end", fill="var(--accent)", weight=700, math=True))
    o.append(_odot(ax + 10, ay - 4, r=7, color="var(--accent2)"))                             # H out of the page
    o.append(text(ax + 22, ay - 8, "H (out)", size=12, anchor="start", fill="var(--accent2)", weight=600))
    o.append(arrow(ax - 44, ay + 40, ax + 44, ay + 40, stroke="var(--hi)", w=2.0, small=True))
    o.append(text(ax - 58, ay - 2, "wave", size=11, anchor="end", fill="var(--muted)"))
    _lines(o, ax - 50, ay + 58, ["up × out = right", "E × H → +z ✓"], size=11.5, lh=14, fill="var(--hi)")

    # ------------------------------------------------------------------ the story in numbers
    y5 = 914
    _panel(o, 24, y5, W - 48, 200, "var(--hi)", op=0.08)
    o.append(text(42, y5 + 30, "The story in numbers", size=20, anchor="start", weight=700, fill="var(--hi)"))
    o.append(text(42, y5 + 52, "a 50 kW transmitter radiating equally in all directions; you stand 10 km away", size=14, anchor="start", math=True))
    tx0, tx1, ty = 60, 270, y5 + 104
    o.append(line(tx0, ty, tx1, ty, w=2.0, stroke="var(--hi)", arrow=True))
    o.append(circle(tx0, ty, 6, fill="var(--hi)", stroke="none")); o.append(line(tx0, ty - 6, tx0, ty - 30, w=2.2))
    o.append(text(tx0, ty + 20, "t = 0", size=12, weight=600)); o.append(text(tx0 - 8, ty + 34, "50 kW leaves", size=11.5, anchor="start", fill="var(--muted)"))
    o.append(circle(tx1 - 4, ty - 22, 4, fill="currentColor", stroke="none")); o.append(line(tx1 - 4, ty - 18, tx1 - 4, ty - 4, w=1.6))
    o.append(text(tx1 - 4, ty + 20, "t = 33.3 μs", size=12, weight=600)); o.append(text(tx1 - 10, ty + 34, "it reaches you", size=11.5, fill="var(--muted)"))
    o.append(text((tx0 + tx1) / 2, ty - 10, "10 km at 300 m/μs", size=12, fill="var(--hi)"))
    _lines(o, 42, y5 + 158, ["a tenth of a volt per metre, half a milliamp", "per metre, 40 μW on each square metre —", "and a receiver hears it easily."], size=12.5, lh=16, fill="var(--muted)")
    rows = [
        ("delay", "r/c = 10⁴ m / (3×10⁸ m/s) = 33.3 μs"),
        ("sphere", "4πr² = 4π(10⁴)² = 1.26×10⁹ m²  (1257 km²)"),
        ("⟨S⟩", "P/(4πr²) = 5×10⁴ / 1.26×10⁹ = 39.8 μW/m²"),
        (E0S, "√(2" + ETA0S + "⟨S⟩) = √(2·377·39.8×10⁻⁶) = 0.173 V/m"),
        (H0S, E0S + "/" + ETA0S + " = 0.173/377 = 0.459 mA/m"),
    ]
    for i, (k, v) in enumerate(rows):
        yy = y5 + 86 + i * 25
        o.append(text(378, yy, k, size=13.5, anchor="end", weight=700, fill="var(--hi)"))
        o.append(text(390, yy, v, size=13.5, anchor="start"))

    # ------------------------------------------------------------------ common mistakes
    y6 = 1140
    o.append(text(24, y6, "Common mistakes", size=18, anchor="start", weight=700, fill="var(--accent2)"))
    cw, gap = 232, 8
    cards = [
        ("c vs v", ["c = 3×10⁸ m/s holds in vacuum", "(and air). In a dielectric", "v = c/√ε" + _sub("", "r") + ": glass, ε" + _sub("", "r") + " = 2.25,", "gives v = c/1.5 and λ = λ" + _sub("", "0") + "/1.5."]),
        ("peak vs average", [E0S + "²/" + ETA0S + " is the PEAK power", "density. Averaged over a", "cycle it is half as much:", "⟨S⟩ = " + E0S + "²/(2" + ETA0S + ") = " + E0S + H0S + "/2."]),
        ("which way it travels", ["cos(ωt − βz) travels to +z,", "cos(ωt + βz) to −z. The sign", "of " + E0S + " says nothing about", "direction; it is just a phase."]),
    ]
    for i, (title, body) in enumerate(cards):
        x = 24 + i * (cw + gap)
        _panel(o, x, y6 + 12, cw, 104, "var(--accent2)", op=0.09, bar=False)
        o.append(text(x + 14, y6 + 36, "✗ " + title, size=14, anchor="start", weight=700, fill="var(--hi)"))
        _lines(o, x + 14, y6 + 57, body, size=12.5, lh=17)
    o.append(text(24, H - 12, "AI-generated infographic for ECE 329 HW8 #5 (narrative, first-year-reader prompt). Rounded: c ≈ 3×10⁸ m/s, " + ETA0S + " ≈ 377 Ω.",
                  size=11.5, anchor="start", fill="var(--muted)"))
    o.append(svg_close())
    figure("info-wave-journey", "".join(o),
           "<strong>Version B — From antenna to receiver.</strong> AI-generated infographic made for HW8 #5 with a "
           "narrative, first-year-reader prompt: four numbered stops (launch, travel, power, reception), a 50 kW / "
           "10 km story worked in numbers, and a common-mistakes strip.")


if __name__ == "__main__":
    fig_info_anatomy()
    fig_info_journey()
