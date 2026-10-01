---
title: "Conductors in electrostatics"
description: "Free charge moves until the interior field vanishes: E = 0 inside, the body is an equipotential, all charge sits on the surface with ρs = n̂·D, and the exterior field meets the surface at right angles. Ohm's law J = σE; relaxation time τ = ε/σ."
tags: [concept, electrostatics, exam-1]
aliases: ["perfect electric conductor", "PEC", "Ohm's law", "conductivity", "relaxation time"]
---

> [!key] A conductor in equilibrium
> 1. $\mathbf{E} = 0$ (and $\mathbf{D} = 0$) everywhere inside.
> 2. $V = $ const throughout: the conductor is an **equipotential**.
> 3. $\rho = \nabla\cdot\mathbf{D} = 0$ inside: **all net charge is on the surface**.
> 4. Just outside: $\hat{n}\cdot\mathbf{D} = \rho_s$ and $\hat{n}\times\mathbf{E} = 0$ with $\hat{n}$ pointing out of the metal — the field is **perpendicular to the surface** and its normal $\mathbf{D}$ component *is* the local surface charge.
>
> **Ohm's law** in the material: $\mathbf{J} = \sigma\mathbf{E}$ [A/m²], with conductivity $\sigma$ [S/m]; for a block, $R = l/(\sigma A)$. A **PEC** has $\sigma\to\infty$ and $\mathbf{E}=0$ unconditionally (a short circuit); a perfect dielectric has $\sigma\to0$ and $\mathbf{J}=0$ whatever the field (an open circuit).

**Why.** Free carriers feel $q\mathbf{E}$ and move; they pile up on the surface until their own field cancels the applied one inside, and only then stop. Any interior charge density decays as $e^{-t/\tau}$ with the **relaxation time** $\tau = \epsilon/\sigma$ — from continuity, Ohm's law and Gauss's law — which is $\sim10^{-19}$ s for copper and $\sim0.2$ ns for sea water. Once the interior is charge-free and no external circuit drives a current through the conductor, $\mathbf{J} = 0$ and hence $\mathbf{E} = 0$; so for every field in this course an isolated metal is in equilibrium at all times. (A wire carrying a steady current has $\rho = 0$ inside but $\mathbf{E} = \mathbf{J}/\sigma\neq0$.) (The same $\tau$ is $RC = \epsilon/\sigma$ of a leaky capacitor: [[concepts/conductance]].) The course also takes $\mathbf{H} = \mathbf{B} = 0$ inside a PEC.

**Examples.** Neutral conducting slab between sheets $\rho_A$ (above) and $\rho_B$ (below): the gap field is that of the two sheets alone, $\mathbf{D} = \tfrac12(\rho_B-\rho_A)\hat{z}$, so the faces carry $\rho_1 = \tfrac12(\rho_B-\rho_A)$ (top) and $-\rho_1$ (bottom). Point charge $Q$ above a grounded plane: no field below the plane (shielding), induced charge non-uniform and totalling $-Q$, field lines meeting the plane at right angles. Coax: $+\lambda$ per unit length on the inner conductor forces $-\lambda$ onto the inner surface of the outer conductor so the field inside the metal is zero. Copper plates with salt water between them: the ions short the field to zero.

> [!trap]
> - "Conductors are neutral, so the induced charge is zero" — no: the *net* charge may be zero while the *surface* charge is not, and a grounded or connected conductor need not be neutral at all.
> - Induced charge is not uniform: $\rho_s = \hat{n}\cdot\mathbf{D}$ follows the field.
> - $\sigma$ is conductivity in this course, never surface charge (that is $\rho_s$).
> - A PEC's $\mathbf{E} = 0$ is unconditional; a real conductor's $\mathbf{E} = 0$ is the *steady state* reached after $\tau$ when no current is driven through it.

**Where it appears.** [[1-electrostatics/08-conductors-dielectrics-and-polarization|Lecture 8]], [[1-electrostatics/07-poisson-and-laplace|Lecture 7]] (plates as equipotentials, $\rho_s$ from $\mathbf{D}$), [[1-electrostatics/10-capacitance-and-conductance|Lecture 10]] (every capacitor), [[problems/two-layer-coaxial-capacitor]].

The field that drives a *current* through a resistive wire is itself electrostatic — made by surface charges distributed along the wire ([[1-electrostatics/11-lorentz-drude-models-for-conductivity-and-susceptibility#6-what-drives-the-current-in-a-wire-a-footnote-worth-a-section|Lecture 11 §6]]); the microscopic origin of $\sigma$ is in [[concepts/conductivity-and-susceptibility-models]]. At the surface of a *perfect* conductor the magnetic field is tangential and carried by a surface current, $\hat n\times\mathbf{H} = \mathbf{J}_s$ ([[3-maxwell-and-waves/16-charge-conservation-displacement-current-and-maxwells-equations|Lecture 16]]).

**Practice.** [[practice/topics#conductors-current-and-resistance|Conductors, current and resistance]] (10 problems) — for example [[practice/08-conductors-dielectrics-and-polarization#81-resistance-of-a-copper-wire|8.1 Resistance of a copper wire]] (easy), [[practice/08-conductors-dielectrics-and-polarization#86-a-coaxial-radial-resistor|8.6 A coaxial radial resistor]] (medium), [[practice/08-conductors-dielectrics-and-polarization#89-charge-in-a-conducting-shells-cavity|8.9 Charge in a conducting shell's cavity]] (hard).

Related: [[concepts/boundary-conditions]] · [[concepts/conductance]] · [[concepts/conductivity-and-susceptibility-models]] · [[concepts/polarization]] (the bound-charge contrast).
