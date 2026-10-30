---
title: "Waves in media — figure reference"
description: "Five reference figures for Lectures 18–30: the family of wave equations (lossless, Helmholtz, diffusion, plasma, transmission line), where θ, τ and ∠γ come from, one wave in four media, phase velocity and loss per wavelength in real materials, and the plane-wave ↔ transmission-line dictionary."
tags: [toolkit, waves]
aliases: ["waves in media figures", "wave equation family", "diffusion equation", "plane wave transmission line analogy"]
---

*Reference page for Lectures 18–30. Symbols, units and regime formulas: [[0-toolkit/07-wave-parameters-map|Wave parameters on one page]]. Every curve is computed from the exact $\gamma$ and $\eta$; every number is checked in `tools/media/verify_media.py`.*

## 1. One equation, many media

> [!key] The general wave equation (source-free, homogeneous, linear medium)
> $$
> \nabla^2\mathbf{E} = \underbrace{\mu\sigma\frac{\partial\mathbf{E}}{\partial t}}_{\text{conduction: loss}} + \underbrace{\mu\epsilon\frac{\partial^2\mathbf{E}}{\partial t^2}}_{\text{displacement: waves}},\qquad \text{one frequency: }\ \nabla^2\tilde{\mathbf{E}} = \gamma^2\tilde{\mathbf{E}},\quad \gamma^2 = j\omega\mu(\sigma + j\omega\epsilon).
> $$
> $\mathbf{H}$ obeys the same equation.

<!-- fig:media-wave-equations -->

> [!derivation]- From Maxwell's equations to the general equation
> Take the curl of Faraday's law and substitute Ampère's law with $\mathbf{J} = \sigma\mathbf{E}$:
> $$
> \nabla\times\nabla\times\mathbf{E} = -\mu\frac{\partial}{\partial t}\nabla\times\mathbf{H} = -\mu\sigma\frac{\partial\mathbf{E}}{\partial t} - \mu\epsilon\frac{\partial^2\mathbf{E}}{\partial t^2}.
> $$
> With no free charge inside, $\nabla\cdot\mathbf{E} = 0$, so $\nabla\times\nabla\times\mathbf{E} = \nabla(\nabla\cdot\mathbf{E}) - \nabla^2\mathbf{E} = -\nabla^2\mathbf{E}$. Replacing $\partial/\partial t$ by $j\omega$ gives the Helmholtz form.

- $\sigma = 0$: the wave equation of [[3-maxwell-and-waves/18-the-wave-equation-and-plane-tem-waves|Lecture 18]]; any shape $f(t\mp z/v)$ travels unchanged.
- $\sigma\gg\omega\epsilon$ at every frequency in the signal: the displacement term drops and the equation is a **diffusion equation**, the heat equation. Fields soak into a conductor rather than travel through it. The notes do not use the name; geophysics calls this the quasi-static regime (EM GeoSci). At one frequency it is the good conductor of [[concepts/skin-depth|Skin depth]], $\gamma^2 = j\omega\mu\sigma$.
- A collisionless plasma has $\sigma = -jNq^2/(m\omega)$ ([[concepts/dispersion-relation|Dispersion relation]]), so $\gamma^2 = (\omega_p^2 - \omega^2)/c^2$: real (evanescent) below $\omega_p$, imaginary (travelling) above.
- A transmission line obeys $d^2\tilde V/dz^2 = \gamma^2\tilde V$ with $\gamma^2 = (\mathcal{R} + j\omega\mathcal{L})(\mathcal{G} + j\omega\mathcal{C})$ (§5).

## 2. Where θ, τ and ∠γ come from

<!-- fig:media-angles -->

$$
\tan\theta = \frac{\sigma}{\omega\epsilon},\qquad \tau = \angle\eta = \frac\theta2,\qquad \angle\gamma = 90^\circ - \tau,\qquad \frac\alpha\beta = \tan\tau .
$$

