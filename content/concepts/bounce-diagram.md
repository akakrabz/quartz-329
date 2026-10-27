---
title: "Bounce diagram"
description: "A z–t chart of the waves bouncing on a line between a Thévenin generator and a resistive load: the first wave carries τ_g = Z₀/(R_g + Z₀) of the input, and each end multiplies it by Γ = (R − Z₀)/(R + Z₀). V and I at any point are read off a vertical line."
tags: [concept, transmission-lines]
aliases: ["bounce diagrams", "injection coefficient", "load reflection coefficient", "source reflection coefficient", "lattice diagram"]
---

> [!key] Definition
> A chart with $z$ across (generator at $z = 0$ on the left, load at $z = \ell$) and time $t$ downward. Each travelling wave is a slanted segment crossing the line in $T = \ell/v$, labelled with its voltage weight:
> $$
> \begin{gathered}
> \tau_g = \frac{Z_0}{R_g+Z_0},\qquad \Gamma_g = \frac{R_g-Z_0}{R_g+Z_0},\\[6pt]
> \Gamma_L = \frac{R_L-Z_0}{R_L+Z_0}.
> \end{gathered}
> $$
> The first weight is $\tau_g$. It is multiplied by $\Gamma_L$ at each load reflection and by $\Gamma_g$ at each generator reflection.

**Physics.** Circuit laws hold at the terminals; d'Alembert waves travel in between ([[4-transmission-lines/28-distributed-circuits-and-bounce-diagrams|Lecture 28]]). The load forces $V/I = R_L$, which needs a reflected wave $\Gamma_L$ times the incident one. KVL at the generator launches $\tau_gf_i$, a voltage divider with the line acting as a resistor $Z_0$. A returning wave sees the ideal source as a short, so it reflects with $\Gamma_g$, which contains $R_g$ alone. Both $\Gamma$'s are [[3-maxwell-and-waves/25-wave-reflection-and-transmission|Lecture 25]]'s $\Gamma$ with $Z_0$ in place of $\eta_1$. The reflected current carries $-\Gamma$.

**Reading it.**
- $V(z_p,t)$: draw a vertical line at $z_p$. Each crossing contributes a copy of $f_i$ delayed to the crossing time and scaled by the segment's weight.
- Crossing times: $z_p/v+2nT$ for forward segments, $2T-z_p/v+2nT$ for backward ones.
- $I(z_p,t)$: the same over $Z_0$, with the sign flipped on backward segments.
- Step input $V_0u(t)$: a staircase, the running sum of the weights crossed. It settles to the DC divider, $V_0R_L/(R_g+R_L)$ and $V_0/(R_g+R_L)$, at every $z$.

**Limits.**
- Matched load ($\Gamma_L = 0$): one segment, no echo.
- Matched generator ($\Gamma_g = 0$, $\tau_g = \tfrac12$): the diagram ends when the first echo returns, at $2T$.
- Ideal source and an open or shorted load ($\lvert\Gamma_L\Gamma_g\rvert = 1$): the echoes never decay (Lecture 31).

**Examples.**
- $Z_0 = 60\ \Omega$, $R_g = 180\ \Omega$, $R_L = 20\ \Omega$, 12 V step: weights 3, $-1.5$, $-0.75$, … V, settling to 1.2 V ([[4-transmission-lines/28-distributed-circuits-and-bounce-diagrams|Lecture 28]] §5).
- [[problems/reading-a-line-from-two-pulses|Worked problem — Reading a line from two pulses]]: two pulses at one point reveal $R_g = Z_0$ and $\Gamma_L = -\tfrac13$; with $R_g = 25\ \Omega$ instead, $\Gamma_g = -\tfrac12$.

> [!trap]
> - $\Gamma_g$ uses $R_g$ only; the source voltage enters through $\tau_g$.
> - Current weights flip sign on backward segments.
> - $\tau_g = (1-\Gamma_g)/2$, not $1+\Gamma_g$.

**Where it appears.** [[4-transmission-lines/28-distributed-circuits-and-bounce-diagrams|Lecture 28]] (derivation, reading rules, DC limit); [[4-transmission-lines/29-bounce-diagram-examples|Lecture 29]] (the notes' examples); [[4-transmission-lines/30-multi-line-circuits|Lecture 30]] (junctions between lines). Every spring/fall Exam 3 on hand and the Summer 2020 final has a bounce-diagram problem.

**Practice.** [[practice/topics#transients-on-lines-and-bounce-diagrams|Transients on lines and bounce diagrams]] (36 problems) — for example [[practice/29-bounce-diagram-examples#291-which-way-round|29.1 Which way round]] (easy), [[practice/29-bounce-diagram-examples#296-both-ends-of-a-short-line|29.6 Both ends of a short line]] (medium), [[practice/29-bounce-diagram-examples#299-one-sine-cycle-on-a-mismatched-line|29.9 One sine cycle on a mismatched line]] (hard).

Related: [[concepts/characteristic-impedance|Characteristic impedance]] · [[concepts/reflection-and-transmission|Reflection and transmission coefficients]] · [[concepts/telegraphers-equations|Telegrapher's equations]] · [[concepts/superposition|Superposition]].
