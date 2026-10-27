---
title: "Lecture 21 — Monochromatic waves and phasor notation"
description: "A single-frequency wave A cos(ωt ∓ βz) has period T = 2π/ω, wavelength λ = 2π/β and phase velocity vₚ = ω/β = λf, and its dispersion relation β(ω) carries the physics of each kind of wave. As a phasor it is Ẽ = E₀e^(∓jβz) x̂: a sine picks up −j, d/dt becomes jω, H̃ is Ẽ divided by η and rotated, and ⟨S⟩ = ½Re{Ẽ × H̃*}."
tags: [lecture, waves]
lecture: 21
---

*Lecture 21 · course notes §21 · **slides: not yet available — this page is built from the course notes** · prev: [[3-maxwell-and-waves/20-poynting-theorem-and-monochromatic-waves|Lecture 20]] · next: [[3-maxwell-and-waves/22-phasor-maxwell-equations-and-damped-waves|Lecture 22]] · worked problem: [[problems/phasors-e-and-power-from-a-given-h|Phasors, E and power from a given H]] · practice: [[practice/21-phasors-and-monochromatic-waves|12 problems]]*

> [!abstract] In one breath
> [[3-maxwell-and-waves/19-dalembert-solutions-and-radiation-from-current-sheets|Lecture 19]]'s sheet radiates the **monochromatic** wave $\cos(\omega t\mp\beta z)$: $T = 2\pi/\omega$, $\lambda = 2\pi/\beta$, $v_p = \omega/\beta = \lambda f$; its **dispersion relation** $\beta(\omega)$ holds the physics. **Phasors**, $a(t) = \text{Re}\{\tilde Ae^{j\omega t}\}$, make calculus algebra: sine → $-j$, $d/dt\to j\omega$, $+z$ travel is $e^{-j\beta z}$, $\tilde{\mathbf{H}}$ is $\tilde{\mathbf{E}}/\eta$ rotated, $\langle\mathbf{S}\rangle = \tfrac12\text{Re}\{\tilde{\mathbf{E}}\times\tilde{\mathbf{H}}^*\}$.

## 1. Monochromatic waves: one frequency, two periodicities

[[3-maxwell-and-waves/18-the-wave-equation-and-plane-tem-waves|Lecture 18]]'s waves $f(t\mp z/v)$ are, by Fourier analysis, sums of cosines. With $f(t) = A\cos(\omega t)$:

$$
\begin{gathered}
A\cos\Big[\omega\Big(t\mp\frac zv\Big)\Big] = A\cos(\omega t\mp\beta z),\\[4pt]
\beta\equiv\frac{\omega}{v} = \omega\sqrt{\mu\epsilon}\ \ [\text{rad/m}].
\end{gathered}
$$

Also *co-sinusoidal* (exams), *time-harmonic* (notes). $\beta$: the notes' **wave-number** (twin of the **wave-frequency** $\omega$), Rao's *phase constant*, physics' $k$. The wave repeats each $2\pi$ of $\omega t$ and of $\beta z$: $\beta$ is a *spatial* frequency, as in image processing.

> [!key] Period, wavelength and phase velocity
> $$
> \begin{gathered}
> \text{fixed } z:\quad T = \frac{2\pi}{\omega} = \frac1f\quad\text{(period, s)},\\[4pt]
> \text{fixed } t:\quad \lambda = \frac{2\pi}{\beta}\quad\text{(wavelength, m)},\\[4pt]
> v_p = \frac{\omega}{\beta} = \frac{\lambda}{T} = \lambda f\quad\text{(phase velocity, m/s)}.
> \end{gathered}
> $$
> Constant phase $\omega t - \beta z = \phi_0$ sits at $z = (\omega t - \phi_0)/\beta$: speed $\omega/\beta$, one wavelength per period. Perfect dielectric: $v_p = 1/\sqrt{\mu\epsilon}$ at every frequency. Notes: $v$; here $v_p$, since §2 meets other speeds.

<!-- fig:phas-snapshot-record -->

