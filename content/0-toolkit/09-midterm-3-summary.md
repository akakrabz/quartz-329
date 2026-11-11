---
title: "Midterm 3 — equation summary"
description: "Midterm 3 on one page, mostly equations. Expect mostly the material since Midterm 2, Lectures 21–30: phasors and average power, damped waves and the two regimes, polarization, reflection and standing waves, transmission lines and bounce diagrams, with the sign rules, the traps, the earlier tools these problems use, what to put on the index card, what Homeworks 8–10 drilled, a plan for the days left and a practice list. (Announced scope: Lectures 1–30, Homeworks 1–11, no Smith chart.)"
tags: [toolkit, exam-3]
aliases: ["Midterm 3 summary", "Exam 3 summary", "Exam 3 formula sheet"]
---

*Midterm 3, Monday, November 16: **expect mostly Lectures 21–30**, the material since Midterm 2. The announcement says the exam covers Lectures 1–30 and Homeworks 1–11, with no Smith chart; the earlier lectures are the background these problems rely on ([[exams/index#what-the-announcement-says|what it says, and what to expect]]). One 4″×6″ card, closed book, no calculators. Here: the equations of Lectures 21–30 (§1–8), the earlier tools they use (§9), the traps (§10), the index card (§11), the homeworks (§12), a plan for the days left (§13) and a practice list (§14). The past papers and problem types are on the [[exams/index|Midterm 3 review]] page. Each section links to the page that derives it; this page only collects.*

> [!recipe] How to use this page
> Read a section, close the page, and rewrite its equations from memory on scrap paper. Then check. What you could not write is your study list, and the best of it goes on your index card. Every equation here has a sign or direction rule beside it; the rule is the part that costs points.

## 1. The whole picture

One plane wave, described by a short chain. The **source** fixes $\omega$. The **medium** ($\mu$, $\epsilon$, $\sigma$) fixes two complex numbers, $\gamma = \alpha+j\beta$ and $\eta = \lvert\eta\rvert e^{j\tau}$. Those give everything else: $\lambda$, $v_p$, $\delta$, $\mathbf{H}$ from $\mathbf{E}$, the power. An **interface** adds $\Gamma$ and $\tau = 1+\Gamma$. A **transmission line** is the same wave guided by two conductors, with $V$, $I$, $Z_0$ in place of $\mathbf{E}$, $\mathbf{H}$, $\eta$:

| plane wave (Lectures 21–26) | transmission line (Lectures 27–30) |
|---|---|
| $\mathbf{E}$, $\mathbf{H}$ | $V$, $I$ |
| $\eta = \sqrt{\mu/\epsilon}$ | $Z_0 = \sqrt{\mathcal{L}/\mathcal{C}}$ |
| $v = 1/\sqrt{\mu\epsilon}$ | $v = 1/\sqrt{\mathcal{L}\mathcal{C}}$ (the same number) |
| backward wave: $\mathbf{H}$ flips | backward wave: $I = -V/Z_0$ |
| $\Gamma = \dfrac{\eta_2-\eta_1}{\eta_2+\eta_1}$, $\ \tau = 1+\Gamma$ | $\Gamma_L = \dfrac{R_L-Z_0}{R_L+Z_0}$; junction $\tau = 1+\Gamma$ |
| $\langle S\rangle = \dfrac{\lvert\tilde E\rvert^2}{2\eta}$ [W/m²] | $\langle P\rangle = \dfrac{\lvert\tilde V\rvert^2}{2Z_0}$ [W] |

Learn the left column and the right one costs almost nothing ([[0-toolkit/08-waves-in-media-figures|figure reference]]).

**From Lectures 18–20, used all the time below** (more in §9): $\mathbf{H} = \hat u\times\mathbf{E}/\eta$ and $\mathbf{E} = \eta\,\mathbf{H}\times\hat u$ ($\hat u$ = travel direction); a current sheet radiates $\mathbf{E} = -\tfrac{\eta}{2}\mathbf{J}_s(t-\lvert\xi\rvert/v)$ on both sides, and $\mathbf{H}$ flips across it; $\langle\cos^2\rangle = \tfrac12$. All on the [[0-toolkit/05-midterm-2-summary#8-plane-waves-and-current-sheets-lectures-1819|Midterm 2 summary, §8–9]].

**No calculator:** $c = 3\times10^8$ m/s $= 300$ m/μs, $\eta_0 = 120\pi\ \Omega$, $\mu_0 = 4\pi\times10^{-7}$ H/m, $\epsilon_0 = 10^{-9}/36\pi$ F/m. Triangles: 3-4-5 gives 37° and 53°; $1{:}\sqrt3{:}2$ gives 30° and 60°; $1{:}1{:}\sqrt2$ gives 45°.

## 2. Monochromatic waves and phasors (Lecture 21)

[[3-maxwell-and-waves/21-monochromatic-waves-and-phasor-notation|Lecture 21]] · [[concepts/monochromatic-waves|Monochromatic waves]] · [[concepts/phasors|Phasors]] · [[concepts/time-average-power|Time-average power]]

$$
\begin{gathered}
\mathbf{E} = \hat x\,E_0\cos(\omega t-\beta z+\theta)\ \leftrightarrow\ \tilde{\mathbf{E}} = \hat x\,E_0e^{j\theta}e^{-j\beta z},\\[4pt]
\beta = \frac{\omega}{v_p} = \frac{2\pi}{\lambda},\qquad \lambda = \frac{v_p}{f},\qquad T = \frac1f = \frac{2\pi}{\omega},\\[4pt]
\tilde{\mathbf{H}} = \frac{\hat u\times\tilde{\mathbf{E}}}{\eta},\qquad \tilde{\mathbf{E}} = \eta\,\tilde{\mathbf{H}}\times\hat u,\\[4pt]
\langle\mathbf{S}\rangle = \tfrac12\text{Re}\{\tilde{\mathbf{E}}\times\tilde{\mathbf{H}}^*\} = \hat u\,\frac{\lvert\tilde E\rvert^2}{2\eta}\ \ (\text{lossless}).
\end{gathered}
$$

- **Direction:** $\omega t-\beta z$, or $e^{-j\beta z}$, travels toward $+z$; $\omega t+\beta z$, or $e^{+j\beta z}$, toward $-z$.
- **Phasor rules:** cosine is the reference and amplitudes are peak values. $A\cos(\omega t+\theta)\leftrightarrow Ae^{j\theta}$; $A\sin(\omega t+\theta)\leftrightarrow -jAe^{j\theta}$; $\partial/\partial t\leftrightarrow j\omega$. Back to time: multiply by $e^{j\omega t}$ and take the real part.
- **Reading an expression:** $\omega$ is the coefficient of $t$, $\beta$ the coefficient of position. Then $f$, $\lambda$, $v_p = \omega/\beta$, and for $\mu = \mu_0$, $\epsilon_r = (c/v_p)^2$.
- **Two components:** powers add. $\tilde{\mathbf{E}} = (\hat xA+\hat yBe^{j\phi})e^{-j\beta z}$ carries $\langle S\rangle = (\lvert A\rvert^2+\lvert B\rvert^2)/2\eta$, whatever $\phi$ is.
- **Plasma** (not a simple medium): $\omega^2 = \omega_p^2+\beta^2c^2$, so $v_p = \omega/\beta>c$ and no propagation below $\omega_p$ ([[concepts/dispersion-relation|Dispersion relation]]).

## 3. Damped waves: γ and η (Lecture 22)

[[3-maxwell-and-waves/22-phasor-maxwell-equations-and-damped-waves|Lecture 22]] · [[concepts/propagation-constant|Propagation constant]] · [[0-toolkit/07-wave-parameters-map|Wave parameters on one page]]

$$
\begin{gathered}
\gamma = \sqrt{j\omega\mu(\sigma+j\omega\epsilon)} = \alpha+j\beta,\qquad
\eta = \sqrt{\frac{j\omega\mu}{\sigma+j\omega\epsilon}} = \lvert\eta\rvert e^{j\tau},\\[4pt]
\gamma\eta = j\omega\mu,\qquad \frac{\gamma}{\eta} = \sigma+j\omega\epsilon,\\[4pt]
\tilde{\mathbf{E}} = \hat x\,E_0e^{-\alpha z}e^{-j\beta z},\qquad
\tilde{\mathbf{H}} = \hat y\,\frac{E_0}{\lvert\eta\rvert}e^{-\alpha z}e^{-j\beta z}e^{-j\tau},\\[4pt]
\langle\mathbf{S}\rangle = \hat z\,\frac{\lvert E_0\rvert^2}{2\lvert\eta\rvert}\,e^{-2\alpha z}\cos\tau .
\end{gathered}
$$

- $\alpha$ [Np/m] sits in the envelope, $\beta$ [rad/m] inside the cosine. $\lambda = 2\pi/\beta$, $v_p = \omega/\beta$, penetration depth $\delta = 1/\alpha$.
- $0\le\tau\le45^\circ$, and $\mathbf{H}$ **lags** $\mathbf{E}$ by $\tau$: in time, $\cos(\omega t-\beta z-\tau)$.
- **Decoding a given wave** (the 25-point problem): read $\alpha$, $\beta$, $\omega$; then $\lvert\eta\rvert = \omega\mu/\lvert\gamma\rvert$ and $\tau = 90^\circ-\angle\gamma$ from $\gamma\eta = j\omega\mu$; then $\sigma$ and $\omega\epsilon$ are the real and imaginary parts of $\gamma/\eta$.
- **Loss tangent in one step:** $\sigma/\omega\epsilon = \tan2\tau$. So $\tau = 30^\circ$ means $\sigma/\omega\epsilon = \sqrt3$.
- Use the medium's $\mu$ in $\gamma\eta = j\omega\mu$. It cancels in the loss tangent.

## 4. The two regimes and skin depth (Lecture 23)

[[3-maxwell-and-waves/23-imperfect-dielectrics-and-good-conductors|Lecture 23]] · [[concepts/loss-tangent|Loss tangent]] · [[concepts/skin-depth|Skin depth]]

Compare $\sigma/\omega\epsilon$ with 1 **at the frequency given**:

| | perfect dielectric, $\sigma = 0$ | imperfect dielectric, $\sigma/\omega\epsilon\ll1$ | good conductor, $\sigma/\omega\epsilon\gg1$ |
|---|---|---|---|
| $\beta$ | $\omega\sqrt{\mu\epsilon}$ | $\omega\sqrt{\mu\epsilon}$ | $\sqrt{\pi f\mu\sigma}$ |
| $\alpha$ | 0 | $\dfrac\sigma2\sqrt{\dfrac\mu\epsilon}$ | $\sqrt{\pi f\mu\sigma}$ |
| $\lvert\eta\rvert$ | $\sqrt{\mu/\epsilon}$ | $\sqrt{\mu/\epsilon}$ | $\sqrt{\omega\mu/\sigma}$ |
| $\tau$ | 0 | $\approx\dfrac{\sigma}{2\omega\epsilon}$ rad, small | 45° |
| $\lambda$ | $2\pi/\beta$ | $2\pi/\beta$ | $2\pi\delta$ |
| $\delta = 1/\alpha$ | $\infty$ | $\dfrac2\sigma\sqrt{\dfrac\epsilon\mu}$ | $\dfrac{1}{\sqrt{\pi f\mu\sigma}}$ |

- **Signatures:** $\alpha\ll\beta$ and $\tau\approx0$: imperfect dielectric. $\alpha = \beta$ and $\tau = 45^\circ$: good conductor. Anything else is in between, and only the exact $\gamma$ and $\eta$ of §3 apply. In all of these media $\alpha\le\beta$.
- **Good conductor:** $\epsilon$ drops out of every formula; the wave dies within one wavelength ($\lambda = 2\pi\delta$); $v_p = \omega\delta$ depends on frequency.
- **Decay:** the field falls as $e^{-z/\delta}$, the power as $e^{-2z/\delta}$. After one $\delta$: 37 % of the field, 13.5 % of the power. In decibels, $8.686\,\alpha$ dB per metre for field and power alike.
- **No-calculator loss tangent:** $\dfrac{\sigma}{\omega\epsilon} = \dfrac{18\times10^9\,\sigma}{f\,\epsilon_r}$. Seawater ($\sigma = 4$ S/m, $\epsilon_r = 81$) crosses 1 at 889 MHz; at 1 kHz it is a good conductor with $\delta = 25/\pi\approx8$ m and $\lambda = 50$ m. Copper at 60 Hz: $\delta\approx8.5$ mm.
- SP17–SP19 printed this table on the exam; FA23 did not. Put it on your card.

## 5. Polarization and group velocity (Lecture 24)

[[3-maxwell-and-waves/24-signal-transmission-and-circular-polarization|Lecture 24]] · [[concepts/wave-polarization|Wave polarization]] · [[concepts/group-velocity|Group velocity]]

For $\tilde{\mathbf{E}} = (\hat xA+\hat yBe^{j\phi})e^{-j\beta z}$ with $A$, $B$ real, travelling toward $+z$:

| condition | polarization |
|---|---|
| $\phi = 0$ or $\pi$, or one component zero | **linear**, whatever $A$ and $B$ are |
| $\lvert A\rvert = \lvert B\rvert$ **and** $\phi = \pm90^\circ$ | **circular** |
| anything else | elliptical |

> [!key] Handedness
> Point your right thumb along the direction of travel. If your fingers curl the way $\mathbf{E}$ turns in time at a fixed point, the wave is right-handed. Shortcut: (leading component) $\times$ (lagging component) $= +\hat u$ means **right** circular. Toward $+z$: $\hat x-j\hat y$ is right circular ($\hat x$ leads, $\hat x\times\hat y = \hat z$) and $\hat x+j\hat y$ is left circular.

- Convert every sine to a cosine first: $\sin(\cdot)$ is a cosine that lags by 90°, a factor $-j$.
- $\mathbf{H}$ has the same polarization as $\mathbf{E}$. Reversing the travel direction with the same rotation in time reverses the handedness (a mirror does this).
- A circular wave with amplitude $E_0$ in each component carries $\langle S\rangle = E_0^2/\eta$: twice the linear wave with the same peak field.
- Linear $=$ right circular $+$ left circular of equal size: $\hat x = \tfrac12(\hat x-j\hat y)+\tfrac12(\hat x+j\hat y)$.
- **Group velocity:** $v_g = d\omega/d\beta$ carries the envelope, the energy and the signal; $v_p = \omega/\beta$ carries the crests. In a plasma $v_pv_g = c^2$.

## 6. Reflection, standing waves, radiation pressure (Lectures 25–26)

[[3-maxwell-and-waves/25-wave-reflection-and-transmission|Lecture 25]] · [[3-maxwell-and-waves/26-standing-waves-and-radiation-pressure|Lecture 26]] · [[concepts/reflection-and-transmission|Reflection and transmission]] · [[concepts/standing-waves|Standing waves]] · [[concepts/radiation-pressure|Radiation pressure]]

A wave in region 1 meets region 2 head-on at $z = 0$:

$$
\begin{gathered}
\Gamma = \frac{\eta_2-\eta_1}{\eta_2+\eta_1},\qquad \tau = 1+\Gamma = \frac{2\eta_2}{\eta_2+\eta_1},\\[4pt]
\tilde{\mathbf{E}}_i = \hat x\,E_0e^{-j\beta_1z},\quad
\tilde{\mathbf{E}}_r = \hat x\,\Gamma E_0e^{+j\beta_1z},\quad
\tilde{\mathbf{E}}_t = \hat x\,\tau E_0e^{-j\beta_2z},\\[4pt]
\tilde{\mathbf{H}}_i = \hat y\,\frac{E_0}{\eta_1}e^{-j\beta_1z},\quad
\tilde{\mathbf{H}}_r = -\hat y\,\frac{\Gamma E_0}{\eta_1}e^{+j\beta_1z},\quad
\tilde{\mathbf{H}}_t = \hat y\,\frac{\tau E_0}{\eta_2}e^{-j\beta_2z}.
\end{gathered}
$$

- Region 1 is where the wave **comes from**. The reflected wave uses $\beta_1$ with the sign of the exponent flipped, and its $\mathbf{H}$ carries $-\Gamma$.
- Power: $\lvert\Gamma\rvert^2$ reflects and $1-\lvert\Gamma\rvert^2 = \lvert\tau\rvert^2\eta_1/\eta_2$ goes through (lossless media). Air into $\epsilon_r = 4$: $\Gamma = -\tfrac13$, $\tau = \tfrac23$, 11 % reflected, 89 % transmitted.
- **Working backward** from a given transmitted wave: $E_i = E_t/\tau$, then $E_r = \Gamma E_i$. Check $E_i+E_r = E_t$ at the interface.
- Into a good conductor $\lvert\eta_2\rvert\ll\eta_1$, so $\Gamma\approx-1$. Out of one, $\Gamma\approx+1$.
- **Perfect conductor** at $z = 0$ ($\Gamma = -1$, $\tau = 0$), in front of it:

$$
\begin{gathered}
\tilde{\mathbf{E}} = -\hat x\,2jE_0\sin\beta z,\qquad \tilde{\mathbf{H}} = \hat y\,\frac{2E_0}{\eta}\cos\beta z,\\[4pt]
\mathbf{E} = \hat x\,2E_0\sin\beta z\,\sin\omega t,\qquad \mathbf{H} = \hat y\,\frac{2E_0}{\eta}\cos\beta z\,\cos\omega t .
\end{gathered}
$$

- A **standing wave:** fixed nodes, $\mathbf{E}$ zero at the mirror and every $\lambda/2$ from it, $\mathbf{H}$ largest where $\mathbf{E}$ is zero, $\mathbf{E}$ and $\mathbf{H}$ a quarter period apart in time. $\langle\mathbf{S}\rangle = 0$ everywhere, but the stored energy is not zero. Surface current on the mirror: $\mathbf{J}_s = \hat n\times\mathbf{H}$, size $2E_0/\eta$.
- **Partial reflection** ($0<\lvert\Gamma\rvert<1$): a travelling part plus a standing part; $\lvert\tilde E\rvert$ swings between $E_0(1+\lvert\Gamma\rvert)$ and $E_0(1-\lvert\Gamma\rvert)$, maxima $\lambda/2$ apart.
- **Radiation pressure:** $\langle S\rangle/c$ on a perfect absorber, $2\langle S\rangle/c$ on a perfect mirror. 1 kW/m² on a mirror: 6.7 μPa.

## 7. Transmission lines (Lecture 27)

[[4-transmission-lines/27-guided-tem-waves-on-transmission-lines|Lecture 27]] · [[concepts/telegraphers-equations|Telegrapher's equations]] · [[concepts/characteristic-impedance|Characteristic impedance]]

$$
\begin{gathered}
-\frac{\partial V}{\partial z} = \mathcal{L}\frac{\partial I}{\partial t},\qquad
-\frac{\partial I}{\partial z} = \mathcal{C}\frac{\partial V}{\partial t},\\[4pt]
v = \frac{1}{\sqrt{\mathcal{L}\mathcal{C}}} = \frac{1}{\sqrt{\mu\epsilon}},\qquad Z_0 = \sqrt{\frac{\mathcal{L}}{\mathcal{C}}},\\[4pt]
V = f\Big(t-\frac zv\Big)+g\Big(t+\frac zv\Big),\qquad
I = \frac1{Z_0}\Big[f\Big(t-\frac zv\Big)-g\Big(t+\frac zv\Big)\Big].
\end{gathered}
$$

- $V/I = +Z_0$ for a forward wave alone, $-Z_0$ for a backward wave alone, and neither for their sum.
- **Parallel plates** (width $W$, gap $d$): $\mathcal{L} = \mu d/W$, $\mathcal{C} = \epsilon W/d$, $Z_0 = \eta\,d/W$. **Coax:** $Z_0 = \dfrac{\eta}{2\pi}\ln\dfrac ba$.
- **Fields ↔ circuit** on the plates: $V = Ed$, $I = HW = J_sW$. $\mathbf{E}$ points from the positive plate to the negative one; the plate current $\mathbf{J}_s = \hat n\times\mathbf{H}$ runs along the direction of travel on one plate and back on the other.
- Power carried by a forward wave: $P = V^2/Z_0$ at each instant, $\lvert\tilde V\rvert^2/2Z_0$ on average. It equals $\langle S\rangle$ times the cross-section $Wd$.
- A filling changes $v = c/\sqrt{\epsilon_r}$ and $Z_0\propto1/\sqrt{\epsilon_r}$; a measured delay gives $\epsilon_r = (c/v)^2$.

## 8. Bounce diagrams (Lectures 28–30)

[[4-transmission-lines/28-distributed-circuits-and-bounce-diagrams|Lecture 28]] · [[4-transmission-lines/29-bounce-diagram-examples|Lecture 29]] · [[4-transmission-lines/30-multi-line-circuits|Lecture 30]] · [[concepts/bounce-diagram|Bounce diagram]]

A source $f_i(t)$ with resistance $R_g$ at $z = 0$, a line $Z_0$ of length $\ell$, a load $R_L$ at $z = \ell$:

$$
\begin{gathered}
\tau_g = \frac{Z_0}{R_g+Z_0},\qquad
\Gamma_L = \frac{R_L-Z_0}{R_L+Z_0},\qquad
\Gamma_g = \frac{R_g-Z_0}{R_g+Z_0},\qquad T = \frac\ell v .
\end{gathered}
$$

> [!recipe] A bounce diagram, every time
> 1. Three coefficients and the one-way time $T$.
> 2. Axes: $z$ across, $t$ down. Launch $\tau_gf_i$ from $(0,0)$; it reaches the load at $T$.
> 3. At the load multiply by $\Gamma_L$, at the generator by $\Gamma_g$, alternately. Label every segment with its weight.
> 4. **Current diagram:** first segment $\tau_gf_i/Z_0$; every reflection multiplies by $-\Gamma$.
> 5. **$V$ at a point and time:** draw the horizontal line at $t$ and add every segment that has already passed $z$. At an end, an arriving segment and its reflection appear together: the load jumps by $(1+\Gamma_L)$ times the arriving wave.
> 6. **Check:** for a step $V_0u(t)$ everything must settle to DC, $V_\infty = V_0R_L/(R_g+R_L)$ and $I_\infty = V_0/(R_g+R_L)$. At DC the line is two wires and $Z_0$ drops out.

- **Loads:** open, $\Gamma_L = +1$ (voltage doubles, current zero); short, $\Gamma_L = -1$ (voltage zero, current doubles); matched, $\Gamma_L = 0$ (no echo). A matched generator ($\Gamma_g = 0$) absorbs the first echo and the diagram ends.
- **Example:** $Z_0 = 50\ \Omega$, $R_g = 25\ \Omega$, $R_L = 100\ \Omega$, a 9 V step. $\tau_g = \tfrac23$, $\Gamma_L = \tfrac13$, $\Gamma_g = -\tfrac13$. Launched: 6 V. Load at $T$: $6+2 = 8$ V. Source end at $2T$: $6+2-\tfrac23 = 7.33$ V. Steady state: $9\cdot\tfrac{100}{125} = 7.2$ V.
- **Other sources:** a pulse is a step minus a delayed step. An impulse $\delta(t)$ gives the impulse response: a train of weighted, delayed impulses; for any $f_i(t)$ replace each $\delta$ by a copy of $f_i$.
- **Snapshots** (against $z$ at one $t$): the part of the waveform launched first is farthest along, so a forward wave appears mirrored in $z$. **Records** (against $t$ at one $z$): the forward wave arrives at $z/v$, its echo at $(2\ell-z)/v$.
- **Inverse problems:** the first arrival time gives $v$; the first weight gives $\tau_g$ and so $R_g$; the ratio of second to first gives $\Gamma_L$ and so $R_L = Z_0\dfrac{1+\Gamma_L}{1-\Gamma_L}$; a missing pulse means a matched end.

**Two lines in cascade (Lecture 30).** A wave on line $j$ arriving at line $k$:

$$
\Gamma_{jk} = \frac{Z_k-Z_j}{Z_k+Z_j},\qquad \tau_{jk} = 1+\Gamma_{jk} = \frac{2Z_k}{Z_k+Z_j} .
$$

- Back through the same junction: $\Gamma_{kj} = -\Gamma_{jk}$, $\tau_{kj} = 1-\Gamma_{jk}$. For **current**: reflection $-\Gamma_{jk}$, transmission $1-\Gamma_{jk}$.
- Each line has its own delay and its own slope on the diagram. Every arrival at the junction makes two new segments.
- A resistor across the junction: the wave sees $R\parallel Z_k$, and $\tau = 1+\Gamma$ still holds. A resistor in series: it sees $R+Z_k$, and $\tau = (1+\Gamma)\dfrac{Z_k}{R+Z_k}$.
- No echo returns to the source only if **nothing** downstream reflects: every junction and the load.

## 9. Tools from earlier lectures that these problems use

Lecture 21–30 problems are built with a handful of tools from before Midterm 2. These are the ones that actually appear inside them:

| tool | equation | where it comes up now | lecture |
|---|---|---|---|
| partner field | $\mathbf{H} = \dfrac{\hat u\times\mathbf{E}}{\eta}$, $\ \mathbf{E} = \eta\,\mathbf{H}\times\hat u$; $\mathbf{E}\times\mathbf{H}$ along the travel $\hat u$ | every wave problem | [[3-maxwell-and-waves/18-the-wave-equation-and-plane-tem-waves\|L18]] |
| speed and impedance | $v = \dfrac{1}{\sqrt{\mu\epsilon}} = \dfrac{c}{\sqrt{\mu_r\epsilon_r}}$, $\ \eta = \sqrt{\dfrac\mu\epsilon} = \eta_0\sqrt{\dfrac{\mu_r}{\epsilon_r}}$ | decoding a medium; a line's filling from a delay | [[3-maxwell-and-waves/18-the-wave-equation-and-plane-tem-waves\|L18]] |
| a travelling waveform | $f(t-z/v)$ goes toward $+z$, $g(t+z/v)$ toward $-z$; fix $z$ for a record, fix $t$ for a snapshot | bounce-diagram plots and snapshots | [[3-maxwell-and-waves/18-the-wave-equation-and-plane-tem-waves\|L18]] |
| current-sheet radiation | $\mathbf{E} = -\dfrac\eta2\mathbf{J}_s\Big(t-\dfrac{\lvert\xi\rvert}{v}\Big)$ on both sides; $\mathbf{H} = \tfrac12\mathbf{J}_s\times\hat n$ flips across the sheet | polarization made by two sheets (HW10 #4), HW9 #2 and #5 | [[3-maxwell-and-waves/19-dalembert-solutions-and-radiation-from-current-sheets\|L19]] |
| power | $\mathbf{S} = \mathbf{E}\times\mathbf{H}$ [W/m²]; $\langle\cos^2\rangle = \tfrac12$; $\mathbf{J}\cdot\mathbf{E}$ [W/m³], $\tfrac12\sigma E_0^2$ on average | power against depth, power of a circular wave, power on a line | [[3-maxwell-and-waves/20-poynting-theorem-and-monochromatic-waves\|L20]] |
| boundary conditions | $\hat n\times(\mathbf{E}_1-\mathbf{E}_2) = 0$, $\ \hat n\times(\mathbf{H}_1-\mathbf{H}_2) = \mathbf{J}_s$, $\ \hat n\cdot(\mathbf{D}_1-\mathbf{D}_2) = \rho_s$; $\hat n$ from 2 into 1 | where $\Gamma$ and $\tau$ come from | [[3-maxwell-and-waves/16-charge-conservation-displacement-current-and-maxwells-equations\|L16]] |
| perfect conductor | no field inside; just outside $\mathbf{E}$ is normal and $\mathbf{H}$ tangential: $\rho_s = \hat n\cdot\mathbf{D}$, $\mathbf{J}_s = \hat n\times\mathbf{H}$ | the mirror's surface current; charges and currents on a line's plates | [[3-maxwell-and-waves/16-charge-conservation-displacement-current-and-maxwells-equations\|L16]] |
| conduction and displacement current | $\sigma\mathbf{E}$ and $\partial\mathbf{D}/\partial t$; for a sinusoid their ratio is $\sigma/\omega\epsilon$ | the loss tangent | [[3-maxwell-and-waves/16-charge-conservation-displacement-current-and-maxwells-equations\|L16]] |
| line parameters | plates: $\mathcal{C} = \dfrac{\epsilon W}{d}$, $\mathcal{L} = \dfrac{\mu d}{W}$; coax: $\mathcal{C} = \dfrac{2\pi\epsilon}{\ln(b/a)}$, $\mathcal{L} = \dfrac{\mu}{2\pi}\ln\dfrac ba$; always $\mathcal{L}\mathcal{C} = \mu\epsilon$ | $Z_0$ and $v$ of a line | [[1-electrostatics/10-capacitance-and-conductance\|L10]], [[2-magnetostatics/15-inductance-magnetic-energy-and-the-potentials\|L15]] |
| circuits | the voltage divider; a resistive circuit's DC steady state | $\tau_g$; the $t\to\infty$ check of a bounce diagram | [[4-transmission-lines/28-distributed-circuits-and-bounce-diagrams\|L28]] |

If one of these feels shaky, read the linked lecture's key box and do one problem: [[practice/18-wave-equation-and-plane-waves#189-triangle-pulse-in-a-magnetic-medium|18.9]] (pulse, partner field), [[practice/19-radiation-from-current-sheets#198-a-cosine-current-in-a-dielectric|19.8]] (cosine sheet), [[practice/20-poynting-theorem-and-power#202-joule-heating-at-a-point|20.2]] ($\mathbf{J}\cdot\mathbf{E}$), [[practice/16-charge-conservation-and-displacement-current#1612-four-conditions-at-a-tilted-interface|16.12]] (all four boundary conditions).

**Formally in scope: everything from Lectures 1–20.** The announcement says the exam covers Lectures 1–30, so nothing earlier is excluded. The expectation, yours and the past papers', is that it shows up as background like the table above, not as separate problems ([[exams/index#what-the-announcement-says|what to expect]]). If you want a fuller refresh: the [[0-toolkit/05-midterm-2-summary|Midterm 2 summary]] has Lectures 11–20 on one page, and the box below has Lectures 1–10.

> [!note]- Lectures 1–10 on one screen (secondary)
> | tool | equations | lecture |
> |---|---|---|
> | Coulomb, superposition | $\mathbf{E} = \dfrac{Q}{4\pi\epsilon_0R^2}\hat R$, $\hat R$ from the charge to the field point; fields add as vectors | [[1-electrostatics/02-coulombs-law-superposition-and-gauss\|L2]] |
> | Gauss's law | $\oint_S\mathbf{D}\cdot d\mathbf{S} = Q_{\text{enc}}$; point $D_r = \dfrac{Q}{4\pi r^2}$; line $D_r = \dfrac{\rho_l}{2\pi r}$; sheet $D = \dfrac{\rho_s}{2}$ on each side | [[1-electrostatics/03-gauss-law-at-work\|L3]] |
> | … inside uniform charge | slab (from the mid-plane) $D_x = \rho x$; cylinder $D_r = \dfrac{\rho r}{2}$; sphere $D_r = \dfrac{\rho r}{3}$; outside, use the total charge | [[1-electrostatics/03-gauss-law-at-work\|L3]] |
> | divergence and curl | $\rho = \nabla\cdot\mathbf{D}$; a static $\mathbf{E}$ must have $\nabla\times\mathbf{E} = 0$ | [[1-electrostatics/04-divergence-and-curl\|L4]] |
> | potential | $V(b)-V(a) = -\displaystyle\int_a^b\mathbf{E}\cdot d\mathbf{l}$; $\mathbf{E} = -\nabla V$; point charge $V = \dfrac{Q}{4\pi\epsilon_0R}$ | [[1-electrostatics/05-curl-free-fields-and-the-electrostatic-potential\|L5]] |
> | Poisson, Laplace | $\nabla^2V = -\rho/\epsilon$; with no charge: $V$ linear between plates, $\propto\ln r$ in a coax, $\propto1/r$ between spheres | [[1-electrostatics/07-poisson-and-laplace\|L7]] |
> | conductors | static: $\mathbf{E} = 0$ inside, one potential; $\mathbf{J} = \sigma\mathbf{E}$; relaxation $\rho = \rho_0e^{-\sigma t/\epsilon}$ | [[1-electrostatics/08-conductors-dielectrics-and-polarization\|L8]] |
> | dielectrics | $\mathbf{P} = \epsilon_0\chi_e\mathbf{E}$; $\mathbf{D} = \epsilon_0\mathbf{E}+\mathbf{P} = \epsilon\mathbf{E}$; $\rho_b = -\nabla\cdot\mathbf{P}$; $\rho_{sb} = \mathbf{P}\cdot\hat n_{\text{out}}$ | [[1-electrostatics/08-conductors-dielectrics-and-polarization\|L8]], [[1-electrostatics/09-static-fields-in-dielectric-media\|L9]] |
> | capacitance | $C = Q/V$; plates $\dfrac{\epsilon A}{d}$; coax $\dfrac{2\pi\epsilon\ell}{\ln(b/a)}$; spheres $\dfrac{4\pi\epsilon ab}{b-a}$ | [[1-electrostatics/10-capacitance-and-conductance\|L10]] |
> | conductance, energy | $G = \dfrac\sigma\epsilon C$; $RC = \dfrac\epsilon\sigma$; $W = \tfrac12CV^2 = \displaystyle\int\tfrac12\epsilon E^2\,dV$ | [[1-electrostatics/10-capacitance-and-conductance\|L10]] |
>
> The four problems of your Exam 1 have worked twins: [[problems/curl-potential-and-charge-from-a-field|a field given by a formula]] · [[problems/charged-slab-with-a-power-law-profile|a non-uniform charged slab]] · [[problems/fields-across-a-dielectric-interface|a dielectric interface]] · [[problems/two-layer-coaxial-capacitor|a two-layer coaxial capacitor]].

## 10. The traps that cost the most points

> [!trap] Signs, factors and directions
> 1. **A sine hides $-90^\circ$.** Convert to cosines before comparing phases or naming a polarization.
> 2. **$e^{-j\beta z}$ travels toward $+z$.** The reflected wave gets $e^{+j\beta_1z}$, with region 1's $\beta$.
> 3. **$\tilde{\mathbf{H}} = \hat u\times\tilde{\mathbf{E}}/\eta$:** write the cross product out; $\hat u$ is the travel direction. In a lossy medium $\mathbf{H}$ lags by $\tau$: the factor is $e^{-j\tau}$.
> 4. **Power decays twice as fast as the field:** $e^{-2\alpha z}$, and $\langle S\rangle$ carries $\cos\tau$ and a $\tfrac12$.
> 5. **"Good conductor" is a statement about $\sigma/\omega\epsilon$ at one frequency**, not about the material.
> 6. **$\mu\ne\mu_0$** enters $\gamma$ and $\eta$. Use the medium's $\mu$ in $\gamma\eta = j\omega\mu$.
> 7. **Linear needs only $\phi = 0$ or $\pi$**, with any amplitudes. **Circular needs both** equal amplitudes and $\pm90^\circ$. Handedness depends on the travel direction.
> 8. **$\Gamma$ is (far side $-$ near side) over the sum**, the near side being where the wave comes from. Swapping them flips the sign.
> 9. **Reflected $\mathbf{H}$ and reflected current carry $-\Gamma$.**
> 10. **A load voltage is incident plus reflected,** $(1+\Gamma_L)V^+$, never the incident wave alone unless the load is matched. One official key makes this slip ([[exams/e3-sp18#3-voltage-and-current-bounce-diagrams-30-points|SP18 #3(d)]]).
> 11. **$\tau_g = Z_0/(R_g+Z_0)$ is a voltage divider.** It is not $1+\Gamma_g$.
> 12. **Timing:** the echo is back at $z = 0$ at $2T$, not $T$. With two lines there are two different $T$'s.
> 13. **Steady state of a step is a DC circuit.** Do not run the bounce sum when a divider will do; use the divider to check the sum.
> 14. **Units on every answer:** Np/m, rad/m, $\Omega$, W/m², A/m, V. The answer boxes ask for them.
> 15. **No calculator:** leave $\pi$, $\sqrt3$ and fractions. An ugly decimal usually means an arithmetic slip.

> [!trap] Earlier-lecture slips that still cost points here
> - **$\hat n$ in a boundary condition** points from medium 2 into medium 1. On a line's plates, $\rho_s = \hat n\cdot\mathbf{D}$ and $\mathbf{J}_s = \hat n\times\mathbf{H}$ with $\hat n$ out of the metal.
> - **$\mathbf{H}$ flips across a current sheet;** the sheet's $\mathbf{E}$ opposes $\mathbf{J}_s$ on both sides.
> - **Speed from an expression is a ratio of coefficients:** $\cos(\omega t-\beta z)$ moves at $\omega/\beta$, not at $\beta$.
> - **A snapshot of a forward wave is its time record mirrored:** what left first is farthest along.

## 11. What to put on the index card

One 4″×6″ card. Whether a formula page is also handed out is not stated, so the card should stand alone. Write it yourself: making it is a review session. Build it around Lectures 21–30, in order of value per square centimetre:

1. **The regime table of §4** (six rows, three columns). It was printed on some past third exams and not on others.
2. $\gamma\eta = j\omega\mu$, $\ \gamma/\eta = \sigma+j\omega\epsilon$, $\ \sigma/\omega\epsilon = \tan2\tau$, $\ \langle S\rangle = \dfrac{\lvert E_0\rvert^2}{2\lvert\eta\rvert}e^{-2\alpha z}\cos\tau$.
3. **Handedness:** "toward $+z$: $\hat x-j\hat y$ right, $\hat x+j\hat y$ left; $\sin\to-j$".
4. $\Gamma$, $\tau$ for waves, with "$\tilde{\mathbf{H}}_r$ gets $-\Gamma$", and the mirror's standing wave: $\mathbf{E}\propto\sin\beta z\sin\omega t$, $\mathbf{H}\propto\cos\beta z\cos\omega t$.
5. **Lines:** $Z_0 = \eta d/W$ (plates), $\dfrac{\eta}{2\pi}\ln\dfrac ba$ (coax); $\tau_g$, $\Gamma_L$, $\Gamma_g$; "current: $-\Gamma$"; junction $\Gamma_{jk}$, $\tau_{jk} = 1+\Gamma_{jk}$; the DC check.
6. Constants: $\epsilon_0 = 10^{-9}/36\pi$, $\mu_0 = 4\pi\times10^{-7}$, $\eta_0 = 120\pi$, $c = 3\times10^8$; $\sigma/\omega\epsilon = 18\times10^9\sigma/(f\epsilon_r)$.
7. Your own two or three recurring mistakes from the timed papers, in your own words. This line is worth the most.

**One corner for the earlier formulas these problems need** (§9), four lines at most:

8. $\mathbf{H} = \hat u\times\mathbf{E}/\eta$; sheet: $\mathbf{E} = -\tfrac\eta2\mathbf{J}_s(t-\lvert\xi\rvert/v)$, $\mathbf{H} = \tfrac12\mathbf{J}_s\times\hat n$.
9. The four boundary conditions with "$\hat n$ from 2 into 1"; at a perfect conductor $\rho_s = \hat n\cdot\mathbf{D}$, $\mathbf{J}_s = \hat n\times\mathbf{H}$.
10. $\mathcal{C} = \epsilon W/d$, $\mathcal{L} = \mu d/W$, $\mathcal{L}\mathcal{C} = \mu\epsilon$.

Leave off what you can rebuild in ten seconds ($\lambda = 2\pi/\beta$, $v_p = \omega/\beta$) and the [[0-toolkit/04-errata-in-the-course-materials|known slips in the course materials]]. If you still have room and want insurance on the earlier units, the Maxwell table from your Midterm 2 card is the densest thing to add.

## 12. What the homeworks drilled

The announcement says the problems will be like "past exams or questions from HWs". The homeworks since Midterm 2 are HW8–HW11, and they are the ones to redo. Exams reuse the homework's *moves*, not its numbers: redo a problem on blank paper before looking at your old answer.

- **HW8–HW10:** problem by problem in the table below. HW10's official solutions are not in the course folder, so its rows give the method only.
- **HW11:** in scope, but not in the course folder yet, so it is **not mapped here**. By the weekly pattern it is on transmission lines; the [[practice/28-bounce-diagrams|Lecture 28]], [[practice/29-bounce-diagram-examples|29]] and [[practice/30-multi-line-circuits|30]] practice sets are the closest practice.
- **HW1–HW7** are named by the announcement too. They are background here: HW5–HW7 are mapped problem by problem in the [[0-toolkit/05-midterm-2-summary#12-what-homeworks-57-drilled|Midterm 2 summary, §12]], and HW1–HW4 by set in the folded box at the end of this section.

| problem | what it asked | the method | read · practise |
|---|---|---|---|
| HW8 #1 | $\mathbf{E}$ and $\mathbf{H}$ of a wave in an unknown lossless medium, one waveform missing: $\eta$, $v$, $\epsilon_r$, $\mu_r$, the missing waveform | pair each $\mathbf{E}$ term with the $\mathbf{H}$ term travelling the same way; their ratio is $\eta$, the argument gives $v$; then $\mu_r\epsilon_r = (c/v)^2$ and $\mu_r/\epsilon_r = (\eta/\eta_0)^2$ | [[homework/hw8-waves-in-free-space#1-reading-a-medium-off-a-pair-of-fields\|companion §1]] · [[practice/18-wave-equation-and-plane-waves#189-triangle-pulse-in-a-magnetic-medium\|18.9]] |
| HW8 #2 | a pulsed current sheet: fields on both sides, plots, radiated energy | $\mathbf{E} = -\tfrac\eta2\mathbf{J}_s(t-\lvert\xi\rvert/v)$ on both sides ($\xi$ = distance from the sheet), $\mathbf{H}$ flips; fix $z$ for a record, fix $t$ for a snapshot | [[homework/hw8-waves-in-free-space#2-a-pulsed-current-sheet-fields-plots-radiated-energy\|companion §2]] · [[practice/19-radiation-from-current-sheets#199-a-sheet-launches-a-step-and-a-ramp\|19.9]] |
| HW8 #3 | a cosine wave in a dielectric: its parameters, $\mathbf{H}$, the Poynting vector | $\omega$ and $\beta$ off the expression, then $v_p$, $\lambda$, $\epsilon_r$, $\eta$; $\mathbf{H} = \hat u\times\mathbf{E}/\eta$; $\langle S\rangle = E_0^2/2\eta$ | [[homework/hw8-waves-in-free-space#3-a-monochromatic-wave-in-a-dielectric-parameters-h-poynting\|companion §3]] · [[practice/21-phasors-and-monochromatic-waves#211-reading-two-waves\|21.1]] |
| HW8 #4 | five waves: the partner field, the phasors, instantaneous and average power | §2 of this page, wave by wave; write each cross product out | [[homework/hw8-waves-in-free-space#4-five-waves-partner-field-phasors-instantaneous-and-average-power\|companion §4]] · [[practice/21-phasors-and-monochromatic-waves#217-partner-fields-on-three-axes\|21.7]], [[practice/21-phasors-and-monochromatic-waves#212-phasors-both-ways\|21.2]] |
| HW9 #1 | three waves described in words (medium, polarization, direction of $\mathbf{S}$, $\omega$ or $\lambda$): $\eta$, $v$, $\lambda$, the fields in time and as phasors, the complex and average Poynting vectors | $\eta = \eta_0\sqrt{\mu_r/\epsilon_r}$, $v = c/\sqrt{\mu_r\epsilon_r}$; the direction of $\mathbf{S}$ is $\hat u$; then §2 | [[3-maxwell-and-waves/21-monochromatic-waves-and-phasor-notation\|Lecture 21]] · [[practice/21-phasors-and-monochromatic-waves#211-reading-two-waves\|21.1]], [[practice/21-phasors-and-monochromatic-waves#217-partner-fields-on-three-axes\|21.7]] |
| HW9 #2 | a sinusoidal sheet that sends a given power to each side: $E_0$, $H_0$, $J_{s0}$, then the phasors | each side carries $E_0^2/2\eta_0$; the sheet supplies $\tfrac12J_{s0}E_0$ per unit area, the two sides together; $-\sin\leftrightarrow+j$ | [[problems/energy-bookkeeping-for-a-radiating-sheet\|worked problem]] · [[practice/20-poynting-theorem-and-power#2010-a-sheet-in-a-magnetic-medium\|20.10]] |
| HW9 #3 | a damped $\mathbf{H}$ given in time: $\gamma$, $\eta$, $\epsilon$, $\sigma$, $\tilde{\mathbf{E}}$, $\langle\mathbf{S}\rangle$, the power dissipated in a cube | the decode of §3, starting from $\mathbf{H}$ ($\tilde{\mathbf{E}} = \eta\tilde{\mathbf{H}}\times\hat u$, phase **plus** $\tau$); dissipated power = flux in minus flux out | [[problems/decoding-a-damped-wave\|worked problem]] · [[practice/22-damped-waves-in-conducting-media#229-decoding-a-wave-toward-minus-y\|22.9]], [[practice/22-damped-waves-in-conducting-media#228-power-soaking-into-lossy-ground\|22.8]] |
| HW9 #4 | seawater at two low frequencies: $\alpha$, $\eta$, the depth where the field is 1 %, $\lambda$ | check $\sigma/\omega\epsilon\gg1$, then the good-conductor column of §4; $e^{-\alpha d} = 0.01$ gives $d = \ln100/\alpha$ | [[3-maxwell-and-waves/23-imperfect-dielectrics-and-good-conductors\|Lecture 23]] · [[practice/23-imperfect-dielectrics-and-good-conductors#239-down-into-a-deep-lake\|23.9]], [[practice/23-imperfect-dielectrics-and-good-conductors#2310-calling-a-submarine\|23.10]] |
| HW9 #5 | a cosine sheet off the origin in a dielectric: $v$, $\beta$, $\lambda$, $\eta$, the fields on both sides, power through an area, $\langle\mathbf{J}_s\cdot\mathbf{E}\rangle$ | distance from the sheet is $\lvert x-x_0\rvert$; $\langle S\rangle = \eta J_{s0}^2/8$ per side; $\langle\mathbf{J}_s\cdot\mathbf{E}\rangle = -\eta J_{s0}^2/4$ in W/m² | [[practice/19-radiation-from-current-sheets#198-a-cosine-current-in-a-dielectric\|19.8]], [[practice/20-poynting-theorem-and-power#2010-a-sheet-in-a-magnetic-medium\|20.10]] |
| HW10 #1 | a slightly damped phasor in a magnetic medium with $v_p$ given: $f$, $\lambda$, $\epsilon_r$, $\sigma$, the $1/e$ distance, $\tilde{\mathbf{H}}$ | $\alpha\ll\beta$: imperfect dielectric. $\omega = \beta v_p$; $\mu_r\epsilon_r = (c/v_p)^2$; $\eta = \sqrt{\mu/\epsilon}$; $\sigma = 2\alpha/\eta$; $\delta = 1/\alpha$ | [[3-maxwell-and-waves/23-imperfect-dielectrics-and-good-conductors\|Lecture 23]] · [[practice/23-imperfect-dielectrics-and-good-conductors#236-wavelength-and-depth-measured-underground\|23.6]], [[practice/23-imperfect-dielectrics-and-good-conductors#238-the-missing-permittivity\|23.8]] |
| HW10 #2 | seawater at 1 kHz and at 1 GHz: $\gamma$, $\lambda$, $\delta$, $\eta$ with the right approximation for each; a submarine's depth for a given fraction of the surface field | classify first: good conductor at 1 kHz; at 1 GHz $\sigma/\omega\epsilon\approx0.9$, in between, where this site would use the exact $\gamma$ and $\eta$ of §3 (the official solution is not on hand to show which approximation it accepts); depth from $e^{-\alpha d}$ | [[concepts/loss-tangent\|Loss tangent]] · [[practice/23-imperfect-dielectrics-and-good-conductors#231-six-media-at-one-frequency\|23.1]], [[practice/23-imperfect-dielectrics-and-good-conductors#239-down-into-a-deep-lake\|23.9]], [[practice/23-imperfect-dielectrics-and-good-conductors#2310-calling-a-submarine\|23.10]] |
| HW10 #3 | five waves given through $\mathbf{E}$ or $\mathbf{H}$: both phasors, and the polarization | sines to cosines; the other field by $\hat u\times$; then the table of §5 and the handedness rule | [[3-maxwell-and-waves/24-signal-transmission-and-circular-polarization\|Lecture 24]] · [[practice/24-group-velocity-and-polarization#243-name-four-polarizations\|24.3]], [[practice/24-group-velocity-and-polarization#248-starting-from-h\|24.8]] |
| HW10 #4 | two sheets a quarter wavelength apart with a free phase: the phase for right circular, left circular and linear; $\langle\mathbf{S}\rangle$ for circular and for linear | write each sheet's wave in the region beyond both; the farther sheet's wave has travelled $\lambda/4$ more, a factor $e^{-j\pi/2} = -j$; then §5; circular carries twice the linear power for the same peak field | [[problems/two-sheets-a-quarter-wave-apart\|worked problem]] · [[practice/21-phasors-and-monochromatic-waves#2110-two-sheets-two-current-directions\|21.10]], [[practice/24-group-velocity-and-polarization#2412-an-elliptically-rotating-sheet-current\|24.12]] |

> [!note]- Homeworks 1–4 by set (background)
> | set | what it drilled | read · practise |
> |---|---|---|
> | HW1 | vector algebra; force and field of point charges; fields deduced from measured forces; the flux of a current density through the faces of a cube; charge and current densities of a plasma | [[1-electrostatics/01-fields-forces-and-the-maxwell-roadmap\|L1]], [[1-electrostatics/02-coulombs-law-superposition-and-gauss\|L2]] · [[practice/02-coulombs-law-superposition-and-gauss#21-coulomb-force-as-a-vector\|2.1]], [[practice/02-coulombs-law-superposition-and-gauss#22-where-the-field-vanishes\|2.2]], [[practice/02-coulombs-law-superposition-and-gauss#23-charge-at-a-cube-corner\|2.3]] |
> | HW2 | a charge moving in a field; Gauss's law for sheets, slabs and a charged cylinder; two unknown charges from the field they make; sketching and computing divergence and curl; $\mathbf{E}$, its curl and its divergence from a potential | [[1-electrostatics/02-coulombs-law-superposition-and-gauss\|L2]]–[[1-electrostatics/05-curl-free-fields-and-the-electrostatic-potential\|L5]] · [[practice/02-coulombs-law-superposition-and-gauss#212-two-charges-one-given-field\|2.12]], [[practice/03-gauss-law-at-work#31-two-sheets-of-charge\|3.1]], [[practice/03-gauss-law-at-work#39-two-slabs-and-a-sheet\|3.9]], [[practice/04-divergence-and-curl#41-faucet-or-whirlpool\|4.1]], [[practice/05-electrostatic-potential#54-field-from-a-potential\|5.4]] |
> | HW3 | the vacuum diode (Poisson's equation); $\nabla\cdot\mathbf{E}$ from a potential; circulation of two fields around a triangle; $\mathbf{D}$ from sheet charges written with $\delta$ functions; a charged metal sphere | [[1-electrostatics/04-divergence-and-curl\|L4]]–[[1-electrostatics/08-conductors-dielectrics-and-polarization\|L8]] · [[practice/07-poisson-and-laplace#710-space-charge-limited-vacuum-diode\|7.10]], [[practice/05-electrostatic-potential#56-two-fields-three-paths\|5.6]], [[practice/03-gauss-law-at-work#34-charges-written-with-delta-functions\|3.4]], [[practice/04-divergence-and-curl#410-charge-layers-from-a-piecewise-d\|4.10]] |
> | HW4 | charged parallel plates; plates with a charged sheet between them; two dielectric slabs between plates; the discharge of a lossy capacitor; a slab slid between charged plates; a coax with layered materials | [[1-electrostatics/06-circulation-and-boundary-conditions\|L6]]–[[1-electrostatics/10-capacitance-and-conductance\|L10]] · [[practice/07-poisson-and-laplace#78-plates-and-a-charged-sheet\|7.8]], [[practice/10-capacitance-and-conductance#106-two-layers-between-charged-plates\|10.6]], [[practice/10-capacitance-and-conductance#107-one-slab-two-placements\|10.7]], [[practice/10-capacitance-and-conductance#1011-two-lossy-layers-in-series\|10.11]], [[problems/two-layer-coaxial-capacitor\|worked problem]] |

## 13. The days left: a plan

Most of the time goes to Lectures 21–30, to Homeworks 8–10 (and 11 when you have it back) and to past Exam 3 papers worked timed. One short slot refreshes the earlier tools of §9.

> [!tip] Wednesday to Monday
> Short weekday blocks, two timed papers at the weekend. If a block runs over, stop: the next day's block matters more than finishing this one.
>
> **Wednesday, November 11 (about 90 min): where do I stand, and lossy media.**
> 1. *20 min.* Read §1–4, close the page, write the regime table and the equations of §3 from memory. Mark what was missing.
> 2. *70 min.* [[practice/22-damped-waves-in-conducting-media#223-reading-a-damped-wave|22.3]] (easy), then [[practice/22-damped-waves-in-conducting-media#229-decoding-a-wave-toward-minus-y|22.9]] (modelled on a past paper's 27-point decode problem), then [[practice/23-imperfect-dielectrics-and-good-conductors#235-power-against-depth-in-seawater|23.5]] and [[practice/23-imperfect-dielectrics-and-good-conductors#236-wavelength-and-depth-measured-underground|23.6]].
>
> **Thursday, November 12 (about 90 min): polarization and reflection.**
> 3. [[practice/24-group-velocity-and-polarization#243-name-four-polarizations|24.3]], [[practice/24-group-velocity-and-polarization#244-true-or-false-on-one-wave|24.4]], then [[practice/24-group-velocity-and-polarization#2410-a-wave-with-a-free-phase|24.10]] (a past paper's 18-point problem).
> 4. [[practice/25-reflection-and-transmission#251-four-interfaces|25.1]], [[practice/25-reflection-and-transmission#259-out-of-the-glass|25.9]] (work back from the transmitted wave), [[practice/26-standing-waves-and-radiation-pressure#262-standing-waves-true-or-false|26.2]]. If Homework 11 is due tonight, finishing it carefully counts as Friday's first step.
>
> **Friday, November 13 (about 2 h): bounce diagrams.**
> 5. Read the recipe in §8, then [[practice/28-bounce-diagrams#281-three-coefficients|28.1]], [[practice/28-bounce-diagrams#289-voltage-and-current-diagrams|28.9]], [[practice/29-bounce-diagram-examples#296-both-ends-of-a-short-line|29.6]], [[practice/29-bounce-diagram-examples#298-one-pulse-and-nothing-else|29.8]].
> 6. [[practice/30-multi-line-circuits#301-coefficients-both-ways|30.1]] and [[practice/30-multi-line-circuits#308-three-sections-and-the-first-echoes|30.8]], then the slide examples of [[4-transmission-lines/30-multi-line-circuits|Lecture 30]]: cover the answers and rebuild the three-line cascade and the reflectometry problem.
>
> **Saturday, November 14: first timed paper, and the homeworks.**
> 7. *Morning.* **SP18 Exam 3** from the blank copy, skipping #1(vi), (viii)–(x) and #4 (Lectures 31–34, not on your exam): about 50 minutes, no calculator, a draft of your card. Grade it with the [[exams/e3-sp18|SP18 guide]] open.
> 8. *Afternoon.* For each part you missed, its method and its twin. Then redo, on blank paper, the HW8–HW10 problems you lost points on (§12), and HW11's.
> 9. *Late afternoon (30–40 min): the earlier tools.* Read the table in §9 and do two of its four problems. This is the only block on pre-Midterm 2 material; it is enough unless the table surprises you.
> 10. *Evening.* Write the real index card (§11).
>
> **Sunday, November 15: second timed paper, then stop.**
> 11. *Morning.* **FA23 Exam 3**, #1–#6 ([[exams/e3-fa23|guide]]), covering the written answers, using the card you made.
> 12. *Afternoon.* Fix what you missed. If energy is left: SP19 #1, #2 and #4 ([[exams/e3-sp19|guide]]).
> 13. *Evening, light.* Reread §10 and your card. Stop by 11 pm; sleep is worth more than a third paper.
>
> **Monday, November 16 (45 min at most before the exam).** Write the card's contents from memory once, redo two problems you got wrong. Nothing new.

If you have less time than this, keep steps 1, 5, 7 and 8. On the past third exams on hand, bounce diagrams are 25 to 54 points and the damped-wave decode was a 25- or 27-point problem on two of the four. Both are procedures: they reward practice more than anything else here.

## 14. The practice list

Two to five problems per lecture, chosen to match the past papers: *exam* marks problems modelled on one. Easy ones first; if an easy one takes more than ten minutes, reread that lecture's key boxes before going on.

- **Lecture 21** (phasors, power): [[practice/21-phasors-and-monochromatic-waves#211-reading-two-waves|21.1]] (easy) · [[practice/21-phasors-and-monochromatic-waves#214-which-electric-field|21.4]] (easy, exam) · [[practice/21-phasors-and-monochromatic-waves#217-partner-fields-on-three-axes|21.7]] (medium) · [[practice/21-phasors-and-monochromatic-waves#2110-two-sheets-two-current-directions|21.10]] (hard, exam)
- **Lecture 22** (damped waves): [[practice/22-damped-waves-in-conducting-media#223-reading-a-damped-wave|22.3]] (easy) · [[practice/22-damped-waves-in-conducting-media#224-possible-or-not-possible|22.4]] (easy, exam) · [[practice/22-damped-waves-in-conducting-media#228-power-soaking-into-lossy-ground|22.8]] (medium, exam) · [[practice/22-damped-waves-in-conducting-media#229-decoding-a-wave-toward-minus-y|22.9]] (hard, exam) · [[practice/22-damped-waves-in-conducting-media#2210-two-components-in-a-magnetic-medium|22.10]] (hard, exam)
- **Lecture 23** (regimes, skin depth): [[practice/23-imperfect-dielectrics-and-good-conductors#231-six-media-at-one-frequency|23.1]] (easy) · [[practice/23-imperfect-dielectrics-and-good-conductors#232-inside-a-good-conductor|23.2]] (easy, exam) · [[practice/23-imperfect-dielectrics-and-good-conductors#235-power-against-depth-in-seawater|23.5]] (easy, exam) · [[practice/23-imperfect-dielectrics-and-good-conductors#236-wavelength-and-depth-measured-underground|23.6]] (medium, exam) · [[practice/23-imperfect-dielectrics-and-good-conductors#239-down-into-a-deep-lake|23.9]] (hard, exam)
- **Lecture 24** (polarization): [[practice/24-group-velocity-and-polarization#243-name-four-polarizations|24.3]] (easy) · [[practice/24-group-velocity-and-polarization#244-true-or-false-on-one-wave|24.4]] (easy, exam) · [[practice/24-group-velocity-and-polarization#248-starting-from-h|24.8]] (medium) · [[practice/24-group-velocity-and-polarization#249-building-a-right-circular-wave|24.9]] (hard, exam) · [[practice/24-group-velocity-and-polarization#2410-a-wave-with-a-free-phase|24.10]] (hard, exam)
- **Lecture 25** (reflection): [[practice/25-reflection-and-transmission#251-four-interfaces|25.1]] (easy) · [[practice/25-reflection-and-transmission#253-into-a-good-conductor|25.3]] (easy, exam) · [[practice/25-reflection-and-transmission#259-out-of-the-glass|25.9]] (hard, exam) · [[practice/25-reflection-and-transmission#2511-a-circular-wave-on-a-mirror|25.11]] (hard, exam) · [[practice/25-reflection-and-transmission#2512-identifying-a-material|25.12]] (hard, exam)
- **Lecture 26** (standing waves): [[practice/26-standing-waves-and-radiation-pressure#261-nodes-in-front-of-a-mirror|26.1]] (easy) · [[practice/26-standing-waves-and-radiation-pressure#262-standing-waves-true-or-false|26.2]] (easy, exam) · [[practice/26-standing-waves-and-radiation-pressure#263-travelling-standing-or-both|26.3]] (easy, exam) · [[practice/26-standing-waves-and-radiation-pressure#269-is-it-a-standing-wave|26.9]] (hard, exam)
- **Lecture 27** (line basics): [[practice/27-transmission-line-basics#271-strip-line-parameters|27.1]] (easy) · [[practice/27-transmission-line-basics#272-telegraphers-equations-true-or-false|27.2]] (easy, exam) · [[practice/27-transmission-line-basics#273-charges-and-currents-on-turned-plates|27.3]] (easy, exam) · [[practice/27-transmission-line-basics#277-two-bench-measurements|27.7]] (medium, exam) · [[practice/27-transmission-line-basics#279-a-pulse-on-a-coax|27.9]] (hard, exam)
- **Lecture 28** (bounce diagrams): [[practice/28-bounce-diagrams#281-three-coefficients|28.1]] (easy, exam) · [[practice/28-bounce-diagrams#283-a-step-meets-four-loads|28.3]] (easy) · [[practice/28-bounce-diagrams#288-snapshots-along-a-shorted-line|28.8]] (medium, exam) · [[practice/28-bounce-diagrams#289-voltage-and-current-diagrams|28.9]] (hard, exam) · [[practice/28-bounce-diagrams#2810-a-pulse-into-a-resistive-load|28.10]] (hard, exam)
- **Lecture 29** (pulses, records, snapshots): [[practice/29-bounce-diagram-examples#293-a-switched-on-sine|29.3]] (easy) · [[practice/29-bounce-diagram-examples#296-both-ends-of-a-short-line|29.6]] (medium, exam) · [[practice/29-bounce-diagram-examples#298-one-pulse-and-nothing-else|29.8]] (medium, exam) · [[practice/29-bounce-diagram-examples#299-one-sine-cycle-on-a-mismatched-line|29.9]] (hard, exam) · [[practice/29-bounce-diagram-examples#2910-a-ramp-into-an-open-line|29.10]] (hard, exam)
- **Lecture 30** (cascaded lines): [[practice/30-multi-line-circuits#301-coefficients-both-ways|30.1]] (easy) · [[practice/30-multi-line-circuits#303-no-echo-toward-the-source|30.3]] (easy, exam) · [[practice/30-multi-line-circuits#308-three-sections-and-the-first-echoes|30.8]] (medium, exam) · [[practice/30-multi-line-circuits#309-two-lines-and-a-mismatched-source|30.9]] (hard, exam) · [[practice/30-multi-line-circuits#3010-locating-a-splice-by-its-echoes|30.10]] (hard, exam)
- **The earlier tools of §9** (a short refresh, not a second list): [[practice/18-wave-equation-and-plane-waves#189-triangle-pulse-in-a-magnetic-medium|18.9]] (hard, exam) · [[practice/19-radiation-from-current-sheets#198-a-cosine-current-in-a-dielectric|19.8]] (medium) · [[practice/20-poynting-theorem-and-power#202-joule-heating-at-a-point|20.2]] (easy, exam) · [[practice/16-charge-conservation-and-displacement-current#1612-four-conditions-at-a-tilted-interface|16.12]] (hard, exam)

**Worked problems** (full write-ups, one per type): [[problems/decoding-a-damped-wave|decoding a damped wave]] · [[problems/a-radio-wave-into-moist-ground|a radio wave into moist ground]] · [[problems/two-sheets-a-quarter-wave-apart|two sheets a quarter wave apart]] · [[problems/working-back-from-a-transmitted-wave|working back from a transmitted wave]] · [[problems/a-circular-wave-meets-a-mirror|a circular wave meets a mirror]] · [[problems/a-backward-pulse-on-a-parallel-plate-line|a backward pulse on a parallel-plate line]] · [[problems/reading-a-line-from-two-pulses|reading a line from two pulses]] · [[problems/a-ramp-pulse-meets-its-echo|a ramp pulse meets its echo]] · [[problems/echoes-trapped-on-the-second-line|echoes trapped on the second line]]

**Past papers:** which to work, in what order and how, is on the [[exams/index#the-papers|Midterm 3 review]] page. The randomized concept checks for Lectures 20–30 on [pl.vops.ch](https://pl.vops.ch) (Practice 7 in the [[0-toolkit/06-prairielearn-guide|PrairieLearn guide]]) make a good ten-minute warm-up.

**If you want more from before Midterm 2:** the practice list in the [[0-toolkit/05-midterm-2-summary#13-how-to-study-for-it-exam-monday-october-19|Midterm 2 summary, §13]] for Lectures 11–20, and the [[practice/index|practice hub]] for Lectures 2–10. Lectures 31–33 and their practice sets are on the site but are **not on this exam**.

### Sources for this page

The site's Lecture 21–30 pages and topic pages, which follow the course notes and slides; the earlier lecture pages for §9; Homeworks 8–10 as posted (HW9 with its posted solutions, re-solved in `tools/build14/checks/hw9.py`; HW10 from its statement only; HW1–4 summarized by set). Numbers and formulas quoted here are computed in `tools/build14/checks/twins.py` and `summary3.py`. The scope and the rules in the header line are the announcement's, as the student passed it on; that the exam is expected to be mostly post-Midterm 2 material is the student's understanding of the course, consistent with the four past Exam 3 papers on hand.
