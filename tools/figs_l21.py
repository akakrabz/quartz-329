#!/usr/bin/env python3
"""Lecture 21 figures (phas-*) for the ECE 329 notes: monochromatic waves and phasor notation.

Same helpers and conventions as figs.py (and the plotting helpers of figs_l18.py).
Running this module writes /home/claude/work/figs/<name>.html.
Every curve is computed from its formula with numpy (no hand-drawn shapes).
Screen frame for every figure: X right, Y up. SVG y grows downward, so a point at math angle phi on a circle
of radius r is drawn at (cx + r cos phi, cy - r sin phi). The complex plane is drawn with Re to the right and
Im up, so a counterclockwise turn on the page is a positive angle: multiplying by j turns an arrow by +90 deg
(z_hat x (Re, Im, 0) in the screen frame) and by -j by -90 deg (checked in digest8/verify_L21.py, section F,
with np.cross). These figures contain no field vectors in 3-D space, so no odot/otimes symbol is needed.
"""
from figs import *
from figs import _odot, _otimes, _sub, _tint
from figs_l18 import lin, poly

PI = np.pi
SUBP = '<tspan baseline-shift="sub" style="font-size:9px">p</tspan>'

def _sup(base, s, size=9):
    """base text with a superscript s (SVG tspan)"""
    return f'{base}<tspan baseline-shift="super" style="font-size:{size}px">{s}</tspan>'

def _legend_line(x, y, color, dash=None, w=2.2, length=26):
    return line(x, y, x + length, y, stroke=color, w=w, dash=dash)

def _ticks(ticks, MX, Yaxis, Ylab, size=10.5):
    """tick marks on a horizontal axis at Yaxis, with labels on their own baseline Ylab (clear of the curves)"""
    s = []
    for tv, tl in ticks:
        X = MX(tv)
        s.append(line(X, Yaxis - 3, X, Yaxis + 3, w=1.1))
        s.append(text(X, Ylab, tl, size=size, fill="var(--muted)"))
    return "".join(s)

def _span(X0, X1, Y, label, Xlab, Ylab, color="currentColor", size=12):
    """double-headed span marker from X0 to X1 at height Y, label at (Xlab, Ylab)"""
    Xm = (X0 + X1) / 2
    return (arrow(Xm, Y, X0, Y, stroke=color, w=1.3, small=True) + arrow(Xm, Y, X1, Y, stroke=color, w=1.3, small=True) +
            text(Xlab, Ylab, label, size=size, weight=600, fill=color))

