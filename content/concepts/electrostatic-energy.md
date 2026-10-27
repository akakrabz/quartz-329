---
title: "Electrostatic energy"
description: "A capacitor stores W = ½CV² = Q²/2C; the energy lives in the field at a density w = ½εE² = ½D·E joules per cubic metre. Potential energy of a charge is qV."
tags: [concept, electrostatics]
aliases: ["stored energy", "energy density", "field energy", "energy of a capacitor"]
---

> [!key] Stored energy
> At charge $q$ the voltage is $q/C$, and moving the next $dq$ across costs $dW = (q/C)\,dq$:
> $$
> W = \int_0^Q\frac{q}{C}\,dq = \frac{Q^2}{2C} = \tfrac12CV^2 = \tfrac12QV\quad[\text{J}].
> $$
> For the parallel plate, $C = \epsilon A/d$ and $V = Ed$ give $W = \tfrac12\epsilon E^2\,(Ad)$: gap volume times
> $$
> w = \tfrac12\epsilon E^2 = \tfrac12\mathbf{D}\cdot\mathbf{E}\quad[\text{J/m}^3],
> $$
> taken in general as the **energy density of the electrostatic field**: energy lives wherever the field is, $W = \int w\,dV$ over all space. (J/m³, not the W/m³ a slide writes — that is a power density.) The potential energy of a point charge $q$ at potential $V$ is $U = qV$.

**Physics.** Energy is stored in the field, wherever the field is — a coax stores $W' = \tfrac12\mathcal{C}V^2$ per metre in its dielectric, most of it near the inner conductor where $E$ is largest. From power: $P = VI = V\,C\,dV/dt = \dfrac{d}{dt}\big(\tfrac12CV^2\big)$, so the same $W$ is $\int_0^t VI\,dt$. A battery at fixed $V$ delivers $QV = CV^2$ while charging the capacitor to $Q$; only half is stored — the other half is dissipated in the charging resistance, however small.

**Examples.** Capacitor $C$ at $V$: $\tfrac12CV^2$. Two-layer coax with $\pm\lambda$: $W' = \lambda^2/2\mathcal{C}$. Field between plates $E = 3$ V/m in vacuum: $w = \tfrac12\epsilon_0(9)\approx4\times10^{-11}$ J/m³.

> [!trap]
> - Joules per cubic metre, not watts (a slide slips here). $W$ is energy; $P = dW/dt$ is power.
> - With a dielectric, $\epsilon$ replaces $\epsilon_0$ in $w$; $\tfrac12\mathbf{D}\cdot\mathbf{E}$ is the form that needs no thought.
> - $\tfrac12QV$ uses the total charge and the *final* voltage; it is half of $QV$ because the voltage grew from zero during charging.

> [!exam] On exams
> Energy questions reduce to $C$: find $C$ by the chain of [[concepts/capacitance|Capacitance]], then $W = \tfrac12CV^2$ or $Q^2/2C$ — which one depends on whether $V$ or $Q$ is held fixed when something changes (plates pulled apart, dielectric inserted). For a field given directly, integrate $\tfrac12\epsilon E^2$ over the region.

**Where it appears.** [[1-electrostatics/10-capacitance-and-conductance#5-energy-stored-in-a-capacitor-and-in-the-field|Lecture 10 §5]], [[1-electrostatics/05-curl-free-fields-and-the-electrostatic-potential|Lecture 5]] ($U = qV$, the electron-volt); [[2-magnetostatics/15-inductance-magnetic-energy-and-the-potentials|Lecture 15]] (the magnetic twin, $\tfrac12LI^2$ and $\tfrac12\mu H^2$ — [[concepts/magnetic-energy|Magnetic energy]]); Unit 3 (Poynting's theorem adds the flow of energy). In a wave, $\tfrac12\epsilon E^2$ is half of the stored energy in [[concepts/poynting-theorem|Poynting's theorem]] ([[3-maxwell-and-waves/20-poynting-theorem-and-monochromatic-waves|Lecture 20]]).

**Related.** [[concepts/capacitance|Capacitance]] · [[concepts/electrostatic-potential|Electrostatic potential V]] · [[concepts/magnetic-energy|Magnetic energy]] · [[concepts/poynting-theorem|Poynting's theorem]].

**Practice.** [[practice/topics#capacitance-stored-energy-and-force|Capacitance, stored energy and force]] (9 problems) — for example [[practice/10-capacitance-and-conductance#101-four-capacitances-by-formula|10.1 Four capacitances by formula]] (easy), [[practice/10-capacitance-and-conductance#106-two-layers-between-charged-plates|10.6 Two layers between charged plates]] (medium), [[practice/10-capacitance-and-conductance#1010-pulling-capacitor-plates-apart|10.10 Pulling capacitor plates apart]] (hard).
