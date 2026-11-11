---
title: "Lecture 31 — Periodic oscillations in lossless TL circuits"
description: "A lossless line segment with open or shorted ends rings at infinitely many, harmonically related frequencies. Like ends hold a whole number of half wavelengths, unlike ends an odd number of quarter wavelengths; each resonance is a standing wave, and any periodic waveform on the line is a sum of them."
tags: [lecture, transmission-lines]
lecture: 31
---

*Lecture 31 · course notes §31 · slides "Lecture 31: Oscillations in Short and Open Stubs", slides 9–14 (annotated deck, Nov 9; its slides 2–8 go with Lecture 32 on this site) · prev: [[4-transmission-lines/30-multi-line-circuits|Lecture 30]] · next: [[4-transmission-lines/32-input-impedance-and-microwave-resonators|Lecture 32]] · worked twin: [[exams/e3-steady-state-lines#s3-resonances-from-two-measurements|Resonances from two measurements]] · practice: [[practice/31-resonances-of-line-segments|8 problems]]*

> [!abstract] In one breath
> An LC circuit rings at one frequency. A lossless line segment with open or shorted ends rings at infinitely many, all multiples of one fundamental. The end conditions pick them. With like ends the wave on the line must repeat after one round trip, $2\ell/v$, and a whole number of half wavelengths fits the line. With one end open and one shorted it repeats after two round trips, only odd harmonics survive, and an odd number of quarter wavelengths fits. Each resonance is a standing wave, and any periodic waveform on the line is a sum of them.

## 1. One resonance, or infinitely many

A lossless LC loop supports a source-free, co-sinusoidal oscillation at one frequency, $\omega = 1/\sqrt{LC}$. A lossless line stores the same two kinds of energy, spread along its length ($\mathcal{L}$ and $\mathcal{C}$ per metre, [[4-transmission-lines/27-guided-tem-waves-on-transmission-lines|Lecture 27]]). Cut off from every source, it can also oscillate, with two differences:

- there are **infinitely many** resonance frequencies, harmonically related;
- the waveform need not be a cosine: sums of the harmonics build any periodic shape, as in a Fourier series.

The tool is the general solution of [[4-transmission-lines/27-guided-tem-waves-on-transmission-lines|Lecture 27]], with the end conditions of [[4-transmission-lines/28-distributed-circuits-and-bounce-diagrams|Lecture 28]]:

$$
V = f\Big(t-\frac zv\Big)+g\Big(t+\frac zv\Big),\qquad I = \frac{1}{Z_0}\Big[f\Big(t-\frac zv\Big)-g\Big(t+\frac zv\Big)\Big].
$$

## 2. A segment open at both ends

Nothing is connected at $z = 0$ or at $z = \ell$, so the current vanishes at both ends at all times.

- $I(0,t) = 0$ gives $g(t) = f(t)$: one function describes both waves.
- $I(\ell,t) = 0$ gives $f(t-\ell/v) = f(t+\ell/v)$, that is $f(t) = f(t+2\ell/v)$: the function is **periodic**.

> [!key] The fundamental of a segment with like ends
> $$
> T = \frac{2\ell}{v},\qquad \omega_0 = \frac{2\pi}{T} = \frac{\pi v}{\ell},\qquad \beta_0 = \frac{\omega_0}{v} = \frac{\pi}{\ell}.
> $$
> $T$ is the round-trip time. Nothing else is required of $f$: any waveform with this period is allowed.

> [!intuition] Why the round trip
> An open end reflects with $\Gamma = +1$ ([[4-transmission-lines/28-distributed-circuits-and-bounce-diagrams|Lecture 28]]). A wave leaving a point returns to it, travelling the same way and with the same sign, after two reflections and a path $2\ell$. The line repeats itself every $2\ell/v$.

The most general $f$ with this period is a Fourier series, $f(t) = F_0+\sum_{n\ge1}F_n\cos(n\omega_0t+\theta_n)$, with arbitrary $F_n$ and $\theta_n$. Put it into $V$ and $I$ with $g = f$ and use $\cos(a-b)\mp\cos(a+b)$:

$$
\begin{gathered}
I(z,t) = \sum_{n=1}^{\infty}\frac{2F_n}{Z_0}\,\sin(n\omega_0t+\theta_n)\,\sin(n\beta_0z),\\[4pt]
V(z,t) = 2F_0+\sum_{n=1}^{\infty}2F_n\,\cos(n\omega_0t+\theta_n)\,\cos(n\beta_0z).
\end{gathered}
$$

Each term is a **resonant mode**: a standing wave, the line's version of the wave in front of a mirror ([[concepts/standing-waves|Standing waves]]).

> [!key] Mode n of an open–open segment (n = 1, 2, 3, …)
> $$
> f_n = \frac{nv}{2\ell},\qquad \lambda_n = \frac{v}{f_n} = \frac{2\ell}{n},\qquad \ell = n\,\frac{\lambda_n}{2}.
> $$
> The line is a whole number of half wavelengths long at every resonance.

What a mode looks like:
- $I\propto\sin(n\beta_0z)$: zero at both ends, as required. $V\propto\cos(n\beta_0z)$: largest at both ends.
- Voltage nulls sit on current maxima, a quarter wavelength from the nearest current null.
- $V$ and $I$ are a quarter period apart in time ($\cos$ against $\sin$): the energy moves between $\tfrac12\mathcal{C}V^2$ and $\tfrac12\mathcal{L}I^2$, and no average power flows.
- The constant $2F_0$ is a DC voltage with no current: a charged, open line. It is allowed too.

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 660 318" width="660" height="318" role="img" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:14px"><defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="context-stroke"/></marker><marker id="ahs" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="context-stroke"/></marker></defs><text x="166.0" y="18.0" text-anchor="middle" fill="currentColor" style="font-size:12.5px;font-weight:600;">open at z = 0, open at z = ℓ</text><line x1="46.0" y1="122.0" x2="302.0" y2="122.0" stroke="currentColor" stroke-width="1.2" marker-end="url(#ah)" stroke-linecap="round"/><text x="308.0" y="126.0" text-anchor="start" fill="currentColor" style="font-size:12px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">z</text><line x1="46.0" y1="122.0" x2="46.0" y2="34.0" stroke="currentColor" stroke-width="1.0" stroke-linecap="round"/><line x1="286.0" y1="122.0" x2="286.0" y2="34.0" stroke="currentColor" stroke-width="1.0" stroke-dasharray="3 3" stroke-linecap="round"/><path d="M46.0,44.0 L52.0,44.2 L59.0,45.1 L65.0,46.4 L72.0,48.5 L85.0,53.9 L99.0,62.0 L113.0,72.1 L128.0,84.8 L144.0,99.8 L166.0,122.0 L188.0,99.8 L204.0,84.8 L219.0,72.1 L233.0,62.0 L247.0,53.9 L260.0,48.5 L267.0,46.4 L273.0,45.1 L280.0,44.2 L286.0,44.0" fill="none" stroke="var(--accent)" stroke-width="2.2" stroke-linejoin="round" stroke-linecap="round"/><path d="M46.0,122.0 L68.0,99.8 L84.0,84.8 L99.0,72.1 L113.0,62.0 L127.0,53.9 L140.0,48.5 L147.0,46.4 L153.0,45.1 L160.0,44.2 L166.0,44.0 L172.0,44.2 L179.0,45.1 L185.0,46.4 L192.0,48.5 L205.0,53.9 L219.0,62.0 L233.0,72.1 L248.0,84.8 L264.0,99.8 L286.0,122.0" fill="none" stroke="var(--hi)" stroke-width="2.2" stroke-dasharray="6 4" stroke-linejoin="round" stroke-linecap="round"/><text x="46.0" y="137.0" text-anchor="middle" fill="var(--muted)" style="font-size:10.5px;">0</text><text x="286.0" y="137.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">ℓ</text><text x="166.0" y="152.0" text-anchor="middle" fill="currentColor" style="font-size:11.5px;">ℓ = λ/2   (n = 1)</text><text x="40.0" y="30.0" text-anchor="end" fill="var(--muted)" style="font-size:10px;">open</text><text x="292.0" y="30.0" text-anchor="start" fill="var(--muted)" style="font-size:10px;">open</text><line x1="46.0" y1="254.0" x2="302.0" y2="254.0" stroke="currentColor" stroke-width="1.2" marker-end="url(#ah)" stroke-linecap="round"/><text x="308.0" y="258.0" text-anchor="start" fill="currentColor" style="font-size:12px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">z</text><line x1="46.0" y1="254.0" x2="46.0" y2="166.0" stroke="currentColor" stroke-width="1.0" stroke-linecap="round"/><line x1="286.0" y1="254.0" x2="286.0" y2="166.0" stroke="currentColor" stroke-width="1.0" stroke-dasharray="3 3" stroke-linecap="round"/><path d="M46.0,176.0 L52.0,177.0 L55.0,178.2 L59.0,180.5 L65.0,185.5 L72.0,193.4 L79.0,203.3 L87.0,216.8 L95.0,231.8 L106.0,254.0 L123.0,220.4 L129.0,209.8 L135.0,200.3 L141.0,192.1 L147.0,185.5 L153.0,180.5 L158.0,177.7 L162.0,176.4 L166.0,176.0 L169.0,176.2 L173.0,177.3 L176.0,178.7 L180.0,181.2 L184.0,184.5 L188.0,188.6 L196.0,198.8 L204.0,211.5 L213.0,228.0 L226.0,254.0 L237.0,231.8 L245.0,216.8 L253.0,203.3 L260.0,193.4 L267.0,185.5 L273.0,180.5 L277.0,178.2 L280.0,177.0 L286.0,176.0" fill="none" stroke="var(--accent)" stroke-width="2.2" stroke-linejoin="round" stroke-linecap="round"/><path d="M46.0,254.0 L57.0,231.8 L65.0,216.8 L73.0,203.3 L80.0,193.4 L87.0,185.5 L93.0,180.5 L97.0,178.2 L100.0,177.0 L106.0,176.0 L112.0,177.0 L115.0,178.2 L119.0,180.5 L125.0,185.5 L132.0,193.4 L139.0,203.3 L147.0,216.8 L155.0,231.8 L166.0,254.0 L179.0,228.0 L188.0,211.5 L196.0,198.8 L204.0,188.6 L208.0,184.5 L212.0,181.2 L216.0,178.7 L219.0,177.3 L223.0,176.2 L226.0,176.0 L230.0,176.4 L234.0,177.7 L239.0,180.5 L245.0,185.5 L251.0,192.1 L257.0,200.3 L263.0,209.8 L269.0,220.4 L286.0,254.0" fill="none" stroke="var(--hi)" stroke-width="2.2" stroke-dasharray="6 4" stroke-linejoin="round" stroke-linecap="round"/><text x="46.0" y="269.0" text-anchor="middle" fill="var(--muted)" style="font-size:10.5px;">0</text><text x="286.0" y="269.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">ℓ</text><text x="166.0" y="284.0" text-anchor="middle" fill="currentColor" style="font-size:11.5px;">ℓ = λ   (n = 2)</text><text x="40.0" y="162.0" text-anchor="end" fill="var(--muted)" style="font-size:10px;">open</text><text x="292.0" y="162.0" text-anchor="start" fill="var(--muted)" style="font-size:10px;">open</text><text x="496.0" y="18.0" text-anchor="middle" fill="currentColor" style="font-size:12.5px;font-weight:600;">open at z = 0, short at z = ℓ</text><line x1="376.0" y1="122.0" x2="632.0" y2="122.0" stroke="currentColor" stroke-width="1.2" marker-end="url(#ah)" stroke-linecap="round"/><text x="638.0" y="126.0" text-anchor="start" fill="currentColor" style="font-size:12px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">z</text><line x1="376.0" y1="122.0" x2="376.0" y2="34.0" stroke="currentColor" stroke-width="1.0" stroke-linecap="round"/><line x1="616.0" y1="122.0" x2="616.0" y2="34.0" stroke="currentColor" stroke-width="1.0" stroke-dasharray="3 3" stroke-linecap="round"/><path d="M376.0,44.0 L388.0,44.2 L401.0,45.0 L414.0,46.4 L427.0,48.3 L440.0,50.7 L454.0,53.9 L481.0,61.7 L509.0,71.7 L539.0,84.3 L572.0,99.8 L616.0,122.0" fill="none" stroke="var(--accent)" stroke-width="2.2" stroke-linejoin="round" stroke-linecap="round"/><path d="M376.0,122.0 L420.0,99.8 L453.0,84.3 L483.0,71.7 L511.0,61.7 L538.0,53.9 L552.0,50.7 L565.0,48.3 L578.0,46.4 L591.0,45.0 L604.0,44.2 L616.0,44.0" fill="none" stroke="var(--hi)" stroke-width="2.2" stroke-dasharray="6 4" stroke-linejoin="round" stroke-linecap="round"/><text x="376.0" y="137.0" text-anchor="middle" fill="var(--muted)" style="font-size:10.5px;">0</text><text x="616.0" y="137.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">ℓ</text><text x="496.0" y="152.0" text-anchor="middle" fill="currentColor" style="font-size:11.5px;">ℓ = λ/4   (n = 0)</text><text x="370.0" y="30.0" text-anchor="end" fill="var(--muted)" style="font-size:10px;">open</text><text x="622.0" y="30.0" text-anchor="start" fill="var(--muted)" style="font-size:10px;">short</text><line x1="376.0" y1="254.0" x2="632.0" y2="254.0" stroke="currentColor" stroke-width="1.2" marker-end="url(#ah)" stroke-linecap="round"/><text x="638.0" y="258.0" text-anchor="start" fill="currentColor" style="font-size:12px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">z</text><line x1="376.0" y1="254.0" x2="376.0" y2="166.0" stroke="currentColor" stroke-width="1.0" stroke-linecap="round"/><line x1="616.0" y1="254.0" x2="616.0" y2="166.0" stroke="currentColor" stroke-width="1.0" stroke-dasharray="3 3" stroke-linecap="round"/><path d="M376.0,176.0 L384.0,177.0 L388.0,178.2 L393.0,180.3 L402.0,185.9 L411.0,193.7 L420.0,203.3 L430.0,215.9 L441.0,231.4 L456.0,254.0 L473.0,228.4 L485.0,211.9 L496.0,198.8 L502.0,192.7 L507.0,188.3 L512.0,184.5 L517.0,181.4 L522.0,178.9 L527.0,177.2 L532.0,176.2 L537.0,176.0 L542.0,176.5 L547.0,177.8 L554.0,180.8 L562.0,185.9 L569.0,191.8 L577.0,199.9 L585.0,209.4 L594.0,221.3 L616.0,254.0" fill="none" stroke="var(--accent)" stroke-width="2.2" stroke-linejoin="round" stroke-linecap="round"/><path d="M376.0,254.0 L398.0,221.3 L407.0,209.4 L415.0,199.9 L423.0,191.8 L430.0,185.9 L438.0,180.8 L445.0,177.8 L450.0,176.5 L455.0,176.0 L460.0,176.2 L465.0,177.2 L470.0,178.9 L475.0,181.4 L480.0,184.5 L485.0,188.3 L490.0,192.7 L496.0,198.8 L507.0,211.9 L519.0,228.4 L536.0,254.0 L551.0,231.4 L562.0,215.9 L572.0,203.3 L581.0,193.7 L590.0,185.9 L599.0,180.3 L604.0,178.2 L608.0,177.0 L616.0,176.0" fill="none" stroke="var(--hi)" stroke-width="2.2" stroke-dasharray="6 4" stroke-linejoin="round" stroke-linecap="round"/><text x="376.0" y="269.0" text-anchor="middle" fill="var(--muted)" style="font-size:10.5px;">0</text><text x="616.0" y="269.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">ℓ</text><text x="496.0" y="284.0" text-anchor="middle" fill="currentColor" style="font-size:11.5px;">ℓ = 3λ/4   (n = 1)</text><text x="370.0" y="162.0" text-anchor="end" fill="var(--muted)" style="font-size:10px;">open</text><text x="622.0" y="162.0" text-anchor="start" fill="var(--muted)" style="font-size:10px;">short</text><line x1="250.0" y1="300.0" x2="280.0" y2="300.0" stroke="var(--accent)" stroke-width="2.2" stroke-linecap="round"/><text x="286.0" y="304.0" text-anchor="start" fill="currentColor" style="font-size:12px;">|V|</text><line x1="340.0" y1="300.0" x2="370.0" y2="300.0" stroke="var(--hi)" stroke-width="2.2" stroke-dasharray="6 4" stroke-linecap="round"/><text x="376.0" y="304.0" text-anchor="start" fill="currentColor" style="font-size:12px;">|I|</text></svg><figcaption>Standing-wave envelopes of the two lowest resonances. Left, both ends open: the current is zero at both ends and a whole number of half wavelengths fits. Right, one end open and one shorted: the current is zero at the open end, the voltage at the short, and an odd number of quarter wavelengths fits. Voltage nulls sit on current maxima. With both ends shorted, swap the two curves of the left panel.</figcaption></figure>

## 3. A segment shorted at both ends

Now $V(0,t) = V(\ell,t) = 0$. The first condition gives $g = -f$, the second the same periodicity. The modes are those of §2 with voltage and current swapped:

$$
V_n\propto\sin(n\omega_0t+\theta_n)\,\sin(n\beta_0z),\qquad I_n\propto\cos(n\omega_0t+\theta_n)\,\cos(n\beta_0z),
$$

with the **same** frequencies $f_n = nv/2\ell$. The voltage vanishes at both ends; the current is largest there. The DC term is now a steady current circulating through the two shorts.

## 4. One end open, one end shorted

The notes' argument: the current must vanish at the open end and the voltage at the short, and the nulls of $\cos\beta z$ and $\sin\beta z$ are an odd number of quarter wavelengths apart.

> [!key] Resonances of an open–short segment (n = 0, 1, 2, …)
> $$
> \ell = (2n+1)\frac{\lambda}{4},\qquad f_n = (2n+1)\frac{v}{4\ell} = \frac{v}{2\ell}\Big(n+\frac12\Big),\qquad \omega_n = \frac{\pi v}{\ell}\Big(n+\frac12\Big).
> $$
> The lowest resonance is a **quarter** wave, at half the fundamental of the same segment with like ends. Only odd multiples of it appear.

> [!derivation]- The same result from f and g
> Open at $z = 0$: $g = f$. Short at $z = \ell$: $f(t-\ell/v)+f(t+\ell/v) = 0$, so $f(t+2\ell/v) = -f(t)$. The function changes sign after one round trip and repeats after two: its period is $4\ell/v$, and a function with $f(t+T/2) = -f(t)$ has only odd harmonics. Hence $\omega = (2n+1)\,2\pi/(4\ell/v) = (2n+1)\pi v/2\ell$. Physically, the short reflects with $\Gamma = -1$ and the open end with $+1$, so one round trip flips the sign.

| ends | condition on the line | resonant frequencies | lowest |
|---|---|---|---|
| open–open | $I = 0$ at both: $\ell = n\lambda/2$ | $nv/2\ell$, $n\ge1$ | $v/2\ell$ |
| short–short | $V = 0$ at both: $\ell = n\lambda/2$ | $nv/2\ell$, $n\ge1$ | $v/2\ell$ |
| open–short | $I = 0$ at one, $V = 0$ at the other: $\ell = (2n+1)\lambda/4$ | $(2n+1)v/4\ell$, $n\ge0$ | $v/4\ell$ |

> [!example] Slides, Lecture 31 (slide 12) — three standing-wave patterns on an open–short stub
> The patterns show a quarter, three quarters and five quarters of a cycle on the length $\ell$. In-class ink: (a) $\ell = \lambda_0/4$, so $\lambda_0 = 4\ell$ and $f_0 = v_p/4\ell$; (b) $\ell = 3\lambda/4$, $\lambda = 4\ell/3$, $f = 3v_p/4\ell$; (c) $\ell = 5\lambda/4$, $\lambda = 4\ell/5$, $f = 5v_p/4\ell$. In general $\lambda_n = 4\ell/(2n+1)$ and $f_n = (2n+1)v_p/4\ell$, the box above. Slides 11, 13 and 14 state the three cases with the end coefficients: open–short ($\Gamma = +1$ and $-1$), $\ell = \lambda/4, 3\lambda/4, \ldots$; open–open and short–short, $\ell = \lambda/2, \lambda, \ldots$ ("an even multiple of $\lambda/4$").

> [!recipe] Resonances from the end conditions
> 1. Translate each end: $\tilde I = 0$ (or "nothing connected") is an open, $\tilde V = 0$ is a short.
> 2. Like ends: fit half wavelengths, $\ell = n\lambda/2$. Unlike ends: fit odd quarter wavelengths.
> 3. $f = v/\lambda$; if $\omega$ is asked, multiply by $2\pi$.
> 4. Shapes: from an open end $\lvert V\rvert\propto\lvert\cos\beta z\rvert$ and $\lvert I\rvert\propto\lvert\sin\beta z\rvert$; from a short, the other way round. Sketch them and check both ends.

> [!trap] Resonances
> - "Lowest resonance" is $\lambda/2$ for like ends and $\lambda/4$ for unlike ends. Decide the ends first.
> - Index conventions differ: the notes count unlike-end modes from $n = 0$ with $(2n+1)$; exams often ask for "the first two" or "the three lowest". List them explicitly.
> - $\omega$ and $f$ differ by $2\pi$. Read which one is asked.
> - A voltage null is a current maximum, not a place where nothing happens.

## 5. Example 1 (notes): a 600 m segment, open at z = 0 and shorted at z = ℓ

$Z_0 = 50\ \Omega$, $v = c$.

**(a) Frequencies.** $600\ \text{m} = (2n+1)\lambda/4$ with $\lambda = c/f$:

$$
f_n = (2n+1)\frac{300\ \text{m}/\mu\text{s}}{4\cdot600\ \text{m}} = \frac{2n+1}{8}\ \text{MHz} = 0.125,\ 0.375,\ 0.625,\ \ldots\ \text{MHz}.
$$

**(b) Current modes.** They must vanish at the open end $z = 0$, so they are sines in $z$. With $\omega_n = 2\pi f_n = (2n+1)\tfrac\pi4$ rad/μs and $\beta_n = \omega_n/c = (2n+1)\tfrac{\pi}{1200}$ rad/m, for unit amplitude:

$$
I_n(z,t) = \sin\Big[(2n+1)\frac{\pi z}{1200}\Big]\sin\Big[(2n+1)\frac{\pi t}{4}\Big]\quad(z\text{ in m},\ t\text{ in }\mu\text{s}).
$$

**(c) Voltage modes.** From the telegrapher's equation $-\partial V/\partial z = \mathcal{L}\,\partial I/\partial t$, integrating in $z$:

$$
V_n(z,t) = \frac{\omega_n}{\beta_n}\mathcal{L}\,\cos\Big[(2n+1)\frac{\pi z}{1200}\Big]\cos\Big[(2n+1)\frac{\pi t}{4}\Big]
= Z_0\cos[\cdots]\cos[\cdots],
$$

because $(\omega/\beta)\mathcal{L} = v\mathcal{L} = Z_0$. A 1 A current mode goes with a 50 V voltage mode. Check: at $z = 600$ m the cosine is $\cos[(2n+1)\pi/2] = 0$, the short.

The amplitudes of $V$ and $I$ in a mode are tied by $Z_0$; they cannot be chosen separately. (The notes write the voltage amplitude as "$300\mathcal{L}$", with $v$ in m/μs; it is $v\mathcal{L} = Z_0$.)

## 6. How a source-free oscillation starts

One way: the line was connected to a source and then disconnected. The notes' example: a 3 V battery is switched onto the $z = 0$ end of a 600 m line with $v = c$ at $t = 0$ and switched out again at $t = 1$ μs; the far end is open.

- At $t = 1$ μs the front has travelled 300 m: $V = 3$ V and $I = 3/Z_0$ for $0<z<300$ m, zero beyond. This is a forward pulse 300 m long.
- From then on both ends are open, so everything on the line has period $T = 2\ell/v = 4$ μs and fundamental $\omega_0 = \pi/2$ rad/μs. $V$ and $I$ for $t>1$ μs are the sum of open–open modes that matches $V(z,1)$ and $I(z,1)$.

> [!example] What that sum looks like (this site's reading)
> The pulse keeps bouncing. Each open end reflects it with $\Gamma = +1$: the voltage keeps its sign and the current reverses. While the pulse is turning round at an end, incident and reflected parts overlap there: 6 V and no current. Any point of the line sees the same record every 4 μs. The average voltage along the line stays $3\ \text{V}\times300/600 = 1.5$ V, the DC term $2F_0$ of §2: the charge the battery delivered cannot leave.

The notes add a second source: resistors at temperature $T$ connected to a line leave thermal energy on it, shared among the resonant modes at about $kT$ per mode. This is thermal noise, and it limits how weak a signal can be received.

## 7. Summary

- A source-free lossless segment supports standing-wave **modes**; any periodic motion of the line is a sum of them.
- Like ends (open–open, short–short): $T = 2\ell/v$, $f_n = nv/2\ell$, $\ell = n\lambda/2$. Open–open: $I\propto\sin$, $V\propto\cos$ from either end. Short–short: swapped.
- Unlike ends: $f_n = (2n+1)v/4\ell$, $\ell = (2n+1)\lambda/4$; lowest is a quarter wave.
- In a mode, $\lvert V\rvert_{\max} = Z_0\lvert I\rvert_{\max}$; $V$ and $I$ are a quarter period apart in time and a quarter wavelength apart in space.
- Notes' example: 600 m, open–short, $v = c$: $\tfrac18$, $\tfrac38$, $\tfrac58$ MHz.
- Next, [[4-transmission-lines/32-input-impedance-and-microwave-resonators|Lecture 32]]: the same segment seen from its input terminals, as a circuit element with an impedance.

Concept pages: [[concepts/line-resonances]] · [[concepts/standing-waves]] · [[concepts/telegraphers-equations]] · [[concepts/characteristic-impedance]].

> [!exam] On exams
> SP19 Exam 3 #5 and FA23 Exam 3 #7 give two measurements in sinusoidal steady state, one at each end ($\tilde V = 0$ or $\tilde I = 0$), and ask for $Z_{\text{in}}$ and $Z_L$, the lowest two or three resonant frequencies, and (FA23) which plotted shapes are $\lvert\tilde V\rvert$ and $\lvert\tilde I\rvert$ and where the line looks like a short. The recipe of §4 is the whole method ([[exams/e3-sp19#5-resonances-from-two-measurements-15-points|SP19 guide]], [[exams/e3-fa23#7-resonances-and-standing-wave-shapes-16-points|FA23 guide]]). Lecture 31 is **not on FA26 Midterm 3**, which covers Lectures 1–30 ([[exams/index#the-scope|scope]]).

> [!tip] Practice this lecture
> [[practice/31-resonances-of-line-segments|8 practice problems]] — 4 easy, 2 medium, 2 hard — each with a folded hint and a worked solution. Start with [[practice/31-resonances-of-line-segments#311-the-three-lowest-three-ways|31.1 The three lowest, three ways]]; the [[practice/index|practice hub]] has the whole bank by difficulty and by topic.

### Sources for this page
Kudeki notes, Lecture 31 (9 pages): the open–open derivation and Fourier series, the mode formulas, the short–short and open–short cases, Example 1, the switched battery and the thermal-noise remark. Slides "Lecture 31: Frequency domain; Oscillations in Short and Open Stubs" (16 slides; annotated deck of Nov 9, ink on slides 4 and 12): slides 9–14 are this lecture's resonance conditions and the worked pattern example; slides 2–8 (phasors on the line, standing waves on shorted and open lines) are used on the Lecture 32 page, because the notes put them there; slides 15–16 open the Smith chart (Lecture 34, not written yet). The deck's page footers read "Lectures 32"; its title and file name say 31. This site's own: the round-trip argument, the $f$–$g$ derivation of the open–short case, the table and recipe, the reading of the battery example, the figure; numbers checked in `tools/build14/checks/L31_33.py`. The notes' "$300\mathcal{L}$" is on the errata page.
