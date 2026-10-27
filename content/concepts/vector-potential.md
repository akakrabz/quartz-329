---
title: "Vector potential"
description: "Because ∇·B = 0, B = ∇×A for some vector field A (Wb/m). A is fixed only up to a gradient; the Coulomb gauge ∇·A = 0 turns Ampère's law into ∇²A = −μ₀J, Poisson's equation with a vector source, solved by the Coulomb integral. With time variation, E = −∇Φ − ∂A/∂t, and (Φ, A) are defined up to a gauge transformation."
tags: [concept, magnetostatics]
aliases: ["magnetic vector potential", "Coulomb gauge", "gauge transformation", "gauge freedom", "potentials", "scalar and vector potentials"]
---

> [!key] Vector potential and the Coulomb gauge
> $$
> \mathbf{B} = \nabla\times\mathbf{A}\quad[\mathbf{A}\ \text{in Wb/m} = \text{T·m}].
> $$
> $\mathbf{A}$ is not unique: $\mathbf{A}+\nabla\lambda$, any scalar $\lambda$, has the same curl ($\nabla\times\nabla\lambda = 0$). In electrostatics the freedom was a constant in $V$, spent by "grounding" a point; here it is a gradient, spent by prescribing $\nabla\cdot\mathbf{A}$. The magnetostatic choice is $\nabla\cdot\mathbf{A} = 0$, the **Coulomb gauge**, in which Ampère's law becomes Poisson's equation for $\mathbf{A}$, solved by the Coulomb integral:
> $$
> \nabla^2\mathbf{A} = -\mu_0\mathbf{J}\qquad\Longrightarrow\qquad \mathbf{A}(\mathbf{r}) = \int\frac{\mu_0\mathbf{J}(\mathbf{r}')}{4\pi\lvert\mathbf{r}-\mathbf{r}'\rvert}\,d^3r' .
> $$
> Compare $\nabla^2V = -\rho/\epsilon_0$ and $V(\mathbf{r}) = \displaystyle\int\frac{\rho(\mathbf{r}')}{4\pi\epsilon_0\lvert\mathbf{r}-\mathbf{r}'\rvert}d^3r'$ ([[concepts/poissons-equation|Poisson's and Laplace's equations]]): the same Green's function $1/(4\pi\lvert\mathbf{r}-\mathbf{r}'\rvert)$, applied to each Cartesian component of $\mathbf{J}$. (The vector Laplacian is the scalar Laplacian of each Cartesian component; cylindrical or spherical components do not split so simply.)

**Physics.** A curl-free field is the gradient of a scalar — $V$ in [[1-electrostatics/05-curl-free-fields-and-the-electrostatic-potential|Lecture 5]]. A divergence-free field is the curl of a vector: $\mathbf{B} = \nabla\times\mathbf{A}$ is divergence-free for every $\mathbf{A}$, since $\nabla\cdot(\nabla\times\mathbf{A}) = 0$ (a determinant with two identical rows of $\partial$'s, or expand: $\partial_x(\partial_yA_z-\partial_zA_y) + \partial_y(\partial_zA_x-\partial_xA_z) + \partial_z(\partial_xA_y-\partial_yA_x)$ cancels pairwise). Conversely every divergence-free field can be written this way. In the Coulomb gauge $\nabla\times\nabla\times\mathbf{A} = \nabla(\nabla\cdot\mathbf{A}) - \nabla^2\mathbf{A}$ loses its first term, and $\nabla\times\mathbf{B} = \mu_0\mathbf{J}$ becomes the Poisson equation above — so $\mathbf{A}$ is "$V$ with $\rho/\epsilon_0\to\mu_0\mathbf{J}$". The integral satisfies $\nabla\cdot\mathbf{A} = 0$ automatically **provided $\nabla\cdot\mathbf{J} = 0$** — true for steady currents (the [[concepts/continuity-equation|Continuity equation (charge conservation)]] with $\partial\rho/\partial t = 0$). For any static (or quasi-static, $L\ll c/f$) current: integrate for $\mathbf{A}$, take the curl for $\mathbf{B}$. A footnote in the notes reads $\mathbf{A}$ in this gauge as potential *momentum* per unit charge, as $V$ is potential energy per unit charge. The flux through a loop is the circulation of $\mathbf{A}$: $\Psi = \int_S\mathbf{B}\cdot d\mathbf{S} = \oint_C\mathbf{A}\cdot d\mathbf{l}$ by Stokes ([[concepts/magnetic-flux|Magnetic flux Ψ]]).

| | scalar potential $V$ | vector potential $\mathbf{A}$ |
|---|---|---|
| exists because | $\nabla\times\mathbf{E} = 0$ | $\nabla\cdot\mathbf{B} = 0$ |
| field from potential | $\mathbf{E} = -\nabla V$ | $\mathbf{B} = \nabla\times\mathbf{A}$ |
| freedom | $V\to V + \text{const}$ | $\mathbf{A}\to\mathbf{A}+\nabla\lambda$ |
| how it is spent | $V = 0$ at a chosen point | $\nabla\cdot\mathbf{A} = 0$ (Coulomb gauge) |
| equation | $\nabla^2V = -\rho/\epsilon_0$ | $\nabla^2\mathbf{A} = -\mu_0\mathbf{J}$ |
| meaning | energy per unit charge | momentum per unit charge |

**The potentials when fields vary in time** ([[2-magnetostatics/15-inductance-magnetic-energy-and-the-potentials#6-the-potentials-when-fields-vary-in-time|Lecture 15 §6]]). In statics $\mathbf{E} = -\nabla V$ because $\nabla\times\mathbf{E} = 0$; Faraday gives $\mathbf{E}$ a curl, so no scalar potential alone suffices. $\nabla\cdot\mathbf{B} = 0$ still holds, so $\mathbf{B} = \nabla\times\mathbf{A}$, and Faraday's law becomes

$$
\nabla\times\mathbf{E} = -\frac{\partial}{\partial t}\nabla\times\mathbf{A}\quad\Rightarrow\quad\nabla\times\Big(\mathbf{E}+\frac{\partial\mathbf{A}}{\partial t}\Big) = 0 .
$$

The bracket is curl-free, hence a gradient — **the fields from the potentials, in general**:

$$
\mathbf{B} = \nabla\times\mathbf{A},\qquad \mathbf{E} = -\nabla\Phi - \frac{\partial\mathbf{A}}{\partial t}.
$$

(The slides' $\Phi$ is the notes' $V$.) Four potential components replace six field components, and the two homogeneous Maxwell equations ($\nabla\cdot\mathbf{B} = 0$, Faraday) hold identically. $-\partial\mathbf{A}/\partial t$ is the induced, circulating part of $\mathbf{E}$ — the part a voltmeter path integral cannot ignore ([[concepts/electromotive-force|Electromotive force (emf) and path-dependent voltage]]). In the static limit $\mathbf{E} = -\nabla\Phi$, and Gauss's law gives back Poisson's equation.

**Gauge freedom.** For any scalar $\lambda(\mathbf{r},t)$,

$$
\mathbf{A}' = \mathbf{A} + \nabla\lambda,\qquad \Phi' = \Phi - \frac{\partial\lambda}{\partial t}
$$

give the same $\mathbf{B}$ ($\nabla\times\nabla\lambda = 0$) and the same $\mathbf{E}$ ($-\nabla\partial_t\lambda$ from $\Phi'$ cancels $-\partial_t\nabla\lambda$ from $\mathbf{A}'$) — the slides pose this as a challenge: *both* fields are unchanged. The Coulomb gauge $\nabla\cdot\mathbf{A} = 0$ is one way to spend the freedom; the wave-friendly Lorenz gauge appears with radiation.

**Example.** The circular loop of radius $a$: $\mathbf{J} = I\delta(z')\delta(r'-a)\hat\phi'$ reduces the $\mathbf{A}$ integral to a single $\phi'$ integral with $A_z = 0$; curling it gives $B_x$, $B_z$ on the plane $y = 0$ as elliptic-type integrals, and on the axis the closed form $B_z = \mu_0Ia^2/[2(a^2+z^2)^{3/2}]$ — worked in full on [[concepts/magnetic-dipole|The current loop and the magnetic dipole]].

> [!trap]
> - $\nabla^2\mathbf{A}$ means the scalar Laplacian of each *Cartesian* component; it does not split that way in cylindrical or spherical components.
> - $\mathbf{A}$ is not unique and not measurable; only $\nabla\times\mathbf{A}$ (and, dynamically, $-\partial\mathbf{A}/\partial t$ together with $-\nabla\Phi$) is. "Find $\mathbf{A}$" always means "in a stated gauge".
> - The Coulomb-gauge integral is valid only for $\nabla\cdot\mathbf{J} = 0$; a current that piles up charge needs the time-dependent potentials.
> - The notes write $V$, the slides $\Phi$, for the scalar potential; same object.

> [!exam] On exams
> Examined lightly: $\mathbf{B} = \nabla\times\mathbf{A}$ and why ($\nabla\cdot\nabla\times\mathbf{A} = 0$); why the gauge freedom exists and what the Coulomb gauge fixes; $\nabla^2\mathbf{A} = -\mu_0\mathbf{J}$ as Poisson's twin; $\mathbf{E} = -\nabla\Phi - \partial\mathbf{A}/\partial t$ and the gauge transformation as a true/false item. The loop integrals are not for exams; the on-axis result might be.

**Where it appears.** [[2-magnetostatics/13-current-sheets-solenoids-and-the-vector-potential#5-the-vector-potential|Lecture 13 §5]] (definition, gauge, Poisson form), [[2-magnetostatics/13-current-sheets-solenoids-and-the-vector-potential#6-the-current-loop-and-the-magnetic-dipole|§6]] (the loop), [[2-magnetostatics/15-inductance-magnetic-energy-and-the-potentials#6-the-potentials-when-fields-vary-in-time|Lecture 15 §6]] (time-varying potentials and gauge transformation), [[3-maxwell-and-waves/16-charge-conservation-displacement-current-and-maxwells-equations|Lecture 16]] ("$\nabla\times\mathbf{H}$ is divergence-free, like $\nabla\times\mathbf{A}$").

**Related.** [[concepts/electrostatic-potential|Electrostatic potential V]] · [[concepts/poissons-equation|Poisson's and Laplace's equations]] · [[concepts/magnetic-flux|Magnetic flux Ψ]] · [[concepts/curl|Curl]] · [[concepts/magnetic-dipole|The current loop and the magnetic dipole]] · [[concepts/faradays-law|Faraday's law]].

**Practice.** [[practice/topics#vector-potential-potentials-and-gauge|Vector potential, potentials and gauge]] (6 problems) — for example [[practice/13-current-sheets-solenoids-and-vector-potential#135-five-true-or-false-statements|13.5 Five true or false statements]] (easy), [[practice/13-current-sheets-solenoids-and-vector-potential#139-two-opposite-slabs-and-a-sheet|13.9 Two opposite slabs and a sheet]] (hard).
