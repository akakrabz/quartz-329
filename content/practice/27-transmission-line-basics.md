---
title: "Practice — Lecture 27: Guided TEM waves on transmission lines"
description: "12 practice problems (5 easy, 3 medium, 4 hard) on guided TEM waves: line parameters from the geometrical factor for plates, coax and twin-lead, charges and currents on the conductors, the telegrapher's equations (with leakage) and the ladder model, forward and backward waves with I = ±V/Z₀, splitting a snapshot into two waves, the front launched by a battery, and power on a line; hints on the medium and hard ones, a worked solution for each."
tags: [practice, transmission-lines]
lecture: 27
---

*Practice for [[4-transmission-lines/27-guided-tem-waves-on-transmission-lines|Lecture 27]] · concepts: [[concepts/telegraphers-equations]] · [[concepts/characteristic-impedance]] · [[concepts/poynting-vector]] · all practice: [[practice/index|hub]] · by difficulty: [[practice/easy|easy]] · [[practice/medium|medium]] · [[practice/hard|hard]] · [[practice/topics|by topic]]*

Work each problem on paper first. Open the **hint** only when stuck, and the **solution** only after you have an answer you would hand in. Every answer here has been checked numerically.

The whole page runs on four lines.
- One homogeneous filling: $\mathcal{C} = \epsilon\,\text{GF}$, $\mathcal{L} = \mu/\text{GF}$, so $v = 1/\sqrt{\mathcal{L}\mathcal{C}} = 1/\sqrt{\mu\epsilon}$ and $Z_0 = \sqrt{\mathcal{L}/\mathcal{C}} = \eta/\text{GF}$.
- $V$ is conductor 2 relative to conductor 1; $I$ flows along $+z$ on conductor 2.
- $V = f+g$ and $Z_0I = f-g$: a forward wave has $V/I = +Z_0$, a backward one $-Z_0$.
- Power along $+z$: $p = VI$; one phasor wave carries $\lvert V^+\rvert^2/2Z_0$.

No loads, source resistances or reflections here: those start in [[4-transmission-lines/28-distributed-circuits-and-bounce-diagrams|Lecture 28]].

## Easy

### 27.1 Strip-line parameters

> [!easy] Easy · line parameters · parallel-plate line · characteristic impedance
> Two perfectly conducting strips $W = 6$ mm wide and $d = 0.5$ mm apart form a parallel-plate line filled with a non-magnetic dielectric, $\epsilon_r = 2.25$. Neglect fringing. Use $\eta_0 = 120\pi\ \Omega$, $c = 3\times10^8$ m/s, $\epsilon_0 = 10^{-9}/36\pi$ F/m.
>
> (a) Find $\mathcal{L}$, $\mathcal{C}$, $v$ and $Z_0$.
>
> (b) How long does a signal take to cross a 30 cm board?
>
> (c) Which width gives $Z_0 = 50\ \Omega$ with the same $d$ and filling? Is neglecting fringing still safe?
>
> *Source: original.*

> [!solution]- Solution
> (a) $\text{GF} = W/d = 12$ and $\eta = \eta_0/1.5 = 80\pi\ \Omega$:
> $$
> \begin{gathered}
> \mathcal{L} = \frac{\mu_0}{12} = 104.7\ \text{nH/m},\qquad \mathcal{C} = 2.25\epsilon_0\cdot12 = 239\ \text{pF/m},\\[4pt]
> v = \frac{c}{1.5} = 2\times10^8\ \text{m/s},\qquad Z_0 = \frac{\eta}{\text{GF}} = \frac{20\pi}{3} = 20.9\ \Omega.
> \end{gathered}
> $$
> (b) $0.3/(2\times10^8) = 1.5$ ns.
>
> (c) $W/d = \eta/Z_0 = 80\pi/50 = 5.03$, so $W = 2.51$ mm. With $W$ only five times $d$, fringing is no longer negligible: 2.5 mm is a first estimate.
>
> **Check:** $\mathcal{L}v = 104.7\times10^{-9}\cdot2\times10^8 = 20.9\ \Omega = Z_0$ ✓.
>
> **Answer.** (a) $\mathcal{L} = 104.7$ nH/m, $\mathcal{C} = 239$ pF/m, $v = 2\times10^8$ m/s, $Z_0 = 20\pi/3 = 20.9\ \Omega$; (b) 1.5 ns; (c) $W\approx2.5$ mm, but at $W/d\approx5$ fringing matters.

### 27.2 Telegrapher's equations, true or false

> [!easy] Easy · true or false · telegrapher's equations · characteristic impedance
> True or false? Every line is a lossless two-conductor line with one homogeneous filling.
>
> (a) On a parallel-plate line, the telegrapher's equations are Faraday's and Ampère's laws rewritten with $V = E_xd$ and $I = H_yW$.
>
> (b) A short length $\Delta z$ of line acts as a series capacitor $\Delta z\,\mathcal{C}$ with an inductor $\Delta z\,\mathcal{L}$ shunted across the line.
>
> (c) Whatever $V(z,t)$ is on the line, $V/I = Z_0$ everywhere.
>
> (d) For $V = g(t+z/v)$, $V/I = -Z_0$.
>
> (e) Thinning the inner conductor of an air-filled coax raises $Z_0$ and lowers $v$.
>
> *Source: SP18 Exam 3 #1(ii) and #1(v) style, as true/false with new statements.*

