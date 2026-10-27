<!-- for concepts/current-sheet-radiation, from Lecture 20 §6 -->

**Example 1 (notes, Lecture 20) — a cosine current sheet in vacuum.** On $z = 0$, $\mathbf{J}_s = \hat x\,f(t) = \hat x\,2\cos(\omega t)$ A/m, free space both sides. Find (a) $\mathbf{E}$, $\mathbf{H}$ for $z\gtrless0$, (b) $\mathbf{E}\times\mathbf{H}$, (c) $\mathbf{J}_s\cdot\mathbf{E}$ on the sheet.

**(a) The fields.** $\mathbf{E} = -\hat x\,\tfrac\eta2f(t\mp z/v)$, $\mathbf{H} = \mp\hat y\,\tfrac12f(t\mp z/v)$ with $v = c$, $\eta = \eta_0\approx120\pi\ \Omega$; delay shifts the phase:

$$
\begin{gathered}
f\Big(t\mp\frac zc\Big) = 2\cos\Big(\omega t\mp\frac{\omega}{c}z\Big) = 2\cos(\omega t\mp\beta z),\\[4pt]
\beta\equiv\frac\omega c .
\end{gathered}
$$

> [!key] Example 1 (a): the radiated fields
> $$
> \begin{gathered}
> \mathbf{E}(z,t) = -\hat x\,\eta_0\cos(\omega t\mp\beta z)\ \ \text{V/m},\\[4pt]
> \mathbf{H}(z,t) = \mp\hat y\,\cos(\omega t\mp\beta z)\ \ \text{A/m},\quad z\gtrless0 .
> \end{gathered}
> $$
> Upper signs for $z>0$. Amplitudes $\eta_0\cdot2/2 = \eta_0\approx377$ V/m and $2/2 = 1$ A/m.

$\lambda = 2\pi/\beta$. One source frequency in a linear time-invariant medium gives that frequency everywhere: **monochromatic waves** ([[concepts/monochromatic-waves]]), here real cosines; phasor form $\tilde{\mathbf{E}} = -\tfrac\eta2\tilde{\mathbf{J}}_se^{-j\beta d}$ on [[concepts/phasors]].

**(b) The Poynting vectors.**

- $z>0$: $(-\eta_0\cos)(-\cos)\,\hat x\times\hat y = +\hat z\,\eta_0\cos^2(\omega t - \beta z)$;
- $z<0$: $(-\eta_0\cos)(+\cos)\,\hat x\times\hat y = -\hat z\,\eta_0\cos^2(\omega t + \beta z)$.

> [!key] Example 1 (b): the Poynting vectors
> $$
> \begin{gathered}
> \mathbf{S} = \mathbf{E}\times\mathbf{H} = \pm\hat z\,\eta_0\cos^2(\omega t\mp\beta z)\ \ \text{W/m}^2,\\[4pt]
> z\gtrless0 .
> \end{gathered}
> $$

The notes say the *average* points along the travel; for one wave the instantaneous $\mathbf{S}$ does too ($\cos^2\ge0$), since $\mathbf{E}$ and $\mathbf{H}$ flip together. Energy leaves in pulses at $2\omega$: humps $\lambda/2$ apart, moving at $c$.

**(c)** $\mathbf{J}_s\cdot\mathbf{E} = -2\eta_0\cos^2(\omega t)$ W/m² on the sheet (a source); the energy balance at the sheet and the slab is on [[concepts/poynting-theorem]], the averages ($\eta_0/2\approx188$ W/m² per side, $\eta_0\approx377$ W/m² injected) on [[concepts/time-average-power]].

**Where it appears (add):** [[3-maxwell-and-waves/20-poynting-theorem-and-monochromatic-waves#6-the-notes-example-monochromatic-waves-from-a-cosine-sheet|Lecture 20 §6]].
