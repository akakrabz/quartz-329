---
title: "Differential elements dl, dS, dV"
description: "The tiny vectors every line and surface integral is built from; tangent for dl, normal (outward on closed surfaces) for dS, and the cross-product rule that sets orientation."
tags: [concept, toolkit]
aliases: ["dl", "dS", "differential length", "differential surface", "line integral", "surface integral"]
---

> [!key] Definitions
> **Differential length vector** $d\mathbf{l}$: an infinitesimal step along a curve, *always tangent* to it. Cartesian:
> $$
> d\mathbf{l} = \hat{x}\,dx + \hat{y}\,dy + \hat{z}\,dz .
> $$
> **Differential surface vector** $d\mathbf{S}$: a surface patch as a vector *normal* to it, magnitude = area. Zoomed in, any patch is flat, so two tangent steps build it:
> $$
> d\mathbf{S} = d\mathbf{l}_1\times d\mathbf{l}_2 .
> $$
> On a **closed** surface $d\mathbf{S}$ points **outward**. $dV$: an infinitesimal volume, $dx\,dy\,dz$ in Cartesian.

**Physics.** The integral-form Maxwell equations are line or surface integrals of these small vectors.

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 300" width="640" height="300" role="img" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:14px"><defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="context-stroke"/></marker><marker id="ahs" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="context-stroke"/></marker></defs><text x="130.0" y="35.0" text-anchor="middle" fill="currentColor" style="font-size:13px;">dl is always tangent to the path</text><path d="M40,230 C80,100 160,260 240,120" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/><line x1="65.3" y1="184.5" x2="91.3" y2="162.6" stroke="var(--accent)" stroke-width="2.2" marker-end="url(#ah)" stroke-linecap="round"/><line x1="125.0" y1="178.8" x2="158.5" y2="184.7" stroke="var(--accent)" stroke-width="2.2" marker-end="url(#ah)" stroke-linecap="round"/><line x1="197.0" y1="169.9" x2="225.5" y2="151.4" stroke="var(--accent)" stroke-width="2.2" marker-end="url(#ah)" stroke-linecap="round"/><text x="143.0" y="208.8" text-anchor="middle" fill="var(--accent)" style="font-size:15px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">dl</text><text x="34.0" y="238.0" text-anchor="end" fill="currentColor" style="font-size:13px;">P₁</text><text x="246.0" y="118.0" text-anchor="start" fill="currentColor" style="font-size:13px;">P₂</text><text x="140.0" y="275.0" text-anchor="middle" fill="currentColor" style="font-size:13px;">Cartesian: dl = x̂ dx + ŷ dy + ẑ dz</text><line x1="430.0" y1="190.0" x2="525.0" y2="190.0" stroke="currentColor" stroke-width="1.1" stroke-dasharray="4 4" opacity="0.6" stroke-linecap="round"/><line x1="430.0" y1="190.0" x2="430.0" y2="95.0" stroke="currentColor" stroke-width="1.1" stroke-dasharray="4 4" opacity="0.6" stroke-linecap="round"/><line x1="430.0" y1="190.0" x2="377.8" y2="223.2" stroke="currentColor" stroke-width="1.1" stroke-dasharray="4 4" opacity="0.6" stroke-linecap="round"/><polygon points="377.8,223.2 472.8,223.2 472.8,128.2 377.8,128.2" fill="var(--accent)" fill-opacity="0.18" stroke="currentColor" stroke-width="1.4" stroke-linejoin="round"/><polygon points="525.0,190.0 472.8,223.2 472.8,128.2 525.0,95.0" fill="var(--accent2)" fill-opacity="0.18" stroke="currentColor" stroke-width="1.4" stroke-linejoin="round"/><polygon points="430.0,95.0 377.8,128.2 472.8,128.2 525.0,95.0" fill="var(--muted)" fill-opacity="0.18" stroke="currentColor" stroke-width="1.4" stroke-linejoin="round"/><line x1="425.2" y1="175.8" x2="396.5" y2="194.0" stroke="var(--accent)" stroke-width="2.4" marker-end="url(#ah)" stroke-linecap="round"/><line x1="498.9" y1="159.1" x2="551.1" y2="159.1" stroke="var(--accent2)" stroke-width="2.4" marker-end="url(#ah)" stroke-linecap="round"/><line x1="451.4" y1="111.6" x2="451.4" y2="59.4" stroke="currentColor" stroke-width="2.4" marker-end="url(#ah)" stroke-linecap="round"/><text x="386.5" y="216.0" text-anchor="middle" fill="currentColor" style="font-size:12px;">dS = x̂ dy dz</text><text x="555.1" y="163.1" text-anchor="start" fill="currentColor" style="font-size:12px;">dS = ŷ dz dx</text><text x="451.4" y="53.4" text-anchor="middle" fill="currentColor" style="font-size:12px;">dS = ẑ dx dy</text><text x="425.2" y="239.2" text-anchor="middle" fill="currentColor" style="font-size:12px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">dy</text><text x="484.8" y="179.8" text-anchor="start" fill="currentColor" style="font-size:12px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">dz</text><text x="389.9" y="208.6" text-anchor="middle" fill="currentColor" style="font-size:12px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">dx</text><text x="440.0" y="292.0" text-anchor="middle" fill="currentColor" style="font-size:13px;">closed surface: every dS points outward</text></svg><figcaption><strong>The two new objects of Lecture 1.</strong> Left: the differential length vector d<b>l</b> is tangent to the path and changes direction along it. Right: a differential surface vector d<b>S</b> is normal to the surface; for a closed surface the convention is <em>outward</em>. Its direction comes from the order of the cross product of two tangent vectors (swap the order and it flips).</figcaption></figure>

