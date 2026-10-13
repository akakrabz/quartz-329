#!/usr/bin/env python3
"""Lecture 22 figures (lossy-*) for the ECE 329 notes: phasor Maxwell equations and damped waves.

Same helpers and conventions as figs.py (plotting helpers from figs_l18.py / figs_l19.py).
Running this module writes /home/claude/work/figs/<name>.html.
Every curve is computed from the formulas checked in digest8/verify_L22.py:
  damped wave   E_x = e^{-alpha z} cos(wt - beta z)                      (section F)
  phasor spiral E~(z)/E0 = e^{-gamma z}, |eta| H~/E0 = e^{-j tau} E~/E0    (section N)
  phase dial    gamma/(w sqrt(mu eps)) = j sqrt(1 - j s), eta/sqrt(mu/eps) = 1/sqrt(1 - j s), s = sig/(w eps)  (section G)
  regimes       alpha, beta in units of alpha_inf = (sig/2) sqrt(mu/eps) against x = w eps / sig  (section H)
No 3-D vectors are drawn. Rotation senses (screen: Re right, Im up): e^{-j beta z} turns clockwise as z grows
(angle decreasing, checked in verify section N); H~ = E~/eta is E~ turned clockwise by tau (lags).
The site's accent/accent2 pair is close in dark mode and hi/accent2 is weak for deutans, so every pair of
curves also differs by dash pattern and carries a direct label (identity is never colour alone).
"""
from figs import *
from figs import _odot, _otimes, _sub, _tint
from figs_l18 import lin, poly, haxis


def _sup(base, s, size=9):
    """base text with a superscript s (SVG tspan)"""
    return f'{base}<tspan baseline-shift="super" style="font-size:{size}px">{s}</tspan>'


def swatch(x, y, stroke, dash=None, w=2.2, L=22):
    """short line sample used in front of a direct label"""
    return line(x, y, x + L, y, stroke=stroke, w=w, dash=dash)


