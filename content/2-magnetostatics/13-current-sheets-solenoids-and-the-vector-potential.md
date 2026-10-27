---
title: "Lecture 13 — Current sheets, solenoids, and the vector potential"
description: "Map of Lecture 13 — Ampère's law on the current sheet, the slab and the solenoid, the two static theories side by side, the vector potential and the Coulomb gauge, the current loop as a magnetic dipole; the full treatment is on the linked topic pages."
tags: [lecture, magnetostatics]
lecture: 13
---

*Lecture 13 · course notes §13 · slides "Ampère's Law" · prev: [[2-magnetostatics/12-magnetic-force-biot-savart-and-amperes-law|Lecture 12]] · next: [[2-magnetostatics/14-faradays-law-and-induced-emf|Lecture 14]] · practice: [[practice/13-current-sheets-solenoids-and-vector-potential|12 problems]]*

> [!abstract] In one breath
> As [[1-electrostatics/03-gauss-law-at-work|Lecture 3]] did with Gauss's law and symmetric charges, this lecture uses Ampère's law on symmetric *currents*; every answer is the Unit 1 answer with "normal" replaced by "tangential". A current sheet makes a tangential field $J_s/2$ that reverses across the sheet and does not fall off; a slab turns the step into a ramp; a solenoid — a sheet rolled into a cylinder — traps a uniform $\mu_0nI$ inside and nothing outside. Second half: because $\nabla\cdot\mathbf{B} = 0$, $\mathbf{B} = \nabla\times\mathbf{A}$; choosing $\nabla\cdot\mathbf{A} = 0$ turns Ampère's law into $\nabla^2\mathbf{A} = -\mu_0\mathbf{J}$, solved by the Coulomb integral with $\rho/\epsilon_0\to\mu_0\mathbf{J}$. A single loop then gives the dipole field shared by bar magnets, compass needles and the Earth.

## 1. The current sheet

Notes Example 1: $\mathbf{J}_s = J_s\hat z$ on $x = 0$. Mirror filaments fix $\mathbf{B} = \hat yB_y(x)$, odd in $x$; a rectangle straddling the sheet gives $2B_yL = \mu_0J_sL$, so $\mathbf{H} = \tfrac12\mathbf{J}_s\times\hat n$ — $\pm J_s/2$, independent of distance, tangential $\mathbf{H}$ jumping by $J_s$.

→ Full treatment: [[concepts/current-sheets-and-slabs|Current sheets and slabs]]
## 2. The current slab

Notes Example 2: $\mathbf{J} = \hat zJ_0$ for $\lvert x\rvert<W/2$. Same rectangle, enclosed current $2xJ_0L$: a ramp $H_y = J_0x$ inside, plateaus $\pm J_0W/2$ outside, continuous at the faces — the charged-slab plot with $D\to H$.

→ Full treatment: [[concepts/current-sheets-and-slabs|Current sheets and slabs]]
## 3. The solenoid

Notes Example 3: $n$ turns/m as a cylindrical sheet $nI\hat\phi$. Rectangle $C_1$ (both legs outside) links zero net current, so the exterior field is uniform, hence zero; $C_2$ (one leg inside) gives $B_z = \mu_0nI$, independent of radius. Finite coil: $\tfrac12nI$ at the ends.

→ Full treatment: [[concepts/solenoids-and-toroids|Solenoids and toroids]]
## 4. Statics, side by side

