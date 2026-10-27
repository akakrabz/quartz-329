---
title: "Worked problem — Echoes trapped on the second line"
description: "A step drives two cascaded lines through a matched generator into a mismatched load: junction coefficients both ways, the voltage bounce diagram, V and I at a point, and the load voltage converging to the DC value. Modelled on SP19 Exam 3 #4 and FA23 Exam 3 #3(a)."
tags: [problem, transmission-lines]
---

*Problem · style of SP19 Exam 3 #4 and FA23 Exam 3 #3(a) · uses [[4-transmission-lines/30-multi-line-circuits|Lecture 30]], [[4-transmission-lines/28-distributed-circuits-and-bounce-diagrams|Lecture 28]] · concepts: [[concepts/bounce-diagram]], [[concepts/reflection-and-transmission]]*

> [!question] Problem
> A source $f_i(t) = 120\,u(t)$ V with $R_g = 60\ \Omega$ drives line 1: $Z_1 = 60\ \Omega$, 300 m long, $v_1 = 2\times10^8$ m/s. At $z = 300$ m it joins line 2: $Z_2 = 180\ \Omega$, 300 m long, air-filled ($v_2 = 3\times10^8$ m/s). Line 2 ends in $R_L = 540\ \Omega$.
>
> (a) Find $\tau_g$, $\Gamma_g$, $\Gamma_L$, and the junction's voltage and current coefficients for waves moving right ($\Gamma_{12}$, $\tau_{12}$) and left ($\Gamma_{21}$, $\tau_{21}$).
>
> (b) Draw the voltage bounce diagram for $0\le t\le 8$ μs.
>
> (c) Find $V(150\text{ m},t)$ and $I(150\text{ m},t)$ for $0<t<8$ μs.
>
> (d) Find the load voltage $V_L(t)$ up to 8 μs and its limit as $t\to\infty$. Check the limit with the lumped circuit.
>
> (e) Which $R_L$ would make $V_L$ jump straight to its final value?

## (a) Coefficients and transit times

$$
\begin{gathered}
\tau_g = \frac{60}{60+60} = \frac12,\qquad \Gamma_g = 0,\\[6pt]
\Gamma_L = \frac{540-180}{540+180} = \frac12,\\[6pt]
\Gamma_{12} = \frac{180-60}{180+60} = \frac12,\qquad \tau_{12} = \frac32,\\[6pt]
\Gamma_{21} = -\frac12,\qquad \tau_{21} = \frac12.
\end{gathered}
$$

The current coefficients are $-\Gamma$ and $1-\Gamma$: $-\tfrac12$ and $\tfrac12$ moving right, $+\tfrac12$ and $\tfrac32$ moving left. One-way times: $T_1 = 300/(2\times10^8) = 1.5$ μs and $T_2 = 300/(3\times10^8) = 1$ μs.

## (b) The bounce diagram

The generator launches $\tau_g\cdot120 = 60$ V. At 1.5 μs the junction splits it into 30 V back and 90 V on. At 2.5 μs the load returns $\tfrac12\cdot90 = 45$ V. At 3.5 μs that echo meets the junction from the right: $\Gamma_{21}\cdot45 = -22.5$ V reflects toward the load and $\tau_{21}\cdot45 = 22.5$ V enters line 1. Everything arriving at $z = 0$ is absorbed ($\Gamma_g = 0$).

<!-- fig:mline-problem-bounce -->

Each trip around line 2 multiplies by $\Gamma_L\Gamma_{21} = -\tfrac14$: $90\to-22.5\to5.625\to\dots$, and the leftward leaks into line 1 are $\tau_{21}$ times $45, -11.25, \dots$

> [!trap] Where (b) loses points
> - Using $\tau_{12} = \tfrac32$ for the echo coming back from the load. Leftward waves use $\tau_{21} = \tfrac12$ and $\Gamma_{21} = -\tfrac12$.
> - Forgetting the leak into line 1 at 3.5 μs: every junction arrival has two offspring.

## (c) Voltage and current at z = 150 m

The point is 0.75 μs from both ends of line 1. Crossings: 60 V (rightward) at 0.75 μs, then the leftward 30 V at 2.25, 22.5 V at 4.25 and $-5.625$ V at 6.25 μs. Each leftward wave adds $-V/Z_1$ to the current.

| $t$ (μs) | 0–0.75 | 0.75–2.25 | 2.25–4.25 | 4.25–6.25 | 6.25–8.25 |
|---|---|---|---|---|---|
| $V$ (V) | 0 | 60 | 90 | 112.5 | 106.875 |
| $I$ (A) | 0 | 1 | 0.5 | 0.125 | 0.219 |

## (d) The load voltage

The load voltage is $(1+\Gamma_L) = \tfrac32$ times each arriving wave, added up: 135 V at 2.5 μs, then $135-33.75 = 101.25$ V at 4.5 μs, then $109.69$ V at 6.5 μs. The steps form a geometric series with ratio $-\tfrac14$:

$$
V_L(\infty) = \frac{135}{1+\tfrac14} = 108\ \text{V}.
$$

Lumped check: at DC both lines are wires, so $V_L = 120\cdot540/(60+540) = 108$ V and $I = 120/600 = 0.2$ A. The crossings at $z = 150$ m add up to the same: $60+30+22.5/(1+\tfrac14) = 108$ V.

> [!key] Answers (c)–(d)
> $V(150\text{ m})$: 60, 90, 112.5, 106.875 V; $I$: 1, 0.5, 0.125, 0.219 A. $V_L$: 0 until 2.5 μs, then 135, 101.25, 109.69 V; $V_L\to108$ V and $I\to0.2$ A.

## (e) No echo from the load

$R_L = Z_2 = 180\ \Omega$ gives $\Gamma_L = 0$. The first arrival, 90 V at 2.5 μs, is then final: the lumped value is $120\cdot180/240 = 90$ V. Line 1 settles at 3 μs, once the 30 V echo is absorbed by the generator.

## The pattern

1. Coefficients both ways at each junction; the generator and load each see only their own line.
2. One-way times, then the diagram; junction arrivals split in two.
3. $V$ at a point: add every crossing. $I$: divide by that line's $Z_0$, minus for leftward.
4. Sum the geometric tail and compare with the lumped circuit.

SP19 Exam 3 #4 runs these steps with the load matched, so the echoes bounce on line 1 between the junction and the generator. Here the generator is matched instead: the echoes stay on line 2, which brings in $\Gamma_{21}$ and $\tau_{21}$. FA23 Exam 3 #3(a) asks the same coefficient questions for three sections.
