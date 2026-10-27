---
title: "Boundary conditions at an interface"
description: "Normal D jumps by free surface charge ρs, tangential E and normal B are continuous, tangential H jumps by surface current Js (n̂ from medium 2 into 1)."
tags: [concept, electrostatics, magnetostatics, exam-1]
aliases: ["jump conditions", "interface conditions", "normal and tangential components"]
---

> [!key] The four conditions ($\hat{n}$ points from medium 2 into medium 1)
> $$
> \hat{n}\cdot(\mathbf{D}_1-\mathbf{D}_2) = \rho_s,\qquad
> \hat{n}\times(\mathbf{E}_1-\mathbf{E}_2) = 0,\qquad
> \hat{n}\cdot(\mathbf{B}_1-\mathbf{B}_2) = 0,\qquad
> \hat{n}\times(\mathbf{H}_1-\mathbf{H}_2) = \mathbf{J}_s .
> $$
> Components: $D_{1n} - D_{2n} = \rho_s$ [C/m², **free** charge]; $E_{1t} = E_{2t}$; $B_{1n} = B_{2n}$; $H_{1t} - H_{2t} = J_s$ [A/m]. From the integral laws on a pillbox (divergence laws → normal) and a thin loop (curl laws → tangential), flattened. Time-varying fields too: the flux terms $\partial_t\mathbf{B}$, $\partial_t\mathbf{D}$ vanish with the loop's width. Notes: $\hat{n}\cdot(\mathbf{D}^+-\mathbf{D}^-) = \rho_s$, $\hat n$ pointing into "$+$".

**What they do not say.** Nothing about tangential $\mathbf{D}$ or normal $\mathbf{E}$ (both jump at a dielectric interface), normal $\mathbf{H}$ or tangential $\mathbf{B}$. Only *differences*; levels come from elsewhere (symmetry, superposition, a conductor's potential).

**Mnemonic.** In each differential law replace $\nabla\to\hat{n}$, field $\to$ (field$_1$ − field$_2$), $\rho\to\rho_s$, $\mathbf{J}\to\mathbf{J}_s$, $\partial/\partial t\to0$.

**Special cases.**
- *Conductor surface* (field zero inside, $\hat{n}$ out of the metal): $\hat{n}\cdot\mathbf{D} = \rho_s$, $\hat{n}\times\mathbf{E} = 0$: $\mathbf{E}$ leaves normally, its $D_n$ *is* the surface charge ([[1-electrostatics/07-poisson-and-laplace|Lecture 7]], [[1-electrostatics/10-capacitance-and-conductance|Lecture 10]]). With $\mathbf{H} = 0$ inside (course convention): $B_{1n} = 0$, $\hat n\times\mathbf{H}_1 = \mathbf{J}_s$, i.e. $\mathbf{H}_{1t} = \mathbf{J}_s\times\hat n$, *tangent* to the metal ([[3-maxwell-and-waves/16-charge-conservation-displacement-current-and-maxwells-equations|Lecture 16]]).
- *Two perfect dielectrics, no free charge:* $D_{1n} = D_{2n}$, $E_{1t} = E_{2t}$, so $E_{2n} = (\epsilon_1/\epsilon_2)E_{1n}$; lines refract, $\tan\theta_1/\tan\theta_2 = \epsilon_1/\epsilon_2$ ([[1-electrostatics/09-static-fields-in-dielectric-media|Lecture 9]]). Bound charge there: $\rho_{sb} = P_{2n} - P_{1n} = \epsilon_0(E_{1n}-E_{2n})$; in general $\hat{n}\cdot(\mathbf{P}_1-\mathbf{P}_2) = -\rho_{sb}$.
- *Two magnetic media, no free surface current:* $B_{1n} = B_{2n}$, $H_{1t} = H_{2t}$, so $\mu_1H_{1n} = \mu_2H_{2n}$, $B_{2t} = (\mu_2/\mu_1)B_{1t}$, $\tan\theta_1/\tan\theta_2 = \mu_1/\mu_2$ ([[3-maxwell-and-waves/17-magnetization-and-maxwells-equations-in-matter#6-boundary-conditions-in-magnetic-media|Lecture 17]]); from iron into air lines leave almost normally. The bound current $\mathbf{J}_{sM} = \hat n\times(\mathbf{M}_1-\mathbf{M}_2)$ carries the jump of tangential $\mathbf{B}$: $\hat n\times(\mathbf{B}_1-\mathbf{B}_2)/\mu_0 = \mathbf{J}_s+\mathbf{J}_{sM}$ ([[problems/fields-across-a-magnetic-interface]]).
- *Planar problems:* a sheet $\rho_s$ steps $D_n$ by $\rho_s$ crossed along $\hat{n}$; tangential components pass (also $D_t$, if vacuum both sides). A current sheet steps tangential $\mathbf{H}$ by $J_s$ (the $\pm\tfrac12\mathbf{J}_s\times\hat n$ of [[2-magnetostatics/13-current-sheets-solenoids-and-the-vector-potential|Lecture 13]]); $B_n$ passes.

**Examples.** $\mathbf{D} = 0$ for $x<0$, sheets $+2$ at $x=0$ and $-2$ C/m² at $x=5$ m ⇒ $\mathbf{D} = 2\hat{x}$ between, $0$ outside. $\epsilon_1 = \epsilon_0$ over $\epsilon_2 = 2\epsilon_0$, $\rho_s = 3$ C/m², $\mathbf{D}_2 = 3\hat{x}+2\hat{y}$ ($\hat{y}$ normal) ⇒ $\mathbf{D}_1 = \tfrac32\hat{x} + 5\hat{y}$: $D_t$ times $\epsilon_1/\epsilon_2$, $D_n$ plus $\rho_s$.

> [!trap]
> - Draw $\hat{n}$ at every interface first; it flips between a slab's faces.
> - $\rho_s$ is free charge; bound charge sits inside $\mathbf{P}$, hence $\mathbf{D}$.
> - A stray $\epsilon_0$ in a jump condition: $\mathbf{E}$ written where $\mathbf{D}$ belongs.
> - No *differential* laws at an interface: fields jump there.

Slips in the course material (missing minus in the $\mathbf{P}$ condition, $D_1-D_2=\rho$): [[0-toolkit/04-errata-in-the-course-materials|errata]].

**Where it appears.** [[1-electrostatics/06-circulation-and-boundary-conditions|Lecture 6]] (derived), [[1-electrostatics/08-conductors-dielectrics-and-polarization|Lecture 8]] (conductors), [[problems/fields-across-a-dielectric-interface]], [[problems/two-layer-coaxial-capacitor]], [[3-maxwell-and-waves/17-magnetization-and-maxwells-equations-in-matter|Lecture 17]]; later, wave reflection (Unit 3).

**Practice.** [[practice/topics#boundary-conditions-and-refraction|Boundary conditions and refraction]] (35 problems) — for example [[practice/06-circulation-and-boundary-conditions#61-what-is-always-continuous|6.1 What is always continuous]] (easy), [[practice/06-circulation-and-boundary-conditions#67-a-charged-tilted-interface|6.7 A charged tilted interface]] (medium), [[practice/06-circulation-and-boundary-conditions#69-two-tilted-charged-planes|6.9 Two tilted charged planes]] (hard).

Related: [[concepts/gauss-law]] · [[concepts/amperes-law]] · [[concepts/electric-flux-density]] · [[concepts/magnetic-field]] · [[concepts/conductors]] · [[concepts/permittivity]].