# ------------------------------------------------------------------------------------------------ 1. damped wave
def fig_lossy_damped_wave():
    W, H = 640, 352
    o = [svg_open(W, H)]
    a, b = 0.6, 2 * np.pi            # per wavelength: delta = 1/a = 1.667 lambda
    MZ = lin(0, 3.0, 62, 598)
    Y0, A = 156, 100
    MY = lambda v: Y0 - A * v
    o.append(text(20, 22, "Snapshots of " + _sub("E", "x") + " = |" + _sub("E", "0") + "| " + _sup("e", "−αz") +
                  " cos(ωt − βz): the wave decays along its travel", size=13, anchor="start", weight=600))
    # recessive axes: z axis through the middle, field axis on the left
    o.append(line(MZ(0), Y0, MZ(3.0) + 14, Y0, w=1.1, arrow=True))
    o.append(text(MZ(3.0) + 18, Y0 + 4, "z", size=13, anchor="start", math=True))
    o.append(line(MZ(0), MY(-1.12), MZ(0), MY(1.18), w=1.1, arrow=True))
    o.append(text(MZ(0) + 6, MY(1.18) + 4, _sub("E", "x") + " / |" + _sub("E", "0") + "|", size=11.5, anchor="start"))
    for v, lab in ((1, "1"), (-1, "−1"), (np.exp(-1), "1/e")):
        o.append(line(MZ(0) - 4, MY(v), MZ(0) + 4, MY(v), w=1.0))
        o.append(text(MZ(0) - 7, MY(v) + 4, lab, size=10.5, anchor="end", fill="var(--muted)"))
    zz = np.linspace(0, 3.0, 1200)
    env = np.exp(-a * zz)
    # envelope +-e^{-alpha z}: dotted, muted
    o.append(poly(zz, env, MZ, MY, stroke="var(--muted)", w=1.4, dash="2 4"))
    o.append(poly(zz, -env, MZ, MY, stroke="var(--muted)", w=1.4, dash="2 4"))
    o.append(text(MZ(2.55), MY(-np.exp(-a * 2.55)) + 18, "envelope ±" + _sup("e", "−αz"), size=11, fill="var(--muted)"))
    # 1/e level and delta = 1/alpha
    d = 1 / a
    o.append(line(MZ(0), MY(np.exp(-1)), MZ(d), MY(np.exp(-1)), stroke="var(--muted)", w=0.9))
    o.append(line(MZ(d), MY(np.exp(-1)), MZ(d), 302, stroke="var(--muted)", w=0.9))
    o.append(circle(MZ(d), MY(np.exp(-1)), 3.6, fill="currentColor", stroke="none"))
    # the two snapshots: t = 0 (solid) and t = T/8 (dashed), moving toward +z
    o.append(poly(zz, env * np.cos(-b * zz), MZ, MY, stroke="var(--accent)", w=2.4))
    o.append(poly(zz, env * np.cos(np.pi / 4 - b * zz), MZ, MY, stroke="var(--accent2)", w=2.0, dash="7 4"))
    # direct labels with swatches
    o.append(swatch(430, 40, "var(--accent)")); o.append(text(458, 44, "t = 0", size=11.5, anchor="start"))
    o.append(swatch(512, 40, "var(--accent2)", dash="7 4", w=2.0)); o.append(text(540, 44, "t = T/8", size=11.5, anchor="start"))
    # nodes move lambda/8 in T/8: zero crossings at z = 2.75 (t = 0) and 2.875 (t = T/8), where the curves are small
    o.append(circle(MZ(2.75), Y0, 3.4, fill="var(--accent)", stroke="none"))
    o.append(circle(MZ(2.875), Y0, 3.4, fill="var(--accent2)", stroke="none"))
    o.append(line(MZ(2.75), Y0 - 4, MZ(2.75), Y0 - 40, stroke="var(--muted)", w=0.8))
    o.append(line(MZ(2.875), Y0 - 4, MZ(2.875), Y0 - 40, stroke="var(--muted)", w=0.8))
    o.append(arrow(MZ(2.75) + 1, Y0 - 36, MZ(2.875) - 1, Y0 - 36, stroke="currentColor", w=1.4, small=True))
    o.append(text(MZ(2.81), Y0 - 46, "a node moves λ/8", size=10.5))
    # dimension lines below the plot: lambda between two crossings, delta from 0
    Yd1, Yd2 = 262, 296
    o.append(line(MZ(0.25), Y0 + 4, MZ(0.25), Yd1 + 6, stroke="var(--muted)", w=0.8))
    o.append(line(MZ(1.25), Y0 + 4, MZ(1.25), Yd1 + 6, stroke="var(--muted)", w=0.8))
    o.append(arrow(MZ(0.75), Yd1, MZ(0.25) + 2, Yd1, stroke="currentColor", w=1.3, small=True))
    o.append(arrow(MZ(0.75), Yd1, MZ(1.25) - 2, Yd1, stroke="currentColor", w=1.3, small=True))
    o.append(text(MZ(0.75), Yd1 - 6, "λ = 2π/β  (two node spacings)", size=11, weight=600))
    o.append(line(MZ(0), Yd2 - 6, MZ(0), Yd2 + 6, stroke="var(--muted)", w=0.8))
    o.append(arrow(MZ(d / 2), Yd2, MZ(0) + 2, Yd2, stroke="currentColor", w=1.3, small=True))
    o.append(arrow(MZ(d / 2), Yd2, MZ(d) - 2, Yd2, stroke="currentColor", w=1.3, small=True))
    o.append(text(MZ(d) + 8, Yd2 + 4, "δ = 1/α: the envelope is down to 1/e ≈ 37 %", size=11, anchor="start", weight=600))
    o.append(text(W / 2, H - 12, "drawn for α/β = 0.6/2π ≈ 0.095 (τ ≈ 5.5°), so δ ≈ 1.67 λ; z ticks every λ", size=10.5, fill="var(--muted)"))
    for k in (1, 2, 3):
        o.append(line(MZ(k), Y0 - 3, MZ(k), Y0 + 3, w=1.0))
        o.append(text(MZ(k) - 4, Y0 + 15, f"{k}λ" if k > 1 else "λ", size=10.5, anchor="end", fill="var(--muted)"))
    o.append(svg_close())
    figure("lossy-damped-wave", "".join(o),
           "<strong>A damped plane wave, frozen at two instants.</strong> Both curves are "
           "e<sup>−αz</sup>cos(ωt − βz), computed with α/β = 0.6/2π. The solid curve is t = 0. The dashed one is an eighth "
           "of a period later, and its zero crossings (the <em>nodes</em>) have moved λ/8 toward +z. Nodes are where the "
           "cosine is zero, so the envelope cannot move them, and they travel at v<sub>p</sub> = ω/β. Successive nodes are "
           "λ/2 apart, so λ = 2π/β spans two of them. The peaks follow the dotted envelope ±e<sup>−αz</sup>, which falls to "
           "1/e at z = δ = 1/α. That is the penetration depth. Here α is small, so the wave survives about 1.7 wavelengths "
           "before it drops to 37 %. In a good conductor α = β and the same drop happens within λ/2π (Lecture 23). "
           "The notes' margin figure shows the same two snapshots without δ and λ marked.")


