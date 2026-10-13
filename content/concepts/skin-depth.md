---
title: "Skin depth"
description: "δ = 1/α is the distance in which a wave's field falls to 1/e, and its power to 1/e². In a good conductor δ = 1/√(πfμσ), with α = β = 1/δ and λ = 2πδ, so a wave dies within a wavelength: copper 8.5 mm at 60 Hz and 2.1 µm at 1 GHz, seawater 7.96 m at 1 kHz. In an imperfect dielectric the penetration depth (2/σ)√(ε/μ) does not depend on frequency."
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
> The notes call $1/\alpha$ the *penetration depth* in general and the *skin depth* when it is small, as in a good conductor.

**Physics.** A wave entering a conductor drives currents $\sigma\mathbf{E}$, and those currents remove its energy as Joule heat. Faraday's law explains why the field does not simply fill the conductor. The changing $\mathbf{B}$ induces eddy currents whose own field opposes the change (Lenz, [[2-magnetostatics/14-faradays-law-and-induced-emf|Lecture 14]]), so each layer shields the layers below it. In a good conductor the decay and the phase advance share one length: $\alpha = \beta = 1/\delta$. So the field falls by $e^{-2\pi}\approx1/535$ (54.6 dB) in one wavelength, and the power is 86 % absorbed within the first $\delta$ ($1 - e^{-2}$) and 99.75 % within $3\delta$. Since $\delta\propto1/\sqrt{f\mu\sigma}$, four times the frequency halves it, and a magnetic metal ($\mu_r\gg1$) has a smaller $\delta$ than a non-magnetic metal of the same $\sigma$, by the factor $1/\sqrt{\mu_r}$. The real part of $\eta$, $1/(\sigma\delta)$, is the DC resistance of a square of the metal one skin depth thick (the *surface resistance*). The wave sees the conductor as a resistive sheet that thick.

**Examples** (good-conductor formula, $\mu = \mu_0$; σ from Rao Table 5.1).

| $f$ | copper, $5.8\times10^{7}$ S/m | aluminium, $3.5\times10^{7}$ S/m | seawater, 4 S/m |
|---|---|---|---|
| 60 Hz | 8.53 mm | 11.0 mm | 32.5 m |
| 1 kHz | 2.09 mm | 2.69 mm | 7.96 m |
| 1 MHz | 66.1 µm | 85.1 µm | 25 cm |
| 1 GHz | 2.09 µm | 2.69 µm | not a good conductor: 1.3 cm (exact) |

- In closed form: copper $0.0661/\sqrt f$ m (Rao's $0.066/\sqrt f$), aluminium $0.0851/\sqrt f$ m, seawater $252/\sqrt f$ m, valid while $\sigma/\omega\epsilon>10$. For seawater that means below about 90 MHz.
- The notes' Example 3: seawater at 1 kHz, $\delta = 1/\sqrt{16\pi^2\times10^{-4}} = 25/\pi = 7.96$ m, so $\lambda = 50$ m.
- Submarine links: 28.9 m at 76 Hz (ELF) and 1.62 m at 24 kHz (VLF). A 100 dB loss budget reaches $11.5\,\delta$, about 330 m and 19 m.
- Skin effect: a copper wire of radius 1 mm at 1 MHz carries its current in a layer about 66 µm thick, so its resistance is about $a/2\delta = 7.6$ times its DC value.
- Moist soil ($\sigma = 10^{-2}$ S/m) at 100 kHz: $\delta = 50/\pi = 15.9$ m ([[problems/a-radio-wave-into-moist-ground]]).

> [!trap]
> - $\delta$ is for the **field**. The power falls to $1/e$ at $\delta/2$; at $z = \delta$ only 14 % of it remains.
> - The formula $1/\sqrt{\pi f\mu\sigma}$ needs $\sigma/\omega\epsilon\gg1$. Seawater at 1 GHz ($\sigma/\omega\epsilon = 0.89$) has an exact $\delta$ of 1.3 cm; the formula gives 0.8 cm.
> - $\pi f$ with $f$, or $\sqrt{2/\omega\mu\sigma}$ with $\omega$. Mixing them gives an error of $\sqrt{2\pi}$.
> - In an imperfect dielectric $1/\alpha\approx(2/\sigma)\sqrt{\epsilon/\mu}$ does not shrink as $1/\sqrt f$.
> - The δ of a datasheet's "tan δ" is a loss angle ([[concepts/loss-tangent]]), not a skin depth.

**Where it appears.** [[3-maxwell-and-waves/22-phasor-maxwell-equations-and-damped-waves|Lecture 22]] (penetration depth $1/\alpha$ and its two limiting formulas); [[3-maxwell-and-waves/23-imperfect-dielectrics-and-good-conductors|Lecture 23]] (§4 the good-conductor wave, §5 seawater and submarines, §6 metals); [[2-magnetostatics/14-faradays-law-and-induced-emf|Lecture 14]] (eddy currents and Lenz's law, the mechanism); [[3-maxwell-and-waves/16-charge-conservation-displacement-current-and-maxwells-equations|Lecture 16]] (the perfect conductor, $\delta = 0$); Lecture 25 (reflection from a good conductor); [[problems/a-radio-wave-into-moist-ground]].

**Practice.** [[practice/topics#imperfect-dielectrics-good-conductors-and-skin-depth|Imperfect dielectrics, good conductors and skin depth]] (16 problems) — for example [[practice/23-imperfect-dielectrics-and-good-conductors#231-six-media-at-one-frequency|23.1 Six media at one frequency]] (easy), [[practice/23-imperfect-dielectrics-and-good-conductors#236-wavelength-and-depth-measured-underground|23.6 Wavelength and depth measured underground]] (medium), [[practice/23-imperfect-dielectrics-and-good-conductors#239-down-into-a-deep-lake|23.9 Down into a deep lake]] (hard).

Related: [[concepts/loss-tangent]] · [[concepts/propagation-constant]] · [[concepts/intrinsic-impedance]] · [[concepts/conductors]] · [[concepts/faradays-law]] · [[concepts/poynting-vector]].
