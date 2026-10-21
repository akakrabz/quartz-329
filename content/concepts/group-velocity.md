---
title: "Group velocity"
description: "The envelope of a narrowband signal travels at the group velocity v_g = dω/dβ, its carrier crests at the phase velocity v_p = ω/β. They agree in a non-dispersive medium; in a collisionless plasma v_p v_g = c², so crests outrun light while signals do not."
tags: [concept, waves]
aliases: ["envelope velocity", "signal velocity", "narrowband AM"]
---

> [!key] Definition
> A narrowband signal $m(t)\cos\omega t$ launched at $z = 0$ into a medium with dispersion relation $\beta(\omega)$ arrives as
> $$
> \begin{gathered}
> \mathbf{E}\approx m\Big(t-\frac{z}{v_g}\Big)\cos(\omega t-\beta z)\,\hat x,\\[4pt]
> v_g = \frac{d\omega}{d\beta},\qquad v_p = \frac\omega\beta,
> \end{gathered}
> $$
> both evaluated at the carrier $\omega$. The envelope (the message) moves at $v_g$ [m/s], the crests at $v_p$.

**Physics.** A signal is a group of nearby frequencies. Expanding $\beta(\omega)$ to first order about the carrier gives every frequency in the envelope the same delay $z/v_g$, while the carrier phase lags by $\beta z$. The derivation is folded on the [[3-maxwell-and-waves/24-signal-transmission-and-circular-polarization#2-dispersive-media-group-velocity|Lecture 24 page]]. If $\beta\propto\omega$ the medium is non-dispersive, $v_g = v_p$, and any waveform keeps its shape. Otherwise the second-order term, $\tfrac12\beta''(\Delta\omega)^2z$, slowly spreads the envelope. On an $\omega$–$\beta$ diagram $v_g$ is the slope of the tangent and $v_p$ the slope of the chord from the origin.

| medium | $v_p$ | $v_g$ |
|---|---|---|
| dielectric | $1/\sqrt{\mu\epsilon}$ | $v_p$ |
| gas (sound; $m$ atomic mass) | $\sqrt{5k_BT/3m}$ | $v_p$ |
| plasma | $c/\sqrt{1-\omega_p^2/\omega^2}$ | $c^2/v_p$ |

The plasma relation is $\omega^2 = \omega_p^2 + c^2\beta^2$, so $v_g = c\sqrt{1-\omega_p^2/\omega^2}$ and $v_pv_g = c^2$.

**Examples.**
- Plasma at $\omega = 2\omega_p$: $v_g = 0.866c$, $v_p = 1.155c$. Each crest slides forward through the envelope.
- Ionosphere, $N = 10^{12}$ m⁻³ ($f_p = 8.98$ MHz), at 10 MHz: $v_g = 0.440c$ and $v_p = 2.27c$. A voice-band message needs 2.27 ms to cross 300 km of such plasma, against 1.00 ms in vacuum.
- Good conductor ([[3-maxwell-and-waves/23-imperfect-dielectrics-and-good-conductors|Lecture 23]]): $\beta\approx\sqrt{\omega\mu\sigma/2}$ gives $v_g = 2v_p$. This is formal, since the wave dies within about a wavelength.

> [!trap]
> - $\omega/\beta$ is a signal speed only when $\beta\propto\omega$.
> - $v_g = d\omega/d\beta$, the inverse of $d\beta/d\omega$; not $\omega/\beta$.
> - $v_p>c$ in a plasma violates nothing; a pure cosine carries no information.

**Where it appears.** [[3-maxwell-and-waves/24-signal-transmission-and-circular-polarization|Lecture 24]] (the notes' footnote, with the derivation, table and examples); [[3-maxwell-and-waves/21-monochromatic-waves-and-phasor-notation|Lecture 21]] (the dispersion relations). The notes leave the details to ECE 450. No Exam 3 paper on hand asks about it.

**Practice.** [[practice/topics#group-velocity-and-wave-polarization|Group velocity and wave polarization]] (13 problems) — for example [[practice/24-group-velocity-and-polarization#241-crests-and-envelope-in-a-plasma|24.1 Crests and envelope in a plasma]] (easy), [[practice/24-group-velocity-and-polarization#246-from-two-snapshots-to-a-phasor|24.6 From two snapshots to a phasor]] (medium), [[practice/24-group-velocity-and-polarization#249-building-a-right-circular-wave|24.9 Building a right-circular wave]] (hard).

Related: [[concepts/dispersion-relation]] · [[concepts/plane-waves]] · [[concepts/wave-polarization]].
