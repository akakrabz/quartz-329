---
title: "Worked problem — Two crossed sheets a quarter wave apart"
description: "Two perpendicular sheet currents a quarter wavelength apart in free space: superpose their phasor fields, choose the phase that makes the wave linear, right- or left-circular, check the hand on the far side, and find the power. Modelled on Summer 2020 FE #4, re-parameterized: λ/4 spacing instead of λ/2, sheets on z-planes, 0.1 A/m, and a new part on the other side."
tags: [problem, waves]
---

*Problem · style of Summer 2020 FE #4 · uses [[3-maxwell-and-waves/24-signal-transmission-and-circular-polarization|Lecture 24]], [[3-maxwell-and-waves/19-dalembert-solutions-and-radiation-from-current-sheets|Lecture 19]], [[3-maxwell-and-waves/21-monochromatic-waves-and-phasor-notation|Lecture 21]] · concepts: [[concepts/wave-polarization]], [[concepts/current-sheet-radiation]], [[concepts/phasors]]*

> [!question] Problem
> Two current sheets in free space carry, in A/m,
> $$
> \begin{gathered}
> \text{sheet A, } z = 0:\ \ \mathbf{J}_s = 0.1\cos(\omega t)\,\hat x,\\[4pt]
> \text{sheet B, } z = \lambda/4:\ \ \mathbf{J}_s = 0.1\cos(\omega t+\phi)\,\hat y,
> \end{gathered}
> $$
> with $f = 300$ MHz and $\phi$ real. Use $\eta_0 = 120\pi\ \Omega$ and $c = 3\times10^8$ m/s.
>
> (a) Write the total field in $z>\lambda/4$ as $\tilde{\mathbf{E}} = Pe^{-j\beta z}(\hat x + Q\hat y)$. Find $\beta$, $P$ and $Q(\phi)$.
>
> (b) For which $\phi$ in $[0, 2\pi)$ is the wave in $z>\lambda/4$ linear, right-circular, left-circular?
>
> (c) Take the right-circular $\phi$ of (b). What is the polarization in $z<0$?
>
> (d) Find $\langle\mathbf{S}\rangle$ in $z>\lambda/4$ for the cases of (b).

## (a) Superpose the two sheets

A sheet on $z = z_0$ with phasor $\tilde{\mathbf{J}}_s$ radiates $\tilde{\mathbf{E}} = -\tfrac{\eta_0}2\tilde{\mathbf{J}}_se^{-j\beta\lvert z-z_0\rvert}$ on both sides ([[3-maxwell-and-waves/19-dalembert-solutions-and-radiation-from-current-sheets|Lecture 19]] in phasor form). Here $\beta = 2\pi f/c = 2\pi$ rad/m, $\lambda = 1$ m and $\beta\lambda/4 = \pi/2$. With $\tfrac{\eta_0}2(0.1) = 6\pi$ V/m, for $z>\lambda/4$:

$$
\begin{gathered}
\tilde{\mathbf{E}}_A = -6\pi\,\hat x\,e^{-j\beta z},\\[4pt]
\tilde{\mathbf{E}}_B = -6\pi e^{j\phi}\,\hat y\,e^{-j\beta(z-\lambda/4)}\\[4pt]
= -6\pi\,e^{j(\phi+\pi/2)}\,\hat y\,e^{-j\beta z}.
\end{gathered}
$$

Sheet B is a quarter wavelength closer to every point beyond it, so its wave arrives with a phase advance of $\pi/2$.

> [!key] Answer (a)
> $\beta = 2\pi$ rad/m and $\tilde{\mathbf{E}} = -6\pi e^{-j\beta z}(\hat x + je^{j\phi}\hat y)$ V/m: $P = -6\pi\approx-18.8$ V/m, $Q = je^{j\phi} = e^{j(\phi+\pi/2)}$.

## (b) Choose the phase

The wave travels along $+\hat z$ and $\lvert Q\rvert = 1$. Lecture 24 §5: $Q$ real is linear, $Q = -j$ right-circular, $Q = +j$ left-circular.

- **Linear:** $\phi + \pi/2 = 0$ or $\pi$ (mod $2\pi$). $\phi = \pi/2$ gives $Q = -1$ (along $\hat x - \hat y$); $\phi = 3\pi/2$ gives $Q = 1$ (along $\hat x + \hat y$).
- **Right-circular:** $e^{j(\phi+\pi/2)} = e^{-j\pi/2}$, so $\phi = \pi$.
- **Left-circular:** $e^{j(\phi+\pi/2)} = e^{j\pi/2}$, so $\phi = 0$.

