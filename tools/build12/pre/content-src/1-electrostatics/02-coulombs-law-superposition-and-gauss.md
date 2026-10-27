---
title: "Lecture 2 — Coulomb's law, superposition, and the birth of Gauss's law"
description: "The electric field defined through force; Coulomb's law with the source-to-field-point convention; superposition for point charges and continuous distributions (the 5-step recipe); and why the flux of ε₀E out of any closed surface equals the enclosed charge."
tags: [lecture, electrostatics, exam-1]
lecture: 2
---

*Lecture 2 · course notes §2 · slides "Lorentz force, Coulomb's law" · prev: [[1-electrostatics/01-fields-forces-and-the-maxwell-roadmap|Lecture 1]] · next: [[1-electrostatics/03-gauss-law-at-work|Lecture 3]] · practice: [[practice/02-coulombs-law-superposition-and-gauss|12 problems]]*

> [!abstract] In one breath
> A stationary charge $Q$ has a radial field falling as $1/r^2$ (Coulomb). Fields of many charges **add** (superposition), so continuous distributions are integrals — the "5-step program". Because the field falls *exactly* as $1/r^2$ while a sphere's area grows *exactly* as $r^2$, the flux of $\epsilon_0\mathbf{E}$ through **any** closed surface equals the charge inside: **Gauss's law**, the first Maxwell equation.

## 1. Force first, then field

From Lecture 1: $\mathbf{F}_E = q\mathbf{E}$ on a stationary charge, $\mathbf{F}_M = q\mathbf{v}\times\mathbf{B}$ on a moving one, $\mathbf{F} = q(\mathbf{E}+\mathbf{v}\times\mathbf{B})$ in total. Two applications that fix the geometry of $\mathbf{v}\times\mathbf{B}$:

> [!example] Velocity selector, then mass selector
> **Crossed fields.** Send a charge with $\mathbf{v}=v_0\hat{x}$ through $\mathbf{E}=E_0\hat{z}$ and $\mathbf{B}=-B_0\hat{y}$. Then $\mathbf{v}\times\mathbf{B} = v_0\hat{x}\times(-B_0\hat{y}) = -v_0B_0\hat{z}$, so
> $$
> \mathbf{F} = q\,(E_0 - v_0B_0)\,\hat{z} = 0 \iff v_0 = E_0/B_0 .
> $$
> Faster particles bend one way (magnetic wins), slower ones the other; only $v = E/B$ passes straight through the aperture.
>
> **Uniform field, no E.** With $\mathbf{B}=B_0\hat{z}$ and $\mathbf{v}\perp\mathbf{B}$, $q\mathbf{v}\times\mathbf{B}$ has constant magnitude $qv_0B_0$, always perpendicular to $\mathbf{v}$: uniform circular motion. $mv_0^2/R = qv_0B_0$ gives $R = mv_0/(qB_0)$; heavier ions land farther out — a mass spectrometer.

For later (Ampère): current is charge in motion, so $I\,d\mathbf{l} \leftrightarrow q\mathbf{v}$ and the force on a wire element is $d\mathbf{F} = I\,d\mathbf{l}\times\mathbf{B}$ (units: A·m = (C/s)·m = C·(m/s) ✓).

## 2. Coulomb's law

Coulomb (1785): two small charges at rest feel a force along the line joining them, proportional to the product of the charges and to $1/R^2$, repulsive for like signs.

<!-- fig:coulomb-pair -->

> [!key] Coulomb's law and the Coulomb field
> Force on $Q_2$ due to $Q_1$ (with $\hat{R}$ the unit vector **from 1 to 2** and $R$ their separation):
> $$
> \mathbf{F}_2 = \frac{Q_1 Q_2}{4\pi\epsilon_0 R^2}\,\hat{R},\qquad \mathbf{F}_1 = -\mathbf{F}_2 .
> $$
> Dividing out the test charge, the **field of a point charge $Q$ at the origin** is
> $$
> \mathbf{E}(\mathbf{r}) = \frac{Q}{4\pi\epsilon_0 r^2}\,\hat{r}
> \qquad\text{(units V/m; } \epsilon_0 \approx 8.854\times10^{-12}\ \text{F/m)} .
> $$
> Radial, $1/r^2$, *away* from positive and *toward* negative charge.

