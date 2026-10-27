---
title: "Lecture 20 — Poynting's theorem and monochromatic waves"
description: "Poynting's theorem: the stored energy ½εE² + ½μH² changes only by flowing away as S = E × H or by going to charges at the rate J·E. A sheet current J₀cos ωt injects ηJ₀²/4 per square metre on average, half carried away by each wave."
tags: [lecture, waves]
lecture: 20
---

*Lecture 20 · course notes §20 · **slides: not yet available — this page is built from the course notes** · prev: [[3-maxwell-and-waves/19-dalembert-solutions-and-radiation-from-current-sheets|Lecture 19]] · next: [[3-maxwell-and-waves/21-monochromatic-waves-and-phasor-notation|Lecture 21]] · worked problem: [[problems/energy-bookkeeping-for-a-radiating-sheet|Energy bookkeeping for a radiating sheet]] · practice: [[practice/20-poynting-theorem-and-power|12 problems]]*

> [!abstract] In one breath
> Dot Faraday's law with $\mathbf{H}$ and Ampère–Maxwell with $\mathbf{E}$, subtract: **Poynting's theorem**, $\partial w/\partial t + \nabla\cdot\mathbf{S} + \mathbf{J}\cdot\mathbf{E} = 0$, with $w = \tfrac12\epsilon E^2 + \tfrac12\mu H^2$ and $\mathbf{S} = \mathbf{E}\times\mathbf{H}$ [W/m²]. It is [[3-maxwell-and-waves/16-charge-conservation-displacement-current-and-maxwells-equations|Lecture 16]]'s continuity equation for energy, plus an exchange term $\mathbf{J}\cdot\mathbf{E}$ (Joule heating if positive, a source if negative). A sheet $\hat x\,2\cos\omega t$ A/m radiates **monochromatic** waves, $\langle S\rangle = \eta_0/2\approx188$ W/m² per side, and injects $\eta_0\approx377$ W/m², the sum.

## 1. Where does the energy go?

