# Review — Lecture 28 "Distributed circuits and bounce diagrams" (independent reviewer, build 11)

Files reviewed: `content-src/4-transmission-lines/28-distributed-circuits-and-bounce-diagrams.md` (2002 words),
`concepts/bounce-diagram.md` (492), `problems/reading-a-line-from-two-pulses.md` (810), `figs_l28.py` + `figs/bounce-*.html`,
`digest10/COVERAGE-L28.md`, `digest10/ERRATA-L28.md`. Notes pages 1–8 read as images; Rao §7.4; exam scans FA23 #4–#5,
S20 FE #5, SP17 #2(v)–(vi), #5.

Independent check: `digest10/review_L28.py` → `review_L28.out`, **50 PASS / 0 FAIL**. Three engines, none using the page's Γ formulas:
an exact characteristic (lattice) solver whose end conditions are solved from KVL/Ohm directly; a Yee FDTD of the telegrapher's
equations (Courant 1, resistive half-cell ends, smoothed step and Gaussian inputs); a phasor solution of the terminated line
compared with the Fourier transform of the §4 series (6 circuits × 4 ω × 5 z). Every quoted point checked: §4 V and Z₀I impulses at
ℓ/2, §5 load and midpoint staircases, DC V and I at every z, §6 table (open, short, matched load/generator, ideal source,
|Γ_LΓ_g| = 1), worked problem (a)–(g) incl. "nothing else arrives" and the next impulse at 4.6 μs, figure weights/curves/crossings.
Writer's `verify_L28.py` read only afterwards; its example constants updated for fix 1, re-run: 160/160 pass.

## Findings
| # | sev | where | what | fix |
|---|---|---|---|---|
| 1 | major | L28 §4–§5 examples, concept page, fig bounce-step | Example circuit Z₀ = 50 Ω, R_L = 50/3 Ω is S20 FE #5's (same Z₀, R_L; same V and I at ℓ/2, step, V_L/I_L), so the #5a key Γ_L = −½ carried over | Re-parameterized to Z₀ = 60, R_g = 180, R_L = 20 Ω: all coefficients and voltages unchanged, DC current 72 → 60 mA; figure constants + caption; writer's verify constants |
| 2 | major | L28 §4 after the series | "only the first few terms matter, unless both ends reflect totally": overstated (notes: "typically"); decay is slow for \|Γ_LΓ_g\| near 1 | "usually"; added the near-1 case |
| 3 | minor | L28 §4 example | Z₀I series ended "− …", but the next term is +1/64 (forward) | "+ …" (lattice C4) |
| 4 | minor | L28 On exams; concept page | "Every Exam 3 paper on hand has a bounce-diagram problem": false for Summer 2017–2020 HE3 | "Every spring/fall Exam 3 on hand (SP17–FA23) and the Summer 2020 final" |
| 5 | minor | L28 §3 intuition; concept page | "sees the source as a short circuit in series with R_g" mixes up the generator and its ideal source | "sees the ideal source as a short, leaving R_g alone" (Rao §7.4) |
| 6 | minor | L28 recipe step 4 | Step response = running sum of the dimensionless weights, with no V₀ | "V₀ times the running sum" |
| 7 | minor | L28 §2; COVERAGE #2 | Notes' V_L, I_L (p. 2, exams' wording) never named; coverage said "used in §6" (not true) | §2 names them; coverage corrected |
| 8 | minor | COVERAGE #27 | cites "erratum 4" (errata has 3 items) | "erratum 3" |
| 9 | minor | fig bounce-step | "1" and "1.2" tick labels crowded | "1" label dropped |

No blockers. Checked and correct: every sign and delay in §2–§4 (incl. the round trip 2(ℓ−z)/v), τ_g = (1−Γ_g)/2, DC
derivation box, current signs (−Γ for current; backward I = −V/Z₀), L25 analogy (η₁ → Z₀, η₂ → R_L, reflected H ↔ −Γ),
§6 table, traps, the 3 figures (rendered light/dark at 820 px and 380 px: no overflow, no KaTeX errors; labels, arrows, crossing
times 0.3T, 1.7T, … and staircases match the lattice), link anchors (L18 §4, L15 §5), check.py OK, word/callout limits
(breath ≤ 100, exam 118 with marker, sources 96).

## Worked problem
Re-parameterized properly from FA23 #4 (keys there: R_g = 50, R_L = 150, A = 15, ε_r = 36) and SP17 #2(v)–(vi): new numbers
(24δ, Z₀ = 75 Ω, 120 m, z = 30 m, negative echo −A/3), new parts (current, R_g change, step staircase, DC). Answers
(150 m/μs, ε_r = 4, 75 Ω, 37.5 Ω, 12 V·μs; 0.16 and +0.0533 A·μs; 18, −6, 3, −1, 0.5; 18/12/15/14/14.5 V; 14.4 V, 0.384 A) all
match no exam key and all verified. FA23 #5 (shorted line, 0 V / 4 A) not reproduced.

## Coverage verdict
Complete: all 28 notes items present and correctly represented (circuit, load condition, KVL and both epochs, footnote, Γ_g,
bounce diagram, series, |Γ| ≤ 1 remark, convolution remark). Erratum 1 (sign of the backward delay, p. 8) is correct
(review A8). Errata 2–3 are notation remarks rather than slips; acceptable as listed.

## Cross-lecture conventions (L29, L30: read only)
Both use the L28 conventions: z = 0 at the generator, +z toward the load, T = ℓ/v per line, τ_g = Z₀/(R_g+Z₀) and
Γ_g = (R_g−Z₀)/(R_g+Z₀) with the generator-side line's Z₀, voltage weights on diagrams, backward I = −V/Z₀. No mismatch found.

## Unresolved
None. Heads-up: the L28 example numbers changed (now 60/180/20 Ω, 60 mA). A practice item quoting the old 50/150/50/3 Ω or
72 mA would need the same change.
