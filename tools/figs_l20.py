#!/usr/bin/env python3
"""Lecture 20 figures (poy-*) for the ECE 329 notes: Poynting's theorem and monochromatic waves.

Same helpers and conventions as figs.py (plotting helpers from figs_l18.py / figs_l19.py).
Running this module writes /home/claude/work/figs/<name>.html.
Every plotted curve is computed from its formula with numpy. Arrow directions are fixed by explicit cross
products in the screen frame (X right, Y up, Z out of the screen); digest8/verify_L20.py section O repeats them:
  resistive wire: physics z (the wire axis) -> X.  Above the wire rho_hat = +Y, phi_hat = z x rho_hat = X x Y = +Z (odot);
                  S = E x H = X x Z = -Y (down, into the wire).  Below: phi_hat = X x (-Y) = -Z (otimes), S = X x (-Z) = +Y (up).
  worked problem icon: physics x -> X (right), z -> Y (up), so y = z x x -> Y x X = -Z (into the page).
                  E = +z (up) on both sides; H = -y (odot) for x > 0 and +y (otimes) for x < 0;
                  S = Y x Z = +X for x > 0 and Y x (-Z) = -X for x < 0: away from the sheet.
  odot = out of the page, otimes = into the page.
"""
from figs import *
from figs import _odot, _otimes, _sub, _tint, _zigzag
from figs_l18 import lin, poly, haxis
from figs_l19 import vaxis, blabels

ETA0 = 376.730313668

def halo(svg_text, width=4):
    """give a <text> element a background-coloured outline so it stays readable on top of curves"""
    return svg_text.replace("<text ", f'<text paint-order="stroke" stroke="var(--paper)" stroke-width="{width}" stroke-linejoin="round" ', 1)

def ellipse(cx, cy, rx, ry, fill="none", fop=None, stroke="currentColor", w=1.6, dash=None):
    fo = f' fill-opacity="{fop}"' if fop is not None else ""
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<ellipse cx="{cx:.1f}" cy="{cy:.1f}" rx="{rx:.1f}" ry="{ry:.1f}" fill="{fill}"{fo} '
            f'stroke="{stroke}" stroke-width="{w}"{d}/>')

def out_arrow(cx, cy, rx, ry, th, inside=6, outside=30, **kw):
    """arrow crossing an ellipse boundary along its outward normal at parameter angle th (screen coords, y down)"""
    bx, by = cx + rx * math.cos(th), cy + ry * math.sin(th)
    nx, ny = math.cos(th) / rx, math.sin(th) / ry
    n = math.hypot(nx, ny); nx, ny = nx / n, ny / n
    return arrow(bx - inside * nx, by - inside * ny, bx + outside * nx, by + outside * ny, **kw), (bx + (outside + 10) * nx, by + (outside + 10) * ny)

