---
title: "Propagation constant"
description: "γ = α + jβ = √(jωμ(σ + jωε)) is the complex number in the e^(∓γz) that a plane wave of one frequency carries. Its real part α (Np/m) makes the wave decay, by 1/e over the penetration depth δ = 1/α; its imaginary part β (rad/m) sets the wavelength 2π/β and the phase velocity ω/β. In a lossless medium γ = jω√(με) is purely imaginary, and β ≥ α in every medium with a real conductivity."
tags: [concept, waves]
aliases: ["gamma = alpha + j beta", "attenuation constant", "complex propagation constant"]
---

> [!key] Definition
> $$
> \begin{gathered}
> \gamma = \sqrt{j\omega\mu(\sigma + j\omega\epsilon)} = \alpha + j\beta\ \ [\text{m}^{-1}],\\[6pt]
> \tilde{\mathbf{E}} = \hat x\,E_0e^{\mp\gamma z},
> \end{gathered}
> $$
> taking the root with $\alpha\ge0$ (and $\beta>0$). The **attenuation constant** $\alpha$ is in nepers per metre and the **phase constant** $\beta$ in radians per metre. They give the penetration depth $\delta = 1/\alpha$, the wavelength $\lambda = 2\pi/\beta$ and the phase velocity $v_p = \omega/\beta$. The partner is the intrinsic impedance: $\gamma\eta = j\omega\mu$ and $\gamma/\eta = \sigma + j\omega\epsilon$.

**Physics.** At one frequency the wave equation becomes $\nabla^2\tilde{\mathbf{E}} = \gamma^2\tilde{\mathbf{E}}$ with $\gamma^2 = j\omega\mu(\sigma + j\omega\epsilon)$. For a plane wave along $z$ its solutions are $e^{\mp\gamma z} = e^{\mp\alpha z}e^{\mp j\beta z}$: one complex number does two jobs. $e^{-\alpha z}$ shrinks the amplitude along the travel, and $e^{-j\beta z}$ turns the phase, one full turn per wavelength. In the time domain this is $\lvert E_0\rvert e^{-\alpha z}\cos(\omega t - \beta z + \angle E_0)$. With $\sigma = 0$, $\gamma = j\omega\sqrt{\mu\epsilon}$ is purely imaginary, and $\alpha = 0$. The lossless phase constant $\beta = \omega/v$ of Lectures 18–21 is the special case. Conductivity enters only through the replacement $j\omega\epsilon\to\sigma + j\omega\epsilon$ ([[3-maxwell-and-waves/22-phasor-maxwell-equations-and-damped-waves|Lecture 22]]).

Squaring $\gamma = \alpha + j\beta$ gives $\beta^2 - \alpha^2 = \omega^2\mu\epsilon$ and $2\alpha\beta = \omega\mu\sigma$, and from them the closed forms

$$
\begin{gathered}
\alpha = \omega\sqrt{\frac{\mu\epsilon}{2}}\left[\sqrt{1 + \Big(\frac{\sigma}{\omega\epsilon}\Big)^2} - 1\right]^{1/2},\\[6pt]
\beta = \omega\sqrt{\frac{\mu\epsilon}{2}}\left[\sqrt{1 + \Big(\frac{\sigma}{\omega\epsilon}\Big)^2} + 1\right]^{1/2} .
\end{gathered}
$$

The angle of $\gamma$ is $90^\circ - \tau$, where $\tau = \tfrac12\tan^{-1}(\sigma/\omega\epsilon)$ is the angle of $\eta$, so for a real $\sigma$ it always lies between 45° and 90°. Hence $\alpha/\beta = \tan\tau\le1$: **β is never smaller than α** in a conducting medium. (A collisionless plasma, whose $\sigma$ is imaginary, is the exception; see the last trap below.) Apart from the scale $\omega\sqrt{\mu\epsilon}$, everything depends on the single ratio $\sigma/\omega\epsilon$ ([[concepts/loss-tangent]]):

- $\sigma\ll\omega\epsilon$ (imperfect dielectric): $\alpha\approx(\sigma/2)\sqrt{\mu/\epsilon}$ and $\beta\approx\omega\sqrt{\mu\epsilon}$. The wave travels many wavelengths before it fades.
- $\sigma\gg\omega\epsilon$ (good conductor): $\gamma\approx\sqrt{j\omega\mu\sigma} = (1 + j)\sqrt{\pi f\mu\sigma}$, so $\alpha\approx\beta$. The amplitude falls by $e^{-2\pi}$ in one wavelength ([[concepts/skin-depth]]).

Reading a measured $\gamma$ backwards gives the medium: $\sigma = 2\alpha\beta/\omega\mu$ and $\epsilon = (\beta^2 - \alpha^2)/\omega^2\mu$.

