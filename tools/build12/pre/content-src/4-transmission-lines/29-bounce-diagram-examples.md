---
title: "Lecture 29 — Bounce diagram examples"
description: "The notes' three bounce-diagram examples: read the impulse response off the diagram, then replace each impulse by a delayed copy of the source. A 1 MHz burst on a line with a matched generator, a step watched at the midpoint until it reaches its DC value, and snapshots of a two-level pulse and its echo."
tags: [lecture, transmission-lines]
lecture: 29
---

*Lecture 29 · course notes §29 (no slides) · prev: [[4-transmission-lines/28-distributed-circuits-and-bounce-diagrams|Lecture 28]] · next: [[4-transmission-lines/30-multi-line-circuits|Lecture 30]] · worked problem: [[problems/a-ramp-pulse-meets-its-echo|A ramp pulse meets its echo]] · practice: [[practice/29-bounce-diagram-examples|12 problems]]*

> [!abstract] In one breath
> No new theory: [[4-transmission-lines/28-distributed-circuits-and-bounce-diagrams|Lecture 28]]'s bounce diagram, used three times. Read the impulse response $h_z(t)$ off the diagram, then replace every $\delta(t-t_k)$ by $f_i(t-t_k)$. A vertical line through the diagram gives the waveform at one $z$; a horizontal line gives a snapshot along the line. Example 1: a 1 MHz burst with a matched generator, one echo, then a steady sinusoid. Example 2: a step watched at the midpoint, a staircase that settles to the DC value. Example 3: snapshots of a two-level pulse and its echo.

## 1. Two ways to cut a bounce diagram

Lecture 28 gives the impulse response as a sum over the diagram's segments, and the recipe for a **vertical cut**: the waveform $V(z_p,t)$ at one point, one delayed copy of $f_i$ per crossing. Its conventions hold here: $Z_0$, speed $v$, length $\ell$, one-way delay $T = \ell/v$, segments labelled with voltage weights, current signs flipped on backward segments.

A **horizontal cut** at $t = t_p$ gives a snapshot $V(z,t_p)$ along the whole line. Every segment that has started by $t_p$ carries its own copy of $f_i$. The copy trails its segment by the input's duration, so a segment the cut no longer crosses can still contribute (Example 1 at 4.5 μs, Example 3 at 9 μs):

> [!key] Snapshot from a horizontal cut
> $$
> \begin{gathered}
> \text{forward segment } n{:}\\[2pt]
> w\,f_i\Big(t_p-\frac zv-2nT\Big),\\[6pt]
> \text{backward segment } n{:}\\[2pt]
> w\,f_i\Big(t_p+\frac zv-2(n+1)T\Big),
> \end{gathered}
> $$
> with $w$ the segment's weight. Add the terms for $V$; subtract the backward ones for $Z_0I$. A term is non-zero only where its argument lies inside the pulse.

> [!intuition] Which way round a pulse lies
> A pulse's leading edge points the way it travels. A forward pulse therefore lies on the $z$ axis in reverse order compared with $f_i(t)$ on the $t$ axis: the part sent first is furthest right. An echo lies in the same order as $f_i(t)$: the part sent first is furthest left. Its length is $v$ times its duration.

Notation: the notes write $Z_o$, use both $l$ and $\ell$, and call the source $f(t)$ in Examples 2–3; this page writes $Z_0$, $\ell$ and $f_i(t)$ throughout. Times are in μs, and $z/v$ is converted to μs with $v = c = 300$ m/μs.

## 2. Example 1: a sine burst, matched generator

The notes' circuit: $\ell = 900$ m, $v = c$, $R_g = Z_0$, $R_L = 2Z_0$, and open-circuit source voltage $f_i(t) = \sin(\omega t)\,u(t)$ with $\omega/2\pi = 1$ MHz.

$$
\begin{gathered}
\tau_g = \frac{Z_0}{Z_0+Z_0} = \frac12,\qquad \Gamma_g = 0,\\[6pt]
\Gamma_L = \frac{2Z_0-Z_0}{2Z_0+Z_0} = \frac13,\\[6pt]
2T = \frac{2\cdot900\ \text{m}}{300\ \text{m}/\mu\text{s}} = 6\ \mu\text{s}.
\end{gathered}
$$

$\Gamma_g = 0$: the generator absorbs the echo, so the diagram has two segments and ends at $t = 2T$.

> [!key] Example 1 response
> Times and $z/v$ in μs:
> $$
> \begin{gathered}
> h_z(t) = \tfrac12\,\delta\Big(t-\frac zv\Big) + \tfrac16\,\delta\Big(t+\frac zv-6\Big),\\[8pt]
> V(z,t) = \tfrac12\sin\omega\Big(t-\frac zv\Big)\,u\Big(t-\frac zv\Big)\\[2pt]
> +\ \tfrac16\sin\omega\Big(t+\frac zv-6\Big)\,u\Big(t+\frac zv-6\Big).
> \end{gathered}
> $$
> $Z_0I(z,t)$ is the same with $-\tfrac16$.

