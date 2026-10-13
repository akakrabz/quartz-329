---
title: "Practice — Lecture 23: Imperfect dielectrics and good conductors"
description: "12 practice problems (5 easy, 3 medium, 4 hard) on the loss tangent σ/ωε with the medium's own ε and the crossover frequency σ/2πε, classifying a medium at a frequency or from a measured λ and δ, the imperfect-dielectric and good-conductor approximations checked against the exact γ and η, skin depth and its 1/√f scaling, power against depth in decibels, where the lost power goes, choosing a frequency to reach a submarine, a medium at its crossover, and the skin effect in a copper wire, each with a folded hint and a worked solution."
tags: [practice, waves]
lecture: 23
---

*Practice for [[3-maxwell-and-waves/23-imperfect-dielectrics-and-good-conductors|Lecture 23]] · concepts: [[concepts/loss-tangent]] · [[concepts/skin-depth]] · [[concepts/propagation-constant]] · [[concepts/intrinsic-impedance]] · all practice: [[practice/index|hub]] · by difficulty: [[practice/easy|easy]] · [[practice/medium|medium]] · [[practice/hard|hard]] · [[practice/topics|by topic]]*

Work each problem on paper first. Open the **hint** only when stuck, and the **solution** only after you have an answer you would hand in. Every answer here has been checked numerically, and every shortcut against the exact $\gamma$ and $\eta$ of Lecture 22.

One recipe does almost every problem on this page. **Classify first**, always with the medium's own $\epsilon$ (with $\epsilon_0\approx10^{-9}/36\pi$ F/m the ratio takes the no-calculator form on the right):
$$
p = \frac{\sigma}{\omega\epsilon} = \frac{18\times10^{9}\,\sigma}{f\,\epsilon_r}.
$$
- $p<0.1$, **imperfect dielectric**: $\alpha\approx\dfrac\sigma2\sqrt{\dfrac\mu\epsilon}$, while $\beta\approx\omega\sqrt{\mu\epsilon}$ and $\eta\approx\sqrt{\mu/\epsilon}$ keep their lossless values; $\angle\eta\approx p/2$.
- $p>10$, **good conductor**: with the skin depth $\delta = \dfrac{1}{\sqrt{\pi f\mu\sigma}}$, $\alpha\approx\beta\approx\dfrac1\delta$, $\lambda\approx2\pi\delta$, $v_p\approx\omega\delta$ and $\eta\approx\dfrac{1+j}{\sigma\delta}$. With $\mu = \mu_0$, $\pi f\mu_0\sigma = 4\pi^2\times10^{-7}f\sigma$.
- In between: the exact formulas of [[3-maxwell-and-waves/22-phasor-maxwell-equations-and-damped-waves|Lecture 22]].

Then the **power**: $\langle\mathbf{S}\rangle = \hat u\,\lvert E_0\rvert^2\cos\tau\,e^{-2\alpha d}/(2\lvert\eta\rvert)$, with $d$ the distance travelled into the medium and $\tau = \angle\eta$. Field and power both lose $8.686\,\alpha$ dB per metre.

## Easy

### 23.1 Six media at one frequency

> [!easy] Easy · loss tangent · regimes
> Six non-magnetic media, with handbook values of $\sigma$ and $\epsilon_r$: copper ($5.8\times10^{7}$ S/m, 1), seawater (4 S/m, 81), moist soil, i.e. loam ($10^{-2}$ S/m, 10), fresh water ($10^{-3}$ S/m, 80), dry earth ($10^{-5}$ S/m, 5) and Bakelite ($10^{-9}$ S/m, 4.9). Use $\epsilon_0\approx10^{-9}/36\pi$ F/m.
>
> (a) Find each medium's crossover frequency $f_c = \sigma/2\pi\epsilon$.
>
> (b) Classify each at $f = 3$ MHz as a good conductor ($\sigma/\omega\epsilon>10$), an imperfect dielectric ($\sigma/\omega\epsilon<0.1$) or neither.
>
> (c) A student classifies fresh water at 3 MHz using $\epsilon_0$ in place of $80\epsilon_0$. What verdict does that give?
>
> *Source: original (in the style of Rao's Table 5.3, with the course's no-calculator constants).*

> [!hint]- Hint
> With $\epsilon_0 = 10^{-9}/36\pi$, $f_c = 18\times10^{9}\,\sigma/\epsilon_r$ Hz, and $\sigma/\omega\epsilon = f_c/f$. One number per medium answers both (a) and (b).

> [!solution]- Solution
> The loss tangent compares the conduction current $\sigma\tilde{\mathbf{E}}$ with the displacement current $j\omega\epsilon\tilde{\mathbf{E}}$. It equals 1 at the crossover and falls as $1/f$:
> $$
> \frac{\sigma}{\omega\epsilon} = \frac{\sigma}{2\pi f\epsilon} = \frac{f_c}{f},\qquad f_c = \frac{\sigma}{2\pi\epsilon_r\epsilon_0} = \frac{18\times10^{9}\,\sigma}{\epsilon_r}\ \text{Hz}.
> $$
> (a) and (b) together, at $f = 3$ MHz:
>
> | medium | $f_c$ | $\sigma/\omega\epsilon$ at 3 MHz | verdict at 3 MHz |
> |---|---|---|---|
> | copper | $1.04\times10^{18}$ Hz | $3.5\times10^{11}$ | good conductor |
> | seawater | 0.889 GHz | 296 | good conductor |
> | moist soil | 18 MHz | 6.0 | neither |
> | fresh water | 225 kHz | 0.075 | imperfect dielectric |
> | dry earth | 36 kHz | 0.012 | imperfect dielectric |
> | Bakelite | 3.67 Hz | $1.2\times10^{-6}$ | imperfect dielectric |
>
> A medium is a good conductor more than a decade *below* its crossover and an imperfect dielectric more than a decade *above* it. Moist soil at 3 MHz is less than a decade below its 18 MHz crossover: its conduction current is only six times its displacement current. The good-conductor shortcut would put $\alpha$ 8.6 % too high and $\beta$ 8.0 % too low there, so it needs the exact formulas of Lecture 22.
>
> (c) With $\epsilon_0$ in place of $80\epsilon_0$ the ratio is $18\times10^{9}\times10^{-3}/(3\times10^{6}) = 6$, which reads as "neither". The true ratio is 80 times smaller, 0.075, and fresh water at 3 MHz is an imperfect dielectric.
>
> **Watch out:** a verdict belongs to a medium *at a frequency*, never to a material's name. Seawater is a good conductor at 3 MHz but an imperfect dielectric above about 9 GHz. Even Bakelite, the best insulator here, would be a good conductor below 0.37 Hz.
>
> **Answer.** (a) Copper $1.04\times10^{18}$ Hz, seawater 0.889 GHz, moist soil 18 MHz, fresh water 225 kHz, dry earth 36 kHz, Bakelite 3.67 Hz. (b) Copper and seawater are good conductors; moist soil ($\sigma/\omega\epsilon = 6$) is neither; fresh water, dry earth and Bakelite are imperfect dielectrics. (c) A ratio of 6 instead of 0.075, so "neither" instead of "imperfect dielectric".

### 23.2 Inside a good conductor

> [!easy] Easy · multiple choice · good conductor
> A uniform plane wave travels in a medium with $\sigma/\omega\epsilon\gg1$ (a good conductor). Which **one** statement is true?
>
> (a) Its phase velocity is larger than $1/\sqrt{\mu\epsilon}$, the speed the same $\epsilon$ and $\mu$ would give without $\sigma$.
>
> (b) Doubling the frequency halves the skin depth.
>
> (c) At a fixed point, $\mathbf{H}$ reaches each maximum one-eighth of a period after $\mathbf{E}$ does.
>
> (d) $\lvert\mathbf{E}\rvert/\lvert\mathbf{H}\rvert = \sqrt{\mu/\epsilon}$, as in a lossless medium.
>
> (e) Over one wavelength the time-average power falls by the factor $e^{-2\pi}\approx1/535$.
>
> *Source: SP17 Exam 3 #2(i) and SP18 Exam 3 #1(i) style, with new statements.*

> [!hint]- Hint
> Write everything with the skin depth: $\alpha = \beta = 1/\delta$, $v_p = \omega\delta$, $\eta = (1+j)/(\sigma\delta)$. Then ask what each statement claims about $v_p$, $\delta(f)$, the phase of $\eta$, $\lvert\eta\rvert$ and $e^{-2\alpha\lambda}$.

