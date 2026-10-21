---
title: "Practice — Lecture 24: Group velocity and polarization"
description: "12 practice problems (5 easy, 3 medium, 4 hard) on phase and group velocity in a plasma, group delay and the spread between carriers, naming linear, circular and elliptical polarizations with the hand rule, building a phasor from a hand or from snapshots, H̃ and ⟨S⟩ of circular and elliptical waves, linear–circular bases, and an elliptically rotating sheet current, each with a worked solution and, for medium and hard, a folded hint."
tags: [practice, waves]
lecture: 24
---

*Practice for [[3-maxwell-and-waves/24-signal-transmission-and-circular-polarization|Lecture 24]] · concepts: [[concepts/group-velocity]] · [[concepts/wave-polarization]] · [[concepts/phasors]] · [[concepts/poynting-vector]] · all practice: [[practice/index|hub]] · by difficulty: [[practice/easy|easy]] · [[practice/medium|medium]] · [[practice/hard|hard]] · [[practice/topics|by topic]]*

Work each problem on paper first. Open the **hint** only when stuck, and the **solution** only after you have an answer you would hand in. Every answer here has been checked numerically; every handedness by rotating the field vector itself.

**Hand test used throughout** (Lecture 24 §4): read $\hat u$ from the exponent; where the exponent is 1, $\mathbf{E}(0) = \text{Re}\{\tilde{\mathbf{E}}\}$ and $\mathbf{E}(T/4) = -\text{Im}\{\tilde{\mathbf{E}}\}$; then $\hat u\cdot[\mathbf{E}(0)\times\mathbf{E}(T/4)]$ positive is right-handed, negative left-handed, zero linear.

## Easy

### 24.1 Crests and envelope in a plasma

> [!easy] Easy · group velocity · plasma frequency
> A laboratory plasma column 0.9 m long has plasma frequency $f_p = 4$ GHz. A 5 GHz carrier, amplitude-modulated by a pulse many carrier periods long (narrowband), crosses it. Use $c = 3\times10^8$ m/s.
>
> (a) Find $v_p$ and $v_g$, and check $v_pv_g = c^2$.
>
> (b) How long does the pulse take to cross the column? How long in vacuum?
>
> *Source: original.*

> [!solution]- Solution
> Plasma: $\omega^2 = \omega_p^2 + c^2\beta^2$, so $v_p = \omega/\beta = c/s$ and $v_g = d\omega/d\beta = c^2\beta/\omega = cs$, with
> $$
> s = \sqrt{1 - f_p^2/f^2} = \sqrt{1 - 0.64} = 0.6 .
> $$
> (a) $v_p = c/0.6 = 5\times10^8$ m/s, $v_g = 0.6c = 1.8\times10^8$ m/s; $v_pv_g = 9\times10^{16}$ m²/s² $= c^2$ ✓.
>
> (b) The pulse is the envelope, so it moves at $v_g$: $0.9/(1.8\times10^8) = 5$ ns, against $0.9/c = 3$ ns in vacuum. A crest needs only 1.8 ns.
>
> **Check:** $v_g<c<v_p$, as in any collisionless plasma above cut-off.
>
> **Answer.** (a) $v_p = 5\times10^8$ m/s $\approx1.67c$, $v_g = 1.8\times10^8$ m/s $= 0.6c$, product $9\times10^{16}$ m²/s² $= c^2$. (b) 5 ns (3 ns in vacuum).

### 24.2 Which velocity carries the message

> [!easy] Easy · multiple choice · group velocity · dispersion
> Which **one** statement is true?
>
> (a) In a lossless dielectric with $\epsilon_r = 4$, $\mu_r = 1$, a pulse's envelope travels at $c/2$ and its crests at $c/4$.
>
> (b) If $\beta(\omega)$ is a straight line, the medium is non-dispersive.
>
> (c) In a collisionless plasma above cut-off, the crests and the envelope cannot both travel slower than light.
>
> (d) Because $v_p>c$ in the ionosphere, a radio message crosses it faster than it would cross the same distance in vacuum.
>
> (e) The group velocity is $d\beta/d\omega$.
>
> *Source: original.*

> [!solution]- Solution
> **(c).** Differentiate $\omega^2 = \omega_p^2 + c^2\beta^2$: $2\omega\,d\omega = 2c^2\beta\,d\beta$, so $v_g = c^2\beta/\omega = c^2/v_p$ and $v_pv_g = c^2$. If one is below $c$ the other is above; here $v_g<c<v_p$.
>
> (a) False. $\beta = \omega\sqrt{\mu\epsilon}\propto\omega$: non-dispersive, $v_p = v_g = c/2$.
>
> (b) False. A line not through the origin, $\beta = \beta_0 + \omega/u$, has $v_g = u$ but $v_p = \omega/(\beta_0 + \omega/u)$, which varies with $\omega$. Non-dispersive needs $\beta\propto\omega$.
>
> (d) False. The message rides the envelope, at $v_g<c$: it arrives later than in vacuum.
>
> (e) False. $d\beta/d\omega = 1/v_g$, in s/m: a slowness, not a speed.
>
> **Answer.** (c).

### 24.3 Name four polarizations

> [!easy] Easy · polarization of waves · handedness
> Each field is a plane wave in a lossless medium. Give its direction of travel and its polarization (linear, circular or elliptical; for the last two, right- or left-handed).
>
> (a) $\mathbf{E} = 2\sin(\omega t - \beta z)\,\hat x + 2\cos(\omega t - \beta z)\,\hat y$
>
> (b) $\mathbf{E} = 3\cos(\omega t + \beta x)\,\hat y - 3\sin(\omega t + \beta x)\,\hat z$
>
> (c) $\mathbf{E} = 2\sin(\omega t - \beta y)\,\hat z - 2\sin(\omega t - \beta y)\,\hat x$
>
> (d) $\mathbf{E} = 4\cos(\omega t - \beta z)\,\hat x + 4\cos(\omega t - \beta z - \pi/3)\,\hat y$
>
> *Source: original.*