# ------------------------------------------------------------------------------------------------ 2. phasor spiral + records
def fig_lossy_phasor_spiral():
    W, H = 640, 360
    o = [svg_open(W, H)]
    tau = np.radians(15.0)                    # sig/(w eps) = tan(30 deg) = 0.577
    b = 2 * np.pi; a = b * np.tan(tau)        # alpha/beta = tan(tau)
    # ---- left: complex plane, radius 1 = 118 px
    cx, cy, R = 160, 182, 118
    MRe = lambda v: cx + R * v
    MIm = lambda v: cy - R * v
    o.append(text(20, 22, "1  The phasor " + "Ẽ(z) = " + _sub("E", "0") + _sup("e", "−γz") + " as z grows", size=12.5, anchor="start", weight=600))
    o.append(line(MRe(-1.15), cy, MRe(1.2), cy, w=1.0, arrow=True)); o.append(text(MRe(1.2) + 3, cy + 4, "Re", size=11, anchor="start"))
    o.append(line(cx, MIm(-1.15), cx, MIm(1.18), w=1.0, arrow=True)); o.append(text(cx + 5, MIm(1.18) + 2, "Im", size=11, anchor="start"))
    o.append(circle(cx, cy, R, stroke="var(--muted)", w=1.1, dash="2 4"))
    o.append(text(20, MIm(1.02), "lossless: a circle", size=10.5, anchor="start", fill="var(--muted)"))
    zz = np.linspace(0, 1.25, 900)
    ph = np.exp(-(a + 1j * b) * zz)
    o.append(poly(ph.real, ph.imag, MRe, MIm, stroke="var(--accent)", w=2.2))
    # marks every quarter wavelength, labels placed outside the spiral (angle -beta z, radius e^{-alpha z})
    for k, lab, dxy in ((0, "z = 0", (8, -8)), (0.25, "λ/4", (6, 16)), (0.5, "λ/2", (-12, 4)), (0.75, "3λ/4", (-4, -12)), (1.0, "λ", (8, -6))):
        p = np.exp(-(a + 1j * b) * k)
        o.append(circle(MRe(p.real), MIm(p.imag), 3.4, fill="var(--accent)", stroke="none"))
        anc = "start" if dxy[0] >= 0 else "end"
        o.append(text(MRe(p.real) + dxy[0], MIm(p.imag) + dxy[1], lab, size=10.5, anchor=anc))
    # direction of travel along the spiral: small arrowhead near z = 0.12 lambda (clockwise, shrinking)
    p1, p2 = np.exp(-(a + 1j * b) * 0.115), np.exp(-(a + 1j * b) * 0.13)
    o.append(arrow(MRe(p1.real), MIm(p1.imag), MRe(p2.real), MIm(p2.imag), stroke="var(--accent)", w=2.2))
    # E~ and |eta| H~ at z = 0: H~ is E~ turned clockwise by tau
    o.append(arrow(cx, cy, MRe(1.0) - 2, cy, stroke="var(--accent)", w=2.4))
    hp = np.exp(-1j * tau) * 0.97
    o.append(line(cx, cy, MRe(hp.real), MIm(hp.imag), stroke="var(--accent2)", w=2.2, dash="6 3"))
    o.append(arrow(MRe(hp.real * 0.92), MIm(hp.imag * 0.92), MRe(hp.real), MIm(hp.imag), stroke="var(--accent2)", w=2.2))
    # angle arc tau
    th = np.linspace(0, -tau, 30); rr = 0.42
    o.append(poly(rr * np.cos(th), rr * np.sin(th), MRe, MIm, stroke="currentColor", w=1.2))
    o.append(text(MRe(0.50), MIm(-0.06) + 4, "τ", size=13, anchor="start", math=True))
    o.append(text(MRe(0.60), MIm(0.10), "Ẽ(0)", size=11, anchor="middle", weight=600))
    o.append(text(MRe(0.52), MIm(-0.35), "|η| H̃(0)", size=11, anchor="middle", weight=600))
    o.append(text(cx, H - 30, "turns clockwise (−βz) and shrinks (" + _sup("e", "−αz") + ");", size=10.5, fill="var(--muted)"))
    o.append(text(cx, H - 14, "each turn is one λ and multiplies the radius by " + _sup("e", "−2π tan τ"), size=10.5, fill="var(--muted)"))
    # ---- right: records at z = 0 against time
    MT = lin(0, 4 * np.pi, 352, 612)
    Yr, Ar = 182, 70
    MY = lambda v: Yr - Ar * v
    o.append(text(338, 22, "2  At one place: E and H against time", size=12.5, anchor="start", weight=600))
    o.append(line(MT(0), Yr, MT(4 * np.pi) + 10, Yr, w=1.0, arrow=True)); o.append(text(MT(4 * np.pi) + 12, Yr + 4, "ωt", size=11.5, anchor="start", math=True))
    o.append(line(MT(0), MY(-1.25), MT(0), MY(1.3), w=1.0))
    for v, lab in ((1, "1"), (-1, "−1")):
        o.append(line(MT(0) - 3, MY(v), MT(0) + 3, MY(v), w=1.0))
        o.append(text(MT(0) - 6, MY(v) + 4, lab, size=10, anchor="end", fill="var(--muted)"))
    for k, lab in ((1, "π"), (2, "2π"), (3, "3π"), (4, "4π")):
        o.append(line(MT(k * np.pi), Yr - 3, MT(k * np.pi), Yr + 3, w=1.0))
        o.append(text(MT(k * np.pi), Yr + 16, lab, size=10, fill="var(--muted)"))
    tt = np.linspace(0, 4 * np.pi, 900)
    o.append(poly(tt, np.cos(tt), MT, MY, stroke="var(--accent)", w=2.3))
    o.append(poly(tt, np.cos(tt - tau), MT, MY, stroke="var(--accent2)", w=2.0, dash="6 3"))
    # lag between peaks at wt = 2 pi and 2 pi + tau
    for x_ in (2 * np.pi, 2 * np.pi + tau):
        o.append(line(MT(x_), MY(1.0) - 2, MT(x_), MY(1.25), stroke="var(--muted)", w=0.8))
    o.append(arrow(MT(2 * np.pi) - 16, MY(1.2), MT(2 * np.pi) - 1, MY(1.2), stroke="currentColor", w=1.2, small=True))
    o.append(arrow(MT(2 * np.pi + tau) + 16, MY(1.2), MT(2 * np.pi + tau) + 1, MY(1.2), stroke="currentColor", w=1.2, small=True))
    o.append(text(MT(2 * np.pi + tau) + 20, MY(1.2) + 4, "τ/ω later", size=10.5, anchor="start"))
    o.append(swatch(352, 288, "var(--accent)")); o.append(text(380, 292, _sub("E", "x") + "(0, t) / |" + _sub("E", "0") + "| = cos ωt", size=11, anchor="start"))
    o.append(swatch(352, 308, "var(--accent2)", dash="6 3", w=2.0)); o.append(text(380, 312, "|η| " + _sub("H", "y") + "(0, t) / |" + _sub("E", "0") + "| = cos(ωt − τ)", size=11, anchor="start"))
    o.append(text(482, H - 14, "steady amplitude in time: the damping is in z, not in t", size=10.5, fill="var(--muted)"))
    o.append(svg_close())
    figure("lossy-phasor-spiral", "".join(o),
           "<strong>What γ and the angle of η do to the phasors.</strong> Panel 1 plots the tip of Ẽ(z)/E<sub>0</sub> = "
           "e<sup>−αz</sup>e<sup>−jβz</sup> in the complex plane, computed for τ = 15° (σ/ωε = tan 30°, α/β = tan 15°). In a "
           "lossless medium the tip would go round the dotted unit circle, once per wavelength. With loss it spirals inward: "
           "e<sup>−jβz</sup> turns it clockwise and e<sup>−αz</sup> shrinks it, by e<sup>−2π tan τ</sup> ≈ 0.19 per turn here. "
           "H̃ = Ẽ/η is the same spiral divided by |η| and turned a further τ clockwise. Panel 2 projects the rotating "
           "phasors onto the real axis at z = 0. Both fields are steady sinusoids in time, and H reaches each peak τ/ω after E. "
           "Elsewhere the two curves are smaller by e<sup>−αz</sup> and shifted by βz, and the lag is still τ.")


