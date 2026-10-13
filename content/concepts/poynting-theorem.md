---
title: "Poynting's theorem"
description: "∂w/∂t + ∇·S + J·E = 0: Maxwell's equations written as an energy ledger. The stored energy density w = ½εE² + ½μH² changes only by flowing away as S = E × H or by being handed to charges at the rate J·E, which is Joule heating when positive and a source when negative. In integral form −dW/dt = ∮S·dA + ∫J·E dV; averaged over a period in a steady state, ∮⟨S⟩·dA = −∫⟨J·E⟩dV."
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
> and, over a volume $V$ with outward area element $d\mathbf{A}$ on its closed surface $A$,
> $$
> \begin{gathered}
> -\frac{dW}{dt} = \oint_A\mathbf{S}\cdot d\mathbf{A} + \int_V\mathbf{J}\cdot\mathbf{E}\,dV,\\[4pt]
> W = \int_Vw\,dV .
> \end{gathered}
> $$
> Valid for fields that obey Maxwell's equations in a linear, isotropic medium whose $\epsilon$ and $\mu$ do not change in time. $\mathbf{J}$ is the free current. Every term is a power per unit volume (or, in the integral form, a power).

**Physics.** Dot Faraday's law with $\mathbf{H}$, dot the Ampère–Maxwell law with $\mathbf{E}$, and subtract. The identity $\nabla\cdot(\mathbf{E}\times\mathbf{H}) = \mathbf{H}\cdot(\nabla\times\mathbf{E}) - \mathbf{E}\cdot(\nabla\times\mathbf{H})$ turns the left side into a divergence, and $\mathbf{E}\cdot\partial\mathbf{D}/\partial t = \partial_t(\tfrac12\epsilon E^2)$ turns the right side into a time derivative ([[3-maxwell-and-waves/20-poynting-theorem-and-monochromatic-waves|Lecture 20]]). The result is the conservation law for electromagnetic energy, built like the [[concepts/continuity-equation]] for charge: $w$ is the density, $\mathbf{S}$ the flux density, and $\mathbf{J}\cdot\mathbf{E}$ is an extra exchange term, because field energy can turn into other forms and charge cannot.

