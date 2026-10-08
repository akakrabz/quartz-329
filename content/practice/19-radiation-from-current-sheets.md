---
title: "Practice — Lecture 19: d'Alembert solutions and radiation from current sheets"
description: "12 practice problems (5 easy, 3 medium, 4 hard) on uniform plane TEM waves, the fields radiated by current sheets in any plane and orientation (E = −(η/2)Jₛ on both sides, H = ½Jₛ × n̂), boundary-condition checks, records and snapshots for rect, ramp and triangle currents, sheets in dielectric and magnetic media, two sheets, finding Jₛ(t) from a measured field, cosine currents with β and λ, the instantaneous Poynting vector and the magnetic-to-electric force ratio, each with a folded hint and a worked solution."
tags: [practice, waves]
lecture: 19
---

*Practice for [[3-maxwell-and-waves/19-dalembert-solutions-and-radiation-from-current-sheets|Lecture 19]] · concepts: [[concepts/current-sheet-radiation]] · [[concepts/poynting-vector]] · [[concepts/plane-waves]] · [[concepts/intrinsic-impedance]] · all practice: [[practice/index|hub]] · by difficulty: [[practice/easy|easy]] · [[practice/medium|medium]] · [[practice/hard|hard]] · [[practice/topics|by topic]]*

Work each problem on paper first. Open the **hint** only when stuck, and the **solution** only after you have an answer you would hand in. Every answer here has been checked numerically.

One recipe does almost every problem on this page. For a sheet carrying $\mathbf{J}_s(t)$, let $\hat n$ point from the sheet toward the field point and let $d$ be the distance from the sheet. Then
$$
\mathbf{E} = -\frac\eta2\,\mathbf{J}_s\Big(t - \frac dv\Big),\qquad \mathbf{H} = \frac12\,\mathbf{J}_s\Big(t - \frac dv\Big)\times\hat n,\qquad \mathbf{E}\times\mathbf{H}\parallel+\hat n .
$$

## Easy

### 19.1 Which one is a plane wave

> [!easy] Easy · multiple choice · plane waves
> In free space, $f$ is a smooth pulse (in V/m), $\eta_0$ is the intrinsic impedance and $c$ the speed of light. Which **one** of these field pairs is a uniform plane TEM wave?
>
> (a) $\mathbf{E} = \hat{z}\,f(t - z/c)$, $\ \mathbf{H} = \hat{x}\,f(t - z/c)/\eta_0$
>
> (b) $\mathbf{E} = \hat{y}\,f(t - z/c)$, $\ \mathbf{H} = \hat{x}\,f(t - z/c)/\eta_0$
>
> (c) $\mathbf{E} = \hat{z}\,f(t + x/c)$, $\ \mathbf{H} = \hat{y}\,f(t + x/c)/\eta_0$
>
> (d) $\mathbf{E} = \hat{x}\,e^{-y^2/a^2}f(t - z/c)$, $\ \mathbf{H} = \hat{y}\,e^{-y^2/a^2}f(t - z/c)/\eta_0$, with $a = 1$ m
>
> (e) $\mathbf{E} = \hat{x}\,f(t - z/c)$, $\ \mathbf{H} = \hat{y}\,f(t - z/c)/(2\eta_0)$
>
> *Source: original (the notes' classification of d'Alembert solutions as uniform plane TEM waves).*

> [!hint]- Hint
> Run four tests on each pair: are $\mathbf{E}$ and $\mathbf{H}$ perpendicular to the travel? Does $\mathbf{E}\times\mathbf{H}$ point along the travel read from the argument? Is $\lvert\mathbf{E}\rvert/\lvert\mathbf{H}\rvert = \eta_0$? Is the field the same everywhere on a plane of constant phase?

> [!solution]- Solution
> **(c)** passes every test. The argument $t + x/c$ means travel toward $-x$, so $\hat u = -\hat{x}$. Both fields are perpendicular to $\hat{x}$, and the pairing rule gives $\mathbf{H} = \hat u\times\mathbf{E}/\eta_0 = (-\hat{x}\times\hat{z})\,f/\eta_0 = +\hat{y}\,f/\eta_0$, exactly what is written. Check: $\mathbf{E}\times\mathbf{H}\parallel\hat{z}\times\hat{y} = -\hat{x}$ ✓.
>
> Why the others fail:
> - (a) $\mathbf{E}$ points along the travel ($\hat{z}$). That is not TEM, and it violates Gauss's law in a source-free region: $\nabla\cdot\mathbf{E} = \partial E_z/\partial z\neq0$.
> - (b) Transverse, with the right ratio, but $\mathbf{E}\times\mathbf{H}\parallel\hat{y}\times\hat{x} = -\hat{z}$, while $t - z/c$ says the wave moves toward $+z$. The partner of $\hat{y}f(t - z/c)$ is $-\hat{x}\,f/\eta_0$. As written, the pair fails Faraday's law.
> - (d) The amplitude changes with $y$ on each plane $z$ = const, so the wave is not uniform. It is not even a solution: $\nabla\times\mathbf{E}$ has a $z$ component $-\partial E_x/\partial y\neq0$, but $\mathbf{B}$ has no $z$ component to balance it in Faraday's law.
> - (e) Right directions, wrong ratio: $\lvert\mathbf{E}\rvert/\lvert\mathbf{H}\rvert = 2\eta_0$. Faraday's law and the Ampère–Maxwell law then both fail by a factor of 2.
>
> **Answer.** (c).

### 19.2 A sheet on the y = 0 plane

> [!easy] Easy · current sheet radiation · boundary conditions
> A sheet on the plane $y = 0$ in free space carries $\mathbf{J}_s = \hat{z}\,g(t)$ A/m. Use $c = 300$ m/µs and $\eta_0\approx120\pi\ \Omega$.
> (a) Write $\mathbf{E}$ and $\mathbf{H}$ for $y>0$ and for $y<0$ in terms of $g$.
> (b) The current is $g = 0.5$ A/m for $0<t<2$ µs and zero otherwise. Find $\mathbf{E}$ and $\mathbf{H}$ at $y = +150$ m and at $y = -450$ m at $t = 1$ µs.
> (c) Check the result of (a) against the boundary conditions at the sheet.
>
> *Source: Lecture 19 slide 17 style, with the current reversed and numbers added.*

> [!solution]- Solution
> (a) The waves leave the sheet, so $\hat n = +\hat{y}$ above and $-\hat{y}$ below. With $\hat{z}\times\hat{y} = -\hat{x}$ and $\hat{z}\times(-\hat{y}) = +\hat{x}$:
> $$
> \mathbf{H} = \mp\frac12\,g\Big(t\mp\frac yc\Big)\,\hat{x}\quad(y\gtrless0),\qquad \mathbf{E} = -\frac{\eta_0}{2}\,g\Big(t - \frac{\lvert y\rvert}{c}\Big)\,\hat{z}\quad\text{on both sides}.
> $$
> (b) At $y = +150$ m the delay is $150/300 = 0.5$ µs, so the fields carry the current from $t = 0.5$ µs, which is $0.5$ A/m: $\mathbf{E} = -60\pi(0.5)\,\hat{z} = -30\pi\,\hat{z}\approx-94.2\,\hat{z}$ V/m and $\mathbf{H} = -0.25\,\hat{x}$ A/m. At $y = -450$ m the delay is 1.5 µs, so the field there would come from $t = -0.5$ µs, before the current was switched on: $\mathbf{E} = \mathbf{H} = 0$. The front reaches $-450$ m only at $t = 1.5$ µs.
>
> (c) $\mathbf{E}$ has the same value on both faces, so tangential $\mathbf{E}$ is continuous. For $\mathbf{H}$, with $\hat n = \hat{y}$ from $y<0$ into $y>0$: $\hat{y}\times(\mathbf{H}^+ - \mathbf{H}^-) = \hat{y}\times(-g\,\hat{x}) = +g\,\hat{z} = \mathbf{J}_s$ ✓. Also $\mathbf{E}\times\mathbf{H}\parallel(-\hat{z})\times(-\hat{x}) = +\hat{y}$ above and $(-\hat{z})\times(+\hat{x}) = -\hat{y}$ below: away from the sheet ✓. Right at the sheet, $\mathbf{H} = -0.25\,\hat{x}$ A/m above is the static field $\tfrac12\mathbf{J}_s\times\hat n$ of Lecture 13.
>
> **Answer.** (a) $\mathbf{H} = \mp\tfrac12g(t\mp y/c)\,\hat{x}$ for $y\gtrless0$, $\mathbf{E} = -\tfrac{\eta_0}{2}g(t - \lvert y\rvert/c)\,\hat{z}$. (b) At $y = 150$ m: $\mathbf{E}\approx-94.2\,\hat{z}$ V/m, $\mathbf{H} = -0.25\,\hat{x}$ A/m; at $y = -450$ m: zero (the pulse arrives at 1.5 µs). (c) $\mathbf{E}$ continuous, $\hat{y}\times(\mathbf{H}^+ - \mathbf{H}^-) = \mathbf{J}_s$ ✓.

