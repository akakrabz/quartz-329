---
title: "Lecture 18 — The wave equation and plane TEM waves"
description: "Source-free Maxwell equations give the wave equation; its plane solutions travel undistorted at v = 1/√(με) with H = û × E/η, η = √(μ/ε); the full treatment is on the topic pages linked from each section."
tags: [lecture, waves]
lecture: 18
---

*Lecture 18 · course notes §18 · slides "Uniform Plane Waves in Free Space" · prev: [[3-maxwell-and-waves/17-magnetization-and-maxwells-equations-in-matter|Lecture 17]] · next: [[3-maxwell-and-waves/19-dalembert-solutions-and-radiation-from-current-sheets|Lecture 19]] · worked problem: [[problems/a-pulse-on-the-move|A pulse on the move]] · practice: [[practice/18-wave-equation-and-plane-waves|12 problems]]*

> [!abstract] In one breath
> With no charges or currents, Maxwell's curl equations still feed each other: changing $\mathbf{H}$ curls $\mathbf{E}$ (Faraday), changing $\mathbf{E}$ curls $\mathbf{H}$ (the displacement current of [[3-maxwell-and-waves/16-charge-conservation-displacement-current-and-maxwells-equations|Lecture 16]]). Together: the **wave equation** $\nabla^2\mathbf{E} = \mu\epsilon\,\partial^2\mathbf{E}/\partial t^2$. Its **plane waves** $\mathbf{E} = \hat x\,f(t\mp z/v)$, any waveform $f$, slide along $\pm z$ unchanged at $v = 1/\sqrt{\mu\epsilon}$ ($c\approx3\times10^8$ m/s in vacuum) with $\mathbf{H} = \pm\hat y\,f/\eta$, the **intrinsic impedance** $\eta = \sqrt{\mu/\epsilon}$ being $\approx377\ \Omega$ in vacuum, and $\mathbf{E}\times\mathbf{H}$ along the travel. Light, radio and X-rays are this one solution with different waveforms.

## 1. Fields without sources?

A homogeneous, lossless, source-free region: static fields cannot exist there alone (Helmholtz), time-varying ones can. The slides' chain: a source current makes $\mathbf{H}$, changing $\mathbf{B}$ curls $\mathbf{E}$, changing $\mathbf{D}$ curls $\mathbf{H}$, and steps 2–4 sustain themselves without the source — that recursion is the wave; without the displacement current, induction but no propagation.

→ Full treatment: [[concepts/wave-equation|Wave equation]]

## 2. The wave equation

Curl Faraday's law, use $\nabla\times(\nabla\times\mathbf{E}) = \nabla(\nabla\cdot\mathbf{E}) - \nabla^2\mathbf{E}$ with $\nabla\cdot\mathbf{E} = 0$, substitute Ampère–Maxwell: $\nabla^2\mathbf{E} = \mu\epsilon\,\partial^2\mathbf{E}/\partial t^2$, per Cartesian component, assumptions named at each step ($\mu$, $\epsilon$ constant, $\mathbf{J} = 0$, $\rho = 0$). The displacement current is the only term on the right; the equation is necessary, not sufficient.

→ Full treatment: [[concepts/wave-equation|Wave equation]]

## 3. The planar problem: only $E_x(z,t)$ and $H_y(z,t)$

The notes try $\mathbf{E} = \hat xE_x(z,t)$; the slides derive the same reduction from an infinite current sheet by symmetry. Either way the curl equations collapse to $\partial E_x/\partial z = -\mu\,\partial H_y/\partial t$ and $-\partial H_y/\partial z = \epsilon\,\partial E_x/\partial t$. A $z$-polarized $f(t\mp z/v)$ fails Gauss's law: no field along the travel.

→ Full treatment: [[concepts/plane-waves|Plane waves]] (TEM) · [[concepts/wave-equation|Wave equation]] (the reduction)

## 4. The 1D wave equation and its solutions

Cross-differentiating gives $\partial^2E_x/\partial z^2 = \mu\epsilon\,\partial^2E_x/\partial t^2$, $v = 1/\sqrt{\mu\epsilon}$, $c = 2.998\times10^8$ m/s (30 cm/ns). Cosines by substitution (notes); any waveform by factoring the operator (slides): d'Alembert's $E_x = Af(t - z/v) + Bg(t + z/v)$, minus sign with $+z$ travel. Linearity and one $v$ for every frequency keep a pulse's shape; a feature slides rigidly at $v$.

→ Full treatment: [[concepts/wave-equation|Wave equation]]

## 5. H from E: the intrinsic impedance

