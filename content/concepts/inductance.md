---
title: "Inductance"
description: "L = NΨ/I, in henries: flux linked per ampere of a circuit's own current. Self-emf −L dI/dt, time constant L/R, the Ampère chain I → H → B → Ψ → L, and 𝓛𝓒 = με."
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
> $\Psi$: flux through one turn from the circuit's own $I$; $N$: turns linking it. $L$ depends only on geometry and $\mu$. Mutual inductance $M = \Psi_{1\leftarrow2}/I_2$ couples two circuits (transformers, ECE 330). Per unit length: $\mathcal{L} = L/\ell$ [H/m].

**Physics.** Magnetic twin of [[concepts/capacitance]]: linear Biot–Savart makes $\Psi\propto I$ as linear Coulomb made $Q\propto V$. Faraday's law on the circuit's own loop gives the self-emf $-L\,dI/dt$, a rise along $I$ opposing any change in it (Lenz). A coil shorted through $R$ obeys $RI = -L\,dI/dt$ and decays as $e^{-t/\tau}$, $\tau = L/R$: large $L$ acts as a slowly varying *current* source (large $C$: a voltage source). Energy $\tfrac12LI^2$ ([[concepts/magnetic-energy]]).

> [!recipe] Computing L
> Assume $I$ → $\mathbf{H}$ by [[concepts/amperes-law]] (or Biot–Savart) → $\mathbf{B} = \mu\mathbf{H}$ → $\Psi = \int_S\mathbf{B}\cdot d\mathbf{S}$ over the surface bounded by the current path (×$N$ for $N$ turns) → $L = N\Psi/I$. $I$ cancels.

**Results.**

| structure | $L$ | with |
|---|---|---|
| long solenoid, $n$ turns/m, area $A$, length $\ell$, $N = n\ell$ | $n^2\mu_0A\ell = N^2\mu_0A/\ell$ | $B = \mu_0nI$ inside |
| shorted coax, radii $a<b$, length $\ell$ | $\dfrac{\mu\ell}{2\pi}\ln\dfrac ba$, $\ \mathcal{L} = \dfrac{\mu}{2\pi}\ln\dfrac ba$ | $B_\phi = \mu I/2\pi r$; flux through the $r$–$z$ rectangle; external inductance only |
| shorted parallel plates, width $W$, gap $d$ | $\mathcal{L} = \mu\,d/W$ | $H = I/W$ inside |

**With a magnetic core, $L\propto\mu$** ([[3-maxwell-and-waves/17-magnetization-and-maxwells-equations-in-matter|Lecture 17]]). The free current fixes $\mathbf{H}$, so the flux $\int\mu\mathbf{H}\cdot d\mathbf{S}$ scales with $\mu$: a cored solenoid has $L = n^2\mu A\ell$, $\mu_r$ times the air value (12.6 μH → 1.26 mH for $n = 1000$/m, $A = 1$ cm², $\ell = 10$ cm, $\mu_r = 100$). Such measurements are the notes' evidence that $\mathbf{M}\propto\mathbf{H}$ in most materials. Iron's $L$ depends on the current, collapsing toward the air value at saturation.

Next to $\mathcal{C} = 2\pi\epsilon/\ln(b/a)$ and $\mathcal{C} = \epsilon W/d$, the geometric factors invert, so $\mathcal{L}\mathcal{C} = \mu\epsilon$ for any line with one homogeneous filling, and $1/\sqrt{\mathcal{LC}} = 1/\sqrt{\mu\epsilon}$ is the signal speed (Unit 4). Also $\mathcal{G}/\mathcal{C} = \sigma/\epsilon$.

> [!trap]
> - $N$ enters twice (field $\propto nI$, linkage $N\Psi$), hence $N^2$; not a third time.
> - Coax flux surface: the rectangle between the conductors, not a circle.
> - $-L\,dI/dt$ is a rise, $L\,dI/dt$ a drop (passive convention), both along $I$; hence the shorted coil's minus sign.
> - A lumped $L$ needs the coil small compared with $\lambda = c/f$.

**Where it appears.** [[2-magnetostatics/15-inductance-magnetic-energy-and-the-potentials|Lecture 15]], [[2-magnetostatics/14-faradays-law-and-induced-emf|Lecture 14]] (the self-emf that $I = \mathcal{E}/R$ neglects), [[1-electrostatics/10-capacitance-and-conductance|Lecture 10]] (the twin), [[problems/coax-inductance-and-the-lc-product]]; Unit 4's telegrapher's equations are built from $\mathcal{L}$ and $\mathcal{C}$.

**Practice.** [[practice/topics#inductance|Inductance]] (11 problems) — for example [[practice/15-inductance-and-magnetic-energy#151-a-long-solenoid-by-the-numbers|15.1 A long solenoid by the numbers]] (easy), [[practice/15-inductance-and-magnetic-energy#157-internal-inductance-of-a-wire|15.7 Internal inductance of a wire]] (medium), [[practice/15-inductance-and-magnetic-energy#159-toroid-with-a-two-layer-core|15.9 Toroid with a two-layer core]] (hard).

Related: [[concepts/capacitance]] · [[concepts/magnetic-flux]] · [[concepts/faradays-law]] · [[concepts/magnetic-energy]] · [[concepts/conductance]].
