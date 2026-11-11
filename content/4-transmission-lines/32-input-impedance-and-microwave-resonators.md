---
title: "Lecture 32 — Input impedance and microwave resonators"
description: "Seen from its input terminals in sinusoidal steady state, a shorted line of length ℓ is the impedance jZ₀ tan βℓ: an inductor, an open circuit, a capacitor or a short, depending on its length in wavelengths. Its zeros and poles are Lecture 31's resonances, now called series and parallel."
tags: [lecture, transmission-lines]
lecture: 32
---

*Lecture 32 · course notes §32 · slides "Lecture 31", slides 2–8, and "Lectures 32: Input Impedance; Microwave Resonators" (annotated deck, Nov 9, ink through slide 6) · prev: [[4-transmission-lines/31-periodic-oscillations-in-lossless-tl-circuits|Lecture 31]] · next: [[4-transmission-lines/33-half-wave-and-quarter-wave-transformers|Lecture 33]] · worked twin: [[exams/e3-steady-state-lines#s1-an-open-stub-that-blocks-the-source|An open stub that blocks the source]] · practice: [[practice/32-stubs-and-input-impedance|8 problems]]*

> [!abstract] In one breath
> Connect a shorted or open line segment (a **stub**) into a circuit running at one frequency and it acts as a two-terminal element. Its input impedance follows from the phasor waves on it, measured from the load: $Z(\ell) = jZ_0\tan\beta\ell$ for a short at the far end, $-jZ_0\cot\beta\ell$ for an open. It is purely reactive and repeats every half wavelength. Where it is zero the stub is in **series resonance** and looks like a short; where it is infinite it is in **parallel resonance** and looks like an open. These are the resonances of Lecture 31, seen from the terminals.

## 1. Two LC resonators to compare with

A series LC pair has impedance $Z_s = j(\omega L-1/\omega C)$; a parallel pair has admittance $Y_p = j(\omega C-1/\omega L)$. Both vanish at $\omega_0 = 1/\sqrt{LC}$:

- **series resonance:** $Z = 0$, the element is a short circuit at that frequency;
- **parallel resonance:** $Y = 0$, the element is an open circuit: it draws no current.

A stub has both kinds, infinitely many of each.

## 2. The resonances of a shorted stub, seen from its input

Take a line of length $\ell$ with a short at the far end, and look into the other end.

- If the source frequency is one where the segment would ring with its input end **open**, $\omega_n = (2n+1)\pi v/2\ell$ (odd quarter wavelengths, [[4-transmission-lines/31-periodic-oscillations-in-lossless-tl-circuits#4-one-end-open-one-end-shorted|Lecture 31 §4]]), the stub carries its standing wave without drawing current: $Y(\ell) = 0$. **Parallel resonance.**
- If the frequency is one where it would ring with its input end **shorted**, $\omega_n = n\pi v/\ell$ (whole half wavelengths), the standing wave has zero voltage at the input: $Z(\ell) = 0$. **Series resonance.**

Along the frequency axis they alternate: parallel at $v/4\ell$, series at $v/2\ell$, parallel at $3v/4\ell$, and so on. The rest of the lecture finds $Z(\ell)$ in between.

## 3. Phasors on the line, measured from the load

At one frequency $\omega$ the two travelling waves of [[4-transmission-lines/27-guided-tem-waves-on-transmission-lines|Lecture 27]] are co-sinusoids, with phasors

$$
\tilde V(z) = V^+e^{-j\beta z}+V^-e^{j\beta z},\qquad \tilde I(z) = \frac{V^+e^{-j\beta z}-V^-e^{j\beta z}}{Z_0},\qquad \beta = \frac\omega v = \omega\sqrt{\mathcal{L}\mathcal{C}} .
$$

$V^+$ and $V^-$ are complex constants. Impedance is a frequency-domain idea, so phasors are needed from here on. Two changes of bookkeeping make the algebra short: put the origin at the **load** end, and measure $d = -z$ from there back toward the input.

> [!key] Voltage and current phasors at distance d from the load
> $$
> \tilde V(d) = V^+e^{j\beta d}+V^-e^{-j\beta d},\qquad
> \tilde I(d) = \frac{V^+e^{j\beta d}-V^-e^{-j\beta d}}{Z_0},\qquad
> Z(d) = \frac{\tilde V(d)}{\tilde I(d)} .
> $$
> $d = 0$ is the load, $d = \ell$ the input. $V^+e^{j\beta d}$ is the wave travelling **toward the load**; $V^-e^{-j\beta d}$ is the reflected one, and it still carries current $-V/Z_0$.

> [!trap] Two coordinates
> Bounce diagrams use $z$ from the generator. Steady-state problems use $d$ from the load, and $e^{+j\beta d}$ is the wave going toward $+z$. The time-domain $\Gamma_L = (R_L-Z_0)/(R_L+Z_0)$ of [[4-transmission-lines/28-distributed-circuits-and-bounce-diagrams|Lecture 28]] is the same number as $V^-/V^+$ here.

## 4. The shorted stub

The short forces $\tilde V(0) = V^++V^- = 0$, so $V^- = -V^+$ (that is $\Gamma_L = -1$):

$$
\tilde V(d) = j2V^+\sin\beta d,\qquad \tilde I(d) = \frac{2V^+}{Z_0}\cos\beta d .
$$

A pure standing wave: voltage zero at the short and every $\lambda/2$ from it, current largest there. The notes write $Y_0\equiv1/Z_0$, the characteristic admittance.

**Slides, Lecture 31 (slides 4–6): the same wave in time.** With $V^+ = \lvert V^+\rvert e^{j\theta}$: $V(d,t) = -2\lvert V^+\rvert\sin\beta d\,\sin(\omega t+\theta)$ and $I(d,t) = 2Y_0\lvert V^+\rvert\cos\beta d\,\cos(\omega t+\theta)$. Their product is the power flowing at $d$: $P(d,t) = -Y_0\lvert V^+\rvert^2\sin2\beta d\,\sin2(\omega t+\theta)$. It swings at $2\omega$ with zero average at every point, and is zero at all times at the nulls of $V$ and of $I$, every $\lambda/4$. The slides call $Z(d) = jZ_0\tan\beta d$ the *line impedance*: the impedance seen at $d$ looking toward the load.

> [!key] Input impedance of a shorted stub
> $$
> Z(\ell) = jZ_0\tan\beta\ell,\qquad Y(\ell) = -jY_0\cot\beta\ell,\qquad \beta\ell = \frac{2\pi\ell}{\lambda} = \frac{\omega\ell}{v}.
> $$

Reading it:
1. It is purely reactive, $Z = jX$, for every length: a lossless stub absorbs no average power.
2. $0<\ell<\lambda/4$: $X>0$, **inductive**.
3. $\lambda/4<\ell<\lambda/2$: $X<0$, **capacitive**.
4. It repeats every $\lambda/2$ in $\ell$, and between 0 and $\lambda/2$ it takes every reactance from $-\infty$ to $+\infty$: one stub can stand in for any inductor or capacitor at one frequency.
5. $\ell\ll\lambda/4$: $\tan\beta\ell\approx\beta\ell$, so $Z\approx jZ_0\beta\ell = j\omega\mathcal{L}\ell$. A short piece of shorted line is the inductor $\mathcal{L}\ell$.
6. $\ell = \lambda/4$: $Y = 0$. A quarter-wave shorted stub looks like an **open circuit**.
7. $\ell = \lambda/2$: $Z = 0$ again.

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 300" width="640" height="300" role="img" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:14px"><defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="context-stroke"/></marker><marker id="ahs" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="context-stroke"/></marker></defs><rect x="60.0" y="32.0" width="132.5" height="236.0" fill="var(--accent)" fill-opacity="0.07" stroke="none"/><text x="126.2" y="45.0" text-anchor="middle" fill="var(--muted)" style="font-size:10.5px;">inductive</text><rect x="192.5" y="32.0" width="132.5" height="236.0" fill="var(--accent2)" fill-opacity="0.07" stroke="none"/><text x="258.8" y="45.0" text-anchor="middle" fill="var(--muted)" style="font-size:10.5px;">capacitive</text><rect x="325.0" y="32.0" width="132.5" height="236.0" fill="var(--accent)" fill-opacity="0.07" stroke="none"/><text x="391.2" y="45.0" text-anchor="middle" fill="var(--muted)" style="font-size:10.5px;">inductive</text><rect x="457.5" y="32.0" width="132.5" height="236.0" fill="var(--accent2)" fill-opacity="0.07" stroke="none"/><text x="523.8" y="45.0" text-anchor="middle" fill="var(--muted)" style="font-size:10.5px;">capacitive</text><line x1="60.0" y1="150.0" x2="604.0" y2="150.0" stroke="currentColor" stroke-width="1.3" marker-end="url(#ah)" stroke-linecap="round"/><text x="610.0" y="154.0" text-anchor="start" fill="currentColor" style="font-size:13px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">ℓ</text><line x1="60.0" y1="268.0" x2="60.0" y2="20.0" stroke="currentColor" stroke-width="1.3" marker-end="url(#ah)" stroke-linecap="round"/><text x="60.0" y="14.0" text-anchor="middle" fill="currentColor" style="font-size:12px;">X / Z₀</text><line x1="192.5" y1="147.0" x2="192.5" y2="153.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><text x="204.5" y="165.0" text-anchor="middle" fill="var(--muted)" style="font-size:10.5px;">λ/4</text><line x1="325.0" y1="147.0" x2="325.0" y2="153.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><text x="337.0" y="165.0" text-anchor="middle" fill="var(--muted)" style="font-size:10.5px;">λ/2</text><line x1="457.5" y1="147.0" x2="457.5" y2="153.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><text x="469.5" y="165.0" text-anchor="middle" fill="var(--muted)" style="font-size:10.5px;">3λ/4</text><line x1="590.0" y1="147.0" x2="590.0" y2="153.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><text x="602.0" y="165.0" text-anchor="middle" fill="var(--muted)" style="font-size:10.5px;">λ</text><line x1="57.0" y1="209.0" x2="63.0" y2="209.0" stroke="currentColor" stroke-width="1.0" stroke-linecap="round"/><text x="52.0" y="213.0" text-anchor="end" fill="var(--muted)" style="font-size:10px;">−2</text><line x1="57.0" y1="179.5" x2="63.0" y2="179.5" stroke="currentColor" stroke-width="1.0" stroke-linecap="round"/><text x="52.0" y="183.5" text-anchor="end" fill="var(--muted)" style="font-size:10px;">−1</text><line x1="57.0" y1="120.5" x2="63.0" y2="120.5" stroke="currentColor" stroke-width="1.0" stroke-linecap="round"/><text x="52.0" y="124.5" text-anchor="end" fill="var(--muted)" style="font-size:10px;">+1</text><line x1="57.0" y1="91.0" x2="63.0" y2="91.0" stroke="currentColor" stroke-width="1.0" stroke-linecap="round"/><text x="52.0" y="95.0" text-anchor="end" fill="var(--muted)" style="font-size:10px;">+2</text><line x1="192.5" y1="268.0" x2="192.5" y2="32.0" stroke="var(--accent)" stroke-width="0.8" stroke-dasharray="2 4" stroke-linecap="round"/><line x1="457.5" y1="268.0" x2="457.5" y2="32.0" stroke="var(--accent)" stroke-width="0.8" stroke-dasharray="2 4" stroke-linecap="round"/><line x1="325.0" y1="268.0" x2="325.0" y2="32.0" stroke="var(--hi)" stroke-width="0.8" stroke-dasharray="2 4" stroke-linecap="round"/><line x1="590.0" y1="268.0" x2="590.0" y2="32.0" stroke="var(--hi)" stroke-width="0.8" stroke-dasharray="2 4" stroke-linecap="round"/><path d="M60.1,150.0 L90.7,138.8 L101.6,134.1 L111.2,129.5 L119.9,124.6 L127.6,119.5 L134.5,114.1 L140.6,108.3 L146.2,101.8 L151.2,94.7 L155.7,86.7 L159.7,78.1 L163.2,68.4 L166.4,57.6 L169.2,45.9 L171.7,32.6" fill="none" stroke="var(--accent)" stroke-width="2.2" stroke-linejoin="round" stroke-linecap="round"/><path d="M213.2,267.8 L216.1,252.6 L219.4,239.3 L223.3,227.3 L227.6,216.7 L232.5,207.4 L238.2,199.0 L244.7,191.4 L252.1,184.5 L258.9,179.4 L266.6,174.5 L275.2,169.8 L285.0,165.1 L304.2,157.4 L351.8,140.3 L363.5,135.5 L373.6,130.8 L383.2,125.7 L391.6,120.2 L399.1,114.5 L405.7,108.2 L411.2,101.7 L416.3,94.5 L420.8,86.6 L424.8,77.9 L428.3,68.1 L431.5,57.3 L434.3,45.5 L436.8,32.2" fill="none" stroke="var(--accent)" stroke-width="2.2" stroke-linejoin="round" stroke-linecap="round"/><path d="M478.3,267.4 L480.8,254.1 L483.6,242.4 L486.8,231.6 L490.3,221.9 L494.3,213.3 L498.8,205.3 L503.8,198.2 L509.4,191.7 L515.5,185.9 L522.4,180.5 L530.1,175.4 L538.8,170.5 L548.4,165.9 L559.3,161.2 L589.9,150.0" fill="none" stroke="var(--accent)" stroke-width="2.2" stroke-linejoin="round" stroke-linecap="round"/><path d="M80.7,267.7 L83.6,252.5 L86.9,239.2 L90.8,227.2 L95.2,216.6 L100.1,207.4 L105.8,198.9 L112.2,191.4 L119.7,184.5 L126.4,179.4 L134.1,174.5 L142.7,169.8 L152.5,165.1 L171.7,157.4 L219.2,140.4 L230.9,135.5 L241.1,130.8 L250.7,125.7 L259.2,120.2 L266.6,114.4 L273.2,108.2 L278.8,101.7 L283.8,94.5 L288.3,86.5 L292.3,77.8 L295.9,68.0 L299.0,57.2 L301.8,45.4 L304.3,32.0" fill="none" stroke="var(--hi)" stroke-width="2.0" stroke-dasharray="6 4" stroke-linejoin="round" stroke-linecap="round"/><path d="M345.7,268.0 L348.2,254.6 L351.0,242.8 L354.1,232.0 L357.7,222.2 L361.7,213.5 L366.2,205.5 L371.2,198.3 L376.8,191.8 L383.4,185.6 L390.8,179.8 L399.3,174.3 L408.9,169.2 L419.1,164.5 L430.8,159.6 L478.3,142.6 L497.5,134.9 L507.3,130.2 L515.9,125.5 L523.6,120.6 L530.3,115.5 L537.8,108.6 L544.2,101.1 L549.9,92.6 L554.8,83.4 L559.2,72.8 L563.1,60.8 L566.4,47.5 L569.3,32.3" fill="none" stroke="var(--hi)" stroke-width="2.0" stroke-dasharray="6 4" stroke-linejoin="round" stroke-linecap="round"/><line x1="80.0" y1="286.0" x2="110.0" y2="286.0" stroke="var(--accent)" stroke-width="2.2" stroke-linecap="round"/><text x="116.0" y="290.0" text-anchor="start" fill="currentColor" style="font-size:11.5px;">shorted stub:  X = Z₀ tan βℓ</text><line x1="340.0" y1="286.0" x2="370.0" y2="286.0" stroke="var(--hi)" stroke-width="2.0" stroke-dasharray="6 4" stroke-linecap="round"/><text x="376.0" y="290.0" text-anchor="start" fill="currentColor" style="font-size:11.5px;">open stub:  X = −Z₀ cot βℓ</text></svg><figcaption>Input reactance of a stub against its length (the band labels are for the shorted stub). The shorted stub starts as an inductor, becomes an open circuit at λ/4, is capacitive up to λ/2 and is a short circuit again there. The open stub is the same curve shifted by λ/4. Everything repeats every λ/2.</figcaption></figure>

**The open stub.** With an open at $d = 0$ the current vanishes there, $V^- = +V^+$:

$$
\tilde V(d) = 2V^+\cos\beta d,\qquad \tilde I(d) = \frac{j2V^+}{Z_0}\sin\beta d,\qquad Z(\ell) = -jZ_0\cot\beta\ell .
$$

Everything shifts by a quarter wavelength: capacitive first (a short open stub is the capacitor $\mathcal{C}\ell$), a **short circuit** at $\ell = \lambda/4$, inductive up to $\lambda/2$, an open circuit there. The notes reach the quarter-wave statement by the argument of items 6 and 7; the formula is the same two lines with the other end condition.

| stub length | shorted stub | open stub |
|---|---|---|
| $0<\ell<\lambda/4$ | inductive | capacitive |
| $\ell = \lambda/4$ | open circuit (parallel resonance) | short circuit (series resonance) |
| $\lambda/4<\ell<\lambda/2$ | capacitive | inductive |
| $\ell = \lambda/2$ | short circuit (series resonance) | open circuit (parallel resonance) |

> [!trap] Stubs
> - $\beta\ell$ depends on frequency. The same stub is $\lambda/4$ at one frequency and $\lambda/2$ at twice that: an open circuit becomes a short.
> - A stub at parallel resonance draws no current from the circuit, yet current flows **inside** it: $\lvert\tilde I\rvert$ is largest a quarter wave from the input.
> - Inductive or capacitive is the sign of $X$ at one frequency. A stub is not an inductor at all frequencies.
> - $\tan$ for the shorted stub, $-\cot$ for the open one. Check with the short-length limit: a shorted hairpin is an inductor.

## 5. Stubs as circuit elements: the notes' examples

> [!example] Example 1 (notes) — a stub in series with a load
> A shorted stub, $\ell = 3$ m, $Z_0 = 50\ \Omega$, $v = c$, in series with $R_L = 50\ \Omega$ and a source $\tilde F$. By voltage division,
> $$
> H(\omega) = \frac{\tilde V_L}{\tilde F} = \frac{R_L}{R_L+jZ_0\tan\beta\ell} = \frac{1}{1+j\tan(\omega\ell/c)} .
> $$
> Because $R_L = Z_0$ here, $\lvert H\rvert = \lvert\cos(\omega\ell/c)\rvert$ (this site's simplification). $\lvert H\rvert = 1$ at the stub's series resonances, $f = nc/2\ell = 0, 50, 100,\ldots$ MHz, where it is a short. $\lvert H\rvert = 0$ at its parallel resonances, $f = (2n+1)c/4\ell = 25, 75, 125,\ldots$ MHz, where it is an open. A comb filter.

> [!example] Example 2 (notes) — a stub with an inductor
> **In series:** $Z = j\omega L+jZ_0\tan(\omega\sqrt{\mathcal{L}\mathcal{C}}\,\ell)$. Series resonances are its zeros: they move, because the inductor adds reactance. Parallel resonances are the poles of the tangent: a finite added term cannot move them. **In parallel:** add admittances, $Y = 1/j\omega L+1/jZ_0\tan(\cdot)$. Now the parallel resonances ($Y = 0$) move and the series ones ($Y = \infty$) stay. $Y = 0$ is the same equation as $Z = 0$ of the series connection, so the shifted frequencies are the same in both.

> [!example] Example 3 (notes) — a stub, a capacitor and a load in series
> Example 1 with $C = 10$ pF added in series:
> $$
> H(\omega) = \frac{R_L}{R_L+\dfrac{1}{j\omega C}+jZ_0\tan\beta\ell} = \frac{1}{1+\dfrac{1}{j\omega R_LC}+j\tan(\omega\ell/c)} .
> $$
> $\lvert H\rvert = 1$ where the two reactances cancel, $Z_0\tan(\omega\ell/c) = 1/\omega C$: the series resonances, shifted up from 0, 50 and 100 MHz to 23.8, 71.5 and 119.3 MHz for the first three. The nulls stay at 25, 75, 125 MHz, and the capacitor adds one at DC. Sliding the short along the stub retunes the filter.

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 250" width="640" height="250" role="img" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:14px"><defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="context-stroke"/></marker><marker id="ahs" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="context-stroke"/></marker></defs><line x1="60.0" y1="196.0" x2="604.0" y2="196.0" stroke="currentColor" stroke-width="1.3" marker-end="url(#ah)" stroke-linecap="round"/><text x="608.0" y="200.0" text-anchor="start" fill="currentColor" style="font-size:13px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">f</text><line x1="60.0" y1="196.0" x2="60.0" y2="22.0" stroke="currentColor" stroke-width="1.3" marker-end="url(#ah)" stroke-linecap="round"/><text x="66.0" y="20.0" text-anchor="start" fill="currentColor" style="font-size:12px;">|H|</text><line x1="148.3" y1="193.0" x2="148.3" y2="199.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><text x="148.3" y="211.0" text-anchor="middle" fill="var(--muted)" style="font-size:10.5px;">50</text><line x1="236.7" y1="193.0" x2="236.7" y2="199.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><text x="236.7" y="211.0" text-anchor="middle" fill="var(--muted)" style="font-size:10.5px;">100</text><line x1="325.0" y1="193.0" x2="325.0" y2="199.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><text x="325.0" y="211.0" text-anchor="middle" fill="var(--muted)" style="font-size:10.5px;">150</text><line x1="413.3" y1="193.0" x2="413.3" y2="199.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><text x="413.3" y="211.0" text-anchor="middle" fill="var(--muted)" style="font-size:10.5px;">200</text><line x1="501.7" y1="193.0" x2="501.7" y2="199.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><text x="501.7" y="211.0" text-anchor="middle" fill="var(--muted)" style="font-size:10.5px;">250</text><line x1="590.0" y1="193.0" x2="590.0" y2="199.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><text x="590.0" y="211.0" text-anchor="middle" fill="var(--muted)" style="font-size:10.5px;">300</text><text x="325.0" y="228.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px;">MHz</text><line x1="57.0" y1="116.0" x2="63.0" y2="116.0" stroke="currentColor" stroke-width="1.0" stroke-linecap="round"/><text x="52.0" y="120.0" text-anchor="end" fill="var(--muted)" style="font-size:10px;">0.5</text><line x1="57.0" y1="36.0" x2="63.0" y2="36.0" stroke="currentColor" stroke-width="1.0" stroke-linecap="round"/><text x="52.0" y="40.0" text-anchor="end" fill="var(--muted)" style="font-size:10px;">1</text><line x1="60.0" y1="36.0" x2="590.0" y2="36.0" stroke="var(--muted)" stroke-width="0.7" stroke-dasharray="2 4" stroke-linecap="round"/><path d="M60.1,36.0 L62.4,36.6 L64.8,38.3 L67.2,41.2 L69.5,45.1 L74.4,56.5 L79.4,72.7 L84.6,93.2 L90.0,118.9 L104.2,196.0 L117.8,121.6 L123.1,96.4 L127.9,76.3 L132.7,60.1 L137.4,48.0 L141.9,40.2 L144.2,37.7 L146.4,36.4 L148.9,36.0 L151.3,36.9 L153.8,39.0 L156.4,42.5 L158.9,47.2 L161.5,53.2 L166.7,69.0 L172.0,89.4 L177.7,115.9 L184.0,148.5 L192.5,196.0 L205.6,124.3 L210.7,99.5 L215.4,79.7 L220.0,63.4 L224.5,50.8 L228.8,42.2 L231.0,39.2 L233.1,37.3 L235.8,36.1 L238.3,36.3 L240.9,37.8 L243.6,40.8 L246.2,45.1 L248.9,50.8 L254.2,66.3 L259.7,86.8 L265.6,113.7 L272.1,147.0 L280.8,196.0 L289.9,145.1 L296.6,110.7 L302.8,83.2 L308.6,62.5 L311.5,54.1 L314.3,47.4 L317.1,42.2 L319.9,38.6 L322.6,36.6 L325.4,36.0 L328.1,37.0 L330.8,39.4 L334.9,45.8 L339.0,55.3 L343.2,68.4 L347.5,84.7 L351.9,104.0 L356.7,127.4 L369.2,196.0 L377.7,148.0 L384.1,115.0 L389.8,88.7 L395.2,68.1 L400.5,52.3 L403.2,46.3 L405.7,41.8 L408.3,38.6 L410.9,36.6 L413.3,36.0 L415.9,36.7 L418.1,38.3 L420.3,40.9 L424.8,49.2 L429.4,61.4 L434.1,77.7 L438.9,97.5 L444.1,122.5 L457.5,196.0 L466.0,148.5 L472.2,116.3 L477.8,90.2 L483.1,69.6 L488.3,53.7 L490.9,47.6 L493.4,42.9 L495.8,39.4 L498.3,37.1 L500.8,36.1 L503.3,36.3 L505.5,37.5 L507.8,39.7 L510.1,43.1 L512.4,47.4 L517.0,59.3 L521.9,75.7 L526.8,96.0 L532.1,121.1 L545.8,196.0 L560.0,118.9 L565.4,93.2 L570.6,72.7 L575.6,56.5 L580.5,45.1 L582.8,41.2 L585.2,38.3 L587.6,36.6 L590.0,36.0" fill="none" stroke="var(--accent)" stroke-width="2.2" stroke-linejoin="round" stroke-linecap="round"/><path d="M60.1,196.0 L81.3,189.7 L91.6,185.8 L94.7,184.0 L96.8,182.2 L98.4,179.8 L99.5,176.8 L100.8,167.1 L101.4,150.1 L102.0,37.5 L102.6,161.0 L103.1,184.2 L104.2,196.0 L105.0,192.4 L106.2,189.8 L107.9,187.7 L110.3,185.8 L118.1,182.2 L147.4,171.6 L159.2,166.1 L164.9,162.6 L169.4,159.0 L173.1,154.9 L175.9,150.4 L178.2,144.9 L180.0,138.1 L181.5,129.6 L182.7,119.4 L184.3,93.6 L186.3,36.0 L189.0,152.7 L190.4,178.2 L192.5,196.0 L194.2,188.4 L196.4,181.9 L199.2,176.5 L202.7,171.9 L206.5,168.3 L211.1,164.6 L232.7,150.8 L241.9,143.9 L246.2,139.8 L249.9,135.6 L253.2,130.9 L255.9,125.9 L258.4,120.2 L260.6,113.5 L264.1,97.2 L266.3,80.5 L269.7,42.3 L270.8,36.0 L271.4,39.2 L272.1,50.6 L274.6,120.0 L276.2,151.6 L278.3,177.0 L280.8,196.0 L283.0,185.9 L285.6,176.9 L288.8,169.3 L292.8,162.2 L296.6,157.0 L301.2,151.6 L319.3,133.8 L326.6,125.9 L333.1,117.0 L338.4,107.3 L342.8,96.4 L346.4,83.6 L349.5,68.4 L353.9,41.1 L354.8,37.3 L355.5,36.0 L356.1,36.7 L356.7,39.5 L357.9,52.0 L362.0,123.9 L364.3,156.1 L366.5,177.8 L369.2,196.0 L371.6,183.9 L374.5,173.5 L377.9,163.9 L382.0,155.2 L385.8,148.5 L390.4,141.6 L406.6,120.4 L412.7,111.8 L418.3,102.6 L423.0,93.2 L426.4,84.7 L429.5,75.5 L432.7,64.1 L438.2,41.6 L439.5,37.6 L440.5,36.1 L441.4,36.5 L442.3,39.0 L444.0,50.3 L451.7,149.8 L454.4,175.2 L457.5,196.0 L460.0,183.5 L462.8,172.2 L466.0,162.0 L469.7,152.4 L473.4,144.4 L477.8,136.2 L497.2,104.9 L505.6,89.4 L512.4,73.7 L522.7,42.3 L524.4,38.2 L525.7,36.3 L526.4,36.0 L527.1,36.4 L528.3,38.9 L529.6,44.3 L530.8,52.7 L539.8,151.3 L542.7,175.9 L545.8,196.0 L548.7,181.6 L551.8,168.9 L555.3,157.2 L559.4,145.8 L567.9,127.4 L590.0,86.3" fill="none" stroke="var(--hi)" stroke-width="2.0" stroke-dasharray="6 4" stroke-linejoin="round" stroke-linecap="round"/><line x1="80.0" y1="240.0" x2="110.0" y2="240.0" stroke="var(--accent)" stroke-width="2.2" stroke-linecap="round"/><text x="116.0" y="244.0" text-anchor="start" fill="currentColor" style="font-size:11.5px;">stub + 50 Ω  (Example 1)</text><line x1="330.0" y1="240.0" x2="360.0" y2="240.0" stroke="var(--hi)" stroke-width="2.0" stroke-dasharray="6 4" stroke-linecap="round"/><text x="366.0" y="244.0" text-anchor="start" fill="currentColor" style="font-size:11.5px;">stub + 10 pF + 50 Ω  (Example 3)</text></svg><figcaption>Amplitude response of the notes' two filters, a 3 m shorted air line (Z₀ = 50 Ω) in series with a 50 Ω load. Without the capacitor the response is |cos(2πfℓ/c)|: full transmission at the stub's series resonances (0, 50, 100 MHz, …) and none at its parallel resonances (25, 75, 125 MHz, …). The series capacitor moves the peaks up and blocks DC, and leaves the nulls where they were.</figcaption></figure>

> [!example] Example 4 (notes) — reading a length from a current
> A source $2\angle0^\circ$ A drives a 50 Ω resistor in parallel with the input of an **open-ended** line. (a) If the resistor current is $\tilde I_R = 2\angle0^\circ$ A, the line takes none: $\tilde I(\ell) = 0$, an open at the input. The far end is open too, so $\ell$ is a whole number of half wavelengths. (b) If $\tilde I_R = 0$, then $\tilde V(\ell) = 50\,\tilde I_R = 0$: a short at the input, an open at the far end, so $\ell$ is an odd number of quarter wavelengths. Both agree with $Z(\ell) = -jZ_0\cot\beta\ell$.

> [!example] Slides, Lecture 32 (slide 5) — finding a short with a signal generator and an ammeter
> A line is shorted somewhere along its length. Sweep the source frequency up from zero and watch the input current. It first vanishes when the faulty section is a quarter wave long and looks like an open circuit: $\ell = \lambda/4 = v/4f_1$ (inked in class). The zeros then repeat every $v/2\ell$. This site's numbers: $v = 2\times10^8$ m/s and a first zero at 1.33 MHz put the short 37.5 m away. The slide asks you to compare with time-domain reflectometry ([[4-transmission-lines/30-multi-line-circuits#2-a-bounce-diagram-across-two-lines|Lecture 30]]): the same distance from an echo delay, $\ell = vT$.

> [!example] Slides, Lecture 32 (slides 17, 21–22) — Examples 1 and 4, with numbers
> These slides carried no ink when the deck was copied; the answers are worked here.
> - **Example 1.** (a) Shorted load, $v = c$, $\ell = 3$ m: parallel resonances at $(2n+1)c/4\ell = 25, 75, 125$ MHz. (b) A 10 m line open at both ends with $v = \tfrac23c$: $nv/2\ell = 10, 20, 30,\ldots$ MHz.
> - **Example 4** is the notes' Example 4 with $v_p = 10^8$ m/s, $Z_0 = 50\ \Omega$ and $\omega = \pi\times10^8$ rad/s, so $\lambda = 2$ m. The open end forces $\tilde I(0) = 0$, and the stub carries a standing wave for every length. $\tilde I_R = 2\angle0^\circ$ A needs $\ell = n\lambda/2$, smallest 1 m; then $\tilde V(\ell) = 100$ V, $\tilde V(\ell/2) = 0$ and $\tilde I(\ell/2) = -j2$ A, not zero. $\tilde I_R = 0$ needs an odd number of quarter waves, smallest 0.5 m. A current null at mid-line needs $\sin(\beta\ell/2) = 0$, smallest $\ell = \lambda = 2$ m.
> - Their Example 2 is the notes' Example 3 above; their Example 3 swaps in an open stub, $Z = R_L+1/j\omega C-jZ_0\cot\beta\ell$.

> [!recipe] A stub in a circuit
> 1. $\lambda = v/f$ on the stub. Express $\ell$ in wavelengths; $\beta\ell = 2\pi\ell/\lambda$.
> 2. $Z(\ell) = jZ_0\tan\beta\ell$ (shorted) or $-jZ_0\cot\beta\ell$ (open). Then treat the stub as that impedance and solve the circuit.
> 3. Backward: a measured zero current into the stub means $Z(\ell) = \infty$; zero voltage across it means $Z(\ell) = 0$. Solve for $\ell$ in wavelengths, keeping the whole family ($+\,n\lambda/2$).
> 4. Adding an element: in series it cannot change an open circuit ($\infty+Z = \infty$); in parallel it cannot change a short.

## 6. Summary

- Measure $d$ from the load: $\tilde V(d) = V^+e^{j\beta d}+V^-e^{-j\beta d}$, $\tilde I(d) = (V^+e^{j\beta d}-V^-e^{-j\beta d})/Z_0$.
- Shorted stub: $\tilde V = j2V^+\sin\beta d$, $\tilde I = (2V^+/Z_0)\cos\beta d$, $Z(\ell) = jZ_0\tan\beta\ell$. Open stub: $\cos$ and $\sin$ swap, $Z(\ell) = -jZ_0\cot\beta\ell$.
- Purely reactive, period $\lambda/2$. Short stubs: shorted $\to$ inductor $\mathcal{L}\ell$, open $\to$ capacitor $\mathcal{C}\ell$.
- Series resonance: $Z(\ell) = 0$. Parallel resonance: $Y(\ell) = 0$. A quarter-wave shorted stub is an open circuit; a quarter-wave open stub is a short.
- Notes' filter: 3 m shorted air stub with 50 Ω: peaks every 50 MHz from 0, nulls at 25, 75, … MHz.
- Next, [[4-transmission-lines/33-half-wave-and-quarter-wave-transformers|Lecture 33]]: any load, with the line a multiple of $\lambda/4$.

Concept pages: [[concepts/stub-input-impedance]] · [[concepts/line-resonances]] · [[concepts/standing-waves]] · [[concepts/characteristic-impedance]].

> [!exam] On exams
> SP17 Exam 3 #6 and SP18 Exam 3 #4(a): a shorted line in series with a resistor and a source; the resistor current is zero. Find $\lambda$, $Z(\ell)$, the shortest $\ell$ or all possible $\lambda$, whether a voltage null can sit at mid-line, and whether an added element must go in series or in parallel (recipe steps 3 and 4). SP18 #1(viii)–(x): $\tilde I(d)$ on a shorted line, and $Z_{\text{in}}$ at twice and at half the lowest series-resonance frequency: rescale $\beta\ell$ with $\omega$. Guides: [[exams/e3-sp17#6-a-shorted-line-in-series-with-a-resistor-11-points|SP17 #6]], [[exams/e3-sp18#4-a-line-in-series-with-a-resistor-20-points|SP18 #4]]. Lecture 32 is **not on FA26 Midterm 3**, which covers Lectures 1–30 ([[exams/index#the-scope|scope]]).

> [!tip] Practice this lecture
> [[practice/32-stubs-and-input-impedance|8 practice problems]] — 4 easy, 2 medium, 2 hard — each with a folded hint and a worked solution. Start with [[practice/32-stubs-and-input-impedance#321-five-stubs|32.1 Five stubs]]; the [[practice/index|practice hub]] has the whole bank by difficulty and by topic.

### Sources for this page
Kudeki notes, Lecture 32 (10 pages): the LC comparison, parallel and series resonance of the shorted stub, the phasor waves and the $d$ coordinate, $Z(\ell) = jZ_0\tan\beta\ell$ with its seven remarks, Examples 1–4. Slides: "Lecture 31" slides 2–8 (phasors measured from the load, standing waves and power on shorted and open lines; ink on slide 4) and "Lectures 32: Input Impedance; Microwave Resonators" (23 slides, 25 pages in the annotated deck of Nov 9; ink on slides 2–6; slide 6, a Smith-chart exercise, appears three times): input impedance and the reactance curve (2–4, 7–9), the fault-finding example (5), series and parallel resonance in four cases (12–16), Examples 1–4 (17–22). The Smith-chart slides belong to Lecture 34, not written yet. The deck's page footers read "Lectures 33"; its title and file name say 32. This site's own: the open-stub formulas written out, the table, the $\lvert\cos\rvert$ form and the shifted peak values, the recipe, the figures; numbers checked in `tools/build14/checks/L31_33.py`.
