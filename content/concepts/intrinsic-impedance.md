---
title: "Intrinsic impedance"
description: "η = √(μ/ε) is the ratio |E|/|H| in a single travelling plane wave. In vacuum η₀ = √(μ₀/ε₀) = 376.7 Ω ≈ 120π Ω; in a medium η = η₀√(μr/εr) = μv. η fixes how big H is for a given E. Its direction comes from requiring E × H to point along the travel."
tags: [concept, waves]
aliases: ["wave impedance", "impedance of free space"]
---

> [!key] Definition
> $$
> \eta\equiv\sqrt{\frac{\mu}{\epsilon}} = \mu v = \frac{1}{\epsilon v} = \eta_0\sqrt{\frac{\mu_r}{\epsilon_r}}\ [\Omega],\qquad \eta_0 = \sqrt{\frac{\mu_0}{\epsilon_0}} = 376.7\ \Omega\approx120\pi\ \Omega .
> $$
> For one plane wave travelling along $\hat u$, $\mathbf{H} = \hat u\times\mathbf{E}/\eta$. So $\lvert\mathbf{E}\rvert = \eta\lvert\mathbf{H}\rvert$ and, with $\mathbf{B} = \mu\mathbf{H}$, $\lvert\mathbf{B}\rvert = \lvert\mathbf{E}\rvert/v$. For $\mathbf{E} = \hat xE_x$ travelling along $z$: $E_x/H_y = +\eta$ toward $+z$ and $-\eta$ toward $-z$.

**Physics.** It falls out of either curl equation. For $E_x = f(t - z/v)$, Faraday's law $\partial E_x/\partial z = -\mu\,\partial H_y/\partial t$ gives $H_y = f/(\mu v)$, and $\mu v = \mu/\sqrt{\mu\epsilon} = \sqrt{\mu/\epsilon}$. Ampère's law gives the same through $\epsilon v = 1/\eta$. Units: $\mu/\epsilon$ is (H/m)/(F/m) = H/F = (Ω·s)/(s/Ω) = Ω², so $\eta$ is in ohms. It is an impedance in the circuit sense, a ratio of a volt-like field (V/m) to an ampere-like one (A/m). It is not a resistor, though: in a lossless medium nothing is dissipated, and the energy is carried away (Lecture 20). In a lossless medium $\eta$ is a positive real number; the sign of $\mathbf{H}$ comes from $\hat u\times\mathbf{E}$. On a transmission line the same role is played by $\sqrt{\mathcal{L}/\mathcal{C}}$, which is $\eta$ times a geometric factor: $(\eta/2\pi)\ln(b/a)$ for a coax and $\eta\,d/W$ for parallel plates. In lossy media $\eta$ becomes complex and $\mathbf{E}$, $\mathbf{H}$ fall out of phase (Lectures 22–23). At an interface the two media's $\eta$'s decide how much of a wave reflects (Lecture 25).

**Examples.**
- Vacuum: a 1 V/m wave has $H = 2.65$ mA/m and $B = 3.34$ nT ($= E/c$).
- Non-magnetic dielectrics: $\epsilon_r = 2.25$ gives 251 Ω ($80\pi$); $\epsilon_r = 4$ gives 188 Ω ($60\pi$); $\epsilon_r = 9$ gives 126 Ω ($40\pi$). From a measured speed, $\eta = \mu_0v$: $v = 2\times10^8$ m/s gives $80\pi = 251.3\ \Omega$.
- A magnetic dielectric with $\mu_r = 2$, $\epsilon_r = 8$ has $\eta = \eta_0/2 = 188\ \Omega$, the same as $\epsilon_r = 4$ alone, but half the speed ($c/4$). $\eta$ depends on the *ratio* $\mu_r/\epsilon_r$ and $v$ on the *product*.
- Coax with polyethylene and $b/a = 3.5$: $\sqrt{\mathcal{L}/\mathcal{C}} = 0.199\times251\ \Omega = 50\ \Omega$ ([[problems/coax-inductance-and-the-lc-product]]).
- Worked problem: 6 V/m in polyethylene pairs with $6/251.3 = 23.9$ mA/m, not $6/377 = 15.9$ mA/m.

> [!trap]
> - $\eta$ versus $1/\eta$: $H = E/\eta$, so 1 V/m gives 2.65 *milli*amperes per metre. The notes' $\mathbf{H}$ amplitude $\sqrt{\epsilon/\mu}$ is $1/\eta$.
> - Use the medium's $\eta$, not $\eta_0$: in a non-magnetic dielectric $\eta = \eta_0/\sqrt{\epsilon_r}$.
> - $E_x/H_y = \pm\eta$ holds for one travelling wave. With $E_x = Af + Bg$ and $H_y = (Af - Bg)/\eta$ the ratio is $\eta\,(Af+Bg)/(Af-Bg)$, which can be anything.
> - $120\pi = 376.99\ \Omega$ approximates $376.73\ \Omega$ to 0.07 %. Either is accepted; say which you used.

**Where it appears.** [[3-maxwell-and-waves/18-the-wave-equation-and-plane-tem-waves|Lecture 18]] (defined; the sign table); [[3-maxwell-and-waves/19-dalembert-solutions-and-radiation-from-current-sheets|Lecture 19]] (a current sheet radiates $\lvert\mathbf{E}\rvert = \eta J_s/2$ on each side, because it drives two half-spaces of impedance $\eta$ in parallel; see [[concepts/current-sheet-radiation]]); Lecture 20 (a travelling wave carries $E^2/\eta$ per unit area); Lectures 22–23 (complex $\eta$); Lecture 25 (reflection); Unit 4 ($\sqrt{\mathcal{L}/\mathcal{C}}$); [[problems/a-pulse-on-the-move]].

**Practice.** [[practice/topics#plane-waves-and-the-wave-equation|Plane waves and the wave equation]] (20 problems) — for example [[practice/18-wave-equation-and-plane-waves#181-which-way-and-how-fast|18.1 Which way and how fast]] (easy), [[practice/18-wave-equation-and-plane-waves#186-which-fields-can-be-waves|18.6 Which fields can be waves]] (medium), [[practice/18-wave-equation-and-plane-waves#189-triangle-pulse-in-a-magnetic-medium|18.9 Triangle pulse in a magnetic medium]] (hard).

Related: [[concepts/plane-waves]] · [[concepts/wave-equation]] · [[concepts/permittivity]] · [[concepts/permeability]] · [[concepts/inductance]] · [[concepts/capacitance]].
