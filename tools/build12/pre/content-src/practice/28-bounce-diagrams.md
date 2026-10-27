---
title: "Practice — Lecture 28: Distributed circuits and bounce diagrams"
description: "12 practice problems (5 easy, 3 medium, 4 hard) on a line between a Thévenin generator and a resistive load: τ_g, Γ_g, Γ_L and the current coefficients, a step meeting open, shorted, matched and resistive loads, arrival times at a point, voltage and current bounce diagrams for step, pulse and impulse sources, snapshots along a shorted line, reflectometry, the ideal source, an energy ledger, the DC limit, and an open line that charges like a capacitor; hints on the medium and hard ones, a worked solution for each."
tags: [practice, transmission-lines]
lecture: 28
---

*Practice for [[4-transmission-lines/28-distributed-circuits-and-bounce-diagrams|Lecture 28]] · concepts: [[concepts/bounce-diagram]] · [[concepts/characteristic-impedance]] · [[concepts/reflection-and-transmission]] · all practice: [[practice/index|hub]] · by difficulty: [[practice/easy|easy]] · [[practice/medium|medium]] · [[practice/hard|hard]] · [[practice/topics|by topic]]*

Work each problem on paper first. Open the **hint** only when stuck, and the **solution** only after you have an answer you would hand in. Every answer here has been checked numerically, bounce diagrams by a time-domain simulation of the line.

Lecture 28's conventions throughout: generator at $z = 0$, load at $z = \ell$, $T = \ell/v$.
- $\tau_g = \dfrac{Z_0}{R_g+Z_0}$, $\Gamma_g = \dfrac{R_g-Z_0}{R_g+Z_0}$, $\Gamma_L = \dfrac{R_L-Z_0}{R_L+Z_0}$; for current the ratios are $-\Gamma$.
- Forward segment $n$: weight $\tau_g(\Gamma_L\Gamma_g)^n$, passes $z$ at $z/v+2nT$. Backward segment $n$: weight $\tau_g\Gamma_L(\Gamma_L\Gamma_g)^n$, passes $z$ at $2T-z/v+2nT$.
- Forward waves carry $I = +V/Z_0$, backward waves $I = -V/Z_0$.
- Step $V_0u(t)$: $V_0$ times the running sum of weights, ending at $V_0R_L/(R_g+R_L)$ and $V_0/(R_g+R_L)$.

## Easy

### 28.1 Three coefficients

> [!easy] Easy · generator reflection coefficient · load reflection coefficient
> A line with $Z_0 = 60\ \Omega$ is driven at $z = 0$ by $16u(t)$ V behind $R_g = 20\ \Omega$ and terminated at $z = \ell$ by $R_L = 180\ \Omega$.
>
> (a) Find $\tau_g$, $\Gamma_g$, $\Gamma_L$, and the current reflection coefficients at both ends.
>
> (b) Find the voltage and current of the first forward wave.
>
> *Source: SP17 Exam 3 #5a style, new resistors.*

> [!solution]- Solution
> (a)
> $$
> \tau_g = \frac{60}{20+60} = \frac34,\qquad \Gamma_g = \frac{20-60}{20+60} = -\frac12,\qquad \Gamma_L = \frac{180-60}{180+60} = \frac12 .
> $$
> Current ratios are $-\Gamma$: $-\tfrac12$ at the load, $+\tfrac12$ at the generator.
>
> (b) Until the first echo returns, the line acts as a resistor $Z_0$: $V^+ = 16\cdot\tfrac34 = 12$ V, $I^+ = 12/60 = 0.2$ A.
>
> **Check:** $\tau_g = (1-\Gamma_g)/2 = \tfrac34$ ✓; KVL: $16-0.2\cdot20 = 12$ V ✓.
>
> **Answer.** $\tau_g = 3/4$, $\Gamma_g = -1/2$, $\Gamma_L = +1/2$; current coefficients $-1/2$ (load) and $+1/2$ (generator); first wave 12 V, 0.2 A.

### 28.2 Line conventions

> [!easy] Easy · true or false · characteristic impedance
> A lossless line $Z_0$ joins a Thévenin source ($f_i$ behind $R_g$) at $z = 0$ to a resistor $R_L$ at $z = \ell$. True or false?
>
> (a) $V(z,t)/I(z,t) = Z_0$ at every point and time.
>
> (b) A wave travelling toward $-z$ carries $I = -V/Z_0$.
>
> (c) Doubling the source voltage doubles $\Gamma_g$.
>
> (d) If $R_g = 0$, then $V(0,t) = f_i(t)$ at all times, whatever $R_L$ is.
>
> (e) $\tau_g = 1+\Gamma_g$.
>
> *Source: SP18 Exam 3 #1(v) style, extended.*

