---
title: "Lecture 16 — Charge conservation, displacement current, and Maxwell's equations"
description: "Charge conservation forces Maxwell's displacement current, which completes the four equations and carries the boundary conditions over to time-varying fields; the full treatment is on the topic pages linked from each section."
tags: [lecture, waves]
lecture: 16
---

*Lecture 16 · course notes §16 · slides "Conservation of Charge / Boundary Conditions" (the displacement current itself is on the Lecture 13 deck) · prev: [[2-magnetostatics/15-inductance-magnetic-energy-and-the-potentials|Lecture 15]] · next: [[3-maxwell-and-waves/17-magnetization-and-maxwells-equations-in-matter|Lecture 17]] · practice: [[practice/16-charge-conservation-and-displacement-current|12 problems]]*

> [!abstract] In one breath
> Charge inside any volume changes only by current crossing its boundary: $\oint\mathbf{J}\cdot d\mathbf{S} = -dQ/dt$, or $\nabla\cdot\mathbf{J} = -\partial\rho/\partial t$ — the **continuity equation**. The divergence of static Ampère, $\nabla\times\mathbf{H} = \mathbf{J}$, is identically zero on the left, so it insists $\nabla\cdot\mathbf{J} = 0$ — false wherever charge accumulates (a charging capacitor, a draining sphere, any antenna). Maxwell's 1861 repair adds the **displacement current** $\partial\mathbf{D}/\partial t$, whose divergence is $\partial\rho/\partial t$ by Gauss's law, turning the contradiction into the continuity equation. That term closes the system and predicts electromagnetic waves (Hertz, 1888). The four boundary conditions carry over unchanged.

## 1. Charge conservation and the continuity equation

The notes derive $\oint_S\mathbf{J}\cdot d\mathbf{S} = -dQ_V/dt$ from two open surfaces on one rim (the bucket), then $\nabla\cdot\mathbf{J} = -\partial\rho/\partial t$ by the divergence theorem. Slide example: $\mathbf{J} = (x,y,z)$ A/m² in the unit cube — charge *decreases* at 3 A, 1 A out through each pair of faces. Already met as the relaxation time $\epsilon/\sigma$ (Lecture 8), the Coulomb-gauge condition (Lecture 13) and the lossy capacitor's $I = C\,dV/dt + GV$ (Lecture 10).

→ Full treatment: [[concepts/continuity-equation|Continuity equation]]

## 2. The asymmetry, and Maxwell's displacement current

Faraday has no converse in static Ampère, and $\nabla\cdot(\nabla\times\mathbf{H}) = 0$ contradicts continuity; the repair $\nabla\times\mathbf{H} = \mathbf{J}+\partial\mathbf{D}/\partial t$ has divergence equal to the continuity equation. Slide examples: the MMF around a draining point charge is $I/2$ through a dome *and* through a bowl (static Ampère gave $I$ and $0$); $\mathbf{E} = E_0te^{-t^2}\hat z$ through 0.1 m² gives $I_d = \epsilon_0AE_0(1-2t^2)e^{-t^2}$ A. In matter the term is $\epsilon_0\partial_t\mathbf{E}$ plus the polarization current.

→ Full treatment: [[concepts/displacement-current|Displacement current]]

## 3. Maxwell's equations, complete

The four equations written together for the first time, microscopic (all charges, $\epsilon_0$, $\mu_0$) and macroscopic (free charges, $\epsilon$, $\mu$) forms, integral forms, Lorentz force. $\nabla\cdot\mathbf{B} = 0$ follows from Faraday's law plus the absence of monopoles. The slide's review table of canonical static fields (point, line, sheet charge; line, sheet current; solenoid).