**Examples.**
- A lossless, non-magnetic dielectric with $\epsilon_r = 4$ at 100 MHz: $\gamma = j\,4\pi/3 = j4.19$ m⁻¹, so $\lambda = 1.5$ m and there is no decay.
- [[3-maxwell-and-waves/22-phasor-maxwell-equations-and-damped-waves#5-the-general-formulas-and-how-to-decode-a-damped-wave|Lecture 22 §5]]: $\mathbf{E} = \hat y\,6e^{-x}\cos(3\times10^8t - 3x)$ V/m has $\gamma = 1 + j3$ m⁻¹ $= \sqrt{10}\,e^{j71.6^\circ}$ m⁻¹. That gives $\delta = 1$ m, $\lambda = 2.09$ m, and a medium with $\sigma/\omega\epsilon = 3/4$.
- At the crossover, $\epsilon_r = 4$, $\sigma = 0.04$ S/m and $f = 180$ MHz, so $\sigma = \omega\epsilon$: $\gamma = 3.43 + j8.28$ m⁻¹. Here the dielectric shortcut misses $\alpha$ by 10 % and the conductor shortcut by 55 %.
- Worked problem: a wave travelling toward $-x$ is written with $e^{+\gamma x}$, and its $\gamma = 1 + j2$ m⁻¹ puts a 3-4-5 triangle into $\gamma^2 = -3 + j4$ ([[problems/decoding-a-damped-wave]]).
- A collisionless plasma with $10^{12}$ electrons per m³ has $f_p\approx9$ MHz. Below it $\gamma$ is real (0.156 m⁻¹ at 5 MHz): the field decays but does not oscillate in space. Above it $\gamma$ is imaginary ($j0.375$ m⁻¹ at 20 MHz), and that is Lecture 21's plasma dispersion relation.
- On a transmission line, $\gamma = \sqrt{(\mathcal{R} + j\omega\mathcal{L})(\mathcal{G} + j\omega\mathcal{C})}$. A coax filled with a lossy medium (no wire resistance) has $\mathcal{L}\mathcal{C} = \mu\epsilon$ and $\mathcal{L}\mathcal{G} = \mu\sigma$, so its $\gamma$ equals the medium's.

> [!trap]
> - **Which root.** $\sqrt{\ }$ has two values, $\pm\gamma$. The other one does not give a new wave: $e^{-(-\gamma)z} = e^{+\gamma z}$ is just the wave travelling toward $-z$, which also decays along its own travel. So fix the convention once — take the root with $\alpha\ge0$ — and carry the direction in the sign of the exponent ($e^{-\gamma z}$ toward $+z$, $e^{+\gamma z}$ toward $-z$).
> - **γ is not β.** In a lossless medium $\gamma = j\beta$, so "$\gamma = 2$ rad/m" is off by a factor $j$. Quote $\gamma$ as $\alpha + j\beta$, in m⁻¹.
> - **The lossless formula in a lossy medium.** $\gamma = j\omega\sqrt{\mu\epsilon}$ holds only for $\sigma = 0$. With conductivity, both $\alpha$ and $\beta$ change.
> - **Amplitude against power.** $\delta = 1/\alpha$ is where the *field* is down to 37 %. Power falls as $e^{-2\alpha z}$, to 13.5 % at $\delta$. One neper is 8.686 dB of field amplitude.
> - **α > 0 does not always mean loss.** Below the plasma frequency $\gamma$ is real, yet nothing is absorbed: $\eta$ is imaginary, no average power flows in, and the wave is reflected.

**Where it appears.** [[3-maxwell-and-waves/18-the-wave-equation-and-plane-tem-waves|Lecture 18]] and [[3-maxwell-and-waves/19-dalembert-solutions-and-radiation-from-current-sheets|Lecture 19]] (the lossless $\beta = \omega/v$); [[3-maxwell-and-waves/21-monochromatic-waves-and-phasor-notation|Lecture 21]] ($\beta$ and dispersion relations); [[3-maxwell-and-waves/22-phasor-maxwell-equations-and-damped-waves|Lecture 22]] (defined, with the general formulas and the regimes); [[3-maxwell-and-waves/23-imperfect-dielectrics-and-good-conductors|Lecture 23]] (the two limits, skin depth, real materials); Lecture 24 (signal transmission); Unit 4 (lossy transmission lines); [[problems/decoding-a-damped-wave]].

**Practice.** [[practice/topics#damped-waves-in-lossy-and-conducting-media|Damped waves in lossy and conducting media]] (18 problems) — for example [[practice/22-damped-waves-in-conducting-media#221-phasor-maxwell-true-or-false|22.1 Phasor Maxwell, true or false]] (easy), [[practice/22-damped-waves-in-conducting-media#226-from-the-medium-to-the-wave|22.6 From the medium to the wave]] (medium), [[practice/22-damped-waves-in-conducting-media#229-decoding-a-wave-toward-minus-y|22.9 Decoding a wave toward minus y]] (hard).

Related: [[concepts/intrinsic-impedance]] · [[concepts/skin-depth]] · [[concepts/loss-tangent]] · [[concepts/dispersion-relation]] · [[concepts/phasors]] · [[concepts/plane-waves]] · [[concepts/wave-equation]].
