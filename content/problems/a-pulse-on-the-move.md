---
title: "Worked problem — A pulse on the move"
description: "A ramp-shaped pulse is given as a snapshot at t = 3 µs, moving along +y at 200 m/µs through a non-magnetic medium. Find where it was at t = 0, E(y,t) everywhere, what a probe at 1 km records, the medium's permittivity, and the magnetic field with its direction. Modelled on SP18 Exam 2 #4, re-parameterized with a new waveform, a new axis, and a dielectric instead of vacuum."
tags: [problem, waves]
---

*Problem · style of SP18 Exam 2 #4 (14 pts) · uses [[3-maxwell-and-waves/18-the-wave-equation-and-plane-tem-waves|Lecture 18]] · concepts: [[concepts/plane-waves]], [[concepts/wave-equation]], [[concepts/intrinsic-impedance]]*

> [!question] Problem
> A uniform, non-magnetic medium fills all space. A wave's electric field travels through it with velocity $\mathbf{v} = +200\,\hat y$ m/µs without changing shape. At $t = 3$ µs its profile is
> $$
> \mathbf{E}(y,\,3\ \mu\text{s}) = 0.02\,(y-400)\,\big[u(y-400)-u(y-700)\big]\,\hat z\ \ \text{V/m}\qquad(y\ \text{in metres}),
> $$
> where $u$ is the unit step. This is a ramp that rises from 0 at $y = 400$ m to 6 V/m at $y = 700$ m and drops abruptly to zero there.
> (a) Find $\mathbf{E}(y,0)$ and sketch it.
> (b) Find $\mathbf{E}(y,t)$ for all $y$ and $t$.
> (c) Sketch what a probe at $y = 1$ km records, $E_z(1000\ \text{m},\,t)$, and give its reading at $t = 5$ µs.
> (d) Find $\epsilon_r$ of the medium. True or false: "the medium must be a conductor, because the wave travels slower than light and its field decreases along the pulse."
> (e) Find $\mathbf{H}(y,t)$, including its direction, and the peak values of $H$ and $B$.

## Before writing anything: which way, how fast, which units

Keep $y$ in metres and $t$ in microseconds throughout. Then $v = 200$, and in SI units $v = 2.0\times10^8$ m/s. A pattern that moves rigidly with velocity $v\hat y$ obeys

$$
\mathbf{E}(y,t) = \mathbf{E}\big(y - v(t - t_1),\ t_1\big),\qquad t_1 = 3\ \mu\text{s}:
$$

