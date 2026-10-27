---
title: "Lecture 23 — Imperfect dielectrics and good conductors"
description: "The loss tangent σ/ωε sorts media into imperfect dielectrics and good conductors, with the notes' regime table, skin depth, seawater and submarines, and metals; the content lives on the topic pages linked from each section."
tags: [lecture, waves]
lecture: 23
---

*Lecture 23 · course notes §23 · **slides: not yet available — this page is built from the course notes** · prev: [[3-maxwell-and-waves/22-phasor-maxwell-equations-and-damped-waves|Lecture 22]] · next: [[3-maxwell-and-waves/24-signal-transmission-and-circular-polarization|Lecture 24]] · worked problem: [[problems/a-radio-wave-into-moist-ground|A radio wave into moist ground]] · practice: [[practice/23-imperfect-dielectrics-and-good-conductors|12 problems]]*

> [!abstract] In one breath
> The **loss tangent** $\sigma/\omega\epsilon$, conduction over displacement current, sorts the damped waves of [[3-maxwell-and-waves/22-phasor-maxwell-equations-and-damped-waves|Lecture 22]]. Small: an **imperfect dielectric**, $\alpha\approx(\sigma/2)\sqrt{\mu/\epsilon}$, the rate at which Joule heat drains the Poynting flux. Large: a **good conductor**, $\alpha = \beta = 1/\delta$ with **skin depth** $\delta = 1/\sqrt{\pi f\mu\sigma}$ and $\eta = (1+j)/(\sigma\delta)$, the field gone within a wavelength. Power falls as $e^{-2\alpha z}$. Seawater's $\delta$ is 7.96 m at 1 kHz but 1.3 cm at 1 GHz: hence slow very-low-frequency submarine links.

## 1. When does a medium count as a conductor?

Conduction current in phase and dissipating, displacement current 90° ahead and lossless; their ratio $\sigma/\omega\epsilon$ names four regimes (imperfect dielectric below 0.1, good conductor above 10), with the crossover $f_c = \sigma/2\pi\epsilon = 1/(2\pi\tau_r)$. A table of media (copper to mica); seawater at four frequencies ($8.9\times10^5$ at 1 kHz to 0.089 at 10 GHz).

→ Full treatment: [[concepts/loss-tangent|Loss tangent]]

## 2. The notes' table, and the one number behind it

The regime table; polar form $1 - jp = \sqrt{1 + p^2}e^{-j\theta}$ gives exact $\alpha$, $\beta$, $\lvert\eta\rvert$ and $\tau = \theta/2\le45^\circ$ at once; accuracy of the shortcuts at $p = 0.1$, 1, 10; the attenuation plateau above $10f_c$. Example: $\lambda = 0.5$ m, $\delta = 20$ m at 200 MHz: imperfect dielectric, $\epsilon_r = 9$, $\sigma = 8.0\times10^{-4}$ S/m.

→ Full treatment: [[concepts/loss-tangent|Loss tangent]] · [[concepts/skin-depth|Skin depth]] ($\alpha$ against frequency)

## 3. Imperfect dielectrics: slow decay, and where the power goes

Notes' Example 1: 2 V/m at 1 GHz in $\epsilon_r = 4$, $\sigma = 10^{-3}$ S/m: $\alpha = 0.094$ Np/m, $\mathbf{H}$ lags 0.13°, $\langle S\rangle = 10.6$ mW/m² at $z = 0$, 15 % left at 10 m. $\langle\mathbf{S}\rangle\propto\cos\tau\,e^{-2\alpha z}$; the averaged Poynting theorem gives $\alpha = \sigma\lvert\eta\rvert/(2\cos\tau)$ exactly: the table's $\alpha$ is energy conservation.

→ Full treatment: [[concepts/loss-tangent|Loss tangent]] (power in a lossy medium) · [[concepts/skin-depth|Skin depth]] (Example 1) · [[concepts/time-average-power|Time averages and average power]] (energy balance)

## 4. Good conductors: skin depth, $\eta = (1+j)/(\sigma\delta)$ and the 45° lag

