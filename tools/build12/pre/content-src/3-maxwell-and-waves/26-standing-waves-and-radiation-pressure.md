---
title: "Lecture 26 — Standing waves and radiation pressure"
description: "A wave reflected by a perfect mirror adds to the incident wave to make a standing wave, E ∝ sin βz sin ωt and H ∝ cos βz cos ωt, with fixed nodes and no net power flow. The mirror's surface current 2E₀/η₁ is the depth integral of a good conductor's skin current, and J × B on it pushes the mirror with the radiation pressure 2⟨S_i⟩/c."
tags: [lecture, waves]
lecture: 26
---

*Lecture 26 · course notes §26 (no slides) · prev: [[3-maxwell-and-waves/25-wave-reflection-and-transmission|Lecture 25]] · next: [[4-transmission-lines/27-guided-tem-waves-on-transmission-lines|Lecture 27]] · worked problem: [[problems/a-circular-wave-meets-a-mirror|A circular wave meets a mirror]] · practice: [[practice/26-standing-waves-and-radiation-pressure|12 problems]]*

> [!abstract] In one breath
> A perfect mirror reflects with $\Gamma = -1$. Incident plus reflected wave make a **standing wave**: $\mathbf{E}\propto\sin\beta z\,\sin\omega t$ and $\mathbf{H}\propto\cos\beta z\,\cos\omega t$. The pattern does not travel; it oscillates in place. $\mathbf{E}$ has nodes at the mirror and every $\lambda/2$, and $\mathbf{H}$ has nodes halfway between. No power flows on average; the energy sloshes between electric and magnetic form. The mirror carries a surface current $2E_0/\eta_1$, the depth integral of a good conductor's skin current. $\mathbf{J}\times\mathbf{B}$ on that current pushes the mirror with the **radiation pressure** $2\langle S_i\rangle/c$: waves carry momentum.

## 1. Incident plus reflected: the standing wave

