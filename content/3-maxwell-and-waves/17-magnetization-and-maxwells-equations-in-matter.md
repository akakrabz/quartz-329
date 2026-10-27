---
title: "Lecture 17 — Magnetization current and Maxwell's equations in matter"
description: "Atomic current loops add up to a magnetization M whose bound currents are absorbed into H = B/μ₀ − M, giving Maxwell's equations in matter, B = μH, and the three classes of magnetic material; the full treatment is on the topic pages linked from each section."
tags: [lecture, waves]
lecture: 17
---

*Lecture 17 · course notes §17 · slides "Magnetic Materials / Maxwell's equations in material media" · prev: [[3-maxwell-and-waves/16-charge-conservation-displacement-current-and-maxwells-equations|Lecture 16]] · next: [[3-maxwell-and-waves/18-the-wave-equation-and-plane-tem-waves|Lecture 18]] · practice: [[practice/17-magnetization-and-maxwell-in-matter|12 problems]]*

> [!abstract] In one breath
> Lecture 16's equations count *every* charge, including the roughly $10^{30}$ bound electrons per cubic metre in a metal, so we average. Bound electrons circulate (orbits, spins) as tiny loops whose moments add up to the **magnetization** $\mathbf{M}$; where it changes or ends, a **magnetization current** $\nabla\times\mathbf{M}$ (surface: $\mathbf{M}\times\hat n$) survives. Folding it into $\mathbf{H} = \mathbf{B}/\mu_0 - \mathbf{M}$ keeps Maxwell's equations with free sources only. Mostly $\mathbf{M} = \chi_m\mathbf{H}$ — no $\mu_0$ — so $\mathbf{B} = \mu\mathbf{H}$, $\mu = \mu_0(1+\chi_m)$. Dia- and paramagnets ($\lvert\chi_m\rvert$ around $10^{-5}$) are nearly vacuum; ferromagnets ($\chi_m$ from hundreds to hundreds of thousands) are non-linear with memory.

## 1. Why matter needs new bookkeeping

The microscopic equations need every charge (about $2.5\times10^{21}$ electrons per mm³ of copper); averaging splits sources into free and bound: $\rho = \rho_f - \nabla\cdot\mathbf{P}$, $\mathbf{J} = \mathbf{J}_f + \partial\mathbf{P}/\partial t + \nabla\times\mathbf{M}$, with a table of where each term was first met.

→ Full treatment: [[concepts/magnetization|Magnetization M and magnetization current]]

## 2. Atomic magnetic dipoles

An orbiting electron is a loop $\mathbf{m} = I\mathbf{A}$ feeling the torque $\mathbf{m}\times\mathbf{B}$ (square-loop derivation folded on the topic page); orbital, spin and nuclear sources; $\mathbf{M} = N\mathbf{m}$ in A/m. Site example: the Bohr orbit gives $m\approx9.28\times10^{-24}$ A·m², the Bohr magneton; saturated iron reaches $\mu_0M\approx2.2$ T.

→ Full treatment: [[concepts/magnetization|Magnetization]] · [[concepts/magnetic-dipole|Magnetic dipole]] (the loop dipole)

## 3. The magnetization current

Bound charge conserves itself, so the bound current beyond $\partial\mathbf{P}/\partial t$ is a curl: $\mathbf{J}_M = \nabla\times\mathbf{M}$, with the site's surface term $\mathbf{M}\times\hat n$ from the loop lattice (interior edges cancel, boundary edges survive). A magnetized rod is a solenoid with $nI\to M$: a 1.3 T magnet acts like 1000 turns/m at 1000 A.

→ Full treatment: [[concepts/magnetization|Magnetization]]

## 4. H redefined: Maxwell's equations in matter

Moving $\nabla\times\mathbf{M}$ to the left of Ampère–Maxwell defines $\mathbf{H} = \mathbf{B}/\mu_0 - \mathbf{M}$ and gives the four equations in their free-space form with free sources only; linear media $\mathbf{M} = \chi_m\mathbf{H}$ (no $\mu_0$), $\mathbf{B} = \mu\mathbf{H}$.

→ Full treatment: [[concepts/permeability|Permeability, susceptibility, and B = μH]]

### The solenoid with a core

The notes' cored solenoid: $\mathbf{H} = nI_0\hat z$ in core and air, $\mathbf{B}$ larger by $\mu_r$ in the core (site numbers: 2.51 mT → 0.251 T at $\mu_r = 100$); $L\propto\mu$; the demagnetization caveat.

