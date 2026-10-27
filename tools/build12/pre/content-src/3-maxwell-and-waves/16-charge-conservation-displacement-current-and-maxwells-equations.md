---
title: "Lecture 16 — Charge conservation, displacement current, and Maxwell's equations"
description: "Charge conservation, ∇·J = −∂ρ/∂t, contradicts static Ampère's law wherever charge piles up; Maxwell's repair ∇×H = J + ∂D/∂t makes its divergence the continuity equation and completes the four equations, with ∇·B = 0 following from Faraday's law plus the absence of magnetic charge. The four boundary conditions hold for time-varying fields too, including Bₙ continuous and Hₜ jumping by the surface current."
tags: [lecture, waves]
lecture: 16
---

*Lecture 16 · course notes §16 · slides "Conservation of Charge / Boundary Conditions" (the displacement current itself is on the Lecture 13 deck) · prev: [[2-magnetostatics/15-inductance-magnetic-energy-and-the-potentials|Lecture 15]] · next: [[3-maxwell-and-waves/17-magnetization-and-maxwells-equations-in-matter|Lecture 17]] · practice: [[practice/16-charge-conservation-and-displacement-current|12 problems]]*

> [!abstract] In one breath
> Charge inside any volume changes only by current crossing its boundary: $\oint\mathbf{J}\cdot d\mathbf{S} = -dQ/dt$, or $\nabla\cdot\mathbf{J} = -\partial\rho/\partial t$ — the **continuity equation**. The divergence of static Ampère, $\nabla\times\mathbf{H} = \mathbf{J}$, is identically zero on the left, so it insists $\nabla\cdot\mathbf{J} = 0$ — false wherever charge accumulates (a charging capacitor, a draining sphere, any antenna). Maxwell's 1861 repair adds the **displacement current** $\partial\mathbf{D}/\partial t$, whose divergence is $\partial\rho/\partial t$ by Gauss's law, turning the contradiction into the continuity equation. That term closes the system and predicts electromagnetic waves (Hertz, 1888). The four boundary conditions carry over unchanged.

## 1. Charge conservation and the continuity equation

<!-- fig:continuity-bucket -->

Charge is made or removed only in $\pm$ pairs: photoionization (neutral atom → free ion + free electron) and recombination; pair creation and electron–positron annihilation at higher energy. So a change in $Q_V = \int_V\rho\,dV$ in a fixed volume must be carried across the bounding surface $S$ by a current.

Take two open surfaces $S_1$ (below) and $S_2$ (above) on the same rim, enclosing $V$, both with $d\mathbf{S}$ "upward": $I_1 = \int_{S_1}\mathbf{J}\cdot d\mathbf{S}_1$ enters through the bottom, $I_2 = \int_{S_2}\mathbf{J}\cdot d\mathbf{S}_2$ leaves through the top, so $dQ_V/dt = I_1 - I_2$. With the **outward** normal on $S = S_1\cup S_2$ (flipping the sign on $S_1$):

> [!key] Continuity equation
> $$
> \oint_S\mathbf{J}\cdot d\mathbf{S} = -\frac{dQ_V}{dt} = -\frac{d}{dt}\int_V\rho\,dV\qquad\Longleftrightarrow\qquad \nabla\cdot\mathbf{J} = -\frac{\partial\rho}{\partial t},
> $$
> the second by the divergence theorem ([[1-electrostatics/04-divergence-and-curl|Lecture 4]]), "true for every $V$". Net current **out** = rate of **decrease** of enclosed charge; where current lines diverge, charge is being depleted. It is charge conservation, nothing more and nothing less.

> [!example] Example (slides) — rate of decrease of charge in a unit cube
> $\mathbf{J} = (x, y, z)$ A/m² in the cube $0<x,y,z<1$ m. $\nabla\cdot\mathbf{J} = 1+1+1 = 3$ A/m³, so $-dQ/dt = \int_V\nabla\cdot\mathbf{J}\,dV = 3$ A: the charge inside *decreases* at 3 C/s. Face by face: $J_x = 1$ on $x = 1$, $0$ on $x = 0$, so 1 A leaves through the $x$ faces; likewise $y$, $z$ — 3 A out ✓. The underlined word is *decrease*; the sign is the point.