> [!solution]- Solution
> (a) **False.** $V/I = Z_0\,(f+g)/(f-g)$ equals $Z_0$ only while $g = 0$: one forward wave, no echo yet.
>
> (b) **True.** $g$ enters $I = (f-g)/Z_0$ with a minus sign.
>
> (c) **False.** $\Gamma_g = (R_g-Z_0)/(R_g+Z_0)$ contains resistances only; the source enters through $\tau_g$.
>
> (d) **True.** KVL: $V(0,t) = f_i(t)-R_gI(0,t) = f_i(t)$. Each returning wave meets $\Gamma_g = -1$, and the two cancel at $z = 0$.
>
> (e) **False.** $\tau_g = Z_0/(R_g+Z_0) = (1-\Gamma_g)/2$. For $R_g = 3Z_0$: $\tau_g = \tfrac14$, but $1+\Gamma_g = \tfrac32$.
>
> **Answer.** (a) F, (b) T, (c) F, (d) T, (e) F.

### 28.3 A step meets four loads

> [!easy] Easy · load reflection coefficient · transients
> A forward voltage step of 6 V travels toward the load on a $50\ \Omega$ line. For each load — open, short, $50\ \Omega$, $25\ \Omega$ — find $\Gamma_L$, the reflected voltage, and the load voltage and current just after the step arrives.
>
> *Source: original.*

> [!solution]- Solution
> Incident current $6/50 = 0.12$ A. At the load the arriving and reflected steps cross together: $V_L = (1+\Gamma_L)\,6$ V, $I_L = (1-\Gamma_L)\,0.12$ A.
>
> | load | $\Gamma_L$ | reflected | $V_L$ | $I_L$ |
> |---|---|---|---|---|
> | open | $+1$ | $+6$ V | 12 V | 0 |
> | short | $-1$ | $-6$ V | 0 | 0.24 A |
> | $50\ \Omega$ | $0$ | 0 | 6 V | 0.12 A |
> | $25\ \Omega$ | $-1/3$ | $-2$ V | 4 V | 0.16 A |
>
> **Check:** $V_L/I_L = R_L$: $6/0.12 = 50$, $4/0.16 = 25$ ✓.
>
> **Watch out:** the open end doubles the voltage, the short doubles the current.
>
> **Answer.** Open: $\Gamma_L = 1$, $+6$ V, 12 V, 0 A. Short: $-1$, $-6$ V, 0 V, 0.24 A. $50\ \Omega$: 0, none, 6 V, 0.12 A. $25\ \Omega$: $-1/3$, $-2$ V, 4 V, 0.16 A.

### 28.4 Arrival times at a point

> [!easy] Easy · multiple choice · bounce diagram
> A line with $\ell = 300$ m and $v = 200$ m/μs has mismatched resistors at both ends and is driven by $\delta(t)$. At $z = 100$ m the first four impulses arrive at
>
> (a) 0.5, 2.5, 3.5, 5.5 μs
>
> (b) 0.5, 2.0, 3.5, 5.0 μs
>
> (c) 0.5, 3.5, 6.5, 9.5 μs
>
> (d) 0.5, 3.0, 3.5, 6.0 μs
>
> *Source: original.*

> [!solution]- Solution
> $T = 300/200 = 1.5$ μs, $z/v = 0.5$ μs. Forward crossings $z/v+2nT$: 0.5, 3.5, 6.5 μs. Backward crossings $2T-z/v+2nT$: 2.5, 5.5 μs. In order: **(a)**.
>
> (b) Equal spacing $T$: wrong, because forward and backward crossings at $z\neq\ell/2$ are unevenly spaced.
>
> (c) Forward segments only: misses the backward ones.
>
> (d) Backward crossings at $2T+2nT$: that is when they reach $z = 0$, not $z = 100$ m.
>
> **Answer.** (a): 0.5, 2.5, 3.5, 5.5 μs.

### 28.5 A launched wave too big

