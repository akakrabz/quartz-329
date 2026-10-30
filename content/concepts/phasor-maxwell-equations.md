---
title: "Maxwell's equations in phasor form"
description: "At one frequency ∂/∂t → jω: the curl equations become algebra, the divergence laws follow from them, a uniform conductor carries no oscillating charge, and the lossless case gives the Helmholtz equation ∇²Ẽ + ω²μεẼ = 0 with its plane-wave solutions."
tags: [concept, waves]
aliases: ["phasor Maxwell equations", "time-harmonic Maxwell equations", "Helmholtz equation", "phasor wave equation", "frequency-domain Maxwell equations"]
---

> [!key] Maxwell's equations in phasor form
> With every field and source monochromatic at $\omega$,
> $$
> \mathbf{E}(\mathbf{r},t) = \text{Re}\{\tilde{\mathbf{E}}(\mathbf{r})\,e^{j\omega t}\},
> $$
> and likewise $\mathbf{H}$, $\mathbf{D}$, $\mathbf{B}$, $\mathbf{J}$, $\rho$:
> $$
> \begin{gathered}
> \frac{\partial}{\partial t}\text{Re}\{\tilde{\mathbf{E}}e^{j\omega t}\} = \text{Re}\{j\omega\tilde{\mathbf{E}}e^{j\omega t}\}\\[4pt]
> \Longrightarrow\qquad\frac{\partial}{\partial t}\ \to\ j\omega .
> \end{gathered}
> $$
> | law | time domain | phasor domain |
> |---|---|---|
> | Gauss | $\nabla\cdot\mathbf{D} = \rho$ | $\nabla\cdot\tilde{\mathbf{D}} = \tilde\rho$ |
> | no magnetic charge | $\nabla\cdot\mathbf{B} = 0$ | $\nabla\cdot\tilde{\mathbf{B}} = 0$ |
> | Faraday | $\nabla\times\mathbf{E} = -\partial\mathbf{B}/\partial t$ | $\nabla\times\tilde{\mathbf{E}} = -j\omega\tilde{\mathbf{B}}$ |
> | Ampère–Maxwell | $\nabla\times\mathbf{H} = \mathbf{J} + \partial\mathbf{D}/\partial t$ | $\nabla\times\tilde{\mathbf{H}} = \tilde{\mathbf{J}} + j\omega\tilde{\mathbf{D}}$ |
> | continuity | $\nabla\cdot\mathbf{J} + \partial\rho/\partial t = 0$ | $\nabla\cdot\tilde{\mathbf{J}} + j\omega\tilde\rho = 0$ |
>
> Implied (the notes): $\tilde{\mathbf{D}} = \epsilon\tilde{\mathbf{E}}$, $\tilde{\mathbf{B}} = \mu\tilde{\mathbf{H}}$, $\tilde{\mathbf{J}} = \sigma\tilde{\mathbf{E}}$, at this frequency. Continuity is the [[concepts/continuity-equation|Continuity equation (charge conservation)]].

> [!key] The phasor wave equation (Helmholtz equation), no conductivity
> $$
> \nabla^2\tilde{\mathbf{E}} + \omega^2\mu\epsilon\,\tilde{\mathbf{E}} = 0 .
> $$
> The [[concepts/wave-equation|wave equation]] $\nabla^2\mathbf{E} = \mu\epsilon\,\partial^2\mathbf{E}/\partial t^2$ with $\partial^2/\partial t^2\to-\omega^2$. $\tilde{\mathbf{H}}$ obeys the same. Solutions along $z$: $\tilde E_x(z) = E_0e^{\mp j\beta z}$, $\beta = \omega\sqrt{\mu\epsilon}$, with $\tilde H_y = \pm\tilde E_x/\eta$, $\eta = \omega\mu/\beta = \sqrt{\mu/\epsilon}$.

**Physics.** [[concepts/phasors|Phasors]] turn one cosine into a complex amplitude; here every field and source is monochromatic at $\omega$. With $\omega$ real, $\partial/\partial t$ passes through $\text{Re}$, while $\nabla\cdot$ and $\nabla\times$ act on phasors unchanged, and $\text{Re}\{\tilde Ae^{j\omega t}\} = 0$ at every instant forces $\tilde A = 0$ (take $\omega t = 0$ and $\pi/2$), so each law holds phasor for phasor. Consequences:

- **Constants are numbers per frequency** (e.g. the Drude $\sigma(\omega)$, [[concepts/conductivity-and-susceptibility-models|Lorentz–Drude models of σ and χe]]): a time-domain convolution over the field's history becomes multiplication by a possibly complex number. Linear media only; other waveforms are Fourier sums (ECE 210), one phasor per frequency.
- **Divergence laws come free.** Divergence of phasor Faraday: $0 = -j\omega\nabla\cdot\tilde{\mathbf{B}}$, so $\nabla\cdot\tilde{\mathbf{B}} = 0$ for $\omega\neq0$. Of phasor Ampère, with continuity: $0 = \nabla\cdot\tilde{\mathbf{J}} + j\omega\nabla\cdot\tilde{\mathbf{D}} = j\omega(\nabla\cdot\tilde{\mathbf{D}} - \tilde\rho)$, so $\nabla\cdot\tilde{\mathbf{D}} = \tilde\rho$: the curl laws plus continuity contain both divergence laws.
- **No oscillating charge in a uniform conductor.** Continuity and Gauss: $-j\omega\tilde\rho = \nabla\cdot\tilde{\mathbf{J}} = \sigma\nabla\cdot\tilde{\mathbf{E}} = (\sigma/\epsilon)\tilde\rho$, so $(\sigma + j\omega\epsilon)\tilde\rho = 0$, $\tilde\rho = 0$: the relaxation equation $\partial\rho/\partial t + (\sigma/\epsilon)\rho = 0$ of [[concepts/conductors|Lecture 8]] with $\partial/\partial t\to j\omega$.

Notation: on the lossy-wave pages $\tau = \angle\eta$, not a relaxation or collision time.

**Conducting media: one replacement.** With $\tilde{\mathbf{J}} = \sigma\tilde{\mathbf{E}}$ only Ampère changes,

$$
\nabla\times\tilde{\mathbf{H}} = \sigma\tilde{\mathbf{E}} + j\omega\epsilon\tilde{\mathbf{E}} = (\sigma + j\omega\epsilon)\,\tilde{\mathbf{E}} .
$$

So every lossless result carries over with $j\omega\epsilon\to\sigma + j\omega\epsilon$ ([[concepts/propagation-constant|Propagation constant]]). Two readings of $\sigma + j\omega\epsilon$. *Complex conductivity:* conduction current $\sigma\tilde{\mathbf{E}}$ plus the [[concepts/displacement-current|displacement current]] $j\omega\epsilon\tilde{\mathbf{E}}$, 90° ahead; circuit twin: the leaky capacitor ([[concepts/conductance|Conductance and the leaky capacitor]]), $\tilde I = (G + j\omega C)\tilde V$ with $G/C = \sigma/\epsilon$. *Complex permittivity:* $\sigma + j\omega\epsilon = j\omega(\epsilon - j\sigma/\omega)$, so
$$
\epsilon_c = \epsilon - j\frac{\sigma}{\omega},\qquad \gamma = j\omega\sqrt{\mu\epsilon_c},\qquad \eta = \sqrt{\frac{\mu}{\epsilon_c}},
$$
the lossless forms with $\epsilon\to\epsilon_c$; the negative imaginary part is the in-phase, dissipating current. Notes: the first view; many textbooks the second. Conduction over displacement current is the [[concepts/loss-tangent|loss tangent]] $\sigma/\omega\epsilon = (1/\omega)/(\epsilon/\sigma)$; crossover $f = \sigma/2\pi\epsilon$: near 18 kHz for Lecture 10's lossy medium ($\epsilon = 2\epsilon_0$, $\sigma = 2\ \mu$S/m, $\epsilon/\sigma = 8.85\ \mu$s), near 0.9 GHz for sea water ($81\epsilon_0$, 4 S/m, $\epsilon/\sigma\approx0.18$ ns; Lecture 8 rounds to 0.2 ns). "Conductor" describes a material *at a frequency*.

