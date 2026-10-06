---
title: "Magnetization M and magnetization current"
description: "M is the magnetic dipole moment per unit volume of a material, in A/m. Where it changes or ends it leaves a bound current — J_M = ∇×M in the volume, J_sM = M × n̂ on a surface — and H = B/μ₀ − M absorbs that current, so that Ampère's law counts free current only."
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
> $\mathbf{m} = I\mathbf{A}$ [A·m²] is the moment of one atomic current loop — an orbiting or spinning electron — with $\mathbf{A}$ normal to the loop by the right-hand rule; $N$ is the number of such moments per unit volume; $\hat n$ is the **outward** normal of the magnetized body. Ampère's law counts all current, $\nabla\times(\mathbf{B}/\mu_0) = \mathbf{J}_f+\partial\mathbf{P}/\partial t+\nabla\times\mathbf{M}+\epsilon_0\partial\mathbf{E}/\partial t$; moving $\nabla\times\mathbf{M}$ to the left gives $\nabla\times\mathbf{H} = \mathbf{J}_f+\partial\mathbf{D}/\partial t$. The surface current $\mathbf{M}\times\hat n$ is this site's addition (the course notes and slides write only the volume term); it is the twin of the bound surface charge $\rho_{sb} = \mathbf{P}\cdot\hat n$.

**Physics.** Electrons orbiting nuclei and spinning are tiny current loops, each with a moment of the order of a Bohr magneton, $\mu_B = 9.27\times10^{-24}$ A·m². A field exerts a torque $\mathbf{m}\times\mathbf{B}$ on each, turning it toward $\mathbf{B}$ against thermal jostling, and the net moment per unit volume is $\mathbf{M}$. Inside a *uniformly* magnetized body, neighbouring loops carry opposite currents on every shared edge and cancel; only the boundary keeps an uncancelled current, $\mathbf{M}\times\hat n$ per unit length. A long rod magnetized along its axis is therefore a solenoid with $nI$ replaced by $M$: $\mathbf{B}\approx\mu_0\mathbf{M}$ inside, if there is no free current. Where $\mathbf{M}$ varies, the shared edges stop cancelling and a volume current $\nabla\times\mathbf{M}$ is left. The course notes reach the same term from charge conservation: bound charge obeys the continuity equation, so whatever bound current exists beyond the polarization current $\partial\mathbf{P}/\partial t$ is divergence-free — hence a curl. Bound currents are real currents and make real fields; they are just currents you did not drive and cannot switch off. Unlike the bound charge of a dielectric, whose field *opposes* $\mathbf{E}$, the magnetization current's field *reinforces* $\mathbf{B}$ inside a para- or ferromagnet.

**Linear media.** $\mathbf{M} = \chi_m\mathbf{H}$ with $\mathbf{H}$ the total local field, so $\mathbf{B} = \mu\mathbf{H}$ and $\mathbf{M} = (\mu_r-1)\mathbf{H} = \mathbf{B}/\mu_0-\mathbf{H}$ ([[concepts/permeability]]). In practice: get $\mathbf{H}$ from the free currents, $\mathbf{B} = \mu\mathbf{H}$, and $\mathbf{M}$ last, if asked; the magnetization currents then serve as a check, since with the free currents in the vacuum formulas they must reproduce $\mathbf{B}$.

