---
title: "ECE 329 · Fields and Waves"
description: "Teaching notes for ECE 329 (Fields and Waves I): 72 topic pages in 10 themes that carry the content, lecture pages that map onto them, worked exam-style problems, a bank of practice problems tagged easy, medium and hard, and interactive demos."
---

Notes for **ECE 329 — Fields and Waves I** (University of Illinois), written to *teach* the material rather than to summarize it. The source material is the course itself — Prof. Kudeki's lecture notes, the lecture slides with their in-class annotations, the homework and exams — digested and rewritten in one consistent notation, with the connections made explicit.

> [!tip] How this site is organized — topics first, one graph
> - **Topics** carry the content: one page per idea (Gauss's law, boundary conditions, skin depth, …) with the key equation, the derivation folded, the course's examples with their numbers, the traps, what exams do with it, and links to every lecture and practice problem that uses it. Grouped by theme below.
> - **Lectures** (in course order) are maps: each keeps the lecture's section headings and says, section by section, what the lecture does and where the full treatment lives.
> - **Problems** and **demos** are where the ideas get exercised — exam-style problems worked in full (with the numbers changed), and interactive pages you can drag things around in.
> - **Practice** is where you do the exercising yourself: 344 problems for Lectures 2–30, tagged easy, medium or hard, each with a folded hint and a worked solution.
>
> Every page links to its neighbours; hover a link for a preview, and use the **graph view** at the top right of any page to see what connects to what. Fields and Waves is a web of ideas, not a list — the site is built the same way.

## Course map

The site is organized by **topic**. Each theme below groups the [[concepts/index|topic pages]] — one page per idea with its definition, derivation (folded), the course's examples, traps and exam notes. Lectures are listed under [[index#by-lecture|By lecture]] as maps onto the topics.

### By topic

**[[concepts/index#fields-and-the-toolkit|Fields and the toolkit]]** — [[concepts/electric-field|Electric field]] · [[concepts/lorentz-force|Lorentz force]] · [[concepts/maxwells-equations|Maxwell's equations]] · [[concepts/differential-elements|Differential elements]] · [[concepts/superposition|Superposition]] · [[concepts/five-step-recipe|5-step recipe]] · [[concepts/charge-density|Charge densities, δ]] · [[concepts/current-distributions|Current distributions]] · [[concepts/helmholtz-theorem|Helmholtz's theorem]]

**[[concepts/index#electrostatics|Electrostatics]]** — [[concepts/coulombs-law|Coulomb's law]] · [[concepts/flux|Flux]] · [[concepts/gauss-law|Gauss's law]] · [[concepts/symmetric-charge-distributions|Symmetric charge distributions]] · [[concepts/divergence|Divergence]] · [[concepts/curl|Curl]] · [[concepts/divergence-theorem|Divergence theorem]] · [[concepts/stokes-theorem|Stokes' theorem]] · [[concepts/conservative-field|Conservative fields]] · [[concepts/electrostatic-potential|Electrostatic potential]] · [[concepts/boundary-conditions|Boundary conditions]] · [[concepts/poissons-equation|Poisson and Laplace]] · [[concepts/pn-junction|The pn junction]]

**[[concepts/index#materials-capacitors-and-conduction|Materials, capacitors and conduction]]** — [[concepts/conductors|Conductors]] · [[concepts/polarization|Polarization]] · [[concepts/electric-flux-density|Electric flux density D]] · [[concepts/permittivity|Permittivity]] · [[concepts/static-fields-in-dielectrics|Static fields in dielectrics]] · [[concepts/capacitance|Capacitance]] · [[concepts/conductance|Conductance]] · [[concepts/electrostatic-energy|Electrostatic energy]] · [[concepts/conductivity-and-susceptibility-models|Lorentz–Drude models]]

**[[concepts/index#magnetostatics|Magnetostatics]]** — [[concepts/magnetic-field|Magnetic field]] · [[concepts/biot-savart-law|Biot–Savart law]] · [[concepts/amperes-law|Ampère's law]] · [[concepts/current-sheets-and-slabs|Current sheets and slabs]] · [[concepts/solenoids-and-toroids|Solenoids and toroids]] · [[concepts/vector-potential|Vector potential]] · [[concepts/magnetic-dipole|Magnetic dipole]] · [[concepts/magnetic-flux|Magnetic flux Ψ]]

**[[concepts/index#induction-and-inductance|Induction and inductance]]** — [[concepts/faradays-law|Faraday's law]] · [[concepts/electromotive-force|Electromotive force]] · [[concepts/motional-emf|Motional emf]] · [[concepts/inductance|Inductance]] · [[concepts/magnetic-energy|Magnetic energy]] · [[concepts/transmission-line-parameters|Line parameters 𝓛, 𝓒, 𝓖]]

**[[concepts/index#maxwells-equations-and-magnetic-matter|Maxwell's equations and magnetic matter]]** — [[concepts/continuity-equation|Continuity equation]] · [[concepts/displacement-current|Displacement current]] · [[concepts/magnetization|Magnetization]] · [[concepts/permeability|Permeability]] · [[concepts/magnetic-materials|Magnetic materials]]

**[[concepts/index#plane-waves|Plane waves]]** — [[concepts/wave-equation|Wave equation]] · [[concepts/plane-waves|Plane waves]] · [[concepts/intrinsic-impedance|Intrinsic impedance]] · [[concepts/current-sheet-radiation|Current-sheet radiation]] · [[concepts/poynting-vector|Poynting vector]] · [[concepts/poynting-theorem|Poynting's theorem]] · [[concepts/time-average-power|Time-average power]] · [[concepts/monochromatic-waves|Monochromatic waves]] · [[concepts/dispersion-relation|Dispersion relation]] · [[concepts/phasors|Phasors]]

**[[concepts/index#waves-in-lossy-media|Waves in lossy media]]** — [[concepts/phasor-maxwell-equations|Phasor Maxwell equations]] · [[concepts/propagation-constant|Propagation constant]] · [[concepts/loss-tangent|Loss tangent]] · [[concepts/skin-depth|Skin depth]]

**[[concepts/index#polarization-reflection-standing-waves|Polarization, reflection, standing waves]]** — [[concepts/group-velocity|Group velocity]] · [[concepts/wave-polarization|Wave polarization]] · [[concepts/reflection-and-transmission|Reflection and transmission]] · [[concepts/standing-waves|Standing waves]] · [[concepts/radiation-pressure|Radiation pressure]]

**[[concepts/index#transmission-lines|Transmission lines]]** — [[concepts/telegraphers-equations|Telegrapher's equations]] · [[concepts/characteristic-impedance|Characteristic impedance]] · [[concepts/bounce-diagram|Bounce diagram]]

### [[0-toolkit/index|Toolkit]] — the mathematics assumed
[[0-toolkit/01-coordinates-and-differential-elements|Coordinates and differential elements]] · [[0-toolkit/02-vector-calculus-cheatsheet|Vector calculus cheat sheet]] · [[0-toolkit/03-units-and-constants|Units and constants]] · [[0-toolkit/04-errata-in-the-course-materials|Errata in the course materials]] · **[[0-toolkit/05-midterm-2-summary|Midterm 2 equation summary]]** · [[0-toolkit/06-prairielearn-guide|PrairieLearn guide (pl.vops.ch)]] · **[[0-toolkit/07-wave-parameters-map|Wave parameters on one page]]** · **[[0-toolkit/08-waves-in-media-figures|Waves in media — figures]]**

### [[practice/index|Practice problems]] — Lectures 2–30
Twelve problems per lecture (eight for Lecture 11), from two-minute checks to exam length, each with a folded hint and a worked solution: by difficulty — [[practice/easy|easy]] · [[practice/medium|medium]] · [[practice/hard|hard]] — or [[practice/topics|by topic]] across lectures. Every lecture page links to its own set.

### Cross-cutting
[[concepts/index|Topics]] · [[problems/index|Worked problems]] · [[practice/index|Practice problems]] · [[demos/index|Interactive demos]] · [[homework/index|Homework companions]] · [[2-magnetostatics/index#the-dictionary-electrostatics--magnetostatics|electrostatics ↔ magnetostatics dictionary]]

## By lecture

Each lecture page keeps the lecture's section headings, says in a few lines what happens in each section and which example it uses, and points to the topic page that carries the full treatment. Lectures 27–30 (transmission lines) are still full lecture pages.

### [[1-electrostatics/index|Unit 1 · Electrostatics]] — Lectures 1–11 (Exam 1: L1–10)
1. [[1-electrostatics/01-fields-forces-and-the-maxwell-roadmap|Fields, forces, and the Maxwell roadmap]]
2. [[1-electrostatics/02-coulombs-law-superposition-and-gauss|Coulomb's law, superposition, and the birth of Gauss's law]]
3. [[1-electrostatics/03-gauss-law-at-work|Gauss's law at work: flux, symmetry, and charge densities]]
4. [[1-electrostatics/04-divergence-and-curl|Divergence and curl: Maxwell's equations at a point]]
5. [[1-electrostatics/05-curl-free-fields-and-the-electrostatic-potential|Curl-free fields and the electrostatic potential]]
6. [[1-electrostatics/06-circulation-and-boundary-conditions|Circulation and boundary conditions]]
7. [[1-electrostatics/07-poisson-and-laplace|Poisson's and Laplace's equations]]
8. [[1-electrostatics/08-conductors-dielectrics-and-polarization|Conductors, dielectrics, and polarization]]
9. [[1-electrostatics/09-static-fields-in-dielectric-media|Static fields in dielectric media]]
10. [[1-electrostatics/10-capacitance-and-conductance|Capacitance and conductance]]
11. [[1-electrostatics/11-lorentz-drude-models-for-conductivity-and-susceptibility|Where σ and χe come from: the Lorentz–Drude models]] (not on Exam 1)

### [[2-magnetostatics/index|Unit 2 · Magnetostatics and induction]] — Lectures 12–15 (Midterm 2)
12. [[2-magnetostatics/12-magnetic-force-biot-savart-and-amperes-law|Magnetic force, Biot–Savart, and Ampère's law]]
13. [[2-magnetostatics/13-current-sheets-solenoids-and-the-vector-potential|Current sheets, solenoids, and the vector potential]]
14. [[2-magnetostatics/14-faradays-law-and-induced-emf|Faraday's law and induced emf]]
15. [[2-magnetostatics/15-inductance-magnetic-energy-and-the-potentials|Inductance, magnetic energy, and the potentials]]

The unit page carries the **[[2-magnetostatics/index#the-dictionary-electrostatics--magnetostatics|electrostatics ↔ magnetostatics dictionary]]** — every Unit 2 result beside its Unit 1 twin.

### [[3-maxwell-and-waves/index|Unit 3 · Maxwell's equations and waves]] — Lectures 16–26
16. [[3-maxwell-and-waves/16-charge-conservation-displacement-current-and-maxwells-equations|Charge conservation, displacement current, and Maxwell's equations]]
17. [[3-maxwell-and-waves/17-magnetization-and-maxwells-equations-in-matter|Magnetization current and Maxwell's equations in matter]]
18. [[3-maxwell-and-waves/18-the-wave-equation-and-plane-tem-waves|The wave equation and plane TEM waves]]
19. [[3-maxwell-and-waves/19-dalembert-solutions-and-radiation-from-current-sheets|d'Alembert solutions and radiation from current sheets]]
20. [[3-maxwell-and-waves/20-poynting-theorem-and-monochromatic-waves|Poynting's theorem and monochromatic waves]]
21. [[3-maxwell-and-waves/21-monochromatic-waves-and-phasor-notation|Monochromatic waves and phasor notation]]
22. [[3-maxwell-and-waves/22-phasor-maxwell-equations-and-damped-waves|Maxwell's equations in phasor form and damped waves in conducting media]]
23. [[3-maxwell-and-waves/23-imperfect-dielectrics-and-good-conductors|Imperfect dielectrics and good conductors]]
24. [[3-maxwell-and-waves/24-signal-transmission-and-circular-polarization|Signal transmission and circular polarization]]
25. [[3-maxwell-and-waves/25-wave-reflection-and-transmission|Wave reflection and transmission]]
26. [[3-maxwell-and-waves/26-standing-waves-and-radiation-pressure|Standing waves and radiation pressure]]

Lectures 20–26 follow the course notes (no slides).

### [[4-transmission-lines/index|Unit 4 · Transmission lines]] — Lectures 27–38
27. [[4-transmission-lines/27-guided-tem-waves-on-transmission-lines|Guided TEM waves on transmission lines]]
28. [[4-transmission-lines/28-distributed-circuits-and-bounce-diagrams|Distributed circuits and bounce diagrams]]
29. [[4-transmission-lines/29-bounce-diagram-examples|Bounce diagram examples]]
30. [[4-transmission-lines/30-multi-line-circuits|Multi-line circuits]]

Then: sinusoidal steady state and input impedance · quarter-wave transformers · the Smith chart · impedance matching — *planned*

## Conventions used throughout

| | this site writes | you may also see |
|---|---|---|
| vectors | bold: $\mathbf{E}$, $\mathbf{r}$ | $\vec{E}$ on the slides |
| unit vectors | $\hat{x},\hat{y},\hat{z}$, $\hat{r},\hat{\phi},\hat{\theta}$ | $\hat{a}_x$ on the slides |
| permittivity of free space | $\epsilon_0$ | $\epsilon_o$ in the course notes |
| charge densities | $\rho$ [C/m³], $\rho_s$ [C/m²], $\rho_l$ [C/m] | $\lambda$ for line charge |
| electric flux density | $\mathbf{D} = \epsilon_0\mathbf{E}$ (vacuum), $\epsilon_0\mathbf{E}+\mathbf{P}$ (matter) | "displacement flux density" |
| differential elements | $d\mathbf{l}$, $d\mathbf{S}$ (outward on closed surfaces), $dV$ | $d\mathbf{L}$, $d\mathbf{s}$ |
| Gauss's law | $\oint_S\mathbf{D}\cdot d\mathbf{S} = Q_{\text{enc}}$ | $\nabla\cdot\mathbf{E} = \rho/\epsilon_0$ (same thing in vacuum) |
| the constant | $\dfrac{1}{4\pi\epsilon_0}$, never "$k$" | $9\times10^9$ |

This follows the Midterm 1 formula sheet (the exam papers themselves write $\lambda$ for line charge and overbar vectors). Units go in square brackets after every result.

## Callouts

The notes use a few recurring boxes, so you can skim for what you need:

> [!key] Key
> The result to remember — a law, a boxed formula, a final answer.

> [!recipe] Recipe
> A procedure: how to actually do the calculation, step by step.

> [!trap] Trap
> A mistake that costs points, and how to avoid it. Several are taken from real exam keys.

> [!exam] Exam
> How the idea shows up on exams, with the FA26 Exam 1 mapping.

> [!intuition] Intuition
> The picture or analogy behind the mathematics.

> [!derivation]- Derivation (click to expand)
> Longer derivations are folded so the narrative stays readable. Expand when you want the details.

The [[practice/index|practice pages]] add their own five: the problem statement sits in an **easy**, **medium** or **hard** box (the difficulty tag, followed by topic tags), and the **hint** and **solution** below it are folded until you click them.

*Status: Lectures 1–30 are written (Toolkit, Units 1–3, Lectures 27–30 of Unit 4 — 20–30 from the course notes alone); Lectures 1–26 are maps onto 72 topic pages in 10 themes, with 24 worked problems and 344 practice problems; Lectures 31–38 are outlined. Sources: E. Kudeki, ECE 329 Lecture Notes (2026); lecture slides (Shao, adapted from Goddard and Cunningham); FA26 homework and Exam 1; N. N. Rao, Fundamentals of Electromagnetics for Electrical and Computer Engineering.*
