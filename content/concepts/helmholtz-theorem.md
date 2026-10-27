---
title: "Helmholtz's theorem"
description: "A field that vanishes at infinity is fixed by its divergence and curl: F = −∇V + ∇×A, each potential a Coulomb-type integral of one source. Proved from the general solution of Poisson's equation, the superposition of point-charge potentials."
tags: [concept, electrostatics]
aliases: ["Helmholtz decomposition", "general solution of Poisson's equation", "Green's function", "impulse response", "superposition integral", "gauge freedom"]
---

> [!key] General solution of Poisson's equation, and Helmholtz's theorem
> For finite charge with $V\to0$ at infinity,
> $$
> V(\mathbf{r}) = \int\frac{\rho(\mathbf{r}')}{4\pi\epsilon_0\,\lvert\mathbf{r}-\mathbf{r}'\rvert}\,d^3\mathbf{r}',\qquad d^3\mathbf{r}' = dx'\,dy'\,dz',
> $$
> over the region where $\rho\neq0$; $\mathbf{r}$ field point, $\mathbf{r}'$ source point. Any field $\mathbf{F}$ vanishing at infinity splits as
> $$
> \mathbf{F} = \underbrace{-\nabla V}_{\text{curl-free}} + \underbrace{\nabla\times\mathbf{A}}_{\text{divergence-free}},
> $$
> with $V$ and $\mathbf{A}$ the Poisson-type integrals of $\nabla\cdot\mathbf{F}$ and $\nabla\times\mathbf{F}$ below: **divergence and curl are a field's complete sources**.

**Physics.** In ECE 210 terms, [[concepts/poissons-equation|Poisson's equation]] is a **linear, shift-invariant** system, input $\rho$, output $V$. Its **impulse response** (to $\rho = \delta(\mathbf{r})$, a unit point charge at the origin) is the point-charge potential $1/(4\pi\epsilon_0\lvert\mathbf{r}\rvert)$; shifted to $\mathbf{r}'$, $1/(4\pi\epsilon_0\lvert\mathbf{r}-\mathbf{r}'\rvert)$ — the **Green's function**. Any $\rho$ is a superposition of impulses, $\rho(\mathbf{r}) = \int\rho(\mathbf{r}')\,\delta(\mathbf{r}-\mathbf{r}')\,d^3\mathbf{r}'$ (sifting), so by linearity $V$ is the same superposition of shifted responses — the integral above, Lecture 5's [[concepts/electrostatic-potential|superposition of point-charge potentials]]. For infinite distributions the integral diverges; a finite reference ("$V(0)=0$") renormalizes it.

Lecture 4 claimed that a field vanishing at infinity is fixed by its divergence and curl ([[1-electrostatics/04-divergence-and-curl#7-the-differential-form-of-maxwells-equations|Lecture 4 §7]]); the general solution proves it.

> [!derivation]- Proof from two Poisson equations
> Split $\mathbf{F} = -\nabla V + \nabla\times\mathbf{A}$. Divergence and curl of both sides give $\nabla^2V = -\nabla\cdot\mathbf{F}$ and (gauge $\nabla\cdot\mathbf{A} = 0$) $\nabla^2\mathbf{A} = -\nabla\times\mathbf{F}$ — two Poisson equations, with $\nabla\cdot\mathbf{F}$ and $\nabla\times\mathbf{F}$ as $\rho/\epsilon_0$:
> $$
> V(\mathbf{r}) = \int\frac{\nabla'\cdot\mathbf{F}(\mathbf{r}')}{4\pi\lvert\mathbf{r}-\mathbf{r}'\rvert}d^3\mathbf{r}',\qquad
> \mathbf{A}(\mathbf{r}) = \int\frac{\nabla'\times\mathbf{F}(\mathbf{r}')}{4\pi\lvert\mathbf{r}-\mathbf{r}'\rvert}d^3\mathbf{r}' .
> $$
> Each is the general solution of its Poisson equation, so both potentials — and hence $\mathbf{F}$ — are determined by the two sources alone.

**The two halves of the course.** Static $\mathbf{E}$: no curl part ([[concepts/conservative-field|Conservative (curl-free) fields and the potential]]), $V$ is the Coulomb integral. Unit 2's magnetic field: no divergence part; $\mathbf{A}$ — the [[concepts/vector-potential|vector potential]] of [[2-magnetostatics/13-current-sheets-solenoids-and-the-vector-potential#5-the-vector-potential|Lecture 13 §5]] — carries everything. $V$ is fixed up to a constant, $\mathbf{A}$ up to a gradient; this **gauge freedom** never changes $\mathbf{F}$.

> [!trap]
> - The theorem needs $\mathbf{F}\to0$ at infinity; a uniform field has zero divergence and curl yet is not zero.
> - "Curl-free" fixes the *form* $\mathbf{E} = -\nabla V$; it does not fix $V$ — that takes the divergence (the charge).
> - $\nabla'$ in the integrals differentiates with respect to the source point $\mathbf{r}'$, not the field point.

> [!exam] On exams
> Not asked directly. It is the reason "find $\rho$ from $\mathbf{E}$" ($\rho = \epsilon_0\nabla\cdot\mathbf{E}$) and "find $V$ from $\rho$" (the superposition integral) are inverses of each other, and why a static $\mathbf{E}$ is completely specified by $\rho$.

**Where it appears.** [[1-electrostatics/07-poisson-and-laplace#4-the-general-solution-superposition-of-point-charges|Lecture 7 §4]] (general solution), [[1-electrostatics/07-poisson-and-laplace#5-helmholtzs-theorem-finally-proved|Lecture 7 §5]] (proof); claimed in [[1-electrostatics/04-divergence-and-curl#7-the-differential-form-of-maxwells-equations|Lecture 4 §7]]; the magnetic half in [[2-magnetostatics/13-current-sheets-solenoids-and-the-vector-potential#5-the-vector-potential|Lecture 13 §5]].

**Related.** [[concepts/poissons-equation|Poisson's and Laplace's equations]] · [[concepts/divergence|Divergence]] · [[concepts/curl|Curl]] · [[concepts/conservative-field|Conservative (curl-free) fields and the potential]] · [[concepts/electrostatic-potential|Electrostatic potential V]] · [[concepts/vector-potential|Vector potential]].

**Practice.** [[practice/topics#divergence-curl-and-the-integral-theorems|Divergence, curl and the integral theorems]] (21 problems) — for example [[practice/04-divergence-and-curl#41-faucet-or-whirlpool|4.1 Faucet or whirlpool]] (easy), [[practice/04-divergence-and-curl#46-three-fields-in-curved-coordinates|4.6 Three fields in curved coordinates]] (medium), [[practice/04-divergence-and-curl#49-electrostatic-or-not|4.9 Electrostatic or not]] (hard).
