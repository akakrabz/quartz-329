---
title: "Lecture 22 — Maxwell's equations in phasor form and damped waves in conducting media"
description: "At one frequency ∂/∂t becomes jω, and a conducting medium enters through one replacement, jωε → σ + jωε: plane waves vary as e^(∓γz) with γ = α + jβ = √(jωμ(σ + jωε)), decay by 1/e over δ = 1/α, and H lags E by the angle τ of η = √(jωμ/(σ + jωε)). One ratio, σ/ωε, places a medium anywhere between a perfect dielectric and a perfect conductor."
tags: [lecture, waves]
lecture: 22
---

*Lecture 22 · course notes §22 · **slides: not yet available — this page is built from the course notes** · prev: [[3-maxwell-and-waves/21-monochromatic-waves-and-phasor-notation|Lecture 21]] · next: [[3-maxwell-and-waves/23-imperfect-dielectrics-and-good-conductors|Lecture 23]] · worked problem: [[problems/decoding-a-damped-wave|Decoding a damped wave]] · practice: [[practice/22-damped-waves-in-conducting-media|12 problems]]*

> [!abstract] In one breath
> With $\partial/\partial t\to j\omega$, Maxwell's equations become algebra for the phasors of [[3-maxwell-and-waves/21-monochromatic-waves-and-phasor-notation|Lecture 21]] and reproduce the waves of [[3-maxwell-and-waves/18-the-wave-equation-and-plane-tem-waves|Lecture 18]]. Conductivity turns $j\omega\epsilon$ into $\sigma + j\omega\epsilon$: the **propagation constant** $\gamma = \alpha + j\beta$ and **intrinsic impedance** $\eta$ go complex, the amplitude falls by $1/e$ per **penetration depth** $\delta = 1/\alpha$, and $\mathbf{H}$ lags $\mathbf{E}$ by $\tau = \angle\eta$. The ratio $\sigma/\omega\epsilon$ ([[1-electrostatics/08-conductors-dielectrics-and-polarization|Lecture 8]]'s relaxation time against $1/\omega$) sorts imperfect dielectrics from good conductors ([[3-maxwell-and-waves/23-imperfect-dielectrics-and-good-conductors|Lecture 23]]).

## 1. Maxwell's equations at one frequency

[[3-maxwell-and-waves/21-monochromatic-waves-and-phasor-notation|Lecture 21]] turned a cosine into a **phasor** ([[concepts/phasors]]); now every field and source is **monochromatic** at $\omega$:

$$
\mathbf{E}(\mathbf{r},t) = \text{Re}\{\tilde{\mathbf{E}}(\mathbf{r})\,e^{j\omega t}\},
$$

and likewise $\mathbf{H}$, $\mathbf{D}$, $\mathbf{B}$, $\mathbf{J}$, $\rho$. With $\omega$ real, $\partial/\partial t$ passes through $\text{Re}$:

$$
\begin{gathered}
\frac{\partial}{\partial t}\text{Re}\{\tilde{\mathbf{E}}e^{j\omega t}\} = \text{Re}\{j\omega\tilde{\mathbf{E}}e^{j\omega t}\}\\[4pt]
\Longrightarrow\qquad\frac{\partial}{\partial t}\ \to\ j\omega .
\end{gathered}
$$

$\nabla\cdot$ and $\nabla\times$ act on phasors unchanged, and $\text{Re}\{\tilde Ae^{j\omega t}\} = 0$ at every instant forces $\tilde A = 0$ (take $\omega t = 0$ and $\pi/2$). So:

> [!key] Maxwell's equations in phasor form
> | law | time domain | phasor domain |
> |---|---|---|
> | Gauss | $\nabla\cdot\mathbf{D} = \rho$ | $\nabla\cdot\tilde{\mathbf{D}} = \tilde\rho$ |
> | no magnetic charge | $\nabla\cdot\mathbf{B} = 0$ | $\nabla\cdot\tilde{\mathbf{B}} = 0$ |
> | Faraday | $\nabla\times\mathbf{E} = -\partial\mathbf{B}/\partial t$ | $\nabla\times\tilde{\mathbf{E}} = -j\omega\tilde{\mathbf{B}}$ |
> | Ampère–Maxwell | $\nabla\times\mathbf{H} = \mathbf{J} + \partial\mathbf{D}/\partial t$ | $\nabla\times\tilde{\mathbf{H}} = \tilde{\mathbf{J}} + j\omega\tilde{\mathbf{D}}$ |
> | continuity | $\nabla\cdot\mathbf{J} + \partial\rho/\partial t = 0$ | $\nabla\cdot\tilde{\mathbf{J}} + j\omega\tilde\rho = 0$ |
>
> Implied (the notes): $\tilde{\mathbf{D}} = \epsilon\tilde{\mathbf{E}}$, $\tilde{\mathbf{B}} = \mu\tilde{\mathbf{H}}$, $\tilde{\mathbf{J}} = \sigma\tilde{\mathbf{E}}$, at this frequency. Continuity is [[3-maxwell-and-waves/16-charge-conservation-displacement-current-and-maxwells-equations|Lecture 16]]'s.

