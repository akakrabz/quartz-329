---
title: "Lecture 4 — Divergence and curl: Maxwell's equations at a point"
description: "Divergence and curl, the divergence and Stokes theorems, conservative fields, static E curl-free, and the differential Maxwell equations — a map of the lecture; the content lives on the topic pages."
tags: [lecture, electrostatics, exam-1]
lecture: 4
---

*Lecture 4 · course notes §4 · slides "Divergence and curl, Maxwell's equations in differential form" · prev: [[1-electrostatics/03-gauss-law-at-work|Lecture 3]] · next: [[1-electrostatics/05-curl-free-fields-and-the-electrostatic-potential|Lecture 5]] · practice: [[practice/04-divergence-and-curl|12 problems]]*

> [!abstract] In one breath
> Apply Gauss's law to a vanishingly small box and divide by its volume: the **divergence** of $\mathbf{D}$ equals the charge density *at that point*, $\nabla\cdot\mathbf{D} = \rho$. The same move on a tiny loop turns a circulation $\oint\mathbf{E}\cdot d\mathbf{l}$ into the **curl**. Divergence = "flux per unit volume" (sources); curl = "circulation per unit area" (whirlpools). The divergence and Stokes' theorems switch between integral and differential laws — and static electric fields have zero curl, which makes voltage possible (Lecture 5).

## 1. From the fundamental theorem of calculus to Stokes

One idea: chop a region into tiny pieces, add a local quantity, interior contributions cancel, only the boundary survives. 1-D FTC → gradient theorem $\int_a^b\nabla f\cdot d\mathbf{l} = f(b)-f(a)$ (so a gradient field is curl-free) → Stokes (surface) → divergence theorem (volume). $\nabla$ dotted gives divergence, crossed gives curl.

→ Full treatment: [[concepts/divergence-theorem|Divergence theorem]] · [[concepts/stokes-theorem|Stokes' theorem]]
## 2. Divergence: flux per unit volume

Gauss's law on a tiny box gives $\nabla\cdot\mathbf{D} = \partial_xD_x+\partial_yD_y+\partial_zD_z = \rho$; "variation along the flow". Examples: $\mathbf{D} = 5x\hat{x}+12\hat{y}$ → $\nabla\cdot\mathbf{D} = 5$ C/m³ (a faucet of strength 5); differentiating the pn-junction field returns $\mp\rho_{1,2}/\epsilon_0$. Also $\nabla\cdot\mathbf{B} = 0$. Tiling boxes gives the divergence theorem.

→ Full treatment: [[concepts/divergence|Divergence]] · [[concepts/divergence-theorem|Divergence theorem]]
## 3. Curl: circulation per unit area

$(\nabla\times\mathbf{v})\cdot\hat{n} = \lim\oint\mathbf{v}\cdot d\mathbf{l}/\Delta S$, the determinant formula, the paddlewheel, "variation across the flow". Example: $\mathbf{v} = -3y\hat{x}+2x\hat{y}$ → $\nabla\times\mathbf{v} = 5\hat{z}$ (a whirlpool of strength 5). Determinant sign trap. Tiling loops gives Stokes' theorem.

→ Full treatment: [[concepts/curl|Curl]] · [[concepts/stokes-theorem|Stokes' theorem]]
## 4. The two pictures, side by side

The same arrow plots answer "source-like?" and "whirlpool-like?" oppositely; practise calling them without computing.

→ Full treatment: [[concepts/divergence|Divergence]] (panels) · [[concepts/curl|Curl]]
## 5. Conservative fields

Four equivalent statements: curl-free ($\nabla\times\mathbf{v} = 0$) ⇔ zero circulation ($\oint_C\mathbf{v}\cdot d\mathbf{l} = 0$) ⇔ path-independent ⇔ $\mathbf{v} = -\nabla f$. The minus sign makes $f$ the voltage.

→ Full treatment: [[concepts/conservative-field|Conservative fields]]
## 6. Static electric fields are curl-free

Every radial field $g(r)\,\mathbf{r}$ has zero curl, so by superposition every electrostatic field does (the notes also check the line field). The laws of electrostatics, $\nabla\cdot\mathbf{D} = \rho$, $\nabla\times\mathbf{E} = 0$, are complete by Helmholtz's theorem.

→ Full treatment: [[concepts/conservative-field|Conservative fields]] · [[concepts/helmholtz-theorem|Helmholtz theorem]]
## 7. The differential form of Maxwell's equations

Each integral law becomes local by Stokes (Faraday, Ampère–Maxwell) or the divergence theorem (both Gauss laws); EMF and MMF; partial, not total, time derivatives.

### A free consequence: charge is conserved
The divergence of Ampère–Maxwell gives $\nabla\cdot\mathbf{J} = -\partial\rho/\partial t$, the continuity equation; vector identities $\nabla\cdot(\nabla\times\mathbf{A}) = 0$, $\nabla\times\nabla f = 0$.

→ Full treatment: [[concepts/maxwells-equations|Maxwell's equations]] · [[concepts/continuity-equation|Continuity equation]] · [[concepts/curl|Curl]] (identities)
## 8. Summary

- Divergence = flux per unit volume (scalar, "along the flow"); $\nabla\cdot\mathbf{D} = \rho$, $\nabla\cdot\mathbf{B} = 0$.
- Curl = circulation per unit area (vector, "across the flow"); Faraday and Ampère are curl equations.
- Divergence and Stokes' theorems: local ↔ integral, by "interior contributions cancel".
- Static $\mathbf{E}$ is curl-free ⇒ conservative ⇒ a potential exists (Lecture 5).
- Continuity, $\nabla\cdot\mathbf{J} = -\partial\rho/\partial t$, is contained in Maxwell's equations.

> [!exam] On Exam 1
> FA26 problem 1 is this lecture plus Lecture 5: $\nabla\times\mathbf{E}$ of a polynomial field (zero), the potential, $\rho = \epsilon_0\nabla\cdot\mathbf{E}$, a line integral by path independence — [[problems/curl-potential-and-charge-from-a-field]]. Exam notes: [[concepts/curl]] · [[concepts/divergence]] · [[concepts/conservative-field]].

> [!tip] Practice this lecture
> [[practice/04-divergence-and-curl|12 practice problems]] — 5 easy, 3 medium, 4 hard — each with a folded hint and a worked solution. Start with [[practice/04-divergence-and-curl#41-faucet-or-whirlpool|4.1 Faucet or whirlpool]]; the [[practice/index|practice hub]] has the whole bank by difficulty and by topic.

### Sources for this page
Kudeki notes, Lecture 4 (Gauss on a small cube → divergence; Examples 1–4; Helmholtz; curl-free Coulomb and line fields). Shao, Lecture 4 slides (FTC → gradient theorem → Stokes ladder; whirlpool/faucet; paddlewheel; true/false panels; pn junction; continuity from Ampère). Slips in the course material: see [[0-toolkit/04-errata-in-the-course-materials|errata]].
