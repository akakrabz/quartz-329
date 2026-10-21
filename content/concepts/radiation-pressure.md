---
title: "Radiation pressure"
description: "A wave pushes what it hits: at normal incidence a perfect mirror feels 2⟨S_i⟩/c and an absorber ⟨S_i⟩/c. The push is J × B on the skin current, and it shows that a wave carries momentum ⟨S⟩/c² per unit volume."
tags: [concept, waves]
aliases: ["light pressure", "momentum of a wave", "momentum density", "J × B force on a mirror"]
---

> [!key] Definition (normal incidence from vacuum)
> $$
> \begin{gathered}
> \mathbf{P}_{rad} = \int_0^\infty\mathbf{J}\times\mathbf{B}\,dz\ \ [\text{N/m}^2],\\[6pt]
> \langle P_{rad}\rangle = \frac{2\langle S_i\rangle}{c}\ \ \text{(mirror)},\\[6pt]
> \langle P_{rad}\rangle = \frac{\langle S_i\rangle}{c}\ \ \text{(absorber)}.
> \end{gathered}
> $$
> A force per unit area along the incident travel. $\langle S_i\rangle$ is the incident wave's time-average flux [W/m²].

**Physics.**
- The incident $\mathbf{E}$ drives a skin current along itself; the wave's $\mathbf{B}$ pushes the moving carriers through $q\mathbf{v}\times\mathbf{B}$, along the travel ([[concepts/lorentz-force]]).
- Momentum view: a wave carries momentum density $\langle S\rangle/c^2$ [N·s/m³], a momentum flux $\langle S\rangle/c$. An absorber stops it; a mirror reverses it and receives it twice.
- A body that absorbs whatever it does not reflect feels $(1+\lvert\Gamma\rvert^2)\langle S_i\rangle/c$ (this site's; checked numerically for conductors).
- Perfect mirror, instantaneous: $P_{rad}(t) = \tfrac12\mu_0\lvert\mathbf{H}(0,t)\rvert^2$, the magnetic energy density at the surface; $(4\langle S_i\rangle/c)\cos^2\omega t$ for a linear wave. The mean $\epsilon_0E_0^2$ equals the standing wave's $\langle w\rangle$.
- Per photon: momentum $\hbar\omega/c$; a circular wave adds spin $\pm\hbar$.

**Examples.**
- Sunlight, 1361 W/m²: 9.08 µPa on a mirror, 4.54 µPa on a black surface. A 100 m × 100 m mirror sail: 0.091 N.
- A 1 W laser beam reflected back: $2P/c = 6.7$ nN.
- Copper at 10 GHz: $\lvert\Gamma\rvert^2 = 0.99972$, so $\langle P_{rad}\rangle = 1.99972\,\langle S_i\rangle/c$, the mirror value to 0.014 %.
- [[problems/a-circular-wave-meets-a-mirror]]: a 94.2 W/m² circular wave pushes with a constant $2\pi\times10^{-7}$ N/m².

> [!trap]
> - The 2 needs total reflection.
> - Use the incident $\langle S_i\rangle$; the standing wave's own $\langle S\rangle$ is 0.
> - Pressure is per unit area; a beam of power $P$ gives a force $2P/c$ on a mirror, whatever its width.
> - $\mathbf{E}$ drives the current along the surface; only $\mathbf{v}\times\mathbf{B}$ pushes normal to it.

**Where it appears.** [[3-maxwell-and-waves/26-standing-waves-and-radiation-pressure|Lecture 26]] §6 (the notes' $\mathbf{J}\times\mathbf{B}$ integral and the momentum margin notes); [[3-maxwell-and-waves/24-signal-transmission-and-circular-polarization|Lecture 24]] (photon spin); [[3-maxwell-and-waves/20-poynting-theorem-and-monochromatic-waves|Lecture 20]] (energy flux).

**Practice.** [[practice/topics#standing-waves-and-radiation-pressure|Standing waves and radiation pressure]] (13 problems) — for example [[practice/26-standing-waves-and-radiation-pressure#261-nodes-in-front-of-a-mirror|26.1 Nodes in front of a mirror]] (easy), [[practice/26-standing-waves-and-radiation-pressure#266-a-mirror-off-the-origin|26.6 A mirror off the origin]] (medium), [[practice/26-standing-waves-and-radiation-pressure#269-is-it-a-standing-wave|26.9 Is it a standing wave]] (hard).

Related: [[concepts/standing-waves]] · [[concepts/poynting-vector]] · [[concepts/lorentz-force]] · [[concepts/skin-depth]] · [[concepts/reflection-and-transmission]].
