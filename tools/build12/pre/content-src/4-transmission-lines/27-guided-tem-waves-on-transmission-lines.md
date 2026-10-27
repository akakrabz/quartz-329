---
title: "Lecture 27 — Guided TEM waves on transmission lines"
description: "Two conducting plates confine a plane TEM wave between them. With V = E_x d and I = H_y W, Faraday's and Ampère's laws become the telegrapher's equations, whose d'Alembert solutions travel at v = 1/√(𝓛𝓒) with V/I = ±Z₀ = ±√(𝓛/𝓒)."
tags: [lecture, transmission-lines]
lecture: 27
---

*Lecture 27 · course notes §27 (no slides) · prev: [[3-maxwell-and-waves/26-standing-waves-and-radiation-pressure|Lecture 26]] · next: [[4-transmission-lines/28-distributed-circuits-and-bounce-diagrams|Lecture 28]] · worked problem: [[problems/a-backward-pulse-on-a-parallel-plate-line|A backward pulse on a parallel-plate line]] · practice: [[practice/27-transmission-line-basics|12 problems]]*

> [!abstract] In one breath
> Two conducting plates at $x = 0$ and $x = d$ can hold an $\hat x$-polarized plane wave between them; charges and currents on their facing surfaces end the fields there. With $V = E_xd$ and $I = H_yW$, Faraday's and Ampère's laws become the **telegrapher's equations** $-\partial V/\partial z = \mathcal{L}\,\partial I/\partial t$ and $-\partial I/\partial z = \mathcal{C}\,\partial V/\partial t$. Their solutions are d'Alembert waves, $V = f(t\mp z/v)$ and $I = \pm f/Z_0$, with $v = 1/\sqrt{\mathcal{L}\mathcal{C}} = 1/\sqrt{\mu\epsilon}$ and **characteristic impedance** $Z_0 = \sqrt{\mathcal{L}/\mathcal{C}}$. The power carried is $VI$.

## 1. From a plane wave to a guided wave

The notes start from an $\hat x$-polarized plane TEM wave travelling along $+z$ ([[3-maxwell-and-waves/18-the-wave-equation-and-plane-tem-waves|Lecture 18]]).

