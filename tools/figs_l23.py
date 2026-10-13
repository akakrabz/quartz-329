#!/usr/bin/env python3
"""Lecture 23 figures (cond-*) for the ECE 329 notes: imperfect dielectrics and good conductors.

Same helpers and conventions as figs.py (and the plotting helpers of figs_l18.py).
Running this module writes /home/claude/work/figs/<name>.html.
Every curve is computed from the formulas (numpy), with the exact propagation constant
gamma = sqrt(j w mu (sigma + j w eps)) and eta = sqrt(j w mu / (sigma + j w eps)) of Lecture 22.
Material values (handbook): copper 5.8e7 S/m, aluminium 3.5e7 S/m, seawater 4 S/m, fresh water 1e-3 S/m,
dry earth 1e-5 S/m, Bakelite 1e-9 S/m, mica 1e-11 S/m (Rao Table 5.1); eps_r: dry earth 5, wet earth 10,
Bakelite 4.9, mica 6 (Rao Table 5.2), seawater 81 (the notes; Rao uses 80), fresh water 80 (Rao Prob. 5.25);
moist soil (loam) 1e-2 S/m (ITU-R P.527-6, sec. 4.1).
Direction check (the only arrows that carry a direction, figure cond-good-conductor-fields), screen frame
X right, Y up, Z out of the screen: physics z (travel) = screen X, physics x (E) = screen Y, so physics
y = z cross x = X cross Y = Z (out of the screen): H along +y is drawn as odot.  E x H = Y cross Z = X: to the right,
into the conductor, as drawn.  (Checked with np.cross in digest8/verify_L23.py, section N.)
"""
from figs import *
from figs import _odot, _otimes, _sub, _tint
from figs_l18 import lin, poly, haxis
import re

mu0 = 4e-7 * np.pi
eps0 = 8.8541878128e-12
c0 = 1 / np.sqrt(mu0 * eps0)
eta0 = np.sqrt(mu0 / eps0)
DB = 20 * np.log10(np.e)            # 8.686 dB per neper


def exact(f, sig, er, mur=1.0):
    """alpha [Np/m], beta [rad/m], |eta| [ohm], tau = angle(eta) [rad], p = sigma/(w eps)"""
    f = np.asarray(f, dtype=float)
    w = 2 * np.pi * f
    mu, eps = mur * mu0, er * eps0
    g = np.sqrt(1j * w * mu * (sig + 1j * w * eps))
    eta = np.sqrt(1j * w * mu / (sig + 1j * w * eps))
    return g.real, g.imag, np.abs(eta), np.angle(eta), sig / (w * eps)


def fc_of(sig, er):
    return sig / (2 * np.pi * er * eps0)


def _sup(base, s, size=9):
    """base text with a superscript s (SVG tspan)"""
    return f'{base}<tspan baseline-shift="super" style="font-size:{size}px">{s}</tspan>'


FC = _sub("f", "c")


def _vis_len(s):
    """number of visible characters in an SVG text string (tags and entities removed)"""
    s = re.sub(r"<[^>]+>", "", s)
    s = re.sub(r"&[a-z]+;", "x", s)
    return len(s)


def tlabel(x, y, s, size=10.5, anchor="middle", fill="currentColor", weight=None, bg=True):
    """text with a paper-coloured backing so that dashed guide lines do not cut through it"""
    w = 0.54 * size * _vis_len(s) + 6
    x0 = x - w / 2 if anchor == "middle" else (x - 3 if anchor == "start" else x - w + 3)
    back = rect(x0, y - size + 1, w, size + 3, fill="var(--paper)", stroke="none", opacity=0.85) if bg else ""
    return back + text(x, y, s, size=size, anchor=anchor, fill=fill, weight=weight)


def ftxt(f):
    """frequency label: 0.89 GHz, 18 MHz, 225 kHz, 3.7 Hz ..."""
    for unit, s in ((1e9, "GHz"), (1e6, "MHz"), (1e3, "kHz"), (1.0, "Hz")):
        if f >= 0.5 * unit:
            v = f / unit
            return (f"{v:.2g}" if v < 10 else f"{v:.0f}") + " " + s
    return f"{f:.2g} Hz"


def logticks_x(MX, Y, decades, labels, size=10):
    """tick marks at every decade, labels where given, on their own baseline below the axis"""
    s = []
    for d in decades:
        s.append(line(MX(d), Y - 3, MX(d), Y + 3, w=1.0))
    for d, lab in labels:
        s.append(text(MX(d), Y + 15, lab, size=size, fill="var(--muted)"))
    return "".join(s)


def vlogaxis(X, Y0, Y1, MY, decs, labels, size=9.5):
    """vertical log axis from Y0 (bottom) to Y1 (top), decade ticks, labels left of the axis"""
    s = [line(X, Y0, X, Y1, w=1.2)]
    for d in decs:
        s.append(line(X - 3, MY(d), X + 3, MY(d), w=1.0))
    for d, lab in labels:
        s.append(text(X - 6, MY(d) + 3.5, lab, size=size, anchor="end", fill="var(--muted)"))
    return "".join(s)


