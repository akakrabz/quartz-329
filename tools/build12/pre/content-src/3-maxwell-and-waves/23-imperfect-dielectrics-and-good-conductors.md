---
title: "Lecture 23 — Imperfect dielectrics and good conductors"
description: "The loss tangent σ/ωε decides how a medium treats a wave: below about 0.1 an imperfect dielectric with α ≈ (σ/2)√(μ/ε), above about 10 a good conductor with α = β = 1/δ, δ = 1/√(πfμσ) and η = (1+j)/(σδ). Seawater has δ ≈ 8 m at 1 kHz but 1.3 cm at 1 GHz, which is why submarines are reached at very low frequencies, and slowly."
tags: [lecture, waves]
lecture: 23
---

*Lecture 23 · course notes §23 · **slides: not yet available — this page is built from the course notes** · prev: [[3-maxwell-and-waves/22-phasor-maxwell-equations-and-damped-waves|Lecture 22]] · next: [[3-maxwell-and-waves/24-signal-transmission-and-circular-polarization|Lecture 24]] · worked problem: [[problems/a-radio-wave-into-moist-ground|A radio wave into moist ground]] · practice: [[practice/23-imperfect-dielectrics-and-good-conductors|12 problems]]*

> [!abstract] In one breath
> The **loss tangent** $\sigma/\omega\epsilon$, conduction over displacement current, sorts the damped waves of [[3-maxwell-and-waves/22-phasor-maxwell-equations-and-damped-waves|Lecture 22]]. Small: an **imperfect dielectric**, $\alpha\approx(\sigma/2)\sqrt{\mu/\epsilon}$, the rate at which Joule heat drains the Poynting flux. Large: a **good conductor**, $\alpha = \beta = 1/\delta$ with **skin depth** $\delta = 1/\sqrt{\pi f\mu\sigma}$ and $\eta = (1+j)/(\sigma\delta)$, the field gone within a wavelength. Power falls as $e^{-2\alpha z}$. Seawater's $\delta$ is 7.96 m at 1 kHz but 1.3 cm at 1 GHz: hence slow very-low-frequency submarine links.

## 1. When does a medium count as a conductor?

In electrostatics any free charge makes a conductor ([[1-electrostatics/08-conductors-dielectrics-and-polarization|Lecture 8]]); for a wave it depends on frequency. Ampère's law ([[3-maxwell-and-waves/22-phasor-maxwell-equations-and-damped-waves|Lecture 22]]):

$$
\nabla\times\tilde{\mathbf{H}} = \underbrace{\sigma\tilde{\mathbf{E}}}_{\text{conduction}} + \underbrace{j\omega\epsilon\tilde{\mathbf{E}}}_{\text{displacement}} = (\sigma + j\omega\epsilon)\,\tilde{\mathbf{E}} .
$$

The conduction current is in phase with $\tilde{\mathbf{E}}$ and dissipates (the Joule heating $\mathbf{J}\cdot\mathbf{E}$ of [[1-electrostatics/10-capacitance-and-conductance|Lecture 10]]); the displacement current leads by 90° and only stores and returns energy.

> [!key] The loss tangent, and the four regimes
> $$
> \frac{\lvert\sigma\tilde{\mathbf{E}}\rvert}{\lvert j\omega\epsilon\tilde{\mathbf{E}}\rvert} = \frac{\sigma}{\omega\epsilon}
> $$
> is dimensionless, with $\omega = 2\pi f$ and the medium's own $\epsilon$.
> - $\sigma = 0$: **perfect dielectric** (Lectures 18–21).
> - $\sigma/\omega\epsilon\ll1$, in practice below 0.1: **imperfect dielectric** (Lecture 22's notes: "lousy conductor"); displacement current dominates.
> - $\sigma/\omega\epsilon\gg1$, in practice above 10: **good conductor**; conduction current dominates.
> - $\sigma\to\infty$: **perfect conductor**, no field inside ([[3-maxwell-and-waves/16-charge-conservation-displacement-current-and-maxwells-equations|Lecture 16]]).
>
> Between 0.1 and 10 the approximations lose accuracy (good-conductor ones fastest, §2): use Lecture 22's exact formulas. The name: the tangent of the angle between displacement and total current ([[concepts/loss-tangent|loss-tangent page]]); Rao and the exams use it, the notes do not.

**Crossover frequency.** The currents are equal at

$$
f_c = \frac{\sigma}{2\pi\epsilon}.
$$

More than a decade below $f_c$: good conductor; more than a decade above: imperfect dielectric. With [[1-electrostatics/08-conductors-dielectrics-and-polarization|Lecture 8]]'s relaxation time $\tau_r = \epsilon/\sigma$ (Lecture 8's $\tau$; here $\tau = \angle\eta$), $\sigma/\omega\epsilon = 1/(\omega\tau_r)$ and $f_c = 1/(2\pi\tau_r)$: a good conductor's charges rearrange, cancelling the field, many times per period. Seawater, $\tau_r = 0.18$ ns, has about a millisecond per cycle at 1 kHz; at 10 GHz the 0.1 ns period is too short. The leaky capacitor of [[1-electrostatics/10-capacitance-and-conductance#6-conductance-the-leaky-capacitor|Lecture 10]], $C$ parallel to $G = (\sigma/\epsilon)C$, has the same ratio $G/\omega C$: "resistor-like for $\omega\ll\sigma/\epsilon$ and capacitor-like for $\omega\gg\sigma/\epsilon$".

Typical values (constant $\sigma$, $\epsilon$):

