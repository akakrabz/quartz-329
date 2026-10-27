---
title: "Lecture 30 — Multi-line circuits"
description: "Where two lines of different Z₀ meet, an arriving wave splits into a reflected part Γ = (Z_k − Z_j)/(Z_k + Z_j) and a transmitted part τ = 1 + Γ. Bounce diagrams then span several lines, and resistors at a junction enter through the impedance the wave sees."
tags: [lecture, transmission-lines]
lecture: 30
---

*Lecture 30 · course notes §30 (no slides) · prev: [[4-transmission-lines/29-bounce-diagram-examples|Lecture 29]] · next: Lecture 31, periodic oscillations in lossless TL circuits (coming) · worked problem: [[problems/echoes-trapped-on-the-second-line|Echoes trapped on the second line]] · practice: [[practice/30-multi-line-circuits|12 problems]]*

> [!abstract] In one breath
> Two lines joined end to end form a junction. A wave arriving on line $j$ sees line $k$ as a resistor $Z_k$, until an echo comes back from beyond it. Continuity of $V$ and $I$ splits the wave: $\Gamma_{jk} = (Z_k-Z_j)/(Z_k+Z_j)$ travels back and $\tau_{jk} = 1+\Gamma_{jk}$ travels on. A bounce diagram now spans several lines, each with its own slope, and every arrival at a junction spawns two impulses. Resistors at a junction enter through the impedance the wave sees; a series resistor breaks $\tau = 1+\Gamma$.

## 1. A junction between two lines

