---
title: "The 5-step recipe for fields of charge distributions"
description: "Draw, chop, write dE of one piece, kill components by symmetry, integrate — the procedure for every superposition integral, the finite and infinite line charge worked through it, and when to abandon it for Gauss's law."
tags: [concept, electrostatics, exam-1]
aliases: ["5-step program", "superposition integral recipe", "finite line charge", "infinite line charge", "continuous charge distribution"]
---

> [!key] Superposition as an integral
> Charge on a line ($\rho_l$, C/m), surface ($\rho_s$, C/m²) or volume ($\rho$, C/m³): superposition becomes an integral over pieces $dQ = \rho_l\,dl = \rho_s\,dS = \rho\,dV$:
> $$
> \mathbf{E}(\mathbf{r}) = \frac{1}{4\pi\epsilon_0}\int \frac{dQ'}{R^2}\,\hat{R},
> \qquad \hat{R} = \frac{\mathbf{r}-\mathbf{r}'}{|\mathbf{r}-\mathbf{r}'|},\ R = |\mathbf{r}-\mathbf{r}'| .
> $$

> [!recipe] The "patented 5-step program" (use it every time)
> 1. **Make a large, clear drawing.** Cross-sections if 3-D; coordinates matching the symmetry.
> 2. **Chop the charge into pieces** $dQ$ in terms of density and coordinate: $\rho_l\,dz$, $\rho_s\,r\,dr\,d\phi$, …
> 3. **Write $d\mathbf{E}$ of one piece**: $d\mathbf{E} = \dfrac{dQ}{4\pi\epsilon_0R^2}\hat{R}$, with $\hat{R}$ (source → field point) and $R$ in your coordinates.
> 4. **Use symmetry** to find components that cancel between mirror-image pieces; keep the survivor (a scalar integral) along a direction that is *fixed at the field point*.
> 5. **Integrate.**
>
> Students skip step 4 — the one that turns a 3-D vector integral into a 1-D scalar one.

**Physics.** Step 4 converts a vector integral with a direction that changes from piece to piece into a scalar integral times a fixed unit vector. Without it you must resolve $\hat{R}$ into Cartesian components and integrate each — legal, but three times the work.

**Examples.**

> [!example] Lecture 2 §4 — finite line charge → infinite line charge
> A uniform line charge $\rho_l$ occupies $-a<z<a$ on the $z$-axis. Find $\mathbf{E}$ at a point in the $z=0$ plane, a distance $r$ from the axis.
>
> 1. *Drawing / coordinates.* Cylindrical $(r,\phi,z)$; the field point is $(r, \phi, 0)$.
> 2. *Pieces.* $dQ = \rho_l\,dz$ at height $z$.
> 3. *One piece.* $R = \sqrt{r^2+z^2}$; $d\mathbf{E} = \dfrac{\rho_l\,dz}{4\pi\epsilon_0(r^2+z^2)}\hat{R}$, $\hat{R}$ from element to $P$ at angle $\alpha$ to the horizontal, $\cos\alpha = r/R$.
> 4. *Symmetry.* The element at $-z$ mirrors $d\mathbf{E}$: $z$-components cancel, radial ones add. Only $dE_r = dE\cos\alpha$ survives, and $\hat{r}$ at $P$ is *fixed* (set by $\phi$ of $P$, not $z$ of the source), so it comes outside.
> 5. *Integrate.*
>
> $$
> E_r = \frac{\rho_l}{4\pi\epsilon_0}\int_{-a}^{a}\frac{r\,dz}{(r^2+z^2)^{3/2}} .
> $$
> Substitute $z = r\tan\alpha$, $dz = r\sec^2\alpha\,d\alpha$, $r^2+z^2 = r^2\sec^2\alpha$:
> $$
> E_r = \frac{\rho_l}{4\pi\epsilon_0 r}\int_{-\alpha_0}^{\alpha_0}\cos\alpha\,d\alpha
>     = \frac{\rho_l}{4\pi\epsilon_0 r}\,2\sin\alpha_0
>     = \frac{\rho_l}{4\pi\epsilon_0 r}\,\frac{2a}{\sqrt{a^2+r^2}} .
> $$

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 330" width="640" height="330" role="img" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:14px"><defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="context-stroke"/></marker><marker id="ahs" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="context-stroke"/></marker></defs><line x1="150.0" y1="310.0" x2="150.0" y2="20.0" stroke="currentColor" stroke-width="1.2" marker-end="url(#ahs)" opacity="0.7" stroke-linecap="round"/><text x="146.0" y="16.0" text-anchor="end" fill="currentColor" style="font-size:15px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">z</text><line x1="150.0" y1="260.0" x2="150.0" y2="70.0" stroke="var(--hi)" stroke-width="5" stroke-linecap="round"/><text x="139.0" y="257.0" text-anchor="middle" fill="var(--hi)" style="font-size:12px;">+</text><text x="139.0" y="235.0" text-anchor="middle" fill="var(--hi)" style="font-size:12px;">+</text><text x="139.0" y="213.0" text-anchor="middle" fill="var(--hi)" style="font-size:12px;">+</text><text x="139.0" y="191.0" text-anchor="middle" fill="var(--hi)" style="font-size:12px;">+</text><text x="139.0" y="169.0" text-anchor="middle" fill="var(--hi)" style="font-size:12px;">+</text><text x="139.0" y="147.0" text-anchor="middle" fill="var(--hi)" style="font-size:12px;">+</text><text x="139.0" y="125.0" text-anchor="middle" fill="var(--hi)" style="font-size:12px;">+</text><text x="139.0" y="103.0" text-anchor="middle" fill="var(--hi)" style="font-size:12px;">+</text><text x="139.0" y="81.0" text-anchor="middle" fill="var(--hi)" style="font-size:12px;">+</text><text x="120.0" y="70.0" text-anchor="end" fill="currentColor" style="font-size:12px;">z = a</text><text x="120.0" y="265.0" text-anchor="end" fill="currentColor" style="font-size:12px;">z = −a</text><text x="110.0" y="169.0" text-anchor="end" fill="var(--hi)" style="font-size:13px;">ρₗ [C/m]</text><line x1="150.0" y1="165.0" x2="470.0" y2="165.0" stroke="currentColor" stroke-width="1.2" stroke-dasharray="5 5" opacity="0.6" stroke-linecap="round"/><text x="310.0" y="183.0" text-anchor="middle" fill="currentColor" style="font-size:15px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">r</text><circle cx="470.0" cy="165.0" r="4.0" fill="currentColor" stroke="currentColor" stroke-width="1.5"/><text x="478.0" y="183.0" text-anchor="start" fill="currentColor" style="font-size:15px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">P</text><rect x="145.0" y="97.0" width="10.0" height="12.0" rx="0" fill="var(--accent)" stroke="none" stroke-width="1.5"/><text x="162.0" y="95.0" text-anchor="start" fill="var(--accent)" style="font-size:13px;">dQ = ρₗ dz</text><rect x="145.0" y="221.0" width="10.0" height="12.0" rx="0" fill="var(--accent2)" stroke="none" stroke-width="1.5"/><text x="162.0" y="245.0" text-anchor="start" fill="var(--accent2)" style="font-size:12px;">mirror element</text><line x1="150.0" y1="103.0" x2="470.0" y2="165.0" stroke="var(--accent)" stroke-width="1.6" stroke-linecap="round"/><line x1="150.0" y1="227.0" x2="470.0" y2="165.0" stroke="var(--accent2)" stroke-width="1.6" stroke-dasharray="4 3" stroke-linecap="round"/><text x="290.0" y="126.0" text-anchor="middle" fill="var(--accent)" style="font-size:15px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">R</text><path d="M430,165.0 A40,40 0 0 0 430.7,157.4" fill="none" stroke="currentColor" stroke-width="1.2" stroke-linejoin="round" stroke-linecap="round"/><text x="418.0" y="153.0" text-anchor="middle" fill="currentColor" style="font-size:15px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">α</text><line x1="470.0" y1="165.0" x2="558.4" y2="182.1" stroke="var(--accent)" stroke-width="2.6" marker-end="url(#ah)" stroke-linecap="round"/><text x="568.4" y="188.1" text-anchor="start" fill="var(--accent)" style="font-size:15px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">dE</text><line x1="470.0" y1="165.0" x2="558.4" y2="165.0" stroke="var(--accent)" stroke-width="1.6" marker-end="url(#ah)" opacity="0.8" stroke-linecap="round"/><text x="520.2" y="181.0" text-anchor="middle" fill="var(--accent)" style="font-size:12px;">dEᵣ = dE cos α</text><line x1="558.4" y1="165.0" x2="558.4" y2="182.1" stroke="var(--accent)" stroke-width="1.2" stroke-dasharray="3 3" opacity="0.8" stroke-linecap="round"/><line x1="470.0" y1="165.0" x2="558.4" y2="147.9" stroke="var(--accent2)" stroke-width="2.2" marker-end="url(#ah)" opacity="0.9" stroke-linecap="round"/><text x="568.4" y="145.9" text-anchor="start" fill="var(--accent2)" style="font-size:13px;">dE′ (mirror)</text><text x="360.0" y="318.0" text-anchor="middle" fill="currentColor" style="font-size:13px;">z-components cancel in pairs → only the radial (r̂) part survives the integral</text></svg><figcaption><strong>Field of a finite line charge — the symmetry step of the 5-step recipe.</strong> Every element dQ at height z has a mirror element at −z. Their fields at P have equal magnitude; the z-components cancel and the radial components add, so only dE cos α needs integrating.</figcaption></figure>

> [!note] Infinite line charge
> Let $a\to\infty$: $\dfrac{2a}{\sqrt{a^2+r^2}}\to 2$, so
> $$
> \mathbf{E} = \frac{\rho_l}{2\pi\epsilon_0\, r}\,\hat{r}
> $$
> A line's field falls as $1/r$ — **not** $1/r^2$ — because charge farther along the line keeps contributing as you move away. ([[concepts/symmetric-charge-distributions|Gauss's law]] gets this in two lines; the cross-check is a course favourite.)

