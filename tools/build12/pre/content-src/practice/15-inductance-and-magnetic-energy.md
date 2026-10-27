---
title: "Practice — Lecture 15: Inductance, magnetic energy, and the potentials"
description: "12 practice problems (5 easy, 3 medium, 4 hard) on self- and mutual inductance (solenoid, toroid, coax, parallel plates, two-wire line), RL decay and rise, magnetic energy and internal inductance, the LC product, and fields from potentials with gauge transformations, each with a worked solution and a folded hint for the medium and hard ones."
tags: [practice, magnetostatics]
lecture: 15
---

*Practice for [[2-magnetostatics/15-inductance-magnetic-energy-and-the-potentials|Lecture 15]] · concepts: [[concepts/inductance]] · [[concepts/magnetic-energy]] · [[concepts/vector-potential]] · all practice: [[practice/index|hub]] · by difficulty: [[practice/easy|easy]] · [[practice/medium|medium]] · [[practice/hard|hard]] · [[practice/topics|by topic]]*

Work each problem on paper first. Open the **hint** only when stuck, and the **solution** only after you have an answer you would hand in. Every answer here has been checked numerically.

## Easy

### 15.1 A long solenoid by the numbers

> [!easy] Easy · inductance · solenoid · magnetic energy
> A long air-core solenoid has $N = 500$ turns wound uniformly over a length $\ell = 25$ cm on a form of radius $a = 1$ cm. Ignore end effects.
>
> (a) Find its inductance $L$.
>
> (b) Find $L$ again if (i) 1000 turns are wound over the same 25 cm, (ii) the original 500 turns are spread over 50 cm (same radius).
>
> (c) At $I = 2$ A, find the stored energy from $\tfrac12LI^2$, and again from the energy density $\tfrac12\mu_0H^2$ times the volume of the interior.
>
> *Source: course notes Lecture 15 (the long solenoid), new numbers.*

> [!solution]- Solution
> **(a)** Inside a long solenoid $B = \mu_0nI$ with $n = N/\ell = 2000$ turns/m ([[2-magnetostatics/13-current-sheets-solenoids-and-the-vector-potential|Lecture 13]]), uniform over the cross-section $\pi a^2$. Each of the $N$ turns links $\Psi = \mu_0nI\,\pi a^2$, so
> $$
> L = \frac{N\Psi}{I} = \frac{\mu_0N^2\pi a^2}{\ell} = \frac{(4\pi\times10^{-7})(500)^2(\pi\times10^{-4})}{0.25} = 4\pi^2\times10^{-5}\ \text{H}\approx0.395\ \text{mH}.
> $$
> **(b)** $L\propto N^2/\ell$. (i) Twice the turns on the same length double $B$ *and* double the number of turns that link it: $L\times4 = 1.58$ mH. (ii) The same turns on twice the length halve $B$, while the number of linking turns stays 500: $L\times\tfrac12 = 0.197$ mH.
>
> **(c)** $W = \tfrac12LI^2 = \tfrac12(4\pi^2\times10^{-5})(2)^2 = 8\pi^2\times10^{-5}$ J $\approx0.790$ mJ. Field route: $H = nI = 4000$ A/m, so $w = \tfrac12\mu_0H^2 = \tfrac12(4\pi\times10^{-7})(4000)^2 = 3.2\pi\approx10.1$ J/m³, filling the interior volume $\pi a^2\ell = 0.25\pi\times10^{-4}\approx7.85\times10^{-5}$ m³:
> $$
> W = w\,\pi a^2\ell = (3.2\pi)(0.25\pi\times10^{-4}) = 8\pi^2\times10^{-5}\ \text{J},
> $$
> the same as $\tfrac12LI^2$ ✓. The two routes must agree: $\tfrac12LI^2$ *is* the field energy, counted at the terminals.
>
> **Watch out:** $L$ grows as $N^2$, not $N$: the field and the number of turns that link it both grow with $N$.
>
> **Answer.** (a) $L = 4\pi^2\times10^{-5}$ H $\approx0.395$ mH. (b) (i) 1.58 mH; (ii) 0.197 mH. (c) $W = 8\pi^2\times10^{-5}$ J $\approx0.790$ mJ by both routes.

### 15.2 A shorted coil lets go

> [!easy] Easy · RL decay · magnetic energy
> A coil with inductance $L = 40$ mH carries $I_0 = 2$ A. At $t = 0$ its source is removed and the coil is left shorted, so the current circulates through the loop's total resistance $R = 8\ \Omega$.
>
> (a) Find the time constant and $I(t)$ for $t>0$.
>
> (b) At $t = \tau$, find the current and the voltage drop $V = L\,dI/dt$ across the inductor in the direction of $I$. Which element is acting as the source?
>
> (c) Find the stored energy at $t = 0$ and at $t = \tau$, and the time at which half of the initial energy is gone.
>
> *Source: course notes Lecture 15, Example 1 style, new numbers.*

> [!solution]- Solution
> **(a)** Around the loop the self-emf (a rise) supplies the resistive drop: $RI = -L\,dI/dt$, so $I(t) = I_0e^{-t/\tau}$ with
> $$
> \tau = \frac LR = \frac{40\times10^{-3}}{8} = 5\ \text{ms},\qquad I(t) = 2e^{-200t}\ \text{A}\quad(t\ \text{in s}).
> $$
> **(b)** $I(\tau) = 2/e = 0.736$ A. The inductor's drop in the direction of $I$ is $V = L\,dI/dt = -\dfrac{L}{\tau}I = -RI = -5.89$ V. A *negative* drop is a rise: the self-emf $-L\,dI/dt = +5.89$ V pushes the current, and the resistor takes the matching drop $RI = 5.89$ V. The inductor is the source, running on its stored energy.
>
> **(c)** $W_0 = \tfrac12LI_0^2 = \tfrac12(0.04)(2)^2 = 80$ mJ. Since $W\propto I^2\propto e^{-2t/\tau}$, the energy decays twice as fast as the current (time constant $\tau/2 = 2.5$ ms): $W(\tau) = W_0e^{-2} = 10.8$ mJ, only 0.135 of the start. Half is gone when $e^{-2t/\tau} = \tfrac12$:
> $$
> t = \frac\tau2\ln2 = 1.73\ \text{ms},\qquad\text{when } I = I_0/\sqrt2 = 1.41\ \text{A}.
> $$
> **Check:** the heat dissipated over all time is $\displaystyle\int_0^\infty I^2R\,dt = \frac{RI_0^2\tau}{2} = 0.08$ J $= W_0$ ✓: every joule stored in the field ends up in the resistor.
>
> **Watch out:** $V = L\,dI/dt$ is a drop in the direction of $I$. While the current decays, $dI/dt<0$ and the "drop" is negative.
>
> **Answer.** (a) $\tau = 5$ ms, $I = 2e^{-t/5\,\text{ms}}$ A. (b) 0.736 A; $V = L\,dI/dt = -5.89$ V, a 5.89 V rise: the inductor drives the current. (c) 80 mJ and 10.8 mJ; half the energy is gone at $t = 1.73$ ms.

### 15.3 Fields from given potentials

> [!easy] Easy · potentials · multiple choice
> In a region of free space the potentials are $\Phi = 2y^2$ V and $\mathbf{A} = -4yt\,\hat{y} + 5x\,\hat{z}$ Wb/m, with $x, y, z$ in metres and $t$ in seconds. Which fields do they describe?
>
> (a) $\mathbf{E} = 0$, $\mathbf{B} = -5\hat{y}$ T
>
> (b) $\mathbf{E} = -4y\,\hat{y}$ V/m, $\mathbf{B} = -5\hat{y}$ T
>
> (c) $\mathbf{E} = 0$, $\mathbf{B} = +5\hat{y}$ T
>
> (d) $\mathbf{E} = -8y\,\hat{y}$ V/m, $\mathbf{B} = -5\hat{y}$ T
>
> *Source: SP18 Exam 2 #1(v) style, new potentials.*

