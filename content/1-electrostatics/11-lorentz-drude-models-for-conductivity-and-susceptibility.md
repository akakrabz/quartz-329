---
title: "Lecture 11 — Where σ and χe come from: the Lorentz–Drude models"
description: "Two mechanical pictures explain the two material constants of Unit 1. Free carriers that drift between collisions give Ohm's law with σ = Nq²τ/m (and a complex σ at high frequency); bound electrons on springs give the susceptibility χe = Nde²/(mε₀ω₀²) and, when the field varies, a polarization current ∂P/∂t. The second is the seed of Maxwell's displacement current."
tags: [lecture, electrostatics]
lecture: 11
---

*Lecture 11 · course notes §11 · no slide deck (the slides jump from capacitance to Biot–Savart) · prev: [[1-electrostatics/10-capacitance-and-conductance|Lecture 10]] · next: [[2-magnetostatics/12-magnetic-force-biot-savart-and-amperes-law|Lecture 12]] · not on Exam 1 · practice: [[practice/11-lorentz-drude-models|8 problems]]*

> [!abstract] In one breath
> Unit 1 used two material constants without explaining them: the conductivity $\sigma$ in $\mathbf{J} = \sigma\mathbf{E}$ ([[1-electrostatics/08-conductors-dielectrics-and-polarization|Lecture 8]]) and the susceptibility $\chi_e$ in $\mathbf{P} = \epsilon_0\chi_e\mathbf{E}$ ([[1-electrostatics/09-static-fields-in-dielectric-media|Lecture 9]]). This lecture supplies the mechanism, Newton's second law applied to one charge at a time. A **free** carrier accelerates in $\mathbf{E}$, collides, and settles at a drift velocity $\propto\mathbf{E}$; multiply by the carrier density and charge and you have Ohm's law with $\sigma = Nq^2\tau/m$. A **bound** electron is pulled off its nucleus against a spring; the dipole it makes is $\propto\mathbf{E}$, and $N_d$ of them per unit volume give $\chi_e = N_de^2/(m\epsilon_0\omega_0^2)$. Let the field vary in time and the bound electrons move too — a **polarization current** $\partial\mathbf{P}/\partial t$ flows in a perfect insulator. That current is half of what Lecture 16 will add to Ampère's law.

