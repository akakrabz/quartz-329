---
title: "Electromotive force (emf) and path-dependent voltage"
description: "ℰ = ∮(E + v×B)·dl, work per unit charge once around a closed path, in volts. With changing flux, voltage depends on the path; a voltmeter reads the integral along its own leads."
tags: [concept, magnetostatics]
aliases: ["emf", "EMF", "voltmeter paradox", "path-dependent voltage", "back-emf"]
---

> [!key] Definition
> $$
> \begin{gathered}
> \mathcal{E}\equiv\oint_C(\mathbf{E}+\mathbf{v}\times\mathbf{B})\cdot d\mathbf{l}\quad[\text{V}],\\[4pt]
> \mathcal{E} = -\frac{d\Psi}{dt}\ \ (\text{Faraday}),\qquad I = \frac{\mathcal{E}}{R}\ \ (\text{conducting loop, self-inductance neglected}).
> \end{gathered}
> $$
> Lorentz-force work per unit charge carried once around the directed path $C$. In circuits: the sum of **rises** around the loop, equated by KVL to the drops: $RI = -d\Psi/dt$. Since Maxwell, "emf" means any *source of energy* driving current around a resistive loop: a battery, or a changing linked flux. A coil's own $-L\,dI/dt$ is the **back-emf**.

**Physics.** In electrostatics $\oint\mathbf{E}\cdot d\mathbf{l} = 0$, so $\int_A^B\mathbf{E}\cdot d\mathbf{l}$ is a *voltage* $V_A - V_B$, the same for every path ([[concepts/conservative-field]]). With $d\Psi/dt\neq0$ the **voltage of a path** $P$, $\int_P(\mathbf{E}+\mathbf{v}\times\mathbf{B})\cdot d\mathbf{l}$ (just $\int_P\mathbf{E}\cdot d\mathbf{l}$ for a stationary path), depends on $P$:

- **A voltmeter reads the voltage of its own path**, formed by its probe wires from red lead to black. Two ideal meters on the same nodes A and B, leads routed differently, differ by $-d\Psi/dt$ through the loop the two lead paths enclose.
- **A moving conductor is a battery.** In a bar moving at $\mathbf{v}$ through $\mathbf{B}$, $\mathbf{v}\times\mathbf{B}$ acts like a cell's chemical force: emf $vB\ell$ across its ends, the bar's resistance internal ([[2-magnetostatics/14-faradays-law-and-induced-emf#4-motional-emf-the-sliding-bar|Lecture 14 §4]]). The lab electric field is static and the same in bar and load; only the bar has $\mathbf{v}\times\mathbf{B}$.

**Examples.** Square loop of 1 m², $R_1 = 2\ \Omega$ and $R_2 = 1\ \Omega$ on opposite sides, $\mathbf{B} = (12-3t)\hat z$: $\mathcal{E} = 3$ V, $I = 1$ A; from corner A to B a meter reads $+2$ V along the $R_1$ side, $-1$ V along the $R_2$ side, $+0.5$ V along the diagonal. Loop of 1 Ω + 3 Ω around a solenoid with $-d\Psi/dt = 8$ V: $I = 2$ A, and a meter across the 1 Ω resistor reads $\pm2$ V or $\mp6$ V depending on which side of the solenoid its leads pass, differing by the 8 V emf ([[2-magnetostatics/14-faradays-law-and-induced-emf#5-when-voltage-stops-being-a-number-the-voltmeter-paradox|Lecture 14 §5]]; re-parameterized in [[problems/sliding-bar-and-the-voltmeter-readings]]).

> [!trap]
> - Volts, not newtons: $\mathcal{E}$ is energy per charge.
> - "The voltage between A and B" is undefined when the flux between the candidate paths changes; say *along which path*.
> - KVL "fails" only when the emf is left out: circuit theory assumes the wiring's flux negligible or lumped into an inductor, untrue for a circuit threading a transformer core or sitting in a changing field.
> - A charge's own motion *along* the path adds nothing: $(\mathbf{v}_q\times\mathbf{B})\cdot d\mathbf{l} = 0$ when $\mathbf{v}_q\parallel d\mathbf{l}$.

**Where it appears.** Lecture 14 (definition, KVL reading, Examples 4–6), [[2-magnetostatics/15-inductance-magnetic-energy-and-the-potentials|Lecture 15]] (self-emf, the inductor's $V = L\,dI/dt$), [[1-electrostatics/05-curl-free-fields-and-the-electrostatic-potential|Lecture 5]] (the voltage generalized here), the MMF ↔ EMF pairing of [[concepts/amperes-law]].

**Practice.** [[practice/topics#magnetic-flux-faradays-law-and-lenz|Magnetic flux, Faraday's law and Lenz]] (11 problems) · [[practice/topics#motional-emf-and-generators|Motional emf and generators]] (7 problems) — for example [[practice/14-faradays-law-and-induced-emf#141-flux-through-a-tilted-loop|14.1 Flux through a tilted loop]] (easy), [[practice/14-faradays-law-and-induced-emf#146-rotating-rod-on-a-circular-rail|14.6 Rotating rod on a circular rail]] (medium), [[practice/14-faradays-law-and-induced-emf#149-loop-crossing-a-field-strip|14.9 Loop crossing a field strip]] (hard).

Related: [[concepts/faradays-law]] · [[concepts/electrostatic-potential]] · [[concepts/inductance]] · [[concepts/lorentz-force]].
