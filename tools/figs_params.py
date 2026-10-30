#!/usr/bin/env python3
"""Figure: the wave-parameter map (Toolkit page 07)."""
from figs import *
try:
    from figs import _sub, _tint
except ImportError:  # older figs.py without part-2 helpers
    def _sub(base, s, size=9):
        return f'{base}<tspan baseline-shift="sub" style="font-size:{size}px">{s}</tspan>'
    def _tint(x, y, w, h, color, op=0.12, rx=0):
        return rect(x, y, w, h, fill=color, stroke="none", opacity=op, rx=rx)

def _box(o, x, y, w, h, title, lines, color, title_size=14, size=12.5, lh=17):
    o.append(_tint(x, y, w, h, color, op=0.10, rx=8))
    o.append(rect(x, y, w, h, stroke=color, sw=1.6, rx=8))
    o.append(text(x + w/2, y + 19, title, size=title_size, weight=700, fill=color))
    yy = y + 19 + lh + 2
    for ln in lines:
        o.append(text(x + w/2, yy, ln, size=size))
        yy += lh

def fig_wave_parameter_map():
    W, H = 760, 600
    o = [svg_open(W, H)]
    A, B, C, M = "var(--accent)", "var(--accent2)", "var(--hi)", "var(--muted)"
    o.append(text(20, 24, "Wave parameters: who is computed from whom", size=18, anchor="start", weight=700))
    o.append(text(20, 44, "Given a medium and a frequency, everything else follows from two complex numbers, γ and η.",
                  size=12.5, anchor="start", fill=M))

    # column headers
    for x, s in ((120, "1 · what you are given"), (380, "2 · the two complex numbers"), (640, "3 · what the wave shows")):
        o.append(text(x, 72, s, size=13, weight=700, fill=M))

    # --- column 1
    _box(o, 20, 84, 200, 118, "Medium", [
        "μ = " + _sub("μ", "r") + "μ₀   (almost always μ₀)",
        "ε = " + _sub("ε", "r") + "ε₀,   n = √(" + _sub("μ", "r") + _sub("ε", "r") + ")",
        "σ   [S/m]  conduction",
        "p = σ/ωε  loss tangent = tan θ",
    ], A)
    _box(o, 20, 222, 200, 70, "Signal", [
        "ω = 2πf   [rad/s]",
        "(the only thing you control)",
    ], A)

    # --- column 2: gamma and eta
    _box(o, 265, 84, 230, 112, "γ = α + jβ   [1/m]", [
        "γ = √( jωμ (σ + jωε) )",
        "α [Np/m]: how fast it decays",
        "β [rad/m]: how fast phase turns",
        "e^(−γz) = e^(−αz) e^(−jβz)",
    ], B)
    _box(o, 265, 222, 230, 112, "η = |η| e^(jτ)   [Ω]", [
        "η = √( jωμ / (σ + jωε) )",
        "|η|: ratio |E| / |H|",
        "τ = ∠η: H lags E by τ",
        "τ = θ/2  (0 … 45°)",
    ], B)
    # link between gamma and eta
    o.append(line(380, 196, 380, 222, stroke=B, w=1.5, dash="3,3"))
    o.append(_tint(300, 200, 160, 20, B, op=0.18, rx=4))
    o.append(text(340, 214, "γη = jωμ", size=12, weight=600))
    o.append(text(425, 214, "γ/η = σ + jωε", size=12, weight=600))

    # arrows from column 1 to column 2
    o.append(arrow(220, 143, 262, 130, stroke=A, w=1.8))
    o.append(arrow(220, 257, 262, 268, stroke=A, w=1.8))
    o.append(arrow(220, 150, 262, 262, stroke=A, w=1.8, opacity=0.6))
    o.append(arrow(220, 250, 262, 136, stroke=A, w=1.8, opacity=0.6))

    # --- column 3
    _box(o, 540, 84, 200, 72, "from α", [
        "δ = 1/α   [m]  penetration depth",
        "|E| ∝ e^(−z/δ),  ⟨S⟩ ∝ e^(−2z/δ)",
    ], C)
    _box(o, 540, 166, 200, 90, "from β", [
        "λ = 2π/β   [m]",
        _sub("v", "p") + " = ω/β   [m/s]",
        _sub("v", "g") + " = dω/dβ  (the message)",
    ], C)
    _box(o, 540, 266, 200, 72, "from η", [
        "H̃ = (ẑ × Ẽ)/η  for +z travel",
        "|H| = |E|/|η|,  phase −τ",
    ], C)
    o.append(arrow(495, 120, 538, 120, stroke=B, w=1.8))
    o.append(arrow(495, 160, 538, 205, stroke=B, w=1.8))
    o.append(arrow(495, 290, 538, 300, stroke=B, w=1.8))

    # --- regime strip
    y0 = 362
    o.append(text(20, y0, "The regimes — one number, p = σ/ωε, decides which simplification applies", size=13.5,
                  anchor="start", weight=700))
    # axis
    o.append(line(40, y0 + 22, 720, y0 + 22, w=1.5, arrow=True))
    o.append(text(40, y0 + 40, "p = 0", size=11.5, fill=M))
    o.append(text(260, y0 + 40, "p = 0.1", size=11.5, fill=M))
    o.append(text(500, y0 + 40, "p = 10", size=11.5, fill=M))
    o.append(text(720, y0 + 40, "p → ∞", size=11.5, fill=M))
    for x in (260, 500):
        o.append(line(x, y0 + 16, x, y0 + 28, w=1.5))
    cols = [
        (20, 225, "perfect dielectric  (σ = 0)", A, [
            "α = 0,  δ = ∞",
            "β = ω√(με) = nω/c",
            "η = √(μ/ε) = η₀/n  (real)",
            "τ = 0: E and H in phase",
            _sub("v", "p") + " = 1/√(με) = c/n",
        ]),
        (268, 225, "imperfect dielectric  (p ≪ 1)", B, [
            "α ≈ (σ/2)√(μ/ε)   (σ-controlled)",
            "β ≈ ω√(με)   (unchanged)",
            "|η| ≈ √(μ/ε),  τ ≈ p/2  rad",
            "δ ≈ (2/σ)√(ε/μ):  f-independent",
            "many wavelengths per δ",
        ]),
        (516, 224, "good conductor  (p ≫ 1)", C, [
            "α = β = 1/δ",
            "δ = 1/√(πfμσ) = √(2/ωμσ)",
            "η = (1+j)/(σδ),  τ = 45°",
            "λ = 2πδ,  " + _sub("v", "p") + " = ωδ  (slow)",
            "gone within one wavelength",
        ]),
    ]
    for x, w, title, col, lines in cols:
        _box(o, x, y0 + 52, w, 128, title, lines, col, title_size=13, size=12, lh=18)
    o.append(text(20, 590, "Between 0.1 and 10 use the exact γ and η (polar form: 1 − jp = √(1+p²) e^(−jθ)). "
                  "Lossless limit of every formula: set σ = 0.", size=11.5, anchor="start", fill=M))
    o.append(svg_close())
    svg = "".join(o).replace("   ", "&#160;&#160;&#160;").replace("  ", "&#160;&#160;")
    figure("wave-parameter-map", svg,
           "The wave-parameter map. Left: what a problem gives you (μ, ε, σ and ω). Middle: the two complex numbers "
           "built from them, tied together by γη = jωμ and γ/η = σ + jωε. Right: what each part of γ and η does to the "
           "wave. Bottom: the loss tangent p = σ/ωε picks the regime and its simplifications.")

if __name__ == "__main__":
    fig_wave_parameter_map()
