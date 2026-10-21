#!/usr/bin/env python3
"""Lecture 25 figures (refl-*) for the ECE 329 notes: wave reflection and transmission at normal incidence.

Same helpers and conventions as figs.py (plot helpers from figs_l18.py).
Running this module writes /home/claude/work/figs/<name>.html.
Every curve is computed from its formula with numpy.
Screen frame: X right, Y up, Z out of the screen. In refl-setup the physics axes map as
z (travel) -> screen right, x (E) -> screen up, y (H) -> out of the screen (odot), a proper rotation:
right x up = out  <->  z x x = y. Directions checked in digest9/verify_L25.py, section H, with np.cross.
"""
from figs import *
from figs import _odot, _otimes, _sub, _tint
from figs_l18 import lin, poly

PI = np.pi
GAM, TAU, N2 = -0.2, 0.8, 1.5          # notes' Example 1: vacuum onto eps = 9/4 eps0


def _legend_line(x, y, color, dash=None, w=2.2, length=26):
    return line(x, y, x + length, y, stroke=color, w=w, dash=dash)


# ------------------------------------------------------------------------------------------------ 1. the setup
def _wave_icon(o, X, Y, hsym, k_dir, elab, hlab, klab):
    """E arrow up (x-hat), H symbol (odot = +y, otimes = -y), travel arrow (k_dir = +1 right, -1 left)"""
    o.append(arrow(X, Y + 22, X, Y - 26, stroke="var(--accent)", w=2.4))           # E along +x: screen up
    o.append(text(X - 8, Y - 30, elab, size=12, anchor="end", fill="var(--accent)"))
    hx = X + 26
    o.append((_odot if hsym == "odot" else _otimes)(hx, Y, r=7, color="var(--accent2)"))
    o.append(text(hx + 12, Y - 10, hlab, size=12, anchor="start", fill="var(--accent2)"))
    kx0 = X + 4 if k_dir > 0 else X + 58
    o.append(arrow(kx0, Y + 34, kx0 + 54 * k_dir, Y + 34, stroke="currentColor", w=2.0, small=True))
    o.append(text(X + 31, Y + 52, klab, size=11.5, fill="var(--muted)"))


def fig_refl_setup():
    W, H = 640, 300
    o = [svg_open(W, H)]
    XI = 330
    o.append(_tint(XI, 30, 290, 230, "var(--muted)", op=0.13))
    o.append(line(XI, 30, XI, 260, w=2.0))
    o.append(text(XI, 278, "z = 0", size=12))
    o.append(text(175, 22, "region 1 (z &lt; 0): " + _sub("μ", "1") + ", " + _sub("ε", "1") + ", " + _sub("σ", "1") + " = 0", size=12.5, weight=600))
    o.append(text(475, 22, "region 2 (z &gt; 0): " + _sub("μ", "2") + ", " + _sub("ε", "2") + ", " + _sub("σ", "2"), size=12.5, weight=600))
    # incident: x x y = +z ; reflected (drawn for real Gamma > 0): x x (-y) = -z ; transmitted: x x y = +z
    _wave_icon(o, 130, 90, "odot", +1, _sub("E", "i") + " ∝ " + _sub("E", "0"), _sub("H", "i"), "incident, +z")
    _wave_icon(o, 130, 190, "otimes", -1, _sub("E", "r") + " ∝ Γ" + _sub("E", "0"), _sub("H", "r") + " ∝ −Γ", "reflected, −z")
    _wave_icon(o, 430, 120, "odot", +1, _sub("E", "t") + " ∝ τ" + _sub("E", "0"), _sub("H", "t"), "transmitted, ∝ " + "e<tspan baseline-shift=\"super\" style=\"font-size:9px\">−γ₂z</tspan>")
    # normal from region 2 into region 1
    o.append(arrow(XI, 236, XI - 46, 236, stroke="var(--hi)", w=2.2, small=True))
    o.append(text(XI - 52, 240, "n̂ = −ẑ", size=12, anchor="end", fill="var(--hi)"))
    # axis triad (screen right = z, up = x, out = y)
    tx, ty = 470, 225
    o.append(arrow(tx, ty, tx + 40, ty, stroke="currentColor", w=1.4, small=True)); o.append(text(tx + 46, ty + 4, "z", size=12, anchor="start", math=True))
    o.append(arrow(tx, ty, tx, ty - 36, stroke="currentColor", w=1.4, small=True)); o.append(text(tx, ty - 42, "x", size=12, math=True))
    o.append(_odot(tx, ty, r=5)); o.append(text(tx - 9, ty + 16, "y (out)", size=11, anchor="end", math=False))
    o.append(svg_close())
    figure("refl-setup", "".join(o),
           "<strong>Normal incidence, drawn for a real Γ &gt; 0.</strong> Each wave has <b>E</b> along x̂ (up) and "
           "<b>H</b> along ±ŷ (⊙ out of the page, ⊗ in), with <b>E</b> × <b>H</b> along its travel. "
           "The reflected <b>H</b> carries −Γ. The normal n̂ points from region 2 into region 1.")