> [!solution]- Solution
> (a) **True.** Faraday gives $-\partial V/\partial z = \mathcal{L}\,\partial I/\partial t$; Ampère gives $-\partial I/\partial z = \mathcal{C}\,\partial V/\partial t$.
>
> (b) **False.** Reversed: a *series inductor* $\Delta z\,\mathcal{L}$ (the drop along the current) and a *shunt capacitor* $\Delta z\,\mathcal{C}$ (current from one conductor to the other). The swapped ladder is a high-pass filter, not a line.
>
> (c) **False.** Only a single forward wave has $V/I = Z_0$. For $V = f+g$, $V/I = Z_0(f+g)/(f-g)$ varies with $z$ and $t$.
>
> (d) **True.** A backward wave has $I = -g/Z_0$: with $V>0$, the current on conductor 2 flows toward $-z$.
>
> (e) **False.** $Z_0 = (\eta_0/2\pi)\ln(b/a)$ rises as $a$ shrinks, but $v = 1/\sqrt{\mu_0\epsilon_0} = c$ for any cross-section. With $b = 3.5$ mm, going from $a = 1$ mm to 0.5 mm takes $Z_0$ from 75.2 Ω to 116.8 Ω; $v = c$ both times.
>
> **Answer.** (a) T, (b) F, (c) F, (d) T, (e) F.

### 27.3 Charges and currents on turned plates

> [!easy] Easy · multiple choice · parallel-plate line · boundary conditions
> Perfectly conducting plates on $y = 0$ and $y = d$ ($W\gg d$ along $x$) guide $\mathbf{E} = \hat yE_0\cos(\omega t-\beta z)$, $E_0>0$, in a lossless filling of intrinsic impedance $\eta$. Where and when $E_y>0$, which is true?
>
> (a) The $y = 0$ plate carries negative charge and the $y = d$ plate positive charge.
>
> (b) Both plates carry positive charge.
>
> (c) The surface current on the $y = d$ plate points along $-\hat z$.
>
> (d) The voltage between the plates depends on the path of integration.
>
> (e) The plate currents flow along $\pm\hat x$, parallel to $\mathbf{H}$.
>
> *Source: SP17 Exam 3 #2(ii) style, plates moved to the planes y = 0 and y = d.*

> [!solution]- Solution
> Forward wave: $\mathbf{H} = \hat z\times\mathbf{E}/\eta = -\hat x\,E_y/\eta$. Take $\hat n$ from each plate into the gap:
> - $y = 0$, $\hat n = \hat y$: $\rho_s = \epsilon E_y>0$; $\mathbf{J}_s = \hat y\times(-\hat x)\,E_y/\eta = +\hat z\,E_y/\eta$.
> - $y = d$, $\hat n = -\hat y$: $\rho_s = -\epsilon E_y<0$; $\mathbf{J}_s = (-\hat y)\times(-\hat x)\,E_y/\eta = -\hat z\,E_y/\eta$.
>
> So **(c)**. The others:
> - (a) has the signs reversed: $\mathbf{E}$ points from the positive plate ($y = 0$) to the negative one.
> - (b) The plates carry equal and opposite charge.
> - (d) TEM fields have $B_z = 0$, so $\oint\mathbf{E}\cdot d\mathbf{l} = 0$ around any loop in a constant-$z$ plane: the voltage is path-independent.
> - (e) $\mathbf{J}_s = \hat n\times\mathbf{H}$ is perpendicular to $\mathbf{H}$, along $\pm\hat z$.
>
> **Check:** the positive plate carries current toward $+z$, as $I = +V/Z_0$ requires for a forward wave.
>
> **Answer.** (c).

### 27.4 Plane-wave power on a line

> [!easy] Easy · find the error · power · characteristic impedance
> An air-filled parallel-plate line with $W = 1.5$ cm and $d = 1$ mm carries $\tilde V(z) = 10e^{-j\beta z}$ V. A student writes:
>
> *"A wave carries amplitude squared over $2\eta_0$, so $\langle P\rangle = \lvert\tilde V\rvert^2/2\eta_0 = 100/(240\pi) = 0.133$ W."*
>
> Find the slip, give the correct $\langle P\rangle$, and confirm it from the fields.
>
> *Source: original.*

> [!solution]- Solution
> **Slip:** $\eta_0$ is the ratio $E/H$ of the fields. The ratio $V/I$ of a line wave is $Z_0 = \eta_0d/W$:
> $$
> Z_0 = \frac{120\pi}{15} = 8\pi = 25.1\ \Omega,\qquad \langle P\rangle = \frac{\lvert\tilde V\rvert^2}{2Z_0} = \frac{100}{16\pi} = 1.99\ \text{W}.
> $$
> **From the fields:** $E_x = V/d = 10^4$ V/m, $H_y = E_x/\eta_0 = 26.5$ A/m, $\langle S\rangle = \tfrac12E_xH_y = 132.6$ kW/m². Times $Wd = 1.5\times10^{-5}$ m²: 1.99 W ✓. Also $\tilde I = H_yW = 0.398$ A $= \tilde V/Z_0$ ✓.
>
> **Watch out:** units cannot catch this (V²/Ω either way). The student's value is low by $W/d = 15$.
>
> **Answer.** Use $Z_0$, not $\eta_0$: $\langle P\rangle = 100/(16\pi) = 1.99$ W.

### 27.5 From a datasheet to a cross-section

> [!easy] Easy · line parameters · characteristic impedance
> A non-magnetic cable is specified by $\mathcal{L} = 0.4\ \mu$H/m and $\mathcal{C} = 40$ pF/m. Use $c = 3\times10^8$ m/s and $\eta_0 = 120\pi\ \Omega$.
>
> (a) Find $v$, $Z_0$ and $\epsilon_r$ of the filling.
>
> (b) Find the delay of a 10 m length.
>
> (c) If it is a coax, find $b/a$. If instead it is a twin-lead with the same filling, find $D/2a$.
>
> *Source: original.*

