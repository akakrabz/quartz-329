---
title: "Lecture 13 — Current sheets, solenoids, and the vector potential"
description: "Ampère's law with a well-chosen rectangle gives the field of a current sheet (tangential, ±Jₛ/2, independent of distance), a current slab (a ramp) and an infinite solenoid (μ₀nI inside, nothing outside). Because ∇·B = 0, B = ∇×A; in the Coulomb gauge ∇²A = −μ₀J, and a current loop follows — a magnetic dipole whose field falls as 1/r³."
tags: [lecture, magnetostatics]
lecture: 13
---

*Lecture 13 · course notes §13 · slides "Ampère's Law" · prev: [[2-magnetostatics/12-magnetic-force-biot-savart-and-amperes-law|Lecture 12]] · next: [[2-magnetostatics/14-faradays-law-and-induced-emf|Lecture 14]] · practice: [[practice/13-current-sheets-solenoids-and-vector-potential|12 problems]]*

> [!abstract] In one breath
> As [[1-electrostatics/03-gauss-law-at-work|Lecture 3]] did with Gauss's law and symmetric charges, this lecture uses Ampère's law on symmetric *currents*; every answer is the Unit 1 answer with "normal" replaced by "tangential". A current sheet makes a tangential field $J_s/2$ that reverses across the sheet and does not fall off; a slab turns the step into a ramp; a solenoid — a sheet rolled into a cylinder — traps a uniform $\mu_0nI$ inside and nothing outside. Second half: because $\nabla\cdot\mathbf{B} = 0$, $\mathbf{B} = \nabla\times\mathbf{A}$; choosing $\nabla\cdot\mathbf{A} = 0$ turns Ampère's law into $\nabla^2\mathbf{A} = -\mu_0\mathbf{J}$, solved by the Coulomb integral with $\rho/\epsilon_0\to\mu_0\mathbf{J}$. A single loop then gives the dipole field shared by bar magnets, compass needles and the Earth.

## 1. The current sheet

<!-- fig:current-sheet-slab -->

Uniform $\mathbf{J}_s = J_s\hat z$ on the plane $x = 0$, infinite in $y$ and $z$. Symmetry fixes the *direction* first: the sheet is a stack of filaments along $z$; pair a filament at $+y'$ with its mirror at $-y'$, and at a point on the $x$ axis their $\hat x$ parts cancel while the $\hat y$ parts add. So $\mathbf{B} = \hat yB_y(x)$, odd in $x$, independent of $y$ and $z$. Now the rectangle in the figure: long sides of length $L$ parallel to $\hat y$ at $x = \mp W/2$, short sides crossing the sheet. On the short sides $\mathbf{B}\perp d\mathbf{l}$; on each long side the field is parallel to the direction of travel (both reverse with $x$), so each contributes $+B_yL$:

$$
\oint_C\mathbf{B}\cdot d\mathbf{l} = 2B_yL = \mu_0I_C = \mu_0J_sL\quad\Rightarrow\quad B_y = \frac{\mu_0J_s}{2}\ (x>0).
$$

> [!key] Field of an infinite current sheet
> $$
> \mathbf{H} = \hat y\,\frac{J_s}{2}\,\text{sgn}(x),\qquad\mathbf{B} = \mu_0\mathbf{H},\qquad\text{in general}\qquad \mathbf{H} = \tfrac12\,\mathbf{J}_s\times\hat n,
> $$
> $\hat n$ the unit normal from the sheet *toward the field point*. Check: for $x>0$, $\hat n = \hat x$ and $\tfrac12J_s\hat z\times\hat x = \tfrac12J_s\hat y$ ✓. The magnitude is independent of distance (an infinite sheet has no scale to fall off with), and **tangential $\mathbf{H}$ jumps by $J_s$** across the sheet: $\hat n\times(\mathbf{H}_1-\mathbf{H}_2) = \mathbf{J}_s$, the boundary condition stated in Lecture 16 — twin of $D_n$ jumping by $\rho_s$.

The slides put the sheet on $y = 0$ with current along $z$ and get $\mathbf{H} = -\tfrac12J_{s0}\hat x\,\text{sgn}(y)$ — same formula $\tfrac12\mathbf{J}_s\times\hat n$, different axes. The $\text{sgn}$ is the most-reversed sign in this unit; evaluate $\mathbf{J}_s\times\hat n$ on one side explicitly rather than remembering a picture.

## 2. The current slab

$\mathbf{J} = \hat zJ_0$ for $|x|<W/2$, zero outside. Same symmetry, same rectangle, now of half-width $x$ centred on the slab: enclosed current $J_0\cdot2x\cdot L$ for $|x|<W/2$, $J_0WL$ beyond:

> [!key] Field of a current slab
> $$
> \mathbf{H} = \begin{cases}\hat y\,J_0x, & |x|<W/2,\\[4pt] \hat y\,J_0\dfrac W2\,\text{sgn}(x), & |x|\ge W/2.\end{cases}
> $$
> A ramp of slope $J_0$ inside — $(\nabla\times\mathbf{H})_z = dH_y/dx = J_0$ ✓ — saturating at $\pm J_0W/2$ outside, **continuous** at the faces (no *surface* current there). From outside, the slab looks like a sheet with $J_s = J_0W$.

The charged slab of Lecture 3 ($D_x = \rho_0x$ inside, $\pm\rho_0W/2$ outside) has the identical plot with $D_x\to H_y$, $\rho_0\to J_0$. [[problems/current-slab-and-sheet-by-amperes-law]] superposes a slab and a sheet, as the Exam 1 slab problem did with charge.

## 3. The solenoid

<!-- fig:solenoid-ampere -->

A tight helix, $n$ turns per metre, each carrying $I$ counter-clockwise viewed from the top: from a little distance, a cylindrical **current sheet** $\mathbf{J}_s = nI\,\hat\phi$. By symmetry the field is axial and depends only on $r$. Two Amperian rectangles of height $L$:

- $C_1$, both long legs *outside*, links $nL$ turns one way and $nL$ the other: $\oint_{C_1}\mathbf{B}\cdot d\mathbf{l} = 0$. So the exterior field is uniform, and for an isolated infinite coil it is zero (a finite loop's field falls off, so the field at infinity, hence everywhere outside, is zero).
- $C_2$, one leg inside and one outside, links $nL$ turns all the same way: $B_zL = \mu_0nLI$.

> [!key] Field of an infinite solenoid
> $$
> \mathbf{B} = \hat z\,\mu_0nI,\qquad \mathbf{H} = \hat z\,nI\quad\text{inside};\qquad \mathbf{B} = 0\quad\text{outside}.
> $$
> Uniform inside, independent of the coil's radius; by the sheet rule, tangential $\mathbf{H}$ jumps by $J_s = nI$ across the winding.

Two footnotes from the notes. Ampère's law alone cannot exclude a uniform exterior field from *other* sources; one would add to the interior field too, unrelated to $I$. A finite solenoid has $\mathbf{H}\approx\hat znI$ at its centre, dropping to $\tfrac12nI$ at each end, with lines fringing out and looping back outside (they cannot end). For a coil much longer than its radius the infinite result is excellent at the centre.

## 4. Statics, side by side

> [!key] The two static theories (course notes, Lecture 13)
> **Static electric fields** are *curl-free*: $\nabla\times\mathbf{E} = 0$, $\nabla\cdot\mathbf{D} = \rho$, with $\mathbf{D} = \epsilon\mathbf{E}$, $\epsilon = \epsilon_r\epsilon_0$.
> **Static magnetic fields** are *divergence-free*: $\nabla\cdot\mathbf{B} = 0$, $\nabla\times\mathbf{H} = \mathbf{J}$, with $\mathbf{B} = \mu\mathbf{H}$, $\mu = \mu_r\mu_0$ ($\mu_r\ne1$ is explained in Lecture 17).
>
> Full translation table: the [[2-magnetostatics/index#the-dictionary-electrostatics--magnetostatics|dictionary]] on the unit page.

A curl-free field is the gradient of a scalar — $V$ in [[1-electrostatics/05-curl-free-fields-and-the-electrostatic-potential|Lecture 5]]. What is a divergence-free field?

## 5. The vector potential

$\mathbf{B} = \nabla\times\mathbf{A}$ is divergence-free for every $\mathbf{A}$, since $\nabla\cdot(\nabla\times\mathbf{A}) = 0$ (a determinant with two identical rows of $\partial$'s, or expand: $\partial_x(\partial_yA_z-\partial_zA_y) + \partial_y(\partial_zA_x-\partial_xA_z) + \partial_z(\partial_xA_y-\partial_yA_x)$ cancels pairwise). Conversely every divergence-free field can be written this way:

> [!key] Vector potential and the Coulomb gauge
> $$
> \mathbf{B} = \nabla\times\mathbf{A}\quad[\mathbf{A}\ \text{in Wb/m} = \text{T·m}].
> $$
> $\mathbf{A}$ is not unique: $\mathbf{A}+\nabla\lambda$, any scalar $\lambda$, has the same curl ($\nabla\times\nabla\lambda = 0$). In electrostatics the freedom was a constant in $V$, spent by "grounding" a point; here it is a gradient, spent by prescribing $\nabla\cdot\mathbf{A}$. The magnetostatic choice is $\nabla\cdot\mathbf{A} = 0$, the **Coulomb gauge**.

Then $\nabla\times\nabla\times\mathbf{A} = \nabla(\nabla\cdot\mathbf{A}) - \nabla^2\mathbf{A}$ loses its first term, and $\nabla\times\mathbf{B} = \mu_0\mathbf{J}$ becomes

> [!key] Poisson's equation for A, and its solution
> $$
> \nabla^2\mathbf{A} = -\mu_0\mathbf{J}\qquad\Longrightarrow\qquad \mathbf{A}(\mathbf{r}) = \int\frac{\mu_0\mathbf{J}(\mathbf{r}')}{4\pi\lvert\mathbf{r}-\mathbf{r}'\rvert}\,d^3r' .
> $$
> Compare $\nabla^2V = -\rho/\epsilon_0$ and $V(\mathbf{r}) = \displaystyle\int\frac{\rho(\mathbf{r}')}{4\pi\epsilon_0\lvert\mathbf{r}-\mathbf{r}'\rvert}d^3r'$ ([[1-electrostatics/07-poisson-and-laplace|Lecture 7]]): the same Green's function $1/(4\pi\lvert\mathbf{r}-\mathbf{r}'\rvert)$, applied to each Cartesian component of $\mathbf{J}$. (The vector Laplacian is the scalar Laplacian of each Cartesian component; cylindrical or spherical components do not split so simply.)

The integral satisfies $\nabla\cdot\mathbf{A} = 0$ automatically **provided $\nabla\cdot\mathbf{J} = 0$** — true for steady currents (the continuity equation of [[3-maxwell-and-waves/16-charge-conservation-displacement-current-and-maxwells-equations|Lecture 16]] with $\partial\rho/\partial t = 0$). For any static (or quasi-static, $L\ll c/f$) current: integrate for $\mathbf{A}$, take the curl for $\mathbf{B}$. A footnote in the notes reads $\mathbf{A}$ in this gauge as potential *momentum* per unit charge, as $V$ is potential energy per unit charge; [[2-magnetostatics/15-inductance-magnetic-energy-and-the-potentials|Lecture 15]] shows what $\mathbf{A}$ does when fields vary.

| | scalar potential $V$ | vector potential $\mathbf{A}$ |
|---|---|---|
| exists because | $\nabla\times\mathbf{E} = 0$ | $\nabla\cdot\mathbf{B} = 0$ |
| field from potential | $\mathbf{E} = -\nabla V$ | $\mathbf{B} = \nabla\times\mathbf{A}$ |
| freedom | $V\to V + \text{const}$ | $\mathbf{A}\to\mathbf{A}+\nabla\lambda$ |
| how it is spent | $V = 0$ at a chosen point | $\nabla\cdot\mathbf{A} = 0$ (Coulomb gauge) |
| equation | $\nabla^2V = -\rho/\epsilon_0$ | $\nabla^2\mathbf{A} = -\mu_0\mathbf{J}$ |
| meaning | energy per unit charge | momentum per unit charge |

## 6. The current loop and the magnetic dipole

<!-- fig:current-loop-field -->

A field Biot–Savart alone makes awkward: a circular loop of radius $a$ in $z = 0$ carrying $I$ counter-clockwise, $\mathbf{J}(\mathbf{r}') = I\,\delta(z')\,\delta(r'-a)\,\hat\phi'$. The $z'$ and $r'$ integrations are trivial, leaving one angle:

$$
\mathbf{A}(\mathbf{r}) = \frac{\mu_0I}{4\pi}\int_{-\pi}^{\pi}\frac{(-a\sin\phi',\ a\cos\phi',\ 0)}{\sqrt{(x-a\cos\phi')^2 + (y-a\sin\phi')^2 + z^2}}\,d\phi' \equiv \hat xA_x + \hat yA_y,
$$

so $A_z = 0$ and $B_x = -\partial_zA_y$, $B_y = \partial_zA_x$, $B_z = \partial_xA_y - \partial_yA_x$. By symmetry the plane $y = 0$ suffices; differentiating under the integral,

$$
B_x = \frac{\mu_0aI}{4\pi}\int_{-\pi}^{\pi}\frac{z\cos\phi\,d\phi}{(x^2+a^2+z^2-2ax\cos\phi)^{3/2}},\qquad
B_z = \frac{\mu_0aI}{4\pi}\int_{-\pi}^{\pi}\frac{(a - x\cos\phi)\,d\phi}{(x^2+a^2+z^2-2ax\cos\phi)^{3/2}},
$$

and $B_y = 0$ (odd integrand). For general $(x,z)$ these are complete elliptic integrals, but two limits are easy:

> [!key] On the axis, and far away
> $$
> B_z(0,0,z) = \frac{\mu_0Ia^2}{2(a^2+z^2)^{3/2}}\quad\xrightarrow{|z|\gg a}\quad \frac{\mu_0Ia^2}{2|z|^3}.
> $$
> At the centre, $B_z = \mu_0I/2a$. Far away the field falls as the **inverse cube** of distance: the loop is a **magnetic dipole** with moment $m = I\pi a^2$ (axial far field $\mu_0m/(2\pi|z|^3)$, the form of the electric dipole's $p/(2\pi\epsilon_0r^3)$ in [[1-electrostatics/02-coulombs-law-superposition-and-gauss|Lecture 2]]).

Why does it fall off? Every closed field line links the loop, so $\oint\mathbf{B}\cdot d\mathbf{l} = \mu_0I$ along *each*: a longer line further out carries a weaker average field. The on-axis formula gives how much weaker, and the same $r^{-3}$ holds in every direction, with a dipole's angular pattern. Far away, the field lines on $y = 0$ are $r = L\sin^2\theta$ ($L$ = the line's radius at the equatorial plane) — the bar-magnet pattern and the topology of the Earth's field.

Coaxial loops with currents in the same sense attract ($I\,d\mathbf{l}\times\mathbf{B}$ on the upper loop: the radial $\mathbf{B}$ there gives an axial force toward the lower loop). Bar magnets are stacks of atomic current loops interacting the same way, through $q\mathbf{v}\times\mathbf{B}$; Lecture 17 turns this into the magnetization $\mathbf{M}$ and the permeability $\mu$.

## 7. Summary

- Sheet: $\mathbf{H} = \tfrac12\mathbf{J}_s\times\hat n$, tangential, $\pm J_s/2$, no distance dependence; tangential $\mathbf{H}$ jumps by $J_s$.
- Slab: ramp $J_0x$ inside, $\pm J_0W/2$ outside, continuous; the charged-slab plot with $D\to H$.
- Solenoid: $\mathbf{B} = \mu_0nI\hat z$ inside, $0$ outside; finite coil: $\tfrac12nI$ at the ends.
- $\nabla\cdot\mathbf{B} = 0\Rightarrow\mathbf{B} = \nabla\times\mathbf{A}$; Coulomb gauge $\nabla\cdot\mathbf{A} = 0$; $\nabla^2\mathbf{A} = -\mu_0\mathbf{J}$; $\mathbf{A} = \int\mu_0\mathbf{J}\,d^3r'/(4\pi\lvert\mathbf{r}-\mathbf{r}'\rvert)$.
- Loop: $B_z = \mu_0Ia^2/[2(a^2+z^2)^{3/2}]$ on the axis; far field $\propto1/r^3$ (dipole); lines $r = L\sin^2\theta$; parallel loops attract.

Concept pages: [[concepts/amperes-law]] · [[concepts/vector-potential]] · [[concepts/magnetic-field]] · [[concepts/boundary-conditions]].

> [!exam] On exams
> Sheet, slab and solenoid are the three "find $\mathbf{H}$ by Ampère's law" set pieces; a superposition (slab plus sheet, two sheets, solenoid inside solenoid) is the natural exam problem — see [[problems/current-slab-and-sheet-by-amperes-law]]. Know $\tfrac12\mathbf{J}_s\times\hat n$ cold, direction from the cross product, and that $H_t$ jumps by $J_s$ while $B_n$ is continuous. The vector potential is examined lightly: $\mathbf{B} = \nabla\times\mathbf{A}$, why the gauge freedom exists, $\nabla^2\mathbf{A} = -\mu_0\mathbf{J}$ as Poisson's twin; the loop integrals are not for exams, the on-axis result might be.

> [!tip] Practice this lecture
> [[practice/13-current-sheets-solenoids-and-vector-potential|12 practice problems]] — 5 easy, 3 medium, 4 hard — each with a folded hint and a worked solution. Start with [[practice/13-current-sheets-solenoids-and-vector-potential#131-one-current-sheet-two-points|13.1 One current sheet, two points]]; the [[practice/index|practice hub]] has the whole bank by difficulty and by topic.

### Sources for this page
Kudeki notes, Lecture 13 (Examples 1–3: sheet, slab, solenoid with $C_1$, $C_2$, the exterior caveat and finite coil; statics box; $\nabla\cdot\nabla\times\mathbf{A} = 0$; gauge freedom, Coulomb gauge, "potential momentum"; $\nabla^2\mathbf{A} = -\mu_0\mathbf{J}$; the loop integrals, on-axis and far fields, $r = L\sin^2\theta$, attracting loops). Shao, Lecture 13 slides (MMF ↔ EMF; mirror-strip symmetry and rectangle; $\mathbf{H} = \tfrac12\mathbf{J}_s\times\hat a_n$; slab with its $H_y(x)$ graph; solenoid). The site's own: $m = I\pi a^2$ and the elliptic-integral remark. Slips in the course material: see [[0-toolkit/04-errata-in-the-course-materials|errata]].
