<!-- for concepts/current-sheet-radiation, from Lecture 22 §7 -->

**The sheet in a conducting medium.** Put the notes' Lecture 21 sheet, $\mathbf{J}_s = \hat x\,J_0\cos\omega t$ on $z = 0$, in a conducting medium ($\gamma = \alpha + j\beta$, complex $\eta$: [[concepts/propagation-constant]]). Lecture 19 §4's boundary-condition argument goes through with $j\beta\to\gamma$:

1. Outgoing waves with the same $\tilde{\mathbf{E}} = \hat x\,Ae^{-\gamma\lvert z\rvert}$ on each face (tangential $\mathbf{E}$ continuous), $\tilde{\mathbf{H}} = \pm\hat y\,(A/\eta)\,e^{-\gamma\lvert z\rvert}$ for $z\gtrless0$.
2. Jump condition ($\hat n = \hat z$): $\hat z\times(\tilde{\mathbf{H}}^+ - \tilde{\mathbf{H}}^-) = \hat z\times\hat y\,(2A/\eta) = -\hat x\,(2A/\eta) = \hat x\,J_0$, so $A = -\eta J_0/2$.

$$
\begin{gathered}
\tilde{\mathbf{E}} = -\hat x\,\frac{\eta J_0}{2}\,e^{-\gamma\lvert z\rvert},\\[6pt]
\tilde{\mathbf{H}} = \mp\hat y\,\frac{J_0}{2}\,e^{-\gamma\lvert z\rvert}\qquad(z\gtrless0).
\end{gathered}
$$

Lecture 19's $\tilde{\mathbf{H}} = \tfrac12\tilde{\mathbf{J}}_s\times\hat n$, $\tilde{\mathbf{E}} = -\tfrac\eta2\tilde{\mathbf{J}}_s$, with $e^{-j\beta\lvert z\rvert}\to e^{-\gamma\lvert z\rvert}$ and complex $\eta$.

> [!example] Example — the sheet in the medium of Lecture 22's decode example
> $\gamma = 1 + j3$ m⁻¹, $\eta = 119.2\,e^{j18.4^\circ}\ \Omega$, $\omega = 3\times10^8$ rad/s, $J_0 = 2$ A/m (the notes' Lecture 21 value):
> $$
> \begin{gathered}
> \mathbf{H} = \mp\hat y\,e^{-\lvert z\rvert}\cos(\omega t - 3\lvert z\rvert)\ \ \text{A/m},\\[4pt]
> \mathbf{E} = -\hat x\,119.2\,e^{-\lvert z\rvert}\cos(\omega t - 3\lvert z\rvert + 18.4^\circ)\ \ \text{V/m}
> \end{gathered}
> $$
> ($z$ in m). Unlike the lossless sheet, both waves fade (by $e$ per metre). $\mathbf{H}$ is still set by the current alone ($\tfrac12J_0 = 1$ A/m at the sheet); the medium sets $\mathbf{E}$, which leads $\mathbf{H}$ by $\tau = 18.4^\circ$ and so is no longer exactly opposite $\mathbf{J}_s$. The power the current gives up, $\langle-\mathbf{J}_s\cdot\mathbf{E}\rangle = \tfrac12\text{Re}\{-\tilde{\mathbf{J}}_s\cdot\tilde{\mathbf{E}}^*\} = \tfrac14J_0^2\,\text{Re}\{\eta\} = 36\pi\approx113$ W/m², carries $\cos\tau$ ($\text{Re}\{\eta\} = \lvert\eta\rvert\cos\tau$); half, 56.5 W/m², enters each side and becomes heat within a few metres. Direction, $z>0$: $(-\hat x)\times(-\hat y) = +\hat z$, away from the sheet ✓.

**Where it appears (add):** [[3-maxwell-and-waves/22-phasor-maxwell-equations-and-damped-waves#7-lecture-19s-current-sheet-in-a-conducting-medium|Lecture 22 §7]] (sheet in a conducting medium).
