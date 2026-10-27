---
title: "Phasors"
description: "Complex amplitudes: Ã = A e^(jθ) for A cos(ωt + θ) = Re{Ã e^(jωt)}."
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
> For a field, $\mathbf{E}(\mathbf{r}, t) = \text{Re}\{\tilde{\mathbf{E}}(\mathbf{r})\,e^{j\omega t}\}$: complex components, real unit vectors. Cosine reference, peak (not rms) amplitudes.
> $$
> \begin{gathered}
> \sin\to-j,\qquad \frac{d}{dt}\to j\omega,\qquad \int dt\to\frac{1}{j\omega},\\[4pt]
> a(t-\tau)\to\tilde Ae^{-j\omega\tau},\qquad \langle ab\rangle = \tfrac12\text{Re}\{\tilde A\tilde B^*\}.
> \end{gathered}
> $$

**Physics.** Linear, one frequency, transients gone: each quantity is an amplitude and a phase, one complex number ($e^{j\omega t}$ unwritten). $\tilde Ae^{j\omega t}$ is an arrow of length $A$ turning counterclockwise; $a(t)$ is its shadow on the real axis, $\tilde A$ the arrow at $t = 0$. $\times j$ turns it $+90^\circ$ (peaks $T/4$ earlier), hence $d/dt\to j\omega$; $\times(-j)$ turns it $-90^\circ$, so $\sin(\omega t + \theta)$ has phasor $-jAe^{j\theta}$. A delay $\tau$ is a lag $\omega\tau$: the d'Alembert $z/v$ becomes $e^{-j\beta z}$, and $\tilde{\mathbf{E}}_0e^{-j\beta\hat u\cdot\mathbf{r}}$ travels toward $+\hat u$. Sums and derivatives carry over; products do not (parts at $0$ and $2\omega$). Their average gives $\langle\mathbf{S}\rangle = \tfrac12\text{Re}\{\tilde{\mathbf{E}}\times\tilde{\mathbf{H}}^*\}$ and $\langle\mathbf{J}\cdot\mathbf{E}\rangle = \tfrac12\text{Re}\{\tilde{\mathbf{J}}\cdot\tilde{\mathbf{E}}^*\}$.

**Going back to the time domain.** Polar form $\tilde A = \lvert\tilde A\rvert e^{j\angle\tilde A}$ gives $a(t) = \lvert\tilde A\rvert\cos(\omega t + \angle\tilde A)$. Multiply by $e^{j\omega t}$ *before* taking Re.

**Examples.**
- $3\sin(\omega t - 30^\circ) = 3\cos(\omega t - 120^\circ)$: $3e^{-j120^\circ} = -1.5 - 2.60j$.
- $6\cos\omega t + 6\sin\omega t$: $6 - 6j = 6\sqrt2\,e^{-j45^\circ}$, i.e. $8.49\cos(\omega t - 45^\circ)$.
- $\tilde{\mathbf{E}} = (4 - 3j)e^{-j\beta z}\hat x$ V/m is $5\cos(\omega t - \beta z - 36.9^\circ)\,\hat x$ $= [4\cos(\omega t - \beta z) + 3\sin(\omega t - \beta z)]\,\hat x$ V/m.
- Notes: $\mathbf{E} = E_0\cos(\omega t\mp\beta z)\,\hat x\leftrightarrow\tilde{\mathbf{E}} = E_0e^{\mp j\beta z}\,\hat x$; partner $\tilde{\mathbf{H}} = \hat u\times\tilde{\mathbf{E}}/\eta$.
- Drude: $m\,d\mathbf{v}/dt = q\mathbf{E} - m\nu\mathbf{v}$ becomes $j\omega m\tilde{\mathbf{v}} = q\tilde{\mathbf{E}} - m\nu\tilde{\mathbf{v}}$, so $\sigma(\omega) = Nq^2/\big(m(\nu + j\omega)\big)$.
- $a = 3\cos(\omega t + 20^\circ)$, $b = 2\cos(\omega t - 40^\circ)$: $\langle ab\rangle = \tfrac12\cdot3\cdot2\cos60^\circ = 1.5$.
- $-0.4\sin(\omega t + 2\pi z - \pi/4)\,\hat y$ has phasor $0.4e^{j\pi/4}e^{j2\pi z}\,\hat y$; with $\eta = 40\pi\ \Omega$ the whole wave carries $5\pi\approx15.7$ W/m².

> [!trap]
> - The $-j$ of a sine; the quadrant: $-4 + 3j$ is at $143.1^\circ$, not $-36.9^\circ$.
> - $e^{+j\beta z}$ travels toward $-z$.
> - No $t$ in a phasor, nothing complex in time: never $\mathbf{E}(z,t) = 5e^{-j\beta z}\hat x$.
> - $\text{Re}\{\tilde A\}\cos\omega t$ is not $\text{Re}\{\tilde Ae^{j\omega t}\}$: it loses the sine part.
> - The $\tfrac12$ and the conjugate in $\langle ab\rangle$; rms phasors drop the $\tfrac12$.
> - One frequency only; a pulse needs Fourier analysis, a sum of phasor problems.

**Where it appears.** [[1-electrostatics/11-lorentz-drude-models-for-conductivity-and-susceptibility|Lecture 11]] (first use); [[3-maxwell-and-waves/21-monochromatic-waves-and-phasor-notation|Lecture 21]] (fields); [[3-maxwell-and-waves/22-phasor-maxwell-equations-and-damped-waves|Lecture 22]] (complex $\gamma$, $\eta$); [[3-maxwell-and-waves/23-imperfect-dielectrics-and-good-conductors|Lecture 23]]; Lectures 24–26; Unit 4 (line phasors); [[problems/phasors-e-and-power-from-a-given-h]].

**Practice.** [[practice/topics#monochromatic-waves-phasors-and-dispersion|Monochromatic waves, phasors and dispersion]] (22 problems) — for example [[practice/21-phasors-and-monochromatic-waves#211-reading-two-waves|21.1 Reading two waves]] (easy), [[practice/21-phasors-and-monochromatic-waves#216-radio-waves-in-a-plasma|21.6 Radio waves in a plasma]] (medium), [[practice/21-phasors-and-monochromatic-waves#219-a-phasor-from-two-snapshots|21.9 A phasor from two snapshots]] (hard).

Related: [[concepts/plane-waves]] · [[concepts/dispersion-relation]] · [[concepts/poynting-vector]] · [[concepts/intrinsic-impedance]] · [[concepts/conductivity-and-susceptibility-models]] · [[concepts/superposition]].