> [!solution]- Solution
> **(a) is correct.** With time variation, $\mathbf{E} = -\nabla\Phi - \partial\mathbf{A}/\partial t$ and $\mathbf{B} = \nabla\times\mathbf{A}$:
> $$
> \mathbf{E} = -4y\,\hat{y} - (-4y\,\hat{y}) = 0,\qquad \mathbf{B} = \hat{y}\Big(\frac{\partial A_x}{\partial z} - \frac{\partial A_z}{\partial x}\Big) = \hat{y}\,(0-5) = -5\hat{y}\ \text{T}.
> $$
> The $x$ and $z$ components of the curl vanish, because $A_y$ depends on $y$ and $t$ only and $A_z$ on $x$ only. *Why* $\mathbf{E} = 0$: the term $-4yt\,\hat{y}$ is the gradient of $\lambda = -2y^2t$, and $\Phi = 2y^2$ is exactly $-\partial\lambda/\partial t$. So $(\Phi,\mathbf{A})$ is a gauge transformation of the static pair $(0,\ 5x\,\hat{z})$, which has $\mathbf{E} = 0$ and $\mathbf{B} = \nabla\times(5x\,\hat{z}) = -5\hat{y}$ T.
>
> (b) uses the electrostatic formula $\mathbf{E} = -\nabla\Phi$ and drops $-\partial\mathbf{A}/\partial t$, which is not allowed once $\mathbf{A}$ depends on time. (c) writes the $y$ component of the curl in the wrong order, $\partial A_z/\partial x - \partial A_x/\partial z$. (d) flips the sign of the $\partial\mathbf{A}/\partial t$ term.
>
> **Check:** Faraday's law $\nabla\times\mathbf{E} = -\partial\mathbf{B}/\partial t$ holds for (a): both sides are zero.
>
> **Answer.** (a): $\mathbf{E} = 0$, $\mathbf{B} = -5\hat{y}$ T.

### 15.4 Gauge transformations, true or false

> [!easy] Easy · gauge · true or false
> The potentials $\Phi = 0$, $\mathbf{A} = B_0x\,\hat{y}$ ($B_0$ a constant, in T) describe a uniform static field $\mathbf{B} = B_0\hat{z}$ with $\mathbf{E} = 0$. True or false: each pair below describes the **same** $\mathbf{E}$ and $\mathbf{B}$ ($x, y, z$ in metres, $t$ in seconds, $\Phi'$ in V, $\mathbf{A}'$ in Wb/m).
>
> (a) $\Phi' = 0$, $\mathbf{A}' = -B_0y\,\hat{x}$
>
> (b) $\Phi' = 0$, $\mathbf{A}' = B_0x\,\hat{y} + 2t\,\hat{z}$
>
> (c) $\Phi' = -2z$, $\mathbf{A}' = B_0x\,\hat{y} + 2t\,\hat{z}$
>
> (d) $\Phi' = 0$, $\mathbf{A}' = B_0y\,\hat{x}$
>
> *Source: Lecture 15 slides, gauge-transformation challenge style.*

> [!solution]- Solution
> Two pairs give the same fields when they differ by a gauge transformation, $\mathbf{A}' = \mathbf{A}+\nabla\lambda$ **together with** $\Phi' = \Phi-\partial\lambda/\partial t$. You can always just compute $\mathbf{E}' = -\nabla\Phi'-\partial\mathbf{A}'/\partial t$ and $\mathbf{B}' = \nabla\times\mathbf{A}'$ and compare.
>
> (a) **True.** $B'_z = \partial A'_y/\partial x - \partial A'_x/\partial y = 0-(-B_0) = B_0$, and nothing depends on $t$, so $\mathbf{E}' = 0$. The gauge function is $\lambda = -B_0xy$: $\nabla\lambda = -B_0y\,\hat{x} - B_0x\,\hat{y}$, and $\mathbf{A}+\nabla\lambda = -B_0y\,\hat{x}$ ✓.
>
> (b) **False.** $\nabla\times(2t\,\hat{z}) = 0$, so $\mathbf{B}' = B_0\hat{z}$ is right, but $\mathbf{E}' = -\partial\mathbf{A}'/\partial t = -2\hat{z}$ V/m $\neq0$. This adds $\nabla\lambda$ with $\lambda = 2zt$ to $\mathbf{A}$ without the matching change of $\Phi$.
>
> (c) **True.** $\mathbf{E}' = -\nabla(-2z) - 2\hat{z} = 2\hat{z}-2\hat{z} = 0$ and $\mathbf{B}' = B_0\hat{z}$. This is the complete transformation with $\lambda = 2zt$: $\nabla\lambda = 2t\,\hat{z}$ and $-\partial\lambda/\partial t = -2z$ ✓.
>
> (d) **False.** $\nabla\times(B_0y\,\hat{x}) = -B_0\hat{z}$: the field is reversed. The change $\mathbf{A}'-\mathbf{A} = B_0y\,\hat{x} - B_0x\,\hat{y}$ has curl $-2B_0\hat{z}\neq0$, so it is not the gradient of anything.
>
> **Watch out:** a gauge transformation always comes as a pair, $+\nabla\lambda$ in $\mathbf{A}$ and $-\partial\lambda/\partial t$ in $\Phi$. Changing only one of them, or flipping one sign, changes $\mathbf{E}$.
>
> **Answer.** (a) true, (b) false, (c) true, (d) false.

### 15.5 Two-wire line, find the error

> [!easy] Easy · find the error · two-wire line · inductance
> Two long parallel wires of radius $a = 1$ mm with centres $D = 1$ cm apart form a two-wire line in free space: wire 1 lies on the $z$ axis and carries $I$ along $+\hat{z}$, wire 2 lies at $x = D$ and carries $I$ along $-\hat{z}$. A student computes the inductance per unit length, ignoring the field inside the wires:
>
> *"Wire 1 makes $B = \mu_0I/(2\pi x)$ in the gap. The flux per metre between the wire surfaces is $\int_a^{D-a}\frac{\mu_0I}{2\pi x}\,dx = \frac{\mu_0I}{2\pi}\ln\frac{D-a}{a}$, so $\mathcal{L} = \frac{\mu_0}{2\pi}\ln9 = 0.44\ \mu$H/m."*
>
> (a) What is wrong? Give the correct $\mathcal{L}$.
>
> (b) In the same approximation, the line's capacitance per unit length is $\mathcal{C} = \pi\epsilon_0/\ln[(D-a)/a]$. Use the product $\mathcal{L}\mathcal{C}$ to show that the student's answer cannot be right.
>
> *Source: original.*

