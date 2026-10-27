---
title: "Lecture 8 — Conductors, dielectrics, and polarization"
description: "Conductors (E = 0 inside, equipotential, surface charge), dielectrics (bound charge, polarization P), the displacement field D = ε₀E + P and the linear law D = εE; the full treatment is on the topic pages linked from each section."
tags: [lecture, electrostatics, exam-1]
lecture: 8
---

*Lecture 8 · course notes §8 · slides "Conductors" and "Dielectrics" · prev: [[1-electrostatics/07-poisson-and-laplace|Lecture 7]] · next: [[1-electrostatics/09-static-fields-in-dielectric-media|Lecture 9]] · practice: [[practice/08-conductors-dielectrics-and-polarization|12 problems]]*

> [!abstract] In one breath
> Matter is made of charges that respond to the field. **Free** charges (a conductor) move until nothing pushes them: zero interior field, an equipotential body, all charge on the surface. **Bound** charges (a dielectric) only shift, turning each atom into a tiny dipole; their sum, the **polarization** $\mathbf{P}$, opposes the applied field and *weakens* the interior field without cancelling it. $\mathbf{D} \equiv \epsilon_0\mathbf{E} + \mathbf{P}$ hides the bound charge, so $\nabla\cdot\mathbf{D} = \rho$ needs only the charge you placed. For ordinary materials $\mathbf{P}\propto\mathbf{E}$ and it all collapses into one number: $\mathbf{D} = \epsilon\mathbf{E}$.

## 1. Two ideal materials

Ohm's law $\mathbf{J} = \sigma\mathbf{E}$ defines the conductivity ($R = l/\sigma A$ for a block); conductivities run from copper's $6\times10^7$ S/m to quartz's $10^{-17}$. The two idealizations: PEC ($\sigma\to\infty$, $\mathbf{E} = 0$ inside — a short) and perfect dielectric ($\sigma\to0$, $\mathbf{J} = 0$ — an open).

→ Full treatment: [[concepts/conductors|Conductors in electrostatics]]

## 2. Conductors in electrostatics

A slab in $\mathbf{E}_0$ polarizes its free charge until the induced $\pm\rho_s$ cancel the field inside: $\mathbf{E} = 0$, $V$ constant, charge only on the surface, $\hat{n}\cdot\mathbf{D} = \rho_s$ and $\mathbf{E}\perp$ surface outside. Interior charge relaxes as $e^{-t/\tau}$, $\tau = \epsilon/\sigma$ ($10^{-19}$ s copper, 0.2 ns sea water). Examples: neutral slab between sheets $\rho_A$, $\rho_B$ (faces $\pm\tfrac12(\rho_B-\rho_A)$); point charge over a grounded plane (field zero below, induced total $-Q$, non-uniform, normal).

→ Full treatment: [[concepts/conductors|Conductors in electrostatics]]

## 3. Dielectrics: bound charge and polarization

Bound electrons shift, each atom becomes a dipole $\mathbf{p} = q\mathbf{d}$; $\mathbf{P} = N\mathbf{p}$ [C/m²] leaves $\rho_{sb} = \mathbf{P}\cdot\hat{n}$ on faces and $\rho_b = -\nabla\cdot\mathbf{P}$ in the bulk. The lattice-of-dipoles average gives $\mathbf{E}_p = -\mathbf{P}/\epsilon_0$ inside a slab polarized normal to its faces: reduced, not zero.

→ Full treatment: [[concepts/polarization|Polarization P and bound charge]]

## 4. The displacement field D, and Gauss's law in matter

$\epsilon_0\mathbf{E}+\mathbf{P} = \epsilon_0\mathbf{E}_0$ in the slab motivates $\mathbf{D}\equiv\epsilon_0\mathbf{E}+\mathbf{P}$ with $\nabla\cdot\mathbf{D} = \rho_f$: Gauss's law counts free charge only; the boundary conditions survive with free $\rho_s$, and $\hat{n}\cdot(\mathbf{P}_1-\mathbf{P}_2) = -\rho_{sb}$. "$\mathbf{D}$ same inside and out" is a slab result, not a law (sphere: $-\mathbf{P}/3\epsilon_0$).

→ Full treatment: [[concepts/electric-flux-density|Electric flux density D]]