# ------------------------------------------------------------------------------------------------ 1. snapshot and record
def fig_phas_snapshot_record():
    W, H = 640, 432
    o = [svg_open(W, H)]
    # ---- panel 1: records E(0,t) = cos(wt) and E(lambda/4,t) = cos(wt - pi/2); t in units of T
    MT = lin(0, 2.6, 90, 590); Y1 = 112; A1 = 38
    MY1 = lambda e: Y1 - A1 * e
    o.append(text(20, 22, "1  At one place, against time: the record repeats every period T", size=12.5, anchor="start", weight=600))
    o.append(_legend_line(420, 41, "var(--accent)")); o.append(text(450, 45, "z = 0", size=11, anchor="start"))
    o.append(_legend_line(506, 41, "var(--accent2)", dash="6 4")); o.append(text(536, 45, "z = λ/4", size=11, anchor="start"))
    o.append(line(80, Y1, 600, Y1, w=1.3, arrow=True)); o.append(text(604, Y1 + 4, "t", size=12.5, anchor="start", math=True))
    t = np.linspace(0, 2.6, 900)
    o.append(poly(t, np.cos(2 * PI * t), MT, MY1, stroke="var(--accent)", w=2.4))
    o.append(poly(t, np.cos(2 * PI * t - PI / 2), MT, MY1, stroke="var(--accent2)", w=2.2, dash="6 4"))
    # period marker between the solid crests at t = 0 and t = T
    yT = MY1(1) - 12
    o.append(line(MT(1), MY1(1) - 4, MT(1), yT - 4, w=0.9, dash="2 2"))
    o.append(line(MT(0), MY1(1) - 4, MT(0), yT - 4, w=0.9, dash="2 2"))
    o.append(_span(MT(0), MT(1), yT, "T = 2π/ω", MT(0.5), yT - 5))
    # delay marker between the troughs at t = 1.5T (z = 0) and t = 1.75T (z = lambda/4)
    yD = MY1(-1) + 11
    o.append(arrow(MT(1.5), yD, MT(1.75), yD, stroke="var(--accent2)", w=1.6, small=True))
    o.append(text(MT(1.75) + 7, yD + 4, "a delay of T/4 at z = λ/4", size=11, anchor="start", fill="var(--accent2)"))
    tt = [(0, "0"), (0.5, "T/2"), (1, "T"), (1.5, "3T/2"), (2, "2T"), (2.5, "5T/2")]
    o.append(_ticks(tt, MT, Y1, MY1(-1) + 30))
    # ---- panel 2: snapshots E(z,0) = cos(beta z) and E(z,T/8) = cos(pi/4 - beta z); z in units of lambda
    MZ = lin(0, 2.6, 90, 590); Y2 = 300; A2 = 38
    MY2 = lambda e: Y2 - A2 * e
    o.append(text(20, 212, "2  At one instant, against position: the snapshot repeats every wavelength λ", size=12.5, anchor="start", weight=600))
    o.append(_legend_line(420, 229, "var(--accent)")); o.append(text(450, 233, "t = 0", size=11, anchor="start"))
    o.append(_legend_line(506, 229, "var(--hi)", dash="6 4")); o.append(text(536, 233, "t = T/8", size=11, anchor="start"))
    o.append(line(80, Y2, 600, Y2, w=1.3, arrow=True)); o.append(text(604, Y2 + 4, "z", size=12.5, anchor="start", math=True))
    z = np.linspace(0, 2.6, 900)
    o.append(poly(z, np.cos(2 * PI * z), MZ, MY2, stroke="var(--accent)", w=2.4))
    o.append(poly(z, np.cos(PI / 4 - 2 * PI * z), MZ, MY2, stroke="var(--hi)", w=2.2, dash="6 4"))
    # wavelength marker between the solid crests at z = 0 and z = lambda
    yL = MY2(1) - 12
    o.append(line(MZ(0), MY2(1) - 4, MZ(0), yL - 4, w=0.9, dash="2 2"))
    o.append(line(MZ(1), MY2(1) - 4, MZ(1), yL - 4, w=0.9, dash="2 2"))
    o.append(_span(MZ(0), MZ(1), yL, "λ = 2π/β", MZ(0.5), yL - 5))
    # shift marker: the solid crest at z = 2 lambda is at z = 2.125 lambda one eighth of a period later (+z)
    o.append(line(MZ(2), MY2(1) - 4, MZ(2), yL - 4, w=0.9, dash="2 2"))
    o.append(arrow(MZ(2.0), yL, MZ(2.125), yL, stroke="var(--hi)", w=1.6, small=True))
    o.append(text(MZ(2.125) + 7, yL + 4, "moved λ/8 = v" + SUBP + "T/8", size=11, anchor="start", fill="var(--hi)"))
    zt = [(0, "0"), (0.5, "λ/2"), (1, "λ"), (1.5, "3λ/2"), (2, "2λ"), (2.5, "5λ/2")]
    o.append(_ticks(zt, MZ, Y2, MY2(-1) + 18))
    # footer
    o.append(text(W / 2, 384, "One cosine, two periodicities: ω counts radians per second at one place, β radians per metre at one instant.", size=11.2))
    o.append(text(W / 2, 406, "In one period every crest moves one wavelength:  " + _sub("v", "p") + " = λ/T = ω/β = λf", size=11.5, weight=600))
    o.append(svg_close())
    figure("phas-snapshot-record", "".join(o),
           "<strong>A monochromatic wave E = cos(ωt − βz), seen two ways.</strong> Panel 1 holds the position fixed. "
           "At z = 0 the field is cos ωt (solid), which repeats every period T = 2π/ω. A quarter wavelength downstream it is "
           "the same cosine delayed by T/4 (dashed), because the wave needs (λ/4)/v<sub>p</sub> = T/4 to get there. Panel 2 holds "
           "the time fixed. At t = 0 the field is cos βz (solid), which repeats every wavelength λ = 2π/β. An eighth of a period "
           "later the whole pattern has slid λ/8 toward +z (dashed). This is the notes' page-3 picture: in a time t the crests "
           "move (ω/β)t, so the phase velocity is v<sub>p</sub> = ω/β = λ/T = λf. β plays in space the role ω plays in time: "
           "it is a spatial frequency.")

