#!/usr/bin/env python3
"""Lecture 31-33 figures (res-*) for the ECE 329 notes: resonances of line segments, stub reactance,
stub filters, half- and quarter-wave sections.

Same helpers and conventions as figs.py (plot helpers from figs_l18.py). Running this module writes
tools/figs/<name>.html. Every curve is computed with numpy from the formulas checked in
tools/build14/checks/L31_33.py (mode shapes, j Z0 tan(beta l), -j Z0 cot(beta l), the notes' Examples 1 and 3
of Lecture 32). No vector directions are drawn, so no cross products are needed.
"""
from figs import *
from figs import _zigzag, _sub
from figs_l18 import lin, poly

PI = np.pi
CV, CI = "var(--accent)", "var(--hi)"


def _clipped(xs, ys, MX, MY, ymax, **kw):
    """polyline broken wherever |y| > ymax (asymptotes)"""
    out, seg = [], []
    for x, y in zip(xs, ys):
        if abs(y) <= ymax:
            seg.append((x, y))
        else:
            if len(seg) > 1:
                out.append(poly([p[0] for p in seg], [p[1] for p in seg], MX, MY, **kw))
            seg = []
    if len(seg) > 1:
        out.append(poly([p[0] for p in seg], [p[1] for p in seg], MX, MY, **kw))
    return "".join(out)


def fig_modes():
    W, H = 660, 318
    o = [svg_open(W, H)]
    cols = [(46, "open", "open", lambda n, u: (abs(np.cos(n * PI * u)), abs(np.sin(n * PI * u))), [(1, "ℓ = λ/2"), (2, "ℓ = λ")]),
            (376, "open", "short", lambda n, u: (abs(np.cos((2 * n + 1) * PI * u / 2)), abs(np.sin((2 * n + 1) * PI * u / 2))), [(0, "ℓ = λ/4"), (1, "ℓ = 3λ/4")])]
    u = np.linspace(0, 1, 241)
    for X0, le, re_, fn, rows in cols:
        X1 = X0 + 240
        o.append(text((X0 + X1) / 2, 18, f"{le} at z = 0, {re_} at z = ℓ", size=12.5, weight=600))
        for r, (n, lab) in enumerate(rows):
            Yb = 122 + r * 132; Yt = Yb - 78
            MX = lin(0, 1, X0, X1); MY = lin(0, 1, Yb, Yt)
            o.append(line(X0, Yb, X1 + 16, Yb, w=1.2, arrow=True)); o.append(text(X1 + 22, Yb + 4, "z", size=12, anchor="start", math=True))
            o.append(line(X0, Yb, X0, Yt - 10, w=1.0)); o.append(line(X1, Yb, X1, Yt - 10, w=1.0, dash="3 3"))
            v, i = fn(n, u)
            o.append(poly(u, v, MX, MY, stroke=CV, w=2.2))
            o.append(poly(u, i, MX, MY, stroke=CI, w=2.2, dash="6 4"))
            o.append(text(X0, Yb + 15, "0", size=10.5, fill="var(--muted)")); o.append(text(X1, Yb + 15, "ℓ", size=11, fill="var(--muted)", math=True))
            o.append(text((X0 + X1) / 2, Yb + 30, lab + (f"   (n = {n})"), size=11.5))
            # end markers
            o.append(text(X0 - 6, Yt - 14, le, size=10, anchor="end", fill="var(--muted)"))
            o.append(text(X1 + 6, Yt - 14, re_, size=10, anchor="start", fill="var(--muted)"))
    # legend
    o.append(line(250, 300, 280, 300, stroke=CV, w=2.2)); o.append(text(286, 304, "|V|", size=12, anchor="start"))
    o.append(line(340, 300, 370, 300, stroke=CI, w=2.2, dash="6 4")); o.append(text(376, 304, "|I|", size=12, anchor="start"))
    o.append(svg_close())
    figure("res-modes", "".join(o),
           "Standing-wave envelopes of the two lowest resonances. Left, both ends open: the current is zero at both ends and a whole number of half wavelengths fits. "
           "Right, one end open and one shorted: the current is zero at the open end, the voltage at the short, and an odd number of quarter wavelengths fits. "
           "Voltage nulls sit on current maxima. With both ends shorted, swap the two curves of the left panel.")