# ------------------------------------------------------------------------------------------------ 1. the two ledgers
def fig_poy_energy_ledger():
    W, H = 640, 372
    o = [svg_open(W, H)]
    o.append(line(320, 34, 320, 316, stroke="var(--muted)", w=1, dash="3 4"))
    cy, rx, ry = 138, 100, 64
    arrows_th = (-2.55, -1.05, -0.15, 0.95, 2.25, 3.25)      # outward arrows, none at the bottom centre
    # ---------------- left: charge
    cx = 160
    o.append(text(cx, 24, "Charge (Lecture 16)", size=13.5, weight=600))
    o.append(ellipse(cx, cy, rx, ry, fill="var(--accent)", fop=0.10))
    rng = np.random.default_rng(7)
    k = 0
    while k < 12:
        u, v = rng.uniform(-1, 1, 2)
        if 0.10 < u * u + v * v < 0.62 and not (abs(u) < 0.32 and abs(v) < 0.42):
            o.append(circle(cx + 0.92 * rx * u, cy + 0.92 * ry * v, 3.2, fill="currentColor", stroke="none")); k += 1
    o.append(text(cx, cy + 6, "ρ", size=17, math=True, weight=700, fill="var(--accent)"))
    for th in arrows_th:
        a, (lx, ly) = out_arrow(cx, cy, rx, ry, th, stroke="var(--accent)", w=2.2)
        o.append(a)
    a, (lx, ly) = out_arrow(cx, cy, rx, ry, -0.15, stroke="var(--accent)", w=2.2)
    o.append(text(lx + 2, ly - 8, "J", size=14, math=True, weight=700, fill="var(--accent)", anchor="start"))
    o.append(text(cx, 254, "dQ/dt = −∮ J · dA", size=13))
    o.append(text(cx, 274, "∂ρ/∂t + ∇ · J = 0", size=13))
    o.append(text(cx, 298, "no source term: charge is", size=11.5, fill="var(--muted)"))
    o.append(text(cx, 313, "never created or destroyed", size=11.5, fill="var(--muted)"))
    # ---------------- right: energy
    cx = 480
    o.append(text(cx, 24, "Electromagnetic energy (Lecture 20)", size=13.5, weight=600))
    o.append(ellipse(cx, cy, rx, ry, fill="var(--accent2)", fop=0.12))
    o.append(text(cx, cy - 26, "w = ½εE² + ½μH²", size=12, fill="var(--accent2)", weight=700))
    for th in arrows_th:
        a, (lx, ly) = out_arrow(cx, cy, rx, ry, th, stroke="var(--accent2)", w=2.2)
        o.append(a)
    a, (lx, ly) = out_arrow(cx, cy, rx, ry, -0.15, stroke="var(--accent2)", w=2.2)
    o.append(text(lx + 2, ly - 8, "S", size=14, math=True, weight=700, fill="var(--accent2)", anchor="start"))
    # a resistor (sink) and a source inside
    o.append(_zigzag(cx - 74, cy - 2, cx - 22, cy - 2, n=6, amp=6, color="var(--hi)", w=1.8))
    o.append(text(cx - 48, cy + 20, "J·E &gt; 0", size=11.5, fill="var(--hi)", weight=600))
    o.append(text(cx - 48, cy + 34, "sink (heat)", size=10.5, fill="var(--hi)"))
    bxx = cx + 32
    o.append(line(bxx - 6, cy - 15, bxx - 6, cy + 11, stroke="currentColor", w=2.2))
    o.append(line(bxx + 4, cy - 8, bxx + 4, cy + 4, stroke="currentColor", w=3.4))
    o.append(line(bxx - 22, cy - 2, bxx - 6, cy - 2, w=1.4)); o.append(line(bxx + 4, cy - 2, bxx + 20, cy - 2, w=1.4))
    o.append(text(bxx, cy + 26, "J·E &lt; 0", size=11.5, weight=600))
    o.append(text(bxx, cy + 40, "source", size=10.5))
    o.append(text(cx, 254, "dW/dt = −∮ S · dA − ∫ J·E dV", size=13))
    o.append(text(cx, 274, "∂w/∂t + ∇ · S = −J·E", size=13))
    o.append(text(cx, 298, "extra term: energy can change form", size=11.5, fill="var(--muted)"))
    o.append(text(cx, 313, "(heat, motion, chemistry)", size=11.5, fill="var(--muted)"))
    o.append(text(W / 2, 352, "density ρ ↔ w,   flux density J ↔ S,   and J·E is the exchange with the rest of the world", size=12, weight=600))
    o.append(svg_close())
    figure("poy-energy-ledger", "".join(o),
           "<strong>Two ledgers kept the same way.</strong> Left: the continuity equation of Lecture 16. The charge inside a "
           "volume changes only by current crossing its surface, because charge is never created or destroyed. Right: "
           "Poynting's theorem. The electromagnetic energy stored in a volume (density w) changes by energy flowing out "
           "through its surface (flux density <b>S</b> = <b>E</b> × <b>H</b>) <em>and</em> by energy exchanged with the "
           "charges inside, at the rate <b>J</b>·<b>E</b> per cubic metre. That second term has no twin on the left, "
           "because field energy can turn into other forms. Where <b>J</b>·<b>E</b> &gt; 0 (a resistor) the field loses "
           "energy, as heat. Where <b>J</b>·<b>E</b> &lt; 0 (a battery, an antenna current, the radiating sheet of "
           "Lecture 19) the current is driven against <b>E</b> and feeds energy into the field.")

