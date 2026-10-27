---
title: "Lecture 17 — Magnetization current and Maxwell's equations in matter"
description: "Atomic current loops add up to a magnetization M that leaves a current ∇×M (surface M × n̂); H = B/μ₀ − M keeps Maxwell's equations with free sources, B = μH, μ = μ₀(1 + χm). Dia- and paramagnets are nearly vacuum; ferromagnets are non-linear with memory."
tags: [lecture, waves]
lecture: 17
---

*Lecture 17 · course notes §17 · slides "Magnetic Materials / Maxwell's equations in material media" · prev: [[3-maxwell-and-waves/16-charge-conservation-displacement-current-and-maxwells-equations|Lecture 16]] · next: [[3-maxwell-and-waves/18-the-wave-equation-and-plane-tem-waves|Lecture 18]] · practice: [[practice/17-magnetization-and-maxwell-in-matter|12 problems]]*

> [!abstract] In one breath
> Lecture 16's equations count *every* charge, including the roughly $10^{30}$ bound electrons per cubic metre in a metal, so we average. Bound electrons circulate (orbits, spins) as tiny loops whose moments add up to the **magnetization** $\mathbf{M}$; where it changes or ends, a **magnetization current** $\nabla\times\mathbf{M}$ (surface: $\mathbf{M}\times\hat n$) survives. Folding it into $\mathbf{H} = \mathbf{B}/\mu_0 - \mathbf{M}$ keeps Maxwell's equations with free sources only. Mostly $\mathbf{M} = \chi_m\mathbf{H}$ — no $\mu_0$ — so $\mathbf{B} = \mu\mathbf{H}$, $\mu = \mu_0(1+\chi_m)$. Dia- and paramagnets ($\lvert\chi_m\rvert$ around $10^{-5}$) are nearly vacuum; ferromagnets ($\chi_m$ from hundreds to hundreds of thousands) are non-linear with memory.

## 1. Why matter needs new bookkeeping

Lecture 16's equations, with $\mathbf{D} = \epsilon_0\mathbf{E}$ and $\mathbf{B} = \mu_0\mathbf{H}$ written out:

$$
\begin{gathered}
\nabla\cdot(\epsilon_0\mathbf{E}) = \rho,\qquad \nabla\cdot\mathbf{B} = 0,\\[4pt]
\nabla\times\mathbf{E} = -\frac{\partial\mathbf{B}}{\partial t},\qquad \nabla\times\frac{\mathbf{B}}{\mu_0} = \mathbf{J}+\frac{\partial(\epsilon_0\mathbf{E})}{\partial t}.
\end{gathered}
$$

These **microscopic** equations need every charge in $\rho$ and $\mathbf{J}$ — hopeless in matter: a cubic millimetre of copper holds about $2.5\times10^{21}$ electrons, nearly all bound. As for dielectrics ([[1-electrostatics/08-conductors-dielectrics-and-polarization|Lecture 8]]), average over many atoms and split sources into **free** (you control them) and **bound** (the material supplies them):