The field is the limit $\mathbf{E} = \lim_{q\to 0}\mathbf{F}/q$, so the test charge does not disturb the sources. The course never writes "$k = 9\times10^9$": keep $1/(4\pi\epsilon_0)$ explicit, because $\epsilon_0$ becomes $\epsilon = \epsilon_0\epsilon_r$ inside materials (Lectures 8–9).

> [!trap] Source point vs field point
> **Source** = 1, field point = 2. $\mathbf{R} = \mathbf{r}_2-\mathbf{r}_1$ ("final minus initial"); $\hat{R} = \mathbf{R}/|\mathbf{R}|$ points from source to field point. For $Q$ off the origin,
> $$
> \mathbf{E}(\mathbf{r}) = \frac{Q}{4\pi\epsilon_0}\,\frac{\mathbf{r}-\mathbf{r}'}{|\mathbf{r}-\mathbf{r}'|^{3}},
> $$
> with $\mathbf{r}'$ the source location. The cube: one power of $|\mathbf{r}-\mathbf{r}'|$ normalizes the direction vector.

Concept page: [[concepts/coulombs-law]].

### Drawing fields

- **Arrow plots**: an arrow on a grid with length $|\mathbf{E}|$ (or a *unit* vector with magnitude coded separately).
- **Field lines**: curves tangent to $\mathbf{E}$. They begin on positive and end on negative charge (or at infinity); leave a point charge uniformly; have *density* proportional to $|\mathbf{E}|$; and **never cross**, because $\mathbf{E}$ has one direction at each point — except at *null points* where $\mathbf{E}=0$ (the saddle between two like charges). A charge $2Q$ has twice as many lines as $Q$ — how you tell which charge is bigger in a picture.

## 3. Superposition

Maxwell's equations and Coulomb's law are linear: the field of several charges is the vector sum of their fields,

$$
\mathbf{E}(\mathbf{r}) = \sum_n \frac{Q_n}{4\pi\epsilon_0 R_n^2}\,\hat{R}_n,
\qquad \mathbf{R}_n = \mathbf{r}-\mathbf{r}_n .
$$

This is the engine of the next three lectures.

> [!example] Field on the perpendicular bisector of two opposite charges
> $+Q$ sits at $(0, a/2)$ and $-Q$ at $(0,-a/2)$. Find $\mathbf{E}$ at $P=(D,0)$.
>
> *Symmetry.* The $x$-components cancel (away from $+Q$, toward $-Q$); the $y$-components are equal, both along $-\hat{y}$. So $\mathbf{E} = 2E_{1y}\,\hat{y}$.
>
> *One contribution.* From $+Q$ to $P$: $\mathbf{R} = (D, -a/2)$, $R = \sqrt{D^2 + a^2/4}$, $\hat{R} = (D,-a/2)/R$, so
> $E_{1y} = \dfrac{Q}{4\pi\epsilon_0 R^2}\,\hat{R}\cdot\hat{y} = \dfrac{Q}{4\pi\epsilon_0 R^2}\left(-\dfrac{a/2}{R}\right)$.
>
> *Result.*
> $$
> \mathbf{E}(D,0) = -\,\frac{Q\,a}{4\pi\epsilon_0\,(D^2 + a^2/4)^{3/2}}\;\hat{y}
> \;\xrightarrow{\;D\gg a\;}\; -\,\frac{Qa}{4\pi\epsilon_0 D^3}\,\hat{y}.
> $$
> Far away the pair is a **dipole** $\mathbf{p} = Qa\,\hat{y}$: on this *equatorial* (broadside) line the field is $-\mathbf{p}/(4\pi\epsilon_0D^3)$, antiparallel to $\mathbf{p}$, falling as $1/D^3$ — faster than $1/D^2$ — because the charges nearly cancel. On the *axis* (point $(0,D)$) the contributions are collinear and *subtract*, giving $+2\mathbf{p}/(4\pi\epsilon_0D^3)$: twice as strong, along $\mathbf{p}$. "Double one component" works only on the bisector.

<!-- fig:dipole-map -->

## 4. Continuous distributions — the 5-step program

Charge on a line ($\rho_l$, C/m), surface ($\rho_s$, C/m²) or volume ($\rho$, C/m³): superposition becomes an integral over pieces $dQ = \rho_l\,dl = \rho_s\,dS = \rho\,dV$:

