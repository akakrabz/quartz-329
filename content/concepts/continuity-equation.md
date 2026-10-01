---
title: "Continuity equation (charge conservation)"
description: "∇·J = −∂ρ/∂t, or ∮J·dS = −dQ/dt: the net current out of a closed surface is the rate at which the enclosed charge decreases. It is charge conservation written as a field equation, it is built into Maxwell's equations, and it is what forces the displacement current."
tags: [concept, waves]
aliases: ["charge conservation", "conservation of charge", "continuity"]
---

> [!key] Definition
> $$
> \oint_S\mathbf{J}\cdot d\mathbf{S} = -\frac{dQ_{\text{enc}}}{dt} = -\frac{d}{dt}\int_V\rho\,dV\qquad\Longleftrightarrow\qquad \nabla\cdot\mathbf{J} = -\frac{\partial\rho}{\partial t},
> $$
> with $d\mathbf{S}$ outward. Net current **out** equals the rate of **decrease** of the charge inside; where current lines diverge, charge is being depleted. The point form follows by the divergence theorem and "true for every volume".

**Physics.** Charge is created and destroyed only in $\pm$ pairs (ionization, recombination, pair creation), so the charge in a region changes only by transport across its boundary — the bucket picture of [[3-maxwell-and-waves/16-charge-conservation-displacement-current-and-maxwells-equations|Lecture 16]]. The equation is not independent of Maxwell's equations: the divergence of $\nabla\times\mathbf{H} = \mathbf{J}+\partial\mathbf{D}/\partial t$ is $0 = \nabla\cdot\mathbf{J}+\partial_t\nabla\cdot\mathbf{D} = \nabla\cdot\mathbf{J}+\partial\rho/\partial t$ by Gauss's law. Run backwards, that is Maxwell's argument: the static law $\nabla\times\mathbf{H} = \mathbf{J}$ would require $\nabla\cdot\mathbf{J} = 0$ always, contradicting conservation wherever charge accumulates, so a term whose divergence is $\partial\rho/\partial t$ *must* be added — the [[concepts/displacement-current]]. Steady currents are the special case $\nabla\cdot\mathbf{J} = 0$: current lines close on themselves, the same current flows through every cross-section of a wire, and the Coulomb-gauge [[concepts/vector-potential]] is consistent.

**Examples.** $\mathbf{J} = (x,y,z)$ A/m² in the unit cube: $\nabla\cdot\mathbf{J} = 3$, so the charge inside *decreases* at 3 A (and 1 A leaves through each pair of faces). A conductor with $\mathbf{J} = \sigma\mathbf{E}$ and $\nabla\cdot\mathbf{D} = \rho$: $\partial_t\rho = -\nabla\cdot(\sigma\mathbf{E}) = -(\sigma/\epsilon)\rho$, so interior charge decays as $e^{-t/\tau}$ with $\tau = \epsilon/\sigma$ — the relaxation time of [[1-electrostatics/08-conductors-dielectrics-and-polarization|Lecture 8]]. The coax conductance of [[1-electrostatics/10-capacitance-and-conductance|Lecture 10]]: the leakage current through every coaxial cylinder is the same, $J_r\cdot2\pi rL$ with $J_r\propto1/r$, because $\nabla\cdot\mathbf{J} = 0$ in the steady state. A capacitor plate: $I_{\text{in}} - GV = dQ/dt = C\,dV/dt$.

> [!trap]
> - The sign: outward flux is a *decrease*. Problems that underline "rate of decrease" want $+\oint\mathbf{J}\cdot d\mathbf{S}$.
> - Partial derivative in the point form; the total $dQ/dt$ is fine for a fixed volume.
> - $\nabla\cdot\mathbf{J} = 0$ is a *statics* statement, not a law.

**Where it appears.** Lecture 16 (derived and used), Lecture 8 (relaxation), [[2-magnetostatics/13-current-sheets-solenoids-and-the-vector-potential|Lecture 13]] (Coulomb gauge consistency), [[concepts/maxwells-equations]] ("built in: charge conservation"), [[problems/mmf-around-a-draining-charge]].

Related: [[concepts/divergence]] · [[concepts/divergence-theorem]] · [[concepts/displacement-current]] · [[concepts/charge-density]].
