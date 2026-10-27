---
title: "Radiation pressure"
description: "A wave pushes what it hits: at normal incidence a perfect mirror feels 2⟨S_i⟩/c and an absorber ⟨S_i⟩/c. The push is J × B on the skin current, and it shows that a wave carries momentum ⟨S⟩/c² per unit volume."
tags: [concept, waves]
aliases: ["light pressure", "momentum of a wave", "momentum density", "J × B force on a mirror", "photon momentum", "solar sail"]
---

> [!key] Radiation pressure (notes' box; normal incidence from vacuum)
> The wave's $\mathbf{B}$ acts on the moving charge carriers through the magnetic part of the [[concepts/lorentz-force|Lorentz force]]. With $N$ carriers per m³ moving at $\mathbf{v}$ in the skin layer of a good conductor ([[concepts/standing-waves|transmitted fields]] $\tilde{\mathbf{J}}_t = \sigma_2\tilde{\mathbf{E}}_t$, $\tilde{\mathbf{B}}_t = \mu_2\tilde{\mathbf{H}}_t$):
> $$
> \begin{gathered}
> N\mathbf{F} = Nq\mathbf{v}\times\mathbf{B}_t = \mathbf{J}_t\times\mathbf{B}_t\ \ [\text{N/m}^3],\\[6pt]
> \mathbf{P}_{rad} = \int_0^\infty\mathbf{J}_t\times\mathbf{B}_t\,dz\ \ [\text{N/m}^2],\\[6pt]
> \langle\mathbf{P}_{rad}\rangle = \int_0^\infty\tfrac12\text{Re}\{\tilde{\mathbf{J}}_t\times\tilde{\mathbf{B}}_t^*\}\,dz = \frac{2\langle\mathbf{S}_i\rangle}{c}.
> \end{gathered}
> $$
> $\langle\mathbf{S}_i\rangle = \hat z\,\lvert E_0\rvert^2/2\eta_0$ is the incident wave's flux. The push is along $\hat x\times\hat y = +\hat z$, into the mirror. An absorber feels $\langle S_i\rangle/c$.

**Physics.**
- The incident $\mathbf{E}$ drives a skin current along itself; the wave's $\mathbf{B}$ pushes the moving carriers through $q\mathbf{v}\times\mathbf{B}$, along the travel.
- **Waves carry momentum.** The notes' margin gives the momentum density $\langle\mathbf{S}_i\rangle/c^2$ [N·s/m³]. Arriving at speed $c$, it is a momentum flux $\langle S_i\rangle/c$. The mirror reverses it, so it receives twice that: the 2 is the wave's recoil (the notes cite Rothman and Boughn, *Am. J. Phys.* 77, 122). A black absorber stops the wave and feels $\langle S_i\rangle/c$ (this site's). A body that absorbs whatever it does not reflect feels $(1+\lvert\Gamma\rvert^2)\langle S_i\rangle/c$ (this site's; checked numerically for conductors).
- **Instantaneous push** (this site's, checked numerically). The same integral without the average gives $\mathbf{P}_{rad}(t) = \hat z\,\tfrac12\mu_0H_y^2(0,t) = \hat z\,(4\langle S_i\rangle/c)\cos^2\omega t$. That is the magnetic energy density at the mirror, and the force on the sheet $\mathbf{J}_s$ in the mean of the fields on its two faces, $\tfrac12\mathbf{B}(0,t)$. It pulses at $2\omega$ between zero and twice its mean.
- $\langle P_{rad}\rangle = \epsilon_0E_0^2$ equals the standing wave's $\langle w\rangle$ ([[concepts/standing-waves|Standing waves]]).
- **Photons** (notes' margin). The photon density is $\lvert\langle\mathbf{S}_i\rangle\rvert/\omega c\hbar$, so each photon carries momentum $\hbar\omega/c$. A circular wave's spin density $\pm\langle S_i\rangle/\omega c$ [N·s/m²] gives $\pm\hbar$ per photon ([[concepts/wave-polarization|Wave polarization]]).
- The notes' summary: waves not only heat, they push.

> [!derivation]- The time average, step by step (notes, with the conjugate written in)
> $\tilde{\mathbf{J}}_t\times\tilde{\mathbf{B}}_t^* = \hat z\,(\sigma_2\tau E_0)(\mu_2\tau E_0/\eta_2)^*e^{-2\alpha_2z}$. With $\sigma_2\tau\approx2\gamma_2/\eta_0$ and $\tau/\eta_2\approx2/\eta_0$ (real), and $\int_0^\infty e^{-2\alpha_2z}dz = 1/2\alpha_2$:
> $$
> \begin{gathered}
> \langle\mathbf{P}_{rad}\rangle\approx\hat z\,\frac{\lvert E_0\rvert^2}{2}\,\text{Re}\Big\{\frac{2\gamma_2}{\eta_0}\,\frac{2\mu_2}{\eta_0}\Big\}\frac{1}{2\alpha_2}\\[6pt]
> = \hat z\,2\,\frac{\lvert E_0\rvert^2}{2\eta_0}\,\frac{\text{Re}\{\gamma_2\}}{\alpha_2}\,\frac{\mu_2}{\eta_0} = \frac{2\langle\mathbf{S}_i\rangle}{c}.
> \end{gathered}
> $$
> $\text{Re}\{\gamma_2\} = \alpha_2$, and $\mu_0/\eta_0 = \sqrt{\mu_0\epsilon_0} = 1/c$.

**Examples.**

> [!example] Example — sunlight and a laser (this site's numbers)
> - Sunlight above the atmosphere, $\langle S_i\rangle\approx1361$ W/m² ($E_0\approx1.01$ kV/m as one cosine wave, [[concepts/time-average-power|Time averages and average power]]): a mirror feels $2\langle S_i\rangle/c = 9.08\ \mu$Pa, a black surface $4.54\ \mu$Pa. A 100 m × 100 m mirror sail gets 0.091 N.
> - The mirror's current peaks at $2E_0/\eta_0 = 5.4$ A/m.
> - A 1 W laser beam reflected straight back pushes with $2P/c = 6.7$ nN, whatever the spot size.

- Copper at 10 GHz: $\lvert\Gamma\rvert^2 = 0.99972$, so $\langle P_{rad}\rangle = 1.99972\,\langle S_i\rangle/c$, the mirror value to 0.014 %.
- [[problems/a-circular-wave-meets-a-mirror|Worked problem — A circular wave meets a mirror]]: a 94.2 W/m² circular wave pushes with a constant $2\pi\times10^{-7}$ N/m².

> [!trap] Radiation pressure
> - The 2 is for total reflection; an absorber feels $\langle S_i\rangle/c$.
> - Use the incident flux $\langle S_i\rangle$, not the standing wave's $\langle S\rangle = 0$.
> - Pressure is per unit area. A beam of power $P$ pushes a mirror with $2P/c$, whatever its width.
> - $\mathbf{E}$ drives the current along $\hat x$; only $\mathbf{v}\times\mathbf{B}$ points along $\hat z$.

> [!exam] On exams
> No Exam 3 paper on hand asks about radiation pressure. If asked: $2\langle S_i\rangle/c$ for a mirror, $\langle S_i\rangle/c$ for an absorber, force = pressure × area; momentum density $\langle S\rangle/c^2$.

**Where it appears.** [[3-maxwell-and-waves/26-standing-waves-and-radiation-pressure#6-radiation-pressure|Lecture 26 §6]] (the notes' $\mathbf{J}\times\mathbf{B}$ integral and the momentum margin notes); [[3-maxwell-and-waves/24-signal-transmission-and-circular-polarization|Lecture 24]] (photon spin); [[3-maxwell-and-waves/20-poynting-theorem-and-monochromatic-waves|Lecture 20]] (energy flux); [[problems/a-circular-wave-meets-a-mirror|Worked problem — A circular wave meets a mirror]].

**Related.** [[concepts/standing-waves|Standing waves]] · [[concepts/poynting-vector|Poynting vector]] · [[concepts/time-average-power|Time averages and average power]] · [[concepts/lorentz-force|Lorentz force]] · [[concepts/skin-depth|Skin depth]] · [[concepts/reflection-and-transmission|Reflection and transmission coefficients]] · [[concepts/wave-polarization|Wave polarization]].

**Practice.** [[practice/topics#standing-waves-and-radiation-pressure|Standing waves and radiation pressure]] (13 problems) — for example [[practice/26-standing-waves-and-radiation-pressure#261-nodes-in-front-of-a-mirror|26.1 Nodes in front of a mirror]] (easy), [[practice/26-standing-waves-and-radiation-pressure#266-a-mirror-off-the-origin|26.6 A mirror off the origin]] (medium), [[practice/26-standing-waves-and-radiation-pressure#269-is-it-a-standing-wave|26.9 Is it a standing wave]] (hard).
