---
title: "Inductance"
description: "L = NΨ/I, in henries: the flux a circuit links per ampere of its own current. Self-emf −L dI/dt (a rise), circuit drop V = L dI/dt, time constant L/R. Computed by the Ampère chain I → H → B → Ψ → L; for any two-conductor line 𝓛𝓒 = με."
tags: [concept, magnetostatics]
aliases: ["self-inductance", "mutual inductance", "henry", "inductor", "inductance per unit length"]
---

> [!key] Definition
> $$
> \begin{gathered}
> \Psi = LI,\qquad L = \frac{N\Psi}{I}\ \ge0\quad[\text{H} = \text{Wb/A}],\\[4pt]
> \mathcal{E} = -L\frac{dI}{dt}\ (\text{rise along }I),\qquad V = L\frac{dI}{dt}\ (\text{drop along }I).
> \end{gathered}
> $$
> $\Psi$ is the flux through one turn produced by the circuit's own current $I$; $N$ the number of turns linking it. $L$ depends only on geometry and $\mu$. Mutual inductance $M = \Psi_{1\leftarrow2}/I_2$ (henries) couples two circuits — transformers, ECE 330. Per unit length of a transmission line, $\mathcal{L} = L/\ell$ [H/m].

**Physics.** The magnetic twin of [[concepts/capacitance]]: linearity of Biot–Savart makes $\Psi\propto I$ exactly as linearity of Coulomb made $Q\propto V$. Faraday's law applied to the circuit's own loop produces the self-emf $-L\,dI/dt$, a voltage rise in the direction of the current that opposes any change in it (Lenz applied to the circuit itself); the circuits-course $V = L\,dI/dt$ is the same statement in the passive sign convention. A coil shorted through $R$ obeys $RI = -L\,dI/dt$ and decays as $e^{-t/\tau}$ with $\tau = L/R$ — large $L$ behaves as a slowly varying *current* source, as large $C$ behaves as a voltage source. Energy $\tfrac12LI^2$ ([[concepts/magnetic-energy]]).

> [!recipe] Computing L
> Assume $I$ → $\mathbf{H}$ by [[concepts/amperes-law]] (or Biot–Savart) → $\mathbf{B} = \mu\mathbf{H}$ → $\Psi = \int_S\mathbf{B}\cdot d\mathbf{S}$ over the surface bounded by the current path (×$N$ for $N$ linked turns) → $L = N\Psi/I$. The assumed $I$ cancels.

**Results.**

| structure | $L$ | with |
|---|---|---|
| long solenoid, $n$ turns/m, area $A$, length $\ell$, $N = n\ell$ | $n^2\mu_0A\ell = N^2\mu_0A/\ell$ | $B = \mu_0nI$ inside |
| shorted coax, radii $a<b$, length $\ell$ | $\dfrac{\mu\ell}{2\pi}\ln\dfrac ba$, $\ \mathcal{L} = \dfrac{\mu}{2\pi}\ln\dfrac ba$ | $B_\phi = \mu I/2\pi r$; flux through the $r$–$z$ rectangle; external inductance only |
| shorted parallel plates, width $W$, gap $d$ | $\mathcal{L} = \mu\,d/W$ | $H = I/W$ between the plates |

Beside $\mathcal{C} = 2\pi\epsilon/\ln(b/a)$ and $\mathcal{C} = \epsilon W/d$: the geometric factor of $\mathcal{L}$ is the inverse of the geometric factor of $\mathcal{C}$, so $\mathcal{L}\mathcal{C} = \mu\epsilon$ for any line with one homogeneous filling, and $1/\sqrt{\mathcal{LC}} = 1/\sqrt{\mu\epsilon}$ is the signal speed (Unit 4). Also $\mathcal{G}/\mathcal{C} = \sigma/\epsilon$.

> [!trap]
> - $N$ enters twice (field $\propto nI$, linkage $N\Psi$), hence $N^2$; do not count it a third time.
> - The flux surface is the one *bounded by the current path* — for the coax a rectangle between the conductors, not a circle.
> - $-L\,dI/dt$ is a rise and $L\,dI/dt$ a drop, both in the direction of $I$; a shorted coil has $RI = -L\,dI/dt$, with no minus sign missing.
> - "A coil has $L = \ldots$" lumps the field into an element; the lumped model needs the coil to be small compared with $\lambda = c/f$.
> - Check coax numbers against $\mathcal{LC} = \mu\epsilon$.

**Where it appears.** [[2-magnetostatics/15-inductance-magnetic-energy-and-the-potentials|Lecture 15]] (all of the above), [[2-magnetostatics/14-faradays-law-and-induced-emf|Lecture 14]] (the self-emf that $I = \mathcal{E}/R$ neglects), [[1-electrostatics/10-capacitance-and-conductance|Lecture 10]] (the twin), [[problems/coax-inductance-and-the-lc-product]]; the telegrapher's equations of Unit 4 are built from $\mathcal{L}$ and $\mathcal{C}$.

**Practice.** [[practice/topics#inductance|Inductance]] (8 problems) — for example [[practice/15-inductance-and-magnetic-energy#151-a-long-solenoid-by-the-numbers|15.1 A long solenoid by the numbers]] (easy), [[practice/15-inductance-and-magnetic-energy#157-internal-inductance-of-a-wire|15.7 Internal inductance of a wire]] (medium), [[practice/15-inductance-and-magnetic-energy#159-toroid-with-a-two-layer-core|15.9 Toroid with a two-layer core]] (hard).

Related: [[concepts/capacitance]] · [[concepts/magnetic-flux]] · [[concepts/faradays-law]] · [[concepts/magnetic-energy]] · [[concepts/conductance]].
