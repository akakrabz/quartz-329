---
title: "Worked problem — A ramp pulse meets its echo"
description: "A 1 μs ramp pulse on a 600 m line with R_g = 25 Ω and R_L = 150 Ω: the coefficients, V and I along the line before, during and after the reflection, and the echo's return to the generator. Modelled on SP17 Exam 3 #5c."
tags: [problem, transmission-lines]
---

*Problem · style of SP17 Exam 3 #5 · uses [[4-transmission-lines/29-bounce-diagram-examples|Lecture 29]], [[4-transmission-lines/28-distributed-circuits-and-bounce-diagrams|Lecture 28]] · concepts: [[concepts/bounce-diagram]], [[concepts/characteristic-impedance]]*

> [!question] Problem
> A lossless line with $Z_0 = 50\ \Omega$ and $v = 200$ m/μs runs from $z = 0$ to $\ell = 600$ m. A source with internal resistance $R_g = 25\ \Omega$ drives it at $z = 0$, and $R_L = 150\ \Omega$ terminates it. The source's open-circuit voltage is a ramp pulse ($t$ in μs):
> $$
> \begin{gathered}
> f_i(t) = 3t\ \text{V}\quad(0<t<1),\\[4pt]
> f_i(t) = 0\quad\text{otherwise}.
> \end{gathered}
> $$
> (a) Find $\tau_g$, $\Gamma_g$, $\Gamma_L$, the one-way delay $T$ and the pulse's length on the line.
>
> (b) Sketch $V(z)$ and $I(z)$ at $t = 2$ μs and at $t = 5$ μs.
>
> (c) Find $V(z)$ and $I(z)$ at $t = 3.5$ μs. Check them at the load.
>
> (d) Find $V(0,t)$ and $I(0,t)$ for $0<t<12$ μs.

## (a) Coefficients and times

$$
\begin{gathered}
\tau_g = \frac{50}{25+50} = \frac23,\qquad \Gamma_g = \frac{25-50}{25+50} = -\frac13,\\[6pt]
\Gamma_L = \frac{150-50}{150+50} = \frac12,\\[6pt]
T = \frac{600\ \text{m}}{200\ \text{m}/\mu\text{s}} = 3\ \mu\text{s}.
\end{gathered}
$$

The pulse lasts 1 μs, so it is $v\cdot1\ \mu\text{s} = 200$ m long on the line. Segment weights (times $f_i$): $\tfrac23$ on $0<t<3$, $\tfrac23\cdot\tfrac12 = \tfrac13$ on $3<t<6$, $\tfrac13\cdot(-\tfrac13) = -\tfrac19$ on $6<t<9$ μs.

> [!key] Answer (a)
> $\tau_g = \tfrac23$, $\Gamma_g = -\tfrac13$, $\Gamma_L = \tfrac12$, $T = 3$ μs; the pulse is 200 m long. The launched wave is $\tfrac23\cdot3 = 2$ V at its peak.

## (b) Before and after the reflection

Each snapshot is a horizontal cut of the diagram ([[4-transmission-lines/29-bounce-diagram-examples|Lecture 29]] §1), with $z/v = z/200$ in μs.

