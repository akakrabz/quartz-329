---
title: "Lecture 20 — Poynting's theorem and monochromatic waves"
description: "Poynting's theorem as an energy ledger, a resistive wire and a coax, the notes' cosine sheet and time averages; the content lives on the topic pages linked from each section."
tags: [lecture, waves]
lecture: 20
---

*Lecture 20 · course notes §20 · **slides: not yet available — this page is built from the course notes** · prev: [[3-maxwell-and-waves/19-dalembert-solutions-and-radiation-from-current-sheets|Lecture 19]] · next: [[3-maxwell-and-waves/21-monochromatic-waves-and-phasor-notation|Lecture 21]] · worked problem: [[problems/energy-bookkeeping-for-a-radiating-sheet|Energy bookkeeping for a radiating sheet]] · practice: [[practice/20-poynting-theorem-and-power|12 problems]]*

> [!abstract] In one breath
> Dot Faraday's law with $\mathbf{H}$ and Ampère–Maxwell with $\mathbf{E}$, subtract: **Poynting's theorem**, $\partial w/\partial t + \nabla\cdot\mathbf{S} + \mathbf{J}\cdot\mathbf{E} = 0$, with $w = \tfrac12\epsilon E^2 + \tfrac12\mu H^2$ and $\mathbf{S} = \mathbf{E}\times\mathbf{H}$ [W/m²]. It is [[3-maxwell-and-waves/16-charge-conservation-displacement-current-and-maxwells-equations|Lecture 16]]'s continuity equation for energy, plus an exchange term $\mathbf{J}\cdot\mathbf{E}$ (Joule heating if positive, a source if negative). A sheet $\hat x\,2\cos\omega t$ A/m radiates **monochromatic** waves, $\langle S\rangle = \eta_0/2\approx188$ W/m² per side, and injects $\eta_0\approx377$ W/m², the sum.

## 1. Where does the energy go?

Capacitor and inductor energies sit in the fields ($\tfrac12\epsilon E^2$, $\tfrac12\mu H^2$); resistors turn them into heat; Lecture 19's sheet feeds two waves. Charge has a continuity equation; energy needs one with an exchange term.