> [!easy] Easy · find the error · bounce diagram
> A $10u(t)$ V source with $R_g = 75\ \Omega$ drives a $50\ \Omega$ line terminated by $R_L = 200\ \Omega$. A student writes:
>
> "$\Gamma_g = \dfrac{75-50}{75+50} = 0.2$, so $\tau_g = 1+\Gamma_g = 1.2$ and the first wave is 12 V. $\Gamma_L = \dfrac{150}{250} = 0.6$, so $V(\ell,t) = 1.6\times12 = 19.2$ V for $T<t<3T$."
>
> Find the error and correct the result.
>
> *Source: original.*

> [!solution]- Solution
> **Slip:** $\tau_g = 1+\Gamma$ is Lecture 25's interface coefficient. The generator launches by voltage division with the line acting as $Z_0$:
> $$
> \tau_g = \frac{Z_0}{R_g+Z_0} = \frac{50}{125} = 0.4 = \frac{1-\Gamma_g}{2}.
> $$
> First wave $10\times0.4 = 4$ V; $V(\ell,t) = 1.6\times4 = 6.4$ V for $T<t<3T$. $\Gamma_g = 0.2$ and $\Gamma_L = 0.6$ were right.
>
> **Check:** $\tau_g\le1$ for any $R_g\ge0$, so the first wave can never exceed the source voltage; 12 V from a 10 V source is the red flag. The load voltage then settles to $10\cdot200/275 = 7.27$ V.
>
> **Answer.** $\tau_g = 0.4$, not 1.2: the first wave is 4 V and $V(\ell,t) = 6.4$ V for $T<t<3T$.

## Medium

### 28.6 Ideal source, mismatched load

> [!medium] Medium · bounce diagram · steady state
> An ideal source $20u(t)$ V ($R_g = 0$) drives an air line with $Z_0 = 100\ \Omega$, $\ell = 150$ m, $v = 300$ m/μs, terminated by $R_L = 300\ \Omega$.
>
> (a) Find $\tau_g$, $\Gamma_g$, $\Gamma_L$ and the voltage weights of the first four segments.
>
> (b) Find $V(\ell,t)$ for $0<t<4.5$ μs.
>
> (c) Find $I(0,t)$ for $0<t<4$ μs.
>
> (d) Find $V(0,t)$ and the DC limits of $V$ and $I$.
>
> *Source: original.*

> [!hint]- Hint
> $T = 0.5$ μs. At an end, the arriving segment and its reflection cross together: add both weights for $V$; for $I$, the backward one counts with a minus sign.

> [!solution]- Solution
> **Setup.** $\tau_g = 1$, $\Gamma_g = -1$, $\Gamma_L = \tfrac{300-100}{400} = \tfrac12$, $\Gamma_L\Gamma_g = -\tfrac12$.
>
> (a) Multiply by $\Gamma_L$, then $\Gamma_g$: 20, 10, $-10$, $-5$ V.
>
> (b) Forward weights reach the load at $T, 3T, 5T, 7T$: 20, $-10$, 5, $-2.5$ V. Each adds $(1+\Gamma_L)w = 1.5w$:
>
> | $t$ (μs) | 0–0.5 | 0.5–1.5 | 1.5–2.5 | 2.5–3.5 | 3.5–4.5 |
> |---|---|---|---|---|---|
> | $V(\ell,t)$ (V) | 0 | 30 | 15 | 22.5 | 18.75 |
>
> (c) Start: $I = 20/100 = 0.2$ A. A backward weight $w$ arriving at $z = 0$ and its reflection $-w$ each carry $-w/Z_0$: jump $-2w/Z_0$, with $w = 10$, $-5$, $2.5$ V at $t = 1, 2, 3$ μs:
>
> | $t$ (μs) | 0–1 | 1–2 | 2–3 | 3–4 |
> |---|---|---|---|---|
> | $I(0,t)$ (A) | 0.2 | 0 | 0.1 | 0.05 |
>
> (d) KVL with $R_g = 0$: $V(0,t) = 20$ V at all $t>0$. DC: $V = 20$ V, $I = 20/300 = 66.7$ mA. Both staircases oscillate around these values ($\Gamma_L\Gamma_g<0$).
>
> **Check:** $V(\ell)/R_L = 0.1, 0.05, 0.075$ A, closing on 66.7 mA from both sides, like $I(0,t)$.
>
> **Answer.** Weights 20, 10, $-10$, $-5$ V. $V(\ell,t)$: 0, 30, 15, 22.5, 18.75 V. $I(0,t)$: 0.2, 0, 0.1, 0.05 A. $V(0,t) = 20$ V always; DC 20 V and 66.7 mA.

