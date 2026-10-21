#!/usr/bin/env python3
"""Lecture 24 figures (pol-*) for the ECE 329 notes: signal transmission and circular polarization.

Same helpers and conventions as figs.py. Running this module writes /home/claude/work/figs/<name>.html.
Every curve is computed with numpy (the AM pulse by exact spectral propagation through beta(w) = sqrt(w^2 - wp^2)/c).

Screen frame: X right, Y up, Z out of the page; SVG y grows downward, so a screen point (X, Y) is drawn at
(cx + X, cy - Y). Polarization views look ALONG the direction of travel +z, so +z points INTO the page (otimes).
With x_hat drawn up and y_hat drawn right: x_hat x y_hat = (0,1,0) x (1,0,0) = (0,0,-1) = into the page = +z,
so the drawn frame is right-handed (checked with np.cross in digest9/verify_L24.py, section J). In this view a
rotation from x (up) toward y (right) is clockwise on the page: right-handed about +z (the notes' right-circular).
"""
from figs import *
from figs import _odot, _otimes, _sub, _tint
from figs_l18 import lin, poly

PI = np.pi


def _legend_line(x, y, color, dash=None, w=2.2, length=26):
    return line(x, y, x + length, y, stroke=color, w=w, dash=dash)


# ------------------------------------------------------------------------------------ AM pulse, exact propagation
WP, C = 1.0, 1.0            # units: omega_p = 1, c = 1 (z in c/omega_p, t in 1/omega_p)
W0, SIG = 2.0, 6.0          # carrier 2 omega_p; Gaussian envelope m(t) = exp(-t^2 / 2 SIG^2)


def beta_plasma(w):
    """exact plasma dispersion beta(w) = sqrt(w^2 - wp^2)/c for w > wp (the spectrum below wp is negligible)"""
    return np.sqrt(np.maximum(w ** 2 - WP ** 2, 0.0)) / C