The equation has been at work already. [[1-electrostatics/08-conductors-dielectrics-and-polarization|Lecture 8]]: with $\mathbf{J} = \sigma\mathbf{E}$ and Gauss, $\partial\rho/\partial t = -(\sigma/\epsilon)\rho$ — the relaxation time $\epsilon/\sigma$. [[2-magnetostatics/13-current-sheets-solenoids-and-the-vector-potential|Lecture 13]]: its static case $\nabla\cdot\mathbf{J} = 0$ makes the Coulomb-gauge solution of $\nabla^2\mathbf{A} = -\mu_0\mathbf{J}$ consistent. [[1-electrostatics/10-capacitance-and-conductance|Lecture 10]]: the lossy capacitor's $I = C\,dV/dt + GV$ is continuity for one plate's charge — current in minus leakage out equals $dQ/dt$.

## 2. The asymmetry, and Maxwell's displacement current

Faraday has a changing $\mathbf{B}$ inducing $\mathbf{E}$; Ampère as written, $\nabla\times\mathbf{H} = \mathbf{J}$, has no converse. Beyond the asymmetry, Maxwell saw an inconsistency: the divergence of a curl is identically zero (the identity behind $\nabla\cdot\mathbf{B} = 0$ for $\mathbf{B} = \nabla\times\mathbf{A}$), so the static law forces $\nabla\cdot\mathbf{J} = 0$ always, contradicting continuity wherever $\partial\rho/\partial t\neq0$. His repair:

> [!key] Ampère–Maxwell equation
> $$
> \nabla\times\mathbf{H} = \mathbf{J} + \frac{\partial\mathbf{D}}{\partial t}\qquad\Longleftrightarrow\qquad \oint_C\mathbf{H}\cdot d\mathbf{l} = \int_S\Big(\mathbf{J}+\frac{\partial\mathbf{D}}{\partial t}\Big)\cdot d\mathbf{S}.
> $$
> $\partial\mathbf{D}/\partial t$ is the **displacement current density** [A/m²]; through a surface, $I_d = \dfrac{d}{dt}\int_S\mathbf{D}\cdot d\mathbf{S} = d\psi_E/dt$, the rate of change of electric flux, in amperes. **Verification:** the divergence gives $0 = \nabla\cdot\mathbf{J} + \dfrac{\partial}{\partial t}\nabla\cdot\mathbf{D} = \nabla\cdot\mathbf{J} + \dfrac{\partial\rho}{\partial t}$ by Gauss's law (assumed, as Maxwell did, to hold for time-varying fields) — the continuity equation. Charge conservation *requires* the term.