# ------------------------------------------------------------------------------------------------ 2. Gamma and tau
def fig_refl_gamma_tau():
    W, H = 640, 330
    o = [svg_open(W, H)]
    MXl = lin(-2, 2, 80, 600)                       # log10(eta2/eta1)
    MY = lin(-1.1, 2.1, 280, 40)
    o.append(text(20, 22, "Real impedances: Γ, τ and the reflected power fraction against " + _sub("η", "2") + "/" + _sub("η", "1"), size=12.5, anchor="start", weight=600))
    for yv in (-1, 0, 1, 2):
        o.append(line(MXl(-2), MY(yv), MXl(2), MY(yv), stroke="var(--muted)", w=0.8, dash="3 3" if yv else None))
        o.append(text(MXl(-2) - 8, MY(yv) + 4, f"{yv:+d}" if yv else "0", size=11, anchor="end", fill="var(--muted)"))
    for lv, lab in ((-2, "0.01"), (-1, "0.1"), (np.log10(2 / 3), "⅔"), (0, "1"), (np.log10(1.5), "1.5"), (1, "10"), (2, "100")):
        o.append(line(MXl(lv), MY(-1.1), MXl(lv), MY(-1.1) + 5, w=1.0))
        o.append(text(MXl(lv), MY(-1.1) + 18, lab, size=10.5, fill="var(--muted)"))
    o.append(text(MXl(2), MY(-1.1) + 36, _sub("η", "2") + "/" + _sub("η", "1") + " (log scale)", size=11.5, anchor="end"))
    lr = np.linspace(-2, 2, 801); r = 10 ** lr
    G = (r - 1) / (r + 1); T = 2 * r / (r + 1)
    o.append(poly(lr, G, MXl, MY, stroke="var(--accent)", w=2.6))
    o.append(poly(lr, T, MXl, MY, stroke="var(--accent2)", w=2.6))
    o.append(poly(lr, G ** 2, MXl, MY, stroke="var(--hi)", w=2.0, dash="6 4"))
    # markers: notes' Example 1 (2/3), matched (1), reverse direction glass -> air (1.5)
    for rv in (2 / 3, 1.0, 1.5):
        g = (rv - 1) / (rv + 1); t = 1 + g; X = MXl(np.log10(rv))
        o.append(circle(X, MY(g), 3.8, fill="var(--accent)", stroke="none"))
        o.append(circle(X, MY(t), 3.8, fill="var(--accent2)", stroke="none"))
    X23, X15 = MXl(np.log10(2 / 3)), MXl(np.log10(1.5))
    o.append(text(X23 + 8, MY(-0.2) + 18, "Γ = −0.2", size=10.5, anchor="start", fill="var(--accent)"))
    o.append(text(X23 - 10, MY(0.8) + 4, "τ = 0.8", size=10.5, anchor="end", fill="var(--accent2)"))
    o.append(text(X15 - 6, MY(0.2) - 7, "Γ = +0.2", size=10.5, anchor="end", fill="var(--accent)"))
    o.append(text(X15 - 6, MY(1.2) - 7, "τ = 1.2", size=10.5, anchor="end", fill="var(--accent2)"))
    o.append(text(MXl(-1.95), MY(0.55), _sub("η", "2") + " → 0:", size=10.5, anchor="start", fill="var(--muted)"))
    o.append(text(MXl(-1.95), MY(0.55) + 15, "Γ → −1, τ → 0", size=10.5, anchor="start", fill="var(--muted)"))
    o.append(text(MXl(1.95), MY(1.5), _sub("η", "2") + " ≫ " + _sub("η", "1") + ": Γ → +1, τ → 2", size=10.5, anchor="end", fill="var(--muted)"))
    lx, ly = 92, 64
    o.append(_legend_line(lx, ly, "var(--accent)", w=2.6)); o.append(text(lx + 32, ly + 4, "Γ", size=12, anchor="start"))
    o.append(_legend_line(lx, ly + 20, "var(--accent2)", w=2.6)); o.append(text(lx + 32, ly + 24, "τ = 1 + Γ", size=12, anchor="start"))
    o.append(_legend_line(lx, ly + 40, "var(--hi)", w=2.0, dash="6 4")); o.append(text(lx + 32, ly + 44, "power reflected, Γ²", size=12, anchor="start"))
    o.append(svg_close())
    figure("refl-gamma-tau", "".join(o),
           "<strong>Γ and τ for real η's.</strong> Γ is odd in log(η<sub>2</sub>/η<sub>1</sub>), so swapping the media flips its "
           "sign and keeps Γ². Dots: the notes' Example 1 (⅔), matched (1) and the reverse trip (1.5). "
           "η<sub>2</sub> → 0 is a perfect conductor. τ exceeds 1 whenever η<sub>2</sub> &gt; η<sub>1</sub>.")


