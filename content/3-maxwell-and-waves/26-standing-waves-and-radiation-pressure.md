---
title: "Lecture 26 — Standing waves and radiation pressure"
description: "A perfect mirror turns incident plus reflected wave into a standing wave with fixed nodes and no net power; its surface current is a good conductor's skin current, and J × B on it is the radiation pressure 2⟨S_i⟩/c; the content lives on the topic pages linked from each section."
tags: [lecture, waves]
lecture: 26
---

*Lecture 26 · course notes §26 (no slides) · prev: [[3-maxwell-and-waves/25-wave-reflection-and-transmission|Lecture 25]] · next: [[4-transmission-lines/27-guided-tem-waves-on-transmission-lines|Lecture 27]] · worked problem: [[problems/a-circular-wave-meets-a-mirror|A circular wave meets a mirror]] · practice: [[practice/26-standing-waves-and-radiation-pressure|12 problems]]*

> [!abstract] In one breath
> A perfect mirror reflects with $\Gamma = -1$. Incident plus reflected wave make a **standing wave**: $\mathbf{E}\propto\sin\beta z\,\sin\omega t$ and $\mathbf{H}\propto\cos\beta z\,\cos\omega t$. The pattern does not travel; it oscillates in place. $\mathbf{E}$ has nodes at the mirror and every $\lambda/2$, and $\mathbf{H}$ has nodes halfway between. No power flows on average; the energy sloshes between electric and magnetic form. The mirror carries a surface current $2E_0/\eta_1$, the depth integral of a good conductor's skin current. $\mathbf{J}\times\mathbf{B}$ on that current pushes the mirror with the **radiation pressure** $2\langle S_i\rangle/c$: waves carry momentum.

## 1. Incident plus reflected: the standing wave

$\Gamma = -1$: $\tilde{\mathbf{E}} = -j\hat x\,2E_0\sin\beta_1z$, $\tilde{\mathbf{H}} = \hat y\,(2E_0/\eta_1)\cos\beta_1z$; in time $\sin\beta_1z\sin\omega t$ and $\cos\beta_1z\cos\omega t$, a function of $z$ times a function of $t$, or two equal waves travelling opposite ways.

→ Full treatment: [[concepts/standing-waves|Standing waves]]

## 2. Nodes, antinodes and time quadrature

$\mathbf{E}$ nodes at the mirror and every $\lambda/2$, $\mathbf{H}$ nodes $\lambda/4$ away; $\mathbf{E}$ and $\mathbf{H}$ a quarter period apart; nodes as shorts and opens. Partial reflection ($\lvert\Gamma\rvert<1$): travelling plus standing, $\lvert\tilde E\rvert$ between $(1\pm\lvert\Gamma\rvert)E_0$.

→ Full treatment: [[concepts/standing-waves|Standing waves]]

## 3. No net power; the energy sloshes

$\langle\mathbf{S}\rangle = 0$ from $\text{Re}\{-j\} = 0$; instantaneous $\mathbf{S}\propto\sin2\beta_1z\sin2\omega t$ moves energy between $\mathbf{H}$ and $\mathbf{E}$ antinodes; $\langle w\rangle = \epsilon_1E_0^2$ everywhere, each $\lambda/4$ cell keeping its energy.

→ Full treatment: [[concepts/standing-waves|Standing waves]]

## 4. The mirror's surface current

$\mathbf{J}_s = \hat n\times\mathbf{H}_1 = \hat x\,(2E_0/\eta_1)\cos\omega t$, along the incident $\mathbf{E}$; as a radiating sheet it cancels the incident wave behind the mirror and produces the reflected wave in front.

→ Full treatment: [[concepts/standing-waves|Standing waves]] · [[concepts/current-sheet-radiation|Radiation from a current sheet]]

## 5. A good conductor: where the surface current comes from

Lecture 25's transmitted fields in a good conductor: $\int_0^\infty\tilde{\mathbf{J}}_t\,dz = \hat x\,\sigma_2\tau E_0/\gamma_2\approx\hat x\,2E_0/\eta_0$ (the notes' box), since $\sigma\eta = \gamma$; the surface resistance $R_s = 1/(\sigma\delta) = \text{Re}\{\eta_2\}$ and the loss $\tfrac12R_s\lvert\tilde{\mathbf{J}}_s\rvert^2$. Example: a copper mirror at 10 GHz reflects 99.97 %.

→ Full treatment: [[concepts/standing-waves|Standing waves]] · [[concepts/skin-depth|Skin depth]]

