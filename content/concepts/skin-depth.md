---
title: "Skin depth"
description: "δ = 1/α, the depth where a wave's field falls to 1/e; in a good conductor δ = 1/√(πfμσ) = λ/2π."
tags: [concept, waves]
aliases: ["penetration depth", "skin effect", "δ = 1/α", "delta = 1/alpha"]
---

> [!key] Definition
> $$
> \begin{gathered}
> \delta\equiv\frac1\alpha\ [\text{m}]:\\[4pt]
> \lvert\tilde{\mathbf{E}}\rvert\propto e^{-z/\delta},\qquad \langle S\rangle\propto e^{-2z/\delta}.
> \end{gathered}
> $$
> **Good conductor** ($\sigma/\omega\epsilon\gg1$):
> $$
> \begin{gathered}
> \delta = \frac{1}{\sqrt{\pi f\mu\sigma}} = \sqrt{\frac{2}{\omega\mu\sigma}},\\[4pt]
> \gamma = \frac{1+j}{\delta},\qquad \lambda = 2\pi\delta,\qquad \eta = \frac{1+j}{\sigma\delta}.
> \end{gathered}
> $$
> **Imperfect dielectric** ($\sigma/\omega\epsilon\ll1$): $\delta\approx\dfrac2\sigma\sqrt{\epsilon/\mu}$, independent of frequency.
>
> The notes: *penetration depth* for $1/\alpha$ in general, *skin depth* when it is small.

**Physics.** Currents $\sigma\mathbf{E}$ take the wave's energy as Joule heat; eddy currents oppose the changing $\mathbf{B}$ (Lenz, [[2-magnetostatics/14-faradays-law-and-induced-emf|Lecture 14]]), so each layer shields those below. In a good conductor $\alpha = \beta = 1/\delta$: the field falls by $e^{-2\pi}\approx1/535$ (54.6 dB) per wavelength; 86 % of the power is absorbed within $\delta$ ($1 - e^{-2}$), 99.75 % within $3\delta$. $\delta\propto1/\sqrt{f\mu\sigma}$: four times the frequency halves it, and $\mu_r\gg1$ shrinks it by $1/\sqrt{\mu_r}$. $\text{Re}\,\eta = 1/(\sigma\delta)$ is the DC resistance of a square of metal $\delta$ thick (the *surface resistance*): the wave sees a resistive sheet that thick.

**Examples** (good-conductor formula, $\mu = \mu_0$; σ from Rao Table 5.1).

| $f$ | copper, $5.8\times10^{7}$ S/m | aluminium, $3.5\times10^{7}$ S/m | seawater, 4 S/m |
|---|---|---|---|
| 60 Hz | 8.53 mm | 11.0 mm | 32.5 m |
| 1 kHz | 2.09 mm | 2.69 mm | 7.96 m |
| 1 MHz | 66.1 µm | 85.1 µm | 25 cm |
| 1 GHz | 2.09 µm | 2.69 µm | not a good conductor: 1.3 cm (exact) |

- Closed form: copper $0.0661/\sqrt f$ m (Rao's $0.066/\sqrt f$), aluminium $0.0851/\sqrt f$ m, seawater $252/\sqrt f$ m, while $\sigma/\omega\epsilon>10$ (seawater: below about 90 MHz).
- Notes' Example 3, seawater at 1 kHz: $\delta = 1/\sqrt{16\pi^2\times10^{-4}} = 25/\pi = 7.96$ m, $\lambda = 50$ m.
- Submarines: 28.9 m at 76 Hz (ELF), 1.62 m at 24 kHz (VLF); a 100 dB budget reaches $11.5\,\delta$, about 330 m and 19 m.
- Copper wire, radius 1 mm, 1 MHz: current in about 66 µm, resistance about $a/2\delta = 7.6$ times DC.
- Moist soil ($\sigma = 10^{-2}$ S/m), 100 kHz: $\delta = 50/\pi = 15.9$ m ([[problems/a-radio-wave-into-moist-ground]]).

> [!trap]
> - $\delta$ is for the **field**: the power is down to $1/e$ at $\delta/2$, to 14 % at $\delta$.
> - $1/\sqrt{\pi f\mu\sigma}$ needs $\sigma/\omega\epsilon\gg1$; seawater at 1 GHz ($\sigma/\omega\epsilon = 0.89$) is 1.3 cm exact, 0.8 cm by formula.
> - $\pi f$ with $f$, or $\sqrt{2/\omega\mu\sigma}$ with $\omega$; mixing them costs $\sqrt{2\pi}$.
> - In an imperfect dielectric $1/\alpha\approx(2/\sigma)\sqrt{\epsilon/\mu}$ does not shrink as $1/\sqrt f$.
> - The δ of "tan δ" is a loss angle ([[concepts/loss-tangent]]).

**Where it appears.** [[3-maxwell-and-waves/22-phasor-maxwell-equations-and-damped-waves|Lecture 22]] ($1/\alpha$, two limits); [[3-maxwell-and-waves/23-imperfect-dielectrics-and-good-conductors|Lecture 23]] (§4–§6: good conductors, seawater, metals); Lecture 14 (the mechanism); [[3-maxwell-and-waves/16-charge-conservation-displacement-current-and-maxwells-equations|Lecture 16]] (perfect conductor, $\delta = 0$); Lecture 25 (reflection).

**Practice.** [[practice/topics#imperfect-dielectrics-good-conductors-and-skin-depth|Imperfect dielectrics, good conductors and skin depth]] (18 problems) — for example [[practice/23-imperfect-dielectrics-and-good-conductors#231-six-media-at-one-frequency|23.1 Six media at one frequency]] (easy), [[practice/23-imperfect-dielectrics-and-good-conductors#236-wavelength-and-depth-measured-underground|23.6 Wavelength and depth measured underground]] (medium), [[practice/23-imperfect-dielectrics-and-good-conductors#239-down-into-a-deep-lake|23.9 Down into a deep lake]] (hard).

Related: [[concepts/propagation-constant]] · [[concepts/intrinsic-impedance]] · [[concepts/conductors]] · [[concepts/faradays-law]] · [[concepts/poynting-vector]].
