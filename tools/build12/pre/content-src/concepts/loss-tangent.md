---
title: "Loss tangent"
description: "σ/ωε, conduction over displacement current: below about 0.1 an imperfect dielectric, above about 10 a good conductor."
tags: [concept, waves]
aliases: ["σ/ωε", "sigma over omega epsilon", "loss angle", "tan delta", "dissipation factor", "crossover frequency"]
---

> [!key] Definition
> $$
> \tan\theta\equiv\frac{\sigma}{\omega\epsilon} = \frac{\lvert\sigma\tilde{\mathbf{E}}\rvert}{\lvert j\omega\epsilon\tilde{\mathbf{E}}\rvert}\qquad(\text{dimensionless}),
> $$
> conduction over displacement current density at $\omega = 2\pi f$, with the medium's $\epsilon$. **Loss angle** $\theta$: the lead of the displacement current $j\omega\epsilon\tilde{\mathbf{E}}$ over the total $(\sigma + j\omega\epsilon)\tilde{\mathbf{E}}$.
> - $\ll1$ (below 0.1): **imperfect dielectric**.
> - $\gg1$ (above 10): **good conductor**.
> - $= 1$ at the **crossover frequency** $f_c = \sigma/2\pi\epsilon$.

**Physics.** With $\tilde{\mathbf{E}}$ real, $\sigma\tilde{\mathbf{E}}$ is in phase and $j\omega\epsilon\tilde{\mathbf{E}}$ 90° ahead; the total sits at $90^\circ - \theta$. Only the in-phase part dissipates, $\langle\mathbf{J}\cdot\mathbf{E}\rangle = \tfrac12\sigma\lvert\tilde{\mathbf{E}}\rvert^2$; per radian, against the peak stored $\tfrac12\epsilon\lvert\tilde{\mathbf{E}}\rvert^2$, the loss is $\sigma/\omega\epsilon$: $1/Q$ of the medium-filled leaky capacitor of [[1-electrostatics/10-capacitance-and-conductance#6-conductance-the-leaky-capacitor|Lecture 10]] ($C$ parallel to $G = (\sigma/\epsilon)C$, $G/\omega C = \sigma/\omega\epsilon$). With $\tau_r = \epsilon/\sigma$ ([[1-electrostatics/08-conductors-dielectrics-and-polarization|Lecture 8]]), $\sigma/\omega\epsilon = 1/(\omega\tau_r)$: a medium conducts when its charges rearrange many times per period.

For a plane wave, with $p = \sigma/\omega\epsilon$ and $\theta = \tan^{-1}p$, the exact results of [[3-maxwell-and-waves/22-phasor-maxwell-equations-and-damped-waves|Lecture 22]] become

$$
\begin{gathered}
\tau = \angle\eta = \frac\theta2,\qquad \frac\alpha\beta = \tan\frac\theta2,\\[4pt]
\lvert\eta\rvert = \sqrt{\frac\mu\epsilon}\,(1+p^2)^{-1/4},\\[4pt]
\lvert\gamma\rvert = \omega\sqrt{\mu\epsilon}\,(1+p^2)^{1/4}.
\end{gathered}
$$

So $\angle\eta$ lies in 0–45° and $\alpha\le\beta$. Small $p$: $\alpha\approx\tfrac12\beta p = (\sigma/2)\sqrt{\mu/\epsilon}$; large $p$: $\alpha\approx\beta\approx\sqrt{\pi f\mu\sigma}$ ([[3-maxwell-and-waves/23-imperfect-dielectrics-and-good-conductors|Lecture 23]]).

**Real dielectrics.** A lagging polarization (the damped Lorentz oscillator of [[1-electrostatics/11-lorentz-drude-models-for-conductivity-and-susceptibility|Lecture 11]], or sluggish rotating molecules) makes $\epsilon = \epsilon' - j\epsilon''$, dissipating like a conductivity $\omega\epsilon''$. Datasheets lump both as **tan δ** $= (\sigma + \omega\epsilon'')/\omega\epsilon'$. For good insulators it varies slowly with $f$; $\sigma/\omega\epsilon$ falls as $1/f$.

**Examples** (σ and ε from Rao Tables 5.1–5.2 and the notes).
- Seawater (4 S/m, $\epsilon_r = 81$): $8.9\times10^{5}$ at 1 kHz, 888 at 1 MHz, 0.89 at 1 GHz, 0.089 at 10 GHz; $f_c = 0.89$ GHz, $\tau_r = 0.18$ ns.
- Notes' Example 1 ($10^{-3}$ S/m, $\epsilon_r = 4$), 1 GHz: $4.5\times10^{-3}$, $\angle\eta = 0.13^\circ$.
- Fresh water ($10^{-3}$ S/m, $\epsilon_r = 80$), 1 MHz: 0.22, in between; $f_c = 225$ kHz.
- Copper, 1 GHz: $1.0\times10^{9}$; formal $f_c = 10^{18}$ Hz.
- No calculator ($\epsilon_0\approx10^{-9}/36\pi$): $\sigma/\omega\epsilon = 18\times10^{9}\,\sigma/(f\epsilon_r)$. A past exam's dry earth ($10^{-3}$ S/m, $\epsilon_0$): $1.8\times10^{4}$ at 1 kHz, $f_c = 18$ MHz.

> [!trap]
> - The medium's $\epsilon$, not $\epsilon_0$ (water: ×80).
> - $\omega$, not $f$: $\sigma/(2\pi f\epsilon)$.
> - A medium *at a frequency*: seawater conducts at 1 kHz, not at 10 GHz.
> - $\angle\eta$ is *half* the loss angle; small $p$: $\sigma/2\omega\epsilon$.
> - The δ in tan δ is an angle, not a skin depth.

**Where it appears.** Lecture 23 (§1 classifying media, crossover table, regime map; §2 exact forms); Lecture 22 ($\sigma + j\omega\epsilon$ in $\gamma$, $\eta$); [[1-electrostatics/10-capacitance-and-conductance|Lecture 10]]; Lecture 8; [[problems/a-radio-wave-into-moist-ground]] (180, then 1.8). Exams: SP19 Exam 3 #1d (find it), FA23 Exam 3 #1(b) (what it represents).

**Practice.** [[practice/topics#imperfect-dielectrics-good-conductors-and-skin-depth|Imperfect dielectrics, good conductors and skin depth]] (18 problems) — for example [[practice/23-imperfect-dielectrics-and-good-conductors#231-six-media-at-one-frequency|23.1 Six media at one frequency]] (easy), [[practice/23-imperfect-dielectrics-and-good-conductors#236-wavelength-and-depth-measured-underground|23.6 Wavelength and depth measured underground]] (medium), [[practice/23-imperfect-dielectrics-and-good-conductors#239-down-into-a-deep-lake|23.9 Down into a deep lake]] (hard).

Related: [[concepts/skin-depth]] · [[concepts/propagation-constant]] · [[concepts/intrinsic-impedance]] · [[concepts/conductors]] · [[concepts/conductance]] · [[concepts/permittivity]] · [[concepts/conductivity-and-susceptibility-models]].
