---
title: "Lecture 2 — Coulomb's law, superposition, and the birth of Gauss's law"
description: "Force → field, Coulomb's law, superposition and the 5-step recipe, and Gauss's law derived from Coulomb — a map of the lecture; the content lives on the topic pages."
tags: [lecture, electrostatics, exam-1]
lecture: 2
---

*Lecture 2 · course notes §2 · slides "Lorentz force, Coulomb's law" · prev: [[1-electrostatics/01-fields-forces-and-the-maxwell-roadmap|Lecture 1]] · next: [[1-electrostatics/03-gauss-law-at-work|Lecture 3]] · practice: [[practice/02-coulombs-law-superposition-and-gauss|12 problems]]*

> [!abstract] In one breath
> A stationary charge $Q$ has a radial field falling as $1/r^2$ (Coulomb). Fields of many charges **add** (superposition), so continuous distributions are integrals — the "5-step program". Because the field falls *exactly* as $1/r^2$ while a sphere's area grows *exactly* as $r^2$, the flux of $\epsilon_0\mathbf{E}$ through **any** closed surface equals the charge inside: **Gauss's law**, the first Maxwell equation.

## 1. Force first, then field

$\mathbf{F}_E = q\mathbf{E}$ on a stationary charge, $\mathbf{F}_M = q\mathbf{v}\times\mathbf{B}$ on a moving one. Two slide examples fix the geometry of $\mathbf{v}\times\mathbf{B}$: the **velocity selector** (crossed $\mathbf{E}$, $\mathbf{B}$; only $v_0 = E_0/B_0$ passes straight) and the **mass spectrometer** (circular orbit, $R = mv_0/(qB_0)$). For Ampère later: $I\,d\mathbf{l}\leftrightarrow q\mathbf{v}$, $d\mathbf{F} = I\,d\mathbf{l}\times\mathbf{B}$.

→ Full treatment: [[concepts/lorentz-force|Lorentz force]] · [[concepts/electric-field|Electric field E]]
## 2. Coulomb's law

$\mathbf{F}_2 = \dfrac{Q_1Q_2}{4\pi\epsilon_0R^2}\hat{R}$ with $\hat{R}$ from source 1 to field point 2; dividing out the test charge, $\mathbf{E} = \dfrac{Q}{4\pi\epsilon_0r^2}\hat{r}$. The off-origin form with $(\mathbf{r}-\mathbf{r}')/\lvert\mathbf{r}-\mathbf{r}'\rvert^3$; keep $4\pi\epsilon_0$ explicit (never "$k$"). Drawing fields: arrow plots and field lines (start on +, end on −, density ∝ $\lvert\mathbf{E}\rvert$, never cross except at null points).

→ Full treatment: [[concepts/coulombs-law|Coulomb's law]] · [[concepts/electric-field|Electric field E]] (field lines)
## 3. Superposition

Fields add as vectors. Example: two opposite charges $\pm Q$ at $(0,\pm a/2)$, field on the bisector at $(D,0)$ — $x$-components cancel, $\mathbf{E} = -\dfrac{Qa}{4\pi\epsilon_0(D^2+a^2/4)^{3/2}}\hat{y}$, far away a **dipole** $p = Qa$ falling as $1/D^3$ (twice as strong, and along $\mathbf{p}$, on the axis).

→ Full treatment: [[concepts/superposition|Superposition]]
## 4. Continuous distributions — the 5-step program

$dQ = \rho_l\,dl = \rho_s\,dS = \rho\,dV$; draw, chop, write $d\mathbf{E}$, use symmetry, integrate. Unit vectors leave the integral only if Cartesian or fixed at the field point. Worked example: **finite line charge** $-a<z<a$ → $E_r = \dfrac{\rho_l}{4\pi\epsilon_0r}\dfrac{2a}{\sqrt{a^2+r^2}}$, and $a\to\infty$ gives the **infinite line** $\dfrac{\rho_l}{2\pi\epsilon_0r}\hat{r}$ — $1/r$, not $1/r^2$. Review at home: ring ($dQ = \rho_{l0}a\,d\phi$) and rod ($\mathbf{F} = \dfrac{qQ}{4\pi\epsilon_0a(L+a)}\hat{x}$).

→ Full treatment: [[concepts/five-step-recipe|The 5-step recipe]]
## 5. From Coulomb to Gauss

Flux of $\epsilon_0\mathbf{E}$ through a sphere around $Q$: $\epsilon_0\cdot\dfrac{Q}{4\pi\epsilon_0r^2}\cdot4\pi r^2 = Q$, independent of $r$. Lines never stop (any surface), flux is linear (superposition), name $\mathbf{D} = \epsilon_0\mathbf{E}$: $\oint_S\mathbf{D}\cdot d\mathbf{S} = Q_{\text{enc}}$ for any closed surface — more fundamental than Coulomb, since it survives moving charges.

→ Full treatment: [[concepts/gauss-law|Gauss's law]] · [[concepts/flux|Flux]] · [[concepts/electric-flux-density|Electric flux density D]]
## 6. Summary

| Configuration | $\mathbf{E}$ | falls off as |
|---|---|---|
| point charge $Q$ | $\dfrac{Q}{4\pi\epsilon_0 r^2}\hat{r}$ | $1/r^2$ |
| dipole $p=Qa$, far away | $\dfrac{p}{4\pi\epsilon_0 D^3}$ on the bisector (antiparallel to $\mathbf{p}$); $\dfrac{2p}{4\pi\epsilon_0 D^3}$ on the axis (along $\mathbf{p}$) | $1/D^3$ |
| infinite line $\rho_l$ | $\dfrac{\rho_l}{2\pi\epsilon_0 r}\hat{r}$ | $1/r$ |

- $\hat{R}$ points from source to field point; superpose vectors, not magnitudes.
- Gauss's law: flux of $\mathbf{D}$ out = charge enclosed, for any closed surface.

> [!exam] On Exam 1
> Coulomb integrals are homework; the exam prefers the Gauss shortcut (FA26 problems 2 and 4) and tests the *ideas*: direction of $\hat{R}$, only enclosed charge sets the flux, the $1/r^2$ / $1/r$ / constant pattern. Exam notes: [[concepts/coulombs-law]] · [[concepts/gauss-law]] · [[concepts/superposition]].

> [!tip] Practice this lecture
> [[practice/02-coulombs-law-superposition-and-gauss|12 practice problems]] — 5 easy, 3 medium, 4 hard — each with a folded hint and a worked solution. Start with [[practice/02-coulombs-law-superposition-and-gauss#21-coulomb-force-as-a-vector|2.1 Coulomb force as a vector]]; the [[practice/index|practice hub]] has the whole bank by difficulty and by topic.

### Sources for this page
Kudeki notes, Lecture 2 (Coulomb field; Example 1 field map; the line of charges summed with δ-functions, then by Gauss). Shao, Lecture 2 slides (velocity/mass selector, field-line rules and poll, 5-step program, ring/rod/finite-line examples). Lecture 3 slides §8–10 (Gauss from Coulomb).
