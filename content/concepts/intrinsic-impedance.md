---
title: "Intrinsic impedance"
description: "η = √(μ/ε) is the ratio |E|/|H| in a single travelling plane wave. In vacuum η₀ = √(μ₀/ε₀) = 376.7 Ω ≈ 120π Ω; in a medium η = η₀√(μr/εr) = μv. η fixes how big H is for a given E. Its direction comes from requiring E × H to point along the travel. In a conducting medium η = √(jωμ/(σ + jωε)) = |η|e^(jτ) is complex, with 0 ≤ τ < 45°, and H lags E by τ."
tags: [concept, waves]
aliases: ["wave impedance", "impedance of free space"]
---

> [!key] Definition
> $$
> \eta\equiv\sqrt{\frac{\mu}{\epsilon}} = \mu v = \frac{1}{\epsilon v} = \eta_0\sqrt{\frac{\mu_r}{\epsilon_r}}\ [\Omega],\qquad \eta_0 = \sqrt{\frac{\mu_0}{\epsilon_0}} = 376.7\ \Omega\approx120\pi\ \Omega .
> $$
> For one plane wave travelling along $\hat u$, $\mathbf{H} = \hat u\times\mathbf{E}/\eta$. So $\lvert\mathbf{E}\rvert = \eta\lvert\mathbf{H}\rvert$ and, with $\mathbf{B} = \mu\mathbf{H}$, $\lvert\mathbf{B}\rvert = \lvert\mathbf{E}\rvert/v$. For $\mathbf{E} = \hat xE_x$ travelling along $z$: $E_x/H_y = +\eta$ toward $+z$ and $-\eta$ toward $-z$.

**Physics.** It falls out of either curl equation. For $E_x = f(t - z/v)$, Faraday's law $\partial E_x/\partial z = -\mu\,\partial H_y/\partial t$ gives $H_y = f/(\mu v)$, and $\mu v = \mu/\sqrt{\mu\epsilon} = \sqrt{\mu/\epsilon}$. Ampère's law gives the same through $\epsilon v = 1/\eta$. Units: $\mu/\epsilon$ is (H/m)/(F/m) = H/F = (Ω·s)/(s/Ω) = Ω², so $\eta$ is in ohms. It is an impedance in the circuit sense, a ratio of a volt-like field (V/m) to an ampere-like one (A/m). It is not a resistor, though: in a lossless medium nothing is dissipated, and the energy is carried away (Lecture 20). In a lossless medium $\eta$ is a positive real number; the sign of $\mathbf{H}$ comes from $\hat u\times\mathbf{E}$. On a transmission line the same role is played by $\sqrt{\mathcal{L}/\mathcal{C}}$, which is $\eta$ times a geometric factor: $(\eta/2\pi)\ln(b/a)$ for a coax and $\eta\,d/W$ for parallel plates. In a conducting medium $\eta$ becomes complex and $\mathbf{E}$, $\mathbf{H}$ fall out of phase ([[3-maxwell-and-waves/22-phasor-maxwell-equations-and-damped-waves|Lecture 22]]; see the section below). At an interface the two media's $\eta$'s decide how much of a wave reflects (Lecture 25).

**Examples.**
- Vacuum: a 1 V/m wave has $H = 2.65$ mA/m and $B = 3.34$ nT ($= E/c$).
- Non-magnetic dielectrics: $\epsilon_r = 2.25$ gives 251 Ω ($80\pi$); $\epsilon_r = 4$ gives 188 Ω ($60\pi$); $\epsilon_r = 9$ gives 126 Ω ($40\pi$). From a measured speed, $\eta = \mu_0v$: $v = 2\times10^8$ m/s gives $80\pi = 251.3\ \Omega$.
- A magnetic dielectric with $\mu_r = 2$, $\epsilon_r = 8$ has $\eta = \eta_0/2 = 188\ \Omega$, the same as $\epsilon_r = 4$ alone, but half the speed ($c/4$). $\eta$ depends on the *ratio* $\mu_r/\epsilon_r$ and $v$ on the *product*.
- Coax with polyethylene and $b/a = 3.5$: $\sqrt{\mathcal{L}/\mathcal{C}} = 0.199\times251\ \Omega = 50\ \Omega$ ([[problems/coax-inductance-and-the-lc-product]]).
- Worked problem: 6 V/m in polyethylene pairs with $6/251.3 = 23.9$ mA/m, not $6/377 = 15.9$ mA/m.

