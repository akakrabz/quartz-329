---
title: "Lecture 5 — Curl-free fields and the electrostatic potential"
description: "Potential as work per unit charge, E = −∇V, exact differentials, path independence, V from E two ways, V from charge — a map of the lecture; the content lives on the topic pages."
tags: [lecture, electrostatics, exam-1]
lecture: 5
---

*Lecture 5 · course notes §5 · slides "Potential Functions for Static Fields" · prev: [[1-electrostatics/04-divergence-and-curl|Lecture 4]] · next: [[1-electrostatics/06-circulation-and-boundary-conditions|Lecture 6]] · practice: [[practice/05-electrostatic-potential|12 problems]]*

> [!abstract] In one breath
> Because $\nabla\times\mathbf{E} = 0$ (Lecture 4), a static field is the **gradient of a scalar**, $\mathbf{E} = -\nabla V$, and $V$ is the familiar **voltage** — work per unit charge to move a test charge between two points, independent of route. $V$ to $\mathbf{E}$: a derivative; $\mathbf{E}$ to $V$: a line integral along any convenient path; charge to $V$: scalar superposition. Poisson's equation, conductors as equipotentials and capacitance are all easier in $V$ than in $\mathbf{E}$.

## 1. Why a potential: energy per unit charge

$dU = -q\,\mathbf{E}\cdot d\mathbf{l}$; divide by $q$: $V(b)-V(a) = -\int_a^b\mathbf{E}\cdot d\mathbf{l}$ is the work per unit charge against the field, $\int_a^b\mathbf{E}\cdot d\mathbf{l} = V(a)-V(b)$ the voltage drop. Field work becomes kinetic energy or heat; a battery pushes charge against the field.

→ Full treatment: [[concepts/electrostatic-potential|Electrostatic potential V]]
## 2. From V to E: the gradient

Matching $dV = -\mathbf{E}\cdot d\mathbf{l}$ with the total differential gives $\mathbf{E} = -\nabla V$: downhill, perpendicular to equipotentials, $\lvert\mathbf{E}\rvert$ = volts per metre ("Mount Electron"). Example: $V = x^2-6y$ → $\mathbf{E} = -2x\hat{x}+6\hat{y}$ V/m. Cylindrical and spherical gradients carry $1/r$, $1/(r\sin\theta)$.

→ Full treatment: [[concepts/electrostatic-potential|Electrostatic potential V]]
## 3. Why V exists at all: exact differentials

$\nabla\times\nabla V = 0$ always; conversely, if $\nabla\times\mathbf{E} = 0$ then $\mathbf{E}\cdot d\mathbf{l}$ is an exact differential $-dV$. Two tiny fields: $y\hat{x}+x\hat{y}$ gives $d(xy)$, $V = -xy$; $y\hat{x}-x\hat{y}$ has no $V$ (curl $-2\hat{z}$). The constant is the ground; trap: $\nabla\cdot\nabla V$ is the Laplacian, not zero.

→ Full treatment: [[concepts/conservative-field|Conservative fields]]
## 4. Path independence

For a curl-free field the $-dV$'s along any route sum to $V(a)-V(b)$. Notes example: $\mathbf{E} = y\hat{x}\pm x\hat{y}$ from $(0,0)$ to $(1,1)$ along two staircases — $+$: both give 1; $-$: $+1$ vs $-1$, the difference 2 being the flux of the curl (Stokes). What a voltmeter measures.

→ Full treatment: [[concepts/conservative-field|Conservative fields]] · [[concepts/stokes-theorem|Stokes' theorem]]
## 5. From E to V: two recipes

Check the curl; then spot the exact differential or integrate along an axis-parallel staircase; fix $C$; verify with $-\nabla V$. Example: $\mathbf{E} = 2x\hat{x}+3z\hat{y}+3(y+1)\hat{z}$, $V(0)=0$ → $V = -x^2-3(y+1)z$ both ways. Three ways to lose the sign.

→ Full treatment: [[concepts/electrostatic-potential|Electrostatic potential V]]
## 6. From charge to V: the point charge and superposition

Integrate inward from infinity: $V = \dfrac{Q}{4\pi\epsilon_0r}$; superposition is a scalar sum; $U = qV$. Example: the hydrogen atom — $27.2$ V at the Bohr radius, $-27.2$ eV, half of it the $-13.6$ eV ground state. Infinite lines and sheets need a finite reference (logarithms for a line).

→ Full treatment: [[concepts/electrostatic-potential|Electrostatic potential V]]
## 7. Summary

- $V(b) - V(a) = -\int_a^b\mathbf{E}\cdot d\mathbf{l}$: work per unit charge, path-independent because $\nabla\times\mathbf{E}=0$.
- $\mathbf{E} = -\nabla V$: downhill, perpendicular to equipotentials, "volts per metre".
- Existence of $V$ ⇔ $\mathbf{E}\cdot d\mathbf{l}$ exact ⇔ curl-free ⇔ conservative.
- $V$ from $\mathbf{E}$: check curl → exact differential or staircase path → fix the constant → verify with $-\nabla V$.
- $V$ from charge: $Q/(4\pi\epsilon_0r)$ and scalar superposition; $U = qV$.
- The reference point is yours to choose; only differences matter.

> [!exam] On Exam 1
> FA26 1(b) $V$ from a polynomial field with $V(0)=0$; 1(d) $\int_A^B\mathbf{E}\cdot d\mathbf{l} = V(A)-V(B)$ without a path; 2(c) $V(b)$ outside a slab with $V(0)=0$. Worked in [[problems/curl-potential-and-charge-from-a-field]] and [[problems/charged-slab-with-a-power-law-profile]]. Exam notes: [[concepts/electrostatic-potential]] · [[concepts/conservative-field]].

> [!tip] Practice this lecture
> [[practice/05-electrostatic-potential|12 practice problems]] — 5 easy, 3 medium, 4 hard — each with a folded hint and a worked solution. Start with [[practice/05-electrostatic-potential#51-uniform-field-between-two-points|5.1 Uniform field between two points]]; the [[practice/index|practice hub]] has the whole bank by difficulty and by topic.

### Sources for this page
Kudeki notes, Lecture 5 (gradient, $\nabla\times\nabla V = 0$; exact/inexact differentials, $\pm$ example; path integral; Examples 1–3, 5, 6; voltmeter; Bohr factoid). Shao, Lecture 5 slides (work against the field; Mount Electron; equipotential spacing; two-path example; point-charge potential, $dr<0$ warning; $V$ from $\mathbf{E}$ two ways; curvilinear gradients). Slips in the course material: see [[0-toolkit/04-errata-in-the-course-materials|errata]].