# ------------------------------------------------------------------------------------------ 1. regime map
MEDIA = [  # name, parameter line, sigma [S/m], eps_r
    ("copper", "σ = 5.8×10⁷ S/m, εr = 1", 5.8e7, 1.0),
    ("seawater", "σ = 4 S/m, εr = 81", 4.0, 81.0),
    ("moist soil", "σ = 10⁻² S/m, εr = 10", 1e-2, 10.0),
    ("notes' Ex. 1 medium", "σ = 10⁻³ S/m, εr = 4", 1e-3, 4.0),
    ("fresh water", "σ = 10⁻³ S/m, εr = 80", 1e-3, 80.0),
    ("dry earth", "σ = 10⁻⁵ S/m, εr = 5", 1e-5, 5.0),
    ("Bakelite", "σ = 10⁻⁹ S/m, εr = 4.9", 1e-9, 4.9),
    ("mica", "σ = 10⁻¹¹ S/m, εr = 6", 1e-11, 6.0),
]


def fig_cond_regime_map():
    W, H = 640, 452
    o = [svg_open(W, H)]
    o.append(text(W / 2, 20, "Conductor or dielectric? Compare σ with ωε at the frequency you use", size=13, weight=600))
    L0, L1 = 0.0, 11.0                       # log10 f: 1 Hz .. 100 GHz
    MX = lin(L0, L1, 178, 614)
    y0, dy, bh = 102, 36, 14
    ylast = y0 + (len(MEDIA) - 1) * dy
    # example frequencies (dashed red), labels staggered on two baselines above the first row
    marks = [(76.0, "ELF 76 Hz", 50), (1e3, "1 kHz (Ex. 2, 3)", 66), (24e3, "VLF 24 kHz", 50), (1e9, "1 GHz (Ex. 1)", 50)]
    for f, lab, yl in marks:
        X = MX(np.log10(f))
        o.append(line(X, yl + 5, X, ylast + bh / 2 + 4, stroke="var(--hi)", w=1.2, dash="4 3", opacity=0.75))
        o.append(tlabel(X, yl, lab, size=10, fill="var(--hi)", weight=600))
    for i, (name, par, s, er) in enumerate(MEDIA):
        yc = y0 + i * dy
        fc = fc_of(s, er)
        lfc = np.log10(fc)
        segs = [(L0, lfc - 1, "var(--accent)"), (lfc - 1, lfc + 1, "var(--muted)"), (lfc + 1, L1, "var(--accent2)")]
        for a, b, col in segs:
            a2, b2 = max(a, L0), min(b, L1)
            if b2 > a2:
                o.append(_tint(MX(a2), yc - bh / 2, MX(b2) - MX(a2), bh, col, op=0.55))
        o.append(rect(MX(L0), yc - bh / 2, MX(L1) - MX(L0), bh, stroke="var(--muted)", sw=0.6))
        if L0 <= lfc <= L1:
            o.append(line(MX(lfc), yc - bh / 2 - 2, MX(lfc), yc + bh / 2 + 2, w=1.8))
            lab = FC + " = " + ftxt(fc)
            half = 0.54 * 9.5 * _vis_len(lab) / 2 + 3
            if MX(lfc) - half < MX(L0):
                o.append(tlabel(MX(L0) + 2, yc - bh / 2 - 4, lab, size=9.5, anchor="start", weight=600))
            else:
                o.append(tlabel(MX(lfc), yc - bh / 2 - 4, lab, size=9.5, weight=600))
        elif lfc > L1:
            o.append(tlabel(MX(L1) - 2, yc - bh / 2 - 4, FC + " ≈ 10¹⁸ Hz →", size=9.5, anchor="end", fill="var(--muted)"))
        else:
            o.append(tlabel(MX(L0) + 2, yc - bh / 2 - 4, "← " + FC + " = 0.03 Hz", size=9.5, anchor="start", fill="var(--muted)"))
        o.append(text(170, yc - 1, name, size=12, anchor="end", weight=600))
        o.append(text(170, yc + 12, par, size=9.5, anchor="end", fill="var(--muted)"))
    # frequency axis
    ya = ylast + bh / 2 + 14
    o.append(line(MX(L0), ya, MX(L1), ya, w=1.2))
    o.append(logticks_x(MX, ya, range(0, 12), [(0, "1 Hz"), (3, "1 kHz"), (6, "1 MHz"), (9, "1 GHz"), (11, "100 GHz")]))
    o.append(text(MX(L1) + 6, ya + 4, "f", size=12, anchor="start", math=True))
    # legend (fixed positions)
    yl = ya + 42
    for xl, col, lab in ((40, "var(--accent)", "good conductor: σ/ωε &gt; 10"), (258, "var(--muted)", "in between"),
                         (366, "var(--accent2)", "imperfect dielectric: σ/ωε &lt; 0.1")):
        o.append(_tint(xl, yl - 10, 22, 12, col, op=0.55))
        o.append(text(xl + 28, yl, lab, size=11, anchor="start"))
    o.append(svg_close())
    figure("cond-regime-map", "".join(o),
           "<strong>Whether a medium acts as a conductor depends on the frequency.</strong> Each bar is one medium, "
           "with handbook values of σ and ε (constant with frequency, as in the notes). The tick marks the crossover "
           "frequency f<sub>c</sub> = σ/2πε, where the conduction current σE and the displacement current ωεE are equally "
           "large. More than a decade below it (σ/ωε &gt; 10, blue) the medium is a good conductor; more than a decade above "
           "it (σ/ωε &lt; 0.1, green) it is an imperfect dielectric; within a decade of f<sub>c</sub> (grey) use the "
           "exact formulas. Seawater is a good conductor for the 76 Hz and 24 kHz signals sent to submarines "
           "and for the notes' 1 kHz examples, but not at 1 GHz. Copper is a good conductor at every radio and microwave "
           "frequency; its formal f<sub>c</sub> of 10¹⁸ Hz means nothing, because its σ stops being constant long before "
           "that (Lecture 11). Mica and Bakelite act as dielectrics at any frequency above a few tens of hertz. Soil and water values "
           "vary a lot with moisture, salt and temperature, so treat these bars as typical.")