**Examples.**
- *Slab between two current sheets* (slide example): $\mu_r = 100$, sheets $\mp0.1\hat y$ A/m above and below. $\mathbf{H} = 0.1\hat x$ A/m, $\mathbf{M} = 9.9\hat x$ A/m; the faces carry $\mathbf{M}\times\hat n = \mp9.9\hat y$ A/m, the same sense as the free sheets, and free plus bound, 10 A/m, gives $B = \mu_0\cdot10$ A/m $= 100\mu_0H$.
- *Permanent magnet:* $\mu_0M\approx1.3$ T means $M\approx1.0\times10^{6}$ A/m — the surface current of a winding of 1000 turns per metre carrying 1000 A.
- *Iron at saturation:* $N\approx8.5\times10^{28}$ atoms/m³ with about $2.2\,\mu_B$ each gives $M\approx1.7\times10^{6}$ A/m, $\mu_0M\approx2.2$ T.
- *Graded magnetization:* $\mathbf{M} = M_0(x/d)\hat z$ in a slab leaves a uniform volume current $\nabla\times\mathbf{M} = -(M_0/d)\hat y$.
- *Interface* ([[problems/fields-across-a-magnetic-interface]]): $\mu_r = 2$ over $\mu_r = 6$ with $\mathbf{H}_1 = 4\hat x-3\hat y-9\hat z$ A/m gives $\mathbf{M}_1 = (4,-3,-9)$ and $\mathbf{M}_2 = (20,-15,-15)$ A/m; the interface carries $\hat n\times(\mathbf{M}_1-\mathbf{M}_2) = -12\hat x-16\hat y$ A/m.

> [!trap]
> - $\mathbf{M} = \mu_0\chi_m\mathbf{H}$ comes out in tesla; it is $\mathbf{M} = \chi_m\mathbf{H}$, because $\mathbf{M}$ and $\mathbf{H}$ share the unit A/m.
> - $\mathbf{M} = \mathbf{B}/\mu_0-\mathbf{H}$, not $\mathbf{B}/\mu_0$, and not $\mathbf{B}/\mu-\mathbf{H}$, which is identically zero.
> - $\mathbf{J}_M = +\nabla\times\mathbf{M}$ has no minus sign (contrast $\rho_b = -\nabla\cdot\mathbf{P}$); at an interface $\mathbf{J}_{sM} = \hat n\times(\mathbf{M}_1-\mathbf{M}_2)$, again with no minus (contrast $\rho_{sb} = -\hat n\cdot(\mathbf{P}_1-\mathbf{P}_2)$).
> - Each face uses the outward normal of *its own* body: at an interface the two faces have opposite normals, and adding $\mathbf{M}_2\times\hat n$ and $\mathbf{M}_1\times(-\hat n)$ gives $\hat n\times(\mathbf{M}_1-\mathbf{M}_2)$.
> - $\mathbf{M}$ responds to the total local $\mathbf{H}$; "$\mathbf{M} = \chi_m\mathbf{H}_{\text{applied}}$" is right only where the material does not change $\mathbf{H}$ (a long rod along the field, a slab with $\mathbf{H}$ along its faces).

**Where it appears.** [[3-maxwell-and-waves/17-magnetization-and-maxwells-equations-in-matter|Lecture 17]] (defined, derived, and the solenoid-with-core model), [[problems/fields-across-a-magnetic-interface]] (the interface current with signs). Each atomic $\mathbf{m}$ is the current-loop dipole of [[2-magnetostatics/13-current-sheets-solenoids-and-the-vector-potential|Lecture 13]].

Its electric twin is [[concepts/polarization]], with four differences worth memorizing: no $\mu_0$ in $\mathbf{M} = \chi_m\mathbf{H}$; no minus sign in $\nabla\times\mathbf{M}$; $\mathbf{H}$ subtracts $\mathbf{M}$ where $\mathbf{D}$ adds $\mathbf{P}$; and $\chi_m$ can be negative.

**Practice.** [[practice/topics#magnetization-and-magnetic-media|Magnetization and magnetic media]] (11 problems) — for example [[practice/17-magnetization-and-maxwell-in-matter#172-four-rods-in-a-solenoid|17.2 Four rods in a solenoid]] (easy), [[practice/17-magnetization-and-maxwell-in-matter#176-graded-magnetization-in-a-slab|17.6 Graded magnetization in a slab]] (medium), [[practice/17-magnetization-and-maxwell-in-matter#179-electret-and-magnet-twins|17.9 Electret and magnet twins]] (hard).

Related: [[concepts/permeability]] · [[concepts/polarization]] · [[concepts/magnetic-field]] · [[concepts/maxwells-equations]] · [[concepts/boundary-conditions]].
