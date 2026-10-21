# Review — Lecture 26 "Standing waves and radiation pressure" (build 11)

Reviewer's script: `digest10/review_L26.py` → `review_L26.out` (113 PASS, 0 FAIL; written before reading `verify_L26.py`).
It covers: the phasor sums and real forms; Faraday and Ampère by central differences (ε_r = 2.25); the PEC condition; node and
antinode positions; ⟨S⟩ = 0 by `np.cross` and by quadrature; instantaneous S and w; ⟨w⟩ = ε₁E₀²; constant energy per λ/4
cell; Poynting's theorem by finite differences; the zeros of w; the partial-reflection decomposition, (1 ± |Γ|) ripple, λ/2
period and ⟨S⟩ = (1 − |Γ|²)E₀²/2η₁ for four complex Γ; J_s = n̂ × H; the sheet-radiation check (E and H); copper at 10 GHz
from the exact γ, η, Γ (δ, R_s = Re η₂, 4R_s/η₀ against 1 − |Γ|², the depth integral of J̃_t, Joule loss ½R_s|J̃_s|²);
⟨P_rad⟩ from the exact fields (2⟨S_i⟩/c to 1.4 × 10⁻⁴, and equal to (1 + |Γ|²)⟨S_i⟩/c to 3 × 10⁻⁹, also for σ = 10⁻² … 10⁵ S/m);
instantaneous P_rad(t) = ½μ₀H_y²(0,t) from the exact copper fields; photon momentum and spin; sunlight, sail and laser
numbers against the solar constant 1361 W/m² (Kopp & Lean 2011) and CODATA constants; the whole worked problem.

## Findings

| # | severity | where | what | fix |
|---|---|---|---|---|
| 1 | major | `concepts/standing-waves.md`, trap 1 | "Only the average flux vanishes; S and w do not" contradicts the page's own circular-wave example (S = 0 at every instant) | "In a linear standing wave only the average flux vanishes…" |
| 2 | minor | lecture §2 trap 4 | "A mirror at z = d puts z − d in place of z" drops the phase factor e^{−jβ₁d} unless E₀ is the incident phasor at the mirror (checked, A14–A15) | clause added |
| 3 | minor | lecture §2 trap 3 | "In a travelling wave Ẽ and H̃ are in phase" — only lossless | "lossless" added |
| 4 | minor | lecture §5, effective-current box | last step σ₂τE₀/γ₂ = 2E₀/η₀ and "whatever σ₂" read as exact; true to O(\|η₂\|/η₀) (copper 1 × 10⁻⁴, graphite 1 GHz 9 × 10⁻⁴) | "≈" and "(to order \|η₂\|/η₀)" |
| 5 | minor | lecture §6 sunlight example | E₀ = 1.01 kV/m and the 5.4 A/m peak treat broadband sunlight as one cosine wave without saying so (L20 says it) | "as one cosine wave" |
| 6 | minor | lecture Sources | R_s = 1/σδ = Re{η₂} (site's, inside a "notes' box") not listed as the site's; no Rao cross-check for partial standing waves | added to the site's list; Rao §7.1–7.2 |
| 7 | minor | `concepts/standing-waves.md`, Physics 2 | "a quarter wavelength apart in space and a quarter period apart in time, so ⟨S⟩ = 0" — only the time quadrature gives it | split; "The time quadrature makes ⟨S⟩ = 0" |
| 8 | minor | `concepts/standing-waves.md`, Physics 5 | partial-reflection bullet (site's addition) unlabelled, unlike the lecture page and the radiation-pressure concept | "(this site's; the notes treat only Γ = −1)" |
| 9 | minor | worked problem, last paragraph | re-parameterization list omits the changed hand (SP19 key LHCP → here RHCP) | "axis, amplitude and hand" |

Checked and correct (no change): every equation of §1–§6 and the folded derivation; directions (x̂ × ŷ = +ẑ push; n̂ = −ẑ,
J_s = +x̂ in phase with E_i at the mirror; sheet fields E^± = −(η₁/2)J_s(t ∓ z/v), H = ½J_s × n̂); ⟨S⟩ = 0; ½ factors;
e^{−2αz} for the force density; the site's additions — partial reflection (§2, labelled), instantaneous pressure
½μ₀H_y²(0,t) = (4⟨S_i⟩/c)cos²ωt and the mean-field-on-a-sheet reading (labelled), ⟨P_rad⟩ = ε₀E₀² = ⟨w⟩, the absorber
⟨S_i⟩/c (labelled), and the concept page's (1 + |Γ|²)⟨S_i⟩/c (labelled; exact for ε₂ = ε₀, μ₂ = μ₀ by momentum balance,
confirmed for σ from 10⁻² to 5.8 × 10⁷ S/m). Numbers: δ = 0.661 µm, R_s = 26.1 mΩ, 4R_s/η₀ = 2.770 × 10⁻⁴ vs exact
1 − |Γ|² = 2.770 × 10⁻⁴, 99.97 %; |Γ|² = 0.99972, 0.014 %; 9.08 / 4.54 µPa, 0.091 N, 5.4 A/m, 6.7 nN.

Worked problem: handedness by numeric rotation (sign of û · (E × dE/dt) over a full period, Lecture 24 convention =
the §4 recipe, which reproduces the SP19 key's LHCP for its own wave): incident right-circular, reflected left-circular, at
y = 0 and y = 3.7 cm. H̃ by `np.cross`; totals E = 120π sin βy â(t), H = cos βy â(t); Faraday and Ampère by finite
differences; S ≡ 0; the energy-density claim w = ½μ₀ = 2π × 10⁻⁷ J/m³ at every y and t is right (ε₀η₀² = μ₀); the trap's
±30π sin 2βy sin 2ωt pair; J_s = ŷ × H = 2E_i(0,t)/η₀; P_rad = −ŷ 2π × 10⁻⁷ N/m² constant = 2⟨S_i⟩/c with ⟨S_i⟩ = 30π W/m².
No key carries over from SP19 Exam 3 #3 (axis, amplitude, frequency and hand changed; (c)'s "standing" is conceptual).

Figures (rendered light + dark with playwright, page also at 380 px: no horizontal scroll, no overflowing displays):
stand-snapshots (nodes, envelopes, instants match §1–2), stand-partial (|1 + Γe^{j2βz}| for four Γ, matches caption),
stand-energy (stacked w_E, w_H at 0, π/4, π/2; S arrows checked against sign of sin 2βz: H antinode → E antinode),
stand-skin-layer (J x̂ up, B ŷ out, J × B +ẑ right: proper rotation; J_x ∝ e^{−s}cos(ωt − s + π/4) from J̃_sγe^{−γz}).
All agree with the text. Cosmetic only: the "−λ" x-tick in stand-partial sits close to the y-label "0".

Format: `check.py` OK; words — lecture 2140 (≤ 3000), standing-waves 477, radiation-pressure 391 (≤ 500), worked problem
895 (≤ 900); in one breath 93, On exams 103 (methods only), Sources 98.

## Coverage verdict
All 33 items of the 6-page notes (checked against the page images) are on the page, faithfully; nothing missing or
misrepresented. Only omission: the class-calendar animation (login page), as COVERAGE says. Errata 1–5 confirmed against
the images (Γ > 0 margin figure, "real time", "see of how", missing conjugate — its 1.4 × 10⁻⁴ effect reproduced — and the
Rothman–Boughn year: Am. J. Phys. 77, 122 (2009), arXiv:0807.1310).

## Unresolved
None. The text references to Lecture 36 (VSWR) and Lecture 39 (lossy lines) are plain text, not links (no pages yet).
