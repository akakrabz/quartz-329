# Independent review — Lecture 25 "Wave reflection and transmission" (build 9)

Files reviewed: `3-maxwell-and-waves/25-wave-reflection-and-transmission.md`, `concepts/reflection-and-transmission.md`,
`problems/working-back-from-a-transmitted-wave.md`, `figs_l25.py` (refl-setup, refl-gamma-tau, refl-interface-snapshot),
`COVERAGE-L25.md`, `ERRATA-L25.md`. Sources: notes pp. 1–6 (page images), L26 pp. 1–4 (boundary, J_s sign), Rao §5.6
(eqs. 5.101–5.106, Ex. 5.4), exam scans S17 HE3 #3, SP18 E3 #2, SP19 E3 #3.

Independent checks: `digest9/review_L25.py` → `review_L25.out`, **100 PASS, 0 FAIL** (written before reading the writer's
script). Covers: phasor Maxwell by finite differences for all three waves (lossy region 2) and for the worked problem's
x-travelling waves; H = û×E/η and every direction by `np.cross`; n̂×(E₁−E₂) = 0 and n̂×(H₁−H₂) = 0 at z = 0; Γ, τ from a
2×2 solve vs closed forms (random complex η₂, and complex η₁ for the On-exams remark); |Γ| ≤ 1 for Re η₂ ≥ 0; H ratios
−Γ, 1−Γ; n-form; time averages by quadrature vs ½Re{Ẽ×H̃*}; balance 1 = |Γ|² + |τ|²η₁Re{1/η₂} (500 random lossy cases;
net region-1 flux = S_i − S_r at every z, no cross term); e^{−αz} fields vs e^{−2αz} power; PEC limit (σ₂ → ∞, Γ → −1,
J_s = n̂×H₁ = x̂ 2E₀/η₁, and L26's depth integral σ₂τE₀/γ₂ → 2E₀/η₁); seawater with exact γ, η (σ = 4 S/m, ε_r = 81,
handbook values; exact η₂ = good-conductor value to 1e-5); quarter-wave coating by a 4×4 field solve (|r| = 5e-17; a
free-space λ₀/4 layer leaves |r|² = 0.5 %); notes' Example 1 (0.5/0.02/0.48 W/m²; 0.50035 with η₀ = 376.73 Ω); Rao Ex. 5.4;
figure arrows (screen-frame cross products) and snapshot continuity; worked problem end to end.

## Findings

| # | severity | where | what | fix |
|---|---|---|---|---|
| 1 | major | worked problem, statement and (c)–(f) | Two exam-key values carried over: the *given* amplitude \|H̃_t\| = 1/(20π) A/m is the S17 HE3 #3f answer (ŷ(1/20π)e^{−jπz/150}), and \|E_r\| = 1 V/m is the S17 #3d answer (SP18 #2e's is −1). Γ, τ, geometry differ, but a key should not reappear. | Amplitude doubled: H_t = ẑ(1/10π)cos(ωt+πx). Now E_t = −16ŷ, E_i = −14ŷ, E_r = −2ŷ V/m; H_i = ẑ7/60π, H_r = −ẑ1/60π (37.1, 5.31 mA/m); ⟨S⟩ = −x̂49/60π, +x̂1/60π, −x̂4/5π (−260, +5.31, −255 mW/m²); PEC E_r = +14ŷ, total H = ẑ7/30π, J_s = −ŷ(7/30π)cos ωt (74.3 mA/m). Γ = 1/7, τ = 8/7 unchanged (concept page still right). Writer's `verify_L25.py` §I updated to the new numbers (152 PASS). |
| 2 | minor | L25 On exams | "Numbers use η₀ = 120π, without a calculator": S17 HE3 allowed calculators. | "…; the Spring papers allow no calculator." |
| 3 | minor | L25 §4 Example 1 | "a negative Γ reverses both" — reverses relative to what was unstated. | "…from the Γ > 0 figure." |
| 4 | minor | L25 §2 | Brief: say once what the notes write; the notes' margin ± form of the BCs was not mentioned. | Parenthesis added. |
| 5 | minor | concept page, Physics | "A larger η₂ reflects E in phase (Γ > 0, τ > 1)" holds only for real η's. | "For real η's, …" |

No blockers. Everything else re-derived correctly: all phasors, exponent signs and the −Γ on H̃_r; Γ/τ derivation and
properties; PEC fields and J_s = x̂2E₀/η₁ (matches notes L26 p. 3); power formulas and the lossy-case proof; coating
(n_c = 1.22, 112 nm); seawater (δ = 7.96 m, Γ = −0.99983 + j0.00017, 0.033 %); Example 1; worked-problem directions
(n̂ = +x̂, E_t = η₂H̃_t×û, J_s along incident E). Scope: no standing-wave or radiation-pressure content beyond one line
each (L26). On-exams callout gives methods only. Figures (rendered light/dark at 820 px, page also at 380 px): arrows,
⊙/⊗, n̂, curves and markers agree with the text; no KaTeX errors, no overflowing displays.

Limits: lecture page 1,858 words (≤ 3,000), concept 426 (≤ 500), worked problem 892 (≤ 900); In one breath 88, On exams
114, Sources 100, captions 48–49. `check.py`: OK (140 pages).

## Coverage verdict
All 30 notes items in `COVERAGE-L25.md` are on the page and correctly represented (checked against each page image); the
notes' margin figure is redrawn with x up, y out (a proper rotation, checked). `ERRATA-L25.md`: all 7 items confirmed on the
page images; item 3 (λ inside the coating) is a clarification rather than a slip, and is numerically right.

## Unresolved / for the integrator
- `problems/index.md` does not yet list `working-back-from-a-transmitted-wave` (not an L25 file).
- Header wording differs slightly from L24's ("built from the course notes (no slides)" vs "slides: not available, built
  from the course notes"); cosmetic, left as is.
