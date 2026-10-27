---
title: "Lecture 6 — Circulation and boundary conditions"
description: "Zero circulation is Kirchhoff's voltage law for fields. The integral laws hold across material boundaries even where the differential laws break down, and squeezing them onto an interface gives the boundary conditions: tangential E and normal B are continuous, normal D jumps by the surface charge, tangential H jumps by the surface current."
tags: [lecture, electrostatics, exam-1]
lecture: 6
---

*Lecture 6 · course notes §6 · slides "Boundary Conditions; Poisson's and Laplace's Equation" (first half) · prev: [[1-electrostatics/05-curl-free-fields-and-the-electrostatic-potential|Lecture 5]] · next: [[1-electrostatics/07-poisson-and-laplace|Lecture 7]] · practice: [[practice/06-circulation-and-boundary-conditions|12 problems]]*

> [!abstract] In one breath
> Around a closed path a static field's line integral is zero: the **circulation** vanishes — Kirchhoff's voltage law, and by Stokes the same as $\nabla\times\mathbf{E} = 0$. The differential laws assume differentiable fields; at a conductor or dielectric surface fields *jump*. The integral laws still hold for a loop or pillbox straddling the surface, and shrinking it onto the surface turns each Maxwell equation into a **boundary condition**: how much each component may jump. Four rules, one drawing, and a normal vector you must never lose track of.

## 1. Circulation: the loop version of path independence

With coinciding endpoints, path independence gives zero for *every* closed loop $C$:

> [!key] Circulation of a static field
> $$
> \oint_C\mathbf{E}\cdot d\mathbf{l} = 0 .
> $$
> $\oint_C\mathbf{E}\cdot d\mathbf{l}$ is the **circulation** of $\mathbf{E}$ around $C$. Zero circulation around every loop = **conservative**; by Stokes, $\oint_C\mathbf{E}\cdot d\mathbf{l} = \int_S(\nabla\times\mathbf{E})\cdot d\mathbf{S}$ for any $S$ spanning $C$, so it is the same as zero curl everywhere. In circuits: KVL, potential drops around a loop sum to zero.

