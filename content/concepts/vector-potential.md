---
title: "Vector potential"
description: "Because ∇·B = 0, B = ∇×A for some vector field A (Wb/m). A is fixed only up to a gradient; the Coulomb gauge ∇·A = 0 turns Ampère's law into ∇²A = −μ₀J, Poisson's equation with a vector source, solved by the Coulomb integral. With time variation, E = −∇Φ − ∂A/∂t."
tags: [concept, magnetostatics]
aliases: ["magnetic vector potential", "Coulomb gauge", "gauge transformation"]
---

> [!key] Definition
> $$
> \begin{gathered}
> \mathbf{B} = \nabla\times\mathbf{A}\quad[\mathbf{A}\ \text{in Wb/m}],\qquad \nabla\cdot\mathbf{A} = 0\ \ (\text{Coulomb gauge}),\\[4pt]
> \nabla^2\mathbf{A} = -\mu_0\mathbf{J},\qquad \mathbf{A}(\mathbf{r}) = \int\frac{\mu_0\mathbf{J}(\mathbf{r}')}{4\pi\lvert\mathbf{r}-\mathbf{r}'\rvert}d^3r' .
> \end{gathered}
> $$
> Any $\mathbf{A}$ gives a divergence-free curl ($\nabla\cdot\nabla\times\mathbf{A} = 0$ identically), and any divergence-free $\mathbf{B}$ can be written this way. Replacing $\mathbf{A}$ by $\mathbf{A}+\nabla\lambda$ changes nothing in $\mathbf{B}$ (since $\nabla\times\nabla\lambda = 0$): this **gauge freedom** is the magnetic analogue of adding a constant to $V$, and it is spent by prescribing $\nabla\cdot\mathbf{A}$.

**Physics.** The scalar potential existed because $\nabla\times\mathbf{E} = 0$; the vector potential exists because $\nabla\cdot\mathbf{B} = 0$. In the Coulomb gauge the identity $\nabla\times\nabla\times\mathbf{A} = \nabla(\nabla\cdot\mathbf{A}) - \nabla^2\mathbf{A}$ loses its first term, and $\nabla\times\mathbf{B} = \mu_0\mathbf{J}$ becomes a Poisson equation for each Cartesian component of $\mathbf{A}$ with the same Green's function as electrostatics — so $\mathbf{A}$ is "$V$ with $\rho/\epsilon_0\to\mu_0\mathbf{J}$". The integral solution is itself divergence-free provided $\nabla\cdot\mathbf{J} = 0$, i.e. for steady currents ([[concepts/continuity-equation]]). In this gauge $\mathbf{A}$ has a physical meaning: potential *momentum* per unit charge, as $V$ is potential energy per unit charge. The flux through a loop is the circulation of $\mathbf{A}$: $\Psi = \int_S\mathbf{B}\cdot d\mathbf{S} = \oint_C\mathbf{A}\cdot d\mathbf{l}$ by Stokes.

**With time variation.** $\nabla\cdot\mathbf{B} = 0$ survives, so $\mathbf{B} = \nabla\times\mathbf{A}$ survives; Faraday's law then says $\nabla\times(\mathbf{E}+\partial\mathbf{A}/\partial t) = 0$, so

$$
\mathbf{E} = -\nabla\Phi - \frac{\partial\mathbf{A}}{\partial t},\qquad\text{gauge freedom}\quad \mathbf{A}\to\mathbf{A}+\nabla\lambda,\ \ \Phi\to\Phi-\frac{\partial\lambda}{\partial t}.
$$

The $-\partial\mathbf{A}/\partial t$ term is the induced, circulating part of $\mathbf{E}$ — the part that makes voltmeter readings path-dependent ([[concepts/electromotive-force]]). Four potential components replace six field components, and the two homogeneous Maxwell equations are satisfied automatically.

**Example.** The circular loop of radius $a$: $\mathbf{J} = I\delta(z')\delta(r'-a)\hat\phi'$ reduces the $\mathbf{A}$ integral to a single $\phi'$ integral with $A_z = 0$; curling it gives $B_x$, $B_z$ on the plane $y = 0$ as elliptic-type integrals, and on the axis the closed form $B_z = \mu_0Ia^2/[2(a^2+z^2)^{3/2}]$ ([[2-magnetostatics/13-current-sheets-solenoids-and-the-vector-potential|Lecture 13 §6]]).

> [!trap]
> - $\nabla^2\mathbf{A}$ means the scalar Laplacian of each *Cartesian* component; it does not split that way in cylindrical or spherical components.
> - $\mathbf{A}$ is not unique and not measurable; only $\nabla\times\mathbf{A}$ (and, dynamically, $-\partial\mathbf{A}/\partial t$ together with $-\nabla\Phi$) is. "Find $\mathbf{A}$" always means "in a stated gauge".
> - The notes write $V$, the slides $\Phi$, for the scalar potential; same object.

**Where it appears.** [[2-magnetostatics/13-current-sheets-solenoids-and-the-vector-potential|Lecture 13]] (definition, gauge, Poisson form, the loop), [[2-magnetostatics/15-inductance-magnetic-energy-and-the-potentials|Lecture 15 §6]] (time-varying potentials and gauge transformation), [[3-maxwell-and-waves/16-charge-conservation-displacement-current-and-maxwells-equations|Lecture 16]] ("$\nabla\times\mathbf{H}$ is divergence-free, like $\nabla\times\mathbf{A}$").

Related: [[concepts/electrostatic-potential]] · [[concepts/poissons-equation]] · [[concepts/magnetic-flux]] · [[concepts/curl]].