## 5. Linear dielectrics: χe, εr, and ε

$\mathbf{P} = \epsilon_0\chi_e\mathbf{E}$ (total field) gives $\mathbf{D} = \epsilon\mathbf{E}$, $\epsilon = \epsilon_0(1+\chi_e) = \epsilon_r\epsilon_0$; typical $\epsilon_r$ from air 1.0006 to water 81. Examples: the slab between charged sheets three ways ($E = E_a/(1+\chi_e)$, $\rho_{sb} = \chi_e\rho_{s0}/(1+\chi_e)$; via $\mathbf{D}$ in one line); HW4 #5 copper plates with $\mathbf{E} = 3\hat{z}$ V/m — vacuum, then an $81\epsilon_0$ fluid ($\mathbf{E} = \tfrac1{27}\hat{z}$, $\mathbf{P} = \tfrac{80}{27}\epsilon_0\hat{z}$), then salt water (shorted).

→ Full treatment: [[concepts/permittivity|Permittivity, susceptibility, and D = εE]]

## 6. Summary

- Conductors: $\mathbf{J} = \sigma\mathbf{E}$; in equilibrium $\mathbf{E} = 0$ inside, $V$ constant, $\rho = 0$ inside, $\rho_s = \hat{n}\cdot\mathbf{D}$ and $\mathbf{E}\perp$ surface outside. Equilibrium is reached in $\tau = \epsilon/\sigma$.
- Dielectrics: bound charges shift, $\mathbf{P} = N\mathbf{p}$ [C/m²]; bound charges $\rho_{sb} = \mathbf{P}\cdot\hat{n}$, $\rho_b = -\nabla\cdot\mathbf{P}$; field reduced, not zero.
- $\mathbf{D} = \epsilon_0\mathbf{E}+\mathbf{P}$: Gauss's law counts free charge only; boundary conditions unchanged.
- Linear media: $\mathbf{P} = \epsilon_0\chi_e\mathbf{E}$ (total field), $\mathbf{D} = \epsilon\mathbf{E}$, $\epsilon = \epsilon_0(1+\chi_e) = \epsilon_r\epsilon_0$.

Concept pages: [[concepts/conductors]] · [[concepts/polarization]] · [[concepts/electric-flux-density]] · [[concepts/permittivity]].

> [!exam] On Exam 1
> FA26 3(c): $\mathbf{P} = \mathbf{D} - \epsilon_0\mathbf{E} = (\epsilon_r-1)\epsilon_0\mathbf{E}$ on both sides of an interface (traps: $\mathbf{D}-\epsilon\mathbf{E}\equiv0$; $\chi_e\mathbf{E}$ lacks $\epsilon_0$). 4(c): the coax's outer conductor carries $-\lambda$ inside. Exam notes: [[concepts/permittivity]], [[concepts/conductors]]; worked in [[problems/fields-across-a-dielectric-interface]], [[problems/two-layer-coaxial-capacitor]].

> [!tip] Practice this lecture
> [[practice/08-conductors-dielectrics-and-polarization|12 practice problems]] — 5 easy, 3 medium, 4 hard — each with a folded hint and a worked solution. Start with [[practice/08-conductors-dielectrics-and-polarization#81-resistance-of-a-copper-wire|8.1 Resistance of a copper wire]]; the [[practice/index|practice hub]] has the whole bank by difficulty and by topic.

### Sources for this page
Kudeki notes, Lecture 8 (conductivity limits; conducting slab; relaxation time; dipole-lattice $\mathbf{E}_p = -\mathbf{P}/\epsilon_0$; $\mathbf{D}$ and Gauss for free charge; $\chi_e$, $\epsilon_r$ table; boundary conditions in media; dielectric-sphere footnote). Shao, Lecture 8 slides (resistor → conductivity; conductivity table; PEC build-up; conductor facts; slab between sheets; point charge over a plane) and Lecture 9 slides (polarized lattice; "reduced but not zero"; total-field correction; $E_a/(1+\chi_e)$ slab; $\epsilon = \epsilon_0\epsilon_r$). FA26 HW4 #5. Slips in the course material: see [[0-toolkit/04-errata-in-the-course-materials|errata]].
