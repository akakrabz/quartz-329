---
title: "Lecture 21 — Monochromatic waves and phasor notation"
description: "Single-frequency waves (T, λ, v_p), dispersion relations, phasors and the Ẽ ↔ H̃ rule, the notes' sheet in phasor form and time averages from phasors; the content lives on the topic pages linked from each section."
tags: [lecture, waves]
lecture: 21
---

*Lecture 21 · course notes §21 · **slides: not yet available — this page is built from the course notes** · prev: [[3-maxwell-and-waves/20-poynting-theorem-and-monochromatic-waves|Lecture 20]] · next: [[3-maxwell-and-waves/22-phasor-maxwell-equations-and-damped-waves|Lecture 22]] · worked problem: [[problems/phasors-e-and-power-from-a-given-h|Phasors, E and power from a given H]] · practice: [[practice/21-phasors-and-monochromatic-waves|12 problems]]*

> [!abstract] In one breath
> [[3-maxwell-and-waves/19-dalembert-solutions-and-radiation-from-current-sheets|Lecture 19]]'s sheet radiates the **monochromatic** wave $\cos(\omega t\mp\beta z)$: $T = 2\pi/\omega$, $\lambda = 2\pi/\beta$, $v_p = \omega/\beta = \lambda f$; its **dispersion relation** $\beta(\omega)$ holds the physics. **Phasors**, $a(t) = \text{Re}\{\tilde Ae^{j\omega t}\}$, make calculus algebra: sine → $-j$, $d/dt\to j\omega$, $+z$ travel is $e^{-j\beta z}$, $\tilde{\mathbf{H}}$ is $\tilde{\mathbf{E}}/\eta$ rotated, $\langle\mathbf{S}\rangle = \tfrac12\text{Re}\{\tilde{\mathbf{E}}\times\tilde{\mathbf{H}}^*\}$.

## 1. Monochromatic waves: one frequency, two periodicities

$A\cos(\omega t\mp\beta z)$ with $\beta = \omega/v$: period $T$ at fixed $z$, wavelength $\lambda$ at fixed $t$, crests at $v_p = \omega/\beta = \lambda f$. Example: $12\cos(4\pi\times10^8t - \tfrac{8\pi}{3}y)\,\hat z$ V/m is 200 MHz, $\lambda = 0.75$ m, $v_p = c/2$, $\epsilon_r = 4$. The notes' spectrum chart, with $f = c/\lambda$ per band.

→ Full treatment: [[concepts/monochromatic-waves|Monochromatic waves]]

## 2. Dispersion relations and phase velocity

The notes' three: TEM in a dielectric ($\beta = \omega\sqrt{\mu\epsilon}$), sound in a monatomic gas, TEM in a collisionless plasma ($\beta = \sqrt{\omega^2 - \omega_p^2}/c$, $v_p>c$, no wave below $f_p\approx9\sqrt N$ Hz). Helium 1019 m/s; the ionosphere at 10 MHz, $v_p = 2.27c$. Folded: the plasma relation from Lecture 11's Drude equation.

→ Full treatment: [[concepts/dispersion-relation|Dispersion relation and phase velocity]]

## 3. Phasors: a rotating arrow and its shadow

$\tilde A = Ae^{j\theta}$ for $A\cos(\omega t + \theta)$; sine → $-j$; the time-function → phasor table; $d/dt\to j\omega$, delay → $e^{-j\omega\tau}$; no phasor for products; vector phasors $\tilde{\mathbf{E}} = E_0e^{\mp j\beta z}\hat x$. Trap: no $t$ in a phasor, nothing complex in a field.

→ Full treatment: [[concepts/phasors|Phasors]]

## 4. Plane-wave phasors and the direction-of-travel trap

$e^{-j\beta z}$ travels toward $+z$, $e^{+j\beta z}$ toward $-z$, $e^{-j\beta\hat u\cdot\mathbf{r}}$ toward $\hat u$; the exam template $e^{j(ax + by + cz)}$ has $(a, b, c) = -\beta\hat u$ (450 MHz toward $-\hat z$ in $\epsilon_r = 4$: $c = +6\pi$ rad/m).

→ Full treatment: [[concepts/phasors|Phasors]]

## 5. The partner field: divide by η and rotate

$\tilde{\mathbf{H}} = \hat u\times\tilde{\mathbf{E}}/\eta$, $\tilde{\mathbf{S}} = \tilde{\mathbf{E}}\times\tilde{\mathbf{H}}^* = \lvert\tilde{\mathbf{E}}\rvert^2\hat u/\eta$ (why the conjugate); folded: from phasor Faraday. The notes' Example 1 (four rows checked) and Example 2 (two counter-propagating waves, each with its own $\hat u$); the 200 MHz wave's $\tilde{\mathbf{H}} = 63.7e^{-j(8\pi/3)y}\hat x$ mA/m.

