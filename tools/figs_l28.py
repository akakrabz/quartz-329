#!/usr/bin/env python3
"""Lecture 28 figures (bounce-*) for the ECE 329 notes: distributed circuits and bounce diagrams.

Same helpers and conventions as figs.py (plot helpers from figs_l18.py).
Running this module writes /home/claude/work/figs/<name>.html.
Screen frame: X right, Y down on screen for SVG. In the bounce diagrams z runs to the right (generator at the left),
time runs downward, as in the notes. Every weight and every curve is computed here from the page's formulas;
digest10/verify_L28.py (section I) compares them with an FDTD run of the telegrapher's equations.
No vector directions appear: the only arrows are wave travel (+z right, -z left) and the current reference
(+z on the upper wire, return on the lower one).
"""
from figs import *
from figs import _odot, _otimes, _sub, _tint, _zigzag
from figs_l18 import lin, poly

Z0, RG, RL, V0 = 60.0, 180.0, 20.0, 12.0           # the page's example circuit
TAU_G = Z0 / (RG + Z0)
GAM_G = (RG - Z0) / (RG + Z0)
GAM_L = (RL - Z0) / (RL + Z0)


def example_weights(n=6):
    """voltage weights of the first n segments for f_i = V0 (step) or V0 delta (impulse)"""
    w, out = V0 * TAU_G, []
    for k in range(n):
        out.append(w)
        w *= GAM_L if k % 2 == 0 else GAM_G
    return out


def step_curves(tT, zs=(0.5, 1.0)):
    """V(z,t) for f_i = V0 u(t): running sum of crossed weights; t in units of T, z in units of l"""
    tT = np.asarray(tT, float)
    out = []
    for z in zs:
        V = np.zeros_like(tT)
        w = V0 * TAU_G
        for k in range(40):
            tk = (k + z) if k % 2 == 0 else (k + 1 - z)        # forward seg k: kT + z/v ; backward: (k+1)T - z/v
            V += w * (tT > tk)
            w *= GAM_L if k % 2 == 0 else GAM_G
        out.append(V)
    return out


def _sup(s, size=9):
    return f'<tspan baseline-shift="super" style="font-size:{size}px">{s}</tspan>'


def _w(tg=True, nL=0, ng=0, size=12):
    """symbolic weight tau_g Gamma_L^nL Gamma_g^ng as SVG text content"""
    s = "τ" + f'<tspan baseline-shift="sub" style="font-size:9px">g</tspan>'
    if nL:
        s += "Γ" + f'<tspan baseline-shift="sub" style="font-size:9px">L</tspan>' + (_sup(nL) if nL > 1 else "")
    if ng:
        s += "Γ" + f'<tspan baseline-shift="sub" style="font-size:9px">g</tspan>' + (_sup(ng) if ng > 1 else "")
    return s


