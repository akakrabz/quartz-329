---
title: "Poynting vector"
description: "S = E × H in W/m²: the direction and density of energy flow; |E|²/η for one plane wave, E₀²/2η on average for a cosine wave."
tags: [concept, waves]
aliases: ["Poynting's vector", "S = E x H", "E × H", "power density of a wave", "power density of a plane wave", "energy flux density", "time-average Poynting vector"]
---

> [!key] Definition
> $$
> \mathbf{S}\equiv\mathbf{E}\times\mathbf{H}\quad[\text{W/m}^2],
> $$
> at one point and instant (**instantaneous**). One plane wave along $\hat u$: $\mathbf{S} = \hat u\,\lvert\mathbf{E}\rvert^2/\eta = \hat u\,\eta\lvert\mathbf{H}\rvert^2$. Units: (V/m)(A/m) = VA/m² = W/m² = (J/s)/m², as $\mathbf{J}$ is (C/s)/m² = A/m².

**Physics.** In the notes (Lecture 19 §7), travel of a TEM wave is *along* $\mathbf{E}\times\mathbf{H}$: the definition that pairs $\mathbf{H}$ with $\mathbf{E}$ ([[concepts/plane-waves|Plane waves]]), divide by $\eta$, rotate. The slides add, unproved, that its size is power per area, W/m² (V/m × A/m): $\mathbf{S}$ is the energy flux density. [[concepts/poynting-theorem|Poynting's theorem]] ([[3-maxwell-and-waves/20-poynting-theorem-and-monochromatic-waves#3-reading-the-three-terms|Lecture 20 §3]]) proves it: $\partial w/\partial t + \nabla\cdot\mathbf{S} + \mathbf{J}\cdot\mathbf{E} = 0$ with $w = \tfrac12\epsilon E^2 + \tfrac12\mu H^2$, so $\mathbf{S}$ gives the flow direction and the power per unit perpendicular area, and $\nabla\cdot\mathbf{S}>0$ means energy leaving that point. $\mathbf{E}\perp\mathbf{H}$ gives $\lvert\mathbf{S}\rvert = \lvert\mathbf{E}\rvert\lvert\mathbf{H}\rvert$; for one wave $\mathbf{S}$ never reverses, as $\mathbf{E}$ and $\mathbf{H}$ change sign together, and it pulses at $2\omega$ (humps $\lambda/2$ apart, moving at $v$). At a radiating sheet $\mathbf{E}$ opposes $\mathbf{J}_s$: $-\mathbf{J}_s\cdot\mathbf{E}>0$ is the power given up, equal at every instant to the $\lvert\mathbf{S}\rvert$ leaving both faces. The theorem fixes only $\oint\mathbf{S}\cdot d\mathbf{A}$: static fields can have a circulating $\mathbf{E}\times\mathbf{H}$ that carries nothing. A resistive wire takes its $I^2R$ in through its sides.

**Examples.**
- Slides (Lecture 19 §7): $\mathbf{J}_s = -J_{s0}\cos(\omega t)\,\hat x$ on $z = 0$, free space ([[concepts/current-sheet-radiation|Radiation from a current sheet]]):
$$
\mathbf{S} = \mathbf{E}\times\mathbf{H} = \pm\hat z\,\frac{\eta_0J_{s0}^2}{4}\cos^2(\omega t\mp\beta z)\ \ \text{W/m}^2,\qquad z\gtrless0 .
$$
Outward on both sides and never negative ($\cos^2\ge0$): pulses at twice the source frequency. $\lvert\mathbf{S}\rvert = \lvert\mathbf{E}\rvert^2/\eta_0 = \eta_0\lvert\mathbf{H}\rvert^2$; for $J_{s0} = 1$ A/m the peak is $\eta_0/4 = 94.2$ W/m² per side. The two sides together carry $\eta_0J_s^2/2$, exactly $-\mathbf{J}_s\cdot\mathbf{E}$ at the sheet ($\mathbf{J}_s\cdot\mathbf{E} = -\tfrac\eta2\lvert\mathbf{J}_s\rvert^2<0$: the charges work on the field; in a resistor $\mathbf{J}\cdot\mathbf{E}>0$).
- Notes (Lecture 20): $\mathbf{J}_s = \hat x\,2\cos\omega t$ A/m in vacuum: $\mathbf{S} = \pm\hat z\,\eta_0\cos^2(\omega t\mp\beta z)$ W/m², peak $\eta_0\approx377$ W/m² per side, $\mathbf{J}_s\cdot\mathbf{E} = -2\eta_0\cos^2\omega t$ W/m² ([[concepts/current-sheet-radiation|Radiation from a current sheet]]).
- 1 V/m in vacuum: $(1\ \text{V/m})^2/377\ \Omega = 2.65$ mW/m².
- $x = 0.75$ m, $t = 6$ ns: $E_z = -283$ V/m, $H_y = +1.5$ A/m give $(-283)(1.5)\,\hat z\times\hat y = +\hat x\,424$ W/m², away from the sheet.
- DC coax: $\mathbf{S} = \hat z\,VI/(2\pi\rho^2\ln(b/a))$ in the dielectric, integrating to $VI$ ([[concepts/poynting-theorem|Poynting's theorem]]).

**Time averages** ([[concepts/time-average-power|Time averages and average power]]). $\langle\mathbf{S}\rangle = \frac1T\int_0^T\mathbf{E}\times\mathbf{H}\,dt = \tfrac12\text{Re}\{\tilde{\mathbf{E}}\times\tilde{\mathbf{H}}^*\}$; $\cos^2(\omega t + \phi) = \tfrac12[1 + \cos(2\omega t + 2\phi)]$ averages to $\tfrac12$:
- cosine plane wave: $\langle\mathbf{S}\rangle = \hat u\,E_0^2/(2\eta) = \hat u\,\tfrac12\eta H_0^2 = \hat u\,\tfrac12E_0H_0$; energy moves at $v$, $\langle S\rangle = v\langle w\rangle$, $\langle w\rangle = \tfrac12\epsilon E_0^2$;
- sheet $J_0\cos\omega t$: $\eta J_0^2/8$ per side, $\langle-\mathbf{J}_s\cdot\mathbf{E}\rangle = \eta J_0^2/4$ injected; the notes' $J_0 = 2$ A/m: $\eta_0/2\approx188$ W/m² per side, $\eta_0\approx377$ W/m² total;
- $\hat x\,E_1\cos(\omega t - \beta z) + \hat y\,E_2\cos(\omega t - \beta z + \phi)$: $(E_1^2 + E_2^2)/(2\eta)$, any $\phi$;
- two equal opposite waves: $\mathbf{S}\neq0$ mostly, yet $\langle\mathbf{S}\rangle = 0$;
- steady state: $\oint\langle\mathbf{S}\rangle\cdot d\mathbf{A} = -\int\langle\mathbf{J}\cdot\mathbf{E}\rangle\,dV$.

Sunlight, about 1361 W/m², is $E_0\approx1.0$ kV/m.

> [!trap]
> - $\mathbf{E}\times\mathbf{H}$, not $\mathbf{H}\times\mathbf{E}$ (points back at the source).
> - $\lvert\mathbf{E}\rvert^2/\eta$, not $\lvert\mathbf{E}\rvert^2\eta$.
> - A cosine wave's $\mathbf{S}$ swings from 0 to peak at $2\omega$; the average is half the peak. Phasor forms: [[concepts/time-average-power|Time averages and average power]].
> - Not additive: same-way waves give $\hat u\,\lvert\mathbf{E}_1 + \mathbf{E}_2\rvert^2/\eta$; opposite ones, $\hat u\,(\lvert\mathbf{E}_1\rvert^2 - \lvert\mathbf{E}_2\rvert^2)/\eta$.

> [!exam] On exams
> Power of a wave: $E_0^2/(2\eta)$, exact with $\eta_0 = 120\pi$; direction from $\mathbf{E}\times\mathbf{H}$ (do the cross product). A sheet's waves (Lecture 19): $\mathbf{S}$ away from the sheet on both sides, magnitude $\lvert\mathbf{E}\rvert\lvert\mathbf{H}\rvert = \eta J_s^2/4$ per side, half the injected $-\mathbf{J}_s\cdot\mathbf{E}$. Methods and papers: [[concepts/time-average-power|Time averages and average power]].

**Where it appears.** [[3-maxwell-and-waves/18-the-wave-equation-and-plane-tem-waves#5-h-from-e-the-intrinsic-impedance|Lecture 18 §5]] (direction rule only); [[3-maxwell-and-waves/19-dalembert-solutions-and-radiation-from-current-sheets#7-a-sinusoidal-sheet-current-β-λ-and-the-poynting-vector-slides|Lecture 19 §7]] (named; the sinusoidal sheet's $\mathbf{S}$); [[3-maxwell-and-waves/20-poynting-theorem-and-monochromatic-waves#3-reading-the-three-terms|Lecture 20 §3]] (theorem, wire, averages); [[problems/a-current-sheet-launches-two-waves|Worked problem — A current sheet launches two waves]]; [[problems/energy-bookkeeping-for-a-radiating-sheet|Worked problem — Energy bookkeeping for a radiating sheet]].

**Related.** [[concepts/poynting-theorem|Poynting's theorem]] · [[concepts/time-average-power|Time averages and average power]] · [[concepts/plane-waves|Plane waves]] · [[concepts/current-sheet-radiation|Radiation from a current sheet]] · [[concepts/intrinsic-impedance|Intrinsic impedance]] · [[concepts/electrostatic-energy|Electrostatic energy]] · [[concepts/magnetic-energy|Magnetic energy]].

**Practice.** [[practice/topics#current-sheet-radiation-and-the-poynting-vector|Current-sheet radiation and the Poynting vector]] (15 problems) · [[practice/topics#poyntings-theorem-energy-flow-and-time-average-power|Poynting's theorem, energy flow and time-average power]] (44 problems) — for example [[practice/19-radiation-from-current-sheets#192-a-sheet-on-the-y--0-plane|19.2 A sheet on the y = 0 plane]] (easy), [[practice/19-radiation-from-current-sheets#196-a-triangle-pulse-in-glass|19.6 A triangle pulse in glass]] (medium), [[practice/19-radiation-from-current-sheets#199-a-sheet-launches-a-step-and-a-ramp|19.9 A sheet launches a step and a ramp]] (hard).
