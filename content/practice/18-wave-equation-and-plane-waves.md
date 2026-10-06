---
title: "Practice — Lecture 18: The wave equation and plane TEM waves"
description: "12 practice problems (5 easy, 3 medium, 4 hard) on the source-free wave equation and what its derivation needs, reading direction and speed from a wave's argument, H from E with the E × H rule along every axis, v and η in dielectric and magnetic media, the cable link 1/√(LC) = v, moving pulses (records, snapshots and the mirror) and counter-propagating pulses, each with a folded hint and a worked solution."
tags: [practice, waves]
lecture: 18
---

*Practice for [[3-maxwell-and-waves/18-the-wave-equation-and-plane-tem-waves|Lecture 18]] · concepts: [[concepts/wave-equation]] · [[concepts/plane-waves]] · [[concepts/intrinsic-impedance]] · [[concepts/displacement-current]] · all practice: [[practice/index|hub]] · by difficulty: [[practice/easy|easy]] · [[practice/medium|medium]] · [[practice/hard|hard]] · [[practice/topics|by topic]]*

Work each problem on paper first. Open the **hint** only when stuck, and the **solution** only after you have an answer you would hand in. Every answer here has been checked numerically.

## Easy

### 18.1 Which way and how fast

> [!easy] Easy · multiple choice · plane waves
> Three travelling waveforms are given, with positions in metres and time in seconds ($u$ is the unit step):
> $$
> p = 5\cos\big(2\pi\times10^{8}\,t + 0.8\pi x\big),\qquad q = u\big(0.004z - t\big),\qquad r = e^{-(t + 0.0125y)^2}.
> $$
> Which line gives their velocities, in m/s, in the order $p$, $q$, $r$?
>
> (a) $+2.5\times10^{8}\,\hat{x}$, $\ +250\,\hat{z}$, $\ -80\,\hat{y}$
>
> (b) $-2.5\times10^{8}\,\hat{x}$, $\ -250\,\hat{z}$, $\ -80\,\hat{y}$
>
> (c) $-2.5\times10^{8}\,\hat{x}$, $\ +250\,\hat{z}$, $\ -80\,\hat{y}$
>
> (d) $-2.5\times10^{8}\,\hat{x}$, $\ +0.004\,\hat{z}$, $\ -0.0125\,\hat{y}$
>
> (e) $-2.5\times10^{8}\,\hat{x}$, $\ +250\,\hat{z}$, $\ +80\,\hat{y}$
>
> *Source: Lecture 18 slides, the velocity challenge (slide 24), with new waveforms, axes and traps.*

> [!hint]- Hint
> Rewrite each argument as a multiple of $t\mp(\text{position})/v$. Opposite signs on the $t$ term and the position term mean travel toward $+$ that axis; equal signs mean $-$. An overall minus sign changes nothing.

> [!solution]- Solution
> A function of $t - \hat u\cdot\mathbf{r}/v$ slides rigidly along $+\hat u$ at speed $v$, so factor out the coefficient of $t$:
> - $p$: $2\pi\times10^{8}t + 0.8\pi x = 2\pi\times10^{8}\big(t + x/(2.5\times10^{8})\big)$. Same signs, so toward $-x$ at $2.5\times10^{8}$ m/s. The crest that is at $x = 0$ at $t = 0$ is at $x = -0.25$ m at $t = 1$ ns.
> - $q$: $0.004z - t = -(t - z/250)$. The overall minus sign does not matter: $q$ is a function of $t - z/250$, so it travels toward $+z$ at 250 m/s. Check: the step's edge sits where $0.004z = t$, i.e. at $z = 250t$, which is $z = 0$, 250 m and 500 m at $t = 0$, 1 s and 2 s.
> - $r$: $t + 0.0125y = t + y/80$. Same signs, so toward $-y$ at 80 m/s; the peak sits at $y = -80t$.
>
> Why the other options fail: (a) reads the "$+$" in $p$ as travel toward $+x$, but a plus *between* the $t$ and position terms means the negative direction. (b) is the term-order trap: $q$ starts with the position term, so its "$-t$" looks like a $-z$ wave, but only the *relative* sign counts. (d) quotes 0.004 and 0.0125 s/m, which are the *slownesses* $1/v$, as if they were speeds. (e) flips the direction of $r$.
>
> **Watch out:** $p$ travels at $2.5\times10^{8}$ m/s, slower than $c$, so it is a wave in matter: in a non-magnetic medium $\epsilon_r = (c/v)^2\approx1.44$.
>
> **Answer.** (c): $p$ travels toward $-x$ at $2.5\times10^{8}$ m/s, $q$ toward $+z$ at 250 m/s, $r$ toward $-y$ at 80 m/s.

### 18.2 The partner field

