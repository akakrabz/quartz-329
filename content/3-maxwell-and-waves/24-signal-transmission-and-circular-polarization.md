---
title: "Lecture 24 — Signal transmission and circular polarization"
description: "Narrowband AM on a plane wave, group velocity in a dispersive medium, and circular polarization with the notes' hand rule, bases, rotating sheet and power; the content lives on the topic pages linked from each section."
tags: [lecture, waves]
lecture: 24
---

*Lecture 24 · course notes §24 (no slides) · prev: [[3-maxwell-and-waves/23-imperfect-dielectrics-and-good-conductors|Lecture 23]] · next: [[3-maxwell-and-waves/25-wave-reflection-and-transmission|Lecture 25]] · worked problem: [[problems/two-sheets-a-quarter-wave-apart|Two crossed sheets a quarter wave apart]] · practice: [[practice/24-group-velocity-and-polarization|12 problems]]*

> [!abstract] In one breath
> A message $m(t)$ on a carrier $\cos\omega t$ rides a plane wave unchanged in a non-dispersive medium. In a dispersive medium the envelope travels at the **group velocity** $v_g = d\omega/d\beta$, the crests at $v_p = \omega/\beta$. The carrier's direction is its **polarization**. An $\hat x$ cosine plus a $\hat y$ sine gives a field vector that rotates once per period: **circular polarization**, phasor $(\hat x\mp j\hat y)e^{-j\beta z}$. The hand whose fingers curl with the rotation, thumb along the travel, names it right- or left-circular. It carries twice the power of either component.

## 1. Narrowband AM in a non-dispersive medium

Field 1: $m(t - z/v)\cos(\omega t - \beta z)\,\hat x$ with its $\mathbf{H}$; envelope and crests move together at $v$, the message arrives delayed and undistorted. Fields 2 and 3: $y$-polarized carriers, cosine and sine.

→ Full treatment: [[concepts/group-velocity|Group velocity]]

## 2. Dispersive media: group velocity

