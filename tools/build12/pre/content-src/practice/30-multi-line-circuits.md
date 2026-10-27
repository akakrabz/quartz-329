---
title: "Practice — Lecture 30: Multi-line circuits"
description: "12 practice problems (5 easy, 3 medium, 4 hard) on junctions between lines: Γ and τ = 1 + Γ both ways with current and power ratios, the line parameters of a splice, shunt and series resistors at a junction, a three-section cascade, a two-line bounce diagram under a step, locating a splice from its echoes, a tap resistor with an open stub, and a switched-on sine; hints on the medium and hard ones, a worked solution for each."
tags: [practice, transmission-lines]
lecture: 30
---

*Practice for [[4-transmission-lines/30-multi-line-circuits|Lecture 30]] · concepts: [[concepts/bounce-diagram]] · [[concepts/characteristic-impedance]] · [[concepts/reflection-and-transmission]] · all practice: [[practice/index|hub]] · by difficulty: [[practice/easy|easy]] · [[practice/medium|medium]] · [[practice/hard|hard]] · [[practice/topics|by topic]]*

Work each problem on paper first. Open the **hint** only when stuck, and the **solution** only after you have an answer you would hand in. Every answer here has been checked numerically.

The page runs on four rules, with [[4-transmission-lines/28-distributed-circuits-and-bounce-diagrams|Lecture 28]]'s conventions ($z = 0$ at the generator, $I$ along $+z$):
- Wave from line $j$ into line $k$: $\Gamma_{jk} = (Z_k-Z_j)/(Z_k+Z_j)$, $\tau_{jk} = 1+\Gamma_{jk}$; current ratios $-\Gamma_{jk}$ and $1-\Gamma_{jk}$.
- Resistor at the junction: $\Gamma$ uses what the wave sees ($R\parallel Z_k$ shunt, $R+Z_k$ series); series $R$ gives $\tau_{jk} = (1+\Gamma_{jk})Z_k/(R+Z_k)$.
- Ends: $\tau_g$ and $\Gamma_g$ with the first line's $Z_0$, $\Gamma_L$ with the last line's.
- $V(z,t)$: add the weights of all segments that have crossed $z$. $I$: divide each by its line's $Z_0$, minus for leftward segments.

## Easy

### 30.1 Coefficients both ways

> [!easy] Easy · line junction · transmission coefficient
> A 50 Ω coax (line 1) is spliced to a 75 Ω coax (line 2).
>
> (a) Find $\Gamma_{12}$, $\tau_{12}$ and the current reflection and transmission coefficients for a wave arriving from line 1.
>
> (b) The same for a wave arriving from line 2.
>
> (c) A 10 V step wave arrives from line 1. Find the reflected and transmitted voltages and currents, and check that $V$ and $I$ are continuous.
>
> *Source: original.*

> [!solution]- Solution
> (a) $Z_j = 50\ \Omega$, $Z_k = 75\ \Omega$:
> $$
> \Gamma_{12} = \frac{75-50}{75+50} = 0.2,\qquad \tau_{12} = 1.2.
> $$
> Current: $-\Gamma_{12} = -0.2$ reflected, $1-\Gamma_{12} = 0.8$ transmitted.
>
> (b) Swap the impedances: $\Gamma_{21} = -0.2$, $\tau_{21} = 0.8$; current $+0.2$ and $1.2$.
>
> (c) $V^- = 2$ V, $V^{++} = 12$ V. Currents along $+z$: incident $10/50 = 0.2$ A, reflected $-2/50 = -0.04$ A (leftward wave), transmitted $12/75 = 0.16$ A.
>
> **Check:** $V$: $10+2 = 12$ ✓. $I$: $0.2-0.04 = 0.16$ ✓. Power: 2 W in, 0.08 W back ($\Gamma^2 = 4\,\%$), 1.92 W on.
>
> **Answer.** (a) $\Gamma_{12} = 0.2$, $\tau_{12} = 1.2$; current $-0.2$ and $0.8$. (b) $\Gamma_{21} = -0.2$, $\tau_{21} = 0.8$; current $+0.2$ and $1.2$. (c) 2 V and $-0.04$ A reflected; 12 V and 0.16 A transmitted.

### 30.2 Junction facts

> [!easy] Easy · true or false · line junction
> Line 1 ($Z_1$, $v_1$) meets line 2 ($Z_2$, $v_2$) at a junction. True or false?
>
> (a) With $Z_2 = Z_1$ and $v_2 = 2v_1$, part of a wave reflects at the junction.
>
> (b) If $\tau_{12} = 4/3$, the transmitted wave carries more power than the incident one.
>
> (c) $\Gamma_{21} = -\Gamma_{12}$ and $\tau_{12}+\tau_{21} = 2$.
>
> (d) A 50 Ω line feeding two 100 Ω lines connected in parallel at one node reflects nothing.
>
> (e) The ratio of transmitted to incident current is $\tau_{12}$.
>
> (f) Just after a wave arrives, line 2 loads the junction like a resistor $Z_2$, even if its far end is open.
>
> *Source: original.*

