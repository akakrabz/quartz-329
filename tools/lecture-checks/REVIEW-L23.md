# Review — Lecture 23 page set (imperfect dielectrics, good conductors)

Reviewed: `23-imperfect-dielectrics-and-good-conductors.md`, `concepts/loss-tangent.md`, `concepts/skin-depth.md`, the new section of
`concepts/conductivity-and-susceptibility-models.md`, `problems/a-radio-wave-into-moist-ground.md`, `figs_l23.py` (5 figures, rendered
light/dark with playwright, table checked at 820 and 390 px). Sources: notes pp. 1–6 (images), Rao §5.3–5.4 and Tables 5.1–5.3,
exam scans (S17/S18/S19/S20 HE3, FA23), L22 page (read only), Wikipedia "Communication with submarines", ITU-R P.527-6 §4.1.
Script: `digest8/review_L23.py` → `review_L23.out`, **482 PASS, 0 FAIL** (written before reading `verify_L23.py`). `check.py`: OK.

| # | sev. | where | what | fix |
|---|---|---|---|---|
| 1 | blocker | L23 §3 "Where does the lost power go?" | "the power flowing **out of** any small volume equals the power delivered to the charges": sign reversed (net outflow = −⟨J·E⟩ < 0) | "the **net power flowing into** …" [E, Z1] |
| 2 | major | L23 §2 regime table | ID α, δ and GC α, β, \|η\|, τ, λ, δ written as equalities next to ≈ entries: approximations stated as exact (notes do the same) | ≈ on every approximate entry (braced so KaTeX keeps "≈ x" on one line); noted under the page's notes slips [C, Z8] |
| 3 | major | fig `cond-seawater-alpha-beta` label + caption | "\|η\| ≈ √(ωμ/σ): a small fraction of an ohm" across the GC band; the plotted curve is 1.4 Ω at 1 MHz, 13 Ω at 89 MHz | "far below √(μ/ε)"; caption gives 0.044 Ω at 1 kHz, 1.4 Ω at 1 MHz [L, Z4] |
| 4 | minor | L23 §2 "How small is small" | "within 0.3 %" but τ is 0.33 %; α, β errors 0.1246 % printed 0.13 % | "within about 0.3 %", 0.12 %; added p = 0.3 (ID α 1.1 %) and p = 3 (GC α 18 %) [C, Z2] |
| 5 | minor | L23 §1 key; 2 figure captions | "between 0.1 and 10 neither set is accurate": too strong on the dielectric side | "the approximations lose accuracy (the good-conductor ones fastest)"; captions "use the exact formulas" [Z3] |
| 6 | minor | L23 On exams #1, #3 | #1 stated the S19 conflict key inequality (ω > 10σ/ε); #3 quoted the exam medium's f_c = 18 MHz | method only ("write the regime condition and solve for ω", "its own f_c"); noted the exam's dry earth ≠ Rao's [M] |
| 7 | minor | loss-tangent page | "dry earth of a past exam … 1.8×10⁵ at 100 Hz" is the S20 HE3 #3(c) key step | re-parameterized: 1.8×10⁴ at 1 kHz [M] |
| 8 | minor | problem, 10 MHz variant | 4.19 dB/m (double rounding of α = 0.482); exact 4.185 | 4.18 dB/m [J] |
| 9 | minor | L23 §5 submarines | antenna size, power and one-way link unsourced; "they match the table" overclaims (100 dB is assumed) | attributed to the same Wikipedia article (text + Sources); "consistent with … the assumed 100 dB budget" [G] |
| 10 | minor | L23 §7 trap | "for metals \|η\| is milliohms" (copper 60 Hz: 2.9 µΩ) | "milliohms or less" [Z6] |
| 11 | minor | loss-tangent, skin-depth pages | "for large p, α = β"; "1/α = (2/σ)√(ε/μ)" stated as exact | ≈ [Z9] |
| 12 | minor | skin-depth page | "the field cannot simply soak in" contradicts L22's "fields soak into a good conductor" (diffusion) | "does not simply fill the conductor" [Z10] |
| 13 | minor | Lorentz–Drude page | "imperfect dielectric that only weakens the wave slowly" (seawater still 84 Np/m above 10 f_c) | "only a little per wavelength" [K] |
| 14 | minor | fig `cond-problem-depth` | y axis "loss [dB]" carries negative values | "level relative to the surface [dB]" [Z5] |
| 15 | minor | fig `cond-regime-map` caption | Mica and Bakelite "insulators above a few hertz"; Bakelite is in between up to 37 Hz | "act as dielectrics above a few tens of hertz" [Z7] |
| 16 | minor | fig `cond-good-conductor-fields` caption | "never gets as far as a second wavelength" (it is −109 dB there, not zero) | "−109 dB after two wavelengths: effectively gone" |
| 17 | minor | L23, problem | `\mathrm{Re}` vs `\text{Re}` of L21–L22; "the loss-tangent page has the phasor sketch" (it has none) | `\text{Re}`; "describes the phasor diagram" |