## 6. Radiation pressure

$\mathbf{P}_{rad} = \int\mathbf{J}_t\times\mathbf{B}_t\,dz$, averaging to $2\langle\mathbf{S}_i\rangle/c$ (the notes' box; derivation folded): momentum density $\langle S\rangle/c^2$, the 2 from recoil, an absorber's $\langle S_i\rangle/c$, the instantaneous $4\langle S_i\rangle/c\cos^2\omega t$, photons with $\hbar\omega/c$. Sunlight on a mirror: 9.08 µPa; a 1 W laser: 6.7 nN.

→ Full treatment: [[concepts/radiation-pressure|Radiation pressure]]

## 7. Summary

- PEC mirror: $\tilde{\mathbf{E}} = -j\hat x\,2E_0\sin\beta_1z$, $\tilde{\mathbf{H}} = \hat y\,(2E_0/\eta_1)\cos\beta_1z$; in time, $\sin\beta_1z\sin\omega t$ and $\cos\beta_1z\cos\omega t$.
- $\mathbf{E}$ nodes at the mirror and every $\lambda/2$; $\mathbf{H}$ nodes $\lambda/4$ away from them. $\mathbf{E}$ and $\mathbf{H}$ are 90° apart in time.
- $\langle\mathbf{S}\rangle = 0$. $\mathbf{S}$ pulses at $2\omega$, moving energy between $\mathbf{H}$ and $\mathbf{E}$ antinodes; $\langle w\rangle = \epsilon_1E_0^2$.
- $\lvert\Gamma\rvert<1$: travelling plus standing, $\lvert\tilde E\rvert$ between $(1\pm\lvert\Gamma\rvert)E_0$.
- $\mathbf{J}_s = \hat x\,(2E_0/\eta_1)\cos\omega t$; in a good conductor it is $\int\tilde{\mathbf{J}}_t\,dz$, and $R_s = 1/\sigma\delta$ gives the loss $\tfrac12R_s\lvert\tilde{\mathbf{J}}_s\rvert^2$.
- $\langle P_{rad}\rangle = 2\langle S_i\rangle/c$ (mirror), $\langle S_i\rangle/c$ (absorber); momentum density $\langle S\rangle/c^2$.
- Next, [[4-transmission-lines/27-guided-tem-waves-on-transmission-lines|Lecture 27]]: plane waves guided between conducting plates.

Concept pages: [[concepts/standing-waves]] · [[concepts/radiation-pressure]] · [[concepts/reflection-and-transmission]] · [[concepts/skin-depth]] · [[concepts/poynting-vector]] · [[concepts/time-average-power]] · [[concepts/lorentz-force]].

> [!exam] On exams
> Standing waves conceptually, radiation pressure never: does a $\sin\cdot\sin$, $\cos\cdot\cos$ pair satisfy Maxwell's equations and carry net power (SP17 #1b–c); what a PEC leaves in front of the mirror (SP19 #3c); energy density and fixed-node plots, instantaneous against average, $\mathbf{E}$ against $\mathbf{H}$ (FA23 #1(c)–(d)). Methods: [[concepts/standing-waves|Standing waves]]; [[problems/a-circular-wave-meets-a-mirror|worked problem]].

> [!tip] Practice this lecture
> [[practice/26-standing-waves-and-radiation-pressure|12 practice problems]] — 5 easy, 3 medium, 4 hard — each with a folded hint and a worked solution. Start with [[practice/26-standing-waves-and-radiation-pressure#261-nodes-in-front-of-a-mirror|26.1 Nodes in front of a mirror]]; the [[practice/index|practice hub]] has the whole bank by difficulty and by topic.

### Sources for this page
Kudeki notes, Lecture 26 (6 pages): the standing-wave phasors and real forms, the node figures and short/open margin notes, the $\langle\mathbf{S}\rangle = 0$ check, the surface current, the effective-surface-current and surface-resistance boxes, and the radiation-pressure box with its momentum notes. Rao (2009) §5.6, §7.1–7.2 (complete and partial standing waves). This site's own: the figures, the partial-reflection paragraph, §3's $\mathbf{S}$ and $w$, the sheet check, $R_s = 1/\sigma\delta = \text{Re}\{\eta_2\}$, the instantaneous pressure, and the examples; numbers checked by script. Slips in the notes (a missing conjugate, a citation year, a $\Gamma>0$ margin figure) are on the errata page.
