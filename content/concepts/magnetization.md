---
title: "Magnetization M and magnetization current"
description: "M is the magnetic dipole moment per unit volume, in A/m. H = B/μ₀ − M absorbs its bound currents ∇×M and M × n̂, so Ampère's law counts free current only."
tags: [concept, waves]
aliases: ["magnetization current", "bound current", "magnetic dipole moment", "magnetic moment", "H = B/μ₀ − M"]
---

> [!key] Definition
> $$
> \begin{gathered}
> \mathbf{M} = N\mathbf{m}\ \ (\text{magnetic dipole moment per unit volume})\quad[\text{A/m}],\\[4pt]
> \mathbf{J}_M = \nabla\times\mathbf{M},\qquad \mathbf{J}_{sM} = \mathbf{M}\times\hat n,\qquad \mathbf{H}\equiv\frac{\mathbf{B}}{\mu_0}-\mathbf{M}.
> \end{gathered}
> $$
> $\mathbf{m} = I\mathbf{A}$ [A·m²] is one atomic current loop (orbiting or spinning electron), $\mathbf{A}$ normal by the right-hand rule; $N$ per unit volume; $\hat n$ the **outward** normal of the body. Ampère's law counts all current, $\nabla\times(\mathbf{B}/\mu_0) = \mathbf{J}_f+\partial\mathbf{P}/\partial t+\nabla\times\mathbf{M}+\epsilon_0\partial\mathbf{E}/\partial t$; moving $\nabla\times\mathbf{M}$ left gives $\nabla\times\mathbf{H} = \mathbf{J}_f+\partial\mathbf{D}/\partial t$. $\mathbf{J}_{sM}$ is this site's addition (notes and slides: volume term only).

**Physics.** Each moment is about a Bohr magneton, $\mu_B = 9.27\times10^{-24}$ A·m²; the torque $\mathbf{m}\times\mathbf{B}$ aligns it against thermal jostling. In a *uniformly* magnetized body neighbouring loops cancel on shared edges, leaving the boundary current $\mathbf{M}\times\hat n$: a rod magnetized along its axis is a solenoid with $nI\to M$, so $\mathbf{B}\approx\mu_0\mathbf{M}$ inside (no free current). Where $\mathbf{M}$ varies, $\nabla\times\mathbf{M}$ is left. The notes get it from charge conservation: bound current beyond $\partial\mathbf{P}/\partial t$ is divergence-free, hence a curl. Unlike a dielectric's bound charge, which *opposes* $\mathbf{E}$, bound currents *reinforce* $\mathbf{B}$ in para- and ferromagnets.

**Linear media.** $\mathbf{M} = \chi_m\mathbf{H}$, so $\mathbf{B} = \mu\mathbf{H}$ and $\mathbf{M} = (\mu_r-1)\mathbf{H} = \mathbf{B}/\mu_0-\mathbf{H}$ ([[concepts/permeability]]). Get $\mathbf{H}$ from free currents, then $\mathbf{B}$, then $\mathbf{M}$; free plus magnetization currents in the vacuum formulas must give back $\mathbf{B}$.

**Examples.**
- *Slab between current sheets* (slides): $\mu_r = 100$, sheets $\mp0.1\hat y$ A/m above and below ⇒ $\mathbf{H} = 0.1\hat x$, $\mathbf{M} = 9.9\hat x$ A/m; face currents $\mathbf{M}\times\hat n = \mp9.9\hat y$ A/m add to the free sheets; the total, 10 A/m, gives $B = \mu_0\cdot10$ A/m $= 100\mu_0H$.
- *Permanent magnet:* $\mu_0M\approx1.3$ T ⇒ $M\approx1.0\times10^{6}$ A/m (1000 turns/m at 1000 A). *Saturated iron:* $8.5\times10^{28}$ atoms/m³, about $2.2\,\mu_B$ each ⇒ $M\approx1.7\times10^{6}$ A/m, $\mu_0M\approx2.2$ T.
- *Graded:* $\mathbf{M} = M_0(x/d)\hat z$ ⇒ uniform $\nabla\times\mathbf{M} = -(M_0/d)\hat y$.
- *Interface* ([[problems/fields-across-a-magnetic-interface]]): $\mu_r = 2$ over $\mu_r = 6$, $\mathbf{H}_1 = 4\hat x-3\hat y-9\hat z$ A/m ⇒ $\mathbf{M}_1 = (4,-3,-9)$, $\mathbf{M}_2 = (20,-15,-15)$ A/m, $\hat n\times(\mathbf{M}_1-\mathbf{M}_2) = -12\hat x-16\hat y$ A/m.

> [!trap]
> - $\mathbf{M}\neq\mu_0\chi_m\mathbf{H}$ (tesla): $\mathbf{M}$ and $\mathbf{H}$ share A/m.
> - $\mathbf{M} = \mathbf{B}/\mu_0-\mathbf{H}$; not $\mathbf{B}/\mu_0$, nor $\mathbf{B}/\mu-\mathbf{H}$ (identically zero).
> - No minus sign: $\mathbf{J}_M = +\nabla\times\mathbf{M}$ (contrast $\rho_b = -\nabla\cdot\mathbf{P}$); at an interface each face uses its own outward normal, $\mathbf{M}_2\times\hat n+\mathbf{M}_1\times(-\hat n) = \hat n\times(\mathbf{M}_1-\mathbf{M}_2)$ (contrast $\rho_{sb} = -\hat n\cdot(\mathbf{P}_1-\mathbf{P}_2)$).
> - $\mathbf{M}$ follows the total local $\mathbf{H}$; $\chi_m\mathbf{H}_{\text{applied}}$ only where the material leaves $\mathbf{H}$ unchanged (long rod along the field, slab with $\mathbf{H}$ along its faces).

**Where it appears.** [[3-maxwell-and-waves/17-magnetization-and-maxwells-equations-in-matter|Lecture 17]] (defined, derived, cored-solenoid model); $\mathbf{m}$ is the loop dipole of [[2-magnetostatics/13-current-sheets-solenoids-and-the-vector-potential|Lecture 13]]. Electric twin: [[concepts/polarization]]; besides no $\mu_0$ and no minus sign, $\mathbf{H}$ subtracts $\mathbf{M}$ where $\mathbf{D}$ adds $\mathbf{P}$, and $\chi_m$ can be negative.

**Practice.** [[practice/topics#magnetization-and-magnetic-media|Magnetization and magnetic media]] (11 problems) — for example [[practice/17-magnetization-and-maxwell-in-matter#172-four-rods-in-a-solenoid|17.2 Four rods in a solenoid]] (easy), [[practice/17-magnetization-and-maxwell-in-matter#176-graded-magnetization-in-a-slab|17.6 Graded magnetization in a slab]] (medium), [[practice/17-magnetization-and-maxwell-in-matter#179-electret-and-magnet-twins|17.9 Electret and magnet twins]] (hard).

Related: [[concepts/permeability]] · [[concepts/polarization]] · [[concepts/magnetic-field]] · [[concepts/maxwells-equations]] · [[concepts/boundary-conditions]].