→ Full treatment: [[concepts/phasors|Phasors]]

## 6. The notes' Example 3: a monochromatic current sheet in phasor form

$\tilde{\mathbf{E}} = -\tfrac\eta2\tilde{\mathbf{J}}_se^{-j\beta d}$, $\tilde{\mathbf{H}} = \tfrac12\tilde{\mathbf{J}}_s\times\hat n\,e^{-j\beta d}$; the notes' $2\hat x$ A/m sheet gives $\tilde{\mathbf{E}}^\pm = -\eta e^{\mp j\beta z}\hat x$, $\tilde{\mathbf{H}}^\pm = \mp e^{\mp j\beta z}\hat y$; a sine sheet picks up $j$.

→ Full treatment: [[concepts/phasors|Phasors]] · [[concepts/current-sheet-radiation|Radiation from a current sheet]]

## 7. Time averages straight from phasors

$\langle ab\rangle = \tfrac12\text{Re}\{\tilde A\tilde B^*\}$ (folded proof), so $\langle\mathbf{S}\rangle = \tfrac12\text{Re}\{\tilde{\mathbf{E}}\times\tilde{\mathbf{H}}^*\} = \lvert\tilde{\mathbf{E}}_0\rvert^2\hat u/2\eta$ and $\langle\mathbf{J}\cdot\mathbf{E}\rangle = \tfrac12\text{Re}\{\tilde{\mathbf{J}}\cdot\tilde{\mathbf{E}}^*\}$. The notes' sheet again: $\pm60\pi\,\hat z$ W/m² per side, $120\pi$ W/m² injected; Example 2's counter-propagating waves subtract; only $\text{Re}\{\sigma\}$ heats.

→ Full treatment: [[concepts/time-average-power|Time averages and average power]]

## 8. Connections

Next: Lecture 22 (complex $\gamma = \alpha + j\beta$, $\eta$), [[3-maxwell-and-waves/24-signal-transmission-and-circular-polarization|Lecture 24]] (circular polarization, $v_g$), [[3-maxwell-and-waves/25-wave-reflection-and-transmission|Lecture 25]] (reflection), Unit 4 ($\tilde V(z)$, $\tilde I(z)$).

## 9. Summary

The In-one-breath box, plus: $(a, b, c) = -\beta\hat u$; sheet $\tilde{\mathbf{E}} = -\tfrac\eta2\tilde{\mathbf{J}}_se^{-j\beta d}$; $\langle ab\rangle = \tfrac12\text{Re}\{\tilde A\tilde B^*\}$; one wave carries $\lvert\tilde{\mathbf{E}}_0\rvert^2/2\eta$; no plasma wave below $f_p\approx9\sqrt N$ Hz.

Concept pages: [[concepts/monochromatic-waves]] · [[concepts/phasors]] · [[concepts/dispersion-relation]] · [[concepts/time-average-power]] · [[concepts/plane-waves]] · [[concepts/poynting-vector]] · [[concepts/poynting-theorem]] · [[concepts/intrinsic-impedance]] · [[concepts/current-sheet-radiation]] · [[concepts/conductivity-and-susceptibility-models]].

> [!exam] On exams
> Opens most Exam 3 wave problems: time → phasor with sines, $\tilde{\mathbf{H}}\leftrightarrow\tilde{\mathbf{E}}$ (direction first), numbers off an expression and the $e^{j(ax+by+cz)}$ template, $\langle\mathbf{S}\rangle$ by components. Traps: $e^{+j\beta x}$ direction, a sine's $-j$, the template's plus, the $\tfrac12$. Papers and methods: [[concepts/phasors|Phasors]], [[concepts/monochromatic-waves|Monochromatic waves]], [[concepts/time-average-power|Time averages]]; [[problems/phasors-e-and-power-from-a-given-h|worked problem]].

> [!tip] Practice this lecture
> [[practice/21-phasors-and-monochromatic-waves|12 practice problems]] — 5 easy, 3 medium, 4 hard — each with a folded hint and a worked solution. Start with [[practice/21-phasors-and-monochromatic-waves#211-reading-two-waves|21.1 Reading two waves]]; the [[practice/index|practice hub]] has the whole bank by difficulty and by topic.

### Sources for this page
Kudeki notes, Lecture 21 (8 pages); no slides. Notes: §§1–2, spectrum chart, Examples 1–3, $\tilde{\mathbf{E}}\leftrightarrow\tilde{\mathbf{H}}$ rules, time averages. Rao (2009) §1.4, §4.5, §8.1, §8.3, §10.1. This site's own: derivations, Example 2's power, the sine current, numbered examples, figures (script-checked). Slips in the course material: see [[0-toolkit/04-errata-in-the-course-materials|errata]].
