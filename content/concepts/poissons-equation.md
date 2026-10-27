---
title: "Poisson's and Laplace's equations"
description: "∇²V = −ρ/ε is Gauss's law written for the potential, valid where ε is constant; ∇²V = 0 in charge-free regions. One-dimensional solutions are linear, logarithmic or 1/r, fixed by two boundary values; with charge present, integrate twice and match V."
tags: [concept, electrostatics, exam-1]
aliases: ["Laplace's equation", "Laplacian", "Poisson equation", "Laplace between conductors", "homogeneous medium", "uniqueness"]
---

> [!key] Poisson's and Laplace's equations (homogeneous medium: $\epsilon$ independent of position)
> Take $\nabla\cdot\mathbf{D} = \rho$ with $\mathbf{D} = \epsilon\mathbf{E}$ and $\mathbf{E} = -\nabla V$:
> $$
> \nabla\cdot(\epsilon\,\nabla V) = -\rho \quad\xrightarrow{\ \epsilon\ \text{constant}\ }\quad \epsilon\,\nabla\cdot\nabla V = -\rho .
> $$
> $$
> \nabla^2V = -\frac{\rho}{\epsilon},\qquad\qquad \nabla^2V = 0\ \ (\rho = 0),
> $$
> with the **Laplacian** $\nabla^2V \equiv \nabla\cdot\nabla V = \dfrac{\partial^2V}{\partial x^2}+\dfrac{\partial^2V}{\partial y^2}+\dfrac{\partial^2V}{\partial z^2}$ (Cartesian; other forms on [[0-toolkit/02-vector-calculus-cheatsheet|the cheat sheet]]). Poisson's equation *is* Gauss's law for the potential. In vacuum $\epsilon = \epsilon_0$.

**Physics.** Both conditions matter. "Static" (or quasi-static) allows $\mathbf{E} = -\nabla V$. "$\epsilon$ constant" lets $\epsilon$ out of the divergence; where permittivity varies, or across two dielectrics, $\nabla^2V = -\rho/\epsilon$ is false — use $\nabla\cdot(\epsilon\nabla V) = -\rho$, or Gauss's law directly ([[concepts/static-fields-in-dielectrics|Static fields in dielectrics]]). *Piecewise* homogeneous (two layers): Laplace in each layer, stitched by the [[concepts/boundary-conditions|boundary conditions]].

With $V$ specified on the boundary the solution is **unique**: any function satisfying the equation and boundary values is *the* answer — guessing is legitimate. The equation is **linear**: solutions superpose.

> [!intuition] What the Laplacian measures
> $\nabla^2V$ at a point $\propto$ (average of $V$ over a small sphere around it) − (value at the point). So Laplace's equation says: **in a charge-free region, $V$ equals the average of $V$ around it** — no bumps, no dips; extremes lie on the boundary (why static fields alone cannot hold a charge in stable equilibrium). Positive charge makes $V$ curve *downward* ($\nabla^2V<0$: dome, $V$ above its local average); negative charge, upward (bowl). A peak or pit can occur only at charge, and curvature alone does not make one: the [[concepts/pn-junction|pn junction]] has $V''<0$ throughout its positive slab while $V$ rises to a plateau.

**One-dimensional solutions.** When $V$ depends on one coordinate, the PDE becomes an ODE integrated twice; two constants from two boundary values.

| symmetry | Laplace's equation | general solution | used for |
|---|---|---|---|
| planar, $V(z)$ | $\dfrac{d^2V}{dz^2} = 0$ | $V = Az + B$ | parallel plates |
| cylindrical, $V(r)$ | $\dfrac{1}{r}\dfrac{d}{dr}\Big(r\dfrac{dV}{dr}\Big) = 0$ | $V = A\ln r + B$ | coaxial cable |
| spherical, $V(r)$ | $\dfrac{1}{r^2}\dfrac{d}{dr}\Big(r^2\dfrac{dV}{dr}\Big) = 0$ | $V = \dfrac{A}{r} + B$ | concentric spheres |

