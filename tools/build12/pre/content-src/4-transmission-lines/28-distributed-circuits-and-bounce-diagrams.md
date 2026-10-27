---
title: "Lecture 28 — Distributed circuits and bounce diagrams"
description: "A transmission line between a Thévenin generator and a resistive load: the generator launches τ_g = Z₀/(R_g + Z₀) of its voltage, each end reflects voltage by Γ = (R − Z₀)/(R + Z₀), and a bounce diagram in the z–t plane adds up the echoes. A step input settles to the DC voltage divider."
tags: [lecture, transmission-lines]
lecture: 28
---

*Lecture 28 · course notes §28 (no slides) · prev: [[4-transmission-lines/27-guided-tem-waves-on-transmission-lines|Lecture 27]] · next: [[4-transmission-lines/29-bounce-diagram-examples|Lecture 29]] · worked problem: [[problems/reading-a-line-from-two-pulses|Reading a line from two pulses]] · practice: [[practice/28-bounce-diagrams|12 problems]]*

> [!abstract] In one breath
> A line ($Z_0$, speed $v$, length $\ell$) joins a Thévenin generator ($f_i$ behind $R_g$) at $z = 0$ to a resistor $R_L$ at $z = \ell$. Circuit laws hold at the two terminals; on the line, $V$ and $I$ are d'Alembert waves. The generator launches $\tau_gf_i$, with $\tau_g = Z_0/(R_g+Z_0)$. Each end reflects voltage by $\Gamma = (R-Z_0)/(R+Z_0)$ and current by $-\Gamma$. A bounce diagram tracks every echo in the $z$–$t$ plane with its weight. $V(z,t)$ is the weighted sum of delayed copies of $f_i$. A step input settles to the DC divider $R_L/(R_g+R_L)$.

## 1. The circuit and the conventions

The notes' problem: a line of characteristic impedance $Z_0$ and speed $v$ runs from $z = 0$ to $z = \ell$ ($v = 1/\sqrt{\mathcal{L}\mathcal{C}}$ and $Z_0 = \sqrt{\mathcal{L}/\mathcal{C}}$ from [[4-transmission-lines/27-guided-tem-waves-on-transmission-lines|Lecture 27]]; $\mathcal{L}$, $\mathcal{C}$ of real lines in [[2-magnetostatics/15-inductance-magnetic-energy-and-the-potentials|Lecture 15]] §5). A Thévenin source drives it at $z = 0$: open-circuit voltage $f_i(t)$, resistance $R_g$ (for example a receiving antenna). A resistor $R_L$ terminates it at $z = \ell$ (a receiver). With $f_i(t) = 0$ for $t<0$, find $V(z,t)$ and $I(z,t)$ for $t>0$.

The method: ordinary circuit laws at the element terminals, d'Alembert waves on the line.

<!-- fig:bounce-circuit -->

> [!key] Conventions (Lectures 28–30)
> - $z = 0$ is the generator end, $z = \ell$ the load end; $+z$ points toward the load. One-way delay $T = \ell/v$.
> - $V(z,t)$ is wire 2 (upper) relative to wire 1. $I(z,t)$ flows along $+z$ on wire 2 and returns on wire 1.
> - On the line, the d'Alembert pair of [[3-maxwell-and-waves/18-the-wave-equation-and-plane-tem-waves#4-the-1d-wave-equation-and-its-solutions|Lecture 18 §4]], now for $V$ and $I$:
> $$
> \begin{gathered}
> V(z,t) = f\Big(t-\frac zv\Big) + g\Big(t+\frac zv\Big),\\[4pt]
> I(z,t) = \frac{1}{Z_0}\Big[f\Big(t-\frac zv\Big) - g\Big(t+\frac zv\Big)\Big].
> \end{gathered}
> $$
> A forward wave carries $I = +V/Z_0$, a backward wave $I = -V/Z_0$.
> - $\Gamma_L$, $\Gamma_g$: reflected over incident **voltage**, at the load and at the generator. For current the ratio is $-\Gamma$.
> - $\tau_g$: launched forward voltage over the generator's open-circuit voltage.
> - Bounce diagram: $z$ across (generator on the left), $t$ downward, each segment labelled with its voltage weight.