- **$\partial w/\partial t$** is the stored energy changing: the [[concepts/electrostatic-energy]] density $\tfrac12\epsilon E^2$ plus the [[concepts/magnetic-energy]] density $\tfrac12\mu H^2$.
- **$\nabla\cdot\mathbf{S}$** is energy flowing away. $\mathbf{S}$ ([[concepts/poynting-vector]]) points the way energy flows, and its size is the power per unit area across a surface perpendicular to it.
- **$\mathbf{J}\cdot\mathbf{E}$** is the power per unit volume the field gives to charges ($\rho\mathbf{E}\cdot\mathbf{u}$; the magnetic force does no work). In an ohmic conductor it is **Joule heating**, $\sigma E^2 = J^2/\sigma\ge0$, the point form of $I^2R$. Where $\mathbf{J}\cdot\mathbf{E}<0$, something non-electromagnetic (a battery's chemistry, the generator behind an antenna current) drives the current against $\mathbf{E}$, and $-\mathbf{J}\cdot\mathbf{E}$ is the power injected into the field.

Across a current sheet the theorem becomes $\hat n\cdot(\mathbf{S}_1 - \mathbf{S}_2) = -\mathbf{J}_s\cdot\mathbf{E}$, with $\hat n$ from side 2 into side 1 (the [[concepts/boundary-conditions]] pattern: a thin pillbox stores nothing). In a periodic steady state $\langle\partial w/\partial t\rangle = 0$, so $\nabla\cdot\langle\mathbf{S}\rangle = -\langle\mathbf{J}\cdot\mathbf{E}\rangle$: on average, the power out of a closed surface is the power injected inside minus the power dissipated inside.

**Examples.**
- *Resistive wire:* $\mathbf{S}$ at the surface points radially inward, $\lvert\mathbf{S}\rvert = (I/\sigma\pi a^2)(I/2\pi a)$, and over the side area $2\pi a\ell$ it delivers exactly $I^2R$. Nothing enters through the ends. A 2 m nichrome wire of radius 0.25 mm at 3 A takes 101 W in through a surface flux of 32 kW/m².
- *Leaky capacitor discharging:* conduction and displacement currents cancel, so $\mathbf{H} = 0$ and $\mathbf{S} = 0$; the theorem reads $\partial w/\partial t = -\sigma E^2$, and each cubic metre turns its stored energy into heat on the spot.
- *Coax carrying DC:* $\mathbf{S} = \hat z\,VI/(2\pi\rho^2\ln(b/a))$ in the dielectric integrates to $VI$. The power travels between the conductors, not in them.
- *Radiating sheet* $\hat x\,2\cos\omega t$ A/m in vacuum (the notes' example): $\mathbf{J}_s\cdot\mathbf{E} = -2\eta_0\cos^2\omega t$, and each face carries $\eta_0\cos^2\omega t$ away. On average, $\eta_0\approx377$ W/m² goes in and $\eta_0/2\approx188$ W/m² leaves on each side.
- *Isotropic antenna (an idealization):* in a steady state, the average power through every sphere around it is the same, so $\langle S\rangle\propto1/r^2$. Far from the antenna, where the wave is locally plane, $E_0 = \sqrt{2\eta_0\langle S\rangle}$ and $E\propto1/r$. For 50 kW at 10 km, $E_0 = 0.173$ V/m.
- Worked problem: a sheet $-\hat z\,3u(t)\cos\omega t$ A/m in a dielectric with $\epsilon_r = 2.25$ injects $180\pi\approx565$ W/m², sends $90\pi\approx283$ W/m² each way, and after 3 µs has stored 1.70 mJ/m² between its two wavefronts.

> [!trap]
> - The sign convention: the outward flux $\oint\mathbf{S}\cdot d\mathbf{A}$ and $\int\mathbf{J}\cdot\mathbf{E}\,dV$ add up to the rate of *decrease* of $W$.
> - $\mathbf{J}\cdot\mathbf{E}$ is called Joule heating even where it is negative (a source). Exam papers do the same with $\langle\mathbf{J}_s\cdot\mathbf{E}\rangle$ at a radiating sheet.
> - $\mathbf{J}_s\cdot\mathbf{E}$ on a sheet is in W/m², not W/m³.
> - Only the flux of $\mathbf{S}$ through a closed surface is fixed by the theorem. Static fields can have $\mathbf{E}\times\mathbf{H}\neq0$ that circulates and carries nothing (a charge next to a magnet).
> - With hysteresis (a ferromagnet) $\mathbf{H}\cdot\partial\mathbf{B}/\partial t$ is not the rate of change of a stored energy; part of it is lost as heat in every cycle.

**Where it appears.** [[3-maxwell-and-waves/20-poynting-theorem-and-monochromatic-waves|Lecture 20]] (derived; the wire, the coax, the cosine sheet, time averages); [[3-maxwell-and-waves/19-dalembert-solutions-and-radiation-from-current-sheets|Lecture 19]] ($\mathbf{E}$ opposing $\mathbf{J}_s$ at a radiating sheet); Lectures 22–23 ($\sigma E^2$ drains a wave in a conductor, so power falls as $e^{-2\alpha z}$); Lecture 26 (standing waves carry no average power); Unit 4 (power flow on transmission lines); [[problems/energy-bookkeeping-for-a-radiating-sheet]].

**Practice.** [[practice/topics#poyntings-theorem-energy-flow-and-time-average-power|Poynting's theorem, energy flow and time-average power]] (23 problems) — for example [[practice/20-poynting-theorem-and-power#201-reading-the-energy-ledger|20.1 Reading the energy ledger]] (easy), [[practice/20-poynting-theorem-and-power#206-split-then-add|20.6 Split, then add]] (medium), [[practice/20-poynting-theorem-and-power#209-a-coax-with-a-resistive-core|20.9 A coax with a resistive core]] (hard).

Related: [[concepts/poynting-vector]] · [[concepts/continuity-equation]] · [[concepts/electrostatic-energy]] · [[concepts/magnetic-energy]] · [[concepts/conductors]] · [[concepts/current-sheet-radiation]] · [[concepts/divergence-theorem]] · [[concepts/maxwells-equations]].