> [!solution]- Solution
> (a) $v = 1/\sqrt{1.6\times10^{-17}} = 2.5\times10^8$ m/s; $Z_0 = \sqrt{10^4} = 100\ \Omega$; $\epsilon_r = (c/v)^2 = 1.44$.
>
> (b) $10/(2.5\times10^8) = 40$ ns.
>
> (c) $\eta = \eta_0/1.2 = 100\pi\ \Omega$ and $Z_0 = \eta/\text{GF}$:
> $$
> \begin{gathered}
> \text{coax: }\ln\frac ba = \frac{2\pi Z_0}{\eta} = 2,\qquad \frac ba = e^2 = 7.39,\\[4pt]
> \text{twin-lead: }\cosh^{-1}\frac{D}{2a} = \frac{\pi Z_0}{\eta} = 1,\qquad \frac{D}{2a} = \cosh1 = 1.54.
> \end{gathered}
> $$
> **Check:** $\mathcal{L}\mathcal{C} = 1.6\times10^{-17} = \mu_0\cdot1.44\epsilon_0$ ✓; the coax gives back $\mathcal{L} = (\mu_0/2\pi)\cdot2 = 0.4\ \mu$H/m ✓.
>
> **Answer.** (a) $v = 2.5\times10^8$ m/s, $Z_0 = 100\ \Omega$, $\epsilon_r = 1.44$; (b) 40 ns; (c) $b/a = e^2 = 7.39$; $D/2a = \cosh1 = 1.54$.

## Medium

### 27.6 Reading a line from V and I

> [!medium] Medium · telegrapher's equations · line parameters · time-average power
> A lossless line carries
> $$
> V(z,t) = 12\cos(10^9t+5z)\ \text{V},\qquad I(z,t) = -0.2\cos(10^9t+5z)\ \text{A},
> $$
> with $z$ in m, $t$ in s, and $I$ along $+z$ on conductor 2.
>
> (a) Which way does the wave travel, and how fast?
>
> (b) Find $\mathcal{L}$ and $\mathcal{C}$ by substituting $V$ and $I$ into the telegrapher's equations.
>
> (c) Find $Z_0$ two ways, and $\epsilon_r$ if the line is non-magnetic.
>
> (d) Find the time-average power and its direction.
>
> *Source: original.*

> [!hint]- Hint
> Write $\psi = 10^9t+5z$. Each equation becomes (number)$\cdot\sin\psi$ = (unknown)$\cdot$(number)$\cdot\sin\psi$. Keep every minus sign.

> [!solution]- Solution
> **(a)** $\psi$ stays constant if $z$ falls as $t$ grows: travel toward $-z$ at $v = \omega/\beta = 10^9/5 = 2\times10^8$ m/s.
>
> **(b)** With $\partial_z\cos\psi = -5\sin\psi$ and $\partial_t\cos\psi = -10^9\sin\psi$:
> $$
> \begin{gathered}
> -\frac{\partial V}{\partial z} = 60\sin\psi = \mathcal{L}\frac{\partial I}{\partial t} = \mathcal{L}\,(2\times10^8)\sin\psi\ \Rightarrow\ \mathcal{L} = 300\ \text{nH/m},\\[4pt]
> -\frac{\partial I}{\partial z} = -\sin\psi = \mathcal{C}\frac{\partial V}{\partial t} = -\mathcal{C}\,(1.2\times10^{10})\sin\psi\ \Rightarrow\ \mathcal{C} = 83.3\ \text{pF/m}.
> \end{gathered}
> $$
> **(c)** $\sqrt{\mathcal{L}/\mathcal{C}} = \sqrt{300\times10^{-9}\cdot1.2\times10^{10}} = 60\ \Omega$. Directly, $V/I = 12/(-0.2) = -60\ \Omega = -Z_0$, as a backward wave requires. $\epsilon_r = (c/v)^2 = 2.25$.
>
> **(d)** $p = VI = -2.4\cos^2\psi$, average $-1.2$ W; equally $\tfrac12\text{Re}\{\tilde V\tilde I^*\} = \tfrac12(12)(-0.2) = -1.2$ W. So 1.2 W flows toward $-z$.
>
> **Check:** $1/\sqrt{\mathcal{L}\mathcal{C}} = 1/\sqrt{2.5\times10^{-17}} = 2\times10^8$ m/s, matching (a).
>
> **Answer.** (a) Toward $-z$ at $2\times10^8$ m/s; (b) $\mathcal{L} = 300$ nH/m, $\mathcal{C} = 83.3$ pF/m; (c) $Z_0 = 60\ \Omega$ ($V/I = -Z_0$), $\epsilon_r = 2.25$; (d) 1.2 W toward $-z$.

### 27.7 Two bench measurements

> [!medium] Medium · line parameters · transmission lines · conductance
> A 20 m non-magnetic cable is open at its far end. Two measurements:
> - a 1 kHz meter at the near end reads 1.6 nF in parallel with 2 nS;
> - a fast step launched at the near end first appears at the far end 100 ns later.
>
> Use $c = 3\times10^8$ m/s and $\epsilon_0 = 10^{-9}/36\pi$ F/m.
>
> (a) Why may the meter treat the whole cable as one lumped capacitor?
>
> (b) Find $\mathcal{C}$, $v$, $\epsilon_r$, $\mathcal{L}$ and $Z_0$.
>
> (c) Find $\mathcal{G}$ and the conductivity of the filling.
>
> *Source: FA23 Exam 3 #4(d) style (filling from a delay), extended with a low-frequency capacitance measurement.*

