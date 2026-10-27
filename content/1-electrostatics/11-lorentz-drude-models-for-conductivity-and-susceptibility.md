---
title: "Lecture 11 — Where σ and χe come from: the Lorentz–Drude models"
description: "Newton's law for one charge gives Ohm's law with σ = Nq²τ/m (complex at high frequency), the Lorentz-oscillator χe, the polarization current ∂P/∂t, and the surface charges that drive a current through a wire; the full treatment is on the topic pages linked from each section."
tags: [lecture, electrostatics]
lecture: 11
---

*Lecture 11 · course notes §11 · no slide deck (the slides jump from capacitance to Biot–Savart) · prev: [[1-electrostatics/10-capacitance-and-conductance|Lecture 10]] · next: [[2-magnetostatics/12-magnetic-force-biot-savart-and-amperes-law|Lecture 12]] · not on Exam 1 · practice: [[practice/11-lorentz-drude-models|8 problems]]*

> [!abstract] In one breath
> Unit 1 used two material constants without explaining them: $\sigma$ in $\mathbf{J} = \sigma\mathbf{E}$ ([[1-electrostatics/08-conductors-dielectrics-and-polarization|Lecture 8]]) and $\chi_e$ in $\mathbf{P} = \epsilon_0\chi_e\mathbf{E}$ ([[1-electrostatics/09-static-fields-in-dielectric-media|Lecture 9]]). The mechanism is Newton's second law for one charge at a time. A **free** carrier accelerates, collides, and settles at a drift velocity $\propto\mathbf{E}$: Ohm's law with $\sigma = Nq^2\tau/m$. A **bound** electron is pulled against a spring; $N_d$ such dipoles per unit volume give $\chi_e = N_de^2/(m\epsilon_0\omega_0^2)$. When the field varies the bound electrons move too — a **polarization current** $\partial\mathbf{P}/\partial t$ flows in a perfect insulator, half of what Lecture 16 adds to Ampère's law.

## 1. Two constants, one law of motion

$m\,d\mathbf{v}/dt = \sum\mathbf{F}$ averaged over carriers; free and bound charges differ only in the forces (no spring vs. $-m\omega_0^2\mathbf{r}$; collisions vs. radiation damping), so one gives a steady velocity (current), the other a steady displacement (polarization). The drift is a tiny coherent part on top of $\sim10^5$ m/s thermal motion.

→ Full treatment: [[concepts/conductivity-and-susceptibility-models|Lorentz–Drude models of σ and χe]]

## 2. Free carriers: the Drude model and Ohm's law

$m\dot{\mathbf{v}} = q\mathbf{E} - m\mathbf{v}/\tau$ settles at $\mathbf{v} = (q\tau/m)\mathbf{E}$ (mobility $\lvert q\tau/m\rvert$); the unit-cube count gives $\mathbf{J} = Nq\mathbf{v}$, hence $\sigma = \sum_sN_sq_s^2/(m_s\nu_s)$ — every species conducts in the same direction. Copper: $\tau\approx2.5\times10^{-14}$ s, 1 A in 1 mm² needs 0.017 V/m and drifts at $7\times10^{-5}$ m/s. Trap: this $\tau$ is not the relaxation time $\epsilon/\sigma$.

→ Full treatment: [[concepts/conductivity-and-susceptibility-models|Lorentz–Drude models of σ and χe]]

## 3. AC conductivity: when the carriers cannot keep up

Phasors turn $d/dt$ into $j\omega$: $\sigma(\omega) = \sigma_{\text{DC}}/(1+j\omega/\nu)$, the DC value for $\omega\ll\nu$ — copper's $\nu\sim4\times10^{13}$ s⁻¹ keeps it real through the microwave range (1 GHz: correction $1.6\times10^{-4}$). Complex $\sigma$ matters in the infrared and in plasmas.

→ Full treatment: [[concepts/conductivity-and-susceptibility-models|Lorentz–Drude models of σ and χe]]

## 4. Bound electrons: the Lorentz oscillator and χe

