# Topic map — restructuring Lectures 1–26 around topic pages (build 12)

Every lecture section is assigned to exactly one topic page (`concepts/<slug>.md`). **Existing** = page exists (grow it);
**NEW** = create it (stub with front matter exists). The *owner* column says which writer batch edits that topic page;
a batch that must contribute to a topic it does not own writes a handoff file instead (see RESTRUCTURE-BRIEF.md).

Batches: **A** = L1–6 · **B** = L7–11 · **C** = L12–15 · **D** = L16–19 · **E** = L20–26.

## Themes (the new topics index, in this order)

1. **Fields and the toolkit** — electric-field, lorentz-force, maxwells-equations, differential-elements, superposition, five-step-recipe, charge-density, current-distributions (NEW), helmholtz-theorem (NEW)
2. **Electrostatics** — coulombs-law, flux, gauss-law, symmetric-charge-distributions (NEW), divergence, curl, divergence-theorem, stokes-theorem, conservative-field, electrostatic-potential, boundary-conditions, poissons-equation, pn-junction (NEW)
3. **Materials, capacitors, conduction** — conductors, polarization, electric-flux-density, permittivity, static-fields-in-dielectrics (NEW), capacitance, conductance, electrostatic-energy, conductivity-and-susceptibility-models
4. **Magnetostatics** — magnetic-field, biot-savart-law, amperes-law, current-sheets-and-slabs (NEW), solenoids-and-toroids (NEW), vector-potential, magnetic-dipole (NEW), magnetic-flux
5. **Induction and inductance** — faradays-law, electromotive-force, motional-emf (NEW), inductance, magnetic-energy, transmission-line-parameters (NEW)
6. **Maxwell's equations and magnetic matter** — continuity-equation, displacement-current, magnetization, permeability, magnetic-materials (NEW)
7. **Plane waves** — wave-equation, plane-waves, intrinsic-impedance, current-sheet-radiation, poynting-vector, poynting-theorem, time-average-power (NEW), monochromatic-waves (NEW), dispersion-relation, phasors
8. **Waves in lossy media** — phasor-maxwell-equations (NEW), propagation-constant, loss-tangent, skin-depth
9. **Polarization, reflection, standing waves** — group-velocity, wave-polarization, reflection-and-transmission, standing-waves, radiation-pressure
10. (unchanged) **Transmission lines** — telegraphers-equations, characteristic-impedance, bounce-diagram

## Section → topic assignments