# ------------------------------------------------------------------------------------------------ 2. dispersion diagram
def fig_phas_dispersion_diagram():
    W, H = 640, 430
    o = [svg_open(W, H)]
    # omega in units of omega_p, beta in units of omega_p / c
    MB = lin(0, 3.2, 80, 420); MW = lin(0, 3.2, 386, 56)
    o.append(text(20, 22, "The notes' dispersion relations on one ω–β diagram", size=12.5, anchor="start", weight=600))
    # band below omega_p: no travelling wave in the plasma
    o.append(_tint(MB(0), MW(1), MB(3.2) - MB(0), MW(0) - MW(1), "var(--hi)", op=0.10))
    o.append(text(MB(2.3), MW(0.45), "ω &lt; " + _sub("ω", "p") + ": no travelling wave", size=11, fill="var(--hi)"))
    o.append(text(MB(2.3), MW(0.45) + 15, "in the plasma (β imaginary)", size=11, fill="var(--hi)"))
    # axes
    o.append(line(MB(0), MW(0), MB(3.28), MW(0), w=1.3, arrow=True)); o.append(text(MB(3.28) + 4, MW(0) + 4, "β", size=13, anchor="start", math=True))
    o.append(line(MB(0), MW(0), MB(0), MW(3.3), w=1.3, arrow=True)); o.append(text(MB(0) + 9, MW(3.3) + 9, "ω", size=13, anchor="start", math=True))
    for k in (1, 2, 3):
        o.append(line(MB(k), MW(0) - 3, MB(k), MW(0) + 3, w=1.1))
        o.append(text(MB(k), MW(0) + 16, f"{k}" + (" ω" + SUBP + "/c" if k == 1 else ""), size=10.5, fill="var(--muted)"))
        o.append(line(MB(0) - 3, MW(k), MB(0) + 3, MW(k), w=1.1))
        o.append(text(MB(0) - 7, MW(k) + 4, (_sub("ω", "p") if k == 1 else f"{k}" + _sub("ω", "p")), size=10.5, anchor="end", fill="var(--muted)"))
    o.append(line(MB(0), MW(1), MB(3.2), MW(1), stroke="var(--muted)", w=0.9, dash="3 3"))
    b = np.linspace(0, 3.2, 400)
    o.append(poly(b, b, MB, MW, stroke="currentColor", w=1.6, dash="7 5"))              # vacuum: omega = c beta
    o.append(poly(b, b / 2, MB, MW, stroke="var(--accent2)", w=2.4))                     # eps_r = 4: omega = c beta / 2
    bp = np.linspace(0, np.sqrt(3.2 ** 2 - 1), 600)
    o.append(poly(bp, np.sqrt(1 + bp ** 2), MB, MW, stroke="var(--hi)", w=2.6))          # plasma
    # point P at omega = 1.5 omega_p: chord (v_p) and tangent (v_g = beta c^2 / omega)
    wP = 1.5; bP = np.sqrt(wP ** 2 - 1); vg = bP / wP
    o.append(line(MB(0), MW(0), MB(bP * 1.5), MW(wP * 1.5), stroke="var(--accent)", w=1.8, dash="2 3"))
    bt = np.array([bP - 0.75, bP + 0.85])
    o.append(line(MB(bt[0]), MW(wP + vg * (bt[0] - bP)), MB(bt[1]), MW(wP + vg * (bt[1] - bP)), stroke="var(--accent)", w=1.8))
    o.append(circle(MB(bP), MW(wP), 4.5, fill="var(--accent)", stroke="none"))
    o.append(text(MB(bP) + 9, MW(wP) + 17, "P", size=12, anchor="start", weight=700, fill="var(--accent)"))
    # legend and notes (right)
    lx, ly = 446, 58
    o.append(_legend_line(lx, ly, "currentColor", dash="7 5", w=1.6)); o.append(text(lx + 32, ly + 4, "vacuum: ω = cβ", size=11, anchor="start"))
    o.append(_legend_line(lx, ly + 24, "var(--accent2)", w=2.4)); o.append(text(lx + 32, ly + 28, "dielectric " + _sub("ε", "r") + " = 4: ω = cβ/2", size=11, anchor="start"))
    o.append(_legend_line(lx, ly + 48, "var(--hi)", w=2.6)); o.append(text(lx + 32, ly + 52, "plasma: " + _sup("ω", "2") + " = " + _sup(_sub("ω", "p"), "2") + " + " + _sup("c", "2") + _sup("β", "2"), size=11, anchor="start"))
    o.append(_legend_line(lx, ly + 72, "var(--accent)", dash="2 3", w=1.8)); o.append(text(lx + 32, ly + 76, "chord to P: slope " + _sub("v", "p") + " = ω/β", size=11, anchor="start"))
    o.append(_legend_line(lx, ly + 96, "var(--accent)", w=1.8)); o.append(text(lx + 32, ly + 100, "tangent at P: slope " + _sub("v", "g"), size=11, anchor="start"))
    o.append(text(lx, ly + 134, "At P, ω = 1.5" + _sub("ω", "p") + ":", size=11, anchor="start", weight=600))
    o.append(text(lx, ly + 152, _sub("v", "p") + " = 1.34c (steeper than light)", size=11, anchor="start"))
    o.append(text(lx, ly + 170, _sub("v", "g") + " = dω/dβ = 0.75c", size=11, anchor="start"))
    o.append(text(lx, ly + 188, _sub("v", "p") + _sub("v", "g") + " = " + _sup("c", "2"), size=11, anchor="start"))
    o.append(text(lx, ly + 222, "Lines through the origin are", size=11, anchor="start", fill="var(--muted)"))
    o.append(text(lx, ly + 238, "non-dispersive: " + _sub("v", "p") + " = " + _sub("v", "g") + " at every ω.", size=11, anchor="start", fill="var(--muted)"))
    o.append(text(lx, ly + 260, "Sound in a gas is one too, with", size=11, anchor="start", fill="var(--muted)"))
    o.append(text(lx, ly + 276, "slope about " + _sup("10", "−6") + "c; at this scale", size=11, anchor="start", fill="var(--muted)"))
    o.append(text(lx, ly + 292, "it lies on the β axis.", size=11, anchor="start", fill="var(--muted)"))
    o.append(svg_close())
    figure("phas-dispersion-diagram", "".join(o),
           "<strong>The notes' dispersion relations on one ω–β diagram</strong> (ω in units of the plasma frequency ω<sub>p</sub>, "
           "β in units of ω<sub>p</sub>/c). A TEM wave in vacuum or in a dielectric is a straight line through the origin, so "
           "ω/β is the same at every frequency: no dispersion, and pulses keep their shape. The collisionless plasma is the "
           "hyperbola ω² = ω<sub>p</sub>² + c²β². Below ω<sub>p</sub> (shaded) it has no real β, so no wave travels; above, it "
           "bends toward the light line. At any point the phase velocity ω/β is the slope of the chord from the origin, and "
           "for the plasma that chord is always steeper than the light line (v<sub>p</sub> &gt; c). The group velocity "
           "dω/dβ, the speed of a signal's envelope (Lecture 24), is the slope of the tangent, always less steep (v<sub>g</sub> &lt; c). "
           "At P, ω = 1.5ω<sub>p</sub>: v<sub>p</sub> = 1.34c and v<sub>g</sub> = 0.75c, with v<sub>p</sub>v<sub>g</sub> = c².")

