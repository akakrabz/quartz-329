---
title: "Lorentz–Drude models of σ and χe"
description: "Newton's law for one charge explains both constants: drifting free carriers give σ = Nq²τ/m (complex at high frequency); bound electrons on springs give χe = Nde²/(mε₀ω₀²) and a polarization current ∂P/∂t."
tags: [concept, electrostatics]
aliases: ["Drude model", "Lorentz oscillator", "mobility", "AC conductivity", "polarization current", "collision time", "drift velocity"]
---

> [!key] The two models
> Free carrier (Drude): $m\,\dot{\mathbf{v}} = q\mathbf{E} - m\mathbf{v}/\tau$ ⟹ $\mathbf{v} = (q\tau/m)\mathbf{E}$, $\mathbf{J} = Nq\mathbf{v} = \sigma\mathbf{E}$,
> $$
> \sigma = \sum_s\frac{N_sq_s^2}{m_s\nu_s}\ (\nu = 1/\tau),\qquad \sigma(\omega) = \sum_s\frac{N_sq_s^2}{m_s(\nu_s+j\omega)} .
> $$
> Bound electron (Lorentz): $m\,\ddot{\mathbf{r}} = -e\mathbf{E} - m\omega_0^2\mathbf{r} - 2m\alpha\,\dot{\mathbf{r}}$ ⟹ $\mathbf{p} = -e\mathbf{r} = \dfrac{e^2}{m\omega_0^2}\mathbf{E}$,
> $$
> \mathbf{P} = N_d\mathbf{p} = \epsilon_0\chi_e\mathbf{E},\qquad \chi_e = \frac{N_de^2/(m\epsilon_0)}{\omega_0^2},\qquad \mathbf{J}_p = \frac{\partial\mathbf{P}}{\partial t}.
> $$

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 290" width="640" height="290" role="img" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:14px"><defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="context-stroke"/></marker><marker id="ahs" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="context-stroke"/></marker></defs><text x="160.0" y="30.0" text-anchor="middle" fill="var(--accent)" style="font-size:13px;font-weight:600;">free carrier (Drude): collisions + drift</text><path d="M73.6,170.1 L102.2,187.2 L114.8,149.5 L145.5,170.1 L113.9,174.3 L110.9,143.4 L81.0,167.8 L44.8,184.6 L41.3,138.0" fill="none" stroke="currentColor" stroke-width="1.3" stroke-dasharray="4 3" opacity="0.7" stroke-linejoin="round" stroke-linecap="round"/><circle cx="73.6" cy="170.1" r="6.0" fill="var(--hi)" stroke="none" stroke-width="1.5"/><line x1="68.6" y1="170.1" x2="78.6" y2="170.1" stroke="white" stroke-width="2.2" stroke-linecap="round"/><line x1="73.6" y1="165.1" x2="73.6" y2="175.1" stroke="white" stroke-width="2.2" stroke-linecap="round"/><text x="90.0" y="100.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px;">E = 0: no net drift</text><path d="M201.6,170.1 L243.2,187.2 L268.8,149.5 L312.5,170.1 L293.9,174.3 L303.9,143.4 L287.0,167.8 L263.8,184.6 L273.3,138.0" fill="none" stroke="var(--accent)" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round"/><circle cx="201.6" cy="170.1" r="6.0" fill="var(--hi)" stroke="none" stroke-width="1.5"/><line x1="196.6" y1="170.1" x2="206.6" y2="170.1" stroke="white" stroke-width="2.2" stroke-linecap="round"/><line x1="201.6" y1="165.1" x2="201.6" y2="175.1" stroke="white" stroke-width="2.2" stroke-linecap="round"/><line x1="269.3" y1="138.0" x2="295.3" y2="138.0" stroke="var(--accent)" stroke-width="2.2" marker-end="url(#ah)" stroke-linecap="round"/><text x="252.0" y="100.0" text-anchor="middle" fill="var(--accent)" style="font-size:11px;">E on: mean drift v = (qτ/m)E</text><line x1="100.0" y1="245.0" x2="260.0" y2="245.0" stroke="var(--hi)" stroke-width="2.4" marker-end="url(#ah)" stroke-linecap="round"/><text x="180.0" y="263.0" text-anchor="middle" fill="var(--hi)" style="font-size:15px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;font-weight:600;">E</text><text x="180.0" y="220.0" text-anchor="middle" fill="currentColor" style="font-size:12.5px;font-weight:600;">J = Nqv = σE,   σ = Nq²τ/m</text><text x="500.0" y="30.0" text-anchor="middle" fill="var(--accent2)" style="font-size:13px;font-weight:600;">bound electron (Lorentz): a spring</text><rect x="390.0" y="80.0" width="230.0" height="150.0" rx="70" fill="var(--accent2)" fill-opacity="0.08" stroke="none"/><circle cx="520.0" cy="150.0" r="12.0" fill="var(--accent2)" stroke="none" stroke-width="1.5"/><line x1="515.0" y1="150.0" x2="525.0" y2="150.0" stroke="white" stroke-width="2.2" stroke-linecap="round"/><line x1="520.0" y1="145.0" x2="520.0" y2="155.0" stroke="white" stroke-width="2.2" stroke-linecap="round"/><text x="520.0" y="180.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px;">nucleus</text><path d="M508.0,150.0 L503.1,157.0 L493.4,143.0 L483.7,157.0 L474.0,143.0 L464.3,157.0 L454.6,143.0 L444.9,157.0 L446.0,150.0" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linejoin="round" stroke-linecap="round"/><circle cx="440.0" cy="150.0" r="8.0" fill="var(--hi)" stroke="none" stroke-width="1.5"/><line x1="435.0" y1="150.0" x2="445.0" y2="150.0" stroke="white" stroke-width="2.2" stroke-linecap="round"/><text x="440.0" y="132.0" text-anchor="middle" fill="var(--hi)" style="font-size:12px;">−e</text><line x1="520.0" y1="110.0" x2="440.0" y2="110.0" stroke="currentColor" stroke-width="1.6" marker-end="url(#ahs)" stroke-linecap="round"/><text x="480.0" y="104.0" text-anchor="middle" fill="currentColor" style="font-size:14px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">r</text><line x1="550.0" y1="110.0" x2="605.0" y2="110.0" stroke="var(--hi)" stroke-width="2.2" marker-end="url(#ah)" stroke-linecap="round"/><text x="578.0" y="104.0" text-anchor="middle" fill="var(--hi)" style="font-size:14px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;font-weight:600;">E</text><line x1="550.0" y1="205.0" x2="605.0" y2="205.0" stroke="var(--accent2)" stroke-width="2.2" marker-end="url(#ah)" stroke-linecap="round"/><text x="578.0" y="222.0" text-anchor="middle" fill="var(--accent2)" style="font-size:12px;font-weight:600;">p = −e r  ∥ E</text><text x="500.0" y="260.0" text-anchor="middle" fill="currentColor" style="font-size:12.5px;font-weight:600;">m r″ = −eE − mω₀²r − 2mα r′</text><text x="500.0" y="278.0" text-anchor="middle" fill="currentColor" style="font-size:11.5px;">DC:  P = N<tspan baseline-shift="sub" style="font-size:9px">d</tspan> p = ε₀χₑE,   χₑ = N<tspan baseline-shift="sub" style="font-size:9px">d</tspan> e²/(mε₀ω₀²)</text></svg><figcaption><strong>Two mechanical models, two material constants.</strong> Left: a free carrier random-walks between collisions; with a field on, each flight is bent a little in the direction of q<b>E</b> and the walk drifts at a mean velocity set by the balance between q<b>E</b> and the collisional drag −m<b>v</b>/τ. Summing Nq<b>v</b> over the carriers gives Ohm's law with σ = Nq²τ/m. Right: a bound electron sits on a spring of natural frequency ω₀; a DC field stretches the spring until −e<b>E</b> balances −mω₀²<b>r</b>, producing a dipole moment along <b>E</b>. N<sub>d</sub> such dipoles per unit volume make the polarization <b>P</b> = ε₀χ<sub>e</sub><b>E</b>. The same spring, driven at ω, gives the frequency dependence of ε that Unit 3 needs.</figcaption></figure>

**Physics.** Unit 1 used two material constants without explaining them: $\sigma$ in $\mathbf{J} = \sigma\mathbf{E}$ ([[concepts/conductors|Conductors in electrostatics]]) and $\chi_e$ in $\mathbf{P} = \epsilon_0\chi_e\mathbf{E}$ ([[concepts/permittivity|Permittivity, susceptibility, and D = εE]]). Everything follows from $m\,d\mathbf{v}/dt = \sum\mathbf{F}$ for a single charge, averaged over many. Conductor and dielectric differ only in *which forces* act:

| | free carrier (metal, electrolyte, plasma) | bound electron (dielectric) |
|---|---|---|
| driving force | $q\mathbf{E}$ | $-e\mathbf{E}$ |
| restoring force | none — the carrier wanders | $-m\omega_0^2\mathbf{r}$ (the spring of the atom) |
| dissipation | collisions, $-m\mathbf{v}/\tau$ | radiation and collisions, $-2m\alpha\,\dot{\mathbf{r}}$ |
| DC response | steady **velocity** $\Rightarrow$ current | steady **displacement** $\Rightarrow$ polarization |
| material constant | $\sigma$ [S/m] | $\chi_e$, $\epsilon = (1+\chi_e)\epsilon_0$ |

$\mathbf{v}$ is an *average*: each carrier's velocity is $\mathbf{v}+\delta\mathbf{v}$ with a zero-mean random part that is huge (thermal speeds $\sim10^5$ m/s in copper) but averages away. Only the tiny coherent drift (a fraction of a millimetre per second for a household current) carries current. Quantum mechanics keeps the form of these results, replacing $m_s$ by an *effective mass* — why the classical model survived.

**Free carriers: Drude and Ohm's law.** A carrier of charge $q$ and mass $m$ in $\mathbf{E}$, with a friction force representing collisions at average rate $\nu = 1/\tau$:

$$
m\frac{d\mathbf{v}}{dt} = q\mathbf{E} - m\frac{\mathbf{v}}{\tau}.
$$

With $\mathbf{E} = 0$, $\mathbf{v}(t) = \mathbf{v}(0)e^{-t/\tau}$: left alone, a conductor with uniform carrier density carries no current. With constant $\mathbf{E}$ the steady state ($d\mathbf{v}/dt = 0$) is

$$
\mathbf{v} = \frac{q\tau}{m}\mathbf{E},\qquad\Big|\frac{q\tau}{m}\Big| = \text{the mobility}\ [\text{m}^2/(\text{V·s})].
$$

*From velocity to current.* In a unit cube with $N$ carriers moving at $v$ toward one face, every carrier within distance $v$ of the face crosses it in one second: charge per unit area per second $Nqv$.

$$
\begin{gathered}
\mathbf{J} = Nq\mathbf{v} = \frac{Nq^2\tau}{m}\mathbf{E} = \frac{Nq^2}{m\nu}\mathbf{E}\quad[\text{A/m}^2],\\[4pt]
\text{so}\qquad \mathbf{J} = \sigma\mathbf{E},\quad\boxed{\ \sigma = \sum_s\frac{N_sq_s^2}{m_s\nu_s}\ }.
\end{gathered}
$$

The sum runs over carrier species $s$ (electrons, holes, ions). $q_s$ enters squared, so negative carriers conduct as well as positive ones, in the *same* direction of $\mathbf{J}$. This is the postulated Ohm's law; its proviso ("provided the carriers suffer occasional collisions") is the $\tau$ in the numerator: no collisions, no steady state, no $\sigma$. The notes' table of DC conductivities (silver, copper, gold $\sim$ several $\times10^7$ S/m; sea water 4; intrinsic silicon $1.6\times10^{-3}$; dry earth $\sim10^{-5}$; glass $10^{-10}$–$10^{-14}$) spans twenty orders of magnitude, almost all of it in $N$: a good insulator has no free carriers.

> [!derivation]- AC conductivity: when the carriers cannot keep up
> With phasors (ECE 210), $\mathbf{E}(t) = \text{Re}\{\tilde{\mathbf{E}}e^{j\omega t}\}$ and likewise $\mathbf{v}$, $\mathbf{J}$; $d/dt\to j\omega$:
> $$
> mj\omega\tilde{\mathbf{v}} = q\tilde{\mathbf{E}} - m\frac{\tilde{\mathbf{v}}}{\tau}\quad\Rightarrow\quad\tilde{\mathbf{v}} = \frac{q\tilde{\mathbf{E}}}{m(\nu + j\omega)},
> $$
> $$
> \tilde{\mathbf{J}} = \sigma\tilde{\mathbf{E}},\qquad \sigma(\omega) = \sum_s\frac{N_sq_s^2}{m_s(\nu_s + j\omega)} = \frac{\sigma_{\text{DC}}}{1 + j\omega/\nu}\ (\text{one species}).
> $$
> For $\omega\ll\nu$ this is the DC value: the carriers reach their drift velocity long before the field reverses. For copper $\nu\sim4\times10^{13}$ s⁻¹, so DC conductivity holds through the radio and microwave range (at 1 GHz the correction is $1.6\times10^{-4}$). The complex part — current lagging the field — matters only in the infrared and beyond, and in plasmas where $\nu$ can be tiny.

**When the conductivity depends on frequency (waves; Lecture 22 §8).** The one-species Drude conductivity of the derivation above feeds the wave formulas:

$$
\sigma(\omega) = \frac{Nq^2}{m(\nu + j\omega)} = \frac{\sigma_{\text{DC}}}{1 + j\omega/\nu} .
$$

The [[concepts/propagation-constant|propagation constant]] and [[concepts/intrinsic-impedance|intrinsic impedance]] still follow from $\sigma(\omega) + j\omega\epsilon$, but $\text{Re}\{\gamma/\eta\}$ and $\text{Im}\{\gamma/\eta\}/\omega$ give only *effective* $\sigma$, $\epsilon$: an imaginary part of $\sigma$ looks exactly like a change in $\epsilon$.

- **Metals.** Real $\sigma$ is safe at every radio and microwave frequency (copper's $1.6\times10^{-4}$ correction at 1 GHz, above).
- **A collisionless plasma** ($\nu\to0$, the ionosphere). $\sigma = Nq^2/(j\omega m)$ is imaginary; the current lags the field by 90° (inertia) and partly cancels the displacement current,

$$
\sigma + j\omega\epsilon_0 = j\omega\epsilon_0\Big(1 - \frac{\omega_p^2}{\omega^2}\Big),\qquad \omega_p^2 = \frac{Nq^2}{m\epsilon_0},
$$

so $\gamma^2 = -(\omega^2 - \omega_p^2)/c^2$.
  - **Above $\omega_p$:** $\gamma = j\sqrt{\omega^2 - \omega_p^2}/c$, no attenuation: the plasma [[concepts/dispersion-relation|dispersion relation]] in one line. $\eta = \omega\mu_0/\beta$ is real, above $\eta_0$.
  - **Below it:** $\gamma = \sqrt{\omega_p^2 - \omega^2}/c$ is real: decay without spatial oscillation (*evanescent*). $\eta$ is imaginary, so $\mathbf{E}$, $\mathbf{H}$ are 90° apart, carrying no average power ([[concepts/time-average-power|Time averages and average power]]). Not loss ($\text{Re}\{\sigma\} = 0$): the plasma reflects ([[concepts/reflection-and-transmission|Reflection and transmission coefficients]]).
- $N = 10^{12}$ m⁻³ (daytime ionospheric peak): $f_p\approx9$ MHz ($f_p\approx9\sqrt N$ Hz). At 5 MHz, $\delta = 6.4$ m; at 20 MHz, $\beta = 0.375$ rad/m against vacuum's 0.419 rad/m.
- Only $\text{Re}\{\sigma\}$ heats: $\langle\mathbf{J}\cdot\mathbf{E}\rangle = \tfrac12\text{Re}\{\sigma\}\lvert\tilde{\mathbf{E}}\rvert^2$; with collisions $\text{Re}\{\sigma_{\text{DC}}/(1 + j\omega/\nu)\} = \sigma_{\text{DC}}/(1 + \omega^2/\nu^2)$.

**Bound electrons: the Lorentz oscillator.** A perfect dielectric has no free carriers ($\sigma = 0$), but its atoms polarize. Model each atom as a nucleus with an electron displaced by $\mathbf{r}$: dipole $\mathbf{p} = -e\mathbf{r}$, pointing from electron to nucleus, i.e. *along* $\mathbf{E}$. Three forces act on the electron — applied field, spring-like binding, damping:

$$
m\frac{d^2\mathbf{r}}{dt^2} = -e\mathbf{E} - m\omega_0^2\mathbf{r} - 2m\alpha\frac{d\mathbf{r}}{dt}.
$$

Left alone, the atom rings down as $\mathbf{r}(t)\approx\mathbf{r}_0e^{-\alpha t}\cos\omega_0t$ — the zero-input response of a strongly underdamped ($\omega_0\gg\alpha$) second-order system. $\omega_0$ comes from the atom's energy levels (optical and ultraviolet, $10^{15}$–$10^{16}$ rad/s); $\alpha$ from the width $2\alpha$ of its spectral lines. *DC response:* with constant $\mathbf{E}$ the steady state is $\mathbf{r} = -\dfrac{e}{m\omega_0^2}\mathbf{E}$, hence

$$
\mathbf{p} = -e\mathbf{r} = \frac{e^2}{m\omega_0^2}\mathbf{E},\qquad
\mathbf{P} = N_d\mathbf{p} = \frac{N_de^2}{m\omega_0^2}\mathbf{E}\equiv\epsilon_0\chi_e\mathbf{E},
$$

$$
\chi_e = \frac{N_de^2/(m\epsilon_0)}{\omega_0^2},\qquad \epsilon_r = 1+\chi_e.
$$

Stiffer springs (larger $\omega_0$) and sparser atoms (smaller $N_d$) give smaller $\chi_e$.

> [!derivation]- AC susceptibility (an extension, not in the notes)
> The phasor equation gives
> $$
> \chi_e(\omega) = \frac{N_de^2/(m\epsilon_0)}{\omega_0^2 - \omega^2 + 2j\alpha\omega},
> $$
> the DC value for $\omega\ll\omega_0$ — all of ECE 329, where "$\epsilon$ is a constant" — but growing, peaking and turning complex near $\omega_0$: dispersion (prisms, chromatic aberration) and absorption (the imaginary part; glass is opaque in the ultraviolet). Unit 3 meets complex permittivities from the conductivity side; this is the dielectric side.

**Polarization current.** Let $\mathbf{E}$ vary slowly compared with $\omega_0$, so $\mathbf{r} = -\dfrac{e}{m\omega_0^2}\mathbf{E}$ tracks the field. The bound electrons *move*, $\mathbf{v} = d\mathbf{r}/dt = -\dfrac{e}{m\omega_0^2}\dfrac{d\mathbf{E}}{dt}$, and $N_d$ of them per unit volume, each carrying $-e$, give

$$
\mathbf{J}_p = -eN_d\mathbf{v} = \frac{N_de^2}{m\omega_0^2}\frac{\partial\mathbf{E}}{\partial t} = \frac{\partial\mathbf{P}}{\partial t}\quad[\text{A/m}^2].
$$

A perfect dielectric carries no DC current — the springs stop the electrons — but carries an AC current whenever its polarization changes. Nothing is conducted; the charges slosh. The *total* current density under a time-varying field is free-carrier conduction plus bound-charge polarization current, $\sigma\mathbf{E} + \partial\mathbf{P}/\partial t$. Ampère's law needs, besides $\mathbf{J} = \sigma\mathbf{E}$,

$$
\frac{\partial\mathbf{D}}{\partial t} = \epsilon_0\frac{\partial\mathbf{E}}{\partial t} + \frac{\partial\mathbf{P}}{\partial t}:
$$

this polarization current plus a vacuum term with no charges behind it — the [[concepts/displacement-current|Displacement current]] of [[3-maxwell-and-waves/16-charge-conservation-displacement-current-and-maxwells-equations|Lecture 16]]. The leaky capacitor of [[concepts/conductance|Conductance and the leaky capacitor]] already had both: $G$ carries $\sigma\mathbf{E}$, $C$ carries $\partial\mathbf{D}/\partial t$ — hence $I = GV + C\,dV/dt$.

**At high frequency, in waves.** In a wave the two constants compete: free carriers carry the conduction current $\sigma\tilde{\mathbf{E}}$, vacuum and bound charges the displacement current $j\omega\epsilon\tilde{\mathbf{E}}$. Their ratio $\sigma/\omega\epsilon$, the [[concepts/loss-tangent|loss tangent]], equals 1 at $f_c = \sigma/2\pi\epsilon = 1/(2\pi\tau_r)$, $\tau_r = \epsilon/\sigma$ being the relaxation time: 0.89 GHz for seawater, 225 kHz for fresh water. Well below $f_c$ the medium is a good conductor: a wave gets only a [[concepts/skin-depth|skin depth]] $\delta = 1/\sqrt{\pi f\mu\sigma}$ into it (copper: 66 µm at 1 MHz; seawater: 7.96 m at 1 kHz). Well above, it is an imperfect dielectric, weakening the wave little per wavelength ([[3-maxwell-and-waves/23-imperfect-dielectrics-and-good-conductors|Lecture 23]]). Constant $\sigma$ and $\epsilon$ fail where the models stop being flat (above); the Lorentz damping also makes the polarization lag the field and dissipate power as $\sigma$ does, so datasheets quote one loss tangent for both mechanisms.

**Examples.**

> [!example] Example — copper
> $N\approx8.5\times10^{28}$ m⁻³ (one free electron per atom), $\sigma = 5.96\times10^7$ S/m. Collision time $\tau = \sigma m_e/(Ne^2)\approx2.5\times10^{-14}$ s, i.e. $\nu\approx4\times10^{13}$ s⁻¹; mobility $e\tau/m_e\approx4.4\times10^{-3}$ m²/(V·s). A 1 A current in a 1 mm² wire has $J = 10^6$ A/m², needs only $E = J/\sigma\approx0.017$ V/m, and drifts at $v = J/(Ne)\approx7\times10^{-5}$ m/s — a tenth of a millimetre per second. The electrons do not race down the wire; the *field* does, at essentially $c$.

Glass-like dielectric: $N_d\sim5\times10^{28}$ m⁻³ and $\omega_0\sim2\pi\times3\times10^{15}$ rad/s give $\chi_e\approx0.45$.

> [!trap] Two different τ's, and other slips
> - The Drude $\tau$ (collision time, $\sim10^{-14}$ s: how fast carriers respond) is not the relaxation time $\tau = \epsilon/\sigma$ of [[concepts/conductors|Conductors in electrostatics]] (how fast an excess charge leaves a conductor's interior: $\sim10^{-19}$ s for copper, microseconds for a poor conductor). The course calls both $\tau$.
> - Superconductivity is the case where the DC *resistivity* vanishes ($\sigma\to\infty$), a correlated-carrier effect outside this model (slip in the notes: [[0-toolkit/04-errata-in-the-course-materials|errata page]]).
> - $\mathbf{r}$ (electron displacement) is antiparallel to $\mathbf{E}$; $\mathbf{p} = -e\mathbf{r}$ and $\mathbf{P}$ are parallel to it.
> - $\chi_e = (N_de^2/m\epsilon_0)/\omega_0^2$: the fraction bar groups $N_de^2/(m\epsilon_0)$ first.

> [!exam] On exams
> Not on Exam 1. Testable content is small and conceptual: drift velocity from the force balance, $\mathbf{J} = Nq\mathbf{v}$, $\sigma\propto Nq^2\tau/m$ and why the DC value holds at radio frequencies, $\partial\mathbf{P}/\partial t$ is a current. Given $N$, $q$, $m$, $\tau$ and asked for $\sigma$ or the mobility: this page.

**Where it appears.** [[1-electrostatics/11-lorentz-drude-models-for-conductivity-and-susceptibility#1-two-constants-one-law-of-motion|Lecture 11 §1]] (the two models side by side), [[1-electrostatics/11-lorentz-drude-models-for-conductivity-and-susceptibility#2-free-carriers-the-drude-model-and-ohms-law|§2]] (Drude), [[1-electrostatics/11-lorentz-drude-models-for-conductivity-and-susceptibility#3-ac-conductivity-when-the-carriers-cannot-keep-up|§3]] (AC), [[1-electrostatics/11-lorentz-drude-models-for-conductivity-and-susceptibility#4-bound-electrons-the-lorentz-oscillator-and-χe|§4]] (Lorentz), [[1-electrostatics/11-lorentz-drude-models-for-conductivity-and-susceptibility#5-polarization-current-bound-charges-that-carry-an-ac-current|§5]] (polarization current); the constants are introduced in [[1-electrostatics/08-conductors-dielectrics-and-polarization|Lecture 8]] and [[1-electrostatics/09-static-fields-in-dielectric-media|Lecture 9]]; the polarization current returns in [[3-maxwell-and-waves/16-charge-conservation-displacement-current-and-maxwells-equations|Lecture 16]]; [[3-maxwell-and-waves/22-phasor-maxwell-equations-and-damped-waves#8-when-the-conductivity-depends-on-frequency|Lecture 22 §8]] (Drude $\sigma(\omega)$ in $\gamma$, $\eta$; the plasma above and below $\omega_p$); complex $\epsilon$ and $\sigma$ with lossy media in Unit 3.

**Related.** [[concepts/conductors|Conductors in electrostatics]] · [[concepts/polarization|Polarization P and bound charge]] · [[concepts/permittivity|Permittivity, susceptibility, and D = εE]] · [[concepts/conductance|Conductance and the leaky capacitor]] · [[concepts/displacement-current|Displacement current]] · [[concepts/loss-tangent|Loss tangent]] · [[concepts/skin-depth|Skin depth]].

**Practice.** [[practice/topics#drude-and-lorentz-models|Drude and Lorentz models]] (9 problems) — for example [[practice/11-lorentz-drude-models#111-drift-speed-in-a-house-wire|11.1 Drift speed in a house wire]] (easy), [[practice/11-lorentz-drude-models#115-sea-waters-two-ions|11.5 Sea water's two ions]] (medium), [[practice/11-lorentz-drude-models#117-conductor-like-or-dielectric-like|11.7 Conductor-like or dielectric-like]] (hard).
