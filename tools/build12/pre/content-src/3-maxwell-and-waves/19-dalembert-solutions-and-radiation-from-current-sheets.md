---
title: "Lecture 19 — d'Alembert solutions and radiation from current sheets"
description: "Uniform plane TEM waves and their simplest source: an infinite current sheet Jₛ(t) radiates E = −(η/2)Jₛ and H = ½Jₛ × n̂, delayed by |z|/v. E opposes the current and is continuous; H reverses and jumps by Jₛ."
tags: [lecture, waves]
lecture: 19
---

*Lecture 19 · course notes §19 · slides "Uniform Plane Waves in Free Space" (Lecture 19) · prev: [[3-maxwell-and-waves/18-the-wave-equation-and-plane-tem-waves|Lecture 18]] · next: [[3-maxwell-and-waves/20-poynting-theorem-and-monochromatic-waves|Lecture 20]] · worked problem: [[problems/a-current-sheet-launches-two-waves|A current sheet launches two waves]] · practice: [[practice/19-radiation-from-current-sheets|12 problems]]*

> [!abstract] In one breath
> Lecture 18's waves $f(t\mp z/v)$ are **uniform plane TEM waves**, travelling along the **Poynting vector** $\mathbf{E}\times\mathbf{H}$. An infinite sheet $\mathbf{J}_s(t)$ launches them: $\mathbf{H} = \tfrac12\mathbf{J}_s\times\hat n$ ([[2-magnetostatics/13-current-sheets-solenoids-and-the-vector-potential|Lecture 13]]) and $\mathbf{E} = -\tfrac{\eta}{2}\mathbf{J}_s$, both delayed by $\lvert z\rvert/v$. $\mathbf{E}$ opposes the current and is continuous; $\mathbf{H}$ reverses and jumps by $J_s$ ([[3-maxwell-and-waves/16-charge-conservation-displacement-current-and-maxwells-equations|Lecture 16]]). A cosine current gives $\beta = \omega/v$, $\lambda = 2\pi/\beta$, and outward $\mathbf{S}$ [W/m²].

## 1. What kind of wave is $f(t\mp z/v)$?

Lecture 18 ended with the d'Alembert solutions for a homogeneous, lossless, source-free region,

$$
\mathbf{E} = \hat x\,f\Big(t\mp\frac zv\Big),\qquad \mathbf{H} = \pm\hat y\,\frac{f(t\mp z/v)}{\eta},\qquad v = \frac{1}{\sqrt{\mu\epsilon}},\quad \eta = \sqrt{\frac\mu\epsilon}.
$$

The notes call them **uniform plane TEM waves**:

