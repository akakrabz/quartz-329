---
title: "Radiation from a current sheet"
description: "An infinite current sheet Jₛ(t) launches one plane wave from each face."
tags: [concept, waves]
aliases: ["current sheet radiation", "radiating current sheet", "sheet current source", "radiation from current sheets"]
---

> [!key] Definition
> A uniform $\mathbf{J}_s(t)$ [A/m] on an infinite plane, in a lossless medium ($\eta = \sqrt{\mu/\epsilon}$, $v = 1/\sqrt{\mu\epsilon}$), radiates
> $$
> \mathbf{E} = -\frac\eta2\,\mathbf{J}_s\Big(t - \frac dv\Big),\qquad \mathbf{H} = \frac12\,\mathbf{J}_s\Big(t - \frac dv\Big)\times\hat n,
> $$
> $d$: distance from the sheet; $\hat n$: unit normal from the sheet toward the field point. Notes' case $\mathbf{J}_s = \hat x\,f(t)$ on $z = 0$: $\mathbf{E} = -\hat x\,\tfrac\eta2f(t\mp z/v)$, $\mathbf{H} = \mp\hat y\,\tfrac12f(t\mp z/v)$ for $z\gtrless0$.

**Physics.** Each face launches an outgoing plane wave ($\mathbf{E}\times\mathbf{H}$ along $+\hat n$), fixed by:

- **Static limit**: the Lecture 13 sheet, $\mathbf{H} = \tfrac12\mathbf{J}_s\times\hat n$, no $\mathbf{E}$.
- **Causality**: delay $d/v$, outgoing waves only ($t - d/v$).
- **Boundary conditions**: tangential $\mathbf{E}$ continuous; tangential $\mathbf{H}$ jumps, $\hat n_{21}\times(\mathbf{H}_1 - \mathbf{H}_2) = \mathbf{J}_s$, so $J_s/2$ each side and $\lvert\mathbf{E}\rvert = \eta\lvert\mathbf{H}\rvert = \eta J_s/2$.

Without displacement current the field would follow $J_s(t)$ instantly everywhere: no wave. $\mathbf{E}$ opposes the current, $\mathbf{J}_s\cdot\mathbf{E} = -\tfrac\eta2\lvert\mathbf{J}_s\rvert^2<0$: the sheet feeds the field $\tfrac\eta2J_s^2$ per unit area, carried off by the waves ([[concepts/poynting-vector]]). The source sees two half-spaces of $\eta$ in parallel, hence $\eta/2$.

**Examples.**
- Vacuum, 1 A/m: $\lvert\mathbf{E}\rvert = \eta_0/2 = 188$ V/m ($60\pi$), $\lvert\mathbf{H}\rvert = 0.5$ A/m each side.
- Notes' Example 4: a ramp from $-1$ to $+1$ A/m in 1 µs; at $t = 2$ µs, 300 m ramps of $H_y$ ($\pm0.5$ A/m) and $E_x$ ($\pm60\pi$ V/m) between 450 and 750 m each side.
- Slide 17: $\mathbf{J}_s = -J_s\hat z$ on $y = 0$: $\mathbf{H} = \pm\tfrac12J_s\hat x$, $\mathbf{E} = +\tfrac{\eta_0}2J_s\hat z$ for $y\gtrless0$; $\hat z\times\hat x = +\hat y$ ✓.
- $J_{s0}\cos\omega t$: waves $\cos(\omega t - \beta d)$, $\beta = \omega/v$, power density $\tfrac{\eta J_{s0}^2}{4}\cos^2(\omega t - \beta d)$ per side.
- $\mathbf{J}_s = \hat zJ_s(t)$ on $x = 0$, $\epsilon_r = 4$: $\mathbf{H} = \pm\tfrac12J_s\,\hat y$ for $x\gtrless0$, $\mathbf{E} = -\tfrac\eta2J_s\,\hat z$, $\eta\approx188\ \Omega$; $(-\hat z)\times\hat y = +\hat x$ ✓.

> [!trap]
> - $\mathbf{E}$ has **no** $\mp$: continuous, the same on both faces. Only $\mathbf{H}$ flips.
> - $\hat n$ points toward the field point, so it flips across the sheet.
> - $t - d/v$ on both sides: $t - z/v$ above $z = 0$, $t + z/v$ below.
> - Half each side: $\eta J_s/2$ and $J_s/2$, not $\eta J_s$ and $J_s$.
> - The notes' $+\hat xJ_x$ and the slides' $-J_s\hat x$ differ by a sign: compare $\mathbf{E}$ with $\mathbf{J}_s$.
> - A probe records the source waveform delayed; a snapshot against distance shows it mirrored (front farthest out); against the coordinate, mirrored on the $+$ side only.

**Where it appears.** [[3-maxwell-and-waves/19-dalembert-solutions-and-radiation-from-current-sheets|Lecture 19]] (derived; slides 17–21); [[3-maxwell-and-waves/18-the-wave-equation-and-plane-tem-waves|Lecture 18]] (symmetry argument); [[2-magnetostatics/13-current-sheets-solenoids-and-the-vector-potential|Lecture 13]] (static limit); [[3-maxwell-and-waves/16-charge-conservation-displacement-current-and-maxwells-equations|Lecture 16]] (jump conditions); Lecture 20 (energy); SP18 Exam 2 #5; [[problems/a-current-sheet-launches-two-waves]].

**Practice.** [[practice/topics#current-sheet-radiation-and-the-poynting-vector|Current-sheet radiation and the Poynting vector]] (15 problems) — for example [[practice/19-radiation-from-current-sheets#192-a-sheet-on-the-y--0-plane|19.2 A sheet on the y = 0 plane]] (easy), [[practice/19-radiation-from-current-sheets#196-a-triangle-pulse-in-glass|19.6 A triangle pulse in glass]] (medium), [[practice/19-radiation-from-current-sheets#199-a-sheet-launches-a-step-and-a-ramp|19.9 A sheet launches a step and a ramp]] (hard).

Related: [[concepts/plane-waves]] · [[concepts/intrinsic-impedance]] · [[concepts/boundary-conditions]] · [[concepts/amperes-law]] · [[concepts/displacement-current]].
