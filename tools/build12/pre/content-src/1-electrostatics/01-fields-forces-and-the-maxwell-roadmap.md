---
title: "Lecture 1 — Fields, forces, and the Maxwell roadmap"
description: "What a field is, how E and B are defined through the force on a charge, the four Maxwell equations as the course roadmap, and the two new tools of the course: dl and dS."
tags: [lecture, electrostatics, exam-1]
lecture: 1
---

*Lecture 1 · course notes §1 · slides "Introduction" · assumes MATH 241 vectors and PHYS 212 · next: [[1-electrostatics/02-coulombs-law-superposition-and-gauss|Lecture 2]]*

> [!abstract] In one breath
> Two **vector fields**, $\mathbf{E}(\mathbf{r},t)$ and $\mathbf{B}(\mathbf{r},t)$, defined by the force on a test charge, describe how charges push on charges. Maxwell's four equations say how charges and currents *create* them; the course is those equations — static, then time-varying, then waves on cables. Today: definitions, roadmap, and the vectors we integrate along ($d\mathbf{l}$) and through ($d\mathbf{S}$).

## 1. Why fields at all?

A **field** — a quantity defined at every point $(x,y,z)$ and time $t$ — makes action "at a distance" tractable. A scalar field assigns a number to each point (temperature, elevation, potential $V$); a vector field assigns a vector (wind velocity, $\mathbf{E}$, $\mathbf{B}$).

$\mathbf{E}$ and $\mathbf{B}$ are defined *operationally* by the force on a charge $q$ moving with velocity $\mathbf{v}$:

> [!key] Lorentz force — the definition of E and B
> $$
> \mathbf{F} = q\left(\mathbf{E} + \mathbf{v}\times\mathbf{B}\right)
> $$
> - $\mathbf{E}$ is **force per unit stationary charge** ($\mathbf{v}=0$): units N/C = **V/m**.
> - $\mathbf{B}$ is defined by the *extra* force on a *moving* charge, $\mathbf{F}_M = q\,\mathbf{v}\times\mathbf{B}$. It is perpendicular to $\mathbf{v}$ (and $\mathbf{B}$), so it does no work; a charge moving *along* $\mathbf{B}$ feels none. Units: **T** (tesla) = Wb/m².
>
> Newton's second law: $m\,d\mathbf{v}/dt = q(\mathbf{E}+\mathbf{v}\times\mathbf{B})$, valid for $|\mathbf{v}|\ll c$.

Two facts that return later:

- **Fields are frame-dependent.** A charge at rest in your frame is a current in mine, so $\mathbf{E}$ and $\mathbf{B}$ mix under a change of frame (to first order, $\mathbf{E}' = \mathbf{E} + \mathbf{v}\times\mathbf{B}$). That is *why* their equations are coupled — first seen in [[1-electrostatics/04-divergence-and-curl#7-the-differential-form-of-maxwells-equations|Faraday's law]].
- **Charge comes in both signs, mass doesn't.** Ordinary matter is nearly neutral, so gravity — far weaker per particle — wins macroscopically, and the *net* charge density $\rho$ in a material is usually a tiny imbalance.

Concept pages: [[concepts/lorentz-force]] · [[concepts/electric-field]].

## 2. The roadmap: Maxwell's equations on day one

The course counts the four off as each is derived ("our first Maxwell equation!" in [[1-electrostatics/02-coulombs-law-superposition-and-gauss|Lecture 2]]). Free space, differential form:

| | Divergence equations | Curl equations |
|---|---|---|
| **electric** | $\nabla\cdot\mathbf{E} = \rho/\epsilon_0$ | $\nabla\times\mathbf{E} = -\dfrac{\partial\mathbf{B}}{\partial t}$ |
| **magnetic** | $\nabla\cdot\mathbf{B} = 0$ | $\nabla\times\mathbf{B} = \mu_0\mathbf{J} + \mu_0\epsilon_0\dfrac{\partial\mathbf{E}}{\partial t}$ |

with the constants

$$
\mu_0 \approx 4\pi\times 10^{-7}\ \tfrac{\text{H}}{\text{m}}\ (\text{exact before the 2019 SI redefinition}),\qquad
\epsilon_0 = \frac{1}{\mu_0 c^2}\approx \frac{1}{36\pi\times 10^{9}}\ \tfrac{\text{F}}{\text{m}}\approx 8.854\times10^{-12}\ \tfrac{\text{F}}{\text{m}},\qquad
c = \frac{1}{\sqrt{\mu_0\epsilon_0}}\approx 3\times10^{8}\ \tfrac{\text{m}}{\text{s}}.
$$

> [!intuition] How to read the table (this is the whole course in one paragraph)
> **Left column:** what fields *emanate from* — electric field lines start and end on charge ($\rho$); magnetic field lines never start or end. **Right column:** what makes fields *circulate* — a changing $\mathbf{B}$ curls $\mathbf{E}$ (Faraday: generators, transformers); a current $\mathbf{J}$ or a changing $\mathbf{E}$ curls $\mathbf{B}$ (Ampère–Maxwell: electromagnets, antennas). Sources on the right-hand sides, fields on the left.

