---
title: "Standing waves"
description: "Two equal waves travelling in opposite directions, as in front of a perfect mirror, add to a pattern that oscillates in place: E ∝ sin βz sin ωt and H ∝ cos βz cos ωt, nodes λ/2 apart, E and H a quarter wavelength and a quarter period apart, and no net power."
tags: [concept, waves]
aliases: ["standing wave", "complete standing wave", "partial standing wave", "node", "antinode"]
---

> [!key] Definition (perfect mirror at z = 0, wave incident from z < 0)
> $$
> \begin{gathered}
> \tilde{\mathbf{E}} = -j\hat x\,2E_0\sin\beta z,\\[4pt]
> \tilde{\mathbf{H}} = \hat y\,\frac{2E_0}{\eta}\cos\beta z,\\[6pt]
> \mathbf{E} = \hat x\,2E_0\sin\beta z\,\sin\omega t,\\[4pt]
> \mathbf{H} = \hat y\,\frac{2E_0}{\eta}\cos\beta z\,\cos\omega t .
> \end{gathered}
> $$
> Incident $\hat x\,E_0e^{-j\beta z}$ plus reflected $-\hat x\,E_0e^{j\beta z}$ ($\Gamma = -1$). Each field is a function of $z$ times a function of $t$: it oscillates in place.

**Physics.**
- $\mathbf{E}$ nodes at the mirror and every $\lambda/2$ from it; $\mathbf{H}$ nodes halfway between. $\lvert\tilde{\mathbf{E}}\rvert$ repeats every $\lambda/2$.
- $\mathbf{E}$ and $\mathbf{H}$ are a quarter wavelength apart in space and a quarter period apart in time. The time quadrature makes $\langle\mathbf{S}\rangle = \tfrac12\text{Re}\{\tilde{\mathbf{E}}\times\tilde{\mathbf{H}}^*\} = 0$. The two travelling waves carry equal power both ways.
- Instantaneously $\mathbf{S} = \hat z\,(E_0^2/\eta)\sin2\beta z\,\sin2\omega t$. Energy sloshes between the $\mathbf{H}$ antinodes (all magnetic at $\omega t = 0$) and the $\mathbf{E}$ antinodes (all electric at $\omega t = \pi/2$). It never crosses a multiple of $\lambda/4$; $\langle w\rangle = \epsilon E_0^2$ everywhere.
- The mirror carries $\mathbf{J}_s = \hat x\,(2E_0/\eta)\cos\omega t$. An $\mathbf{E}$ node acts as a short circuit, an $\mathbf{H}$ node as an open.
- Partial reflection, $\lvert\Gamma\rvert<1$ (this site's; the notes treat only $\Gamma = -1$): a travelling part plus a standing part. $\lvert\tilde E\rvert$ ripples between $(1\pm\lvert\Gamma\rvert)E_0$, with net power $(1-\lvert\Gamma\rvert^2)E_0^2/2\eta$.

**Examples.**
- 1.5 GHz in air ($\lambda = 20$ cm): $\mathbf{E}$ nodes at 0, 10, 20 cm from the mirror, $\mathbf{H}$ nodes at 5, 15, 25 cm.
- Vacuum onto $\epsilon_r = 9$ ($\Gamma = -1/2$): $\lvert\tilde E\rvert$ between $0.5E_0$ and $1.5E_0$, minimum at the interface.
- [[problems/a-circular-wave-meets-a-mirror]]: a circular wave on a mirror. The two components' standing waves are 90° apart in time, so $\mathbf{S} = 0$ at every instant and $w = 2\epsilon_0E_0^2$ is constant.

> [!trap]
> - In a linear standing wave only the *average* flux vanishes; $\mathbf{S}$ and $w$ do not.
> - $\lvert\tilde{\mathbf{E}}\rvert$ has period $\lambda/2$, not $\lambda$.
> - $\mathbf{E}$ and $\mathbf{H}$ have the same shape, shifted by $\lambda/4$; a plot alone does not say which is which.
> - With $\Gamma = -1$ the reflected $\tilde{\mathbf{H}}$ keeps the incident sign.

**Where it appears.** [[3-maxwell-and-waves/26-standing-waves-and-radiation-pressure|Lecture 26]] (the whole lecture); [[3-maxwell-and-waves/25-wave-reflection-and-transmission|Lecture 25]] §3 ($\Gamma = -1$); [[3-maxwell-and-waves/20-poynting-theorem-and-monochromatic-waves|Lecture 20]] §7 (two counter-propagating waves); [[4-transmission-lines/index|Unit 4]] (voltage and current on shorted and open lines).

**Practice.** [[practice/topics#standing-waves-and-radiation-pressure|Standing waves and radiation pressure]] (13 problems) — for example [[practice/26-standing-waves-and-radiation-pressure#261-nodes-in-front-of-a-mirror|26.1 Nodes in front of a mirror]] (easy), [[practice/26-standing-waves-and-radiation-pressure#266-a-mirror-off-the-origin|26.6 A mirror off the origin]] (medium), [[practice/26-standing-waves-and-radiation-pressure#269-is-it-a-standing-wave|26.9 Is it a standing wave]] (hard).

Related: [[concepts/radiation-pressure]] · [[concepts/reflection-and-transmission]] · [[concepts/poynting-vector]] · [[concepts/plane-waves]] · [[concepts/phasors]].
