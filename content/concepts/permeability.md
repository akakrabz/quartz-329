---
title: "Permeability, susceptibility, and B = μH"
description: "For linear magnetic media M = χmH, with no μ₀, so B = μ₀(1 + χm)H = μH with μ = μrμ₀. Diamagnets (χm ≈ −10⁻⁵) and paramagnets (χm ≈ +10⁻⁵) are nearly vacuum; ferromagnets have χm ≫ 1 that depends on H and on history. What a core changes, what happens at an interface, and typical values."
tags: [concept, waves]
aliases: ["relative permeability", "magnetic susceptibility", "diamagnetism", "paramagnetism", "ferromagnetism", "hysteresis", "B = μH"]
---

> [!key] Constitutive relation of a linear, isotropic magnetic medium
> $$
> \mathbf{M} = \chi_m\mathbf{H}\quad\Longrightarrow\quad \mathbf{B} = \mu_0(1+\chi_m)\mathbf{H} = \mu\mathbf{H},\qquad
> \mu = \mu_r\mu_0,\quad \mu_r = 1+\chi_m .
> $$
> $\chi_m$ (magnetic susceptibility) and $\mu_r$ (relative permeability) are dimensionless; $\mu$ is in H/m, and $\mu_0 = 4\pi\times10^{-7}$ H/m. No $\mu_0$ multiplies $\chi_m$, because $\mathbf{M}$ and $\mathbf{H}$ are both in A/m — compare $\mathbf{P} = \epsilon_0\chi_e\mathbf{E}$, where the units differ.

**Three classes.**

| | $\chi_m$ | mechanism | examples (course slides) |
|---|---|---|---|
| diamagnetic | negative, about $-10^{-5}$ ($\mu_r$ just below 1) | field *induces* orbital moments opposing it (Lenz) | copper $-0.94\times10^{-5}$, water $-0.88\times10^{-5}$, bismuth $-1.7\times10^{-4}$ |
| paramagnetic | positive, $10^{-5}$ to $10^{-3}$ ($\mu_r$ just above 1) | *permanent* atomic moments, partly aligned against thermal agitation; no domains | aluminum $+2.1\times10^{-5}$, palladium $+8\times10^{-4}$ |
| ferromagnetic | $10^2$ to $10^6$, depends on $H$ and history | spontaneously aligned *domains* that grow and turn | cobalt $\mu_r\approx250$, nickel 600, iron 5000, mumetal $10^5$ |

For ordinary dia- and paramagnets $\lvert\chi_m\rvert\lesssim10^{-3}$ (liquid oxygen, about $3.5\times10^{-3}$, is an unusually strong paramagnet), so $\mu = \mu_0$ to a fraction of a percent; that is why most problems treat such media as non-magnetic. Ferromagnets are non-linear and hysteretic: $B$ saturates (near 2 T for iron), a remanent $B_r$ survives at $H = 0$ (permanent magnets), and a reverse field $-H_c$ (the coercivity) is needed to remove it. Their tabulated $\mu_r$ is a small-field value. The mnemonic from the slides: **Para** ↔ **Pos**itive.

**Where the μ goes.** Everywhere $\mu_0$ appeared in a magnetostatic formula whose field region is filled with the medium: $\mathbf{B} = \mu\mathbf{H}$ around a line current or inside a solenoid ($\mu nI$), inductance ($L = n^2\mu A\ell$, $\mathcal{L} = \tfrac{\mu}{2\pi}\ln\tfrac ba$), energy density $\tfrac12\mu H^2$, and from Lecture 18 on the wave speed $1/\sqrt{\mu\epsilon}$ and the [[concepts/intrinsic-impedance|intrinsic impedance]] $\sqrt{\mu/\epsilon}$. Ampère's law in its $\mathbf{H}$ form needs no $\mu$ at all: $\oint\mathbf{H}\cdot d\mathbf{l} = I_{\text{free}}$.