### 19.3 Sheet facts, true or false

> [!easy] Easy · true or false · current sheet radiation
> A sheet on $z = 0$ in free space carries $\mathbf{J}_s = \hat{x}\,J(t)$. True or false?
>
> (a) $\mathbf{E}$ just above the sheet equals $\mathbf{E}$ just below it.
>
> (b) $\mathbf{H}$ just above the sheet equals $\mathbf{H}$ just below it.
>
> (c) The amplitude of $\mathbf{E}$ at $z = 300$ m is smaller than at $z = 3$ m, because the wave spreads out as it travels.
>
> (d) At the sheet $\mathbf{J}_s\cdot\mathbf{E}<0$, so the current gives energy to the fields.
>
> (e) If all space is filled with a non-magnetic dielectric with $\epsilon_r = 4$ and $J(t)$ is unchanged, the amplitude of $\mathbf{E}$ halves and the amplitude of $\mathbf{H}$ stays the same.
>
> (f) Below the sheet ($z<0$), $\mathbf{E}\times\mathbf{H}$ points along $+\hat{z}$, toward the sheet.
>
> *Source: original.*

> [!solution]- Solution
> (a) **True.** $\mathbf{E} = -\tfrac\eta2\mathbf{J}_s(t - \lvert z\rvert/v)$ on both sides. It must be: tangential $\mathbf{E}$ cannot jump.
>
> (b) **False.** $\mathbf{H} = \tfrac12\mathbf{J}_s\times\hat n$ reverses with $\hat n$: $-\tfrac12J\,\hat{y}$ above, $+\tfrac12J\,\hat{y}$ below. The jump equals the surface current.
>
> (c) **False.** A wave from an *infinite* sheet is a uniform plane wave; it does not spread, so it arrives at 300 m with the same amplitude, just later ($300/c = 1$ µs). Only waves from compact sources (spherical waves) weaken with distance.
>
> (d) **True.** $\mathbf{J}_s\cdot\mathbf{E} = -\tfrac\eta2\lvert\mathbf{J}_s\rvert^2<0$ (for 1 A/m in vacuum, $-188$ W/m²). In a resistor $\mathbf{J}\cdot\mathbf{E}>0$ and the field does work on the charges; here the sign is reversed and the source does work on the field.
>
> (e) **True.** $\eta = \eta_0/\sqrt{\epsilon_r} = \eta_0/2$, so $\lvert\mathbf{E}\rvert = \tfrac\eta2\lvert J\rvert$ drops from 188.4 to 94.2 V/m per A/m. $\lvert\mathbf{H}\rvert = \tfrac12\lvert J\rvert$ (0.5 A/m per A/m) does not contain $\eta$ at all: it is fixed by the jump condition.
>
> (f) **False.** Below the sheet $\mathbf{E}\propto-\hat{x}$ and $\mathbf{H}\propto+\hat{y}$, so $\mathbf{E}\times\mathbf{H}\parallel(-\hat{x})\times\hat{y} = -\hat{z}$: away from the sheet, as on the other side.
>
> **Answer.** (a) T, (b) F, (c) F, (d) T, (e) T, (f) F.

### 19.4 Reading a wave's parameters

