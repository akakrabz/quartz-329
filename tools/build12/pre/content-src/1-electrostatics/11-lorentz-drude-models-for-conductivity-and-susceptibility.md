---
title: "Lecture 11 — Where σ and χe come from: the Lorentz–Drude models"
description: "Free carriers drifting between collisions give Ohm's law with σ = Nq²τ/m (complex at high frequency); bound electrons on springs give χe = Nde²/(mε₀ω₀²) and, when the field varies, a polarization current ∂P/∂t — the seed of Maxwell's displacement current."
tags: [lecture, electrostatics]
lecture: 11
---

*Lecture 11 · course notes §11 · no slide deck (the slides jump from capacitance to Biot–Savart) · prev: [[1-electrostatics/10-capacitance-and-conductance|Lecture 10]] · next: [[2-magnetostatics/12-magnetic-force-biot-savart-and-amperes-law|Lecture 12]] · not on Exam 1 · practice: [[practice/11-lorentz-drude-models|8 problems]]*

> [!abstract] In one breath
> Unit 1 used two material constants without explaining them: $\sigma$ in $\mathbf{J} = \sigma\mathbf{E}$ ([[1-electrostatics/08-conductors-dielectrics-and-polarization|Lecture 8]]) and $\chi_e$ in $\mathbf{P} = \epsilon_0\chi_e\mathbf{E}$ ([[1-electrostatics/09-static-fields-in-dielectric-media|Lecture 9]]). The mechanism is Newton's second law for one charge at a time. A **free** carrier accelerates, collides, and settles at a drift velocity $\propto\mathbf{E}$: Ohm's law with $\sigma = Nq^2\tau/m$. A **bound** electron is pulled against a spring; $N_d$ such dipoles per unit volume give $\chi_e = N_de^2/(m\epsilon_0\omega_0^2)$. When the field varies the bound electrons move too — a **polarization current** $\partial\mathbf{P}/\partial t$ flows in a perfect insulator, half of what Lecture 16 adds to Ampère's law.

## 1. Two constants, one law of motion

<!-- fig:drude-lorentz-models -->

Everything follows from $m\,d\mathbf{v}/dt = \sum\mathbf{F}$ for a single charge, averaged over many. Conductor and dielectric differ only in *which forces* act:

| | free carrier (metal, electrolyte, plasma) | bound electron (dielectric) |
|---|---|---|
| driving force | $q\mathbf{E}$ | $-e\mathbf{E}$ |
| restoring force | none — the carrier wanders | $-m\omega_0^2\mathbf{r}$ (the spring of the atom) |
| dissipation | collisions, $-m\mathbf{v}/\tau$ | radiation and collisions, $-2m\alpha\,\dot{\mathbf{r}}$ |
| DC response | steady **velocity** $\Rightarrow$ current | steady **displacement** $\Rightarrow$ polarization |
| material constant | $\sigma$ [S/m] | $\chi_e$, $\epsilon = (1+\chi_e)\epsilon_0$ |

$\mathbf{v}$ is an *average*: each carrier's velocity is $\mathbf{v}+\delta\mathbf{v}$ with a zero-mean random part that is huge (thermal speeds $\sim10^5$ m/s in copper) but averages away. Only the tiny coherent drift (a fraction of a millimetre per second for a household current) carries current.

## 2. Free carriers: the Drude model and Ohm's law

A carrier of charge $q$ and mass $m$ in $\mathbf{E}$, with a friction force representing collisions at average rate $\nu = 1/\tau$:

> [!key] Drude equation of motion
> $$
> m\frac{d\mathbf{v}}{dt} = q\mathbf{E} - m\frac{\mathbf{v}}{\tau}.
> $$
> With $\mathbf{E} = 0$, $\mathbf{v}(t) = \mathbf{v}(0)e^{-t/\tau}$: left alone, a conductor with uniform carrier density carries no current. With constant $\mathbf{E}$ the steady state ($d\mathbf{v}/dt = 0$) is
> $$
> \mathbf{v} = \frac{q\tau}{m}\mathbf{E},\qquad\Big|\frac{q\tau}{m}\Big| = \text{the mobility}\ [\text{m}^2/(\text{V·s})].
> $$