> [!solution]- Solution
> In a good conductor everything follows from one length: $\alpha = \beta = 1/\delta$ with $\delta = 1/\sqrt{\pi f\mu\sigma}$, $\lambda = 2\pi\delta$, $v_p = \omega\delta$ and $\eta = (1+j)/(\sigma\delta) = \lvert\eta\rvert e^{j\pi/4}$.
>
> **(c) is true.** $\tilde{\mathbf{H}} = \hat u\times\tilde{\mathbf{E}}/\eta$, and dividing by $\eta$ subtracts its phase, $\pi/4$ (exactly so in the good-conductor limit; 44.99997° for seawater at 1 kHz). So when $\mathbf{E}\propto\cos\omega t$ at some point, $\mathbf{H}\propto\cos(\omega t - \pi/4)$ there: each maximum of $\mathbf{H}$ comes $(\pi/4)/\omega = T/8$ later. In seawater at 1 kHz that is 125 µs.
>
> Why the others are false:
> - (a) $v_p = \omega\delta = \sqrt{2\omega/\mu\sigma}$. Divided by the lossless speed $1/\sqrt{\mu\epsilon}$ this is $\sqrt{2\omega\epsilon/\sigma}\ll1$: the wave is much *slower*. In seawater at 1 kHz, $5\times10^{4}$ m/s against $3.3\times10^{7}$ m/s.
> - (b) $\delta\propto1/\sqrt f$, so doubling $f$ divides $\delta$ by $\sqrt2$ (to 71 %). Halving $\delta$ takes four times the frequency.
> - (d) $\lvert\eta\rvert = \sqrt{\omega\mu/\sigma} = \sqrt{\mu/\epsilon}\,\sqrt{\omega\epsilon/\sigma}$, far below $\sqrt{\mu/\epsilon}$: 0.0444 Ω against 41.9 Ω in seawater at 1 kHz. A good conductor carries a large $\mathbf{H}$ with a small $\mathbf{E}$.
> - (e) $e^{-2\pi}$ is what happens to the **field**: $e^{-\alpha\lambda} = e^{-2\pi}\approx1/535$ because $\alpha\lambda = 2\pi$. The power goes as the field squared, so it falls by $e^{-4\pi}\approx3.5\times10^{-6}$. In decibels both are the same 54.6 dB, because a power ratio takes $10\log_{10}$ and a field ratio $20\log_{10}$.
>
> **Answer.** (c).

### 23.3 Regimes, true or false

> [!easy] Easy · true or false · loss tangent · regimes
> Use the handbook values seawater ($\sigma = 4$ S/m, $\epsilon_r = 81$) and fresh water ($\sigma = 10^{-3}$ S/m, $\epsilon_r = 80$), both non-magnetic, and $\epsilon_0\approx10^{-9}/36\pi$ F/m. True or false?
>
> (a) $\sigma/\omega\epsilon$ is the tangent of the angle by which the displacement current density leads the total current density.
>
> (b) Fresh water is a good conductor at 1 MHz, because there $\sigma/\omega\epsilon_0 = 18$.
>
> (c) Seawater conducts so well that it is a good conductor at every frequency up to 10 GHz.
>
> (d) For any real, positive $\sigma$, $\epsilon$ and $\mu$, the attenuation constant $\alpha$ is smaller than the phase constant $\beta$.
>
> (e) In an imperfect dielectric with constant $\sigma$ and $\epsilon$, doubling the frequency doubles $\beta$ but leaves $\alpha$ almost unchanged.
>
> (f) $\delta = 1/\sqrt{\pi f\mu\sigma}$ gives the penetration depth of fresh water at 100 MHz.
>
> *Source: original.*

> [!hint]- Hint
> For the statements about a medium, compute $\sigma/\omega\epsilon$ with that medium's own $\epsilon$ at the stated frequency. For the general ones, use $\alpha/\beta = \tan\tau$ with $\tau = \tfrac12\tan^{-1}(\sigma/\omega\epsilon)$, and the two rows of the regime table.

> [!solution]- Solution
> (a) **True.** Draw the phasors with $\tilde{\mathbf{E}}$ real. The conduction current $\sigma\tilde{\mathbf{E}}$ lies along the real axis and the displacement current $j\omega\epsilon\tilde{\mathbf{E}}$ along the imaginary axis. Their sum, the total current, leans away from the imaginary axis by an angle $\theta$ with $\tan\theta = \sigma/\omega\epsilon$, so the displacement current leads it by $\theta$. Read as a ratio, the loss tangent is conduction over displacement current, not the reverse.
>
> (b) **False.** The ratio must use the water's own permittivity: $18\times10^{9}\times10^{-3}/(10^{6}\times80) = 0.225$. Fresh water at 1 MHz is between the regimes, nearer the dielectric side. With $\epsilon_0$ the ratio is 80 times too large.
>
> (c) **False.** Seawater's crossover is $f_c = 18\times10^{9}\times4/81 = 0.89$ GHz. It is a good conductor only below about 89 MHz. At 1 GHz its $\sigma/\omega\epsilon$ is 0.89 (in between), and at 10 GHz it is 0.089, an imperfect dielectric.
>
> (d) **True.** $\alpha/\beta = \tan\tau$ with $\tau = \tfrac12\tan^{-1}(\sigma/\omega\epsilon)<45^\circ$, so $\alpha<\beta$ for every finite $\sigma$. The two become equal only in the good-conductor limit. (A collisionless plasma below its plasma frequency, Lecture 21, is not such a medium: there no wave travels at all.)
>
> (e) **True.** $\alpha\approx(\sigma/2)\sqrt{\mu/\epsilon}$ contains no frequency, while $\beta\approx\omega\sqrt{\mu\epsilon}$ is proportional to it. Fresh water has $\alpha = 0.0211$ Np/m at both 100 and 200 MHz, while $\beta$ goes from 18.7 to 37.5 rad/m.
>
> (f) **False.** That formula is the good-conductor row. Fresh water at 100 MHz has $\sigma/\omega\epsilon = 0.00225$, an imperfect dielectric, and its penetration depth is $(2/\sigma)\sqrt{\epsilon/\mu} = 47$ m. The skin-depth formula gives 1.6 m, 30 times too short.
>
> **Answer.** (a) T, (b) F, (c) F, (d) T, (e) T, (f) F.

### 23.4 Skin depth in gold

> [!easy] Easy · skin depth · good conductor
> Gold has $\sigma = 4.1\times10^{7}$ S/m and $\mu = \mu_0$.
>
> (a) Show that its skin depth is $\delta\approx0.0786/\sqrt f$ m ($f$ in Hz), and evaluate it at 60 Hz and at 1 MHz.
>
> (b) Using only the $1/\sqrt f$ scaling and your 1 MHz value, find $\delta$ at 4 MHz and at 10 GHz.
>
> (c) A connector pin is plated with 1.5 µm of gold. At 10 GHz, how many skin depths thick is the plating, and what fraction of the power entering the gold is absorbed within it (treat the gold as if it continued below)? At what frequency is the plating exactly one skin depth thick?
>
> *Source: original.*

> [!hint]- Hint
> $\delta\sqrt f = 1/\sqrt{\pi\mu_0\sigma}$ is a constant of the metal. The power still travelling at depth $d$ is $e^{-2d/\delta}$ of what entered.

> [!solution]- Solution
> (a) Gold is a good conductor at all these frequencies ($\sigma/\omega\epsilon_0\approx7\times10^{7}$ even at 10 GHz), so
> $$
> \delta = \frac{1}{\sqrt{\pi f\mu_0\sigma}} = \frac{1}{\sqrt{161.9\,f}} = \frac{0.0786}{\sqrt f}\ \text{m}.
> $$
> At 60 Hz, $\delta = 0.0786/7.75 = 10.1$ mm; at 1 MHz, $\delta = 0.0786/1000 = 78.6$ µm.
>
> (b) $\delta\propto1/\sqrt f$. Four times the frequency halves $\delta$: 39.3 µm at 4 MHz. $10^{4}$ times the frequency divides it by 100: 0.786 µm at 10 GHz.
>
> (c) $1.5/0.786 = 1.91$ skin depths. The power still travelling at the back of the plating is $e^{-2\times1.91} = e^{-3.82} = 2.2$ % of what entered, so 97.8 % is absorbed within the gold. The field at the back is $e^{-1.91} = 15$ % of its surface value. The plating is one skin depth thick where $\sqrt f = 0.0786/(1.5\times10^{-6})$, at $f = 2.75$ GHz.
>
> **Watch out:** at the back of the plating the field is still 15 % of its surface value, but the power is down to 2.2 %. Power goes as the square of the field.
>
> **Answer.** (a) 10.1 mm at 60 Hz, 78.6 µm at 1 MHz. (b) 39.3 µm at 4 MHz, 0.786 µm at 10 GHz. (c) 1.91 skin depths; 97.8 % of the power is absorbed in the plating; one skin depth at 2.75 GHz.

### 23.5 Power against depth in seawater

> [!easy] Easy · attenuation · decibels · seawater
> A plane wave travels straight down into the sea. Let $\hat z$ point **up**, with the surface at $z = 0$ and water for $z<0$. In the water
> $$
> \tilde{\mathbf{E}} = \hat x\,0.5\,e^{0.4z}e^{j0.4z}\ \text{V/m}\qquad(z\text{ in m}).
> $$
> (a) Which way does the wave travel? How can you tell from $\tilde{\mathbf{E}}$ alone that the water is a good conductor at this frequency, and what is the phase of $\eta$?
>
> (b) Find the time-average Poynting vector $\langle\mathbf{S}\rangle(z)$, with the water's $\lvert\eta\rvert$ left as a symbol.
>
> (c) By what factor per metre, and by how many dB per metre, does the power density fall with depth?
>
> (d) At what depth is the power density 30 dB below its value just under the surface?
>
> (e) The water is seawater, $\sigma = 4$ S/m, $\epsilon_r = 81$, $\mu = \mu_0$. Find the frequency, $\lvert\eta\rvert$, and $\langle\mathbf{S}\rangle$ just under the surface.
>
> *Source: FA23 Exam 3 #6, re-parameterized: $\hat z$ up instead of down, a new amplitude and decay constant, and a numerical part (e).*

