---
title: "Faraday's law"
description: "∇×E = −∂B/∂t: a changing B makes a circulating E. Around any loop ℰ = ∮(E + v×B)·dl = −dΨ/dt (the flux rule), however the flux changes; Lenz's rule fixes the sign."
tags: [concept, magnetostatics]
aliases: ["flux rule", "law of induction", "Lenz's rule", "Lenz's law", "motional emf", "transformer emf"]
---

> [!key] Definition
> $$
> \nabla\times\mathbf{E} = -\frac{\partial\mathbf{B}}{\partial t}\qquad\Longleftrightarrow\qquad \oint_C\mathbf{E}\cdot d\mathbf{l} = -\int_S\frac{\partial\mathbf{B}}{\partial t}\cdot d\mathbf{S},
> $$
> for every surface $S$ on every closed directed path $C$, $d\mathbf{S}$ by the right-hand rule from $C$. For a loop moving or deforming with velocity $\mathbf{v}$,
> $$
> \mathcal{E}\equiv\oint_C(\mathbf{E}+\mathbf{v}\times\mathbf{B})\cdot d\mathbf{l} = -\frac{d\Psi}{dt},\qquad \Psi = \int_S\mathbf{B}\cdot d\mathbf{S},
> $$
> the **flux rule**, however the flux change is produced.

**Physics.** The first curl equation with a time derivative, and the end of path-independent voltage: $\mathbf{E}$ gains a circulating part ($-\partial\mathbf{A}/\partial t$, with $\mathbf{A}$ the [[concepts/vector-potential]]). Three ways to get $d\Psi/dt\neq0$: (1) fixed $C$, $\mathbf{B}$ varying in time: *transformer* emf, all of it $\oint\mathbf{E}\cdot d\mathbf{l}$; (2) constant $\mathbf{B}$, $C$ moving, rotating or stretching: *motional*, all of it $\oint(\mathbf{v}\times\mathbf{B})\cdot d\mathbf{l}$; (3) static nonuniform $\mathbf{B}$, $C$ moving through it: also motional. A loop moving through a *uniform* static field has no emf. Riding with the loop in cases 2–3, an observer sees case 1, with $\mathbf{E}' = \mathbf{v}\times\mathbf{B}$; the Lorentz force is (nearly) frame-invariant at low speeds, so the current agrees. The induced $\mathbf{E}$ is ultimately caused by the time-varying *current* behind the changing $\mathbf{B}$ (Lecture 14, footnote 1). **Lenz's rule** is the minus sign: the induced current's field opposes the flux change; the other sign would make induced currents grow without limit.

**In a wave.** Faraday's law is half of the E–H recursion that makes a wave; the displacement current is the other. For $\mathbf{E} = \hat xE_x(z,t)$ it reads $\partial E_x/\partial z = -\mu\,\partial H_y/\partial t$: where $\mathbf{E}$ varies along the travel direction, $\mathbf{H}$ changes in time. Integrated in time, it gives [[3-maxwell-and-waves/18-the-wave-equation-and-plane-tem-waves|Lecture 18]] the $\mathbf{H}$ of a given $\mathbf{E}$: $\mathbf{H} = \pm\hat y\,f(t\mp z/v)/\eta$ ([[concepts/plane-waves]]).

**Examples.** Circle of radius 10 m in $B_0e^{-t/\tau}\hat z$: $\mathcal{E} = 100\pi(B_0/\tau)e^{-t/\tau}$ V, counter-clockwise, propping up the decaying field. Square loop receding from a line current: $\mathcal{E} = \mu_0I/[\pi(t^2-\tfrac14)]$ by $-d\Psi/dt$ *and* by $\oint(\mathbf{v}\times\mathbf{B})\cdot d\mathbf{l}$. Generator: $\Psi = \Psi_0\cos\omega t$, $\mathcal{E} = \omega\Psi_0\sin\omega t$. Sliding bar: $\mathcal{E} = vB\ell$, a battery with internal resistance. All six in [[2-magnetostatics/14-faradays-law-and-induced-emf|Lecture 14]].

> [!trap]
> - Orient $C$ first; $d\mathbf{S}$ follows, and the sign of $\mathcal{E}$ is relative to it. "Counter-clockwise" needs a viewpoint ("seen from $+z$").
> - Moving loop: $-d\Psi/dt$ with the *total* derivative; $-\int\partial_t\mathbf{B}\cdot d\mathbf{S}$ is only the transformer part.
> - $I = \mathcal{E}/R$ neglects the self-emf $-L\,dI/dt$ ([[concepts/inductance]]); fine when $L\,dI/dt\ll\mathcal{E}$.
> - $\mathcal{E}$ is work per unit charge, in volts, not a force.
> - Perfectly conducting parts of a loop add nothing to $\oint\mathbf{E}\cdot d\mathbf{l}$; resistors and moving conductors carry it.

**Where it appears.** Previewed in [[1-electrostatics/04-divergence-and-curl|Lecture 4]] and [[concepts/conservative-field]]; worked in Lecture 14; self-inductance in [[2-magnetostatics/15-inductance-magnetic-energy-and-the-potentials|Lecture 15]]; paired with Ampère–Maxwell in [[3-maxwell-and-waves/16-charge-conservation-displacement-current-and-maxwells-equations|Lecture 16]] to give waves; [[problems/emf-of-a-loop-moving-near-a-line-current]], [[problems/sliding-bar-and-the-voltmeter-readings]].

**Practice.** [[practice/topics#magnetic-flux-faradays-law-and-lenz|Magnetic flux, Faraday's law and Lenz]] (11 problems) — for example [[practice/14-faradays-law-and-induced-emf#141-flux-through-a-tilted-loop|14.1 Flux through a tilted loop]] (easy), [[practice/04-divergence-and-curl#48-circulation-from-a-given-curl|4.8 Circulation from a given curl]] (medium), [[practice/14-faradays-law-and-induced-emf#149-loop-crossing-a-field-strip|14.9 Loop crossing a field strip]] (hard).

Related: [[concepts/electromotive-force]] · [[concepts/magnetic-flux]] · [[concepts/stokes-theorem]] · [[concepts/lorentz-force]] · [[concepts/maxwells-equations]].