> [!solution]- Solution
> (a) **False.** $\Gamma_{12} = (Z_2-Z_1)/(Z_2+Z_1) = 0$; speeds only set the timing.
>
> (b) **False.** $\tau_{12} = 4/3$ means $Z_2 = 2Z_1$, so the transmitted fraction is $\tau_{12}^2Z_1/Z_2 = \tfrac{16}9\cdot\tfrac12 = \tfrac89$. More volts, fewer amps.
>
> (c) **True.** Swapping $Z_1$ and $Z_2$ flips the sign of $\Gamma$; $\tau_{12}+\tau_{21} = 2+\Gamma_{12}+\Gamma_{21} = 2$.
>
> (d) **True.** The wave sees $100\parallel100 = 50\ \Omega = Z_1$: $\Gamma = 0$, and $\tau = 1$ into each branch, which takes half the power.
>
> (e) **False.** It is $1-\Gamma_{12} = \tau_{12}Z_1/Z_2$.
>
> (f) **True.** Line 2 carries only the outgoing wave, $V/I = Z_2$, until the echo from its far end returns $2T_2$ later.
>
> **Answer.** (a) F, (b) F, (c) T, (d) T, (e) F, (f) T.

### 30.3 No echo toward the source

> [!easy] Easy · multiple choice · line junction
> A generator ($R_g$) drives line A ($Z_A$). At the end of line A, a resistor $R$ is connected across the junction with line B ($Z_B$), which ends in $R_L$. The source is a step. What is the minimum set of conditions for no wave ever to travel back toward the generator on line A?
>
> (a) $R_g = Z_A$
>
> (b) $Z_B = Z_A$
>
> (c) $RZ_B/(R+Z_B) = Z_A$
>
> (d) $RZ_B/(R+Z_B) = Z_A$ and $R_L = Z_B$
>
> (e) the conditions of (d) and $R_g = Z_A$
>
> *Source: SP18 Exam 3 #1(vii) style, with two lines and a shunt resistor.*

> [!solution]- Solution
> **(d).** Every discontinuity downstream must be silent:
> - Junction from the left: the wave sees $R\parallel Z_B$, so $\Gamma_{AB} = 0$ needs $R\parallel Z_B = Z_A$.
> - Load: $R_L = Z_B$, so nothing comes back along line B.
>
> The others:
> - (a) $R_g$ absorbs echoes that arrive; it does not stop them arriving.
> - (b) With $R$ present the wave sees $R\parallel Z_A<Z_A$, so $\Gamma_{AB}<0$.
> - (c) Kills only the first echo. A load echo crosses back with $\tau_{BA} = 2Z'/(Z'+Z_B)\neq0$, where $Z' = R\parallel Z_A$.
> - (e) Sufficient, but not minimal: with (d) nothing returns, so there is nothing for $R_g$ to absorb.
>
> **Answer.** (d).

### 30.4 Line parameters of a splice

> [!easy] Easy · line parameters · line junction
> Line 2 has half the characteristic impedance and a third of the speed of line 1: $Z_2 = Z_1/2$, $v_2 = v_1/3$.
>
> (a) Find $\mathcal{L}_2$ and $\mathcal{C}_2$ in terms of $\mathcal{L}_1$ and $\mathcal{C}_1$.
>
> (b) Find $\Gamma_{12}$ and $\tau_{12}$.
>
> (c) Both lines have the same cross-section, and line 1 is air-filled. Find $\mu_r$ and $\epsilon_r$ of line 2's filling.
>
> *Source: course notes Lecture 30 Example 1, new ratios.*

> [!solution]- Solution
> (a) $Z_0 = \sqrt{\mathcal{L}/\mathcal{C}}$ and $v = 1/\sqrt{\mathcal{L}\mathcal{C}}$ give $\mathcal{L} = Z_0/v$ and $\mathcal{C} = 1/(Z_0v)$:
> $$
> \frac{\mathcal{L}_2}{\mathcal{L}_1} = \frac{1/2}{1/3} = \frac32,\qquad \frac{\mathcal{C}_2}{\mathcal{C}_1} = \frac{1}{\tfrac12\cdot\tfrac13} = 6.
> $$
> (b) $\Gamma_{12} = \dfrac{Z_1/2-Z_1}{Z_1/2+Z_1} = -\dfrac13$, $\tau_{12} = \dfrac23$. The speeds do not enter.
>
> (c) Same geometrical factor, so $\mathcal{L}\propto\mu$ and $\mathcal{C}\propto\epsilon$ ([[4-transmission-lines/27-guided-tem-waves-on-transmission-lines|Lecture 27]] §4): $\mu_r = 1.5$, $\epsilon_r = 6$.
>
> **Check:** $v_2/v_1 = 1/\sqrt{1.5\cdot6} = 1/3$ ✓; $Z_2/Z_1 = \sqrt{1.5/6} = 1/2$ ✓.
>
> **Answer.** $\mathcal{L}_2 = 1.5\,\mathcal{L}_1$, $\mathcal{C}_2 = 6\,\mathcal{C}_1$; $\Gamma_{12} = -1/3$, $\tau_{12} = 2/3$; $\mu_r = 1.5$, $\epsilon_r = 6$.