**From velocity to current.** In a unit cube with $N$ carriers moving at $v$ toward one face, every carrier within distance $v$ of the face crosses it in one second: charge per unit area per second $Nqv$.

> [!key] Current density and conductivity
> $$
> \begin{gathered}
> \mathbf{J} = Nq\mathbf{v} = \frac{Nq^2\tau}{m}\mathbf{E} = \frac{Nq^2}{m\nu}\mathbf{E}\quad[\text{A/m}^2],\\[4pt]
> \text{so}\qquad \mathbf{J} = \sigma\mathbf{E},\quad\boxed{\ \sigma = \sum_s\frac{N_sq_s^2}{m_s\nu_s}\ }.
> \end{gathered}
> $$
> The sum runs over carrier species $s$ (electrons, holes, ions). $q_s$ enters squared, so negative carriers conduct as well as positive ones, in the *same* direction of $\mathbf{J}$.

This is Lecture 8's postulated Ohm's law; its proviso ("provided the carriers suffer occasional collisions") is the $\tau$ in the numerator: no collisions, no steady state, no $\sigma$.

> [!example] Example — copper
> $N\approx8.5\times10^{28}$ m⁻³ (one free electron per atom), $\sigma = 5.96\times10^7$ S/m. Collision time $\tau = \sigma m_e/(Ne^2)\approx2.5\times10^{-14}$ s, i.e. $\nu\approx4\times10^{13}$ s⁻¹; mobility $e\tau/m_e\approx4.4\times10^{-3}$ m²/(V·s). A 1 A current in a 1 mm² wire has $J = 10^6$ A/m², needs only $E = J/\sigma\approx0.017$ V/m, and drifts at $v = J/(Ne)\approx7\times10^{-5}$ m/s — a tenth of a millimetre per second. The electrons do not race down the wire; the *field* does, at essentially $c$.

The notes' table of DC conductivities (silver, copper, gold $\sim$ several $\times10^7$ S/m; sea water 4; intrinsic silicon $1.6\times10^{-3}$; dry earth $\sim10^{-5}$; glass $10^{-10}$–$10^{-14}$) spans twenty orders of magnitude, almost all of it in $N$: a good insulator has no free carriers.

> [!trap] Two different τ's
> The Drude $\tau$ (collision time, $\sim10^{-14}$ s: how fast carriers respond) is not Lecture 8's relaxation time $\tau = \epsilon/\sigma$ (how fast an excess charge leaves a conductor's interior: $\sim10^{-19}$ s for copper, microseconds for a poor conductor). The course calls both $\tau$. Also: superconductivity is the case where the DC *resistivity* vanishes ($\sigma\to\infty$), a correlated-carrier effect outside this model (slip in the notes: [[0-toolkit/04-errata-in-the-course-materials|errata page]]).

## 3. AC conductivity: when the carriers cannot keep up

With phasors (ECE 210), $\mathbf{E}(t) = \text{Re}\{\tilde{\mathbf{E}}e^{j\omega t}\}$ and likewise $\mathbf{v}$, $\mathbf{J}$; $d/dt\to j\omega$:

$$
mj\omega\tilde{\mathbf{v}} = q\tilde{\mathbf{E}} - m\frac{\tilde{\mathbf{v}}}{\tau}\quad\Rightarrow\quad\tilde{\mathbf{v}} = \frac{q\tilde{\mathbf{E}}}{m(\nu + j\omega)},
$$

> [!key] AC conductivity
> $$
> \tilde{\mathbf{J}} = \sigma\tilde{\mathbf{E}},\qquad \sigma(\omega) = \sum_s\frac{N_sq_s^2}{m_s(\nu_s + j\omega)} = \frac{\sigma_{\text{DC}}}{1 + j\omega/\nu}\ (\text{one species}).
> $$
> For $\omega\ll\nu$ this is the DC value: the carriers reach their drift velocity long before the field reverses. For copper $\nu\sim4\times10^{13}$ s⁻¹, so DC conductivity holds through the radio and microwave range (at 1 GHz the correction is $1.6\times10^{-4}$). The complex part — current lagging the field — matters only in the infrared and beyond, and in plasmas where $\nu$ can be tiny.