> [!hint]- Hint
> Restore $e^{j\omega t}$: $e^{j0.4z}$ becomes $\cos(\omega t + 0.4z)$. Equal $\alpha$ and $\beta$ is the signature of one regime. For the power use $\tilde{\mathbf{H}} = \hat u\times\tilde{\mathbf{E}}/\eta$ and $\langle\mathbf{S}\rangle = \tfrac12\text{Re}\{\tilde{\mathbf{E}}\times\tilde{\mathbf{H}}^*\}$.

> [!solution]- Solution
> (a) In the time domain the field is $\hat x\,0.5e^{0.4z}\cos(\omega t + 0.4z)$. A crest, $\omega t + 0.4z = 0$, sits at $z = -\omega t/0.4$, which moves toward $-z$ (down) as $t$ grows. The amplitude $e^{0.4z}$ shrinks downward too, as it must along the travel. A wave toward $-z$ is $e^{+\gamma z}$, so $\gamma = 0.4 + j0.4$: $\alpha = \beta = 0.4$ m⁻¹. Equal $\alpha$ and $\beta$ mark a good conductor: $\alpha<\beta$ in any other medium with real, positive $\sigma$, $\epsilon$, $\mu$, and the two become equal only in the good-conductor limit. So $\eta = \lvert\eta\rvert e^{j45^\circ}$.
>
> (b) With $\hat u = -\hat z$ and $(-\hat z)\times\hat x = -\hat y$, $\tilde{\mathbf{H}} = -\hat y\,(0.5/\eta)\,e^{0.4z}e^{j0.4z}$. Then
> $$
> \langle\mathbf{S}\rangle = \tfrac12\text{Re}\Big\{\hat x\times(-\hat y)\,\frac{0.25}{\eta^*}\Big\}e^{0.8z} = -\hat z\,\frac{0.25\cos45^\circ}{2\lvert\eta\rvert}\,e^{0.8z} = -\hat z\,\frac{0.0884}{\lvert\eta\rvert}\,e^{0.8z}\ \text{W/m}^2,
> $$
> pointing down, as the travel does.
>
> (c) Each metre down, $z$ drops by 1 and the power density is multiplied by $e^{-0.8} = 0.449$. The power attenuates at $2\alpha = 0.8$ per metre, which is $10\log_{10}e^{0.8} = 8.686\times0.4 = 3.47$ dB/m.
>
> (d) $30/3.47 = 8.63$ m down, at $z = -8.63$ m. (Equivalently $e^{-0.8d} = 10^{-3}$ gives $d = \ln1000/0.8$.) The field there is 30 dB down too, at 3.2 % of its surface value.
>
> (e) In a good conductor $\alpha = \sqrt{\pi f\mu\sigma}$, so
> $$
> f = \frac{\alpha^2}{\pi\mu_0\sigma} = \frac{0.16}{\pi\cdot4\pi\times10^{-7}\cdot4} = 10.1\ \text{kHz}.
> $$
> There $\sigma/\omega\epsilon = 8.8\times10^{4}$ with $\epsilon = 81\epsilon_0$, which confirms the regime. $\lvert\eta\rvert = \sqrt{\omega\mu_0/\sigma} = \sqrt2\,\alpha/\sigma = 0.141\ \Omega$, so just under the surface $\langle\mathbf{S}\rangle = -\hat z\,0.0884/0.141 = -\hat z\,0.625$ W/m².
>
> **Watch out:** depth is $-z$ here. The power factor is $e^{+0.8z} = e^{-0.8\lvert z\rvert}$; writing $e^{-0.8z}$ would make the power grow with depth.
>
> **Answer.** (a) Down ($-\hat z$); $\alpha = \beta = 0.4$ m⁻¹ marks a good conductor; $\angle\eta = 45^\circ$. (b) $\langle\mathbf{S}\rangle = -\hat z\,(0.0884/\lvert\eta\rvert)\,e^{0.8z}$ W/m². (c) A factor $e^{-0.8} = 0.449$ per metre, 3.47 dB/m. (d) 8.63 m down. (e) $f = 10.1$ kHz, $\lvert\eta\rvert = 0.141\ \Omega$, $\langle\mathbf{S}\rangle(0) = -\hat z\,0.625$ W/m².

## Medium

### 23.6 Wavelength and depth measured underground

> [!medium] Medium · regimes · good conductor · penetration depth
> An electromagnetic survey at $f = 1$ kHz measures, inside the ground, a wavelength $\lambda = 1.00$ km and a penetration depth $\delta = 159.2$ m. The ground is non-magnetic.
>
> (a) Is the ground an imperfect dielectric or a good conductor at 1 kHz? Why?
>
> (b) Find the phase velocity.
>
> (c) Find $\sigma$. Which handbook material has this conductivity?
>
> (d) Find $\eta$ (magnitude and phase).
>
> (e) Can you find $\epsilon_r$ from these measurements? What *can* you say about it?
>
> *Source: Summer 2017 HE3 #2b style, re-parameterized: a good conductor instead of an imperfect dielectric, a new frequency and new measurements, and part (e) added.*

> [!hint]- Hint
> $\alpha = 1/\delta$ and $\beta = 2\pi/\lambda$; their ratio is $\tan\tau$, which names the regime. Then look at the good-conductor row: which material constants appear in it, and which do not?

> [!solution]- Solution
> **Setup.** A measured $\lambda$ and $\delta$ give $\beta$ and $\alpha$ directly, and $\alpha/\beta = \tan\tau$ tells the regime (Lecture 23, recipe step 5).
>
> **(a)** $\alpha = 1/\delta = 1/159.2 = 6.28\times10^{-3}$ Np/m and $\beta = 2\pi/\lambda = 6.28\times10^{-3}$ rad/m. They are equal to within the precision of the data ($\alpha/\beta = 0.9997$), so $\lambda = 2\pi\delta$: a **good conductor**. $\tan\tau = 0.9997$ puts $\tau$ at 45° and $\sigma/\omega\epsilon = \tan2\tau$ in the thousands. An imperfect dielectric would instead have $\delta\gg\lambda$.
>
> **(b)** $v_p = \lambda f = 1000\times1000 = 10^{6}$ m/s, $c/300$. Without its conductivity, a soil with the handbook $\epsilon_r = 10$ of wet earth would carry the wave at $c/\sqrt{10} = 9.5\times10^{7}$ m/s; the conduction current slows it about a hundredfold.
>
> **(c)** In a good conductor $\alpha = \sqrt{\pi f\mu\sigma}$, so
> $$
> \sigma = \frac{1}{\pi f\mu_0\delta^2} = \frac{1}{\pi\cdot10^{3}\cdot4\pi\times10^{-7}\cdot159.2^2} = 9.99\times10^{-3}\approx1.0\times10^{-2}\ \text{S/m}.
> $$
> The exact route of Lecture 22, $\sigma = \text{Re}\{\gamma/\eta\} = 2\alpha\beta/\omega\mu$, gives the same value. $10^{-2}$ S/m is the handbook conductivity of moist soil (loam).
>
> **(d)** In a good conductor
> $$
> \eta = \sqrt{\frac{\omega\mu_0}{\sigma}}\,e^{j\pi/4} = \sqrt{\frac{2\pi\times10^{3}\cdot4\pi\times10^{-7}}{10^{-2}}}\,e^{j\pi/4} = 0.889\,e^{j45^\circ}\ \Omega = 0.628(1+j)\ \Omega,
> $$
> the same as $(1+j)/(\sigma\delta)$. So $\lvert\eta\rvert = 0.889\ \Omega$ and $\tau = 45^\circ$.
>
> **(e)** No. The good-conductor row contains $\sigma$, $\mu$ and $f$ but not $\epsilon$: the displacement current is too small to leave a mark. Formally $\epsilon = (\beta^2 - \alpha^2)/\omega^2\mu$ (Lecture 22), but here that is the difference of two almost equal numbers. With $\lambda = 1000$ m, $\delta = 159.15$ m gives $\epsilon_r = -5.6$, $\delta = 159.2$ m gives 51, and $\delta = 159.25$ m gives 107. A 0.06 % change in $\delta$ swings $\epsilon_r$ by more than 100, so the result is measurement noise. What the data do say is an upper bound. The good-conductor reading needs $\sigma/\omega\epsilon>10$, so $\epsilon<\sigma/10\omega = 1.6\times10^{-7}$ F/m, i.e. $\epsilon_r<1.8\times10^{4}$, which every soil satisfies.
>
> **Check:** with $\epsilon_r = 1$, 10 or 1000, the exact formulas give $\delta = 159.2$, 159.2 and 159.6 m, and $\lambda = 1000$, 1000 and 997 m. Only an absurd $\epsilon_r$ would show in the measurement. The handbook value for wet earth, $\epsilon_r = 10$, gives $\sigma/\omega\epsilon = 1.8\times10^{4}$, consistent with (a).
>
> **Watch out:** in the exam this problem is modelled on, $\delta\gg\lambda$ and the medium is a dielectric, so $\epsilon_r$ comes from $v_p$. Here the same step would give nonsense: $(c/v_p)^2 = 9\times10^{4}$.
>
> **Answer.** (a) Good conductor: $\alpha = \beta = 6.28\times10^{-3}$ m⁻¹, $\lambda = 2\pi\delta$. (b) $v_p = 10^{6}$ m/s. (c) $\sigma = 1.0\times10^{-2}$ S/m, moist soil. (d) $\eta = 0.628(1+j)\ \Omega$, $\lvert\eta\rvert = 0.889\ \Omega$, $\tau = 45^\circ$. (e) No; $\epsilon$ drops out in a good conductor. The data only bound it: $\epsilon_r<1.8\times10^{4}$.

