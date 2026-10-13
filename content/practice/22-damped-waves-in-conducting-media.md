---
title: "Practice — Lecture 22: Phasor Maxwell equations and damped waves"
description: "12 practice problems (5 easy, 3 medium, 4 hard) on Maxwell's equations in phasor form (continuity, Gauss's law from the curl laws, no oscillating charge inside a conductor), the Helmholtz equation in a conducting medium, σ + jωε as a complex conductivity and ε − jσ/ω as a complex permittivity, the propagation constant γ = α + jβ and the complex intrinsic impedance η with both square-root branches, decoding damped waves (direction, α, β, λ, v_p, penetration depth, H with its phase lag), backing out μ, σ and ε from γη = jωμ and γ/η = σ + jωε, field versus power decay and ⟨S⟩ with cos τ, the regimes, and a current sheet in a lossy medium, each with a folded hint and a worked solution."
tags: [practice, waves]
lecture: 22
---

*Practice for [[3-maxwell-and-waves/22-phasor-maxwell-equations-and-damped-waves|Lecture 22]] · concepts: [[concepts/propagation-constant]] · [[concepts/intrinsic-impedance]] · [[concepts/phasors]] · [[concepts/maxwells-equations]] · all practice: [[practice/index|hub]] · by difficulty: [[practice/easy|easy]] · [[practice/medium|medium]] · [[practice/hard|hard]] · [[practice/topics|by topic]]*

Work each problem on paper first. Open the **hint** only when stuck, and the **solution** only after you have an answer you would hand in. Every answer here has been checked numerically.