# ------------------------------------------------------------------------------------------------ 1. the circuit
def fig_bounce_circuit():
    W, H = 640, 236
    o = [svg_open(W, H)]
    yt, yb = 64, 172                       # upper wire (wire 2), lower wire (wire 1)
    xs, x0, x1, xr = 52, 170, 520, 576     # source, line start z=0, line end z=l, load
    # source and R_g
    o.append(circle(xs, (yt + yb) / 2, 15, stroke="var(--hi)", w=1.8))
    o.append(text(xs, (yt + yb) / 2 - 3, "+", size=13, fill="var(--hi)"))
    o.append(text(xs, (yt + yb) / 2 + 12, "−", size=13, fill="var(--hi)"))
    o.append(text(xs - 20, (yt + yb) / 2 + 5, _sub("f", "i") + "(t)", size=13, anchor="end"))
    o.append(line(xs, (yt + yb) / 2 - 15, xs, yt)); o.append(line(xs, yt, 82, yt))
    o.append(_zigzag(82, yt, 134, yt, n=6, amp=7))
    o.append(text(108, yt - 14, _sub("R", "g"), size=13))
    o.append(line(134, yt, x0, yt))
    o.append(line(xs, (yt + yb) / 2 + 15, xs, yb)); o.append(line(xs, yb, x0, yb))
    # the line: two thick conductors
    o.append(line(x0, yt, x1, yt, w=4.5)); o.append(line(x0, yb, x1, yb, w=4.5))
    o.append(text(x1 - 6, yt - 9, "wire 2", size=10.5, anchor="end", fill="var(--muted)"))
    o.append(text(x1 - 6, yb + 17, "wire 1", size=10.5, anchor="end", fill="var(--muted)"))
    o.append(text((x0 + x1) / 2 + 40, yt - 14, _sub("Z", "0") + ", v,  T = ℓ/v", size=13))
    # load
    o.append(line(x1, yt, xr, yt)); o.append(line(xr, yt, xr, 88))
    o.append(_zigzag(xr, 88, xr, 148, n=6, amp=7))
    o.append(line(xr, 148, xr, yb)); o.append(line(xr, yb, x1, yb))
    o.append(text(xr + 14, (yt + yb) / 2 + 5, _sub("R", "L"), size=13, anchor="start"))
    # V(z,t) reference: + on wire 2, - on wire 1
    xv = 214
    o.append(text(xv, yt + 20, "+", size=14))
    o.append(text(xv, (yt + yb) / 2 + 5, "V(z,t)", size=13))
    o.append(text(xv, yb - 9, "−", size=14))
    # I(z,t) reference: +z on wire 2, return (-z) on wire 1
    o.append(arrow(x0 + 18, yt - 12, x0 + 62, yt - 12, stroke="var(--hi)", w=1.8, small=True))
    o.append(text(x0 + 40, yt - 20, "I(z,t)", size=12, fill="var(--hi)"))
    o.append(arrow(x0 + 62, yb + 12, x0 + 18, yb + 12, stroke="var(--hi)", w=1.8, small=True))
    o.append(text(x0 + 40, yb + 27, "I(z,t)", size=12, fill="var(--hi)"))
    # forward and backward waves
    xm = 390
    o.append(arrow(xm - 70, 100, xm + 80, 100, stroke="var(--accent)", w=2.2, small=True))
    o.append(text(xm + 5, 90, "f(t − z/v),  I = +V/" + _sub("Z", "0"), size=12, fill="var(--accent)"))
    o.append(arrow(xm + 80, 138, xm - 70, 138, stroke="var(--accent2)", w=2.2, small=True))
    o.append(text(xm + 5, 128, "g(t + z/v),  I = −V/" + _sub("Z", "0"), size=12, fill="var(--accent2)"))
    # z axis
    ya = 214
    o.append(line(x0, ya, x1 + 70, ya, w=1.2, arrow=True)); o.append(text(x1 + 76, ya + 4, "z", size=13, anchor="start", math=True))
    for X, lab, sub in ((x0, "0", "generator"), (x1, "ℓ", "load")):
        o.append(line(X, ya - 4, X, ya + 4, w=1.2))
        o.append(text(X, ya - 9, lab, size=12))
        o.append(text(X, ya + 17, sub, size=10.5, fill="var(--muted)"))
    o.append(svg_close())
    figure("bounce-circuit", "".join(o),
           "<strong>The notes' circuit, with the site's references.</strong> V(z,t) is wire 2 relative to wire 1; I(z,t) "
           "flows along +z on wire 2 and returns on wire 1. Forward waves carry I = +V/Z<sub>0</sub>, backward waves "
           "I = −V/Z<sub>0</sub>.")


