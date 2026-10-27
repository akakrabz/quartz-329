---
title: "Lecture 19 — d'Alembert solutions and radiation from current sheets"
description: "Uniform plane TEM waves and their simplest source, an infinite current sheet radiating E = −(η/2)Jₛ and H = ½Jₛ × n̂ delayed by |z|/v; the full treatment is on the topic pages linked from each section."
tags: [lecture, waves]
lecture: 19
---

*Lecture 19 · course notes §19 · slides "Uniform Plane Waves in Free Space" (Lecture 19) · prev: [[3-maxwell-and-waves/18-the-wave-equation-and-plane-tem-waves|Lecture 18]] · next: [[3-maxwell-and-waves/20-poynting-theorem-and-monochromatic-waves|Lecture 20]] · worked problem: [[problems/a-current-sheet-launches-two-waves|A current sheet launches two waves]] · practice: [[practice/19-radiation-from-current-sheets|12 problems]]*

> [!abstract] In one breath
> Lecture 18's waves $f(t\mp z/v)$ are **uniform plane TEM waves**, travelling along the **Poynting vector** $\mathbf{E}\times\mathbf{H}$. An infinite sheet $\mathbf{J}_s(t)$ launches them: $\mathbf{H} = \tfrac12\mathbf{J}_s\times\hat n$ ([[2-magnetostatics/13-current-sheets-solenoids-and-the-vector-potential|Lecture 13]]) and $\mathbf{E} = -\tfrac{\eta}{2}\mathbf{J}_s$, both delayed by $\lvert z\rvert/v$. $\mathbf{E}$ opposes the current and is continuous; $\mathbf{H}$ reverses and jumps by $J_s$ ([[3-maxwell-and-waves/16-charge-conservation-displacement-current-and-maxwells-equations|Lecture 16]]). A cosine current gives $\beta = \omega/v$, $\lambda = 2\pi/\beta$, and outward $\mathbf{S}$ [W/m²].

## 1. What kind of wave is $f(t\mp z/v)$?

The notes name Lecture 18's d'Alembert pair a *uniform plane TEM wave*: $\mathbf{E}$, $\mathbf{H}$ transverse, travel along $\mathbf{S} = \mathbf{E}\times\mathbf{H}$, one field over each plane of constant phase moving at $v_p = v$; $\mathbf{H} = \hat u\times\mathbf{E}/\eta$.

→ Full treatment: [[concepts/plane-waves|Plane waves]]

## 2. Three warm-up examples (notes)

Example 1: a triangular pulse along $y$ and its $\mathbf{B}$ by rotation and by Faraday's law. Example 2: the wave's magnetic force is smaller than the electric by $v/c$. Example 3: a ramp pulse against $t$ (delayed) and against $z$ (mirrored).

→ Full treatment: [[concepts/intrinsic-impedance|Intrinsic impedance]] (Examples 1–2) · [[concepts/plane-waves|Plane waves]] (Example 3)

## 3. What launches a plane wave? The notes' route

Static sheet field $\tfrac12\mathbf{J}_s\times\hat n$ → quasi-static → delayed by $\lvert z\rvert/v$ (exact, by causality and uniqueness), $\mathbf{E} = -\tfrac\eta2\mathbf{J}_s(t\mp z/v)$ from the TEM rule; amplitudes $\eta J_s/2$ and $J_s/2$.

→ Full treatment: [[concepts/current-sheet-radiation|Radiation from a current sheet]]

## 4. The same result from boundary conditions (slides)

General solution $Af + Bg$, radiation condition, tangential $\mathbf{E}$ continuous, tangential $\mathbf{H}$ jumping by $\mathbf{J}_s$ ($2Af/\eta = J_s$), delay — the derivation to reproduce when asked; the any-orientation recipe.

→ Full treatment: [[concepts/current-sheet-radiation|Radiation from a current sheet]] · [[concepts/boundary-conditions|Boundary conditions]]

## 5. Reading the result

$\mathbf{E}$ even, $\mathbf{H}$ odd; $\mathbf{J}_s\cdot\mathbf{E}<0$, the sheet feeds the waves. Notes' Example 4: a ramp current ($-1$ to $+1$ A/m in 1 µs) at $t = 2$ µs — 300 m ramps of $H_y$ ($\pm0.5$ A/m) and $E_x$ ($\pm60\pi$ V/m) between 450 and 750 m each side. Slide 17: $\mathbf{E}$ from $\mathbf{H}$.

→ Full treatment: [[concepts/current-sheet-radiation|Radiation from a current sheet]]

## 6. Transforming time and space (slide 11)