def am_spectrum(n=2 ** 15, dt=0.05):
    """positive-frequency spectrum of m(t) cos(W0 t) recorded at z = 0 (analytic-signal representation)"""
    t = (np.arange(n) - n // 2) * dt
    s = np.exp(-t ** 2 / (2 * SIG ** 2)) * np.exp(1j * W0 * t)          # analytic signal of m(t) cos W0 t
    S = np.fft.fft(np.fft.ifftshift(s)) * dt
    w = 2 * PI * np.fft.fftfreq(n, dt)
    keep = (w > 0) & (np.abs(S) > 1e-10 * np.abs(S).max())
    return w[keep], S[keep], 2 * PI / (n * dt)


def am_field(z, t):
    """E(z, t) = Re{(1/2pi) sum S(w) exp(j(w t - beta(w) z)) dw}; z array, t scalar"""
    w, S, dw = am_spectrum()
    ph = np.exp(1j * (np.outer(np.ones_like(z), w) * t - np.outer(z, beta_plasma(w))))
    a = (ph * S).sum(axis=1) * dw / (2 * PI)
    return a.real, np.abs(a)


def am_numbers():
    b0 = beta_plasma(W0)
    vp, vg = W0 / b0, C ** 2 * b0 / W0
    return b0, vp, vg


def fig_pol_am_group_delay():
    W, H = 640, 352
    o = [svg_open(W, H)]
    b0, vp, vg = am_numbers()
    t1, dT = 20.0, 20.0
    t2 = t1 + dT
    MZ = lin(0, 54, 60, 600)
    o.append(text(20, 22, "An AM pulse in a plasma, carrier ω = 2" + _sub("ω", "p") +
                  ":  " + _sub("v", "g") + " = 0.87c,  " + _sub("v", "p") + " = 1.15c", size=12.5, anchor="start", weight=600))
    z = np.linspace(0, 54, 1400)
    # the tracked crest: the crest nearest the envelope peak at t1 (phase W0 t - b0 z = 2 pi k)
    zc_env1 = vg * t1
    k = np.round((W0 * t1 - b0 * zc_env1) / (2 * PI))
    zc1 = (W0 * t1 - 2 * PI * k) / b0
    zc2 = zc1 + vp * dT
    rows = [(t1, 108, "t = " + _sub("t", "1")), (t2, 250, "t = " + _sub("t", "1") + " + Δt")]
    for i, (tt, Yc, lab) in enumerate(rows):
        A = 46
        MY = lambda e, Yc=Yc: Yc - A * e
        Ez, env = am_field(z, tt)
        o.append(line(56, Yc, 606, Yc, w=1.1, arrow=True))
        o.append(text(610, Yc + 4, "z", size=12, anchor="start", math=True))
        o.append(text(20, Yc - A - 4, lab, size=11.5, anchor="start", weight=600))
        o.append(poly(z, env, MZ, MY, stroke="var(--muted)", w=1.3, dash="5 4"))
        o.append(poly(z, -env, MZ, MY, stroke="var(--muted)", w=1.3, dash="5 4"))
        o.append(poly(z, Ez, MZ, MY, stroke="var(--accent)", w=1.6))
        ze = vg * tt
        o.append(line(MZ(ze), Yc - A - 6, MZ(ze), Yc + A + 4, stroke="var(--accent2)", w=1.4, dash="3 3"))
        zc = zc1 if i == 0 else zc2
        Ec, _ = am_field(np.array([zc]), tt)
        o.append(circle(MZ(zc), MY(Ec[0]), 4.2, fill="var(--hi)", stroke="none"))
    # displacement arrows under panel 2
    ya, yb = 318, 336
    o.append(arrow(MZ(vg * t1), ya, MZ(vg * t2), ya, stroke="var(--accent2)", w=1.8, small=True))
    o.append(text(MZ(vg * t1) - 6, ya + 4, "envelope peak: " + _sub("v", "g") + "Δt", size=11, anchor="end", fill="var(--accent2)"))
    o.append(arrow(MZ(zc1), yb, MZ(zc2), yb, stroke="var(--hi)", w=1.8, small=True))
    o.append(text(MZ(zc1) - 6, yb + 4, "one crest: " + _sub("v", "p") + "Δt", size=11, anchor="end", fill="var(--hi)"))
    o.append(line(MZ(zc1), 160, MZ(zc1), yb, stroke="var(--hi)", w=0.8, dash="2 3", opacity=0.6))
    o.append(line(MZ(vg * t1), 160, MZ(vg * t1), ya, stroke="var(--accent2)", w=0.8, dash="2 3", opacity=0.6))
    o.append(svg_close())
    figure("pol-am-group-delay", "".join(o),
           "<strong>Envelope at v<sub>g</sub>, crests at v<sub>p</sub>.</strong> Two snapshots of a narrowband AM pulse "
           "propagated through a plasma (exact β(ω), numpy). The envelope (dashed) and its peak advance v<sub>g</sub>Δt; "
           "a marked crest advances v<sub>p</sub>Δt and slides forward through the envelope.")


# ------------------------------------------------------------------------------------ handedness, two views
def _view_axes(cx, cy, R):
    """x_hat up, y_hat right, +z (travel) into the page; returns svg"""
    s = [line(cx - R - 18, cy, cx + R + 22, cy, w=1.0, arrow=True, small=True, stroke="var(--muted)"),
         line(cx, cy + R + 18, cx, cy - R - 22, w=1.0, arrow=True, small=True, stroke="var(--muted)"),
         text(cx + R + 26, cy + 4, "y", size=12.5, anchor="start", math=True),
         text(cx + 6, cy - R - 20, "x", size=12.5, anchor="start", math=True),
         _otimes(cx, cy, r=7, color="var(--accent2)"),
         text(cx - 10, cy + 20, "z", size=12, anchor="end", math=True, fill="var(--accent2)")]
    return "".join(s)


def _rot_arc(cx, cy, R, ph0, ph1, color):
    """arc on the screen circle from math angle ph0 to ph1 (radians, CCW positive), arrow at the end"""
    ph = np.linspace(ph0, ph1, 60)
    d = "M" + " L".join(f"{cx + R * np.cos(p):.1f},{cy - R * np.sin(p):.1f}" for p in ph)
    return path(d, stroke=color, w=2.0, arrow=True)


def fig_pol_handedness():
    W, H = 640, 300
    o = [svg_open(W, H)]
    R = 62
    panels = [(170, "right-circular:  x̂ − jŷ", -1, "clockwise", "var(--hi)"),
              (470, "left-circular:  x̂ + jŷ", +1, "counterclockwise", "var(--accent)")]
    for cx, title, s, sense, col in panels:
        cy = 150
        o.append(text(cx, 30, title, size=13, weight=600))
        o.append(text(cx, 48, sense + " on the page", size=11, fill=col))
        o.append(circle(cx, cy, R, stroke="var(--muted)", w=1.0, dash="3 3"))
        o.append(_view_axes(cx, cy, R))
        # E(t) = x cos wt - s y sin wt  (s = -1: x - jy, s = +1: x + jy); screen X = E_y, Y = E_x
        for wt, dash, lab in ((0.0, None, "t = 0"), (PI / 4, "5 3", "t = T/8")):
            X, Y = -s * np.sin(wt) * R, np.cos(wt) * R
            o.append(line(cx, cy, cx + X, cy - Y, stroke=col, w=2.4, dash=dash, arrow=True))
        # labels on the side away from the rotation: t = 0 beside the x arrow, t = T/8 below the dashed arrow
        o.append(text(cx + s * 8, cy - 0.62 * R, "t = 0", size=10.5, anchor=("start" if s > 0 else "end"), fill=col))
        o.append(text(cx - s * 0.64 * R, cy - 0.10 * R, "t = T/8", size=10, anchor="middle", fill=col))
        # rotation arc: x (math angle 90 deg) toward +y (0 deg) for s = -1, toward -y (180 deg) for s = +1
        o.append(_rot_arc(cx, cy, R + 12, PI / 2 + s * 0.12, PI / 2 + s * 1.15, col))
    o.append(text(W / 2, 262, "Both views look along the direction of travel, +z (into the page, ⊗).", size=11.5))
    o.append(text(W / 2, 282, "Right hand: thumb along +z, fingers curl x → y.  Left hand: thumb along +z, fingers curl x → −y.",
                  size=11.5, fill="var(--muted)"))
    o.append(svg_close())
    figure("pol-handedness", "".join(o),
           "<strong>Right- and left-circular, as the notes define them.</strong> At a fixed point the field vector of "
           "(x̂ ∓ jŷ)e<sup>−jβz</sup> turns once per period. Seen looking along the travel direction, right-circular turns "
           "clockwise and left-circular counterclockwise.")


# ------------------------------------------------------------------------------------ x + e^{j phi} y, eight phases
PHASES = [(-PI / 4, "−π/4"), (-PI / 2, "−π/2"), (-3 * PI / 4, "−3π/4"), (0.0, "0"),
          (PI / 4, "π/4"), (PI / 2, "π/2"), (3 * PI / 4, "3π/4"), (PI, "π")]


def pol_kind(phi, A=1.0, B=1.0):
    """classification for E = x A + y B e^{j phi}, travel +z (the page's rule)"""
    s = np.sin(phi)
    if abs(s) < 1e-12 or A == 0 or B == 0:
        return "linear"
    hand = "right" if s < 0 else "left"
    if abs(A - B) < 1e-12 and abs(abs(s) - 1) < 1e-12:
        return hand + "-circular"
    return hand + "-elliptical"


def fig_pol_phase_family():
    W, H = 640, 386
    o = [svg_open(W, H)]
    R = 40
    o.append(text(20, 22, "E = x̂ cos ωt + ŷ cos(ωt + φ) at a fixed point, seen along +z (into the page)",
                  size=12.5, anchor="start", weight=600))
    o.append(text(20, 50, "ŷ lags x̂ (sin φ &lt; 0) · last panel φ = 0", size=11.5, anchor="start", fill="var(--hi)", weight=600))
    o.append(text(20, 222, "ŷ leads x̂ (sin φ &gt; 0) · last panel φ = π", size=11.5, anchor="start", fill="var(--accent)", weight=600))
    for i, (phi, lab) in enumerate(PHASES):
        r, cidx = divmod(i, 4)
        cx, cy = 90 + 150 * cidx, 116 + 172 * r
        kind = pol_kind(phi)
        col = "var(--hi)" if kind.startswith("right") else ("var(--accent)" if kind.startswith("left") else "currentColor")
        o.append(line(cx - R - 10, cy, cx + R + 12, cy, w=0.9, stroke="var(--muted)", arrow=True, small=True))
        o.append(line(cx, cy + R + 10, cx, cy - R - 12, w=0.9, stroke="var(--muted)", arrow=True, small=True))
        o.append(text(cx + R + 14, cy + 4, "y", size=11, anchor="start", math=True))
        o.append(text(cx + 5, cy - R - 12, "x", size=11, anchor="start", math=True))
        wt = np.linspace(0, 2 * PI, 241)
        X, Y = np.cos(wt + phi) * R, np.cos(wt) * R          # screen X = E_y, Y = E_x
        d = "M" + " L".join(f"{cx + a:.1f},{cy - b:.1f}" for a, b in zip(X, Y))
        o.append(path(d, stroke=col, w=2.0))
        o.append(circle(cx + np.cos(phi) * R, cy - R, 3.6, fill=col, stroke="none"))       # t = 0 point
        if kind != "linear":
            ws = np.linspace(0.10, 0.75, 30)                                                 # direction of travel on the curve
            d = "M" + " L".join(f"{cx + 1.18 * np.cos(a + phi) * R:.1f},{cy - 1.18 * np.cos(a) * R:.1f}" for a in ws)
            o.append(path(d, stroke=col, w=1.6, arrow=True))
        o.append(text(cx, cy + R + 28, "φ = " + lab, size=11.5, weight=600))
        o.append(text(cx, cy + R + 43, kind, size=11, fill=col))
    o.append(svg_close())
    figure("pol-phase-family", "".join(o),
           "<strong>One phase decides the shape and the hand.</strong> Equal amplitudes, travel along +z. The dot marks "
           "t = 0, the short arrow the sense of rotation. φ = 0 or π: linear; φ = ∓π/2: right/left-circular; otherwise "
           "elliptical, right-handed when sin φ &lt; 0.")


if __name__ == "__main__":
    for fn in (fig_pol_am_group_delay, fig_pol_handedness, fig_pol_phase_family):
        fn()