Quantum mechanics keeps the form of these results, replacing $m_s$ by an *effective mass* — why the classical model survived.

## 4. Bound electrons: the Lorentz oscillator and χe

A perfect dielectric has no free carriers ($\sigma = 0$), but its atoms polarize. Model each atom as a nucleus with an electron displaced by $\mathbf{r}$: dipole $\mathbf{p} = -e\mathbf{r}$, pointing from electron to nucleus, i.e. *along* $\mathbf{E}$. Three forces act on the electron — applied field, spring-like binding, damping:

> [!key] Lorentz equation of motion
> $$
> m\frac{d^2\mathbf{r}}{dt^2} = -e\mathbf{E} - m\omega_0^2\mathbf{r} - 2m\alpha\frac{d\mathbf{r}}{dt}.
> $$
> Left alone, the atom rings down as $\mathbf{r}(t)\approx\mathbf{r}_0e^{-\alpha t}\cos\omega_0t$ — the zero-input response of a strongly underdamped ($\omega_0\gg\alpha$) second-order system. $\omega_0$ comes from the atom's energy levels (optical and ultraviolet, $10^{15}$–$10^{16}$ rad/s); $\alpha$ from the width $2\alpha$ of its spectral lines.

**DC response.** With constant $\mathbf{E}$ the steady state is $\mathbf{r} = -\dfrac{e}{m\omega_0^2}\mathbf{E}$, hence

$$
\mathbf{p} = -e\mathbf{r} = \frac{e^2}{m\omega_0^2}\mathbf{E},\qquad
\mathbf{P} = N_d\mathbf{p} = \frac{N_de^2}{m\omega_0^2}\mathbf{E}\equiv\epsilon_0\chi_e\mathbf{E},
$$

> [!key] DC susceptibility
> $$
> \chi_e = \frac{N_de^2/(m\epsilon_0)}{\omega_0^2},\qquad \epsilon_r = 1+\chi_e.
> $$
> Stiffer springs (larger $\omega_0$) and sparser atoms (smaller $N_d$) give smaller $\chi_e$. $N_d\sim5\times10^{28}$ m⁻³ and $\omega_0\sim2\pi\times3\times10^{15}$ rad/s give $\chi_e\approx0.45$ — glass-like.

**AC response (an extension, not in the notes).** The phasor equation gives

$$
\chi_e(\omega) = \frac{N_de^2/(m\epsilon_0)}{\omega_0^2 - \omega^2 + 2j\alpha\omega},
$$

the DC value for $\omega\ll\omega_0$ — all of ECE 329, where "$\epsilon$ is a constant" — but growing, peaking and turning complex near $\omega_0$: dispersion (prisms, chromatic aberration) and absorption (the imaginary part; glass is opaque in the ultraviolet). Unit 3 meets complex permittivities from the conductivity side; this is the dielectric side.

## 5. Polarization current: bound charges that carry an AC current

Let $\mathbf{E}$ vary slowly compared with $\omega_0$, so $\mathbf{r} = -\dfrac{e}{m\omega_0^2}\mathbf{E}$ tracks the field. The bound electrons *move*, $\mathbf{v} = d\mathbf{r}/dt = -\dfrac{e}{m\omega_0^2}\dfrac{d\mathbf{E}}{dt}$, and $N_d$ of them per unit volume, each carrying $-e$, give

> [!key] Polarization current density
> $$
> \mathbf{J}_p = -eN_d\mathbf{v} = \frac{N_de^2}{m\omega_0^2}\frac{\partial\mathbf{E}}{\partial t} = \frac{\partial\mathbf{P}}{\partial t}\quad[\text{A/m}^2].
> $$
> A perfect dielectric carries no DC current — the springs stop the electrons — but carries an AC current whenever its polarization changes. Nothing is conducted; the charges slosh.

The *total* current density under a time-varying field is free-carrier conduction plus bound-charge polarization current, $\sigma\mathbf{E} + \partial\mathbf{P}/\partial t$. Lecture 16 shows Ampère's law needs, besides $\mathbf{J} = \sigma\mathbf{E}$,

