---
title: "Practice — Lecture 20: Poynting's theorem and power"
description: "12 practice problems (5 easy, 3 medium, 4 hard) on Poynting's theorem and power: the meaning, units and assumptions of its terms, J·E as Joule heating or as a source, time averages with real cosines (⟨S⟩ = E₀²/2η, perpendicular components and different frequencies adding, standing waves carrying no average power), field strength from intensity, power ledgers for a leaky sphere, a ramping solenoid, a coax with a resistive core and a charging leaky capacitor, and the energy balance of radiating sheets, each with a folded hint and a worked solution."
tags: [practice, waves]
lecture: 20
---

*Practice for [[3-maxwell-and-waves/20-poynting-theorem-and-monochromatic-waves|Lecture 20]] · concepts: [[concepts/poynting-theorem]] · [[concepts/poynting-vector]] · [[concepts/current-sheet-radiation]] · [[concepts/plane-waves]] · all practice: [[practice/index|hub]] · by difficulty: [[practice/easy|easy]] · [[practice/medium|medium]] · [[practice/hard|hard]] · [[practice/topics|by topic]]*

Work each problem on paper first. Open the **hint** only when stuck, and the **solution** only after you have an answer you would hand in. Every answer here has been checked numerically.

Three tools do almost every problem on this page. Poynting's theorem, at a point and for a volume $V$ with outward area element $d\mathbf{A}$:
$$
\begin{aligned}
&\frac{\partial w}{\partial t} + \nabla\cdot\mathbf{S} + \mathbf{J}\cdot\mathbf{E} = 0,\\
&-\frac{dW}{dt} = \oint_A\mathbf{S}\cdot d\mathbf{A} + \int_V\mathbf{J}\cdot\mathbf{E}\,dV,\\
&w = \tfrac12\epsilon E^2 + \tfrac12\mu H^2,\qquad \mathbf{S} = \mathbf{E}\times\mathbf{H}.
\end{aligned}
$$
Time averages over a period, with real cosines: $\langle\cos^2(\omega t + \phi)\rangle = \tfrac12$ and $\langle\cos(\omega t + \phi_1)\cos(\omega t + \phi_2)\rangle = \tfrac12\cos(\phi_1 - \phi_2)$. And for one plane wave of amplitude $E_0$ travelling along $\hat u$: $\langle\mathbf{S}\rangle = \hat u\,E_0^2/(2\eta)$ and $\langle w\rangle = \tfrac12\epsilon E_0^2 = \langle S\rangle/v$. Cylindrical coordinates are $(r,\phi,z)$ here, as on the other practice pages; the lecture page writes $\rho$ for $r$.

## Easy

### 20.1 Reading the energy ledger

> [!easy] Easy · true or false · Poynting's theorem
> Poynting's theorem, $\partial w/\partial t + \nabla\cdot\mathbf{S} + \mathbf{J}\cdot\mathbf{E} = 0$ with $w = \tfrac12\epsilon E^2 + \tfrac12\mu H^2$ and $\mathbf{S} = \mathbf{E}\times\mathbf{H}$, comes from dotting Faraday's law with $\mathbf{H}$ and the Ampère–Maxwell law with $\mathbf{E}$ and subtracting. True or false?
>
> (a) Each of the three terms is a power per unit volume (W/m³); $\mathbf{S}$ itself is a power per unit area (W/m²).
>
> (b) $\mathbf{J}\cdot\mathbf{E}$ is the Joule-heating term, so it can never be negative.
>
> (c) Inside a battery that drives a current around a circuit, $\mathbf{J}\cdot\mathbf{E}<0$.
>
> (d) Where there is no current, the theorem has the same form as the continuity equation of Lecture 16, with $w$ in the role of $\rho$ and $\mathbf{S}$ in the role of $\mathbf{J}$.
>
> (e) The derivation needs $\mathbf{D} = \epsilon\mathbf{E}$ and $\mathbf{B} = \mu\mathbf{H}$ with constant $\epsilon$ and $\mu$, so the theorem fails in a dielectric whose $\epsilon$ varies from place to place.
>
> (f) A charge held at rest next to a bar magnet has $\mathbf{E}\times\mathbf{H}\neq0$ around it, so energy flows steadily out of any closed surface drawn around the pair.
>
> *Source: original.*

> [!solution]- Solution
> (a) **True.** $\partial w/\partial t$: (J/m³)/s = W/m³. $\nabla\cdot\mathbf{S}$: (W/m²)/m = W/m³. $\mathbf{J}\cdot\mathbf{E}$: (A/m²)(V/m) = W/m³. And $\mathbf{S}$: (V/m)(A/m) = W/m².
>
> (b) **False.** $\mathbf{J}\cdot\mathbf{E}$ is the power per unit volume that the field hands to the charges. Only in an ohmic conductor, where $\mathbf{J} = \sigma\mathbf{E}$, is it $\sigma E^2\ge0$. Where something non-electromagnetic drives the current *against* $\mathbf{E}$, it is negative, and $-\mathbf{J}\cdot\mathbf{E}$ is power injected into the field: a battery, a generator, or the radiating sheet of Lecture 19, where $\mathbf{E} = -\tfrac\eta2\mathbf{J}_s$ gives $\mathbf{J}_s\cdot\mathbf{E} = -\tfrac\eta2J_s^2$ (about $-188$ W/m² for 1 A/m in vacuum).
>
> (c) **True.** Inside the battery the current runs from the $-$ terminal to the $+$ terminal, against the field of the terminal charges, which points from $+$ to $-$; the chemistry does the driving. For a 1.5 V cell delivering 1 A, $-\int\mathbf{J}\cdot\mathbf{E}\,dV = 1.5$ W, the power it gives the circuit.
>
> (d) **True.** With $\mathbf{J} = 0$ the theorem reads $\partial w/\partial t + \nabla\cdot\mathbf{S} = 0$, the twin of $\partial\rho/\partial t + \nabla\cdot\mathbf{J} = 0$. With current there is an extra exchange term $\mathbf{J}\cdot\mathbf{E}$ that the charge equation lacks: charge is never created or destroyed, but field energy can turn into heat or come from chemistry.
>
> (e) **False.** The step $\mathbf{E}\cdot\partial\mathbf{D}/\partial t = \partial(\tfrac12\epsilon E^2)/\partial t$ needs $\epsilon$ to be constant *in time* at each point. A dependence on position is harmless, because $\partial/\partial t$ does not act on it, so layered and graded dielectrics are fine. What breaks the step is an $\epsilon$ that changes in time (then an extra $\tfrac12E^2\,\partial\epsilon/\partial t$ appears), a nonlinear medium, or hysteresis.
>
> (f) **False.** For static fields $\nabla\times\mathbf{E} = 0$, and with no free current $\nabla\times\mathbf{H} = 0$, so $\nabla\cdot\mathbf{S} = \mathbf{H}\cdot(\nabla\times\mathbf{E}) - \mathbf{E}\cdot(\nabla\times\mathbf{H}) = 0$ everywhere. The lines of $\mathbf{S}$ close on themselves, and the flux through every closed surface is zero. Nothing changes and nothing heats up, so no energy can be arriving or leaving.
>
> **Answer.** (a) T, (b) F, (c) T, (d) T, (e) F, (f) F.

### 20.2 Joule heating at a point

> [!easy] Easy · Joule heating · time average
> At a point inside a conducting medium with $\sigma = 0.02$ S/m the current density is $\mathbf{J} = -\hat{z}\,0.1\sin(\omega t)$ A/m², at a frequency low enough that $\mathbf{J} = \sigma\mathbf{E}$ holds at every instant.
> (a) Find $\mathbf{E}$ at that point.
> (b) Find the maximum and the time-averaged value of $\mathbf{J}\cdot\mathbf{E}$ there.
> (c) What does $\mathbf{J}\cdot\mathbf{E}$ measure? (Look at its unit.)
> (d) The medium is replaced by one with twice the conductivity. Find $\langle\mathbf{J}\cdot\mathbf{E}\rangle$ if the same $\mathbf{E}$ is applied, and if instead the same $\mathbf{J}$ is driven through it.
>
> *Source: Summer 2019 HE3 #1b and its conflict version, re-parameterized: a sine along $-\hat{z}$, a new $\sigma$ and amplitude; part (d) added.*

> [!solution]- Solution
> (a) $\mathbf{E} = \mathbf{J}/\sigma = -\hat{z}\,(0.1/0.02)\sin\omega t = -\hat{z}\,5\sin(\omega t)$ V/m, parallel to $\mathbf{J}$ at every instant.
>
> (b) $\mathbf{J}\cdot\mathbf{E} = (-0.1\sin\omega t)(-5\sin\omega t) = 0.5\sin^2(\omega t)$ W/m³ ($= \sigma E^2 = J^2/\sigma$). Its maximum is 0.5 W/m³, at $\omega t = \pi/2, 3\pi/2, \dots$; with $\langle\sin^2\rangle = \tfrac12$ the average is 0.25 W/m³.
>
> (c) W/m³ is a power per unit volume: $\mathbf{J}\cdot\mathbf{E}$ is the rate at which the field gives energy to the charges, which pass it to the material as heat (Joule heating, the point form of $I^2R$). Here that is 0.25 W per cubic metre on average, or 0.25 mW per litre. It is never negative, because $\mathbf{J}$ and $\mathbf{E}$ are always parallel; it touches zero twice per period.
>
> (d) Same $\mathbf{E}$: $\mathbf{J}$ doubles, and $\langle\sigma E^2\rangle$ doubles to 0.5 W/m³. Same $\mathbf{J}$: $\mathbf{E}$ halves, and $\langle J^2/\sigma\rangle$ halves to 0.125 W/m³. It is the circuit rule: at a fixed voltage $V^2/R$ grows as $R$ falls; at a fixed current $I^2R$ shrinks.
>
> **Watch out:** average the product, not the factors. $\langle J\rangle = \langle E\rangle = 0$, but $\langle\mathbf{J}\cdot\mathbf{E}\rangle = 0.25$ W/m³.
>
> **Answer.** (a) $\mathbf{E} = -\hat{z}\,5\sin(\omega t)$ V/m. (b) Maximum 0.5 W/m³, average 0.25 W/m³. (c) The power per unit volume the field delivers to the charges, here dissipated as heat. (d) 0.5 W/m³ with the same $\mathbf{E}$; 0.125 W/m³ with the same $\mathbf{J}$.

