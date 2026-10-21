# Review — Lecture 30 (Multi-line circuits), build 11

Files reviewed: `4-transmission-lines/30-multi-line-circuits.md` (2,048 words), `problems/echoes-trapped-on-the-second-line.md`
(832), `figs_l30.py` + `figs/mline-{bounce,burst,junctions,problem-bounce}.html`, `COVERAGE-L30.md`, `ERRATA-L30.md`. No concept pages.
Verification: `digest10/review_L30.py` → `review_L30.out`, **114 PASS / 0 FAIL**. Two independent simulators: an exact
characteristic lattice (every generator/junction/load solved from its own KVL/KCL with `np.linalg.solve`, no Γ/τ formula) and a
Yee FDTD of the telegrapher's equations (Courant 0.5, smooth-ramp steps). Checked: junction Γ, τ, Γ_kj, τ_kj, current and power
ratios (random Z's); shunt/series/three-line junctions by direct circuit solve and by simulated pulses; every segment weight in
both bounce figures at its midpoint; the impulse-response key (V and I, all probes, 0–70 μs, exact); Example 2 snapshots vs the
figure's own curves (exact), front positions, 4/9 at 12 μs, echo span 600–1200 m, λ = 150/300 m, late amplitudes 1/2 (line 2),
3/8 and 1/8 (line 1), snapshot range [1/4, 1/2], 1/4 at half-integer μs; DC limits; Example 1 and the coax ε_r = 4 realization
(v₁ = 149.9 m/μs); worked problem (a)–(e) on the lattice and by FDTD, including uniqueness of R_L = 180 Ω in (e).

## Findings

| # | severity | where | what | fix |
|---|---|---|---|---|
| 1 | major | L30 §2 recipe, step 6 | "add the weights of every segment that has crossed z by time t" is the step-input reading only; wrong for the δ and sine inputs the page uses next | now: a segment of weight w crossing z at t_k adds w f_i(t − t_k); for a step, add the weights crossed by t |
| 2 | minor | L30 §1 trap, last bullet | "Only junction coefficients obey τ = 1 + Γ" contradicts §4 (series R junction) | "holds at a junction (not with a series resistor, §4), never for injection" |
| 3 | minor | L30 §4 trap | "Γ² plus the power into line k" mixes a ratio with a power | "plus the fraction of power entering line k" |
| 4 | minor | fig mline-problem-bounce | (b) asks for 0–8 μs; the two offspring launched at 7.5 μs (−1.41 V on, +1.41 V back) were missing | added as cut segments (no arrowheads) with labels; caption says so |
| 5 | minor | fig mline-problem-bounce | "60" label sat on the z = 150 m probe line; caption "the only echoes are trapped on line 2" ignores the leaks through line 1 | label moved; caption: echoes bounce only on line 2, each leaks once through line 1 |
| 6 | minor | fig mline-junctions | unicode subscripts (Γ₁₂, Z₂) next to tspan subscripts, against the site's figure convention | all subscripts via `_sub` |
| 7 | minor | figs mline-burst, mline-bounce | panel title "the notes' margin plot" (it reproduces it); "no echo: R_L = Z₂" touched the load's dashed line | "as in the notes' margin plot"; note nudged left |

Everything else checked correct: all equations, signs (I = −V/Z₀ for leftward waves, current coefficients −Γ and 1 − Γ),
numbers, times, weights, the t_z form and the notes' (4n+1) form, DC checks, Example 1 algebra, shunt/series formulas and limits,
the 3 dB matching example, worked-problem tables and answers. Figures agree with the text (light, dark, 380 px phone; no overflow,
no KaTeX errors). `check.py` prints OK. Word counts within limits (abstract 89, On exams 108, Sources 85).

## Coverage verdict
Complete. Every notes item (p1–6: circuit, margin bounce diagram, Γ_jk/τ_jk and the subscript rule, the verification, Examples 1–3,
the series-R exercise with its hint, the margin plot) maps to a section; COVERAGE-L30 is accurate. Site additions are labelled.
Errata: both rows confirmed — "Z₂ = 2Z₂" (p1); "V(z,3 us)" label (p4): at 3 μs the front is at 450 m, and the plotted curve is a late
half-integer-μs snapshot (lattice: matches within 3×10⁻³). The "carried over from Lecture 29" guess is plausible: L29 notes p4 has a
"V(z,3)" plot.

## Conventions vs Lecture 28
No mismatch: z = 0 at the generator, +z toward the load, V upper wire vs lower, I along +z on the upper wire, Γ_L, Γ_g as voltage
ratios, current −Γ, τ_g = Z₀/(R_g + Z₀), z across / t down; L30's T₁, T₂ are L28's T per line (stated).

## Exams
Worked problem vs SP19 E3 #4 (scan p7: 1/3, 4/3, 650/9 V, 75 V) and FA23 E3 #3(a): new numbers, matched generator instead of
matched load (needs Γ₂₁, τ₂₁); no key carries over. On-exams callout gives methods. Borderline, left as is: the SP18 #1(vii) method
"check each discontinuity downstream, the load included" points at the answer, but it is the physics of the question.

## Unresolved
None.