The slides' two "review at home" examples follow the same pattern: a **ring** of radius $a$, line charge $\rho_{l0}$ ($dQ = \rho_{l0}\,a\,d\phi$, total $2\pi a\rho_{l0}$); and a **charged rod** (charge $Q$ over length $L$ on the $x$-axis) acting on a point charge $q$ on that axis a distance $a$ beyond its end: $\mathbf{F} = \dfrac{qQ}{4\pi\epsilon_0\,a(L+a)}\hat{x}$, with $\hat{x}$ outside the integral because it is Cartesian. Two equal and opposite charges with the field point on their perpendicular bisector: double one contribution's surviving component ([[concepts/superposition|Superposition]]); on the dipole *axis* the contributions are collinear and must be subtracted instead.

**When to skip it.** If the distribution is spherically, cylindrically or planarly symmetric *and infinite/complete* (whole sphere, infinite line, infinite sheet), [[concepts/gauss-law|Gauss's law]] gives the same answer in four lines. Use the recipe when the symmetry is partial — a finite rod, a ring, a disk, a dipole — or when you need the field somewhere the Gaussian trick doesn't reach.

The same five steps compute magnetic fields with $d\mathbf{B} = \mu_0I\,d\mathbf{l}\times\hat R/(4\pi R^2)$ in place of $d\mathbf{E}$ — [[2-magnetostatics/12-magnetic-force-biot-savart-and-amperes-law|Lecture 12]] runs them for the straight wire ([[concepts/biot-savart-law|Biot–Savart law]]).

> [!trap] Unit vectors are constant only in Cartesian coordinates
> $\hat{x}$ can be pulled out of an integral; $\hat{r}$ and $\hat{\phi}$ change direction from point to point and **cannot**. Resolve them into Cartesian components first, or use symmetry so the surviving component is along a *fixed* direction at the field point. See [[0-toolkit/01-coordinates-and-differential-elements|Coordinates and differential elements]].

> [!exam] On exams
> Coulomb integrals are homework; the exam prefers the Gauss shortcut where symmetry allows (FA26 problems 2 and 4). Know the finite-line result and its $a\to\infty$ limit, and why $\hat{r}$ may leave the integral but $\hat{R}$ may not.

**Where it appears.** [[1-electrostatics/02-coulombs-law-superposition-and-gauss#4-continuous-distributions--the-5-step-program|Lecture 2 §4]]; homework 1–2; [[1-electrostatics/05-curl-free-fields-and-the-electrostatic-potential|Lecture 5]] repeats it for the potential (a scalar integral from the start — even easier).

**Related.** [[concepts/superposition|Superposition]] · [[concepts/coulombs-law|Coulomb's law]] · [[concepts/charge-density|Charge densities and δ-functions]] · [[concepts/symmetric-charge-distributions|Symmetric charge distributions]] · [[concepts/biot-savart-law|Biot–Savart law]].

**Practice.** [[practice/topics#continuous-charge-and-the-five-step-program|Continuous charge and the five-step program]] (5 problems) — for example [[practice/02-coulombs-law-superposition-and-gauss#26-ring-of-charge-on-its-axis|2.6 Ring of charge on its axis]] (medium), [[practice/02-coulombs-law-superposition-and-gauss#29-finite-line-charge-at-any-point|2.9 Finite line charge at any point]] (hard).