> [!easy] Easy · plane waves · intrinsic impedance
> Each wave below travels in free space. Find the missing field (as a vector, with its amplitude) and the amplitude of $\mathbf{B}$. Use $\eta_0 = 376.7\ \Omega$ and $c = 3.00\times10^{8}$ m/s; $\omega$ and $\tau$ are constants.
>
> (a) $\mathbf{E} = 6\cos\big(\omega(t - z/c)\big)\,\hat{y}$ V/m. Find $\mathbf{H}$.
>
> (b) $\mathbf{E} = 3\,e^{-[(t + y/c)/\tau]^2}\,\hat{x}$ V/m. Find $\mathbf{H}$.
>
> (c) $\mathbf{H} = 50\cos\big(\omega(t - x/c)\big)\,\hat{z}$ mA/m. Find $\mathbf{E}$.
>
> *Source: original (the Lecture 18 notes' E–H rules, applied along three different axes).*

> [!hint]- Hint
> Read the direction of travel $\hat u$ off the argument, then use $\mathbf{H} = \hat u\times\mathbf{E}/\eta_0$ or, the other way round, $\mathbf{E} = \eta_0\,\mathbf{H}\times\hat u$. Write each cross product out. For the magnetic flux density, $\lvert\mathbf{B}\rvert = \mu_0\lvert\mathbf{H}\rvert = \lvert\mathbf{E}\rvert/c$.

> [!solution]- Solution
> In every case $\mathbf{H}$ is $\mathbf{E}$ divided by $\eta_0$ and turned by 90° so that $\mathbf{E}\times\mathbf{H}$ points along the travel.
>
> **(a)** The argument is $t - z/c$, so the wave travels toward $+z$ and $\hat u = \hat{z}$. Since $\hat{z}\times\hat{y} = -\hat{x}$,
> $$
> \mathbf{H} = -\frac{6\ \text{V/m}}{376.7\ \Omega}\cos\big(\omega(t - z/c)\big)\,\hat{x} = -15.9\cos\big(\omega(t - z/c)\big)\,\hat{x}\ \text{mA/m}.
> $$
> Check: $\hat{y}\times(-\hat{x}) = +\hat{z}$ ✓. $B = 6/c = 20.0$ nT.
>
> **(b)** The argument is $t + y/c$: toward $-y$, $\hat u = -\hat{y}$. Then $(-\hat{y})\times\hat{x} = -(\hat{y}\times\hat{x}) = +\hat{z}$, so $\mathbf{H} = +7.96\,e^{-[(t + y/c)/\tau]^2}\,\hat{z}$ mA/m. Check: $\hat{x}\times\hat{z} = -\hat{y}$ ✓. $B = 3/c = 10.0$ nT.
>
> **(c)** The argument is $t - x/c$: toward $+x$. Since $\hat{z}\times\hat{x} = +\hat{y}$,
> $$
> \mathbf{E} = \eta_0\,\mathbf{H}\times\hat u = 376.7\times0.05\cos\big(\omega(t - x/c)\big)\,\hat{y} = 18.8\cos\big(\omega(t - x/c)\big)\,\hat{y}\ \text{V/m}.
> $$
> Check: $\hat{y}\times\hat{z} = +\hat{x}$ ✓, and $\hat u\times\mathbf{E}/\eta_0$ points along $\hat{x}\times\hat{y} = \hat{z}$, giving back $\mathbf{H}$. $B = \mu_0H = 62.8$ nT, the same as $E/c$.
>
> **Watch out:** in (a) $\mathbf{E}$ is along $\hat{y}$, so for travel toward $+z$ the field $\mathbf{H}$ is along $-\hat{x}$, not $+\hat{x}$. The $x$-polarized pattern ($\hat{x}$ goes with $+\hat{y}$) does not carry over by swapping letters.
>
> **Answer.** (a) $\mathbf{H} = -15.9\cos\big(\omega(t - z/c)\big)\,\hat{x}$ mA/m, $B = 20.0$ nT; (b) $\mathbf{H} = +7.96\,e^{-[(t + y/c)/\tau]^2}\,\hat{z}$ mA/m, $B = 10.0$ nT; (c) $\mathbf{E} = 18.8\cos\big(\omega(t - x/c)\big)\,\hat{y}$ V/m, $B = 62.8$ nT.

### 18.3 Phase rate and snapshot period

> [!easy] Easy · plane waves · intrinsic impedance
> A plane wave $\mathbf{E} = 12\cos(\omega t - \beta x)\,\hat{y}$ V/m travels through a lossless, non-magnetic dielectric. A probe at a fixed point sees the argument of the cosine grow by $6\pi$ rad every 10 ns. A snapshot of the field at one instant repeats itself every 0.4 m along $x$ (this spatial period is called the **wavelength**).
>
> (a) Find $\omega$, $\beta$, the speed and direction of travel, and $\epsilon_r$.
>
> (b) Find $\eta$, $\mathbf{H}$ as a function of $x$ and $t$, and the amplitude of $\mathbf{B}$.
>
> *Source: SP18 Exam 2 #1(vii) style, re-parameterized (a dielectric instead of vacuum, and the speed, medium and fields asked instead of the wavelength).*

> [!hint]- Hint
> At a fixed $x$ the argument grows at the rate $\omega$; at a fixed $t$ it repeats when $\beta x$ grows by $2\pi$. Then $v = \omega/\beta$, $\epsilon_r = (c/v)^2$ and $\eta = \mu_0v$.

> [!solution]- Solution
> **(a)** At a fixed $x$ the argument changes only through $\omega t$, so $\omega = 6\pi/(10\ \text{ns}) = 6\pi\times10^{8}$ rad/s $= 1.885\times10^{9}$ rad/s. A snapshot repeats when $\beta\times(0.4\ \text{m}) = 2\pi$, so $\beta = 5\pi$ rad/m $= 15.7$ rad/m. Then
> $$
> \omega t - \beta x = \omega\Big(t - \frac{x}{\omega/\beta}\Big),\qquad v = \frac{\omega}{\beta} = \frac{6\pi\times10^{8}}{5\pi} = 1.2\times10^{8}\ \text{m/s},
> $$
> toward $+x$ (opposite signs). Equivalently, the pattern moves one spatial period, 0.4 m, in one temporal period, $2\pi/\omega = 3.33$ ns. The medium is non-magnetic, so $\epsilon_r = (c/v)^2 = (2.998/1.2)^2 = 6.24$ (6.25 with $c = 3\times10^{8}$ m/s).
>
> **(b)** $\eta = \sqrt{\mu_0/\epsilon} = \mu_0v = 4\pi\times10^{-7}\times1.2\times10^{8} = 48\pi\approx150.8\ \Omega$. Direction: $\hat u\times\mathbf{E}$ is along $\hat{x}\times\hat{y} = +\hat{z}$, so
> $$
> \mathbf{H} = \frac{12\ \text{V/m}}{150.8\ \Omega}\cos(6\pi\times10^{8}t - 5\pi x)\,\hat{z} = 79.6\cos(6\pi\times10^{8}t - 5\pi x)\,\hat{z}\ \text{mA/m}.
> $$
> Check: $\mathbf{E}\times\mathbf{H}$ is along $\hat{y}\times\hat{z} = +\hat{x}$ ✓. $B = E/v = 12/(1.2\times10^{8}) = 100$ nT, the same as $\mu_0H$.
>
> **Watch out:** $\eta_0\approx377\ \Omega$ belongs to vacuum. In this dielectric $H$ is $\sqrt{\epsilon_r}\approx2.5$ times larger than $12/377$ A/m.
>
> **Answer.** (a) $\omega = 6\pi\times10^{8}$ rad/s, $\beta = 5\pi$ rad/m, $v = 1.2\times10^{8}$ m/s toward $+x$, $\epsilon_r\approx6.24$; (b) $\eta = 48\pi\approx151\ \Omega$, $\mathbf{H} = 79.6\cos(6\pi\times10^{8}t - 5\pi x)\,\hat{z}$ mA/m, $B = 100$ nT.

### 18.4 What the derivation needs

> [!easy] Easy · true or false · wave equation · displacement current
> The wave equation $\nabla^2\mathbf{E} = \mu\epsilon\,\partial^2\mathbf{E}/\partial t^2$ comes from taking the curl of Faraday's law and using the Ampère–Maxwell law. True or false?
>
> (a) Without the displacement current $\partial\mathbf{D}/\partial t$, the same steps would give $\nabla^2\mathbf{E} = 0$ in a source-free region, and there would be no travelling waves.
>
> (b) In a region with a fixed, non-uniform free charge density $\rho(\mathbf{r})$ (but $\mathbf{J} = 0$ and constant $\mu$, $\epsilon$), the same steps still give $\nabla^2\mathbf{E} = \mu\epsilon\,\partial^2\mathbf{E}/\partial t^2$.
>
> (c) In a charge-free region where $\epsilon$ varies with position, $\nabla\cdot\mathbf{E} = 0$ still holds, because Gauss's law gives $\nabla\cdot\mathbf{D} = 0$.
>
> (d) $\mathbf{E} = E_0\cos\big(\omega(t - z/v)\big)\,\hat{z}$ satisfies the 1D wave equation, so it is a possible wave in a source-free region.
>
> *Source: original (the assumptions of the Lecture 18 derivation, and the notes' question on z-polarized waves).*

> [!hint]- Hint
> Write the chain out: $\nabla\times(\nabla\times\mathbf{E}) = \nabla(\nabla\cdot\mathbf{E}) - \nabla^2\mathbf{E}$ on the left, $-\mu\,\partial(\nabla\times\mathbf{H})/\partial t$ on the right. For each statement, ask which term changes.

> [!solution]- Solution
> **(a) True.** The right-hand side of the curl-curl step is $-\mu\,\partial(\nabla\times\mathbf{H})/\partial t$. With $\nabla\times\mathbf{H} = \mathbf{J} = 0$ it vanishes, leaving $\nabla^2\mathbf{E} = 0$, Laplace's equation. A travelling wave such as $\cos\big(\omega(t - z/v)\big)\,\hat{x}$ has $\nabla^2E_x = -(\omega/v)^2E_x\neq0$, so it could not exist. The displacement current is the term that makes light.
>
> **(b) False.** Now $\nabla\cdot\mathbf{E} = \rho/\epsilon$, so the term $\nabla(\nabla\cdot\mathbf{E})$ no longer drops out:
> $$
> \nabla^2\mathbf{E} = \mu\epsilon\frac{\partial^2\mathbf{E}}{\partial t^2} + \frac{\nabla\rho}{\epsilon}.
> $$
> Example: $\rho = \rho_0x/a$ comes with the static field $E_x = \rho_0x^2/(2\epsilon a)$, which has $\nabla^2\mathbf{E} = (\rho_0/\epsilon a)\,\hat{x}\neq0$ and no time dependence at all. Only a uniform $\rho$, with $\nabla\rho = 0$, would leave the equation intact.
>
> **(c) False.** $\nabla\cdot(\epsilon\mathbf{E}) = \epsilon\nabla\cdot\mathbf{E} + \mathbf{E}\cdot\nabla\epsilon = 0$ gives $\nabla\cdot\mathbf{E} = -\mathbf{E}\cdot\nabla\epsilon/\epsilon$, which is non-zero wherever $\mathbf{E}$ has a component along $\nabla\epsilon$. Example: with $\epsilon = \epsilon_0(1 + x/a)$, the field $\mathbf{E} = E_0\hat{x}/(1 + x/a)$ has $\nabla\cdot\mathbf{D} = 0$ but $\nabla\cdot\mathbf{E} = -E_0/a$ at $x = 0$. That is why the derivation needs a homogeneous medium.
>
> **(d) False.** It does solve the 1D wave equation, but it fails Gauss's law with $\rho = 0$:
> $$
> \nabla\cdot\mathbf{E} = \frac{\partial E_z}{\partial z} = \frac{\omega E_0}{v}\sin\Big(\omega\Big(t - \frac zv\Big)\Big)\neq0 .
> $$
> Its curl is also zero, so Faraday's law gives it no $\mathbf{H}$ partner. The wave equation is necessary, not sufficient: a plane wave has no field component along its direction of travel.
>
> **Answer.** (a) True; (b) false, an extra term $\nabla\rho/\epsilon$ appears; (c) false, $\nabla\cdot\mathbf{E} = -\mathbf{E}\cdot\nabla\epsilon/\epsilon$; (d) false, $\nabla\cdot\mathbf{E}\neq0$.

### 18.5 The backwards magnetic field

> [!easy] Easy · find the error · plane waves · intrinsic impedance
> In a lossless non-magnetic dielectric, $\mathbf{E} = 12\cos(1.5\pi\times10^{8}\,t + 2\pi x)\,\hat{z}$ V/m. A student finds $\mathbf{H}$:
>
> "The $t$ and $x$ terms have the same sign, so the wave travels toward $-x$, $\hat u = -\hat{x}$, at $v = 1.5\pi\times10^{8}/2\pi = 7.5\times10^{7}$ m/s. Then $\epsilon_r = (c/v)^2 = 16$ and $\eta = \eta_0/4 = 94.2\ \Omega$, so $H = 12/94.2 = 0.127$ A/m. Direction: $\mathbf{H} = \mathbf{E}\times\hat u/\eta$, and $\hat{z}\times(-\hat{x}) = -\hat{y}$. So $\mathbf{H} = -0.127\cos(1.5\pi\times10^{8}\,t + 2\pi x)\,\hat{y}$ A/m."
>
> Find the slip, correct it, and give $\mathbf{H}$.
>
> *Source: original.*

> [!hint]- Hint
> Test the student's answer against the rule it must satisfy: does $\mathbf{E}\times\mathbf{H}$ point toward $-x$?

> [!solution]- Solution
> **The slip:** the order of the cross product. The rule is $\mathbf{H} = \hat u\times\mathbf{E}/\eta$, and $\mathbf{E}\times\hat u$ is its negative. Everything else (the direction of travel, $v$, $\epsilon_r$, $\eta$ and the magnitude) is right.
>
> **Fix:** $(-\hat{x})\times\hat{z} = -(\hat{x}\times\hat{z}) = -(-\hat{y}) = +\hat{y}$, so
> $$
> \mathbf{H} = +0.127\cos(1.5\pi\times10^{8}\,t + 2\pi x)\,\hat{y}\ \text{A/m}.
> $$
> **Check:** $\mathbf{E}\times\mathbf{H}$ is along $\hat{z}\times\hat{y} = -\hat{x}$, the direction of travel ✓. The student's field gives $\hat{z}\times(-\hat{y}) = +\hat{x}$, a wave going the other way, and it fails Faraday's law ($\partial E_z/\partial x = \mu_0\,\partial H_y/\partial t$ for this geometry) by a sign. Small print: $\eta = \mu_0v = 30\pi = 94.2\ \Omega$ exactly; $\eta_0/4$ agrees because $\epsilon_r = 15.98\approx16$.
>
> **Answer.** The student computed $\mathbf{E}\times\hat u$ instead of $\hat u\times\mathbf{E}$. Correct: $\mathbf{H} = +0.127\cos(1.5\pi\times10^{8}\,t + 2\pi x)\,\hat{y}$ A/m (amplitude 127 mA/m), with $\mathbf{E}\times\mathbf{H}$ along $-\hat{x}$.

## Medium

### 18.6 Which fields can be waves

> [!medium] Medium · wave equation · superposition
> A lossless medium with $\mu = \mu_0$ has $\mu\epsilon = 1.0\times10^{-16}$ s²/m² (so $\epsilon_r\approx9$). Four fields $\mathbf{E} = E_x(z,t)\,\hat{x}$ are proposed, in V/m with $z$ in metres and $t$ in seconds:
> $$
> \begin{aligned}
> E_1 &= 4\cos(2\times10^{8}t - 2z), & E_2 &= 4\cos(2\times10^{8}t)\cos(2z),\\
> E_3 &= 4\cos(2\times10^{8}t - 6z), & E_4 &= 4\cos(2\times10^{8}t - 2z)\cos(2\times10^{8}t + 2z).
> \end{aligned}
> $$
> (a) Which of them satisfy the 1D wave equation in this medium? For those that do, give $v$.
>
> (b) For $E_2$, find $\mathbf{H}$ from Faraday's law, and check that the pair satisfies the Ampère–Maxwell law.
>
> (c) Write $E_2$ as the sum of two travelling waves, and confirm your $\mathbf{H}$ with $H_y = (Af - Bg)/\eta$.
>
> (d) At what instant is $E_2$ zero everywhere? What is $\mathbf{H}$ then?
>
> *Source: original.*

> [!hint]- Hint
> For each candidate compute $\partial^2E/\partial z^2$ and $\mu\epsilon\,\partial^2E/\partial t^2$ and compare them at every $(z,t)$, signs included. For (b), the $y$ component of Faraday's law reads $\partial E_x/\partial z = -\mu_0\,\partial H_y/\partial t$; integrate in time.

> [!solution]- Solution
> **Setup.** Here $v = 1/\sqrt{\mu\epsilon} = 10^{8}$ m/s and $\eta = \mu_0v = 40\pi\approx125.7\ \Omega$. A candidate passes only if $\partial^2E/\partial z^2 = \mu\epsilon\,\partial^2E/\partial t^2$ at every point.
>
> **(a)**
> - $E_1$: $\partial^2E_1/\partial z^2 = -4E_1$ and $\mu\epsilon\,\partial^2E_1/\partial t^2 = -10^{-16}(4\times10^{16})E_1 = -4E_1$ ✓. It travels toward $+z$ at $2\times10^{8}/2 = 10^{8}$ m/s.
> - $E_2$: again $-4E_2$ on both sides ✓, with $v = 10^{8}$ m/s. A product of a function of $t$ and a function of $z$ can solve the equation, provided the ratio of the two coefficients, $\omega/\beta$, equals $v$.
> - $E_3$: $\partial^2E_3/\partial z^2 = -36E_3$ but $\mu\epsilon\,\partial^2E_3/\partial t^2 = -4E_3$ ✗. It is a travelling wave, but at $3.33\times10^{7}$ m/s, which would need $\mu\epsilon$ nine times larger ($\epsilon_r\approx81$). Wrong medium.
> - $E_4$: a product of two travelling waves is not their sum. Expanding, $E_4 = 2\cos(4z) + 2\cos(4\times10^{8}t)$, so $\partial^2E_4/\partial z^2 = -32\cos(4z)$ while $\mu\epsilon\,\partial^2E_4/\partial t^2 = -32\cos(4\times10^{8}t)$. These differ: at $z = 0$, $t = 7.85$ ns they are $-32$ and $+32$ V/m³ ✗.
>
> **(b)** With $\omega = 2\times10^{8}$ rad/s and $\beta = 2$ rad/m, Faraday's law gives
> $$
> \frac{\partial E_x}{\partial z} = -4\beta\cos\omega t\,\sin\beta z = -\mu_0\frac{\partial H_y}{\partial t}\quad\Rightarrow\quad H_y = \frac{4\beta}{\mu_0\omega}\sin\omega t\,\sin\beta z = \frac{4}{\eta}\sin\omega t\,\sin\beta z ,
> $$
> since $\mu_0\omega/\beta = \mu_0v = \eta$ (the constant of integration would be a static field, and is dropped). So $\mathbf{H} = 31.8\sin(2\times10^{8}t)\sin(2z)\,\hat{y}$ mA/m. Ampère–Maxwell, $x$ component: $-\partial H_y/\partial z = -(4\beta/\eta)\sin\omega t\cos\beta z$ and $\epsilon\,\partial E_x/\partial t = -4\epsilon\omega\sin\omega t\cos\beta z$. They agree because $\beta/\eta = \omega\sqrt{\mu_0\epsilon}\big/\sqrt{\mu_0/\epsilon} = \epsilon\omega$ ✓.
>
> **(c)** $\cos a\cos b = \tfrac12[\cos(a-b) + \cos(a+b)]$ gives $E_2 = 2\cos(\omega t - \beta z) + 2\cos(\omega t + \beta z)$: two equal waves of 2 V/m, one toward $+z$ ($Af$) and one toward $-z$ ($Bg$). Then
> $$
> H_y = \frac{1}{\eta}\big[2\cos(\omega t - \beta z) - 2\cos(\omega t + \beta z)\big] = \frac{4}{\eta}\sin\omega t\,\sin\beta z\qquad\checkmark
> $$
> The electric fields add; the magnetic fields subtract, because the $-z$ wave's $\mathbf{H}$ is reversed relative to its $\mathbf{E}$.
>
> **(d)** $E_2 = 0$ at every $z$ when $\cos\omega t = 0$, first at $t = \pi/(2\omega) = 7.85$ ns. Then $\sin\omega t = 1$ and $\mathbf{H} = 31.8\sin(2z)\,\hat{y}$ mA/m, largest at $z = \pi/4 = 0.785$ m: for that instant the field is entirely magnetic. A quarter period later $\mathbf{H}$ vanishes everywhere and $\mathbf{E}$ is back.
>
> **Check:** for a single travelling wave $E_x/H_y = \pm\eta$. Here $E_x/H_y = \eta\cot\omega t\cot\beta z$ takes every value, as it should when two waves overlap.
>
> **Answer.** (a) $E_1$ and $E_2$, with $v = 10^{8}$ m/s ($E_1$ travels toward $+z$; $E_2$ is two waves); not $E_3$ (it travels at $3.33\times10^{7}$ m/s, wrong for this medium) and not $E_4$. (b) $\mathbf{H} = (4/\eta)\sin\omega t\,\sin\beta z\,\hat{y} = 31.8\sin(2\times10^{8}t)\sin(2z)\,\hat{y}$ mA/m. (c) $E_2 = 2\cos(\omega t - \beta z) + 2\cos(\omega t + \beta z)$ and $H_y = (2/\eta)[\cos(\omega t - \beta z) - \cos(\omega t + \beta z)]$. (d) At $t = 7.85$ ns, when $\mathbf{H} = 31.8\sin(2z)\,\hat{y}$ mA/m.

### 18.7 A cable and its filling

> [!medium] Medium · LC product · intrinsic impedance
> A strip line is made of two copper strips $W = 8$ mm wide and $d = 1$ mm apart, with a non-magnetic dielectric between them (ignore fringing). A short pulse launched at one end of a 3.0 m length arrives at the other end 18 ns later. Take $c = 3\times10^{8}$ m/s.
>
> (a) Find the signal speed $v$, and the permittivity $\epsilon_r$ and intrinsic impedance $\eta$ of the filling.
>
> (b) Find $\mathcal{L}$ and $\mathcal{C}$ from Lectures 10 and 15, and check that $1/\sqrt{\mathcal{L}\mathcal{C}} = v$.
>
> (c) Show that $\sqrt{\mathcal{L}/\mathcal{C}}$ is $\eta$ times a geometric factor, and evaluate it.
>
> (d) A coax filled with the same dielectric is to have the same $\sqrt{\mathcal{L}/\mathcal{C}}$. Find $b/a$, and the delay over the same 3.0 m.
>
> *Source: original (the Lecture 18 cable link, on a strip line and a matching coax).*

> [!hint]- Hint
> For parallel plates $\mathcal{C} = \epsilon W/d$ and $\mathcal{L} = \mu d/W$; for a coax $\mathcal{C} = 2\pi\epsilon/\ln(b/a)$ and $\mathcal{L} = (\mu/2\pi)\ln(b/a)$. In each pair the product does not depend on the geometry, and the ratio does.

> [!solution]- Solution
> **Setup.** The field between two conductors is a TEM wave guided by them, and it travels at the plane-wave speed of the filling. So the delay measures $\epsilon_r$, and the line parameters must reproduce that speed.
>
> **(a)** $v = 3.0\ \text{m}/18\ \text{ns} = 1.67\times10^{8}$ m/s. The filling is non-magnetic, so $\epsilon_r = (c/v)^2 = (3/1.667)^2 = 1.8^2 = 3.24$ and $\eta = \eta_0/\sqrt{\epsilon_r} = 120\pi/1.8 = 209\ \Omega$ (the same as $\mu_0v$).
>
> **(b)** With $\epsilon = 3.24\,\epsilon_0$,
> $$
> \mathcal{C} = \frac{\epsilon W}{d} = 3.24\times8.854\times10^{-12}\times8 = 229.5\ \text{pF/m},\qquad \mathcal{L} = \frac{\mu_0d}{W} = \frac{4\pi\times10^{-7}}{8} = 157.1\ \text{nH/m}.
> $$
> The product is $\mathcal{L}\mathcal{C} = \mu_0\epsilon\,(d/W)(W/d) = \mu\epsilon$, so $1/\sqrt{\mathcal{L}\mathcal{C}} = 1/\sqrt{\mu\epsilon} = 1.67\times10^{8}$ m/s $= v$ ✓.
>
> **(c)**
> $$
> \sqrt{\frac{\mathcal{L}}{\mathcal{C}}} = \sqrt{\frac{\mu d/W}{\epsilon W/d}} = \sqrt{\frac{\mu}{\epsilon}}\;\frac dW = \eta\,\frac dW = \frac{209\ \Omega}{8} = 26.2\ \Omega .
> $$
> Directly from (b): $\sqrt{157.1\times10^{-9}/229.5\times10^{-12}} = 26.2\ \Omega$ ✓.
>
> **(d)** For the coax $\sqrt{\mathcal{L}/\mathcal{C}} = (\eta/2\pi)\ln(b/a)$. Setting this equal to $\eta\,d/W$:
> $$
> \ln\frac ba = \frac{2\pi d}{W} = \frac\pi4 = 0.785,\qquad \frac ba = e^{\pi/4} = 2.19 .
> $$
> The delay is still 18 ns: $v$ depends only on the filling, not on the shape of the conductors. (This coax even has the same $\mathcal{L} = 157.1$ nH/m and $\mathcal{C} = 229.5$ pF/m as the strips.)
>
> **Check:** units, $\sqrt{(\text{H/m})/(\text{F/m})} = \sqrt{\text{H/F}} = \Omega$ ✓. Wider strips (larger $W$) lower $\sqrt{\mathcal{L}/\mathcal{C}}$ but leave $v$ alone, as the formulas say.
>
> **Answer.** (a) $v = 1.67\times10^{8}$ m/s, $\epsilon_r = 3.24$, $\eta\approx209\ \Omega$; (b) $\mathcal{C} = 229.5$ pF/m, $\mathcal{L} = 157.1$ nH/m, $1/\sqrt{\mathcal{L}\mathcal{C}} = 1.67\times10^{8}$ m/s; (c) $\sqrt{\mathcal{L}/\mathcal{C}} = \eta\,d/W = 26.2\ \Omega$; (d) $b/a = e^{\pi/4}\approx2.19$, delay 18 ns.

### 18.8 From probe record to snapshots

> [!medium] Medium · moving pulses · plane waves
> A plane wave travels toward $+x$ in free space ($c = 300$ m/μs, $\eta_0 = 120\pi\ \Omega$), with $\mathbf{E}$ along $\hat{z}$. A probe at $x = 0$ records
> $$
> E_z(0,t) = \begin{cases} 5\ \text{V/m}, & 0<t<1\ \mu\text{s},\\ -2\ \text{V/m}, & 1<t<3\ \mu\text{s},\\ 0 & \text{otherwise.}\end{cases}
> $$
> (a) Write $E_z(x,t)$ for all $x$ and $t$.
>
> (b) Sketch the snapshot $E_z(x,\,2\ \mu\text{s})$ and give its values. Is it the record mirrored or not, and why?
>
> (c) What does a probe at $x = 900$ m record?
>
> (d) Find $\mathbf{H}$ at $x = 450$ m and at $x = 0$, both at $t = 2$ μs, and $\lvert\mathbf{B}\rvert$ at those points.
>
> *Source: original (the shift identities of the Lecture 18 slides, slide 25, applied to a two-level record).*

> [!hint]- Hint
> For travel toward $+x$, $E_z(x,t) = E_z(0,\ t - x/c)$: a probe at $x$ sees what the probe at 0 saw $x/c$ earlier. Keep $x$ in metres and $t$ in microseconds, so that $x/c = x/300$.

> [!solution]- Solution
> **Setup.** Call the record $F(s)$. Travel toward $+x$ means the field depends on $x$ and $t$ only through $s = t - x/c$ (minus sign, plus direction).
>
> **(a)** $E_z(x,t) = F(t - x/300)$ with $x$ in m and $t$ in μs: 5 V/m where $0<t - x/300<1$, $-2$ V/m where $1<t - x/300<3$, and zero elsewhere.
>
> **(b)** At $t = 2$ μs, $s = 2 - x/300$:
> - $0<s<1$, i.e. $300<x<600$ m: $E_z = +5$ V/m;
> - $1<s<3$, i.e. $-300<x<300$ m: $E_z = -2$ V/m;
> - zero for $x<-300$ m and for $x>600$ m.
>
> The record shows $+5$ first (on the left of a time axis), then $-2$. The snapshot shows $-2$ on the left and $+5$ on the right: it is the record **mirrored**. The $+5$ part passed $x = 0$ first, so by now it has gone furthest toward $+x$: the front of a $+x$ wave is its right-hand end.
>
> **(c)** At $x = 900$ m, $s = t - 3$: the probe records 5 V/m for $3<t<4$ μs, then $-2$ V/m for $4<t<6$ μs, then zero. It is the same record, delayed by $900/300 = 3$ μs.
>
> **(d)** $\mathbf{H} = \hat u\times\mathbf{E}/\eta_0$ with $\hat u = \hat{x}$, and $\hat{x}\times\hat{z} = -\hat{y}$:
> - at $x = 450$ m ($s = 0.5$ μs), $E_z = +5$ V/m and $\mathbf{H} = -\hat{y}\,5/120\pi = -13.3\,\hat{y}$ mA/m; $B = 5/c = 16.7$ nT;
> - at $x = 0$ ($s = 2$ μs), $E_z = -2$ V/m and $\mathbf{H} = -\hat{y}\,(-2)/120\pi = +5.31\,\hat{y}$ mA/m; $B = 6.67$ nT.
>
> **Check:** at both points $\mathbf{E}\times\mathbf{H}$ points along $+\hat{x}$: $(5\hat{z})\times(-\hat{y}) = +5\hat{x}$ and $(-2\hat{z})\times(+\hat{y}) = +2\hat{x}$, each times $1/\eta_0$ ✓. When $\mathbf{E}$ reverses, $\mathbf{H}$ reverses with it, and the direction of travel stays the same.
>
> **Watch out:** drawing the snapshot as a copy of the record, with $+5$ on the left, is the classic error. Test one point: at $t = 2$ μs, $x = 450$ m has $s = 0.5$ μs, which lies in the $+5$ part of the record.
>
> **Answer.** (a) $E_z = F(t - x/300)$; (b) $-2$ V/m on $-300<x<300$ m and $+5$ V/m on $300<x<600$ m, the record mirrored; (c) 5 V/m for $3<t<4$ μs, then $-2$ V/m for $4<t<6$ μs; (d) $\mathbf{H} = -13.3\,\hat{y}$ mA/m ($B = 16.7$ nT) at 450 m, and $\mathbf{H} = +5.31\,\hat{y}$ mA/m ($B = 6.67$ nT) at $x = 0$.

## Hard

### 18.9 Triangle pulse in a magnetic medium

> [!hard] Hard · moving pulses · intrinsic impedance
> A uniform medium fills all space. The electric field of a wave moves with velocity $\mathbf{v} = -150\,\hat{z}$ m/μs without changing shape. At $t = 2$ μs its profile is ($z$ in metres)
> $$
> \mathbf{E}(z,\,2\ \mu\text{s}) = g(z)\,\hat{x},\qquad g(z) = \begin{cases} 0.04\,(z - 300)\ \text{V/m}, & 300\le z\le450,\\ (900 - z)/75\ \text{V/m}, & 450\le z\le900,\\ 0 & \text{otherwise,}\end{cases}
> $$
> a triangle that rises from 0 to 6 V/m over 150 m and falls back to 0 over the next 450 m.
>
> (a) Find $\mathbf{E}(z,0)$.
>
> (b) Find $\mathbf{E}(z,t)$ for all $z$ and $t$, and write it as a function of $t + z/v$.
>
> (c) Sketch what a probe at $z = -750$ m records, and give its readings at $t = 9.5$ μs and $t = 11.5$ μs. Is the record the snapshot mirrored?
>
> (d) A magnetic probe finds that the peak $H$ is 15.9 mA/m. Find $\mu_r$ and $\epsilon_r$. Then true or false: "since $E/H = 377\ \Omega$, the medium is vacuum"; "since the wave is slower than light and its field falls off behind the peak, the medium is a conductor".
>
> (e) Find $\mathbf{H}(z,t)$ with its direction, and the peak value of $B$.
>
> *Source: SP18 Exam 2 #4 style, re-parameterized (a triangle moving toward −z through a magnetic medium, in place of the exam's decaying pulse moving toward −x in vacuum and the site's ramp moving toward +y).*

> [!hint]- Hint
> A pattern moving rigidly toward $-z$ at 150 m/μs obeys $\mathbf{E}(z,t) = \mathbf{E}\big(z + 150(t - 2),\ 2\ \mu\text{s}\big)$: the field at $z$ now is what sat $150(t-2)$ metres further toward $+z$ at $t = 2$ μs. Check every shift by following the peak. For (d), $v$ fixes the product $\mu_r\epsilon_r$ and $\eta$ fixes the ratio $\mu_r/\epsilon_r$.

> [!solution]- Solution
> **Setup.** Keep $z$ in metres and $t$ in microseconds, so $v = 150$. The pulse moves toward $-z$, so its **front** is the low-$z$ end, the steep 150 m rise, and the long 450 m fall is its tail. The peak sits at $z_{\text{peak}}(t) = 450 - 150(t - 2) = 750 - 150t$.
>
> **(a)** At $t = 0$ the pattern was $2\times150 = 300$ m further toward $+z$, so $\mathbf{E}(z,0) = g(z - 300)\,\hat{x}$:
> $$
> E_x(z,0) = \begin{cases} 0.04\,(z - 600)\ \text{V/m}, & 600\le z\le750,\\ (1200 - z)/75\ \text{V/m}, & 750\le z\le1200,\\ 0 & \text{otherwise,}\end{cases}
> $$
> with the peak at $z = 750$ m $= z_{\text{peak}}(0)$ ✓.
>
> **(b)** Shift by $150(t - 2)$ instead of by 300 m: $\mathbf{E}(z,t) = g(z + 150t - 300)\,\hat{x}$. With $s = t + z/150$ (in μs), $z + 150t - 300 = 150(s - 2)$, and
> $$
> \mathbf{E}(z,t) = F\Big(t + \frac zv\Big)\,\hat{x},\qquad F(s) = \begin{cases} 6\,(s - 4)\ \text{V/m}, & 4\le s\le5,\\ 2\,(8 - s)\ \text{V/m}, & 5\le s\le8,\\ 0 & \text{otherwise,}\end{cases}
> $$
> a function of $t + z/v$, with the plus sign that a $-z$ wave must have. Checks: $t = 2$ gives the given profile and $t = 0$ gives (a).
>
> **(c)** At $z = -750$ m, $s = t - 5$, so the record is $F(t - 5)$. It rises from 0 at $t = 9$ μs to 6 V/m at $t = 10$ μs (the front arrives first), then falls to 0 at $t = 13$ μs. Readings: $E_x = 6\,(9.5 - 9) = 3$ V/m at 9.5 μs, and $E_x = 2\,(13 - 11.5) = 3$ V/m at 11.5 μs. Cross-check with the snapshot at 11.5 μs, $g(z + 1425)$: at $z = -750$ m it is $g(675) = (900 - 675)/75 = 3$ V/m ✓. The record is **not mirrored**: a steep rise and then a slow fall, in the same order as the snapshot read from low to high $z$. For travel toward $-z$ the front is on the left in both pictures.
>
> **(d)** The pulse keeps its shape, so the medium is lossless (second statement below) and $v = c/\sqrt{\mu_r\epsilon_r}$. The speed gives $\mu_r\epsilon_r = (c/v)^2 = (2.998/1.5)^2 = 3.99\approx4$. The impedance is $\eta = 6\ \text{V/m}\,/\,15.9\ \text{mA/m} = 377\ \Omega\approx\eta_0$, so $\mu_r/\epsilon_r = (\eta/\eta_0)^2\approx1$. Together, $\mu_r = \epsilon_r = 2$.
> - "Vacuum": **false**. $\eta = \eta_0\sqrt{\mu_r/\epsilon_r}$ depends only on the ratio, which is 1 here, but $v = c/\sqrt{\mu_r\epsilon_r} = c/2$. One measurement cannot identify the medium.
> - "Conductor": **false**. A dielectric or magnetic medium slows a wave without any loss, and the fall behind the peak is the pulse's shape, not attenuation: the peak is 6 V/m at every time. A conducting medium would shrink and spread the pulse as it travelled (Lectures 22–23), contradicting "without changing shape".
>
> **(e)** $\hat u = -\hat{z}$ and $(-\hat{z})\times\hat{x} = -\hat{y}$, so
> $$
> \mathbf{H}(z,t) = -\frac{F(t + z/v)}{\eta}\,\hat{y},\qquad \eta = \mu v = 2\mu_0\times1.5\times10^{8} = 120\pi\approx377\ \Omega .
> $$
> Check: $\hat{x}\times(-\hat{y}) = -\hat{z}$, the direction of travel ✓. At the peak, $H = 6/377 = 15.9$ mA/m (consistent with (d)) and $B = \mu H = 2\mu_0\times15.9\ \text{mA/m} = 40$ nT, the same as $E/v = 6/(1.5\times10^{8})$ ✓. At the probe at 11.5 μs, $\mathbf{H} = -7.96\,\hat{y}$ mA/m.
>
> **Watch out:** shifting the wrong way, $g(z + 300)$ for (a), would put the pulse at $0\le z\le600$ m at $t = 0$, *ahead* of where it is at 2 μs (on its $-z$ side), as if it had moved toward $+z$. Following the peak catches this at once.
>
> **Answer.** (a) $E_x(z,0) = 0.04(z - 600)$ V/m on $600\le z\le750$ m and $(1200 - z)/75$ V/m on $750\le z\le1200$ m, peak 6 V/m at 750 m; (b) $\mathbf{E} = g(z + 150t - 300)\,\hat{x} = F(t + z/v)\,\hat{x}$, with $F = 6(s - 4)$ on $4\le s\le5$ μs and $2(8 - s)$ on $5\le s\le8$ μs; (c) rises from 0 at 9 μs to 6 V/m at 10 μs and falls to 0 at 13 μs, reading 3 V/m at both 9.5 and 11.5 μs; not mirrored; (d) $\mu_r = \epsilon_r = 2$, and both statements are false; (e) $\mathbf{H} = -F(t + z/v)\,\hat{y}/\eta$ with $\eta\approx377\ \Omega$, peak $H = 15.9$ mA/m and $B = 40$ nT.

### 18.10 Two pulses passing through each other

> [!hard] Hard · moving pulses · superposition
> Two $x$-polarized pulses travel along the $z$ axis in free space (take $c = 300$ m/μs and $\eta_0 = 120\pi\ \Omega$). At $t = 0$, pulse A, moving toward $+z$, has $E_x = 6$ V/m on $-600<z<-300$ m; pulse B, moving toward $-z$, has $E_x = 3$ V/m on $300<z<900$ m; the field is zero elsewhere.
>
> (a) Write $E_x$ and $H_y$ of each pulse as functions of $t\mp z/c$, with the sign of each $H_y$.
>
> (b) Find $E_x$ and $H_y$ everywhere at $t = 1.5$ μs, and the ratio $E_x/H_y$ in each region. Does the result contradict $E/H = \eta_0$?
>
> (c) What do probes of $E_x$ and $H_y$ at $z = 0$ record?
>
> (d) Where are the pulses at $t = 4$ μs, and what do they look like?
>
> (e) Repeat (b) with B replaced by a pulse B′ that has $E_x = -6$ V/m on $300<z<600$ m at $t = 0$, also moving toward $-z$. A classmate says that at $t = 1.5$ μs "the two pulses have cancelled and the wave is gone". Comment.
>
> *Source: original (counter-propagating d'Alembert solutions, Lecture 18 slides 21–23).*

> [!hint]- Hint
> Superpose: $E_x = f(t - z/c) + g(t + z/c)$ and $H_y = [f(t - z/c) - g(t + z/c)]/\eta_0$. The minus sign is the whole story: the $-z$ pulse's $\mathbf{H}$ is reversed relative to its $\mathbf{E}$. Track the two edges of each pulse, which move at 300 m/μs.

> [!solution]- Solution
> **Setup.** Each pulse alone is a single travelling wave, with $\mathbf{H} = \hat u\times\mathbf{E}/\eta_0$. Maxwell's equations are linear, so the total field is the sum, and each pulse moves on as if the other were absent.
>
> **(a)** Pulse A occupies $-600 + 300t<z<-300 + 300t$, i.e. $1<t - z/300<2$ μs: $E_x^A = f(t - z/c)$, with $f = 6$ V/m for $1<s<2$ μs. Since $\hat{z}\times\hat{x} = +\hat{y}$, $H_y^A = +f/\eta_0$, which is $+15.9$ mA/m on the pulse. Pulse B occupies $300 - 300t<z<900 - 300t$, i.e. $1<t + z/300<3$ μs: $E_x^B = g(t + z/c)$, with $g = 3$ V/m for $1<s<3$ μs. Since $(-\hat{z})\times\hat{x} = -\hat{y}$, $H_y^B = -g/\eta_0$, which is $-7.96$ mA/m on the pulse.
>
> **(b)** At $t = 1.5$ μs, A lies on $-150<z<150$ m and B on $-150<z<450$ m:
> - $-150<z<150$ m (A and B): $E_x = 6 + 3 = 9$ V/m, $H_y = 15.9 - 7.96 = +7.96$ mA/m, so $E_x/H_y = 3\eta_0 = 1131\ \Omega$;
> - $150<z<450$ m (B alone): $E_x = 3$ V/m, $H_y = -7.96$ mA/m, so $E_x/H_y = -\eta_0 = -377\ \Omega$;
> - elsewhere: $E_x = H_y = 0$.
>
> The electric fields add and the magnetic fields subtract. The ratio $3\eta_0$ does not contradict $E/H = \eta_0$: that rule holds for **one** travelling wave, and the overlap contains two. Where B is alone the ratio is $-\eta_0$, as a $-z$ wave requires.
>
> **(c)** At $z = 0$, A passes during $1<t<2$ μs and B during $1<t<3$ μs:
> - $1<t<2$ μs: $E_x = 9$ V/m and $H_y = +7.96$ mA/m;
> - $2<t<3$ μs: $E_x = 3$ V/m and $H_y = -7.96$ mA/m;
> - zero before 1 μs and after 3 μs.
>
> $H_y$ reverses at $t = 2$ μs although $E_x$ stays positive: the $+z$ pulse has left, and only the $-z$ one remains.
>
> **(d)** At $t = 4$ μs, A lies on $600<z<900$ m with 6 V/m and $H_y = +15.9$ mA/m, and B on $-900<z<-300$ m with 3 V/m and $H_y = -7.96$ mA/m. Each is exactly as it was before the encounter, only moved: pulses in a linear medium pass through each other without interacting.
>
> **(e)** B′ moves toward $-z$ with $E_x = -6$ V/m, so $H_y^{B'} = -(-6)/\eta_0 = +15.9$ mA/m. Check: $(-\hat{z})\times(-6\,\hat{x}) = +6\,\hat{y}$ ✓. At $t = 1.5$ μs, A and B′ both lie exactly on $-150<z<150$ m:
> $$
> E_x = 6 - 6 = 0,\qquad H_y = \frac{6 - (-6)}{\eta_0} = \frac{12}{120\pi} = 31.8\ \text{mA/m}.
> $$
> The classmate is wrong. At that instant $\mathbf{E}$ is zero everywhere, but $\mathbf{H}$ is twice as large as either pulse's own. Both waves are still there, and they separate again: at $t = 2.5$ μs, A is on $150<z<450$ m with 6 V/m and B′ on $-450<z<-150$ m with $-6$ V/m, each with $H_y = +15.9$ mA/m and unchanged.
>
> **Check:** the total fields satisfy both component equations, $\partial E_x/\partial z = -\mu_0\,\partial H_y/\partial t$ and $-\partial H_y/\partial z = \epsilon_0\,\partial E_x/\partial t$, only with the minus sign in $H_y = (f - g)/\eta_0$. With $(f + g)/\eta_0$ both equations fail on the edges of B.
>
> **Answer.** (a) $E_x = f(t - z/c) + g(t + z/c)$ and $H_y = (f - g)/\eta_0$: A has 6 V/m with $+15.9$ mA/m, B has 3 V/m with $-7.96$ mA/m. (b) 9 V/m and $+7.96$ mA/m on $-150<z<150$ m (ratio $3\eta_0 = 1131\ \Omega$), 3 V/m and $-7.96$ mA/m on $150<z<450$ m, zero elsewhere. (c) 9 V/m and $+7.96$ mA/m for $1<t<2$ μs, then 3 V/m and $-7.96$ mA/m for $2<t<3$ μs. (d) A on $600<z<900$ m and B on $-900<z<-300$ m, both unchanged. (e) $E_x = 0$ and $H_y = 31.8$ mA/m on $-150<z<150$ m; the pulses are not gone, and they re-emerge unchanged.

### 18.11 The derivation along the x axis

> [!hard] Hard · wave equation · plane waves
> Redo the Lecture 18 derivation for a wave that travels along $x$ instead of $z$. In a source-free, homogeneous, lossless medium ($\mu$, $\epsilon$), look for a field $\mathbf{E} = E_z(x,t)\,\hat{z}$.
>
> (a) Show that Gauss's law holds automatically. Use Faraday's law to show that $\mathbf{H}$ has only a $y$ component (apart from a static field), and write the two scalar equations that link $E_z$ and $H_y$, with their signs.
>
> (b) Cross-differentiate to get the 1D wave equation for $E_z$. Say where $\mathbf{J} = 0$, constant $\mu$ and constant $\epsilon$ were used.
>
> (c) For $E_z = A\,f(t - x/v) + B\,g(t + x/v)$, find $H_y$. Compare with the $z$-travelling result $H_y = (Af - Bg)/\eta$, and explain the difference with $\mathbf{E}\times\mathbf{H}$.
>
> (d) In a non-magnetic medium, $\mathbf{E} = 10\cos(5\pi\times10^{8}\,t + 4\pi x)\,\hat{z}$ V/m. Identify the travelling part(s) and $v$, and find $\epsilon_r$ and $\mathbf{H}$.
>
> (e) A classmate adds $3\cos(5\pi\times10^{8}\,t + 4\pi x)\,\hat{x}$ V/m to the field of (d) "to make it point partly along the direction of travel". Which Maxwell equation forbids this?
>
> *Source: original (the derivation of the Lecture 18 notes and slides, rotated to the x axis).*

> [!hint]- Hint
> With only $\partial/\partial x$ and $\partial/\partial t$ non-zero, $\nabla\times(E_z\hat{z}) = -\dfrac{\partial E_z}{\partial x}\,\hat{y}$ and $\nabla\times(H_y\hat{y}) = \dfrac{\partial H_y}{\partial x}\,\hat{z}$. Take the signs from the determinant, not from memory.

> [!solution]- Solution
> **(a)** $\nabla\cdot\mathbf{E} = \partial E_z/\partial z = 0$, because $E_z$ does not depend on $z$: Gauss's law with $\rho = 0$ holds. The curl has a single component,
> $$
> \nabla\times\mathbf{E} = \Big(\frac{\partial E_z}{\partial y} - \frac{\partial E_y}{\partial z}\Big)\hat{x} + \Big(\frac{\partial E_x}{\partial z} - \frac{\partial E_z}{\partial x}\Big)\hat{y} + \Big(\frac{\partial E_y}{\partial x} - \frac{\partial E_x}{\partial y}\Big)\hat{z} = -\frac{\partial E_z}{\partial x}\,\hat{y},
> $$
> so Faraday's law $\nabla\times\mathbf{E} = -\mu\,\partial\mathbf{H}/\partial t$ gives $\partial H_x/\partial t = \partial H_z/\partial t = 0$. $H_x$ and $H_z$ are static and are dropped, and $\partial H_y/\partial t$ depends only on $x$ and $t$, so $\mathbf{H} = H_y(x,t)\,\hat{y}$ (which has $\nabla\cdot\mathbf{H} = 0$). The $y$ component of Faraday's law and the $z$ component of Ampère–Maxwell, where $\nabla\times(H_y\hat{y}) = (\partial H_y/\partial x)\,\hat{z}$, give
> $$
> \frac{\partial E_z}{\partial x} = \mu\frac{\partial H_y}{\partial t},\qquad \frac{\partial H_y}{\partial x} = \epsilon\frac{\partial E_z}{\partial t}.
> $$
> Both carry a plus sign here, unlike the $z$-travelling pair $\partial E_x/\partial z = -\mu\,\partial H_y/\partial t$, $-\partial H_y/\partial z = \epsilon\,\partial E_x/\partial t$.
>
> **(b)** Differentiate the first equation by $x$, swap the order of the derivatives, and substitute the second:
> $$
> \frac{\partial^2E_z}{\partial x^2} = \mu\frac{\partial}{\partial t}\Big(\frac{\partial H_y}{\partial x}\Big) = \mu\epsilon\frac{\partial^2E_z}{\partial t^2} = \frac{1}{v^2}\frac{\partial^2E_z}{\partial t^2},\qquad v = \frac{1}{\sqrt{\mu\epsilon}} .
> $$
> Where the assumptions entered: $\mathbf{J} = 0$ removed the conduction term from Ampère–Maxwell (a conductor would add $\mu\sigma\,\partial E_z/\partial t$). Constant $\mu$ gave $\partial\mathbf{B}/\partial t = \mu\,\partial\mathbf{H}/\partial t$ and let $\mu$ pass through $\partial/\partial x$ in the cross-differentiation. Constant $\epsilon$ gave $\partial\mathbf{D}/\partial t = \epsilon\,\partial\mathbf{E}/\partial t$ and makes $v$ one number for the whole region. Gauss's law ($\rho = 0$) was used in (a), where it holds by the choice of field.
>
> **(c)** For the $+x$ wave, $\partial E_z/\partial x = -Af'/v$, so $\mu\,\partial H_y/\partial t = -Af'/v$ and $H_y = -Af/(\mu v) = -Af/\eta$. For the $-x$ wave, $\partial E_z/\partial x = +Bg'/v$ and $H_y = +Bg/\eta$. Together,
> $$
> H_y = \frac{-A\,f(t - x/v) + B\,g(t + x/v)}{\eta} = -\frac{Af - Bg}{\eta},
> $$
> the opposite sign to the $z$-travelling case. The cross products agree. Toward $+x$: $\hat{x}\times\hat{z} = -\hat{y}$, so $\mathbf{H}$ is along $-\hat{y}$ when $f>0$, and $\hat{z}\times(-\hat{y}) = +\hat{x}$ ✓. Toward $-x$: $(-\hat{x})\times\hat{z} = +\hat{y}$, and $\hat{z}\times\hat{y} = -\hat{x}$ ✓. Renaming $z\to x$ and $x\to z$ swaps two axes, which is a mirror reflection: it turns a right-handed triad into a left-handed one, so $\mathbf{H}$ must flip to keep $\mathbf{E}\times\mathbf{H}$ along the travel.
>
> **(d)** The $t$ and $x$ terms have the same sign, so this is a $-x$ wave: $5\pi\times10^{8}t + 4\pi x = 5\pi\times10^{8}\big(t + x/(1.25\times10^{8})\big)$. So $A = 0$, $B\,g(s) = 10\cos(5\pi\times10^{8}s)$ V/m, and $v = 1.25\times10^{8}$ m/s. Non-magnetic: $\epsilon_r = (c/v)^2 = (2.998/1.25)^2 = 5.75$ (5.76 with $c = 3\times10^{8}$ m/s), and $\eta = \mu_0v = 50\pi = 157\ \Omega$. From (c), $H_y = +Bg/\eta$:
> $$
> \mathbf{H} = \frac{10\ \text{V/m}}{157.1\ \Omega}\cos(5\pi\times10^{8}\,t + 4\pi x)\,\hat{y} = 63.7\cos(5\pi\times10^{8}\,t + 4\pi x)\,\hat{y}\ \text{mA/m}.
> $$
> Check: $\hat{z}\times\hat{y} = -\hat{x}$ ✓, and $B = E/v = 80$ nT $= \mu_0H$.
>
> **(e)** Gauss's law. The added component varies along its own direction:
> $$
> \nabla\cdot\mathbf{E} = \frac{\partial E_x}{\partial x} = -12\pi\sin(5\pi\times10^{8}\,t + 4\pi x)\ \text{V/m}^2\neq0,
> $$
> which would need an oscillating charge density $\rho = \epsilon\nabla\cdot\mathbf{E}$ in a region that has none. The added field also has no curl, so Faraday's law gives it no $\mathbf{H}$, and the $x$ component of Ampère–Maxwell then demands $\partial E_x/\partial t = 0$. A plane wave has no field component along its direction of travel.
>
> **Answer.** (a) $\partial E_z/\partial x = \mu\,\partial H_y/\partial t$ and $\partial H_y/\partial x = \epsilon\,\partial E_z/\partial t$; (b) $\partial^2E_z/\partial x^2 = \mu\epsilon\,\partial^2E_z/\partial t^2$; (c) $H_y = (Bg - Af)/\eta$, the reverse of the $z$ case, as $\hat{x}\times\hat{z} = -\hat{y}$ requires; (d) a single $-x$ wave with $v = 1.25\times10^{8}$ m/s, $\epsilon_r\approx5.75$, $\mathbf{H} = 63.7\cos(5\pi\times10^{8}t + 4\pi x)\,\hat{y}$ mA/m; (e) Gauss's law, since $\nabla\cdot\mathbf{E} = -12\pi\sin(\cdots)\neq0$.

### 18.12 A wave on a slant

> [!hard] Hard · plane waves · divergence · curl
> In a lossless non-magnetic medium,
> $$
> \mathbf{E} = (6\,\hat{x} - 8\,\hat{y})\cos\phi\ \ \text{V/m},\qquad \phi = 7.5\pi\times10^{8}\,t - 2.4\pi x - 1.8\pi y\quad(x,\ y\ \text{in m},\ t\ \text{in s}).
> $$
> (a) Find the direction of travel $\hat u$, the speed $v$ and $\epsilon_r$.
>
> (b) Show that $\mathbf{E}$ is transverse ($\mathbf{E}\cdot\hat u = 0$) and that $\nabla\cdot\mathbf{E} = 0$.
>
> (c) Find $\eta$ and $\mathbf{H}$, writing the cross product out, and check the direction with $\mathbf{E}\times\mathbf{H}$.
>
> (d) Verify Faraday's law by computing $\nabla\times\mathbf{E}$ directly.
>
> (e) Two other fields with the same $\cos\phi$ are proposed: $\mathbf{E}' = (8\,\hat{x} + 6\,\hat{y})\cos\phi$ and $\mathbf{E}'' = 10\cos\phi\,\hat{z}$ V/m. Which one can exist in this source-free medium? For that one, find $\mathbf{H}''$.
>
> *Source: original (a plane wave along an oblique direction, checked with the divergence and curl of Lecture 4).*

> [!hint]- Hint
> Factor the position terms: $2.4\pi x + 1.8\pi y = 3\pi\,(0.8x + 0.6y)$, and $0.8^2 + 0.6^2 = 1$. So $0.8x + 0.6y$ is $\hat u\cdot\mathbf{r}$ for a unit vector $\hat u$, and $\phi = \omega\big(t - \hat u\cdot\mathbf{r}/v\big)$.

> [!solution]- Solution
> **(a)** With $2.4\pi x + 1.8\pi y = 3\pi\,\hat u\cdot\mathbf{r}$ and
> $$
> \hat u = 0.8\,\hat{x} + 0.6\,\hat{y}\quad(36.9^\circ\ \text{from the}\ x\ \text{axis toward}\ y),
> $$
> the argument is $\phi = 7.5\pi\times10^{8}\big(t - \hat u\cdot\mathbf{r}/v\big)$ with $v = 7.5\pi\times10^{8}/3\pi = 2.5\times10^{8}$ m/s. The signs are opposite, so the wave travels toward $+\hat u$. Non-magnetic: $\epsilon_r = (c/v)^2 = 1.44$.
>
> **(b)** $\mathbf{E}_0\cdot\hat u = 6(0.8) - 8(0.6) = 0$ ✓. Directly: $\partial\phi/\partial x = -2.4\pi$ and $\partial\phi/\partial y = -1.8\pi$, so $\partial(\cos\phi)/\partial x = 2.4\pi\sin\phi$ and $\partial(\cos\phi)/\partial y = 1.8\pi\sin\phi$, and
> $$
> \nabla\cdot\mathbf{E} = 6\,(2.4\pi\sin\phi) - 8\,(1.8\pi\sin\phi) = (14.4\pi - 14.4\pi)\sin\phi = 0\qquad\checkmark
> $$
> **(c)** $\eta = \mu_0v = 4\pi\times10^{-7}\times2.5\times10^{8} = 100\pi\approx314\ \Omega$, and $\lvert\mathbf{E}_0\rvert = \sqrt{6^2 + 8^2} = 10$ V/m. Term by term,
> $$
> \hat u\times\mathbf{E}_0 = (0.8\,\hat{x} + 0.6\,\hat{y})\times(6\,\hat{x} - 8\,\hat{y}) = 0.8(-8)\,\hat{x}\times\hat{y} + 0.6(6)\,\hat{y}\times\hat{x} = -6.4\,\hat{z} - 3.6\,\hat{z} = -10\,\hat{z},
> $$
> so
> $$
> \mathbf{H} = \frac{\hat u\times\mathbf{E}}{\eta} = -\frac{10\ \text{V/m}}{100\pi\ \Omega}\cos\phi\,\hat{z} = -31.8\cos\phi\,\hat{z}\ \text{mA/m}.
> $$
> Check: $(6\,\hat{x} - 8\,\hat{y})\times(-\hat{z}) = 6\,\hat{y} + 8\,\hat{x} = 10\,\hat u$, along the travel ✓.
>
> **(d)** Only $E_x$ and $E_y$ are non-zero and neither depends on $z$, so $\nabla\times\mathbf{E} = \big(\partial E_y/\partial x - \partial E_x/\partial y\big)\hat{z}$, with
> $$
> \frac{\partial E_y}{\partial x} = -8\,(2.4\pi)\sin\phi = -19.2\pi\sin\phi,\qquad \frac{\partial E_x}{\partial y} = 6\,(1.8\pi)\sin\phi = 10.8\pi\sin\phi,
> $$
> so $\nabla\times\mathbf{E} = -30\pi\sin\phi\,\hat{z}$ V/m². On the other side, $\partial\mathbf{H}/\partial t = +(10/\eta)\,\omega\sin\phi\,\hat{z}$, and with $\mu_0/\eta = 1/v$,
> $$
> -\mu_0\frac{\partial\mathbf{H}}{\partial t} = -\frac{10\,\omega}{v}\sin\phi\,\hat{z} = -10\times3\pi\sin\phi\,\hat{z} = -30\pi\sin\phi\,\hat{z}\qquad\checkmark
> $$
> The Ampère–Maxwell law checks the same way: both $\nabla\times\mathbf{H}$ and $\epsilon\,\partial\mathbf{E}/\partial t$ point along $-0.6\,\hat{x} + 0.8\,\hat{y}$, with magnitudes $3\pi\times10/\eta$ and $10\,\epsilon\omega$, which agree because $\epsilon v\eta = 1$.
>
> **(e)** $\mathbf{E}'$ cannot exist. $(8\,\hat{x} + 6\,\hat{y})\cdot\hat u = 6.4 + 3.6 = 10$: it points along the travel, and $\nabla\cdot\mathbf{E}' = (8\times2.4\pi + 6\times1.8\pi)\sin\phi = 30\pi\sin\phi\neq0$, which violates Gauss's law with $\rho = 0$. $\mathbf{E}''$ can: $\hat{z}\perp\hat u$ and $\nabla\cdot\mathbf{E}'' = \partial E_z/\partial z = 0$. Its partner:
> $$
> \hat u\times\hat{z} = 0.8\,\hat{x}\times\hat{z} + 0.6\,\hat{y}\times\hat{z} = 0.6\,\hat{x} - 0.8\,\hat{y},\qquad \mathbf{H}'' = 31.8\cos\phi\,(0.6\,\hat{x} - 0.8\,\hat{y}) = (19.1\,\hat{x} - 25.5\,\hat{y})\cos\phi\ \text{mA/m}.
> $$
> Check: $\hat{z}\times(0.6\,\hat{x} - 0.8\,\hat{y}) = 0.6\,\hat{y} + 0.8\,\hat{x} = \hat u$ ✓. A wave travelling along $\hat u$ can have its $\mathbf{E}$ anywhere in the plane perpendicular to $\hat u$; $\mathbf{E}$ and $\mathbf{E}''$ are its two independent polarizations.
>
> **Answer.** (a) $\hat u = 0.8\,\hat{x} + 0.6\,\hat{y}$, $v = 2.5\times10^{8}$ m/s, $\epsilon_r\approx1.44$; (b) $\mathbf{E}_0\cdot\hat u = 0$ and $\nabla\cdot\mathbf{E} = 0$; (c) $\eta = 100\pi\approx314\ \Omega$, $\mathbf{H} = -31.8\cos\phi\,\hat{z}$ mA/m; (d) $\nabla\times\mathbf{E} = -30\pi\sin\phi\,\hat{z}$ V/m² $= -\mu_0\,\partial\mathbf{H}/\partial t$; (e) only $\mathbf{E}''$, with $\mathbf{H}'' = (19.1\,\hat{x} - 25.5\,\hat{y})\cos\phi$ mA/m.

### Sources for this page
Course notes and slides for Lecture 18: the velocity challenge of slide 24 (18.1, with new waveforms, axes and traps); the shift identities of slide 25 (18.8, applied to a two-level record); the counter-propagating pair $H_y = (Af - Bg)/\eta$ of slides 21–23 (18.10); the notes' E–H rules (18.2), their $z$-polarized question and the assumptions of the derivation (18.4); and the derivation itself, rotated to the $x$ axis (18.11). Old exams: SP18 Exam 2 #4, re-parameterized (18.9: a triangle pulse moving toward $-z$ through a magnetic medium with $\mu_r = \epsilon_r = 2$, in place of the exam's decaying pulse moving toward $-x$ in vacuum, and different from the site's worked problem [[problems/a-pulse-on-the-move|A pulse on the move]]), and the style of SP18 Exam 2 #1(vii) (18.3: a phase rate and a spatial period, in a dielectric). The cable link of Lecture 18 §7, with the line parameters of Lectures 10 and 15 (18.7). Original: 18.5, 18.6 and 18.12.

*Previous: [[practice/17-magnetization-and-maxwell-in-matter|Lecture 17 practice]] · [[practice/index|all practice]]*