$\delta = 1/\sqrt{\pi f\mu\sigma}$, $\gamma = (1 + j)/\delta$, $\lambda = 2\pi\delta$, $v_p = \omega\delta$; dead within a wavelength (54.6 dB), slow and dispersive, $\mathbf{H}$ large and 45° behind; $\text{Re}\{\eta\} = 1/(\sigma\delta)$ as a surface resistance. Notes' Example 2 (the same 2 V/m wave at 1 kHz in seawater: 45 A/m, 31.8 W/m²) and Example 3 ($\delta = 25/\pi = 7.96$ m).

→ Full treatment: [[concepts/skin-depth|Skin depth]]

## 5. Why submarines are called at very low frequencies

Fixing the medium, $\alpha = \sqrt{\pi f\mu\sigma}$ falls with frequency: 0.30 dB/m at 76 Hz against 673 dB/m at 1 GHz; a 100 dB budget reaches $11.5\,\delta$ (330 m at ELF, 19 m at VLF). Prices: bandwidth and antennas.

→ Full treatment: [[concepts/skin-depth|Skin depth]]

## 6. Skin depth in metals

Copper $\delta = 0.0661/\sqrt f$ m (8.5 mm at 60 Hz, 2.1 µm at 1 GHz), aluminium 1.29 times that; skin effect in wires, shielding, copper's milliohm $\lvert\eta\rvert$ as a near short; "good at all frequencies" fails in the infrared.

→ Full treatment: [[concepts/skin-depth|Skin depth]]

## 7. Reading a lossy-medium problem

Classify, constants, fields, power ($e^{-2\alpha d}$, $8.686\,\alpha\,d$ dB), inverse; the traps (own $\epsilon$, $2\pi f$, distance travelled, $\cos\tau$).

→ Full treatment: [[concepts/loss-tangent|Loss tangent]]

## 8. Connections

**Lecture 25 (ahead):** a good conductor's tiny $\eta$ makes it a near-perfect reflector; SP17 Exam 3 #2(iv) asks for $\Gamma$ from a medium with $\sigma = 400\,\omega\epsilon_0$, $\epsilon = 4\epsilon_0$: decide its regime first.

## 9. Summary

$p = \sigma/\omega\epsilon$: below 0.1 imperfect dielectric, above 10 good conductor; $f_c = 1/(2\pi\tau_r)$. Exactly $\alpha/\beta = \tan\tau\le1$ and $\alpha = \sigma\lvert\eta\rvert/(2\cos\tau)$. Good conductor: $\alpha = \beta = 1/\delta$, $\eta = (1+j)/(\sigma\delta)$. Power $\propto e^{-2\alpha d}$.

> [!exam] On exams
> On every third-exam paper: classify then compute (seawater at 1 kHz, calculator-free $\delta$; Summer 2018/2019 HE3 #3b), regime from measured $\lambda$ and $\delta$ (Summer 2017 HE3 #2b), "possible or not" ($\alpha\le\beta$; Summer 2020 HE3 #3), good-conductor concepts (SP17, SP18), power against depth (FA23 #6). Methods and traps: [[concepts/loss-tangent|Loss tangent]], [[concepts/skin-depth|Skin depth]]; [[problems/a-radio-wave-into-moist-ground|worked problem]].

> [!tip] Practice this lecture
> [[practice/23-imperfect-dielectrics-and-good-conductors|12 practice problems]] — 5 easy, 3 medium, 4 hard — each with a folded hint and a worked solution. Start with [[practice/23-imperfect-dielectrics-and-good-conductors#231-six-media-at-one-frequency|23.1 Six media at one frequency]]; the [[practice/index|practice hub]] has the whole bank by difficulty and by topic.

### Sources for this page
Kudeki notes, Lecture 23 (6 pp.): the regime table; Examples 1–3 (paraphrased, script-checked); the heating, microwave-oven and communication remarks; the low-frequency argument and its bandwidth cost. No slides were available. Rao (2009) §§5.3–5.4, Tables 5.1–5.3: "loss tangent", crossover and thresholds, copper figures, 54.6 dB per wavelength, the antenna remark, Problem 5.26, material values. ITU-R P.527-6: loam conductivity, water permittivity. Wikipedia, "Communication with submarines": VLF/ELF data. This site's own: polar forms and accuracy figures, the energy balance, the media, seawater and metal tables, the fair 1 GHz comparison, the inverse example, recipe, traps, figures. Slips in the course material: see [[0-toolkit/04-errata-in-the-course-materials|errata]].