# ------------------------------------------------------------------------------------------ 2. seawater across the boundary
def fig_cond_seawater_alpha_beta():
    W, H = 640, 590
    o = [svg_open(W, H)]
    s, er = 4.0, 81.0
    fc = fc_of(s, er)
    L0, L1 = 1.0, 11.0                        # 10 Hz .. 100 GHz
    MX = lin(L0, L1, 84, 600)
    ff = np.logspace(L0, L1, 700)
    A, B, ETA, TAU, P = exact(ff, s, er)
    lf = np.log10(ff)
    Xc = MX(np.log10(fc))

    def bands(Ytop, Ybot):
        return "".join([
            _tint(MX(L0), Ytop, MX(np.log10(fc / 10)) - MX(L0), Ybot - Ytop, "var(--accent)", op=0.08),
            _tint(MX(np.log10(10 * fc)), Ytop, MX(L1) - MX(np.log10(10 * fc)), Ybot - Ytop, "var(--accent2)", op=0.12),
            line(Xc, Ytop, Xc, Ybot, stroke="currentColor", w=1.1, dash="2 3")])
    o.append(text(W / 2, 20, "Seawater (σ = 4 S/m, εr = 81) from 10 Hz to 100 GHz, exact Lecture 22 formulas", size=13, weight=600))
    # ---------- panel 1: alpha and beta (log), 1e-2 .. 1e5
    Y0, Y1 = 236, 50
    MY = lin(-2, 5, Y0, Y1)
    o.append(bands(Y1, Y0))
    o.append(vlogaxis(MX(L0), Y0, Y1, MY, range(-2, 6), [(-2, "0.01"), (0, "1"), (2, "100"), (4, "10⁴")]))
    o.append(text(MX(L0) - 44, (Y0 + Y1) / 2, "α [Np/m], β [rad/m]", size=11, rotate=-90))
    o.append(line(MX(L0), Y0, MX(L1), Y0, w=1.2))
    o.append(logticks_x(MX, Y0, range(1, 12), []))
    # asymptotes (dashed grey): sqrt(pi f mu sigma); plateau (sigma/2) sqrt(mu/eps); beta -> w sqrt(mu eps)
    fa = np.logspace(L0, 9.6, 50)
    o.append(poly(np.log10(fa), np.log10(np.sqrt(np.pi * fa * mu0 * s)), MX, MY, stroke="var(--muted)", w=1.4, dash="6 4"))
    plateau = s / 2 * np.sqrt(mu0 / (er * eps0))
    o.append(line(MX(8.2), MY(np.log10(plateau)), MX(L1), MY(np.log10(plateau)), stroke="var(--muted)", w=1.4, dash="6 4"))
    fb = np.logspace(8.3, L1, 30)
    o.append(poly(np.log10(fb), np.log10(2 * np.pi * fb * np.sqrt(mu0 * er * eps0)), MX, MY, stroke="var(--muted)", w=1.4, dash="6 4"))
    o.append(poly(lf, np.log10(B), MX, MY, stroke="var(--accent2)", w=2.2))
    o.append(poly(lf, np.log10(A), MX, MY, stroke="var(--accent)", w=2.6))
    o.append(text(MX(1.3), MY(0.45), "α ≈ β ≈ √(πfμσ)", size=11, anchor="start", fill="var(--accent)", weight=600))
    o.append(text(MX(1.3), MY(0.45) + 14, "(the two curves coincide)", size=10, anchor="start", fill="var(--muted)"))
    o.append(tlabel(MX(10.95), MY(np.log10(plateau)) + 28, "α → (σ/2)√(μ/ε) = 84 Np/m", size=10.5, anchor="end", fill="var(--accent)", weight=600))
    o.append(tlabel(MX(10.15), MY(np.log10(2 * np.pi * 10 ** 10.3 * np.sqrt(mu0 * er * eps0))) - 6, "β → ω√(με)", size=10.5,
                    anchor="end", fill="var(--accent2)", weight=600))
    o.append(tlabel(Xc - 4, Y0 - 6, FC + " = 0.89 GHz", size=10, anchor="end", weight=600))
    a1k = exact(1e3, s, er)[0]
    a1g = exact(1e9, s, er)[0]
    o.append(circle(MX(3), MY(np.log10(a1k)), 3.6, fill="var(--hi)", stroke="none"))
    o.append(text(MX(3) + 8, MY(np.log10(a1k)) + 16, "1 kHz: α = π/25 = 0.126 Np/m", size=10, anchor="start", fill="var(--hi)"))
    o.append(circle(MX(9), MY(np.log10(a1g)), 3.6, fill="var(--hi)", stroke="none"))
    o.append(tlabel(MX(9) - 7, MY(np.log10(a1g)) - 24, "1 GHz: α = 77 Np/m", size=10, anchor="end", fill="var(--hi)"))
    o.append(text(MX(1.1), Y1 + 12, "good conductor", size=10, anchor="start", fill="var(--accent)", weight=600))
    o.append(text(MX(10.98), Y1 + 12, "dielectric", size=10, anchor="end", fill="var(--accent2)", weight=600))
    # ---------- panel 2: |eta| (log), 1e-3 .. 1e2
    Y0b, Y1b = 384, 270
    MYb = lin(-3, 2, Y0b, Y1b)
    o.append(bands(Y1b, Y0b))
    o.append(vlogaxis(MX(L0), Y0b, Y1b, MYb, range(-3, 3), [(-3, "0.001"), (-1, "0.1"), (1, "10")]))
    o.append(text(MX(L0) - 44, (Y0b + Y1b) / 2, "|η| [Ω]", size=11, rotate=-90))
    o.append(line(MX(L0), Y0b, MX(L1), Y0b, w=1.2))
    o.append(logticks_x(MX, Y0b, range(1, 12), []))
    fe = np.logspace(L0, 10.0, 40)
    o.append(poly(np.log10(fe), np.log10(np.sqrt(2 * np.pi * fe * mu0 / s)), MX, MYb, stroke="var(--muted)", w=1.4, dash="6 4"))
    eta_d = np.sqrt(mu0 / (er * eps0))
    o.append(line(MX(8.0), MYb(np.log10(eta_d)), MX(L1), MYb(np.log10(eta_d)), stroke="var(--muted)", w=1.4, dash="6 4"))
    o.append(poly(lf, np.log10(ETA), MX, MYb, stroke="var(--accent)", w=2.6))
    o.append(text(MX(4.0), MYb(-1.9), "|η| ≈ √(ωμ/σ): far below √(μ/ε)", size=11, anchor="start", fill="var(--accent)", weight=600))
    o.append(tlabel(MX(10.95), MYb(np.log10(eta_d)) + 20, "→ √(μ/ε) = η₀/9 = 42 Ω", size=10.5, anchor="end", fill="var(--accent)", weight=600))
    # ---------- panel 3: tau = angle(eta), degrees
    Y0c, Y1c = 520, 420
    MYc = lin(0, 50, Y0c, Y1c)
    o.append(bands(Y1c, Y0c))
    o.append(line(MX(L0), Y0c, MX(L0), Y1c, w=1.2))
    for tv in (0, 15, 30, 45):
        o.append(line(MX(L0) - 3, MYc(tv), MX(L0) + 3, MYc(tv), w=1.0))
        o.append(text(MX(L0) - 6, MYc(tv) + 3.5, f"{tv}°", size=9.5, anchor="end", fill="var(--muted)"))
    o.append(text(MX(L0) - 44, (Y0c + Y1c) / 2, "τ = ∠η", size=11, rotate=-90))
    o.append(line(MX(L0), MYc(45), MX(L1), MYc(45), stroke="var(--muted)", w=1.2, dash="6 4"))
    o.append(poly(lf, np.degrees(TAU), MX, MYc, stroke="var(--accent)", w=2.6))
    o.append(text(MX(4.0), MYc(45) + 15, "τ = 45°: H lags E by 45°", size=11, anchor="start", fill="var(--accent)", weight=600))
    o.append(tlabel(MX(10.95), MYc(22), "τ ≈ σ/2ωε → 0", size=10.5, anchor="end", fill="var(--accent)", weight=600))
    o.append(line(MX(L0), Y0c, MX(L1), Y0c, w=1.2))
    o.append(logticks_x(MX, Y0c, range(1, 12), [(1, "10 Hz"), (3, "1 kHz"), (5, "100 kHz"), (7, "10 MHz"), (9, "1 GHz"), (11, "100 GHz")]))
    o.append(text(MX(L1) + 6, Y0c + 4, "f", size=12, anchor="start", math=True))
    o.append(text(W / 2, H - 22, "dashed grey: the good-conductor and imperfect-dielectric approximations;  dotted: σ = ωε",
                  size=10.5, fill="var(--muted)"))
    o.append(svg_close())
    figure("cond-seawater-alpha-beta", "".join(o),
           "<strong>One medium, both regimes.</strong> The curves are the exact α, β, |η| and τ = ∠η of seawater, "
           "computed from γ = √(jωμ(σ + jωε)) and η = √(jωμ/(σ + jωε)). Below about 90 MHz (blue band, σ/ωε &gt; 10) "
           "the good-conductor formulas hold: α and β are equal and both grow as √f, |η| = √(ωμ/σ) is far below the "
           "lossless √(μ/ε) (0.044 Ω at 1 kHz, 1.4 Ω at 1 MHz), and η has a phase of 45°. Above about 9 GHz (green band, σ/ωε &lt; 0.1) the imperfect-dielectric "
           "formulas take over: β grows in proportion to f, |η| levels off at √(μ/ε) = 42 Ω, the phase drops toward zero, "
           "and α stops growing at (σ/2)√(μ/ε) = 84 Np/m, a penetration depth of 1.2 cm that no higher frequency improves. "
           "Between the bands, use the exact formulas. The red dots are the notes' 1 kHz examples "
           "(δ = 7.96 m) and seawater at 1 GHz, where α is about 600 times larger. The constant ε = 81ε₀ is itself an "
           "approximation above a few GHz.")