> [!solution]- Solution
> **(a) The slip: the return wire was forgotten.** Wire 2 carries current along $-\hat{z}$, and in the gap its field points the *same* way as wire 1's. At a point between the wires, wire 2's Biot–Savart direction is $(-\hat{z})\times(-\hat{x}) = +\hat{y}$, and wire 1's is $\hat{z}\times\hat{x} = +\hat{y}$. So in the gap
> $$
> B_y = \frac{\mu_0I}{2\pi}\Big[\frac1x + \frac1{D-x}\Big],\qquad \frac{\Psi}{\ell} = \frac{\mu_0I}{2\pi}\Big[\ln\frac{D-a}{a} + \ln\frac{D-a}{a}\Big] = \frac{\mu_0I}{\pi}\ln\frac{D-a}{a},
> $$
> and $\mathcal{L} = \dfrac{\mu_0}{\pi}\ln9 = 0.879\ \mu$H/m, twice the student's value ($\ln9 = 2.197$). This keeps the student's approximation (each wire's field taken as that of a line current at its centre, flux counted between the surfaces); for $D/a = 10$ an exact calculation gives a value about 4–5% higher.
>
> **(b)** $\mathcal{C} = \pi\epsilon_0/\ln9 = 12.7$ pF/m. The corrected pair gives $\mathcal{L}\mathcal{C} = \dfrac{\mu_0}{\pi}\ln9\cdot\dfrac{\pi\epsilon_0}{\ln9} = \mu_0\epsilon_0 = 1.11\times10^{-17}$ s²/m², as it must for a two-conductor line in vacuum. The student's $\mathcal{L}$ gives $\mathcal{L}\mathcal{C} = \mu_0\epsilon_0/2$, i.e. $1/\sqrt{\mathcal{L}\mathcal{C}} = \sqrt2\,c = 4.24\times10^8$ m/s, faster than light in vacuum. That is impossible.
>
> **Answer.** The return wire's field (also along $+\hat{y}$ in the gap) was left out; $\mathcal{L} = (\mu_0/\pi)\ln9 = 0.879\ \mu$H/m. With $\mathcal{C} = 12.7$ pF/m the corrected value gives $\mathcal{L}\mathcal{C} = \mu_0\epsilon_0$, while the student's gives $\mu_0\epsilon_0/2$.

## Medium

### 15.6 Switching on an RL circuit

> [!medium] Medium · RL circuit · magnetic energy · power
> At $t = 0$ a switch connects a $V_0 = 12$ V battery to a coil of inductance $L = 0.2$ H. The total series resistance is $R = 10\ \Omega$, and no current flows before the switch closes.
>
> (a) Find $I(t)$.
>
> (b) At $t = \tau$, find the current and the voltage drops across $R$ and across $L$.
>
> (c) At $t = \tau$, find the stored energy, the power delivered by the battery, the power dissipated in $R$, and the rate at which the stored energy grows. Show that they balance.
>
> (d) At what time does the stored energy reach half of its final value?
>
> *Source: classic.*

> [!hint]- Hint
> KVL around the loop: $V_0 = RI + L\,dI/dt$. For (d), the energy goes as $I^2$, so "half the energy" means $I = I_\infty/\sqrt2$, not $I_\infty/2$.

> [!solution]- Solution
> **Setup.** The battery's rise equals the two drops in the direction of $I$: $V_0 = RI + L\,dI/dt$, with $I(0) = 0$ because an inductor's current cannot jump.
>
> **(a)** The solution is the steady current minus a decaying transient:
> $$
> I(t) = \frac{V_0}{R}\big(1-e^{-t/\tau}\big),\qquad \tau = \frac LR = 20\ \text{ms},\qquad I(t) = 1.2\big(1-e^{-50t}\big)\ \text{A}\quad(t\ \text{in s}).
> $$
> **(b)** $I(\tau) = 1.2(1-e^{-1}) = 0.759$ A. The drops are $V_R = RI = 7.59$ V and $V_L = L\,dI/dt = V_0e^{-t/\tau} = 12/e = 4.41$ V. They add to 12 V ✓.
>
> **(c)** $W = \tfrac12LI^2 = \tfrac12(0.2)(0.7585)^2 = 57.5$ mJ. The powers are
> $$
> P_{\text{battery}} = V_0I = 9.10\ \text{W},\qquad P_R = I^2R = 5.75\ \text{W},\qquad \frac{dW}{dt} = LI\frac{dI}{dt} = V_LI = 3.35\ \text{W}.
> $$
> $5.75 + 3.35 = 9.10$ W ✓: the battery's power splits into heat in $R$ and growth of the field energy.
>
> **(d)** The final energy is $W_\infty = \tfrac12L(1.2)^2 = 144$ mJ. Half of it requires $I = I_\infty/\sqrt2$:
> $$
> 1-e^{-t/\tau} = \frac1{\sqrt2}\quad\Rightarrow\quad t = \tau\ln\frac{1}{1-1/\sqrt2} = 1.228\,\tau = 24.6\ \text{ms}.
> $$
> **Check:** limits. At $t = 0^+$, $I = 0$ and $V_L = V_0 = 12$ V: the coil momentarily takes the whole battery voltage. As $t\to\infty$, $V_L\to0$ and $I\to V_0/R = 1.2$ A: the coil acts like a wire.
>
> **Watch out:** the current reaches half its final value at $\tau\ln2 = 13.9$ ms, but the energy needs 24.6 ms to reach half of its final value, because it goes as $I^2$.
>
> **Answer.** (a) $I = 1.2\big(1-e^{-t/20\,\text{ms}}\big)$ A. (b) 0.759 A; $V_R = 7.59$ V, $V_L = 4.41$ V. (c) $W = 57.5$ mJ; 9.10 W from the battery = 5.75 W of heat + 3.35 W into the field. (d) $t = 24.6$ ms.

### 15.7 Internal inductance of a wire

> [!medium] Medium · internal inductance · magnetic energy
> A long straight round wire of radius $a$ carries a steady current $I$, spread uniformly over its cross-section; $\mu = \mu_0$ inside.
>
> (a) Find $\mathbf{H}$ inside the wire.
>
> (b) Find the magnetic energy $W'$ stored *inside* the wire per metre of length, and from it the internal inductance per unit length $\mathcal{L}_{\text{int}} = 2W'/I^2$. Show that it does not depend on $a$, and evaluate it.
>
> (c) A student instead takes the flux per metre crossing the strip $0<r<a$ (in a plane containing the axis) and divides it by $I$. What does she get, and why is that not the inductance?
>
> (d) Add the internal inductance of both wires to the two-wire line of Problem 15.5 ($\mathcal{L} = 0.879\ \mu$H/m without it). By what percentage does $\mathcal{L}$ grow (low frequency, uniform current)?
>
> *Source: classic.*

> [!hint]- Hint
> Ampère's law on a circle of radius $r<a$ encloses only the fraction $r^2/a^2$ of the current. Then integrate $\tfrac12\mu_0H^2$ over the disk $r<a$ with $dS = 2\pi r\,dr$.

> [!solution]- Solution
> **Setup.** Cylindrical symmetry gives $\mathbf{H} = H_\phi(r)\hat\phi$. When the field lives *inside* the current there is no single surface "bounded by the current path", so the energy route, $\mathcal{L} = 2W'/I^2$, is the safe definition of inductance.
>
> **(a)** Ampère: $H_\phi\cdot2\pi r = I\dfrac{r^2}{a^2}$, so $\mathbf{H} = \dfrac{Ir}{2\pi a^2}\hat\phi$ for $r<a$.
>
> **(b)**
> $$
> W' = \int_0^a\tfrac12\mu_0\Big(\frac{Ir}{2\pi a^2}\Big)^2 2\pi r\,dr = \frac{\mu_0I^2}{4\pi a^4}\int_0^a r^3\,dr = \frac{\mu_0I^2}{16\pi},\qquad \mathcal{L}_{\text{int}} = \frac{2W'}{I^2} = \frac{\mu_0}{8\pi} = 50\ \text{nH/m}.
> $$
> The radius cancels: at a given fraction $r/a$ of the radius, a thicker wire has a weaker field ($H\propto1/a$, so $w\propto1/a^2$) spread over a larger area ($\propto a^2$). The energy per metre is $2.5\times10^{-8}$ J/m at 1 A for any $a$.
>
> **(c)** The strip flux is $\displaystyle\int_0^a\mu_0\frac{Ir}{2\pi a^2}\,dr = \frac{\mu_0I}{4\pi}$, giving $\mu_0/(4\pi) = 100$ nH/m, **twice** the correct value. The flux crossing the strip at radius $r$ encircles only the current inside $r$, the fraction $r^2/a^2$ of $I$, so it is not linked by the whole circuit. Weighting each strip element by that fraction repairs it:
> $$
> \frac1I\int_0^a\frac{r^2}{a^2}\,\mu_0\frac{Ir}{2\pi a^2}\,dr = \frac{\mu_0}{8\pi},
> $$
> in agreement with the energy route ✓.
>
> **(d)** $\mathcal{L} = 0.879 + 2(0.050) = 0.979\ \mu$H/m, about 11% more than the external value alone.
>
> **Check:** units: $\mu_0$ [H/m] times a pure number is an inductance per metre ✓. Two independent routes (energy, weighted flux) give the same $\mu_0/(8\pi)$.
>
> **Answer.** (a) $\mathbf{H} = \dfrac{Ir}{2\pi a^2}\hat\phi$. (b) $W' = \mu_0I^2/(16\pi)$; $\mathcal{L}_{\text{int}} = \mu_0/(8\pi) = 50$ nH/m for any $a$. (c) $\mu_0/(4\pi) = 100$ nH/m, twice too big: the flux inside the wire links only part of the current. (d) $0.979\ \mu$H/m, about 11% more.