> [!trap] τ is not the loss tangent
> The loss tangent is $\tan\theta = \sigma/\omega\epsilon$. The angle of $\eta$ is half of $\theta$. "$\tau\approx\sigma/2\omega\epsilon$" holds only when $\sigma/\omega\epsilon\ll1$, and $\tau$ never exceeds $45^\circ$. A $\gamma$ at less than $45^\circ$ means $\alpha$ and $\beta$ were swapped.

## 3. What the wave looks like

<!-- fig:media-snapshots -->

The snapshot $e^{-\alpha z}\cos(\omega t - \beta z)$ of $E$ and $e^{-\alpha z}\cos(\omega t - \beta z - \tau)$ of $\lvert\eta\rvert H$: the $H$ crest trails the $E$ crest by $\tau/2\pi$ of a wavelength, which at a fixed point is a time lag of $\tau$. Below its plasma frequency a plasma has a real $\gamma = \kappa$ and an imaginary $\eta$, so $\langle\mathbf{S}\rangle = \tfrac12\text{Re}\{\tilde{\mathbf{E}}\times\tilde{\mathbf{H}}^*\} = 0$: the wave is turned back, not absorbed.

## 4. Dispersion and loss across media

<!-- fig:media-dispersion -->

$$
\text{loss per wavelength} = 8.686\,\alpha\lambda = 2\pi\cdot8.686\,\tan\tau = 54.6\tan\!\Big(\tfrac12\tan^{-1}\frac{\sigma}{\omega\epsilon}\Big)\ \text{dB},\qquad \text{loss per skin depth} = 8.686\ \text{dB}.
$$

| medium | $\sigma$ [S/m] | $\epsilon_r$ | $f_c = \sigma/2\pi\epsilon$ | source |
|---|---|---|---|---|
| copper | $5.8\times10^{7}$ | 1 | $1.0\times10^{18}$ Hz | Rao, Table 5.1 |
| seawater | 4 | 81 | 0.89 GHz | course notes (Rao: 80); ITU-R P.527: $\sigma$ varies with temperature and salinity |
| moist soil (loam) | $10^{-2}$ | 10 | 18 MHz | ITU-R P.527-6 §4.1 (dried loam: $10^{-4}$); Rao, Table 5.2 |
| fresh water | $10^{-3}$ | 80 | 225 kHz | Rao |
| ionosphere (plasma) | — | — | $f_p = \sqrt{80.6N} = 9$ MHz at $N = 10^{12}\ \text{m}^{-3}$ | Kudeki, ECE 458 notes |

Constant $\sigma$ and $\epsilon$ are an idealization (the notes make it too): water's $\epsilon_r$ falls in the microwave range (ITU-R P.527), and copper stops being a simple conductor long before $10^{18}$ Hz ([[concepts/conductivity-and-susceptibility-models|Lorentz–Drude models]]).

## 5. The same equations on a transmission line

<!-- fig:media-tl-analogy -->

| | plane wave ($E_x$, $H_y$, along $z$) | transmission line ($V$, $I$) |
|---|---|---|
| Faraday / first telegrapher | $-\dfrac{\partial E_x}{\partial z} = \mu\dfrac{\partial H_y}{\partial t}$ | $-\dfrac{\partial V}{\partial z} = \mathcal{R}I + \mathcal{L}\dfrac{\partial I}{\partial t}$ |
| Ampère / second telegrapher | $-\dfrac{\partial H_y}{\partial z} = \sigma E_x + \epsilon\dfrac{\partial E_x}{\partial t}$ | $-\dfrac{\partial I}{\partial z} = \mathcal{G}V + \mathcal{C}\dfrac{\partial V}{\partial t}$ |
| propagation constant | $\gamma = \sqrt{j\omega\mu(\sigma + j\omega\epsilon)}$ | $\gamma = \sqrt{(\mathcal{R} + j\omega\mathcal{L})(\mathcal{G} + j\omega\mathcal{C})}$ |
| impedance of one travelling wave | $\eta = \sqrt{\dfrac{j\omega\mu}{\sigma + j\omega\epsilon}}$ | $Z_0 = \sqrt{\dfrac{\mathcal{R} + j\omega\mathcal{L}}{\mathcal{G} + j\omega\mathcal{C}}}$ |
| reflection | $\Gamma = \dfrac{\eta_2 - \eta_1}{\eta_2 + \eta_1}$ | $\Gamma_L = \dfrac{Z_L - Z_0}{Z_L + Z_0}$ |
| average power | $\langle S_z\rangle = \tfrac12\text{Re}\{\tilde E_x\tilde H_y^*\}$ | $\langle P\rangle = \tfrac12\text{Re}\{\tilde V\tilde I^*\}$ |

