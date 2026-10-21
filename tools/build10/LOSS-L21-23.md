# Loss review: Lectures 21–23 (build 9)

Words after review (trim_check count): L21 3497 → 3538 (+1.2 %), L22 3779 → 3844 (+1.7 %), L23 4036 → 4098 (+1.5 %).
trim_check: L21, L22 OK structure kept; L23 FAIL on header line only (expected). check.py: OK.
## L21 — monochromatic waves and phasors
Restored:
- §2 plasma derivation: missing step "transverse wave, ∇·E = 0, so left side is −∇²E".
- §2: v_g = dω/dβ is general; c√(1−ωp²/ω²) is the plasma value (was written as if general); "no paper on hand asks for v_g".
- §2 gas: why γ = 5/3 is adiabatic (too fast for heat to flow).
- §7 Joule heating: condition J̃ = σẼ before ⟨J·E⟩ = ½Re{σ}|Ẽ|².
- §7 sheet example: 377 W/m² is the power "from the current" (energy balance with η/2 per side).
- Exam box: papers often ask one component's power first, then the whole wave.
Judged fine: Connections/Summary cuts (repeats of §§1–7); notes' slips (on errata page); spectrum trivia; folded product rule (result in title, key box, Summary).
## L22 — phasor Maxwell, damped waves
Meaning fixes:
- §2 "ŷ dẼx/dz = −jωμH̃y" equated a vector to a scalar → curl step written out, then scalar equation.
- §4 "β now frequency dependent" (true even when lossless) → β no longer ∝ ω: v_p not constant, λ not ∝ 1/f.
- §6 "'λ longer than δ' decides nothing" → only means σ/ωε > 0.33 (in-between range included), not proof of a good conductor.
- §4 ⟨S⟩ formula labelled "for the +z wave" and why it points along û (cos τ > 0).
- §3 diffusion equation: says the μϵ (second-derivative) term drops for σ ≫ ωε.
Restored:
- §1: conclusion ∇·D̃ = ρ̃ (curl laws + continuity contain both divergence laws).
- §3: G/C = σ/ε holds for one homogeneous filling.
- §4: group velocity is a different speed from v_p.
- §6 derivation: validity conditions σ/ωε ≪ 1, ≫ 1 and |a| ≪ 1 for the binomial rule.
- Exam box: "one of the most reliably examined parts of Exam 3".
Judged fine: relaxation physics and L10 resistor/capacitor-like (on L23 §1, linked); Connections (repeats); slips on errata.
## L23 — imperfect dielectrics and good conductors
Meaning fixes:
- Key box "between 0.1 and 10 the approximations fail" → "lose accuracy" (imperfect-dielectric α still 1.1 % at p = 0.3).
- §1 "a decade below/above f_c" → "more than a decade".
- §2 "α 10 % and 55 % high" → says which formula is which.
- §6 shielding: "nearly transparent" → "to absorption" (reflection still acts); "power-frequency fields" → "magnetic fields".
Restored:
- §4: stored energy in a good conductor is almost all magnetic; perfect conductor: no field inside, the δ-thick layer becomes the surface current.
- §5: why bandwidth limits rate (carrier carries only a small fraction of f); why antennas are huge (≪ λ0, radiate poorly) and why the link is one-way.
- Exam box: "constant or decaying power flow" T/F item; e^{-0.2z}e^{-j0.2z} has α = β, a good conductor.
Judged fine: Connections bullets (repeats of §§1–6); summary numbers (in §§1, 5, 6 tables); notes' slips (errata rows L23).
