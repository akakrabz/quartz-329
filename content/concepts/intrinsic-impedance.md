---
title: "Intrinsic impedance"
description: "η = √(μ/ε), the |E|/|H| of one plane wave: 376.7 Ω in vacuum, complex (H lags E) in a conductor."
tags: [concept, waves]
aliases: ["wave impedance", "impedance of free space"]
---

> [!key] Definition
> $$
> \eta\equiv\sqrt{\frac{\mu}{\epsilon}} = \mu v = \frac{1}{\epsilon v} = \eta_0\sqrt{\frac{\mu_r}{\epsilon_r}}\ [\Omega],\qquad \eta_0 = \sqrt{\frac{\mu_0}{\epsilon_0}} = 376.7\ \Omega\approx120\pi\ \Omega .
> $$
> One plane wave along $\hat u$: $\mathbf{H} = \hat u\times\mathbf{E}/\eta$, so $\lvert\mathbf{E}\rvert = \eta\lvert\mathbf{H}\rvert$, $\lvert\mathbf{B}\rvert = \lvert\mathbf{E}\rvert/v$. For $\mathbf{E} = \hat xE_x$: $E_x/H_y = +\eta$ toward $+z$, $-\eta$ toward $-z$.

**Physics.** Faraday's law $\partial E_x/\partial z = -\mu\,\partial H_y/\partial t$ turns $E_x = f(t - z/v)$ into $H_y = f/(\mu v)$. Units: H/F = Ω². Not a resistor: nothing is dissipated (Lecture 20). A line's $\sqrt{\mathcal{L}/\mathcal{C}}$ is $\eta$ times geometry: $(\eta/2\pi)\ln(b/a)$ (coax), $\eta\,d/W$ (plates).

**Examples.**
- Vacuum, 1 V/m: $H = 2.65$ mA/m, $B = 3.34$ nT.
- $\mu_0$, $\epsilon_r = 2.25$, 4, 9: 251 Ω ($80\pi$), 188 Ω ($60\pi$), 126 Ω ($40\pi$). Or $\eta = \mu_0v$: $2\times10^8$ m/s gives $251.3\ \Omega$.
- $\mu_r = 2$, $\epsilon_r = 8$: $\eta_0/2 = 188\ \Omega$ as for $\epsilon_r = 4$, but speed $c/4$ ($\eta$ follows the ratio, $v$ the product).
- Polyethylene coax, $b/a = 3.5$: $0.199\times251\ \Omega = 50\ \Omega$ ([[problems/coax-inductance-and-the-lc-product]]).

> [!trap]
> - $H = E/\eta$, not $E\eta$; the notes' $\sqrt{\epsilon/\mu}$ is $1/\eta$.
> - The medium's $\eta$: 6 V/m in polyethylene → $6/251.3 = 23.9$ mA/m, not $6/377 = 15.9$.
> - $\pm\eta$ is for one wave: $E_x = Af + Bg$, $H_y = (Af - Bg)/\eta$ give $\eta\,(Af+Bg)/(Af-Bg)$.
> - $120\pi = 376.99\ \Omega$ vs $376.73\ \Omega$ (0.07 %): either; say which.

**In a conducting medium (Lecture 22).** $j\omega\epsilon\to\sigma + j\omega\epsilon$:

> [!key] Complex intrinsic impedance
> $$
> \begin{gathered}
> \eta = \sqrt{\frac{j\omega\mu}{\sigma + j\omega\epsilon}} = \lvert\eta\rvert e^{j\tau},\\[6pt]
> \gamma\eta = j\omega\mu,\qquad \frac{\gamma}{\eta} = \sigma + j\omega\epsilon,\\[6pt]
> \lvert\eta\rvert = \frac{\sqrt{\mu/\epsilon}}{\big[1 + (\sigma/\omega\epsilon)^2\big]^{1/4}},\\[6pt]
> \tau = \frac12\tan^{-1}\frac{\sigma}{\omega\epsilon}\quad(0\le\tau<45^\circ).
> \end{gathered}
> $$
> Still $\tilde{\mathbf{H}} = \hat u\times\tilde{\mathbf{E}}/\eta$: $\mathbf{H}$ lags $\mathbf{E}$ by $\tau$, amplitude ratio $\lvert\eta\rvert$ ($\gamma$: [[concepts/propagation-constant|propagation constant]]).

