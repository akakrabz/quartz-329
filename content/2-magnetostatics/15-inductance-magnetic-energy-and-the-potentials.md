---
title: "Lecture 15 — Inductance, magnetic energy, and the potentials"
description: "Map of Lecture 15 — self-inductance and the inductor's sign convention, the RL decay, the Ampère chain for L, magnetic energy, the line parameters 𝓛, 𝓒, 𝓖 with 𝓛𝓒 = με, and the potentials with gauge freedom; the full treatment is on the linked topic pages."
tags: [lecture, magnetostatics]
lecture: 15
---

*Lecture 15 · course notes §15 · slides "Potentials" and "Inductance" · prev: [[2-magnetostatics/14-faradays-law-and-induced-emf|Lecture 14]] · next: [[3-maxwell-and-waves/16-charge-conservation-displacement-current-and-maxwells-equations|Lecture 16]] · practice: [[practice/15-inductance-and-magnetic-energy|12 problems]]*

> [!abstract] In one breath
> [[1-electrostatics/10-capacitance-and-conductance|Lecture 10]] made electrostatics a circuit element, $Q = CV$; here magnetostatics plus Faraday does the same: a loop links its *own* flux, $\Psi = LI$. Changing $I$ produces a self-emf $-L\,dI/dt$ — a rise in the direction of $I$, written in circuits as the drop $V = L\,dI/dt$. Shorted through a resistor the current decays with $\tau = L/R$, twin of $RC$. $L$ comes from the capacitance chain with letters changed: Ampère gives $\mathbf{H}$, $\mu$ gives $\mathbf{B}$, a surface integral gives $\Psi$. The energy $\tfrac12LI^2$ lives in the field at $\tfrac12\mu H^2$ per cubic metre, and for a coax or plates the per-metre inductance and capacitance multiply to $\mu\epsilon$ — the seed of Unit 4. With time variation $\mathbf{E}$ needs the pair $(\Phi,\mathbf{A})$, defined up to a gauge transformation.

## 1. Self-inductance

$\Psi = LI$, $L = N\Psi/I$ [H], geometry and $\mu$ only; mutual inductance $M$ named. Faraday on the coil's own loop: self-emf $-L\,dI/dt$, a *rise* along $I$; circuits write the *drop* $V = L\,dI/dt$ (a typed slide has the sign wrong — errata).

→ Full treatment: [[concepts/inductance|Inductance]]
## 2. The RL decay, and when I = ℰ/R was allowed

$RI = -L\,dI/dt\Rightarrow I = I(0)e^{-t/\tau}$, $\tau = L/R$. Notes Example 1: 1 Ω, 1 μH, 3 A → $3e^{-10^6t}$ A. A large $L$ is a current source as a large $C$ is a voltage source. Lecture 14's $I = \mathcal{E}/R$ holds when $L\,dI/dt\ll\mathcal{E}$.

→ Full treatment: [[concepts/inductance|Inductance]]
## 3. Computing L: the Ampère chain

$I\to\mathbf{H}\to\mathbf{B} = \mu\mathbf{H}\to\Psi\to L = N\Psi/I$; $I$ cancels. Long solenoid: $L = n^2\mu_0A\ell = N^2\mu_0A/\ell$ — $N$ enters twice.

→ Full treatment: [[concepts/inductance|Inductance]] (recipe, solenoid, table of results)
## 4. Energy: ½LI², and ½μH² per cubic metre

$P = VI = d(\tfrac12LI^2)/dt$; for the solenoid $\tfrac12LI^2 = \tfrac12\mu_0H_z^2\cdot A\ell$, so $w = \tfrac12\mu\mathbf{H}\cdot\mathbf{H}$ [J/m³] in general; $W\ge0$ gives $L\ge0$.

→ Full treatment: [[concepts/magnetic-energy|Magnetic energy]]
## 5. Transmission-line geometries: 𝓛, 𝓒, and their product

Shorted coax: $\Psi = (\mu\ell I/2\pi)\ln(b/a)$ through the $r$–$z$ rectangle, $\mathcal{L} = (\mu/2\pi)\ln(b/a)$; shorted plates $\mathcal{L} = \mu d/W$. Beside $\mathcal{C}$ and $\mathcal{G}$ the geometric factors invert: $\mathcal{LC} = \mu\epsilon$, $\mathcal{G}/\mathcal{C} = \sigma/\epsilon$, $1/\sqrt{\mathcal{LC}} = 1/\sqrt{\mu\epsilon}$. Slide challenge: widening the plates' gap raises $\mathcal{L}$, lowers $\mathcal{C}$ and $\mathcal{G}$ (c).