# ------------------------------------------------------------------------------------------------ 2. resistive wire
def fig_poy_resistive_wire():
    W, H = 640, 360
    o = [svg_open(W, H)]
    o.append(text(20, 22, "1  A wire carrying steady current, seen from the side", size=12.5, anchor="start", weight=600))
    X0, X1, Yc, R = 70, 360, 176, 24
    o.append(_tint(X0, Yc - R, X1 - X0, 2 * R, "var(--hi)", op=0.10))
    o.append(line(X0, Yc - R, X1, Yc - R, w=1.6)); o.append(line(X0, Yc + R, X1, Yc + R, w=1.6))
    o.append(ellipse(X0, Yc, 8, R, w=1.4)); o.append(ellipse(X1, Yc, 8, R, w=1.4, dash="3 3"))
    # current in from the left
    o.append(arrow(X0 - 52, Yc, X0 - 12, Yc, stroke="currentColor", w=2.2))
    o.append(text(X0 - 44, Yc - 8, "I", size=14, math=True, weight=700))
    # E inside, along +z (to the right)
    for xx in (110, 200, 290):
        o.append(arrow(xx, Yc, xx + 42, Yc, stroke="var(--accent)", w=2.2))
    o.append(text(X1 + 14, Yc + 5, "E = J/σ", size=12.5, weight=700, fill="var(--accent)", anchor="start"))
    # H: above the wire out of the page (odot), below into the page (otimes)
    #   phi_hat = z x rho_hat: X x Y = +Z above; X x (-Y) = -Z below
    for xx in (110, 210, 300):
        o.append(_odot(xx, Yc - R - 20, r=7, color="var(--accent2)"))
        o.append(_otimes(xx, Yc + R + 20, r=7, color="var(--accent2)"))
    o.append(text(330, Yc - R - 16, "H ⊙", size=12, anchor="start", fill="var(--accent2)", weight=700))
    o.append(text(330, Yc + R + 24, "H ⊗", size=12, anchor="start", fill="var(--accent2)", weight=700))
    # S = E x H: above X x Z = -Y (down into the wire); below X x (-Z) = +Y (up into the wire)
    for xx in (160, 260):
        o.append(arrow(xx, Yc - R - 66, xx, Yc - R - 4, stroke="currentColor", w=2.8))
        o.append(arrow(xx, Yc + R + 66, xx, Yc + R + 4, stroke="currentColor", w=2.8))
    o.append(text(170, Yc - R - 54, "S = E × H", size=12.5, anchor="start", weight=700))
    o.append(text(170, Yc + R + 62, "S = E × H", size=12.5, anchor="start", weight=700))
    o.append(text(215, 312, "|S| = E H(a) = (I/σπa²)(I/2πa) on the surface", size=11.5))
    o.append(text(215, 330, "× side area 2πaℓ  =  I²ℓ/(σπa²)  =  I²R", size=11.5, weight=600))
    o.append(text(215, 348, "No S along the axis inside: nothing enters through the ends.", size=11, fill="var(--muted)"))
    # ---- panel 2: power crossing the cylinder of radius rho, P(rho)/I^2R = (rho/a)^2
    o.append(text(408, 22, "2  Power still flowing inward", size=12.5, anchor="start", weight=600))
    o.append(text(408, 38, "through the cylinder of radius ρ", size=12.5, anchor="start", weight=600))
    MR = lin(0, 1.0, 466, 602); MP = lin(0, 1.0, 270, 90)
    rr = np.linspace(0, 1, 201)
    o.append(_tint(MR(0), MP(1), MR(1) - MR(0), MP(0) - MP(1), "var(--hi)", op=0.06))
    o.append(poly(rr, rr ** 2, MR, MP, stroke="var(--hi)", w=2.6))
    o.append(haxis(459, 614, MP(0), "ρ/a", [(0, "0"), (0.5, "0.5"), (1, "1")], MR))
    o.append(vaxis(MR(0), MP(0) + 4, MP(1.12), "P(ρ) / I²R", [(0, "0"), (0.25, "0.25"), (0.5, "0.5"), (1, "1")], MP))
    o.append(line(MR(0), MP(1), MR(1), MP(1), stroke="var(--muted)", w=1, dash="4 3"))
    o.append(text(MR(0.47), MP(0.62), "(ρ/a)²", size=12.5, fill="var(--hi)", weight=700, anchor="end"))
    o.append(text(540, 300, "= the heat made inside radius ρ:", size=11, fill="var(--muted)"))
    o.append(text(540, 315, "energy is absorbed as it flows in", size=11, fill="var(--muted)"))
    o.append(svg_close())
    figure("poy-resistive-wire", "".join(o),
           "<strong>Where the heat in a resistor comes from.</strong> A straight wire of radius a and conductivity σ "
           "carries a steady current I to the right. Inside, <b>E</b> = <b>J</b>/σ points along the wire, and so does its "
           "tangential partner just outside the surface (tangential <b>E</b> is continuous). <b>H</b> circles the wire: out "
           "of the page above it (⊙), into the page below (⊗). Panel 1: on both sides <b>S</b> = <b>E</b> × <b>H</b> points "
           "<em>into</em> the wire, perpendicular to the current. Multiplying |<b>S</b>| by the side area gives exactly "
           "I²R. Panel 2, computed from S<sub>ρ</sub> = −E H<sub>φ</sub>(ρ) with H<sub>φ</sub> = Iρ/2πa²: the power that "
           "still crosses a cylinder of radius ρ falls as (ρ/a)², which is the heat generated inside that cylinder. The "
           "energy is delivered by the fields around the wire and absorbed on its way to the axis. It does not travel "
           "along the copper.")