> [!hint]- Hint
> At 1 kHz the cable is a tiny fraction of a wavelength, so $V$ is the same all along it. For (c), $\mathcal{G}$ and $\mathcal{C}$ share the geometrical factor ([[1-electrostatics/10-capacitance-and-conductance|Lecture 10]]).

> [!solution]- Solution
> **(a)** At 1 kHz, $\lambda = v/f = 2\times10^8/10^3 = 200$ km, $10^4$ times the length. $V$ and $I$ barely vary along the cable ($\ell\ll\lambda$), so it acts as one capacitor $\mathcal{C}\ell$ with one leakage conductance $\mathcal{G}\ell$.
>
> **(b)**
> $$
> \begin{gathered}
> \mathcal{C} = \frac{1.6\ \text{nF}}{20\ \text{m}} = 80\ \text{pF/m},\qquad v = \frac{20}{100\times10^{-9}} = 2\times10^8\ \text{m/s},\qquad \epsilon_r = \Big(\frac cv\Big)^2 = 2.25,\\[4pt]
> \mathcal{L} = \frac{1}{\mathcal{C}v^2} = 312.5\ \text{nH/m},\qquad Z_0 = \frac{1}{\mathcal{C}v} = 62.5\ \Omega.
> \end{gathered}
> $$
> **(c)** $\mathcal{G} = 2\ \text{nS}/20\ \text{m} = 0.1$ nS/m. $\mathcal{G} = \sigma\,\text{GF}$ and $\mathcal{C} = \epsilon\,\text{GF}$, so
> $$
> \sigma = \epsilon\,\frac{\mathcal{G}}{\mathcal{C}} = 2.25\cdot\frac{10^{-9}}{36\pi}\cdot\frac{10^{-10}}{8\times10^{-11}} = 2.5\times10^{-11}\ \text{S/m}.
> $$
> **Check:** $\sqrt{\mathcal{L}/\mathcal{C}} = \sqrt{312.5/0.08} = 62.5\ \Omega$ ✓; $\mathcal{L}\mathcal{C} = 2.5\times10^{-17} = \mu_0\cdot2.25\epsilon_0$ ✓. The exact input admittance of the open lossy line at 1 kHz equals the lumped $G+j\omega C$ to six digits.
>
> **Answer.** (a) $\ell/\lambda = 10^{-4}$; (b) $\mathcal{C} = 80$ pF/m, $v = 2\times10^8$ m/s, $\epsilon_r = 2.25$, $\mathcal{L} = 312.5$ nH/m, $Z_0 = 62.5\ \Omega$; (c) $\mathcal{G} = 0.1$ nS/m, $\sigma = 2.5\times10^{-11}$ S/m.

### 27.8 An artificial line

> [!medium] Medium · telegrapher's equations · transmission lines
> A delay line is built from 30 identical sections, each a series inductor $L_1 = 0.5\ \mu$H followed by a shunt capacitor $C_1 = 200$ pF: the ladder model of Lecture 27 with one section per $\Delta z$.
>
> (a) Find its characteristic impedance and total delay.
>
> (b) What length of polyethylene-filled coax ($\epsilon_r = 2.25$) has the same delay?
>
> (c) An ideal source applies a slowly rising 2 V step. Before anything returns, what current does it supply? Check by counting capacitor charge.
>
> (d) The ladder imitates a line only for wavelengths much longer than a section. With ten sections per wavelength, find the highest usable frequency.
>
> *Source: course notes, Lecture 27 ladder model, original numbers.*

> [!hint]- Hint
> One section is $\Delta z\,\mathcal{L} = L_1$ and $\Delta z\,\mathcal{C} = C_1$. Write $Z_0$ and the delay $\Delta z/v$ of one section in terms of $\mathcal{L}$, $\mathcal{C}$ and $\Delta z$; $\Delta z$ cancels.

> [!solution]- Solution
> **(a)** $Z_0 = \sqrt{\mathcal{L}/\mathcal{C}} = \sqrt{L_1/C_1} = \sqrt{2500} = 50\ \Omega$. One section delays by $\Delta z\sqrt{\mathcal{L}\mathcal{C}} = \sqrt{L_1C_1} = 10$ ns; 30 sections, 300 ns.
>
> **(b)** $v = c/1.5 = 2\times10^8$ m/s, so $300\ \text{ns}\times v = 60$ m.
>
> **(c)** A forward wave: $I = V/Z_0 = 2/50 = 40$ mA. Charge count: the front charges one more 200 pF capacitor to 2 V every 10 ns, so $I = 400\ \text{pC}/10\ \text{ns} = 40$ mA ✓.
>
> **(d)** One section takes 10 ns, so ten per wavelength means a period of at least 100 ns: $f\le10$ MHz.
>
> **Check:** integrating the ladder's circuit equations (100 ns ramp, 50 Ω at the far end) gives a delay within 2 % of 300 ns and an input current within 1 % of $V/Z_0$.
>
> **Answer.** (a) $Z_0 = 50\ \Omega$, delay 300 ns; (b) 60 m; (c) 40 mA; (d) about 10 MHz.

## Hard

### 27.9 A pulse on a coax