| lecture section | topic page | owner |
|---|---|---|
| L1 §1 Why fields; §2 roadmap | electric-field (§1), maxwells-equations (§2) | A owns electric-field; maxwells-equations owned by **D** → A hands off |
| L1 §3 units; §4 vector algebra | stay on the lecture page as 2-line pointers to the Toolkit pages | — |
| L1 §5 dl and dS; §6 | differential-elements; (§6 drop) | A |
| L2 §1 force → field | electric-field, lorentz-force | A |
| L2 §2 Coulomb | coulombs-law | A |
| L2 §3 superposition | superposition | A |
| L2 §4 5-step program | five-step-recipe | A |
| L2 §5 Coulomb → Gauss | gauss-law | A |
| L3 §1 flux | flux | A |
| L3 §2 Gauss restated | gauss-law | A |
| L3 §3 three symmetries | symmetric-charge-distributions (NEW) | A |
| L3 §4 superposition of building blocks | symmetric-charge-distributions | A |
| L3 §5 charge densities, δ | charge-density | A |
| L3 §6 ∮B·dS = 0 | magnetic-flux | **C** → A hands off |
| L4 §1 FTC → Stokes; §4 two pictures | divergence-theorem, stokes-theorem | A |
| L4 §2 divergence | divergence | A |
| L4 §3 curl | curl | A |
| L4 §5 conservative fields; §6 static E curl-free | conservative-field | A |
| L4 §7 differential Maxwell | maxwells-equations | **D** → A hands off |
| L5 §1, 2, 5, 6 | electrostatic-potential | A |
| L5 §3 exact differentials; §4 path independence | conservative-field | A |
| L6 §1 circulation | conservative-field | A |
| L6 §2–5 boundary conditions | boundary-conditions | A (owner; B, D, E hand off) |
| L7 §1 Gauss → Poisson; §2 Laplace 1-D; §3 Poisson with charge | poissons-equation | B |
| L7 §3 pn-junction example (if present) | pn-junction (NEW) | B |
| L7 §4 general solution; §5 Helmholtz | helmholtz-theorem (NEW) | B |
| L8 §1 two ideal materials; §2 conductors | conductors | B (owner; D hands off perfect-conductor material) |
| L8 §3 bound charge, polarization | polarization | B |
| L8 §4 D and Gauss in matter | electric-flux-density | B |
| L8 §5 linear dielectrics | permittivity | B |
| L9 §1 rules; §2 refraction | boundary-conditions (refraction) → **A** owns → B hands off; §1 "rules" → static-fields-in-dielectrics | B |
| L9 §3 layer by layer; §4 graded ε; §5 dielectric coat | static-fields-in-dielectrics (NEW) | B |
| L10 §1–4 | capacitance | B |
| L10 §5 energy | electrostatic-energy | B |
| L10 §6 conductance | conductance | B |
| L10 §7 diode junction | pn-junction | B |
| L11 §1–5 | conductivity-and-susceptibility-models | B (owner; E hands off L22 §8) |
| L11 §6 what drives the current in a wire | conductors | B |
| L12 §1, 2 | magnetic-field | C |
| L12 §3 | biot-savart-law | C |
| L12 §4, 6 | amperes-law | C |
| L12 §5 J, J_s, I, δ | current-distributions (NEW) | C |
| L13 §1 sheet; §2 slab | current-sheets-and-slabs (NEW) | C |
| L13 §3 solenoid | solenoids-and-toroids (NEW) | C |
| L13 §4 statics side by side | stays on the lecture page as a pointer to the Unit 2 dictionary | — |
| L13 §5 vector potential | vector-potential | C |
| L13 §6 loop and dipole | magnetic-dipole (NEW) | C |
| L14 §1 law and flux; §3 transformer emf examples | faradays-law | C |
| L14 §2 moving loops, emf, Lenz | electromotive-force | C |
| L14 §4 sliding bar; §5 voltmeter paradox | motional-emf (NEW) | C |
| L15 §1 self-inductance; §2 RL; §3 Ampère chain | inductance | C |
| L15 §4 energy | magnetic-energy | C |
| L15 §5 𝓛, 𝓒, product | transmission-line-parameters (NEW) | C |
| L15 §6 potentials in time | vector-potential | C |
| L16 §1 | continuity-equation | D |
| L16 §2 | displacement-current | D |
| L16 §3 complete equations | maxwells-equations | D |
| L16 §4 dynamic boundary conditions, perfect conductors | boundary-conditions (hand off to A); perfect conductors → conductors (hand off to B) | D |
| L17 §1–3 | magnetization | D |
| L17 §4 H redefined, linear media, solenoid with core | permeability | D |
| L17 §5 dia/para/ferro, hysteresis | magnetic-materials (NEW) | D |
| L17 §6 boundary conditions in magnetic media | boundary-conditions (hand off to A) | D |
| L17 §7 dictionary P ↔ M | magnetization (table) | D |
| L18 §1, 2, 4 | wave-equation | D |
| L18 §3 planar problem; §6 reading a wave | plane-waves | D |
| L18 §5 η; §7 in matter and on a cable | intrinsic-impedance | D (owner; E hands off complex η) |
| L19 §1, 2, 5, 6 | plane-waves | D |
| L19 §3, 4, 7, 8 | current-sheet-radiation | D (owner; E hands off L22 §7) |
| L19 §7 Poynting part | poynting-vector | **E** → D hands off |
| L20 §1–5 | poynting-theorem | E |
| L20 §3 reading the terms (S part) | poynting-vector | E |
| L20 §6 cosine sheet example | current-sheet-radiation (hand off to D) or poynting-theorem (keep the energy-balance part) | E |
| L20 §7 time averages; L21 §7 | time-average-power (NEW) | E |
| L21 §1 | monochromatic-waves (NEW) | E |
| L21 §2 | dispersion-relation | E |
| L21 §3–6 | phasors | E |
| L22 §1, 2 | phasor-maxwell-equations (NEW) | E |
| L22 §3–6 | propagation-constant (§5's complex η → intrinsic-impedance handoff to D) | E |
| L22 §7 | current-sheet-radiation (hand off to D) | E |
| L22 §8 | conductivity-and-susceptibility-models (hand off to B) | E |
| L23 §1, 2, 3, 7 | loss-tangent | E |
| L23 §4, 5, 6 | skin-depth | E |
| L24 §1, 2 | group-velocity | E |
| L24 §3–8 | wave-polarization | E |
| L25 §1–4 | reflection-and-transmission | E |
| L26 §1–5 | standing-waves | E |
| L26 §6 | radiation-pressure | E |

Topic ownership summary — **A:** electric-field, lorentz-force, differential-elements, coulombs-law, superposition,
five-step-recipe, gauss-law, flux, symmetric-charge-distributions, charge-density, divergence, curl, divergence-theorem,
stokes-theorem, conservative-field, electrostatic-potential, boundary-conditions. **B:** poissons-equation, pn-junction,
helmholtz-theorem, conductors, polarization, electric-flux-density, permittivity, static-fields-in-dielectrics,
capacitance, electrostatic-energy, conductance, conductivity-and-susceptibility-models. **C:** magnetic-field,
biot-savart-law, amperes-law, current-distributions, current-sheets-and-slabs, solenoids-and-toroids, vector-potential,
magnetic-dipole, magnetic-flux, faradays-law, electromotive-force, motional-emf, inductance, magnetic-energy,
transmission-line-parameters. **D:** continuity-equation, displacement-current, maxwells-equations, magnetization,
permeability, magnetic-materials, wave-equation, plane-waves, intrinsic-impedance, current-sheet-radiation.
**E:** poynting-vector, poynting-theorem, time-average-power, monochromatic-waves, dispersion-relation, phasors,
phasor-maxwell-equations, propagation-constant, loss-tangent, skin-depth, group-velocity, wave-polarization,
reflection-and-transmission, standing-waves, radiation-pressure.