> [!example] Example — a rectangle in a slab field
> Inside a uniformly charged slab centred on $x=0$, $\mathbf{E} = \hat{x}\,\rho x/\epsilon_0$ ([[1-electrostatics/03-gauss-law-at-work#3c-uniform-slab-planar-with-interior|Lecture 3]]), slab wide enough ($\lvert x\rvert<W/2$, $W/2\ge3$ m) to contain the loop. Rectangle $(1,0)$, $(3,0)$, $(3,4)$, $(1,4)$ in the $xy$-plane, in that order (counter-clockwise from $+z$):
> $$
> \oint_C\mathbf{E}\cdot d\mathbf{l} = \underbrace{\int_{x=1}^{3}\frac{\rho x}{\epsilon_0}\,dx}_{4\rho/\epsilon_0} + \underbrace{\int_{y=0}^{4}\hat{x}\frac{3\rho}{\epsilon_0}\cdot\hat{y}\,dy}_{0} + \underbrace{\int_{x=3}^{1}\frac{\rho x}{\epsilon_0}\,dx}_{-4\rho/\epsilon_0} + \underbrace{\int_{y=4}^{0}\hat{x}\frac{\rho}{\epsilon_0}\cdot\hat{y}\,dy}_{0} = 0 .
> $$
> Vertical legs: $\mathbf{E}\perp d\mathbf{l}$, zero; horizontal legs equal and opposite. (The notes' rectangle $-3\le x\le3$ makes each horizontal leg zero alone; off-centre, the cancellation does real work.) Bookkeeping: $d\mathbf{l}$ is $\hat{x}\,dx$ or $\hat{y}\,dy$, always with a plus sign; the *limits* walk around $C$ in the chosen direction.

Curl is local circulation: $(\nabla\times\mathbf{E})_x = \lim\frac{1}{\Delta y\Delta z}\oint_{C_x}\mathbf{E}\cdot d\mathbf{l} = \frac{\partial E_z}{\partial y} - \frac{\partial E_y}{\partial z}$ for a tiny loop in a constant-$x$ plane, and similarly ([[1-electrostatics/04-divergence-and-curl#3-curl-circulation-per-unit-area|Lecture 4 §3]]). Right-hand rule: fingers curl along the travel, thumb along $d\mathbf{S}$.

> [!key] The laws of electrostatics, and when they apply
> $$
> \nabla\times\mathbf{E} = 0,\qquad \nabla\cdot\mathbf{D} = \rho,\qquad \mathbf{D} = \epsilon_0\mathbf{E}\ (\text{vacuum}).
> $$
> They also hold **quasi-statically**: if sources vary on a time scale $\tau\gg L/c$ (light-travel time across the region), the fields at each instant are the static fields of the instantaneous sources (plus a small, slowly varying $\mathbf{B}$). Excellent for lab circuits below a few MHz; the transmission-line unit is about when it fails.

## 2. Where fields jump

At a **surface charge** fields are not differentiable: the sheet of [[1-electrostatics/03-gauss-law-at-work#3b-infinite-sheet-planar|Lecture 3]], $\mathbf{E} = \hat{z}\dfrac{\rho_s}{2\epsilon_0}\text{sgn}(z)$, flips its $z$-component across the sheet. Add the smooth field $\mathbf{E}_0$ of the *other* sources:

$$
\mathbf{E} = \hat{z}\frac{\rho_s}{2\epsilon_0}\text{sgn}(z) + \mathbf{E}_0 .
$$

At $z=0^\pm$ the smooth part is the same, so **tangential** $E_x, E_y$ are continuous while the **normal component** jumps: $E_z(0^+) - E_z(0^-) = \rho_s/\epsilon_0$, i.e. $D_z(0^+) - D_z(0^-) = \rho_s$. Neither orientation nor flatness was used (a curved surface is flat on a small scale), so this holds at *any* charged surface. §3 derives it from the integral laws, so the magnetic conditions come for free.

## 3. The boundary conditions, from the integral laws

The integral laws hold for **every** closed surface and path — including ones straddling a boundary, where the differential forms are meaningless. Apply them to a straddling shape, then squash it flat.

<!-- fig:bc-pillbox-loop -->

> [!derivation]- Pillbox and loop, step by step
> **Conventions.** Medium 1 on one side, medium 2 on the other; $\hat{n}$ is the unit normal to the interface **pointing from medium 2 into medium 1**. Subscripts $n$ and $t$ denote normal and tangential components.
>
> **Gauss's law on a pillbox.** Caps of area $A$, one in each medium, side wall of height $h$. As $h\to0$ the side flux vanishes (finite field, vanishing area), the enclosed *volume* charge vanishes, the *surface* charge $\rho_sA$ stays. Outward normals: $+\hat{n}$ on the medium-1 cap, $-\hat{n}$ on the medium-2 cap:
> $$
> \oint\mathbf{D}\cdot d\mathbf{S} = \mathbf{D}_1\cdot\hat{n}A - \mathbf{D}_2\cdot\hat{n}A = \rho_sA \quad\Longrightarrow\quad \hat{n}\cdot(\mathbf{D}_1-\mathbf{D}_2) = \rho_s .
> $$
> The same pillbox with $\oint\mathbf{B}\cdot d\mathbf{S} = 0$ gives $\hat{n}\cdot(\mathbf{B}_1-\mathbf{B}_2) = 0$.
>
> **Faraday's law on a loop.** Rectangle of length $L$ along the surface, height $h$ across, one long edge in each medium. As $h\to0$ the short edges give nothing and the magnetic flux ($\propto Lh$) vanishes even if $\partial\mathbf{B}/\partial t\neq0$. Long edges traversed in opposite directions:
> $$
> \oint\mathbf{E}\cdot d\mathbf{l} = E_{1t}L - E_{2t}L = 0 \quad\Longrightarrow\quad E_{1t} = E_{2t},\ \text{i.e.}\ \hat{n}\times(\mathbf{E}_1-\mathbf{E}_2) = 0 .
> $$
> (The cross product with $\hat{n}$ picks out the tangential part of a vector — rotated by 90°, but zero is zero.)
>
> **Ampère's law on the same loop.** $\oint\mathbf{H}\cdot d\mathbf{l} = I_{\text{enc}} + \frac{d}{dt}\int\mathbf{D}\cdot d\mathbf{S}$. The displacement term dies with the area, but a **surface current** $\mathbf{J}_s$ [A/m] *in* the interface threads the loop with $I_{\text{enc}} = J_sL$ (component of $\mathbf{J}_s$ perpendicular to the loop). Hence $H_{1t} - H_{2t} = J_s$, or $\hat{n}\times(\mathbf{H}_1-\mathbf{H}_2) = \mathbf{J}_s$.
>
> The time-derivative terms vanish with the *area*, not because fields are static, so all four conditions hold for time-varying fields too.

> [!key] The four boundary conditions ($\hat{n}$ from medium 2 into medium 1)
> $$
> \hat{n}\cdot(\mathbf{D}_1-\mathbf{D}_2) = \rho_s,\qquad
> \hat{n}\times(\mathbf{E}_1-\mathbf{E}_2) = 0,\qquad
> \hat{n}\cdot(\mathbf{B}_1-\mathbf{B}_2) = 0,\qquad
> \hat{n}\times(\mathbf{H}_1-\mathbf{H}_2) = \mathbf{J}_s .
> $$
> **Normal $\mathbf{D}$ jumps by the free surface charge; tangential $\mathbf{E}$ is continuous; normal $\mathbf{B}$ is continuous; tangential $\mathbf{H}$ jumps by the surface current.** *Nothing* is said about tangential $\mathbf{D}$ or normal $\mathbf{E}$ (they jump at a dielectric interface even with $\rho_s=0$), nor normal $\mathbf{H}$ or tangential $\mathbf{B}$. The notes write $\hat{n}\cdot(\mathbf{D}^+-\mathbf{D}^-) = \rho_s$, "$+$" = the side $\hat{n}$ points into — identical content.

<!-- fig:bc-summary-panels -->

> [!recipe] How to remember them
> In each differential Maxwell equation replace $\nabla\to\hat{n}$, each field by (field in 1) − (field in 2), $\rho\to\rho_s$, $\mathbf{J}\to\mathbf{J}_s$, $\partial/\partial t\to0$: $\nabla\cdot\mathbf{D}=\rho$ becomes $\hat{n}\cdot(\mathbf{D}_1-\mathbf{D}_2)=\rho_s$, $\nabla\times\mathbf{E} = -\partial\mathbf{B}/\partial t$ becomes $\hat{n}\times(\mathbf{E}_1-\mathbf{E}_2)=0$, etc. Divergence equations constrain normal components; curl equations tangential ones.

## 4. The normal vector is half the problem

Every sign error here is an $\hat{n}$ error. *You* choose which side is medium 1; $\hat{n}$ must point into it. At a second interface you usually re-choose, and $\hat{n}$ flips. Draw $\hat{n}$ at every interface before writing an equation.

> [!example] Example — a vacuum gap bounded by two charged planes
> Vacuum; $\mathbf{D} = 0$ measured for $x<0$. Planes $x=0$ and $x=5$ m carry $\rho_s = 2$ C/m² and an unknown $\rho_{s0}$; no other charges. Find $\mathbf{D}$ everywhere and $\rho_{s0}$.
>
> *At $x=0$:* gap $0<x<5$ = medium 1, $x<0$ = medium 2, $\hat{n} = +\hat{x}$. $\hat{x}\cdot(\mathbf{D}_1 - 0) = 2$, so $D_{1x} = 2$; no tangential field on the left, $E_t$ continuous, $\mathbf{D} = \epsilon_0\mathbf{E}$ both sides: $\mathbf{D}_1 = 2\hat{x}$ C/m² in the gap.
>
> *At $x=5$:* now the gap is side "2" and $x>5$ medium 1 ($\hat{n} = +\hat{x}$ into $x>5$) — or keep the gap as medium 1 with $\hat{n} = -\hat{x}$. Either way $D_x(x>5) - 2 = \rho_{s0}$. The jump alone cannot fix $\rho_{s0}$; superposition does. The two sheets' fields must cancel for $x<0$: sheet 1 gives $-\tfrac{2}{2}\hat{x}$ there, sheet 2 $-\tfrac{\rho_{s0}}{2}\hat{x}$, so $\rho_{s0} = -2$ C/m², and $\mathbf{D} = 0$ for $x>5$ too.
>
> Result: $\mathbf{D} = 0,\ 2\hat{x},\ 0$ C/m² in the three regions — a parallel-plate capacitor's field.

> [!example] Example — tangential and normal bookkeeping together
> $\mathbf{D} = 3\hat{y}$ C/m² for $x<0$; sheets $\rho_s = 2$ at $x=0$ and $-6$ C/m² at $x=5$ m; $\mathbf{D}$ uniform in each region (vacuum). *Tangential:* $\mathbf{E} = 3\hat{y}/\epsilon_0$ is parallel to both planes and never jumps, $\mathbf{D} = \epsilon_0\mathbf{E}$, so $D_y = 3$ everywhere (from distant charges, not the sheets). *Normal:* $D_x$ starts at 0, rises by $2$ at $x=0$, by $-6$ at $x=5$:
> $$
> \mathbf{D} = \begin{cases}3\hat{y}, & x<0\\ 2\hat{x}+3\hat{y}, & 0<x<5\text{ m}\\ -4\hat{x}+3\hat{y}, & x>5\text{ m}\end{cases}\quad[\text{C/m}^2].
> $$

> [!example] Example — a preview of dielectrics (in-class challenge)
> Medium 1 ($\epsilon_1 = \epsilon_0$, above) meets medium 2 ($\epsilon_2 = 2\epsilon_0$, below) on a plane with free charge $\rho_s = 3$ C/m². Below, $\mathbf{D}_2 = 3\hat{x} + 2\hat{y}$ C/m², $\hat{y}$ normal. Find $\mathbf{D}_1$, using $\mathbf{D} = \epsilon\mathbf{E}$ in each medium ([[1-electrostatics/08-conductors-dielectrics-and-polarization|Lecture 8]]).
> - Tangential: $E_{1t} = E_{2t}$ ⇒ $D_{1t}/\epsilon_0 = D_{2t}/(2\epsilon_0) = 3/(2\epsilon_0)$ ⇒ $D_{1t} = \tfrac32$. **Tangential $\mathbf{D}$ is not continuous** — it scales with $\epsilon$.
> - Normal ($\hat{n} = \hat{y}$ from 2 into 1): $D_{1n} - D_{2n} = \rho_s$ ⇒ $D_{1n} = 2 + 3 = 5$.
>
> $\mathbf{D}_1 = \tfrac32\hat{x} + 5\hat{y}$ C/m². The slide's wrong options are the standard errors: $3\hat{x}+2\hat{y}$ (everything continuous), $3\hat{x}+5\hat{y}$ (tangential $\mathbf{D}$ continuous), $\tfrac32\hat{x} - 1\hat{y}$ (jump subtracted — $\hat{n}$ flipped).

## 5. What the conditions do and do not tell you

- They fix **differences**, never levels; the level comes from a measured field, symmetry, superposition, or a conductor's potential.
- $\rho_s$ is **free** surface charge. In matter ([[1-electrostatics/08-conductors-dielectrics-and-polarization|Lecture 8]]) the equation survives with $\mathbf{D} = \epsilon_0\mathbf{E}+\mathbf{P}$; $\mathbf{P}$ accounts for bound charge.
- At a conductor the interior field is zero, so $\hat{n}\cdot\mathbf{D} = \rho_s$ and $\hat{n}\times\mathbf{E} = 0$, $\hat{n}$ out of the metal: **the field leaves a conductor perpendicularly, and its normal $\mathbf{D}$ *is* the surface charge** ([[1-electrostatics/07-poisson-and-laplace|Lecture 7]] reads plate charges this way).
- Between two perfect dielectrics there is normally no free charge: $D_n$ and $E_t$ continuous — the pair that bends field lines ([[1-electrostatics/09-static-fields-in-dielectric-media|Lecture 9]]).

> [!trap] Four ways to go wrong
> 1. **Mixing up what is continuous.** $E_t$ and $D_n$, not $E_n$ and $D_t$. Test: at a charged conductor $\mathbf{E}$ is nonzero outside, zero inside — normal $\mathbf{E}$ jumps.
> 2. **Losing $\hat{n}$.** Pick medium 1, point $\hat{n}$ into it, re-decide at every interface. Swapping labels *and* $\hat{n}$ changes nothing; swapping one flips the sign of $\rho_s$.
> 3. **Differential laws across a boundary.** $\nabla\cdot\mathbf{D}=\rho$ needs a differentiable $\mathbf{D}$; at a surface charge use the jump condition (or a $\delta$-function).
> 4. **Units.** $\rho_s$ and $\mathbf{D}$ in C/m²; $\mathbf{J}_s$ in A/m (current per unit *width*, not $I/S$) and $\mathbf{H}$ in A/m. A stray $\epsilon_0$ in a jump condition means $\mathbf{E}$ written where $\mathbf{D}$ belongs.

## 6. Summary

- $\oint_C\mathbf{E}\cdot d\mathbf{l} = 0$ for static fields: KVL, equivalent to $\nabla\times\mathbf{E} = 0$ by Stokes.
- Fields jump only at surface charges and currents; the squeezed integral laws say by how much.
- $\hat{n}\cdot(\mathbf{D}_1-\mathbf{D}_2) = \rho_s$, $\hat{n}\times(\mathbf{E}_1-\mathbf{E}_2) = 0$, $\hat{n}\cdot(\mathbf{B}_1-\mathbf{B}_2) = 0$, $\hat{n}\times(\mathbf{H}_1-\mathbf{H}_2) = \mathbf{J}_s$, with $\hat{n}$ from 2 into 1.
- Conditions fix jumps, not levels; $\rho_s$ is free charge; $\hat{n}$ is re-chosen at every interface.

Concept page: [[concepts/boundary-conditions]].

> [!exam] On Exam 1
> FA26 problem 3: a dielectric interface — given $\mathbf{E}_1$ above $z=0$ and two permittivities, find $\mathbf{E}_2$ (tangential copied, normal scaled by $\epsilon_1/\epsilon_2$), then $\mathbf{D}$ and $\mathbf{P}$ on both sides. Worked with other numbers in [[problems/fields-across-a-dielectric-interface]]. The two-plane examples are the pattern of HW3 #6, where a sheet is written $\rho = \rho_s\,\delta(y)$ and you read off the jump.

> [!tip] Practice this lecture
> [[practice/06-circulation-and-boundary-conditions|12 practice problems]] — 5 easy, 3 medium, 4 hard — each with a folded hint and a worked solution. Start with [[practice/06-circulation-and-boundary-conditions#61-what-is-always-continuous|6.1 What is always continuous]]; the [[practice/index|practice hub]] has the whole bank by difficulty and by topic.

### Sources for this page
Kudeki notes, Lecture 6 (circulation; Example 1; curl as circulation per area; quasi-static note; sheet plus background; $\pm$ notation; loop/pillbox justification; Examples 2–3). Shao, Lectures 6–7 slides (integral vs differential forms at a boundary; pillbox and loop derivations; "Points INTO medium 1"; two-plane example; challenge question; "Remember this drawing!!" and the memorization rule). Slips in the course material: see [[0-toolkit/04-errata-in-the-course-materials|errata]].
