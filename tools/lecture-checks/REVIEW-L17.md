# REVIEW — Lecture 17 (magnetization, Maxwell's equations in matter)

Independent reviewer, 2026-10-05. Own checks: `digest6/review_L17.py` → `review_L17.out` (78 OK, 1 FAIL = finding 4). All 5 figures rendered (`preview/r17`) and inspected in light and dark mode, with every ⊙/⊗, force, torque and angle checked against `np.cross`. I compared with the writer's `verify_L17.py` only after that. `check.py`: **OK** (106 pages, 1946 links, 18 513 math). Files edited: L17 page, L16 page, `concepts/permeability.md`, `problems/fields-across-a-magnetic-interface.md`. No figure needed changing.

## Findings and fixes
| # | sev | where | finding → fix |
|---|---|---|---|
| 1 | major | L17 §5 values table; `permeability.md` | Three of the slide values are physically wrong but appeared as fact. Pt is +2.9e-5 on the slide; the handbook value is ≈ +2.7e-4. Liquid O₂ is +3.5e-5 on the slide, ≈ +3.5e-3 at 90 K. Ag is μr 0.99993 (χm −7e-5) on the slide, ≈ 0.99998 (χm −2.4e-5) by the handbook. The slide-15 scan itself prints 0.99993 for both Ag and Pb, so the digest read it correctly. → I kept the slide numbers (faithful to the course) and added a flagged note under the table. "Every dia-/paramagnet < 1 part in 10³" now applies to the table only. `permeability.md` drops Pt, and its "\|χm\| < 10⁻³ for every…" now reads "ordinary…, LOX ≈ 3.5e-3". |
| 2 | major | L17 table header | Misattribution: the header said the slides give χm for dia/para and μr for the rest. In fact only Cu, water, Al, Pt and LOX are typed as χm (s12–13); Bi, Ag and Pd are μr from s15. → header corrected. |
| 3 | major | L16 "Two perfect dielectrics" | "Fields refract … but nothing jumps" contradicts refraction: Eₙ and Dₜ jump when ε differs. → rewritten: no surface source, but Eₙ and Dₜ change by the permittivity ratio. |
| 4 | minor (number) | L17 §2 Bohr example | The printed inputs (a₀ = 5.29e-11, v = 2.19e6) give I = 1.056 mA (not 1.05) and m = 9.28e-24 (not 9.27e-24). The writer's check used exact constants. → "≈ 1.06 mA", "≈ 9.28e-24, = μB = 9.27e-24 to the rounding". |
| 5 | minor | L17 §5 diamagnetism | "atoms with no permanent moment — filled electron shells: copper, bismuth" is wrong: free Cu (4s¹) and Bi (6p³) atoms are not closed-shell. → "where no permanent moments outweigh it — water, wood, glass, Cu, Ag, Bi". |
| 6 | minor | L17 §2 | "In most atoms the electrons pair up" (about half the elements have odd Z) → "in filled shells and most chemical bonds". |
| 7 | minor | L17 §5 hysteresis | "B stays at the remanence" (as if B stayed at saturation) → "falls back only to the remanence". |
| 8 | minor | L17 §4 core trap | The demagnetizing field makes H smaller only for χm > 0; in a diamagnet H is slightly larger (checked with 3H₀/(μr+2)). Also "∇×H = J_free" → "+ ∂D/∂t when fields vary". |
| 9 | minor (attribution) | L17 §4, §5 end | The inductance evidence is in the notes' text (p. 8); fn 3 only recalls L ∝ μ. The notes call the χm resonances "relevant for … magnetic imaging techniques", but the page said they "are the basis of MRI". → both reworded. |
| 10 | minor | L17 §7 dictionary | Added "Eₜ (always)" to match "Bₙ (always)". |
| 11 | minor | problem page, trap (a) | "the slip the FA26 key made" → "appears, struck out, in the FA26 key" (matches the dielectric page). |

## Re-derived and correct (unchanged)
- **Curls and magnetization current.**
  - Curls: Mz(x)ẑ → −∂Mz/∂x ŷ; M₀x/d ẑ → −(M₀/d)ŷ; uniform slab → 0.
  - Loop-lattice leftover current = −dM/dx.
  - Thin-layer ∫∇×M dn = M×n̂: slab faces ∓9.9ŷ, rod side Mφ̂ (ends 0), interface n̂×(M₁−M₂) = (−12,−16,0); twin −∇·P → P·n̂.
