---
title: "Midterm 2 — equation summary"
description: "Everything on Midterm 2 (Lectures 11–20, Homeworks 5–7) on one page, mostly equations: material models, magnetostatics, Faraday and inductance, the complete Maxwell equations, magnetic media, plane waves, current-sheet radiation and Poynting's theorem — with the sign rules, the canonical fields, the traps, what the homework drilled, a practice list and a weekend study plan."
tags: [toolkit, exam-2]
aliases: ["Midterm 2", "Exam 2 summary", "Exam 2 formula sheet"]
---

*Scope: **Lectures 11–20 and Homeworks 5–7**, for the exam on Monday, October 19. Lecture numbers on this site are the course notes'; from Lecture 13 on they match the slide files (the slides combine 11 and 12). Lecture 20 is Poynting's theorem ([[#9-energy-and-power-poyntings-theorem-lecture-20|§9]]). Phasors start in Lecture 21, after the cut-off; if your class reached them before the exam, read the [[3-maxwell-and-waves/21-monochromatic-waves-and-phasor-notation#9-summary|Lecture 21 summary]] too. Exam 1 tools (Gauss, potential, boundary conditions, capacitance) are still needed and are summarized in [[#10-what-you-still-need-from-unit-1|§10]]. What each homework problem practised is in [[#12-what-homeworks-57-drilled|§12]], and a weekend plan with a practice list in [[#13-how-to-study-for-it-exam-monday-october-19|§13]]. Each section links to the lecture that derives it; this page only collects.*

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
\mathbf{D} = \epsilon_0\mathbf{E}+\mathbf{P} = \epsilon\mathbf{E},\\[4pt]
\mathbf{B} = \mu_0(\mathbf{H}+\mathbf{M}) = \mu\mathbf{H},\\[4pt]
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
d\mathbf{B} = \frac{\mu_0}{4\pi}\frac{I\,d\mathbf{l}\times\hat R}{R^2}\\
(\hat R\ \text{from source to field point}),\\[4pt]
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
V = L\frac{dI}{dt}\ (\text{drop along } I),\\[4pt]
W = \tfrac12LI^2 = \int\tfrac12\mu H^2\,dV .
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
\nabla^2\mathbf{E} = \mu\epsilon\frac{\partial^2\mathbf{E}}{\partial t^2},\\[4pt]
E_x = Af\Big(t-\frac zv\Big)+Bg\Big(t+\frac zv\Big),\\[4pt]
H_y = \frac1\eta\Big[Af\Big(t-\frac zv\Big)-Bg\Big(t+\frac zv\Big)\Big],\\[4pt]
v = \frac{1}{\sqrt{\mu\epsilon}} = \frac{c}{\sqrt{\mu_r\epsilon_r}},\\[4pt]
\eta = \sqrt{\frac\mu\epsilon} = \eta_0\sqrt{\frac{\mu_r}{\epsilon_r}},\\[4pt]
c\approx3\times10^8\ \text{m/s} = 300\ \text{m}/\mu\text{s},\\[4pt]
\eta_0\approx120\pi\approx377\ \Omega .
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
- **Poynting vector:** $\mathbf{S} = \mathbf{E}\times\mathbf{H}$ [W/m²], along the travel, $\lvert\mathbf{S}\rvert = \lvert\mathbf{E}\rvert^2/\eta$; for a sinusoidal sheet $\lvert\mathbf{S}\rvert = \tfrac14\eta J_{s0}^2\cos^2(\omega t\mp\beta z)$ on each side. Its meaning as power, and the time averages, are §9.

## 9. Energy and power: Poynting's theorem (Lecture 20)

[[3-maxwell-and-waves/20-poynting-theorem-and-monochromatic-waves|Lecture 20]] · [[concepts/poynting-theorem]] · worked problem: [[problems/energy-bookkeeping-for-a-radiating-sheet|energy bookkeeping for a radiating sheet]]

$$
\begin{gathered}
\frac{\partial w}{\partial t}+\nabla\cdot\mathbf{S}+\mathbf{J}\cdot\mathbf{E} = 0,\\[4pt]
w = \tfrac12\epsilon E^2+\tfrac12\mu H^2\ [\text{J/m}^3],\\[4pt]
\mathbf{S} = \mathbf{E}\times\mathbf{H}\ [\text{W/m}^2],\qquad \mathbf{J}\cdot\mathbf{E}\ [\text{W/m}^3],\\[4pt]
-\frac{dW}{dt} = \oint_S\mathbf{S}\cdot d\mathbf{A}+\int_V\mathbf{J}\cdot\mathbf{E}\,dV\\[2pt]
(d\mathbf{A}\text{ outward}).
\end{gathered}
$$

- **Where it comes from:** $\mathbf{H}\cdot$(Faraday) $-\ \mathbf{E}\cdot$(Ampère–Maxwell), with $\nabla\cdot(\mathbf{E}\times\mathbf{H}) = \mathbf{H}\cdot\nabla\times\mathbf{E}-\mathbf{E}\cdot\nabla\times\mathbf{H}$; it needs $\epsilon$ and $\mu$ constant in time. It is the energy twin of the continuity equation $\partial\rho/\partial t+\nabla\cdot\mathbf{J} = 0$, plus an exchange term.
- **Reading $\mathbf{J}\cdot\mathbf{E}$:** positive means the field gives energy to the charges (Joule heating, $\sigma E^2 = J^2/\sigma$ in a conductor); negative means the current is a *source* that feeds the field (inside a battery, an antenna, a radiating sheet). It is the field version of a circuit element's $vi$.
- **A resistive wire is heated through its sides.** Current $I$ along $+\hat z$ in a wire of radius $a$: $\mathbf{E} = \hat z\,J/\sigma$ inside, $\mathbf{H} = \hat\phi\,I/2\pi a$ at the surface, so $\mathbf{S}$ points along $\hat z\times\hat\phi = -\hat r$, *into* the wire. Over a length $\ell$ of the side, $S\cdot2\pi a\ell = E\ell\,I = I^2R$.
- **Time averages of real cosines** (no phasors needed): $\langle\cos^2(\omega t+\phi)\rangle = \tfrac12$. For a plane wave $E_0\cos(\omega t-\beta z)$: $\langle S\rangle = E_0^2/2\eta$ along the travel (the instantaneous peak is $E_0^2/\eta$), $\langle w\rangle = \tfrac12\epsilon E_0^2$ (half electric, half magnetic) and $\langle S\rangle = v\langle w\rangle$. In a conductor with $E_0\cos\omega t$, $\langle\mathbf{J}\cdot\mathbf{E}\rangle = \tfrac12\sigma E_0^2$.
- **Radiating sheet:** $\mathbf{J}_s = \hat x\,J_0\cos\omega t$ in a medium with $\eta$ sends $\langle S\rangle = \eta J_0^2/8$ into each half-space and injects $\langle-\mathbf{J}_s\cdot\mathbf{E}\rangle = \eta J_0^2/4$ per unit area: the two sides together. At every instant $\hat n\cdot(\mathbf{S}_1-\mathbf{S}_2) = -\mathbf{J}_s\cdot\mathbf{E}$, with $\hat n$ from side 2 into side 1. The notes' sheet, $J_0 = 2$ A/m in vacuum, gives $\eta_0/2\approx188$ W/m² per side.
- **Two equal waves travelling in opposite directions** (a standing wave): $\langle\mathbf{S}\rangle = 0$ everywhere, yet $\langle w\rangle\neq0$ — the energy is stored, not carried.
- **Power through an area:** $P = \int\langle\mathbf{S}\rangle\cdot d\mathbf{A}$; a uniform plane wave crossing an area $A$ head-on delivers $\langle S\rangle A$.

## 10. What you still need from Unit 1

| tool | equation | where |
|---|---|---|
| Gauss's law, symmetric cases | $D_r = \dfrac{Q}{4\pi r^2}$, $D_r = \dfrac{\rho_l}{2\pi r}$, $D = \dfrac{\rho_s}{2}$ | [[1-electrostatics/03-gauss-law-at-work\|L3]] |
| potential | $V(b)-V(a) = -\displaystyle\int_a^b\mathbf{E}\cdot d\mathbf{l}$, $\ \mathbf{E} = -\nabla V$ | [[1-electrostatics/05-curl-free-fields-and-the-electrostatic-potential\|L5]] |
| capacitance, conductance | $C = Q/V$; plates $\epsilon A/d$; coax $2\pi\epsilon\ell/\ln(b/a)$; $G = (\sigma/\epsilon)C$ | [[1-electrostatics/10-capacitance-and-conductance\|L10]] |
| relaxation | $\rho(t) = \rho_0e^{-t\sigma/\epsilon}$ | [[1-electrostatics/08-conductors-dielectrics-and-polarization\|L8]] |
| electric energy | $W = \tfrac12CV^2 = \displaystyle\int\tfrac12\epsilon E^2\,dV$ | L10 |

**Electrostatics ↔ magnetostatics, the rows that come up most:** $Q\leftrightarrow I$, $\mathbf{D}\leftrightarrow\mathbf{H}$ (the field the free source alone sets), $\mathbf{D} = \epsilon\mathbf{E}\leftrightarrow\mathbf{B} = \mu\mathbf{H}$, $C = Q/V\leftrightarrow L = N\Psi/I$, $\tfrac12CV^2\leftrightarrow\tfrac12LI^2$, Gauss surface ↔ Ampère loop, $D_n$ jumps by $\rho_s$ ↔ $H_t$ jumps by $J_s$.

## 11. The traps that cost the most points

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
> 10. **Units:** $J_s$ in A/m, $\mathbf{M}$ and $\mathbf{H}$ in A/m, $\Psi$ in Wb, $\eta$ in Ω, $\mathbf{S}$ in W/m², $w$ in J/m³, $\mathbf{J}\cdot\mathbf{E}$ in W/m³.
> 11. **Power (Lecture 20):** a time average carries a ½ — $\langle S\rangle = E_0^2/2\eta$, while the instantaneous peak is $E_0^2/\eta$.
> 12. **$\mathbf{J}\cdot\mathbf{E} < 0$ marks a source**; a radiating sheet always has $\mathbf{J}_s\cdot\mathbf{E}<0$ because its $\mathbf{E}$ opposes $\mathbf{J}_s$. Power flowing *into* a volume is $-\oint\mathbf{S}\cdot d\mathbf{A}$ with $d\mathbf{A}$ outward.

## 12. What Homeworks 5–7 drilled

Exams reuse the homework's *moves*, not its numbers. For each problem: what it asked, the method in one line, and where to read and practise it. Redo each one on blank paper before looking at your old answer.

| problem | what it asked | the method | read · practise |
|---|---|---|---|
| HW5 #1 | flux of a uniform $\mathbf{B}$ through the faces of a closed wedge-shaped surface | $\oint\mathbf{B}\cdot d\mathbf{S} = 0$: compute the flat faces with outward normals; the curved face is minus their sum | [[2-magnetostatics/12-magnetic-force-biot-savart-and-amperes-law|L12]], [[concepts/magnetic-flux|magnetic flux]] · [[practice/12-magnetic-force-biot-savart-and-ampere#124-could-this-be-a-magnetic-field|12.4]] |
| HW5 #2 | two parallel current sheets: $\mathbf{H}$ at a point for several current directions | each sheet gives $\tfrac12\mathbf{J}_s\times\hat n$ with $\hat n$ from that sheet toward the point; add the vectors | [[2-magnetostatics/13-current-sheets-solenoids-and-the-vector-potential#1-the-current-sheet|L13 §1]] · [[practice/13-current-sheets-solenoids-and-vector-potential#131-one-current-sheet-two-points|13.1]], [[practice/13-current-sheets-solenoids-and-vector-potential#138-three-sheets-in-three-directions|13.8]] |
| HW5 #3 | a current slab: field direction by symmetry, zero at the mid-plane, $\mathbf{B}$ inside and outside, plot | Biot–Savart symmetry for the direction; an Ampère rectangle from the mid-plane: linear inside, constant outside | [[2-magnetostatics/13-current-sheets-solenoids-and-the-vector-potential#2-the-current-slab|L13 §2]], [[problems/current-slab-and-sheet-by-amperes-law|worked problem]] · [[practice/13-current-sheets-solenoids-and-vector-potential#137-a-slab-with-graded-current|13.7]], [[practice/13-current-sheets-solenoids-and-vector-potential#139-two-opposite-slabs-and-a-sheet|13.9]] |
| HW5 #4 | a wire with uniform $\mathbf{J}$, then the same wire with an off-centre hole | Ampère circle inside ($H = Jr/2$); the hole is the full wire plus an opposite current filling the hole, and the field in the hole is uniform | [[2-magnetostatics/12-magnetic-force-biot-savart-and-amperes-law#4-ampères-law-the-circulation-of-b|L12 §4]] · [[practice/12-magnetic-force-biot-savart-and-ampere#127-a-wire-with-a-nonuniform-current|12.7]], [[practice/12-magnetic-force-biot-savart-and-ampere#1212-a-wire-with-an-off-axis-hole|12.12]] |
| HW6 #1 | emf around fixed rectangular and triangular paths in a uniform, time-varying $\mathbf{B}$ | $\mathcal{E} = -d\Psi/dt$ with $d\mathbf{S}$ from the path's direction (right-hand rule); only the component of $\mathbf{B}$ normal to the path's plane counts; reversing the path flips $\mathcal{E}$ | [[2-magnetostatics/14-faradays-law-and-induced-emf#1-the-law-and-the-flux-it-is-about|L14 §1]] · [[practice/14-faradays-law-and-induced-emf#141-flux-through-a-tilted-loop|14.1]], [[practice/14-faradays-law-and-induced-emf#142-current-from-a-ramping-field|14.2]] |
| HW6 #2 | a square loop tilted in a uniform field, then turning at a constant rate | $\Psi(\theta) = \mathbf{B}\cdot\mathbf{S}$ with the stated $d\mathbf{S}$, then $\mathcal{E} = -d\Psi/dt$; a positive current circulates with $d\mathbf{S}$ by the right-hand rule, so flipping $d\mathbf{S}$ flips the sign of $\mathcal{E}$ but not the physical current | [[2-magnetostatics/14-faradays-law-and-induced-emf#2-moving-loops-the-emf-and-lenz|L14 §2]] · [[practice/14-faradays-law-and-induced-emf#147-generator-coil-in-a-uniform-field|14.7]] |
| HW6 #3 | a small loop moving through a field that varies with $x$ | $\Psi(t)\approx B_z(x_c(t))\,\pi r^2$, so $\mathcal{E} = -\pi r^2v\,\partial B_z/\partial x$ (counter-clockwise seen from $+z$ for $d\mathbf{S} = +\hat z\,dS$); $I = \mathcal{E}/R$ | [[2-magnetostatics/14-faradays-law-and-induced-emf#2-moving-loops-the-emf-and-lenz|L14 §2]], [[problems/emf-of-a-loop-moving-near-a-line-current|worked problem]] · [[practice/14-faradays-law-and-induced-emf#148-square-loop-in-a-graded-field|14.8]] |
| HW6 #4 | two concentric loops: resistance, mutual flux and inductance, the small loop moving along the axis, an RL equation | $R = \ell/\sigma A$; $B = \mu_0I/2a$ at the centre of a loop ($\mu_0Ia^2/2(a^2+z^2)^{3/2}$ on its axis); $M = \Psi/I$; $L\,di/dt+Ri = \mathcal{E}$ | [[1-electrostatics/10-capacitance-and-conductance|L10]], [[2-magnetostatics/13-current-sheets-solenoids-and-the-vector-potential#6-the-current-loop-and-the-magnetic-dipole|L13 §6]], [[2-magnetostatics/15-inductance-magnetic-energy-and-the-potentials#1-self-inductance|L15 §1–2]] · [[practice/15-inductance-and-magnetic-energy#156-switching-on-an-rl-circuit|15.6]], [[practice/15-inductance-and-magnetic-energy#1511-wire-and-rectangular-loop|15.11]] |
| HW6 #5 | rails with a sliding armature: generator, then rail gun | $\mathcal{E} = vBL$ from $-d\Psi/dt$ or $\oint(\mathbf{v}\times\mathbf{B})\cdot d\mathbf{l}$; direction by Lenz; force $I\mathbf{L}\times\mathbf{B}$; $a = F/M$ | [[2-magnetostatics/14-faradays-law-and-induced-emf#4-motional-emf-the-sliding-bar|L14 §4]], [[problems/sliding-bar-and-the-voltmeter-readings|worked problem]] · [[practice/14-faradays-law-and-induced-emf#145-a-sliding-bar-find-the-error|14.5]], [[practice/14-faradays-law-and-induced-emf#1411-magnetic-braking|14.11]] |
| HW6 #6 | a rectangular loop spinning on a vertical shaft in a uniform horizontal field | write the loop's normal $\hat s(\phi)$, then $\Psi = Bab\,\hat s\cdot\hat x$, $\phi = \omega t$, $\mathcal{E} = -d\Psi/dt$, $I = \mathcal{E}/R$ | [[2-magnetostatics/14-faradays-law-and-induced-emf#2-moving-loops-the-emf-and-lenz|L14 §2]] · [[practice/14-faradays-law-and-induced-emf#147-generator-coil-in-a-uniform-field|14.7]] |
| HW7 #1 | measuring $\epsilon$ and $\mu$ from time constants: a slab filling a capacitor gap, then half of it, and a rod inside a solenoid | $\tau = RC$ or $L/R$ with $R$ unchanged, so the ratio of time constants is the ratio of $C$ or $L$; a half-filled gap is two capacitors in series; $\mu<\mu_0$ means diamagnetic | [[1-electrostatics/10-capacitance-and-conductance#4-layered-dielectrics-series-and-parallel|L10 §4]], [[3-maxwell-and-waves/17-magnetization-and-maxwells-equations-in-matter#the-solenoid-with-a-core|L17 §4]] · [[practice/10-capacitance-and-conductance#107-one-slab-two-placements|10.7]], [[practice/17-magnetization-and-maxwell-in-matter#172-four-rods-in-a-solenoid|17.2]] |
| HW7 #2 | charge density from a given $\mathbf{J}(\mathbf{r})$, and the units of its coefficients | $\partial\rho/\partial t = -\nabla\cdot\mathbf{J}$, integrate in time and add $\rho$ at $t = 0$; units from $[J] = $ A/m² | [[3-maxwell-and-waves/16-charge-conservation-displacement-current-and-maxwells-equations#1-charge-conservation-and-the-continuity-equation|L16 §1]] · [[practice/16-charge-conservation-and-displacement-current#161-charge-piling-up-in-a-cylinder|16.1]] |
| HW7 #3 | charge relaxation in a homogeneous conductor, and where the stored energy goes | Gauss plus continuity with $\mathbf{J} = \sigma\mathbf{E}$ give $\partial\rho/\partial t+(\sigma/\epsilon)\rho = 0$, so $\rho = \rho_0e^{-t\sigma/\epsilon}$; the field energy ends up as Joule heat | [[1-electrostatics/08-conductors-dielectrics-and-polarization#2-conductors-in-electrostatics|L8 §2]] · [[practice/08-conductors-dielectrics-and-polarization#810-relaxation-of-a-charge-wave|8.10]], [[practice/11-lorentz-drude-models#118-relaxation-time-versus-collision-time|11.8]] |
| HW7 #4 | the partner field of a given plane wave, and the medium's $\epsilon_r$ or $\mu_r$ from its speed | speed = $\omega/\beta$ gives $\mu_r\epsilon_r$; then $\mathbf{H} = \hat u\times\mathbf{E}/\eta$ (or $\mathbf{E} = \eta\mathbf{H}\times\hat u$), checked against Faraday or Ampère–Maxwell and the time integral | [[3-maxwell-and-waves/18-the-wave-equation-and-plane-tem-waves#5-h-from-e-the-intrinsic-impedance|L18 §5]] · [[practice/18-wave-equation-and-plane-waves#182-the-partner-field|18.2]], [[practice/18-wave-equation-and-plane-waves#185-the-backwards-magnetic-field|18.5]] |
| HW7 #5 | which fields solve the wave equation: $f(\omega t-\beta x)+g(\omega t+\beta x)$, $\cos^2$, a standing wave, an oblique wave | substitute and compare $\partial^2/\partial t^2$ with $v^2\nabla^2$; any function of $t\mp\hat u\cdot\mathbf{r}/v$ works, and so do sums of them; an oblique wave needs $\omega^2 = v^2(\beta_x^2+\beta_y^2)$ | [[3-maxwell-and-waves/18-the-wave-equation-and-plane-tem-waves#4-the-1d-wave-equation-and-its-solutions|L18 §4]] · [[practice/18-wave-equation-and-plane-waves#186-which-fields-can-be-waves|18.6]], [[practice/18-wave-equation-and-plane-waves#1812-a-wave-on-a-slant|18.12]] |
| HW7 #6 | a triangle pulse travelling toward $-x$: $\mathbf{E}$, $\mathbf{H}$, $\mathbf{S}$ and its peak, where the peak is, a record at one place, a snapshot at one time | read direction and speed from $t+x/c$; $\mathbf{H}$ from $\hat u\times\mathbf{E}/\eta_0$; $\mathbf{S} = \mathbf{E}\times\mathbf{H}$ points along the travel ($-\hat x$); fix $x$ for a record, fix $t$ for a snapshot | [[3-maxwell-and-waves/18-the-wave-equation-and-plane-tem-waves#6-reading-a-wave|L18 §6]], [[3-maxwell-and-waves/20-poynting-theorem-and-monochromatic-waves|L20]] · [[practice/18-wave-equation-and-plane-waves#188-from-probe-record-to-snapshots|18.8]], [[practice/18-wave-equation-and-plane-waves#189-triangle-pulse-in-a-magnetic-medium|18.9]], [[practice/19-radiation-from-current-sheets#196-a-triangle-pulse-in-glass|19.6]] |

## 13. How to study for it (exam Monday, October 19)

> [!tip] A weekend plan
> **Saturday afternoon and evening: magnetostatics and induction.**
>
> 1. *30 min, diagnostic.* Read §1, close the page, and write the Maxwell table and the material relations from memory. What you can't write is your study list.
> 2. *2 h, Lectures 12–13 and HW5.* Redo HW5 cold (§12), then the Lecture 12–13 problems below.
> 3. *2 h, Lectures 14–15 and HW6.* Redo HW6 cold, then the Lecture 14–15 problems below.
> 4. *1 h 15, Lectures 16–17.* The four boundary conditions, displacement current, $\mathbf{M}$, $\mathbf{J}_{sM}$, $\mathbf{H} = \mathbf{B}/\mu_0-\mathbf{M}$; two easy problems each.
>
> **Sunday: waves, then timed papers.**
>
> 5. *Morning, Lectures 18–20 and HW7.* Read a wave's direction and speed, $\mathbf{H} = \hat u\times\mathbf{E}/\eta$, the sheet fields, then §9; redo HW7 cold.
> 6. *Early afternoon, one past paper under exam time, closed notes.* SP18 Exam 2 is the closest to this exam (it has the waves problems, #4–#5). Grade it honestly.
> 7. *Mid-afternoon, fix what you missed* with the lecture page and one practice problem on the same idea.
> 8. *Late afternoon, a second timed paper:* Summer 2018 or 2019 HE2.
> 9. *Evening, light:* §11's traps, and the Lecture 20 items from past papers listed below. Stop by 11 pm — sleep is worth more than a fourth paper.
>
> **Monday morning (45 min at most):** write this page's equations from memory once, reread §11, redo two or three problems you got wrong. Nothing new.

**The practice list.** Two to five problems per lecture, chosen to match the exam: *exam* marks problems modelled on a past paper. Easy ones first; if an easy one takes more than ten minutes, reread the lecture's key boxes before going on.

- **Lecture 11** (Drude, relaxation): [[practice/11-lorentz-drude-models#114-true-or-false|11.4]] (easy) · [[practice/11-lorentz-drude-models#118-relaxation-time-versus-collision-time|11.8]] (hard, exam)
- **Lecture 12** (Biot–Savart, Ampère): [[practice/12-magnetic-force-biot-savart-and-ampere#122-two-antiparallel-wires|12.2]] (easy) · [[practice/12-magnetic-force-biot-savart-and-ampere#127-a-wire-with-a-nonuniform-current|12.7]] (medium) · [[practice/12-magnetic-force-biot-savart-and-ampere#1210-two-crossing-line-currents|12.10]] (hard, exam) · [[practice/12-magnetic-force-biot-savart-and-ampere#1212-a-wire-with-an-off-axis-hole|12.12]] (hard)
- **Lecture 13** (sheets, slabs, solenoids, vector potential): [[practice/13-current-sheets-solenoids-and-vector-potential#131-one-current-sheet-two-points|13.1]] (easy) · [[practice/13-current-sheets-solenoids-and-vector-potential#133-a-solenoid-inside-a-solenoid|13.3]] (easy, exam) · [[practice/13-current-sheets-solenoids-and-vector-potential#138-three-sheets-in-three-directions|13.8]] (medium) · [[practice/13-current-sheets-solenoids-and-vector-potential#139-two-opposite-slabs-and-a-sheet|13.9]] (hard, exam)
- **Lecture 14** (Faraday, motional emf): [[practice/14-faradays-law-and-induced-emf#142-current-from-a-ramping-field|14.2]] (easy, exam) · [[practice/14-faradays-law-and-induced-emf#143-magnet-pulled-up-through-a-ring|14.3]] (easy, exam) · [[practice/14-faradays-law-and-induced-emf#147-generator-coil-in-a-uniform-field|14.7]] (medium) · [[practice/14-faradays-law-and-induced-emf#148-square-loop-in-a-graded-field|14.8]] (medium, exam) · [[practice/14-faradays-law-and-induced-emf#1410-voltmeters-around-a-ramping-solenoid|14.10]] (hard, exam)
- **Lecture 15** (inductance, energy, potentials): [[practice/15-inductance-and-magnetic-energy#153-fields-from-given-potentials|15.3]] (easy, exam) · [[practice/15-inductance-and-magnetic-energy#156-switching-on-an-rl-circuit|15.6]] (medium) · [[practice/15-inductance-and-magnetic-energy#159-toroid-with-a-two-layer-core|15.9]] (hard, exam) · [[practice/15-inductance-and-magnetic-energy#1510-shorted-parallel-plate-line|15.10]] (hard, exam)
- **Lecture 16** (displacement current, boundary conditions): [[practice/16-charge-conservation-and-displacement-current#162-displacement-current-through-a-window|16.2]] (easy) · [[practice/16-charge-conservation-and-displacement-current#1611-a-region-with-no-conduction-current|16.11]] (hard, exam) · [[practice/16-charge-conservation-and-displacement-current#1612-four-conditions-at-a-tilted-interface|16.12]] (hard, exam)
- **Lecture 17** (magnetic materials): [[practice/17-magnetization-and-maxwell-in-matter#171-moment-and-torque-on-a-loop|17.1]] (easy) · [[practice/17-magnetization-and-maxwell-in-matter#173-ferrite-between-sheets-find-the-error|17.3]] (easy) · [[practice/17-magnetization-and-maxwell-in-matter#1711-a-toroid-with-an-air-gap|17.11]] (hard, exam)
- **Lecture 18** (plane waves): [[practice/18-wave-equation-and-plane-waves#181-which-way-and-how-fast|18.1]] (easy) · [[practice/18-wave-equation-and-plane-waves#183-phase-rate-and-snapshot-period|18.3]] (easy, exam) · [[practice/18-wave-equation-and-plane-waves#189-triangle-pulse-in-a-magnetic-medium|18.9]] (hard, exam)
- **Lecture 19** (current-sheet radiation): [[practice/19-radiation-from-current-sheets#192-a-sheet-on-the-y--0-plane|19.2]] (easy) · [[practice/19-radiation-from-current-sheets#198-a-cosine-current-in-a-dielectric|19.8]] (medium) · [[practice/19-radiation-from-current-sheets#199-a-sheet-launches-a-step-and-a-ramp|19.9]] (hard, exam)
- **Lecture 20** (Poynting's theorem): [[practice/20-poynting-theorem-and-power#201-reading-the-energy-ledger|20.1]] (easy) · [[practice/20-poynting-theorem-and-power#202-joule-heating-at-a-point|20.2]] (easy, exam) · [[practice/20-poynting-theorem-and-power#204-standing-waves-true-or-false|20.4]] (easy, exam) · [[practice/20-poynting-theorem-and-power#2010-a-sheet-in-a-magnetic-medium|20.10]] (hard, exam)

**Past papers for timed practice** (in the course's exam folder): SP18 Exam 2 (Lectures 12–19, including a moving pulse and a radiating sheet); Summer 2017–2020 hour exam 2 (magnetostatics and induction, plus a conflict version of 2019). Lecture 20 never had its own Exam 2 problem; the closest past items are on Exam 3 papers: Summer 2019 HE3 #1b ($\mathbf{J}\cdot\mathbf{E}$ at a point, peak and average), Summer 2020 HE3 #2c–d (energy bookkeeping at a radiating sheet), and SP17 Exam 3 #1c and FA23 Exam 3 #1(c) (true/false on standing waves). The practice problems above marked *exam* are re-parameterized versions of these.

> [!tip] How to work a past paper
> Set a timer for the exam's length, close everything but a formula sheet if one is allowed, and write every answer with units and a direction. Then grade against the solution and sort each lost point: *didn't know the equation* (→ this page), *set up wrong* (→ the lecture's recipe box and one practice problem), or *algebra or sign slip* (→ §11). The third pile is the cheapest to fix.