# ------------------------------------------------------------------------------------------ 3. good-conductor fields
def fig_cond_good_conductor_fields():
    W, H = 640, 540
    o = [svg_open(W, H)]
    # ---------- panel 1: record at the surface z = 0: E ~ cos(wt), H ~ cos(wt - pi/4)
    o.append(text(20, 22, "1  At the surface z = 0: H peaks one-eighth of a period after E", size=12.5, anchor="start", weight=600))
    MT = lin(0, 4 * np.pi, 70, 430)
    Y1, A1 = 104, 46
    MY1 = lambda v: Y1 - A1 * v
    o.append(haxis(60, 446, Y1, "ωt", [(k * np.pi, None) for k in range(5)], MT, tick_labels=False))
    for k, lab in ((1, "π"), (2, "2π"), (3, "3π"), (4, "4π")):
        o.append(text(MT(k * np.pi), Y1 + A1 + 16, lab, size=10.5, fill="var(--muted)"))
    wt = np.linspace(0, 4 * np.pi, 400)
    o.append(poly(wt, np.cos(wt), MT, MY1, stroke="var(--accent)", w=2.4))
    o.append(poly(wt, np.cos(wt - np.pi / 4), MT, MY1, stroke="var(--accent2)", w=2.4, dash="7 4"))
    o.append(line(MT(2 * np.pi), MY1(1.0) - 4, MT(2 * np.pi), Y1 + 6, stroke="var(--accent)", w=1.0, dash="2 2"))
    o.append(line(MT(2 * np.pi + np.pi / 4), MY1(1.0) - 4, MT(2 * np.pi + np.pi / 4), Y1 + 6, stroke="var(--accent2)", w=1.0, dash="2 2"))
    o.append(arrow(MT(2 * np.pi), MY1(1.0) - 10, MT(2 * np.pi + np.pi / 4), MY1(1.0) - 10, stroke="var(--hi)", w=1.6, small=True))
    o.append(text(MT(2 * np.pi + np.pi / 8), MY1(1.0) - 16, "45° = T/8", size=10.5, fill="var(--hi)", weight=600))
    o.append(text(438, MY1(1.0) + 2, "E/E₀", size=11, anchor="start", fill="var(--accent)", weight=700))
    o.append(text(438, MY1(np.cos(-np.pi / 4)) + 12, "H/H₀", size=11, anchor="start", fill="var(--accent2)", weight=700))
    # ---------- icon: travel along +z = screen right, E along +x = screen up, H along +y = out of the screen
    # np.cross(Y, Z) = X: E (up) x H (out of the screen, odot) = right = travel into the conductor (verify_L23.py section N)
    gx, gy = 530, 100
    o.append(rect(gx - 12, gy - 60, 110, 120, fill="var(--muted)", stroke="none", opacity=0.10))
    o.append(line(gx - 12, gy - 60, gx - 12, gy + 60, stroke="currentColor", w=2.2))
    o.append(text(gx - 16, gy - 46, "air", size=10, anchor="end", fill="var(--muted)"))
    o.append(text(gx + 94, gy - 46, "conductor", size=10, anchor="end", fill="var(--muted)"))
    o.append(arrow(gx + 20, gy + 20, gx + 20, gy - 24, stroke="var(--accent)", w=2.4))
    o.append(text(gx + 26, gy - 18, "E", size=13, anchor="start", fill="var(--accent)", weight=700, math=True))
    o.append(_odot(gx + 54, gy + 2, r=7, color="var(--accent2)"))
    o.append(text(gx + 64, gy - 6, "H", size=13, anchor="start", fill="var(--accent2)", weight=700, math=True))
    o.append(arrow(gx + 30, gy + 40, gx + 84, gy + 40, stroke="currentColor", w=2.2, small=True))
    o.append(text(gx + 57, gy + 54, "E × H", size=10.5, weight=600))
    o.append(text(gx + 44, gy + 78, "x up, z right, y out (⊙)", size=9.5, fill="var(--muted)"))
    # ---------- panel 2: snapshot at t = 0 against depth, one wavelength = 2 pi delta
    o.append(text(20, 200, "2  A snapshot at t = 0: within one wavelength λ = 2πδ the field all but disappears",
                  size=12.5, anchor="start", weight=600))
    U1 = 2 * np.pi + 0.35
    MZ = lin(0, U1, 70, 600)
    Y2, A2 = 334, 100
    MY2 = lambda v: Y2 - A2 * v
    o.append(haxis(60, 612, Y2, "z", [(k, None) for k in range(1, 7)], MZ, tick_labels=False))
    for k in range(1, 7):
        o.append(text(MZ(k), Y2 + A2 + 16, ("δ" if k == 1 else f"{k}δ"), size=10.5, fill="var(--muted)"))
    o.append(line(MZ(2 * np.pi), Y2 - 6, MZ(2 * np.pi), Y2 + 6, stroke="var(--hi)", w=2.0))
    o.append(text(MZ(2 * np.pi) + 4, Y2 - 12, "λ = 2πδ: field down to " + _sup("e", "−2π") + " ≈ 1/535", size=11,
                  anchor="end", fill="var(--hi)", weight=600))
    u = np.linspace(0, U1, 500)
    env = np.exp(-u)
    o.append(poly(u, env, MZ, MY2, stroke="var(--muted)", w=1.3, dash="5 4"))
    o.append(poly(u, -env, MZ, MY2, stroke="var(--muted)", w=1.3, dash="5 4"))
    o.append(poly(u, np.exp(-2 * u), MZ, MY2, stroke="var(--hi)", w=1.6, dash="2 3"))
    o.append(poly(u, env * np.cos(u), MZ, MY2, stroke="var(--accent)", w=2.6))
    o.append(poly(u, env * np.cos(u + np.pi / 4), MZ, MY2, stroke="var(--accent2)", w=2.4, dash="7 4"))
    # 1/e guide: the power reaches 1/e at delta/2, the field envelope at delta
    ye = MY2(np.exp(-1))
    o.append(line(MZ(0), ye, MZ(1), ye, stroke="currentColor", w=0.9, dash="3 3"))
    o.append(text(MZ(0) - 6, ye + 4, "1/e", size=10.5, anchor="end"))
    o.append(circle(MZ(0.5), ye, 3.6, fill="var(--hi)", stroke="none"))
    o.append(circle(MZ(1.0), ye, 3.6, fill="currentColor", stroke="none"))
    # legend block in the empty upper right (above the envelope everywhere)
    lx, ly = MZ(2.55), 236
    rows = [("var(--accent)", "blue: E/E₀ = " + _sup("e", "−z/δ") + " cos(z/δ)"),
            ("var(--accent2)", "green, dashed: H/H₀ = " + _sup("e", "−z/δ") + " cos(z/δ + π/4)"),
            ("var(--muted)", "grey, dashed: the envelope ±" + _sup("e", "−z/δ")),
            ("var(--hi)", "red, dotted: the power, ∝ " + _sup("e", "−2z/δ")),
            ("currentColor", "dots: power down to 1/e at δ/2, the field at δ")]
    for k, (col, lab) in enumerate(rows):
        o.append(text(lx, ly + 17 * k, lab, size=10.5, anchor="start", fill=col, weight=600 if k < 4 else None))
    o.append(text(W / 2, H - 34, "E = x̂ E₀ " + _sup("e", "−z/δ") + " cos(ωt − z/δ),   H = ŷ H₀ " + _sup("e", "−z/δ")
                  + " cos(ωt − z/δ − π/4),   H₀ = E₀/|η| = σδE₀/√2", size=11.5, weight=600))
    o.append(text(W / 2, H - 14, "each field is drawn relative to its own amplitude; H₀ is far larger than E₀/η₀ would be in air",
                  size=10.5, fill="var(--muted)"))
    o.append(svg_close())
    figure("cond-good-conductor-fields", "".join(o),
           "<strong>A plane wave inside a good conductor, travelling along +z.</strong> Panel 1 is the record at the surface: "
           "because η = (1 + j)/(σδ) has a phase of 45°, H reaches each maximum one-eighth of a period after E. Panel 2 is a "
           "snapshot against depth, in units of δ = 1/√(πfμσ). Since α = β = 1/δ, the decay and the phase advance happen "
           "on the same length scale. The field envelope falls to 1/e at one skin depth; the power, which goes as the "
           "square, is already down to 1/e at δ/2 and to e<sup>−2</sup> = 14 % at δ. After one wavelength λ = 2πδ the "
           "field is down to e<sup>−2π</sup> ≈ 1/535 (−54.6 dB), and after two wavelengths to −109 dB: in a good conductor "
           "a wave is effectively gone within a wavelength or two. The icon checks the direction: with x up, z to the right and y out of the page, E (up) × H (out, ⊙) "
           "points right, into the conductor.")


