---
title: "Loss tangent"
description: "σ/ωε compares the conduction current with the displacement current that a field of angular frequency ω drives in a medium. It is the tangent of the angle by which the displacement current leads the total current. Below about 0.1 the medium is an imperfect dielectric and above about 10 a good conductor; it equals 1 at the crossover frequency σ/2πε, and it fixes the phase of η exactly, ∠η = ½ tan⁻¹(σ/ωε)."
tags: [concept, waves]
aliases: ["σ/ωε", "sigma over omega epsilon", "loss angle", "tan delta", "dissipation factor", "crossover frequency"]
---

> [!key] Definition
> $$
> \tan\theta\equiv\frac{\sigma}{\omega\epsilon} = \frac{\lvert\sigma\tilde{\mathbf{E}}\rvert}{\lvert j\omega\epsilon\tilde{\mathbf{E}}\rvert}\qquad(\text{dimensionless}),
> $$
> the ratio of the conduction current density to the displacement current density at angular frequency $\omega = 2\pi f$, with the medium's own $\epsilon$. The **loss angle** $\theta$ is the angle by which the displacement current $j\omega\epsilon\tilde{\mathbf{E}}$ leads the total current $(\sigma + j\omega\epsilon)\tilde{\mathbf{E}}$.
> - $\sigma/\omega\epsilon\ll1$ (in practice below 0.1): **imperfect dielectric**.
> - $\sigma/\omega\epsilon\gg1$ (in practice above 10): **good conductor**.
> - $\sigma/\omega\epsilon = 1$ at the **crossover frequency** $f_c = \sigma/2\pi\epsilon$.

