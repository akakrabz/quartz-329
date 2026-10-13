---
title: "Practice — Lecture 21: Monochromatic waves and phasors"
description: "12 practice problems (5 easy, 3 medium, 4 hard) on monochromatic waves and phasors: reading ω, f, T, β, λ, vₚ and the direction from an expression, snapshots versus records, the dispersion relations of light, sound and a collisionless plasma, phasor conversions with sines and d/dt → jω, plane-wave phasors and the e^(+jβz) trap, Ẽ ↔ H̃ by η and rotation on several axes, the monochromatic current sheet in phasor form, and time averages ⟨ab⟩ = ½Re{ÃB̃*} and ⟨S⟩ = ½Re{Ẽ × H̃*}, with folded hints and worked solutions."
tags: [practice, waves]
lecture: 21
---

*Practice for [[3-maxwell-and-waves/21-monochromatic-waves-and-phasor-notation|Lecture 21]] · concepts: [[concepts/phasors]] · [[concepts/dispersion-relation]] · [[concepts/plane-waves]] · [[concepts/poynting-vector]] · all practice: [[practice/index|hub]] · by difficulty: [[practice/easy|easy]] · [[practice/medium|medium]] · [[practice/hard|hard]] · [[practice/topics|by topic]]*

Work each problem on paper first. Open the **hint** only when stuck, and the **solution** only after you have an answer you would hand in. Every answer here has been checked numerically.

A handful of rules does almost every problem on this page. With the course's convention $a(t) = \text{Re}\{\tilde Ae^{j\omega t}\}$ (cosine reference, peak values), and for one plane wave travelling toward $\hat u$ in a lossless medium:
$$
\begin{aligned}
&\sin\to-j,\qquad \frac{d}{dt}\to j\omega,\qquad \tilde{\mathbf{E}} = \tilde{\mathbf{E}}_0\,e^{-j\beta\hat u\cdot\mathbf{r}},\qquad \tilde{\mathbf{H}} = \frac1\eta\,\hat u\times\tilde{\mathbf{E}},\\
&\langle ab\rangle = \tfrac12\text{Re}\{\tilde A\tilde B^*\},\qquad \langle\mathbf{S}\rangle = \tfrac12\text{Re}\{\tilde{\mathbf{E}}\times\tilde{\mathbf{H}}^*\}.
\end{aligned}
$$

## Easy

### 21.1 Reading two waves