### 28.7 Reflectometry with a matched source

> [!medium] Medium · load reflection coefficient · transients
> To test a buried cable ($Z_0 = 50\ \Omega$, $v = 200$ m/μs) of unknown length, you connect $12u(t)$ V behind $R_g = 50\ \Omega$ to its near end ($z = 0$) and record $V(0,t)$: 6 V for $0<t<2.4$ μs, then 8 V for all later times.
>
> (a) Find the cable length.
>
> (b) Find $\Gamma_L$ and the resistance $R_L$ at the far end.
>
> (c) What would the record be if the far end were (i) $25\ \Omega$, (ii) a short?
>
> *Source: classic (time-domain reflectometry).*

> [!hint]- Hint
> With $R_g = Z_0$ the generator absorbs every echo, so the record holds the first wave and exactly one echo. The jump is $\Gamma_L$ times the first wave; 2.4 μs is a round trip.

> [!solution]- Solution
> **Setup.** $\tau_g = \tfrac12$, $\Gamma_g = 0$: the first wave is 6 V; one echo $6\Gamma_L$ returns at $2T$ and is absorbed.
>
> (a) $2T = 2.4$ μs, so $T = 1.2$ μs and $\ell = vT = 240$ m.
>
> (b) $6\Gamma_L = 8-6$, so $\Gamma_L = \tfrac13$ and
> $$
> R_L = Z_0\,\frac{1+\Gamma_L}{1-\Gamma_L} = 50\cdot\frac{4/3}{2/3} = 100\ \Omega .
> $$
>
> (c) (i) $\Gamma_L = (25-50)/75 = -\tfrac13$: 6 V, then 4 V after 2.4 μs. (ii) $\Gamma_L = -1$: 6 V, then 0.
>
> **Check:** with $\Gamma_g = 0$ the record is final after $2T$, so it must equal the DC divider: $12\cdot100/150 = 8$ V ✓, $12\cdot25/75 = 4$ V ✓, short 0 V ✓.
>
> **Answer.** $\ell = 240$ m; $\Gamma_L = 1/3$, $R_L = 100\ \Omega$; (i) 6 V then 4 V, (ii) 6 V then 0 V, the step at 2.4 μs.

### 28.8 Snapshots along a shorted line

> [!medium] Medium · bounce diagram · transients
> A $16u(t)$ V source with $R_g = 30\ \Omega$ drives a $50\ \Omega$ line, $\ell = 400$ m, $v = 200$ m/μs, short-circuited at $z = \ell$.
>
> (a) Find $V(z)$ and $I(z)$ along the whole line at $t = 3$ μs.
>
> (b) The same at $t = 5$ μs.
>
> (c) Find $V$ and $I$ as $t\to\infty$.
>
> *Source: SP17 Exam 3 #5c style, step source and a shorted load.*

> [!hint]- Hint
> A snapshot is a horizontal line across the bounce diagram. A segment that left an end at $t_0$ is $v(t-t_0)$ from that end. At each $z$, add the weights of the segments that have already passed it.

> [!solution]- Solution
> **Setup.** $T = 2$ μs; $\tau_g = \tfrac{50}{80} = \tfrac58$, $\Gamma_g = \tfrac{30-50}{80} = -\tfrac14$, $\Gamma_L = -1$. Voltage weights 10, $-10$, 2.5 V; currents $+0.2$, $+0.2$ (backward: sign flips), $+0.05$ A.
>
> (a) $t = 3$ μs: the $-10$ V echo left the load at 2 μs and is now 200 m back, at $z = 200$ m.
> - $z<200$ m: $V = 10$ V, $I = 0.2$ A.
> - $z>200$ m: $V = 10-10 = 0$, $I = 0.2+0.2 = 0.4$ A.
>
> (b) $t = 5$ μs: the echo reached $z = 0$ at 4 μs; its 2.5 V reflection is now at $z = 200$ m.
> - $z<200$ m: $V = 10-10+2.5 = 2.5$ V, $I = 0.2+0.2+0.05 = 0.45$ A.
> - $z>200$ m: $V = 0$, $I = 0.4$ A.
>
> (c) DC: the short makes $V = 0$ and $I = 16/30 = 0.533$ A at every $z$.
>
> **Check:** $V(\ell) = 0$ in every snapshot (short) ✓; KVL at $z = 0$, $t = 5$ μs: $16-30\times0.45 = 2.5$ V ✓.
>
> **Answer.** $t = 3$ μs: 10 V, 0.2 A for $z<200$ m; 0 V, 0.4 A for $z>200$ m. $t = 5$ μs: 2.5 V, 0.45 A for $z<200$ m; 0 V, 0.4 A beyond. DC: 0 V, 0.533 A.

