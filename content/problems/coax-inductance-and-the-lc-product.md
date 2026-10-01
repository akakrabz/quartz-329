---
title: "Worked problem — Inductance of a coax, and the 𝓛𝓒 product"
description: "The full line-parameter table for a real-looking coax: 𝓛 by the Ampère chain and again by the energy integral, 𝓒 and 𝓖 from Unit 1, the checks 𝓛𝓒 = με and 𝓖/𝓒 = σ/ε, the signal speed, and — as a look ahead — the 50 Ω that falls out."
tags: [problem, magnetostatics]
---

*Problem · style of a Lecture 15 inductance problem (the magnetic twin of FA26 Exam 1 #4) · uses [[2-magnetostatics/15-inductance-magnetic-energy-and-the-potentials|Lecture 15]] and [[1-electrostatics/10-capacitance-and-conductance|Lecture 10]] · concepts: [[concepts/inductance]], [[concepts/magnetic-energy]], [[concepts/capacitance]], [[concepts/conductance]]*

> [!question] Problem
> A coaxial cable has an inner conductor of radius $a = 0.5$ mm and an outer conductor of inner radius $b = 1.75$ mm. The space between is filled with polyethylene: $\epsilon = 2.25\,\epsilon_0$, $\mu = \mu_0$, and a tiny conductivity $\sigma = 10^{-9}$ S/m. The far end is shorted so that a current $I$ flows down the inner conductor and returns on the inside of the outer one.
> (a) Find $\mathbf{H}$ between the conductors and the flux linked per unit length; hence the inductance per unit length $\mathcal{L}$. (b) Recover $\mathcal{L}$ from the stored magnetic energy. (c) Write down $\mathcal{C}$ and $\mathcal{G}$ for the same cable and check $\mathcal{L}\mathcal{C} = \mu\epsilon$ and $\mathcal{G}/\mathcal{C} = \sigma/\epsilon$. (d) What is $1/\sqrt{\mathcal{L}\mathcal{C}}$, and what does it mean? (e) *(Look ahead.)* Evaluate $\sqrt{\mathcal{L}/\mathcal{C}}$.

Throughout, $\ln(b/a) = \ln3.5 = 1.2528$.

## (a) The Ampère chain

**$\mathbf{H}$.** Cylindrical symmetry ⟹ $\mathbf{H} = H_\phi(r)\hat\phi$. Ampère on a circle of radius $a<r<b$ encloses $I$: $H_\phi\cdot2\pi r = I$, so $\mathbf{H} = \dfrac{I}{2\pi r}\hat\phi$, $\mathbf{B} = \dfrac{\mu_0I}{2\pi r}\hat\phi$. Outside $r>b$ the return current cancels $I$: $\mathbf{H} = 0$ — the field, and hence the flux, is confined to the cable.

**Flux per unit length.** The surface bounded by the current path (down the core, across the short, back along the shield) is the rectangle $a<r<b$ in a plane containing the axis, with normal $\hat\phi$ — along $\mathbf{B}$. Per metre of length:

$$
\frac{\Psi}{\ell} = \int_a^b\frac{\mu_0I}{2\pi r}\,dr = \frac{\mu_0I}{2\pi}\ln\frac ba .
$$

> [!key] Answer (a)
> $$
> \mathcal{L} = \frac{\Psi/\ell}{I} = \frac{\mu_0}{2\pi}\ln\frac ba = 2\times10^{-7}\times1.2528 = 2.51\times10^{-7}\ \text{H/m} = 251\ \text{nH/m}.
> $$
> Units: $\mu_0$ [H/m] times a pure number. The assumed $I$ has cancelled, as it must.

## (b) The energy route

$W' = \tfrac12\mathcal{L}I^2$ must equal the field energy per metre, $\displaystyle\int\tfrac12\mu_0H^2\,dV$ over the annulus:

$$
W' = \int_a^b\tfrac12\mu_0\Big(\frac{I}{2\pi r}\Big)^2\,2\pi r\,dr = \frac{\mu_0I^2}{4\pi}\ln\frac ba\quad\Rightarrow\quad \mathcal{L} = \frac{2W'}{I^2} = \frac{\mu_0}{2\pi}\ln\frac ba\quad\checkmark
$$