### 15.8 Two coaxial solenoids

> [!medium] Medium · mutual inductance · solenoid · magnetic energy
> Two long coaxial solenoids share the same length $\ell = 0.5$ m in free space. The inner one has radius $a = 1$ cm and $n_1 = 2000$ turns/m; the outer one has radius $b = 2$ cm and $n_2 = 1000$ turns/m. Ignore end effects.
>
> (a) Find the self-inductances $L_1$ and $L_2$.
>
> (b) Find the mutual inductance $M$ two ways: from the flux of the inner coil's field through the outer coil's turns, and from the flux of the outer coil's field through the inner coil's turns.
>
> (c) With the outer coil open-circuited, the inner current rises at $dI_1/dt = 100$ A/s. What emf appears across the outer coil?
>
> (d) The coils are connected in series so that the same current $I$ flows in both, first with their fields aiding and then opposing. Find the total inductance in each case from the stored energy, and show that it equals $L_1+L_2\pm2M$.
>
> *Source: classic, new numbers.*

> [!hint]- Hint
> A long solenoid's field is uniform inside and zero outside. Ask *through which area* each coil's field actually crosses the other coil's turns. For (d), add the two fields region by region ($r<a$ and $a<r<b$) before squaring.

> [!solution]- Solution
> **Setup.** $N_1 = n_1\ell = 1000$ and $N_2 = n_2\ell = 500$. Each coil's field is $\mu_0nI$ inside its own radius and zero outside it.
>
> **(a)** $L_1 = \mu_0n_1^2\pi a^2\ell = 0.8\pi^2\times10^{-4}$ H $= 0.790$ mH and $L_2 = \mu_0n_2^2\pi b^2\ell = 0.790$ mH. They are equal here only because $n_1a = n_2b$.
>
> **(b)** *Route 1:* $I_1$ makes $\mu_0n_1I_1$ in $r<a$ and nothing beyond. A turn of the outer coil (radius $b$) catches only that flux, $\mu_0n_1I_1\pi a^2$, so $M = N_2\mu_0n_1\pi a^2 = \mu_0n_1n_2\pi a^2\ell$. *Route 2:* $I_2$ makes $\mu_0n_2I_2$ everywhere in $r<b$, and a turn of the inner coil (radius $a$) catches $\mu_0n_2I_2\pi a^2$, so $M = N_1\mu_0n_2\pi a^2 = \mu_0n_1n_2\pi a^2\ell$. The two routes agree, as they must:
> $$
> M = \mu_0n_1n_2\pi a^2\ell = 0.4\pi^2\times10^{-4}\ \text{H} = 0.395\ \text{mH}.
> $$
> **(c)** $\lvert\mathcal{E}\rvert = M\,dI_1/dt = (0.395\ \text{mH})(100\ \text{A/s}) = 39.5$ mV.
>
> **(d)** Aiding: $H = (n_1+n_2)I$ for $r<a$ and $n_2I$ for $a<r<b$. Then
> $$
> W = \tfrac12\mu_0I^2\pi\ell\Big[(n_1+n_2)^2a^2 + n_2^2(b^2-a^2)\Big] = \tfrac12\mu_0I^2\pi\ell\,(900+300),
> $$
> so $L_{\text{aid}} = 2W/I^2 = \mu_0\pi\ell(1200) = 2.37$ mH. Opposing: $(n_1-n_2)^2a^2 + n_2^2(b^2-a^2) = 100+300 = 400$, so $L_{\text{opp}} = \mu_0\pi\ell(400) = 0.790$ mH. Expanding the bracket, $(n_1\pm n_2)^2a^2 + n_2^2(b^2-a^2) = n_1^2a^2 + n_2^2b^2 \pm 2n_1n_2a^2$, and multiplying by $\mu_0\pi\ell$ gives exactly $L_1+L_2\pm2M = 0.790+0.790\pm0.790$ mH ✓.
>
> **Check:** $M/\sqrt{L_1L_2} = 0.5 = a/b$, less than 1 as it must be: the outer coil's flux in $a<r<b$ misses the inner coil.
>
> **Answer.** (a) $L_1 = L_2 = 0.8\pi^2\times10^{-4}$ H $= 0.790$ mH. (b) $M = \mu_0n_1n_2\pi a^2\ell = 0.395$ mH both ways. (c) 39.5 mV. (d) 2.37 mH aiding and 0.790 mH opposing, $= L_1+L_2\pm2M$.

## Hard

### 15.9 Toroid with a two-layer core

> [!hard] Hard · toroid · inductance · magnetic energy
> A toroid has $N = 1000$ turns wound tightly on a core of rectangular cross-section occupying $a<r<b$, $0<z<h$, with $a = 5$ cm, $b = 10$ cm, $h = 2$ cm. The lower half of the core ($0<z<1$ cm) is ferrite with $\mu = 9\mu_0$; the upper half ($1<z<2$ cm) is air. Each turn carries $I = 2$ A, flowing along $+\hat{z}$ on the inner face ($r = a$), outward along the top, along $-\hat{z}$ on the outer face, and inward along the bottom.
>
> (a) Find $\mathbf{H}$ and $\mathbf{B}$ in both layers of the core and outside it. Why is $\mathbf{H}$ the same in the two layers while $\mathbf{B}$ is not?
>
> (b) Find the flux through one turn, the total flux linkage $N\Psi$, and the inductance $L$. Compare $L$ with that of an all-air core. If the current is increasing at $dI/dt = 50$ A/s, what is the voltage drop $V = L\,dI/dt$ across the winding?
>
> (c) Find the stored energy from $\tfrac12LI^2$ and from $\int\tfrac12\mu H^2\,dV$. What fraction is stored in the ferrite?
>
> (d) The toroid is rewound with 500 turns (same core, same current). By what factors do $\lvert\mathbf{B}\rvert$, the flux per turn, $N\Psi$ and $L$ change?
>
> *Source: SP18 Exam 2 #2, re-parameterized (two-layer core added).*

