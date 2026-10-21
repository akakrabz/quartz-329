# Review — Lecture 27 "Guided TEM waves on TL systems" (build 11, independent reviewer)

Files reviewed: `content-src/4-transmission-lines/27-guided-tem-waves-on-transmission-lines.md`, `concepts/telegraphers-equations.md`,
`concepts/characteristic-impedance.md`, `problems/a-backward-pulse-on-a-parallel-plate-line.md`, `figs_l27.py` (tl-guided-pulse,
tl-cross-sections, tl-ladder), `digest10/COVERAGE-L27.md`, `digest10/ERRATA-L27.md`. Notes pages p-1…p-8 read as images.
Own verification: `digest10/review_L27.py` → `review_L27.out`, **110 PASS, 0 FAIL** (written before reading `verify_L27.py`).
It checks: field equations (lossless and lossy, σ ≠ 0) and the telegrapher's equations with 𝓛 = μd/W, 𝓒 = εW/d, 𝓖 = σW/d by
finite differences; forward, backward and f + g waves (and a wrong-sign control that fails); wave equation; I = ±f/Z₀ by
quadrature of −∂I/∂z; plate ρ_s, J_s and every E × H, n̂ × H, Faraday-loop normal by `np.cross`; coax 𝓒, 𝓛 by quadrature and
twin-lead 𝓒, 𝓛 by image line charges/filaments (𝓛𝓒 = με both; Rao Table 6.1 form with half-spacing); all page numbers (CODATA
ε₀, μ₀; polyethylene ε_r = 2.25); exact coax TE11 cutoff (29.08 GHz vs rule 28.27 GHz); L- vs T-section ABCD phase and
ladder β → ω√(𝓛𝓒); FDTD of the ideal-battery step (3 V, 60 mA behind the front, stored energy = VI·t); every worked-problem
number with an FD check of the backward pulse; concept-page numbers; exam keys; figure screen-frame crosses.
`check.py`: OK. Words: lecture 2522, concepts 405 / 353, worked problem 898. Figures viewed light + dark (820 and 380 px; no overflow).

## Findings

| # | severity | where | what | fix |
|---|---|---|---|---|
| 1 | major | lecture, On exams | SP17 #2(ii), SP18 #1(ii), SP18 #1(v) bullets stated the conclusions that decide the multiple-choice keys (SP17 "none of these"; SP18 "I and II only"; the polarity item) | rewritten as methods (B_z = 0, n̂·D and n̂ × H with n̂ into the gap; check statements against §2/§3/§6; §3 trap); callout 117 words |
| 2 | major | problem (b), trap | "Writing V = +Z₀·0.5 out of habit" names the correct value (+2π V) as the error: the two habitual sign slips (plate, direction) cancel | "Fixing only one sign (plate or direction) gives V = −2π V. Sign I on plate 2 first, then V = −Z₀I." |
| 3 | minor | lecture §2 intuition | Faraday loop: "emf … equals μd Δz ∂H_y/∂t, the rate of change of the flux it links" hides Faraday's minus (loop normal is −ŷ) | normal −ŷ, Ψ = −μH_y d Δz, emf = −dΨ/dt = μd Δz ∂H_y/∂t (verified numerically) |
| 4 | minor | lecture §5 | plate 2 is the x = 0 (lower) plate in §1–2 and tl-guided-pulse, but wire 2 is drawn on top in tl-ladder and in L28; page never said so | one sentence: wire 2 plays plate 2's role; circuit drawings here and in L28 put it on top |
| 5 | minor | lecture summary; concept Z₀ | "L25's Γ with Z₀ for η" ambiguous (which η) | "Z₀ for η₁ and R for η₂" |
| 6 | minor | lecture Sources | Rao eqs. 7.39–7.47 sit in Ch. 7 "B. Time domain" before §7.4, not in "§7.4's opening" | corrected (Sources 95 words) |
| 7 | minor | figs_l27.py | twin-lead comment "D/2a = 2" but code draws 2.5 | comment fixed; module re-run, SVGs byte-identical |

No blockers: every equation, sign, direction, unit and number checked correct (incl. 50/75 Ω coax, 300 Ω twin-lead D = 12.3a,
W/d = 7.5, 15 GHz / 28 GHz (29 exact), 60 mA / 0.18 W and the energy split, 5000 km / 6.7 cm, problem (a)–(d)).
Figures agree with the text: side view (z right, x up, y out) E up × H out = +z, +ρ_s and +z current on the x = 0 plate;
cross-sections (z into page, x up, y right) E × H into the page for plates, coax (H clockwise about ⊗) and twin-lead (E lines
circles through ±s, H lines Apollonius circles = equipotentials, circulation correct about ⊗ and ⊙); ladder L-section with
series Δz𝓛, shunt Δz𝓒, I along +z on the upper wire 2.

## Coverage verdict
Complete. All 38 items of COVERAGE-L27 checked against the page images: plates in a plane wave, facing-surface sources,
fringing, excitation; scalar Faraday/Ampère with σ; V (path-independent, B_z = 0) and I; telegrapher's equations with 𝓖 and
the missing 𝓡; footnote; mnemonic; wave equation, d'Alembert V, I, Z_o, GF margin table; battery example a)–c) and the
lumped/distributed discussion; ΔV, ΔI ladder; Δz ≪ λ; p = VI and ½Re{ṼĨ*}; non-TEM margin note. Nothing misrepresented.
ERRATA-L27 items 1–4 confirmed (cover-up method; doubled "known as"; "makes"; the drawn section is an L-section, same
per-section phase as a T-section: verified by ABCD traces).

## Exams
Worked problem is re-parameterized: backward rectangular pulse on the top plate, PE filling, W/d = 20 (keys 4π Ω, 1000π V/m,
18/π W, ε_r = 4) vs SP19 #2 forward δ on the bottom plate (1.2π Ω, 240πδ V/m, 2.4π W) and FA23 #4(d) (ε_r = 36). (d)'s ε_r = 4
equals SP19's given filling (data, not a key): acceptable.

## Lecture 28 consistency (not edited)
No mismatch. Both pages: V = conductor/wire 2 relative to 1; I along +z on wire 2, returning on wire 1; z = 0 at the source,
+z toward the load; V = f(t − z/v) + g(t + z/v), I = (f − g)/Z₀; backward wave I = −V/Z₀. L27's ideal battery f = 3u(t)
matches L28's R_g = 0 row (τ_g = 1). figs_l28 draws wire 2 on top, as L27's §5 now says.

## Unresolved
None.
