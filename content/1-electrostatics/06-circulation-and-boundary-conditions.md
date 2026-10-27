---
title: "Lecture 6 — Circulation and boundary conditions"
description: "Zero circulation as Kirchhoff's voltage law, where fields jump, the four boundary conditions from the integral laws, the normal vector, and what the conditions do and do not tell you — a map of the lecture; the content lives on the topic pages."
tags: [lecture, electrostatics, exam-1]
lecture: 6
---

*Lecture 6 · course notes §6 · slides "Boundary Conditions; Poisson's and Laplace's Equation" (first half) · prev: [[1-electrostatics/05-curl-free-fields-and-the-electrostatic-potential|Lecture 5]] · next: [[1-electrostatics/07-poisson-and-laplace|Lecture 7]] · practice: [[practice/06-circulation-and-boundary-conditions|12 problems]]*

> [!abstract] In one breath
> Around a closed path a static field's line integral is zero: the **circulation** vanishes — Kirchhoff's voltage law, and by Stokes the same as $\nabla\times\mathbf{E} = 0$. The differential laws assume differentiable fields; at a conductor or dielectric surface fields *jump*. The integral laws still hold for a loop or pillbox straddling the surface, and shrinking it onto the surface turns each Maxwell equation into a **boundary condition**: how much each component may jump. Four rules, one drawing, and a normal vector you must never lose track of.

## 1. Circulation: the loop version of path independence

$\oint_C\mathbf{E}\cdot d\mathbf{l} = 0$ for static fields — KVL, equal to zero curl by Stokes. Notes Example 1: a rectangle $(1,0)$–$(3,4)$ inside a slab field $\hat{x}\rho x/\epsilon_0$ — vertical legs zero, horizontal legs $\pm4\rho/\epsilon_0$ cancel. Curl as local circulation; the laws of electrostatics and their quasi-static validity ($\tau\gg L/c$).

→ Full treatment: [[concepts/conservative-field|Conservative fields]] · [[concepts/electric-field|Electric field E]] (quasi-statics)
## 2. Where fields jump

A sheet's field $\hat{z}\dfrac{\rho_s}{2\epsilon_0}\text{sgn}(z)$ plus a smooth background $\mathbf{E}_0$: tangential components continuous, normal $D_z$ jumps by $\rho_s$ — at any charged surface, flat or curved.

→ Full treatment: [[concepts/boundary-conditions|Boundary conditions]]
## 3. The boundary conditions, from the integral laws

Gauss and $\oint\mathbf{B}\cdot d\mathbf{S}=0$ on a squashed pillbox, Faraday and Ampère on a squashed loop: $\hat{n}\cdot(\mathbf{D}_1-\mathbf{D}_2) = \rho_s$, $\hat{n}\times(\mathbf{E}_1-\mathbf{E}_2) = 0$, $\hat{n}\cdot(\mathbf{B}_1-\mathbf{B}_2) = 0$, $\hat{n}\times(\mathbf{H}_1-\mathbf{H}_2) = \mathbf{J}_s$, with $\hat{n}$ from medium 2 into medium 1, valid for time-varying fields. Mnemonic: $\nabla\to\hat{n}$, field → difference, $\rho\to\rho_s$, $\mathbf{J}\to\mathbf{J}_s$.

→ Full treatment: [[concepts/boundary-conditions|Boundary conditions]]
## 4. The normal vector is half the problem

Draw $\hat{n}$ at every interface first; it flips when you re-choose medium 1. Notes Example 2: vacuum gap between planes at $x=0$ ($\rho_s = 2$) and $x=5$ m → $\mathbf{D} = 2\hat{x}$ C/m² in the gap, $\rho_{s0} = -2$ C/m² by superposition. Example 3: $\mathbf{D} = 3\hat{y}$ on the left, sheets $+2$ and $-6$ → $D_x$ steps $0\to2\to-4$, $D_y = 3$ throughout. Slides' challenge: $\epsilon_0$ over $2\epsilon_0$ with $\rho_s = 3$, $\mathbf{D}_2 = 3\hat{x}+2\hat{y}$ → $\mathbf{D}_1 = \tfrac32\hat{x}+5\hat{y}$ C/m².

→ Full treatment: [[concepts/boundary-conditions|Boundary conditions]]
## 5. What the conditions do and do not tell you

Differences, not levels; $\rho_s$ is free charge; at a conductor $\hat{n}\cdot\mathbf{D} = \rho_s$ and the field leaves normally; between perfect dielectrics $D_n$ and $E_t$ continuous bend the lines. Four ways to go wrong.

→ Full treatment: [[concepts/boundary-conditions|Boundary conditions]] · [[concepts/conductors|Conductors]] · [[concepts/static-fields-in-dielectrics|Static fields in dielectrics]]
## 6. Summary

- $\oint_C\mathbf{E}\cdot d\mathbf{l} = 0$ for static fields: KVL, equivalent to $\nabla\times\mathbf{E} = 0$ by Stokes.
- Fields jump only at surface charges and currents; the squeezed integral laws say by how much.
- $\hat{n}\cdot(\mathbf{D}_1-\mathbf{D}_2) = \rho_s$, $\hat{n}\times(\mathbf{E}_1-\mathbf{E}_2) = 0$, $\hat{n}\cdot(\mathbf{B}_1-\mathbf{B}_2) = 0$, $\hat{n}\times(\mathbf{H}_1-\mathbf{H}_2) = \mathbf{J}_s$, with $\hat{n}$ from 2 into 1.
- Conditions fix jumps, not levels; $\rho_s$ is free charge; $\hat{n}$ is re-chosen at every interface.

> [!exam] On Exam 1
> FA26 problem 3: a dielectric interface — given $\mathbf{E}_1$ and two permittivities, find $\mathbf{E}_2$, $\mathbf{D}$ and $\mathbf{P}$ on both sides ([[problems/fields-across-a-dielectric-interface]]). The two-plane examples are the pattern of HW3 #6 ($\rho = \rho_s\,\delta(y)$). Exam notes: [[concepts/boundary-conditions]] · [[concepts/conservative-field]].

> [!tip] Practice this lecture
> [[practice/06-circulation-and-boundary-conditions|12 practice problems]] — 5 easy, 3 medium, 4 hard — each with a folded hint and a worked solution. Start with [[practice/06-circulation-and-boundary-conditions#61-what-is-always-continuous|6.1 What is always continuous]]; the [[practice/index|practice hub]] has the whole bank by difficulty and by topic.

### Sources for this page
Kudeki notes, Lecture 6 (circulation; Example 1; curl as circulation per area; quasi-static note; sheet plus background; $\pm$ notation; loop/pillbox justification; Examples 2–3). Shao, Lectures 6–7 slides (integral vs differential forms at a boundary; pillbox and loop derivations; "Points INTO medium 1"; two-plane example; challenge question; "Remember this drawing!!" and the memorization rule). Slips in the course material: see [[0-toolkit/04-errata-in-the-course-materials|errata]].