> [!hint]- Hint
> Ampère's law contains only the enclosed current, never $\mu$, so a circle of radius $r$ inside either layer gives the same $H$. Then $B = \mu H$ layer by layer, and the flux integral over the rectangular cross-section splits into two rectangles.

> [!solution]- Solution
> **Setup.** Symmetry gives $\mathbf{H} = H_\phi(r)\hat\phi$. Take an Ampère circle of radius $r$ at a fixed height, traversed along $+\hat\phi$ (counter-clockwise seen from $+z$); its flat disk then has $d\mathbf{S}$ along $+\hat{z}$.
>
> **(a)** For $a<r<b$ and $0<z<h$, the disk is pierced by the $N$ inner-face wires, each carrying $I$ along $+\hat{z}$: $H_\phi\cdot2\pi r = NI$. For $r<a$ nothing is enclosed, for $r>b$ the inner and outer faces cancel, and a circle above or below the core encloses no current. So
> $$
> \mathbf{H} = \frac{NI}{2\pi r}\hat\phi\ \ \text{(both layers)},\qquad \mathbf{B} = \begin{cases}9\mu_0\dfrac{NI}{2\pi r}\hat\phi & \text{ferrite}\\[6pt] \mu_0\dfrac{NI}{2\pi r}\hat\phi & \text{air}\end{cases},\qquad \mathbf{H} = \mathbf{B} = 0\ \text{outside the core}.
> $$
> At $I = 2$ A, $H$ falls from 6366 A/m at $r = a$ to 3183 A/m at $r = b$. *Why the layers differ:* $\mu$ never enters Ampère's law, so $H$ is fixed by the current alone; $\mu$ enters only through $B = \mu H$. The boundary conditions at the interface $z = 1$ cm ($\hat{n} = \hat{z}$) agree: $\mathbf{H}$ is tangential and continuous (no surface current), and $B_z = 0$ on both sides, so normal $\mathbf{B}$ is continuous too. Only tangential $\mathbf{B}$ jumps, by the factor 9.
>
> **(b)** By the right-hand rule along the current of a turn (up the inner face, then outward: $\hat{z}\times\hat{r} = \hat\phi$), the turn's $d\mathbf{S}$ is $\hat\phi\,dr\,dz$, along $\mathbf{B}$. Then
> $$
> \Psi = \int_0^{h/2}\!\!\int_a^b\frac{9\mu_0NI}{2\pi r}\,dr\,dz + \int_{h/2}^{h}\!\int_a^b\frac{\mu_0NI}{2\pi r}\,dr\,dz = (9+1)\,\frac h2\,\frac{\mu_0NI}{2\pi}\ln\frac ba = 5\,\frac{\mu_0Nh}{2\pi}\ln2\cdot I.
> $$
> With $\mu_0Nh/(2\pi) = 4\times10^{-6}$ Wb/A, $\Psi = (1.386\times10^{-5}\ \text{Wb/A})\,I = 2.77\times10^{-5}$ Wb per turn at 2 A, and $N\Psi = 2.77\times10^{-2}$ Wb. Hence
> $$
> L = \frac{N\Psi}{I} = 5\,\frac{\mu_0N^2h}{2\pi}\ln2 = 13.9\ \text{mH},
> $$
> five times the all-air value $\mu_0N^2h\ln(b/a)/(2\pi) = 2.77$ mH. The two layers sit side by side across the flux, so $L$ uses the area average $\mu_r = (9+1)/2 = 5$. The winding's drop is $V = L\,dI/dt = (13.86\ \text{mH})(50\ \text{A/s}) = 0.693$ V; the self-emf $-L\,dI/dt = -0.693$ V around the winding (in the direction of $I$) opposes the rise of the current, and the source must supply this drop.
>
> **(c)** $W = \tfrac12LI^2 = \tfrac12(13.86\ \text{mH})(2\ \text{A})^2 = 27.7$ mJ. Field route, with $dV = 2\pi r\,dr\,dz$ and $\tfrac12\mu H^2\cdot2\pi r = \mu(NI)^2/(4\pi r)$:
> $$
> W = \big(9\mu_0+\mu_0\big)\frac{(NI)^2}{4\pi}\cdot\frac h2\ln2,
> $$
> where the $9\mu_0$ term is the ferrite (24.95 mJ) and the $\mu_0$ term the air (2.77 mJ), totalling 27.7 mJ ✓. The ferrite holds 90% of the energy: at the same $H$, $w = \tfrac12\mu H^2$ is nine times larger there.
>
> **(d)** With $N$ halved at fixed $I$: $H$ and $\lvert\mathbf{B}\rvert$ ($\propto NI$) change by $\times0.5$; the flux per turn ($\propto B$) by $\times0.5$; $N\Psi$ by $0.5\times0.5 = 0.25$; and $L = N\Psi/I$ by $\times0.25$, the $N^2$ law.
>
> **Check:** the flux and energy routes give the same $L$ ($2W/I^2 = 13.9$ mH ✓), and $L>0$ with the right-hand-rule $d\mathbf{S}$, as a self-inductance must be.
>
> **Answer.** (a) $\mathbf{H} = \dfrac{NI}{2\pi r}\hat\phi$ in both layers (6366 A/m at $r = a$ to 3183 A/m at $r = b$); $\mathbf{B} = 9\mu_0\mathbf{H}$ in the ferrite and $\mu_0\mathbf{H}$ in air; zero outside. (b) $\Psi = 2.77\times10^{-5}$ Wb per turn, $N\Psi = 2.77\times10^{-2}$ Wb, $L = 13.9$ mH (5 × the air-core 2.77 mH); $V = 0.693$ V. (c) $W = 27.7$ mJ both ways, 90% of it in the ferrite. (d) $\lvert\mathbf{B}\rvert$ and $\Psi$ per turn $\times0.5$; $N\Psi$ and $L$ $\times0.25$.

### 15.10 Shorted parallel-plate line

> [!hard] Hard · parallel plates · current sheets · inductance
> Two thin conducting strips of width $W = 5$ cm ($0<z<W$) lie on the planes $y = 0$ and $y = d = 2$ mm and run from $x = 0$ to $x = \ell = 1$ m; they are shorted together at $x = \ell$. The gap between them is filled with a magnetodielectric film with $\mu = 3\mu_0$ and $\epsilon = 3\epsilon_0$; outside the gap is free space. A source at $x = 0$ drives $I = 10$ A along $+\hat{x}$ on the top strip ($y = d$), down through the short, and back along $-\hat{x}$ on the bottom strip ($y = 0$). Since $W\gg d$, treat each strip as part of an infinite sheet with a uniform surface current (ignore fringing).
>
> (a) Find $\mathbf{J}_s$ on each strip, and $\mathbf{H}$ between the strips and outside them, using $\mathbf{H} = \tfrac12\mathbf{J}_s\times\hat{n}$. Verify the boundary condition $\hat{n}\times(\mathbf{H}_1-\mathbf{H}_2) = \mathbf{J}_s$ at the top strip.
>
> (b) Find the flux $\Psi$ linked by the current path (state the direction of $d\mathbf{S}$ you use, and why), the inductance $L$, and $\mathcal{L}$.
>
> (c) Find the stored energy from $\int\tfrac12\mu H^2\,dV$ and compare it with $\tfrac12LI^2$. With $\mathcal{C} = \epsilon W/d$, verify that $\mathcal{L}\mathcal{C} = \mu\epsilon$.
>
> (d) The separation is halved, the width doubled and the current tripled. By what factors do $\lvert\mathbf{B}\rvert$ between the strips, $\Psi$, $L$ and $\mathcal{C}$ change?
>
> *Source: SP18 Exam 2 #3, re-parameterized (new orientation, a magnetodielectric fill, new numbers and a new scaling question).*