### 30.5 The returning echo

> [!easy] Easy · find the error · line junction
> Line 1 ($Z_1 = 50\ \Omega$) joins line 2 ($Z_2 = 200\ \Omega$). A 25 V echo from the load travels back along line 2 toward the junction. A student writes:
>
> "$\Gamma_{12} = \dfrac{200-50}{200+50} = 0.6$ and $\tau_{12} = 1.6$. Into line 1: $1.6\times25 = 40$ V. Back toward the load: $0.6\times25 = 15$ V."
>
> What is wrong? Give the correct voltages and check them.
>
> *Source: original.*

> [!solution]- Solution
> **The slip:** the wave arrives from line 2, so $Z_j = 200\ \Omega$ and $Z_k = 50\ \Omega$:
> $$
> \Gamma_{21} = \frac{50-200}{50+200} = -0.6,\qquad \tau_{21} = 0.4.
> $$
> Into line 1: $0.4\times25 = 10$ V. Back toward the load: $-0.6\times25 = -15$ V.
>
> **Check** (currents along $+z$): line-2 side $-25/200+(-15)/200 = -0.2$ A; line-1 side $-10/50 = -0.2$ A ✓. The student's numbers give $-0.05$ A and $-0.8$ A.
>
> **Watch out:** $V$ continuity cannot catch this slip ($25+15 = 40$ balances too), because $\tau = 1+\Gamma$ holds for either pair. Check the current.
>
> **Answer.** The student used the coefficients for a right-moving wave. With $\Gamma_{21} = -0.6$, $\tau_{21} = 0.4$: 10 V enters line 1 and $-15$ V reflects toward the load.

## Medium

### 30.6 A shunt resistor that matches

> [!medium] Medium · line junction · power balance
> Line 1 ($Z_1 = 50\ \Omega$) meets line 2 ($Z_2 = 75\ \Omega$), with a resistor $R$ across the junction.
>
> (a) Find $R$ so that waves from line 1 do not reflect.
>
> (b) With that $R$, what fractions of the incident power enter line 2 and $R$?
>
> (c) Find $\Gamma_{21}$ and $\tau_{21}$ for a wave arriving from line 2, and the fractions of its power reflected, sent into line 1 and absorbed by $R$.
>
> *Source: course notes Lecture 30 Example 3, new numbers.*

> [!hint]- Hint
> From line 1 the wave sees $R\parallel Z_2$; from line 2 it sees $R\parallel Z_1$. Each power is the junction voltage squared over the resistance it sits across.

> [!solution]- Solution
> **Setup.** Shunt $R$: $Z_{eq} = R\parallel Z_k$ in $\Gamma_{jk}$, and $\tau_{jk} = 1+\Gamma_{jk}$ (one junction voltage across all three).
>
> (a) $R\parallel75 = 50$: $\dfrac1R = \dfrac1{50}-\dfrac1{75} = \dfrac1{150}$, so $R = 150\ \Omega$; $\Gamma_{12} = 0$, $\tau_{12} = 1$.
>
> (b) The junction voltage is $V^+$. Incident $(V^+)^2/50$; line 2 takes $(V^+)^2/75$, a fraction $\tfrac23$; $R$ takes $(V^+)^2/150$, a fraction $\tfrac13$.
>
> (c) $Z_{eq} = 150\parallel50 = 37.5\ \Omega$:
> $$
> \Gamma_{21} = \frac{37.5-75}{37.5+75} = -\frac13,\qquad \tau_{21} = \frac23.
> $$
> Fractions of $(V^+)^2/75$: reflected $\Gamma_{21}^2 = \tfrac19$; line 1 $\tau_{21}^2\cdot\tfrac{75}{50} = \tfrac23$; $R$ $\tau_{21}^2\cdot\tfrac{75}{150} = \tfrac29$.
>
> **Check:** $\tfrac19+\tfrac23+\tfrac29 = 1$ ✓. The match works from one side only and costs a third of the power.
>
> **Answer.** $R = 150\ \Omega$; $\tfrac23$ into line 2, $\tfrac13$ into $R$. From line 2: $\Gamma_{21} = -\tfrac13$, $\tau_{21} = \tfrac23$; $\tfrac19$ reflected, $\tfrac23$ into line 1, $\tfrac29$ into $R$.

### 30.7 A series resistor in the splice

> [!medium] Medium · line junction · transmission coefficient · power balance
> Line 1 ($Z_1 = 50\ \Omega$) and line 2 ($Z_2 = 75\ \Omega$) are joined through a resistor $R = 25\ \Omega$ in series with the upper conductor.
>
> (a) Find $\Gamma_{12}$ and $\tau_{12}$.
>
> (b) Find $\Gamma_{21}$ and $\tau_{21}$.
>
> (c) For a wave from line 1, find the fractions of its power reflected, transmitted and absorbed by $R$.
>
> (d) Why is $\tau_{12}\neq1+\Gamma_{12}$ here?
>
> *Source: course notes Lecture 30 exercise (series resistor), new numbers.*