Most problems on this page run the decoding recipe of [[3-maxwell-and-waves/22-phasor-maxwell-equations-and-damped-waves#5-the-general-formulas-and-how-to-decode-a-damped-wave|Lecture 22 §5]]. A wave travelling along $\hat u$ varies as $e^{-\gamma\,\hat u\cdot\mathbf{r}}$, so it decays in the direction it travels, and
$$
\begin{gathered}
\gamma = \sqrt{j\omega\mu(\sigma + j\omega\epsilon)} = \alpha + j\beta\ \ (\alpha\ge0),\qquad \eta = \frac{j\omega\mu}{\gamma} = \lvert\eta\rvert e^{j\tau}\ \ (0\le\tau<45^\circ),\\[6pt]
\tilde{\mathbf{H}} = \frac{\hat u\times\tilde{\mathbf{E}}}{\eta},\qquad \frac{\gamma}{\eta} = \sigma + j\omega\epsilon .
\end{gathered}
$$
Dividing by $\eta$ divides the amplitude by $\lvert\eta\rvert$ and subtracts $\tau$ from the phase, so $\mathbf{H}$ lags $\mathbf{E}$.

## Easy

### 22.1 Phasor Maxwell, true or false

> [!easy] Easy · true or false · phasor Maxwell equations · complex permittivity
> All fields vary as $e^{j\omega t}$ with $\omega\neq0$, in a linear, uniform medium with permittivity $\epsilon$, permeability $\mu$ and conductivity $\sigma$. True or false?
>
> (a) In phasor form Faraday's law reads $\nabla\times\tilde{\mathbf{E}} = -j\omega\mu\tilde{\mathbf{H}}$, and in a source-free region of the medium the Ampère–Maxwell law reads $\nabla\times\tilde{\mathbf{H}} = (\sigma + j\omega\epsilon)\tilde{\mathbf{E}}$.
>
> (b) Charge conservation becomes $\nabla\cdot\tilde{\mathbf{J}} = j\omega\tilde\rho$.
>
> (c) Gauss's law $\nabla\cdot\tilde{\mathbf{D}} = \tilde\rho$ need not be imposed separately: it follows from the phasor Ampère–Maxwell law $\nabla\times\tilde{\mathbf{H}} = \tilde{\mathbf{J}} + j\omega\tilde{\mathbf{D}}$ together with charge conservation.
>
> (d) Inside a uniform block of a medium with $\sigma = 0.1$ S/m and $\epsilon = 10\epsilon_0$, a strong enough applied field at 1 MHz can keep a free-charge density $\tilde\rho\neq0$ oscillating.
>
> (e) At 1 MHz the medium of (d) acts like a dielectric with the complex permittivity $\epsilon_c = (10 - j1800)\epsilon_0$ (use $\epsilon_0 = 10^{-9}/36\pi$ F/m).
>
> (f) In that medium the conduction current density $\sigma\tilde{\mathbf{E}}$ leads $\tilde{\mathbf{E}}$ by 90°, while the displacement current density $j\omega\epsilon\tilde{\mathbf{E}}$ is in phase with $\tilde{\mathbf{E}}$.
>
> *Source: original.*

> [!hint]- Hint
> Every $\partial/\partial t$ becomes a factor $j\omega$, and nothing else changes. For (c) and (d), take the divergence of the Ampère–Maxwell law: the divergence of a curl is zero.

> [!solution]- Solution
> (a) **True.** Each $\partial/\partial t$ becomes $j\omega$: $\nabla\times\tilde{\mathbf{E}} = -j\omega\tilde{\mathbf{B}} = -j\omega\mu\tilde{\mathbf{H}}$. With the conduction current $\tilde{\mathbf{J}} = \sigma\tilde{\mathbf{E}}$ as the only current, $\nabla\times\tilde{\mathbf{H}} = \sigma\tilde{\mathbf{E}} + j\omega\epsilon\tilde{\mathbf{E}}$.
>
> (b) **False.** $\nabla\cdot\mathbf{J} + \partial\rho/\partial t = 0$ becomes $\nabla\cdot\tilde{\mathbf{J}} + j\omega\tilde\rho = 0$, so $\nabla\cdot\tilde{\mathbf{J}} = -j\omega\tilde\rho$. The minus sign is physics: current flowing out of a point drains the charge there.
>
> (c) **True.** Take the divergence of the Ampère–Maxwell law and use (b): $0 = \nabla\cdot\tilde{\mathbf{J}} + j\omega\nabla\cdot\tilde{\mathbf{D}} = j\omega(\nabla\cdot\tilde{\mathbf{D}} - \tilde\rho)$. With $\omega\neq0$, $\nabla\cdot\tilde{\mathbf{D}} = \tilde\rho$. Faraday's law gives $\nabla\cdot\tilde{\mathbf{B}} = 0$ the same way.
>
> (d) **False.** Inside the block $\tilde{\mathbf{J}} = \sigma\tilde{\mathbf{E}}$ and $\tilde{\mathbf{D}} = \epsilon\tilde{\mathbf{E}}$, so $-j\omega\tilde\rho = \nabla\cdot\tilde{\mathbf{J}} = (\sigma/\epsilon)\tilde\rho$, that is, $(\sigma + j\omega\epsilon)\tilde\rho = 0$. Since $\sigma + j\omega\epsilon\neq0$, $\tilde\rho = 0$ however strong the field is. This is Lecture 8's relaxation with $\partial/\partial t\to j\omega$: interior charge disappears in about $\epsilon/\sigma = 0.88$ ns, more than a thousand times faster than the 1 µs period. Oscillating charge can sit only on the block's surfaces.
>
> (e) **True.** $\sigma + j\omega\epsilon = j\omega(\epsilon - j\sigma/\omega)$, and $\sigma/(\omega\epsilon_0) = 0.1\big/\big(2\pi\times10^6\times10^{-9}/36\pi\big) = 1800$. So $\epsilon_c = (10 - j1800)\epsilon_0$. The imaginary part is huge because at 1 MHz the conduction current is $\sigma/\omega\epsilon = 180$ times the displacement current.
>
> (f) **False: it is the other way round.** $\sigma$ is real, so $\sigma\tilde{\mathbf{E}}$ is in phase with $\tilde{\mathbf{E}}$; it is the current that heats the medium. The factor $j$ in $j\omega\epsilon\tilde{\mathbf{E}}$ puts the displacement current 90° *ahead* of $\tilde{\mathbf{E}}$.
>
> **Answer.** (a) T, (b) F, (c) T, (d) F, (e) T, (f) F.

### 22.2 Which phasors are allowed

> [!easy] Easy · multiple choice · Helmholtz equation · propagation constant
> A uniform conducting medium has $\gamma^2 = j\omega\mu(\sigma + j\omega\epsilon) = -8 + j6\ \text{m}^{-2}$ at the working frequency. Which of these phasors can be the electric field in a source-free region of the medium? Choose all that apply ($x$, $y$, $z$ in metres).
>
> (a) $\tilde{\mathbf{E}} = \hat{x}\,2e^{-(1 + j3)z}$ V/m
>
> (b) $\tilde{\mathbf{E}} = \hat{y}\,2e^{+(1 + j3)z}$ V/m
>
> (c) $\tilde{\mathbf{E}} = \hat{x}\,2e^{-(3 + j)z}$ V/m
>
> (d) $\tilde{\mathbf{E}} = \hat{x}\,2e^{-(1 - j3)z}$ V/m
>
> (e) $\tilde{\mathbf{E}} = \hat{z}\,2e^{-(1 + j3)z}$ V/m
>
> (f) $\tilde{\mathbf{E}} = \hat{x}\,2e^{-(1 + j3)(0.6y + 0.8z)}$ V/m
>
> *Source: original.*

> [!hint]- Hint
> A phasor field in a source-free region must pass two tests: the Helmholtz equation $\nabla^2\tilde{\mathbf{E}} = \gamma^2\tilde{\mathbf{E}}$, and Gauss's law $\nabla\cdot\tilde{\mathbf{E}} = 0$. For a field proportional to $e^{-k s}$, where $s$ is distance along a unit vector, $\nabla^2$ simply multiplies by $k^2$.

> [!solution]- Solution
> In a uniform, source-free medium $\tilde\rho = 0$ (Lecture 22 §1), so an allowed field must satisfy $\nabla^2\tilde{\mathbf{E}} = \gamma^2\tilde{\mathbf{E}}$ **and** $\nabla\cdot\tilde{\mathbf{E}} = 0$. For $e^{-k(\hat u\cdot\mathbf{r})}$, $\nabla^2$ multiplies by $k^2\lvert\hat u\rvert^2 = k^2$, so the first test is $k^2 = -8 + j6$. Note that $(1 + j3)^2 = 1 - 9 + j6 = -8 + j6$.
> - (a) **Allowed.** $k^2 = -8 + j6$ ✓ and $\nabla\cdot\tilde{\mathbf{E}} = \partial\tilde E_x/\partial x = 0$ ✓. This is the wave travelling toward $+z$.
> - (b) **Allowed.** $\big(-(1 + j3)\big)^2 = -8 + j6$ ✓ and $\partial\tilde E_y/\partial y = 0$ ✓. This is the other root at work: $e^{+\gamma z}$ is the wave travelling toward $-z$, and it decays toward $-z$, along its travel.
> - (c) **Not allowed.** $(3 + j)^2 = 8 + j6$: $\alpha$ and $\beta$ have been swapped. That would also give $\beta<\alpha$, which a real $\sigma$ never allows.
> - (d) **Not allowed.** $(1 - j3)^2 = -8 - j6$. This field decays toward $+z$, but its phase $e^{+j3z}$ travels toward $-z$: it would grow along its own travel. The Helmholtz equation itself rules it out.
> - (e) **Not allowed.** $k^2$ is right, but $\nabla\cdot\tilde{\mathbf{E}} = \partial\tilde E_z/\partial z = -(1 + j3)\tilde E_z\neq0$. A field pointing along its own direction of variation needs a charge density, which a uniform conductor cannot hold. As in Lecture 18, a $z$-polarized wave cannot travel along $z$.
> - (f) **Allowed.** $\nabla^2$ gives $(1 + j3)^2(0.6^2 + 0.8^2) = -8 + j6$ ✓, and $\nabla\cdot\tilde{\mathbf{E}} = \partial\tilde E_x/\partial x = 0$ ✓. It is a wave travelling along $0.6\hat{y} + 0.8\hat{z}$, with $\tilde{\mathbf{E}}$ perpendicular to that direction.
>
> This $\gamma^2$ belongs to the medium of the Lecture 22 §5 example ($\epsilon = 8\epsilon_0$, $\sigma = 1/20\pi$ S/m, $\mu_0$, $\omega = 3\times10^8$ rad/s), where $\gamma = 1 + j3$ m⁻¹.
>
> **Answer.** (a), (b) and (f).

### 22.3 Reading a damped wave

> [!easy] Easy · damped waves · penetration depth · attenuation
> In a non-magnetic lossy medium, $\mathbf{E}(z,t) = \hat{x}\,20e^{-0.5z}\cos(2\pi\times10^8t - 2\pi z + 45^\circ)$ V/m ($z$ in m, $t$ in s).
> (a) Which way does the wave travel?
> (b) Find $\omega$, $f$, $\alpha$, $\beta$, and $\gamma$ in rectangular and polar form.
> (c) Find $\lambda$, $v_p$ and the penetration depth $\delta$.
> (d) By what factor is the amplitude at $z = 4$ m smaller than at $z = 0$? By what factor is the power density smaller?
>
> *Source: original.*

> [!hint]- Hint
> $\omega$ multiplies $t$, $\beta$ multiplies $z$ inside the cosine, and $\alpha$ multiplies $z$ in the exponential. Power goes as the square of the field.

> [!solution]- Solution
> (a) The $t$ and $z$ terms have opposite signs, so the wave travels toward $+z$. The amplitude $e^{-0.5z}$ shrinks in that direction, as it must.
>
> (b) $\omega = 2\pi\times10^8$ rad/s, so $f = 100$ MHz. $\alpha = 0.5$ Np/m and $\beta = 2\pi\approx6.28$ rad/m, so $\gamma = 0.5 + j6.28$ m⁻¹ $= 6.30\,e^{j85.45^\circ}$ m⁻¹. The 45° is a constant phase, not part of $\beta$.
>
> (c) $\lambda = 2\pi/\beta = 1$ m, $v_p = \omega/\beta = 1\times10^8$ m/s and $\delta = 1/\alpha = 2$ m. Check: $\lambda f = 10^8$ m/s ✓.
>
> (d) $z = 4$ m is $2\delta$, so the amplitude is $20e^{-2} = 2.71$ V/m, a factor $e^{-2} = 0.135$ (13.5 %) of its value at $z = 0$, that is, $e^2 = 7.39$ times smaller. Power density goes as the amplitude squared: a factor $e^{-4} = 0.0183$, or 1.83 %, that is, $e^4 = 54.6$ times smaller.
>
> **Watch out:** $\delta$ is where the *field* is down to $1/e$. The power is then down to $1/e^2$.
>
> **Answer.** (a) Toward $+z$. (b) $\omega = 2\pi\times10^8$ rad/s, $f = 100$ MHz, $\alpha = 0.5$ Np/m, $\beta = 2\pi$ rad/m, $\gamma = 0.5 + j6.28$ m⁻¹ $= 6.30\,e^{j85.45^\circ}$ m⁻¹. (c) $\lambda = 1$ m, $v_p = 1\times10^8$ m/s, $\delta = 2$ m. (d) The amplitude falls to $e^{-2} = 0.135$ of its value (2.71 V/m), $e^2 = 7.39$ times smaller; the power density falls to $e^{-4} = 0.0183$ of its value, $e^4 = 54.6$ times smaller.

### 22.4 Possible or not possible

> [!easy] Easy · true or false · regimes · propagation constant
> Statements (a)–(d) describe a uniform plane wave in a homogeneous medium with real, positive $\mu$ and $\epsilon$ and a real $\sigma\ge0$. Statement (e) is about a plasma. Is each POSSIBLE or NOT POSSIBLE? Give a one-line reason.
>
> (a) The wave has $\alpha = 2$ Np/m and $\beta = 0.5$ rad/m.
>
> (b) In a non-magnetic medium with $\epsilon = 4\epsilon_0$ and $\sigma = 0.01$ S/m, a 1 GHz wave has $\alpha$ much smaller than $\beta$ (use $\epsilon_0 = 10^{-9}/36\pi$ F/m).
>
> (c) At every point of a 50 MHz wave, $\mathbf{H}$ reaches each of its maxima 2 ns *before* $\mathbf{E}$ does.
>
> (d) The amplitude falls by a factor $e$ over one tenth of a wavelength.
>
> (e) In a collisionless plasma (Lecture 22 §8) a wave's field decays as $e^{-\alpha z}$ with $\alpha>0$, yet the plasma absorbs no power.
>
> *Source: Summer 2020 HE3 #3a style (POSSIBLE or NOT POSSIBLE), with new statements and media.*

> [!hint]- Hint
> Statements (a)–(d) all follow from the angle of $\eta$, $\tau = \tfrac12\tan^{-1}(\sigma/\omega\epsilon)$, which lies between 0 and 45°: $\alpha/\beta = \tan\tau$, and $\mathbf{H}$ lags $\mathbf{E}$ by $\tau$.

> [!solution]- Solution
> (a) **NOT POSSIBLE.** $\alpha/\beta = \tan\tau$ with $0\le\tau<45^\circ$, so $\alpha<\beta$ whenever $\sigma$ is real. The two are equal only in the limit $\sigma/\omega\epsilon\to\infty$. Here $\alpha/\beta = 4$.
>
> (b) **POSSIBLE.** $\omega\epsilon = 2\pi\times10^9\times4\times10^{-9}/36\pi = 0.222$ S/m, so $\sigma/\omega\epsilon = 0.045\ll1$: an imperfect dielectric. The exact values are $\alpha = 0.942$ Np/m and $\beta = 41.9$ rad/m, so $\alpha/\beta = 0.022$.
>
> (c) **NOT POSSIBLE.** With real $\mu$, $\epsilon$ and $\sigma$, $\mathbf{H}$ *lags* $\mathbf{E}$ by $\tau/\omega\ge0$. A 2 ns lead is $36^\circ$ at 50 MHz and would need $\tau = -36^\circ$, that is, $\sigma<0$. A 2 ns *lag* would be possible, since $36^\circ<45^\circ$; a lag longer than 2.5 ns would not.
>
> (d) **NOT POSSIBLE.** A fall by $e$ over $\lambda/10$ means $\alpha\lambda = 10$, so $\alpha/\beta = 10/2\pi = 1.6>1$. For a real $\sigma$ the penetration depth is never shorter than $\lambda/2\pi$; it approaches that value only in the good-conductor limit, where the field drops to $e^{-2\pi} = 0.19$ % in one wavelength.
>
> (e) **POSSIBLE.** A collisionless plasma has an imaginary conductivity. Below the plasma frequency $\gamma$ is real, so the field decays without oscillating in space, but $\eta$ is purely imaginary. $\mathbf{E}$ and $\mathbf{H}$ are then 90° apart and $\langle\mathbf{S}\rangle = \tfrac12\text{Re}\{\tilde{\mathbf{E}}\times\tilde{\mathbf{H}}^*\} = 0$. With $\text{Re}\{\sigma\} = 0$ nothing is heated: the plasma reflects the wave instead of absorbing it. For example, $N = 10^{11}$ electrons per m³ gives $f_p = 2.84$ MHz, and at 2 MHz $\delta = 23.7$ m and $\eta = j374\ \Omega$.
>
> **Answer.** (a) NOT POSSIBLE, (b) POSSIBLE, (c) NOT POSSIBLE, (d) NOT POSSIBLE, (e) POSSIBLE.

### 22.5 The magnetic field that leads

> [!easy] Easy · find the error · complex intrinsic impedance
> A plane wave $\mathbf{E} = \hat{z}\,60e^{-\alpha x}\cos(\omega t - \beta x)$ V/m travels toward $+x$ in a lossy medium whose intrinsic impedance is $\eta = 150e^{j20^\circ}\ \Omega$. A student finds $\mathbf{H}$:
>
> "Dividing by $\eta$ divides the amplitude by 150 and adds the angle of $\eta$, 20°. For the direction, $\mathbf{E}\times\mathbf{H}$ must point along $+\hat{x}$, and $\hat{z}\times(-\hat{y}) = +\hat{x}$, so $\mathbf{H}$ points along $-\hat{y}$. Therefore $\mathbf{H} = -\hat{y}\,0.4e^{-\alpha x}\cos(\omega t - \beta x + 20^\circ)$ A/m, and $\mathbf{H}$ leads $\mathbf{E}$ by 20°."
>
> Find the slip, correct it, and confirm the correction with Faraday's law.
>
> *Source: original.*

> [!hint]- Hint
> Write $1/\eta$ in polar form.

> [!solution]- Solution
> **The slip:** dividing by $\eta = \lvert\eta\rvert e^{j\tau}$ means multiplying by $1/\eta = e^{-j\tau}/\lvert\eta\rvert$, which *subtracts* $\tau$. The student added it. The direction is right.
>
> **Fix:** $\tilde{\mathbf{H}} = \hat u\times\tilde{\mathbf{E}}/\eta = (\hat{x}\times\hat{z})\,\dfrac{60}{150}\,e^{-j20^\circ}e^{-\gamma x} = -\hat{y}\,0.4e^{-j20^\circ}e^{-\gamma x}$ A/m, so
> $$
> \mathbf{H} = -\hat{y}\,0.4e^{-\alpha x}\cos(\omega t - \beta x - 20^\circ)\ \text{A/m}.
> $$
> $\mathbf{H}$ **lags** $\mathbf{E}$ by 20°, as it always does when $\mu$, $\epsilon$ and $\sigma$ are real.
>
> **Faraday's law:** $\nabla\times(\hat{z}\tilde E_z) = -\hat{y}\,\partial\tilde E_z/\partial x = \hat{y}\,\gamma\tilde E_z$, and this must equal $-j\omega\mu\tilde{\mathbf{H}}$. So $\tilde{\mathbf{H}} = -\hat{y}\,\dfrac{\gamma}{j\omega\mu}\tilde E_z = -\hat{y}\,\tilde E_z/\eta$, using $\gamma\eta = j\omega\mu$. The phase of $1/\eta$ is $-20^\circ$ ✓. A lead of 20° would need $\tau = -20^\circ$, that is, $\sigma/\omega\epsilon = \tan(-40^\circ) = -0.84<0$: a medium that supplies energy instead of absorbing it.
>
> **Watch out:** a power check cannot catch this slip. $\langle\mathbf{S}\rangle = \tfrac12\cdot60\cdot0.4\cos(\pm20^\circ)\,e^{-2\alpha x}\,\hat{x} = 11.3e^{-2\alpha x}\,\hat{x}$ W/m² either way, because the cosine is even. Faraday's law does catch it.
>
> **Answer.** The student added $\tau$ instead of subtracting it. Correct: $\mathbf{H} = -\hat{y}\,0.4e^{-\alpha x}\cos(\omega t - \beta x - 20^\circ)$ A/m, so $\mathbf{H}$ lags $\mathbf{E}$ by 20°.

## Medium

### 22.6 From the medium to the wave

> [!medium] Medium · propagation constant · complex intrinsic impedance · complex permittivity
> A non-magnetic medium has $\epsilon = 5\epsilon_0$ and $\sigma = 1/(10\pi)$ S/m $\approx31.8$ mS/m. A plane wave with $\omega = 3\times10^8$ rad/s travels through it toward $+z$. Use $\epsilon_0 = 10^{-9}/36\pi$ F/m and $\mu_0 = 4\pi\times10^{-7}$ H/m; no calculator is needed.
> (a) Find $\sigma + j\omega\epsilon$, the ratio $\sigma/\omega\epsilon$, and the complex permittivity $\epsilon_c = \epsilon - j\sigma/\omega$ as a multiple of $\epsilon_0$.
> (b) Find $\gamma^2 = j\omega\mu(\sigma + j\omega\epsilon)$ and both of its square roots. Which root is $\gamma$, and what does the other root describe?
> (c) Find $\eta$ from $\eta^2 = j\omega\mu/(\sigma + j\omega\epsilon)$, in rectangular and polar form, and check $\gamma\eta = j\omega\mu$.
> (d) Find $\delta$, $\lambda$ and $v_p$. Compare $\beta$ and $\lvert\eta\rvert$ with the values the same medium would have without its conductivity.
>
> *Source: original.*

> [!hint]- Hint
> Here $\omega\mu_0 = 120\pi\ \Omega$/m, so put everything over $120\pi$. To take $\sqrt{-5 + j12}$ by hand, solve $\beta^2 - \alpha^2 = 5$ and $2\alpha\beta = 12$, or take the square root of the magnitude (13) and halve the angle.

> [!solution]- Solution
> **Setup.** Lecture 22's single replacement, $j\omega\epsilon\to\sigma + j\omega\epsilon$, gives both $\gamma$ and $\eta$ from one complex number.
>
> **(a)** $\omega\epsilon = 3\times10^8\times5\times10^{-9}/36\pi = 1/(24\pi)$ S/m $= 13.3$ mS/m, so
> $$
> \sigma + j\omega\epsilon = \frac{1}{10\pi} + \frac{j}{24\pi} = \frac{12 + j5}{120\pi}\ \text{S/m} = 31.8 + j13.3\ \text{mS/m},\qquad \frac{\sigma}{\omega\epsilon} = \frac{12}{5} = 2.4 .
> $$
> Dividing by $j\omega$ gives $\epsilon_c = \epsilon - j\sigma/\omega = (5 - j12)\epsilon_0$, since $\sigma/(\omega\epsilon_0) = 12$.
>
> **(b)** With $\omega\mu_0 = 3\times10^8\times4\pi\times10^{-7} = 120\pi$:
> $$
> \gamma^2 = j120\pi\cdot\frac{12 + j5}{120\pi} = -5 + j12\ \text{m}^{-2}.
> $$
> Its roots satisfy $\beta^2 - \alpha^2 = 5$ and $2\alpha\beta = 12$, so they are $\pm(2 + j3)$. Take $\gamma = 2 + j3$ m⁻¹ $= \sqrt{13}\,e^{j56.31^\circ} = 3.61\,e^{j56.31^\circ}$ m⁻¹, the root with $\alpha\ge0$. The other root, $-2 - j3$, describes nothing new: $e^{-(-2 - j3)z} = e^{+(2 + j3)z}$ is just the wave travelling toward $-z$, decaying toward $-z$. Choosing $\alpha\ge0$ is the convention that keeps $e^{-\gamma z}$ for travel toward $+z$ and $e^{+\gamma z}$ for travel toward $-z$, with $\alpha$ the decay rate along the travel. Using the other root would simply swap those labels.
>
> **(c)**
> $$
> \eta^2 = \frac{j120\pi\cdot120\pi}{12 + j5} = \frac{(120\pi)^2\,j(12 - j5)}{169} = \Big(\frac{120\pi}{13}\Big)^2(5 + j12),
> $$
> and $5 + j12 = (3 + j2)^2$, so $\eta = \pm\tfrac{120\pi}{13}(3 + j2)$. The root with a positive real part is
> $$
> \eta = \frac{120\pi}{13}(3 + j2) = 87.0 + j58.0\ \Omega = 104.6\,e^{j33.69^\circ}\ \Omega .
> $$
> Check: $\gamma\eta = (2 + j3)(3 + j2)\tfrac{120\pi}{13} = j13\cdot\tfrac{120\pi}{13} = j120\pi = j\omega\mu_0$ ✓, and $\tau = 90^\circ - 56.31^\circ = 33.69^\circ = \tan^{-1}(\alpha/\beta)$ ✓. The other root, at $-146.31^\circ$, gives $\gamma\eta = -j\omega\mu_0$ and would make $\langle\mathbf{S}\rangle$ point against the travel.
>
> **(d)** $\delta = 1/\alpha = 0.5$ m, $\lambda = 2\pi/3 = 2.09$ m and $v_p = \omega/\beta = 1\times10^8$ m/s. Without conductivity, $\beta_{\sigma=0} = \omega\sqrt{\mu_0\cdot5\epsilon_0} = \sqrt5 = 2.24$ rad/m and $\eta_{\sigma=0} = 120\pi/\sqrt5 = 168.6\ \Omega$. Conduction raises $\beta$ by 34 % and lowers $\lvert\eta\rvert$ by 38 %.
>
> **Check** with the general formulas of Lecture 22 §5: $\omega\sqrt{\mu\epsilon/2} = \sqrt{5/2}$ and $\sqrt{1 + 2.4^2} = 2.6$, so $\alpha = \sqrt{5/2}\,\sqrt{1.6} = 2$ ✓ and $\beta = \sqrt{5/2}\,\sqrt{3.6} = 3$ ✓.
>
> **Answer.** (a) $\sigma + j\omega\epsilon = (12 + j5)/120\pi$ S/m $= 31.8 + j13.3$ mS/m, $\sigma/\omega\epsilon = 2.4$, $\epsilon_c = (5 - j12)\epsilon_0$. (b) $\gamma^2 = -5 + j12$ m⁻²; roots $\pm(2 + j3)$; $\gamma = 2 + j3$ m⁻¹ $= 3.61\,e^{j56.31^\circ}$ m⁻¹. (c) $\eta = (120\pi/13)(3 + j2) = 87.0 + j58.0\ \Omega = 104.6\,e^{j33.69^\circ}\ \Omega$. (d) $\delta = 0.5$ m, $\lambda = 2.09$ m, $v_p = 1\times10^8$ m/s; $\beta$ rises from 2.24 to 3 rad/m and $\lvert\eta\rvert$ falls from 168.6 to 104.6 Ω.

### 22.7 Microwave heating of raw meat

> [!medium] Medium · complex permittivity · penetration depth · time-average power
> Model raw meat at 2.45 GHz, the frequency of a microwave oven, as a non-magnetic medium with the complex permittivity $\epsilon_c = \epsilon - j\sigma/\omega = (52 - j17)\epsilon_0$. Just inside its flat surface $z = 0$, a plane wave travelling toward $+z$ has an electric-field amplitude of 1000 V/m. This is a calculator problem; use $c = 3\times10^8$ m/s, $\epsilon_0 = 10^{-9}/36\pi$ F/m and $\eta_0 = 120\pi\ \Omega$.
> (a) Find the effective conductivity $\sigma$ and the ratio $\sigma/\omega\epsilon$. Could these data tell you how much of the loss comes from free ions and how much from the lagging polarization of the water molecules?
> (b) Find $\gamma = j\omega\sqrt{\mu_0\epsilon_c}$, then $\delta$, the wavelength in the meat and $v_p$.
> (c) Find $\eta = \sqrt{\mu_0/\epsilon_c}$ in polar form and the amplitude of $\mathbf{H}$ just inside the surface.
> (d) Find the time-average power density just inside the surface and at depths of 1 cm and 2 cm. At what depth has half of the power been absorbed?
>
> *Source: original (the material values are illustrative, chosen for this problem).*

> [!hint]- Hint
> $\epsilon_c$ already contains $\sigma$: $\sigma = 17\,\omega\epsilon_0$. One complex square root, $\sqrt{52 - j17}$, gives both $\gamma = j(\omega/c)\sqrt{52 - j17}$ and $\eta = \eta_0/\sqrt{52 - j17}$.

> [!solution]- Solution
> **Setup.** The data use the complex-permittivity reading of $\sigma + j\omega\epsilon = j\omega\epsilon_c$ (Lecture 22 §3), so the lossless formulas carry over with $\epsilon\to\epsilon_c$.
>
> **(a)** $\omega = 2\pi\times2.45\times10^9 = 1.539\times10^{10}$ rad/s. The imaginary part of $\epsilon_c$ is $\sigma/\omega = 17\epsilon_0$, so
> $$
> \sigma = 17\,\omega\epsilon_0 = 2.31\ \text{S/m},\qquad \frac{\sigma}{\omega\epsilon} = \frac{17}{52} = 0.327 .
> $$
> No. At one frequency only the total $\sigma + j\omega\epsilon$ (equivalently $\epsilon_c$) enters Maxwell's equations, so every loss mechanism, moving ions or a lagging polarization, ends up in the one number 17 (Lecture 22 §8). The 2.31 S/m is an *effective* conductivity.
>
> **(b)** $\omega/c = 51.31$ rad/m. For the square root, $\lvert52 - j17\rvert = 54.71$ at an angle of $-18.10^\circ$; take the root with a positive real part, $\sqrt{54.71}$ at $-9.05^\circ$: $\sqrt{52 - j17} = 7.304 - j1.164$. Then
> $$
> \gamma = j\frac{\omega}{c}\sqrt{52 - j17} = 51.31\,(1.164 + j7.304) = 59.7 + j374.8\ \text{m}^{-1}.
> $$
> So $\delta = 1/\alpha = 1.67$ cm, $\lambda = 2\pi/\beta = 1.68$ cm (12.24 cm in air) and $v_p = \omega/\beta = 4.11\times10^7$ m/s.
>
> **(c)** $\eta = \eta_0/\sqrt{52 - j17} = 120\pi/(7.397\,e^{-j9.05^\circ}) = 50.97\,e^{j9.05^\circ}\ \Omega$, and $\lvert\mathbf{H}\rvert = 1000/50.97 = 19.6$ A/m. Check: $\tau = \tan^{-1}(\alpha/\beta) = 9.05^\circ$ ✓.
>
> **(d)** $\langle S\rangle(z) = \dfrac{E_0^2}{2\lvert\eta\rvert}\cos\tau\,e^{-2\alpha z}$. At the surface, $\dfrac{10^6}{2\times50.97}\times0.9875 = 9.69$ kW/m². With $2\alpha = 119.4$ m⁻¹, it is $9.69\,e^{-1.194} = 2.93$ kW/m² at 1 cm and $9.69\,e^{-2.388} = 0.889$ kW/m² at 2 cm. Half of the power is gone at $z = \ln2/(2\alpha) = 5.8$ mm.
>
> **Check:** $\lambda/\delta = 2\pi\alpha/\beta = 2\pi\tan\tau = 1.001$, so $\delta$ and $\lambda$ are almost equal here, as computed. And the imperfect-dielectric shortcut of Lecture 22 §6, $\alpha\approx(\sigma/2)\sqrt{\mu_0/\epsilon} = 60.5$ Np/m, is only 1.3 % high at $\sigma/\omega\epsilon = 0.33$.
>
> **Watch out:** $\delta = 1.67$ cm is where the *field* is down to 37 %. By then 86 % of the power is gone, and 70 % is already absorbed in the first centimetre. That is why a thick piece cooks from the outside in.
>
> **Answer.** (a) $\sigma = 2.31$ S/m, $\sigma/\omega\epsilon = 0.327$; no, one frequency gives only the total loss. (b) $\gamma = 59.7 + j374.8$ m⁻¹, $\delta = 1.67$ cm, $\lambda = 1.68$ cm, $v_p = 4.11\times10^7$ m/s. (c) $\eta = 50.97\,e^{j9.05^\circ}\ \Omega$, $\lvert\mathbf{H}\rvert = 19.6$ A/m. (d) 9.69, 2.93 and 0.889 kW/m² at 0, 1 and 2 cm; half of the power is absorbed within 5.8 mm.

### 22.8 Power soaking into lossy ground

> [!medium] Medium · time-average power · attenuation · lossy media
> Wet ground fills the region $z<0$ below its surface $z = 0$; the $z$ axis points **up**. A 1 MHz plane wave travels down into the ground, where its electric-field phasor is
> $$
> \tilde{\mathbf{E}} = \hat{y}\,20\,e^{0.05(1 + j\sqrt3)z}\ \text{V/m}\qquad(z\le0,\ z\text{ in m}).
> $$
> The ground is non-magnetic; use $\mu_0 = 4\pi\times10^{-7}$ H/m.
> (a) Check the direction of travel from the phasor. Find $\alpha$, $\beta$, $\delta$ and $\lambda$.
> (b) Find $\eta$ in polar form and the phasor $\tilde{\mathbf{H}}$.
> (c) Find the time-average Poynting vector $\langle\mathbf{S}\rangle$ as a function of $z$, and its value just below the surface.
> (d) At what depth has the power density fallen to 1 % of its value at the surface? At what depth has $\lvert\mathbf{E}\rvert$ fallen to 1 %?
> (e) How much power per square metre of surface is absorbed in the top 20 m?
>
> *Source: FA23 Exam 3 #6(a) style, re-parameterized: $z$ points up, so the wave is $e^{+\gamma z}$; the ground is not a good conductor ($\tau = 30^\circ$ rather than 45°); $\eta$ is computed instead of left as a symbol; and the depth questions are new.*

> [!hint]- Hint
> The field is $e^{+\gamma z}$ with $\gamma = 0.05(1 + j\sqrt3) = 0.1e^{j60^\circ}$ m⁻¹. In $\tfrac12\text{Re}\{\tilde{\mathbf{E}}\times\tilde{\mathbf{H}}^*\}$ the $e^{\pm j\beta z}$ factors cancel, the two $e^{\alpha z}$ factors multiply, and $1/\eta^*$ contributes $e^{j\tau}/\lvert\eta\rvert$.

> [!solution]- Solution
> **Setup.** Let $d = -z$ be the depth. The power density goes as $e^{2\alpha z} = e^{-2\alpha d}$, the field only as $e^{-\alpha d}$.
>
> **(a)** $\tilde{\mathbf{E}}\propto e^{\gamma z}$ with $\gamma = 0.05 + j0.0866$ m⁻¹ $= 0.1\,e^{j60^\circ}$ m⁻¹. The phase factor $e^{+j\beta z}$ gives $\cos(\omega t + \beta z)$, travel toward $-z$, which is down ✓, and the amplitude $e^{0.05z}$ shrinks going down ✓. So $\alpha = 0.05$ Np/m, $\beta = 0.0866$ rad/m, $\delta = 20$ m and $\lambda = 2\pi/\beta = 72.6$ m.
>
> **(b)** $\omega\mu_0 = 2\pi\times10^6\times4\pi\times10^{-7} = 0.8\pi^2\ \Omega$/m, so
> $$
> \eta = \frac{j\omega\mu_0}{\gamma} = \frac{0.8\pi^2\,e^{j90^\circ}}{0.1\,e^{j60^\circ}} = 8\pi^2e^{j30^\circ} = 78.96\,e^{j30^\circ}\ \Omega .
> $$
> With $\hat u = -\hat{z}$ and $(-\hat{z})\times\hat{y} = +\hat{x}$:
> $$
> \tilde{\mathbf{H}} = \frac{\hat u\times\tilde{\mathbf{E}}}{\eta} = \hat{x}\,\frac{20}{8\pi^2}\,e^{-j30^\circ}e^{0.05(1 + j\sqrt3)z} = \hat{x}\,0.253\,e^{-j30^\circ}e^{0.05(1 + j\sqrt3)z}\ \text{A/m}.
> $$
>
> **(c)**
> $$
> \langle\mathbf{S}\rangle = \tfrac12\text{Re}\{\tilde{\mathbf{E}}\times\tilde{\mathbf{H}}^*\} = (\hat{y}\times\hat{x})\,\frac{20^2}{2\cdot8\pi^2}\cos30^\circ\,e^{0.1z} = -\hat{z}\,2.19\,e^{0.1z}\ \text{W/m}^2 .
> $$
> Just below the surface, $\tfrac{25\sqrt3}{2\pi^2} = 2.194$ W/m² flows down.
>
> **(d)** Power: $e^{-0.1d} = 0.01$ at $d = 10\ln100 = 46.1$ m. Field: $e^{-0.05d} = 0.01$ at $d = 20\ln100 = 92.1$ m, twice as deep.
>
> **(e)** $2.194\times(1 - e^{-2}) = 1.90$ W/m², that is, 86.5 % of what enters.
>
> **Check:** $\gamma\eta = 0.1e^{j60^\circ}\cdot8\pi^2e^{j30^\circ} = j0.8\pi^2 = j\omega\mu_0$ ✓, and $\langle\mathbf{S}\rangle$ points along $-\hat{z}$, the direction of travel ✓. From $\gamma/\eta$, the ground behind these numbers has $\sigma = 1.10$ mS/m and $\epsilon = 11.4\epsilon_0$, so $\sigma/\omega\epsilon = \sqrt3$.
>
> **Watch out:** dropping $\cos\tau$ overstates the power by 15 % (2.53 instead of 2.19 W/m²), and using $e^{-\alpha d}$ for the power puts the 1 % depth at 92 m instead of 46 m.
>
> **Answer.** (a) Down ($-z$); $\alpha = 0.05$ Np/m, $\beta = 0.0866$ rad/m, $\delta = 20$ m, $\lambda = 72.6$ m. (b) $\eta = 8\pi^2e^{j30^\circ} = 78.96\,e^{j30^\circ}\ \Omega$; $\tilde{\mathbf{H}} = \hat{x}\,0.253\,e^{-j30^\circ}e^{0.05(1 + j\sqrt3)z}$ A/m. (c) $\langle\mathbf{S}\rangle = -\hat{z}\,2.19\,e^{0.1z}$ W/m²: 2.19 W/m² downward at the surface. (d) Power at 1 % at a depth of 46.1 m; field at 1 % at 92.1 m. (e) 1.90 W/m².

## Hard

### 22.9 Decoding a wave toward minus y

> [!hard] Hard · damped waves · propagation constant · complex intrinsic impedance
> In conducting media the plane-wave parameters satisfy $\gamma\eta = j\omega\mu$ and $\gamma/\eta = \sigma + j\omega\epsilon$. In a non-magnetic medium,
> $$
> \mathbf{E}(y,t) = \hat{z}\,8e^{y}\cos(6\times10^8t + 7y + 30^\circ)\ \text{V/m}\qquad(y\text{ in m},\ t\text{ in s}).
> $$
> Use $\epsilon_0 = 10^{-9}/36\pi$ F/m, $\mu_0 = 4\pi\times10^{-7}$ H/m, $\tan^{-1}(1/7) = 8.13^\circ$ and $\sqrt2 = 1.414$.
> (a) Which way does the wave travel? Find $\alpha$, $\beta$ and $\gamma$, with $\gamma$ also in polar form.
> (b) Find $\lambda$, $f$, $v_p$ and the penetration depth $\delta$.
> (c) Find $\lvert\eta\rvert$ and $\tau = \angle\eta$.
> (d) Find $\mathbf{H}(y,t)$, direction included. At a fixed point, by how much time does $\mathbf{H}$ lag $\mathbf{E}$?
> (e) Find $\sigma$, $\epsilon$ (as a multiple of $\epsilon_0$) and $\sigma/\omega\epsilon$. Where does the medium sit between a perfect dielectric and a good conductor?
>
> *Source: SP17 Exam 3 #3, re-parameterized: travel toward $-y$ instead of $+x$, $\alpha:\beta = 1:7$ instead of the exam's 3-4-5 triangle, a new $\omega$, amplitude and phase, and part (e) added.*

> [!hint]- Hint
> The $t$ and $y$ terms have the same sign. Then follow the recipe: $\eta = j\omega\mu_0/\gamma$; $\tilde{\mathbf{H}} = \hat u\times\tilde{\mathbf{E}}/\eta$ with $\hat u$ the direction of travel; and $\gamma/\eta = \gamma^2/(j\omega\mu_0) = \sigma + j\omega\epsilon$.

> [!solution]- Solution
> **Setup.** Lecture 22's decoding recipe (§5): read the numbers off, then find $\eta$, then the other field, then the medium.
>
> **(a)** $6\times10^8t$ and $+7y$ have the same sign, so the wave travels toward $-\hat{y}$, and the amplitude $8e^{y}$ shrinks toward $-y$ ✓. $\omega = 6\times10^8$ rad/s, $\alpha = 1$ Np/m and $\beta = 7$ rad/m, so
> $$
> \gamma = 1 + j7\ \text{m}^{-1} = 5\sqrt2\,e^{j81.87^\circ} = 7.07\,e^{j81.87^\circ}\ \text{m}^{-1},
> $$
> since $\lvert\gamma\rvert = \sqrt{50}$ and $\angle\gamma = 90^\circ - \tan^{-1}(1/7)$. As a phasor, $\tilde{\mathbf{E}} = \hat{z}\,8e^{j30^\circ}e^{+\gamma y}$.
>
> **(b)** $\lambda = 2\pi/7 = 0.898$ m, $f = \omega/2\pi = 95.5$ MHz, $v_p = \omega/\beta = 8.57\times10^7$ m/s and $\delta = 1/\alpha = 1$ m.
>
> **(c)** $\omega\mu_0 = 6\times10^8\times4\pi\times10^{-7} = 240\pi$, so
> $$
> \eta = \frac{j240\pi}{1 + j7} = \frac{j240\pi(1 - j7)}{50} = 4.8\pi(7 + j) = 105.6 + j15.1\ \Omega,
> $$
> with $\lvert\eta\rvert = 240\pi/(5\sqrt2) = 24\sqrt2\,\pi = 106.6\ \Omega$ and $\tau = \tan^{-1}(1/7) = 8.13^\circ$.
>
> **(d)** $\hat u = -\hat{y}$ and $(-\hat{y})\times\hat{z} = -\hat{x}$. Divide the amplitude by $\lvert\eta\rvert$, $8/106.6 = 0.0750$ A/m, and subtract $\tau$ from the phase, $30^\circ - 8.13^\circ = 21.87^\circ$:
> $$
> \begin{gathered}
> \tilde{\mathbf{H}} = -\hat{x}\,75.0\,e^{j21.87^\circ}e^{(1 + j7)y}\ \text{mA/m},\\[4pt]
> \mathbf{H} = -\hat{x}\,75.0\,e^{y}\cos(6\times10^8t + 7y + 21.87^\circ)\ \text{mA/m}.
> \end{gathered}
> $$
> $\mathbf{H}$ lags $\mathbf{E}$ by $\tau/\omega = 0.1419/(6\times10^8) = 0.236$ ns. Check: $\mathbf{E}\times\mathbf{H}\parallel\hat{z}\times(-\hat{x}) = -\hat{y}$, the direction of travel ✓.
>
> **(e)** $\gamma^2 = (1 + j7)^2 = -48 + j14$, so
> $$
> \sigma + j\omega\epsilon = \frac{\gamma^2}{j\omega\mu_0} = \frac{-48 + j14}{j240\pi} = \frac{14 + j48}{240\pi}\ \text{S/m}.
> $$
> So $\sigma = 14/240\pi = 7/120\pi = 18.6$ mS/m, and $\omega\epsilon = 48/240\pi = 1/5\pi$ gives $\epsilon = 1/(5\pi\times6\times10^8) = 1.06\times10^{-10}$ F/m $= 12\epsilon_0$. The ratio is $\sigma/\omega\epsilon = 14/48 = 7/24 = 0.29$: the conduction current is 29 % of the displacement current. That is on the imperfect-dielectric side of the crossover. Even though 0.29 is hardly "$\ll1$", the Lecture 22 §6 shortcuts $\alpha\approx(\sigma/2)\sqrt{\mu/\epsilon} = 7/(2\sqrt{12}) = 1.010$ Np/m and $\beta\approx\omega\sqrt{\mu\epsilon} = \sqrt{48} = 6.93$ rad/m are only about 1 % off the exact 1 and 7 (1.04 % high and 1.03 % low).
>
> **Check:** $\lvert\gamma\rvert\lvert\eta\rvert = 5\sqrt2\times24\sqrt2\,\pi = 240\pi = \omega\mu_0$ ✓; $\tan2\tau = \tan16.26^\circ = 0.292 = \sigma/\omega\epsilon$ ✓; $\beta>\alpha$ and $\tau<45^\circ$ ✓.
>
> **Watch out:** the direction of $\mathbf{H}$ comes from $(-\hat{y})\times\hat{z} = -\hat{x}$. A remembered "$\mathbf{E}$ along $z$ gives $\mathbf{H}$ along $y$" belongs to travel along $x$.
>
> **Answer.** (a) Toward $-\hat{y}$; $\alpha = 1$ Np/m, $\beta = 7$ rad/m, $\gamma = 1 + j7$ m⁻¹ $= 7.07\,e^{j81.87^\circ}$ m⁻¹. (b) $\lambda = 0.898$ m, $f = 95.5$ MHz, $v_p = 8.57\times10^7$ m/s, $\delta = 1$ m. (c) $\lvert\eta\rvert = 106.6\ \Omega$, $\tau = 8.13^\circ$. (d) $\mathbf{H} = -\hat{x}\,75.0\,e^{y}\cos(6\times10^8t + 7y + 21.87^\circ)$ mA/m, lagging $\mathbf{E}$ by 0.236 ns. (e) $\sigma = 18.6$ mS/m, $\epsilon = 12\epsilon_0 = 1.06\times10^{-10}$ F/m, $\sigma/\omega\epsilon = 7/24\approx0.29$: between the two limits, on the imperfect-dielectric side.

### 22.10 Two components in a magnetic medium

> [!hard] Hard · damped waves · phasor fields · regimes
> A plane wave with $\omega = 3\times10^8$ rad/s travels in a medium with $\mu = 4\mu_0$ and unknown real $\epsilon$ and $\sigma$. Its electric-field phasor is
> $$
> \tilde{\mathbf{E}} = (6\hat{x} - j8\hat{y})\,e^{(3 + j5)z}\ \text{V/m}\qquad(z\text{ in m}).
> $$
> Use $\gamma\eta = j\omega\mu$, $\gamma/\eta = \sigma + j\omega\epsilon$, $\epsilon_0 = 10^{-9}/36\pi$ F/m, $\mu_0 = 4\pi\times10^{-7}$ H/m, $\tan^{-1}(3/5) = 30.96^\circ$ and $\sqrt{34} = 5.831$.
> (a) Which way does the wave travel? Find $\alpha$, $\beta$, $\lambda$, $\delta$ and $v_p$.
> (b) Find $\eta$ as $\lvert\eta\rvert e^{j\tau}$.
> (c) Find $\tilde{\mathbf{H}}(z)$, and write $\mathbf{E}(z,t)$ and $\mathbf{H}(z,t)$.
> (d) Find $\sigma/\omega\epsilon$ and classify the medium: perfect dielectric, imperfect dielectric, in between, good conductor or perfect conductor. Then find $\sigma$ and $\epsilon$.
> (e) Find $\langle\mathbf{S}\rangle(z)$. What share of it does each component of $\tilde{\mathbf{E}}$ carry?
>
> *Source: SP19 Exam 3 #1 style, re-parameterized: $\mu = 4\mu_0$ instead of $2\mu_0$, travel toward $-z$ instead of $+y$, two field components with a 90° phase difference, $\alpha:\beta = 3:5$ instead of $1:\sqrt3$, and part (e) added.*

> [!hint]- Hint
> Both components share the same $\gamma$ and $\eta$, so treat them as two waves travelling together. Do the cross product one component at a time: $(-\hat{z})\times\hat{x}$ and $(-\hat{z})\times\hat{y}$.

> [!solution]- Solution
> **Setup.** $e^{+\gamma z}$ means travel toward $-\hat{z}$. Both components carry the same $e^{\gamma z}$, so every step of the recipe works component by component.
>
> **(a)** $\gamma = 3 + j5$ m⁻¹ in $e^{+\gamma z}$: the phase $e^{+j5z}$ travels toward $-z$, and the amplitude $e^{3z}$ shrinks toward $-z$ ✓. So $\alpha = 3$ Np/m, $\beta = 5$ rad/m, $\lambda = 2\pi/5 = 1.26$ m, $\delta = 1/3$ m $= 0.333$ m and $v_p = 3\times10^8/5 = 6\times10^7$ m/s.
>
> **(b)** $\omega\mu = 3\times10^8\times4\times4\pi\times10^{-7} = 480\pi$, so
> $$
> \eta = \frac{j480\pi}{3 + j5} = \frac{j480\pi(3 - j5)}{34} = \frac{240\pi}{17}(5 + j3) = 221.8 + j133.1\ \Omega = 258.6\,e^{j30.96^\circ}\ \Omega,
> $$
> with $\lvert\eta\rvert = 480\pi/\sqrt{34}$ and $\tau = \tan^{-1}(3/5) = 30.96^\circ$.
>
> **(c)** With $\hat u = -\hat{z}$: $(-\hat{z})\times\hat{x} = -\hat{y}$ and $(-\hat{z})\times\hat{y} = +\hat{x}$, so $\hat u\times(6\hat{x} - j8\hat{y}) = -6\hat{y} - j8\hat{x}$ and
> $$
> \tilde{\mathbf{H}} = \frac{-j8\hat{x} - 6\hat{y}}{\eta}\,e^{(3 + j5)z} = \Big[\hat{x}\,30.93\,e^{-j120.96^\circ} - \hat{y}\,23.20\,e^{-j30.96^\circ}\Big]e^{(3 + j5)z}\ \text{mA/m},
> $$
> using $8/\lvert\eta\rvert = 30.93$ mA/m, $6/\lvert\eta\rvert = 23.20$ mA/m and $-j = e^{-j90^\circ}$. In the time domain (the $-j8$ is a sine):
> $$
> \begin{aligned}
> \mathbf{E} &= e^{3z}\big[\hat{x}\,6\cos(3\times10^8t + 5z) + \hat{y}\,8\sin(3\times10^8t + 5z)\big]\ \text{V/m},\\
> \mathbf{H} &= e^{3z}\big[\hat{x}\,30.93\cos(3\times10^8t + 5z - 120.96^\circ) - \hat{y}\,23.20\cos(3\times10^8t + 5z - 30.96^\circ)\big]\ \text{mA/m}.
> \end{aligned}
> $$
> $H_x$ is $E_y/\eta$ and $H_y$ is $-E_x/\eta$: each lags its partner by 30.96°.
>
> **(d)** $\gamma^2 = (3 + j5)^2 = -16 + j30$, so
> $$
> \frac{\sigma}{\omega\epsilon} = \frac{2\alpha\beta}{\beta^2 - \alpha^2} = \frac{30}{16} = 1.875 .
> $$
> That is neither $\ll1$ nor $\gg1$: **in between**. The conduction current is about twice the displacement current, and $\tau = 31^\circ$ is far from both 0 and 45°. From $\gamma/\eta = \gamma^2/(j\omega\mu) = (30 + j16)/480\pi$: $\sigma = 30/480\pi = 1/16\pi = 19.9$ mS/m, and $\omega\epsilon = 16/480\pi$ gives $\epsilon = 3.54\times10^{-11}$ F/m $= 4\epsilon_0$.
>
> **(e)** $\tilde{\mathbf{E}}\times\tilde{\mathbf{H}}^* = \big[(6)(-6)\,\hat{x}\times\hat{y} + (-j8)(+j8)\,\hat{y}\times\hat{x}\big]\dfrac{e^{6z}}{\eta^*} = -\hat{z}\,\dfrac{36 + 64}{\eta^*}\,e^{6z}$, so
> $$
> \langle\mathbf{S}\rangle = -\hat{z}\,\frac{100}{2\lvert\eta\rvert}\cos\tau\,e^{6z} = -\hat{z}\,\frac{25}{48\pi}\,e^{6z} = -\hat{z}\,0.166\,e^{6z}\ \text{W/m}^2 .
> $$
> The $x$ component carries 36/100 = 36 % (0.060 W/m² at $z = 0$) and the $y$ component 64 % (0.106 W/m²). The powers of perpendicular components add, and their 90° phase difference does not matter.
>
> **Check:** $\gamma\eta = (3 + j5)(5 + j3)\tfrac{240\pi}{17} = j34\cdot\tfrac{240\pi}{17} = j480\pi = j\omega\mu$ ✓, and $\langle\mathbf{S}\rangle$ points along $-\hat{z}$, the direction of travel ✓. Without its conductivity this medium, with $\mu_r = \epsilon_r = 4$, would have $\eta = 120\pi$ exactly.
>
> **Watch out:** with $\mu_0$ in place of $4\mu_0$, $\lvert\eta\rvert$ comes out 4 times too small (64.7 Ω) and $\sigma$ and $\epsilon$ 4 times too large. Only $\sigma/\omega\epsilon$ and $\tau$ survive.
>
> **Answer.** (a) Toward $-\hat{z}$; $\alpha = 3$ Np/m, $\beta = 5$ rad/m, $\lambda = 1.26$ m, $\delta = 0.333$ m, $v_p = 6\times10^7$ m/s. (b) $\eta = 258.6\,e^{j30.96^\circ}\ \Omega$. (c) $\tilde{\mathbf{H}} = (-j8\hat{x} - 6\hat{y})e^{(3 + j5)z}/\eta$; $\mathbf{H} = e^{3z}[\hat{x}\,30.93\cos(3\times10^8t + 5z - 120.96^\circ) - \hat{y}\,23.20\cos(3\times10^8t + 5z - 30.96^\circ)]$ mA/m, with $\mathbf{E} = e^{3z}[\hat{x}\,6\cos(3\times10^8t + 5z) + \hat{y}\,8\sin(3\times10^8t + 5z)]$ V/m. (d) $\sigma/\omega\epsilon = 15/8$: in between; $\sigma = 19.9$ mS/m, $\epsilon = 4\epsilon_0$. (e) $\langle\mathbf{S}\rangle = -\hat{z}\,0.166\,e^{6z}$ W/m², 36 % from $E_x$ and 64 % from $E_y$.

### 22.11 Current sheet in a lossy medium

> [!hard] Hard · current sheet radiation · damped waves · time-average power
> A current sheet on the plane $x = 0$ carries $\mathbf{J}_s = \hat{z}\,4\cos(\omega t)$ A/m with $\omega = 3\times10^8$ rad/s. All space is filled with the medium of 22.6 ($\mu_0$, $\epsilon = 5\epsilon_0$, $\sigma = 1/(10\pi)$ S/m), for which $\gamma = 2 + j3$ m⁻¹ and $\eta = (120\pi/13)(3 + j2) = 104.6\,e^{j33.69^\circ}\ \Omega$.
> (a) Write $\tilde{\mathbf{E}} = \hat{z}\,A\,e^{-\gamma\lvert x\rvert}$ on both sides, find $\tilde{\mathbf{H}}$ on each side from the direction of travel, and use the boundary conditions at the sheet to find $A$.
> (b) Write $\mathbf{E}(x,t)$ and $\mathbf{H}(x,t)$ for $x>0$. At the sheet, is $\mathbf{E}$ exactly opposite to $\mathbf{J}_s$ at every instant?
> (c) Find $\langle\mathbf{S}\rangle$ on both sides, and the time-average power per unit area that the current gives up, $\langle-\mathbf{J}_s\cdot\mathbf{E}\rangle$ at $x = 0$. Check the balance.
> (d) What fraction of the power sent into $x>0$ is absorbed within $0<x<\delta$? Within what distance is 99 % of it absorbed?
> (e) Find the field amplitude at the sheet and the power supplied for the same current in a medium with the same $\epsilon$ and $\mu$ but $\sigma = 0$. Which medium draws more power from the current, and why?
>
> *Source: original (the sheet of Lecture 22 §7 on a new plane, with a new current direction and medium).*

> [!hint]- Hint
> On each side the wave travels away from the sheet: $\hat u = +\hat{x}$ for $x>0$ and $-\hat{x}$ for $x<0$. At $x = 0$ the normal $\hat n = \hat{x}$ points from region 2 ($x<0$) into region 1 ($x>0$), and $\hat{x}\times(\tilde{\mathbf{H}}_1 - \tilde{\mathbf{H}}_2) = \tilde{\mathbf{J}}_s = 4\hat{z}$ A/m.

> [!solution]- Solution
> **Setup.** Lecture 19's boundary-condition argument in phasor form, as in Lecture 22 §7: outgoing waves on both sides, the delay $e^{-j\beta\lvert x\rvert}$ replaced by $e^{-\gamma\lvert x\rvert}$, and a complex $\eta$. The phasor current is $\tilde{\mathbf{J}}_s = 4\hat{z}$ A/m.
>
> **(a)** Tangential $\mathbf{E}$ is continuous at $x = 0$, so both sides share the amplitude $A$. With $\hat{x}\times\hat{z} = -\hat{y}$ and $(-\hat{x})\times\hat{z} = +\hat{y}$:
> $$
> \tilde{\mathbf{H}} = -\hat{y}\,\frac{A}{\eta}\,e^{-\gamma x}\ \ (x>0),\qquad \tilde{\mathbf{H}} = +\hat{y}\,\frac{A}{\eta}\,e^{\gamma x}\ \ (x<0).
> $$
> The jump condition reads $\hat{x}\times\big(-\tfrac{2A}{\eta}\hat{y}\big) = -\tfrac{2A}{\eta}\hat{z} = 4\hat{z}$, so $A = -2\eta$:
> $$
> \tilde{\mathbf{E}} = -\hat{z}\,2\eta\,e^{-\gamma\lvert x\rvert},\qquad \tilde{\mathbf{H}} = \pm\hat{y}\,2\,e^{-\gamma\lvert x\rvert}\ \text{A/m}\quad(x\gtrless0).
> $$
> These are $\tilde{\mathbf{E}} = -\tfrac\eta2\tilde{\mathbf{J}}_s$ and $\tilde{\mathbf{H}} = \tfrac12\tilde{\mathbf{J}}_s\times\hat n$ again: $\hat{z}\times\hat{x} = +\hat{y}$ for $x>0$ and $\hat{z}\times(-\hat{x}) = -\hat{y}$ for $x<0$.
>
> **(b)** $2\lvert\eta\rvert = 209.1$ V/m and $\angle\eta = 33.69^\circ$, so for $x>0$
> $$
> \begin{gathered}
> \mathbf{E} = -\hat{z}\,209.1\,e^{-2x}\cos(\omega t - 3x + 33.69^\circ)\ \text{V/m},\\[4pt]
> \mathbf{H} = \hat{y}\,2\,e^{-2x}\cos(\omega t - 3x)\ \text{A/m}.
> \end{gathered}
> $$
> At the sheet, $\mathbf{E} = -\hat{z}\,209.1\cos(\omega t + 33.69^\circ)$ V/m while $\mathbf{J}_s = \hat{z}\,4\cos\omega t$ A/m. $\mathbf{E}$ points against the current but not exactly in step with it: $-\mathbf{E}$ leads the current by $\tau = 33.69^\circ$, that is, by $\tau/\omega = 1.96$ ns. $\mathbf{H}$ at the sheet is fixed by the current alone and stays in phase with it.
>
> **(c)** For $x>0$, with $(-\hat{z})\times\hat{y} = +\hat{x}$ and $\text{Re}\{\eta\} = 360\pi/13 = 87.0\ \Omega$:
> $$
> \langle\mathbf{S}\rangle = \tfrac12\text{Re}\big\{(-\hat{z}\,2\eta)\times(\hat{y}\,2)\big\}\,e^{-4x} = \hat{x}\,2\,\text{Re}\{\eta\}\,e^{-4x} = \hat{x}\,174.0\,e^{-4x}\ \text{W/m}^2 .
> $$
> For $x<0$ the same magnitude points along $-\hat{x}$. At the sheet,
> $$
> \langle-\mathbf{J}_s\cdot\mathbf{E}\rangle = \tfrac12\text{Re}\{-\tilde{\mathbf{J}}_s\cdot\tilde{\mathbf{E}}^*\} = \tfrac12\text{Re}\{4\cdot2\eta^*\} = 4\,\text{Re}\{\eta\} = 348.0\ \text{W/m}^2,
> $$
> exactly the $2\times174.0$ W/m² that leaves through the two faces ✓.
>
> **(d)** The flux falls as $e^{-4x}$. Within $\delta = 0.5$ m a fraction $1 - e^{-2} = 86.5$ % (150.4 W/m²) is absorbed, and 99 % within $x = \ln100/4 = 1.15$ m. Nothing reaches infinity.
>
> **(e)** With $\sigma = 0$, $\eta = 120\pi/\sqrt5 = 168.6\ \Omega$, which is real. The field at the sheet is then $2\eta = 337.2$ V/m, and the current supplies $\tfrac14J_0^2\eta = 674.4$ W/m², all of it carried off to infinity. The conducting medium draws only 348.0 W/m², about half. The sheet is a current source driving the two half-spaces in parallel, each presenting $\eta$, so it sees $\eta/2$ and delivers $\tfrac12J_0^2\,\text{Re}\{\eta/2\}$ per unit area; conduction lowers $\text{Re}\{\eta\}$ from 168.6 to 87.0 Ω.
>
> **Check:** at $x = 0$, $\hat{x}\times(\tilde{\mathbf{H}}_1 - \tilde{\mathbf{H}}_2) = \hat{x}\times4\hat{y} = 4\hat{z} = \tilde{\mathbf{J}}_s$ ✓, and on both sides the fields satisfy the phasor Faraday and Ampère–Maxwell laws with $\sigma + j\omega\epsilon$.
>
> **Answer.** (a) $A = -2\eta$: $\tilde{\mathbf{E}} = -\hat{z}\,2\eta\,e^{-\gamma\lvert x\rvert}$, $\tilde{\mathbf{H}} = \pm\hat{y}\,2e^{-\gamma\lvert x\rvert}$ A/m for $x\gtrless0$. (b) $\mathbf{E} = -\hat{z}\,209.1e^{-2x}\cos(\omega t - 3x + 33.69^\circ)$ V/m and $\mathbf{H} = \hat{y}\,2e^{-2x}\cos(\omega t - 3x)$ A/m; no: $-\mathbf{E}$ leads $\mathbf{J}_s$ by 33.69° (1.96 ns). (c) $\langle\mathbf{S}\rangle = \pm\hat{x}\,174.0\,e^{-4\lvert x\rvert}$ W/m² for $x\gtrless0$; the sheet supplies 348.0 W/m². (d) 86.5 %; 99 % within 1.15 m. (e) Without conduction, 337.2 V/m and 674.4 W/m²: the lossless medium draws about twice as much, because the current source sees $\text{Re}\{\eta\}$, which conduction lowers.

### 22.12 Three probes identify a medium

> [!hard] Hard · lossy media · complex intrinsic impedance · damped waves
> A uniform plane wave with $\omega = 3\times10^8$ rad/s travels along the $y$ axis through an unknown homogeneous medium with real $\mu$, $\epsilon$ and $\sigma$; the medium may be magnetic. Probe A at $y = 0$ and probe B at $y = -0.25$ m record the electric field, which has only a $z$ component. A small loop at A records the magnetic field, which has only an $x$ component:
> $$
> \begin{aligned}
> E_z(\text{A}) &= 10\cos(\omega t)\ \text{V/m},\\
> E_z(\text{B}) &= 12.84\cos(\omega t + 57.30^\circ)\ \text{V/m},\\
> H_x(\text{A}) &= 21.87\cos(\omega t - 14.04^\circ)\ \text{mA/m}.
> \end{aligned}
> $$
> The probes are less than one wavelength apart. Use $\mu_0 = 4\pi\times10^{-7}$ H/m and $\epsilon_0 = 10^{-9}/36\pi$ F/m.
> (a) Which way does the wave travel? Find $\alpha$, $\beta$ and $\gamma$.
> (b) Find $\eta$ from the records at A, and check its angle against $\gamma$.
> (c) Find $\mu$, $\sigma$, $\epsilon$ and $\sigma/\omega\epsilon$.
> (d) A classmate has only the two electric probes and assumes $\mu = \mu_0$. What $\sigma$ and $\epsilon$ does she report? Which of her conclusions are still right?
> (e) Find $\langle\mathbf{S}\rangle$ at A and at B, and the power absorbed per square metre of wavefront in the 0.25 m between them.
>
> *Source: original.*

> [!hint]- Hint
> The probe that sees the wave first, and stronger, is upstream. Over the 0.25 m from B to A the amplitude ratio is $e^{0.25\alpha}$ and the phase difference is $0.25\beta$ (in radians). At A, $\eta$ is the ratio of the $E_z$ and $H_x$ phasors, with the sign fixed by $\hat u\times\hat{z}$. Then use $\mu = \gamma\eta/j\omega$.

> [!solution]- Solution
> **Setup.** The records are three phasors: $\tilde E_z(\text{A}) = 10$ V/m, $\tilde E_z(\text{B}) = 12.84e^{j57.30^\circ}$ V/m and $\tilde H_x(\text{A}) = 21.87e^{-j14.04^\circ}$ mA/m. Build $\gamma$ from the two electric probes and $\eta$ from the electric and magnetic probes at A; the two product rules then give the medium.
>
> **(a)** B, at $y = -0.25$ m, leads A by 57.30° and is stronger, so the wave reaches B first and decays on its way to A: it travels toward $+\hat{y}$. With $\tilde E_z\propto e^{-\gamma y}$, $\tilde E_z(\text{B})/\tilde E_z(\text{A}) = e^{0.25\gamma}$, so
> $$
> \alpha = \frac{\ln(12.84/10)}{0.25} = 1.000\ \text{Np/m},\qquad \beta = \frac{57.30^\circ\times\pi/180}{0.25} = \frac{1.000\ \text{rad}}{0.25} = 4.00\ \text{rad/m},
> $$
> and $\gamma = 1 + j4$ m⁻¹ $= 4.12\,e^{j75.96^\circ}$ m⁻¹. "Less than a wavelength apart" rules out adding 360° to the phase difference.
>
> **(b)** For travel along $+\hat{y}$ with $\mathbf{E}$ along $\hat{z}$, $\hat{y}\times\hat{z} = +\hat{x}$, so $\tilde H_x = \tilde E_z/\eta$ and
> $$
> \eta = \frac{10}{21.87\times10^{-3}\,e^{-j14.04^\circ}} = 457.2\,e^{j14.04^\circ}\ \Omega = 443.6 + j110.9\ \Omega .
> $$
> Check: with a real $\mu$, $\tau$ must equal $90^\circ - \angle\gamma = \tan^{-1}(\alpha/\beta) = \tan^{-1}(1/4) = 14.04^\circ$ ✓. Had you guessed travel toward $-\hat{y}$, $\tilde H_x = -\tilde E_z/\eta$ would give $\eta$ a negative real part, which no passive medium has.
>
> **(c)** The angles of $\gamma$ and $\eta$ add to $75.96^\circ + 14.04^\circ = 90^\circ$, so $\gamma\eta = j\lvert\gamma\rvert\lvert\eta\rvert = j(4.123)(457.2) = j1885\ \Omega$/m and
> $$
> \mu = \frac{\gamma\eta}{j\omega} = \frac{1885}{3\times10^8} = 6.28\times10^{-6}\ \text{H/m} = 5.00\,\mu_0 .
> $$
> Next, $\sigma + j\omega\epsilon = \gamma/\eta = (4.123/457.2)\,e^{j(75.96^\circ - 14.04^\circ)} = 9.02\times10^{-3}\,e^{j61.93^\circ} = 4.24\times10^{-3} + j7.96\times10^{-3}$ S/m. So $\sigma = 4.24$ mS/m, and $\epsilon = 7.96\times10^{-3}/(3\times10^8) = 2.65\times10^{-11}$ F/m $= 3.00\,\epsilon_0$. The ratio is $\sigma/\omega\epsilon = 0.533 = 8/15$: between the two limits. In exact form, $\eta = \tfrac{600\pi}{17}(4 + j)\ \Omega$, $\mu = 5\mu_0$ and $\gamma/\eta = (8 + j15)/600\pi$ S/m.
>
> **(d)** With $\mu_0$, she computes $\sigma + j\omega\epsilon = \gamma^2/(j\omega\mu_0) = (-15 + j8)/(j120\pi) = (8 + j15)/120\pi$ S/m, so $\sigma' = 21.2$ mS/m and $\epsilon' = 15\epsilon_0$, both 5 times too large. Her $\lvert\eta\rvert = \omega\mu_0/\lvert\gamma\rvert = 91.4\ \Omega$ is 5 times too small. Still right: everything read from $\gamma$ alone ($\alpha$, $\beta$, $\lambda$, $\delta$, $v_p$, the direction), $\tau$, and $\sigma/\omega\epsilon = 8/15$, which does not contain $\mu$. Only the magnetic probe can reveal $\mu$.
>
> **(e)** At A, $\langle S_y\rangle = \tfrac12(10)(21.87\times10^{-3})\cos14.04^\circ = 0.106$ W/m² (exactly $1/3\pi$), along $+\hat{y}$. At B it is larger by $e^{2\alpha\times0.25} = e^{0.5}$: 0.175 W/m². The 0.25 m layer absorbs $0.175 - 0.106 = 0.069$ W/m².
>
> **Check:** $\lvert\gamma\rvert\lvert\eta\rvert = \sqrt{17}\times600\pi/\sqrt{17} = 600\pi = \omega\mu$ ✓, and with $\mu = 5\mu_0$, $\epsilon = 3\epsilon_0$ and $\sigma = 1/75\pi$ S/m the exact square root $\sqrt{j\omega\mu(\sigma + j\omega\epsilon)}$ returns $1 + j4$.
>
> **Answer.** (a) Toward $+\hat{y}$; $\alpha = 1.00$ Np/m, $\beta = 4.00$ rad/m, $\gamma = 1 + j4$ m⁻¹. (b) $\eta = 457\,e^{j14.04^\circ}\ \Omega$, consistent with $\tan^{-1}(\alpha/\beta)$. (c) $\mu = 5\mu_0$, $\sigma = 4.24$ mS/m, $\epsilon = 3\epsilon_0$, $\sigma/\omega\epsilon = 8/15$. (d) $\sigma' = 21.2$ mS/m and $\epsilon' = 15\epsilon_0$, 5 times too large; $\gamma$, $\tau$ and $\sigma/\omega\epsilon$ survive. (e) 0.106 W/m² at A, 0.175 W/m² at B, 0.069 W/m² absorbed.

### Sources for this page
The site's Lecture 22 page and the course notes behind it: the phasor table and its consequences (22.1), the Helmholtz equation in a conducting medium (22.2), the decoding recipe (22.3, 22.5, 22.9, 22.10), the margin formulas $\mu = \gamma\eta/j\omega$, $\sigma = \text{Re}\{\gamma/\eta\}$, $\epsilon = \text{Im}\{\gamma/\eta\}/\omega$ (22.12), the regime tests and the collisionless plasma (22.4), and the sheet in a conducting medium (22.11). Old exams, re-parameterized: SP17 Exam 3 #3 (22.9: travel toward $-y$, $\alpha:\beta = 1:7$, a new $\omega$, amplitude and phase, and the medium added), SP19 Exam 3 #1 (22.10: $\mu = 4\mu_0$, travel toward $-z$, two field components, $\alpha:\beta = 3:5$, and the power added), FA23 Exam 3 #6(a) (22.8: $z$ up so the wave is $e^{+\gamma z}$, $\tau = 30^\circ$, $\eta$ computed, and new depth questions), and the POSSIBLE / NOT POSSIBLE format of Summer 2020 HE3 #3a (22.4, with new statements). Original: 22.1–22.3, 22.5–22.7, 22.11 and 22.12. The material values in 22.7 are illustrative, chosen for this problem.

*Previous: [[practice/21-phasors-and-monochromatic-waves|Lecture 21 practice]] · next: [[practice/23-imperfect-dielectrics-and-good-conductors|Lecture 23 practice]] · [[practice/index|all practice]]*