### 23.7 Divers talking through a lake

> [!medium] Medium · imperfect dielectric · Joule heating · energy balance
> Two divers 10 m apart in a fresh-water lake ($\sigma = 10^{-3}$ S/m, $\epsilon_r = 80$, $\mu = \mu_0$) talk by 100 MHz radio. Model the signal as a plane wave travelling toward $+x$ with $\tilde{\mathbf{E}} = \hat z\,0.5$ V/m at $x = 0$. Use $\epsilon_0\approx10^{-9}/36\pi$ F/m and $\eta_0\approx120\pi\ \Omega$.
>
> (a) Classify the water at 100 MHz.
>
> (b) Use the imperfect-dielectric formulas to find $\lvert\eta\rvert$, $\tau$, $\alpha$, $\beta$, $\delta$, $\lambda$ and $v_p$. Write $\tilde{\mathbf{H}}(x)$.
>
> (c) Find $\langle\mathbf{S}\rangle(x)$. Show that $-d\langle S_x\rangle/dx$ equals the time-average Joule heating $\tfrac12\sigma\lvert\tilde{\mathbf{E}}\rvert^2$ at every $x$, and use this to explain the formula $\alpha\approx(\sigma/2)\sqrt{\mu/\epsilon}$.
>
> (d) What fraction of the power is turned into heat between the divers, and how much heat is that per square metre of wavefront?
>
> *Source: course notes Lecture 23, Example 1 style (imperfect dielectric, Joule heating), with a new medium, frequency and geometry.*

> [!hint]- Hint
> In an imperfect dielectric everything except $\alpha$ keeps its lossless value. For (c), Poynting's theorem averaged over a period has no stored-energy term, so $-d\langle S_x\rangle/dx = \langle\mathbf{J}\cdot\mathbf{E}\rangle$ with $\mathbf{J} = \sigma\mathbf{E}$.

> [!solution]- Solution
> **Setup.** Classify first. In an imperfect dielectric the only new feature is the decay, and its rate is set by energy conservation.
>
> **(a)** $\sigma/\omega\epsilon = 18\times10^{9}\times10^{-3}/(10^{8}\times80) = 2.25\times10^{-3}\ll0.1$: an **imperfect dielectric**.
>
> **(b)** With the lossless values for $\eta$ and $\beta$:
> $$
> \begin{aligned}
> \lvert\eta\rvert&\approx\frac{\eta_0}{\sqrt{80}} = \frac{120\pi}{8.944} = 42.1\ \Omega,\qquad \tau\approx\frac{\sigma}{2\omega\epsilon} = 1.125\times10^{-3}\ \text{rad} = 0.064^\circ,\\
> \alpha&\approx\frac\sigma2\lvert\eta\rvert = 0.5\times10^{-3}\times42.15 = 0.0211\ \text{Np/m},\qquad \delta = 47.5\ \text{m},\\
> \beta&\approx\frac{\omega\sqrt{80}}{c} = 18.7\ \text{rad/m},\qquad \lambda = 0.335\ \text{m},\qquad v_p = \frac{c}{\sqrt{80}} = 3.35\times10^{7}\ \text{m/s}.
> \end{aligned}
> $$
> For $\tilde{\mathbf{H}}$: $\hat u = \hat x$ and $\hat x\times\hat z = -\hat y$, so
> $$
> \tilde{\mathbf{H}} = -\hat y\,\frac{0.5}{\eta}\,e^{-\alpha x}e^{-j\beta x} = -\hat y\,11.9\,e^{-j0.064^\circ}e^{-\alpha x}e^{-j\beta x}\ \text{mA/m}.
> $$
> Check: $\hat z\times(-\hat y) = +\hat x$, along the travel ✓.
>
> **(c)** $\langle\mathbf{S}\rangle = \hat x\,\dfrac{\lvert E_0\rvert^2\cos\tau}{2\lvert\eta\rvert}\,e^{-2\alpha x} = \hat x\,2.97\,e^{-2\alpha x}$ mW/m². The heating is $\langle\mathbf{J}\cdot\mathbf{E}\rangle = \tfrac12\sigma\lvert E_0\rvert^2e^{-2\alpha x} = 0.125\,e^{-2\alpha x}$ mW/m³. Averaged over a cycle, the stored energy comes back each period, so Poynting's theorem says the flux shrinks exactly as fast as the medium heats:
> $$
> -\frac{d\langle S_x\rangle}{dx} = 2\alpha\,\frac{\lvert E_0\rvert^2\cos\tau}{2\lvert\eta\rvert}\,e^{-2\alpha x} = \tfrac12\sigma\lvert E_0\rvert^2e^{-2\alpha x}\quad\Longrightarrow\quad\alpha = \frac{\sigma\lvert\eta\rvert}{2\cos\tau}.
> $$
> This holds at every $x$ because both sides carry the same $e^{-2\alpha x}$. With $\cos\tau\approx1$ and $\lvert\eta\rvert\approx\sqrt{\mu/\epsilon}$ it is the imperfect-dielectric $\alpha\approx(\sigma/2)\sqrt{\mu/\epsilon}$: the attenuation is just the Joule heat. At $x = 0$: $2\alpha\langle S_x\rangle = 2\times0.0211\times2.97 = 0.125$ mW/m³ ✓.
>
> **(d)** The fraction turned into heat over 10 m is $1 - e^{-2\alpha\cdot10} = 1 - e^{-0.421} = 34.4$ % (a 1.83 dB loss). Per square metre of wavefront,
> $$
> \int_0^{10\ \text{m}}\tfrac12\sigma\lvert E_0\rvert^2e^{-2\alpha x}\,dx = 0.125\ \text{mW/m}^3\times\frac{1 - e^{-0.421}}{2\alpha} = 1.02\ \text{mW/m}^2,
> $$
> which is $0.344\times2.97$ mW/m², the drop in $\langle S_x\rangle$ ✓.
>
> **Check:** the exact $\gamma$ and $\eta$ of Lecture 22 for this water give the same $\alpha$, $\beta$ and $\lvert\eta\rvert$ to better than $10^{-5}$, as expected at $\sigma/\omega\epsilon = 0.00225$. For contrast, seawater at 100 MHz loses 326 dB per metre (exact formulas, since there $\sigma/\omega\epsilon = 8.9$): divers in the sea cannot use VHF radio at all.
>
> **Answer.** (a) Imperfect dielectric ($\sigma/\omega\epsilon = 2.25\times10^{-3}$). (b) $\lvert\eta\rvert = 42.1\ \Omega$, $\tau = 0.064^\circ$, $\alpha = 0.0211$ Np/m, $\beta = 18.7$ rad/m, $\delta = 47.5$ m, $\lambda = 0.335$ m, $v_p = 3.35\times10^{7}$ m/s; $\tilde{\mathbf{H}} = -\hat y\,11.9\,e^{-j0.064^\circ}e^{-\alpha x}e^{-j\beta x}$ mA/m. (c) $\langle\mathbf{S}\rangle = \hat x\,2.97\,e^{-2\alpha x}$ mW/m²; $-d\langle S_x\rangle/dx = \tfrac12\sigma\lvert\tilde{\mathbf{E}}\rvert^2$ gives $\alpha = \sigma\lvert\eta\rvert/(2\cos\tau)\approx(\sigma/2)\sqrt{\mu/\epsilon}$. (d) 34.4 % of the power, 1.02 mW/m².

### 23.8 The missing permittivity

> [!medium] Medium · find the error · loss tangent · regimes
> A tank holds distilled water: $\sigma = 2\times10^{-4}$ S/m, $\epsilon_r = 81$, $\mu = \mu_0$. A student finds the penetration depth, the wavelength and the intrinsic impedance for a 100 kHz plane wave in it:
>
> "$\sigma/\omega\epsilon = 2\times10^{-4}/(2\pi\times10^{5}\times8.854\times10^{-12}) = 36\gg1$, so the water is a good conductor. Then $\delta = 1/\sqrt{\pi f\mu_0\sigma} = 1/\sqrt{\pi\cdot10^{5}\cdot4\pi\times10^{-7}\cdot2\times10^{-4}} = 113$ m, $\lambda = 2\pi\delta = 707$ m, and $\eta = (1+j)/(\sigma\delta) = 44.4(1+j)\ \Omega$, so $\lvert\eta\rvert = 62.8\ \Omega$ and $\mathbf{H}$ lags $\mathbf{E}$ by 45°."
>
> Find the slip, decide the correct regime, and find the correct $\delta$, $\lambda$, $\lvert\eta\rvert$ and phase of $\eta$. By what factor was each of the student's numbers off?
>
> *Source: original.*

