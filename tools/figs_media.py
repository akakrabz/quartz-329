#!/usr/bin/env python3
"""Toolkit page 08 figures (media-*): waves in dielectrics, conductors, plasmas and on lines.
Same helpers and conventions as figs.py, figs_l18.py and figs_l23.py. Every curve is computed with numpy from
gamma = sqrt(j w mu (sigma + j w eps)), eta = sqrt(j w mu / (sigma + j w eps)); every number shown is checked in
media/verify_media.py (PASS lines in media/verify_media.out).
Materials (as figs_l23.py): copper 5.8e7 S/m; seawater 4 S/m, eps_r 81 (the notes); moist soil 1e-2 S/m, eps_r 10;
fresh water 1e-3 S/m, eps_r 80. Ionospheric plasma f_p = 9 MHz (N = 1e12 m^-3; Kudeki, ECE 458 notes, f_p = sqrt(80.6 N)).
Direction (figure media-tl-analogy): screen X right = physics z (travel), screen Y up = physics x (E), so physics y =
z cross x = X cross Y = Z, out of the screen: H along +y is drawn as odot; E x H = x cross y = z, to the right.
"""
from figs import *
from figs import _sub, _tint, _odot, _zigzag, _coil
from figs_l18 import lin, poly
from figs_l23 import exact, tlabel, logticks_x, vlogaxis, mu0, eps0, c0, DB, _sup, fc_of

A, B, C, M = "var(--accent)", "var(--accent2)", "var(--hi)", "var(--muted)"


def _card(o, x, y, w, h, title, lines, color, ts=13, size=11.5, lh=16, op=0.09):
    o.append(_tint(x, y, w, h, color, op=op, rx=7))
    o.append(rect(x, y, w, h, stroke=color, sw=1.5, rx=7))
    o.append(text(x + w / 2, y + 18, title, size=ts, weight=700, fill=color))
    yy = y + 18 + lh + 1
    for ln in lines:
        if isinstance(ln, tuple):
            s, kw = ln
        else:
            s, kw = ln, {}
        o.append(text(x + w / 2, yy, s, size=kw.get("size", size), fill=kw.get("fill", "currentColor"),
                      weight=kw.get("weight")))
        yy += lh


def _arc(cx, cy, r, a0, a1, color="currentColor", w=1.3):
    """arc of radius r from angle a0 to a1 (degrees, math sense, screen y up)"""
    x0, y0 = cx + r * math.cos(math.radians(a0)), cy - r * math.sin(math.radians(a0))
    x1, y1 = cx + r * math.cos(math.radians(a1)), cy - r * math.sin(math.radians(a1))
    large = 1 if abs(a1 - a0) > 180 else 0
    sweep = 0 if a1 > a0 else 1
    return path(f"M{x0:.1f},{y0:.1f} A{r},{r} 0 {large} {sweep} {x1:.1f},{y1:.1f}", stroke=color, w=w)


def _nb(s):
    return s.replace("  ", "&#160;&#160;")