## 1. Two constants, one law of motion

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 290" width="640" height="290" role="img" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:14px"><defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="context-stroke"/></marker><marker id="ahs" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="context-stroke"/></marker></defs><text x="160.0" y="30.0" text-anchor="middle" fill="var(--accent)" style="font-size:13px;font-weight:600;">free carrier (Drude): collisions + drift</text><path d="M73.6,170.1 L102.2,187.2 L114.8,149.5 L145.5,170.1 L113.9,174.3 L110.9,143.4 L81.0,167.8 L44.8,184.6 L41.3,138.0" fill="none" stroke="currentColor" stroke-width="1.3" stroke-dasharray="4 3" opacity="0.7" stroke-linejoin="round" stroke-linecap="round"/><circle cx="73.6" cy="170.1" r="6.0" fill="var(--hi)" stroke="none" stroke-width="1.5"/><line x1="68.6" y1="170.1" x2="78.6" y2="170.1" stroke="white" stroke-width="2.2" stroke-linecap="round"/><line x1="73.6" y1="165.1" x2="73.6" y2="175.1" stroke="white" stroke-width="2.2" stroke-linecap="round"/><text x="90.0" y="100.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px;">E = 0: no net drift</text><path d="M201.6,170.1 L243.2,187.2 L268.8,149.5 L312.5,170.1 L293.9,174.3 L303.9,143.4 L287.0,167.8 L263.8,184.6 L273.3,138.0" fill="none" stroke="var(--accent)" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round"/><circle cx="201.6" cy="170.1" r="6.0" fill="var(--hi)" stroke="none" stroke-width="1.5"/><line x1="196.6" y1="170.1" x2="206.6" y2="170.1" stroke="white" stroke-width="2.2" stroke-linecap="round"/><line x1="201.6" y1="165.1" x2="201.6" y2="175.1" stroke="white" stroke-width="2.2" stroke-linecap="round"/><line x1="269.3" y1="138.0" x2="295.3" y2="138.0" stroke="var(--accent)" stroke-width="2.2" marker-end="url(#ah)" stroke-linecap="round"/><text x="252.0" y="100.0" text-anchor="middle" fill="var(--accent)" style="font-size:11px;">E on: mean drift v = (qτ/m)E</text><line x1="100.0" y1="245.0" x2="260.0" y2="245.0" stroke="var(--hi)" stroke-width="2.4" marker-end="url(#ah)" stroke-linecap="round"/><text x="180.0" y="263.0" text-anchor="middle" fill="var(--hi)" style="font-size:15px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;font-weight:600;">E</text><text x="180.0" y="220.0" text-anchor="middle" fill="currentColor" style="font-size:12.5px;font-weight:600;">J = Nqv = σE,   σ = Nq²τ/m</text><text x="500.0" y="30.0" text-anchor="middle" fill="var(--accent2)" style="font-size:13px;font-weight:600;">bound electron (Lorentz): a spring</text><rect x="390.0" y="80.0" width="230.0" height="150.0" rx="70" fill="var(--accent2)" fill-opacity="0.08" stroke="none"/><circle cx="520.0" cy="150.0" r="12.0" fill="var(--accent2)" stroke="none" stroke-width="1.5"/><line x1="515.0" y1="150.0" x2="525.0" y2="150.0" stroke="white" stroke-width="2.2" stroke-linecap="round"/><line x1="520.0" y1="145.0" x2="520.0" y2="155.0" stroke="white" stroke-width="2.2" stroke-linecap="round"/><text x="520.0" y="180.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px;">nucleus</text><path d="M508.0,150.0 L503.1,157.0 L493.4,143.0 L483.7,157.0 L474.0,143.0 L464.3,157.0 L454.6,143.0 L444.9,157.0 L446.0,150.0" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linejoin="round" stroke-linecap="round"/><circle cx="440.0" cy="150.0" r="8.0" fill="var(--hi)" stroke="none" stroke-width="1.5"/><line x1="435.0" y1="150.0" x2="445.0" y2="150.0" stroke="white" stroke-width="2.2" stroke-linecap="round"/><text x="440.0" y="132.0" text-anchor="middle" fill="var(--hi)" style="font-size:12px;">−e</text><line x1="520.0" y1="110.0" x2="440.0" y2="110.0" stroke="currentColor" stroke-width="1.6" marker-end="url(#ahs)" stroke-linecap="round"/><text x="480.0" y="104.0" text-anchor="middle" fill="currentColor" style="font-size:14px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">r</text><line x1="550.0" y1="110.0" x2="605.0" y2="110.0" stroke="var(--hi)" stroke-width="2.2" marker-end="url(#ah)" stroke-linecap="round"/><text x="578.0" y="104.0" text-anchor="middle" fill="var(--hi)" style="font-size:14px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;font-weight:600;">E</text><line x1="550.0" y1="205.0" x2="605.0" y2="205.0" stroke="var(--accent2)" stroke-width="2.2" marker-end="url(#ah)" stroke-linecap="round"/><text x="578.0" y="222.0" text-anchor="middle" fill="var(--accent2)" style="font-size:12px;font-weight:600;">p = −e r  ∥ E</text><text x="500.0" y="260.0" text-anchor="middle" fill="currentColor" style="font-size:12.5px;font-weight:600;">m r″ = −eE − mω₀²r − 2mα r′</text><text x="500.0" y="278.0" text-anchor="middle" fill="currentColor" style="font-size:11.5px;">DC:  P = N<tspan baseline-shift="sub" style="font-size:9px">d</tspan> p = ε₀χₑE,   χₑ = N<tspan baseline-shift="sub" style="font-size:9px">d</tspan> e²/(mε₀ω₀²)</text></svg><figcaption><strong>Two mechanical models, two material constants.</strong> Left: a free carrier random-walks between collisions; with a field on, each flight is bent a little in the direction of q<b>E</b> and the walk drifts at a mean velocity set by the balance between q<b>E</b> and the collisional drag −m<b>v</b>/τ. Summing Nq<b>v</b> over the carriers gives Ohm's law with σ = Nq²τ/m. Right: a bound electron sits on a spring of natural frequency ω₀; a DC field stretches the spring until −e<b>E</b> balances −mω₀²<b>r</b>, producing a dipole moment along <b>E</b>. N<sub>d</sub> such dipoles per unit volume make the polarization <b>P</b> = ε₀χ<sub>e</sub><b>E</b>. The same spring, driven at ω, gives the frequency dependence of ε that Unit 3 needs.</figcaption></figure>

Everything in this lecture follows from $m\,d\mathbf{v}/dt = \sum\mathbf{F}$ for a single charge, averaged over many of them. What distinguishes a conductor from a dielectric is only *which forces* act on its charges:

| | free carrier (metal, electrolyte, plasma) | bound electron (dielectric) |
|---|---|---|
| driving force | $q\mathbf{E}$ | $-e\mathbf{E}$ |
| restoring force | none — the carrier wanders | $-m\omega_0^2\mathbf{r}$ (the spring of the atom) |
| dissipation | collisions, $-m\mathbf{v}/\tau$ | radiation and collisions, $-2m\alpha\,\dot{\mathbf{r}}$ |
| DC response | steady **velocity** $\Rightarrow$ current | steady **displacement** $\Rightarrow$ polarization |
| material constant | $\sigma$ [S/m] | $\chi_e$, $\epsilon = (1+\chi_e)\epsilon_0$ |

The macroscopic velocity $\mathbf{v}$ here is an *average*: each carrier's true velocity is $\mathbf{v}+\delta\mathbf{v}$ with a zero-mean random part $\delta\mathbf{v}$ that is huge (thermal speeds $\sim10^5$ m/s in copper) but averages away. Only the tiny coherent drift (a fraction of a millimetre per second for a household current) carries the current.

## 2. Free carriers: the Drude model and Ohm's law

A carrier of charge $q$ and mass $m$ in a field $\mathbf{E}$, subject to a friction force that represents collisions with the lattice at an average rate $\nu = 1/\tau$ per second:

> [!key] Drude equation of motion
> $$
> m\frac{d\mathbf{v}}{dt} = q\mathbf{E} - m\frac{\mathbf{v}}{\tau}.
> $$
> With $\mathbf{E} = 0$ the velocity decays, $\mathbf{v}(t) = \mathbf{v}(0)e^{-t/\tau}$: left alone, a conductor with uniform carrier density carries no current. With a constant $\mathbf{E}$ the steady state ($d\mathbf{v}/dt = 0$) is
> $$
> \mathbf{v} = \frac{q\tau}{m}\mathbf{E},\qquad\Big|\frac{q\tau}{m}\Big| = \text{the mobility}\ [\text{m}^2/(\text{V·s})].
> $$

**From velocity to current.** Picture a cube of unit volume with $N$ carriers moving at speed $v$ toward one face. In one second every carrier within a distance $v$ of that face crosses it, so the charge crossing per unit area per second is $Nqv$:

> [!key] Current density and conductivity
> $$
> \begin{gathered}
> \mathbf{J} = Nq\mathbf{v} = \frac{Nq^2\tau}{m}\mathbf{E} = \frac{Nq^2}{m\nu}\mathbf{E}\quad[\text{A/m}^2],\\[4pt]
> \text{so}\qquad \mathbf{J} = \sigma\mathbf{E},\quad\boxed{\ \sigma = \sum_s\frac{N_sq_s^2}{m_s\nu_s}\ }.
> \end{gathered}
> $$
> The sum is over carrier species $s$ (electrons, holes, ions) when a material has several. Each contributes positively — $q_s$ enters squared — so negative carriers conduct just as well as positive ones, in the *same* direction of $\mathbf{J}$.

This is the Ohm's law that Lecture 8 postulated, with the proviso it gave there ("provided the carriers suffer occasional collisions") now visible as the $\tau$ in the numerator: no collisions, no steady state, no $\sigma$.

> [!example] Example — copper
> $N\approx8.5\times10^{28}$ m⁻³ (one free electron per atom), $\sigma = 5.96\times10^7$ S/m. Solving for the collision time: $\tau = \sigma m_e/(Ne^2)\approx2.5\times10^{-14}$ s, i.e. $\nu\approx4\times10^{13}$ collisions per second. The mobility is $e\tau/m_e\approx4.4\times10^{-3}$ m²/(V·s). A 1 A current in a 1 mm² wire has $J = 10^6$ A/m², needs only $E = J/\sigma\approx0.017$ V/m to drive it, and drifts at $v = J/(Ne)\approx7\times10^{-5}$ m/s — a tenth of a millimetre per second. The electrons do not race down the wire; the *field* does, at essentially $c$.

The notes' table of DC conductivities (silver, copper, gold $\sim$ several $\times10^7$ S/m; sea water 4; intrinsic silicon $1.6\times10^{-3}$; dry earth $\sim10^{-5}$; glass $10^{-10}$–$10^{-14}$) spans twenty orders of magnitude, almost all of it in $N$: a good insulator is simply a material with no free carriers.

> [!trap] Two different τ's
> The Drude $\tau$ (collision time, $\sim10^{-14}$ s) is not the relaxation time $\tau = \epsilon/\sigma$ of Lecture 8 (the time for charge to leave the interior of a conductor, $\sim10^{-19}$ s for copper and microseconds for a poor conductor). Both are called $\tau$ in the course. One sets *how fast carriers respond*; the other, *how fast an excess charge disperses*. Also: superconductivity is the case where the DC *resistivity* vanishes ($\sigma\to\infty$), a correlated-carrier effect outside this model (the notes say "conductivity vanishes" — a slip, listed on the [[0-toolkit/04-errata-in-the-course-materials|errata page]]).

## 3. AC conductivity: when the carriers cannot keep up

For a sinusoidal field use phasors (ECE 210): $\mathbf{E}(t) = \text{Re}\{\tilde{\mathbf{E}}e^{j\omega t}\}$ and likewise for $\mathbf{v}$, $\mathbf{J}$. The time derivative becomes $j\omega$:

$$
mj\omega\tilde{\mathbf{v}} = q\tilde{\mathbf{E}} - m\frac{\tilde{\mathbf{v}}}{\tau}\quad\Rightarrow\quad\tilde{\mathbf{v}} = \frac{q\tilde{\mathbf{E}}}{m(\nu + j\omega)},
$$

> [!key] AC conductivity
> $$
> \tilde{\mathbf{J}} = \sigma\tilde{\mathbf{E}},\qquad \sigma(\omega) = \sum_s\frac{N_sq_s^2}{m_s(\nu_s + j\omega)} = \frac{\sigma_{\text{DC}}}{1 + j\omega/\nu}\ (\text{one species}).
> $$
> For $\omega\ll\nu$ this is the DC value: the carriers reach their drift velocity long before the field reverses. For copper $\nu\sim4\times10^{13}$ s⁻¹, so the DC conductivity is excellent through the entire radio and microwave range (at 1 GHz the correction is $1.6\times10^{-4}$). The complex part — current lagging the field — matters only in the infrared and beyond, and in plasmas where $\nu$ can be tiny.

Quantum mechanics changes nothing in the form of these results; it replaces $m_s$ by an *effective mass*. That is why the classical model survived.

## 4. Bound electrons: the Lorentz oscillator and χe

In a perfect dielectric there are no free carriers, so $\sigma = 0$ — but the atoms can be polarized. Model each atom as a nucleus with an electron displaced from it by $\mathbf{r}$, forming a dipole $\mathbf{p} = -e\mathbf{r}$ (the dipole points from the electron to the nucleus, i.e. *along* $\mathbf{E}$, since the electron is pulled against the field). Three forces act on the electron: the applied field, a spring-like binding force, and a damping force:

> [!key] Lorentz equation of motion
> $$
> m\frac{d^2\mathbf{r}}{dt^2} = -e\mathbf{E} - m\omega_0^2\mathbf{r} - 2m\alpha\frac{d\mathbf{r}}{dt}.
> $$
> Left alone, the atom rings down as $\mathbf{r}(t)\approx\mathbf{r}_0e^{-\alpha t}\cos\omega_0t$ — the zero-input response of a second-order system, strongly underdamped ($\omega_0\gg\alpha$). The natural frequency $\omega_0$ comes from the atom's bound-state energy levels (optical and ultraviolet frequencies, $10^{15}$–$10^{16}$ rad/s); the damping rate $\alpha$ is read off the width $2\alpha$ of the atom's spectral lines.

**DC response.** With a constant $\mathbf{E}$ the steady state is $\mathbf{r} = -\dfrac{e}{m\omega_0^2}\mathbf{E}$, hence

$$
\mathbf{p} = -e\mathbf{r} = \frac{e^2}{m\omega_0^2}\mathbf{E},\qquad
\mathbf{P} = N_d\mathbf{p} = \frac{N_de^2}{m\omega_0^2}\mathbf{E}\equiv\epsilon_0\chi_e\mathbf{E},
$$

> [!key] DC susceptibility
> $$
> \chi_e = \frac{N_de^2/(m\epsilon_0)}{\omega_0^2},\qquad \epsilon_r = 1+\chi_e.
> $$
> Stiffer springs (larger $\omega_0$) and sparser atoms (smaller $N_d$) give a smaller $\chi_e$. With $N_d\sim5\times10^{28}$ m⁻³ and $\omega_0\sim2\pi\times3\times10^{15}$ rad/s one gets $\chi_e\approx0.45$ — glass-like.

**AC response (an extension, not in the notes).** The phasor version of the equation gives

$$
\chi_e(\omega) = \frac{N_de^2/(m\epsilon_0)}{\omega_0^2 - \omega^2 + 2j\alpha\omega},
$$

which reduces to the DC value for $\omega\ll\omega_0$ — the regime of all of ECE 329, where "$\epsilon$ is a constant" — but grows, peaks and turns complex near $\omega_0$. That is dispersion (ε depends on frequency, hence prisms and chromatic aberration) and absorption (the imaginary part, hence why glass is opaque in the ultraviolet). Unit 3 will meet complex permittivities from the conductivity side; this is the dielectric side of the same coin.

## 5. Polarization current: bound charges that carry an AC current

Now let $\mathbf{E}$ vary in time, slowly compared with $\omega_0$ so that $\mathbf{r} = -\dfrac{e}{m\omega_0^2}\mathbf{E}$ tracks the field. The bound electrons then *move*: $\mathbf{v} = d\mathbf{r}/dt = -\dfrac{e}{m\omega_0^2}\dfrac{d\mathbf{E}}{dt}$, and $N_d$ of them per unit volume, each carrying $-e$, make a current density

> [!key] Polarization current density
> $$
> \mathbf{J}_p = -eN_d\mathbf{v} = \frac{N_de^2}{m\omega_0^2}\frac{\partial\mathbf{E}}{\partial t} = \frac{\partial\mathbf{P}}{\partial t}\quad[\text{A/m}^2].
> $$
> A perfect dielectric cannot carry a DC current — the springs stop the electrons — but it carries an AC current whenever its polarization changes. Nothing is conducted; the charges just slosh.

Where this goes. The *total* current density in a material under a time-varying field is the conduction current of the free carriers plus the polarization current of the bound ones, $\sigma\mathbf{E} + \partial\mathbf{P}/\partial t$. Lecture 16 will show that Ampère's law must contain, in addition to $\mathbf{J} = \sigma\mathbf{E}$, the term

$$
\frac{\partial\mathbf{D}}{\partial t} = \epsilon_0\frac{\partial\mathbf{E}}{\partial t} + \frac{\partial\mathbf{P}}{\partial t}:
$$

the polarization current of this lecture, plus a vacuum term that has no charges behind it at all. The lossy capacitor of [[1-electrostatics/10-capacitance-and-conductance#6-conductance-the-leaky-capacitor|Lecture 10]] already contained both: its conductance $G$ carries the free carriers' $\sigma\mathbf{E}$ and its capacitance $C$ carries the bound carriers' $\partial\mathbf{D}/\partial t$ — which is why $I = GV + C\,dV/dt$.

## 6. What drives the current in a wire? (a footnote worth a section)

[[1-electrostatics/08-conductors-dielectrics-and-polarization|Lecture 8]] established that $\mathbf{E} = 0$ inside a conductor *in equilibrium*. This lecture needs $\mathbf{E} = \mathbf{J}/\sigma\neq0$ inside a wire *carrying a current*. Both are true, and the notes' footnote (citing Jefimenko 1962 and Parker 1970 in *Am. J. Phys.*) tells you how: the field inside a resistive wire is an **electrostatic field produced by surface charges on the wire itself**, distributed along its length with a gradient — denser near one terminal, sparser near the other. These charges arrange themselves, on the relaxation time scale of Lecture 8, so that $\mathbf{E}$ inside follows every bend of the wire and has exactly the magnitude $J/\sigma$. Outside the wire the same charges make a field with a large radial component (the demonstrations show it with suspended fibres, like iron filings for a magnetic field). An ideal zero-resistivity wire needs no such field and carries no such charge — which is the idealization Lecture 12 starts from when it says a current-carrying wire is neutral.

## 7. Summary

- One law of motion, $m\,d\mathbf{v}/dt = \sum\mathbf{F}$, averaged over carriers.
- Free carriers: $\mathbf{v} = (q\tau/m)\mathbf{E}$, $\mathbf{J} = Nq\mathbf{v}$, $\sigma = \sum_sN_sq_s^2/(m_s\nu_s)$; AC: $\nu\to\nu + j\omega$, DC value valid for $\omega\ll\nu\sim10^{13}$ s⁻¹.
- Bound electrons: $m\ddot{\mathbf{r}} = -e\mathbf{E} - m\omega_0^2\mathbf{r} - 2m\alpha\dot{\mathbf{r}}$; DC $\chi_e = N_de^2/(m\epsilon_0\omega_0^2)$; AC $\chi_e(\omega)$ complex near $\omega_0$.
- Polarization current $\mathbf{J}_p = \partial\mathbf{P}/\partial t$; total $\sigma\mathbf{E} + \partial\mathbf{D}/\partial t$ is what Ampère's law will need.
- The field in a current-carrying wire is made by surface charges on the wire.

Concept page: [[concepts/conductivity-and-susceptibility-models]] · related: [[concepts/conductors]] · [[concepts/polarization]] · [[concepts/permittivity]].

> [!exam] On exams
> Not on Exam 1. The testable content is small and conceptual: derive the drift velocity from the force balance, recognize $\mathbf{J} = Nq\mathbf{v}$, know that $\sigma\propto Nq^2\tau/m$ and why the DC value is fine at radio frequencies, and know that $\partial\mathbf{P}/\partial t$ is a current. If a question gives $N$, $q$, $m$, $\tau$ and asks for $\sigma$ or the mobility, it is this lecture.

> [!tip] Practice this lecture
> [[practice/11-lorentz-drude-models|8 practice problems]] — 4 easy, 2 medium, 2 hard — each with a folded hint and a worked solution. Start with [[practice/11-lorentz-drude-models#111-drift-speed-in-a-house-wire|11.1 Drift speed in a house wire]]; the [[practice/index|practice hub]] has the whole bank by difficulty and by topic.

### Sources for this page
Kudeki notes, Lecture 11 (Drude force balance, decay, mobility, unit-cube derivation of $\mathbf{J} = Nq\mathbf{v}$, species sum, phasor AC conductivity and its validity, conductivity table, Lorentz oscillator, zero-input response, DC susceptibility, polarization current, the closing remark on $\sigma\mathbf{E} + d\mathbf{P}/dt$); Lecture 12 footnote 2 and the Jefimenko (1962) and Parker (1970) papers it cites (surface charges on current-carrying wires). The copper numbers and the AC susceptibility formula are extensions, checked against the notes' DC limits.