# ------------------------------------------------------------------------------------------------ 3. the notes' sheet
def legend_line(o, x, y, color, dash=None, label="", sub=None, w=2.4):
    o.append(line(x, y, x + 26, y, stroke=color, w=w, dash=dash))
    o.append(text(x + 32, y + 4, label, size=11.5, anchor="start", fill=color, weight=600))
    if sub:
        o.append(text(x + 32, y + 19, sub, size=10.5, anchor="start", fill="var(--muted)"))

def fig_poy_sheet_energy():
    W, H = 640, 540
    o = [svg_open(W, H)]
    # ---- panel 1: snapshot at t = 0, S_z(z) = +-eta0 cos^2(beta z), z in wavelengths
    o.append(text(20, 22, "1  Snapshot at t = 0:  " + _sub("S", "z") + "(z) = ±η₀ cos²(βz),  z in wavelengths", size=12.5, anchor="start", weight=600))
    o.append(text(20, 40, "dashed: the time averages, +η₀/2 on the right and −η₀/2 on the left", size=11, anchor="start", fill="var(--muted)"))
    MZ = lin(-2.15, 2.15, 70, 610); Y1 = 166; A1 = 88
    MY1 = lambda s_: Y1 - A1 * s_
    zt = [(k, ("−" if k < 0 else "") + (f"{abs(k)}λ" if k else "0")) for k in (-2, -1, 0, 1, 2)]
    o.append(line(MZ(0), MY1(1.2), MZ(0), MY1(-1.2), stroke="var(--hi)", w=2, dash="4 3"))
    o.append(haxis(58, 622, Y1, "z", zt, MZ, tick_labels=False)); o.append(blabels(zt, MZ, MY1(-1.2) + 16))
    zp = np.linspace(0, 2.15, 1200)
    o.append(poly(zp, np.cos(2 * np.pi * zp) ** 2, MZ, MY1, stroke="var(--accent)", w=2.4))
    o.append(poly(-zp, -np.cos(2 * np.pi * zp) ** 2, MZ, MY1, stroke="var(--accent)", w=2.4))
    o.append(line(MZ(0.02), MY1(0.5), MZ(2.15), MY1(0.5), stroke="var(--accent)", w=1.4, dash="6 4"))
    o.append(line(MZ(-2.15), MY1(-0.5), MZ(-0.02), MY1(-0.5), stroke="var(--accent)", w=1.4, dash="6 4"))
    for sv, lab in ((1, "+η₀"), (0.5, "+η₀/2"), (-0.5, "−η₀/2"), (-1, "−η₀")):
        o.append(line(MZ(-2.15) - 3, MY1(sv), MZ(-2.15) + 3, MY1(sv), w=1))
        o.append(text(MZ(-2.15) - 6, MY1(sv) + 4, lab, size=10.5, anchor="end", fill="var(--muted)"))
    # motion arrows in the empty corners (above the right humps, below the left ones)
    o.append(arrow(MZ(1.45), MY1(1.15), MZ(1.95), MY1(1.15), stroke="currentColor", w=1.8, small=True))
    o.append(halo(text(MZ(1.4), MY1(1.15) + 4, "humps move out at c", size=10.5, anchor="end")))
    o.append(arrow(MZ(-1.45), MY1(-1.15), MZ(-1.95), MY1(-1.15), stroke="currentColor", w=1.8, small=True))
    o.append(halo(text(MZ(-1.4), MY1(-1.15) + 4, "humps move out at c", size=10.5, anchor="start")))
    o.append(halo(text(MZ(0) + 6, MY1(-1.12), "sheet", size=10.5, anchor="start", fill="var(--hi)")))
    # ---- panel 2: the record at the sheet over two periods (legend on the right)
    o.append(text(20, 306, "2  At the sheet, against time: injected = what leaves through the two faces", size=12.5, anchor="start", weight=600))
    MT = lin(0, 2.0, 80, 440); Y2 = 506; A2 = 82
    MY2 = lambda p_: Y2 - A2 * p_
    tt = np.linspace(0, 2, 801)
    tticks = [(0, "0"), (0.5, "T/2"), (1, "T"), (1.5, "3T/2"), (2, "2T")]
    o.append(haxis(70, 456, Y2, "t", tticks, MT))
    o.append(vaxis(MT(0), Y2, MY2(2.2), "W/m²", [(0, "0"), (0.5, "η₀/2"), (1, "η₀"), (2, "2η₀")], MY2))
    o.append(poly(tt, 2 * np.cos(2 * np.pi * tt) ** 2, MT, MY2, stroke="var(--hi)", w=2.4))
    o.append(poly(tt, np.cos(2 * np.pi * tt) ** 2, MT, MY2, stroke="var(--accent)", w=2.4))
    o.append(line(MT(0), MY2(1), MT(2), MY2(1), stroke="var(--hi)", w=1.4, dash="6 4"))
    o.append(line(MT(0), MY2(0.5), MT(2), MY2(0.5), stroke="var(--accent)", w=1.4, dash="6 4"))
    lx = 474
    legend_line(o, lx, 352, "var(--hi)", label="−" + _sub("J", "s") + "·E, injected", sub="= 2η₀ cos²ωt")
    legend_line(o, lx, 396, "var(--accent)", label="|S| at each face", sub="= η₀ cos²ωt")
    legend_line(o, lx, 440, "var(--hi)", dash="6 4", label="average η₀", w=1.4)
    legend_line(o, lx, 466, "var(--accent)", dash="6 4", label="average η₀/2", w=1.4)
    o.append(svg_close())
    figure("poy-sheet-energy", "".join(o),
           "<strong>The notes' Example 1: J<sub>s</sub> = x̂ 2cos(ωt) A/m on z = 0 in vacuum.</strong> Panel 1 is a "
           "snapshot of the Poynting vector, computed from S<sub>z</sub> = ±η₀cos²(ωt ∓ βz). It is positive (pointing "
           "+z) on the right and negative (pointing −z) on the left, so energy flows away from the sheet on both sides and "
           "never back. Its humps are half a wavelength apart and travel outward at c. Each side averages η₀/2 ≈ 188 W/m² "
           "(the dashed lines). Panel 2 is a record at the sheet. The current gives up −<b>J</b><sub>s</sub>·<b>E</b> = "
           "2η₀cos²ωt watts per square metre (red), and at every instant that is exactly the sum of what crosses the two "
           "faces, η₀cos²ωt each (blue). Both oscillate at 2ω, twice the source frequency. Averaged, η₀ goes in and "
           "η₀/2 leaves on each side.")