> [!hint]- Hint
> Freeze each field at the origin and compare $\omega t = 0$ with $\omega t = \pi/2$ (a quarter period later).

> [!solution]- Solution
> At the origin, with $\mathbf{E}(0)$ at $\omega t = 0$ and $\mathbf{E}(T/4)$ at $\omega t = \pi/2$:
>
> | | $\hat u$ | $\mathbf{E}(0)$ | $\mathbf{E}(T/4)$ | $\hat u\cdot[\mathbf{E}(0)\times\mathbf{E}(T/4)]$ | polarization |
> |---|---|---|---|---|---|
> | (a) | $+\hat z$ | $2\hat y$ | $2\hat x$ | $-4$ | left-circular |
> | (b) | $-\hat x$ | $3\hat y$ | $-3\hat z$ | $+9$ | right-circular |
> | (c) | $+\hat y$ | $0$ | $2(\hat z - \hat x)$ | $0$ | linear, along $\hat z - \hat x$ |
> | (d) | $+\hat z$ | $4\hat x + 2\hat y$ | $2\sqrt3\,\hat y$ | $+8\sqrt3$ | right-handed elliptical |
>
> (a), (b): equal amplitudes, a cosine and a sine, so circular. (c): one common time function, so $\mathbf{E}$ stays on one line. (d): equal amplitudes but 60° apart, not 90°: $\phi = -\pi/3$, $y$ lags $x$, right-handed elliptical (Lecture 24 §5).
>
> **Watch out:** (b) travels toward $-x$. With the thumb along $+x$ you would call it left.
>
> **Answer.** (a) $+z$, left-circular. (b) $-x$, right-circular. (c) $+y$, linear along $\hat z - \hat x$. (d) $+z$, right-handed elliptical.

### 24.4 True or false on one wave

> [!easy] Easy · true or false · circular polarization · elliptical polarization
> A plane wave in free space has $\tilde{\mathbf{E}} = \big(6\hat y + Be^{j\phi}\hat z\big)e^{+j\beta x}$ V/m, with real $B\ge0$ and $0\le\phi<2\pi$. True or false?
>
> (i) It is linear if $\phi = \pi$, for any $B$.
>
> (ii) It is linear if $B = 0$, for any $\phi$.
>
> (iii) It is right-circular if $(\phi, B) = (\pi/2, 6)$.
>
> (iv) It is right-circular if $(\phi, B) = (3\pi/2, 6)$.
>
> (v) It is left-handed elliptical if $(\phi, B) = (\pi/2, 3)$.
>
> (vi) It is circular if $B = 6$, for any $\phi$.
>
> *Source: SP18 Exam 3 #1(iii)–(iv) style, re-parameterized: travel along $-x$, components on $\hat y$ and $\hat z$, six statements.*

> [!solution]- Solution
> $e^{+j\beta x}$: $\hat u = -\hat x$. At $x = 0$: $\mathbf{E}(0) = 6\hat y + B\cos\phi\,\hat z$, $\mathbf{E}(T/4) = -B\sin\phi\,\hat z$, so
> $$
> \hat u\cdot[\mathbf{E}(0)\times\mathbf{E}(T/4)] = -\hat x\cdot(-6B\sin\phi\,\hat x) = 6B\sin\phi .
> $$
> (i) **True**: $\sin\pi = 0$; $\mathbf{E}$ stays along $6\hat y - B\hat z$.
>
> (ii) **True**: only $\hat y$ is left.
>
> (iii) **True**: $6B\sin\phi = 36>0$, equal amplitudes 90° apart.
>
> (iv) **False**: $\sin(3\pi/2) = -1$, left-circular.
>
> (v) **False**: $6\cdot3\cdot1 = 18>0$, right-handed elliptical.
>
> (vi) **False**: $\phi = 0$ or $\pi$ is linear, $\phi = \pi/4$ elliptical. Circular needs $B = 6$ **and** $\phi = \pi/2$ or $3\pi/2$.
>
> **Watch out:** for travel along $+x$, (iii) and (iv) swap.
>
> **Answer.** (i) T. (ii) T. (iii) T. (iv) F, left-circular. (v) F, right-handed elliptical. (vi) F.

### 24.5 The forgotten travel direction

> [!easy] Easy · find the error · handedness · phasor fields
> A student analyses $\tilde{\mathbf{E}} = 5(\hat x + j\hat y)e^{+j\beta z}$ V/m in free space:
>
> "This is $A\hat x + Be^{j\phi}\hat y$ with $A = B = 5$, $\phi = +\pi/2$, so by Lecture 24 §5 it is left-circular. Then $\tilde{\mathbf{H}} = \hat z\times\tilde{\mathbf{E}}/\eta_0 = 5(\hat y - j\hat x)e^{+j\beta z}/\eta_0$."
>
> Find the slip, fix it, and give the polarization, $\tilde{\mathbf{H}}$ and $\langle\mathbf{S}\rangle$ ($\eta_0 = 120\pi\ \Omega$).
>
> *Source: original.*

