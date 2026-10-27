---
title: "Worked problem — A ramp pulse meets its echo"
description: "A 1 μs ramp pulse on a 600 m line with R_g = 25 Ω and R_L = 150 Ω: the coefficients, V and I along the line before, during and after the reflection, and the echo's return to the generator. Modelled on SP17 Exam 3 #5c."
tags: [problem, transmission-lines]
---

*Problem · style of SP17 Exam 3 #5 · uses [[4-transmission-lines/29-bounce-diagram-examples|Lecture 29]], [[4-transmission-lines/28-distributed-circuits-and-bounce-diagrams|Lecture 28]] · concepts: [[concepts/bounce-diagram]], [[concepts/characteristic-impedance]]*

> [!question] Problem
> A lossless line with $Z_0 = 50\ \Omega$ and $v = 200$ m/μs runs from $z = 0$ to $\ell = 600$ m. A source with internal resistance $R_g = 25\ \Omega$ drives it at $z = 0$, and $R_L = 150\ \Omega$ terminates it. The source's open-circuit voltage is a ramp pulse ($t$ in μs):
> $$
> \begin{gathered}
> f_i(t) = 3t\ \text{V}\quad(0<t<1),\\[4pt]
> f_i(t) = 0\quad\text{otherwise}.
> \end{gathered}
> $$
> (a) Find $\tau_g$, $\Gamma_g$, $\Gamma_L$, the one-way delay $T$ and the pulse's length on the line.
>
> (b) Sketch $V(z)$ and $I(z)$ at $t = 2$ μs and at $t = 5$ μs.
>
> (c) Find $V(z)$ and $I(z)$ at $t = 3.5$ μs. Check them at the load.
>
> (d) Find $V(0,t)$ and $I(0,t)$ for $0<t<12$ μs.

## (a) Coefficients and times

$$
\begin{gathered}
\tau_g = \frac{50}{25+50} = \frac23,\qquad \Gamma_g = \frac{25-50}{25+50} = -\frac13,\\[6pt]
\Gamma_L = \frac{150-50}{150+50} = \frac12,\\[6pt]
T = \frac{600\ \text{m}}{200\ \text{m}/\mu\text{s}} = 3\ \mu\text{s}.
\end{gathered}
$$

The pulse lasts 1 μs, so it is $v\cdot1\ \mu\text{s} = 200$ m long on the line. Segment weights (times $f_i$): $\tfrac23$ on $0<t<3$, $\tfrac23\cdot\tfrac12 = \tfrac13$ on $3<t<6$, $\tfrac13\cdot(-\tfrac13) = -\tfrac19$ on $6<t<9$ μs.

> [!key] Answer (a)
> $\tau_g = \tfrac23$, $\Gamma_g = -\tfrac13$, $\Gamma_L = \tfrac12$, $T = 3$ μs; the pulse is 200 m long. The launched wave is $\tfrac23\cdot3 = 2$ V at its peak.

## (b) Before and after the reflection

Each snapshot is a horizontal cut of the diagram ([[4-transmission-lines/29-bounce-diagram-examples|Lecture 29]] §1), with $z/v = z/200$ in μs.

**$t = 2$ μs.** Only the first segment: $V = \tfrac23f_i(2-z/200) = 4-z/100$ V where $0<2-z/200<1$, i.e. on $200<z<400$ m. It jumps to 2 V at $z = 200$ m (the ramp's end, sent last) and falls to 0 at the front, 400 m. $I = V/Z_0$: 40 mA peak.

**$t = 5$ μs.** Only the echo: $V = \tfrac13f_i(5+z/200-6) = z/200-1$ V on $200<z<400$ m, rising from 0 at its front ($z = 200$ m) to 1 V. Backward wave: $I = -V/Z_0$, down to $-20$ mA. The next forward segment starts at 6 μs.

<!-- fig:bex-ramp-problem -->

> [!key] Answer (b)
> - $t = 2$ μs: $V = 4-z/100$ V, $I = V/50$, on $200<z<400$ m; zero elsewhere.
> - $t = 5$ μs: $V = z/200-1$ V, $I = -V/50$, on $200<z<400$ m; zero elsewhere.

> [!trap] Where (b) loses points
> - Drawing the forward ramp rising toward $+z$. Its 0 V start leads, so it falls toward $+z$.
> - Forgetting the sign of $I$ for the echo. $\Gamma_L>0$ keeps $V$ positive but makes $I$ negative.

## (c) Overlap at t = 3.5 μs

Two segments contribute. The cut crosses only the echo, but the forward ramp's tail is still arriving.

$$
\begin{gathered}
V^+ = \tfrac23f_i\Big(3.5-\frac z{200}\Big) = 7-\frac z{100},\\[6pt]
V^- = \tfrac13f_i\Big(\frac z{200}-2.5\Big) = \frac z{200}-2.5,
\end{gathered}
$$

both on $500<z<600$ m and zero elsewhere. The forward ramp's first 100 m has already reflected into $V^-$. On $500<z<600$ m:

$$
\begin{gathered}
V = V^++V^- = 4.5-\frac z{200}\ \text{V},\\[6pt]
I = \frac{V^+-V^-}{Z_0} = \frac{9.5-0.015\,z}{50}\ \text{A}.
\end{gathered}
$$

> [!key] Answer (c)
> $V$ falls from 2 V at $z = 500$ m to 1.5 V at the load; $I$ falls from 40 mA to 10 mA. Zero for $z<500$ m.
>
> Load check: $V(\ell)/I(\ell) = 1.5\ \text{V}/10\ \text{mA} = 150\ \Omega = R_L$, and $V(\ell) = (1+\Gamma_L)V^+(\ell) = 1.5\cdot1$ V.

## (d) At the generator

A vertical cut at $z = 0$ (Lecture 28's recipe):

- $0<t<1$: the launched wave alone. $V(0,t) = \tfrac23f_i(t) = 2t$ V and $I = V/Z_0 = 40t$ mA.
- $1<t<6$: zero; the pulse is on the line.
- $6<t<7$: the echo arrives, $V^- = \tfrac13f_i(t-6) = t-6$ V, and leaves as $\Gamma_gV^-$. Add both segments:

$$
\begin{gathered}
V(0,t) = (1+\Gamma_g)V^- = \tfrac23(t-6)\ \text{V},\\[6pt]
I(0,t) = \frac{\Gamma_gV^- - V^-}{Z_0} = -\frac{4}{3}\cdot\frac{t-6}{50}\ \text{A}.
\end{gathered}
$$

- $7<t<12$: zero; the next echo returns at 12 μs.

> [!key] Answer (d)
> $V(0,t) = 2t$ V and $I(0,t) = 40t$ mA on $0<t<1$; $V(0,t) = \tfrac23(t-6)$ V and $I(0,t) = -26.7(t-6)$ mA on $6<t<7$; zero otherwise.
>
> Check: for $t>1$ the source is off, so KVL gives $V(0,t) = -R_gI(0,t)$, and $-25\cdot(-26.7\ \text{mA}) = 0.667$ V at $t\to7$.

## The pattern

1. Coefficients, $T$, pulse length.
2. The segments in flight; each is a weighted, delayed copy of $f_i$.
3. Where each argument lies inside the pulse.
4. $V$ adds the copies; $Z_0I$ subtracts the backward ones.
5. Ohm's law at the end involved.

SP17 Exam 3 #5c sends a truncated sine through a line with $\Gamma_g = \tfrac13$, $\Gamma_L = -\tfrac13$ and asks for $V(z)$ at two times. This version uses a ramp, so the reversal shows, adds $I$, an overlap snapshot and the generator end.
