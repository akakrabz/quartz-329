---
title: "Worked problem — Reading a line from two pulses"
description: "An impulse drives a 120 m line and only two pulses ever reach z = 30 m: find v, ε_r, R_g, R_L, the amplitude and the current, then the pulses and the step response after R_g changes. Modelled on FA23 Exam 3 #4–#5 and SP17 Exam 3 #2(v)–(vi)."
tags: [problem, transmission-lines]
---

*Problem · style of FA23 Exam 3 #4–#5 and SP17 Exam 3 #2(v)–(vi) · uses [[4-transmission-lines/28-distributed-circuits-and-bounce-diagrams|Lecture 28]] · concepts: [[concepts/bounce-diagram]], [[concepts/characteristic-impedance]]*

> [!question] Problem
> A generator with open-circuit voltage $f_i(t) = 24\,\delta(t)$ and unknown internal resistance $R_g$ drives a lossless, non-magnetic line, $Z_0 = 75\ \Omega$, from $z = 0$ to $z = \ell = 120$ m. An unknown resistor $R_L$ terminates it. Time is in μs throughout, so impulse weights are in V·μs. The voltage at $z = 30$ m is
> $$
> V(30\ \text{m},t) = A\,\delta(t-0.2) - \frac A3\,\delta(t-1.4),
> $$
> and nothing else ever arrives there. Use $c = 300$ m/μs.
>
> (a) Find $v$ and $\epsilon_r$.
>
> (b) Find $R_g$, (c) $R_L$, (d) $A$.
>
> (e) Find $I(30\ \text{m},t)$.
>
> (f) $R_g$ is replaced by $25\ \Omega$. Find $\tau_g$, $\Gamma_g$, and every impulse at $z = 30$ m for $t<3.5$ μs.
>
> (g) With $R_g = 25\ \Omega$, the source becomes $24\,u(t)$ V. Find $V(30\ \text{m},t)$ for $t<4.6$ μs, and the steady-state load voltage and current.

## (a) Speed

The first pulse is the injected wave arriving directly, at $z/v$:

$$
v = \frac{30\ \text{m}}{0.2\ \mu\text{s}} = 150\ \text{m}/\mu\text{s},\qquad T = \frac{\ell}{v} = 0.8\ \mu\text{s}.
$$

Check: the load echo arrives at $(2\ell-z)/v = 210/150 = 1.4$ μs, as observed. Non-magnetic, so $v = c/\sqrt{\epsilon_r}$ and $\epsilon_r = (300/150)^2 = 4$.

## (b)–(d) The generator, the load, the amplitude

- **$R_g$.** The load echo would re-reflect at the generator and pass $z = 30$ m again at $0.2+2T = 1.8$ μs. Nothing arrives, so $\Gamma_g\Gamma_L = 0$. There is an echo, so $\Gamma_L\ne0$; hence $\Gamma_g = 0$ and $R_g = Z_0 = 75\ \Omega$.
- **$R_L$.** The second pulse is the first one times $\Gamma_L$, so $\Gamma_L = -\tfrac13$ and
$$
R_L = Z_0\,\frac{1+\Gamma_L}{1-\Gamma_L} = 75\cdot\frac{2/3}{4/3} = 37.5\ \Omega .
$$
- **$A$.** $A = 24\,\tau_g = 24\cdot\dfrac{75}{75+75} = 12$ V·μs.

> [!key] Answers (a)–(d)
> $v = 150$ m/μs, $\epsilon_r = 4$, $R_g = 75\ \Omega$, $R_L = 37.5\ \Omega$, $A = 12$ V·μs.

## (e) Current

Forward waves carry $I = +V/Z_0$, backward waves $I = -V/Z_0$:

$$
\begin{gathered}
I(30\ \text{m},t) = \frac{12}{75}\,\delta(t-0.2) - \frac{(-4)}{75}\,\delta(t-1.4)\\[4pt]
= 0.16\,\delta(t-0.2) + 0.0533\,\delta(t-1.4)\ \ \text{A}\cdot\mu\text{s}.
\end{gathered}
$$

> [!trap] Where (e) loses points
> - Copying the voltage signs. The echo's voltage is negative, but it travels backward, so its current is positive.

## (f) A mismatched generator

$$
\begin{gathered}
\tau_g = \frac{75}{25+75} = \frac34,\qquad \Gamma_g = \frac{25-75}{25+75} = -\frac12,\\[6pt]
\Gamma_L\Gamma_g = \Big(-\frac13\Big)\Big(-\frac12\Big) = \frac16 .
\end{gathered}
$$

First weight $24\tau_g = 18$; then $\times\Gamma_L$ at the load, $\times\Gamma_g$ at the generator. Forward segments pass $z = 30$ m at $0.2+1.6n$ μs, backward ones at $1.4+1.6n$ μs:

| $t$ (μs) | segment | weight (V·μs) |
|---|---|---|
| 0.2 | forward, injected | $18$ |
| 1.4 | backward, $\times\Gamma_L$ | $-6$ |
| 1.8 | forward, $\times\Gamma_g$ | $3$ |
| 3.0 | backward, $\times\Gamma_L$ | $-1$ |
| 3.4 | forward, $\times\Gamma_g$ | $0.5$ |

> [!key] Answer (f)
> $V(30\ \text{m},t) = 18\,\delta(t-0.2) - 6\,\delta(t-1.4) + 3\,\delta(t-1.8) - \delta(t-3.0) + 0.5\,\delta(t-3.4)$ for $t<3.5$ μs.

## (g) Step input and steady state

Each impulse becomes a step, so $V(30\ \text{m},t)$ is the running sum of (f)'s weights: $18$ V on $(0.2, 1.4)$, $12$ on $(1.4, 1.8)$, $15$ on $(1.8, 3.0)$, $14$ on $(3.0, 3.4)$, $14.5$ on $(3.4, 4.6)$.

As $t\to\infty$ the line is two wires:

$$
\begin{gathered}
V_L = 24\cdot\frac{37.5}{25+37.5} = 14.4\ \text{V},\\[6pt]
I_L = \frac{24}{25+37.5} = 0.384\ \text{A}.
\end{gathered}
$$

Check with the series: $24\cdot\tfrac34\cdot\dfrac{1+\Gamma_L}{1-\Gamma_L\Gamma_g} = 18\cdot\dfrac{2/3}{5/6} = 14.4$ V.

> [!key] Answer (g)
> Staircase 18, 12, 15, 14, 14.5 V, closing in on $14.4$ V; $I_L(\infty) = 0.384$ A.

## The pattern

1. The first arrival time gives $v$; later arrivals check it.
2. A missing re-reflection means a matched end.
3. A pulse over its parent pulse is the $\Gamma$ of the end between them; invert for $R$.
4. The first weight over the source strength is $\tau_g$.
5. Current: flip the sign on backward waves.
6. Steady state: the lumped divider.

FA23 Exam 3 #4 runs steps 1–4 at the midpoint with a positive echo; SP17 Exam 3 #2(v)–(vi) sees a single pulse; FA23 #5 asks the steady state of a shorted line. This version observes at a quarter point, has a negative echo, asks for the current, and changes $R_g$. Every number here is checked by an FDTD simulation of the line.