# ------------------------------------------------------------------------------------------ 1. the family of wave equations
def fig_media_wave_equations():
    W, H = 760, 650
    o = [svg_open(W, H)]
    o.append(text(20, 24, "One equation, many media", size=18, anchor="start", weight=700))
    o.append(text(20, 43, "Every wave equation of Lectures 18–30 is the same equation with one term kept, dropped or renamed.",
                  size=12, anchor="start", fill=M))
    # row A: Maxwell
    o.append(_tint(150, 56, 460, 58, "currentColor", op=0.05, rx=7))
    o.append(rect(150, 56, 460, 58, stroke="currentColor", sw=1.3, rx=7))
    o.append(text(380, 76, "Maxwell's curl equations — source-free, homogeneous, linear", size=12.5, weight=700))
    o.append(text(380, 97, _nb("∇×E = −μ ∂H/∂t        ∇×H = σE + ε ∂E/∂t"), size=13.5))
    o.append(arrow(380, 114, 380, 140, stroke="currentColor", w=1.6))
    o.append(text(392, 132, "curl of Faraday, ∇·E = 0", size=11, anchor="start", fill=M))
    # row B: the general lossy wave equation, term by term
    o.append(_tint(110, 142, 540, 88, A, op=0.10, rx=8))
    o.append(rect(110, 142, 540, 88, stroke=A, sw=1.8, rx=8))
    o.append(text(380, 162, "The general wave equation (time domain)", size=13, weight=700, fill=A))
    yy = 194
    o.append(text(278, yy, "∇²E =", size=17, anchor="end"))
    o.append(text(330, yy, "μσ ∂E/∂t", size=17))
    o.append(text(398, yy, "+", size=17))
    o.append(text(470, yy, "με ∂²E/∂t²", size=17))
    o.append(text(330, yy + 22, "conduction: loss", size=11, fill=C, weight=600))
    o.append(text(470, yy + 22, "displacement: waves", size=11, fill=B, weight=600))
    # row C: three branches
    yC, hC, wC = 278, 128, 228
    xs = (14, 266, 518)
    o.append(arrow(240, 230, 128, yC - 2, stroke=B, w=1.8))
    o.append(arrow(380, 230, 380, yC - 2, stroke=A, w=1.8))
    o.append(arrow(520, 230, 632, yC - 2, stroke=C, w=1.8))
    o.append(tlabel(150, 252, "σ = 0", size=11, anchor="end", fill=B, weight=600))
    o.append(tlabel(388, 256, "one frequency: ∂/∂t → jω", size=11, anchor="start", fill=A, weight=600))
    o.append(tlabel(612, 252, "σ ≫ ωε", size=11, anchor="start", fill=C, weight=600))
    _card(o, xs[0], yC, wC, hC, "Lossless wave equation", [
        ("∇²E = με ∂²E/∂t²", {"size": 13}),
        "E = f(t ∓ z/v),  v = 1/√(με)",
        "any pulse keeps its shape",
        "η = √(μ/ε) real: E, H in step",
        ("Lectures 18–19", {"fill": M, "size": 10.5}),
    ], B)
    _card(o, xs[1], yC, wC, hC, "Helmholtz equation (phasor)", [
        ("∇²Ẽ = γ²Ẽ", {"size": 13}),
        "γ² = jωμ(σ + jωε)",
        "Ẽ = E₀ e^(∓γz),  γ = α + jβ",
        "covers every case below",
        ("Lectures 21–22", {"fill": M, "size": 10.5}),
    ], A)
    _card(o, xs[2], yC, wC, hC, "Diffusion equation", [
        ("∇²E = μσ ∂E/∂t", {"size": 13}),
        "the heat equation: fields soak in",
        "pulses smear, no fixed speed",
        "phasor form: γ² = jωμσ",
        ("good conductor (EM GeoSci: quasi-static)", {"fill": M, "size": 10.5}),
    ], C)
    # row D: gamma^2 in each medium
    yD = 452
    o.append(arrow(380, yC + hC, 380, yD - 26, stroke=A, w=1.8))
    o.append(text(380, yD - 8, "γ² in each medium the course meets", size=13, weight=700))
    cw, gap, x0, hD = 142, 8, 14, 172
    cards = [
        ("perfect dielectric", B, ["γ² = −ω²με", "γ = jβ,  β = ω√(με)", "travels, no decay", "τ = 0", ("L18–21", {"fill": M, "size": 10.5})]),
        ("lossy medium", A, ["γ² = jωμσ − ω²με", "γ = α + jβ", "travels and decays", "H lags E by τ = ∠η", ("L22–23", {"fill": M, "size": 10.5})]),
        ("good conductor", C, ["γ² ≈ jωμσ", "γ = (1 + j)/δ", "gone within one λ", "τ = 45°", ("L23", {"fill": M, "size": 10.5})]),
        ("plasma (no collisions)", "var(--accent)", ["σ = −jNq²/(mω)", "γ² = (" + _sub("ω", "p") + "² − ω²)/c²", "ω > " + _sub("ω", "p") + ": travels, " + _sub("v", "p") + " > c",
                                                      "ω < " + _sub("ω", "p") + ": evanescent", ("L21, L24", {"fill": M, "size": 10.5})]),
        ("transmission line", B, ["d²Ṽ/dz² = γ²Ṽ", "γ² = (𝓡 + jω𝓛)", "        × (𝓖 + jω𝓒)", "same algebra, V and I", ("L27–30", {"fill": M, "size": 10.5})]),
    ]
    for i, (t, col, lines) in enumerate(cards):
        _card(o, x0 + i * (cw + gap), yD, cw, hD - 46, t, [l if isinstance(l, tuple) else (_nb(l), {}) for l in lines], col,
              ts=12, size=11.2, lh=17)
    o.append(text(380, yD + hD - 20, "Read γ off the solution e^(−γz): α = Re γ (decay, Np/m), β = Im γ (phase, rad/m); η = jωμ/γ.",
                  size=11.5, fill=M))
    o.append(text(380, yD + hD - 2, "Plasma: Kudeki's ECE 458 notes; diffusion vs waves: EM GeoSci, Løseth et al. (2006).",
                  size=10.5, fill=M))
    o.append(svg_close())
    figure("media-wave-equations", "".join(o),
           "<strong>One equation, many media.</strong> Taking the curl of Faraday's law and substituting Ampère's law gives "
           "one time-domain equation with a conduction term (loss) and a displacement term (waves). Drop the conduction "
           "term and you have the lossless wave equation of Lectures 18–19; drop the displacement term and it becomes a "
           "diffusion equation, the good conductor; at one frequency it becomes the Helmholtz equation, whose γ² covers "
           "every medium, a collisionless plasma, and the voltage on a transmission line.")