> [!hint]- Hint
> Check every number in the student's first line against the data for distilled water. Near $\sigma/\omega\epsilon\approx1$, the polar forms of Lecture 23 §2 are the quickest exact route: $\theta = \tan^{-1}p$, $\alpha,\beta = \omega\sqrt{\mu\epsilon}\,(1+p^2)^{1/4}\sin,\cos(\theta/2)$, $\lvert\eta\rvert = \sqrt{\mu/\epsilon}\,(1+p^2)^{-1/4}$, $\tau = \theta/2$.

> [!solution]- Solution
> **The slip:** $\epsilon_0$ in the loss tangent. The water's permittivity is $81\epsilon_0$, so
> $$
> \frac{\sigma}{\omega\epsilon} = \frac{36}{81} = 0.444 .
> $$
> That is **neither** regime (between 0.1 and 10), on the dielectric side. Every later step used the good-conductor row far outside its range.
>
> **Fix**, with the exact polar forms: $p = 0.444$, $\theta = \tan^{-1}p = 23.9^\circ$, $(1+p^2)^{1/4} = 1.046$, $\omega\sqrt{\mu\epsilon} = 2\pi\times10^{5}\times9/c = 0.01886$ rad/m and $\sqrt{\mu/\epsilon} = \eta_0/9 = 41.86\ \Omega$. Then
> $$
> \begin{aligned}
> \alpha &= 0.01886\times1.046\times\sin11.97^\circ = 4.09\times10^{-3}\ \text{Np/m},&\quad \delta &= 244\ \text{m},\\
> \beta &= 0.01886\times1.046\times\cos11.97^\circ = 0.0193\ \text{rad/m},&\quad \lambda &= 326\ \text{m},\\
> \lvert\eta\rvert &= 41.86/1.046 = 40.0\ \Omega,&\quad \tau &= \theta/2 = 12.0^\circ .
> \end{aligned}
> $$
> The student's $\delta$ was 2.17 times too short and $\lambda$ 2.17 times too long, $\lvert\eta\rvert$ 1.57 times too large, and the phase 45° instead of 12°.
>
> **Check:** $\alpha/\beta = 0.212 = \tan12.0^\circ$ ✓, and $\lvert\gamma\rvert\lvert\eta\rvert = 0.01973\times40.0 = 0.790 = \omega\mu_0$ ✓. The imperfect-dielectric row would give $\delta = 239$ m (2.3 % short), $\lambda = 333$ m (2.3 % long), $\lvert\eta\rvert = 41.9\ \Omega$ (4.6 % high) and $\tau = p/2 = 12.7^\circ$. At $p = 0.44$ those shortcuts are a few percent off; the good-conductor ones were off by a factor of two.
>
> **Watch out:** for water the factor $\epsilon_r\approx80$ is decisive. Leaving it out multiplies the loss tangent by 81, enough to jump from one side of the crossover to the other.
>
> **Answer.** The student used $\epsilon_0$ instead of $81\epsilon_0$: $\sigma/\omega\epsilon = 0.444$, not 36, so neither shortcut applies (the dielectric one is closer). Correct: $\delta = 244$ m, $\lambda = 326$ m, $\lvert\eta\rvert = 40.0\ \Omega$, $\angle\eta = 12.0^\circ$. The student's $\delta$ was 2.17 times too small, $\lambda$ 2.17 times too large, $\lvert\eta\rvert$ 1.57 times too large.

## Hard

### 23.9 Down into a deep lake

> [!hard] Hard · good conductor · skin depth · decibels
> A 2.5 kHz plane wave travels straight down into a deep fresh-water lake: $\sigma = 10^{-3}$ S/m, $\epsilon_r = 80$, $\mu = \mu_0$. Let $\hat z$ point **down**, with the surface at $z = 0$ and water for $z>0$. Just below the surface the magnetic field phasor is $\tilde{\mathbf{H}}(0) = \hat x\,20$ mA/m. Use $\epsilon_0\approx10^{-9}/36\pi$ F/m and $\mu_0 = 4\pi\times10^{-7}$ H/m; parts (a)–(c) need no calculator.
>
> (a) Is the water an imperfect dielectric or a good conductor at 2.5 kHz? Why?
>
> (b) Find $\alpha$, $\beta$, the skin depth $\delta$, the wavelength $\lambda$ and the phase velocity $v_p$. Compare $v_p$ with the speed in a lossless medium with $\epsilon_r = 80$.
>
> (c) Find $\eta$, then the phasors $\tilde{\mathbf{H}}(z)$ and $\tilde{\mathbf{E}}(z)$ and the real fields $\mathbf{H}(z,t)$ and $\mathbf{E}(z,t)$. Which field leads, and by how much time?
>
> (d) Find $\langle\mathbf{S}\rangle$ just below the surface and 500 m down. What is the loss in dB per metre, and at what depth is the power 1 % of its surface value?
>
> (e) At what depth does $\mathbf{E}$ point opposite to the surface field at the same instant, and what fraction of the power is left there?
>
> *Source: Summer 2018 HE3 #3b (repeated as Summer 2019 HE3 #3b), re-parameterized: fresh water at 2.5 kHz instead of seawater at 1 kHz, travel along $+z$ with $\hat z$ pointing down, the surface $\mathbf{H}$ given instead of a power density, and part (e) added; also different from the site's worked problem [[problems/a-radio-wave-into-moist-ground|A radio wave into moist ground]].*

> [!hint]- Hint
> Classify with $80\epsilon_0$. In the good-conductor row, $\pi f\mu_0\sigma = 4\pi^2\times10^{-7}f\sigma$ is a perfect square here. From $\mathbf{H}$, the electric field is $\tilde{\mathbf{E}} = \eta\,\tilde{\mathbf{H}}\times\hat u$ (multiply by $\lvert\eta\rvert$, *add* $\tau$), and the power is $\langle\mathbf{S}\rangle = \hat u\,\tfrac12\text{Re}\{\eta\}\lvert\tilde{\mathbf{H}}\rvert^2$.

