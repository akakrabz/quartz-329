---
title: "Propagation constant"
description: "γ = α + jβ = √(jωμ(σ + jωε)): α (Np/m) sets the decay, β (rad/m) the wavelength and phase velocity."
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
> taking $\alpha\ge0$ ($\beta>0$). **Attenuation constant** $\alpha$ [Np/m], **phase constant** $\beta$ [rad/m]: penetration depth $\delta = 1/\alpha$, $\lambda = 2\pi/\beta$, $v_p = \omega/\beta$. Partner: $\gamma\eta = j\omega\mu$, $\gamma/\eta = \sigma + j\omega\epsilon$.

**Physics.** At one frequency $\nabla^2\tilde{\mathbf{E}} = \gamma^2\tilde{\mathbf{E}}$; along $z$, $e^{\mp\gamma z} = e^{\mp\alpha z}e^{\mp j\beta z}$ decays and turns $2\pi$ per wavelength: $\lvert E_0\rvert e^{-\alpha z}\cos(\omega t - \beta z + \angle E_0)$. $\sigma = 0$ gives $\gamma = j\omega\sqrt{\mu\epsilon}$, the $\beta = \omega/v$ of Lectures 18–21. Conductivity: $j\omega\epsilon\to\sigma + j\omega\epsilon$ ([[3-maxwell-and-waves/22-phasor-maxwell-equations-and-damped-waves|Lecture 22]]). Squaring, $\beta^2 - \alpha^2 = \omega^2\mu\epsilon$ and $2\alpha\beta = \omega\mu\sigma$, so

$$
\begin{gathered}
\alpha = \omega\sqrt{\frac{\mu\epsilon}{2}}\left[\sqrt{1 + \Big(\frac{\sigma}{\omega\epsilon}\Big)^2} - 1\right]^{1/2},\\[6pt]
\beta = \omega\sqrt{\frac{\mu\epsilon}{2}}\left[\sqrt{1 + \Big(\frac{\sigma}{\omega\epsilon}\Big)^2} + 1\right]^{1/2} .
\end{gathered}
$$

$\angle\gamma = 90^\circ - \tau$, with $\tau = \tfrac12\tan^{-1}(\sigma/\omega\epsilon) = \angle\eta$: between 45° and 90° for real $\sigma$, so $\alpha/\beta = \tan\tau\le1$ (**β ≥ α**; plasma excepted). Only [[concepts/loss-tangent|σ/ωε]] matters beyond the scale $\omega\sqrt{\mu\epsilon}$:

- $\sigma\ll\omega\epsilon$: $\alpha\approx(\sigma/2)\sqrt{\mu/\epsilon}$, $\beta\approx\omega\sqrt{\mu\epsilon}$.
- $\sigma\gg\omega\epsilon$: $\gamma\approx\sqrt{j\omega\mu\sigma} = (1 + j)\sqrt{\pi f\mu\sigma}$, $\alpha\approx\beta$; $e^{-2\pi}$ per wavelength ([[concepts/skin-depth]]).

Backwards: $\sigma = 2\alpha\beta/\omega\mu$, $\epsilon = (\beta^2 - \alpha^2)/\omega^2\mu$.

**Examples.**
- Lossless, non-magnetic, $\epsilon_r = 4$, 100 MHz: $\gamma = j\,4\pi/3 = j4.19$ m⁻¹, $\lambda = 1.5$ m.
- [[3-maxwell-and-waves/22-phasor-maxwell-equations-and-damped-waves#5-the-general-formulas-and-how-to-decode-a-damped-wave|Lecture 22 §5]]: $\hat y\,6e^{-x}\cos(3\times10^8t - 3x)$ V/m: $\gamma = 1 + j3$ m⁻¹ $= \sqrt{10}\,e^{j71.6^\circ}$ m⁻¹, $\delta = 1$ m, $\lambda = 2.09$ m, $\sigma/\omega\epsilon = 3/4$.
- Crossover ($\epsilon_r = 4$, $\sigma = 0.04$ S/m, $f = 180$ MHz): $\gamma = 3.43 + j8.28$ m⁻¹; the dielectric shortcut misses $\alpha$ by 10 %, the conductor one by 55 %.
- Toward $-x$: $e^{+\gamma x}$; $\gamma = 1 + j2$ m⁻¹ gives $\gamma^2 = -3 + j4$, a 3-4-5 triangle ([[problems/decoding-a-damped-wave]]).
- Plasma, $10^{12}$ m⁻³, $f_p\approx9$ MHz: real $\gamma$ below (0.156 m⁻¹ at 5 MHz: no oscillation), imaginary above ($j0.375$ m⁻¹ at 20 MHz).
- Line: $\gamma = \sqrt{(\mathcal{R} + j\omega\mathcal{L})(\mathcal{G} + j\omega\mathcal{C})}$; a lossy-filled coax ($\mathcal{L}\mathcal{C} = \mu\epsilon$, $\mathcal{L}\mathcal{G} = \mu\sigma$) has the medium's $\gamma$.

> [!trap]
> - **Which root.** $-\gamma$ is no new wave: $e^{+\gamma z}$ is the $-z$ wave.
> - **γ is not β.** Lossless $\gamma = j\beta$: "$\gamma = 2$ rad/m" is off by $j$.
> - **Lossless formula.** $j\omega\sqrt{\mu\epsilon}$ needs $\sigma = 0$.
> - **Amplitude vs power.** At $\delta$ the field is 37 %, the power ($e^{-2\alpha z}$) 13.5 %. 1 Np = 8.686 dB.
> - **α > 0 is not always loss.** Below the plasma frequency $\gamma$ is real but $\eta$ imaginary: no average power enters; the wave reflects.

**Where it appears.** [[3-maxwell-and-waves/18-the-wave-equation-and-plane-tem-waves|Lecture 18]], [[3-maxwell-and-waves/19-dalembert-solutions-and-radiation-from-current-sheets|Lecture 19]] (lossless $\beta$); [[3-maxwell-and-waves/21-monochromatic-waves-and-phasor-notation|Lecture 21]] (dispersion); Lecture 22 (defined); [[3-maxwell-and-waves/23-imperfect-dielectrics-and-good-conductors|Lecture 23]] (limits); Lecture 24; Unit 4 (lossy lines).

**Practice.** [[practice/topics#damped-waves-in-lossy-and-conducting-media|Damped waves in lossy and conducting media]] (23 problems) — for example [[practice/22-damped-waves-in-conducting-media#221-phasor-maxwell-true-or-false|22.1 Phasor Maxwell, true or false]] (easy), [[practice/22-damped-waves-in-conducting-media#226-from-the-medium-to-the-wave|22.6 From the medium to the wave]] (medium), [[practice/22-damped-waves-in-conducting-media#229-decoding-a-wave-toward-minus-y|22.9 Decoding a wave toward minus y]] (hard).

Related: [[concepts/intrinsic-impedance]] · [[concepts/skin-depth]] · [[concepts/loss-tangent]] · [[concepts/dispersion-relation]] · [[concepts/phasors]] · [[concepts/plane-waves]] · [[concepts/wave-equation]].
