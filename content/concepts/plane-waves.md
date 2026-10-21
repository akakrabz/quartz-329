---
title: "Plane waves"
description: "Uniform plane TEM waves: E = E₀f(t − û·r/v), E₀ ⊥ û, H = û × E/η, at v = 1/√(με)."
tags: [concept, waves]
aliases: ["uniform plane wave", "plane TEM wave", "TEM wave", "travelling wave", "traveling wave"]
---

> [!key] Definition
> $$
> \begin{gathered}
> \mathbf{E} = \hat x\,f\Big(t\mp\frac zv\Big),\qquad \mathbf{H} = \pm\hat y\,\frac1\eta\,f\Big(t\mp\frac zv\Big)\\
> (\text{travel toward }\pm z),\\[6pt]
> \mathbf{E} = \mathbf{E}_0\,f\Big(t-\frac{\hat u\cdot\mathbf{r}}{v}\Big),\qquad \mathbf{H} = \frac1\eta\,\hat u\times\mathbf{E}\\
> (\mathbf{E}_0\perp\hat u;\ \text{travel toward }\hat u),
> \end{gathered}
> $$
> with $v = 1/\sqrt{\mu\epsilon}$, $\eta = \sqrt{\mu/\epsilon}$. *Plane*: uniform over each plane $\hat u\cdot\mathbf{r} = $ const. *TEM*: $\mathbf{E}$, $\mathbf{H}\perp\hat u$. $\mathbf{E}$'s direction: the **polarization**.

**Physics.** Simplest source-free Maxwell solutions (notes: try $\mathbf{E} = \hat xE_x(z,t)$; slides: current sheet). $\mathbf{E}\times\mathbf{H}$ (Poynting) points along $\hat u$; $\lvert\mathbf{B}\rvert = \lvert\mathbf{E}\rvert/v$. Nothing along $\hat u$: $\hat z f(t - z/v)$ has $\nabla\cdot\mathbf{E}\neq0$. Opposite waves, $E_x = Af + Bg$, $H_y = (Af - Bg)/\eta$, make standing waves (Lecture 26). A sheet launches one per face, $\mathbf{E} = -\tfrac\eta2\mathbf{J}_s$, $\mathbf{H} = \tfrac12\mathbf{J}_s\times\hat n$ ([[concepts/current-sheet-radiation]]). Far-field waves look plane.

**Reading a plane wave.** Opposite signs on the $t$ and position terms: toward $+$; same sign: $-$. Coefficient ratio: speed. $E(z,t) = E(0, t\mp z/v) = E(z\mp vt, 0)$ for $\pm z$.

**Monochromatic plane waves and phasors ([[3-maxwell-and-waves/21-monochromatic-waves-and-phasor-notation|Lecture 21]]).** $A\cos(\omega t\mp\beta z)$: $\beta = \omega/v = \omega\sqrt{\mu\epsilon}$, $\lambda = 2\pi/\beta$, $v_p = \omega/\beta = \lambda f$. With $\mathbf{E} = \text{Re}\{\tilde{\mathbf{E}}e^{j\omega t}\}$:
$$
\begin{gathered}
\tilde{\mathbf{E}}(\mathbf{r}) = \tilde{\mathbf{E}}_0\,e^{-j\beta\hat u\cdot\mathbf{r}},\qquad \tilde{\mathbf{H}} = \frac1\eta\,\hat u\times\tilde{\mathbf{E}},\\[4pt]
\langle\mathbf{S}\rangle = \tfrac12\text{Re}\{\tilde{\mathbf{E}}\times\tilde{\mathbf{H}}^*\} = \frac{\lvert\tilde{\mathbf{E}}_0\rvert^2}{2\eta}\,\hat u .
\end{gathered}
$$
$e^{-j\beta\hat u\cdot\mathbf{r}}$: the delay $\hat u\cdot\mathbf{r}/v$ as a phase lag; in $e^{j(ax + by + cz)}$, $(a, b, c) = -\beta\hat u$. Complex components of $\tilde{\mathbf{E}}_0$ give [[concepts/wave-polarization|polarization]] ([[3-maxwell-and-waves/24-signal-transmission-and-circular-polarization|Lecture 24]]); $\lvert\tilde{\mathbf{E}}_0\rvert^2$ adds their powers.

