---
title: "Intrinsic impedance"
description: "η = √(μ/ε), the |E|/|H| of one plane wave: 376.7 Ω in vacuum, η₀√(μr/εr) in a medium, complex (H lags E) in a conductor. How H follows from E, the sign table, speed and impedance in matter and on a cable."
tags: [concept, waves]
aliases: ["wave impedance", "impedance of free space", "H from E", "eta", "speed and impedance in a medium", "refractive index"]
---

> [!key] The plane-wave pair and the intrinsic impedance
> $$
> \begin{gathered}
> E_x = A f\Big(t-\frac zv\Big) + B g\Big(t+\frac zv\Big),\qquad H_y = \frac1\eta\Big[A f\Big(t-\frac zv\Big) - B g\Big(t+\frac zv\Big)\Big],\\[6pt]
> \eta\equiv\sqrt{\frac\mu\epsilon} = \mu v = \frac{1}{\epsilon v}\ [\Omega],\qquad \eta_0 = \sqrt{\frac{\mu_0}{\epsilon_0}} = 376.7\ \Omega\approx120\pi\ \Omega .
> \end{gathered}
> $$
> One wave: $E_x/H_y = +\eta$ toward $+z$, $-\eta$ toward $-z$. Units: (V/m)/(A/m) = Ω; H/F = Ω². With $\mathbf{B} = \mu\mathbf{H}$: $\lvert\mathbf{B}\rvert = \lvert\mathbf{E}\rvert/v$, a quick check. The notes' general rule — **$\mathbf{H}$ is $\mathbf{E}$ divided by $\eta$ and rotated 90° so that $\mathbf{E}\times\mathbf{H}$ points the way the wave travels**; $\mathbf{E}$ is $\eta\mathbf{H}$ rotated back — with $\hat u$ the direction of travel:
> $$
> \mathbf{H} = \frac1\eta\,\hat u\times\mathbf{E},\qquad \mathbf{E} = \eta\,\mathbf{H}\times\hat u .
> $$
>
> **Speed and impedance in a medium:**
> $$
> v = \frac{c}{\sqrt{\mu_r\epsilon_r}},\qquad \eta = \eta_0\sqrt{\frac{\mu_r}{\epsilon_r}} .
> $$
> Both slow the wave; $\epsilon_r$ lowers $\eta$, $\mu_r$ raises it. $c/v = \sqrt{\mu_r\epsilon_r}$ is the refractive index of optics. Nothing in the derivation needed vacuum: in a linear medium ([[concepts/permeability|Permeability, susceptibility, and B = μH]] for $\mu = \mu_r\mu_0$, [[concepts/permittivity|Permittivity, susceptibility, and D = εE]] for $\epsilon = \epsilon_r\epsilon_0$) bound charges and currents are already inside $\mu$ and $\epsilon$.

**Physics: H from E.** *From Faraday's law (notes).* For $E_x = f(t - z/v)$, $\partial E_x/\partial z = -f'/v$, so $-\mu\,\partial H_y/\partial t = -f'/v$; integrating in time (dropping a static constant), $H_y = f/(\mu v)$. Since $\mu v = \mu/\sqrt{\mu\epsilon} = \sqrt{\mu/\epsilon}$, call it $\eta$: $H_y = f/\eta$. For $E_x = g(t + z/v)$ the $z$-derivative flips sign: $H_y = -g/\eta$.

*From Ampère–Maxwell (slides).* $\partial H_y/\partial z = -\epsilon\,\partial E_x/\partial t = -\epsilon\,[A f' + B g']$. Integrate in $z$ with $\int f'(t - z/v)\,dz = -v f$ and $\int g'(t + z/v)\,dz = +v g$:

$$
H_y = \epsilon v\,\big[A f - B g\big] = \frac1\eta\big[A f - B g\big],\qquad\text{since }\ \epsilon v = \sqrt{\epsilon/\mu} = 1/\eta .
$$