> [!hint]- Hint
> The arriving wave sees $R+Z_2$. The voltage $(1+\Gamma_{12})V^+$ on the line-1 side then divides between $R$ and line 2.

> [!solution]- Solution
> **Setup.** Series $R$: $Z_{eq} = R+Z_k$ in $\Gamma_{jk}$, and $\tau_{jk} = (1+\Gamma_{jk})Z_k/(R+Z_k)$.
>
> (a) $Z_{eq} = 100\ \Omega$: $\Gamma_{12} = \dfrac{100-50}{100+50} = \dfrac13$, $\ \tau_{12} = \dfrac43\cdot\dfrac{75}{100} = 1$.
>
> (b) $Z_{eq} = 25+50 = 75\ \Omega = Z_2$: $\Gamma_{21} = 0$, $\ \tau_{21} = 1\cdot\dfrac{50}{75} = \dfrac23$.
>
> (c) Reflected $\Gamma_{12}^2 = \tfrac19$. Line 2: $\tau_{12}^2Z_1/Z_2 = \tfrac23$. $R$ carries the line-1 current $(1-\Gamma_{12})V^+/Z_1$, so its share is $(1-\Gamma_{12})^2R/Z_1 = \tfrac49\cdot\tfrac12 = \tfrac29$.
>
> (d) $1+\Gamma_{12} = \tfrac43$ is the voltage on the line-1 side; $R$ takes a quarter of it and line 2 the rest.
>
> **Check:** $\tfrac19+\tfrac23+\tfrac29 = 1$ ✓. Current: $\tfrac23V^+/50 = V^+/75 = \tau_{12}V^+/Z_2$ ✓. Compare 30.6: a shunt $R$ matches the low-impedance side, a series $R$ the high-impedance side.
>
> **Answer.** $\Gamma_{12} = \tfrac13$, $\tau_{12} = 1$; $\Gamma_{21} = 0$, $\tau_{21} = \tfrac23$; $\tfrac19$ reflected, $\tfrac23$ transmitted, $\tfrac29$ in $R$; $R$ takes part of the junction voltage, so line 2 gets less than $1+\Gamma_{12}$.

### 30.8 Three sections and the first echoes

> [!medium] Medium · line junction · bounce diagram · impulse response
> An impulse source $f_i(t) = \delta(t)$ behind $R_g = 25\ \Omega$ drives three cascaded sections: $Z_{01} = 75\ \Omega$ (one-way delay 2 μs), $Z_{02} = 150\ \Omega$ (1 μs) and $Z_{03} = 50\ \Omega$ (3 μs), ending in $R_L = 50\ \Omega$.
>
> (a) Find $\tau_g$ and $\Gamma_g$.
>
> (b) Find the voltage reflection coefficient at the 1–2 junction and the current reflection coefficient at the 2–3 junction, both for right-moving waves.
>
> (c) List the impulses in $V(0,t)$ for $0\le t<8$ μs. Which one comes from the 2–3 junction?
>
> (d) When does the first impulse reach the load, and with what weight?
>
> *Source: FA23 Exam 3 #3(a) style, re-parameterized.*

> [!hint]- Hint
> Two paths return before 8 μs: out and back through section 1 (4 μs), and out and back through sections 1 and 2 (6 μs). Multiply the coefficients along each; $V(0,t)$ gets $(1+\Gamma_g)$ times each arrival.

> [!solution]- Solution
> (a) $\tau_g = \dfrac{75}{25+75} = \dfrac34$, $\ \Gamma_g = \dfrac{25-75}{25+75} = -\dfrac12$.
>
> (b) $\Gamma_{12} = \dfrac{150-75}{150+75} = \dfrac13$. $\ \Gamma_{23} = \dfrac{50-150}{50+150} = -\dfrac12$, so the current coefficient is $-\Gamma_{23} = +\tfrac12$. Needed below: $\tau_{12} = \tfrac43$, $\tau_{21} = \tfrac23$, $\tau_{23} = \tfrac12$, $\Gamma_L = 0$.
>
> (c) Impulses in $V(0,t)$:
> - $t = 0$: the launch, $\tfrac34$.
> - $t = 2\cdot2 = 4$ μs: the 1–2 echo arrives with $\tfrac34\cdot\tfrac13 = \tfrac14$; $V$ gets $(1+\Gamma_g)\tfrac14 = \tfrac18$.
> - $t = 2(2+1) = 6$ μs: the 2–3 echo arrives with $\tfrac34\cdot\tfrac43\cdot(-\tfrac12)\cdot\tfrac23 = -\tfrac13$; $V$ gets $\tfrac12\cdot(-\tfrac13) = -\tfrac16$.
>
> (d) Straight through, $2+1+3 = 6$ μs, with $\tau_g\tau_{12}\tau_{23} = \tfrac34\cdot\tfrac43\cdot\tfrac12 = \tfrac12$. $\Gamma_L = 0$, so $V_L$ gets exactly that.
>
> **Check:** no 2–3 echo can arrive before $2(T_1+T_2) = 6$ μs. The next arrivals at $z = 0$ come at 8 μs (a second round trip in section 1, a bounce inside section 2); a load echo would need 12 μs, but $\Gamma_L = 0$.
>
> **Answer.** (a) $\tau_g = \tfrac34$, $\Gamma_g = -\tfrac12$. (b) $\tfrac13$; current coefficient $+\tfrac12$. (c) $V(0,t) = \tfrac34\delta(t)+\tfrac18\delta(t-4\ \mu\text{s})-\tfrac16\delta(t-6\ \mu\text{s})$; the last is the 2–3 echo. (d) At 6 μs, weight $\tfrac12$.

