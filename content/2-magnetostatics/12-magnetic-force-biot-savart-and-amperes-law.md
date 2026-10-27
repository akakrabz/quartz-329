---
title: "Lecture 12 — Magnetic force, Biot–Savart, and Ampère's law"
description: "Map of Lecture 12 — the magnetic force and its relativistic origin, the field of a straight wire, Biot–Savart, Ampère's law and the laws of magnetostatics, current densities, the coax; the full treatment is on the linked topic pages."
tags: [lecture, magnetostatics]
lecture: 12
---

*Lecture 12 · course notes §12 · slides "Magnetic Flux and Magnetic Fields / Biot–Savart Law / Ampère's Law" · prev: [[1-electrostatics/11-lorentz-drude-models-for-conductivity-and-susceptibility|Lecture 11]] · next: [[2-magnetostatics/13-current-sheets-solenoids-and-the-vector-potential|Lecture 13]] · practice: [[practice/12-magnetic-force-biot-savart-and-ampere|12 problems]]*

> [!abstract] In one breath
> Parallel wires with currents in the same direction attract, though neither carries net charge. In the frame of one wire's drifting electrons, the other wire's ion and electron spacings are Lorentz-contracted by different amounts, so that wire *is* charged there and its Coulomb field pushes on the electrons. The lab packages the same force as $\mathbf{F} = q\mathbf{v}\times\mathbf{B}$ with $\mathbf{B} = \dfrac{\mu_0I}{2\pi r}\hat\phi$ circling the wire. **Biot–Savart** (Coulomb's law with a cross product) and **Ampère** (circulation of $\mathbf{H} = \mathbf{B}/\mu_0$ around a loop equals the current through it — Gauss's law with a loop) give $\mathbf{B}$ for any steady current. Differentially, $\nabla\times\mathbf{H} = \mathbf{J}$ and $\nabla\cdot\mathbf{B} = 0$: electrostatics mirrored.

## 1. The observation, and the definition of B

Ampère's 1820 experiment — like currents attract, force per length $\propto1/r$ — fixes the force law $d\mathbf{F} = I\,d\mathbf{l}\times\mathbf{B}$, i.e. $\mathbf{F} = q\mathbf{v}\times\mathbf{B}$, and defines $\mathbf{B}$ in tesla. Magnetic forces do no work; a stationary charge beside a neutral wire feels nothing.

→ Full treatment: [[concepts/magnetic-field|Magnetic field: B and H]]
## 2. Where the force comes from: a charged wire, in the right frame

In the drifting electrons' frame the ion spacing is contracted and the electron spacing dilated, so the wire carries $\lambda' = \gamma\lambda_+v^2/c^2$; its Coulomb field, transformed back, is the lab force $q\mathbf{v}\times\mathbf{B}$ with $\mathbf{B} = \mu_0I/(2\pi r)\,\hat\phi$ (right-hand rule), $\mu_0\epsilon_0 = 1/c^2$. Copper numbers: $v^2/c^2\sim6\times10^{-26}$ against $\lambda_+\sim10^4$ C/m.

→ Full treatment: [[concepts/magnetic-field|Magnetic field: B and H]] (derivation folded there)
## 3. Biot–Savart: Coulomb's law for current elements

$d\mathbf{B} = \mu_0I\,d\mathbf{l}\times\hat R/(4\pi R^2)$, $\hat R$ from source to field point. The slides run the five-step program on the straight wire: every element along $\hat\phi$, $\int dz/(r^2+z^2)^{3/2} = 2/r^2$, result $\mu_0I/(2\pi r)$ ✓.

→ Full treatment: [[concepts/biot-savart-law|Biot–Savart law]]
## 4. Ampère's law: the circulation of B

$\oint\mathbf{H}\cdot d\mathbf{l} = I_{\text{enc}}$ through any surface on the loop, right-hand rule, $\mathbf{H} = \mathbf{B}/\mu_0$ in A/m (an MMF, twin of the EMF). Stokes gives $\nabla\times\mathbf{H} = \mathbf{J}$, beside $\nabla\cdot\mathbf{B} = 0$: div and curl swapped relative to electrostatics. Valid quasi-statically for $L\ll c/f$ (MQS).