> [!hard] Hard · transmission lines · coax · Poynting vector
> A coax has inner radius $a = 0.4$ mm and $\ln(b/a) = 5/3$ (outer radius $b = 2.12$ mm), with a non-magnetic filling, $\epsilon_r = 4$. Use $\eta_0 = 120\pi\ \Omega$, $c = 3\times10^8$ m/s.
>
> (a) Find $\mathcal{L}$, $\mathcal{C}$, $v$ and $Z_0$.
>
> (b) A 0.3 A pulse lasting $T = 4$ ns travels toward $+z$, flowing along $+z$ on the **outer** conductor and back on the inner one. Inside it find $V$, $\mathbf{E}$, $\mathbf{H}$ and $\rho_s$ on each conductor.
>
> (c) Integrate the Poynting vector over the cross-section; compare with $VI$. Find the pulse's energy.
>
> (d) Instead, $\tilde{\mathbf{E}}(r = a) = \hat r\,15e^{-j\beta z}$ kV/m at 300 MHz. Find $\beta$, $\tilde V$, $\langle P\rangle$. Is TEM the only propagating mode?
>
> *Source: SP19 Exam 3 #2 style, recast for a coax with the current on the outer conductor.*

> [!hint]- Hint
> Let the inner conductor be conductor 2: $V$ is inner relative to outer, $I$ the $+z$ current on the inner one, so here $I = -0.3$ A. Between the conductors $E_r = V/(r\ln(b/a))$ and $H_\phi = I/(2\pi r)$, as in statics.

> [!solution]- Solution
> **(a)** $\text{GF} = 2\pi/\ln(b/a) = 6\pi/5$ and $\eta = 60\pi\ \Omega$:
> $$
> \begin{gathered}
> \mathcal{L} = \frac{\mu_0}{\text{GF}} = 333\ \text{nH/m},\qquad \mathcal{C} = 4\epsilon_0\,\text{GF} = 133\ \text{pF/m},\\[4pt]
> v = \frac c2 = 1.5\times10^8\ \text{m/s},\qquad Z_0 = \frac{\eta}{\text{GF}} = 50\ \Omega.
> \end{gathered}
> $$
> **(b)** The inner conductor carries the return: $I = -0.3$ A. Forward wave: $V = Z_0I = -15$ V. With $r$ in m,
> $$
> \mathbf{E} = \hat r\,\frac{V}{r\ln(b/a)} = -\hat r\,\frac{9}{r}\ \text{V/m},\qquad \mathbf{H} = \hat\phi\,\frac{I}{2\pi r} = -\hat\phi\,\frac{0.0477}{r}\ \text{A/m}.
> $$
> $\mathbf{E}$ points toward the axis: the outer conductor is positive. $\mathbf{E}\times\mathbf{H}\propto(-\hat r)\times(-\hat\phi) = +\hat z$ ✓. With $\hat n$ into the gap,
> $$
> \rho_s(a) = \epsilon E_r(a) = 4\epsilon_0\,(-22.5\ \text{kV/m}) = -0.796\ \mu\text{C/m}^2,\qquad \rho_s(b) = -\epsilon E_r(b) = +0.150\ \mu\text{C/m}^2.
> $$
> Per metre: $2\pi a\rho_s(a) = -2.0$ nC/m $= \mathcal{C}V$, and $+2.0$ nC/m on the outer conductor ✓.
>
> **(c)** $S_z = E_rH_\phi = \dfrac{2.7}{2\pi r^2}$ W/m², so
> $$
> P = \int_a^bS_z\,2\pi r\,dr = 2.7\ln\frac ba = 4.5\ \text{W} = VI = (-15)(-0.3).
> $$
> Energy: $4.5\ \text{W}\times4\ \text{ns} = 18$ nJ, in a pulse $vT = 0.6$ m long.
>
> **(d)** $\tilde V = E_r(a)\,a\ln(b/a) = 15\times10^3\cdot0.4\times10^{-3}\cdot\tfrac53 = 10$ V, so $\tilde V = 10e^{-j\beta z}$ V. $\beta = \omega/v = 4\pi = 12.6$ rad/m ($\lambda = 0.5$ m). $\langle P\rangle = \lvert\tilde V\rvert^2/2Z_0 = 1$ W. TEM only: $a+b = 2.52$ mm $<\lambda/\pi = 159$ mm; other modes need $f>v/\pi(a+b)\approx19$ GHz.
>
> **Check:** $\mathcal{L}v = 50\ \Omega = Z_0$ ✓; the stored energy per metre (half electric, half magnetic) times $v$ is again 4.5 W.
>
> **Answer.** (a) $\mathcal{L} = 333$ nH/m, $\mathcal{C} = 133$ pF/m, $v = 1.5\times10^8$ m/s, $Z_0 = 50\ \Omega$; (b) $V = -15$ V, $\mathbf{E} = -\hat r\,9/r$ V/m, $\mathbf{H} = -\hat\phi\,0.0477/r$ A/m, $\rho_s = -0.796\ \mu$C/m² (inner), $+0.150\ \mu$C/m² (outer); (c) 4.5 W $= VI$, 18 nJ; (d) $\beta = 4\pi$ rad/m, $\tilde V = 10e^{-j\beta z}$ V, $\langle P\rangle = 1$ W toward $+z$, TEM only.

### 27.10 Splitting a snapshot into two waves

