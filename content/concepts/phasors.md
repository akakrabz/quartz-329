---
title: "Phasors"
description: "A phasor is the complex amplitude of a sinusoid: a(t) = A cos(ωt + θ) = Re{Ã e^(jωt)} with Ã = A e^(jθ), the starting position of an arrow that turns at ω and whose shadow is a(t). A sine picks up −j, d/dt becomes jω, a delay τ becomes e^(−jωτ), a plane wave toward +z is Ẽ₀e^(−jβz), and the time average of a product is ⟨ab⟩ = ½Re{ÃB̃*}."
tags: [concept, waves]
aliases: ["phasor", "phasor notation", "complex amplitude", "time-harmonic fields", "time average of a product"]
---

> [!key] Definition
> $$
> \begin{gathered}
> a(t) = A\cos(\omega t + \theta) = \text{Re}\{\tilde A\,e^{j\omega t}\},\\[4pt]
> \tilde A = A\,e^{j\theta}\quad(\lvert\tilde A\rvert = A,\ \angle\tilde A = \theta).
> \end{gathered}
> $$
> For a field, $\mathbf{E}(\mathbf{r}, t) = \text{Re}\{\tilde{\mathbf{E}}(\mathbf{r})\,e^{j\omega t}\}$, where $\tilde{\mathbf{E}} = \tilde E_x\hat x + \tilde E_y\hat y + \tilde E_z\hat z$ has complex components and real unit vectors. The course uses the cosine as the reference and peak (not rms) amplitudes.
> $$
> \begin{gathered}
> \sin\to-j,\qquad \frac{d}{dt}\to j\omega,\qquad \int dt\to\frac{1}{j\omega},\\[4pt]
> a(t-\tau)\to\tilde Ae^{-j\omega\tau},\qquad \langle ab\rangle = \tfrac12\text{Re}\{\tilde A\tilde B^*\}.
> \end{gathered}
> $$

**Physics.** In a linear medium driven at a single frequency, every field, current and charge oscillates at that frequency once transients have died away, so each is fully described by an amplitude and a phase at each point. A phasor stores the two as one complex number and leaves the shared factor $e^{j\omega t}$ unwritten. Picture $\tilde Ae^{j\omega t}$ as an arrow of length $A$ turning counterclockwise once per period: $a(t)$ is its shadow on the real axis, and $\tilde A$ is the arrow at $t = 0$. Multiplying by $j$ turns the arrow $+90^\circ$, so its shadow peaks a quarter period earlier; differentiation, which makes a cosine peak a quarter period early, therefore becomes $j\omega$. Multiplying by $-j$ turns it $-90^\circ$, which is why $\sin(\omega t + \theta)$, a cosine a quarter period late, has phasor $-jAe^{j\theta}$. A delay $\tau$ is a phase lag $\omega\tau$: that is how the d'Alembert delay $z/v$ of a plane wave becomes the factor $e^{-j\beta z}$, so $\tilde{\mathbf{E}}_0e^{-j\beta\hat u\cdot\mathbf{r}}$ travels toward $+\hat u$. Sums and derivatives carry over to phasors; products do not, because the product of two signals at $\omega$ has parts at $0$ and $2\omega$. Its average is $\tfrac12\text{Re}\{\tilde A\tilde B^*\}$, which gives $\langle\mathbf{S}\rangle = \tfrac12\text{Re}\{\tilde{\mathbf{E}}\times\tilde{\mathbf{H}}^*\}$ and $\langle\mathbf{J}\cdot\mathbf{E}\rangle = \tfrac12\text{Re}\{\tilde{\mathbf{J}}\cdot\tilde{\mathbf{E}}^*\}$.

**Going back to the time domain.** Write the phasor in polar form, $\tilde A = \lvert\tilde A\rvert e^{j\angle\tilde A}$, with the angle in its own quadrant; then $a(t) = \lvert\tilde A\rvert\cos(\omega t + \angle\tilde A)$. Multiply by $e^{j\omega t}$ *before* taking the real part.

