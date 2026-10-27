---
title: "Worked problem — MMF around a draining point charge"
description: "A point charge drains away through a wire. The circulation of H around a circle in the plane of the charge, computed through a dome and through a bowl with the Ampère–Maxwell law — same answer, I/2 — and confirmed by Biot–Savart for a semi-infinite wire. Then the loop is raised above the charge."
tags: [problem, waves]
---

*Problem · re-parameterized from the Lecture 16 slides (an "old book" Example 2.5) · uses [[3-maxwell-and-waves/16-charge-conservation-displacement-current-and-maxwells-equations|Lecture 16]] and [[2-magnetostatics/12-magnetic-force-biot-savart-and-amperes-law|Lecture 12]] · concepts: [[concepts/displacement-current]], [[concepts/continuity-equation]], [[concepts/amperes-law]], [[concepts/biot-savart-law]]*

> [!question] Problem
> A small conducting sphere at the origin carries a charge $Q(t) = Q_0e^{-t/\tau}$ with $Q_0 = 2$ nC and $\tau = 1$ ms, draining away through a thin straight wire that runs from the sphere along $+\hat z$ to a distant ground. Let $C$ be the circle of radius $a = 5$ cm in the plane $z = 0$, centred on the origin and traversed counter-clockwise when viewed from $+z$. Free space.
> (a) Find the current $I(t)$ in the wire and its direction. (b) Evaluate the MMF $\oint_C\mathbf{H}\cdot d\mathbf{l}$ using the Ampère–Maxwell law on a hemispherical dome spanning $C$ above the plane. (c) Repeat with a bowl below the plane, and comment. (d) Confirm the result with the Biot–Savart law. (e) Now raise the loop to the plane $z = h = 5$ cm (same radius, same centre line). What is the MMF?

## (a) The current

Charge conservation for a surface enclosing the sphere: the current *out* through the wire equals the rate of *decrease* of $Q$.

$$
I(t) = -\frac{dQ}{dt} = \frac{Q_0}{\tau}e^{-t/\tau} = 2\ \mu\text{A}\times e^{-t/\tau},
$$

flowing in $+\hat z$, away from the sphere.

> [!key] Answer (a)
> $I = (Q_0/\tau)e^{-t/\tau}$, $2\ \mu$A at $t = 0$, directed $+\hat z$ since positive charge is leaving the sphere. ([[concepts/continuity-equation]] in one line: $\oint\mathbf{J}\cdot d\mathbf{S} = -dQ/dt$.)

## (b) Through the dome

Ampère–Maxwell in integral form, with $S$ any surface bounded by $C$ and $d\mathbf{S}$ by the right-hand rule (upward/outward for a counter-clockwise $C$):

$$
\oint_C\mathbf{H}\cdot d\mathbf{l} = \int_S\mathbf{J}\cdot d\mathbf{S} + \frac{d}{dt}\int_S\mathbf{D}\cdot d\mathbf{S}.
$$

*Conduction term.* The wire pierces the dome going outward: $\int\mathbf{J}\cdot d\mathbf{S} = +I$.

*Displacement term.* The sphere's field is radial, $\mathbf{D} = \dfrac{Q}{4\pi R^2}\hat R$. Through the whole sphere of radius $a$ the flux is $Q$ (Gauss); by symmetry half of it, $Q/2$, exits through the upper hemisphere, outward. So $\dfrac{d}{dt}\int_S\mathbf{D}\cdot d\mathbf{S} = \dfrac{d}{dt}\dfrac Q2 = -\dfrac I2$.

$$
\text{MMF} = I - \frac I2 = \frac I2 = \frac{Q_0}{2\tau}e^{-t/\tau} = 1\ \mu\text{A}\times e^{-t/\tau}.
$$

> [!key] Answer (b)
> $\oint_C\mathbf{H}\cdot d\mathbf{l} = I/2$; $1\ \mu$A at $t = 0$ (an MMF is measured in amperes).

## (c) Through the bowl

