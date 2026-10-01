---
title: "Magnetic energy"
description: "An inductor stores W = ½LI²; the energy lives in the field at ½μH·H joules per cubic metre, the twin of ½εE². Together they are the electromagnetic energy density that Poynting's theorem accounts for."
tags: [concept, magnetostatics]
aliases: ["magnetic energy density", "stored energy in an inductor"]
---

> [!key] Definition
> $$
> W = \tfrac12LI^2\quad[\text{J}],\qquad w = \tfrac12\mu\,\mathbf{H}\cdot\mathbf{H} = \tfrac12\mathbf{B}\cdot\mathbf{H} = \frac{B^2}{2\mu}\quad[\text{J/m}^3],\qquad W = \int w\,dV .
> $$

**Physics.** An inductor with a quasi-static current absorbs power $P = VI = LI\,dI/dt = \dfrac{d}{dt}\big(\tfrac12LI^2\big)$, so $\tfrac12LI^2$ is what has been put in. For a long solenoid, $\tfrac12(n^2\mu_0A\ell)I^2 = \dfrac{(\mu_0nI)^2}{2\mu_0}A\ell = \tfrac12\mu_0H^2\cdot(\text{volume of the field})$ — the energy is the field's volume times $\tfrac12\mu_0H^2$, which is taken as the energy density of any magnetostatic field, exactly as $\tfrac12CV^2 = \tfrac12\epsilon E^2\cdot(\text{volume})$ for the parallel plate gave $\tfrac12\epsilon E^2$ ([[concepts/electrostatic-energy]]). In a medium, $\mu = (1+\chi_m)\mu_0$. Because $w\ge0$, $L = 2W/I^2\ge0$ — inductance is never negative. The total electromagnetic energy density $\tfrac12\epsilon E^2 + \tfrac12\mu H^2$ is what a wave carries and what Poynting's theorem (Lecture 20) balances against the power flowing through a surface.

**Examples.** Solenoid, $n = 1000$ m⁻¹, $A = 1$ cm², $\ell = 20$ cm, $I = 2$ A: $L = 25.1\ \mu$H, $W = 50.3\ \mu$J, $w = \tfrac12\mu_0(2000)^2 = 2.51$ J/m³ — the same $50.3\ \mu$J either way. Coax of length $\ell$: $W = \tfrac12LI^2 = \displaystyle\int_a^b\tfrac12\mu\Big(\frac{I}{2\pi r}\Big)^2\,2\pi r\ell\,dr = \frac{\mu\ell I^2}{4\pi}\ln\frac ba$, which reproduces $L = \dfrac{\mu\ell}{2\pi}\ln\dfrac ba$ — a second route to the inductance that avoids choosing a flux surface.

> [!trap]
> - Joules per cubic metre, not watts; power is the rate of change.
> - $\tfrac12\mu H^2$ uses the medium's $\mu$; $B^2/2\mu_0$ is wrong inside a magnetic material.
> - The field energy is the whole story only for linear media and for the external field; the course's coax ignores the energy inside the inner conductor (internal inductance), consistently.

**Where it appears.** [[2-magnetostatics/15-inductance-magnetic-energy-and-the-potentials|Lecture 15 §4]]; the energy-integral route to $L$ in [[problems/coax-inductance-and-the-lc-product]]; Poynting's theorem in Unit 3.

**Practice.** [[practice/topics#magnetic-energy-and-rl-circuits|Magnetic energy and RL circuits]] (8 problems) — for example [[practice/15-inductance-and-magnetic-energy#151-a-long-solenoid-by-the-numbers|15.1 A long solenoid by the numbers]] (easy), [[practice/15-inductance-and-magnetic-energy#156-switching-on-an-rl-circuit|15.6 Switching on an RL circuit]] (medium), [[practice/15-inductance-and-magnetic-energy#159-toroid-with-a-two-layer-core|15.9 Toroid with a two-layer core]] (hard).

Related: [[concepts/inductance]] · [[concepts/electrostatic-energy]] · [[concepts/magnetic-field]].