**What a core changes.** With the free current fixed and the core's surfaces *parallel* to $\mathbf{H}$ (a long core along a solenoid's axis, a toroid, the filling of a coax), $\mathbf{H}$ is unchanged and $\mathbf{B}$, the flux and $L$ grow by $\mu_r$; $\mathbf{M} = \chi_m\mathbf{H}$ makes up the difference. Example: $n = 1000$ turns/m, $I = 2$ A, $\mu_r = 100$: $H = 2000$ A/m with or without the core, and $B$ rises from 2.51 mT to 0.251 T. When $\mathbf{H}$ crosses the core's surface (a short rod, a sphere, a gap), the ends set up a demagnetizing field and $\mathbf{H}$ inside drops: a sphere in a uniform $\mathbf{H}_0$ has $\mathbf{H}_{\text{in}} = 3\mathbf{H}_0/(\mu_r+2)$, so $B$ inside stays below $3\mu_0H_0$ however large $\mu_r$ is. And the linear formula has limits: an iron core with $\mu_r = 5000$ in the coil above would "give" 12.6 T, but iron saturates near 2 T.

**At an interface** between $\mu_1$ and $\mu_2$ with no free surface current: $H_t$ continuous and $B_n$ continuous, so $H_{2n} = (\mu_1/\mu_2)H_{1n}$, $B_{2t} = (\mu_2/\mu_1)B_{1t}$, and $\tan\theta_1/\tan\theta_2 = \mu_1/\mu_2$. From iron ($\mu_r = 5000$) into air, a line at 85° to the normal inside the iron leaves at 0.13°: field lines leave iron perpendicularly, as electric field lines leave a conductor. With a free surface current, $\hat n\times(\mathbf{H}_1-\mathbf{H}_2) = \mathbf{J}_s$ replaces the tangential condition; the normal one never changes.

> [!trap]
> - $\mathbf{M} = \chi_m\mathbf{H}$, not $\mu_0\chi_m\mathbf{H}$ (that would be in tesla).
> - $\mu_r$ and $\chi_m$ differ by 1: $\mu_r = 100$ means $\chi_m = 99$. It matters for $\mathbf{M}$, hardly for $\mathbf{B}$.
> - $\mathbf{B} = \mu\mathbf{H}$ uses the permeability of the region where you evaluate it.
> - "$\nabla\cdot\mathbf{H} = 0$" holds only where $\mu$ is uniform; the law is $\nabla\cdot\mathbf{B} = 0$, and normal $\mathbf{H}$ jumps at an interface.
> - "$\mathbf{H}$ is unchanged by the core" is true only when the core lies along $\mathbf{H}$; otherwise there is a demagnetizing field.
> - A ferromagnet's $\mu$ is not a constant; linear formulas are small-field approximations.

**Where it appears.** [[3-maxwell-and-waves/17-magnetization-and-maxwells-equations-in-matter|Lecture 17]] (defined, classified, boundary conditions), [[2-magnetostatics/15-inductance-magnetic-energy-and-the-potentials|Lecture 15]] ($L\propto\mu$, $\tfrac12\mu H^2$), [[problems/fields-across-a-magnetic-interface]], [[problems/coax-inductance-and-the-lc-product]] ($\mathcal{L}\mathcal{C} = \mu\epsilon$); from [[3-maxwell-and-waves/18-the-wave-equation-and-plane-tem-waves|Lecture 18]] on, every wave formula contains $\mu$.

**Practice.** [[practice/topics#magnetization-and-magnetic-media|Magnetization and magnetic media]] (11 problems) — for example [[practice/17-magnetization-and-maxwell-in-matter#172-four-rods-in-a-solenoid|17.2 Four rods in a solenoid]] (easy), [[practice/17-magnetization-and-maxwell-in-matter#176-graded-magnetization-in-a-slab|17.6 Graded magnetization in a slab]] (medium), [[practice/17-magnetization-and-maxwell-in-matter#179-electret-and-magnet-twins|17.9 Electret and magnet twins]] (hard).

Related: [[concepts/magnetization]] · [[concepts/magnetic-field]] · [[concepts/inductance]] · [[concepts/permittivity]] · [[concepts/boundary-conditions]].