### 20.3 A laser pointer's beam

> [!easy] Easy · Poynting vector · time-average power · energy density
> Treat the beam of a laser pointer as a uniform plane wave filling a cross-section of area $A = 1.0$ mm². In air its electric field is $\mathbf{E} = \hat{z}\,240\pi\cos(\omega t + \beta y)$ V/m ($240\pi\approx754$). Use $\eta_0 = 120\pi\ \Omega$, $c = 3\times10^8$ m/s and $\epsilon_0 = 10^{-9}/(36\pi)$ F/m.
> (a) Which way does the beam travel? Find $\mathbf{H}$.
> (b) Find the instantaneous Poynting vector and its time average.
> (c) Find the power of the beam.
> (d) Find the time-averaged energy density, and the field energy in a 1 m length of the beam.
>
> *Source: original.*

> [!solution]- Solution
> (a) The phase $\omega t + \beta y$ stays constant where $y$ decreases as $t$ grows, so the beam travels toward $-\hat{y}$: a "+" between the two terms means the negative direction. With $\hat u = -\hat{y}$ and $(-\hat{y})\times\hat{z} = -\hat{x}$:
> $$
> \mathbf{H} = \frac{\hat u\times\mathbf{E}}{\eta_0} = -\hat{x}\,\frac{240\pi}{120\pi}\cos(\omega t + \beta y) = -\hat{x}\,2\cos(\omega t + \beta y)\ \text{A/m}.
> $$
> (b) $\mathbf{S} = \mathbf{E}\times\mathbf{H} = (240\pi)(2)\cos^2(\cdot)\,\hat{z}\times(-\hat{x}) = -\hat{y}\,480\pi\cos^2(\omega t + \beta y)\approx-\hat{y}\,1508\cos^2(\omega t + \beta y)$ W/m². It points along the travel at every instant and pulses between 0 and its peak at twice the light's frequency. With $\langle\cos^2\rangle = \tfrac12$: $\langle\mathbf{S}\rangle = -\hat{y}\,240\pi\approx-\hat{y}\,754$ W/m², which is $E_0^2/(2\eta_0)$.
>
> (c) $P = \langle S\rangle A = 754\ \text{W/m}^2\times10^{-6}\ \text{m}^2 = 0.754$ mW. The intensity is just over half that of sunlight (1361 W/m²), squeezed into 1 mm².
>
> (d) $\langle w\rangle = \langle S\rangle/c = 240\pi/(3\times10^8) = 8\pi\times10^{-7}\approx2.51\times10^{-6}$ J/m³. Directly: $\tfrac12\epsilon_0E_0^2 = \tfrac12\cdot\dfrac{10^{-9}}{36\pi}\,(240\pi)^2 = 8\pi\times10^{-7}$ J/m³ ✓, half of it electric and half magnetic. A 1 m length of beam holds $\langle w\rangle A\times1\ \text{m} = 2.51\times10^{-12}$ J $= P/c$: the energy that flows past a point in the 3.33 ns that light needs to travel 1 m.
>
> **Answer.** (a) Toward $-\hat{y}$; $\mathbf{H} = -\hat{x}\,2\cos(\omega t + \beta y)$ A/m. (b) $\mathbf{S} = -\hat{y}\,480\pi\cos^2(\omega t + \beta y)$ W/m²; $\langle\mathbf{S}\rangle = -\hat{y}\,240\pi\approx-\hat{y}\,754$ W/m². (c) 0.754 mW. (d) $\langle w\rangle = 8\pi\times10^{-7}\approx2.51\ \mu$J/m³; 2.51 pJ in 1 m of beam.

### 20.4 Standing waves, true or false

> [!easy] Easy · true or false · Poynting vector · energy density
> In free space two plane waves of equal amplitude travel in opposite directions along $x$: $\hat{y}\,E_0\cos(\omega t - \beta x)$ and $\hat{y}\,E_0\cos(\omega t + \beta x)$, with $\beta = \omega/c$. Their sum is the standing wave
> $$
> \begin{aligned}
> \mathbf{E} &= \hat{y}\,2E_0\cos(\omega t)\cos(\beta x),\\
> \mathbf{H} &= \hat{z}\,\frac{2E_0}{\eta_0}\sin(\omega t)\sin(\beta x).
> \end{aligned}
> $$
> True or false?
>
> (a) The Poynting vector of the standing wave is zero at every point and every instant.
>
> (b) Its time average $\langle\mathbf{S}\rangle$ is zero at every point.
>
> (c) Since no net energy flows, the energy density $\tfrac12\epsilon_0\mathbf{E}\cdot\mathbf{E} + \tfrac12\mu_0\mathbf{H}\cdot\mathbf{H}$ is zero throughout the region.
>
> (d) On the planes where $\mathbf{E}$ is zero at all times, the energy density is zero at all times.
>
> (e) The energy stored between two neighbouring planes on which $\mathbf{E}$ is always zero (per square metre of those planes) does not change with time.
>
> (f) If the wave travelling toward $-x$ had amplitude $E_0/2$ instead, the time-averaged power per unit area would be $3E_0^2/(8\eta_0)$, directed along $+\hat{x}$.
>
> *Source: SP17 Exam 3 #1c and FA23 Exam 3 #1(c) style (standing-wave true or false), extended to six statements.*

> [!solution]- Solution
> First multiply out. With $\hat{y}\times\hat{z} = \hat{x}$ and $\mu_0/\eta_0^2 = \epsilon_0$:
> $$
> \begin{aligned}
> \mathbf{S} &= \hat{x}\,\frac{E_0^2}{\eta_0}\sin(2\omega t)\sin(2\beta x),\\
> w &= 2\epsilon_0E_0^2\big[\cos^2(\omega t)\cos^2(\beta x) + \sin^2(\omega t)\sin^2(\beta x)\big].
> \end{aligned}
> $$
> (a) **False.** $\mathbf{S}$ vanishes only on the planes where $\sin2\beta x = 0$ (every quarter wavelength) or at the instants when $\sin2\omega t = 0$. Elsewhere energy sloshes back and forth within each quarter wavelength, reversing every quarter period.
>
> (b) **True.** $\langle\sin2\omega t\rangle = 0$, so $\langle\mathbf{S}\rangle = 0$ everywhere: the two waves carry $E_0^2/(2\eta_0)$ each, in opposite directions. Standing waves carry no net energy.
>
> (c) **False.** Averaging $w$ gives $\langle w\rangle = \epsilon_0E_0^2$ at every $x$, the sum of the two waves' $\tfrac12\epsilon_0E_0^2$ each. "No net flow" does not mean "no energy"; FA23 tests exactly this trap.
>
> (d) **False.** $\mathbf{E}$ is always zero where $\cos\beta x = 0$, for example at $x = \lambda/4$. There $\sin\beta x = \pm1$, so $\mathbf{H} = \pm\hat{z}\,(2E_0/\eta_0)\sin\omega t$ and $w = \tfrac12\mu_0H^2 = 2\epsilon_0E_0^2\sin^2(\omega t)$: all magnetic, and zero only at the instants when $\sin\omega t = 0$.
>
> (e) **True.** Between $x = \lambda/4$ and $3\lambda/4$, $\cos^2\beta x$ and $\sin^2\beta x$ each integrate to $\lambda/4$, so $\int w\,dx = 2\epsilon_0E_0^2\,\tfrac\lambda4\,(\cos^2\omega t + \sin^2\omega t) = \epsilon_0E_0^2\lambda/2$, the same at every instant. It must be: $\mathbf{S} = 0$ on those planes ($\sin2\beta x = 0$ there), so no energy crosses them. Inside, the energy only changes form, from electric near the maxima of $\mathbf{E}$ to magnetic near the maxima of $\mathbf{H}$ and back.
>
> (f) **True.** For two waves on one line travelling in opposite directions the cross terms cancel in $\mathbf{S}$: $H_z = (E_{1y} - E_{2y})/\eta_0$, so $S_x = E_yH_z = (E_{1y}^2 - E_{2y}^2)/\eta_0$. Averaging, $\langle S_x\rangle = \big(E_0^2 - E_0^2/4\big)/(2\eta_0) = 3E_0^2/(8\eta_0)>0$. The powers subtract, and the stronger wave wins.
>
> **Answer.** (a) F, (b) T, (c) F, (d) F, (e) T, (f) T.

### 20.5 How far a station reaches

> [!easy] Easy · find the error · intensity · time-average power
> A transmitter radiates an average power $P = 6$ kW, equally in all directions (an idealization), in free space. A receiver many wavelengths away, where the wave is locally a plane wave, needs a field amplitude of at least $E_{\min} = 10$ mV/m. How far away can it be? A student writes:
>
> "The power spreads evenly over a sphere of radius $r$, so $\langle S\rangle = P/(4\pi r^2)$. For a plane wave $\langle S\rangle = E_0^2/\eta_0$, so $E_0 = \sqrt{\eta_0P/(4\pi)}/r = \sqrt{30P}/r$ with $\eta_0 = 120\pi\ \Omega$. Setting $E_0 = 10$ mV/m gives $r = \sqrt{30\times6000}/0.01\approx42.4$ km."
>
> Find the slip, correct it, and give the range.
>
> *Source: original (the isotropic-transmitter argument of the Lecture 20 page, with a classic slip).*