> [!solution]- Solution
> **Slip:** the travel direction. $e^{+j\beta z}$ travels toward $-z$; §5's rule is written for $+z$. Both conclusions inherit the error.
>
> **Fix.** $\hat u = -\hat z$. At $z = 0$: $\mathbf{E}(0) = 5\hat x$, $\mathbf{E}(T/4) = -5\hat y$, and $-\hat z\cdot(5\hat x\times(-5\hat y)) = +25>0$: **right-circular**.
> $$
> \tilde{\mathbf{H}} = \frac{-\hat z\times\tilde{\mathbf{E}}}{\eta_0} = \frac{5(j\hat x - \hat y)}{\eta_0}e^{+j\beta z}\ \text{A/m},\qquad \langle\mathbf{S}\rangle = -\frac{5^2 + 5^2}{2\eta_0}\hat z = -\frac{25}{\eta_0}\hat z .
> $$
> **Check:** the student's $\tilde{\mathbf{H}}$ is minus the correct one, so it sends $\langle\mathbf{S}\rangle$ toward $+z$, against the exponent — a red flag.
>
> **Answer.** The $-z$ travel was ignored. Right-circular; $\tilde{\mathbf{H}} = 5(j\hat x - \hat y)e^{j\beta z}/\eta_0$ A/m; $\langle\mathbf{S}\rangle = -(25/\eta_0)\hat z\approx-0.0663\,\hat z$ W/m².

## Medium

### 24.6 From two snapshots to a phasor

> [!medium] Medium · circular polarization · handedness · phasor fields
> A uniform plane wave at $f = 50$ MHz travels toward $-y$ in a lossless non-magnetic dielectric with $\epsilon_r = 4$. At the origin, $\mathbf{E} = 3\hat z$ V/m at $t = 0$ and $\mathbf{E} = 3\hat x$ V/m at $t = T/4$. Use $c = 3\times10^8$ m/s and $\eta_0 = 120\pi\ \Omega$.
>
> (a) Find $T$, $\lambda$ and $\beta$.
>
> (b) Is the wave right- or left-circular?
>
> (c) Write $\tilde{\mathbf{E}}(y)$ and $\mathbf{E}(y, t)$.
>
> (d) Find $\tilde{\mathbf{H}}(y)$ and $\langle\mathbf{S}\rangle$.
>
> *Source: Summer 2019 HE3 #3a style, re-parameterized: travel along $-y$ in a dielectric, new snapshots, with $\tilde{\mathbf{H}}$ and power added.*

> [!hint]- Hint
> Two snapshots a quarter period apart fix the phasor: $\text{Re}\{\tilde{\mathbf{E}}\} = \mathbf{E}(0)$ and $\text{Im}\{\tilde{\mathbf{E}}\} = -\mathbf{E}(T/4)$. For the hand, the thumb points along $-\hat y$.

> [!solution]- Solution
> **(a)** $v = c/\sqrt{\epsilon_r} = 1.5\times10^8$ m/s. $T = 1/f = 20$ ns, $\lambda = v/f = 3$ m, $\beta = 2\pi/\lambda = 2\pi/3$ rad/m. Also $\eta = \eta_0/2 = 60\pi\ \Omega$.
>
> **(b)** $\hat u\cdot[\mathbf{E}(0)\times\mathbf{E}(T/4)] = -\hat y\cdot(3\hat z\times3\hat x) = -9<0$: **left-circular**. (The right thumb along $-\hat y$ curls $\hat x\to\hat z$; the field turns $\hat z\to\hat x$.)
>
> **(c)** $\mathbf{E}(0) - j\mathbf{E}(T/4) = 3(\hat z - j\hat x)$; travel toward $-y$ brings $e^{+j\beta y}$:
> $$
> \tilde{\mathbf{E}} = 3(\hat z - j\hat x)e^{j2\pi y/3}\ \text{V/m},\qquad \mathbf{E} = 3\cos(\omega t + \tfrac{2\pi}{3}y)\,\hat z + 3\sin(\omega t + \tfrac{2\pi}{3}y)\,\hat x\ \text{V/m}.
> $$
> **(d)** With $-\hat y\times\hat z = -\hat x$ and $-\hat y\times\hat x = \hat z$:
> $$
> \tilde{\mathbf{H}} = \frac{-\hat y\times\tilde{\mathbf{E}}}{\eta} = \frac{3(-\hat x - j\hat z)}{60\pi}e^{j2\pi y/3} = -\frac{\hat x + j\hat z}{20\pi}e^{j2\pi y/3}\ \text{A/m},
> $$
> $$
> \langle\mathbf{S}\rangle = -\frac{3^2 + 3^2}{2\eta}\hat y = -\frac{3}{20\pi}\hat y\approx-0.0477\,\hat y\ \text{W/m}^2 .
> $$
> **Check:** $\mathbf{E}(0,0) = 3\hat z$ and $\mathbf{E}(0,T/4) = 3\hat x$ ✓; $\langle\mathbf{S}\rangle$ along $\hat u$ ✓.
>
> **Answer.** (a) $T = 20$ ns, $\lambda = 3$ m, $\beta = 2\pi/3$ rad/m. (b) Left-circular. (c) $\tilde{\mathbf{E}} = 3(\hat z - j\hat x)e^{j2\pi y/3}$ V/m; $\mathbf{E} = 3\cos(\omega t + 2\pi y/3)\,\hat z + 3\sin(\omega t + 2\pi y/3)\,\hat x$ V/m. (d) $\tilde{\mathbf{H}} = -(\hat x + j\hat z)e^{j2\pi y/3}/(20\pi)$ A/m; $\langle\mathbf{S}\rangle = -(3/20\pi)\,\hat y\approx-0.0477\,\hat y$ W/m².

### 24.7 Linear and circular building blocks

