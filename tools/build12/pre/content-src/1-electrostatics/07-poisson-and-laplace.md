---
title: "Lecture 7 — Poisson's and Laplace's equations"
description: "Substituting E = −∇V into Gauss's law gives one scalar equation for the potential, ∇²V = −ρ/ε, which becomes Laplace's equation ∇²V = 0 where there is no charge. Solve it in one dimension by integrating twice and matching boundary values; the general solution is a superposition of point-charge potentials, and the Helmholtz theorem follows."
tags: [lecture, electrostatics, exam-1]
lecture: 7
---

*Lecture 7 · course notes §7 · slides "Boundary Conditions; Poisson's and Laplace's Equation" (second half) · prev: [[1-electrostatics/06-circulation-and-boundary-conditions|Lecture 6]] · next: [[1-electrostatics/08-conductors-dielectrics-and-polarization|Lecture 8]] · practice: [[practice/07-poisson-and-laplace|12 problems]]*

> [!abstract] In one breath
> $\mathbf{E} = -\nabla V$ solves $\nabla\times\mathbf{E} = 0$ once and for all; putting it into $\nabla\cdot\mathbf{D} = \rho$ leaves one **scalar** equation: **Poisson's equation** $\nabla^2V = -\rho/\epsilon$, or **Laplace's equation** $\nabla^2V = 0$ where there is no charge. In 1-D: integrate twice, fix two constants from boundary values — the workhorse of capacitance. The general solution is the superposition of point-charge potentials, which also proves Lecture 4's Helmholtz theorem.

## 1. From Gauss's law to Poisson's equation

Take $\nabla\cdot\mathbf{D} = \rho$ with $\mathbf{D} = \epsilon\mathbf{E}$ and $\mathbf{E} = -\nabla V$:

$$
\nabla\cdot(\epsilon\,\nabla V) = -\rho \quad\xrightarrow{\ \epsilon\ \text{constant}\ }\quad \epsilon\,\nabla\cdot\nabla V = -\rho .
$$

> [!key] Poisson's and Laplace's equations (homogeneous medium: $\epsilon$ independent of position)
> $$
> \nabla^2V = -\frac{\rho}{\epsilon},\qquad\qquad \nabla^2V = 0\ \ (\rho = 0),
> $$
> with the **Laplacian** $\nabla^2V \equiv \nabla\cdot\nabla V = \dfrac{\partial^2V}{\partial x^2}+\dfrac{\partial^2V}{\partial y^2}+\dfrac{\partial^2V}{\partial z^2}$ (Cartesian; other forms on [[0-toolkit/02-vector-calculus-cheatsheet|the cheat sheet]]). Poisson's equation *is* Gauss's law for the potential. In vacuum $\epsilon = \epsilon_0$.

Both conditions matter. "Static" (or quasi-static) allows $\mathbf{E} = -\nabla V$. "$\epsilon$ constant" lets $\epsilon$ out of the divergence; where permittivity varies, or across two dielectrics, $\nabla^2V = -\rho/\epsilon$ is false — use $\nabla\cdot(\epsilon\nabla V) = -\rho$ ([[1-electrostatics/09-static-fields-in-dielectric-media|Lecture 9]]). *Piecewise* homogeneous (two layers): Laplace in each layer, stitched by Lecture 6's boundary conditions.

> [!intuition] What the Laplacian measures
> $\nabla^2V$ at a point $\propto$ (average of $V$ over a small sphere around it) − (value at the point). So Laplace's equation says: **in a charge-free region, $V$ equals the average of $V$ around it** — no bumps, no dips; extremes lie on the boundary (why static fields alone cannot hold a charge in stable equilibrium). Positive charge makes $V$ curve *downward* ($\nabla^2V<0$: dome, $V$ above its local average); negative charge, upward (bowl). A peak or pit can occur only at charge, and curvature alone does not make one: the pn junction below has $V''<0$ throughout its positive slab while $V$ rises to a plateau.

With $V$ specified on the boundary the solution is **unique**: any function satisfying the equation and boundary values is *the* answer — guessing is legitimate. The equation is **linear**: solutions superpose.

## 2. Solving Laplace's equation in one dimension

When $V$ depends on one coordinate, the PDE becomes an ODE integrated twice:

| symmetry | Laplace's equation | general solution | used for |
|---|---|---|---|
| planar, $V(z)$ | $\dfrac{d^2V}{dz^2} = 0$ | $V = Az + B$ | parallel plates |
| cylindrical, $V(r)$ | $\dfrac{1}{r}\dfrac{d}{dr}\Big(r\dfrac{dV}{dr}\Big) = 0$ | $V = A\ln r + B$ | coaxial cable |
| spherical, $V(r)$ | $\dfrac{1}{r^2}\dfrac{d}{dr}\Big(r^2\dfrac{dV}{dr}\Big) = 0$ | $V = \dfrac{A}{r} + B$ | concentric spheres |

> [!recipe] Laplace between conductors
> 1. **Symmetry:** the single coordinate $V$ depends on (infinite plates: $z$; long coax: $r$).
> 2. **Integrate twice** (table above): $V$ with two constants.
> 3. **Boundary values:** each conductor's potential fixes a constant (conductors are equipotentials — [[1-electrostatics/08-conductors-dielectrics-and-polarization|Lecture 8]]).
> 4. $\mathbf{E} = -\nabla V$, then $\mathbf{D} = \epsilon\mathbf{E}$.
> 5. **Surface charges** $\rho_s = \hat{n}\cdot\mathbf{D}$, $\hat{n}$ out of the conductor into the field region (zero field inside).
>
> The chain $V\to\mathbf{E}\to\mathbf{D}\to\rho_s$ is the "given $V$" route to capacitance in [[1-electrostatics/10-capacitance-and-conductance|Lecture 10]].

<!-- fig:laplace-plates -->

> [!example] Example — parallel plates
> Infinite conducting plates $d = 2$ m apart in $z$; $z=0$ grounded, $z=d$ at $-3$ V. $V = V(z)$, $V''(z) = 0$ between (vacuum, no charge): $V = Az + B$. $V(0) = 0$ gives $B = 0$; $V(2) = -3$ gives $A = -\tfrac32$ V/m.
> $$
> V(z) = -\tfrac32 z\ \text{V},\qquad \mathbf{E} = -\nabla V = -\hat{z}\frac{dV}{dz} = +\tfrac32\,\hat{z}\ \text{V/m}\quad(0<z<2\ \text{m}).
> $$
> Uniform, from the 0 V plate toward the $-3$ V plate (high to low). In symbols, $V = V_0z/d$ and $\mathbf{E} = -(V_0/d)\hat{z}$ for a top plate at $V_0$.
>
> *Plate charges.* Outside, the field is zero (equal and opposite sheets cancel). Bottom plate, $\hat{n} = +\hat{z}$ into the gap: $\rho_s(0) = \hat{z}\cdot\epsilon_0\mathbf{E} = +\tfrac32\epsilon_0 \approx 1.3\times10^{-11}$ C/m². Top plate, $\hat{n} = -\hat{z}$: $\rho_s(d) = -\hat{z}\cdot\epsilon_0\mathbf{E} = -\tfrac32\epsilon_0$ C/m². Equal and opposite — so the sheets' fields also cancel *inside each metal plate*: zero field inside a conductor, an equipotential. Lecture 8 makes this a principle.

> [!example] Example — reading a potential difference off a surface charge
> Two copper blocks face each other across a 3 m gap in $x$; facing surfaces carry $\rho_s = +2$ C/m² (left, at $x=0$, $V=0$) and $-2$ C/m² (right). Find the right block's potential $V_p$.
>
> Inside copper $\mathbf{D} = 0$. At $x=0$, $\hat{n} = \hat{x}$ out of the left block: $\hat{x}\cdot(\mathbf{D}_{\text{gap}} - 0) = 2$, so $E_x = 2/\epsilon_0$ V/m, uniform. Drop across the gap $E_xd = 6/\epsilon_0$ V; $\mathbf{E}$ points high to low, so the right block is *lower*: $V_p = -6/\epsilon_0 \approx -6.8\times10^{11}$ V. (Absurd — 2 C/m² is enormous; real capacitors carry µC/m². The method is the point: $\mathbf{D}$ jump ⇒ $E$ ⇒ $\lvert\Delta V\rvert = Ed$ ⇒ sign from the direction of $\mathbf{E}$.)

## 3. Poisson's equation where there is charge