> [!solution]- Solution
> **The slip:** $\langle S\rangle = E_0^2/\eta_0$. The field is $E_0\cos(\omega t - \beta r)$, so $S = (E_0^2/\eta_0)\cos^2(\cdot)$, whose time average is *half* its peak: $\langle S\rangle = E_0^2/(2\eta_0)$. The student used the peak of $S$ (equivalently, put the amplitude $E_0$ into the rms formula $\langle S\rangle = E_\text{rms}^2/\eta_0$, where $E_\text{rms} = E_0/\sqrt2$).
>
> **Fix:** $E_0 = \sqrt{2\eta_0\langle S\rangle} = \sqrt{2\eta_0P/(4\pi r^2)} = \sqrt{60P}/r$, so
> $$
> r = \frac{\sqrt{60\times6000}}{0.01}\ \text{m} = \frac{600}{0.01}\ \text{m} = 60\ \text{km}.
> $$
> **Check:** at 60 km, $\langle S\rangle = 6000/\big(4\pi(6\times10^4)^2\big) = 1.33\times10^{-7}$ W/m², and $E_0^2/(2\eta_0) = (0.01)^2/(240\pi) = 1.33\times10^{-7}$ W/m² ✓. The student's range is short by a factor $\sqrt2$.
>
> The sphere was right. In a steady state, the time-averaged Poynting theorem for the shell between two spheres, with nothing absorbing inside it, says that the same average power crosses every sphere: $\langle S\rangle\propto1/r^2$, and in the far field $E_0\propto1/r$.
>
> **Answer.** The slip is $\langle S\rangle = E_0^2/\eta_0$. With $\langle S\rangle = E_0^2/(2\eta_0)$, $E_0 = \sqrt{60P}/r$ and the range is 60 km, not 42.4 km.

## Medium

### 20.6 Split, then add

> [!medium] Medium · time-average power · plane waves
> In a lossless, non-magnetic dielectric with $\epsilon_r = 4$, a plane wave of frequency $f = 75$ MHz has
> $$
> \mathbf{E} = \hat{x}\,6\cos(\omega t + \beta z) - \hat{y}\,8\sin(\omega t + \beta z)\ \text{V/m}.
> $$
> Use $c = 3\times10^8$ m/s and $\eta_0 = 120\pi\ \Omega$.
> (a) Find the direction of travel, $v$, $\eta$ and $\beta$.
> (b) Find $\mathbf{H}$.
> (c) Let $\mathbf{E}_1 = \hat{x}(\mathbf{E}\cdot\hat{x})$ be the $x$ component alone, with its own magnetic field $\mathbf{H}_1$. Find $\langle\mathbf{E}_1\times\mathbf{H}_1\rangle$.
> (d) Find $\langle\mathbf{E}\times\mathbf{H}\rangle$ for the whole wave. Why does the answer not depend on the quarter-period shift between the two components?
> (e) At $z = 0$, find the largest and smallest values of $\lvert\mathbf{S}\rvert$ during a period, and the values of $\omega t$ at which they occur.
> (f) Find the average power through a square window of side 0.5 m lying in a plane $z$ = const.
>
> *Source: Summer 2019 HE3 #1a(iv)–(v) style ("split, then add"), re-parameterized: real fields only, a dielectric instead of vacuum, unequal amplitudes, travel along $-\hat{z}$; parts (e)–(f) added.*

> [!hint]- Hint
> The sign between $\omega t$ and $\beta z$ gives the direction. Each component is a plane wave in its own right, with $\mathbf{H} = \hat u\times\mathbf{E}/\eta$. For waves that all travel along $\hat u$, $\mathbf{S} = \hat u\,\lvert\mathbf{E}\rvert^2/\eta$ at every instant.

> [!solution]- Solution
> **Setup.** Both components travel the same way, so they share $\hat u$, $v$ and $\eta$. Each is a plane wave on its own, and Lecture 20's averages do the rest.
>
> **(a)** $\omega t + \beta z$: travel toward $-\hat{z}$. $v = c/\sqrt4 = 1.5\times10^8$ m/s, $\eta = \eta_0/2 = 60\pi\approx188.5\ \Omega$, $\beta = \omega/v = 2\pi(75\times10^6)/(1.5\times10^8) = \pi$ rad/m ($\lambda = 2$ m).
>
> **(b)** With $\hat u = -\hat{z}$: $(-\hat{z})\times\hat{x} = -\hat{y}$ and $(-\hat{z})\times(-\hat{y}) = -\hat{x}$. So
> $$
> \begin{aligned}
> \mathbf{H} &= -\hat{y}\,\frac{6}{60\pi}\cos(\omega t + \beta z) - \hat{x}\,\frac{8}{60\pi}\sin(\omega t + \beta z)\\
> &\approx-\hat{y}\,0.0318\cos(\omega t + \beta z) - \hat{x}\,0.0424\sin(\omega t + \beta z)\ \text{A/m}.
> \end{aligned}
> $$
> **(c)** $\mathbf{E}_1\times\mathbf{H}_1 = (6)(6/\eta)\cos^2(\cdot)\,\hat{x}\times(-\hat{y}) = -\hat{z}\,(36/\eta)\cos^2(\omega t + \beta z)$, so
> $$
> \langle\mathbf{E}_1\times\mathbf{H}_1\rangle = -\hat{z}\,\frac{36}{2\eta} = -\hat{z}\,\frac{3}{10\pi}\approx-\hat{z}\,0.0955\ \text{W/m}^2 .
> $$
> **(d)** For one direction of travel, $\mathbf{S} = \mathbf{E}\times(\hat u\times\mathbf{E})/\eta = \hat u\,\lvert\mathbf{E}\rvert^2/\eta$ (because $\mathbf{E}\cdot\hat u = 0$), and $\lvert\mathbf{E}\rvert^2 = E_x^2 + E_y^2$ has no cross term since $\hat{x}\cdot\hat{y} = 0$. Each square averages to half its peak, whatever its phase:
> $$
> \langle\mathbf{E}\times\mathbf{H}\rangle = -\hat{z}\,\frac{36 + 64}{2\eta} = -\hat{z}\,\frac{5}{6\pi}\approx-\hat{z}\,0.265\ \text{W/m}^2 ,
> $$
> the $x$ part's 0.0955 W/m² plus the $y$ part's $64/(2\eta)\approx0.170$ W/m². Perpendicular components carry power independently.
>
> **(e)** At $z = 0$: $\lvert\mathbf{S}\rvert = (36\cos^2\omega t + 64\sin^2\omega t)/\eta = (36 + 28\sin^2\omega t)/\eta$. Smallest: $36/\eta\approx0.191$ W/m² at $\omega t = 0, \pi$ (when $\mathbf{E} = \pm\hat{x}\,6$ V/m). Largest: $64/\eta\approx0.340$ W/m² at $\omega t = \pi/2, 3\pi/2$ (when $\mathbf{E} = \mp\hat{y}\,8$ V/m). It never drops to zero, because the two components never vanish together. A single linear wave with the same average power (amplitude 10 V/m) would swing between 0 and $100/\eta\approx0.531$ W/m².
>
> **(f)** $P = \lvert\langle\mathbf{S}\rangle\rvert\times(0.5\ \text{m})^2 = \dfrac{5}{6\pi}\times0.25 = \dfrac{5}{24\pi}\approx0.0663$ W $= 66.3$ mW.
>
> **Check:** for the $y$ part, $(-\hat{y})\times(-\hat{x}) = -\hat{z}$, along the travel ✓. Energy: $\langle w\rangle = \epsilon\langle\lvert\mathbf{E}\rvert^2\rangle = 4\epsilon_0\times50\ \text{V}^2/\text{m}^2 = 1.77\times10^{-9}$ J/m³, and $v\langle w\rangle = 0.265$ W/m² ✓.
>
> **Answer.** (a) Toward $-\hat{z}$; $v = 1.5\times10^8$ m/s, $\eta = 60\pi\approx188.5\ \Omega$, $\beta = \pi$ rad/m. (b) $\mathbf{H} = -\hat{y}\,0.0318\cos(\omega t + \beta z) - \hat{x}\,0.0424\sin(\omega t + \beta z)$ A/m. (c) $-\hat{z}\,3/(10\pi)\approx-\hat{z}\,0.0955$ W/m². (d) $-\hat{z}\,5/(6\pi)\approx-\hat{z}\,0.265$ W/m², whatever the phase shift. (e) Smallest 0.191 W/m² at $\omega t = 0, \pi$; largest 0.340 W/m² at $\omega t = \pi/2, 3\pi/2$. (f) 66.3 mW.

### 20.7 A leaky spherical capacitor

> [!medium] Medium · Poynting's theorem · Joule heating · conductance
> Two concentric, perfectly conducting spheres of radii $a = 1$ cm and $b = 3$ cm are separated by a lossy dielectric with $\epsilon = 6\epsilon_0$ and $\sigma = 2.0\times10^{-7}$ S/m. At $t = 0$ the inner sphere is at $V_0 = 1.0$ kV relative to the outer one; the spheres carry charges $\pm Q_0$, so there is no field outside, and they are then left isolated. (Calculator problem; $\epsilon_0 = 8.85\times10^{-12}$ F/m.)
> (a) Find the relaxation time $\tau$, the capacitance $C$, $Q_0$, and $\mathbf{E}(r,t)$ between the spheres.
> (b) Find $\mathbf{J}$ and $\partial\mathbf{D}/\partial t$ between the spheres. Explain why $\mathbf{H} = 0$ there, and what that means for $\mathbf{S}$.
> (c) At $r = a$ and $t = 0$ find $w$ and $\mathbf{J}\cdot\mathbf{E}$, and show that $\partial w/\partial t = -\mathbf{J}\cdot\mathbf{E}$ at every point and instant.
> (d) Find the stored energy $W(t)$ and the total Joule heating rate $P(t)$, and show that the total heat produced, $\int_0^\infty P\,dt$, equals $W(0)$. When has half of the stored energy gone, and when half of the charge?
>
> *Source: original (the leaky-capacitor example of the Lecture 20 page in spherical geometry, where $\mathbf{H} = 0$ holds exactly).*

