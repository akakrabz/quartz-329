---
title: "Electric field E"
description: "Force per unit stationary charge; a vector field with units V/m, sourced by charge, drawn as arrows or field lines. Why fields at all, and the two laws a static E obeys."
tags: [concept, electrostatics]
aliases: ["E field", "electric field", "field", "scalar field", "vector field", "field lines"]
---

> [!key] Definition
> $$
> \mathbf{E}(\mathbf{r}) = \lim_{q\to 0}\frac{\mathbf{F}}{q}\qquad [\text{V/m} = \text{N/C}]
> $$
> The force a small stationary test charge $q$ would feel at $\mathbf{r}$, divided by $q$; the limit means the test charge does not disturb the sources. It exists whether or not a test charge is there. On a stationary charge $\mathbf{F}_E = q\mathbf{E}$; on a moving one add $\mathbf{F}_M = q\mathbf{v}\times\mathbf{B}$ ([[concepts/lorentz-force|Lorentz force]]).

**Physics.** A **field** is a quantity defined at every point $(x,y,z)$ and time $t$; it makes action "at a distance" tractable. A *scalar* field assigns a number to each point (temperature, elevation, potential $V$); a *vector* field assigns a vector (wind velocity, $\mathbf{E}$, $\mathbf{B}$). $\mathbf{E}$ and $\mathbf{B}$ are defined *operationally*, by the force on a test charge, and Maxwell's equations say how charges and currents create them ([[concepts/maxwells-equations|Maxwell's equations]]). Two facts that return later:

- **Fields are frame-dependent.** A charge at rest in your frame is a current in mine, so $\mathbf{E}$ and $\mathbf{B}$ mix under a change of frame (to first order, $\mathbf{E}' = \mathbf{E} + \mathbf{v}\times\mathbf{B}$). That is *why* their equations are coupled — first seen in Faraday's law ([[2-magnetostatics/14-faradays-law-and-induced-emf|Lecture 14]]).
- **Charge comes in both signs, mass doesn't.** Ordinary matter is nearly neutral, so gravity — far weaker per particle — wins macroscopically, and the *net* charge density $\rho$ in a material is usually a tiny imbalance.

**How it is produced.** By charge: a point charge gives the Coulomb field $\dfrac{Q}{4\pi\epsilon_0 r^2}\hat{r}$ ([[concepts/coulombs-law|Coulomb's law]]); many charges give the vector sum ([[concepts/superposition|Superposition]]); charge densities give integrals ([[concepts/five-step-recipe|The 5-step recipe for fields of charge distributions]]) or, with symmetry, Gauss's law ([[concepts/gauss-law|Gauss's law]]). Time-varying magnetic fields *also* produce $\mathbf{E}$ (Faraday) — that part of $\mathbf{E}$ is not curl-free.

**How to picture it.**
- *Arrow plots*: an arrow on a grid with length $\lvert\mathbf{E}\rvert$ (or a *unit* vector with magnitude coded separately).
- *Field lines*: curves tangent to $\mathbf{E}$. They begin on positive and end on negative charge (or at infinity); leave a point charge uniformly; have *density* proportional to $\lvert\mathbf{E}\rvert$; and **never cross**, because $\mathbf{E}$ has one direction at each point — except at *null points* where $\mathbf{E}=0$ (the saddle between two like charges). A charge $2Q$ has twice as many lines as $Q$ — how you tell which charge is bigger in a picture.

**Its two local properties — the laws of electrostatics, and when they apply.**
$$
\nabla\times\mathbf{E} = 0,\qquad \nabla\cdot\mathbf{D} = \rho,\qquad \mathbf{D} = \epsilon_0\mathbf{E}\ (\text{vacuum}).
$$
Sources are charges ($\nabla\cdot\mathbf{E} = \rho/\epsilon_0$ in vacuum); a static field has no whirlpools, so it is [[concepts/conservative-field|conservative]] and $\mathbf{E} = -\nabla V$ — voltage exists ([[concepts/electrostatic-potential|Electrostatic potential V]]). They also hold **quasi-statically**: if sources vary on a time scale $\tau\gg L/c$ (light-travel time across the region), the fields at each instant are the static fields of the instantaneous sources (plus a small, slowly varying $\mathbf{B}$). Excellent for lab circuits below a few MHz; the transmission-line unit is about when it fails.

**Relatives.** $\mathbf{D} = \epsilon_0\mathbf{E}$ in vacuum, $\epsilon_0\mathbf{E}+\mathbf{P}$ in matter ([[concepts/electric-flux-density|Electric flux density D]]). Inside a perfect conductor in statics, $\mathbf{E}=0$ ([[concepts/conductors|Conductors in electrostatics]]).

> [!exam] On exams
> Units on every answer (V/m for $\mathbf{E}$, C/m² for $\mathbf{D}$); field-line pictures: which charge is bigger (line count), where $\mathbf{E}=0$ (null points), and that lines never cross.

**Where it appears.** [[1-electrostatics/01-fields-forces-and-the-maxwell-roadmap#1-why-fields-at-all|Lecture 1 §1]] (what a field is; frame dependence) · [[1-electrostatics/02-coulombs-law-superposition-and-gauss#1-force-first-then-field|Lecture 2 §1–2]] (force → field; drawing fields) · every lecture after.

**Related.** [[concepts/lorentz-force|Lorentz force]] · [[concepts/coulombs-law|Coulomb's law]] · [[concepts/superposition|Superposition]] · [[concepts/gauss-law|Gauss's law]] · [[concepts/electrostatic-potential|Electrostatic potential V]].
