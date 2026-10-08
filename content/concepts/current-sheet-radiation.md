---
title: "Radiation from a current sheet"
description: "An infinite sheet of time-varying surface current Jₛ(t) launches one uniform plane wave from each face. The fields are E = −(η/2)Jₛ(t − d/v) and H = ½Jₛ(t − d/v) × n̂, with n̂ pointing toward the field point and d the distance from the sheet. E is the same on both sides and opposes the current; H reverses and jumps by Jₛ."
tags: [concept, waves]
aliases: ["current sheet radiation", "radiating current sheet", "sheet current source", "radiation from current sheets"]
---

> [!key] Definition
> A uniform surface current $\mathbf{J}_s(t)$ [A/m] on an infinite plane, in a homogeneous lossless medium ($\eta = \sqrt{\mu/\epsilon}$, $v = 1/\sqrt{\mu\epsilon}$), radiates
> $$
> \mathbf{E} = -\frac\eta2\,\mathbf{J}_s\Big(t - \frac dv\Big),\qquad \mathbf{H} = \frac12\,\mathbf{J}_s\Big(t - \frac dv\Big)\times\hat n,
> $$
> where $d$ is the distance from the sheet and $\hat n$ is the unit normal pointing from the sheet toward the field point. For the sheet $\mathbf{J}_s = \hat x\,f(t)$ on $z = 0$ (the notes' case), this reads $\mathbf{E} = -\hat x\,\tfrac\eta2f(t\mp z/v)$ and $\mathbf{H} = \mp\hat y\,\tfrac12f(t\mp z/v)$ for $z\gtrless0$.

**Physics.** Each face of the sheet launches a uniform plane wave that travels away from it, with $\mathbf{E}\times\mathbf{H}$ along $+\hat n$. Three facts fix the fields.

- **The static limit** is the Lecture 13 sheet, $\mathbf{H} = \tfrac12\mathbf{J}_s\times\hat n$ with no $\mathbf{E}$.
- **Causality** delays the response by the travel time $d/v$ and allows only outgoing waves, $t - d/v$.
- **The boundary conditions** at the sheet set the amplitude. Tangential $\mathbf{E}$ is continuous, so $\mathbf{E}$ is the same on both faces. Tangential $\mathbf{H}$ jumps by $J_s$: $\hat n_{21}\times(\mathbf{H}_1 - \mathbf{H}_2) = \mathbf{J}_s$, which gives $J_s/2$ on each side. Then $\lvert\mathbf{E}\rvert = \eta\lvert\mathbf{H}\rvert = \eta J_s/2$.

The displacement current is what turns the static field into a wave: without it the field would follow $J_s(t)$ instantly at every distance. $\mathbf{E}$ opposes the current, so $\mathbf{J}_s\cdot\mathbf{E} = -\tfrac\eta2\lvert\mathbf{J}_s\rvert^2<0$: the sheet gives energy to the field, at the rate $\tfrac\eta2J_s^2$ per unit area, which the two waves carry away ([[concepts/poynting-vector]]). Seen from the source, the sheet drives two half-spaces of impedance $\eta$ in parallel, hence the $\eta/2$.

**Examples.**
- Vacuum, 1 A/m: $\lvert\mathbf{E}\rvert = \eta_0/2 = 188$ V/m ($60\pi$) and $\lvert\mathbf{H}\rvert = 0.5$ A/m on each side.
- Notes' Example 4: a ramp current from $-1$ to $+1$ A/m in 1 µs gives, at $t = 2$ µs, 300 m long ramps of $H_y$ ($\pm0.5$ A/m) and $E_x$ ($\pm60\pi$ V/m) between 450 and 750 m on each side.
- Slide 17: $\mathbf{J}_s = -J_s\hat z$ on $y = 0$ gives $\mathbf{H} = \pm\tfrac12J_s\hat x$ and $\mathbf{E} = +\tfrac{\eta_0}2J_s\hat z$ for $y\gtrless0$; $\hat z\times\hat x = +\hat y$ ✓.
- Cosine current $J_{s0}\cos\omega t$: waves $\cos(\omega t - \beta d)$ with $\beta = \omega/v$ and power density $\tfrac{\eta J_{s0}^2}{4}\cos^2(\omega t - \beta d)$ on each side.
- Worked problem: a sheet on $x = 0$ with $\mathbf{J}_s = \hat zJ_s(t)$ in a dielectric with $\epsilon_r = 4$ has $\mathbf{H} = \pm\tfrac12J_s\,\hat y$ for $x\gtrless0$ and $\mathbf{E} = -\tfrac\eta2J_s\,\hat z$, with $\eta\approx188\ \Omega$; $(-\hat z)\times\hat y = +\hat x$ ✓.

> [!trap]
> - $\mathbf{E}$ has **no** $\mp$: it is the same on both faces (continuous). Only $\mathbf{H}$ flips.
> - The normal in $\tfrac12\mathbf{J}_s\times\hat n$ points toward the field point, so it changes sign across the sheet.
> - The argument is $t - d/v$ on both sides: $t - z/v$ above a sheet on $z = 0$ and $t + z/v$ below it.
> - Each side gets half: $\eta J_s/2$ and $J_s/2$, not $\eta J_s$ and $J_s$.
> - The notes write $\mathbf{J}_s = +\hat xJ_x$ and the slides $-J_s\hat x$, so their formulas differ by a sign. Compare $\mathbf{E}$ with $\mathbf{J}_s$, not formula with formula.
> - A probe's record is the source current delayed (and scaled); a snapshot plotted against distance from the sheet is the source waveform mirrored (the front, emitted first, is farthest out). Against the coordinate itself this is a mirror image on the $+$ side only.

**Where it appears.** [[3-maxwell-and-waves/19-dalembert-solutions-and-radiation-from-current-sheets|Lecture 19]] (derived by both routes; Example 4; slides 17–21); [[3-maxwell-and-waves/18-the-wave-equation-and-plane-tem-waves|Lecture 18]] (the slides' symmetry argument); [[2-magnetostatics/13-current-sheets-solenoids-and-the-vector-potential|Lecture 13]] (the static limit); [[3-maxwell-and-waves/16-charge-conservation-displacement-current-and-maxwells-equations|Lecture 16]] (the jump conditions); Lecture 20 (the energy balance); SP18 Exam 2 #5; [[problems/a-current-sheet-launches-two-waves]].

**Practice.** [[practice/topics#current-sheet-radiation-and-the-poynting-vector|Current-sheet radiation and the Poynting vector]] (10 problems) — for example [[practice/19-radiation-from-current-sheets#192-a-sheet-on-the-y--0-plane|19.2 A sheet on the y = 0 plane]] (easy), [[practice/19-radiation-from-current-sheets#196-a-triangle-pulse-in-glass|19.6 A triangle pulse in glass]] (medium), [[practice/19-radiation-from-current-sheets#199-a-sheet-launches-a-step-and-a-ramp|19.9 A sheet launches a step and a ramp]] (hard).

Related: [[concepts/plane-waves]] · [[concepts/intrinsic-impedance]] · [[concepts/poynting-vector]] · [[concepts/boundary-conditions]] · [[concepts/amperes-law]] · [[concepts/displacement-current]].
