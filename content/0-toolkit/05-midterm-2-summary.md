---
title: "Midterm 2 — equation summary"
description: "Everything since Exam 1 on one page, mostly equations: material models, magnetostatics, Faraday and inductance, the complete Maxwell equations, magnetic media, plane waves and current-sheet radiation — with the sign rules, the canonical fields, the traps, and a study plan."
tags: [toolkit, exam-2]
aliases: ["Midterm 2", "Exam 2 summary", "Exam 2 formula sheet"]
---

*Scope assumed here: Lectures 11–19, everything after Exam 1 — check the course page for the official list. Exam 1 tools (Gauss, potential, boundary conditions, capacitance) are still needed and are summarized in [[#9-what-you-still-need-from-unit-1|§9]]. Each section links to the lecture that derives it; this page only collects.*

> [!recipe] How to use this page
> Read a section, close the page, and rewrite its equations from memory on scrap paper — then check. The gaps you find are your study list. Every equation here has a sign or direction rule next to it; the rule is the part that costs points.

## 1. The whole picture: Maxwell's equations

| law | integral form | differential form | lecture |
|---|---|---|---|
| Gauss | $\oint_S\mathbf{D}\cdot d\mathbf{S} = Q_{\text{enc}}$ | $\nabla\cdot\mathbf{D} = \rho$ | 2–4 |
| no monopoles | $\oint_S\mathbf{B}\cdot d\mathbf{S} = 0$ | $\nabla\cdot\mathbf{B} = 0$ | 3, 4 |
| Faraday | $\oint_C\mathbf{E}\cdot d\mathbf{l} = -\dfrac{d}{dt}\displaystyle\int_S\mathbf{B}\cdot d\mathbf{S}$ | $\nabla\times\mathbf{E} = -\dfrac{\partial\mathbf{B}}{\partial t}$ | 14 |
| Ampère–Maxwell | $\oint_C\mathbf{H}\cdot d\mathbf{l} = \displaystyle\int_S\Big(\mathbf{J}+\dfrac{\partial\mathbf{D}}{\partial t}\Big)\cdot d\mathbf{S}$ | $\nabla\times\mathbf{H} = \mathbf{J}+\dfrac{\partial\mathbf{D}}{\partial t}$ | 12, 16 |
| continuity | $\oint_S\mathbf{J}\cdot d\mathbf{S} = -\dfrac{dQ_{\text{enc}}}{dt}$ | $\nabla\cdot\mathbf{J} = -\dfrac{\partial\rho}{\partial t}$ | 16 |

$$
\begin{gathered}
\mathbf{D} = \epsilon_0\mathbf{E}+\mathbf{P} = \epsilon\mathbf{E},\qquad \mathbf{B} = \mu_0(\mathbf{H}+\mathbf{M}) = \mu\mathbf{H},\\[4pt]
\mathbf{J} = \sigma\mathbf{E},\qquad \mathbf{F} = q(\mathbf{E}+\mathbf{v}\times\mathbf{B}).
\end{gathered}
$$

Static fields: drop every $\partial/\partial t$ and the electric and magnetic halves decouple. Electrostatics is curl-free with sources in the divergence; magnetostatics is divergence-free with sources in the curl ([[2-magnetostatics/index#the-dictionary-electrostatics--magnetostatics|the dictionary]]).

## 2. Where σ and χe come from (Lecture 11)

[[1-electrostatics/11-lorentz-drude-models-for-conductivity-and-susceptibility|Lecture 11]]

| quantity | formula | note |
|---|---|---|
| drift velocity | $\mathbf{v} = \dfrac{q\tau}{m}\mathbf{E}$, mobility $\lvert q\tau/m\rvert$ | $\tau = 1/\nu$ = collision time ($\sim10^{-14}$ s), *not* $\epsilon/\sigma$ |
| conductivity | $\sigma = \displaystyle\sum_s\frac{N_sq_s^2\tau_s}{m_s}$, $\ \mathbf{J} = Nq\mathbf{v} = \sigma\mathbf{E}$ | every species adds ($q^2>0$) |
| AC conductivity | $\sigma(\omega) = \dfrac{\sigma_{\text{DC}}}{1+j\omega/\nu}$ | phasor ($e^{j\omega t}$); DC value for $\omega\ll\nu$ |
| susceptibility | $\chi_e = \dfrac{N_de^2/(m\epsilon_0)}{\omega_0^2}$, $\ \epsilon_r = 1+\chi_e$ | Lorentz (bound) electron |
| polarization current | $\mathbf{J}_p = \dfrac{\partial\mathbf{P}}{\partial t}$ | AC current through a perfect insulator |

## 3. Magnetostatics (Lectures 12–13)

[[2-magnetostatics/12-magnetic-force-biot-savart-and-amperes-law|Lecture 12]] · [[2-magnetostatics/13-current-sheets-solenoids-and-the-vector-potential|Lecture 13]]

$$
\begin{gathered}
\mathbf{F} = q\mathbf{v}\times\mathbf{B},\qquad d\mathbf{F} = I\,d\mathbf{l}\times\mathbf{B},\\[4pt]
\frac{F}{\ell} = \frac{\mu_0I_1I_2}{2\pi d}\ \ (\text{parallel currents attract}),\\[4pt]
d\mathbf{B} = \frac{\mu_0}{4\pi}\frac{I\,d\mathbf{l}\times\hat R}{R^2}\ \ (\hat R\ \text{from source to field point}),\\[4pt]
\oint_C\mathbf{H}\cdot d\mathbf{l} = I_{\text{enc}}\ \ (\text{right-hand rule fixes the sign}).
\end{gathered}
$$

**The canonical fields** — know these cold; Ampère's law with the right path reproduces each in three lines.

| source | field | path / method |
|---|---|---|
| long wire $I$ | $\mathbf{H} = \dfrac{I}{2\pi r}\hat\phi$ | circle |
| thick wire, uniform $J$, radius $a$ | $H_\phi = \dfrac{Ir}{2\pi a^2}$ inside, $\dfrac{I}{2\pi r}$ outside | circle |
| coax ($+I$ inner, $-I$ outer) | $H_\phi = \dfrac{I}{2\pi r}$ between, $0$ outside | circle |
| sheet $\mathbf{J}_s$ [A/m] | $\mathbf{H} = \tfrac12\mathbf{J}_s\times\hat n$, $\hat n$ toward the field point | rectangle; flips across the sheet |
| slab $J_0$, width $W$ | ramp $J_0x$ inside ($x$ from the centre), $\pm J_0W/2$ outside | rectangle straddling the centre |
| solenoid, $n$ turns/m | $\mathbf{H} = nI\,\hat z$ inside, $0$ outside | rectangle |
| toroid, $N$ turns | $H_\phi = \dfrac{NI}{2\pi r}$ inside the core | circle |
| loop radius $a$, on axis | $B_z = \dfrac{\mu_0Ia^2}{2(a^2+z^2)^{3/2}}$, centre $\dfrac{\mu_0I}{2a}$ | Biot–Savart |
| far from a loop (dipole) | $\mathbf{m} = I\mathbf{A}$; axial $B = \dfrac{\mu_0m}{2\pi\lvert z\rvert^3}$ | $1/r^3$, like the electric dipole |

**Vector potential:** $\mathbf{B} = \nabla\times\mathbf{A}$ [Wb/m], $\nabla^2\mathbf{A} = -\mu_0\mathbf{J}$, $\mathbf{A} = \displaystyle\int\frac{\mu_0\mathbf{J}\,dV'}{4\pi R}$ (each current element contributes along its own direction, as each charge contributes to $V$); $\oint_C\mathbf{A}\cdot d\mathbf{l} = \Psi$ through $C$.

## 4. Faraday's law and emf (Lecture 14)

[[2-magnetostatics/14-faradays-law-and-induced-emf|Lecture 14]]

$$
\begin{gathered}
\mathcal{E} = \oint_C(\mathbf{E}+\mathbf{v}\times\mathbf{B})\cdot d\mathbf{l} = -\frac{d\Psi}{dt},\\[4pt]
\Psi = \int_S\mathbf{B}\cdot d\mathbf{S}\quad(d\mathbf{S}\ \text{from the sense of } C).
\end{gathered}
$$

| situation | emf |
|---|---|
| fixed loop, changing $\mathbf{B}$ (transformer) | $-\displaystyle\int_S\frac{\partial\mathbf{B}}{\partial t}\cdot d\mathbf{S}$ |
| bar of length $\ell$ sliding at $v$ in uniform $B$ | $vB\ell$ (motional: $\int(\mathbf{v}\times\mathbf{B})\cdot d\mathbf{l}$ along the bar) |
| $N$-turn loop of area $A$ turning at $\omega$ in uniform $B$ | $\Psi = BA\cos\omega t$ per turn, $\ \mathcal{E} = -N\,d\Psi/dt = NBA\omega\sin\omega t$ |
| rod of length $L$ spinning about one end | $\tfrac12B\omega L^2$ |
| loop moving through non-uniform $B$ | $-d\Psi/dt$ with $\Psi(t)$ computed at each position |

**Lenz:** the induced current makes a field that opposes the *change* of flux. Check every sign with it. **Voltmeters:** a meter reads $\int\mathbf{E}\cdot d\mathbf{l}$ along *its own leads*; two meters on the same two points can read different values when their leads enclose changing flux.

## 5. Inductance, energy, potentials (Lecture 15)

[[2-magnetostatics/15-inductance-magnetic-energy-and-the-potentials|Lecture 15]]

$$
\begin{gathered}
L = \frac{N\Psi}{I},\qquad M_{21} = \frac{N_2\Psi_{21}}{I_1} = M_{12},\\[4pt]
V = L\frac{dI}{dt}\ (\text{drop along } I),\qquad W = \tfrac12LI^2 = \int\tfrac12\mu H^2\,dV .
\end{gathered}
$$

| geometry | inductance |
|---|---|
| long solenoid ($n$ turns/m, area $A$, length $\ell$) | $L = n^2\mu A\ell = N^2\mu A/\ell$ |
| toroid, rectangular cross-section (height $h$, radii $a<b$) | $L = \dfrac{\mu N^2h}{2\pi}\ln\dfrac ba$ |
| coax (per metre) | $\mathcal{L} = \dfrac{\mu}{2\pi}\ln\dfrac ba$ |
| parallel plates, width $W$, gap $d$ (per metre) | $\mathcal{L} = \dfrac{\mu d}{W}$ |
| inside a round wire (per metre) | $\mathcal{L}_{\text{int}} = \dfrac{\mu}{8\pi}$ |
| any two-conductor line | $\mathcal{L}\mathcal{C} = \mu\epsilon$ |

**RL circuit:** $\tau = L/R$; decay $I_0e^{-t/\tau}$, rise $\tfrac{V}{R}(1-e^{-t/\tau})$. **Potentials:** $\mathbf{B} = \nabla\times\mathbf{A}$, $\mathbf{E} = -\nabla\Phi-\partial\mathbf{A}/\partial t$; gauge change $\mathbf{A}' = \mathbf{A}+\nabla\lambda$, $\Phi' = \Phi-\partial\lambda/\partial t$ leaves $\mathbf{E}$ and $\mathbf{B}$ unchanged.

## 6. Displacement current and boundary conditions (Lecture 16)

[[3-maxwell-and-waves/16-charge-conservation-displacement-current-and-maxwells-equations|Lecture 16]]

Displacement current density $\partial\mathbf{D}/\partial t$ [A/m²]; through a capacitor gap it equals the wire current. In a lossy medium with $E_0\cos\omega t$: conduction/displacement amplitude ratio $= \sigma/(\omega\epsilon)$.

$$
\begin{gathered}
\hat n\cdot(\mathbf{D}_1-\mathbf{D}_2) = \rho_s,\qquad \hat n\cdot(\mathbf{B}_1-\mathbf{B}_2) = 0,\\[4pt]
\hat n\times(\mathbf{E}_1-\mathbf{E}_2) = 0,\qquad \hat n\times(\mathbf{H}_1-\mathbf{H}_2) = \mathbf{J}_s,\\[4pt]
\hat n\ \text{from medium 2 into medium 1}.
\end{gathered}
$$

**Perfect conductor** (medium 2, $\mathbf{E} = \mathbf{H} = 0$ inside): just outside, $\mathbf{E}$ is normal and $\mathbf{H}$ is tangential; $\rho_s = \hat n\cdot\mathbf{D}_1$, $\mathbf{J}_s = \hat n\times\mathbf{H}_1$.

## 7. Magnetic materials (Lecture 17)

[[3-maxwell-and-waves/17-magnetization-and-maxwells-equations-in-matter|Lecture 17]]

$$
\begin{gathered}
\mathbf{m} = I\mathbf{A}\ [\text{A}\cdot\text{m}^2],\qquad \mathbf{T} = \mathbf{m}\times\mathbf{B},\\[4pt]
\mathbf{M} = N\mathbf{m}\ [\text{A/m}],\\[4pt]
\mathbf{J}_M = \nabla\times\mathbf{M},\qquad \mathbf{J}_{sM} = \mathbf{M}\times\hat n_{\text{out}},\\[4pt]
\mathbf{H} = \frac{\mathbf{B}}{\mu_0}-\mathbf{M},\qquad \mathbf{M} = \chi_m\mathbf{H},\\[4pt]
\mathbf{B} = \mu\mathbf{H},\qquad \mu = \mu_0(1+\chi_m) = \mu_r\mu_0 .
\end{gathered}
$$

- **Free currents set $\mathbf{H}$; the material sets $\mathbf{B}$.** A core in a long solenoid or toroid keeps the same $H$ ($nI$; $NI/2\pi r$ in a toroid) and multiplies $B$ (and $L$) by $\mu_r$.
- Diamagnets $\chi_m\approx-10^{-5}$, paramagnets $\approx+10^{-5}$ to $10^{-3}$, ferromagnets $\chi_m\gg1$ (non-linear, hysteresis: remanence $B_r$, coercive field $H_c$).
- At an interface with no free current: $B_n$ continuous ($\mu_1H_{1n} = \mu_2H_{2n}$), $H_t$ continuous, and $\dfrac{\tan\theta_1}{\tan\theta_2} = \dfrac{\mu_1}{\mu_2}$ (angles from the normal). Field lines leave iron almost perpendicular to its surface.
- Twins: $\mathbf{P}\leftrightarrow\mathbf{M}$, $-\nabla\cdot\mathbf{P}\leftrightarrow\nabla\times\mathbf{M}$, $\mathbf{P}\cdot\hat n\leftrightarrow\mathbf{M}\times\hat n$, but $\mathbf{P} = \epsilon_0\chi_e\mathbf{E}$ while $\mathbf{M} = \chi_m\mathbf{H}$ (no $\mu_0$).

## 8. Plane waves and current sheets (Lectures 18–19)

[[3-maxwell-and-waves/18-the-wave-equation-and-plane-tem-waves|Lecture 18]] · [[3-maxwell-and-waves/19-dalembert-solutions-and-radiation-from-current-sheets|Lecture 19]]

$$
\begin{gathered}
\nabla^2\mathbf{E} = \mu\epsilon\frac{\partial^2\mathbf{E}}{\partial t^2},\qquad E_x = Af\Big(t-\frac zv\Big)+Bg\Big(t+\frac zv\Big),\\[4pt]
H_y = \frac1\eta\Big[Af\Big(t-\frac zv\Big)-Bg\Big(t+\frac zv\Big)\Big],\\[4pt]
v = \frac{1}{\sqrt{\mu\epsilon}} = \frac{c}{\sqrt{\mu_r\epsilon_r}},\qquad \eta = \sqrt{\frac\mu\epsilon} = \eta_0\sqrt{\frac{\mu_r}{\epsilon_r}},\\[4pt]
c\approx3\times10^8\ \text{m/s} = 300\ \text{m}/\mu\text{s},\qquad \eta_0\approx120\pi\approx377\ \Omega .
\end{gathered}
$$

- **Direction:** $t - z/v$ travels toward $+z$; $t + z/v$ toward $-z$. Speed = coefficient of $t$ divided by coefficient of position.
- **H from E:** $\mathbf{H} = \dfrac1\eta\,\hat u\times\mathbf{E}$, $\mathbf{E} = \eta\,\mathbf{H}\times\hat u$, $\mathbf{E}\times\mathbf{H}$ along the travel $\hat u$; $\lvert\mathbf{B}\rvert = \lvert\mathbf{E}\rvert/v$. Write the cross product out every time.
- **Moving pulses:** toward $+z$, $E(z,t) = E(0,\,t-z/v) = E(z-vt,\,0)$; toward $-z$ swap the signs. A snapshot of a $+z$ wave is its time record mirrored.
- **Current sheet** $\mathbf{J}_s(t)$ on a plane, distance $\xi$ from it, $\hat n$ pointing away from the sheet: $\mathbf{E}$ is the same on both sides and opposes $\mathbf{J}_s$; $\mathbf{H}$ flips across the sheet.

$$
\begin{gathered}
\mathbf{E} = -\frac\eta2\,\mathbf{J}_s\Big(t-\frac{\lvert\xi\rvert}{v}\Big),\\[4pt]
\mathbf{H} = \frac12\,\mathbf{J}_s\Big(t-\frac{\lvert\xi\rvert}{v}\Big)\times\hat n .
\end{gathered}
$$

- **Cosine waves (real, no phasors):** $\cos(\omega t\mp\beta z)$ with $\beta = \omega/v$ [rad/m], $\lambda = 2\pi/\beta = v/f$, $v_p = \omega/\beta$, $f = \omega/2\pi$.
- **Poynting vector:** $\mathbf{S} = \mathbf{E}\times\mathbf{H}$ [W/m²], along the travel, $\lvert\mathbf{S}\rvert = \lvert\mathbf{E}\rvert^2/\eta$; for a sinusoidal sheet $\lvert\mathbf{S}\rvert = \tfrac14\eta J_{s0}^2\cos^2(\omega t\mp\beta z)$ on each side.

## 9. What you still need from Unit 1

| tool | equation | where |
|---|---|---|
| Gauss's law, symmetric cases | $D_r = \dfrac{Q}{4\pi r^2}$, $D_r = \dfrac{\rho_l}{2\pi r}$, $D = \dfrac{\rho_s}{2}$ | [[1-electrostatics/03-gauss-law-at-work\|L3]] |
| potential | $V(b)-V(a) = -\displaystyle\int_a^b\mathbf{E}\cdot d\mathbf{l}$, $\ \mathbf{E} = -\nabla V$ | [[1-electrostatics/05-curl-free-fields-and-the-electrostatic-potential\|L5]] |
| capacitance, conductance | $C = Q/V$; plates $\epsilon A/d$; coax $2\pi\epsilon\ell/\ln(b/a)$; $G = (\sigma/\epsilon)C$ | [[1-electrostatics/10-capacitance-and-conductance\|L10]] |
| relaxation | $\rho(t) = \rho_0e^{-t\sigma/\epsilon}$ | [[1-electrostatics/08-conductors-dielectrics-and-polarization\|L8]] |
| electric energy | $W = \tfrac12CV^2 = \displaystyle\int\tfrac12\epsilon E^2\,dV$ | L10 |

**Electrostatics ↔ magnetostatics, the rows that come up most:** $Q\leftrightarrow I$, $\mathbf{D}\leftrightarrow\mathbf{H}$ (the field the free source alone sets), $\mathbf{D} = \epsilon\mathbf{E}\leftrightarrow\mathbf{B} = \mu\mathbf{H}$, $C = Q/V\leftrightarrow L = N\Psi/I$, $\tfrac12CV^2\leftrightarrow\tfrac12LI^2$, Gauss surface ↔ Ampère loop, $D_n$ jumps by $\rho_s$ ↔ $H_t$ jumps by $J_s$.

## 10. The traps that cost the most points

> [!trap] Signs and directions
> 1. **Right-hand rules everywhere:** $\hat\phi$ around a current, $d\mathbf{S}$ from the sense of $C$, $I_{\text{enc}}$ signed by the loop direction. Decide the orientation *before* computing.
> 2. **$\hat n$ in the sheet formula points toward the field point**, so $\mathbf{H}$ reverses across a sheet; in boundary conditions $\hat n$ points from medium 2 into medium 1.
> 3. **$\mathbf{F} = q\mathbf{v}\times\mathbf{B}$, not $\mathbf{B}\times\mathbf{v}$**; an electron reverses the answer.
> 4. **Lenz opposes the change, not the field.** A decreasing flux induces a current that *supports* the original field.
> 5. **Motional emf uses the velocity of the path**, and only the parts of the loop that move contribute.
> 6. **$L = N\Psi/I$**: each of the $N$ turns links the flux; $L\propto N^2$.
> 7. **$\mathbf{M} = \chi_m\mathbf{H}$** — no $\mu_0$ (unlike $\mathbf{P} = \epsilon_0\chi_e\mathbf{E}$); **$\mathbf{J}_M = \nabla\times\mathbf{M}$** — no minus sign (unlike $-\nabla\cdot\mathbf{P}$); **$\mathbf{J}_{sM} = \mathbf{M}\times\hat n$**, in that order, $\hat n$ outward.
> 8. **Waves:** read the speed from the *ratio* of coefficients ($t + 0.02x$ means 50 m/s toward $-x$, not 0.02); $\mathbf{H} = \hat u\times\mathbf{E}/\eta$ with $\hat u$ the travel direction.
> 9. **The sheet's E opposes the current on both sides**; its H flips.
> 10. **Units:** $J_s$ in A/m, $\mathbf{M}$ and $\mathbf{H}$ in A/m, $\Psi$ in Wb, $\eta$ in Ω, $\mathbf{S}$ in W/m².

## 11. How to study for it

> [!tip] A plan that works when you feel lost
> 1. **Lecture by lecture, problems first.** For each of Lectures 11–19: read only the lecture's *key* boxes, then do the [[practice/index|practice set]]'s easy problems with this page open. Easy problems are where the equations stop being symbols.
> 2. **Then close this page.** Redo two medium problems per lecture without it. Whatever you had to look up goes on your notecard (if one is allowed) or into your memory drills.
> 3. **Worked problems as models.** Read one worked problem per unit the way an exam answer should look: [[problems/current-slab-and-sheet-by-amperes-law|slab and sheet by Ampère]] (L13), [[problems/sliding-bar-and-the-voltmeter-readings|sliding bar and voltmeters]] (L14), [[problems/coax-inductance-and-the-lc-product|coax inductance]] (L15), [[problems/fields-across-a-magnetic-interface|magnetic interface]] (L17), [[problems/a-pulse-on-the-move|a pulse on the move]] (L18), [[problems/a-current-sheet-launches-two-waves|a current sheet launches two waves]] (L19).
> 4. **Timed practice last.** In the final days, work past Exam 2s under exam time with no notes (the course's old Exam 2 / hour exam 2 papers), and the [[practice/hard|hard problems]] marked *modelled on* an exam. Grade yourself honestly against the solution's *Check* step.
> 5. **Spaced, not crammed.** Short daily sessions beat one long night: revisit yesterday's wrong problems first each day, then new material.
