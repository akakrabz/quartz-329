# REVIEW — Lecture 21 (Monochromatic waves and phasor notation), independent review

Files reviewed: `3-maxwell-and-waves/21-monochromatic-waves-and-phasor-notation.md`, `concepts/phasors.md`,
`concepts/dispersion-relation.md`, `concepts/plane-waves.md` (monochromatic section), `problems/phasors-e-and-power-from-a-given-h.md`,
`figs_l21.py` (5 figures, rendered light + dark). Notes: `329lect21.pdf` pp. 1–8 (page renders read one by one), L22/L24 notes for v_g.
Own checks: `digest8/review_L21.py` → `review_L21.out`, **202 PASS, 0 FAIL**: Maxwell's curl equations by 3-D finite differences for
every field pair (notes' Examples 1–3, the 200 MHz example, random complex plane waves, the worked problem and its magnetic variant,
plus controls with the wrong rotation that must fail); every time average by quadrature vs ½Re{ÃB̃*}; np.cross for every direction;
the plasma relation from the collisionless Drude current (wave-equation residual, ε_eff, ⟨J·E⟩ = 0), v_g = dω/dβ by finite difference
**and** by FFT propagation of a narrowband pulse (envelope at 0.745c = v_g); sound speeds vs handbook (Zuckerwar 20 °C: He 1007, Ar 319 m/s;
CRC Ar 323 m/s at 27 °C; dry air 343.2 / 331.3 m/s), f_p = 8.98√N vs Rao §10.1. `check.py`: OK. Phone width (390 px): 0 overflowing displays.

## Findings (all fixed)
| # | sev | where | what | fix |
|---|---|---|---|---|
| 1 | major | page §7 trap "Power from phasors", bullet 4 | "For one wave [instantaneous **S**] swings between 0 and twice the average" holds only for a linearly polarized wave; a single wave with out-of-phase perpendicular components never reaches 0 (the worked problem's own (f): −4.2 to −27.2 W/m²), a circular one is constant. The trap contradicted the worked problem. [L11, L12, M21] | restricted to "one linearly polarized wave", added the out-of-phase case with a link to the worked problem (f) |
| 2 | minor | page §2, plasma bullet ω > ω_p | β = 0.0923 rad/m with the stated f_p = 8.98 MHz; that input gives 0.0922 (0.0923 needs the unrounded 8.979 MHz). λ, v_p, v_g unaffected. [C10, C11] | 0.0922 |
| 3 | minor | page §5 "Why the conjugate" | Ẽ×H̃ "points nowhere in particular": it is (Ẽ·Ẽ/η)û, still along û; its coefficient turns along z, so its real part changes sign every λ/4. [F3] | reworded with the formula |
| 4 | minor | page §5 Faraday derivation, last line | complex η "breaks the rides-along-unchanged": complex factors still ride along; what changes is that H̃ gains −∠η relative to Ẽ | reworded |
| 5 | minor | page §2 opening | "… plasma physics or quantum mechanics, has the same form A cos(ωt ∓ βz)": Schrödinger's equation has no real-cosine solutions | "seismology" |
| 6 | minor | page §2 opening | "the propagation speed always follows … v_p = ω/β" against the section's own trap (ω/β is the phase velocity) | "the phase velocity" |
| 7 | minor | page §7 trap, bullet 2 | ½Re{Ẽ×H̃} "for a single wave varies as cos 2βz": linear polarization only (0 for circular) [F3, L10] | "single linearly polarized wave" |
| 8 | minor | page §1 | "Exam papers also say time-harmonic or co-sinusoidal": OCR of all 88 Exam 3/HE3/FE scans finds "co-sinusoidal", never "time-harmonic" (the notes' p. 8 margin uses it) | attributed to the notes |
| 9 | minor | On exams, item 1 | "… a ẑ sine, both with (ωt + βx)" reads as both papers; SP17 #4a is (ωt − βz) | "a ẑ sine of (ωt + βx)" |
| 10 | minor | page §7 product-rule proof | ½AB cos(θ_a − θ_b) used A, B, θ_a, θ_b without defining them | "Here Ã = Ae^{jθ_a}, B̃ = Be^{jθ_b}" |
| 11 | minor | page §3, derivative rule | "a cosine is steepest a quarter period before its peak" (it is equally steep, falling, a quarter period after) [D17] | "rises fastest" |
| 12 | minor | page §1 | the notes' margin plots "side by side": they are one above the other | fixed |
| 13 | minor | page §8; `phasors.md` "Where it appears" | "complex β and η" for Lecture 22, whose page writes γ = α + jβ with β real | "complex γ = α + jβ and η" |
| 14 | minor | page §3 derivative display; §2 plasma display | overflowed a 390 px phone by 9 px and 3 px | split on two lines / thinner spacing |

## Verified correct (no change)
- Plasma: β = (1/c)√(ω² − ω_p²), v_p = c/√(1 − ω_p²/ω²) > c, v_g = c√(1 − ω_p²/ω²) < c, v_p v_g = c², no real β below ω_p, f_p ≈ 8.98√N,
  10 MHz: λ 68.1 m, 2.27c, 0.440c; 100 MHz 1.004c; the Drude derivation and "J lags E by 90°, ⟨J·E⟩ = 0, lossless". Figure P: 1.34c / 0.75c.
- Every phasor conversion (the 8-row table, sine → −j, Examples 1–3, the sine-current variant, the worked problem incl. its three
  slip variants) and every direction from e^{∓jβz} and the template (a, b, c) = −βû (450 MHz and diagonal examples).
- The proof of ⟨ab⟩ = ½Re{ÃB̃*} (expansion checked pointwise, averages by quadrature, vector forms ⟨E×H⟩, ⟨J·E⟩ with random phasors);
  sheet ±60πẑ and 120π W/m² both routes; Example 2's power and the parallel-polarization cross terms (purely imaginary).
- Figures: all five computed from formulas, directions verified by cross products in the screen frame, labels clear in light and dark.
- Scope: lossless only (σ appears only in pointers to L22–23 and in the ⟨J·E⟩ = ½Re{σ}|Ẽ|² link to L10–11).

## Coverage verdict
All 26 items of the notes (pp. 1–8: monochromatic waves, β as wave-number, margin plots, spatial-frequency remark, the three dispersion
relations and the "for all wave motions" margin, v = λ/T = λf, the p. 3 figure, the spectrum chart, the x-polarized phasor, Example 1's
table, Example 2, the two Ẽ↔H̃ rules, Example 3, the p. 8 averages, the margin proof and ⟨−J_s·E⟩ = η) are on the page and correctly
represented; the COVERAGE-L21 map is accurate. Worked problem: re-parameterized against the S19 HE3 #1a and SP17 E3 #4 scans (H given,
ε_r = 9, −z, new amplitudes/phases); no key carries over. On exams: methods only.

## Unresolved / notes
- `concepts/plane-waves.md` Definition display (pre-existing from the L18 build, not the L21 extension) overflows a 390 px phone (534 px);
  left as is, like several L19 displays.
- The writer's `verify_L21.py` still checks β = 0.0923 (from the unrounded f_p); harmless, the page now matches its stated 8.98 MHz.
- Notes' p. 8 "= η ≈ 120π W/m²" (impedance written as a power density) is reproduced as in the notes (errata E12); numerically right.
