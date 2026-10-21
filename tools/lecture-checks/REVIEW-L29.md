# Independent review — Lecture 29 "Bounce diagram examples" (build 11)

Files reviewed: `content-src/4-transmission-lines/29-bounce-diagram-examples.md` (1,768 words after fixes),
`content-src/problems/a-ramp-pulse-meets-its-echo.md` (889), `figs_l29.py` + `figs/bex-*.html` (4 figures),
`digest10/COVERAGE-L29.md`, `digest10/ERRATA-L29.md`. No concept pages for L29.

## Verification
`digest10/review_L29.py` → `review_L29.out`: **72 PASS, 0 FAIL**. Written before opening the writer's scripts.
- Two independent steppers that use only circuit laws at the ends (no Γ formulas): method of characteristics
  (KVL `f_i = R_g I + V` at z = 0, `V = R_L I` at z = ℓ; exact on its grid) and a Yee FDTD of the telegrapher's
  equations with lumped half-cell ends (S = 1 for R_g = 0 or R_g = Z₀; S = 0.5 for R_g = 25 Ω, where S = 1 holds an
  odd-even mode after a jump).
- Checked: every coefficient and delay; Example 1 V and Z₀I at 1, 2, 4.5, 6, 7, 10 μs, fronts at 300/600 m, echo front at
  450 m, load voltage ⅔ sin ω(t−3), steady state ½ sin(ωt−βz) + ⅙ sin(ωt+βz) with envelope ⅓…⅔ and maxima every 150 m incl.
  the load; Example 2 crossing times, weights, V levels 1, 4/3, 1, 8/9, 1, 28/27, 1, I levels 20 … 9.6 mA, error ratio −⅓,
  DC 1 V / 10 mA at 400 μs; Example 3 series vs MoC at six times, all plateaus/edges at 3, 9, 11 μs, V/I = R_L at 9 μs; the
  §1 snapshot series on a generic circuit (Z₀ 75, R_g 30, R_L 400, triangle pulse); worked problem (a)–(d) incl. the
  generator-end KVL; every figure curve (`figs_l29.series`) and diagram weight (`legs`) against the MoC.
- Afterwards compared with the writer's `verify_L29.out` (134 checks): no disagreement.

## Findings
| # | severity | where | what | fix |
|---|---|---|---|---|
| 1 | major | L29 §1 (horizontal cut) and Summary bullet 1 | "It meets every segment still in flight at t_p" — wrong for inputs with duration. At 4.5 μs (Ex. 1) the cut crosses only the echo, yet the forward burst fills z < 450 m; at 9 μs (Ex. 3) forward segment 0 ended at 8 μs but its 2 V part is on 2250–2400 m. A student following the rule drops terms (checks D2, D3; Rao Ex. 7.5 uses the same "last T plus duration" rule) | "Every segment that has started by t_p carries its own copy of f_i. The copy trails its segment by the input's duration, so a segment the cut no longer crosses can still contribute (Example 1 at 4.5 μs, Example 3 at 9 μs)"; Summary: "one copy of f_i per segment started by t_p, including segments the cut has already passed" |
| 2 | major | worked problem (c) | "Two segments are in flight" at 3.5 μs: only the echo segment is in flight; the forward ramp's tail is what remains (same misconception as #1) | "Two segments contribute. The cut crosses only the echo, but the forward ramp's tail is still arriving." |
| 3 | minor | bex-example3 | panel c's z tick labels (1350, 1650, 1950, 2400) clipped by the SVG bottom (H = 420) | H = 434 |
| 4 | minor | bex-example3 caption | "b: the 2 V part meets the echo of the 1 V part" — the 2 V part overlaps its own echo (§5 example) | "b: near the load the 2 V part overlaps its own echo; the 1 V part's echo heads left" |
| 5 | minor | bex-ramp-problem | panel/cut letters a–d clashed with problem parts (a)–(d): panel "d, t = 5 μs" belongs to part (b) | cuts labelled 2, 3.5, 5; panels "t = 2 μs, part (b)", "t = 3.5 μs, part (c)", "t = 5 μs, part (b)"; caption by time |
| 6 | minor | L29 §2, last bullet | β used without definition | "with β = ω/v" |
| 7 | minor | L29 §4 trap | "Once an echo has passed" (reads as "gone") | "has arrived" |

No blockers: every equation, sign, direction, number and unit on both pages is right; figures agree with the text
(viewed light, dark and at 380 px; no overflowing displays). `check.py` OK; word counts within limits (abstract 93,
On exams 106, Sources 87).

## Coverage verdict
Complete. All 30 notes items (4 page images re-read) map to the page as COVERAGE-L29 states; only the class-calendar
animations are omitted (not available). Errata 1–3 confirmed on the images (p. 3 "in Example 1", p. 4 "described in
Example 1", margin label "v(4,t)"); remarks N1–N4 accurate.

## Conventions, exams
- Matches the Lecture 28 page: z = 0 generator, +z toward the load, T = ℓ/v, τ_g = Z₀/(R_g+Z₀), Γ_L and Γ_g as voltage
  ratios (current −Γ), I along +z on the upper wire, backward segments flip the current sign, diagram z across / t down,
  segment numbering n of L28's impulse-response box. No mismatch to report.
- Worked problem vs SP17 E3 #5c (solution scan p. 8): different ℓ, v, R_g, R_L, Γ signs and input (ramp vs sine); only
  Z₀ = 50 Ω and one snapshot time (2 μs) coincide — no key carries over. On-exams callout cites catalogue ids correctly
  and describes methods only.

## Unresolved
None.