> [!hint]- Hint
> From Lecture 10 the charge relaxes as $e^{-t/\tau}$ with $\tau = \epsilon/\sigma$, while $\mathbf{E}$ keeps its static shape $\propto1/r^2$. Compare $\sigma\mathbf{E}$ with $\epsilon\,\partial\mathbf{E}/\partial t$.

> [!solution]- Solution
> **Setup.** Spherical symmetry gives $\mathbf{E} = \hat{r}E(r,t)$; Lecture 10's relaxation gives its time dependence; Poynting's theorem is then applied point by point.
>
> **(a)** $\tau = \epsilon/\sigma = 6\times8.85\times10^{-12}/(2\times10^{-7}) = 266$ µs. $C = 4\pi\epsilon\,ab/(b - a) = 4\pi(6\epsilon_0)(0.015\ \text{m}) = 10.0$ pF and $Q_0 = CV_0 = 10.0$ nC. Gauss's law gives $E = Q/(4\pi\epsilon r^2)$ with $Q = Q_0e^{-t/\tau}$:
> $$
> \mathbf{E} = \hat{r}\,\frac{V_0\,ab}{(b - a)\,r^2}\,e^{-t/\tau} = \hat{r}\,\frac{15\ \text{V}\cdot\text{m}}{r^2}\,e^{-t/\tau},
> $$
> which at $t = 0$ is $1.50\times10^5$ V/m at $r = a$ and $1.67\times10^4$ V/m at $r = b$.
>
> **(b)** $\mathbf{J} = \sigma\mathbf{E} = \hat{r}\,(3.0\times10^{-6}\ \text{A}/r^2)\,e^{-t/\tau}$, outward (0.030 A/m² at $r = a$, $t = 0$). And $\partial\mathbf{D}/\partial t = \epsilon\,\partial\mathbf{E}/\partial t = -(\epsilon/\tau)\mathbf{E} = -\sigma\mathbf{E} = -\mathbf{J}$. The total current density $\mathbf{J} + \partial\mathbf{D}/\partial t$ is zero everywhere, so the Ampère–Maxwell law gives $\nabla\times\mathbf{H} = 0$. Symmetry finishes the job: a spherically symmetric source cannot pick out a tangential direction, and a radial $\mathbf{H}(r)$ would make $\oint\mathbf{B}\cdot d\mathbf{A} = 4\pi r^2B_r\neq0$, a magnetic charge. So $\mathbf{H} = 0$, and $\mathbf{S} = \mathbf{E}\times\mathbf{H} = 0$: no energy moves anywhere.
>
> **(c)** At $r = a$, $t = 0$: $w = \tfrac12\epsilon E^2 = \tfrac12(6\times8.85\times10^{-12})(1.5\times10^5)^2 = 0.597$ J/m³ and $\mathbf{J}\cdot\mathbf{E} = \sigma E^2 = 2\times10^{-7}\times(1.5\times10^5)^2 = 4500$ W/m³. In general, with $\partial\mathbf{E}/\partial t = -\mathbf{E}/\tau$,
> $$
> \frac{\partial w}{\partial t} = \epsilon\,\mathbf{E}\cdot\frac{\partial\mathbf{E}}{\partial t} = -\frac{\epsilon}{\tau}E^2 = -\sigma E^2 = -\mathbf{J}\cdot\mathbf{E},
> $$
> which is Poynting's theorem with $\nabla\cdot\mathbf{S} = 0$. Each cubic metre turns its own stored energy into heat, at the rate $2w/\tau$ (at $r = a$: $2\times0.597/266\ \mu\text{s}\approx4500$ W/m³ ✓).
>
> **(d)** $W(t) = \tfrac12CV_0^2\,e^{-2t/\tau}$, with $W(0) = \tfrac12(10.0\ \text{pF})(1000\ \text{V})^2 = 5.00\ \mu$J. The heating rate is
> $$
> \begin{aligned}
> P(t) &= \int_a^b\sigma E^2\,4\pi r^2\,dr = 4\pi\sigma\Big(\frac{V_0ab}{b - a}\Big)^2\Big(\frac1a - \frac1b\Big)e^{-2t/\tau}\\
> &= \frac{4\pi\sigma ab}{b - a}\,V_0^2\,e^{-2t/\tau},
> \end{aligned}
> $$
> that is $GV_0^2e^{-2t/\tau}$ with $G = 3.77\times10^{-8}$ S, so $P(0) = 37.7$ mW $= 2W(0)/\tau$. Then $\int_0^\infty P\,dt = P(0)\,\tau/2 = 5.00\ \mu\text{J} = W(0)$ ✓: every joule stored ends as heat without ever moving. Half the energy is gone when $e^{-2t/\tau} = \tfrac12$, at $t = (\tau/2)\ln2 = 92$ µs; half the charge only at $\tau\ln2 = 184$ µs, because the energy goes as the square of the charge.
>
> **Check:** $W(0)$ also equals $\int\tfrac12\epsilon E^2\,dV = 5.00\ \mu$J ✓, and $P(0)$ has units (S)(V²) = W ✓.
>
> **Answer.** (a) $\tau = 266$ µs, $C = 10.0$ pF, $Q_0 = 10.0$ nC, $\mathbf{E} = \hat{r}\,(15\ \text{V}\cdot\text{m}/r^2)\,e^{-t/\tau}$. (b) $\mathbf{J} = -\partial\mathbf{D}/\partial t = \hat{r}\,(3.0\times10^{-6}/r^2)\,e^{-t/\tau}$ A/m²; their sum is zero and symmetry allows no $\mathbf{H}$, so $\mathbf{H} = 0$ and $\mathbf{S} = 0$. (c) $w = 0.597$ J/m³, $\mathbf{J}\cdot\mathbf{E} = 4500$ W/m³; $\partial w/\partial t = -\sigma E^2$. (d) $W = 5.00\,e^{-2t/\tau}\ \mu$J, $P = 37.7\,e^{-2t/\tau}$ mW, total heat 5.00 µJ; half the energy at 92 µs, half the charge at 184 µs.

### 20.8 Energy flows into a solenoid

> [!medium] Medium · Poynting's theorem · power flow · magnetic energy
> A long air-core solenoid of radius $a = 2$ cm with $n = 1000$ turns/m lies along the $z$ axis. Its current rises at a steady rate, $I(t) = kt$ with $k = 50$ A/s, and flows along $+\hat\phi$, so that $\mathbf{H} = \hat{z}\,nI(t)$ inside (Lecture 13) and $\mathbf{H} = 0$ outside.
> (a) Use Faraday's law to find the induced $\mathbf{E}$ inside ($r<a$). Then find $\mathbf{S}$ inside at $t = 0.2$ s, with its direction.
> (b) At a point inside, find $\partial w/\partial t$, $\nabla\cdot\mathbf{S}$ and $\mathbf{J}\cdot\mathbf{E}$, and confirm Poynting's theorem. Confirm also that $\nabla\cdot\mathbf{S} = \mathbf{H}\cdot(\nabla\times\mathbf{E}) - \mathbf{E}\cdot(\nabla\times\mathbf{H})$.
> (c) Find the power that crosses the cylinder $r = a$ into the interior, per metre of length, at $t = 0.2$ s, and compare it with $\dfrac{d}{dt}\big(\tfrac12\mathcal{L}I^2\big)$, where $\mathcal{L}$ is the inductance per unit length.
> (d) Treat the winding as a surface current $\mathbf{J}_s = \hat\phi\,nI$ on $r = a$. Find $\mathbf{J}_s\cdot\mathbf{E}$ there. What does its sign say?
>
> *Source: classic (energy flowing into an inductor), new numbers.*

> [!hint]- Hint
> Faraday's law on a circle of radius $r<a$, counter-clockwise seen from $+z$: $E_\phi\cdot2\pi r = -\dfrac{d}{dt}\big(\mu_0nI\,\pi r^2\big)$. For a radial vector field, $\nabla\cdot(S_r\hat{r}) = \dfrac1r\dfrac{\partial(rS_r)}{\partial r}$.

