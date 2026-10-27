---
title: "Charge densities and δ-functions"
description: "ρ, ρ_s, ρ_l and point charges; how to write all of them as a volume density with impulses; and the unit checks that go with each."
tags: [concept, electrostatics, exam-1]
aliases: ["charge density", "delta function charge", "impulse", "Dirac delta", "surface charge density", "line charge density"]
---

> [!key] The four kinds of charge, one formula for the total
> | distribution | density | total charge |
> |---|---|---|
> | point | $Q$ [C] | $Q$ |
> | line | $\rho_l$ [C/m] (also written $\lambda$) | $\int_L\rho_l\,dl$ |
> | surface | $\rho_s$ [C/m²] | $\int_S\rho_s\,dS$ |
> | volume | $\rho$ [C/m³] | $\int_V\rho\,dV$ |
>
> Each is "charge per unit of the thing it lives on"; the differential element $dQ$ is density × element. Charges source $\mathbf{E}$ and $\mathbf{D}$; currents ($I$ [A], $\mathbf{J}_s$ [A/m], $\mathbf{J}$ [A/m²]) source $\mathbf{H}$ and $\mathbf{B}$ ([[concepts/current-distributions|Current distributions: J, J_s, I]]). The densities' "dimension ladder" checks an answer's units ([[0-toolkit/03-units-and-constants|Units, constants, and the dimension ladder]]).

**Physics.** Gauss's law uses a volume density $\rho$, but charge often lives on points, lines, sheets. The unifying device is the **impulse** (Dirac δ) from ECE 210:

$$
\int_{-\infty}^{\infty}\delta(x)\,dx = 1,\qquad \delta(x-x_0) = 0\ \text{for } x\ne x_0,\qquad [\delta(x)] = \tfrac{1}{\text{m}} .
$$

| charge | volume density $\rho(x,y,z)$ |
|---|---|
| point $Q$ at $(x_0,y_0,z_0)$ | $Q\,\delta(x-x_0)\,\delta(y-y_0)\,\delta(z-z_0)$ |
| line $\rho_l$ along $z$ through $(x_0,y_0)$ | $\rho_l\,\delta(x-x_0)\,\delta(y-y_0)$ |
| sheet $\rho_s(y,z)$ on $x=x_0$ | $\rho_s(y,z)\,\delta(x-x_0)$ |

Units each time: $[\text{C}]\cdot[1/\text{m}]^3 = \text{C/m}^3$ ✓. Integrating $\rho$ over a volume recovers the total charge, so $Q_{\text{enc}} = \int_V\rho\,dV$ covers points, lines, sheets and volumes at once — as does the differential Gauss's law $\nabla\cdot\mathbf{D}=\rho$ ([[concepts/divergence|Divergence]]). A row of point charges $Q$ at $z = n\Delta z$ is $\rho = Q\sum_n\delta(x)\delta(y)\delta(z-n\Delta z)$; on scales coarser than $\Delta z$ it acts like a line charge $\rho_l = Q/\Delta z$ — this is how the course notes motivate the macroscopic line charge.

**Converting between kinds.** A slab of volume density $\rho(x)$ seen from far away is a sheet with $\rho_s = \int\rho(x)\,dx$ (FA26 Exam 1, problem 2a); a thin cylinder of $\rho$ is a line with $\rho_l = \rho\cdot\pi a^2$. Conversely, a "surface charge" is really a thin layer of large $\rho$ — which is why fields *jump* there ([[concepts/boundary-conditions|Boundary conditions at an interface]]).

> [!trap] Signs and absolute values
> - A density such as $\rho(x) = \rho_0\lvert x\rvert/a$ is *even*: its total is $2\int_0^a$, not zero. Dropping the absolute value (which makes the integral vanish) or the factor 2 is the classic error on slab problems like the [[problems/charged-slab-with-a-power-law-profile|worked one]].
> - A sheet written $\rho = \rho_s\,\delta(y)$ (HW3 #6) is a surface charge $\rho_s$ on $y=0$: read off the jump of $D_y$, do not try to differentiate across it.

> [!exam] On exams
> Units on every density and every answer; $Q_{\text{enc}}$ as the integral of $\rho$ over the Gaussian volume (FA26 problem 2); recognizing $\rho_s\,\delta(y)$ as a sheet.

**Where it appears.** [[1-electrostatics/01-fields-forces-and-the-maxwell-roadmap#3-units-and-the-source--field-bookkeeping|Lecture 1 §3]] (units), [[1-electrostatics/03-gauss-law-at-work#5-charge-densities-and-δ-functions|Lecture 3 §5]] (δ formalism), [[1-electrostatics/08-conductors-dielectrics-and-polarization|Lecture 8]] (bound charge $\rho_b = -\nabla\cdot\mathbf{P}$, surface charge on conductors $\rho_s = \hat{n}\cdot\mathbf{D}$).

**Related.** [[concepts/gauss-law|Gauss's law]] · [[concepts/five-step-recipe|The 5-step recipe for fields of charge distributions]] · [[concepts/symmetric-charge-distributions|Symmetric charge distributions]] · [[concepts/current-distributions|Current distributions: J, J_s, I]] · [[concepts/boundary-conditions|Boundary conditions at an interface]] · [[0-toolkit/03-units-and-constants|Units, constants, and the dimension ladder]].