→ Full treatment: [[concepts/poynting-theorem|Poynting's theorem]]

## 2. Deriving the theorem from Maxwell's equations

$\mathbf{H}\cdot$(Faraday) $-\ \mathbf{E}\cdot$(Ampère–Maxwell); the vector identity makes the left side $\nabla\cdot(\mathbf{E}\times\mathbf{H})$, constant $\epsilon$, $\mu$ make the right side $-\partial w/\partial t - \mathbf{J}\cdot\mathbf{E}$. Folded: the identity in components and Rao's 1-D route.

→ Full treatment: [[concepts/poynting-theorem|Poynting's theorem]]

## 3. Reading the three terms

Storage, outflow ($\mathbf{S}$ as energy flux density, W/m²), transfer to charges ($\mathbf{J}\cdot\mathbf{E} = \sigma E^2$ in a conductor, negative at a battery or a radiating sheet). Side-by-side table with the continuity equation; a situation table; the leaky capacitor that empties without any energy flow ($\tau = 3.54$ µs, $\mathbf{S} = 0$).

→ Full treatment: [[concepts/poynting-theorem|Poynting's theorem]] · [[concepts/poynting-vector|Poynting vector]]

## 4. The integral form: a ledger for any volume

$-dW/dt = \oint\mathbf{S}\cdot d\mathbf{A} + \int\mathbf{J}\cdot\mathbf{E}\,dV$, with a recipe for using it. Example: a DC coax carries all of $VI$ in its dielectric, none in the copper. Only $\oint\mathbf{S}\cdot d\mathbf{A}$ is unambiguous (a charge beside a magnet).

→ Full treatment: [[concepts/poynting-theorem|Poynting's theorem]]

## 5. Joule heating at work: a wire is heated through its surface

Steady current: $\mathbf{S}$ points radially *into* the wire and its flux through the side is exactly $I^2R$; the 100 W nichrome heater takes 32 kW/m² through its surface.

→ Full treatment: [[concepts/poynting-theorem|Poynting's theorem]]

## 6. The notes' example: monochromatic waves from a cosine sheet

Notes' Example 1: $\mathbf{J}_s = \hat x\,2\cos\omega t$ A/m in vacuum radiates $\mathbf{E} = -\hat x\,\eta_0\cos(\omega t\mp\beta z)$, $\mathbf{H} = \mp\hat y\cos(\omega t\mp\beta z)$, $\mathbf{S} = \pm\hat z\,\eta_0\cos^2(\omega t\mp\beta z)$, and $\mathbf{J}_s\cdot\mathbf{E} = -2\eta_0\cos^2\omega t$ W/m²: the books balance at every instant on the sheet, only on average in a slab around it.

→ Full treatment: [[concepts/current-sheet-radiation|Radiation from a current sheet]] (the fields) · [[concepts/poynting-theorem|Poynting's theorem]] (the balance) · [[concepts/monochromatic-waves|Monochromatic waves]]

## 7. Time averages

$\langle\cos^2\rangle = \tfrac12$; the sheet's $\eta_0/2$ per side and $\eta_0$ injected; the time-averaged theorem $\nabla\cdot\langle\mathbf{S}\rangle = -\langle\mathbf{J}\cdot\mathbf{E}\rangle$; one wave's $\langle S\rangle = E_0^2/2\eta = v\langle w\rangle$; sea water heating, sunlight (1.01 kV/m), a 50 kW station at 10 km (0.173 V/m), perpendicular components adding, two opposite waves with $\langle\mathbf{S}\rangle = 0$.

→ Full treatment: [[concepts/time-average-power|Time averages and average power]]

## 8. Connections

- **Lectures 10, 15, 16, 19:** energy densities now general; continuity as template; the sheet injects $\tfrac\eta2J_s^2$ per m², half into each wave.
- **Lectures 21–23, Unit 4:** phasor averages; power decay $e^{-2\alpha z}$ in conductors; lines guide $\mathbf{S}$.

## 9. Summary

- $\mathbf{H}\cdot$(Faraday) $-\ \mathbf{E}\cdot$(Ampère–Maxwell) gives the theorem; $\mathbf{J}\cdot\mathbf{E} = \sigma E^2$ in a conductor, $<0$ at a source.
- $I^2R$ enters a resistor through its sides; coax power flows in the dielectric.
- Sheet, on average: $\eta_0/2$ per side, $\eta_0$ injected; one wave $\langle S\rangle = E_0^2/2\eta = v\langle w\rangle$; standing wave $\langle S\rangle = 0$, $\langle w\rangle\neq0$.

Concept pages: [[concepts/poynting-theorem]] · [[concepts/poynting-vector]] · [[concepts/time-average-power]] · [[concepts/continuity-equation]] · [[concepts/electrostatic-energy]] · [[concepts/magnetic-energy]] · [[concepts/conductors]] · [[concepts/current-sheet-radiation]] · [[concepts/plane-waves]] · [[concepts/divergence-theorem]].

> [!exam] On exams
> The last lecture on Midterm 2 ([[0-toolkit/05-midterm-2-summary#9-energy-and-power-poyntings-theorem-lecture-20|summary §9]]); Exam 3 papers ask for a wave's $E_0^2/(2\eta)$, "split, then add" for circular polarization, $\mathbf{J}\cdot\mathbf{E}$ in a conductor (peak and average), a radiating sheet's injected power split per side, standing-wave true/false, power against depth ($e^{-2\alpha z}$) and power through an area. Methods and papers: [[concepts/time-average-power|time averages]], [[concepts/poynting-theorem|Poynting's theorem]].

> [!tip] Practice this lecture
> [[practice/20-poynting-theorem-and-power|12 practice problems]] — 5 easy, 3 medium, 4 hard — each with a folded hint and a worked solution. Start with [[practice/20-poynting-theorem-and-power#201-reading-the-energy-ledger|20.1 Reading the energy ledger]]; the [[practice/index|practice hub]] has the whole bank by difficulty and by topic.

### Sources for this page
Kudeki notes, Lecture 20 (no slides yet): derivation, three terms, negative $\mathbf{J}\cdot\mathbf{E}$, Example 1 (numbers checked), time averages; $\eta_o$ for $\eta_0$. Rao (2009) §4.6, §5.3: the 1-D derivation, the $1/r$ argument (reworded). This site's own: validity conditions, the situation table, other examples, pillbox, slab, averaged theorem, traps, figures; numbers in `digest8/verify_L20.py`. Slips in the course material: see [[0-toolkit/04-errata-in-the-course-materials|errata]].
