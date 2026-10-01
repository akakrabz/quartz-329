---
title: "Ampère's law"
description: "∮H·dl = I_enc: the circulation of H around any closed loop equals the net current through any surface the loop bounds (right-hand rule). Differential form ∇×H = J. With the displacement current added it becomes the Ampère–Maxwell equation. It is to currents what Gauss's law is to charges."
tags: [concept, magnetostatics]
aliases: ["Ampere's law", "circuital law", "Ampère–Maxwell equation", "MMF"]
---

> [!key] Definition
> $$
> \oint_C\mathbf{H}\cdot d\mathbf{l} = I_{\text{enc}} = \int_S\mathbf{J}\cdot d\mathbf{S}\qquad\Longleftrightarrow\qquad \nabla\times\mathbf{H} = \mathbf{J}\quad(\text{static}),
> $$
> for every closed directed path $C$ and any surface $S$ it bounds, with $d\mathbf{S}$ (and the positive sense of current) fixed by the right-hand rule from the direction of $C$. In free space $\mathbf{H} = \mathbf{B}/\mu_0$, so equivalently $\oint\mathbf{B}\cdot d\mathbf{l} = \mu_0I_{\text{enc}}$. The circulation $\oint\mathbf{H}\cdot d\mathbf{l}$ is called the **magnetomotive force**, MMF, in amperes — the twin of the EMF $\oint\mathbf{E}\cdot d\mathbf{l}$ in volts. Time-varying fields need the extra term: $\nabla\times\mathbf{H} = \mathbf{J} + \partial\mathbf{D}/\partial t$ ([[concepts/displacement-current]]).

**Physics.** It is Gauss's law with a loop. Gauss counts flux out of a closed *surface* and equates it to the charge inside; Ampère counts circulation around a closed *loop* and equates it to the current through. Both are exact for every surface/loop, and both are *useful* only when symmetry makes the field constant along the loop so it factors out: $H\cdot(\text{loop length}) = I_{\text{enc}}$. The three symmetries are the cylindrical ones (circle: $H_\phi\cdot2\pi r$), the planar ones (rectangle straddling a sheet or slab: $2H\cdot L$), and the solenoid (rectangle with one leg inside: $H\cdot L$). Stokes' theorem converts the integral law to $\nabla\times\mathbf{H} = \mathbf{J}$; the divergence of that equation forces $\nabla\cdot\mathbf{J} = 0$, which is why the static law fails when charge accumulates and Maxwell had to add $\partial\mathbf{D}/\partial t$.

**Examples.** Straight wire: $H_\phi = I/(2\pi r)$ for any radius. Coax with uniform core: $Ir/(2\pi a^2)$, $I/(2\pi r)$, $0$. Sheet $\mathbf{J}_s$: $\mathbf{H} = \tfrac12\mathbf{J}_s\times\hat n$. Slab: ramp $J_0x$ then $\pm J_0W/2$. Solenoid: $nI$ inside, zero outside ([[2-magnetostatics/13-current-sheets-solenoids-and-the-vector-potential|Lecture 13]]). Across any current sheet the tangential $\mathbf{H}$ jumps by $J_s$ — the boundary condition $\hat n\times(\mathbf{H}_1-\mathbf{H}_2) = \mathbf{J}_s$ is Ampère's law on a vanishingly thin loop.

> [!trap]
> - $I_{\text{enc}}$ is signed: for a clockwise loop, currents *into* the page count positive (right-hand rule); for counter-clockwise, out of the page.
> - Only current that *pierces* the surface counts. A wire next to the loop contributes to $\mathbf{H}$ along the path but not to the circulation.
> - The surface may be any surface on $C$ — flat disk or bowl — and the answer must not depend on the choice; in statics it never does, and the two-surface paradox of [[3-maxwell-and-waves/16-charge-conservation-displacement-current-and-maxwells-equations|Lecture 16]] is what happens when it does.
> - Ampère's law gives the *field* only after symmetry has fixed its direction and dependence. Where there is no symmetry, use [[concepts/biot-savart-law]].
> - Cancel the arbitrary path length $L$ at the end; if it survives, the loop was wrong.

**Where it appears.** [[2-magnetostatics/12-magnetic-force-biot-savart-and-amperes-law|Lecture 12]] (statement, $\mathbf{H}$, differential form, coax), Lecture 13 (sheet, slab, solenoid), [[2-magnetostatics/15-inductance-magnetic-energy-and-the-potentials|Lecture 15]] (first step of every inductance), Lecture 16 (completed with the displacement current), [[problems/current-slab-and-sheet-by-amperes-law]], [[problems/coax-inductance-and-the-lc-product]], [[problems/mmf-around-a-draining-charge]].

Related: [[concepts/gauss-law]] · [[concepts/stokes-theorem]] · [[concepts/curl]] · [[concepts/magnetic-field]] · [[concepts/maxwells-equations]].