> [!solution]- Solution
> **Setup.** The wave travels along $\hat u = +\hat z$ and decays that way, so every phasor carries $e^{-\gamma z}$, and the distance travelled is $z$ itself.
>
> **(a)** $\dfrac{\sigma}{\omega\epsilon} = \dfrac{18\times10^{9}\times10^{-3}}{2.5\times10^{3}\times80} = 90\gg10$: a **good conductor**. The conduction current is 90 times the displacement current. With $\epsilon_0$ instead of $80\epsilon_0$ it would be 7200, the same verdict here, but only by luck.
>
> **(b)** $\pi f\mu_0\sigma = 4\pi^2\times10^{-7}\times2.5\times10^{3}\times10^{-3} = \pi^2\times10^{-6}$, so
> $$
> \alpha = \beta = \pi\times10^{-3}\ \text{m}^{-1},\qquad \delta = \frac{1000}{\pi} = 318\ \text{m},\qquad \lambda = 2\pi\delta = 2000\ \text{m},
> $$
> $$
> v_p = \lambda f = \omega\delta = 5\times10^{6}\ \text{m/s} = \frac{c}{60}.
> $$
> A lossless medium with $\epsilon_r = 80$ would carry the wave at $c/\sqrt{80} = 3.35\times10^{7}$ m/s, 6.7 times faster. In a good conductor the wave is slow, and its speed grows as $\sqrt f$.
>
> **(c)** $\sigma\delta = 10^{-3}\times1000/\pi = 1/\pi$ S, so
> $$
> \eta = \frac{1+j}{\sigma\delta} = \pi(1+j) = 4.44\,e^{j\pi/4}\ \Omega .
> $$
> Then $\tilde{\mathbf{H}}(z) = \hat x\,20\,e^{-z/\delta}e^{-jz/\delta}$ mA/m and, with $\hat x\times\hat z = -\hat y$,
> $$
> \tilde{\mathbf{E}}(z) = \eta\,\tilde{\mathbf{H}}\times\hat z = -\hat y\,0.02\pi(1+j)\,e^{-z/\delta}e^{-jz/\delta} = -\hat y\,88.9\,e^{j\pi/4}e^{-z/\delta}e^{-jz/\delta}\ \text{mV/m}.
> $$
> With $\omega = 5000\pi$ rad/s and $1/\delta = \pi\times10^{-3}$ m⁻¹:
> $$
> \begin{aligned}
> \mathbf{H}(z,t) &= \hat x\,20\,e^{-z/\delta}\cos\Big(\omega t - \frac z\delta\Big)\ \text{mA/m},\\
> \mathbf{E}(z,t) &= -\hat y\,88.9\,e^{-z/\delta}\cos\Big(\omega t - \frac z\delta + \frac\pi4\Big)\ \text{mV/m}.
> \end{aligned}
> $$
> $\mathbf{E}$ leads $\mathbf{H}$ by 45°, i.e. by $T/8 = 50$ µs (the period is 400 µs). Equivalently $\mathbf{H}$ lags. Direction: $\mathbf{E}\times\mathbf{H}\propto(-\hat y)\times\hat x = +\hat z$, down ✓.
>
> **(d)** At the surface
> $$
> \langle\mathbf{S}\rangle(0) = \hat z\,\tfrac12\text{Re}\{\eta\}\lvert H_0\rvert^2 = \hat z\,\tfrac12\pi(0.02)^2 = \hat z\,2\pi\times10^{-4}\ \text{W/m}^2 = \hat z\,0.628\ \text{mW/m}^2 .
> $$
> (The same from $\mathbf{E}$: $\lvert E_0\rvert^2\cos45^\circ/(2\lvert\eta\rvert) = (0.02\sqrt2\,\pi)^2(1/\sqrt2)/(2\sqrt2\,\pi) = 2\pi\times10^{-4}$ W/m².) 500 m down, the factor is $e^{-2\alpha z} = e^{-2\pi\times10^{-3}\times500} = e^{-\pi} = 0.0432$, so $\langle\mathbf{S}\rangle = \hat z\,27.2$ µW/m². The loss is $8.686\,\alpha = 0.0273$ dB/m (27.3 dB per km), and 13.6 dB over the 500 m. The power is 1 % of its surface value where $e^{-2\alpha z} = 0.01$, at $z = \ln100/(2\pi\times10^{-3}) = 733$ m.
>
> **(e)** The phase $z/\delta$ lags by $\pi$ at $z = \pi\delta = \lambda/2 = 1000$ m: there, at every instant, $\mathbf{E}$ points opposite to the surface field. The field is down to $e^{-\pi} = 4.3$ % and the power to $e^{-2\pi} = 0.19$ %, 27.3 dB below the surface value. Half a wavelength already costs that much. A good conductor never lets a wave travel "several wavelengths".
>
> **Check:** the exact $\gamma$ and $\eta$ of Lecture 22 (with $\sigma/\omega\epsilon = 90$) give $\delta = 320$ m and $\lambda = 1989$ m, within 0.6 % of the shortcuts, and $\tau = 44.7^\circ$ instead of $45^\circ$; the 1 % depth becomes 737 m. The shortcut phasors satisfy Faraday's law exactly ($\gamma\eta = j\omega\mu$) but the Ampère–Maxwell law only to 1.1 %, the share of the displacement current that the good-conductor row drops ($\omega\epsilon/\lvert\sigma + j\omega\epsilon\rvert\approx1/90$; checked numerically).
>
> **Watch out:** the power factor is $e^{-2\alpha z}$, not $e^{-\alpha z}$. The latter gives the field, which at 500 m is still 21 %.
>
> **Answer.** (a) Good conductor, $\sigma/\omega\epsilon = 90$. (b) $\alpha = \beta = \pi\times10^{-3}$ m⁻¹, $\delta = 1000/\pi = 318$ m, $\lambda = 2$ km, $v_p = 5\times10^{6}$ m/s (6.7 times slower than $c/\sqrt{80}$). (c) $\eta = \pi(1+j) = 4.44\,e^{j\pi/4}\ \Omega$; $\mathbf{H} = \hat x\,20e^{-z/\delta}\cos(\omega t - z/\delta)$ mA/m, $\mathbf{E} = -\hat y\,88.9e^{-z/\delta}\cos(\omega t - z/\delta + \pi/4)$ mV/m; $\mathbf{E}$ leads by 50 µs. (d) 0.628 mW/m² down at the surface, 27.2 µW/m² at 500 m; 0.0273 dB/m; 1 % at 733 m. (e) At 1000 m, where 0.19 % of the power is left.

### 23.10 Calling a submarine

> [!hard] Hard · seawater · skin depth · decibels
> Seawater: $\sigma = 4$ S/m, $\epsilon_r = 81$, $\mu = \mu_0$. A shore station transmits at 25 kHz (the VLF band). A submarine's receiver still works if the time-average power density at its antenna is 80 dB below the value just under the sea surface. Ignore the air above and the reflection at the surface. Use $\epsilon_0\approx10^{-9}/36\pi$ F/m.
>
> (a) Check that seawater is a good conductor at 25 kHz. Find $\alpha$, $\delta$, $\lambda$ in the water and the loss in dB per metre, without a calculator except for the last number.
>
> (b) How deep can the antenna be?
>
> (c) The navy wants to reach ten times deeper on the same budget. What frequency is needed? Check the regime there. How deep is that, in wavelengths in the water, at either frequency?
>
> (d) The price. Assume the usable bandwidth is about 1 % of the carrier. Compare the bandwidths and the free-space wavelengths $\lambda_0 = c/f$ at the two frequencies. Why can't the submarine answer on the same frequency?
>
> (e) A buoy towed 2 m below the surface carries a second antenna. What is the highest frequency it can use with the same 80 dB budget? Is the good-conductor formula still accurate there?
>
> *Source: course notes Lecture 23, Example 2 and the remark on bandwidth, turned into a design problem; original.*

> [!hint]- Hint
> In a good conductor the loss is $8.686\sqrt{\pi f\mu\sigma}$ dB per metre, so on a fixed dB budget the depth reached scales as $1/\sqrt f$. 80 dB is a factor $10^{8}$ in power, and a good conductor charges the same 54.6 dB for every wavelength travelled.

> [!solution]- Solution
> **Setup.** Classify, then use the good-conductor row: the loss per metre is $8.686\,\alpha$ with $\alpha = \sqrt{\pi f\mu_0\sigma}$, and the depth reached is the budget divided by that.
>
> **(a)** $\sigma/\omega\epsilon = 18\times10^{9}\times4/(2.5\times10^{4}\times81) = 3.6\times10^{4}\gg10$: a good conductor. Then $\pi f\mu_0\sigma = 4\pi^2\times10^{-7}\times2.5\times10^{4}\times4 = 4\pi^2\times10^{-2}$, so
> $$
> \alpha = 0.2\pi = 0.628\ \text{Np/m},\qquad \delta = \frac5\pi = 1.59\ \text{m},\qquad \lambda = 2\pi\delta = 10\ \text{m},
> $$
> and the loss is $8.686\times0.628 = 5.46$ dB/m.
>
> **(b)** $80/5.46 = 14.7$ m. (Equivalently $e^{-2\alpha d} = 10^{-8}$ gives $d = \ln10^{8}/(2\alpha) = 14.7$ m.)
>
> **(c)** Depth on a fixed budget goes as $1/\alpha\propto1/\sqrt f$, so ten times deeper needs $1/100$ of the frequency: **250 Hz**. There $\sigma/\omega\epsilon = 3.6\times10^{6}$, still a good conductor, with $\alpha = 0.02\pi = 0.0628$ Np/m, $\delta = 15.9$ m, $\lambda = 100$ m and 0.546 dB/m, so the antenna can be 147 m down. In wavelengths nothing changed: a good conductor costs $20\log_{10}e^{2\pi} = 54.6$ dB per wavelength at any frequency, so 80 dB buys $80/54.6 = 1.47$ wavelengths: 14.7 m at 25 kHz ($\lambda = 10$ m) and 147 m at 250 Hz ($\lambda = 100$ m).
>
> **(d)** With about 1 % of the carrier usable, the bandwidth is roughly 250 Hz at 25 kHz but only 2.5 Hz at 250 Hz: a hundred times slower signalling, about the rates of real VLF links (hundreds of bits per second) and ELF links (a few characters per minute). The free-space wavelength grows from $\lambda_0 = 12$ km to 1200 km. A quarter-wave antenna would be 3 km and 300 km tall, so real stations use electrically short antennas kilometres long, driven with huge power. A submarine cannot carry anything like that, so it receives but cannot answer on these frequencies.
>
> **(e)** Over 2 m the budget allows $\alpha\le80/(8.686\times2) = 4.61$ Np/m, so
> $$
> f_{\max} = \frac{\alpha^2}{\pi\mu_0\sigma} = \frac{4.61^2}{\pi\cdot4\pi\times10^{-7}\cdot4} = 1.34\ \text{MHz}.
> $$
> There $\sigma/\omega\epsilon\approx660$, so the good-conductor formula is still excellent: the exact $\gamma$ gives a loss of 79.94 dB over the 2 m instead of 80 dB.
>
> **Check:** at 25 kHz and 250 Hz the exact $\gamma$ agrees with the good-conductor $\alpha$, $\delta$ and $\lambda$ to within 0.002 % ($\sigma/\omega\epsilon\ge3.6\times10^{4}$). The same budget at the real ELF frequency of 76 Hz reaches 266 m, and at 24 kHz 15.0 m.
>
> **Watch out:** the budget is in dB of **power**, and $10\log_{10}e^{2\alpha d} = 8.686\,\alpha d$. Using $e^{-\alpha d}$ for the power would make every depth twice too large.
>
> **Answer.** (a) $\sigma/\omega\epsilon = 3.6\times10^{4}$; $\alpha = 0.628$ Np/m, $\delta = 1.59$ m, $\lambda = 10$ m, 5.46 dB/m. (b) 14.7 m. (c) 250 Hz ($\sigma/\omega\epsilon = 3.6\times10^{6}$), reaching 147 m; 1.47 wavelengths in the water at either frequency. (d) Bandwidth about 250 Hz against 2.5 Hz; $\lambda_0 = 12$ km against 1200 km; no submarine can carry a transmitting antenna of that scale, so the link is one-way. (e) 1.34 MHz; $\sigma/\omega\epsilon\approx660$, so the formula is accurate to 0.1 %.

### 23.11 Dry earth from ELF to VHF