**Physics.** Draw the phasors with $\tilde{\mathbf{E}}$ along the real axis. The conduction current $\sigma\tilde{\mathbf{E}}$ lies along it, in phase with the field. The displacement current $j\omega\epsilon\tilde{\mathbf{E}}$ points straight up, 90° ahead. Their sum, the total current, sits at $90^\circ - \theta$ from $\tilde{\mathbf{E}}$, with $\tan\theta = \sigma/\omega\epsilon$. So the displacement current leads the total current by $\theta$, and the ratio of the two currents is $\tan\theta$: two descriptions of one number. Only the in-phase part dissipates. The Joule heating is $\langle\mathbf{J}\cdot\mathbf{E}\rangle = \tfrac12\sigma\lvert\tilde{\mathbf{E}}\rvert^2$, while the displacement current only stores energy and returns it. Measured against the peak stored electric energy density $\tfrac12\epsilon\lvert\tilde{\mathbf{E}}\rvert^2$, the loss per radian of a cycle is $\sigma/\omega\epsilon$, so the loss tangent is $1/Q$ of a capacitor filled with the medium. That capacitor is the leaky capacitor of [[1-electrostatics/10-capacitance-and-conductance#6-conductance-the-leaky-capacitor|Lecture 10]], a $C$ in parallel with $G = (\sigma/\epsilon)C$, whose current ratio is $G/\omega C = \sigma/\omega\epsilon$. The relaxation time $\tau_r = \epsilon/\sigma$ of [[1-electrostatics/08-conductors-dielectrics-and-polarization|Lecture 8]] gives a third reading: $\sigma/\omega\epsilon = 1/(\omega\tau_r)$. A medium conducts when its charges can rearrange many times within one period of the field.

For a plane wave the loss tangent controls everything that $\sigma$ changes. With $p = \sigma/\omega\epsilon$ and $\theta = \tan^{-1}p$, the exact results of [[3-maxwell-and-waves/22-phasor-maxwell-equations-and-damped-waves|Lecture 22]] become

$$
\begin{gathered}
\tau = \angle\eta = \frac\theta2,\qquad \frac\alpha\beta = \tan\frac\theta2,\\[4pt]
\lvert\eta\rvert = \sqrt{\frac\mu\epsilon}\,(1+p^2)^{-1/4},\\[4pt]
\lvert\gamma\rvert = \omega\sqrt{\mu\epsilon}\,(1+p^2)^{1/4}.
\end{gathered}
$$

So $\eta$'s phase lies between 0 and 45°, and $\alpha\le\beta$ always. For small $p$, $\alpha\approx\tfrac12\beta p = (\sigma/2)\sqrt{\mu/\epsilon}$; for large $p$, $\alpha\approx\beta\approx\sqrt{\pi f\mu\sigma}$. ([[3-maxwell-and-waves/23-imperfect-dielectrics-and-good-conductors|Lecture 23]] has the derivation and the table.)

**Real dielectrics.** $\sigma$ is not the only way to lose energy. A polarization that lags the field, from the damped Lorentz oscillator of [[1-electrostatics/11-lorentz-drude-models-for-conductivity-and-susceptibility|Lecture 11]] or from molecules that rotate sluggishly, makes the permittivity complex, $\epsilon = \epsilon' - j\epsilon''$. It then dissipates exactly as a conductivity $\omega\epsilon''$ would. Datasheets lump both mechanisms into one loss tangent, $(\sigma + \omega\epsilon'')/\omega\epsilon'$, and write it **tan δ**. That δ is an angle and has nothing to do with the skin depth $\delta$. For good insulators this tan δ often changes only slowly with frequency, unlike $\sigma/\omega\epsilon$, which falls as $1/f$.

**Examples** (σ and ε from Rao Tables 5.1–5.2 and the notes).
- Seawater ($\sigma = 4$ S/m, $\epsilon_r = 81$): $8.9\times10^{5}$ at 1 kHz, 888 at 1 MHz, 0.89 at 1 GHz, 0.089 at 10 GHz. Its crossover is $f_c = 0.89$ GHz, with $\tau_r = 0.18$ ns.
- The notes' Example 1 medium ($\sigma = 10^{-3}$ S/m, $\epsilon_r = 4$) at 1 GHz: $4.5\times10^{-3}$, an imperfect dielectric with $\angle\eta = 0.13^\circ$.
- Fresh water ($\sigma = 10^{-3}$ S/m, $\epsilon_r = 80$) at 1 MHz: 0.22, in between. Its crossover is 225 kHz.
- Copper at 1 GHz: $1.0\times10^{9}$. Its formal crossover is $10^{18}$ Hz.
- Without a calculator ($\epsilon_0\approx10^{-9}/36\pi$): $\sigma/\omega\epsilon = 18\times10^{9}\,\sigma/(f\epsilon_r)$. The "dry earth" of a past exam ($\sigma = 10^{-3}$ S/m, $\epsilon = \epsilon_0$) gives $1.8\times10^{4}$ at 1 kHz, and its crossover is 18 MHz.

> [!trap]
> - Use the medium's $\epsilon$, not $\epsilon_0$; for water that is a factor of about 80.
> - $\omega$, not $f$: the ratio is $\sigma/(2\pi f\epsilon)$.
> - The loss tangent belongs to a medium *at a frequency*. "Seawater is a conductor" is true at 1 kHz and false at 10 GHz.
> - The phase of $\eta$ is half the loss angle, $\tfrac12\tan^{-1}(\sigma/\omega\epsilon)$, not the full angle. Its small-$p$ form is $\sigma/2\omega\epsilon$.
> - Datasheet tan δ is a loss tangent; the δ in it is not a skin depth.

**Where it appears.** [[3-maxwell-and-waves/23-imperfect-dielectrics-and-good-conductors|Lecture 23]] (§1: classifying media, the crossover table and regime map; §2: the exact forms); [[3-maxwell-and-waves/22-phasor-maxwell-equations-and-damped-waves|Lecture 22]] ($\sigma + j\omega\epsilon$ in $\gamma$ and $\eta$); [[1-electrostatics/10-capacitance-and-conductance|Lecture 10]] (the leaky capacitor's $G/\omega C$); [[1-electrostatics/08-conductors-dielectrics-and-polarization|Lecture 8]] (the relaxation time); [[problems/a-radio-wave-into-moist-ground]] ($\sigma/\omega\epsilon = 180$, then 1.8). On exams: SP19 Exam 3 #1d asks for the loss tangent of a given wave, and FA23 Exam 3 #1(b) asks what it represents.

**Practice.** [[practice/topics#imperfect-dielectrics-good-conductors-and-skin-depth|Imperfect dielectrics, good conductors and skin depth]] (16 problems) — for example [[practice/23-imperfect-dielectrics-and-good-conductors#231-six-media-at-one-frequency|23.1 Six media at one frequency]] (easy), [[practice/23-imperfect-dielectrics-and-good-conductors#236-wavelength-and-depth-measured-underground|23.6 Wavelength and depth measured underground]] (medium), [[practice/23-imperfect-dielectrics-and-good-conductors#239-down-into-a-deep-lake|23.9 Down into a deep lake]] (hard).

Related: [[concepts/skin-depth]] · [[concepts/propagation-constant]] · [[concepts/intrinsic-impedance]] · [[concepts/conductors]] · [[concepts/conductance]] · [[concepts/permittivity]] · [[concepts/conductivity-and-susceptibility-models]].
