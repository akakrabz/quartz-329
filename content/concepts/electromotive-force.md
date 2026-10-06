---
title: "Electromotive force (emf) and path-dependent voltage"
description: "ℰ = ∮(E + v×B)·dl is the work per unit charge once around a closed path — a source, in volts, not a force. When flux changes, the 'voltage' of a path depends on the path, a voltmeter reads the line integral along its own leads, and two meters on the same nodes can disagree by the emf of the loop their leads form."
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
> The work the Lorentz force does per unit charge carried once around the directed path $C$. In circuit language it is the sum of the voltage **rises** around the loop, which KVL equates to the sum of the drops: $RI = -d\Psi/dt$. Since Maxwell, "emf" means any *source of energy* that drives current around a resistive loop — a battery, or a changing linked flux. The self-emf $-L\,dI/dt$ of a coil's own current is also called the **back-emf**.

**Physics.** In electrostatics $\oint\mathbf{E}\cdot d\mathbf{l} = 0$, so $\int_A^B\mathbf{E}\cdot d\mathbf{l}$ is a *voltage* $V_A - V_B$ independent of the path — [[concepts/conservative-field]]. With $d\Psi/dt\neq0$ the circulation is not zero, and the **voltage of a path** $P$, $\int_P(\mathbf{E}+\mathbf{v}\times\mathbf{B})\cdot d\mathbf{l}$ (just $\int_P\mathbf{E}\cdot d\mathbf{l}$ for a stationary path), depends on $P$. Two consequences the course insists on:

- **A voltmeter reads the voltage of its own path** — the path formed by its probe wires from the red lead to the black one. Connect two ideal meters to the same nodes A and B with the leads routed differently and they differ by $-d\Psi/dt$ through the loop the two lead paths enclose.
- **A moving conductor is a battery.** Inside a bar moving at $\mathbf{v}$ through $\mathbf{B}$, $\mathbf{v}\times\mathbf{B}$ acts like the chemical force in a cell; the emf $vB\ell$ appears across its ends, with the bar's own resistance as internal resistance ([[2-magnetostatics/14-faradays-law-and-induced-emf#4-motional-emf-the-sliding-bar|Lecture 14 §4]]). The lab electric field is static and the same in the bar and in the load — only the bar has the $\mathbf{v}\times\mathbf{B}$ term.

**Examples.** A square loop of 1 m² with $R_1 = 2\ \Omega$ and $R_2 = 1\ \Omega$ on opposite sides in $\mathbf{B} = (12-3t)\hat z$: $\mathcal{E} = 3$ V, $I = 1$ A. From corner A to corner B a meter reads $+2$ V along the $R_1$ side, $-1$ V along the $R_2$ side, $+0.5$ V along the diagonal. A loop of 1 Ω + 3 Ω around a solenoid with $-d\Psi/dt = 8$ V: $I = 2$ A, and a meter across the 1 Ω resistor reads $\pm2$ V or $\mp6$ V depending on which side of the solenoid its leads pass — opposite signs, differing by the 8 V emf of the loop the two lead paths enclose ([[2-magnetostatics/14-faradays-law-and-induced-emf#5-when-voltage-stops-being-a-number-the-voltmeter-paradox|Lecture 14 §5]]; re-parameterized in [[problems/sliding-bar-and-the-voltmeter-readings]]).

> [!trap]
> - Volts, not newtons: $\mathcal{E}$ is energy per charge.
> - "The voltage between A and B" is undefined when the flux through the region between the candidate paths is changing; always say *along which path*.
> - Circuit theory works because the flux through the wiring is negligible or has been lumped into an inductor; a circuit that threads a transformer core or sits in a changing field is where KVL "fails" — it has not failed, the emf has been left out.
> - A charge's own motion *along* the path contributes nothing: $(\mathbf{v}_q\times\mathbf{B})\cdot d\mathbf{l} = 0$ when $\mathbf{v}_q\parallel d\mathbf{l}$.

**Where it appears.** Lecture 14 (definition, KVL reading, Examples 4–6), [[2-magnetostatics/15-inductance-magnetic-energy-and-the-potentials|Lecture 15]] (self-emf and the inductor's $V = L\,dI/dt$), [[1-electrostatics/05-curl-free-fields-and-the-electrostatic-potential|Lecture 5]] (the voltage that this concept generalizes), and the MMF ↔ EMF pairing of [[concepts/amperes-law]].

**Practice.** [[practice/topics#magnetic-flux-faradays-law-and-lenz|Magnetic flux, Faraday's law and Lenz]] (11 problems) · [[practice/topics#motional-emf-and-generators|Motional emf and generators]] (7 problems) — for example [[practice/14-faradays-law-and-induced-emf#141-flux-through-a-tilted-loop|14.1 Flux through a tilted loop]] (easy), [[practice/14-faradays-law-and-induced-emf#146-rotating-rod-on-a-circular-rail|14.6 Rotating rod on a circular rail]] (medium), [[practice/14-faradays-law-and-induced-emf#149-loop-crossing-a-field-strip|14.9 Loop crossing a field strip]] (hard).

Related: [[concepts/faradays-law]] · [[concepts/electrostatic-potential]] · [[concepts/inductance]] · [[concepts/lorentz-force]].