→ Full treatment: [[concepts/amperes-law|Ampère's law]]
## 5. Describing currents: J, Jₛ, I, and δ-functions

$\mathbf{J}$ [A/m²]; a sheet is $\mathbf{J}_s\,\delta(x-x_0)$, a line current $\hat zI\,\delta(x-x_0)\delta(y-y_0)$. Notes Example 1: $\mathbf{J}_s = \hat zy\,\text{rect}(y-\tfrac12)$ A/m carries $\tfrac12$ A — integrate *across* the flow.

→ Full treatment: [[concepts/current-distributions|Current distributions: J, J_s, I]]
## 6. Ampère at work: the coaxial cable

Slide challenge: uniform core of radius $a$, return shell at $b$. $H_\phi = Ir/(2\pi a^2)$, $I/(2\pi r)$, $0$ — constant only for $r>b$ (answer (c)); each region is a Lecture 3 result with $D\to H$. Trap: $I_{\text{enc}}$ is signed and counts only current *through* the surface.

→ Full treatment: [[concepts/amperes-law|Ampère's law]] (coax example and trap)
## 7. Summary

- $\mathbf{F} = q\mathbf{v}\times\mathbf{B}$, $d\mathbf{F} = I\,d\mathbf{l}\times\mathbf{B}$; magnetic forces do no work; parallel currents attract.
- The force is the Coulomb force of a wire charged *in the moving frame*; the lab writes $\mathbf{B} = \mu_0I/(2\pi r)\,\hat\phi$, $\mu_0\epsilon_0 = 1/c^2$.
- Biot–Savart: $d\mathbf{B} = \mu_0I\,d\mathbf{l}\times\hat R/(4\pi R^2)$, $\hat R$ from source to field point; five steps; $\int dz/(r^2+z^2)^{3/2} = 2/r^2$.
- Ampère: $\oint\mathbf{H}\cdot d\mathbf{l} = I_{\text{enc}}$ through any surface on $C$, right-hand rule; $\mathbf{H} = \mathbf{B}/\mu_0$ [A/m].
- $\nabla\times\mathbf{H} = \mathbf{J}$, $\nabla\cdot\mathbf{B} = 0$ — div and curl swapped; quasi-statically valid for $L\ll c/f$.
- $\mathbf{J}_s\,\delta(x-x_0)$, $\hat zI\,\delta(x-x_0)\delta(y-y_0)$; integrate $\mathbf{J}_s$ across the flow for $I$.
- Coax: $H_\phi = Ir/(2\pi a^2)$, $I/(2\pi r)$, $0$.

Topic pages: [[concepts/magnetic-field]] · [[concepts/biot-savart-law]] · [[concepts/amperes-law]] · [[concepts/current-distributions]] · [[concepts/lorentz-force]].

> [!exam] On exams
> The magnetic twin of Exam 1 problem 2: "a symmetric current distribution — find $\mathbf{H}$ everywhere" (method on [[concepts/amperes-law]]). Direction questions are cheap points: right-hand rule and $q\mathbf{v}\times\mathbf{B}$ explicitly ([[concepts/magnetic-field]]). Units: A/m for $\mathbf{H}$, T for $\mathbf{B}$.

> [!tip] Practice this lecture
> [[practice/12-magnetic-force-biot-savart-and-ampere|12 practice problems]] — 5 easy, 3 medium, 4 hard — each with a folded hint and a worked solution. Start with [[practice/12-magnetic-force-biot-savart-and-ampere#121-a-charge-passing-a-wire|12.1 A charge passing a wire]]; the [[practice/index|practice hub]] has the whole bank by difficulty and by topic.

### Sources for this page
Kudeki notes, Lecture 12 (two-wire attraction; relativity footnote, $\lambda' = \gamma\lambda_+v^2/c^2$, $\mathbf{F} = \mathbf{F}'/\gamma$; $\mathbf{B}$ and the right-hand rule; Biot–Savart and its validity; Ampère's law, $\mathbf{H} = \mathbf{B}/\mu_0$, differential laws; δ-function currents, Example 1; MQS note). Shao, "Lectures 11–12" slides (Ampère's experiment; $I\,d\mathbf{l} = q\mathbf{v}$; five-step Biot–Savart; circulation; laws beside electrostatics; current units; coax challenge, signed currents). The site's own: copper numbers. Slips in the course material: see [[0-toolkit/04-errata-in-the-course-materials|errata]].