> [!hint]- Hint
> Between the strips the two sheet fields add; outside they cancel. The film changes $\mathbf{B} = \mu\mathbf{H}$, not $\mathbf{H}$. For the flux, the current path is a long thin rectangle in the $x$–$y$ plane: go around it in the direction of the current and use the right-hand rule for $d\mathbf{S}$.

> [!solution]- Solution
> **Setup.** Each strip carries $I$ spread over the width $W$: $J_s = I/W = 200$ A/m, so $\mathbf{J}_s = +200\,\hat{x}$ A/m on the top strip ($y = d$) and $-200\,\hat{x}$ A/m on the bottom strip ($y = 0$). For each sheet, $\hat{n}$ points from that sheet toward the field point ([[2-magnetostatics/13-current-sheets-solenoids-and-the-vector-potential|Lecture 13]]).
>
> **(a)** Between the strips ($0<y<d$) the field point is below the top sheet ($\hat{n} = -\hat{y}$) and above the bottom sheet ($\hat{n} = +\hat{y}$):
> $$
> \mathbf{H} = \tfrac12(200\,\hat{x})\times(-\hat{y}) + \tfrac12(-200\,\hat{x})\times\hat{y} = -100\,\hat{z} - 100\,\hat{z} = -200\,\hat{z}\ \text{A/m}.
> $$
> Above both strips both normals are $+\hat{y}$, giving $+100\,\hat{z}-100\,\hat{z} = 0$; below both, likewise 0. The film does not change $\mathbf{H}$, which Ampère's law fixes from the currents alone; $\mu$ enters only through $\mathbf{B} = \mu\mathbf{H}$ (as in Problem 15.9). So $\mathbf{B} = 3\mu_0\mathbf{H} = -7.54\times10^{-4}\,\hat{z}$ T in the film and zero outside. Boundary condition at the top strip, with medium 1 above (air), medium 2 between (the film) and $\hat{n} = +\hat{y}$ (from 2 into 1): $\hat{y}\times\big(0-(-200\,\hat{z})\big) = 200\,\hat{y}\times\hat{z} = 200\,\hat{x}$ A/m $= \mathbf{J}_s$ ✓.
>
> **(b)** Seen from $+z$, the current runs right along the top ($+\hat{x}$ at $y = d$), down the short, and left along the bottom: clockwise. The right-hand rule therefore gives $d\mathbf{S} = -\hat{z}\,dx\,dy$ over the rectangle $0<x<\ell$, $0<y<d$, and
> $$
> \Psi = \int_S\mathbf{B}\cdot d\mathbf{S} = (-7.54\times10^{-4}\,\hat{z})\cdot(-\hat{z})\,d\,\ell = \mu\frac IW\,d\,\ell = 1.51\times10^{-6}\ \text{Wb},
> $$
> positive, as a loop's own flux must be. $L = \Psi/I = \mu d\ell/W = 151$ nH and $\mathcal{L} = \mu d/W = 151$ nH/m.
>
> **(c)** The field is uniform in the volume $W\,d\,\ell$ of the film:
> $$
> W_m = \tfrac12\mu H^2\,(W\,d\,\ell) = \tfrac12(3)(4\pi\times10^{-7})(200)^2(0.05)(0.002)(1) = 7.54\ \mu\text{J},
> $$
> and $\tfrac12LI^2 = \tfrac12(150.8\ \text{nH})(10\ \text{A})^2 = 7.54\ \mu$J ✓. Also $\mathcal{C} = \epsilon W/d = 664$ pF/m, and $\mathcal{L}\mathcal{C} = \mu\dfrac dW\cdot\epsilon\dfrac Wd = \mu\epsilon = 9\mu_0\epsilon_0$: the geometric factors are exact inverses, so $1/\sqrt{\mathcal{L}\mathcal{C}} = 1/\sqrt{\mu\epsilon} = c/3 = 9.99\times10^7$ m/s.
>
> **(d)** The film still fills the thinner gap. $\lvert\mathbf{B}\rvert = \mu I/W$ changes by $3/2 = 1.5$. $\Psi = \mu(I/W)\,d\,\ell$ by $1.5\times\tfrac12 = 0.75$. $L = \mu d\ell/W$, which does not depend on $I$, by $\tfrac12\times\tfrac12 = 0.25$. $\mathcal{C} = \epsilon W/d$ by $2\times2 = 4$. The product $\mathcal{L}\mathcal{C}$ is unchanged ($0.25\times4 = 1$), as it must be.
>
> **Watch out:** $\Psi$ depends on $I$ but $L$ does not. And the flux surface is the rectangle bounded by the current path (normal along $\pm\hat{z}$), not the surface of a strip.
>
> **Answer.** (a) $\mathbf{J}_s = +200\,\hat{x}$ A/m (top), $-200\,\hat{x}$ A/m (bottom); $\mathbf{H} = -200\,\hat{z}$ A/m between the strips ($\mathbf{B} = -7.54\times10^{-4}\,\hat{z}$ T in the film), 0 outside. (b) $d\mathbf{S} = -\hat{z}\,dx\,dy$; $\Psi = 1.51\times10^{-6}$ Wb, $L = 151$ nH, $\mathcal{L} = 151$ nH/m. (c) $W_m = 7.54\ \mu$J both ways; $\mathcal{C} = 664$ pF/m and $\mathcal{L}\mathcal{C} = \mu\epsilon = 9\mu_0\epsilon_0$. (d) $\times1.5$, $\times0.75$, $\times0.25$, $\times4$.

### 15.11 Wire and rectangular loop

> [!hard] Hard · mutual inductance · vector potential · RL circuit
> A long straight wire on the $z$ axis carries a current $I(t)$ along $+\hat{z}$. A rectangular loop lies in the plane $y = 0$, with sides at $x = d_1 = 2$ cm and $x = d_2 = 8$ cm and at $z = 0$ and $z = h = 0.5$ m; free space. Take the loop's reference direction to be up ($+\hat{z}$) along the near side $x = d_1$.
>
> (a) Find the mutual inductance $M$ between the wire and the loop, stating the $d\mathbf{S}$ that goes with the reference direction.
>
> (b) The wire current ramps up at $dI/dt = 10^4$ A/s. Find the emf around the loop in the reference direction and the direction of the induced current. Is the loop attracted to the wire or repelled?
>
> (c) Rederive the emf from the wire's vector potential $\mathbf{A} = -\dfrac{\mu_0I}{2\pi}\ln\dfrac{r}{r_0}\,\hat{z}$ ($r_0$ an arbitrary reference radius): compute $\oint\mathbf{A}\cdot d\mathbf{l}$, show that $r_0$ drops out, and find the difference $E_z(d_1)-E_z(d_2)$ of the induced field $\mathbf{E} = -\partial\mathbf{A}/\partial t$ between the near and far sides.
>
> (d) The loop has resistance $R = 5\ \text{m}\Omega$ and self-inductance $L_{\text{loop}} = 1\ \mu$H, and carries no current when the ramp starts at $t = 0$. Find the loop current $i(t)$, its final value, and the time it takes to reach 99% of it.
>
> *Source: classic (wire–loop mutual inductance), extended with the vector-potential route and the loop's own inductance.*

> [!hint]- Hint
> On the loop, the wire's field is $\mu_0I/(2\pi x)$ along $+\hat{y}$ and varies with $x$ only, so integrate in strips $dS = h\,dx$. For (d), the loop's own self-emf $-L_{\text{loop}}\,di/dt$ joins the emf from (b) in KVL.