## Hard

### 30.9 Two lines and a mismatched source

> [!hard] Hard · bounce diagram · line junction · steady state
> A source $f_i(t) = 80\,u(t)$ V with $R_g = 50\ \Omega$ drives line 1: $Z_1 = 150\ \Omega$ from $z = 0$ to 400 m, $v_1 = 2\times10^8$ m/s. At $z = 400$ m it joins line 2: $Z_2 = 50\ \Omega$, 300 m long, air-filled ($v_2 = 3\times10^8$ m/s), ending in $R_L = 50\ \Omega$.
>
> (a) Find $\tau_g$, $\Gamma_g$, $\Gamma_L$ and the voltage and current reflection and transmission coefficients at the junction for a right-moving wave.
>
> (b) Draw the voltage bounce diagram for $0\le t\le10$ μs, with every weight.
>
> (c) Find $V$ and $I$ at $z = 100$ m, $t = 5$ μs.
>
> (d) Find $V_L(t)$ up to 10 μs, and $V_L$ and $I_L$ as $t\to\infty$. Check with the lumped circuit.
>
> *Source: SP19 Exam 3 #4, re-parameterized (step-down junction, mismatched source).*

> [!hint]- Hint
> $T_1 = 2$ μs, $T_2 = 1$ μs. Nothing returns from the load, so the echoes stay on line 1, and each round trip there multiplies by $\Gamma_{12}\Gamma_g$. At $z = 100$ m, rightward segments cross at $0.5+4n$ μs and leftward ones at $3.5+4n$ μs.

> [!solution]- Solution
> (a) $\tau_g = \dfrac{150}{50+150} = \dfrac34$, $\ \Gamma_g = \dfrac{50-150}{50+150} = -\dfrac12$, $\ \Gamma_L = 0$.
> $$
> \Gamma_{12} = \frac{50-150}{50+150} = -\frac12,\qquad \tau_{12} = \frac12.
> $$
> Current: $-\Gamma_{12} = +\tfrac12$ reflected, $1-\Gamma_{12} = \tfrac32$ transmitted. $T_1 = 400/(2\times10^8) = 2$ μs, $T_2 = 300/(3\times10^8) = 1$ μs.
>
> (b) Launch $\tfrac34\cdot80 = 60$ V; each round trip on line 1 multiplies by $\Gamma_{12}\Gamma_g = \tfrac14$.
>
> | segment | line | $t$ (μs) | weight (V) |
> |---|---|---|---|
> | launch, rightward | 1 | 0–2 | 60 |
> | junction echo, leftward | 1 | 2–4 | $-30$ |
> | transmitted, absorbed at load | 2 | 2–3 | 30 |
> | generator echo, rightward | 1 | 4–6 | 15 |
> | junction echo, leftward | 1 | 6–8 | $-7.5$ |
> | transmitted, absorbed at load | 2 | 6–7 | 7.5 |
> | generator echo, rightward | 1 | 8–10 | 3.75 |
>
> At 10 μs the junction splits 3.75 V into $-1.875$ V back and 1.875 V on.
>
> (c) Crossings at 100 m before 5 μs: 60 V at 0.5 μs (rightward), $-30$ V at 3.5 μs (leftward), 15 V at 4.5 μs (rightward):
> $$
> V = 60-30+15 = 45\ \text{V},\qquad I = \frac{60-(-30)+15}{150} = 0.7\ \text{A}.
> $$
> (d) $\Gamma_L = 0$, so $V_L$ is the running sum of arrivals: 0 for $t<3$ μs, 30 V on $3<t<7$ μs, 37.5 V on $7<t<11$ μs. Then
> $$
> V_L(\infty) = \frac{30}{1-\tfrac14} = 40\ \text{V},\qquad I_L(\infty) = \frac{40}{50} = 0.8\ \text{A}.
> $$
> **Check:** lumped divider $80\cdot\dfrac{50}{50+50} = 40$ V and $80/100 = 0.8$ A ✓. On line 1 the rightward weights sum to $60/(1-\tfrac14) = 80$ V and the leftward ones to $-40$ V: $V = 40$ V, $I = (80+40)/150 = 0.8$ A ✓.
>
> **Watch out:** a leftward segment with negative voltage carries positive current.
>
> **Answer.** (a) $\tau_g = \tfrac34$, $\Gamma_g = -\tfrac12$, $\Gamma_L = 0$; $\Gamma_{12} = -\tfrac12$, $\tau_{12} = \tfrac12$; current $+\tfrac12$ and $\tfrac32$. (b) Line 1: 60, $-30$, 15, $-7.5$, 3.75 V starting at 0, 2, 4, 6, 8 μs; line 2: 30 V at 2 μs, 7.5 V at 6 μs. (c) 45 V, 0.7 A. (d) $V_L = 0$, then 30 V from 3 μs and 37.5 V from 7 μs; $V_L\to40$ V, $I_L\to0.8$ A.