## Hard

### 28.9 Voltage and current diagrams

> [!hard] Hard · bounce diagram · generator reflection coefficient · steady state
> A line with $Z_0 = 50\ \Omega$, $\ell = 20$ cm and $v = \tfrac23c$ is driven at $z = 0$ by $12u(t)$ V behind $R_g = 25\ \Omega$ and terminated by $R_L = 200\ \Omega$.
>
> (a) Find $\tau_g$, $\Gamma_g$, $\Gamma_L$ and the current reflection coefficients.
>
> (b) Give the voltage and current weight of every segment of the bounce diagrams for $0<t<5$ ns.
>
> (c) Find $V(0,t)$ and $V(\ell,t)$ for $0<t<6$ ns.
>
> (d) Find $V$ and $I$ at $z = 5$ cm, $t = 3.5$ ns.
>
> (e) Find the steady-state load voltage and current; compare with (c).
>
> *Source: SP18 Exam 3 #3a–b, re-parameterized.*

> [!hint]- Hint
> $v = 0.2$ m/ns, so $T = 1$ ns. Current weights are voltage weights over $Z_0$, with the sign flipped on backward segments. At an end, add the arriving and the reflected weight.

> [!solution]- Solution
> **(a)** $\tau_g = \tfrac{50}{75} = \tfrac23$, $\Gamma_g = \tfrac{-25}{75} = -\tfrac13$, $\Gamma_L = \tfrac{150}{250} = 0.6$; current coefficients $-0.6$ (load), $+\tfrac13$ (generator). $\Gamma_L\Gamma_g = -0.2$.
>
> **(b)** First weight $12\cdot\tfrac23 = 8$ V; then $\times0.6$, $\times(-\tfrac13)$ in turn:
>
> | segment | $t$ (ns) | direction | $V$ (V) | $I$ (A) |
> |---|---|---|---|---|
> | 1 | 0–1 | forward | 8 | 0.16 |
> | 2 | 1–2 | backward | 4.8 | $-0.096$ |
> | 3 | 2–3 | forward | $-1.6$ | $-0.032$ |
> | 4 | 3–4 | backward | $-0.96$ | 0.0192 |
> | 5 | 4–5 | forward | 0.32 | 0.0064 |
>
> **(c)** Generator end, changes at $2T, 4T$ (arrival + reflection): $8$; $8+4.8-1.6 = 11.2$; $11.2-0.96+0.32 = 10.56$ V. Load end, $(1+\Gamma_L) = 1.6$ times each arrival: $1.6\times8 = 12.8$; $12.8-1.6\times1.6 = 10.24$; $10.24+1.6\times0.32 = 10.752$ V.
>
> | $t$ (ns) | 0–1 | 1–2 | 2–3 | 3–4 | 4–5 | 5–6 |
> |---|---|---|---|---|---|---|
> | $V(0,t)$ (V) | 8 | 8 | 11.2 | 11.2 | 10.56 | 10.56 |
> | $V(\ell,t)$ (V) | 0 | 12.8 | 12.8 | 10.24 | 10.24 | 10.752 |
>
> **(d)** $z = 5$ cm $= \ell/4$: crossings at 0.25, 1.75, 2.25 ns (segments 1–3) before 3.5 ns; the next is at 3.75 ns.
> $$
> V = 8+4.8-1.6 = 11.2\ \text{V},\qquad I = 0.16-0.096-0.032 = 0.032\ \text{A}.
> $$
>
> **(e)** DC divider: $V_L = 12\cdot\tfrac{200}{225} = 10.67$ V, $I_L = \tfrac{12}{225} = 53.3$ mA. Both staircases in (c) close in on 10.67 V from alternate sides ($\Gamma_L\Gamma_g<0$).
>
> **Check:** at the load $I = 0.4\times0.16 = 0.064$ A on 1–3 ns, and $12.8/0.064 = 200\ \Omega$ ✓. Series: $8\cdot\dfrac{1.6}{1.2} = 10.67$ V ✓.
>
> **Answer.** $\tau_g = 2/3$, $\Gamma_g = -1/3$, $\Gamma_L = 0.6$ (current: $+1/3$, $-0.6$). Weights 8, 4.8, $-1.6$, $-0.96$, 0.32 V and 0.16, $-0.096$, $-0.032$, 0.0192, 0.0064 A. $V(0,t)$: 8, 11.2, 10.56 V; $V(\ell,t)$: 0, 12.8, 10.24, 10.752 V. $V = 11.2$ V, $I = 32$ mA at (5 cm, 3.5 ns). DC: 10.67 V, 53.3 mA.