> [!intuition] What the displacement current is
> In matter, $\partial\mathbf{D}/\partial t = \epsilon_0\,\partial\mathbf{E}/\partial t + \partial\mathbf{P}/\partial t$. The second piece is the **polarization current** of [[1-electrostatics/11-lorentz-drude-models-for-conductivity-and-susceptibility#5-polarization-current-bound-charges-that-carry-an-ac-current|Lecture 11]] — bound charges really moving. The first exists in empty space with no charges moving: a genuinely new source of magnetic field, and what lets a wave cross vacuum — changing $\mathbf{E}$ makes $\mathbf{H}$, changing $\mathbf{H}$ makes $\mathbf{E}$, and the pair runs off at $1/\sqrt{\mu_0\epsilon_0} = c$. Hertz's waves (around 1888) confirmed the term.

<!-- fig:displacement-current-hemisphere -->

> [!example] Example (slides) — MMF around a draining point charge
> A point charge $Q(t)$ at the origin drains through a wire along $+z$, $I = -dQ/dt$. Find $\oint_C\mathbf{H}\cdot d\mathbf{l}$ (the MMF) around a circle of radius $a$ in $z = 0$, counter-clockwise seen from $+z$. Any surface on $C$ will do; the hint: a sphere and a hemisphere.
> - **Dome above** (pierced by the wire; normal consistent with $C$): conduction $+I$; the whole sphere carries flux $Q$ (Gauss), the dome $Q/2$: displacement $\dfrac{d}{dt}\dfrac Q2 = -\dfrac I2$. MMF $= I - I/2 = I/2$.
> - **Bowl below** (no wire): conduction 0; its flux, oriented from $C$, is $-Q/2$: displacement $+I/2$. MMF $= I/2$ again.
>
> Static Ampère would give $I$ for the dome and $0$ for the bowl: a circulation that depends on the imagined surface, which is absurd. $I/2$ is also Biot–Savart for a semi-infinite wire ending at the origin ($H_\phi = I/4\pi a$ in the plane of its end). Textbook version, the charging capacitor: a surface through the wire sees $I$, one through the gap sees $d\psi_E/dt = dQ/dt = I$.

> [!example] Example (slides) — displacement current through an area
> $\mathbf{E} = E_0\,t\,e^{-t^2}\hat z$ in free space; $A = 0.1$ m² in the $xy$-plane, $d\mathbf{S} = \hat z\,dS$. $\psi_E = \int\mathbf{D}\cdot d\mathbf{S} = \epsilon_0AE_0\,te^{-t^2}$ [C], so $I_d = d\psi_E/dt = \epsilon_0AE_0(1-2t^2)e^{-t^2}$ [A], $\epsilon_0A = 8.85\times10^{-13}$ F. It reverses sign at $t = 1/\sqrt2$ s, when the field stops growing. Units: $\epsilon_0$ [F/m] × area [m²] × $E$ [V/m] / time [s] = F·V/s = C/s = A ✓.

## 3. Maxwell's equations, complete

> [!key] Maxwell's equations (differential form, as the notes list them)
> $$
> \begin{gathered}
> \nabla\cdot\mathbf{D} = \rho\ \ (\text{Gauss}),\qquad \nabla\cdot\mathbf{B} = 0,\\[4pt]
> \nabla\times\mathbf{E} = -\frac{\partial\mathbf{B}}{\partial t}\ \ (\text{Faraday}),\qquad \nabla\times\mathbf{H} = \mathbf{J}+\frac{\partial\mathbf{D}}{\partial t}\ \ (\text{Ampère–Maxwell}),
> \end{gathered}
> $$
> with $\mathbf{D} = \epsilon_0\mathbf{E}$, $\mathbf{B} = \mu_0\mathbf{H}$ if $\rho$ and $\mathbf{J}$ include *all* charges and currents, bound and free (microscopic form, valid down to about the Compton wavelength); or $\mathbf{D} = \epsilon\mathbf{E}$, $\mathbf{B} = \mu\mathbf{H}$ with only the *free* $\rho$, $\mathbf{J}$ (macroscopic form, Lecture 17). Integral forms: $\oint_S\mathbf{D}\cdot d\mathbf{S} = Q_{\text{enc}}$, $\oint_S\mathbf{B}\cdot d\mathbf{S} = 0$, $\oint_C\mathbf{E}\cdot d\mathbf{l} = -\int_S\partial_t\mathbf{B}\cdot d\mathbf{S}$, $\oint_C\mathbf{H}\cdot d\mathbf{l} = \int_S(\mathbf{J}+\partial_t\mathbf{D})\cdot d\mathbf{S}$, plus the Lorentz force for what the fields do.

The destination announced in [[1-electrostatics/01-fields-forces-and-the-maxwell-roadmap|Lecture 1]]: Lectures 2–13 built the static pieces, [[2-magnetostatics/14-faradays-law-and-induced-emf|Lecture 14]] replaced $\nabla\times\mathbf{E} = 0$ by Faraday, this lecture replaces $\nabla\times\mathbf{H} = \mathbf{J}$ by Ampère–Maxwell. The rest of the course — waves, Poynting, phasors, reflection, transmission lines — is these four equations plus constitutive relations and boundary conditions, no new physics.

**The unnamed equation.** $\nabla\cdot\mathbf{B} = 0$ is not independent like the others. The divergence of Faraday's law gives $0 = \nabla\cdot(\nabla\times\mathbf{E}) = -\dfrac{\partial}{\partial t}\nabla\cdot\mathbf{B}$: $\nabla\cdot\mathbf{B}$ is **constant in time** at every point. Zero for the static fields of Lectures 12–13, it stays zero when fields vary. Physically: no magnetic charge. Monopoles would make $\nabla\cdot\mathbf{B}$ their density, with $\mathbf{B}$-lines starting and ending on them; none has been observed at any scale or any epoch accessible to astronomy.

> [!key] The canonical fields, in one table (the slide's review, plus the solenoid sketched beside it)
> | source | field | from |
> |---|---|---|
> | point charge $Q$ | $\mathbf{E} = \dfrac{Q}{4\pi\epsilon_0R^2}\hat R$ | Coulomb / Gauss on a sphere |
> | line charge $\rho_l$ | $\mathbf{E} = \dfrac{\rho_l}{2\pi\epsilon_0r}\hat r$ | Gauss on a cylinder |
> | sheet charge $\rho_s$ | $\mathbf{E} = \dfrac{\rho_s}{2\epsilon_0}(\pm\hat n)$ | Gauss on a pillbox |
> | line current $I$ | $\mathbf{B} = \dfrac{\mu_0I}{2\pi r}\hat\phi$ | Ampère on a circle |
> | sheet current $\mathbf{J}_s$ | $\mathbf{B} = \dfrac{\mu_0}{2}\mathbf{J}_s\times\hat n$ | Ampère on a rectangle |
> | solenoid $nI$ | $\mathbf{B} = \mu_0nI\hat z$ inside | Ampère on a rectangle |
>
> Units 1–2 in one rule: pick the symmetric surface or loop, count the enclosed source.

## 4. Boundary conditions — "same for dynamics"

<!-- fig:pec-boundary-fields -->

> [!key] The four boundary conditions ($\hat n$ from medium 2 into medium 1; the notes' $\pm$ superscripts mean the same)
> $$
> \begin{gathered}
> \hat n\cdot(\mathbf{D}_1-\mathbf{D}_2) = \rho_s,\qquad \hat n\cdot(\mathbf{B}_1-\mathbf{B}_2) = 0,\\[4pt]
> \hat n\times(\mathbf{E}_1-\mathbf{E}_2) = 0,\qquad \hat n\times(\mathbf{H}_1-\mathbf{H}_2) = \mathbf{J}_s .
> \end{gathered}
> $$
> They hold for time-varying fields exactly as for static ones. The first and third come from [[1-electrostatics/06-circulation-and-boundary-conditions|Lecture 6]]; the second is $\oint\mathbf{B}\cdot d\mathbf{S} = 0$ on a vanishing pillbox (no magnetic charge, no jump); the fourth is Ampère–Maxwell on a thin rectangle straddling the interface — the $\partial\mathbf{D}/\partial t$ flux vanishes with the width $w$, as the $\partial\mathbf{B}/\partial t$ flux did in Lecture 6, and only a *surface* current $\mathbf{J}_s$ survives (the notes defer the detailed justification to Lecture 19). [[2-magnetostatics/13-current-sheets-solenoids-and-the-vector-potential|Lecture 13]]'s current sheet is the fourth condition in action: $\mathbf{H}$ jumps by $J_s$.

Two special cases carry most of the course from here:

- **Two perfect dielectrics** ($\sigma = 0$, so $\mathbf{J}_s = 0$; no free charge, so $\rho_s = 0$): $D_n$, $E_t$, $B_n$, $H_t$ all continuous. The fields still refract ([[1-electrostatics/09-static-fields-in-dielectric-media|Lecture 9]]): $E_n$ and $D_t$ change by the permittivity ratio where $\epsilon_1\neq\epsilon_2$. With different permeabilities, $B = \mu H$ turns continuity of $B_n$ into $\mu_1H_{1n} = \mu_2H_{2n}$ — twin of $\epsilon_1E_{1n} = \epsilon_2E_{2n}$, in ink on the slide and taken up in [[3-maxwell-and-waves/17-magnetization-and-maxwells-equations-in-matter|Lecture 17]].
- **Surface of a perfect conductor** (medium 2, $\sigma\to\infty$, $\mathbf{E} = 0$ inside): Faraday inside gives $\partial\mathbf{B}/\partial t = -\nabla\times\mathbf{E} = 0$, so no *time-varying* $\mathbf{B}$ exists in it either — the class's reason for setting $\mathbf{H} = 0$ inside. Then $E_{1t} = 0$ and $B_{1n} = 0$: $\mathbf{E}$ meets the surface *normally* and ends on $\rho_s = \hat n\cdot\mathbf{D}_1$; $\mathbf{H}$ runs *tangentially*, carried by $\mathbf{J}_s = \hat n\times\mathbf{H}_1$, equivalently $\mathbf{H}_{1t} = \mathbf{J}_s\times\hat n$. (A typed slide's "$D_{1n} = \rho$" means $\rho_s$.)

> [!example] Two slide exercises (worked in class)
> *Surface charge from $\mathbf{D}$ on a conductor.* (a) $\mathbf{D} = D_0\langle1,-2,2\rangle$ pointing *away* from the surface: $\hat n$ (out of the conductor) is $\langle1,-2,2\rangle/3$, so $\rho_s = \hat n\cdot\mathbf{D} = D_0(1+4+4)/3 = 3D_0$. (b) $\mathbf{D} = D_0\langle1,0,\sqrt3\rangle$ pointing *toward* the surface: $\hat n = -\langle1,0,\sqrt3\rangle/2$ and $\rho_s = -2D_0$ — negative charge, field lines ending on it. Shortcut: $\mathbf{D}$ pointing away gives $\rho_s = \lvert\mathbf{D}\rvert$; pointing in, $\rho_s = -\lvert\mathbf{D}\rvert$.
> *Which pictures are possible just outside a perfect conductor?* An oblique arrow: neither $\mathbf{E}$ nor $\mathbf{H}$. A tangential arrow: $\mathbf{H}$ only ($B_{1n} = 0$, $\hat n\times\mathbf{H}_1 = \mathbf{J}_s$). A normal arrow: $\mathbf{E}$ only ($E_{1t} = 0$, $\hat n\cdot\mathbf{D}_1 = \rho_s$). Answer (e), circled in class.

> [!trap] At a boundary, use the integral forms
> The slide's bold closing rule: **never** use the differential Maxwell equations at a boundary — the fields are discontinuous and their derivatives are δ-functions. Apply the integral laws to a pillbox or thin loop, shrink, read off the jump. (The mnemonic in [[concepts/boundary-conditions]] — $\nabla\to\hat n$, field → its difference, $\rho\to\rho_s$, $\mathbf{J}\to\mathbf{J}_s$, drop time derivatives — is the result of doing that, not a substitute.)

## 5. Summary

- Charge conservation: $\oint\mathbf{J}\cdot d\mathbf{S} = -dQ/dt$, $\nabla\cdot\mathbf{J} = -\partial\rho/\partial t$. Out = decrease.
- $\nabla\cdot(\nabla\times\mathbf{H}) = 0$ forces $\nabla\times\mathbf{H} = \mathbf{J}+\partial\mathbf{D}/\partial t$; its divergence *is* continuity (with Gauss). $I_d = d\psi_E/dt$ [A]; in matter $\partial\mathbf{D}/\partial t = \epsilon_0\partial_t\mathbf{E} + \partial_t\mathbf{P}$.
- Two surfaces on one loop agree: draining charge $I/2$ both ways; capacitor $I$ both ways.
- Maxwell's equations complete; Hertz 1888; $\nabla\cdot\mathbf{B} = 0$ from Faraday + no monopoles.
- Boundary conditions unchanged by time variation: $D_n$ jumps by $\rho_s$, $E_t$ continuous, $B_n$ continuous, $H_t$ jumps by $J_s$. PEC: $\mathbf{E}$ normal (ends on $\rho_s$), $\mathbf{H}$ tangential (carried by $\mathbf{J}_s$). Integral forms at boundaries.

Concept pages: [[concepts/continuity-equation]] · [[concepts/displacement-current]] · [[concepts/maxwells-equations]] · [[concepts/boundary-conditions]].

> [!exam] On exams
> Four things get asked. (1) Continuity: given $\mathbf{J}$, the rate of change of charge in a region — divergence theorem, and say *decrease* or *increase*. (2) Displacement current: given $\mathbf{E}(t)$ and an area, $I_d = \epsilon\,d/dt\int\mathbf{E}\cdot d\mathbf{S}$, units checked. (3) Concept: why the term is needed (divergence of a curl is zero; charge conservation), or the two-surface paradox. (4) Boundary conditions with surface current: $\hat n\times(\mathbf{H}_1-\mathbf{H}_2) = \mathbf{J}_s$ and the perfect-conductor cases, $\hat n$ drawn first — Exam 1 problem 3's rubric with four conditions instead of two. Later, every reflection problem is condition-matching at an interface.

> [!tip] Practice this lecture
> [[practice/16-charge-conservation-and-displacement-current|12 practice problems]] — 5 easy, 3 medium, 4 hard — each with a folded hint and a worked solution. Start with [[practice/16-charge-conservation-and-displacement-current#161-charge-piling-up-in-a-cylinder|16.1 Charge piling up in a cylinder]]; the [[practice/index|practice hub]] has the whole bank by difficulty and by topic.

### Sources for this page
Kudeki notes, Lecture 16 (charge conservation, two-surface derivation, continuity; asymmetry and inconsistency; Ampère–Maxwell 1861, Hertz 1888; microscopic and macroscopic forms; $\nabla\cdot\mathbf{B} = 0$ and monopoles; boundary conditions with margin derivations). Shao, Lecture 16 slides (bucket; draining-charge MMF; unit cube; canonical fields; dynamic boundary conditions with the 2 October ink — $\hat n$ "from 2 to 1", $\mu_1H_{1n} = \mu_2H_{2n}$, $\mathbf{H} = 0$ in a PEC; the two exercises; integral forms at boundaries); Lecture 13 slides (capacitor paradox, $\psi_E$, the 0.1 m² example). The site's own: relaxation-time and lossy-capacitor links. Slips in the course material: see [[0-toolkit/04-errata-in-the-course-materials|errata]].