the field at $y$ now is whatever sat a distance $v(t - t_1)$ further back at time $t_1$. Equivalently, $\mathbf{E}$ depends on $y$ and $t$ only through $t - y/v$, with the minus sign that goes with travel toward $+y$ ([[3-maxwell-and-waves/18-the-wave-equation-and-plane-tem-waves#6-reading-a-wave|Lecture 18 §6]]).

**Which edge is the front?** The pulse travels toward $+y$, so the front is its high-$y$ end: the abrupt 6 V/m edge at $y = 700$ m. The 0 V/m end at $y = 400$ m is the back.

## (a) The pulse at t = 0

At $t = 0$ the pattern was $3\ \mu\text{s}\times200$ m/µs $= 600$ m further back, toward $-y$. So $\mathbf{E}(y,0) = \mathbf{E}(y + 600,\ 3\ \mu\text{s})$:

$$
\mathbf{E}(y,0) = 0.02\,\big((y+600)-400\big)\big[u(y+600-400) - u(y+600-700)\big]\hat z = 0.02\,(y+200)\big[u(y+200)-u(y-100)\big]\hat z\ \ \text{V/m}.
$$

> [!key] Answer (a)
> $\mathbf{E}(y,0) = 0.02\,(y+200)\,\big[u(y+200)-u(y-100)\big]\,\hat z$ V/m: the same ramp, now on $-200<y<100$ m, with its 6 V/m front at $y = 100$ m. The sketch is panel 1 of the figure below part (c).

> [!trap] Shifting the wrong way
> $\mathbf{E}(y - 600,\ 3\ \mu\text{s})$ would put the pulse on $1000<y<1300$ m at $t = 0$, *ahead* of where it is at 3 µs, as if it moved backwards. Check any shift with one point: the front sits at $y_{\text{front}}(t) = 100 + 200t$, which gives 700 m at $t = 3$ µs ✓.

## (b) The field everywhere, at all times

Shift by $v(t - 3)$ instead of by 600 m:

$$
\mathbf{E}(y,t) = \mathbf{E}\big(y - 200(t-3),\ 3\big) = 0.02\,(y - 200t + 200)\big[u(y-200t+200) - u(y-200t-100)\big]\hat z\ \ \text{V/m}.
$$

To see the d'Alembert form, put $s = t - y/v$ (in µs). Then $y - 200t + 200 = 200(1 - s)$ and the field is

$$
E_z(y,t) = F\Big(t - \frac yv\Big),\qquad F(s) = 4\,(1 - s)\,\big[u(s + 0.5) - u(s - 1)\big]\ \ \text{V/m}.
$$

$F$ is what a probe at $y = 0$ records: the front passes $y = 0$ at $t = -0.5$ µs at 6 V/m, and the back at $t = 1$ µs.

> [!key] Answer (b)
> $\mathbf{E}(y,t) = 0.02\,(y-200t+200)\big[u(y-200t+200)-u(y-200t-100)\big]\hat z$ V/m ($y$ in m, $t$ in µs), which is $\hat z\,F(t - y/v)$ with $F(s) = 4(1-s)$ on $-0.5<s<1$ µs. Checks: $t = 3$ gives the given profile, $t = 0$ gives (a), and the field depends on $y$ and $t$ only through $t - y/v$, with the minus sign a $+y$ wave must have.

## (c) What a probe at y = 1 km records

Fix $y = 1000$ m, so $s = t - 1000/200 = t - 5$ µs:

$$
E_z(1000\ \text{m},\ t) = F(t - 5) = 4\,(6 - t)\ \text{V/m}\quad\text{for }4.5<t<6\ \mu\text{s},\qquad 0\ \text{otherwise}.
$$

The front ($y_{\text{front}} = 100 + 200t$) arrives at $t = 4.5$ µs, and the record jumps to 6 V/m. It then falls linearly to zero as the back ($y_{\text{back}} = -200 + 200t$) passes at $t = 6$ µs. The duration, 1.5 µs, is the pulse length divided by the speed: 300 m ÷ 200 m/µs. At $t = 5$ µs the reading is $F(0) = 4$ V/m. Cross-check with the snapshot at 5 µs, $0.02(y - 800)$ on $800<y<1100$ m: at $y = 1000$ m it gives 4 V/m ✓.

> [!key] Answer (c)
> The record jumps to 6 V/m at $t = 4.5$ µs, falls linearly to 0 at $t = 6$ µs, and reads 4 V/m at $t = 5$ µs. It is the snapshot reversed left-to-right. In space the 6 V/m edge leads on the right; in time it comes first, on the left.

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 340" width="640" height="340" role="img" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:14px"><defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="context-stroke"/></marker><marker id="ahs" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="context-stroke"/></marker></defs><text x="20.0" y="24.0" text-anchor="start" fill="currentColor" style="font-size:12.5px;font-weight:600;">1  Snapshots: the pulse slides toward +y at 200 m/µs without changing shape</text><line x1="40.0" y1="144.0" x2="606.0" y2="144.0" stroke="currentColor" stroke-width="1.3" marker-end="url(#ah)" stroke-linecap="round"/><text x="610.0" y="148.0" text-anchor="start" fill="currentColor" style="font-size:12.5px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">y</text><line x1="57.9" y1="141.0" x2="57.9" y2="147.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><text x="57.9" y="159.0" text-anchor="middle" fill="var(--muted)" style="font-size:10px;">-400</text><line x1="117.0" y1="141.0" x2="117.0" y2="147.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><text x="117.0" y="159.0" text-anchor="middle" fill="var(--muted)" style="font-size:10px;">-200</text><line x1="176.2" y1="141.0" x2="176.2" y2="147.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><text x="176.2" y="159.0" text-anchor="middle" fill="var(--muted)" style="font-size:10px;">0</text><line x1="235.3" y1="141.0" x2="235.3" y2="147.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><text x="235.3" y="159.0" text-anchor="middle" fill="var(--muted)" style="font-size:10px;">200</text><line x1="294.4" y1="141.0" x2="294.4" y2="147.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><text x="294.4" y="159.0" text-anchor="middle" fill="var(--muted)" style="font-size:10px;">400</text><line x1="353.6" y1="141.0" x2="353.6" y2="147.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><text x="353.6" y="159.0" text-anchor="middle" fill="var(--muted)" style="font-size:10px;">600</text><line x1="412.7" y1="141.0" x2="412.7" y2="147.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><text x="412.7" y="159.0" text-anchor="middle" fill="var(--muted)" style="font-size:10px;">800</text><line x1="471.8" y1="141.0" x2="471.8" y2="147.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><text x="471.8" y="159.0" text-anchor="middle" fill="var(--muted)" style="font-size:10px;">1000</text><line x1="531.0" y1="141.0" x2="531.0" y2="147.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><text x="531.0" y="159.0" text-anchor="middle" fill="var(--muted)" style="font-size:10px;">1200</text><line x1="590.1" y1="141.0" x2="590.1" y2="147.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><text x="590.1" y="159.0" text-anchor="middle" fill="var(--muted)" style="font-size:10px;">1400</text><text x="608.0" y="159.0" text-anchor="start" fill="var(--muted)" style="font-size:10.5px;">m</text><path d="M52.0,144.0 L117.0,144.0 L205.7,66.0 L205.7,144.0 L596.0,144.0" fill="none" stroke="var(--accent2)" stroke-width="2.2" stroke-dasharray="6 4" stroke-linejoin="round" stroke-linecap="round"/><path d="M52.0,144.0 L294.4,144.0 L383.1,66.0 L383.1,144.0 L596.0,144.0" fill="none" stroke="var(--accent)" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"/><path d="M52.0,144.0 L412.7,144.0 L501.4,66.0 L501.4,144.0 L596.0,144.0" fill="none" stroke="var(--muted)" stroke-width="1.8" stroke-dasharray="2 3" stroke-linejoin="round" stroke-linecap="round"/><line x1="57.9" y1="66.0" x2="63.9" y2="66.0" stroke="currentColor" stroke-width="1.0" stroke-linecap="round"/><text x="66.9" y="70.0" text-anchor="start" fill="var(--muted)" style="font-size:10.5px;">6 V/m</text><text x="112.6" y="99.8" text-anchor="end" fill="var(--accent2)" style="font-size:11.5px;font-weight:600;">t = 0</text><text x="112.6" y="113.8" text-anchor="end" fill="var(--accent2)" style="font-size:10.5px;">(part a)</text><text x="290.0" y="99.8" text-anchor="end" fill="var(--accent)" style="font-size:11.5px;font-weight:600;">t = 3 µs</text><text x="290.0" y="113.8" text-anchor="end" fill="var(--accent)" style="font-size:10.5px;">(given)</text><text x="501.4" y="58.0" text-anchor="middle" fill="var(--muted)" style="font-size:11.5px;font-weight:600;">t = 5 µs</text><line x1="205.7" y1="50.4" x2="383.1" y2="50.4" stroke="currentColor" stroke-width="1.8" marker-end="url(#ah)" stroke-linecap="round"/><text x="294.4" y="44.4" text-anchor="middle" fill="currentColor" style="font-size:11px;">600 m in 3 µs</text><line x1="471.8" y1="146.0" x2="471.8" y2="58.2" stroke="var(--hi)" stroke-width="1.6" stroke-dasharray="4 3" stroke-linecap="round"/><text x="506.7" y="97.2" text-anchor="start" fill="var(--hi)" style="font-size:11px;font-weight:600;">probe at</text><text x="506.7" y="111.2" text-anchor="start" fill="var(--hi)" style="font-size:11px;font-weight:600;">y = 1 km</text><text x="20.0" y="196.0" text-anchor="start" fill="currentColor" style="font-size:12.5px;font-weight:600;">2  What the probe at y = 1 km records: the snapshot reversed (part c)</text><line x1="40.0" y1="300.0" x2="606.0" y2="300.0" stroke="currentColor" stroke-width="1.3" marker-end="url(#ah)" stroke-linecap="round"/><text x="610.0" y="304.0" text-anchor="start" fill="currentColor" style="font-size:12.5px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">t</text><line x1="71.0" y1="297.0" x2="71.0" y2="303.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><text x="71.0" y="315.0" text-anchor="middle" fill="var(--muted)" style="font-size:10.5px;">0</text><line x1="134.2" y1="297.0" x2="134.2" y2="303.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><text x="134.2" y="315.0" text-anchor="middle" fill="var(--muted)" style="font-size:10.5px;">1</text><line x1="197.5" y1="297.0" x2="197.5" y2="303.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><text x="197.5" y="315.0" text-anchor="middle" fill="var(--muted)" style="font-size:10.5px;">2</text><line x1="260.7" y1="297.0" x2="260.7" y2="303.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><text x="260.7" y="315.0" text-anchor="middle" fill="var(--muted)" style="font-size:10.5px;">3</text><line x1="324.0" y1="297.0" x2="324.0" y2="303.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><text x="324.0" y="315.0" text-anchor="middle" fill="var(--muted)" style="font-size:10.5px;">4</text><line x1="387.3" y1="297.0" x2="387.3" y2="303.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><text x="387.3" y="315.0" text-anchor="middle" fill="var(--muted)" style="font-size:10.5px;">5</text><line x1="450.5" y1="297.0" x2="450.5" y2="303.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><text x="450.5" y="315.0" text-anchor="middle" fill="var(--muted)" style="font-size:10.5px;">6</text><line x1="513.8" y1="297.0" x2="513.8" y2="303.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><text x="513.8" y="315.0" text-anchor="middle" fill="var(--muted)" style="font-size:10.5px;">7</text><line x1="577.0" y1="297.0" x2="577.0" y2="303.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><text x="577.0" y="315.0" text-anchor="middle" fill="var(--muted)" style="font-size:10.5px;">8</text><text x="608.0" y="315.0" text-anchor="start" fill="var(--muted)" style="font-size:10.5px;">µs</text><path d="M52.0,300.0 L355.6,300.0 L355.6,222.0 L450.5,300.0 L596.0,300.0" fill="none" stroke="var(--hi)" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"/><circle cx="387.3" cy="248.0" r="4.5" fill="var(--accent)" stroke="none" stroke-width="1.5"/><text x="396.3" y="244.0" text-anchor="start" fill="var(--accent)" style="font-size:11.5px;font-weight:700;">t = 5 µs: 4 V/m</text><text x="349.6" y="226.0" text-anchor="end" fill="currentColor" style="font-size:11px;">front arrives, 4.5 µs</text><text x="458.5" y="292.0" text-anchor="start" fill="currentColor" style="font-size:11px;">back passes, 6 µs</text></svg><figcaption><strong>The worked problem in two pictures.</strong> Panel 1: the given profile at t = 3 µs (solid) is a ramp whose 6 V/m edge is the front. Because the pulse travels toward +y at 200 m/µs, at t = 0 it was 600 m further back (dashed, part a), and at t = 5 µs it is 400 m further on (dotted), straddling the probe. Panel 2: the probe at y = 1 km sees the front first, so its record jumps to 6 V/m at 4.5 µs and then falls linearly to zero at 6 µs. That is the snapshot reversed left-to-right, as for every wave travelling toward +y. At t = 5 µs the probe reads 4 V/m, matching the dotted snapshot at y = 1000 m.</figcaption></figure>

> [!trap] Drawing the record with the snapshot's shape
> The most common wrong sketch is a ramp that rises for 1.5 µs and then drops, a copy of the spatial profile. For travel toward $+y$, $E(y_0,t) = E\big(y_0 - v(t - t_1),\ t_1\big)$. As $t$ increases the position argument *decreases*, so the probe reads the profile from right to left, front first. A wave moving toward $-y$ would give a record with the snapshot's order (see the variant below).

## (d) The medium

The pulse keeps its shape, so the medium is lossless (the true/false below explains why), and in a lossless medium $v = c/\sqrt{\mu_r\epsilon_r}$. Here $\mu_r = 1$, so

$$
\epsilon_r = \Big(\frac cv\Big)^2 = \Big(\frac{2.998\times10^8}{2.0\times10^8}\Big)^2 = 2.25 .
$$

More precisely 2.247 with $c = 2.998\times10^8$ m/s, and exactly 2.25 with $c = 3\times10^8$ m/s. That is polyethylene, the filling of the [[problems/coax-inductance-and-the-lc-product|coax problem]].

> [!key] Answer (d)
> $\epsilon_r\approx2.25$. The statement is **false** on both counts. A wave slower than $c$ is what any dielectric produces ($\epsilon_r>1$); the speed says nothing about conduction. The decrease along the pulse is the pulse's *shape*, not attenuation: the 6 V/m front is still 6 V/m at $t = 0$, at 3 µs, and when it reaches the probe. In a conductor the pulse would shrink and spread as it travelled (Lectures 22–23), and the premise "without changing shape" could not hold.

## (e) The magnetic field

The impedance of the medium:

$$
\eta = \sqrt{\frac{\mu_0}{\epsilon_r\epsilon_0}} = \frac{\eta_0}{\sqrt{\epsilon_r}} = \frac{376.7}{1.5}\ \Omega\approx251\ \Omega,\qquad\text{or directly}\qquad \eta = \mu_0v = 4\pi\times10^{-7}\times2\times10^8 = 80\pi = 251.3\ \Omega .
$$

The direction: $\mathbf{H} = \hat u\times\mathbf{E}/\eta$ with $\hat u = \hat y$ and $\mathbf{E}\parallel\hat z$, and $\hat y\times\hat z = +\hat x$. Check: $\mathbf{E}\times\mathbf{H}\parallel\hat z\times\hat x = +\hat y$, the direction of travel ✓. So $\mathbf{H} = \hat x\,E_z/\eta$:

$$
\mathbf{H}(y,t) = \hat x\,7.96\times10^{-5}\,(y-200t+200)\big[u(y-200t+200)-u(y-200t-100)\big]\ \text{A/m} = \hat x\,\frac{1-s}{20\pi}\ \text{A/m}\ \ (-0.5<s<1\ \mu\text{s}).
$$

At the front, $H = 6/251.3 = 23.9$ mA/m and $B = \mu_0H = E/v = 6/(2\times10^8) = 3.0\times10^{-8}$ T $= 30$ nT.

> [!key] Answer (e)
> $\mathbf{H}(y,t) = \hat x\,E_z(y,t)/\eta$ with $\eta = 80\pi\approx251\ \Omega$; in d'Alembert form $\mathbf{H} = \hat x\,0.0159\,(1-s)$ A/m on $-0.5<s<1$ µs, $s = t - y/v$. Peak values (at the front): $H = 23.9$ mA/m, $B = 30$ nT.

> [!trap] Where this part loses points
> - Using $\eta_0$: $6/377 = 15.9$ mA/m is the vacuum value, not this medium's.
> - $\mathbf{H}$ along $-\hat x$, from $\hat z\times\hat y$ (wrong order), or from relabelling the $\pm z$ sign table by swapping two letters (only a cyclic relabelling, $x\to y\to z\to x$, keeps the signs right). Always finish by checking that $\mathbf{E}\times\mathbf{H}$ points along the travel.
> - Units: 200 m/µs is $2\times10^8$ m/s, not 200 m/s. $\eta = \mu_0v$ needs SI.
> - $\eta$ inverted: $H = E/\eta$ is in milliamperes per metre for volts per metre.

## Variant: the same pulse moving toward −y

Suppose the profile at $t = 3$ µs is the same but $\mathbf{v} = -200\,\hat y$ m/µs. Then $\mathbf{E}(y,t) = \mathbf{E}\big(y + 200(t-3),\ 3\big)$, and at $t = 0$ the pulse sits on $1000<y<1300$ m, the very answer that was wrong above. Now the front is the low-$y$ end. The probe at $y = 1$ km records $E_z = 4t$ V/m for $0<t<1.5$ µs, a rise followed by a drop: the record has the snapshot's order, as for any wave moving toward $-y$. The magnetic field reverses: $\mathbf{H} = (-\hat y)\times\mathbf{E}/\eta = -\hat x\,E_z/\eta$.

## The pattern behind this problem

For a pulse known at one instant $t_1$ and moving rigidly with velocity $v\hat u$ through a lossless medium:

$$
\mathbf{E}(\mathbf{r},t) = \mathbf{E}\big(\mathbf{r} - v\hat u\,(t-t_1),\ t_1\big),\qquad \mu_r\epsilon_r = \Big(\frac cv\Big)^2,\qquad \mathbf{H} = \frac{\hat u\times\mathbf{E}}{\eta},\quad \eta = \mu v = \eta_0\sqrt{\frac{\mu_r}{\epsilon_r}} .
$$

A probe's record is the same formula at fixed $\mathbf{r}$. It is the snapshot read front-first, which reverses it for travel toward $+$ an axis and keeps its order for travel toward $-$. The exam instance (SP18 Exam 2 #4) had an exponentially decaying profile moving toward $-x$ at $c$. It uses the same recipe with the shift in the other direction, and its true/false part turns on the same two observations as (d): the speed and the unchanged shape.