Inside a charged region the integrations pick up $\rho$. Canonical case: the pn junction of [[1-electrostatics/03-gauss-law-at-work#4-superposition-of-the-building-blocks|Lecture 3]], $-\rho_1$ on $-W_1<x<0$, $+\rho_2$ on $0<x<W_2$, $\rho_1W_1 = \rho_2W_2$ (neutral), with field

$$
E_x = \begin{cases}-\dfrac{\rho_1(x+W_1)}{\epsilon_0}, & -W_1<x<0\\[8pt] \dfrac{\rho_2(x-W_2)}{\epsilon_0}, & 0<x<W_2\end{cases}
\qquad(\text{zero outside}).
$$

<!-- fig:pn-potential -->

> [!example] Example — the built-in potential of a junction
> $V'' = -\rho(x)/\epsilon_0$. Once: $V' = -E_x$; again, with constants so that $V_1 = V(-W_1)$ and $V_2 = V(W_2)$ are the plateaus,
> $$
> V(x) = \begin{cases}\dfrac{\rho_1(x+W_1)^2}{2\epsilon_0} + V_1, & -W_1<x<0\\[8pt] -\dfrac{\rho_2(x-W_2)^2}{2\epsilon_0} + V_2, & 0<x<W_2 .\end{cases}
> $$
> The branches must agree at $x=0$:
> $$
> \frac{\rho_1W_1^2}{2\epsilon_0} + V_1 = -\frac{\rho_2W_2^2}{2\epsilon_0} + V_2
> \quad\Longrightarrow\quad
> V_{21}\equiv V_2 - V_1 = \frac{\rho_1W_1^2 + \rho_2W_2^2}{2\epsilon_0} = \frac{\rho_2W_2\,(W_1+W_2)}{2\epsilon_0} .
> $$
> (Last step: neutrality.) The positive side is at higher potential, consistent with $\mathbf{E}$ along $-\hat{x}$. $V(0) = 0$ makes the plateaus $V_1 = -\rho_1W_1^2/2\epsilon_0$ and $V_2 = +\rho_2W_2^2/2\epsilon_0$. Curvature: $V'' = +\rho_1/\epsilon_0>0$ in the negative slab (bowl), $V'' = -\rho_2/\epsilon_0<0$ in the positive slab (dome). Solved for the widths, $W_1+W_2 = \sqrt{2\epsilon_0V_{21}\,(\rho_1+\rho_2)/(\rho_1\rho_2)}$ — ECE 440's depletion-width formula; [[1-electrostatics/10-capacitance-and-conductance#7-a-nonlinear-capacitor-the-diode-junction|Lecture 10]] makes it a capacitance.

> [!trap] Where Laplace's equation may and may not be used
> - Only where $\rho = 0$ *inside* the region. Charge on the *bounding* conductors enters through boundary values; a charged sheet mid-gap splits the problem into two Laplace regions joined by a $\mathbf{D}$-jump ([[1-electrostatics/09-static-fields-in-dielectric-media|Lecture 9]]).
> - Only where $\epsilon$ is constant. Two layers ⇒ two Laplace problems plus matching.
> - The inverse use is as common on exams: $\rho = \epsilon\nabla\cdot\mathbf{E} = -\epsilon\nabla^2V$. Zero curl does not mean zero charge.

## 4. The general solution: superposition of point charges

For finite charge with $V\to0$ at infinity, the answer is Lecture 5's:

> [!key] General solution of Poisson's equation
> $$
> V(\mathbf{r}) = \int\frac{\rho(\mathbf{r}')}{4\pi\epsilon_0\,\lvert\mathbf{r}-\mathbf{r}'\rvert}\,d^3\mathbf{r}',\qquad d^3\mathbf{r}' = dx'\,dy'\,dz',
> $$
> over the region where $\rho\neq0$; $\mathbf{r}$ field point, $\mathbf{r}'$ source point.

Why, in ECE 210 terms: Poisson's equation is a **linear, shift-invariant** system, input $\rho$, output $V$. Its **impulse response** (to $\rho = \delta(\mathbf{r})$, a unit point charge at the origin) is the point-charge potential $1/(4\pi\epsilon_0\lvert\mathbf{r}\rvert)$; shifted to $\mathbf{r}'$, $1/(4\pi\epsilon_0\lvert\mathbf{r}-\mathbf{r}'\rvert)$ — the **Green's function**. Any $\rho$ is a superposition of impulses, $\rho(\mathbf{r}) = \int\rho(\mathbf{r}')\,\delta(\mathbf{r}-\mathbf{r}')\,d^3\mathbf{r}'$ (sifting), so by linearity $V$ is the same superposition of shifted responses — the formula above. For infinite distributions the integral diverges; a finite reference ("$V(0)=0$") renormalizes it.

## 5. Helmholtz's theorem, finally proved

Lecture 4 claimed a field vanishing at infinity is fixed by its divergence and curl; the general solution proves it. Split any such field as

$$
\mathbf{F} = \underbrace{-\nabla V}_{\text{curl-free}} + \underbrace{\nabla\times\mathbf{A}}_{\text{divergence-free}},
$$

Divergence and curl of both sides give $\nabla^2V = -\nabla\cdot\mathbf{F}$ and (gauge $\nabla\cdot\mathbf{A} = 0$) $\nabla^2\mathbf{A} = -\nabla\times\mathbf{F}$ — two Poisson equations, with $\nabla\cdot\mathbf{F}$ and $\nabla\times\mathbf{F}$ as $\rho/\epsilon_0$:

$$
V(\mathbf{r}) = \int\frac{\nabla'\cdot\mathbf{F}(\mathbf{r}')}{4\pi\lvert\mathbf{r}-\mathbf{r}'\rvert}d^3\mathbf{r}',\qquad
\mathbf{A}(\mathbf{r}) = \int\frac{\nabla'\times\mathbf{F}(\mathbf{r}')}{4\pi\lvert\mathbf{r}-\mathbf{r}'\rvert}d^3\mathbf{r}' .
$$

Divergence and curl are a field's complete "sources". Static $\mathbf{E}$: no curl part, $V$ is the Coulomb integral. Unit 2's magnetic field: no divergence part; $\mathbf{A}$ — the [[concepts/vector-potential|vector potential]] of [[2-magnetostatics/13-current-sheets-solenoids-and-the-vector-potential|Lecture 13]] — carries everything. ($V$ is fixed up to a constant, $\mathbf{A}$ up to a gradient; this **gauge freedom** never changes $\mathbf{F}$.)

## 6. Summary

- $\nabla^2V = -\rho/\epsilon$ (Poisson), $\nabla^2V = 0$ (Laplace): Gauss's law for the potential, valid where $\epsilon$ is constant.
- 1-D solutions: linear (planar), logarithmic (cylindrical), $1/r$ (spherical); two constants from two boundary values.
- Chain: $V\to\mathbf{E}=-\nabla V\to\mathbf{D}\to\rho_s = \hat{n}\cdot\mathbf{D}$ on conductors.
- With charge present: integrate $V'' = -\rho/\epsilon_0$ twice, match $V$ at interfaces (pn junction: $V_{21} = \rho_2W_2(W_1+W_2)/2\epsilon_0$).
- General solution = Coulomb superposition; Helmholtz follows.

Concept page: [[concepts/poissons-equation]].

> [!exam] On Exam 1
> Mostly *backwards*: $\rho = \epsilon_0\nabla\cdot\mathbf{E}$ from a field (FA26 1(c)), or $\rho = -\epsilon_0\nabla^2V$ from a potential. Forwards — integrate twice, constants from plate potentials — starts Lecture 9's layered dielectrics, Lecture 10's capacitances, and HW3 #1 (vacuum diode, $V\propto x^{4/3}$). Know the three 1-D solutions cold; deriving $V = A\ln r + B$ under time pressure is where minutes go to die.

> [!tip] Practice this lecture
> [[practice/07-poisson-and-laplace|12 practice problems]] — 5 easy, 3 medium, 4 hard — each with a folded hint and a worked solution. Start with [[practice/07-poisson-and-laplace#71-two-plates-two-potentials|7.1 Two plates, two potentials]]; the [[practice/index|practice hub]] has the whole bank by difficulty and by topic.

### Sources for this page
Kudeki notes, Lecture 7 (Poisson and Laplace; Examples 1–4, "Notice" on zero field in conductors; general solution as LSI impulse response / Green's function; Helmholtz and gauge). Shao, Lectures 6–7 slides (Laplacian; "just Gauss's law in terms of potentials"; "$\epsilon$ = const" and "static" conditions; parallel plates with $\mathbf{E}\to\mathbf{D}\to\rho_s$; layered-dielectric sketch). Slips in the course material (including a Lecture 10 slide's "$V(z) = V_0x/d$"): see [[0-toolkit/04-errata-in-the-course-materials|errata]].
