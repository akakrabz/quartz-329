---
title: "Lecture 25 — Wave reflection and transmission"
description: "A plane wave meeting a planar interface head-on splits into reflected and transmitted waves with Γ = (η₂ − η₁)/(η₂ + η₁) and τ = 1 + Γ; the content lives on the topic page linked from each section."
tags: [lecture, waves]
lecture: 25
---

*Lecture 25 · course notes §25 (no slides) · prev: [[3-maxwell-and-waves/24-signal-transmission-and-circular-polarization|Lecture 24]] · next: [[3-maxwell-and-waves/26-standing-waves-and-radiation-pressure|Lecture 26]] · worked problem: [[problems/working-back-from-a-transmitted-wave|Working back from a transmitted wave]] · practice: [[practice/25-reflection-and-transmission|12 problems]]*

> [!abstract] In one breath
> A plane wave hits the plane $z = 0$ head-on. On its own it would violate the boundary conditions there, so a reflected wave travels back into region 1 and a transmitted wave continues into region 2. Continuity of tangential $\tilde{\mathbf{E}}$ and $\tilde{\mathbf{H}}$ fixes their amplitudes: $\Gamma = (\eta_2-\eta_1)/(\eta_2+\eta_1)$ and $\tau = 1+\Gamma$. Equal impedances transmit everything. A perfect conductor ($\eta_2 = 0$) reflects everything, with $\Gamma = -1$. The fraction of the power reflected is $\lvert\Gamma\rvert^2$; the rest enters region 2.

## 1. Three waves at a planar interface

The notes' setup (lossless region 1, general region 2, no surface current for finite $\sigma_2$) and the three postulated phasor pairs: incident $E_0e^{-j\beta_1z}$, reflected $\Gamma E_0e^{j\beta_1z}$ with $\tilde{\mathbf{H}}_r$ carrying $-\Gamma$, transmitted $\tau E_0e^{-\gamma_2z}$. Notation: $\tau$ is the transmission coefficient here, $\angle\eta$ the phase of $\eta$.

→ Full treatment: [[concepts/reflection-and-transmission|Reflection and transmission coefficients]]

## 2. Matching tangential E and H: Γ and τ

Continuity at $z = 0$ gives $1 + \Gamma = \tau$ and $(1 - \Gamma)/\eta_1 = \tau/\eta_2$, hence $\Gamma = (\eta_2 - \eta_1)/(\eta_2 + \eta_1)$, $\tau = 2\eta_2/(\eta_2 + \eta_1)$; signs for real $\eta$'s, complex values for a lossy region 2, the $n$-form $\Gamma = (n_1 - n_2)/(n_1 + n_2)$; traps and a six-step recipe.

→ Full treatment: [[concepts/reflection-and-transmission|Reflection and transmission coefficients]]

## 3. Special cases

Perfect conductor ($\Gamma = -1$, $\tau = 0$, surface current $\hat x\,2E_0/\eta_1$); matched impedances ($\Gamma = 0$); lossless region 2 with partial reflection and the quarter-wave anti-glare coating of impedance $\sqrt{\eta_1\eta_2}$ (glass: $n_c = 1.22$, 112 nm for green light).

→ Full treatment: [[concepts/reflection-and-transmission|Reflection and transmission coefficients]]

## 4. Power balance

$1 = \lvert\Gamma\rvert^2 + \lvert\tau\rvert^2\eta_1\text{Re}\{1/\eta_2\}$ (proof folded, lossy case included). Example 1 (notes): vacuum onto $\epsilon_r = 9/4$, $\Gamma = -1/5$, $\tau = 4/5$, $0.02 + 0.48 = 0.5$ W/m². Air onto seawater at 1 kHz: 0.033 % enters.

→ Full treatment: [[concepts/reflection-and-transmission|Reflection and transmission coefficients]]

## 5. Summary

- Incident, reflected and transmitted phasors: $\hat x$ components $E_0e^{-j\beta_1z}$, $\Gamma E_0e^{j\beta_1z}$ and $\tau E_0e^{-\gamma_2z}$. Each $\tilde{\mathbf{H}}$ is $\hat u\times\tilde{\mathbf{E}}/\eta$, so the reflected $\tilde{\mathbf{H}}$ carries $-\Gamma$.
- Continuity of tangential $\tilde{\mathbf{E}}$ and $\tilde{\mathbf{H}}$ (no $\mathbf{J}_s$ for finite $\sigma_2$): $\Gamma = (\eta_2-\eta_1)/(\eta_2+\eta_1)$ and $\tau = 1+\Gamma = 2\eta_2/(\eta_2+\eta_1)$.
- Perfect conductor: $\Gamma = -1$, $\tau = 0$, $\tilde{\mathbf{J}}_s = \hat x\,2E_0/\eta_1$. Matched: $\Gamma = 0$, $\tau = 1$. Lossless region 2: partial reflection, reduced by a quarter-wave coating of impedance $\sqrt{\eta_1\eta_2}$.
- Power: $1 = \lvert\Gamma\rvert^2 + \lvert\tau\rvert^2\eta_1\text{Re}\{1/\eta_2\}$. Glass reflects 4 %.
- Next, [[3-maxwell-and-waves/26-standing-waves-and-radiation-pressure|Lecture 26]]: the standing wave in region 1, and radiation pressure.

Concept pages: [[concepts/reflection-and-transmission]] · [[concepts/boundary-conditions]] · [[concepts/intrinsic-impedance]] · [[concepts/poynting-vector]] · [[concepts/time-average-power]] · [[concepts/plane-waves]].

> [!exam] On exams
> Four Exam 3 problems on hand: work back from the *transmitted* wave to $\Gamma$, $\tau$ and the incident and reflected phasors (Summer 2017 HE3 #3c–f, SP18 #2d–e); a circular wave on a perfect conductor (SP19 #3b); a wave from a lossy medium into air (SP17 #2(iv), complex $\eta_1$). Methods and traps: [[concepts/reflection-and-transmission|Reflection and transmission coefficients]]; [[problems/working-back-from-a-transmitted-wave|worked problem]].

> [!tip] Practice this lecture
> [[practice/25-reflection-and-transmission|12 practice problems]] — 5 easy, 3 medium, 4 hard — each with a folded hint and a worked solution. Start with [[practice/25-reflection-and-transmission#251-four-interfaces|25.1 Four interfaces]]; the [[practice/index|practice hub]] has the whole bank by difficulty and by topic.

### Sources for this page
Kudeki notes, Lecture 25 (6 pages): the setup with the boundary conditions in the margin, the three postulated waves, the two matching conditions with the boxed $\Gamma$ and $\tau$, the three special cases with the quarter-wave footnote, and Example 1 with its power check. Rao (2009) §5.6, eqs. 5.101–5.105, for cross-checks. This site's own: the figures, the recipe, the lossy-case power proof, the $n$-form of $\Gamma$, the surface current (derived in the notes' Lecture 26), the coating and seawater examples; numbers checked by script. Slips in the notes (typos, a margin figure drawn for $\Gamma>0$) are on the errata page.