- **Constants are numbers per frequency** (e.g. the Drude $\sigma(\omega)$ of [[1-electrostatics/11-lorentz-drude-models-for-conductivity-and-susceptibility|Lecture 11]]): a time-domain convolution over the field's history becomes multiplication by a possibly complex number (§8). Linear media only; other waveforms are Fourier sums (ECE 210), one phasor per frequency ([[3-maxwell-and-waves/18-the-wave-equation-and-plane-tem-waves|Lecture 18]] §4).
- **Divergence laws come free.** Divergence of phasor Faraday: $0 = -j\omega\nabla\cdot\tilde{\mathbf{B}}$, so $\nabla\cdot\tilde{\mathbf{B}} = 0$ for $\omega\neq0$. Of phasor Ampère, with continuity: $0 = \nabla\cdot\tilde{\mathbf{J}} + j\omega\nabla\cdot\tilde{\mathbf{D}} = j\omega(\nabla\cdot\tilde{\mathbf{D}} - \tilde\rho)$, so $\nabla\cdot\tilde{\mathbf{D}} = \tilde\rho$: the curl laws plus continuity contain both divergence laws.
- **No oscillating charge in a uniform conductor.** Continuity and Gauss: $-j\omega\tilde\rho = \nabla\cdot\tilde{\mathbf{J}} = \sigma\nabla\cdot\tilde{\mathbf{E}} = (\sigma/\epsilon)\tilde\rho$, so $(\sigma + j\omega\epsilon)\tilde\rho = 0$, $\tilde\rho = 0$: the relaxation equation $\partial\rho/\partial t + (\sigma/\epsilon)\rho = 0$ of [[1-electrostatics/08-conductors-dielectrics-and-polarization#2-conductors-in-electrostatics|Lecture 8 §2]] with $\partial/\partial t\to j\omega$.

Notation: $\tau = \angle\eta$, not a relaxation or collision time.

## 2. No conductivity: the Helmholtz equation and Lecture 18's waves

With $\tilde\rho = 0$, $\tilde{\mathbf{J}} = 0$, constant $\mu$, $\epsilon$:

$$
\begin{gathered}
\nabla\cdot\tilde{\mathbf{E}} = 0,\qquad \nabla\cdot\tilde{\mathbf{H}} = 0,\\[4pt]
\nabla\times\tilde{\mathbf{E}} = -j\omega\mu\tilde{\mathbf{H}},\qquad \nabla\times\tilde{\mathbf{H}} = j\omega\epsilon\tilde{\mathbf{E}} .
\end{gathered}
$$

Curl of Faraday: $\nabla\times(\nabla\times\tilde{\mathbf{E}}) = -j\omega\mu\,\nabla\times\tilde{\mathbf{H}} = -j\omega\mu\,(j\omega\epsilon\tilde{\mathbf{E}}) = \omega^2\mu\epsilon\,\tilde{\mathbf{E}}$, and the left side is $\nabla(\nabla\cdot\tilde{\mathbf{E}}) - \nabla^2\tilde{\mathbf{E}} = -\nabla^2\tilde{\mathbf{E}}$:

> [!key] The phasor wave equation (Helmholtz equation)
> $$
> \nabla^2\tilde{\mathbf{E}} + \omega^2\mu\epsilon\,\tilde{\mathbf{E}} = 0 .
> $$
> Lecture 18's $\nabla^2\mathbf{E} = \mu\epsilon\,\partial^2\mathbf{E}/\partial t^2$ with $\partial^2/\partial t^2\to-\omega^2$. $\tilde{\mathbf{H}}$ obeys the same ([[concepts/wave-equation]]).

For $\tilde{\mathbf{E}} = \hat x\,\tilde E_x(z)$:

$$
\frac{d^2\tilde E_x}{dz^2} + \omega^2\mu\epsilon\,\tilde E_x = 0 .
$$

The trial $e^{\mp\gamma z}$ gives $\gamma^2 = -\omega^2\mu\epsilon$, so

$$
\gamma = j\beta,\qquad \beta = \omega\sqrt{\mu\epsilon}\ \ [\text{rad/m}],
$$

(the root $-j\beta$ only swaps the exponentials) and

$$
\begin{gathered}
\tilde E_x(z) = E_0e^{\mp j\beta z}\\[4pt]
\Longleftrightarrow\quad E_x(z,t) = \lvert E_0\rvert\cos(\omega t\mp\beta z + \angle E_0),
\end{gathered}
$$

waves toward $\pm z$ at $\omega/\beta = 1/\sqrt{\mu\epsilon}$.

**H from phasor Faraday:** $\nabla\times(\hat x\tilde E_x) = \hat y\,d\tilde E_x/dz$, so $d\tilde E_x/dz = -j\omega\mu\tilde H_y$, with $d\tilde E_x/dz = \mp j\beta\tilde E_x$:

$$
\begin{gathered}
\tilde H_y = -\frac{1}{j\omega\mu}\frac{d\tilde E_x}{dz} = \pm\frac{\beta}{\omega\mu}\tilde E_x = \pm\frac{\tilde E_x}{\eta},\\[6pt]
\eta = \frac{\omega\mu}{\beta} = \sqrt{\frac\mu\epsilon} .
\end{gathered}
$$

This is [[3-maxwell-and-waves/18-the-wave-equation-and-plane-tem-waves#5-h-from-e-the-intrinsic-impedance|Lecture 18 §5]], with time integration replaced by division by $j\omega$: no static constant appears.

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

## 3. Conducting media: one replacement

With $\tilde{\mathbf{J}} = \sigma\tilde{\mathbf{E}}$ ($\tilde\rho = 0$, §1) only Ampère changes:

$$
\nabla\times\tilde{\mathbf{H}} = \sigma\tilde{\mathbf{E}} + j\omega\epsilon\tilde{\mathbf{E}} = (\sigma + j\omega\epsilon)\,\tilde{\mathbf{E}} .
$$

So every §2 result carries over with $j\omega\epsilon\to\sigma + j\omega\epsilon$:

$$
\begin{gathered}
\gamma^2 = -\omega^2\mu\epsilon = (j\omega\mu)(j\omega\epsilon)\\[4pt]
\longrightarrow\quad \gamma^2 = (j\omega\mu)(\sigma + j\omega\epsilon),\\[8pt]
\eta = \sqrt{\frac{j\omega\mu}{j\omega\epsilon}}\quad\longrightarrow\quad \eta = \sqrt{\frac{j\omega\mu}{\sigma + j\omega\epsilon}} .
\end{gathered}
$$

> [!key] Propagation constant and intrinsic impedance of a conducting medium
> $$
> \begin{gathered}
> \gamma = \sqrt{j\omega\mu(\sigma + j\omega\epsilon)} = \alpha + j\beta\ \ [\text{m}^{-1}],\\[6pt]
> \eta = \sqrt{\frac{j\omega\mu}{\sigma + j\omega\epsilon}} = \lvert\eta\rvert e^{j\tau}\ \ [\Omega],\\[6pt]
> \gamma\eta = j\omega\mu,\qquad \frac{\gamma}{\eta} = \sigma + j\omega\epsilon .
> \end{gathered}
> $$
> Roots with positive real part ($\sigma = 0$: $\gamma = +j\beta$): $\alpha\ge0$, $\beta>0$, $0\le\tau<45^\circ$ (§5); $\alpha = \tau = 0$ only if $\sigma = 0$. **Attenuation constant** $\alpha$ in nepers per metre (Np/m), **phase constant** $\beta$ in rad/m; both 1/m. See [[concepts/propagation-constant]], [[concepts/intrinsic-impedance]].

Backwards (notes' margin; real $\sigma$, $\epsilon$):

$$
\mu = \frac{\gamma\eta}{j\omega},\qquad \sigma = \text{Re}\Big\{\frac\gamma\eta\Big\},\qquad \epsilon = \frac1\omega\,\text{Im}\Big\{\frac\gamma\eta\Big\} .
$$

**Two ways to read σ + jωε.**

- *Complex conductivity:* conduction current $\sigma\tilde{\mathbf{E}}$ plus the displacement current $j\omega\epsilon\tilde{\mathbf{E}}$ of [[3-maxwell-and-waves/16-charge-conservation-displacement-current-and-maxwells-equations#2-the-asymmetry-and-maxwells-displacement-current|Lecture 16]], 90° ahead. Circuit twin: the leaky capacitor of [[1-electrostatics/10-capacitance-and-conductance#6-conductance-the-leaky-capacitor|Lecture 10]], $\tilde I = (G + j\omega C)\tilde V$ with $G/C = \sigma/\epsilon$ (one homogeneous filling).
- *Complex permittivity:* $\sigma + j\omega\epsilon = j\omega(\epsilon - j\sigma/\omega)$, so
$$
\epsilon_c = \epsilon - j\frac{\sigma}{\omega},\qquad \gamma = j\omega\sqrt{\mu\epsilon_c},\qquad \eta = \sqrt{\frac{\mu}{\epsilon_c}},
$$
the lossless forms with $\epsilon\to\epsilon_c$; the negative imaginary part is the in-phase, dissipating current. The notes use the first view, many textbooks the second.

**One ratio decides.** Conduction over displacement current is $\sigma/\omega\epsilon = (1/\omega)/(\epsilon/\sigma)$, Lecture 23's **loss tangent** ([[concepts/loss-tangent]]; physics there). Crossover $f = \sigma/2\pi\epsilon$: near 18 kHz for Lecture 10's lossy medium ($\epsilon = 2\epsilon_0$, $\sigma = 2\ \mu$S/m, $\epsilon/\sigma = 8.85\ \mu$s), near 0.9 GHz for sea water ($81\epsilon_0$, 4 S/m, $\epsilon/\sigma\approx0.18$ ns; Lecture 8 rounds to 0.2 ns). "Conductor" describes a material *at a frequency*.

**Time domain.** Curl of Faraday with $\mathbf{J} = \sigma\mathbf{E}$, uniform medium:

$$
\nabla^2\mathbf{E} = \mu\sigma\frac{\partial\mathbf{E}}{\partial t} + \mu\epsilon\frac{\partial^2\mathbf{E}}{\partial t^2} .
$$

The first term is the damping [[3-maxwell-and-waves/18-the-wave-equation-and-plane-tem-waves#2-the-wave-equation|Lecture 18 §2]] promised: $f(t\mp z/v)$ fails, so waves decay and change shape; for $\sigma\gg\omega\epsilon$ the last term drops and it is a diffusion (heat) equation, and fields soak in rather than propagate. In phasors: $\nabla^2\tilde{\mathbf{E}} = (j\omega\mu\sigma - \omega^2\mu\epsilon)\tilde{\mathbf{E}} = \gamma^2\tilde{\mathbf{E}}$, one complex number.

## 4. The damped plane wave

> [!key] An x-polarized plane wave in a conducting medium
> $$
> \begin{gathered}
> \tilde{\mathbf{E}} = \hat x\,E_0e^{\mp\gamma z},\qquad \tilde{\mathbf{H}} = \pm\hat y\,\frac{E_0}{\eta}\,e^{\mp\gamma z},\\[6pt]
> \mathbf{E} = \hat x\,\lvert E_0\rvert\,e^{\mp\alpha z}\cos(\omega t\mp\beta z + \angle E_0),\\[4pt]
> \mathbf{H} = \pm\hat y\,\frac{\lvert E_0\rvert}{\lvert\eta\rvert}\,e^{\mp\alpha z}\cos(\omega t\mp\beta z + \angle E_0 - \tau).
> \end{gathered}
> $$
> Upper signs: toward $+z$; lower: toward $-z$. Either way the wave **decays in the direction it travels**.

- **β sets the phase:** $\lambda = 2\pi/\beta$, $v_p = \omega/\beta = \lambda f$, with $\beta$ no longer $\propto\omega$: $v_p$ is not constant, nor $\lambda\propto1/f$. $v_p$ is the speed of the **nodes** (zero crossings), which decay cannot move; $\lambda$ is twice the node spacing. Frequency-dependent $v_p$ spreads pulses (dispersion, [[concepts/dispersion-relation]]); group velocity (a different speed) is ECE 450's, signal transmission Lecture 24's.
- **α sets the decay.** The **penetration depth**
$$
\delta\equiv\frac1\alpha = \frac{1}{\text{Re}\{\sqrt{j\omega\mu(\sigma + j\omega\epsilon)}\}}
$$
is where the amplitude is down by $e$, to 37 % (the **skin depth** when small, [[concepts/skin-depth]]); the power, $\propto e^{-2\alpha z}$, is at 13.5 %. One neper is a factor $e$: $20\log_{10}e = 8.686$ dB.
- **τ sets the timing:** $\mathbf{H}$ peaks $\tau/\omega$ after $\mathbf{E}$; in a snapshot it sits $\tau/\beta$ behind, on the source side.

<!-- fig:lossy-damped-wave -->

**Damped in space, steady in time:** at a fixed point the field is a steady sinusoid (the source feeds it); the amplitude decays from point to point.

<!-- fig:lossy-phasor-spiral -->

**Direction.** Lecture 18's rule, with complex $\eta$:

$$
\tilde{\mathbf{H}} = \frac1\eta\,\hat u\times\tilde{\mathbf{E}},\qquad \tilde{\mathbf{E}} = \eta\,\tilde{\mathbf{H}}\times\hat u .
$$

Dividing by $\eta$ divides by $\lvert\eta\rvert$ *and* subtracts $\tau$. Lecture 21's $\langle\mathbf{S}\rangle = \tfrac12\text{Re}\{\tilde{\mathbf{E}}\times\tilde{\mathbf{H}}^*\}$, for the $+z$ wave $\hat z\,(\lvert E_0\rvert^2/2\lvert\eta\rvert)\cos\tau\,e^{-2\alpha z}$, still points along $\hat u$ ($\cos\tau>0$); the lost power is the $\mathbf{J}\cdot\mathbf{E}>0$ Joule term of Poynting's theorem ([[concepts/poynting-theorem]]; Lecture 23).

> [!trap] Sign and phase traps with damped waves
> - **Which exponential.** $e^{-\gamma z} = e^{-\alpha z}e^{-j\beta z}$: toward $+z$; $e^{+\gamma z}$: toward $-z$. $e^{-\alpha z}\cos(\omega t + \beta z)$ would grow along its travel: impossible in a passive medium.
> - **The phase of H.** $\tilde{\mathbf{E}}/\eta$ subtracts $\tau$, $\eta\tilde{\mathbf{H}}$ adds it. With real $\mu$, $\epsilon$, $\sigma$ (every medium here), $\mathbf{H}$ lags $\mathbf{E}$.
> - **β is never smaller than α.** Real $\sigma$ puts $\angle\gamma$ between 45° and 90° (§5); $\beta = \alpha$ only in the good-conductor limit. Exception: the §8 plasma (imaginary $\sigma$), $\beta = 0$ below its plasma frequency.
> - **Nepers and radians.** $\alpha$ multiplies distance in an exponential, $\beta$ in a cosine; both 1/m, not interchangeable.
> - **Degrees and radians in one argument.** In $\cos(\omega t - 4x + 60^\circ)$, $\beta x$ is radians, the constant degrees: convert before adding $\tau$.

## 5. The general formulas, and how to decode a damped wave

The notes take $\alpha$, $\beta$ as Re and Im of the root (the calculator route). Squaring $\gamma = \alpha + j\beta$ (Rao §5.3):

$$
\begin{gathered}
(\alpha + j\beta)^2 = \alpha^2 - \beta^2 + 2j\alpha\beta = -\omega^2\mu\epsilon + j\omega\mu\sigma\\[4pt]
\Longrightarrow\quad \beta^2 - \alpha^2 = \omega^2\mu\epsilon,\qquad 2\alpha\beta = \omega\mu\sigma .
\end{gathered}
$$

With $\alpha^2 + \beta^2 = \lvert\gamma\rvert^2 = \lvert j\omega\mu\rvert\,\lvert\sigma + j\omega\epsilon\rvert = \omega^2\mu\epsilon\sqrt{1 + (\sigma/\omega\epsilon)^2}$, add and subtract:

> [!key] The general formulas (real, positive σ, ε, μ)
> $$
> \begin{gathered}
> \alpha = \omega\sqrt{\frac{\mu\epsilon}{2}}\left[\sqrt{1 + \Big(\frac{\sigma}{\omega\epsilon}\Big)^2} - 1\right]^{1/2},\\[8pt]
> \beta = \omega\sqrt{\frac{\mu\epsilon}{2}}\left[\sqrt{1 + \Big(\frac{\sigma}{\omega\epsilon}\Big)^2} + 1\right]^{1/2},\\[8pt]
> \lvert\eta\rvert = \frac{\sqrt{\mu/\epsilon}}{\big[1 + (\sigma/\omega\epsilon)^2\big]^{1/4}},\\[8pt]
> \tau = \frac12\tan^{-1}\frac{\sigma}{\omega\epsilon},\qquad \angle\gamma = 90^\circ - \tau,\\[8pt]
> \frac\alpha\beta = \tan\tau,\qquad \frac{\sigma}{\omega\epsilon} = \tan2\tau = \frac{2\alpha\beta}{\beta^2 - \alpha^2} .
> \end{gathered}
> $$
> Also $\lvert\gamma\rvert\lvert\eta\rvert = \omega\mu$.

**Where the angles come from.** $j\omega\mu$ is at 90°, $\sigma + j\omega\epsilon$ at $90^\circ - \tan^{-1}(\sigma/\omega\epsilon)$. $\eta$ (root of the ratio) takes half the difference, $\tau$; $\gamma$ (root of the product) half the sum, $90^\circ - \tau$. Hence $\alpha/\beta = \cot\angle\gamma = \tan\tau$.

Beyond the scales $\omega\sqrt{\mu\epsilon}$ and $\sqrt{\mu/\epsilon}$, only $\sigma/\omega\epsilon$ matters:

<!-- fig:lossy-phase-dial -->

> [!recipe] Decoding a damped wave (the exam skill)
> 1. **Read off.** Opposite signs on the $t$ and position terms: travel toward $+$ that axis; same signs: toward $-$. $\omega$: coefficient of $t$; $\beta$: of position in the cosine; $\alpha$: in the exponential, which must decay along the travel. $\gamma = \alpha + j\beta$.
> 2. **η** $= j\omega\mu/\gamma$ with the medium's $\mu$: $\lvert\eta\rvert = \omega\mu/\lvert\gamma\rvert$, $\tau = 90^\circ - \angle\gamma = \tan^{-1}(\alpha/\beta)$.
> 3. **The other field.** $\tilde{\mathbf{H}} = \hat u\times\tilde{\mathbf{E}}/\eta$ (divide by $\lvert\eta\rvert$, subtract $\tau$) or $\tilde{\mathbf{E}} = \eta\,\tilde{\mathbf{H}}\times\hat u$ (multiply, add $\tau$). Do the cross product; never guess.
> 4. **The medium.** $\gamma/\eta = \gamma^2/j\omega\mu = \sigma + j\omega\epsilon$: $\sigma = 2\alpha\beta/\omega\mu$, $\epsilon = (\beta^2 - \alpha^2)/\omega^2\mu$.
> 5. **The regime.** $\sigma/\omega\epsilon = 2\alpha\beta/(\beta^2 - \alpha^2) = \tan2\tau$ (§6).
> 6. **Sanity checks.** $\beta\ge\alpha$; $0\le\tau<45^\circ$; $\lvert\gamma\rvert\lvert\eta\rvert = \omega\mu$; $\epsilon\ge\epsilon_0$ for ordinary matter.

> [!example] Example — decode $\mathbf{E} = \hat y\,6e^{-x}\cos(3\times10^8t - 3x)$ V/m in a non-magnetic medium
> Find $\gamma$, $\eta$, $\mathbf{H}$, $\sigma$, $\epsilon$, $\delta$, $\lambda$, $v_p$ ($\epsilon_0 = 10^{-9}/36\pi$ F/m).
> - **Read off.** Opposite signs: toward $+x$, with $e^{-x}$ decaying that way ✓. $\omega = 3\times10^8$ rad/s ($f = 47.7$ MHz), $\alpha = 1$ Np/m, $\beta = 3$ rad/m, $\gamma = 1 + j3 = \sqrt{10}\,e^{j71.6^\circ}$ m⁻¹.
> - **η.** $\omega\mu_0 = 3\times10^8\times4\pi\times10^{-7} = 120\pi$ Ω/m:
> $$
> \begin{gathered}
> \eta = \frac{j120\pi}{1 + j3} = \frac{120\pi\,j(1 - j3)}{10} = 12\pi(3 + j)\\[6pt]
> = 113.1 + j37.7 = 119.2\,e^{j18.4^\circ}\ \Omega .
> \end{gathered}
> $$
> Check: $\tan^{-1}(1/3) = 18.4^\circ$ ✓.
> - **H.** $\tilde{\mathbf{H}} = \hat x\times\hat y\,(6/\eta)\,e^{-\gamma x} = \hat z\,(6/119.2)\,e^{-j18.4^\circ}e^{-\gamma x}$ A/m: $\mathbf{H} = \hat z\,50.3\,e^{-x}\cos(3\times10^8t - 3x - 18.4^\circ)$ mA/m. Check: $\hat y\times\hat z = +\hat x$ ✓.
> - **The medium.** $\gamma^2 = -8 + j6$, $\gamma/\eta = (-8 + j6)/(j120\pi) = (6 + j8)/120\pi$: $\sigma = 6/120\pi = 1/20\pi = 15.9$ mS/m; $\omega\epsilon = 8/120\pi$ gives $\epsilon = 7.07\times10^{-11}$ F/m $= 8\epsilon_0$. $\sigma/\omega\epsilon = 3/4$: comparable currents.
> - **Lengths, speed.** $\delta = 1$ m, $\lambda = 2.09$ m, $v_p = 1.0\times10^8$ m/s, below the $c/\sqrt8 = 1.06\times10^8$ m/s of a lossless $\epsilon_r = 8$.
> - **Cross-check.** $\omega\sqrt{\mu\epsilon} = 2\sqrt2$ rad/m, $\sqrt{1 + (3/4)^2} = 5/4$: $\alpha = 2\sqrt{5/4 - 1} = 1$ ✓, $\beta = 2\sqrt{5/4 + 1} = 3$ ✓.

> [!trap] What μ does, and does not, change
> $\mu$ enters $\eta = j\omega\mu/\gamma$, $\sigma = 2\alpha\beta/\omega\mu$ and $\epsilon = (\beta^2 - \alpha^2)/\omega^2\mu$: $\mu_0$ for a magnetic medium spoils all three, but not $\sigma/\omega\epsilon$, so the regime verdict survives. The [[problems/decoding-a-damped-wave|worked problem]] ($\mu = 3\mu_0$) shows the factor of 3.

## 6. Four regimes at a glance

Overview; [[3-maxwell-and-waves/23-imperfect-dielectrics-and-good-conductors|Lecture 23]] has the notes' table, real materials and power.

> [!key] The four regimes (overview)
> - **Perfect dielectric**, $\sigma = 0$: $\gamma = j\omega\sqrt{\mu\epsilon}$, $\eta = \sqrt{\mu/\epsilon}$; no decay, $\alpha = \tau = 0$.
> - **Imperfect dielectric** (notes: also "lousy" conductor), $\sigma\ll\omega\epsilon$: $\gamma\approx\tfrac\sigma2\sqrt{\mu/\epsilon} + j\omega\sqrt{\mu\epsilon}$, $\eta\approx\sqrt{\mu/\epsilon}\,(1 + j\sigma/2\omega\epsilon)$; many wavelengths, $\tau\approx\sigma/2\omega\epsilon$ rad.
> - **Good conductor**, $\sigma\gg\omega\epsilon$: $\gamma\approx(1 + j)\sqrt{\pi f\mu\sigma}$, $\eta\approx\sqrt{\omega\mu/\sigma}\,e^{j\pi/4}$; $\alpha\approx\beta$, gone within a wavelength, $\tau\approx45^\circ$.
> - **Perfect conductor**, $\sigma\to\infty$: $\alpha\to\infty$, $\eta\to0$; no field inside.

> [!derivation]- Where the two shortcuts come from (the notes' route)
> $\sigma + j\omega\epsilon = j\omega\epsilon\,(1 - j\sigma/\omega\epsilon)$, so
> $$
> \begin{gathered}
> \gamma = j\omega\sqrt{\mu\epsilon}\,\Big(1 - j\frac{\sigma}{\omega\epsilon}\Big)^{1/2},\\[6pt]
> \eta = \sqrt{\frac\mu\epsilon}\,\Big(1 - j\frac{\sigma}{\omega\epsilon}\Big)^{-1/2} .
> \end{gathered}
> $$
> **Imperfect dielectric** ($\sigma/\omega\epsilon\ll1$): $(1 + a)^n\approx1 + na$ for $\lvert a\rvert\ll1$, $n = \tfrac12$ for $\gamma$, $n = -\tfrac12$ for $\eta$:
> $$
> \begin{gathered}
> \gamma\approx j\omega\sqrt{\mu\epsilon}\Big(1 - j\frac{\sigma}{2\omega\epsilon}\Big) = \frac\sigma2\sqrt{\frac\mu\epsilon} + j\omega\sqrt{\mu\epsilon},\\[6pt]
> \eta\approx\sqrt{\frac\mu\epsilon}\Big(1 + j\frac{\sigma}{2\omega\epsilon}\Big)\approx\sqrt{\frac\mu\epsilon}\,e^{j\sigma/2\omega\epsilon} .
> \end{gathered}
> $$
> Errors are of order $(\sigma/\omega\epsilon)^2$; the notes' phase $\tan^{-1}(\sigma/2\omega\epsilon)$ agrees to this order.
>
> **Good conductor** ($\sigma/\omega\epsilon\gg1$): drop the 1, so $\gamma^2\approx j\omega\mu\sigma$, $\eta^2\approx j\omega\mu/\sigma$, and $\sqrt j = e^{j\pi/4} = (1 + j)/\sqrt2$:
> $$
> \begin{gathered}
> \gamma\approx(1 + j)\sqrt{\frac{\omega\mu\sigma}{2}} = (1 + j)\sqrt{\pi f\mu\sigma},\\[6pt]
> \eta\approx\sqrt{\frac{j\omega\mu}{\sigma}} = \sqrt{\frac{\omega\mu}{\sigma}}\,e^{j\pi/4} .
> \end{gathered}
> $$
> **Perfect conductor:** $\delta\to0$, $\lvert\eta\rvert\to0$, so any finite surface $\mathbf{H}$ comes with $\mathbf{E} = \eta\mathbf{H}\to0$. The notes defer the proof that $\tilde E_x\to0$ to reflection from conductors.

**Penetration depth against frequency** (fixed material):

- *High* ($\sigma\ll\omega\epsilon$): $\delta\to\dfrac2\sigma\sqrt{\dfrac\epsilon\mu}$, frequency independent, small if $\sigma$ is large.
- *Low* ($\sigma\gg\omega\epsilon$): $\delta\approx\sqrt{\dfrac{2}{\omega\mu\sigma}} = \dfrac{1}{\sqrt{\pi f\mu\sigma}}$, growing as frequency falls: low frequencies get through sea water (numbers and bandwidth cost: Lecture 23).

<!-- fig:lossy-regimes -->

As numbers ($\delta_\infty = (2/\sigma)\sqrt{\epsilon/\mu}$; $x = \omega\epsilon/\sigma$):

| $x = \omega\epsilon/\sigma$ | 0.01 | 0.1 | 1 | 10 | 100 |
|---|---|---|---|---|---|
| $\delta/\delta_\infty$ | 7.11 | 2.35 | 1.10 | 1.001 | 1.000 |
| $\lambda/(2\pi\delta_\infty)$ | 7.04 | 2.13 | 0.455 | 0.050 | 0.005 |
| $\lvert\eta\rvert/\sqrt{\mu/\epsilon}$ | 0.100 | 0.315 | 0.841 | 0.998 | 1.000 |
| $\tau$ | 44.7° | 42.1° | 22.5° | 2.86° | 0.29° |

**Reading the regime from a wave.**

- $\beta\ge\alpha$ (§4): "$\beta$ much smaller than $\alpha$" is impossible.
- Decay per wavelength $e^{-\alpha\lambda} = e^{-2\pi\tan\tau}$: $e^{-2\pi}\approx0.19\,\%$ in a good conductor, $\approx1 - \pi\sigma/\omega\epsilon$ in an imperfect dielectric.
- $\lambda/\delta = 2\pi\alpha/\beta = 2\pi\tan\tau$, so $\lambda<2\pi\delta$ always. Good conductor: $\lambda\approx2\pi\delta$; imperfect dielectric: $\delta\gg\lambda$. "$\lambda$ longer than $\delta$" only means $\sigma/\omega\epsilon>0.33$, which includes the in-between range: not proof of a good conductor.

> [!example] Example — a medium at the crossover, where neither shortcut works
> $\mu = \mu_0$, $\epsilon = 4\epsilon_0$, $\sigma = 0.04$ S/m, $f = 180$ MHz: $\omega\epsilon = 2\pi(1.8\times10^8)(4\times10^{-9}/36\pi) = 0.04$ S/m, $\sigma/\omega\epsilon = 1$ (0.9986 with the exact $\epsilon_0$).
> - **Exact.** $\omega\sqrt{\mu\epsilon} = 2.4\pi = 7.540$ rad/m: $\alpha = (7.540/\sqrt2)\sqrt{\sqrt2 - 1} = 3.43$ Np/m, $\beta = (7.540/\sqrt2)\sqrt{\sqrt2 + 1} = 8.28$ rad/m, $\lvert\eta\rvert = 60\pi/2^{1/4} = 158.5\ \Omega$, $\tau = \tfrac12\tan^{-1}1 = 22.5^\circ$; $\delta = 0.291$ m, $\lambda = 0.758$ m, $v_p = 1.37\times10^8$ m/s.
> - **Imperfect-dielectric shortcut.** $\alpha\approx(\sigma/2)\sqrt{\mu/\epsilon} = 0.02\times60\pi = 3.77$ (10 % high), $\beta\approx7.54$ (9 % low), $\tau\approx0.5$ rad $= 28.6^\circ$.
> - **Good-conductor shortcut.** $\alpha\approx\beta\approx\sqrt{\omega\mu\sigma/2} = 5.33$: $\alpha$ 55 % high, $\beta$ 36 % low, $\tau = 45^\circ$.
>
> Near $\sigma = \omega\epsilon$, use the exact formulas.

## 7. Lecture 19's current sheet in a conducting medium

Put the notes' Lecture 21 sheet, $\mathbf{J}_s = \hat x\,J_0\cos\omega t$ on $z = 0$, in a conducting medium. [[3-maxwell-and-waves/19-dalembert-solutions-and-radiation-from-current-sheets#4-the-same-result-from-boundary-conditions-slides|Lecture 19 §4]]'s argument goes through with $j\beta\to\gamma$:

1. Outgoing waves with the same $\tilde{\mathbf{E}} = \hat x\,Ae^{-\gamma\lvert z\rvert}$ on each face (tangential $\mathbf{E}$ continuous), $\tilde{\mathbf{H}} = \pm\hat y\,(A/\eta)\,e^{-\gamma\lvert z\rvert}$ for $z\gtrless0$.
2. Jump condition ($\hat n = \hat z$): $\hat z\times(\tilde{\mathbf{H}}^+ - \tilde{\mathbf{H}}^-) = \hat z\times\hat y\,(2A/\eta) = -\hat x\,(2A/\eta) = \hat x\,J_0$, so $A = -\eta J_0/2$.

$$
\begin{gathered}
\tilde{\mathbf{E}} = -\hat x\,\frac{\eta J_0}{2}\,e^{-\gamma\lvert z\rvert},\\[6pt]
\tilde{\mathbf{H}} = \mp\hat y\,\frac{J_0}{2}\,e^{-\gamma\lvert z\rvert}\qquad(z\gtrless0).
\end{gathered}
$$

[[3-maxwell-and-waves/19-dalembert-solutions-and-radiation-from-current-sheets|Lecture 19]]'s $\tilde{\mathbf{H}} = \tfrac12\tilde{\mathbf{J}}_s\times\hat n$, $\tilde{\mathbf{E}} = -\tfrac\eta2\tilde{\mathbf{J}}_s$, with $e^{-j\beta\lvert z\rvert}\to e^{-\gamma\lvert z\rvert}$ and complex $\eta$.

> [!example] Example — the sheet in the medium of the §5 example
> $\gamma = 1 + j3$ m⁻¹, $\eta = 119.2\,e^{j18.4^\circ}\ \Omega$, $\omega = 3\times10^8$ rad/s, $J_0 = 2$ A/m (the notes' Lecture 21 value):
> $$
> \begin{gathered}
> \mathbf{H} = \mp\hat y\,e^{-\lvert z\rvert}\cos(\omega t - 3\lvert z\rvert)\ \ \text{A/m},\\[4pt]
> \mathbf{E} = -\hat x\,119.2\,e^{-\lvert z\rvert}\cos(\omega t - 3\lvert z\rvert + 18.4^\circ)\ \ \text{V/m}
> \end{gathered}
> $$
> ($z$ in m). Unlike the lossless sheet, both waves fade (by $e$ per metre). $\mathbf{H}$ is still set by the current alone ($\tfrac12J_0 = 1$ A/m at the sheet); the medium sets $\mathbf{E}$, which leads $\mathbf{H}$ by $\tau = 18.4^\circ$ and so is no longer exactly opposite $\mathbf{J}_s$. The power the current gives up, $\langle-\mathbf{J}_s\cdot\mathbf{E}\rangle = \tfrac12\text{Re}\{-\tilde{\mathbf{J}}_s\cdot\tilde{\mathbf{E}}^*\} = \tfrac14J_0^2\,\text{Re}\{\eta\} = 36\pi\approx113$ W/m², carries $\cos\tau$ ($\text{Re}\{\eta\} = \lvert\eta\rvert\cos\tau$); half, 56.5 W/m², enters each side and becomes heat within a few metres. Direction, $z>0$: $(-\hat x)\times(-\hat y) = +\hat z$, away from the sheet ✓.

## 8. When the conductivity depends on frequency

The Drude conductivity ([[1-electrostatics/11-lorentz-drude-models-for-conductivity-and-susceptibility#3-ac-conductivity-when-the-carriers-cannot-keep-up|Lecture 11 §3]]):

$$
\sigma(\omega) = \frac{Nq^2}{m(\nu + j\omega)} = \frac{\sigma_{\text{DC}}}{1 + j\omega/\nu} .
$$

$\gamma$, $\eta$ still follow from $\sigma(\omega) + j\omega\epsilon$, but $\text{Re}\{\gamma/\eta\}$ and $\text{Im}\{\gamma/\eta\}/\omega$ give only *effective* $\sigma$, $\epsilon$: an imaginary part of $\sigma$ looks exactly like a change in $\epsilon$ ([[concepts/conductivity-and-susceptibility-models]]).

**Metals.** Copper's $\nu\approx4\times10^{13}$ s⁻¹ keeps $\sigma(\omega)$ within $1.6\times10^{-4}$ of DC at 1 GHz: real $\sigma$ is safe here.

**A collisionless plasma** ($\nu\to0$, the ionosphere). $\sigma = Nq^2/(j\omega m)$ is imaginary; the current lags the field by 90° (inertia) and partly cancels the displacement current,

$$
\sigma + j\omega\epsilon_0 = j\omega\epsilon_0\Big(1 - \frac{\omega_p^2}{\omega^2}\Big),\qquad \omega_p^2 = \frac{Nq^2}{m\epsilon_0},
$$

so $\gamma^2 = -(\omega^2 - \omega_p^2)/c^2$.

- **Above $\omega_p$:** $\gamma = j\sqrt{\omega^2 - \omega_p^2}/c$, no attenuation: the plasma dispersion relation of [[3-maxwell-and-waves/21-monochromatic-waves-and-phasor-notation|Lecture 21]] ([[concepts/dispersion-relation]]) in one line. $\eta = \omega\mu_0/\beta$ is real, above $\eta_0$.
- **Below it:** $\gamma = \sqrt{\omega_p^2 - \omega^2}/c$ is real: decay without spatial oscillation (*evanescent*). $\eta$ is imaginary, so $\mathbf{E}$, $\mathbf{H}$ are 90° apart, carrying no average power. Not loss ($\text{Re}\{\sigma\} = 0$): the plasma reflects (Lecture 25).

$N = 10^{12}$ m⁻³ (daytime ionospheric peak): $f_p\approx9$ MHz ($f_p\approx9\sqrt N$ Hz). At 5 MHz, $\delta = 6.4$ m; at 20 MHz, $\beta = 0.375$ rad/m against vacuum's 0.419 rad/m.

## 9. Connections

**Unit 4, transmission lines** (the site's own): a coax with the lossy filling has $\mathcal{L} = (\mu/2\pi)\ln(b/a)$, $\mathcal{C} = 2\pi\epsilon/\ln(b/a)$, $\mathcal{G} = 2\pi\sigma/\ln(b/a)$. With $\mathcal{L}\mathcal{C} = \mu\epsilon$ ([[2-magnetostatics/15-inductance-magnetic-energy-and-the-potentials|Lecture 15]]) and $\mathcal{G}/\mathcal{C} = \sigma/\epsilon$, its $\sqrt{j\omega\mathcal{L}(\mathcal{G} + j\omega\mathcal{C})}$ is exactly $\gamma$, and $\sqrt{j\omega\mathcal{L}/(\mathcal{G} + j\omega\mathcal{C})} = \eta\ln(b/a)/2\pi$: the same problem.

## 10. Summary

$\partial/\partial t\to j\omega$, $j\omega\epsilon\to\sigma + j\omega\epsilon$; $\gamma\eta = j\omega\mu$, $\gamma/\eta = \sigma + j\omega\epsilon$; $\delta = 1/\alpha$; $\mathbf{H}$ lags by $\tau = \tfrac12\tan^{-1}(\sigma/\omega\epsilon)<45^\circ$; $\alpha/\beta = \tan\tau$. Limits: §6.

Concept pages: [[concepts/propagation-constant]] · [[concepts/intrinsic-impedance]] · [[concepts/phasors]] · [[concepts/loss-tangent]] · [[concepts/skin-depth]] · [[concepts/dispersion-relation]] · [[concepts/plane-waves]] · [[concepts/wave-equation]] · [[concepts/maxwells-equations]] · [[concepts/displacement-current]] · [[concepts/conductivity-and-susceptibility-models]].

> [!exam] On exams
> One of the most reliably examined parts of Exam 3.
> 1. **Decode a damped wave** (§5 recipe). SP17 Exam 3 #3: $\mathbf{E} = 3e^{-3x}\cos(8\pi10^6t - 4x + 60^\circ)\,\hat z$ V/m, non-magnetic: every constant ($\gamma$ in both forms, $\lambda$, $f$, $v_p$, $\lvert\eta\rvert$, $\tau$), then $\mathbf{H}$ with direction. Summer 2018 HE3 #1b: time-domain $\mathbf{H}$ ($\mu_0$) to $\epsilon$ and both phasors. SP19 Exam 3 #1: phasor $\tilde{\mathbf{E}}$, $\mu = 2\mu_0$, to $\tilde{\mathbf{H}}$, $\sigma/\omega\epsilon$, regime. The [[problems/decoding-a-damped-wave|worked problem]] does it with $-x$ travel and $\mu = 3\mu_0$.
> 2. **γ and η from one field.** SP18 Exam 3 #2a–c, lossless: $\gamma = j\beta$, $\eta = \omega\mu/\beta$ from $\eta\gamma = j\omega\mu$.
> 3. **Regime reasoning** (§6). Summer 2020 HE3 #3a: can $\beta\ll\alpha$ at high frequency? Summer 2019 HE3 conflict #3b: $\delta\gg\lambda$, inequality on $\omega$.
> 4. **Given aids.** Stems print $\gamma\eta = j\omega\mu$, $\gamma/\eta = \sigma + j\omega\epsilon$, sometimes $\gamma$, $\eta$. Numbers land on 3-4-5 and 30-60-90 triangles ($\tan^{-1}(4/3) = 53^\circ$, $1 + j\sqrt3 = 2e^{j60^\circ}$), as in §5.
> 5. **Recurring traps.** $\mu\neq\mu_0$; the sign of $\tau$ in $\mathbf{H}$; Np/m against rad/m; 60° against $\pi/3$; travel along $x$ or $y$ (use $\hat u\times\tilde{\mathbf{E}}$).

> [!tip] Practice this lecture
> [[practice/22-damped-waves-in-conducting-media|12 practice problems]] — 5 easy, 3 medium, 4 hard — each with a folded hint and a worked solution. Start with [[practice/22-damped-waves-in-conducting-media#221-phasor-maxwell-true-or-false|22.1 Phasor Maxwell, true or false]]; the [[practice/index|practice hub]] has the whole bank by difficulty and by topic.

### Sources for this page
Kudeki notes, Lecture 22 (8 pp.): $\partial/\partial t\to j\omega$ and the margin Maxwell sets; the lossless derivation; the replacement, boxed $\gamma$, $\eta$ and margin formulas; the damped wave, $v_p$ as node speed; the four cases by binomial expansion; penetration-depth limits; the snapshot figure (redrawn). No slides were available. Rao (2009) §§5.3–5.4: closed forms for $\alpha$, $\beta$; the neper; the sheet in a material medium; dispersion. This site's own: the continuity row, divergence and $\tilde\rho$ arguments, readings of $\sigma + j\omega\epsilon$, angle identities, recipe, traps, every example (checked by `verify_L22.py`), the plasma section, the transmission-line twin, all figures. Slips in the course material: see [[0-toolkit/04-errata-in-the-course-materials|errata]].