# ------------------------------------------------------------------------------------------------ 3. rotating arrow
def fig_phas_rotating_arrow():
    W, H = 640, 410
    o = [svg_open(W, H)]
    th = PI / 6                     # phase of the phasor A e^{j theta}; |A| = 1 is drawn as R pixels
    cx, cy, R = 165, 200, 100
    P = lambda r, ang: (cx + r * np.cos(ang), cy - r * np.sin(ang))   # math angle -> screen (Y up)
    o.append(text(20, 22, "1  The complex plane: the arrow Ã" + _sup("e", "jωt") + " turns counterclockwise", size=12.5, anchor="start", weight=600))
    # axes
    o.append(line(cx - 135, cy, cx + 140, cy, w=1.3, arrow=True)); o.append(text(cx + 143, cy + 4, "Re", size=12, anchor="start"))
    o.append(line(cx, cy + 135, cx, cy - 140, w=1.3, arrow=True)); o.append(text(cx + 6, cy - 132, "Im", size=12, anchor="start"))
    o.append(circle(cx, cy, R, stroke="var(--muted)", w=1.0, dash="4 4"))
    # 8 positions at t = kT/8: angle theta + k pi/4 (counterclockwise = increasing angle)
    for k in range(8):
        ang = th + k * PI / 4
        X, Y = P(R, ang)
        o.append(circle(X, Y, 3.6, fill="var(--accent)", stroke="none"))
        Xl, Yl = P(R + 13, ang)
        o.append(text(Xl, Yl + 4, str(k), size=10.5, fill="var(--accent)", weight=700))
    # rotation sense: arc inside the circle, counterclockwise
    a0, a1, rr = th + 0.35, th + 1.25, R - 26
    arc = [P(rr, a) for a in np.linspace(a0, a1, 30)]
    o.append(path("M" + " L".join(f"{X:.1f},{Y:.1f}" for X, Y in arc), stroke="var(--accent)", w=1.4, arrow=True))
    Xa, Ya = P(rr - 15, (a0 + a1) / 2)
    o.append(text(Xa, Ya + 4, "ω", size=12, fill="var(--accent)", math=True))
    # the phasor at t = 0 (position 0), and its shadow on the real axis
    X0, Y0 = P(R, th)
    o.append(line(X0, Y0, X0, cy, stroke="var(--accent)", w=1.2, dash="3 3"))
    o.append(line(cx, cy, X0, cy, stroke="var(--accent)", w=5, opacity=0.5))
    o.append(arrow(cx, cy, X0, Y0, stroke="var(--accent)", w=2.8))
    o.append(text(X0 + 20, Y0 + 18, "Ã = A" + _sup("e", "jθ"), size=12, anchor="start", fill="var(--accent)", weight=700))
    o.append(text(cx + 42, cy + 16, "A cos θ", size=10.5, anchor="start", fill="var(--accent)"))
    # -j A: turned by -90 deg, i.e. the arrow a quarter period EARLIER in its turn = a signal a quarter period LATER
    Xm, Ym = P(R, th - PI / 2)
    o.append(arrow(cx, cy, Xm, Ym, stroke="var(--hi)", w=2.2))
    Xt, Yt = P(R + 34, th - PI / 2)
    o.append(text(Xt, Yt + 4, "−jÃ", size=12, fill="var(--hi)", weight=700))
    # +j A: turned by +90 deg
    Xp, Yp = P(R, th + PI / 2)
    o.append(arrow(cx, cy, Xp, Yp, stroke="var(--accent2)", w=2.2))
    Xt, Yt = P(R + 32, th + PI / 2)
    o.append(text(Xt, Yt + 4, "jÃ", size=12, fill="var(--accent2)", weight=700))
    o.append(text(20, 360, "−jÃ (turned −90°): a sine, a quarter period later", size=11, anchor="start", fill="var(--hi)"))
    o.append(text(20, 376, "jÃ (turned +90°): d/dt gives jωÃ, a quarter period earlier", size=11, anchor="start", fill="var(--accent2)"))
    # ---- panel 2: the shadow against time
    MT = lin(0, 2 * PI, 355, 605); MA = lambda a: cy - 95 * a
    o.append(text(345, 58, "2  Its shadow on the Re axis, against time", size=12.5, anchor="start", weight=600))
    o.append(line(345, cy, 618, cy, w=1.3, arrow=True)); o.append(text(621, cy + 4, "ωt", size=12, anchor="start", math=True))
    o.append(line(MT(0), cy + 108, MT(0), cy - 112, w=1.3, arrow=True))
    for tv, tl in ((PI, "π"), (2 * PI, "2π")):
        o.append(line(MT(tv), cy - 3, MT(tv), cy + 3, w=1.1)); o.append(text(MT(tv) + 8, cy + 16, tl, size=10.5, fill="var(--muted)"))
    for av, al in ((1, "A"), (-1, "−A")):
        o.append(line(MT(0) - 3, MA(av), MT(0) + 3, MA(av), w=1.1)); o.append(text(MT(0) - 6, MA(av) + 4, al, size=10.5, anchor="end", fill="var(--muted)"))
    wt = np.linspace(0, 2 * PI, 600)
    o.append(poly(wt, np.cos(wt + th - PI / 2), MT, MA, stroke="var(--hi)", w=1.8, dash="6 4"))
    o.append(poly(wt, np.cos(wt + th), MT, MA, stroke="var(--accent)", w=2.6))
    for k in range(8):
        tk = k * PI / 4; ak = np.cos(tk + th)
        o.append(circle(MT(tk), MA(ak), 3.6, fill="var(--accent)", stroke="none"))
        falling = np.sin(tk + th) > 0          # a(t) decreasing at this instant: label above-right, else below-right
        o.append(text(MT(tk) + (13 if k == 0 else 8), MA(ak) + (-7 if falling else 15), str(k), size=10.5, fill="var(--accent)", weight=700))
    o.append(text(605, cy - 116, "a(t) = A cos(ωt + θ)", size=11, anchor="end", fill="var(--accent)", weight=600))
    o.append(text(605, cy + 124, "dashed: A sin(ωt + θ), the shadow of −jÃ", size=11, anchor="end", fill="var(--hi)"))
    o.append(text(W / 2, H - 8, "Dot k is the arrow at t = kT/8 (drawn with θ = 30°); the same k marks a(t) at that instant.", size=11.5))
    o.append(svg_close())
    figure("phas-rotating-arrow", "".join(o),
           "<strong>A phasor is the starting position of a turning arrow.</strong> The complex number Ãe<sup>jωt</sup> = "
           "Ae<sup>j(ωt+θ)</sup> runs counterclockwise around a circle of radius A, once per period (dots 0–7 are eighths of a "
           "period). Its shadow on the real axis is a(t) = A cos(ωt + θ), plotted on the right with the same numbering. So the "
           "phasor Ã = Ae<sup>jθ</sup> (the arrow at t = 0) holds the amplitude and the phase, and the agreed frequency ω does the rest. "
           "Multiplying by −j turns the arrow back a quarter turn, to where Ã was a quarter period earlier, so its shadow (dashed) "
           "peaks a quarter period later: that is why a sine has phasor −jA. Multiplying by j turns it forward a quarter turn: "
           "the derivative of a(t) peaks a quarter period earlier, which is why d/dt becomes jω.")

