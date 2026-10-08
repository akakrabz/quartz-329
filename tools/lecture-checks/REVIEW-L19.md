# REVIEW — Lecture 19 (independent physics and policy review, 2026-10-07)

Scope: `3-maxwell-and-waves/19-dalembert-solutions-and-radiation-from-current-sheets.md`, `figs_l19.py` (4 figures),
`concepts/current-sheet-radiation.md`, `concepts/poynting-vector.md`, the L19 sentences in `concepts/plane-waves.md` and
`concepts/intrinsic-impedance.md`, `problems/a-current-sheet-launches-two-waves.md`.
Checks: `digest7/review_L19.py` → `review_L19.out`. It runs finite-difference Faraday and Ampère–Maxwell checks on every (E, H) pair:
the notes' sheet (εr = 2.5), the slides' sheet, Ex. 1, slide 17, the §7 cosine, §8's x-sheet, and the worked problem (all residuals ≤ 1e-6).
It also checks the jump and continuity conditions, uses np.cross for every H, E×H and S, and recomputes every number.
Preview screenshots were taken in light and dark (`preview/r19/shots/`); scrollWidth is 820 and there are 0 KaTeX errors. `check.py` prints OK.

## Findings and fixes
| # | Sev. | Where | Finding | Fix |
|---|---|---|---|---|
| 1 | blocker (policy) | problem page, all parts | The "re-parameterized" problem (J = ŷJs on x = 0) gave **H = −½Js ẑ forward, +½Js ẑ reverse**. That is exactly the SP18 Exam 2 #5 key (same unit vector, same signed coefficients), so the key carried over. | Re-parameterized the current to **J = ẑJs(t)**. Now H = ±½Js ŷ for x ≷ 0 and E = −(η/2)Js ẑ. Rewrote (a)–(e), the traps, the answers, the probe record (now inverted) and S = (−282.5ẑ)×(1.5ŷ) = +424x̂. Updated the figure and the two concept-page examples. |
| 2 | blocker (policy) | L19 "On exams" #5 | The callout stated the key: the directions and coefficients of H for both waves. | Rewritten to give what is asked plus the method (½J×n̂ per side, delay, E×H check, landmark placement), with a pointer to the worked problem. No answers. |
| 3 | blocker (policy) | L19 §7 example "SP18 Exam 2 #1(vii)" | Used the exam's numbers (3π rad in 10 µs) and gave the answer (2000 m, "option (e)"). | Re-parameterized: 4π rad in 5 µs gives ω = 8π×10⁵ rad/s, f = 400 kHz, λ = 750 m. The example is framed as the skill the exam tests. #4 has no answers on the page, so it was left as is. |
| 4 | major | fig `sheet-space-time` footer | "A, at the front, arrives first" is backwards. For a +z wave the front is at large z: E and D cross z = 0 first (t = −4, −3 s) and A crosses last (t = +1 s). | Changed to "E and D (the front) cross first, A last". |
| 5 | major | `concepts/poynting-vector` trap | It claimed that for counter-propagating waves the S cross terms do not vanish. They cancel identically for any polarizations (checked numerically); co-propagating waves are the non-additive case. | Trap rewritten: same direction gives û\|E₁+E₂\|²/η; opposite directions give û(\|E₁\|²−\|E₂\|²)/η. |
| 6 | minor | L19 §6 slide 11(a) | It said "zero crossing on the rising edge". The crossing is on the B–C edge, which falls in z. | Changed to "between B and C (the falling edge in z)". |
| 7 | minor | L19 §7 key callout; poynting trap | "Phasors arrive … in Lecture 20" broke the site convention (phasors are Lecture 21). | Now reads Lecture 21; time averages stay in Lecture 20. |
| 8 | minor | L19 §4 | "The ink marks the two places students slip" claimed more than the ink shows. | Attributed to the blue ink on slides 5 and 7; the "slip" remark is now marked as the site's own. |
| 9 | minor | current-sheet concept trap | "A snapshot on the +n̂ side is … mirrored" was ambiguous (n̂ flips from side to side). | Now says the snapshot is mirrored against distance from the sheet, and against the coordinate only on the + side. |
| 10 | cosmetic | slide 17 callout title | The preview renderer cut the title at "$y = 0$:". | Title rephrased without the colon. The heading is unchanged, so anchors are safe. |
| 11 | cosmetic | problem figure icon | The labels were crowded. | Sheet drawn with ⊙ current marks, H arrows up/down, E ⊗; the "front" label moved. Every direction re-checked by cross product. |

## Verified correct (no change)
- Notes' and slides' sheet forms. Recipe ½J×n̂ and −(η/2)J. BCs ẑ×(H⁺−H⁻) = Js, E continuous. Ex. 1 (both sides of Faraday −6.671e-3 T/s).
- Ex. 2 ratios (3.34e-3, 0.667). Ex. 3 and Ex. 4 numbers, including the spot check at z = 700 m. Slide 17. Slide 11(b, c).
- 100 MHz: β = 2.094 rad/m, λ = 3.00 m. Peak S per side η₀/4 = 94.2 W/m²; the two sides together equal −J·E.
- §8 at plot scale: (a) H(400 m, t) is a 2 A/m step at 2 µs falling to 0 at 7/3 µs; (b) the H(x, 4 µs) profile; (c) E ∥ −ẑ with peak −2η₀ = −754 V/m; (d) J = ẑ12(1−t) for 2/3 < t < 1 µs.
- §9 line picture E = ηJs/2. Worked-problem values: η = 188.4 Ω, levels ±3/±1 A/m, +188/−565 V/m, max |S| = 1.70 kW/m².
- The SP18 #5 waveform and instant (ramp to ±4 A/m, t = 5 ns) differ from the problem's (6/−2 A/m, t = 6 ns).
- Figures 1 and 2: ⊙/⊗, arrows and pulse positions all agree with the physics.

## Unresolved / for the owner
- §8 uses the plot's scale (peak 2 A/m), says so, and gives the ×100 rule. Which of the two the instructor intended is unknown.
- `figs/sheet-slab.html` is not produced by `figs_l19.py`; it was not reviewed.
- A practice page `practice/19-…` is being written in parallel. If it reuses the old worked-problem fields (H_z, E_y), it needs the same re-parameterization.

## Errata candidates (course sources)
- Slides L19 S18–S21: the stem's H = 2x[u(x)−u(x−100)] A/m peaks at 200 A/m, but the plot is labelled "2" (×100). S18–S21 also leave the medium and the direction of Js unstated.
- Slides L19 S6: a stray small "H_y = (A/η₀) f(t)" with the wrong sign sits in the z = 0⁻ column, where E_x(0⁻) = Af(t) belongs.
- Slides L19 S7: â_n and region 1 are not identified (â_n = â_z, region 1 is z > 0). S2 writes J_x(t) where the rest of the deck writes J_s(t). On S15/S22, f is both the waveform and the frequency.
- Notes L19 p.4–5, Ex. 3: H is asked for but never given. The p.4 margin plot labels the ordinate "V" instead of V/m. p.9: η₀ = 120π is written as an equality.
- Exam catalogue: SP18 E2 #5 and #1(vii) are tagged "beyond L15"; they belong to L19 (with L18 and L13).
