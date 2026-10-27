---
title: "Magnetic energy"
description: "An inductor stores W = ½LI²; the energy lives in the field at ½μH·H joules per cubic metre, the twin of ½εE². Derived from P = VI for a quasi-static inductor and the long solenoid; together with ½εE² it is the electromagnetic energy density that Poynting's theorem accounts for."
tags: [concept, magnetostatics]
aliases: ["magnetic energy density", "stored energy in an inductor", "energy in a magnetic field"]
---

> [!key] Stored magnetic energy and its density
> $$
> W = \tfrac12LI^2\quad[\text{J}],\qquad w = \tfrac12\mu\,\mathbf{H}\cdot\mathbf{H} = \tfrac12\mathbf{B}\cdot\mathbf{H} = \frac{B^2}{2\mu}\quad[\text{J/m}^3],\qquad W = \int w\,dV .
> $$
> In free space $w = \tfrac12\mu_0\,\mathbf{H}\cdot\mathbf{H} = \tfrac12\mathbf{B}\cdot\mathbf{H}$; in a medium $\mu_0\to\mu = (1+\chi_m)\mu_0$ in $L$, $W$ and $w$, as $\epsilon = (1+\chi_e)\epsilon_0$ ([[concepts/permeability|Permeability, susceptibility, and B = μH]]).

**Physics.** With a quasi-static current (size $\ll\lambda = c/f$, as for capacitors) the terminal voltage is $V = L\,dI/dt$ ([[concepts/inductance|Inductance]]) and the inductor absorbs

$$
P = VI = LI\frac{dI}{dt} = \frac{d}{dt}\Big(\tfrac12LI^2\Big),
$$

so $\tfrac12LI^2$ is what has been put in. For the long solenoid ([[concepts/solenoids-and-toroids|Solenoids and toroids]]),

$$
W = \tfrac12LI^2 = \tfrac12(n^2\mu_0A\ell)I^2 = \frac{(\mu_0nI)^2}{2\mu_0}A\ell = \frac{B_z^2}{2\mu_0}A\ell = \tfrac12\mu_0H_z^2\cdot A\ell
$$

— field volume times

$$
w = \tfrac12\mu_0\,\mathbf{H}\cdot\mathbf{H} = \tfrac12\mathbf{B}\cdot\mathbf{H}\quad[\text{J/m}^3],
$$

taken, like $\tfrac12\epsilon E^2$, as the **energy density of the magnetic field** in general, exactly as $\tfrac12CV^2 = \tfrac12\epsilon E^2\cdot(\text{volume})$ for the parallel plate gave $\tfrac12\epsilon E^2$ ([[concepts/electrostatic-energy|Electrostatic energy]]). Since $W = \int w\,dV\ge0$, $L = 2W/I^2\ge0$ — not an assumption: inductance is never negative. The total electromagnetic energy density $\tfrac12\epsilon E^2 + \tfrac12\mu H^2$ is what a wave carries and what [[concepts/poynting-theorem|Poynting's theorem]] ([[3-maxwell-and-waves/20-poynting-theorem-and-monochromatic-waves|Lecture 20]]) balances against the power flowing through a surface. [[3-maxwell-and-waves/17-magnetization-and-maxwells-equations-in-matter|Lecture 17]] explains $\chi_m$.

**Examples** (site's own). Solenoid, $n = 1000$ m⁻¹, $A = 1$ cm², $\ell = 20$ cm, $I = 2$ A: $L = 25.1\ \mu$H, $W = 50.3\ \mu$J, $w = \tfrac12\mu_0(2000)^2 = 2.51$ J/m³ — the same $50.3\ \mu$J either way. Coax of length $\ell$: $W = \tfrac12LI^2 = \displaystyle\int_a^b\tfrac12\mu\Big(\frac{I}{2\pi r}\Big)^2\,2\pi r\ell\,dr = \frac{\mu\ell I^2}{4\pi}\ln\frac ba$, which reproduces $L = \dfrac{\mu\ell}{2\pi}\ln\dfrac ba$ — a second route to the inductance that avoids choosing a flux surface ([[concepts/transmission-line-parameters|Transmission-line parameters 𝓛, 𝓒, 𝓖]]). The shorted coil of [[concepts/inductance|Inductance]] (1 μH, 3 A) dissipates its $\tfrac12LI^2 = 4.5\ \mu$J in the resistor within a few microseconds.

> [!trap]
> - Joules per cubic metre, not watts; power is the rate of change.
> - $\tfrac12\mu H^2$ uses the medium's $\mu$; $B^2/2\mu_0$ is wrong inside a magnetic material.
> - The field energy is the whole story only for linear media and for the external field; the course's coax ignores the energy inside the inner conductor (internal inductance), consistently.
> - $W = \tfrac12LI^2$ needs the quasi-static (lumped) inductor; for a long line the energy is distributed, $\tfrac12\mathcal{L}I^2$ per metre.

> [!exam] On exams
> Energy questions want $\tfrac12LI^2$ or $\int\tfrac12\mu H^2dV$, shown to agree — the agreement is the check on $L$. Use the energy integral as the route to $L$ when the flux surface is awkward (coax, two-layer core). Give J and J/m³ with the medium's $\mu$.

**Where it appears.** [[2-magnetostatics/15-inductance-magnetic-energy-and-the-potentials#4-energy-½li²-and-½μh²-per-cubic-metre|Lecture 15 §4]]; the energy-integral route to $L$ in [[problems/coax-inductance-and-the-lc-product|Worked problem — Inductance of a coax, and the 𝓛𝓒 product]]; [[concepts/poynting-theorem|Poynting's theorem]] ([[3-maxwell-and-waves/20-poynting-theorem-and-monochromatic-waves|Lecture 20]]), where $\tfrac12\mu H^2$ is one of the two stored-energy terms.

**Related.** [[concepts/inductance|Inductance]] · [[concepts/electrostatic-energy|Electrostatic energy]] · [[concepts/magnetic-field|Magnetic field: B and H]] · [[concepts/permeability|Permeability, susceptibility, and B = μH]] · [[concepts/poynting-theorem|Poynting's theorem]].

**Practice.** [[practice/topics#magnetic-energy-and-rl-circuits|Magnetic energy and RL circuits]] (9 problems) — for example [[practice/15-inductance-and-magnetic-energy#151-a-long-solenoid-by-the-numbers|15.1 A long solenoid by the numbers]] (easy), [[practice/15-inductance-and-magnetic-energy#156-switching-on-an-rl-circuit|15.6 Switching on an RL circuit]] (medium), [[practice/15-inductance-and-magnetic-energy#159-toroid-with-a-two-layer-core|15.9 Toroid with a two-layer core]] (hard).
