---
title: "Electric flux density D"
description: "D = ε₀E in vacuum, D = ε₀E + P in matter: the field whose flux counts free charge in coulombs. Gauss's law in matter, ∇·D = ρ_free, and why 'D is the same inside and out' is a slab result, not a law."
tags: [concept, electrostatics, exam-1]
aliases: ["D field", "displacement field", "electric displacement", "Gauss's law in matter", "free charge"]
---

> [!key] The displacement field and Gauss's law for free charge
> $$
> \mathbf{D} \equiv \epsilon_0\mathbf{E} + \mathbf{P}\qquad[\text{C/m}^2],\qquad\qquad \nabla\cdot\mathbf{D} = \rho_f,\qquad \oint_S\mathbf{D}\cdot d\mathbf{S} = Q_{f,\text{enc}} .
> $$
> Gauss's law proper counts *all* charge, $\nabla\cdot(\epsilon_0\mathbf{E}) = \rho_f + \rho_b$; moving $\rho_b = -\nabla\cdot\mathbf{P}$ to the left absorbs the bound charge into $\mathbf{D}$. From here on, unsubscripted $\rho$ means **free** charge — the charges you control. In vacuum $\mathbf{P} = 0$, $\mathbf{D} = \epsilon_0\mathbf{E}$; in a linear dielectric $\mathbf{D} = \epsilon\mathbf{E}$, $\epsilon = \epsilon_0\epsilon_r$. Maxwell called $\mathbf{D}$ the *electric displacement*; the slides say "displacement flux density"; this site says "electric flux density".

**Physics.** In vacuum $\mathbf{D}$ is just $\epsilon_0\mathbf{E}$ and carries no new information. Inside matter the medium polarizes, producing *bound* charge that also sources $\mathbf{E}$ ([[concepts/polarization|Polarization P and bound charge]]). Where the definition comes from: inside an infinite slab polarized normal to its faces, the averaged bound-charge field is $-\mathbf{P}/\epsilon_0$, so $\mathbf{E} = \mathbf{E}_0 - \mathbf{P}/\epsilon_0$ with $\mathbf{E}_0$ the free charges' field. Rearranged, $\epsilon_0\mathbf{E} + \mathbf{P} = \epsilon_0\mathbf{E}_0$: the right side is $\epsilon_0\mathbf{E}$ *before* the dielectric was inserted, the free charges' field alone. $\mathbf{D}$ is built so that its sources are the **free** charge only:
$$
\nabla\cdot\mathbf{D} = \rho_{\text{free}},\qquad \nabla\cdot(\epsilon_0\mathbf{E}) = \rho_{\text{free}}+\rho_{\text{bound}},\qquad \rho_{\text{bound}} = -\nabla\cdot\mathbf{P}.
$$
So a Gauss's-law calculation gives $\mathbf{D}$ from the free charge *regardless of the material*, and then $\mathbf{E} = \mathbf{D}/\epsilon$ region by region ([[concepts/static-fields-in-dielectrics|Static fields in dielectrics]]). That is exactly the structure of the FA26 coax problem (problem 4a–b): one $\mathbf{D}$, two different $\mathbf{E}$'s.

**Boundary behaviour.** The [[concepts/boundary-conditions|boundary conditions]] survive (they came from the integral laws): $\hat{n}\cdot(\mathbf{D}_1-\mathbf{D}_2) = \rho_s$ with **free** $\rho_s$, and $\hat{n}\times(\mathbf{E}_1-\mathbf{E}_2) = 0$. So the normal component of $\mathbf{D}$ is continuous across an interface carrying no free surface charge; the tangential component of $\mathbf{E}$ is continuous. (Not the other way round — FA26 problem 3.) For $\mathbf{P}$ the pillbox gives $\hat{n}\cdot(\mathbf{P}_1-\mathbf{P}_2) = -\rho_{sb}$: bound surface charge is how much normal $\mathbf{P}$ *decreases* from medium 2 into medium 1 (along $\hat{n}$).

**Units check.** $\epsilon_0$ [F/m] × $\mathbf{E}$ [V/m] = C/(V·m)·(V/m) = C/m² ✓.

> [!trap] "D is the same inside and outside" is a slab result, not a law
> - For an infinite slab with the field *normal* to its faces, $\mathbf{D}$ inside equals $\epsilon_0\mathbf{E}_0$ outside because the bound face layers are infinite sheets whose fields cancel outside.
> - With the field *along* the faces, $\mathbf{E}$ is unchanged inside and $\mathbf{D}$ jumps by $\mathbf{P}$ — the tangential-$\mathbf{D}$ jump of Lecture 6.
> - A dielectric *sphere* in a uniform field has a dipole-like fringe field outside and $\mathbf{E}_p = -\mathbf{P}/(3\epsilon_0)$ inside, not $-\mathbf{P}/\epsilon_0$.
> - General: $\nabla\cdot\mathbf{D} = \rho_f$, and normal $\mathbf{D}$ continuous across an interface without free charge. With planar, cylindrical or spherical symmetry that gives $\mathbf{D}$ from free charge alone — which is why those are the problems you get.
> - Writing $\mathbf{D}$ with an $\epsilon$ in it (confusing $\mathbf{D}$ with $\mathbf{E}$) is the most common error in FA26 problems 3 and 4.

> [!exam] On exams
> Start every dielectric problem from $\mathbf{D}$: Gauss's law with the *free* charge, or $D_n$ continuous across a charge-free interface, or $\hat{n}\cdot\mathbf{D} = \rho_s$ at a conductor. Then $\mathbf{E} = \mathbf{D}/\epsilon$ per region, $\mathbf{P} = \mathbf{D}-\epsilon_0\mathbf{E}$ last. Worked in [[problems/two-layer-coaxial-capacitor|Worked problem — Two-layer coaxial capacitor]] and [[problems/fields-across-a-dielectric-interface|Worked problem — Fields across a dielectric interface]].

**Where it appears.** [[1-electrostatics/02-coulombs-law-superposition-and-gauss#5-from-coulomb-to-gauss|Lecture 2 §5]] (introduced), [[1-electrostatics/03-gauss-law-at-work|Lecture 3]] (every Gauss's-law example), [[1-electrostatics/08-conductors-dielectrics-and-polarization#4-the-displacement-field-d-and-gausss-law-in-matter|Lecture 8 §4]] (defined in matter), [[1-electrostatics/09-static-fields-in-dielectric-media|Lecture 9]], [[1-electrostatics/10-capacitance-and-conductance|Lecture 10]] (materials, capacitance), [[problems/two-layer-coaxial-capacitor|Worked problem — Two-layer coaxial capacitor]].

**Related.** [[concepts/gauss-law|Gauss's law]] · [[concepts/electric-field|Electric field E]] · [[concepts/flux|Flux]] · [[concepts/polarization|Polarization P and bound charge]] · [[concepts/permittivity|Permittivity, susceptibility, and D = εE]] · [[concepts/static-fields-in-dielectrics|Static fields in dielectrics]] · [[concepts/boundary-conditions|Boundary conditions at an interface]].

**Practice.** [[practice/topics#fields-in-dielectric-media|Fields in dielectric media]] (16 problems) — for example [[practice/09-static-fields-in-dielectric-media#91-three-layers-between-charged-plates|9.1 Three layers between charged plates]] (easy), [[practice/09-static-fields-in-dielectric-media#96-graded-dielectric-at-fixed-voltage|9.6 Graded dielectric at fixed voltage]] (medium), [[practice/09-static-fields-in-dielectric-media#99-glass-slab-in-an-oblique-field|9.9 Glass slab in an oblique field]] (hard).