# ------------------------------------------------------------------------------------------ 2. angle bookkeeping
def fig_media_angles():
    W, H = 760, 360
    o = [svg_open(W, H)]
    th = 50.0
    p = math.tan(math.radians(th))
    o.append(text(20, 24, "Where the angles come from:  θ (loss angle),  τ = ∠η,  ∠γ", size=16, anchor="start", weight=700))
    o.append(text(20, 43, f"Drawn for tan θ = σ/ωε = {p:.2f} (θ = 50°); lengths normalized by the lossless values.", size=12,
                  anchor="start", fill=M))
    # panel frames
    for i, t in enumerate(("1  the current: (σ + jωε)Ẽ", "2  γ² = jωμ(σ + jωε)  →  γ", "3  η² = jωμ/(σ + jωε)  →  η")):
        x = 14 + i * 250
        o.append(rect(x, 56, 238, 254, stroke=M, sw=1.0, rx=6, opacity=0.6))
        o.append(text(x + 10, 76, t, size=12.5, anchor="start", weight=700))
    # ---- panel 1: origin bottom-left
    ox, oy, S = 44, 270, 92
    o.append(line(ox - 10, oy, ox + 196, oy, w=1.1, arrow=True, small=True))
    o.append(line(ox, oy + 10, ox, oy - 170, w=1.1, arrow=True, small=True))
    o.append(text(ox + 196, oy + 14, "Re", size=10.5, anchor="end", fill=M))
    o.append(text(ox + 6, oy - 162, "Im", size=10.5, anchor="start", fill=M))
    xr, yi = ox + p * S, oy - S
    o.append(arrow(ox, oy, xr, oy, stroke=C, w=2.4))
    o.append(arrow(ox, oy, ox, yi, stroke=B, w=2.4))
    o.append(line(xr, oy, xr, yi, stroke=M, w=1, dash="3 3"))
    o.append(line(ox, yi, xr, yi, stroke=M, w=1, dash="3 3"))
    o.append(arrow(ox, oy, xr, yi, stroke=A, w=2.6))
    o.append(_arc(ox, oy, 40, 40, 90, color="currentColor"))
    o.append(text(ox + 22, oy - 48, "θ", size=14, math=True, weight=700))
    o.append(text((ox + xr) / 2, oy + 16, "σẼ: conduction, heats", size=10.5, fill=C, weight=600))
    o.append(text(ox - 4, yi - 8, "jωεẼ: displacement", size=10.5, anchor="start", fill=B, weight=600))
    o.append(text(xr + 4, yi + 14, "total", size=10.5, anchor="start", fill=A, weight=600))
    o.append(text(139, 300, "tan θ = σ/ωε  (the loss tangent)", size=11.5, weight=600))
    # ---- panel 2: origin centre-bottom
    ox2, oy2, S2 = 14 + 250 + 130, 270, 82
    o.append(line(ox2 - 120, oy2, ox2 + 100, oy2, w=1.1, arrow=True, small=True))
    o.append(line(ox2, oy2 + 10, ox2, oy2 - 170, w=1.1, arrow=True, small=True))
    o.append(text(ox2 + 100, oy2 + 14, "Re", size=10.5, anchor="end", fill=M))
    o.append(text(ox2 + 6, oy2 - 162, "Im", size=10.5, anchor="start", fill=M))
    g2 = 1j * (p + 1j)
    g = np.sqrt(g2)
    X2, Y2 = ox2 + g2.real * S2, oy2 - g2.imag * S2
    Xg, Yg = ox2 + g.real * S2, oy2 - g.imag * S2
    o.append(arrow(ox2, oy2, X2, Y2, stroke=M, w=2.0))
    o.append(text(X2 - 4, Y2 - 8, "γ²  (×j: +90°)", size=10.5, anchor="middle", fill=M, weight=600))
    o.append(line(Xg, oy2, Xg, Yg, stroke=C, w=1.2, dash="3 3"))
    o.append(line(ox2, Yg, Xg, Yg, stroke=B, w=1.2, dash="3 3"))
    o.append(arrow(ox2, oy2, Xg, Yg, stroke=A, w=2.8))
    o.append(text(Xg + 6, Yg - 4, "γ", size=15, anchor="start", math=True, weight=700, fill=A))
    o.append(text(Xg, oy2 + 15, "α", size=12, math=True, fill=C, weight=700))
    o.append(text(ox2 - 9, Yg + 4, "β", size=12, anchor="end", math=True, fill=B, weight=700))
    o.append(_arc(ox2, oy2, 30, 0, 65, color="currentColor"))
    o.append(text(ox2 + 36, oy2 - 20, "65°", size=10.5, anchor="start"))
    o.append(text(389, 300, "√ halves the angle: ∠γ = 90° − θ/2", size=11.5, weight=600))
    # ---- panel 3
    ox3, oy3, S3 = 14 + 500 + 30, 270, 165
    o.append(line(ox3 - 10, oy3, ox3 + 196, oy3, w=1.1, arrow=True, small=True))
    o.append(line(ox3, oy3 + 10, ox3, oy3 - 170, w=1.1, arrow=True, small=True))
    o.append(text(ox3 + 196, oy3 + 14, "Re", size=10.5, anchor="end", fill=M))
    o.append(text(ox3 + 6, oy3 - 162, "Im", size=10.5, anchor="start", fill=M))
    e2 = 1j / (p + 1j)
    e = np.sqrt(e2)
    Xe2, Ye2 = ox3 + e2.real * S3, oy3 - e2.imag * S3
    Xe, Ye = ox3 + e.real * S3, oy3 - e.imag * S3
    o.append(arrow(ox3, oy3, Xe2, Ye2, stroke=M, w=2.0))
    o.append(text(Xe2 - 6, Ye2 - 8, "η²: angle θ", size=10.5, anchor="middle", fill=M, weight=600))
    o.append(arrow(ox3, oy3, Xe, Ye, stroke=B, w=2.8))
    o.append(text(Xe + 6, Ye + 2, "η", size=15, anchor="start", math=True, weight=700, fill=B))
    o.append(_arc(ox3, oy3, 62, 0, 25, color=B, w=1.6))
    o.append(text(ox3 + 70, oy3 - 10, "τ = θ/2 = 25°", size=11, anchor="start", fill=B, weight=600))
    o.append(text(639, 300, "H lags E by τ (0° … 45°)", size=11.5, weight=600))
    o.append(text(W / 2, 334, _nb("τ = θ/2     ∠γ = 90° − τ     α/β = tan τ     |γ| ∝ (1 + tan²θ)^¼,  |η| ∝ (1 + tan²θ)^−¼"),
                  size=12.5, weight=600, fill=A))
    o.append(text(W / 2, 352, "Here |γ|/ω√(με) = 1.25, |η|/√(μ/ε) = 0.80, α/β = 0.47.", size=11, fill=M))
    o.append(svg_close())
    figure("media-angles", "".join(o),
           "<strong>Three angles, one origin.</strong> The total current (σ + jωε)Ẽ leans away from the displacement "
           "current by the loss angle θ, with tan θ = σ/ωε. Multiplying by jωμ turns it a further 90° (γ²), and the square "
           "root halves the angle, so γ sits at 90° − θ/2, between 45° (good conductor) and 90° (lossless). Dividing "
           "instead gives η² at θ, so τ = ∠η = θ/2. The loss tangent is tan θ; τ is half of θ, not the tangent itself.")