# ------------------------------------------------------------------------------------------------ 2. generic diagram
def fig_bounce_diagram():
    W, H = 640, 410
    o = [svg_open(W, H)]
    X0, X1 = 92, 412                       # z = 0, z = l
    Y0, dY = 62, 50                        # t = 0, pixels per T
    MX = lin(0, 1, X0, X1); MY = lambda tT: Y0 + dY * tT
    zp = 0.3
    # axes
    o.append(line(X0, Y0, X1 + 34, Y0, w=1.3, arrow=True)); o.append(text(X1 + 40, Y0 + 4, "z", size=13, anchor="start", math=True))
    o.append(line(X0, Y0, X0, MY(6.55), w=1.3, arrow=True)); o.append(text(X0, MY(6.55) + 16, "t", size=13, math=True))
    o.append(line(X1, Y0, X1, MY(6.3), w=1.0, dash="3 3", opacity=0.6))
    o.append(text(X0, Y0 - 10, "0", size=12)); o.append(text(X1, Y0 - 10, "ℓ", size=12))
    o.append(text(X0 + 4, Y0 - 30, "generator: " + _sub("Γ", "g") + ", " + _sub("τ", "g"), size=12, anchor="start", fill="var(--muted)"))
    o.append(text(X1 + 4, Y0 - 30, "load: " + _sub("Γ", "L"), size=12, anchor="end", fill="var(--muted)"))
    for k in range(1, 7):
        side = X1 if k % 2 else X0
        o.append(line(side - 4, MY(k), side + 4, MY(k), w=1.1))
        o.append(text(side + (10 if k % 2 else -10), MY(k) + 4, ("" if k == 1 else str(k)) + "T", size=11.5,
                      anchor="start" if k % 2 else "end", fill="var(--muted)"))
    # segments and weights: forward k even, backward k odd
    labels = [(0, 0), (1, 0), (1, 1), (2, 1), (2, 2), (3, 2)]
    for k, (nL, ng) in enumerate(labels):
        za, zb = (0, 1) if k % 2 == 0 else (1, 0)
        xa, ya, xb, yb = MX(za), MY(k), MX(zb), MY(k + 1)
        col = "var(--accent)" if k % 2 == 0 else "var(--accent2)"
        o.append(arrow(xa, ya, xb, yb, stroke=col, w=2.4))
        # label just above the segment, near its first third
        fx = 0.6                                   # forward: z = 0.6 l; backward: z = 0.4 l (clear of z_p)
        lx = xa + (xb - xa) * fx; ly = ya + (yb - ya) * fx - 9
        o.append(text(lx, ly, _w(True, nL, ng), size=12.5, fill=col))
    # observation line and crossings
    xp = MX(zp)
    o.append(line(xp, Y0, xp, MY(6.3), w=1.4, dash="5 4", stroke="var(--hi)"))
    o.append(text(xp, Y0 - 10, _sub("z", "p"), size=12, fill="var(--hi)"))
    cross = []
    for k in range(6):
        tk = (k + zp) if k % 2 == 0 else (k + 1 - zp)
        cross.append(tk)
        o.append(circle(xp, MY(tk), 3.8, fill="var(--hi)", stroke="none"))
    # right panel: V(z_p, t) aligned in time (weights drawn for the page example, Gamma_L = -1/2, Gamma_g = 1/2)
    XB = 530; S = 62                       # baseline, pixels per unit of tau_g
    wts = [w / (V0 * TAU_G) for w in example_weights(6)]
    o.append(text(XB, Y0 - 30, _sub("V", "") + "(" + _sub("z", "p") + ", t)", size=12.5, weight=600))
    o.append(text(XB, Y0 - 12, "drawn for " + _sub("Γ", "L") + " = −½, " + _sub("Γ", "g") + " = ½", size=10.5, fill="var(--muted)"))
    o.append(line(XB, Y0, XB, MY(6.55), w=1.2, arrow=True)); o.append(text(XB, MY(6.55) + 16, "t", size=13, math=True))
    for tk, wv in zip(cross, wts):
        Y = MY(tk)
        o.append(line(X1 + 30, Y, XB - 4, Y, w=0.9, dash="1 4", opacity=0.7, stroke="var(--hi)"))
        o.append(arrow(XB, Y, XB + S * wv, Y, stroke="currentColor", w=2.0, small=True))
        o.append(text(XB + 72, Y + 4, f"{tk:.1f}T", size=11, anchor="start", fill="var(--muted)"))
    o.append(svg_close())
    figure("bounce-diagram", "".join(o),
           "<strong>Bounce diagram for an impulse input.</strong> Each segment is one travelling impulse, labelled with its "
           "voltage weight; ×Γ<sub>L</sub> at the load, ×Γ<sub>g</sub> at the generator. The dashed line at "
           "z<sub>p</sub> = 0.3ℓ meets them at z<sub>p</sub>/v + 2nT (forward) and 2T − z<sub>p</sub>/v + 2nT (backward): "
           "V(z<sub>p</sub>, t), right.")