### 30.10 Locating a splice by its echoes

> [!hard] Hard · line junction · bounce diagram · load reflection coefficient
> A pulse generator ($R_g = 50\ \Omega$; open-circuit output an 18 V pulse, 10 ns long) drives a 50 Ω cable ($v_1 = 2\times10^8$ m/s) from $z = 0$. Somewhere along it the cable is spliced to an air-filled line ($v_2 = 3\times10^8$ m/s) of unknown $Z_2$ and length, which ends in an unknown resistor. A scope at $z = 0$ shows 10 ns pulses of 9 V at $t = 0$, 3 V at 1.0 μs, $-8$ V at 1.8 μs and $-8/3$ V at 2.6 μs.
>
> (a) Where is the splice?
>
> (b) Find $Z_2$.
>
> (c) Find the termination and the length of the air line.
>
> (d) Predict the next pulse.
>
> (e) With $R_g = 25\ \Omega$ instead, how high would the pulse at 1.0 μs be?
>
> *Source: FA23 Exam 3 #4 style, extended to a splice.*

> [!hint]- Hint
> $\Gamma_g = 0$, so the scope shows each arrival once, unchanged. The first echo is $\Gamma_{12}$ times the launched pulse; the second has crossed the splice twice ($\tau_{12}$, then $\tau_{21}$) and reflected once at the far end. For (e), $V(0,t)$ gets $(1+\Gamma_g)$ times the arrival.

> [!solution]- Solution
> **Setup.** $\tau_g = \tfrac12$: the launched pulse is 9 V. $\Gamma_g = 0$: every arrival appears once and is absorbed.
>
> (a) The splice echo returns after $2d/v_1 = 1.0$ μs: $d = 100$ m.
>
> (b) $\Gamma_{12} = 3/9 = \tfrac13$, so
> $$
> Z_2 = Z_1\frac{1+\Gamma_{12}}{1-\Gamma_{12}} = 50\cdot\frac{4/3}{2/3} = 100\ \Omega.
> $$
> (c) Then $\tau_{12} = \tfrac43$, $\Gamma_{21} = -\tfrac13$, $\tau_{21} = \tfrac23$. Second echo:
> $$
> 9\,\tau_{12}\Gamma_L\tau_{21} = 8\,\Gamma_L = -8\ \text{V}\quad\Rightarrow\quad\Gamma_L = -1,
> $$
> a short circuit. The round trip in the air line is $1.8-1.0 = 0.8$ μs, so $\ell_2 = v_2\cdot0.4\ \mu\text{s} = 120$ m.
>
> **Check:** each later echo makes one more round trip in line 2, a factor $\Gamma_{21}\Gamma_L = \tfrac13$: $-8\cdot\tfrac13 = -\tfrac83$ V at 2.6 μs ✓.
>
> (d) $-\tfrac83\cdot\tfrac13 = -\tfrac89\approx-0.89$ V at 3.4 μs.
>
> (e) $\tau_g = \tfrac{50}{75} = \tfrac23$ launches 12 V, and 4 V returns at 1.0 μs. Now $\Gamma_g = -\tfrac13$, so the scope shows $(1-\tfrac13)\cdot4 = \tfrac83\approx2.67$ V.
>
> **Answer.** (a) 100 m from the generator. (b) $Z_2 = 100\ \Omega$. (c) A short ($\Gamma_L = -1$) at the end of a 120 m air line. (d) $-8/9$ V at 3.4 μs. (e) $8/3\approx2.67$ V.

### 30.11 A tap resistor and an open stub

> [!hard] Hard · line junction · transients · steady state
> A source $f_i(t) = 100\,u(t)$ V with $R_g = 50\ \Omega$ drives line 1 ($Z_1 = 50\ \Omega$, one-way delay $T_1 = 1$ μs). At its end a resistor $R = 50\ \Omega$ is connected across the junction with line 2 ($Z_2 = 50\ \Omega$, $T_2 = 0.5$ μs), whose far end is open.
>
> (a) Find $\tau_g$, $\Gamma_g$, $\Gamma_L$ and the junction coefficients both ways.
>
> (b) Draw the voltage bounce diagram for $0\le t\le4$ μs.
>
> (c) Find the junction voltage $V_J(t)$ for $0<t<4$ μs and the current in $R$ at $t = 2.5$ μs.
>
> (d) Find $V_J$, the open-end voltage and the current in $R$ as $t\to\infty$. Check with the lumped circuit.
>
> *Source: original (course notes Lecture 30 Example 3 with an open stub).*