### 28.10 A pulse into a resistive load

> [!hard] Hard · bounce diagram · transients · steady state
> A source with $R_g = 50\ \Omega$ drives a lossless $50\ \Omega$ line, $\ell = 600$ m, $v = 200$ m/μs, terminated by $R_L = 150\ \Omega$.
>
> (a) For $f_i = 200u(t)$ V, find the steady-state $V(0,t)$ and $I(\ell,t)$.
>
> (b) Now $f_i$ is a 200 V rectangular pulse on $0<t<4$ μs. Find $V(0,t)$ and $I(0,t)$ for $0<t<12$ μs.
>
> (c) Find $V$ and $I$ at the midpoint $z = 300$ m for $0<t<12$ μs.
>
> (d) Show that the energy delivered into the line at $z = 0$ equals the energy absorbed by $R_L$.
>
> *Source: FA23 Exam 3 #5, re-parameterized (resistive load instead of a short).*

> [!hint]- Hint
> $\Gamma_g = 0$, so only two segments ever exist. Slide the whole 4 μs pulse along each segment; where two copies overlap at one $z$, voltages add and currents subtract.

> [!solution]- Solution
> **Setup.** $T = 3$ μs; $\tau_g = \tfrac12$, $\Gamma_g = 0$, $\Gamma_L = \tfrac{100}{200} = \tfrac12$. Forward pulse 100 V (2 A); backward pulse 50 V ($-1$ A), absorbed at $z = 0$.
>
> **(a)** DC divider: $V = 200\cdot\tfrac{150}{200} = 150$ V at every $z$, $I = \tfrac{200}{200} = 1$ A. With $\Gamma_g = 0$ it is reached at $2T = 6$ μs.
>
> **(b)** The forward pulse leaves $z = 0$ on 0–4 μs; the echo returns on $2T$ to $2T+4$ = 6–10 μs.
>
> | $t$ (μs) | 0–4 | 4–6 | 6–10 | 10–12 |
> |---|---|---|---|---|
> | $V(0,t)$ (V) | 100 | 0 | 50 | 0 |
> | $I(0,t)$ (A) | 2 | 0 | $-1$ | 0 |
>
> **(c)** Forward pulse passes $z = 300$ m on 1.5–5.5 μs, the echo on $2T-1.5 = 4.5$ to 8.5 μs; they overlap on 4.5–5.5 μs.
>
> | $t$ (μs) | 0–1.5 | 1.5–4.5 | 4.5–5.5 | 5.5–8.5 | 8.5–12 |
> |---|---|---|---|---|---|
> | $V$ (V) | 0 | 100 | 150 | 50 | 0 |
> | $I$ (A) | 0 | 2 | 1 | $-1$ | 0 |
>
> **(d)** Into the line at $z = 0$: $\int V I\,dt = 100\cdot2\cdot4-50\cdot1\cdot4 = 600$ μJ. At the load: $V_L = 1.5\times100 = 150$ V, $I_L = 0.5\times2 = 1$ A on 3–7 μs, so $150\cdot1\cdot4 = 600$ μJ ✓. The lossless line stores nothing in the end.
>
> **Check:** the source supplies $200\cdot2\cdot4 = 1600$ μJ; $R_g$ takes $2^2\cdot50\cdot4+1^2\cdot50\cdot4 = 1000$ μJ; $1000+600 = 1600$ ✓.
>
> **Watch out:** the echo's voltage is positive but its current is negative; at $z = 0$ it returns 200 μJ to $R_g$.
>
> **Answer.** (a) 150 V, 1 A. (b) $V(0,t)$ = 100 V (0–4 μs), 50 V (6–10 μs), else 0; $I(0,t)$ = 2 A, then $-1$ A. (c) 100, 150, 50 V and 2, 1, $-1$ A on 1.5–4.5, 4.5–5.5, 5.5–8.5 μs. (d) 600 μJ in both.