| medium | $\sigma$ [S/m] | $\epsilon_r$ | $f_c = \sigma/2\pi\epsilon$ | good conductor below | imperfect dielectric above |
|---|---|---|---|---|---|
| copper | $5.8\times10^{7}$ | 1 | $1.0\times10^{18}$ Hz | every radio and microwave frequency | — |
| seawater | 4 | 81 | 0.89 GHz | 89 MHz | 8.9 GHz |
| moist soil (loam) | $10^{-2}$ | 10 | 18 MHz | 1.8 MHz | 180 MHz |
| the notes' Example 1 medium | $10^{-3}$ | 4 | 4.5 MHz | 450 kHz | 45 MHz |
| fresh water | $10^{-3}$ | 80 | 225 kHz | 22 kHz | 2.2 MHz |
| dry earth | $10^{-5}$ | 5 | 36 kHz | 3.6 kHz | 360 kHz |
| Bakelite | $10^{-9}$ | 4.9 | 3.7 Hz | 0.37 Hz | 37 Hz |
| mica | $10^{-11}$ | 6 | 0.03 Hz | — | 0.3 Hz |

Values: Rao Tables 5.1–5.2 (mica: top of its range; moist soil: "wet earth") and Problem 5.25; seawater's 81 from the notes (Rao: 80); loam's $\sigma$ from ITU-R P.527 (about $10^{-2}$ S/m moist, $10^{-4}$ dried). Rao Table 5.3 agrees: $3.6\times10^4$ Hz for dry earth, $0.9\times10^9$ Hz for seawater with $\epsilon_r = 80$. Soil and water vary widely: typical values.

<!-- fig:cond-regime-map -->

> [!example] Example — seawater at four frequencies
> $\sigma = 4$ S/m, $\epsilon = 81\epsilon_0$: $\sigma/\omega\epsilon = 8.9\times10^{5}$ at 1 kHz, 888 at 1 MHz, 0.89 at 1 GHz, 0.089 at 10 GHz: good conductor, good conductor, in between, imperfect dielectric. Without a calculator ($\epsilon_0\approx10^{-9}/36\pi$ F/m):
> $$
> \begin{gathered}
> \frac{\sigma}{\omega\epsilon} = \frac{\sigma\cdot36\pi\times10^{9}}{2\pi f\,\epsilon_r} = \frac{18\times10^{9}\,\sigma}{f\,\epsilon_r},\\[4pt]
> \text{at 1 kHz:}\quad \frac{18\times10^{9}\times4}{10^{3}\times81} = 8.9\times10^{5}.
> \end{gathered}
> $$