> [!hint]- Hint
> Both ways the wave sees $50\parallel50 = 25\ \Omega$. The generator is matched, so leftward waves on line 1 are absorbed and the echoes live on line 2, each round trip there multiplying by $\Gamma_L\Gamma_{21}$. An arrival $w$ from line 2 changes $V_J$ by $(1+\Gamma_{21})w$.

> [!solution]- Solution
> (a) $\tau_g = \tfrac12$, $\Gamma_g = 0$, $\Gamma_L = +1$. Both ways $Z_{eq} = 50\parallel50 = 25\ \Omega$:
> $$
> \Gamma_{12} = \Gamma_{21} = \frac{25-50}{25+50} = -\frac13,\qquad \tau_{12} = \tau_{21} = \frac23.
> $$
> (b) Launch 50 V; each trip around line 2 multiplies by $\Gamma_L\Gamma_{21} = -\tfrac13$. Weights in V (→ rightward, ← leftward):
>
> | $t$ (μs) | line 1 | line 2, first half-interval | line 2, second half-interval |
> |---|---|---|---|
> | 0–1 | 50 → | — | — |
> | 1–2 | $-50/3$ ← | $100/3$ → | $100/3$ ← |
> | 2–3 | $200/9$ ← | $-100/9$ → | $-100/9$ ← |
> | 3–4 | $-200/27$ ← | $100/27$ → | $100/27$ ← |
>
> (c) $V_J$ starts at $\tau_{12}\cdot50$; each later arrival $w$ from line 2 adds $\tfrac23w$:
> - $0<t<1$ μs: 0.
> - $1<t<2$ μs: $100/3 = 33.3$ V.
> - $2<t<3$ μs: $\tfrac{100}3+\tfrac23\cdot\tfrac{100}3 = \tfrac{500}9 = 55.6$ V.
> - $3<t<4$ μs: $\tfrac{500}9-\tfrac23\cdot\tfrac{100}9 = \tfrac{1300}{27} = 48.1$ V.
>
> Current in $R$ at 2.5 μs: $\dfrac{500/9}{50} = \dfrac{10}9\approx1.11$ A.
>
> (d) The arrivals form a geometric series with ratio $-\tfrac13$:
> $$
> V_J(\infty) = \frac{100}3+\frac{\tfrac23\cdot\tfrac{100}3}{1+\tfrac13} = \frac{100}3+\frac{50}3 = 50\ \text{V}.
> $$
> The open end gets twice each arrival: $\tfrac{200}3$, then $\tfrac{400}9$, $\tfrac{1400}{27}$ V, …, tending to $\dfrac{200/3}{1+1/3} = 50$ V. $I_R\to1$ A.
>
> **Check:** at DC the stub carries no current and both lines are wires: $100\cdot\dfrac{50}{50+50} = 50$ V everywhere and $I_R = 1$ A ✓.
>
> **Watch out:** an arrival from line 2 changes $V_J$ by $(1+\Gamma_{21})w = \tau_{21}w$; it equals $\tau_{12}w$ here only because $Z_1 = Z_2$.
>
> **Answer.** (a) $\tau_g = \tfrac12$, $\Gamma_g = 0$, $\Gamma_L = 1$; $\Gamma_{12} = \Gamma_{21} = -\tfrac13$, $\tau_{12} = \tau_{21} = \tfrac23$. (b) Line 1: 50 V, then $-\tfrac{50}3$, $\tfrac{200}9$, $-\tfrac{200}{27}$ V leftward from 1, 2, 3 μs; line 2: $\tfrac{100}3$, $-\tfrac{100}9$, $\tfrac{100}{27}$ V from 1, 2, 3 μs, each returning unchanged from the open end. (c) $V_J = 0$, 33.3, 55.6, 48.1 V in successive microseconds; $I_R(2.5\ \mu\text{s}) = 1.11$ A. (d) $V_J$ and the open end tend to 50 V, $I_R$ to 1 A.

### 30.12 A switched-on sine across a step-down

> [!hard] Hard · impulse response · line junction · steady state
> A source $f_i(t) = 14\sin(2\pi ft)\,u(t)$ V with $R_g = 150\ \Omega$ drives line 1 ($Z_1 = 50\ \Omega$, 600 m, $v_1 = 2\times10^8$ m/s), joined to line 2 ($Z_2 = 25\ \Omega$, 450 m, $v_2 = 3\times10^8$ m/s), which ends in $R_L = 25\ \Omega$.
>
> (a) Find $\tau_g$, $\Gamma_g$, $\Gamma_{12}$, $\tau_{12}$, $\Gamma_L$, $T_1$ and $T_2$.
>
> (b) Write the load's impulse response $h_L(t)$.
>
> (c) For $f = 1$ MHz, find $V_L(t)$ for $4.5<t<10.5$ μs and for $10.5<t<16.5$ μs, and the wavelength on each line.
>
> (d) Find the amplitude $V_L$ settles to for $f = 1$ MHz and for $f = 1.25$ MHz. Why do they differ?
>
> *Source: course notes Lecture 30 Example 2 style, new circuit.*

