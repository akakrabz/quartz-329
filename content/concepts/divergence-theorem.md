---
title: "Divergence theorem"
description: "Flux out of a closed surface equals the volume integral of the divergence inside — the bridge between the integral and differential forms of Gauss's law, and one rung of the ladder from the fundamental theorem of calculus to Stokes."
tags: [concept, toolkit, exam-1]
aliases: ["Gauss's theorem", "Gauss–Ostrogradsky theorem", "fundamental theorem of calculus", "gradient theorem"]
---

> [!key] Divergence theorem
> $$
> \int_V \nabla\cdot\mathbf{F}\,dV = \oint_{S}\mathbf{F}\cdot d\mathbf{S}\qquad (S = \partial V,\ d\mathbf{S}\ \text{outward})
> $$
> Integral ↔ differential Gauss: $\oint\mathbf{D}\cdot d\mathbf{S} = \int_V\nabla\cdot\mathbf{D}\,dV = \int_V\rho\,dV$ for *every* $V$ forces $\nabla\cdot\mathbf{D} = \rho$ pointwise.

**Physics — one idea, four theorems.** *Chop a region into tiny pieces, add a local quantity over them; interior contributions cancel, leaving only the boundary.*

- **1-D**: $\displaystyle\int_a^b \frac{df}{dx}\,dx = f(b)-f(a)$.
- **Along a curve** (gradient theorem): $\displaystyle\int_a^b \nabla f\cdot d\mathbf{l} = f(b) - f(a)$, where $\nabla f = \hat{x}\dfrac{\partial f}{\partial x}+\hat{y}\dfrac{\partial f}{\partial y}+\hat{z}\dfrac{\partial f}{\partial z}$ is the gradient (steepest increase; $df = \nabla f\cdot d\mathbf{l}$). Only the endpoints matter, so $\oint_C\nabla f\cdot d\mathbf{l} = 0$ around any *closed* loop: a gradient field is **conservative**, or **curl-free** ([[concepts/conservative-field|Conservative (curl-free) fields and the potential]]).
- **Over a surface**: [[concepts/stokes-theorem|Stokes' theorem]].
- **Through a volume**: the divergence theorem. Tile $V$ with tiny boxes. A shared face counts as "out" of each neighbour with opposite signs and cancels; only the outer boundary survives. Adding "flux per unit volume × volume" over all boxes therefore leaves only the outer surface — and each box's flux per unit volume is the *definition* of [[concepts/divergence|divergence]].

**What it is for.**
- Converts Gauss's law between forms (above). Same for $\oint\mathbf{B}\cdot d\mathbf{S} = 0$ ⟺ $\nabla\cdot\mathbf{B} = 0$.
- Interprets divergence as *flux per unit volume*.
- Gives the continuity equation its integral form: $\oint_S\mathbf{J}\cdot d\mathbf{S} = -\dfrac{d}{dt}\int_V\rho\,dV$ — current out = rate of loss of charge inside ([[concepts/continuity-equation|Continuity equation (charge conservation)]]).

> [!tip] Check a divergence by a flux
> For the slab field $E_x = \rho x/\epsilon_0$, a pillbox of caps at $\pm x$ has flux $2\epsilon_0E_xA = 2\rho xA$ = enclosed charge. Differentiating instead: $\epsilon_0\,dE_x/dx = \rho$. Same content, two languages.

> [!trap]
> - $d\mathbf{S}$ outward, always; the theorem needs a *closed* surface.
> - At a surface charge $\mathbf{D}$ is not differentiable: use the integral law (or a δ-function), not $\nabla\cdot\mathbf{D} = \rho$ across the sheet ([[concepts/boundary-conditions|Boundary conditions at an interface]]).

> [!exam] On exams
> Convert freely between $\oint\mathbf{D}\cdot d\mathbf{S} = Q_{\text{enc}}$ and $\nabla\cdot\mathbf{D} = \rho$: differentiate a given field for $\rho$, integrate a given $\rho$ for the flux.

**Where it appears.** [[1-electrostatics/04-divergence-and-curl#1-from-the-fundamental-theorem-of-calculus-to-stokes|Lecture 4 §1–2]] (the ladder; the theorem), [[1-electrostatics/04-divergence-and-curl#4-the-two-pictures-side-by-side|Lecture 4 §4]] (divergence and curl pictures side by side), [[1-electrostatics/04-divergence-and-curl#7-the-differential-form-of-maxwells-equations|Lecture 4 §7]] (both divergence equations), [[3-maxwell-and-waves/16-charge-conservation-displacement-current-and-maxwells-equations|Lecture 16]] (continuity). Its curl-side twin is [[concepts/stokes-theorem|Stokes' theorem]].

**Related.** [[concepts/divergence|Divergence]] · [[concepts/gauss-law|Gauss's law]] · [[concepts/flux|Flux]] · [[concepts/stokes-theorem|Stokes' theorem]] · [[concepts/differential-elements|Differential elements dl, dS, dV]].

**Practice.** [[practice/topics#divergence-curl-and-the-integral-theorems|Divergence, curl and the integral theorems]] (21 problems) — for example [[practice/04-divergence-and-curl#41-faucet-or-whirlpool|4.1 Faucet or whirlpool]] (easy), [[practice/04-divergence-and-curl#46-three-fields-in-curved-coordinates|4.6 Three fields in curved coordinates]] (medium), [[practice/04-divergence-and-curl#49-electrostatic-or-not|4.9 Electrostatic or not]] (hard).