- **TEM:** $\mathbf{E},\mathbf{H}\perp$ the travel. For fields depending on $z$ alone, $\nabla\cdot\mathbf{E} = \nabla\cdot\mathbf{H} = 0$ forbids a $z$-component ($\partial E_z/\partial z\neq0$; [[3-maxwell-and-waves/18-the-wave-equation-and-plane-tem-waves#3-the-planar-problem-only-exzt-and-hyzt|Lecture 18 §3]]).
- **Travel along $\mathbf{S}\equiv\mathbf{E}\times\mathbf{H}$**, the **Poynting vector**, now the definition: $\hat x\times(\pm\hat y) = \pm\hat z$.
- **Uniform plane:** the same field over each **plane of constant phase** $t - z/v = t_0$, i.e. $z = v(t - t_0)$, perpendicular to $\mathbf{S}$, moving at the **phase velocity** $v_p = v$ ($c$ in free space; §7).

A compact antenna's spherical waves are TEM but not uniform (ECE 450); a *plane* wave needs an infinite plane of current.

> [!key] Uniform plane TEM wave, and the rule that pairs E with H
> A field that depends on position only through $t - \hat u\cdot\mathbf{r}/v$, with $\mathbf{E}\perp\hat u$ and
> $$
> \mathbf{H} = \frac1\eta\,\hat u\times\mathbf{E},\qquad \mathbf{E} = \eta\,\mathbf{H}\times\hat u,\qquad \mathbf{E}\times\mathbf{H}\parallel\hat u .
> $$
> The notes: divide $\mathbf{E}$ by $\eta$ and rotate 90° so that $\mathbf{E}\times\mathbf{H}$ points along the travel ([[3-maxwell-and-waves/18-the-wave-equation-and-plane-tem-waves#5-h-from-e-the-intrinsic-impedance|Lecture 18 §5]]).

## 2. Three warm-up examples (notes)

> [!example] Example 1 — a triangular pulse travelling along $y$, and its B two ways
> In free space $\mathbf{E} = \hat x\,\triangle\big((t - y/c)/\tau\big)$, $\triangle(u)$ the unit triangle of ECE 210 (peak 1 at $u = 0$, zero for $\lvert u\rvert\ge\tfrac12$). Find $\mathbf{B}$.
>
> **Route 1, rotation.** Travel toward $+y$: $\mathbf{H} = \hat y\times\mathbf{E}/\eta_0 = -\hat z\,\triangle/\eta_0$ ($\hat x\times(-\hat z) = +\hat y$ ✓); $\mu_0/\eta_0 = \sqrt{\mu_0\epsilon_0} = 1/c$:
> $$
> \mathbf{B} = \mu_0\mathbf{H} = -\hat z\,\frac1c\,\triangle\Big(\frac{t - y/c}{\tau}\Big).
> $$
> **Route 2, Faraday.** $\partial\mathbf{B}/\partial t = -\nabla\times(\hat xE_x) = +\hat z\,\partial E_x/\partial y = -\hat z\,\triangle'/(c\tau)$ ($\triangle'$: derivative with respect to the argument). Integrating in time, static constant dropped, gives the same $\mathbf{B}$. At $y = 40$ m, $t = 0.05$ µs, $\tau = 1$ µs both sides equal $-6.67\times10^{-3}$ T/s.

> [!example] Example 2 — is the magnetic force of a wave negligible?
> A charge $q$ with velocity $\mathbf{v}$ in the Example 1 wave ([[concepts/lorentz-force]]):
> $$
> \mathbf{F} = q\,\triangle\Big(\frac{t - y/c}{\tau}\Big)\Big(\hat x - \frac{\mathbf{v}\times\hat z}{c}\Big).
> $$
> The magnetic term is smaller by $v_\perp/c$ ($v_\perp$: velocity perpendicular to $\mathbf{B}$; this site's phrasing of the notes' point): $3.3\times10^{-3}$ at $10^6$ m/s (a fast vacuum-tube electron), 0.67 at $2\times10^8$ m/s: negligible unless the charge is relativistic. So $\mathbf{E}$ does the work in antennas and absorbed light, though $E$ and $H$ carry equal energy (Lecture 20).

> [!example] Example 3 — one pulse, plotted against t and against z
> $\mathbf{E} = \hat x\,f(t - z/c)$ in free space, $f(t) = At\,\mathrm{rect}(t/\tau)$, $A = 2$ V/m per µs, $\tau = 1$ µs (a ramp from $-1$ to $+1$ V/m over $\lvert t\rvert<0.5$ µs), $c = 300$ m/µs.
> - **Against t.** At $z = 600$ m (delay 2 µs), $E_x = 2(t-2)\,\mathrm{rect}(t-2)$ V/m ($t$ in µs): the same rising ramp, $-1$ at 1.5 µs to $+1$ at 2.5 µs.
> - **Against z.** $E_x(z,0) = 2(-z/c)\,\mathrm{rect}(-z/c)$: a *descending* ramp, $+1$ at $z = -150$ m to $-1$ at $+150$ m. At $t = 2$ µs: $+1$ at 450 m, 0 at 600 m, $-1$ at 750 m.
> - **H** (not given in the notes): $\mathbf{H} = \hat z\times\mathbf{E}/\eta_0 = \hat y\,f(t - z/c)/\eta_0$, peak $1/\eta_0 = 2.65$ mA/m.
>
> A $+z$ snapshot is the record mirrored ([[3-maxwell-and-waves/18-the-wave-equation-and-plane-tem-waves#6-reading-a-wave|Lecture 18 §6]]; drilled in §6).

## 3. What launches a plane wave? The notes' route

Lecture 18's waves need $\rho = 0$, $\mathbf{J} = 0$; the notes trace them to varying charges and currents elsewhere, linked by the [[concepts/continuity-equation|continuity equation]]. A *plane* wave needs a source that looks the same from every point of a plane: a sheet $\mathbf{J}_s = \hat x\,J_x$ [A/m] on $z = 0$, homogeneous lossless medium ($\mu$, $\epsilon$) on both sides.

**Step 1: static current (Lecture 13).**

$$
\mathbf{H} = \tfrac12\mathbf{J}_s\times\hat n = \mp\hat y\,\frac{J_x}{2}\quad(z\gtrless0),
$$

with $\hat n$ from the sheet toward the field point ($\tfrac12J_x\,\hat x\times\hat z = -\tfrac12J_x\hat y$ above). Tangential $\mathbf{H}$ jumps by $J_x$; no $\mathbf{E}$.

**Step 2: quasi-static.** For slowly varying $J_x(t)$, $\mathbf{H}\approx\mp\hat y\,J_x(t)/2$ near the sheet. If this held everywhere, $\mathbf{H}$ a light-year away would change at the same instant: infinite speed (footnote 1). Valid only where $\lvert z\rvert/v$ is negligible.

**Step 3: delay it (exact).** Off the sheet the medium is source-free, so the fields must be d'Alembert waves: $J_x(t)\to J_x(t\mp z/v)$ and "≈" → "=":

$$
\mathbf{H}(z,t) = \mp\hat y\,\frac12J_x\Big(t\mp\frac zv\Big),\qquad \mathbf{E}(z,t) = -\hat x\,\frac\eta2\,J_x\Big(t\mp\frac zv\Big)\qquad(z\gtrless0).
$$

$\mathbf{E}$ follows from the §1 rule with $\mathbf{E}\times\mathbf{H}$ away from the sheet: $(-\hat x)\times(\mp\hat y) = \pm\hat z$ ✓.

- **Causality picks the signs** (footnote 2). Both $t\mp z/v$ solve the wave equation, but the sheet is the only source, so waves travel only away from it (ripples from a pebble in a pond): the argument is $t - \lvert z\rvert/v$.
- **Uniqueness confirms it.** Maxwell's equations with the boundary conditions have one solution; these fields are d'Alembert waves in each region and meet the jump conditions (§5).

<!-- fig:sheet-radiated-fields -->

> [!key] Fields radiated by a current sheet (notes' form)
> $\mathbf{J}_s = \hat x\,f(t)$ on $z = 0$, homogeneous lossless medium:
> $$
> \mathbf{E}^\pm = -\hat x\,\frac{\eta}{2}\,f\Big(t\mp\frac zv\Big),\qquad \mathbf{H}^\pm = \mp\hat y\,\frac12\,f\Big(t\mp\frac zv\Big)\qquad\text{in } z\gtrless0 .
> $$
> Upper signs together ($z>0$), lower together; the two $\mp$ are separate signs that agree. **No** $\mp$ before $\mathbf{E}$. Amplitudes $\tfrac\eta2\lvert J_s\rvert$ and $\tfrac12\lvert J_s\rvert$ (ratio $\eta$); in vacuum 1 A/m gives $188$ V/m ($60\pi$) and 0.5 A/m per side.

**Where the displacement current enters.** Without $\partial\mathbf{D}/\partial t$, Step 2 would be exact (no $\mathbf{E}$, infinite speed). It couples $\mathbf{H}$ to $\mathbf{E}$, delaying the response by $\lvert z\rvert/v$.

## 4. The same result from boundary conditions (slides)

Reproduce this route when asked to "derive". Slides: $\mathbf{J}_s = -J_s(t)\,\hat x$, free space ($\eta_0$, $v_p = c$), $\hat a_x$; site notation below:

1. **General solution:** $E_x = A f(t - z/v) + B g(t + z/v)$, $H_y = \frac{1}{\eta}\big[Af(t - z/v) - Bg(t + z/v)\big]$.
2. **Radiation condition:** $B = 0$ for $z>0$, $A = 0$ for $z<0$. So $E_x = Af$, $H_y = Af/\eta$ above; $E_x = Bg$, $H_y = -Bg/\eta$ below.
3. **Tangential $\mathbf{E}$ continuous** at $z = 0$: $Af(t) = Bg(t)$ for all $t$; same waveform, same sign.
4. **Tangential $\mathbf{H}$ jumps by $\mathbf{J}_s$:** $\hat n\times(\mathbf{H}_1 - \mathbf{H}_2) = \mathbf{J}_s$, region 1 = $z>0$, $\hat n = \hat z$. With $\hat z\times\hat y = -\hat x$, $-\hat x\,\big[H_y(0^+) - H_y(0^-)\big] = -J_s\hat x$:
$$
H_y(0^+) - H_y(0^-) = \frac{Af(t)}{\eta} - \Big(-\frac{Af(t)}{\eta}\Big) = \frac{2Af(t)}{\eta} = J_s(t)\quad\Longrightarrow\quad Af(t) = \frac\eta2\,J_s(t).
$$
5. **Delay it:** $Af(t - z/v) = \tfrac\eta2J_s(t - z/v)$; likewise below.

The blue ink (slides 5, 7) marks the sign-slip spots: both sides evaluated at $z = 0$ (step 3), and the minus of $H_y$ below becoming a plus in the jump (step 4).

> [!key] Fields radiated by a current sheet (slides' form, free space)
> For $\mathbf{J}_s = -J_s(t)\,\hat x$ on $z = 0$:
> $$
> \mathbf{E}(z,t) = \hat x\,\frac{\eta_0}{2}\,J_s\Big(t\mp\frac zc\Big),\qquad \mathbf{H}(z,t) = \pm\hat y\,\frac12\,J_s\Big(t\mp\frac zc\Big),\qquad z\gtrless0 .
> $$
> The notes' result with $f\to-J_s$: the sheets point opposite ways. In both, $\mathbf{E}$ opposes the current.

> [!recipe] Fields of a current sheet in any orientation
> $\hat n$: unit normal from the sheet toward the field point (it flips side to side); $d$: distance from the sheet.
> $$
> \mathbf{E} = -\frac\eta2\,\mathbf{J}_s\Big(t - \frac dv\Big),\qquad \mathbf{H} = \frac12\,\mathbf{J}_s\Big(t - \frac dv\Big)\times\hat n,\qquad \mathbf{E}\times\mathbf{H}\parallel+\hat n .
> $$
> 1. Write $\mathbf{J}_s(t)$ as a vector, sign included.
> 2. $\mathbf{H} = \tfrac12\mathbf{J}_s\times\hat n$ (Lecture 13), each side separately.
> 3. $\mathbf{E} = -\tfrac\eta2\mathbf{J}_s$, the same on both sides.
> 4. $t\to t - d/v$ (sheet on $y = 0$: $t\mp y/v$ for $y\gtrless0$).
> 5. Check that $\mathbf{E}\times\mathbf{H}$ points away from the sheet on both sides.

## 5. Reading the result

**E is even, H is odd** (circled on the slides: $\eta_0/2$ both sides, $\pm\tfrac12$ flips): the Lecture 16 conditions ([[concepts/boundary-conditions]]) $E_x(0^+,t) = E_x(0^-,t)$ and $\hat z\times(\mathbf{H}^+ - \mathbf{H}^-) = \hat z\times(-\hat y\,f) = +\hat x\,f = \mathbf{J}_s$ (notes' orientation). The $\tfrac12$ is Lecture 13's half-jump per side; $\mathbf{E}$ is new.

**E opposes the current:** $\mathbf{J}_s\cdot\mathbf{E} = -\tfrac\eta2\lvert\mathbf{J}_s\rvert^2<0$. In a resistor $\mathbf{J}\cdot\mathbf{E}>0$ (field works on charges); here the charges work on the field, so the sheet is the *source* of the waves' energy (notes; quantified in Lecture 20). Lecture 18's ink: "$\mathbf{E}$ always opposite of $\mathbf{J}_s$".

> [!trap] Sign traps at a sheet
> - A $\mp$ before $\mathbf{E}$ by analogy with $\mathbf{H}$: then tangential $\mathbf{E}$ would jump.
> - $t + z/v$ above the sheet: the argument is always $t - (\text{distance})/v$, outgoing.
> - One $\hat n$ for both sides: it points toward the field point, $+\hat z$ above, $-\hat z$ below.
> - Dropping the $\tfrac12$, or $\mathbf{E}$ amplitude $\eta J_s$: each side gets $\eta J_s/2$ and $J_s/2$.
> - Matching the slides' and notes' formulas term by term: their sheets point opposite ways; compare $\mathbf{E}$ with $\mathbf{J}_s$.

> [!example] Example 4 (notes) — a ramp of sheet current, seen at $t = 2$ µs
> Free space, $\mathbf{J}_s = \hat x\,f(t)$ on $z = 0$, $f(t) = At\,\mathrm{rect}(t/\tau)$, $A = 2$ A/m per µs, $\tau = 1$ µs (ramp from $-1$ to $+1$ A/m). Plot $H_y$, $E_x$ against $z$ at $t = 2$ µs ($c = 300$ m/µs, $\eta_0\approx120\pi\ \Omega$).
>
> The waves have gone 600 m, so the fields occupy $450<\lvert z\rvert<750$ m:
> $$
> H_y(z, 2\ \mu\text{s}) = \mp\frac12\,f\Big(2\mp\frac{z}{300}\Big),\qquad E_x(z, 2\ \mu\text{s}) = -60\pi\,f\Big(2\mp\frac z{300}\Big)\quad(z\gtrless0;\ z\ \text{in m},\ f\ \text{in A/m}).
> $$
> - $z>0$ (450 → 750 m): $H_y$ rises $-0.5\to+0.5$ A/m; $E_x$ rises $-60\pi\to+60\pi\approx188$ V/m.
> - $z<0$ ($-750\to-450$ m): $H_y$ rises $-0.5\to+0.5$; $E_x$ falls $+60\pi\to-60\pi$.
>
> Rescaled, delayed copies of the source, mirrored on the $+z$ side. Spot check, 700 m: $f(2 - 7/3) = f(-1/3) = -2/3$ A/m, $H_y = +1/3$ A/m, $E_x = +40\pi$ V/m, $\hat x\times\hat y = +\hat z$ ✓.

<!-- fig:sheet-ramp-radiation -->

> [!example] Example (slide 17) — given $\mathbf{J}_s$ and $\mathbf{H}$ of a sheet on $y = 0$, find $\mathbf{E}$
> Sheet in the $xz$-plane, $\mathbf{J}_s = -J_s(t)\,\hat z$, sinusoidal $\mathbf{H}$ of amplitude $H_0$. Find $\mathbf{E}$. (Hint: $\mathbf{E}\times\mathbf{H}$ along the propagation, $\eta_0 = \lvert\mathbf{E}\rvert/\lvert\mathbf{H}\rvert$. Unsolved in the deck.)
> - $\hat n = \pm\hat y$ for $y\gtrless0$: $\mathbf{H} = \tfrac12(-J_s\hat z)\times(\pm\hat y) = \pm\tfrac12J_s\,\hat x$, so $H_0 = J_{s0}/2$.
> - $\mathbf{E} = -\tfrac{\eta_0}{2}\mathbf{J}_s = +\hat z\,\tfrac{\eta_0}{2}J_s$ on both sides, against the current, amplitude $\eta_0H_0\approx377H_0$ ($120\pi H_0$).
> - Hint check: $\hat z\times(\pm\hat x) = \pm\hat y$ ✓.
>
> Cosine current: $\mathbf{E} = \hat z\,\eta_0H_0\cos(\omega t\mp\beta y)$, $\mathbf{H} = \pm\hat x\,H_0\cos(\omega t\mp\beta y)$ for $y\gtrless0$ ($\beta$: §7).

## 6. Transforming time and space (slide 11)

Snapshot (field against position, one instant) ↔ record (field against time, one place): slide 11, inked twice in class.

> [!example] Example (slide 11) — a wave given at $t = 0$
> A $+z$ wave at 100 m/s has, at $t = 0$, a piecewise-linear profile through A $(-100\ \text{m}, 0)$, B $(0, 1)$, C $(100\ \text{m}, -1)$, D $(300\ \text{m}, 0)$, E $(400\ \text{m}, 0)$, zero outside. Sketch (a) $E(z, 1\ \text{s})$, (b) $E(0,t)$, (c) $E(200\ \text{m}, t)$.
>
> $E(z,t) = F(z - 100t)$: each corner rides a **world line** $z = z_0 + 100t$ in the $z$–$t$ plane (ink: "+ slope" for a $+z$ wave).
> - **(a)** Corners move 100 m right: $z = 0, 100, 200, 400, 500$ m, values $0, 1, -1, 0, 0$; the B–C zero crossing moves from 50 to 150 m. (Inked.)
> - **(b)** Corner $z_0$ reaches $z = 0$ at $t = -z_0/100$: A $+1$ s, B 0, C $-1$ s, D $-3$ s, E $-4$ s. Record: 0 until $-3$ s, $-1$ at $-1$ s, zero at $-0.5$ s, $+1$ at 0, 0 at $+1$ s: the profile reversed. (Inked.)
> - **(c)** $E(200, t) = F(200 - 100t) = E(0, t - 2\ \text{s})$: 0 until $-1$ s, $-0.5$ at 0, $-1$ at 1 s, zero at 1.5 s, $+1$ at 2 s, 0 at 3 s. (Unsolved in the deck.)

<!-- fig:sheet-space-time -->

It answers every snapshot/record question in the unit ([[problems/a-pulse-on-the-move|A pulse on the move]], SP18 Exam 2 #4). For a $-z$ wave the world lines slope the other way and the record keeps the profile's order.

## 7. A sinusoidal sheet current: β, λ and the Poynting vector (slides)

The slides take $\mathbf{J}_s = -J_{s0}\cos(\omega t)\,\hat x$ on $z = 0$ in free space; $J_s(t\mp z/c) = J_{s0}\cos(\omega t\mp\beta z)$ in §4 gives:

> [!key] The sheet's sinusoidal waves (free space)
> $$
> \mathbf{E}(z,t) = \hat x\,\frac{\eta_0J_{s0}}{2}\cos(\omega t\mp\beta z),\qquad \mathbf{H}(z,t) = \pm\hat y\,\frac{J_{s0}}{2}\cos(\omega t\mp\beta z),\qquad z\gtrless0,\qquad \beta = \frac{\omega}{v_p}.
> $$
> Real cosines of time; phasors arrive in Lecture 21.

Every parameter comes from the **phase** $\phi = \omega t\mp\beta z$:

| quantity | definition | unit |
|---|---|---|
| phase | $\phi = \omega t\mp\beta z$ | rad |
| angular frequency | $\omega = \partial\phi/\partial t$ | rad/s |
| frequency | $f = \omega/2\pi$ | Hz = 1/s |
| phase constant | $\beta = \lvert\partial\phi/\partial z\rvert$ | rad/m |
| wavelength | $\lambda = 2\pi/\beta$ | m |
| phase velocity | $v_p = \omega/\beta = \lambda f$ ($= c$ in free space) | m/s |
| intrinsic impedance | $\eta_0 = \lvert\mathbf{E}\rvert/\lvert\mathbf{H}\rvert$ | Ω |

($f$: waveform in §4, frequency here.) $\phi$ = const gives $z = (\omega t - \text{const})/\beta$, moving at $\omega/\beta$. $\lambda$ is the distance over which the phase changes by $2\pi$ at fixed $t$. At 100 MHz in free space, $\beta = 2\pi f/c = 2.10$ rad/m, $\lambda = 3.00$ m.

**The Poynting vector** points along the energy flow; its size is power per area, W/m² (V/m × A/m):

$$
\mathbf{S} = \mathbf{E}\times\mathbf{H} = \pm\hat z\,\frac{\eta_0J_{s0}^2}{4}\cos^2(\omega t\mp\beta z)\ \ \text{W/m}^2,\qquad z\gtrless0 .
$$

Outward on both sides and never negative ($\cos^2\ge0$): pulses at twice the source frequency. $\lvert\mathbf{S}\rvert = \lvert\mathbf{E}\rvert^2/\eta_0 = \eta_0\lvert\mathbf{H}\rvert^2$; for $J_{s0} = 1$ A/m the peak is $\eta_0/4 = 94.2$ W/m² per side. The two sides together carry $\eta_0J_s^2/2$, exactly $-\mathbf{J}_s\cdot\mathbf{E}$ at the sheet (§5). Why this is a power density, and its time average: [[3-maxwell-and-waves/20-poynting-theorem-and-monochromatic-waves|Lecture 20]], [[concepts/poynting-vector]].

> [!example] Example — frequency and wavelength from a phase change (the skill tested by SP18 Exam 2 #1(vii))
> At a fixed point in free space the phase advances by $4\pi$ rad in 5 µs: $\omega = \partial\phi/\partial t = 4\pi/(5\times10^{-6}\ \text{s}) = 8\pi\times10^5\approx2.51\times10^6$ rad/s, $f = \omega/2\pi = 400$ kHz, $\lambda = c/f = (3\times10^8)/(4\times10^5) = 750$ m.

## 8. An inverse problem: slides 18–21

From a radiated field, find the rest, including the current (unsolved in the deck; this site's solutions).

**Stem.** A sheet current flows in the plane $x = 0$. For $x>0$, $\mathbf{H}(x, t = 1\ \mu\text{s}) = 2x\,[u(x) - u(x - 100)]\,\hat y$ A/m ($x$ in m): a ramp from 0 to its peak at 100 m, then a vertical drop. Medium unstated; take $c = 300$ m/µs.

> [!trap] The stem and its plot disagree by a factor of 100
> As printed, $2x$ at 100 m is **200 A/m**; the plot marks the peak "2" (perhaps the coefficient should be 0.02 A/m²). Below uses the **plot's scale** ($H_y = 0.02x$, peak 2 A/m). For the formula, multiply every field and current by 100; shapes and times unchanged.

- **(a) $H_y(400\ \text{m}, t)$, $0\le t\le10$ µs.** $H_y(x,t) = F\big(x - c(t - 1)\big)$, $F$ the given profile. The vertical edge at 100 m is the front; it reaches 400 m $300/300 = 1$ µs later, at $t = 2$ µs. The record jumps to 2 A/m at 2 µs, falls linearly to 0 at $t = 7/3\approx2.33$ µs, then stays zero: the sharp edge comes first in time.
- **(b) $H_y(x, 4\ \mu\text{s})$, $\lvert x\rvert\le1500$ m.** 3 µs later the pattern has moved 900 m: for $x>0$, a ramp from 0 at 900 m to 2 A/m at 1000 m, then zero. For $x<0$, $\mathbf{H}$ is reversed (odd): a step to $-2$ A/m at $-1000$ m, ramping to 0 at $-900$ m.
- **(c) $\mathbf{E}(x, 2\ \mu\text{s})$, $\lvert x\rvert\le500$ m.** For $x>0$, $\mathbf{E} = \eta_0\mathbf{H}\times\hat x$ points along $\hat y\times\hat x = -\hat z$; $\mathbf{E}$ is even. Front at $\lvert x\rvert = 400$ m: $E_z = -2\eta_0(\lvert x\rvert - 300)/100$ for $300<\lvert x\rvert<400$ m, from 0 to $-2\eta_0\approx-754$ V/m at $\lvert x\rvert\to400$ m, zero elsewhere.
- **(d) The current.** With $\hat n = \hat x$: $\mathbf{J}_s = \hat x\times\big(\mathbf{H}(0^+) - \mathbf{H}(0^-)\big) = \hat z\,2H_y(0^+, t)$, and $H_y(0^+, t) = F\big(c(1 - t)\big)$, nonzero for $2/3<t<1$ µs:
$$
\mathbf{J}_s(t) = \hat z\,12\Big(1 - \frac{t}{1\ \mu\text{s}}\Big)\ \text{A/m}\quad\text{for } \tfrac23\ \mu\text{s}<t<1\ \mu\text{s},\ \ \text{zero otherwise}.
$$
It jumps to 4 A/m at $t = 2/3$ µs and ramps to zero at 1 µs (formula scale: $1200(1 - t)$ A/m, peak 400 A/m). Checks: $\mathbf{E}$ along $-\hat z$ opposes $\mathbf{J}_s$ along $+\hat z$, and $E_z(0,t) = -\tfrac{\eta_0}{2}J_{s,z}(t)$ ✓.

This is the notes' Example 4 run backwards.

## 9. Connections

- **Lectures 13, 16, 18:** static sheet field (Step 1), boundary conditions and displacement current (§4–5), d'Alembert waves now given a source and amplitude.
- **Lecture 15** (this site's link). A wide parallel-plate line (width $W$, spacing $d$) in one medium has $1/\sqrt{\mathcal{L}\mathcal{C}} = v$ and $\sqrt{\mathcal{L}/\mathcal{C}} = \eta\,d/W$. A current $I = J_sW$ fed into the middle of an infinite one sees two lines in parallel, $\eta d/(2W)$: $V = I\eta d/(2W)$, $E = V/d = \eta J_s/2$, the sheet's result. A sheet is a current source driving two lines of $\eta$ per square (Unit 4).

## 10. Summary

- Sheet: $\mathbf{E} = -\tfrac\eta2\mathbf{J}_s(t - d/v)$, $\mathbf{H} = \tfrac12\mathbf{J}_s(t - d/v)\times\hat n$; $\mathbf{E}$ even, $\mathbf{H}$ odd, $\mathbf{S}$ outward, $\mathbf{J}_s\cdot\mathbf{E}<0$.
- Derive it by delaying the static field (notes) or by $Af + Bg$ plus boundary conditions (slides).
- Cosine: $\beta = \omega/v_p$, $\lambda = 2\pi/\beta$, $v_p = \lambda f$, $\mathbf{S}\propto\cos^2$, outward.
- Snapshot ↔ record: follow world lines; distance $d$ means delay $d/v$.

Concept pages: [[concepts/current-sheet-radiation]] · [[concepts/poynting-vector]] · [[concepts/plane-waves]] · [[concepts/intrinsic-impedance]] · [[concepts/boundary-conditions]] · [[concepts/displacement-current]] · [[concepts/wave-equation]].

> [!exam] On exams
> 1. **SP18 Exam 2 #5 is this lecture.** Sheet on $y = 0$, $\mathbf{J} = -J_s(t)\,\hat x$, free space, piecewise-linear $J_s(t)$. (a), (b): unit vector and signed coefficient of $\mathbf{H}$ for $y>0$ and $y<0$; (c): that component against $y$ at one instant, scales labelled. Method: the §4 recipe with $\hat n = \pm\hat y$, delay $\lvert y\rvert/v_p$, check $\mathbf{E}\times\mathbf{H}$ points away. Sketch: a source landmark at source time $t'$ sits at distance $v_p(t - t')$ (front farthest out); $\mathbf{H}$ has opposite signs on the two sides. The worked problem runs every step in another geometry; the exam key is not reproduced.
> 2. **#1(vii)**: $\omega$, $f$, $\lambda$ from a phase change (end of §7). **#4**: a pulse moved in space and time (§6).
> 3. Variants: any sheet plane and current direction; $\mathbf{E}$ instead of $\mathbf{H}$ (same sign both sides, against $\mathbf{J}_s$); amplitudes $\eta J_s/2$, $J_s/2$; $\mathbf{J}_s(t)$ from a field (§8); $\beta$, $\lambda$, $v_p$; $\mathbf{S}$.

> [!tip] Practice this lecture
> [[practice/19-radiation-from-current-sheets|12 practice problems]] — 5 easy, 3 medium, 4 hard — each with a folded hint and a worked solution. Start with [[practice/19-radiation-from-current-sheets#191-which-one-is-a-plane-wave|19.1 Which one is a plane wave]]; the [[practice/index|practice hub]] has the whole bank by difficulty and by topic.

### Sources for this page
Kudeki notes, Lecture 19: plane TEM waves, Examples 1–4 (numbers checked), the delayed-static route. Shao, Lecture 19 slides: boundary-condition derivation (slides 2–12), sinusoidal sheet, parameter table, Poynting vector (13–16), examples (11, 17–21; unsolved 11(c), 17, 18–21 solved here). This site's own: $v_\perp/c$, the any-orientation recipe, the traps, the $\mathbf{J}_s\cdot\mathbf{E}$ bookkeeping, the transmission-line picture, all figures. Slips in the course material: see [[0-toolkit/04-errata-in-the-course-materials|errata]]; also, the notes write $\eta_0 = 120\pi$ as an equality (0.07 % high).