- Perfectly conducting plates at $x = 0$ and $x = d$ leave the fields unchanged. Surface charge and current appear on both faces of each plate, as the boundary conditions require ([[3-maxwell-and-waves/16-charge-conservation-displacement-current-and-maxwells-equations#4-boundary-conditions--same-for-dynamics|Lecture 16 §4]]).
- Keep only the charge and current on the two facing surfaces. The fields then exist only between the plates: a **guided wave**.
- Plates of finite width $W$ add a small fringing field at their edges. It is negligible for $W\gg d$, assumed from here on.
- Conversely, wavelike charge and current on the plates produce the guided fields. A voltage or current source at one $z$ launches them; how they spread from there is the subject of the rest of the course.

> [!key] Plate charges and currents (this site's table)
> The notes give $J_{sz} = H_y$ on plate 2. Here $\hat n$ points from each plate into the gap.
>
> | | plate 2, $x = 0$, $\hat n = \hat x$ | plate 1, $x = d$, $\hat n = -\hat x$ |
> |---|---|---|
> | $\rho_s = \hat n\cdot\mathbf{D}$ | $+\epsilon E_x$ | $-\epsilon E_x$ |
> | $\mathbf{J}_s = \hat n\times\mathbf{H}$ | $+\hat z\,H_y$ | $-\hat z\,H_y$ |
>
> What one plate carries, the other returns.

<!-- fig:tl-guided-pulse -->

## 2. Fields to V and I: the telegrapher's equations

Between the plates $\mathbf{E} = \hat xE_x(z,t)$ and $\mathbf{H} = \hat yH_y(z,t)$, uniform in $x$ and $y$. Faraday's and Ampère's laws reduce to

$$
\begin{gathered}
\frac{\partial E_x}{\partial z} = -\mu\frac{\partial H_y}{\partial t},\\[4pt]
-\frac{\partial H_y}{\partial z} = \sigma E_x + \epsilon\frac{\partial E_x}{\partial t}.
\end{gathered}
$$

The notes define two circuit quantities:

- $V\equiv E_xd = \int_0^dE_x\,dx$, the voltage drop from plate 2 to plate 1. It does not depend on the path within a plane of constant $z$: TEM fields have $B_z = 0$, so $\oint\mathbf{E}\cdot d\mathbf{l} = -\tfrac{d}{dt}\int\mathbf{B}\cdot d\mathbf{S} = 0$ around any loop in that plane.
- $I\equiv H_yW$, the current along $+z$ on plate 2 ($J_{sz} = H_y$ across the width $W$).

Multiply both field equations by $d$ and write $H_y = I/W$:

> [!key] Telegrapher's equations
> $$
> \begin{gathered}
> -\frac{\partial V}{\partial z} = \mathcal{L}\frac{\partial I}{\partial t},\qquad -\frac{\partial I}{\partial z} = \mathcal{C}\frac{\partial V}{\partial t} + \mathcal{G}V,\\[6pt]
> \mathcal{L} = \mu\frac dW,\qquad \mathcal{C} = \epsilon\frac Wd,\qquad \mathcal{G} = \sigma\frac Wd .
> \end{gathered}
> $$
> These are the inductance, capacitance and conductance per unit length of the parallel-plate line, found from statics in [[2-magnetostatics/15-inductance-magnetic-energy-and-the-potentials|Lecture 15 §5]] and [[1-electrostatics/10-capacitance-and-conductance|Lecture 10]].

Losses:
- $\mathcal{G}V$ is leakage current through the filling from one plate to the other: an ohmic loss.
- Plates of finite conductivity would add a series term $\mathcal{R}I$ to the right side of the first equation. Perfect plates miss it.
- The notes drop both and study the **ideal lossless line** until the last day of the semester. Heaviside wrote these equations down in the 1880s.

Memory aid (notes): apart from the $-\partial/\partial z$ on the left, they are an inductor's $v = L\,di/dt$ and a capacitor's $i = C\,dv/dt$.

> [!intuition] Two laws in circuit dress (this site's reading)
> - **First equation: Faraday's law.** Take a thin loop in the $xz$ plane: up across the gap at $z$, back down at $z+\Delta z$. Its right-hand normal is $-\hat y$, so it links $\Psi = -\mu H_yd\,\Delta z$. Its emf is $V(z) - V(z+\Delta z) = -d\Psi/dt = \mu d\,\Delta z\,\partial H_y/\partial t$.
> - **Second equation: charge conservation on plate 2.** The plate holds $\rho_sW = \epsilon E_xW = \mathcal{C}V$ per metre. Current arriving minus current leaving, $-\partial I/\partial z$, charges it, and $\mathcal{G}V$ leaks across the gap.

## 3. Wave equation, speed and characteristic impedance

Eliminating $I$ (lossless line):

$$
\frac{\partial^2V}{\partial z^2} = \mathcal{L}\mathcal{C}\,\frac{\partial^2V}{\partial t^2},
$$

the twin of $\partial^2E_x/\partial z^2 = \mu\epsilon\,\partial^2E_x/\partial t^2$ ([[3-maxwell-and-waves/18-the-wave-equation-and-plane-tem-waves#4-the-1d-wave-equation-and-its-solutions|Lecture 18 §4]]). Its solutions are d'Alembert waves.

> [!key] Waves on a lossless line
> $$
> \begin{gathered}
> V = f\Big(t\mp\frac zv\Big),\qquad I = \pm\frac{1}{Z_0}\,f\Big(t\mp\frac zv\Big),\\[6pt]
> v = \frac{1}{\sqrt{\mathcal{L}\mathcal{C}}} = \frac{1}{\sqrt{\mu\epsilon}},\qquad Z_0\equiv\frac{1}{\mathcal{C}v} = \sqrt{\frac{\mathcal{L}}{\mathcal{C}}} .
> \end{gathered}
> $$
> Upper signs: travel toward $+z$; lower signs: toward $-z$. $v$ is the plane-wave speed in the filling. $Z_0$ is the **characteristic impedance** (the notes write $Z_o$).

> [!derivation]- Where I comes from (notes)
> Put $V = f(t\mp z/v)$ into the second equation: $-\partial I/\partial z = \mathcal{C}f'(t\mp z/v)$. Since $\partial f(t\mp z/v)/\partial z = \mp f'/v$, an antiderivative in $z$ is
> $$
> I = \pm\mathcal{C}v\,f\Big(t\mp\frac zv\Big),\qquad \mathcal{C}v = \frac{\mathcal{C}}{\sqrt{\mathcal{L}\mathcal{C}}} = \frac{1}{Z_0}.
> $$
> A constant of integration would be a steady current with no field change; it is set to zero. The first equation checks: $-\partial V/\partial z = \pm f'/v$ and $\mathcal{L}\,\partial I/\partial t = \pm\mathcal{L}f'/Z_0 = \pm\sqrt{\mathcal{L}\mathcal{C}}\,f'$.

Both directions together, by superposition (Lecture 28 starts from this form):

$$
\begin{gathered}
V = f\Big(t-\frac zv\Big) + g\Big(t+\frac zv\Big),\\[4pt]
I = \frac{1}{Z_0}\Big[f\Big(t-\frac zv\Big) - g\Big(t+\frac zv\Big)\Big].
\end{gathered}
$$

The line copies the plane wave of [[3-maxwell-and-waves/18-the-wave-equation-and-plane-tem-waves#5-h-from-e-the-intrinsic-impedance|Lecture 18 §5]] term by term:

| plane wave | line |
|---|---|
| $E_x$, $H_y$ | $V = E_xd$, $I = H_yW$ |
| $\mu$, $\epsilon$ | $\mathcal{L}$, $\mathcal{C}$ |
| $v = 1/\sqrt{\mu\epsilon}$ | $v = 1/\sqrt{\mathcal{L}\mathcal{C}}$, the same number |
| $\eta = \sqrt{\mu/\epsilon}$ | $Z_0 = \sqrt{\mathcal{L}/\mathcal{C}}$ |
| $H_y = (f-g)/\eta$ | $I = (f-g)/Z_0$ |

For the plates, $Z_0 = E_xd/(H_yW) = \eta\,d/W$.

> [!trap] V/I and the sign of Z₀
> - $V/I = +Z_0$ only for a wave toward $+z$. Toward $-z$ it is $-Z_0$; for a sum $f + g$ it is neither.
> - $I$ is the current along $+z$ on conductor 2, the one at higher potential when $V>0$. A backward wave with $V>0$ has $I<0$.
> - $Z_0$ is not a resistance: a lossless line dissipates nothing.

## 4. Other cross-sections: the geometrical factor

Any two-conductor line filled with one homogeneous medium carries the same TEM structure. Its line parameters share one **geometrical factor** GF ([[2-magnetostatics/15-inductance-magnetic-energy-and-the-potentials|Lecture 15]] found $\mathcal{L}\mathcal{C} = \mu\epsilon$ this way):

> [!key] Line parameters from the geometrical factor (notes' margin)
> $$
> \begin{gathered}
> \mathcal{C} = \epsilon\,\text{GF},\qquad \mathcal{L} = \frac{\mu}{\text{GF}},\\[4pt]
> Z_0 = \frac{1}{\text{GF}}\sqrt{\frac\mu\epsilon} = \frac{\eta}{\text{GF}}.
> \end{gathered}
> $$
>
> | line | GF | $Z_0$ |
> |---|---|---|
> | parallel plates, width $W$, gap $d$ | $W/d$ | $\eta\,d/W$ |
> | coax, radii $a<b$ | $2\pi/\ln(b/a)$ | $(\eta/2\pi)\ln(b/a)$ |
> | twin-lead, wire radius $a$, centres $D$ apart | $\pi/\cosh^{-1}(D/2a)$ | $(\eta/\pi)\cosh^{-1}(D/2a)$ |
>
> $\mathcal{L}\mathcal{C} = \mu\epsilon$ for all of them: $v$ depends on the filling only, $Z_0$ on filling and geometry. Coax $\mathcal{C}$: [[1-electrostatics/10-capacitance-and-conductance#3-the-coaxial-cable|Lecture 10 §3]].

<!-- fig:tl-cross-sections -->

> [!example] Example — three common impedances (this site's numbers)
> - Coax in polyethylene ($\epsilon_r = 2.25$, $\eta = 251\ \Omega$) with $b/a = 3.5$: $Z_0 = 50\ \Omega$, as in the [[problems/coax-inductance-and-the-lc-product|coax problem]]. 75 Ω needs $b/a = e^{2\pi\cdot75/251} = 6.5$.
> - Twin-lead in air, 300 Ω: $\cosh^{-1}(D/2a) = 300\pi/377 = 2.50$, so $D = 12.3a$.
> - Plates in air, 50 Ω: $W/d = 377/50 = 7.5$, only marginally "$W\gg d$".
>
> Signals on the polyethylene coax travel at $c/1.5 = 2\times10^8$ m/s, whatever $b/a$.

**Non-TEM modes (notes' margin).** Lines also carry modes with a nonzero $E_z$ or $H_z$.
- At low frequencies these modes are evanescent. Excited at discontinuities, they stay near them.
- The condition is $d<\lambda/2$ for plates and, approximately, $a+b<\lambda/\pi$ for coax, with $\lambda$ the wavelength in the filling.
- Where practical $d$, $a$, $b$ cannot meet it, the notes recommend single-conductor waveguides, which use these modes, instead of two-conductor lines.
- Site's numbers: air plates 1 cm apart stay TEM-only below $c/2d = 15$ GHz. Polyethylene coax with $a = 0.5$ mm, $b = 1.75$ mm does below about 28 GHz by the rule (29 GHz exactly).

## 5. Launching a wave: the battery example (notes)

A 3 V battery is connected at $t = 0$ to an uncharged line ($V = I = 0$ for $t<0$), wire 2 to its $+$ terminal. Wire 2 plays plate 2's role; circuit drawings, here and in Lecture 28, put it on top.

- Electrons leave the $-$ terminal onto wire 1. As many leave wire 2 into the $+$ terminal. So $I$ flows along $+z$ on wire 2 and back toward the battery on wire 1.
- At $t = 0^+$ this current exists only at $z = 0^+$. The rest of the line carries none.
- Electrons at some $z>0$ start to move only after their neighbours at $z^-$ have left, exposing positive charge. So $V$ and $I$ spread from $z = 0$ at the finite speed $v$, like ripples from a pebble dropped in a pond.

Unequal currents along one wire contradict **lumped-circuit analysis**. Lumped analysis is an approximation: it ignores the delays of charge motion, which is fine when wires are short. The telegrapher's equations make the spreading quantitative: **distributed-circuit analysis**.

For an ideal battery on a line long enough that nothing has come back yet, $f(t) = 3u(t)$ V (this site's; [[4-transmission-lines/28-distributed-circuits-and-bounce-diagrams|Lecture 28]] adds the source resistance and the far end):

$$
V = 3\,u\Big(t-\frac zv\Big)\ \text{V},\qquad I = \frac{3}{Z_0}\,u\Big(t-\frac zv\Big)\ \text{A}.
$$

> [!example] Example — the energy behind the front (this site's numbers)
> On a 50 Ω line the battery drives $I = 60$ mA and delivers $VI = 0.18$ W.
> - Each metre the front passes stores $\tfrac12\mathcal{C}V^2 + \tfrac12\mathcal{L}I^2$.
> - The two shares are equal: $\mathcal{L}I^2 = \mathcal{L}V^2/Z_0^2 = \mathcal{C}V^2$.
> - The front advances $v$ metres per second, so the storage rate is $\mathcal{C}V^2v = V^2/Z_0 = VI$. All of the battery's power goes into the growing charged section.

## 6. The distributed-circuit model

Over a short length $\Delta z$ the telegrapher's equations read

$$
\begin{gathered}
-\Delta V\equiv V(z,t) - V(z+\Delta z,t) = \Delta z\,\mathcal{L}\,\frac{\partial I}{\partial t},\\[4pt]
-\Delta I\equiv I(z,t) - I(z+\Delta z,t) = \Delta z\,\mathcal{C}\,\frac{\partial V}{\partial t}.
\end{gathered}
$$

- The first is an inductive drop $\Delta z\,\mathcal{L}\,\partial I/\partial t$ along the current on wire 2.
- The second is a capacitor current $\Delta z\,\mathcal{C}\,\partial V/\partial t$ that leaves wire 2 at a node between $z$ and $z+\Delta z$ and enters wire 1 there.

So each $\Delta z$ is a series inductor $\Delta z\,\mathcal{L}$ followed by a shunt capacitor $\Delta z\,\mathcal{C}$, and the line is a ladder of such sections. The model needs $I(z+\Delta z)\approx I(z)$ and $V(z+\Delta z)\approx V(z)$, which holds only for $\Delta z\ll\lambda$, the shortest wavelength in the $V$ and $I$ waveforms.

<!-- fig:tl-ladder -->

> [!example] Example — when lumped analysis is enough (this site's numbers)
> - Power grid, 60 Hz: $\lambda = c/f = 5000$ km. House wiring is lumped; a 1000 km transmission line is not.
> - A 3 GHz signal on polyethylene coax: $\lambda = 6.7$ cm. A 10 cm cable is already a distributed circuit.

## 7. Power on the line

The Poynting vector $\mathbf{E}\times\mathbf{H} = \hat zE_xH_y$ is uniform over the cross-section $Wd$, so the power carried along $+z$ is

$$
\begin{gathered}
p(z,t) = WdE_xH_y = (E_xd)(H_yW)\\[4pt]
= V(z,t)\,I(z,t),
\end{gathered}
$$

the circuit formula. In sinusoidal steady state, with phasors $\tilde V(z)$ and $\tilde I(z)$ ([[3-maxwell-and-waves/21-monochromatic-waves-and-phasor-notation#7-time-averages-straight-from-phasors|Lecture 21 §7]]):

$$
\langle P\rangle = \tfrac12\text{Re}\{\tilde V\tilde I^*\}.
$$

This site's additions:
- One wave: $p = f^2/Z_0$ toward $+z$; a backward wave has $p = -g^2/Z_0$.
- Both: $VI = (f^2-g^2)/Z_0$. The cross terms cancel, so each wave carries its own power.
- One phasor wave $\tilde V = V^+e^{-j\beta z}$: $\langle P\rangle = \lvert V^+\rvert^2/2Z_0$.

## 8. Summary

- Plates at $x = 0$ and $d$ guide a TEM wave. The facing surfaces carry $\rho_s = \pm\epsilon E_x$ and $\mathbf{J}_s = \pm\hat zH_y$.
- $V = E_xd$ and $I = H_yW$ turn Maxwell's equations into $-\partial V/\partial z = \mathcal{L}\,\partial I/\partial t$ and $-\partial I/\partial z = \mathcal{C}\,\partial V/\partial t\ (+\mathcal{G}V)$.
- Plates: $\mathcal{L} = \mu d/W$, $\mathcal{C} = \epsilon W/d$. Any line: $\mathcal{C} = \epsilon\,\text{GF}$, $\mathcal{L} = \mu/\text{GF}$, $\mathcal{L}\mathcal{C} = \mu\epsilon$.
- $V = f(t-z/v) + g(t+z/v)$ and $I = (f-g)/Z_0$, with $v = 1/\sqrt{\mathcal{L}\mathcal{C}}$ and $Z_0 = \sqrt{\mathcal{L}/\mathcal{C}} = \eta/\text{GF}$.
- A source launches $V$ and $I$ fronts that move at $v$. Lumped analysis fails unless lengths are $\ll\lambda$.
- Ladder model: series $\Delta z\,\mathcal{L}$, shunt $\Delta z\,\mathcal{C}$.
- $p = VI$; $\langle P\rangle = \tfrac12\text{Re}\{\tilde V\tilde I^*\}$.
- Next, Lecture 28: source resistance, loads and bounce diagrams. A load $R$ reflects with $\Gamma = (R-Z_0)/(R+Z_0)$, [[3-maxwell-and-waves/25-wave-reflection-and-transmission|Lecture 25]]'s $\Gamma$ with $Z_0$ for $\eta_1$ and $R$ for $\eta_2$.

Concept pages: [[concepts/telegraphers-equations]] · [[concepts/characteristic-impedance]] · [[concepts/inductance]] · [[concepts/capacitance]] · [[concepts/intrinsic-impedance]] · [[concepts/poynting-vector]].

> [!exam] On exams
> Five Exam 3 items.
> - **SP19 Exam 3 #2**, a filled parallel-plate line: $Z_0 = \eta d/W$; $\mathbf{E}$ from a given plate current through $H_y = I/W$ and $E_x = \eta H_y$; average power as $\langle S\rangle Wd$ or $\lvert\tilde V\rvert^2/2Z_0$. See the [[problems/a-backward-pulse-on-a-parallel-plate-line|worked problem]].
> - **SP17 Exam 3 #2(ii)**, plate voltage, charge and current: test each statement with $B_z = 0$ (§2), $\rho_s = \hat n\cdot\mathbf{D}$ and $\hat n\times\mathbf{H}$ with $\hat n$ into the gap (§1 table).
> - **SP18 Exam 3 #1(ii)**: check each statement against §2 (origin), §3 (solutions) and §6 (which element is in series).
> - **SP18 #1(v)**, $V/I$ with polarity: §3 trap.
> - **FA23 Exam 3 #4(d)**: $\epsilon_r = (c/v)^2$ from a delay.

> [!tip] Practice this lecture
> [[practice/27-transmission-line-basics|12 practice problems]] — 5 easy, 3 medium, 4 hard — each with a folded hint and a worked solution. Start with [[practice/27-transmission-line-basics#271-strip-line-parameters|27.1 Strip-line parameters]]; the [[practice/index|practice hub]] has the whole bank by difficulty and by topic.

### Sources for this page
Kudeki notes, Lecture 27 (8 pages): plates in a plane wave; $V$, $I$ and the telegrapher's equations with $\mathcal{G}$ and the missing $\mathcal{R}$; the wave equation, $Z_0$ and the GF table; the battery example; the ladder model; power and the non-TEM note. Rao (2009) §6.5–6.6 with Table 6.1, and the "Time domain" opening of Ch. 7 before §7.4 (eqs. 7.39–7.47), for cross-checks. This site's own: figures, the plate-source table, the circuit reading, all examples, the power split; numbers checked by script. Slips in the notes ("close-up method", "T-network") are on the errata page.