# ------------------------------------------------------------------------------------------------ 4. direction trap
def _dial_row(o, MZ, Ydial, Ysnap, sign, color, title, ytitle):
    """dials of exp(sign*j*beta*z) at z = k lambda/8, and the snapshots Re{exp(j(wt + sign*beta*z))} at t = 0 and T/8"""
    o.append(text(20, ytitle, title, size=12.5, anchor="start", weight=600))
    r = 14
    for k in range(9):
        zk = k / 8; X = MZ(zk)
        phi = sign * 2 * PI * zk                   # phase of the phasor at z (math angle, counterclockwise positive)
        o.append(circle(X, Ydial, r, stroke="var(--muted)", w=1.0))
        o.append(line(X - r - 3, Ydial, X + r + 3, Ydial, stroke="var(--muted)", w=0.6))
        o.append(arrow(X, Ydial, X + (r - 1) * np.cos(phi), Ydial - (r - 1) * np.sin(phi), stroke=color, w=2.0, small=True))
    for k, lab in ((0, "0"), (2, "λ/4"), (4, "λ/2"), (6, "3λ/4"), (8, "λ")):
        o.append(text(MZ(k / 8), Ydial + r + 14, lab, size=10, fill="var(--muted)"))
    A = 30
    MY = lambda e: Ysnap - A * e
    o.append(_legend_line(80, Ysnap - A - 15, "currentColor", w=2.0, length=22)); o.append(text(106, Ysnap - A - 11, "t = 0", size=10.5, anchor="start"))
    o.append(_legend_line(150, Ysnap - A - 15, color, dash="6 4", w=2.2, length=22)); o.append(text(176, Ysnap - A - 11, "t = T/8", size=10.5, anchor="start"))
    o.append(line(MZ(-0.05), Ysnap, MZ(1.22), Ysnap, w=1.2, arrow=True)); o.append(text(MZ(1.22) + 4, Ysnap + 4, "z", size=12, anchor="start", math=True))
    z = np.linspace(-0.05, 1.18, 700)
    o.append(poly(z, np.cos(sign * 2 * PI * z), MZ, MY, stroke="currentColor", w=2.0))
    o.append(poly(z, np.cos(PI / 4 + sign * 2 * PI * z), MZ, MY, stroke=color, w=2.2, dash="6 4"))
    # the t = 0 crest at z = lambda is found at z = lambda - sign*lambda/8 one eighth of a period later
    z1 = 1 - sign / 8
    o.append(line(MZ(1), MY(1) - 3, MZ(1), MY(1) - 14, w=0.9, dash="2 2"))
    o.append(arrow(MZ(1), MY(1) - 9, MZ(z1), MY(1) - 9, stroke=color, w=1.8, small=True))
    o.append(text(MZ((1 + z1) / 2), MY(1) - 17, "toward " + ("+z" if sign < 0 else "−z"), size=11, fill=color, weight=600))

