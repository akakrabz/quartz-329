---
title: "Practice — Lecture 31: Resonances of line segments"
description: "8 practice problems (4 easy, 2 medium, 2 hard) on source-free oscillations of lossless lines: resonant frequencies for like and unlike ends, mode shapes and their nulls, voltage and current modes from the telegrapher's equations, identifying the ends from measured resonances, a two-measurement exam problem, and a pulse trapped on a line after its source is removed; hints on the medium and hard ones, a worked solution for each."
tags: [practice, transmission-lines]
lecture: 31
---

*Practice for [[4-transmission-lines/31-periodic-oscillations-in-lossless-tl-circuits|Lecture 31]] · concepts: [[concepts/line-resonances]] · [[concepts/standing-waves]] · all practice: [[practice/index|hub]] · by difficulty: [[practice/easy|easy]] · [[practice/medium|medium]] · [[practice/hard|hard]] · [[practice/topics|by topic]]*

*After the scope of FA26 Midterm 3, which covers Lectures 1–30 ([[exams/index#the-scope|scope]]).*

Work each problem on paper first. Open the **hint** only when stuck, and the **solution** only after you have an answer you would hand in. Every answer here has been checked numerically.

The page runs on three rules:
- Open end: $I = 0$. Shorted end: $V = 0$.
- Like ends: $\ell = n\lambda/2$, $f_n = nv/2\ell$, $n\ge1$. Unlike ends: $\ell = (2n+1)\lambda/4$, $f_n = (2n+1)v/4\ell$, $n\ge0$.
- In a mode, measured from an open end, $V\propto\cos\beta z$ and $I\propto\sin\beta z$ (from a short, the reverse); $\lvert V\rvert_{\max} = Z_0\lvert I\rvert_{\max}$; $V$ and $I$ are a quarter period apart in time.

## Easy

### 31.1 The three lowest, three ways

> [!easy] Easy · line resonances
> A lossless line is 45 m long and has $v = 1.8\times10^8$ m/s. List its three lowest resonant frequencies when
> (a) both ends are open, (b) both ends are shorted, (c) one end is open and the other shorted.
>
> *Source: original.*

> [!solution]- Solution
> (a), (b) Like ends: $\ell = n\lambda/2$, so $f_n = nv/2\ell = n\,(1.8\times10^8)/90 = n\times2$ MHz: 2, 4, 6 MHz in both cases. Open or shorted only decides which of $V$ and $I$ vanishes at the ends.
>
> (c) Unlike ends: $\ell = (2n+1)\lambda/4$, so $f_n = (2n+1)v/4\ell = (2n+1)\times1$ MHz: 1, 3, 5 MHz.
>
> **Answer.** (a) 2, 4, 6 MHz. (b) 2, 4, 6 MHz. (c) 1, 3, 5 MHz.

### 31.2 Modes, true or false

> [!easy] Easy · true or false · resonant modes
> True or false, for source-free modes of a lossless line segment?
> (a) On a segment open at both ends the current is zero at both ends in every mode.
> (b) On a segment open at both ends the voltage is zero at the midpoint in every mode.
> (c) A short–short segment and an open–open segment of the same length and speed have the same resonant frequencies.
> (d) An open–short segment's lowest resonance is at half the lowest resonant frequency of the same segment with like ends.
> (e) In a mode, the voltage and the current reach their peak values at the same instants.
> (f) Doubling the length of a segment halves every resonant frequency.
>
> *Source: original.*

> [!solution]- Solution
> (a) **True.** That is the end condition, and it holds at all times.
> (b) **False.** $V\propto\cos(n\pi z/\ell)$ is $\cos(n\pi/2)$ at the midpoint: zero for odd $n$, a maximum for even $n$.
> (c) **True.** Both need $\ell = n\lambda/2$; the roles of $V$ and $I$ swap.
> (d) **True.** $v/4\ell$ against $v/2\ell$.
> (e) **False.** $V\propto\cos\omega t$ goes with $I\propto\sin\omega t$: a quarter period apart. When $V$ peaks, $I = 0$ everywhere.
> (f) **True.** Every $f_n$ is proportional to $v/\ell$.
>
> **Answer.** True, false, true, true, false, true.

### 31.3 The lowest resonance of a cable

> [!easy] Easy · find the error · line resonances
> A 12 m cable with $v = 2.4\times10^8$ m/s is shorted at one end and left open at the other. A student writes: "The lowest resonance fits half a wavelength into the cable: $f = v/2\ell = 10$ MHz, then 20 MHz and 30 MHz."
> Find the error and give the three lowest resonant frequencies.
>
> *Source: original.*

> [!solution]- Solution
> Half wavelengths fit a line whose ends are **alike**. Here the voltage must vanish at the short and the current at the open end, and those nulls are an odd number of quarter wavelengths apart: $\ell = (2n+1)\lambda/4$.
> $$
> f_n = (2n+1)\frac{v}{4\ell} = (2n+1)\frac{2.4\times10^8}{48} = (2n+1)\times5\ \text{MHz}.
> $$
> The student's 10, 20, 30 MHz are the resonances of the same cable with both ends shorted (or both open). None of them is a resonance of this one.
>
> **Answer.** Unlike ends need odd quarter wavelengths: 5, 15, 25 MHz.

### 31.4 Where the nulls are

> [!easy] Easy · resonant modes · standing waves on lines
> A 90 m air line ($v = 3\times10^8$ m/s, $Z_0 = 75\ \Omega$) is open at both ends and oscillates in its $n = 3$ mode with a peak voltage of 12 V.
> (a) Find the frequency and the wavelength.
> (b) Where are the current nulls and the voltage nulls?
> (c) Find the peak current, and say where on the line it occurs.
>
> *Source: original.*

> [!solution]- Solution
> (a) $f_3 = 3v/2\ell = 3(3\times10^8)/180 = 5$ MHz and $\lambda = 2\ell/3 = 60$ m.
>
> (b) $I\propto\sin(3\pi z/90)$: zero at $z = 0, 30, 60, 90$ m. $V\propto\cos(3\pi z/90)$: zero at $z = 15, 45, 75$ m. Each voltage null is a quarter wavelength (15 m) from the nearest current null.
>
> (c) $\lvert I\rvert_{\max} = \lvert V\rvert_{\max}/Z_0 = 12/75 = 0.16$ A, at the voltage nulls: $z = 15, 45, 75$ m.
>
> **Answer.** (a) 5 MHz, 60 m. (b) $I = 0$ at 0, 30, 60, 90 m; $V = 0$ at 15, 45, 75 m. (c) 0.16 A at 15, 45 and 75 m.

## Medium

### 31.5 A mode on a short–open line

> [!medium] Medium · resonant modes · telegrapher's equations
> A 150 m air line ($v = c = 3\times10^8$ m/s, $Z_0 = 100\ \Omega$) is **shorted at $z = 0$** and **open at $z = \ell$**.
> (a) Find its resonant frequencies.
> (b) For the second-lowest mode, the voltage has peak value 20 V and is largest at $t = 0$. Write $V(z,t)$, then find $I(z,t)$ from the telegrapher's equation $-\partial V/\partial z = \mathcal{L}\,\partial I/\partial t$.
> (c) At which times is the voltage zero everywhere on the line? Where is the energy then?
>
> *Source: Kudeki notes, Lecture 31, Example 1 style, with the ends exchanged, a new line and the second mode.*

> [!hint]- Hint
> The voltage must vanish at the short, so it is a sine in $z$. Integrate $\partial I/\partial t$ in time; $\beta/\omega\mathcal{L} = 1/Z_0$.

> [!solution]- Solution
> **(a)** Unlike ends: $f_n = (2n+1)c/4\ell = (2n+1)\times0.5$ MHz: 0.5, 1.5, 2.5 MHz, …
>
> **(b)** Second-lowest: $f = 1.5$ MHz, $\omega = 3\pi$ rad/μs, $\beta = \omega/c = \pi/100$ rad/m ($\lambda = 200$ m, $\ell = 3\lambda/4$). Zero voltage at $z = 0$, largest at $t = 0$:
> $$
> V(z,t) = 20\sin\frac{\pi z}{100}\cos(3\pi t)\ \text{V}\quad(z\text{ in m},\ t\text{ in }\mu\text{s}).
> $$
> Then $\mathcal{L}\,\partial I/\partial t = -\partial V/\partial z = -20\beta\cos\beta z\cos\omega t$. Integrating in $t$ and using $\beta/\omega\mathcal{L} = 1/v\mathcal{L} = 1/Z_0$:
> $$
> I(z,t) = -\frac{20}{Z_0}\cos\frac{\pi z}{100}\sin(3\pi t) = -0.2\cos\frac{\pi z}{100}\sin(3\pi t)\ \text{A}.
> $$
> Check: $I(\ell,t)\propto\cos(1.5\pi) = 0$, the open end. The other telegrapher's equation, $-\partial I/\partial z = \mathcal{C}\,\partial V/\partial t$, is satisfied too ($\beta/Z_0 = \omega\mathcal{C}$).
>
> **(c)** $V = 0$ everywhere when $\cos(3\pi t) = 0$: $t = \tfrac16+\tfrac k3$ μs. At those instants $\lvert\sin3\pi t\rvert = 1$: the current is at its peak and all the energy is magnetic, $\tfrac12\mathcal{L}I^2$ per metre.
>
> **Answer.** (a) $(2n+1)\times0.5$ MHz. (b) $V = 20\sin(\pi z/100)\cos(3\pi t)$ V, $I = -0.2\cos(\pi z/100)\sin(3\pi t)$ A. (c) $t = \tfrac16+\tfrac k3$ μs; all of it is magnetic.

### 31.6 Resonances tell you the ends

> [!medium] Medium · line resonances
> A 20 m length of non-magnetic cable has unknown terminations, each either an open or a short. Its two lowest resonances are measured at 2.5 MHz and 7.5 MHz.
> (a) Are the ends alike or different?
> (b) Find $v$ and the dielectric constant of the filling.
> (c) One end is now changed so that both ends are alike. Find the three lowest resonant frequencies.
>
> *Source: original.*

> [!hint]- Hint
> Look at the ratio of the two frequencies. Like ends give 1 : 2 : 3; unlike ends give 1 : 3 : 5.

> [!solution]- Solution
> **(a)** $7.5/2.5 = 3$: the second resonance is the third harmonic of the first, and the second harmonic is missing. Odd harmonics only: the ends are **different** (one open, one short).
>
> **(b)** Lowest unlike-end resonance: $f_0 = v/4\ell$, so $v = 4\ell f_0 = 4(20)(2.5\times10^6) = 2\times10^8$ m/s. For a non-magnetic filling $\epsilon_r = (c/v)^2 = 2.25$.
>
> **(c)** Like ends: $f_n = nv/2\ell = n\times5$ MHz: 5, 10, 15 MHz. They fall halfway between the old ones.
>
> **Answer.** (a) Different. (b) $2\times10^8$ m/s, $\epsilon_r = 2.25$. (c) 5, 10, 15 MHz.

## Hard

### 31.7 A resonator from two zero readings

> [!hard] Hard · line resonances · standing waves on lines
> A lossless line of length $\ell = 50$ m with $v = 2.5\times10^8$ m/s supports resonant oscillations. In sinusoidal steady state the voltage phasor is zero at the input and the current phasor is zero at the load: $\tilde V_{\text{in}} = 0$, $\tilde I_L = 0$. Let $d$ be the distance from the load.
> (a) What are $Z_{\text{in}}$ and $Z_L$ for these oscillations?
> (b) Find the three lowest resonant values of $\omega$.
> (c) At the second resonance, where are the nulls of $\lvert\tilde V(d)\rvert$ and of $\lvert\tilde I(d)\rvert$?
> (d) At the second resonance, where between the two ends does the line look like an open circuit?
> (e) The load end is now shorted as well. Find the lowest resonant frequency.
>
> *Source: SP19 Exam 3 #5 and FA23 Exam 3 #7 style, re-parameterized: a new line, the null positions and the open-circuit point asked, and the like-ends case added.*

> [!hint]- Hint
> Zero voltage with non-zero current is a short; zero current with non-zero voltage is an open. From the open load, $\lvert\tilde I\rvert\propto\lvert\sin\beta d\rvert$ and $\lvert\tilde V\rvert\propto\lvert\cos\beta d\rvert$.

> [!solution]- Solution
> **(a)** $Z_{\text{in}} = \tilde V_{\text{in}}/\tilde I_{\text{in}} = 0$ (a short at the input) and $Z_L = \tilde V_L/\tilde I_L = \infty$ (an open load).
>
> **(b)** Unlike ends: $\ell = (2n+1)\lambda/4$.
> $$
> f_n = (2n+1)\frac{v}{4\ell} = (2n+1)(1.25\ \text{MHz}),\qquad \omega_n = 2\pi f_n = 2.5\pi,\ 7.5\pi,\ 12.5\pi\ \times10^6\ \text{rad/s}.
> $$
>
> **(c)** Second resonance: $f = 3.75$ MHz, $\lambda = v/f = 66.7$ m, $\ell = 3\lambda/4$. From the open load, $\lvert\tilde V\rvert\propto\lvert\cos\beta d\rvert$: nulls at $d = \lambda/4 = 16.7$ m and $d = 3\lambda/4 = 50$ m (the input, as required). $\lvert\tilde I\rvert\propto\lvert\sin\beta d\rvert$: nulls at $d = 0$ (the load) and $d = \lambda/2 = 33.3$ m.
>
> **(d)** The line looks like an open circuit where $\tilde I = 0$ with $\tilde V\ne0$: at $d = \lambda/2 = 33.3$ m. A half-wave section repeats its load.
>
> **(e)** Like ends: $f_1 = v/2\ell = 2.5$ MHz.
>
> **Check:** at $d = 16.7$ m the line looks like a short, a quarter wave from the open load; the input short is half a wave further on.
>
> **Answer.** (a) $Z_{\text{in}} = 0$, $Z_L = \infty$. (b) $2.5\pi\times10^6$, $7.5\pi\times10^6$, $12.5\pi\times10^6$ rad/s. (c) $\lvert\tilde V\rvert = 0$ at $d = 16.7$ m and 50 m; $\lvert\tilde I\rvert = 0$ at $d = 0$ and 33.3 m. (d) At $d = 33.3$ m. (e) 2.5 MHz.

### 31.8 A pulse trapped on a line

> [!hard] Hard · source-free oscillations · line resonances
> A 900 m air line ($v = 300$ m/μs, $Z_0 = 50\ \Omega$) is **shorted at $z = \ell$**. An ideal 5 V battery is connected across the $z = 0$ end at $t = 0$ and removed at $t = 2$ μs, leaving that end open.
> (a) Find $V(z)$ and $I(z)$ at $t = 2$ μs.
> (b) Find the period and the fundamental frequency of everything that happens afterwards.
> (c) Give $V$ and $I$ at the midpoint, $z = 450$ m, for $2<t<14$ μs.
> (d) Find the energy left on the line. Where is it, and in what form, at $t = 4$ μs?
>
> *Source: Kudeki notes, Lecture 31 (the switched battery), re-parameterized: a new line and battery, the far end shorted instead of open, and the record and the energy added.*

> [!hint]- Hint
> Follow the pulse. The short reflects with $\Gamma = -1$, the open end with $+1$. A backward wave of voltage $V$ carries current $-V/Z_0$. The ends are unlike: after one round trip the pulse comes back inverted.

> [!solution]- Solution
> **(a)** The battery launches $V = 5$ V with $I = 5/50 = 0.1$ A. In 2 μs the front travels 600 m: $V = 5$ V and $I = 0.1$ A for $0<z<600$ m, zero beyond. Removing the battery ends the pulse: a forward pulse 600 m long.
>
> **(b)** One open end and one shorted end: the period is two round trips, $T = 4\ell/v = 12$ μs, and the fundamental is $1/T = 83.3$ kHz $= v/4\ell$. Only odd harmonics are present.
>
> **(c)** The pulse occupies a 2 μs window at any point.
>
> | window at $z = 450$ m [μs] | the pulse is | $V$ [V] | $I$ [A] |
> |---|---|---|---|
> | $2<t<3.5$ | forward, original | $+5$ | $+0.1$ |
> | $4.5<t<6.5$ | backward, after the short ($\Gamma = -1$) | $-5$ | $+0.1$ |
> | $7.5<t<9.5$ | forward, after the open end ($\Gamma = +1$) | $-5$ | $-0.1$ |
> | $10.5<t<12.5$ | backward, after the short again | $+5$ | $-0.1$ |
> | $13.5<t<14$ | forward again: the cycle repeats | $+5$ | $+0.1$ |
>
> Between the windows $V = I = 0$. Timing: the tail passes 450 m at $2+450/300 = 3.5$ μs; the front reaches the short at 3 μs and is back at 450 m at 4.5 μs; it reaches $z = 0$ at 6 μs and 450 m again at 7.5 μs; and so on, every 3 μs.
>
> **(d)** The battery delivered $VI\,\Delta t = (5)(0.1)(2\times10^{-6}) = 1\ \mu$J, half electric and half magnetic in the travelling pulse. At $t = 4$ μs the leading 300 m has reflected and overlaps the trailing 300 m on $600<z<900$ m: $V = 5-5 = 0$ and $I = 0.1+0.1 = 0.2$ A. All of the energy is magnetic, in the 300 m next to the short: with $\mathcal{L} = Z_0/v = 0.167\ \mu$H/m, $\tfrac12\mathcal{L}I^2\times300\ \text{m} = 1\ \mu$J ✓.
>
> **Check:** the record at 450 m repeats after 12 μs, and $V(t+6\ \mu\text{s}) = -V(t)$: odd harmonics only.
>
> **Answer.** (a) $V = 5$ V, $I = 0.1$ A for $0<z<600$ m; zero beyond. (b) 12 μs; 83.3 kHz. (c) The table above; zero between the windows. (d) 1 μJ; at 4 μs all magnetic, in $600<z<900$ m, where $V = 0$ and $I = 0.2$ A.

### Sources for this page
Kudeki notes, Lecture 31: the resonance conditions, Example 1 (31.5, with the ends exchanged) and the switched battery (31.8, with a shorted far end). Past exams, re-parameterized: SP19 Exam 3 #5 and FA23 Exam 3 #7 (31.7). The rest is original. Every number is checked by `practice/checks/L31.py` and re-solved independently in `practice/review/R31.py` (a leapfrog simulation of the telegrapher's equations and the spectrum of a ringing line).

*Previous: [[practice/30-multi-line-circuits|Lecture 30 practice]] · next: [[practice/32-stubs-and-input-impedance|Lecture 32 practice]] · [[practice/index|all practice]]*