# ------------------------------------------------------------------------------------------------ 4. time averages
def fig_poy_time_average():
    W, H = 640, 540
    o = [svg_open(W, H)]
    o.append(text(20, 22, "1  cos²(ωt) = ½ + ½ cos(2ωt): a constant plus a ripple at 2ω", size=12.5, anchor="start", weight=600))
    MT = lin(0, 2.0, 80, 450); Y1 = 196; A1 = 140
    MY1 = lambda p_: Y1 - A1 * p_
    tt = np.linspace(0, 2, 801); cc = np.cos(2 * np.pi * tt) ** 2
    up = np.maximum(cc, 0.5); dn = np.minimum(cc, 0.5)
    def band(ys, color):
        sel = slice(None, None, 4)                      # 201 points are plenty for a fill
        pts = [(MT(t), MY1(y)) for t, y in zip(tt[sel], ys[sel])] + [(MT(t), MY1(0.5)) for t in (tt[-1], tt[0])]
        return '<path d="M' + " L".join(f"{X:.1f},{Yv:.1f}" for X, Yv in pts) + f' Z" fill="{color}" fill-opacity="0.20" stroke="none"/>'
    o.append(band(up, "var(--accent)")); o.append(band(dn, "var(--accent2)"))
    tticks = [(0, "0"), (0.5, "T/2"), (1, "T"), (1.5, "3T/2"), (2, "2T")]
    o.append(haxis(70, 466, Y1, "t", tticks, MT))
    o.append(vaxis(MT(0), Y1, MY1(1.1), "", [(0, "0"), (0.5, "½"), (1, "1")], MY1))
    o.append(poly(tt, cc, MT, MY1, stroke="currentColor", w=2.4))
    o.append(line(MT(0), MY1(0.5), MT(2), MY1(0.5), stroke="var(--hi)", w=1.8, dash="6 4"))
    lx = 486
    legend_line(o, lx, 64, "currentColor", label="cos²(ωt)")
    legend_line(o, lx, 92, "var(--hi)", dash="6 4", label="average ½", w=1.8)
    o.append(_tint(lx, 112, 26, 12, "var(--accent)", op=0.30)); o.append(text(lx + 32, 122, "above ½", size=11.5, anchor="start", fill="var(--accent)", weight=600))
    o.append(_tint(lx, 134, 26, 12, "var(--accent2)", op=0.30)); o.append(text(lx + 32, 144, "below ½", size=11.5, anchor="start", fill="var(--accent2)", weight=600))
    o.append(text(lx, 168, "equal areas: the ripple", size=10.5, anchor="start", fill="var(--muted)"))
    o.append(text(lx, 182, "averages to zero", size=10.5, anchor="start", fill="var(--muted)"))
    # ---- panel 2: travelling vs standing, at a fixed point
    o.append(text(20, 256, "2  S at z = λ/8: one travelling wave vs two equal waves in opposite directions", size=12.5, anchor="start", weight=600))
    Y2 = 382; A2 = 84
    MY2 = lambda p_: Y2 - A2 * p_
    o.append(haxis(70, 466, Y2, "t", tticks, MT, tick_labels=False))
    o.append(blabels(tticks, MT, MY2(-1.1) + 16))
    o.append(vaxis(MT(0), MY2(-1.1), MY2(1.14), "", [(-1, "−1"), (0, "0"), (0.5, "½"), (1, "1")], MY2))
    o.append(text(MT(0) - 34, MY2(1.3), "S in units of E₀²/η", size=11, anchor="start"))
    # one wave at z = lambda/8: cos^2(wt - beta z) = cos^2(wt - pi/4); standing wave there: sin 2wt sin(pi/2) = sin 2wt
    o.append(poly(tt, np.cos(2 * np.pi * tt - np.pi / 4) ** 2, MT, MY2, stroke="var(--accent)", w=2.4))
    o.append(poly(tt, np.sin(4 * np.pi * tt), MT, MY2, stroke="var(--hi)", w=2.4))
    o.append(line(MT(0), MY2(0.5), MT(2), MY2(0.5), stroke="var(--accent)", w=1.3, dash="6 4"))
    legend_line(o, lx, 300, "var(--accent)", label="one wave", sub="cos²(ωt − π/4) ≥ 0")
    legend_line(o, lx, 340, "var(--accent)", dash="6 4", label="its average, ½", w=1.3)
    legend_line(o, lx, 372, "var(--hi)", label="standing wave", sub="sin 2ωt (sin 2βz = 1)")
    o.append(text(lx + 32, 406, "average 0", size=10.5, anchor="start", fill="var(--muted)"))
    o.append(text(W / 2, 528, "Same peak flux, same period of the ripple; only the travelling wave carries energy on average.", size=11.5, weight=600))
    o.append(svg_close())
    figure("poy-time-average", "".join(o),
           "<strong>Why the time average of a cosine squared is ½, and when an average hides a lot.</strong> Panel 1: "
           "cos²(ωt) equals ½ plus a ripple ½cos(2ωt). Over any whole period the ripple contributes nothing, because the "
           "area above ½ (blue) equals the area below it (green). So ⟨cos²(ωt + φ)⟩ = ½ for every phase φ, including "
           "φ = ∓βz. Panel 2 compares two Poynting vectors at the same point, z = λ/8. A single travelling wave (blue) pushes energy "
           "forward at every instant, in pulses at 2ω, with average E₀²/2η. Two equal waves travelling in opposite "
           "directions (a standing wave, red) give S = (E₀²/η) sin 2ωt sin 2βz. Here energy moves forward "
           "and back each cycle and the average is exactly zero at every z, even though the instantaneous S is not.")

