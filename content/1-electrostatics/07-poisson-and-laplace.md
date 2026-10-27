---
title: "Lecture 7 — Poisson's and Laplace's equations"
description: "Gauss's law for the potential, ∇²V = −ρ/ε, its one-dimensional solutions, the pn junction's built-in potential, the Coulomb superposition integral and the Helmholtz theorem; the full treatment is on the topic pages linked from each section."
tags: [lecture, electrostatics, exam-1]
lecture: 7
---

*Lecture 7 · course notes §7 · slides "Boundary Conditions; Poisson's and Laplace's Equation" (second half) · prev: [[1-electrostatics/06-circulation-and-boundary-conditions|Lecture 6]] · next: [[1-electrostatics/08-conductors-dielectrics-and-polarization|Lecture 8]] · practice: [[practice/07-poisson-and-laplace|12 problems]]*

> [!abstract] In one breath
> $\mathbf{E} = -\nabla V$ solves $\nabla\times\mathbf{E} = 0$ once and for all; putting it into $\nabla\cdot\mathbf{D} = \rho$ leaves one **scalar** equation: **Poisson's equation** $\nabla^2V = -\rho/\epsilon$, or **Laplace's equation** $\nabla^2V = 0$ where there is no charge. In 1-D: integrate twice, fix two constants from boundary values — the workhorse of capacitance. The general solution is the superposition of point-charge potentials, which also proves Lecture 4's Helmholtz theorem.

## 1. From Gauss's law to Poisson's equation

$\nabla\cdot(\epsilon\nabla V) = -\rho$ becomes $\nabla^2V = -\rho/\epsilon$ only where $\epsilon$ is constant and the field is static; the Laplacian measures how far $V$ sits above or below its local average, so a charge-free $V$ has no interior bumps or dips. Uniqueness makes guessing legitimate; linearity lets solutions superpose.

→ Full treatment: [[concepts/poissons-equation|Poisson's and Laplace's equations]]

## 2. Solving Laplace's equation in one dimension

Planar $Az+B$, cylindrical $A\ln r+B$, spherical $A/r+B$; two constants from two conductor potentials, then $\mathbf{E}\to\mathbf{D}\to\rho_s = \hat{n}\cdot\mathbf{D}$. Examples: plates 2 m apart at 0 and $-3$ V ($V = -\tfrac32z$, $\mathbf{E} = \tfrac32\hat{z}$ V/m, plate charges $\pm\tfrac32\epsilon_0$ C/m²); copper blocks with $\pm2$ C/m² facing across 3 m ($V_p = -6/\epsilon_0$ V — the method, not the number, is the point).

→ Full treatment: [[concepts/poissons-equation|Poisson's and Laplace's equations]]

## 3. Poisson's equation where there is charge

Integrate $V'' = -\rho/\epsilon_0$ twice through the pn junction's two charge slabs and match at $x = 0$: built-in potential $V_{21} = \rho_2W_2(W_1+W_2)/2\epsilon_0$, positive side high, bowl in the negative slab and dome in the positive one, depletion width $W_1+W_2 = \sqrt{2\epsilon_0V_{21}(\rho_1+\rho_2)/(\rho_1\rho_2)}$. Where Laplace may and may not be used (charge inside, $\epsilon$ jumps) is the trap of the lecture.

→ Full treatment: [[concepts/pn-junction|The pn junction]] · [[concepts/poissons-equation|Poisson's and Laplace's equations]]

## 4. The general solution: superposition of point charges

$V(\mathbf{r}) = \int\rho(\mathbf{r}')\,d^3\mathbf{r}'/(4\pi\epsilon_0\lvert\mathbf{r}-\mathbf{r}'\rvert)$: Poisson's equation as a linear shift-invariant system whose impulse response is the point-charge potential (the Green's function), $\rho$ sifted into impulses.

→ Full treatment: [[concepts/helmholtz-theorem|Helmholtz's theorem]]

## 5. Helmholtz's theorem, finally proved

Split $\mathbf{F} = -\nabla V + \nabla\times\mathbf{A}$; divergence and curl give two Poisson equations, each solved by the superposition integral. Static $\mathbf{E}$ has only the first part, the magnetic field only the second ($\mathbf{A}$, Lecture 13); gauge freedom never changes $\mathbf{F}$.

→ Full treatment: [[concepts/helmholtz-theorem|Helmholtz's theorem]]

## 6. Summary

- $\nabla^2V = -\rho/\epsilon$ (Poisson), $\nabla^2V = 0$ (Laplace): Gauss's law for the potential, valid where $\epsilon$ is constant.
- 1-D solutions: linear (planar), logarithmic (cylindrical), $1/r$ (spherical); two constants from two boundary values.
- Chain: $V\to\mathbf{E}=-\nabla V\to\mathbf{D}\to\rho_s = \hat{n}\cdot\mathbf{D}$ on conductors.
- With charge present: integrate $V'' = -\rho/\epsilon_0$ twice, match $V$ at interfaces (pn junction: $V_{21} = \rho_2W_2(W_1+W_2)/2\epsilon_0$).
- General solution = Coulomb superposition; Helmholtz follows.

Concept pages: [[concepts/poissons-equation]] · [[concepts/pn-junction]] · [[concepts/helmholtz-theorem]].

> [!exam] On Exam 1
> Mostly *backwards*: $\rho = \epsilon_0\nabla\cdot\mathbf{E}$ (FA26 1(c)) or $\rho = -\epsilon_0\nabla^2V$. Forwards — integrate twice, constants from plate potentials — feeds Lectures 9–10 and HW3 #1. Know the three 1-D solutions cold. Exam notes: [[concepts/poissons-equation]], [[concepts/pn-junction]].

> [!tip] Practice this lecture
> [[practice/07-poisson-and-laplace|12 practice problems]] — 5 easy, 3 medium, 4 hard — each with a folded hint and a worked solution. Start with [[practice/07-poisson-and-laplace#71-two-plates-two-potentials|7.1 Two plates, two potentials]]; the [[practice/index|practice hub]] has the whole bank by difficulty and by topic.

### Sources for this page
Kudeki notes, Lecture 7 (Poisson and Laplace; Examples 1–4, "Notice" on zero field in conductors; general solution as LSI impulse response / Green's function; Helmholtz and gauge). Shao, Lectures 6–7 slides (Laplacian; "just Gauss's law in terms of potentials"; "$\epsilon$ = const" and "static" conditions; parallel plates with $\mathbf{E}\to\mathbf{D}\to\rho_s$; layered-dielectric sketch). Slips in the course material (including a Lecture 10 slide's "$V(z) = V_0x/d$"): see [[0-toolkit/04-errata-in-the-course-materials|errata]].
