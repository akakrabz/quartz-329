---
title: "Maxwell's equations"
description: "The four equations in integral and differential form, what each says physically, the static special case, the microscopic and macroscopic forms, and where in the course each one is derived and used."
tags: [concept, electrostatics, magnetostatics, waves]
aliases: ["Maxwell equations", "field equations", "Maxwell's equations complete", "no magnetic monopoles", "canonical fields", "quasi-static approximation", "electrically small", "differential form of Maxwell's equations"]
---

> [!key] Maxwell's equations (differential form, as the notes list them)
> $$
> \begin{gathered}
> \nabla\cdot\mathbf{D} = \rho\ \ (\text{Gauss}),\qquad \nabla\cdot\mathbf{B} = 0,\\[4pt]
> \nabla\times\mathbf{E} = -\frac{\partial\mathbf{B}}{\partial t}\ \ (\text{Faraday}),\qquad \nabla\times\mathbf{H} = \mathbf{J}+\frac{\partial\mathbf{D}}{\partial t}\ \ (\text{Ampère–Maxwell}),
> \end{gathered}
> $$
> with $\mathbf{D} = \epsilon_0\mathbf{E}$, $\mathbf{B} = \mu_0\mathbf{H}$ if $\rho$ and $\mathbf{J}$ include *all* charges and currents, bound and free (microscopic form, valid down to about the Compton wavelength); or $\mathbf{D} = \epsilon\mathbf{E}$, $\mathbf{B} = \mu\mathbf{H}$ with only the *free* $\rho$, $\mathbf{J}$ (macroscopic form, [[concepts/permeability|Permeability, susceptibility, and B = μH]]). Integral forms in the table below; the [[concepts/lorentz-force|Lorentz force]] $\mathbf{F} = q(\mathbf{E}+\mathbf{v}\times\mathbf{B})$ says what the fields do.

| law | integral form | theorem | differential form | says |
|---|---|---|---|---|
| Gauss | $\oint_S\mathbf{D}\cdot d\mathbf{S} = \int_V\rho\,dV$ | divergence | $\nabla\cdot\mathbf{D} = \rho$ | E-lines start/end on charge |
| Gauss (magnetic) | $\oint_S\mathbf{B}\cdot d\mathbf{S} = 0$ | divergence | $\nabla\cdot\mathbf{B} = 0$ | B-lines never start or end |
| Faraday | $\oint_C\mathbf{E}\cdot d\mathbf{l} = -\dfrac{\partial}{\partial t}\int_S\mathbf{B}\cdot d\mathbf{S}$ | Stokes | $\nabla\times\mathbf{E} = -\dfrac{\partial\mathbf{B}}{\partial t}$ | changing B makes E circulate |
| Ampère–Maxwell | $\oint_C\mathbf{H}\cdot d\mathbf{l} = \int_S\Big(\mathbf{J}+\dfrac{\partial\mathbf{D}}{\partial t}\Big)\cdot d\mathbf{S}$ | Stokes | $\nabla\times\mathbf{H} = \mathbf{J}+\dfrac{\partial\mathbf{D}}{\partial t}$ | current and changing D make H circulate |

Lecture 1 writes the free-space set in $\mathbf{E}$ and $\mathbf{B}$: $\nabla\cdot\mathbf{E} = \rho/\epsilon_0$, $\nabla\cdot\mathbf{B} = 0$, $\nabla\times\mathbf{E} = -\dfrac{\partial\mathbf{B}}{\partial t}$, $\nabla\times\mathbf{B} = \mu_0\mathbf{J} + \mu_0\epsilon_0\dfrac{\partial\mathbf{E}}{\partial t}$, with

$$
\mu_0 \approx 4\pi\times 10^{-7}\ \tfrac{\text{H}}{\text{m}}\ (\text{exact before the 2019 SI redefinition}),\qquad
\epsilon_0 = \frac{1}{\mu_0 c^2}\approx \frac{1}{36\pi\times 10^{9}}\ \tfrac{\text{F}}{\text{m}}\approx 8.854\times10^{-12}\ \tfrac{\text{F}}{\text{m}},\qquad
c = \frac{1}{\sqrt{\mu_0\epsilon_0}}\approx 3\times10^{8}\ \tfrac{\text{m}}{\text{s}}.
$$