The $z$-integration "constant" is a function of $t$; Faraday's law forces it constant in time too, a uniform static field, set to zero (slide 21 drops it silently; slide 9's "we can turn off our source"). The routes agree and each satisfies *both* component equations (flipping the sign of $Bg$ breaks Ampère's law). $\mathbf{E}\times\mathbf{H}$ is the [[concepts/poynting-vector|Poynting vector]], here only the direction rule (ink: "$\mathbf{E}\times\mathbf{H}\to$ propagation direction"); as power per unit area, Lecture 20. Not a resistor: nothing is dissipated.

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 340" width="640" height="340" role="img" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:14px"><defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="context-stroke"/></marker><marker id="ahs" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="context-stroke"/></marker></defs><text x="190.0" y="22.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-weight:600;">travel toward +z</text><text x="500.0" y="22.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-weight:600;">travel toward −z</text><text x="16.0" y="112.0" text-anchor="middle" fill="currentColor" style="font-size:12.5px;font-weight:600;" transform="rotate(-90 16 112)">x-polarized</text><text x="16.0" y="268.0" text-anchor="middle" fill="currentColor" style="font-size:12.5px;font-weight:600;" transform="rotate(-90 16 268)">y-polarized</text><line x1="34.0" y1="186.0" x2="630.0" y2="186.0" stroke="var(--muted)" stroke-width="1" stroke-dasharray="3 4" stroke-linecap="round"/><line x1="340.0" y1="34.0" x2="340.0" y2="330.0" stroke="var(--muted)" stroke-width="1" stroke-dasharray="3 4" stroke-linecap="round"/><line x1="128.0" y1="108.0" x2="128.0" y2="62.0" stroke="var(--muted)" stroke-width="1" stroke-dasharray="3 3" stroke-linecap="round"/><text x="128.0" y="57.7" text-anchor="middle" fill="var(--muted)" style="font-size:11px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">x</text><line x1="128.0" y1="108.0" x2="99.5" y2="130.1" stroke="var(--muted)" stroke-width="1" stroke-dasharray="3 3" stroke-linecap="round"/><text x="94.3" y="138.1" text-anchor="middle" fill="var(--muted)" style="font-size:11px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">y</text><line x1="128.0" y1="108.0" x2="174.0" y2="108.0" stroke="var(--muted)" stroke-width="1" stroke-dasharray="3 3" stroke-linecap="round"/><text x="186.3" y="112.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">z</text><line x1="128.0" y1="108.0" x2="192.0" y2="108.0" stroke="currentColor" stroke-width="3.2" marker-end="url(#ah)" stroke-linecap="round"/><line x1="128.0" y1="108.0" x2="128.0" y2="52.0" stroke="var(--accent)" stroke-width="2.6" marker-end="url(#ah)" stroke-linecap="round"/><line x1="128.0" y1="108.0" x2="97.0" y2="132.0" stroke="var(--accent2)" stroke-width="2.6" marker-end="url(#ah)" stroke-linecap="round"/><text x="136.0" y="44.0" text-anchor="middle" fill="var(--accent)" style="font-size:13px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;font-weight:700;">E</text><text x="87.5" y="143.3" text-anchor="middle" fill="var(--accent2)" style="font-size:13px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;font-weight:700;">H</text><text x="163.2" y="100.0" text-anchor="middle" fill="currentColor" style="font-size:11px;">travel</text><text x="212.0" y="74.0" text-anchor="start" fill="var(--accent)" style="font-size:11.5px;font-weight:600;">E = x̂ f(t − z/v)</text><text x="212.0" y="92.0" text-anchor="start" fill="var(--accent2)" style="font-size:11.5px;font-weight:600;">H = +ŷ f(t − z/v)/η</text><text x="212.0" y="110.0" text-anchor="start" fill="currentColor" style="font-size:11.5px;">E × H along +ẑ</text><line x1="433.0" y1="108.0" x2="433.0" y2="62.0" stroke="var(--muted)" stroke-width="1" stroke-dasharray="3 3" stroke-linecap="round"/><text x="433.0" y="57.7" text-anchor="middle" fill="var(--muted)" style="font-size:11px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">x</text><line x1="433.0" y1="108.0" x2="404.5" y2="130.1" stroke="var(--muted)" stroke-width="1" stroke-dasharray="3 3" stroke-linecap="round"/><text x="399.3" y="138.1" text-anchor="middle" fill="var(--muted)" style="font-size:11px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">y</text><line x1="433.0" y1="108.0" x2="479.0" y2="108.0" stroke="var(--muted)" stroke-width="1" stroke-dasharray="3 3" stroke-linecap="round"/><text x="491.3" y="112.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">z</text><line x1="433.0" y1="108.0" x2="369.0" y2="108.0" stroke="currentColor" stroke-width="3.2" marker-end="url(#ah)" stroke-linecap="round"/><line x1="433.0" y1="108.0" x2="433.0" y2="52.0" stroke="var(--accent)" stroke-width="2.6" marker-end="url(#ah)" stroke-linecap="round"/><line x1="433.0" y1="108.0" x2="464.0" y2="84.0" stroke="var(--accent2)" stroke-width="2.6" marker-end="url(#ah)" stroke-linecap="round"/><text x="441.0" y="44.0" text-anchor="middle" fill="var(--accent)" style="font-size:13px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;font-weight:700;">E</text><text x="473.5" y="80.7" text-anchor="middle" fill="var(--accent2)" style="font-size:13px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;font-weight:700;">H</text><text x="397.8" y="100.0" text-anchor="middle" fill="currentColor" style="font-size:11px;">travel</text><text x="517.0" y="74.0" text-anchor="start" fill="var(--accent)" style="font-size:11.5px;font-weight:600;">E = x̂ f(t + z/v)</text><text x="517.0" y="92.0" text-anchor="start" fill="var(--accent2)" style="font-size:11.5px;font-weight:600;">H = −ŷ f(t + z/v)/η</text><text x="517.0" y="110.0" text-anchor="start" fill="currentColor" style="font-size:11.5px;">E × H along −ẑ</text><line x1="128.0" y1="264.0" x2="128.0" y2="218.0" stroke="var(--muted)" stroke-width="1" stroke-dasharray="3 3" stroke-linecap="round"/><text x="128.0" y="213.7" text-anchor="middle" fill="var(--muted)" style="font-size:11px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">x</text><line x1="128.0" y1="264.0" x2="99.5" y2="286.1" stroke="var(--muted)" stroke-width="1" stroke-dasharray="3 3" stroke-linecap="round"/><text x="94.3" y="294.1" text-anchor="middle" fill="var(--muted)" style="font-size:11px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">y</text><line x1="128.0" y1="264.0" x2="174.0" y2="264.0" stroke="var(--muted)" stroke-width="1" stroke-dasharray="3 3" stroke-linecap="round"/><text x="186.3" y="268.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">z</text><line x1="128.0" y1="264.0" x2="192.0" y2="264.0" stroke="currentColor" stroke-width="3.2" marker-end="url(#ah)" stroke-linecap="round"/><line x1="128.0" y1="264.0" x2="93.3" y2="290.9" stroke="var(--accent)" stroke-width="2.6" marker-end="url(#ah)" stroke-linecap="round"/><line x1="128.0" y1="264.0" x2="128.0" y2="314.0" stroke="var(--accent2)" stroke-width="2.6" marker-end="url(#ah)" stroke-linecap="round"/><text x="79.8" y="302.2" text-anchor="middle" fill="var(--accent)" style="font-size:13px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;font-weight:700;">E</text><text x="136.0" y="330.0" text-anchor="middle" fill="var(--accent2)" style="font-size:13px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;font-weight:700;">H</text><text x="163.2" y="256.0" text-anchor="middle" fill="currentColor" style="font-size:11px;">travel</text><text x="212.0" y="230.0" text-anchor="start" fill="var(--accent)" style="font-size:11.5px;font-weight:600;">E = ŷ f(t − z/v)</text><text x="212.0" y="248.0" text-anchor="start" fill="var(--accent2)" style="font-size:11.5px;font-weight:600;">H = −x̂ f(t − z/v)/η</text><text x="212.0" y="266.0" text-anchor="start" fill="currentColor" style="font-size:11.5px;">E × H along +ẑ</text><line x1="433.0" y1="264.0" x2="433.0" y2="218.0" stroke="var(--muted)" stroke-width="1" stroke-dasharray="3 3" stroke-linecap="round"/><text x="433.0" y="213.7" text-anchor="middle" fill="var(--muted)" style="font-size:11px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">x</text><line x1="433.0" y1="264.0" x2="404.5" y2="286.1" stroke="var(--muted)" stroke-width="1" stroke-dasharray="3 3" stroke-linecap="round"/><text x="399.3" y="294.1" text-anchor="middle" fill="var(--muted)" style="font-size:11px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">y</text><line x1="433.0" y1="264.0" x2="479.0" y2="264.0" stroke="var(--muted)" stroke-width="1" stroke-dasharray="3 3" stroke-linecap="round"/><text x="491.3" y="268.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">z</text><line x1="433.0" y1="264.0" x2="369.0" y2="264.0" stroke="currentColor" stroke-width="3.2" marker-end="url(#ah)" stroke-linecap="round"/><line x1="433.0" y1="264.0" x2="398.3" y2="290.9" stroke="var(--accent)" stroke-width="2.6" marker-end="url(#ah)" stroke-linecap="round"/><line x1="433.0" y1="264.0" x2="433.0" y2="214.0" stroke="var(--accent2)" stroke-width="2.6" marker-end="url(#ah)" stroke-linecap="round"/><text x="384.8" y="302.2" text-anchor="middle" fill="var(--accent)" style="font-size:13px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;font-weight:700;">E</text><text x="441.0" y="206.0" text-anchor="middle" fill="var(--accent2)" style="font-size:13px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;font-weight:700;">H</text><text x="397.8" y="256.0" text-anchor="middle" fill="currentColor" style="font-size:11px;">travel</text><text x="517.0" y="230.0" text-anchor="start" fill="var(--accent)" style="font-size:11.5px;font-weight:600;">E = ŷ f(t + z/v)</text><text x="517.0" y="248.0" text-anchor="start" fill="var(--accent2)" style="font-size:11.5px;font-weight:600;">H = +x̂ f(t + z/v)/η</text><text x="517.0" y="266.0" text-anchor="start" fill="currentColor" style="font-size:11.5px;">E × H along −ẑ</text></svg><figcaption><strong>Divide by η and rotate by 90°, choosing the rotation that makes E × H point the way the wave travels.</strong> The axes are drawn as on the slides: x up, z right, y out of the page (drawn toward the lower left). Top row: an x-polarized wave has <b>H</b> along +ŷ when it travels toward +z, and along −ŷ when it travels toward −z. That is the sign flip in H<sub>y</sub> = (Af − Bg)/η. Bottom row: a y-polarized wave needs <b>H</b> along −x̂ for +z travel, because ŷ × (−x̂) = +ẑ, and along +x̂ for −z travel. In every case <b>E</b> ⊥ <b>H</b>, both are perpendicular to the direction of travel, and |<b>E</b>|/|<b>H</b>| = η. In vector form, <b>H</b> = û × <b>E</b>/η and <b>E</b> = η<b>H</b> × û, with û the direction of travel.</figcaption></figure>

**Sign table** (every row checked with an explicit cross product).

| wave | $\mathbf{E}$ | $\mathbf{H}$ | $\mathbf{E}\times\mathbf{H}$ | travels toward |
|---|---|---|---|---|
| $x$-polarized | $\hat x\,f(t-z/v)$ | $+\hat y\,f(t-z/v)/\eta$ | $\hat x\times\hat y = +\hat z$ | $+z$ |
| $x$-polarized | $\hat x\,f(t+z/v)$ | $-\hat y\,f(t+z/v)/\eta$ | $\hat x\times(-\hat y) = -\hat z$ | $-z$ |
| $y$-polarized | $\hat y\,f(t-z/v)$ | $-\hat x\,f(t-z/v)/\eta$ | $\hat y\times(-\hat x) = +\hat z$ | $+z$ |
| $y$-polarized | $\hat y\,f(t+z/v)$ | $+\hat x\,f(t+z/v)/\eta$ | $\hat y\times\hat x = -\hat z$ | $-z$ |
| $z$-polarized | $\hat z\,f(t\mp z/v)$ | — | — | impossible: $\nabla\cdot\mathbf{E}\neq0$ ([[concepts/wave-equation|Wave equation]]) |

The notes write the $y$-polarized pair as $\mathbf{E} = \hat yf(t\mp z/v)$, $\mathbf{H} = \mp\hat x f(t\mp z/v)/\eta$ (upper signs together, lower together): the sign before $\hat x$ is opposite to the one before $\hat y$ in the $x$-polarized pair.

**On a cable.** [[2-magnetostatics/15-inductance-magnetic-energy-and-the-potentials|Lecture 15]] found $\mathcal{L}\mathcal{C} = \mu\epsilon$ for any two-conductor line in one medium, so $1/\sqrt{\mathcal{L}\mathcal{C}} = v$: a cable signal travels at the plane-wave speed of its filling. $\sqrt{\mathcal{L}/\mathcal{C}}$, Unit 4's [[concepts/characteristic-impedance|characteristic impedance]], is $\eta$ times geometry: $(\eta/2\pi)\ln(b/a)$ for a coax, $\eta\,d/W$ for parallel plates (width $W$, spacing $d$). A current $I = J_sW$ fed into the middle of an infinite parallel-plate line sees two lines in parallel, $\eta d/(2W)$: $V = I\eta d/(2W)$, $E = V/d = \eta J_s/2$ — the radiating sheet's result ([[concepts/current-sheet-radiation|Radiation from a current sheet]]): a current source driving two lines of $\eta$ per square.

**In a conducting medium ([[3-maxwell-and-waves/22-phasor-maxwell-equations-and-damped-waves|Lecture 22]]): the complex intrinsic impedance.** $j\omega\epsilon\to\sigma + j\omega\epsilon$:

$$
\begin{gathered}
\eta = \sqrt{\frac{j\omega\mu}{\sigma + j\omega\epsilon}} = \lvert\eta\rvert e^{j\tau},\\[6pt]
\gamma\eta = j\omega\mu,\qquad \frac{\gamma}{\eta} = \sigma + j\omega\epsilon,\\[6pt]
\lvert\eta\rvert = \frac{\sqrt{\mu/\epsilon}}{\big[1 + (\sigma/\omega\epsilon)^2\big]^{1/4}},\\[6pt]
\tau = \frac12\tan^{-1}\frac{\sigma}{\omega\epsilon}\quad(0\le\tau<45^\circ).
\end{gathered}
$$
Still $\tilde{\mathbf{H}} = \hat u\times\tilde{\mathbf{E}}/\eta$: $\mathbf{H}$ lags $\mathbf{E}$ by $\tau$, amplitude ratio $\lvert\eta\rvert$ ($\gamma$: [[concepts/propagation-constant|propagation constant]]).

**Where the angles come from** (Lecture 22 §5). $j\omega\mu$ is at 90°, $\sigma + j\omega\epsilon$ at $90^\circ - \tan^{-1}(\sigma/\omega\epsilon)$. $\eta$ (root of the ratio) takes half the difference, $\tau$; $\gamma$ (root of the product) half the sum, $90^\circ - \tau$. Hence $\alpha/\beta = \cot\angle\gamma = \tan\tau$, and $\lvert\gamma\rvert\lvert\eta\rvert = \omega\mu$: conduction raises $\lvert\gamma\rvert$ and lowers $\lvert\eta\rvert$; beyond the scales $\omega\sqrt{\mu\epsilon}$ and $\sqrt{\mu/\epsilon}$ only $\sigma/\omega\epsilon$ matters. **τ sets the timing:** $\mathbf{H}$ peaks $\tau/\omega$ after $\mathbf{E}$, $\tau/\beta$ behind it in a snapshot. Dividing by $\eta$ divides by $\lvert\eta\rvert$ *and* subtracts $\tau$: $\mathbf{H} = \pm\hat y\,(\lvert E_0\rvert/\lvert\eta\rvert)\,e^{\mp\alpha z}\cos(\omega t\mp\beta z + \angle E_0 - \tau)$. Limits ([[concepts/loss-tangent|σ/ωε]]): imperfect dielectric $\tau\approx\sigma/2\omega\epsilon$ rad, $\lvert\eta\rvert\approx\sqrt{\mu/\epsilon}$; good conductor $\eta\approx\sqrt{\omega\mu/\sigma}\,e^{j\pi/4}$ ([[3-maxwell-and-waves/23-imperfect-dielectrics-and-good-conductors|Lecture 23]]).

**From a measured wave (exam step).** $\eta = j\omega\mu/\gamma$ with the medium's $\mu$: $\lvert\eta\rvert = \omega\mu/\lvert\gamma\rvert$, $\tau = 90^\circ - \angle\gamma = \tan^{-1}(\alpha/\beta)$ (worked in the Examples).

**The current sheet in a conducting medium** ([[3-maxwell-and-waves/22-phasor-maxwell-equations-and-damped-waves#7-lecture-19s-current-sheet-in-a-conducting-medium|Lecture 22 §7]]). $\mathbf{J}_s = \hat x\,J_0\cos\omega t$ on $z = 0$; the [[concepts/current-sheet-radiation|Lecture 19]] argument with $j\beta\to\gamma$: outgoing $\tilde{\mathbf{E}} = \hat x\,Ae^{-\gamma\lvert z\rvert}$ on each face (tangential $\mathbf{E}$ continuous), $\tilde{\mathbf{H}} = \pm\hat y\,(A/\eta)\,e^{-\gamma\lvert z\rvert}$ for $z\gtrless0$; the jump $\hat z\times(\tilde{\mathbf{H}}^+ - \tilde{\mathbf{H}}^-) = \hat z\times\hat y\,(2A/\eta) = -\hat x\,(2A/\eta) = \hat x\,J_0$ gives $A = -\eta J_0/2$:

$$
\begin{gathered}
\tilde{\mathbf{E}} = -\hat x\,\frac{\eta J_0}{2}\,e^{-\gamma\lvert z\rvert},\\[6pt]
\tilde{\mathbf{H}} = \mp\hat y\,\frac{J_0}{2}\,e^{-\gamma\lvert z\rvert}\qquad(z\gtrless0).
\end{gathered}
$$

The lossless result with $e^{-j\beta\lvert z\rvert}\to e^{-\gamma\lvert z\rvert}$ and complex $\eta$.

**Examples.**

> [!example] A 1 V/m plane wave in vacuum
> $E = 1$ V/m in free space: $H = E/\eta_0 = 2.65$ mA/m, $B = \mu_0H = E/c = 3.34$ nT — tiny next to the Earth's roughly 50 μT, yet not negligible: different units make "small" meaningless; the ratio $E/B = c$ ($E/H = \eta_0$) is fixed. If $\mathbf{E} = \hat y$ V/m travels toward $-z$: $\mathbf{H} = \hat u\times\mathbf{E}/\eta_0 = (-\hat z)\times\hat y/\eta_0 = +\hat x\,2.65$ mA/m. Check: $\hat y\times\hat x = -\hat z$ ✓.

> [!example] Notes, Example 1 (Lecture 19) — a triangular pulse travelling along $y$, and its B two ways
> In free space $\mathbf{E} = \hat x\,\triangle\big((t - y/c)/\tau\big)$, $\triangle(u)$ the unit triangle of ECE 210 (peak 1 at $u = 0$, zero for $\lvert u\rvert\ge\tfrac12$). Find $\mathbf{B}$.
>
> **Route 1, rotation.** Travel toward $+y$: $\mathbf{H} = \hat y\times\mathbf{E}/\eta_0 = -\hat z\,\triangle/\eta_0$ ($\hat x\times(-\hat z) = +\hat y$ ✓); $\mu_0/\eta_0 = \sqrt{\mu_0\epsilon_0} = 1/c$:
> $$
> \mathbf{B} = \mu_0\mathbf{H} = -\hat z\,\frac1c\,\triangle\Big(\frac{t - y/c}{\tau}\Big).
> $$
> **Route 2, Faraday.** $\partial\mathbf{B}/\partial t = -\nabla\times(\hat xE_x) = +\hat z\,\partial E_x/\partial y = -\hat z\,\triangle'/(c\tau)$ ($\triangle'$: derivative with respect to the argument). Integrating in time, static constant dropped, gives the same $\mathbf{B}$. At $y = 40$ m, $t = 0.05$ µs, $\tau = 1$ µs both sides equal $-6.67\times10^{-3}$ T/s.

> [!example] Notes, Example 2 — is the magnetic force of a wave negligible?
> A charge $q$ with velocity $\mathbf{v}$ in the Example 1 wave ([[concepts/lorentz-force|Lorentz force]]):
> $$
> \mathbf{F} = q\,\triangle\Big(\frac{t - y/c}{\tau}\Big)\Big(\hat x - \frac{\mathbf{v}\times\hat z}{c}\Big).
> $$
> The magnetic term is smaller by $v_\perp/c$ ($v_\perp$ perpendicular to $\mathbf{B}$; the site's phrasing of the notes' point): $3.3\times10^{-3}$ at $10^6$ m/s (a fast vacuum-tube electron), 0.67 at $2\times10^8$ m/s — negligible unless relativistic. $\mathbf{E}$ does the work in antennas and absorbed light, though $E$ and $H$ carry equal energy (Lecture 20).

- $\epsilon_r = 4$, $\mu_r = 1$: $v = c/2 = 1.50\times10^8$ m/s, $\eta = \eta_0/2 = 188\ \Omega$ ($\approx60\pi$).
- Slide 24's wave $h$, at $10^8$ m/s, in a non-magnetic medium: $\epsilon_r = (c/v)^2 = 8.99\approx9$, $\eta = \mu_0v = 40\pi\approx126\ \Omega$.
- Polyethylene, $\epsilon_r = 2.25$: $v = c/1.5 = 2.00\times10^8$ m/s, $\eta = 251\ \Omega$ ($80\pi$); or $\eta = \mu_0v$: $2\times10^8$ m/s gives $251.3\ \Omega$. Its coax, $b/a = 3.5$: $251\ \Omega\times\ln(3.5)/2\pi = 251\times0.199$, the 50 Ω of [[problems/coax-inductance-and-the-lc-product|Worked problem — Inductance of a coax, and the 𝓛𝓒 product]] — a coax guides a TEM wave.
- $\mu_r = 2$, $\epsilon_r = 8$: $\eta_0/2 = 188\ \Omega$ as for $\epsilon_r = 4$, but speed $c/4$ ($\eta$ follows the ratio, $v$ the product).

> [!example] The [[concepts/propagation-constant|decode example]] — $\eta$ from a measured $\gamma$
> $\gamma = 1 + j3$ m⁻¹, $\omega = 3\times10^8$ rad/s, $\mu_0$, so $\omega\mu_0 = 120\pi$ Ω/m and
>
> $$
> \begin{gathered}
> \eta = \frac{j120\pi}{1 + j3} = \frac{120\pi\,j(1 - j3)}{10} = 12\pi(3 + j)\\[6pt]
> = 113.1 + j37.7 = 119.2\,e^{j18.4^\circ}\ \Omega ;
> \end{gathered}
> $$
>
> check $\tan^{-1}(1/3) = 18.4^\circ$; lossless ($8\epsilon_0$) would give $133.3\ \Omega$. Then $\tilde{\mathbf{H}} = \hat x\times\hat y\,(6/\eta)\,e^{-\gamma x} = \hat z\,(6/119.2)\,e^{-j18.4^\circ}e^{-\gamma x}$ A/m for $\tilde{\mathbf{E}} = \hat y\,6e^{-\gamma x}$ V/m.

- $\mu = 3\mu_0$, $\epsilon = 9\epsilon_0$, $\sigma/\omega\epsilon = 4/3$: $24\pi(2 + j) = 168.6\,e^{j26.6^\circ}\ \Omega$; lossless $217.7\ \Omega$.
- $\sigma = \omega\epsilon$: $\lvert\eta\rvert = 2^{-1/4}\sqrt{\mu/\epsilon} = 0.84\sqrt{\mu/\epsilon}$, $\tau = 22.5^\circ$.

> [!example] The sheet in the decode example's medium
> $\gamma = 1 + j3$ m⁻¹, $\eta = 119.2\,e^{j18.4^\circ}\ \Omega$, $\omega = 3\times10^8$ rad/s, $J_0 = 2$ A/m:
> $$
> \begin{gathered}
> \mathbf{H} = \mp\hat y\,e^{-\lvert z\rvert}\cos(\omega t - 3\lvert z\rvert)\ \ \text{A/m},\\[4pt]
> \mathbf{E} = -\hat x\,119.2\,e^{-\lvert z\rvert}\cos(\omega t - 3\lvert z\rvert + 18.4^\circ)\ \ \text{V/m}
> \end{gathered}
> $$
> ($z$ in m). Both waves fade by $e$ per metre. $\mathbf{H}$ is still set by the current alone ($\tfrac12J_0 = 1$ A/m at the sheet); the medium sets $\mathbf{E}$, which leads $\mathbf{H}$ by $\tau = 18.4^\circ$, no longer exactly opposite $\mathbf{J}_s$. Power given up: $\langle-\mathbf{J}_s\cdot\mathbf{E}\rangle = \tfrac12\text{Re}\{-\tilde{\mathbf{J}}_s\cdot\tilde{\mathbf{E}}^*\} = \tfrac14J_0^2\,\text{Re}\{\eta\} = 36\pi\approx113$ W/m² ($\text{Re}\{\eta\} = \lvert\eta\rvert\cos\tau$); half, 56.5 W/m², enters each side, heat within a few metres. $z>0$: $(-\hat x)\times(-\hat y) = +\hat z$ ✓.

> [!trap]
> - $H = E/\eta$, not $E\eta$; the notes' $\sqrt{\epsilon/\mu}$ is $1/\eta$.
> - The medium's $\eta$: 6 V/m in polyethylene → $6/251.3 = 23.9$ mA/m, not $6/377 = 15.9$.
> - $\pm\eta$ is for one wave: $E_x = Af + Bg$, $H_y = (Af - Bg)/\eta$ give $\eta\,(Af+Bg)/(Af-Bg)$.
> - $-z$ travel reverses $\mathbf{H}$: write $\hat u\times\mathbf{E}$ out; relabel axes cyclically only.
> - $120\pi = 376.99\ \Omega$ vs $376.73\ \Omega$ (0.07 %): either; say which. The notes write $\eta_0 = 120\pi$ as an equality.
> - $\sqrt{\mu/\epsilon}$ needs $\sigma = 0$; else $j\omega\mu/\gamma$.
> - $\tilde{\mathbf{E}}/\eta$ subtracts $\tau$, $\eta\tilde{\mathbf{H}}$ adds it: $\mathbf{H}$ lags.
> - $\lvert\eta\rvert$ is an *amplitude* ratio; $E_x(t)/H_y(t)$ varies.
> - Collisionless plasma below $f_p$: $\eta$ imaginary (90°), no average power (Lecture 22 §8).
> - $\mu$ enters $\eta = j\omega\mu/\gamma$, $\sigma = 2\alpha\beta/\omega\mu$ and $\epsilon = (\beta^2 - \alpha^2)/\omega^2\mu$: $\mu_0$ for a magnetic medium spoils all three, not $\sigma/\omega\epsilon$ ([[problems/decoding-a-damped-wave|Worked problem — Decoding a damped wave]], $\mu = 3\mu_0$).

> [!exam] On exams
> **$\mathbf{H}$ from $\mathbf{E}$, or back**, including $y$-polarized and $-z$ waves: write the cross product out. **$v$, $\eta$ in a dielectric**, or $\epsilon_r$ from a speed; slower than $c$ means matter, not loss. **Constants**: $\eta_0\approx120\pi\ \Omega$, $c\approx3\times10^8$ m/s. Lossy media: $\lvert\eta\rvert$ and $\tau$ from $\sigma/\omega\epsilon$ or from $\gamma$.

**Where it appears.** [[3-maxwell-and-waves/18-the-wave-equation-and-plane-tem-waves#5-h-from-e-the-intrinsic-impedance|Lecture 18 §5]] (sign table) and [[3-maxwell-and-waves/18-the-wave-equation-and-plane-tem-waves#7-in-matter-and-on-a-cable|§7]] (matter, cable); [[3-maxwell-and-waves/19-dalembert-solutions-and-radiation-from-current-sheets#2-three-warm-up-examples-notes|Lecture 19 §2]] (Examples 1–2) and [[3-maxwell-and-waves/19-dalembert-solutions-and-radiation-from-current-sheets#9-connections|§9]] ($\eta/2$); Lecture 20 ($E^2/\eta$); [[3-maxwell-and-waves/22-phasor-maxwell-equations-and-damped-waves#5-the-general-formulas-and-how-to-decode-a-damped-wave|Lecture 22 §5]] (complex $\eta$ from $\gamma$) and [[3-maxwell-and-waves/22-phasor-maxwell-equations-and-damped-waves#7-lecture-19s-current-sheet-in-a-conducting-medium|§7]] (sheet in a conductor); Lecture 23 ($\cos\tau$ in power); Lecture 25 (reflection); [[problems/a-pulse-on-the-move|Worked problem — A pulse on the move]]; [[problems/decoding-a-damped-wave|Worked problem — Decoding a damped wave]].

**Related.** [[concepts/plane-waves|Plane waves]] · [[concepts/wave-equation|Wave equation]] · [[concepts/current-sheet-radiation|Radiation from a current sheet]] · [[concepts/poynting-vector|Poynting vector]] · [[concepts/permittivity|Permittivity, susceptibility, and D = εE]] · [[concepts/permeability|Permeability, susceptibility, and B = μH]] · [[concepts/characteristic-impedance|Characteristic impedance]] · [[concepts/inductance|Inductance]] · [[concepts/capacitance|Capacitance]].

**Practice.** [[practice/topics#plane-waves-and-the-wave-equation|Plane waves and the wave equation]] (25 problems) — for example [[practice/18-wave-equation-and-plane-waves#181-which-way-and-how-fast|18.1 Which way and how fast]] (easy), [[practice/18-wave-equation-and-plane-waves#186-which-fields-can-be-waves|18.6 Which fields can be waves]] (medium), [[practice/18-wave-equation-and-plane-waves#189-triangle-pulse-in-a-magnetic-medium|18.9 Triangle pulse in a magnetic medium]] (hard).
