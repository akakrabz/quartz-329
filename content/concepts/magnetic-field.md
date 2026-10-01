---
title: "Magnetic field: B and H"
description: "B is the magnetic flux density (tesla), defined by the force qv×B; H = B/μ is the field whose circulation is the current (A/m). Both are produced by moving charge, both are divergence-free, and the canonical results — line, sheet, solenoid, loop — are listed here."
tags: [concept, magnetostatics]
aliases: ["magnetic flux density", "B field", "H field", "permeability"]
---

> [!key] Definition
> $\mathbf{B}$ is defined by the velocity-dependent part of the force on a charge,
> $$
> \mathbf{F} = q\mathbf{v}\times\mathbf{B}\qquad(\text{equivalently } d\mathbf{F} = I\,d\mathbf{l}\times\mathbf{B}\text{ on a current element}),
> $$
> in tesla, $\text{T} = \text{N/(A·m)} = \text{Wb/m}^2$. $\mathbf{H} = \mathbf{B}/\mu_0$ in free space, $\mathbf{B} = \mu\mathbf{H}$ in a medium, in A/m: it is the field whose line integral around a loop equals the current through it. $\mu_0 = 4\pi\times10^{-7}$ H/m is the permeability of free space; $\mu = (1+\chi_m)\mu_0 = \mu_r\mu_0$ in a material (Lecture 17). The pairing $\mathbf{B}\leftrightarrow\mathbf{D}$ (flux densities: normal components continuous unless a surface charge intervenes — $\rho_s$ for $\mathbf{D}$, never for $\mathbf{B}$) and $\mathbf{H}\leftrightarrow\mathbf{E}$ (fields: tangential components continuous unless a surface current intervenes — $\mathbf{J}_s$ for $\mathbf{H}$, never for $\mathbf{E}$) is the one that boundary conditions respect.

**Physics.** Moving charge — current — makes $\mathbf{B}$, and $\mathbf{B}$ acts only on moving charge. The force is perpendicular to the velocity, so static magnetic fields do no work: they bend trajectories (circular motion of radius $mv/|q|B$) without changing speed. Why a neutral current-carrying wire exerts a force at all is a relativistic effect of the Coulomb force ([[2-magnetostatics/12-magnetic-force-biot-savart-and-amperes-law|Lecture 12]]); magnetism is what remains of electrostatics when a near-perfect charge cancellation is spoiled by motion.

**The two laws.** Static: $\nabla\times\mathbf{H} = \mathbf{J}$ (sources in the curl — [[concepts/amperes-law]]) and $\nabla\cdot\mathbf{B} = 0$ always (no magnetic charge; field lines close on themselves). Any current distribution's field is given by [[concepts/biot-savart-law]] or by the [[concepts/vector-potential]]. Dynamic: $\nabla\times\mathbf{H} = \mathbf{J}+\partial\mathbf{D}/\partial t$ ([[concepts/displacement-current]]).

**Canonical fields (free space).**

| source | field | where derived |
|---|---|---|
| long straight current $I$ | $\mathbf{B} = \dfrac{\mu_0I}{2\pi r}\hat\phi$ (right-hand rule) | [[2-magnetostatics/12-magnetic-force-biot-savart-and-amperes-law\|Lecture 12]] |
| sheet $\mathbf{J}_s$ | $\mathbf{H} = \tfrac12\mathbf{J}_s\times\hat n$, $\hat n$ toward the field point; tangential, ± on the two sides, distance-independent | [[2-magnetostatics/13-current-sheets-solenoids-and-the-vector-potential\|Lecture 13]] |
| slab $J_0$, thickness $W$ | $H_y = J_0x$ inside, $\pm J_0W/2$ outside | Lecture 13 |
| long solenoid, $n$ turns/m | $\mathbf{B} = \mu_0nI\hat z$ inside, 0 outside | Lecture 13 |
| coax, uniform core | $H_\phi = Ir/(2\pi a^2)$, $I/(2\pi r)$, $0$ | Lecture 12 |
| loop of radius $a$, on axis | $B_z = \dfrac{\mu_0Ia^2}{2(a^2+z^2)^{3/2}}$; far field $\propto1/r^3$ (dipole $m = I\pi a^2$) | Lecture 13 |

> [!trap]
> - $\hat\phi$ is set by the right-hand rule about the *current*, not by the coordinate axes; a current along $-\hat x$ circulates $\mathbf{H}$ in $-\hat\phi$ about $+\hat x$.
> - $\mathbf{B}$ in tesla, $\mathbf{H}$ in A/m, $\mathbf{J}_s$ in A/m: a surface current and $\mathbf{H}$ share units because $H_t$ jumps by $J_s$.
> - "$\nabla\cdot\mathbf{H} = 0$" is only true where $\mu$ is uniform; the law is $\nabla\cdot\mathbf{B} = 0$.
> - A magnetic force never changes a particle's kinetic energy; if your answer has one doing work, recheck.

**Where it appears.** Defined in [[1-electrostatics/01-fields-forces-and-the-maxwell-roadmap|Lecture 1]] and derived in Lecture 12; computed throughout Lectures 12–13; its flux drives Faraday's law ([[2-magnetostatics/14-faradays-law-and-induced-emf|Lecture 14]]) and defines inductance ([[2-magnetostatics/15-inductance-magnetic-energy-and-the-potentials|Lecture 15]]); energy density $\tfrac12\mu H^2$ ([[concepts/magnetic-energy]]). The electrostatic twin of every row above is in the [[2-magnetostatics/index#the-dictionary-electrostatics--magnetostatics|dictionary]].

Related: [[concepts/lorentz-force]] · [[concepts/electric-field]] · [[concepts/magnetic-flux]] · [[concepts/boundary-conditions]].