→ Full treatment: [[concepts/maxwells-equations|Maxwell's equations]]

## 4. Boundary conditions — "same for dynamics"

The four conditions, $\hat n$ from medium 2 into medium 1, hold for time-varying fields: the $\partial_t\mathbf{D}$ and $\partial_t\mathbf{B}$ fluxes vanish with the loop's width. Two cases carry the course: perfect dielectrics (everything continuous, refraction with $\epsilon$ or $\mu$) and the perfect conductor ($\mathbf{H} = 0$ inside by Faraday; $\mathbf{E}$ normal, ending on $\rho_s = \hat n\cdot\mathbf{D}_1$; $\mathbf{H}$ tangential, $\mathbf{J}_s = \hat n\times\mathbf{H}_1$). Slide exercises: $\rho_s = 3D_0$ and $-2D_0$ from a given $\mathbf{D}$; which field pictures are possible outside a conductor (answer (e)). Rule: integral forms at a boundary, never the differential equations.

→ Full treatment: [[concepts/boundary-conditions|Boundary conditions]] · [[concepts/conductors|Conductors]] (perfect conductors)

## 5. Summary

- Charge conservation: $\oint\mathbf{J}\cdot d\mathbf{S} = -dQ/dt$, $\nabla\cdot\mathbf{J} = -\partial\rho/\partial t$. Out = decrease.
- $\nabla\cdot(\nabla\times\mathbf{H}) = 0$ forces $\nabla\times\mathbf{H} = \mathbf{J}+\partial\mathbf{D}/\partial t$; its divergence *is* continuity (with Gauss). $I_d = d\psi_E/dt$ [A]; in matter $\partial\mathbf{D}/\partial t = \epsilon_0\partial_t\mathbf{E} + \partial_t\mathbf{P}$.
- Two surfaces on one loop agree: draining charge $I/2$ both ways; capacitor $I$ both ways.
- Maxwell's equations complete; Hertz 1888; $\nabla\cdot\mathbf{B} = 0$ from Faraday + no monopoles.
- Boundary conditions unchanged by time variation: $D_n$ jumps by $\rho_s$, $E_t$ continuous, $B_n$ continuous, $H_t$ jumps by $J_s$. PEC: $\mathbf{E}$ normal (ends on $\rho_s$), $\mathbf{H}$ tangential (carried by $\mathbf{J}_s$). Integral forms at boundaries.

Concept pages: [[concepts/continuity-equation]] · [[concepts/displacement-current]] · [[concepts/maxwells-equations]] · [[concepts/boundary-conditions]] · [[concepts/conductors]].

> [!exam] On exams
> Four things get asked: (1) rate of change of charge from $\mathbf{J}$ — [[concepts/continuity-equation]]; (2) $I_d$ from $\mathbf{E}(t)$ and an area, and why the term is needed — [[concepts/displacement-current]]; (3) the two-surface paradox; (4) boundary conditions with surface current and the perfect-conductor cases, $\hat n$ drawn first — [[concepts/boundary-conditions]], [[concepts/conductors]]. Every later reflection problem is condition-matching.

> [!tip] Practice this lecture
> [[practice/16-charge-conservation-and-displacement-current|12 practice problems]] — 5 easy, 3 medium, 4 hard — each with a folded hint and a worked solution. Start with [[practice/16-charge-conservation-and-displacement-current#161-charge-piling-up-in-a-cylinder|16.1 Charge piling up in a cylinder]]; the [[practice/index|practice hub]] has the whole bank by difficulty and by topic.

### Sources for this page
Kudeki notes, Lecture 16 (charge conservation, two-surface derivation, continuity; asymmetry and inconsistency; Ampère–Maxwell 1861, Hertz 1888; microscopic and macroscopic forms; $\nabla\cdot\mathbf{B} = 0$ and monopoles; boundary conditions with margin derivations). Shao, Lecture 16 slides (bucket; draining-charge MMF; unit cube; canonical fields; dynamic boundary conditions with the 2 October ink — $\hat n$ "from 2 to 1", $\mu_1H_{1n} = \mu_2H_{2n}$, $\mathbf{H} = 0$ in a PEC; the two exercises; integral forms at boundaries); Lecture 13 slides (capacitor paradox, $\psi_E$, the 0.1 m² example). The site's own: relaxation-time and lossy-capacitor links. Slips in the course material: see [[0-toolkit/04-errata-in-the-course-materials|errata]].
