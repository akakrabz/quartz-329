---
title: "Electromotive force (emf) and path-dependent voltage"
description: "ℰ = ∮(E + v×B)·dl, work per unit charge once around a closed path, in volts; for a moving or deforming loop it equals −dΨ/dt (the swept-band derivation). I = ℰ/R, the KVL reading, and why with changing flux voltage depends on the path."
tags: [concept, magnetostatics]
aliases: ["emf", "EMF", "path-dependent voltage", "back-emf", "voltage of a path", "KVL with induction"]
---

> [!key] The flux rule, and the emf
> $$
> \boxed{\ \mathcal{E}\equiv\oint_C(\mathbf{E}+\mathbf{v}\times\mathbf{B})\cdot d\mathbf{l} = -\frac{d\Psi}{dt}\ }
> $$
> The left side is the **work per unit charge** done by the Lorentz force on a charge carried once around the directed path $C$ ($\mathbf{v}$ = velocity of the path; a charge's own velocity *along* the path adds nothing, since $(\mathbf{v}_q\times\mathbf{B})\cdot d\mathbf{l} = 0$ when $\mathbf{v}_q\parallel d\mathbf{l}$). Faraday's name, **electromotive force** $\mathcal{E}$, is poor: it is work per charge (volts), not a force. A conducting loop of resistance $R$ carries
> $$
> I = \frac{\mathcal{E}}{R}
> $$
> in the circulation direction (for $\mathcal{E}>0$): inside the wire $\mathbf{J} = \sigma(\mathbf{E}+\mathbf{v}\times\mathbf{B})$, as in a battery-driven resistor, and integrating around a homogeneous loop gives $I\cdot(\text{length}/\sigma A) = \mathcal{E}$ (self-inductance neglected — [[concepts/inductance|Inductance]]).

**Physics.** [[concepts/faradays-law|Faraday's law]] for a fixed loop is $\oint\mathbf{E}\cdot d\mathbf{l} = -d\Psi/dt$. If $C$ moves or deforms, $d/dt$ and $\int_S$ no longer commute: part of $d\Psi/dt$ comes from the loop sweeping through the field, and the notes (margin, p. 2) show the extra piece is a circulation of $\mathbf{v}\times\mathbf{B}$:

> [!derivation]- The swept band (course notes, Lecture 14 margin)
> Let $S$ span $C$ at time 0 and $C(\Delta t)$ be the displaced loop, each point moved by $\mathbf{v}\Delta t$. The band $\delta S$ swept between $C$ and $C(\Delta t)$ has area elements $d\mathbf{S} = \Delta t\,\mathbf{v}\times d\mathbf{l}$. Spanning $C(\Delta t)$ by $S\cup\delta S$:
> $$
> \frac{\Psi(\Delta t)-\Psi(0)}{\Delta t} = \int_S\frac{\mathbf{B}(\mathbf{r},\Delta t)-\mathbf{B}(\mathbf{r},0)}{\Delta t}\cdot d\mathbf{S} + \oint_C\mathbf{B}\cdot(\mathbf{v}\times d\mathbf{l}),
> $$
> and since $\mathbf{B}\cdot(\mathbf{v}\times d\mathbf{l}) = -(\mathbf{v}\times\mathbf{B})\cdot d\mathbf{l}$ (both the volume of the parallelepiped on $d\mathbf{l}$, $\mathbf{v}$, $\mathbf{B}$, up to sign),
> $$
> \frac{d\Psi}{dt} = \int_S\frac{\partial\mathbf{B}}{\partial t}\cdot d\mathbf{S} - \oint_C(\mathbf{v}\times\mathbf{B})\cdot d\mathbf{l}.
> $$
> $\mathbf{v}$ may vary around $C$ — the loop may stretch or rotate. With Faraday's law for the first term, the boxed flux rule follows: it covers every case ([[concepts/faradays-law|the three ways to change Ψ]]).

**Reading it as a circuit.** $RI = -d\Psi/dt$ is KVL for the loop: $RI$ is the sum of voltage **drops** in the direction of $C$, $-d\Psi/dt$ a voltage **rise** in the same direction — a source. Since Maxwell, "emf" means any *source of energy* driving current around a resistive loop: a battery, or a changing linked flux. A non-conducting path has an emf too; it drives no current. A coil's own $-L\,dI/dt$ is the **back-emf**, a rise along $I$ ([[concepts/inductance|Inductance]]). The magnetic twin is the MMF $\oint\mathbf{H}\cdot d\mathbf{l}$ in amperes ([[concepts/amperes-law|Ampère's law]]).

