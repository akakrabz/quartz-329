<!-- for concepts/poynting-vector, from Lecture 19 §7 -->
<!-- Batch D → E. The Poynting part of Lecture 19 §7 (the sinusoidal sheet). The page already carries the slides'
     S example in its Examples list, so most of this is a dedupe check; the display below is also kept VERBATIM on
     concepts/current-sheet-radiation (the sheet's result), so the L19 loss check does not depend on this merge.
     The lecture page links [[concepts/poynting-vector]] (no anchor). -->

**Aliases to add:** "power density of a plane wave", "E × H".

**Physics (Lecture 19 §7, as the slides introduce S):** travel of a TEM wave is *along* $\mathbf{S}\equiv\mathbf{E}\times\mathbf{H}$ — in the notes this is the definition that pairs $\mathbf{H}$ with $\mathbf{E}$ ([[concepts/plane-waves]]); the slides add that its size is power per area, W/m² (V/m × A/m). For the sheet $\mathbf{J}_s = -J_{s0}\cos(\omega t)\,\hat x$ on $z = 0$ in free space ([[concepts/current-sheet-radiation]]):

$$
\mathbf{S} = \mathbf{E}\times\mathbf{H} = \pm\hat z\,\frac{\eta_0J_{s0}^2}{4}\cos^2(\omega t\mp\beta z)\ \ \text{W/m}^2,\qquad z\gtrless0 .
$$

Outward on both sides and never negative ($\cos^2\ge0$): pulses at twice the source frequency. $\lvert\mathbf{S}\rvert = \lvert\mathbf{E}\rvert^2/\eta_0 = \eta_0\lvert\mathbf{H}\rvert^2$; for $J_{s0} = 1$ A/m the peak is $\eta_0/4 = 94.2$ W/m² per side. The two sides together carry $\eta_0J_s^2/2$, exactly $-\mathbf{J}_s\cdot\mathbf{E}$ at the sheet ($\mathbf{J}_s\cdot\mathbf{E} = -\tfrac\eta2\lvert\mathbf{J}_s\rvert^2<0$: the charges work on the field; in a resistor $\mathbf{J}\cdot\mathbf{E}>0$). Why this is a power density, and its time average: Lecture 20.

**Exam item (Lecture 19):** $\mathbf{S}$ of a sheet's waves — direction away from the sheet on both sides, magnitude $\lvert\mathbf{E}\rvert\lvert\mathbf{H}\rvert = \eta J_s^2/4$ per side.

**Where it appears (add):** [[3-maxwell-and-waves/19-dalembert-solutions-and-radiation-from-current-sheets#7-a-sinusoidal-sheet-current-β-λ-and-the-poynting-vector-slides|Lecture 19 §7]] (named, sheet example); [[3-maxwell-and-waves/18-the-wave-equation-and-plane-tem-waves#5-h-from-e-the-intrinsic-impedance|Lecture 18 §5]] (direction rule only).

**Inline formulas the loss check looks for (all above):** $\lvert\mathbf{S}\rvert = \lvert\mathbf{E}\rvert^2/\eta_0 = \eta_0\lvert\mathbf{H}\rvert^2$, $\eta_0/4 = 94.2$, $\eta_0J_s^2/2$, $J_{s0} = 1$.