Line $j$ (impedance $Z_j$, speed $v_j$) meets line $k$ ($Z_k$, $v_k$) at one point. A voltage wave $V^+$ arriving on line $j$ launches a reflected wave $V^-$ back along line $j$ and a transmitted wave $V^{++}$ along line $k$ (the notes' names). Each wave carries the current $\pm V/Z_0$ of its own line, minus for the one travelling toward $-z$ ([[4-transmission-lines/28-distributed-circuits-and-bounce-diagrams|Lecture 28]]). The junction has no length, so the total $V$ and $I$ are the same on both sides.

> [!key] Junction coefficients
> $$
> \begin{gathered}
> V:\quad V^+ + V^- = V^{++},\\[4pt]
> I:\quad \frac{V^+ - V^-}{Z_j} = \frac{V^{++}}{Z_k},\\[8pt]
> \Gamma_{jk} \equiv \frac{V^-}{V^+} = \frac{Z_k-Z_j}{Z_k+Z_j},\\[6pt]
> \tau_{jk} \equiv \frac{V^{++}}{V^+} = 1+\Gamma_{jk} = \frac{2Z_k}{Z_k+Z_j}.
> \end{gathered}
> $$
> $Z_j$ belongs to the line that brings the wave, $Z_k$ to the line it enters. Put $\tau_{jk} = 1+\Gamma_{jk}$ into the current equation and solve.

This is [[3-maxwell-and-waves/25-wave-reflection-and-transmission|Lecture 25]]'s plane-wave $\Gamma$ with $\eta\to Z_0$: tangential $\mathbf{E}$ and $\mathbf{H}$ there, $V$ and $I$ here. It is also Lecture 28's $\Gamma_L$ with $R_L\to Z_k$, because line $k$ carries only the outgoing wave at first.

What the formulas say:
- Speeds do not enter $\Gamma$ or $\tau$; they only set the timing.
- Going back through the same junction: $\Gamma_{kj} = -\Gamma_{jk}$ and $\tau_{kj} = 1+\Gamma_{kj} = 1-\Gamma_{jk}$.
- Current ratios: reflected over incident current is $-\Gamma_{jk}$; transmitted over incident is $1-\Gamma_{jk} = \tau_{jk}Z_j/Z_k$.
- Power ratios: $\Gamma_{jk}^2$ reflects and $\tau_{jk}^2Z_j/Z_k = 1-\Gamma_{jk}^2$ is transmitted. So $\tau>1$ (for $Z_k>Z_j$) is not a gain.
- $Z_k = Z_j$: no reflection, whatever the speeds.

> [!trap] Junction coefficients
> - $\Gamma_{jk}$ is "far side minus arriving side": the subscripts follow the wave.
> - An echo returning from line $k$ uses $\Gamma_{kj}$ and $\tau_{kj}$, not $\Gamma_{jk}$ and $\tau_{jk}$.
> - "Current reflection coefficient" means $-\Gamma_{jk}$, and the current transmission coefficient is $1-\Gamma_{jk}$.
> - $Z_k$ is line $k$'s $Z_0$, not the load at its far end.
> - $\tau = 1+\Gamma$ holds at a junction (not with a series resistor, §4), never for injection: $\tau_g = Z_0/(R_g+Z_0)$.

## 2. A bounce diagram across two lines

The notes' circuit: a source $f_i(t)$ with $R_g = 2Z_1$ drives line 1 ($Z_1$, $v_1$) from $z = 0$ to $\ell/2$. Line 2 ($Z_2 = 2Z_1$, $v_2 = 2v_1$) runs from $\ell/2$ to $\ell$ and ends in $R_L = Z_2$. The one-way delays are $T_1 = (\ell/2)/v_1$ and $T_2 = (\ell/2)/v_2 = T_1/2$: Lecture 28's $T$, one per line. The generator sees line 1, so $\tau_g$ and $\Gamma_g$ use $Z_1$; the load sees line 2. Notation: the notes write $Z_o$, $l$, and $f(t)$ for the source; this page follows Lecture 28 with $Z_0$, $\ell$ and $f_i(t)$.

$$
\begin{gathered}
\tau_g = \frac{Z_1}{R_g+Z_1} = \frac13,\qquad \Gamma_g = \frac{R_g-Z_1}{R_g+Z_1} = \frac13,\\[6pt]
\Gamma_{12} = \frac{2Z_1-Z_1}{2Z_1+Z_1} = \frac13,\qquad \tau_{12} = \frac43,\qquad \Gamma_L = 0.
\end{gathered}
$$

<!-- fig:mline-bounce -->

How the diagram grows:
- Each travelling impulse is a slanted segment with slope $1/v$. Line 2 takes $T_2$, half of line 1's $T_1$, so its segments are flatter.
- An arrival at an end spawns one impulse ($\times\Gamma_g$ or $\times\Gamma_L$); an arrival at the junction spawns two ($\times\Gamma_{12}$ back, $\times\tau_{12}$ on).
- Weights multiply along each path: $\tfrac13$, then $\tfrac19$ and $\tfrac49$, then $\tfrac1{27}$, then $\tfrac1{81}$ and $\tfrac4{81}$.
- $\Gamma_L = 0$, so nothing returns from line 2 and $\Gamma_{21} = -\tfrac13$, $\tau_{21} = \tfrac23$ are never used. Each round trip on line 1 multiplies by $\Gamma_{12}\Gamma_g = \tfrac19$.

DC check with $f_i = u(t)$: the weights reaching line 2 sum to $\tfrac49/(1-\tfrac19) = \tfrac12$. On line 1 the forward ones sum to $\tfrac38$ and the backward ones to $\tfrac18$, again $\tfrac12$ in total. Lecture 28's DC divider gives $R_L/(R_g+R_L) = \tfrac12$: at DC both lines are just wires.

> [!example] Example 1 (notes) — the line parameters of line 2
> Line 2 has $Z_2 = 2Z_1$ and $v_2 = 2v_1$. With $Z_0 = \sqrt{\mathcal{L}/\mathcal{C}}$ and $v = 1/\sqrt{\mathcal{L}\mathcal{C}}$ ([[4-transmission-lines/27-guided-tem-waves-on-transmission-lines|Lecture 27]]):
> $$
> \frac{\mathcal{L}_2}{\mathcal{C}_2} = 4\frac{\mathcal{L}_1}{\mathcal{C}_1},\qquad \frac{1}{\mathcal{L}_2\mathcal{C}_2} = \frac{4}{\mathcal{L}_1\mathcal{C}_1}.
> $$
> The product gives $\mathcal{C}_2^2 = \mathcal{C}_1^2/16$, so $\mathcal{C}_2 = \mathcal{C}_1/4$; the ratio gives $\mathcal{L}_2 = \mathcal{L}_1$. One way to build it (this site's): the same conductors throughout, with a non-magnetic $\epsilon_r = 4$ filling on line 1 and air on line 2. $\mathcal{L}\propto\mu$ stays put and $\mathcal{C}\propto\epsilon$ drops by 4 ([[2-magnetostatics/15-inductance-magnetic-energy-and-the-potentials|Lecture 15]] §5).

> [!recipe] A multi-line bounce diagram
> 1. $\tau_g$, $\Gamma_g$ with the first line's $Z_0$; $\Gamma_L$ with the last line's.
> 2. At every junction, both directions: $\Gamma_{jk}$, $\tau_{jk}$ and $\Gamma_{kj}$, $\tau_{kj}$.
> 3. One-way time of each line, length over speed. Draw $z$ across and $t$ down, each line with its own slope.
> 4. Launch $\tau_gf_i$. At each arrival multiply by the coefficient there; at a junction draw both offspring.
> 5. Impulses that meet at the same place and time add.
> 6. $V(z,t)$: a segment of weight $w$ crossing $z$ at $t_k$ adds $w\,f_i(t-t_k)$; for a step, add the weights crossed by time $t$. For $I$, divide each weight by its own line's $Z_0$, with a minus for leftward segments.
> 7. For a step source, check $t\to\infty$ against the lumped circuit.

## 3. The impulse response and a sinusoidal burst

Read off the diagram with $f_i = \delta(t)$; a round trip on line 1 takes $2T_1 = \ell/v_1$:

> [!key] Impulse response of the notes' circuit
> For $z<\ell/2$:
> $$
> \begin{aligned}
> V &= \frac13\sum_{n=0}^{\infty}\frac{\delta(t-z/v_1-2nT_1)}{9^n}\\
> &\quad+\frac19\sum_{n=0}^{\infty}\frac{\delta(t+z/v_1-2(n+1)T_1)}{9^n}.
> \end{aligned}
> $$
> For $\ell/2<z<\ell$:
> $$
> \begin{gathered}
> V = \frac49\sum_{n=0}^{\infty}\frac{\delta(t-t_z-2nT_1)}{9^n},\\[4pt]
> t_z = T_1+\frac{z-\ell/2}{v_2}.
> \end{gathered}
> $$
> $I$: the same terms over $Z_1$ for $z<\ell/2$, with the second sum subtracted; over $Z_2$ for $z>\ell/2$.

The first sum is the forward impulse after $n$ round trips, the second its echo from the junction. On line 2, $t_z$ is the first arrival at $z$: $T_1$ to reach the junction, then $(z-\ell/2)/v_2$. The notes write $t_z+2nT_1$ as $z/v_2+(4n+1)(\ell/2)/v_2$; the two agree because $T_1 = 2T_2$.

> [!example] Example 2 (notes) — a switched-on sine
> $f_i(t) = \sin(2\pi t)\,u(t)$ with $t$ in μs (1 MHz), $\ell = 2400$ m, $v_1 = 150$ m/μs and $Z_1 = 25\ \Omega$ (so $Z_2 = 50\ \Omega$). Then $T_1 = 8$ μs, $T_2 = 4$ μs, and a round trip on line 1 takes $2T_1 = 16$ μs. Each $\delta(t-t_0)$ above becomes $f_i(t-t_0)$, a delayed copy of the input (Lecture 28's convolution). The current divides each term by 25 Ω or 50 Ω.

<!-- fig:mline-burst -->

Reading the snapshots:
- The wavelength is $v/f$: 150 m on line 1, 300 m on line 2.
- At $t = 12$ μs line 2 carries amplitude $\tfrac49$. On line 1 the $\tfrac19$ echo overlaps the $\tfrac13$ wave between 600 and 1200 m.
- $2T_1 = 16$ μs is a whole number of periods, so every contribution on line 2 arrives in phase. The amplitude there tends to $\tfrac49/(1-\tfrac19) = \tfrac12$.
- On line 1 the forward and backward totals tend to $\tfrac38$ and $\tfrac18$. Their sum has a snapshot amplitude between $\tfrac14$ and $\tfrac12$, depending on the instant. The notes' margin plot is such a late snapshot; Lecture 31 studies this periodic state.

## 4. Resistors at a junction

**Shunt resistor (Example 3, notes).** A resistor $R$ across the junction leaves KVL unchanged and adds its current to KCL:

$$
\begin{gathered}
V^+ + V^- = V^{++},\\[4pt]
\frac{V^+-V^-}{Z_1} = \frac{V^{++}}{R}+\frac{V^{++}}{Z_2}.
\end{gathered}
$$

> [!key] Shunt resistor at a junction
> $$
> \begin{gathered}
> Z_{eq} = \frac{RZ_2}{R+Z_2},\qquad \Gamma_{12} = \frac{Z_{eq}-Z_1}{Z_{eq}+Z_1},\\[6pt]
> \tau_{12} = 1+\Gamma_{12} = \frac{2Z_{eq}}{Z_{eq}+Z_1}.
> \end{gathered}
> $$
> From the right, by symmetry: $Z_{eq} = RZ_1/(R+Z_1)$ in $\Gamma_{21} = (Z_{eq}-Z_2)/(Z_{eq}+Z_2)$, and $\tau_{21} = 1+\Gamma_{21}$.

- $R\to\infty$ recovers §1; $R\to0$ shorts the junction, $\Gamma_{12} = -1$ and $\tau_{12} = 0$.
- Any lines and resistors in parallel at one node: $Z_{eq}$ is their parallel combination, each outgoing line counted as its $Z_0$. Three equal lines meeting give $Z_{eq} = Z_0/2$, $\Gamma = -\tfrac13$ and $\tau = \tfrac23$ into each branch.

**Series resistor (the notes' exercise).** With $R$ in one wire between the lines, the arriving wave sees $R+Z_2$. The junction voltage $(1+\Gamma_{12})V^+$ then divides between $R$ and line 2.

> [!key] Series resistor at a junction
> $$
> \begin{gathered}
> \Gamma_{12} = \frac{(R+Z_2)-Z_1}{(R+Z_2)+Z_1},\\[6pt]
> \tau_{12} = (1+\Gamma_{12})\frac{Z_2}{R+Z_2} = \frac{2Z_2}{R+Z_1+Z_2}.
> \end{gathered}
> $$

<!-- fig:mline-junctions -->

The rule behind all three: $\Gamma$ uses the resistance the arriving wave sees; $\tau$ is the voltage that ends up across line $k$'s terminals, per volt of $V^+$.

> [!example] Example — matching with a shunt resistor (this site's numbers)
> $Z_1 = 25\ \Omega$, $Z_2 = 50\ \Omega$, $R = 50\ \Omega$. Then $Z_{eq} = 25\ \Omega = Z_1$, so $\Gamma_{12} = 0$ and $\tau_{12} = 1$: no echo. The junction voltage is $V^+$. Line 2 takes $(V^+)^2/Z_2$, half of the incident power $(V^+)^2/Z_1$, and $R$ burns the other half. The match costs 3 dB.

> [!trap] Resistive junctions
> - Series $R$: $\tau_{12}\neq1+\Gamma_{12}$. Apply the divider $Z_2/(R+Z_2)$.
> - With a resistor, $\Gamma^2$ plus the fraction of power entering line $k$ is less than 1; $R$ absorbs the rest.

## 5. Summary

- Junction: $\Gamma_{jk} = (Z_k-Z_j)/(Z_k+Z_j)$ and $\tau_{jk} = 1+\Gamma_{jk}$, from continuity of $V$ and $I$. Back through it: $\Gamma_{kj} = -\Gamma_{jk}$. Currents: $-\Gamma_{jk}$ and $1-\Gamma_{jk}$. Power: $\Gamma^2+\tau^2Z_j/Z_k = 1$.
- Multi-line bounce diagram: one slope per line; a junction arrival splits in two; weights multiply; coincident impulses add.
- Notes' circuit: $\tau_g = \Gamma_g = \Gamma_{12} = \tfrac13$, $\tau_{12} = \tfrac43$, $\Gamma_L = 0$; each line-1 round trip multiplies by $\tfrac19$; DC limit $\tfrac12$.
- Example 1: $\mathcal{L}_2 = \mathcal{L}_1$, $\mathcal{C}_2 = \mathcal{C}_1/4$. Example 2: the wavelength doubles on line 2, where the late amplitude is $\tfrac12$.
- Shunt $R$: $Z_{eq} = R\parallel Z_2$ and $\tau = 1+\Gamma$. Series $R$: $Z_{eq} = R+Z_2$ and $\tau = (1+\Gamma)Z_2/(R+Z_2)$.
- Next, Lecture 31: source-free oscillations and periodic steady state on lossless lines.

Concept pages: [[concepts/bounce-diagram]] · [[concepts/characteristic-impedance]] · [[concepts/reflection-and-transmission]] · [[concepts/telegraphers-equations]].

> [!exam] On exams
> Three Exam 3 papers have junction items. SP19 Exam 3 #4 is the notes' two-line circuit with numbers. It asks for $\Gamma_{12}$ and $\tau_{12}$ for voltage and current, the voltage bounce diagram to a given time, $V$ at one $(z,t)$ read off it, and the DC load voltage. FA23 Exam 3 #3(a) cascades three sections. It asks for $\tau_g$, a voltage and a current reflection coefficient, and the earliest return of the far junction's echo: add the one-way times out and back. SP18 Exam 3 #1(vii) asks what removes every echo toward the source: check each discontinuity downstream, the load included. No calculators; the fractions are simple.

> [!tip] Practice this lecture
> [[practice/30-multi-line-circuits|12 practice problems]] — 5 easy, 3 medium, 4 hard — each with a folded hint and a worked solution. Start with [[practice/30-multi-line-circuits#301-coefficients-both-ways|30.1 Coefficients both ways]]; the [[practice/index|practice hub]] has the whole bank by difficulty and by topic.

### Sources for this page
Kudeki notes, Lecture 30 (6 pages): the two-line circuit and bounce diagram, $\Gamma_{jk}$ and $\tau_{jk}$ with their verification, Examples 1–3, the series-resistor exercise and its hint. Rao (2009) §7.2, eqs. 7.20–7.26, for cross-checks, including the current coefficients. This site's own: the figures, the recipe, the DC and late-time sums, the $T_1$-form of the impulse response, the power ratios, the dielectric realization, the shunt-matching example; numbers checked by script. Slips in the notes (a $Z_2 = 2Z_2$ typo, a mislabelled plot) are on the errata page.