> [!hard] Hard · transmission lines · moving pulses · energy
> A long lossless line has $Z_0 = 80\ \Omega$ and $v = 2\times10^8$ m/s. At $t = 0$ the section $-1\ \text{m}<z<1$ m holds $V = 12$ V and $I = 0.05$ A (along $+z$ on conductor 2); elsewhere $V = I = 0$.
>
> (a) Split the disturbance into a forward wave $f$ and a backward wave $g$.
>
> (b) Find $V$ and $I$ in every region of $z$ at $t = 2.5$ ns and at $t = 10$ ns.
>
> (c) Find $VI$ in each region at $t = 2.5$ ns; compare with $(f^2-g^2)/Z_0$.
>
> (d) Compare the stored energy at $t = 0$ with the pulses' energies.
>
> (e) Which initial current would send everything toward $+z$?
>
> *Source: original.*

> [!hint]- Hint
> At $t = 0$, $V = f+g$ and $Z_0I = f-g$ hold point by point. Solve for $f$ and $g$ on the section, then slide $f$ right and $g$ left by $vt$.

> [!solution]- Solution
> **(a)** $f = \tfrac12(V+Z_0I) = \tfrac12(12+4) = 8$ V and $g = \tfrac12(V-Z_0I) = 4$ V, each on the 2 m section at $t = 0$.
>
> **(b)** Each pulse moves $vt$: 0.5 m by 2.5 ns, 2 m by 10 ns. $V = f+g$, $I = (f-g)/Z_0$:
>
> | $t$ | region (m) | waves | $V$ | $I$ |
> |---|---|---|---|---|
> | 2.5 ns | $-1.5<z<-0.5$ | $g$ | 4 V | $-50$ mA |
> | 2.5 ns | $-0.5<z<0.5$ | $f+g$ | 12 V | $+50$ mA |
> | 2.5 ns | $0.5<z<1.5$ | $f$ | 8 V | $+100$ mA |
> | 10 ns | $-3<z<-1$ | $g$ | 4 V | $-50$ mA |
> | 10 ns | $1<z<3$ | $f$ | 8 V | $+100$ mA |
>
> Everywhere else $V = I = 0$; by 10 ns the pulses have separated and $-1<z<1$ is empty.
>
> **(c)** At 2.5 ns, $VI = -0.2$ W, $+0.6$ W, $+0.8$ W in the three regions. $(f^2-g^2)/Z_0$ gives $-16/80$, $(64-16)/80$, $64/80$: the same. $(f+g)(f-g) = f^2-g^2$ exactly, so each wave carries its own power even where they overlap.
>
> **(d)** $\mathcal{C} = 1/(Z_0v) = 62.5$ pF/m, $\mathcal{L} = Z_0/v = 400$ nH/m. At $t = 0$,
> $$
> W = 2\ \text{m}\times\big(\tfrac12\mathcal{C}V^2+\tfrac12\mathcal{L}I^2\big) = 2\,(4.5+0.5)\ \text{nJ} = 10\ \text{nJ}.
> $$
> Each pulse passes a point in $2\ \text{m}/v = 10$ ns: forward $0.8\ \text{W}\times10\ \text{ns} = 8$ nJ, backward $0.2\ \text{W}\times10\ \text{ns} = 2$ nJ. Total 10 nJ ✓.
>
> **(e)** $g = 0$ needs $Z_0I = V$: $I = 12/80 = 0.15$ A.
>
> **Check:** solving the telegrapher's equations directly from the initial $V$ and $I$ (spectral solver, no splitting) reproduces every entry of the table.
>
> **Answer.** (a) $f = 8$ V forward, $g = 4$ V backward; (b) the table; (c) $-0.2$, $+0.6$, $+0.8$ W $= (f^2-g^2)/Z_0$; (d) 10 nJ $= 8+2$ nJ; (e) 0.15 A.

### 27.11 The battery and the front

> [!hard] Hard · transmission lines · surface charge · telegrapher's equations
> Plates $W = 3$ cm wide at $x = 0$ and $x = d = 1$ mm, with an unknown non-magnetic filling, form a long line (no fringing). At $t = 0$ an ideal 12 V battery is connected at $z = 0$, $+$ terminal to the $x = d$ plate. The step reaches a probe at $z = 30$ m at $t = 200$ ns. Use $c = 3\times10^8$ m/s, $\eta_0 = 120\pi\ \Omega$.
>
> (a) Find $v$, $\epsilon_r$, $\mathcal{L}$, $\mathcal{C}$ and $Z_0$.
>
> (b) Behind the front find $V$ and $I$ (plate 2 at $x = 0$, as in the lecture), $\mathbf{E}$, $\mathbf{H}$, and $\rho_s$, $\mathbf{J}_s$ on each plate.
>
> (c) Without the telegrapher's equations, show $I = \mathcal{C}vV$ (charge conservation on plate 2) and $V = \mathcal{L}vI$ (Faraday, a loop spanning the front). Deduce $v$ and $Z_0$.
>
> *Source: course notes, Lecture 27 battery example, extended.*

> [!hint]- Hint
> In time $dt$ the front moves $v\,dt$. Plate 2 gains the charge $\mathcal{C}V\,v\,dt$ of the newly charged length, and only $I$ at a point behind the front can bring it. For Faraday, the flux through the loop grows because the field region inside it lengthens.