> [!easy] Easy · wave parameters · intrinsic impedance
> In a lossless, non-magnetic dielectric, $\mathbf{H} = 0.05\cos(6\pi\times10^{8}\,t - 4\pi z)\,\hat{x}$ A/m ($t$ in s, $z$ in m).
> (a) Find the direction of travel, $\omega$, $f$, $\beta$, $\lambda$ and $v_p$.
> (b) Find $\epsilon_r$ (use $c = 3\times10^{8}$ m/s).
> (c) Find $\eta$ and $\mathbf{E}$.
>
> *Source: original (the slides' wave-parameter table).*

> [!solution]- Solution
> (a) Opposite signs on the $t$ and $z$ terms: travel toward $+z$. Read off the phase $\phi = \omega t - \beta z$: $\omega = 6\pi\times10^{8} = 1.885\times10^{9}$ rad/s, $f = \omega/2\pi = 3\times10^{8}$ Hz = 300 MHz, $\beta = 4\pi = 12.57$ rad/m, $\lambda = 2\pi/\beta = 0.5$ m, $v_p = \omega/\beta = 1.5\times10^{8}$ m/s (check: $\lambda f = 0.5\times3\times10^{8}$ ✓).
>
> (b) $v_p = c/\sqrt{\epsilon_r}$ gives $\epsilon_r = (c/v_p)^2 = 4$.
>
> (c) $\eta = \sqrt{\mu_0/\epsilon} = \mu_0v_p = 4\pi\times10^{-7}\times1.5\times10^{8} = 60\pi\approx188.5\ \Omega$ (the same as $\eta_0/2$). $\mathbf{E} = \eta\,\mathbf{H}\times\hat u$ with $\hat u = \hat{z}$, and $\hat{x}\times\hat{z} = -\hat{y}$:
> $$
> \mathbf{E} = -3\pi\cos(6\pi\times10^{8}\,t - 4\pi z)\,\hat{y}\approx-9.42\cos(6\pi\times10^{8}\,t - 4\pi z)\,\hat{y}\ \text{V/m}.
> $$
> Check: $\mathbf{E}\times\mathbf{H}\parallel(-\hat{y})\times\hat{x} = +\hat{z}$ ✓.
>
> **Answer.** Toward $+z$; $\omega = 6\pi\times10^{8}$ rad/s, $f = 300$ MHz, $\beta = 4\pi$ rad/m, $\lambda = 0.5$ m, $v_p = 1.5\times10^{8}$ m/s; $\epsilon_r = 4$; $\eta = 60\pi\approx188.5\ \Omega$, $\mathbf{E} = -9.42\cos(6\pi\times10^{8}t - 4\pi z)\,\hat{y}$ V/m.

### 19.5 The electric field that flips

> [!easy] Easy · find the error · current sheet radiation · boundary conditions
> A sheet on the plane $x = 0$ in free space carries $\mathbf{J}_s = -\hat{y}\,g(t)$. A student writes:
>
> "For a sheet, $\mathbf{H} = \tfrac12\mathbf{J}_s\times\hat n$. The normal of the plane $x = 0$ is $\hat n = \hat{x}$, so $\mathbf{H} = \tfrac12(-\hat{y}\times\hat{x})\,g = +\tfrac12g\,\hat{z}$. Then $\mathbf{E} = \eta_0\mathbf{H}\times\hat u$ on each side. For $x>0$, $\hat u = \hat{x}$ and $\hat{z}\times\hat{x} = \hat{y}$, so $\mathbf{E} = +\tfrac{\eta_0}{2}g\,\hat{y}$. For $x<0$, $\hat u = -\hat{x}$, so $\mathbf{E} = -\tfrac{\eta_0}{2}g\,\hat{y}$. Like the magnetic field of a static sheet, $\mathbf{E}$ reverses across the current."
>
> (All fields are delayed by $\lvert x\rvert/c$.) Find the slip, correct it, and give $\mathbf{E}$ and $\mathbf{H}$ on both sides.
>
> *Source: original.*

> [!solution]- Solution
> **The slip:** one normal for both sides. In $\tfrac12\mathbf{J}_s\times\hat n$ the normal points from the sheet *toward the field point*, so it is $+\hat{x}$ for $x>0$ and $-\hat{x}$ for $x<0$.
>
> **Fix:** $(-\hat{y})\times(+\hat{x}) = +\hat{z}$ and $(-\hat{y})\times(-\hat{x}) = -\hat{z}$, so
> $$
> \mathbf{H} = \pm\frac12\,g\Big(t\mp\frac xc\Big)\,\hat{z}\quad(x\gtrless0),\qquad \mathbf{E} = +\frac{\eta_0}{2}\,g\Big(t - \frac{\lvert x\rvert}{c}\Big)\,\hat{y}\quad\text{on both sides}.
> $$
> The student's $x>0$ answer was right by luck; on the $x<0$ side both fields have the wrong sign.
>
> **Two red flags the student should have seen:** the student's $\mathbf{E}$ jumps by $\eta_0g$ across the sheet (tangential $\mathbf{E}$ must be continuous), and the student's $\mathbf{H}$ is the same on both sides, so $\hat{x}\times(\mathbf{H}^+ - \mathbf{H}^-) = 0$ instead of $\mathbf{J}_s$. The corrected fields give $\hat{x}\times(g\,\hat{z}) = -g\,\hat{y} = \mathbf{J}_s$ ✓, and $\mathbf{E}$ along $+\hat{y}$ opposes $\mathbf{J}_s$ along $-\hat{y}$, as it always must. For $x<0$: $\mathbf{E}\times\mathbf{H}\parallel\hat{y}\times(-\hat{z}) = -\hat{x}$, away from the sheet ✓.
>
> **Answer.** The student used $\hat n = +\hat{x}$ on both sides. Correct: $\mathbf{H} = +\tfrac12g(t - x/c)\,\hat{z}$ for $x>0$ and $-\tfrac12g(t + x/c)\,\hat{z}$ for $x<0$; $\mathbf{E} = +\tfrac{\eta_0}{2}g(t - \lvert x\rvert/c)\,\hat{y}$ on both sides. $\mathbf{E}$ never reverses across a sheet.

## Medium

### 19.6 A triangle pulse in glass

> [!medium] Medium · current sheet radiation · moving pulses
> A sheet on the plane $y = 0$ carries $\mathbf{J}_s = -\hat{z}\,g(t)$, embedded in a lossless non-magnetic dielectric with $\epsilon_r = 9$ that fills all space. The current is zero for $t<0$, rises linearly to 3 A/m at $t = 1$ ns, falls linearly to zero at $t = 4$ ns, and stays zero. Use $c = 3\times10^{8}$ m/s and $\eta_0\approx120\pi\ \Omega$.
> (a) Find $v$ and $\eta$, and write $\mathbf{E}$ and $\mathbf{H}$ on both sides.
> (b) Probes at $y = +0.5$ m and $y = -0.3$ m record $E_z(t)$ and $H_x(t)$. Describe each record: when it starts, when it peaks, the peak values, when it ends.
> (c) Describe $H_x$ and $E_z$ against $y$ at $t = 6$ ns. On each side, is the steep edge of the pulse nearer to or farther from the sheet?
>
> *Source: course notes Example 4 style (radiated pulse plotted against $t$ and against position), with a triangle current in a dielectric.*

> [!hint]- Hint
> Inside the dielectric $v = c/\sqrt{\epsilon_r}$ and $\eta = \eta_0/\sqrt{\epsilon_r}$. A probe at distance $d$ records the current delayed by $d/v$. For the snapshot, the field at distance $d$ carries the current from the source time $t' = t - d/v$: the part emitted first has travelled farthest.

> [!solution]- Solution
> **Setup.** Same recipe as in vacuum, with the medium's $v$ and $\eta$.
>
> **(a)** $v = c/3 = 1\times10^{8}$ m/s $= 0.1$ m/ns and $\eta = \eta_0/3 = 40\pi\approx125.7\ \Omega$. With $\hat n = \pm\hat{y}$, $(-\hat{z})\times\hat{y} = +\hat{x}$ and $(-\hat{z})\times(-\hat{y}) = -\hat{x}$:
> $$
> \mathbf{H} = \pm\frac12\,g\Big(t - \frac{\lvert y\rvert}{v}\Big)\,\hat{x}\quad(y\gtrless0),\qquad \mathbf{E} = +20\pi\,g\Big(t - \frac{\lvert y\rvert}{v}\Big)\,\hat{z}\ \text{V/m}\quad\text{on both sides}.
> $$
> Peak values: $\lvert H_x\rvert = 1.5$ A/m and $E_z = +20\pi\times3 = +60\pi\approx+188.5$ V/m ($\mathbf{E}$ along $+\hat{z}$, opposite to the current).
>
> **(b)** At $y = +0.5$ m the delay is $0.5/0.1 = 5$ ns. The record is the source shifted by 5 ns: zero until 5 ns, a fast rise to the peak at 6 ns ($E_z = +188.5$ V/m, $H_x = +1.5$ A/m), a slow fall to zero at 9 ns. At $y = -0.3$ m the delay is 3 ns: start at 3 ns, peak at 4 ns ($E_z = +188.5$ V/m, $H_x = -1.5$ A/m), end at 7 ns. Halfway up the rise, e.g. at 5.5 ns at the first probe, $g = 1.5$ A/m gives $E_z = +94.2$ V/m and $H_x = +0.75$ A/m. A record keeps the source's order in time: fast rise first.
>
> **(c)** At $t = 6$ ns, distance $\lvert y\rvert = 0.1(6 - t')$ m holds the current from source time $t'$ ns: $t' = 0$ (the start) is at 0.6 m, $t' = 1$ ns (the peak) at 0.5 m, $t' = 4$ ns (the end) at 0.2 m. So on $y>0$, $H_x$ is zero up to 0.2 m, rises slowly to $+1.5$ A/m at 0.5 m, then drops steeply to zero at 0.6 m. On $y<0$ the same shape is mirrored, with $H_x$ negative ($-1.5$ A/m at $y = -0.5$ m). $E_z$ has the same shape on both sides and is positive everywhere: $+188.5$ V/m at $\lvert y\rvert = 0.5$ m. Spot checks: at $y = 0.3$ m, $t' = 3$ ns and $g = 1$ A/m, so $H_x = +0.5$ A/m and $E_z = +62.8$ V/m; at $y = -0.55$ m, $t' = 0.5$ ns and $g = 1.5$ A/m, so $H_x = -0.75$ A/m and $E_z = +94.2$ V/m. The steep edge is the front, emitted first: it is **farther** from the sheet on both sides.
>
> **Check:** $\mathbf{E}\times\mathbf{H}\parallel\hat{z}\times(+\hat{x}) = +\hat{y}$ for $y>0$ and $\hat{z}\times(-\hat{x}) = -\hat{y}$ for $y<0$, away from the sheet ✓. At the sheet, $\hat{y}\times(\mathbf{H}^+ - \mathbf{H}^-) = \hat{y}\times g\,\hat{x} = -g\,\hat{z} = \mathbf{J}_s$ ✓, and $\lvert\mathbf{E}\rvert/\lvert\mathbf{H}\rvert = 40\pi = \eta$ ✓.
>
> **Watch out:** in the dielectric the pulse needs 5 ns, not 1.67 ns, to reach 0.5 m, and the $\mathbf{E}$ amplitude is a third of the vacuum value for the same current.
>
> **Answer.** (a) $v = 0.1$ m/ns, $\eta = 40\pi\approx125.7\ \Omega$; $\mathbf{H} = \pm\tfrac12g(t - \lvert y\rvert/v)\,\hat{x}$ for $y\gtrless0$, $\mathbf{E} = +20\pi g(t - \lvert y\rvert/v)\,\hat{z}$ V/m. (b) $y = 0.5$ m: 5–9 ns, peak at 6 ns with $E_z = +188.5$ V/m and $H_x = +1.5$ A/m. $y = -0.3$ m: 3–7 ns, peak at 4 ns with $E_z = +188.5$ V/m and $H_x = -1.5$ A/m. (c) The pulse occupies $0.2<\lvert y\rvert<0.6$ m with its peak at $\lvert y\rvert = 0.5$ m; $H_x$ is positive for $y>0$ and negative for $y<0$, $E_z$ is positive on both sides; the steep edge is the outer one.

### 19.7 Which current made this field

> [!medium] Medium · current sheet radiation · boundary conditions
> A current sheet on the plane $z = 0$ in free space is the only source. A probe at $z = -600$ m records $\mathbf{E}(t) = +94.2\,\hat{y}$ V/m for $2.5<t<4$ µs and zero at all other times. Use $c = 300$ m/µs and $\eta_0\approx120\pi\ \Omega$ (so 94.2 V/m $\approx30\pi$ V/m).
> (a) Find $\mathbf{J}_s(t)$, as a vector.
> (b) Find $\mathbf{H}$ at the probe while the pulse passes, and the Poynting vector there.
> (c) Find $\mathbf{E}$ and $\mathbf{H}$ everywhere at $t = 3$ µs.
>
> *Source: Lecture 19 slides 18–21 style (find the current from a measured field), new plane, field and waveform.*

> [!hint]- Hint
> Run the recipe backwards. $\mathbf{E}$ at the sheet is $-\tfrac{\eta_0}{2}\mathbf{J}_s(t)$, and the probe sees it $600/300$ µs later. Then $\mathbf{J}_s(t) = -\tfrac{2}{\eta_0}\mathbf{E}_{\text{probe}}(t + 2\ \mu\text{s})$.

> [!solution]- Solution
> **Setup.** The probe is 600 m below the sheet, so it records the sheet's field with a delay of $600/300 = 2$ µs; the field at the sheet is $\mathbf{E}(0,t) = -\tfrac{\eta_0}{2}\mathbf{J}_s(t)$ and the same on both faces.
>
> **(a)** Undo the delay and the factor:
> $$
> \mathbf{J}_s(t) = -\frac{2}{\eta_0}\,\mathbf{E}_{\text{probe}}(t + 2\ \mu\text{s}) = -\frac{2\times30\pi}{120\pi}\,\hat{y} = -0.5\,\hat{y}\ \text{A/m}\quad\text{for } 0.5<t<2\ \mu\text{s},
> $$
> and zero otherwise: a rectangular pulse of current along $-\hat{y}$.
>
> **(b)** Below the sheet $\hat n = -\hat{z}$: $\mathbf{H} = \tfrac12(-0.5\,\hat{y})\times(-\hat{z}) = +0.25\,(\hat{y}\times\hat{z}) = +0.25\,\hat{x}$ A/m during $2.5<t<4$ µs. Then $\mathbf{S} = \mathbf{E}\times\mathbf{H} = (94.2\,\hat{y})\times(0.25\,\hat{x}) = -23.6\,\hat{z}$ W/m²: away from the sheet, as it must be below it. Check: $\eta_0J_s^2/4 = 120\pi\times0.25/4 = 23.6$ W/m² ✓.
>
> **(c)** At $t = 3$ µs the current from source time $t'$ sits at $\lvert z\rvert = 300(3 - t')$ m. The pulse, $0.5<t'<2$ µs, therefore occupies $300<\lvert z\rvert<750$ m on both sides. There $\mathbf{E} = +94.2\,\hat{y}$ V/m on both sides, $\mathbf{H} = +0.25\,\hat{x}$ A/m for $-750<z<-300$ m, and $\mathbf{H} = \tfrac12(-0.5\,\hat{y})\times\hat{z} = -0.25\,\hat{x}$ A/m for $300<z<750$ m. Everywhere else both fields are zero.
>
> **Check:** above the sheet $\mathbf{E}\times\mathbf{H}\parallel\hat{y}\times(-\hat{x}) = +\hat{z}$, away ✓; $\hat{z}\times(\mathbf{H}^+ - \mathbf{H}^-) = \hat{z}\times(-0.5\,\hat{x}) = -0.5\,\hat{y} = \mathbf{J}_s$ ✓.
>
> **Watch out:** $\mathbf{E}$ points along $+\hat{y}$, so the current points along $-\hat{y}$. $\mathbf{E}$ is always *opposite* to the current that radiates it; answering $+0.5\,\hat{y}$ is the classic slip.
>
> **Answer.** (a) $\mathbf{J}_s = -0.5\,\hat{y}$ A/m for $0.5<t<2$ µs, zero otherwise. (b) $\mathbf{H} = +0.25\,\hat{x}$ A/m, $\mathbf{S} = -23.6\,\hat{z}$ W/m². (c) Fields only on $300<\lvert z\rvert<750$ m: $\mathbf{E} = +94.2\,\hat{y}$ V/m on both sides, $\mathbf{H} = -0.25\,\hat{x}$ A/m for $z>0$ and $+0.25\,\hat{x}$ A/m for $z<0$.

### 19.8 A cosine current in a dielectric

> [!medium] Medium · current sheet radiation · wave parameters · Poynting vector
> A sheet on the plane $y = 0$ carries $\mathbf{J}_s = 0.4\cos(\omega t)\,\hat{x}$ A/m with $f = 50$ MHz, in a lossless non-magnetic dielectric with $\epsilon_r = 2.25$ filling all space. Use $c = 3\times10^{8}$ m/s and $\eta_0\approx120\pi\ \Omega$.
> (a) Find $v$, $\eta$, $\omega$, $\beta$ and $\lambda$.
> (b) Write $\mathbf{E}$ and $\mathbf{H}$ for $y>0$ and $y<0$ as real cosines.
> (c) Find the Poynting vector on each side: direction, peak value, and how it varies in time.
> (d) Find $\mathbf{E}$, $\mathbf{H}$ and $\mathbf{S}$ at $t = 5$ ns at $y = 1$ m and at $y = -3$ m. Where on $y>0$ is $\mathbf{E}$ zero at that instant?
>
> *Source: Lecture 19 slides 13–16 style (sinusoidal sheet current, wave parameters, Poynting vector), new plane, current direction and medium.*

> [!hint]- Hint
> Replace $t$ by $t - \lvert y\rvert/v$ in the current: $\cos\big(\omega(t - \lvert y\rvert/v)\big) = \cos(\omega t - \beta\lvert y\rvert)$ with $\beta = \omega/v$. For (d), first compute $\omega t$ at 5 ns.

> [!solution]- Solution
> **(a)** $v = c/\sqrt{2.25} = 2\times10^{8}$ m/s, $\eta = \eta_0/1.5 = 80\pi\approx251.3\ \Omega$, $\omega = 2\pi\times50\times10^{6} = \pi\times10^{8}$ rad/s, $\beta = \omega/v = \pi/2\approx1.571$ rad/m, $\lambda = 2\pi/\beta = 4$ m (check: $v/f = 2\times10^{8}/5\times10^{7} = 4$ m ✓).
>
> **(b)** $\hat n = \pm\hat{y}$; $\hat{x}\times\hat{y} = +\hat{z}$ and $\hat{x}\times(-\hat{y}) = -\hat{z}$. Amplitudes $\tfrac\eta2\times0.4 = 16\pi\approx50.3$ V/m and $\tfrac12\times0.4 = 0.2$ A/m:
> $$
> \mathbf{E} = -50.3\cos(\omega t - \beta\lvert y\rvert)\,\hat{x}\ \text{V/m},\qquad \mathbf{H} = \pm0.2\cos(\omega t - \beta\lvert y\rvert)\,\hat{z}\ \text{A/m}\quad(y\gtrless0).
> $$
> For $y>0$ the argument is $\omega t - \beta y$ (travel toward $+y$); for $y<0$ it is $\omega t + \beta y$ (toward $-y$).
>
> **(c)** $\mathbf{S} = \mathbf{E}\times\mathbf{H} = \pm\hat{y}\,(50.3)(0.2)\cos^2(\omega t - \beta\lvert y\rvert)$, since $(-\hat{x})\times(+\hat{z}) = +\hat{y}$ and $(-\hat{x})\times(-\hat{z}) = -\hat{y}$. The peak is $\eta J_{s0}^2/4 = 3.2\pi\approx10.05$ W/m², always pointing away from the sheet (a square is never negative). At a fixed point $\mathbf{S}$ pulses at twice the source frequency: $\cos^2$ repeats every 10 ns, i.e. at 100 MHz. At the sheet the current gives up $-\mathbf{J}_s\cdot\mathbf{E} = \tfrac\eta2J_{s0}^2\cos^2\omega t$, with peak 20.1 W/m², exactly the two outgoing peaks together.
>
> **(d)** At $t = 5$ ns, $\omega t = \pi\times10^{8}\times5\times10^{-9} = \pi/2$.
> - $y = 1$ m: phase $\pi/2 - \pi/2 = 0$, $\cos = 1$: $\mathbf{E} = -50.3\,\hat{x}$ V/m, $\mathbf{H} = +0.2\,\hat{z}$ A/m, $\mathbf{S} = +10.05\,\hat{y}$ W/m².
> - $y = -3$ m: phase $\pi/2 - 3\pi/2 = -\pi$, $\cos = -1$: $\mathbf{E} = +50.3\,\hat{x}$ V/m, $\mathbf{H} = -0.2\,(-1)\,\hat{z} = +0.2\,\hat{z}$ A/m, $\mathbf{S} = (50.3\,\hat{x})\times(0.2\,\hat{z}) = -10.05\,\hat{y}$ W/m², away from the sheet ✓.
> - $\mathbf{E} = 0$ on $y>0$ where $\pi/2 - \pi y/2 = \pi/2 + k\pi$, i.e. at $y = 0, 2, 4, \dots$ m, every half wavelength. There $\mathbf{H}$ and $\mathbf{S}$ vanish too.
>
> **Check:** $\lvert\mathbf{E}\rvert/\lvert\mathbf{H}\rvert = 50.3/0.2 = 251\ \Omega = \eta$ ✓; at the sheet $\hat{y}\times(\mathbf{H}^+ - \mathbf{H}^-) = \hat{y}\times0.4\cos\omega t\,\hat{z} = 0.4\cos\omega t\,\hat{x} = \mathbf{J}_s$ ✓.
>
> **Answer.** (a) $v = 2\times10^{8}$ m/s, $\eta = 80\pi\approx251\ \Omega$, $\omega = \pi\times10^{8}$ rad/s, $\beta = \pi/2$ rad/m, $\lambda = 4$ m. (b) $\mathbf{E} = -50.3\cos(\omega t - \beta\lvert y\rvert)\,\hat{x}$ V/m, $\mathbf{H} = \pm0.2\cos(\omega t - \beta\lvert y\rvert)\,\hat{z}$ A/m for $y\gtrless0$. (c) $\mathbf{S} = \pm10.05\cos^2(\omega t - \beta\lvert y\rvert)\,\hat{y}$ W/m², away from the sheet, pulsing at 100 MHz. (d) $y = 1$ m: $-50.3\,\hat{x}$ V/m, $+0.2\,\hat{z}$ A/m, $+10.05\,\hat{y}$ W/m²; $y = -3$ m: $+50.3\,\hat{x}$ V/m, $+0.2\,\hat{z}$ A/m, $-10.05\,\hat{y}$ W/m²; $\mathbf{E} = 0$ at $y = 0, 2, 4, \dots$ m.

## Hard

### 19.9 A sheet launches a step and a ramp

> [!hard] Hard · current sheet radiation · moving pulses · Poynting vector
> An infinitesimally thin sheet in the plane $z = 0$ carries the surface current $\mathbf{J}_s = -g(t)\,\hat{y}$ A/m in free space. The waveform is $g = 0$ for $t<0$; $g = +2$ A/m for $0<t<1$ ns; at $t = 1$ ns it jumps to $-4$ A/m and then rises linearly to 0 at $t = 3$ ns; $g = 0$ afterwards. Use $c = 0.3$ m/ns and $\eta_0\approx120\pi\ \Omega$.
> (a) Write the magnetic field of the forward wave ($z>0$) and of the reverse wave ($z<0$) as $\mathbf{H} = (\text{coefficient})\,g(t\mp z/c)\,(\text{unit vector})$.
> (b) Find the electric field of each wave.
> (c) Sketch $H_x$ against $z$ at $t = 4$ ns for $-1.5<z<1.5$ m, with labelled scales. Sketch $E_y$ at the same instant.
> (d) A probe at $z = -0.9$ m records $H_x(t)$. Describe the record.
> (e) Find the Poynting vector at $z = 0.6$ m and at $z = -1.0$ m at $t = 4$ ns. Find $\mathbf{J}_s\cdot\mathbf{E}$ at the sheet at $t = 0.5$ ns and compare.
>
> *Source: SP18 Exam 2 #5 style, re-parameterized: sheet on $z = 0$ instead of $y = 0$, current along $-\hat{y}$ instead of $-\hat{x}$, a step-then-ramp waveform, a new instant, and a probe and Poynting part added (also different from the site's worked problem [[problems/a-current-sheet-launches-two-waves|A current sheet launches two waves]]).*

> [!hint]- Hint
> For (a), $\tfrac12\mathbf{J}_s\times\hat n$ with $\hat n = +\hat{z}$ above and $-\hat{z}$ below. For (c), the field at distance $\lvert z\rvert$ at $t = 4$ ns carries the current from $t' = 4 - \lvert z\rvert/0.3$ ns: locate where $t' = 0$, 1 and 3 ns sit, then fill in.

> [!solution]- Solution
> **Setup.** Waves travel away from the sheet: toward $+z$ with $t - z/c$ above, toward $-z$ with $t + z/c$ below.
>
> **(a)** $\mathbf{J}_s = -g\,\hat{y}$. Above: $(-\hat{y})\times\hat{z} = -\hat{x}$. Below: $(-\hat{y})\times(-\hat{z}) = +\hat{x}$. So
> $$
> \mathbf{H} = -\frac12\,g\Big(t - \frac zc\Big)\,\hat{x}\quad(z>0),\qquad \mathbf{H} = +\frac12\,g\Big(t + \frac zc\Big)\,\hat{x}\quad(z<0).
> $$
> Check: $\hat{z}\times(\mathbf{H}^+ - \mathbf{H}^-) = \hat{z}\times(-g\,\hat{x}) = -g\,\hat{y} = \mathbf{J}_s$ ✓.
>
> **(b)** $\mathbf{E} = -\tfrac{\eta_0}{2}\mathbf{J}_s = +\tfrac{\eta_0}{2}\,g\,\hat{y}$, the same on both sides:
> $$
> \mathbf{E} = +60\pi\,g\Big(t - \frac{\lvert z\rvert}{c}\Big)\,\hat{y}\ \text{V/m}\qquad(60\pi\approx188.5\ \Omega).
> $$
> Check: above, $\mathbf{E}\times\mathbf{H}\parallel\hat{y}\times(-\hat{x}) = +\hat{z}$; below, $\hat{y}\times\hat{x} = -\hat{z}$; away from the sheet on both sides ✓ (for either sign of $g$, since both fields flip together).
>
> **(c)** At $t = 4$ ns, $\lvert z\rvert = 0.3(4 - t')$ m. Source time $t' = 0$ (the start) is at $\lvert z\rvert = 1.2$ m, $t' = 1$ ns (the jump) at 0.9 m, $t' = 3$ ns (the end of the ramp) at 0.3 m.
> - $z>0$, $H_x = -\tfrac12g$: zero for $0<z<0.3$ m; from 0 at $z = 0.3$ m rising linearly to $+2$ A/m just inside $z = 0.9$ m (where $g\to-4$); a jump to $-1$ A/m at $z = 0.9$ m; $-1$ A/m on $0.9<z<1.2$ m; zero beyond 1.2 m.
> - $z<0$, $H_x = +\tfrac12g$: the mirror image with the sign flipped. Zero for $-0.3<z<0$; from 0 at $-0.3$ m falling to $-2$ A/m just inside $-0.9$ m; a jump to $+1$ A/m; $+1$ A/m on $-1.2<z<-0.9$ m; zero beyond.
> - $E_y = 60\pi g$, the same on both sides (even in $z$): zero for $\lvert z\rvert<0.3$ m; from 0 at $\lvert z\rvert = 0.3$ m to $-240\pi\approx-754$ V/m just inside $\lvert z\rvert = 0.9$ m; $+120\pi\approx+377$ V/m on $0.9<\lvert z\rvert<1.2$ m; zero beyond.
>
> Spot check: at $z = 0.6$ m, $t' = 2$ ns and $g = -4 + 2(2 - 1) = -2$ A/m, so $H_x = +1$ A/m and $E_y = -377$ V/m. On each side the pattern is the waveform reversed in order: the first-emitted part (the $+2$ A/m step) is farthest out.
>
> **(d)** The probe is 0.9 m from the sheet, a delay of 3 ns, and on the $z<0$ side: $H_x(t) = +\tfrac12g(t - 3\ \text{ns})$. Zero until 3 ns; $+1$ A/m for $3<t<4$ ns; a jump to $-2$ A/m at $t = 4$ ns; a linear rise back to 0 at $t = 6$ ns; zero afterwards. The record keeps the source's time order (the step comes first).
>
> **(e)** At $z = 0.6$ m: $g = -2$ A/m, so $\mathbf{E} = -377\,\hat{y}$ V/m, $\mathbf{H} = +1\,\hat{x}$ A/m and $\mathbf{S} = (-377\,\hat{y})\times(1\,\hat{x}) = +377\,\hat{z}$ W/m². At $z = -1.0$ m: $t' = 4 - 1.0/0.3 = 0.667$ ns, $g = +2$ A/m, so $\mathbf{E} = +377\,\hat{y}$ V/m, $\mathbf{H} = +1\,\hat{x}$ A/m and $\mathbf{S} = (377\,\hat{y})\times(1\,\hat{x}) = -377\,\hat{z}$ W/m². Both have magnitude $\eta_0g^2/4 = 377$ W/m² and point away from the sheet. At the sheet at $t = 0.5$ ns, $\mathbf{J}_s = -2\,\hat{y}$ A/m and $\mathbf{E} = +377\,\hat{y}$ V/m, so $\mathbf{J}_s\cdot\mathbf{E} = -754$ W/m² $= -\tfrac{\eta_0}{2}g^2$: the current supplies 754 W/m², which leaves as 377 W/m² through each face.
>
> **Watch out:** $\mathbf{E}$ does not flip across the sheet, $\mathbf{H}$ does. A sketch of $E_y$ with opposite signs on the two sides, or of $H_x$ with the same sign, is wrong at a glance.
>
> **Answer.** (a) $\mathbf{H} = -\tfrac12g(t - z/c)\,\hat{x}$ for $z>0$, $+\tfrac12g(t + z/c)\,\hat{x}$ for $z<0$. (b) $\mathbf{E} = +60\pi g(t - \lvert z\rvert/c)\,\hat{y}$ V/m on both sides. (c) $H_x$: ramp from 0 at $z = 0.3$ m to $+2$ A/m at 0.9 m, jump to $-1$ A/m on $0.9<z<1.2$ m; mirrored with opposite sign for $z<0$. $E_y$: 0 to $-754$ V/m on $0.3<\lvert z\rvert<0.9$ m, $+377$ V/m on $0.9<\lvert z\rvert<1.2$ m, both sides. (d) $+1$ A/m for 3–4 ns, then $-2$ A/m rising to 0 at 6 ns. (e) $+377\,\hat{z}$ W/m² at $z = 0.6$ m, $-377\,\hat{z}$ W/m² at $z = -1.0$ m; $\mathbf{J}_s\cdot\mathbf{E} = -754$ W/m².

### 19.10 Two sheets, one-sided radiation

> [!hard] Hard · current sheet radiation · superposition · moving pulses
> Two parallel sheets in free space: sheet A on $z = 0$ carries $\mathbf{J}_A = +1\,\hat{x}$ A/m for $0<t<10$ ns; sheet B on $z = 3$ m carries $\mathbf{J}_B = -1\,\hat{x}$ A/m for $10<t<20$ ns. Both currents are zero at all other times. Use $c = 0.3$ m/ns and $\eta_0\approx120\pi\ \Omega$.
> (a) Write $\mathbf{E}$ and $\mathbf{H}$ radiated by each sheet alone, on each side of it.
> (b) Show that the total field is zero for $z>3$ m at all times.
> (c) What do probes of $E_x$ and $H_y$ at $z = -1.5$ m record?
> (d) Find $E_x$ and $H_y$ everywhere at $t = 15$ ns.
> (e) Find $\mathbf{E}$ at sheet B while B carries current, and $\mathbf{J}_B\cdot\mathbf{E}$. Is sheet B a source of energy? Where does the energy of the pulse it sends toward $-z$ come from?
>
> *Source: original (superposition of two sheets; the timing is chosen so that sheet B switches on exactly as A's wave passes it).*

> [!hint]- Hint
> Each sheet radiates as if the other were absent, and the total is the sum. Sheet A's upward wave reaches $z = 3$ m after $3/0.3 = 10$ ns, exactly when B switches on. Compare A's wave and B's upward wave term by term for $z>3$ m.

> [!solution]- Solution
> **Setup.** Maxwell's equations are linear, so superpose the two sheets' fields. Each obeys the recipe with its own $\hat n$ and distance.
>
> **(a)** Sheet A ($\mathbf{J}_A = +\hat{x}\,g_A$): $\mathbf{E}_A = -60\pi\,g_A(t - \lvert z\rvert/c)\,\hat{x}$; $\hat{x}\times\hat{z} = -\hat{y}$ and $\hat{x}\times(-\hat{z}) = +\hat{y}$, so $\mathbf{H}_A = \mp\tfrac12g_A\,\hat{y}$ for $z\gtrless0$. Sheet B ($\mathbf{J}_B = -\hat{x}\,g_B$): $\mathbf{E}_B = +60\pi\,g_B(t - \lvert z - 3\rvert/c)\,\hat{x}$; $(-\hat{x})\times\hat{z} = +\hat{y}$ and $(-\hat{x})\times(-\hat{z}) = -\hat{y}$, so $\mathbf{H}_B = \pm\tfrac12g_B\,\hat{y}$ for $z\gtrless3$ m. The amplitudes are $60\pi\approx188.5$ V/m and 0.5 A/m.
>
> **(b)** For $z>3$ m, A's wave is nonzero when $0<t - z/c<10$ ns and B's when $10<t - (z - 3)/c<20$ ns. Since $3/c = 10$ ns, the second condition is the same as $0<t - z/c<10$ ns: the two waves cover exactly the same region at every instant. There
> $$
> E_x = -188.5 + 188.5 = 0,\qquad H_y = -0.5 + 0.5 = 0 .
> $$
> Nothing ever travels beyond sheet B. The pair is a one-sided radiator.
>
> **(c)** At $z = -1.5$ m, A's downward wave arrives after 5 ns and B's after $4.5/0.3 = 15$ ns:
> - $5<t<15$ ns: A's pulse, $E_x = -188.5$ V/m and $H_y = +0.5$ A/m;
> - $25<t<35$ ns: B's pulse, $E_x = +188.5$ V/m and $H_y = -0.5$ A/m;
> - zero otherwise.
>
> Both are $-z$ waves: $(-\hat{x})\times(+\hat{y}) = -\hat{z}$ and $(+\hat{x})\times(-\hat{y}) = -\hat{z}$ ✓.
>
> **(d)** At $t = 15$ ns:
> - $-4.5<z<-1.5$ m: A's downward pulse, $E_x = -188.5$ V/m and $H_y = +0.5$ A/m.
> - $1.5<z<3$ m: A's upward pulse ($0<15 - z/0.3<10$ means $1.5<z<4.5$ m) overlaps B's downward pulse ($10<15 - (3 - z)/0.3<20$ means $z>1.5$ m, up to the sheet at $z = 3$ m): $E_x = -188.5 + 188.5 = 0$ and $H_y = -0.5 - 0.5 = -1.0$ A/m.
> - Everywhere else, including all of $z>3$ m: $E_x = H_y = 0$.
>
> Between the sheets the electric fields cancel and the magnetic fields add: two counter-propagating waves, as in Lecture 18.
>
> **(e)** While B carries current ($10<t<20$ ns), the field at $z = 3$ m is A's wave, $-188.5\,\hat{x}$ V/m, plus B's own, $+188.5\,\hat{x}$ V/m: $\mathbf{E} = 0$, so $\mathbf{J}_B\cdot\mathbf{E} = 0$. Sheet B supplies no energy. Sheet A, with only its own field at $z = 0$ during $0<t<10$ ns, has $\mathbf{J}_A\cdot\mathbf{E} = -188.5$ W/m²; over 10 ns it supplies $1885$ nJ/m². Each pulse carries $\lvert\mathbf{S}\rvert = \eta_0/4 = 94.2$ W/m² for 10 ns, i.e. 942.5 nJ/m². A's downward pulse takes half of A's energy; the other half went up, and B turned it around: the $-z$ pulse that B launches carries the energy of A's upward pulse, which B cancels. All 1885 nJ/m² end up travelling toward $-z$.
>
> **Check:** the superposed fields satisfy Faraday's law and the Ampère–Maxwell law everywhere off the sheets, and at $z = 3$ m, $\hat{z}\times(\mathbf{H}(3^+) - \mathbf{H}(3^-)) = \hat{z}\times(0 - (-1.0\,\hat{y})) = -1.0\,\hat{x} = \mathbf{J}_B$ ✓ (A's wave is continuous there and drops out of the jump).
>
> **Answer.** (a) $\mathbf{E}_A = -188.5\,g_A\,\hat{x}$, $\mathbf{H}_A = \mp0.5\,g_A\,\hat{y}$ ($z\gtrless0$); $\mathbf{E}_B = +188.5\,g_B\,\hat{x}$, $\mathbf{H}_B = \pm0.5\,g_B\,\hat{y}$ ($z\gtrless3$ m), with the delays $\lvert z\rvert/c$ and $\lvert z - 3\rvert/c$. (b) For $z>3$ m the two waves cover the same region with opposite fields. (c) $-188.5$ V/m and $+0.5$ A/m for 5–15 ns, then $+188.5$ V/m and $-0.5$ A/m for 25–35 ns. (d) $E_x = -188.5$ V/m, $H_y = +0.5$ A/m on $-4.5<z<-1.5$ m; $E_x = 0$, $H_y = -1.0$ A/m on $1.5<z<3$ m; zero elsewhere. (e) $\mathbf{E} = 0$ at sheet B, $\mathbf{J}_B\cdot\mathbf{E} = 0$; all the energy (1885 nJ/m²) comes from sheet A.

### 19.11 A sheet on a diagonal plane

> [!hard] Hard · current sheet radiation · Poynting vector · plane waves
> A sheet lies on the plane $y = x$ (it contains the $z$ axis) in free space and carries $\mathbf{J}_s = 0.2\cos(\omega t)\,\hat{z}$ A/m with $f = 150$ MHz. Use $c = 3\times10^{8}$ m/s and $\eta_0\approx120\pi\ \Omega$.
> (a) Find $\beta$ and $\lambda$, the unit normal $\hat n$ pointing into the region $x>y$, and the distance $d$ from a point $(x,y,z)$ to the sheet.
> (b) Write $\mathbf{E}$ and $\mathbf{H}$ on both sides as real cosines.
> (c) At $P = (1, -1, 0)$ m, evaluate $\mathbf{E}$, $\mathbf{H}$ and $\mathbf{S}$ at the instant $t_1 = d_P/c$.
> (d) At that instant an electron passes $P$ with velocity $\mathbf{u} = 3\times10^{6}\,\hat{z}$ m/s. Find the electric and magnetic forces on it (vectors) and their ratio. For which direction of $\mathbf{u}$ would the magnetic force vanish?
>
> *Source: original; part (d) is the course notes' Example 2 (magnetic versus electric force in a plane wave) applied to a sheet's wave.*

> [!hint]- Hint
> The plane $x - y = 0$ has normal $\pm(\hat{x} - \hat{y})/\sqrt2$, and the distance from it is $\lvert x - y\rvert/\sqrt2$. Nothing else changes: the recipe works with any $\hat n$. Write $\hat{z}\times\hat{x}$ and $\hat{z}\times\hat{y}$ out separately.

> [!solution]- Solution
> **Setup.** The recipe holds for a sheet in any plane; only $\hat n$ and $d$ change.
>
> **(a)** $\beta = \omega/c = 2\pi\times1.5\times10^{8}/(3\times10^{8}) = \pi$ rad/m and $\lambda = 2$ m. The plane $x - y = 0$ has gradient direction $\hat{x} - \hat{y}$, which points toward increasing $x - y$, so $\hat n = (\hat{x} - \hat{y})/\sqrt2$ on the side $x>y$ and $-(\hat{x} - \hat{y})/\sqrt2$ on the side $x<y$. The distance is $d = \lvert x - y\rvert/\sqrt2$.
>
> **(b)** $\hat{z}\times(\hat{x} - \hat{y}) = \hat{y} + \hat{x}$, so on the side $x>y$
> $$
> \mathbf{H} = \frac12(0.2)\,\frac{\hat{x} + \hat{y}}{\sqrt2}\cos(\omega t - \beta d) = 0.0707\,(\hat{x} + \hat{y})\cos(\omega t - \beta d)\ \text{A/m},
> $$
> magnitude 0.1 A/m, and $\mathbf{H} = -0.0707\,(\hat{x} + \hat{y})\cos(\omega t - \beta d)$ A/m on the side $x<y$. On both sides
> $$
> \mathbf{E} = -\frac{\eta_0}{2}(0.2)\cos(\omega t - \beta d)\,\hat{z} = -12\pi\cos(\omega t - \beta d)\,\hat{z}\approx-37.7\cos(\omega t - \beta d)\,\hat{z}\ \text{V/m},
> $$
> with $d = \lvert x - y\rvert/\sqrt2$ and $\beta = \pi$ rad/m.
>
> **(c)** $P$ has $x - y = 2>0$, so it is on the $\hat n = (\hat{x} - \hat{y})/\sqrt2$ side, at $d_P = 2/\sqrt2 = \sqrt2 = 1.414$ m; $t_1 = d_P/c = 4.714$ ns, when $\omega t_1 - \beta d_P = 0$ and the cosine is 1. Then $\mathbf{E} = -37.7\,\hat{z}$ V/m, $\mathbf{H} = 0.0707\,(\hat{x} + \hat{y})$ A/m, and
> $$
> \mathbf{S} = \mathbf{E}\times\mathbf{H} = -37.7\times0.0707\,\big(\hat{z}\times\hat{x} + \hat{z}\times\hat{y}\big) = -2.67\,(\hat{y} - \hat{x}) = 2.67\,(\hat{x} - \hat{y})\ \text{W/m}^2,
> $$
> magnitude $\eta_0J_{s0}^2/4 = 1.2\pi\approx3.77$ W/m², along $\hat n$, away from the sheet ✓.
>
> **(d)** Electric force: $\mathbf{F}_e = -e\mathbf{E} = +1.602\times10^{-19}\times37.7\,\hat{z} = +6.04\times10^{-18}\,\hat{z}$ N. Magnetic force: $\mathbf{B} = \mu_0\mathbf{H}$, magnitude $1.257\times10^{-7}$ T $= \lvert\mathbf{E}\rvert/c$. Since $\hat{z}\times(\hat{x} + \hat{y}) = \hat{y} - \hat{x}$,
> $$
> \mathbf{F}_m = -e\,\mathbf{u}\times\mathbf{B} = 4.27\times10^{-20}\,(\hat{x} - \hat{y})\ \text{N},\qquad \lvert\mathbf{F}_m\rvert = 6.04\times10^{-20}\ \text{N}.
> $$
> The ratio is $\lvert\mathbf{F}_m\rvert/\lvert\mathbf{F}_e\rvert = u\,\mu_0H/(\eta_0H) = u/c = 0.01$: the magnetic force is 1 % of the electric one, here pointing along the direction of travel $\hat n$. It vanishes when $\mathbf{u}$ is parallel (or antiparallel) to $\mathbf{B}$, i.e. along $\pm(\hat{x} + \hat{y})/\sqrt2$.
>
> **Check:** at the sheet $\hat n\times(\mathbf{H}_1 - \mathbf{H}_2) = \hat n\times\big(J_{s0}\cos\omega t\,\hat{z}\times\hat n\big) = J_{s0}\cos\omega t\,\hat{z}$ ✓ (because $\hat n\perp\hat{z}$), and the fields pass Faraday's and the Ampère–Maxwell laws on both sides (finite differences).
>
> **Answer.** (a) $\beta = \pi$ rad/m, $\lambda = 2$ m, $\hat n = (\hat{x} - \hat{y})/\sqrt2$, $d = \lvert x - y\rvert/\sqrt2$. (b) $\mathbf{E} = -37.7\cos(\omega t - \beta d)\,\hat{z}$ V/m; $\mathbf{H} = \pm0.0707\,(\hat{x} + \hat{y})\cos(\omega t - \beta d)$ A/m for $x\gtrless y$. (c) $\mathbf{E} = -37.7\,\hat{z}$ V/m, $\mathbf{H} = 0.0707(\hat{x} + \hat{y})$ A/m, $\mathbf{S} = 2.67(\hat{x} - \hat{y})$ W/m² ($3.77$ W/m²). (d) $\mathbf{F}_e = 6.04\times10^{-18}\,\hat{z}$ N, $\mathbf{F}_m = 4.27\times10^{-20}(\hat{x} - \hat{y})$ N, ratio $u/c = 0.01$; $\mathbf{F}_m = 0$ for $\mathbf{u}\parallel\pm(\hat{x} + \hat{y})$.

### 19.12 Deriving the sheet field in a magnetic medium

> [!hard] Hard · current sheet radiation · boundary conditions · intrinsic impedance
> A sheet on the plane $x = 0$ carries $\mathbf{J}_s = -K(t)\,\hat{z}$, in a lossless medium with $\mu_r = 2$ and $\epsilon_r = 8$ that fills all space. Use $c = 3\times10^{8}$ m/s and $\eta_0\approx120\pi\ \Omega$.
> (a) Find $v$ and $\eta$.
> (b) Write the general d'Alembert solution for $E_z(x,t)$ and $H_y(x,t)$ on each side, with the correct sign between $E_z$ and $H_y$ for each direction of travel. Apply the radiation condition.
> (c) Use the two boundary conditions at $x = 0$ to find the amplitude, and compare with the recipe $\mathbf{E} = -\tfrac\eta2\mathbf{J}_s$, $\mathbf{H} = \tfrac12\mathbf{J}_s\times\hat n$.
> (d) The current is a ramp: $K = 0$ for $t<0$ and $K = 2t$ A/m ($t$ in µs) for $t>0$. At $t = 1$ µs, find $H_y$ and $E_z$ at $x = 1.5$ m and at $x = 60$ m, and compare $H_y$ with the undelayed static-sheet value $\tfrac12\mathbf{J}_s(t)\times\hat n$ of Lecture 13.
> (e) Verify Faraday's law numerically at $x = 1.5$ m, $t = 1$ µs.
>
> *Source: Lecture 19 slides 3–10 (the boundary-condition derivation), redone in a new orientation and a magnetic medium, plus the notes' quasi-static step.*

> [!hint]- Hint
> For a wave along $\hat u$, $\mathbf{H} = \hat u\times\mathbf{E}/\eta$: with $\mathbf{E} = E_z\hat{z}$, $\hat{x}\times\hat{z} = -\hat{y}$ and $(-\hat{x})\times\hat{z} = +\hat{y}$. At the sheet, $\hat n = \hat{x}$ points from region 2 ($x<0$) into region 1 ($x>0$) in $\hat n\times(\mathbf{H}_1 - \mathbf{H}_2) = \mathbf{J}_s$.

> [!solution]- Solution
> **(a)** $v = 1/\sqrt{\mu\epsilon} = c/\sqrt{\mu_r\epsilon_r} = c/4 = 7.5\times10^{7}$ m/s $= 75$ m/µs, and $\eta = \eta_0\sqrt{\mu_r/\epsilon_r} = \eta_0/2 = 60\pi\approx188.5\ \Omega$.
>
> **(b)** A wave toward $+x$ with $E_z = A f(t - x/v)$ has $\mathbf{H} = \hat{x}\times\hat{z}\,E_z/\eta = -\hat{y}\,E_z/\eta$. A wave toward $-x$ with $E_z = B g(t + x/v)$ has $\mathbf{H} = (-\hat{x})\times\hat{z}\,E_z/\eta = +\hat{y}\,E_z/\eta$. So on each side
> $$
> E_z = Af\Big(t - \frac xv\Big) + Bg\Big(t + \frac xv\Big),\qquad H_y = \frac1\eta\Big[-Af\Big(t - \frac xv\Big) + Bg\Big(t + \frac xv\Big)\Big].
> $$
> Radiation condition: only outgoing waves, so $B = 0$ for $x>0$ and $A = 0$ for $x<0$.
>
> **(c)** Tangential $\mathbf{E}$ continuous at $x = 0$: $Af(t) = Bg(t)\equiv F(t)$. Tangential $\mathbf{H}$: $\mathbf{H}_1 = -\tfrac{F}{\eta}\hat{y}$, $\mathbf{H}_2 = +\tfrac{F}{\eta}\hat{y}$, and
> $$
> \hat{x}\times(\mathbf{H}_1 - \mathbf{H}_2) = -\frac{2F}{\eta}\,\hat{x}\times\hat{y} = -\frac{2F}{\eta}\,\hat{z} = \mathbf{J}_s = -K\,\hat{z}\quad\Longrightarrow\quad F(t) = \frac\eta2K(t).
> $$
> Hence $E_z = \tfrac\eta2K(t - \lvert x\rvert/v)$ on both sides, $H_y = -\tfrac12K(t - x/v)$ for $x>0$ and $+\tfrac12K(t + x/v)$ for $x<0$. The recipe agrees: $-\tfrac\eta2(-K\hat{z}) = +\tfrac\eta2K\hat{z}$; $\tfrac12(-\hat{z})\times\hat{x} = -\tfrac12\hat{y}$ and $\tfrac12(-\hat{z})\times(-\hat{x}) = +\tfrac12\hat{y}$ ✓. Note that $\mu_r$ enters only through $v$ and $\eta$; the $\tfrac12$ in $\mathbf{H}$ is untouched.
>
> **(d)** $K' = 2$ A/m per µs. At $x = 1.5$ m the delay is $1.5/75 = 0.02$ µs: $H_y = -\tfrac12\times2\times0.98 = -0.98$ A/m and $E_z = 30\pi\times2\times0.98 = 184.7$ V/m. The static-sheet (quasi-static) value is $\tfrac12(-K\hat{z})\times\hat{x} = -\tfrac12K(t)\,\hat{y}$, i.e. $H_y = -1.00$ A/m: only 2 % off, because the delay is tiny compared with the time over which $K$ changes. At $x = 60$ m the delay is 0.8 µs: $H_y = -\tfrac12\times2\times0.2 = -0.20$ A/m and $E_z = 30\pi\times2\times0.2 = 37.7$ V/m, while the quasi-static value is still $-1.00$ A/m, five times too large. Near the sheet the static $\mathbf{H}$ is right; what magnetostatics cannot give is the $\mathbf{E}$ of 185 V/m, the Faraday partner of the growing $\mathbf{H}$.
>
> **(e)** For $\mathbf{E} = E_z(x,t)\hat{z}$, $\nabla\times\mathbf{E} = -\hat{y}\,\partial E_z/\partial x$, so Faraday's law $\nabla\times\mathbf{E} = -\mu\,\partial\mathbf{H}/\partial t$ reads $\partial E_z/\partial x = \mu\,\partial H_y/\partial t$. On the ramp ($K' = 2\times10^{6}$ A/(m·s)):
> $$
> \frac{\partial E_z}{\partial x} = -\frac{\eta}{2v}K' = -\frac{60\pi}{2\times7.5\times10^{7}}\times2\times10^{6} = -2.513\ \text{V/m}^2,\qquad \mu\frac{\partial H_y}{\partial t} = 2\mu_0\Big(-\frac12K'\Big) = -2.513\ \text{V/m}^2\ \checkmark
> $$
> They agree because $\eta/v = \sqrt{\mu/\epsilon}\sqrt{\mu\epsilon} = \mu$.
>
> **Watch out:** in a magnetic medium $\eta = \eta_0\sqrt{\mu_r/\epsilon_r}$, not $\eta_0/\sqrt{\epsilon_r}$; using the latter here would give $\eta_0/\sqrt8$ instead of $\eta_0/2$.
>
> **Answer.** (a) $v = 7.5\times10^{7}$ m/s, $\eta = 60\pi\approx188.5\ \Omega$. (b) $E_z = Af(t - x/v) + Bg(t + x/v)$, $H_y = (-Af + Bg)/\eta$; $B = 0$ for $x>0$, $A = 0$ for $x<0$. (c) $Af = Bg = \tfrac\eta2K$: $E_z = \tfrac\eta2K(t - \lvert x\rvert/v)$, $H_y = \mp\tfrac12K(t - \lvert x\rvert/v)$ for $x\gtrless0$, as the recipe says. (d) $x = 1.5$ m: $H_y = -0.98$ A/m (static $-1.00$), $E_z = 184.7$ V/m; $x = 60$ m: $H_y = -0.20$ A/m, $E_z = 37.7$ V/m. (e) Both sides equal $-2.513$ V/m².

### Sources for this page
Course notes, Lecture 19: the classification of d'Alembert solutions as uniform plane TEM waves (19.1), Example 2 on magnetic versus electric force (19.11(d)), Example 4's radiated pulse plotted against time and position (19.6, with a triangle current in a dielectric), and the quasi-static step (19.12(d)). Lecture 19 slides: slide 17 (19.2, current reversed), the boundary-condition derivation of slides 3–10 (19.12, in a new orientation and a magnetic medium), the sinusoidal sheet, wave-parameter table and Poynting vector of slides 13–16 (19.4, 19.8), and the inverse problem of slides 18–21 (19.7, new plane and waveform). Old exams: SP18 Exam 2 #5, re-parameterized (19.9: sheet on $z = 0$ with current along $-\hat{y}$ and a step-then-ramp waveform, in place of the exam's $y = 0$ sheet with current along $-\hat{x}$, and different from the site's worked problem). Original: 19.3, 19.5, 19.10 and 19.11.

*Previous: [[practice/18-wave-equation-and-plane-waves|Lecture 18 practice]] · [[practice/index|all practice]]*
