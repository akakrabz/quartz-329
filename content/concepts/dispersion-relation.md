---
title: "Dispersion relation and phase velocity"
description: "The ω–β relation a wave's physics imposes; it sets vₚ = ω/β = λf."
tags: [concept, waves]
aliases: ["phase velocity", "wave-number", "wavenumber", "plasma frequency", "dispersive medium"]
---

> [!key] Definition
> For $A\cos(\omega t\mp\beta z)$, the **dispersion relation** links $\omega$ [rad/s] and the wave-number $\beta$ [rad/m] as the governing equations demand. It fixes
> $$
> \begin{gathered}
> \lambda = \frac{2\pi}{\beta},\qquad T = \frac{2\pi}{\omega} = \frac1f,\\[4pt]
> v_p = \frac{\omega}{\beta} = \frac\lambda T = \lambda f,\qquad v_g = \frac{d\omega}{d\beta}.
> \end{gathered}
> $$
> The notes' three examples:
> | wave | dispersion relation | $v_p$ |
> |---|---|---|
> | TEM, perfect dielectric | $\beta = \omega\sqrt{\mu\epsilon}$ | $1/\sqrt{\mu\epsilon}$ |
> | sound, monatomic gas | $\beta = \omega\sqrt{m/(\tfrac53k_BT)}$ | $\sqrt{5k_BT/3m}$ |
> | TEM, collisionless plasma | $\beta = \tfrac1c\sqrt{\omega^2 - \omega_p^2}$ | $c/\sqrt{1 - \omega_p^2/\omega^2}$ |
>
> with $\omega_p = \sqrt{Ne^2/(m\epsilon_0)}$ ($N$ electrons per m³ of mass $m$; $f_p\approx8.98\sqrt N$ Hz). $v_p$ the same at every $\omega$: **non-dispersive**; otherwise **dispersive**.

**Physics.** Light in a dielectric: a straight line through the origin, one speed for all, so pulses keep their shape (Lecture 18). Sound in an ideal gas: also straight, adiabatic index $\gamma = \tfrac53$ (monatomic). Plasma: collisionless free electrons carry a current a quarter period behind $\mathbf{E}$, lowering the permittivity to $\epsilon_0(1 - \omega_p^2/\omega^2)$ and bending the line into $\omega^2 = \omega_p^2 + c^2\beta^2$. On an $\omega$–$\beta$ diagram $v_p$ is the chord slope, $v_g$ the tangent slope; in the plasma $v_p>c$, $v_g<c$, $v_pv_g = c^2$. A pure cosine carries no message; signals and energy go at $v_g$. Below $\omega_p$ there is no real $\beta$: the plasma turns the wave back.

**Examples.**
- 200 MHz, non-magnetic, $\epsilon_r = 4$: $\beta = 2\pi f\sqrt{\epsilon_r}/c = 8\pi/3\approx8.38$ rad/m, $\lambda = 0.75$ m, $v_p = 1.5\times10^8$ m/s.
- Sound at 300 K: helium 1019 m/s, argon 323 m/s ($\propto1/\sqrt m$); at 20 °C, 1007 and 319 m/s (handbook values). Air (diatomic, $\gamma = \tfrac75$): 343 m/s at 20 °C ($\tfrac53$ would give 375). 440 Hz: $\lambda = 2.32$ m in helium, 0.73 m in argon.
- Ionosphere, $N\sim10^{12}$ m⁻³: $f_p\approx9$ MHz. At 10 MHz $\lambda = 68.1$ m (30.0 m in vacuum), $v_p = 2.27c$, $v_g = 0.44c$; at 100 MHz $v_p = 1.004c$. Below 9 MHz a vertical wave is turned back.
- $\cos(4\pi\times10^8t - \tfrac{8\pi}{3}y)$: $\omega/\beta = 1.5\times10^8$ m/s, so $\mu_r\epsilon_r = (c/v_p)^2 = 4$.

> [!trap]
> - $v_p = \omega/\beta$ is the crest speed. The notes' "propagation velocity" is the signal speed only without dispersion.
> - $v_p>c$ in a plasma breaks no law; $v_g<c$ does the carrying.
> - Below $\omega_p$: no travelling wave, not a slow one.
> - A measured $v_p$ gives $\mu_r\epsilon_r$; "non-magnetic" (or $\eta$) splits it.
> - Acoustic $T$ is a temperature; $\tfrac53$ is for monatomic gases only.

**Where it appears.** [[3-maxwell-and-waves/18-the-wave-equation-and-plane-tem-waves|Lecture 18]]; [[3-maxwell-and-waves/19-dalembert-solutions-and-radiation-from-current-sheets|Lecture 19]] ($\beta$, $\lambda$, $v_p$ from a phase); [[3-maxwell-and-waves/21-monochromatic-waves-and-phasor-notation|Lecture 21]] (defined); [[1-electrostatics/11-lorentz-drude-models-for-conductivity-and-susceptibility|Lecture 11]] (Drude and Lorentz responses); [[3-maxwell-and-waves/22-phasor-maxwell-equations-and-damped-waves|Lecture 22]] ($v_p$ varies with $f$ in conductors); [[3-maxwell-and-waves/24-signal-transmission-and-circular-polarization|Lecture 24]] ([[concepts/group-velocity|group velocity]]).

**Practice.** [[practice/topics#monochromatic-waves-phasors-and-dispersion|Monochromatic waves, phasors and dispersion]] (22 problems) — for example [[practice/21-phasors-and-monochromatic-waves#211-reading-two-waves|21.1 Reading two waves]] (easy), [[practice/21-phasors-and-monochromatic-waves#216-radio-waves-in-a-plasma|21.6 Radio waves in a plasma]] (medium), [[practice/21-phasors-and-monochromatic-waves#219-a-phasor-from-two-snapshots|21.9 A phasor from two snapshots]] (hard).

Related: [[concepts/phasors]] · [[concepts/plane-waves]] · [[concepts/wave-equation]] · [[concepts/intrinsic-impedance]] · [[concepts/conductivity-and-susceptibility-models]] · [[concepts/permittivity]].