<!-- fig:bex-example1 -->

Reading it:
- $\lambda = v/f = 300$ m, so the line is $3\lambda$ long. At $t = 1$ μs the front is at $z = 300$ m with one wavelength of amplitude $\tfrac12$ behind it; at $t = 2$ μs, two wavelengths (the notes' margin plots).
- The front reaches the load at 3 μs, where the two segments meet: $V(\ell,t) = (1+\Gamma_L)\tfrac12\sin\omega(t-3) = \tfrac23\sin\omega(t-3)$ for $t>3$ μs.
- At $t = 4.5$ μs the echo has come back to $z = 450$ m. To its right the two waves add.
- From $t = 6$ μs on, both terms fill the line. Since $\omega\cdot6\ \mu\text{s} = 12\pi$, with $\beta = \omega/v$ the line holds $\tfrac12\sin(\omega t-\beta z) + \tfrac16\sin(\omega t+\beta z)$ for good. It is the partial standing wave of [[3-maxwell-and-waves/26-standing-waves-and-radiation-pressure|Lecture 26]]: amplitude between $\tfrac13$ and $\tfrac23$, maxima every 150 m, one of them at the load. Lecture 31 treats this sinusoidal steady state.

## 3. Example 2: a step at the midpoint

Circuit: $Z_0 = 50\ \Omega$, $v = c$, $\ell = 2400$ m, $R_g = 0$, $R_L = 100\ \Omega$, $f_i(t) = u(t)$. Find $V(1200,t)$.

$$
\begin{gathered}
\tau_g = 1,\qquad \Gamma_g = -1,\\[4pt]
\Gamma_L = \frac13,\qquad T = 8\ \mu\text{s}.
\end{gathered}
$$

The vertical line at $z = 1200$ m is crossed every 8 μs from $t = 4$ μs, alternately by forward and backward segments:

> [!key] Example 2 at z = 1200 m
> Times in μs:
> $$
> \begin{gathered}
> h_{1200}(t) = \delta(t-4) + \tfrac13\delta(t-12)\\[2pt]
> -\ \tfrac13\delta(t-20) - \tfrac19\delta(t-28)\\[2pt]
> +\ \tfrac19\delta(t-36) + \cdots,\\[8pt]
> V(1200,t) = u(t-4) + \tfrac13u(t-12)\\[2pt]
> -\ \tfrac13u(t-20) - \tfrac19u(t-28)\\[2pt]
> +\ \tfrac19u(t-36) + \cdots
> \end{gathered}
> $$
> Levels: 1, 4/3, 1, 8/9, 1, 28/27, 1, … V.

<!-- fig:bex-example2 -->

- $\Gamma_g = -1$ launches each forward segment as the negative of the backward one that arrived. Once both have passed, they cancel, so every second level is exactly 1 V.
- The current (this site's addition) flips the backward steps: $Z_0I(1200,t) = u(t-4) - \tfrac13u(t-12) - \tfrac13u(t-20) + \tfrac19u(t-28) + \tfrac19u(t-36) - \cdots$. In mA: 20, 13.3, 6.7, 8.9, 11.1, 10.4, 9.6, …

## 4. The DC limit

As $t\to\infty$, $V(1200,t)\to1$ V and $I(1200,t)\to10$ mA. With $R_g = 0$, the 1 V source sits directly across $R_L = 100\ \Omega$: these are the lumped-circuit values, as [[4-transmission-lines/28-distributed-circuits-and-bounce-diagrams|Lecture 28]]'s DC limit $V_0R_L/(R_g+R_L)$, $V_0/(R_g+R_L)$ predicts.

The notes' reasons and limits:
- DC means $\omega = 0$ and $\lambda\to\infty$. Then $\ell\ll\lambda$ always holds, and the line is an ordinary pair of wires.
- Only inputs that settle to a constant, such as $u(t)$ and its delayed copies, reach a DC limit. $\sin(\omega t)\,u(t)$ never does; Example 1 keeps oscillating.

> [!trap] Reading a step response
> - The staircase converges as $(\Gamma_L\Gamma_g)^n$. Here $\Gamma_L\Gamma_g = -\tfrac13$: the error shrinks threefold per round trip and alternates in sign.
> - Once an echo has arrived, the total $I$ is not $V/Z_0$: on 12–20 μs, $V = \tfrac43$ V but $I = 13.3$ mA, not 26.7 mA.

## 5. Example 3: a two-level pulse, snapshots in z

The notes say "the circuit of Example 1" but use Example 2's ($\tau_g = 1$, $\Gamma_g = -1$, $\Gamma_L = \tfrac13$, $2T = 16$ μs, $Z_0 = 50\ \Omega$). The source is $f_i(t) = \text{rect}(t) + 2\,\text{rect}(t-1)$ ($t$ in μs; the notes' $T$ there is the 1 μs width): 1 V for $-0.5<t<0.5$, then 2 V until $t = 1.5$. With $\Gamma_L\Gamma_g = -\tfrac13$:

> [!key] Example 3 response
> Times and $z/c$ in μs:
> $$
> \begin{gathered}
> V(z,t) = \sum_{n=0}^{\infty}\Big(-\frac13\Big)^n\Big[f_i\Big(t-\frac zc-16n\Big)\\[2pt]
> +\ \frac13\,f_i\Big(t+\frac zc-16(n+1)\Big)\Big].
> \end{gathered}
> $$
> $50\,I(z,t)$ is the same with $-\tfrac13$ in front of the second term.

The two snapshots of the notes:
- **$t = 3$ μs.** Only the first forward segment: $f_i(3-z/c)\ne0$ for $1.5<z/c<3.5$. That is 2 V on 450–750 m and 1 V on 750–1050 m, with $I = V/50$: 40 and 20 mA.
- **$t = 11$ μs.** Only the first echo, $\tfrac13f_i(z/c-5)$: $\tfrac13$ V on 1350–1650 m and $\tfrac23$ V on 1650–1950 m, with $I = -V/50$.

In both, the 1 V part, sent first, leads: on the right at 3 μs, on the left at 11 μs (§1).

<!-- fig:bex-example3 -->

> [!example] Example — the pulse meets its echo, t = 9 μs (this site's numbers)
> The 1 V part has reflected; the 2 V part is arriving. Forward: $f_i(9-z/c)$ is 2 V on 2250–2400 m. Echo: $\tfrac13f_i(z/c-7)$ is $\tfrac13$ V on 1950–2250 m and $\tfrac23$ V on 2250–2400 m.
> - 1950–2250 m, echo alone: $V = \tfrac13$ V, $I = -6.7$ mA.
> - 2250–2400 m: $V = 2+\tfrac23 = \tfrac83$ V and $I = (2-\tfrac23)/50 = 26.7$ mA.
>
> On the last stretch the 2 V part overlaps its own echo, so $V/I = 100\ \Omega = R_L$, as at the load.

## 6. Summary

- Vertical cut (Lecture 28): $V(z_p,t)$ as delayed copies of $f_i$. Horizontal cut: the snapshot $V(z,t_p)$, one copy of $f_i$ per segment started by $t_p$, including segments the cut has already passed.
- On a snapshot, forward pulses lie reversed, echoes in source order.
- Example 1 ($\Gamma_g = 0$): a $\tfrac12$ burst and one $\tfrac16$ echo; $\tfrac23\sin\omega(t-3)$ at the load; a steady partial standing wave after 6 μs.
- Example 2 ($\Gamma_g = -1$, $\Gamma_L = \tfrac13$): $V(1200,t)$ steps through 1, 4/3, 1, 8/9, … to 1 V; $I$ to 10 mA. These are the DC values.
- A DC limit exists only for inputs that settle.
- Example 3: forward pulse at 3 μs, overlap at 9 μs, a $\tfrac13$-size echo at 11 μs.
- Next, [[4-transmission-lines/30-multi-line-circuits|Lecture 30]]: junctions between lines.

Concept pages: [[concepts/bounce-diagram]] · [[concepts/characteristic-impedance]] · [[concepts/superposition]] · [[concepts/standing-waves]] · [[concepts/reflection-and-transmission]].

> [!exam] On exams
> The Exam 3 papers on hand ask Lecture 29 skills in three forms.
> - **Waveform at one point** (SP18 E3 #3c–d, both ends; S20 FE #5b–c at $\ell/2$; FA23 E3 #5(c), a pulse into a short): vertical cut, one copy of $f_i$ per crossing; at an end add both segments.
> - **Snapshot along the line** (SP17 E3 #5c, a sine burst at two times): horizontal cut; mind which way round each pulse lies. See the worked problem.
> - **Timing and steady state** (FA23 E3 #3(a)(iv), SP19 E3 #4f–g): arrival times from the diagram; the DC divider for $t\to\infty$.

> [!tip] Practice this lecture
> [[practice/29-bounce-diagram-examples|12 practice problems]] — 5 easy, 3 medium, 4 hard — each with a folded hint and a worked solution. Start with [[practice/29-bounce-diagram-examples#291-which-way-round|29.1 Which way round]]; the [[practice/index|practice hub]] has the whole bank by difficulty and by topic.

### Sources for this page
Kudeki notes, Lecture 29 (4 pages): Examples 1–3 with their margin diagrams and plots, and the DC-limit remarks. Rao (2009) §7.4, Examples 7.4–7.5 (voltage versus $t$ and versus $z$ for a pulse), for cross-checks. This site's own: the horizontal-cut rule and pulse order, the load voltage and steady state in Example 1, all currents, the 9 μs snapshot, the traps and the figures; numbers checked against two time-steppings of the line. Slips in the notes (two wrong example references, a plot label) are on the errata page.