> [!hard] Hard · regimes · imperfect dielectric · good conductor
> Dry earth: $\sigma = 10^{-5}$ S/m, $\epsilon_r = 5$, $\mu = \mu_0$ (Rao's handbook values). Use $\epsilon_0\approx10^{-9}/36\pi$ F/m and $\eta_0\approx120\pi\ \Omega$.
>
> (a) Find the crossover frequency. For which angular frequencies $\omega$ is dry earth a good conductor ($\sigma/\omega\epsilon>10$), and for which an imperfect dielectric ($\sigma/\omega\epsilon<0.1$)?
>
> (b) POSSIBLE or NOT POSSIBLE? Explain each. (i) At 1 kHz a wave in dry earth has $\alpha$ much larger than $\beta$. (ii) At 50 Hz the wave dies out within about one wavelength. (iii) A 10 MHz wave keeps more than 10 % of its power after travelling 1 km.
>
> (c) At 100 Hz, find $\delta$ and $\lambda$ without a calculator.
>
> (d) At 10 MHz, find $\lvert\eta\rvert$, $\alpha$, $\delta$, $\lambda$ and the loss in dB/km. Which of these change at 100 MHz?
>
> (e) At the crossover frequency, find $\alpha$, $\beta$, $\lvert\eta\rvert$, $\tau$, $\delta$ and $\lambda$ from the exact formulas, and compare $\alpha$ with both shortcuts.
>
> *Source: Summer 2020 HE3 #3 and Summer 2019 HE3 (conflict) #3b style, re-parameterized: Rao's dry-earth values ($\sigma = 10^{-5}$ S/m, $\epsilon_r = 5$) instead of the exam's $\sigma = 10^{-3}$ S/m with $\epsilon_0$, new statements, and an exact part at the crossover.*

> [!hint]- Hint
> $f_c = 18\times10^{9}\sigma/\epsilon_r$ splits the frequency axis: a decade below it the good-conductor row holds, a decade above it the imperfect-dielectric row. At $f_c$ itself $\sigma/\omega\epsilon = 1$, so the loss angle is $45^\circ$ and $\tau = 22.5^\circ$; use $\alpha,\beta = \omega\sqrt{\mu\epsilon}\,2^{1/4}\sin,\cos22.5^\circ$.

> [!solution]- Solution
> **Setup.** One medium, three regimes. The ratio $\sigma/\omega\epsilon$ decides which formulas apply at each frequency.
>
> **(a)** $f_c = 18\times10^{9}\times10^{-5}/5 = 36$ kHz, and $\sigma/\epsilon = 7.2\pi\times10^{4}$ s⁻¹ $= 2.26\times10^{5}$ s⁻¹. Good conductor for $\omega<\sigma/10\epsilon = 7.2\pi\times10^{3}\approx2.26\times10^{4}$ rad/s ($f<3.6$ kHz). Imperfect dielectric for $\omega>10\sigma/\epsilon = 7.2\pi\times10^{5}\approx2.26\times10^{6}$ rad/s ($f>360$ kHz).
>
> **(b)** (i) **Not possible.** $\alpha/\beta = \tan\tau\le1$ for any real, positive $\sigma$, $\epsilon$ and $\mu$; $\alpha$ can approach $\beta$ but never exceed it. At 1 kHz ($\sigma/\omega\epsilon = 36$) the exact ratio is $\alpha/\beta = 0.973$.
> (ii) **Possible.** At 50 Hz, $\sigma/\omega\epsilon = 720$: a good conductor, so $\lambda = 2\pi\delta$ and the field falls by $e^{-2\pi}$ (to 0.19 %) in one wavelength, which here is 141 km.
> (iii) **Possible.** At 10 MHz (an imperfect dielectric, see (d)) $\alpha = 8.43\times10^{-4}$ Np/m, so after 1 km the power factor is $e^{-2\times0.843} = 0.185$: 18.5 % is left.
>
> **(c)** At 100 Hz, $\sigma/\omega\epsilon = 360$: a good conductor. $\pi f\mu_0\sigma = 4\pi^2\times10^{-7}\times100\times10^{-5} = 4\pi^2\times10^{-10}$, so $\alpha = \beta = 2\pi\times10^{-5}$ m⁻¹ and
> $$
> \delta = \frac{10^{5}}{2\pi} = 15.9\ \text{km},\qquad \lambda = 2\pi\delta = 100\ \text{km}.
> $$
>
> **(d)** At 10 MHz, $\sigma/\omega\epsilon = 3.6\times10^{-3}$: an imperfect dielectric. Then $\lvert\eta\rvert\approx120\pi/\sqrt5 = 168.6\ \Omega$ and
> $$
> \alpha\approx\frac\sigma2\lvert\eta\rvert = 5\times10^{-6}\times168.6 = 8.43\times10^{-4}\ \text{Np/m},\qquad \delta = 1186\ \text{m},\qquad \lambda = \frac{c}{f\sqrt5} = 13.4\ \text{m},
> $$
> a loss of $8.686\times0.843 = 7.32$ dB/km. At 100 MHz only $\lambda$ changes, to 1.34 m: $\alpha$, $\delta$, $\lvert\eta\rvert$ and the dB/km stay put, because the imperfect-dielectric $\alpha$ does not depend on frequency.
>
> **(e)** At 36 kHz, $\sigma/\omega\epsilon = 1$: the loss angle is $\theta = 45^\circ$, $\tau = 22.5^\circ$ and $(1+p^2)^{1/4} = 2^{1/4} = 1.189$. With $\omega\sqrt{\mu\epsilon} = 2\pi\times36\times10^{3}\sqrt5/c = 1.686\times10^{-3}$ rad/m:
> $$
> \begin{aligned}
> \alpha &= 1.686\times10^{-3}\times1.189\times\sin22.5^\circ = 7.67\times10^{-4}\ \text{Np/m},&\quad \delta &= 1303\ \text{m},\\
> \beta &= 1.686\times10^{-3}\times1.189\times\cos22.5^\circ = 1.852\times10^{-3}\ \text{rad/m},&\quad \lambda &= 3392\ \text{m},\\
> \lvert\eta\rvert &= 168.6/1.189 = 141.8\ \Omega,&\quad \tau &= 22.5^\circ .
> \end{aligned}
> $$
> The imperfect-dielectric $\alpha$ (the plateau $8.43\times10^{-4}$) is 9.9 % too high, and the good-conductor $\alpha = \sqrt{\pi f\mu_0\sigma} = 1.192\times10^{-3}$ is 55 % too high. For $\beta$ the two shortcuts are 9.0 % and 36 % too low. Near the crossover only the exact formulas will do.
>
> **Check:** the three regimes join smoothly. The penetration depth falls monotonically with frequency, from 15.9 km at 100 Hz through 1303 m at 36 kHz to the plateau of 1186 m above 360 kHz. At 100 Hz the exact formulas give $\delta = 15.94$ km and $\lambda = 99.9$ km, within 0.14 % of (c).
>
> **Watch out:** the dielectric plateau means that raising the frequency of a radar above about 360 kHz no longer costs extra loss per metre in this earth. In a good conductor, though, every factor of 100 in frequency costs a factor of 10 in dB per metre.
>
> **Answer.** (a) $f_c = 36$ kHz; good conductor for $\omega<2.26\times10^{4}$ rad/s ($f<3.6$ kHz), imperfect dielectric for $\omega>2.26\times10^{6}$ rad/s ($f>360$ kHz). (b) (i) Not possible ($\alpha\le\beta$ always). (ii) Possible ($\sigma/\omega\epsilon = 720$). (iii) Possible (18.5 % left). (c) $\delta = 15.9$ km, $\lambda = 100$ km. (d) $\lvert\eta\rvert = 168.6\ \Omega$, $\alpha = 8.43\times10^{-4}$ Np/m, $\delta = 1186$ m, $\lambda = 13.4$ m, 7.32 dB/km; at 100 MHz only $\lambda$ changes (1.34 m). (e) $\alpha = 7.67\times10^{-4}$ Np/m, $\beta = 1.852\times10^{-3}$ rad/m, $\lvert\eta\rvert = 141.8\ \Omega$, $\tau = 22.5^\circ$, $\delta = 1303$ m, $\lambda = 3392$ m; the shortcuts overestimate $\alpha$ by 9.9 % (dielectric) and 55 % (conductor).

### 23.12 Skin effect in a copper wire

> [!hard] Hard · skin depth · Joule heating · resistance
> A long straight copper wire ($\sigma = 5.8\times10^{7}$ S/m, $\mu = \mu_0$) of radius $a = 0.5$ mm lies along the $z$ axis and carries $I(t) = I_0\cos\omega t$ with $I_0 = 2$ A along $+\hat z$, at $f = 10$ MHz.
>
> (a) Find the skin depth and compare it with $a$. Why may the wire's surface be treated as a flat good conductor, with a plane wave entering it radially?
>
> (b) Just outside the wire, $\mathbf{H} = (I/2\pi a)\,\hat\phi$ by Ampère's law, and tangential $\mathbf{H}$ is continuous at the surface. Taking the wave inside to travel toward $-\hat r$, find $\eta$ and the electric field phasor $\tilde{\mathbf{E}}$ just inside the surface: its direction, magnitude and phase relative to the current.
>
> (c) Find the time-average power per unit area entering the wire and the power per unit length. Write the latter as $\tfrac12I_0^2R'_{\text{ac}}$ and find $R'_{\text{ac}}$. Show that $R'_{\text{ac}}/R'_{\text{dc}} = a/2\delta$, with $R'_{\text{dc}} = 1/(\sigma\pi a^2)$.
>
> (d) Check (c) by integrating the Joule heating $\tfrac12\sigma\lvert\tilde{\mathbf{E}}\rvert^2$ over the depth. What fraction of the heat is generated within one skin depth of the surface?
>
> (e) Repeat (a) at 60 Hz. What does the flat-surface model predict there, and what is the actual resistance per unit length?
>
> *Source: original (the skin-effect remark of Lecture 23 §6, with Ampère's law from Lecture 12 and $R = l/\sigma A$ from Lecture 8).*

> [!hint]- Hint
> Seen from inside, a skin a few tens of micrometres thick on a half-millimetre wire is flat. The wave entering the surface carries $\tfrac12\text{Re}\{\eta\}\lvert H_0\rvert^2$ per square metre, all of which turns into heat, and that power times the circumference $2\pi a$ is the heat per metre of wire.

> [!solution]- Solution
> **Setup.** Copper is a good conductor at 10 MHz ($\sigma/\omega\epsilon_0 = 1.0\times10^{11}$). Locally the surface is a flat good conductor with a plane wave entering it. Ampère's law supplies the surface $\mathbf{H}$, and energy conservation turns the absorbed power into a resistance.
>
> **(a)** $\delta = 1/\sqrt{\pi f\mu_0\sigma} = 0.0661/\sqrt{10^{7}}$ m $= 20.9$ µm, so $a/\delta = 23.9$. The field dies within a few skin depths, about 0.1 mm, in a layer much thinner than the radius. Over that layer the curvature of the surface hardly matters, so locally it is a plane wave entering a flat conductor.
>
> **(b)** $H_0 = I_0/(2\pi a) = 2/(2\pi\times0.5\times10^{-3}) = 637$ A/m, along $\hat\phi$, in phase with $I$. Since $\sigma\delta = 5.8\times10^{7}\times20.9\times10^{-6} = 1212$ S,
> $$
> \eta = \frac{1+j}{\sigma\delta} = (1+j)\,0.825\ \text{m}\Omega,\qquad \lvert\eta\rvert = 1.17\ \text{m}\Omega .
> $$
> With $\hat u = -\hat r$, $\tilde{\mathbf{E}} = \eta\,\tilde{\mathbf{H}}\times\hat u$ and $\hat\phi\times(-\hat r) = +\hat z$:
> $$
> \tilde{\mathbf{E}}(a) = \hat z\,\eta H_0 = \hat z\,0.743\,e^{j45^\circ}\ \text{V/m}.
> $$
> $\mathbf{E}$ points along the current, as it must to drive it, and leads the current by 45°. Check: $\mathbf{E}\times\mathbf{H}\propto\hat z\times\hat\phi = -\hat r$, into the wire ✓. The energy enters the wire from the space around it, as for the resistive wire of Lecture 20.
>
> **(c)** Per unit area of surface,
> $$
> \langle S\rangle_{\text{in}} = \tfrac12\text{Re}\{\eta\}H_0^2 = \tfrac12\times0.825\times10^{-3}\times637^2 = 167\ \text{W/m}^2,
> $$
> and per metre of wire $P' = 167\times2\pi a = 0.525$ W/m. Setting $P' = \tfrac12I_0^2R'_{\text{ac}}$, with $H_0 = I_0/2\pi a$ and $\text{Re}\{\eta\} = 1/\sigma\delta$:
> $$
> R'_{\text{ac}} = \frac{2P'}{I_0^2} = \frac{1}{2\pi a\,\sigma\delta} = 0.263\ \Omega/\text{m},\qquad \frac{R'_{\text{ac}}}{R'_{\text{dc}}} = \frac{\sigma\pi a^2}{2\pi a\,\sigma\delta} = \frac{a}{2\delta} = 12.0 .
> $$
> $R'_{\text{dc}} = 1/(\sigma\pi a^2) = 22.0$ mΩ/m. $R'_{\text{ac}}$ is the DC resistance of a copper tube of circumference $2\pi a$ and wall $\delta$: the current flows only in the skin.
>
> **(d)** At depth $s$ below the surface, $\lvert\tilde{\mathbf{E}}\rvert = 0.743\,e^{-s/\delta}$ V/m. So
> $$
> \int_0^{\infty}\tfrac12\sigma\lvert\tilde{\mathbf{E}}\rvert^2\,ds = \tfrac12\sigma(0.743)^2\,\frac\delta2 = 1.60\times10^{7}\ \text{W/m}^3\times10.4\ \mu\text{m} = 167\ \text{W/m}^2,
> $$
> the power that entered the surface ✓. Algebraically, $\tfrac12\sigma\lvert\eta\rvert^2H_0^2\,\delta/2 = H_0^2/2\sigma\delta = \tfrac12\text{Re}\{\eta\}H_0^2$. The heat generated within $\delta$ of the surface is $1 - e^{-2} = 86.5$ % of the total.
>
> **(e)** At 60 Hz, $\delta = 0.0661/\sqrt{60} = 8.53$ mm, seventeen times the radius. There is no thin skin, and the flat-surface model fails. Its formula would claim $R'_{\text{ac}}/R'_{\text{dc}} = a/2\delta = 0.029$, a resistance *below* the DC value, which is impossible. The current fills the whole cross-section almost uniformly, and $R'\approx R'_{\text{dc}} = 22.0$ mΩ/m.
>
> **Check:** the exact solution for a round wire (Bessel functions, beyond this course) gives $R' = 0.268\ \Omega/\text{m}$ at 10 MHz, 2.1 % above the flat-surface value: the known correction $R'/R'_{\text{dc}}\approx a/2\delta + \tfrac14$. At 60 Hz it gives $R'_{\text{dc}}$ to better than one part in a million. The reactive half of $\eta$ is the wire's internal inductance: $L' = R'_{\text{ac}}/\omega = 4.2$ nH/m, down from the DC value $\mu_0/8\pi = 50$ nH/m of [[practice/15-inductance-and-magnetic-energy#157-internal-inductance-of-a-wire|Problem 15.7]], because the magnetic field now reaches only about a skin depth into the copper.
>
> **Watch out:** the skin effect is not a loss of conductivity. The copper is unchanged; the induced eddy currents (Lenz) push the current into a thinner layer, and that layer has a higher resistance.
>
> **Answer.** (a) $\delta = 20.9$ µm $\ll a = 0.5$ mm ($a/\delta = 23.9$). (b) $\eta = (1+j)\,0.825$ mΩ; $\tilde{\mathbf{E}}(a) = \hat z\,0.743\,e^{j45^\circ}$ V/m, along the current and leading it by 45°. (c) 167 W/m² into the surface, 0.525 W/m; $R'_{\text{ac}} = 1/(2\pi a\sigma\delta) = 0.263\ \Omega$/m, which is $a/2\delta = 12.0$ times $R'_{\text{dc}} = 22.0$ mΩ/m. (d) The integral gives the same 167 W/m²; 86.5 % of the heat is within $\delta$. (e) $\delta = 8.53$ mm $\gg a$: no skin effect, $R'\approx R'_{\text{dc}} = 22.0$ mΩ/m.

### Sources for this page
Course notes, Lecture 23: Example 1 (an imperfect dielectric whose lost power heats the medium) for 23.7, with fresh water at 100 MHz, a new geometry and the energy balance worked out; Example 2 and the remark on bandwidth for the submarine design of 23.10. Rao, *Fundamentals of Electromagnetics for ECE*, Tables 5.1–5.3: the conductivities and permittivities of copper, gold, seawater, fresh and distilled water, dry and wet earth and Bakelite, and the style of 23.1. ITU-R P.527 (via the Lecture 23 page) for moist soil (loam), $10^{-2}$ S/m. Old exams, all re-parameterized: SP17 Exam 3 #2(i) and SP18 Exam 3 #1(i) (good-conductor multiple choice; 23.2, new statements); FA23 Exam 3 #6 (power against depth in water; 23.5, with $\hat z$ up and a numerical part); Summer 2017 HE3 #2b (classify from a measured $\lambda$ and $\delta$; 23.6, now a good conductor, with the $\epsilon_r$ question); Summer 2018 and 2019 HE3 #3b (classify, then $\delta$, $\lambda$, $v_p$ and power at depth; 23.9, fresh water at 2.5 kHz, travel along $+\hat z$ downward, surface $\mathbf{H}$ given, different from the site's worked problem); Summer 2020 HE3 #3 and Summer 2019 HE3 (conflict) #3b ("possible or not possible" and the frequency inequality; 23.11, with Rao's dry-earth values and an exact part at the crossover). Original: 23.3, 23.4, 23.8 and 23.12. The data rates and antennas of real VLF and ELF links in 23.10 are those quoted on the Lecture 23 page, from the Wikipedia article "Communication with submarines".

*Previous: [[practice/22-damped-waves-in-conducting-media|Lecture 22 practice]] · [[practice/index|all practice]]*