- **Torque.** Discretised square and circular loops give F = 0 and T = m×B = Iℓ²B sinθ x̂, which turns m toward B. x̂×û = m̂, so the circulation sense is right.
- **Order-of-magnitude numbers.**
  - Iron: N 8.49e28, M_sat 1.73e6 A/m, μ₀M_sat 2.18 T.
  - Permanent magnet: M 1.03e6 A/m.
  - Cu: 2.46e21 e⁻/mm³.
  - kT/(μB·1 T) = 447.
- **Coil and core.**
  - Coil: H 2000 A/m, B₀ 2.51 mT, μ₀M 0.249 T, B 0.251 T; 12.6 T for μr 5000.
  - Inductance: L 12.6 μH → 1.26 mH.
  - Sphere: H₀−M/3 = 3H₀/(μr+2), B < 3μ₀H₀.
- **Slab between sheets.** H = 0.1x̂ A/m, B = 12.6 μT, M = 9.9x̂ A/m. The four-sheet vacuum formula gives B/μ₀ = 10 in the slab, 0.1 in the gap, 0 outside.
- **Interfaces.**
  - Iron refraction 0.131° and 6.54°.
  - Interface problem (a)–(e) and its variant; 200 random cases of the general pattern.
  - L16 exercises 3D₀ and −2D₀; L16 PEC bullet consistent with `L16-deck-update.md`.
- **Figures** (light and dark): torque-loop ⊙ upper-left, ⊗ lower-right, F ← / →, T ⊙ (CCW arc); lattice CCW with boundary M×n̂; rod ⊙ left, ⊗ right; slab: free and bound ⊙ on top, ⊗ below, y into the page; hysteresis loop CCW, B_r and ±H_c in place, virgin curve inside the loop; refraction 29.1°/59.0° and 85° → ≈ normal.

## Unresolved / notes
- The handbook values come from CRC molar susceptibilities (Pt +193, Ag −19.5, O₂(l, 90 K) +7699 ×10⁻⁶ cm³/mol; table in `review_L17.out` §F). Cite a handbook if the errata page wants a source.
- Cosmetic: in dark mode the electron's "−" in figure mag-moment-torque is hard to see on the light-blue dot.
- `problems/current-slab-and-sheet-by-amperes-law.md` also uses "nothing jumps". It is not reviewed here and is probably fine in its own context.

## Errata candidates (course sources)
**Slides (Shao, L17)**
- s13: Pt χm "+2.90×10⁻⁵" (measured ≈ +2.7×10⁻⁴) and liquid O₂ "+3.50×10⁻⁵" (≈ +3.5×10⁻³); both look like exponent slips. Also "domains reorient" for paramagnets: domains are ferromagnetic.
- s15 table (scan checked): Ag μr 0.99993 (measured ≈ 0.99998); Pb μr 0.99993 (≈ 0.999984, inconsistent with s12's −1.70×10⁻⁵). Also "Mn-An-ferrite" (Mn-Zn).
- s16: the statement gives one sheet value (−0.1â_y), but the figure has −0.1 on top and +0.1 below. The hint has a stray x̂: it should read H = ½J_s×â_n.
- s18 (magnetic column): "H ≠ 0 inside but it can be reduced or increased". It is B that changes; H is unchanged in the deck's own model (s19).
- s7, s8, s10, s19: M = χm H_ext holds only where the internal H equals the applied H (long rod, slab).
- s6: N counts atoms, but m is "per molecule". s10 title: "Magnetic Polarization". s17: J is not written as a vector, and the normal-B and tangential-E conditions are missing (B_n added in ink).

**Notes (Kudeki, L17)**
- p. 2: "D = ε_e E + P" should be ε_o; also uses ε and μ (linear media) before p. 8 defines them.
- p. 4: "**M**called" (missing space).
- p. 6: the caption has N_l where the text has N_a.
- p. 7: "H is the same in both regions" holds only for this geometry.
- fn 6 (p. 11): "dispacement", "chare".
- p. 12: unclosed parenthesis.