$$
\mathbf{E}(\mathbf{r}) = \frac{1}{4\pi\epsilon_0}\int \frac{dQ'}{R^2}\,\hat{R},
\qquad \hat{R} = \frac{\mathbf{r}-\mathbf{r}'}{|\mathbf{r}-\mathbf{r}'|},\ R = |\mathbf{r}-\mathbf{r}'| .
$$

> [!recipe] The "patented 5-step program" (use it every time)
> 1. **Make a large, clear drawing.** Cross-sections if 3-D; coordinates matching the symmetry.
> 2. **Chop the charge into pieces** $dQ$ in terms of density and coordinate: $\rho_l\,dz$, $\rho_s\,r\,dr\,d\phi$, …
> 3. **Write $d\mathbf{E}$ of one piece**: $d\mathbf{E} = \dfrac{dQ}{4\pi\epsilon_0R^2}\hat{R}$, with $\hat{R}$ and $R$ in your coordinates.
> 4. **Use symmetry** to find components that cancel between mirror-image pieces; keep the survivor (a scalar integral).
> 5. **Integrate.**
>
> Students skip step 4 — the one that turns a 3-D vector integral into a 1-D scalar one.

> [!trap] Unit vectors are constant only in Cartesian coordinates
> $\hat{x}$ can be pulled out of an integral; $\hat{r}$ and $\hat{\phi}$ change direction from point to point and **cannot**. Resolve them into Cartesian components first, or use symmetry so the surviving component is along a *fixed* direction at the field point. See [[0-toolkit/01-coordinates-and-differential-elements]].

### Worked example: finite line charge → infinite line charge

A uniform line charge $\rho_l$ occupies $-a<z<a$ on the $z$-axis. Find $\mathbf{E}$ at a point in the $z=0$ plane, a distance $r$ from the axis.

<!-- fig:line-charge-side -->

1. *Drawing / coordinates.* Cylindrical $(r,\phi,z)$; the field point is $(r, \phi, 0)$.
2. *Pieces.* $dQ = \rho_l\,dz$ at height $z$.
3. *One piece.* $R = \sqrt{r^2+z^2}$; $d\mathbf{E} = \dfrac{\rho_l\,dz}{4\pi\epsilon_0(r^2+z^2)}\hat{R}$, $\hat{R}$ from element to $P$ at angle $\alpha$ to the horizontal, $\cos\alpha = r/R$.
4. *Symmetry.* The element at $-z$ mirrors $d\mathbf{E}$: $z$-components cancel, radial ones add. Only $dE_r = dE\cos\alpha$ survives, and $\hat{r}$ at $P$ is *fixed* (set by $\phi$ of $P$, not $z$ of the source), so it comes outside.
5. *Integrate.*
   $$
   E_r = \frac{\rho_l}{4\pi\epsilon_0}\int_{-a}^{a}\frac{r\,dz}{(r^2+z^2)^{3/2}} .
   $$
   Substitute $z = r\tan\alpha$, $dz = r\sec^2\alpha\,d\alpha$, $r^2+z^2 = r^2\sec^2\alpha$:
   $$
   E_r = \frac{\rho_l}{4\pi\epsilon_0 r}\int_{-\alpha_0}^{\alpha_0}\cos\alpha\,d\alpha
       = \frac{\rho_l}{4\pi\epsilon_0 r}\,2\sin\alpha_0
       = \frac{\rho_l}{4\pi\epsilon_0 r}\,\frac{2a}{\sqrt{a^2+r^2}} .
   $$

> [!key] Infinite line charge
> Let $a\to\infty$: $\dfrac{2a}{\sqrt{a^2+r^2}}\to 2$, so
> $$
> \mathbf{E} = \frac{\rho_l}{2\pi\epsilon_0\, r}\,\hat{r}
> $$
> A line's field falls as $1/r$ — **not** $1/r^2$ — because charge farther along the line keeps contributing as you move away. (Lecture 3 gets this in two lines with Gauss's law; the cross-check is a course favourite.)

The slides' two "review at home" examples follow the same pattern: a **ring** of radius $a$, line charge $\rho_{l0}$ ($dQ = \rho_{l0}\,a\,d\phi$, total $2\pi a\rho_{l0}$); and a **charged rod** (charge $Q$ over length $L$ on the $x$-axis) acting on a point charge $q$ on that axis a distance $a$ beyond its end: $\mathbf{F} = \dfrac{qQ}{4\pi\epsilon_0\,a(L+a)}\hat{x}$, with $\hat{x}$ outside the integral because it is Cartesian.

