---
title: "Biot–Savart law"
description: "dB = μ₀ I dl × R̂ /(4πR²): the magnetic field of a current element, falling off as 1/R² — Coulomb's law for currents, with a cross product. Summed over a closed circuit it gives the field of any steady current; the straight wire is the worked case."
tags: [concept, magnetostatics]
aliases: ["Biot-Savart", "field of a current element"]
---

> [!key] Definition
> $$
> \begin{gathered}
> d\mathbf{B} = \frac{\mu_0}{4\pi}\,\frac{I\,d\mathbf{l}\times\hat R}{R^2},\\[4pt]
> \mathbf{B} = \frac{\mu_0}{4\pi}\oint\frac{I\,d\mathbf{l}\times\hat R}{R^2}\quad\Big(\text{or }\frac{\mu_0}{4\pi}\int\frac{\mathbf{J}\times\hat R}{R^2}dV'\Big),
> \end{gathered}
> $$
> where $\mathbf{R} = R\hat R$ runs **from the current element to the field point**. Valid for elements of steady (or quasi-static) closed circuits; a lone element is not a possible steady current, and only the full integral is physical.

**Physics.** It is the magnetic Coulomb's law: $1/R^2$, superposition, and the same five-step recipe as [[concepts/coulombs-law]] — draw, divide into elements, write $d\mathbf{B}$, use symmetry to discard components that cancel, integrate. The difference is the cross product: $d\mathbf{B}$ is perpendicular both to the element and to the line joining it to the field point, so the field *circles* its source instead of pointing away from it. The law reproduces $\mathbf{B} = \mu_0I/(2\pi r)\,\hat\phi$ for a long wire (every element contributes along $\hat\phi$, and $\int_{-\infty}^\infty dz/(r^2+z^2)^{3/2} = 2/r^2$ — the same integral as the line charge), and the on-axis field of a loop, $B_z = \mu_0Ia^2/[2(a^2+z^2)^{3/2}]$. For problems with symmetry, [[concepts/amperes-law]] gets there faster; Biot–Savart is for everything else (finite segments, loops off-axis, coils), and it is the law that the [[concepts/vector-potential]] integral reproduces.

**Example.** A semi-infinite wire ending at the origin and running along $+z$: in the plane $z = 0$ at distance $a$, only half the straight-wire integral survives, $H_\phi = I/(4\pi a)$ — half the infinite-wire value. That is the number that [[3-maxwell-and-waves/16-charge-conservation-displacement-current-and-maxwells-equations|Lecture 16]]'s draining-charge example recovers from Ampère–Maxwell.

> [!trap]
> - Order: $d\mathbf{l}\times\hat R$, never $\hat R\times d\mathbf{l}$; and $\hat R$ from *source* to *field point*. Both slips flip the sign.
> - You cannot treat a whole wire as one element and "plug in" — integrate (the slides warn in boldface).
> - The force between two elements, $I_1d\mathbf{l}_1\times d\mathbf{B}_2$, is *not* equal and opposite to its partner; only the forces between closed circuits are.
> - The same letter $r$ is the cylindrical radius in $\mu_0I/(2\pi r)$ and, in the notes, the distance $|\mathbf{r}|$ in $d\mathbf{B}$; this site writes $R$ for the latter.

**Where it appears.** [[2-magnetostatics/12-magnetic-force-biot-savart-and-amperes-law|Lecture 12]] (statement; straight wire by the five steps), [[2-magnetostatics/13-current-sheets-solenoids-and-the-vector-potential|Lecture 13]] (loop, via $\mathbf{A}$), [[problems/mmf-around-a-draining-charge]] (semi-infinite wire check).

**Practice.** [[practice/topics#the-biotsavart-law|The Biot–Savart law]] (2 problems) — for example [[practice/12-magnetic-force-biot-savart-and-ampere#126-the-centre-of-a-square-loop|12.6 The centre of a square loop]] (medium).

Related: [[concepts/amperes-law]] · [[concepts/magnetic-field]] · [[concepts/superposition]] · [[concepts/five-step-recipe]].
