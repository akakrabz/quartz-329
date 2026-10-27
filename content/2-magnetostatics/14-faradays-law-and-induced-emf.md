---
title: "Lecture 14 — Faraday's law and induced emf"
description: "Map of Lecture 14 — Faraday's law and the linked flux, moving loops and the emf, Lenz's rule, three transformer-emf examples, the sliding bar, and the voltmeter paradox; the full treatment is on the linked topic pages."
tags: [lecture, magnetostatics]
lecture: 14
---

*Lecture 14 · course notes §14 · slides "Faraday's Law" · prev: [[2-magnetostatics/13-current-sheets-solenoids-and-the-vector-potential|Lecture 13]] · next: [[2-magnetostatics/15-inductance-magnetic-energy-and-the-potentials|Lecture 15]] · practice: [[practice/14-faradays-law-and-induced-emf|12 problems]]*

> [!abstract] In one breath
> A time-varying magnetic field makes an electric field that **circulates**, $\nabla\times\mathbf{E} = -\partial\mathbf{B}/\partial t$, so voltage is no longer path-independent. Around a loop $C$ this is the flux rule $\mathcal{E} = -d\Psi/dt$: the **emf** $\mathcal{E}$ is the work per unit charge done by $\mathbf{E}+\mathbf{v}\times\mathbf{B}$ once around $C$, and $\Psi = \int\mathbf{B}\cdot d\mathbf{S}$ is the linked flux. *Why* $\Psi$ changes does not matter; the minus sign (Lenz) makes the induced current fight the change. A conducting loop carries $I = \mathcal{E}/R$, a moving bar becomes a battery, and a voltmeter reads $\int\mathbf{E}\cdot d\mathbf{l}$ *along its own leads* — so two meters on the same nodes can disagree.

## 1. The law, and the flux it is about

$\nabla\times\mathbf{E} = -\partial\mathbf{B}/\partial t$, integrated: $\oint_C\mathbf{E}\cdot d\mathbf{l} = -\int_S\partial_t\mathbf{B}\cdot d\mathbf{S}$, $d\mathbf{S}$ from the sense of $C$. The right side is the flux $\Psi$ linking $C$ [Wb], the same for every surface on $C$ since $\nabla\cdot\mathbf{B} = 0$; for a fixed loop, $\oint\mathbf{E}\cdot d\mathbf{l} = -d\Psi/dt$.