$\mathbf{E}\approx m(t - z/v_g)\cos(\omega t - \beta z)\,\hat x$, $v_g = d\omega/d\beta$ (the notes' footnote; derivation folded); table of $v_p$, $v_g$ for the dielectric, gas and plasma ($v_pv_g = c^2$). Example: 10 MHz through $10^{12}$ m⁻³ plasma, $v_g = 0.440c$, 2.27 ms across 300 km.

→ Full treatment: [[concepts/group-velocity|Group velocity]]

## 3. Circular polarization: a rotating carrier

Fields 1 and 3 together: the carrier vector rotates once per period; $(\hat x - j\hat y)e^{-j\beta z}$ right-circular, $(\hat x + j\hat y)e^{-j\beta z}$ left-circular; why some links use circular carriers.

→ Full treatment: [[concepts/wave-polarization|Wave polarization]]

## 4. Right or left: the notes' rule

Thumb along the travel, fingers with the rotation; the leading component points first; a three-step recipe for any phasor. Example 1 (notes): $(\hat z + j\hat y)e^{j\beta x}$ travels toward $-x$ and is left-circular.

→ Full treatment: [[concepts/wave-polarization|Wave polarization]]

## 5. Linear, circular, elliptical

$(A\hat x + Be^{j\phi}\hat y)e^{-j\beta z}$: linear for $\phi = 0, \pi$; circular for $A = B$, $\phi = \mp\pi/2$; elliptical otherwise; swap hands for $-z$ travel, cyclic axes otherwise.

→ Full treatment: [[concepts/wave-polarization|Wave polarization]]

## 6. Orthogonal bases

Circulars from linears and back ($\hat x = \tfrac12(\hat x - j\hat y) + \tfrac12(\hat x + j\hat y)$); the circular pair as the fundamental basis, photon spin $\pm\hbar$; why polarization matters (sources, forces, angular momentum).

→ Full treatment: [[concepts/wave-polarization|Wave polarization]]

## 7. A rotating current sheet

Example 2 (notes): $\mathbf{J}_s = m(t)[\cos\omega t\,\hat x + \sin\omega t\,\hat y]$ radiates right-circular into $z>0$ and left-circular into $z<0$.

→ Full treatment: [[concepts/wave-polarization|Wave polarization]] · [[concepts/current-sheet-radiation|Radiation from a current sheet]]

## 8. Power of a circular wave

Example 3 (notes): $(\hat x - j\hat y)e^{-j\beta z}$ V/m carries $\hat z/\eta_0\approx2.65$ mW/m², twice a linear wave's; in general $\langle\mathbf{S}\rangle = (\lvert\tilde E_x\rvert^2 + \lvert\tilde E_y\rvert^2)\hat u/2\eta$, and a circular wave's instantaneous $\mathbf{S}$ is constant.

→ Full treatment: [[concepts/wave-polarization|Wave polarization]] · [[concepts/time-average-power|Time averages and average power]]

## 9. Summary

- Non-dispersive medium: $m(t - z/v)\cos(\omega t - \beta z)$, undistorted. Dispersive: envelope at $v_g = d\omega/d\beta$, crests at $v_p = \omega/\beta$; plasma $v_pv_g = c^2$.
- An $\hat x$ cosine plus a $\hat y$ sine carrier rotates once per period. For travel along $+z$, $(\hat x - j\hat y)e^{-j\beta z}$ is right-circular and $(\hat x + j\hat y)e^{-j\beta z}$ left-circular.
- Hand rule: thumb along the travel; the hand whose fingers follow the rotation names it. The leading component points first.
- $A\hat x + Be^{j\phi}\hat y$: linear for $\phi = 0, \pi$; circular for $A = B$, $\phi = \mp\pi/2$; elliptical otherwise.
- Linear and circular pairs are bases for each other.
- A rotating sheet current: right-circular on one side, left-circular on the other.
- $\langle\mathbf{S}\rangle = (\lvert\tilde E_x\rvert^2 + \lvert\tilde E_y\rvert^2)/2\eta$: a circular wave carries twice a component's power.

> [!exam] On exams
> Every Lecture 24 item on the Exam 3 papers on hand is about polarization; none asks about group velocity. Name the polarization (SP17 #4c, SP18 #1(iii)–(iv), SP19 #3a, FA23 #2), build the phasor from a hand and snapshots (Summer 2017–2019 HE3), two sheets one phase (Summer 2020 FE #4; [[problems/two-sheets-a-quarter-wave-apart|worked problem]]), power by components, bases (FA23 #1(a)). Methods: [[concepts/wave-polarization|Wave polarization]].

> [!tip] Practice this lecture
> [[practice/24-group-velocity-and-polarization|12 practice problems]] — 5 easy, 3 medium, 4 hard — each with a folded hint and a worked solution. Start with [[practice/24-group-velocity-and-polarization#241-crests-and-envelope-in-a-plasma|24.1 Crests and envelope in a plasma]]; the [[practice/index|practice hub]] has the whole bank by difficulty and by topic.

### Sources for this page
Kudeki notes, Lecture 24 (9 pages): Fields 1–3 and the group-velocity footnote; the circular carrier, its $\mathbf{H}$ and phasors; the hand rule and margin figures; Example 1; bases; the helicity footnote; why polarization matters; Examples 2–3. Rao (2009) §1.4 and §4.5 (polarization, same handedness convention), §8.3 (group velocity), §10.1–10.2 (plasma, Faraday rotation). This site's own: the derivation and $v_g$ table, the ionosphere numbers, the recipe, §5, the $\langle\mathbf{S}\rangle$ formula, and all figures; numbers checked by script. Slips in the notes: Example 3 prints V/m for $\tilde{\mathbf{H}}_c$ (A/m); footnote 1's "β non-linear in ω" means "not proportional to ω".