def fig_reactance():
    W, H = 640, 300
    o = [svg_open(W, H)]
    X0, X1, Yc, ymax = 60, 590, 150, 4.0
    MX = lin(0, 1, X0, X1); MY = lin(-ymax, ymax, Yc + 118, Yc - 118)
    # inductive / capacitive bands for the shorted stub
    for a, b, lab in ((0, 0.25, "inductive"), (0.25, 0.5, "capacitive"), (0.5, 0.75, "inductive"), (0.75, 1.0, "capacitive")):
        col = "var(--accent)" if lab == "inductive" else "var(--accent2)"
        o.append(f'<rect x="{MX(a):.1f}" y="{MY(ymax):.1f}" width="{MX(b) - MX(a):.1f}" height="{MY(-ymax) - MY(ymax):.1f}" fill="{col}" fill-opacity="0.07" stroke="none"/>')
        o.append(text((MX(a) + MX(b)) / 2, MY(ymax) + 13, lab, size=10.5, fill="var(--muted)"))
    o.append(line(X0, Yc, X1 + 14, Yc, w=1.3, arrow=True)); o.append(text(X1 + 20, Yc + 4, "ℓ", size=13, anchor="start", math=True))
    o.append(line(X0, MY(-ymax), X0, MY(ymax) - 12, w=1.3, arrow=True)); o.append(text(X0, MY(ymax) - 18, "X / Z₀", size=12))
    for tv, tl in ((0.25, "λ/4"), (0.5, "λ/2"), (0.75, "3λ/4"), (1.0, "λ")):
        o.append(line(MX(tv), Yc - 3, MX(tv), Yc + 3, w=1.1)); o.append(text(MX(tv) + 12, Yc + 15, tl, size=10.5, fill="var(--muted)"))
    for yv in (-2, -1, 1, 2):
        o.append(line(X0 - 3, MY(yv), X0 + 3, MY(yv), w=1.0)); o.append(text(X0 - 8, MY(yv) + 4, f"{yv:+d}".replace("-", "−"), size=10, anchor="end", fill="var(--muted)"))
    for tv in (0.25, 0.75):
        o.append(line(MX(tv), MY(-ymax), MX(tv), MY(ymax), stroke=CV, w=0.8, dash="2 4"))
    for tv in (0.5, 1.0):
        o.append(line(MX(tv), MY(-ymax), MX(tv), MY(ymax), stroke=CI, w=0.8, dash="2 4"))
    u = np.linspace(1e-4, 1 - 1e-4, 4001)
    o.append(_clipped(u, np.tan(2 * PI * u), MX, MY, ymax, stroke=CV, w=2.2))
    o.append(_clipped(u, -1 / np.tan(2 * PI * u), MX, MY, ymax, stroke=CI, w=2.0, dash="6 4"))
    o.append(line(80, 286, 110, 286, stroke=CV, w=2.2)); o.append(text(116, 290, "shorted stub:  X = Z₀ tan βℓ", size=11.5, anchor="start"))
    o.append(line(340, 286, 370, 286, stroke=CI, w=2.0, dash="6 4")); o.append(text(376, 290, "open stub:  X = −Z₀ cot βℓ", size=11.5, anchor="start"))
    o.append(svg_close())
    figure("res-reactance", "".join(o),
           "Input reactance of a stub against its length (the band labels are for the shorted stub). The shorted stub starts as an inductor, becomes an open circuit at λ/4, "
           "is capacitive up to λ/2 and is a short circuit again there. The open stub is the same curve shifted by λ/4. Everything repeats every λ/2.")


