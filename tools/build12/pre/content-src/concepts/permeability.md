---
title: "Permeability, susceptibility, and B = μH"
description: "Linear magnetic media: M = χmH (no μ₀), B = μH, μ = μrμ₀. Dia-, para- and ferromagnets, cores, interfaces."
tags: [concept, waves]
aliases: ["relative permeability", "magnetic susceptibility", "diamagnetism", "paramagnetism", "ferromagnetism", "hysteresis", "B = μH"]
---

> [!key] Constitutive relation of a linear, isotropic magnetic medium
> $$
> \mathbf{M} = \chi_m\mathbf{H}\quad\Longrightarrow\quad \mathbf{B} = \mu_0(1+\chi_m)\mathbf{H} = \mu\mathbf{H},\qquad
> \mu = \mu_r\mu_0,\quad \mu_r = 1+\chi_m .
> $$
> $\chi_m$ (magnetic susceptibility) and $\mu_r$ (relative permeability) are dimensionless; $\mu$ in H/m, $\mu_0 = 4\pi\times10^{-7}$ H/m. No $\mu_0$ in $\chi_m\mathbf{H}$ ($\mu_0\chi_m\mathbf{H}$ would be tesla): $\mathbf{M}$, $\mathbf{H}$ are both A/m, unlike $\mathbf{P} = \epsilon_0\chi_e\mathbf{E}$.

**Three classes.**

| | $\chi_m$ | mechanism | examples (course slides) |
|---|---|---|---|
| diamagnetic | about $-10^{-5}$ ($\mu_r\lesssim1$) | field *induces* opposing orbital moments (Lenz) | copper $-0.94\times10^{-5}$, water $-0.88\times10^{-5}$, bismuth $-1.7\times10^{-4}$ |
| paramagnetic | $10^{-5}$ to $10^{-3}$ ($\mu_r\gtrsim1$) | *permanent* moments partly aligned against thermal agitation; no domains | aluminum $+2.1\times10^{-5}$, palladium $+8\times10^{-4}$ |
| ferromagnetic | $10^2$ to $10^6$, depends on $H$ and history | aligned *domains* grow and turn | cobalt $\mu_r\approx250$, nickel 600, iron 5000, mumetal $10^5$ |

For dia- and paramagnets problems take $\mu = \mu_0$ (liquid oxygen, $\chi_m\approx3.5\times10^{-3}$, is unusually strong). Ferromagnets are hysteretic: $B$ saturates (iron near 2 T), a remanent $B_r$ survives at $H = 0$ (permanent magnets), and the coercive field $-H_c$ removes it. Slides' mnemonic: **Para** ↔ **Pos**itive.

**Where the μ goes.** $\mu$ replaces $\mu_0$ wherever the medium fills the field region: $\mathbf{B} = \mu\mathbf{H}$ ($\mu nI$ in a solenoid), $L = n^2\mu A\ell$, $\mathcal{L} = \tfrac{\mu}{2\pi}\ln\tfrac ba$, energy density $\tfrac12\mu H^2$; from [[3-maxwell-and-waves/18-the-wave-equation-and-plane-tem-waves|Lecture 18]] on, wave speed $1/\sqrt{\mu\epsilon}$ and [[concepts/intrinsic-impedance|intrinsic impedance]] $\sqrt{\mu/\epsilon}$. Ampère's law for $\mathbf{H}$ needs no $\mu$: $\oint\mathbf{H}\cdot d\mathbf{l} = I_{\text{free}}$.

**What a core changes.** At fixed free current, a core whose surfaces are *parallel* to $\mathbf{H}$ (long solenoid core, toroid, coax filling) leaves $\mathbf{H}$ unchanged, while $\mathbf{B}$, flux and $L$ grow by $\mu_r$. Example: $n = 1000$ turns/m, $I = 2$ A, $\mu_r = 100$: $H = 2000$ A/m either way, $B$ rises from 2.51 mT to 0.251 T. If $\mathbf{H}$ crosses its surface (short rod, sphere, gap), a demagnetizing field lowers it inside: a sphere in uniform $\mathbf{H}_0$ has $\mathbf{H}_{\text{in}} = 3\mathbf{H}_0/(\mu_r+2)$, so $B_{\text{in}} < 3\mu_0H_0$ for any $\mu_r$. An iron core ($\mu_r = 5000$) in the coil above would "give" 12.6 T, far past saturation.

**At an interface** without free surface current, $H_t$ and $B_n$ are continuous: $H_{2n} = (\mu_1/\mu_2)H_{1n}$, $B_{2t} = (\mu_2/\mu_1)B_{1t}$, $\tan\theta_1/\tan\theta_2 = \mu_1/\mu_2$. Iron into air: 85° from the normal inside, 0.13° outside, as $\mathbf{E}$ leaves a conductor. A free sheet changes only the tangential condition: $\hat n\times(\mathbf{H}_1-\mathbf{H}_2) = \mathbf{J}_s$.

> [!trap]
> - $\mu_r = 100$ means $\chi_m = 99$: matters for $\mathbf{M}$, hardly for $\mathbf{B}$.
> - $\mathbf{B} = \mu\mathbf{H}$ with the local $\mu$.
> - $\nabla\cdot\mathbf{H} = 0$ only where $\mu$ is uniform; the law is $\nabla\cdot\mathbf{B} = 0$.
> - Ferromagnets: tabulated $\mu_r$ and linear formulas hold for small fields only.

**Where it appears.** [[3-maxwell-and-waves/17-magnetization-and-maxwells-equations-in-matter|Lecture 17]], [[2-magnetostatics/15-inductance-magnetic-energy-and-the-potentials|Lecture 15]], [[problems/fields-across-a-magnetic-interface]], [[problems/coax-inductance-and-the-lc-product]] ($\mathcal{L}\mathcal{C} = \mu\epsilon$).

**Practice.** [[practice/topics#magnetization-and-magnetic-media|Magnetization and magnetic media]] (11 problems) — for example [[practice/17-magnetization-and-maxwell-in-matter#172-four-rods-in-a-solenoid|17.2 Four rods in a solenoid]] (easy), [[practice/17-magnetization-and-maxwell-in-matter#176-graded-magnetization-in-a-slab|17.6 Graded magnetization in a slab]] (medium), [[practice/17-magnetization-and-maxwell-in-matter#179-electret-and-magnet-twins|17.9 Electret and magnet twins]] (hard).

Related: [[concepts/magnetization]] · [[concepts/magnetic-field]] · [[concepts/inductance]] · [[concepts/permittivity]] · [[concepts/boundary-conditions]].
