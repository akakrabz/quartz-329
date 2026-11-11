---
title: "Past Exam 3 type — lines in sinusoidal steady state (Lectures 31–33; not on FA26 Midterm 3)"
description: "Not on FA26 Midterm 3 (Lectures 1–30). The minimum of Lectures 31–33 that past Exam 3 papers use: voltage and current phasors on a line, shorted and open stubs, resonances from the end conditions, quarter- and half-wave sections, the reflection coefficient along the line; with five worked twins of the exam items."
tags: [exam-3, transmission-lines]
aliases: ["sinusoidal steady state on lines", "stub resonances", "quarter-wave transformer"]
---

*Part of the [[exams/index|Midterm 3 review]] · the exam-sized version of [[4-transmission-lines/31-periodic-oscillations-in-lossless-tl-circuits|Lecture 31]], [[4-transmission-lines/32-input-impedance-and-microwave-resonators|Lecture 32]] and [[4-transmission-lines/33-half-wave-and-quarter-wave-transformers|Lecture 33]] (and one item from the notes' §34) · every Spring and Fall Exam 3 on hand has one problem of this kind: [[exams/e3-sp17#6-a-shorted-line-in-series-with-a-resistor-11-points|SP17 #6]], [[exams/e3-sp18#1-ten-multiple-choice-items-30-points|SP18 #1(vi), (viii)–(x)]] and [[exams/e3-sp18#4-a-line-in-series-with-a-resistor-20-points|#4]], [[exams/e3-sp19#5-resonances-from-two-measurements-15-points|SP19 #5]], [[exams/e3-fa23#7-resonances-and-standing-wave-shapes-16-points|FA23 #7]]*

> [!warning] Not on FA26 Midterm 3
> The exam stops at Lecture 30 and has no Smith chart ([[exams/index#the-scope|the scope]]); this page is Lectures 31–33. Skip it for Monday. It stays here because every Spring and Fall Exam 3 on hand has one problem of this kind, so it explains the part of each past paper you are skipping, and it will be needed after the midterm.
>
> This page is the short version. The full treatment, with the notes' and slides' examples and eight practice problems each, is in [[4-transmission-lines/31-periodic-oscillations-in-lossless-tl-circuits|Lecture 31]], [[4-transmission-lines/32-input-impedance-and-microwave-resonators|Lecture 32]] and [[4-transmission-lines/33-half-wave-and-quarter-wave-transformers|Lecture 33]]. All of it was checked by simulation ([[exams/index#how-these-pages-were-checked|how]]).

## 1. The phasors on a line

> [!key] Voltage, current and impedance at distance d from the load
> One frequency $\omega$, lossless line, $\beta = \omega/v = 2\pi/\lambda$. Measure $d$ from the **load** ($d = 0$) back toward the generator ($d = \ell$ is the input).
> $$
> \begin{gathered}
> \tilde V(d) = V^+e^{j\beta d}+V^-e^{-j\beta d},\\[4pt]
> \tilde I(d) = \frac{V^+e^{j\beta d}-V^-e^{-j\beta d}}{Z_0},\\[4pt]
> \Gamma_L = \frac{V^-}{V^+} = \frac{Z_L-Z_0}{Z_L+Z_0},\\[4pt]
> Z(d) = \frac{\tilde V(d)}{\tilde I(d)} = Z_0\,\frac{Z_L+jZ_0\tan\beta d}{Z_0+jZ_L\tan\beta d}.
> \end{gathered}
> $$
> $V^+e^{j\beta d}$ is the wave travelling toward the load, $V^-e^{-j\beta d}$ the reflected one. They are the steady-state sum of all the bounces of [[4-transmission-lines/28-distributed-circuits-and-bounce-diagrams|Lecture 28]]; the backward wave still carries $I = -V/Z_0$, hence the minus sign in $\tilde I$.

| load | $\tilde V(d)$ | $\tilde I(d)$ | $Z(d)$ |
|---|---|---|---|
| short, $\Gamma_L = -1$ | $2jV^+\sin\beta d$ | $\dfrac{2V^+}{Z_0}\cos\beta d$ | $jZ_0\tan\beta d$ |
| open, $\Gamma_L = +1$ | $2V^+\cos\beta d$ | $\dfrac{2jV^+}{Z_0}\sin\beta d$ | $-jZ_0\cot\beta d$ |
| matched, $\Gamma_L = 0$ | $V^+e^{j\beta d}$ | $\dfrac{V^+}{Z_0}e^{j\beta d}$ | $Z_0$ |

A shorted or open line holds a pure **standing wave**: $\lvert\tilde V\rvert$ and $\lvert\tilde I\rvert$ have fixed nulls a quarter wavelength apart, voltage nulls sit on current maxima, and $Z(d)$ is purely imaginary, so the line absorbs no average power. It is the circuit twin of the wave in front of a mirror ([[concepts/standing-waves|Standing waves]]).

> [!key] What a stub looks like from its input
> | length $\ell$ | shorted stub | open stub |
> |---|---|---|
> | $0<\ell<\lambda/4$ | inductive ($+j$) | capacitive ($-j$) |
> | $\ell = \lambda/4$ | open circuit, $Z = \infty$ | short circuit, $Z = 0$ |
> | $\lambda/4<\ell<\lambda/2$ | capacitive | inductive |
> | $\ell = \lambda/2$ | short circuit | open circuit |
>
> The pattern repeats every $\lambda/2$. The notes call $Z(\ell) = 0$ a **series resonance** (the stub passes current with no voltage, like a series LC at resonance) and $Z(\ell) = \infty$ a **parallel resonance** (voltage with no current).

## 2. Resonances from the end conditions

A measured $\tilde V = 0$ at an end means a short there; $\tilde I = 0$ means an open. Then count quarter wavelengths:

| the two ends | the line must hold | resonant frequencies |
|---|---|---|
| same kind (short–short or open–open) | a whole number of half wavelengths, $\ell = n\lambda/2$ | $f_n = \dfrac{nv}{2\ell}$, $n = 1, 2, 3,\ldots$ |
| different (short at one end, open at the other) | an odd number of quarter wavelengths, $\ell = (2n-1)\lambda/4$ | $f_n = \dfrac{(2n-1)v}{4\ell}$ |

Shapes: measured from a **short**, $\lvert\tilde V\rvert\propto\lvert\sin\beta d\rvert$ and $\lvert\tilde I\rvert\propto\lvert\cos\beta d\rvert$; from an **open**, swap them. The $n$-th resonance fits $n$ half waves (same ends) or $2n-1$ quarter waves (different ends) into $\ell$.

## 3. Quarter-wave and half-wave sections

> [!key] Two lengths worth memorizing
> $$
> \begin{gathered}
> \ell = \frac\lambda4:\quad Z_{\text{in}}Z_L = Z_0^2,\qquad \tilde I_L = -j\,\frac{\tilde V_{\text{in}}}{Z_0},\qquad \tilde V_L = -jZ_0\,\tilde I_{\text{in}},\\[6pt]
> \ell = \frac\lambda2:\quad Z_{\text{in}} = Z_L,\qquad \tilde V_{\text{in}} = -\tilde V_L,\qquad \tilde I_{\text{in}} = -\tilde I_L .
> \end{gathered}
> $$
> A quarter-wave section **inverts** the load ($Z_0^2/Z_L$: a short looks open, a large resistance looks small). A half-wave section **repeats** it with the sign of $\tilde V$ and $\tilde I$ flipped. Both follow from $e^{\pm j\beta\ell} = \pm j$ and $-1$ in the box of §1.

Power on a lossless line is the same at every $d$: $P = \tfrac12\text{Re}\{\tilde V\tilde I^*\}$. Compute it at the input (a voltage divider with $Z_{\text{in}}$), and it is the load's.

**Reflection coefficient along the line** (notes §34; one multiple-choice item on SP18):

$$
\Gamma(d) = \frac{V^-e^{-j\beta d}}{V^+e^{j\beta d}} = \Gamma_Le^{-j2\beta d},\qquad Z(d) = Z_0\,\frac{1+\Gamma(d)}{1-\Gamma(d)} .
$$

Its magnitude is the same everywhere on a lossless line; its phase falls by $2\beta d$, so it repeats every $\lambda/2$.

> [!recipe] The exam items, in the order they are usually asked
> 1. **Wavelength first:** $\lambda = v/f$ with $f = \omega/2\pi$. Every length is then a fraction of $\lambda$.
> 2. **Translate the measurement:** zero current into the line means $Z_{\text{in}} = \infty$; zero voltage across it means $Z_{\text{in}} = 0$. In a series circuit, zero resistor current means the line's input is an open circuit.
> 3. **Pick the row** of the stub table (or of the resonance table) and solve for $\ell$ in units of $\lambda$, or for $f$.
> 4. **Where else is the line a short or an open?** Voltage nulls are every $\lambda/2$ starting at a short (every $\lambda/2$ starting $\lambda/4$ from an open); the line looks like a short circuit at each voltage null.
> 5. **Adding an element:** a series element cannot unblock an open circuit ($\infty + Z = \infty$); a parallel one can. A parallel element cannot change a short circuit; a series one can.

> [!trap] Where the points go
> - $d$ runs from the load **toward the generator**: $e^{+j\beta d}$ is the wave going toward the load. The bounce-diagram $z$ runs the other way.
> - The $-$ sign in $\tilde I(d)$. With $\Gamma_L = -1$ the two current terms **add** (current maximum at a short), the voltage terms subtract.
> - "Lowest resonance" depends on the ends: $\lambda/2$ for like ends, $\lambda/4$ for unlike ends.
> - Doubling the frequency doubles $\beta\ell$: a $\lambda/4$ stub becomes a $\lambda/2$ stub, so an open circuit turns into a short.
> - $Z_{\text{in}} = Z_0^2/Z_L$ holds only at $\ell = \lambda/4$ (and $3\lambda/4$, …), not "for a quarter of the line".
> - A stub that draws no current from the source still carries current **inside** itself (S1).

## 4. Worked twins

New numbers and at least one changed detail in each, as everywhere on this site; the official keys do not apply. Work each on paper before opening the solution. More of the same kind: [[practice/31-resonances-of-line-segments#317-a-resonator-from-two-zero-readings|31.7 A resonator from two zero readings]] · [[practice/32-stubs-and-input-impedance#327-a-shorted-line-that-stops-the-current|32.7 A shorted line that stops the current]] · [[practice/33-half-and-quarter-wave-transformers#337-one-line-at-three-frequencies|33.7 One line at three frequencies]].

### S1 An open stub that blocks the source

> [!hard] Hard · stub input impedance · resonance
> A lossless line with $Z_0 = 75\ \Omega$ and $v = 2.4\times10^8$ m/s is **open-circuited** at its load end. Its input is connected in series with a resistor $R = 150\ \Omega$ and an ideal source $\tilde F = 6\angle0^\circ$ V at $f = 60$ MHz.
> (a) Find the wavelength on the line.
> (b) The resistor current is found to be zero. What is $Z(\ell)$, and what are the possible lengths $\ell$?
> (c) For the shortest length: find $\tilde V$ at the input and at the open end, where on the stub the voltage is zero, and the largest current amplitude on the stub.
> (d) The frequency is halved to 30 MHz with the same stub. Find the resistor current.
> (e) Back at 60 MHz, a capacitor is added at the stub's input and the resistor current is no longer zero. Is it in series or in parallel with the stub?
>
> *Source: SP17 Exam 3 #6 and SP18 Exam 3 #4(a) style, re-parameterized: an open stub instead of a shorted one, new line and source, parts (c)–(d) added.*

> [!hint]- Hint
> Zero current through a series resistor means the stub's input is an open circuit. For an open stub $Z(\ell) = -jZ_0\cot\beta\ell$: when is that infinite? With no drop across $R$, the whole source voltage sits across the stub input.

> [!solution]- Solution
> **(a)** $\lambda = v/f = 2.4\times10^8/6\times10^7 = 4$ m.
>
> **(b)** $\tilde I_R = 0$ in a series loop requires $Z(\ell) = \infty$. Open stub: $Z(\ell) = -jZ_0\cot\beta\ell = \infty$ when $\beta\ell = n\pi$, so $\ell = n\lambda/2 = 2, 4, 6,\ldots$ m. (A half-wave line repeats its load, and the load is an open.)
>
> **(c)** $\ell = 2$ m. No current, so no drop across $R$: $\tilde V(\ell) = \tilde F = 6$ V. On the stub $\tilde V(d) = 2V^+\cos\beta d$, and $\tilde V(\ell) = 2V^+\cos\pi = -2V^+ = 6$ V gives the open-end voltage $\tilde V(0) = 2V^+ = -6$ V: the same size, opposite sign. The voltage is zero where $\cos\beta d = 0$: $d = \lambda/4 = 1$ m from the open end. The current $\tilde I(d) = (2jV^+/Z_0)\sin\beta d$ is largest there: $6/75 = 80$ mA.
>
> **(d)** At 30 MHz $\lambda = 8$ m and the stub is $\lambda/4$: $Z(\ell) = -jZ_0\cot(\pi/2) = 0$. The stub is a short circuit, so $\tilde I_R = \tilde F/R = 6/150 = 40\angle0^\circ$ mA and $\tilde V(\ell) = 0$.
>
> **(e)** In parallel. In series the total is $\infty + 1/j\omega C = \infty$ and the loop stays open. In parallel the capacitor gives the current a path around the stub.
>
> **Check:** energy. At 60 MHz the source delivers no average power (no current); the stub stores energy and returns it. At 30 MHz the resistor dissipates $\tfrac12(0.04)^2(150) = 0.12$ W and the reactive stub none.
>
> **Answer.** (a) 4 m. (b) $Z(\ell) = \infty$; $\ell = n\lambda/2 = 2n$ m. (c) $\tilde V(\ell) = 6$ V, $\tilde V(0) = -6$ V, null at $d = 1$ m, $\lvert\tilde I\rvert_{\max} = 80$ mA. (d) 40 mA. (e) In parallel.

### S2 A quarter-wave section between source and load

> [!medium] Medium · quarter-wave transformer · power
> A source $\tilde V_g = 12\angle0^\circ$ V with internal resistance $R_g = 60\ \Omega$ feeds a load $Z_L = 20\ \Omega$ through a lossless line with $Z_0 = 60\ \Omega$ whose length is $\lambda/4$ at the source frequency.
> (a) Find $Z_{\text{in}}$, $\tilde V_{\text{in}}$ and $\tilde I_{\text{in}}$.
> (b) Find $\tilde I_L$ and $\tilde V_L$.
> (c) Find the average power delivered to the load.
> (d) Repeat (a) and (c) if the line is $\lambda/2$ long instead.
>
> *Source: SP18 Exam 3 #4(b) style, re-parameterized: new source, line and load; the load phasors and the power added.*

> [!hint]- Hint
> $Z_{\text{in}} = Z_0^2/Z_L$, then a voltage divider. The load current follows from the input **voltage**: $\tilde I_L = -j\tilde V_{\text{in}}/Z_0$.

> [!solution]- Solution
> **(a)** $Z_{\text{in}} = Z_0^2/Z_L = 3600/20 = 180\ \Omega$. Divider: $\tilde V_{\text{in}} = 12\cdot\dfrac{180}{180+60} = 9$ V, $\tilde I_{\text{in}} = 12/240 = 50$ mA.
>
> **(b)** $\tilde I_L = -j\tilde V_{\text{in}}/Z_0 = -j\,9/60 = -j0.15$ A, and $\tilde V_L = \tilde I_LZ_L = -j3$ V. (Also $\tilde V_L = -jZ_0\tilde I_{\text{in}} = -j(60)(0.05)$ ✓.) The load quantities lag the input by 90°: a quarter period of travel.
>
> **(c)** $P_L = \tfrac12\lvert\tilde I_L\rvert^2R_L = \tfrac12(0.15)^2(20) = 0.225$ W. At the input, $\tfrac12\text{Re}\{\tilde V_{\text{in}}\tilde I_{\text{in}}^*\} = \tfrac12(9)(0.05) = 0.225$ W ✓: a lossless line passes on all it receives.
>
> **(d)** $Z_{\text{in}} = Z_L = 20\ \Omega$, $\tilde V_{\text{in}} = 12\cdot\tfrac{20}{80} = 3$ V, $\tilde V_L = -3$ V, $P_L = \tfrac12(3)^2/20 = 0.225$ W.
>
> **Check:** the power is the same in (c) and (d) because $180\ \Omega$ and $20\ \Omega$ are mismatched to $R_g = 60\ \Omega$ by the same ratio ($180\cdot20 = 60^2$). Both are below the matched maximum $\lvert\tilde V_g\rvert^2/8R_g = 0.3$ W.
>
> **Answer.** (a) $180\ \Omega$, $9\angle0^\circ$ V, $50\angle0^\circ$ mA. (b) $\tilde I_L = 0.15\angle{-90^\circ}$ A, $\tilde V_L = 3\angle{-90^\circ}$ V. (c) 0.225 W. (d) $20\ \Omega$, 3 V, 0.225 W.

### S3 Resonances from two measurements

> [!hard] Hard · resonance · standing waves
> A lossless line of length $\ell = 60$ m with $v = 1.5\times10^8$ m/s supports resonant oscillations. In sinusoidal steady state the current phasor is zero at the input ($\tilde I_{\text{in}} = 0$ at $d = \ell$) and zero at the load ($\tilde I_L = 0$).
> (a) What are $Z_{\text{in}}$ and $Z_L$ for these resonances?
> (b) Find the three lowest resonant frequencies.
> (c) At the second resonance: where are the voltage nulls, and what is the shortest distance from the load at which the line looks like a short circuit?
> (d) The load end is now short-circuited ($\tilde V_L = 0$), still with $\tilde I_{\text{in}} = 0$. Find the three lowest resonant frequencies.
>
> *Source: SP19 Exam 3 #5 and FA23 Exam 3 #7 style, re-parameterized: open at both ends (both exams have one short and one open), a new line, and the unlike-ends case as part (d).*

> [!hint]- Hint
> Zero current with non-zero voltage is an open circuit. Like ends hold whole half-waves; unlike ends hold odd quarter-waves. From an open end $\lvert\tilde V\rvert\propto\lvert\cos\beta d\rvert$.

> [!solution]- Solution
> **(a)** $Z = \tilde V/\tilde I$ with $\tilde I = 0$ and $\tilde V\ne0$: $Z_{\text{in}} = \infty$ and $Z_L = \infty$. Both ends are open.
>
> **(b)** From the open load, $\tilde I(d)\propto\sin\beta d$. It must vanish again at $d = \ell$: $\beta\ell = n\pi$, $\ell = n\lambda/2$, so
> $$
> f_n = \frac{nv}{2\ell} = n\,\frac{1.5\times10^8}{120} = 1.25,\ 2.5,\ 3.75\ \text{MHz}.
> $$
>
> **(c)** Second resonance: $\lambda = \ell = 60$ m. $\lvert\tilde V(d)\rvert\propto\lvert\cos\beta d\rvert$ is zero at $d = \lambda/4$ and $3\lambda/4$: 15 m and 45 m from the load. The line looks like a short where $\tilde V = 0$ with $\tilde I\ne0$: first at $d = \lambda/4 = 15$ m. (Current nulls: $d = 0$, 30 m, 60 m.)
>
> **(d)** Unlike ends: from the short, $\tilde I(d)\propto\cos\beta d$ must vanish at $d = \ell$, so $\beta\ell = (2n-1)\pi/2$ and
> $$
> f_n = \frac{(2n-1)v}{4\ell} = (2n-1)(0.625\ \text{MHz}) = 0.625,\ 1.875,\ 3.125\ \text{MHz}.
> $$
>
> **Check:** the unlike-ends frequencies fall halfway between the like-ends ones, and each family is evenly spaced by $v/2\ell = 1.25$ MHz.
>
> **Answer.** (a) $Z_{\text{in}} = Z_L = \infty$. (b) 1.25, 2.5, 3.75 MHz. (c) Voltage nulls 15 m and 45 m from the load; short-circuit input first at $d = 15$ m $= \lambda/4$. (d) 0.625, 1.875, 3.125 MHz.

### S4 An open stub at four frequencies

> [!medium] Medium · stub input impedance · multiple choice
> A lossless line of length $\ell$ and characteristic impedance $Z_0$ is open-circuited at the load end. Its lowest **series** resonance ($Z_{\text{in}} = 0$) is at $\omega_0$.
> (a) With $V^+$ a non-zero constant, write $\tilde V(d)$ and $\tilde I(d)$.
> (b) For each of $\omega = \tfrac12\omega_0$, $\tfrac32\omega_0$, $2\omega_0$, $3\omega_0$, state whether $Z_{\text{in}} = Z(\ell)$ is zero, infinite, inductive or capacitive.
>
> *Source: SP18 Exam 3 #1(viii)–(x) style, re-parameterized: an open load, four frequencies, and the reactance values asked.*

> [!hint]- Hint
> $Z(\ell) = -jZ_0\cot\beta\ell$ and $\beta\ell$ is proportional to $\omega$. What is $\beta\ell$ at $\omega_0$?

> [!solution]- Solution
> **(a)** Open load: $\Gamma_L = +1$, $V^- = V^+$. $\tilde V(d) = V^+(e^{j\beta d}+e^{-j\beta d}) = 2V^+\cos\beta d$ and $\tilde I(d) = \dfrac{V^+}{Z_0}(e^{j\beta d}-e^{-j\beta d}) = \dfrac{2jV^+}{Z_0}\sin\beta d$.
>
> **(b)** $Z(\ell) = -jZ_0\cot\beta\ell$ first vanishes at $\beta\ell = \pi/2$: at $\omega_0$ the stub is a quarter wave, and at any other frequency $\beta\ell = \dfrac\pi2\dfrac{\omega}{\omega_0}$.
>
> | $\omega$ | $\beta\ell$ | $Z(\ell)$ | |
> |---|---|---|---|
> | $\tfrac12\omega_0$ | $\pi/4$ | $-jZ_0$ | capacitive |
> | $\tfrac32\omega_0$ | $3\pi/4$ | $+jZ_0$ | inductive |
> | $2\omega_0$ | $\pi$ | $\infty$ | parallel resonance: a half-wave stub repeats its open |
> | $3\omega_0$ | $3\pi/2$ | $0$ | the next series resonance |
>
> **Watch out:** for a **shorted** stub the lowest series resonance is at $\ell = \lambda/2$, so the same four frequencies give a different table.
>
> **Answer.** (a) $\tilde V = 2V^+\cos\beta d$, $\tilde I = (2jV^+/Z_0)\sin\beta d$. (b) Capacitive ($-jZ_0$); inductive ($+jZ_0$); infinite; zero.

### S5 The reflection coefficient along the line

> [!easy] Easy · true or false · generalized reflection coefficient
> A lossless line with $Z_0 = 50\ \Omega$ ends in $Z_L = 150\ \Omega$. True or false?
> (a) $\lvert\Gamma(d)\rvert = \tfrac12$ at every point of the line.
> (b) The phase of $\Gamma(d)$ is the same at every point.
> (c) $\Gamma(d)$ is the ratio of the reflected to the incident voltage phasor at $d$, anywhere on the line.
> (d) $\Gamma(d)$ repeats every $\lambda/2$.
> (e) At $d = \lambda/4$ the line impedance is $16.7\ \Omega$.
>
> *Source: SP18 Exam 3 #1(vi) style, with numbers and two added statements.*

> [!solution]- Solution
> $\Gamma_L = (150-50)/(150+50) = \tfrac12$ and $\Gamma(d) = \Gamma_Le^{-j2\beta d}$.
> (a) **True**: the exponential has unit magnitude. (b) **False**: the phase is $-2\beta d$; $\Gamma(\lambda/8) = -j/2$, $\Gamma(\lambda/4) = -\tfrac12$. (c) **True**: that is its definition, $V^-e^{-j\beta d}/V^+e^{j\beta d}$. (d) **True**: $2\beta(\lambda/2) = 2\pi$. (e) **True**: $Z = Z_0\dfrac{1+\Gamma}{1-\Gamma} = 50\cdot\dfrac{1/2}{3/2} = 16.7\ \Omega = Z_0^2/Z_L$, the quarter-wave rule.
>
> **Answer.** True, false, true, true, true.

### Sources for this page

Course notes §31 (resonances of open and shorted line segments), §32 (input impedance of stubs, series and parallel resonance), §33 (half- and quarter-wave transformers and the current-forcing relations), §34 (the reflection coefficient along the line), in the notes' convention ($d$ from the load). The twins are the site's own, modelled on the Exam 3 items named in their *Source* lines; every number is computed in `tools/build14/checks/twins.py` and re-derived by a time-domain line simulation, a spectrum of the free oscillations and a lumped-ladder model in `tools/build14/checks/review_twins.py`.