> [!hint]- Hint
> $\Gamma_L = 0$, so only line 1 echoes: each round trip ($2T_1$) multiplies by $\Gamma_{12}\Gamma_g$. Replace each $\delta(t-t_n)$ by $f_i(t-t_n)$, and compare $2T_1$ with the period.

> [!solution]- Solution
> (a) $\tau_g = \dfrac{50}{200} = \dfrac14$, $\Gamma_g = \dfrac{100}{200} = \dfrac12$, $\Gamma_{12} = \dfrac{25-50}{25+50} = -\dfrac13$, $\tau_{12} = \dfrac23$, $\Gamma_L = 0$; $T_1 = 3$ μs, $T_2 = 1.5$ μs.
>
> (b) First arrival $\tau_g\tau_{12} = \tfrac16$ at $T_1+T_2 = 4.5$ μs; each round trip on line 1 adds 6 μs and a factor $\Gamma_{12}\Gamma_g = -\tfrac16$:
> $$
> h_L(t) = \frac16\sum_{n=0}^{\infty}\Big(-\frac16\Big)^n\delta(t-4.5-6n)\qquad(t\ \text{in}\ \mu\text{s}).
> $$
> (c) With $t$ in μs, $f_i(t) = 14\sin2\pi t$. Then $f_i(t-4.5) = 14\sin(2\pi t-9\pi) = -14\sin2\pi t$, and $f_i(t-10.5) = -14\sin2\pi t$ too:
> $$
> \begin{aligned}
> 4.5<t<10.5:&\quad V_L = -\tfrac{14}6\sin2\pi t = -\tfrac73\sin2\pi t\ \text{V},\\
> 10.5<t<16.5:&\quad V_L = \Big(-\tfrac73+\tfrac{14}{36}\Big)\sin2\pi t = -\tfrac{35}{18}\sin2\pi t\ \text{V}.
> \end{aligned}
> $$
> Wavelengths $v/f$: 200 m on line 1, 300 m on line 2.
>
> (d) 1 MHz: $2T_1 = 6$ periods, so every copy is $-14\sin2\pi t$ and the weights add as $\tfrac16(1-\tfrac16+\tfrac1{36}-\dots)$:
> $$
> \lvert V_L\rvert\to14\cdot\frac{1/6}{1+1/6} = 2\ \text{V}.
> $$
> 1.25 MHz: the period is 0.8 μs and $2T_1 = 7.5$ periods, so each copy is inverted relative to the one before. That cancels the sign of $\Gamma_{12}\Gamma_g$:
> $$
> \lvert V_L\rvert\to14\cdot\frac{1/6}{1-1/6} = 2.8\ \text{V}.
> $$
> **Check:** at 1 MHz the copies stack like those of a DC step, and the DC divider gives $14\cdot\dfrac{25}{150+25} = 2$ V ✓. The 1 MHz amplitudes run 2.33, 1.94, 2.01 V, … toward 2 V.
>
> **Answer.** (a) $\tau_g = \tfrac14$, $\Gamma_g = \tfrac12$, $\Gamma_{12} = -\tfrac13$, $\tau_{12} = \tfrac23$, $\Gamma_L = 0$; 3 μs and 1.5 μs. (b) $h_L = \tfrac16\sum_n(-\tfrac16)^n\delta(t-4.5-6n)$, $t$ in μs. (c) $-\tfrac73\sin2\pi t$ V, then $-\tfrac{35}{18}\sin2\pi t$ V; 200 m and 300 m. (d) 2 V at 1 MHz, 2.8 V at 1.25 MHz: the line-1 round trip is a whole number of periods in the first case and an odd number of half periods in the second.

### Sources for this page
Kudeki notes, Lecture 30: the junction coefficients, Example 1 (line parameters, 30.4), Example 2 (impulse response and switched-on sine, 30.12), Example 3 (shunt resistor, 30.6, 30.11) and the series-resistor exercise (30.7), all with new numbers. Past exams, re-parameterized: SP18 Exam 3 #1(vii) (30.3), FA23 Exam 3 #3(a) (30.8), SP19 Exam 3 #4 (30.9), FA23 Exam 3 #4 (30.10). The rest is original. Every number is checked by `practice/checks/L30.py`: junction coefficients and power splits by solving KVL/KCL directly, and every bounce diagram by an independent FDTD simulation of the telegrapher's equations with lumped resistors.

*Previous: [[practice/29-bounce-diagram-examples|Lecture 29 practice]] · [[practice/index|all practice]]*