$\lvert\gamma\rvert\lvert\eta\rvert = \omega\mu$: conduction raises $\lvert\gamma\rvert$ and lowers $\lvert\eta\rvert$. Limits ([[concepts/loss-tangent|σ/ωε]]): imperfect dielectric $\tau\approx\sigma/2\omega\epsilon$ rad, $\lvert\eta\rvert\approx\sqrt{\mu/\epsilon}$; good conductor $\eta\approx\sqrt{\omega\mu/\sigma}\,e^{j\pi/4}$ ([[3-maxwell-and-waves/23-imperfect-dielectrics-and-good-conductors|Lecture 23]]).

- Lecture 22: $\gamma = 1 + j3$ m⁻¹, $\omega = 3\times10^8$ rad/s, $\mu_0$: $\eta = j\omega\mu_0/\gamma = 12\pi(3 + j) = 119.2\,e^{j18.4^\circ}\ \Omega$; lossless ($8\epsilon_0$) $133.3\ \Omega$.
- $\mu = 3\mu_0$, $\epsilon = 9\epsilon_0$, $\sigma/\omega\epsilon = 4/3$: $24\pi(2 + j) = 168.6\,e^{j26.6^\circ}\ \Omega$; lossless $217.7\ \Omega$.
- $\sigma = \omega\epsilon$: $\lvert\eta\rvert = 2^{-1/4}\sqrt{\mu/\epsilon} = 0.84\sqrt{\mu/\epsilon}$, $\tau = 22.5^\circ$.
- Current sheet: $\mathbf{E} = -\tfrac\eta2\mathbf{J}_s$, shifted by $\tau$ (Lecture 22 §7).

> [!trap]
> - $\sqrt{\mu/\epsilon}$ needs $\sigma = 0$; else $j\omega\mu/\gamma$.
> - $\tilde{\mathbf{E}}/\eta$ subtracts $\tau$, $\eta\tilde{\mathbf{H}}$ adds it: $\mathbf{H}$ lags.
> - $\lvert\eta\rvert$ is an *amplitude* ratio; $E_x(t)/H_y(t)$ varies.
> - Collisionless plasma below $f_p$: $\eta$ imaginary (90°), no average power (Lecture 22 §8).

**Where it appears.** [[3-maxwell-and-waves/18-the-wave-equation-and-plane-tem-waves|Lecture 18]]; [[3-maxwell-and-waves/19-dalembert-solutions-and-radiation-from-current-sheets|Lecture 19]] (a sheet sees $\eta/2$, so $\eta J_s/2$ per side; [[concepts/current-sheet-radiation]]); Lecture 20 ($E^2/\eta$); [[3-maxwell-and-waves/22-phasor-maxwell-equations-and-damped-waves|Lecture 22]]; Lecture 23 ($\cos\tau$ in power); Lecture 25 (reflection); [[problems/a-pulse-on-the-move]]; [[problems/decoding-a-damped-wave]].

**Practice.** [[practice/topics#plane-waves-and-the-wave-equation|Plane waves and the wave equation]] (25 problems) — for example [[practice/18-wave-equation-and-plane-waves#181-which-way-and-how-fast|18.1 Which way and how fast]] (easy), [[practice/18-wave-equation-and-plane-waves#186-which-fields-can-be-waves|18.6 Which fields can be waves]] (medium), [[practice/18-wave-equation-and-plane-waves#189-triangle-pulse-in-a-magnetic-medium|18.9 Triangle pulse in a magnetic medium]] (hard).

Related: [[concepts/plane-waves]] · [[concepts/wave-equation]] · [[concepts/permittivity]] · [[concepts/permeability]] · [[concepts/inductance]] · [[concepts/capacitance]].