- A capacitor's $\tfrac12CV^2$ sits in the field at $\tfrac12\epsilon E^2$ per m³ ([[1-electrostatics/10-capacitance-and-conductance#5-energy-stored-in-a-capacitor-and-in-the-field|Lecture 10]]), an inductor's $\tfrac12LI^2$ at $\tfrac12\mu H^2$ ([[2-magnetostatics/15-inductance-magnetic-energy-and-the-potentials|Lecture 15]]).
- Resistors, and a leaky capacitor ([[1-electrostatics/10-capacitance-and-conductance#6-conductance-the-leaky-capacitor|Lecture 10 §6]]), turn it into heat.
- On [[3-maxwell-and-waves/19-dalembert-solutions-and-radiation-from-current-sheets#5-reading-the-result|Lecture 19]]'s sheet, $\mathbf{E}$ opposes $\mathbf{J}_s$ and two waves carry $\mathbf{E}\times\mathbf{H}$ away.

Charge obeys a continuity equation ([[3-maxwell-and-waves/16-charge-conservation-displacement-current-and-maxwells-equations#1-charge-conservation-and-the-continuity-equation|Lecture 16]]); field energy also needs an exchange term (heat in a resistor, chemistry in a battery). Maxwell's equations supply it.

## 2. Deriving the theorem from Maxwell's equations

From the curl equations of [[3-maxwell-and-waves/16-charge-conservation-displacement-current-and-maxwells-equations#3-maxwells-equations-complete|Lecture 16]]:

**Step 1:** dot Faraday's law with $\mathbf{H}$ and Ampère–Maxwell with $\mathbf{E}$ (every term W/m³):

$$
\begin{gathered}
\mathbf{H}\cdot(\nabla\times\mathbf{E}) = -\mathbf{H}\cdot\frac{\partial\mathbf{B}}{\partial t},\\[4pt]
\mathbf{E}\cdot(\nabla\times\mathbf{H}) = \mathbf{E}\cdot\mathbf{J} + \mathbf{E}\cdot\frac{\partial\mathbf{D}}{\partial t}.
\end{gathered}
$$

**Step 2:** subtract the second from the first:

$$
\begin{aligned}
&\underbrace{\mathbf{H}\cdot(\nabla\times\mathbf{E}) - \mathbf{E}\cdot(\nabla\times\mathbf{H})}_{\nabla\cdot(\mathbf{E}\times\mathbf{H})}\\
&\qquad = -\mathbf{E}\cdot\frac{\partial\mathbf{D}}{\partial t} - \mathbf{H}\cdot\frac{\partial\mathbf{B}}{\partial t} - \mathbf{J}\cdot\mathbf{E}.
\end{aligned}
$$

- **Left side:** a divergence, by $\nabla\cdot(\mathbf{A}\times\mathbf{B}) = \mathbf{B}\cdot(\nabla\times\mathbf{A}) - \mathbf{A}\cdot(\nabla\times\mathbf{B})$ ([[0-toolkit/02-vector-calculus-cheatsheet#identities-valid-for-any-smooth-fields|toolkit]]; folded below).
- **First two terms on the right:** a time derivative if $\mathbf{D} = \epsilon\mathbf{E}$, $\mathbf{B} = \mu\mathbf{H}$ with $\epsilon$, $\mu$ constant in time, since $\partial(\mathbf{E}\cdot\mathbf{E})/\partial t = 2\,\mathbf{E}\cdot\partial\mathbf{E}/\partial t$:

$$
\begin{gathered}
\mathbf{E}\cdot\frac{\partial\mathbf{D}}{\partial t} = \frac{\partial}{\partial t}\Big(\tfrac12\epsilon\,\mathbf{E}\cdot\mathbf{E}\Big),\\[4pt]
\mathbf{H}\cdot\frac{\partial\mathbf{B}}{\partial t} = \frac{\partial}{\partial t}\Big(\tfrac12\mu\,\mathbf{H}\cdot\mathbf{H}\Big).
\end{gathered}
$$

> [!key] Poynting's theorem (point form)
> $$
> \begin{gathered}
> \frac{\partial}{\partial t}\Big(\tfrac12\epsilon\,\mathbf{E}\cdot\mathbf{E} + \tfrac12\mu\,\mathbf{H}\cdot\mathbf{H}\Big)\\
> {} + \nabla\cdot(\mathbf{E}\times\mathbf{H}) + \mathbf{J}\cdot\mathbf{E} = 0 ,
> \end{gathered}
> $$
> or, with $w\equiv\tfrac12\epsilon E^2 + \tfrac12\mu H^2$ [J/m³] and $\mathbf{S}\equiv\mathbf{E}\times\mathbf{H}$ [W/m²],
> $$
> \frac{\partial w}{\partial t} + \nabla\cdot\mathbf{S} + \mathbf{J}\cdot\mathbf{E} = 0\qquad[\text{W/m}^3].
> $$
> Valid at every point and instant in a linear, isotropic medium with $\epsilon$, $\mu$ constant in time (they may vary in space; unstated in the notes). $\mathbf{J}$ is the free current; bound sources sit inside $\epsilon$, $\mu$.

In a hysteretic ferromagnet ([[3-maxwell-and-waves/17-magnetization-and-maxwells-equations-in-matter|Lecture 17]]) $\mathbf{H}\cdot\partial\mathbf{B}/\partial t$ is no stored-energy rate: each cycle loses the loop area as heat.

> [!derivation]- The vector identity, and the same result in one dimension
> In components:
> $$
> \begin{aligned}
> \nabla\cdot(\mathbf{E}\times\mathbf{H}) &= \frac{\partial}{\partial x}(E_yH_z - E_zH_y)\\
> &\quad + \frac{\partial}{\partial y}(E_zH_x - E_xH_z)\\
> &\quad + \frac{\partial}{\partial z}(E_xH_y - E_yH_x).
> \end{aligned}
> $$
> The product rule splits each product; the six pieces with $\mathbf{E}$ differentiated give
> $$
> \begin{aligned}
> &H_x\Big(\frac{\partial E_z}{\partial y} - \frac{\partial E_y}{\partial z}\Big) + H_y\Big(\frac{\partial E_x}{\partial z} - \frac{\partial E_z}{\partial x}\Big)\\
> &\quad + H_z\Big(\frac{\partial E_y}{\partial x} - \frac{\partial E_x}{\partial y}\Big) = \mathbf{H}\cdot(\nabla\times\mathbf{E}).
> \end{aligned}
> $$
> The other six, each bracket reversed, give $-\mathbf{E}\cdot(\nabla\times\mathbf{H})$.
>
> **1-D check (Rao's route).** $\mathbf{E} = \hat x\,E_x(z,t)$, $\mathbf{H} = \hat y\,H_y(z,t)$ ([[3-maxwell-and-waves/18-the-wave-equation-and-plane-tem-waves#3-the-planar-problem-only-exzt-and-hyzt|Lecture 18]]) with a current $J_x$: $\partial E_x/\partial z = -\mu\,\partial H_y/\partial t$, $-\partial H_y/\partial z = J_x + \epsilon\,\partial E_x/\partial t$. With $S_z = E_xH_y$,
> $$
> \begin{aligned}
> \frac{\partial S_z}{\partial z} &= H_y\frac{\partial E_x}{\partial z} + E_x\frac{\partial H_y}{\partial z}\\
> &= -\mu H_y\frac{\partial H_y}{\partial t} - E_x\Big(J_x + \epsilon\frac{\partial E_x}{\partial t}\Big)\\
> &= -\frac{\partial}{\partial t}\Big(\tfrac12\mu H_y^2 + \tfrac12\epsilon E_x^2\Big) - J_xE_x ,
> \end{aligned}
> $$
> the theorem.

## 3. Reading the three terms

Each is W/m³: storage increase + net outflow + transfer to charges = 0.

**$\partial w/\partial t$: stored energy changing.** $w_e = \tfrac12\epsilon E^2$ and $w_m = \tfrac12\mu H^2$ [J/m³], read off a capacitor and a solenoid ([[concepts/electrostatic-energy]], [[concepts/magnetic-energy]]), hold for any time-varying field.

**$\nabla\cdot\mathbf{S}$: energy flowing away.** $\mathbf{S}$, the **energy flux density**, gives the flow direction and the power per unit perpendicular area: (V/m)(A/m) = VA/m² = W/m² = (J/s)/m², as $\mathbf{J}$ is (C/s)/m² = A/m². Where $\nabla\cdot\mathbf{S}>0$, energy is leaving that point.

**$\mathbf{J}\cdot\mathbf{E}$: energy handed to charges.** The force density $\rho(\mathbf{E} + \mathbf{u}\times\mathbf{B})$ does work at $\rho\,\mathbf{E}\cdot\mathbf{u} = \mathbf{J}\cdot\mathbf{E}$; the magnetic part does none ([[2-magnetostatics/12-magnetic-force-biot-savart-and-amperes-law|Lecture 12]]). The notes: **Joule heating**, non-zero only where there is current. Ohmic, $\mathbf{J} = \sigma\mathbf{E}$ ([[1-electrostatics/08-conductors-dielectrics-and-polarization#1-two-ideal-materials|Lecture 8]]):

$$
\mathbf{J}\cdot\mathbf{E} = \sigma E^2 = \frac{J^2}{\sigma}\ge0\qquad[\text{W/m}^3],
$$

point-form $I^2R$, passed to the lattice in Drude collisions ([[1-electrostatics/11-lorentz-drude-models-for-conductivity-and-susceptibility|Lecture 11]]); in a vacuum beam it is kinetic energy, in a charging battery chemical.

**Negative $\mathbf{J}\cdot\mathbf{E}$ is a source:** something else drives current against $\mathbf{E}$ and feeds the field at $-\mathbf{J}\cdot\mathbf{E}$ per m³. In a battery, current runs from − to + against the terminal charges' field ([[1-electrostatics/05-curl-free-fields-and-the-electrostatic-potential#1-why-a-potential-energy-per-unit-charge|Lecture 5]]); on Lecture 19's sheet, $\mathbf{E} = -\tfrac\eta2\mathbf{J}_s$. The notes' analogy: in the passive sign convention $vi>0$ absorbs, $vi<0$ supplies.

<!-- fig:poy-energy-ledger -->

> [!key] Poynting's theorem next to the continuity equation
> | | charge (Lecture 16) | electromagnetic energy (Lecture 20) |
> |---|---|---|
> | density | $\rho$ [C/m³] | $w = \tfrac12\epsilon E^2 + \tfrac12\mu H^2$ [J/m³] |
> | flux density | $\mathbf{J}$ [A/m² = (C/s)/m²] | $\mathbf{S} = \mathbf{E}\times\mathbf{H}$ [W/m² = (J/s)/m²] |
> | point form | $\partial\rho/\partial t + \nabla\cdot\mathbf{J} = 0$ | $\partial w/\partial t + \nabla\cdot\mathbf{S} = -\mathbf{J}\cdot\mathbf{E}$ |
> | exchange term | none: charge is never created or destroyed | $\mathbf{J}\cdot\mathbf{E}$: to heat, motion or chemistry ($>0$), or from them ($<0$) |
> | density moving at a speed | $\mathbf{J} = \rho\,\mathbf{u}$ | $\mathbf{S} = v\,w\,\hat u$ for one plane wave (§7) |
>
> The notes: the conservation law for energy, as continuity is for charge.

| situation | $\partial w/\partial t$ | $\nabla\cdot\mathbf{S}$ | $\mathbf{J}\cdot\mathbf{E}$ | what happens |
|---|---|---|---|---|
| plane wave, lossless medium | oscillates | $-\partial w/\partial t$ | 0 | transport at the wave speed |
| leaky capacitor discharging | $-\sigma E^2$ | 0 | $\sigma E^2$ | stored energy → heat in place |
| wire, steady current (§5) | 0 | $-\sigma E^2$ | $\sigma E^2$ | energy flows in, becomes heat |
| battery; radiating sheet (§6) | 0 (on average) | positive | negative | driven charges feed the field; energy flows away |

> [!example] Example — a leaky capacitor empties without any energy flow
> $\epsilon_r = 4$, $\sigma = 10^{-5}$ S/m, charged to $E_0 = 10$ kV/m (10 V across 1 mm), disconnected: $E = E_0e^{-t/\tau}$, $\tau = \epsilon/\sigma = 3.54$ µs. Conduction $\sigma\mathbf{E}$ and displacement $\epsilon\,\partial\mathbf{E}/\partial t = -(\epsilon/\tau)\mathbf{E} = -\sigma\mathbf{E}$ cancel: $\mathbf{H} = 0$, $\mathbf{S} = 0$ (edges ignored), $\partial w/\partial t = -\mathbf{J}\cdot\mathbf{E}$, heat in place. At $t = 0$, $w = \tfrac12\epsilon E_0^2 = 1.77$ mJ/m³, $\sigma E_0^2 = 1000$ W/m³ $= 2w/\tau$ ($w\propto e^{-2t/\tau}$): energy halves every $(\tau/2)\ln2 = 1.23$ µs, charge every 2.45 µs.

## 4. The integral form: a ledger for any volume

Integrate and apply the divergence theorem ([[0-toolkit/02-vector-calculus-cheatsheet#integral-theorems|toolkit]]); outward area element $d\mathbf{A}$, so as not to clash with $\mathbf{S}$.

> [!key] Poynting's theorem (integral form)
> $$
> \begin{gathered}
> -\frac{dW}{dt} = \oint_A\mathbf{S}\cdot d\mathbf{A} + \int_V\mathbf{J}\cdot\mathbf{E}\,dV,\\[4pt]
> W = \int_V\Big(\tfrac12\epsilon E^2 + \tfrac12\mu H^2\Big)dV .
> \end{gathered}
> $$
> Rate of decrease of stored energy in $V$ = outflow through $A$ + power handed to charges inside. A source inside supplies $-\int\mathbf{J}\cdot\mathbf{E}\,dV$ to storage, outflow and any resistive region.

> [!recipe] Using the integral form
> 1. **Surface:** pillbox (sheet), cylinder (wire), sphere (antenna), box beyond a wavefront.
> 2. **Outflow:** $\mathbf{S}\cdot d\mathbf{A}$ per face, outward; $\mathbf{S} = 0$ or tangential gives nothing.
> 3. **Exchange:** $\int\mathbf{J}\cdot\mathbf{E}\,dV$ ($\mathbf{J}_s\cdot\mathbf{E}$ × area for a sheet).
> 4. **Storage:** $dW/dt$; zero if steady, zero on average if periodic (§7).
> 5. **Check:** the sum is zero; the skipped term follows.

> [!example] Example — DC power travels in the dielectric of a coax, not in the copper
> Perfect conductors of radii $a$, $b$; inner at $V$, carrying $I$ along $+\hat z$. Between them $\mathbf{E} = \hat\rho\,V/\big(\rho\ln(b/a)\big)$ ([[1-electrostatics/10-capacitance-and-conductance#3-the-coaxial-cable|Lecture 10]]), $\mathbf{H} = \hat\phi\,I/(2\pi\rho)$, $\hat\rho\times\hat\phi = \hat z$:
> $$
> \begin{gathered}
> \mathbf{S} = \hat z\,\frac{VI}{2\pi\rho^2\ln(b/a)},\\[4pt]
> \int_a^bS_z\,2\pi\rho\,d\rho = \frac{VI}{\ln(b/a)}\int_a^b\frac{d\rho}{\rho} = VI .
> \end{gathered}
> $$
> All of $VI$ flows in the dielectric toward the load, mostly near the inner conductor ($S\propto1/\rho^2$). In the copper $\mathbf{E} = 0$, so $\mathbf{S} = 0$: it guides the energy, does not carry it (Unit 4).

> [!intuition] What S does and does not tell you
> Only $\nabla\cdot\mathbf{S}$ is fixed, so only flux through a *closed* surface is unambiguous. A charge beside a bar magnet has $\mathbf{E}\times\mathbf{H}\neq0$ though nothing changes: $\nabla\times\mathbf{E} = 0$ and $\nabla\times\mathbf{H} = \mathbf{J} = 0$ give $\nabla\cdot\mathbf{S} = 0$, closed loops carrying no net energy.

## 5. Joule heating at work: a wire is heated through its surface

Wire: radius $a$, length $\ell$, conductivity $\sigma$, steady $I$ along $+\hat z$. Steady means $\partial w/\partial t = 0$, so $\nabla\cdot\mathbf{S} = -\sigma E^2<0$: energy converges on the wire.

- **E** $= \hat z\,I/(\sigma\pi a^2)$ inside, continuous (tangential) just outside ([[3-maxwell-and-waves/16-charge-conservation-displacement-current-and-maxwells-equations#4-boundary-conditions--same-for-dynamics|Lecture 16]]); surface charges set it up and add a radial outside part ([[1-electrostatics/11-lorentz-drude-models-for-conductivity-and-susceptibility#6-what-drives-the-current-in-a-wire-a-footnote-worth-a-section|Lecture 11 §6]]).
- **H** $= \hat\phi\,I\rho/(2\pi a^2)$ inside, $\hat\phi\,I/(2\pi\rho)$ outside.
- **S** at the surface: $\hat z\times\hat\phi = -\hat\rho$, so $\mathbf{S} = -\hat\rho\,E_zH_\phi(a)$, radially **inward**.

Power through the side:

$$
\begin{aligned}
E_zH_\phi(a)\cdot2\pi a\ell &= \frac{I}{\sigma\pi a^2}\cdot\frac{I}{2\pi a}\cdot2\pi a\ell\\
&= I^2\,\frac{\ell}{\sigma\pi a^2} = I^2R,
\end{aligned}
$$

$R = \ell/(\sigma\pi a^2)$ ([[1-electrostatics/10-capacitance-and-conductance|Lecture 10]]). The end faces get nothing ($S_z = 0$). Inside, $S_\rho = -E_z\,I\rho/(2\pi a^2)$ carries $I^2R\,(\rho/a)^2$ across radius $\rho$: exactly the heat produced within it.

<!-- fig:poy-resistive-wire -->

Lines of $\mathbf{S}$ start in the battery ($\mathbf{J}\cdot\mathbf{E}<0$, $\nabla\cdot\mathbf{S}>0$), run alongside the wires (radial $\mathbf{E}$ with $\mathbf{H}$), and enter the resistor through its sides.

> [!example] Example — a 100 W heater wire
> Nichrome, resistivity about $1.10\ \mu\Omega\cdot$m ($\sigma\approx9.1\times10^5$ S/m), $a = 0.25$ mm, $\ell = 2$ m, $I = 3$ A: $R = 11.2\ \Omega$, $P = I^2R = 101$ W; $E = 16.8$ V/m ($E\ell = IR = 33.6$ V), $H(a) = I/(2\pi a) = 1.91$ kA/m; $\lvert\mathbf{S}\rvert = EH = 32.1$ kW/m² inward (about 24 suns); × side area $2\pi a\ell = 3.14\times10^{-3}$ m² $= 101$ W ✓.

## 6. The notes' example: monochromatic waves from a cosine sheet

> [!example] Example 1 (notes) — a cosine current sheet in vacuum
> On $z = 0$, $\mathbf{J}_s = \hat x\,f(t) = \hat x\,2\cos(\omega t)$ A/m, free space both sides. Find (a) $\mathbf{E}$, $\mathbf{H}$ for $z\gtrless0$, (b) $\mathbf{E}\times\mathbf{H}$, (c) $\mathbf{J}_s\cdot\mathbf{E}$ on the sheet.

**(a) The fields.** From [[3-maxwell-and-waves/19-dalembert-solutions-and-radiation-from-current-sheets#3-what-launches-a-plane-wave-the-notes-route|Lecture 19 §3]], $\mathbf{E} = -\hat x\,\tfrac\eta2f(t\mp z/v)$, $\mathbf{H} = \mp\hat y\,\tfrac12f(t\mp z/v)$, with $v = c$, $\eta = \eta_0\approx120\pi\ \Omega$; delay shifts the phase:

$$
\begin{gathered}
f\Big(t\mp\frac zc\Big) = 2\cos\Big(\omega t\mp\frac{\omega}{c}z\Big) = 2\cos(\omega t\mp\beta z),\\[4pt]
\beta\equiv\frac\omega c .
\end{gathered}
$$

> [!key] Example 1 (a): the radiated fields
> $$
> \begin{gathered}
> \mathbf{E}(z,t) = -\hat x\,\eta_0\cos(\omega t\mp\beta z)\ \ \text{V/m},\\[4pt]
> \mathbf{H}(z,t) = \mp\hat y\,\cos(\omega t\mp\beta z)\ \ \text{A/m},\quad z\gtrless0 .
> \end{gathered}
> $$
> Upper signs for $z>0$. Amplitudes $\eta_0\cdot2/2 = \eta_0\approx377$ V/m and $2/2 = 1$ A/m.

$\lambda = 2\pi/\beta$ ([[3-maxwell-and-waves/19-dalembert-solutions-and-radiation-from-current-sheets|Lecture 19 §7]]). One source frequency in a linear time-invariant medium gives that frequency everywhere: **monochromatic waves**, here real cosines; phasors are [[3-maxwell-and-waves/21-monochromatic-waves-and-phasor-notation|Lecture 21]].

**(b) The Poynting vectors.**

- $z>0$: $(-\eta_0\cos)(-\cos)\,\hat x\times\hat y = +\hat z\,\eta_0\cos^2(\omega t - \beta z)$;
- $z<0$: $(-\eta_0\cos)(+\cos)\,\hat x\times\hat y = -\hat z\,\eta_0\cos^2(\omega t + \beta z)$.

> [!key] Example 1 (b): the Poynting vectors
> $$
> \begin{gathered}
> \mathbf{S} = \mathbf{E}\times\mathbf{H} = \pm\hat z\,\eta_0\cos^2(\omega t\mp\beta z)\ \ \text{W/m}^2,\\[4pt]
> z\gtrless0 .
> \end{gathered}
> $$

The notes say the *average* points along the travel; for one wave the instantaneous $\mathbf{S}$ does too ($\cos^2\ge0$), since $\mathbf{E}$ and $\mathbf{H}$ flip together. Energy leaves in pulses at $2\omega$: humps $\lambda/2$ apart, moving at $c$ (figure, panel 1).

**(c) $\mathbf{J}_s\cdot\mathbf{E}$ on the sheet.** $\mathbf{E}(0,t) = -\hat x\,\eta_0\cos\omega t$ (continuous), so

$$
\begin{aligned}
\mathbf{J}_s\cdot\mathbf{E} &= \big(\hat x\,2\cos\omega t\big)\cdot\big(-\hat x\,\eta_0\cos\omega t\big)\\
&= -2\eta_0\cos^2(\omega t)\ \ \text{W/m}^2 .
\end{aligned}
$$

Power per unit *area* of sheet ([A/m]×[V/m]): $\int\mathbf{J}\cdot\mathbf{E}\,dz$ with $\mathbf{J} = \mathbf{J}_s\,\delta(z)$. Negative except at the zeros of $\cos\omega t$, so the sheet is a source; the notes: $\pm\mathbf{J}_s\cdot\mathbf{E}$ is power absorbed or injected per unit area.

**The books balance at every instant at the sheet.** Pillbox of face area $A$ hugging the sheet: outflow $\mathbf{S}(0^+)\cdot\hat z\,A + \mathbf{S}(0^-)\cdot(-\hat z)\,A = 2\eta_0\cos^2\omega t\,A$, no storage at zero height, and $\mathbf{J}_s\cdot\mathbf{E}\,A = -2\eta_0\cos^2\omega t\,A$: sum zero.

> [!key] Poynting's theorem across a current sheet
> $$
> \hat n\cdot(\mathbf{S}_1 - \mathbf{S}_2) = -\mathbf{J}_s\cdot\mathbf{E},
> $$
> $\hat n$ from side 2 into side 1: the jump in normal Poynting flux is the power per area the sheet injects. Lecture 16's boundary-condition pattern: $\nabla\to\hat n$, field → jump, $\mathbf{J}\to\mathbf{J}_s$, no time derivative (a thin pillbox stores nothing). Here $\hat n = \hat z$: $\eta_0\cos^2\omega t - (-\eta_0\cos^2\omega t) = 2\eta_0\cos^2\omega t$ ✓.

**Away from the sheet, inflow and outflow match only on average.** Slab $\lvert z\rvert<d$: energy enters at $2\eta_0\cos^2\omega t$ per m², leaves at $2\eta_0\cos^2(\omega t - \beta d)$ (delay $d/c$); the difference is stored:

$$
\frac{dW}{dt} = 2\eta_0\big[\cos^2\omega t - \cos^2(\omega t - \beta d)\big],
$$

per m² of sheet. For $\beta d = \pi/2$ this is $2\eta_0\cos2\omega t$: the slab fills and drains twice per cycle, averaging zero. Hence the notes compare *time averages*.

<!-- fig:poy-sheet-energy -->

## 7. Time averages

For period $T = 2\pi/\omega$, over any whole period,

$$
\langle f\rangle\equiv\frac1T\int_{t_0}^{t_0+T}f(t)\,dt,
$$

and the notes' tool is $\cos^2(\omega t + \phi) = \tfrac12\big[1 + \cos(2\omega t + 2\phi)\big]$: a constant plus a $2\omega$ ripple that averages to zero.

> [!key] The averages you need
> $$
> \begin{gathered}
> \langle\cos^2(\omega t + \phi)\rangle = \langle\sin^2(\omega t + \phi)\rangle = \tfrac12,\\[4pt]
> \langle\cos(\omega t + \phi)\rangle = 0,\qquad \langle\sin\omega t\cos\omega t\rangle = 0,
> \end{gathered}
> $$
> for every phase, including $\phi = \mp\beta z$: $\tfrac12$ at every point.

<!-- fig:poy-time-average -->

> [!key] Energy balance of the notes' sheet
> For $\mathbf{J}_s = \hat x\,2\cos\omega t$ A/m in vacuum:
> $$
> \begin{gathered}
> \langle\mathbf{E}\times\mathbf{H}\rangle = \pm\hat z\,\frac{\eta_0}{2}\approx\pm\hat z\,188\ \text{W/m}^2,\\[4pt]
> \langle-\mathbf{J}_s\cdot\mathbf{E}\rangle = \eta_0\approx377\ \text{W/m}^2 ,
> \end{gathered}
> $$
> upper sign for $z>0$: injected = $\eta_0/2 + \eta_0/2$ (the notes' $60\pi$ and $120\pi$). For $\hat x\,J_0\cos\omega t$ in impedance $\eta$: $\eta J_0^2/8$ per side, $\langle-\mathbf{J}_s\cdot\mathbf{E}\rangle = \eta J_0^2/4$.

**Why stored energy drops out.** Periodic steady state: $\langle\partial w/\partial t\rangle = [w(t_0 + T) - w(t_0)]/T = 0$, leaving:

> [!key] Time-averaged Poynting theorem (periodic steady state)
> $$
> \begin{gathered}
> \nabla\cdot\langle\mathbf{S}\rangle = -\langle\mathbf{J}\cdot\mathbf{E}\rangle,\\[4pt]
> \oint_A\langle\mathbf{S}\rangle\cdot d\mathbf{A} = -\int_V\langle\mathbf{J}\cdot\mathbf{E}\rangle\,dV .
> \end{gathered}
> $$
> Average outflow = power injected minus power dissipated inside. Slab $\lvert z\rvert<d$: $\eta_0/2 + \eta_0/2 = \eta_0$ for every $d$.

**A single plane wave**, $\mathbf{E} = \hat x\,E_0\cos(\omega t - \beta z)$, $\mathbf{H} = \hat y\,(E_0/\eta)\cos(\omega t - \beta z)$ ([[3-maxwell-and-waves/18-the-wave-equation-and-plane-tem-waves#5-h-from-e-the-intrinsic-impedance|Lecture 18 §5]]):

$$
\langle\mathbf{S}\rangle = \hat z\,\frac{E_0^2}{2\eta} = \hat z\,\tfrac12\eta H_0^2 = \hat z\,\tfrac12E_0H_0 .
$$

Since $\eta^2 = \mu/\epsilon$, $\tfrac12\mu(E/\eta)^2 = \tfrac12\epsilon E^2$: electric and magnetic energies are equal at every instant, $w = \epsilon E^2$, $\langle w\rangle = \tfrac12\epsilon E_0^2$, and $\langle S\rangle = v\langle w\rangle$, like $\mathbf{J} = \rho\mathbf{u}$. Notes' example: $\langle w\rangle = \eta_0/(2c) = 6.3\times10^{-7}$ J/m³ per side.

> [!example] Example — J·E in sea water (the exam's question, new numbers)
> Sea water ($\sigma\approx4$ S/m), low-frequency $\mathbf{E} = \hat y\,0.5\cos\omega t$ V/m: $\mathbf{J} = \hat y\,2\cos\omega t$ A/m², $\mathbf{J}\cdot\mathbf{E} = \sigma E^2 = \cos^2\omega t$ W/m³; peak 1, average 0.5 W/m³ of heat, half a milliwatt per litre. Summer 2019 HE3 #1b.

> [!example] Example — sunlight and a radio station as fields
> - **Sunlight** above the atmosphere: about 1361 W/m². As one cosine wave, $E_0 = \sqrt{2\eta_0\langle S\rangle}\approx1.01$ kV/m, $H_0 = E_0/\eta_0\approx2.69$ A/m (rms 716 V/m, 1.90 A/m); energy density $\langle S\rangle/c\approx4.5\ \mu$J/m³.
> - **A 50 kW transmitter radiating equally in all directions** (idealized). Averaged integral form on a sphere of radius $r$, enclosing only the transmitter: $4\pi r^2\langle S\rangle = 50$ kW for every $r$, $\langle S\rangle\propto1/r^2$. Far out (many wavelengths) the wave is locally plane, $E_0 = \sqrt{2\eta_0\langle S\rangle}\propto1/r$; near the antenna, energy-storing fields break this. At 10 km: $\langle S\rangle = 3.98\times10^{-5}$ W/m², $E_0 = 0.173$ V/m; with $\eta_0 = 120\pi$, $E_0 = \sqrt{60P}/r$ (Rao's argument).

> [!example] Example — perpendicular components carry power independently
> $\mathbf{E} = \hat x\,E_1\cos(\omega t - \beta z) + \hat y\,E_2\cos(\omega t - \beta z + \phi)$, $\mathbf{H} = \hat z\times\mathbf{E}/\eta$: $S_z = E_xH_y - E_yH_x = (E_x^2 + E_y^2)/\eta$, no cross term, so $\langle\mathbf{S}\rangle = \hat z\,(E_1^2 + E_2^2)/(2\eta)$ for any $\phi$. $E_1 = 3$, $E_2 = 4$ V/m in vacuum: $25/(2\times377) = 33$ mW/m². Exams "split, then add" for circular polarization (Lecture 24).

> [!example] Example — two equal waves in opposite directions: S ≠ 0 but ⟨S⟩ = 0
> $\hat x\,E_0\cos(\omega t - \beta z)$ plus $-\hat x\,E_0\cos(\omega t + \beta z)$ ([[3-maxwell-and-waves/18-the-wave-equation-and-plane-tem-waves|Lecture 18]]), each with its own $\mathbf{H}$:
> $$
> \begin{gathered}
> \mathbf{E} = \hat x\,2E_0\sin\omega t\,\sin\beta z,\\[4pt]
> \mathbf{H} = \hat y\,\frac{2E_0}{\eta}\cos\omega t\,\cos\beta z,\\[4pt]
> \mathbf{S} = \hat z\,\frac{E_0^2}{\eta}\sin2\omega t\,\sin2\beta z .
> \end{gathered}
> $$
> $\mathbf{S}$ flips sign every quarter period; $\langle\mathbf{S}\rangle = 0$ at every $z$ ($= (\lvert\mathbf{E}_1\rvert^2 - \lvert\mathbf{E}_2\rvert^2)/\eta$, [[concepts/poynting-vector]]). Yet $\langle w\rangle = \epsilon E_0^2$ everywhere, sloshing between electric ($\mathbf{E}$ maxima) and magnetic ($\mathbf{H}$ maxima) each quarter period; where $\sin\beta z = 0$, $w = 0$ when $\cos\omega t = 0$. Each half wavelength's energy is constant (Lecture 26).

> [!trap] Where time averages go wrong
> - **The ½ belongs to the average of a squared cosine.** DC has none; the *peak* of $\cos^2$ is 1.
> - **Average the product, not the factors:** $\langle E\rangle\langle H\rangle = 0\times0$, but $\langle EH\rangle = \tfrac12E_0H_0$ for one wave.
> - **Per area or per volume?** $\mathbf{J}_s\cdot\mathbf{E}$ is W/m², $\mathbf{J}\cdot\mathbf{E}$ W/m³. Exams call $\langle\mathbf{J}_s\cdot\mathbf{E}\rangle$ "the average Joule heating rate" even at a source (negative).
> - **A sheet's power splits evenly** (same medium both sides): each side carries half.
> - **E and H out of phase** (lossy media, Lectures 22–23, $\mathbf{H}$ lags $\mathbf{E}$): $\langle S\rangle\neq\tfrac12E_0H_0$; $\cos a\cos b = \tfrac12[\cos(a - b) + \cos(a + b)]$ gives $\langle\cos(\omega t + \phi_1)\cos(\omega t + \phi_2)\rangle = \tfrac12\cos(\phi_1 - \phi_2)$ (Lecture 21's phasor rule).

## 8. Connections

- **Lectures 10, 15, 16, 19:** energy densities now general; continuity as template; the sheet injects $\tfrac\eta2J_s^2$ per m², half into each wave.
- **Lectures 21–23, Unit 4:** phasor averages; power decay $e^{-2\alpha z}$ in conductors; lines guide $\mathbf{S}$.

## 9. Summary

- $\mathbf{H}\cdot$(Faraday) $-\ \mathbf{E}\cdot$(Ampère–Maxwell) gives the theorem; $\mathbf{J}\cdot\mathbf{E} = \sigma E^2$ in a conductor, $<0$ at a source.
- $I^2R$ enters a resistor through its sides; coax power flows in the dielectric.
- Sheet, on average: $\eta_0/2$ per side, $\eta_0$ injected; one wave $\langle S\rangle = E_0^2/2\eta = v\langle w\rangle$; standing wave $\langle S\rangle = 0$, $\langle w\rangle\neq0$.

Concept pages: [[concepts/poynting-theorem]] · [[concepts/poynting-vector]] · [[concepts/continuity-equation]] · [[concepts/electrostatic-energy]] · [[concepts/magnetic-energy]] · [[concepts/conductors]] · [[concepts/current-sheet-radiation]] · [[concepts/plane-waves]] · [[concepts/divergence-theorem]].

> [!exam] On exams
> **Fall 2026:** the last lecture on Midterm 2 (October 19; [[0-toolkit/05-midterm-2-summary#9-energy-and-power-poyntings-theorem-lecture-20|summary §9]]); expect it closing a sheet or plane-wave problem. Exam 3 papers ask:
> 1. **Average power of a wave:** $E_0^2/(2\eta)$ (Summer 2017/2018 HE3, SP17 #4b, Summer 2020 FE #4c); exact, $\eta_0 = 120\pi$; phasor form in Lecture 21.
> 2. **Split, then add** for circular polarization (§7).
> 3. **J·E in a conductor:** peak $\sigma E_0^2$, average $\sigma E_0^2/2$, W/m³ (Summer 2019 HE3 #1b, and conflict version).
> 4. **Radiating sheet:** $\langle\mathbf{J}_s\cdot\mathbf{E}\rangle<0$, then half its magnitude into one half-space (Summer 2020 HE3 #2c–d; worked problem: same steps, other geometry; exam key not reproduced).
> 5. **Standing-wave true/false** (SP17 #1c, FA23 #1(c)): write $\mathbf{S}$, $w$, average; watch "instantaneous"/"time-averaged", "at a point"/"in the region".
> 6. **Power against depth** (Summer 2018/2019 HE3 #3b(v), FA23 #6(b)): $\propto E^2$, so $e^{-2\alpha z}$ when the field falls as $e^{-\alpha z}$.
> 7. **Power through an area:** $\langle S\rangle$ × area (SP19 #2c, Unit 4).

> [!tip] Practice this lecture
> [[practice/20-poynting-theorem-and-power|12 practice problems]] — 5 easy, 3 medium, 4 hard — each with a folded hint and a worked solution. Start with [[practice/20-poynting-theorem-and-power#201-reading-the-energy-ledger|20.1 Reading the energy ledger]]; the [[practice/index|practice hub]] has the whole bank by difficulty and by topic.

### Sources for this page
Kudeki notes, Lecture 20 (no slides yet): derivation, three terms, negative $\mathbf{J}\cdot\mathbf{E}$, Example 1 (numbers checked), time averages; $\eta_o$ for $\eta_0$. Rao (2009) §4.6, §5.3: the 1-D derivation, the $1/r$ argument (reworded). This site's own: validity conditions, the situation table, other examples, pillbox, slab, averaged theorem, traps, figures; numbers in `digest8/verify_L20.py`. Slips in the course material: see [[0-toolkit/04-errata-in-the-course-materials|errata]].