# ------------------------------------------------------------------------------------------ 4. skin depth: metals and seawater
def fig_cond_skin_depth():
    W, H = 640, 590
    o = [svg_open(W, H)]
    L0, L1 = 1.0, 11.0
    MX = lin(L0, L1, 92, 600)
    xlabels = [(1, "10 Hz"), (3, "1 kHz"), (5, "100 kHz"), (7, "10 MHz"), (9, "1 GHz"), (11, "100 GHz")]
    # ---------- panel 1: metals
    o.append(text(20, 22, "1  Metals: δ = 1/√(πfμσ), millimetres at 60 Hz, micrometres at microwave frequencies", size=12.5, anchor="start", weight=600))
    Y0, Y1 = 236, 46
    MY = lin(-7, -1, Y0, Y1)              # log10 delta [m]: 0.1 um .. 100 mm
    o.append(vlogaxis(MX(L0), Y0, Y1, MY, range(-7, 0),
                      [(-7, "0.1 µm"), (-6, "1 µm"), (-5, "10 µm"), (-4, "100 µm"), (-3, "1 mm"), (-2, "10 mm"), (-1, "100 mm")]))
    o.append(line(MX(L0), Y0, MX(L1), Y0, w=1.2))
    o.append(logticks_x(MX, Y0, range(1, 12), xlabels))
    ff = np.logspace(L0, L1, 60)
    for sg, col in ((5.8e7, "var(--accent)"), (3.5e7, "var(--accent2)")):
        d = 1 / np.sqrt(np.pi * ff * mu0 * sg)
        o.append(poly(np.log10(ff), np.log10(d), MX, MY, stroke=col, w=2.4))
    # legend in the empty lower-left corner (the lines run from upper left to lower right)
    o.append(line(MX(1.2), MY(-5.45) - 4, MX(1.2) + 22, MY(-5.45) - 4, stroke="var(--accent2)", w=2.4))
    o.append(text(MX(1.2) + 28, MY(-5.45), "aluminium, σ = 3.5×10⁷ S/m (upper line)", size=10.5, anchor="start", fill="var(--accent2)", weight=600))
    o.append(line(MX(1.2), MY(-5.95) - 4, MX(1.2) + 22, MY(-5.95) - 4, stroke="var(--accent)", w=2.4))
    o.append(text(MX(1.2) + 28, MY(-5.95), "copper, σ = 5.8×10⁷ S/m (lower line)", size=10.5, anchor="start", fill="var(--accent)", weight=600))
    for f, lab in ((60.0, "60 Hz: Cu 8.5 mm, Al 11 mm"), (1e6, "1 MHz: Cu 66 µm"), (1e9, "1 GHz: Cu 2.1 µm")):
        d = 1 / np.sqrt(np.pi * f * mu0 * 5.8e7)
        o.append(circle(MX(np.log10(f)), MY(np.log10(d)), 3.4, fill="var(--hi)", stroke="none"))
        o.append(text(MX(np.log10(f)) + 8, MY(np.log10(d)) - 9, lab, size=10, anchor="start", fill="var(--hi)"))
    # ---------- panel 2: seawater, exact, and the 100 dB depth
    o.append(text(20, 296, "2  Seawater: the skin depth δ, and the depth where a signal is 100 dB down (11.5δ)",
                  size=12.5, anchor="start", weight=600))
    s, er = 4.0, 81.0
    Y0b, Y1b = 530, 316
    MYb = lin(-3, 3, Y0b, Y1b)          # log10 depth [m]: 1 mm .. 1 km
    o.append(vlogaxis(MX(L0), Y0b, Y1b, MYb, range(-3, 4),
                      [(-3, "1 mm"), (-2, "1 cm"), (-1, "10 cm"), (0, "1 m"), (1, "10 m"), (2, "100 m"), (3, "1 km")]))
    o.append(line(MX(L0), Y0b, MX(L1), Y0b, w=1.2))
    o.append(logticks_x(MX, Y0b, range(1, 12), xlabels))
    o.append(text(MX(L1) + 6, Y0b + 4, "f", size=12, anchor="start", math=True))
    fs = np.logspace(L0, L1, 500)
    A = exact(fs, s, er)[0]
    fc = fc_of(s, er)
    o.append(line(MX(np.log10(fc)), Y1b, MX(np.log10(fc)), Y0b, stroke="currentColor", w=1.1, dash="2 3"))
    o.append(tlabel(MX(np.log10(fc)) + 4, Y1b + 12, FC + " = 0.89 GHz", size=10, anchor="start", weight=600))
    fg = np.logspace(L0, 10.75, 300)            # keep the dotted good-conductor line above 1 mm
    o.append(poly(np.log10(fg), np.log10(1 / np.sqrt(np.pi * fg * mu0 * s)), MX, MYb, stroke="var(--muted)", w=1.3, dash="2 3"))
    o.append(poly(np.log10(fs), np.log10(100 / (DB * A)), MX, MYb, stroke="var(--accent2)", w=2.2, dash="7 4"))
    o.append(poly(np.log10(fs), np.log10(1 / A), MX, MYb, stroke="var(--accent)", w=2.6))
    # legend in the empty lower-left corner
    lx, ly = MX(1.2), 462
    o.append(line(lx, ly - 4, lx + 22, ly - 4, stroke="var(--accent)", w=2.6))
    o.append(text(lx + 28, ly, "skin depth δ = 1/α (exact)", size=10.5, anchor="start", fill="var(--accent)", weight=600))
    o.append(line(lx, ly + 13, lx + 22, ly + 13, stroke="var(--accent2)", w=2.2, dash="7 4"))
    o.append(text(lx + 28, ly + 17, "depth for a 100 dB loss = 11.5δ", size=10.5, anchor="start", fill="var(--accent2)", weight=600))
    o.append(line(lx, ly + 30, lx + 22, ly + 30, stroke="var(--muted)", w=1.3, dash="2 3"))
    o.append(text(lx + 28, ly + 34, "1/√(πfμσ), used out of its range", size=10.5, anchor="start", fill="var(--muted)"))
    o.append(tlabel(MX(10.98), MYb(np.log10(1 / exact(1e11, s, er)[0])) - 8, "δ levels off at 1.2 cm", size=10, anchor="end", fill="var(--accent)"))
    pts = [(76.0, "ELF 76 Hz: δ = 29 m, 100 dB at 330 m"), (1e3, "1 kHz: δ = 7.96 m, 100 dB at 92 m"),
           (24e3, "VLF 24 kHz: δ = 1.6 m, 100 dB at 19 m"), (1e9, "1 GHz: δ = 1.3 cm, 100 dB at 15 cm")]
    for f, lab in pts:
        a = exact(f, s, er)[0]
        X = MX(np.log10(f))
        o.append(line(X, MYb(np.log10(1 / a)), X, MYb(np.log10(100 / (DB * a))), stroke="var(--hi)", w=1.0, opacity=0.6))
        o.append(circle(X, MYb(np.log10(1 / a)), 3.4, fill="var(--hi)", stroke="none"))
        o.append(circle(X, MYb(np.log10(100 / (DB * a))), 3.4, fill="var(--hi)", stroke="none"))
    for f, lab in pts[:3]:
        a = exact(f, s, er)[0]
        o.append(tlabel(MX(np.log10(f)) + 8, MYb(np.log10(100 / (DB * a))) - 9, lab, size=10, anchor="start", fill="var(--hi)"))
    o.append(tlabel(MX(9) - 8, Y0b - 22, pts[3][1], size=10, anchor="end", fill="var(--hi)"))
    o.append(svg_close())
    figure("cond-skin-depth", "".join(o),
           "<strong>Skin depths as numbers.</strong> Panel 1: in copper and aluminium δ = 1/√(πfμσ) holds at every "
           "radio and microwave frequency, and it is small. It is 8.5 mm (copper) and 11 mm (aluminium) at the 60 Hz "
           "of the power grid, 66 µm in copper at 1 MHz and 2.1 µm at 1 GHz. Halving δ takes four times the frequency. "
           "Panel 2: seawater, from the exact formula. Its δ follows the same √f law up to about 100 MHz, then levels "
           "off at 1.2 cm once seawater stops being a good conductor; the dotted line shows how wrong the good-conductor "
           "formula would be there. The dashed curve is the depth at which a signal has lost 100 dB, an illustrative "
           "receiver budget equal to 100/8.686 = 11.5 skin depths. It is about 330 m at the 76 Hz of the former US Navy "
           "ELF system and about 19 m at a 24 kHz VLF frequency, against 15 cm at 1 GHz.")


