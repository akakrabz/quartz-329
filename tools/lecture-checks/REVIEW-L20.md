# REVIEW — Lecture 20 (Poynting's theorem and monochromatic waves), independent review

Files reviewed: `3-maxwell-and-waves/20-poynting-theorem-and-monochromatic-waves.md`, `concepts/poynting-theorem.md` (new), `concepts/poynting-vector.md` (extension only: diffed against `stage/quartz`), `problems/energy-bookkeeping-for-a-radiating-sheet.md`, `figs_l20.py` (5 figures), `COVERAGE-L20.md`, `ERRATA-L20.md`. Sources: notes `329lect20.pdf` (all 7 pages; the p. 4 margin figure was re-read at 300 dpi), Rao §4.6 and §5.3, `exam3/EXAM3-CATALOGUE.md`, and the scans S20 HE3 p. 2, S19 HE3 pp. 2 and 6, FA23 p. 2.
Verification: `digest8/review_L20.py` → `review_L20.out`, **125 PASS / 0 FAIL**. I wrote it before reading the writer's `verify_L20.py`. It checks:
- the general theorem for fields built from arbitrary potentials, with ε(r) and μ(r) varying in space (residual 1e-11), plus a negative control with ε(t);
- the identity and the "six pieces", by complex step; the 1D route of the folded derivation;
- every number by quadrature or closed form, and every average against ½Re{ÃB̃*};
- every direction with `np.cross`;
- the figure curves parsed from the SVG paths and compared with the formulas, and the figure arrows parsed and compared with `np.cross` in the screen frame;
- WP stored energy = ∫(−J_s·E)dt at arbitrary t;
- no number in common with any exam key.

`check.py` prints OK. The figures were viewed in light and dark mode after the fixes, and no display overflows at 390 px.

## Findings (all fixed)
| # | severity | where | what | fix |
|---|---|---|---|---|
| 1 | major | L20 §7 "sunlight and a radio station"; `concepts/poynting-theorem` "Isotropic antenna" | The 1/r field and $E_0=\sqrt{2\eta_0\langle S\rangle}$ were stated for every r. They hold only far from the antenna: Rao's Ex. 4.4 says "far from a physical antenna". In the script, near a dipole (kr = 0.5) \|E\|/\|H\| = 1.12η, while ⟨S⟩r² stays exact. | Added the far-field condition and "an idealization" on both pages. The ⟨S⟩ ∝ 1/r² statement is kept, since it is exact. |
| 2 | minor | L20 abstract | Used η for the vacuum example, while §6–§9 use η₀. | η → η₀ (3 places). |
| 3 | minor | L20 header | The slides note was not bold; the brief and L21–23 make it bold. | Made it bold. |
| 4 | minor | L20 §3; poynting-theorem; ledger caption | "If charges move against E" / "pushes charges against E" is wrong for negative carriers. | Changed to "the current flows (is driven) against E". |
| 5 | minor | L20 §3 four-situation table | "charges create energy" | Changed to "the driven charges feed energy into the field". |
| 6 | minor | L20 §6 | "Away from the sheet the books balance only on average" reads as if the theorem held only on average. | Changed to "inflow and outflow match only on average". |
| 7 | minor | L20 §7 traps | "A sheet's power splits evenly" holds only with the same medium on both sides. | Added "(same medium on both sides)". |
| 8 | minor | L20 Sources | Listed Example 1 "with its margin figure", which the page does not redraw. | Reworded: the figure is Lecture 19's sheet picture, and its directions are given in words. |
| 9 | minor | fig `poy-energy-ledger` | S arrows ran through "w = ½εE² + ½μH²", "source" and "sink (heat)". | Arrows now start 6 px inside the boundary; labels and battery nudged. |
| 10 | minor | fig `poy-resistive-wire` | The label "E = J/σ" ran into panel 2's "0.5" tick ("E = J/σ 0.5"). | Panel 2 moved 14 px right. |
| 11 | minor | fig `poy-time-average` panel 2 | The title says "S at one point", but the travelling wave was drawn for z = 0 and the standing wave for z = λ/8. | Both curves now at z = λ/8: the travelling wave is cos²(ωt − π/4). Title, legend and caption updated. |

No blockers. All of these are correct:
- every equation, number, sign, direction and unit on the four pages;
- in all 5 figures, the curves (from the formulas) and the arrows (E×H; H = ½J_s×n̂ with n̂ toward the field point; E = −(η/2)J_s(t−|ξ|/v));
- the ½ factors and the e^{−2αz} pointer.

Scope: no phasors (only forward pointers to L21), lossless media only. The worked problem is re-parameterized from S20 HE3 #2(c)–(d): plane x = 0, current along −ẑ, cos, 2 MHz, 3 A/m, ε_r = 2.25. Its answers (−180π, 90π, 4.5 µs at 900 m, λ = 100 m) share nothing with the key (−480π, 240π, 2 µs at 600 m, λ = 300 m). The sea-water example (1 and 0.5 W/m³) shares nothing with the S19 HE3 #1b keys either. The `On exams` callout gives methods only.

## Coverage verdict
Complete. All 32 notes items in `COVERAGE-L20.md` are on the page and correctly represented:
- the derivation and its underbraces;
- the three terms with their units;
- the source sign and the vi analogy;
- Example 1 (a)–(c);
- "monochromatic";
- the cos² identity and the averages;
- 60π/120π given as approximate values;
- the closing balance.

The margin Maxwell list and the margin figure are covered by reference to Lectures 16 and 19, with the directions given in words. The three slips in `ERRATA-L20.md` are confirmed: the missing "see"; H⁺ unlabelled but drawn correctly toward −ŷ; 60π/120π written as equalities.

## Unresolved / for the coordinator
- The Lecture 19 header (not my file) still reads "next: Lecture 20, Poynting theorem and monochromatic waves (coming)". It should now link to the Lecture 20 page.
- Cosmetic, site-wide (shared `haxis`/`vaxis` helpers): the vertical-axis "0" tick label is crossed by the horizontal axis line in the poy- plots, as in earlier lectures. Left as is.
