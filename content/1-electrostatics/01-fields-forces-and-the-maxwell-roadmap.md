---
title: "Lecture 1 — Fields, forces, and the Maxwell roadmap"
description: "What a field is, how E and B are defined through the Lorentz force, the four Maxwell equations as the course roadmap, and dl and dS — a map of the lecture; the content lives on the topic pages."
tags: [lecture, electrostatics, exam-1]
lecture: 1
---

*Lecture 1 · course notes §1 · slides "Introduction" · assumes MATH 241 vectors and PHYS 212 · next: [[1-electrostatics/02-coulombs-law-superposition-and-gauss|Lecture 2]]*

> [!abstract] In one breath
> Two **vector fields**, $\mathbf{E}(\mathbf{r},t)$ and $\mathbf{B}(\mathbf{r},t)$, defined by the force on a test charge, describe how charges push on charges. Maxwell's four equations say how charges and currents *create* them; the course is those equations — static, then time-varying, then waves on cables. Today: definitions, roadmap, and the vectors we integrate along ($d\mathbf{l}$) and through ($d\mathbf{S}$).

## 1. Why fields at all?

A field assigns a number (scalar) or a vector to every point and time; it makes action at a distance tractable. $\mathbf{E}$ and $\mathbf{B}$ are defined operationally by the Lorentz force $\mathbf{F} = q(\mathbf{E}+\mathbf{v}\times\mathbf{B})$: $\mathbf{E}$ in V/m, $\mathbf{B}$ in T. Two facts for later: fields mix between reference frames (why the equations are coupled), and charge comes in both signs while mass does not (why gravity wins macroscopically).

→ Full treatment: [[concepts/electric-field|Electric field E]] · [[concepts/lorentz-force|Lorentz force]]
## 2. The roadmap: Maxwell's equations on day one

The four equations in free space, differential form, with $\mu_0$, $\epsilon_0$ and $c = 1/\sqrt{\mu_0\epsilon_0}$; how to read the table (divergence column = what fields emanate from, curl column = what makes them circulate). Two consequences: statics decouple into a curl-free $\mathbf{E}$ fixed by charge and a divergence-free $\mathbf{B}$ fixed by current; with the time derivatives kept, waves at $c$ with $\lambda = c/f$. Quasi-statics: a circuit is a circuit while $L\ll\lambda$ ($T\gg L/c$); $c = 30$ cm/ns, so a 3 GHz clock has $\lambda = 10$ cm.

→ Full treatment: [[concepts/maxwells-equations|Maxwell's equations]]
## 3. Units and the source → field bookkeeping

Charges → $\mathbf{E}$ (V/m), $\mathbf{D}$ (C/m²); currents → $\mathbf{H}$ (A/m), $\mathbf{B}$ (T); the density ladder $Q$, $\rho_l$, $\rho_s$, $\rho$ and $I$, $\mathbf{J}_s$, $\mathbf{J}$. Table and unit checks: [[0-toolkit/03-units-and-constants|Units and constants]] · [[concepts/charge-density|Charge densities]].

## 4. Vector algebra you must be fluent in (review at home)

Components $\mathbf{A} = A_x\hat{x}+A_y\hat{y}+A_z\hat{z}$, magnitude $|\mathbf{A}| = \sqrt{A_x^2+A_y^2+A_z^2}$, unit vector $\hat{a} = \mathbf{A}/|\mathbf{A}|$; the separation vector $\mathbf{R}_{12} = \mathbf{r}_2 - \mathbf{r}_1$ (final minus initial; $\hat{R}_{12}$ points from 1 toward 2 — every Coulomb's-law calculation uses it); dot product as projection, cross product by determinant and the right-hand rule. In-class discussion problem: $\mathbf{A} = 3\hat{x}+2\hat{y}+\hat{z}$, $\mathbf{B} = \hat{x}+\hat{y}-\hat{z}$, $\mathbf{C} = \hat{x}+2\hat{y}+3\hat{z}$ give $\mathbf{B}\times\mathbf{C} = \hat{x}(1\cdot3-(-1)\cdot2) - \hat{y}(1\cdot3-(-1)\cdot1) + \hat{z}(1\cdot2-1\cdot1) = 5\hat{x}-4\hat{y}+\hat{z}.$ Then $\mathbf{A}\cdot(\mathbf{B}\times\mathbf{C}) = 3\cdot5 + 2\cdot(-4) + 1\cdot1 = 8$, the signed volume of the parallelepiped. Review: [[0-toolkit/02-vector-calculus-cheatsheet|Vector calculus cheat sheet]].

## 5. The two new tools: dl and dS

$d\mathbf{l}$ is a tangent step ($\int\mathbf{F}\cdot d\mathbf{l}$ sums the tangential component: work, voltage); $d\mathbf{S} = d\mathbf{l}_1\times d\mathbf{l}_2$ is a normal patch ($\int\mathbf{F}\cdot d\mathbf{S}$ sums the normal component: flux). The order of the cross product sets the orientation; closed surfaces are outward. Cylindrical and spherical elements: [[0-toolkit/01-coordinates-and-differential-elements]].

→ Full treatment: [[concepts/differential-elements|Differential elements dl, dS, dV]]
## 6. Where this goes next

Lecture 2: Coulomb's law, superposition, Gauss's law (first Maxwell equation). Lecture 3: Gauss's law as a tool (line, sheet, slab); δ-function point charges. Lecture 4: divergence and curl form.

> [!exam] What Lecture 1 contributes to Exam 1
> Nothing directly, but every problem uses it: vector components, the $\mathbf{R}_{12}$ convention, $d\mathbf{l}$ in a line integral, outward $d\mathbf{S}$ on a Gaussian surface, and units on every answer. Exam notes: [[concepts/differential-elements]] · [[concepts/electric-field]].

### Sources for this page
Kudeki, *ECE 329 Lecture Notes*, Lecture 1 (big picture; frame-dependence of fields; quasi-statics). Shao, Lecture 1 slides (units table, $d\mathbf{l}$/$d\mathbf{S}$ construction, discussion problem). Rao, *Fundamentals of Electromagnetics for Electrical and Computer Engineering*, ch. 1. Slips in the course material: see [[0-toolkit/04-errata-in-the-course-materials|errata]].