> [!key] Answer (b)
> Same $\mathcal{L}$, with no flux surface to choose — a good cross-check whenever the "surface bounded by the current path" is confusing. (For $I = 2$ A the cable stores $0.50\ \mu$J per metre.)

## (c) The other two parameters, and the two checks

From Lecture 10, with the same geometric factor $2\pi/\ln(b/a)$:

$$
\mathcal{C} = \frac{2\pi\epsilon}{\ln(b/a)} = \frac{2\pi\times2.25\times8.854\times10^{-12}}{1.2528} = 9.99\times10^{-11}\ \text{F/m}\approx100\ \text{pF/m},\qquad
\mathcal{G} = \frac{2\pi\sigma}{\ln(b/a)} = 5.02\times10^{-9}\ \text{S/m}.
$$

Checks:

$$
\mathcal{L}\mathcal{C} = (2.51\times10^{-7})(9.99\times10^{-11}) = 2.50\times10^{-17}\ \text{s}^2/\text{m}^2 = \mu_0\epsilon = 2.25\times(1.113\times10^{-17})\quad\checkmark
$$

$$
\frac{\mathcal{G}}{\mathcal{C}} = \frac{5.02\times10^{-9}}{9.99\times10^{-11}} = 50.2\ \text{s}^{-1},\qquad \frac{\sigma}{\epsilon} = \frac{10^{-9}}{2.25\times8.854\times10^{-12}} = 50.2\ \text{s}^{-1}\quad\checkmark
$$

> [!key] Answer (c)
> $\mathcal{C}\approx100$ pF/m, $\mathcal{G}\approx5.0$ nS/m, and both identities hold — because the logarithm sits in the denominator of $\mathcal{C}$ and $\mathcal{G}$ and in the numerator of $\mathcal{L}$. The ratio $\mathcal{G}/\mathcal{C} = \sigma/\epsilon$ is also the inverse relaxation time of the filling ($\tau = 20$ ms here — a very good insulator at any frequency of interest).

## (d) The speed

$$
\frac{1}{\sqrt{\mathcal{L}\mathcal{C}}} = \frac{1}{\sqrt{2.50\times10^{-17}}} = 2.00\times10^8\ \text{m/s},\qquad \frac{1}{\sqrt{\mu_0\epsilon}} = \frac{c}{\sqrt{2.25}} = \frac{c}{1.5}.
$$

> [!key] Answer (d)
> $2.00\times10^8$ m/s, the speed of light *in polyethylene* — and, as Unit 4 will show, the speed at which a signal travels along this cable. It depends on the filling only, not on the radii: any coax, any pair of plates, any two-wire line with the same dielectric carries signals at the same speed.

## (e) Look ahead

$$
\sqrt{\frac{\mathcal{L}}{\mathcal{C}}} = \sqrt{\frac{2.51\times10^{-7}}{9.99\times10^{-11}}} = \sqrt{2508}\ \Omega = 50.1\ \Omega .
$$

> [!key] Answer (e)
> About $50\ \Omega$ — the **characteristic impedance** of the line, the ratio of voltage to current for a wave travelling along it (Unit 4). The numbers were not chosen at random: $b/a = 3.5$ with $\epsilon_r = 2.25$ is the recipe for standard 50 Ω coax, and the formula is $Z_0 = \dfrac{1}{2\pi}\sqrt{\dfrac\mu\epsilon}\ln\dfrac ba = \dfrac{60\ \Omega}{\sqrt{\epsilon_r}}\ln\dfrac ba$.

> [!trap] Where this problem loses points
> - Using $\mu_0$ for the *field* but forgetting the medium's $\epsilon$ in $\mathcal{C}$ (or vice versa): each parameter takes its own material constant.
> - Taking the flux through a circle instead of the $r$–$z$ rectangle; the circle's normal is along the axis, perpendicular to $\mathbf{B}$, and gives zero.
> - Reporting H instead of H/m: the question asked *per unit length*, and the answer is 251 nH/m, not 251 nH.
> - Not checking $\mathcal{L}\mathcal{C} = \mu\epsilon$ at the end: it costs ten seconds and catches a dropped $2\pi$ or an inverted logarithm every time.
