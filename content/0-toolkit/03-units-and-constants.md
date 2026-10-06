---
title: "Units, constants, and the dimension ladder"
description: "The constants the course uses (ε₀, μ₀, c, e), the units of every field and source, and the habit of checking dimensions that saves exam points."
tags: [toolkit, reference]
---

*Toolkit · reference page*

## Constants

| symbol | value | name |
|---|---|---|
| $\epsilon_0$ | $8.854\times10^{-12}\ \text{F/m} \approx \dfrac{1}{36\pi}\times10^{-9}\ \text{F/m}$ | permittivity of free space |
| $\mu_0$ | $4\pi\times10^{-7}\ \text{H/m}$ (exact by the old definition) | permeability of free space |
| $c = 1/\sqrt{\mu_0\epsilon_0}$ | $2.998\times10^{8}\ \text{m/s}\approx 3\times10^{8}$ m/s $=$ 300 m/µs $=$ 30 cm/ns | speed of light (defines the metre) |
| $\dfrac{1}{4\pi\epsilon_0}$ | $\approx 9\times10^{9}\ \text{m/F}$ | Coulomb's constant — the course keeps it in the $4\pi\epsilon_0$ form |
| $\eta_0 = \sqrt{\mu_0/\epsilon_0}$ | $\approx 377\ \Omega \approx 120\pi\ \Omega$ | impedance of free space (from Lecture 18) |
| $e$ | $1.602\times10^{-19}$ C | elementary charge (proton $+e$, electron $-e$) |

Wavelength–frequency: $\lambda f = c$. With $c = 300$ m/µs: 1 MHz ↔ 300 m, 100 MHz ↔ 3 m, 1 GHz ↔ 30 cm, 10 GHz ↔ 3 cm.

## Units of fields and sources

| quantity | unit | equivalent |
|---|---|---|
| $\mathbf{E}$ | V/m | N/C |
| $\mathbf{D}$ | C/m² | |
| $\mathbf{P}$ (polarization) | C/m² | dipole moment per volume |
| $\mathbf{B}$ | T (tesla) | Wb/m² = V·s/m² |
| $\mathbf{H}$ | A/m | |
| $\mathbf{M}$ (magnetization) | A/m | magnetic moment per volume; same unit as $\mathbf{H}$ (Lecture 17) |
| magnetic moment $\mathbf{m} = I\mathbf{A}$ | A·m² | J/T |
| $V$ (potential) | V | J/C |
| flux $\psi_E = \oint\mathbf{D}\cdot d\mathbf{S}$ | C | |
| flux $\psi_B = \int\mathbf{B}\cdot d\mathbf{S}$ | Wb | V·s |
| $\epsilon$ | F/m | C/(V·m) |
| $\mu$ | H/m | V·s/(A·m) |
| $\sigma$ (conductivity) | S/m | (Ω·m)⁻¹ |
| capacitance $C$; per length $\mathcal{C}$ | F; F/m | |
| conductance $G$; per length $\mathcal{G}$ | S; S/m | |
| inductance $L$; per length $\mathcal{L}$ | H (henry) = Wb/A; H/m | V·s/A |
| $\mathbf{A}$ (vector potential) | Wb/m | T·m = V·s/m |
| emf $\mathcal{E} = \oint(\mathbf{E}+\mathbf{v}\times\mathbf{B})\cdot d\mathbf{l}$ | V | |
| MMF $\oint\mathbf{H}\cdot d\mathbf{l}$ | A | |
| surface current $\mathbf{J}_s$ | A/m | same as $\mathbf{H}$: $H_t$ jumps by $J_s$ |
| mobility $\lvert q\tau/m\rvert$ | m²/(V·s) | |
| $\chi_m$, $\mu_r$, $\chi_e$, $\epsilon_r$ | dimensionless | $\mu = \mu_r\mu_0 = (1+\chi_m)\mu_0$ |
| wave speed $v = 1/\sqrt{\mu\epsilon}$ | m/s | $c = 2.998\times10^8$ m/s $\approx 300$ m/µs in vacuum |
| intrinsic impedance $\eta = \sqrt{\mu/\epsilon}$ | Ω | $E/H$ in a plane wave (V/m over A/m) |
| energy density $w$ | J/m³ | $\tfrac12\epsilon E^2$, $\tfrac12\mu H^2$ |

## The dimension ladder of sources

| dimension | charge | current |
|---|---|---|
| point / wire | $Q$ [C] | $I$ [A] |
| line / sheet | $\rho_l$ [C/m] | $\mathbf{J}_s$ [A/m] |
| surface / volume | $\rho_s$ [C/m²] | $\mathbf{J}$ [A/m²] |
| volume | $\rho$ [C/m³] | — |

Charges source $\mathbf{E}$ and $\mathbf{D}$; currents source $\mathbf{H}$ and $\mathbf{B}$. A δ-function carries units of 1/m per dimension, which is how a point charge $Q\,\delta(x)\delta(y)\delta(z)$ becomes a legitimate C/m³ ([[concepts/charge-density]]).

> [!tip] Three-second dimension checks that catch most errors
> - $\rho = \epsilon_0\nabla\cdot\mathbf{E}$: (F/m)(V/m)/m = C/m³ ✓ — if you forgot $\epsilon_0$, you have V/m², not a charge density.
> - $\oint\mathbf{D}\cdot d\mathbf{S}$: (C/m²)(m²) = C ✓.
> - $V = -\int\mathbf{E}\cdot d\mathbf{l}$: (V/m)(m) = V ✓.
> - $\mathcal{C} = \rho_l/V$: (C/m)/V = F/m ✓ — an answer in F for a "per unit length" quantity is wrong.
> - $E_0$ in a field like $E_0(2xy\hat{x}+\dots)$ must carry V/m³ for $\mathbf{E}$ to be V/m; numerical answers then quietly assume metres.

Related: [[1-electrostatics/01-fields-forces-and-the-maxwell-roadmap#3-units-and-the-source--field-bookkeeping|Lecture 1 §3]].