> [!easy] Easy · wave parameters · monochromatic waves · dispersion relation
> (a) In a lossless, non-magnetic dielectric, $\mathbf{E} = 4\cos\big(5\pi\times10^8\,t + 2.5\pi y + \tfrac\pi3\big)\,\hat x$ V/m, with $t$ in seconds and $y$ in metres. Find $\omega$, $f$, $T$, $\beta$, $\lambda$, $v_p$, the direction of travel, and $\epsilon_r$ (use $c = 3\times10^8$ m/s).
> (b) For the same wave: at $t = 0$, where is the crest (the maximum of $E_x$) nearest the origin on the side $y>0$? After $t = 0$, when does a probe at $y = 0$ next record a crest? Show that the two answers fit the speed found in (a).
> (c) A sound wave in helium has the acoustic pressure $p = 20\cos(\pi x - 1000\pi t)$ Pa. Find $f$, $\lambda$, $v_p$ and the direction of travel. Then use the notes' dispersion relation for a monatomic gas, $\beta = \omega\sqrt{m/(\tfrac53k_BT_{\text{gas}})}$, to find the gas temperature $T_{\text{gas}}$ ($m = 6.65\times10^{-27}$ kg for a helium atom, $k_B = 1.381\times10^{-23}$ J/K).
>
> *Source: original (the notes' reading of a monochromatic wave, and their dispersion relation for a monatomic gas).*

> [!hint]- Hint
> The coefficient of $t$ is $\omega$ and the coefficient of the position is $\beta$. Only the *relative* sign of the two terms gives the direction: the same sign means travel toward minus. A cosine is even, so $\cos(\pi x - 1000\pi t) = \cos(1000\pi t - \pi x)$.

> [!solution]- Solution
> (a) The argument is $\omega t + \beta y + \phi$ with $\omega = 5\pi\times10^8\approx1.571\times10^9$ rad/s and $\beta = 2.5\pi\approx7.85$ rad/m. So $f = \omega/2\pi = 250$ MHz, $T = 1/f = 4$ ns, $\lambda = 2\pi/\beta = 0.8$ m and $v_p = \omega/\beta = 2\times10^8$ m/s (check: $\lambda f = 0.8\times2.5\times10^8$ m/s ✓). The $t$ and $y$ terms have the **same** sign, so the wave travels toward $-y$: a crest, where the argument is zero, sits at $y = -(\omega t + \pi/3)/\beta$, which decreases as $t$ grows. The $\pi/3$ is a phase and changes none of these numbers. With $\mu_r = 1$, $\epsilon_r = (c/v_p)^2 = 1.5^2 = 2.25$.
>
> (b) Snapshot at $t = 0$: crests where $2.5\pi y + \pi/3 = 2\pi n$, i.e. $y = 0.8n - 2/15$ m. The nearest one with $y>0$ is $n = 1$, at $y = 2/3\approx0.667$ m. Record at $y = 0$: crests where $5\pi\times10^8\,t + \pi/3 = 2\pi n$, i.e. $t = (4n - \tfrac23)$ ns; the next one after $t = 0$ is $n = 1$, at $t = 10/3\approx3.33$ ns. They fit: the crest at $y = 2/3$ m moves toward $-y$ at $2\times10^8$ m/s and reaches the probe after $(2/3)/(2\times10^8)$ s $= 3.33$ ns ✓.
>
> (c) $p = 20\cos(1000\pi t - \pi x)$: opposite signs, so the wave travels toward $+x$. $\omega = 1000\pi$ rad/s gives $f = 500$ Hz; $\beta = \pi$ rad/m gives $\lambda = 2$ m; $v_p = \omega/\beta = 1000$ m/s. The dispersion relation says $v_p = \omega/\beta = \sqrt{5k_BT_{\text{gas}}/(3m)}$, so
> $$
> T_{\text{gas}} = \frac{3mv_p^2}{5k_B} = \frac{3\,(6.65\times10^{-27})(10^6)}{5\,(1.381\times10^{-23})}\approx289\ \text{K}\quad(\text{about }16\ ^\circ\text{C}).
> $$
>
> **Watch out:** the plus sign in front of $2.5\pi y$ does not mean travel toward $+y$; the $t$ term has a plus sign too, and the two together mean $-y$.
>
> **Answer.** (a) $\omega = 5\pi\times10^8$ rad/s, $f = 250$ MHz, $T = 4$ ns, $\beta = 2.5\pi\approx7.85$ rad/m, $\lambda = 0.8$ m, $v_p = 2\times10^8$ m/s, toward $-\hat y$; $\epsilon_r = 2.25$. (b) Crest at $y = 2/3$ m at $t = 0$; the probe at $y = 0$ records it at $t = 10/3\approx3.33$ ns, which is $(2/3\ \text{m})/v_p$. (c) $f = 500$ Hz, $\lambda = 2$ m, $v_p = 1000$ m/s toward $+\hat x$; $T_{\text{gas}}\approx289$ K.

### 21.2 Phasors both ways

> [!easy] Easy · phasors · sine to cosine · phasor fields
> Use the course's convention, $a(t) = \text{Re}\{\tilde Ae^{j\omega t}\}$ with the cosine as reference and peak values.
> (a) Write the phasors of $i(t) = 4\sin(\omega t + 60^\circ)$ A and $v(t) = -10\cos(\omega t - 45^\circ)$ V, in polar and in rectangular form.
> (b) Add phasors to write $8\cos\omega t - 6\sin\omega t$ as a single cosine.
> (c) Go back to the time domain: $\tilde{\mathbf{E}} = (-5 + 12j)\,e^{j4\pi x}\,\hat z$ V/m and $\tilde{\mathbf{H}} = (2\hat x - 3j\hat y)\,e^{-j\beta z}$ A/m. Which way does each wave travel?
> (d) Use $d/dt\to j\omega$ to find the steady-state solution of $\dfrac{da}{dt} + 3a = 10\cos4t$ ($t$ in seconds).
>
> *Source: original (the conversion rules of Lecture 21 §3; part (d) is the ECE 210 move).*

> [!solution]- Solution
> (a) A sine is a cosine a quarter period late: $\sin(\omega t + 60^\circ) = \cos(\omega t - 30^\circ)$, so $\tilde I = 4e^{-j30^\circ} = 3.46 - 2j$ A. A minus sign is a factor $-1 = e^{j180^\circ}$: $\tilde V = -10e^{-j45^\circ} = 10e^{j135^\circ} = -7.07 + 7.07j$ V.
>
> (b) $8\cos\omega t\to8$ and $-6\sin\omega t\to-6(-j) = +6j$. The sum $8 + 6j$ has length 10 and angle $\tan^{-1}(6/8) = 36.9^\circ$ (first quadrant), so $8\cos\omega t - 6\sin\omega t = 10\cos(\omega t + 36.9^\circ)$.
>
> (c) $-5 + 12j$ lies in the **second** quadrant: length 13, angle $180^\circ - 67.4^\circ = 112.6^\circ$. (A calculator's $\tan^{-1}(12/(-5)) = -67.4^\circ$ points into the wrong quadrant.) Multiply by $e^{j\omega t}$ and take the real part:
> $$
> \mathbf{E} = 13\cos(\omega t + 4\pi x + 112.6^\circ)\,\hat z = \big[-5\cos(\omega t + 4\pi x) - 12\sin(\omega t + 4\pi x)\big]\,\hat z\ \text{V/m},
> $$
> travelling toward $-x$, because of the $e^{+j4\pi x}$. For $\tilde{\mathbf{H}}$, component by component, $2\to2\cos$ and $-3j\to+3\sin$:
> $$
> \mathbf{H} = 2\cos(\omega t - \beta z)\,\hat x + 3\sin(\omega t - \beta z)\,\hat y\ \text{A/m},
> $$
> travelling toward $+z$.
>
> (d) With $a = \text{Re}\{\tilde Ae^{j4t}\}$ the equation becomes $(j4 + 3)\tilde A = 10$, so
> $$
> \tilde A = \frac{10}{3 + 4j} = \frac{10(3 - 4j)}{25} = 1.2 - 1.6j = 2e^{-j53.1^\circ},\qquad a(t) = 2\cos(4t - 53.1^\circ).
> $$
> Check: with $\theta = 4t - 53.1^\circ$, $da/dt + 3a = -8\sin\theta + 6\cos\theta = 10\cos(\theta + 53.1^\circ) = 10\cos4t$ ✓.
>
> **Watch out:** taking $\text{Re}\{-5 + 12j\} = -5$ first and multiplying by $\cos(\omega t + 4\pi x)$ afterwards keeps the $-5\cos$ and loses the $-12\sin$.
>
> **Answer.** (a) $\tilde I = 4e^{-j30^\circ} = 3.46 - 2j$ A; $\tilde V = 10e^{j135^\circ} = -7.07 + 7.07j$ V. (b) $10\cos(\omega t + 36.9^\circ)$. (c) $\mathbf{E} = 13\cos(\omega t + 4\pi x + 112.6^\circ)\,\hat z$ V/m, toward $-x$; $\mathbf{H} = 2\cos(\omega t - \beta z)\,\hat x + 3\sin(\omega t - \beta z)\,\hat y$ A/m, toward $+z$. (d) $a(t) = 2\cos(4t - 53.1^\circ)$.

### 21.3 Phasor pitfalls, true or false

> [!easy] Easy · true or false · phasors · time average
> True or false? (Cosine reference, peak values, $\eta_0 = 120\pi\ \Omega$.)
>
> (a) The phasor of $5\sin\omega t$ is $5j$.
>
> (b) If $a(t)$ has the phasor $\tilde A$, then $a(t)^2$ has the phasor $\tilde A^2$.
>
> (c) $\tilde{\mathbf{E}} = 2e^{+j5y}\,\hat z$ V/m describes a wave travelling toward $-y$.
>
> (d) For $a(t) = 4\cos(\omega t + 70^\circ)$ and $b(t) = 3\cos(\omega t - 20^\circ)$, the time average of $a(t)\,b(t)$ is zero.
>
> (e) The phasor $\tilde{\mathbf{E}}(z) = 3e^{-j\beta z}\,\hat x$ V/m is the electric field at $t = 0$.
>
> (f) In free space, $\tilde{\mathbf{E}} = 20e^{-j\beta z}\,\hat x$ V/m carries $\langle\mathbf{S}\rangle = \dfrac{400}{120\pi}\,\hat z\approx1.06\,\hat z$ W/m².
>
> (g) For a single plane wave in a lossless medium, $\tilde{\mathbf{H}}$ has the same phase as $\tilde{\mathbf{E}}$ at every point.
>
> *Source: original.*

> [!solution]- Solution
> (a) **False.** $\sin\omega t = \cos(\omega t - 90^\circ)$, so the phasor is $5e^{-j90^\circ} = -5j$. With $5j$ you get $\text{Re}\{5je^{j\omega t}\} = -5\sin\omega t$: the right shape with the wrong sign.
>
> (b) **False.** $a^2 = A^2\cos^2(\omega t + \theta) = \tfrac12A^2 + \tfrac12A^2\cos(2\omega t + 2\theta)$: a constant plus a part at $2\omega$, and nothing at $\omega$. A product has no phasor; $\text{Re}\{\tilde A^2e^{j\omega t}\} = A^2\cos(\omega t + 2\theta)$ is a different signal. What phasors *can* give is the average, $\langle a^2\rangle = \tfrac12\lvert\tilde A\rvert^2$.
>
> (c) **True.** Restore the time factor: $e^{j5y}e^{j\omega t} = e^{j(\omega t + 5y)}$, with the same sign on both terms, so the wave travels toward $-y$. A minus sign in the exponent means travel toward plus, and this one is a plus.
>
> (d) **True.** $\langle ab\rangle = \tfrac12\text{Re}\{\tilde A\tilde B^*\} = \tfrac12(4)(3)\cos\big(70^\circ - (-20^\circ)\big) = 6\cos90^\circ = 0$. Two sinusoids in quadrature have a zero average product.
>
> (e) **False.** A phasor is a complex amplitude, not a field. The field at $t = 0$ is its real part, $\text{Re}\{3e^{-j\beta z}\}\,\hat x = 3\cos(\beta z)\,\hat x$; minus its imaginary part, $3\sin(\beta z)\,\hat x$, is the field a quarter period later. One complex number holds both snapshots.
>
> (f) **False.** The $\tfrac12$ is missing: $\langle\mathbf{S}\rangle = \lvert\tilde{\mathbf{E}}_0\rvert^2/(2\eta_0)\,\hat z = \dfrac{400}{240\pi}\,\hat z\approx0.531\,\hat z$ W/m². Phasor magnitudes are peak values, and $\langle\cos^2\rangle = \tfrac12$.
>
> (g) **True.** $\tilde{\mathbf{H}} = \hat u\times\tilde{\mathbf{E}}/\eta$, with a real $\eta$ and a real $\hat u$, so any complex factor of $\tilde{\mathbf{E}}$ rides along unchanged. In a lossy medium (Lecture 22) $\eta$ is complex and $\mathbf{H}$ lags $\mathbf{E}$.
>
> **Answer.** (a) F, (b) F, (c) T, (d) T, (e) F, (f) F, (g) T.

### 21.4 Which electric field

> [!easy] Easy · multiple choice · phasor fields · intrinsic impedance
> A plane wave travels in a lossless magnetic material with $\epsilon = \epsilon_0$ and $\mu = 9\mu_0$. Its magnetic field is $\mathbf{H} = \text{Re}\{-0.4j\,e^{j(\omega t + \beta z)}\}\,\hat y$ A/m. Which is its electric field, in V/m? (Use $\eta_0 = 120\pi\ \Omega$.)
>
> (a) $\mathbf{E} = -144\pi\sin(\omega t + \beta z)\,\hat x$
>
> (b) $\mathbf{E} = +144\pi\sin(\omega t + \beta z)\,\hat x$
>
> (c) $\mathbf{E} = -144\pi\cos(\omega t + \beta z)\,\hat x$
>
> (d) $\mathbf{E} = -48\pi\sin(\omega t + \beta z)\,\hat x$
>
> (e) None of these.
>
> *Source: SP17 Exam 3 #2(iii), re-parameterized: a material with $\mu = 9\mu_0$, an $\mathbf{H}$ written with a $-j$ and travelling toward $-z$, and new options.*

> [!hint]- Hint
> Three readings first: $\eta$ of this material, what the $-j$ does to $\mathbf{H}$, and which way $e^{+j\beta z}$ travels. Then $\tilde{\mathbf{E}} = \eta\,\tilde{\mathbf{H}}\times\hat u$.

> [!solution]- Solution
> **(a).** Three readings, then one cross product.
> - $\eta = \sqrt{\mu/\epsilon} = \eta_0\sqrt{\mu_r/\epsilon_r} = 3\eta_0 = 360\pi\approx1131\ \Omega$.
> - $\tilde{\mathbf{H}} = -0.4j\,e^{j\beta z}\,\hat y$ A/m, so $\mathbf{H} = 0.4\sin(\omega t + \beta z)\,\hat y$ A/m: the $-j$ is a sine.
> - $e^{+j\beta z}$ travels toward $-z$: $\hat u = -\hat z$.
>
> Then, with $\hat y\times(-\hat z) = -\hat x$,
> $$
> \tilde{\mathbf{E}} = \eta\,\tilde{\mathbf{H}}\times\hat u = 360\pi\,(-0.4j)\,e^{j\beta z}\,(-\hat x) = 144\pi j\,e^{j\beta z}\,\hat x,
> $$
> and since $\text{Re}\{je^{j(\omega t + \beta z)}\} = -\sin(\omega t + \beta z)$, $\mathbf{E} = -144\pi\sin(\omega t + \beta z)\,\hat x\approx-452\sin(\omega t + \beta z)\,\hat x$ V/m.
>
> **Check:** $\mathbf{E}\times\mathbf{H}\propto(-\hat x)\times\hat y\,\sin^2(\omega t + \beta z) = -\hat z\,\sin^2(\omega t + \beta z)$, along the travel ✓; $\lvert\mathbf{E}\rvert/\lvert\mathbf{H}\rvert = 360\pi = \eta$ ✓.
>
> Why the others are wrong:
> - (b) is the result of rotating with $\hat u = +\hat z$: reading $e^{+j\beta z}$ as travel toward $+z$, or computing $\eta\,\hat u\times\tilde{\mathbf{H}}$ instead of $\eta\,\tilde{\mathbf{H}}\times\hat u$. Its $\mathbf{E}\times\mathbf{H}$ points along $+\hat z$, against the wave.
> - (c) drops the $-j$, as if $\mathbf{H}$ were $0.4\cos(\omega t + \beta z)\,\hat y$. Its $\mathbf{E}$ is a quarter period out of step with the given $\mathbf{H}$, so the pair would carry no average power.
> - (d) uses $\eta_0$: $0.4\times120\pi = 48\pi$ is the free-space amplitude. In this material $\eta = 3\eta_0$ (and $v_p = c/3$).
>
> **Answer.** (a): $\mathbf{E} = -144\pi\sin(\omega t + \beta z)\,\hat x\approx-452\sin(\omega t + \beta z)\,\hat x$ V/m.

### 21.5 The power that flowed backward

> [!easy] Easy · find the error · time average · phasor fields
> A plane wave in free space has $\tilde{\mathbf{E}} = (6\hat x + 8j\hat y)\,e^{-j2\pi z}$ V/m. A student finds its time-average power density:
>
> "The wave travels toward $+z$, so $\tilde{\mathbf{H}} = \dfrac{1}{\eta_0}\,\hat z\times\tilde{\mathbf{E}} = \dfrac{1}{\eta_0}(6\hat y - 8j\hat x)\,e^{-j2\pi z}$. Then
> $$
> \tilde{\mathbf{E}}\times\tilde{\mathbf{H}} = \frac{1}{\eta_0}\big[36\,\hat x\times\hat y + (8j)(-8j)\,\hat y\times\hat x\big]e^{-j4\pi z} = \frac{36 - 64}{\eta_0}\,e^{-j4\pi z}\,\hat z,\qquad \langle\mathbf{S}\rangle = \tfrac12\text{Re}\{\tilde{\mathbf{E}}\times\tilde{\mathbf{H}}\} = -\frac{14}{\eta_0}\cos(4\pi z)\,\hat z .
> $$
> At $z = 0$ this is $-0.0371\,\hat z$ W/m², so the wave carries power toward $-z$."
>
> Find the slip, correct it, and give $\langle\mathbf{S}\rangle$ ($\eta_0 = 120\pi\ \Omega$).
>
> *Source: original.*

> [!solution]- Solution
> **The slip:** the conjugate is missing. The average is $\tfrac12\text{Re}\{\tilde{\mathbf{E}}\times\tilde{\mathbf{H}}^*\}$. The student's $\tilde{\mathbf{H}}$ is right. Without the conjugate, though, the two factors $e^{-j2\pi z}$ multiply to $e^{-j4\pi z}$ instead of cancelling, and the $\hat y$ component, whose phasor carries a $j$, contributes $(8j)^2 = -64$ instead of $\lvert8j\rvert^2 = +64$. (For one wave, $\tilde{\mathbf{E}}\times\tilde{\mathbf{H}} = (\tilde{\mathbf{E}}\cdot\tilde{\mathbf{E}}/\eta)\,\hat u$, and here $\tilde{\mathbf{E}}_0\cdot\tilde{\mathbf{E}}_0 = 36 + (8j)^2 = -28$.)
>
> **Fix:** $\tilde{\mathbf{H}}^* = \dfrac{1}{\eta_0}(6\hat y + 8j\hat x)\,e^{+j2\pi z}$, so
> $$
> \tilde{\mathbf{E}}\times\tilde{\mathbf{H}}^* = \frac{1}{\eta_0}\big[36\,\hat x\times\hat y + (8j)(8j)\,\hat y\times\hat x\big] = \frac{36 + 64}{\eta_0}\,\hat z,\qquad \langle\mathbf{S}\rangle = \frac{50}{\eta_0}\,\hat z = \frac{5}{12\pi}\,\hat z\approx0.133\,\hat z\ \text{W/m}^2 .
> $$
> The $\hat x$ part carries $36/(2\eta_0)\approx0.048$ W/m² and the $\hat y$ part $64/(2\eta_0)\approx0.085$ W/m². Perpendicular components add their powers whatever the phase between them: $\lvert\tilde{\mathbf{E}}_0\rvert^2 = 36 + 64 = 100$ (V/m)².
>
> **Three red flags in the student's result:** a time average that changes with $z$ in a lossless medium (energy would have to pile up or vanish somewhere); power flowing against the direction of travel the student had just identified; and component powers that subtract.
>
> **Answer.** The conjugate on $\tilde{\mathbf{H}}$ was dropped. Correct: $\langle\mathbf{S}\rangle = \tfrac12\text{Re}\{\tilde{\mathbf{E}}\times\tilde{\mathbf{H}}^*\} = \dfrac{50}{\eta_0}\,\hat z = \dfrac{5}{12\pi}\,\hat z\approx0.133\,\hat z$ W/m², the same at every $z$.

## Medium

### 21.6 Radio waves in a plasma

> [!medium] Medium · dispersion relation · plasma frequency · phase velocity
> A layer of the ionosphere is modelled as a uniform collisionless plasma with $N = 4.47\times10^{11}$ free electrons per m³. Use $e = 1.602\times10^{-19}$ C, $m = 9.109\times10^{-31}$ kg, $\epsilon_0 = 8.854\times10^{-12}$ F/m and $c = 3\times10^8$ m/s.
> (a) Find $\omega_p$ and $f_p$.
> (b) Which of the frequencies 4 MHz, 10 MHz and 100 MHz can travel through the layer?
> (c) For the 10 MHz wave, find $\beta$, $\lambda$ and $v_p$ inside the layer, and compare $\lambda$ with its free-space value.
> (d) Since $v_p>c$, does a 10 MHz signal cross a 150 km thick layer faster than light would? A signal travels at the group velocity $v_g = d\omega/d\beta$. Find $v_g$ from the dispersion relation, check that $v_pv_g = c^2$, and compare the crossing times.
>
> *Source: original (the notes' third dispersion relation, with new numbers).*

> [!hint]- Hint
> $\beta = \tfrac1c\sqrt{\omega^2 - \omega_p^2} = \tfrac\omega c\sqrt{1 - f_p^2/f^2}$. With the $f_p$ of (a), the square root at 10 MHz is a 3-4-5 number. For (d), differentiate $\omega^2 = \omega_p^2 + \beta^2c^2$.

> [!solution]- Solution
> **Setup.** The notes' plasma relation, $\beta = \tfrac1c\sqrt{\omega^2 - \omega_p^2}$ with $\omega_p^2 = Ne^2/(m\epsilon_0)$, decides everything. A travelling wave needs a real $\beta$, so $\omega>\omega_p$.
>
> **(a)**
> $$
> \omega_p = \sqrt{\frac{Ne^2}{m\epsilon_0}} = \sqrt{\frac{(4.47\times10^{11})(1.602\times10^{-19})^2}{(9.109\times10^{-31})(8.854\times10^{-12})}} = 3.77\times10^7\ \text{rad/s},\qquad f_p = \frac{\omega_p}{2\pi} = 6.00\ \text{MHz}.
> $$
> The shortcut $f_p\approx8.98\sqrt N$ Hz gives the same.
>
> **(b)** At 4 MHz, below $f_p$, $\beta^2<0$: there is no real $\beta$ and no travelling wave, and the layer turns the wave back. 10 MHz and 100 MHz are above $f_p$ and travel through.
>
> **(c)** At 10 MHz, $\sqrt{1 - (6/10)^2} = 0.8$ and $\omega/c = 2\pi\times10^7/(3\times10^8) = \pi/15$ rad/m, so
> $$
> \beta = 0.8\cdot\frac{\pi}{15} = \frac{4\pi}{75}\approx0.168\ \text{rad/m},\qquad \lambda = \frac{2\pi}{\beta} = 37.5\ \text{m},\qquad v_p = \lambda f = 3.75\times10^8\ \text{m/s} = 1.25c .
> $$
> In free space $\lambda = c/f = 30$ m. Inside the plasma the wavelength is longer, because the crests move faster. (At 100 MHz, $f_p^2/f^2 = 0.0036$ and $v_p = 1.0018c$: almost vacuum.)
>
> **(d)** Differentiate $\omega^2 = \omega_p^2 + \beta^2c^2$: $2\omega\,d\omega = 2\beta c^2\,d\beta$, so
> $$
> v_g = \frac{d\omega}{d\beta} = \frac{\beta c^2}{\omega} = \frac{c^2}{v_p} = c\sqrt{1 - \frac{f_p^2}{f^2}} = 0.8c = 2.4\times10^8\ \text{m/s},
> $$
> and $v_pv_g = (3.75\times10^8)(2.4\times10^8) = 9\times10^{16}$ m²/s² $= c^2$ ✓. The signal crosses 150 km in $(150\times10^3)/(2.4\times10^8) = 0.625$ ms, later than light's 0.500 ms. Nothing physical travels at $v_p$: a pure cosine has no start and no end to carry a message, and its crests are a pattern, not a thing.
>
> **Check:** $\lambda f = 37.5\times10^7$ m/s $= v_p$ ✓; and as $f$ grows the relation approaches the light line $\beta = \omega/c$ (at 100 MHz, $v_p$ is only 0.18 % above $c$), as it must for $\omega\gg\omega_p$.
>
> **Watch out:** below $f_p$ the plasma does not carry "a slower wave"; it carries no travelling wave at all.
>
> **Answer.** (a) $\omega_p = 3.77\times10^7$ rad/s, $f_p = 6.00$ MHz. (b) 10 MHz and 100 MHz travel; 4 MHz is cut off. (c) $\beta = 4\pi/75\approx0.168$ rad/m, $\lambda = 37.5$ m (30 m in free space), $v_p = 3.75\times10^8$ m/s $= 1.25c$. (d) No: $v_g = 0.8c = 2.4\times10^8$ m/s and $v_pv_g = c^2$; the crossing takes 0.625 ms, against 0.500 ms for light in vacuum.

### 21.7 Partner fields on three axes

> [!medium] Medium · phasor fields · intrinsic impedance · plane waves
> Each phasor below is a single plane wave in a lossless medium. For each one, find the direction of travel $\hat u$, the partner field ($\tilde{\mathbf{H}}$ from $\tilde{\mathbf{E}}$, or $\tilde{\mathbf{E}}$ from $\tilde{\mathbf{H}}$), the partner in the time domain, and $\langle\mathbf{S}\rangle$ as a vector. Use $\eta_0 = 120\pi\ \Omega$.
> (a) Free space: $\tilde{\mathbf{E}} = 6e^{-j2\pi x}\,\hat y$ V/m.
> (b) A non-magnetic dielectric with $\epsilon_r = 9$: $\tilde{\mathbf{H}} = 0.1j\,e^{+j\pi y}\,\hat x$ A/m.
> (c) Free space: $\tilde{\mathbf{E}} = 5e^{j(1.2\pi x - 1.6\pi y)}\,\hat z$ V/m, written in the exam template $e^{j(ax + by + cz)}$.
>
> *Source: course notes Example 1 style (a table of fields, phasors and partners), with new axes, a dielectric, and the $e^{j(ax + by + cz)}$ template of the Summer exam papers.*

> [!hint]- Hint
> Read $\hat u$ first, from the exponent: the wave travels toward where the phase lags, so the exponent is $-j\beta\hat u\cdot\mathbf{r}$, and in the template $(a, b, c) = -\beta\hat u$. Then $\tilde{\mathbf{H}} = \hat u\times\tilde{\mathbf{E}}/\eta$ or $\tilde{\mathbf{E}} = \eta\,\tilde{\mathbf{H}}\times\hat u$, and finally check that $\tilde{\mathbf{E}}\times\tilde{\mathbf{H}}^*$ points along $\hat u$.

> [!solution]- Solution
> **Setup.** One wave each, in lossless media: $\eta$ is real, so any complex factor rides along into the partner field.
>
> **(a)** $e^{-j2\pi x}$ travels toward $+x$: $\hat u = \hat x$ and $\beta = 2\pi$ rad/m (300 MHz in free space). With $\hat x\times\hat y = \hat z$,
> $$
> \tilde{\mathbf{H}} = \frac{6}{120\pi}\,e^{-j2\pi x}\,\hat z = \frac{1}{20\pi}\,e^{-j2\pi x}\,\hat z\approx15.9\,e^{-j2\pi x}\,\hat z\ \text{mA/m},\qquad \mathbf{H} = 15.9\cos(\omega t - 2\pi x)\,\hat z\ \text{mA/m}.
> $$
> Check: $\hat y\times\hat z = +\hat x$ ✓. Then $\langle\mathbf{S}\rangle = \dfrac{36}{240\pi}\,\hat x = \dfrac{3}{20\pi}\,\hat x\approx0.0477\,\hat x$ W/m².
>
> **(b)** $e^{+j\pi y}$ travels toward $-y$: $\hat u = -\hat y$, and $\eta = \eta_0/3 = 40\pi\ \Omega$ ($\beta = \pi$ rad/m: $\lambda = 2$ m, 50 MHz at $v = c/3$). With $\hat x\times(-\hat y) = -\hat z$,
> $$
> \tilde{\mathbf{E}} = \eta\,\tilde{\mathbf{H}}\times\hat u = 40\pi\,(0.1j)\,e^{j\pi y}\,(-\hat z) = -4\pi j\,e^{j\pi y}\,\hat z\ \text{V/m},\qquad \mathbf{E} = 4\pi\sin(\omega t + \pi y)\,\hat z\approx12.6\sin(\omega t + \pi y)\,\hat z\ \text{V/m},
> $$
> since $\text{Re}\{-je^{j\phi}\} = \sin\phi$. (The given field itself is $\mathbf{H} = -0.1\sin(\omega t + \pi y)\,\hat x$ A/m.) Check: $\tilde{\mathbf{E}}\times\tilde{\mathbf{H}}^* = (-4\pi j)(-0.1j)\,(\hat z\times\hat x) = -0.4\pi\,\hat y$, along $-\hat y$ ✓. So $\langle\mathbf{S}\rangle = -0.2\pi\,\hat y\approx-0.628\,\hat y$ W/m².
>
> **(c)** $(a, b, c) = (1.2\pi, -1.6\pi, 0)$ rad/m has length $\beta = \pi\sqrt{1.44 + 2.56} = 2\pi$ rad/m (300 MHz in free space), and $\hat u = -(a, b, c)/\beta = -0.6\,\hat x + 0.8\,\hat y$. Write the cross product out: $\hat u\times\hat z = -0.6\,(\hat x\times\hat z) + 0.8\,(\hat y\times\hat z) = 0.6\,\hat y + 0.8\,\hat x$. So
> $$
> \tilde{\mathbf{H}} = \frac{5}{120\pi}\,(0.8\,\hat x + 0.6\,\hat y)\,e^{j(1.2\pi x - 1.6\pi y)}\approx(10.6\,\hat x + 7.96\,\hat y)\,e^{j(1.2\pi x - 1.6\pi y)}\ \text{mA/m},
> $$
> and $\mathbf{H} = (10.6\,\hat x + 7.96\,\hat y)\cos(\omega t + 1.2\pi x - 1.6\pi y)$ mA/m. Check: $\hat z\times(0.8\,\hat x + 0.6\,\hat y) = 0.8\,\hat y - 0.6\,\hat x = \hat u$ ✓. Then $\langle\mathbf{S}\rangle = \dfrac{25}{240\pi}\,\hat u = \dfrac{5}{48\pi}\,\hat u\approx0.0332\,\hat u = -0.0199\,\hat x + 0.0265\,\hat y$ W/m².
>
> **Watch out:** in (c) the template's plus sign puts the minus into $(a, b, c)$. The wave travels toward $-x$ and $+y$, opposite to the signs of $a$ and $b$.
>
> **Answer.** (a) Toward $+\hat x$; $\tilde{\mathbf{H}} = \tfrac{1}{20\pi}e^{-j2\pi x}\,\hat z$ A/m $\approx15.9e^{-j2\pi x}\,\hat z$ mA/m, $\mathbf{H} = 15.9\cos(\omega t - 2\pi x)\,\hat z$ mA/m; $\langle\mathbf{S}\rangle\approx0.0477\,\hat x$ W/m². (b) Toward $-\hat y$; $\tilde{\mathbf{E}} = -4\pi j\,e^{j\pi y}\,\hat z$ V/m, $\mathbf{E} = 12.6\sin(\omega t + \pi y)\,\hat z$ V/m; $\langle\mathbf{S}\rangle\approx-0.628\,\hat y$ W/m². (c) $\hat u = -0.6\,\hat x + 0.8\,\hat y$; $\tilde{\mathbf{H}}\approx(10.6\,\hat x + 7.96\,\hat y)\,e^{j(1.2\pi x - 1.6\pi y)}$ mA/m, $\mathbf{H} = (10.6\,\hat x + 7.96\,\hat y)\cos(\omega t + 1.2\pi x - 1.6\pi y)$ mA/m; $\langle\mathbf{S}\rangle\approx-0.0199\,\hat x + 0.0265\,\hat y$ W/m² (magnitude 0.0332 W/m²).

### 21.8 A driven electron in phasors

> [!medium] Medium · phasors · time average · dispersion relation
> The free electrons of a collisionless plasma ($N = 1.0\times10^{12}$ m⁻³, charge $-e$, mass $m$) are driven by $\mathbf{E} = E_0\cos(\omega t)\,\hat x$ with $E_0 = 0.2$ V/m and $f = 20$ MHz. Use $e = 1.602\times10^{-19}$ C, $m = 9.109\times10^{-31}$ kg, $\epsilon_0 = 8.854\times10^{-12}$ F/m and $c = 3\times10^8$ m/s (calculator problem).
> (a) Solve $m\,d\mathbf{v}/dt = -e\mathbf{E}$ for the steady-state velocity with phasors, and write $\mathbf{v}(t)$.
> (b) Find $\tilde{\mathbf{J}} = -Ne\tilde{\mathbf{v}}$ and $\mathbf{J}(t)$. Does $\mathbf{J}$ lead or lag $\mathbf{E}$, and by how much? Find $\langle\mathbf{J}\cdot\mathbf{E}\rangle$.
> (c) Compare $\mathbf{J}$ with the displacement current density $\epsilon_0\,\partial\mathbf{E}/\partial t$: the ratio of their amplitudes and their relative phase. Show that together they equal the displacement current density of a dielectric with $\epsilon = \epsilon_0(1 - \omega_p^2/\omega^2)$, and use $\beta = \omega\sqrt{\mu_0\epsilon}$ to recover the notes' plasma dispersion relation. Find $\beta$, $\lambda$ and $v_p$ at 20 MHz.
>
> *Source: original (Lecture 11's Drude equation without collisions, solved with Lecture 21's phasor rules).*

> [!hint]- Hint
> $d/dt\to j\omega$ turns the equation of motion into $j\omega m\tilde{\mathbf{v}} = -e\tilde{\mathbf{E}}$: divide. For (b), $\langle\mathbf{J}\cdot\mathbf{E}\rangle = \tfrac12\text{Re}\{\tilde{\mathbf{J}}\cdot\tilde{\mathbf{E}}^*\}$. For (c), the displacement current density has the phasor $j\omega\epsilon_0\tilde{\mathbf{E}}$.

> [!solution]- Solution
> **Setup.** Everything oscillates at $\omega = 2\pi\times20\times10^6 = 1.257\times10^8$ rad/s, so phasors apply. $\tilde{\mathbf{E}} = E_0\,\hat x$ is real, a pure cosine.
>
> **(a)** $j\omega m\tilde{\mathbf{v}} = -e\tilde{\mathbf{E}}$ gives
> $$
> \tilde{\mathbf{v}} = \frac{-eE_0}{j\omega m}\,\hat x = j\,\frac{eE_0}{m\omega}\,\hat x,\qquad v_0 = \frac{eE_0}{m\omega} = \frac{(1.602\times10^{-19})(0.2)}{(9.109\times10^{-31})(1.257\times10^8)} = 280\ \text{m/s},
> $$
> so $\mathbf{v}(t) = \text{Re}\{jv_0e^{j\omega t}\}\,\hat x = -280\sin(\omega t)\,\hat x$ m/s. Check: $m\,dv_x/dt = -m\omega v_0\cos\omega t = -eE_0\cos\omega t$ ✓. The velocity leads $\mathbf{E}$ by 90°.
>
> **(b)** $\tilde{\mathbf{J}} = -Ne\tilde{\mathbf{v}} = -j\,\dfrac{Ne^2E_0}{m\omega}\,\hat x$, with amplitude $J_0 = Nev_0 = (10^{12})(1.602\times10^{-19})(280) = 4.48\times10^{-5}$ A/m². So $\mathbf{J}(t) = 44.8\sin(\omega t)\,\hat x$ µA/m²: the factor $-j$ means $\mathbf{J}$ **lags** $\mathbf{E}$ by 90°. Then
> $$
> \langle\mathbf{J}\cdot\mathbf{E}\rangle = \tfrac12\text{Re}\{\tilde{\mathbf{J}}\cdot\tilde{\mathbf{E}}^*\} = \tfrac12\text{Re}\{-jJ_0E_0\} = 0 .
> $$
> The field gives the electrons energy during one quarter period and takes it back during the next: on average, nothing is absorbed.
>
> **(c)** The displacement current density has the phasor $j\omega\epsilon_0E_0\,\hat x$: amplitude $\omega\epsilon_0E_0 = (1.257\times10^8)(8.854\times10^{-12})(0.2) = 2.23\times10^{-4}$ A/m² $= 223$ µA/m², leading $\mathbf{E}$ by 90°. So $\mathbf{J}$ and $\epsilon_0\,\partial\mathbf{E}/\partial t$ are in antiphase, with the amplitude ratio
> $$
> \frac{J_0}{\omega\epsilon_0E_0} = \frac{Ne^2}{m\epsilon_0\omega^2} = \frac{\omega_p^2}{\omega^2} = 0.202 .
> $$
> Together, $\tilde{\mathbf{J}} + j\omega\epsilon_0\tilde{\mathbf{E}} = j\omega\epsilon_0\big(1 - \omega_p^2/\omega^2\big)\tilde{\mathbf{E}}$, which is the displacement current density $j\omega\epsilon\tilde{\mathbf{E}}$ of a dielectric with $\epsilon = \epsilon_0(1 - \omega_p^2/\omega^2) = 0.798\,\epsilon_0$. Then
> $$
> \beta = \omega\sqrt{\mu_0\epsilon_0\Big(1 - \frac{\omega_p^2}{\omega^2}\Big)} = \frac1c\sqrt{\omega^2 - \omega_p^2},
> $$
> the notes' dispersion relation. With numbers, $\beta = (\omega/c)\sqrt{0.798} = (0.419)(0.894) = 0.374$ rad/m, $\lambda = 2\pi/\beta = 16.8$ m and $v_p = \omega/\beta = 3.36\times10^8$ m/s $= 1.12c$.
>
> **Check:** $f_p = \sqrt{Ne^2/(m\epsilon_0)}/2\pi = 8.98$ MHz, below 20 MHz, so $\epsilon>0$ and the wave travels; and $(8.98/20)^2 = 0.202$, the ratio found in (c) ✓.
>
> **Watch out:** an effective $\epsilon$ that changes with $\omega$ is what makes the plasma dispersive. Below $\omega_p$ it turns negative, and $\beta$ is no longer real.
>
> **Answer.** (a) $\tilde{\mathbf{v}} = j(eE_0/m\omega)\,\hat x$, $\mathbf{v} = -280\sin(\omega t)\,\hat x$ m/s. (b) $\mathbf{J} = 44.8\sin(\omega t)\,\hat x$ µA/m², lagging $\mathbf{E}$ by 90°; $\langle\mathbf{J}\cdot\mathbf{E}\rangle = 0$. (c) $\mathbf{J}$ is 0.202 times the displacement current density (223 µA/m²) and in antiphase with it; $\epsilon = \epsilon_0(1 - \omega_p^2/\omega^2) = 0.798\,\epsilon_0$ gives $\beta = \tfrac1c\sqrt{\omega^2 - \omega_p^2}\approx0.374$ rad/m, $\lambda\approx16.8$ m, $v_p\approx3.36\times10^8$ m/s $= 1.12c$.

## Hard

### 21.9 A phasor from two snapshots

> [!hard] Hard · phasor fields · wave parameters · time-average power
> A uniform plane wave at $f = 100$ MHz travels in a lossless, non-magnetic dielectric with $\epsilon_r = 2.25$, in the direction $\hat u = (-4\hat x + 3\hat y)/5$. At the origin its instantaneous electric field is $\mathbf{E} = 4\hat z$ V/m at $t = 0$, and $\mathbf{E} = 3\hat x + 4\hat y$ V/m a quarter period later, at $t = T/4$. Its phasor is written $\tilde{\mathbf{E}} = (A\hat x + B\hat y + C\hat z)\,e^{j(ax + by + cz)}$ V/m, where $a$, $b$, $c$ are constants of the template (here $c$ is not the speed of light). Take the speed of light as $3\times10^8$ m/s and $\eta_0 = 120\pi\ \Omega$.
> (a) Find $\beta$, $\lambda$, $\eta$, and the constants $a$, $b$, $c$.
> (b) Check that both snapshots are allowed for this wave, and find $A$, $B$, $C$. Write $\mathbf{E}(0, t)$.
> (c) Find $\tilde{\mathbf{H}}$.
> (d) Find $\langle\mathbf{S}\rangle$ as a vector, and the time-average power density carried by the $\hat z$ component of $\mathbf{E}$ alone and by its $xy$-plane component alone.
> (e) Find $\mathbf{E}$ at the point $P = (1, 0.5, 0)$ m at $t = 0$, and explain why it equals one of the given snapshots.
>
> *Source: Summer 2019 HE3 #3a and Summer 2018 HE3 #3a style, re-parameterized: a diagonal direction of travel in a dielectric, two snapshots of unequal size (so that no polarization question arises), and $\tilde{\mathbf{H}}$, the component powers and a quarter-wave point added.*

> [!hint]- Hint
> For (a), $(a, b, c) = -\beta\hat u$: the plus sign of the template puts a minus in front. For (b), at the origin $\mathbf{E}(0, t) = \text{Re}\{\tilde{\mathbf{E}}_0e^{j\omega t}\} = \text{Re}\{\tilde{\mathbf{E}}_0\}\cos\omega t - \text{Im}\{\tilde{\mathbf{E}}_0\}\sin\omega t$, so the snapshot at $t = 0$ is $\text{Re}\{\tilde{\mathbf{E}}_0\}$ and the one at $T/4$ is $-\text{Im}\{\tilde{\mathbf{E}}_0\}$.

> [!solution]- Solution
> **Setup.** A plane wave along $\hat u$ has $\tilde{\mathbf{E}} = \tilde{\mathbf{E}}_0\,e^{-j\beta\hat u\cdot\mathbf{r}}$ with $\tilde{\mathbf{E}}_0\perp\hat u$. The template is the same thing with $(a, b, c) = -\beta\hat u$ and $\tilde{\mathbf{E}}_0 = A\hat x + B\hat y + C\hat z$.
>
> **(a)** $v = (3\times10^8\ \text{m/s})/\sqrt{2.25} = 2\times10^8$ m/s, $\beta = \omega/v = 2\pi\times10^8/(2\times10^8) = \pi$ rad/m, $\lambda = 2$ m, $\eta = \eta_0/1.5 = 80\pi\approx251\ \Omega$. Then
> $$
> (a, b, c) = -\pi\,(-0.8,\ 0.6,\ 0) = (0.8\pi,\ -0.6\pi,\ 0)\ \text{rad/m}\approx(2.51,\ -1.88,\ 0)\ \text{rad/m}.
> $$
>
> **(b)** Both snapshots must be perpendicular to $\hat u$, as a TEM wave requires: $4\hat z\cdot\hat u = 0$ and $(3\hat x + 4\hat y)\cdot\hat u = (-12 + 12)/5 = 0$ ✓. From the hint, $\text{Re}\{\tilde{\mathbf{E}}_0\} = 4\hat z$ and $\text{Im}\{\tilde{\mathbf{E}}_0\} = -(3\hat x + 4\hat y)$:
> $$
> \tilde{\mathbf{E}}_0 = 4\hat z - j(3\hat x + 4\hat y),\qquad A = -3j,\quad B = -4j,\quad C = 4\ \text{V/m}.
> $$
> So $\mathbf{E}(0, t) = 3\sin(\omega t)\,\hat x + 4\sin(\omega t)\,\hat y + 4\cos(\omega t)\,\hat z$ V/m, which gives $4\hat z$ at $t = 0$ and $3\hat x + 4\hat y$ at $\omega t = \pi/2$ ✓.
>
> **(c)** $\tilde{\mathbf{H}} = \hat u\times\tilde{\mathbf{E}}/\eta$. Component by component, with $\hat u = (-0.8, 0.6, 0)$ and $\tilde{\mathbf{E}}_0 = (-3j, -4j, 4)$:
> $$
> \hat u\times\tilde{\mathbf{E}}_0 = \big(0.6\cdot4 - 0,\ \ 0 - (-0.8)(4),\ \ (-0.8)(-4j) - (0.6)(-3j)\big) = (2.4,\ 3.2,\ 5j),
> $$
> $$
> \tilde{\mathbf{H}} = \frac{2.4\,\hat x + 3.2\,\hat y + 5j\,\hat z}{80\pi}\,e^{j(0.8\pi x - 0.6\pi y)}\approx(9.55\,\hat x + 12.7\,\hat y + 19.9j\,\hat z)\,e^{j(0.8\pi x - 0.6\pi y)}\ \text{mA/m}.
> $$
>
> **(d)** $\lvert\tilde{\mathbf{E}}_0\rvert^2 = 9 + 16 + 16 = 41$ (V/m)², so
> $$
> \langle\mathbf{S}\rangle = \frac{\lvert\tilde{\mathbf{E}}_0\rvert^2}{2\eta}\,\hat u = \frac{41}{160\pi}\,\hat u\approx0.0816\,\hat u = -0.0653\,\hat x + 0.0489\,\hat y\ \text{W/m}^2 .
> $$
> The $\hat z$ part alone carries $16/(160\pi)\approx0.0318$ W/m², and the $xy$ part, with $\lvert{-3j}\rvert^2 + \lvert{-4j}\rvert^2 = 25$, carries $25/(160\pi)\approx0.0497$ W/m². They add up to the total although the two parts are 90° out of phase: the cross terms in $\lvert\tilde{\mathbf{E}}_0\rvert^2 = \tilde{\mathbf{E}}_0\cdot\tilde{\mathbf{E}}_0^*$ are dot products of $\hat z$ with vectors in the $xy$ plane, and vanish.
>
> **(e)** $\hat u\cdot\mathbf{r}_P = (-4 + 1.5)/5 = -0.5$ m $= -\lambda/4$, so $e^{-j\beta\hat u\cdot\mathbf{r}_P} = e^{j\pi/2} = j$ and
> $$
> \tilde{\mathbf{E}}(P) = j\,\big(4\hat z - 3j\hat x - 4j\hat y\big) = 3\hat x + 4\hat y + 4j\hat z,\qquad \mathbf{E}(P, 0) = \text{Re}\{\tilde{\mathbf{E}}(P)\} = 3\hat x + 4\hat y\ \text{V/m}.
> $$
> $P$ lies a quarter wavelength *upstream* of the origin, so it shows now what the origin will show a quarter period later: $\mathbf{E}(P, 0) = \mathbf{E}(0, T/4)$.
>
> **Check:** $\tilde{\mathbf{E}}_0\cdot\hat u = 2.4j - 2.4j = 0$ ✓; $\lvert\tilde{\mathbf{H}}_0\rvert = \sqrt{2.4^2 + 3.2^2 + 5^2}/(80\pi) = \sqrt{41}/(80\pi) = \lvert\tilde{\mathbf{E}}_0\rvert/\eta$ ✓; and $\tfrac12\text{Re}\{\tilde{\mathbf{E}}_0\times\tilde{\mathbf{H}}_0^*\}$, worked out component by component, gives the same $\langle\mathbf{S}\rangle$.
>
> **Watch out:** writing $(a, b, c) = +\beta\hat u = (-0.8\pi, 0.6\pi, 0)$ sends the wave the wrong way; the snapshots and $\tilde{\mathbf{H}}$ would then belong to a different wave.
>
> **Answer.** (a) $\beta = \pi$ rad/m, $\lambda = 2$ m, $\eta = 80\pi\approx251\ \Omega$, $(a, b, c) = (0.8\pi, -0.6\pi, 0)$ rad/m. (b) $A = -3j$, $B = -4j$, $C = 4$ V/m; $\mathbf{E}(0, t) = (3\hat x + 4\hat y)\sin\omega t + 4\hat z\cos\omega t$ V/m. (c) $\tilde{\mathbf{H}} = (2.4\,\hat x + 3.2\,\hat y + 5j\,\hat z)\,e^{j(0.8\pi x - 0.6\pi y)}/(80\pi)$ A/m $\approx(9.55\,\hat x + 12.7\,\hat y + 19.9j\,\hat z)\,e^{j(0.8\pi x - 0.6\pi y)}$ mA/m. (d) $\langle\mathbf{S}\rangle = \dfrac{41}{160\pi}\,\hat u\approx-0.0653\,\hat x + 0.0489\,\hat y$ W/m² (0.0816 W/m²): 0.0318 W/m² from the $\hat z$ part and 0.0497 W/m² from the $xy$ part. (e) $\mathbf{E}(P, 0) = 3\hat x + 4\hat y$ V/m $= \mathbf{E}(0, T/4)$.

### 21.10 Two sheets, two current directions

> [!hard] Hard · current sheet radiation · phasor fields · energy balance
> Two current sheets are embedded in a lossless, non-magnetic dielectric with $\epsilon_r = 4$ that fills all space. Sheet A, on the plane $z = 0$, carries $\mathbf{J}_A = 2\cos(\omega t)\,\hat x$ A/m; sheet B, on the plane $z = d$, carries $\mathbf{J}_B = \sin(\omega t)\,\hat y$ A/m. The frequency is $f = 75$ MHz and $d = \lambda/4$. Use $c = 3\times10^8$ m/s and $\eta_0 = 120\pi\ \Omega$.
> (a) Find $\beta$, $\lambda$, $d$, $\eta$, and the phasors $\tilde{\mathbf{J}}_A$ and $\tilde{\mathbf{J}}_B$.
> (b) Write $\tilde{\mathbf{E}}$ and $\tilde{\mathbf{H}}$ radiated by each sheet alone, on each side of it.
> (c) For $z>d$, write the total field as $\tilde{\mathbf{E}} = P\,e^{-j\beta z}(\hat x + Q\hat y)$ and find $P$ and $Q$. Find the total $\tilde{\mathbf{E}}$ for $z<0$ and for $0<z<d$.
> (d) Find $\langle\mathbf{S}\rangle$ in each of the three regions.
> (e) Find the power each sheet delivers per unit area, $\langle-\mathbf{J}_A\cdot\mathbf{E}\rangle$ at $z = 0$ and $\langle-\mathbf{J}_B\cdot\mathbf{E}\rangle$ at $z = d$, and show that the energy balance closes.
> (f) Sheet B's current is turned to $\sin(\omega t)\,\hat x$, parallel to A's. Find $\langle\mathbf{S}\rangle$ for $z>d$ and for $z<0$. Why do the two sheets' powers no longer simply add on each side?
>
> *Source: Summer 2020 final #4a and #4c, re-parameterized: sheets on $z = 0$ and $z = \lambda/4$ in a dielectric (not on $x = 0$ and $x = \lambda/2$ in free space), currents of 2 and 1 A/m with a sine in place of a free phase, and all three regions, the energy balance and a parallel-current variant added.*

> [!hint]- Hint
> Use the sheet recipe in phasor form, $\tilde{\mathbf{E}} = -\tfrac\eta2\tilde{\mathbf{J}}_s\,e^{-j\beta d_s}$ and $\tilde{\mathbf{H}} = \tfrac12\tilde{\mathbf{J}}_s\times\hat n\,e^{-j\beta d_s}$, with $d_s$ the distance from that sheet and $\hat n$ pointing away from it, then superpose. For $z>d$, $e^{-j\beta(z - d)} = e^{-j\beta z}e^{j\beta d}$, and $e^{j\beta d} = e^{j\pi/2} = j$.

> [!solution]- Solution
> **Setup.** Each sheet radiates as if it were alone (Lecture 19); in phasor form the delay $d_s/v$ becomes the factor $e^{-j\beta d_s}$ (Lecture 21 §6). The total field is the sum.
>
> **(a)** $v = c/2 = 1.5\times10^8$ m/s, $\beta = 2\pi f/v = \pi$ rad/m, $\lambda = 2$ m, $d = 0.5$ m, $\eta = \eta_0/2 = 60\pi\approx188.5\ \Omega$. $\tilde{\mathbf{J}}_A = 2\hat x$ A/m and, the sine picking up $-j$, $\tilde{\mathbf{J}}_B = -j\hat y$ A/m.
>
> **(b)** With $\hat x\times(\pm\hat z) = \mp\hat y$ and $\hat y\times(\pm\hat z) = \pm\hat x$:
> $$
> \begin{aligned}
> \text{A:}\quad &\tilde{\mathbf{E}}_A = -60\pi\,e^{-j\beta\lvert z\rvert}\,\hat x\ \text{V/m},\qquad \tilde{\mathbf{H}}_A = \mp e^{-j\beta\lvert z\rvert}\,\hat y\ \text{A/m}\quad(z\gtrless0),\\
> \text{B:}\quad &\tilde{\mathbf{E}}_B = 30\pi j\,e^{-j\beta\lvert z - d\rvert}\,\hat y\ \text{V/m},\qquad \tilde{\mathbf{H}}_B = \mp\tfrac{j}{2}\,e^{-j\beta\lvert z - d\rvert}\,\hat x\ \text{A/m}\quad(z\gtrless d).
> \end{aligned}
> $$
>
> **(c)** For $z>d$, $e^{-j\beta(z - d)} = je^{-j\beta z}$, so B's field there is $30\pi j\cdot j\,e^{-j\beta z}\,\hat y = -30\pi\,e^{-j\beta z}\,\hat y$ and
> $$
> \tilde{\mathbf{E}} = -60\pi\,e^{-j\beta z}\big(\hat x + \tfrac12\hat y\big):\qquad P = -60\pi\approx-188.5\ \text{V/m},\quad Q = \tfrac12 .
> $$
> For $z<0$, $e^{-j\beta(d - z)} = -je^{j\beta z}$, so $\tilde{\mathbf{E}} = -60\pi\,e^{j\beta z}\big(\hat x - \tfrac12\hat y\big)$. Between the sheets two waves travel in opposite directions, A's toward $+z$ and B's toward $-z$: $\tilde{\mathbf{E}} = -60\pi\,e^{-j\beta z}\,\hat x + 30\pi\,e^{j\beta z}\,\hat y$.
>
> **(d)** Each outer region holds one wave with $\lvert\tilde{\mathbf{E}}_0\rvert^2 = (60\pi)^2(1 + \tfrac14)$:
> $$
> \langle\mathbf{S}\rangle = \pm\frac{(60\pi)^2\,(5/4)}{2\,(60\pi)}\,\hat z = \pm37.5\pi\,\hat z\approx\pm118\,\hat z\ \text{W/m}^2\qquad(+\ \text{for}\ z>d,\ -\ \text{for}\ z<0).
> $$
> Between the sheets, A's wave carries $(60\pi)^2/(120\pi) = 30\pi$ W/m² toward $+z$ and B's carries $(30\pi)^2/(120\pi) = 7.5\pi$ W/m² toward $-z$. The cross terms in $\tilde{\mathbf{E}}\times\tilde{\mathbf{H}}^*$ are $\hat x\times\hat x$ and $\hat y\times\hat y$ and vanish, so $\langle\mathbf{S}\rangle = 22.5\pi\,\hat z\approx70.7\,\hat z$ W/m².
>
> **(e)** The total field is $\tilde{\mathbf{E}}(0) = -60\pi\,\hat x + 30\pi\,\hat y$ at sheet A and $\tilde{\mathbf{E}}(d) = 60\pi j\,\hat x + 30\pi j\,\hat y$ at sheet B. Then
> $$
> \begin{aligned}
> \langle-\mathbf{J}_A\cdot\mathbf{E}\rangle &= \tfrac12\text{Re}\big\{-(2\hat x)\cdot(-60\pi\,\hat x + 30\pi\,\hat y)\big\} = 60\pi\approx188.5\ \text{W/m}^2,\\
> \langle-\mathbf{J}_B\cdot\mathbf{E}\rangle &= \tfrac12\text{Re}\big\{-(-j)(30\pi j)^*\big\} = \tfrac12\text{Re}\big\{-(-j)(-30\pi j)\big\} = 15\pi\approx47.1\ \text{W/m}^2 .
> \end{aligned}
> $$
> Together $75\pi\approx236$ W/m², equal to the $37.5\pi + 37.5\pi$ leaving through the two outer regions ✓. Sheet by sheet: across A the flux steps from $-37.5\pi$ to $+22.5\pi$, by $60\pi$; across B from $22.5\pi$ to $37.5\pi$, by $15\pi$; each step is that sheet's delivery. Each sheet delivers exactly what it would alone, $\tfrac\eta4J_0^2$, because its current is perpendicular to the other sheet's field.
>
> **(f)** Now $\tilde{\mathbf{J}}_B = -j\hat x$ and B's field is $30\pi j\,e^{-j\beta\lvert z - d\rvert}\,\hat x$, parallel to A's:
> $$
> z>d:\ \tilde{\mathbf{E}} = (-60\pi - 30\pi)\,e^{-j\beta z}\,\hat x = -90\pi\,e^{-j\beta z}\,\hat x,\qquad z<0:\ \tilde{\mathbf{E}} = (-60\pi + 30\pi)\,e^{j\beta z}\,\hat x = -30\pi\,e^{j\beta z}\,\hat x,
> $$
> so $\langle\mathbf{S}\rangle = (90\pi)^2/(120\pi)\,\hat z = 67.5\pi\,\hat z\approx212\,\hat z$ W/m² above and $-(30\pi)^2/(120\pi)\,\hat z = -7.5\pi\,\hat z\approx-23.6\,\hat z$ W/m² below. Parallel fields add as phasors *before* squaring, so each side's power gets a cross term. Toward $+z$, B's quarter-period lag matches the quarter-wave trip from A to B, and the two waves leave in step; toward $-z$ they leave half a period apart and partly cancel. The total is still $75\pi$ here, but the sheets now share it differently: A delivers $30\pi$ and B $45\pi$ W/m².
>
> **Check:** at each sheet, $\hat z\times(\tilde{\mathbf{H}}^+ - \tilde{\mathbf{H}}^-) = \tilde{\mathbf{J}}_s$; at A, for example, $\hat z\times(-\hat y - \hat y) = 2\hat x$ ✓ (B's $\tfrac12\hat x$ is continuous there). Tangential $\tilde{\mathbf{E}}$ is continuous at both sheets, and the total field satisfies both curl equations in every region (checked by script).
>
> **Answer.** (a) $\beta = \pi$ rad/m, $\lambda = 2$ m, $d = 0.5$ m, $\eta = 60\pi\ \Omega$; $\tilde{\mathbf{J}}_A = 2\hat x$, $\tilde{\mathbf{J}}_B = -j\hat y$ A/m. (b) $\tilde{\mathbf{E}}_A = -60\pi e^{-j\beta\lvert z\rvert}\,\hat x$, $\tilde{\mathbf{H}}_A = \mp e^{-j\beta\lvert z\rvert}\,\hat y$ ($z\gtrless0$); $\tilde{\mathbf{E}}_B = 30\pi j\,e^{-j\beta\lvert z - d\rvert}\,\hat y$, $\tilde{\mathbf{H}}_B = \mp\tfrac{j}{2}e^{-j\beta\lvert z - d\rvert}\,\hat x$ ($z\gtrless d$). (c) $P = -60\pi$ V/m, $Q = \tfrac12$; $z<0$: $-60\pi e^{j\beta z}(\hat x - \tfrac12\hat y)$; between: $-60\pi e^{-j\beta z}\,\hat x + 30\pi e^{j\beta z}\,\hat y$ V/m. (d) $37.5\pi\,\hat z\approx118\,\hat z$ W/m² for $z>d$, $22.5\pi\,\hat z\approx70.7\,\hat z$ W/m² between, $-37.5\pi\,\hat z$ W/m² for $z<0$. (e) $60\pi\approx188.5$ W/m² and $15\pi\approx47.1$ W/m², total $75\pi$ = outflow ✓. (f) $67.5\pi\,\hat z\approx212\,\hat z$ W/m² above, $-7.5\pi\,\hat z\approx-23.6\,\hat z$ W/m² below: parallel fields interfere.

### 21.11 Two waves on one line

> [!hard] Hard · phasor fields · time average · energy density
> In a lossless, non-magnetic dielectric with $\epsilon_r = 9$, the electric field is
> $$
> \mathbf{E} = \big[6\cos(\omega t - \beta z) + 2\sin(\omega t + \beta z)\big]\,\hat x\ \text{V/m},\qquad f = 100\ \text{MHz}.
> $$
> Use $c = 3\times10^8$ m/s and $\eta_0 = 120\pi\ \Omega$.
> (a) Find $\beta$, $\lambda$ and $\eta$. Write $\tilde{\mathbf{E}}$ as a sum of two waves, find $\tilde{\mathbf{H}}$, and write $\mathbf{H}(z, t)$.
> (b) Find $\langle\mathbf{S}\rangle = \tfrac12\text{Re}\{\tilde{\mathbf{E}}\times\tilde{\mathbf{H}}^*\}$. Show that the cross terms between the two waves are purely imaginary and that $\langle\mathbf{S}\rangle$ does not depend on $z$.
> (c) Find $\lvert\tilde{\mathbf{E}}(z)\rvert$ and $\lvert\tilde{\mathbf{H}}(z)\rvert$. Where on $0\le z<\lambda/2$ is each largest and smallest, and what are the extreme values? Is $\lvert\tilde{\mathbf{E}}\rvert/\lvert\tilde{\mathbf{H}}\rvert = \eta$?
> (d) Find the time-average energy densities $\langle w_e\rangle$ and $\langle w_m\rangle$ (with $w_e = \tfrac12\epsilon E^2$ and $w_m = \tfrac12\mu H^2$). Show that their sum is the same at every $z$, and compare $\langle\mathbf{S}\rangle$ with $v\langle w\rangle$.
> (e) At $z = 0$, is the instantaneous $S_z$ ever negative? If so, for what fraction of each period?
>
> *Source: original (the notes' Example 2 with parallel instead of perpendicular polarizations; Lecture 21 §7 remarks that the cross terms are then imaginary).*

> [!hint]- Hint
> Give each wave its own $\hat u$: the $\cos(\omega t - \beta z)$ wave travels toward $+z$, and the $\sin(\omega t + \beta z)$ wave travels toward $-z$ and picks up a $-j$. For (c), $\lvert\tilde E\rvert^2 = \tilde E\tilde E^*$ and $e^{j\phi} - e^{-j\phi} = 2j\sin\phi$. For (d), $\langle a^2\rangle = \tfrac12\lvert\tilde A\rvert^2$.

> [!solution]- Solution
> **Setup.** Two waves of the same frequency on the $z$ axis, one each way. Each obeys the partner rule with its own $\hat u$, and every average comes from the phasor product rule.
>
> **(a)** $v = c/3 = 10^8$ m/s, $\beta = 2\pi f/v = 2\pi$ rad/m, $\lambda = 1$ m, $\eta = \eta_0/3 = 40\pi\ \Omega$. The two waves are $6e^{-j\beta z}\,\hat x$ (toward $+z$) and $-2j\,e^{+j\beta z}\,\hat x$ (toward $-z$). With $\hat z\times\hat x = \hat y$ and $(-\hat z)\times\hat x = -\hat y$:
> $$
> \tilde{\mathbf{E}} = \big(6e^{-j\beta z} - 2je^{j\beta z}\big)\,\hat x,\qquad \tilde{\mathbf{H}} = \frac{1}{\eta}\big(6e^{-j\beta z} + 2je^{j\beta z}\big)\,\hat y,
> $$
> $$
> \mathbf{H} = \big[47.7\cos(\omega t - \beta z) - 15.9\sin(\omega t + \beta z)\big]\,\hat y\ \text{mA/m}\qquad(6/\eta = 47.7\ \text{mA/m},\ 2/\eta = 15.9\ \text{mA/m}).
> $$
> The backward wave's $\mathbf{H}$ enters with the opposite sign, as for the counter-propagating pulses of Lecture 18.
>
> **(b)**
> $$
> \tilde{\mathbf{E}}\times\tilde{\mathbf{H}}^* = \frac1\eta\big(6e^{-j\beta z} - 2je^{j\beta z}\big)\big(6e^{j\beta z} - 2je^{-j\beta z}\big)\,\hat z = \frac1\eta\Big[36 - 4 - 12j\big(e^{-j2\beta z} + e^{j2\beta z}\big)\Big]\hat z = \frac{32 - 24j\cos2\beta z}{\eta}\,\hat z .
> $$
> The cross terms, $-24j\cos(2\beta z)/\eta$, are purely imaginary and drop out of the real part:
> $$
> \langle\mathbf{S}\rangle = \frac{16}{\eta}\,\hat z = \frac{0.4}{\pi}\,\hat z\approx0.127\,\hat z\ \text{W/m}^2,
> $$
> the forward wave's $36/(2\eta) = 0.143$ W/m² minus the backward wave's $4/(2\eta) = 0.0159$ W/m², at every $z$.
>
> **(c)**
> $$
> \lvert\tilde E\rvert^2 = \big(6e^{-j\beta z} - 2je^{j\beta z}\big)\big(6e^{j\beta z} + 2je^{-j\beta z}\big) = 40 + 12j\big(e^{-j2\beta z} - e^{j2\beta z}\big) = 40 + 24\sin(2\beta z),
> $$
> and in the same way $\eta^2\lvert\tilde H\rvert^2 = 40 - 24\sin(2\beta z)$. With $2\beta z = 4\pi z$, $\lvert\tilde{\mathbf{E}}\rvert$ is largest, $\sqrt{64} = 8$ V/m, at $z = \lambda/8 = 0.125$ m, and smallest, $\sqrt{16} = 4$ V/m, at $z = 3\lambda/8 = 0.375$ m. $\lvert\tilde{\mathbf{H}}\rvert$ does the opposite: largest, $8/\eta = 63.7$ mA/m, at $z = 0.375$ m, and smallest, $4/\eta = 31.8$ mA/m, at $z = 0.125$ m. So $\lvert\tilde{\mathbf{E}}\rvert/\lvert\tilde{\mathbf{H}}\rvert$ swings from $2\eta$ (at 0.125 m) to $\eta/2$ (at 0.375 m): the ratio $\eta$ belongs to a single wave, not to a sum of waves.
>
> **(d)** $\langle w_e\rangle = \tfrac12\epsilon\langle E_x^2\rangle = \tfrac14\epsilon\lvert\tilde E\rvert^2$ and $\langle w_m\rangle = \tfrac14\mu_0\lvert\tilde H\rvert^2$. Since $\mu_0/\eta^2 = \epsilon$,
> $$
> \langle w_e\rangle = \tfrac14\epsilon\big(40 + 24\sin2\beta z\big),\qquad \langle w_m\rangle = \tfrac14\epsilon\big(40 - 24\sin2\beta z\big),\qquad \langle w\rangle = 20\epsilon\approx1.59\ \text{nJ/m}^3
> $$
> at every $z$ ($\epsilon = 9\epsilon_0$), while $\langle w_e\rangle$ alone swings between $4\epsilon$ and $16\epsilon$ (about 0.32 and 1.27 nJ/m³). For a single wave $\langle S\rangle = v\langle w\rangle$. Here $v\langle w\rangle = 20\epsilon v = 20/\eta$, but $\langle S\rangle = 16/\eta$: the energy drifts forward at only $\langle S\rangle/\langle w\rangle = 0.8v = 8\times10^7$ m/s, because part of it belongs to the backward wave.
>
> **(e)** At $z = 0$, $E_x = 6\cos\omega t + 2\sin\omega t$ and $H_y = (6\cos\omega t - 2\sin\omega t)/\eta$, so
> $$
> S_z(0, t) = \frac{36\cos^2\omega t - 4\sin^2\omega t}{\eta},
> $$
> which is negative whenever $\lvert\tan\omega t\rvert>3$, that is for $71.6^\circ<\omega t<108.4^\circ$ and again half a period later: a fraction $1 - \tfrac2\pi\tan^{-1}3\approx0.205$ of each period, about 20 %. $S_z$ swings between $-4/\eta = -0.0318$ W/m² and $36/\eta = 0.286$ W/m² and averages to $16/\eta$ ✓. A single travelling wave never sends energy backward, even for an instant; two counter-propagating waves can.
>
> **Check:** the pair $(\mathbf{E}, \mathbf{H})$ satisfies both curl equations (finite differences, by script), and at $z = 0$ the direct average of $S_z(0, t)$, $\tfrac12(36 - 4)/\eta = 16/\eta$, matches the phasor result ✓.
>
> **Answer.** (a) $\beta = 2\pi$ rad/m, $\lambda = 1$ m, $\eta = 40\pi\ \Omega$; $\tilde{\mathbf{E}} = (6e^{-j\beta z} - 2je^{j\beta z})\,\hat x$ V/m, $\tilde{\mathbf{H}} = (6e^{-j\beta z} + 2je^{j\beta z})\,\hat y/\eta$, $\mathbf{H} = [47.7\cos(\omega t - \beta z) - 15.9\sin(\omega t + \beta z)]\,\hat y$ mA/m. (b) $\tilde{\mathbf{E}}\times\tilde{\mathbf{H}}^* = (32 - 24j\cos2\beta z)\,\hat z/\eta$; $\langle\mathbf{S}\rangle = (16/\eta)\,\hat z\approx0.127\,\hat z$ W/m² at every $z$. (c) $\lvert\tilde{\mathbf{E}}\rvert$: 8 V/m at $z = 0.125$ m, 4 V/m at 0.375 m; $\lvert\tilde{\mathbf{H}}\rvert$: 63.7 mA/m at 0.375 m, 31.8 mA/m at 0.125 m; the ratio runs from $2\eta$ to $\eta/2$, not $\eta$. (d) $\langle w\rangle = 20\epsilon\approx1.59$ nJ/m³ at every $z$; $\langle S\rangle/\langle w\rangle = 0.8v$. (e) Yes, for about 20 % of each period ($\lvert\tan\omega t\rvert>3$); the minimum is $-0.0318$ W/m².

### 21.12 A medium from phasor readings

> [!hard] Hard · phasor fields · wave parameters · intrinsic impedance
> A uniform plane wave at $f = 25$ MHz travels along the $z$ axis through a lossless medium whose $\mu$ and $\epsilon$ are unknown. Two probes on the $z$ axis, 0.25 m apart and closer than half a wavelength, report phasors (cosine reference, peak values):
> - at $z = 0$: $\tilde{\mathbf{E}} = 37.7\,e^{j30^\circ}\,\hat y$ V/m and $\tilde{\mathbf{H}} = 0.2\,e^{j30^\circ}\,\hat x$ A/m;
> - at $z = 0.25$ m: $\tilde{\mathbf{E}} = 37.7\,e^{j75^\circ}\,\hat y$ V/m.
>
> Use $c = 3\times10^8$ m/s and $\eta_0 = 120\pi\ \Omega$.
> (a) Find the direction of travel in two independent ways.
> (b) Find $\beta$, $\lambda$ and $v_p$; then $\eta$, $\mu_r$ and $\epsilon_r$.
> (c) Write $\tilde{\mathbf{E}}(z)$, $\tilde{\mathbf{H}}(z)$, $\mathbf{E}(z, t)$ and $\mathbf{H}(z, t)$.
> (d) Find $\langle\mathbf{S}\rangle$, and the time-average power crossing a 1 m × 2 m rectangle in the plane $z = -4$ m.
> (e) What does a probe at $z = -0.5$ m record? Give its phasor and $\mathbf{E}(t)$. At $t = 0$, where on $-2<z<0$ m is $E_y$ at its positive peak?
>
> *Source: original (phasors as measured amplitude and phase; a speed fixes only $\mu_r\epsilon_r$, and $\eta$ fixes $\mu_r/\epsilon_r$).*

> [!hint]- Hint
> Direction: $\tilde{\mathbf{E}}\times\tilde{\mathbf{H}}^*$ points along the travel, and the phase falls in the direction of travel (a downstream point repeats what an upstream point did, later). Then $\beta = \lvert\Delta\phi\rvert/\Delta z$, $\eta = \lvert\tilde{\mathbf{E}}\rvert/\lvert\tilde{\mathbf{H}}\rvert$, $c/v_p = \sqrt{\mu_r\epsilon_r}$ and $\eta/\eta_0 = \sqrt{\mu_r/\epsilon_r}$.

> [!solution]- Solution
> **Setup.** A phasor is what a probe measures: the amplitude and the phase of the local cosine. The phases at two points give $\beta$ and the direction, the ratio $\lvert\tilde{\mathbf{E}}\rvert/\lvert\tilde{\mathbf{H}}\rvert$ gives $\eta$, and the two together give the medium.
>
> **(a)** First way: $\tilde{\mathbf{E}}\times\tilde{\mathbf{H}}^* = (37.7)(0.2)\,e^{j30^\circ}e^{-j30^\circ}\,(\hat y\times\hat x) = -7.54\,\hat z$, so power flows toward $-z$. Second way: the phase *rises* from $30^\circ$ at $z = 0$ to $75^\circ$ at $z = 0.25$ m, so it falls toward $-z$; the probe at $z = 0.25$ m leads, and the wave travels toward where the phase lags: toward $-z$ ✓; the probes are closer than $\lambda/2$, so this $+45^\circ$ cannot be a $315^\circ$ lag. ($\tilde{\mathbf{E}}$ and $\tilde{\mathbf{H}}$ also have the same phase, as they must in a lossless medium.)
>
> **(b)** $\lvert\Delta\phi\rvert = 45^\circ = \pi/4$ over 0.25 m; it is less than $\pi$, as the spacing guarantees, so no multiple of $2\pi$ hides in it. Hence $\beta = \pi$ rad/m, $\lambda = 2$ m and $v_p = \omega/\beta = 2\pi(25\times10^6)/\pi = 5\times10^7$ m/s $= c/6$. Next, $\eta = 37.7/0.2 = 188.5\ \Omega = \eta_0/2$, and
> $$
> \mu_r\epsilon_r = \Big(\frac{c}{v_p}\Big)^2 = 36,\qquad \frac{\mu_r}{\epsilon_r} = \Big(\frac{\eta}{\eta_0}\Big)^2 = \frac14\qquad\Longrightarrow\qquad \mu_r = 3,\quad \epsilon_r = 12 .
> $$
>
> **(c)** Toward $-z$ the position factor is $e^{+j\beta z}$:
> $$
> \tilde{\mathbf{E}} = 37.7\,e^{j30^\circ}e^{j\pi z}\,\hat y\ \text{V/m},\qquad \tilde{\mathbf{H}} = \frac1\eta\,(-\hat z)\times\tilde{\mathbf{E}} = 0.2\,e^{j30^\circ}e^{j\pi z}\,\hat x\ \text{A/m},
> $$
> using $(-\hat z)\times\hat y = +\hat x$; this reproduces the measured $\tilde{\mathbf{H}}$ ✓. With $\omega = 5\pi\times10^7$ rad/s, $\mathbf{E} = 37.7\cos(\omega t + \pi z + 30^\circ)\,\hat y$ V/m and $\mathbf{H} = 0.2\cos(\omega t + \pi z + 30^\circ)\,\hat x$ A/m. At $z = 0.25$ m the phase is $30^\circ + 45^\circ = 75^\circ$, the second reading ✓.
>
> **(d)** $\langle\mathbf{S}\rangle = \tfrac12\text{Re}\{\tilde{\mathbf{E}}\times\tilde{\mathbf{H}}^*\} = -\tfrac12(37.7)(0.2)\,\hat z = -3.77\,\hat z$ W/m² ($= -1.2\pi\,\hat z$), the same at every $z$ in a lossless medium. Through the 2 m² rectangle at $z = -4$ m: $3.77\times2 = 7.54$ W, crossing toward $-z$.
>
> **(e)** $z = -0.5$ m is $\lambda/4$ downstream of the origin. Its phasor is $37.7\,e^{j30^\circ}e^{-j\pi/2}\,\hat y = 37.7\,e^{-j60^\circ}\,\hat y$ V/m, so it records $\mathbf{E}(t) = 37.7\cos(\omega t - 60^\circ)\,\hat y$ V/m: the origin's record delayed by a quarter period, $T/4 = 10$ ns. The snapshot $E_y(z, 0) = 37.7\cos(\pi z + 30^\circ)$ peaks where $\pi z + \pi/6 = 2\pi n$; on $-2<z<0$ that is $z = -1/6\approx-0.167$ m. A quarter period later that crest has moved $\lambda/4$ toward $-z$, to $z = -0.667$ m.
>
> **Check:** with $\mu = 3\mu_0$ and $\epsilon = 12\epsilon_0$ the pair satisfies Faraday's law and the Ampère–Maxwell law (finite differences, by script); and $\lambda f = 2\times25\times10^6 = 5\times10^7$ m/s $= v_p$ ✓.
>
> **Watch out:** the speed alone cannot tell this medium from a non-magnetic one with $\epsilon_r = 36$, which has the same $v_p$; only $\eta$ separates them ($20\pi\approx62.8\ \Omega$ for $\epsilon_r = 36$, against $188.5\ \Omega$ here).
>
> **Answer.** (a) Toward $-\hat z$: $\tilde{\mathbf{E}}\times\tilde{\mathbf{H}}^*\parallel-\hat z$, and the phase grows with $z$. (b) $\beta = \pi$ rad/m, $\lambda = 2$ m, $v_p = 5\times10^7$ m/s; $\eta = 188.5\ \Omega$, $\mu_r = 3$, $\epsilon_r = 12$. (c) $\tilde{\mathbf{E}} = 37.7\,e^{j30^\circ}e^{j\pi z}\,\hat y$ V/m, $\tilde{\mathbf{H}} = 0.2\,e^{j30^\circ}e^{j\pi z}\,\hat x$ A/m; $\mathbf{E} = 37.7\cos(\omega t + \pi z + 30^\circ)\,\hat y$ V/m, $\mathbf{H} = 0.2\cos(\omega t + \pi z + 30^\circ)\,\hat x$ A/m. (d) $\langle\mathbf{S}\rangle = -3.77\,\hat z$ W/m²; 7.54 W toward $-z$. (e) Phasor $37.7\,e^{-j60^\circ}\,\hat y$ V/m, $\mathbf{E}(t) = 37.7\cos(\omega t - 60^\circ)\,\hat y$ V/m (10 ns behind the origin); positive peak at $z = -1/6\approx-0.167$ m.

### Sources for this page
Course notes, Lecture 21: reading a monochromatic wave, with the period, wavelength and phase velocity (21.1); the three dispersion relations, including the acoustic one (21.1(c)) and the collisionless plasma (21.6, 21.8); the phasor conversions and Example 1's table of fields, phasors and partners (21.2, 21.7); Example 2, here with parallel polarizations (21.11); Example 3's current sheet in phasor form (21.10); and the time-average rule $\langle ab\rangle = \tfrac12\text{Re}\{\tilde A\tilde B^*\}$ (21.3, 21.5 and throughout). Lecture 11's Drude equation, without collisions (21.8). Old exams, re-parameterized as described in each problem: SP17 Exam 3 #2(iii) (21.4), Summer 2019 HE3 #3a and Summer 2018 HE3 #3a (21.9), and the Summer 2020 final (FE) #4a and #4c (21.10). Original: 21.3, 21.5, 21.11 and 21.12. No problem duplicates the site's worked problem [[problems/phasors-e-and-power-from-a-given-h|Phasors, E and power from a given H]].

*Previous: [[practice/20-poynting-theorem-and-power|Lecture 20 practice]] · next: [[practice/22-damped-waves-in-conducting-media|Lecture 22 practice]] · [[practice/index|all practice]]*
