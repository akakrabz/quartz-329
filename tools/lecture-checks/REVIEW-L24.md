# Review — Lecture 24 "Signal transmission, circular polarization" (build 9)

Files: `3-maxwell-and-waves/24-signal-transmission-and-circular-polarization.md`, `concepts/group-velocity.md`,
`concepts/wave-polarization.md`, `problems/two-sheets-a-quarter-wave-apart.md`, `figs_l24.py` (pol-*).
Independent checks: `digest9/review_L24.py` → `review_L24.out`, **108/108 PASS** (written before reading `verify_L24.py`).
`check.py` OK. Light/dark/380-px renders looked at: no overflow, no KaTeX errors.

**Handedness convention (notes pp. 3–4, read on the images; Rao §4.5 identical).** Right-circular ⇔ right thumb along
the travel, fingers curl with the rotation of E at a fixed point ⇔ clockwise when looking along the travel. The notes
mention no other convention; the page states none. Script: `rotation()` integrates û·(E × dE/dt) over one period at a
fixed point; `screen_sense()` projects onto a screen viewed along û. Every hand claim in the four files checked this way:
notes p. 4 pair, Example 1 (left), Example 2 (E⁺ right, E⁻ left), §4 recipe and "leading → lagging" rule (400 random
phasors and directions), §5 rule, traps, figures (frame x̂ up × ŷ right = into page = +z), worked problem (a)–(c)
by direct time-domain superposition of −(η/2)J_s(t − |z − z₀|/c) on both sides.

**Group velocity.** Gaussian AM pulse (carrier 2ω_p) through exact plasma β(ω) by FFT: envelope peak at z = 200, 600
arrives at 231.00, 692.99 vs z/v_g = 230.94, 692.82 (0.03 %); carrier phase at the peak follows ω₀t − β₀z; width growth
matches the 2nd-order (β'') Gaussian law; non-dispersive case undistorted. v_g = 1/(dβ/dω) by finite differences for
dielectric, gas (He 1019 m/s), plasma (v_pv_g = c²), good conductor (2v_p). Ionosphere: f_p = 8.979 MHz (CODATA;
Rao √(80.6N)), 0.440c, 2.27c, 2.27/1.00/0.44 ms, 0.996c. Folded derivation correct and labelled (site's; Rao §8.3).

| # | sev | where | what | fix |
|---|---|---|---|---|
| 1 | major | L24 §5, concept table, On exams | Rule "x̂, ŷ, travel ±z" applied to other axes in anti-cyclic order (e.g. ẑ, ŷ for x-travel, as in Example 1 / SP19-type items) gives the wrong hand; not said | §5: take components in cyclic order (ŷ,ẑ for ±x; ẑ,x̂ for ±y), else the hand flips, or use §4 recipe; concept trap; On-exams "(cyclic axes otherwise)". Checked (flip shown) |
| 2 | major | problem (b) | Hand recipe evaluated "at z = 0", outside z > λ/4; the real field there is the z<0 wave (E(T/4) = +6πŷ, opposite sense) | evaluate at z = λ = 1 m; (c) now says "at z = 0" (valid there) |
| 3 | major | concept wave-polarization trap | "equal amplitudes or 90° alone gives an ellipse": false for equal amplitudes in phase (linear) | "either alone is not enough" |
| 4 | minor | L24 §4 trap | Overall factor "(−1, j, η) turns the whole picture": η only scales; j delays | "only scales or delays the rotation" |
| 5 | minor | L24 §8, concept | ⟨S⟩ = (\|Ẽx\|²+\|Ẽy\|²)û/2η stated for any û | L24: "travelling along û = ±ẑ"; concept: \|Ẽ\|²û/2η |
| 6 | minor | L24 §4, concept | H's polarization not mentioned (FA23 #2 gives H) | trap: H = û×E/η is E turned 90° about û, same shape and hand (checked) |
| 7 | minor | L24 §2 | v_g table (site's own) not labelled in place; m (atomic mass) clashes with m(t) | title "(this site's table)"; "m the atomic mass" (also concept) |
| 8 | minor | L24 §2 | Notes' ∂ω/∂β notation not stated (brief rule) | one sentence |
| 9 | minor | L24 / concept ionosphere ex. | "the message arrives after 2.27 ms": first-order delay holds only for a narrow band (½\|β''\|Ω²z = 0.03 at 3 kHz, 0.30 at 10 kHz) | "a voice-band message" |
| 10 | minor | L24 Summary | hand-rule bullet did not say which hand | "the hand whose fingers follow the rotation names it" |
| 11 | minor | fig pol-phase-family | row headers "sin φ < 0 / > 0" sat over the φ = 0 / π linear panels | headers add "· last panel φ = 0 / π"; module re-run |

Everything else verified: Fields 1–3 (Maxwell by finite differences, H = ẑ×E/η, quarter-period identity), phasor
pairs, Example 3 (H̃ = (ŷ + jx̂)/η₀, (−jŷ)×(−jx̂) = ẑ, ⟨S⟩ = ẑ/η₀ = 2.654 mW/m² = quadrature), constant instantaneous
S for circular, 2ω pulsing for linear, bases weights, figures (AM markers at v_gt and on true crests; arrow senses).
Worked problem: P = −6π, Q = je^{jφ}, linear π/2 (x̂ − ŷ) and 3π/2 (x̂ + ŷ), right π, left 0, right also in z < 0,
⟨S⟩ = 0.3π W/m² by quadrature for all φ. Re-parameterized vs Summer 2020 FE #4 (scan p. 4: key P = 60π, Q = −e^{jφ},
right π/2, left −π/2, ⟨S⟩ = 30π): no answer carries over. On exams: methods only, ≤ 120 words.

**Coverage verdict:** complete. All 35 notes items (COVERAGE-L24 rows) are on the page and faithful; p. 1 margin plots
and p. 8 margin sketch not redrawn (acceptable). Site additions (derivation, table, ionosphere, recipe, §5 elliptical,
general ⟨S⟩) are correct and labelled. Errata 1–5 confirmed on the page images.
Words after review: lecture 2517 (≤ 3000), group-velocity 420, wave-polarization 496 (≤ 500), problem 845 (≤ 900).

**Unresolved / judgement calls:** Erratum 2 ("non-linear" → "not proportional") is a wording nitpick; kept. Header
line keeps "slides: not available" wording (L23 uses a bold variant; not harmonized).