**Examples.**
- $3\sin(\omega t - 30^\circ) = 3\cos(\omega t - 120^\circ)$ has phasor $3e^{-j120^\circ} = -1.5 - 2.60j$.
- Adding sinusoids by adding arrows: $6\cos\omega t + 6\sin\omega t$ has phasor $6 - 6j = 6\sqrt2\,e^{-j45^\circ}$, so it equals $8.49\cos(\omega t - 45^\circ)$.
- $\tilde{\mathbf{E}} = (4 - 3j)e^{-j\beta z}\hat x$ V/m is $\mathbf{E} = 5\cos(\omega t - \beta z - 36.9^\circ)\,\hat x$ V/m $= [4\cos(\omega t - \beta z) + 3\sin(\omega t - \beta z)]\,\hat x$ V/m.
- The notes' plane wave: $\mathbf{E} = E_0\cos(\omega t\mp\beta z)\,\hat x\leftrightarrow\tilde{\mathbf{E}} = E_0e^{\mp j\beta z}\,\hat x$; its partner is $\tilde{\mathbf{H}} = \hat u\times\tilde{\mathbf{E}}/\eta$.
- The Drude equation of Lecture 11, $m\,d\mathbf{v}/dt = q\mathbf{E} - m\nu\mathbf{v}$, becomes $j\omega m\tilde{\mathbf{v}} = q\tilde{\mathbf{E}} - m\nu\tilde{\mathbf{v}}$, which gives the AC conductivity $\sigma(\omega) = Nq^2/\big(m(\nu + j\omega)\big)$.
- $\langle ab\rangle$ for $a = 3\cos(\omega t + 20^\circ)$ and $b = 2\cos(\omega t - 40^\circ)$: $\tfrac12\cdot3\cdot2\cos60^\circ = 1.5$.
- Worked problem: $-0.4\sin(\omega t + 2\pi z - \pi/4)\,\hat y$ has phasor $0.4e^{j\pi/4}e^{j2\pi z}\,\hat y$, and with $\eta = 40\pi\ \Omega$ the whole wave carries $5\pi\approx15.7$ W/m².

> [!trap]
> - The $-j$ of a sine, and the quadrant of the angle: $-4 + 3j$ is at $143.1^\circ$, not $-36.9^\circ$.
> - $e^{+j\beta z}$ travels toward $-z$. A minus sign in the exponent means travel toward plus.
> - A phasor never contains $t$, and a time-domain field is never complex. Do not write $\mathbf{E}(z,t) = 5e^{-j\beta z}\hat x$.
> - $\text{Re}\{\tilde A\}\cos\omega t$ is not $\text{Re}\{\tilde Ae^{j\omega t}\}$: it loses the sine part.
> - The $\tfrac12$ and the conjugate in $\langle ab\rangle = \tfrac12\text{Re}\{\tilde A\tilde B^*\}$. With rms phasors the $\tfrac12$ disappears; this course uses peak values.
> - The rules hold only when everything oscillates at one frequency. For a pulse, use Fourier analysis, which is a sum of phasor problems.

**Where it appears.** [[1-electrostatics/11-lorentz-drude-models-for-conductivity-and-susceptibility|Lecture 11]] (the AC conductivity and susceptibility, the course's first phasors); [[3-maxwell-and-waves/21-monochromatic-waves-and-phasor-notation|Lecture 21]] (defined for fields; plane-wave phasors; $\tilde{\mathbf{E}}\leftrightarrow\tilde{\mathbf{H}}$; time averages); [[3-maxwell-and-waves/22-phasor-maxwell-equations-and-damped-waves|Lecture 22]] (Maxwell's equations with $\partial/\partial t\to j\omega$; complex $\gamma = \alpha + j\beta$ and $\eta$); [[3-maxwell-and-waves/23-imperfect-dielectrics-and-good-conductors|Lecture 23]] (lossy media); Lecture 24 (polarization as phasor components with a phase between them); Lectures 25–26 (reflection, standing waves); Unit 4 (voltage and current phasors on transmission lines); [[problems/phasors-e-and-power-from-a-given-h]].

**Practice.** [[practice/topics#monochromatic-waves-phasors-and-dispersion|Monochromatic waves, phasors and dispersion]] (13 problems) — for example [[practice/21-phasors-and-monochromatic-waves#211-reading-two-waves|21.1 Reading two waves]] (easy), [[practice/21-phasors-and-monochromatic-waves#216-radio-waves-in-a-plasma|21.6 Radio waves in a plasma]] (medium), [[practice/21-phasors-and-monochromatic-waves#219-a-phasor-from-two-snapshots|21.9 A phasor from two snapshots]] (hard).

Related: [[concepts/plane-waves]] · [[concepts/dispersion-relation]] · [[concepts/poynting-vector]] · [[concepts/intrinsic-impedance]] · [[concepts/conductivity-and-susceptibility-models]] · [[concepts/superposition]].