Region 1 ($z<0$) is a perfect dielectric with $\eta_1$ and $\beta_1$. A perfect conductor fills $z>0$, so $\Gamma = -1$ and $\tau = 0$ ([[3-maxwell-and-waves/25-wave-reflection-and-transmission#3-special-cases|Lecture 25 §3]]).

> [!key] Standing-wave phasors (perfect mirror at z = 0)
> $$
> \begin{gathered}
> \tilde{\mathbf{E}}_i = \hat x\,E_0e^{-j\beta_1z},\quad \tilde{\mathbf{E}}_r = -\hat x\,E_0e^{j\beta_1z},\\[6pt]
> \tilde{\mathbf{H}}_i = \hat y\,\frac{E_0}{\eta_1}e^{-j\beta_1z},\quad \tilde{\mathbf{H}}_r = \hat y\,\frac{E_0}{\eta_1}e^{j\beta_1z},\\[8pt]
> \tilde{\mathbf{E}} = -j\hat x\,2E_0\sin\beta_1z,\\[6pt]
> \tilde{\mathbf{H}} = \hat y\,\frac{2E_0}{\eta_1}\cos\beta_1z .
> \end{gathered}
> $$
> With $E_0$ real, multiplying by $e^{j\omega t}$ and taking the real part gives
> $$
> \begin{gathered}
> \mathbf{E}(z,t) = \hat x\,2E_0\sin(\beta_1z)\sin(\omega t),\\[4pt]
> \mathbf{H}(z,t) = \hat y\,\frac{2E_0}{\eta_1}\cos(\beta_1z)\cos(\omega t).
> \end{gathered}
> $$

The sums use $e^{-j\theta}-e^{j\theta} = -2j\sin\theta$ and $e^{-j\theta}+e^{j\theta} = 2\cos\theta$. The reflected $\tilde{\mathbf{H}}$ carries $-\Gamma = +1$, so it keeps the incident sign.

A d'Alembert wave $f(t\mp z/v)$ ([[3-maxwell-and-waves/18-the-wave-equation-and-plane-tem-waves|Lecture 18]]) moves its shape. Here each field is a function of $z$ times a function of $t$: it oscillates in place, with an amplitude set by position. Read backward, $2\sin\beta z\sin\omega t = \cos(\omega t-\beta z) - \cos(\omega t+\beta z)$: two equal waves travelling in opposite directions.

Notation: the notes write $E_o$; this page writes $E_0$.

<!-- fig:stand-snapshots -->

## 2. Nodes, antinodes and time quadrature

> [!key] Where the fields vanish (z ≤ 0, m = 0, 1, 2, …)
> - $\mathbf{E}$ nodes at $z = -m\lambda/2$, the mirror included. $\mathbf{E}$ antinodes (amplitude $2E_0$) at $z = -(2m+1)\lambda/4$.
> - $\mathbf{H}$ nodes at $z = -(2m+1)\lambda/4$. $\mathbf{H}$ antinodes (amplitude $2E_0/\eta_1$) at $z = -m\lambda/2$, the mirror included.
> - Adjacent nodes of one field are $\lambda/2$ apart. An $\mathbf{E}$ node and the nearest $\mathbf{H}$ node are $\lambda/4$ apart.
> - In time, $\mathbf{E}\propto\sin\omega t$ and $\mathbf{H}\propto\cos\omega t$: a quarter period apart (the $-j$ in $\tilde{\mathbf{E}}$).

The notes' circuit picture: an $\mathbf{E}$ node acts as a **short** ($v = 0$) and an $\mathbf{H}$ node as an **open** ($i = 0$). The mirror is a short: it holds $E_x = 0$ while a current flows on it. [[4-transmission-lines/index|Unit 4]] uses the same language for lines.

> [!trap] Standing waves
> - $\lvert\tilde{\mathbf{E}}\rvert = 2E_0\lvert\sin\beta_1z\rvert$ repeats every $\lambda/2$, not every $\lambda$.
> - Fixed-node sinusoids drawn at several instants fit $\mathbf{E}$ or $\mathbf{H}$ alike; only the node or antinode at the mirror tells them apart.
> - In a lossless travelling wave $\tilde{\mathbf{E}}$ and $\tilde{\mathbf{H}}$ are in phase; here they are 90° apart.
> - Distances count from the mirror. A mirror at $z = d$ puts $z - d$ in place of $z$, with $E_0$ the incident phasor at the mirror (otherwise a factor $e^{-j\beta_1d}$).

**Partial reflection (this site's addition).** For $\lvert\Gamma\rvert<1$, region 1 holds $\tilde E_x = E_0e^{-j\beta_1z}\big(1+\Gamma e^{j2\beta_1z}\big)$. Write $\Gamma = \lvert\Gamma\rvert e^{j\theta}$:
$$
\begin{gathered}
\tilde E_x = (1-\lvert\Gamma\rvert)E_0e^{-j\beta_1z}\\[4pt]
+\ 2\lvert\Gamma\rvert E_0\,e^{j\theta/2}\cos\!\big(\beta_1z+\tfrac\theta2\big).
\end{gathered}
$$
A travelling wave plus a standing wave. $\lvert\tilde E_x\rvert$ ripples between $(1+\lvert\Gamma\rvert)E_0$ and $(1-\lvert\Gamma\rvert)E_0$ with period $\lambda/2$, with no true nulls, and $\langle S\rangle = (1-\lvert\Gamma\rvert^2)E_0^2/2\eta_1$ ([[3-maxwell-and-waves/25-wave-reflection-and-transmission#4-power-balance|Lecture 25 §4]]). The notes treat only $\Gamma = -1$; Lecture 36 returns to such patterns on lines.

<!-- fig:stand-partial -->

## 3. No net power; the energy sloshes

The notes' check, from the phasors:
$$
\begin{gathered}
\langle\mathbf{S}\rangle = \tfrac12\text{Re}\{\tilde{\mathbf{E}}\times\tilde{\mathbf{H}}^*\}\\[4pt]
= \hat z\,\frac{2E_0^2}{\eta_1}\sin\beta_1z\cos\beta_1z\,\text{Re}\{-j\} = 0 .
\end{gathered}
$$
The two travelling waves carry equal power in opposite directions. The instantaneous flux is not zero ([[3-maxwell-and-waves/20-poynting-theorem-and-monochromatic-waves#7-time-averages|Lecture 20 §7]] works the same pair):

> [!key] Instantaneous flux and energy density
> $$
> \begin{gathered}
> \mathbf{S} = \hat z\,\frac{E_0^2}{\eta_1}\sin(2\beta_1z)\sin(2\omega t),\\[6pt]
> w = 2\epsilon_1E_0^2\big[\sin^2\beta_1z\,\sin^2\omega t\\
> +\cos^2\beta_1z\,\cos^2\omega t\big],\\[6pt]
> \langle w\rangle = \epsilon_1E_0^2\ \ \text{at every } z .
> \end{gathered}
> $$

- At $\omega t = 0$ the energy is all magnetic, at the $\mathbf{H}$ antinodes. At $\omega t = \pi/2$ it is all electric, at the $\mathbf{E}$ antinodes. In between, $\mathbf{S}$ carries it across.
- $\mathbf{S} = 0$ at every multiple of $\lambda/4$ at all times. Each $\lambda/4$ cell keeps its energy, $\epsilon_1E_0^2\lambda/4$ per m² of cross-section.
- $w$ vanishes only at an $\mathbf{E}$ node when $\cos\omega t = 0$, and at an $\mathbf{H}$ node when $\sin\omega t = 0$.

<!-- fig:stand-energy -->

## 4. The mirror's surface current

$\mathbf{E}(0,t) = 0$, as the tangential-$\mathbf{E}$ condition requires: all fields vanish inside a perfect conductor. Tangential $\mathbf{H}$ does not vanish: $\mathbf{H}(0,t) = \hat y\,(2E_0/\eta_1)\cos\omega t$. With $\hat n = -\hat z$ from the conductor into region 1 ([[3-maxwell-and-waves/16-charge-conservation-displacement-current-and-maxwells-equations|Lecture 16]]):

> [!key] Surface current on a perfect mirror
> $$
> \begin{gathered}
> \mathbf{J}_s = \hat n\times\mathbf{H}_1 = -\hat z\times\mathbf{H}(0,t)\\[4pt]
> = \hat x\,\frac{2E_0}{\eta_1}\cos\omega t\ \ \text{A/m}.
> \end{gathered}
> $$
> It flows along the incident $\mathbf{E}$. Its phasor $\hat x\,2E_0/\eta_1$ is Lecture 25's.

The notes' reading: $\mathbf{J}_s$ idealizes volume currents in a layer a few skin depths thick (§5); real mirrors are good, not perfect, conductors. Radiation from $\mathbf{J}_s$ produces the reflected wave and cancels the incident wave in $z>0$. Check with [[3-maxwell-and-waves/19-dalembert-solutions-and-radiation-from-current-sheets|Lecture 19]]'s sheet in a uniform medium, $\mathbf{E}^\pm = -\tfrac{\eta_1}{2}\mathbf{J}_s(t\mp z/v)$ (this site's check). It radiates $-\hat x\,E_0\cos(\omega t-\beta_1z)$ into $z>0$, minus the incident wave. Into $z<0$ it radiates $-\hat x\,E_0\cos(\omega t+\beta_1z)$, the reflected wave.

## 5. A good conductor: where the surface current comes from

The notes return to Lecture 25's transmitted fields, with region 1 vacuum and $\mu_2 = \mu_0$:
$$
\begin{gathered}
\tilde{\mathbf{E}}_t = \hat x\,\tau E_0e^{-\gamma_2z},\qquad \tilde{\mathbf{H}}_t = \hat y\,\frac{\tau E_0}{\eta_2}e^{-\gamma_2z},\\[4pt]
\tilde{\mathbf{J}}_t = \sigma_2\tilde{\mathbf{E}}_t,\qquad \tilde{\mathbf{B}}_t = \mu_2\tilde{\mathbf{H}}_t .
\end{gathered}
$$
In a good conductor $\eta_2\approx\sqrt{j\omega\mu_2/\sigma_2}$ and $\gamma_2\approx\sqrt{j\omega\mu_2\sigma_2} = (1+j)/\delta$ ([[3-maxwell-and-waves/23-imperfect-dielectrics-and-good-conductors|Lecture 23]]), with $\lvert\eta_2\rvert\ll\eta_0$.

> [!key] Effective surface current (notes' box)
> $$
> \begin{gathered}
> \tau = \frac{2\eta_2}{\eta_0+\eta_2}\approx\frac{2\eta_2}{\eta_0},\\[6pt]
> \sigma_2\tau\approx\frac{2\sigma_2\eta_2}{\eta_0} = \frac{2\gamma_2}{\eta_0},\\[8pt]
> \int_0^\infty\tilde{\mathbf{J}}_t\,dz = \hat x\,\frac{\sigma_2\tau E_0}{\gamma_2} \approx \hat x\,\frac{2E_0}{\eta_0}.
> \end{gathered}
> $$
> The depth integral of the volume current is the perfect mirror's $\tilde{\mathbf{J}}_s$, whatever $\sigma_2$ (to order $\lvert\eta_2\rvert/\eta_0$).

The key step is $\sigma\eta = \sqrt{j\omega\mu\sigma} = \gamma$. A larger $\sigma_2$ squeezes the same total current into a thinner layer; as $\sigma_2\to\infty$, $\delta\to0$ and the layer becomes the sheet of §4.

> [!key] Surface resistance (notes' box)
> Take $\tilde{\mathbf{J}}(z) = \tilde{\mathbf{J}}_s\gamma e^{-\gamma z}$ with $\gamma = \alpha(1+j)$, so $\int_0^\infty\tilde{\mathbf{J}}\,dz = \tilde{\mathbf{J}}_s$. The Joule heat per unit volume is $\langle\mathbf{J}\cdot\mathbf{E}\rangle = \tfrac12\lvert\tilde{\mathbf{J}}_s\gamma\rvert^2e^{-2\alpha z}/\sigma$. Per unit area:
> $$
> \begin{gathered}
> \int_0^\infty\langle\mathbf{J}\cdot\mathbf{E}\rangle\,dz = \tfrac12R_s\lvert\tilde{\mathbf{J}}_s\rvert^2,\\[6pt]
> R_s\equiv\frac\alpha\sigma = \sqrt{\frac{\pi f\mu}{\sigma}} = \frac{1}{\sigma\delta}\ \ [\Omega].
> \end{gathered}
> $$
> $R_s$, the **surface resistance**, equals $\text{Re}\{\eta_2\}$. It models wall losses in waveguides and cavities (ECE 450) and lossy transmission lines (Lecture 39).

> [!example] Example — a copper mirror at 10 GHz (this site's numbers)
> $\sigma = 5.8\times10^7$ S/m gives $\delta = 0.661\ \mu$m and $R_s = 26.1$ mΩ. The mirror current $2E_0/\eta_0$ dissipates $\tfrac12R_s(2E_0/\eta_0)^2 = (4R_s/\eta_0)\langle S_i\rangle$. The absorbed fraction $4R_s/\eta_0 = 2.77\times10^{-4}$ matches $1-\lvert\Gamma\rvert^2$ from Lecture 25's exact $\Gamma$: the mirror reflects 99.97 %.

## 6. Radiation pressure

The wave's $\mathbf{B}$ acts on the moving charge carriers through the magnetic part of the Lorentz force ([[concepts/lorentz-force]]). With $N$ carriers per m³ moving at $\mathbf{v}$:

> [!key] Radiation pressure (notes' box)
> $$
> \begin{gathered}
> N\mathbf{F} = Nq\mathbf{v}\times\mathbf{B}_t = \mathbf{J}_t\times\mathbf{B}_t\ \ [\text{N/m}^3],\\[6pt]
> \mathbf{P}_{rad} = \int_0^\infty\mathbf{J}_t\times\mathbf{B}_t\,dz\ \ [\text{N/m}^2],\\[6pt]
> \langle\mathbf{P}_{rad}\rangle = \int_0^\infty\tfrac12\text{Re}\{\tilde{\mathbf{J}}_t\times\tilde{\mathbf{B}}_t^*\}\,dz = \frac{2\langle\mathbf{S}_i\rangle}{c}.
> \end{gathered}
> $$
> $\langle\mathbf{S}_i\rangle = \hat z\,\lvert E_0\rvert^2/2\eta_0$ is the incident wave's flux. The push is along $\hat x\times\hat y = +\hat z$, into the mirror.

> [!derivation]- The time average, step by step (notes, with the conjugate written in)
> $\tilde{\mathbf{J}}_t\times\tilde{\mathbf{B}}_t^* = \hat z\,(\sigma_2\tau E_0)(\mu_2\tau E_0/\eta_2)^*e^{-2\alpha_2z}$. With $\sigma_2\tau\approx2\gamma_2/\eta_0$ and $\tau/\eta_2\approx2/\eta_0$ (real), and $\int_0^\infty e^{-2\alpha_2z}dz = 1/2\alpha_2$:
> $$
> \begin{gathered}
> \langle\mathbf{P}_{rad}\rangle\approx\hat z\,\frac{\lvert E_0\rvert^2}{2}\,\text{Re}\Big\{\frac{2\gamma_2}{\eta_0}\,\frac{2\mu_2}{\eta_0}\Big\}\frac{1}{2\alpha_2}\\[6pt]
> = \hat z\,2\,\frac{\lvert E_0\rvert^2}{2\eta_0}\,\frac{\text{Re}\{\gamma_2\}}{\alpha_2}\,\frac{\mu_2}{\eta_0} = \frac{2\langle\mathbf{S}_i\rangle}{c}.
> \end{gathered}
> $$
> $\text{Re}\{\gamma_2\} = \alpha_2$, and $\mu_0/\eta_0 = \sqrt{\mu_0\epsilon_0} = 1/c$.

Reading the result:
- **Waves carry momentum.** The notes' margin gives the momentum density $\langle\mathbf{S}_i\rangle/c^2$ [N·s/m³]. Arriving at speed $c$, it is a momentum flux $\langle S_i\rangle/c$. The mirror reverses it, so it receives twice that: the 2 is the wave's recoil (the notes cite Rothman and Boughn, *Am. J. Phys.* 77, 122). A black absorber stops the wave and feels $\langle S_i\rangle/c$ (this site's).
- **Instantaneous push** (this site's, checked numerically). The same integral without the average gives $\mathbf{P}_{rad}(t) = \hat z\,\tfrac12\mu_0H_y^2(0,t) = \hat z\,(4\langle S_i\rangle/c)\cos^2\omega t$. That is the magnetic energy density at the mirror, and the force on the sheet $\mathbf{J}_s$ in the mean of the fields on its two faces, $\tfrac12\mathbf{B}(0,t)$. It pulses at $2\omega$ between zero and twice its mean.
- $\langle P_{rad}\rangle = \epsilon_0E_0^2$ equals the standing wave's $\langle w\rangle$ (§3).
- **Photons** (notes' margin). The photon density is $\lvert\langle\mathbf{S}_i\rangle\rvert/\omega c\hbar$, so each photon carries momentum $\hbar\omega/c$. A circular wave's spin density $\pm\langle S_i\rangle/\omega c$ [N·s/m²] gives $\pm\hbar$ per photon ([[3-maxwell-and-waves/24-signal-transmission-and-circular-polarization#6-orthogonal-bases|Lecture 24 §6]]).
- The notes' summary: waves not only heat, they push.

<!-- fig:stand-skin-layer -->

> [!example] Example — sunlight and a laser (this site's numbers)
> - Sunlight above the atmosphere, $\langle S_i\rangle\approx1361$ W/m² ($E_0\approx1.01$ kV/m as one cosine wave, [[3-maxwell-and-waves/20-poynting-theorem-and-monochromatic-waves#7-time-averages|Lecture 20]]): a mirror feels $2\langle S_i\rangle/c = 9.08\ \mu$Pa, a black surface $4.54\ \mu$Pa. A 100 m × 100 m mirror sail gets 0.091 N.
> - The mirror's current peaks at $2E_0/\eta_0 = 5.4$ A/m.
> - A 1 W laser beam reflected straight back pushes with $2P/c = 6.7$ nN, whatever the spot size.

> [!trap] Radiation pressure
> - The 2 is for total reflection; an absorber feels $\langle S_i\rangle/c$.
> - Use the incident flux $\langle S_i\rangle$, not the standing wave's $\langle S\rangle = 0$.
> - Pressure is per unit area. A beam of power $P$ pushes a mirror with $2P/c$.
> - $\mathbf{E}$ drives the current along $\hat x$; only $\mathbf{v}\times\mathbf{B}$ points along $\hat z$.

## 7. Summary

- PEC mirror: $\tilde{\mathbf{E}} = -j\hat x\,2E_0\sin\beta_1z$, $\tilde{\mathbf{H}} = \hat y\,(2E_0/\eta_1)\cos\beta_1z$; in time, $\sin\beta_1z\sin\omega t$ and $\cos\beta_1z\cos\omega t$.
- $\mathbf{E}$ nodes at the mirror and every $\lambda/2$; $\mathbf{H}$ nodes $\lambda/4$ away from them. $\mathbf{E}$ and $\mathbf{H}$ are 90° apart in time.
- $\langle\mathbf{S}\rangle = 0$. $\mathbf{S}$ pulses at $2\omega$, moving energy between $\mathbf{H}$ and $\mathbf{E}$ antinodes; $\langle w\rangle = \epsilon_1E_0^2$.
- $\lvert\Gamma\rvert<1$: travelling plus standing, $\lvert\tilde E\rvert$ between $(1\pm\lvert\Gamma\rvert)E_0$.
- $\mathbf{J}_s = \hat x\,(2E_0/\eta_1)\cos\omega t$; in a good conductor it is $\int\tilde{\mathbf{J}}_t\,dz$, and $R_s = 1/\sigma\delta$ gives the loss $\tfrac12R_s\lvert\tilde{\mathbf{J}}_s\rvert^2$.
- $\langle P_{rad}\rangle = 2\langle S_i\rangle/c$ (mirror), $\langle S_i\rangle/c$ (absorber); momentum density $\langle S\rangle/c^2$.
- Next, [[4-transmission-lines/27-guided-tem-waves-on-transmission-lines|Lecture 27]]: plane waves guided between conducting plates.

Concept pages: [[concepts/standing-waves]] · [[concepts/radiation-pressure]] · [[concepts/reflection-and-transmission]] · [[concepts/skin-depth]] · [[concepts/poynting-vector]] · [[concepts/lorentz-force]].

> [!exam] On exams
> The Exam 3 papers on hand ask about standing waves only conceptually, and never about radiation pressure. SP17 Exam 3 #1b–c: does a given $\sin\cdot\sin$, $\cos\cdot\cos$ pair satisfy Maxwell's equations, and do standing waves carry net power? Check both curl equations: $\beta = \omega\sqrt{\mu\epsilon}$ and the amplitude ratio $\eta$; then §3. SP19 Exam 3 #3c: what does a PEC reflection leave in front of the mirror? $\lvert\Gamma\rvert = 1$ against $\lvert\Gamma\rvert<1$ (§2). FA23 Exam 3 #1(c)–(d): the energy density of a standing wave, and a plot of fixed nodes: instantaneous against average (§3), $\mathbf{E}$ against $\mathbf{H}$ (§2 trap). See the [[problems/a-circular-wave-meets-a-mirror|worked problem]].

> [!tip] Practice this lecture
> [[practice/26-standing-waves-and-radiation-pressure|12 practice problems]] — 5 easy, 3 medium, 4 hard — each with a folded hint and a worked solution. Start with [[practice/26-standing-waves-and-radiation-pressure#261-nodes-in-front-of-a-mirror|26.1 Nodes in front of a mirror]]; the [[practice/index|practice hub]] has the whole bank by difficulty and by topic.

### Sources for this page
Kudeki notes, Lecture 26 (6 pages): the standing-wave phasors and real forms, the node figures and short/open margin notes, the $\langle\mathbf{S}\rangle = 0$ check, the surface current, the effective-surface-current and surface-resistance boxes, and the radiation-pressure box with its momentum notes. Rao (2009) §5.6, §7.1–7.2 (complete and partial standing waves). This site's own: the figures, the partial-reflection paragraph, §3's $\mathbf{S}$ and $w$, the sheet check, $R_s = 1/\sigma\delta = \text{Re}\{\eta_2\}$, the instantaneous pressure, and the examples; numbers checked by script. Slips in the notes (a missing conjugate, a citation year, a $\Gamma>0$ margin figure) are on the errata page.