def fig_filter():
    W, H = 640, 250
    o = [svg_open(W, H)]
    X0, X1, Yb, Yt = 60, 590, 196, 36
    MX = lin(0, 300, X0, X1); MY = lin(0, 1, Yb, Yt)
    o.append(line(X0, Yb, X1 + 14, Yb, w=1.3, arrow=True)); o.append(text(X1 + 18, Yb + 4, "f", size=13, anchor="start", math=True))
    o.append(line(X0, Yb, X0, Yt - 14, w=1.3, arrow=True)); o.append(text(X0 + 6, Yt - 16, "|H|", size=12, anchor="start"))
    for fv in (50, 100, 150, 200, 250, 300):
        o.append(line(MX(fv), Yb - 3, MX(fv), Yb + 3, w=1.1)); o.append(text(MX(fv), Yb + 15, f"{fv}", size=10.5, fill="var(--muted)"))
    o.append(text((X0 + X1) / 2, Yb + 32, "MHz", size=11, fill="var(--muted)"))
    for yv in (0.5, 1.0):
        o.append(line(X0 - 3, MY(yv), X0 + 3, MY(yv), w=1.0)); o.append(text(X0 - 8, MY(yv) + 4, f"{yv:g}", size=10, anchor="end", fill="var(--muted)"))
    o.append(line(X0, MY(1), X1, MY(1), stroke="var(--muted)", w=0.7, dash="2 4"))
    f = np.linspace(0.05, 300, 6000) * 1e6
    l, c, Z0, RL, C = 3.0, 3e8, 50.0, 50.0, 10e-12
    x = 2 * PI * f * l / c
    H1 = np.abs(RL / (RL + 1j * Z0 * np.tan(x)))
    H3 = np.abs(RL / (RL + 1 / (1j * 2 * PI * f * C) + 1j * Z0 * np.tan(x)))
    o.append(poly(f / 1e6, H1, MX, MY, stroke=CV, w=2.2))
    o.append(poly(f / 1e6, H3, MX, MY, stroke=CI, w=2.0, dash="6 4"))
    o.append(line(80, 240, 110, 240, stroke=CV, w=2.2)); o.append(text(116, 244, "stub + 50 Ω  (Example 1)", size=11.5, anchor="start"))
    o.append(line(330, 240, 360, 240, stroke=CI, w=2.0, dash="6 4")); o.append(text(366, 244, "stub + 10 pF + 50 Ω  (Example 3)", size=11.5, anchor="start"))
    o.append(svg_close())
    figure("res-filter", "".join(o),
           "Amplitude response of the notes' two filters, a 3 m shorted air line (Z₀ = 50 Ω) in series with a 50 Ω load. Without the capacitor the response is |cos(2πfℓ/c)|: "
           "full transmission at the stub's series resonances (0, 50, 100 MHz, …) and none at its parallel resonances (25, 75, 125 MHz, …). "
           "The series capacitor moves the peaks up and blocks DC, and leaves the nulls where they were.")


def _line_box(o, X0, X1, Yt, Yb, lab):
    o.append(line(X0, Yt, X1, Yt, stroke=CV, w=3.2)); o.append(line(X0, Yb, X1, Yb, stroke=CV, w=3.2))
    o.append(text((X0 + X1) / 2, (Yt + Yb) / 2 + 4, "Z₀", size=12.5))
    o.append(line(X1, Yt, X1 + 18, Yt, w=1.4)); o.append(line(X1, Yb, X1 + 18, Yb, w=1.4))
    o.append(rect(X1 + 11, Yt + 10, 14, Yb - Yt - 20, sw=1.4))
    o.append(text(X1 + 34, (Yt + Yb) / 2 + 4, _sub("Z", "L"), size=12.5, anchor="start"))
    o.append(line(X0, Yb + 20, X1, Yb + 20, w=0.9, arrow=True, small=True)); o.append(line(X1, Yb + 20, X0, Yb + 20, w=0.9, arrow=True, small=True))
    o.append(text((X0 + X1) / 2, Yb + 36, lab, size=12))
    o.append(circle(X0, Yt, 3, fill="currentColor")); o.append(circle(X0, Yb, 3, fill="currentColor"))
    o.append(text(X0 - 8, (Yt + Yb) / 2 + 4, "in", size=11, anchor="end", fill="var(--muted)"))


def fig_transformers():
    W, H = 660, 210
    o = [svg_open(W, H)]
    _line_box(o, 60, 230, 40, 96, "ℓ = λ/2")
    Zi, ZL, Vi, VL, Ii, IL = (_sub(a, b) for a in "ZVI" for b in ("in", "L"))
    for k, s in enumerate((f"{Zi} = {ZL}", f"{Vi} = −{VL}", f"{Ii} = −{IL}")):
        o.append(text(160, 158 + 17 * k, s, size=12.5))
    _line_box(o, 390, 560, 40, 96, "ℓ = λ/4")
    for k, s in enumerate((f"{Zi} {ZL} = Z₀²", f"{IL} = −j {Vi} / Z₀", f"{VL} = −j Z₀ {Ii}")):
        o.append(text(490, 158 + 17 * k, s, size=12.5))
    o.append(svg_close())
    figure("res-transformers", "".join(o),
           "The two special lengths. A half-wave section repeats its load and flips the sign of voltage and current. "
           "A quarter-wave section inverts the load about Z₀ and fixes the load current from the input voltage alone, whatever the load is.")


if __name__ == "__main__":
    fig_modes(); fig_reactance(); fig_filter(); fig_transformers()
