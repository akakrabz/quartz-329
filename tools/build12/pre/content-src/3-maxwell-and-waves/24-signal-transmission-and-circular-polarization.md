---
title: "Lecture 24 — Signal transmission and circular polarization"
description: "A narrowband AM signal m(t) cos ωt rides a plane wave undistorted in a non-dispersive medium; in a dispersive one its envelope travels at the group velocity v_g = dω/dβ while the crests travel at v_p = ω/β. An x̂ cosine plus a ŷ sine carrier rotates instead of oscillating: circular polarization, right- or left-handed by the hand whose fingers curl with the rotation when the thumb points along the travel."
tags: [lecture, waves]
lecture: 24
---

*Lecture 24 · course notes §24 (no slides) · prev: [[3-maxwell-and-waves/23-imperfect-dielectrics-and-good-conductors|Lecture 23]] · next: [[3-maxwell-and-waves/25-wave-reflection-and-transmission|Lecture 25]] · worked problem: [[problems/two-sheets-a-quarter-wave-apart|Two crossed sheets a quarter wave apart]] · practice: [[practice/24-group-velocity-and-polarization|12 problems]]*

> [!abstract] In one breath
> A message $m(t)$ on a carrier $\cos\omega t$ rides a plane wave unchanged in a non-dispersive medium. In a dispersive medium the envelope travels at the **group velocity** $v_g = d\omega/d\beta$, the crests at $v_p = \omega/\beta$. The carrier's direction is its **polarization**. An $\hat x$ cosine plus a $\hat y$ sine gives a field vector that rotates once per period: **circular polarization**, phasor $(\hat x\mp j\hat y)e^{-j\beta z}$. The hand whose fingers curl with the rotation, thumb along the travel, names it right- or left-circular. It carries twice the power of either component.

## 1. Narrowband AM in a non-dispersive medium

In a perfect dielectric $v$ and $\eta$ do not depend on frequency, so any waveform travels unchanged as $\mathbf{E} = \hat x f(t - z/v)$, $\mathbf{H} = \hat y f(t - z/v)/\eta$ ([[3-maxwell-and-waves/18-the-wave-equation-and-plane-tem-waves|Lecture 18]]). Take

$$
f(t) = m(t)\cos\omega t ,
$$

with a message $m(t)$ (voice, data) that changes slowly compared with the period $T = 2\pi/\omega$. This is **narrowband AM**, and $\omega$ is the **carrier frequency**. With $\omega(t - z/v) = \omega t - \beta z$ and $\beta = \omega\sqrt{\mu\epsilon}$:

> [!key] Field 1: AM with an x-polarized carrier
> $$
> \begin{gathered}
> \mathbf{E} = m\Big(t-\frac zv\Big)\cos(\omega t-\beta z)\,\hat x,\\[4pt]
> \mathbf{H} = \frac{m(t-z/v)}{\eta}\cos(\omega t-\beta z)\,\hat y .
> \end{gathered}
> $$
> Envelope and crests move together at $v$. The message arrives undistorted, delayed by $z/v$.

Two more carriers from the notes:

- **Field 2:** $m(t - z/v)\cos(\omega t - \beta z)\,\hat y$, a $y$-polarized carrier.
- **Field 3:** $m(t - z/v)\sin(\omega t - \beta z)\,\hat y$, also $y$-polarized, with the carrier a quarter period late: $\sin(\omega t - \beta z) = \cos(\omega(t - T/4) - \beta z)$.

## 2. Dispersive media: group velocity

When $\beta(\omega)$ is not a straight line through the origin, $v_p = \omega/\beta$ depends on frequency and the medium is dispersive. The notes state the result in a footnote and leave the details to ECE 450:

> [!key] Group velocity
> $$
> \begin{gathered}
> \mathbf{E}\approx m\Big(t-\frac{z}{v_g}\Big)\cos(\omega t-\beta z)\,\hat x,\\[4pt]
> v_g\equiv\frac{d\omega}{d\beta},\qquad v_p = \frac\omega\beta .
> \end{gathered}
> $$
> The notes write $\partial\omega/\partial\beta$. The message (the envelope) travels at $v_g$, the carrier crests at $v_p$. On an $\omega$–$\beta$ diagram $v_p$ is the slope of the chord from the origin and $v_g$ the slope of the tangent ([[3-maxwell-and-waves/21-monochromatic-waves-and-phasor-notation#2-dispersion-relations-and-phase-velocity|Lecture 21 §2]]).

> [!derivation]- Why the envelope moves at dω/dβ (this site's; Rao §8.3)
> Write the source as $\text{Re}\{m(t)e^{j\omega_0t}\}$, and $m(t)$ as a sum of slow tones $e^{j\Omega t}$ with $\lvert\Omega\rvert\ll\omega_0$. Each frequency $\omega_0 + \Omega$ travels with its own $\beta(\omega_0 + \Omega)$. Expand about the carrier:
> $$
> \beta(\omega_0+\Omega)\approx\beta_0+\frac{\Omega}{v_g},\qquad \frac1{v_g} = \frac{d\beta}{d\omega}\Big|_{\omega_0}.
> $$
> Each tone then becomes
> $$
> e^{j(\omega_0+\Omega)t - j\beta(\omega_0+\Omega)z}\approx e^{j(\omega_0t-\beta_0z)}\,e^{j\Omega(t - z/v_g)} .
> $$
> The first factor is the same for every tone: the carrier, with phase speed $\omega_0/\beta_0$. The second delays every tone of $m$ by the same $z/v_g$. Summing gives $m(t - z/v_g)\cos(\omega_0t - \beta_0z)$. The next term of the expansion, $\tfrac12\beta''\Omega^2z$, spreads the envelope; it is negligible while $\tfrac12\lvert\beta''\rvert\Omega^2z\ll1$.

> [!key] Group velocity for the notes' dispersion relations (this site's table)
> The relations of [[3-maxwell-and-waves/21-monochromatic-waves-and-phasor-notation|Lecture 21]]: $\beta = \omega\sqrt{\mu\epsilon}$ (dielectric), $\omega\sqrt{m/(\tfrac53k_BT)}$ (sound in a monatomic gas, $m$ the atomic mass), $\tfrac1c\sqrt{\omega^2-\omega_p^2}$ (collisionless plasma).
>
> | medium | $v_p$ | $v_g$ |
> |---|---|---|
> | dielectric | $1/\sqrt{\mu\epsilon}$ | $v_p$ |
> | gas (sound) | $\sqrt{5k_BT/3m}$ | $v_p$ |
> | plasma | $c/\sqrt{1-\omega_p^2/\omega^2}$ | $c^2/v_p$ |
>
> Plasma: differentiating $\omega^2 = \omega_p^2 + c^2\beta^2$ gives $d\omega/d\beta = c^2\beta/\omega$, so $v_pv_g = c^2$ and $v_g = c\sqrt{1-\omega_p^2/\omega^2}<c<v_p$. A pure cosine carries no message; signals and energy travel at $v_g$.

<!-- fig:pol-am-group-delay -->

> [!example] Example — 10 MHz through an ionospheric plasma (this site's numbers)
> $N = 10^{12}$ electrons/m³ gives $f_p\approx8.98$ MHz. At $f = 10$ MHz, $\sqrt{1 - f_p^2/f^2} = 0.440$, so $v_g = 0.440c$ and $v_p = 2.27c$. Across 300 km of such plasma a voice-band message arrives after 2.27 ms, against 1.00 ms in vacuum; a crest would need only 0.44 ms. Higher carriers are delayed less: at 100 MHz, $v_g = 0.996c$.

> [!trap]
> - "Propagation velocity" $\omega/\beta$ is the signal speed only when $\beta\propto\omega$.
> - $v_p>c$ in a plasma breaks no law: crests carry no information.
> - $v_g = d\omega/d\beta$, not $\omega/\beta$ and not $d\beta/d\omega$.

## 3. Circular polarization: a rotating carrier

Transmit Fields 1 and 3 together. They superpose:

> [!key] A circularly polarized carrier
> $$
> \begin{gathered}
> \mathbf{E} = m\Big(t-\frac zv\Big)\big[\cos(\omega t-\beta z)\,\hat x\\
> + \sin(\omega t-\beta z)\,\hat y\big],\\[6pt]
> \mathbf{H} = \frac{m(t - z/v)}{\eta}\big[\cos(\omega t-\beta z)\,\hat y\\
> - \sin(\omega t-\beta z)\,\hat x\big].
> \end{gathered}
> $$
> $\mathbf{H} = \hat z\times\mathbf{E}/\eta$, term by term. At fixed $z$ the carrier vector keeps its length and **rotates** instead of oscillating, once per period: the rotation frequency is the wave frequency.

Each linear piece has its own phasor (a sine picks up $-j$, [[3-maxwell-and-waves/21-monochromatic-waves-and-phasor-notation|Lecture 21]]), so the two rotation senses are

$$
\begin{gathered}
\cos(\omega t-\beta z)\,\hat x+\sin(\omega t-\beta z)\,\hat y\\
\leftrightarrow\ (\hat x-j\hat y)e^{-j\beta z}\ \ \text{(right-circular)},\\[8pt]
\cos(\omega t-\beta z)\,\hat x-\sin(\omega t-\beta z)\,\hat y\\
\leftrightarrow\ (\hat x+j\hat y)e^{-j\beta z}\ \ \text{(left-circular)}.
\end{gathered}
$$

Some links work better with circular carriers because of the propagation medium, for example Earth's ionosphere or the interplanetary medium. (Along Earth's magnetic field the ionosphere turns the plane of a linear wave, Faraday rotation, Rao §10.2.)

## 4. Right or left: the notes' rule

> [!key] Handedness (helicity)
> Point the thumb along the direction of travel. If the **right** hand's fingers curl the way the field vector rotates, the wave is **right-circular**; if the left hand's, **left-circular**. Equivalently, looking along the direction of travel, right-circular turns **clockwise** and left-circular **counterclockwise**. For travel along $+z$, at $z = 0$:
> - $\cos\omega t\,\hat x + \sin\omega t\,\hat y\leftrightarrow\hat x - j\hat y$ turns $x\to y$: right-circular. The $x$ component **leads** $y$ by 90° (the $-j$).
> - $\cos\omega t\,\hat x - \sin\omega t\,\hat y\leftrightarrow\hat x + j\hat y$ turns $x\to -y$: left-circular. The $x$ component **lags**.

<!-- fig:pol-handedness -->

The phasor shows the rotation fastest: the leading component peaks first, so the vector turns from the leading axis toward the lagging one. Then match a hand to that rotation and the travel direction.

> [!recipe] Handedness of any phasor (this site's packaging of the notes' rule)
> 1. Travel direction $\hat u$ from the exponent: $e^{-j\beta z}$ is $+\hat z$, $e^{+j\beta x}$ is $-\hat x$ ([[3-maxwell-and-waves/21-monochromatic-waves-and-phasor-notation#4-plane-wave-phasors-and-the-direction-of-travel-trap|Lecture 21 §4]]).
> 2. Where the exponent equals 1: $\mathbf{E}(0) = \text{Re}\{\tilde{\mathbf{E}}\}$, and a quarter period later $\mathbf{E}(T/4) = \text{Re}\{j\tilde{\mathbf{E}}\} = -\text{Im}\{\tilde{\mathbf{E}}\}$.
> 3. $\hat u\cdot[\mathbf{E}(0)\times\mathbf{E}(T/4)]>0$: right-handed; $<0$: left-handed; $=0$: linear.

> [!example] Example 1 (notes) — Ẽ = (ẑ + jŷ) exp(jβx)
> *Travel:* the exponent has no minus sign, so $-\hat x$. *Rotation at $x = 0$:* $\mathbf{E} = \text{Re}\{(\hat z + j\hat y)e^{j\omega t}\} = \hat z\cos\omega t - \hat y\sin\omega t$. The $y$ component leads $z$ by 90°, so the vector points along $\hat y$ a quarter period before it points along $\hat z$: it turns from $y$ toward $z$. *Hand:* the right thumb along $-\hat x$ curls from $z$ toward $y$, the wrong way. The wave is **left-circular**. Recipe check: $\hat z\times(-\hat y) = \hat x$, and $(-\hat x)\cdot\hat x<0$.

> [!trap]
> - $\hat x - j\hat y$ is right-circular for travel along $+z$ only; along $-z$ it is left-circular.
> - An overall factor ($-1$, $j$, $\eta$) only scales or delays the rotation; it never changes the hand.
> - Look along the travel, from behind the wave, not toward the source.
> - $\mathbf{H} = \hat u\times\mathbf{E}/\eta$ is $\mathbf{E}$ turned 90° about $\hat u$: same shape, same hand.

## 5. Linear, circular, elliptical

The notes' cases are special values of one phase. For $\tilde{\mathbf{E}} = (A\hat x + Be^{j\phi}\hat y)e^{-j\beta z}$ with $A, B\ge0$ (this site's summary; Rao §1.4, §4.5):

> [!key] Polarization of two perpendicular components
> - **Linear:** $\phi = 0$ or $\pi$, or $A = 0$, or $B = 0$.
> - **Circular:** $A = B$ and $\phi = \mp\pi/2$: right-circular for $-\pi/2$, left-circular for $+\pi/2$.
> - **Elliptical:** every other case; right-handed if $\sin\phi<0$ ($y$ lags $x$), left-handed if $\sin\phi>0$.
>
> For travel along $-z$, swap right and left. Other axes: take the components in cyclic order ($\hat y, \hat z$ for travel along $\pm x$; $\hat z, \hat x$ for $\pm y$) and read $+x$ or $+y$ in place of $+z$. Out of order, the hand flips; the §4 recipe avoids this.

<!-- fig:pol-phase-family -->

## 6. Orthogonal bases

For a given travel direction, any polarization is a weighted sum of any orthogonal pair of polarizations; such a pair is a complete set of **basis functions**. For travel along $+z$, with every term multiplied by $e^{-j\beta z}$:

> [!key] Circulars from linears, linears from circulars
> $$
> \begin{gathered}
> \hat x - j\hat y = (1)\,\hat x + (-j)\,\hat y,\\[4pt]
> \hat x + j\hat y = (1)\,\hat x + (j)\,\hat y,\\[4pt]
> \hat x = \tfrac12(\hat x - j\hat y) + \tfrac12(\hat x + j\hat y),\\[4pt]
> \hat y = -\tfrac1{2j}(\hat x - j\hat y) + \tfrac1{2j}(\hat x + j\hat y).
> \end{gathered}
> $$

The notes argue that the circular pair is the more fundamental basis: which axis is called $x$ is arbitrary, but the helicity of a circular wave travelling in a given direction is not. In particle terms, each photon of a right-circular (left-circular) wave carries spin angular momentum $+\hbar$ ($-\hbar$) with certainty. A linear wave's photons are in an equal superposition of the two states: each measurement gives $+\hbar$ or $-\hbar$ with probability 50 %.

**Why polarization matters (notes).** Oscillating charges radiate linear polarization; charges rotating in a plane radiate circular polarization along the normal to that plane. So polarization is set by the geometry and dynamics of the source, and it may change with the medium. It decides the direction of the Lorentz force on a test charge or a load, and the angular momentum the wave carries.

## 7. A rotating current sheet

> [!example] Example 2 (notes) — a rotating sheet current
> $\mathbf{J}_s(t) = m(t)[\cos\omega t\,\hat x + \sin\omega t\,\hat y]$ A/m flows on $z = 0$. A sheet radiates $\mathbf{E}^\pm = -\tfrac\eta2\mathbf{J}_s(t\mp z/v)$ into $z>0$ and $z<0$ ([[3-maxwell-and-waves/19-dalembert-solutions-and-radiation-from-current-sheets|Lecture 19]]), so
> $$
> \begin{gathered}
> \mathbf{E}^\pm = -\frac\eta2\,m\Big(t\mp\frac zv\Big)\big[\cos(\omega t\mp\beta z)\,\hat x\\
> +\sin(\omega t\mp\beta z)\,\hat y\big]\ \ \text{V/m}.
> \end{gathered}
> $$
> On $z = 0$ the carrier is $-(\cos\omega t\,\hat x + \sin\omega t\,\hat y)$. It turns from $x$ toward $y$; the minus sign only adds 180°. $\mathbf{E}^+$ travels along $+z$, so the right hand fits: **right-circular**. $\mathbf{E}^-$ travels along $-z$: **left-circular**. One current component alone would radiate a linear wave; two perpendicular ones 90° out of phase radiate a circular one.

## 8. Power of a circular wave

> [!example] Example 3 (notes) — the power of a circular carrier in vacuum
> $\mathbf{E}_c = \cos(\omega t - \beta z)\,\hat x + \sin(\omega t - \beta z)\,\hat y$ V/m in $z>0$ (Example 2's carrier at unit amplitude):
> $$
> \begin{gathered}
> \tilde{\mathbf{E}}_c = (\hat x - j\hat y)e^{-j\beta z}\ \text{V/m},\\[4pt]
> \tilde{\mathbf{H}}_c = \frac{\hat z\times\tilde{\mathbf{E}}_c}{\eta_0} = \frac{\hat y + j\hat x}{\eta_0}e^{-j\beta z}\ \text{A/m},\\[4pt]
> \langle\mathbf{S}\rangle = \frac12\text{Re}\{\tilde{\mathbf{E}}_c\times\tilde{\mathbf{H}}_c^*\}\\[4pt]
> = \frac1{2\eta_0}\text{Re}\{(\hat x - j\hat y)\times(\hat y - j\hat x)\}\\[4pt]
> = \frac1{2\eta_0}(\hat z + \hat z) = \frac{\hat z}{\eta_0}\approx2.65\ \text{mW/m}^2 .
> \end{gathered}
> $$
> The second $\hat z$ is $(-j\hat y)\times(-j\hat x) = j^2(\hat y\times\hat x) = \hat z$. The result is twice the $1/(2\eta_0)$ of a linear wave of the same amplitude.

For any plane wave travelling along $\hat u = \pm\hat z$ in a lossless medium, $\tilde{\mathbf{H}} = \hat u\times\tilde{\mathbf{E}}/\eta$ gives

$$
\langle\mathbf{S}\rangle = \frac{\lvert\tilde E_x\rvert^2 + \lvert\tilde E_y\rvert^2}{2\eta}\,\hat u ,
$$

whatever the phase between the components: the powers of perpendicular components add ([[3-maxwell-and-waves/21-monochromatic-waves-and-phasor-notation#7-time-averages-straight-from-phasors|Lecture 21 §7]], [[3-maxwell-and-waves/20-poynting-theorem-and-monochromatic-waves#7-time-averages|Lecture 20 §7]]). A circular wave's $\lvert\mathbf{E}\rvert$ never changes, so its instantaneous $\mathbf{S}$ is constant and equals $\langle\mathbf{S}\rangle$; a linear wave's $\mathbf{S}$ pulses at $2\omega$.

## 9. Summary

- Non-dispersive medium: $m(t - z/v)\cos(\omega t - \beta z)$, undistorted.
- Dispersive medium: envelope at $v_g = d\omega/d\beta$, crests at $v_p = \omega/\beta$. Plasma: $v_pv_g = c^2$.
- An $\hat x$ cosine plus a $\hat y$ sine carrier rotates once per period. For travel along $+z$, $(\hat x - j\hat y)e^{-j\beta z}$ is right-circular and $(\hat x + j\hat y)e^{-j\beta z}$ left-circular.
- Hand rule: thumb along the travel; the hand whose fingers follow the rotation names it. The leading component points first.
- $A\hat x + Be^{j\phi}\hat y$: linear for $\phi = 0, \pi$; circular for $A = B$, $\phi = \mp\pi/2$; elliptical otherwise.
- Linear and circular pairs are bases for each other.
- A rotating sheet current: right-circular on one side, left-circular on the other.
- $\langle\mathbf{S}\rangle = (\lvert\tilde E_x\rvert^2 + \lvert\tilde E_y\rvert^2)/2\eta$: a circular wave carries twice a component's power.

Concept pages: [[concepts/group-velocity]] · [[concepts/wave-polarization]] · [[concepts/dispersion-relation]] · [[concepts/phasors]] · [[concepts/poynting-vector]] · [[concepts/current-sheet-radiation]].

> [!exam] On exams
> Every Lecture 24 item on the Exam 3 papers on hand is about polarization; none asks about group velocity.
> - **Name the polarization** (SP17 #4c, SP18 #1(iii)–(iv), SP19 #3a, FA23 #2): write the field as $A\hat x + Be^{j\phi}\hat y$ (cyclic axes otherwise), apply §5 with the travel direction.
> - **Build the phasor** from a hand, a direction and snapshots of $\mathbf{E}$ (Summer 2017–2019 HE3): run the §4 recipe backwards.
> - **Two sheets, one phase** (Summer 2020 FE #4): superpose the sheet fields, then choose $\phi$; see the [[problems/two-sheets-a-quarter-wave-apart|worked problem]].
> - **Power**: one component first, then the whole wave ("twice the linear value").
> - **Bases** (FA23 #1(a)): §6.

> [!tip] Practice this lecture
> [[practice/24-group-velocity-and-polarization|12 practice problems]] — 5 easy, 3 medium, 4 hard — each with a folded hint and a worked solution. Start with [[practice/24-group-velocity-and-polarization#241-crests-and-envelope-in-a-plasma|24.1 Crests and envelope in a plasma]]; the [[practice/index|practice hub]] has the whole bank by difficulty and by topic.

### Sources for this page
Kudeki notes, Lecture 24 (9 pages): Fields 1–3 and the group-velocity footnote; the circular carrier, its $\mathbf{H}$ and phasors; the hand rule and margin figures; Example 1; bases; the helicity footnote; why polarization matters; Examples 2–3. Rao (2009) §1.4 and §4.5 (polarization, same handedness convention), §8.3 (group velocity), §10.1–10.2 (plasma, Faraday rotation). This site's own: the derivation and $v_g$ table, the ionosphere numbers, the recipe, §5, the $\langle\mathbf{S}\rangle$ formula, and all figures; numbers checked by script. Slips in the notes: Example 3 prints V/m for $\tilde{\mathbf{H}}_c$ (A/m); footnote 1's "β non-linear in ω" means "not proportional to ω".