> [!trap] Classifying a medium
> - Use the medium's own $\epsilon$: $\epsilon_0$ for $81\epsilon_0$ makes seawater's ratio 81 times too large, harmless at 1 kHz, decisive near the crossover.
> - $\omega = 2\pi f$, not $f$: dropping $2\pi$ moves the ratio by 6.3.
> - Never classify by name (seawater above; the table's dry earth is a good conductor at 100 Hz).
> - Real $\sigma$, $\epsilon$ vary with frequency ([[1-electrostatics/11-lorentz-drude-models-for-conductivity-and-susceptibility|Lecture 11]]), so $f_c$ is a guide, not a sharp line: water's permittivity falls in the microwave range (ITU-R P.527), and copper's $\sigma$ stops being constant above about $10^{13}$ Hz.

## 2. The notes' table, and the one number behind it

The notes tabulate Lecture 22's regimes; in this site's notation ($\eta = \lvert\eta\rvert e^{j\tau}$, $\lambda = 2\pi/\beta$, $\delta = 1/\alpha$):

| regime | condition | $\alpha$ [Np/m] | $\beta$ [rad/m] | $\lvert\eta\rvert$ [Ω] | $\tau = \angle\eta$ | $\lambda$ | $\delta = 1/\alpha$ |
|---|---|---|---|---|---|---|---|
| perfect dielectric | $\sigma = 0$ | $0$ | $\omega\sqrt{\mu\epsilon}$ | $\sqrt{\mu/\epsilon}$ | $0$ | $2\pi/\omega\sqrt{\mu\epsilon}$ | $\infty$ |
| imperfect dielectric | $\sigma/\omega\epsilon\ll1$ | ${\approx\dfrac\sigma2\sqrt{\mu/\epsilon}}$ | ${\approx\omega\sqrt{\mu\epsilon}}$ | ${\approx\sqrt{\mu/\epsilon}}$ | ${\approx\dfrac{\sigma}{2\omega\epsilon}}$ | ${\approx2\pi/\omega\sqrt{\mu\epsilon}}$ | ${\approx\dfrac2\sigma\sqrt{\epsilon/\mu}}$ |
| good conductor | $\sigma/\omega\epsilon\gg1$ | ${\approx\sqrt{\pi f\mu\sigma}}$ | ${\approx\sqrt{\pi f\mu\sigma}}$ | ${\approx\sqrt{\omega\mu/\sigma}}$ | ${\approx45^\circ}$ | ${\approx2\pi\delta}$ | ${\approx1/\sqrt{\pi f\mu\sigma}}$ |
| perfect conductor | $\sigma\to\infty$ | $\infty$ | $\infty$ | $0$ | — | $0$ | $0$ |

The notes write the imperfect-dielectric $\alpha$ as $\beta\cdot\tfrac12\sigma/\omega\epsilon$ (the same) and recall the damped-wave pair and the $\langle\mathbf{S}\rangle$ of [[3-maxwell-and-waves/21-monochromatic-waves-and-phasor-notation|Lecture 21]].

**Where the entries come from.** Instead of Lecture 22's binomial expansion, polar form gives the limits and the exact values at once:

$$
\begin{gathered}
\gamma = j\omega\sqrt{\mu\epsilon}\,\big(1 - jp\big)^{1/2},\\[4pt]
\eta = \sqrt{\frac\mu\epsilon}\,\big(1 - jp\big)^{-1/2},\qquad p\equiv\frac{\sigma}{\omega\epsilon}.
\end{gathered}
$$

In polar form $1 - jp = \sqrt{1+p^2}\,e^{-j\theta}$, with **loss angle** $\theta = \tan^{-1}p$, between 0 and 90°.

> [!key] Exact forms for any medium (this site's packaging of Lecture 22)
> $$
> \begin{gathered}
> \alpha = \omega\sqrt{\mu\epsilon}\,(1+p^2)^{1/4}\sin\frac\theta2,\\[4pt]
> \beta = \omega\sqrt{\mu\epsilon}\,(1+p^2)^{1/4}\cos\frac\theta2,\\[4pt]
> \lvert\eta\rvert = \sqrt{\frac\mu\epsilon}\,(1+p^2)^{-1/4},\\[4pt]
> \tau = \angle\eta = \frac\theta2 = \frac12\tan^{-1}\frac{\sigma}{\omega\epsilon},\qquad \frac\alpha\beta = \tan\tau .
> \end{gathered}
> $$
> $\tau$ is half the loss angle (0 to 45°), and $\alpha/\beta = \tan\tau\le1$: $\alpha$ never exceeds $\beta$.

> [!derivation]- The polar-form derivation
> $(1 - jp)^{1/2} = (1+p^2)^{1/4}e^{-j\theta/2}$ (positive real part), so
> $$
> \begin{gathered}
> \gamma = j\omega\sqrt{\mu\epsilon}\,(1+p^2)^{1/4}e^{-j\theta/2}\\[4pt]
> = \omega\sqrt{\mu\epsilon}\,(1+p^2)^{1/4}\,e^{j(\pi/2 - \theta/2)},
> \end{gathered}
> $$
> with real part $\omega\sqrt{\mu\epsilon}(1+p^2)^{1/4}\cos(\pi/2 - \theta/2) = \ldots\sin(\theta/2) = \alpha$ and imaginary part $\ldots\cos(\theta/2) = \beta$. $0\le\theta<\pi/2$ gives $\beta>0$, $\alpha\ge0$ ($\alpha = 0$ only for $\sigma = 0$): $e^{-\gamma z}$ travels toward $+z$ and decays. $(1 - jp)^{-1/2} = (1+p^2)^{-1/4}e^{+j\theta/2}$ gives $\lvert\eta\rvert = \sqrt{\mu/\epsilon}\,(1+p^2)^{-1/4}$ and $\tau = \theta/2$; dividing, $\alpha/\beta = \tan(\theta/2)$. (The notes' small-$p$ phase $\tan^{-1}(\sigma/2\omega\epsilon)$ agrees to first order in $p$.)

**The two limits.** $p\ll1$: $\theta\approx p$, $(1+p^2)^{1/4}\approx1$, so $\alpha\approx\omega\sqrt{\mu\epsilon}\cdot p/2 = (\sigma/2)\sqrt{\mu/\epsilon}$ and $\tau\approx p/2$; the second row, where only the decay is new. $p\gg1$: $\theta\to90^\circ$, $(1+p^2)^{1/4}\approx\sqrt p$, so $\alpha\approx\beta\approx\omega\sqrt{\mu\epsilon}\,\sqrt p\,/\sqrt2 = \sqrt{\pi f\mu\sigma}$, $\lvert\eta\rvert\approx\sqrt{\mu/\epsilon}/\sqrt p = \sqrt{\omega\mu/\sigma}$, $\tau\to45^\circ$; the third row, with $\epsilon$ gone.

**How small is "small"?** At $p = 0.1$ the imperfect-dielectric formulas are within 0.3 % ($\alpha$, $\beta$ 0.12 %, $\lvert\eta\rvert$ 0.25 %, $\tau$ 0.33 %); at 0.3, $\alpha$ within 1.1 %. At $p = 10$ the good-conductor $\alpha$ is 5 % high, $\beta$ 5 % low, the true $\tau$ 42.1°; at 3, $\alpha$ is 18 % high. At $p = 1$ both fail (imperfect-dielectric $\alpha$ 10 %, good-conductor $\alpha$ 55 % high; Lecture 22's crossover example). Hence 0.1 and 10.

<!-- fig:cond-seawater-alpha-beta -->

**The attenuation saturates.** Above $10f_c$, $\alpha = (\sigma/2)\sqrt{\mu/\epsilon}$ no longer grows with frequency (per wavelength it even falls); below $f_c/10$, $\alpha = \sqrt{\pi f\mu\sigma}$ grows as $\sqrt f$, so lower frequencies always penetrate further. Seawater's plateau: 84 Np/m, a penetration depth of 1.2 cm. (Rao Problem 5.26: the good-conductor $\alpha$ is the plateau value times $\sqrt{2\omega\epsilon/\sigma}$.)

> [!example] Example — classifying a medium from a measured wavelength and penetration depth (this site's numbers)
> 200 MHz, non-magnetic, $\lambda = 0.5$ m, $\delta = 20$ m. Regime, $v_p$, $\epsilon_r$, $\lvert\eta\rvert$, $\sigma$?
> - $\beta = 2\pi/\lambda = 4\pi = 12.6$ rad/m, $\alpha = 1/\delta = 0.05$ Np/m: $\alpha/\beta = \tan\tau = 0.004$, $\tau = 0.23^\circ$, $p = \tan2\tau = 0.008\ll1$, an **imperfect dielectric** (the field takes 40 wavelengths to reach $1/e$; a good conductor would have $\alpha = \beta$).
> - $v_p = \lambda f = 0.5\times2\times10^{8} = 10^{8}$ m/s, so $\epsilon_r = (c/v_p)^2 = 9$ ($\beta\approx\omega\sqrt{\mu_0\epsilon}$); $\lvert\eta\rvert\approx\eta_0/3 = 40\pi\approx126\ \Omega$.
> - $\sigma = 2\alpha/\lvert\eta\rvert = 0.1/(40\pi) = 8.0\times10^{-4}$ S/m. Check: $\sigma/\omega\epsilon = 8.0\times10^{-4}/(2\pi\cdot2\times10^{8}\cdot9\epsilon_0) = 0.008$ ✓.

## 3. Imperfect dielectrics: slow decay, and where the power goes

> [!example] Example 1 (notes) — a 1 GHz wave in an imperfect dielectric
> $\tilde{\mathbf{E}} = \hat y\,2e^{-\alpha z}e^{-j\beta z}$ V/m toward $+z$; $\epsilon = 4\epsilon_0$, $\mu = \mu_0$, $\sigma = 10^{-3}$ S/m, $\omega = 2\pi\times10^{9}$ rad/s. Find $\tilde{\mathbf{H}}$, $\langle\mathbf{S}\rangle$, and $\langle\mathbf{S}\rangle$ at $z = 0$ and 10 m.
>
> **Classify.** $\sigma/\omega\epsilon = 10^{-3}\cdot36\pi\times10^{9}/(2\pi\times10^{9}\cdot4) = 4.5\times10^{-3}\ll1$. So $\tau\approx\sigma/2\omega\epsilon = 2.25\times10^{-3}$ rad $= 0.13^\circ$, $\lvert\eta\rvert\approx\sqrt{\mu_0/4\epsilon_0} = \eta_0/2\approx60\pi = 188\ \Omega$, $\alpha\approx(\sigma/2)\lvert\eta\rvert = 30\pi\times10^{-3} = 0.094$ Np/m, $\beta\approx\omega\sqrt{\mu_0\cdot4\epsilon_0} = 41.9$ rad/m, $\lambda = 15$ cm.
>
> **Magnetic field.** Divide by $\eta$; $\mathbf{E}\times\mathbf{H}$ along $+\hat z$ needs $\hat z\times\hat y = -\hat x$:
> $$
> \begin{gathered}
> \tilde{\mathbf{H}} = -\hat x\,\frac{2}{\eta}\,e^{-\alpha z}e^{-j\beta z}\\[4pt]
> = -\hat x\,\frac{2}{\lvert\eta\rvert}\,e^{-\alpha z}e^{-j\beta z}e^{-j\tau}\ \ \text{A/m}.
> \end{gathered}
> $$
> Check: $\hat y\times(-\hat x) = +\hat z$ ✓. Time domain ($E_0$ real):
> $$
> \begin{gathered}
> \mathbf{E} = \hat y\,2e^{-\alpha z}\cos(\omega t - \beta z)\ \text{V/m},\\[4pt]
> \mathbf{H} = -\hat x\,\frac{2}{\lvert\eta\rvert}e^{-\alpha z}\cos(\omega t - \beta z - \tau)\ \text{A/m},
> \end{gathered}
> $$
> $2/\lvert\eta\rvert = 10.6$ mA/m; $\mathbf{H}$ lags by 0.13°.
>
> **Power.**
> $$
> \begin{gathered}
> \langle\mathbf{S}\rangle = \tfrac12\text{Re}\{\tilde{\mathbf{E}}\times\tilde{\mathbf{H}}^*\}\\[4pt]
> = \tfrac12\text{Re}\Big\{\hat y\times(-\hat x)\,\frac{4}{\lvert\eta\rvert}e^{-2\alpha z}e^{+j\tau}\Big\}\\[4pt]
> = \hat z\,\frac{2}{\lvert\eta\rvert}\cos\tau\,e^{-2\alpha z}\ \ \text{W/m}^2 .
> \end{gathered}
> $$
> $z = 0$: $2/(60\pi) = 1/(30\pi) = 10.6$ mW/m². $z = 10$ m: $e^{-2\times0.094\times10} = e^{-0.6\pi} = 0.15$, so $0.15/(30\pi)\approx1.6$ mW/m², 15 % left. Loss $8.686\,\alpha = 0.82$ dB/m, 8.2 dB over 10 m; $\delta = 1/\alpha = 10.6$ m.

> [!key] Time-average power in a lossy medium
> For $\tilde{\mathbf{E}} = \hat xE_0e^{-\alpha z}e^{-j\beta z}$, $\tilde{\mathbf{H}} = \hat y\,(E_0/\eta)\,e^{-\alpha z}e^{-j\beta z}$, $E_0$ possibly complex:
> $$
> \begin{gathered}
> \langle\mathbf{S}\rangle = \tfrac12\text{Re}\{\tilde{\mathbf{E}}\times\tilde{\mathbf{H}}^*\}\\[4pt]
> = \hat z\,\frac{\lvert E_0\rvert^2}{2\lvert\eta\rvert}\,\cos\tau\;e^{-2\alpha z}\quad[\text{W/m}^2].
> \end{gathered}
> $$
> - **Power** reaches $1/e$ at $z = \delta/2$, the field at $z = \delta$.
> - In **decibels** both fall at the same rate: $10\log_{10}e^{2\alpha z} = 20\log_{10}e^{\alpha z} = 8.686\,\alpha z$ dB (1 Np = 8.686 dB).
> - $\cos\tau$ is a power factor: 1 lossless, $1/\sqrt2$ in a good conductor.

**Where the lost power goes: heat.** Cycle-averaged, stored energy drops out of Poynting's theorem ([[3-maxwell-and-waves/20-poynting-theorem-and-monochromatic-waves|Lecture 20]], [[concepts/poynting-theorem]]): $\nabla\cdot\langle\mathbf{S}\rangle = -\langle\mathbf{J}\cdot\mathbf{E}\rangle$. With $\mathbf{J} = \sigma\mathbf{E}$ and $z$ dependence only:

$$
\begin{gathered}
-\frac{d\langle S_z\rangle}{dz} = 2\alpha\,\frac{\lvert E_0\rvert^2\cos\tau}{2\lvert\eta\rvert}\,e^{-2\alpha z}\\[4pt]
= \langle\mathbf{J}\cdot\mathbf{E}\rangle = \tfrac12\sigma\lvert E_0\rvert^2e^{-2\alpha z}\\[4pt]
\Longrightarrow\quad \alpha = \frac{\sigma\lvert\eta\rvert}{2\cos\tau}.
\end{gathered}
$$

Exact for any medium (Lecture 22's $\text{Re}\{\gamma/\eta\} = \sigma$ in disguise); with $\cos\tau\approx1$, $\lvert\eta\rvert\approx\sqrt{\mu/\epsilon}$ it is the table's $\alpha = (\sigma/2)\sqrt{\mu/\epsilon}$, so that entry is energy conservation. Example 1 at $z = 0$: $\tfrac12\sigma\lvert E_0\rvert^2 = \tfrac12\times10^{-3}\times4 = 2.0$ mW/m³ $= 2\alpha\langle S_z\rangle = 2\times0.094\times10.6$ mW/m² ✓.

The notes add: such heating is what a microwave oven is for (in food much of the loss is lagging water polarization, not $\sigma$; the loss tangent lumps both, [[concepts/loss-tangent]]); for communication it is waste.

## 4. Good conductors: skin depth, $\eta = (1+j)/(\sigma\delta)$ and the 45° lag

For $\sigma\gg\omega\epsilon$ drop $j\omega\epsilon$: $\gamma\approx\sqrt{j\omega\mu\sigma}$, $\eta\approx\sqrt{j\omega\mu/\sigma}$, and $\sqrt j = e^{j\pi/4} = (1+j)/\sqrt2$.

> [!key] A plane wave in a good conductor
> $$
> \begin{gathered}
> \delta = \frac{1}{\sqrt{\pi f\mu\sigma}} = \sqrt{\frac{2}{\omega\mu\sigma}},\\[4pt]
> \gamma = \frac{1+j}{\delta}\quad(\alpha = \beta = 1/\delta),\\[4pt]
> \eta = \frac{1+j}{\sigma\delta} = \sqrt{\frac{\omega\mu}{\sigma}}\;e^{j\pi/4},\\[4pt]
> \lambda = 2\pi\delta,\qquad v_p = \frac\omega\beta = \omega\delta .
> \end{gathered}
> $$
> Valid for $\sigma/\omega\epsilon\gg1$; $\delta$ is the **skin depth** ([[concepts/skin-depth]]). For $\tilde{\mathbf{E}} = \hat xE_0e^{-z/\delta}e^{-jz/\delta}$, $E_0$ real:
> $$
> \begin{gathered}
> \mathbf{E} = \hat x\,E_0e^{-z/\delta}\cos\Big(\omega t - \frac z\delta\Big),\\[4pt]
> \mathbf{H} = \hat y\,\frac{\sigma\delta E_0}{\sqrt2}\,e^{-z/\delta}\cos\Big(\omega t - \frac z\delta - \frac\pi4\Big),
> \end{gathered}
> $$
> and $\langle\mathbf{S}\rangle = \hat z\,\dfrac{\sigma\delta E_0^2}{4}\,e^{-2z/\delta}$.

Check: $\sqrt{\omega\mu/2\sigma} = \tfrac1\sigma\sqrt{\omega\mu\sigma/2} = 1/(\sigma\delta)$; the power is $\lvert E_0\rvert^2\cos\tau/(2\lvert\eta\rvert)$ with $\cos\tau = 1/\sqrt2$, $\lvert\eta\rvert = \sqrt2/(\sigma\delta)$.

<!-- fig:cond-good-conductor-fields -->

1. **Dead within a wavelength:** $e^{-2\pi}\approx1/535$, 54.6 dB, per wavelength.
2. **Slow and dispersive:** $v_p = \omega\delta = \sqrt{2\omega/\mu\sigma}\propto\sqrt f$. Seawater at 1 kHz: $5\times10^{4}$ m/s (Example 3), against $c/9 = 3.3\times10^{7}$ m/s if lossless. Copper at 1 MHz: $\lambda = 0.42$ mm, $v_p = 415$ m/s.
3. **H lags E by 45°**, an eighth of a period, and is large: $1/\lvert\eta\rvert$ is 22.5 (A/m) per (V/m) in seawater at 1 kHz, against $1/377$ in air. Electric over magnetic time-average energy density is $\epsilon\lvert\eta\rvert^2/\mu = 1/\sqrt{1+p^2}\approx\omega\epsilon/\sigma$, $1.1\times10^{-6}$ for seawater at 1 kHz (1 in a lossless medium): the stored energy is almost all magnetic.
4. **Perfect conductor as the limit:** $\delta\to0$, $\eta\to0$, no field inside; the $\delta$-thick current layer shrinks to a surface current carrying the jump in $\mathbf{H}$ ([[3-maxwell-and-waves/16-charge-conservation-displacement-current-and-maxwells-equations|Lecture 16]]).

> [!intuition] Why the good-conductor η looks like a resistance
> $\text{Re}\{\eta\} = 1/(\sigma\delta)$ is the edge-to-edge DC resistance of a square slab one skin depth thick ($R = l/(\sigma A)$, [[1-electrostatics/08-conductors-dielectrics-and-polarization|Lecture 8]], with $A = l\delta$): the induced current is a resistive sheet, absorbing $\tfrac12\text{Re}\{\eta\}\lvert\tilde H_0\rvert^2 = \lvert\tilde H_0\rvert^2/(2\sigma\delta)$ per area, its $\tfrac12RI^2$. It hugs the surface by [[2-magnetostatics/14-faradays-law-and-induced-emf|Lecture 14]]'s induction: eddy currents oppose the changing $\mathbf{B}$ (Lenz), each layer shielding those below.

> [!example] Example 2 (notes) — the same wave at 1 kHz in seawater
> Example 1 with $\omega = 2\pi\times10^{3}$ rad/s, $\sigma = 4$ S/m. The notes keep $\epsilon = 4\epsilon_0$ ($\sigma/\omega\epsilon = 1.8\times10^{7}$); seawater's $81\epsilon_0$ gives $8.9\times10^{5}$. Either way a **good conductor**, $\epsilon$ drops out:
> $$
> \begin{gathered}
> \tau = \frac\pi4,\\[4pt]
> \lvert\eta\rvert = \sqrt{\frac{\omega\mu_0}{\sigma}} = \sqrt{\frac{2\pi\times10^{3}\cdot4\pi\times10^{-7}}{4}}\\[4pt]
> = \frac{\pi\sqrt2}{100} = 0.0444\ \Omega,\\[4pt]
> \alpha = \sqrt{\pi f\mu_0\sigma} = \frac{\pi}{25} = 0.126\ \text{Np/m}.
> \end{gathered}
> $$
> $\tilde{\mathbf{H}} = -\hat x\,(2/\lvert\eta\rvert)\,e^{-j\pi/4}e^{-\alpha z}e^{-j\beta z}$: 45 A/m, 4,240 times Example 1's for the same 2 V/m. So
> $$
> \begin{gathered}
> \langle\mathbf{S}\rangle = \hat z\,\frac{2}{\lvert\eta\rvert}\cos\frac\pi4\,e^{-2\alpha z}\\[4pt]
> = \hat z\,\frac{100}{\pi}\,e^{-2\alpha z}\ \text{W/m}^2,
> \end{gathered}
> $$
> 31.8 W/m² at $z = 0$ (3,000 times Example 1's 10.6 mW/m²) and $31.8\times e^{-0.8\pi} = 31.8\times0.081 = 2.6$ W/m² at 10 m: 8 % left, 1.09 dB/m.

> [!example] Example 3 (notes) — the penetration depth of seawater at 1 kHz
> $\sigma = 4$ S/m, $\epsilon = 81\epsilon_0$, $\mu_0$, 1 kHz: $\sigma/\omega\epsilon = 72\times10^{9}/(81\times10^{3}) = 8.9\times10^{5}\gg1$, so
> $$
> \begin{gathered}
> \delta = \frac{1}{\sqrt{\pi\cdot10^{3}\cdot4\pi\times10^{-7}\cdot4}}\\[4pt]
> = \frac{1}{\sqrt{16\pi^2\times10^{-4}}} = \frac{100}{4\pi} = \frac{25}{\pi} = 7.96\ \text{m}.
> \end{gathered}
> $$
> In the water $\lambda = 2\pi\delta = 50$ m, $v_p = \lambda f = 5\times10^{4}$ m/s.

## 5. Why submarines are called at very low frequencies

The notes argue from Examples 1 and 2 for low frequencies, but those change the medium too: the 1 kHz seawater wave loses more over 10 m (92 %) than the 1 GHz Example 1 wave (85 %). Fix the medium. At 1 GHz seawater is in between ($\sigma/\omega\epsilon = 0.89$); Lecture 22's exact formula gives $\alpha = 77$ Np/m, 673 dB/m: 6,700 dB over 10 m, against 11 dB at 1 kHz. With $\alpha = \sqrt{\pi f\mu\sigma}$, each factor of 100 down in frequency divides the dB/m by 10.

Seawater ($\sigma = 4$ S/m, $\epsilon_r = 81$), exact formulas; the depth column assumes an illustrative 100 dB budget, $100/(8.686\,\alpha) = 11.5\,\delta$:

| $f$ | $\sigma/\omega\epsilon$ | $\delta$ | loss [dB/m] | depth for 100 dB | free-space $\lambda_0 = c/f$ |
|---|---|---|---|---|---|
| 76 Hz (ELF) | $1.2\times10^{7}$ | 28.9 m | 0.30 | 332 m | 3,900 km |
| 1 kHz (notes) | $8.9\times10^{5}$ | 7.96 m | 1.09 | 92 m | 300 km |
| 24 kHz (VLF) | $3.7\times10^{4}$ | 1.62 m | 5.3 | 19 m | 12.5 km |
| 1 MHz | 888 | 25 cm | 34.5 | 2.9 m | 300 m |
| 100 MHz | 8.9 | 2.7 cm | 326 | 31 cm | 3 m |
| 1 GHz | 0.89 | 1.3 cm | 673 | 15 cm | 30 cm |

At 100 MHz the good-conductor formula gives 2.5 cm, 5 % short ($\sigma/\omega\epsilon<10$); at 1 GHz it is badly wrong.

<!-- fig:cond-skin-depth -->

The price (the notes) is **bandwidth**: a carrier at $f$ carries only a small fraction of $f$, so deep links are slow. VLF (3–30 kHz) reaches a few tens of metres at roughly 300 bit/s; ELF (US Navy 76 Hz, shut down in 2004; Russia 82 Hz) reaches hundreds of metres at a few characters per minute (Wikipedia, "Communication with submarines"; cf. the table's 19 m and 330 m). The second price is the **antenna**: against free-space wavelengths of 3,900 km and 12.5 km, any buildable antenna is a tiny fraction of $\lambda_0$ and radiates poorly, so transmitters need tens of kilometres of wire and very large power, and the link is one-way (no submarine can carry such an antenna to reply). (Rao: in the water $\lambda = 2\pi\delta$, 50 m at 1 kHz, so immersed antennas can be short.)

## 6. Skin depth in metals

Metals are good conductors at every course frequency (§1). With $\mu_0$, $\delta = 0.0661/\sqrt f$ m for copper (Rao's figure), $0.0851/\sqrt f$ m for aluminium; panel 1 of the §5 figure plots both.

| $f$ | copper, $\sigma = 5.8\times10^{7}$ S/m | aluminium, $\sigma = 3.5\times10^{7}$ S/m | copper $\lvert\eta\rvert$ |
|---|---|---|---|
| 60 Hz | 8.53 mm | 11.0 mm | 2.86 µΩ |
| 1 kHz | 2.09 mm | 2.69 mm | 11.7 µΩ |
| 1 MHz | 66.1 µm | 85.1 µm | 0.369 mΩ |
| 100 MHz | 6.61 µm | 8.51 µm | 3.69 mΩ |
| 1 GHz | 2.09 µm | 2.69 µm | 11.7 mΩ |
| 10 GHz | 0.661 µm | 0.851 µm | 36.9 mΩ |

Rao Table 5.1 conductivities (5.8×10⁷ S/m: the international annealed-copper standard); $\lvert\eta\rvert = \sqrt{\omega\mu_0/\sigma} = 3.69\times10^{-7}\sqrt f\ \Omega$ (Rao, copper). Aluminium's $\delta$ is $\sqrt{5.8/3.5} = 1.29$ times copper's.

- **Skin effect in wires.** Current crowds into a layer about $\delta$ thick: a wire of radius $a\gg\delta$ acts as a tube of wall $\delta$, resistance up by about $a/2\delta$ (7.6 for 1 mm radius copper at 1 MHz). At 60 Hz, $\delta = 8.5$ mm exceeds house wiring, which conducts throughout.
- **Shielding.** Absorption through thickness $d$: $e^{-d/\delta}$, $8.686\,d/\delta$ dB, plus reflection (Lecture 25). 1 mm of aluminium is $0.09\,\delta$ at 60 Hz (nearly transparent to absorption) but $11.8\,\delta$ (102 dB) at 1 MHz: power-frequency magnetic fields are hard to shield, radio easy. At a microwave oven's 2.45 GHz, aluminium's $\delta = 1.7$ µm, so a sub-millimetre wall is hundreds of skin depths.
- **Tiny $\lvert\eta\rvert$.** Copper's 11.7 mΩ at 1 GHz, $3\times10^{-5}$ of $\eta_0$, is a near short: almost total reflection (Lecture 25).

> [!trap] "Copper is a good conductor at all frequencies"
> Constant $\sigma$ puts copper's $\sigma/\omega\epsilon_0 = 1$ at $f_c = 1.0\times10^{18}$ Hz (X-rays), but $\sigma/\omega\epsilon\to0$ as $\omega\to\infty$, so every medium ends up a dielectric. The model fails earlier still: the Drude $\sigma_{\text{DC}}/(1 + j\omega/\nu)$ of [[1-electrostatics/11-lorentz-drude-models-for-conductivity-and-susceptibility|Lecture 11]] ($\nu\approx4\times10^{13}$ s⁻¹ for copper) changes in the infrared, and X-rays pass through thin foil. Safe: good at every radio and microwave frequency.

## 7. Reading a lossy-medium problem

> [!recipe] Damped plane waves, start to finish
> 1. **Classify:** $p = \sigma/\omega\epsilon$, own $\epsilon$, stated $\omega$. Below 0.1, imperfect-dielectric row; above 10, good-conductor row; between, Lecture 22's exact formulas or §2's polar forms.
> 2. **Constants:** $\alpha$, $\beta$, $\lvert\eta\rvert$, $\tau$; $\delta = 1/\alpha$, $\lambda = 2\pi/\beta$, $v_p = \omega/\beta$. In a good conductor all follow from $\delta$ (§4).
> 3. **Fields:** $\tilde{\mathbf{H}} = \hat u\times\tilde{\mathbf{E}}/\eta$ ($-\tau$ in the phase), $\mathbf{E}\times\mathbf{H}$ checked along $\hat u$; time domain $\lvert E_0\rvert e^{-\alpha d}\cos(\omega t - \beta d + \angle E_0)$, $d$ the distance travelled.
> 4. **Power:** $\langle\mathbf{S}\rangle = \hat u\,\lvert E_0\rvert^2\cos\tau\,e^{-2\alpha d}/(2\lvert\eta\rvert)$; between depths $e^{-2\alpha\,\Delta d}$, or $8.686\,\alpha\,\Delta d$ dB.
> 5. **Inverse** (given $\lambda$ and $\delta$, or a field): $\beta = 2\pi/\lambda$, $\alpha = 1/\delta$; $\alpha/\beta = \tan\tau$ (regime), $\tan2\tau = \sigma/\omega\epsilon$; $\gamma\eta = j\omega\mu$, $\gamma/\eta = \sigma + j\omega\epsilon$ (material).

> [!trap] Where damped-wave problems lose points
> - Power decays as $e^{-2\alpha d}$: after one $\delta$, field 37 %, power 14 %.
> - Distance travelled, not coordinate: toward $-z$, $z = -10$ m means 10 m gone, $e^{-2\alpha\cdot10}$.
> - $\cos\tau$ in $\langle\mathbf{S}\rangle$ is $1/\sqrt2$ in a good conductor, not 1.
> - Good-conductor $\lvert\eta\rvert = \sqrt{\omega\mu/\sigma}$, not $\sqrt{\mu/\epsilon}$: milliohms or less for metals.
> - Np/m × 8.686 = dB/m; $\beta$ is in rad/m.
> - $\delta = 1/\sqrt{\pi f\mu\sigma}$ uses $f$, $\sqrt{2/\omega\mu\sigma}$ uses $\omega$: mixing errs by $\sqrt{2\pi}$.
> - An imperfect dielectric's penetration depth, $(2/\sigma)\sqrt{\epsilon/\mu}$, is frequency independent: not the skin-depth formula.

## 8. Connections

Earlier lectures (8, 10, 11, 14, 16, 20–22) are linked where used. **Lecture 25 (ahead):** a good conductor's tiny $\eta$ makes it a near-perfect reflector; SP17 Exam 3 #2(iv) asks for the reflection coefficient from a medium with $\sigma = 400\,\omega\epsilon_0$, $\epsilon = 4\epsilon_0$: decide its regime first.

## 9. Summary

$p = \sigma/\omega\epsilon$: below 0.1 imperfect dielectric, above 10 good conductor; $f_c = 1/(2\pi\tau_r)$. Exactly $\alpha/\beta = \tan\tau\le1$ and $\alpha = \sigma\lvert\eta\rvert/(2\cos\tau)$. Good conductor: $\alpha = \beta = 1/\delta$, $\eta = (1+j)/(\sigma\delta)$. Power $\propto e^{-2\alpha d}$. Numbers: tables in §§1, 5, 6.

Concept pages: [[concepts/loss-tangent]] · [[concepts/skin-depth]] · [[concepts/propagation-constant]] · [[concepts/intrinsic-impedance]] · [[concepts/poynting-vector]] · [[concepts/poynting-theorem]] · [[concepts/phasors]] · [[concepts/conductivity-and-susceptibility-models]] · [[concepts/conductors]].

> [!exam] On exams
> On every third-exam paper on hand; SP17–SP19 print the notes' regime table, so they test recognizing the regime.
> 1. **Classify, then compute** (Summer 2018, 2019 HE3 #3b): toward $-z$ in $\epsilon = 81\epsilon_0$, $\sigma = 4$ S/m, 1 kHz; regime, calculator-free $\delta$, $\lambda$, $v_p$, power 10 m in. §7, good-conductor row; traps $e^{-2\alpha d}$, the sign of $z$. Same steps: [[problems/a-radio-wave-into-moist-ground|A radio wave into moist ground]]. The 2019 conflict paper's 10 GHz version: solve §1's regime condition for $\omega$.
> 2. **From measured $\lambda$ and $\delta$** (Summer 2017 HE3 #2b): regime, $v$, $\epsilon_r$, $\lvert\eta\rvert$, $\sigma$ (§2 example).
> 3. **"Possible or not possible"** (Summer 2020 HE3 #3: "dry earth", $\sigma = 10^{-3}$ S/m, $\epsilon = \epsilon_0$, 100 Hz): $\alpha$ against $\beta$, $\lambda$ against $2\pi\delta$. Use $\alpha/\beta\le1$ and this medium's own $f_c$ (not the §1 table's dry earth).
> 4. **Good-conductor concepts** (SP17 #1a, #2(i); SP18 #1(i)): $\alpha$ vs $\beta$, 45° phase, decay within a wavelength, dispersive $v_p$, constant or decaying power flow, "good at all frequencies" (§§4, 6). Also the loss tangent's meaning (FA23 #1(b)); a five-way scale (SP19 #1e).
> 5. **Power against depth in water** (FA23 #6): e.g. $e^{-0.2z}e^{-j0.2z}$ ($\alpha = \beta$: good conductor); $\langle S\rangle$ against depth, $2\alpha$ per metre, $8.686\,\alpha$ dB/m.
>
> With $\epsilon_0\approx10^{-9}/36\pi$ F/m: $\sigma/\omega\epsilon = 18\times10^{9}\,\sigma/(f\epsilon_r)$ and $\pi f\mu_0\sigma = 4\pi^2\times10^{-7}f\sigma$, so a calculator-free $\delta$ needs $f\sigma\times10^{-7}$ to be a perfect square ($f\sigma = 4\times10^{3}$ for seawater).

> [!tip] Practice this lecture
> [[practice/23-imperfect-dielectrics-and-good-conductors|12 practice problems]] — 5 easy, 3 medium, 4 hard — each with a folded hint and a worked solution. Start with [[practice/23-imperfect-dielectrics-and-good-conductors#231-six-media-at-one-frequency|23.1 Six media at one frequency]]; the [[practice/index|practice hub]] has the whole bank by difficulty and by topic.

### Sources for this page
Kudeki notes, Lecture 23 (6 pp.): the regime table; Examples 1–3 (paraphrased, script-checked); the heating, microwave-oven and communication remarks; the low-frequency argument and its bandwidth cost. No slides were available. Rao (2009) §§5.3–5.4, Tables 5.1–5.3: "loss tangent", crossover and thresholds, copper figures, 54.6 dB per wavelength, the antenna remark, Problem 5.26, material values. ITU-R P.527-6: loam conductivity, water permittivity. Wikipedia, "Communication with submarines": VLF/ELF data. This site's own: polar forms and accuracy figures, the energy balance, the media, seawater and metal tables, the fair 1 GHz comparison, the inverse example, recipe, traps, figures. Slips in the course material: see [[0-toolkit/04-errata-in-the-course-materials|errata]].