> [!solution]- Solution
> **(a)** $v = 30/(200\times10^{-9}) = 1.5\times10^8$ m/s, $\epsilon_r = (c/v)^2 = 4$, $\eta = 60\pi\ \Omega$, $\text{GF} = W/d = 30$:
> $$
> \mathcal{L} = \frac{\mu_0}{30} = 41.9\ \text{nH/m},\qquad \mathcal{C} = 4\epsilon_0\cdot30 = 1.06\ \text{nF/m},\qquad Z_0 = \frac{60\pi}{30} = 2\pi = 6.28\ \Omega.
> $$
> **(b)** $V$ is plate 2 ($x = 0$) relative to plate 1, so $V = -12$ V. Forward wave: $I = V/Z_0 = -6/\pi = -1.91$ A.
> $$
> \mathbf{E} = \hat x\,\frac Vd = -\hat x\,12\ \text{kV/m},\qquad \mathbf{H} = \hat y\,\frac IW = -\hat y\,63.7\ \text{A/m}.
> $$
> $\mathbf{E}\times\mathbf{H}\propto(-\hat x)\times(-\hat y) = +\hat z$ ✓. With $\hat n$ into the gap:
>
> | plate | $\rho_s = \hat n\cdot\epsilon\mathbf{E}$ | $\mathbf{J}_s = \hat n\times\mathbf{H}$ |
> |---|---|---|
> | $x = 0$, $\hat n = \hat x$ | $-424$ nC/m² | $-63.7\,\hat z$ A/m |
> | $x = d$, $\hat n = -\hat x$ | $+424$ nC/m² | $+63.7\,\hat z$ A/m |
>
> The positive plate carries 1.91 A away from the battery; the negative plate brings it back.
>
> **(c)** *Charge.* Plate 2 holds $\epsilon E_xW = \mathcal{C}V$ per metre behind the front and nothing ahead. Its charge between a point $z_1$ behind the front and the front grows at $\mathcal{C}V\,v$, fed only by $I(z_1)$: $I = \mathcal{C}vV$.
>
> *Faraday.* Loop: up the gap at $z_1$ ($+\hat x$), along $x = d$ past the front, down, back along $x = 0$; normal $\hat x\times\hat z = -\hat y$. Only the side at $z_1$ has tangential $\mathbf{E}$, so $\oint\mathbf{E}\cdot d\mathbf{l} = V$. The flux $\Psi = -\mu_0H_yd\times(\text{field length})$ changes at $-\mu_0H_yd\,v = -\mathcal{L}vI$, so $V = -d\Psi/dt = \mathcal{L}vI$.
>
> Divide, then multiply, the two results:
> $$
> \Big(\frac VI\Big)^2 = \frac{\mathcal{L}}{\mathcal{C}}\ \Rightarrow\ Z_0 = \sqrt{\frac{\mathcal{L}}{\mathcal{C}}},\qquad \mathcal{L}\mathcal{C}v^2 = 1\ \Rightarrow\ v = \frac{1}{\sqrt{\mathcal{L}\mathcal{C}}}.
> $$
> Numbers: $\mathcal{C}v = 0.159$ S gives $I = 0.159\cdot(-12) = -1.91$ A ✓; $\mathcal{L}v = 6.28\ \Omega$ ✓.
>
> **Check:** the battery supplies $VI = 22.9$ W; the line stores $\tfrac12\mathcal{C}V^2+\tfrac12\mathcal{L}I^2 = 76.4+76.4$ nJ/m, and times $v$ that is 22.9 W ✓. An FDTD run of the telegrapher's equations puts the arrival at 200.0 ns with $V = -12$ V, $I = -1.910$ A behind the front.
>
> **Answer.** (a) $v = 1.5\times10^8$ m/s, $\epsilon_r = 4$, $\mathcal{L} = 41.9$ nH/m, $\mathcal{C} = 1.06$ nF/m, $Z_0 = 2\pi = 6.28\ \Omega$; (b) $V = -12$ V, $I = -1.91$ A, $\mathbf{E} = -\hat x\,12$ kV/m, $\mathbf{H} = -\hat y\,63.7$ A/m; $\rho_s = -424$ nC/m², $\mathbf{J}_s = -63.7\,\hat z$ A/m at $x = 0$ and $+424$ nC/m², $+63.7\,\hat z$ A/m at $x = d$; (c) $Z_0 = \sqrt{\mathcal{L}/\mathcal{C}}$, $v = 1/\sqrt{\mathcal{L}\mathcal{C}}$.

### 27.12 Telegrapher's equations for a leaky coax

> [!hard] Hard · telegrapher's equations · coax · conductance
> A coax (radii $a<b$) is filled with a medium of $\mu_0$, $\epsilon$ and small conductivity $\sigma$. Its TEM fields are
> $$
> \mathbf{E} = \hat r\,\frac{V(z,t)}{r\ln(b/a)},\qquad \mathbf{H} = \hat\phi\,\frac{I(z,t)}{2\pi r}.
> $$
> (a) Show that $V = \int_a^bE_r\,dr$ and that $I$ is the $+z$ current on the inner conductor.
>
> (b) Show that Faraday's and Ampère's laws reduce to $-\partial V/\partial z = \mathcal{L}\,\partial I/\partial t$ and $-\partial I/\partial z = \mathcal{C}\,\partial V/\partial t+\mathcal{G}V$. Identify $\mathcal{L}$, $\mathcal{C}$, $\mathcal{G}$; find $\mathcal{L}\mathcal{C}$ and $\mathcal{G}/\mathcal{C}$.
>
> (c) Evaluate them, $v$ and $Z_0$ for $b/a = e$, $\epsilon_r = 2.25$, $\sigma = 10^{-5}$ S/m (ignore $\mathcal{G}$ for $v$ and $Z_0$). Use $\epsilon_0 = 10^{-9}/36\pi$ F/m.
>
> (d) For sinusoidal $V$, at what frequency does the leakage current equal the capacitive current? Is $\mathcal{G}$ negligible at 10 MHz?
>
> *Source: course notes, Lecture 27 derivation, recast for a coax.*

