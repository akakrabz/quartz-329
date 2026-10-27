---
title: "Permeability, susceptibility, and B = μH"
description: "H = B/μ₀ − M keeps Maxwell's equations in matter in their free-space form with free sources only; in linear media M = χmH (no μ₀), B = μH, μ = μrμ₀. Cores, the cored solenoid, demagnetization, and where μ enters later formulas."
tags: [concept, waves]
aliases: ["relative permeability", "magnetic susceptibility", "B = μH", "Maxwell's equations in matter", "macroscopic Maxwell equations", "auxiliary fields", "solenoid with a core", "magnetizing field", "demagnetizing field"]
---

> [!key] Maxwell's equations in matter ("the same form as before")
> $$
> \begin{gathered}
> \nabla\cdot\mathbf{D} = \rho,\qquad \nabla\cdot\mathbf{B} = 0,\\[4pt]
> \nabla\times\mathbf{E} = -\frac{\partial\mathbf{B}}{\partial t},\qquad \nabla\times\mathbf{H} = \mathbf{J}+\frac{\partial\mathbf{D}}{\partial t},
> \end{gathered}
> $$
> with the **auxiliary fields**
> $$
> \mathbf{D}\equiv\epsilon_0\mathbf{E}+\mathbf{P},\qquad\qquad \mathbf{H}\equiv\frac{\mathbf{B}}{\mu_0}-\mathbf{M},
> $$
> $\rho$, $\mathbf{J}$ **free** only; linear isotropic media $\mathbf{D} = \epsilon\mathbf{E}$, $\mathbf{B} = \mu\mathbf{H}$. Integral form $\oint_C\mathbf{H}\cdot d\mathbf{l} = I_{f,\text{enc}} + \dfrac{d}{dt}\displaystyle\int_S\mathbf{D}\cdot d\mathbf{S}$: free current only, whatever material the loop crosses.

**Constitutive relation of a linear, isotropic magnetic medium:**

$$
\mathbf{M} = \chi_m\mathbf{H}\quad\Longrightarrow\quad \mathbf{B} = \mu_0(\mathbf{H}+\mathbf{M}) = \mu_0(1+\chi_m)\mathbf{H} = \mu\mathbf{H},\qquad \mu = \mu_0(1+\chi_m) = \mu_r\mu_0,\quad \mu_r = 1+\chi_m .
$$

**Susceptibility** $\chi_m$, **relative permeability** $\mu_r$ (slides only): dimensionless. **Permeability** $\mu$ in H/m, $\mu_0 = 4\pi\times10^{-7}$ H/m. $\mathbf{H}$ is the total field at that point. Twin (slides): $\mathbf{P} = \epsilon_0\chi_e\mathbf{E}$, $\mathbf{D} = \epsilon_0(1+\chi_e)\mathbf{E} = \epsilon\mathbf{E}$. Measured inductances of coils on magnetic materials (notes; the $L\propto\mu$ of [[concepts/inductance|Inductance]]) show $\mathbf{M}\propto\mathbf{H}$ for most materials.

**Physics: H redefined.** The microscopic Ampère–Maxwell law counts all current ([[concepts/magnetization|Magnetization M and magnetization current]] for the bound terms):

$$
\nabla\times\frac{\mathbf{B}}{\mu_0} = \mathbf{J}_f + \frac{\partial\mathbf{P}}{\partial t} + \nabla\times\mathbf{M} + \frac{\partial(\epsilon_0\mathbf{E})}{\partial t}.
$$

The curl term moves left; the polarization current joins the displacement current:

$$
\nabla\times\Big(\frac{\mathbf{B}}{\mu_0}-\mathbf{M}\Big) = \mathbf{J}_f + \frac{\partial}{\partial t}(\epsilon_0\mathbf{E}+\mathbf{P}).
$$

With Gauss's $\nabla\cdot(\epsilon_0\mathbf{E}+\mathbf{P}) = \rho_f$ ([[concepts/electric-flux-density|Electric flux density D]]), name the combinations and drop $f$: the key box. Faraday's law and $\nabla\cdot\mathbf{B} = 0$ have no sources and use the Lorentz-force fields $\mathbf{E}$, $\mathbf{B}$ ($q(\mathbf{E}+\mathbf{v}\times\mathbf{B})$): unchanged.