> [!solution]- Solution
> **(a) Setup.** In the half-plane $y = 0$, $x>0$, the wire's $\hat\phi$ is $\hat{z}\times\hat{x} = +\hat{y}$, so $\mathbf{B} = \dfrac{\mu_0I}{2\pi x}\hat{y}$. The reference circulation goes up the near side and then along $+\hat{x}$ on top; $\hat{z}\times\hat{x} = \hat{y}$, so $d\mathbf{S} = +\hat{y}\,dx\,dz$. Then
> $$
> \Psi = \int_0^h\!\!\int_{d_1}^{d_2}\frac{\mu_0I}{2\pi x}\,dx\,dz = \frac{\mu_0Ih}{2\pi}\ln\frac{d_2}{d_1},\qquad M = \frac{\Psi}{I} = \frac{\mu_0h}{2\pi}\ln4 = 1.39\times10^{-7}\ \text{H} = 0.139\ \mu\text{H}.
> $$
> **(b)** $\mathcal{E} = -\dfrac{d\Psi}{dt} = -M\dfrac{dI}{dt} = -(1.39\times10^{-7})(10^4) = -1.39$ mV in the reference direction. The minus sign means the induced current circulates the *other* way: **down** the near side, antiparallel to the wire's current. Lenz agrees: the $+\hat{y}$ flux grows, and the induced current makes $-\hat{y}$ flux inside the loop. Forces, with $i$ the size of the induced current: on the near side $ih\,(-\hat{z})\times\hat{y}\,B(d_1) = +ihB(d_1)\,\hat{x}$, away from the wire; the far side is pulled toward the wire but sits in a weaker field ($B\propto1/x$); the forces on the top and bottom sides cancel. The net force is
> $$
> \mathbf{F} = \frac{\mu_0Iih}{2\pi}\Big(\frac1{d_1}-\frac1{d_2}\Big)\hat{x},
> $$
> so the loop is **repelled**.
>
> **(c)** $\mathbf{A}$ is along $\hat{z}$, so only the two vertical sides contribute (on the top and bottom sides $d\mathbf{l}\perp\mathbf{A}$):
> $$
> \oint\mathbf{A}\cdot d\mathbf{l} = h\,A_z(d_1) - h\,A_z(d_2) = \frac{\mu_0Ih}{2\pi}\Big[-\ln\frac{d_1}{r_0}+\ln\frac{d_2}{r_0}\Big] = \frac{\mu_0Ih}{2\pi}\ln\frac{d_2}{d_1} = \Psi.
> $$
> $r_0$ cancels, as it must: adding a constant to $\mathbf{A}$ changes neither $\mathbf{B}$ nor $\oint\mathbf{A}\cdot d\mathbf{l}$. With $\Phi = 0$, $E_z = -\partial A_z/\partial t = \dfrac{\mu_0}{2\pi}\dfrac{dI}{dt}\ln\dfrac{r}{r_0}$, so
> $$
> E_z(d_1)-E_z(d_2) = \frac{\mu_0}{2\pi}\frac{dI}{dt}\ln\frac{d_1}{d_2} = -2.77\ \text{mV/m},\qquad \oint\mathbf{E}\cdot d\mathbf{l} = h\big[E_z(d_1)-E_z(d_2)\big] = -1.39\ \text{mV},
> $$
> the emf of (b) ✓.
>
> **(d)** KVL for the loop in the reference direction: the total emf, $-M\,dI/dt$ from the wire plus the self-emf $-L_{\text{loop}}\,di/dt$, drives the resistive drop $Ri$:
> $$
> L_{\text{loop}}\frac{di}{dt} + Ri = -1.39\ \text{mV},\qquad i(t) = i_\infty\big(1-e^{-t/\tau}\big),\quad \tau = \frac{L_{\text{loop}}}{R} = 0.2\ \text{ms},\quad i_\infty = \frac{-1.386\ \text{mV}}{5\ \text{m}\Omega} = -0.277\ \text{A}.
> $$
> So 0.277 A flows down the near side once the transient is over, and the current reaches 99% of that at $t = \tau\ln100 = 0.921$ ms. This is when [[2-magnetostatics/14-faradays-law-and-induced-emf|Lecture 14]]'s algebraic $i = \mathcal{E}/R$ becomes valid: after a few $\tau$, once the loop's own self-emf has died out.
>
> **Check:** two independent routes to the emf, the flux of $\mathbf{B}$ in (b) and the circulation of $\mathbf{A}$ (or of $\mathbf{E}$) in (c), agree. Units: $\mu_0h$ is (H/m)(m) = H ✓.
>
> **Answer.** (a) $d\mathbf{S} = +\hat{y}\,dx\,dz$; $M = (\mu_0h/2\pi)\ln4 = 0.139\ \mu$H. (b) $\mathcal{E} = -1.39$ mV: the induced current flows down the near side, and the loop is repelled. (c) $\oint\mathbf{A}\cdot d\mathbf{l} = (\mu_0Ih/2\pi)\ln(d_2/d_1)$, independent of $r_0$; $E_z(d_1)-E_z(d_2) = -2.77$ mV/m, giving the same $-1.39$ mV. (d) $i = -0.277\big(1-e^{-t/0.2\,\text{ms}}\big)$ A (0.277 A down the near side); 99% after 0.921 ms.

### 15.12 Coax with a magnetic sleeve

> [!hard] Hard · coax · magnetic energy · LC product
> A long coaxial cable has a solid inner conductor of radius $a = 1$ mm ($\mu_0$, current spread uniformly), a sleeve of magnetic dielectric with $\mu = 4\mu_0$ and $\epsilon = 4\epsilon_0$ filling $a<r<s$ with $s = 2$ mm, and air for $s<r<b$ with $b = 4$ mm. The outer conductor is a thin shell at $r = b$. The cable carries $I$ along $+\hat{z}$ on the inner conductor and back along $-\hat{z}$ on the outer one.
>
> (a) Find $\mathbf{H}$ and $\mathbf{B}$ in all regions. Which of them is continuous at $r = s$, and why?
>
> (b) For $I = 1$ A, find the magnetic energy per metre in each of the regions $r<a$, $a<r<s$, $s<r<b$, and the corresponding contributions $2W'/I^2$ to the inductance per unit length. Find the total $\mathcal{L}$ and the share of each region.
>
> (c) Find the external inductance $\mathcal{L}_{\text{ext}}$ (the flux in $a<r<b$) by the flux route, and check it against (b).
>
> (d) Find the capacitance per unit length $\mathcal{C}$ and the product $\mathcal{L}_{\text{ext}}\mathcal{C}$. Compare it with $\mu_0\epsilon_0$ and with $\mu\epsilon$ of the sleeve, and explain why the lecture's $\mathcal{L}\mathcal{C} = \mu\epsilon$ does not apply.
>
> *Source: original; extends the coax of the worked problem with a solid inner conductor and a magnetic sleeve.*

> [!hint]- Hint
> Ampère's law gives $H$ in every region without knowing $\mu$; $\mu$ enters only in $B$ and in $w = \tfrac12\mu H^2$. For $\mathcal{C}$, Gauss's law gives $D_r = \rho_l/(2\pi r)$ in both dielectric layers, and the voltages across the two layers add, like capacitors in series.