> [!recipe] Laplace between conductors
> 1. **Symmetry:** the single coordinate $V$ depends on (infinite plates: $z$; long coax: $r$).
> 2. **Integrate twice** (table above): $V$ with two constants.
> 3. **Boundary values:** each conductor's potential fixes a constant ([[concepts/conductors|conductors]] are equipotentials).
> 4. $\mathbf{E} = -\nabla V$, then $\mathbf{D} = \epsilon\mathbf{E}$.
> 5. **Surface charges** $\rho_s = \hat{n}\cdot\mathbf{D}$, $\hat{n}$ out of the conductor into the field region (zero field inside).
>
> The chain $V\to\mathbf{E}\to\mathbf{D}\to\rho_s$ is the "given $V$" route to [[concepts/capacitance|capacitance]].

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 316" width="640" height="316" role="img" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:14px"><defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="context-stroke"/></marker><marker id="ahs" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="context-stroke"/></marker></defs><rect x="40.0" y="70.0" width="260.0" height="160.0" rx="0" fill="var(--accent)" fill-opacity="0.06" stroke="none"/><line x1="40.0" y1="230.0" x2="300.0" y2="230.0" stroke="currentColor" stroke-width="6" opacity="0.85" stroke-linecap="round"/><line x1="40.0" y1="70.0" x2="300.0" y2="70.0" stroke="currentColor" stroke-width="6" opacity="0.85" stroke-linecap="round"/><text x="62.0" y="248.0" text-anchor="middle" fill="var(--hi)" style="font-size:13px;">+</text><text x="94.0" y="248.0" text-anchor="middle" fill="var(--hi)" style="font-size:13px;">+</text><text x="126.0" y="248.0" text-anchor="middle" fill="var(--hi)" style="font-size:13px;">+</text><text x="158.0" y="248.0" text-anchor="middle" fill="var(--hi)" style="font-size:13px;">+</text><text x="190.0" y="248.0" text-anchor="middle" fill="var(--hi)" style="font-size:13px;">+</text><text x="222.0" y="248.0" text-anchor="middle" fill="var(--hi)" style="font-size:13px;">+</text><text x="254.0" y="248.0" text-anchor="middle" fill="var(--hi)" style="font-size:13px;">+</text><text x="286.0" y="248.0" text-anchor="middle" fill="var(--hi)" style="font-size:13px;">+</text><text x="62.0" y="62.0" text-anchor="middle" fill="var(--accent)" style="font-size:14px;">−</text><text x="94.0" y="62.0" text-anchor="middle" fill="var(--accent)" style="font-size:14px;">−</text><text x="126.0" y="62.0" text-anchor="middle" fill="var(--accent)" style="font-size:14px;">−</text><text x="158.0" y="62.0" text-anchor="middle" fill="var(--accent)" style="font-size:14px;">−</text><text x="190.0" y="62.0" text-anchor="middle" fill="var(--accent)" style="font-size:14px;">−</text><text x="222.0" y="62.0" text-anchor="middle" fill="var(--accent)" style="font-size:14px;">−</text><text x="254.0" y="62.0" text-anchor="middle" fill="var(--accent)" style="font-size:14px;">−</text><text x="286.0" y="62.0" text-anchor="middle" fill="var(--accent)" style="font-size:14px;">−</text><text x="305.0" y="234.0" text-anchor="start" fill="currentColor" style="font-size:12px;">z = 0,  V = 0</text><text x="305.0" y="74.0" text-anchor="start" fill="currentColor" style="font-size:12px;">z = d = 2 m,  V = −3 V</text><line x1="100.0" y1="216.0" x2="100.0" y2="84.0" stroke="var(--accent)" stroke-width="2.4" marker-end="url(#ah)" stroke-linecap="round"/><line x1="170.0" y1="216.0" x2="170.0" y2="84.0" stroke="var(--accent)" stroke-width="2.4" marker-end="url(#ah)" stroke-linecap="round"/><line x1="240.0" y1="216.0" x2="240.0" y2="84.0" stroke="var(--accent)" stroke-width="2.4" marker-end="url(#ah)" stroke-linecap="round"/><text x="184.0" y="150.0" text-anchor="start" fill="currentColor" style="font-size:12px;">E = +1.5 ẑ V/m</text><text x="170.0" y="40.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px;">E = 0 above</text><text x="170.0" y="268.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px;">E = 0 below</text><line x1="60.0" y1="228.0" x2="60.0" y2="200.0" stroke="currentColor" stroke-width="1.6" marker-end="url(#ah)" stroke-linecap="round"/><text x="48.0" y="210.0" text-anchor="end" fill="currentColor" style="font-size:12px;">n̂</text><line x1="60.0" y1="72.0" x2="60.0" y2="100.0" stroke="currentColor" stroke-width="1.6" marker-end="url(#ah)" stroke-linecap="round"/><text x="48.0" y="92.0" text-anchor="end" fill="currentColor" style="font-size:12px;">n̂</text><text x="170.0" y="300.0" text-anchor="middle" fill="currentColor" style="font-size:12px;">ρₛ(0) = +1.5 ε₀ ,   ρₛ(d) = −1.5 ε₀  [C/m²]</text><line x1="380.0" y1="200.0" x2="610.0" y2="200.0" stroke="currentColor" stroke-width="1.3" marker-end="url(#ahs)" stroke-linecap="round"/><text x="618.0" y="204.0" text-anchor="start" fill="currentColor" style="font-size:14px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">z</text><line x1="380.0" y1="270.0" x2="380.0" y2="110.0" stroke="currentColor" stroke-width="1.3" marker-end="url(#ahs)" stroke-linecap="round"/><text x="374.0" y="120.0" text-anchor="end" fill="currentColor" style="font-size:14px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">V</text><line x1="380.0" y1="200.0" x2="560.0" y2="260.0" stroke="var(--accent2)" stroke-width="2.6" stroke-linecap="round"/><line x1="560.0" y1="200.0" x2="560.0" y2="260.0" stroke="currentColor" stroke-width="1" stroke-dasharray="3 3" opacity="0.6" stroke-linecap="round"/><text x="566.0" y="192.0" text-anchor="start" fill="currentColor" style="font-size:11px;">d = 2 m</text><line x1="380.0" y1="260.0" x2="560.0" y2="260.0" stroke="currentColor" stroke-width="1" stroke-dasharray="3 3" opacity="0.6" stroke-linecap="round"/><text x="374.0" y="264.0" text-anchor="end" fill="currentColor" style="font-size:11px;">−3 V</text><text x="508.0" y="196.0" text-anchor="middle" fill="var(--accent2)" style="font-size:13px;font-weight:600;">V(z) = −1.5 z</text><text x="495.0" y="300.0" text-anchor="middle" fill="currentColor" style="font-size:12px;">slope dV/dz = −1.5 V/m  ⇒  E_z = +1.5 V/m</text></svg><figcaption><strong>Laplace's equation between two plates.</strong> With nothing but the plates to depend on, V = V(z), so ∇²V = d²V/dz² = 0 forces a straight line V = Az + B; the plate potentials fix A and B. The field is minus the slope, and points from the 0 V plate toward the −3 V plate. The plate charges follow from the boundary condition ρₛ = n̂·<b>D</b> with n̂ pointing out of each conductor into the gap.</figcaption></figure>