**$t = 2$ μs.** Only the first segment: $V = \tfrac23f_i(2-z/200) = 4-z/100$ V where $0<2-z/200<1$, i.e. on $200<z<400$ m. It jumps to 2 V at $z = 200$ m (the ramp's end, sent last) and falls to 0 at the front, 400 m. $I = V/Z_0$: 40 mA peak.

**$t = 5$ μs.** Only the echo: $V = \tfrac13f_i(5+z/200-6) = z/200-1$ V on $200<z<400$ m, rising from 0 at its front ($z = 200$ m) to 1 V. Backward wave: $I = -V/Z_0$, down to $-20$ mA. The next forward segment starts at 6 μs.

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 360" width="640" height="360" role="img" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:14px"><defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="context-stroke"/></marker><marker id="ahs" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="context-stroke"/></marker></defs><text x="20.0" y="20.0" text-anchor="start" fill="currentColor" style="font-size:11.5px;font-weight:600;">bounce diagram (weights × f<tspan baseline-shift="sub" style="font-size:9px">i</tspan>)</text><line x1="62.0" y1="62.0" x2="254.0" y2="62.0" stroke="currentColor" stroke-width="1.3" marker-end="url(#ah)" stroke-linecap="round"/><text x="258.0" y="66.0" text-anchor="start" fill="currentColor" style="font-size:12.5px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">z</text><line x1="62.0" y1="62.0" x2="62.0" y2="316.0" stroke="currentColor" stroke-width="1.3" marker-end="url(#ah)" stroke-linecap="round"/><text x="64.0" y="330.0" text-anchor="middle" fill="currentColor" style="font-size:12.5px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">t</text><line x1="232.0" y1="62.0" x2="232.0" y2="304.0" stroke="var(--muted)" stroke-width="1.0" stroke-dasharray="2 3" stroke-linecap="round"/><text x="62.0" y="54.0" text-anchor="middle" fill="var(--muted)" style="font-size:10.5px;">0</text><text x="232.0" y="54.0" text-anchor="middle" fill="var(--muted)" style="font-size:10.5px;">600 m</text><text x="62.0" y="38.0" text-anchor="middle" fill="var(--muted)" style="font-size:10.5px;">Γ<tspan baseline-shift="sub" style="font-size:8px">g</tspan> = −1/3</text><text x="232.0" y="38.0" text-anchor="middle" fill="var(--muted)" style="font-size:10.5px;">Γ<tspan baseline-shift="sub" style="font-size:8px">L</tspan> = 1/2</text><line x1="59.0" y1="62.0" x2="65.0" y2="62.0" stroke="currentColor" stroke-width="1.0" stroke-linecap="round"/><text x="56.0" y="66.0" text-anchor="end" fill="var(--muted)" style="font-size:10px;">0</text><line x1="59.0" y1="151.2" x2="65.0" y2="151.2" stroke="currentColor" stroke-width="1.0" stroke-linecap="round"/><text x="56.0" y="155.2" text-anchor="end" fill="var(--muted)" style="font-size:10px;">3</text><line x1="59.0" y1="240.5" x2="65.0" y2="240.5" stroke="currentColor" stroke-width="1.0" stroke-linecap="round"/><text x="56.0" y="244.5" text-anchor="end" fill="var(--muted)" style="font-size:10px;">6 μs</text><line x1="62.0" y1="121.5" x2="232.0" y2="121.5" stroke="var(--hi)" stroke-width="1.0" stroke-dasharray="4 3" stroke-linecap="round"/><text x="237.0" y="125.5" text-anchor="start" fill="var(--hi)" style="font-size:10.5px;font-weight:600;">2</text><line x1="62.0" y1="166.1" x2="232.0" y2="166.1" stroke="var(--hi)" stroke-width="1.0" stroke-dasharray="4 3" stroke-linecap="round"/><text x="237.0" y="170.1" text-anchor="start" fill="var(--hi)" style="font-size:10.5px;font-weight:600;">3.5</text><line x1="62.0" y1="210.8" x2="232.0" y2="210.8" stroke="var(--hi)" stroke-width="1.0" stroke-dasharray="4 3" stroke-linecap="round"/><text x="237.0" y="214.8" text-anchor="start" fill="var(--hi)" style="font-size:10.5px;font-weight:600;">5</text><line x1="62.0" y1="62.0" x2="232.0" y2="151.2" stroke="var(--accent)" stroke-width="2.4" marker-end="url(#ah)" stroke-linecap="round"/><text x="144.1" y="95.5" text-anchor="middle" fill="var(--accent)" style="font-size:10.5px;font-weight:600;">2/3</text><line x1="232.0" y1="151.2" x2="62.0" y2="240.5" stroke="var(--accent2)" stroke-width="2.4" marker-end="url(#ah)" stroke-linecap="round"/><text x="149.9" y="184.8" text-anchor="middle" fill="var(--accent2)" style="font-size:10.5px;font-weight:600;">1/3</text><line x1="62.0" y1="240.5" x2="175.3" y2="300.0" stroke="var(--accent)" stroke-width="2.4" stroke-linecap="round"/><text x="144.1" y="274.0" text-anchor="middle" fill="var(--accent)" style="font-size:10.5px;font-weight:600;">−1/9</text><text x="330.0" y="56.0" text-anchor="start" fill="currentColor" style="font-size:11.5px;font-weight:600;">t = 2 μs, part (b)</text><line x1="330.0" y1="112.0" x2="598.0" y2="112.0" stroke="currentColor" stroke-width="1.1" marker-end="url(#ahs)" stroke-linecap="round"/><text x="602.0" y="116.0" text-anchor="start" fill="var(--muted)" style="font-size:10.5px;">z (m)</text><line x1="330.0" y1="109.5" x2="330.0" y2="114.5" stroke="currentColor" stroke-width="1.0" stroke-linecap="round"/><text x="330.0" y="125.0" text-anchor="middle" fill="var(--muted)" style="font-size:9.5px;">0</text><line x1="416.7" y1="109.5" x2="416.7" y2="114.5" stroke="currentColor" stroke-width="1.0" stroke-linecap="round"/><text x="416.7" y="125.0" text-anchor="middle" fill="var(--muted)" style="font-size:9.5px;">200</text><line x1="503.3" y1="109.5" x2="503.3" y2="114.5" stroke="currentColor" stroke-width="1.0" stroke-linecap="round"/><text x="503.3" y="125.0" text-anchor="middle" fill="var(--muted)" style="font-size:9.5px;">400</text><line x1="546.7" y1="109.5" x2="546.7" y2="114.5" stroke="currentColor" stroke-width="1.0" stroke-linecap="round"/><line x1="590.0" y1="109.5" x2="590.0" y2="114.5" stroke="currentColor" stroke-width="1.0" stroke-linecap="round"/><text x="590.0" y="125.0" text-anchor="middle" fill="var(--muted)" style="font-size:9.5px;">600</text><line x1="330.0" y1="88.0" x2="590.0" y2="88.0" stroke="var(--muted)" stroke-width="0.7" stroke-dasharray="2 3" stroke-linecap="round"/><text x="326.0" y="91.5" text-anchor="end" fill="var(--muted)" style="font-size:9.5px;">1</text><line x1="330.0" y1="64.0" x2="590.0" y2="64.0" stroke="var(--muted)" stroke-width="0.7" stroke-dasharray="2 3" stroke-linecap="round"/><text x="326.0" y="67.5" text-anchor="end" fill="var(--muted)" style="font-size:9.5px;">2</text><path d="M330.0,112.0 L416.7,112.0 L416.8,64.1 L503.3,112.0 L590.0,112.0" fill="none" stroke="var(--accent)" stroke-width="2.2" stroke-linejoin="round" stroke-linecap="round"/><path d="M330.0,112.0 L416.7,112.0 L416.8,64.1 L503.3,112.0 L590.0,112.0" fill="none" stroke="var(--accent2)" stroke-width="1.8" stroke-dasharray="5 3" stroke-linejoin="round" stroke-linecap="round"/><text x="330.0" y="160.0" text-anchor="start" fill="currentColor" style="font-size:11.5px;font-weight:600;">t = 3.5 μs, part (c)</text><line x1="330.0" y1="216.0" x2="598.0" y2="216.0" stroke="currentColor" stroke-width="1.1" marker-end="url(#ahs)" stroke-linecap="round"/><text x="602.0" y="220.0" text-anchor="start" fill="var(--muted)" style="font-size:10.5px;">z (m)</text><line x1="330.0" y1="213.5" x2="330.0" y2="218.5" stroke="currentColor" stroke-width="1.0" stroke-linecap="round"/><text x="330.0" y="229.0" text-anchor="middle" fill="var(--muted)" style="font-size:9.5px;">0</text><line x1="416.7" y1="213.5" x2="416.7" y2="218.5" stroke="currentColor" stroke-width="1.0" stroke-linecap="round"/><text x="416.7" y="229.0" text-anchor="middle" fill="var(--muted)" style="font-size:9.5px;">200</text><line x1="503.3" y1="213.5" x2="503.3" y2="218.5" stroke="currentColor" stroke-width="1.0" stroke-linecap="round"/><text x="503.3" y="229.0" text-anchor="middle" fill="var(--muted)" style="font-size:9.5px;">400</text><line x1="546.7" y1="213.5" x2="546.7" y2="218.5" stroke="currentColor" stroke-width="1.0" stroke-linecap="round"/><text x="546.7" y="229.0" text-anchor="middle" fill="var(--muted)" style="font-size:9.5px;">500</text><line x1="590.0" y1="213.5" x2="590.0" y2="218.5" stroke="currentColor" stroke-width="1.0" stroke-linecap="round"/><text x="590.0" y="229.0" text-anchor="middle" fill="var(--muted)" style="font-size:9.5px;">600</text><line x1="330.0" y1="192.0" x2="590.0" y2="192.0" stroke="var(--muted)" stroke-width="0.7" stroke-dasharray="2 3" stroke-linecap="round"/><text x="326.0" y="195.5" text-anchor="end" fill="var(--muted)" style="font-size:9.5px;">1</text><line x1="330.0" y1="168.0" x2="590.0" y2="168.0" stroke="var(--muted)" stroke-width="0.7" stroke-dasharray="2 3" stroke-linecap="round"/><text x="326.0" y="171.5" text-anchor="end" fill="var(--muted)" style="font-size:9.5px;">2</text><path d="M330.0,216.0 L546.7,216.0 L546.8,168.0 L590.0,180.0" fill="none" stroke="var(--accent)" stroke-width="2.2" stroke-linejoin="round" stroke-linecap="round"/><path d="M330.0,216.0 L546.7,216.0 L546.8,168.1 L590.0,204.0" fill="none" stroke="var(--accent2)" stroke-width="1.8" stroke-dasharray="5 3" stroke-linejoin="round" stroke-linecap="round"/><text x="330.0" y="264.0" text-anchor="start" fill="currentColor" style="font-size:11.5px;font-weight:600;">t = 5 μs, part (b)</text><line x1="330.0" y1="320.0" x2="598.0" y2="320.0" stroke="currentColor" stroke-width="1.1" marker-end="url(#ahs)" stroke-linecap="round"/><text x="602.0" y="324.0" text-anchor="start" fill="var(--muted)" style="font-size:10.5px;">z (m)</text><line x1="330.0" y1="317.5" x2="330.0" y2="322.5" stroke="currentColor" stroke-width="1.0" stroke-linecap="round"/><text x="330.0" y="357.0" text-anchor="middle" fill="var(--muted)" style="font-size:9.5px;">0</text><line x1="416.7" y1="317.5" x2="416.7" y2="322.5" stroke="currentColor" stroke-width="1.0" stroke-linecap="round"/><text x="416.7" y="357.0" text-anchor="middle" fill="var(--muted)" style="font-size:9.5px;">200</text><line x1="503.3" y1="317.5" x2="503.3" y2="322.5" stroke="currentColor" stroke-width="1.0" stroke-linecap="round"/><text x="503.3" y="357.0" text-anchor="middle" fill="var(--muted)" style="font-size:9.5px;">400</text><line x1="546.7" y1="317.5" x2="546.7" y2="322.5" stroke="currentColor" stroke-width="1.0" stroke-linecap="round"/><line x1="590.0" y1="317.5" x2="590.0" y2="322.5" stroke="currentColor" stroke-width="1.0" stroke-linecap="round"/><text x="590.0" y="357.0" text-anchor="middle" fill="var(--muted)" style="font-size:9.5px;">600</text><line x1="330.0" y1="296.0" x2="590.0" y2="296.0" stroke="var(--muted)" stroke-width="0.7" stroke-dasharray="2 3" stroke-linecap="round"/><text x="326.0" y="299.5" text-anchor="end" fill="var(--muted)" style="font-size:9.5px;">1</text><line x1="330.0" y1="272.0" x2="590.0" y2="272.0" stroke="var(--muted)" stroke-width="0.7" stroke-dasharray="2 3" stroke-linecap="round"/><text x="326.0" y="275.5" text-anchor="end" fill="var(--muted)" style="font-size:9.5px;">2</text><line x1="330.0" y1="344.0" x2="590.0" y2="344.0" stroke="var(--muted)" stroke-width="0.7" stroke-dasharray="2 3" stroke-linecap="round"/><text x="326.0" y="347.5" text-anchor="end" fill="var(--muted)" style="font-size:9.5px;">−1</text><path d="M330.0,320.0 L416.7,320.0 L503.2,296.0 L503.3,320.0 L590.0,320.0" fill="none" stroke="var(--accent)" stroke-width="2.2" stroke-linejoin="round" stroke-linecap="round"/><path d="M330.0,320.0 L416.7,320.0 L503.2,344.0 L503.3,320.0 L590.0,320.0" fill="none" stroke="var(--accent2)" stroke-width="1.8" stroke-dasharray="5 3" stroke-linejoin="round" stroke-linecap="round"/><line x1="470.0" y1="18.0" x2="492.0" y2="18.0" stroke="var(--accent)" stroke-width="2.2" stroke-linecap="round"/><text x="497.0" y="22.0" text-anchor="start" fill="currentColor" style="font-size:10.5px;">V (V)</text><line x1="470.0" y1="34.0" x2="492.0" y2="34.0" stroke="var(--accent2)" stroke-width="2.2" stroke-dasharray="5 3" stroke-linecap="round"/><text x="497.0" y="38.0" text-anchor="start" fill="currentColor" style="font-size:10.5px;">Z<tspan baseline-shift="sub" style="font-size:9px">0</tspan>I (V)</text></svg><figcaption><strong>The ramp pulse.</strong> 2 μs: heading right, the ramp is drawn backwards (its 0 V start leads). 3.5 μs: pulse and echo overlap on 500–600 m; V adds, I subtracts. 5 μs: the echo, half as large, heads left, drawn forwards. Z<sub>0</sub> = 50 Ω.</figcaption></figure>

> [!key] Answer (b)
> - $t = 2$ μs: $V = 4-z/100$ V, $I = V/50$, on $200<z<400$ m; zero elsewhere.
> - $t = 5$ μs: $V = z/200-1$ V, $I = -V/50$, on $200<z<400$ m; zero elsewhere.

> [!trap] Where (b) loses points
> - Drawing the forward ramp rising toward $+z$. Its 0 V start leads, so it falls toward $+z$.
> - Forgetting the sign of $I$ for the echo. $\Gamma_L>0$ keeps $V$ positive but makes $I$ negative.

## (c) Overlap at t = 3.5 μs

Two segments contribute. The cut crosses only the echo, but the forward ramp's tail is still arriving.

$$
\begin{gathered}
V^+ = \tfrac23f_i\Big(3.5-\frac z{200}\Big) = 7-\frac z{100},\\[6pt]
V^- = \tfrac13f_i\Big(\frac z{200}-2.5\Big) = \frac z{200}-2.5,
\end{gathered}
$$

both on $500<z<600$ m and zero elsewhere. The forward ramp's first 100 m has already reflected into $V^-$. On $500<z<600$ m:

$$
\begin{gathered}
V = V^++V^- = 4.5-\frac z{200}\ \text{V},\\[6pt]
I = \frac{V^+-V^-}{Z_0} = \frac{9.5-0.015\,z}{50}\ \text{A}.
\end{gathered}
$$

> [!key] Answer (c)
> $V$ falls from 2 V at $z = 500$ m to 1.5 V at the load; $I$ falls from 40 mA to 10 mA. Zero for $z<500$ m.
>
> Load check: $V(\ell)/I(\ell) = 1.5\ \text{V}/10\ \text{mA} = 150\ \Omega = R_L$, and $V(\ell) = (1+\Gamma_L)V^+(\ell) = 1.5\cdot1$ V.

## (d) At the generator

A vertical cut at $z = 0$ (Lecture 28's recipe):

- $0<t<1$: the launched wave alone. $V(0,t) = \tfrac23f_i(t) = 2t$ V and $I = V/Z_0 = 40t$ mA.
- $1<t<6$: zero; the pulse is on the line.
- $6<t<7$: the echo arrives, $V^- = \tfrac13f_i(t-6) = t-6$ V, and leaves as $\Gamma_gV^-$. Add both segments:

$$
\begin{gathered}
V(0,t) = (1+\Gamma_g)V^- = \tfrac23(t-6)\ \text{V},\\[6pt]
I(0,t) = \frac{\Gamma_gV^- - V^-}{Z_0} = -\frac{4}{3}\cdot\frac{t-6}{50}\ \text{A}.
\end{gathered}
$$

- $7<t<12$: zero; the next echo returns at 12 μs.

> [!key] Answer (d)
> $V(0,t) = 2t$ V and $I(0,t) = 40t$ mA on $0<t<1$; $V(0,t) = \tfrac23(t-6)$ V and $I(0,t) = -26.7(t-6)$ mA on $6<t<7$; zero otherwise.
>
> Check: for $t>1$ the source is off, so KVL gives $V(0,t) = -R_gI(0,t)$, and $-25\cdot(-26.7\ \text{mA}) = 0.667$ V at $t\to7$.

## The pattern

1. Coefficients, $T$, pulse length.
2. The segments in flight; each is a weighted, delayed copy of $f_i$.
3. Where each argument lies inside the pulse.
4. $V$ adds the copies; $Z_0I$ subtracts the backward ones.
5. Ohm's law at the end involved.

SP17 Exam 3 #5c sends a truncated sine through a line with $\Gamma_g = \tfrac13$, $\Gamma_L = -\tfrac13$ and asks for $V(z)$ at two times. This version uses a ramp, so the reversal shows, adds $I$, an overlap snapshot and the generator end.