def fig_phas_direction_trap():
    W, H = 640, 470
    o = [svg_open(W, H)]
    MZ = lin(0, 1.25, 70, 560)
    _dial_row(o, MZ, 62, 166, -1, "var(--accent)", "A   " + _sup("e", "−jβz") + ":  the phase falls along +z, so the wave travels toward +z", 24)
    _dial_row(o, MZ, 276, 380, +1, "var(--hi)", "B   " + _sup("e", "+jβz") + ":  the phase rises along +z, so the wave travels toward −z", 238)
    o.append(text(W / 2, H - 26, "A minus sign in the exponent means travel toward plus.", size=12, weight=600))
    o.append(text(W / 2, H - 8, "Check by restoring the time factor:  " + _sup("e", "−jβz") + _sup("e", "jωt") + " = " + _sup("e", "j(ωt − βz)") + ";  opposite signs  →  +z.", size=11.5))
    o.append(svg_close())
    figure("phas-direction-trap", "".join(o),
           "<strong>Reading the direction of travel from a phasor.</strong> Each dial is the phasor at one position, z = 0, λ/8, …, λ. "
           "In row A, e<sup>−jβz</sup>, the arrow turns clockwise as z grows: the phase falls by β per metre, so each point "
           "repeats, later, what the point behind it did. Below the dials, the snapshot at t = 0 (solid; at each z it is the "
           "real part of the dial) and an eighth of a period later (dashed): the crest has moved λ/8 toward +z. In row B, "
           "e<sup>+jβz</sup>, the arrows turn counterclockwise, the phase lags toward −z, and the crest moves λ/8 toward −z. "
           "The phasor has no t in it, so the time-domain rule (opposite signs of the t and z terms mean +z) applies only "
           "after multiplying by e<sup>jωt</sup>.")