→ Full treatment: [[concepts/faradays-law|Faraday's law]] · [[concepts/magnetic-flux|Magnetic flux Ψ]] (the flux itself)

## 2. Moving loops, the emf, and Lenz

The notes' swept-band argument adds $-\oint(\mathbf{v}\times\mathbf{B})\cdot d\mathbf{l}$ to $d\Psi/dt$ for a moving loop, giving $\mathcal{E}\equiv\oint(\mathbf{E}+\mathbf{v}\times\mathbf{B})\cdot d\mathbf{l} = -d\Psi/dt$ in every case; $I = \mathcal{E}/R$; KVL reads rise $-d\Psi/dt$ = drop $RI$. Lenz: the induced current opposes the change; three ways to change $\Psi$ (field varies; loop moves; loop crosses a nonuniform field).

→ Full treatment: [[concepts/electromotive-force|Electromotive force]] (derivation, KVL) · [[concepts/faradays-law|Faraday's law]] (Lenz, the three cases)

## 3. Transformer emf: three examples from the lecture

Notes Example 1 — 10 m circle in $B_0e^{-t/\tau}\hat z$: $\mathcal{E} = 100\pi(B_0/\tau)e^{-t/\tau}$ V, propping up the field. Example 2 — 2 m square receding from a line current at 2 m/s: $\mathcal{E} = \mu_0I/[\pi(t^2-\tfrac14)]$ by $-d\Psi/dt$ *and* by $\oint(\mathbf{v}\times\mathbf{B})\cdot d\mathbf{l}$. Example 3 — generator, 0.1 m loop at 60 Hz in 10 T: $\mathcal{E} = 12\pi^2\sin(120\pi t)$ V, about 10 A peak in 12 Ω.

→ Full treatment: [[concepts/faradays-law|Faraday's law]] (all three with their numbers)
## 4. Motional emf: the sliding bar

Notes Example 4 — bar on perfect rails, 2 m, 3 m/s, 1 T: $\mathcal{E} = 6$ V both by $-d\Psi/dt$ and by $vB\ell$; the lab $\mathbf{E}$ is the same in bar and load ($-2$ V/m with $R_2 = 2\ \Omega$, $-3$ V/m open); the bar is a battery of emf $vB\ell$ with internal resistance $R_1$.

→ Full treatment: [[concepts/motional-emf|Motional emf and the voltmeter paradox]]
## 5. When voltage stops being a number: the voltmeter paradox

Example 5 — 1 Ω + 3 Ω loop around a solenoid with $-d\Psi/dt = 8$ V: 2 A, and a meter reads 2 V or 6 V depending on which side of the solenoid its leads pass. Example 6 — square loop dissected: readings $+2$, $-1$, $+0.5$ V between the same corners along three routes. Voltage is the voltage *of a path*.

→ Full treatment: [[concepts/motional-emf|Motional emf and the voltmeter paradox]] · [[concepts/electromotive-force|Electromotive force]] (path-dependent voltage)

## 6. Summary

- $\nabla\times\mathbf{E} = -\partial\mathbf{B}/\partial t$; $\oint_C\mathbf{E}\cdot d\mathbf{l} = -\int_S\partial_t\mathbf{B}\cdot d\mathbf{S}$, $C$ and $d\mathbf{S}$ by the right-hand rule.
- $\Psi = \int_S\mathbf{B}\cdot d\mathbf{S}$ [Wb], the same for every $S$ on $C$; fixed loop: $\oint\mathbf{E}\cdot d\mathbf{l} = -d\Psi/dt$.
- $\mathcal{E}\equiv\oint(\mathbf{E}+\mathbf{v}\times\mathbf{B})\cdot d\mathbf{l} = -d\Psi/dt$ for any loop; $I = \mathcal{E}/R$; KVL: drop $RI$ = rise $-d\Psi/dt$.
- Lenz: induced current opposes the flux change. Causes: $\mathbf{B}(t)$; moving/rotating/stretching $C$; $C$ moving through nonuniform $\mathbf{B}$.
- Moving bar: emf $vB\ell$, a battery with internal resistance; lab $\mathbf{E}$ static, equal in bar and load.
- Voltage is path-dependent; a voltmeter reads $\int\mathbf{E}\cdot d\mathbf{l}$ along its own leads; readings differ by the emf of the lead loop.

Topic pages: [[concepts/faradays-law]] · [[concepts/electromotive-force]] · [[concepts/motional-emf]] · [[concepts/magnetic-flux]] · [[concepts/conservative-field]].

> [!exam] On exams
> Three recurring tasks: compute an emf (orient $C$, $d\mathbf{S}$, $\Psi(t)$, differentiate, sign — [[concepts/faradays-law]]); direction only, by Lenz; bar and voltmeter — the moving conductor is a battery, meter readings are path integrals ([[concepts/motional-emf]]). Points are lost for $d\mathbf{S}$ the wrong way, forgetting the rails contribute nothing, and calling $\mathcal{E}$ a force.

> [!tip] Practice this lecture
> [[practice/14-faradays-law-and-induced-emf|12 practice problems]] — 5 easy, 3 medium, 4 hard — each with a folded hint and a worked solution. Start with [[practice/14-faradays-law-and-induced-emf#141-flux-through-a-tilted-loop|14.1 Flux through a tilted loop]]; the [[practice/index|practice hub]] has the whole bank by difficulty and by topic.

### Sources for this page
Kudeki notes, Lecture 14 (differential and integral Faraday; linked flux; moving-contour derivation in the margin; emf as work per charge; $I = G\mathcal{E}$; KVL reading; Lenz and its footnote; three causes, frame change; footnote 1 on the cause of induced $\mathbf{E}$; Examples 1–6 with all numbers). Shao, Lecture 14 slides (conservative-field recap; Lenz demos with magnet, coil, copper ring; disk-vs-bowl surfaces; shrinking-loop challenge; rails as a battery; EMF beside MMF). Slips in the course material: see [[0-toolkit/04-errata-in-the-course-materials|errata]].
