---
title: "Poynting's theorem"
description: "∂w/∂t + ∇·S + J·E = 0: Maxwell's equations as an energy ledger."
tags: [concept, waves]
aliases: ["Poynting theorem", "electromagnetic energy conservation", "energy conservation for fields", "Joule heating"]
---

> [!key] Definition
> $$
> \begin{gathered}
> \frac{\partial w}{\partial t} + \nabla\cdot\mathbf{S} + \mathbf{J}\cdot\mathbf{E} = 0,\\[4pt]
> w = \tfrac12\epsilon E^2 + \tfrac12\mu H^2\ [\text{J/m}^3],\\[4pt]
> \mathbf{S} = \mathbf{E}\times\mathbf{H}\ [\text{W/m}^2],
> \end{gathered}
> $$
> and, over $V$ with outward $d\mathbf{A}$ on its closed surface $A$,
> $$
> \begin{gathered}
> -\frac{dW}{dt} = \oint_A\mathbf{S}\cdot d\mathbf{A} + \int_V\mathbf{J}\cdot\mathbf{E}\,dV,\\[4pt]
> W = \int_Vw\,dV .
> \end{gathered}
> $$
> Linear, isotropic, time-invariant $\epsilon$, $\mu$; free $\mathbf{J}$. Terms in W/m³ (integral form: W).

**Physics.** Dot Faraday's law with $\mathbf{H}$, Ampère–Maxwell with $\mathbf{E}$, subtract: $\nabla\cdot(\mathbf{E}\times\mathbf{H}) = \mathbf{H}\cdot(\nabla\times\mathbf{E}) - \mathbf{E}\cdot(\nabla\times\mathbf{H})$ gives the divergence, $\mathbf{E}\cdot\partial\mathbf{D}/\partial t = \partial_t(\tfrac12\epsilon E^2)$ the time derivative ([[3-maxwell-and-waves/20-poynting-theorem-and-monochromatic-waves|Lecture 20]]). It is the [[concepts/continuity-equation]] plus an exchange term: field energy can change form, charge cannot.

- **$\partial w/\partial t$**: stored [[concepts/electrostatic-energy]] $\tfrac12\epsilon E^2$ plus [[concepts/magnetic-energy]] $\tfrac12\mu H^2$.
- **$\nabla\cdot\mathbf{S}$**: outflow; $\mathbf{S}$ ([[concepts/poynting-vector]]) is power per unit area along the flow.
- **$\mathbf{J}\cdot\mathbf{E}$**: power to charges ($\rho\mathbf{E}\cdot\mathbf{u}$; the magnetic force does no work). Ohmic: **Joule heating** $\sigma E^2 = J^2/\sigma\ge0$, point form of $I^2R$. Where $\mathbf{J}\cdot\mathbf{E}<0$, a non-electromagnetic agent (battery, antenna generator) drives current against $\mathbf{E}$, injecting $-\mathbf{J}\cdot\mathbf{E}$.

Across a sheet, $\hat n\cdot(\mathbf{S}_1 - \mathbf{S}_2) = -\mathbf{J}_s\cdot\mathbf{E}$, $\hat n$ from 2 into 1 (thin pillbox, [[concepts/boundary-conditions]]). Periodic steady state: $\langle\partial w/\partial t\rangle = 0$, so $\nabla\cdot\langle\mathbf{S}\rangle = -\langle\mathbf{J}\cdot\mathbf{E}\rangle$; average power out = injected − dissipated.

**Examples.**
- *Resistive wire:* $\mathbf{S}$ radially inward, $\lvert\mathbf{S}\rvert = (I/\sigma\pi a^2)(I/2\pi a)$; over $2\pi a\ell$ exactly $I^2R$, none through the ends. 2 m nichrome, radius 0.25 mm, 3 A: 101 W through 32 kW/m².
- *Leaky capacitor discharging:* conduction and displacement currents cancel, $\mathbf{H} = 0$, $\mathbf{S} = 0$; $\partial w/\partial t = -\sigma E^2$, heat on the spot.
- *DC coax:* $\mathbf{S} = \hat z\,VI/(2\pi\rho^2\ln(b/a))$ in the dielectric integrates to $VI$; power flows between the conductors.
- *Sheet* $\hat x\,2\cos\omega t$ A/m, vacuum (notes): $\mathbf{J}_s\cdot\mathbf{E} = -2\eta_0\cos^2\omega t$, each face carries $\eta_0\cos^2\omega t$; on average $\eta_0\approx377$ W/m² in, $\eta_0/2\approx188$ W/m² out per side.
- *Isotropic antenna (idealized):* equal average power through every sphere, $\langle S\rangle\propto1/r^2$; far out $E_0 = \sqrt{2\eta_0\langle S\rangle}$, $E\propto1/r$. 50 kW at 10 km: $E_0 = 0.173$ V/m.
- Sheet $-\hat z\,3u(t)\cos\omega t$ A/m, $\epsilon_r = 2.25$: injects $180\pi\approx565$ W/m², $90\pi\approx283$ W/m² each way; after 3 µs, 1.70 mJ/m² stored between the wavefronts.

> [!trap]
> - Outward flux plus $\int\mathbf{J}\cdot\mathbf{E}\,dV$ = rate of *decrease* of $W$.
> - Exams call even negative $\mathbf{J}\cdot\mathbf{E}$ (a source, e.g. $\langle\mathbf{J}_s\cdot\mathbf{E}\rangle$) Joule heating.
> - $\mathbf{J}_s\cdot\mathbf{E}$ is in W/m², not W/m³.
> - Only $\oint\mathbf{S}\cdot d\mathbf{A}$ is fixed: a static $\mathbf{E}\times\mathbf{H}\neq0$ can circulate, carrying nothing (a charge by a magnet).
> - Hysteresis: $\mathbf{H}\cdot\partial\mathbf{B}/\partial t$ is not a stored-energy rate; part is lost each cycle.

**Where it appears.** Lecture 20; [[3-maxwell-and-waves/19-dalembert-solutions-and-radiation-from-current-sheets|Lecture 19]] ($\mathbf{E}$ opposing $\mathbf{J}_s$); Lectures 22–23 ($\sigma E^2$ drains a wave: power $\propto e^{-2\alpha z}$); Lecture 26 (standing waves: no average power); Unit 4; [[problems/energy-bookkeeping-for-a-radiating-sheet]].

**Practice.** [[practice/topics#poyntings-theorem-energy-flow-and-time-average-power|Poynting's theorem, energy flow and time-average power]] (44 problems) — for example [[practice/20-poynting-theorem-and-power#201-reading-the-energy-ledger|20.1 Reading the energy ledger]] (easy), [[practice/20-poynting-theorem-and-power#206-split-then-add|20.6 Split, then add]] (medium), [[practice/20-poynting-theorem-and-power#209-a-coax-with-a-resistive-core|20.9 A coax with a resistive core]] (hard).

Related: [[concepts/conductors]] · [[concepts/current-sheet-radiation]] · [[concepts/divergence-theorem]] · [[concepts/maxwells-equations]].