# ------------------------------------------------------------------------------------------------ 3. step response
def fig_bounce_step():
    W, H = 640, 330
    o = [svg_open(W, H)]
    # left: numeric diagram, 12 V step
    X0, X1, Y0, dY = 40, 200, 58, 38
    MX = lin(0, 1, X0, X1); MY = lambda tT: Y0 + dY * tT
    o.append(text(20, 20, "12 V step: weights (V)", size=12.5, anchor="start", weight=600))
    o.append(line(X0, Y0, X1 + 22, Y0, w=1.2, arrow=True)); o.append(text(X1 + 26, Y0 + 4, "z", size=12, anchor="start", math=True))
    o.append(line(X0, Y0, X0, MY(6.4), w=1.2, arrow=True)); o.append(text(X0, MY(6.4) + 15, "t", size=12, math=True))
    o.append(line(X1, Y0, X1, MY(6.2), w=1.0, dash="3 3", opacity=0.6))
    o.append(text(X0 - 2, Y0 - 8, _sub("Γ", "g") + " = ½", size=11, anchor="start", fill="var(--muted)"))
    o.append(text(X1 + 2, Y0 - 8, _sub("Γ", "L") + " = −½", size=11, anchor="end", fill="var(--muted)"))
    ws = example_weights(6)
    for k, wv in enumerate(ws):
        za, zb = (0, 1) if k % 2 == 0 else (1, 0)
        xa, ya, xb, yb = MX(za), MY(k), MX(zb), MY(k + 1)
        col = "var(--accent)" if k % 2 == 0 else "var(--accent2)"
        o.append(arrow(xa, ya, xb, yb, stroke=col, w=2.2))
        lab = f"{wv:+.4g}".replace("-", "−")
        fx = 0.7 if k % 2 == 0 else 0.75           # forward: z = 0.7 l; backward: z = 0.25 l (clear of l/2)
        lx = xa + (xb - xa) * fx; ly = ya + (yb - ya) * fx - 8
        o.append(text(lx, ly, lab, size=11.5, fill=col))
    xh = MX(0.5)
    o.append(line(xh, Y0, xh, MY(6.2), w=1.2, dash="5 4", stroke="var(--hi)"))
    o.append(text(xh, Y0 - 8, "ℓ/2", size=11, fill="var(--hi)"))
    for k in (1, 3, 5):
        o.append(text(X1 + 8, MY(k) + 4, f"{k}T" if k > 1 else "T", size=10.5, anchor="start", fill="var(--muted)"))
    for k in (2, 4, 6):
        o.append(text(X0 - 6, MY(k) + 4, f"{k}T", size=10.5, anchor="end", fill="var(--muted)"))
    # right: V(l/2,t) and V(l,t)
    PX = lin(0, 8, 300, 596); PY = lin(0, 3.2, 290, 50)
    o.append(text(300, 20, "V(z, t) for " + _sub("f", "i") + " = 12u(t) V", size=12.5, anchor="start", weight=600))
    o.append(line(PX(0), PY(0), PX(8) + 12, PY(0), w=1.2, arrow=True)); o.append(text(PX(8) + 16, PY(0) + 4, "t/T", size=11.5, anchor="start"))
    o.append(line(PX(0), PY(0), PX(0), PY(3.2) - 8, w=1.2, arrow=True))
    for tv in range(0, 9, 2):
        o.append(line(PX(tv), PY(0), PX(tv), PY(0) + 4, w=1.0)); o.append(text(PX(tv), PY(0) + 16, str(tv), size=10.5, fill="var(--muted)"))
    for vv in (0, 1.2, 2, 3):
        o.append(line(PX(0) - 4, PY(vv), PX(0), PY(vv), w=1.0))
        o.append(text(PX(0) - 7, PY(vv) + 4, f"{vv:g}", size=10.5, anchor="end", fill="var(--hi)" if vv == 1.2 else "var(--muted)"))
    o.append(line(PX(0), PY(1.2), PX(8), PY(1.2), stroke="var(--hi)", w=1.4, dash="6 4"))
    o.append(text(PX(8), PY(1.2) + 18, "DC: 12·" + _sub("R", "L") + "/(" + _sub("R", "g") + " + " + _sub("R", "L") + ") = 1.2 V", size=11, anchor="end", fill="var(--hi)"))
    tt = np.linspace(0, 8, 3201)
    Vh, Vl = step_curves(tt)
    o.append(poly(tt, Vh, PX, PY, stroke="var(--accent)", w=2.4))
    o.append(poly(tt, Vl, PX, PY, stroke="var(--accent2)", w=2.4))
    o.append(line(420, 70, 444, 70, stroke="var(--accent)", w=2.4)); o.append(text(450, 74, "z = ℓ/2", size=11.5, anchor="start"))
    o.append(line(520, 70, 544, 70, stroke="var(--accent2)", w=2.4)); o.append(text(550, 74, "z = ℓ (load)", size=11.5, anchor="start"))
    o.append(svg_close())
    figure("bounce-step", "".join(o),
           "<strong>Example: Z<sub>0</sub> = 60 Ω, R<sub>g</sub> = 180 Ω, R<sub>L</sub> = 20 Ω, 12 V step.</strong> "
           "Each crossing adds its weight, so V(z,t) is a staircase. Γ<sub>L</sub>Γ<sub>g</sub> = −¼ makes it "
           "overshoot and undershoot the DC value, at every z. Checked against an FDTD run.")


if __name__ == "__main__":
    for fn in (fig_bounce_circuit, fig_bounce_diagram, fig_bounce_step):
        fn()