## 5. From Coulomb to Gauss

Surround a point charge $Q$ by a sphere of radius $r$ and compute the **flux** of $\epsilon_0\mathbf{E}$ ($\oint_S\mathbf{F}\cdot d\mathbf{S}$ adds up the normal component; intuition in Lecture 3):

$$
\oint_S \epsilon_0\mathbf{E}\cdot d\mathbf{S}
= \epsilon_0\,\frac{Q}{4\pi\epsilon_0 r^2}\;\underbrace{(4\pi r^2)}_{\text{sphere area}} = Q .
$$

On the sphere $\mathbf{E}$ has constant magnitude and is parallel to the outward $d\mathbf{S}$, so the integral is $|\mathbf{E}|\times$area; the area's $r^2$ cancels Coulomb's $1/r^2$ **exactly**, independent of $r$. Three observations make this a law:

- **Any surface.** Lines leaving $Q$ never stop; each crosses any enclosing surface exactly once net (a wiggly surface crossed three times: two cancel). So the flux is $Q$ through *any* closed surface around $Q$ — and **zero** for one *not* enclosing $Q$ (every line that enters also leaves).
- **Superposition.** Flux is linear in $\mathbf{E}$: $Q_1 + Q_2 + \dots$ for charges inside, nothing for those outside.
- **Naming.** The **electric flux density** $\mathbf{D} = \epsilon_0\mathbf{E}$ (C/m²) makes flux come out in coulombs. (In materials, Lecture 8, $\mathbf{D} = \epsilon_0\mathbf{E}+\mathbf{P}$, and $\mathbf{D}$ keeps counting free charge.)

> [!key] Gauss's law — the first Maxwell equation
> $$
> \oint_S \mathbf{D}\cdot d\mathbf{S} = Q_{\text{enc}} = \int_V \rho\,dV
> $$
> for **any** closed surface $S$ bounding volume $V$, $d\mathbf{S}$ **outward**. Flux out = charge enclosed. Charges outside $S$ add nothing to the *flux* (they do change $\mathbf{E}$ on $S$; their flux cancels).

Derived here from Coulomb's law, Gauss's law is more fundamental: it holds for moving charges and time-varying fields, where Coulomb's law fails. The notes: "at this stage the introduction of Gauss's law may seem unnecessary"; Lecture 3 gets the line charge in two lines, and Lecture 4 makes it one of the four governing equations.

Concept pages: [[concepts/flux]] · [[concepts/electric-flux-density]] · [[concepts/gauss-law]] · [[concepts/superposition]].

## 6. Summary

| Configuration | $\mathbf{E}$ | falls off as |
|---|---|---|
| point charge $Q$ | $\dfrac{Q}{4\pi\epsilon_0 r^2}\hat{r}$ | $1/r^2$ |
| dipole $p=Qa$, far away | $\dfrac{p}{4\pi\epsilon_0 D^3}$ on the bisector (antiparallel to $\mathbf{p}$); $\dfrac{2p}{4\pi\epsilon_0 D^3}$ on the axis (along $\mathbf{p}$) | $1/D^3$ |
| infinite line $\rho_l$ | $\dfrac{\rho_l}{2\pi\epsilon_0 r}\hat{r}$ | $1/r$ |

> [!exam] On Exam 1
> Coulomb integrals (5-step program) are homework; the exam prefers the Gauss shortcut where symmetry allows (FA26 problems 2 and 4) and tests this lecture's *ideas*: which way $\hat{R}$ points, that only enclosed charge sets the flux, and the $1/r^2$ vs $1/r$ vs "no distance" pattern of point, line and sheet.

> [!tip] Practice this lecture
> [[practice/02-coulombs-law-superposition-and-gauss|12 practice problems]] — 5 easy, 3 medium, 4 hard — each with a folded hint and a worked solution. Start with [[practice/02-coulombs-law-superposition-and-gauss#21-coulomb-force-as-a-vector|2.1 Coulomb force as a vector]]; the [[practice/index|practice hub]] has the whole bank by difficulty and by topic.

### Sources for this page
Kudeki notes, Lecture 2 (Coulomb field; Example 1 field map; the line of charges summed with δ-functions, then by Gauss). Shao, Lecture 2 slides (velocity/mass selector, field-line rules and poll, 5-step program, ring/rod/finite-line examples). Lecture 3 slides §8–10 (Gauss from Coulomb).