# ------------------------------------------------------------------------------------------ 5. worked problem: loss against depth in moist soil
def fig_cond_problem_depth():
    W, H = 640, 384
    o = [svg_open(W, H)]
    s, er = 1e-2, 10.0
    o.append(text(W / 2, 20, "Worked problem: moist soil (σ = 10⁻² S/m, εr = 10), loss against depth", size=13, weight=600))
    MZ = lin(0, 120, 84, 588)
    MY = lin(-60, 0, 322, 44)
    for dbv in range(0, -61, -10):
        o.append(line(MZ(0) - 3, MY(dbv), MZ(0) + 3, MY(dbv), w=1.0))
        o.append(text(MZ(0) - 6, MY(dbv) + 3.5, f"{dbv}".replace("-", "−"), size=10, anchor="end", fill="var(--muted)"))
        if dbv < 0:
            o.append(line(MZ(0), MY(dbv), MZ(120), MY(dbv), stroke="var(--muted)", w=0.6, opacity=0.4))
    o.append(line(MZ(0), MY(0), MZ(120), MY(0), w=1.2))
    o.append(line(MZ(0), MY(0), MZ(0), MY(-60), w=1.2))
    o.append(text(MZ(0) - 42, MY(-30), "level relative to the surface [dB]", size=11, rotate=-90))
    for zv in range(0, 121, 20):
        o.append(line(MZ(zv), MY(-60) - 3, MZ(zv), MY(-60) + 3, w=1.0))
        o.append(text(MZ(zv), MY(-60) + 16, f"{zv}", size=10, fill="var(--muted)"))
    o.append(line(MZ(0), MY(-60), MZ(120), MY(-60), w=1.2))
    o.append(text(MZ(120), MY(-60) + 32, "depth d below the surface [m]", size=11, anchor="end"))
    zz = np.linspace(0, 120, 200)
    for f, col, w_, dash in ((1e5, "var(--accent)", 2.6, None), (5.3718e4, "var(--accent2)", 2.4, "7 4"), (1e7, "var(--hi)", 2.0, "2 3")):
        a = exact(f, s, er)[0]
        zs = zz[zz <= min(120.0, 60 / (DB * a))]
        o.append(poly(zs, -DB * a * zs, MZ, MY, stroke=col, w=w_, dash=dash))
    # legend in the empty upper right (above the 53.7 kHz line)
    lx = MZ(66)
    for k, (col, dash, w_, lab) in enumerate((("var(--accent)", None, 2.6, "100 kHz: 0.55 dB/m (the problem)"),
                                              ("var(--accent2)", "7 4", 2.4, "53.7 kHz: 0.40 dB/m (part e)"),
                                              ("var(--hi)", "2 3", 2.0, "10 MHz: 4.2 dB/m (the variant)"))):
        yk = MY(-6) + 16 * k
        o.append(line(lx, yk - 4, lx + 22, yk - 4, stroke=col, w=w_, dash=dash))
        o.append(text(lx + 28, yk, lab, size=10.5, anchor="start", fill=col, weight=600))
    # points A, B on the 100 kHz line and C on the 53.7 kHz line; letters placed off the lines
    for zv, dbv, col, let, dx, dy, anc in ((25.0, -13.64, "var(--accent)", "A", -6, 14, "end"),
                                           (36.65, -20.0, "var(--accent)", "B", -6, 14, "end"),
                                           (100.0, -40.0, "var(--accent2)", "C", 8, -6, "start")):
        o.append(circle(MZ(zv), MY(dbv), 3.8, fill=col, stroke="none"))
        o.append(text(MZ(zv) + dx, MY(dbv) + dy, let, size=12, anchor=anc, fill=col, weight=700))
    for k, lab in enumerate(("A: 25 m, power down to 4.3 % (−13.6 dB)", "B: 36.6 m, 1 % of the power (−20 dB)",
                             "C: at 53.7 kHz, 40 dB at 100 m")):
        o.append(text(MZ(20), MY(-48) + 17 * k, lab, size=10.5, anchor="start"))
    o.append(svg_close())
    figure("cond-problem-depth", "".join(o),
           "<strong>Loss against depth in the worked problem's soil, from the exact α.</strong> Loss in decibels is the "
           "same number for the field and for the power, 8.686αd, so each frequency gives a straight line. At 100 kHz "
           "the soil is a good conductor with δ = 15.9 m, and the wave loses 0.55 dB per metre: 13.6 dB (a power factor "
           "e<sup>−π</sup>) at 25 m (A), and 20 dB (1 % of the power) at 36.6 m (B). Lowering the frequency to 53.7 kHz "
           "makes the slope 0.40 dB/m, which meets a 40 dB budget at 100 m (C). At 10 MHz the soil is between regimes "
           "(σ/ωε = 1.8): the exact α gives 4.2 dB/m, and neither the good-conductor nor the imperfect-dielectric formula "
           "is accurate there.")


if __name__ == "__main__":
    for fn in (fig_cond_regime_map, fig_cond_seawater_alpha_beta, fig_cond_good_conductor_fields, fig_cond_skin_depth,
               fig_cond_problem_depth):
        fn()