$$
\frac{\partial\mathbf{D}}{\partial t} = \epsilon_0\frac{\partial\mathbf{E}}{\partial t} + \frac{\partial\mathbf{P}}{\partial t}:
$$

this lecture's polarization current plus a vacuum term with no charges behind it. The lossy capacitor of [[1-electrostatics/10-capacitance-and-conductance#6-conductance-the-leaky-capacitor|Lecture 10]] already had both: $G$ carries $\sigma\mathbf{E}$, $C$ carries $\partial\mathbf{D}/\partial t$ — hence $I = GV + C\,dV/dt$.

## 6. What drives the current in a wire? (a footnote worth a section)

[[1-electrostatics/08-conductors-dielectrics-and-polarization|Lecture 8]]: $\mathbf{E} = 0$ inside a conductor *in equilibrium*. Here: $\mathbf{E} = \mathbf{J}/\sigma\neq0$ inside a wire *carrying a current*. The notes' footnote (Jefimenko 1962, Parker 1970, *Am. J. Phys.*) reconciles them: the field inside a resistive wire is an **electrostatic field produced by surface charges on the wire itself**, graded along its length — denser near one terminal, sparser near the other. They arrange themselves, on Lecture 8's relaxation time scale, so that $\mathbf{E}$ inside follows every bend with magnitude exactly $J/\sigma$. Outside, the same charges make a field with a large radial component (demonstrated with suspended fibres, like iron filings for a magnetic field). An ideal zero-resistivity wire needs no such field or charge — the idealization Lecture 12 starts from when it calls a current-carrying wire neutral.

## 7. Summary

- One law of motion, $m\,d\mathbf{v}/dt = \sum\mathbf{F}$, averaged over carriers.
- Free carriers: $\mathbf{v} = (q\tau/m)\mathbf{E}$, $\mathbf{J} = Nq\mathbf{v}$, $\sigma = \sum_sN_sq_s^2/(m_s\nu_s)$; AC: $\nu\to\nu + j\omega$, DC value valid for $\omega\ll\nu\sim10^{13}$ s⁻¹.
- Bound electrons: $m\ddot{\mathbf{r}} = -e\mathbf{E} - m\omega_0^2\mathbf{r} - 2m\alpha\dot{\mathbf{r}}$; DC $\chi_e = N_de^2/(m\epsilon_0\omega_0^2)$; AC $\chi_e(\omega)$ complex near $\omega_0$.
- $\mathbf{J}_p = \partial\mathbf{P}/\partial t$; Ampère's law will need the total $\sigma\mathbf{E} + \partial\mathbf{D}/\partial t$.
- The field in a current-carrying wire is made by surface charges on the wire.

Concept page: [[concepts/conductivity-and-susceptibility-models]] · related: [[concepts/conductors]] · [[concepts/polarization]] · [[concepts/permittivity]].

> [!exam] On exams
> Not on Exam 1. Testable content is small and conceptual: drift velocity from the force balance, $\mathbf{J} = Nq\mathbf{v}$, $\sigma\propto Nq^2\tau/m$ and why the DC value holds at radio frequencies, $\partial\mathbf{P}/\partial t$ is a current. Given $N$, $q$, $m$, $\tau$ and asked for $\sigma$ or the mobility: this lecture.

> [!tip] Practice this lecture
> [[practice/11-lorentz-drude-models|8 practice problems]] — 4 easy, 2 medium, 2 hard — each with a folded hint and a worked solution. Start with [[practice/11-lorentz-drude-models#111-drift-speed-in-a-house-wire|11.1 Drift speed in a house wire]]; the [[practice/index|practice hub]] has the whole bank by difficulty and by topic.

### Sources for this page
Kudeki notes, Lecture 11 (Drude force balance, mobility, unit-cube $\mathbf{J} = Nq\mathbf{v}$, species sum, AC conductivity, conductivity table, Lorentz oscillator, DC susceptibility, polarization current, $\sigma\mathbf{E} + d\mathbf{P}/dt$); Lecture 12 footnote 2 and the Jefimenko (1962) and Parker (1970) papers it cites. The site's own: copper numbers and the AC susceptibility formula, checked against the notes' DC limits.
