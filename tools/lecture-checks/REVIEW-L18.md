# REVIEW — Lecture 18 (wave equation, plane TEM waves): independent physics review, 2026-10-05

**Scope.** `3-maxwell-and-waves/18-the-wave-equation-and-plane-tem-waves.md`; `figs_l18.py` → `figs/wave-*.html` (5 figures); `concepts/wave-equation.md`, `plane-waves.md`, `intrinsic-impedance.md`; `problems/a-pulse-on-the-move.md`; today's edits to `concepts/displacement-current.md`, `concepts/faradays-law.md` and `problems/coax-inductance-and-the-lc-product.md`. Faithfulness was checked against `digest6/DIGEST-L18.md`, and the exam against `sources/EXAM-CATALOGUE.md` and `sources/txt/329sp18_exam2.txt`.

**Method.** I wrote and ran `digest6/review_L18.py` (output in `review_L18.out`) before opening the writer's `verify_L18.py`. It runs 90 checks, and all pass after the fixes.
- Finite-difference residuals of Faraday's law, Ampère–Maxwell and both divergences, for the four sign-table pairs, the Af + Bg superposition, a plane wave along a random û, and the worked problem's (E, H) in SI units. All residuals are at most 1e-8. Deliberately wrong signs fail at O(1): +x̂ for the y-polarized +z wave, +Bg in H_y, and −x̂ in the problem.
- A time-varying z-integration "constant" fails Faraday's law, and ∇·(ẑ f) = −f′/v.
- Numerical 3D Laplacian of E and H, and the curl-curl identity.
- np.cross for every E×H, û×E/η and E = ηH×û.
- The ξ/ζ factorization; speeds from v = −(∂tφ)∇φ/|∇φ|²; the shift identities and the mirror rule.
- Every number: c, η₀, 120π, the 1 V/m example, ε_r = 4, 9 and 2.25, μ_r = 2 with ε_r = 8, the coax and plate √(𝓛/𝓒), 50 Ω, the slide-26 values with both signs, and every position, record and reading in the worked problem and its variant.
- Screen-frame cross products for every drawn arrow.

The writer's `verify_L18.py` (164 PASS) agrees. I rendered all five figures and looked at each in light and dark: every arrow, ⊙/⊗, axis label and pulse position is right. There are no KaTeX errors and no sideways scroll at 390 px. `check.py` prints OK.

**Result.** I found no wrong equation, sign, direction, number or unit anywhere, figures included. The fixes below correct misleading statements, one attribution to the slides, and one flaw in the problem's design.

## Findings and fixes
| # | Sev. | Where | Problem | Fix |
|---|---|---|---|---|
| 1 | major | L18 "In one breath", §1, §8 | "Static fields need sources, so no static field survives there" was said of a source-free *region*. That is false: a charge-free region can hold the static field of charges outside it (a capacitor gap; the Laplace problems of L5–7). The Helmholtz argument needs zero divergence and curl *everywhere*. | Reworded: a static field in the region can only come from outside sources and vanishes with them. Helmholtz now says "everywhere in space"; the summary says "with no sources anywhere". |
| 2 | major | problem statement and (d) | The statement said "lossless dielectric", which settles the (d) true/false ("must be a conductor") by the premise alone. The opening sentence also echoed the exam's wording. | Now "a uniform, non-magnetic medium". (d) first infers that the medium is lossless from the unchanged shape, then uses v = c/√(μ_rε_r). Description and opening sentence reworded. |
| 3 | major (attribution) | L18 §5 | The page said the slides set the z-integration constant to zero, quoting "we can turn off our source". Slide 21 drops it without comment; the quote is from slide 9 and is about E_y (digest B.7 #7). | Attribution corrected. |
| 4 | minor | L18 §5 example | "Not small in the sense that matters: η₀, not 1, is the natural ratio of E to H" was muddled. | E and B have different units, so "small" means nothing between them; in a wave E/B = c (E/H = η₀). |
| 5 | minor | L18 "In one breath" | H was "smaller by the intrinsic impedance", which makes no sense across different units. | Now \|H\| = \|E\|/η. |
| 6 | minor | L18 §4 | "Every frequency travels at the same v because v depends only on μ, ε" holds only if ε does not depend on frequency. The page also cited "Lecture 23" alone. | Added the dispersion caveat (Lorentz model, L11) and changed the citation to "Lectures 22–23". |
| 7 | minor | plane-waves trap; problem (e) trap | "The ±z sign table does not carry over by relabelling letters" is too strong. A cyclic relabelling (det +1) carries it over; swapping two letters reverses H. | Both reworded; checked with permutation matrices. |
| 8 | minor | intrinsic-impedance | "η is always positive" contradicted "η becomes complex" two sentences later. | Now "in a lossless medium η is a positive real number". |
| 9 | minor | L18 §3, §4; end of problem page | ±½J_s ŷ lacked "for z ≷ 0". "E_y uniform" lacked "and constant in time" (from Ampère's y-component). "In time units" was unclear. The exam was described as "at c in vacuum", but it gives only v = −c x̂ and asks whether the medium conducts. | Added the missing conditions; "In time units" became "In handy units"; the exam description now says "at c". |
| 10 | minor | L18 "Sources" | The slip in the notes' p. 8 margin was not listed. | Added. |

**Checked and left unchanged.**
- Every equation and sign in §§1–7 and on the three concept pages: the sign table, the shift identities and the mirror rule, the S24 and S26 solutions, §7's numbers, and the cable link.
- The small edits to displacement-current, faradays-law and the coax "Plane-wave twins" paragraph.
- The "(14 pts)" label, confirmed in the exam text.
- Rounding: polyethylene η appears as 251 Ω (η₀/1.5 = 251.2) and as 251.3 Ω (80π, from v = 2×10⁸ exactly). Each is stated with the route that gives it.

**Exam numbers.** No given value reproduces SP18 E2 #4, whose givens are 3 V/m, an edge at x = 100 m, a 50 m decay, t = 1 µs and v = −300 m/µs. The problem uses a ramp of 0.02 V/m² on 400–700 m, at 3 µs, moving +y at 200 m/µs through a dielectric. Two positions coincide in other roles: the given ramp start (400 m) equals the exam's answer-(a) edge, and the answer-(a) front (100 m) equals the exam's given edge. I judged this acceptable and left it. Parts (c) and (e) are new.

**Unresolved.** Nothing blocking.

## Slips in the course materials (errata page; from the digest, with locations)
- Slides S2, S3, S8, S9, S10: d/dt for ∂/∂t in the point forms, including the boxed ∂E_x/∂z = −μ₀ dH_y/dt on S8 and S10. Minor; it recurs from L14–16.
- Slide S5: the static-sheet sketch draws **H** for a current *out of* the page, which is opposite to S4's **J**_s = −J_s(t)â_x and to S6–S11. This is inferred from the axis icon. Minor (figure).
- Slides S4 → S11–S13: J_s(t) is renamed J_x(t), and J_x is then reused as the volume-density component in ∂_zH_y = −J_x − ∂_tD_x, without the −δ(z). Notation only; the term is dropped "for now" on S14.
- Trivial or cosmetic:
  - S11 ink "progation";
  - S22 writes "= 3×10⁸" as an equality;
  - S18: "two first order diff eqns that each can be a solution";
  - S21 drops the integration constant without comment;
  - the S26 t-axis has no units;
  - S24 and S26 cite an unnamed "old book".
- Notes p. 8 margin: the shifted rect and triangle plots label their edges −τ/2 and τ/2 instead of t_o ∓ τ/2. Minor (figure).
- The digest found no arithmetic or sign errors in either source.