**Time domain.** Curl of Faraday with $\mathbf{J} = \sigma\mathbf{E}$, uniform medium:
$$
\nabla^2\mathbf{E} = \mu\sigma\frac{\partial\mathbf{E}}{\partial t} + \mu\epsilon\frac{\partial^2\mathbf{E}}{\partial t^2} .
$$
The first term is the damping the [[concepts/wave-equation|wave equation]] promised: $f(t\mp z/v)$ fails, so waves decay and change shape; for $\sigma\gg\omega\epsilon$ the last term drops and it is a diffusion (heat) equation, and fields soak in rather than propagate. In phasors: $\nabla^2\tilde{\mathbf{E}} = (j\omega\mu\sigma - \omega^2\mu\epsilon)\tilde{\mathbf{E}} = \gamma^2\tilde{\mathbf{E}}$, one complex number.

> [!derivation]- Lecture 18's waves from the phasor equations
> With $\tilde\rho = 0$, $\tilde{\mathbf{J}} = 0$, constant $\mu$, $\epsilon$:
> $$
> \begin{gathered}
> \nabla\cdot\tilde{\mathbf{E}} = 0,\qquad \nabla\cdot\tilde{\mathbf{H}} = 0,\\[4pt]
> \nabla\times\tilde{\mathbf{E}} = -j\omega\mu\tilde{\mathbf{H}},\qquad \nabla\times\tilde{\mathbf{H}} = j\omega\epsilon\tilde{\mathbf{E}} .
> \end{gathered}
> $$
> Curl of Faraday: $\nabla\times(\nabla\times\tilde{\mathbf{E}}) = -j\omega\mu\,\nabla\times\tilde{\mathbf{H}} = -j\omega\mu\,(j\omega\epsilon\tilde{\mathbf{E}}) = \omega^2\mu\epsilon\,\tilde{\mathbf{E}}$, and the left side is $\nabla(\nabla\cdot\tilde{\mathbf{E}}) - \nabla^2\tilde{\mathbf{E}} = -\nabla^2\tilde{\mathbf{E}}$: the Helmholtz equation. For $\tilde{\mathbf{E}} = \hat x\,\tilde E_x(z)$:
> $$
> \frac{d^2\tilde E_x}{dz^2} + \omega^2\mu\epsilon\,\tilde E_x = 0 .
> $$
> The trial $e^{\mp\gamma z}$ gives $\gamma^2 = -\omega^2\mu\epsilon$, so
> $$
> \gamma = j\beta,\qquad \beta = \omega\sqrt{\mu\epsilon}\ \ [\text{rad/m}],
> $$
> (the root $-j\beta$ only swaps the exponentials) and
> $$
> \begin{gathered}
> \tilde E_x(z) = E_0e^{\mp j\beta z}\\[4pt]
> \Longleftrightarrow\quad E_x(z,t) = \lvert E_0\rvert\cos(\omega t\mp\beta z + \angle E_0),
> \end{gathered}
> $$
> waves toward $\pm z$ at $\omega/\beta = 1/\sqrt{\mu\epsilon}$. **H from phasor Faraday:** $\nabla\times(\hat x\tilde E_x) = \hat y\,d\tilde E_x/dz$, so $d\tilde E_x/dz = -j\omega\mu\tilde H_y$, with $d\tilde E_x/dz = \mp j\beta\tilde E_x$:
> $$
> \begin{gathered}
> \tilde H_y = -\frac{1}{j\omega\mu}\frac{d\tilde E_x}{dz} = \pm\frac{\beta}{\omega\mu}\tilde E_x = \pm\frac{\tilde E_x}{\eta},\\[6pt]
> \eta = \frac{\omega\mu}{\beta} = \sqrt{\frac\mu\epsilon} .
> \end{gathered}
> $$
> This is [[concepts/intrinsic-impedance|Lecture 18 §5]], with time integration replaced by division by $j\omega$: no static constant appears.

**Examples.**