> [!key] The two static theories (course notes, Lecture 13)
> **Static electric fields** are *curl-free*: $\nabla\times\mathbf{E} = 0$, $\nabla\cdot\mathbf{D} = \rho$, with $\mathbf{D} = \epsilon\mathbf{E}$, $\epsilon = \epsilon_r\epsilon_0$.
> **Static magnetic fields** are *divergence-free*: $\nabla\cdot\mathbf{B} = 0$, $\nabla\times\mathbf{H} = \mathbf{J}$, with $\mathbf{B} = \mu\mathbf{H}$, $\mu = \mu_r\mu_0$ ($\mu_r\ne1$ is explained in [[3-maxwell-and-waves/17-magnetization-and-maxwells-equations-in-matter|Lecture 17]]).
>
> Full translation table: the [[2-magnetostatics/index#the-dictionary-electrostatics--magnetostatics|dictionary]] on the unit page.

A curl-free field is the gradient of a scalar — $V$ in [[1-electrostatics/05-curl-free-fields-and-the-electrostatic-potential|Lecture 5]]. A divergence-free field is the curl of a vector: next section.

## 5. The vector potential

$\nabla\cdot(\nabla\times\mathbf{A}) = 0$ identically, so $\mathbf{B} = \nabla\times\mathbf{A}$ [Wb/m], unique only up to $\nabla\lambda$; the Coulomb gauge $\nabla\cdot\mathbf{A} = 0$ turns $\nabla\times\mathbf{B} = \mu_0\mathbf{J}$ into $\nabla^2\mathbf{A} = -\mu_0\mathbf{J}$, solved by the Coulomb integral with the same Green's function as $V$ (table $V$ vs $\mathbf{A}$ on the topic page). $\mathbf{A}$ as momentum per unit charge.

→ Full treatment: [[concepts/vector-potential|Vector potential]]
## 6. The current loop and the magnetic dipole

Loop of radius $a$: $\mathbf{J} = I\delta(z')\delta(r'-a)\hat\phi'$ makes $\mathbf{A}$ a single $\phi'$ integral; curling it gives elliptic integrals off the axis and, on the axis, $B_z = \mu_0Ia^2/[2(a^2+z^2)^{3/2}]$ — $\mu_0I/2a$ at the centre, $\propto1/\lvert z\rvert^3$ far away: a dipole, $m = I\pi a^2$. Field lines $r = L\sin^2\theta$; coaxial like loops attract.

→ Full treatment: [[concepts/magnetic-dipole|The current loop and the magnetic dipole]]
## 7. Summary

- Sheet: $\mathbf{H} = \tfrac12\mathbf{J}_s\times\hat n$, tangential, $\pm J_s/2$, no distance dependence; tangential $\mathbf{H}$ jumps by $J_s$.
- Slab: ramp $J_0x$ inside, $\pm J_0W/2$ outside, continuous; the charged-slab plot with $D\to H$.
- Solenoid: $\mathbf{B} = \mu_0nI\hat z$ inside, $0$ outside; finite coil: $\tfrac12nI$ at the ends.
- $\nabla\cdot\mathbf{B} = 0\Rightarrow\mathbf{B} = \nabla\times\mathbf{A}$; Coulomb gauge $\nabla\cdot\mathbf{A} = 0$; $\nabla^2\mathbf{A} = -\mu_0\mathbf{J}$; $\mathbf{A} = \int\mu_0\mathbf{J}\,d^3r'/(4\pi\lvert\mathbf{r}-\mathbf{r}'\rvert)$.
- Loop: $B_z = \mu_0Ia^2/[2(a^2+z^2)^{3/2}]$ on the axis; far field $\propto1/r^3$ (dipole); lines $r = L\sin^2\theta$; parallel loops attract.

Topic pages: [[concepts/current-sheets-and-slabs]] · [[concepts/solenoids-and-toroids]] · [[concepts/amperes-law]] · [[concepts/vector-potential]] · [[concepts/magnetic-dipole]] · [[concepts/boundary-conditions]].

> [!exam] On exams
> Sheet, slab and solenoid are the three "find $\mathbf{H}$ by Ampère's law" set pieces; superpositions are the natural exam problem ([[problems/current-slab-and-sheet-by-amperes-law]]; methods on [[concepts/current-sheets-and-slabs]] and [[concepts/solenoids-and-toroids]]). The vector potential is examined lightly ([[concepts/vector-potential]]); the loop's on-axis result might be ([[concepts/magnetic-dipole]]).

> [!tip] Practice this lecture
> [[practice/13-current-sheets-solenoids-and-vector-potential|12 practice problems]] — 5 easy, 3 medium, 4 hard — each with a folded hint and a worked solution. Start with [[practice/13-current-sheets-solenoids-and-vector-potential#131-one-current-sheet-two-points|13.1 One current sheet, two points]]; the [[practice/index|practice hub]] has the whole bank by difficulty and by topic.

### Sources for this page
Kudeki notes, Lecture 13 (Examples 1–3: sheet, slab, solenoid with $C_1$, $C_2$, the exterior caveat and finite coil; statics box; $\nabla\cdot\nabla\times\mathbf{A} = 0$; gauge freedom, Coulomb gauge, "potential momentum"; $\nabla^2\mathbf{A} = -\mu_0\mathbf{J}$; the loop integrals, on-axis and far fields, $r = L\sin^2\theta$, attracting loops). Shao, Lecture 13 slides (MMF ↔ EMF; mirror-strip symmetry and rectangle; $\mathbf{H} = \tfrac12\mathbf{J}_s\times\hat a_n$; slab with its $H_y(x)$ graph; solenoid). The site's own: $m = I\pi a^2$ and the elliptic-integral remark. Slips in the course material: see [[0-toolkit/04-errata-in-the-course-materials|errata]].