$m\ddot{\mathbf{r}} = -e\mathbf{E} - m\omega_0^2\mathbf{r} - 2m\alpha\dot{\mathbf{r}}$, an underdamped second-order system ringing at $\omega_0\sim10^{15}$–$10^{16}$ rad/s. DC: $\mathbf{p} = -e\mathbf{r} = (e^2/m\omega_0^2)\mathbf{E}$, so $\chi_e = N_de^2/(m\epsilon_0\omega_0^2)$ ($\approx0.45$ for glass-like numbers); AC (site extension): $\chi_e(\omega)$ resonant and complex near $\omega_0$ — dispersion and absorption.

→ Full treatment: [[concepts/conductivity-and-susceptibility-models|Lorentz–Drude models of σ and χe]]

## 5. Polarization current: bound charges that carry an AC current

A field varying slowly compared with $\omega_0$ drags the bound electrons along: $\mathbf{J}_p = -eN_d\mathbf{v} = \partial\mathbf{P}/\partial t$ — an AC current in a perfect insulator. Total current $\sigma\mathbf{E} + \partial\mathbf{P}/\partial t$; with the vacuum term, $\partial\mathbf{D}/\partial t$ — the leaky capacitor's $G$ and $C$ branches.

→ Full treatment: [[concepts/conductivity-and-susceptibility-models|Lorentz–Drude models of σ and χe]]

## 6. What drives the current in a wire? (a footnote worth a section)

Lecture 8's $\mathbf{E} = 0$ holds in *equilibrium*; a wire carrying current has $\mathbf{E} = \mathbf{J}/\sigma$ inside, produced by surface charges graded along the wire (Jefimenko 1962, Parker 1970) that follow every bend; an ideal zero-resistivity wire needs none — Lecture 12's neutral wire.

→ Full treatment: [[concepts/conductors|Conductors in electrostatics]]

## 7. Summary

- One law of motion, $m\,d\mathbf{v}/dt = \sum\mathbf{F}$, averaged over carriers.
- Free carriers: $\mathbf{v} = (q\tau/m)\mathbf{E}$, $\mathbf{J} = Nq\mathbf{v}$, $\sigma = \sum_sN_sq_s^2/(m_s\nu_s)$; AC: $\nu\to\nu + j\omega$, DC value valid for $\omega\ll\nu\sim10^{13}$ s⁻¹.
- Bound electrons: $m\ddot{\mathbf{r}} = -e\mathbf{E} - m\omega_0^2\mathbf{r} - 2m\alpha\dot{\mathbf{r}}$; DC $\chi_e = N_de^2/(m\epsilon_0\omega_0^2)$; AC $\chi_e(\omega)$ complex near $\omega_0$.
- $\mathbf{J}_p = \partial\mathbf{P}/\partial t$; Ampère's law will need the total $\sigma\mathbf{E} + \partial\mathbf{D}/\partial t$.
- The field in a current-carrying wire is made by surface charges on the wire.

Concept page: [[concepts/conductivity-and-susceptibility-models]] · related: [[concepts/conductors]] · [[concepts/polarization]] · [[concepts/permittivity]].

> [!exam] On exams
> Not on Exam 1. Testable content is small and conceptual: drift velocity from the force balance, $\mathbf{J} = Nq\mathbf{v}$, $\sigma\propto Nq^2\tau/m$ and why the DC value holds at radio frequencies, $\partial\mathbf{P}/\partial t$ is a current. Exam notes: [[concepts/conductivity-and-susceptibility-models]].

> [!tip] Practice this lecture
> [[practice/11-lorentz-drude-models|8 practice problems]] — 4 easy, 2 medium, 2 hard — each with a folded hint and a worked solution. Start with [[practice/11-lorentz-drude-models#111-drift-speed-in-a-house-wire|11.1 Drift speed in a house wire]]; the [[practice/index|practice hub]] has the whole bank by difficulty and by topic.

### Sources for this page
Kudeki notes, Lecture 11 (Drude force balance, mobility, unit-cube $\mathbf{J} = Nq\mathbf{v}$, species sum, AC conductivity, conductivity table, Lorentz oscillator, DC susceptibility, polarization current, $\sigma\mathbf{E} + d\mathbf{P}/dt$); Lecture 12 footnote 2 and the Jefimenko (1962) and Parker (1970) papers it cites. The site's own: copper numbers and the AC susceptibility formula, checked against the notes' DC limits.
