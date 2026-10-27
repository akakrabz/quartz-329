---
title: "HW8 — waves in free space: methods, parallel examples, infographics"
description: "FA26 Homework 8 (Lectures 20–22): the method for each of problems 1–4 with a fully worked parallel example on different numbers, and the two AI-generated infographics for problem 5 with the prompts that produced them. Final answers to the graded problems are withheld until the deadline."
tags: [homework, waves]
---

*Companion to FA26 HW8 (reading: Kudeki Lectures 20–22). Problems 1–4 are graded, so this page gives the **method** and a **parallel example with different numbers**, not the answers; they will be added after the deadline. Problem 5 asks for AI-generated infographics: both are below, with the prompts used. Pages to have open: [[3-maxwell-and-waves/18-the-wave-equation-and-plane-tem-waves|Lecture 18]] · [[3-maxwell-and-waves/19-dalembert-solutions-and-radiation-from-current-sheets|Lecture 19]] · [[3-maxwell-and-waves/20-poynting-theorem-and-monochromatic-waves|Lecture 20]] · [[3-maxwell-and-waves/21-monochromatic-waves-and-phasor-notation|Lecture 21]].*

## 1. Reading a medium off a pair of fields

**What is asked.** A TEM wave in a lossless medium is given as $\mathbf{E}$ (an $\hat x$ step plus an unknown $\hat y$ waveform) and $\mathbf{H}$ (two components). Find $\eta$, $v$, $\epsilon_r$, $\mu_r$ and the unknown waveform $g$.

**Method.**
1. **Speed from the argument.** $u(t - z/v)$ travels toward $+z$ at $v$; read $v$ off the coefficient of $z$.
2. **$\eta$ from a matched pair.** For a $+z$ wave, $\hat x E$ pairs with $+\hat y H$ and $\hat y E$ with $-\hat x H$ (check: $\mathbf{E}\times\mathbf{H}$ must point along $+\hat z$). The ratio of the paired amplitudes is $\eta$: $H_y = E_x/\eta$.
3. **Two equations for two unknowns.** $v = c/\sqrt{\mu_r\epsilon_r}$ gives $\mu_r\epsilon_r$; $\eta = \eta_0\sqrt{\mu_r/\epsilon_r}$ gives $\mu_r/\epsilon_r$. Multiply and divide.
4. **The unknown waveform.** The other pair gives $E_y = -\eta H_x$; rewrite the $H_x$ expression so its argument is $t - z/v$, and read $g$ off it.

> [!example] Parallel example (different numbers)
> $\mathbf{E} = \hat x\,u(t - 3z/c) + \hat y\,g(t - 3z/c)$ V/m, $\mathbf{H} = \hat x\,(60z/c - 20t) + \hat y\,\tfrac{1}{40\pi}u(t - 3z/c)$ A/m.
> 1. $v = c/3$.
> 2. $H_y = E_x/\eta \Rightarrow \eta = 40\pi\ \Omega$.
> 3. $\mu_r\epsilon_r = 9$ and $\mu_r/\epsilon_r = (40\pi/120\pi)^2 = 1/9$, so $\epsilon_r = 9$, $\mu_r = 1$.
> 4. $60z/c - 20t = -20\,(t - 3z/c)$, so $E_y = -\eta H_x = 800\pi\,(t - 3z/c)$ V/m and $g(t) = 800\pi\,t$. Check: $\hat y\times(-\hat x) = +\hat z$. ✓

**Trap.** The sign in step 4: $\hat y E$ needs $-\hat x H$ for $+z$ travel, so a $+\hat x H_x$ expression that is itself negative is the normal case, not a contradiction.

## 2. A pulsed current sheet: fields, plots, radiated energy

**What is asked.** $\mathbf{J}_s(t)$ is a short ramp-shaped pulse on $z = 0$ in free space. Write $\mathbf{E}(z,t)$ and $\mathbf{H}(z,t)$ on both sides, plot records at $z = \pm z_0$ and a snapshot at one instant, and find the energy radiated per unit area.

