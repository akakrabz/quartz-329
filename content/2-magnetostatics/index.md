---
title: "Unit 2 · Magnetostatics and induction"
description: "Lectures 12–15: steady currents and the magnetic fields they make (Biot–Savart, Ampère's law, current sheets, solenoids, the vector potential), then Faraday's law, emf, and inductance. Every result has an electrostatic twin — the dictionary on this page lists them."
tags: [magnetostatics]
---

Steady current → static magnetic field. The unit is built exactly like Unit 1 with the roles of divergence and curl swapped: the electric field was *curl-free with sources* ($\nabla\times\mathbf{E} = 0$, $\nabla\cdot\mathbf{D} = \rho$); the magnetic field is *divergence-free with sources in its curl* ($\nabla\cdot\mathbf{B} = 0$, $\nabla\times\mathbf{H} = \mathbf{J}$). Ampère's law plays the part Gauss's law played, Biot–Savart the part of Coulomb's law, the vector potential $\mathbf{A}$ the part of $V$, and the inductor is the circuit element that falls out at the end, just as the capacitor did. Then, in Lecture 14, time enters for the first time: a changing magnetic flux drives an electric field around a loop, and "voltage" stops being a number between two points.

| # | page | one line |
|---|---|---|
| 12 | [[2-magnetostatics/12-magnetic-force-biot-savart-and-amperes-law\|Magnetic force, Biot–Savart, and Ampère's law]] | why parallel currents attract (relativity); $\mathbf{F} = q\mathbf{v}\times\mathbf{B}$; $\mathbf{B} = \mu_0I/(2\pi r)\,\hat\phi$; Biot–Savart; $\oint\mathbf{H}\cdot d\mathbf{l} = I_{\text{enc}}$; $\nabla\times\mathbf{H} = \mathbf{J}$; δ-function currents |
| 13 | [[2-magnetostatics/13-current-sheets-solenoids-and-the-vector-potential\|Current sheets, solenoids, and the vector potential]] | sheet $\mathbf{H} = \tfrac12\mathbf{J}_s\times\hat n$; slab; solenoid $\mu_0nI$; $\mathbf{B} = \nabla\times\mathbf{A}$, $\nabla^2\mathbf{A} = -\mu_0\mathbf{J}$; the current loop and the dipole field |
| 14 | [[2-magnetostatics/14-faradays-law-and-induced-emf\|Faraday's law and induced emf]] | $\nabla\times\mathbf{E} = -\partial\mathbf{B}/\partial t$; $\mathcal{E} = -d\Psi/dt$; motional emf; Lenz; six examples; the voltmeter paradox |
| 15 | [[2-magnetostatics/15-inductance-magnetic-energy-and-the-potentials\|Inductance, magnetic energy, and the potentials]] | $L = \Psi/I$; $V = L\,dI/dt$; $\tau = L/R$; solenoid and coax $L$; $\tfrac12LI^2$, $\tfrac12\mu H^2$; $\mathcal{L}\mathcal{C} = \mu\epsilon$; $\mathbf{E} = -\nabla V - \partial\mathbf{A}/\partial t$ and gauge freedom |

**Worked problems for this unit:** [[problems/current-slab-and-sheet-by-amperes-law]] · [[problems/emf-of-a-loop-moving-near-a-line-current]] · [[problems/sliding-bar-and-the-voltmeter-readings]] · [[problems/coax-inductance-and-the-lc-product]]

## The dictionary: electrostatics ↔ magnetostatics

If Unit 1 made sense, Unit 2 is a translation exercise. Read each row left to right, and notice that the geometry factors, the recipes, and even the traps carry over.

| electrostatics (Unit 1) | magnetostatics (Unit 2) | what changes |
|---|---|---|
| source: charge $\rho$ [C/m³], $\rho_s$, $\rho_l$, $Q$ | source: current $\mathbf{J}$ [A/m²], $\mathbf{J}_s$ [A/m], $I$ [A] | the source is a **vector** |
| Coulomb's law $d\mathbf{E} = \dfrac{\rho\,dV}{4\pi\epsilon_0R^2}\hat{R}$ | Biot–Savart $d\mathbf{B} = \dfrac{\mu_0\,I\,d\mathbf{l}\times\hat{R}}{4\pi R^2}$ | $1/R^2$ both; $d\mathbf{B}$ is *perpendicular* to the source and to $\hat R$ |
| line charge $\mathbf{E} = \dfrac{\rho_l}{2\pi\epsilon_0r}\hat r$ | line current $\mathbf{B} = \dfrac{\mu_0I}{2\pi r}\hat\phi$ | radial ↔ azimuthal; $\epsilon_0$ divides, $\mu_0$ multiplies |
| sheet charge $\mathbf{D} = \tfrac12\rho_s\,\hat n$ (normal, ± on the two sides) | sheet current $\mathbf{H} = \tfrac12\mathbf{J}_s\times\hat n$ (tangential, ± on the two sides) | normal ↔ tangential; both independent of distance |
| Gauss $\oint\mathbf{D}\cdot d\mathbf{S} = Q_{\text{enc}}$, $\nabla\cdot\mathbf{D} = \rho$ | Ampère $\oint\mathbf{H}\cdot d\mathbf{l} = I_{\text{enc}}$, $\nabla\times\mathbf{H} = \mathbf{J}$ | closed **surface** ↔ closed **loop**; divergence ↔ curl |
| $\nabla\times\mathbf{E} = 0$ (no circulation) | $\nabla\cdot\mathbf{B} = 0$ (no sources) | the "other" equation is homogeneous in both |
| five-step recipe: symmetry → $D(r)\cdot(\text{area}) = Q_{\text{enc}}$ | symmetry → $H(r)\cdot(\text{length}) = I_{\text{enc}}$ | pillbox/cylinder/sphere ↔ circle/rectangle |
| curl-free ⟹ $\mathbf{E} = -\nabla V$, scalar potential | divergence-free ⟹ $\mathbf{B} = \nabla\times\mathbf{A}$, vector potential | $V$ is fixed up to a constant; $\mathbf{A}$ up to a gradient |
| Poisson $\nabla^2V = -\rho/\epsilon_0$, $V = \displaystyle\int\frac{\rho\,d^3r'}{4\pi\epsilon_0\lvert\mathbf{r}-\mathbf{r}'\rvert}$ | $\nabla^2\mathbf{A} = -\mu_0\mathbf{J}$, $\mathbf{A} = \displaystyle\int\frac{\mu_0\mathbf{J}\,d^3r'}{4\pi\lvert\mathbf{r}-\mathbf{r}'\rvert}$ | same Green's function, component by component (Coulomb gauge) |
| material: $\mathbf{D} = \epsilon\mathbf{E}$, $\epsilon = (1+\chi_e)\epsilon_0$ | material: $\mathbf{B} = \mu\mathbf{H}$, $\mu = (1+\chi_m)\mu_0$ | polarization $\mathbf{P}$ ↔ magnetization $\mathbf{M}$ (Lecture 17) |
| boundary: $\hat n\cdot(\mathbf{D}_1-\mathbf{D}_2) = \rho_s$, $\hat n\times(\mathbf{E}_1-\mathbf{E}_2) = 0$ | boundary: $\hat n\cdot(\mathbf{B}_1-\mathbf{B}_2) = 0$, $\hat n\times(\mathbf{H}_1-\mathbf{H}_2) = \mathbf{J}_s$ | the normal component of the *flux density* and the tangential component of the *field* are the regular ones |
| conductor surface: $\mathbf{E}$ normal, ends on $\rho_s$ | conductor surface: $\mathbf{H}$ tangential, carried by $\mathbf{J}_s$ | |
| element: $C = Q/V$ (given $Q$: Gauss → $\mathbf{D}\to\mathbf{E}\to V$) | element: $L = \Psi/I$ (given $I$: Ampère → $\mathbf{H}\to\mathbf{B}\to\Psi$) | the same geometric factor, inverted: $\mathcal{L}\mathcal{C} = \mu\epsilon$ |
| $I = C\,dV/dt$; $\tau = RC$; large $C$ ≈ voltage source | $V = L\,dI/dt$; $\tau = L/R$; large $L$ ≈ current source | |
| energy $\tfrac12CV^2$, density $\tfrac12\epsilon E^2$ | energy $\tfrac12LI^2$, density $\tfrac12\mu H^2$ | |
| EMF $\oint\mathbf{E}\cdot d\mathbf{l}$ [V] — zero in statics | MMF $\oint\mathbf{H}\cdot d\mathbf{l}$ [A] — equals the linked current | Lecture 14 makes the EMF nonzero |

Two things do *not* translate. There is no magnetic charge, so there is no magnetic Coulomb's law and no "magnetic potential drop" that is path-independent; and the magnetic force on a charge depends on its velocity, so static magnetic fields do no work. Both come back as useful checks: if a magnetostatic calculation produces field lines that begin or end, or a force along $\mathbf{v}$, something is wrong.

The concept pages [[concepts/lorentz-force]], [[concepts/curl]], [[concepts/stokes-theorem]] and [[concepts/maxwells-equations]] were written with this unit in mind; the new ones are [[concepts/magnetic-field]], [[concepts/biot-savart-law]], [[concepts/amperes-law]], [[concepts/vector-potential]], [[concepts/magnetic-flux]], [[concepts/faradays-law]], [[concepts/electromotive-force]], [[concepts/inductance]] and [[concepts/magnetic-energy]].
