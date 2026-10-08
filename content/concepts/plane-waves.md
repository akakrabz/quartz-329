---
title: "Plane waves"
description: "A uniform plane wave has the same field everywhere on each plane perpendicular to its direction of travel û: E = E₀ f(t − û·r/v) with E₀ ⊥ û, and H = û × E/η. E, H and û form a right-handed set, the waveform f is arbitrary, and the whole pattern travels without distortion at v = 1/√(με)."
tags: [concept, waves]
aliases: ["uniform plane wave", "plane TEM wave", "TEM wave", "travelling wave", "traveling wave", "polarization of a wave"]
---

> [!key] Definition
> $$
> \begin{gathered}
> \mathbf{E} = \hat x\,f\Big(t\mp\frac zv\Big),\qquad \mathbf{H} = \pm\hat y\,\frac1\eta\,f\Big(t\mp\frac zv\Big)\qquad(\text{travel toward }\pm z),\\[6pt]
> \mathbf{E} = \mathbf{E}_0\,f\Big(t-\frac{\hat u\cdot\mathbf{r}}{v}\Big),\quad \mathbf{E}_0\perp\hat u,\qquad \mathbf{H} = \frac1\eta\,\hat u\times\mathbf{E}\qquad(\text{travel toward }\hat u),
> \end{gathered}
> $$
> with $v = 1/\sqrt{\mu\epsilon}$ and $\eta = \sqrt{\mu/\epsilon}$. *Plane* (uniform): the field has the same value at every point of each plane $\hat u\cdot\mathbf{r} = $ const. *TEM* (transverse electromagnetic): $\mathbf{E}$ and $\mathbf{H}$ are both perpendicular to $\hat u$. The direction of $\mathbf{E}$ is the wave's **polarization**: $\hat x\,f$ is "$x$-polarized".

**Physics.** These are the simplest solutions of the source-free Maxwell equations. The notes find them by trying $\mathbf{E} = \hat xE_x(z,t)$. The slides find them as the field of an infinite current sheet, where symmetry leaves only $E_x(z,t)$ and $H_y(z,t)$. Their properties:

- $\mathbf{E}\perp\mathbf{H}$, both perpendicular to $\hat u$, with $\mathbf{E}\times\mathbf{H}$ along $\hat u$. That vector is the Poynting vector, whose meaning as power per unit area comes in Lecture 20.
- $\lvert\mathbf{E}\rvert/\lvert\mathbf{H}\rvert = \eta$ and $\lvert\mathbf{B}\rvert = \lvert\mathbf{E}\rvert/v$ for a single wave.
- Any waveform, carried rigidly at speed $v$.

No component can lie along $\hat u$: $\hat z f(t - z/v)$ has $\nabla\cdot\mathbf{E}\neq0$. Waves travelling in opposite directions superpose: $E_x = Af + Bg$, $H_y = (Af - Bg)/\eta$. Then $E_x/H_y$ is no longer $\pm\eta$; that is the beginning of standing waves (Lecture 26). An infinite current sheet radiates one plane wave from each face, with $\mathbf{E} = -\tfrac\eta2\mathbf{J}_s$ and $\mathbf{H} = \tfrac12\mathbf{J}_s\times\hat n$ delayed by the travel time ([[3-maxwell-and-waves/19-dalembert-solutions-and-radiation-from-current-sheets|Lecture 19]], [[concepts/current-sheet-radiation]]). A compact antenna radiates spherical waves instead (ECE 450), but over a region small compared with its distance from the source a spherical wave looks like a plane wave. That is why plane waves model radio links and light beams.

**Reading a plane wave.** $f(t - \hat u\cdot\mathbf{r}/v)$ travels toward $+\hat u$. The relative sign of the $t$ term and the position term gives the direction: opposite signs mean $+$, the same sign means $-$. The ratio of their coefficients gives the speed. A record at one place and a snapshot at one time are related by $E(z,t) = E(0, t\mp z/v) = E(z\mp vt, 0)$ for travel toward $\pm z$. Put $t = 0$: a $+z$ snapshot is the time record *mirrored*, and a $-z$ snapshot is not.

**Examples.**
- The four $z$-travelling cases: $\hat xf(t - z/v)$ with $+\hat y f/\eta$; $\hat xf(t + z/v)$ with $-\hat y f/\eta$; $\hat yf(t - z/v)$ with $-\hat x f/\eta$; $\hat yf(t + z/v)$ with $+\hat x f/\eta$. Each is checked by $\mathbf{E}\times\mathbf{H}$; for the third, $\hat y\times(-\hat x) = +\hat z$ matches travel toward $+z$.
- Slide 24: $(0.05y - t)^2$ travels toward $+y$ at 20 m/s and $u(t + 0.02x)$ toward $-x$ at 50 m/s.
- Slide 26: a $-z$ wave at 100 m/s has $E(200\ \text{m}, 0.2\ \text{s}) = E(0, 2.2\ \text{s}) = 0.9$.
- Worked problem: a ramp pulse with $\mathbf{E}\parallel\hat z$ travelling toward $+y$ in polyethylene has $\mathbf{H} = \hat y\times\mathbf{E}/\eta\parallel+\hat x$, with 6 V/m paired with 23.9 mA/m.

> [!trap]
> - "$x$-polarized" names the direction of $\mathbf{E}$, not the direction of travel.
> - Travel toward $-z$ reverses $\mathbf{H}$ relative to $\mathbf{E}$ ($H_y = -g/\eta$). Get $\mathbf{H}$ from $\hat u\times\mathbf{E}/\eta$ instead of memorizing.
> - The $\pm z$ sign table carries over to another axis only by a cyclic relabelling ($x\to y\to z\to x$); swapping two letters reverses $\mathbf{H}$. For travel along $+y$ with $\mathbf{E}\parallel\hat z$, $\mathbf{H}\parallel\hat y\times\hat z = +\hat x$. Check $\mathbf{E}\times\mathbf{H}$ at the end.
> - A snapshot is not a record. For $+z$ travel one is the other reversed left-to-right.
> - $E/H = \pm\eta$ holds for one travelling wave, not for a superposition.

**Where it appears.** [[3-maxwell-and-waves/18-the-wave-equation-and-plane-tem-waves|Lecture 18]] (derived, the sign table, reading waves); [[3-maxwell-and-waves/19-dalembert-solutions-and-radiation-from-current-sheets|Lecture 19]] ("uniform plane TEM waves" named, launched by current sheets); Lecture 20 (Poynting vector, monochromatic waves); Lecture 24 (circular polarization); Lectures 25–26 (reflection and standing waves); [[problems/a-pulse-on-the-move]].

**Practice.** [[practice/topics#plane-waves-and-the-wave-equation|Plane waves and the wave equation]] (20 problems) — for example [[practice/18-wave-equation-and-plane-waves#181-which-way-and-how-fast|18.1 Which way and how fast]] (easy), [[practice/18-wave-equation-and-plane-waves#186-which-fields-can-be-waves|18.6 Which fields can be waves]] (medium), [[practice/18-wave-equation-and-plane-waves#189-triangle-pulse-in-a-magnetic-medium|18.9 Triangle pulse in a magnetic medium]] (hard).

Related: [[concepts/current-sheet-radiation]] · [[concepts/poynting-vector]] · [[concepts/wave-equation]] · [[concepts/intrinsic-impedance]] · [[concepts/maxwells-equations]] · [[concepts/faradays-law]] · [[concepts/displacement-current]].