> [!key] Sources in matter, averaged
> $$
> \rho = \rho_f - \nabla\cdot\mathbf{P},\qquad \mathbf{J} = \mathbf{J}_f + \frac{\partial\mathbf{P}}{\partial t} + \nabla\times\mathbf{M}.
> $$
> | term | name | physically | first met |
> |---|---|---|---|
> | $\rho_f$, $\mathbf{J}_f$ | free | placed charges; drifting carriers ($\sigma\mathbf{E}$) | Lectures 2, 8, 12 |
> | $-\nabla\cdot\mathbf{P}$ | bound charge | uncancelled dipole ends | [[1-electrostatics/08-conductors-dielectrics-and-polarization\|Lecture 8]] |
> | $\partial\mathbf{P}/\partial t$ | polarization current | bound charges moving as dipoles stretch | [[1-electrostatics/11-lorentz-drude-models-for-conductivity-and-susceptibility#5-polarization-current-bound-charges-that-carry-an-ac-current\|Lecture 11]] |
> | $\nabla\times\mathbf{M}$ | magnetization current | uncancelled atomic loops | this lecture |

$\mathbf{P}$, $\mathbf{M}$: electric, magnetic dipole moment per unit volume. Bound sources conserve charge by themselves: $\partial_t(-\nabla\cdot\mathbf{P}) + \nabla\cdot(\partial_t\mathbf{P}) = 0$, $\nabla\cdot(\nabla\times\mathbf{M}) = 0$.

## 2. Atomic magnetic dipoles

<!-- fig:mag-moment-torque -->

An orbiting electron is a loop current $I = e/T$, flowing **opposite** to its velocity; from far away it is a magnetic dipole ([[2-magnetostatics/13-current-sheets-solenoids-and-the-vector-potential#6-the-current-loop-and-the-magnetic-dipole|Lecture 13]]):

> [!key] Magnetic dipole moment, and the torque a field exerts on it
> $$
> \mathbf{m} = I\mathbf{A} = IA\,\hat n\quad[\text{A}\cdot\text{m}^2],\qquad\qquad \mathbf{T} = \mathbf{m}\times\mathbf{B}\quad[\text{N}\cdot\text{m}],
> $$
> $\hat n$ by the right-hand rule. Circle: $m = I\pi a^2$ (slides: $\mathbf{m} = I(\pi a^2)\hat a_z$ in the $xy$-plane). Uniform $\mathbf{B}$: zero net force, $\oint I\,d\mathbf{l}\times\mathbf{B} = I(\oint d\mathbf{l})\times\mathbf{B} = 0$, but a torque $mB\sin\theta$ turns $\mathbf{m}$ toward $\mathbf{B}$ like a compass needle (slide: the couple $I\,d\mathbf{l}\times\mathbf{B}_0$ on a tilted orbit). Twin: $\mathbf{p}\times\mathbf{E}$.

> [!derivation]- The torque on a square loop, side by side
> Square loop, side $\ell$, $\mathbf{m} = I\ell^2(0,\sin\theta,\cos\theta)$, tilted by $\theta$ about $x$ from $\mathbf{B} = B\hat z$. Two sides run along $\pm\hat x$ at $\mp\tfrac\ell2\hat u$, $\hat u = (0,\cos\theta,-\sin\theta)$ (so $\hat x\times\hat u = \mathbf{m}/m$):
> $$
> \mathbf{F}_{+x} = I\ell\,\hat x\times B\hat z = -I\ell B\,\hat y,\qquad \mathbf{F}_{-x} = +I\ell B\,\hat y .
> $$
> The sides along $\pm\hat u$ feel $\pm I\ell B\cos\theta\,\hat x$ on one line through the centre: no torque. Net force zero; torque about the centre:
> $$
> \Big(-\tfrac\ell2\hat u\Big)\times(-I\ell B\hat y) + \Big(\tfrac\ell2\hat u\Big)\times(I\ell B\hat y) = I\ell^2B\,(\hat u\times\hat y) = I\ell^2B\sin\theta\,\hat x = \mathbf{m}\times\mathbf{B}.
> $$
> Tiling a flat loop with squares (shared edges cancel, §3) extends it to any planar loop in uniform $\mathbf{B}$.

**Sources of atomic loops** (notes): **orbital** motion (slides' **L**); electron **spin** (slides' **S**), quantized, with no working classical picture; charge motion **inside protons and neutrons**, far weaker. Paired electrons cancel; only unpaired ones leave a permanent moment.

> [!example] Example (this site's numbers) — the size of an atomic moment
> Bohr hydrogen: $a_0 = 5.29\times10^{-11}$ m, $v = 2.19\times10^{6}$ m/s: $I = ev/(2\pi a_0) \approx 1.06$ mA through about $10^{-20}$ m², $m = I\pi a_0^2 = eva_0/2 \approx 9.28\times10^{-24}$ A·m² — the **Bohr magneton** $\mu_B = 9.27\times10^{-24}$ A·m² to rounding, the unit of atomic and spin moments; $\mathbf{m}$ antiparallel to the angular momentum.

**From moments to magnetization.** With no field, thermal motion scatters the moments to zero sum (slide 3); a field torques them toward alignment (slide 5):

> [!key] Magnetization
> $$
> \mathbf{M} = N\mathbf{m}\qquad\Big[\frac{1}{\text{m}^3}\cdot\text{A}\cdot\text{m}^2 = \text{A/m}\Big],
> $$
> $N$ atoms per unit volume, $\mathbf{m}$ the *average* moment. Unit of $\mathbf{H}$ (ink: "same H") and of a surface current (§3); twin $\mathbf{P} = N\mathbf{p}$ [C/m²], a surface-charge unit.

Upper limit: iron, $N\approx8.5\times10^{28}$ atoms/m³ at about $2.2\,\mu_B$ each, all aligned: $M\approx1.7\times10^{6}$ A/m, $\mu_0M\approx2.2$ T — why iron cores saturate near 2 T.

## 3. The magnetization current

**Why a curl? (the notes' argument).** Bound charge is conserved, $\partial\rho_b/\partial t + \nabla\cdot\mathbf{J}_b = 0$; with $\rho_b = -\nabla\cdot\mathbf{P}$:

$$
\nabla\cdot\Big(\mathbf{J}_b - \frac{\partial\mathbf{P}}{\partial t}\Big) = 0 .
$$

So bound current beyond $\partial\mathbf{P}/\partial t$ is divergence-free, hence a curl (as $\mathbf{B} = \nabla\times\mathbf{A}$, [[2-magnetostatics/13-current-sheets-solenoids-and-the-vector-potential#5-the-vector-potential|Lecture 13]]):

> [!key] Bound current density
> $$
> \mathbf{J}_b = \frac{\partial\mathbf{P}}{\partial t} + \nabla\times\mathbf{M}.
> $$
> $\partial\mathbf{P}/\partial t$ is *not sufficient* (notes): orbits and spins are closed loops that never pile up charge, invisible to continuity. $\mathbf{J}_M = \nabla\times\mathbf{M}$ (slides' symbol) is the **magnetization current density** [A/m²].

This only *allows* the term (a gradient could be added to $\mathbf{M}$, as to $\mathbf{A}$); $\mathbf{M} = N\mathbf{m}$ pins it down, and the picture shows its curl is the leftover loop current.

<!-- fig:mag-loops-surface-current -->

**Loops cancel inside, survive at the edges.** Cells of side $s$, loop current $I$: $m = Is^2$, $M = m/s^3 = I/s$. Interior edges cancel in pairs; boundary edges leave $I$ per length $s$, a surface current $I/s = M$ [A/m]. If $\mathbf{M}$ varies, shared edges stop cancelling: $\mathbf{M} = M_z(x)\hat z$ leaves $-\partial M_z/\partial x$ along $\hat y$, exactly $(\nabla\times\mathbf{M})_y$.

> [!key] Magnetization current: volume and surface
> $$
> \mathbf{J}_M = \nabla\times\mathbf{M}\quad[\text{A/m}^2],\qquad\qquad \mathbf{J}_{sM} = \mathbf{M}\times\hat n\quad[\text{A/m}],
> $$
> $\hat n$ **outward**; at an interface ($\hat n$ from 2 into 1) $\mathbf{J}_{sM} = \hat n\times(\mathbf{M}_1-\mathbf{M}_2)$. **The surface term is this site's addition**, twin of $\rho_{sb} = \mathbf{P}\cdot\hat n$ ([[1-electrostatics/08-conductors-dielectrics-and-polarization#3-dielectrics-bound-charge-and-polarization|Lecture 8]]): across the layer where $\mathbf{M}$ falls to zero, $\nabla$ acts as $\hat n$ on the jump (outside minus inside), $\hat n\times(0-\mathbf{M}) = \mathbf{M}\times\hat n$, as $-\hat n\cdot(0-\mathbf{P}) = \mathbf{P}\cdot\hat n$.

**A magnetized rod is a solenoid.** $\mathbf{M} = M\hat z$ (figure, right): side $\mathbf{M}\times\hat r = M\hat\phi$, a winding with $nI\to M$; ends $\mathbf{M}\times(\pm\hat z) = 0$. Inside a long rod $\mathbf{B}\approx\mu_0\mathbf{M}$ (§4). A $\mu_0M\approx1.3$ T magnet acts like 1000 turns/m carrying 1000 A.

## 4. H redefined: Maxwell's equations in matter

The microscopic Ampère–Maxwell law counts all current:

$$
\nabla\times\frac{\mathbf{B}}{\mu_0} = \mathbf{J}_f + \frac{\partial\mathbf{P}}{\partial t} + \nabla\times\mathbf{M} + \frac{\partial(\epsilon_0\mathbf{E})}{\partial t}.
$$

The curl term moves left; the polarization current joins the displacement current:

$$
\nabla\times\Big(\frac{\mathbf{B}}{\mu_0}-\mathbf{M}\Big) = \mathbf{J}_f + \frac{\partial}{\partial t}(\epsilon_0\mathbf{E}+\mathbf{P}).
$$

With Gauss's $\nabla\cdot(\epsilon_0\mathbf{E}+\mathbf{P}) = \rho_f$ (Lecture 8), name the combinations and drop $f$:

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

Faraday's law and $\nabla\cdot\mathbf{B} = 0$ have no sources and use the Lorentz-force fields $\mathbf{E}$, $\mathbf{B}$ ($q(\mathbf{E}+\mathbf{v}\times\mathbf{B})$): unchanged.

**What sets what** (notes, footnote 6): free currents set the **magnetizing field** $\mathbf{H}$, the material sets $\mathbf{B} = \mu\mathbf{H}$ — as free charge sets $\mathbf{D}$, the medium $\mathbf{E} = \mathbf{D}/\epsilon$ (exact only with symmetry; trap below). Notes: $\mathbf{H}$ *magnetic field intensity*, $\mathbf{B}$ *flux density*, $\mu_o$ for $\mu_0$; slides: $\mathbf{H}$ *magnetic field*.

### Linear media: χm and μ

Measured inductances of coils on magnetic materials (notes; footnote: Lecture 15's $L\propto\mu$) show $\mathbf{M}\propto\mathbf{H}$ for most materials:

> [!key] Linear magnetic media
> $$
> \mathbf{M} = \chi_m\mathbf{H}\quad\Longrightarrow\quad \mathbf{B} = \mu_0(\mathbf{H}+\mathbf{M}) = \mu_0(1+\chi_m)\mathbf{H} = \mu\mathbf{H},\qquad \mu = \mu_0(1+\chi_m) = \mu_r\mu_0,\quad \mu_r = 1+\chi_m .
> $$
> **Susceptibility** $\chi_m$, **relative permeability** $\mu_r$ (slides only): dimensionless. **Permeability** $\mu$ in H/m, $\mu_0 = 4\pi\times10^{-7}$ H/m. $\mathbf{H}$ is the total field at that point. Twin (slide 8): $\mathbf{P} = \epsilon_0\chi_e\mathbf{E}$, $\mathbf{D} = \epsilon_0(1+\chi_e)\mathbf{E} = \epsilon\mathbf{E}$.

> [!trap] No μ₀ in M = χm H (the point highlighted on the slide)
> - $\mathbf{P}$ [C/m²] and $\mathbf{E}$ [V/m] differ, hence $\epsilon_0$; $\mathbf{M}$, $\mathbf{H}$ are both A/m. "$\mathbf{M} = \mu_0\chi_m\mathbf{H}$" is in tesla.
> - $\mathbf{M} = \mathbf{B}/\mu_0 - \mathbf{H}$; not $\mathbf{B}/\mu_0$, nor $\mathbf{B}/\mu - \mathbf{H}$ ($\equiv0$, like "$\mathbf{P} = \mathbf{D}-\epsilon\mathbf{E}$").
> - $\mathbf{H} = \mathbf{B}/\mu_0 - \mathbf{M} = \mathbf{B}/\mu$; never $\mathbf{B}/\mu - \mathbf{M}$.
> - Concept map's $\mathbf{M} = \mathbf{B}\,(\mu-\mu_0)/(\mu\mu_0)$ = $\chi_m\mathbf{H}$ via $\mathbf{B}$.

### The solenoid with a core

The notes: a long solenoid ($n$ turns/m, current $I_0$) around a long, thinner core. Without it ([[2-magnetostatics/13-current-sheets-solenoids-and-the-vector-potential#3-the-solenoid|Lecture 13]]) $\mathbf{H}_0 = nI_0\hat z$, $\mathbf{B}_0 = \mu_0nI_0\hat z$; the core's loops, a long "solenoid" themselves, add $\mu_0\mathbf{M}$ inside only:

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

> [!example] Example (this site's numbers) — a coil with and without a core
> $n = 1000$ turns/m, $I_0 = 2$ A, core $\chi_m = 99$ ($\mu_r = 100$).
> - $\mathbf{H} = nI_0 = 2000$ A/m in core and air (Ampère encloses free $n\ell I_0$ whatever the core).
> - Air: $B_0 = \mu_0H = 2.51$ mT. Core: $M = \chi_mH = 1.98\times10^{5}$ A/m, $\mu_0M = 0.249$ T, $B = \mu_0(H+M) = 0.251$ T $= 100B_0$.
> - Iron, $\mu_r = 5000$: linearly 12.6 T — impossible; saturation near 2.2 T (§2).

> [!trap] "H is the same with or without the core" is a fact about this geometry, not a law
> It needs a long core along $\mathbf{H}$ ($H_t$ continuous at the side wall, ends far away). A short or crosswise core's ends, where $\mathbf{M}$ stops, make a *demagnetizing* field: $\mathbf{H}$ inside drops below $nI_0$ (for $\chi_m>0$; slightly above it in a diamagnet). Sphere in applied $\mathbf{H}_0$: $\mathbf{H}_0-\mathbf{M}/3 = 3\mathbf{H}_0/(\mu_r+2)$ inside, so even iron ($\mu_r\to\infty$) multiplies $B$ by under 3, against $\mu_r$ for a long rod. Twin of Lecture 8's slab trap (sphere: $\mathbf{E}_p = -\mathbf{P}/3\epsilon_0$); the slides' $\mathbf{M} = \chi_m\mathbf{H}_{\text{ext}}$ shares the caveat. Always true: $\nabla\times\mathbf{H} = \mathbf{J}_{\text{free}}$ (plus $\partial\mathbf{D}/\partial t$) and the §6 boundary conditions.

**Inductance is proportional to μ** ([[2-magnetostatics/15-inductance-magnetic-energy-and-the-potentials|Lecture 15]]: also $\tfrac12LI^2$, $\tfrac12\mu H^2$): free current fixes $\mathbf{H}$, flux $\Psi = \int\mu\mathbf{H}\cdot d\mathbf{S}$ scales with $\mu$. Cored solenoid $L = n^2\mu A\ell$; $n = 1000$/m, $A = 1$ cm², $\ell = 10$ cm: 12.6 μH → 1.26 mH at $\mu_r = 100$.

## 5. Dia-, para- and ferromagnetism

| | diamagnetic | paramagnetic | ferromagnetic |
|---|---|---|---|
| $\chi_m$ | about $-10^{-5}$ | about $10^{-5}$ to $10^{-3}$ | $10^2$ to $10^6$, not a constant |
| $\mu_r$ | slightly below 1 | slightly above 1 | $\gg1$ |
| mechanism | orbital moments *induced* (Lenz) | *permanent* moments partly aligned | permanent moments aligned *spontaneously*, in domains |
| $\mathbf{M}$ at $\mathbf{H} = 0$? | no | no | yes — permanent magnets |
| examples (slides) | copper, bismuth, water, silver | aluminum, platinum, liquid oxygen, palladium | iron, nickel, cobalt, alloys |

**Diamagnetism** is in every atom: a switched-on field induces an emf around each orbit ([[2-magnetostatics/14-faradays-law-and-induced-emf|Lecture 14]]), and by Lenz the induced moment opposes it (the notes' "electron clouds spin up" is this orbital change, not spin). Water, wood, glass, copper, silver, bismuth show only this: weakly pushed out of strong fields.

**Paramagnetism**: unpaired spins in unfilled inner shells (Pauli pairs those in filled ones) align against thermal agitation — lopsidedly: at 1 T, $\mu_BB\approx9\times10^{-24}$ J is about $1/450$ of room-temperature $k_BT\approx4\times10^{-21}$ J, so only a small excess aligns. Weak attraction to magnets. Mnemonic: **Para**magnetic ↔ **Pos**itive.

**Ferromagnetism** is quantum: conduction electrons, constrained by exclusion, pass a spin orientation from atom to atom ("exchange"), so spins align spontaneously into saturated domains pointing different ways ($\mathbf{M}\approx0$ unmagnetized). Applied $\mathbf{H}$ grows aligned domains: modest $\mathbf{H}$, enormous $\mathbf{M}$, and $\mathbf{B} = \mu_0\mathbf{H}+\mu_0\mathbf{M}(\mathbf{H})$ depends on history.

<!-- fig:mag-hysteresis -->

That memory is **hysteresis**: back at $H = 0$ after the virgin curve to saturation, $B$ keeps the **remanence** $B_r$; the **coercivity** $-H_c$ zeroes it. $\mathbf{B}\neq0$ at $\mathbf{H} = 0$ is a **permanent magnet** (notes, p. 12). Loop area = heat per m³ per cycle: *soft* (small $H_c$: transformer steel, ferrites) for AC, *hard* (large $B_r$, $H_c$) for magnets.

> [!example] The slides' values ($\chi_m$ from slides 12–13 for copper, water, aluminum, platinum, liquid oxygen; $\mu_r$ from the slide-15 table otherwise; other column from $\mu_r = 1+\chi_m$)
> | material | class | $\chi_m$ | $\mu_r$ |
> |---|---|---|---|
> | bismuth | dia | $-1.7\times10^{-4}$ | 0.99983 |
> | silver | dia | $-7\times10^{-5}$ | 0.99993 |
> | copper | dia | $-0.94\times10^{-5}$ | 0.999991 |
> | water | dia | $-0.88\times10^{-5}$ | 0.999991 |
> | vacuum | — | 0 | 1 (by definition) |
> | aluminum | para | $+2.1\times10^{-5}$ | 1.00002 |
> | platinum | para | $+2.9\times10^{-5}$ | 1.000029 |
> | liquid oxygen | para | $+3.5\times10^{-5}$ | 1.000035 |
> | palladium | para | $+8\times10^{-4}$ | 1.0008 |
> | cobalt / nickel | ferro | $\approx\mu_r$ | 250 / 600 |
> | mild steel / iron (0.2% impurity) | ferro | $\approx\mu_r$ | 2000 / 5000 |
> | silicon iron / mumetal | ferro | $\approx\mu_r$ | 7000 / 100,000 |
> | purified iron / superalloy | ferro | $\approx\mu_r$ | 200,000 / 1,000,000 |
>
> Ink: $\chi_m<0$, "$\chi_m>0$ small", $\chi_m\gg1$ (slide 14: $\mu_r-1 = \chi_m\gg1$). The table's dia- and paramagnets are within one part in a thousand of $\mu_r = 1$: hence $\mu = \mu_0$ for most media later. *Handbook check (site):* silver $\approx-2.4\times10^{-5}$ ($\mu_r\approx0.99998$), platinum $+2.7\times10^{-4}$, liquid oxygen (90 K) $+3.5\times10^{-3}$; lead omitted (slide 12: $-1.70\times10^{-5}$; slide 15: $\mu_r = 0.99993$). No class changes, but a strong paramagnet like liquid oxygen reaches a few parts in a thousand.

> [!trap] Classification slips
> - Domains: ferromagnets only; paramagnet atoms align individually, slightly.
> - Every atom is diamagnetic; para/ferro means permanent moments win (notes, footnote 4).
> - A ferromagnet's "$\mu_r = 5000$" is a small-field slope; near saturation $B$ grows only as $\mu_0H$.
> - $\chi_e>0$ always (Unit 1); $\chi_m$ can be negative.

Notes: a first-principles $\chi_m$ needs quantum mechanics; like $\chi_e$ ([[1-electrostatics/11-lorentz-drude-models-for-conductivity-and-susceptibility|Lecture 11]]) it depends on frequency, with loss and resonances that matter for magnetic imaging.

## 6. Boundary conditions in magnetic media

[[3-maxwell-and-waves/16-charge-conservation-displacement-current-and-maxwells-equations#4-boundary-conditions--same-for-dynamics|Lecture 16's]] conditions are already macroscopic (free $\rho_s$, $\mathbf{J}_s$). With $\mathbf{B} = \mu\mathbf{H}$:

> [!key] Magnetic boundary conditions ($\hat n$ from medium 2 into medium 1)
> $$
> \hat n\cdot(\mathbf{B}_1-\mathbf{B}_2) = 0\ \Longrightarrow\ \mu_1H_{1n} = \mu_2H_{2n},\qquad\qquad \hat n\times(\mathbf{H}_1-\mathbf{H}_2) = \mathbf{J}_s\ \ (\text{free}).
> $$
> Without free surface current $\mathbf{H}_t$ (so $\mathbf{B}_t/\mu$) is continuous and $B$- and $H$-lines **refract** alike:
> $$
> \frac{\tan\theta_1}{\tan\theta_2} = \frac{\mu_1}{\mu_2}\qquad(\text{angles from the normal}).
> $$
> Tangential $\mathbf{B}$ jumps by the bound current, $\hat n\times(\mathbf{B}_1-\mathbf{B}_2)/\mu_0 = \mathbf{J}_s + \hat n\times(\mathbf{M}_1-\mathbf{M}_2)$; normal $\mathbf{H}$ jumps too, $H_{1n}-H_{2n} = -(M_{1n}-M_{2n})$ — "$\nabla\cdot\mathbf{H} = 0$" fails here, $\nabla\cdot\mathbf{B} = 0$ never.

<!-- fig:mag-refraction -->

This is [[1-electrostatics/09-static-fields-in-dielectric-media#2-refraction-of-field-lines-at-an-interface|Lecture 9's refraction law]] with $\epsilon\to\mu$ (ink: $\mu_1H_{n1} = \mu_2H_{n2}$, $B_{n1} = B_{n2}$); numbers in [[problems/fields-across-a-magnetic-interface]]. Iron, $\mu_r = 5000$: 85° inside leaves at 0.13°, 89.9° at 6.5° — almost normal, like $\mathbf{E}$ at a conductor; hence iron pole pieces in motors and loudspeakers.

> [!recipe] Problems with magnetic media
> 1. **$\mathbf{H}$ from free currents alone**: Ampère, sheets $\tfrac12\mathbf{J}_s\times\hat n$, superposition, boundary conditions.
> 2. **$\mathbf{B} = \mu\mathbf{H}$** region by region; then flux, inductance or force.
> 3. **$\mathbf{M} = \mathbf{B}/\mu_0-\mathbf{H} = \chi_m\mathbf{H}$ last.** Check: $\nabla\times\mathbf{M}$, $\mathbf{M}\times\hat n$ plus free currents in *vacuum* formulas return $\mathbf{B}$.
>
> Lecture 9's chain (free charge → $\mathbf{D}$ → $\mathbf{E} = \mathbf{D}/\epsilon$ → $V$ → $\mathbf{P}$), translated.

<!-- fig:mag-slab-between-sheets -->

> [!example] Example (slides, solved in class) — a magnetic slab between two current sheets
> Slab $\mu_r = 100$ between sheets $-0.1\hat y$ A/m on top and $+0.1\hat y$ A/m below ($x$ right, $z$ up, $y$ into the page). Find $\mathbf{H}$, $\mathbf{B}$, $\mathbf{M}$; compare $\mu_r = 1$.
> - $\mathbf{H}$, each sheet $\tfrac12\mathbf{J}_s\times\hat n$ ($\hat n$ toward the point): top $\tfrac12(-0.1\hat y)\times(-\hat z) = +0.05\hat x$, bottom $\tfrac12(0.1\hat y)\times\hat z = +0.05\hat x$; $\mathbf{H} = 0.1\hat x$ A/m $= J_s\hat x$ between, $0$ outside.
> - No free current on the slab ("no $J_s$ on slab"), so $H_t$ continuous: $\mathbf{H}_{\text{slab}} = 0.1\hat x$ A/m.
> - $\mathbf{B}_{\text{slab}} = \mu_0\mu_r\mathbf{H} = 100\mu_0(0.1)\hat x = 1.26\times10^{-5}\hat x$ T (12.6 μT); $\mathbf{M} = \chi_m\mathbf{H} = 99\times0.1\hat x = 9.9\hat x$ A/m; $\mu_0(\mathbf{H}+\mathbf{M}) = \mu_0(10)\hat x$ ✓.
> - $\mu_r = 1$: same $\mathbf{H}$, $\mathbf{B} = \mu_0(0.1)\hat x = 1.26\times10^{-7}\hat x$ T (100 times smaller), $\mathbf{M} = 0$.
>
> *Bound-current check (site):* $\nabla\times\mathbf{M} = 0$; top $\mathbf{M}\times\hat z = 9.9\hat x\times\hat z = -9.9\hat y$ A/m, bottom $+9.9\hat y$ A/m, each along its free sheet. Free plus bound, $10$ A/m per face, in the *vacuum* formula: $\mathbf{B} = \mu_0(10\text{ A/m})\hat x = 100\mu_0\mathbf{H}$ in the slab, $\mu_0(0.1)\hat x$ in any air gap, zero outside.

## 7. The dictionary: polarization ↔ magnetization

The slides' first annotation is "M → P"; the deck pairs the two throughout. Extending the [[2-magnetostatics/index#the-dictionary-electrostatics--magnetostatics|Unit 2 dictionary]]:

| | polarization (Lectures 8–9) | magnetization (Lecture 17) |
|---|---|---|
| dipole; torque | $\mathbf{p} = q\mathbf{d}$, $-$ to $+$; $\mathbf{p}\times\mathbf{E}$ | $\mathbf{m} = I\mathbf{A}$; $\mathbf{m}\times\mathbf{B}$ |
| bound volume; surface | $-\nabla\cdot\mathbf{P}$; $\mathbf{P}\cdot\hat n$ | $\nabla\times\mathbf{M}$; $\mathbf{M}\times\hat n$ |
| interface ($\hat n$ 2→1) | $-\hat n\cdot(\mathbf{P}_1-\mathbf{P}_2)$ | $\hat n\times(\mathbf{M}_1-\mathbf{M}_2)$ |
| averaged bound field (notes' model) | $-\mathbf{P}/\epsilon_0$, opposes $\mathbf{p}$ | $+\mu_0\mathbf{M}$, along $\mathbf{m}$ |
| auxiliary field, law | $\mathbf{D} = \epsilon_0\mathbf{E}+\mathbf{P}$; $\oint\mathbf{D}\cdot d\mathbf{S} = Q_f$ | $\mathbf{H} = \mathbf{B}/\mu_0-\mathbf{M}$; $\oint\mathbf{H}\cdot d\mathbf{l} = I_f + d\psi_E/dt$ |
| linear medium | $\mathbf{P} = \epsilon_0\chi_e\mathbf{E}$, $\epsilon = \epsilon_0(1+\chi_e)$ | $\mathbf{M} = \chi_m\mathbf{H}$, $\mu = \mu_0(1+\chi_m)$ |
| free sources set (with symmetry) → medium sets | $\mathbf{D}$ → $\mathbf{E} = \mathbf{D}/\epsilon$ | $\mathbf{H}$ → $\mathbf{B} = \mu\mathbf{H}$ |
| continuous (no free surface sources) | $D_n$; $E_t$ always | $B_n$ always; $H_t$ |
| interface law | $\tan\theta_1/\tan\theta_2 = \epsilon_1/\epsilon_2$ | $\tan\theta_1/\tan\theta_2 = \mu_1/\mu_2$ |
| huge susceptibility | $\mathbf{E}\to0$ inside, like a conductor | $B$-lines leave normally (iron pole faces) |
| susceptibility | $\chi_e>0$; Lorentz ([[1-electrostatics/11-lorentz-drude-models-for-conductivity-and-susceptibility\|Lecture 11]]) | any sign; quantum |
| circuit | $C\propto\epsilon$ | $L\propto\mu$ |

> [!intuition] The four places where the analogy is *not* a straight translation
> 1. **$\epsilon_0$ in $\mathbf{P} = \epsilon_0\chi_e\mathbf{E}$, none in $\mathbf{M} = \chi_m\mathbf{H}$**: units.
> 2. **$-\nabla\cdot\mathbf{P}$ but $+\nabla\times\mathbf{M}$**: converging $\mathbf{P}$ crowds $+$ ends together; loop currents just add.
> 3. **$\mathbf{D}$ adds $\mathbf{P}$, $\mathbf{H}$ subtracts $\mathbf{M}$**: $\mathbf{B}$ (felt by charges) is the twin of $\mathbf{E}$; a dielectric weakens $\mathbf{E}$, a para- or ferromagnet strengthens $\mathbf{B}$.
> 4. **$\chi_m$ can be negative, $\chi_e$ cannot**: electric dipoles are induced along the field, orbital moments against it (Lenz); only permanent moments make $\chi_m>0$.

## 8. Summary

- $\mathbf{J}_M = \nabla\times\mathbf{M}$, surface $\mathbf{M}\times\hat n$; $\mathbf{H}\equiv\mathbf{B}/\mu_0-\mathbf{M}$, set by free currents; $\mathbf{B} = \mu\mathbf{H}$, $\mathbf{M} = \chi_m\mathbf{H}$ (no $\mu_0$).
- Dia $\chi_m<0$, para small $>0$, ferro $\gg1$. $B_n$ continuous; $H_t$ too unless free $J_s$.

Concept pages: [[concepts/magnetization]] · [[concepts/permeability]] · [[concepts/maxwells-equations]] · [[concepts/boundary-conditions]] · [[concepts/magnetic-field]] · [[concepts/inductance]] · [[concepts/polarization]]. Worked problem: [[problems/fields-across-a-magnetic-interface]].

> [!exam] On exams
> None named; the site's guess: (1) the slab-and-sheets problem, with the $\mu_r = 1$ comparison; (2) "no $\mu_0$" in $\mathbf{M} = \chi_m\mathbf{H}$; (3) classify from $\chi_m$ or $\mu_r$, or say which class has domains, hysteresis, $\chi_m<0$; (4) $\mathbf{H} = \mathbf{B}/\mu_0-\mathbf{M}$, $\mathbf{J}_M = \nabla\times\mathbf{M}$; (5) interface problems like FA26 Exam 1 #3 with $\epsilon\to\mu$, $\mathbf{E}\to\mathbf{H}$.

> [!tip] Practice this lecture
> [[practice/17-magnetization-and-maxwell-in-matter|12 practice problems]] — 5 easy, 3 medium, 4 hard — each with a folded hint and a worked solution. Start with [[practice/17-magnetization-and-maxwell-in-matter#171-moment-and-torque-on-a-loop|17.1 Moment and torque on a loop]]; the [[practice/index|practice hub]] has the whole bank by difficulty and by topic.

### Sources for this page
Kudeki notes, Lecture 17, with footnotes 3, 4, 6. Shao, Lecture 17 slides: moments, torque, "no μ₀", $\mu_r$ table, slab example, concept map. This site's own: $\mathbf{M}\times\hat n$, loop lattice, square-loop torque, "this site's numbers", demagnetization, iron refraction, bound-current check, dictionary; verified in `verify_L17.py`. Slips in the course material: see [[0-toolkit/04-errata-in-the-course-materials|errata]].