> [!hint]- Hint
> In cylindrical coordinates $(\nabla\times\mathbf{E})_\phi = \partial E_r/\partial z-\partial E_z/\partial r$ and $(\nabla\times\mathbf{H})_r = \tfrac1r\,\partial H_z/\partial\phi-\partial H_\phi/\partial z$. Every term carries the same $1/r$.

> [!solution]- Solution
> **(a)** $\displaystyle\int_a^b\frac{V\,dr}{r\ln(b/a)} = V$. On the inner surface $\hat n = \hat r$: $\mathbf{J}_s = \hat r\times\hat\phi\,\dfrac{I}{2\pi a} = \hat z\,\dfrac{I}{2\pi a}$, totalling $I$ around the circumference.
>
> **(b)** Faraday, $\phi$ component ($E_z = 0$):
> $$
> \frac{\partial E_r}{\partial z} = -\mu_0\frac{\partial H_\phi}{\partial t}\ \Rightarrow\ \frac{1}{r\ln(b/a)}\frac{\partial V}{\partial z} = -\frac{\mu_0}{2\pi r}\frac{\partial I}{\partial t}\ \Rightarrow\ -\frac{\partial V}{\partial z} = \frac{\mu_0\ln(b/a)}{2\pi}\frac{\partial I}{\partial t}.
> $$
> Ampère–Maxwell, $r$ component ($H_z = 0$):
> $$
> -\frac{\partial H_\phi}{\partial z} = \sigma E_r+\epsilon\frac{\partial E_r}{\partial t}\ \Rightarrow\ -\frac{\partial I}{\partial z} = \frac{2\pi\epsilon}{\ln(b/a)}\frac{\partial V}{\partial t}+\frac{2\pi\sigma}{\ln(b/a)}V.
> $$
> The $1/r$ cancels in both: keeping the static cross-section shape is what lets the TEM wave travel. The remaining components vanish identically ($E_z = H_z = 0$, $\partial(rH_\phi)/\partial r = 0$). So
> $$
> \begin{gathered}
> \mathcal{L} = \frac{\mu_0\ln(b/a)}{2\pi},\qquad \mathcal{C} = \frac{2\pi\epsilon}{\ln(b/a)},\qquad \mathcal{G} = \frac{2\pi\sigma}{\ln(b/a)},\\[4pt]
> \mathcal{L}\mathcal{C} = \mu_0\epsilon,\qquad \frac{\mathcal{G}}{\mathcal{C}} = \frac{\sigma}{\epsilon}.
> \end{gathered}
> $$
> **(c)** $\ln(b/a) = 1$: $\mathcal{L} = 200$ nH/m, $\mathcal{C} = 2\pi\cdot2.25\epsilon_0 = 125$ pF/m, $\mathcal{G} = 2\pi\times10^{-5} = 62.8\ \mu$S/m, $v = 2\times10^8$ m/s, $Z_0 = 40\ \Omega$.
>
> **(d)** Amplitudes $\mathcal{G}V$ and $\omega\mathcal{C}V$ are equal when $\omega = \mathcal{G}/\mathcal{C} = \sigma/\epsilon$, the loss-tangent crossover of [[3-maxwell-and-waves/23-imperfect-dielectrics-and-good-conductors|Lecture 23]]:
> $$
> f = \frac{\sigma}{2\pi\epsilon} = \frac{10^{-5}}{1.25\times10^{-10}} = 80\ \text{kHz}.
> $$
> At 10 MHz the ratio is $\sigma/\omega\epsilon = 0.008$: the leakage current is 0.8 % of the capacitive one, negligible.
>
> **Check:** finite-difference curls of the full 3-D fields, built from an exact lossy-line wave at 50 kHz, satisfy both Maxwell curl equations to a relative $10^{-5}$.
>
> **Answer.** (b) $\mathcal{L} = \mu_0\ln(b/a)/2\pi$, $\mathcal{C} = 2\pi\epsilon/\ln(b/a)$, $\mathcal{G} = 2\pi\sigma/\ln(b/a)$, $\mathcal{L}\mathcal{C} = \mu_0\epsilon$, $\mathcal{G}/\mathcal{C} = \sigma/\epsilon$; (c) $\mathcal{L} = 200$ nH/m, $\mathcal{C} = 125$ pF/m, $\mathcal{G} = 62.8\ \mu$S/m, $v = 2\times10^8$ m/s, $Z_0 = 40\ \Omega$; (d) 80 kHz; at 10 MHz $\mathcal{G}$ is negligible (0.8 %).

### Sources for this page
Course notes, Lecture 27: the plate derivation (recast for a coax with leakage in 27.12), the ladder model (27.8, new numbers) and the battery example (27.11, extended with a reversed battery, plate charges and currents, and the charge and Faraday arguments at the front). Old exams, all re-parameterized: SP18 Exam 3 #1(ii) and #1(v) (27.2, new statements as true/false); SP17 Exam 3 #2(ii) (27.3, plates moved to $y = 0$ and $y = d$); FA23 Exam 3 #4(d) (27.7, the filling from a delay, plus a capacitance-meter reading and leakage); SP19 Exam 3 #2 (27.9, recast for a coax with the current on the outer conductor, the Poynting integral and a field-phasor part). Original: 27.1, 27.4–27.6, 27.10.

*Back to [[4-transmission-lines/27-guided-tem-waves-on-transmission-lines|Lecture 27]] · [[practice/index|all practice]]*

*Previous: [[practice/26-standing-waves-and-radiation-pressure|Lecture 26 practice]] · next: [[practice/28-bounce-diagrams|Lecture 28 practice]] · [[practice/index|all practice]]*