### 28.11 Impulse response at a third point

> [!hard] Hard · impulse response · bounce diagram · steady state
> A non-magnetic line with $Z_0 = 60\ \Omega$, $\ell = 300$ m and $\epsilon_r = 9$ is driven at $z = 0$ by $f_i = 12\,\delta(t)$ behind $R_g = 20\ \Omega$ and terminated by $R_L = 300\ \Omega$. Time is in μs, so impulse weights are in V·μs. Use $c = 300$ m/μs.
>
> (a) Find $v$, $T$, $\tau_g$, $\Gamma_g$ and $\Gamma_L$.
>
> (b) Write $V(100\ \text{m},t)$ as a sum of weighted impulses for $0<t<14$ μs.
>
> (c) Write $I(100\ \text{m},t)$ for the same window.
>
> (d) Now $f_i = 12u(t)$ V. Find $V(100\ \text{m},t)$ for $0<t<14$ μs and the steady-state $V$ and $I$.
>
> *Source: Summer 2020 final #5, re-parameterized.*

> [!hint]- Hint
> $v = c/\sqrt{\epsilon_r}$. Forward segments cross $z$ at $z/v+2nT$, backward ones at $2T-z/v+2nT$. For the step, each impulse becomes a step of the same weight: take running sums.

> [!solution]- Solution
> **(a)** $v = 300/3 = 100$ m/μs, $T = 3$ μs. $\tau_g = \tfrac{60}{80} = \tfrac34$, $\Gamma_g = \tfrac{-40}{80} = -\tfrac12$, $\Gamma_L = \tfrac{240}{360} = \tfrac23$; $\Gamma_L\Gamma_g = -\tfrac13$.
>
> **(b)** Weights $12\tau_g = 9$, then $\times\tfrac23$, $\times(-\tfrac12)$ in turn: 9, 6, $-3$, $-2$, 1 V·μs. At $z = 100$ m, $z/v = 1$ μs: forward crossings at $1+6n$ = 1, 7, 13 μs; backward at $6-1+6n$ = 5, 11 μs:
> $$
> V(100\ \text{m},t) = 9\,\delta(t-1)+6\,\delta(t-5)-3\,\delta(t-7)-2\,\delta(t-11)+\delta(t-13).
> $$
>
> **(c)** Divide by 60 Ω and flip the backward (5 and 11 μs) signs:
> $$
> I = 0.15\,\delta(t-1)-0.1\,\delta(t-5)-0.05\,\delta(t-7)+0.0333\,\delta(t-11)+0.0167\,\delta(t-13)\ \ \text{A}\cdot\mu\text{s}.
> $$
>
> **(d)** Running sums of (b):
>
> | $t$ (μs) | 0–1 | 1–5 | 5–7 | 7–11 | 11–13 | 13–14 |
> |---|---|---|---|---|---|---|
> | $V$ (V) | 0 | 9 | 15 | 12 | 10 | 11 |
>
> Steady state: $V = 12\cdot\tfrac{300}{320} = 11.25$ V and $I = \tfrac{12}{320} = 37.5$ mA, at every $z$.
>
> **Check:** series $9\cdot\dfrac{1+2/3}{1+1/3} = 11.25$ V ✓. Current running sums 0.15, 0.05, 0, 0.0333, 0.05 A also straddle 37.5 mA.
>
> **Answer.** $v = 100$ m/μs, $T = 3$ μs, $\tau_g = 3/4$, $\Gamma_g = -1/2$, $\Gamma_L = 2/3$. $V = 9\delta(t-1)+6\delta(t-5)-3\delta(t-7)-2\delta(t-11)+\delta(t-13)$ V·μs; $I = 0.15\delta(t-1)-0.1\delta(t-5)-0.05\delta(t-7)+0.0333\delta(t-11)+0.0167\delta(t-13)$ A·μs. Step: 9, 15, 12, 10, 11 V; DC 11.25 V, 37.5 mA.

### 28.12 Open line charges like a capacitor

