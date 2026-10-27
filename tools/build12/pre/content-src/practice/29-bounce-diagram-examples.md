---
title: "Practice — Lecture 29: Bounce diagram examples"
description: "12 practice problems (5 easy, 3 medium, 4 hard) on the notes' bounce-diagram examples with new sources: snapshots V(z, t₀) and records V(z₀, t) for pulses, a triangle, sine bursts, a cut-off ramp and a ramped step; which way round a pulse lies, pulses overlapping their own echoes, currents with the backward sign flip, records at both ends of a line, a line read off one probe, which inputs reach a DC limit, and a partial standing wave building up; hints on the medium and hard ones, a worked solution for each."
tags: [practice, transmission-lines]
lecture: 29
---

*Practice for [[4-transmission-lines/29-bounce-diagram-examples|Lecture 29]] · concepts: [[concepts/bounce-diagram]] · [[concepts/characteristic-impedance]] · [[concepts/superposition]] · [[concepts/standing-waves]] · all practice: [[practice/index|hub]] · by difficulty: [[practice/easy|easy]] · [[practice/medium|medium]] · [[practice/hard|hard]] · [[practice/topics|by topic]]*

Work each problem on paper first. Open the **hint** only when stuck, and the **solution** only after you have an answer you would hand in. Every answer here has been checked numerically, each waveform by a time-domain simulation of the line.