**How to read them.** Divergence laws: what the fields emanate from (sources). Curl laws: what makes them circulate. Sources on the right-hand sides, fields on the left. Each integral law becomes local by the matching theorem ([[concepts/divergence-theorem|Divergence theorem]], [[concepts/stokes-theorem|Stokes' theorem]]) plus "true for every surface/volume ⟹ true at every point" ([[1-electrostatics/04-divergence-and-curl#7-the-differential-form-of-maxwells-equations|Lecture 4 §7]]). $\oint_C\mathbf{E}\cdot d\mathbf{l}$ is an **EMF** (volts), $\oint_C\mathbf{H}\cdot d\mathbf{l}$ an **MMF** (amperes). Ampère's right side: the static **conduction current** $\mathbf{J}$ plus the dynamic **displacement current** $\partial\mathbf{D}/\partial t$ — Maxwell's addition, and the reason light exists. The course counts the four off as each is derived ("our first Maxwell equation!" in [[1-electrostatics/02-coulombs-law-superposition-and-gauss|Lecture 2]]).

**The destination.** Announced in [[1-electrostatics/01-fields-forces-and-the-maxwell-roadmap|Lecture 1]]: Lectures 2–13 built the static pieces, [[2-magnetostatics/14-faradays-law-and-induced-emf|Lecture 14]] replaced $\nabla\times\mathbf{E} = 0$ by Faraday, [[3-maxwell-and-waves/16-charge-conservation-displacement-current-and-maxwells-equations|Lecture 16]] replaces $\nabla\times\mathbf{H} = \mathbf{J}$ by Ampère–Maxwell and writes the four together for the first time. The rest of the course — waves, Poynting, phasors, reflection, transmission lines — is these four equations plus constitutive relations and boundary conditions, no new physics.

**Built in: charge conservation.** $\nabla\cdot(\nabla\times\mathbf{H}) = 0$ gives $\nabla\cdot\mathbf{J} = -\partial\rho/\partial t$ — the [[concepts/continuity-equation|Continuity equation (charge conservation)]]; run backwards, this is why the [[concepts/displacement-current|Displacement current]] has to be there.

> [!derivation]- Charge conservation falls out of Ampère–Maxwell (Lecture 4 §7)
> Take the divergence of the Ampère–Maxwell equation. Since $\nabla\cdot(\nabla\times\mathbf{H}) = 0$ identically,
> $$
> 0 = \nabla\cdot\mathbf{J} + \frac{\partial}{\partial t}\nabla\cdot\mathbf{D} = \nabla\cdot\mathbf{J} + \frac{\partial\rho}{\partial t}
> \quad\Longrightarrow\quad
> \boxed{\ \nabla\cdot\mathbf{J} = -\frac{\partial\rho}{\partial t}\ }
> $$
> the **continuity equation**: current flowing out of a point drains its charge — conservation is built into Maxwell's equations. The identity $\nabla\cdot(\nabla\times\mathbf{A}) = 0$ and its companions are on [[concepts/curl|Curl]].

**The unnamed equation.** $\nabla\cdot\mathbf{B} = 0$ is not independent like the others. The divergence of Faraday's law gives $0 = \nabla\cdot(\nabla\times\mathbf{E}) = -\dfrac{\partial}{\partial t}\nabla\cdot\mathbf{B}$: $\nabla\cdot\mathbf{B}$ is **constant in time** at every point. Zero for the static fields of Lectures 12–13, it stays zero when fields vary. Physically: no magnetic charge. Monopoles would make $\nabla\cdot\mathbf{B}$ their density, with $\mathbf{B}$-lines starting and ending on them; none has been observed at any scale or any epoch accessible to astronomy.

**The static split (Lecture 1 §2; Lectures 1–13).** With $\partial/\partial t = 0$ both time-derivative terms vanish and the system decouples:
- *Electrostatics* (Lectures 1–11): $\nabla\cdot\mathbf{D} = \rho$, $\nabla\times\mathbf{E} = 0$ — a **curl-free** field fixed by charge, so $\mathbf{E} = -\nabla V$ and $\nabla^2V = -\rho/\epsilon_0$.
- *Magnetostatics* (Lectures 12–13): $\nabla\cdot\mathbf{B} = 0$, $\nabla\times\mathbf{H} = \mathbf{J}$ — a **divergence-free** field fixed by current, so $\mathbf{B} = \nabla\times\mathbf{A}$.

By the [[concepts/helmholtz-theorem|Helmholtz theorem]], divergence + curl (with decay at infinity) determine a field uniquely, so each pair is a complete description. Lectures 14–15 bring $\partial\mathbf{B}/\partial t$ back.

> [!note] The canonical static fields in one table (the Lecture 16 slide's review)
> | source | field | from |
> |---|---|---|
> | point charge $Q$ | $\mathbf{E} = \dfrac{Q}{4\pi\epsilon_0R^2}\hat R$ | Coulomb / Gauss on a sphere |
> | line charge $\rho_l$ | $\mathbf{E} = \dfrac{\rho_l}{2\pi\epsilon_0r}\hat r$ | Gauss on a cylinder |
> | sheet charge $\rho_s$ | $\mathbf{E} = \dfrac{\rho_s}{2\epsilon_0}(\pm\hat n)$ | Gauss on a pillbox |
> | line current $I$ | $\mathbf{B} = \dfrac{\mu_0I}{2\pi r}\hat\phi$ | Ampère on a circle |
> | sheet current $\mathbf{J}_s$ | $\mathbf{B} = \dfrac{\mu_0}{2}\mathbf{J}_s\times\hat n$ | Ampère on a rectangle |
> | solenoid $nI$ | $\mathbf{B} = \mu_0nI\hat z$ inside | Ampère on a rectangle |
>
> Units 1–2 in one rule: pick the symmetric surface or loop, count the enclosed source.

**The dynamic coupling (Lectures 14–38).** [[2-magnetostatics/14-faradays-law-and-induced-emf|Lecture 14]] (Faraday's law) puts $\partial\mathbf{B}/\partial t$ back into the curl-$\mathbf{E}$ equation — the first coupling, and the end of "voltage is path-independent"; Lecture 16 adds the displacement current, and from then on Faraday and Ampère–Maxwell feed each other: a changing $\mathbf{B}$ makes $\mathbf{E}$, a changing $\mathbf{E}$ makes $\mathbf{B}$. The result is the [[concepts/wave-equation|wave equation]] with speed $c = 1/\sqrt{\mu_0\epsilon_0}$ — light, radio, and signals on transmission lines (Hertz, 1888). Lecture 1 §2 states it on day one: empty space supports $\mathbf{E},\mathbf{B}\propto\cos\!\big(2\pi f\,(t - z/c)+\phi\big)$, disturbances travelling at $c$ with wavelength $\lambda = c/f$ ([[concepts/plane-waves|Plane waves]]) — the reason the course ends with transmission lines and the Smith chart.

**Quasi-statics: when is a circuit "a circuit"?** A source of period $T$ can be treated *statically* — using the instantaneous $\rho$ and $\mathbf{J}$ — when the field crosses the system before the source changes:

$$
T \gg \frac{L}{c}\quad\Longleftrightarrow\quad L \ll \lambda .
$$

This **quasi-static approximation** is the assumption behind lumped-circuit theory (ECE 210): a circuit is a circuit only while *electrically small*. Shrink $\lambda$ (raise the clock) or grow $L$ (a long cable, a PCB trace at GHz) and delays $L/c$ matter — Lectures 27–38. (Lecture 6 §1 states the same condition as $\tau\gg L/c$: the fields at each instant are the static fields of the instantaneous sources, plus a small slowly varying $\mathbf{B}$; excellent for lab circuits below a few MHz.)

> [!tip] A number to carry around
> $c \approx 3\times10^{8}$ m/s $= 300$ m/µs $= 30$ cm/ns. So 1 MHz ↔ 300 m wavelength; 1 GHz ↔ 30 cm; a 3 GHz clock has $\lambda = 10$ cm, which is *not* large compared with a motherboard.

**In matter.** Read with $\rho$ and $\mathbf{J}$ counting *every* charge, bound ones included, the equations are the **microscopic** form. In a material the bound sources are averaged, $\rho = \rho_f-\nabla\cdot\mathbf{P}$ and $\mathbf{J} = \mathbf{J}_f+\partial\mathbf{P}/\partial t+\nabla\times\mathbf{M}$, and absorbed into $\mathbf{D} = \epsilon_0\mathbf{E}+\mathbf{P}$ and $\mathbf{H} = \mathbf{B}/\mu_0-\mathbf{M}$. The result is the **macroscopic** form: the same four equations, with $\rho$ and $\mathbf{J}$ now the *free* charge and current only, and $\mathbf{D} = \epsilon\mathbf{E}$, $\mathbf{B} = \mu\mathbf{H}$ in linear media. Faraday's law and $\nabla\cdot\mathbf{B} = 0$ are unchanged — they have no sources — so only Gauss and Ampère–Maxwell need the auxiliary fields ([[concepts/polarization|Polarization P and bound charge]] for $\mathbf{P}$, [[concepts/magnetization|Magnetization M and magnetization current]] for $\mathbf{M}$; the derivation is on [[concepts/permeability|Permeability, susceptibility, and B = μH]]).

> [!trap]
> - $\nabla\cdot\mathbf{B} = 0$ is not a fifth independent law: Faraday's law keeps $\nabla\cdot\mathbf{B}$ constant, and "no monopoles" sets the constant to zero.
> - At a boundary, use the integral forms: the fields jump there and their derivatives are δ-functions ([[concepts/boundary-conditions|Boundary conditions at an interface]]).
> - Macroscopic $\rho$, $\mathbf{J}$ are *free* sources only; the bound ones live in $\mathbf{D}$ and $\mathbf{H}$.
> - Partial, not total, time derivatives: fields depend on $(x,y,z,t)$; read a slide's $d/dt$ as $\partial/\partial t$.

> [!exam] On exams
> Write all four, with the time-derivative terms and the right auxiliary fields; name what each says and which term is Maxwell's. "Which Maxwell equation says …" and the differential ↔ integral conversion of Gauss's law recur on Exam 1 (never the dynamic equations); keep $\partial/\partial t$ partial and the continuity sign ($\nabla\cdot\mathbf{J}$ *negative* where charge piles up). Know the static special cases, where $\nabla\cdot\mathbf{B} = 0$ comes from, and the canonical-field table.

**Where it appears.** [[1-electrostatics/01-fields-forces-and-the-maxwell-roadmap#2-the-roadmap-maxwells-equations-on-day-one|Lecture 1 §2]] (roadmap); Gauss: [[1-electrostatics/02-coulombs-law-superposition-and-gauss|Lecture 2]] (from Coulomb) and [[1-electrostatics/04-divergence-and-curl#7-the-differential-form-of-maxwells-equations|Lecture 4 §7]] (all four in differential form; continuity as a consequence); magnetic Gauss: [[1-electrostatics/03-gauss-law-at-work#6-the-magnetic-counterpart--bds--0|Lecture 3 §6]]; Faraday: [[2-magnetostatics/14-faradays-law-and-induced-emf|Lecture 14]]; Ampère: [[2-magnetostatics/12-magnetic-force-biot-savart-and-amperes-law|Lecture 12]], [[2-magnetostatics/13-current-sheets-solenoids-and-the-vector-potential|Lecture 13]]; completed in [[3-maxwell-and-waves/16-charge-conservation-displacement-current-and-maxwells-equations#3-maxwells-equations-complete|Lecture 16 §3]]; in matter, [[3-maxwell-and-waves/17-magnetization-and-maxwells-equations-in-matter#4-h-redefined-maxwells-equations-in-matter|Lecture 17 §4]]; source-free form, [[3-maxwell-and-waves/18-the-wave-equation-and-plane-tem-waves#1-fields-without-sources|Lecture 18 §1]].

**Related.** [[concepts/continuity-equation|Continuity equation (charge conservation)]] · [[concepts/displacement-current|Displacement current]] · [[concepts/boundary-conditions|Boundary conditions at an interface]] · [[concepts/wave-equation|Wave equation]] · [[concepts/permeability|Permeability, susceptibility, and B = μH]] · [[concepts/lorentz-force|Lorentz force]].

**Practice.** [[practice/topics#divergence-curl-and-the-integral-theorems|Divergence, curl and the integral theorems]] (21 problems) — for example [[practice/04-divergence-and-curl#41-faucet-or-whirlpool|4.1 Faucet or whirlpool]] (easy), [[practice/04-divergence-and-curl#46-three-fields-in-curved-coordinates|4.6 Three fields in curved coordinates]] (medium), [[practice/04-divergence-and-curl#49-electrostatic-or-not|4.9 Electrostatic or not]] (hard).