Two consequences, derived later:

1. **Statics decouple.** With no time variation both $\partial/\partial t$ terms vanish and the table splits:
   - *Electrostatics* (Lectures 1–11): $\nabla\cdot\mathbf{E}=\rho/\epsilon_0$ and $\nabla\times\mathbf{E}=0$ — a **curl-free** field fixed by charge.
   - *Magnetostatics* ([[2-magnetostatics/12-magnetic-force-biot-savart-and-amperes-law|Lecture 12]], [[2-magnetostatics/13-current-sheets-solenoids-and-the-vector-potential|Lecture 13]]): $\nabla\cdot\mathbf{B}=0$ and $\nabla\times\mathbf{B}=\mu_0\mathbf{J}$ — a **divergence-free** field fixed by current. ([[2-magnetostatics/14-faradays-law-and-induced-emf|Lecture 14]] and [[2-magnetostatics/15-inductance-magnetic-energy-and-the-potentials|Lecture 15]], Faraday's law and inductance, bring $\partial\mathbf{B}/\partial t$ back.)
2. **Waves.** With the time derivatives kept, empty space supports $\mathbf{E},\mathbf{B}\propto\cos\!\big(2\pi f\,(t - z/c)+\phi\big)$ — disturbances travelling at $c$ with wavelength $\lambda = c/f$ (Lecture 18), and the reason the course ends with transmission lines and the Smith chart.

### Quasi-statics: when is a circuit "a circuit"?

A source of period $T$ can be treated *statically* — using the instantaneous $\rho$ and $\mathbf{J}$ — when the field crosses the system before the source changes:

$$
T \gg \frac{L}{c}\quad\Longleftrightarrow\quad L \ll \lambda .
$$

This **quasi-static approximation** is the assumption behind lumped-circuit theory (ECE 210): a circuit is a circuit only while *electrically small*. Shrink $\lambda$ (raise the clock) or grow $L$ (a long cable, a PCB trace at GHz) and delays $L/c$ matter — Lectures 27–38.

> [!tip] A number to carry around
> $c \approx 3\times10^{8}$ m/s $= 300$ m/µs $= 30$ cm/ns. So 1 MHz ↔ 300 m wavelength; 1 GHz ↔ 30 cm; a 3 GHz clock has $\lambda = 10$ cm, which is *not* large compared with a motherboard.

Concept page: [[concepts/maxwells-equations]].

## 3. Units and the source → field bookkeeping

| Quantity | Symbol | Units | Sourced by |
|---|---|---|---|
| electric field | $\mathbf{E}$ | V/m | charge |
| electric flux density | $\mathbf{D}=\epsilon_0\mathbf{E}$ (+$\mathbf{P}$ in matter) | C/m² | charge |
| magnetic field | $\mathbf{H}$ | A/m | current |
| magnetic flux density | $\mathbf{B}=\mu_0\mathbf{H}$ (in vacuum) | T = Wb/m² | current |
| charge densities | point $Q$; line $\rho_l$; surface $\rho_s$; volume $\rho$ | C; C/m; C/m²; C/m³ | — |
| current densities | wire $I$; sheet $\mathbf{J}_s$; volume $\mathbf{J}$ | A; A/m; A/m² | — |

The slide's blue brace: **charges → $\mathbf{E},\mathbf{D}$; currents → $\mathbf{H},\mathbf{B}$.** The densities' "dimension ladder" checks an answer's units. Details: [[concepts/charge-density]], [[0-toolkit/03-units-and-constants]].

## 4. Vector algebra you must be fluent in (review at home)

Assumed by the course. If any line is not automatic, do the exercises on [[0-toolkit/02-vector-calculus-cheatsheet]].

- Cartesian components: $\mathbf{A} = A_x\hat{x} + A_y\hat{y} + A_z\hat{z}$ (the slides also write $\hat{a}_x$ and $\langle A_x, A_y, A_z\rangle$).
- Magnitude $|\mathbf{A}| = \sqrt{A_x^2+A_y^2+A_z^2}$; unit vector $\hat{a} = \mathbf{A}/|\mathbf{A}|$.
- **Separation vector** from point 1 to point 2: $\mathbf{R}_{12} = \mathbf{r}_2 - \mathbf{r}_1$ — *final minus initial*; $\hat{R}_{12}$ points from 1 toward 2. Every Coulomb's-law calculation uses it.
- Dot product: $\mathbf{A}\cdot\mathbf{B} = |\mathbf{A}||\mathbf{B}|\cos\theta = A_xB_x + A_yB_y + A_zB_z$. Projection of $\mathbf{A}$ on $\hat{b}$: $\mathbf{A}\cdot\hat{b}$.
- Cross product: $|\mathbf{A}\times\mathbf{B}| = |\mathbf{A}||\mathbf{B}|\sin\theta$, direction by the right-hand rule, computed by the determinant
  $$
  \mathbf{A}\times\mathbf{B} = \begin{vmatrix}\hat{x}&\hat{y}&\hat{z}\\ A_x&A_y&A_z\\ B_x&B_y&B_z\end{vmatrix},
  \qquad \hat{x}\times\hat{y}=\hat{z},\ \hat{y}\times\hat{z}=\hat{x},\ \hat{z}\times\hat{x}=\hat{y}.
  $$

> [!example] In-class discussion problem
> $\mathbf{A} = 3\hat{x}+2\hat{y}+\hat{z}$, $\mathbf{B} = \hat{x}+\hat{y}-\hat{z}$, $\mathbf{C} = \hat{x}+2\hat{y}+3\hat{z}$. Find $\mathbf{B}\times\mathbf{C}$ and $\mathbf{A}\cdot(\mathbf{B}\times\mathbf{C})$.
>
> Expand along the top row, alternating sign on $\hat{y}$:
> $$
> \mathbf{B}\times\mathbf{C} = \hat{x}(1\cdot3-(-1)\cdot2) - \hat{y}(1\cdot3-(-1)\cdot1) + \hat{z}(1\cdot2-1\cdot1) = 5\hat{x}-4\hat{y}+\hat{z}.
> $$
> Then $\mathbf{A}\cdot(\mathbf{B}\times\mathbf{C}) = 3\cdot5 + 2\cdot(-4) + 1\cdot1 = 8$ — the signed volume of the parallelepiped spanned by the three vectors.

## 5. The two new tools: dl and dS

Integral-form Maxwell equations are line or surface integrals of small vector elements.

<!-- fig:dl-ds-cube -->

**Differential length vector** $d\mathbf{l}$: an infinitesimal step, *always tangent* to the curve; in Cartesian coordinates

$$
d\mathbf{l} = \hat{x}\,dx + \hat{y}\,dy + \hat{z}\,dz .
$$

$\int_{P_1}^{P_2}\mathbf{F}\cdot d\mathbf{l}$ adds up the *tangential* component of $\mathbf{F}$ along the path — the work done by a force field from $P_1$ to $P_2$ (the slides' "walking through a river"). A step perpendicular to the flow costs nothing. This goes into Faraday's law and, in [[concepts/conservative-field|Lecture 5]], defines voltage.

**Differential surface vector** $d\mathbf{S}$: a surface patch as a vector *normal* to it, with magnitude equal to its area. Zoomed in, any patch is flat, so two tangent steps build it:

$$
d\mathbf{S} = d\mathbf{l}_1\times d\mathbf{l}_2 .
$$

> [!trap] The order of the cross product is the orientation
> $d\mathbf{l}_1\times d\mathbf{l}_2$ and $d\mathbf{l}_2\times d\mathbf{l}_1$ are opposite normals. **Closed** surface: always **outward**; open surface: *choose* a normal and stick with it. The six faces of a Cartesian box have
> $$
> d\mathbf{S} = \pm\hat{x}\,dy\,dz,\quad \pm\hat{y}\,dz\,dx,\quad \pm\hat{z}\,dx\,dy ,
> $$
> with the sign fixed by "outward". A wrong sign silently flips a flux — see the [[problems/flux-through-a-plane-from-two-charges|flux-through-a-plane problem]].

$\int_S \mathbf{F}\cdot d\mathbf{S}$ adds up the *normal* component of $\mathbf{F}$ — how much field "pokes through": the **flux**, subject of [[1-electrostatics/03-gauss-law-at-work|Lecture 3]]. Cylindrical and spherical $d\mathbf{l}$, $d\mathbf{S}$, $dV$: [[0-toolkit/01-coordinates-and-differential-elements]].

## 6. Where this goes next

- **Lecture 2**: Coulomb's law, superposition, Gauss's law (first Maxwell equation).
- **Lecture 3**: Gauss's law as a tool (line, sheet, slab); δ-function point charges.
- **Lecture 4**: divergence and curl form.

> [!exam] What Lecture 1 contributes to Exam 1
> Nothing is asked "about Lecture 1" directly, but every problem uses it: vector components, the $\mathbf{R}_{12}$ convention, $d\mathbf{l}$ in a line integral (Exam 1, problem 1d), outward $d\mathbf{S}$ on a Gaussian surface (problems 2 and 4), and units on every answer. Missing units cost more marks than missing physics.

### Sources for this page
Kudeki, *ECE 329 Lecture Notes*, Lecture 1 (big picture; frame-dependence of fields; quasi-statics). Shao, Lecture 1 slides (units table, $d\mathbf{l}$/$d\mathbf{S}$ construction, discussion problem). Rao, *Fundamentals of Electromagnetics for Electrical and Computer Engineering*, ch. 1. Slips in the course material: see [[0-toolkit/04-errata-in-the-course-materials|errata]].