→ Full treatment: [[concepts/transmission-line-parameters|Transmission-line parameters 𝓛, 𝓒, 𝓖]]
## 6. The potentials when fields vary in time

$\mathbf{B} = \nabla\times\mathbf{A}$ survives; Faraday makes $\mathbf{E}+\partial\mathbf{A}/\partial t$ curl-free, so $\mathbf{E} = -\nabla\Phi - \partial\mathbf{A}/\partial t$. Gauge transformation $\mathbf{A}+\nabla\lambda$, $\Phi-\partial_t\lambda$ leaves both fields unchanged (slide challenge, answer (b)).

→ Full treatment: [[concepts/vector-potential|Vector potential]]
## 7. Summary

- $\Psi = LI$, $L = N\Psi/I$ [H]; self-emf $-L\,dI/dt$ (rise), circuit drop $V = L\,dI/dt$; $M$ for two coils.
- Shorted coil: $RI = -L\,dI/dt$, $I = I(0)e^{-t/\tau}$, $\tau = L/R$; large $L$ ≈ current source; $I = \mathcal{E}/R$ needs $L\,dI/dt\ll\mathcal{E}$.
- Chain: $I\to\mathbf{H}\to\mathbf{B}\to\Psi\to L$. Solenoid $L = n^2\mu_0A\ell = N^2\mu_0A/\ell$.
- $W = \tfrac12LI^2$; $w = \tfrac12\mu\mathbf{H}\cdot\mathbf{H}$ [J/m³]; $\mu = (1+\chi_m)\mu_0$.
- Coax $\mathcal{L} = (\mu/2\pi)\ln(b/a)$, plates $\mathcal{L} = \mu d/W$; $\mathcal{LC} = \mu\epsilon$, $\mathcal{G}/\mathcal{C} = \sigma/\epsilon$, $1/\sqrt{\mathcal{LC}} = 1/\sqrt{\mu\epsilon}$.
- $\mathbf{B} = \nabla\times\mathbf{A}$, $\mathbf{E} = -\nabla\Phi - \partial\mathbf{A}/\partial t$; gauge: $\mathbf{A}+\nabla\lambda$, $\Phi - \partial_t\lambda$.

Topic pages: [[concepts/inductance]] · [[concepts/magnetic-energy]] · [[concepts/transmission-line-parameters]] · [[concepts/vector-potential]] · [[concepts/capacitance]].

> [!exam] On exams
> "Find the inductance (per unit length) of …" is the magnetic twin of Exam 1 problem 4, graded on the Ampère chain ([[concepts/inductance]]). Energy: $\tfrac12LI^2$ and $\int\tfrac12\mu H^2dV$ shown to agree ([[concepts/magnetic-energy]]). Signs: $V = L\,dI/dt$ as a drop along $I$. Check $\mathcal{LC} = \mu\epsilon$ ([[concepts/transmission-line-parameters]]).

> [!tip] Practice this lecture
> [[practice/15-inductance-and-magnetic-energy|12 practice problems]] — 5 easy, 3 medium, 4 hard — each with a folded hint and a worked solution. Start with [[practice/15-inductance-and-magnetic-energy#151-a-long-solenoid-by-the-numbers|15.1 A long solenoid by the numbers]]; the [[practice/index|practice hub]] has the whole bank by difficulty and by topic.

### Sources for this page
Kudeki notes, Lecture 15 (self-inductance, self-emf as a rise; back-emf; $RL$ decay, current-source remark; $N$ turns; Example 1; solenoid; $w = \tfrac12\mu_0\mathbf{H}\cdot\mathbf{H}$, $\mu = (1+\chi_m)\mu_0$; shorted coax and plates; inverse geometric factors). Shao, Lecture 15 slides (potentials and the gauge challenge; $L = \Psi/I$ beside $C = Q/V$; circuit symbol; mutual inductance; five-step recipe; $\mathcal{C}$, $\mathcal{G}$, $\mathcal{L}$ table with $\mathcal{LC} = \mu\epsilon$ — only implied in the notes; $v_p = 1/\sqrt{\mathcal{LC}}$; plate-separation challenge). Slips in the course material: see [[0-toolkit/04-errata-in-the-course-materials|errata]].
