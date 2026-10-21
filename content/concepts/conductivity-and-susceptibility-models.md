---
title: "Lorentz–Drude models of σ and χe"
description: "Newton's law for one charge explains both constants: drifting free carriers give σ = Nq²τ/m (complex at high frequency); bound electrons on springs give χe = Nde²/(mε₀ω₀²) and a polarization current ∂P/∂t."
tags: [concept, electrostatics]
aliases: ["Drude model", "Lorentz oscillator", "mobility", "AC conductivity", "polarization current"]
---

> [!key] Definition
> Free carrier: $m\,\dot{\mathbf{v}} = q\mathbf{E} - m\mathbf{v}/\tau$ ⟹ $\mathbf{v} = (q\tau/m)\mathbf{E}$, $\mathbf{J} = Nq\mathbf{v} = \sigma\mathbf{E}$,
> $$
> \sigma = \sum_s\frac{N_sq_s^2}{m_s\nu_s}\ (\nu = 1/\tau),\qquad \sigma(\omega) = \sum_s\frac{N_sq_s^2}{m_s(\nu_s+j\omega)} .
> $$
> Bound electron: $m\,\ddot{\mathbf{r}} = -e\mathbf{E} - m\omega_0^2\mathbf{r} - 2m\alpha\,\dot{\mathbf{r}}$ ⟹ $\mathbf{p} = -e\mathbf{r} = \dfrac{e^2}{m\omega_0^2}\mathbf{E}$,
> $$
> \mathbf{P} = N_d\mathbf{p} = \epsilon_0\chi_e\mathbf{E},\qquad \chi_e = \frac{N_de^2/(m\epsilon_0)}{\omega_0^2},\qquad \mathbf{J}_p = \frac{\partial\mathbf{P}}{\partial t}.
> $$

**Physics.** Both are the steady-state response of a damped mechanical system to a force $q\mathbf{E}$. Without a restoring force the carrier reaches a terminal *velocity*, a current; with one, a terminal *displacement*, a dipole. Collisions at rate $\nu$ are the friction; $|q\tau/m|$ is the mobility. Each species contributes $\propto q_s^2$, so holes and ions add to electrons. In phasors $d/dt\to j\omega$: the complex $\sigma(\omega)$ keeps its DC value for $\omega\ll\nu$ (copper: $\nu\approx4\times10^{13}$ s⁻¹, through the microwave range), and the resonant $\chi_e(\omega) = (N_de^2/m\epsilon_0)/(\omega_0^2-\omega^2+2j\alpha\omega)$ is flat and real for $\omega\ll\omega_0$ (optical frequencies), true throughout this course. A time-varying field moves the bound electrons, so a perfect insulator carries the AC *polarization current* $\partial\mathbf{P}/\partial t$, the material half of the [[concepts/displacement-current]].

**Examples.** Copper: $N = 8.5\times10^{28}$ m⁻³, $\sigma = 6\times10^7$ S/m ⟹ $\tau = 2.5\times10^{-14}$ s, mobility $4.4\times10^{-3}$ m²/(V·s), drift 0.4 mm/s at 0.1 V/m. Glass-like dielectric: $N_d = 5\times10^{28}$ m⁻³, $\omega_0 = 2\pi\times3\times10^{15}$ rad/s ⟹ $\chi_e\approx0.45$. Conductivities span $10^{-14}$ (glass) to several $\times10^7$ S/m (silver), almost entirely through $N$.

> [!trap]
> - The Drude $\tau$ ($\sim10^{-14}$ s) is not the relaxation time $\epsilon/\sigma$; both are written $\tau$.
> - $\mathbf{r}$ (electron displacement) is antiparallel to $\mathbf{E}$; $\mathbf{p} = -e\mathbf{r}$ and $\mathbf{P}$ are parallel to it.
> - Superconductors have vanishing *resistivity*, not conductivity.
> - $\chi_e = (N_de^2/m\epsilon_0)/\omega_0^2$: the fraction bar groups $N_de^2/(m\epsilon_0)$ first.

**At high frequency, in waves.** In a wave the two constants compete: free carriers carry the conduction current $\sigma\tilde{\mathbf{E}}$, vacuum and bound charges the displacement current $j\omega\epsilon\tilde{\mathbf{E}}$. Their ratio $\sigma/\omega\epsilon$, the [[concepts/loss-tangent|loss tangent]], equals 1 at $f_c = \sigma/2\pi\epsilon = 1/(2\pi\tau_r)$, $\tau_r = \epsilon/\sigma$ being the relaxation time: 0.89 GHz for seawater, 225 kHz for fresh water. Well below $f_c$ the medium is a good conductor: a wave gets only a [[concepts/skin-depth|skin depth]] $\delta = 1/\sqrt{\pi f\mu\sigma}$ into it (copper: 66 µm at 1 MHz; seawater: 7.96 m at 1 kHz). Well above, it is an imperfect dielectric, weakening the wave little per wavelength ([[3-maxwell-and-waves/23-imperfect-dielectrics-and-good-conductors|Lecture 23]]). Constant $\sigma$ and $\epsilon$ fail where the models stop being flat (above); the Lorentz damping also makes the polarization lag the field and dissipate power as $\sigma$ does, so datasheets quote one loss tangent for both mechanisms.

**Where it appears.** [[1-electrostatics/11-lorentz-drude-models-for-conductivity-and-susceptibility|Lecture 11]]; the constants are introduced in [[1-electrostatics/08-conductors-dielectrics-and-polarization|Lecture 8]] and [[1-electrostatics/09-static-fields-in-dielectric-media|Lecture 9]]; the polarization current returns in [[3-maxwell-and-waves/16-charge-conservation-displacement-current-and-maxwells-equations|Lecture 16]], complex $\epsilon$ and $\sigma$ with lossy media in Unit 3.

**Practice.** [[practice/topics#drude-and-lorentz-models|Drude and Lorentz models]] (9 problems) — for example [[practice/11-lorentz-drude-models#111-drift-speed-in-a-house-wire|11.1 Drift speed in a house wire]] (easy), [[practice/11-lorentz-drude-models#115-sea-waters-two-ions|11.5 Sea water's two ions]] (medium), [[practice/11-lorentz-drude-models#117-conductor-like-or-dielectric-like|11.7 Conductor-like or dielectric-like]] (hard).

Related: [[concepts/conductors]] · [[concepts/polarization]] · [[concepts/permittivity]] · [[concepts/conductance]].
