---
title: "Current distributions: J, J_s, I"
description: "Volume current density J (A/m²), surface current density J_s (A/m) and line current I (A), and how δ-functions write the thinner ones as volume densities — the current-side twin of the charge-density hierarchy. Integrate J_s across the flow, not over an area, to get amperes."
tags: [concept, magnetostatics]
aliases: ["current density", "surface current density", "surface current", "line current", "sheet current", "J_s"]
---

> [!key] The three current densities
> | distribution | units | as a volume density $\mathbf{J}$ |
> |---|---|---|
> | volume current $\mathbf{J}$ | A/m² | $\mathbf{J}$ itself: $\sigma\mathbf{E}$ in a conductor, $Nq\mathbf{v}$ in general |
> | surface current $\mathbf{J}_s(y,z)$ on the plane $x = x_0$ | A/m | $\mathbf{J}_s(y,z)\,\delta(x-x_0)$ |
> | line current $I(z)$ along the line $x = x_0$, $y = y_0$ | A | $\hat z\,I(z)\,\delta(x-x_0)\,\delta(y-y_0)$ |
> | point charge $Q$ moving at $\mathbf{v}$ through $\mathbf{r}_0(t)$ | — | $Q\mathbf{v}\,\delta(x-x_0)\delta(y-y_0)\delta(z-z_0)$ (time-varying) |
>
> Each δ carries 1/m, so every row comes out in A/m². The current through a surface $S$ is $I = \int_S\mathbf{J}\cdot d\mathbf{S}$; for a sheet, $I = \int\mathbf{J}_s\cdot\hat m\,dw$ across a line of width $w$ drawn on the sheet, $\hat m$ the in-sheet normal to that line.

**Physics.** $\mathbf{J}$ in Ampère's law is a volume current density [A/m²] — $\sigma\mathbf{E}$ in a conductor, $Nq\mathbf{v}$ in general ([[1-electrostatics/11-lorentz-drude-models-for-conductivity-and-susceptibility|Lecture 11]], [[concepts/conductivity-and-susceptibility-models|Lorentz–Drude models of σ and χe]]). Thinner distributions use δ-functions, exactly as $\rho_s$ and $\rho_l$ did for charge in [[1-electrostatics/03-gauss-law-at-work#5-charge-densities-and-δ-functions|Lecture 3 §5]] ([[concepts/charge-density|Charge densities and δ-functions]]): the δ's put the current where it is and make the units work. $\mathbf{J}_s$ is current per unit **width**, measured across the flow; integrate across the flow, not over an area, to get amperes. The δ-function picture is also why $\nabla\times\mathbf{H} = \mathbf{J}$ is consistent with $\nabla\times\mathbf{B} = 0$ everywhere off a thin wire: the whole curl sits on the wire, as a δ ([[concepts/amperes-law|Ampère's law]]). The same units bookkeeping decides the boundary condition: tangential $\mathbf{H}$ [A/m] jumps by $J_s$ [A/m] across a current sheet ([[concepts/current-sheets-and-slabs|Current sheets and slabs]]), as $D_n$ [C/m²] jumps by $\rho_s$ [C/m²].

**Examples.**

> [!example] Total current on a sheet (course notes, Lecture 12, Example 1)
> $\mathbf{J}_s = \hat z\,y\,\text{rect}(y - \tfrac12)$ A/m on the plane $x = 0$: a strip $0<y<1$ m wide (infinite in $z$) whose current density grows linearly from 0 to 1 A/m across it. Total current, integrating *across* the strip: $I = \displaystyle\int_0^1y\,dy = \tfrac12$ A.

*Site's own.* A long wire of radius $a$ carrying $I$ uniformly has $\mathbf{J} = \hat z\,I/(\pi a^2)$ inside and zero outside; seen from far away it is the line current $\hat zI\,\delta(x)\delta(y)$. A solenoid of $n$ turns/m is, from a little distance, the cylindrical sheet $\mathbf{J}_s = nI\,\hat\phi$ ([[concepts/solenoids-and-toroids|Solenoids and toroids]]); $N$ turns on a plate of width $W$ carrying $I$ make $J_s = NI/W$.

> [!trap]
> - $\mathbf{J}_s$ is A/m, integrated across a *width*; $\int J_s\,dS$ over an area is dimensionally wrong.
> - A line current as a volume density needs *two* δ's, $\delta(x-x_0)\delta(y-y_0)$; a slide dropped one — [[0-toolkit/04-errata-in-the-course-materials|errata page]]. The notes' $\mathbf{J}_s(x,y)$ for a sheet on $x = x_0$ should read $\mathbf{J}_s(y,z)$ (errata).
> - Steady currents are divergence-free ($\nabla\cdot\mathbf{J} = 0$, [[concepts/continuity-equation|Continuity equation (charge conservation)]]): a surface or line current that ends somewhere is piling up charge and is not magnetostatic.

> [!exam] On exams
> "Count the current" items: total $I$ from a given $\mathbf{J}$ or $\mathbf{J}_s$ (integrate across the right dimension), and $I_{\text{enc}}$ for an Amperian loop through a slab or a coax core ($J\cdot$ area, with its sign). Write the δ-function form when asked to express a sheet or wire as a volume density; check the units come out A/m².

**Where it appears.** [[2-magnetostatics/12-magnetic-force-biot-savart-and-amperes-law#5-describing-currents-j-jₛ-i-and-δ-functions|Lecture 12 §5]]; the sheet and slab of [[2-magnetostatics/13-current-sheets-solenoids-and-the-vector-potential|Lecture 13]]; the loop's $\mathbf{J} = I\,\delta(z')\,\delta(r'-a)\,\hat\phi'$ in [[concepts/magnetic-dipole|The current loop and the magnetic dipole]]; the continuity equation of [[3-maxwell-and-waves/16-charge-conservation-displacement-current-and-maxwells-equations|Lecture 16]]; the radiating sheet of [[concepts/current-sheet-radiation|Radiation from a current sheet]].

**Related.** [[concepts/charge-density|Charge densities and δ-functions]] · [[concepts/amperes-law|Ampère's law]] · [[concepts/current-sheets-and-slabs|Current sheets and slabs]] · [[concepts/continuity-equation|Continuity equation (charge conservation)]] · [[concepts/conductivity-and-susceptibility-models|Lorentz–Drude models of σ and χe]].

**Practice.** [[practice/topics#ampères-law-and-current-density|Ampère's law and current density]] (10 problems) — for example [[practice/12-magnetic-force-biot-savart-and-ampere#125-counting-current-in-delta-functions|12.5 Counting current in delta functions]] (easy), [[practice/12-magnetic-force-biot-savart-and-ampere#126-the-centre-of-a-square-loop|12.6 The centre of a square loop]] (medium), [[practice/12-magnetic-force-biot-savart-and-ampere#1211-a-coax-with-unequal-currents|12.11 A coax with unequal currents]] (hard).