**With charge present.** Inside a charged region the integrations pick up $\rho$: integrate $V'' = -\rho/\epsilon$ twice ($V' = -E_x$ after the first) and match $V$ — and, where there is no surface charge, $\epsilon V'$ — at interfaces. Canonical case: the [[concepts/pn-junction|pn junction]], whose built-in potential is $V_{21} = \rho_2W_2(W_1+W_2)/2\epsilon_0$.

**General solution.** For finite charge with $V\to0$ at infinity, $V(\mathbf{r}) = \displaystyle\int\frac{\rho(\mathbf{r}')\,d^3\mathbf{r}'}{4\pi\epsilon_0\lvert\mathbf{r}-\mathbf{r}'\rvert}$: the point-charge potential is the impulse response (Green's function) of a linear, shift-invariant system, and any $\rho$ is a superposition of impulses. Its consequence, the [[concepts/helmholtz-theorem|Helmholtz theorem]], is treated there.

**Examples.**

> [!example] Example — parallel plates
> Infinite conducting plates $d = 2$ m apart in $z$; $z=0$ grounded, $z=d$ at $-3$ V. $V = V(z)$, $V''(z) = 0$ between (vacuum, no charge): $V = Az + B$. $V(0) = 0$ gives $B = 0$; $V(2) = -3$ gives $A = -\tfrac32$ V/m.
> $$
> V(z) = -\tfrac32 z\ \text{V},\qquad \mathbf{E} = -\nabla V = -\hat{z}\frac{dV}{dz} = +\tfrac32\,\hat{z}\ \text{V/m}\quad(0<z<2\ \text{m}).
> $$
> Uniform, from the 0 V plate toward the $-3$ V plate (high to low). In symbols, $V = V_0z/d$ and $\mathbf{E} = -(V_0/d)\hat{z}$ for a top plate at $V_0$.
>
> *Plate charges.* Outside, the field is zero (equal and opposite sheets cancel). Bottom plate, $\hat{n} = +\hat{z}$ into the gap: $\rho_s(0) = \hat{z}\cdot\epsilon_0\mathbf{E} = +\tfrac32\epsilon_0 \approx 1.3\times10^{-11}$ C/m². Top plate, $\hat{n} = -\hat{z}$: $\rho_s(d) = -\hat{z}\cdot\epsilon_0\mathbf{E} = -\tfrac32\epsilon_0$ C/m². Equal and opposite — so the sheets' fields also cancel *inside each metal plate*: zero field inside a conductor, an equipotential.

> [!example] Example — reading a potential difference off a surface charge
> Two copper blocks face each other across a 3 m gap in $x$; facing surfaces carry $\rho_s = +2$ C/m² (left, at $x=0$, $V=0$) and $-2$ C/m² (right). Find the right block's potential $V_p$.
>
> Inside copper $\mathbf{D} = 0$. At $x=0$, $\hat{n} = \hat{x}$ out of the left block: $\hat{x}\cdot(\mathbf{D}_{\text{gap}} - 0) = 2$, so $E_x = 2/\epsilon_0$ V/m, uniform. Drop across the gap $E_xd = 6/\epsilon_0$ V; $\mathbf{E}$ points high to low, so the right block is *lower*: $V_p = -6/\epsilon_0 \approx -6.8\times10^{11}$ V. (Absurd — 2 C/m² is enormous; real capacitors carry µC/m². The method is the point: $\mathbf{D}$ jump ⇒ $E$ ⇒ $\lvert\Delta V\rvert = Ed$ ⇒ sign from the direction of $\mathbf{E}$.)

Coax with $V(a)=V_0$, $V(b)=0$: $V = V_0\ln(b/r)/\ln(b/a)$ (worked on [[concepts/capacitance|Capacitance]]).

> [!trap] Where Laplace's equation may and may not be used
> - Only where $\rho = 0$ *inside* the region. Charge on the *bounding* conductors enters through boundary values; a charged sheet mid-gap splits the problem into two Laplace regions joined by a $\mathbf{D}$-jump ([[concepts/static-fields-in-dielectrics|Static fields in dielectrics]]).
> - Only where $\epsilon$ is constant. Two layers ⇒ two Laplace problems plus matching ($V$, $D_n$); graded $\epsilon$ ⇒ $\nabla\cdot\mathbf{D} = 0$ ⇒ $D_n$ constant.
> - The inverse use is as common on exams: $\rho = \epsilon\nabla\cdot\mathbf{E} = -\epsilon\nabla^2V$. Zero curl does not mean zero charge.

> [!exam] On exams
> Mostly *backwards*: $\rho = \epsilon_0\nabla\cdot\mathbf{E}$ from a field (FA26 1(c)), or $\rho = -\epsilon_0\nabla^2V$ from a potential. Forwards — integrate twice, constants from plate potentials — starts the layered dielectrics of [[concepts/static-fields-in-dielectrics|Static fields in dielectrics]], the capacitances of [[concepts/capacitance|Capacitance]], and HW3 #1 (vacuum diode, $V\propto x^{4/3}$). Know the three 1-D solutions cold; deriving $V = A\ln r + B$ under time pressure is where minutes go to die.

**Where it appears.** [[1-electrostatics/07-poisson-and-laplace#1-from-gausss-law-to-poissons-equation|Lecture 7 §1]] (derived), [[1-electrostatics/07-poisson-and-laplace#2-solving-laplaces-equation-in-one-dimension|§2]] (1-D solutions), [[1-electrostatics/07-poisson-and-laplace#3-poissons-equation-where-there-is-charge|§3]] (with charge); [[1-electrostatics/09-static-fields-in-dielectric-media#3-laplaces-equation-layer-by-layer|Lecture 9 §3]] (piecewise, and where it fails); [[1-electrostatics/10-capacitance-and-conductance#2-parallel-plates-both-ways|Lecture 10 §2–3]] (the given-$V$ route to capacitance); [[problems/curl-potential-and-charge-from-a-field|Worked problem — Curl, potential, and charge from a given field]] (the backwards use).

**Related.** [[concepts/electrostatic-potential|Electrostatic potential V]] · [[concepts/gauss-law|Gauss's law]] · [[concepts/divergence|Divergence]] · [[concepts/boundary-conditions|Boundary conditions at an interface]] · [[concepts/pn-junction|The pn junction]] · [[concepts/helmholtz-theorem|Helmholtz's theorem]].

**Practice.** [[practice/topics#poissons-and-laplaces-equations|Poisson's and Laplace's equations]] (14 problems) — for example [[practice/07-poisson-and-laplace#71-two-plates-two-potentials|7.1 Two plates, two potentials]] (easy), [[practice/07-poisson-and-laplace#76-coaxial-cable-by-laplace|7.6 Coaxial cable by Laplace]] (medium), [[practice/07-poisson-and-laplace#79-junction-with-an-intrinsic-layer|7.9 Junction with an intrinsic layer]] (hard).
