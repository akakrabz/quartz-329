---
title: "Lorentz–Drude models of σ and χe"
description: "Newton's law for one charge explains both material constants: free carriers drifting between collisions give σ = Nq²τ/m (complex at high frequency, σ/(1 + jω/ν)); bound electrons on springs give χe = Nde²/(mε₀ω₀²) and, when E varies, a polarization current ∂P/∂t."
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

**Physics.** Both are the steady-state response of a damped mechanical system to a force $q\mathbf{E}$. Without a restoring force the carrier reaches a terminal *velocity* — a current; with one it reaches a terminal *displacement* — a dipole. Collisions at rate $\nu$ are the friction; $|q\tau/m|$ is the mobility. Each species contributes $\propto q_s^2$, so holes and ions add to electrons. In phasors $d/dt\to j\omega$, giving the complex $\sigma(\omega)$ whose DC value is accurate for $\omega\ll\nu$ (copper: $\nu\approx4\times10^{13}$ s⁻¹, so through the microwave range) and the resonant $\chi_e(\omega) = (N_de^2/m\epsilon_0)/(\omega_0^2-\omega^2+2j\alpha\omega)$, flat and real for $\omega\ll\omega_0$ (optical frequencies) — the regime of the whole course. A time-varying field makes the bound electrons move, so a perfect insulator carries the AC *polarization current* $\partial\mathbf{P}/\partial t$; it is the material half of the [[concepts/displacement-current]].

**Examples.** Copper: $N = 8.5\times10^{28}$ m⁻³, $\sigma = 6\times10^7$ S/m ⟹ $\tau = 2.5\times10^{-14}$ s, mobility $4.4\times10^{-3}$ m²/(V·s), drift 0.4 mm/s at 0.1 V/m. Glass-like dielectric: $N_d = 5\times10^{28}$ m⁻³, $\omega_0 = 2\pi\times3\times10^{15}$ rad/s ⟹ $\chi_e\approx0.45$. Conductivities span $10^{-14}$ (glass) to several $\times10^7$ S/m (silver), almost entirely through $N$.

> [!trap]
> - The Drude $\tau$ ($\sim10^{-14}$ s) is not the relaxation time $\epsilon/\sigma$; both are written $\tau$.
> - $\mathbf{r}$ (electron displacement) is antiparallel to $\mathbf{E}$; $\mathbf{p} = -e\mathbf{r}$ and $\mathbf{P}$ are parallel to it. One minus sign, easy to drop.
> - Superconductors have vanishing *resistivity*, not conductivity.
> - $\chi_e = (N_de^2/m\epsilon_0)/\omega_0^2$: the fraction bar groups $N_de^2/(m\epsilon_0)$ first.

**Where it appears.** [[1-electrostatics/11-lorentz-drude-models-for-conductivity-and-susceptibility|Lecture 11]] (all of it); the constants it explains are introduced in [[1-electrostatics/08-conductors-dielectrics-and-polarization|Lecture 8]] and [[1-electrostatics/09-static-fields-in-dielectric-media|Lecture 9]]; the polarization current reappears in [[3-maxwell-and-waves/16-charge-conservation-displacement-current-and-maxwells-equations|Lecture 16]]; complex $\epsilon$ and $\sigma$ return with lossy media in Unit 3.

Related: [[concepts/conductors]] · [[concepts/polarization]] · [[concepts/permittivity]] · [[concepts/conductance]].
