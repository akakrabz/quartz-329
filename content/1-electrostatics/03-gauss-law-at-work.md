---
title: "Lecture 3 — Gauss's law at work: flux, symmetry, and charge densities"
description: "Flux, Gauss's law restated, the three symmetric cases and their superposition (pn junction), charge densities and δ-functions, ∮B·dS = 0 — a map of the lecture; the content lives on the topic pages."
tags: [lecture, electrostatics, exam-1]
lecture: 3
---

*Lecture 3 · course notes §3 · slides "Surface integrals, connecting Coulomb's and Gauss's law" · prev: [[1-electrostatics/02-coulombs-law-superposition-and-gauss|Lecture 2]] · next: [[1-electrostatics/04-divergence-and-curl|Lecture 4]] · practice: [[practice/03-gauss-law-at-work|12 problems]]*

> [!abstract] In one breath
> The flux of $\mathbf{D}$ out of a closed surface always equals the charge inside. When symmetry makes $\lvert\mathbf{D}\rvert$ *constant* and *normal* on a well-chosen surface, the integral collapses to "$D\times$area" and $\mathbf{E}$ falls out in two lines. Three symmetries do this: spherical, cylindrical, planar. The rest of the lecture builds the tool (flux, densities, δ-functions) or superposes these three.

## 1. Flux: counting arrows through a surface

$\Delta\psi = \mathbf{F}\cdot\Delta\mathbf{S} = F_n\,\Delta S$ through a flat patch; tile and sum for $\psi = \int_S\mathbf{F}\cdot d\mathbf{S}$. The "trick that works sometimes" — $F\cdot A$ where the field is uniform and normal, zero where it is parallel — is the whole method. Closed surfaces: outward normal, $\oint_S$.

→ Full treatment: [[concepts/flux|Flux]]
## 2. Gauss's law, restated for use

$\psi_E = \oint_S\mathbf{D}\cdot d\mathbf{S} = Q_{\text{enc}}$ [C]. Concept checks by symmetry alone: $Q$ at the centre of a cube ($Q/6$ per face), of a thin box ($Q/2$ per big face), of a hemisphere's base ($Q/2$ through the dome, 0 through the base), above an infinite plane ($\pm Q/2$) — the in-class challenge question, worked with other numbers in [[problems/flux-through-a-plane-from-two-charges]].

→ Full treatment: [[concepts/gauss-law|Gauss's law]]
## 3. The three symmetries

Argue the symmetry, choose the surface, write "top + bottom + side = $Q_{\text{enc}}$", convert to $\mathbf{E}$ with units.

### 3a. Infinite line charge (cylindrical)
Coaxial cylinder, caps zero: $D\cdot2\pi rL = \rho_lL$, $\mathbf{E} = \dfrac{\rho_l}{2\pi\epsilon_0r}\hat{r}$ — Lecture 2's integral in one line.

### 3b. Infinite sheet (planar)
Pillbox, both caps: $2DA = \rho_sA$, $\mathbf{E} = \hat{z}\,\text{sgn}(z)\dfrac{\rho_s}{2\epsilon_0}$ — no distance dependence.

### 3c. Uniform slab (planar, with interior)
Same pillbox, $Q_{\text{enc}}$ depends on cap position: $\mathbf{E} = \dfrac{\rho x}{\epsilon_0}\hat{x}$ inside, $\dfrac{\rho W}{2\epsilon_0}\text{sgn}(x)\hat{x}$ outside — linear, then flat, continuous at the faces. Plus the table of fields to recognize on sight and the three pillbox traps.

→ Full treatment: [[concepts/symmetric-charge-distributions|Symmetric charge distributions]]
## 4. Superposition of the building blocks

Two opposite sheets → $\rho_s/\epsilon_0$ between, zero outside (a capacitor in embryo). The **pn junction**: two neutral slabs $-\rho_1$, $+\rho_2$ added with their plateaus — a triangular field peaking at $-\rho_1W_1/\epsilon_0$ at the junction, zero outside. Recognize the blocks, then superpose.

→ Full treatment: [[concepts/symmetric-charge-distributions|Symmetric charge distributions]] · [[concepts/superposition|Superposition]] · [[concepts/pn-junction|pn junction]]
## 5. Charge densities and δ-functions

Point, line and sheet charges written as volume densities with impulses ($Q\,\delta(x-x_0)\delta(y-y_0)\delta(z-z_0)$, …), units C/m³ each time, so $Q_{\text{enc}} = \int_V\rho\,dV$ covers every case.

→ Full treatment: [[concepts/charge-density|Charge densities and δ-functions]]
## 6. The magnetic counterpart: ∮ B·dS = 0

Magnetic field lines have no ends ("Yadaraf bugs" always return to their hole): $\psi_B = \oint_S\mathbf{B}\cdot d\mathbf{S} = 0$ for every closed surface — the second Maxwell equation. Open surfaces can carry magnetic flux (Faraday, Lecture 14).

→ Full treatment: [[concepts/magnetic-flux|Magnetic flux Ψ]]
## 7. Summary

- Flux = normal component × area, summed; closed surface = "flux out".
- $\oint_S\mathbf{D}\cdot d\mathbf{S} = Q_{\text{enc}}$ is always true, *useful* when symmetry makes $D$ constant on a sphere, cylinder or pillbox.
- Point $1/r^2$, line $1/r$, sheet constant, slab linear-then-constant; superpose.
- $\oint_S\mathbf{B}\cdot d\mathbf{S} = 0$.

> [!exam] On Exam 1
> FA26 problem 2 (slab with $\rho\propto\lvert x\rvert$: pillbox, both caps, $Q_{\text{enc}}$ as an integral, sgn, then a potential) and problem 4 (two-layer coax: Gaussian cylinder, $\mathbf{D}$ independent of material). Exam notes: [[concepts/symmetric-charge-distributions]] · [[concepts/gauss-law]] · [[concepts/charge-density]].

> [!tip] Practice this lecture
> [[practice/03-gauss-law-at-work|12 practice problems]] — 5 easy, 3 medium, 4 hard — each with a folded hint and a worked solution. Start with [[practice/03-gauss-law-at-work#31-two-sheets-of-charge|3.1 Two sheets of charge]]; the [[practice/index|practice hub]] has the whole bank by difficulty and by topic.

### Sources for this page
Kudeki notes, Lecture 3 (sheet, slab, two sheets, two slabs = pn junction, δ-function formalism, dipole flux example). Shao, Lecture 3 slides (flux intuition, "trick that works sometimes", symmetry ladder, challenge questions, line/sheet/slab derivations, Yadaraf bugs) and Lecture 4 whiteboard page (pn junction by superposition). Slips in the course material: see [[0-toolkit/04-errata-in-the-course-materials|errata]].