# ------------------------------------------------------------------------------------------------ 5. time average of a product
def fig_phas_time_average():
    W, H = 640, 448
    o = [svg_open(W, H)]
    B = 0.8
    MT = lin(0, 2, 80, 596)
    o.append(text(20, 22, "a(t) = cos ωt and b(t) = 0.8 cos(ωt − φ): their product is a constant plus a part at 2ω", size=12.5, anchor="start", weight=600))
    lx = 80
    o.append(_legend_line(lx, 42, "var(--accent)", w=1.4)); o.append(text(lx + 30, 46, "a(t)", size=11, anchor="start"))
    o.append(_legend_line(lx + 80, 42, "var(--accent2)", dash="5 3", w=1.4)); o.append(text(lx + 110, 46, "b(t)", size=11, anchor="start"))
    o.append(_legend_line(lx + 160, 42, "var(--hi)", w=2.6)); o.append(text(lx + 190, 46, "a(t) b(t)", size=11, anchor="start"))
    o.append(_legend_line(lx + 265, 42, "currentColor", dash="2 3", w=1.6)); o.append(text(lx + 295, 46, "⟨ab⟩ = ½Re{ÃB̃*} = 0.4 cos φ", size=11, anchor="start"))
    t = np.linspace(0, 2, 900)
    a = np.cos(2 * PI * t)
    rows = [(0, "φ = 0, in phase:  ⟨ab⟩ = 0.40, and the product never goes negative",
             "like E and H of one wave in a lossless medium"),
            (60, "φ = 60°:  ⟨ab⟩ = 0.40 cos 60° = 0.20",
             "for part of each period the product is negative"),
            (90, "φ = 90°, in quadrature:  ⟨ab⟩ = 0",
             "like a collisionless plasma's current against its E: energy in, then back out")]
    for i, (phd, t1, t2) in enumerate(rows):
        Yc = 126 + i * 124; A = 34
        MY = lambda e, Yc=Yc: Yc - A * e
        o.append(text(20, Yc - 58, t1, size=12, anchor="start", weight=600))
        o.append(text(20, Yc - 43, t2, size=10.5, anchor="start", fill="var(--muted)"))
        o.append(line(70, Yc, 606, Yc, w=1.1, arrow=True)); o.append(text(609, Yc + 4, "t", size=11.5, anchor="start", math=True))
        b = B * np.cos(2 * PI * t - np.radians(phd))
        o.append(poly(t, a, MT, MY, stroke="var(--accent)", w=1.4))
        o.append(poly(t, b, MT, MY, stroke="var(--accent2)", w=1.4, dash="5 3"))
        o.append(poly(t, a * b, MT, MY, stroke="var(--hi)", w=2.6))
        avg = 0.5 * B * np.cos(np.radians(phd))
        o.append(line(MT(0), MY(avg), MT(2), MY(avg), stroke="currentColor", w=1.6, dash="2 3"))
        o.append(text(66, MY(avg) + 4, f"{avg:.2f}" if avg > 1e-9 else "0", size=10.5, anchor="end", weight=600))
        for tv, tl in ((1, "T"), (2, "2T")):
            o.append(line(MT(tv), Yc - 3, MT(tv), Yc + 3, w=1.0)); o.append(text(MT(tv), Yc + A + 13, tl, size=10, fill="var(--muted)"))
    o.append(svg_close())
    figure("phas-time-average", "".join(o),
           "<strong>Why the time average of a product is ½Re{ÃB̃*}.</strong> Two sinusoids at the same frequency, with "
           "phasors Ã = 1 and B̃ = 0.8e<sup>−jφ</sup>. Their product (thick) is a constant plus a sinusoid at 2ω, so over a "
           "period only the constant survives, and it is ½AB cos φ, which depends only on the phase difference. In phase "
           "(top) the product never goes negative: this is E and H of a single wave in a lossless medium, whose power always "
           "flows forward. At 60° the flow reverses for part of each period. In quadrature (bottom) the product spends as much "
           "time negative as positive and averages to zero. That is the electron current of a collisionless plasma, 90° behind its "
           "E field: it takes energy from the wave and gives it back each period, so it absorbs nothing on average.")

if __name__ == "__main__":
    for fn in (fig_phas_snapshot_record, fig_phas_dispersion_diagram, fig_phas_rotating_arrow,
               fig_phas_direction_trap, fig_phas_time_average):
        fn()