**Verified correct (no change):** every f_c and regime boundary of the media table; all seawater numbers (σ/ωε at 4 frequencies,
exact α = 77 Np/m and δ = 1.3 cm at 1 GHz, 673 dB/m, plateau 84 Np/m, the 6-row frequency table incl. 100 dB depths, 11.5δ);
copper/aluminium δ and \|η\| tables (0.0661/√f, 0.0851/√f, 3.69×10⁻⁷√f Ω), skin-effect ×7.6, shielding 0.09δ/11.8δ/102 dB, 1.7 µm
at 2.45 GHz, copper f_c = 1.04×10¹⁸ Hz (4.3 keV, X-ray); polar forms vs exact γ, η for 200 random media; α = σ\|η\|/(2cos τ) exact;
Examples 1–3 (all numbers, H direction, phases); FD Maxwell residuals < 1e-9 for every time-domain pair (+z, −z, −y); ⟨S⟩ by
quadrature = ½Re{Ẽ×H̃*} = formula; e^{−2αz} for power vs e^{−αz} for field; dB/m = 8.686α for both; ⟨w_e⟩/⟨w_m⟩ = 1/√(1+p²);
inverse example; worked problem (a)–(e) and variant; every `np.cross` (incl. the figure icon in the screen frame).
**Handbook values** (stated in the script): Cu 5.80×10⁷ (IACS) ✓; Al 3.5×10⁷ is Rao's, 7 % below pure Al (3.77×10⁷), within
commercial grades; seawater 4 S/m (4.29 at 35 PSU, 15 °C) ✓, ε_r 81 at the top of 70–81; fresh water 10⁻³ ✓; loam 10⁻² (ITU-R
P.527-6 §4.1 "normally ~10⁻² S/m … as low as 10⁻⁴ dried": wording verified) ✓; dry earth, Bakelite, mica within ranges.
**Accuracy claims** at p = 0.1, 1, 10 recomputed (table above for the two corrections). **Submarines:** Wikipedia confirms VLF
3–30 kHz, a few tens of metres, ~300 bit/s; ELF 76 Hz (US, dismantled Sept 2004) and 82 Hz (ZEVS), hundreds of metres, a few
characters per minute; Republic MI antenna ≈ 52 km; one-way links. Now stated cautiously and attributed.
**L22 consistency:** τ = ½tan⁻¹(σ/ωε), α/β = tan τ, 13.5 %/14 % at δ, e^{−2π} per λ, sea-water crossover 0.9 GHz, the binomial limits
and the hand-off of power bookkeeping all agree; wording conflict on "soak" fixed on the L23 side (L22 not edited).

**Coverage:** complete. All 40 items of `COVERAGE-L23.md` checked against the six page images; nothing in the notes is missing or
misrepresented. Errata 1–6 confirmed (25/π = 7.9577 → 7.96; 72×10⁹/81×10³ = 8.9×10⁵; Ex. 2 keeps 4ε₀; missing ·; "perfect"
dielectric; the unfair Ex. 1/Ex. 2 comparison). One addition (now on the page): the notes' table writes approximate entries as `=`.
**Exam keys:** worked problem re-parameterized (soil, 100 kHz, −ŷ) and shares no number with the S18/S19 HE3 #3b key (25/π m, 50 m,
50 km/s, 0.081); inverse example shares none with S17 HE3 #2b (2×10⁸, 9/4, 80π, 10⁻³/4π).

**Open (judgment calls, left):** (a) the problem's closing paragraph notes that S18/S19 #3b reuses the notes' Example 3, whose
numbers the lecture page shows — that is the notes' own example, so kept. (b) Seawater ε_r = 81 (notes) is high for real seawater
(≈ 70–75); it moves f_c by ~10 %, covered by the page's "typical" caveat. (c) "copper's σ no longer constant above about 10¹³ Hz":
the Drude knee is 6.5 THz and a 1 % change already appears near 0.9 THz; order-of-magnitude statement, kept. (d) The problem
figure's "0.55 dB/m" is the GC answer rounded while the line uses the exact α (0.544 dB/m), 0.3 % apart. (e) The problem's
η = 2π(1+j) Ω and v_p = 10⁷ m/s coincide with Rao Problem 5.25(b) (same f/σ); a textbook problem, not an exam.