> [!example] Example — H from E by the phasor curl
> Lossless, non-magnetic, $\epsilon_r = 4$: $\mathbf{E} = \hat y\,2\cos(2\pi\times10^8t + \tfrac{4\pi}{3}x)$ V/m. Find $\mathbf{H}$.
>
> $\tilde{\mathbf{E}} = \hat y\,2e^{j\beta x}$, $\beta = 4\pi/3$ rad/m $= \omega\sqrt{\mu_0\epsilon} = 2\pi\times10^8\times2/(3\times10^8)$ ✓; the $+$ means travel toward $-x$. Faraday: $\hat z\,j\beta\tilde E_y = -j\omega\mu_0\tilde{\mathbf{H}}$, so
> $$
> \begin{gathered}
> \tilde{\mathbf{H}} = -\hat z\,\frac{\beta}{\omega\mu_0}\,2e^{j\beta x} = -\hat z\,\frac{2}{\eta}\,e^{j\beta x},\\[6pt]
> \eta = \frac{\eta_0}{2} = 60\pi\ \Omega,
> \end{gathered}
> $$
> and $\mathbf{H} = -\hat z\,10.6\cos(2\pi\times10^8t + \tfrac{4\pi}{3}x)$ mA/m. Checks: $\hat u\times\tilde{\mathbf{E}}/\eta = (-\hat x)\times\hat y\,(2/\eta) = -\hat z\,(2/\eta)$ ✓; $\tilde{\mathbf{E}}\times\tilde{\mathbf{H}}^*$ along $\hat y\times(-\hat z) = -\hat x$ ✓.

- Drude in phasors: $j\omega m\tilde{\mathbf{v}} = q\tilde{\mathbf{E}} - m\nu\tilde{\mathbf{v}}$, so $\sigma(\omega) = Nq^2/\big(m(\nu + j\omega)\big)$.

> [!trap]
> - $\partial/\partial t\to j\omega$ only for the phasor of a *linear* equation at one frequency; no phasor for products ($\mathbf{E}\times\mathbf{H}$, $\mathbf{J}\cdot\mathbf{E}$: [[concepts/time-average-power|Time averages and average power]]).
> - $\gamma = j\beta$ in a lossless medium, not $\beta$: "$\gamma = 2$ rad/m" is off by $j$.
> - The root $-\gamma$ is no new wave: $e^{+\gamma z}$ is the $-z$ wave.
> - $\tilde\rho = 0$ inside a uniform conductor does not mean no surface charge at its boundary.

> [!exam] On exams
> **Phasor Maxwell true/false** (practice 22.1): which laws change under $\partial/\partial t\to j\omega$, which follow from the others. **γ and η from one lossless field** (SP18 Exam 3 #2a–c): $\gamma = j\beta$, then $\eta$ from $\gamma\eta = j\omega\mu$ (method on [[concepts/propagation-constant|Propagation constant]]).

**Where it appears.** [[3-maxwell-and-waves/22-phasor-maxwell-equations-and-damped-waves#1-maxwells-equations-at-one-frequency|Lecture 22 §1–2]] (defined; Helmholtz; the lossless waves); [[3-maxwell-and-waves/21-monochromatic-waves-and-phasor-notation|Lecture 21]] (phasor Faraday for $\tilde{\mathbf{H}}$); [[3-maxwell-and-waves/23-imperfect-dielectrics-and-good-conductors|Lecture 23]] (Ampère's law with $\sigma + j\omega\epsilon$); Unit 4 (phasor telegrapher's equations).

**Related.** [[concepts/maxwells-equations|Maxwell's equations]] · [[concepts/phasors|Phasors]] · [[concepts/wave-equation|Wave equation]] · [[concepts/propagation-constant|Propagation constant]] · [[concepts/intrinsic-impedance|Intrinsic impedance]] · [[concepts/continuity-equation|Continuity equation (charge conservation)]] · [[concepts/displacement-current|Displacement current]] · [[concepts/plane-waves|Plane waves]]. · [[0-toolkit/08-waves-in-media-figures|Waves in media — figures]]

**Practice.** [[practice/topics#damped-waves-in-lossy-and-conducting-media|Damped waves in lossy and conducting media]] (23 problems) — for example [[practice/22-damped-waves-in-conducting-media#221-phasor-maxwell-true-or-false|22.1 Phasor Maxwell, true or false]] (easy), [[practice/22-damped-waves-in-conducting-media#226-from-the-medium-to-the-wave|22.6 From the medium to the wave]] (medium), [[practice/22-damped-waves-in-conducting-media#229-decoding-a-wave-toward-minus-y|22.9 Decoding a wave toward minus y]] (hard).