**What sets what** (notes, footnote 6): free currents set the **magnetizing field** $\mathbf{H}$, the material sets $\mathbf{B} = \mu\mathbf{H}$ — as free charge sets $\mathbf{D}$, the medium $\mathbf{E} = \mathbf{D}/\epsilon$ (exact only with symmetry; trap below). Notes: $\mathbf{H}$ *magnetic field intensity*, $\mathbf{B}$ *flux density*, $\mu_o$ for $\mu_0$; slides: $\mathbf{H}$ *magnetic field*.

**Three classes.** Diamagnets ($\chi_m\approx-10^{-5}$), paramagnets ($10^{-5}$ to $10^{-3}$) and ferromagnets ($10^2$ to $10^6$, non-linear with hysteresis) — mechanisms, the slides' table of values, domains and hysteresis are on [[concepts/magnetic-materials|Dia-, para- and ferromagnetism]]. For dia- and paramagnets problems take $\mu = \mu_0$.

**Where the μ goes.** $\mu$ replaces $\mu_0$ wherever the medium fills the field region: $\mathbf{B} = \mu\mathbf{H}$ ($\mu nI$ in a solenoid), $L = n^2\mu A\ell$, $\mathcal{L} = \tfrac{\mu}{2\pi}\ln\tfrac ba$, energy density $\tfrac12\mu H^2$; from [[3-maxwell-and-waves/18-the-wave-equation-and-plane-tem-waves|Lecture 18]] on, wave speed $1/\sqrt{\mu\epsilon}$ and [[concepts/intrinsic-impedance|intrinsic impedance]] $\sqrt{\mu/\epsilon}$. Ampère's law for $\mathbf{H}$ needs no $\mu$: $\oint\mathbf{H}\cdot d\mathbf{l} = I_{\text{free}}$. **Inductance is proportional to μ** ([[2-magnetostatics/15-inductance-magnetic-energy-and-the-potentials|Lecture 15]]: also $\tfrac12LI^2$, $\tfrac12\mu H^2$): free current fixes $\mathbf{H}$, flux $\Psi = \int\mu\mathbf{H}\cdot d\mathbf{S}$ scales with $\mu$. Cored solenoid $L = n^2\mu A\ell$; $n = 1000$/m, $A = 1$ cm², $\ell = 10$ cm: 12.6 μH → 1.26 mH at $\mu_r = 100$.