# ------------------------------------------------------------------------------------------ 3. snapshots in four media
def fig_media_snapshots():
    W, H = 760, 640
    o = [svg_open(W, H)]
    o.append(text(20, 24, "The same wave in four media: a snapshot at t = 0", size=16, anchor="start", weight=700))
    o.append(text(20, 43, "solid: E/E₀   dashed: |η|H/E₀ (scaled to E)   dotted: envelope ±e^(−αz)   travel → +z",
                  size=12, anchor="start", fill=M))
    X0, X1 = 64, 520
    rows = [
        (0.0, "lossless dielectric", B, ["σ = 0,  p = 0", "τ = 0: E and H in step", "δ = ∞, no decay", "0 dB per λ"]),
        (0.2, "imperfect dielectric", A, ["p = σ/ωε = 0.2", "τ = 5.7°,  α/β = 0.099", "δ = 1.61 λ", "5.4 dB per λ"]),
        (100.0, "good conductor", C, ["p = 100", "τ = 44.7° ≈ 45°,  α ≈ β", "δ = 0.16 λ ≈ λ/2π", "54 dB per λ"]),
    ]
    rh, top = 132, 58
    zz = np.linspace(0, 2, 900)
    MX = lin(0, 2, X0, X1)
    for i, (p, name, col, info) in enumerate(rows):
        y0 = top + i * rh
        yc = y0 + 62
        MY = lin(-1, 1, yc + 50, yc - 50)
        tau = math.atan(p) / 2
        ab = math.tan(tau)
        al = 2 * math.pi * ab          # alpha per lambda (beta = 2 pi per lambda)
        env = np.exp(-al * zz)
        o.append(line(X0, yc, X1 + 8, yc, w=1.0, opacity=0.5))
        o.append(line(X0, yc - 52, X0, yc + 52, w=1.0, opacity=0.5))
        for k in (0.5, 1, 1.5, 2):
            o.append(line(MX(k), yc - 3, MX(k), yc + 3, w=1.0))
        if i == 2:
            for k, lab in ((0.5, "λ/2"), (1, "λ"), (1.5, "3λ/2"), (2, "2λ")):
                o.append(text(MX(k), yc + 66, lab, size=10, fill=M))
        if p > 0:
            o.append(poly(zz, env, MX, MY, stroke=M, w=1.1, dash="2 3"))
            o.append(poly(zz, -env, MX, MY, stroke=M, w=1.1, dash="2 3"))
            d = 1 / al
            if d < 2:
                o.append(line(MX(d), yc - 50, MX(d), yc + 50, stroke=col, w=1.0, dash="5 3"))
                o.append(tlabel(MX(d) + 4, yc - 38, "z = δ: 1/e", size=10, anchor="start", fill=col, weight=600))
        o.append(poly(zz, env * np.cos(2 * np.pi * zz), MX, MY, stroke=col, w=2.3))
        o.append(poly(zz, env * np.cos(2 * np.pi * zz + tau), MX, MY, stroke="var(--accent2)" if col != B else A, w=1.8, dash="6 4"))
        if i == 2:
            # mark the H crest trailing the E crest by tau/2pi of a wavelength
            zE, zH = 1.0, 1.0 - tau / (2 * math.pi)
            o.append(text(MX(0.62), yc - 22, "dashed H trails E by λ/8: τ = 45°", size=10.5, anchor="start", fill=M))
        o.append(text(X1 + 22, y0 + 22, name, size=13, anchor="start", weight=700, fill=col))
        for j, s in enumerate(info):
            o.append(text(X1 + 22, y0 + 42 + j * 17, _nb(s), size=11.5, anchor="start"))
        o.append(text(X0 - 8, yc + 4, "0", size=10, anchor="end", fill=M))
    o.append(text(X1 + 14, top + 2 * rh + 62 + 66, "z", size=12, anchor="start", math=True))
    # row 4: plasma below cutoff, evanescent
    y0 = top + 3 * rh + 22
    yc = y0 + 66
    o.append(line(14, y0 - 10, W - 14, y0 - 10, w=0.8, opacity=0.4))
    MXe = lin(0, 4, X0, X1)
    MYe = lin(-1, 1, yc + 50, yc - 50)
    ze = np.linspace(0, 4, 400)
    o.append(line(X0, yc, X1 + 8, yc, w=1.0, opacity=0.5))
    o.append(line(X0, yc - 52, X0, yc + 52, w=1.0, opacity=0.5))
    for k, lab in ((1, "1/κ"), (2, "2/κ"), (3, "3/κ"), (4, "4/κ")):
        o.append(line(MXe(k), yc - 3, MXe(k), yc + 3, w=1.0))
        o.append(text(MXe(k), yc + 66, lab, size=10, fill=M))
    for wt, op in ((0, 1.0), (math.pi / 3, 0.6), (2 * math.pi / 3, 0.35)):
        o.append(poly(ze, np.exp(-ze) * math.cos(wt), MXe, MYe, stroke=A, w=2.0, opacity=op))
    o.append(text(MXe(1.6), yc + 30, "bold → faint: ωt = 0, π/3, 2π/3", size=10.5, anchor="start", fill=A))
    o.append(text(MXe(1.6), yc - 32, "no crests, nothing travels:", size=11, anchor="start", fill=M))
    o.append(text(MXe(1.6), yc - 16, "the field rises and falls in place", size=11, anchor="start", fill=M))
    o.append(text(X0 - 8, yc + 4, "0", size=10, anchor="end", fill=M))
    o.append(text(X1 + 22, y0 + 22, "plasma below cutoff", size=13, anchor="start", weight=700, fill=A))
    for j, s in enumerate(["f = " + _sub("f", "p") + "/2:  γ = κ, real", "η = j|η|: H lags E by 90°",
                           "⟨S⟩ = ½Re{ẼH̃*} = 0", "ionosphere, " + _sub("f", "p") + " = 9 MHz: 1/κ = 6.1 m"]):
        o.append(text(X1 + 22, y0 + 42 + j * 17, s, size=11.5, anchor="start"))
    o.append(text(X1 + 14, yc + 66, "z", size=12, anchor="start", math=True))
    o.append(svg_close())
    figure("media-snapshots", "".join(o),
           "<strong>What the wave looks like.</strong> Rows 1–3: the same snapshot e<sup>−αz</sup>cos(βz) of E (solid) and "
           "|η|H (dashed) for three values of the loss tangent p = σ/ωε, computed from the exact γ and η. As p grows the "
           "envelope steepens and H slides back by τ/2π of a wavelength, up to λ/8 in a good conductor, where the wave "
           "is gone within one wavelength (54.6 dB per λ). Row 4: below its plasma frequency a collisionless plasma "
           "has a real γ: the field decays without oscillating in z, E and H are 90° apart in time, and no power flows in.")