> [!trap]
> - $\eta$ versus $1/\eta$: $H = E/\eta$, so 1 V/m gives 2.65 *milli*amperes per metre. The notes' $\mathbf{H}$ amplitude $\sqrt{\epsilon/\mu}$ is $1/\eta$.
> - Use the medium's $\eta$, not $\eta_0$: in a non-magnetic dielectric $\eta = \eta_0/\sqrt{\epsilon_r}$.
> - $E_x/H_y = \pm\eta$ holds for one travelling wave. With $E_x = Af + Bg$ and $H_y = (Af - Bg)/\eta$ the ratio is $\eta\,(Af+Bg)/(Af-Bg)$, which can be anything.
> - $120\pi = 376.99\ \Omega$ approximates $376.73\ \Omega$ to 0.07 %. Either is accepted; say which you used.

**In a conducting medium (Lecture 22).** With conductivity, Ampère's law carries $\sigma + j\omega\epsilon$ where it had $j\omega\epsilon$, and $\sqrt{\mu/\epsilon} = \sqrt{j\omega\mu/j\omega\epsilon}$ becomes complex:

> [!key] Complex intrinsic impedance
> $$
> \begin{gathered}
> \eta = \sqrt{\frac{j\omega\mu}{\sigma + j\omega\epsilon}} = \lvert\eta\rvert e^{j\tau},\\[6pt]
> \gamma\eta = j\omega\mu,\qquad \frac{\gamma}{\eta} = \sigma + j\omega\epsilon,\\[6pt]
> \lvert\eta\rvert = \frac{\sqrt{\mu/\epsilon}}{\big[1 + (\sigma/\omega\epsilon)^2\big]^{1/4}},\\[6pt]
> \tau = \frac12\tan^{-1}\frac{\sigma}{\omega\epsilon}\quad(0\le\tau<45^\circ).
> \end{gathered}
> $$
> The rotation rule is unchanged, $\tilde{\mathbf{H}} = \hat u\times\tilde{\mathbf{E}}/\eta$, but dividing by a complex $\eta$ also shifts the phase. At every point $\mathbf{H}$ lags $\mathbf{E}$ by $\tau$, a time $\tau/\omega$, and the ratio of the amplitudes is $\lvert\eta\rvert$. Here $\gamma = \alpha + j\beta$ is the [[concepts/propagation-constant|propagation constant]].

Where the angle comes from: $j\omega\mu$ points at 90° and $\sigma + j\omega\epsilon$ at $90^\circ - \tan^{-1}(\sigma/\omega\epsilon)$, and $\eta$ is the square root of their ratio. The magnitude follows from $\lvert\gamma\rvert\lvert\eta\rvert = \omega\mu$. Conduction makes the wave vary faster in space ($\lvert\gamma\rvert$ grows), so a given $\mathbf{E}$ drives a larger $\mathbf{H}$ and $\lvert\eta\rvert$ drops below $\sqrt{\mu/\epsilon}$. The ratio $\sigma/\omega\epsilon$ ([[concepts/loss-tangent]]) controls both: $\tau\approx\sigma/2\omega\epsilon$ (rad) and $\lvert\eta\rvert\approx\sqrt{\mu/\epsilon}$ in an imperfect dielectric; $\eta\approx\sqrt{\omega\mu/\sigma}\,e^{j\pi/4}$ in a good conductor, a small fraction of $\sqrt{\mu/\epsilon}$ ([[3-maxwell-and-waves/23-imperfect-dielectrics-and-good-conductors|Lecture 23]]). Read with $\gamma$, $\eta$ also identifies the medium ($\gamma/\eta = \sigma + j\omega\epsilon$), and its angle reappears in the average power as $\cos\tau$ (Lecture 23).