[[4-transmission-lines/28-distributed-circuits-and-bounce-diagrams|Lecture 28]]'s conventions; times in μs unless stated.
- Forward segment $n$ (weight $w$) carries $w\,f_i(t-z/v-2nT)$; backward segment $n$ carries $w\,f_i(t+z/v-2(n+1)T)$.
- Record $V(z_p,t)$ (vertical cut): one copy of $f_i$ per crossing. Snapshot $V(z,t_p)$ (horizontal cut): one copy per segment started by $t_p$, including segments the cut has already passed (a copy trails its segment by the input's duration).
- $V$ adds the copies; $Z_0I$ subtracts the backward ones.
- On a snapshot a forward pulse lies reversed (the part sent first is furthest right); an echo lies in source order.

## Easy

### 29.1 Which way round

> [!easy] Easy · multiple choice · bounce diagram
> A 1000 m line ($Z_0 = 50\ \Omega$, $v = 200$ m/μs) has $R_g = 50\ \Omega$ at $z = 0$ and $R_L = 100\ \Omega$ at $z = \ell$. The source's open-circuit voltage is 2 V for $0<t<1$ μs, 6 V for $1<t<2$ μs, and 0 otherwise. Which is $V(z)$ at $t = 3$ μs?
>
> (a) 3 V on 200–400 m, 1 V on 400–600 m, 0 elsewhere.
>
> (b) 1 V on 200–400 m, 3 V on 400–600 m, 0 elsewhere.
>
> (c) 6 V on 200–400 m, 2 V on 400–600 m, 0 elsewhere.
>
> (d) 3 V on 400–600 m, 1 V on 600–800 m, 0 elsewhere.
>
> *Source: original.*

> [!solution]- Solution
> $\tau_g = \tfrac{50}{100} = \tfrac12$. The front reaches the load only at $T = 5$ μs, so only forward segment 0 has started:
> $$
> V(z,3) = \tfrac12f_i\Big(3-\frac{z}{200}\Big).
> $$
> - Argument in $(0,1)$, i.e. $400<z<600$ m: $\tfrac12\cdot2 = 1$ V. Sent first, now furthest right.
> - Argument in $(1,2)$, i.e. $200<z<400$ m: $\tfrac12\cdot6 = 3$ V.
>
> Wrong options:
> - (b) copies the $t$-axis order onto $z$. A forward pulse lies reversed.
> - (c) forgets $\tau_g$: the line takes only $Z_0/(R_g+Z_0)$ of $f_i$.
> - (d) shifts the pulse 200 m too far right: a front at 800 m would have left before $t = 0$. The front left at $t = 0$ and is at $vt = 600$ m; the tail left at 2 μs and is at 200 m.
>
> **Answer.** (a). With $I = V/Z_0$: 60 mA on 200–400 m, 20 mA on 400–600 m.

### 29.2 Four statements

> [!easy] Easy · true or false · steady state
> A line (characteristic impedance $Z_0$, one-way delay $T$) joins a generator with resistance $R_g$ to a resistor $R_L$. True or false?
>
> (a) With $f_i(t) = 5\sin(\omega t)\,u(t)$ V and $\lvert\Gamma_L\Gamma_g\rvert<1$, $V(z,t)$ settles to a constant as $t\to\infty$.
>
> (b) If $R_g = Z_0$, a burst lasting $D$ leaves the whole line at rest for $t>2T+D$.
>
> (c) For a step input $V_0u(t)$, the final $V$ depends on $Z_0$ and on the line's length.
>
> (d) On a snapshot $V(z,t_0)$, the part of an echo that the source sent first lies nearest the generator.
>
> *Source: original.*

> [!solution]- Solution
> (a) **False.** Every echo adds another delayed sine, and a sum of sines of one frequency is a sine: $V$ oscillates for ever (the lecture's Example 1). A DC limit needs an input that settles to a constant.
>
> (b) **True.** $\Gamma_g = 0$, so the diagram has two segments. The echo passes $z$ during $2T-z/v<t<2T-z/v+D$ and is absorbed at $z = 0$ by $t = 2T+D$.
>
> (c) **False.** $V\to V_0R_L/(R_g+R_L)$ and $I\to V_0/(R_g+R_L)$: at DC the line is two wires. $Z_0$, $v$ and $\ell$ only shape the staircase on the way.
>
> (d) **True.** An echo travels toward $-z$ and its leading edge is the part sent first, so that part is furthest left.
>
> **Answer.** (a) F, (b) T, (c) F, (d) T.

### 29.3 A switched-on sine

> [!easy] Easy · transients · load reflection coefficient
> A 450 m line ($Z_0 = 75\ \Omega$, $v = 300$ m/μs) has $R_g = 75\ \Omega$ and $R_L = 225\ \Omega$. The source is $f_i(t) = 8\sin(\omega t)\,u(t)$ V with $f = 2$ MHz.
>
> (a) At $t = 1$ μs, where is the front, and how many wavelengths lie behind it? Write $V(z)$ at that instant.
>
> (b) Find $V(\ell,t)$ and $I(\ell,t)$ for $t>T$.
>
> *Source: course notes Lecture 29 Example 1, new numbers.*

> [!solution]- Solution
> $\tau_g = \tfrac12$, $\Gamma_g = 0$, $\Gamma_L = \tfrac{225-75}{300} = \tfrac12$, $T = 1.5$ μs, $\lambda = v/f = 150$ m, $\omega = 4\pi$ rad/μs.
>
> (a) Front at $vt = 300$ m: $300/150 = 2$ wavelengths. Forward wave only:
> $$
> V(z,1) = 4\sin\omega\Big(1-\frac{z}{300}\Big) = -4\sin\frac{\pi z}{75}\ \text{V},\qquad 0<z<300\ \text{m}.
> $$
> $I = V/Z_0$, amplitude 53.3 mA.
>
> (b) At the load the arriving wave and its reflection add: $(1+\Gamma_L)\cdot4 = 6$ V. With $\omega T = 6\pi$:
> $$
> V(\ell,t) = 6\sin\omega(t-1.5) = 6\sin\omega t\ \text{V}\qquad(t>1.5\ \mu\text{s}).
> $$
> $\Gamma_g = 0$ absorbs the echo, so nothing else ever reaches the load.
>
> **Check:** $I(\ell,t) = (1-\Gamma_L)\dfrac{4}{75}\sin\omega t = 26.7\sin\omega t$ mA, equal to $V/R_L$ ✓.
>
> **Answer.** (a) Front at 300 m, 2 wavelengths behind it; $V = -4\sin(\pi z/75)$ V for $z<300$ m, 0 beyond. (b) $V(\ell,t) = 6\sin\omega t$ V and $I(\ell,t) = 26.7\sin\omega t$ mA for $t>1.5$ μs.

### 29.4 The echo's current

> [!easy] Easy · find the error · bounce diagram
> A 900 m line ($Z_0 = 60\ \Omega$, $v = 300$ m/μs) has $R_g = 60\ \Omega$ and $R_L = 20\ \Omega$. The source gives 4 V for $0<t<1$ μs, then 2 V until $t = 2$ μs. A student finds the snapshot at $t = 5$ μs:
>
> "$\tau_g = \tfrac12$ and $\Gamma_L = -\tfrac12$, so the echo carries $-\tfrac14f_i$. By 5 μs the forward pulse has fully reflected. The echo gives $V = -1$ V on 300–600 m and $-0.5$ V on 600–900 m. Each piece is a wave with $I = V/Z_0$: $-16.7$ mA and $-8.3$ mA."
>
> Find the error and correct it.
>
> *Source: original.*

> [!solution]- Solution
> The voltages and their order are right; the currents have the wrong sign. A backward wave carries $I = -V/Z_0$:
> $$
> I = -\frac{-1}{60} = +16.7\ \text{mA},\qquad I = -\frac{-0.5}{60} = +8.3\ \text{mA}.
> $$
> **Check:** a reflected current is $-\Gamma_L$ times the incident one. The 4 V part launched $2/60 = 33.3$ mA, and $\tfrac12\cdot33.3 = 16.7$ mA ✓.
>
> **Answer.** $I = V/Z_0$ holds only for forward waves. $V = -1$ V, $I = +16.7$ mA on 300–600 m; $V = -0.5$ V, $I = +8.3$ mA on 600–900 m.

### 29.5 Inputs that settle

> [!easy] Easy · steady state · transients
> A 300 m line ($Z_0 = 50\ \Omega$, $v = 200$ m/μs) joins $R_g = 25\ \Omega$ to $R_L = 100\ \Omega$. For each open-circuit source voltage ($t$ in μs), find $V$ and $I$ on the line as $t\to\infty$, or say why there is no constant limit.
>
> (a) $12u(t-2)$ V. (b) $9u(t)-6u(t-1)$ V. (c) $6\sin(2\pi t)\,u(t)$ V. (d) $10[u(t)-u(t-3)]$ V.
>
> *Source: course notes Lecture 29 (the DC-limit remarks), new inputs.*

> [!solution]- Solution
> $\Gamma_L\Gamma_g = \tfrac13\cdot(-\tfrac13) = -\tfrac19$, so echoes die out. An input that settles to $F$ volts gives the DC divider at every $z$:
> $$
> V\to F\,\frac{R_L}{R_g+R_L} = 0.8F,\qquad I\to\frac{F}{R_g+R_L} = \frac{F}{125\ \Omega}.
> $$
> (a) $F = 12$ V: $V = 9.6$ V, $I = 96$ mA. The 2 μs delay does not matter as $t\to\infty$.
>
> (b) $F = 9-6 = 3$ V: $V = 2.4$ V, $I = 24$ mA.
>
> (c) No constant limit: each copy of $f_i$ is a sine that never ends, so $V$ and $I$ keep oscillating.
>
> (d) $F = 0$: $V\to0$, $I\to0$.
>
> **Answer.** (a) 9.6 V, 96 mA. (b) 2.4 V, 24 mA. (c) None: $V$ and $I$ oscillate for ever. (d) 0 V, 0 A.

## Medium

### 29.6 Both ends of a short line

> [!medium] Medium · bounce diagram · generator reflection coefficient
> A line with $Z_0 = 120\ \Omega$, $\ell = 10$ cm and $v = 0.2$ m/ns is driven at $z = 0$ through $R_g = 180\ \Omega$ and ends in $R_L = 40\ \Omega$. The source is a 15 V pulse on $0<t<1.5$ ns.
>
> (a) Find $\tau_g$, $\Gamma_g$, $\Gamma_L$ and $T$.
>
> (b) Find $V(0,t)$ and $I(0,t)$ for $0<t<3$ ns.
>
> (c) Find $V(\ell,t)$ and $I(\ell,t)$ for $0<t<3$ ns.
>
> *Source: SP18 Exam 3 #3c–d, re-parameterized (pulse source, new line and resistors).*

> [!hint]- Hint
> The pulse lasts $3T$, longer than the $2T$ between arrivals at one end, so copies overlap there. List each copy with its time window and add. At the load an arrival $w$ gives $(1+\Gamma_L)w$; at the generator an echo $b$ adds $(1+\Gamma_g)b$ to $V$ and $-(1-\Gamma_g)b$ to $Z_0I$.

> [!solution]- Solution
> **(a)** $\tau_g = \tfrac{120}{300} = 0.4$, $\Gamma_g = \tfrac{60}{300} = 0.2$, $\Gamma_L = \tfrac{-80}{160} = -0.5$, $T = 0.1/0.2 = 0.5$ ns.
>
> Segment heights: forward 6, $-0.6$, 0.06 V; backward $-3$, 0.3, $-0.03$ V. Each is a 1.5 ns copy of the pulse.
>
> **(b)** At $z = 0$: the launched 6 V on 0–1.5 ns; echoes from 1 ns and from 2 ns add $1.2\times(-3) = -3.6$ V and $0.36$ V to $V$, and $-0.8\times(-3) = 2.4$ V and $-0.24$ V to $Z_0I$.
>
> | $t$ (ns) | 0–1 | 1–1.5 | 1.5–2 | 2–2.5 | 2.5–3 |
> |---|---|---|---|---|---|
> | $V(0,t)$ (V) | 6 | 2.4 | $-3.6$ | $-3.24$ | 0.36 |
> | $I(0,t)$ (mA) | 50 | 70 | 20 | 18 | $-2$ |
>
> **(c)** At $z = \ell$: arrivals from 0.5, 1.5, 2.5 ns, each $(1+\Gamma_L)\times$ forward: 3, $-0.3$, 0.03 V. $I = V/R_L$.
>
> | $t$ (ns) | 0–0.5 | 0.5–1.5 | 1.5–2 | 2–2.5 | 2.5–3 |
> |---|---|---|---|---|---|
> | $V(\ell,t)$ (V) | 0 | 3 | 2.7 | $-0.3$ | $-0.27$ |
> | $I(\ell,t)$ (mA) | 0 | 75 | 67.5 | $-7.5$ | $-6.75$ |
>
> **Check:** KVL at $z = 0$, $V = f_i-R_gI$: $15-180(0.07) = 2.4$ V on 1–1.5 ns; $0-180(0.02) = -3.6$ V on 1.5–2 ns ✓.
>
> **Answer.** (a) $\tau_g = 0.4$, $\Gamma_g = 0.2$, $\Gamma_L = -0.5$, $T = 0.5$ ns. (b) On 0–1, 1–1.5, 1.5–2, 2–2.5, 2.5–3 ns: $V(0,t)$ = 6, 2.4, $-3.6$, $-3.24$, 0.36 V and $I(0,t)$ = 50, 70, 20, 18, $-2$ mA. (c) On 0–0.5, 0.5–1.5, 1.5–2, 2–2.5, 2.5–3 ns: $V(\ell,t)$ = 0, 3, 2.7, $-0.3$, $-0.27$ V and $I(\ell,t)$ = 0, 75, 67.5, $-7.5$, $-6.75$ mA.

### 29.7 A triangle meets a short

> [!medium] Medium · bounce diagram · transients
> A 400 m line ($Z_0 = 50\ \Omega$, $v = 200$ m/μs) has $R_g = 50\ \Omega$ and a short circuit at $z = \ell$. The source is a triangle: $f_i$ rises linearly from 0 to 12 V on $0<t<0.5$ μs and falls back to 0 at $t = 1$ μs.
>
> Find $V(z)$ and $I(z)$ along the line at (a) $t = 2$ μs, (b) $t = 2.5$ μs, (c) $t = 3$ μs.
>
> *Source: original.*

> [!hint]- Hint
> The forward copy is $\tfrac12f_i(t-z/v)$, the echo $-\tfrac12f_i(t+z/v-2T)$. At 2.5 μs both lie on 300–400 m: write each as a function of $z$ there before adding.

> [!solution]- Solution
> **Setup.** $\tau_g = \tfrac12$, $\Gamma_g = 0$, $\Gamma_L = -1$, $T = 2$ μs. The pulse is $v\cdot1$ μs = 200 m long, peak $\tfrac12\cdot12 = 6$ V. Forward $I = V/50$, echo $I = -V/50$.
>
> **(a)** Forward only; argument $2-z/200\in(0,1)$ puts it on 200–400 m. A triangle: 0 at 200 m, 6 V at 300 m, 0 at the load. $V = 0.06(z-200)$ V on 200–300 m, $0.06(400-z)$ V on 300–400 m; $I = V/50$, peak 120 mA.
>
> **(b)** On 300–400 m: forward argument $2.5-z/200\in(0.5,1)$ (the falling half), echo argument $z/200-1.5\in(0,0.5)$ (the rising half, inverted):
> $$
> V^+ = 0.06(z-300),\qquad V^- = -0.06(z-300).
> $$
> So $V = 0$ on the whole line, and $I = (V^+-V^-)/50 = 0.0024(z-300)$ A: 0 at 300 m, 240 mA at the load.
>
> **(c)** Echo only, on 200–400 m: the inverted triangle, $-6$ V at 300 m. $I = -V/50$: $+120$ mA at 300 m.
>
> **Check (energy).** $\mathcal{C} = 1/(Z_0v) = 100$ pF/m, $\mathcal{L} = Z_0/v = 0.25$ μH/m. (a): $\int\mathcal{C}V^2dz = 10^{-10}\times2400 = 0.24$ μJ, half electric, half magnetic. (b): $\int\tfrac12\mathcal{L}I^2dz = \tfrac12(0.25\times10^{-6})(1.92) = 0.24$ μJ, all magnetic ✓.
>
> **Answer.** (a) Triangle on 200–400 m, peak 6 V and 120 mA at 300 m. (b) $V = 0$ everywhere; $I = 2.4(z-300)$ mA on 300–400 m (240 mA at the load), 0 elsewhere. (c) Inverted triangle on 200–400 m: $-6$ V and $+120$ mA at 300 m.

### 29.8 One pulse and nothing else

> [!medium] Medium · load reflection coefficient · generator reflection coefficient
> A source gives a 20 V pulse on $0<t<1$ μs to a 300 m line with $Z_0 = 60\ \Omega$; $R_g$, $R_L$ and $v$ are unknown. A probe at $z = 100$ m records 15 V on $0.5<t<1.5$ μs and nothing else, ever.
>
> (a) Find $v$.
>
> (b) Find $R_L$ and $R_g$.
>
> (c) $R_L$ is replaced by an open circuit. Find $V$ and $I$ at $z = 100$ m for $0<t<8$ μs.
>
> *Source: SP17 Exam 3 #2(v)–(vi), re-parameterized (pulse source, open-load follow-up).*

> [!hint]- Hint
> An echo would pass the probe on its way back. The height at the probe is $\tau_g\times20$ V. For (c), list the crossing times $z/v+2nT$ and $2T-z/v+2nT$ with their weights.

> [!solution]- Solution
> **(a)** The front covers 100 m in 0.5 μs: $v = 200$ m/μs, $T = 1.5$ μs.
>
> **(b)** Any $\Gamma_L\ne0$ would send an echo past the probe from $2T-0.5 = 2.5$ μs. None comes, so $R_L = Z_0 = 60\ \Omega$. Then $\tau_g = \tfrac{15}{20} = \tfrac34 = \dfrac{60}{R_g+60}$, so $R_g = 20\ \Omega$. ($\Gamma_g = -\tfrac12$ never shows here: nothing returns to the generator.)
>
> **(c)** $\Gamma_L = 1$, $\Gamma_L\Gamma_g = -\tfrac12$. Crossings at 100 m, each 1 μs long:
>
> | $t$ (μs) | 0.5–1.5 | 2.5–3.5 | 3.5–4.5 | 5.5–6.5 | 6.5–7.5 |
> |---|---|---|---|---|---|
> | segment | forward 0 | backward 0 | forward 1 | backward 1 | forward 2 |
> | $V$ (V) | 15 | 15 | $-7.5$ | $-7.5$ | 3.75 |
> | $I$ (mA) | 250 | $-250$ | $-125$ | 125 | 62.5 |
>
> Zero in the gaps. $I = \pm V/60$, minus on backward segments.
>
> **Check:** forward 1 is $\Gamma_g\times$ backward 0 $= -\tfrac12\cdot15$ V ✓. The crossings are at least 1 μs apart, so the pulses never overlap at this $z$.
>
> **Answer.** (a) 200 m/μs. (b) $R_L = 60\ \Omega$, $R_g = 20\ \Omega$. (c) On 0.5–1.5, 2.5–3.5, 3.5–4.5, 5.5–6.5, 6.5–7.5 μs: $V$ = 15, 15, $-7.5$, $-7.5$, 3.75 V and $I$ = 250, $-250$, $-125$, 125, 62.5 mA; zero otherwise.

## Hard

### 29.9 One sine cycle on a mismatched line

> [!hard] Hard · bounce diagram · generator reflection coefficient
> A 500 m line ($Z_0 = 50\ \Omega$, $v = 200$ m/μs) has $R_g = 150\ \Omega$ and $R_L = 10\ \Omega$. The source sends one sine cycle: $f_i(t) = 12\sin(2\pi t)$ V for $0<t<1$ μs, zero otherwise ($t$ in μs).
>
> (a) Find $\tau_g$, $\Gamma_g$, $\Gamma_L$, $T$, the pulse's length on the line and the amplitudes of the first four segments.
>
> (b) Find $V(z)$ and $I(z)$ at $t = 2$ μs.
>
> (c) The same at $t = 2.75$ μs. Check the result at the load.
>
> (d) The same at $t = 6$ μs.
>
> *Source: SP17 Exam 3 #5c, re-parameterized (full sine cycle; overlap and generator echo added).*

> [!hint]- Hint
> Write each segment started by then as amplitude $\times\sin2\pi s$ with $s$ its argument, and keep only the $z$ where $0<s<1$. With $k = \pi/100$ rad/m, each $\sin2\pi s$ reduces to $\pm\sin kz$ or $\pm\cos kz$ at these times.

> [!solution]- Solution
> **(a)** $\tau_g = \tfrac{50}{200} = \tfrac14$, $\Gamma_g = \tfrac{100}{200} = \tfrac12$, $\Gamma_L = \tfrac{-40}{60} = -\tfrac23$, $T = 2.5$ μs; length $v\cdot1$ μs = 200 m. Amplitudes: $12\tau_g = 3$ V; $\times\Gamma_L$: $-2$ V; $\times\Gamma_g$: $-1$ V; $\times\Gamma_L$: $\tfrac23$ V. Below, $k = \pi/100$ rad/m.
>
> **(b)** Forward only, $s = 2-z/200$, on 200–400 m. $2\pi s = 4\pi-kz$, so $V = 3\sin(4\pi-kz) = -3\sin kz$ and $I = V/50$. The first half-cycle leads ($+3$ V at 350 m); $-3$ V at 250 m; peaks $\pm60$ mA.
>
> **(c)** Forward, $s = 2.75-z/200$, on 350–500 m: $V^+ = -3\cos kz$. Echo, $s = z/200-2.25$, on 450–500 m: $V^- = -2\sin2\pi s = 2\cos kz$.
> $$
> \begin{aligned}
> 350<z<450:&\quad V = -3\cos kz,\quad I = -60\cos kz\ \text{mA},\\
> 450<z<500:&\quad V = -\cos kz,\quad I = \frac{V^+-V^-}{50} = -100\cos kz\ \text{mA}.
> \end{aligned}
> $$
> Load ($kz = 5\pi$): $V = 1$ V, $I = 100$ mA, $V/I = 10\ \Omega = R_L$ ✓.
>
> **(d)** Segments started by 6 μs: forward 0, backward 0, forward 1. The two segment-0 copies have left the line ($s\notin(0,1)$ for $0<z<500$ m). The echo reached $z = 0$ at 5 μs and left as forward segment 1 ($-1$ V), $s = 1-z/200$, on 0–200 m:
> $$
> V = -\sin(2\pi-kz) = \sin kz,\qquad I = \frac{V}{50},\ \text{peak }20\ \text{mA}.
> $$
> **Watch out:** segment 1 carries $\Gamma_L\Gamma_g<0$, so its leading half-cycle (now near 150 m) is negative, the reverse of the original.
>
> **Answer.** (a) $\tau_g = \tfrac14$, $\Gamma_g = \tfrac12$, $\Gamma_L = -\tfrac23$, $T = 2.5$ μs, 200 m; 3, $-2$, $-1$, $\tfrac23$ V. (b) $V = -3\sin(\pi z/100)$ V, $I = V/50$, on 200–400 m. (c) $V = -3\cos(\pi z/100)$ V, $I = V/50$ on 350–450 m; $V = -\cos(\pi z/100)$ V, $I = -100\cos(\pi z/100)$ mA on 450–500 m; 1 V and 100 mA at the load. (d) $V = \sin(\pi z/100)$ V, $I = V/50$, on 0–200 m. Zero elsewhere at each time.

### 29.10 A ramp into an open line

> [!hard] Hard · bounce diagram · transients
> A 300 m line ($Z_0 = 50\ \Omega$, $v = 200$ m/μs) is open at $z = \ell$ and driven through $R_g = 50\ \Omega$ by a ramp that is cut off: $f_i(t) = 20t$ V for $0<t<5$ μs, zero otherwise ($t$ in μs).
>
> (a) Find $V(0,t)$ and $I(0,t)$ for $0<t<10$ μs.
>
> (b) Find $V(\ell,t)$ for $0<t<10$ μs.
>
> (c) Find $V(z)$ and $I(z)$ at $t = 4.5$ μs.
>
> (d) The same at $t = 6$ μs.
>
> *Source: FA23 Exam 3 #5(c), re-parameterized (ramp source, open load).*

> [!hint]- Hint
> $\Gamma_g = 0$ and $\Gamma_L = 1$: only two segments, $\tfrac12f_i(t-z/v)$ and $\tfrac12f_i(t+z/v-2T)$, with $2T = 3$ μs, shorter than the 5 μs ramp. Where both are on, add them for $V$ and subtract them for $Z_0I$.

> [!solution]- Solution
> **Setup.** $\tau_g = \tfrac12$, $\Gamma_g = 0$, $\Gamma_L = 1$, $T = 1.5$ μs. $V^+ = 10(t-z/200)$ and $V^- = 10(t+z/200-3)$ V wherever their arguments lie in $(0,5)$; $V = V^++V^-$, $Z_0I = V^+-V^-$.
>
> **(a)** At $z = 0$: $V^+ = \tfrac12f_i(t)$, $V^- = \tfrac12f_i(t-3)$.
>
> | $t$ (μs) | 0–3 | 3–5 | 5–8 | after 8 |
> |---|---|---|---|---|
> | $V(0,t)$ (V) | $10t$ | $20t-30$ | $10(t-3)$ | 0 |
> | $I(0,t)$ (A) | $0.2t$ | 0.6 | $-0.2(t-3)$ | 0 |
>
> **(b)** Open end: $V(\ell,t) = 2V^+ = f_i(t-1.5) = 20(t-1.5)$ V on $1.5<t<6.5$ μs (up to 100 V), zero otherwise; $I(\ell,t) = 0$.
>
> **(c)** Both arguments, $4.5-z/200$ and $1.5+z/200$, lie in the ramp for every $z$:
> $$
> V = 10\Big(4.5-\frac z{200}\Big) + 10\Big(1.5+\frac z{200}\Big) = 60\ \text{V},\qquad I = \frac{30-z/10}{50} = 0.6\Big(1-\frac z{300}\Big)\ \text{A}.
> $$
> Uniform $V$, current falling to 0 at the open end: the line charges like a capacitor $\mathcal{C}\ell = \ell/(Z_0v) = 30$ nF, and 30 nF × 20 V/μs = 0.6 A $= I(0,t)$ ✓.
>
> **(d)** The cut-off left $z = 0$ at 5 μs and is now at 200 m. The cut at 6 μs no longer crosses forward segment 0, but its copy is still on the line: $V^+ = 60-z/20$ for $z>200$ m; $V^- = 30+z/20$ everywhere.
> - $0<z<200$ m: $V = 30+z/20$ (30 to 40 V), $I = -(0.6+z/1000)$ A ($-0.6$ to $-0.8$ A).
> - $200<z<300$ m: $V = 90$ V, $I = 0.6-z/500$ A (0.2 A down to 0).
>
> **Check:** the jump at 200 m, $\Delta V = -50$ V with $\Delta I = -1$ A, is a forward step ($\Delta V/\Delta I = Z_0$); at $z = 0$ the source is off and $V = -R_gI = 30$ V ✓.
>
> **Answer.** (a) $V(0,t) = 10t$, $20t-30$, $10(t-3)$ V and $I(0,t) = 0.2t$, 0.6, $-0.2(t-3)$ A on 0–3, 3–5, 5–8 μs; zero after 8 μs. (b) $V(\ell,t) = 20(t-1.5)$ V on 1.5–6.5 μs, zero otherwise. (c) $V = 60$ V, $I = 0.6(1-z/300)$ A. (d) $V = 30+z/20$ V, $I = -(0.6+z/1000)$ A for $z<200$ m; $V = 90$ V, $I = 0.6-z/500$ A for $z>200$ m.

### 29.11 A ramped step off-centre

> [!hard] Hard · impulse response · steady state
> A 400 m line ($Z_0 = 50\ \Omega$, $v = 200$ m/μs) has $R_g = 25\ \Omega$ and $R_L = 100\ \Omega$. The source rises linearly from 0 to 27 V over $0<t<2$ μs and then stays at 27 V.
>
> (a) Find the impulse response at $z = 300$ m for $0<t<12$ μs, and the matching $Z_0I$ weights.
>
> (b) Find $V$ at $z = 300$ m at $t = 1.5, 2.5, \dots, 9.5$ μs, and its shape in between.
>
> (c) Find $I$ at $z = 300$ m on $4.5<t<5.5$ μs and on $8.5<t<9.5$ μs.
>
> (d) Find $V$ and $I$ as $t\to\infty$. By how much does $V$ overshoot?
>
> *Source: course notes Lecture 29 Example 2 style, re-parameterized (ramped step, off-centre point).*

> [!hint]- Hint
> Crossings at $z/v+2nT$ (forward) and $2T-z/v+2nT$ (backward). Each impulse becomes a delayed 2 μs ramp. Between crossings the slope of $V$ is the sum of $27w/(2\ \mu\text{s})$ over the ramps still rising.

> [!solution]- Solution
> **(a)** $\tau_g = \tfrac23$, $\Gamma_g = -\tfrac13$, $\Gamma_L = \tfrac13$, $T = 2$ μs, $z/v = 1.5$ μs. Forward crossings at 1.5, 5.5, 9.5 μs; backward at 2.5, 6.5, 10.5 μs:
> $$
> \begin{aligned}
> h_{300}(t) = {}&\tfrac23\delta(t-1.5) + \tfrac29\delta(t-2.5) - \tfrac2{27}\delta(t-5.5)\\
> &- \tfrac2{81}\delta(t-6.5) + \tfrac2{243}\delta(t-9.5) + \tfrac2{729}\delta(t-10.5).
> \end{aligned}
> $$
> $Z_0I$ weights: the same with the backward signs flipped, $\tfrac23$, $-\tfrac29$, $-\tfrac2{27}$, $\tfrac2{81}$, $\tfrac2{243}$, $-\tfrac2{729}$.
>
> **(b)** Times 27 V the copies are ramps to 18, 6, $-2$, $-\tfrac23$, $\tfrac29$, … V, each rising over 2 μs. $V$ is piecewise linear through:
>
> | $t$ (μs) | 1.5 | 2.5 | 3.5 | 4.5 | 5.5 | 6.5 | 7.5 | 8.5 | 9.5 |
> |---|---|---|---|---|---|---|---|---|---|
> | $V$ (V) | 0 | 9 | 21 | 24 | 24 | 23 | 21.67 | 21.33 | 21.33 |
>
> On 2.5–3.5 μs two ramps overlap (slope $9+3 = 12$ V/μs); $V$ is flat on 4.5–5.5 and 8.5–9.5 μs.
>
> **(c)** Completed ramps with backward signs flipped: $18-6 = 12$ V, so $I = 240$ mA on 4.5–5.5 μs; $18-6-2+\tfrac23 = \tfrac{32}3$ V, so $I = 213$ mA on 8.5–9.5 μs.
>
> **(d)** DC divider: $V\to27\cdot\tfrac{100}{125} = 21.6$ V, $I\to\tfrac{27}{125} = 216$ mA. The peak is 24 V, an overshoot of 2.4 V.
>
> **Check:** summing every weight, $27\tau_g\dfrac{1+\Gamma_L}{1-\Gamma_L\Gamma_g} = 27\cdot\tfrac23\cdot\dfrac{4/3}{10/9} = 21.6$ V ✓.
>
> **Answer.** (a) $\tfrac23$, $\tfrac29$, $-\tfrac2{27}$, $-\tfrac2{81}$, $\tfrac2{243}$, $\tfrac2{729}$ at 1.5, 2.5, 5.5, 6.5, 9.5, 10.5 μs; for $Z_0I$ flip the 2nd, 4th and 6th signs. (b) 0, 9, 21, 24, 24, 23, 21.67, 21.33, 21.33 V at 1.5, 2.5, …, 9.5 μs, linear in between. (c) 240 mA, then 213 mA. (d) 21.6 V and 216 mA; overshoot 2.4 V.

### 29.12 A partial standing wave builds up

> [!hard] Hard · standing waves · bounce diagram
> A 500 m line ($Z_0 = 75\ \Omega$, $v = 200$ m/μs) has $R_g = 75\ \Omega$ and $R_L = 25\ \Omega$. The source is switched on at $t = 0$: $f_i(t) = 12\sin(\omega t)\,u(t)$ V with $f = 0.5$ MHz.
>
> (a) Find $\tau_g$, $\Gamma_g$, $\Gamma_L$, $T$, $\lambda$ and $\beta$.
>
> (b) Find $V(\ell,t)$ and $I(\ell,t)$.
>
> (c) Find $V(z)$ and $I(z)$ at $t = 4$ μs, and check them at the load.
>
> (d) For $t>5$ μs, find the amplitude of $V$ and of $I$ at each $z$. Where are their maxima and minima?
>
> *Source: course notes Lecture 29 Example 1, re-parameterized (load with $\Gamma_L<0$).*

> [!hint]- Hint
> $\Gamma_g = 0$: only the forward wave and its echo exist. With $\omega = \pi$ rad/μs, each reduces to $\pm\sin\beta z$ at $t = 4$ μs. For (d), the amplitude of $a\sin x+b\sin y$ is $\sqrt{a^2+b^2+2ab\cos(x-y)}$.

> [!solution]- Solution
> **(a)** $\tau_g = \tfrac12$, $\Gamma_g = 0$, $\Gamma_L = \tfrac{25-75}{100} = -\tfrac12$, $T = 2.5$ μs, $\lambda = v/f = 400$ m, $\beta = 2\pi/\lambda = \pi/200$ rad/m; $\omega = \pi$ rad/μs. Forward $V^+ = 6\sin\omega(t-z/v)$; echo $V^- = -3\sin\omega(t+z/v-5)$, present from $t = 5-z/v$.
>
> **(b)** $(1+\Gamma_L)\cdot6 = 3$ V and $\omega T = 2.5\pi$, so for $t>2.5$ μs:
> $$
> \begin{aligned}
> V(\ell,t) &= 3\sin(\pi t-2.5\pi) = -3\cos\pi t\ \text{V},\\
> I(\ell,t) &= V/R_L = -120\cos\pi t\ \text{mA}.
> \end{aligned}
> $$
> **(c)** $V^+ = 6\sin(4\pi-\beta z) = -6\sin\beta z$ on the whole line. The echo has come back to 200 m: $V^- = -3\sin(\beta z-\pi) = 3\sin\beta z$ for $z>200$ m.
> - $0<z<200$ m: $V = -6\sin\beta z$, $I = -80\sin\beta z$ mA.
> - $200<z<500$ m: $V = -3\sin\beta z$, $I = (V^+-V^-)/75 = -120\sin\beta z$ mA.
>
> Load: $V = -3$ V, $I = -120$ mA, $V/I = 25\ \Omega$ ✓, and (b) gives $-3\cos4\pi = -3$ V ✓.
>
> **(d)** $\omega\cdot5\ \mu\text{s} = 5\pi$ turns the echo into $3\sin(\omega t+\beta z)$:
> $$
> \begin{aligned}
> V &= 6\sin(\omega t-\beta z) + 3\sin(\omega t+\beta z),\\
> Z_0I &= 6\sin(\omega t-\beta z) - 3\sin(\omega t+\beta z).
> \end{aligned}
> $$
> Amplitudes $\sqrt{45+36\cos2\beta z}$ V and $\sqrt{45-36\cos2\beta z}/75$ A:
> - $V$: 9 V at $z = 0$, 200, 400 m; 3 V at 100, 300, 500 m (a minimum at the load, since $\Gamma_L<0$).
> - $I$: 120 mA where $V$ is smallest, 40 mA where $V$ is largest.
>
> **Check:** at $z = 0$, $V = 9\sin\omega t$ and $I = 40\sin\omega t$ mA; KVL: $12-75(0.04) = 9$ V ✓.
>
> **Answer.** (a) $\tfrac12$, 0, $-\tfrac12$, 2.5 μs, 400 m, $\pi/200$ rad/m. (b) $V(\ell,t) = -3\cos\pi t$ V and $I(\ell,t) = -120\cos\pi t$ mA for $t>2.5$ μs ($t$ in μs). (c) $V = -6\sin(\pi z/200)$ V, $I = -80\sin(\pi z/200)$ mA for $z<200$ m; $V = -3\sin(\pi z/200)$ V, $I = -120\sin(\pi z/200)$ mA for $z>200$ m. (d) $V$ amplitude 9 V at 0, 200, 400 m and 3 V at 100, 300, 500 m; $I$ amplitude 40 mA and 120 mA at the same points.

### Sources for this page
Kudeki notes, Lecture 29: Example 1 (switched-on sine, matched generator) behind 29.3 and 29.12, Example 2 (step watched at one point) behind 29.11, the DC-limit remarks behind 29.5. Past Exam 3 papers, re-parameterized: SP18 E3 #3c–d (29.6), SP17 E3 #2(v)–(vi) (29.8), SP17 E3 #5c (29.9), FA23 E3 #5(c) (29.10). The rest is original. Every value was checked in `practice/checks/L29.py` (29.6, 29.9 and 29.10 were re-parameterized in review and re-checked in `practice/review/R29.py`) against a method-of-characteristics time-stepping of the line (exact on its grid) and, for 29.6, 29.9–29.12, a Yee FDTD of the telegrapher's equations.

*Previous: [[practice/28-bounce-diagrams|Lecture 28 practice]] · next: [[practice/30-multi-line-circuits|Lecture 30 practice]] · [[practice/index|all practice]]*
