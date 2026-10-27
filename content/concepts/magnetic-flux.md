---
title: "Magnetic flux Ψ"
description: "Ψ = ∫B·dS through a surface, in webers. Through a closed surface it is always zero (Gauss's law for magnetism: no magnetic charge); through any surface spanning a given loop it is the same number — the flux linking the loop — which is what Faraday's law differentiates and what inductance is the ratio of."
tags: [concept, magnetostatics]
aliases: ["flux linkage", "weber", "linked flux", "Gauss's law for magnetism", "no magnetic charge", "magnetic monopole"]
---

> [!key] Definition, and Gauss's law for magnetism
> $$
> \Psi = \int_S\mathbf{B}\cdot d\mathbf{S}\quad[\text{Wb} = \text{T·m}^2 = \text{V·s}],\qquad\qquad \psi_B = \oint_S \mathbf{B}\cdot d\mathbf{S} = 0 \quad\text{for every closed surface } S.
> $$
> For an open surface $S$ bounded by a directed loop $C$, $d\mathbf{S}$ follows the right-hand rule from $C$, and $\Psi$ is called the flux **linking** $C$: field lines thread the loop like links of a chain. For an $N$-turn coil whose turns each link $\Psi$, the flux *linkage* is $N\Psi$. The closed-surface flux is zero — **no magnetic charge** — so every surface spanning the same $C$ gives the same $\Psi$: the flat disk and the bowl agree. An *open* surface can have nonzero magnetic flux ([[concepts/faradays-law|Faraday's law]]); a *closed* one never does. Shrinking the surface to a point gives $\nabla\cdot\mathbf{B} = 0$ ([[concepts/divergence|Divergence]]): no magnetic sources or sinks anywhere, in statics or dynamics.

**Physics.** Magnetic field lines have no ends: they close or run on forever. The slides' "Yadaraf bugs" (Faraday backwards) always return to their hole, so any *closed* net catches as many leaving as returning — the second Maxwell equation, stated in [[1-electrostatics/03-gauss-law-at-work#6-the-magnetic-counterpart--bds--0|Lecture 3 §6]] long before any magnetic field is computed. $\Psi$ is to $\mathbf{B}$ what $\psi_E = \int\mathbf{D}\cdot d\mathbf{S}$ is to $\mathbf{D}$ ([[concepts/flux|Flux]]), with that one difference: no closed surface ever has net magnetic flux. Two consequences follow. The flux through a loop is well defined without naming the surface — two surfaces spanning $C$ together form a closed surface with zero net flux, so they agree ([[2-magnetostatics/14-faradays-law-and-induced-emf#1-the-law-and-the-flux-it-is-about|Lecture 14 §1]]). And $\mathbf{B}$ is the curl of a [[concepts/vector-potential|Vector potential]], so $\Psi = \oint_C\mathbf{A}\cdot d\mathbf{l}$ by Stokes. The "weber" in T = Wb/m² is this flux; the "volt-second" in Wb = V·s is Faraday's law: a flux changing at 1 Wb/s drives an emf of 1 V around the loop. Two roles in the course: [[concepts/faradays-law|Faraday's law]] differentiates it, $\mathcal{E} = -d\Psi/dt$, and [[concepts/inductance|Inductance]] divides it by the current that made it, $L = N\Psi/I$.

**Examples.** Uniform $B_0\hat z$ through a circle of radius $r$ in the plane $z = 0$: $\Psi = \pi r^2B_0$ (10 m radius, $B_0 = 1$ T: 314 Wb). A 2 m square above a line current $I$ along $x$, between $y = 2t-1$ and $2t+1$: $\Psi = \dfrac{\mu_0I}{\pi}\ln\dfrac{2t+1}{2t-1}$ ([[concepts/faradays-law|Lecture 14, Example 2]]). A shorted coax of length $\ell$: $\Psi = \dfrac{\mu\ell I}{2\pi}\ln\dfrac ba$ through the $r$–$z$ rectangle between the conductors ([[concepts/transmission-line-parameters|Transmission-line parameters 𝓛, 𝓒, 𝓖]]). A solenoid turn: $\Psi = \mu_0nIA$ ([[concepts/solenoids-and-toroids|Solenoids and toroids]]). A closed box anywhere in any of these fields: zero.

> [!trap]
> - Choose the surface that makes the integral easy — any surface on $C$ will do — but orient it by the right-hand rule from the direction you chose for $C$, or the sign of the emf comes out wrong.
> - For a coax the flux-linking surface is the rectangle between the conductors (normal $\hat\phi$, along $\mathbf{B}$), not a circle.
> - $\Psi$ of an $N$-turn coil: count the field once (it is produced by all $N$ turns, $B\propto nI$) and the linkage once more ($N\Psi$); both factors of $N$ are real, which is why $L\propto N^2$.
> - Units: Wb, never T. "$\oint\mathbf{B}\cdot d\mathbf{S} = 0$" is for *closed* surfaces; an open loop's flux is generally nonzero.

> [!exam] On exams
> Compute $\Psi$ with a stated $C$ and $d\mathbf{S}$ before differentiating; for a tilted loop, $\mathbf{B}\cdot\hat n$ times the area. "Is $\oint\mathbf{B}\cdot d\mathbf{S}$ zero for this closed surface?" — always, whatever the field; say why (no magnetic charge, $\nabla\cdot\mathbf{B} = 0$).

**Where it appears.** [[1-electrostatics/03-gauss-law-at-work#6-the-magnetic-counterpart--bds--0|Lecture 3 §6]] (closed-surface flux is zero), [[2-magnetostatics/12-magnetic-force-biot-savart-and-amperes-law#4-ampères-law-the-circulation-of-b|Lecture 12 §4]] ($\nabla\cdot\mathbf{B} = 0$ beside $\nabla\times\mathbf{H} = \mathbf{J}$), [[2-magnetostatics/14-faradays-law-and-induced-emf#1-the-law-and-the-flux-it-is-about|Lecture 14 §1]] (linked flux, flux rule), [[2-magnetostatics/15-inductance-magnetic-energy-and-the-potentials|Lecture 15]] (inductance, flux of the coax and solenoid), [[problems/emf-of-a-loop-moving-near-a-line-current|Worked problem — EMF of a loop moving away from a line current]], [[problems/coax-inductance-and-the-lc-product|Worked problem — Inductance of a coax, and the 𝓛𝓒 product]].

**Related.** [[concepts/flux|Flux]] · [[concepts/faradays-law|Faraday's law]] · [[concepts/inductance|Inductance]] · [[concepts/vector-potential|Vector potential]] · [[concepts/divergence|Divergence]] · [[concepts/magnetic-field|Magnetic field: B and H]].

**Practice.** [[practice/topics#magnetic-flux-faradays-law-and-lenz|Magnetic flux, Faraday's law and Lenz]] (11 problems) — for example [[practice/14-faradays-law-and-induced-emf#141-flux-through-a-tilted-loop|14.1 Flux through a tilted loop]] (easy), [[practice/04-divergence-and-curl#48-circulation-from-a-given-curl|4.8 Circulation from a given curl]] (medium), [[practice/14-faradays-law-and-induced-emf#149-loop-crossing-a-field-strip|14.9 Loop crossing a field strip]] (hard).