Take the lower hemisphere. *Conduction term:* no wire passes through it, $0$. *Displacement term:* with the orientation inherited from $C$ (normal pointing "up", i.e. *into* the lower hemisphere, toward the charge), the flux is $-Q/2$ — the field exits the bowl downward, against the chosen normal. Its rate of change is $\dfrac{d}{dt}\Big(-\dfrac Q2\Big) = +\dfrac I2$.

$$
\text{MMF} = 0 + \frac I2 = \frac I2\quad\checkmark
$$

> [!key] Answer (c)
> The same $I/2$. Without the displacement term the dome would give $I$ and the bowl $0$ — the left side cannot depend on which surface you imagined, so static Ampère's law is simply wrong here; charge is accumulating (depleting) at the origin, $\nabla\cdot\mathbf{J}\neq0$, and that is exactly the situation Maxwell's term was invented for.

## (d) Biot–Savart check

The wire is semi-infinite, from $z = 0$ to $\infty$. For a straight segment the field at perpendicular distance $a$ is $H_\phi = \dfrac{I}{4\pi a}(\sin\theta_2 - \sin\theta_1)$, with the angles measured at the field point from the perpendicular to the wire; here the perpendicular foot is at the wire's end, so $\theta_1 = 0$ and $\theta_2 = 90°$: $H_\phi = \dfrac{I}{4\pi a}$ — half the infinite-wire value, since only half the elements are there. (Biot–Savart on the wire alone gives the exact field here: the only other effective source, the radial displacement current $\partial\mathbf{D}/\partial t$ of the shrinking Coulomb field, is spherically symmetric and contributes no $\mathbf{H}$.) Then

$$
\oint_C\mathbf{H}\cdot d\mathbf{l} = \frac{I}{4\pi a}\cdot2\pi a = \frac I2\quad\checkmark
$$

Numerically, $H_\phi(a = 5\ \text{cm}) = \dfrac{2\times10^{-6}}{4\pi\times0.05} = 3.2\ \mu$A/m at $t = 0$.

> [!key] Answer (d)
> Biot–Savart agrees: $I/2$. The two laws are consistent *because* of the displacement current; Biot–Savart applied to the wire alone silently includes the effect that Ampère's law needs the extra term to capture.

## (e) The loop raised to z = h

Use the flat disk at height $h$ as the surface. *Conduction:* the wire pierces it, $+I$. *Displacement:* the disk subtends, at the charge, a cone of half-angle $\theta_0$ with $\cos\theta_0 = h/\sqrt{h^2+a^2}$; the fraction of $Q$'s flux through it is the solid-angle fraction $\tfrac12(1-\cos\theta_0)$. So

$$
\text{MMF} = I + \frac{d}{dt}\Big[\frac Q2(1-\cos\theta_0)\Big] = I - \frac I2(1-\cos\theta_0) = \frac I2(1+\cos\theta_0).
$$

With $h = a$: $\cos\theta_0 = 1/\sqrt2 = 0.707$, MMF $= 0.854\,I = 1.71\ \mu$A at $t = 0$. Biot–Savart for the semi-infinite wire at height $h$ gives $H_\phi = \dfrac{I}{4\pi a}(1+\cos\theta_0)$ — the same thing. Limits: $h\to0$ returns $I/2$; $h\to\infty$ gives $I$, the full infinite-wire circulation, because far up the wire looks infinite in both directions and the charge's flux through the loop no longer changes.

> [!key] Answer (e)
> $\text{MMF} = \tfrac12I(1+\cos\theta_0) = 0.854\,I\approx1.7\ \mu$A at $t = 0$.

> [!trap] Where this problem loses points
> - Sign of the displacement term: $dQ/dt = -I$ (the charge is *draining*); a dropped minus sign gives $3I/2$ instead of $I/2$.
> - Orientation of the second surface: the bowl's normal must be the one the right-hand rule assigns from $C$, which makes its flux $-Q/2$, not $+Q/2$.
> - Looking for a magnetic field from the radial displacement current of the shrinking Coulomb field: it is spherically symmetric and makes none, which is why Biot–Savart on the wire alone is exact.
> - Reporting the MMF in volts. $\oint\mathbf{H}\cdot d\mathbf{l}$ is in amperes; $\oint\mathbf{E}\cdot d\mathbf{l}$ is the one in volts.