> [!medium] Medium · circular polarization · elliptical polarization · time-average power
> All waves travel toward $+z$ in free space; the common factor $e^{-j\beta z}$ is dropped. Use $\eta_0 = 120\pi\ \Omega$.
>
> (a) Write the linear wave $\tilde{\mathbf{E}} = 4\hat y$ V/m as a right-circular plus a left-circular wave. Compare its power with the sum of the two circular parts' powers.
>
> (b) A right-circular wave $3(\hat x - j\hat y)$ V/m and a left-circular wave $(\hat x + j\hat y)$ V/m travel together. Write the sum as $A\hat x + B\hat y$, name its polarization, and find the largest and smallest $\lvert\mathbf{E}\rvert$.
>
> (c) Find $\langle\mathbf{S}\rangle$ of the sum in (b) two ways: from its $\hat x$, $\hat y$ components and from its circular parts.
>
> *Source: original (the notes' bases, Lecture 24 §6).*

> [!hint]- Hint
> Solve $4\hat y = a(\hat x - j\hat y) + b(\hat x + j\hat y)$ component by component. In (b) the two circular vectors turn opposite ways at the same rate: they line up twice per period and oppose in between.

> [!solution]- Solution
> **(a)** $\hat x$: $a + b = 0$. $\hat y$: $-ja + jb = 4$. So $a = 2j$, $b = -2j$:
> $$
> 4\hat y = 2j(\hat x - j\hat y) - 2j(\hat x + j\hat y).
> $$
> Each part has $\lvert\tilde{\mathbf{E}}\rvert^2 = 8$, power $8/(2\eta_0) = 4/\eta_0$; together $8/\eta_0$. The linear wave: $16/(2\eta_0) = 8/\eta_0 = 1/(15\pi)\approx0.0212$ W/m² ✓.
>
> **(b)** $3(\hat x - j\hat y) + (\hat x + j\hat y) = 4\hat x - 2j\hat y$. At $z = 0$: $\mathbf{E} = 4\cos\omega t\,\hat x + 2\sin\omega t\,\hat y$, an ellipse with semi-axes 4 V/m along $\hat x$ and 2 V/m along $\hat y$. $\hat z\cdot(4\hat x\times2\hat y) = 8>0$: **right-handed elliptical**. $\lvert\mathbf{E}\rvert_{\max} = 3 + 1 = 4$ V/m, $\lvert\mathbf{E}\rvert_{\min} = 3 - 1 = 2$ V/m. The larger circular part sets the hand.
>
> **(c)** Components: $(4^2 + 2^2)/(2\eta_0) = 10/\eta_0$. Circular parts: $2\cdot3^2/(2\eta_0) + 2\cdot1^2/(2\eta_0) = 9/\eta_0 + 1/\eta_0 = 10/\eta_0$ ✓. Right and left circular waves are orthogonal, so their powers add like those of perpendicular linear components.
>
> **Answer.** (a) $4\hat y = 2j(\hat x - j\hat y) - 2j(\hat x + j\hat y)$; $4/\eta_0$ each, total $8/\eta_0 = 1/(15\pi)\approx0.0212$ W/m², the linear wave's power. (b) $4\hat x - 2j\hat y$, right-handed elliptical, $\lvert\mathbf{E}\rvert$ from 2 to 4 V/m. (c) $\langle\mathbf{S}\rangle = (10/\eta_0)\hat z = \hat z/(12\pi)\approx0.0265\,\hat z$ W/m², both ways.

### 24.8 Starting from H

> [!medium] Medium · circular polarization · phasor fields · time-average power
> In a lossless magnetic material with $\mu_r = 4$, $\epsilon_r = 1$, a plane wave has
> $$
> \mathbf{H} = 0.1\cos(\omega t - 2\pi x)\,\hat y + 0.1\sin(\omega t - 2\pi x)\,\hat z\ \text{A/m}\qquad(x\text{ in m}).
> $$
> Use $c = 3\times10^8$ m/s and $\eta_0 = 120\pi\ \Omega$.
>
> (a) Find $v$, $\eta$ and $f$.
>
> (b) Find $\tilde{\mathbf{H}}$, $\tilde{\mathbf{E}}$ and $\mathbf{E}(x,t)$.
>
> (c) Name the polarization. Does $\mathbf{H}$ turn the same way as $\mathbf{E}$?
>
> (d) Find $\langle\mathbf{S}\rangle$, and show that the instantaneous $\mathbf{S}$ is constant.
>
> *Source: original.*

> [!hint]- Hint
> $\tilde{\mathbf{H}} = \hat u\times\tilde{\mathbf{E}}/\eta$ inverts to $\tilde{\mathbf{E}} = \eta\,\tilde{\mathbf{H}}\times\hat u$. A sine picks up $-j$.

> [!solution]- Solution
> **(a)** $v = c/\sqrt{\mu_r\epsilon_r} = 1.5\times10^8$ m/s, $\eta = \eta_0\sqrt{\mu_r/\epsilon_r} = 240\pi\ \Omega$, $f = v\beta/2\pi = 150$ MHz ($\lambda = 1$ m).
>
> **(b)** $\hat u = +\hat x$. With $\hat y\times\hat x = -\hat z$ and $\hat z\times\hat x = \hat y$:
> $$
> \tilde{\mathbf{H}} = 0.1(\hat y - j\hat z)e^{-j2\pi x},\qquad \tilde{\mathbf{E}} = \eta\,\tilde{\mathbf{H}}\times\hat x = -24\pi(\hat z + j\hat y)e^{-j2\pi x}\ \text{V/m},
> $$
> $$
> \mathbf{E} = 24\pi\sin(\omega t - 2\pi x)\,\hat y - 24\pi\cos(\omega t - 2\pi x)\,\hat z\ \text{V/m}\quad(24\pi\approx75.4).
> $$
> **(c)** At $x = 0$: $\mathbf{E}(0) = -24\pi\hat z$, $\mathbf{E}(T/4) = 24\pi\hat y$, and $\hat x\cdot[(-\hat z)\times\hat y] = +1$: **right-circular**. $\mathbf{H}$ goes $0.1\hat y\to0.1\hat z$, $\hat x\cdot(\hat y\times\hat z) = +1$: right as well. $\mathbf{H} = \hat u\times\mathbf{E}/\eta$ is $\mathbf{E}$ turned 90° about $\hat u$, so the two always turn together.
>
> **(d)** $\langle\mathbf{S}\rangle = \tfrac12\eta\lvert\tilde{\mathbf{H}}\rvert^2\hat x = \tfrac12(240\pi)(0.01 + 0.01)\hat x = 2.4\pi\,\hat x$ W/m². Instantaneously $\mathbf{E}\perp\mathbf{H}$, both of constant length: $\mathbf{S} = (24\pi)(0.1)\hat x = 2.4\pi\,\hat x$ at every instant.
>
> **Check:** at $x = 0$, $t = 0$: $(-24\pi\hat z)\times(0.1\hat y) = +2.4\pi\,\hat x$, along the travel ✓.
>
> **Answer.** (a) $v = 1.5\times10^8$ m/s, $\eta = 240\pi\ \Omega$, $f = 150$ MHz. (b) $\tilde{\mathbf{H}} = 0.1(\hat y - j\hat z)e^{-j2\pi x}$ A/m; $\tilde{\mathbf{E}} = -24\pi(\hat z + j\hat y)e^{-j2\pi x}$ V/m; $\mathbf{E} = 24\pi[\sin(\omega t - 2\pi x)\,\hat y - \cos(\omega t - 2\pi x)\,\hat z]$ V/m. (c) Right-circular; $\mathbf{H}$ turns the same way. (d) $\langle\mathbf{S}\rangle = \mathbf{S}(t) = 2.4\pi\,\hat x\approx7.54\,\hat x$ W/m².

## Hard

### 24.9 Building a right-circular wave

> [!hard] Hard · circular polarization · phasor fields · time-average power
> A right-circular plane wave travels toward $-z$ in free space at $f = 75$ MHz; at the origin at $t = 0$, $\mathbf{E} = 6\hat y$ V/m. Write $\tilde{\mathbf{E}} = (A\hat x + B\hat y + C\hat z)e^{j(ax + by + cz)}$ (here $c$ is a template constant; light travels at $3\times10^8$ m/s). Use $\eta_0 = 120\pi\ \Omega$.
>
> (a) Find $a$, $b$, $c$.
>
> (b) Find $A$, $B$, $C$ and $\mathbf{E}(z,t)$.
>
> (c) Find $\tilde{\mathbf{H}}$ and $\langle\mathbf{S}\rangle$; compare with one linear component alone.
>
> (d) Find $\mathbf{E}$ at $t = 0$ at $z = \pm1$ m. When does a probe at $z = -1$ m first read $6\hat y$?
>
> *Source: Summer 2018 HE3 #3a, re-parameterized: travel along $-z$ instead of $+y$, 75 MHz, a 6 V/m snapshot along $\hat y$, with $\tilde{\mathbf{H}}$, the time-domain field and part (d) added.*

> [!hint]- Hint
> $\mathbf{E}(T/4)$ is $\pm6\hat x$. Pick the sign that makes $\hat u\cdot[\mathbf{E}(0)\times\mathbf{E}(T/4)]>0$ with $\hat u = -\hat z$, then $\tilde{\mathbf{E}}(0) = \mathbf{E}(0) - j\mathbf{E}(T/4)$.

> [!solution]- Solution
> **Setup.** $\lambda = 3\times10^8/(75\times10^6) = 4$ m, $\beta = 2\pi/\lambda = \pi/2$ rad/m, $T = 13.3$ ns. Travel toward $-z$ means $e^{+j\beta z}$.
>
> **(a)** $a = b = 0$, $c = +\pi/2$ rad/m.
>
> **(b)** $\mathbf{E}(T/4)$ is perpendicular to $\hat u$ and to $\mathbf{E}(0)$, with the same length: $\pm6\hat x$.
> $$
> -\hat z\cdot(6\hat y\times6\hat x) = -\hat z\cdot(-36\hat z) = +36>0\quad\text{for }+6\hat x .
> $$
> So $\tilde{\mathbf{E}}(0) = 6\hat y - 6j\hat x$: $(A, B, C) = (-6j, 6, 0)$ V/m. Equivalently $\tilde{\mathbf{E}} = -6j(\hat x + j\hat y)e^{j\pi z/2}$: the left-circular pattern for $+z$, hence right-circular for $-z$ ✓.
> $$
> \mathbf{E}(z,t) = 6\sin(\omega t + \tfrac\pi2z)\,\hat x + 6\cos(\omega t + \tfrac\pi2z)\,\hat y\ \text{V/m}.
> $$
> **(c)**
> $$
> \tilde{\mathbf{H}} = \frac{-\hat z\times\tilde{\mathbf{E}}}{\eta_0} = \frac{6\hat x + 6j\hat y}{120\pi}e^{j\pi z/2} = \frac{\hat x + j\hat y}{20\pi}e^{j\pi z/2}\ \text{A/m},
> $$
> $$
> \langle\mathbf{S}\rangle = -\frac{6^2 + 6^2}{2\eta_0}\hat z = -\frac{3}{10\pi}\hat z\approx-0.0955\,\hat z\ \text{W/m}^2,
> $$
> twice the $3/(20\pi)\approx0.0477$ W/m² of one 6 V/m linear component.
>
> **(d)** $\mathbf{E}(-1, 0) = 6\sin(-\pi/2)\,\hat x = -6\hat x$; $\mathbf{E}(1, 0) = +6\hat x$. At one instant the field tips trace a helix along $z$. The point $z = -1$ m is downstream: the wave reaches it $(1\text{ m})/c = 3.33$ ns $= T/4$ later, so the probe first reads $6\hat y$ at $t = 3.33$ ns.
>
> **Check:** $\mathbf{E}(0,0) = 6\hat y$, $\mathbf{E}(0,T/4) = 6\hat x$ ✓. At the origin, $t = 0$: $\mathbf{E}\times\mathbf{H} = 6\hat y\times\hat x/(20\pi)$ points along $-\hat z$ ✓.
>
> **Answer.** (a) $(a, b, c) = (0, 0, \pi/2)$ rad/m. (b) $(A, B, C) = (-6j, 6, 0)$ V/m; $\mathbf{E} = 6\sin(\omega t + \pi z/2)\,\hat x + 6\cos(\omega t + \pi z/2)\,\hat y$ V/m. (c) $\tilde{\mathbf{H}} = (\hat x + j\hat y)e^{j\pi z/2}/(20\pi)$ A/m; $\langle\mathbf{S}\rangle = -(3/10\pi)\,\hat z\approx-0.0955\,\hat z$ W/m², twice one component's. (d) $-6\hat x$ at $z = -1$ m, $+6\hat x$ at $z = +1$ m; the probe reads $6\hat y$ first at $t = 3.33$ ns.

### 24.10 A wave with a free phase

> [!hard] Hard · elliptical polarization · phasor fields · time-average power
> In free space,
> $$
> \mathbf{E} = E_1\cos(\omega t + \beta x)\,\hat y + E_2\cos(\omega t + \beta x + \phi)\,\hat z\ \text{V/m},
> $$
> with $E_1, E_2>0$ and $0\le\phi<2\pi$. Use $\eta_0 = 120\pi\ \Omega$.
>
> (a) Find the direction of travel, $\tilde{\mathbf{E}}$ and $\tilde{\mathbf{H}}$.
>
> (b) Find $\langle\mathbf{S}\rangle$. Does it depend on $\phi$?
>
> (c) For which $(E_1, E_2, \phi)$ is the wave linear, right-circular, left-circular? When it is elliptical, which $\phi$ make it right-handed?
>
> (d) Take $E_1 = 4$ V/m, $E_2 = 3$ V/m, $\phi = \pi/2$. Name the polarization, give the largest and smallest $\lvert\mathbf{E}\rvert$, and evaluate $\tilde{\mathbf{H}}$ and $\langle\mathbf{S}\rangle$.
>
> *Source: SP17 Exam 3 #4 style, re-parameterized: travel along $-x$ with $\hat y$, $\hat z$ components, a free phase on a cosine, the conditions asked directly instead of as multiple choice, and a numerical part.*

> [!hint]- Hint
> $\omega t + \beta x$ travels toward $-x$. Compute $\hat u\cdot[\mathbf{E}(0)\times\mathbf{E}(T/4)]$ at $x = 0$ for general $\phi$: one sign decides every case.

> [!solution]- Solution
> **(a)** $\omega t + \beta x$: toward $-\hat x$. With $-\hat x\times\hat y = -\hat z$ and $-\hat x\times\hat z = \hat y$:
> $$
> \tilde{\mathbf{E}} = (E_1\hat y + E_2e^{j\phi}\hat z)e^{j\beta x},\qquad \tilde{\mathbf{H}} = \frac{-\hat x\times\tilde{\mathbf{E}}}{\eta_0} = \frac{E_2e^{j\phi}\hat y - E_1\hat z}{\eta_0}e^{j\beta x}.
> $$
> **(b)** In $\tilde{\mathbf{E}}\times\tilde{\mathbf{H}}^*$ the mixed products are $\hat y\times\hat y$ and $\hat z\times\hat z$, both zero:
> $$
> \langle\mathbf{S}\rangle = \tfrac12\text{Re}\{\tilde{\mathbf{E}}\times\tilde{\mathbf{H}}^*\} = -\frac{E_1^2 + E_2^2}{2\eta_0}\hat x,
> $$
> independent of $\phi$.
>
> **(c)** At $x = 0$: $\mathbf{E}(0) = E_1\hat y + E_2\cos\phi\,\hat z$, $\mathbf{E}(T/4) = -E_2\sin\phi\,\hat z$, so
> $$
> \hat u\cdot[\mathbf{E}(0)\times\mathbf{E}(T/4)] = -\hat x\cdot(-E_1E_2\sin\phi\,\hat x) = E_1E_2\sin\phi .
> $$
> Linear: $\phi = 0$ or $\pi$, any amplitudes. Right-circular: $E_1 = E_2$, $\phi = \pi/2$. Left-circular: $E_1 = E_2$, $\phi = 3\pi/2$. Otherwise elliptical: right-handed for $0<\phi<\pi$, left-handed for $\pi<\phi<2\pi$.
>
> **(d)** $\tilde{\mathbf{E}} = (4\hat y + 3j\hat z)e^{j\beta x}$; $\sin\phi = 1>0$ and $E_1\neq E_2$: **right-handed elliptical**. At $x = 0$, $\mathbf{E} = 4\cos\omega t\,\hat y - 3\sin\omega t\,\hat z$: semi-axes 4 V/m along $\hat y$ (largest $\lvert\mathbf{E}\rvert$) and 3 V/m along $\hat z$ (smallest).
> $$
> \tilde{\mathbf{H}} = \frac{3j\hat y - 4\hat z}{120\pi}e^{j\beta x}\ \text{A/m},\qquad \langle\mathbf{S}\rangle = -\frac{16 + 9}{240\pi}\hat x = -\frac{5}{48\pi}\hat x\approx-0.0332\,\hat x\ \text{W/m}^2 .
> $$
> **Check:** at $x = 0$, $t = 0$: $\mathbf{E}\times\mathbf{H} = 4\hat y\times(-4\hat z)/\eta_0 = -16\hat x/\eta_0$, along $\hat u$ ✓.
>
> **Watch out:** "right for $\phi = \pi/2$" holds only for this geometry ($-x$ travel, $\hat y$ written first). Redo the sign for each new one.
>
> **Answer.** (a) Toward $-x$; $\tilde{\mathbf{E}} = (E_1\hat y + E_2e^{j\phi}\hat z)e^{j\beta x}$, $\tilde{\mathbf{H}} = (E_2e^{j\phi}\hat y - E_1\hat z)e^{j\beta x}/\eta_0$. (b) $\langle\mathbf{S}\rangle = -(E_1^2 + E_2^2)\hat x/(2\eta_0)$, independent of $\phi$. (c) Linear: $\phi = 0, \pi$. Right-circular: $E_1 = E_2$, $\phi = \pi/2$. Left-circular: $E_1 = E_2$, $\phi = 3\pi/2$. Otherwise elliptical, right-handed for $0<\phi<\pi$. (d) Right-handed elliptical, $\lvert\mathbf{E}\rvert$ from 3 to 4 V/m; $\tilde{\mathbf{H}} = (3j\hat y - 4\hat z)e^{j\beta x}/(120\pi)$ A/m; $\langle\mathbf{S}\rangle = -(5/48\pi)\,\hat x\approx-0.0332\,\hat x$ W/m².

### 24.11 Reading the ionosphere from two delays

> [!hard] Hard · group velocity · signal transmission · plasma frequency
> Two narrowband pulses, on 15 MHz and 20 MHz carriers, cross a uniform ionospheric layer (a collisionless plasma of unknown $f_p$ and thickness $L$) at normal incidence. Their envelopes take $\tau_1 = 1.00$ ms and $\tau_2 = 0.75$ ms. Use $c = 3\times10^8$ m/s; calculator allowed.
>
> (a) Write $\tau(f)$; find $f_p$ and $L$.
>
> (b) Find the electron density $N$ ($e = 1.602\times10^{-19}$ C, $m = 9.109\times10^{-31}$ kg, $\epsilon_0 = 8.854\times10^{-12}$ F/m).
>
> (c) How long does a carrier crest take to cross at each frequency?
>
> (d) The 20 MHz pulse spans 19.95–20.05 MHz. How much later does its lower edge arrive than its upper edge?
>
> (e) What happens to a 10 MHz pulse?
>
> *Source: original (the dual-frequency idea used to correct satellite signals for the ionosphere).*

> [!hint]- Hint
> $\tau = L/v_g$ with $v_g = c\sqrt{1 - f_p^2/f^2}$. In the ratio $\tau_1/\tau_2$ the thickness cancels, and squaring leaves an equation linear in $f_p^2$.

> [!solution]- Solution
> **(a)** $v_g = cs(f)$ with $s(f) = \sqrt{1 - f_p^2/f^2}$, so $\tau(f) = L/(c\,s(f))$. With $f$ in MHz,
> $$
> \Big(\frac{\tau_1}{\tau_2}\Big)^2 = \frac{1 - f_p^2/400}{1 - f_p^2/225} = \frac{16}{9}\ \Rightarrow\ f_p^2\Big(\frac{16}{225} - \frac{9}{400}\Big) = 7\ \Rightarrow\ f_p^2 = 144 .
> $$
> $f_p = 12$ MHz, so $s_1 = 0.6$, $s_2 = 0.8$ and $L = c\tau_1s_1 = (3\times10^8)(10^{-3})(0.6) = 180$ km (and $c\tau_2s_2 = 180$ km ✓).
>
> **(b)** $N = (2\pi f_p)^2m\epsilon_0/e^2\approx1.79\times10^{12}\ \text{m}^{-3}$.
>
> **(c)** $v_p = c/s$, so a crest needs $Ls/c$: 0.36 ms at 15 MHz, 0.48 ms at 20 MHz. Both beat vacuum (0.6 ms); the envelopes lose to it.
>
> **(d)** $\tau(19.95\text{ MHz}) - \tau(20.05\text{ MHz}) = 0.75106 - 0.74895$ ms $\approx2.1\ \mu$s. Same from the derivative:
> $$
> \Big\lvert\frac{d\tau}{df}\Big\rvert\Delta f = \frac{L}{c}\,\frac{f_p^2}{f^3s^3}\,\Delta f = (0.6\text{ ms})\,\frac{1.8\times10^{-8}\ \text{Hz}^{-1}}{0.512}\,(10^5\text{ Hz}) = 2.1\ \mu\text{s}.
> $$
> The pulse's finest features ($\approx1/\Delta f = 10\ \mu$s) blur by about a fifth: the envelope spreads.
>
> **(e)** $10<f_p = 12$ MHz: $\beta^2 = (\omega^2 - \omega_p^2)/c^2<0$, so no wave propagates in the layer (cut-off, Lecture 21). The pulse does not get through.
>
> **Check:** the higher carrier has the larger $v_g$ and arrives first ($\tau_2<\tau_1$) ✓; $v_pv_g = c^2$ at both frequencies ($5\times10^8\cdot1.8\times10^8$ and $3.75\times10^8\cdot2.4\times10^8$) ✓.
>
> **Answer.** (a) $\tau = L/(c\sqrt{1 - f_p^2/f^2})$; $f_p = 12$ MHz, $L = 180$ km. (b) $N\approx1.79\times10^{12}$ m⁻³. (c) 0.36 ms at 15 MHz, 0.48 ms at 20 MHz. (d) About 2.1 μs. (e) Below $f_p$: cut off, it does not cross the layer.

### 24.12 An elliptically rotating sheet current

> [!hard] Hard · current sheet radiation · elliptical polarization · energy balance
> A sheet on the plane $x = 0$ in free space carries
> $$
> \mathbf{J}_s(t) = 0.2\cos(\omega t)\,\hat y - 0.1\sin(\omega t)\,\hat z\ \text{A/m},\qquad f = 150\ \text{MHz}.
> $$
> Use $c = 3\times10^8$ m/s and $\eta_0 = 120\pi\ \Omega$.
>
> (a) Find $\tilde{\mathbf{E}}$ and $\tilde{\mathbf{H}}$ for $x>0$ and for $x<0$.
>
> (b) Name the polarization on each side.
>
> (c) Find $\langle\mathbf{S}\rangle$ on each side, and compare with the power the sheet supplies, $\langle-\mathbf{J}_s\cdot\mathbf{E}\rangle$ at $x = 0$.
>
> (d) Split the $x>0$ wave into a right- and a left-circular wave. Which dominates? Check that their powers add to (c).
>
> *Source: course notes Example 2 (Lecture 24 §7), re-parameterized: an elliptical current on the plane $x = 0$, with the power balance and a circular decomposition added.*

> [!hint]- Hint
> In phasors a sheet radiates $\tilde{\mathbf{E}} = -\tfrac{\eta_0}{2}\tilde{\mathbf{J}}_se^{-j\beta\lvert x\rvert}$ on both sides, with $\tilde{\mathbf{H}} = \hat u\times\tilde{\mathbf{E}}/\eta_0$. The rotation is the same on both sides; the thumb flips. For travel along $+x$, $(\hat y, \hat z)$ play the roles of $(\hat x, \hat y)$, so $\hat y - j\hat z$ is right-circular.

> [!solution]- Solution
> **Setup.** $\beta = 2\pi f/c = \pi$ rad/m; $\tilde{\mathbf{J}}_s = 0.2\hat y + 0.1j\hat z$ A/m (the $-\sin$ becomes $+j$).
>
> **(a)**
> $$
> \tilde{\mathbf{E}} = -60\pi\,\tilde{\mathbf{J}}_s\,e^{-j\pi\lvert x\rvert} = -(12\pi\hat y + 6\pi j\hat z)e^{-j\pi\lvert x\rvert}\ \text{V/m},
> $$
> $$
> \tilde{\mathbf{H}} = \frac{\pm\hat x\times\tilde{\mathbf{E}}}{\eta_0} = \pm(0.05j\hat y - 0.1\hat z)e^{-j\pi\lvert x\rvert}\ \text{A/m}\quad(x\gtrless0),
> $$
> the same as $\tfrac12\tilde{\mathbf{J}}_s\times\hat n$ with $\hat n = \pm\hat x$ away from the sheet.
>
> **(b)** At $x = 0^\pm$: $\mathbf{E}(0) = -12\pi\hat y$, $\mathbf{E}(T/4) = 6\pi\hat z$, $\mathbf{E}(0)\times\mathbf{E}(T/4) = -72\pi^2\hat x$. Unequal amplitudes 90° apart: elliptical. $x>0$ ($\hat u = \hat x$): negative, **left-handed**. $x<0$ ($\hat u = -\hat x$): positive, **right-handed**.
>
> **(c)** Each side: $\lvert\langle\mathbf{S}\rangle\rvert = \dfrac{(12\pi)^2 + (6\pi)^2}{240\pi} = 0.75\pi\approx2.36$ W/m², along $\pm\hat x$. The sheet supplies
> $$
> \langle-\mathbf{J}_s\cdot\mathbf{E}\rangle = \tfrac12\text{Re}\{-\tilde{\mathbf{J}}_s\cdot\tilde{\mathbf{E}}^*\} = \tfrac12(60\pi)(0.2^2 + 0.1^2) = 1.5\pi\ \text{W/m}^2 = 2(0.75\pi)\ \checkmark .
> $$
> **(d)** Without $e^{-j\pi x}$: $-12\pi\hat y - 6\pi j\hat z = a(\hat y - j\hat z) + b(\hat y + j\hat z)$ gives $a + b = -12\pi$, $b - a = -6\pi$: $a = -3\pi$ (right), $b = -9\pi$ (left). The left part dominates, as (b) found. Powers: $2(3\pi)^2/(240\pi) + 2(9\pi)^2/(240\pi) = 0.075\pi + 0.675\pi = 0.75\pi$ W/m² ✓. Semi-axes: $9\pi + 3\pi = 12\pi$ and $9\pi - 3\pi = 6\pi$ V/m ✓.
>
> **Check:** with equal current amplitudes this becomes the notes' Example 2 with the rotation reversed (left-circular for $x>0$, right-circular for $x<0$); here the opposite hands survive as ellipses.
>
> **Answer.** (a) $\tilde{\mathbf{E}} = -(12\pi\hat y + 6\pi j\hat z)e^{-j\pi\lvert x\rvert}$ V/m on both sides; $\tilde{\mathbf{H}} = \pm(0.05j\hat y - 0.1\hat z)e^{-j\pi\lvert x\rvert}$ A/m for $x\gtrless0$. (b) Left-handed elliptical for $x>0$, right-handed elliptical for $x<0$. (c) $\pm0.75\pi\,\hat x\approx\pm2.36\,\hat x$ W/m²; the sheet supplies $1.5\pi\approx4.71$ W/m², the sum. (d) $-3\pi(\hat y - j\hat z) - 9\pi(\hat y + j\hat z)$ V/m; the left part dominates; $0.075\pi + 0.675\pi = 0.75\pi$ W/m².

### Sources for this page
Course notes, Lecture 24: the group-velocity footnote with the site's $v_g$ table and derivation (24.1, 24.2, 24.11); the hand rule and the site's recipe (24.3–24.10, 24.12); the bases (24.7, 24.12); Example 2's rotating sheet (24.12); Example 3's power of a circular wave (24.8, 24.9). Old exams, re-parameterized as each source line says: SP18 Exam 3 #1(iii)–(iv) (24.4), Summer 2019 HE3 #3a (24.6), Summer 2018 HE3 #3a (24.9), SP17 Exam 3 #4 (24.10). Original: 24.1–24.3, 24.5, 24.7, 24.8, 24.11. No problem duplicates the site's worked problem [[problems/two-sheets-a-quarter-wave-apart|Two crossed sheets a quarter wave apart]]; 24.11 does not repeat practice 21.6 (there $N$ is given, here it is inferred from two delays).

*Previous: [[practice/23-imperfect-dielectrics-and-good-conductors|Lecture 23 practice]] · next: [[practice/25-reflection-and-transmission|Lecture 25 practice]] · [[practice/index|all practice]]*