**Path-dependent voltage.** In electrostatics $\oint\mathbf{E}\cdot d\mathbf{l} = 0$, so $\int_A^B\mathbf{E}\cdot d\mathbf{l}$ is a *voltage* $V_A - V_B$, the same for every path ([[concepts/conservative-field|Conservative (curl-free) fields and the potential]], [[1-electrostatics/05-curl-free-fields-and-the-electrostatic-potential#4-path-independence|Lecture 5 §4]]). With $d\Psi/dt\neq0$ the **voltage of a path** $P$, $\int_P(\mathbf{E}+\mathbf{v}\times\mathbf{B})\cdot d\mathbf{l}$ (just $\int_P\mathbf{E}\cdot d\mathbf{l}$ for a stationary path), depends on $P$:

- **A voltmeter reads the voltage of its own path**, formed by its probe wires from red lead to black. Two ideal meters on the same nodes A and B, leads routed differently, differ by $-d\Psi/dt$ through the loop the two lead paths enclose.
- **A moving conductor is a battery.** In a bar moving at $\mathbf{v}$ through $\mathbf{B}$, $\mathbf{v}\times\mathbf{B}$ acts like a cell's chemical force: emf $vB\ell$ across its ends, the bar's resistance internal. The lab electric field is static and the same in bar and load; only the bar has $\mathbf{v}\times\mathbf{B}$.

Both are worked with the lecture's numbers on [[concepts/motional-emf|Motional emf and the voltmeter paradox]] (sliding bar, the loop around a solenoid, the dissected square loop). Circuit theory survives because in a well-designed circuit the flux through the wiring is negligible — or lumped into an inductor.

**Examples.** Transformer emfs with numbers: [[concepts/faradays-law|Faraday's law]] (decaying field, receding loop, 60 Hz generator). Motional emfs and voltmeter readings: [[concepts/motional-emf|Motional emf and the voltmeter paradox]]. The receding loop shows the two routes agreeing: $-d\Psi/dt$ and $\oint(\mathbf{v}\times\mathbf{B})\cdot d\mathbf{l}$ both give $\mu_0I/[\pi(t^2-\tfrac14)]$.

> [!trap]
> - Volts, not newtons: $\mathcal{E}$ is energy per charge.
> - "The voltage between A and B" is undefined when the flux between the candidate paths changes; say *along which path*.
> - KVL "fails" only when the emf is left out: circuit theory assumes the wiring's flux negligible or lumped into an inductor, untrue for a circuit threading a transformer core or sitting in a changing field.
> - $I = \mathcal{E}/R$ is the special case $L\,dI/dt\ll\mathcal{E}$; in general the loop obeys an ODE with its self-emf.

> [!exam] On exams
> State $\mathcal{E}$ as a closed-path integral with its direction, equate it to $-d\Psi/dt$, then $I = \mathcal{E}/R$ with the direction of circulation; read the result as KVL (rise $-d\Psi/dt$ = drop $RI$). For "which voltmeter is right", answer "both — each reads its own path". Calling $\mathcal{E}$ a force, or writing a voltage without naming the path, loses points.

**Where it appears.** [[2-magnetostatics/14-faradays-law-and-induced-emf#2-moving-loops-the-emf-and-lenz|Lecture 14 §2]] (definition, derivation, KVL reading), [[2-magnetostatics/14-faradays-law-and-induced-emf#4-motional-emf-the-sliding-bar|§4]]–[[2-magnetostatics/14-faradays-law-and-induced-emf#5-when-voltage-stops-being-a-number-the-voltmeter-paradox|§5]] (Examples 4–6), [[2-magnetostatics/15-inductance-magnetic-energy-and-the-potentials|Lecture 15]] (self-emf, the inductor's $V = L\,dI/dt$), [[1-electrostatics/05-curl-free-fields-and-the-electrostatic-potential|Lecture 5]] (the voltage generalized here), [[problems/sliding-bar-and-the-voltmeter-readings|Worked problem — The sliding bar, and what a voltmeter reads]].

**Related.** [[concepts/faradays-law|Faraday's law]] · [[concepts/motional-emf|Motional emf and the voltmeter paradox]] · [[concepts/electrostatic-potential|Electrostatic potential V]] · [[concepts/inductance|Inductance]] · [[concepts/lorentz-force|Lorentz force]].

**Practice.** [[practice/topics#magnetic-flux-faradays-law-and-lenz|Magnetic flux, Faraday's law and Lenz]] (11 problems) · [[practice/topics#motional-emf-and-generators|Motional emf and generators]] (7 problems) — for example [[practice/14-faradays-law-and-induced-emf#141-flux-through-a-tilted-loop|14.1 Flux through a tilted loop]] (easy), [[practice/14-faradays-law-and-induced-emf#146-rotating-rod-on-a-circular-rail|14.6 Rotating rod on a circular rail]] (medium), [[practice/14-faradays-law-and-induced-emf#149-loop-crossing-a-field-strip|14.9 Loop crossing a field strip]] (hard).
