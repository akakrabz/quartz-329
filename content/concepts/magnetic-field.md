---
title: "Magnetic field: B and H"
description: "B is the magnetic flux density (tesla), defined by the force qv×B; H = B/μ (A/m) is the field whose circulation is the free current. Canonical fields of lines, sheets, solenoids and loops."
tags: [concept, magnetostatics]
aliases: ["magnetic flux density", "B field", "H field"]
---

> [!key] Definition
> $\mathbf{B}$ is defined by the velocity-dependent part of the force on a charge,
> $$
> \mathbf{F} = q\mathbf{v}\times\mathbf{B}\qquad(\text{equivalently } d\mathbf{F} = I\,d\mathbf{l}\times\mathbf{B}\text{ on a current element}),
> $$
> in tesla, $\text{T} = \text{N/(A·m)} = \text{Wb/m}^2$. $\mathbf{H} = \mathbf{B}/\mu_0$ in free space, $\mathbf{B} = \mu\mathbf{H}$ in a medium, in A/m: its line integral around a loop is the current through it. $\mu_0 = 4\pi\times10^{-7}$ H/m; $\mu = (1+\chi_m)\mu_0 = \mu_r\mu_0$ ([[concepts/permeability]]). Boundary conditions pair $\mathbf{B}\leftrightarrow\mathbf{D}$ (normal components jump only by surface charge: $\rho_s$ for $\mathbf{D}$, never for $\mathbf{B}$) and $\mathbf{H}\leftrightarrow\mathbf{E}$ (tangential components jump only by surface current: $\mathbf{J}_s$ for $\mathbf{H}$, never for $\mathbf{E}$).

**Physics.** Current makes $\mathbf{B}$, and $\mathbf{B}$ acts only on moving charge. The force is perpendicular to $\mathbf{v}$, so static magnetic fields do no work: they bend trajectories (radius $mv/|q|B$) without changing speed. A neutral current-carrying wire exerts a force through a relativistic effect of the Coulomb force ([[2-magnetostatics/12-magnetic-force-biot-savart-and-amperes-law|Lecture 12]]): magnetism is what remains of electrostatics when motion spoils a near-perfect charge cancellation.

**In matter** ([[3-maxwell-and-waves/17-magnetization-and-maxwells-equations-in-matter|Lecture 17]]). In general $\mathbf{H}\equiv\mathbf{B}/\mu_0-\mathbf{M}$, with $\mathbf{M}$ the [[concepts/magnetization]], built so that $\oint\mathbf{H}\cdot d\mathbf{l}$ counts *free* current only. Free currents set $\mathbf{H}$ (independently of the medium when symmetry lets Ampère's law decide alone: sheet, solenoid, coax), and the medium sets $\mathbf{B} = \mu\mathbf{H}$, as free charge sets $\mathbf{D}$ and the medium $\mathbf{E} = \mathbf{D}/\epsilon$. The force law uses $\mathbf{B}$, not $\mathbf{H}$.

**The two laws.** Static: $\nabla\times\mathbf{H} = \mathbf{J}$ ([[concepts/amperes-law]]) and, always, $\nabla\cdot\mathbf{B} = 0$ (no magnetic charge; field lines close). Any current's field follows from [[concepts/biot-savart-law]] or the [[concepts/vector-potential]]. Dynamic: $\nabla\times\mathbf{H} = \mathbf{J}+\partial\mathbf{D}/\partial t$ ([[concepts/displacement-current]]).

**Canonical fields (free space).**

| source | field | where derived |
|---|---|---|
| long straight current $I$ | $\mathbf{B} = \dfrac{\mu_0I}{2\pi r}\hat\phi$ (right-hand rule) | [[2-magnetostatics/12-magnetic-force-biot-savart-and-amperes-law\|Lecture 12]] |
| sheet $\mathbf{J}_s$ | $\mathbf{H} = \tfrac12\mathbf{J}_s\times\hat n$, $\hat n$ toward the field point; tangential, reversed across the sheet, distance-independent | [[2-magnetostatics/13-current-sheets-solenoids-and-the-vector-potential\|Lecture 13]] |
| slab $J_0$, thickness $W$ | $H_y = J_0x$ inside, $\pm J_0W/2$ outside | Lecture 13 |
| long solenoid, $n$ turns/m | $\mathbf{B} = \mu_0nI\hat z$ inside, 0 outside | Lecture 13 |
| coax, uniform core | $H_\phi = Ir/(2\pi a^2)$, $I/(2\pi r)$, $0$ | Lecture 12 |
| loop of radius $a$, on axis | $B_z = \dfrac{\mu_0Ia^2}{2(a^2+z^2)^{3/2}}$; far field $\propto1/r^3$ (dipole $m = I\pi a^2$) | Lecture 13 |

> [!trap]
> - $\hat\phi$ follows the right-hand rule about the *current*, not the axes: a current along $-\hat x$ circulates $\mathbf{H}$ in $-\hat\phi$ about $+\hat x$.
> - $\mathbf{B}$ in tesla; $\mathbf{H}$ and $\mathbf{J}_s$ in A/m, because $H_t$ jumps by $J_s$.
> - "$\nabla\cdot\mathbf{H} = 0$" holds only where $\mu$ is uniform; the law is $\nabla\cdot\mathbf{B} = 0$.

**Where it appears.** Defined in [[1-electrostatics/01-fields-forces-and-the-maxwell-roadmap|Lecture 1]], derived in Lecture 12, computed in Lectures 12–13; its flux drives Faraday's law ([[2-magnetostatics/14-faradays-law-and-induced-emf|Lecture 14]]) and defines inductance ([[2-magnetostatics/15-inductance-magnetic-energy-and-the-potentials|Lecture 15]]); energy density $\tfrac12\mu H^2$ ([[concepts/magnetic-energy]]). Electrostatic twins of every row: the [[2-magnetostatics/index#the-dictionary-electrostatics--magnetostatics|dictionary]].

Related: [[concepts/lorentz-force]] · [[concepts/electric-field]] · [[concepts/magnetic-flux]] · [[concepts/boundary-conditions]].