Snapshot ↔ record by world lines $z = z_0 + vt$: slide 11's profile moved 100 m at $t = 1$ s, recorded reversed at $z = 0$, delayed 2 s at $z = 200$ m.

→ Full treatment: [[concepts/plane-waves|Plane waves]]

## 7. A sinusoidal sheet current: β, λ and the Poynting vector (slides)

$\mathbf{J}_s = -J_{s0}\cos(\omega t)\hat x$ radiates $\cos(\omega t\mp\beta z)$ waves, $\beta = \omega/v_p$; the parameter table ($\omega$, $f$, $\beta$, $\lambda$, $v_p$); $\mathbf{S} = \pm\hat z\,(\eta_0J_{s0}^2/4)\cos^2$, outward, peak 94.2 W/m² per side for 1 A/m; $4\pi$ of phase in 5 µs means 400 kHz, $\lambda = 750$ m.

→ Full treatment: [[concepts/current-sheet-radiation|Radiation from a current sheet]] · [[concepts/plane-waves|Plane waves]] (phase table) · [[concepts/poynting-vector|Poynting vector]]

## 8. An inverse problem: slides 18–21

From a given $\mathbf{H}$ snapshot beside a sheet on $x = 0$ (stem and plot disagree by 100; the site uses the plot's 2 A/m peak): the record at 400 m, the snapshot at 4 µs, $\mathbf{E}$ at 2 µs, and the current $\mathbf{J}_s = \hat z\,12(1 - t/\mu\text{s})$ A/m for $\tfrac23<t<1$ µs.

→ Full treatment: [[concepts/current-sheet-radiation|Radiation from a current sheet]]

## 9. Connections

Lectures 13, 16, 18 supply the static field, the jump conditions and the waves. Site picture: a sheet feeding an infinite parallel-plate line sees two lines in parallel, so $E = \eta J_s/2$.

→ Full treatment: [[concepts/intrinsic-impedance|Intrinsic impedance]]

## 10. Summary

- Sheet: $\mathbf{E} = -\tfrac\eta2\mathbf{J}_s(t - d/v)$, $\mathbf{H} = \tfrac12\mathbf{J}_s(t - d/v)\times\hat n$; $\mathbf{E}$ even, $\mathbf{H}$ odd, $\mathbf{S}$ outward, $\mathbf{J}_s\cdot\mathbf{E}<0$.
- Derive it by delaying the static field (notes) or by $Af + Bg$ plus boundary conditions (slides).
- Cosine: $\beta = \omega/v_p$, $\lambda = 2\pi/\beta$, $v_p = \lambda f$, $\mathbf{S}\propto\cos^2$, outward. Snapshot ↔ record by world lines; distance $d$ means delay $d/v$.

Concept pages: [[concepts/current-sheet-radiation]] · [[concepts/plane-waves]] · [[concepts/intrinsic-impedance]] · [[concepts/poynting-vector]] · [[concepts/boundary-conditions]] · [[concepts/displacement-current]] · [[concepts/wave-equation]].

> [!exam] On exams
> **SP18 Exam 2 #5 is this lecture** (sheet on $y = 0$, piecewise-linear $J_s(t)$: $\mathbf{H}$ on both sides, then a snapshot) — method and variants on [[concepts/current-sheet-radiation]]; **#1(vii)** ($\omega$, $f$, $\lambda$ from a phase change) and **#4** (a moved pulse) on [[concepts/plane-waves]]. The key is not reproduced; the worked problem runs every step.

> [!tip] Practice this lecture
> [[practice/19-radiation-from-current-sheets|12 practice problems]] — 5 easy, 3 medium, 4 hard — each with a folded hint and a worked solution. Start with [[practice/19-radiation-from-current-sheets#191-which-one-is-a-plane-wave|19.1 Which one is a plane wave]]; the [[practice/index|practice hub]] has the whole bank by difficulty and by topic.

### Sources for this page
Kudeki notes, Lecture 19: plane TEM waves, Examples 1–4 (numbers checked), the delayed-static route. Shao, Lecture 19 slides: boundary-condition derivation (slides 2–12), sinusoidal sheet, parameter table, Poynting vector (13–16), examples (11, 17–21; unsolved 11(c), 17, 18–21 solved here). This site's own: $v_\perp/c$, the any-orientation recipe, the traps, the $\mathbf{J}_s\cdot\mathbf{E}$ bookkeeping, the transmission-line picture, all figures. Slips in the course material: see [[0-toolkit/04-errata-in-the-course-materials|errata]]; also, the notes write $\eta_0 = 120\pi$ as an equality (0.07 % high).
