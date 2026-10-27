---
title: "Lorentz force"
description: "F = q(E + v×B): the definition of the electric and magnetic fields through the force on a charge, with the velocity selector and mass spectrometer as its two textbook applications."
tags: [concept, electrostatics, magnetostatics]
aliases: ["Lorentz force law", "velocity selector", "mass spectrometer", "magnetic force on a charge"]
---

> [!key] Lorentz force — the definition of E and B
> $$
> \mathbf{F} = q\left(\mathbf{E} + \mathbf{v}\times\mathbf{B}\right)
> $$
> - $\mathbf{E}$ is **force per unit stationary charge** ($\mathbf{v}=0$): units N/C = **V/m**.
> - $\mathbf{B}$ is defined by the *extra* force on a *moving* charge, $\mathbf{F}_M = q\,\mathbf{v}\times\mathbf{B}$. It is perpendicular to $\mathbf{v}$ (and $\mathbf{B}$), so it does no work; a charge moving *along* $\mathbf{B}$ feels none. Units: **T** (tesla) = Wb/m² = N·s/(C·m).
>
> Newton's second law: $m\,d\mathbf{v}/dt = q(\mathbf{E}+\mathbf{v}\times\mathbf{B})$, valid for $\lvert\mathbf{v}\rvert\ll c$.

**Physics.** The law is not derived from anything — it is how $\mathbf{E}$ and $\mathbf{B}$ are *defined*, operationally, by what they do to a test charge; Maxwell's equations then say how charges and currents produce the fields. Consequences:

- The magnetic force does no work ($\mathbf{F}_M\perp\mathbf{v}$); it changes direction, not speed → for $\mathbf{v}\perp\mathbf{B}$, circular motion of radius $R = mv/(\lvert q\rvert B)$ in a uniform $\mathbf{B}$ (a helix in general).
- Crossed fields select a velocity: $\mathbf{F}=0$ when $v = E/B$.
- Current is charge in motion, so $I\,d\mathbf{l} \leftrightarrow q\mathbf{v}$ and the force on a wire element is $d\mathbf{F} = I\,d\mathbf{l}\times\mathbf{B}$ (units: A·m = (C/s)·m = C·(m/s) ✓) — motors, [[2-magnetostatics/12-magnetic-force-biot-savart-and-amperes-law|Lecture 12]].
- $\mathbf{E}$ and $\mathbf{B}$ mix between reference frames: $\mathbf{E}'\approx\mathbf{E}+\mathbf{v}\times\mathbf{B}$. A charge at rest for you is a current for me — which is why Maxwell's equations couple the two fields.

**Examples.**

> [!example] Slides, Lecture 2: velocity selector, then mass selector
> **Crossed fields.** Send a charge with $\mathbf{v}=v_0\hat{x}$ through $\mathbf{E}=E_0\hat{z}$ and $\mathbf{B}=-B_0\hat{y}$. Then $\mathbf{v}\times\mathbf{B} = v_0\hat{x}\times(-B_0\hat{y}) = -v_0B_0\hat{z}$, so
> $$
> \mathbf{F} = q\,(E_0 - v_0B_0)\,\hat{z} = 0 \iff v_0 = E_0/B_0 .
> $$
> Faster particles bend one way (magnetic wins), slower ones the other; only $v = E/B$ passes straight through the aperture.
>
> **Uniform field, no E.** With $\mathbf{B}=B_0\hat{z}$ and $\mathbf{v}\perp\mathbf{B}$, $q\mathbf{v}\times\mathbf{B}$ has constant magnitude $qv_0B_0$, always perpendicular to $\mathbf{v}$: uniform circular motion. $mv_0^2/R = qv_0B_0$ gives $R = mv_0/(qB_0)$; heavier ions land farther out — a mass spectrometer.

> [!trap] The cross product sets the geometry
> - Compute $\mathbf{v}\times\mathbf{B}$ with the determinant or the cyclic rule ($\hat{x}\times\hat{y}=\hat{z}$); a sign error reverses the bend.
> - A negative charge bends the other way; $R$ uses $\lvert q\rvert$.

> [!exam] On exams
> Direction of $q\mathbf{v}\times\mathbf{B}$ for a given sign of $q$; the balance $qE = qvB$ in a selector; $R = mv/(\lvert q\rvert B)$. Magnetic force never changes speed.

**Where it appears.** [[1-electrostatics/01-fields-forces-and-the-maxwell-roadmap#1-why-fields-at-all|Lecture 1 §1]] (definition), [[1-electrostatics/02-coulombs-law-superposition-and-gauss#1-force-first-then-field|Lecture 2 §1]] (velocity and mass selectors, $I\,d\mathbf{l}\leftrightarrow q\mathbf{v}$), [[2-magnetostatics/12-magnetic-force-biot-savart-and-amperes-law|Lecture 12]] (magnetic force on currents, and where $\mathbf{B}$ comes from), [[2-magnetostatics/14-faradays-law-and-induced-emf|Lecture 14]] (motional emf, and the unchanged definitions of $\mathbf{E}$ and $\mathbf{B}$ in time-varying fields).

**Related.** [[concepts/electric-field|Electric field E]] · [[concepts/coulombs-law|Coulomb's law]] · [[concepts/magnetic-field|Magnetic field: B and H]] · [[concepts/motional-emf|Motional emf and the voltmeter paradox]].

**Practice.** [[practice/topics#magnetic-force-and-charged-particles|Magnetic force and charged particles]] (8 problems) — for example [[practice/12-magnetic-force-biot-savart-and-ampere#121-a-charge-passing-a-wire|12.1 A charge passing a wire]] (easy), [[practice/12-magnetic-force-biot-savart-and-ampere#129-a-rectangular-loop-beside-a-wire|12.9 A rectangular loop beside a wire]] (hard).
