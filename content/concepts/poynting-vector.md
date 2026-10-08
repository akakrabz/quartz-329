---
title: "Poynting vector"
description: "S = E × H, in W/m². It points in the direction a plane wave travels, which is the direction its energy flows, and its size is the instantaneous power crossing a unit area perpendicular to it. For one plane wave |S| = |E|²/η = η|H|². Poynting's theorem, which explains why, is Lecture 20."
tags: [concept, waves]
aliases: ["Poynting's vector", "S = E x H", "power density of a wave", "energy flux density"]
---

> [!key] Definition
> $$
> \mathbf{S}\equiv\mathbf{E}\times\mathbf{H}\quad[\text{W/m}^2],
> $$
> evaluated at one point and one instant (the **instantaneous** Poynting vector). For a single uniform plane wave travelling along $\hat u$, $\mathbf{S} = \hat u\,\lvert\mathbf{E}\rvert^2/\eta = \hat u\,\eta\lvert\mathbf{H}\rvert^2$. Units: (V/m)(A/m) = W/m².

**Physics.** Lecture 19 uses $\mathbf{S}$ in two ways. In the notes it is the definition of the propagation direction of a uniform plane TEM wave: $\mathbf{E}$ and $\mathbf{H}$ are transverse, and the wave moves along $\mathbf{E}\times\mathbf{H}$. That is also how $\mathbf{H}$ is found from $\mathbf{E}$: divide by $\eta$ and rotate so that $\mathbf{E}\times\mathbf{H}$ points along the travel. The slides add the physical meaning, stated without proof: $\mathbf{S}$ points along the flow of energy, and its size is the energy flux density, the power per unit area crossing a surface perpendicular to it. For a plane wave $\mathbf{E}\perp\mathbf{H}$, so $\lvert\mathbf{S}\rvert = \lvert\mathbf{E}\rvert\lvert\mathbf{H}\rvert$, and $\lvert\mathbf{E}\rvert = \eta\lvert\mathbf{H}\rvert$ gives the two forms above. $\mathbf{S}$ along the travel is never negative for a single wave, even when $\mathbf{E}$ and $\mathbf{H}$ change sign, because they change sign together.

Where the energy comes from: at a radiating current sheet $\mathbf{E}$ opposes $\mathbf{J}_s$, so $-\mathbf{J}_s\cdot\mathbf{E}>0$ is the power per unit area the current gives up. It equals the total $\lvert\mathbf{S}\rvert$ leaving the two faces. Poynting's theorem, which derives the meaning of $\mathbf{S}$ from Maxwell's equations and balances it against stored energy and $\mathbf{J}\cdot\mathbf{E}$, is Lecture 20 material, and so are time averages.

**Examples.**
- Sinusoidal current sheet (slides): $\mathbf{J}_s = -J_{s0}\cos(\omega t)\,\hat x$ on $z = 0$ in free space gives $\mathbf{S} = \pm\hat z\,\tfrac{\eta_0J_{s0}^2}{4}\cos^2(\omega t\mp\beta z)$ for $z\gtrless0$, pointing away from the sheet on both sides. For $J_{s0} = 1$ A/m the peak is $\eta_0/4 = 94.2$ W/m² per side.
- At the sheet the two sides together carry $\tfrac{\eta_0}{2}J_s^2 = -\mathbf{J}_s\cdot\mathbf{E}$.
- A 1 V/m plane wave in vacuum has $\lvert\mathbf{S}\rvert = (1\ \text{V/m})^2/377\ \Omega = 2.65$ mW/m².
- Worked problem: at $x = 0.75$ m, $t = 6$ ns, $E_z = -283$ V/m and $H_y = +1.5$ A/m give $\mathbf{S} = (-283)(1.5)\,\hat z\times\hat y = +\hat x\,424$ W/m², away from the sheet.

> [!trap]
> - Order matters: $\mathbf{E}\times\mathbf{H}$, not $\mathbf{H}\times\mathbf{E}$. The reverse order points back toward the source.
> - $\lvert\mathbf{E}\rvert^2/\eta$, not $\lvert\mathbf{E}\rvert^2\eta$: 1 V/m carries milliwatts per square metre.
> - The instantaneous $\mathbf{S}$ of a cosine wave oscillates between 0 and its peak at twice the frequency. Its time average is half the peak; time averages come in Lecture 20 and phasor forms in Lecture 21.
> - $\mathbf{S}$ is not additive in general. Two waves travelling the *same* way along $\hat u$ give $\mathbf{S} = \hat u\,\lvert\mathbf{E}_1 + \mathbf{E}_2\rvert^2/\eta$, not the sum of the separate $\mathbf{S}$ values. (For two waves travelling in *opposite* directions along the same line the cross terms cancel, and $\mathbf{S} = \hat u\,(\lvert\mathbf{E}_1\rvert^2 - \lvert\mathbf{E}_2\rvert^2)/\eta$.)

**Where it appears.** [[3-maxwell-and-waves/18-the-wave-equation-and-plane-tem-waves|Lecture 18]] (named; the direction rule); [[3-maxwell-and-waves/19-dalembert-solutions-and-radiation-from-current-sheets|Lecture 19]] (the propagation direction of TEM waves; the sheet's sinusoidal $\mathbf{S}$ as power per unit area); Lecture 20 (Poynting's theorem, time averages); [[problems/a-current-sheet-launches-two-waves]].

**Practice.** [[practice/topics#current-sheet-radiation-and-the-poynting-vector|Current-sheet radiation and the Poynting vector]] (10 problems) — for example [[practice/19-radiation-from-current-sheets#192-a-sheet-on-the-y--0-plane|19.2 A sheet on the y = 0 plane]] (easy), [[practice/19-radiation-from-current-sheets#196-a-triangle-pulse-in-glass|19.6 A triangle pulse in glass]] (medium), [[practice/19-radiation-from-current-sheets#199-a-sheet-launches-a-step-and-a-ramp|19.9 A sheet launches a step and a ramp]] (hard).

Related: [[concepts/plane-waves]] · [[concepts/current-sheet-radiation]] · [[concepts/intrinsic-impedance]] · [[concepts/electrostatic-energy]] · [[concepts/magnetic-energy]].