Check $\phi = \pi$ with the hand recipe: $\tilde{\mathbf{E}} = -6\pi(\hat x - j\hat y)e^{-j\beta z}$, so at $z = \lambda = 1$ m (where $e^{-j\beta z} = 1$), $\mathbf{E}(0) = -6\pi\hat x$ and $\mathbf{E}(T/4) = -\text{Im}\{\tilde{\mathbf{E}}\} = -6\pi\hat y$. Then $\mathbf{E}(0)\times\mathbf{E}(T/4) = 36\pi^2\hat z$, along the travel: right-handed. In the time domain, $\mathbf{E} = -6\pi[\cos(\omega t-\beta z)\,\hat x + \sin(\omega t-\beta z)\,\hat y]$ V/m.

> [!key] Answer (b)
> Linear: $\phi = \pi/2$ (along $\hat x - \hat y$) or $3\pi/2$ (along $\hat x + \hat y$). Right-circular: $\phi = \pi$. Left-circular: $\phi = 0$. In-phase currents give a left-circular wave: the spacing alone supplies the 90°.

> [!trap]
> - Dropping the $e^{+j\beta\lambda/4} = j$ of the offset sheet puts every answer a quarter cycle off.
> - $e^{-j\beta(z-\lambda/4)} = e^{-j\beta z}e^{+j\pi/2}$: the shift has a plus sign.
> - The common factor $-6\pi$ turns the picture by 180°; it does not change the hand.

## (c) The other side

For $z<0$ both waves travel toward $-z$, as $e^{+j\beta(z-z_0)}$:

$$
\begin{gathered}
\tilde{\mathbf{E}} = -6\pi\big[\hat x + e^{j(\phi-\pi/2)}\hat y\big]e^{j\beta z}\\[4pt]
\overset{\phi=\pi}{=}\ -6\pi(\hat x + j\hat y)e^{j\beta z}\ \text{V/m}.
\end{gathered}
$$

Recipe at $z = 0$: $\hat u = -\hat z$, $\mathbf{E}(0) = -6\pi\hat x$, $\mathbf{E}(T/4) = -\text{Im}\{\tilde{\mathbf{E}}\} = 6\pi\hat y$, so $\mathbf{E}(0)\times\mathbf{E}(T/4) = -36\pi^2\hat z$, again along $\hat u$.

> [!key] Answer (c)
> $\tilde{\mathbf{E}} = -6\pi(\hat x + j\hat y)e^{j\beta z}$ V/m, travelling toward $-z$: **right-circular** as well.

The notes' Example 2, one rotating sheet, gives opposite hands on its two sides. Here the offset adds $+\pi/2$ to sheet B's phase on one side and $-\pi/2$ on the other. The rotation reverses together with the travel direction, so the hand is the same.

## (d) Power

$\langle\mathbf{S}\rangle = \lvert\tilde{\mathbf{E}}\rvert^2\hat z/2\eta_0$ (Lecture 24 §8):

$$
\langle\mathbf{S}\rangle = \frac{(6\pi)^2(1+\lvert Q\rvert^2)}{2\cdot120\pi}\,\hat z = 0.3\pi\,\hat z\ \text{W/m}^2 .
$$

> [!key] Answer (d)
> $\langle\mathbf{S}\rangle = 0.3\pi\,\hat z\approx0.94\ \text{W/m}^2$ in all four cases. Each sheet alone gives $0.15\pi$; perpendicular components add their powers whatever $\phi$ is.

## The pattern

1. Each sheet: $-\tfrac\eta2\tilde{\mathbf{J}}_se^{-j\beta\lvert z-z_0\rvert}$.
2. Factor out the common exponential; the offsets become phases $e^{\pm j\beta z_0}$.
3. Read $Q$: real is linear; $\mp j$ is right/left-circular for $+z$ travel (swap for $-z$).
4. Power from $\lvert\tilde{\mathbf{E}}\rvert^2/2\eta$.

Summer 2020 FE #4 puts the sheets $\lambda/2$ apart on $x$-planes, so the offset there only flips a sign. Here $\lambda/4$ supplies a 90° shift of its own, and part (c) adds the far side.