# ------------------------------------------------------------------------------------------ 4. dispersion and loss per wavelength
def fig_media_dispersion():
    W, H = 760, 700
    o = [svg_open(W, H)]
    o.append(text(20, 24, "Phase velocity across media, and loss per wavelength", size=16, anchor="start", weight=700))
    o.append(text(20, 43, "exact γ = √(jωμ(σ + jωε)), μ = μ₀;  marks: the crossover " + _sub("f", "c") + " = σ/2πε (p = 1)",
                  size=12, anchor="start", fill=M))
    # ---------- panel 1
    L0, L1 = 0.0, 11.0
    X0, X1 = 92, 600
    MX = lin(L0, L1, X0, X1)
    Y0, Y1 = 384, 64
    MY = lin(-9.5, 1.7, Y0, Y1)
    o.append(vlogaxis(X0, Y0, Y1, MY, range(-9, 2), [(-9, "10⁻⁹"), (-7, "10⁻⁷"), (-5, "10⁻⁵"), (-3, "10⁻³"),
                                                    (-1, "0.1"), (0, "1"), (1, "10")]))
    o.append(text(X0 - 50, (Y0 + Y1) / 2, _sub("v", "p") + "/c", size=12, rotate=-90))
    o.append(line(X0, Y0, X1, Y0, w=1.2))
    o.append(logticks_x(MX, Y0, range(0, 12), [(0, "1 Hz"), (3, "1 kHz"), (6, "1 MHz"), (9, "1 GHz"), (11, "100 GHz")]))
    o.append(text(X1 + 6, Y0 + 4, "f", size=12, anchor="start", math=True))
    o.append(line(X0, MY(0), X1, MY(0), stroke=M, w=1.0, dash="2 3"))
    o.append(text(MX(4.0), MY(0) - 5, "vacuum: c", size=10, anchor="start", fill=M))
    o.append(line(X0, MY(np.log10(0.5)), X1, MY(np.log10(0.5)), stroke=B, w=2.0))
    o.append(text(MX(0.15), MY(np.log10(0.5)) + 14, "lossless dielectric, εr = 4: c/2 at every f", size=10.5, anchor="start", fill=B, weight=600))
    ff = np.logspace(L0, L1, 600)
    lf = np.log10(ff)
    mats = [("copper", 5.8e7, 1.0, C), ("seawater", 4.0, 81.0, A), ("moist soil", 1e-2, 10.0, "var(--accent2)"),
            ("fresh water", 1e-3, 80.0, M)]
    for name, s, er, col in mats:
        a, b, *_ = exact(ff, s, er)
        vp = 2 * np.pi * ff / b / c0
        o.append(poly(lf, np.log10(vp), MX, MY, stroke=col, w=2.3))
        fc = fc_of(s, er)
        if fc < 10 ** L1:
            bb = exact(fc, s, er)[1]
            o.append(circle(MX(np.log10(fc)), MY(np.log10(2 * np.pi * fc / bb / c0)), 3.8, fill=col, stroke="none"))
    o.append(tlabel(MX(4.8), MY(-7.1), "copper: " + _sub("v", "p") + " = √(2ω/μσ), 3.2 m/s at 60 Hz", size=10.5, anchor="start", fill=C, weight=600))
    o.append(tlabel(MX(0.15), MY(-5.9), "seawater", size=10.5, anchor="start", fill=A, weight=600))
    o.append(tlabel(MX(0.15), MY(-2.3), "fresh water", size=10.5, anchor="start", fill=M, weight=600))
    o.append(tlabel(MX(1.2), MY(-3.85), "moist soil", size=10.5, anchor="start", fill="var(--accent2)", weight=600))
    o.append(text(MX(3.2), MY(-8.4), "slope ½: good conductor, " + _sub("v", "p") + " ∝ √f — dispersive", size=11, anchor="start", fill=M, weight=600))
    o.append(text(MX(3.2), MY(-8.4) + 15, "flat: dielectric, " + _sub("v", "p") + " = c/n — no dispersion", size=11, anchor="start", fill=M, weight=600))
    # plasma
    fp = 9e6
    fpl = np.logspace(np.log10(fp * 1.012), L1, 300)
    vpp = 1 / np.sqrt(1 - (fp / fpl) ** 2)
    o.append(poly(np.log10(fpl), np.log10(vpp), MX, MY, stroke="var(--hi)", w=1.8, dash="7 3"))
    o.append(line(MX(np.log10(fp)), MY(1.0), MX(np.log10(fp)), MY(-0.6), stroke="var(--hi)", w=1.0, dash="2 3"))
    o.append(line(MX(np.log10(fp)), MY(1.7), MX(np.log10(fp)), MY(1.0), stroke="var(--hi)", w=1.0, dash="2 3"))
    o.append(tlabel(MX(np.log10(fp)) - 4, MY(1.55), "ionosphere: " + _sub("v", "p") + " > c above " + _sub("f", "p") + " = 9 MHz",
                    size=10, anchor="end", fill=C, weight=600))
    o.append(tlabel(MX(np.log10(fp)) - 4, MY(1.55) + 17, "nothing travels below; " + _sub("v", "p") + _sub("v", "g") + " = c²",
                    size=10, anchor="end", fill=C))
    # legend at right
    lx = X1 + 26
    o.append(text(lx, 80, _sub("f", "c") + " of each medium", size=11.5, anchor="start", weight=700))
    for j, (s, s2, col) in enumerate((("copper  1.0×10¹⁸ Hz", "always a conductor", C), ("seawater  0.89 GHz", "then → c/√81 = c/9", A),
                                      ("moist soil  18 MHz", "then → c/√10", "var(--accent2)"), ("fresh water  225 kHz", "then → c/√80", M))):
        o.append(circle(lx + 5, 98 + j * 36, 3.8, fill=col, stroke="none"))
        o.append(text(lx + 14, 102 + j * 36, _nb(s), size=11, anchor="start"))
        o.append(text(lx + 14, 118 + j * 36, s2, size=10.5, anchor="start", fill=M))
    o.append(text(lx, 258, "below " + _sub("f", "c") + ": conductor", size=11, anchor="start", fill=M))
    o.append(text(lx, 274, "above " + _sub("f", "c") + ": dielectric", size=11, anchor="start", fill=M))
    # ---------- panel 2: dB per wavelength vs p
    Yb0, Yb1 = 650, 460
    P0, P1 = -3.0, 4.0
    MXp = lin(P0, P1, X0, X1)
    MYp = lin(0, 60, Yb0, Yb1)
    o.append(text(20, Yb1 - 22, "Loss per wavelength depends only on p = σ/ωε:   2π · 8.686 · tan(½ tan⁻¹p)  dB per λ",
                  size=13, anchor="start", weight=700))
    o.append(_tint(MXp(P0), Yb1, MXp(-1) - MXp(P0), Yb0 - Yb1, "var(--accent2)", op=0.12))
    o.append(_tint(MXp(1), Yb1, MXp(P1) - MXp(1), Yb0 - Yb1, "var(--accent)", op=0.10))
    o.append(text(MXp(-2.0), MYp(32), "imperfect dielectric", size=10.5, fill=B, weight=600))
    o.append(text(MXp(-2.0), MYp(32) + 14, "p < 0.1", size=10, fill=B))
    o.append(text(MXp(2.6), MYp(32), "good conductor", size=10.5, fill=A, weight=600))
    o.append(text(MXp(2.6), MYp(32) + 14, "p > 10", size=10, fill=A))
    o.append(line(X0, Yb0, X1, Yb0, w=1.2))
    o.append(line(X0, Yb0, X0, Yb1, w=1.2))
    for v in (0, 20, 40, 60):
        o.append(line(X0 - 3, MYp(v), X0 + 3, MYp(v), w=1.0))
        o.append(text(X0 - 6, MYp(v) + 3.5, str(v), size=9.5, anchor="end", fill=M))
    o.append(text(X0 - 40, (Yb0 + Yb1) / 2, "dB per λ", size=11.5, rotate=-90))
    o.append(logticks_x(MXp, Yb0, range(-3, 5), [(-3, "0.001"), (-2, "0.01"), (-1, "0.1"), (0, "1"), (1, "10"), (2, "100"),
                                                  (3, "10³"), (4, "10⁴")]))
    o.append(text(X1 + 6, Yb0 + 4, "p", size=12, anchor="start", math=True))
    pp = np.logspace(P0, P1, 400)
    dbl = 2 * np.pi * DB * np.tan(np.arctan(pp) / 2)
    o.append(line(X0, MYp(2 * np.pi * DB), X1, MYp(2 * np.pi * DB), stroke=M, w=1.1, dash="6 4"))
    o.append(tlabel(MXp(-2.9), MYp(2 * np.pi * DB) - 4, "54.6 dB per λ = 2π × 8.686: the good-conductor limit", size=10, anchor="start", fill=M))
    o.append(poly(np.log10(pp), dbl, MXp, MYp, stroke=A, w=2.6))
    for pv, lab, anc, dx, dy in ((0.1, "p = 0.1: 2.7 dB", "end", -8, -24), (1, "p = 1: 22.6 dB", "start", 8, 12),
                                 (10, "p = 10: 49.4 dB", "start", 8, 16)):
        yv = 2 * np.pi * DB * math.tan(math.atan(pv) / 2)
        o.append(circle(MXp(math.log10(pv)), MYp(yv), 3.6, fill=A, stroke="none"))
        o.append(tlabel(MXp(math.log10(pv)) + dx, MYp(yv) + dy, lab, size=10, anchor=anc, fill=A, weight=600))
    # material examples
    ex = [(fc_of(4.0, 81.0) / 1e9, "seawater, 1 GHz"), (fc_of(1e-2, 10.0) / 1e5, "moist soil, 100 kHz"),
          (fc_of(1e-3, 80.0) / 1e8, "fresh water, 100 MHz")]
    for pv, lab in ex:
        yv = 2 * np.pi * DB * math.tan(math.atan(pv) / 2)
        o.append(circle(MXp(math.log10(pv)), MYp(yv), 4.2, fill="none", stroke=C, w=1.6))
    o.append(tlabel(MXp(math.log10(ex[0][0])) - 8, MYp(20.7) - 8, "seawater 1 GHz: 20.7", size=10, anchor="end", fill=C))
    o.append(tlabel(MXp(math.log10(ex[1][0])) + 8, MYp(54.3) + 18, "moist soil 100 kHz: 54.3", size=10, anchor="start", fill=C))
    xf = MXp(math.log10(ex[2][0]))
    o.append(line(xf, MYp(0.06) - 5, xf + 4, Yb0 - 44, stroke=C, w=1.0))
    o.append(tlabel(xf + 2, Yb0 - 48, "fresh water 100 MHz: 0.06", size=10, anchor="start", fill=C))
    o.append(text(lx - 4, Yb1 + 60, "Per skin depth δ = 1/α", size=11.5, anchor="start", weight=700))
    o.append(text(lx - 4, Yb1 + 78, "the loss is always", size=11, anchor="start"))
    o.append(text(lx - 4, Yb1 + 96, "8.686 dB (field 1/e,", size=11, anchor="start"))
    o.append(text(lx - 4, Yb1 + 114, "power 1/e²) in every", size=11, anchor="start"))
    o.append(text(lx - 4, Yb1 + 132, "medium.", size=11, anchor="start"))
    o.append(svg_close())
    figure("media-dispersion", "".join(o),
           "<strong>Dispersion and loss in one place.</strong> Top: phase velocity from the exact γ. Dielectrics are flat "
           "(no dispersion); good conductors climb as √f (copper crawls at 3.2 m/s at 60 Hz); water and soil switch from one "
           "to the other at their crossover frequency f<sub>c</sub> (dots). The ionospheric plasma (dashed) has v<sub>p</sub> &gt; c "
           "above its plasma frequency and no travelling wave below it. Bottom: loss per wavelength is a function of "
           "p = σ/ωε alone; it saturates at 54.6 dB per λ in a good conductor.")