> [!solution]- Solution
> **Setup.** Inside, $\mathbf{H}$ is uniform and grows linearly in time; Faraday's law gives a circulating $\mathbf{E}$ that is constant in time. Then $\mathbf{S} = \mathbf{E}\times\mathbf{H}$, and the theorem can be checked term by term.
>
> **(a)** From the hint, $E_\phi = -\mu_0nkr/2$:
> $$
> \begin{aligned}
> \mathbf{E} &= -\hat\phi\,\frac{\mu_0nkr}{2},\\
> E_\phi(a) &= -\frac{4\pi\times10^{-7}\times1000\times50\times0.02}{2} = -6.28\times10^{-4}\ \text{V/m},
> \end{aligned}
> $$
> clockwise seen from $+z$, against the winding current (Lenz). At $t = 0.2$ s, $I = 10$ A and $H = nI = 10^4$ A/m. With $\hat\phi\times\hat{z} = \hat{r}$,
> $$
> \mathbf{S} = \Big(-\frac{\mu_0nkr}{2}\Big)(nkt)\,\hat\phi\times\hat{z} = -\hat{r}\,\frac{\mu_0n^2k^2rt}{2},
> $$
> radially **inward**, with size 6.28 W/m² at $r = a$.
>
> **(b)** $\partial w/\partial t = \partial(\tfrac12\mu_0H^2)/\partial t = \mu_0n^2k^2t = 628$ W/m³ at $t = 0.2$ s, the same at every point inside. ($\tfrac12\epsilon_0E^2$, about $10^{-18}$ J/m³, does not change in time.) Next, $\nabla\cdot\mathbf{S} = \dfrac1r\dfrac{\partial}{\partial r}\Big(-\dfrac{\mu_0n^2k^2r^2t}{2}\Big) = -\mu_0n^2k^2t = -628$ W/m³. There is no current inside, so $\mathbf{J}\cdot\mathbf{E} = 0$. Sum: $628 - 628 + 0 = 0$ ✓. For the identity: $\nabla\times\mathbf{E} = \hat{z}\,\dfrac1r\dfrac{\partial(rE_\phi)}{\partial r} = -\hat{z}\,\mu_0nk$, so $\mathbf{H}\cdot(\nabla\times\mathbf{E}) = -\mu_0n^2k^2t = -628$ W/m³; $\mathbf{H}$ is uniform, so $\nabla\times\mathbf{H} = 0$ and $\mathbf{E}\cdot(\nabla\times\mathbf{H}) = 0$. The difference is $-628$ W/m³ $= \nabla\cdot\mathbf{S}$ ✓.
>
> **(c)** Inflow per metre: $\lvert\mathbf{S}(a)\rvert\cdot2\pi a = \mu_0n^2k^2\,\pi a^2\,t = 6.28\times2\pi(0.02) = 0.790$ W/m. With $\mathcal{L} = \mu_0n^2\pi a^2 = 1.58\times10^{-3}$ H/m (Lecture 15), $\dfrac{d}{dt}\big(\tfrac12\mathcal{L}I^2\big) = \mathcal{L}Ik = 1.58\times10^{-3}\times10\times50 = 0.790$ W/m ✓. The magnetic energy of an inductor arrives through the side of its winding, not along the wires.
>
> **(d)** $\mathbf{E}$ is continuous across the winding, so there $\mathbf{E} = -\hat\phi\,6.28\times10^{-4}$ V/m while $\mathbf{J}_s = +\hat\phi\,10^4$ A/m: $\mathbf{J}_s\cdot\mathbf{E} = -6.28$ W/m². Negative, so the winding is a **source**. The generator drives the current against the induced field (the back emf) and hands the field 6.28 W per square metre of winding, exactly the inward flux just inside. Outside, $\mathbf{H} = 0$ and so $\mathbf{S} = 0$: none of it goes outward. In the sheet form of the theorem, with $\hat n = \hat{r}$ from the inside (2) to the outside (1): $\hat{r}\cdot(\mathbf{S}_1 - \mathbf{S}_2) = 0 - (-6.28) = 6.28$ W/m² $= -\mathbf{J}_s\cdot\mathbf{E}$ ✓.
>
> **Answer.** (a) $\mathbf{E} = -\hat\phi\,\mu_0nkr/2$ ($6.28\times10^{-4}$ V/m at $r = a$); $\mathbf{S} = -\hat{r}\,\mu_0n^2k^2rt/2$, inward, 6.28 W/m² at $r = a$. (b) $\partial w/\partial t = 628$ W/m³, $\nabla\cdot\mathbf{S} = -628$ W/m³, $\mathbf{J}\cdot\mathbf{E} = 0$; $\mathbf{H}\cdot(\nabla\times\mathbf{E}) = -628$ W/m³ and $\mathbf{E}\cdot(\nabla\times\mathbf{H}) = 0$. (c) 0.790 W/m $= \mathcal{L}Ik$. (d) $\mathbf{J}_s\cdot\mathbf{E} = -6.28$ W/m²: the winding injects the power that flows inward.

## Hard

### 20.9 A coax with a resistive core

> [!hard] Hard · Poynting vector · Joule heating · power flow
> A coaxial cable of length $\ell = 10$ m lies along the $z$ axis. Its inner conductor, of radius $a = 1$ mm, is a resistive alloy with $\sigma\approx3.18\times10^5$ S/m, chosen so that its resistance per metre is $R' = 1/(\sigma\pi a^2) = 1.00\ \Omega$/m. The outer conductor, of inner radius $b = 4$ mm, is a perfect conductor, and the dielectric between them is lossless. A battery of $V_0 = 100$ V connects the two conductors at $z = 0$ (inner conductor positive), and a load $R_L = 40\ \Omega$ connects them at $z = \ell$. Consider the DC steady state and ignore end effects.
> (a) Find the current $I$, the voltage $V(z)$ of the inner conductor relative to the outer one, and the powers delivered by the battery, dissipated in the inner conductor and dissipated in the load.
> (b) In the dielectric the potential is $\Phi(r,z) = V(z)\ln(b/r)/\ln(b/a)$. Find $\mathbf{E}$ and $\mathbf{H}$ there. Check that $\Phi$ satisfies Laplace's equation, that $E_z$ is continuous at $r = a$, and that the tangential $\mathbf{E}$ vanishes at $r = b$.
> (c) Find $S_z$, and the total power crossing the dielectric's cross-section at $z = 0$ and at $z = \ell$.
> (d) Find $S_r$ just outside the inner conductor and just inside the outer one. How much power enters the inner conductor per metre? Show that the integral form of Poynting's theorem balances for the ring of dielectric between $z$ and $z + \Delta z$.
> (e) Find the ratio $\lvert S_r\rvert/S_z$ just outside the inner conductor at $z = 0$ and at $z = \ell$. What does it say about the direction of energy flow?
>
> *Source: original (the coax and the resistive wire of the Lecture 20 page in one device).*

> [!hint]- Hint
> Inside the inner conductor $\mathbf{E} = \hat{z}\,J/\sigma$ is uniform over the cross-section, so the conductor's surface potential falls linearly along $z$. Write $\mathbf{S}$ component by component, with $\hat{r}\times\hat\phi = \hat{z}$ and $\hat{z}\times\hat\phi = -\hat{r}$.