> [!solution]- Solution
> **Setup.** Cylindrical symmetry: $\mathbf{H} = H_\phi(r)\hat\phi$, from Ampère's law on circles of radius $r$. (The plain coax is worked in [[problems/coax-inductance-and-the-lc-product]].)
>
> **(a)**
> $$
> H_\phi = \begin{cases}\dfrac{Ir}{2\pi a^2} & r<a\\[6pt] \dfrac{I}{2\pi r} & a<r<b\\[6pt] 0 & r>b\end{cases}\qquad\qquad B_\phi = \mu H_\phi = \begin{cases}\mu_0H_\phi & r<a\\ 4\mu_0H_\phi & a<r<s\\ \mu_0H_\phi & s<r<b\end{cases}
> $$
> At $r = s$ the field is tangential to the interface and there is no surface current, so $\hat{n}\times(\mathbf{H}_1-\mathbf{H}_2) = 0$: $\mathbf{H}$ is continuous. $\mathbf{B}$ jumps by the factor 4, which is allowed because only *normal* $\mathbf{B}$ must be continuous, and here $B_r = 0$ on both sides. $\mathbf{H}$ is also continuous at $r = a$ (both forms give $I/(2\pi a) = 159$ A/m at 1 A).
>
> **(b)** With $dV = 2\pi r\,dr$ per metre:
> $$
> \begin{aligned}
> W'_1 &= \int_0^a\tfrac12\mu_0\Big(\frac{Ir}{2\pi a^2}\Big)^2 2\pi r\,dr = \frac{\mu_0I^2}{16\pi} = 2.50\times10^{-8}\ \text{J/m},\\
> W'_2 &= \int_a^s\tfrac12(4\mu_0)\Big(\frac{I}{2\pi r}\Big)^2 2\pi r\,dr = \frac{\mu_0I^2}{\pi}\ln2 = 2.77\times10^{-7}\ \text{J/m},\\
> W'_3 &= \int_s^b\tfrac12\mu_0\Big(\frac{I}{2\pi r}\Big)^2 2\pi r\,dr = \frac{\mu_0I^2}{4\pi}\ln2 = 6.93\times10^{-8}\ \text{J/m}.
> \end{aligned}
> $$
> So $\mathcal{L} = 2W'/I^2$ splits as $50 + 554.5 + 138.6 = 743$ nH/m: 6.7% inside the conductor, 74.6% in the sleeve, 18.7% in the air. The thin sleeve dominates because it sits where $H$ is strongest *and* stores four times the energy density at a given $H$.
>
> **(c)** The flux through an $r$–$z$ rectangle of unit length from $r = a$ to $r = b$, per ampere:
> $$
> \mathcal{L}_{\text{ext}} = \frac1I\int_a^b\mu H_\phi\,dr = \frac{4\mu_0}{2\pi}\ln\frac sa + \frac{\mu_0}{2\pi}\ln\frac bs = \frac{5\mu_0}{2\pi}\ln2 = 10^{-6}\ln2\ \text{H/m} = 0.693\ \mu\text{H/m},
> $$
> equal to $554.5 + 138.6$ nH/m from (b) ✓. The flux route needs extra care only inside the conductor, where the flux links just part of the current (Problem 15.7); the energy route handles that automatically.
>
> **(d)** A charge $\rho_l$ per metre on the inner conductor gives $D_r = \rho_l/(2\pi r)$ in both layers and $E_r = D_r/\epsilon$:
> $$
> V(a)-V(b) = \frac{\rho_l}{2\pi}\Big[\frac{\ln(s/a)}{4\epsilon_0} + \frac{\ln(b/s)}{\epsilon_0}\Big] = \frac{\rho_l}{2\pi\epsilon_0}\,(1.25\ln2),\qquad \mathcal{C} = \frac{2\pi\epsilon_0}{1.25\ln2} = 64.2\ \text{pF/m}.
> $$
> Then
> $$
> \mathcal{L}_{\text{ext}}\mathcal{C} = \frac{5\mu_0\ln2}{2\pi}\cdot\frac{2\pi\epsilon_0}{1.25\ln2} = 4\mu_0\epsilon_0 = 4.45\times10^{-17}\ \text{s}^2/\text{m}^2,
> $$
> four times the vacuum value but only a quarter of the sleeve's $\mu\epsilon = 16\mu_0\epsilon_0$. (The lecture's $\mathcal{L}$ assumes the currents flow on the conductor surfaces, so it is $\mathcal{L}_{\text{ext}}$ that belongs in this product.) The rule $\mathcal{L}\mathcal{C} = \mu\epsilon$ relies on the geometric factors of $\mathcal{L}$ and $\mathcal{C}$ being exact inverses, which holds when one homogeneous medium fills the line. Here the sleeve weights $\mathcal{L}$ by $\mu$ (the factor $4+1 = 5$) but $\mathcal{C}$ by $1/\epsilon$ in series (the factor $\tfrac14+1 = 1.25$), so the product is $5/1.25 = 4$, not $\mu_r\epsilon_r$ of either material. Correspondingly $1/\sqrt{\mathcal{L}_{\text{ext}}\mathcal{C}} = c/2 = 1.50\times10^8$ m/s, between the sleeve's $1/\sqrt{\mu\epsilon} = c/4 = 7.49\times10^7$ m/s and $c$ in air.
>
> **Check:** the flux and energy routes give the same $\mathcal{L}_{\text{ext}}$. With the same material in both layers, the same formulas give $\mathcal{L}_{\text{ext}}\mathcal{C} = \mu\epsilon$ exactly, recovering the lecture's result as the special case of a uniform fill.
>
> **Answer.** (a) $H_\phi = Ir/(2\pi a^2)$ for $r<a$, $I/(2\pi r)$ for $a<r<b$, 0 outside; $B_\phi = \mu H_\phi$ with $\mu = 4\mu_0$ in the sleeve; $\mathbf{H}$ is continuous at $r = s$, $\mathbf{B}$ jumps by 4. (b) $W' = 2.50\times10^{-8}$, $2.77\times10^{-7}$ and $6.93\times10^{-8}$ J/m; $\mathcal{L} = 50 + 554.5 + 138.6 = 743$ nH/m (6.7%, 74.6%, 18.7%). (c) $\mathcal{L}_{\text{ext}} = 10^{-6}\ln2$ H/m $= 0.693\ \mu$H/m. (d) $\mathcal{C} = 64.2$ pF/m; $\mathcal{L}_{\text{ext}}\mathcal{C} = 4\mu_0\epsilon_0 = 4.45\times10^{-17}$ s²/m², neither $\mu_0\epsilon_0$ nor $16\mu_0\epsilon_0$, because the fill is not uniform.

### Sources for this page
Course notes, Lecture 15: the long solenoid (15.1) and Example 1, the shorted coil (15.2), both with new numbers. Shao's Lecture 15 slides: the gauge-transformation challenge (15.4). Old exams: SP18 Exam 2 #1(v) (fields from potentials; 15.3, with new potentials), #2 (toroid flux and emf; 15.9, re-parameterized with a two-layer core) and #3 (shorted parallel-plate line with a scaling question; 15.10, re-parameterized with a new orientation, a magnetodielectric fill, new numbers and a new scaling question). Classic problems: the RL switch-on (15.6), the internal inductance of a round wire (15.7), coaxial solenoids (15.8, new numbers) and the wire–loop mutual inductance (15.11, extended with the vector-potential route and the loop's own inductance). Problems 15.5 and 15.12 are original; 15.12 extends the coax of the site's worked problem with a solid inner conductor and a magnetic sleeve.

*Previous: [[practice/14-faradays-law-and-induced-emf|Lecture 14 practice]] · next: [[practice/16-charge-conservation-and-displacement-current|Lecture 16 practice]] · [[practice/index|all practice]]*
