---
title: "Displacement current"
description: "∂D/∂t, Maxwell's addition to Ampère's law: a changing electric flux produces a magnetic field exactly as a conduction current does. Required by charge conservation, it resolves the two-surface paradox of a charging capacitor and makes electromagnetic waves possible."
tags: [concept, waves]
aliases: ["Ampère–Maxwell law", "displacement current density", "Maxwell's correction"]
---

> [!key] Definition
> $$
> \begin{gathered}
> \nabla\times\mathbf{H} = \mathbf{J} + \frac{\partial\mathbf{D}}{\partial t},\\[4pt]
> \oint_C\mathbf{H}\cdot d\mathbf{l} = \int_S\mathbf{J}\cdot d\mathbf{S} + \frac{d}{dt}\int_S\mathbf{D}\cdot d\mathbf{S} = I_c + I_d .
> \end{gathered}
> $$
> $\partial\mathbf{D}/\partial t$ is the displacement current *density* [A/m²]; through a surface, $I_d = d\psi_E/dt$ [A] is the rate of change of electric flux. In matter $\partial\mathbf{D}/\partial t = \epsilon_0\partial\mathbf{E}/\partial t + \partial\mathbf{P}/\partial t$: the polarization current of bound charges ([[1-electrostatics/11-lorentz-drude-models-for-conductivity-and-susceptibility|Lecture 11]]) plus a vacuum term with no charges behind it.

**Physics.** Why it must be there: the divergence of a curl is zero, so $\nabla\times\mathbf{H} = \mathbf{J}$ alone implies $\nabla\cdot\mathbf{J} = 0$, which contradicts the [[concepts/continuity-equation]] wherever charge is piling up. With the extra term, $\nabla\cdot(\nabla\times\mathbf{H}) = \nabla\cdot\mathbf{J} + \partial_t\nabla\cdot\mathbf{D} = \nabla\cdot\mathbf{J}+\partial_t\rho = 0$ is the continuity equation itself (assuming Gauss's law holds for time-varying fields, as it does). What it does: changing $\mathbf{E}$ now makes $\mathbf{H}$, as changing $\mathbf{B}$ makes $\mathbf{E}$, and the two curl equations feed each other — the wave equation, with speed $1/\sqrt{\mu\epsilon}$ ($= c$ in vacuum), confirmed by Hertz around 1888. It is the only term that survives on the right of the curl-curl step in [[3-maxwell-and-waves/18-the-wave-equation-and-plane-tem-waves|Lecture 18]]: without $\partial\mathbf{D}/\partial t$ that step gives $\nabla^2\mathbf{E} = 0$, Laplace's equation, and no waves at all ([[concepts/wave-equation]]). It also repairs Ampère's law's surface-independence: with only $\int\mathbf{J}\cdot d\mathbf{S}$ on the right, two surfaces spanning the same loop disagree whenever one is pierced by a wire and the other passes through a gap where charge accumulates; the displacement flux through the second surface makes up the difference.

**Examples.** Charging capacitor: a surface through the wire gives $I$; one through the gap gives $d\psi_E/dt = dQ/dt = I$. Draining point charge: a dome pierced by the wire gives $I + \tfrac{d}{dt}(Q/2) = I/2$; a bowl below, not pierced, links the flux $-Q/2$ (oriented by the loop) and gives $0 + \tfrac{d}{dt}(-Q/2) = I/2$ as well — and Biot–Savart for a semi-infinite wire confirms $I/2$ ([[3-maxwell-and-waves/16-charge-conservation-displacement-current-and-maxwells-equations|Lecture 16]]; worked with numbers in [[problems/mmf-around-a-draining-charge]]). $\mathbf{E} = E_0te^{-t^2}\hat z$ through $0.1$ m²: $I_d = \epsilon_0AE_0(1-2t^2)e^{-t^2}$ A. In a lossy capacitor the two currents flow side by side: $I = GV + C\,dV/dt$ is conduction plus displacement.

> [!trap]
> - It is not a flow of charge in vacuum; nothing moves. It is a source term for $\mathbf{H}$ that behaves like a current.
> - $\partial/\partial t$, partial; the total $d/dt$ is allowed only in front of the flux integral over a fixed surface.
> - The ratio $|\partial_t\mathbf{D}|/|\sigma\mathbf{E}| = \omega\epsilon/\sigma$ decides whether a medium acts as a dielectric or a conductor at a given frequency — the same $\sigma/\epsilon$ as the relaxation rate (Lectures 8, 10, 23).
> - At a boundary the displacement-current flux through a shrinking loop vanishes, which is why $\hat n\times(\mathbf{H}_1-\mathbf{H}_2) = \mathbf{J}_s$ contains no $\partial\mathbf{D}/\partial t$.

**Where it appears.** Lecture 16 (statement, verification, examples, the completed Maxwell equations); the Lecture 13 slides (capacitor paradox and the flux-area example); Lecture 18 (the wave equation); Units 3–4 (every wave).

**Practice.** [[practice/topics#continuity-relaxation-and-displacement-current|Continuity, relaxation and displacement current]] (19 problems) — for example [[practice/16-charge-conservation-and-displacement-current#161-charge-piling-up-in-a-cylinder|16.1 Charge piling up in a cylinder]] (easy), [[practice/16-charge-conservation-and-displacement-current#166-conduction-versus-displacement-in-soil|16.6 Conduction versus displacement in soil]] (medium), [[practice/16-charge-conservation-and-displacement-current#169-a-leaky-capacitor-and-its-leads|16.9 A leaky capacitor and its leads]] (hard).

Related: [[concepts/amperes-law]] · [[concepts/continuity-equation]] · [[concepts/maxwells-equations]] · [[concepts/electric-flux-density]] · [[concepts/polarization]].