# ------------------------------------------------------------------------------------------------ 3. phase dial
def fig_lossy_phase_dial():
    W, H = 640, 400
    o = [svg_open(W, H)]
    ox, oy, S = 62, 352, 128          # origin and px per unit (normalized values)
    MX = lambda v: ox + S * v
    MY = lambda v: oy - S * v
    o.append(text(20, 22, "γ and η as s = σ/ωε grows, each divided by its lossless value", size=12.5, anchor="start", weight=600))
    # recessive axes and the unit circle
    o.append(line(MX(0), oy, MX(2.42), oy, w=1.0, arrow=True)); o.append(text(MX(2.42) + 2, oy + 16, "real part", size=10.5, anchor="end", fill="var(--muted)"))
    o.append(line(ox, MY(0), ox, MY(2.42), w=1.0, arrow=True)); o.append(text(ox + 6, MY(2.42) + 4, "imaginary part", size=10.5, anchor="start", fill="var(--muted)"))
    th = np.linspace(0, np.pi / 2, 100)
    o.append(poly(np.cos(th), np.sin(th), MX, MY, stroke="var(--muted)", w=1.0, dash="2 4"))
    for v in (1, 2):
        o.append(line(MX(v), oy - 3, MX(v), oy + 3, w=1.0)); o.append(text(MX(v), oy + 16, str(v), size=10, fill="var(--muted)"))
        o.append(line(ox - 3, MY(v), ox + 3, MY(v), w=1.0)); o.append(text(ox - 7, MY(v) + 4, str(v), size=10, anchor="end", fill="var(--muted)"))
    o.append(text(ox - 7, oy + 14, "0", size=10, anchor="end", fill="var(--muted)"))
    # the 45-degree line: the good-conductor limit of both angles
    o.append(line(MX(0), MY(0), MX(2.3), MY(2.3), stroke="var(--muted)", w=1.0, dash="6 4"))
    o.append(text(MX(2.0) + 6, MY(2.0) + 16, "45°", size=10.5, anchor="start", fill="var(--muted)"))
    s = np.concatenate([np.linspace(0, 1, 200), np.linspace(1, 10, 400)])
    gn = 1j * np.sqrt(1 - 1j * s)
    en = 1 / np.sqrt(1 - 1j * s)
    o.append(poly(gn.real, gn.imag, MX, MY, stroke="var(--accent)", w=2.3))
    o.append(poly(en.real, en.imag, MX, MY, stroke="var(--accent2)", w=2.1, dash="7 4"))
    marks = ((0, "0"), (1, "1"), (np.sqrt(3), "√3"), (4, "4"), (10, "10"))
    for sv, lab in marks:
        g = 1j * np.sqrt(1 - 1j * sv); e = 1 / np.sqrt(1 - 1j * sv)
        o.append(circle(MX(g.real), MY(g.imag), 4.2, fill="var(--accent)", stroke="var(--paper)", w=1.5))
        o.append(rect(MX(e.real) - 3.8, MY(e.imag) - 3.8, 7.6, 7.6, fill="var(--accent2)", stroke="var(--paper)", sw=1.5))
        if sv == 0:
            o.append(text(MX(g.real) + 9, MY(g.imag) - 8, "s = 0", size=10.5, anchor="start"))
            o.append(text(MX(e.real) + 7, MY(e.imag) - 9, "s = 0", size=10.5, anchor="start"))
            continue
        if sv == 1:
            o.append(text(MX(g.real) - 3, MY(g.imag) + 17, lab, size=10.5, anchor="end"))
        else:
            o.append(text(MX(g.real) - 9, MY(g.imag) + 4, lab, size=10.5, anchor="end"))
        if sv in (1, 4):
            o.append(text(MX(e.real) + 2, MY(e.imag) + 17, lab, size=10.5, anchor="middle"))
    # s = sqrt(3): the two rays, 60 and 30 degrees
    g3 = 1j * np.sqrt(1 - 1j * np.sqrt(3)); e3 = 1 / np.sqrt(1 - 1j * np.sqrt(3))
    o.append(line(MX(0), MY(0), MX(g3.real), MY(g3.imag), stroke="var(--accent)", w=1.0, opacity=0.8))
    o.append(line(MX(0), MY(0), MX(e3.real), MY(e3.imag), stroke="var(--accent2)", w=1.0, opacity=0.8))
    ar = np.linspace(0, np.pi / 6, 20)
    o.append(poly(0.30 * np.cos(ar), 0.30 * np.sin(ar), MX, MY, stroke="currentColor", w=1.1))
    o.append(text(MX(0.34), MY(0.07), "τ", size=12, anchor="start", math=True))
    # direct labels (text colour) with swatches
    o.append(swatch(MX(0.12), MY(2.25), "var(--accent)")); o.append(text(MX(0.12) + 28, MY(2.25) + 4, "γ / ω√(με)  (circles)", size=11.5, anchor="start", weight=600))
    o.append(text(MX(0.12) + 28, MY(2.25) + 20, "x = α, y = β, both / ω√(με)", size=10.5, anchor="start", fill="var(--muted)"))
    o.append(swatch(MX(1.12), MY(0.46), "var(--accent2)", dash="7 4", w=2.1)); o.append(text(MX(1.12) + 28, MY(0.46) + 4, "η / √(μ/ε)  (squares)", size=11.5, anchor="start", weight=600))
    o.append(text(MX(1.12) + 28, MY(0.46) + 20, "its angle is τ", size=10.5, anchor="start", fill="var(--muted)"))
    # right column: relations and the table view
    X0 = 418
    o.append(text(X0, 52, "γ / ω√(με) = j √(1 − js)", size=11.5, anchor="start"))
    o.append(text(X0, 70, "η / √(μ/ε) = 1 / √(1 − js)", size=11.5, anchor="start"))
    o.append(text(X0, 92, "∠γ + ∠η = 90°,  |γ| |η| = ωμ", size=11.5, anchor="start"))
    o.append(text(X0, 110, "τ = ∠η = ½ tan⁻¹ s,  α/β = tan τ", size=11.5, anchor="start"))
    o.append(text(X0, 130, "η is γ inverted in the unit circle", size=11, anchor="start", fill="var(--muted)"))
    o.append(text(X0, 146, "and reflected across the 45° line", size=11, anchor="start", fill="var(--muted)"))
    rows = [("s", "τ", "∠γ", "|γ|", "|η|"), ("0", "0°", "90°", "1", "1"), ("¼", "7.0°", "83.0°", "1.02", "0.98"),
            ("1", "22.5°", "67.5°", "1.19", "0.84"), ("√3", "30°", "60°", "1.41", "0.71"), ("4", "38.0°", "52.0°", "2.03", "0.49"),
            ("10", "42.1°", "47.9°", "3.17", "0.32"), ("→ ∞", "→ 45°", "→ 45°", "→ ∞", "→ 0")]
    cols = [X0, X0 + 38, X0 + 86, X0 + 138, X0 + 178]
    for i, r in enumerate(rows):
        yy = 176 + 20 * i
        for j, (cxx, cell) in enumerate(zip(cols, r)):
            o.append(text(cxx, yy, cell, size=11, anchor="start", weight=(600 if i == 0 else None),
                          fill=("currentColor" if (i == 0 or j == 0) else "var(--muted)")))
        if i == 0:
            o.append(line(X0, yy + 6, X0 + 212, yy + 6, stroke="var(--muted)", w=0.8))
    o.append(text(X0, 176 + 20 * 8 + 4, "|γ|, |η| in units of ω√(με), √(μ/ε)", size=10.5, anchor="start", fill="var(--muted)"))
    o.append(svg_close())
    figure("lossy-phase-dial", "".join(o),
           "<strong>One number, s = σ/ωε, sets the angles of γ and η.</strong> Both are plotted in the complex plane "
           "for s from 0 to 10, normalized by their lossless values ω√(με) and √(μ/ε). The circles trace γ: at s = 0 it "
           "sits on the imaginary axis (pure β, no α), and as s grows it leans toward the 45° line, where α = β. The squares "
           "trace η: it starts on the real axis at √(μ/ε), shrinks, and leans up toward 45°. Because γη = jωμ, the two "
           "angles always add to 90°, so the angle of γ is 90° − τ and α/β = tan τ. The thin rays show s = √3, where τ = 30° "
           "and γ points at 60°. The table gives the same curves as numbers. The 45° line itself is the good-conductor limit, "
           "which neither curve reaches at finite s.")