> [!solution]- Solution
> **Setup.** The circuit gives $I$ and $V(z)$. The given $\Phi$ gives $\mathbf{E}$ in the dielectric, which now has a small axial part; Ampère's law gives $\mathbf{H}$; then $\mathbf{S}$. The ledger is checked on a ring of dielectric.
>
> **(a)** In series, $R'\ell + R_L = 10 + 40 = 50\ \Omega$, so $I = 100/50 = 2$ A, along $+\hat{z}$ in the inner conductor and back along $-\hat{z}$ in the outer one. The inner conductor's potential falls by $IR' = 2$ V per metre: $V(z) = 100 - 2z$ V ($z$ in m), and $V(\ell) = 80$ V $= IR_L$ ✓. Powers: battery $V_0I = 200$ W; inner conductor $I^2R'\ell = 40$ W; load $V(\ell)I = 160$ W.
>
> **(b)** $\nabla^2\Phi = \dfrac1r\dfrac{\partial}{\partial r}\Big(r\dfrac{\partial\Phi}{\partial r}\Big) + \dfrac{\partial^2\Phi}{\partial z^2} = 0 + V''(z)\,\dfrac{\ln(b/r)}{\ln(b/a)} = 0$, because $V$ is linear in $z$; and $\Phi(a,z) = V(z)$, $\Phi(b,z) = 0$ ✓. Then $\mathbf{E} = -\nabla\Phi$ and Ampère's law give
> $$
> \begin{aligned}
> E_r &= \frac{V(z)}{r\ln(b/a)},\\
> E_z &= -\frac{dV}{dz}\,\frac{\ln(b/r)}{\ln(b/a)} = IR'\,\frac{\ln(b/r)}{\ln(b/a)},\\
> \mathbf{H} &= \hat\phi\,\frac{I}{2\pi r}.
> \end{aligned}
> $$
> At $r = a$: $E_z = IR' = 2$ V/m, the same as $J/\sigma = I/(\sigma\pi a^2) = 2$ V/m inside the inner conductor ✓. At $r = b$: $E_z = 0$ ✓. Numbers at $r = a$: $E_r = 72.1$ kV/m at $z = 0$ and 57.7 kV/m at $z = \ell$ (with $\ln4 = 1.386$); $H = I/(2\pi a) = 318$ A/m.
>
> **(c)** $\mathbf{S} = (E_r\hat{r} + E_z\hat{z})\times H_\phi\hat\phi = E_rH_\phi\,\hat{z} - E_zH_\phi\,\hat{r}$. The axial part,
> $$
> \begin{aligned}
> S_z &= \frac{V(z)\,I}{2\pi r^2\ln(b/a)},\\
> \int_a^bS_z\,2\pi r\,dr &= \frac{V(z)\,I}{\ln(b/a)}\int_a^b\frac{dr}{r} = V(z)\,I ,
> \end{aligned}
> $$
> carries 200 W through the cross-section at $z = 0$ and 160 W at $z = \ell$, toward the load. (Just outside the inner conductor at $z = 0$, $S_z = 2.30\times10^7$ W/m²: a huge flux density, through a small area.)
>
> **(d)** The radial part:
> $$
> \begin{aligned}
> S_r &= -E_zH_\phi = -\frac{I^2R'\,\ln(b/r)}{2\pi r\ln(b/a)},\\
> S_r(a) &= -\frac{I^2R'}{2\pi a} = -\frac{4}{2\pi\times10^{-3}} = -637\ \text{W/m}^2 ,
> \end{aligned}
> $$
> pointing **into** the inner conductor; $S_r(b) = 0$, since a perfect conductor allows no $E_z$. Per metre of inner conductor: $637\times2\pi a = 4$ W/m $= I^2R'$, exactly its Joule heat; over 10 m, 40 W ✓.
>
> Ledger for the ring $a<r<b$ between $z$ and $z + \Delta z$: nothing is stored (DC) and no current flows in the dielectric, so the outward flux must be zero. Through the two ends: $V(z + \Delta z)I - V(z)I = -I^2R'\Delta z$. Through $r = a$, where the outward normal of the ring is $-\hat{r}$: $+I^2R'\Delta z$. Through $r = b$: 0. Total: 0 ✓. (For $2<z<3$ m: $188 - 192 + 4 + 0 = 0$ W.)
>
> **(e)** At $r = a$, $\lvert S_r\rvert/S_z = E_z/E_r = IR'\,a\ln(b/a)/V(z)$: $2\times10^{-3}\times1.386/100 = 2.77\times10^{-5}$ at $z = 0$ and $3.47\times10^{-5}$ at $z = \ell$, a tilt of only $0.0016^\circ$ to $0.0020^\circ$. Energy flows almost exactly along the cable, through the dielectric. A tiny inward tilt peels off the 4 W/m that heats the inner conductor, and the tilt grows toward the load as $V(z)$ falls.
>
> **Check:** with a perfect inner conductor ($\sigma\to\infty$) $E_z = 0$, $\mathbf{S}$ is purely axial and $V(z)I = V_0I$ at every $z$: the coax of the Lecture 20 page. Overall, battery $=$ inner conductor $+$ load: $200 = 40 + 160$ W ✓.
>
> **Answer.** (a) $I = 2$ A, $V(z) = 100 - 2z$ V; 200 W from the battery, 40 W in the inner conductor, 160 W in the load. (b) $E_r = V(z)/(r\ln4)$, $E_z = IR'\ln(b/r)/\ln4$, $\mathbf{H} = \hat\phi\,I/(2\pi r)$; $E_z = 2$ V/m at $r = a$ and 0 at $r = b$. (c) $S_z = V(z)I/(2\pi r^2\ln4)$; 200 W at $z = 0$, 160 W at $z = \ell$. (d) $S_r(a) = -637$ W/m² (inward), $S_r(b) = 0$; 4 W/m enters the inner conductor; the ring balances. (e) $2.77\times10^{-5}$ at $z = 0$ and $3.47\times10^{-5}$ at $z = \ell$: the flow is almost exactly axial.

### 20.10 A sheet in a magnetic medium

> [!hard] Hard · current sheet radiation · energy balance · time-average power
> An infinitesimally thin sheet on the plane $y = 0$ carries the surface current $\mathbf{J}_s = -\hat{x}\,u(t)\sin(\omega t)$ A/m, with $\omega = 5\pi\times10^6$ rad/s ($f = 2.5$ MHz) and $u(t)$ the unit step. A lossless medium with $\mu_r = 4$ and $\epsilon_r = 4$ fills all space. Use $c = 3\times10^8$ m/s, $\eta_0 = 120\pi\ \Omega$ and $\epsilon_0 = 10^{-9}/(36\pi)$ F/m.
> (a) Find $v$, $\eta$, $\beta$ and $\lambda$ in the medium.
> (b) Write $\mathbf{E}$ and $\mathbf{H}$ for $y>0$ and for $y<0$.
> (c) Find $\mathbf{J}_s\cdot\mathbf{E}$ on the sheet for $t>0$, and its time average (the "average Joule heating rate" of the radiator). What does its sign mean?
> (d) Find the time-averaged power per unit area carried into the region $y>0$, and check the energy balance at the sheet.
> (e) Find the time-averaged energy density behind the wavefronts and the ratio $\langle S\rangle/\langle w\rangle$. If the same current flowed in vacuum, which of $E_0$, $H_0$, $\langle S\rangle$, $\langle w\rangle$ and $\lambda$ would change, and by what factor?
> (f) The current is changed to $\mathbf{J}_s = -\hat{x}\,u(t)\big[\sin(\omega t) + 0.5\sin(3\omega t)\big]$ A/m. Find the new $\langle-\mathbf{J}_s\cdot\mathbf{E}\rangle$ on the sheet and the average power per unit area carried into $y>0$.
>
> *Source: Summer 2020 HE3 #2c–d, re-parameterized: a sheet on $y = 0$ carrying $-\hat{x}$ 1 A/m at 2.5 MHz in a medium with $\mu_r = \epsilon_r = 4$, instead of $\hat{y}$ 4 A/m at 1 MHz on $z = 0$ in vacuum; parts (e)–(f) added. Different also from the site's worked problem [[problems/energy-bookkeeping-for-a-radiating-sheet|Energy bookkeeping for a radiating sheet]].*

> [!hint]- Hint
> The Lecture 19 recipe holds in any lossless medium, with that medium's $v = c/\sqrt{\mu_r\epsilon_r}$ and $\eta = \eta_0\sqrt{\mu_r/\epsilon_r}$. On the sheet, $\mathbf{E} = -\tfrac\eta2\mathbf{J}_s(t)$ for any waveform. For (f), expand the square and average term by term over the period $2\pi/\omega$.

> [!solution]- Solution
> **Setup.** The Lecture 19 recipe gives the waves; Lecture 20's averages and the sheet balance $\hat n\cdot(\mathbf{S}_1 - \mathbf{S}_2) = -\mathbf{J}_s\cdot\mathbf{E}$ give the power.
>
> **(a)** $v = c/\sqrt{16} = 7.5\times10^7$ m/s (75 m/µs), $\eta = \eta_0\sqrt{4/4} = 120\pi\approx377\ \Omega$, $\beta = \omega/v = 5\pi\times10^6/(7.5\times10^7) = \pi/15\approx0.209$ rad/m, and $\lambda = 2\pi/\beta = 30$ m ($= v/f$ ✓).
>
> **(b)** $\mathbf{E} = -\tfrac\eta2\mathbf{J}_s(t - \lvert y\rvert/v) = +\hat{x}\,60\pi\,u(t - \lvert y\rvert/v)\sin(\omega t - \beta\lvert y\rvert)$ V/m on both sides ($60\pi\approx188.5$). For $\mathbf{H} = \tfrac12\mathbf{J}_s\times\hat n$: $(-\hat{x})\times\hat{y} = -\hat{z}$ and $(-\hat{x})\times(-\hat{y}) = +\hat{z}$, so
> $$
> \mathbf{H} = \mp\hat{z}\,0.5\,u\Big(t\mp\frac yv\Big)\sin(\omega t\mp\beta y)\ \text{A/m}\qquad(y\gtrless0).
> $$
> Checks: $\hat{x}\times(-\hat{z}) = +\hat{y}$ and $\hat{x}\times\hat{z} = -\hat{y}$, away from the sheet ✓; $60\pi/0.5 = 120\pi = \eta$ ✓; $\hat{y}\times(\mathbf{H}^+ - \mathbf{H}^-) = \hat{y}\times(-\hat{z}\sin\omega t) = -\hat{x}\sin\omega t = \mathbf{J}_s$ ✓.
>
> **(c)** On the sheet $\mathbf{E}(0,t) = \hat{x}\,60\pi\sin\omega t$, so
> $$
> \begin{aligned}
> \mathbf{J}_s\cdot\mathbf{E} &= (-\sin\omega t)(60\pi\sin\omega t) = -60\pi\sin^2(\omega t)\ \text{W/m}^2,\\
> \langle\mathbf{J}_s\cdot\mathbf{E}\rangle &= -30\pi\approx-94.2\ \text{W/m}^2 .
> \end{aligned}
> $$
> Negative: the sheet is a **source**. Whatever drives the current pushes it against $\mathbf{E}$ and delivers 94.2 W per square metre of sheet on average ($\eta J_0^2/4$ with $J_0 = 1$ A/m).
>
> **(d)** Behind the front, $\mathbf{S} = \pm\hat{y}\,(60\pi)(0.5)\sin^2(\omega t\mp\beta y) = \pm\hat{y}\,30\pi\sin^2(\omega t\mp\beta y)$ W/m², so $\langle\mathbf{S}\rangle = \pm\hat{y}\,15\pi\approx\pm\hat{y}\,47.1$ W/m². The power carried into $y>0$ is **47.1 W/m², half** of the injected 94.2 W/m²; the same medium on both sides takes the other half into $y<0$. Balance: $15\pi + 15\pi = 30\pi$ ✓. It holds even at every instant at the sheet: $30\pi\sin^2\omega t$ leaves through each face, and the two add up to $-\mathbf{J}_s\cdot\mathbf{E} = 60\pi\sin^2\omega t$.
>
> **(e)** For one wave the electric and magnetic parts are equal, so $\langle w\rangle = \epsilon\langle E^2\rangle = (4\epsilon_0)(60\pi)^2/2 = 2\pi\times10^{-7}\approx6.28\times10^{-7}$ J/m³. Then $\langle S\rangle/\langle w\rangle = 15\pi/(2\pi\times10^{-7}) = 7.5\times10^7$ m/s $= v$ ✓: the energy moves at the wave speed. In vacuum the same current meets the same $\eta = 120\pi\ \Omega$, so $E_0 = 60\pi$ V/m, $H_0 = 0.5$ A/m and $\langle S\rangle = 15\pi$ W/m² are **unchanged**. But $v = c$ is 4 times larger, so $\langle w\rangle = \langle S\rangle/c = 1.57\times10^{-7}$ J/m³ is 4 times **smaller**, and $\lambda = 120$ m is 4 times **longer**. $\eta$ decides how much power a given current draws; $v$ decides how densely that power is packed.
>
> **(f)** $\mathbf{E}(0,t) = -\tfrac\eta2\mathbf{J}_s(t)$ still holds (the medium treats every frequency alike), so $-\mathbf{J}_s\cdot\mathbf{E} = \tfrac\eta2\lvert\mathbf{J}_s\rvert^2 = 60\pi\big[\sin\omega t + 0.5\sin3\omega t\big]^2$. Over one period $2\pi/\omega$: $\langle\sin^2\omega t\rangle = \tfrac12$, $\langle0.25\sin^23\omega t\rangle = 0.125$, and $\langle\sin\omega t\,\sin3\omega t\rangle = \tfrac12\langle\cos2\omega t - \cos4\omega t\rangle = 0$. So
> $$
> \langle-\mathbf{J}_s\cdot\mathbf{E}\rangle = 60\pi(0.5 + 0.125) = 37.5\pi\approx118\ \text{W/m}^2 ,
> $$
> the $30\pi$ of the fundamental plus $7.5\pi$ for the third harmonic: different frequencies carry power independently, like perpendicular components. Into $y>0$ goes half, $18.75\pi\approx58.9$ W/m².
>
> **Watch out:** the exam calls $\langle\mathbf{J}_s\cdot\mathbf{E}\rangle$ the "average Joule heating rate" even here, where it is negative. A positive answer means $\mathbf{E}$ was taken along $\mathbf{J}_s$ instead of against it.
>
> **Answer.** (a) $v = 7.5\times10^7$ m/s, $\eta = 120\pi\approx377\ \Omega$, $\beta = \pi/15\approx0.209$ rad/m, $\lambda = 30$ m. (b) $\mathbf{E} = \hat{x}\,60\pi\,u(t - \lvert y\rvert/v)\sin(\omega t - \beta\lvert y\rvert)$ V/m; $\mathbf{H} = \mp\hat{z}\,0.5\,u(t\mp y/v)\sin(\omega t\mp\beta y)$ A/m for $y\gtrless0$. (c) $\mathbf{J}_s\cdot\mathbf{E} = -60\pi\sin^2\omega t$ W/m², average $-30\pi\approx-94.2$ W/m² (a source). (d) $15\pi\approx47.1$ W/m² into $y>0$; $15\pi + 15\pi = 30\pi$ ✓. (e) $\langle w\rangle = 2\pi\times10^{-7}\approx6.28\times10^{-7}$ J/m³, $\langle S\rangle/\langle w\rangle = v$; in vacuum $E_0$, $H_0$, $\langle S\rangle$ are unchanged, $\langle w\rangle$ is 4 times smaller and $\lambda$ 4 times longer. (f) $37.5\pi\approx118$ W/m² injected, $18.75\pi\approx58.9$ W/m² into $y>0$.

### 20.11 Two sheets in step

> [!hard] Hard · current sheet radiation · superposition · energy balance
> Two parallel current sheets in free space carry equal currents in step: $\mathbf{J}_A = \hat{x}\,J_0\cos(\omega t)$ on the plane $z = 0$ and $\mathbf{J}_B = \hat{x}\,J_0\cos(\omega t)$ on the plane $z = d$, with $J_0 = 1$ A/m and $f = 100$ MHz. Use $c = 3\times10^8$ m/s and $\eta_0 = 120\pi\ \Omega$.
> (a) Find $\beta$ and $\lambda$. Write the total $\mathbf{E}$ for $z>d$ and for $z<0$ as a single cosine whose amplitude depends on $d$.
> (b) Find $\langle\mathbf{S}\rangle$ in both outer regions as a function of $d$.
> (c) Find $\langle-\mathbf{J}_A\cdot\mathbf{E}\rangle$ on sheet A and $\langle-\mathbf{J}_B\cdot\mathbf{E}\rangle$ on sheet B, with $\mathbf{E}$ the *total* field on each sheet. Show that the two sheets together inject exactly the power that leaves through the outer regions.
> (d) Evaluate (b) and (c) for $d = 0.75$ m, $d = 1.5$ m and $d\to0$, and compare with one sheet alone.
> (e) Show that $\langle\mathbf{S}\rangle = 0$ between the sheets. Where, then, does each sheet's power go?
>
> *Source: original.*

> [!hint]- Hint
> Superpose the two sheets' waves. On each sheet, use its own field plus the other sheet's field, delayed by $d/c$. You need $\cos A + \cos B = 2\cos\tfrac{A - B}{2}\cos\tfrac{A + B}{2}$ and $\langle\cos(\omega t)\cos(\omega t - \theta)\rangle = \tfrac12\cos\theta$.

> [!solution]- Solution
> **Setup.** Each sheet radiates as if alone (Lecture 19): $-\hat{x}\,\tfrac{\eta_0}{2}J_0 = -\hat{x}\,60\pi$ V/m in amplitude on both of its sides. Superpose, then average.
>
> **(a)** $\beta = \omega/c = 2\pi\times10^8/(3\times10^8) = 2\pi/3\approx2.09$ rad/m and $\lambda = 3$ m. For $z>d$ both waves travel toward $+z$; B's has $d/c$ less delay, so its phase is ahead by $\beta d$:
> $$
> \begin{aligned}
> \mathbf{E} &= -\hat{x}\,60\pi\big[\cos(\omega t - \beta z) + \cos(\omega t - \beta z + \beta d)\big]\\
> &= -\hat{x}\,120\pi\cos\frac{\beta d}{2}\,\cos\Big(\omega t - \beta z + \frac{\beta d}{2}\Big)\ \text{V/m}.
> \end{aligned}
> $$
> For $z<0$, in the same way, $\mathbf{E} = -\hat{x}\,120\pi\cos(\beta d/2)\cos(\omega t + \beta z - \beta d/2)$ V/m. The amplitude is $120\pi\lvert\cos(\beta d/2)\rvert$ on both sides.
>
> **(b)** Each outer region holds a single plane wave, so $\langle S\rangle = E_0^2/(2\eta_0)$ along its travel:
> $$
> \langle\mathbf{S}\rangle = \pm\hat{z}\,\frac{(120\pi)^2\cos^2(\beta d/2)}{2\times120\pi} = \pm\hat{z}\,60\pi\cos^2\frac{\beta d}{2}\ \text{W/m}^2 ,
> $$
> with $+$ for $z>d$ and $-$ for $z<0$.
>
> **(c)** On sheet A the total field is its own $-\hat{x}\,60\pi\cos\omega t$ plus B's wave, which arrives delayed by $d/c$: $\mathbf{E}(0,t) = -\hat{x}\,60\pi\big[\cos\omega t + \cos(\omega t - \beta d)\big]$. Then
> $$
> \begin{aligned}
> \langle-\mathbf{J}_A\cdot\mathbf{E}\rangle &= 60\pi\big[\langle\cos^2\omega t\rangle + \langle\cos\omega t\cos(\omega t - \beta d)\rangle\big]\\
> &= 30\pi(1 + \cos\beta d) = 60\pi\cos^2\frac{\beta d}{2}\ \text{W/m}^2 ,
> \end{aligned}
> $$
> and the same on sheet B, by symmetry. Together the sheets inject $120\pi\cos^2(\beta d/2)$, exactly the $60\pi\cos^2(\beta d/2)$ leaving through each of the two outer regions ✓.
>
> **(d)** One sheet alone injects $\eta_0J_0^2/4 = 30\pi\approx94.2$ W/m² and sends $15\pi\approx47.1$ W/m² each way.
> - $d = 0.75$ m $= \lambda/4$: $\cos^2(\pi/4) = \tfrac12$. Each sheet injects $30\pi\approx94.2$ W/m², the same as alone, but each outer region now receives $30\pi$, twice a lone sheet's share (amplitude $120\pi/\sqrt2\approx267$ V/m).
> - $d = 1.5$ m $= \lambda/2$: $\cos^2(\pi/2) = 0$. Nothing is radiated, and neither sheet injects anything. In fact $\mathbf{E} = 0$ on each sheet at every instant: the other sheet's field, arriving half a period late, cancels its own.
> - $d\to0$: $\cos^2\to1$. Each sheet injects $60\pi\approx188.5$ W/m², twice its solo value, and each side receives $60\pi$: $120\pi\approx377$ W/m² in total, four times one sheet. The two merge into one sheet carrying $2J_0$, and $\eta_0(2J_0)^2/4 = 120\pi$ ✓.
>
> **(e)** Between the sheets A's wave travels toward $+z$ and B's toward $-z$, each with amplitude $60\pi$ V/m. For counter-propagating waves the powers subtract (as in 20.4(f)): $\langle S_z\rangle = \big[(60\pi)^2 - (60\pi)^2\big]/(2\eta_0) = 0$. No average power crosses the gap, so each sheet's power goes entirely to its own outer side: A's $60\pi\cos^2(\beta d/2)$ to $z<0$, B's to $z>d$. Check with the sheet form at A, $\hat n = \hat{z}$: $\langle S_z(0^+)\rangle - \langle S_z(0^-)\rangle = 0 + 60\pi\cos^2(\beta d/2) = \langle-\mathbf{J}_A\cdot\mathbf{E}\rangle$ ✓.
>
> **Watch out:** a sheet's power depends on the field the *other* sheet produces at its location. Interference does not create or destroy energy; it changes how much each source delivers.
>
> **Answer.** (a) $\beta = 2\pi/3$ rad/m, $\lambda = 3$ m; $\mathbf{E} = -\hat{x}\,120\pi\cos(\beta d/2)\cos(\omega t\mp\beta z\pm\beta d/2)$ V/m, upper signs for $z>d$ and lower signs for $z<0$. (b) $\pm\hat{z}\,60\pi\cos^2(\beta d/2)$ W/m². (c) Each sheet injects $60\pi\cos^2(\beta d/2)$ W/m²; the total, $120\pi\cos^2(\beta d/2)$, equals the total outflow. (d) $d = 0.75$ m: 94.2 W/m² per sheet and per side; $d = 1.5$ m: 0; $d\to0$: 188.5 W/m² per sheet and per side (377 W/m² in total, four times one sheet's 94.2 W/m²). (e) $\langle\mathbf{S}\rangle = 0$ between the sheets; each sheet feeds only its own outer side.

### 20.12 Charging a leaky capacitor

> [!hard] Hard · Poynting's theorem · displacement current · conductance
> A parallel-plate capacitor has circular plates of radius $a = 5$ cm in the planes $z = 0$ and $z = d = 2$ mm; ignore fringing. The gap is filled with a slightly conducting dielectric, $\epsilon = 4\epsilon_0$, whose conductivity makes the leakage resistance between the plates $R = 10$ MΩ. The capacitor is uncharged until $t = 0$; then a constant current $I = 10\ \mu$A charges it. The current arrives along $+\hat{z}$ through a thin lead on the axis below the bottom plate and leaves along $+\hat{z}$ through a lead above the top plate. Let $V(t)$ be the voltage of the bottom plate relative to the top one. (Calculator problem; $\epsilon_0 = 8.85\times10^{-12}$ F/m.)
> (a) Find $C$, $\sigma$, $\tau = RC$ and $V(t)$.
> (b) Find $\mathbf{E}$, $\mathbf{J}$ and $\partial\mathbf{D}/\partial t$ in the gap. Show that $\mathbf{J} + \partial\mathbf{D}/\partial t$ is uniform and constant in time, and find $\mathbf{H}$ in the gap for $r<a$.
> (c) Find $\mathbf{S}$ in the gap and the power entering through the side surface $r = a$. Show that it equals $V(t)I$.
> (d) At $r = a/2$ and $t = \tau$, evaluate $\partial w/\partial t$, $\nabla\cdot\mathbf{S}$ and $\mathbf{J}\cdot\mathbf{E}$, and check Poynting's theorem.
> (e) For the whole gap at $t = \tau$, check $-dW/dt = \oint\mathbf{S}\cdot d\mathbf{A} + \int\mathbf{J}\cdot\mathbf{E}\,dV$. What fraction of the inflow is being stored at $t = 0^+$, at $t = \tau$, and as $t\to\infty$?
>
> *Source: classic (the charging capacitor is fed through its sides), with a lossy dielectric added.*

> [!hint]- Hint
> Lecture 10's circuit model: $I$ feeds $C$ in parallel with $R$, so $I = C\,dV/dt + V/R$. In the gap, the Ampère–Maxwell law on a circle of radius $r$ counts the conduction plus displacement current through the disk it bounds; ask how that total is spread over the plate area.

> [!solution]- Solution
> **Setup.** The circuit gives $V(t)$ and the uniform field $E = V/d$; the Ampère–Maxwell law gives $\mathbf{H}$; then $\mathbf{S}$, and a theorem with all three terms non-zero.
>
> **(a)** $A = \pi a^2 = 7.85\times10^{-3}$ m², $C = \epsilon A/d = 139$ pF, $\sigma = d/(RA) = 2.55\times10^{-8}$ S/m, and $\tau = RC = 1.39$ ms ($= \epsilon/\sigma$ ✓). Solving $I = C\,dV/dt + V/R$ with $V(0) = 0$:
> $$
> V(t) = IR\big(1 - e^{-t/\tau}\big) = 100\big(1 - e^{-t/\tau}\big)\ \text{V},\qquad V(\tau) = 63.2\ \text{V}.
> $$
> **(b)** The bottom plate charges positive, so $\mathbf{E} = \hat{z}\,V/d = \hat{z}\,5\times10^4\big(1 - e^{-t/\tau}\big)$ V/m (31.6 kV/m at $t = \tau$). Then $\mathbf{J} = \sigma\mathbf{E} = \hat{z}\,\dfrac IA\big(1 - e^{-t/\tau}\big)$ and $\partial\mathbf{D}/\partial t = \epsilon\,\partial\mathbf{E}/\partial t = \hat{z}\,\dfrac IA\,e^{-t/\tau}$, using $\sigma R/d = 1/A$ and $\epsilon R/(d\tau) = \epsilon/(dC) = 1/A$. Their sum is $\hat{z}\,I/A = \hat{z}\,1.27\times10^{-3}$ A/m², uniform and constant: all displacement current at first, all conduction current at the end (at $t = \tau$: $8.05\times10^{-4}$ and $4.68\times10^{-4}$ A/m²). The Ampère–Maxwell law on a circle of radius $r$, counter-clockwise seen from $+z$:
> $$
> H_\phi\cdot2\pi r = \frac IA\,\pi r^2\quad\Longrightarrow\quad\mathbf{H} = \hat\phi\,\frac{Ir}{2\pi a^2},
> $$
> independent of time and of the losses: $3.18\times10^{-5}$ A/m at $r = a$ and $1.59\times10^{-5}$ A/m at $r = a/2$.
>
> **(c)** With $\hat{z}\times\hat\phi = -\hat{r}$:
> $$
> \begin{aligned}
> \mathbf{S} &= -\hat{r}\,\frac Vd\,\frac{Ir}{2\pi a^2},\\
> \lvert\mathbf{S}(a)\rvert\cdot2\pi a\,d &= \frac Vd\,\frac{I}{2\pi a}\,2\pi a\,d = V(t)\,I .
> \end{aligned}
> $$
> Energy flows radially **inward** from the space around the plates, not along the leads. At $t = \tau$: $\lvert\mathbf{S}(a)\rvert = 1.01$ W/m² over a side area of $6.28\times10^{-4}$ m², that is $VI = 63.2\ \text{V}\times10\ \mu\text{A} = 0.632$ mW.
>
> **(d)** At $t = \tau$, $E = 3.16\times10^4$ V/m and $dE/dt = (IR/d\tau)\,e^{-1} = 1.32\times10^7$ V/(m·s). Then
> - $\partial w/\partial t = \epsilon E\,dE/dt = 14.8$ W/m³ (uniform; $\mathbf{H}$ does not change);
> - $\nabla\cdot\mathbf{S} = \dfrac1r\dfrac{\partial(rS_r)}{\partial r} = -\dfrac{EI}{\pi a^2} = -40.2$ W/m³ (uniform too);
> - $\mathbf{J}\cdot\mathbf{E} = \sigma E^2 = 25.4$ W/m³.
>
> Sum: $14.8 - 40.2 + 25.4 = 0$ ✓. Energy converges on every point of the gap; part of it is stored and the rest becomes heat. (Here $\nabla\times\mathbf{E} = 0$, so $\nabla\cdot\mathbf{S} = -\mathbf{E}\cdot(\nabla\times\mathbf{H}) = -E\,I/A$, the same number.)
>
> **(e)** All three densities are uniform, so multiply by the gap volume $Ad = 1.57\times10^{-5}$ m³: $dW/dt = 232.5\ \mu$W, $\int\mathbf{J}\cdot\mathbf{E}\,dV = 399.6\ \mu$W ($= V^2/R$ ✓), and $\oint\mathbf{S}\cdot d\mathbf{A} = -632.1\ \mu$W (an inflow). Then $-232.5 = -632.1 + 399.6\ \mu$W ✓. The stored fraction is
> $$
> \frac{dW/dt}{VI} = \frac{CV\,dV/dt}{VI} = \frac CI\,\frac{dV}{dt} = e^{-t/\tau}:
> $$
> 100 % at $t = 0^+$ (no voltage yet, so no leakage), 36.8 % at $t = \tau$, and 0 as $t\to\infty$. In the end $V\to100$ V, the capacitor acts as the 10 MΩ resistor, and every watt entering through the side becomes heat, like the wire of the Lecture 20 page.
>
> **Answer.** (a) $C = 139$ pF, $\sigma = 2.55\times10^{-8}$ S/m, $\tau = 1.39$ ms, $V = 100(1 - e^{-t/\tau})$ V. (b) $\mathbf{E} = \hat{z}\,5\times10^4(1 - e^{-t/\tau})$ V/m, $\mathbf{J} = \hat{z}\,1.27\times10^{-3}(1 - e^{-t/\tau})$ A/m², $\partial\mathbf{D}/\partial t = \hat{z}\,1.27\times10^{-3}e^{-t/\tau}$ A/m²; $\mathbf{H} = \hat\phi\,Ir/(2\pi a^2)$, $3.18\times10^{-5}$ A/m at $r = a$. (c) $\mathbf{S} = -\hat{r}\,(V/d)\,Ir/(2\pi a^2)$, inward; inflow $V(t)I$, 0.632 mW at $t = \tau$. (d) $14.8 - 40.2 + 25.4 = 0$ W/m³. (e) $-232.5 = -632.1 + 399.6\ \mu$W; stored fraction $e^{-t/\tau}$: 100 %, 36.8 %, 0.

### Sources for this page
Course notes and the site's Lecture 20 page: the derivation and the meaning of the terms (20.1), the leaky-capacitor example (20.7, moved to spherical geometry), the coax and resistive-wire examples (20.9, combined into one device), the isotropic-transmitter argument (20.5), and the time averages of plane waves and of the cosine sheet (20.3, 20.6, 20.10, 20.11). Old exams, re-parameterized: Summer 2019 HE3 #1b and its conflict version (20.2: $\mathbf{J}\cdot\mathbf{E}$ at a point, with new numbers and a part on doubling $\sigma$), SP17 Exam 3 #1c and FA23 Exam 3 #1(c) (20.4: standing-wave true or false, extended), Summer 2019 HE3 #1a(iv)–(v) (20.6: "split, then add" with real fields in a dielectric and unequal amplitudes), and Summer 2020 HE3 #2c–d (20.10: a new plane, current, amplitude and frequency, and a medium with $\mu_r = \epsilon_r = 4$; different from the site's worked problem). Classic: energy flowing into an inductor (20.8) and into a charging capacitor (20.12, here with a lossy dielectric). Original: 20.1, 20.3, 20.5, 20.7, 20.9 and 20.11.

*Previous: [[practice/19-radiation-from-current-sheets|Lecture 19 practice]] · next: [[practice/21-phasors-and-monochromatic-waves|Lecture 21 practice]] · [[practice/index|all practice]]*