> [!example] Example — everything from one expression (this site's numbers)
> Lossless, non-magnetic: $\mathbf{E} = 12\cos\big(4\pi\times10^8\,t - \tfrac{8\pi}{3}\,y\big)\,\hat z$ V/m.
> - $f = 200$ MHz, $T = 5$ ns; $\beta = 8\pi/3\approx8.38$ rad/m, $\lambda = 0.75$ m.
> - Opposite signs: toward $+y$ ([[3-maxwell-and-waves/18-the-wave-equation-and-plane-tem-waves#6-reading-a-wave|Lecture 18 §6]]); $v_p = \omega/\beta = \lambda f = 1.5\times10^8$ m/s $= c/2$.
> - $\sqrt{\mu_r\epsilon_r} = c/v_p = 2$; only "non-magnetic" gives $\epsilon_r = 4$, $\eta = \eta_0/\sqrt{\epsilon_r} = 60\pi\approx188\ \Omega$.
> - Probes 25 cm apart along $y$: downstream lags $\beta\,\Delta y = 2\pi/3$ (120°): $\Delta y/v_p = 1.67$ ns $= T/3$.

**The spectrum (notes p. 4).** The chart's frequency bar is schematic; compute $f = c/\lambda$:

| band | wavelength on the chart | $f = c/\lambda$ |
|---|---|---|
| radio | $10^3$ m | 300 kHz |
| microwave | $10^{-2}$ m | 30 GHz |
| infrared | $10^{-5}$ m | 30 THz |
| visible | $0.5\times10^{-6}$ m | 600 THz |
| ultraviolet | $10^{-8}$ m | $3\times10^{16}$ Hz |
| X-ray | $10^{-10}$ m | $3\times10^{18}$ Hz |
| gamma ray | $10^{-12}$ m | $3\times10^{20}$ Hz |

Memorize: 1 MHz ↔ 300 m, 100 MHz ↔ 3 m, 1 GHz ↔ 30 cm, 10 GHz ↔ 3 cm; visible 400 nm (750 THz, violet) to 700 nm (430 THz, red). Radio and visible pass the atmosphere.

## 2. Dispersion relations and phase velocity

Any 1D wave has solutions $A\cos(\omega t\mp\beta z)$; its physics is the **dispersion relation** $\beta(\omega)$.

> [!key] Three dispersion relations (notes)
> | wave | dispersion relation | phase velocity $\omega/\beta$ |
> |---|---|---|
> | TEM wave in a perfect dielectric | $\beta = \omega\sqrt{\mu\epsilon}$ | $1/\sqrt{\mu\epsilon}$ at every $\omega$ |
> | sound in a monatomic gas | $\beta = \omega\sqrt{\dfrac{m}{\frac53k_BT}}$ | $\sqrt{5k_BT/3m}$ at every $\omega$ |
> | TEM wave in a collisionless plasma | $\beta = \dfrac1c\sqrt{\omega^2 - \omega_p^2}$ | $\dfrac{c}{\sqrt{1 - \omega_p^2/\omega^2}}$, faster than $c$ |
>
> $T$: temperature; $m$: atomic mass (row 2), electron mass (row 3); $k_B = 1.381\times10^{-23}$ J/K. **Plasma frequency** $\omega_p = \sqrt{Ne^2/(m\epsilon_0)}$, $N$ electrons/m³ of charge $-e$. Rows 1–2 **non-dispersive** ($v_p$ independent of $\omega$: pulses keep their shape, [[3-maxwell-and-waves/18-the-wave-equation-and-plane-tem-waves#4-the-1d-wave-equation-and-its-solutions|Lecture 18 §4]]); row 3 **dispersive**.

**Gas.** $\tfrac53 = \gamma$ (adiabatic: too fast for heat to flow). This site's $v_p$ checks: helium 1019 m/s, argon 323 m/s at 300 K; 1007 and 319 m/s at 20 °C (tabulated). Diatomic air, $\gamma = \tfrac75$: 343 m/s at 20 °C (375 with $\tfrac53$). 440 Hz: $\lambda = 2.32$ m (He), 0.73 m (Ar); $v_p\propto1/\sqrt m$, ratio $\sqrt{39.95/4.003} = 3.16$.

**Plasma** (ionosphere, 50–1000 km): $f_p\approx8.98\sqrt{N}$ Hz; daytime $N\sim10^{12}$ m⁻³ gives $f_p\approx9$ MHz.

- **$\omega>\omega_p$:** 10 MHz, $f_p = 8.98$ MHz: $\beta = 0.0922$ rad/m, $\lambda = 68.1$ m (30.0 m in vacuum), $v_p = 6.81\times10^8$ m/s $= 2.27c$.
- **$\omega\gg\omega_p$:** 100 MHz: $v_p = 1.004c$; FM and satellite links pass.
- **$\omega<\omega_p$:** $\beta^2<0$, no travelling wave; waves are turned back (shortwave hops around the Earth).

$v_p>c$ breaks nothing: a pure cosine carries no message. Signals travel at the [[concepts/group-velocity|group velocity]] $v_g = d\omega/d\beta$, in the plasma $c\sqrt{1 - \omega_p^2/\omega^2}<c$ ($0.440c$ at 10 MHz; $v_pv_g = c^2$); [[3-maxwell-and-waves/24-signal-transmission-and-circular-polarization|Lecture 24]]; no paper on hand asks for $v_g$. Non-dispersive: $v_g = v_p$.

<!-- fig:phas-dispersion-diagram -->

> [!derivation]- Where the plasma relation comes from (this site's derivation, using Lecture 11)
> [[1-electrostatics/11-lorentz-drude-models-for-conductivity-and-susceptibility|Lecture 11]]'s collisionless Drude equation $m\,dv_x/dt = -eE_x$, $J_x = -Nev_x$:
> $$
> \frac{\partial J_x}{\partial t} = \frac{Ne^2}{m}E_x .
> $$
> Into $\nabla\times\nabla\times\mathbf{E} = -\mu_0\,\partial_t\big(\mathbf{J} + \epsilon_0\,\partial_t\mathbf{E}\big)$; a transverse wave has $\nabla\cdot\mathbf{E} = 0$, so the left side is $-\nabla^2\mathbf{E}$:
> $$
> \frac{\partial^2E_x}{\partial z^2} = \mu_0\frac{Ne^2}{m}E_x + \mu_0\epsilon_0\frac{\partial^2E_x}{\partial t^2}.
> $$
> $E_x = E_0\cos(\omega t - \beta z)$:
> $$
> \begin{gathered}
> -\beta^2 = \mu_0\frac{Ne^2}{m} - \frac{\omega^2}{c^2}\ \Longrightarrow\ \beta^2 = \frac{\omega^2 - \omega_p^2}{c^2},\\[4pt]
> \omega_p^2 = \frac{Ne^2}{m\epsilon_0}.
> \end{gathered}
> $$
> Equivalently, $\sigma(\omega) = Ne^2/\big(m(\nu + j\omega)\big)$ at $\nu = 0$, $-jNe^2/(m\omega)$: imaginary, hence lossless (§7).

> [!trap] Speeds and symbols in §2
> - $\omega/\beta$ is the **phase** velocity, not a universal "propagation velocity": in a plasma energy travels at $v_g<c<v_p$.
> - Below $\omega_p$: no travelling wave, not "a slower wave".
> - $\tfrac53$: monatomic gases only; air needs $\tfrac75$.
> - Acoustic $T$ is a temperature, not the period.

## 3. Phasors: a rotating arrow and its shadow

A linear system driven at $\omega$ settles at $\omega$: amplitude plus phase, one complex number.

> [!key] The phasor of a sinusoid
> $$
> \begin{gathered}
> a(t) = A\cos(\omega t + \theta) = \text{Re}\{\tilde A\,e^{j\omega t}\},\\[4pt]
> \tilde A = A\,e^{j\theta}.
> \end{gathered}
> $$
> $\lvert\tilde A\rvert = A$ (**peak**, not rms), $\angle\tilde A = \theta$, cosine reference, no $t$. Euler: $\tilde Ae^{j\omega t} = A\cos(\omega t + \theta) + jA\sin(\omega t + \theta)$.

$\tilde Ae^{j\omega t}$ is an arrow turning counterclockwise at $\omega$; $a(t)$ is its real-axis shadow, $\tilde A$ its $t = 0$ position.

<!-- fig:phas-rotating-arrow -->

> [!key] The complex-number moves this lecture needs
> - $x + jy = re^{j\phi}$, $r = \sqrt{x^2 + y^2}$, $\phi$ in the point's own quadrant: $-4 + 3j$ is at $143.1^\circ$, not $\tan^{-1}(3/(-4)) = -36.9^\circ$.
> - $j = e^{j\pi/2}$ turns $+90^\circ$, $-j = 1/j = e^{-j\pi/2}$ turns $-90^\circ$, $-1 = e^{j\pi}$ half a turn.
> - $(re^{j\phi})^* = re^{-j\phi}$, $zz^* = \lvert z\rvert^2$, $\text{Re}\{z\} = \tfrac12(z + z^*)$, $(r_1e^{j\phi_1})(r_2e^{j\phi_2}) = r_1r_2e^{j(\phi_1 + \phi_2)}$.

**Sines.** $\sin(\omega t + \theta) = \cos(\omega t + \theta - \pi/2)$ → $-jAe^{j\theta}$, a quarter-period lag: $\text{Re}\{-je^{j\omega t}\} = \text{Re}\{-j\cos\omega t + \sin\omega t\} = \sin\omega t$.

> [!key] Time function → phasor
> | time function | phasor |
> |---|---|
> | $A\cos\omega t$ | $A$ |
> | $A\sin\omega t$ | $-jA$ |
> | $-A\cos\omega t$ | $-A$ ($e^{j\pi} = -1$) |
> | $-A\sin\omega t$ | $+jA$ ($(-1)(-j) = j$) |
> | $A\cos(\omega t + \theta)$ | $Ae^{j\theta}$ |
> | $A\sin(\omega t + \theta)$ | $-jAe^{j\theta} = Ae^{j(\theta - \pi/2)}$ |
> | $A\cos(\omega t - \beta z)$ | $Ae^{-j\beta z}$ |
> | $A\sin(\omega t + \beta y)$ | $-jAe^{j\beta y}$ |

**Back:** $a(t) = \lvert\tilde A\rvert\cos(\omega t + \angle\tilde A)$. $(4 - 3j)\,e^{-j\beta z}\hat x$ V/m, $4 - 3j = 5e^{-j36.9^\circ}$: $5\cos(\omega t - \beta z - 36.9^\circ)\,\hat x$ V/m $= 4\cos(\omega t - \beta z) + 3\sin(\omega t - \beta z)$. Slip: $\text{Re}\{\tilde A\}\cos\omega t$ loses the 3.

**Rules.** Linear ($a + b\to\tilde A + \tilde B$, $ka\to k\tilde A$, $k$ real) and unique (compare $t = 0$, $\omega t = \pi/2$): sinusoid equations become phasor equations. Re commutes with $d/dt$:

$$
\begin{aligned}
\frac{d}{dt}\text{Re}\{\tilde Ae^{j\omega t}\} &= \text{Re}\Big\{\tilde A\,\frac{d}{dt}e^{j\omega t}\Big\}\\
&= \text{Re}\big\{(j\omega\tilde A)\,e^{j\omega t}\big\}.
\end{aligned}
$$

$j\omega$: stretch, turn a quarter *forward* (derivatives peak a quarter period early); $\tfrac{d}{dt}\cos\omega t = -\omega\sin\omega t = \text{Re}\{j\omega e^{j\omega t}\}$.

> [!key] Calculus becomes algebra
> $$
> \begin{gathered}
> \frac{da}{dt}\ \leftrightarrow\ j\omega\tilde A,\qquad \int a\,dt\ \leftrightarrow\ \frac{\tilde A}{j\omega},\\[4pt]
> a(t-\tau)\ \leftrightarrow\ \tilde Ae^{-j\omega\tau}.
> \end{gathered}
> $$
> Delay = phase lag $\omega\tau$ (§4). So came ECE 210's $\tilde I = j\omega C\tilde V$ and [[1-electrostatics/11-lorentz-drude-models-for-conductivity-and-susceptibility#3-ac-conductivity-when-the-carriers-cannot-keep-up|Lecture 11 §3]]'s $\sigma(\omega) = Nq^2/\big(m(\nu + j\omega)\big)$.

**No phasor for products:** $\cos^2\omega t = \tfrac12 + \tfrac12\cos2\omega t$, so $\text{Re}\{\tilde A\tilde Be^{j\omega t}\}\neq a(t)b(t)$; power needs §7.

**Vector phasors**, $\tilde{\mathbf{E}} = \tilde E_x\hat x + \tilde E_y\hat y + \tilde E_z\hat z$ (complex components, real unit vectors):
$$
\mathbf{E}(\mathbf{r}, t) = \text{Re}\{\tilde{\mathbf{E}}(\mathbf{r})\,e^{j\omega t}\}.
$$
The notes' example; $e^{\mp j\beta z}$ is the phase at each position:
$$
\begin{gathered}
\mathbf{E} = E_0\cos(\omega t\mp\beta z)\,\hat x\ \ [\text{V/m}]\\[2pt]
\updownarrow\\[2pt]
\tilde{\mathbf{E}} = E_0e^{\mp j\beta z}\,\hat x\ \ [\text{V/m}],
\end{gathered}
$$

> [!trap] Mixing the two domains
> Not "$\mathbf{E}(z, t) = 5e^{-j\beta z}\hat x$" but $\tilde{\mathbf{E}}(z) = 5e^{-j\beta z}\hat x$ or $5\cos(\omega t - \beta z)\,\hat x$: no $t$ in phasors, nothing complex in fields.

## 4. Plane-wave phasors and the direction-of-travel trap

Toward $+z$, $\mathbf{E}(z, t) = \mathbf{E}(0, t - z/v_p)$: delay factor $e^{-j\omega z/v_p} = e^{-j\beta z}$. Toward $-z$: $e^{+j\beta z}$.

> [!key] Plane-wave phasors
> $$
> \begin{gathered}
> \text{toward }{+z}:\ \ \tilde{\mathbf{E}}(z) = \tilde{\mathbf{E}}_0\,e^{-j\beta z},\\[4pt]
> \text{toward }{-z}:\ \ \tilde{\mathbf{E}}(z) = \tilde{\mathbf{E}}_0\,e^{+j\beta z},\\[4pt]
> \text{toward }\hat u:\ \ \tilde{\mathbf{E}}(\mathbf{r}) = \tilde{\mathbf{E}}_0\,e^{-j\beta\,\hat u\cdot\mathbf{r}},\quad \tilde{\mathbf{E}}_0\perp\hat u .
> \end{gathered}
> $$
> Uniform $\lvert\tilde{\mathbf{E}}\rvert$; phase *falls* along the travel. $\tilde{\mathbf{E}}_0$ may be complex ([[3-maxwell-and-waves/24-signal-transmission-and-circular-polarization|Lecture 24]]'s circular polarization).

**The trap.** $e^{+j\beta z}e^{j\omega t} = e^{j(\omega t + \beta z)}$: same signs, toward $-z$. **A minus sign in the exponent means travel toward plus**, toward where the phase lags.

<!-- fig:phas-direction-trap -->

**Any direction, and the exam template.** Wave vector $\beta\hat u$: factor $e^{-j(\beta_xx + \beta_yy + \beta_zz)}$ (Rao §8.1). The template $(A\hat x + B\hat y + C\hat z)\,e^{j(ax + by + cz)}$ has a plus sign:
$$
(a, b, c) = -\beta\,\hat u,\qquad a^2 + b^2 + c^2 = \beta^2:
$$
- Toward $-\hat z$, 450 MHz, non-magnetic, $\epsilon_r = 4$: $\beta = 2\pi f\sqrt{\epsilon_r}/c = 6\pi$ rad/m, $e^{+j6\pi z}$, $(a, b, c) = (0, 0, +6\pi)$ rad/m.
- Toward $(\hat x + \hat y)/\sqrt2$, $\beta = 2\pi$ rad/m: $e^{-j\sqrt2\pi(x + y)}$, $a = b = -\sqrt2\pi\approx-4.44$ rad/m, $c = 0$; amplitude $\perp\hat u$: $\hat z$, $\hat x - \hat y$ or a complex mix.

> [!trap] Reading the direction from a phasor
> - $e^{-j\beta z}$: $+z$; $e^{+j\beta z}$: $-z$. Unsure? Multiply by $e^{j\omega t}$; use Lecture 18's sign rule.
> - Template $(a, b, c)$ points *against* the travel.
> - A front factor ($-j$, $e^{j\pi/3}$, $4 - 3j$) is a phase, not a direction.

## 5. The partner field: divide by η and rotate

Lectures 18–19's $\mathbf{H} = \tfrac1\eta\hat u\times\mathbf{E}$ carries over: real $\eta$, $\hat u$ commute with Re.

> [!key] The Ẽ ↔ H̃ rule (one wave, lossless medium)
> $$
> \begin{gathered}
> \tilde{\mathbf{H}} = \frac1\eta\,\hat u\times\tilde{\mathbf{E}},\qquad \tilde{\mathbf{E}} = \eta\,\tilde{\mathbf{H}}\times\hat u,\\[4pt]
> \tilde{\mathbf{S}}\equiv\tilde{\mathbf{E}}\times\tilde{\mathbf{H}}^* = \frac{\lvert\tilde{\mathbf{E}}\rvert^2}{\eta}\,\hat u .
> \end{gathered}
> $$
> Notes: divide by $\eta$, rotate so $\tilde{\mathbf{S}}$ points along the travel. Complex factors ride along.

**Why the conjugate:** it cancels the shared $e^{-j\beta\hat u\cdot\mathbf{r}}$. With $\mathbf{a}\times(\mathbf{b}\times\mathbf{c}) = \mathbf{b}(\mathbf{a}\cdot\mathbf{c}) - \mathbf{c}(\mathbf{a}\cdot\mathbf{b})$, $\tilde{\mathbf{E}}\cdot\hat u = 0$:
$$
\begin{aligned}
\tilde{\mathbf{E}}\times\tilde{\mathbf{H}}^* &= \frac1\eta\,\tilde{\mathbf{E}}\times\big(\hat u\times\tilde{\mathbf{E}}^*\big)\\
&= \frac1\eta\Big[\hat u\,\big(\tilde{\mathbf{E}}\cdot\tilde{\mathbf{E}}^*\big) - \tilde{\mathbf{E}}^*\big(\tilde{\mathbf{E}}\cdot\hat u\big)\Big] = \frac{\lvert\tilde{\mathbf{E}}\rvert^2}{\eta}\,\hat u .
\end{aligned}
$$
Without it, $\tilde{\mathbf{E}}\times\tilde{\mathbf{H}} = (\tilde{\mathbf{E}}\cdot\tilde{\mathbf{E}}/\eta)\,\hat u$ carries $e^{-2j\beta z}$, flipping sign every quarter wavelength.

> [!derivation]- Why "divide by η" works, from Faraday's law in phasor form
> [[3-maxwell-and-waves/18-the-wave-equation-and-plane-tem-waves#3-the-planar-problem-only-exzt-and-hyzt|Lecture 18 §3]]'s planar curl equations with $\partial/\partial t\to j\omega$:
> $$
> \frac{d\tilde E_x}{dz} = -j\omega\mu\,\tilde H_y,\qquad -\frac{d\tilde H_y}{dz} = j\omega\epsilon\,\tilde E_x .
> $$
> $\tilde E_x = E_0e^{\mp j\beta z}$ gives $d/dz\to\mp j\beta$:
> $$
> \begin{gathered}
> \tilde H_y = \pm\frac{\beta}{\omega\mu}\,\tilde E_x = \pm\frac{\tilde E_x}{\eta},\\[4pt]
> \text{since}\quad \frac{\beta}{\omega\mu} = \frac{\omega\sqrt{\mu\epsilon}}{\omega\mu} = \sqrt{\frac\epsilon\mu} = \frac1\eta .
> \end{gathered}
> $$
> $\pm$ is the direction; the second equation holds as $\beta/\eta = \omega\epsilon$. With $\sigma\neq0$ (Lecture 22), complex $\eta$ shifts $\tilde{\mathbf{H}}$ by $-\angle\eta$.

**The notes' Example 1** (all rows right):

| field | phasor | the check |
|---|---|---|
| $\mathbf{E} = \cos(\omega t + \beta y)\,\hat z$ | $\tilde{\mathbf{E}} = e^{j\beta y}\,\hat z$ | $+j\beta y$: $\hat u = -\hat y$ |
| (its partner) | $\tilde{\mathbf{H}} = -\dfrac{e^{j\beta y}}{\eta}\,\hat x$ | $\tfrac1\eta(-\hat y)\times\hat z = -\tfrac1\eta\hat x$; $\hat z\times(-\hat x) = -\hat y$ ✓ |
| $\mathbf{H} = \sin(\omega t - \beta z)\,\hat y$ | $\tilde{\mathbf{H}} = -je^{-j\beta z}\,\hat y$ | sine → $-j$; $+z$ |
| $\mathbf{E} = \eta\sin(\omega t - \beta z)\,\hat x$ | $\tilde{\mathbf{E}} = -j\eta e^{-j\beta z}\,\hat x$ | $\eta\tilde{\mathbf{H}}\times\hat z$ with $\hat y\times\hat z = \hat x$ |

> [!example] Example 2 (notes) — two waves at once, one rule each
> $\mathbf{H} = \hat xH^+\cos(\omega t - \beta z) + \hat yH^-\sin(\omega t + \beta z)$, real $H^\pm$:
> $$
> \tilde{\mathbf{H}} = \hat xH^+e^{-j\beta z} - j\,\hat yH^-e^{j\beta z}.
> $$
> Each wave **with its own** $\hat u$:
> - $+z$: $\eta H^+e^{-j\beta z}\,(\hat x\times\hat z) = -\hat y\,\eta H^+e^{-j\beta z}$;
> - $-z$: $\eta(-jH^-e^{j\beta z})\,\big(\hat y\times(-\hat z)\big) = \eta(-jH^-e^{j\beta z})(-\hat x) = +j\,\hat x\,\eta H^-e^{j\beta z}$.
>
> $$
> \tilde{\mathbf{E}} = -\hat y\,\eta H^+e^{-j\beta z} + j\,\hat x\,\eta H^-e^{j\beta z},
> $$
> $$
> \begin{aligned}
> \mathbf{E} = &-\hat y\,\eta H^+\cos(\omega t - \beta z)\\
> &- \hat x\,\eta H^-\sin(\omega t + \beta z),
> \end{aligned}
> $$
> as $\text{Re}\{je^{j(\omega t + \beta z)}\} = -\sin(\omega t + \beta z)$. No sign error, despite the notes' invitation (checked numerically); one $\hat u$ for both flips a term.

> [!recipe] From a field to its partner, in phasors
> 1. Convert term by term; group into waves by exponent; read each $\hat u$ (§4).
> 2. Per wave: $\tilde{\mathbf{H}} = \tfrac1\eta\hat u\times\tilde{\mathbf{E}}$ or $\tilde{\mathbf{E}} = \eta\tilde{\mathbf{H}}\times\hat u$.
> 3. Check $\tilde{\mathbf{E}}\times\tilde{\mathbf{H}}^*\parallel+\hat u$, $\lvert\tilde{\mathbf{E}}\rvert/\lvert\tilde{\mathbf{H}}\rvert = \eta$.
> 4. Time domain: $\times e^{j\omega t}$, take Re.

> [!example] Example — the 200 MHz wave of §1
> $\tilde{\mathbf{E}} = 12e^{-j(8\pi/3)y}\,\hat z$ V/m toward $+\hat y$: $\tilde{\mathbf{H}} = \tfrac{1}{60\pi}\,\hat y\times\hat z\;12e^{-j(8\pi/3)y} = \tfrac{1}{5\pi}e^{-j(8\pi/3)y}\,\hat x\approx63.7\,e^{-j(8\pi/3)y}\,\hat x$ mA/m ($\hat z\times\hat x = +\hat y$ ✓); $\mathbf{H} = 63.7\cos\big(4\pi\times10^8t - \tfrac{8\pi}{3}y\big)\,\hat x$ mA/m.

## 6. The notes' Example 3: a monochromatic current sheet in phasor form

Lecture 19's delay $d/v$ ($d$: distance; $\hat n$: from sheet to field point) becomes $e^{-j\beta d}$:

> [!key] A sinusoidal current sheet, in phasors
> For $\mathbf{J}_s(t) = \text{Re}\{\tilde{\mathbf{J}}_se^{j\omega t}\}$ in a lossless medium,
> $$
> \tilde{\mathbf{E}} = -\frac\eta2\,\tilde{\mathbf{J}}_s\,e^{-j\beta d},\qquad \tilde{\mathbf{H}} = \frac12\,\tilde{\mathbf{J}}_s\times\hat n\;e^{-j\beta d}.
> $$
> Sheet on $z = 0$: $d = \lvert z\rvert$, $\hat n = \pm\hat z$ for $z\gtrless0$; $\tilde{\mathbf{S}}\parallel+\hat n$.

**The notes' example.** $\mathbf{J}_s = \hat x\,2\cos(\omega t)$ A/m on $z = 0$, vacuum: $\tilde{\mathbf{J}}_s = 2\hat x$ A/m, $\beta = \omega/c$, $\eta = \eta_0\approx120\pi\ \Omega$; Lecture 19's $E_x = -\eta\cos(\omega t\mp\beta z)$, $H_y = \mp\cos(\omega t\mp\beta z)$ become
$$
\begin{gathered}
\tilde{\mathbf{E}}^\pm = -\eta\,e^{\mp j\beta z}\,\hat x\ \ \text{V/m},\\[4pt]
\tilde{\mathbf{H}}^\pm = \mp e^{\mp j\beta z}\,\hat y\ \ \text{A/m}\qquad(z\gtrless0).
\end{gathered}
$$
Box: $\tfrac12(2\hat x)\times(\pm\hat z) = \mp\hat y$ ✓; $(-\eta\hat x)\times(-\hat y) = +\eta\hat z$ above, $(-\eta\hat x)\times(+\hat y) = -\eta\hat z$ below ✓.

**A sine instead** (this site's): $\mathbf{J}_s = \hat x\,2\sin(\omega t)$ A/m, $\tilde{\mathbf{J}}_s = -2j\hat x$; $\tilde{\mathbf{E}}^\pm = j\eta e^{\mp j\beta z}\hat x$, $\tilde{\mathbf{H}}^\pm = \pm je^{\mp j\beta z}\hat y$, i.e. $E_x = -\eta\sin(\omega t\mp\beta z)$, $H_y = \mp\sin(\omega t\mp\beta z)$. Same averages (§7).

## 7. Time averages straight from phasors

Instead of [[3-maxwell-and-waves/20-poynting-theorem-and-monochromatic-waves|Lecture 20]]'s $\cos^2$ averages:

> [!derivation]- The product rule ⟨a b⟩ = ½ Re{Ã B̃*}
> With $\text{Re}\{z\} = \tfrac12(z + z^*)$:
> $$
> \begin{aligned}
> a\,b &= \tfrac14\big(\tilde Ae^{j\omega t} + \tilde A^*e^{-j\omega t}\big)\big(\tilde Be^{j\omega t} + \tilde B^*e^{-j\omega t}\big)\\[4pt]
> &= \frac{\tilde A\tilde B^* + \tilde A^*\tilde B}{4} + \frac{\tilde A\tilde Be^{j2\omega t} + \tilde A^*\tilde B^*e^{-j2\omega t}}{4}\\[4pt]
> &= \tfrac12\text{Re}\{\tilde A\tilde B^*\} + \tfrac12\text{Re}\{\tilde A\tilde B\,e^{j2\omega t}\}.
> \end{aligned}
> $$
> The $2\omega$ term averages out:
> $$
> \begin{aligned}
> \langle a\,b\rangle &= \frac1T\int_0^Ta(t)\,b(t)\,dt\\
> &= \tfrac12\text{Re}\{\tilde A\tilde B^*\} = \tfrac12AB\cos(\theta_a - \theta_b).
> \end{aligned}
> $$
> Notes: same proof for $\langle v(t)i(t)\rangle = \tfrac12\text{Re}\{VI^*\}$. A common phase cancels.

$\langle a^2\rangle = \tfrac12\lvert\tilde A\rvert^2$; in phase $\tfrac12AB$, quadrature 0, antiphase $-\tfrac12AB$. $3\cos(\omega t + 20^\circ)$, $2\cos(\omega t - 40^\circ)$: $\tfrac12\cdot3\cdot2\cos60^\circ = 1.5$.

<!-- fig:phas-time-average -->

> [!key] Time averages of power densities
> $$
> \begin{gathered}
> \langle\mathbf{E}\times\mathbf{H}\rangle = \tfrac12\text{Re}\{\tilde{\mathbf{E}}\times\tilde{\mathbf{H}}^*\}\ \ [\text{W/m}^2],\\[4pt]
> \langle\mathbf{J}\cdot\mathbf{E}\rangle = \tfrac12\text{Re}\{\tilde{\mathbf{J}}\cdot\tilde{\mathbf{E}}^*\}\ \ [\text{W/m}^3],\\[6pt]
> \tilde{\mathbf{S}}\equiv\tilde{\mathbf{E}}\times\tilde{\mathbf{H}}^*\ \ (\text{complex Poynting vector}),\\[4pt]
> \langle\mathbf{S}\rangle = \tfrac12\text{Re}\{\tilde{\mathbf{S}}\}.
> \end{gathered}
> $$
> Componentwise; sheets: $\langle\mathbf{J}_s\cdot\mathbf{E}\rangle = \tfrac12\text{Re}\{\tilde{\mathbf{J}}_s\cdot\tilde{\mathbf{E}}^*\}$ W/m². **One lossless plane wave** (§5):
> $$
> \langle\mathbf{S}\rangle = \frac{\lvert\tilde{\mathbf{E}}_0\rvert^2}{2\eta}\,\hat u = \frac{\eta\lvert\tilde{\mathbf{H}}_0\rvert^2}{2}\,\hat u,
> $$
> $\lvert\tilde{\mathbf{E}}_0\rvert^2 = \lvert\tilde E_{0x}\rvert^2 + \lvert\tilde E_{0y}\rvert^2 + \lvert\tilde E_{0z}\rvert^2$, whatever the phases.

§1's wave: $\langle\mathbf{S}\rangle = 144/(120\pi)\,\hat y = 0.382\,\hat y$ W/m².

> [!example] Same numbers, two routes: the notes' sheet (Lecture 20 by cos², Lecture 21 by phasors)
> §6's phasors:
> $$
> \begin{aligned}
> \langle\mathbf{S}^\pm\rangle &= \tfrac12\text{Re}\big\{(-\eta e^{\mp j\beta z}\hat x)\times(\mp e^{\pm j\beta z}\hat y)\big\}\\
> &= \pm\frac\eta2\,\hat z = \pm60\pi\,\hat z\ \ \text{W/m}^2,
> \end{aligned}
> $$
> $$
> \begin{aligned}
> \langle-\mathbf{J}_s\cdot\mathbf{E}(0, t)\rangle &= \tfrac12\text{Re}\{-\tilde{\mathbf{J}}_s\cdot\tilde{\mathbf{E}}^*(0)\}\\
> &= \tfrac12\text{Re}\{-(2\hat x)\cdot(-\eta\hat x)\}\\
> &= \eta\approx120\pi\ \ \text{W/m}^2 .
> \end{aligned}
> $$
> Lecture 20's $\pm60\pi\,\hat z$ ($\approx188$ W/m²) and 377 W/m² from the current: $\eta/2$ per side, any $z$. Sine current: $(-j)(-j)^* = 1$, same.

> [!example] Example 2's power: counter-propagating waves subtract (this site's extension)
> $\tilde{\mathbf{H}}^* = \hat xH^+e^{j\beta z} + j\hat yH^-e^{-j\beta z}$; $\hat x\times\hat x$, $\hat y\times\hat y$ vanish:
> $$
> \begin{aligned}
> \tilde{\mathbf{E}}\times\tilde{\mathbf{H}}^* &= -\eta(H^+)^2\,(\hat y\times\hat x)\\
> &\quad + j\cdot j\,\eta(H^-)^2\,(\hat x\times\hat y)\\
> &= \eta\big[(H^+)^2 - (H^-)^2\big]\hat z,
> \end{aligned}
> $$
> so $\langle\mathbf{S}\rangle = \tfrac\eta2\big[(H^+)^2 - (H^-)^2\big]\hat z$. Parallel polarizations add imaginary cross terms, absent from $\langle\mathbf{S}\rangle$ (instantaneous: [[concepts/poynting-vector|Poynting vector page]]).

**Joule heating, and Lecture 11 once more.** With $\tilde{\mathbf{J}} = \sigma\tilde{\mathbf{E}}$, $\langle\mathbf{J}\cdot\mathbf{E}\rangle = \tfrac12\text{Re}\{\sigma\}\,\lvert\tilde{\mathbf{E}}\rvert^2$: $\tfrac12\sigma E_0^2$ for real $\sigma$ ([[1-electrostatics/10-capacitance-and-conductance|Lecture 10]]). Only current in phase with $\mathbf{E}$ absorbs. The plasma's imaginary $\sigma$: current 90° off, energy returned each quarter period (figure, bottom), lossless. Collisions: $\text{Re}\{\sigma_{\text{DC}}/(1 + j\omega/\nu)\} = \sigma_{\text{DC}}/(1 + \omega^2/\nu^2)$, damping ([[3-maxwell-and-waves/22-phasor-maxwell-equations-and-damped-waves|Lecture 22]], [[3-maxwell-and-waves/23-imperfect-dielectrics-and-good-conductors|Lecture 23]]).

> [!trap] Power from phasors
> - Missing $\tfrac12$ (peak phasors; rms ones drop it) or conjugate ($\tfrac12\text{Re}\{\tilde{\mathbf{E}}\times\tilde{\mathbf{H}}\}$ varies as $\cos2\beta z$ for one linearly polarized wave).
> - "Phasor of the power": none; only the average, from $\tilde A\tilde B^*$.
> - Instantaneous $\mathbf{S}$ of one linearly polarized wave swings 0 to $2\langle\mathbf{S}\rangle$ at $2\omega$; with out-of-phase perpendicular components it never hits 0 ([[problems/phasors-e-and-power-from-a-given-h|worked problem]], (f)).
> - Dropping a perpendicular component: powers add.

## 8. Connections

Next: Lecture 22 (complex $\gamma = \alpha + j\beta$, $\eta$), [[3-maxwell-and-waves/24-signal-transmission-and-circular-polarization|Lecture 24]] (circular polarization, $v_g$), [[3-maxwell-and-waves/25-wave-reflection-and-transmission|Lecture 25]] (reflection), Unit 4 ($\tilde V(z)$, $\tilde I(z)$).

## 9. Summary

The In-one-breath box, plus: $(a, b, c) = -\beta\hat u$; sheet $\tilde{\mathbf{E}} = -\tfrac\eta2\tilde{\mathbf{J}}_se^{-j\beta d}$; $\langle ab\rangle = \tfrac12\text{Re}\{\tilde A\tilde B^*\}$; one wave carries $\lvert\tilde{\mathbf{E}}_0\rvert^2/2\eta$; no plasma wave below $f_p\approx9\sqrt N$ Hz.

Concept pages: [[concepts/phasors]] · [[concepts/dispersion-relation]] · [[concepts/plane-waves]] · [[concepts/poynting-vector]] · [[concepts/poynting-theorem]] · [[concepts/intrinsic-impedance]] · [[concepts/current-sheet-radiation]] · [[concepts/conductivity-and-susceptibility-models]].

> [!exam] On exams
> Opens most Exam 3 wave problems on hand (SP17–FA23; Summer (Su) 2017–2020 HE3; Su20 final, FE):
> 1. **Time → phasor, sines included**: SP17 #4a, Su19 HE3 #1a(i), Su20 FE #4a (two sheets). §3's table, group by exponent.
> 2. **$\tilde{\mathbf{H}}$ ↔ $\tilde{\mathbf{E}}$**: SP19 #1c, Su17 HE3 #3f, Su19 HE3 #1a(ii), Su18 HE3 #1b(v), Su20 HE3 #1a, SP17 #2(iii) ($\eta = 1500\ \Omega$). §5's recipe, direction first.
> 3. **Numbers off an expression**: SP17 #3c, Su20 HE3 #2a, #2f, Su20 FE #3a; template: Su17 HE3 #2a, Su18 HE3 #3a, Su19 HE3 #3a. §1's example, §4's rule.
> 4. **$\langle\mathbf{S}\rangle$**: SP17 #4b, SP19 #2c (× plate cross-section), Su20 FE #4c, FA23 #6(a) (damped). Often one component's power first, then the whole wave: component powers add.
>
> Traps: $e^{+j\beta x}$ direction, a sine's $-j$, the template's plus, $\tilde{\mathbf{H}}$ orientation, the $\tfrac12$. No-calculator: $\eta_0 = 120\pi\ \Omega$, $c = 3\times10^8$ m/s. [[problems/phasors-e-and-power-from-a-given-h|Worked problem]]: skills 1–4.

> [!tip] Practice this lecture
> [[practice/21-phasors-and-monochromatic-waves|12 practice problems]] — 5 easy, 3 medium, 4 hard — each with a folded hint and a worked solution. Start with [[practice/21-phasors-and-monochromatic-waves#211-reading-two-waves|21.1 Reading two waves]]; the [[practice/index|practice hub]] has the whole bank by difficulty and by topic.

### Sources for this page
Kudeki notes, Lecture 21 (8 pages); no slides. Notes: §§1–2, spectrum chart, Examples 1–3, $\tilde{\mathbf{E}}\leftrightarrow\tilde{\mathbf{H}}$ rules, time averages. Rao (2009) §1.4, §4.5, §8.1, §8.3, §10.1. This site's own: derivations, Example 2's power, the sine current, numbered examples, figures (script-checked). Slips in the course material: see [[0-toolkit/04-errata-in-the-course-materials|errata]].