# ------------------------------------------------------------------------------------------ 5. plane wave <-> transmission line
def fig_media_tl_analogy():
    W, H = 760, 430
    o = [svg_open(W, H)]
    o.append(text(20, 24, "Plane wave in a medium  ↔  TEM wave on a line", size=16, anchor="start", weight=700))
    o.append(text(20, 43, "Same two first-order equations, so the same γ, the same impedance, the same Γ.", size=12,
                  anchor="start", fill=M))
    # left: plane wave slab
    lx0, ly0 = 30, 70
    o.append(_tint(lx0, ly0, 300, 150, A, op=0.08, rx=6))
    o.append(rect(lx0, ly0, 300, 150, stroke=A, sw=1.2, rx=6, dash="5 4"))
    o.append(text(lx0 + 150, ly0 + 18, "medium: μ, ε, σ", size=12, fill=A, weight=700))
    ex, ey = lx0 + 90, ly0 + 110
    o.append(arrow(ex, ey, ex, ey - 64, stroke=C, w=2.6))
    o.append(text(ex - 8, ey - 40, "E", size=15, anchor="end", math=True, weight=700, fill=C))
    o.append(text(ex - 8, ey - 25, _sub("E", "x"), size=11, anchor="end", fill=C))
    o.append(_odot(ex + 46, ey - 20, r=8, color=B))
    o.append(text(ex + 60, ey - 26, "H", size=15, anchor="start", math=True, weight=700, fill=B))
    o.append(text(ex + 60, ey - 10, _sub("H", "y") + " (out of page)", size=11, anchor="start", fill=B))
    o.append(arrow(lx0 + 40, ly0 + 136, lx0 + 270, ly0 + 136, stroke="currentColor", w=1.6))
    o.append(text(lx0 + 264, ly0 + 130, "z, E×H", size=11, anchor="end", fill=M))
    # right: ladder section
    rx0, ry0 = 400, 70
    top, bot = ry0 + 40, ry0 + 120
    o.append(text(rx0 + 160, ry0 - 2, "line section Δz: 𝓡, 𝓛, 𝓖, 𝓒 per metre", size=12, fill=A, weight=700))
    o.append(line(rx0, top, rx0 + 30, top, w=1.6))
    o.append(_zigzag(rx0 + 30, top, rx0 + 90, top, n=6, amp=7, color=C, w=1.8))
    o.append(_coil(rx0 + 100, top, rx0 + 170, n=4, r=9, color=A))
    o.append(line(rx0 + 90, top, rx0 + 100, top, w=1.6))
    o.append(line(rx0 + 170, top, rx0 + 330, top, w=1.6))
    o.append(line(rx0, bot, rx0 + 330, bot, w=1.6))
    o.append(text(rx0 + 60, top - 12, "𝓡Δz", size=11.5, fill=C, weight=600))
    o.append(text(rx0 + 135, top - 16, "𝓛Δz", size=11.5, fill=A, weight=600))
    # shunt C
    cx = rx0 + 220
    o.append(line(cx, top, cx, top + 30, w=1.6))
    o.append(line(cx - 12, top + 30, cx + 12, top + 30, stroke=B, w=2.4))
    o.append(line(cx - 12, top + 38, cx + 12, top + 38, stroke=B, w=2.4))
    o.append(line(cx, top + 38, cx, bot, w=1.6))
    o.append(text(cx - 16, top + 40, "𝓒Δz", size=11.5, anchor="end", fill=B, weight=600))
    # shunt G
    gx = rx0 + 280
    o.append(line(gx, top, gx, top + 14, w=1.6))
    o.append(_zigzag(gx, top + 14, gx, bot - 14, n=6, amp=6, color="var(--hi)", w=1.8))
    o.append(line(gx, bot - 14, gx, bot, w=1.6))
    o.append(text(gx + 12, top + 44, "𝓖Δz", size=11.5, anchor="start", fill=C, weight=600))
    # V and I
    o.append(arrow(rx0 + 12, bot - 4, rx0 + 12, top + 6, stroke="currentColor", w=1.5))
    o.append(text(rx0 + 18, (top + bot) / 2 + 4, "V", size=14, anchor="start", math=True, weight=700))
    o.append(arrow(rx0 + 175, top - 2, rx0 + 205, top - 2, stroke="currentColor", w=1.5, small=True))
    o.append(text(rx0 + 190, top - 8, "I", size=14, math=True, weight=700))
    o.append(arrow(rx0 + 30, bot + 16, rx0 + 300, bot + 16, stroke="currentColor", w=1.6))
    o.append(text(rx0 + 294, bot + 32, "z", size=12, anchor="end", math=True))
    # dictionary rows
    rows = [
        (_sub("E", "x"), "V", "volts per metre ↔ volts", C),
        (_sub("H", "y"), "I", "amperes per metre ↔ amperes", B),
        ("μ", "𝓛", "stores magnetic energy", A),
        ("ε", "𝓒", "stores electric energy", B),
        ("σ", "𝓖", "shunt loss: current through the medium", C),
        ("—", "𝓡", "series loss in the conductors: no plane-wave twin", M),
        ("η", _sub("Z", "0"), "V/I of one travelling wave", A),
    ]
    y = 262
    o.append(text(170, y - 14, "plane wave", size=12, weight=700))
    o.append(text(240, y - 14, "line", size=12, weight=700))
    for i, (a, b, s, col) in enumerate(rows):
        yy = y + 8 + i * 22
        if i % 2 == 0:
            o.append(_tint(110, yy - 15, 560, 21, "currentColor", op=0.04))
        o.append(text(170, yy, a, size=14, math=True, weight=700, fill=col))
        o.append(text(205, yy, "↔", size=13, fill=M))
        o.append(text(240, yy, b, size=14, weight=700, fill=col))
        o.append(text(290, yy, s, size=11.5, anchor="start"))
    o.append(svg_close())
    figure("media-tl-analogy", "".join(o),
           "<strong>The dictionary between Units 3 and 4.</strong> For an x-polarized wave travelling along z, Faraday's "
           "and Ampère's laws read ∂E<sub>x</sub>/∂z = −μ∂H<sub>y</sub>/∂t and ∂H<sub>y</sub>/∂z = −σE<sub>x</sub> − ε∂E<sub>x</sub>/∂t; "
           "the telegrapher's equations of a line are the same with V, I, 𝓛, 𝓖 and 𝓒 in their places. So "
           "γ = √((𝓡 + jω𝓛)(𝓖 + jω𝓒)) and Z<sub>0</sub> = √((𝓡 + jω𝓛)/(𝓖 + jω𝓒)) are the plane-wave γ and η "
           "with one extra term, the series resistance of the wires.")


if __name__ == "__main__":
    fig_media_wave_equations()
    fig_media_angles()
    fig_media_snapshots()
    fig_media_dispersion()
    fig_media_tl_analogy()
