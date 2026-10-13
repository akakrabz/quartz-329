# Review — Lecture 22 page set (phasor Maxwell equations, damped waves in conducting media)

Reviewed: `3-maxwell-and-waves/22-phasor-maxwell-equations-and-damped-waves.md`, `concepts/propagation-constant.md`,
`concepts/intrinsic-impedance.md` (new section), `problems/decoding-a-damped-wave.md`, `figs_l22.py` (4 figures), against
the notes (pp. 1–8, page images), Rao §5.3 (eqs. 5.54–5.66, Tables 5.1/5.3), the Exam 3 catalogue and scans (SP17 #3,
S18 HE3 #1b, SP19 #1, S20 HE3 #3), Lectures 8/10/11/15/16/18/19/21 and the Lecture 23 page (read, not edited).
Independent check: `digest8/review_L22.py` → `review_L22.out`, **382 PASS / 0 FAIL** (written before reading verify_L22.py).

## Findings (0 blockers, 2 majors, 7 minors — all fixed)
| # | sev | where | what | fix |
|---|---|---|---|---|
| 1 | major | L22 §4 trap "β is never smaller than α", §6 "β against α"; propagation-constant description and body | "β ≥ α in every passive medium" / "cannot hold in any passive medium" is contradicted by the page's own §8: a collisionless (lossless, passive) plasma below f_p has real γ, β = 0 < α (script H8). It holds for real σ (C, D: s = 1e-6…1e6). | Restricted to real σ; the plasma named as the exception (imaginary σ). |
| 2 | major | L22 §6 "δ against λ" | '"λ is longer than δ" is telling you the regime' is false: λ/δ = 2π tan τ, so λ > δ needs only σ/ωε > 0.33 (true at 0.5, in between). The decisive tests are δ ≫ λ and λ ≈ 2πδ (S20 HE3 #3b's wording); λ < 2πδ always (H5). | Rewritten with λ/δ = 2π tan τ < 2π and the 0.33 caveat. |
| 3 | minor | L22 §4 trap "phase of H"; intrinsic-impedance trap | "In a passive medium H lags E, never the reverse" — true for real μ, ε, σ; magnetic loss can give τ < 0. | "With real μ, ε and σ". |
| 4 | minor | L22 §3 key | "Lecture 18's γ = jω√(με)": L18 has neither γ nor β. | "the lossless γ of §2 and Lecture 18's η". |
| 5 | minor | L22 §3 "One ratio decides" | "ε/σ ≈ 0.18 ns in Lecture 8": L8 says ≈ 0.2 ns. | "0.18 ns, which Lecture 8 rounds to 0.2 ns". |
| 6 | minor | L22 §6 key | Notes p. 6 name "lousy" conductor missing (coverage map claims it; L23 cites it as L22's). | Added. |
| 7 | minor | fig `lossy-regimes` | \|η\| panel labels quote \|η\| values on a \|η\|/√(μ/ε) axis; "(α = β)" and "coincide" state an approximation as exact. | "\|η\| ≈ …", "\|η\| → …", "α ≈ β", "nearly coincide"; module re-run. |
| 8 | minor | fig `lossy-damped-wave` | "λ = 2π/β (two nodes apart)" ambiguous for a span of two node spacings. | "(two node spacings)". |
| 9 | minor | worked problem, description | "H given instead of E" as a changed detail, but S18 HE3 #1b (one of its three models) also gives H. | "H given rather than E (as only the Summer 2018 paper does)". |

## Verified correct (no change needed)
- **Closed forms** α, β, \|η\|, τ = ½tan⁻¹(σ/ωε), ∠γ = 90° − τ, α/β = tan τ, σ/ωε = tan 2τ = 2αβ/(β² − α²),
  \|γ\|\|η\| = ωμ, β² − α² = ω²με, 2αβ = ωμσ, α² + β² = ω²με√(1+s²): equal to the exact principal roots to 1e-8 for s = 1e-3…1e3.
- **Branch:** principal roots give α ≥ 0, β > 0, Re η > 0, 0 ≤ τ < 45° for 241 media (s = 1e-6…1e6); γη = jωμ and
  γ/η = σ + jωε to 1e-12; −γ breaks the product rule; ε_c = ε − jσ/ω form identical; σ = 0 gives +jβ; margin μ, σ, ε.
- **Maxwell:** finite-difference curls of the §4 phasors (±z, complex E₀, μ_r = 1 and 3, sea water) and of the time-domain
  fields (incl. ∇²E = μσ∂E/∂t + με∂²E/∂t²); Helmholtz and H̃_y = ±Ẽ_x/η for σ = 0; ∇·∇× = 0; ρ̃ = 0 from (σ + jωε)ρ̃ = 0.
- **Which field lags:** H peaks τ/ω after E at a fixed point; in a snapshot H's zero crossings sit τ/β toward the source
  (both directions, two media). ⟨S⟩ by quadrature = ½Re{Ẽ×H̃*} = û\|E₀\|²cos τ e^{−2αd}/(2\|η\|) (np.cross); 37 %, 13.5 %, 8.686 dB.
- **Examples:** §2 lossless (FD curl, 10.6 mA/m, directions); §5 decode (12π(3+j), 50.3 mA/m, σ = 1/20π, ε = 8ε₀, back-check);
  §6 crossover (3.43, 8.28, 158.5 Ω, 10 %/9 %/55 %/36 %); §6 table (20 entries); quick tests; error orders O(s²), notes'
  angle O(s³); §7 sheet (jump with n̂ = ẑ from 2 into 1, ½J̃s×n̂, 36π W/m² by quadrature, 56.5 each side; = Rao 5.66);
  §8 Drude 1.6e-4, plasma f_p = 8.98 MHz, δ = 6.4 m, 0.375 vs 0.419 rad/m, imaginary η, ⟨S⟩ = 0; §9 coax twin.
- **Worked problem** (a)–(f) and the μ₀ variant: all numbers; Faraday and Ampère by FD on the phasors and on the answer's
  time-domain E; −ŷ = ẑ×(−x̂); E leads H by 26.57°. Keys differ from SP17 #3, S18 HE3 #1b, SP19 #1 (only α = 1 coincides with S18).
- **Concept pages:** all numbers. **Figures:** every plotted quantity recomputed (nodes 2.75 → 2.875, spiral sense and
  0.19/turn, dial table and the "inverted and reflected" construction, regime asymptotes); rendered light/dark
  (`preview/r22/shots/`): no overlaps or clipping; no horizontal scroll at 820 px or 390 px. `check.py`: OK.
- **Lecture 23 agreement:** L23's polar forms = L22's closed forms; L23's α = σ\|η\|/(2cos τ) exact; thresholds 0.1/10 =
  L22 figure bands; L23 accuracy figures at p = 0.1, 1, 10; sea-water f_c 0.89 GHz; regime-table rows = L22 overview.

## Coverage verdict
Complete. Every bullet, equation, margin set, case and figure of notes pp. 1–8 is on the page (checked item by item against
the images and COVERAGE-L22.md); the one gap ("lousy" conductor) is fixed. ERRATA-L22 rows confirmed on the images. Scope
is right: L22 gives the regimes as an overview and leaves materials, power loss and the table to L23.

## Unresolved / for the maintainer (not my files)
- `exam3/EXAM3-CATALOGUE.md` L22 traps: "μ ≠ μ₀ … changes η and σ/ωε". For a given γ, σ/ωε = 2αβ/(β² − α²) does not
  contain μ (script I, variant). The site pages state it correctly.
- Symbols across pages: L23 writes p = σ/ωε; L22 uses p for the notes' binomial exponent and s, x in its figures.
  Each page defines its own; harmless but worth unifying when L23 is next touched.
- The SP17 Exam 3 key (scan p. 5) writes γ = 3 + 4j "rad/m" (should be m⁻¹); not on the errata page yet.
- Phase-dial figure marks s = √3 (τ = 30°), which is SP19 #1d's value: a generic 30-60-90 relation, left as is.