- $\int_{P_1}^{P_2}\mathbf{F}\cdot d\mathbf{l}$ adds up the *tangential* component of $\mathbf{F}$ along the path — the work done by a force field from $P_1$ to $P_2$ (the slides' "walking through a river"; a step perpendicular to the flow costs nothing). It goes into Faraday's law and, in Lecture 5, defines voltage ([[concepts/electrostatic-potential|Electrostatic potential V]]). The closed-loop version $\oint_C$ is a **circulation** ([[concepts/conservative-field|Conservative (curl-free) fields and the potential]]).
- $\int_S\mathbf{F}\cdot d\mathbf{S}$ adds up the *normal* component — how much field "pokes through": the **flux** ([[concepts/flux|Flux]]). Closed version $\oint_S$ = flux out ([[concepts/gauss-law|Gauss's law]]).
- $\int_V f\,dV$ adds up a density: total charge from $\rho$ ([[concepts/charge-density|Charge densities and δ-functions]]).

**Orientation rules.**
- Closed surface: outward, no choice.
- Open surface with boundary curve $C$: right-hand rule — fingers along $d\mathbf{l}$ of $C$, thumb along $d\mathbf{S}$. This links the two sides of [[concepts/stokes-theorem|Stokes' theorem]]. Without a boundary in play, *choose* a normal and stick with it.
- Path integrals: $d\mathbf{l}$ follows the direction of travel from the start point to the end point; reversing the path negates the integral. Write $d\mathbf{l} = \hat{x}\,dx$ (plus sign) and let the *limits* carry the direction.

> [!trap] The order of the cross product is the orientation
> $d\mathbf{l}_1\times d\mathbf{l}_2$ and $d\mathbf{l}_2\times d\mathbf{l}_1$ are opposite normals. The six faces of a Cartesian box have
> $$
> d\mathbf{S} = \pm\hat{x}\,dy\,dz,\quad \pm\hat{y}\,dz\,dx,\quad \pm\hat{z}\,dx\,dy ,
> $$
> with the sign fixed by "outward". A wrong sign silently flips a flux — see the [[problems/flux-through-a-plane-from-two-charges|flux-through-a-plane problem]].

**In other coordinate systems** $d\mathbf{l}$ picks up metric factors ($r\,d\phi$, $r\sin\theta\,d\phi$) and $d\mathbf{S}$ on a sphere is $\hat{r}\,r^2\sin\theta\,d\theta\,d\phi$ — tabulated in [[0-toolkit/01-coordinates-and-differential-elements|Coordinates and differential elements]].

> [!exam] On exams
> Nothing is asked "about $d\mathbf{l}$", but every problem uses it: $d\mathbf{l}$ in a line integral (Exam 1, problem 1d), outward $d\mathbf{S}$ on a Gaussian surface (problems 2 and 4), and units on every answer. Missing units cost more marks than missing physics.

**Where it appears.** [[1-electrostatics/01-fields-forces-and-the-maxwell-roadmap#5-the-two-new-tools-dl-and-ds|Lecture 1 §5]] introduces them; [[concepts/flux|Flux]], [[concepts/gauss-law|Gauss's law]], [[concepts/stokes-theorem|Stokes' theorem]] use them.

**Related.** [[concepts/flux|Flux]] · [[concepts/gauss-law|Gauss's law]] · [[concepts/stokes-theorem|Stokes' theorem]] · [[concepts/divergence-theorem|Divergence theorem]] · [[0-toolkit/01-coordinates-and-differential-elements|Coordinates and differential elements]].