**The solenoid with a core** (notes). A long solenoid ($n$ turns/m, current $I_0$) around a long, thinner core. Without it ([[concepts/solenoids-and-toroids|Solenoids and toroids]], [[2-magnetostatics/13-current-sheets-solenoids-and-the-vector-potential#3-the-solenoid|Lecture 13 §3]]) $\mathbf{H}_0 = nI_0\hat z$, $\mathbf{B}_0 = \mu_0nI_0\hat z$; the core's loops, a long "solenoid" themselves, add $\mu_0\mathbf{M}$ inside only:

$$
\mathbf{B} = \mathbf{B}_0 + \mu_0\mathbf{M}\ \ \text{in the core},\qquad \mathbf{B} = \mathbf{B}_0\ \ \text{in the air around it}\qquad\Longrightarrow\qquad \mathbf{H} = \frac{\mathbf{B}}{\mu_0}-\mathbf{M} = nI_0\hat z\ \ \text{in both}.
$$

$\mathbf{B}$ differs, $\mathbf{H}$ does not — "analogous with $\mathbf{D}$ in dielectrics". Core $\mathbf{B}$ is below $\mathbf{B}_0$ in diamagnets, above in para- and ferromagnets.

> [!derivation]- Where μ₀M comes from: stacks of atomic loops (the notes' model)
> $N = 1/(\Delta x\,\Delta y\,\Delta z)$ atoms/m³, each a loop of area $A_l$, current $I_l$, $\mathbf{m} = I_lA_l\hat z$. A column spaced $\Delta z$ is a solenoid with $1/\Delta z$ turns/m: field $\mu_0I_l/\Delta z$ inside $A_l$, zero outside. One column per $\Delta x\,\Delta y$, so the average is
> $$
> \frac{A_l}{\Delta x\,\Delta y}\cdot\mu_0\frac{I_l}{\Delta z}\,\hat z = \mu_0NI_lA_l\,\hat z = \mu_0N\mathbf{m} = \mu_0\mathbf{M}.
> $$
> Lecture 8's dipole lattice gave $-\mathbf{P}/\epsilon_0$: between its charges a dipole's field runs $+\to-$, *against* $\mathbf{p}$; inside a loop the field runs *along* $\mathbf{m}$. Hence $+\mathbf{P}$ in $\mathbf{D}$, $-\mathbf{M}$ in $\mathbf{H}$.

The same holds for any core whose surfaces are *parallel* to $\mathbf{H}$ (toroid, coax filling): $\mathbf{H}$ unchanged, $\mathbf{B}$, flux and $L$ up by $\mu_r$. If $\mathbf{H}$ crosses the surface (short rod, sphere, gap), a demagnetizing field lowers it inside (trap below).

> [!recipe] Problems with magnetic media
> 1. **$\mathbf{H}$ from free currents alone**: Ampère, sheets $\tfrac12\mathbf{J}_s\times\hat n$, superposition, boundary conditions.
> 2. **$\mathbf{B} = \mu\mathbf{H}$** region by region; then flux, inductance or force.
> 3. **$\mathbf{M} = \mathbf{B}/\mu_0-\mathbf{H} = \chi_m\mathbf{H}$ last.** Check: $\nabla\times\mathbf{M}$, $\mathbf{M}\times\hat n$ plus free currents in *vacuum* formulas return $\mathbf{B}$.
>
> Lecture 9's chain (free charge → $\mathbf{D}$ → $\mathbf{E} = \mathbf{D}/\epsilon$ → $V$ → $\mathbf{P}$), translated.

**Examples.**

> [!example] This site's numbers — a coil with and without a core
> $n = 1000$ turns/m, $I_0 = 2$ A, core $\chi_m = 99$ ($\mu_r = 100$).
> - $\mathbf{H} = nI_0 = 2000$ A/m in core and air (Ampère encloses free $n\ell I_0$ whatever the core).
> - Air: $B_0 = \mu_0H = 2.51$ mT. Core: $M = \chi_mH = 1.98\times10^{5}$ A/m, $\mu_0M = 0.249$ T, $B = \mu_0(H+M) = 0.251$ T $= 100B_0$.
> - Iron, $\mu_r = 5000$: linearly 12.6 T — impossible; saturation near 2.2 T ([[concepts/magnetic-materials|Dia-, para- and ferromagnetism]]).

- *At an interface* without free surface current, $H_t$ and $B_n$ are continuous: $H_{2n} = (\mu_1/\mu_2)H_{1n}$, $B_{2t} = (\mu_2/\mu_1)B_{1t}$, $\tan\theta_1/\tan\theta_2 = \mu_1/\mu_2$. Iron into air: 85° from the normal inside, 0.13° outside, as $\mathbf{E}$ leaves a conductor. A free sheet changes only the tangential condition: $\hat n\times(\mathbf{H}_1-\mathbf{H}_2) = \mathbf{J}_s$ ([[concepts/boundary-conditions|Boundary conditions at an interface]], [[problems/fields-across-a-magnetic-interface|Worked problem — Fields across a magnetic interface]]).
- *Slab between current sheets* ($\mu_r = 100$, sheets $\mp0.1\hat y$ A/m): $\mathbf{H} = 0.1\hat x$ A/m with or without the slab, $\mathbf{B}_{\text{slab}} = 1.26\times10^{-5}\hat x$ T, 100 times the empty value — worked on [[concepts/magnetization|Magnetization M and magnetization current]].

> [!trap] No μ₀ in M = χm H (the point highlighted on the slide)
> - $\mathbf{P}$ [C/m²] and $\mathbf{E}$ [V/m] differ, hence $\epsilon_0$; $\mathbf{M}$, $\mathbf{H}$ are both A/m. "$\mathbf{M} = \mu_0\chi_m\mathbf{H}$" is in tesla.
> - $\mathbf{M} = \mathbf{B}/\mu_0 - \mathbf{H}$; not $\mathbf{B}/\mu_0$, nor $\mathbf{B}/\mu - \mathbf{H}$ ($\equiv0$, like "$\mathbf{P} = \mathbf{D}-\epsilon\mathbf{E}$").
> - $\mathbf{H} = \mathbf{B}/\mu_0 - \mathbf{M} = \mathbf{B}/\mu$; never $\mathbf{B}/\mu - \mathbf{M}$.
> - The slides' concept map writes $\mathbf{M} = \mathbf{B}\,(\mu-\mu_0)/(\mu\mu_0)$: the same $\chi_m\mathbf{H}$, via $\mathbf{B}$.
> - $\mu_r = 100$ means $\chi_m = 99$: matters for $\mathbf{M}$, hardly for $\mathbf{B}$.

> [!trap] "H is the same with or without the core" is a fact about this geometry, not a law
> - It needs a long core along $\mathbf{H}$ ($H_t$ continuous at the side wall, ends far away). A short or crosswise core's ends, where $\mathbf{M}$ stops, make a *demagnetizing* field: $\mathbf{H}$ inside drops below $nI_0$ (for $\chi_m>0$; slightly above it in a diamagnet).
> - Sphere in applied $\mathbf{H}_0$: $\mathbf{H}_0-\mathbf{M}/3 = 3\mathbf{H}_0/(\mu_r+2)$ inside, so even iron ($\mu_r\to\infty$) multiplies $B$ by under 3, against $\mu_r$ for a long rod ($B_{\text{in}} < 3\mu_0H_0$ for any $\mu_r$). Twin of Lecture 8's slab trap (sphere: $\mathbf{E}_p = -\mathbf{P}/3\epsilon_0$); the slides' $\mathbf{M} = \chi_m\mathbf{H}_{\text{ext}}$ shares the caveat.
> - Always true: $\nabla\times\mathbf{H} = \mathbf{J}_{\text{free}}$ (plus $\partial\mathbf{D}/\partial t$) and the boundary conditions. $\nabla\cdot\mathbf{H} = 0$ only where $\mu$ is uniform; the law is $\nabla\cdot\mathbf{B} = 0$.
> - Ferromagnets: tabulated $\mu_r$ and linear formulas hold for small fields only.

> [!exam] On exams
> "No $\mu_0$" in $\mathbf{M} = \chi_m\mathbf{H}$; $\mathbf{H}$ from free current, then $\mathbf{B} = \mu\mathbf{H}$, then $\mathbf{M}$ (the recipe), with the $\mu_r = 1$ comparison; interface problems like FA26 Exam 1 #3 with $\epsilon\to\mu$, $\mathbf{E}\to\mathbf{H}$; $L$ and $\mathcal{L}$ scale with $\mu$.

**Where it appears.** [[3-maxwell-and-waves/17-magnetization-and-maxwells-equations-in-matter#4-h-redefined-maxwells-equations-in-matter|Lecture 17 §4]] (derived; linear media; cored solenoid), [[3-maxwell-and-waves/17-magnetization-and-maxwells-equations-in-matter#6-boundary-conditions-in-magnetic-media|§6]] (recipe, slab example), [[2-magnetostatics/15-inductance-magnetic-energy-and-the-potentials|Lecture 15]] ($L\propto\mu$), [[3-maxwell-and-waves/18-the-wave-equation-and-plane-tem-waves#7-in-matter-and-on-a-cable|Lecture 18 §7]] ($v$, $\eta$ in matter), [[problems/fields-across-a-magnetic-interface|Worked problem — Fields across a magnetic interface]], [[problems/coax-inductance-and-the-lc-product|Worked problem — Inductance of a coax, and the 𝓛𝓒 product]] ($\mathcal{L}\mathcal{C} = \mu\epsilon$).

**Related.** [[concepts/magnetization|Magnetization M and magnetization current]] · [[concepts/magnetic-materials|Dia-, para- and ferromagnetism]] · [[concepts/maxwells-equations|Maxwell's equations]] · [[concepts/magnetic-field|Magnetic field: B and H]] · [[concepts/inductance|Inductance]] · [[concepts/permittivity|Permittivity, susceptibility, and D = εE]] · [[concepts/boundary-conditions|Boundary conditions at an interface]].

**Practice.** [[practice/topics#magnetization-and-magnetic-media|Magnetization and magnetic media]] (11 problems) — for example [[practice/17-magnetization-and-maxwell-in-matter#172-four-rods-in-a-solenoid|17.2 Four rods in a solenoid]] (easy), [[practice/17-magnetization-and-maxwell-in-matter#176-graded-magnetization-in-a-slab|17.6 Graded magnetization in a slab]] (medium), [[practice/17-magnetization-and-maxwell-in-matter#179-electret-and-magnet-twins|17.9 Electret and magnet twins]] (hard).