Lectures 27–30 use lossless lines, $\mathcal{R} = \mathcal{G} = 0$: $\gamma = j\omega\sqrt{\mathcal{L}\mathcal{C}}$ and $Z_0 = \sqrt{\mathcal{L}/\mathcal{C}}$, the twins of $\beta = \omega\sqrt{\mu\epsilon}$ and $\eta = \sqrt{\mu/\epsilon}$. The parallel-plate line makes the map literal: $V = E_xd$, $I = H_yW$, $\mathcal{L} = \mu d/W$, $\mathcal{C} = \epsilon W/d$ ([[concepts/telegraphers-equations|Telegrapher's equations]]).

**Topic pages.** [[concepts/wave-equation|Wave equation]] · [[concepts/phasor-maxwell-equations|Maxwell's equations in phasor form]] · [[concepts/propagation-constant|Propagation constant]] · [[concepts/intrinsic-impedance|Intrinsic impedance]] · [[concepts/loss-tangent|Loss tangent]] · [[concepts/skin-depth|Skin depth]] · [[concepts/dispersion-relation|Dispersion relation]] · [[concepts/group-velocity|Group velocity]] · [[concepts/characteristic-impedance|Characteristic impedance]]

### Sources for this page
- E. Kudeki, ECE 329 course notes, Lectures 18–30; N. N. Rao, *Fundamentals of Electromagnetics for Electrical and Computer Engineering*, Tables 5.1–5.2.
- [EM GeoSci — Derivation of the wave equation in time](https://github.com/geoscixyz/em/blob/main/content/maxwell1_fundamentals/appendix/wave_eq_derivation.rst) (the general time-domain equation).
- [EM GeoSci — Attenuation and skin depth](https://em.geosci.xyz/content/maxwell1_fundamentals/harmonic_planewaves_homogeneous/skindepth.html) (quasi-static and wave regimes).
- [Løseth et al., "Low-frequency electromagnetic fields in applied geophysics: Waves or diffusion?", *Geophysics* 71 (2006)](https://doi.org/10.1190/1.2208275).
- [E. Kudeki, ECE 458 notes, *Applications of Radiowave Propagation*](https://courses.physics.illinois.edu/ece458/458sp10.pdf) (plasma frequency $\sqrt{80.6N}$, ionospheric maximum about 9 MHz, evanescence below $f_p$).
- [ITU-R Recommendation P.527-6, *Electrical characteristics of the surface of the Earth*](https://www.itu.int/dms_pubrec/itu-r/rec/p/R-REC-P.527-6-202109-I!!PDF-E.pdf) (soil conductivity range).
- [M. Steer, *Microwave and RF Design II*, §2.2 Transmission line theory](https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Microwave_and_RF_Design_II_-_Transmission_Lines_(Steer)/02%3A_Transmission_Lines/2.02%3A_Transmission_Line_Theory) ($\gamma$ and $Z_0$ of a lossy line).
- [F. Martín, Appendix A: equivalence between plane waves and TEM lines (Wiley, 2015)](https://doi.org/10.1002/9781119058403.app1).