Faraday (notes) or Ampère–Maxwell (slides) gives $H_y = (Af - Bg)/\eta$, $\eta = \sqrt{\mu/\epsilon} = \mu v = 1/\epsilon v$, $\eta_0 = 376.7\ \Omega\approx120\pi\ \Omega$; the rule $\mathbf{H} = \hat u\times\mathbf{E}/\eta$ with $\mathbf{E}\times\mathbf{H}$ along the travel, and the four-row sign table. Example: 1 V/m in vacuum goes with 2.65 mA/m and 3.34 nT.

→ Full treatment: [[concepts/intrinsic-impedance|Intrinsic impedance]]

## 6. Reading a wave

Direction and speed from the argument (factor out the coefficient of $t$; compare signs). Slide 24: $(0.05y - t)^2$, $u(t + 0.02x)$, $\cos(2\pi10^8t - 2\pi z)$ travel at $20\hat y$, $-50\hat x$, $10^8\hat z$ m/s — answer (c). Shift identities $E(z,t) = E(0, t\mp z/v) = E(z\mp vt, 0)$, the mirror of a $+z$ snapshot, and slide 26's moving waveform ($-z$ at 100 m/s: 0.9, 0.4, 1.0 at the three probes).

→ Full treatment: [[concepts/plane-waves|Plane waves]]

## 7. In matter, and on a cable

$v = c/\sqrt{\mu_r\epsilon_r}$, $\eta = \eta_0\sqrt{\mu_r/\epsilon_r}$: $\epsilon_r = 4$ gives $c/2$ and 188 Ω; the slide-24 wave at $10^8$ m/s needs $\epsilon_r\approx9$, 126 Ω; polyethylene, $2.00\times10^8$ m/s and 251 Ω. On a line $1/\sqrt{\mathcal{L}\mathcal{C}} = v$ and $\sqrt{\mathcal{L}/\mathcal{C}}$ is $\eta$ times geometry — the polyethylene coax's 50 Ω.

→ Full treatment: [[concepts/intrinsic-impedance|Intrinsic impedance]]

## 8. Summary

- $\nabla^2\mathbf{E} = \mu\epsilon\,\partial_t^2\mathbf{E}$ needs the displacement current, constant $\mu,\epsilon$, $\rho = \mathbf{J} = 0$.
- $E_x = Af(t - z/v) + Bg(t + z/v)$, $H_y = (Af - Bg)/\eta$, $\mathbf{H} = \hat u\times\mathbf{E}/\eta$; $\eta_0\approx377\ \Omega$.
- $E(z,t) = E(0, t\mp z/v)$; matter: $v = c/\sqrt{\mu_r\epsilon_r}$, $\eta = \eta_0\sqrt{\mu_r/\epsilon_r}$.

Concept pages: [[concepts/wave-equation]] · [[concepts/plane-waves]] · [[concepts/intrinsic-impedance]] · [[concepts/displacement-current]] · [[concepts/faradays-law]] · [[concepts/maxwells-equations]].

> [!exam] On exams
> Direction and speed from an argument, moving pulses (SP18 Exam 2 #4, [[problems/a-pulse-on-the-move]]), no $z$-polarized wave along $z$ — [[concepts/plane-waves]]. $\mathbf{H}$ from $\mathbf{E}$ or back with the cross product written out; $v$, $\eta$ in a dielectric; the constants — [[concepts/intrinsic-impedance]]. The derivation with assumptions named — [[concepts/wave-equation]]. Current-sheet amplitudes: Lecture 19.

> [!tip] Practice this lecture
> [[practice/18-wave-equation-and-plane-waves|12 practice problems]] — 5 easy, 3 medium, 4 hard — each with a folded hint and a worked solution. Start with [[practice/18-wave-equation-and-plane-waves#181-which-way-and-how-fast|18.1 Which way and how fast]]; the [[practice/index|practice hub]] has the whole bank by difficulty and by topic.

### Sources for this page
Kudeki notes, Lecture 18 (all of it, including the margin pulse plots). Shao, Lecture 18 slides: motivation (3), current sheet (4–11; Lecture 19 material in the notes, used here only for symmetry and sign), component equations (12–16), factoring (17–20), $H_y$ (21), $v_p = c$ (slides' $v_p$ = this site's $v$), $\eta_0$ (22), slides 24–26. This site's own: solutions to slides 24 and 26 (checked numerically), the assumption list, necessary-not-sufficient, the "why every solution" derivation, $\eta = \mu v$, the mirror rule, §7's numbers, all figures. Slips in the course material: see [[0-toolkit/04-errata-in-the-course-materials|errata]].
