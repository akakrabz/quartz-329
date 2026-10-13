---
title: "Dispersion relation and phase velocity"
description: "A monochromatic wave A cos(ωt ∓ βz) can only exist if ω and β satisfy the dispersion relation that the physics of that wave imposes. It sets the phase velocity vₚ = ω/β = λf. Light in a dielectric (β = ω√(με)) and sound in a gas are non-dispersive; radio waves in a collisionless plasma, β = √(ω² − ω_p²)/c, are dispersive, with vₚ > c, a group velocity dω/dβ < c, and no travelling wave below the plasma frequency."
tags: [concept, waves]
aliases: ["phase velocity", "wave-number", "wavenumber", "plasma frequency", "group velocity", "dispersive medium"]
---

> [!key] Definition
> For a monochromatic wave $A\cos(\omega t\mp\beta z)$, the **dispersion relation** is the relation between the frequency $\omega$ [rad/s] and the wave-number $\beta$ [rad/m] that the governing equations impose. It fixes
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
> with $\omega_p = \sqrt{Ne^2/(m\epsilon_0)}$ for $N$ electrons per m³ of mass $m$ ($f_p\approx8.98\sqrt N$ Hz). If $v_p$ is the same at every $\omega$ the medium is **non-dispersive**; otherwise it is **dispersive**.

**Physics.** Every linear, uniform medium admits monochromatic waves of the same form, $A\cos(\omega t\mp\beta z)$; the physics of the wave decides which $(\omega, \beta)$ pairs are allowed. For light in a dielectric the pairs lie on a straight line through the origin, so every frequency moves at the same speed and a pulse built from many frequencies keeps its shape (Lecture 18). Sound in an ideal gas is also a straight line, with the adiabatic index $\gamma = \tfrac53$ for a monatomic gas. A plasma is different: its free electrons, driven by the wave and with no collisions to slow them, carry a current a quarter period behind $\mathbf{E}$. That current lowers the effective permittivity to $\epsilon_0(1 - \omega_p^2/\omega^2)$, which bends the line into the hyperbola $\omega^2 = \omega_p^2 + c^2\beta^2$. On an $\omega$–$\beta$ diagram, $v_p$ is the slope of the chord from the origin and $v_g$ the slope of the tangent. For the plasma the chord is steeper than the light line ($v_p>c$) and the tangent less steep ($v_g<c$), with $v_pv_g = c^2$. Crests can outrun light because a pure cosine carries no message; signals and energy travel at $v_g$. Below $\omega_p$ there is no real $\beta$ and no travelling wave: the plasma turns the wave back.

**Examples.**
- 200 MHz in a non-magnetic dielectric with $\epsilon_r = 4$: $\beta = 2\pi f\sqrt{\epsilon_r}/c = 8\pi/3\approx8.38$ rad/m, $\lambda = 0.75$ m, $v_p = 1.5\times10^8$ m/s.
- Sound at 300 K: helium 1019 m/s, argon 323 m/s ($\propto1/\sqrt m$). At 20 °C the formula gives 1007 and 319 m/s, the handbook values. Air, mostly diatomic, needs $\gamma = \tfrac75$: 343 m/s at 20 °C (the $\tfrac53$ formula would give 375 m/s). A 440 Hz tone has $\lambda = 2.32$ m in helium and 0.73 m in argon.
- The ionosphere, $N\sim10^{12}$ m⁻³: $f_p\approx9$ MHz. At 10 MHz, $\lambda = 68.1$ m (30.0 m in vacuum), $v_p = 2.27c$ and $v_g = 0.44c$; at 100 MHz, $v_p = 1.004c$. Below 9 MHz a wave sent straight up is turned back.
- Reading an expression: $\cos(4\pi\times10^8t - \tfrac{8\pi}{3}y)$ has $\omega/\beta = 1.5\times10^8$ m/s, so $\mu_r\epsilon_r = (c/v_p)^2 = 4$.

> [!trap]
> - $v_p = \omega/\beta$ is the speed of the crests. The notes call it "the propagation velocity", which is the speed of signals only in a non-dispersive medium.
> - $v_p>c$ in a plasma does not violate relativity; $v_g<c$ does the carrying.
> - Below $\omega_p$ the plasma has no travelling wave, not a slow one.
> - A measured $v_p$ gives $\mu_r\epsilon_r$, not $\epsilon_r$; you need "non-magnetic" (or $\eta$) to split it.
> - In the acoustic formula $T$ is a temperature, not the period, and $\tfrac53$ applies to monatomic gases only.

**Where it appears.** [[3-maxwell-and-waves/18-the-wave-equation-and-plane-tem-waves|Lecture 18]] (every frequency at the same $v$); [[3-maxwell-and-waves/19-dalembert-solutions-and-radiation-from-current-sheets|Lecture 19]] ($\beta$, $\lambda$, $v_p$ from a phase); [[3-maxwell-and-waves/21-monochromatic-waves-and-phasor-notation|Lecture 21]] (the dispersion relations, defined); [[1-electrostatics/11-lorentz-drude-models-for-conductivity-and-susceptibility|Lecture 11]] (the Drude and Lorentz responses behind dispersion in plasmas and dielectrics); [[3-maxwell-and-waves/22-phasor-maxwell-equations-and-damped-waves|Lecture 22]] (in conducting media $v_p$ depends on frequency); Lecture 24 (group velocity, in a footnote; ECE 450 in detail).

**Practice.** [[practice/topics#monochromatic-waves-phasors-and-dispersion|Monochromatic waves, phasors and dispersion]] (13 problems) — for example [[practice/21-phasors-and-monochromatic-waves#211-reading-two-waves|21.1 Reading two waves]] (easy), [[practice/21-phasors-and-monochromatic-waves#216-radio-waves-in-a-plasma|21.6 Radio waves in a plasma]] (medium), [[practice/21-phasors-and-monochromatic-waves#219-a-phasor-from-two-snapshots|21.9 A phasor from two snapshots]] (hard).

Related: [[concepts/phasors]] · [[concepts/plane-waves]] · [[concepts/wave-equation]] · [[concepts/intrinsic-impedance]] · [[concepts/conductivity-and-susceptibility-models]] · [[concepts/permittivity]].