→ Full treatment: [[concepts/permeability|Permeability]] (the solenoid with a core)

## 5. Dia-, para- and ferromagnetism

Three classes by mechanism and sign of $\chi_m$: induced orbital moments (dia, Lenz), permanent moments partly aligned (para), spontaneous alignment in domains (ferro, with hysteresis, remanence, coercivity, saturation). The slides' table of $\chi_m$ and $\mu_r$ values from bismuth to superalloy.

→ Full treatment: [[concepts/magnetic-materials|Dia-, para- and ferromagnetism]]

## 6. Boundary conditions in magnetic media

$B_n$ continuous ($\mu_1H_{1n} = \mu_2H_{2n}$), $H_t$ jumps by free $\mathbf{J}_s$; without it $B$-lines refract with $\tan\theta_1/\tan\theta_2 = \mu_1/\mu_2$ (iron → air: 85° becomes 0.13°). Recipe: $\mathbf{H}$ from free currents, $\mathbf{B} = \mu\mathbf{H}$ region by region, $\mathbf{M}$ last. Slide example: slab $\mu_r = 100$ between sheets $\mp0.1\hat y$ A/m — $\mathbf{H} = 0.1\hat x$ A/m with or without the slab, $\mathbf{B}$ 100 times larger inside it, $\mathbf{M} = 9.9\hat x$ A/m.

→ Full treatment: [[concepts/boundary-conditions|Boundary conditions]] · [[concepts/permeability|Permeability]] (recipe) · [[concepts/magnetization|Magnetization]] (slab example)

## 7. The dictionary: polarization ↔ magnetization

Row-by-row translation (dipole, bound sources, auxiliary field, linear law, continuity at interfaces, circuit element) and the four places it is not a straight translation: $\epsilon_0$ vs none, $-\nabla\cdot\mathbf{P}$ vs $+\nabla\times\mathbf{M}$, $\mathbf{D}$ adds vs $\mathbf{H}$ subtracts, $\chi_m$ of either sign.

→ Full treatment: [[concepts/magnetization|Magnetization]] (dictionary table)

## 8. Summary

- $\mathbf{J}_M = \nabla\times\mathbf{M}$, surface $\mathbf{M}\times\hat n$; $\mathbf{H}\equiv\mathbf{B}/\mu_0-\mathbf{M}$, set by free currents; $\mathbf{B} = \mu\mathbf{H}$, $\mathbf{M} = \chi_m\mathbf{H}$ (no $\mu_0$).
- Dia $\chi_m<0$, para small $>0$, ferro $\gg1$. $B_n$ continuous; $H_t$ too unless free $J_s$.

Concept pages: [[concepts/magnetization]] · [[concepts/permeability]] · [[concepts/magnetic-materials]] · [[concepts/maxwells-equations]] · [[concepts/boundary-conditions]] · [[concepts/magnetic-field]] · [[concepts/inductance]] · [[concepts/polarization]]. Worked problem: [[problems/fields-across-a-magnetic-interface]].

> [!exam] On exams
> None named; the site's guess: the slab-and-sheets problem with the $\mu_r = 1$ comparison and "no $\mu_0$" — [[concepts/permeability]], [[concepts/magnetization]]; classify from $\chi_m$ or $\mu_r$ — [[concepts/magnetic-materials]]; $\mathbf{H} = \mathbf{B}/\mu_0-\mathbf{M}$, $\mathbf{J}_M = \nabla\times\mathbf{M}$; interface problems with $\epsilon\to\mu$ — [[concepts/boundary-conditions]].

> [!tip] Practice this lecture
> [[practice/17-magnetization-and-maxwell-in-matter|12 practice problems]] — 5 easy, 3 medium, 4 hard — each with a folded hint and a worked solution. Start with [[practice/17-magnetization-and-maxwell-in-matter#171-moment-and-torque-on-a-loop|17.1 Moment and torque on a loop]]; the [[practice/index|practice hub]] has the whole bank by difficulty and by topic.

### Sources for this page
Kudeki notes, Lecture 17, with footnotes 3, 4, 6. Shao, Lecture 17 slides: moments, torque, "no μ₀", $\mu_r$ table, slab example, concept map. This site's own: $\mathbf{M}\times\hat n$, loop lattice, square-loop torque, "this site's numbers", demagnetization, iron refraction, bound-current check, dictionary; verified in `verify_L17.py`. Slips in the course material: see [[0-toolkit/04-errata-in-the-course-materials|errata]].
