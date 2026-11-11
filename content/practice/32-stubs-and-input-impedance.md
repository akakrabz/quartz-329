---
title: "Practice — Lecture 32: Stubs and input impedance"
description: "8 practice problems (4 easy, 2 medium, 2 hard) on shorted and open stubs in sinusoidal steady state: jZ₀ tan βℓ and −jZ₀ cot βℓ, inductive and capacitive lengths, a stub as a lumped inductor, series and parallel resonance, a stub filter, the standing wave inside a resonant stub, a stub that blocks a source, and tuning a stub with a capacitor; hints on the medium and hard ones, a worked solution for each."
tags: [practice, transmission-lines]
lecture: 32
---

*Practice for [[4-transmission-lines/32-input-impedance-and-microwave-resonators|Lecture 32]] · concepts: [[concepts/stub-input-impedance]] · [[concepts/line-resonances]] · all practice: [[practice/index|hub]] · by difficulty: [[practice/easy|easy]] · [[practice/medium|medium]] · [[practice/hard|hard]] · [[practice/topics|by topic]]*

*After the scope of FA26 Midterm 3, which covers Lectures 1–30 ([[exams/index#the-scope|scope]]).*

Work each problem on paper first. Open the **hint** only when stuck, and the **solution** only after you have an answer you would hand in. Every answer here has been checked numerically.

The page runs on three rules, with $d$ measured from the load ($d = \ell$ is the input) and $\beta\ell = 2\pi\ell/\lambda$:
- $\tilde V(d) = V^+e^{j\beta d}+V^-e^{-j\beta d}$, $\tilde I(d) = (V^+e^{j\beta d}-V^-e^{-j\beta d})/Z_0$.
- Shorted stub: $\tilde V = j2V^+\sin\beta d$, $\tilde I = (2V^+/Z_0)\cos\beta d$, $Z(\ell) = jZ_0\tan\beta\ell$. Open stub: $\tilde V = 2V^+\cos\beta d$, $\tilde I = (j2V^+/Z_0)\sin\beta d$, $Z(\ell) = -jZ_0\cot\beta\ell$.
- Series resonance: $Z(\ell) = 0$ (a short). Parallel resonance: $Z(\ell) = \infty$ (an open).

## Easy

### 32.1 Five stubs

> [!easy] Easy · stub input impedance
> Stubs are cut from a lossless 50 Ω line. Find the input impedance of each and say whether it is inductive, capacitive, a short or an open:
> (a) shorted, $\ell = \lambda/8$; (b) shorted, $\ell = 3\lambda/8$; (c) open, $\ell = \lambda/8$; (d) open, $\ell = \lambda/6$; (e) shorted, $\ell = \lambda/2$.
>
> *Source: original.*

> [!solution]- Solution
> $\beta\ell = 2\pi\ell/\lambda$: 45°, 135°, 45°, 60°, 180°.
> (a) $j50\tan45^\circ = j50\ \Omega$, inductive. (b) $j50\tan135^\circ = -j50\ \Omega$, capacitive. (c) $-j50\cot45^\circ = -j50\ \Omega$, capacitive. (d) $-j50\cot60^\circ = -j50/\sqrt3 = -j28.9\ \Omega$, capacitive. (e) $j50\tan180^\circ = 0$: a short circuit.
>
> **Answer.** (a) $j50\ \Omega$, inductive. (b) $-j50\ \Omega$, capacitive. (c) $-j50\ \Omega$, capacitive. (d) $-j28.9\ \Omega$, capacitive. (e) 0, a short.

### 32.2 Stub facts, true or false

> [!easy] Easy · true or false · stub input impedance
> True or false, for lossless stubs in sinusoidal steady state?
> (a) The input impedance of a shorted stub is purely imaginary at every frequency.
> (b) A shorted stub shorter than a quarter wavelength is capacitive.
> (c) A quarter-wave open stub looks like a short circuit at its input.
> (d) Lengthening a stub by half a wavelength does not change its input impedance.
> (e) At parallel resonance no current flows anywhere on the stub.
> (f) With $d$ measured from the load, $V^+e^{+j\beta d}$ is the wave travelling toward the load.
>
> *Source: original.*

> [!solution]- Solution
> (a) **True**: $jZ_0\tan\beta\ell$; no resistance, no average power.
> (b) **False**: $\tan\beta\ell>0$ for $\beta\ell<90^\circ$, so it is inductive. The open stub is the capacitive one.
> (c) **True**: $-jZ_0\cot90^\circ = 0$.
> (d) **True**: $\tan$ and $\cot$ have period $\pi$ in $\beta\ell$.
> (e) **False**: no current enters at the input, but inside $\lvert\tilde I\rvert$ reaches $2\lvert V^+\rvert/Z_0$ a quarter wave from the input.
> (f) **True**: $d = -z$, so $e^{+j\beta d} = e^{-j\beta z}$, the $+z$ wave.
>
> **Answer.** True, false, true, true, false, true.

### 32.3 The stub that should have blocked

> [!easy] Easy · find the error · stub input impedance
> A shorted stub must look like an open circuit at 150 MHz. It is cut from 75 Ω cable with $v = 2\times10^8$ m/s. A student writes: "$\lambda = c/f = 2$ m, so $\ell = \lambda/4 = 0.5$ m."
> Find the error, give the right length, and find what the 0.5 m stub actually looks like at 150 MHz.
>
> *Source: original.*

> [!solution]- Solution
> The wavelength **on the stub** uses the cable's speed: $\lambda = v/f = (2\times10^8)/(1.5\times10^8) = 1.33$ m. The quarter-wave length is $\ell = 0.333$ m.
>
> The 0.5 m stub has $\beta\ell = 2\pi(0.5)/1.333 = 0.75\pi = 135^\circ$, so $Z = j75\tan135^\circ = -j75\ \Omega$: a capacitor of reactance 75 Ω, not an open circuit.
>
> **Answer.** Use $\lambda = v/f = 1.33$ m: $\ell = 33.3$ cm. The 0.5 m stub is $3\lambda/8$ long and looks like $-j75\ \Omega$.

### 32.4 A stub as an inductor

> [!easy] Easy · stub input impedance · lumped equivalents
> A shorted stub on a line with $Z_0 = 100\ \Omega$ and $v = 2\times10^8$ m/s must act as a 50 nH inductor at 100 MHz.
> (a) What reactance is needed?
> (b) Find the shortest stub length.
> (c) Compare with the short-stub estimate $\ell\approx L/\mathcal{L}$.
>
> *Source: original.*

> [!solution]- Solution
> (a) $X = \omega L = 2\pi(10^8)(50\times10^{-9}) = 31.4\ \Omega$.
>
> (b) $Z_0\tan\beta\ell = 31.4$ gives $\tan\beta\ell = 0.314$, $\beta\ell = 0.304$ rad. With $\beta = 2\pi f/v = \pi$ rad/m, $\ell = 0.304/\pi = 9.69$ cm.
>
> (c) $\mathcal{L} = Z_0/v = 0.5\ \mu$H/m, so $\ell\approx(50\ \text{nH})/(0.5\ \mu\text{H/m}) = 10$ cm: 3 % long, because $\tan x>x$.
>
> **Answer.** (a) 31.4 Ω. (b) 9.69 cm. (c) 10 cm from the estimate, 3 % high.

## Medium

### 32.5 A stub across the load

> [!medium] Medium · stub filters · series and parallel resonance
> A source $\tilde F$ with internal resistance $R_g = 50\ \Omega$ feeds a load $R_L = 50\ \Omega$. A shorted stub ($Z_0 = 50\ \Omega$, $\ell = 1.5$ m, $v = 2\times10^8$ m/s) is connected **across** the load.
> (a) Find $H(\omega) = \tilde V_L/\tilde F$ and its magnitude in terms of $\beta\ell$.
> (b) At which frequencies is $\lvert H\rvert = 0$?
> (c) At which frequencies is $\lvert H\rvert$ largest, and how large?
> (d) Find $\lvert H\rvert$ at 50 MHz.
>
> *Source: Kudeki notes, Lecture 32, Example 1 style, with the stub in parallel with the load instead of in series, and a new line.*

> [!hint]- Hint
> In parallel, add admittances: $Y_{\text{stub}} = 1/(jZ_0\tan\beta\ell) = -jY_0\cot\beta\ell$. Then a voltage divider between $R_g$ and the parallel combination.

> [!solution]- Solution
> **(a)** Load and stub in parallel have admittance $Y_p = \tfrac1{50}-\tfrac{j}{50}\cot\beta\ell$. The divider gives
> $$
> H = \frac{1/Y_p}{R_g+1/Y_p} = \frac{1}{1+R_gY_p} = \frac{1}{2-j\cot\beta\ell},\qquad \lvert H\rvert = \frac{1}{\sqrt{4+\cot^2\beta\ell}} .
> $$
>
> **(b)** $\lvert H\rvert = 0$ when $\cot\beta\ell = \infty$: $\beta\ell = n\pi$, the stub's series resonances, where it short-circuits the load. $f = nv/2\ell = n\times66.7$ MHz: 0 (DC), 66.7, 133.3 MHz, …
>
> **(c)** Largest when $\cot\beta\ell = 0$: $\beta\ell = (2n+1)\pi/2$, the parallel resonances, where the stub is an open circuit and might as well not be there. $f = (2n+1)v/4\ell = 33.3, 100, 166.7$ MHz, … and $\lvert H\rvert = \tfrac12$, the plain divider.
>
> **(d)** $\beta\ell = 2\pi(50\times10^6)(1.5)/(2\times10^8) = 0.75\pi$, $\cot = -1$: $\lvert H\rvert = 1/\sqrt5 = 0.447$.
>
> **Check:** compared with the notes' series connection, peaks and nulls have changed places: a shunt stub removes what a series stub passes.
>
> **Answer.** (a) $H = 1/(2-j\cot\beta\ell)$, $\lvert H\rvert = 1/\sqrt{4+\cot^2\beta\ell}$. (b) $n\times66.7$ MHz, DC included. (c) 33.3, 100, 166.7 MHz, …; $\lvert H\rvert = 0.5$. (d) 0.447.

### 32.6 Inside a resonant stub

> [!medium] Medium · stub input impedance · standing waves on lines
> A shorted stub with $Z_0 = 50\ \Omega$ is $3\lambda/4$ long at the frequency of an ideal source $\tilde V_s = 10\angle0^\circ$ V connected across its input.
> (a) Find the input impedance and the current drawn from the source.
> (b) Find $V^+$, then $\tilde V(d)$ and $\tilde I(d)$ on the stub.
> (c) Where is $\lvert\tilde V\rvert$ zero and where is it largest? What current flows through the short?
> (d) How much average power does the source deliver?
>
> *Source: original.*

> [!hint]- Hint
> $\tilde V(d) = j2V^+\sin\beta d$ must equal 10 V at $d = \ell$, where $\beta\ell = 3\pi/2$.

> [!solution]- Solution
> **(a)** $Z(\ell) = j50\tan(3\pi/2) = \infty$: parallel resonance. The source supplies no current.
>
> **(b)** $\tilde V(\ell) = j2V^+\sin(3\pi/2) = -j2V^+ = 10$, so $V^+ = 10/(-2j) = j5$ V. Then
> $$
> \tilde V(d) = j2(j5)\sin\beta d = -10\sin\beta d\ \text{V},\qquad \tilde I(d) = \frac{2(j5)}{50}\cos\beta d = j0.2\cos\beta d\ \text{A}.
> $$
>
> **(c)** $\lvert\tilde V\rvert = 0$ at $d = 0$ and $d = \lambda/2$; it is largest, 10 V, at $d = \lambda/4$ and at the input $d = 3\lambda/4$. Through the short, $\tilde I(0) = j0.2$ A: amplitude 0.2 A, a quarter period ahead of the source voltage. At the input, $\tilde I(\ell) = j0.2\cos(3\pi/2) = 0$ ✓.
>
> **(d)** None: $\tfrac12\text{Re}\{\tilde V\tilde I^*\} = 0$ at the input. The stub was charged once and now only stores energy.
>
> **Answer.** (a) $Z(\ell) = \infty$; no current. (b) $V^+ = j5$ V; $\tilde V = -10\sin\beta d$ V, $\tilde I = j0.2\cos\beta d$ A. (c) Zero at $d = 0$, $\lambda/2$; 10 V at $\lambda/4$, $3\lambda/4$; $j0.2$ A through the short. (d) 0 W.

## Hard

### 32.7 A shorted line that stops the current

> [!hard] Hard · stub input impedance · series and parallel resonance
> A shorted line ($Z_0 = 50\ \Omega$, $v = 2.5\times10^8$ m/s) is connected in series with a resistor $R = 75\ \Omega$ and an ideal source $\tilde F = 9\angle0^\circ$ V at $f = 125$ MHz.
> (a) Find the wavelength on the line.
> (b) The resistor current is zero. What is $Z(\ell)$? List all possible line lengths.
> (c) For the shortest length, find the voltage at the line's input and the current phasor through the short.
> (d) Is there a length, still with zero resistor current, for which the line current is zero at $d = \ell/3$? If so, which?
> (e) With the shortest length of (b), the frequency is raised to 250 MHz. Find the resistor current.
>
> *Source: SP17 Exam 3 #6 and SP18 Exam 3 #4(a) style, re-parameterized: a new line and source, the current in the short, a null at one third of the line instead of a voltage null at mid-line, and a second frequency.*

> [!hint]- Hint
> Zero current in a series loop means the line's input is an open circuit: $jZ_0\tan\beta\ell = \infty$. On a shorted line $\tilde I(d)\propto\cos\beta d$. For (d), impose both conditions on $\beta\ell$.

> [!solution]- Solution
> **(a)** $\lambda = v/f = (2.5\times10^8)/(1.25\times10^8) = 2$ m.
>
> **(b)** $\tilde I_R = 0$ needs $Z(\ell) = \infty$: $\tan\beta\ell = \infty$, $\beta\ell = (2n+1)\pi/2$, so $\ell = (2n+1)\lambda/4 = 0.5, 1.5, 2.5,\ldots$ m.
>
> **(c)** No current, no drop across $R$: $\tilde V(\ell) = \tilde F = 9$ V. With $\ell = \lambda/4$: $\tilde V(\ell) = j2V^+\sin(\pi/2) = j2V^+ = 9$, so $V^+ = -j4.5$ V and
> $$
> \tilde I(0) = \frac{2V^+}{Z_0} = \frac{-j9}{50} = -j0.18\ \text{A}.
> $$
> The short carries 0.18 A although the source supplies none.
>
> **(d)** $\tilde I(d)\propto\cos\beta d = 0$ at $d = \ell/3$ needs $\beta\ell/3 = \pi/2+m\pi$, that is $\beta\ell = 3\pi/2+3m\pi$. Zero resistor current needs $\beta\ell = \pi/2+n\pi$. Both hold for $\beta\ell = 3\pi/2$ ($m = 0$, $n = 1$): **yes**, $\ell = 3\lambda/4 = 1.5$ m, with the null at $d = 0.5$ m, a quarter wave from the short. (Next: $\beta\ell = 9\pi/2$, $\ell = 4.5$ m.)
>
> **(e)** At 250 MHz $\lambda = 1$ m and the 0.5 m line is $\lambda/2$: $Z(\ell) = j50\tan\pi = 0$. The line is a short circuit and $\tilde I_R = 9/75 = 0.12\angle0^\circ$ A.
>
> **Check:** in (c), $\tilde V(d) = j2V^+\sin\beta d = 9\sin\beta d$ V: 9 V at the input, 0 at the short ✓.
>
> **Answer.** (a) 2 m. (b) $Z(\ell) = \infty$; $\ell = (2n+1)(0.5\ \text{m})$. (c) 9 V; $-j0.18$ A. (d) Yes: $\ell = 1.5$ m ($3\lambda/4$). (e) $0.12\angle0^\circ$ A.

### 32.8 Tuning a stub with a capacitor

> [!hard] Hard · stub filters · series and parallel resonance
> A shorted air stub ($Z_0 = 50\ \Omega$, $\ell = 0.6$ m, $v = 3\times10^8$ m/s) is in series with a load $R_L = 50\ \Omega$ and a source $\tilde F$; $H = \tilde V_L/\tilde F$.
> (a) With nothing else in the loop, find the lowest non-zero frequency at which $\lvert H\rvert = 1$ and the lowest at which $\lvert H\rvert = 0$.
> (b) A capacitor $C$ is added in series. Find the $C$ that puts a transmission peak, $\lvert H\rvert = 1$, at 62.5 MHz.
> (c) With that capacitor, find $\lvert H\rvert$ at 125 MHz and as $f\to0$.
> (d) With that capacitor, find $\lvert H\rvert$ at 31.25 MHz.
> (e) Why did the capacitor move the peak but not the null?
>
> *Source: Kudeki notes, Lecture 32, Examples 1–3 style, re-parameterized: a new stub, the capacitor chosen to place a peak, and two spot values.*

> [!hint]- Hint
> $H = R_L/(R_L+jX)$ with $X = Z_0\tan\beta\ell-1/\omega C$. A peak needs $X = 0$; a null needs $X = \infty$. At 62.5 MHz, $\beta\ell = \pi/4$.

> [!solution]- Solution
> **(a)** $\lvert H\rvert = 1$ at series resonance, $\beta\ell = \pi$: $f = v/2\ell = 250$ MHz. $\lvert H\rvert = 0$ at parallel resonance, $\beta\ell = \pi/2$: $f = v/4\ell = 125$ MHz.
>
> **(b)** At 62.5 MHz, $\beta\ell = 2\pi(62.5\times10^6)(0.6)/(3\times10^8) = \pi/4$ and the stub is $+j50\ \Omega$. The capacitor must cancel it: $1/\omega C = 50\ \Omega$,
> $$
> C = \frac{1}{2\pi(62.5\times10^6)(50)} = 50.9\ \text{pF}.
> $$
>
> **(c)** At 125 MHz the stub is an open circuit: $\lvert H\rvert = 0$, capacitor or not. As $f\to0$ the capacitor is an open circuit: $\lvert H\rvert\to0$.
>
> **(d)** At 31.25 MHz, $\beta\ell = \pi/8$: stub $+j50\tan22.5^\circ = +j20.7\ \Omega$; capacitor $-j100\ \Omega$ (half the frequency, twice the reactance). $X = -79.3\ \Omega$ and
> $$
> \lvert H\rvert = \frac{50}{\sqrt{50^2+79.3^2}} = 0.533 .
> $$
>
> **(e)** A peak is a zero of the total reactance, and adding $-1/\omega C$ shifts where the sum crosses zero. A null is where the stub's reactance is infinite, and a finite added reactance cannot change that. The capacitor also adds a null of its own at DC.
>
> **Answer.** (a) 250 MHz; 125 MHz. (b) 50.9 pF. (c) 0 and 0. (d) 0.533. (e) Zeros of a sum of reactances move when a term is added; its poles do not.

### Sources for this page
Kudeki notes, Lecture 32: $Z(\ell) = jZ_0\tan\beta\ell$ and its remarks (32.1–32.4), Example 1 (32.5, with the stub in parallel), Examples 2–3 (32.8). Past exams, re-parameterized: SP17 Exam 3 #6 and SP18 Exam 3 #4(a) (32.7). The rest is original. Every number is checked by `practice/checks/L32.py` and re-solved independently in `practice/review/R32.py` (time-domain simulation of the line and a lumped-ladder model of the stub).

*Previous: [[practice/31-resonances-of-line-segments|Lecture 31 practice]] · next: [[practice/33-half-and-quarter-wave-transformers|Lecture 33 practice]] · [[practice/index|all practice]]*