Notation: the notes write $Z_o$ and use both $l$ and $\ell$; $T$ is the site's shorthand for their $\ell/v$.

## 2. The load reflection coefficient

At $z = \ell$ the resistor fixes $V/I$ (the notes' $V_L/I_L$, load voltage over load current):

$$
\frac{V(\ell,t)}{I(\ell,t)} = Z_0\,\frac{f(t-T)+g(t+T)}{f(t-T)-g(t+T)} = R_L .
$$

Solve for $g$, then replace $t$ by $t-T$:

> [!key] Load reflection coefficient
> $$
> \begin{gathered}
> g(t+T) = \Gamma_L\,f(t-T),\\[4pt]
> g(t) = \Gamma_L\,f(t-2T),\\[4pt]
> \Gamma_L = \frac{R_L-Z_0}{R_L+Z_0},\\[8pt]
> V(z,t) = f\Big(t-\frac zv\Big) + \Gamma_Lf\Big(t+\frac zv-2T\Big),\\[4pt]
> I(z,t) = \frac{1}{Z_0}\Big[f\Big(t-\frac zv\Big)\\[2pt]
> -\ \Gamma_Lf\Big(t+\frac zv-2T\Big)\Big].
> \end{gathered}
> $$
> The backward wave is the forward one scaled by $\Gamma_L$ and delayed by the round trip $2(\ell-z)/v$ from $z$ to the load and back.

This is [[3-maxwell-and-waves/25-wave-reflection-and-transmission|Lecture 25]]'s $\Gamma = (\eta_2-\eta_1)/(\eta_2+\eta_1)$, with $Z_0$ for the incident side's $\eta_1$ and $R_L$ for $\eta_2$. The reflected current carries $-\Gamma_L$, as the reflected $\mathbf{H}$ carries $-\Gamma$.

## 3. The generator: injection and reflection

KVL around the source loop at $z = 0$, with §2's $V$ and $I$:

$$
\begin{gathered}
f_i(t) = R_g\,I(0,t) + V(0,t)\\[4pt]
= \frac{R_g}{Z_0}\big[f(t)-\Gamma_Lf(t-2T)\big]\\[4pt]
+\ f(t) + \Gamma_Lf(t-2T).
\end{gathered}
$$

**First epoch, $0<t<2T$.** Nothing has come back yet: $f(t-2T) = 0$. Then $f_i = (1+R_g/Z_0)f$, so

$$
f(t) = \tau_g\,f_i(t),\qquad \tau_g = \frac{Z_0}{R_g+Z_0}.
$$

$\tau_g$ is the **injection coefficient**. It is a voltage divider: until the first echo returns, the line looks like a resistor $Z_0$ (the notes' footnote).

**Later epochs.** Regroup the KVL as

$$
f_i(t) = \Big(1+\frac{R_g}{Z_0}\Big)f(t) + \Big(1-\frac{R_g}{Z_0}\Big)\Gamma_Lf(t-2T),
$$

where $f(t-2T)$ is already known from the epoch before. Solve for $f(t)$:

> [!key] Injection and generator reflection
> $$
> \begin{gathered}
> f(t) = \tau_g\,f_i(t) + \Gamma_g\Gamma_L\,f(t-2T),\\[6pt]
> \tau_g = \frac{Z_0}{R_g+Z_0},\qquad \Gamma_g = \frac{R_g-Z_0}{R_g+Z_0}.
> \end{gathered}
> $$
> The wave leaving $z = 0$ is the fresh injection plus the returning wave reflected with $\Gamma_g$, the **source reflection coefficient**. $\Gamma_g$ is $\Gamma_L$ with $R_L$ replaced by $R_g$: the same process at the other end. Also $\tau_g = (1-\Gamma_g)/2$.

The notes do this one epoch at a time with $f_i = \delta(t)$: for $2T<t<4T$, $f(t) = \tau_g\delta(t) + \Gamma_g\Gamma_L\tau_g\delta(t-2T)$. The recursion above covers every epoch at once.

> [!intuition] Why the generator reflects through its resistance alone
> By superposition, the source's own output is already the injected $\tau_gf_i$. A returning wave therefore sees the ideal source as a short, leaving $R_g$ alone (Rao §7.4).

## 4. Impulse response and the bounce diagram

With $f_i = \delta(t)$, $V(z,t)$ is the **impulse response**, which the notes call $h_z(t)$. Iterating the recursion gives $f(t) = \tau_g\sum_n(\Gamma_L\Gamma_g)^n\delta(t-2nT)$, and §2 then gives:

> [!key] Impulse response
> $$
> \begin{gathered}
> V(z,t) = \tau_g\sum_{n=0}^{\infty}(\Gamma_L\Gamma_g)^n\Big[\delta\Big(t-\frac zv-2nT\Big)\\[2pt]
> +\ \Gamma_L\,\delta\Big(t+\frac zv-2(n+1)T\Big)\Big],\\[10pt]
> I(z,t) = \frac{\tau_g}{Z_0}\sum_{n=0}^{\infty}(\Gamma_L\Gamma_g)^n\Big[\delta\Big(t-\frac zv-2nT\Big)\\[2pt]
> -\ \Gamma_L\,\delta\Big(t+\frac zv-2(n+1)T\Big)\Big].
> \end{gathered}
> $$

Terms shrink as $(\Gamma_L\Gamma_g)^n$. Passive resistors give $\lvert\Gamma\rvert\le1$, so usually only the first few terms matter. They decay slowly if $\lvert\Gamma_L\Gamma_g\rvert$ is near 1, and never if both ends reflect totally ($\lvert\Gamma_L\Gamma_g\rvert = 1$, a lossless resonant circuit: Lecture 31).

The bounce diagram draws these terms instead of writing them out.

<!-- fig:bounce-diagram -->

- One slanted segment per travelling impulse. It crosses the line in time $T$, its lifetime.
- Weights: $\tau_g$ on the first segment, then $\times\Gamma_L$ at each load reflection and $\times\Gamma_g$ at each generator reflection.
- Forward segment $n$, weight $\tau_g(\Gamma_L\Gamma_g)^n$, passes $z$ at $t = z/v+2nT$. Backward segment $n$, weight $\tau_g\Gamma_L(\Gamma_L\Gamma_g)^n$, passes $z$ at $t = 2T-z/v+2nT$.

> [!recipe] Reading V and I off a bounce diagram
> 1. Draw a vertical line at the observation point $z_p$.
> 2. Each crossing is one impulse of $V(z_p,t)$, at the crossing time, with the segment's weight.
> 3. $I(z_p,t)$: the same impulses divided by $Z_0$, with the sign flipped on backward segments.
> 4. Any other input: replace each $\delta(t-t_k)$ by $f_i(t-t_k)$, since $\delta(t-t_k)*f_i(t) = f_i(t-t_k)$. For a step $V_0u(t)$, $V(z_p,t)$ is $V_0$ times the running sum of the weights crossed so far.
> 5. At an end, the arriving segment and its reflection cross together: add both, e.g. $(1+\Gamma_L)w$ at the load.

> [!example] Example — reading one point (this site's numbers)
> $Z_0 = 60\ \Omega$, $R_g = 180\ \Omega$, $R_L = 20\ \Omega$: $\tau_g = \tfrac14$, $\Gamma_g = \tfrac12$, $\Gamma_L = -\tfrac12$. Weights: $\tfrac14$, $-\tfrac18$, $-\tfrac1{16}$, $\tfrac1{32}$, … At $z = \ell/2$:
> $$
> \begin{gathered}
> h_{\ell/2}(t) = \tfrac14\delta(t-\tfrac T2) - \tfrac18\delta(t-\tfrac{3T}2)\\
> - \tfrac1{16}\delta(t-\tfrac{5T}2) + \tfrac1{32}\delta(t-\tfrac{7T}2) + \ldots,\\[6pt]
> Z_0I\big(\tfrac\ell2,t\big) = \tfrac14\delta(t-\tfrac T2) + \tfrac18\delta(t-\tfrac{3T}2)\\
> - \tfrac1{16}\delta(t-\tfrac{5T}2) - \tfrac1{32}\delta(t-\tfrac{7T}2) + \ldots
> \end{gathered}
> $$
> The second and fourth impulses travel backward, so their current signs flip.

## 5. Step inputs and the DC limit

For $f_i = V_0u(t)$ each crossing adds a step, so $V(z,t)$ is a staircase. As $t\to\infty$, sum the geometric series ($\lvert\Gamma_L\Gamma_g\rvert<1$):

> [!key] DC limit of a step response (this site's derivation)
> $$
> \begin{gathered}
> V(z,\infty) = V_0\,\tau_g\,\frac{1+\Gamma_L}{1-\Gamma_L\Gamma_g} = V_0\,\frac{R_L}{R_g+R_L},\\[8pt]
> I(z,\infty) = \frac{V_0}{Z_0}\,\tau_g\,\frac{1-\Gamma_L}{1-\Gamma_L\Gamma_g} = \frac{V_0}{R_g+R_L},
> \end{gathered}
> $$
> the same at every $z$. In DC the line is just two wires, and the circuit is the lumped divider. The notes reach this by example in [[4-transmission-lines/29-bounce-diagram-examples|Lecture 29]]. Use it to check any step-driven diagram.

> [!derivation]- The algebra
> $$
> \begin{gathered}
> 1-\Gamma_L\Gamma_g = \frac{(R_L+Z_0)(R_g+Z_0)-(R_L-Z_0)(R_g-Z_0)}{(R_L+Z_0)(R_g+Z_0)}\\[6pt]
> = \frac{2Z_0(R_L+R_g)}{(R_L+Z_0)(R_g+Z_0)},\\[8pt]
> \tau_g(1+\Gamma_L) = \frac{2Z_0R_L}{(R_g+Z_0)(R_L+Z_0)},\\[6pt]
> \tau_g(1-\Gamma_L) = \frac{2Z_0^2}{(R_g+Z_0)(R_L+Z_0)}.
> \end{gathered}
> $$
> Divide the last two lines by the first.

> [!example] Example — the same circuit, 12 V step (this site's numbers)
> - First wave: $12\tau_g = 3$ V. Weights $3$, $-1.5$, $-0.75$, $0.375$, … V.
> - Load, $(1+\Gamma_L)\times$ each arrival: $V(\ell,t) = 1.5$ V on $(T,3T)$, $1.125$ V on $(3T,5T)$, then $1.219$, $1.195$, …
> - Midpoint: $3$, $1.5$, $0.75$, $1.125$, $1.3125$, … V, one step per $T$ from $T/2$.
> - DC: $12\cdot\tfrac{20}{180+20} = 1.2$ V, and $I = 12/200 = 60$ mA.
> - $\Gamma_L\Gamma_g = -\tfrac14<0$, so the staircase overshoots and undershoots on its way.

<!-- fig:bounce-step -->

The DC shortcut needs an input that settles to a constant. A switched-on sine does not settle (Lecture 29; Lecture 31).

## 6. Special terminations

Rao §7.4 lists the load cases; the notes use $\Gamma_g = 0$ and $\Gamma_g = -1$ in Lecture 29.

| end | resistor | coefficients | on the line |
|---|---|---|---|
| matched load | $R_L = Z_0$ | $\Gamma_L = 0$ | no echo: the line looks infinitely long |
| open load | $R_L\to\infty$ | $\Gamma_L = +1$ | $I(\ell,t) = 0$; $V(\ell,t)$ is twice the arriving voltage |
| shorted load | $R_L = 0$ | $\Gamma_L = -1$ | $V(\ell,t) = 0$; $I(\ell,t)$ is twice the arriving current |
| matched generator | $R_g = Z_0$ | $\Gamma_g = 0$, $\tau_g = \tfrac12$ | echoes are absorbed at $z = 0$; the diagram ends at $t = 2T$ |
| ideal source | $R_g = 0$ | $\Gamma_g = -1$, $\tau_g = 1$ | $V(0,t) = f_i(t)$ at all times |

> [!trap] Bounce-diagram traps
> - $\Gamma_g$ uses $R_g$ alone; the source voltage enters only through $\tau_g$.
> - $\tau_g = Z_0/(R_g+Z_0)$ is not Lecture 25's $\tau = 1+\Gamma$; here $\tau_g = (1-\Gamma_g)/2$.
> - Backward waves carry $I = -V/Z_0$; a current diagram uses $-\Gamma_L$ and $-\Gamma_g$.
> - $V/I = Z_0$ holds for a single forward wave, not for the total $V/I$ (unless nothing reflects).

## 7. Summary

- Circuit laws at the terminals, d'Alembert waves in between. Forward: $I = V/Z_0$; backward: $I = -V/Z_0$.
- Load: $g(t) = \Gamma_Lf(t-2T)$, $\Gamma_L = (R_L-Z_0)/(R_L+Z_0)$. Generator: $f(t) = \tau_gf_i(t) + \Gamma_g\Gamma_Lf(t-2T)$, with $\tau_g = Z_0/(R_g+Z_0)$ and $\Gamma_g = (R_g-Z_0)/(R_g+Z_0)$.
- Bounce diagram: $z$ across, $t$ down; weights $\tau_g$, then $\times\Gamma_L$ and $\times\Gamma_g$ at the ends. Read $V$ at $z_p$ from the crossings of a vertical line; current flips sign on backward segments.
- Any input: weighted, delayed copies of $f_i$. Step input: staircase to $V_0R_L/(R_g+R_L)$ and $V_0/(R_g+R_L)$.
- Next, [[4-transmission-lines/29-bounce-diagram-examples|Lecture 29]]: the notes' worked examples.

Concept pages: [[concepts/bounce-diagram]] · [[concepts/characteristic-impedance]] · [[concepts/telegraphers-equations]] · [[concepts/reflection-and-transmission]] · [[concepts/superposition]].

> [!exam] On exams
> Every spring/fall Exam 3 on hand (SP17–FA23) and the Summer 2020 final has a bounce-diagram problem; Lecture 29 covers the plotting parts. Lecture 28 parts:
> - $\tau_g$, $\Gamma_g$, $\Gamma_L$ from the resistors (SP17 E3 #5a, SP18 E3 #3a, FA23 E3 #3(a)(i)); SP19 E3 #4c–d also asks for the current coefficients, $-\Gamma$.
> - A labelled diagram over a time window (SP17 #5b, SP18 #3b, S20 FE #5a): arrival times, then multiply at each end.
> - Steady state under a step (FA23 #5a–b, SP19 #4g, S20 FE #5d): the DC divider.
> - Inverse problems: $R_g$, $R_L$, $v$ from pulses seen at one point (SP17 #2(v)–(vi), FA23 #4). See the worked problem.

> [!tip] Practice this lecture
> [[practice/28-bounce-diagrams|12 practice problems]] — 5 easy, 3 medium, 4 hard — each with a folded hint and a worked solution. Start with [[practice/28-bounce-diagrams#281-three-coefficients|28.1 Three coefficients]]; the [[practice/index|practice hub]] has the whole bank by difficulty and by topic.

### Sources for this page
Kudeki notes, Lecture 28 (8 pages): the circuit, the load condition and $\Gamma_L$, the KVL at $z = 0$ with $\tau_g$ and its footnote, the two-epoch impulse response, $\Gamma_g$, the bounce diagram, the series and the convolution remark. Rao (2009) §7.4 for cross-checks. This site's own: the conventions box, the all-epoch recursion, $\tau_g = (1-\Gamma_g)/2$, the reading recipe, the DC-limit proof, the terminations table, the examples and figures; numbers checked by an FDTD simulation. One slip in the notes (the sign of a delay, p. 8) is on the errata page.