# ------------------------------------------------------------------------------------------------ 3. snapshot at the interface
def fig_refl_interface_snapshot():
    W, H = 640, 380
    o = [svg_open(W, H)]
    wt = 0.3 * PI                                   # instant shown, omega t
    MZ = lin(-2.0, 1.5, 70, 590)                    # z in units of lambda_1
    b1 = 2 * PI; b2 = N2 * b1                       # beta in rad per lambda_1
    z1 = np.linspace(-2.0, 0, 700); z2 = np.linspace(0, 1.5, 600)
    panels = [
        ("E", 120, "a  " + _sub("E", "x") + "/" + _sub("E", "0"),
         np.cos(wt - b1 * z1), GAM * np.cos(wt + b1 * z1), TAU * np.cos(wt - b2 * z2)),
        ("H", 290, "b  " + _sub("η", "1") + _sub("H", "y") + "/" + _sub("E", "0"),
         np.cos(wt - b1 * z1), -GAM * np.cos(wt + b1 * z1), N2 * TAU * np.cos(wt - b2 * z2)),
    ]
    A = 52
    for key, Yc, title, inc, ref, tra in panels:
        MY = lambda v, Yc=Yc: Yc - A * v
        o.append(text(20, Yc - 70, title, size=12.5, anchor="start", weight=600))
        o.append(_tint(MZ(0), Yc - 68, MZ(1.5) - MZ(0), 136, "var(--muted)", op=0.13))
        o.append(line(MZ(-2.0), Yc, MZ(1.5) + 6, Yc, w=1.1, arrow=True)); o.append(text(MZ(1.5) + 12, Yc + 4, "z", size=12, anchor="start", math=True))
        o.append(line(MZ(0), Yc - 68, MZ(0), Yc + 68, w=1.6))
        o.append(poly(z1, inc, MZ, MY, stroke="var(--accent)", w=1.4, dash="6 4"))
        o.append(poly(z1, ref, MZ, MY, stroke="var(--accent2)", w=1.4, dash="2 3"))
        o.append(poly(z1, inc + ref, MZ, MY, stroke="currentColor", w=2.6))
        o.append(poly(z2, tra, MZ, MY, stroke="var(--hi)", w=2.6))
        v0 = (inc + ref)[-1]
        o.append(circle(MZ(0), MY(v0), 4.2, fill="var(--hi)", stroke="none"))
        for zv, zl in ((-2, "−2" + "λ₁"), (-1, "−λ₁"), (1, "λ₁")):
            o.append(line(MZ(zv), Yc - 3, MZ(zv), Yc + 3, w=1.0))
            o.append(text(MZ(zv), Yc + 66, zl, size=10, fill="var(--muted)"))
    lx, ly = 300, 30
    o.append(_legend_line(lx, ly - 4, "var(--accent)", dash="6 4", w=1.4, length=20)); o.append(text(lx + 24, ly, "incident", size=11, anchor="start"))
    o.append(_legend_line(lx + 82, ly - 4, "var(--accent2)", dash="2 3", w=1.4, length=20)); o.append(text(lx + 106, ly, "reflected", size=11, anchor="start"))
    o.append(_legend_line(lx + 170, ly - 4, "currentColor", w=2.6, length=20)); o.append(text(lx + 194, ly, "total", size=11, anchor="start"))
    o.append(_legend_line(lx + 236, ly - 4, "var(--hi)", w=2.6, length=20)); o.append(text(lx + 260, ly, "transmitted", size=11, anchor="start"))
    o.append(svg_close())
    figure("refl-interface-snapshot", "".join(o),
           "<strong>Notes' Example 1 at ωt = 0.3π</strong> (Γ = −1/5, τ = 4/5, β<sub>2</sub> = 1.5β<sub>1</sub>). "
           "Incident plus reflected (thick) meets the transmitted wave at z = 0 with no jump in <b>E</b> or <b>H</b>. "
           "Entering, <b>E</b> scales by τ = 0.8, <b>H</b> by 1 − Γ = 1.2.")


if __name__ == "__main__":
    for fn in (fig_refl_setup, fig_refl_gamma_tau, fig_refl_interface_snapshot):
        fn()