**Method.** ([[concepts/current-sheet-radiation]])
1. **Fields.** $\mathbf{E} = -\tfrac{\eta_0}{2}\mathbf{J}_s(t - \lvert z\rvert/c)$ on both sides; $\mathbf{H} = \tfrac12\mathbf{J}_s(t - \lvert z\rvert/c)\times\hat n$ with $\hat n = \pm\hat z$ pointing away from the sheet, so $\mathbf{H}$ flips sign across it.
2. **A record at $z_0$** is the source waveform delayed by $\lvert z_0\rvert/c$ (5 µs per 1500 m), scaled by $-\eta_0/2$ for $E$ and $\pm\tfrac12$ for $H$. A `rect` of width $\tau$ centred on $t = 0$ turns on at $-\tau/2$, so part of the pulse is at *negative* delayed time.
3. **A snapshot at $t_0$** is the waveform laid out in $\lvert z\rvert$ with $z = c(t_0 - t')$: the earliest part of the pulse is farthest out, on both sides, mirror-symmetric.
4. **Energy per area.** The sheet injects $-\mathbf{J}_s\cdot\mathbf{E} = \tfrac{\eta_0}{2}\lvert J_s\rvert^2$ per unit area ([[3-maxwell-and-waves/20-poynting-theorem-and-monochromatic-waves#4-the-integral-form-a-ledger-for-any-volume|Lecture 20 §4]]); integrate it over the pulse. Half goes each way. Keep the units: $(\text{A/m})^2\cdot\Omega\cdot\text{s} = \text{J/m}^2$.

> [!example] Parallel example
> $\mathbf{J}_s = \hat x\,3t\,\text{rect}(t/\tau)$ A/m, $\tau = 4$ µs.
> 1. $\mathbf{E} = -\hat x\,60\pi\,\cdot3(t - \lvert z\rvert/c)\,\text{rect}\!\big((t - \lvert z\rvert/c)/\tau\big)$; $\mathbf{H} = \mp\hat y\,\tfrac32(t - \lvert z\rvert/c)\,\text{rect}(\cdots)$ for $z\gtrless0$ (from $\hat x\times\hat z = -\hat y$).
> 4. $W = \tfrac{\eta_0}{2}\int_{-\tau/2}^{\tau/2}9t^2\,dt = 60\pi\cdot9\cdot\tau^3/12 = 9.05\times10^{-15}$ J/m².

**Trap.** $\text{rect}(t/\tau)$ is centred on $t = 0$; the pulse starts at $-\tau/2$, so at $z_0$ the record starts at $z_0/c - \tau/2$.

## 3. A monochromatic wave in a dielectric: parameters, H, Poynting

**What is asked.** $\mathbf{E} = \cos(\omega t + \beta z)\,\hat y$ in a perfect dielectric with a given $\epsilon_r$, phase speed and frequency: $\mu_r$, $\eta$, $\lambda$, $\beta$, $\mathbf{H}$, the instantaneous $\mathbf{S}$ on two planes at one instant, and whether the field energy between the planes is growing or shrinking.

**Method.**
1. $v_p = c/\sqrt{\mu_r\epsilon_r}$ gives $\mu_r$; then $\eta = \eta_0\sqrt{\mu_r/\epsilon_r}$.
2. $\lambda = v_p/f$; $\beta = 2\pi/\lambda = \omega/v_p$.
3. Direction: $(\omega t + \beta z)$ travels toward $-z$, so $\hat u = -\hat z$ and $\mathbf{H} = \tfrac1\eta\hat u\times\mathbf{E}$. Write the cross product out.
4. $\mathbf{S} = \mathbf{E}\times\mathbf{H} = \tfrac{1}{\eta}\cos^2(\omega t + \beta z)\,\hat u$. Evaluate the phase at the stated $t$ and $z$; multiples of $\pi$ make $\cos^2$ equal 1 or 0.
5. **Energy balance of the slab:** $-dW/dt = \oint\mathbf{S}\cdot d\mathbf{A}$ ([[concepts/poynting-theorem]]). With $\mathbf{S}$ along $-\hat z$, power enters the slab through its $+z$ face and leaves through its $-z$ face. If more enters than leaves, the field energy inside is growing.

> [!example] Parallel example
> $\mathbf{E} = \cos(\omega t - \beta z)\,\hat x$ V/m, $\epsilon = 2\epsilon_0$, $v_p = c/2$, $f = 150$ MHz.
> 1. $\mu_r\epsilon_r = 4 \Rightarrow \mu_r = 2$; $\eta = \eta_0\sqrt{2/2} = 120\pi\ \Omega$.
> 2. $\lambda = 1.5\times10^8/1.5\times10^8 = 1$ m; $\beta = 2\pi$ rad/m.
> 3. $+z$ travel: $\mathbf{H} = \tfrac{1}{120\pi}\hat z\times\hat x\cos(\cdots) = \hat y\,\tfrac{1}{120\pi}\cos(\omega t - \beta z)$ A/m.
> 4. At $t = 5$ ns, $\omega t = 1.5\pi$. On $z = 0.25$ m: $\beta z = 0.5\pi$, $\cos^2(\pi) = 1$, $\mathbf{S} = \hat z/(120\pi) = 2.65\,\hat z$ mW/m². On $z = 0.5$ m: $\beta z = \pi$, $\cos^2(0.5\pi) = 0$, $\mathbf{S} = 0$.
> 5. Between $z = 0.25$ and $0.5$ m: power enters at $z = 0.25$, none leaves at $z = 0.5$ → the stored energy is increasing at that instant.

**Trap.** $\mathbf{S}$ is instantaneous here: $\cos^2$, not $\tfrac12$. The $\tfrac12$ belongs to the time average only.

## 4. Five waves: partner field, phasors, instantaneous and average power

**What is asked.** For each given $\mathbf{E}$ or $\mathbf{H}$ in free space: the partner field, both phasors, the instantaneous power through 1 m² facing the wave, and its time average.

**Method.** (every step on [[3-maxwell-and-waves/21-monochromatic-waves-and-phasor-notation|Lecture 21]])
1. **Direction** from the sign between $\omega t$ and the position term; $\hat u$ is along that axis.
2. **Partner field:** $\mathbf{H} = \tfrac{1}{\eta_0}\hat u\times\mathbf{E}$ or $\mathbf{E} = \eta_0\,\mathbf{H}\times\hat u$, component by component, keeping each component's own phase. $\eta_0 = 120\pi\ \Omega$.
3. **Phasors:** write every component as a cosine first ($\sin\theta = \cos(\theta - \pi/2)$), then $A\cos(\omega t \mp \beta z + \phi)\to Ae^{j\phi}e^{\mp j\beta z}$. A sine picks up $-j$.
4. **Instantaneous power through 1 m²:** $\mathbf{S}\cdot\hat u$ with $\mathbf{S} = \mathbf{E}\times\mathbf{H}$. With two perpendicular components, $S = (E_1^2 + E_2^2)/\eta_0$: a sum of two $\cos^2$ terms with their own phases. For a circular wave it is constant in time.
5. **Average:** $\tfrac12\text{Re}\{\tilde{\mathbf{E}}\times\tilde{\mathbf{H}}^*\}\cdot\hat u = (\lvert\tilde E_1\rvert^2 + \lvert\tilde E_2\rvert^2)/2\eta_0$, which must equal the time average of step 4.

> [!example] Parallel example
> $\mathbf{H} = 2\cos(\omega t + \beta z)\,\hat x + 2\sin(\omega t + \beta z)\,\hat y$ A/m, free space.
> 1. $\hat u = -\hat z$.
> 2. $\mathbf{E} = \eta_0\mathbf{H}\times(-\hat z)$: $\hat x\times(-\hat z) = +\hat y$, $\hat y\times(-\hat z) = -\hat x$, so $\mathbf{E} = 240\pi\cos(\cdots)\,\hat y - 240\pi\sin(\cdots)\,\hat x$ V/m.
> 3. $\tilde{\mathbf{H}} = (2\hat x - 2j\hat y)e^{+j\beta z}$; $\tilde{\mathbf{E}} = (2j\hat x + 2\hat y)\,120\pi\,e^{+j\beta z}$.
> 4. $\mathbf{S}\cdot\hat u = \eta_0(4\cos^2 + 4\sin^2) = 4\eta_0 = 1508$ W/m², constant (circular polarization).
> 5. $\tfrac12\text{Re}\{\tilde E_x\tilde H_y^* - \tilde E_y\tilde H_x^*\} = -1508$ W/m² along $\hat z$, i.e. $1508$ W/m² along $\hat u$. ✓

**Traps.** $e^{+j\beta z}$ means travel toward $-z$. The phase constant of a sine component ($-\pi/2$) adds to any phase already written in its argument.

## 5. Generative-AI infographics: wave propagation in free space

The assignment asks for two beginner-friendly infographics made with a generative-AI tool, then a critical evaluation. Both infographics below were generated in this chat (Claude, model `claude-fable-5-1`, via Claude Code, 22 October 2026) as SVG figures for this site; the prompts are quoted after each one. **The evaluation (parts c–e) is yours**: the figures are the AI's best attempt, not a checked reference, and nothing on this page says what is right or wrong in them.

### Version A — a reference poster

<!-- fig:info-wave-anatomy -->

> [!quote] Prompt A
> Create a beginner-friendly, comprehensive one-page reference poster titled 'Anatomy of a plane wave' on wave propagation in free space. Show one large labelled diagram of an x-polarized plane wave travelling toward +z (E along x, H along y, E×H along z, wavelength marked), a panel of the key relations (wave equation, f(t − z/c) and how to read the direction, c = 1/√(μ₀ε₀), η₀ = √(μ₀/ε₀) = 377 Ω, H = ẑ×E/η₀, λ = c/f, β = 2π/λ = ω/c, Poynting vector and its time average), a strip of SI units, and a boxed worked example at 100 MHz with E₀ = 3 V/m giving λ, β, H₀, ⟨S⟩ and the full E and H expressions. Clean technical poster style, every quantity labelled.

### Version B — a wave's journey

<!-- fig:info-wave-journey -->

> [!quote] Prompt B
> Make a friendly, story-style infographic for a first-year student called 'From antenna to receiver: a wave's journey'. Use four numbered stops with small sketches: (1) a current sheet or antenna launches the wave and the field opposes the current (E = −η₀Jₛ/2), (2) it travels at c = 3×10⁸ m/s with a delay z/c ('300 m per microsecond'), (3) it carries power, ⟨S⟩ = E₀²/2η₀, spreading as 1/r² from an isotropic source, (4) a receiver reads it with H = E/η₀ and the direction read from the sign in (t − z/c). Tell one worked example as a story: a 50 kW isotropic transmitter heard 10 km away (power density, E₀, H₀, delay). End with a short 'common mistakes' strip. Use a different layout, colours and typography from a formula poster.

> [!tip] For your report
> Platform and model: Claude (Anthropic), model `claude-fable-5-1`, run through Claude Code; screenshot this page and the chat for the history. For part (c), check every equation and number against [[3-maxwell-and-waves/18-the-wave-equation-and-plane-tem-waves|Lecture 18]], [[3-maxwell-and-waves/20-poynting-theorem-and-monochromatic-waves|Lecture 20]] and [[0-toolkit/03-units-and-constants|the units table]], and recompute the worked example by hand.
