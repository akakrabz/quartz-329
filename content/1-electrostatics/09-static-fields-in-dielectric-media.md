---
title: "Lecture 9 — Static fields in dielectric media"
description: "The working rules for dielectric problems (D from free charge, E = D/ε, V by integration, P last), refraction of field lines, layered and graded media, and a dielectric-coated sphere; the full treatment is on the topic pages linked from each section."
tags: [lecture, electrostatics, exam-1]
lecture: 9
---

*Lecture 9 · course notes §9 · slides "Dielectrics" (examples) · prev: [[1-electrostatics/08-conductors-dielectrics-and-polarization|Lecture 8]] · next: [[1-electrostatics/10-capacitance-and-conductance|Lecture 10]] · practice: [[practice/09-static-fields-in-dielectric-media|12 problems]]*

> [!abstract] In one breath
> Every dielectric problem is a short chain: **free** charge fixes $\mathbf{D}$ (Gauss's law, continuity of normal $\mathbf{D}$), each region's permittivity gives $\mathbf{E} = \mathbf{D}/\epsilon$, a line integral gives $V$, and $\mathbf{P} = \mathbf{D}-\epsilon_0\mathbf{E}$ comes last if asked. Laplace's equation holds only where $\epsilon$ is constant: layered media are solved layer by layer and stitched with boundary conditions; graded media need Gauss's law itself.

## 1. The rules

Five things you may assume ($\mathbf{D} = \epsilon\mathbf{E}$ per region; $D_n$ and $E_t$ continuous between dielectrics; $\hat{n}\cdot\mathbf{D} = \rho_s$ at a conductor with $\hat{n}$ into the dielectric; Gauss counts free charge; $\mathbf{P} = \mathbf{D}-\epsilon_0\mathbf{E}$) and the planar chain $D\to E\to V\to P$. Example: a slab in $18\hat{x}$ V/m with $3\hat{x}$ inside — $\mathbf{D} = 18\epsilon_0\hat{x}$ everywhere, $\epsilon_r = 6$, $\chi_e = 5$, $\mathbf{P} = 15\epsilon_0\hat{x}$, faces $\pm15\epsilon_0$ C/m².

→ Full treatment: [[concepts/static-fields-in-dielectrics|Static fields in dielectrics]]

## 2. Refraction of field lines at an interface

$E_{2t} = E_{1t}$ and $\epsilon_2E_{2n} = \epsilon_1E_{1n}$ give $\tan\theta_1/\tan\theta_2 = \epsilon_1/\epsilon_2$: lines tilt toward the surface entering the higher-$\epsilon$ side; $\mathbf{D}$ bends the same way with the roles swapped; the interface bound charge is $\rho_{sb} = P_{2n}-P_{1n} = \epsilon_0(E_{1n}-E_{2n})$. FA26 problem 3, worked in [[problems/fields-across-a-dielectric-interface]].

→ Full treatment: [[concepts/boundary-conditions|Boundary conditions at an interface]]

## 3. Laplace's equation, layer by layer

Laplace only inside a homogeneous region; where $\epsilon$ jumps, solve each layer and join with $V$ and $D_n$ continuous — or take $\mathbf{D}$ from the free sheets first. Examples: two layers ($\epsilon_0$, $2\epsilon_0$) between plates carrying $\mp2\epsilon_0$ C/m², $V(2) = 3$ V both ways (HW4 #1, #3); a free sheet between grounded plates, the "tent" $V_0 = (\rho_s/\epsilon_0)\,d_1d_2/d$, plate shares $-\rho_sd_2/d$ and $-\rho_sd_1/d$, HW4 #2's $V_0 = 36/7$ V.

→ Full treatment: [[concepts/static-fields-in-dielectrics|Static fields in dielectrics]]

## 4. When ε varies continuously: Gauss's law directly

$\nabla\cdot\mathbf{D} = 0$ makes $D_z$ constant; $E_z = D_z/\epsilon(z)$, then integrate. Example: $\epsilon(z) = 4\epsilon_0/(4-z)$ over 2 m with $2\epsilon_0$ C/m² on the bottom plate — $E_z = 2(1-z/4)$ V/m, $V(2) = -3$ V, uniform $\rho_b = -\epsilon_0/2$ C/m³ with no free charge inside.

→ Full treatment: [[concepts/static-fields-in-dielectrics|Static fields in dielectrics]]

## 5. Spherical symmetry: a charged sphere with a dielectric coat

HW3 #7: metal sphere $Q$, shell $\epsilon$ for $a<r<b$ — $\mathbf{D} = Q\hat{r}/4\pi r^2$ everywhere outside the metal, $\mathbf{E}$ reduced by $\epsilon_r$ in the shell, $V(0) = \dfrac{Q}{4\pi}\Big(\dfrac1{\epsilon_0b}+\dfrac1{\epsilon a}-\dfrac1{\epsilon b}\Big)$, bound charge $\mp(1-1/\epsilon_r)Q$ on the two surfaces, $\rho_b = 0$. Concept check: with $\mathbf{D}$ inward, the outer conductor is the higher potential whatever $\epsilon$.

→ Full treatment: [[concepts/static-fields-in-dielectrics|Static fields in dielectrics]]

## 6. Summary

- $\mathbf{D}$ from free charge (Gauss, $D_n$ continuous); $\mathbf{E} = \mathbf{D}/\epsilon$ per region; $V = -\int\mathbf{E}\cdot d\mathbf{l}$ summed over regions; $\mathbf{P} = \mathbf{D}-\epsilon_0\mathbf{E}$ last.
- Interfaces: $E_t$ continuous, $D_n$ continuous (no free charge) ⇒ $\tan\theta_1/\tan\theta_2 = \epsilon_1/\epsilon_2$.
- Laplace/Poisson only inside a homogeneous region; layered ⇒ piecewise plus matching ($V$, $D_n$); graded ⇒ $\nabla\cdot\mathbf{D} = 0$ directly ($D_z$, $rD_r$ or $r^2D_r$ constant).
- Bound charge: $\rho_{sb} = \mathbf{P}\cdot\hat{n}$ on faces, $\rho_b = -\nabla\cdot\mathbf{P}$ (graded $\epsilon$, or free charge inside); total zero.

Concept pages: [[concepts/static-fields-in-dielectrics]] · [[concepts/boundary-conditions]] · [[concepts/permittivity]] · [[concepts/polarization]].

> [!exam] On Exam 1
> FA26 problems 3 and 4 are both this lecture: 3 is §2 verbatim ($\mathbf{E}_2$, then $\mathbf{D}_{1,2}$, then $\mathbf{P}_{1,2}$); 4(a)–(b) is the planar chain in a coax. Most common error: an $\epsilon$ inside $\mathbf{D}$. Exam notes: [[concepts/boundary-conditions]], [[concepts/static-fields-in-dielectrics]]; worked in [[problems/fields-across-a-dielectric-interface]], [[problems/two-layer-coaxial-capacitor]].

> [!tip] Practice this lecture
> [[practice/09-static-fields-in-dielectric-media|12 practice problems]] — 5 easy, 3 medium, 4 hard — each with a folded hint and a worked solution. Start with [[practice/09-static-fields-in-dielectric-media#91-three-layers-between-charged-plates|9.1 Three layers between charged plates]]; the [[practice/index|practice hub]] has the whole bank by difficulty and by topic.

### Sources for this page
Kudeki notes, Lecture 9 (rules; homogeneous vs inhomogeneous; Examples 1–4: slab, two layers, sheet between grounded plates with the quasi-static remark, graded $\epsilon(z)$). Shao, Lecture 9 slides (slab; partially filled plates both ways; spherical-shell challenge). FA26 HW3 #7, HW4 #1–#3. Slips in the course material: see [[0-toolkit/04-errata-in-the-course-materials|errata]].