# ------------------------------------------------------------------------------------------------ 5. worked problem
def fig_poy_problem_energy():
    W, H = 640, 500
    o = [svg_open(W, H)]
    # problem data (exam constants: eps0 = 1e-9/36pi, mu0 = 4pi 1e-7)
    eps0x = 1e-9 / (36 * np.pi); epsr = 2.25; eps = epsr * eps0x
    v = 2e8; eta = 80 * np.pi; f = 2e6; om = 2 * np.pi * f; beta = om / v; J0 = 3.0
    E0 = eta * J0 / 2; t1 = 3e-6
    wpk = eps * E0 ** 2 * 1e6                          # micro J/m^3 (w = eps E^2 for a one-way wave)
    o.append(text(20, 22, "1  Energy density w(x) at t = 3 µs  (" + _sub("w", "e") + " = " + _sub("w", "m") + ", so w = εE²)", size=12.5, anchor="start", weight=600))
    o.append(text(20, 40, "dashed: the cycle average ⟨w⟩ = εE₀²/2 = 1.41 µJ/m³, half the peak", size=11, anchor="start", fill="var(--muted)"))
    MX = lin(-820, 820, 66, 610); Y1 = 206; A1 = 136 / wpk
    MY1 = lambda w: Y1 - A1 * w
    xt = [(k, f"{k}".replace("-", "−")) for k in (-600, -300, 0, 300, 600)]
    o.append(line(MX(0), MY1(1.14 * wpk), MX(0), Y1, stroke="var(--hi)", w=2, dash="4 3"))
    o.append(haxis(56, 622, Y1, "x", xt, MX, tick_labels=False)); o.append(blabels(xt, MX, Y1 + 16))
    o.append(text(624, Y1 + 16, "m", size=10.5, anchor="start", fill="var(--muted)"))
    xr = np.linspace(0, 820, 3000)
    wr = np.where(xr < v * t1, wpk * np.cos(om * t1 - beta * xr) ** 2, 0.0)
    xr2 = np.concatenate([xr[xr < 600], [600, 600], xr[xr > 600]])
    wr2 = np.concatenate([wr[xr < 600], [wpk, 0], wr[xr > 600]])
    o.append(poly(xr2, wr2, MX, MY1, stroke="var(--accent2)", w=1.8))
    o.append(poly(-xr2, wr2, MX, MY1, stroke="var(--accent2)", w=1.8))
    o.append(line(MX(-600), MY1(wpk / 2), MX(600), MY1(wpk / 2), stroke="var(--hi)", w=1.5, dash="6 4"))
    o.append(vaxis(MX(-820), Y1, MY1(1.12 * wpk), "µJ/m³", [(0, "0"), (wpk / 2, f"{wpk/2:.2f}"), (wpk, f"{wpk:.2f}")], MY1))
    o.append(text(MX(600) + 6, MY1(0.86 * wpk), "front", size=10.5, fill="var(--accent2)", anchor="start"))
    o.append(text(MX(600) + 6, MY1(0.86 * wpk) + 13, "x = vt", size=10.5, fill="var(--accent2)", anchor="start"))
    o.append(text(MX(-600) - 6, MY1(0.86 * wpk), "front", size=10.5, fill="var(--accent2)", anchor="end"))
    o.append(text(MX(-600) - 6, MY1(0.86 * wpk) + 13, "x = −vt", size=10.5, fill="var(--accent2)", anchor="end"))
    o.append(halo(text(MX(0) + 5, MY1(1.1 * wpk), "sheet", size=10.5, anchor="start", fill="var(--hi)")))
    # ---- panel 2: energy delivered vs stored, per m^2 of sheet
    o.append(text(20, 268, "2  Energy per m² of sheet, 0 to 3 µs", size=12.5, anchor="start", weight=600))
    MT = lin(0, 3.0, 82, 380); Y2 = 452; A2 = 160 / 1.75
    MY2 = lambda wj: Y2 - A2 * wj        # mJ/m^2
    tt = np.linspace(0, 3e-6, 1201)
    Winj = (eta * J0 ** 2 / 2) * (tt / 2 + np.sin(2 * om * tt) / (4 * om)) * 1e3
    tticks = [(k, f"{k}") for k in range(0, 4)]
    o.append(haxis(72, 392, Y2, "t", tticks, MT, tick_labels=False)); o.append(blabels(tticks, MT, Y2 + 16))
    o.append(text(394, Y2 + 16, "µs", size=10.5, anchor="start", fill="var(--muted)"))
    o.append(vaxis(MT(0), Y2, MY2(1.85), "mJ/m²", [(0, "0"), (0.5, "0.5"), (1.0, "1.0"), (1.5, "1.5")], MY2))
    o.append(poly(tt * 1e6, Winj, MT, MY2, stroke="var(--hi)", w=2.4))
    # stored energy at sample times, by integrating w(x) over |x| < v t (both sides)
    for ts in np.linspace(0.25e-6, 3e-6, 12):
        n = 6000; xs = (np.arange(n) + 0.5) / n * v * ts
        Wst = 2 * np.mean(eps * (E0 * np.cos(om * ts - beta * xs)) ** 2) * v * ts * 1e3
        o.append(circle(MT(ts * 1e6), MY2(Wst), 3.6, fill="var(--accent2)", stroke="none"))
    o.append(text(MT(0.15), MY2(1.62), "line: delivered by the current, ∫(−" + _sub("J", "s") + "·E) dt", size=11, anchor="start", fill="var(--hi)", weight=600))
    o.append(text(MT(0.15), MY2(1.45), "dots: stored in |x| &lt; vt, ∫w dx", size=11, anchor="start", fill="var(--accent2)", weight=600))
    o.append(text(MT(3.0), MY2(1.70) - 8, "1.70", size=10.5, anchor="middle", fill="var(--hi)"))
    # ---- geometry icon (problem frame: x right, z up, y into the page)
    gx, gy = 520, 360
    o.append(text(gx, 268, "fields next to the sheet", size=11.5, weight=600))
    o.append(text(gx, 283, "while cos ωt &gt; 0", size=11.5, weight=600))
    o.append(line(gx, gy - 52, gx, gy + 52, stroke="var(--hi)", w=2.4))
    for yy in (-40, 4):
        o.append(arrow(gx, gy + yy, gx, gy + yy + 30, stroke="var(--hi)", w=1.6, small=True))   # Js = -z: down
    o.append(text(gx, gy + 66, _sub("J", "s") + " along −ẑ", size=10.5, fill="var(--hi)", anchor="middle"))
    for sgn in (1, -1):
        o.append(arrow(gx + sgn * 30, gy + 22, gx + sgn * 30, gy - 22, stroke="var(--accent)", w=2.2, small=True))  # E = +z: up
        o.append(text(gx + sgn * 30, gy + 38, "E", size=11, fill="var(--accent)", weight=700))
    o.append(_odot(gx + 58, gy, r=6, color="var(--accent2)")); o.append(_otimes(gx - 58, gy, r=6, color="var(--accent2)"))
    o.append(text(gx + 58, gy + 22, "H", size=11, fill="var(--accent2)", weight=700))
    o.append(text(gx - 58, gy + 22, "H", size=11, fill="var(--accent2)", weight=700))
    o.append(arrow(gx + 70, gy - 30, gx + 104, gy - 30, stroke="currentColor", w=2.2, small=True))
    o.append(arrow(gx - 70, gy - 30, gx - 104, gy - 30, stroke="currentColor", w=2.2, small=True))
    o.append(text(gx + 87, gy - 38, "S", size=11, weight=700)); o.append(text(gx - 87, gy - 38, "S", size=11, weight=700))
    ax, ay = 458, 468
    o.append(arrow(ax, ay, ax + 26, ay, stroke="currentColor", w=1.3, small=True)); o.append(text(ax + 30, ay + 4, "x", size=11, anchor="start", math=True))
    o.append(arrow(ax, ay, ax, ay - 26, stroke="currentColor", w=1.3, small=True)); o.append(text(ax + 5, ay - 22, "z", size=11, anchor="start", math=True))
    o.append(_otimes(ax, ay, r=4.5)); o.append(text(ax - 8, ay + 4, "y", size=11, anchor="end", math=True))
    o.append(text(ax + 44, ay + 4, "(y into the page)", size=10, anchor="start", fill="var(--muted)"))
    o.append(svg_close())
    figure("poy-problem-energy", "".join(o),
           "<strong>The worked problem's energy ledger at t = 3 µs.</strong> A sheet on x = 0 carries "
           "<b>J</b><sub>s</sub> = −ẑ 3u(t)cos(ωt) A/m at 2 MHz in a dielectric with ε<sub>r</sub> = 2.25 (v = 200 m/µs, "
           "λ = 100 m). Panel 1, computed from w = εE<sup>2</sup> with E = (ηJ<sub>0</sub>/2)cos(ωt − β|x|): the field fills "
           "|x| &lt; 600 m, twelve humps of energy density per side, and nothing has reached beyond the fronts. Averaged "
           "over a cycle the density is 1.41 µJ/m³ (dashed). Panel 2: the energy the current has given up, the integral "
           "of −<b>J</b><sub>s</sub>·<b>E</b> (line), and the energy found by integrating w over the region the waves have "
           "reached (dots) are the same at every instant: 1.70 mJ per square metre of sheet at 3 µs. That is Poynting's "
           "theorem in integral form for a box whose faces lie beyond the fronts, where <b>S</b> = 0. The icon shows "
           "the directions while cos ωt &gt; 0, when the current points down (−ẑ): <b>E</b> up (+ẑ, opposite to the current) on both sides, "
           "<b>H</b> = −ŷ (⊙) on the right and +ŷ (⊗) on the left, and <b>S</b> = <b>E</b> × <b>H</b> pointing away from "
           "the sheet.")

if __name__ == "__main__":
    for fn in (fig_poy_energy_ledger, fig_poy_resistive_wire, fig_poy_sheet_energy, fig_poy_time_average, fig_poy_problem_energy):
        fn()