- Lecture 22's decoding example: $\gamma = 1 + j3$ m⁻¹ at $\omega = 3\times10^8$ rad/s with $\mu_0$ gives $\eta = j\omega\mu_0/\gamma = 12\pi(3 + j) = 119.2\,e^{j18.4^\circ}\ \Omega$. The same medium without its conductivity ($\epsilon = 8\epsilon_0$) would have $\eta_0/\sqrt8 = 133.3\ \Omega$.
- Worked problem: $\mu = 3\mu_0$, $\epsilon = 9\epsilon_0$, $\sigma/\omega\epsilon = 4/3$ gives $\eta = 24\pi(2 + j) = 168.6\,e^{j26.6^\circ}\ \Omega$ against a lossless $217.7\ \Omega$ ([[problems/decoding-a-damped-wave]]).
- At the crossover $\sigma = \omega\epsilon$: $\lvert\eta\rvert = 2^{-1/4}\sqrt{\mu/\epsilon} = 0.84\sqrt{\mu/\epsilon}$ and $\tau = 22.5^\circ$.
- A current sheet in a conducting medium still sets $\mathbf{H} = \tfrac12\mathbf{J}_s\times\hat n$ at its faces, but now $\mathbf{E} = -\tfrac\eta2\mathbf{J}_s$ is shifted by $\tau$ and is no longer exactly opposite to the current (Lecture 22 §7).

> [!trap]
> - **The lossless formula.** $\sqrt{\mu/\epsilon}$ is $\eta$ only for $\sigma = 0$. In a lossy medium use $j\omega\mu/\gamma$ or the full square root.
> - **The sign of τ.** $\tilde{\mathbf{H}} = \tilde{\mathbf{E}}/\eta$ subtracts $\tau$ from the phase; $\tilde{\mathbf{E}} = \eta\tilde{\mathbf{H}}$ adds it. With real $\mu$, $\epsilon$ and $\sigma$, $\mathbf{H}$ lags.
> - **Ratios of instantaneous values.** $\lvert\eta\rvert$ is the ratio of the *amplitudes*. Because $\mathbf{E}$ and $\mathbf{H}$ cross zero at different times, $E_x(t)/H_y(t)$ is not constant in a lossy medium.
> - **The 0–45° range assumes a real σ.** In a collisionless plasma below its plasma frequency, $\eta$ is purely imaginary: $\mathbf{E}$ and $\mathbf{H}$ are 90° apart and carry no average power (Lecture 22 §8).

**Where it appears.** [[3-maxwell-and-waves/18-the-wave-equation-and-plane-tem-waves|Lecture 18]] (defined; the sign table); [[3-maxwell-and-waves/19-dalembert-solutions-and-radiation-from-current-sheets|Lecture 19]] (a current sheet radiates $\lvert\mathbf{E}\rvert = \eta J_s/2$ on each side, because it drives two half-spaces of impedance $\eta$ in parallel; see [[concepts/current-sheet-radiation]]); Lecture 20 (a travelling wave carries $E^2/\eta$ per unit area); [[3-maxwell-and-waves/22-phasor-maxwell-equations-and-damped-waves|Lecture 22]] (complex $\eta$, $\gamma\eta = j\omega\mu$, the lag $\tau$); [[3-maxwell-and-waves/23-imperfect-dielectrics-and-good-conductors|Lecture 23]] (its two limits, and $\cos\tau$ in the power); Lecture 25 (reflection); Unit 4 ($\sqrt{\mathcal{L}/\mathcal{C}}$); [[problems/a-pulse-on-the-move]]; [[problems/decoding-a-damped-wave]].

**Practice.** [[practice/topics#plane-waves-and-the-wave-equation|Plane waves and the wave equation]] (24 problems) — for example [[practice/18-wave-equation-and-plane-waves#181-which-way-and-how-fast|18.1 Which way and how fast]] (easy), [[practice/18-wave-equation-and-plane-waves#186-which-fields-can-be-waves|18.6 Which fields can be waves]] (medium), [[practice/18-wave-equation-and-plane-waves#189-triangle-pulse-in-a-magnetic-medium|18.9 Triangle pulse in a magnetic medium]] (hard).

Related: [[concepts/plane-waves]] · [[concepts/wave-equation]] · [[concepts/propagation-constant]] · [[concepts/loss-tangent]] · [[concepts/permittivity]] · [[concepts/permeability]] · [[concepts/inductance]] · [[concepts/capacitance]].