**Examples.**
- $\hat yf(t\mp z/v)$ pairs with $\mp\hat xf/\eta$: $\hat y\times(-\hat x) = +\hat z$.
- Slide 24: $(0.05y - t)^2$ goes $+y$ at 20 m/s; $u(t + 0.02x)$, $-x$ at 50 m/s.
- Slide 26: $-z$ at 100 m/s, $E(200\ \text{m}, 0.2\ \text{s}) = E(0, 2.2\ \text{s}) = 0.9$.
- $\mathbf{E}\parallel\hat z$ toward $+y$ in polyethylene: $\mathbf{H}\parallel\hat y\times\hat z = +\hat x$; 6 V/m with 23.9 mA/m.
- $12\cos(4\pi\times10^8t - \tfrac{8\pi}{3}y)\,\hat z$ V/m, non-magnetic: $f = 200$ MHz, $\lambda = 0.75$ m, $v_p = c/2$ ($\epsilon_r = 4$, $\eta = 60\pi\ \Omega$), $\tilde{\mathbf{H}} = \tfrac{1}{5\pi}e^{-j(8\pi/3)y}\,\hat x$ A/m, $\langle\mathbf{S}\rangle = 0.382\,\hat y$ W/m².
- $\mathbf{H} = \sin(\omega t - \beta z)\,\hat y$: $\tilde{\mathbf{H}} = -je^{-j\beta z}\hat y$, $\tilde{\mathbf{E}} = -j\eta e^{-j\beta z}\hat x$, $\mathbf{E} = \eta\sin(\omega t - \beta z)\,\hat x$.

> [!trap]
> - "$x$-polarized" names $\mathbf{E}$, not the travel.
> - $-z$ reverses $\mathbf{H}$: use $\hat u\times\mathbf{E}/\eta$; relabel axes cyclically only ($x\to y\to z\to x$).
> - At $t = 0$ a $+z$ snapshot is the record mirrored ($-z$: not).
> - $E/H = \pm\eta$ for one wave only.
> - $e^{+j\beta z}$ goes toward $-z$: restore $e^{j\omega t}$ first. A sine's phasor has $-j$.

**Where it appears.** [[3-maxwell-and-waves/18-the-wave-equation-and-plane-tem-waves|Lecture 18]]; [[3-maxwell-and-waves/19-dalembert-solutions-and-radiation-from-current-sheets|Lecture 19]]; [[3-maxwell-and-waves/20-poynting-theorem-and-monochromatic-waves|Lecture 20]]; [[3-maxwell-and-waves/22-phasor-maxwell-equations-and-damped-waves|Lecture 22]]; Lectures 24–26; [[problems/a-pulse-on-the-move]]; [[problems/phasors-e-and-power-from-a-given-h]].

**Practice.** [[practice/topics#plane-waves-and-the-wave-equation|Plane waves and the wave equation]] (25 problems) — for example [[practice/18-wave-equation-and-plane-waves#181-which-way-and-how-fast|18.1 Which way and how fast]] (easy), [[practice/18-wave-equation-and-plane-waves#186-which-fields-can-be-waves|18.6 Which fields can be waves]] (medium), [[practice/18-wave-equation-and-plane-waves#189-triangle-pulse-in-a-magnetic-medium|18.9 Triangle pulse in a magnetic medium]] (hard).

Related: [[concepts/poynting-vector]] · [[concepts/wave-equation]] · [[concepts/intrinsic-impedance]] · [[concepts/maxwells-equations]] · [[concepts/faradays-law]] · [[concepts/displacement-current]] · [[concepts/phasors]] · [[concepts/dispersion-relation]].
