---
title: "Practice — Lecture 33: Half- and quarter-wave transformers"
description: "8 practice problems (4 easy, 2 medium, 2 hard) on lines whose length is a multiple of a quarter wavelength: Z_in = Z₀²/Z_L and Z_in = Z_L, current forcing, the divider that must come first, a quarter-wave matching section, chaining the two rules with a complex load, two loads fed from one point, one line at three frequencies, and a quarter-wave line with a stub across its load; hints on the medium and hard ones, a worked solution for each."
tags: [practice, transmission-lines]
lecture: 33
---

*Practice for [[4-transmission-lines/33-half-wave-and-quarter-wave-transformers|Lecture 33]] · concepts: [[concepts/quarter-wave-transformer]] · [[concepts/stub-input-impedance]] · all practice: [[practice/index|hub]] · by difficulty: [[practice/easy|easy]] · [[practice/medium|medium]] · [[practice/hard|hard]] · [[practice/topics|by topic]]*

*After the scope of FA26 Midterm 3, which covers Lectures 1–30 ([[exams/index#the-scope|scope]]).*

Work each problem on paper first. Open the **hint** only when stuck, and the **solution** only after you have an answer you would hand in. Every answer here has been checked numerically.

The page runs on two rules (load at $d = 0$, input at $d = \ell$):
- **Quarter wave:** $Z_{\text{in}} = Z_0^2/Z_L$, $\tilde I_L = -j\tilde V_{\text{in}}/Z_0$, $\tilde V_L = Z_L\tilde I_L = -jZ_0\tilde I_{\text{in}}$.
- **Half wave:** $Z_{\text{in}} = Z_L$, $\tilde V_{\text{in}} = -\tilde V_L$, $\tilde I_{\text{in}} = -\tilde I_L$.

Chain them for $3\lambda/4$, $\lambda$, …. Average power: $\tfrac12\text{Re}\{\tilde V\tilde I^*\}$, the same at the input and at the load of a lossless line.

## Easy

### 33.1 Five inputs

> [!easy] Easy · quarter-wave transformer · half-wave transformer
> A lossless line has $Z_0 = 75\ \Omega$. Find $Z_{\text{in}}$ for
> (a) $\ell = \lambda/4$, $Z_L = 25\ \Omega$; (b) $\ell = \lambda/2$, $Z_L = 25\ \Omega$; (c) $\ell = \lambda/4$, $Z_L = j75\ \Omega$; (d) $\ell = 3\lambda/4$, $Z_L = 150\ \Omega$; (e) $\ell = \lambda/4$, $Z_L = 75+j75\ \Omega$.
>
> *Source: original.*

> [!solution]- Solution
> (a) $75^2/25 = 225\ \Omega$. (b) $25\ \Omega$: a half wave repeats the load. (c) $75^2/j75 = -j75\ \Omega$: an inductor looks like a capacitor. (d) $3\lambda/4$ is a half wave (repeat) plus a quarter wave (invert): $75^2/150 = 37.5\ \Omega$. (e) $75^2/(75+j75) = 75/(1+j) = 37.5-j37.5\ \Omega$.
>
> **Answer.** (a) 225 Ω. (b) 25 Ω. (c) $-j75\ \Omega$. (d) 37.5 Ω. (e) $37.5-j37.5\ \Omega$.

### 33.2 Transformer facts, true or false

> [!easy] Easy · true or false · quarter-wave transformer
> True or false, for lossless lines in sinusoidal steady state?
> (a) A half-wave line's input impedance equals its load impedance, whatever $Z_0$ is.
> (b) A quarter-wave line turns a capacitive load into an inductive input impedance.
> (c) $Z_{\text{in}} = Z_0^2/Z_L$ holds for a line of any length if the load is a resistor.
> (d) On a quarter-wave line, the load current is set by the input voltage and $Z_0$, not by the load.
> (e) On a half-wave line, $\lvert\tilde V_L\rvert = \lvert\tilde V_{\text{in}}\rvert$.
> (f) A quarter-wave line with $Z_L = Z_0$ has $\lvert\tilde V_L\rvert = \lvert\tilde V_{\text{in}}\rvert$.
>
> *Source: original.*

> [!solution]- Solution
> (a) **True**: $e^{\pm j\pi} = -1$ multiplies both waves, and $Z_0$ cancels in the ratio.
> (b) **True**: $Z_0^2/(-jX) = +jZ_0^2/X$.
> (c) **False**: only at odd multiples of $\lambda/4$. At a half wave it is $Z_L$; in between, neither.
> (d) **True**: $\tilde I_L = -j\tilde V_{\text{in}}/Z_0$.
> (e) **True**: $\tilde V_{\text{in}} = -\tilde V_L$.
> (f) **True**: $\tilde V_L = Z_0\tilde I_L = -j\tilde V_{\text{in}}$. A matched line only delays.
>
> **Answer.** True, true, false, true, true, true.

### 33.3 The forgotten divider

> [!easy] Easy · find the error · current forcing
> A source $\tilde V_g = 12\angle0^\circ$ V with internal resistance $R_g = 50\ \Omega$ drives a 100 Ω load through a quarter-wave line with $Z_0 = 50\ \Omega$. A student writes: "Current forcing: $\tilde I_L = -j\tilde V_g/Z_0 = -j0.24$ A."
> Find the error, then find $\tilde I_L$, $\tilde V_L$ and the load power.
>
> *Source: original.*

> [!solution]- Solution
> Current forcing uses the voltage **at the line's input**, not the source's open-circuit voltage. Part of $\tilde V_g$ drops across $R_g$.
>
> $Z_{\text{in}} = 50^2/100 = 25\ \Omega$. Divider: $\tilde V_{\text{in}} = 12\cdot\tfrac{25}{25+50} = 4$ V. Then $\tilde I_L = -j4/50 = -j0.08$ A and $\tilde V_L = 100\,\tilde I_L = -j8$ V.
>
> $P_L = \tfrac12(0.08)^2(100) = 0.32$ W. Check at the input: $\tfrac12(4)(4/25) = 0.32$ W ✓.
>
> **Answer.** Use $\tilde V_{\text{in}} = 4$ V: $\tilde I_L = -j0.08$ A, $\tilde V_L = -j8$ V, $P_L = 0.32$ W.

### 33.4 Choosing a matching section

> [!easy] Easy · quarter-wave transformer · impedance matching
> An antenna that looks like $112.5\ \Omega$ at 300 MHz is fed from a 50 Ω line.
> (a) Without matching, what fraction of the incident power is reflected at the antenna?
> (b) What characteristic impedance must a quarter-wave matching section have?
> (c) The section is built from line with $v = 2\times10^8$ m/s. How long is it?
>
> *Source: original.*

> [!solution]- Solution
> (a) $\Gamma_L = (112.5-50)/(112.5+50) = 0.385$; reflected fraction $\Gamma_L^2 = 0.148$, about 15 %.
>
> (b) The section must turn 112.5 Ω into 50 Ω: $Z_q^2/112.5 = 50$, $Z_q = \sqrt{50\times112.5} = 75\ \Omega$.
>
> (c) $\lambda = v/f = 0.667$ m on the section, so $\ell = \lambda/4 = 16.7$ cm.
>
> **Answer.** (a) 14.8 %. (b) 75 Ω. (c) 16.7 cm.

## Medium

### 33.5 Five quarter waves and a complex load

> [!medium] Medium · quarter-wave transformer · half-wave transformer
> A load $Z_L = 30+j40\ \Omega$ ends a lossless 50 Ω line of length $\ell = 1.25\lambda$. The source at the input has $\tilde V_g = 60\angle0^\circ$ V and internal impedance $Z_g = 30+j40\ \Omega$.
> (a) Find $Z_{\text{in}}$.
> (b) Find $\tilde V_{\text{in}}$ and $\tilde I_{\text{in}}$.
> (c) Find $\tilde I_L$ and $\tilde V_L$.
> (d) Find the power delivered to the load, and compare it with the most this source can deliver to any load.
>
> *Source: Kudeki notes, Lecture 33, Example 3 style, re-parameterized: a complex load and source impedance, five quarter waves, and the power comparison.*

> [!hint]- Hint
> $1.25\lambda$ is two half waves and a quarter wave. Two half waves change nothing, sign included. $\lvert30+j40\rvert = 50$.

> [!solution]- Solution
> **(a)** A full wavelength repeats the load; the last quarter wave inverts it:
> $$
> Z_{\text{in}} = \frac{50^2}{30+j40} = \frac{2500(30-j40)}{2500} = 30-j40\ \Omega .
> $$
>
> **(b)** $Z_g+Z_{\text{in}} = 60\ \Omega$, so $\tilde I_{\text{in}} = 60/60 = 1\angle0^\circ$ A and $\tilde V_{\text{in}} = Z_{\text{in}}\tilde I_{\text{in}} = 30-j40$ V.
>
> **(c)** One wavelength toward the load the voltage is the same, $\tilde V(\lambda/4) = 30-j40$ V (two sign flips). Current forcing over the last quarter wave:
> $$
> \tilde I_L = -j\frac{30-j40}{50} = -0.8-j0.6\ \text{A},\qquad \tilde V_L = (30+j40)(-0.8-j0.6) = -j50\ \text{V}.
> $$
>
> **(d)** $P_L = \tfrac12\lvert\tilde I_L\rvert^2R_L = \tfrac12(1)(30) = 15$ W. The source's available power is $\lvert\tilde V_g\rvert^2/8R_g = 3600/240 = 15$ W: the line presents $Z_{\text{in}} = Z_g^*$, a conjugate match, so the load gets all of it.
>
> **Check:** at the input, $\tfrac12\text{Re}\{(30-j40)(1)\} = 15$ W ✓. Also $\tilde V_L = -jZ_0\tilde I(\lambda/4)$ with $\tilde I(\lambda/4) = 1$ A gives $-j50$ V ✓.
>
> **Answer.** (a) $30-j40\ \Omega$. (b) $30-j40$ V, $1\angle0^\circ$ A. (c) $\tilde I_L = -0.8-j0.6$ A, $\tilde V_L = -j50$ V. (d) 15 W, equal to the available power.

### 33.6 Two loads from one point

> [!medium] Medium · current forcing · quarter-wave transformer
> Two quarter-wave lines are connected in parallel at their inputs, where $\tilde V_{\text{in}} = 10\angle0^\circ$ V. Line 1 has $Z_{01} = 50\ \Omega$ and ends in $Z_{L1} = 25\ \Omega$; line 2 has $Z_{02} = 100\ \Omega$ and ends in $Z_{L2} = 200\ \Omega$.
> (a) Find both load currents and load voltages.
> (b) Find the power in each load.
> (c) Find the total input current, and check the power at the input.
> (d) What $Z_{02}$ would give the two loads equal currents?
>
> *Source: Kudeki notes, Lecture 33, Example 4 style, re-parameterized: unequal lines, new loads, the input check and part (d).*

> [!hint]- Hint
> Each line forces its own current, $-j\tilde V_{\text{in}}/Z_0$. For (c), each line shows $Z_0^2/Z_L$ at the input.

> [!solution]- Solution
> **(a)** $\tilde I_{L1} = -j10/50 = -j0.2$ A, $\tilde V_{L1} = 25\tilde I_{L1} = -j5$ V. $\tilde I_{L2} = -j10/100 = -j0.1$ A, $\tilde V_{L2} = 200\tilde I_{L2} = -j20$ V.
>
> **(b)** $P_1 = \tfrac12(0.2)^2(25) = 0.5$ W, $P_2 = \tfrac12(0.1)^2(200) = 1$ W.
>
> **(c)** $Z_{\text{in},1} = 50^2/25 = 100\ \Omega$ and $Z_{\text{in},2} = 100^2/200 = 50\ \Omega$: $\tilde I_{\text{in}} = 10/100+10/50 = 0.3$ A. $P_{\text{in}} = \tfrac12(10)(0.3) = 1.5$ W $= P_1+P_2$ ✓.
>
> **(d)** The forced current is $\tilde V_{\text{in}}/Z_0$ in size, so equal currents need equal $Z_0$: $Z_{02} = 50\ \Omega$, whatever the loads are.
>
> **Answer.** (a) $-j0.2$ A, $-j5$ V; $-j0.1$ A, $-j20$ V. (b) 0.5 W and 1 W. (c) 0.3 A; 1.5 W. (d) 50 Ω.

## Hard

### 33.7 One line at three frequencies

> [!hard] Hard · quarter-wave transformer · half-wave transformer · impedance matching
> A source $\tilde V_g = 10\angle0^\circ$ V with $R_g = 50\ \Omega$ feeds a load $R_L = 200\ \Omega$ through a lossless line with $Z_0 = 100\ \Omega$ that is a quarter wavelength long at $f_0 = 100$ MHz.
> (a) At $f_0$: find $Z_{\text{in}}$, $\tilde V_{\text{in}}$, $\tilde I_L$, $\tilde V_L$ and $P_L$.
> (b) At $2f_0$: find $Z_{\text{in}}$, $\tilde V_L$ and $P_L$.
> (c) At $3f_0$: find $Z_{\text{in}}$, $\tilde I_L$, $\tilde V_L$ and $P_L$.
> (d) Compare with connecting the load directly to the source.
>
> *Source: SP18 Exam 3 #4(b) style, re-parameterized: a matching section between a resistive source and load, three frequencies, and the load power.*

> [!hint]- Hint
> The length in wavelengths scales with frequency: $\lambda/4$, $\lambda/2$, $3\lambda/4$. For (c), use the half-wave rule first to reach the point a quarter wave from the load.

> [!solution]- Solution
> **(a)** $Z_{\text{in}} = 100^2/200 = 50\ \Omega$, equal to $R_g$. $\tilde V_{\text{in}} = 10\cdot\tfrac{50}{100} = 5$ V. $\tilde I_L = -j5/100 = -j0.05$ A, $\tilde V_L = 200\tilde I_L = -j10$ V, $P_L = \tfrac12(0.05)^2(200) = 0.25$ W. That is the source's available power, $10^2/(8\cdot50)$.
>
> **(b)** The line is $\lambda/2$: $Z_{\text{in}} = 200\ \Omega$. $\tilde V_{\text{in}} = 10\cdot\tfrac{200}{250} = 8$ V, $\tilde V_L = -8$ V, $P_L = \tfrac12(8)^2/200 = 0.16$ W.
>
> **(c)** The line is $3\lambda/4$: $Z_{\text{in}} = 50\ \Omega$ again and $\tilde V_{\text{in}} = 5$ V. Half a wave toward the load the voltage is $-5$ V; current forcing over the last quarter wave gives $\tilde I_L = -j(-5)/100 = +j0.05$ A, $\tilde V_L = +j10$ V, $P_L = 0.25$ W. Same power as (a), opposite sign of the load phasors.
>
> **(d)** Direct connection: $\tilde V_L = 10\cdot\tfrac{200}{250} = 8$ V and $P_L = 0.16$ W at every frequency, the same as the half-wave case. The section raises the power to 0.25 W, but only near $f_0$, $3f_0$, $5f_0$, …
>
> **Check:** in (a) $\lvert\tilde V_L\rvert = 10$ V is larger than $\lvert\tilde V_{\text{in}}\rvert = 5$ V. No contradiction: the load current is smaller by the same factor.
>
> **Answer.** (a) 50 Ω, 5 V, $-j0.05$ A, $-j10$ V, 0.25 W. (b) 200 Ω, $-8$ V, 0.16 W. (c) 50 Ω, $+j0.05$ A, $+j10$ V, 0.25 W. (d) 8 V and 0.16 W directly; the section gains a factor 1.56 at $f_0$.

### 33.8 A quarter-wave line with a stub across its load

> [!hard] Hard · quarter-wave transformer · stub input impedance
> A 100 Ω resistor has a shorted stub of length $\lambda/8$ connected across it. The pair is fed through a quarter-wave line. Stub and line both have $Z_0 = 50\ \Omega$. The source has $\tilde V_g = 10\angle0^\circ$ V and $R_g = 25\ \Omega$.
> (a) Find the stub's impedance and the total load admittance $Y_L$.
> (b) Find $Z_{\text{in}}$ of the quarter-wave line.
> (c) Find $\tilde V_{\text{in}}$ and $\tilde I_{\text{in}}$.
> (d) Find the voltage across the resistor and the power it dissipates.
> (e) Check the power at the input.
>
> *Source: original; combines Lectures 32 and 33.*

> [!hint]- Hint
> Parallel elements: add admittances. For the quarter-wave line $Z_{\text{in}} = Z_0^2Y_L$. The load voltage follows from the input **current**: $\tilde V_L = -jZ_0\tilde I_{\text{in}}$.

> [!solution]- Solution
> **(a)** Stub: $j50\tan45^\circ = j50\ \Omega$. $Y_L = \tfrac1{100}+\tfrac1{j50} = 0.01-j0.02$ S.
>
> **(b)** $Z_{\text{in}} = Z_0^2/Z_L = Z_0^2Y_L = 2500(0.01-j0.02) = 25-j50\ \Omega$. The inductive stub appears as a series capacitance.
>
> **(c)** $\tilde I_{\text{in}} = \dfrac{10}{25+25-j50} = \dfrac{10}{50(1-j)} = 0.1+j0.1$ A. $\tilde V_{\text{in}} = Z_{\text{in}}\tilde I_{\text{in}} = (25-j50)(0.1+j0.1) = 7.5-j2.5$ V.
>
> **(d)** $\tilde V_L = -jZ_0\tilde I_{\text{in}} = -j50(0.1+j0.1) = 5-j5$ V, with $\lvert\tilde V_L\rvert^2 = 50$. Only the resistor dissipates: $P = \tfrac12\lvert\tilde V_L\rvert^2/100 = 0.25$ W.
>
> **(e)** $P_{\text{in}} = \tfrac12\text{Re}\{\tilde V_{\text{in}}\tilde I_{\text{in}}^*\} = \tfrac12\text{Re}\{(7.5-j2.5)(0.1-j0.1)\} = \tfrac12(0.75-0.25) = 0.25$ W ✓.
>
> **Check:** current forcing gives the total current into the load pair, $-j\tilde V_{\text{in}}/Z_0 = -0.05-j0.15$ A, and $Y_L\tilde V_L = (0.01-j0.02)(5-j5) = -0.05-j0.15$ A ✓.
>
> **Answer.** (a) $j50\ \Omega$; $0.01-j0.02$ S. (b) $25-j50\ \Omega$. (c) $7.5-j2.5$ V, $0.1+j0.1$ A. (d) $5-j5$ V, 0.25 W. (e) 0.25 W.

### Sources for this page
Kudeki notes, Lecture 33: the two transformer rules and the current-forcing equation, Example 3 (33.5) and Example 4 (33.6), with new numbers and added parts. Past exams, re-parameterized: SP18 Exam 3 #4(b) (33.7). The rest is original. Every number is checked by `practice/checks/L33.py` and re-solved independently in `practice/review/R33.py` (time-domain simulation of the line for the resistive cases, a lumped-ladder model for the complex ones).

*Previous: [[practice/32-stubs-and-input-impedance|Lecture 32 practice]] · [[practice/index|all practice]]*
