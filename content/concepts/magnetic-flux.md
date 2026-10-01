---
title: "Magnetic flux Ψ"
description: "Ψ = ∫B·dS through a surface, in webers. Through a closed surface it is always zero; through any surface spanning a given loop it is the same number — the flux linking the loop — which is what Faraday's law differentiates and what inductance is the ratio of."
tags: [concept, magnetostatics]
aliases: ["flux linkage", "weber", "linked flux"]
---

> [!key] Definition
> $$
> \Psi = \int_S\mathbf{B}\cdot d\mathbf{S}\quad[\text{Wb} = \text{T·m}^2 = \text{V·s}],\qquad \oint_{\text{closed}}\mathbf{B}\cdot d\mathbf{S} = 0 .
> $$
> For an open surface $S$ bounded by a directed loop $C$, $d\mathbf{S}$ follows the right-hand rule from $C$, and $\Psi$ is called the flux **linking** $C$: field lines thread the loop like links of a chain. Because the closed-surface flux vanishes, every surface spanning the same $C$ gives the same $\Psi$ — the flat disk and the bowl agree. For an $N$-turn coil whose turns each link $\Psi$, the flux *linkage* is $N\Psi$.

**Physics.** $\Psi$ is to $\mathbf{B}$ what $\psi_E = \int\mathbf{D}\cdot d\mathbf{S}$ is to $\mathbf{D}$ ([[concepts/flux]]), with one difference: there is no magnetic charge, so no closed surface ever has net magnetic flux and no field line ever begins or ends. The "weber" in T = Wb/m² is this flux; the "volt-second" in Wb = V·s is Faraday's law: a flux changing at 1 Wb/s drives an emf of 1 V around the loop. Two roles in the course: [[concepts/faradays-law]] differentiates it, $\mathcal{E} = -d\Psi/dt$, and [[concepts/inductance]] divides it by the current that made it, $L = N\Psi/I$. It is also the circulation of the vector potential, $\Psi = \oint_C\mathbf{A}\cdot d\mathbf{l}$.

**Examples.** Uniform $B_0\hat z$ through a circle of radius $r$ in the plane $z = 0$: $\Psi = \pi r^2B_0$ (10 m radius, $B_0 = 1$ T: 314 Wb). A 2 m square above a line current $I$ along $x$, between $y = 2t-1$ and $2t+1$: $\Psi = \dfrac{\mu_0I}{\pi}\ln\dfrac{2t+1}{2t-1}$ ([[2-magnetostatics/14-faradays-law-and-induced-emf|Lecture 14]], Example 2). A shorted coax of length $\ell$: $\Psi = \dfrac{\mu\ell I}{2\pi}\ln\dfrac ba$ through the $r$–$z$ rectangle between the conductors ([[2-magnetostatics/15-inductance-magnetic-energy-and-the-potentials|Lecture 15]]). A solenoid turn: $\Psi = \mu_0nIA$.

> [!trap]
> - Choose the surface that makes the integral easy — any surface on $C$ will do — but orient it by the right-hand rule from the direction you chose for $C$, or the sign of the emf comes out wrong.
> - For a coax the flux-linking surface is the rectangle between the conductors (normal $\hat\phi$, along $\mathbf{B}$), not a circle.
> - $\Psi$ of an $N$-turn coil: count the field once (it is produced by all $N$ turns, $B\propto nI$) and the linkage once more ($N\Psi$); both factors of $N$ are real, which is why $L\propto N^2$.
> - Units: Wb, never T.

**Where it appears.** [[1-electrostatics/03-gauss-law-at-work#6-the-magnetic-counterpart--bds--0|Lecture 3 §6]] (closed-surface flux is zero), Lecture 14 (linked flux, flux rule, six examples), Lecture 15 (inductance, flux of the coax and solenoid), [[problems/emf-of-a-loop-moving-near-a-line-current]], [[problems/coax-inductance-and-the-lc-product]].

**Practice.** [[practice/topics#magnetic-flux-faradays-law-and-lenz|Magnetic flux, Faraday's law and Lenz]] (10 problems) — for example [[practice/14-faradays-law-and-induced-emf#141-flux-through-a-tilted-loop|14.1 Flux through a tilted loop]] (easy), [[practice/04-divergence-and-curl#48-circulation-from-a-given-curl|4.8 Circulation from a given curl]] (medium), [[practice/14-faradays-law-and-induced-emf#149-loop-crossing-a-field-strip|14.9 Loop crossing a field strip]] (hard).

Related: [[concepts/flux]] · [[concepts/faradays-law]] · [[concepts/inductance]] · [[concepts/vector-potential]].
