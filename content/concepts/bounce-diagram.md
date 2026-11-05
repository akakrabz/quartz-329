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
- Slides, Lecture 28 (slides 11–21; [[4-transmission-lines/28-distributed-circuits-and-bounce-diagrams#5-step-inputs-and-the-dc-limit|Lecture 28 §5]]): 100 V behind 40 Ω, $Z_0 = 60\ \Omega$, $R_L = 120\ \Omega$, $T = 1$ μs. Weights 60, 20, −4 V; at $\ell/4$, $V$ = 60, 80, 76 V and $I$ = 1, $\tfrac23$, $\tfrac35$ A from 0.25, 1.75, 2.25 μs; steady state 75 V, 0.625 A (Lecture 29 slides 3–4).
- [[problems/reading-a-line-from-two-pulses|Worked problem — Reading a line from two pulses]]: two pulses at one point reveal $R_g = Z_0$ and $\Gamma_L = -\tfrac13$; with $R_g = 25\ \Omega$ instead, $\Gamma_g = -\tfrac12$.

> [!trap]
> - $\Gamma_g$ uses $R_g$ only; the source voltage enters through $\tau_g$.
> - Current weights flip sign on backward segments. The slides label a current diagram's ends with the current coefficients under the same symbols ($\Gamma_g = \tfrac15$, $\Gamma_L = -\tfrac13$ for voltage coefficients $-\tfrac15$, $\tfrac13$).
> - $\tau_g = (1-\Gamma_g)/2$, not $1+\Gamma_g$.

> [!intuition] Three pictures from other courses
> - **At a terminal two waves count at once.** Where a wave reflects, incident and reflected arrive together, so the load voltage jumps by $(1+\Gamma_L)$ times the incident weight in one step; anywhere else each crossing adds one weight ([Valparaiso OER notes, ch. 27](https://scholar.valpo.edu/cgi/viewcontent.cgi?article=1000&context=engineering_oer&filename=27&type=additional); [BYU ECE 360](http://ece360web.groups.et.byu.net/notes/ln_bounce.pdf)).
> - **A capacitor charging in steps.** An open line ($\Gamma_L = 1$) driven by $V_0u(t)$ through $R_g$: after $n$ round trips the load sits at $V_0(1-\Gamma_g^{\,n})$. For $R_g\gg Z_0$ this staircase hugs $V_0\big(1-e^{-t/R_g\mathcal{C}\ell}\big)$, the RC charging of the line's total capacitance $\mathcal{C}\ell$, with $R_g\mathcal{C}\ell = (R_g/Z_0)\,T$ many transit times. That is why circuit theory sees only a capacitor ([MIT 6.013, Example 14.4.3](https://web.mit.edu/6.013_book/www/chapter14/14.4.html)).
> - **Time-domain reflectometry.** Launch a step and watch the input: an echo at $t_e$ marks a discontinuity at $d = vt_e/2$; a step up means a higher impedance (open-like, $\Gamma>0$), a step down a lower one (short-like). Cable-fault finders and radar work this way ([Virginia Tech ECE 3105](https://www.courses.ece.vt.edu/ece3105/chp2_lssn5.html); [TI AN-991, "lattice diagram"](https://www.ti.com/lit/an/snla043/snla043.pdf)).

**Where it appears.** [[4-transmission-lines/28-distributed-circuits-and-bounce-diagrams|Lecture 28]] (derivation, reading rules, DC limit; slides 11–23); [[4-transmission-lines/29-bounce-diagram-examples|Lecture 29]] (the notes' examples; slides' round-trip equation, steady state, pulse at the midpoint); [[4-transmission-lines/30-multi-line-circuits|Lecture 30]] (junctions between lines). Every spring/fall Exam 3 on hand and the Summer 2020 final has a bounce-diagram problem.

**Practice.** [[practice/topics#transients-on-lines-and-bounce-diagrams|Transients on lines and bounce diagrams]] (36 problems) — for example [[practice/29-bounce-diagram-examples#291-which-way-round|29.1 Which way round]] (easy), [[practice/29-bounce-diagram-examples#296-both-ends-of-a-short-line|29.6 Both ends of a short line]] (medium), [[practice/29-bounce-diagram-examples#299-one-sine-cycle-on-a-mismatched-line|29.9 One sine cycle on a mismatched line]] (hard).

Related: [[concepts/characteristic-impedance|Characteristic impedance]] · [[concepts/reflection-and-transmission|Reflection and transmission coefficients]] · [[concepts/telegraphers-equations|Telegrapher's equations]] · [[concepts/superposition|Superposition]].