> [!hard] Hard · bounce diagram · steady state · capacitance
> A $10u(t)$ V source with $R_g = 450\ \Omega$ drives an open-circuited $50\ \Omega$ line, $\ell = 100$ m, $v = 200$ m/μs.
>
> (a) Find $\tau_g$, $\Gamma_g$, $\Gamma_L$ and $V(\ell,t)$ for $0<t<7T$.
>
> (b) Show that $V(\ell,t) = 10(1-0.8^{n+1})$ V for $(2n+1)T<t<(2n+3)T$. When does $V(\ell,t)$ first reach 99 % of its final value?
>
> (c) Model the line as a lumped capacitor $C = \ell\mathcal{C}$ charged through $R_g$. Find $C$, $R_gC$ and the 99 % time of that RC circuit.
>
> (d) Explain why the two pictures agree when $R_g\gg Z_0$.
>
> *Source: original.*

> [!hint]- Hint
> At the open end $V$ jumps by twice each arriving weight, and the forward weights form a geometric series in $\Gamma_g$. For (c), $\mathcal{C} = 1/(Z_0v)$ from Lecture 27.

> [!solution]- Solution
> **(a)** $T = 0.5$ μs. $\tau_g = \tfrac{50}{500} = 0.1$, $\Gamma_g = \tfrac{400}{500} = 0.8$, $\Gamma_L = 1$. Forward weights 1, 0.8, 0.64 V, each doubled on arrival: $V(\ell,t) = 0$ for $t<T$, then 2, 3.6, 4.88 V on $(T,3T)$, $(3T,5T)$, $(5T,7T)$.
>
> **(b)** Forward weight $n$ is $0.8^n$ V, so
> $$
> V(\ell,t) = 2\sum_{k=0}^{n}0.8^k = 2\,\frac{1-0.8^{n+1}}{1-0.8} = 10\big(1-0.8^{n+1}\big).
> $$
> 99 %: $0.8^{n+1}\le0.01$, $n+1\ge\ln100/\ln1.25 = 20.6$, so $n = 20$: $t = 41T = 20.5$ μs.
>
> **(c)** $C = \dfrac{\ell}{Z_0v} = \dfrac{T}{Z_0} = \dfrac{0.5\ \mu\text{s}}{50\ \Omega} = 10$ nF, $R_gC = 4.5$ μs $= 9T$. RC charging $10(1-e^{-t/4.5\,\mu\text{s}})$ reaches 99 % at $4.5\ln100 = 20.7$ μs — within one round trip of (b).
>
> **(d)** Per round trip $2T$, the staircase multiplies the remaining gap by $\Gamma_g$; the RC curve by $e^{-2T/R_gC} = e^{-2Z_0/R_g}$. With $x = Z_0/R_g$:
> $$
> \Gamma_g = \frac{1-x}{1+x} = e^{-2(x+x^3/3+\ldots)}\approx e^{-2x}.
> $$
> Here $0.8$ against $e^{-1/4.5} = 0.8007$. The match needs $x\ll1$: the charging time $R_gC$ spans many round trips, so the line acts as one lumped capacitor.
>
> **Check:** final value $V_0R_L/(R_g+R_L)\to V_0 = 10$ V for an open load ✓.
>
> **Answer.** $\tau_g = 0.1$, $\Gamma_g = 0.8$, $\Gamma_L = 1$; $V(\ell,t)$ = 0, 2, 3.6, 4.88 V; 99 % at $41T = 20.5$ μs. $C = 10$ nF, $R_gC = 4.5$ μs, RC 99 % time 20.7 μs; they agree because $\Gamma_g\approx e^{-2Z_0/R_g}$ for $R_g\gg Z_0$.

### Sources for this page
Course notes, Lecture 28: $\tau_g$, $\Gamma_g$, $\Gamma_L$, the bounce diagram and the impulse-response series, used throughout with new numbers. Old exams, all re-parameterized: SP17 Exam 3 #5a (28.1, new resistors), #5c (28.8: snapshots along the line, now a step into a short); SP18 Exam 3 #1(v) (28.2, extended to five statements) and #3a–b (28.9: new resistors, length and source, plus a point reading and the DC limit); FA23 Exam 3 #5 (28.10: resistive load instead of a short, a midpoint and an energy ledger added); Summer 2020 final #5 (28.11: new line, observed at $\ell/3$). Time-domain reflectometry (28.7) is a classic. Original: 28.3–28.6, 28.12.

*[[practice/index|All practice]]*

*Previous: [[practice/27-transmission-line-basics|Lecture 27 practice]] · next: [[practice/29-bounce-diagram-examples|Lecture 29 practice]] · [[practice/index|all practice]]*