# ------------------------------------------------------------------------------------------------ 4. regimes vs frequency
def fig_lossy_regimes():
    W, H = 640, 560
    o = [svg_open(W, H)]
    MX = lin(-2, 2, 96, 600)                       # log10(x), x = w eps / sig
    xs = np.logspace(-2, 2, 800); lx = np.log10(xs)
    s = 1 / xs
    an = np.sqrt(2) * xs * np.sqrt(np.sqrt(1 + s * s) - 1)     # alpha / alpha_inf
    bn = np.sqrt(2) * xs * np.sqrt(np.sqrt(1 + s * s) + 1)     # beta / alpha_inf
    o.append(text(20, 22, "One medium (fixed σ, ε, μ) at all frequencies; x = ωε/σ = ω × (relaxation time ε/σ)", size=12.5, anchor="start", weight=600))
    # regime bands across all three panels
    top, bot = 44, 500
    o.append(_tint(MX(-2), top, MX(-1) - MX(-2), bot - top, "var(--muted)", op=0.13))
    o.append(_tint(MX(1), top, MX(2) - MX(1), bot - top, "var(--muted)", op=0.13))
    o.append(line(MX(0), top, MX(0), bot, stroke="var(--muted)", w=1.0))
    o.append(text(MX(-1.5), top + 14, "good conductor", size=11, weight=600))
    o.append(text(MX(-1.5), top + 28, "σ ≫ ωε", size=11))
    o.append(text(MX(1.5), top + 14, "imperfect dielectric", size=11, weight=600))
    o.append(text(MX(1.5), top + 28, "σ ≪ ωε", size=11))
    o.append(text(MX(0) + 5, top + 14, "σ = ωε", size=11, anchor="start", weight=600))
    o.append(text(MX(0) + 5, top + 28, "neither shortcut", size=10.5, anchor="start", fill="var(--muted)"))
    # ---- panel 1: delta = 1/alpha and lambda/2pi = 1/beta, in units of delta_inf (log-log)
    MY1 = lin(-2.5, 1.0, 262, 64)
    for k in (-2, -1, 0, 1):
        o.append(line(MX(-2), MY1(k), MX(2), MY1(k), stroke="var(--muted)", w=0.5, opacity=0.6))
        o.append(text(MX(-2) - 6, MY1(k) + 4, {-2: "0.01", -1: "0.1", 0: "1", 1: "10"}[k], size=10, anchor="end", fill="var(--muted)"))
    o.append(line(MX(-2), MY1(-2.5), MX(-2), MY1(1.0), w=1.0))
    o.append(text(26, MY1(-0.75), "length / " + _sub("δ", "∞"), size=11, rotate=-90))
    # asymptotes (dotted): low x both 1/sqrt(2x); high x delta -> 1, lambda/2pi -> 1/(2x)
    xl = np.logspace(-2, -0.3, 50)
    o.append(poly(np.log10(xl), np.log10(1 / np.sqrt(2 * xl)), MX, MY1, stroke="var(--muted)", w=1.3, dash="2 3"))
    xh = np.logspace(0.3, 2, 50)
    o.append(poly(np.log10(xh), np.log10(1 / (2 * xh)), MX, MY1, stroke="var(--muted)", w=1.3, dash="2 3"))
    o.append(poly([0.3, 2], [0, 0], MX, MY1, stroke="var(--muted)", w=1.3, dash="2 3"))
    o.append(poly(lx, np.log10(1 / an), MX, MY1, stroke="var(--accent)", w=2.4))
    o.append(poly(lx, np.log10(1 / bn), MX, MY1, stroke="var(--accent2)", w=2.1, dash="7 4"))
    o.append(swatch(MX(0.62), MY1(0.0) - 14, "var(--accent)")); o.append(text(MX(0.62) + 28, MY1(0.0) - 10, "δ = 1/α  →  " + _sub("δ", "∞") + " = (2/σ)√(ε/μ)", size=11, anchor="start", weight=600))
    o.append(swatch(MX(-0.75), MY1(-2.0), "var(--accent2)", dash="7 4", w=2.1)); o.append(text(MX(-0.75) + 28, MY1(-2.0) + 4, "λ/2π = 1/β, falls as 1/ω on the right", size=11, anchor="start", weight=600))
    o.append(text(MX(-1.96), MY1(-0.55), "δ ≈ λ/2π = 1/√(πfμσ)", size=11, anchor="start", weight=600))
    o.append(text(MX(-1.96), MY1(-0.55) + 16, "both ∝ 1/√ω here (α ≈ β)", size=10.5, anchor="start", fill="var(--muted)"))
    # ---- panel 2: |eta| / sqrt(mu/eps)
    MY2 = lin(0, 1, 372, 300)
    o.append(text(MX(-2), 292, "|η| / √(μ/ε)", size=11.5, anchor="start", weight=600))
    for v in (0, 0.5, 1):
        o.append(line(MX(-2), MY2(v), MX(2), MY2(v), stroke="var(--muted)", w=0.5, opacity=0.6))
        o.append(text(MX(-2) - 6, MY2(v) + 4, {0: "0", 0.5: "0.5", 1: "1"}[v], size=10, anchor="end", fill="var(--muted)"))
    o.append(line(MX(-2), MY2(0), MX(-2), MY2(1.02), w=1.0))
    o.append(poly(lx, (1 + s * s) ** -0.25, MX, MY2, stroke="var(--accent)", w=2.3))
    o.append(text(MX(-1.95), MY2(0.38), "|η| ≈ √(ωμ/σ), small", size=10.5, anchor="start", fill="var(--muted)"))
    o.append(text(MX(1.92), MY2(0.75), "|η| → √(μ/ε)", size=10.5, anchor="end", fill="var(--muted)"))
    # ---- panel 3: tau in degrees
    MY3 = lin(0, 45, 482, 410)
    o.append(text(MX(-2), 402, "τ = ∠η", size=11.5, anchor="start", weight=600))
    for v in (0, 22.5, 45):
        o.append(line(MX(-2), MY3(v), MX(2), MY3(v), stroke="var(--muted)", w=0.5, opacity=0.6))
        o.append(text(MX(-2) - 6, MY3(v) + 4, {0: "0°", 22.5: "22.5°", 45: "45°"}[v], size=10, anchor="end", fill="var(--muted)"))
    o.append(line(MX(-2), MY3(0), MX(-2), MY3(46), w=1.0))
    o.append(poly(lx, np.degrees(0.5 * np.arctan(s)), MX, MY3, stroke="var(--accent)", w=2.3))
    o.append(text(MX(1.92), MY3(14), "≈ σ/2ωε (rad)", size=10.5, anchor="end", fill="var(--muted)"))
    # x axis
    o.append(line(MX(-2), bot, MX(2) + 10, bot, w=1.1, arrow=True))
    for k, lab in ((-2, "0.01"), (-1, "0.1"), (0, "1"), (1, "10"), (2, "100")):
        o.append(line(MX(k), bot - 3, MX(k), bot + 3, w=1.0))
        o.append(text(MX(k), bot + 16, lab, size=10.5, fill="var(--muted)"))
    o.append(text(MX(0), bot + 34, "x = ωε/σ  (log scale; x = 1 at f = σ/2πε)", size=11.5, weight=600))
    o.append(svg_close())
    figure("lossy-regimes", "".join(o),
           "<strong>How one material changes character with frequency.</strong> All curves come from the exact formulas, "
           "plotted against x = ωε/σ, the inverse of the ratio s = σ/ωε. Top: the penetration depth δ = 1/α (solid) and "
           "λ/2π = 1/β (dashed), in units of the high-frequency depth δ<sub>∞</sub> = (2/σ)√(ε/μ). On the left the medium is "
           "a good conductor. There the two lengths nearly coincide and grow as 1/√ω toward low frequency (dotted asymptote), which "
           "is the notes' reason for using low frequencies in sea water. On the right it is an imperfect dielectric: δ "
           "levels off at δ<sub>∞</sub>, while λ keeps shrinking as 1/ω, so the wave travels many wavelengths before it "
           "fades. Middle and bottom: |η| climbs from √(ωμ/σ) to √(μ/ε), and its angle τ falls from 45° to 0. Near x = 1 "
           "neither shortcut holds; there τ = 22.5° and δ = 1.10 δ<sub>∞</sub>. The page's table lists the same values.")


if __name__ == "__main__":
    for fn in (fig_lossy_damped_wave, fig_lossy_phasor_spiral, fig_lossy_phase_dial, fig_lossy_regimes):
        fn()
